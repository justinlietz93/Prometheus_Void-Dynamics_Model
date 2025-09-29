from __future__ import annotations

import ast
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CODE_ROOT = PROJECT_ROOT / "code"

# Modules that must never be imported directly from the public tree.
BANNED_IMPORT_PREFIXES = {
    "VDM_Void_Equations",
    "VDM_Void_Debt_Modulation",
    "Void_Debt_Modulation",
    "VDM_rt",
    "VDM_Demo_original",
    "secrets",
}


def _iter_python_files(root: Path) -> list[Path]:
    return [p for p in root.rglob("*.py") if p.is_file()]


def _find_forbidden_imports(path: Path) -> list[tuple[int, str]]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    violations: list[tuple[int, str]] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                if any(name == banned or name.startswith(f"{banned}.") for banned in BANNED_IMPORT_PREFIXES):
                    violations.append((node.lineno, name))
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if any(module == banned or module.startswith(f"{banned}.") for banned in BANNED_IMPORT_PREFIXES):
                violations.append((node.lineno, module))
    return violations


def test_forbidden_imports_absent():
    py_files = _iter_python_files(CODE_ROOT)
    bad: dict[str, list[tuple[int, str]]] = {}
    for path in py_files:
        rel = path.relative_to(PROJECT_ROOT)
        violations = _find_forbidden_imports(path)
        if violations:
            bad[str(rel)] = violations
    if bad:
        details = "\n".join(
            f"{fname}: {violations}" for fname, violations in sorted(bad.items())
        )
        pytest.fail(f"Forbidden classified imports detected:\n{details}")
