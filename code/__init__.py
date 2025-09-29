"""Prometheus VDM repository modules (shadowing the stdlib ``code`` module)."""

from __future__ import annotations

import sys
from pathlib import Path

__all__: list[str] = []

_pkg_path = Path(__file__).resolve().parent
_pkg_str = str(_pkg_path)
if _pkg_str not in sys.path:
	sys.path.insert(0, _pkg_str)

# Ensure ``import code`` resolves to this package rather than the stdlib helper module.
sys.modules.setdefault(__name__, sys.modules[__name__])
