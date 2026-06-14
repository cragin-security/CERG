#!/usr/bin/env python3
"""
Populate §9 (Competency Anchors), §10 (Success Profile), and §11.3 (Management Track)
in all 27 per-role CERG JD files.

Source data:
  - §9: CMP-001 §4 (Engineering), §5 (Risk), §6 (Governance), §7 (Management addendum)
  - §10: Generated from each role's Role Summary + Key Responsibilities
  - §11.3: JA-001 §8 career pathing rules
"""
import re
import os
import sys

BASE = '/home/lupus/CERG'

# ──────────────────────────────────────────────────
# COMPETENCY ANCHORS — from CMP-001 §4 (Engineering), §5 (Risk), §6 (Governance)
# Each pillar has 8 domains × 4 grades (S1-S4)
# ──────────────────────────────────────────────────

# Engineering Pillar Anchors (CMP-001 §4)
ENG = {
    'Technical Depth': {
        'S1': 'Executes assigned engineering tasks (IaC module, configuration change, architecture review checklist item) from established procedures. Recognizes when a task result does not match expected output and escalates with context. Learning the organization\'s technology stack: can name the major platforms, their purpose, and their security control points.',
        'S2': 'Owns a technology domain (e.g., AWS security, Azure AD, Kubernetes admission control). Designs and implements security controls independently within that domain. Performs architecture reviews in their domain and produces findings that require minimal rework from the reviewer. Authors and improves procedures for their domain.',
        'S3': 'Shapes the organization\'s technical security strategy in their domain. Designs reference architectures adopted by other engineers. Anticipates how changes in the technology stack will affect security posture before they land. Performs architecture reviews across domains with credibility.',
        'S4': 'Sets the technical bar for the entire Engineering pillar. Called upon for the hardest cross-domain problems. Represents the organization\'s engineering position to vendors, industry working groups, and regulators. Can step into any Engineering domain and contribute meaningfully within days.',
    },
    'Cross-Pillar Fluency': {
        'S1': 'Understands that Risk and Governance pillars exist and can describe their basic functions. Reads vulnerability reports and compliance findings that affect their work.',
        'S2': 'Consumes Risk pillar output (vulnerability data, threat intelligence) and incorporates it into engineering decisions. Understands what Governance needs from Engineering for an audit and provides it without being chased.',
        'S3': 'Anticipates what Risk and Governance will need from an engineering decision before they ask. Participates in cross-pillar working groups as the Engineering voice. Can represent Engineering\'s position to a regulator or auditor without a Governance handler.',
        'S4': 'Operates fluently across all three pillars. Contributes to Risk assessments and Governance standards as a peer, not a guest. Is the person a pillar leader calls when a cross-pillar problem does not fit any procedure.',
    },
    'Risk Judgment': {
        'S1': 'Follows the risk taxonomy when documenting findings. Can distinguish between a configuration drift alert that needs a ticket and one that needs an incident response page.',
        'S2': 'Independently assesses the severity and likelihood of findings in their domain. Assigns risk ratings that are consistent with the taxonomy and rarely adjusted by a senior reviewer.',
        'S3': 'Evaluates risk across domains and articulates the business impact in terms an executive can act on. Identifies compensating controls that reduce risk below what a pure vulnerability score would suggest.',
        'S4': 'Shapes the organization\'s risk appetite through technical judgment. Called upon by the CISO for independent risk assessments on material decisions. Their risk evaluation carries the same weight as a pillar leader\'s.',
    },
    'Communication': {
        'S1': 'Writes clear ticket updates and status reports. Explains a technical finding to their immediate team without ambiguity.',
        'S2': 'Writes architecture review findings that a project manager or business owner can understand and act on. Presents technical topics to their pillar. Authors clear, usable procedures.',
        'S3': 'Represents Engineering in cross-functional forums with credibility. Writes decision memos that frame technical options in business terms. Presents to senior leadership and external stakeholders.',
        'S4': 'Communicates complex technical risk to the CISO, the board (as requested), regulators, and industry peers. Writes the organization\'s public technical positions. Represents the organization at conferences and in industry working groups.',
    },
    'Operational Discipline': {
        'S1': 'Follows procedures correctly. Updates tickets and documentation when work is complete. Meets assigned SLAs. Admits when they do not know something rather than guessing.',
        'S2': 'Owns operational SLAs for their domain work streams. Ensures evidence is collected and stored per the evidence procedure. Improves procedures when they find gaps. Their work is consistently auditable without retroactive cleanup.',
        'S3': 'Designs procedures that are operationally sustainable, not just technically correct. Ensures the evidence trail for their domain is audit-ready at all times. Identifies and eliminates toil: automates repetitive operational tasks.',
        'S4': 'Sets operational standards for the pillar. Defines what "good" looks like for procedure compliance, evidence quality, and SLA management. Holds the pillar accountable to its own operational commitments.',
    },
    'Influence and Mentorship': {
        'S1': 'Actively learns from senior engineers. Asks good questions. Shares what they learn with peers.',
        'S2': 'Onboards new Specialists without assistance. Peer-reviews code and configurations with constructive feedback. Their technical opinion is sought by other engineers in their domain.',
        'S3': 'Mentors Specialists and Sr. Specialists across domains. Leads technical initiatives without formal authority. Their architectural recommendations are rarely overruled.',
        'S4': 'Shapes the development of the entire Engineering team. Sets the technical bar through their own work and their mentoring. Influences hiring profiles, team composition, and organizational design.',
    },
    'Compliance and Regulatory Literacy': {
        'S1': 'Knows which regulatory frameworks apply to their organization. Can describe the security implications of the major ones (NERC-CIP, CMMC, SOX) at a high level.',
        'S2': 'Understands the specific regulatory requirements that affect their domain. Can explain to an auditor how a control they implemented satisfies a regulatory requirement.',
        'S3': 'Anticipates regulatory implications of engineering decisions. Advises project teams on compliance requirements before design is complete. Represents Engineering in regulatory audits without a Governance chaperone.',
        'S4': 'Contributes to the organization\'s regulatory strategy. Engages with regulators on technical matters. Shapes standards so that compliance is a byproduct of good engineering, not a separate activity.',
    },
    'Continuous Learning': {
        'S1': 'Completes assigned training. Pursues foundational certifications relevant to their domain. Learns the organization\'s technology stack.',
        'S2': 'Maintains current certifications. Stays current on developments in their domain. Shares what they learn with the team.',
        'S3': 'Pursues advanced certifications. Contributes to the team\'s knowledge base through documented research, brown-bag sessions, or internal training. Evaluates new technologies for organizational adoption.',
        'S4': 'Recognized externally for expertise. Shapes the organization\'s technology and certification roadmap. The person other engineers go to when they need to understand an emerging technology or threat.',
    },
}

