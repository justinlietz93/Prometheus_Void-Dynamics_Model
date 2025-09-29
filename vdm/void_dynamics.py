from __future__ import annotations

import importlib
import importlib.util
import logging
import os
from pathlib import Path
from types import ModuleType
from typing import Any, Tuple

CLASSIFIED_MESSAGE = (
    "Attempted to import classified void-dynamics code, ask the author for access "
    "to run the full simulation. Public builds use a deterministic placeholder."
)
_PLACEHOLDER_MODULE = "vdm._placeholders.void_dynamics_placeholder"
_LOGGER = logging.getLogger(__name__)


def _load_module_from_path(path: Path, qualname: str) -> ModuleType | None:
    spec = importlib.util.spec_from_file_location(qualname, path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - defensive
        _LOGGER.debug("Failed to load classified module from %s: %s", path, exc)
        return None
    return module


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_impl() -> Tuple[ModuleType, str, bool]:
    plugin = os.environ.get("VDM_CLASSIFIED_PLUGIN")
    if plugin:
        try:
            module = importlib.import_module(f"{plugin}.void_dynamics")
            return module, f"plugin:{plugin}", True
        except Exception as exc:  # pragma: no cover - optional dependency
            _LOGGER.debug("VDM_CLASSIFIED_PLUGIN failed for %s: %s", plugin, exc)

    root = _repo_root()
    candidates = [
        root / "secrets" / "FUM_Void_Equations.py",
        root / "secrets" / "VDM_Void_Equations.py",
        root / "secrets" / "Void_Equations.py",
        root / "secrets" / "FUM_Void_Debt_Modulation.py",
        root / "secrets" / "VDM_Void_Debt_Modulation.py",
        root / "secrets" / "Void_Debt_Modulation.py",
        root / "derivation" / "code" / "VDM_Void_Equations.py",
        root / "derivation" / "code" / "VDM_Void_Debt_Modulation.py",
        root / "derivation" / "memory_steering" / "VDM_Void_Equations.py",
        root / "derivation" / "memory_steering" / "VDM_Void_Debt_Modulation.py",
        root / "VDM_Void_Equations.py",
        root / "VDM_Void_Debt_Modulation.py",
    ]

    eq_module: ModuleType | None = None
    mod_module: ModuleType | None = None
    eq_source: str | None = None
    mod_source: str | None = None

    for path in candidates:
        if not path.exists():
            continue
        module = _load_module_from_path(path, f"vdm_classified_{path.stem}")
        if module is None:
            continue
        if eq_module is None and hasattr(module, "universal_void_dynamics"):
            eq_module = module
            eq_source = f"file:{path.relative_to(root)}"
        if mod_module is None and hasattr(module, "VoidDebtModulation"):
            mod_module = module
            mod_source = mod_source or f"file:{path.relative_to(root)}"
        if eq_module and mod_module:
            break

    if eq_module and mod_module:
        bridge = type("_Bridge", (), {})()
        setattr(bridge, "universal_void_dynamics", getattr(eq_module, "universal_void_dynamics"))
        setattr(bridge, "VoidDebtModulation", getattr(mod_module, "VoidDebtModulation"))
        source = eq_source or mod_source or "file:secrets"
        return bridge, source, True

    placeholder = importlib.import_module(_PLACEHOLDER_MODULE)
    source = getattr(placeholder, "VOID_SOURCE", "placeholder")
    return placeholder, source, getattr(placeholder, "HAS_CLASSIFIED_IMPL", False)


_IMPL, VOID_SOURCE, HAS_CLASSIFIED_IMPL = _load_impl()

universal_void_dynamics = getattr(_IMPL, "universal_void_dynamics")
VoidDebtModulation = getattr(_IMPL, "VoidDebtModulation")


def ensure_classified_void_kernel() -> None:
    if not HAS_CLASSIFIED_IMPL:
        raise ImportError(CLASSIFIED_MESSAGE)


__all__ = [
    "CLASSIFIED_MESSAGE",
    "HAS_CLASSIFIED_IMPL",
    "VOID_SOURCE",
    "VoidDebtModulation",
    "ensure_classified_void_kernel",
    "universal_void_dynamics",
]
