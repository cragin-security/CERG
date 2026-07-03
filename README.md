# CERG · Cybersecurity Operating Model

## cragin-security fork — practice-hardened, opinionated, MSP/MSSP-ready

**This is the [cragin-security](https://github.com/cragin-security) fork of the upstream [m0dernz/CERG](https://github.com/m0dernz/CERG) project.** We contribute upstream, but this fork carries our opinionated spin: specific tools, ~100 controls with copy-paste instructions, and practitioner materials built for MSPs, MSSPs, and IT generalists delivering security to small and mid-sized clients.

**Upstream CERG** is a cybersecurity operating model — not a control framework or compliance checklist. It gives security teams the policy spine, roles, standards, procedures, and evidence habits needed to run a real program. Read the [upstream README](https://github.com/m0dernz/CERG) for the canonical description.

**This fork** extends upstream with:

| Dimension | Upstream (m0dernz) | This Fork (cragin-security) |
|-----------|-------------------|---------------------------|
| Controls | ~18 schematic entries | **97 enumerated controls** with MSP copy-paste instructions |
| Tools | Framework-level | **Opinionated tool matrix** — 12 categories, Primary/Acceptable/Avoid with integration map |
| Audience | Program architects, auditors | **MSPs, MSSPs, IT generalists** — entry-level IT staff can follow the runbook |
| GRC anchor | Architecture reference | **ServiceNow GRC + Vanta rollout guide** with control import and evidence automation |
| Controls document | [CB-001](governance/CERG-GOV-CB-001_Unified_Control_Baseline.md) | [CB-002](governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) — 97 controls, 19 families |
| Delivery | CERG Lite / Standard / Regulated adoption paths | **Full engagement playbook** with pricing, SOW essentials, and delivery phases |
| Consulting | Implicit | **Explicit** — engagement playbook, MSP runbook, pricing reference, anti-patterns |

---

## What's different in this fork

### Practice Assets (`practice-assets/`)

Practical, opinionated materials for delivering CERG as a consulting service:

| Document | What it does |
|----------|--------------|
| [Opinionated Tool Matrix](practice-assets/tools/opinionated-tool-matrix-v1.md) | 12 security tool categories — every recommendation scored on integration surface, MSP multi-tenancy, and IT generalist usability. Integration map shows how the stack wires together. |
| [GRC Rollout Guide](practice-assets/tools/grc-rollout-v1.md) | Step-by-step ServiceNow GRC control import, evidence automation, MSP multi-tenancy. Vanta fallback for SMB. |
| [MSP/MSSP Runbook](practice-assets/msp-runbook-v1.md) | 5-phase delivery playbook: intake → deployment (copy-paste commands for SentinelOne, Wazuh, Tenable, Wiz, Veeam) → per-control implementation → evidence collection cadence → client reporting. Common pitfalls. |
| [Engagement Playbook](practice-assets/engagement-playbook-v1.md) | Full consulting lifecycle: Discover → Assess → Plan → Deploy → Operate → Handoff. Pricing for SMB ($5k-25k) through enterprise ($25k-100k). Anti-patterns and SOW essentials. |

### 100-Core Control Baseline

The [100-Core Control Baseline](governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) extends upstream's schematic control matrix into 97 fully enumerated controls across all 19 NIST 800-53r5 families. Every control has:

- An action statement an IT generalist can understand
- Named evidence with collection method and frequency
- Per-control MSP implementation notes
- Tool bindings tied to the opinionated tool matrix

This is the control set you hand to an MSP technician on day one — not a framework reference they have to translate.

### Recommends specific tools, not categories

Instead of "deploy a SIEM" or "use a GRC platform," this fork says:

- **Primary:** Wazuh (SMB), Elastic Security (enterprise) — not "choose a SIEM"
- **Primary:** SentinelOne for endpoint — not "deploy EDR"
- **Primary:** ServiceNow GRC or Vanta — not "select a GRC platform"
- **Avoid:** spreadsheets, DIY ELK, Symantec, Archer — with reasons why

Every recommendation is backed by integration surface, MSP multi-tenancy, and IT generalist usability criteria.

---

## Start here

| If you are... | Start with |
|---|---|
| An MSP/MSSP delivering CERG to clients | [MSP/MSSP Runbook](practice-assets/msp-runbook-v1.md) |
| Picking tools for a CERG deployment | [Opinionated Tool Matrix](practice-assets/tools/opinionated-tool-matrix-v1.md) |
| Setting up a GRC platform | [GRC Rollout Guide](practice-assets/tools/grc-rollout-v1.md) |
| Scoping or pricing a CERG engagement | [Engagement Playbook](practice-assets/engagement-playbook-v1.md) |
| Looking for the full control set | [100-Core Control Baseline](governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) |
| New to CERG (upstream) | [START-HERE.md](START-HERE.md) |
| Using an AI assistant | [ADOPT-WITH-AN-AGENT.md](ADOPT-WITH-AN-AGENT.md) |
| Contributing upstream | [CONTRIBUTING.md](CONTRIBUTING.md) |

---

## Relationship to upstream

This fork is **upstream-friendly**. We:

- Contribute validator fixes, bug patches, and non-opinionated improvements back to [m0dernz/CERG](https://github.com/m0dernz/CERG)
- Keep the core architecture compatible — CB-002 is an extension of CB-001, not a replacement
- Mark all practice-assets as `OPN` domain code so they don't collide with upstream's `GOV`, `STD`, `PRC` namespace
- Maintain a clear boundary: `governance/CERG-GOV-CB-002` is the fork's control extension; everything in `practice-assets/` is consulting delivery material

Upstream sets the architecture. This fork shows practitioners how to wire it into a functioning program with specific tools, clear instructions, and a business model.

---

## What is in the repo

Everything upstream carries, plus:

| Directory | Content |
|-----------|---------|
| `governance/` | Policy, operating model, risk framework, RACI, metrics, maturity, workforce governance — plus the fork's [100-Core Control Baseline](governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md) |
| `standards/` | Technical security standards (15 docs) |
| `procedures/` | Repeatable workflows for risk, exposure, architecture review, TPRM, audit, change, threat modeling |
| `plans/` | Operational packages for regulated or specialized scopes |
| `templates/` | Forms, registers, and records |
| `roles/` | Workforce architecture — job families, JDs, competencies, onboarding |
| `practice-assets/` | **Fork-only**: tool matrix, GRC rollout, MSP runbook, engagement playbook |
| `machine-readable/` | Indexes, manifests, schemas, LLM metadata |
| `examples/` | Adoption examples and day-in-the-life walkthroughs |

The authoritative inventory is the [Document Catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md).

---

## LLM and automation use

- [`machine-readable/cerg-llm-index.json`](machine-readable/cerg-llm-index.json): complete local corpus map (153 documents)
- [`machine-readable/cerg-document-tiers.yaml`](machine-readable/cerg-document-tiers.yaml): adoption tiers and loading order
- [`AGENTS.md`](AGENTS.md): guidance for AI coding agents working in this repo

---

## When this fork is right for you

Use `cragin-security/CERG` when you:

- Are an MSP, MSSP, or IT generalist delivering security to small/mid-sized clients
- Want specific tool recommendations, not categories to evaluate
- Need copy-paste deployment instructions your entry-level techs can follow
- Want a consulting practice wrapper around the CERG operating model
- Need ~100 controls with per-control evidence and MSP implementation notes

Stick with upstream `m0dernz/CERG` when you:

- Want the canonical framework architecture without opinionated tool choices
- Are building your own tool strategy and just need the program structure
- Prefer the lighter, schematic control set for organizational calibration

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Fork freely — adapt openly — attribute generously.

Upstream: [m0dernz/CERG](https://github.com/m0dernz/CERG) · Fork: [cragin-security/CERG](https://github.com/cragin-security/CERG)
