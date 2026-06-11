# CERG · Cyber Engineering, Risk & Governance

**A security program in a box.**

Cybersecurity teams have struggled with the same structural problem for twenty years: fragmented tools, siloed teams, and a culture of "no" that slows the business without meaningfully reducing risk. CERG is a deliberate answer to that problem.

Fork it. Adapt it. Run it. → **[cerg.nexus](https://cerg.nexus)**

---

## What CERG gives you

Not a control framework. Not a compliance checklist. A complete, ready-to-run cybersecurity operating model, with the policies, standards, procedures, runbooks, and templates a mature security function actually needs.

Everything is in Markdown. Everything is interconnected. Drop it in, adapt the names and org structure to fit yours, and you have a functioning program.

Regulatory alignment — NIST 800-53r5, NIST 800-171r3, NIST CSF 2.0, NIST RMF, NERC-CIP, CMMC L2, SOX ITGC — is a byproduct of running the program well, not the point of it.

---

## Three pillars. One accountability model.

Most control failures trace back to the same root cause: ambiguous ownership. CERG fixes that by assigning every piece of security work to exactly one of three pillars, with crisp missions and clear handoffs between them.

Together the three pillars are pronounced **SURGE**, because effective security is fast, powerful, and directional. It's an operational force, not a support function.

---

### 🔧 Cyber Engineering
*Build securely. Deploy confidently. Consult continuously.*

Engineering is the organization's internal security consulting practice. Engineers embed in projects from the first conversation through production handoff, reviewing architecture, driving pre-launch remediation, and ensuring the team inheriting a new system knows its security posture. They do not own the systems they help build. They make the systems worth owning.

---

### 🔍 Cyber Risk
*Know your exposure. Manage it deliberately. Never be surprised.*

Risk hunts for problems rather than waiting for them to surface. Continuous vulnerability management, adversarial testing, threat intelligence, and vendor risk assessment combine to give the organization the clearest possible picture of what's threatening it, and how severe those threats actually are. Pre-production findings are engineering inputs. Post-production findings are managed risks. The distinction matters.

---

### 📋 Cyber Governance
*Set the rules. Track the work. Enable the business to move with confidence.*

Governance defines what good looks like, then makes sure the organization gets there. Policy, standards, compliance tracking, control evidence, risk register, audit response — all of it. The operating philosophy is "yes, and…", not a function that closes doors, but one that gives the business the guardrails to move fast without hidden exposure.

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

**Governance (26 documents)**
- [CERG Framework](CERG-GOV-FRM-001_CERG_Framework.md) — design philosophy, the three-pillar model, team structure, and the path to adaptive maturity
- [Cybersecurity Policy](CERG-POL-001_Cybersecurity_Policy.md) — the durable principles that anchor everything below
- [Operating Model](CERG-GOV-OM-001_CERG_Operating_Model.md) — pillar charters, interfaces, and governance cadence
- [Document Catalog](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) — ID scheme and authoritative artifact inventory
- [Unified Control Baseline](CERG-GOV-CB-001_Unified_Control_Baseline.md) — 28 controls across 6 families, with named evidence and regulatory overlays
- [Compliance Matrix](CERG-GOV-CMX-001_Compliance_Matrix.md) — 22 security intents mapped to every framework simultaneously
- [Risk Taxonomy](CERG-GOV-TAX-001_Risk_Taxonomy.md) — the threat reasoning behind each control
- [Risk Management Framework](CERG-GOV-RMF-001_Risk_Management_Framework.md) — how risk is identified, scored, treated, and tracked
- [Style Guide](CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md) — authorship conventions for the entire corpus
- [Consolidated Roles & RACI](CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md) — 27 canonical roles with full RACI
- [Implementation & Adaptation Guide](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) — how to adopt and tailor CERG
- [Organization Adaptation Profile](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) — variance and scoping template
- [Maturity Self-Assessment](CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md) — NIST CSF-based maturity scoring
- [Metrics & Reporting](CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md) — CISO and board-level dashboard
- [Annual Security Calendar](CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md) — annual governance cadence
- [Traceability Matrix](CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md) — control-to-procedure cross-reference
- [Control Effectiveness Framework](CERG-GOV-CEF-001_Control_Effectiveness_Framework.md) — how controls are tested and rated
- [Job Architecture](CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md) — security job family and grading
- [Job Descriptions](CERG-GOV-JD-001_CERG_Job_Descriptions.md) — full security role descriptions
- [Competency Model](CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md) — behavioral anchors per role
- [Performance Management](CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md) — performance evaluation criteria
- [Workforce Planning](CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md) — team sizing and capacity model
- [Succession Planning](CERG-GOV-SUCC-001_Succession_Planning_and_Talent_Review_Framework.md) — bench strength and talent pipeline
- [Training & Certification](CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md) — learning paths and certification requirements
- [Onboarding Program](CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md) — structured new-hire integration plan
- [Contractor Integration](CERG-GOV-CON-001_Contractor_and_Non-Employee_Staff_Integration_Guide.md) — non-employee staff onboarding
- [Program Improvement Register](CERG-GOV-IMPREG-001_Program_Improvement_Register.md) — continuous improvement tracking

**Standards (15 documents)**
- [Access Management](CERG-STD-AC-001_Access_Management_Standard.md)
- [Secure Configuration Baseline](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md)
- [Cryptography & Key Management](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md)
- [CUI Handling](CERG-STD-CUI-001_CUI_Handling_Standard.md)
- [IT / Cloud / SaaS Security](CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md)
- [Logging, Monitoring & Detection](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md)
- [Grid Control Systems Security](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md)
- [Cyber Resilience & Backup](CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md)
- [Asset Management & Inventory](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md)
- [Data Governance & Classification](CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md)
- [Network Security & Segmentation](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md)
- [Endpoint & Mobile Security](CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md)
- [Email & Messaging Security](CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md)
- [AI Security](CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md)
- [Secure Software Development](CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md)

**Procedures & Runbooks (12 documents)**
- [Access Management Runbook](CERG-PRC-AC-002_Access_Management_Runbook.md)
- [Architecture Review & Project Intake](CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md)
- [Adversarial Validation](CERG-PRC-AV-001_Adversarial_Validation_Procedure.md)
- [Risk Register & Exception Process](CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md)
- [Third-Party & Supply Chain Risk](CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md)
- [Vulnerability Management](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md)
- [Change Management](CERG-PRC-CHG-001_Security_Change_Management_Procedure.md)
- [Audit & Evidence Management](CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md)
- [Threat Intelligence](CERG-PRC-TI-001_Threat_Intelligence_Procedure.md)
- [Threat Modeling](CERG-PRC-TM-001_Threat_Modeling_Procedure.md)
- [Incident Response Playbook Set](CERG-PRC-IR-002_Incident_Response_Playbook_Set.md)
- [Lessons Learned & Improvement](CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md)

**Plans & Operational Packages (7 documents)**
- [Incident Response Plan](CERG-PLN-IR-001_Incident_Response_Plan.md)
- [Business Continuity & Disaster Recovery](CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md)
- [NERC-CIP Operational Package](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md)
- [CUI / CMMC Operational Package](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md)
- [SOX ITGC Operational Package](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md)
- [ISO 27001 Operational Package](CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md)
- [Privacy & Data Protection Package](CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md)

**Templates (10 documents)**
- [Risk Register Templates & Reporting](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md)
- [Security Exception Request Form](CERG-TMPL-RM-002_Security_Exception_Request_Form.md)
- [Risk Acceptance Memo Template](CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md)
- [Architecture & Project Intake Form](CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md)
- [Control Evidence & Test Worksheet](CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md)
- [System Security Plan Template](CERG-TMPL-CUI-001_System_Security_Plan_Template.md)
- [POA&M Template](CERG-TMPL-CUI-002_POAM_Template.md)
- [Vendor Security Questionnaire](CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md)
- [Board & CISO Reporting Deck](CERG-TMPL-MTR-001_Board_and_CISO_Reporting_Deck_Template.md)
- [Stakeholder Perception Survey](CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md)

---

## Scales to fit you

The framework describes what operating at [NIST CSF Adaptive maturity](https://www.nist.gov/cyberframework) looks like for a large organization — 14,000 employees, 60-person security team. That's the upper bound. Every team structure, headcount, and engagement model in these documents is designed to scale down. A 5-person team runs the same model with fewer people covering more pillars.

---

## For LLMs and automation

Every document is Markdown. The full corpus is available at [cerg.nexus](https://cerg.nexus):

- **[/llms.txt](https://cerg.nexus/llms.txt)** — document index for AI tools and crawlers
- **[/llms-full.txt](https://cerg.nexus/llms-full.txt)** — full corpus concatenated into one file
- **[Bulk download](https://cerg.nexus/downloads/cerg-docs.zip)** — all 72 documents as a single ZIP

---

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — fork freely, adapt openly, attribute generously.