"""Book-level compilation and deterministic LaTeX QA."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

from .project import BookPaths, ProjectError, directory_manifest_hash, sha256_file
from .qa import find_chinese_prose_punctuation


LABEL = re.compile(r"\\label\{([^}]+)\}")
REFERENCE = re.compile(r"\\(eqref|ref|cref)\{([^}]+)\}")
TRANSLATED_ENVIRONMENT_REFERENCE = re.compile(r"(定理|定义|引理|命题|推论|证明|例|注|习题)\s*~?\s*\\(?:ref|cref)\{")


def canonical_tex_files(book: BookPaths) -> list[Path]:
    files = [book.main_tex]
    for name in ("frontmatter.tex", "backmatter.tex"):
        path = book.root / "tex" / name
        if path.exists():
            files.append(path)
    files.extend(sorted((book.root / "tex" / "chapters").rglob("*.tex")))
    return [path for path in files if path.is_file()]


def latex_qa(book: BookPaths) -> dict[str, object]:
    files = canonical_tex_files(book)
    labels: list[str] = []
    references: list[tuple[str, str]] = []
    punctuation = []
    translated_environment_references = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        labels.extend(LABEL.findall(text))
        references.extend(REFERENCE.findall(text))
        punctuation.extend(
            {"file": path.relative_to(book.root).as_posix(), "line": item.line, "column": item.column, "character": item.character}
            for item in find_chinese_prose_punctuation(text)
        )
        for line_number, line in enumerate(text.splitlines(), 1):
            for match in TRANSLATED_ENVIRONMENT_REFERENCE.finditer(line):
                translated_environment_references.append({
                    "file": path.relative_to(book.root).as_posix(),
                    "line": line_number,
                    "environment_name": match.group(1),
                })
    counts = Counter(labels)
    duplicates = sorted(label for label, count in counts.items() if count > 1)
    undefined = sorted({label for _, label in references} - set(labels))
    wrong_commands = sorted({label for command, label in references if (label.startswith("eq:")) != (command == "eqref")})
    return {
        "files": len(files),
        "labels": len(labels),
        "duplicate_labels": duplicates,
        "references": len(references),
        "undefined_references": undefined,
        "wrong_reference_commands": wrong_commands,
        "translated_environment_references": translated_environment_references,
        "punctuation_violations": punctuation,
        "passed": not any((duplicates, undefined, wrong_commands, translated_environment_references, punctuation)),
    }


def compile_book(book: BookPaths, *, output_directory: Path | None = None) -> dict[str, object]:
    """Compile a book from a fresh directory without modifying shared template files."""
    config = book.load_config()
    expected_template = config.get("template_manifest_hash")
    actual_template = directory_manifest_hash(book.project.template)
    if expected_template and expected_template != actual_template:
        raise ProjectError(
            "The book is pinned to a different template manifest. Compile with its recorded template version or review the upgrade explicitly."
        )
    if not book.main_tex.is_file():
        raise ProjectError(f"Book main TeX file is missing: {book.main_tex}")
    latexmk = shutil.which("latexmk")
    if not latexmk:
        raise ProjectError("latexmk is not available.")
    if output_directory is None:
        parent = book.root / "workspace" / "temporary"
        parent.mkdir(parents=True, exist_ok=True)
        output_directory = Path(tempfile.mkdtemp(prefix="clean-build-", dir=parent))
    else:
        output_directory = output_directory.resolve()
        if output_directory.exists() and any(output_directory.iterdir()):
            raise ProjectError(f"Build directory is not clean: {output_directory}")
        output_directory.mkdir(parents=True, exist_ok=True)
    template = book.project.template
    search_paths = [template / "style", template / "adapter", template / "assets", book.root / "tex"]
    environment = os.environ.copy()
    environment["TEXINPUTS"] = os.pathsep.join(str(path) for path in search_paths) + os.pathsep + os.pathsep
    command = [
        latexmk, "-norc", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", f"-outdir={output_directory}", str(book.main_tex),
    ]
    completed = subprocess.run(command, cwd=book.root / "tex", env=environment, capture_output=True, check=False)
    wrapper_log = (completed.stdout + b"\n" + completed.stderr).decode("utf-8", errors="replace")
    native_log_path = output_directory / "main.log"
    native_log = native_log_path.read_text(encoding="utf-8", errors="replace") if native_log_path.exists() else ""
    log_path = book.root / "logs" / "latest-compilation.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(wrapper_log + "\n===== native TeX log =====\n" + native_log, encoding="utf-8")
    pdf = output_directory / "main.pdf"
    qa = latex_qa(book)
    report = {
        "success": completed.returncode == 0 and pdf.is_file() and qa["passed"],
        "exit_code": completed.returncode,
        "build_directory": str(output_directory),
        "pdf": str(pdf) if pdf.exists() else None,
        "pdf_bytes": pdf.stat().st_size if pdf.exists() else None,
        "pdf_sha256": sha256_file(pdf) if pdf.exists() else None,
        "undefined_reference_warnings": len(re.findall(r"undefined references?", native_log, re.I)),
        "multiply_defined_warnings": len(re.findall(r"multiply defined|multiply-defined", native_log, re.I)),
        "latex_errors": len(re.findall(r"^!", native_log, re.M)),
        "latex_qa": qa,
        "template_manifest_hash": actual_template,
        "log": str(log_path),
    }
    report_path = book.root / "qa" / "latest-compilation.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report
