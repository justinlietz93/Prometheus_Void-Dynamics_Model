# src/common/io_paths.py
'''
Copyright © 2025 Justin K. Lietz, Neuroca, Inc. All Rights Reserved.

This research is protected under a dual-license to foster open academic
research while ensuring commercial applications are aligned with the project's ethical principles. Commercial use requires written permission from the author..
See LICENSE file for full terms.

# Example usage inside a physics script:

from pathlib import Path
import matplotlib.pyplot as plt
from common.io_paths import figure_path, log_path, write_log

domain, slug = "fluid_dynamics", "corner_test_r_c_scan"

# ... run simulation, compute metrics -> 'metrics' dict

# Save figure
fig_path = figure_path(domain, slug, failed=False)
plt.savefig(fig_path, dpi=160, bbox_inches="tight")

# Save log
log = {
    "timestamp": __import__("datetime").datetime.now().isoformat(),
    "git_hash": "YOUR_GIT_HASH_HERE",
    "seed": 1234,
    "domain": domain,
    "slug": slug,
    "params": {"H":1.0, "nu":1e-3, "...":"..."},
    "metrics": metrics,
    "status": "success"
}
write_log(log_path(domain, slug, failed=False), log)

# In Markdown (relative to the repository root):
# ![Corner test r_c scan](figures/fluid_dynamics/20250823_corner_test_r_c_scan.png)
# [Run log](logs/fluid_dynamics/20250823_corner_test_r_c_scan.json)

'''
from pathlib import Path
from datetime import datetime
import json

REPO_ROOT = Path(__file__).resolve().parents[2]
FIGURES_ROOT = REPO_ROOT / "figures"
LOGS_ROOT = REPO_ROOT / "logs"

def _ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def ensure_dir(p: Path) -> Path:
    p.mkdir(parents=True, exist_ok=True)
    return p

def figure_path(domain: str, slug: str, failed: bool=False) -> Path:
    base = FIGURES_ROOT / domain / ("failed_runs" if failed else "")
    return ensure_dir(base) / f"{_ts()}_{slug}.png"

def log_path(domain: str, slug: str, failed: bool=False) -> Path:
    base = LOGS_ROOT / domain / ("failed_runs" if failed else "")
    return ensure_dir(base) / f"{_ts()}_{slug}.json"

def write_log(path: Path, data: dict):
    ensure_dir(path.parent)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
