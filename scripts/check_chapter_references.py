"""Audit labels and references for one translated chapter."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABEL = re.compile(r"\\label\{([^}]+)\}")
REFERENCE = re.compile(r"\\(?P<command>eqref|ref|cref|Cref|autoref|pageref)\{(?P<label>[^}]+)\}")
UNRESOLVED = re.compile(r"\\MBUnresolvedReference\{(?P<kind>[^}]+)\}\{(?P<source>[^}]+)\}")
PREFIX_KIND = {
    "chap": "chapter",
    "sec": "section",
    "subsec": "subsection",
    "thm": "theorem",
    "lem": "lemma",
    "prop": "proposition",
    "cor": "corollary",
    "def": "definition",
    "eq": "equation",
    "fig": "figure",
    "tab": "table",
    "ex": "example-or-exercise",
    "rem": "remark",
}


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def context_line(text: str, position: int) -> str:
    start = text.rfind("\n", 0, position) + 1
    end = text.find("\n", position)
    return text[start : len(text) if end < 0 else end].strip()


def kind_for(label: str) -> str:
    return PREFIX_KIND.get(label.split(":", 1)[0], "unknown")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("chapter_id", help="For example: chapter-01")
    args = parser.parse_args()
    driver = ROOT / "tex" / "chapters" / f"{args.chapter_id}.tex"
    files = [driver, *sorted((ROOT / "tex" / "chapters" / args.chapter_id).glob("*.tex"))]
    if not driver.is_file() or len(files) == 1:
        raise FileNotFoundError("Chapter driver or section files are missing")

    labels: list[tuple[str, str, int]] = []
    references: list[tuple[str, str, str, int, str]] = []
    unresolved: list[tuple[str, str, str, int]] = []
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        for match in LABEL.finditer(text):
            labels.append((match.group(1), relative, line_number(text, match.start())))
        for match in REFERENCE.finditer(text):
            references.append(
                (
                    match.group("command"),
                    match.group("label"),
                    relative,
                    line_number(text, match.start()),
                    context_line(text, match.start()),
                )
            )
        for match in UNRESOLVED.finditer(text):
            unresolved.append((match.group("kind"), match.group("source"), relative, line_number(text, match.start())))

    project_labels: list[tuple[str, str, int]] = []
    for project_path in sorted((ROOT / "tex").rglob("*.tex")):
        project_text = project_path.read_text(encoding="utf-8")
        relative = project_path.relative_to(ROOT).as_posix()
        for match in LABEL.finditer(project_text):
            project_labels.append((match.group(1), relative, line_number(project_text, match.start())))

    counts = Counter(label for label, _, _ in project_labels)
    duplicates = sorted(label for label, count in counts.items() if count > 1)
    defined = set(counts)
    undefined = sorted({label for _, label, _, _, _ in references if label not in defined})
    wrong_command = sorted(
        {
            f"{path}:{line}: \\{command}{{{label}}}"
            for command, label, path, line, _ in references
            if (label.startswith("eq:") and command != "eqref") or (not label.startswith("eq:") and command == "eqref")
        }
    )

    registry_path = ROOT / "qa" / "translation" / f"{args.chapter_id}-cross-reference-registry.tsv"
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    target_locations = {label: f"{path}:{line}" for label, path, line in project_labels}
    with registry_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["Record Type", "Original Reference", "Target Object", "LaTeX Label", "Command", "Translation Location", "Target Location", "Status"])
        for label, path, line in labels:
            writer.writerow(["target", "", kind_for(label), label, "label", f"{path}:{line}", f"{path}:{line}", "defined"])
        for command, label, path, line, context in references:
            writer.writerow(["reference", context, kind_for(label), label, command, f"{path}:{line}", target_locations.get(label, ""), "resolved" if label in defined else "undefined"])
        for kind, source, path, line in unresolved:
            writer.writerow(["unresolved", source, kind, "", "MBUnresolvedReference", f"{path}:{line}", "", "needs-review"])

    report_path = ROOT / "qa" / "translation" / f"{args.chapter_id}-cross-reference-report.md"
    report = [
        f"# {args.chapter_id} cross-reference report",
        "",
        f"- Files checked: {len(files)}",
        f"- Labels: {len(labels)} ({len(defined)} unique)",
        f"- LaTeX reference commands: {len(references)}",
        f"- Explicit unresolved source references: {len(unresolved)}",
        f"- Duplicate labels: {len(duplicates)}",
        f"- Undefined local labels: {len(undefined)}",
        f"- Incorrect equation/non-equation reference commands: {len(wrong_command)}",
        f"- Registry: `{registry_path.relative_to(ROOT).as_posix()}`",
        "",
        "## Duplicate labels",
        "",
        *([f"- `{item}`" for item in duplicates] or ["- None."]),
        "",
        "## Undefined local labels",
        "",
        *([f"- `{item}`" for item in undefined] or ["- None."]),
        "",
        "## Reference-command mismatches",
        "",
        *([f"- `{item}`" for item in wrong_command] or ["- None."]),
        "",
        "## Explicitly unresolved source references",
        "",
        *([f"- `{kind}` `{source}` at `{path}:{line}`" for kind, source, path, line in unresolved] or ["- None."]),
        "",
        "## Result",
        "",
        "Pass for all determinable local references; unresolved source citations and forward references remain explicit and are not guessed."
        if not duplicates and not undefined and not wrong_command
        else "Fail: resolve the duplicate, undefined, or command-mismatch findings above.",
        "",
    ]
    report_path.write_text("\n".join(report), encoding="utf-8")
    print(f"labels={len(labels)} references={len(references)} unresolved={len(unresolved)} duplicates={len(duplicates)} undefined={len(undefined)} mismatches={len(wrong_command)}")
    return 0 if not duplicates and not undefined and not wrong_command else 1


if __name__ == "__main__":
    raise SystemExit(main())
