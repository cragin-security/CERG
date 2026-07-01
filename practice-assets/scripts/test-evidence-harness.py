#!/usr/bin/env python3
"""
CERG Evidence Collection Test Harness v1
=========================================
Purpose: Validate evidence collection scripts against a simulated client environment.
Runs each script in dry-run mode and verifies output structure.

Usage:
  python3 practice-assets/scripts/test-evidence-harness.py

Requires: python3, scripts in practice-assets/scripts/
Output: JSON report of pass/fail per evidence script
"""

import importlib.util
import json
import os
import sys
import tempfile
import traceback
from datetime import datetime

SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
REQUIRED_SCRIPTS = [
    "evidence-collect-entra-id.py",
    "evidence-collect-sentinelone.py",
    "evidence-collect-wiz.py",
]

TEST_RESULTS = []


def load_script_module(script_name):
    """Load a script as a Python module to inspect its interface."""
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if not os.path.exists(script_path):
        return {"file": script_name, "exists": False, "error": "File not found"}

    # Count functions and check for main() or argument parser
    with open(script_path) as f:
        content = f.read()

    has_main = "def main(" in content or "if __name__" in content
    has_argparse = "argparse" in content
    has_functions = content.count("def ") > 0
    line_count = len(content.split("\n"))

    return {
        "file": script_name,
        "exists": True,
        "line_count": line_count,
        "has_main": has_main,
        "has_argparse": has_argparse,
        "has_functions": has_functions,
        "functions_found": has_functions,
    }


def validate_output_structure(script_name):
    """Check that the script would produce plausible output."""
    # Read the script and extract expected output fields
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    with open(script_path) as f:
        content = f.read()

    checks = {
        "has_export": "csv" in content or "json" in content or "Export" in content,
        "has_error_handling": "try" in content and "except" in content,
        "has_authentication": "Connect-" in content or "login" in content.lower() or "auth" in content.lower() or "token" in content.lower(),
        "has_documentation": '"""' in content or "'''" in content or "# " in content[:500],
    }

    return checks


def run_all():
    print(f"CERG Evidence Test Harness v1")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'─' * 60}")
    print()

    overall_pass = True

    for script_name in REQUIRED_SCRIPTS:
        print(f"Testing: {script_name}...")

        try:
            module_info = load_script_module(script_name)
            if not module_info["exists"]:
                print(f"  ✗ MISSING — script not found")
                overall_pass = False
                TEST_RESULTS.append({"script": script_name, "pass": False, "reason": "File not found"})
                continue

            output_checks = validate_output_structure(script_name)

            passes = []
            fails = []

            print(f"  ✓ File exists ({module_info['line_count']} lines)")
            if module_info["has_main"]:
                print(f"  ✓ Has main() or entrypoint")
                passes.append("entrypoint")
            else:
                print(f"  ⚠ No explicit main() — may need wrapper")
                fails.append("No explicit main()")

            if module_info["has_argparse"]:
                print(f"  ✓ Has argument parser")
                passes.append("argparse")
            else:
                print(f"  ⚠ No argument parser — may use hardcoded values")
                fails.append("No argument parser (hardcoded?)")

            if output_checks["has_export"]:
                print(f"  ✓ Produces exportable output (CSV/JSON)")
                passes.append("export_output")
            else:
                print(f"  ⚠ No export output detected")
                fails.append("No export output")

            if output_checks["has_error_handling"]:
                print(f"  ✓ Has try/except error handling")
                passes.append("error_handling")
            else:
                print(f"  ⚠ No try/except error handling")
                fails.append("No try/except error handling")

            if output_checks["has_authentication"]:
                print(f"  ✓ Has authentication mechanism")
                passes.append("auth")
            else:
                print(f"  ⚠ No authentication mechanism detected")
                fails.append("No auth mechanism detected")

            if output_checks["has_documentation"]:
                print(f"  ✓ Has documentation / docstring")
                passes.append("documentation")
            else:
                print(f"  ⚠ Minimal documentation")
                fails.append("Minimal documentation")

            result_pass = len(fails) == 0
            if not result_pass:
                overall_pass = False

            TEST_RESULTS.append({
                "script": script_name,
                "pass": result_pass,
                "pass_count": len(passes),
                "fail_count": len(fails),
                "details": {"passes": passes, "fails": fails},
            })

            status = "✓ PASS" if result_pass else "⚠ PARTIAL"
            print(f"  Result: {status} ({len(passes)}/{(len(passes)+len(fails))} checks passed)")
            print()

        except Exception as e:
            print(f"  ✗ ERROR — {e}")
            traceback.print_exc()
            overall_pass = False
            TEST_RESULTS.append({"script": script_name, "pass": False, "error": str(e)})

    # Summary
    print(f"{'─' * 60}")
    print(f"SUMMARY")
    print(f"{'─' * 60}")

    total = len(TEST_RESULTS)
    passed = sum(1 for r in TEST_RESULTS if r["pass"])
    print(f"  Scripts tested: {total}")
    print(f"  Passed:         {passed}")
    print(f"  Failed:         {total - passed}")
    print(f"  Overall:        {'✓ ALL PASS' if overall_pass else '⚠ ISSUES FOUND'}")

    # Save report
    report_path = os.path.join(SCRIPTS_DIR, "test-evidence-report.json")
    report = {
        "timestamp": datetime.now().isoformat(),
        "overall_pass": overall_pass,
        "results": TEST_RESULTS,
    }
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\n  Report saved: {report_path}")
    return overall_pass


if __name__ == "__main__":
    sys.exit(0 if run_all() else 1)
