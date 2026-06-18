# Task A01 Output: Build the corpus map and audit index

## Scope Reviewed
- Files read: `machine-readable/cerg-llm-index.json`, `README.md`, required spine documents listed in the work plan, and generated repository file inventory from the index.
- Sections reviewed: index metadata for all Markdown artifacts; spine document purpose, pillar, role, flow, glossary, and style sections loaded as audit context.
- Files intentionally not reviewed: non-Markdown source files and generated machine-readable YAML/JSON bodies other than the LLM index. Those remain in the machine-readable review zone for later tasks.

## Method
- Steps performed: loaded the LLM index, counted documents by metadata field, compared index paths to repository Markdown paths, separated governed artifacts from readme/meta files, and grouped artifacts into review zones.
- Search terms or scripts used: Python counters over `documents[]`; filesystem `*.md` path comparison excluding ignored build/VCS directories.
- Assumptions avoided: did not treat surprising classifications as wrong; did not edit source documents.

## Corpus Summary
- CERG version in index: `1.44`
- Index generated: `2026-06-18`
- Total indexed Markdown documents: **146**
- Total estimated tokens: **916,259**
- Governed artifacts (non-`META` prefix): **127**
- Readme/meta artifacts (`META` prefix): **19**

### Counts by type
| Type | Count |
|---|---:|
| governance-instrument | 41 |
| job-description | 33 |
| template | 16 |
| standard | 15 |
| readme | 14 |
| procedure | 12 |
| plan | 7 |
| meta | 5 |
| job-family | 2 |
| policy | 1 |

### Counts by prefix
| Prefix | Count |
|---|---:|
| GOV | 41 |
| JD | 33 |
| META | 19 |
| TMPL | 16 |
| STD | 15 |
| PRC | 12 |
| PLN | 7 |
| JF | 2 |
| POL | 1 |

### Counts by pillar
| Pillar | Count |
|---|---:|
| governance | 60 |
| workforce | 35 |
| cross-cutting | 19 |
| engineering | 18 |
| risk | 14 |

### Counts by owner
| Owner | Count |
|---|---:|
| Governance Pillar Leader | 35 |
| (none) | 19 |
| Governance Pillar Leader (Policy & Standards) | 15 |
| Risk Pillar Leader | 13 |
| Engineering Pillar Leader | 12 |
| Governance Pillar Leader (Document Control) | 7 |
| CISO | 5 |
| Engineering Pillar Leader (Platforms) | 5 |
| CMMC / Federal Compliance Manager | 4 |
| Chief Information Security Officer | 3 |
| Risk Register Owner | 3 |
| Vendor Risk Analyst | 3 |
| Engineering Pillar Leader (Application Security) | 2 |
| Governance Pillar Leader (Control Baseline) | 2 |
| Standing IR Team / Incident Commander | 2 |
| Adversarial Testing Lead | 1 |
| Application Security Engineer | 1 |
| Cyber Governance (CERG Pillar) | 1 |
| Engineering Pillar Leader (Endpoint) | 1 |
| Engineering Pillar Leader (Resilience) | 1 |
| Evidence Librarian | 1 |
| Exposure Management Lead | 1 |
| Governance Pillar Leader (OT/NERC-CIP) | 1 |
| Governance Pillar Leader (Reporting) | 1 |
| Governance Pillar Leader (Risk Register) | 1 |
| Governance Pillar Leader (SOX Liaison) | 1 |
| Identity Engineer | 1 |
| NERC-CIP Compliance Manager | 1 |
| Risk Pillar Leader (Detection Engineering) | 1 |
| Risk Pillar Leader / Governance Pillar Leader | 1 |
| Vendor Risk Analyst / Governance Pillar Leader | 1 |

### Counts by status
| Status | Count |
|---|---:|
| Approved | 125 |
| (none) | 19 |
| External Interface | 2 |

## Review Zones
| Zone | Count | Selection rule |
|---|---:|---|
| spine documents | 17 | `spine documents` grouping from path, prefix, and spine ID list |
| governance instruments | 28 | `governance instruments` grouping from path, prefix, and spine ID list |
| standards | 15 | `standards` grouping from path, prefix, and spine ID list |
| procedures | 12 | `procedures` grouping from path, prefix, and spine ID list |
| plans/packages | 7 | `plans/packages` grouping from path, prefix, and spine ID list |
| templates/records | 16 | `templates/records` grouping from path, prefix, and spine ID list |
| workforce | 35 | `workforce` grouping from path, prefix, and spine ID list |
| examples | 6 | `examples` grouping from path, prefix, and spine ID list |
| machine-readable artifacts | 1 | `machine-readable artifacts` grouping from path, prefix, and spine ID list |
| repo meta/adoption/tools | 9 | `repo meta/adoption/tools` grouping from path, prefix, and spine ID list |

### Zone: spine documents
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| README | README | readme | cross-cutting |  |  | `README.md` |
| START-HERE | START-HERE | readme | cross-cutting |  |  | `START-HERE.md` |
| CERG-GOV-AUD-001 | Evidence Quality Standard | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md` |
| CERG-GOV-CAT-001 | Document Catalog and Naming Convention | governance-instrument | governance | Approved | Governance Pillar Leader (Document Control) | `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md` |
| CERG-GOV-CAT-002 | Record Catalog | governance-instrument | governance | Approved | Governance Pillar Leader (Document Control) | `governance/CERG-GOV-CAT-002_Record_Catalog.md` |
| CERG-GOV-CB-001 | Unified Control Baseline | governance-instrument | engineering | Approved | Governance Pillar Leader (Control Baseline) | `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md` |
| CERG-GOV-FLOW-001 | Cross-Pillar Operational Flows | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` |
| CERG-GOV-FRM-001 | CERG Framework | governance-instrument | governance | Approved | CISO | `governance/CERG-GOV-FRM-001_CERG_Framework.md` |
| CERG-GOV-FRM-002 | Framework System Map | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-FRM-002_Framework_System_Map.md` |
| CERG-GOV-GEN-001 | CERG Glossary | governance-instrument | governance | Approved | Governance Pillar Leader (Document Control) | `governance/CERG-GOV-GEN-001_CERG_Glossary.md` |
| CERG-GOV-IMPREG-001 | Program Improvement Register | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md` |
| CERG-GOV-MTR-001 | Metrics Dashboard and Reporting | governance-instrument | governance | Approved | Governance Pillar Leader (Reporting) | `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md` |
| CERG-GOV-OM-001 | CERG Operating Model | governance-instrument | governance | Approved | Chief Information Security Officer | `governance/CERG-GOV-OM-001_CERG_Operating_Model.md` |
| CERG-GOV-RAC-001 | Consolidated Roles and RACI Instrument | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md` |
| CERG-GOV-RMF-001 | Risk Management Framework | governance-instrument | risk | Approved | Cyber Governance (CERG Pillar) | `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md` |
| CERG-GOV-STY-001 | Document Authoring and Style Guide | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md` |
| CERG-POL-001 | Cybersecurity Policy | policy | governance | Approved | Chief Information Security Officer | `governance/CERG-POL-001_Cybersecurity_Policy.md` |

