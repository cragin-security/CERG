# START HERE · Adopting CERG

You just found CERG. You have a repo full of Markdown. What do you actually do on Monday morning?

**This page is your first 48 hours.** Read it before you read anything else.

---

## Step 0: Is CERG right for you right now?

CERG requires organizational commitment. Answer honestly:

- Do you have a named person who will own security? (Even part-time, even informal.)
- Does leadership support establishing guardrails — not just buying tools?
- Can you name the systems, business units, and regulators in your scope?
- Will you track versions, record decisions, and produce evidence?

If you answered **no** to any of these, start with NIST CSF or CIS Controls. Come back to CERG when you're ready.

If you answered **yes** to all four, pick your path below.

If you are still unsure where to begin, use these four helpers before diving into the full library:

- [Framework System Map](governance/CERG-GOV-FRM-002_Framework_System_Map.md) - how the documents, pillars, records, evidence, and improvement loops fit together.
- [Adoption Decision Tree and Dependency Matrix](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md) - which path and overlays apply, plus what must be adopted together.
- [Role-Based Implementation Checklists](governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md) - what the CISO, Governance, Risk, and Engineering leads do first.
- [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md) - the records and minimum evidence that prove the program is operating.
- [Day in the Life examples](examples/day-in-the-life/README.md) - seven narrative walkthroughs showing how the three pillars produce real work during incidents, audits, intake, AI rollouts, and access reviews. Read one before you read the standards.

---

## Path 1: CERG Lite (small security team, 2-8 people)

**You have:** A small team with at least two named participants in cyber risk decisions. No existing framework, or a framework that is not yet operational.

If you are a one-person security function, use CERG as a planning reference and adopt the MVC documents only after you have an Executive Sponsor and an independent approver for High/Critical risk decisions.

**Your goal:** Stand up a real program without drowning in documents.

### First 48 hours

1. **Read the [Cybersecurity Policy](governance/CERG-POL-001_Cybersecurity_Policy.md).** This is the spine. Nothing is authoritative until an Executive Sponsor signs this.
2. **Read the [CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md)** — the three-pillar model. You'll consolidate roles heavily; that's expected.
3. **Read the [Small Team Adoption Path](governance/CERG-GOV-IMP-003_Small_Team_Adoption_Path.md).** This is your primary guide. It covers the CERG Lite package, 5-person operating rhythm, role consolidation map, first 10 records, and spreadsheet schemas.
4. **Read the [Role-Based Implementation Checklists](governance/CERG-GOV-IMP-006_Role_Based_Implementation_Checklists.md).** Use the small-team consolidated checklist if one person holds multiple roles.
5. **Read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4 (MVC). Follow the Minimum Viable CERG sequence.
6. **Fork the repo.** Do not cherry-pick individual files. The documents are interconnected.
7. **Fill in the [Organization Adaptation Profile](governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md).** Set your headcount, sector, and regulators. Do NOT leave the default values.
8. **Start the Risk Register.** Open [the template](templates/CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md). Create your first entry. It can be simple.
9. **Create the first records from the [Record Catalog](governance/CERG-GOV-CAT-002_Record_Catalog.md).** Start with role assignment, evidence index, asset extract, top risks, exposure backlog, and exception register.
10. **Run the first exposure management cycle.** Even if it starts with one Nessus scan on your production subnet, open [PRC-VM-001](procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) and follow the observe → validate → assess reachability → classify → treat → verify flow.

### Your MVC set

Adopt these eight documents first:

1. Cybersecurity Policy
2. CERG Framework
3. Operating Model (focus on §6, role consolidation)
4. Document Catalog (update it as you go)
5. Risk Management Framework
6. Risk Register & Exception Process
7. Risk Register Templates
8. Exposure Management Procedure

Use the Record Catalog, Adoption Safety Guide, Small Team Adoption Path, and Role-Based Implementation Checklists as adoption aids. They help you adopt the MVC; they are not additional MVC requirements.

**Read one story.** The [CERG Lite day-in-the-life walkthrough](examples/day-in-the-life/story-8-cerg-lite-maria.md) shows what your first month of running the MVC actually looks like when two people own everything.

### What you can defer

