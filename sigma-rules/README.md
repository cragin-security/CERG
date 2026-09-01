# CERG Sigma Rules

This directory houses Sigma detection rules for the CERG security operating model.

## Current Status

Sigma rules are under active development. For the initial v1 release, CERG recommends using the following authoritative Sigma rule sources directly:

| Source | Description | Link |
|--------|-------------|------|
| **SigmaHQ/sigma** | The official Sigma rule repository — community-maintained, broad coverage | [github.com/SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) |
| **Elastic Detection Rules** | Elastic's detection rule set, including Sigma-format rules | [github.com/elastic/detection-rules](https://github.com/elastic/detection-rules) |
| **Wazuh Ruleset** | Built-in rules for Wazuh deployments | [documentation.wazuh.com](https://documentation.wazuh.com/current/user-manual/ruleset/index.html) |

## Rule Conversion

CERG detection rules are written in **Sigma format** (portable across Elastic, Splunk, Wazuh, Sentinel) and converted using `sigmac`:

```bash
pip install sigmatools
sigmac -t elastic -o /output/rules.json rule.yml
```

## Integration with MSP Runbook

When the MSP Runbook references `sigma-rules/`, use the SigmaHQ repository directly until CERG ships its own curated rule set.

## Planned

- CERG-specific detection rules mapped to the Extended Control Baseline
- Sigma-to-SIEM conversion scripts
- Atomic Red Team test mappings per rule

---

*This directory is a placeholder for future CERG Sigma rule content.*
