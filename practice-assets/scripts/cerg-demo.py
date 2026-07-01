#!/usr/bin/env python3
"""
CERG Demo Script — Run a Tier 1 Foundations Engagement in 30 Minutes
=====================================================================
Purpose: Demo script for prospect meetings. Walks through a mini-engagement
end-to-end: intake → discovery → findings → recommendations.

Usage:
  python3 practice-assets/scripts/cerg-demo.py --client "Acme Corp" --sector healthcare --output /tmp/cerg-demo

Requires: python3, no external dependencies for the demo path.
For live tool demos (optional): ConnectWise / Sentinel / Entra ID access.
"""

import argparse
import json
import os
import sys
from datetime import datetime

DEMO_VERSION = "1.0"

# ── Sample Control Assessment Data ──────────────────────────────────────
SAMPLE_FINDINGS = {
    "AC-1": {"status": "Partial", "finding": "No formal access control policy exists"},
    "AC-2": {"status": "Not Implemented", "finding": "No account lifecycle management"},
    "AC-3": {"status": "Partial", "finding": "Legacy authentication still enabled"},
    "IA-1": {"status": "Not Implemented", "finding": "MFA not enforced for any users"},
    "SI-1": {"status": "Implemented", "finding": "EDR deployed on 85% of endpoints"},
    "RA-2": {"status": "Not Implemented", "finding": "No vulnerability scanning in place"},
    "AU-1": {"status": "Not Implemented", "finding": "No centralized log collection"},
    "CP-1": {"status": "Partial", "finding": "Backups exist but not tested"},
    "CM-1": {"status": "Not Implemented", "finding": "No security baseline configuration"},
}

SECTOR_OVERLAYS = {
    "healthcare": "HIPAA / HITRUST — 36 additional requirements",
    "financial": "SOX ITGC / PCI DSS — 40 additional requirements",
    "government": "CMMC L2 / FedRAMP — 80 additional requirements",
    "energy": "NERC-CIP — 45 additional requirements",
    "saas": "SOC 2 + ISO 27001 — 30 additional requirements",
    "dib": "CMMC L2 + DFARS — 75 additional requirements",
    "manufacturing": "NIST 800-82 / IEC 62443 — 25 OT-specific controls",
    "cross-holding": "Multi-sector — combination of above",
}


def banner():
    print("=" * 70)
    print(f"  CERG Demo — Tier 1 Foundations Engagement  v{DEMO_VERSION}")
    print("=" * 70)


def phase_intake(client, sector):
    print(f"\n{'─' * 70}")
    print("  PHASE 1: INTAKE")
    print(f"{'─' * 70}")
    print(f"  Client:      {client}")
    print(f"  Sector:      {sector}")
    print(f"  Overlay:     {SECTOR_OVERLAYS.get(sector, 'Standard CERG Core Controls (100)')}")
    print(f"  Date:        {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  Engagement:  Tier 1 Foundations")
    print(f"  Duration:    2 weeks")
    print(f"  Price:       $10-20k")
    print()
    print("  [✓] Intake questionnaire completed")
    print("  [✓] Sector profile loaded")
    print("  [✓] Stakeholder map created")
    print("  [✓] SOW scope confirmed")
    return {"client": client, "sector": sector, "tier": "T1"}


def phase_discovery():
    print(f"\n{'─' * 70}")
    print("  PHASE 2: DISCOVERY")
    print(f"{'─' * 70}")
    print("  Assessing 100 Core Controls...")

    implemented = sum(1 for f in SAMPLE_FINDINGS.values() if f["status"] == "Implemented")
    partial = sum(1 for f in SAMPLE_FINDINGS.values() if f["status"] == "Partial")
    not_impl = sum(1 for f in SAMPLE_FINDINGS.values() if f["status"] == "Not Implemented")
    total = len(SAMPLE_FINDINGS)

    print(f"  Controls assessed: {total}")
    print(f"  Implemented:       {implemented}")
    print(f"  Partial:           {partial}")
    print(f"  Not Implemented:   {not_impl}")
    print(f"  Compliance score:  {int(implemented/total*100)}%")
    print()
    return {"assessed": total, "implemented": implemented, "score": int(implemented/total*100)}


