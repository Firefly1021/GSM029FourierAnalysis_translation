"""Structured QA issue recording."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


PUNCTUATION_REPLACEMENTS = {
    "……": "...",
    "，": ",",
    "。": ".",
    "：": ":",
    "；": ";",
    "？": "?",
    "！": "!",
    "（": "(",
    "）": ")",
    "【": "[",
    "】": "]",
}

_CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
_PROTECTED_PATTERNS = (
    re.compile(r"(?m)(?<!\\)%.*$"),
    re.compile(r"\\begin\{(?:equation\*?|align\*?|gather\*?|multline\*?|displaymath|math|cases|aligned)\}.*?\\end\{(?:equation\*?|align\*?|gather\*?|multline\*?|displaymath|math|cases|aligned)\}", re.DOTALL),
    re.compile(r"\\begin\{(?:verbatim|Verbatim|lstlisting|minted)\}.*?\\end\{(?:verbatim|Verbatim|lstlisting|minted)\}", re.DOTALL),
    re.compile(r"\\\[.*?\\\]", re.DOTALL),
    re.compile(r"\\\(.*?\\\)", re.DOTALL),
    re.compile(r"(?<!\\)\$\$.*?(?<!\\)\$\$", re.DOTALL),
    re.compile(r"(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$", re.DOTALL),
    re.compile(r"\\(?:label|ref|eqref|cref|Cref|autoref|pageref|cite|parencite|textcite|url|path|input|include|includegraphics|addbibresource)\s*(?:\[[^\]]*\]\s*)?\{[^{}]*\}"),
)


@dataclass(frozen=True)
class PunctuationViolation:
    line: int
    column: int
    character: str
    replacement: str


def _protected_mask(text: str) -> list[bool]:
    """Mark math, code, comments, and reference-like command arguments."""
    mask = [False] * len(text)
    for pattern in _PROTECTED_PATTERNS:
        for match in pattern.finditer(text):
            for index in range(match.start(), match.end()):
                mask[index] = True
    return mask


def _has_cjk_context(text: str, mask: list[bool], start: int, end: int) -> bool:
    left = max(0, start - 48)
    right = min(len(text), end + 48)
    context = "".join(character for index, character in enumerate(text[left:right], left) if not mask[index])
    return bool(_CJK.search(context))


def find_chinese_prose_punctuation(text: str) -> list[PunctuationViolation]:
    """Find forbidden full-width punctuation in unprotected Chinese prose."""
    mask = _protected_mask(text)
    violations: list[PunctuationViolation] = []
    pattern = re.compile("|".join(re.escape(item) for item in sorted(PUNCTUATION_REPLACEMENTS, key=len, reverse=True)))
    for match in pattern.finditer(text):
        if any(mask[index] for index in range(match.start(), match.end())):
            continue
        if not _has_cjk_context(text, mask, match.start(), match.end()):
            continue
        line = text.count("\n", 0, match.start()) + 1
        line_start = text.rfind("\n", 0, match.start()) + 1
        violations.append(PunctuationViolation(line, match.start() - line_start + 1, match.group(), PUNCTUATION_REPLACEMENTS[match.group()]))
    return violations


def normalize_chinese_prose_punctuation(text: str) -> str:
    """Normalize only forbidden punctuation found in unprotected Chinese prose."""
    violations = find_chinese_prose_punctuation(text)
    if not violations:
        return text
    by_position = {(item.line, item.column): item for item in violations}
    lines = text.splitlines(keepends=True)
    for line_number, line in enumerate(lines, 1):
        items = sorted((item for key, item in by_position.items() if key[0] == line_number), key=lambda item: item.column, reverse=True)
        for item in items:
            start = item.column - 1
            line = line[:start] + item.replacement + line[start + len(item.character):]
        lines[line_number - 1] = line
    return "".join(lines)


@dataclass(frozen=True)
class QAIssue:
    id: str
    category: str
    severity: str
    message: str
    confidence: float
    review_status: str = "not-reviewed"
    source_file: str | None = None
    source_location: dict[str, Any] | None = None
    details: dict[str, Any] = field(default_factory=dict)


def append_issue(path: Path, issue: QAIssue) -> None:
    """Append one JSON object without replacing existing review data."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(asdict(issue), ensure_ascii=False) + "\n")
