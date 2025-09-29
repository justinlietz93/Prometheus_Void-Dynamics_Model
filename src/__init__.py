"""Prometheus VDM repository modules (loaded under the ``src`` package namespace)."""

from __future__ import annotations

import sys
from pathlib import Path

__all__: list[str] = []

_pkg_path = Path(__file__).resolve().parent
_pkg_str = str(_pkg_path)
if _pkg_str not in sys.path:
	sys.path.insert(0, _pkg_str)

# Ensure legacy ``import code`` continues to resolve to this package.
sys.modules.setdefault("code", sys.modules[__name__])
