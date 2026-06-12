#!/usr/bin/env python3
"""
Populate §6 NICE TKS Statement References in all 27 per-role CERG JD files
using the NIST NICE Framework v2.2.0 components dataset.

Maps each CERG role's primary NICE Work Role (from JF-002) to the
v2.2.0 work role ID, extracts the top 5 Task, Knowledge, and Skill
statements by domain-keyword relevance, and replaces the placeholder §6.
"""
import json
import re
import os
import sys

# ── Load NICE JSON dataset ──
NICE_PATH = '/tmp/nice_components.json'
if not os.path.exists(NICE_PATH):
    print(f"ERROR: NICE dataset not found at {NICE_PATH}")
    print("Download with: curl -sL -o /tmp/nice_components.json \\")
    print('  "https://csrc.nist.gov/csrc/media/Projects/cprt/documents/nice/v2-2-0_nf_components.json"')
    sys.exit(1)

with open(NICE_PATH) as f:
    nice_data = json.load(f)

elem_by_id = {e['element_identifier']: e for e in nice_data['elements']}

# Build work_role -> TKS lookup
wr_tks = {}
for r in nice_data['relationships']:
    src = r['source_element_identifier']
    dst = r['dest_element_identifier']
    if src not in wr_tks:
        wr_tks[src] = {'tasks': [], 'knowledge': [], 'skills': []}
    dst_elem = elem_by_id.get(dst)
    if dst_elem:
        t = dst_elem['element_type']
        if t == 'task':
            wr_tks[src]['tasks'].append(dst_elem)
        elif t == 'knowledge':
            wr_tks[src]['knowledge'].append(dst_elem)
        elif t == 'skill':
            wr_tks[src]['skills'].append(dst_elem)

# ── Old-to-new NICE Work Role ID mapping ──
OLD_TO_NEW = {
    'SP-ARC-001': 'DD-WRL-001',
    'SP-ARC-002': 'DD-WRL-002',
    'SP-DEV-001': 'DD-WRL-005',
    'SP-DEV-002': 'DD-WRL-003',
    'OM-ANA-001': 'IO-WRL-006',
    'OM-NET-001': 'IO-WRL-004',
    'OM-KMG-001': 'IO-WRL-003',
    'OV-SCA-001': 'OG-WRL-012',
    'OV-SAA-001': 'OG-WRL-013',
    'OV-PSP-001': 'OG-WRL-002',
    'OV-PMA-001': 'OG-WRL-016',
    'OV-WDM-001': 'OG-WRL-003',
    'OV-ISSN-001': 'OG-WRL-014',
    'OG-WRL-001': 'OG-WRL-007',
    'PR-VAM-001': 'PD-WRL-007',
    'PR-CDA-001': 'PD-WRL-001',
    'PR-CIR-001': 'PD-WRL-003',
    'PR-INF-001': 'PD-WRL-004',
    'AN-TWA-001': 'PD-WRL-006',
    'AN-ASA-001': 'IO-WRL-001',
    'CO-CIP-001': 'PD-WRL-006',
    'IN-WRL-001': 'IN-WRL-001',
    'IN-WRL-002': 'IN-WRL-002',
}

def get_new_code(old_code):
    return OLD_TO_NEW.get(old_code, old_code)