# Risk Pillar Anchors (CMP-001 §5)
RISK = {
    'Technical Depth': {
        'S1': 'Operates the Risk pillar\'s tools (vulnerability scanner, CSPM platform, threat intel platform, detection pipeline) under supervision. Triages alerts following established procedures. Recognizes false positives and true positives with increasing accuracy.',
        'S2': 'Owns a Risk domain (e.g., vulnerability management for a platform class, vendor assessments for a business unit, a set of detection rules). Tunes tools to reduce noise and improve signal. Independently investigates findings and determines root cause.',
        'S3': 'Shapes the Risk pillar\'s approach to exposure management. Designs assessment methodologies. Correlates findings across tools to identify systemic weaknesses that individual alerts miss.',
        'S4': 'Sets the analytical bar for the entire Risk pillar. Called upon for the hardest exposure questions. Represents the organization\'s risk posture to regulators, auditors, and industry peers.',
    },
    'Cross-Pillar Fluency': {
        'S1': 'Understands that Engineering builds systems and Governance owns compliance. Reads architecture review outputs and compliance standards that affect their risk assessments.',
        'S2': 'Delivers risk findings in a format Engineering can act on. Understands what evidence Governance needs from Risk assessments and provides it proactively. Participates in cross-pillar threat modeling sessions.',
        'S3': 'Collaborates with Engineering to design controls that address risk findings, not just report them. Feeds risk intelligence into Governance\'s compliance calendar. Anticipates which risk findings will become audit findings.',
        'S4': 'Operates fluently across all three pillars. Contributes to Engineering architecture decisions and Governance standards as a peer. The person a pillar leader calls when a risk question spans all three pillars.',
    },
    'Risk Judgment': {
        'S1': 'Applies the risk taxonomy correctly when triaging findings. Distinguishes between Critical, High, Medium, and Low severity using the defined criteria. Escalates findings that exceed SLA without delay.',
        'S2': 'Independently assesses the business impact of findings in their domain. Adjusts risk ratings based on context and documents the rationale. Produces risk assessments that the Risk Pillar Leader accepts without material revision.',
        'S3': 'Assesses systemic risk: identifies patterns across individual findings that indicate a deeper weakness. Evaluates risk from new technologies, vendors, or business initiatives before they are operational.',
        'S4': 'Shapes the organization\'s risk appetite. Called upon by the CISO for independent risk evaluation on material decisions. Their risk judgment on novel or ambiguous situations is treated as authoritative.',
    },
    'Communication': {
        'S1': 'Writes clear finding descriptions with reproducible steps, impact statements, and remediation guidance. Updates stakeholders on finding status without being prompted.',
        'S2': 'Delivers risk briefings to business owners and project teams. Translates vulnerability data into business risk without losing technical accuracy. Writes vendor risk assessment reports that procurement and legal can act on.',
        'S3': 'Presents risk posture to executive audiences. Communicates threat landscape changes and their organizational implications. Writes threat intelligence products consumed by leadership.',
        'S4': 'Communicates organizational risk posture to the board, regulators, and external stakeholders. Represents the organization\'s risk position in industry forums.',
    },
    'Operational Discipline': {
        'S1': 'Triages findings within SLA. Documents assessment results in the designated system. Follows the vulnerability management and risk register procedures.',
        'S2': 'Owns operational SLAs for their domain. Ensures risk register entries are current and complete. Maintains scanning schedules, detection rule lifecycles, or vendor assessment cadences without gaps.',
        'S3': 'Designs risk assessment workflows that produce consistent, auditable output. Ensures the Risk pillar\'s operational cadence is documented, measured, and improving. Identifies and automates repetitive risk assessment tasks.',
        'S4': 'Sets operational standards for the Risk pillar. Defines what "defensible" risk assessment looks like under regulatory scrutiny.',
    },
    'Influence and Mentorship': {
        'S1': 'Learns from senior analysts. Asks good questions about methodology and judgment. Shares interesting findings with the team.',
        'S2': 'Trains new analysts on Risk tools and procedures. Peer-reviews risk assessments and detection rules. Their analytical judgment is sought by other team members.',
        'S3': 'Mentors analysts across Risk domains. Leads cross-functional risk initiatives. Their risk assessments shape how Engineering and business owners prioritize remediation.',
        'S4': 'Develops the analytical capability of the entire Risk team. Sets the quality bar for risk assessment, threat intelligence, and detection engineering. Influences organizational risk culture.',
    },
    'Compliance and Regulatory Literacy': {
        'S1': 'Knows which regulatory frameworks apply and can describe how Risk assessments support compliance.',
        'S2': 'Understands the specific regulatory requirements that govern their Risk domain. Produces risk assessments that meet the evidence standards of the relevant frameworks.',
        'S3': 'Anticipates how regulatory changes will affect the Risk program\'s scope and cadence. Advises Governance on the risk implications of compliance findings.',
        'S4': 'Contributes to the organization\'s regulatory strategy from a risk perspective. Engages with regulators on risk methodology.',
    },
    'Continuous Learning': {
        'S1': 'Completes assigned training. Pursues foundational certifications. Learns the organization\'s threat landscape.',
        'S2': 'Maintains current certifications. Tracks the threat actors, TTPs, and vulnerabilities relevant to the organization\'s industry.',
        'S3': 'Pursues advanced certifications. Contributes threat research or methodology improvements adopted by the team. Represents the organization in threat-sharing communities.',
        'S4': 'Recognized externally for risk or threat expertise. Contributes to industry threat intelligence, risk methodology, or detection frameworks.',
    },
}

