#!/usr/bin/env bash
# CERG SBOM Generation — CI/CD Integration Snippet
# Usage: source this in your pipeline or call as standalone script
# Generates CycloneDX SBOM, scans for vulns/license/secrets, signs, publishes
# Requires: syft, grype, trivy, cosign, jq (install in CI image)

set -euo pipefail

# ── Config (override via env) ──
PROJECT_NAME="${PROJECT_NAME:-$(basename "$PWD")}"
VERSION="${VERSION:-$(git describe --tags --always --dirty 2>/dev/null || echo "dev")}"
SBOM_OUTPUT_DIR="${SBOM_OUTPUT_DIR:-./sbom-output}"
COSIGN_KEY="${COSIGN_KEY:-}"  # Path to cosign private key, or use keyless
REGISTRY_URL="${REGISTRY_URL:-}"  # Optional OCI registry for SBOM artifact
FAIL_ON_CRITICAL="${FAIL_ON_CRITICAL:-true}"
FAIL_ON_HIGH="${FAIL_ON_HIGH:-true}"
FAIL_ON_SECRETS="${FAIL_ON_SECRETS:-true}"

# ── Helpers ──
log() { echo "[CERG-SBOM] $*"; }
die() { log "ERROR: $*"; exit 1; }

# ── Ensure tools ──
for cmd in syft grype cosign jq; do
    command -v "$cmd" >/dev/null || die "$cmd not found in PATH"
done

mkdir -p "$SBOM_OUTPUT_DIR"

SBOM_FILE="$SBOM_OUTPUT_DIR/${PROJECT_NAME}-${VERSION}.cdx.json"
log "Generating CycloneDX SBOM for $PROJECT_NAME:$VERSION"
syft pkg dir:. -o cyclonedx-json="$SBOM_FILE" || die "syft failed"

# ── Vulnerability scan ──
VULN_FILE="$SBOM_OUTPUT_DIR/${PROJECT_NAME}-${VERSION}.vuln.json"
log "Scanning SBOM for vulnerabilities"
grype sbom:"$SBOM_FILE" -o json > "$VULN_FILE" || die "grype failed"

# Check for Critical/High
CRIT_COUNT=$(jq '[.matches[] | select(.vulnerability.severity=="Critical")] | length' "$VULN_FILE")
HIGH_COUNT=$(jq '[.matches[] | select(.vulnerability.severity=="High")] | length' "$VULN_FILE")
log "Found $CRIT_COUNT Critical, $HIGH_COUNT High vulnerabilities"

if [[ "$FAIL_ON_CRITICAL" == "true" && $CRIT_COUNT -gt 0 ]]; then
    log "FAIL: Critical vulnerabilities found (gate: FAIL_ON_CRITICAL=true)"
    jq '.matches[] | select(.vulnerability.severity=="Critical") | {id: .vulnerability.id, severity: .vulnerability.severity, pkg: .artifact.name}' "$VULN_FILE"
    exit 1
fi
if [[ "$FAIL_ON_HIGH" == "true" && $HIGH_COUNT -gt 0 ]]; then
    log "FAIL: High vulnerabilities found (gate: FAIL_ON_HIGH=true)"
    jq '.matches[] | select(.vulnerability.severity=="High") | {id: .vulnerability.id, severity: .vulnerability.severity, pkg: .artifact.name}' "$VULN_FILE"
    exit 1
fi

# ── Secrets scan ──
SECRETS_FILE="$SBOM_OUTPUT_DIR/${PROJECT_NAME}-${VERSION}.secrets.json"
log "Scanning for embedded secrets"
trivy fs --scanners secret --format json --output "$SECRETS_FILE" . || die "trivy secrets failed"

SECRETS_COUNT=$(jq '[.Results[]?.Secrets[]?] | length' "$SECRETS_FILE" 2>/dev/null || echo 0)
log "Found $SECRETS_COUNT secrets"

