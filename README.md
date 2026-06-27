# CERG · Practice-Hardened Operating Model

**100 Core controls. Implementation guidance for IT generalists, MSPs, and engineers. Opinionated tool stack. Built for consulting delivery.**

This is a practice-hardened fork of the upstream [CERG cybersecurity operating model](https://github.com/m0dernz/CERG). It keeps the three-pillar spine (Engineering · Risk · Governance) but adds what you need to actually implement the controls: step-by-step instructions, copy-paste commands, tool recommendations, compensating controls, and threat-intel-validated guidance.

---

## What is different about this fork

| Dimension | Upstream CERG | This fork |
|-----------|---------------|-----------|
| **Controls** | ~45 baseline controls | **100 Core controls** with implementation guidance across 18 families |
| **Implementation guidance** | Written for security engineers | **Three readers**: IT generalist (numbered steps + commands), MSP (template patterns), security engineer (standard references) |
| **Tool opinions** | Tool-agnostic, no recommendations | **Primary + acceptable + avoid** per control. Wiz, SentinelOne, Entra ID, CyberArk, Veeam, Sentinel — named with rationales |
| **Compensating controls** | Not addressed | Per-control compensating control catalog with regulatory acceptability notes |
| **Threat intel validation** | Not referenced | Controls validated against live threat intelligence: Miasma supply chain, Chrome session theft, Shai Hulud cloud exfil, OT advisory pacing, Signal recovery attacks |
| **Implementation tiers** | Not addressed | Core (100 controls, all orgs) · Enhanced (planned) · Advanced (planned) |
| **Practice assets** | Not included | Intake questionnaire, 4-tier scope templates, org profile checklist, sector profiles, engagement trackers, debrief protocol, MSP runbook patterns |
| **Client delivery model** | Not addressed | CON-001 defines Tier 1-4 engagement model with fixed-scope deliverables, role consolidation maps, risk register bootstrap, handover memos |

---

## What is in the repo

```
governance/          Policy, capability map, control baseline (100 Core controls), operating model
standards/           Technical standards per domain
procedures/          Repeatable workflows for risk, exposure, architecture, TPRM, audit
plans/               Operational packages: PCI DSS, NERC-CIP, CMMC, SOX, consulting model
templates/           System control profiles, risk register forms, AI intake forms
roles/               Workforce architecture, job descriptions, competency models
machine-readable/    LLM index, manifest, tool matrix, crosswalks
practice-assets/     Consulting delivery assets:
  ├── agent-integration/  6 LLM agent specifications (intake, adaptation, crosswalk, threat, assembly, practice knowledge)
  ├── checklists/         Organization profile validation checklist
  ├── detection/          Detection engineering framework (20 MITRE ATT&CK techniques with KQL + Sigma)
  ├── intake/             Client intake questionnaire with tier/sector/overlay routing
  ├── scripts/            Upstream drift check, render-and-diff, client repo provisioning
  ├── scope-templates/   4 tier scope templates + guardrails + gate criteria
  ├── sector-profiles/   8 sector profiles + overlay assessments (FedRAMP, HIPAA, ISO, cloud migration)
  ├── templates/          Adoption record, risk register bootstrap, handover memo, improvement register, case study
  └── trackers/           Engagement tracker, debrief protocol, client register, backlog, pricing, competency
```

---

## The control baseline (CB-001)

The core of this fork is a completely rewritten control baseline. Every control includes:

- **Statement** — one-sentence operational requirement
- **For the IT Generalist** — numbered steps, OS-specific commands (PowerShell, bash, Azure CLI), expected output
- **For the MSP** — how to template across clients, automation patterns, evidence collection
- **For the Security Engineer** — standard reference (NIST, ISO, PCI), evidence cadence, integration notes
- **Tool Mappings** — ✅ Primary recommendation, ◐ Acceptable alternatives, ❌ Tools to avoid
- **Verification** — command to run, what "control failure" looks like
- **Common Mistakes** — top 3-5 implementation errors observed in practice
- **If You Cannot Implement This** — compensating control path with regulatory acceptability
- **Threat Intel Validation** — real-world attack references that validate the control's relevance

100 controls across: AC (13) · AU (9) · CM (8) · CP (6) · IA (8) · RA (5) · SI (8) · SC (7) · CA (2) · AT (3) · IR (5) · PE (3) · PL (3) · PM (6) · PS (4) · SA (2) · MA (3) · MP (2) · DG (1)

---

## Adoption modes

| Mode | Best for | Starting point |
|------|----------|----------------|
| **Tier 1: Foundations** | New security function, 1-15 FTEs, no operating model | MVC spine (8 docs) + risk register bootstrap |
| **Tier 2: Structure** | Existing function, 5-30 FTEs, fragmented policies | MVC + standards gap analysis + architecture review |
| **Tier 3: Compliance** | Regulated environment, recurring audit burden | Tier 2 + regulatory packages (PCI, SOX, CMMC, NERC-CIP) |
| **Tier 4: Strategic Partner** | Enterprise, multi-regulator, strategic investment | Tier 3 + co-designed evolution roadmap |

See `plans/CERG-PLN-CON-001_Consulting_Services_Operating_Plan.md` for the full engagement model.

---

## Quick start

```bash
# 1. Validate the corpus
python3 tools/cerg-validate.py

# 2. Review the 100 Core controls
grep "^### [A-Z]*-[0-9]" governance/CERG-GOV-CB-001_Unified_Control_Baseline.md

# 3. Check upstream drift
python3 practice-assets/scripts/check-upstream-drift.py --client-repo .

# 4. Explore practice assets
ls practice-assets/
```

---

## Relationship to upstream CERG

This repository tracks upstream CERG and layers on practice-specific content. The `machine-readable/` index, validation tooling, and corpus structure remain compatible. The practice assets in `practice-assets/` are not part of the upstream corpus — they are consulting delivery tooling.

Upstream contributions (bug fixes, template improvements, crosswalk additions) are filed against `m0dernz/CERG` following the contribution workflow in `practice-assets/trackers/upstream-contribution-workflow-v1.md`.

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — Fork freely, adapt openly, attribute generously.