# Governance Pillar Anchors (CMP-001 §6)
GOV = {
    'Technical Depth': {
        'S1': 'Operates the Governance pillar\'s tools (document management system, evidence library, GRC platform). Executes evidence collection, control testing, or policy review tasks from established procedures. Reads and correctly interprets CERG standards and regulatory requirements in their assigned domain.',
        'S2': 'Owns a compliance domain. Independently collects, organizes, and presents evidence for audits and assessments. Maps regulatory requirements to CERG controls and identifies gaps. Authors compliance documentation that requires minimal revision.',
        'S3': 'Shapes the organization\'s compliance strategy for their domain. Designs evidence collection workflows that survive auditor scrutiny. Interprets ambiguous regulatory guidance and produces defensible organizational positions.',
        'S4': 'Sets the compliance and governance bar for the entire Governance pillar. Called upon for the hardest regulatory interpretation questions. Represents the organization to regulators, assessors, and auditors as the authoritative technical voice.',
    },
    'Cross-Pillar Fluency': {
        'S1': 'Understands the basic functions of Engineering and Risk pillars. Reads engineering architecture outputs and risk assessments that affect their compliance work.',
        'S2': 'Engages Engineering and Risk as partners in compliance, not subjects of it. Understands the technical reality behind the controls they are assessing. Requests evidence in terms the providing pillar understands.',
        'S3': 'Translates between regulatory language and technical reality in both directions. Anticipates which engineering or risk decisions will have compliance implications before they are made.',
        'S4': 'Operates fluently across all three pillars. Engages with Engineering on architecture and Risk on exposure posture as a peer.',
    },
    'Risk Judgment': {
        'S1': 'Applies the risk taxonomy when documenting compliance findings. Understands the relationship between control failures and organizational risk.',
        'S2': 'Assesses the risk implication of control gaps in their domain. Prioritizes compliance findings by actual risk to the organization, not by framework numbering.',
        'S3': 'Evaluates the risk impact of regulatory changes. Advises leadership on the risk trade-offs of compliance decisions. Correlates compliance findings with vulnerability and threat data.',
        'S4': 'Shapes organizational risk decisions through the compliance lens. Advises the CISO on the risk implications of regulatory strategy.',
    },
    'Communication': {
        'S1': 'Writes clear evidence descriptions, control test results, and compliance status updates. Communicates evidence requests to Engineering and Risk without ambiguity.',
        'S2': 'Presents compliance status and findings to pillar leadership. Translates regulatory requirements into language project teams can act on. Writes policy and standard sections that are clear and enforceable.',
        'S3': 'Represents the organization to auditors, assessors, and regulators as a primary point of contact. Writes regulatory responses and compliance positions adopted by leadership.',
        'S4': 'Communicates the organization\'s compliance posture to the board, regulators, and external stakeholders. Shapes the organization\'s regulatory narrative.',
    },
    'Operational Discipline': {
        'S1': 'Follows evidence management procedures. Documents compliance activities in the designated systems. Meets regulatory filing deadlines. Maintains organized, retrievable evidence packages.',
        'S2': 'Owns the compliance calendar for their domain. Ensures evidence is collected, reviewed, and stored on schedule. Maintains audit-ready evidence packages at all times.',
        'S3': 'Designs compliance operations that are sustainable year-round. Ensures the Governance pillar\'s operational cadence is documented, measured, and improving.',
        'S4': 'Sets operational standards for the Governance pillar. Defines what "audit-ready" means in measurable terms.',
    },
    'Influence and Mentorship': {
        'S1': 'Learns from senior Governance staff. Asks good questions about regulatory interpretation and evidence standards. Supports peers during audit preparation.',
        'S2': 'Trains new Governance staff on compliance domains and evidence procedures. Peer-reviews compliance documentation. Their regulatory knowledge is sought by Engineering and Risk staff.',
        'S3': 'Mentors Governance staff across compliance domains. Influences how the organization approaches regulatory compliance, moving from reactive to proactive.',
        'S4': 'Develops the compliance capability of the entire Governance team and the broader organization. Sets the quality bar for regulatory interpretation, evidence standards, and auditor engagement.',
    },
    'Compliance and Regulatory Literacy': {
        'S1': 'Knows the regulatory frameworks in the organization\'s scope. Can describe the structure and key requirements of each. Correctly applies framework terminology.',
        'S2': 'Deep knowledge of the regulatory frameworks in their domain. Independently interprets regulatory requirements and maps them to organizational controls.',
        'S3': 'Authority on their regulatory domain. Interprets ambiguous regulatory guidance and produces defensible positions. Anticipates regulatory changes.',
        'S4': 'Shapes the organization\'s regulatory strategy. Engages directly with regulators and industry bodies on regulatory development.',
    },
    'Continuous Learning': {
        'S1': 'Completes assigned training. Pursues foundational certifications. Learns the organization\'s regulatory landscape.',
        'S2': 'Maintains current certifications. Tracks regulatory developments and framework updates relevant to their domain.',
        'S3': 'Pursues advanced certifications. Contributes to the Governance body of knowledge through documented regulatory analysis.',
        'S4': 'Recognized externally for regulatory or compliance expertise. Contributes to regulatory development, industry standards, or professional certification bodies.',
    },
}