def phase_findings():
    print(f"\n{'─' * 70}")
    print("  PHASE 3: CRITICAL FINDINGS")
    print(f"{'─' * 70}")
    print(f"  {'Control':<10} {'Status':<20} {'Finding':<40}")
    print(f"  {'─'*8:<10} {'─'*18:<20} {'─'*38:<40}")

    for cid, data in sorted(SAMPLE_FINDINGS.items()):
        status_display = {"Implemented": "✅ Implemented", "Partial": "◐ Partial", "Not Implemented": "❌ Not Implemented"}
        print(f"  {cid:<10} {status_display.get(data['status'], data['status']):<20} {data['finding']:<40}")

    critical = [cid for cid, d in SAMPLE_FINDINGS.items() if d['status'] == 'Not Implemented']
    print()
    print(f"  Critical gaps to address in Tier 1: {', '.join(critical[:5])}")

    return {"critical": critical}


def phase_recommendations():
    print(f"\n{'─' * 70}")
    print("  PHASE 4: RECOMMENDATIONS")
    print(f"{'─' * 70}")

    roadmap = [
        ("Week 1", "IA-1", "Enable MFA for all users", "4 hrs"),
        ("Week 1", "AC-1", "Deploy access control policy template", "2 hrs"),
        ("Week 1", "SI-1", "Enable EDR on remaining endpoints", "4 hrs"),
        ("Week 2", "AC-3", "Block legacy authentication via CA", "2 hrs"),
        ("Week 2", "RA-2", "Configure vulnerability scanning", "4 hrs"),
        ("Week 2", "AU-1", "Set up log collection + SIEM connector", "6 hrs"),
    ]

    print(f"  {'Week':<10} {'Control':<10} {'Action':<50} {'Effort':<8}")
    print(f"  {'─'*8:<10} {'─'*8:<10} {'─'*48:<50} {'─'*6:<8}")
    for week, ctrl, action, effort in roadmap:
        print(f"  {week:<10} {ctrl:<10} {action:<50} {effort:<8}")

    print()
    print("  Estimated Tier 1 cost: $10-15k")
    print("  Estimated effort: 22 hours consulting + 15 hours client team")
    print()

    return {"weeks": 2, "cost": "10-15k"}


def phase_deliverables(output_dir):
    print(f"\n{'─' * 70}")
    print("  PHASE 5: DELIVERABLES")
    print(f"{'─' * 70}")

    deliverables = [
        "Assessment report (this summary)",
        "Control gap analysis",
        "30-60-90 day remediation roadmap",
        "Policy templates (AC-1, IA-1, IR-1)",
        "Evidence package (screenshots, config exports)",
        "QBR schedule + first quarterly report template",
    ]

    for d in deliverables:
        print(f"  [ ] {d}")

    os.makedirs(output_dir, exist_ok=True)
    summary_path = os.path.join(output_dir, "demo-summary.json")

    summary = {
        "client": client_name,
        "sector": sector_name,
        "tier": "T1 Foundations",
        "findings": SAMPLE_FINDINGS,
        "timestamp": datetime.now().isoformat(),
        "demo_version": DEMO_VERSION,
    }

    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n  [✓] Demo summary saved to: {summary_path}")
    return summary_path


def phase_handoff():
    print(f"\n{'─' * 70}")
    print("  PHASE 6: HANDOFF")
    print(f"{'─' * 70}")
    print("  1. Runbook delivered to client IT team")
    print("  2. Evidence package handed over")
    print("  3. QBR scheduled for 3 months out")
    print("  4. Client security contact named")
    print("  5. MSP transition plan (if applicable)")
    print()
    print("  Next engagement option: Tier 2 Structure ($30-50k)")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CERG Demo — Tier 1 Foundations Engagement")
    parser.add_argument("--client", default="Demo Corp", help="Client name")
    parser.add_argument("--sector", default="saas", choices=list(SECTOR_OVERLAYS.keys()), help="Client sector")
    parser.add_argument("--output", default="/tmp/cerg-demo", help="Output directory")
    args = parser.parse_args()

    client_name = args.client
    sector_name = args.sector

    banner()
    phase_intake(client_name, sector_name)
    phase_discovery()
    phase_findings()
    phase_recommendations()
    phase_deliverables(args.output)
    phase_handoff()

    print("=" * 70)
    print("  Demo complete. Ready for Q&A.")
    print("=" * 70)
