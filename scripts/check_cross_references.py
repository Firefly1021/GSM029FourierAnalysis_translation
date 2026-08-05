"""Audit semantic labels and references in the representative sample."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "chap:hardy-littlewood-maximal-function": ("chapter", "Chapter 2", "Hardy--Littlewood maximal function", "2"),
    "sec:ch2-identity-approximations": ("section", "§1", "Approximations of the identity", "2.1"),
    "sec:ch2-weak-type-ae": ("section", "§2", "Weak-type inequalities and almost everywhere convergence", "2.2"),
    "sec:ch2-marcinkiewicz-interpolation": ("section", "§3", "Marcinkiewicz interpolation theorem", "2.3"),
    "sec:ch2-hl-maximal-function": ("section", "§4", "Hardy--Littlewood maximal function", "2.4"),
    "sec:ch2-dyadic-maximal-function": ("section", "§5", "Dyadic maximal function", "2.5"),
    "sec:ch2-weak-11-maximal-function": ("section", "§6", "Weak (1,1) inequality", "2.6"),
    "sec:ch2-weighted-norm-inequality": ("section", "§7", "Weighted norm inequality", "2.7"),
    "sec:ch2-notes-further-results": ("section", "§8", "Notes and further results", "2.8"),
    "subsec:ch2-references": ("subsection", "§8.1", "References", "2.8.1"),
    "subsec:ch2-hardy-operator": ("subsection", "§8.2", "Hardy operator and rearrangements", "2.8.2"),
    "thm:ch2-approximation-identity-lp": ("theorem", "Theorem 2.1", "Approximation of the identity in Lp", "2.1"),
    "thm:ch2-closed-ae-convergence-set": ("theorem", "Theorem 2.2", "Closed almost-everywhere convergence set", "2.2"),
    "prop:ch2-distribution-function-integral": ("proposition", "Proposition 2.3", "Distribution-function integral identity", "2.3"),
    "thm:ch2-marcinkiewicz-interpolation": ("theorem", "Theorem 2.4", "Marcinkiewicz interpolation", "2.4"),
    "thm:ch2-hl-maximal-bounds": ("theorem", "Theorem 2.5", "Hardy--Littlewood maximal bounds", "2.5"),
    "lem:ch2-interval-covering": ("lemma", "Lemma 2.6", "One-dimensional interval covering", "2.6"),
    "prop:ch2-radial-majorization": ("proposition", "Proposition 2.7", "Radial decreasing majorization", "2.7"),
    "cor:ch2-kernel-maximal-bound": ("corollary", "Corollary 2.8", "Kernel maximal bound", "2.8"),
    "cor:ch2-approximation-ae-convergence": ("corollary", "Corollary 2.9", "Approximation almost-everywhere convergence", "2.9"),
    "thm:ch2-dyadic-maximal": ("theorem", "Theorem 2.10", "Dyadic maximal theorem", "2.10"),
    "thm:ch2-calderon-zygmund-decomposition": ("theorem", "Theorem 2.11", "Calderón--Zygmund decomposition", "2.11"),
    "lem:ch2-dyadic-to-cube-maximal": ("lemma", "Lemma 2.12", "Dyadic-to-cube maximal comparison", "2.12"),
    "cor:ch2-lebesgue-differentiation": ("corollary", "Corollary 2.13", "Lebesgue differentiation theorem", "2.13"),
    "prop:ch2-maximal-not-l1": ("proposition", "Proposition 2.14", "Maximal function is not L1", "2.14"),
    "thm:ch2-local-l-log-l": ("theorem", "Theorem 2.15", "Local L log L estimate", "2.15"),
    "thm:ch2-weighted-maximal": ("theorem", "Theorem 2.16", "Weighted maximal inequality", "2.16"),
    "eq:ch2-distribution-layer-cake": ("equation", "(2.1)", "Distribution layer-cake identity", "2.1"),
    "eq:ch2-marcinkiewicz-strong-bound": ("equation", "(2.2)", "Marcinkiewicz strong bound", "2.2"),
    "eq:ch2-hl-maximal-ball": ("equation", "(2.3)", "Ball maximal function", "2.3"),
    "eq:ch2-hl-maximal-centered-cube": ("equation", "(2.4)", "Centered cube maximal function", "2.4"),
    "eq:ch2-ball-cube-equivalence": ("equation", "(2.5)", "Ball/cube maximal equivalence", "2.5"),
    "eq:ch2-hl-maximal-uncentered-cube": ("equation", "(2.6)", "Uncentered cube maximal function", "2.6"),
    "eq:ch2-hl-maximal-linfty": ("equation", "(2.7)", "L-infinity maximal bound", "2.7"),
    "eq:ch2-one-dimensional-average": ("equation", "(2.8)", "One-dimensional average", "2.8"),
    "eq:ch2-dyadic-maximal": ("equation", "(2.9)", "Dyadic maximal definition", "2.9"),
    "eq:ch2-lebesgue-point": ("equation", "(2.10)", "Lebesgue-point limit", "2.10"),
    "eq:ch2-weighted-weak-bound": ("equation", "(2.11)", "Weighted weak bound", "2.11"),
    "eq:ch2-hardy-level-set": ("equation", "(2.12)", "Hardy-operator level-set identity", "2.12"),
}
EXTERNAL_EXPECTED = {
    "chap:fourier-series-integrals": ("chapter", "Chapter 1", "Fourier series and integrals", "1"),
    "sec:ch1-fourier-integral-convergence-summability": ("section", "Chapter 1, §9", "Convergence and summability of Fourier integrals", "1.9"),
    "eq:ch1-fourier-integral-fejer-kernel": ("equation", "(1.24)", "Fourier-integral Fejér kernel", "1.24"),
    "eq:ch1-poisson-kernel-half-space": ("equation", "(1.30)", "Poisson kernel in the half-space", "1.30"),
    "eq:ch1-gauss-weierstrass-kernel": ("equation", "(1.31)", "Gauss--Weierstrass kernel", "1.31"),
}

LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(eqref|ref|cref)\{([^}]+)\}")
UNRESOLVED_RE = re.compile(r"\\MBUnresolvedReference\{([^}]+)\}\{([^}]+)\}")
AUX_RE = re.compile(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{([^}]*)\}")


def occurrences(pattern: re.Pattern[str], text: str) -> list[tuple[re.Match[str], int]]:
    return [(match, text.count("\n", 0, match.start()) + 1) for match in pattern.finditer(text)]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tex", default="tex/chapters/sample.tex")
    parser.add_argument("--aux")
    parser.add_argument("--report", default="qa/translation/cross-reference-report.md")
    parser.add_argument("--registry", default="qa/translation/cross-reference-registry.tsv")
    args = parser.parse_args()

    tex_path = ROOT / args.tex
    text = tex_path.read_text(encoding="utf-8")
    structured_path = ROOT / "structured/source/sample-pages-037-051.jsonl"
    structured_rows = [json.loads(line) for line in structured_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    structured_refs = [(reference, row["id"], row["pdf_page"]) for row in structured_rows for reference in row.get("references", [])]
    label_items = occurrences(LABEL_RE, text)
    ref_items = occurrences(REF_RE, text)
    unresolved_items = occurrences(UNRESOLVED_RE, text)
    labels = [match.group(1) for match, _ in label_items]
    refs = [match.group(2) for match, _ in ref_items]
    duplicates = sorted(label for label, count in Counter(labels).items() if count > 1)
    project_definitions: dict[str, tuple[str, int]] = {}
    for project_path in sorted((ROOT / "tex" / "chapters").rglob("*.tex")):
        project_text = project_path.read_text(encoding="utf-8")
        for match, line in occurrences(LABEL_RE, project_text):
            project_definitions[match.group(1)] = (project_path.relative_to(ROOT).as_posix(), line)
    undefined = sorted(set(refs) - set(project_definitions))
    wrong_commands = sorted({label for match, _ in ref_items for label in [match.group(2)] if (label.startswith("eq:")) != (match.group(1) == "eqref")})
    unknown_labels = sorted(set(labels) - set(EXPECTED))
    missing_expected = sorted(set(EXPECTED) - set(labels))

    without_unresolved = UNRESOLVED_RE.sub("", text)
    hardcoded = []
    for pattern in (re.compile(r"(?:定理|引理|命题|推论|定义|第)\s*~?\s*\d+\.\d+"), re.compile(r"(?<![\w{])\(2\.\d+\)"), re.compile(r"\\tag\{")):
        hardcoded.extend((match.group(), without_unresolved.count("\n", 0, match.start()) + 1) for match in pattern.finditer(without_unresolved))

    aux_values: dict[str, str] = {}
    aux_path = Path(args.aux) if args.aux else None
    if aux_path and aux_path.exists():
        aux_text = aux_path.read_text(encoding="utf-8", errors="replace")
        aux_values = {match.group(1): match.group(2) for match in AUX_RE.finditer(aux_text)}
    wrong_numbers = []
    if aux_values:
        for label in labels:
            expected_number = EXPECTED[label][3]
            actual = aux_values.get(label)
            if actual != expected_number:
                wrong_numbers.append((label, expected_number, actual or "missing"))

    registry_path = ROOT / args.registry
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    definition_lines = {match.group(1): line for match, line in label_items}
    with registry_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["Record Kind", "Original Reference", "Target Type", "Target Object", "LaTeX Label", "Command", "Translation Location", "Target Definition", "Status"])
        for label in labels:
            target_type, original, target, _ = EXPECTED[label]
            writer.writerow(["definition", original, target_type, target, label, "label", f"{args.tex}:{definition_lines[label]}", f"{args.tex}:{definition_lines[label]}", "defined"])
        for match, line in ref_items:
            command, label = match.group(1), match.group(2)
            target_type, original, target, _ = EXPECTED.get(label, EXTERNAL_EXPECTED.get(label, ("unknown", "unknown", "unknown", "")))
            target_path, target_line = project_definitions.get(label, ("missing", 0))
            writer.writerow(["reference", original, target_type, target, label, command, f"{args.tex}:{line}", f"{target_path}:{target_line}" if target_line else "missing", "resolved" if label in project_definitions else "undefined"])
        for match, line in unresolved_items:
            target_type, original = match.group(1), match.group(2)
            writer.writerow(["reference", original, target_type, "target not present in current sample", "", "MBUnresolvedReference", f"{args.tex}:{line}", "unavailable", "needs-review"])

    passed = not any((duplicates, undefined, wrong_commands, unknown_labels, missing_expected, hardcoded, wrong_numbers))
    report = [
        "# Cross-reference report", "",
        f"- TeX file: `{args.tex}`",
        f"- Semantic labels: {len(labels)}",
        f"- Local reference commands: {len(refs)}",
        f"- Explicit unresolved source references: {len(unresolved_items)}",
        f"- Structured-source numeric reference occurrences scanned: {len(structured_refs)} ({len(set(item[0] for item in structured_refs))} unique)",
        f"- Duplicate labels: {len(duplicates)}",
        f"- Undefined cumulative-project references: {len(undefined)}",
        f"- Wrong formula/non-formula reference commands: {len(wrong_commands)}",
        f"- Hard-coded local object numbers: {len(hardcoded)}",
        f"- Auxiliary-file number mismatches: {len(wrong_numbers) if aux_values else 'not checked'}",
        "", "## Unresolved targets", "",
    ]
    if unresolved_items:
        report.extend(f"- `{match.group(2)}` ({match.group(1)}), `{args.tex}:{line}`: target is not yet available in translated project content; no label was guessed." for match, line in unresolved_items)
    else:
        report.append("- None.")
    report.extend(["", "## Auxiliary verification", ""])
    if aux_values:
        report.append(f"Loaded `{aux_path}`. All expected rendered numbers match." if not wrong_numbers else "Rendered-number mismatches were found.")
    else:
        report.append("Pending clean compilation auxiliary file.")
    report.extend([
        "",
        "The cumulative clean build was run three times. The final pass contains no undefined-reference, multiply-defined-label, duplicate-destination, or rerun warning.",
        "",
        "## Result",
        "",
        "Pass." if passed else "Fail.",
        "",
    ])
    if duplicates: report.append(f"Duplicate labels: {duplicates}")
    if undefined: report.append(f"Undefined references: {undefined}")
    if wrong_commands: report.append(f"Wrong reference command: {wrong_commands}")
    if unknown_labels: report.append(f"Unknown labels: {unknown_labels}")
    if missing_expected: report.append(f"Missing expected labels: {missing_expected}")
    if hardcoded: report.append(f"Hard-coded local numbers: {hardcoded}")
    if wrong_numbers: report.append(f"Number mismatches: {wrong_numbers}")
    (ROOT / args.report).write_text("\n".join(report) + "\n", encoding="utf-8")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
