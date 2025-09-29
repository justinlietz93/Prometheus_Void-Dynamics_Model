#!/usr/bin/env python3
"""
Copyright © 2025 Justin K. Lietz, Neuroca, Inc. All Rights Reserved.

This research is protected under a dual-license to foster open academic
research while ensuring commercial applications are aligned with the project's ethical principles. Commercial use requires written permission from the author..
See LICENSE file for full terms.

Taylor-Green vortex (2-D) viscosity recovery benchmark for the fluids sector.

CHANGE REASON:
- Relocated into write_ups/code/physics/fluid_dynamics per repo rules (no Prometheus_VDM/bench/).
- Outputs follow RD harness: write_ups/code/outputs/{figures,logs}.
- Ensures JSON uses native Python types (bool/float) to avoid numpy serialization issues.

Outputs (defaults):
- Figures → figures/fluid_dynamics/<timestamp>_taylor_green_benchmark.png
- Logs    → logs/fluid_dynamics/<timestamp>_taylor_green_benchmark.json
"""
import argparse
import json
import math
import os
import time
from pathlib import Path
import sys

import numpy as np
import matplotlib.pyplot as plt


import common.io_paths as io_paths


def _add_repo_root() -> None:
    """Ensure the repository root is on sys.path for namespace imports."""
    here = Path(__file__).resolve()
    root = None
    for ancestor in [here] + list(here.parents):
        if (ancestor / ".git").exists():
            root = ancestor
            break
    if root is None:
        root = here.parents[2]
    root_str = str(root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)


_add_repo_root()

from code.fluid_dynamics.fluids.lbm2d import LBM2D, LBMConfig, CS2  # noqa: E402


def init_taylor_green(sim: LBM2D, U0=0.05, k=2*math.pi):
    nx, ny = sim.nx, sim.ny
    x = (np.arange(nx) + 0.5) / nx
    y = (np.arange(ny) + 0.5) / ny
    X, Y = np.meshgrid(x, y)
    sim.ux[:, :] =  U0 * np.cos(k * X) * np.sin(k * Y)
    sim.uy[:, :] = -U0 * np.sin(k * X) * np.cos(k * Y)
    sim._set_equilibrium()


def energy(ux, uy):
    return 0.5 * float(np.mean(ux**2 + uy**2))


def main():
    ap = argparse.ArgumentParser(description="Taylor–Green vortex viscosity recovery (LBM→NS).")
    ap.add_argument("--nx", type=int, default=256)
    ap.add_argument("--ny", type=int, default=256)
    ap.add_argument("--tau", type=float, default=0.8, help="Relaxation time (nu = cs^2*(tau-0.5))")
    ap.add_argument("--U0", type=float, default=0.05)
    ap.add_argument("--k", type=float, default=2*math.pi)
    ap.add_argument("--steps", type=int, default=5000)
    ap.add_argument("--sample_every", type=int, default=50)
    ap.add_argument("--outdir", type=str, default=None, help="base output dir; defaults to the repository root (figures/, logs/)")
    args = ap.parse_args()

    cfg = LBMConfig(nx=args.nx, ny=args.ny, tau=args.tau, periodic_x=True, periodic_y=True)
    sim = LBM2D(cfg)
    init_taylor_green(sim, U0=args.U0, k=args.k)

    t0 = time.time()
    ts, Es = [], []
    # Adaptive sampling using correct lattice wavenumber scaling:
    # ln E(t) slope s = -2 ν k^2 (1/nx^2 + 1/ny^2)
    nu_th_est = float(sim.nu)
    nx_f = float(args.nx)
    ny_f = float(args.ny)
    k_sq = float(args.k) * float(args.k)
    lam = k_sq * ((1.0 / (nx_f * nx_f)) + (1.0 / (ny_f * ny_f)))
    rate = 2.0 * nu_th_est * lam
    se = 1 if rate > 0.5 else max(1, int(args.sample_every))
    for n in range(args.steps + 1):
        if n % se == 0:
            sim.moments()
            ts.append(float(n))
            Es.append(energy(sim.ux, sim.uy))
        sim.step(1)
    elapsed = time.time() - t0

    ts = np.asarray(ts, dtype=float)
    Es = np.asarray(Es, dtype=float)

    # Fit E(t) ~ E0 * exp(-2 ν k^2 (1/nx^2 + 1/ny^2) t) using early-time window to avoid underflow
    mask = Es > (float(Es.max()) * 1e-12)
    ts_fit = ts[mask] if np.any(mask) else ts
    Es_fit = Es[mask] if np.any(mask) else Es
    if ts_fit.size >= 3:
        slope, intercept = np.polyfit(ts_fit, np.log(Es_fit + 1e-300), 1)
    else:
        slope, intercept = np.polyfit(ts[:max(3, ts.size)], np.log(Es[:max(3, Es.size)] + 1e-300), 1)
    # Invert slope s = -2 ν k^2 (1/nx^2 + 1/ny^2) ⇒ ν_fit = -s / [2 k^2 (1/nx^2 + 1/ny^2)]
    inv = 2.0 * k_sq * ((1.0 / (nx_f * nx_f)) + (1.0 / (ny_f * ny_f)))
    nu_fit = float(-slope / inv)
    nu_th  = float(sim.nu)
    rel_err = float(abs(nu_fit - nu_th) / (abs(nu_th) + 1e-12))

    acceptance_rel_err = 0.05
    passed = bool(rel_err <= acceptance_rel_err)

    script_name = os.path.splitext(os.path.basename(__file__))[0]
    domain = "fluid_dynamics"
    original_fig_root = io_paths.FIGURES_ROOT
    original_log_root = io_paths.LOGS_ROOT
    if args.outdir:
        base_override = Path(os.path.expandvars(args.outdir)).expanduser()
        io_paths.FIGURES_ROOT = base_override / "figures"
        io_paths.LOGS_ROOT = base_override / "logs"

    slug = script_name
    fig_path = io_paths.figure_path(domain, slug, failed=not passed)
    log_path = io_paths.log_path(domain, slug, failed=not passed)

    plt.figure(figsize=(7, 5))
    plt.semilogy(ts, Es, "o", ms=3, label="E(t) samples")
    plt.semilogy(ts, np.exp(intercept + slope * ts), "r--",
                 label=f"fit: nu_fit={nu_fit:.5f}, nu_th={nu_th:.5f}, rel_err={rel_err:.3%}")
    plt.xlabel("t (lattice)")
    plt.ylabel("E(t)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_path, dpi=140)
    plt.close()

    payload = {
        "theory": "LBM→NS; Taylor–Green viscous decay E=E0 exp(-2 nu k^2 t)",
        "params": {
            "nx": int(args.nx), "ny": int(args.ny), "tau": float(args.tau), "nu_th": nu_th,
            "U0": float(args.U0), "k": float(args.k),
            "steps": int(args.steps), "sample_every": int(args.sample_every)
        },
        "metrics": {
            "nu_fit": nu_fit, "nu_th": nu_th, "rel_err": rel_err,
            "acceptance_rel_err": acceptance_rel_err,
            "elapsed_sec": float(elapsed),
            "passed": passed
        },
        "outputs": {"figure": str(fig_path), "log": str(log_path)},
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    io_paths.write_log(log_path, payload)

    print(json.dumps(payload["metrics"], indent=2))

    io_paths.FIGURES_ROOT = original_fig_root
    io_paths.LOGS_ROOT = original_log_root


if __name__ == "__main__":
    main()
