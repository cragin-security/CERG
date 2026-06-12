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

---

## Path 1: CERG Lite (small team, ≤5 people, first security hire)

**You have:** A small team. Maybe one person doing security. No existing framework.

**Your goal:** Stand up a real program without drowning in documents.

### First 48 hours

1. **Read the [Cybersecurity Policy](CERG-POL-001_Cybersecurity_Policy.md).** This is the spine. Nothing is authoritative until an Executive Sponsor signs this.
2. **Read the [CERG Framework](CERG-GOV-FRM-001_CERG_Framework.md)** — the three-pillar model. You'll consolidate roles heavily; that's expected.
3. **Read the [Small Team Adoption Path](CERG-GOV-IMP-003_Small_Team_Adoption_Path.md).** This is your primary guide. It covers the CERG Lite package, 5-person operating rhythm, role consolidation map, first 10 records, and spreadsheet schemas.
4. **Read the [Implementation Guide](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4 (MVC). Follow the Minimum Viable CERG sequence.
5. **Fork the repo.** Do not cherry-pick individual files. The documents are interconnected.
6. **Fill in the [Organization Adaptation Profile](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md).** Set your headcount, sector, and regulators. Do NOT leave the default values.
7. **Start the Risk Register.** Open [the template](CERG-TMPL-RM-001_Risk_Register_Templates_and_Reporting.md). Create your first entry. It can be simple.
8. **Run the first Vulnerability scan cycle.** Even if it's one Nessus scan on your production subnet. Open [PRC-VM-001](CERG-PRC-VM-001_Vulnerability_Management_Procedure.md) and follow the triage flow.

### Your MVC set

1. Cybersecurity Policy
2. CERG Framework
3. Operating Model (focus on §6, role consolidation)
4. Document Catalog (update it as you go)
5. Risk Management Framework
6. Risk Register & Exception Process
7. Risk Register Templates
8. Vulnerability Management Procedure

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

1. **Read the [CERG Framework](CERG-GOV-FRM-001_CERG_Framework.md).** Map your existing team to the three pillars. Identify gaps.
2. **Read the [Implementation Guide](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4-5. Follow the MVC sequence plus core standards.
3. **Map your current documents to CAT-001.** What do you already have that maps to a CERG artifact? What's missing?
4. **Adopt the spine (8 MVC docs) first.** Adapt them to your organization — not the other way around.
5. **Layer core standards next:** Access Management, Configuration Baseline (DISH), IT/Cloud/SaaS, Logging/Monitoring.
6. **Add Architecture Review and TPRM procedures.** These are the two procedures that prevent the most future pain.

### Your starting set

MVC (all 8) + Access Standard, Config Baseline Standard, IT/Cloud/SaaS Standard, Logging/Monitoring Standard + Architecture Review Procedure, TPRM Procedure.

---

## Path 3: CERG Regulated (NERC-CIP, CMMC, SOX, OT environments)

**You have:** Regulatory obligations. Auditors. Critical infrastructure. An existing security team.

**Your goal:** Map CERG to your regulatory framework without duplicating work.

### First 48 hours

1. **Read the [CERG Framework](CERG-GOV-FRM-001_CERG_Framework.md).** Understand the three-pillar model.
2. **Read the [Implementation Guide](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)** §4-5.
3. **Adopt the MVC spine.**
4. **Identify your regulatory overlay.** Open the relevant operational package:
   - NERC-CIP → [PLN-CIP-001](CERG-PLN-CIP-001_NERC_CIP_Operational_Package.md)
   - CMMC / CUI → [PLN-CUI-001](CERG-PLN-CUI-001_CUI_CMMC_Operational_Package.md)
   - SOX ITGC → [PLN-SOX-001](CERG-PLN-SOX-001_SOX_ITGC_Operational_Package.md)
   - ISO 27001 → [PLN-ISO-001](CERG-PLN-ISO-001_ISO_IEC_27001_Operational_Package.md)
5. **Map your evidence requirements.** Each operational package links evidence to specific CERG procedures. Understanding this linkage is the key to making compliance a byproduct of operations.
6. **See the [Compliance Matrix](CERG-GOV-CMX-001_Compliance_Matrix.md).** 22 security intents mapped to every framework simultaneously.

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
1. Re-read the [Implementation Guide](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md) §9 (Common Adoption Pitfalls).
2. Check your org profile in [VAR-001](CERG-GOV-VAR-001_Organization_Adaptation_Profile.md) — are you still using the default values?
3. Run `python3 tools/cerg-validate.py` — broken links or catalog mismatches will surface mechanical problems.
4. Look at the [examples/](examples/) directory for sample profiles that match your sector and size.

---

## After the first 30 days

Once MVC is running, layer the remaining documents as needed. The sequence matters less after the spine is in place. Prioritize based on what's causing the most operational friction.

**[Back to README](README.md)** · **[Full catalog](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md)** · **[Implementation Guide](CERG-GOV-IMP-001_Implementation_and_Adaptation_Guide.md)**
