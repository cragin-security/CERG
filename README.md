# CERG ,  Cyber Engineering, Risk & Governance

**A security program in a box.**

Cybersecurity teams have struggled with the same structural problem for twenty years: fragmented tools, siloed teams, and a culture of "no" that slows the business without meaningfully reducing risk. CERG is a deliberate answer to that problem.

Fork it. Adapt it. Run it. → **[cerg.nexus](https://cerg.nexus)**

---

## What CERG gives you

Not a control framework. Not a compliance checklist. A complete, ready-to-run cybersecurity operating model ,  with the policies, standards, procedures, runbooks, and templates a mature security function actually needs.

Everything is in Markdown. Everything is interconnected. Drop it in, adapt the names and org structure to fit yours, and you have a functioning program.

Regulatory alignment ,  NIST, NERC-CIP, CMMC L2, SOX ITGC ,  is a byproduct of running the program well, not the point of it.

---

## Three pillars. One accountability model.

Most control failures trace back to the same root cause: ambiguous ownership. CERG fixes that by assigning every piece of security work to exactly one of three pillars, with crisp missions and clear handoffs between them.

Together the three pillars are pronounced **SURGE** ,  because effective security is fast, powerful, and directional. It's an operational force, not a support function.

---

### 🔧 Cyber Engineering
*Build securely. Deploy confidently. Consult continuously.*

Engineering is the organization's internal security consulting practice. Engineers embed in projects from the first conversation through production handoff ,  reviewing architecture, driving pre-launch remediation, and ensuring the team inheriting a new system knows its security posture. They do not own the systems they help build. They make the systems worth owning.

---

### 🔍 Cyber Risk
*Know your exposure. Manage it deliberately. Never be surprised.*

Risk hunts for problems rather than waiting for them to surface. Continuous vulnerability management, adversarial testing, threat intelligence, and vendor risk assessment combine to give the organization the clearest possible picture of what's threatening it ,  and how severe those threats actually are. Pre-production findings are engineering inputs. Post-production findings are managed risks. The distinction matters.

---

### 📋 Cyber Governance
*Set the rules. Track the work. Enable the business to move with confidence.*

Governance defines what good looks like, then makes sure the organization gets there. Policy, standards, compliance tracking, control evidence, risk register, audit response ,  all of it. The operating philosophy is "yes, and…" ,  not a function that closes doors, but one that gives the business the guardrails to move fast without hidden exposure.

---

## How the pillars work together

The pillars are not sequential. They run simultaneously, with structured handoffs:

| Stage | Lead | Supporting |
|---|---|---|
| New project / business requirement | Engineering | Governance sets standards; Risk flags vendor concerns |
| Architecture and design review | Engineering | Risk performs threat modeling |
| Pre-production vulnerability scan | Risk | Engineering drives remediation before go-live |
| Risk acceptance for unresolved findings | Engineering + Risk | Governance provides treatment template; leadership signs off |
| Post-production monitoring | Governance | Risk tracks emerging CVEs; Engineering re-engages on major changes |
| Audit and evidence collection | Governance | Engineering and Risk produce artifacts from daily work |

---

## What's in the repo

**Governance**
- [CERG Framework](CERG-GOV-FRM-001_CERG_Framework.md) ,  design philosophy, the three-pillar model, team structure, and the path to adaptive maturity
- [Cybersecurity Policy](CERG-POL-001_Cybersecurity_Policy.md) ,  the durable principles that anchor everything below
- [Operating Model](CERG-GOV-OM-001_CERG_Operating_Model.md) ,  pillar charters, interfaces, and governance cadence
- [Document Catalog](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) ,  ID scheme and authoritative artifact inventory
- [Metrics & Reporting](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) ,  CISO and board-level dashboard
- [Unified Control Baseline](CERG-GOV-CB-001_Unified_Control_Baseline.md) ,  the full control set with named evidence and regulatory overlays
- [Compliance Matrix](CERG-GOV-CMX-001_Compliance_Matrix.md) ,  22 security intents mapped to every framework simultaneously
- [Risk Taxonomy](CERG-GOV-TAX-001_Risk_Taxonomy.md) ,  the threat reasoning behind each control
- [Risk Management Framework](CERG-GOV-RMF-001_Risk_Management_Framework.md) ,  how risk is identified, scored, treated, and tracked

**Standards**
- [Access Management](CERG-STD-AC-001_Access_Management_Standard.md)
- [Secure Configuration Baseline](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)
- [Cryptography & Key Management](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)
- [CUI Handling](CERG-STD-CUI-001_CUI_Handling_Standard.md)
- [IT / Cloud / SaaS Security](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md)
- [Logging, Monitoring & Detection](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)
- [Grid Control Systems Security](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)
- [Cyber Resilience & Backup](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md)

**Procedures & Runbooks**
- [Access Management Runbook](CERG-PRC-AC-002_Access_Management_Runbook.md)
- [Architecture Review & Project Intake](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)
- [Adversarial Validation](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)
- [Risk Register & Exception Process](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
- [Third-Party & Supply Chain Risk](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)
- [Vulnerability Management](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md)

**Plans & Operational Packages**
- [Incident Response Plan](CERG-PLN-IR-001_Incident_Response_Plan.md)
- [NERC-CIP Operational Package](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md)
- [CUI / CMMC Operational Package](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md)
- [SOX ITGC Operational Package](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md)

**Templates**
- [Risk Register Templates & Reporting](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md)

---

## Scales to fit you

The framework describes what operating at [NIST CSF Adaptive maturity](https://www.nist.gov/cyberframework) looks like for a large organization ,  14,000 employees, 60-person security team. That's the upper bound. Every team structure, headcount, and engagement model in these documents is designed to scale down. A 5-person team runs the same model with fewer people covering more pillars.

---

## For LLMs and automation

Every document is Markdown. The full corpus is available at [cerg.nexus](https://cerg.nexus):

- **[/llms.txt](https://cerg.nexus/llms.txt)** ,  document index for AI tools and crawlers
- **[/llms-full.txt](https://cerg.nexus/llms-full.txt)** ,  full corpus concatenated into one file
- **[Bulk download](https://cerg.nexus/downloads/cerg-docs.zip)** ,  all 28 documents as a single ZIP

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) ,  fork freely, adapt openly, attribute generously.