# ──────────────────────────────────────────────────
# SUCCESS PROFILES — role-specific, derived from Role Summary + Key Responsibilities
# ──────────────────────────────────────────────────

SUCCESS_PROFILES = {
    'Cloud Security Engineer': 'A Cloud Security Engineer is successful when cloud and SaaS platforms are designed, deployed, and operated with security embedded, not bolted on. Key indicators: every cloud landing zone ships with guardrails, not gates; CSPM posture is green and findings are triaged within SLA; IaC reviews are fast, consistent, and rarely find the same issue twice; Engineering teams treat security as part of the deployment pipeline, not a separate review step. The engineer is the person project teams seek out for cloud security advice — and that advice is actioned, not debated.',
    'Identity Engineer': 'An Identity Engineer is successful when the identity and access control infrastructure is invisible to legitimate users and impenetrable to attackers. Key indicators: access decisions are made in milliseconds against authoritative data; privilege escalation attempts are detected in real time; user access certifications complete on schedule with minimal exceptions; the identity architecture scales without redesign as the organization grows. The engineer\'s work means that when an auditor asks "who has access to what," the answer is immediate, complete, and accurate.',
    'OT Security Engineer': 'An OT Security Engineer is successful when operational technology environments are secured without disrupting production. Key indicators: the Purdue model is implemented and enforced; OT asset inventory is complete and current; vulnerabilities in the OT environment are discovered before they cause incidents; engineering and operations teams understand and respect the security controls in their environment. The engineer bridges the gap between IT security practices and OT reliability requirements, earning trust from both sides.',
    'Application Security Engineer': 'An Application Security Engineer is successful when security is a natural, frictionless part of the software development lifecycle. Key indicators: SAST/DAST/SCA tools are integrated into CI/CD pipelines with low false-positive rates; findings from security reviews are fixed before deployment, not tracked as technical debt; developers seek security input early in the design phase; the mean time to remediate a critical application vulnerability is measured in hours, not days. The engineer makes it easier to build securely than to cut corners.',
    'Endpoint Engineer': 'An Endpoint Engineer is successful when every managed device is a controlled, defensible platform regardless of its location or user. Key indicators: endpoint configuration drift is detected and remediated automatically within hours; EDR coverage is complete with zero stale agents; patch compliance for critical vulnerabilities exceeds 95% within the defined window; mobile and remote devices are indistinguishable from office devices in their security posture. The engineer\'s work is measured in coverage percentage and response time, not tickets closed.',
    'Cryptography Engineer': 'A Cryptography Engineer is successful when the organization\'s cryptographic posture is correct by design and sustainable over time. Key indicators: all cryptographic keys are managed through a centralized key management system with full lifecycle tracking; certificate expiry is never an emergency; TLS configurations across the estate score A+ on every assessment; cryptographic algorithms and key lengths are consistent with current best practice. The engineer makes crypto "boring" — it works correctly, automatically, and nobody has to think about it.',
    'Engineering Pillar Leader': 'An Engineering Pillar Leader is successful when the engineering organization is delivering security outcomes reliably, sustainably, and measurably. Key indicators: the team\'s standards are published, adopted, and enforced; architecture reviews are completed within SLA with no systemic finding patterns; team members can articulate their growth trajectory; the pillar\'s evidence is audit-ready without fire drills. The leader is trusted by the CISO to set technical direction and by the team to advocate for the resources and conditions they need to succeed.',
    'Pre-production Reviewer': 'A Pre-production Reviewer is successful when security issues are identified and resolved before they reach production, not after. Key indicators: architecture reviews are completed before any infrastructure is provisioned; findings are specific enough that project teams can act on them without reinterpretation; the review cycle time does not delay releases; recurring findings trigger standard updates rather than repeated manual reviews. The reviewer is seen as an enabler of secure delivery, not a gate that slows things down.',
    'Exposure Management Lead': 'A Exposure Management Lead is successful when the organization knows its exposure posture in real time and is actively reducing it. Key indicators: scanning coverage is complete across all in-scope assets; vulnerability age is trending down, not up; remediation SLAs are met for each severity tier; the vulnerability register is the authoritative source of truth for exposure decisions. The lead ensures that every Critical and High finding has an owner, a plan, and a due date — and that the CISO can report exposure status to the board in under an hour.',
    'Adversarial Testing Lead': 'An Adversarial Testing Lead is successful when the organization understands its real-world security posture through validated attack simulation. Key indicators: every test has a clear scope, approved rules of engagement, and a structured findings report; findings are reproducible and include validated exploitation paths; remediation verification testing confirms fixes are effective; the test calendar covers all in-scope systems on a risk-prioritized schedule. The lead ensures that testing is a learning tool for the defense team, not a gotcha exercise.',
    'Threat Intelligence Analyst': 'A Threat Intelligence Analyst is successful when intelligence drives organizational decisions rather than filling a report nobody reads. Key indicators: intelligence products are consumed by Engineering (to prioritize controls), by Risk (to update exposure assessments), and by leadership (to inform budget and strategy); intelligence informs detection rule creation with measurable improvements in detection coverage; finished intelligence is delivered before the relevant threat events. The analyst is the person leadership asks "what should we worry about this quarter?"',
    'Detection Engineer': 'A Detection Engineer is successful when the organization detects malicious activity before it causes material harm. Key indicators: detection coverage maps to the MITRE ATT&CK framework with measurable gaps identified and prioritized; alert-to-investigation time is trending down; false positive rates for production detection rules are below 5%; detection rules are tested against known adversary behavior before deployment. The engineer\'s detections catch real threats while generating noise only when the security team should actually pay attention.',
    'OT Risk Analyst': 'An OT Risk Analyst is successful when OT risk is measured, tracked, and managed with the same rigor as IT risk — while respecting OT operational constraints. Key indicators: the OT risk register covers all critical industrial control systems; risk assessments incorporate both cybersecurity and safety impact; findings are prioritized by actual operational risk, not CVSS alone; OT-specific threat intelligence feeds into risk assessments. The analyst speaks the language of both control engineers and security professionals fluently.',
    'Identity Risk Analyst': 'An Identity Risk Analyst is successful when identity-related risk is visible, measurable, and actively managed. Key indicators: the identity risk register captures access-related findings from across the organization; user access risk scoring identifies anomalous behavior before it becomes an incident; access certification results are analyzed for risk patterns, not just checked off; SOD violations are identified and remediated before they cause audit findings. The analyst connects identity events to business risk in terms leadership understands.',
    'Vendor Risk Analyst': 'A Vendor Risk Analyst is successful when vendor risk is managed systematically rather than through fire drills triggered by news events. Key indicators: every in-scope vendor has a current risk assessment with a clear risk rating; vendor onboarding SLAs are met without security being the bottleneck; high-risk vendor findings have documented remediation plans with owner and due date; the vendor register is current enough that leadership can answer "what is our supply chain risk exposure?" in a single meeting.',
    'Risk Pillar Leader': 'A Risk Pillar Leader is successful when the Risk pillar\'s output drives organizational risk reduction, not just risk tracking. Key indicators: the risk register is the authoritative source that the CISO, Engineering, and Governance all use for prioritization; exposure posture is improving quarter over quarter across measurable dimensions; the pillar\'s findings are actionable and acted upon; team members can describe the pillar\'s strategy and how their work contributes to it. The leader is trusted to represent the CISO in risk decisions and to defend those decisions to leadership.',
    'NERC-CIP Compliance Manager': 'A NERC-CIP Compliance Manager is successful when compliance is a continuous operational state, not a periodic audit event. Key indicators: evidence packages are audit-ready at all times, not just during audit windows; NERC-CIP non-compliance findings are trending down; the evidence collection burden on Engineering is stable or decreasing year over year; the compliance calendar is accurate to within a week for every filing deadline. The manager ensures that the answer to "can you prove compliance?" is always yes, with a single click.',
    'CMMC / Federal Compliance Manager': 'A CMMC / Federal Compliance Manager is successful when the organization can demonstrate compliance to any federal assessor on any day without a panic. Key indicators: CUI is properly identified and protected across all environments; POA&Ms are actively managed with clear owners and due dates; assessment readiness reviews reveal fewer findings each cycle; DIBCAC and C3PAO interactions are professional, efficient, and predictable. The manager ensures that CMMC Level 2 certification is a baseline, not a stretch goal.',
    'SOX ITGC Lead': 'A SOX ITGC Lead is successful when ITGC audits are boring — no material weaknesses, no significant deficiencies, no surprises. Key indicators: control testing pass rates are above 90% with a clear trend line; control deficiencies are identified by internal testing before the external auditors find them; remediation plans for any control failures are documented and tracked; SOD conflicts are identified and remediated proactively. The lead ensures that ITGC is a well-oiled machine that the external auditors trust.',
    'Policy & Standards Manager': 'A Policy & Standards Manager is successful when CERG policies and standards are actually followed, not just filed. Key indicators: policy exceptions are rare and documented; standards are referenced in architecture reviews, risk assessments, and compliance testing by name; the policy library is current — no document is past its review date by more than 30 days; feedback from standards users results in documented improvements. The manager ensures that every CERG document is findable, readable, and usable by the person who needs it.',
    'Risk Register Owner': 'A Risk Register Owner is successful when the risk register is a decision-support tool, not a compliance artifact. Key indicators: risk entries are complete, current, and consistently scored; aging risks have documented reasons and treatment plans; the register is referenced in every material decision (architecture changes, vendor selection, budget allocation); leadership reviews risk trends quarterly and acts on them. The owner ensures that when someone asks "what are our top five risks," the answer is in the register, current, and actionable.',
    'Evidence Librarian': 'An Evidence Librarian is successful when evidence is treated as a managed asset rather than a scramble before every audit. Key indicators: every control has a current, valid evidence artifact with a known location and retention date; evidence collection is automated or scheduled, not manually triggered; retrieval time for any evidence artifact is measured in minutes, not days; evidence gaps are identified and remediated before the audit calendar triggers them. The librarian\'s work means the organization passes audits on process, not on heroics.',
    'Governance Pillar Leader': 'A Governance Pillar Leader is successful when the governance program enables rather than constrains the organization. Key indicators: compliance calendars are predictable and auditable; the policy library is current and comprehensive; standards are technically validated and adopted by Engineering; regulatory changes are assessed and actioned before they become compliance gaps. The leader is the CISO\'s trusted advisor on regulatory strategy and the person who ensures the governance machine runs quietly in the background.',
    'Chief Information Security Officer (CISO)': 'A CISO is successful when the organization\'s cybersecurity risk is understood, accepted by leadership, and managed within appetite. Key indicators: the CISO has the confidence of the board and executive leadership; cybersecurity metrics are presented in business terms and drive decisions; the security program has adequate budget and resources; incident response is effective without requiring the CISO\'s direct involvement in every call. The CISO builds a program that survives their departure and a culture where security is everyone\'s business.',
    'Executive Sponsor': 'An Executive Sponsor is successful when cybersecurity is resourced and governed as a business priority, not a technical cost center. Key indicators: the sponsor ensures that cybersecurity has a seat at the leadership table; budget requests are evaluated against risk, not against last year\'s spend; the sponsor champions security culture from the top; the CISO has direct access to the sponsor without going through intermediaries. The sponsor\'s success is measured by whether the organization\'s security posture improves during their tenure, not by whether an incident occurred.',
    'Incident Commander': 'An Incident Commander is successful when incidents are managed efficiently, decisively, and with minimal business impact. Key indicators: every incident has a clear commander, a documented timeline, and a post-incident report; containment decisions are made within the SLA for the severity level; communication to stakeholders is regular and accurate; post-incident actions are tracked to closure. The commander keeps the response team focused and effective under pressure, ensuring that the organization learns from every incident.',
    'Lead Investigator': 'A Lead Investigator is successful when every investigation produces defensible findings that stand up to legal and regulatory scrutiny. Key indicators: evidence is collected and preserved with a complete chain of custody; the investigation timeline is documented and repeatable; findings are specific enough that the organization can act on them; post-incident reports are structured, complete, and filed within SLA. The investigator\'s work ensures that the organization can explain exactly what happened, when, and why — to a regulator, a court, or the board.',
}

