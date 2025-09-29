# Domain notebooks

This directory hosts interactive walkthroughs that mirror the repository’s
physics domains. Each notebook focuses on one benchmark or acceptance harness
and demonstrates how to drive the corresponding module from Python code while
capturing figures and logs in the standard locations (`figures/` and `logs/`).

## Layout

- `conservation_law/` – logistic invariant validation (`qfum_validate`).
- `fluid_dynamics/` – lid cavity and related fluid benchmarks.
- `reaction_diffusion/` – Fisher–KPP front-speed diagnostics.
- `memory_steering/` – memory steering acceptance and exploratory runs.

Shared helpers live in `utils.py`; they add the repository root to
`sys.path`, surface convenience wrappers around `code.common.io_paths`, and
generate timestamped slugs for artifacts.

## Usage

1. Activate the project environment and launch Jupyter from the repository
   root:

   ```bash
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
