from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_public_reference():
    root = Path(__file__).resolve().parents[2]
    target = root / "code" / "memory_steering" / "memory_steering.py"
    spec = importlib.util.spec_from_file_location("vdm_public_memory_steering", target)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load public memory steering placeholder from {target}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_PUBLIC = _load_public_reference()

build_graph_laplacian = getattr(_PUBLIC, "build_graph_laplacian")
collect_junction_choices = getattr(_PUBLIC, "collect_junction_choices")
compute_dimensionless_groups = getattr(_PUBLIC, "compute_dimensionless_groups")
sample_next_neighbor = getattr(_PUBLIC, "sample_next_neighbor")
sample_next_neighbor_heading = getattr(_PUBLIC, "sample_next_neighbor_heading")
transition_probs = getattr(_PUBLIC, "transition_probs")
transition_probs_temp = getattr(_PUBLIC, "transition_probs_temp")
update_memory = getattr(_PUBLIC, "update_memory")
y_junction_adjacency = getattr(_PUBLIC, "y_junction_adjacency")

CLASSIFIED_MESSAGE = (
    "Attempted to import classified memory-steering primitives. Public builds use the "
    "documented reference implementation—request private access for the augmented kernel."
)
HAS_CLASSIFIED_IMPL = False
MEMORY_SOURCE = "placeholder:code.memory_steering.memory_steering"

__all__ = [
    "CLASSIFIED_MESSAGE",
    "HAS_CLASSIFIED_IMPL",
    "MEMORY_SOURCE",
    "build_graph_laplacian",
    "collect_junction_choices",
    "compute_dimensionless_groups",
    "sample_next_neighbor",
    "sample_next_neighbor_heading",
    "transition_probs",
    "transition_probs_temp",
    "update_memory",
    "y_junction_adjacency",
]