# ──────────────────────────────────────────────────
# MANAGEMENT TRACK — §11.3 formalization
# Uses JA-001 §8 career pathing rules
# ──────────────────────────────────────────────────

def get_management_track_text(role_name, jf_family):
    """Generate §11.3 Management Track Option text specific to this role."""
    if jf_family == 'JF-ADJUNCT':
        return (
            'Management track progression for Adjacent roles follows the '
            'Incident Response team\'s career framework, not CERG\'s. '
            'See [OM-001 §3.4] for the Adjacent Function boundary definition. '
            'CERG\'s Management track is documented in [JA-001 §5] '
            '(Management Progression: Grade Definitions) and §8.1 '
            '(SME to Management Transition).'
        )
    elif jf_family == 'JF-EXEC':
        if 'CISO' in role_name:
            return (
                'The CISO is an organizational leadership role that sits above the '
                'standard SME/Management track duality. See [JA-001 §5.4] '
                '(Director Grade M4) for the CISO level definition. '
                'Management competencies for leaders are documented in '
                '[CMP-001 §7] (Management Track Competency Addendum), '
                'including People Leadership, Strategic Thinking, Resource and '
                'Budget Management, Stakeholder Management, and Organizational '
                'Development.'
            )
        else:
            return (
                'The Executive Sponsor is a business leadership role outside the '
                'CERG grade structure. See [OM-001 §5] for the Executive '
                'Sponsor\'s role definition. CERG\'s Management track for internal '
                'roles is documented in [JA-001 §5] and [CMP-001 §7].'
            )
    else:
        return (
            'At L3+ (SME track), a Management track option may be available '
            'per [JA-001 §8.1] (SME to Management Transition). Readiness indicators '
            'include: consistently sought out for guidance by junior team members, '
            'leading cross-functional initiatives without formal authority, and '
            'communicating clearly with non-technical stakeholders. The transition '
            'is a track change, not a grade promotion — an S3 Advisor moving to M1 '
            'Manager carries their technical credibility into the management role. '
            'Management competencies are defined in [CMP-001 §7]. '
            'See [JA-001 §5] for Management grade definitions (M1-M4) and '
            '§9 (Span of Control and Team Design) for when to create a management role.'
        )


