from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - for type checkers only
    import numpy as np

CLASSIFIED_MESSAGE = (
    "Attempted to import classified void-dynamics code. Public builds ship a deterministic "
    "placeholder—request private access for production-grade behavior."
)
HAS_CLASSIFIED_IMPL = False
VOID_SOURCE = "placeholder:vdm._placeholders.void_dynamics_placeholder"


def universal_void_dynamics(
    W: Any,
    t: int,
    *,
    domain_modulation: float = 1.0,
    use_time_dynamics: bool = True,
) -> Any:
    """Return a zero update, preserving the input shape/dtype."""
    try:
        import numpy as _np  # type: ignore
    except ModuleNotFoundError:  # pragma: no cover - numpy should exist for sims
        if hasattr(W, "__iter__") and not isinstance(W, (str, bytes)):
            return type(W)(0 for _ in W)  # type: ignore[call-arg]
        return 0

    arr = _np.asarray(W)
    return _np.zeros_like(arr, dtype=arr.dtype)


@dataclass(slots=True)
class _PlaceholderDomain:
    name: str
    domain_modulation: float
    description: str

    def as_dict(self) -> Dict[str, float | str]:
        return {
            "domain": self.name,
            "domain_modulation": float(self.domain_modulation),
            "description": self.description,
            "source": VOID_SOURCE,
        }


class VoidDebtModulation:
    """Public, deterministic stand-in for the classified domain modulation."""

    _DOMAINS = (
        _PlaceholderDomain("standard_model", 1.0, "Unity stabilization (placeholder)"),
        _PlaceholderDomain("high_shear", 0.85, "Mild damping for shear-driven flows"),
        _PlaceholderDomain("lid_cavity", 0.9, "Tuned for lid-driven cavity benchmark"),
    )

    def __init__(self) -> None:
        self._domain_map = {d.name: d for d in self._DOMAINS}

    def get_universal_domain_modulation(
        self,
        physics_domain: str,
        target_sparsity_pct: float | None = None,
    ) -> Dict[str, float | str | None]:
        domain = self._domain_map.get(physics_domain, self._domain_map["standard_model"])
        rec = domain.as_dict()
        rec["target_sparsity_pct"] = target_sparsity_pct
        return rec

    def get_all_domain_modulations(self) -> Dict[str, Dict[str, float | str | None]]:
        return {name: dom.as_dict() for name, dom in self._domain_map.items()}

    def print_modulation_table(self) -> None:
        for dom in self._DOMAINS:
            rec = dom.as_dict()
            print(f"{rec['domain']:<16} modulation={rec['domain_modulation']:.3f} source={rec['source']}")

    def validate_modulation_consistency(self) -> bool:
        for dom in self._DOMAINS:
            if dom.domain_modulation <= 0:
                return False
        return True


__all__ = [
    "CLASSIFIED_MESSAGE",
    "HAS_CLASSIFIED_IMPL",
    "VOID_SOURCE",
    "VoidDebtModulation",
    "universal_void_dynamics",
]