### Zone: governance instruments
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| CERG-GOV-CAL-001 | Annual Security and Governance Calendar | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md` |
| CERG-GOV-CAL-002 | Calibration Checklist | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-CAL-002_Calibration_Checklist.md` |
| CERG-GOV-CEF-001 | Control Effectiveness Framework | governance-instrument | engineering | Approved | Governance Pillar Leader | `governance/CERG-GOV-CEF-001_Control_Effectiveness_Framework.md` |
| CERG-GOV-CJ-001 | Crown Jewel Register and Scenario Library | governance-instrument | governance | Approved | Risk Pillar Leader / Governance Pillar Leader | `governance/CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md` |
| CERG-GOV-CMP-001 | Competency Model and Behavioral Anchors | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md` |
| CERG-GOV-CMX-001 | Compliance Matrix | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-CMX-001_Compliance_Matrix.md` |
| CERG-GOV-CON-001 | Contractor and Non-Employee Staff Integration Guide | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-CON-001_Contractor_and_Non-Employee_Staff_Integration_Guide.md` |
| CERG-GOV-EDG-001 | Edge Register | governance-instrument | governance | Approved | Vendor Risk Analyst / Governance Pillar Leader | `governance/CERG-GOV-EDG-001_Edge_Register.md` |
| CERG-GOV-IMP-001 | Implementation and Adaptation Guide | governance-instrument | governance | Approved | Governance Pillar Leader (Document Control) | `governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md` |
| CERG-GOV-IMP-002 | Adoption Safety Guide | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md` |
| CERG-GOV-IMP-003 | Small Team Adoption Path | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md` |
| CERG-GOV-IMP-004 | Implementation Cards | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-IMP-004_Implementation_Cards.md` |
| CERG-GOV-IMP-005 | Adoption Decision Tree and Dependency Matrix | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md` |
| CERG-GOV-IMP-006 | Role Based Implementation Checklists | governance-instrument | governance | Approved | Governance Pillar Leader | `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md` |
| CERG-GOV-IMP-007 | Role Reader Paths | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md` |
| CERG-GOV-JA-001 | Job Architecture and Grade Framework | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md` |
| CERG-GOV-JD-001 | CERG Job Descriptions | meta | cross-cutting | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-JD-001_CERG_Job_Descriptions.md` |
| CERG-GOV-MAT-001 | Maturity Self Assessment and Scorecard | governance-instrument | governance | Approved | Governance Pillar Leader (Document Control) | `governance/CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md` |
| CERG-GOV-ONB-001 | Onboarding and Integration Program | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md` |
| CERG-GOV-PERF-001 | Performance Management and Promotion Framework | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md` |
| CERG-GOV-SLC-001 | CERG Service Level Commitments | governance-instrument | governance | Approved | Chief Information Security Officer | `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md` |
| CERG-GOV-STY-002 | Style Compliance Tracker | governance-instrument | governance | Approved | Governance Pillar Leader (Document Control) | `governance/CERG-GOV-STY-002_Style_Compliance_Tracker.md` |
| CERG-GOV-SUCC-001 | Succession Planning and Talent Review Framework | governance-instrument | governance | Approved | CISO | `governance/CERG-GOV-SUCC-001_Succession_Planning_and_Talent_Review_Framework.md` |
| CERG-GOV-TAX-001 | Risk Taxonomy | governance-instrument | risk | Approved | Risk Pillar Leader | `governance/CERG-GOV-TAX-001_Risk_Taxonomy.md` |
| CERG-GOV-TRC-001 | Control to Procedure Traceability Matrix | governance-instrument | engineering | Approved | Governance Pillar Leader (Control Baseline) | `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md` |
| CERG-GOV-TRN-001 | Training Development and Certification Framework | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md` |
| CERG-GOV-VAR-001 | Organization Adaptation Profile | governance-instrument | governance | Approved | Governance Pillar Leader (Document Control) | `governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md` |
| CERG-GOV-WFP-001 | Workforce Planning and Capacity Model | governance-instrument | governance | Approved | Governance Pillar Leader (Policy & Standards) | `governance/CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md` |

### Zone: standards
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| CERG-STD-AC-001 | Access Management Standard | standard | engineering | Approved | Governance Pillar Leader | `standards/CERG-STD-AC-001_Access_Management_Standard.md` |
| CERG-STD-AI-001 | Artificial Intelligence Security Standard | standard | engineering | Approved | Engineering Pillar Leader (Application Security) | `standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md` |
| CERG-STD-AM-001 | Asset Management and Inventory Standard | standard | engineering | Approved | Engineering Pillar Leader (Platforms) | `standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md` |
| CERG-STD-CFG-001 | Secure Configuration Baseline Standard DISH | standard | engineering | Approved | Engineering Pillar Leader (Platforms) | `standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md` |
| CERG-STD-CR-001 | Cryptography and Key Management Standard | standard | engineering | Approved | Engineering Pillar Leader (Platforms) | `standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md` |
| CERG-STD-CUI-001 | CUI Handling Standard | standard | engineering | Approved | CMMC / Federal Compliance Manager | `standards/CERG-STD-CUI-001_CUI_Handling_Standard.md` |
| CERG-STD-DG-001 | Data Governance and Classification Standard | standard | engineering | Approved | Governance Pillar Leader (Policy & Standards) | `standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md` |
| CERG-STD-EP-001 | Endpoint and Mobile Security Standard | standard | engineering | Approved | Engineering Pillar Leader (Endpoint) | `standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md` |
| CERG-STD-IT-001 | IT Cloud SaaS Security Standard | standard | engineering | Approved | Governance Pillar Leader | `standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md` |
| CERG-STD-LM-001 | Logging Monitoring and Detection Standard | standard | engineering | Approved | Risk Pillar Leader (Detection Engineering) | `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md` |
| CERG-STD-MSG-001 | Email and Messaging Security Standard | standard | engineering | Approved | Engineering Pillar Leader (Platforms) | `standards/CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md` |
| CERG-STD-NET-001 | Network Security and Segmentation Standard | standard | engineering | Approved | Engineering Pillar Leader (Platforms) | `standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md` |
| CERG-STD-OT-001 | Grid Control Systems Security Standard | standard | engineering | Approved | Governance Pillar Leader (OT/NERC-CIP) | `standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md` |
| CERG-STD-RES-001 | Cyber Resilience and Backup Standard | standard | engineering | Approved | Engineering Pillar Leader (Resilience) | `standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md` |
| CERG-STD-SDL-001 | Secure Software Development and Application Security Standard | standard | engineering | Approved | Engineering Pillar Leader (Application Security) | `standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md` |

### Zone: procedures
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| CERG-PRC-AC-002 | Access Management Runbook | procedure | risk | Approved | Identity Engineer | `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md` |
| CERG-PRC-AR-001 | Architecture Review and Project Intake Procedure | procedure | risk | Approved | Engineering Pillar Leader | `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md` |
| CERG-PRC-AUD-001 | Audit and Evidence Management Procedure | procedure | risk | Approved | Governance Pillar Leader | `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md` |
| CERG-PRC-AV-001 | Adversarial Validation Procedure | procedure | risk | Approved | Adversarial Testing Lead | `procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md` |
| CERG-PRC-CHG-001 | Security Change Management Procedure | procedure | risk | Approved | Engineering Pillar Leader | `procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md` |
| CERG-PRC-IR-002 | Incident Response Playbook Set | procedure | risk | External Interface | Standing IR Team / Incident Commander | `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md` |
| CERG-PRC-LL-001 | Lessons Learned and Program Improvement Procedure | procedure | risk | Approved | Governance Pillar Leader | `procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md` |
| CERG-PRC-RM-001 | Risk Register and Exception Process | procedure | risk | Approved | Risk Register Owner | `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md` |
| CERG-PRC-TI-001 | Threat Intelligence Procedure | procedure | risk | Approved | Risk Pillar Leader | `procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md` |
| CERG-PRC-TM-001 | Threat Modeling Procedure | procedure | risk | Approved | Risk Pillar Leader | `procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md` |
| CERG-PRC-TPRM-001 | Third Party and Supply Chain Risk Procedure | procedure | risk | Approved | Vendor Risk Analyst | `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md` |
| CERG-PRC-VM-001 | Exposure Management Procedure | procedure | risk | Approved | Exposure Management Lead | `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md` |

### Zone: plans/packages
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| CERG-PLN-BC-001 | Business Continuity and Disaster Recovery Plan | plan | governance | Approved | Governance Pillar Leader | `plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md` |
| CERG-PLN-CIP-001 | NERC CIP Operational Package | plan | governance | Approved | NERC-CIP Compliance Manager | `plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md` |
| CERG-PLN-CUI-001 | CUI CMMC Operational Package | plan | governance | Approved | CMMC / Federal Compliance Manager | `plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md` |
| CERG-PLN-IR-001 | Incident Response Plan | plan | governance | External Interface | Standing IR Team / Incident Commander | `plans/CERG-PLN-IR-001_Incident_Response_Plan.md` |
| CERG-PLN-ISO-001 | ISO IEC 27001 Operational Package | plan | governance | Approved | Governance Pillar Leader | `plans/CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md` |
| CERG-PLN-PRIV-001 | Privacy and Data Protection Operational Package | plan | governance | Approved | Governance Pillar Leader | `plans/CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md` |
| CERG-PLN-SOX-001 | SOX ITGC Operational Package | plan | governance | Approved | Governance Pillar Leader (SOX Liaison) | `plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md` |

### Zone: templates/records
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| CERG-TMPL-AI-001 | AI Intake and Sanctioning Template | template | governance | Approved | Governance Pillar Leader | `templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md` |
| CERG-TMPL-AI-002 | Sanctioned AI Tools Register Template | template | governance | Approved | Governance Pillar Leader | `templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md` |
| CERG-TMPL-AI-003 | AI System and Model Register Template | template | governance | Approved | Application Security Engineer | `templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md` |
| CERG-TMPL-AR-001 | Architecture and Project Intake Form | template | governance | Approved | Engineering Pillar Leader | `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md` |
| CERG-TMPL-AUD-001 | Control Evidence and Test Worksheet | template | governance | Approved | Evidence Librarian | `templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md` |
| CERG-TMPL-CUI-001 | System Security Plan Template | template | governance | Approved | CMMC / Federal Compliance Manager | `templates/CERG-TMPL-CUI-001_System_Security_Plan_Template.md` |
| CERG-TMPL-CUI-002 | POAM Template | template | governance | Approved | CMMC / Federal Compliance Manager | `templates/CERG-TMPL-CUI-002_POAM_Template.md` |
| CERG-TMPL-GOV-001 | Stakeholder Perception Survey | template | governance | Approved | Governance Pillar Leader | `templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md` |
| CERG-TMPL-MTR-001 | Board and CISO Reporting Deck Template | template | governance | Approved | Governance Pillar Leader | `templates/CERG-TMPL-MTR-001_Board_and_CISO_Reporting_Deck_Template.md` |
| CERG-TMPL-RM-001 | Risk Register Templates and Reporting | template | governance | Approved | Governance Pillar Leader (Risk Register) | `templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md` |
| CERG-TMPL-RM-002 | Security Exception Request Form | template | governance | Approved | Risk Register Owner | `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md` |
| CERG-TMPL-RM-003 | Risk Acceptance Memo Template | template | governance | Approved | Risk Pillar Leader | `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md` |
| CERG-TMPL-RM-004 | Risk Acceptance Request Form | template | governance | Approved | Risk Register Owner | `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md` |
| CERG-TMPL-SAAS-001 | SaaS Evidence Collection Checklist | template | governance | Approved | Governance Pillar Leader | `templates/CERG-TMPL-SAAS-001_SaaS_Evidence_Collection_Checklist.md` |
| CERG-TMPL-SBOM-001 | SBOM Evidence Collection Checklist | template | governance | Approved | Vendor Risk Analyst | `templates/CERG-TMPL-SBOM-001_SBOM_Evidence_Collection_Checklist.md` |
| CERG-TMPL-TPRM-001 | Vendor Security Questionnaire and Assessment Template | template | governance | Approved | Vendor Risk Analyst | `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md` |

### Zone: workforce
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| CERG-GOV-JF-001 | Job Families Overview | job-family | workforce | Approved | Governance Pillar Leader (Policy & Standards) | `roles/CERG-GOV-JF-001_Job_Families_Overview.md` |
| CERG-GOV-JF-002 | NICE Workforce Framework Crosswalk | job-family | workforce | Approved | Governance Pillar Leader (Policy & Standards) | `roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md` |
| README-roles | README | job-description | workforce |  |  | `roles/README.md` |
| CERG-GOV-JD-ADJUNCT-000 | Incident Response Family | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-000_Incident_Response_Family.md` |
| CERG-GOV-JD-ADJUNCT-001 | Incident Commander | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md` |
| CERG-GOV-JD-ADJUNCT-002 | Lead Investigator | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-002_Lead_Investigator.md` |
| CERG-GOV-JD-EXEC-000 | Executive Leadership Family | job-description | workforce | Approved | CISO | `roles/jf-exec/CERG-GOV-JD-EXEC-000_Executive_Leadership_Family.md` |
| CERG-GOV-JD-EXEC-001 | Chief Information Security Officer | job-description | workforce | Approved | CISO | `roles/jf-exec/CERG-GOV-JD-EXEC-001_Chief_Information_Security_Officer.md` |
| CERG-GOV-JD-EXEC-002 | Executive Sponsor | job-description | workforce | Approved | CISO | `roles/jf-exec/CERG-GOV-JD-EXEC-002_Executive_Sponsor.md` |
| CERG-GOV-JD-GOVCOMP-000 | Governance Compliance Family | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-000_Governance_Compliance_Family.md` |
| CERG-GOV-JD-GOVCOMP-001 | NERC-CIP Compliance Manager | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-001_NERC-CIP_Compliance_Manager.md` |
| CERG-GOV-JD-GOVCOMP-002 | CMMC Federal Compliance Manager | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-002_CMMC_Federal_Compliance_Manager.md` |
| CERG-GOV-JD-GOVCOMP-003 | SOX ITGC Lead | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-003_SOX_ITGC_Lead.md` |
| CERG-GOV-JD-GOVCOMP-004 | Policy and Standards Manager | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-004_Policy_and_Standards_Manager.md` |
| CERG-GOV-JD-GOVCOMP-005 | Risk Register Owner | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-005_Risk_Register_Owner.md` |
| CERG-GOV-JD-GOVCOMP-006 | Evidence Librarian | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-006_Evidence_Librarian.md` |
| CERG-GOV-JD-GOVCOMP-007 | Governance Pillar Leader | job-description | workforce | Approved | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-007_Governance_Pillar_Leader.md` |
| CERG-GOV-JD-RISKOPS-000 | Risk Operations Family | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-000_Risk_Operations_Family.md` |
| CERG-GOV-JD-RISKOPS-001 | Exposure Management Lead | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md` |
| CERG-GOV-JD-RISKOPS-002 | Adversarial Testing Lead | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-002_Adversarial_Testing_Lead.md` |
| CERG-GOV-JD-RISKOPS-003 | Threat Intelligence Analyst | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-003_Threat_Intelligence_Analyst.md` |
| CERG-GOV-JD-RISKOPS-004 | Detection Engineer | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md` |
| CERG-GOV-JD-RISKOPS-005 | OT Risk Analyst | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-005_OT_Risk_Analyst.md` |
| CERG-GOV-JD-RISKOPS-006 | Identity Risk Analyst | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-006_Identity_Risk_Analyst.md` |
| CERG-GOV-JD-RISKOPS-007 | Vendor Risk Analyst | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md` |
| CERG-GOV-JD-RISKOPS-008 | Risk Pillar Leader | job-description | workforce | Approved | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-008_Risk_Pillar_Leader.md` |
| CERG-GOV-JD-SECENG-000 | Security Engineering Family | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-000_Security_Engineering_Family.md` |
| CERG-GOV-JD-SECENG-001 | Cloud Security Engineer | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-001_Cloud_Security_Engineer.md` |
| CERG-GOV-JD-SECENG-002 | Identity Engineer | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-002_Identity_Engineer.md` |
| CERG-GOV-JD-SECENG-003 | OT Security Engineer | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-003_OT_Security_Engineer.md` |
| CERG-GOV-JD-SECENG-004 | Application Security Engineer | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-004_Application_Security_Engineer.md` |
| CERG-GOV-JD-SECENG-005 | Endpoint Engineer | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-005_Endpoint_Engineer.md` |
| CERG-GOV-JD-SECENG-006 | Cryptography Engineer | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-006_Cryptography_Engineer.md` |
| CERG-GOV-JD-SECENG-007 | Engineering Pillar Leader | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-007_Engineering_Pillar_Leader.md` |
| CERG-GOV-JD-SECENG-008 | Pre-production Reviewer | job-description | workforce | Approved | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md` |

