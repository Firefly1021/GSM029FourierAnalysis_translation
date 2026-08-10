"""Command-line interface for the multi-book translation system."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .project import ProjectError, ProjectPaths, load_config, validate_project_structure
from .template import compile_reference, validate_template_inputs, verify_manifest, write_analysis_reports, write_manifest
from .workflow import (
    approve_sample,
    book_status,
    finish_book,
    list_books,
    new_book,
    resume_book,
    start_book,
    terminology_action,
    translate_book,
)


def _print_json(value: object) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def _inspect_template() -> int:
    problems = validate_template_inputs()
    if problems:
        raise ProjectError("\n".join(problems))
    manifest = write_manifest()
    analysis, dependencies = write_analysis_reports()
    _print_json({
        "files": len(manifest["files"]),
        "reference": manifest["selected_reference"],
        "document_class": analysis["document_class"],
        "engine": analysis["engine"],
        "missing_dependencies": len(dependencies["missing"]),
    })
    return 0


def _verify_template() -> int:
    differences = verify_manifest()
    if differences:
        raise ProjectError("Template integrity verification failed:\n" + "\n".join(differences))
    print("Template integrity verified: all recorded SHA-256 hashes are unchanged.")
    return 0


def _validate_project() -> int:
    missing = validate_project_structure()
    load_config("default.yaml")
    load_config("translation.yaml")
    project = ProjectPaths()
    schema_errors: list[str] = []
    for path in sorted((project.root / "schemas").glob("*.schema.json")):
        try:
            schema = json.loads(path.read_text(encoding="utf-8"))
            if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
                schema_errors.append(f"{path.name}: unsupported or missing $schema")
            if schema.get("type") != "object":
                schema_errors.append(f"{path.name}: root type must be object")
        except (OSError, json.JSONDecodeError) as exc:
            schema_errors.append(f"{path.name}: {exc}")
    errors = [*missing, *schema_errors]
    if errors:
        raise ProjectError("Project validation failed:\n" + "\n".join(errors))
    print("Shared structure, per-book structure, configuration, and JSON Schemas are valid.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mathbook")
    sub = parser.add_subparsers(dest="command", required=True)

    new = sub.add_parser("new-book", help="register a source PDF and create an isolated branch/worktree")
    new.add_argument("book_id")
    new.add_argument("--source", required=True, type=Path)

    for name in ("start-book", "approve-sample", "translate-book", "resume", "finish-book", "status"):
        command = sub.add_parser(name)
        command.add_argument("book_id")
    sub.add_parser("list-books")

    terminology = sub.add_parser("terminology")
    terminology.add_argument("action", choices=("review", "promote", "conflicts", "history"))
    terminology.add_argument("book_id", nargs="?")

    sub.add_parser("inspect-template")
    sub.add_parser("verify-template")
    sub.add_parser("compile-template")
    sub.add_parser("validate-project")
    return parser


def dispatch(args: argparse.Namespace) -> int:
    project = ProjectPaths()
    if args.command == "new-book":
        _print_json(new_book(project, args.book_id, args.source))
    elif args.command == "start-book":
        _print_json(start_book(project, args.book_id))
    elif args.command == "approve-sample":
        _print_json(approve_sample(project, args.book_id))
    elif args.command == "translate-book":
        _print_json(translate_book(project, args.book_id))
    elif args.command == "resume":
        _print_json(resume_book(project, args.book_id))
    elif args.command == "finish-book":
        _print_json(finish_book(project, args.book_id))
    elif args.command == "status":
        _print_json(book_status(project, args.book_id))
    elif args.command == "list-books":
        _print_json(list_books(project))
    elif args.command == "terminology":
        _print_json(terminology_action(project, args.action, args.book_id))
    elif args.command == "inspect-template":
        return _inspect_template()
    elif args.command == "verify-template":
        return _verify_template()
    elif args.command == "compile-template":
        report = compile_reference()
        _print_json(report)
        return 0 if report["success"] and report["template_integrity_verified"] else 1
    elif args.command == "validate-project":
        return _validate_project()
    else:
        raise ProjectError(f"Unsupported command: {args.command}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return dispatch(args)
    except (ProjectError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