# ── Domain relevance keywords per CERG role ──
# Each role gets keywords to prioritise TKS statements most relevant to its domain.
ROLE_KEYWORDS = {
    # JF-SECENG
    'Cloud Security Engineer': [
        'cloud', 'saas', 'iaas', 'paas', 'infrastructure', 'network',
        'virtualization', 'container', 'orchestration', 'api', 'identity',
        'access control', 'iam', 'encryption', 'data protection',
        'architecture', 'federation', 'workload', 'landing zone',
        'cspm', 'casb', 'cwp', 'sso', 'zero trust'
    ],
    'Identity Engineer': [
        'identity', 'access control', 'iam', 'authentication', 'authorization',
        'federation', 'sso', 'directory', 'active directory', 'ldap',
        'privileged access', 'pam', 'mfa', 'credential', 'password',
        'role', 'entitlement', 'user', 'account', 'certificate', 'pki'
    ],
    'OT Security Engineer': [
        'operational technology', 'ot', 'ics', 'scada', 'industrial control',
        'plc', 'rtu', 'physical', 'safety', 'cyber-physical',
        'network', 'segmentation', 'purdue', 'protocol', 'modbus',
        'dnp3', 'field device', 'sensor', 'actuator', 'process control'
    ],
    'Application Security Engineer': [
        'application security', 'sdlc', 'secure coding', 'code review',
        'owasp', 'ci/cd', 'pipeline', 'static analysis', 'dynamic analysis',
        'dependency', 'vulnerability', 'threat modeling', 'software',
        'development', 'deployment', 'devsecops', 'api', 'web',
        'penetration test', 'security testing', 'bug bounty'
    ],
    'Endpoint Engineer': [
        'endpoint', 'device', 'workstation', 'server', 'mobile',
        'os', 'operating system', 'hardening', 'configuration',
        'antivirus', 'edr', 'xdr', 'host', 'agent', 'deployment',
        'patch', 'update', 'baseline', 'compliance', 'inventory'
    ],
    'Cryptography Engineer': [
        'cryptography', 'encryption', 'key management', 'pki',
        'certificate', 'tls', 'ssl', 'hsm', 'cipher', 'hash',
        'signature', 'cryptographic', 'public key', 'secret',
        'algorithm', 'quantum', 'key rotation', 'crypto',
        'random', 'entropy', 'secure channel'
    ],
    'Engineering Pillar Leader': [
        'leadership', 'management', 'strategy', 'budget', 'resource',
        'governance', 'risk', 'compliance', 'architecture',
        'security architecture', 'program', 'stakeholder',
        'communication', 'team', 'mentor', 'direction',
        'oversight', 'policy', 'standard', 'vision'
    ],
    'Pre-production Reviewer': [
        'review', 'assessment', 'evaluation', 'architecture review',
        'threat modeling', 'security control', 'control assessment',
        'compliance', 'design review', 'risk analysis',
        'audit', 'verification', 'validation', 'testing',
        'acceptance', 'approval', 'gate', 'quality', 'assurance'
    ],
    # JF-RISKOPS
    'Vulnerability Management Lead': [
        'vulnerability', 'cve', 'cwe', 'scanning', 'remediation',
        'patch', 'exposure', 'prioritization', 'risk scoring',
        'cvss', 'epss', 'vulnerability management', 'triage',
        'exploit', 'mitigation', 'reporting', 'metrics',
        'inventory', 'asset', 'discovery', 'reconnaissance'
    ],
    'Adversarial Testing Lead': [
        'penetration test', 'pentest', 'red team', 'adversarial',
        'exploitation', 'ethical hacking', 'social engineering',
        'phishing', 'web application test', 'network test',
        'wireless test', 'physical security test', 'attack simulation',
        'tactics', 'techniques', 'procedure', 'mitre',
        'purple team', 'breach simulation', 'scoping'
    ],
    'Threat Intelligence Analyst': [
        'threat intelligence', 'threat', 'intelligence', 'ttps',
        'indicator', 'ioc', 'actor', 'campaign', 'malware',
        'ransomware', 'apt', 'cyber threat', 'threat hunting',
        'osint', 'open source', 'intelligence analysis',
        'threat landscape', 'adversary', 'tactics', 'techniques'
    ],
    'Detection Engineer': [
        'detection', 'alert', 'siem', 'rule', 'correlation',
        'signature', 'anomaly', 'monitoring', 'log analysis',
        'event', 'detection engineering', 'detection rule',
        'false positive', 'telemetry', 'data source',
        'security monitoring', 'suricata', 'sigma', 'yara',
        'machine learning', 'behavioral'
    ],
    'OT Risk Analyst': [
        'operational technology', 'ot', 'ics', 'scada', 'risk',
        'risk assessment', 'risk analysis', 'safety', 'critical infrastructure',
        'physical', 'cyber-physical', 'impact', 'likelihood',
        'resilience', 'reliability', 'availability',
        'safety', 'process', 'industrial', 'asset criticality'
    ],
    'Identity Risk Analyst': [
        'identity', 'access', 'risk', 'risk assessment',
        'user behavior', 'anomaly', 'privilege', 'entitlement',
        'access review', 'access certification', 'segregation of duties',
        'sod', 'iam risk', 'identity governance', 'iga',
        'user access', 'risk scoring', 'insider',
        'authentication risk', 'authorization risk'
    ],
    'Vendor Risk Analyst': [
        'vendor', 'third party', 'supply chain', 'vendor risk',
        'tprm', 'assessment', 'questionnaire', 'due diligence',
        'contract', 'sla', 'saas', 'cloud provider',
        'subprocessor', 'data sharing', 'vendor management',
        'risk assessment', 'onboarding', 'offboarding', 'tiering'
    ],
    'Risk Pillar Leader': [
        'leadership', 'risk management', 'strategy', 'governance',
        'risk appetite', 'risk tolerance', 'board', 'reporting',
        'metrics', 'program', 'stakeholder', 'communication',
        'vision', 'direction', 'oversight', 'policy',
        'compliance', 'regulatory', 'risk framework'
    ],
    # JF-GOVCOMP
    'NERC-CIP Compliance Manager': [
        'nerc', 'cip', 'compliance', 'regulatory', 'electric',
        'grid', 'bulk power', 'critical infrastructure',
        'audit', 'evidence', 'control testing', 'implementation',
        'npcc', 'enforcement', 'reliability', 'standard',
        'compliance monitoring', 'self-certification'
    ],
    'CMMC / Federal Compliance Manager': [
        'cmmc', 'federal', 'dfars', 'nist 800-171', 'nist 800-53',
        'compliance', 'audit', 'assessment', 'certification',
        'cui', 'controlled unclassified', 'ssp', 'plan of action',
        'poam', 'evidence', 'control', 'fedramp', 'fisma'
    ],
    'SOX ITGC Lead': [
        'sox', 'itgc', 'audit', 'financial', 'control testing',
        'internal control', 'auditor', 'material weakness',
        'deficiency', 'segregation of duties', 'sod',
        'change management', 'access management', 'computer operations',
        'pcaob', 'coso', 'control design', 'operating effectiveness'
    ],
    'Policy & Standards Manager': [
        'policy', 'standard', 'procedure', 'governance',
        'documentation', 'writing', 'compliance', 'regulatory',
        'framework', 'nist', 'iso', 'development', 'review',
        'approval', 'maintenance', 'policy management',
        'guideline', 'directive', 'control', 'requirement'
    ],
    'Risk Register Owner': [
        'risk register', 'risk', 'register', 'tracking',
        'risk treatment', 'risk acceptance', 'mitigation',
        'remediation', 'status', 'reporting', 'dashboard',
        'risk owner', 'risk scoring', 'risk review',
        'risk reduction', 'risk aging', 'exception', 'waiver',
        'acceptance', 'residual risk'
    ],
    'Evidence Librarian': [
        'evidence', 'artifact', 'collection', 'retention',
        'repository', 'library', 'catalog', 'metadata',
        'lifecycle', 'storage', 'preservation', 'disposition',
        'control evidence', 'audit evidence', 'documentation',
        'index', 'search', 'retrieval', 'version', 'archive'
    ],
    'Governance Pillar Leader': [
        'governance', 'leadership', 'strategy', 'oversight',
        'board', 'reporting', 'compliance', 'regulatory',
        'policy', 'standard', 'framework', 'direction',
        'risk', 'stakeholder', 'communication',
        'program management', 'quality', 'continuous improvement'
    ],
    # JF-EXEC
    'Chief Information Security Officer (CISO)': [
        'cybersecurity', 'leadership', 'executive', 'strategy',
        'risk management', 'board', 'communication', 'vision',
        'program management', 'budget', 'resource', 'compliance',
        'regulatory', 'incident response', 'crisis management',
        'stakeholder', 'policy', 'governance', 'metrics',
        'reporting', 'culture', 'awareness'
    ],
    'Executive Sponsor': [
        'executive', 'sponsor', 'strategy', 'governance',
        'oversight', 'budget', 'resource', 'board',
        'risk appetite', 'decision', 'authority', 'accountability',
        'vision', 'direction', 'investment', 'priority',
        'program', 'project', 'champion', 'advocate'
    ],
    # JF-ADJUNCT
    'Incident Commander': [
        'incident', 'response', 'command', 'triage', 'containment',
        'eradication', 'recovery', 'communication', 'escalation',
        'crisis', 'forensics', 'investigation', 'coordinator',
        'bridge', 'call', 'decision', 'timeline', 'notification',
        'legal', 'regulatory', 'breach', 'severity'
    ],
    'Lead Investigator': [
        'investigation', 'forensic', 'digital evidence', 'analysis',
        'preservation', 'chain of custody', 'imaging', 'collection',
        'examination', 'reporting', 'malware', 'analysis',
        'timeline', 'attribution', 'reconstruction', 'tool',
        'methodology', 'expert', 'witness', 'documentation'
    ],
}

