# Upstream Contribution Workflow v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: When and how practice improvements flow back to upstream CERG

---

## Principles

1. **Client benefit first, upstream second.** The practice's primary obligation is to deliver working programs for clients. Improvements discovered during client work are captured in the practice backlog first. They flow upstream when they are structural enough to benefit all adopters, not just one client profile.

2. **Credit the client investment.** When a client-funded discovery or improvement is contributed upstream, the client is credited in the contribution (e.g., "Initial analysis contributed by [Client Name] during their CERG adoption"). This is not a disclosure of proprietary information — it is attribution for the investment that enabled the improvement.

3. **Open source is not free labor.** The practice contributes upstream because a stronger upstream means less downstream maintenance per client. Contributions are selected for high leverage (widespread benefit, low ongoing maintenance) not for volume.

---

## Decision Tree: Issue vs. PR vs. Practice Asset

| Finding | Action | Example |
|---|---|---|
| Bug in validator or tooling | **File upstream issue** with reproduction steps | `cerg-validate.py` false positive on cross-reference format |
| Missing control in CB-001 | **File upstream issue** with proposed control | PCI overlay crosswalk in CB-001 §10.5 |
| Missing template for common scenario | **File upstream issue** with template draft | SCP-001 template was contributed this way |
| Clarification needed in existing doc | **File upstream issue** with proposed language | Ambiguous "critical vulnerability" definition in PRC-VM-001 |
| Client-specific adaptation not generalizable | **Keep as practice asset** — do not upstream | Sector-specific metric priorities (they are consulting conventions, not CERG framework) |
| Client-funded build of new overlay | **Discuss with upstream maintainer** before filing | New regulatory package for a client's specific regulator |
| Practice-only workflow or cheat sheet | **Keep as practice asset** — do not upstream | Intake questionnaire, scope templates, debrief protocol |

---

## Workflow

### Step 1: Capture
During or after an engagement, the practitioner records the finding in the practice backlog (see 6.3) with the appropriate category tag.

### Step 2: Triage
The Practice Principal reviews backlog items quarterly for upstream suitability. Selection criteria:

| Criterion | Weight |
|---|---|
| Benefits multiple client profiles | High |
| Reduces practice maintenance burden | High |
| Is consistent with upstream CERG design principles (NIST spine, three pillars, tool-agnostic) | Required |
| Does not expose client-specific configurations | Required |

### Step 3: Prepare
For items selected for upstream contribution:

1. **Issue:** Write a clear, self-contained issue that a maintainer can act on without context from the practice engagement. Include:
   - The problem (what happens today)
   - The expected behavior (what should happen)
   - The proposed change (specific document, section, and language)
   - The rationale (why this matters for adopters in general)

2. **PR:** For mechanical fixes (typo, broken link, template field addition), file a PR directly. For structural changes (new overlay, new control, new template), file an issue first and discuss approach.

### Step 4: Submit
File the issue or PR on the upstream CERG repository (`m0dernz/CERG`). Tag with appropriate labels (enhancement, bug, documentation, help wanted).

### Step 5: Track
Record the upstream issue/PR number in the practice backlog entry. Monitor for responses within 30 days. If no response, the Practice Principal may follow up via the upstream maintainer's preferred channel.

### Step 6: Close
When the contribution is accepted:
- Update the practice backlog entry to `resolved`
- Remove the resolved item from any client-specific improvement registers where it was a placeholder

When the contribution is declined:
- Update the practice backlog entry with the maintainer's rationale
- Re-classify as a practice-only asset
- If the gap is critical for client delivery, build the practice-only workaround

---

## Review Cadence

| Activity | Frequency |
|---|---|
| Backlog review for upstream candidates | Quarterly |
| Upstream issue/PR submission | Quarterly (batched, not ad hoc) |
| Status check on open contributions | Bi-weekly during active submission season |
| Client attribution review | Per contribution |

---

## Target Rate

One upstream contribution per quarter is the minimum target. A contribution can be a high-quality issue, not necessarily a merged PR. The practice measures contribution quality by:
- Does it get acknowledged by maintainers?
- Does it lead to a fix or improvement?
- Does it reduce downstream maintenance for subsequent client engagements?
