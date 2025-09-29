# Void Dynamics Models (FUVDM - Fully Unified Void Dynamics Model) - Declassified Public Overview

> Author: Justin K. Lietz<br>
> ORCID: [0009-0008-9028-1366](https://orcid.org/0009-0008-9028-1366)<br>
> Contact: <justin@neuroca.ai>
>
> Created: August 9, 2025<br>
> Updated: September 29, 2025
>
> This research is protected under a dual-license to foster open academic
> research while ensuring commercial applications are aligned with the project's ethical principles.
> Commercial use requires written permission from the author..  
> See LICENSE file for full terms.

DOIs:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17220869.svg)](https://doi.org/10.5281/zenodo.17220869)

<div style="text-align: center;">
<img width="800" height="800" alt="logo" src="https://github.com/user-attachments/assets/b22adc5d-f126-4865-9e47-71af5fa4f7f7" />
</div>

---

## NOTE

> **This organization is currently managed and operated by me (J. Lietz) alone as a solo developer / researcher. I may not respond by email right away. If you want to get my attention post in the discussion board briefly about what you'd like to talk about and let me know you sent me an email.**

**Discussion Board:** https://github.com/orgs/Neuroca-Inc/discussions

***Current Status:*** Setting up reproducible code for all the work I'm comfortable with sharing publicly. Code that directly runs my private Void Equations will call a private workflow and return the results so you can still see proof.

***Status Last Updated:*** Sep 29, 2025

This folder provides a public, paper-only view of the Void Dynamics program.
It summarizes the theory and validation write-ups for review by physicists,
applied mathematicians, and scientifically minded engineers. Proprietary
source code is not included yet.

> **Classified dependency notice**
>
> Certain executable simulations load void-dynamics and memory-steering modules
> from `secrets/`. If those files are missing, the code exits with:
>
> `Attempted to import classified code, ask the author for access to run this
> simulation. Otherwise you can still view figures and logs.`
>
> Affected entry points include:
>
> * `code/fluid_dynamics/fluids/lbm2d.py` (and benchmarks such as
>   `taylor_green_benchmark.py` and `lid_cavity_benchmark.py`).
> * `code/memory_steering/memory_steering_experiments.py`.
>
> Contact the maintainer for access. After placing the classified modules in
> `secrets/`, the simulations will run normally.

## What this is

* A set of derivation papers that establish a clean baseline physics slice
  using reaction–diffusion (RD).
* Additional documents that explore a future, quarantined effective field
  theory (EFT) branch, clearly labeled as future work.
* Each paper separates what is proven from what is plausible or speculative
  and, where applicable, includes acceptance criteria for simple numerical
  checks.

## Why it relates to AI (brief)

* The project studies how simple, local rules can yield stable, interpretable
  global behavior under resource constraints.
* That design philosophy is relevant to AI systems that favor locality,
  event-driven updates, and transparent evaluation instead of opaque
  heuristics.
* “Memory steering” (covered separately) frames slow routing bias and
  retention/decay as structured influences over faster dynamics, an analogy
  for directing computation without black-box shortcuts.

## What’s inside (papers)

* Program overview and banner:
  * [VDM_Overview.md](VDM_Overview.md)
* Foundations:
  * [discrete_to_continuum.md](write_ups/foundations/discrete_to_continuum.md)
  * [continuum_stack.md](write_ups/foundations/continuum_stack.md)
* Reaction–Diffusion (canonical baseline):
  * [rd_front_speed_validation.md](write_ups/reaction_diffusion/rd_front_speed_validation.md)
  * [rd_dispersion_validation.md](write_ups/reaction_diffusion/rd_dispersion_validation.md)
  * [rd_validation_plan.md](write_ups/reaction_diffusion/rd_validation_plan.md)
* Memory Steering (slow routing bias; separate layer):
  * [memory_steering_acceptance_verification.md](write_ups/memory_steering/memory_steering_acceptance_verification.md)
* Finite-domain EFT modes (quarantined future work):
  * [finite_tube_mode_analysis.md](write_ups/tachyon_condensation/finite_tube_mode_analysis.md)
* Change log / scoping notes:
  * [CORRECTIONS.md](CORRECTIONS.md)

## What’s not included

* Source code, executables, or private runtime harnesses.
* Logs, figures, or any artifacts that would be sufficient to easily
  reconstruct proprietary implementations. Notebooks with clear falsifiable
  code will be provided soon.
* Drafts outside the derivation index above.

## How to read these papers

* Each file follows a consistent structure: Purpose · Assumptions/Parameters ·
  Discrete law · Continuum limit · PDE/Action/Potential · Fixed points &
  stability · Dispersion · Conservation/Lyapunov · Numerical plan +
  acceptance · Results · Open questions.
* Claim labels:
  * [PROVEN] = sign/dimension/limit checks plus a minimal numerical test that
    passes stated tolerances.
  * [PLAUSIBLE] = future work with rationale; quarantined until derivation +
    checks are complete.
  * [SPECULATIVE] = exploratory; not used for baseline claims.

## Licensing and scope

* These materials are shared for academic review and discussion. Commercial
  use requires prior written permission. See the project’s license notice in
  the distribution or parent repository materials.
* The scope stays within theoretical physics and simulation. Broad
  cosmological claims are withheld or clearly labeled until backed by
  derivation + numeric checks.

## Citations

* When referencing specific results, cite the overview and the relevant
  validation paper, for example:
  * [VDM_Overview.md](VDM_Overview.md)
  * [rd_front_speed_validation.md](write_ups/reaction_diffusion/rd_front_speed_validation.md)
  * [rd_dispersion_validation.md](write_ups/reaction_diffusion/rd_dispersion_validation.md)

## Contact

* For scope questions or clarifications about acceptance criteria, refer to the
  headers in the overview and topic files listed above. If you are reading this
  as part of a paper-only bundle, the maintainer’s contact is provided alongside
  the distribution materials.
