# Void Dynamics Model - Declassified Public Overview

***Current Status:*** 

> Cleaning up existing RD papers, adding code files to Zenodo, and writing new papers for Memory Steering + reproducibility code.

***Status Last Updated:*** Sep 29, 2025

> Author: Justin K. Lietz<br>
<a href="https://orcid.org/0009-0008-9028-1366"><img src="https://img.shields.io/badge/ORCID-0009--0008--9028--1366-blue?" alt="ORCID: 0009-0008-9028-1366"></a> <br>
> Contact: <justin@neuroca.ai>
>
> Created: August 9, 2025<br>
> Updated: September 29, 2025
>
> This research is protected under a dual-license to foster open academic
> research while ensuring commercial applications are aligned with the project's ethical principles.
> Commercial use requires written permission from the author..
>
> ![Static Badge](https://img.shields.io/badge/Academic%2FCommercial%20Dual-License?label=LICENSE&color=%23fff200&link=https%3A%2F%2Fgithub.com%2FNeuroca-Inc%2FPrometheus_Void-Dynamics_Model%2Fblob%2Fmain%2FLICENSE.md)
>
> See LICENSE file or click the LICENSE badge above for full terms.

## 🔥News:
- **September 29, 2025:** First public code release + creation of private Void Dynamics package which can now be imported and run in this repository using workflows and repository secrets.
- **September 28, 2025:** Posted two pre-prints to [Zenodo](https://doi.org/10.5281/zenodo.17220869). If you've published similar or relevant work on Reaction-Diffusion in the past 3 years on arXiv and want to support this work by endorsing me in a related category, submit an issue, post in the discussion board, or send me an email with `Subject: RD Endorsement` to get my attention. It would be much appreciated!
- **August 21, 2025:** Launched public repo

## 🎯Planned:
- Continue to slowly declassify private work to this repository.
- Request endorsements to publish to a Mathematics category on ArXiv for latest Reaction Diffusion validations.
- Post Memory Steering validations as pre-print to Zenodo.
- Publish a working demo of my currently private Multimodel Untrained Real-Time Void Dynamics Intelligence Model with a real-time self-organizing spiking neural network and self-healing emergent knowledge graph that performs topological data analysis on it's own graph during runtime.
- Continue working toward other areas of Physics, like Quantum Gravity
- Once published to arXiv, take steps towards a peer reviewed journal and gather criticisms to refine my work.

## DOIs:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17220869.svg)](https://doi.org/10.5281/zenodo.17220869)

<div style="text-align: center;">
<img width="800" height="800" alt="logo" src="https://github.com/user-attachments/assets/b22adc5d-f126-4865-9e47-71af5fa4f7f7" />
</div>

---

## ❗NOTE

> **This organization is currently managed and operated by me (J. Lietz) alone as a solo developer / researcher. I may not respond by email right away. If you want to get my attention post in the discussion board briefly about what you'd like to talk about and let me know you sent me an email.**

## 📜Background Context

> You may see reference to **FUM (Fully Unified Model** or **FUVDM (Fully Unified Void Dynamics Model)** within the repository, this is referencing the **VDM (Void Dynamics Model)**. These were earlier names given to the model for specific reasons, and it's been my decision to simplify and specify the name to improve clarity. **Fully Unified Model** was originally named so because of it's unique architecture.
>
> I effectively broke down every type of machine learning model to it's fundamental principles and strategies. Then I began unifying them into a single architecture. This created my first variant of the model I called **AMN (Adaptive Modular Network)**. **AMN** was able to learn to solve quadratic equations with ~85% accuracy in 65 seconds of training and only a handful of examples.
>
> While doing this I quickly realized I could get the same behavior or better while removing a lot of the heavy solutions that LLMs, GNNs, SNNs, CNNs, and other ANNs used just by allowing a principle in physics called **the path of least action** to occur in the space between interactions. Eventually I realized I accidentally connected a lifelong hypothesis of mine ("intelligence emerges from the void space within the interactions of entities") to the model. Thus, the **Void Dynamics Model** earned it's name.

### 💬**Discussion Board:** 
- https://github.com/orgs/Neuroca-Inc/discussions

---

This repository includes provides a public, declassified view of the Void Dynamics Model.
It includes the theory, write-ups, code, notebooks, figures, logs, and validations for review by physicists,
applied mathematicians, and scientifically minded engineers. 
Reproducible code released for the public is now available. Proprietary code is not available to view directly, but can be run via a private package with this repository.
Remaining proprietary work must be requested directly.

> **Classified dependency notice**
>
> Certain executable simulations load void-dynamics and memory-steering modules
> from a private Neuroca, Inc package repository. If those files are missing, the code exits with:
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
> Contact the maintainer for access. After gaining access, the simulations will run normally.

## 🧭What this is

* A set of derivation papers that establish a clean baseline physics slice
  using reaction-diffusion (RD).
* Additional documents that explore a future, quarantined effective field
  theory (EFT) branch, clearly labeled as future work.
* Each paper separates what is proven from what is plausible or speculative
  and, where applicable, includes acceptance criteria for simple numerical
  checks.

## 🤖Why it relates to AI (brief)

* The project studies how simple, local rules can yield stable, interpretable
  global behavior under resource constraints.
* That design philosophy is relevant to AI systems that favor locality,
  event-driven updates, and transparent evaluation instead of opaque
  heuristics.
* “Memory steering” (covered separately) frames slow routing bias and
  retention/decay as structured influences over faster dynamics, an analogy
  for directing computation without black-box shortcuts.

## ☄️What’s inside (papers)

* Program overview and banner:
  * [VDM_Overview.md](VDM_Overview.md)
* Papers and pre-prints:
  * [papers/](/papers/)
* Foundations:
  * [discrete_to_continuum.md](write_ups/foundations/discrete_to_continuum.md)
  * [continuum_stack.md](write_ups/foundations/continuum_stack.md)
* Reaction-Diffusion (canonical baseline):
  * [rd_front_speed_validation.md](write_ups/reaction_diffusion/rd_front_speed_validation.md)
  * [rd_dispersion_validation.md](write_ups/reaction_diffusion/rd_dispersion_validation.md)
  * [rd_validation_plan.md](write_ups/reaction_diffusion/rd_validation_plan.md)
* Memory Steering (slow routing bias; separate layer):
  * [memory_steering_acceptance_verification.md](write_ups/memory_steering/memory_steering_acceptance_verification.md)
* Finite-domain EFT modes (quarantined future work):
  * [finite_tube_mode_analysis.md](write_ups/tachyon_condensation/finite_tube_mode_analysis.md)
* Change log / scoping notes:
  * [CORRECTIONS.md](CORRECTIONS.md)

## 🚫What’s not included

* Source code, executables, or private runtime harnesses.
* Logs, figures, or any artifacts that would be sufficient to easily
  reconstruct proprietary implementations. Notebooks with clear falsifiable
  code will be provided soon.
* Drafts outside the derivation index above.

## 📖How to read these papers

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

## ⚖️Licensing and scope

* These materials are shared for academic review and discussion. Commercial
  use requires prior written permission. See the project’s license notice in
  the distribution or parent repository materials.
* The scope stays within theoretical physics and simulation. Broad
  cosmological claims are withheld or clearly labeled until backed by
  derivation + numeric checks.

## 🔖Citations

* When referencing specific results, cite the overview and the relevant
  validation paper, for example:
  * [VDM_Overview.md](VDM_Overview.md)
  * [rd_front_speed_validation.md](write_ups/reaction_diffusion/rd_front_speed_validation.md)
  * [rd_dispersion_validation.md](write_ups/reaction_diffusion/rd_dispersion_validation.md)

## 📫Contact

* For scope questions or clarifications about acceptance criteria, refer to the
  headers in the overview and topic files listed above. If you are reading this
  as part of a paper-only bundle, the maintainer’s contact is provided alongside
  the distribution materials.
