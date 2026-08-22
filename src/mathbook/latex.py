"""Template-aware LaTeX output validation interfaces."""

from __future__ import annotations

import re
from pathlib import Path


ENVIRONMENT_DEFINITION = re.compile(
    r"\\(?:NewDocumentEnvironment|RenewDocumentEnvironment|newenvironment|renewenvironment)\s*\{([^}]+)\}"
)


def defined_environments(text: str) -> set[str]:
    return set(ENVIRONMENT_DEFINITION.findall(text))


def adapter_environment_conflicts(style_path: Path, adapter_path: Path) -> set[str]:
    """Return user environments redefined by the adapter."""
    style = style_path.read_text(encoding="utf-8")
    adapter = adapter_path.read_text(encoding="utf-8")
    return defined_environments(style) & defined_environments(adapter)


def emit_environment(environment: str, body: str, title: str | None = None) -> str:
    """Emit an existing template environment without changing its definition."""
    opening = f"\\begin{{{environment}}}" + (f"{{{title}}}" if title else "")
    return f"{opening}\n{body}\n\\end{{{environment}}}\n"