# ──────────────────────────────────────────────────
# ROLE-TO-PILLAR MAPPING
# ──────────────────────────────────────────────────

# Each entry: (role_name, file_path, pillar, is_pillar_leader)
# Pillar: 'eng', 'risk', 'gov', 'exec', 'adjunct'
# is_pillar_leader: True for roles that also need Management addendum note
ROLES = [
    # JF-SECENG
    ('Cloud Security Engineer', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-001_Cloud_Security_Engineer.md', 'eng', False),
    ('Identity Engineer', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-002_Identity_Engineer.md', 'eng', False),
    ('OT Security Engineer', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-003_OT_Security_Engineer.md', 'eng', False),
    ('Application Security Engineer', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-004_Application_Security_Engineer.md', 'eng', False),
    ('Endpoint Engineer', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-005_Endpoint_Engineer.md', 'eng', False),
    ('Cryptography Engineer', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-006_Cryptography_Engineer.md', 'eng', False),
    ('Engineering Pillar Leader', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-007_Engineering_Pillar_Leader.md', 'eng', True),
    ('Pre-production Reviewer', f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md', 'eng', False),
    # JF-RISKOPS
    ('Exposure Management Lead', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Exposure_Management_Lead.md', 'risk', False),
    ('Adversarial Testing Lead', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-002_Adversarial_Testing_Lead.md', 'risk', False),
    ('Threat Intelligence Analyst', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-003_Threat_Intelligence_Analyst.md', 'risk', False),
    ('Detection Engineer', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md', 'risk', False),
    ('OT Risk Analyst', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-005_OT_Risk_Analyst.md', 'risk', False),
    ('Identity Risk Analyst', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-006_Identity_Risk_Analyst.md', 'risk', False),
    ('Vendor Risk Analyst', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md', 'risk', False),
    ('Risk Pillar Leader', f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-008_Risk_Pillar_Leader.md', 'risk', True),
    # JF-GOVCOMP
    ('NERC-CIP Compliance Manager', f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-001_NERC-CIP_Compliance_Manager.md', 'gov', False),
    ('CMMC / Federal Compliance Manager', f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-002_CMMC_Federal_Compliance_Manager.md', 'gov', False),
    ('SOX ITGC Lead', f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-003_SOX_ITGC_Lead.md', 'gov', False),
    ('Policy & Standards Manager', f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-004_Policy_and_Standards_Manager.md', 'gov', False),
    ('Risk Register Owner', f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-005_Risk_Register_Owner.md', 'gov', False),
    ('Evidence Librarian', f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-006_Evidence_Librarian.md', 'gov', False),
    ('Governance Pillar Leader', f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-007_Governance_Pillar_Leader.md', 'gov', True),
    # JF-EXEC
    ('Chief Information Security Officer (CISO)', f'{BASE}/roles/jf-exec/CERG-GOV-JD-EXEC-001_Chief_Information_Security_Officer.md', 'exec', True),
    ('Executive Sponsor', f'{BASE}/roles/jf-exec/CERG-GOV-JD-EXEC-002_Executive_Sponsor.md', 'exec', False),
    # JF-ADJUNCT
    ('Incident Commander', f'{BASE}/roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md', 'adjunct', False),
    ('Lead Investigator', f'{BASE}/roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-002_Lead_Investigator.md', 'adjunct', False),
]

PILLAR_MAP = {
    'eng': ('Engineering', ENG),
    'risk': ('Risk', RISK),
    'gov': ('Governance', GOV),
}

DOMAIN_NAMES = [
    'Technical Depth', 'Cross-Pillar Fluency', 'Risk Judgment', 'Communication',
    'Operational Discipline', 'Influence and Mentorship',
    'Compliance and Regulatory Literacy', 'Continuous Learning'
]


def build_competency_section(role_name, pillar, is_pillar_leader):
    """Build the §9 replacement block with behavioral anchors."""
    lines = []
    lines.append('## 9. Competency Expectations by Grade')
    lines.append('')

    if pillar == 'exec':
        lines.append(
            'Competency expectations for this role follow the Management Track '
            'Competency Addendum ([CMP-001 §7]). The five management-specific '
            'domains are: People Leadership, Strategic Thinking, Resource and Budget '
            'Management, Stakeholder Management, and Organizational Development. '
            'Grade-level expectations (M1-M4) for each domain are in CMP-001 §7. '
            'This role is also expected to demonstrate SME competencies in the '
            'relevant home pillar at or above S2 level, as defined in CMP-001 §1.'
        )
        lines.append('')
        lines.append(
            '| CMP-001 §7 Domain | M1 Expectation | M2 Expectation | M3 Expectation | M4 Expectation |'
        )
        lines.append(
            '|-------------------|----------------|----------------|----------------|----------------|'
        )
        mgmt_domains = [
            ('People Leadership', 'Conducts regular, meaningful 1:1s. Sets clear expectations. Delivers honest performance feedback promptly.', 'Develops the Managers reporting to them. Ensures consistent people-management practices.', 'Builds a leadership bench. Shapes the people strategy.', 'Accountable for the entire pillar\'s talent health. Develops next generation of leaders.'),
            ('Strategic Thinking', 'Translates pillar goals into actionable team tasks. Prioritizes team work against organizational objectives.', 'Defines a function strategy and roadmap. Anticipates changes affecting priorities.', 'Shapes pillar strategy. Identifies emerging organizational needs.', 'Sets multi-year strategic direction. Aligns pillar with org strategy.'),
            ('Resource and Budget Management', 'Manages team resources effectively. Identifies resource gaps.', 'Owns the function\'s budget input. Manages vendor relationships.', 'Owns significant budget lines. Builds multi-year resource plans.', 'Owns the pillar\'s budget. Makes investment cases to leadership.'),
            ('Stakeholder Management', 'Represents the team effectively. Manages stakeholder expectations honestly.', 'Manages complex stakeholder relationships across functions.', 'Manages executive stakeholder relationships. Represents CERG externally.', 'Manages the organization\'s most critical stakeholder relationships.'),
            ('Organizational Development', 'Contributes to team culture and morale. Recognizes contributions publicly.', 'Builds a positive, high-performance culture within the function.', 'Shapes organizational culture across the pillar. Leads change initiatives.', 'Shapes organizational culture across CERG. Designs org model.'),
        ]
        for dmn, m1, m2, m3, m4 in mgmt_domains:
            lines.append(f'| {dmn} | {m1} | {m2} | {m3} | {m4} |')
        lines.append('')
        lines.append(
            '> **Full Reference:** See [CMP-001 §7] for the complete Management Track '
            'Competency Addendum. Grade definitions (M1-M4) are in [JA-001 §5]. '
            'The role-specific SME competency matrix from the home pillar is available '
            'in CMP-001 §4-6 as applicable.'
        )
        lines.append('')
        return lines

    elif pillar == 'adjunct':
        lines.append(
            'The two Adjacent Incident Response roles are out of scope for '
            'the CERG Competency Model ([CMP-001 §1]). Behavioral anchors for '
            'these roles follow the Incident Response team\'s competency framework. '
            'For reference, the eight CERG competency domains are listed below; '
            'contact the Incident Response team for domain-specific anchors.'
        )
        lines.append('')
        lines.append('| Competency Domain (CMP-001) | L1 Expectation | L2 Expectation | L3 Expectation | L4 Expectation |')
        lines.append('|-----------------------------|----------------|----------------|----------------|----------------|')
        for domain in DOMAIN_NAMES:
            lines.append(f'| {domain} | See IR team framework | See IR team framework | See IR team framework | See IR team framework |')
        lines.append('')
        lines.append(
            '> **Note:** CMP-001 competency domains provide the organizing structure; '
            'actual anchor text must be sourced from the Incident Response team\'s '
            'competency framework per OM-001 §3.4.'
        )
        lines.append('')
        return lines

    pillar_name, anchors = PILLAR_MAP[pillar]

    if is_pillar_leader:
        lines.append(
            f'Competency expectations for this role follow the {pillar_name} pillar '
            'behavioral anchors from [CMP-001] with the addition of the Management Track '
            'Competency Addendum ([CMP-001 §7]) for leadership-specific domains: '
            'People Leadership, Strategic Thinking, Resource and Budget Management, '
            'Stakeholder Management, and Organizational Development.'
        )
    else:
        lines.append(
            f'Competency expectations for this role follow the {pillar_name} pillar '
            'behavioral anchors from [CMP-001]. Each cell describes observable behavior '
            'demonstrating the competency at that grade. Anchors are cumulative: an L3 '
            'expectation includes the L1 and L2 anchors.'
        )

    lines.append('')
    lines.append('| Competency Domain (CMP-001) | L1 Expectation | L2 Expectation | L3 Expectation | L4 Expectation |')
    lines.append('|-----------------------------|----------------|----------------|----------------|----------------|')

    for domain in DOMAIN_NAMES:
        a = anchors[domain]
        lines.append(f'| {domain} | {a["S1"]} | {a["S2"]} | {a["S3"]} | {a["S4"]} |')

    lines.append('')
    lines.append(
        '> **Full Reference:** See [CMP-001] for the complete competency model, '
        'including the Management Track addendum (§7) and guidance on using the '
        'model for hiring, development, and promotion (§8).'
    )
    lines.append('')
    return lines


def build_success_profile(role_name):
    """Build the §10 replacement block."""
    text = SUCCESS_PROFILES.get(role_name, 'Success in this role is measured by the impact of the role\'s work on the organization\'s security posture, as described in the Role Summary and Key Responsibilities sections above.')
    lines = [
        '## 10. Success Profile',
        '',
        text,
        '',
    ]
    return lines


def build_management_track(role_name, pillar):
    """Build the §11.3 replacement block."""
    # Determine JF family from pillar
    if pillar == 'adjunct':
        jf = 'JF-ADJUNCT'
    elif pillar == 'exec':
        jf = 'JF-EXEC'
    else:
        # Check by role name for more specific JF
        if 'Engineer' in role_name or 'Reviewer' in role_name or 'Pillar Leader' in role_name and 'Engineering' in role_name:
            jf = 'JF-SECENG'
        elif 'Risk' in role_name or 'Vulnerability' in role_name or 'Adversarial' in role_name or 'Threat' in role_name or 'Detection' in role_name:
            jf = 'JF-RISKOPS'
        else:
            jf = 'JF-GOVCOMP'

    text = get_management_track_text(role_name, jf)
    lines = [
        '### 11.3 Management Track Option',
        '',
        text,
        '',
    ]
    return lines


def find_section_bounds(content, section_num):
    """Find (start_line, end_line) for a ## N. section header.
    
    Returns (start, end) where start is the ## N. line and end is the
    line of the NEXT ## N. section (or end of file).
    Works by section number so it's tolerant of any variations in title text.
    """
    lines = content.split('\n')
    pattern = re.compile(rf'^## {section_num}\. ')
    next_pattern = re.compile(rf'^## {section_num + 1}\. ')
    
    start = None
    end = None
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if pattern.match(stripped):
            start = i
        elif start is not None and next_pattern.match(stripped):
            end = i
            break
    
    # If we found start but no next section, scan all remaining for any ## N.
    if start is not None and end is None:
        for i in range(start + 1, len(lines)):
            if lines[i].strip().startswith('## ') and not lines[i].strip().startswith('### '):
                end = i
                break
        if end is None:
            end = len(lines)
    
    return start, end


def main():
    success_9 = 0
    success_10 = 0
    success_11 = 0
    errors = []

    for role_name, filepath, pillar, is_pillar_leader in ROLES:
        try:
            with open(filepath) as f:
                content = f.read()
        except FileNotFoundError:
            print(f"  ✗ ERROR: {filepath} not found")
            errors.append(role_name)
            continue

        lines = content.split('\n')
        changed = False

        # ── §9: Competency Anchors ──
        s9_start, s9_end = find_section_bounds(content, 9)
        if s9_start is None:
            print(f"  ⚠ {role_name}: cannot find §9 start")
        else:
            new_s9 = build_competency_section(role_name, pillar, is_pillar_leader)
            lines[s9_start:s9_end] = new_s9
            changed = True
            success_9 += 1

        if not changed:
            content = '\n'.join(lines)
        else:
            content = '\n'.join(lines)

        # ── §10: Success Profile ──
        s10_start, s10_end = find_section_bounds(content, 10)
        if s10_start is None:
            print(f"  ⚠ {role_name}: cannot find §10 start")
        else:
            new_s10 = build_success_profile(role_name)
            lines = content.split('\n')
            lines[s10_start:s10_end] = new_s10
            content = '\n'.join(lines)
            success_10 += 1

        # ── §11.3: Management Track ──
        # We need to find the ### 11.3 subsection within §11
        lines = content.split('\n')
        s11_start = None
        s11_end = None
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped == '### 11.3 Management Track Option':
                s11_start = i
            elif s11_start is not None and stripped.startswith('## 12.'):
                s11_end = i
                break

        if s11_start is None:
            print(f"  ⚠ {role_name}: cannot find §11.3 start")
        else:
            new_s11 = build_management_track(role_name, pillar)
            lines[s11_start:s11_end] = new_s11
            content = '\n'.join(lines)
            success_11 += 1

        # Write file
        with open(filepath, 'w') as f:
            f.write(content)

        n9 = len(build_competency_section(role_name, pillar, is_pillar_leader))
        print(f"  ✓ {role_name}: §9 ({n9} lines), §10 (populated), §11.3 (formalized)")

    print(f"\n{'='*60}")
    print(f"§9 Competency Anchors: {success_9}/27 populated")
    print(f"§10 Success Profiles: {success_10}/27 populated")
    print(f"§11.3 Management Track: {success_11}/27 formalized")
    if errors:
        print(f"Errors: {', '.join(errors)}")


if __name__ == '__main__':
    main()