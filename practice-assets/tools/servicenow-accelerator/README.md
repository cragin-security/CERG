# CERG ServiceNow GRC Accelerator

Import the CERG cybersecurity operating model into ServiceNow GRC in one day.

## Files

| File | ServiceNow Module | Description |
|------|------------------|-------------|
| `cerg-control-framework.csv` | Policy & Compliance > Controls | 99 CERG controls across 18 families |
| `cerg-framework-mapping.csv` | Policy & Compliance > Framework Mapping | Control-to-regulation mappings (NIST, PCI, ISO, CMMC, NERC) |
| `cerg-risk-taxonomy.csv` | Risk Management > Risk Taxonomy | 17 risk categories with pre-scored impact/likelihood |

## Installation

### Prerequisites
- ServiceNow instance with **Policy & Compliance Management** module
- **Risk Management** module (for risk taxonomy)
- Admin or **snc_internal** role for data imports

### Step 1: Import the Control Framework
1. Navigate to **Policy & Compliance** > **Controls** > **Import Controls**
2. Select `cerg-control-framework.csv`
3. Map columns: `control_id` -> Control Number, `family` -> Category, `statement` -> Description
4. Map `nist_800_53` to a custom field or Tag
5. Click **Import**

### Step 2: Import the Framework Mapping
1. Navigate to **Policy & Compliance** > **Frameworks** > **Import Mappings**
2. Select `cerg-framework-mapping.csv`
3. Map `control_id`, `framework`, `control_ref`
4. Click **Import**

### Step 3: Import the Risk Taxonomy
1. Navigate to **Risk Management** > **Risk Taxonomy** > **Import**
2. Select `cerg-risk-taxonomy.csv`
3. Map columns to Risk Category, Risk Subcategory, Description, Impact Score, Likelihood Score
4. Click **Import**

### Step 4: Configure Evidence Collection (optional)
Each control requires evidence. Configure using the Verification steps from the CERG CB-001 document:
- **Automated evidence**: Integrate Entra ID, Sentinel, Wiz, Qualys APIs
- **Manual evidence**: Use the CERG TMPL-AUD-001 evidence worksheet template
- **Cadence**: Set monthly collection cadence for automated evidence, quarterly for manual

## Post-Installation

1. **Run the CERG Assessment** — Policy & Compliance > Assessments > Create
2. **Review the Risk Register** — Risk Management > Risk Register
3. **Map to Regulations** — Attach framework mappings to relevant regulations
4. **Configure the CISO Dashboard** — Performance Analytics > Dashboard

## Customization

- Add custom fields to controls for regulatory-specific guidance
- Map additional frameworks (FedRAMP, HIPAA, GDPR) using the same mapping CSV format
- Modify risk scores in the taxonomy to match organizational risk appetite

## Support

For questions, contact your CERG practice consultant.

---

*CERG ServiceNow GRC Accelerator v1 — July 2026*
