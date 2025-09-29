from __future__ import annotations

import importlib
import importlib.util
import logging
import os
from pathlib import Path
from types import ModuleType
from typing import Any, Tuple

CLASSIFIED_MESSAGE = (
    "Attempted to import classified memory-steering primitives, ask the author for access "
    "to run the full experiments. Public builds fall back to the documented reference implementation."
)
_PLACEHOLDER_MODULE = "vdm._placeholders.memory_steering_placeholder"
_LOGGER = logging.getLogger(__name__)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_module_from_path(path: Path, qualname: str) -> ModuleType | None:
    spec = importlib.util.spec_from_file_location(qualname, path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - defensive
        _LOGGER.debug("Failed to load classified memory module from %s: %s", path, exc)
        return None
    return module


def _load_impl() -> Tuple[ModuleType, str, bool]:
    plugin = os.environ.get("VDM_CLASSIFIED_PLUGIN")
    if plugin:
        try:
            module = importlib.import_module(f"{plugin}.memory_steering")
            source = getattr(module, "MEMORY_SOURCE", f"plugin:{plugin}")
            return module, source, True
        except Exception as exc:  # pragma: no cover
            _LOGGER.debug("VDM_CLASSIFIED_PLUGIN memory load failed for %s: %s", plugin, exc)

    root = _repo_root()
    candidates = [
        root / "secrets" / "VDM_rt" / "core" / "memory_steering.py",
        root / "secrets" / "memory_steering" / "memory_steering.py",
    ]

    for path in candidates:
        if not path.exists():
            continue
        module = _load_module_from_path(path, f"vdm_classified_memory_{path.stem}")
        if module is None:
            continue
        source = f"file:{path.relative_to(root)}"
        return module, source, True

    placeholder = importlib.import_module(_PLACEHOLDER_MODULE)
    source = getattr(placeholder, "MEMORY_SOURCE", "placeholder")
    has_impl = getattr(placeholder, "HAS_CLASSIFIED_IMPL", False)
    return placeholder, source, has_impl


_IMPL, MEMORY_SOURCE, HAS_CLASSIFIED_IMPL = _load_impl()

build_graph_laplacian = getattr(_IMPL, "build_graph_laplacian")
collect_junction_choices = getattr(_IMPL, "collect_junction_choices")
compute_dimensionless_groups = getattr(_IMPL, "compute_dimensionless_groups")
sample_next_neighbor = getattr(_IMPL, "sample_next_neighbor")
sample_next_neighbor_heading = getattr(_IMPL, "sample_next_neighbor_heading")
transition_probs = getattr(_IMPL, "transition_probs")
transition_probs_temp = getattr(_IMPL, "transition_probs_temp")
update_memory = getattr(_IMPL, "update_memory")
y_junction_adjacency = getattr(_IMPL, "y_junction_adjacency")


def ensure_classified_memory_kernel() -> None:
    if not HAS_CLASSIFIED_IMPL:
        raise ImportError(CLASSIFIED_MESSAGE)


__all__ = [
    "CLASSIFIED_MESSAGE",
    "HAS_CLASSIFIED_IMPL",
    "MEMORY_SOURCE",
    "build_graph_laplacian",
    "collect_junction_choices",
    "compute_dimensionless_groups",
    "ensure_classified_memory_kernel",
    "sample_next_neighbor",
    "sample_next_neighbor_heading",
    "transition_probs",
    "transition_probs_temp",
    "update_memory",
    "y_junction_adjacency",
]
