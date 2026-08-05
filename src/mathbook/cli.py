"""Command-line entry point for the Phase 1 project."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .project import ROOT, ProjectError, SOURCE_PDF_MESSAGE, load_config, source_pdf_files, validate_project_structure
from .template import compile_reference, validate_template_inputs, verify_manifest, write_analysis_reports, write_manifest


PDF_COMMANDS = {
    "inspect-pdf", "render", "extract", "structure", "terminology",
    "check-names", "translate", "qa", "compile",
}


def _status() -> int:
    path = ROOT / "PROJECT_STATUS.md"
    print(path.read_text(encoding="utf-8").strip())
    return 0


def _inspect_template() -> int:
    problems = validate_template_inputs()
    if problems:
        raise ProjectError("\n".join(problems))
    manifest = write_manifest()
    analysis, dependencies = write_analysis_reports()
    print(json.dumps({
        "files": len(manifest["files"]),
        "reference": manifest["selected_reference"],
        "document_class": analysis["document_class"],
        "engine": analysis["engine"],
        "missing_dependencies": len(dependencies["missing"]),
    }, ensure_ascii=False, indent=2))
    return 0


def _verify_template() -> int:
    problems = validate_template_inputs()
    if problems:
        raise ProjectError("\n".join(problems))
    differences = verify_manifest()
    if differences:
        raise ProjectError("Template integrity verification failed:\n" + "\n".join(differences))
    print("Template integrity verified: all recorded SHA-256 hashes are unchanged.")
    return 0


def _compile_template() -> int:
    report = compile_reference()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["success"] and report["template_integrity_verified"] else 1


def _validate_project() -> int:
    missing = validate_project_structure()
    for name in ("project.yaml", "translation.yaml"):
        load_config(name)
    schema_errors: list[str] = []
    for path in sorted((ROOT / "schemas").glob("*.schema.json")):
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                schema_errors.append(f"{path.name}: unsupported or missing $schema")
            if schema.get("type") != "object":
                schema_errors.append(f"{path.name}: root type must be object")
        except (OSError, json.JSONDecodeError) as exc:
            schema_errors.append(f"{path.name}: {exc}")
    errors = missing + schema_errors
    if errors:
        raise ProjectError("Project validation failed:\n" + "\n".join(errors))
    print("Project structure, configuration, and JSON Schema files are valid.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mathbook")
    parser.add_argument("command", choices=[
        "status", "inspect-template", "verify-template", "compile-template", "validate-project",
        "inspect-pdf", "render", "extract", "structure", "terminology", "check-names",
        "translate", "qa", "compile",
    ])
    return parser


def run_command(command: str) -> int:
    if command == "status":
        return _status()
    if command == "inspect-template":
        return _inspect_template()
    if command == "verify-template":
        return _verify_template()
    if command == "compile-template":
        return _compile_template()
    if command == "validate-project":
        return _validate_project()
    if command in PDF_COMMANDS:
        if not source_pdf_files():
            raise ProjectError(SOURCE_PDF_MESSAGE)
        raise ProjectError(f"The '{command}' command is not enabled beyond the validated sample.")
    raise ProjectError(f"Unsupported command: {command}")


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return run_command(args.command)
    except ProjectError as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
