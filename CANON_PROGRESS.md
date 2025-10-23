Void Dynamics Model (VDM) — Public Canon Progress Ledger

Repo: https://github.com/Neuroca-Inc/Prometheus_Void-Dynamics_Model
Maintainer: Justin K. Lietz (@Neuroca-Inc)
Document scope: Public, high‑level progress only. This ledger intentionally omits proprietary figures, logs, data files, internal thresholds/gates, and unreleased proposals. It is meant to advertise state, direction, and provenance at a coarse granularity.

VDM in one line: A unified, axiom‑driven program that treats “void fluctuation dynamics” as the substrate from which both ordinary physical behavior (waves, diffusion, structure) and a measurable agency/coordination field emerge, with claims tied to reproducible, falsifiable tests.

⸻

0) Reading guide
	•	What you’ll see here: branch structure, current focus, dated milestones (redacted), decisions, and next public steps.
	•	What you won’t see here: raw data, charts, solver settings, acceptance thresholds, or private proposal/result notes. Those are held back until curated releases.

⸻

1) Branch structure (high‑level)

VDM is developed as three coordinated limbs. Each limb has its own validation gates and cross‑checks.
	1.	Wave / EFT limb (hyperbolic)
Focus: finite signal cones, Noether/energy‑momentum accounting, conservative dynamics, dispersion.
Purpose: nails locality/causality in the conservative regime.
	2.	Diffusive / RD limb (parabolic)
Focus: reaction–diffusion calibration, pulled‑front speeds, linear dispersion, entropy/gradient‑flow checks.
Purpose: provides a disciplined “instrument” for driven/relaxational phenomena and budget audits.
	3.	Agency field C (driven, measurable proxy field)
Focus: causal (retarded) Green‑response to operational proxies (prediction, integration, control), regional budget closure, and cross‑substrate scaling collapse.
Purpose: tests whether a well‑posed “capability density” field behaves as a physical field under controlled drives.

A fourth thread (QG engine sketch) tracks the non‑perturbative, background‑independent direction in discrete form. Public notes here stay architectural until validation artifacts are posted.

⸻

2) Tier ladder (public summary)
	•	T1–T3 (calibration & sanity): establish basic solver hygiene, front‑speed/dispersion checks, and invariant/budget audits.
	•	T4 (causality response): impulse‑response fits to a retarded kernel; verify no pre‑response and budget closure.
	•	T5 (identifiability): separated drives yield monotone, minimally confounded sensitivities to defined source channels.
	•	T6 (universality): cross‑substrate scaling collapse in dimensionless coordinates; solver‑order checks.

Detailed thresholds and pass/fail gates are maintained privately and will be released alongside curated artifacts.

⸻

3) Public timeline (recent, high‑level)
	•	2025‑10‑23 — Ledger established
This public progress document created to synchronize the repo with the current state of work.
	•	2025‑10‑13 — Wave Flux Meter (Open‑Ports) — Phase B run completed (redacted)
High‑level: experimental runner and dashboard exercised with multiple channels/ports; confirms viability of the budget‑style auditing approach used for subsequent C‑field tests. Figures and metrics withheld pending curation.
	•	2025‑Q3 — Agency field C: T4/T5 protocol finalized (design level)
Causal impulse‑response and source‑decomposition plans locked (no numbers published here). Regional budget identity implemented in code; public release pending.
	•	2025‑Q3 — RD limb instrument re‑QC (design level)
Front‑speed and linear‑dispersion quick checks refreshed on current stack; detailed QC artifacts withheld. Purpose: ensure measurement “instrument” remains calibrated before higher‑tier tests.
	•	2025‑Q2–Q3 — Cross‑substrate plan drafted (design level)
Second substrate selected (fluid/transport proxy); KPI and two‑grid order checks defined internally for future T6 collapse attempt.
	•	2025‑Q2 — Axiom program & measurement discipline consolidated (doc level)
Internal documentation harmonized around locality/causality, metriplectic/Noether checks, scale program, and measurability practices.

⸻

4) Current focus (public)
	•	Near‑term: Execute and publish a minimal, self‑contained T4 causal response demonstration for the agency field C on a calibrated RD instrument (impulse → retarded fit → budget closure), with a plain‑English narrative and a small, reviewable artifact bundle.
	•	Staging: Prepare the second substrate harness to enable a T6 scaling‑collapse attempt after T4/T5 are public.

⸻

5) Decisions & scope cuts (public notes)
	•	Telescope & hardware builds: paused. Priority is on simulation discipline, reproducibility, and instrument‑grade numerical gates before expanding hardware surface area.
	•	Background‑independence claims: in the discrete setting, framed as scaling and re‑tessellation invariants, not exact continuum diffeomorphism invariance. We will state tolerances when artifacts are released.
	•	Public claims standard: VDM posts only claims paired to runnable artifacts and explicit gates. Narrative without instrumentation is treated as provisional.

⸻

6) What to expect next (public deliverables)

These are public‑facing deliverables that do not expose private data until curated:
	1.	VDM‑C T4 (Causal Response) — Minimal Release Note
	•	Contents: short rationale, method sketch, impulse protocol, pass/fail gate description (no raw logs), and one or two low‑resolution summary plots with hashes/commits redacted or batched.
	•	Goal: demonstrate cause‑before‑effect and budget closure in a way that is independently checkable once artifacts are opened.
	2.	Instrument QC Note (RD limb)
	•	Contents: brief reminder of the front‑speed & linear‑dispersion checks; explain why these serve as “measurement calibration” for C‑field work.
	•	Goal: contextualize T4 with instrument provenance.
	3.	Road‑to‑T6 Outline
	•	Contents: dimensionless rescaling plan, second‑substrate KPI table (without numbers), and the comparison protocol.
	•	Goal: set public expectations for what a scaling‑collapse result will mean.

Dates are not listed here; releases will appear as PRs in this repo with concise release notes.

⸻

7) Community notes
	•	Issues & questions: Please open GitHub Issues for conceptual questions or suggestions about public materials. Questions about private results will be acknowledged but may be deferred until the corresponding artifact release.
	•	Citations & reuse: If you discuss or reuse concepts from this repo, cite the repo root and this ledger file. Commercial use requires written permission per LICENSE.

⸻

8) Glossary (brief, public)
	•	Agency field C: An operationally defined field intended to quantify organized capability (prediction/integration/control) in a system. Tested via causal response and energy‑style budget closure.
	•	Budget identity (regional): Flux − decay + sources = change in stored quantity; used as a physical audit for field dynamics.
	•	Scaling collapse: After rescaling to dimensionless units, responses from distinct substrates overlay within tolerance; evidence of universality.
	•	T4/T5/T6: Progress tiers for causal response (T4), identifiability & dose–response (T5), and cross‑substrate universality (T6).

⸻

9) Changelog (public)
	•	2025‑10‑23: Initial public ledger added; synchronized with recent internal work.
	•	2025‑10‑13: Wave Flux Meter (Open‑Ports) Phase B run completed (summary only).

⸻

Maintainer note

This ledger is deliberately conservative. When results are posted, they will arrive with the usual artifact bundle (code+data), acceptance gates, and a short, reproducible path from equations → discretization → measurement. Until then, this file serves as the canonical public heartbeat of VDM.
