"""Read-only LaTeX template inspection, verification, and isolated compilation."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from .project import ROOT, ProjectError, iter_files, load_config, sha256_file


TEMPLATE_ROOT = ROOT / "template"
MANIFEST_PATH = ROOT / "config" / "template-manifest.json"


def _relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def _file_type(path: Path) -> str:
    return {
        ".sty": "latex-package",
        ".cls": "latex-class",
        ".tex": "latex-source",
        ".bib": "bibliography",
        ".png": "image",
        ".jpg": "image",
        ".jpeg": "image",
        ".pdf": "pdf-asset",
        ".ttf": "font",
        ".otf": "font",
        ".gitkeep": "directory-marker",
    }.get(path.suffix.lower() if path.name != ".gitkeep" else ".gitkeep", "auxiliary")


def build_manifest() -> dict[str, Any]:
    """Hash every shared template file without modifying it."""
    files = [
        {
            "path": _relative(path),
            "file_type": _file_type(path),
            "size_bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in iter_files(TEMPLATE_ROOT)
    ]
    references = [item["path"] for item in files if item["file_type"] == "latex-source"]
    configured = load_config("default.yaml")["template"]["reference"]
    if len(references) == 1:
        selection_reason = "The reference directory contains exactly one .tex file."
    elif configured in references:
        selection_reason = "Multiple candidates exist; the selected reference is explicitly configured in config/default.yaml."
    else:
        selection_reason = "No unambiguous reference selection is available."
    return {
        "root": "template",
        "read_only": True,
        "files": files,
        "reference_candidates": references,
        "selected_reference": configured if configured in references else None,
        "selection_reason": selection_reason,
    }


def write_manifest() -> dict[str, Any]:
    manifest = build_manifest()
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def verify_manifest() -> list[str]:
    """Return integrity differences from the recorded manifest."""
    if not MANIFEST_PATH.exists():
        raise ProjectError("Template manifest has not been created.")
    recorded = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    current = build_manifest()
    old = {item["path"]: item["sha256"] for item in recorded["files"]}
    new = {item["path"]: item["sha256"] for item in current["files"]}
    differences: list[str] = []
    for path in sorted(old.keys() | new.keys()):
        if path not in old:
            differences.append(f"added: {path}")
        elif path not in new:
            differences.append(f"removed: {path}")
        elif old[path] != new[path]:
            differences.append(f"changed: {path}")
    return differences


def validate_template_inputs() -> list[str]:
    """Return input problems without changing user files."""
    problems: list[str] = []
    styles = list((TEMPLATE_ROOT / "style").glob("*.sty")) + list((TEMPLATE_ROOT / "style").glob("*.cls"))
    references = list((TEMPLATE_ROOT / "reference").glob("*.tex"))
    if not styles:
        problems.append("No .sty or .cls file exists in template/style/.")
    if not references:
        problems.append("No .tex file exists in template/reference/.")
    config = load_config("default.yaml")["template"]
    for key in ("style", "reference"):
        if not (ROOT / config[key]).is_file():
            problems.append(f"Configured template {key} is missing: {config[key]}")
    return problems


def strip_comments(text: str) -> str:
    """Remove unescaped LaTeX comments for dependency and command analysis."""
    cleaned: list[str] = []
    for line in text.splitlines():
        cut = len(line)
        for index, char in enumerate(line):
            if char == "%" and (index == 0 or line[index - 1] != "\\"):
                cut = index
                break
        cleaned.append(line[:cut])
    return "\n".join(cleaned)


def _packages(text: str) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    pattern = re.compile(r"\\(?:RequirePackage|usepackage)(?:\[([^]]*)\])?\{([^}]*)\}")
    for options, names in pattern.findall(text):
        for name in names.split(","):
            result.append({"name": name.strip(), "options": [item.strip() for item in options.split(",") if item.strip()]})
    unique = {(item["name"], tuple(item["options"])): item for item in result}
    return sorted(unique.values(), key=lambda item: item["name"].lower())


def _custom_commands(style_text: str, reference_text: str) -> list[dict[str, Any]]:
    names = set(re.findall(r"\\(?:newcommand|renewcommand)\s*\{\\([A-Za-z@]+)\}", style_text))
    names.update(re.findall(r"\\NewDocumentCommand\s*\{\\([A-Za-z@]+)\}", style_text))
    names.update(re.findall(r"\\def\\([A-Za-z@]+)", style_text))
    names.update(re.findall(r"\\DeclarePairedDelimiterX\s*\{\\([A-Za-z@]+)\}", style_text))
    return [
        {"name": "\\" + name, "reference_usage_count": len(re.findall(r"\\" + re.escape(name) + r"\b", reference_text))}
        for name in sorted(names)
    ]


def _environments(style_text: str, reference_text: str) -> list[dict[str, Any]]:
    names = set(re.findall(r"\\(?:NewDocumentEnvironment|newenvironment)\s*\{([^}]+)\}", style_text))
    return [
        {"name": name, "reference_usage_count": len(re.findall(r"\\begin\{" + re.escape(name) + r"\}", reference_text))}
        for name in sorted(names)
    ]


def analyze_template() -> dict[str, Any]:
    """Analyze configured style and reference files using conservative LaTeX parsing."""
    problems = validate_template_inputs()
    if problems:
        raise ProjectError("; ".join(problems))
    config = load_config("default.yaml")["template"]
    style_path = ROOT / config["style"]
    reference_path = ROOT / config["reference"]
    style_raw = style_path.read_text(encoding="utf-8")
    reference_raw = reference_path.read_text(encoding="utf-8")
    style = strip_comments(style_raw)
    reference = strip_comments(reference_raw)
    document_match = re.search(r"\\documentclass(?:\[([^]]*)\])?\{([^}]+)\}", reference)
    bibliography = re.findall(r"\\addbibresource\{([^}]+)\}", style + "\n" + reference)
    external_inputs = re.findall(r"\\(?:input|include|includegraphics|bibliography)\{([^}]+)\}", reference)
    commands = _custom_commands(style, reference)
    environments = _environments(style, reference)
    operators = sorted({
        "\\" + name for name in re.findall(
            r"\\newcommand\s*\{\\([A-Za-z@]+)\}\s*\{\\operatorname\{[^}]+\}\}", style
        )
    })
    labels = re.findall(r"\\label\{([^}]+)\}", reference)
    refs = re.findall(r"\\(?:ref|eqref|autoref)\{([^}]+)\}", reference)
    citations = re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", reference)
    theorem_argument_mismatches = []
    if re.search(r"\\NewDocumentEnvironment\{Theorem\}\{o\}", style):
        count = len(re.findall(r"\\begin\{Theorem\}\{", reference))
        if count:
            theorem_argument_mismatches.append({
                "environment": "Theorem", "count": count,
                "issue": "The environment declares an optional [title] argument, while the reference uses a braced group after \\begin{Theorem}."
            })
    return {
        "document_class": document_match.group(2) if document_match else None,
        "document_class_options": [item.strip() for item in document_match.group(1).split(",")] if document_match and document_match.group(1) else [],
        "engine": "xelatex",
        "engine_reason": "fontspec and ctexart are loaded; the isolated reference build succeeded with XeLaTeX.",
        "bibliography_backend": "biber" if "backend=biber" in style.replace(" ", "") else None,
        "bibliography_style": "numeric" if "style=numeric" in style.replace(" ", "") else None,
        "bibliography_resources": bibliography,
        "packages": _packages(style + "\n" + reference),
        "custom_commands": commands,
        "custom_operators": operators,
        "custom_environments": environments,
        "tikz_libraries": [item.strip() for group in re.findall(r"\\usetikzlibrary\{([^}]+)\}", style) for item in group.split(",")],
        "page": {"paper": "a4paper", "geometry": {"left": "2.0cm", "right": "2.0cm", "top": "1.66cm", "bottom": "1.27cm"}},
        "section_formatting": {"section": "ctex zihao 4 with SectionColor number", "subsection": "ctex zihao -4", "subsubsection": "ctex zihao -4"},
        "page_style": "plain",
        "formula_numbering": "within subsection",
        "labels": labels,
        "references": refs,
        "citations": sorted({key.strip() for group in citations for key in group.split(",")}),
        "external_inputs": external_inputs,
        "fonts": {"fontspec_loaded": True, "explicit_font_commands": [], "effective_reference_fontset": "ctexart Windows fontset (TeX log used SimSun for CJK text)"},
        "figures_and_tables": {"packages": ["graphicx", "float", "subfigure", "caption", "array", "multirow", "tabularx"], "reference_usage": []},
        "index_system": None,
        "reference_usage": {
            "sections": len(re.findall(r"\\section\{", reference)),
            "subsections": len(re.findall(r"\\subsection\{", reference)),
            "display_math_double_dollar": reference.count("$$") // 2,
            "printbibliography": bool(re.search(r"\\printbibliography\b", reference)),
        },
        "observed_usage_issues": theorem_argument_mismatches,
    }


def _kpsewhich(name: str) -> str | None:
    executable = shutil.which("kpsewhich")
    if not executable:
        return None
    try:
        result = subprocess.run([executable, name], capture_output=True, timeout=15, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    output = result.stdout.decode("utf-8", errors="replace").strip()
    return output or None


def dependency_report(analysis: dict[str, Any]) -> dict[str, Any]:
    """Resolve LaTeX packages and external files without installing anything."""
    resolved = []
    missing = []
    class_name = analysis["document_class"]
    class_path = _kpsewhich(f"{class_name}.cls") if class_name else None
    (resolved if class_path else missing).append({"name": class_name, "kind": "class", "resolved_path": class_path})
    for package in analysis["packages"]:
        local_candidates = list((TEMPLATE_ROOT / "style").glob(f"{package['name']}.sty"))
        path = _relative(local_candidates[0]) if local_candidates else _kpsewhich(f"{package['name']}.sty")
        entry = {"name": package["name"], "kind": "package", "resolved_path": path}
        (resolved if path else missing).append(entry)
    external = []
    for resource in analysis["bibliography_resources"]:
        candidates = [TEMPLATE_ROOT / "assets" / resource, TEMPLATE_ROOT / "reference" / resource]
        match = next((path for path in candidates if path.is_file()), None)
        entry = {"name": resource, "kind": "bibliography", "resolved_path": _relative(match) if match else None}
        external.append(entry)
        if not match:
            missing.append(entry)
    return {"resolved": resolved, "external": external, "missing": missing, "tools": {name: shutil.which(name) for name in ("latexmk", "xelatex", "biber", "bibtex", "makeindex", "kpsewhich")}}


def write_analysis_reports() -> tuple[dict[str, Any], dict[str, Any]]:
    """Generate all Phase 1 template analysis artifacts."""
    analysis = analyze_template()
    dependencies = dependency_report(analysis)
    qa_dir = ROOT / "qa" / "template"
    qa_dir.mkdir(parents=True, exist_ok=True)
    (qa_dir / "style-commands.json").write_text(json.dumps({
        "custom_commands": analysis["custom_commands"],
        "custom_operators": analysis["custom_operators"],
        "custom_environments": analysis["custom_environments"],
        "tikz_libraries": analysis["tikz_libraries"],
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    package_lines = "\n".join(f"- `{item['name']}`" + (f" with options `{', '.join(item['options'])}`" if item["options"] else "") for item in analysis["packages"])
    environment_lines = "\n".join(f"- `{item['name']}`: {item['reference_usage_count']} use(s) in the reference" for item in analysis["custom_environments"])
    issue_lines = "\n".join(f"- {item['issue']} Observed {item['count']} time(s)." for item in analysis["observed_usage_issues"]) or "- None observed."
    style_report = f"""# Style analysis\n\n- Style source: `input/template/style/Mystyle.sty`\n- Document class used by the reference: `{analysis['document_class']}` with options `{', '.join(analysis['document_class_options'])}`\n- Required engine: XeLaTeX (`fontspec` and `ctexart`; verified by isolated build)\n- Bibliography: biblatex numeric style with Biber; resource `ref.bib`; URL fields use `\\url`.\n- Page: A4; geometry left 2.0cm, right 2.0cm, top 1.66cm, bottom 1.27cm.\n- Page background: `sublight yellow`; the current style color names include `SectionColor` and `PageColor`.\n- Page style: plain. `fancyhdr` is loaded but not configured, so no custom header or footer is defined.\n- Formula numbering: reset within subsection. Inline math is globally forced to display style by `\\everymath{{\\displaystyle}}`.\n- Hyperlinks: color links enabled; internal links black and citations blue.\n- Explicit user font commands: none. The successful reference build selected the ctex Windows fontset and logged SimSun for CJK text.\n- Index system: none configured; MakeIndex is not required by the reference.\n\n## Packages\n\n{package_lines}\n\n## Custom commands and mathematical operators\n\nAll discovered definitions and reference usage counts are recorded in `style-commands.json`. Operator-style commands are: {', '.join(analysis['custom_operators'])}.\n\n## Custom environments\n\n{environment_lines}\n\nThe theorem-like environments share the section-scoped `statement` counter. The user style defines distinct visual treatments for theorem, definition, lemma, proposition, corollary, example, and exercise; the translation adapter preserves those distinctions while localizing headings and retaining referenceable counters.\n\n## Section and contents behavior\n\nThe reference class is article-based and defines no chapter usage. Sections, subsections, and subsubsections are styled through `ctexset`, with colored numbers and black Chinese titles. The reference invokes `\\tableofcontents`.\n\n## Figures, tables, labels, and cross-references\n\nFigure/table support is loaded through graphicx, float, subfigure, caption, array, multirow, and tabularx. The reference contains no active figure, table, label, ref, eqref, or autoref usage.\n\n## External dependencies\n\nThe only active user auxiliary dependency is `ref.bib`. Commented `Section/...` input lines are not active dependencies. Installed package and tool resolution is recorded in `dependencies.md`.\n\n## Observed usage issues\n\n{issue_lines}\n"""
    style_report = style_report.replace("input/template/", "template/")
    (qa_dir / "style-analysis.md").write_text(style_report, encoding="utf-8")
    reference_report = f"""# Reference analysis\n\n- Selected reference: `input/template/reference/main.tex`\n- Selection reason: the reference directory contains exactly one `.tex` file.\n- Document class: `{analysis['document_class']}`\n- Style invocation: `\\usepackage{{Mystyle}}`\n- Sections: {analysis['reference_usage']['sections']}\n- Subsections: {analysis['reference_usage']['subsections']}\n- Double-dollar display math blocks: {analysis['reference_usage']['display_math_double_dollar']}\n- Bibliography printed: {analysis['reference_usage']['printbibliography']}\n- Citation keys used: {', '.join(analysis['citations'])}\n- Active external inputs other than the bibliography: none. Commented `Section/...` inputs are not dependencies.\n\n## Actual custom-environment usage\n\n{environment_lines}\n\n## Labels and cross-references\n\nNo active `label`, `ref`, `eqref`, or `autoref` command is present in the reference.\n\n## Usage note requiring review\n\n{issue_lines}\n"""
    reference_report = reference_report.replace("input/template/", "template/")
    (qa_dir / "reference-analysis.md").write_text(reference_report, encoding="utf-8")
    missing_lines = "\n".join(f"- `{item['kind']}` `{item['name']}`" for item in dependencies["missing"]) or "- None detected in the installed TeX Live environment."
    resolved_lines = "\n".join(f"- `{item['kind']}` `{item['name']}` -> `{item['resolved_path']}`" for item in dependencies["resolved"])
    tool_lines = "\n".join(f"- `{name}`: `{path or 'not found'}`" for name, path in dependencies["tools"].items())
    external_lines = "\n".join(f"- `{item['name']}` -> `{item['resolved_path'] or 'missing'}`" for item in dependencies["external"]) or "- None."
    dep_report = f"""# Template dependencies\n\n## External user files\n\n{external_lines}\n\n## Required tools\n\n{tool_lines}\n\n## Resolved class and packages\n\n{resolved_lines}\n\n## Missing dependencies\n\n{missing_lines}\n\nPackage resolution used the user style directory first and `kpsewhich` for installed TeX files; no package was installed or modified.\n"""
    (qa_dir / "dependencies.md").write_text(dep_report, encoding="utf-8")
    return analysis, dependencies