if [[ "$FAIL_ON_SECRETS" == "true" && $SECRETS_COUNT -gt 0 ]]; then
    log "FAIL: Secrets detected (gate: FAIL_ON_SECRETS=true)"
    jq '.Results[]?.Secrets[]? | {file: .File, rule: .RuleID, severity: .Severity}' "$SECRETS_FILE"
    exit 1
fi

# ── License scan (optional, warn only) ──
LICENSE_FILE="$SBOM_OUTPUT_DIR/${PROJECT_NAME}-${VERSION}.license.json"
log "Scanning licenses"
trivy fs --scanners license --format json --output "$LICENSE_FILE" . || log "trivy license scan failed (non-blocking)"
# Check for copyleft in proprietary builds
FORBIDDEN_LICENSES=("GPL-3.0" "AGPL-3.0" "LGPL-3.0")
for lic in "${FORBIDDEN_LICENSES[@]}"; do
    if jq -e ".Results[]?.Licenses[]? | select(.Name | contains(\"$lic\"))" "$LICENSE_FILE" >/dev/null 2>&1; then
        log "WARN: Forbidden license detected: $lic"
    fi
done

# ── Sign SBOM ──
SIGNED_SBOM="${SBOM_FILE}.sig"
log "Signing SBOM with cosign"
if [[ -n "$COSIGN_KEY" ]]; then
    cosign sign-blob --key "$COSIGN_KEY" --output-signature "$SIGNED_SBOM" "$SBOM_FILE" || die "cosign sign failed"
else
    cosign sign-blob --yes --output-signature "$SIGNED_SBOM" "$SBOM_FILE" || die "cosign keyless sign failed"
fi

# ── Verify signature ──
cosign verify-blob --signature "$SIGNED_SBOM" "$SBOM_FILE" || die "Signature verification failed"

# ── Optional: Push to OCI registry ──
if [[ -n "$REGISTRY_URL" ]]; then
    log "Pushing SBOM to $REGISTRY_URL"
    # Requires ORAS or cosign copy
    cosign copy --additional-tag "$VERSION" "$REGISTRY_URL/$PROJECT_NAME-sbom" || log "Registry push failed (non-blocking)"
fi

# ── Output summary for CERG registry ingestion ──
cat <<EOF > "$SBOM_OUTPUT_DIR/${PROJECT_NAME}-${VERSION}.cerg-registry.json"
{
  "sbom_id": "CERG-SBOM-${PROJECT_NAME}-${VERSION}",
  "vendor_name": "internal",
  "product_name": "$PROJECT_NAME",
  "product_version": "$VERSION",
  "sbom_format": "CycloneDX",
  "sbom_source": "internally_generated",
  "component_count": $(jq '.components | length' "$SBOM_FILE"),
  "has_known_vulnerabilities": $(jq -e '.matches | length > 0' "$VULN_FILE" && echo true || echo false),
  "critical_vuln_count": $CRIT_COUNT,
  "high_vuln_count": $HIGH_COUNT,
  "license_risk_flag": false,
  "embedded_secrets_flag": $([[ $SECRETS_COUNT -gt 0 ]] && echo true || echo false),
  "supply_chain_tier": "direct_vendor",
  "cve_scan_date": "$(date -I)",
  "next_scan_due": "$(date -I -d '+90 days')",
  "associated_vendor_tier": "T1",
  "regulatory_scope": ["SOX"],
  "evidence_links": [
    "sbom:$SBOM_FILE",
    "vuln:$VULN_FILE",
    "secrets:$SECRETS_FILE",
    "license:$LICENSE_FILE",
    "signature:$SIGNED_SBOM"
  ],
  "vex_status": "not_applicable",
  "approval_status": "approved",
  "approver": "CI/CD Pipeline",
  "approval_date": "$(date -I)"
}
EOF

log "SBOM generation complete. Registry record: $SBOM_OUTPUT_DIR/${PROJECT_NAME}-${VERSION}.cerg-registry.json"
log "Artifacts in $SBOM_OUTPUT_DIR:"
ls -la "$SBOM_OUTPUT_DIR"