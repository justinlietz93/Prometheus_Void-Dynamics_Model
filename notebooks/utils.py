"""Utility helpers shared by domain notebooks.

These functions keep the repository root on ``sys.path`` so that the
``code/<domain>/`` packages can be imported directly from notebooks, and they
provide small quality-of-life helpers for allocating artifact paths and
summarising numpy arrays.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, Mapping


REPO_ROOT = Path(__file__).resolve().parents[1]
CODE_ROOT = REPO_ROOT / "code"


def ensure_repo_path() -> Path:
	"""Ensure the repo (and ``code/``) directories are importable.

	Returns the repository root so callers can build absolute Paths when they
	want to reference files on disk.
	"""

	for path in (REPO_ROOT, CODE_ROOT):
		path_str = str(path)
		if path_str not in sys.path:
			sys.path.insert(0, path_str)
	_bootstrap_local_packages()
	return REPO_ROOT


def _bootstrap_local_packages() -> None:
	"""Load repository packages that shadow stdlib names (e.g. ``code``)."""

	def _load_package(name: str, package_path: Path) -> None:
		init_file = package_path / "__init__.py"
		if not init_file.exists():
			return
		existing = sys.modules.get(name)
		if existing is not None and getattr(existing, "__file__", None) == str(init_file):
			return
		spec = importlib.util.spec_from_file_location(
			name,
			init_file,
			submodule_search_locations=[str(package_path)],
		)
		if spec is None or spec.loader is None:
			return
		module = importlib.util.module_from_spec(spec)
		sys.modules[name] = module
		spec.loader.exec_module(module)

	_load_package("code", CODE_ROOT)


def repo_path(*parts: str) -> Path:
	"""Join ``parts`` onto the repository root as a ``Path``."""

	return ensure_repo_path().joinpath(*parts)


def allocate_artifacts(domain: str, slug: str, failed: bool = False) -> Dict[str, Path]:
	"""Reserve figure/log paths for a domain-specific run.

	The helper mirrors the behaviour used by the production scripts so notebooks
	save artifacts into the same ``figures/`` and ``logs/`` directories.
	"""

	ensure_repo_path()
	from code.common import io_paths  # imported lazily to avoid notebook startup cost

	figure_path = io_paths.figure_path(domain, slug, failed=failed)
	log_path = io_paths.log_path(domain, slug, failed=failed)
	return {"figure": figure_path, "log": log_path}


def preview_json(data: Mapping[str, Any]) -> str:
	"""Render a mapping as pretty-printed JSON for quick inspection."""

	return json.dumps(data, indent=2, sort_keys=True, default=str)


def summarize_array(arr: Any) -> Dict[str, Any]:
	"""Return basic statistics for an array-like object."""

	import numpy as np

	np_arr = np.asarray(arr)
	if np_arr.size == 0:
		return {"shape": list(np_arr.shape), "size": 0}
	return {
		"shape": list(np_arr.shape),
		"size": int(np_arr.size),
		"min": float(np_arr.min()),
		"max": float(np_arr.max()),
		"mean": float(np_arr.mean()),
		"std": float(np_arr.std()),
	}


def timestamp_slug(prefix: str) -> str:
	"""Generate a timestamped slug (UTC) suitable for artifact filenames."""

	from datetime import datetime, timezone

	return f"{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}_{prefix}"


__all__ = [
	"allocate_artifacts",
	"ensure_repo_path",
	"preview_json",
	"repo_path",
	"summarize_array",
	"timestamp_slug",
]
