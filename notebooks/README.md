# Domain notebooks

This directory hosts interactive walkthroughs that mirror the repository’s
physics domains. Each notebook focuses on one benchmark or acceptance harness
and demonstrates how to drive the corresponding module from Python code while
capturing figures and logs in the standard locations (`figures/` and `logs/`).

## Layout

- `conservation_law/` - logistic invariant validation (`qfum_validate`).
- `reaction_diffusion/` - Fisher-KPP front-speed diagnostics (`rd_front_speed_walkthrough`, `rd_dispersion_walkthrough`, `rd_front_speed_sweep_walkthrough`).
- `fluid_dynamics/` - LBM-based benchmarks (`lid_cavity_walkthrough`, `taylor_green_walkthrough`).
- `memory_steering/` - steering experiments, acceptance, core helpers, and plotting harness (`memory_steering_*_walkthrough.ipynb`).
- `tachyonic_condensation/` - finite-tube mode solver and condensation baseline (`cylinder_modes_walkthrough`, `condense_tube_walkthrough`).

Shared helpers live in `utils.py`; they add the repository root to
`sys.path`, surface convenience wrappers around `src.common.io_paths`, and
generate timestamped slugs for artifacts.

## Usage

1. Activate the project environment and launch Jupyter from the repository
   root:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt  # if needed
   jupyter lab
   ```

2. Open any domain notebook and run the first code cell to initialise the path
   helpers (`ensure_repo_path`).
3. Execute the remaining cells in order. The example runs are lightweight and
   meant to illustrate inputs, acceptance gates, and artifact locations.
4. When you want production-grade outputs, run the scripted CLI entrypoints
   described in each notebook’s final section.

Tip: restart the kernel and use “Run All” before committing a notebook to
guarantee the recorded outputs are reproducible.