# ── Role-to-file mapping ──
BASE = '/home/lupus/CERG'

ROLE_FILES = [
    # JF-SECENG
    ('Cloud Security Engineer', 'SP-ARC-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-001_Cloud_Security_Engineer.md'),
    ('Identity Engineer', 'OM-ANA-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-002_Identity_Engineer.md'),
    ('OT Security Engineer', 'SP-ARC-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-003_OT_Security_Engineer.md'),
    ('Application Security Engineer', 'SP-DEV-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-004_Application_Security_Engineer.md'),
    ('Endpoint Engineer', 'OM-ANA-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-005_Endpoint_Engineer.md'),
    ('Cryptography Engineer', 'SP-ARC-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-006_Cryptography_Engineer.md'),
    ('Engineering Pillar Leader', 'OG-WRL-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-007_Engineering_Pillar_Leader.md'),
    ('Pre-production Reviewer', 'OV-SCA-001',
     f'{BASE}/roles/jf-seceng/CERG-GOV-JD-SECENG-008_Pre-production_Reviewer.md'),
    # JF-RISKOPS
    ('Vulnerability Management Lead', 'PR-VAM-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-001_Vulnerability_Management_Lead.md'),
    ('Adversarial Testing Lead', 'PR-VAM-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-002_Adversarial_Testing_Lead.md'),
    ('Threat Intelligence Analyst', 'AN-TWA-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-003_Threat_Intelligence_Analyst.md'),
    ('Detection Engineer', 'PR-CDA-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-004_Detection_Engineer.md'),
    ('OT Risk Analyst', 'AN-TWA-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-005_OT_Risk_Analyst.md'),
    ('Identity Risk Analyst', 'PR-CDA-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-006_Identity_Risk_Analyst.md'),
    ('Vendor Risk Analyst', 'OV-SCA-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-007_Vendor_Risk_Analyst.md'),
    ('Risk Pillar Leader', 'OG-WRL-001',
     f'{BASE}/roles/jf-riskops/CERG-GOV-JD-RISKOPS-008_Risk_Pillar_Leader.md'),
    # JF-GOVCOMP
    ('NERC-CIP Compliance Manager', 'OV-SCA-001',
     f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-001_NERC-CIP_Compliance_Manager.md'),
    ('CMMC / Federal Compliance Manager', 'OV-SCA-001',
     f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-002_CMMC_Federal_Compliance_Manager.md'),
    ('SOX ITGC Lead', 'OV-SCA-001',
     f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-003_SOX_ITGC_Lead.md'),
    ('Policy & Standards Manager', 'OV-PSP-001',
     f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-004_Policy_and_Standards_Manager.md'),
    ('Risk Register Owner', 'OV-ISSN-001',
     f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-005_Risk_Register_Owner.md'),
    ('Evidence Librarian', 'OV-SCA-001',
     f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-006_Evidence_Librarian.md'),
    ('Governance Pillar Leader', 'OG-WRL-001',
     f'{BASE}/roles/jf-govcomp/CERG-GOV-JD-GOVCOMP-007_Governance_Pillar_Leader.md'),
    # JF-EXEC
    ('Chief Information Security Officer (CISO)', 'OG-WRL-001',
     f'{BASE}/roles/jf-exec/CERG-GOV-JD-EXEC-001_Chief_Information_Security_Officer.md'),
    ('Executive Sponsor', 'OG-WRL-001',
     f'{BASE}/roles/jf-exec/CERG-GOV-JD-EXEC-002_Executive_Sponsor.md'),
    # JF-ADJUNCT
    ('Incident Commander', 'PR-CIR-001',
     f'{BASE}/roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-001_Incident_Commander.md'),
    ('Lead Investigator', 'PR-CIR-001',
     f'{BASE}/roles/jf-adjunct/CERG-GOV-JD-ADJUNCT-002_Lead_Investigator.md'),
]


def score_tks(tks_item, keywords):
    """Score a TKS statement by how many domain keywords its text contains."""
    text = (tks_item.get('title', '') + ' ' + tks_item.get('text', '')).lower()
    score = 0
    for kw in keywords:
        if kw.lower() in text:
            score += 2
        # Also check individual words
    # Bonus for containing multiple keywords
    matched = sum(1 for kw in keywords if kw.lower() in text)
    return matched + score  # Prefer breadth over depth


def get_top_tks(new_role_id, keywords, n=5):
    """Get top-n Task, Knowledge, and Skill statements for a work role by keyword relevance."""
    tks = wr_tks.get(new_role_id, {'tasks': [], 'knowledge': [], 'skills': []})

    tasks = sorted(tks['tasks'], key=lambda t: score_tks(t, keywords), reverse=True)
    knowledge = sorted(tks['knowledge'], key=lambda t: score_tks(t, keywords), reverse=True)
    skills = sorted(tks['skills'], key=lambda t: score_tks(t, keywords), reverse=True)

    return tasks[:n], knowledge[:n], skills[:n]


def build_section_6(role_name, old_code, new_code, top_tasks, top_knowledge, top_skills):
    """Build the replacement §6 content."""
    lines = []
    lines.append('## 6. NICE TKS Statement References')
    lines.append('')
    lines.append(f'The following Task, Knowledge, and Skill statements are extracted from the NIST NICE Framework v2.2.0 Work Role [{new_code} — {role_name} primary mapping] and filtered by relevance to this CERG role. The full TKS database is maintained at https://www.nist.gov/nice/framework/.')
    lines.append('')
    lines.append('| NICE TKS Type | Statement ID | Statement Summary | Relevance to This Role |')
    lines.append('|---------------|-------------|-------------------|------------------------|')

    for task in top_tasks:
        tid = task['element_identifier']
        summary = task['text'][:120]
        if len(task['text']) > 120:
            summary = summary[:117] + '...'
        # Get a brief relevance note from the matched keywords
        lines.append(f'| Task | {tid} | {summary} | Core work activity for this NICE Work Role |')

    for k in top_knowledge:
        kid = k['element_identifier']
        summary = k['text'][:120]
        if len(k['text']) > 120:
            summary = summary[:117] + '...'
        lines.append(f'| Knowledge | {kid} | {summary} | Foundational knowledge for this role |')

    for s in top_skills:
        sid = s['element_identifier']
        summary = s['text'][:120]
        if len(s['text']) > 120:
            summary = summary[:117] + '...'
        lines.append(f'| Skill | {sid} | {summary} | Core capability for this role |')

    lines.append('')
    lines.append(f'> **Full TKS Reference:** The complete TKS statement set for the primary NICE Work Role ({old_code} → {new_code}) is in the NICE Framework Components v2.2.0 dataset ([download](https://csrc.nist.gov/csrc/media/Projects/cprt/documents/nice/v2-2-0_nf_components.json)). JF-002 contains the complete CERG-to-NICE crosswalk with secondary role mappings.')
    lines.append('')
    return lines


def find_section_6_bounds(content):
    """Find the start and end line numbers of §6 in the file content."""
    lines = content.split('\n')
    start = None
    end = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '## 6. NICE TKS Statement References':
            start = i
        elif start is not None and stripped.startswith('## 7.'):
            end = i
            break
    return start, end


def main():
    total = len(ROLE_FILES)
    success = 0
    skipped = 0
    errors = []

    for role_name, old_code, filepath in ROLE_FILES:
        keywords = ROLE_KEYWORDS.get(role_name, [role_name.lower()])
        new_code = get_new_code(old_code)

        # Skip if no TKS available for this work role
        if new_code not in wr_tks:
            print(f"  ⚠ SKIP {role_name}: no TKS for {old_code}→{new_code}")
            skipped += 1
            continue

        top_tasks, top_knowledge, top_skills = get_top_tks(new_code, keywords)

        if not top_tasks and not top_knowledge and not top_skills:
            print(f"  ⚠ SKIP {role_name}: no TKS returned for {new_code}")
            skipped += 1
            continue

        # Read file
        try:
            with open(filepath) as f:
                content = f.read()
        except FileNotFoundError:
            print(f"  ✗ ERROR {role_name}: file not found at {filepath}")
            errors.append(role_name)
            continue

        # Find §6 bounds
        start, end = find_section_6_bounds(content)
        if start is None or end is None:
            print(f"  ⚠ SKIP {role_name}: cannot find §6 boundaries")
            skipped += 1
            continue

        # Build replacement
        new_section = build_section_6(role_name, old_code, new_code, top_tasks, top_knowledge, top_skills)

        # Replace
        lines = content.split('\n')
        old_section_lines = end - start
        lines[start:end] = new_section

        new_content = '\n'.join(lines)

        with open(filepath, 'w') as f:
            f.write(new_content)

        n_t = len(top_tasks)
        n_k = len(top_knowledge)
        n_s = len(top_skills)
        print(f"  ✓ {role_name} ({old_code}→{new_code}): {n_t}T/{n_k}K/{n_s}S")
        success += 1

    print(f"\n{'='*60}")
    print(f"Done: {success} populated, {skipped} skipped, {len(errors)} errors")
    if errors:
        print(f"Errors: {', '.join(errors)}")


if __name__ == '__main__':
    main()