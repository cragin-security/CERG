# CERG Example Profiles

Sample organization profiles for different sectors and sizes. Use these as starting points
for your [Organization Adaptation Profile](../governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md).

## Available profiles

| Profile | Sector | Size | Team | Key regulatory |
|---------|--------|------|------|----------------|
| [Regulated Utility](regulated-utility-profile/) | Electric utility | 14,000 employees | 60-person CERG | NERC-CIP, CMMC, SOX |

## Operational stories

| Story set | Purpose |
|-----------|---------|
| [Day in the Life](day-in-the-life/) | Narrative walkthroughs for common three-pillar cyber operations scenarios |

More profiles coming: small-team SaaS, healthcare, manufacturing/OT, financial services, MSP-heavy nonprofit/municipality.

## Using a profile

1. Read the profile's README to understand the organizational context.
2. Copy the token values to your `cerg-org-profile.yml`.
3. Adjust headcount, sector, and regulators to match your reality.
4. Run `python3 tools/cerg-render.py` to produce your organization-specific corpus.

**These are examples, not defaults.** The CERG framework itself is sector-agnostic.