### Zone: examples
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| README-examples | README | readme | cross-cutting |  |  | `examples/README.md` |
| README-examples-day-in-the-life | README | readme | cross-cutting |  |  | `examples/day-in-the-life/README.md` |
| story-10-new-ciso-90-days | story-10-new-ciso-90-days | meta | cross-cutting |  |  | `examples/day-in-the-life/story-10-new-ciso-90-days.md` |
| story-8-cerg-lite-maria | story-8-cerg-lite-maria | meta | cross-cutting |  |  | `examples/day-in-the-life/story-8-cerg-lite-maria.md` |
| story-9-f-01-control-intent | story-9-f-01-control-intent | meta | cross-cutting |  |  | `examples/day-in-the-life/story-9-f-01-control-intent.md` |
| README-examples-regulated-utility-profile | README | readme | cross-cutting |  |  | `examples/regulated-utility-profile/README.md` |

### Zone: machine-readable artifacts
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| README-machine-readable | README | readme | cross-cutting |  |  | `machine-readable/README.md` |

### Zone: repo meta/adoption/tools
| ID | Title | Type | Pillar | Status | Owner | Path |
|---|---|---|---|---|---|---|
| ADOPT-WITH-AN-AGENT | ADOPT-WITH-AN-AGENT | readme | cross-cutting |  |  | `ADOPT-WITH-AN-AGENT.md` |
| AGENTS | AGENTS | readme | cross-cutting |  |  | `AGENTS.md` |
| BEGINNER-GUIDE | BEGINNER-GUIDE | readme | cross-cutting |  |  | `BEGINNER-GUIDE.md` |
| CODE_OF_CONDUCT | CODE OF CONDUCT | readme | cross-cutting |  |  | `CODE_OF_CONDUCT.md` |
| CONTRIBUTING | CONTRIBUTING | readme | cross-cutting |  |  | `CONTRIBUTING.md` |
| SECURITY | SECURITY | readme | cross-cutting |  |  | `SECURITY.md` |
| README-adoption-packs-cerg-lite | README | readme | cross-cutting |  |  | `adoption-packs/cerg-lite/README.md` |
| agent-prompt | agent-prompt | meta | cross-cutting |  |  | `adoption-packs/cerg-lite/agent-prompt.md` |
| README-tools-policy-as-code | README | readme | cross-cutting |  |  | `tools/policy-as-code/README.md` |