- All 15 standards (bring in individually as needed)
- Most procedures beyond VM and Risk Register
- Operational packages (unless you're regulated — see Path 3)
- Workforce architecture docs (start with JF-001, defer per-role JDs)
- Machine-readable artifacts
- Detailed job descriptions

---

## Path 2: CERG Standard (existing security team, 6-30 people)

**You have:** A functioning security team. Policies exist but are fragmented. Tools are deployed but processes are ad hoc.

**Your goal:** Replace the pile of disconnected documents with a unified operating model.

### First 48 hours

1. **Read the [CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md).** Map your existing team to the three pillars. Identify gaps.
2. **Read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4-5. Follow the MVC sequence plus core standards.
3. **Map your current documents to CAT-001.** What do you already have that maps to a CERG artifact? What's missing?
4. **Adopt the spine (8 MVC docs) first.** Adapt them to your organization — not the other way around.
5. **Layer core standards next:** Access Management, Asset Management, Configuration Baseline (DISH), IT/Cloud/SaaS where applicable, Logging/Monitoring, and Resilience/Backup.
6. **Add Architecture Review and TPRM procedures.** These are the two procedures that prevent the most future pain.

### Your starting set

MVC (all 8) + Access, Asset, Config Baseline, IT/Cloud/SaaS where applicable, Logging/Monitoring, and Resilience/Backup standards + Architecture Review Procedure, TPRM Procedure.

---

## Path 3: CERG Regulated (NERC-CIP, CMMC, SOX, OT environments)

**You have:** Regulatory obligations. Auditors. Critical infrastructure. An existing security team.

**Your goal:** Map CERG to your regulatory framework without duplicating work.

### First 48 hours

1. **Read the [CERG Framework](governance/CERG-GOV-FRM-001_CERG_Framework.md).** Understand the three-pillar model.
2. **Read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4-5.
3. **Adopt the MVC spine.**
4. **Identify your regulatory overlay.** Open the relevant operational package:
   - NERC-CIP → [PLN-CIP-001](plans/CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md)
   - CMMC / CUI → [PLN-CUI-001](plans/CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md)
   - SOX ITGC → [PLN-SOX-001](plans/CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md)
   - ISO 27001 → [PLN-ISO-001](plans/CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md)
5. **Map your evidence requirements.** Each operational package links evidence to specific CERG procedures. Understanding this linkage is the key to making compliance a byproduct of operations.
6. **See the [Compliance Matrix](governance/CERG-GOV-CMX-001_Compliance_Matrix.md).** 22 security intents mapped to every framework simultaneously.

### Your starting set

MVC + all 15 standards + Architecture Review, TPRM, Change Management, Audit/Evidence procedures + your regulatory operational packages.

---

## What CERG adoption is NOT

- **Not a certification.** You can adopt CERG and still fail a regulatory assessment if controls aren't implemented and evidenced.
- **Not a substitute for judgment.** CERG provides structure. You provide decisions, owners, scope, and risk appetite.
- **Not a one-time exercise.** A program runs on cadence. If you're not producing evidence from real work every month, you're not running CERG.
- **Not shelfware.** If you fork the repo, rename the company, approve everything, and walk away, you have produced exactly nothing.

---

## When you get stuck

**Before you ask for help:**
1. Re-read the [Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §9 (Common Adoption Pitfalls).
2. Check your org profile in [VAR-001](governance/CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) — are you still using the default values?
3. Run `python3 tools/cerg-validate.py` — broken links or catalog mismatches will surface mechanical problems.
4. Look at the [examples/](examples/) directory for sample profiles that match your sector and size.

---

## After the first 30 days

Once MVC is running, layer the remaining documents as needed. The sequence matters less after the spine is in place. Prioritize based on what's causing the most operational friction.

Before broad standard-layer adoption, use the Gate 2 to Gate 3 transition test in the [Adoption Decision Tree and Dependency Matrix](governance/CERG-GOV-IMP-005_Adoption_Decision_Tree_and_Dependency_Matrix.md). Do not advance just because the calendar says day 60 or day 90. Advance when the MVC has produced risk, exposure, intake, evidence, pillar-accountability, and adoption-plan records.

**[Back to README](README.md)** · **[Full catalog](governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md)** · **[Implementation Guide](governance/CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)**
