import importlib.util
import sys
import textwrap
from pathlib import Path


def load_validator():
    module_path = Path(__file__).resolve().parents[1] / "tools" / "cerg-validate.py"
    spec = importlib.util.spec_from_file_location("cerg_validate", module_path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def test_valid_repository_has_no_findings(tmp_path):
    write(
        tmp_path / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md",
        """
        # Catalog

        ## 5. Authoritative Catalog (V1)

        | **ID** | **Title** | **Owner** | **Status** |
        |---|---|---|---|
        | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Cybersecurity Policy | CISO | Approved |
        | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Access Management Standard | Governance Pillar Leader | Approved |

        ## 6. Cross-Reference Rules
        """,
    )
    write(
        tmp_path / "governance" / "CERG-POL-001_Cybersecurity_Policy.md",
        """
        | | |
        |---|---|
        | **Document ID** | CERG-POL-001 |
        | **Status** | Approved |

        See [CERG-STD-AC-001](CERG-STD-AC-001_Access_Management_Standard.md).
        """,
    )
    write(
        tmp_path / "governance" / "CERG-STD-AC-001_Access_Management_Standard.md",
        """
        | | |
        |---|---|
        | **Document ID** | CERG-STD-AC-001 |
        | **Status** | Approved |

        Related: CERG-POL-001.
        """,
    )

    validator = load_validator()
    findings = validator.validate_repository(tmp_path)

    assert findings == []


def test_detects_missing_link_uncataloged_id_and_status_mismatch(tmp_path):
    write(
        tmp_path / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md",
        """
        # Catalog

        ## 5. Authoritative Catalog (V1)

        | **ID** | **Title** | **Owner** | **Status** |
        |---|---|---|---|
        | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Cybersecurity Policy | CISO | Approved |

        ## 6. Cross-Reference Rules
        """,
    )
    write(
        tmp_path / "CERG - Cybersecurity Policy.md",
        """
        | | |
        |---|---|
        | **Document ID** | CERG-POL-001 |
        | **Status** | Draft |

        Broken link: [missing](missing.md).
        Uncataloged reference: CERG-STD-NET-001.
        """,
    )

    validator = load_validator()
    findings = validator.validate_repository(tmp_path)
    messages = "\n".join(f.message for f in findings)

    assert "does not resolve" in messages
    assert "is cited but not listed" in messages
    assert "status mismatch" in messages


def test_detects_catalog_filesystem_mismatches(tmp_path):
    write(
        tmp_path / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md",
        """
        # Catalog

        ## 5. Authoritative Catalog (V1)

        | **ID** | **Title** | **Owner** | **Status** |
        |---|---|---|---|
        | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Cybersecurity Policy | CISO | Approved |
        | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Access Management Standard | Governance Pillar Leader | Approved |

        ## 6. Cross-Reference Rules
        """,
    )
    write(
        tmp_path / "CERG - Cybersecurity Policy.md",
        """
        | | |
        |---|---|
        | **Document ID** | CERG-POL-001 |
        | **Status** | Approved |
        """,
    )
    write(
        tmp_path / "CERG-STD-NET-001_Network_Security_Standard.md",
        """
        | | |
        |---|---|
        | **Document ID** | CERG-STD-NET-001 |
        | **Status** | Draft |
        """,
    )

    validator = load_validator()
    findings = validator.validate_repository(tmp_path)
    messages = "\n".join(f.message for f in findings)

    assert "catalog entry points to missing file" in messages


def test_detects_metadata_version_mismatch_in_same_file(tmp_path):
    """A document with two metadata tables whose Version rows disagree must emit
    a METADATA_VERSION_MISMATCH finding. CAT-001 historically had two metadata
    tables (front-matter and §8 Document Control); contributors would update one
    and forget the other. This test pins the rule in place."""
    write(
        tmp_path / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md",
        """
        # Catalog

        | | |
        |---|---|
        | **Document ID** | CERG-GOV-CAT-001 |
        | **Version** | 1.43 |
        | **Status** | Approved |

        ## 5. Authoritative Catalog (V1)

        | **ID** | **Title** | **Owner** | **Status** |
        |---|---|---|---|
        | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Cybersecurity Policy | CISO | Approved |

        ## 6. Cross-Reference Rules

        ## 7. Document Control

        | | |
        |---|---|
        | **Document ID** | CERG-GOV-CAT-001 |
        | **Version** | 9.99 |
        | **Status** | Approved |
        """,
    )
    write(
        tmp_path / "CERG - Cybersecurity Policy.md",
        """
        | | |
        |---|---|
        | **Document ID** | CERG-POL-001 |
        | **Status** | Approved |
        """,
    )

    validator = load_validator()
    findings = validator.validate_repository(tmp_path)
    version_findings = [f for f in findings if f.code == "METADATA_VERSION_MISMATCH"]
    assert len(version_findings) == 1
    assert "'1.43'" in version_findings[0].message
    assert "'9.99'" in version_findings[0].message


def test_metadata_version_consistency_passes_when_versions_agree(tmp_path):
    """Two metadata tables with the same Version must not emit a finding."""
    write(
        tmp_path / "governance" / "CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md",
        """
        # Catalog

        | | |
        |---|---|
        | **Document ID** | CERG-GOV-CAT-001 |
        | **Version** | 1.43 |
        | **Status** | Approved |

        ## 5. Authoritative Catalog (V1)

        | **ID** | **Title** | **Owner** | **Status** |
        |---|---|---|---|
        | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) | Cybersecurity Policy | CISO | Approved |

        ## 6. Cross-Reference Rules

        ## 7. Document Control

        | | |
        |---|---|
        | **Document ID** | CERG-GOV-CAT-001 |
        | **Version** | 1.43 |
        | **Status** | Approved |
        """,
    )
    write(
        tmp_path / "CERG - Cybersecurity Policy.md",
        """
        | | |
        |---|---|
        | **Document ID** | CERG-POL-001 |
        | **Status** | Approved |
        """,
    )

    validator = load_validator()
    findings = validator.validate_repository(tmp_path)
    version_findings = [f for f in findings if f.code == "METADATA_VERSION_MISMATCH"]
    assert version_findings == []