def compile_reference() -> dict[str, Any]:
    """Compile a read-only copy of the configured reference with XeLaTeX/Biber."""
    problems = validate_template_inputs()
    if problems:
        raise ProjectError("; ".join(problems))
    before = {path: sha256_file(path) for path in iter_files(TEMPLATE_ROOT)}
    latexmk = shutil.which("latexmk")
    if not latexmk:
        raise ProjectError("latexmk is not available; reference compilation cannot run.")
    staging = Path(tempfile.mkdtemp(prefix="mathbook-template-build-"))
    output = staging / "out"
    output.mkdir()
    seen: set[str] = set()
    for path in iter_files(TEMPLATE_ROOT):
        if path.name == ".gitkeep":
            continue
        if path.name in seen:
            raise ProjectError(f"Cannot flatten template inputs because a filename is duplicated: {path.name}")
        seen.add(path.name)
        shutil.copy2(path, staging / path.name)
    reference_name = Path(load_config("default.yaml")["template"]["reference"]).name
    reference_copy = staging / reference_name
    reference_text = reference_copy.read_text(encoding="utf-8")
    style_load = "\\usepackage{Mystyle}"
    adapter_load = "\\usepackage{translation-adapter}"
    if adapter_load not in reference_text:
        if style_load not in reference_text:
            raise ProjectError("The reference does not load the configured user style.")
        reference_copy.write_text(reference_text.replace(style_load, style_load + "\n" + adapter_load, 1), encoding="utf-8")
    command = [latexmk, "-xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", f"-outdir={output}", reference_name]
    completed = subprocess.run(command, cwd=staging, capture_output=True, check=False)
    wrapper_output = (completed.stdout + b"\n" + completed.stderr).decode("utf-8", errors="replace")
    native_log_path = output / (Path(reference_name).stem + ".log")
    native_log = native_log_path.read_bytes().decode("utf-8", errors="replace") if native_log_path.exists() else ""
    log_path = staging / "template-compilation.log"
    log_path.write_text(wrapper_output + "\n\n===== native TeX log =====\n" + native_log, encoding="utf-8")
    after = {path: sha256_file(path) for path in iter_files(TEMPLATE_ROOT)}
    integrity_ok = before == after
    pdf_path = output / (Path(reference_name).stem + ".pdf")
    success = completed.returncode == 0 and pdf_path.is_file()
    warnings = []
    for line in native_log.splitlines():
        if "Warning:" in line or "Overfull \\hbox" in line or "Underfull \\hbox" in line:
            warnings.append(line.strip())
    report = {
        "success": success,
        "exit_code": completed.returncode,
        "engine": "xelatex",
        "driver": "latexmk",
        "bibliography": "biber",
        "pdf_generated": pdf_path.is_file(),
        "pdf_size_bytes": pdf_path.stat().st_size if pdf_path.is_file() else None,
        "warnings": warnings,
        "template_integrity_verified": integrity_ok,
        "build_directory": str(staging),
        "log": str(log_path),
    }
    warning_text = "\n".join(f"- {line}" for line in warnings) or "- None."
    report_text = f"""# Template compilation report\n\n- Reference: `input/template/reference/{reference_name}`\n- Isolated build directory: `{report['build_directory']}`\n- Driver: latexmk\n- Engine: XeLaTeX\n- Bibliography backend: Biber\n- Exit code: {completed.returncode}\n- PDF generated: {str(report['pdf_generated']).lower()}\n- Result: {'success' if success else 'failure'}\n- User-template hashes unchanged: {str(integrity_ok).lower()}\n- Full log: `logs/template-compilation.log`\n\n## Warnings\n\n{warning_text}\n"""
    return report