## Governed Artifact Index
Every governed Markdown artifact from the index is listed below. Readme/meta files are separated in the next section.

| ID | Title | Path | Type | Pillar | Owner | Summary |
|---|---|---|---|---|---|---|
| CERG-GOV-AUD-001 | Evidence Quality Standard | `governance/CERG-GOV-AUD-001_Evidence_Quality_Standard.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Evidence Quality Standard |
| CERG-GOV-CAL-001 | Annual Security and Governance Calendar | `governance/CERG-GOV-CAL-001_Annual_Security_and_Governance_Calendar.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Annual Security and Governance Calendar |
| CERG-GOV-CAL-002 | Calibration Checklist | `governance/CERG-GOV-CAL-002_Calibration_Checklist.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Calibration Checklist |
| CERG-GOV-CAT-001 | Document Catalog and Naming Convention | `governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md` | governance-instrument | governance | Governance Pillar Leader (Document Control) | CERG GOV document: Document Catalog and Naming Convention |
| CERG-GOV-CAT-002 | Record Catalog | `governance/CERG-GOV-CAT-002_Record_Catalog.md` | governance-instrument | governance | Governance Pillar Leader (Document Control) | CERG GOV document: Record Catalog |
| CERG-GOV-CB-001 | Unified Control Baseline | `governance/CERG-GOV-CB-001_Unified_Control_Baseline.md` | governance-instrument | engineering | Governance Pillar Leader (Control Baseline) | CERG GOV document: Unified Control Baseline |
| CERG-GOV-CEF-001 | Control Effectiveness Framework | `governance/CERG-GOV-CEF-001_Control_Effectiveness_Framework.md` | governance-instrument | engineering | Governance Pillar Leader | CERG GOV document: Control Effectiveness Framework |
| CERG-GOV-CJ-001 | Crown Jewel Register and Scenario Library | `governance/CERG-GOV-CJ-001_Crown_Jewel_Register_and_Scenario_Library.md` | governance-instrument | governance | Risk Pillar Leader / Governance Pillar Leader | CERG GOV document: Crown Jewel Register and Scenario Library |
| CERG-GOV-CMP-001 | Competency Model and Behavioral Anchors | `governance/CERG-GOV-CMP-001_Competency_Model_and_Behavioral_Anchors.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Competency Model and Behavioral Anchors |
| CERG-GOV-CMX-001 | Compliance Matrix | `governance/CERG-GOV-CMX-001_Compliance_Matrix.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Compliance Matrix |
| CERG-GOV-CON-001 | Contractor and Non-Employee Staff Integration Guide | `governance/CERG-GOV-CON-001_Contractor_and_Non-Employee_Staff_Integration_Guide.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Contractor and Non-Employee Staff Integration Guide |
| CERG-GOV-EDG-001 | Edge Register | `governance/CERG-GOV-EDG-001_Edge_Register.md` | governance-instrument | governance | Vendor Risk Analyst / Governance Pillar Leader | CERG GOV document: Edge Register |
| CERG-GOV-FLOW-001 | Cross-Pillar Operational Flows | `governance/CERG-GOV-FLOW-001_Cross-Pillar_Operational_Flows.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Cross-Pillar Operational Flows |
| CERG-GOV-FRM-001 | CERG Framework | `governance/CERG-GOV-FRM-001_CERG_Framework.md` | governance-instrument | governance | CISO | CERG GOV document: CERG Framework |
| CERG-GOV-FRM-002 | Framework System Map | `governance/CERG-GOV-FRM-002_Framework_System_Map.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Framework System Map |
| CERG-GOV-GEN-001 | CERG Glossary | `governance/CERG-GOV-GEN-001_CERG_Glossary.md` | governance-instrument | governance | Governance Pillar Leader (Document Control) | CERG GOV document: CERG Glossary |
| CERG-GOV-IMP-001 | Implementation and Adaptation Guide | `governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md` | governance-instrument | governance | Governance Pillar Leader (Document Control) | CERG GOV document: Implementation and Adaptation Guide |
| CERG-GOV-IMP-002 | Adoption Safety Guide | `governance/CERG-GOV-IMP-002_Adoption_Safety_Guide.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Adoption Safety Guide |
| CERG-GOV-IMP-003 | Small Team Adoption Path | `governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Small Team Adoption Path |
| CERG-GOV-IMP-004 | Implementation Cards | `governance/CERG-GOV-IMP-004_Implementation_Cards.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Implementation Cards |
| CERG-GOV-IMP-005 | Adoption Decision Tree and Dependency Matrix | `governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Adoption Decision Tree and Dependency Matrix |
| CERG-GOV-IMP-006 | Role Based Implementation Checklists | `governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Role Based Implementation Checklists |
| CERG-GOV-IMP-007 | Role Reader Paths | `governance/CERG-GOV-IMP-007_Role_Reader_Paths.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Role Reader Paths |
| CERG-GOV-IMPREG-001 | Program Improvement Register | `governance/CERG-GOV-IMPREG-001_Program_Improvement_Register.md` | governance-instrument | governance | Governance Pillar Leader | CERG GOV document: Program Improvement Register |
| CERG-GOV-JA-001 | Job Architecture and Grade Framework | `governance/CERG-GOV-JA-001_Job_Architecture_and_Grade_Framework.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Job Architecture and Grade Framework |
| CERG-GOV-JD-ADJUNCT-000 | Incident Response Family | `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-000_Incident_Response_Family.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Incident Response Family |
| CERG-GOV-JD-ADJUNCT-001 | Incident Commander | `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Incident Commander |
| CERG-GOV-JD-ADJUNCT-002 | Lead Investigator | `roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-002_Lead_Investigator.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Lead Investigator |
| CERG-GOV-JD-EXEC-000 | Executive Leadership Family | `roles/jf-exec/CERG-GOV-JD-EXEC-000_Executive_Leadership_Family.md` | job-description | workforce | CISO | CERG JD document: Executive Leadership Family |
| CERG-GOV-JD-EXEC-001 | Chief Information Security Officer | `roles/jf-exec/CERG-GOV-JD-EXEC-001_Chief_Information_Security_Officer.md` | job-description | workforce | CISO | CERG JD document: Chief Information Security Officer |
| CERG-GOV-JD-EXEC-002 | Executive Sponsor | `roles/jf-exec/CERG-GOV-JD-EXEC-002_Executive_Sponsor.md` | job-description | workforce | CISO | CERG JD document: Executive Sponsor |
| CERG-GOV-JD-GOVCOMP-000 | Governance Compliance Family | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-000_Governance_Compliance_Family.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Governance Compliance Family |
| CERG-GOV-JD-GOVCOMP-001 | NERC-CIP Compliance Manager | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-001_NERC-CIP_Compliance_Manager.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: NERC-CIP Compliance Manager |
| CERG-GOV-JD-GOVCOMP-002 | CMMC Federal Compliance Manager | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-002_CMMC_Federal_Compliance_Manager.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: CMMC Federal Compliance Manager |
| CERG-GOV-JD-GOVCOMP-003 | SOX ITGC Lead | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-003_SOX_ITGC_Lead.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: SOX ITGC Lead |
| CERG-GOV-JD-GOVCOMP-004 | Policy and Standards Manager | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-004_Policy_and_Standards_Manager.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Policy and Standards Manager |
| CERG-GOV-JD-GOVCOMP-005 | Risk Register Owner | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-005_Risk_Register_Owner.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Risk Register Owner |
| CERG-GOV-JD-GOVCOMP-006 | Evidence Librarian | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-006_Evidence_Librarian.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Evidence Librarian |
| CERG-GOV-JD-GOVCOMP-007 | Governance Pillar Leader | `roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-007_Governance_Pillar_Leader.md` | job-description | workforce | Governance Pillar Leader | CERG JD document: Governance Pillar Leader |
| CERG-GOV-JD-RISKOPS-000 | Risk Operations Family | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-000_Risk_Operations_Family.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Risk Operations Family |
| CERG-GOV-JD-RISKOPS-001 | Exposure Management Lead | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Exposure Management Lead |
| CERG-GOV-JD-RISKOPS-002 | Adversarial Testing Lead | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-002_Adversarial_Testing_Lead.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Adversarial Testing Lead |
| CERG-GOV-JD-RISKOPS-003 | Threat Intelligence Analyst | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-003_Threat_Intelligence_Analyst.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Threat Intelligence Analyst |
| CERG-GOV-JD-RISKOPS-004 | Detection Engineer | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Detection Engineer |
| CERG-GOV-JD-RISKOPS-005 | OT Risk Analyst | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-005_OT_Risk_Analyst.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: OT Risk Analyst |
| CERG-GOV-JD-RISKOPS-006 | Identity Risk Analyst | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-006_Identity_Risk_Analyst.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Identity Risk Analyst |
| CERG-GOV-JD-RISKOPS-007 | Vendor Risk Analyst | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Vendor Risk Analyst |
| CERG-GOV-JD-RISKOPS-008 | Risk Pillar Leader | `roles/jf-riskops/CERG-GOV-JD-RISKOPS-008_Risk_Pillar_Leader.md` | job-description | workforce | Risk Pillar Leader | CERG JD document: Risk Pillar Leader |
| CERG-GOV-JD-SECENG-000 | Security Engineering Family | `roles/jf-seceng/CERG-GOV-JD-SECENG-000_Security_Engineering_Family.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Security Engineering Family |
| CERG-GOV-JD-SECENG-001 | Cloud Security Engineer | `roles/jf-seceng/CERG-GOV-JD-SECENG-001_Cloud_Security_Engineer.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Cloud Security Engineer |
| CERG-GOV-JD-SECENG-002 | Identity Engineer | `roles/jf-seceng/CERG-GOV-JD-SECENG-002_Identity_Engineer.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Identity Engineer |
| CERG-GOV-JD-SECENG-003 | OT Security Engineer | `roles/jf-seceng/CERG-GOV-JD-SECENG-003_OT_Security_Engineer.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: OT Security Engineer |
| CERG-GOV-JD-SECENG-004 | Application Security Engineer | `roles/jf-seceng/CERG-GOV-JD-SECENG-004_Application_Security_Engineer.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Application Security Engineer |
| CERG-GOV-JD-SECENG-005 | Endpoint Engineer | `roles/jf-seceng/CERG-GOV-JD-SECENG-005_Endpoint_Engineer.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Endpoint Engineer |
| CERG-GOV-JD-SECENG-006 | Cryptography Engineer | `roles/jf-seceng/CERG-GOV-JD-SECENG-006_Cryptography_Engineer.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Cryptography Engineer |
| CERG-GOV-JD-SECENG-007 | Engineering Pillar Leader | `roles/jf-seceng/CERG-GOV-JD-SECENG-007_Engineering_Pillar_Leader.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Engineering Pillar Leader |
| CERG-GOV-JD-SECENG-008 | Pre-production Reviewer | `roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md` | job-description | workforce | Engineering Pillar Leader | CERG JD document: Pre-production Reviewer |
| CERG-GOV-JF-001 | Job Families Overview | `roles/CERG-GOV-JF-001_Job_Families_Overview.md` | job-family | workforce | Governance Pillar Leader (Policy & Standards) | CERG JF document: Job Families Overview |
| CERG-GOV-JF-002 | NICE Workforce Framework Crosswalk | `roles/CERG-GOV-JF-002_NICE_Workforce_Framework_Crosswalk.md` | job-family | workforce | Governance Pillar Leader (Policy & Standards) | CERG JF document: NICE Workforce Framework Crosswalk |
| CERG-GOV-MAT-001 | Maturity Self Assessment and Scorecard | `governance/CERG-GOV-MAT-001_Maturity_Self_Assessment_and_Scorecard.md` | governance-instrument | governance | Governance Pillar Leader (Document Control) | CERG GOV document: Maturity Self Assessment and Scorecard |
| CERG-GOV-MTR-001 | Metrics Dashboard and Reporting | `governance/CERG-GOV-MTR-001_Metrics_Dashboard_and_Reporting.md` | governance-instrument | governance | Governance Pillar Leader (Reporting) | CERG GOV document: Metrics Dashboard and Reporting |
| CERG-GOV-OM-001 | CERG Operating Model | `governance/CERG-GOV-OM-001_CERG_Operating_Model.md` | governance-instrument | governance | Chief Information Security Officer | CERG GOV document: CERG Operating Model |
| CERG-GOV-ONB-001 | Onboarding and Integration Program | `governance/CERG-GOV-ONB-001_Onboarding_and_Integration_Program.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Onboarding and Integration Program |
| CERG-GOV-PERF-001 | Performance Management and Promotion Framework | `governance/CERG-GOV-PERF-001_Performance_Management_and_Promotion_Framework.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Performance Management and Promotion Framework |
| CERG-GOV-RAC-001 | Consolidated Roles and RACI Instrument | `governance/CERG-GOV-RAC-001_Consolidated_Roles_and_RACI_Instrument.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Consolidated Roles and RACI Instrument |
| CERG-GOV-RMF-001 | Risk Management Framework | `governance/CERG-GOV-RMF-001_Risk_Management_Framework.md` | governance-instrument | risk | Cyber Governance (CERG Pillar) | CERG GOV document: Risk Management Framework |
| CERG-GOV-SLC-001 | CERG Service Level Commitments | `governance/CERG-GOV-SLC-001_CERG_Service_Level_Commitments.md` | governance-instrument | governance | Chief Information Security Officer | CERG GOV document: CERG Service Level Commitments |
| CERG-GOV-STY-001 | Document Authoring and Style Guide | `governance/CERG-GOV-STY-001_Document_Authoring_and_Style_Guide.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Document Authoring and Style Guide |
| CERG-GOV-STY-002 | Style Compliance Tracker | `governance/CERG-GOV-STY-002_Style_Compliance_Tracker.md` | governance-instrument | governance | Governance Pillar Leader (Document Control) | CERG GOV document: Style Compliance Tracker |
| CERG-GOV-SUCC-001 | Succession Planning and Talent Review Framework | `governance/CERG-GOV-SUCC-001_Succession_Planning_and_Talent_Review_Framework.md` | governance-instrument | governance | CISO | CERG GOV document: Succession Planning and Talent Review Framework |
| CERG-GOV-TAX-001 | Risk Taxonomy | `governance/CERG-GOV-TAX-001_Risk_Taxonomy.md` | governance-instrument | risk | Risk Pillar Leader | CERG GOV document: Risk Taxonomy |
| CERG-GOV-TRC-001 | Control to Procedure Traceability Matrix | `governance/CERG-GOV-TRC-001_Control_to_Procedure_Traceability_Matrix.md` | governance-instrument | engineering | Governance Pillar Leader (Control Baseline) | CERG GOV document: Control to Procedure Traceability Matrix |
| CERG-GOV-TRN-001 | Training Development and Certification Framework | `governance/CERG-GOV-TRN-001_Training_Development_and_Certification_Framework.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Training Development and Certification Framework |
| CERG-GOV-VAR-001 | Organization Adaptation Profile | `governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md` | governance-instrument | governance | Governance Pillar Leader (Document Control) | CERG GOV document: Organization Adaptation Profile |
| CERG-GOV-WFP-001 | Workforce Planning and Capacity Model | `governance/CERG-GOV-WFP-001_Workforce_Planning_and_Capacity_Model.md` | governance-instrument | governance | Governance Pillar Leader (Policy & Standards) | CERG GOV document: Workforce Planning and Capacity Model |
| CERG-PLN-BC-001 | Business Continuity and Disaster Recovery Plan | `plans/CERG-PLN-BC-001_Business_Continuity_and_Disaster_Recovery_Plan.md` | plan | governance | Governance Pillar Leader | CERG PLN document: Business Continuity and Disaster Recovery Plan |
| CERG-PLN-CIP-001 | NERC CIP Operational Package | `plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md` | plan | governance | NERC-CIP Compliance Manager | CERG PLN document: NERC CIP Operational Package |
| CERG-PLN-CUI-001 | CUI CMMC Operational Package | `plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md` | plan | governance | CMMC / Federal Compliance Manager | CERG PLN document: CUI CMMC Operational Package |
| CERG-PLN-IR-001 | Incident Response Plan | `plans/CERG-PLN-IR-001_Incident_Response_Plan.md` | plan | governance | Standing IR Team / Incident Commander | CERG PLN document: Incident Response Plan |
| CERG-PLN-ISO-001 | ISO IEC 27001 Operational Package | `plans/CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md` | plan | governance | Governance Pillar Leader | CERG PLN document: ISO IEC 27001 Operational Package |
| CERG-PLN-PRIV-001 | Privacy and Data Protection Operational Package | `plans/CERG-PLN-PRIV-001_Privacy_and_Data_Protection_Operational_Package.md` | plan | governance | Governance Pillar Leader | CERG PLN document: Privacy and Data Protection Operational Package |
| CERG-PLN-SOX-001 | SOX ITGC Operational Package | `plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md` | plan | governance | Governance Pillar Leader (SOX Liaison) | CERG PLN document: SOX ITGC Operational Package |
| CERG-POL-001 | Cybersecurity Policy | `governance/CERG-POL-001_Cybersecurity_Policy.md` | policy | governance | Chief Information Security Officer | CERG POL document: Cybersecurity Policy |
| CERG-PRC-AC-002 | Access Management Runbook | `procedures/CERG-PRC-AC-002_Access_Management_Runbook.md` | procedure | risk | Identity Engineer | CERG PRC document: Access Management Runbook |
| CERG-PRC-AR-001 | Architecture Review and Project Intake Procedure | `procedures/CERG-PRC-AR-001_Architecture_Review_and_Project_Intake_Procedure.md` | procedure | risk | Engineering Pillar Leader | CERG PRC document: Architecture Review and Project Intake Procedure |
| CERG-PRC-AUD-001 | Audit and Evidence Management Procedure | `procedures/CERG-PRC-AUD-001_Audit_and_Evidence_Management_Procedure.md` | procedure | risk | Governance Pillar Leader | CERG PRC document: Audit and Evidence Management Procedure |
| CERG-PRC-AV-001 | Adversarial Validation Procedure | `procedures/CERG-PRC-AV-001_Adversarial_Validation_Procedure.md` | procedure | risk | Adversarial Testing Lead | CERG PRC document: Adversarial Validation Procedure |
| CERG-PRC-CHG-001 | Security Change Management Procedure | `procedures/CERG-PRC-CHG-001_Security_Change_Management_Procedure.md` | procedure | risk | Engineering Pillar Leader | CERG PRC document: Security Change Management Procedure |
| CERG-PRC-IR-002 | Incident Response Playbook Set | `procedures/CERG-PRC-IR-002_Incident_Response_Playbook_Set.md` | procedure | risk | Standing IR Team / Incident Commander | CERG PRC document: Incident Response Playbook Set |
| CERG-PRC-LL-001 | Lessons Learned and Program Improvement Procedure | `procedures/CERG-PRC-LL-001_Lessons_Learned_and_Program_Improvement_Procedure.md` | procedure | risk | Governance Pillar Leader | CERG PRC document: Lessons Learned and Program Improvement Procedure |
| CERG-PRC-RM-001 | Risk Register and Exception Process | `procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md` | procedure | risk | Risk Register Owner | CERG PRC document: Risk Register and Exception Process |
| CERG-PRC-TI-001 | Threat Intelligence Procedure | `procedures/CERG-PRC-TI-001_Threat_Intelligence_Procedure.md` | procedure | risk | Risk Pillar Leader | CERG PRC document: Threat Intelligence Procedure |
| CERG-PRC-TM-001 | Threat Modeling Procedure | `procedures/CERG-PRC-TM-001_Threat_Modeling_Procedure.md` | procedure | risk | Risk Pillar Leader | CERG PRC document: Threat Modeling Procedure |
| CERG-PRC-TPRM-001 | Third Party and Supply Chain Risk Procedure | `procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md` | procedure | risk | Vendor Risk Analyst | CERG PRC document: Third Party and Supply Chain Risk Procedure |
| CERG-PRC-VM-001 | Exposure Management Procedure | `procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md` | procedure | risk | Exposure Management Lead | CERG PRC document: Exposure Management Procedure |
| CERG-STD-AC-001 | Access Management Standard | `standards/CERG-STD-AC-001_Access_Management_Standard.md` | standard | engineering | Governance Pillar Leader | CERG STD document: Access Management Standard |
| CERG-STD-AI-001 | Artificial Intelligence Security Standard | `standards/CERG-STD-AI-001_Artificial_Intelligence_Security_Standard.md` | standard | engineering | Engineering Pillar Leader (Application Security) | CERG STD document: Artificial Intelligence Security Standard |
| CERG-STD-AM-001 | Asset Management and Inventory Standard | `standards/CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md` | standard | engineering | Engineering Pillar Leader (Platforms) | CERG STD document: Asset Management and Inventory Standard |
| CERG-STD-CFG-001 | Secure Configuration Baseline Standard DISH | `standards/CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md` | standard | engineering | Engineering Pillar Leader (Platforms) | CERG STD document: Secure Configuration Baseline Standard DISH |
| CERG-STD-CR-001 | Cryptography and Key Management Standard | `standards/CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md` | standard | engineering | Engineering Pillar Leader (Platforms) | CERG STD document: Cryptography and Key Management Standard |
| CERG-STD-CUI-001 | CUI Handling Standard | `standards/CERG-STD-CUI-001_CUI_Handling_Standard.md` | standard | engineering | CMMC / Federal Compliance Manager | CERG STD document: CUI Handling Standard |
| CERG-STD-DG-001 | Data Governance and Classification Standard | `standards/CERG-STD-DG-001_Data_Governance_and_Classification_Standard.md` | standard | engineering | Governance Pillar Leader (Policy & Standards) | CERG STD document: Data Governance and Classification Standard |
| CERG-STD-EP-001 | Endpoint and Mobile Security Standard | `standards/CERG-STD-EP-001_Endpoint_and_Mobile_Security_Standard.md` | standard | engineering | Engineering Pillar Leader (Endpoint) | CERG STD document: Endpoint and Mobile Security Standard |
| CERG-STD-IT-001 | IT Cloud SaaS Security Standard | `standards/CERG-STD-IT-001_IT_Cloud_SaaS_Security_Standard.md` | standard | engineering | Governance Pillar Leader | CERG STD document: IT Cloud SaaS Security Standard |
| CERG-STD-LM-001 | Logging Monitoring and Detection Standard | `standards/CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md` | standard | engineering | Risk Pillar Leader (Detection Engineering) | CERG STD document: Logging Monitoring and Detection Standard |
| CERG-STD-MSG-001 | Email and Messaging Security Standard | `standards/CERG-STD-MSG-001_Email_and_Messaging_Security_Standard.md` | standard | engineering | Engineering Pillar Leader (Platforms) | CERG STD document: Email and Messaging Security Standard |
| CERG-STD-NET-001 | Network Security and Segmentation Standard | `standards/CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md` | standard | engineering | Engineering Pillar Leader (Platforms) | CERG STD document: Network Security and Segmentation Standard |
| CERG-STD-OT-001 | Grid Control Systems Security Standard | `standards/CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md` | standard | engineering | Governance Pillar Leader (OT/NERC-CIP) | CERG STD document: Grid Control Systems Security Standard |
| CERG-STD-RES-001 | Cyber Resilience and Backup Standard | `standards/CERG-STD-RES-001_Cyber_Resilience_and_Backup_Standard.md` | standard | engineering | Engineering Pillar Leader (Resilience) | CERG STD document: Cyber Resilience and Backup Standard |
| CERG-STD-SDL-001 | Secure Software Development and Application Security Standard | `standards/CERG-STD-SDL-001_Secure_Software_Development_and_Application_Security_Standard.md` | standard | engineering | Engineering Pillar Leader (Application Security) | CERG STD document: Secure Software Development and Application Security Standard |
| CERG-TMPL-AI-001 | AI Intake and Sanctioning Template | `templates/CERG-TMPL-AI-001_AI_Intake_and_Sanctioning_Template.md` | template | governance | Governance Pillar Leader | CERG TMPL document: AI Intake and Sanctioning Template |
| CERG-TMPL-AI-002 | Sanctioned AI Tools Register Template | `templates/CERG-TMPL-AI-002_Sanctioned_AI_Tools_Register_Template.md` | template | governance | Governance Pillar Leader | CERG TMPL document: Sanctioned AI Tools Register Template |
| CERG-TMPL-AI-003 | AI System and Model Register Template | `templates/CERG-TMPL-AI-003_AI_System_and_Model_Register_Template.md` | template | governance | Application Security Engineer | CERG TMPL document: AI System and Model Register Template |
| CERG-TMPL-AR-001 | Architecture and Project Intake Form | `templates/CERG-TMPL-AR-001_Architecture_and_Project_Intake_Form.md` | template | governance | Engineering Pillar Leader | CERG TMPL document: Architecture and Project Intake Form |
| CERG-TMPL-AUD-001 | Control Evidence and Test Worksheet | `templates/CERG-TMPL-AUD-001_Control_Evidence_and_Test_Worksheet.md` | template | governance | Evidence Librarian | CERG TMPL document: Control Evidence and Test Worksheet |
| CERG-TMPL-CUI-001 | System Security Plan Template | `templates/CERG-TMPL-CUI-001_System_Security_Plan_Template.md` | template | governance | CMMC / Federal Compliance Manager | CERG TMPL document: System Security Plan Template |
| CERG-TMPL-CUI-002 | POAM Template | `templates/CERG-TMPL-CUI-002_POAM_Template.md` | template | governance | CMMC / Federal Compliance Manager | CERG TMPL document: POAM Template |
| CERG-TMPL-GOV-001 | Stakeholder Perception Survey | `templates/CERG-TMPL-GOV-001_Stakeholder_Perception_Survey.md` | template | governance | Governance Pillar Leader | CERG TMPL document: Stakeholder Perception Survey |
| CERG-TMPL-MTR-001 | Board and CISO Reporting Deck Template | `templates/CERG-TMPL-MTR-001_Board_and_CISO_Reporting_Deck_Template.md` | template | governance | Governance Pillar Leader | CERG TMPL document: Board and CISO Reporting Deck Template |
| CERG-TMPL-RM-001 | Risk Register Templates and Reporting | `templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md` | template | governance | Governance Pillar Leader (Risk Register) | CERG TMPL document: Risk Register Templates and Reporting |
| CERG-TMPL-RM-002 | Security Exception Request Form | `templates/CERG-TMPL-RM-002_Security_Exception_Request_Form.md` | template | governance | Risk Register Owner | CERG TMPL document: Security Exception Request Form |
| CERG-TMPL-RM-003 | Risk Acceptance Memo Template | `templates/CERG-TMPL-RM-003_Risk_Acceptance_Memo_Template.md` | template | governance | Risk Pillar Leader | CERG TMPL document: Risk Acceptance Memo Template |
| CERG-TMPL-RM-004 | Risk Acceptance Request Form | `templates/CERG-TMPL-RM-004_Risk_Acceptance_Request_Form.md` | template | governance | Risk Register Owner | CERG TMPL document: Risk Acceptance Request Form |
| CERG-TMPL-SAAS-001 | SaaS Evidence Collection Checklist | `templates/CERG-TMPL-SAAS-001_SaaS_Evidence_Collection_Checklist.md` | template | governance | Governance Pillar Leader | CERG TMPL document: SaaS Evidence Collection Checklist |
| CERG-TMPL-SBOM-001 | SBOM Evidence Collection Checklist | `templates/CERG-TMPL-SBOM-001_SBOM_Evidence_Collection_Checklist.md` | template | governance | Vendor Risk Analyst | CERG TMPL document: SBOM Evidence Collection Checklist |
| CERG-TMPL-TPRM-001 | Vendor Security Questionnaire and Assessment Template | `templates/CERG-TMPL-TPRM-001_Vendor_Security_Questionnaire_and_Assessment_Template.md` | template | governance | Vendor Risk Analyst | CERG TMPL document: Vendor Security Questionnaire and Assessment Template |
| README-roles | README | `roles/README.md` | job-description | workforce |  | CERG JD document: README |

## Readme and Meta Artifact Index
| ID | Title | Path | Type | Pillar | Summary |
|---|---|---|---|---|---|
| ADOPT-WITH-AN-AGENT | ADOPT-WITH-AN-AGENT | `ADOPT-WITH-AN-AGENT.md` | readme | cross-cutting | CERG META document: ADOPT-WITH-AN-AGENT |
| AGENTS | AGENTS | `AGENTS.md` | readme | cross-cutting | Guide for AI agents working on CERG — conventions, pitfalls, tools, git workflow. |
| BEGINNER-GUIDE | BEGINNER-GUIDE | `BEGINNER-GUIDE.md` | readme | cross-cutting | CERG META document: BEGINNER-GUIDE |
| CODE_OF_CONDUCT | CODE OF CONDUCT | `CODE_OF_CONDUCT.md` | readme | cross-cutting | Community code of conduct for CERG contributors. |
| CONTRIBUTING | CONTRIBUTING | `CONTRIBUTING.md` | readme | cross-cutting | Contributing guide — validation requirements, conventions, PR workflow. |
| README | README | `README.md` | readme | cross-cutting | CERG repository root — project overview, adoption paths, architecture, reader guides. |
| SECURITY | SECURITY | `SECURITY.md` | readme | cross-cutting | Security policy and vulnerability disclosure. |
| START-HERE | START-HERE | `START-HERE.md` | readme | cross-cutting | First 48 hours adoption guide — Lite, Standard, and Regulated paths. |
| README-adoption-packs-cerg-lite | README | `adoption-packs/cerg-lite/README.md` | readme | cross-cutting | CERG META document: README |
| agent-prompt | agent-prompt | `adoption-packs/cerg-lite/agent-prompt.md` | meta | cross-cutting | CERG META document: agent-prompt |
| README-examples | README | `examples/README.md` | readme | cross-cutting | CERG META document: README |
| README-examples-day-in-the-life | README | `examples/day-in-the-life/README.md` | readme | cross-cutting | CERG META document: README |
| story-10-new-ciso-90-days | story-10-new-ciso-90-days | `examples/day-in-the-life/story-10-new-ciso-90-days.md` | meta | cross-cutting | CERG META document: story-10-new-ciso-90-days |
| story-8-cerg-lite-maria | story-8-cerg-lite-maria | `examples/day-in-the-life/story-8-cerg-lite-maria.md` | meta | cross-cutting | CERG META document: story-8-cerg-lite-maria |
| story-9-f-01-control-intent | story-9-f-01-control-intent | `examples/day-in-the-life/story-9-f-01-control-intent.md` | meta | cross-cutting | CERG META document: story-9-f-01-control-intent |
| README-examples-regulated-utility-profile | README | `examples/regulated-utility-profile/README.md` | readme | cross-cutting | CERG META document: README |
| CERG-GOV-JD-001 | CERG Job Descriptions | `governance/CERG-GOV-JD-001_CERG_Job_Descriptions.md` | meta | cross-cutting | CERG META document: CERG Job Descriptions |
| README-machine-readable | README | `machine-readable/README.md` | readme | cross-cutting | CERG META document: README |
| README-tools-policy-as-code | README | `tools/policy-as-code/README.md` | readme | cross-cutting | CERG META document: README |

## Findings

### A01-F01 Low ID-looking artifact classified as META
Affected files:
- `governance/CERG-GOV-JD-001_CERG_Job_Descriptions.md`
Problem: The file has a CERG-style governed ID in its path and index ID, but the LLM index classifies it with prefix `META` and type `meta`, outside the governed `JD`/`JF` workforce set.
Why it matters: Later workforce review could miss it if reviewers select only `JD` and `JF` prefixes. It may be a useful legacy/consolidated reference, or it may be superseded by role-specific JDs.
Evidence from corpus: A01 index grouping shows 33 `JD` role-specific job descriptions plus this ID-looking `META` artifact.
Recommended action: Carry this into D01/G01. Decide whether it is a retained meta summary, a retired/superseded workforce artifact, or should be reclassified in generated indexes.
Owner/workstream: Workforce / Refinement.

### A01-F02 Low Example stories and adoption prompt are intentionally non-governed but operationally important
Affected files:
- `examples/day-in-the-life/story-8-cerg-lite-maria.md`
- `examples/day-in-the-life/story-9-f-01-control-intent.md`
- `examples/day-in-the-life/story-10-new-ciso-90-days.md`
- `adoption-packs/cerg-lite/agent-prompt.md`
Problem: These are classified as `META`, which is mechanically reasonable, but later example and reader-test work must not treat them as disposable readmes.
Why it matters: The work plan identifies examples as first-class teaching tools; excluding META artifacts from conceptual review would understate CERG's human-understanding layer.
Evidence from corpus: The day-in-the-life README explicitly promotes Story 8 for CERG Lite and Story 10 for first-90-days comprehension.
Recommended action: Include all day-in-the-life Markdown stories in E/H workstreams regardless of governed prefix.
Owner/workstream: Examples / Reader Testing.

## Positive Confirmations
- The LLM index and filesystem Markdown inventory match exactly: 146 indexed Markdown paths and 146 repository Markdown paths in scope.
- Governed artifacts are clearly separable from readme/meta files by `prefix != META`.
- The corpus already distinguishes policy, governance instruments, standards, procedures, plans, templates, workforce, examples, and machine-readable support in a way later reviewers can select without searching manually.
- Status distribution is coherent at the index level: 125 Approved, 2 External Interface, and 19 unstatused readme/meta artifacts.

## Open Questions
- Should `CERG-GOV-JD-001_CERG_Job_Descriptions.md` remain a meta/consolidated reference, be marked retired, or be folded into the workforce architecture?
- Should operational examples receive a distinct non-governed-but-authoritative teaching classification in the LLM index?

## Proposed Next Tasks
- A02: capture validator, integrity, heading, role-name, and vocabulary baselines.
- B01/B02/B03: start conceptual review using this corpus map and the spine documents already loaded.
