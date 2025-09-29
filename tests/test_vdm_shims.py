from __future__ import annotations

import inspect

import pytest

import vdm.memory_steering as ms
import vdm.void_dynamics as vd


def _public_memory():
    import importlib.util
    from pathlib import Path

    path = Path(__file__).resolve().parents[1] / "code" / "memory_steering" / "memory_steering.py"
    spec = importlib.util.spec_from_file_location("vdm_public_memory", path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    spec.loader.exec_module(module)
    return module


def _public_void_placeholder():
    import importlib

    return importlib.import_module("vdm._placeholders.void_dynamics_placeholder")


@pytest.mark.parametrize("name", [
    "build_graph_laplacian",
    "collect_junction_choices",
    "compute_dimensionless_groups",
    "update_memory",
    "y_junction_adjacency",
])
def test_memory_signatures_match_public_reference(name: str):
    public = _public_memory()
    shim_obj = getattr(ms, name)
    public_obj = getattr(public, name)
    assert inspect.signature(shim_obj) == inspect.signature(public_obj)


def test_memory_placeholder_flag():
    assert not ms.HAS_CLASSIFIED_IMPL
    assert ms.MEMORY_SOURCE.startswith("placeholder")


@pytest.mark.parametrize("name", [
    "universal_void_dynamics",
])
def test_void_signature_matches_placeholder(name: str):
    placeholder = _public_void_placeholder()
    shim_obj = getattr(vd, name)
    placeholder_obj = getattr(placeholder, name)
    assert inspect.signature(shim_obj) == inspect.signature(placeholder_obj)


def test_void_modulation_placeholder_metadata():
    placeholder = _public_void_placeholder()
    inst = placeholder.VoidDebtModulation()
    shim_inst = vd.VoidDebtModulation()
    assert shim_inst.get_all_domain_modulations() == inst.get_all_domain_modulations()
    assert shim_inst.validate_modulation_consistency() == inst.validate_modulation_consistency()
    assert vd.HAS_CLASSIFIED_IMPL is False
    assert vd.VOID_SOURCE.startswith("placeholder")
