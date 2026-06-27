# CERG PCI Crosswalk Generator Agent — Specification v1
## Practice Asset — Not a CERP Corpus Document

---

## Capability
Read PCI DSS v4.0.1 requirements and CERG's Unified Control Baseline (CB-001), then produce a draft PCI-to-CERG crosswalk with evidence mapping and gap list.

## Trigger
A new regulatory overlay build is initiated. Target framework: PCI DSS v4.0.1.

## Inputs Required
1. PCI DSS v4.0.1 requirements (official standard or structured summary)
2. CERG Unified Control Baseline (`governance/CERG-GOV-CB-001_Unified_Control_Baseline.md`)
3. Existing crosswalk patterns in CB-001 §10

## Knowledge to Load

### CERG Corpus
- `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md` — §6 (control set), §9 (evidence mapping), §10 (crosswalk patterns)
- `machine-readable/pci-dss-crosswalk-v1.csv` — reference crosswalk from prior manual build
- `plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md` — §4 (control library pattern), §5 (evidence reuse pattern)

### External
- PCI DSS v4.0.1 requirements text
- CB-001 §10.1 (NIST/NERC-CIP/CMMC/SOX crosswalk) as the format template

## Instructions

### Step 1: PCI Requirements Inventory
List all PCI DSS v4.0.1 requirements and sub-requirements (12 requirements, ~264 sub-requirements). Note whether each is "Required" or "Best Practice" per v4.0.1 phase-in dates.

### Step 2: Map to CERG Controls
For each PCI requirement, identify the CERG CB-001 control(s) that satisfy it:
- If a direct match exists: record the CERG control ID
- If partial match: note the gap and whether CERG parameters can be tightened
- If no match: flag as a PCI-specific control gap

Use the CB-001 §6 control table as the authoritative CERG control list. Use the §10.1 crosswalk format as the mapping template.

### Step 3: Map Evidence
For each mapped control, identify the CERG evidence artifact (§9) that would satisfy the PCI requirement. Flag cases where:
- The existing evidence cadence is less frequent than PCI requires (e.g., CERG says annual, PCI says quarterly)
- The evidence format does not match PCI expectations (e.g., SIM vs. ASV scan)
- No existing CERG evidence artifact exists

### Step 4: Identify PCI-Specific Gaps
Requirements that have no CERG control match become PCI-specific control proposals:
- Name the gap
- Propose a PCI-specific control ID (PCI-NSC-001, PCI-SAD-001, etc.)
- Suggest subordinate standard or procedure reference
- Flag that these will need CPA attestation consideration

### Step 5: Build Crosswalk Table
Format: one row per CERG baseline control with PCI DSS requirement mapping:

| Baseline Control | PCI DSS Requirement(s) |
|---|---|
| AC-2 | Req 7.2, 7.2.4, 8.1.2 |
| AC-3 | Req 7.1, 7.1.2, 8.3.1 |
| ... | ... |

Plus a gap table:

| PCI Req | Gap | Proposed Control |
|---|---|---|
| 1.1.5 | NSC rule reviews every 6 months | PCI-NSC-001 |

## Output Format
A file named `crosswalk-pci-dss-{YYYY-MM-DD}.md` written to `machine-readable/` containing:
1. Framework metadata (PCI DSS v4.0.1, date, scope)
2. Control-to-requirement crosswalk table
3. Evidence mapping per control
4. Gap analysis with proposed new controls
5. Notes for QSAR evidence package requirements

## Validation Criteria
- [ ] Every PCI DSS requirement is addressed (mapped or gapped)
- [ ] Each CERG control reference uses the correct ID from CB-001 §6
- [ ] Evidence references use the correct artifact names from CB-001 §9
- [ ] Gap analysis notes which requirements have no CERG match
- [ ] Crosswalk format matches CB-001 §10.1 conventions
- [ ] Proposed PCI-specific controls use the correct ID format
