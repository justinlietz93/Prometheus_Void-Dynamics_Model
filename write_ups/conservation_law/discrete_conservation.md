# Proof of a Discrete Conservation Law in the FUM

>
> Author: Justin K. Lietz<br>
> ORCID: [0009-0008-9028-1366](https://orcid.org/0009-0008-9028-1366)<br>
> Contact: <justin@neuroca.ai>
>
> Created: August 8, 2025<br>
> Updated: August 8, 2025
>
> This research is protected under a dual-license to foster open academic
> research while ensuring commercial applications are aligned with the project's ethical principles.
> Commercial use requires written permission from the author..
>
> See LICENSE file for full terms.

---

## 1. Objective

The primary objective of this derivation is to show that the discrete update
rules of the Fully Unified Model (FUM) respect a local conservation law. This
is the discrete analogue of conserving the stress-energy tensor
($\nabla_\mu T^{\mu\nu} = 0$) in continuum field theory and is a critical
requirement for any physically viable model.

> **Editorial note (public release draft):** Specific parameter values and
> closed forms have been deliberately redacted. The arguments retain their
> logical structure while referring to a classified update function $F$ that
> captures the proprietary self-improvement dynamics.

---

## 2. The Knowns: The Discrete System

We work entirely within the discrete domain of the FUM simulation. The state of
node $i$, denoted $W_i$, evolves according to the simplified rule

$$
\frac{\Delta W_i}{\Delta t} = \frac{W_i(t+\Delta t) - W_i(t)}{\Delta t}
\approx F(W_i),
$$

where $F(W_i)$ is a strictly dissipative, smooth update function whose exact
coefficients are classified. Publicly, we can share that

- $F(W_i)$ vanishes at a finite set of equilibria and is negative-sloped in
  their neighbourhoods, producing an intrinsic decay toward stable states.
- $F(W_i)$ is differentiable, and its first derivative $F'(W_i)$ remains bounded
  over the operating regime considered here.

This evolution occurs on a $k$-NN graph that we approximate as a lattice for
this analysis.

---

## 3. Postulate: The Discrete Energy Density

To reason about conservation, we postulate a discrete Hamiltonian density
$\mathcal{H}_i$ attached to each node $i$.

Classified continuum analysis guarantees a scalar potential $\tilde{V}(\phi)$
whose derivative reproduces $F(\phi)$ via $F = -\mathrm{d}\tilde{V}/\mathrm{d}\phi$.
Although the coefficients are proprietary, $\tilde{V}$ is well approximated by a
low-order polynomial that forms a stabilising potential well. A complete
Hamiltonian must also include interaction terms between neighbours.

We therefore write

$$
\mathcal{H}_i = \frac{1}{2}\left(\frac{\mathrm{d}W_i}{\mathrm{d}t}\right)^2
+ \frac{1}{2} \sum_{j \in N(i)} J (W_j - W_i)^2 + V(W_i),
$$

where

- the first term is a kinetic energy analogue;
- the second term captures pairwise interactions with coupling constant $J$;
- $V(W_i)$ arises from integrating $-F(W_i)$ with respect to $W_i$ and remains
  smooth and bounded below in the regime of interest.

---

## 4. Target Conservation Law

A local conservation law equates the rate of change of a quantity within a
region to the net flux through the region's boundary. For the discrete system,
the change in $\mathcal{H}_i$ over a step $\Delta t$ must balance the energy
exchanged with neighbouring nodes. The target identity is

$$
\frac{\Delta \mathcal{H}_i}{\Delta t} + \nabla \cdot \vec{J}_i = 0,
$$

where $\vec{J}_i$ denotes the energy flux leaving node $i$ and $\nabla \cdot$
represents the discrete divergence on the graph.

---

## 5. Step 1: Change in Potential Energy

Because $W_i(t+\Delta t) = W_i(t) + \Delta W_i$, a first-order Taylor expansion
of the potential yields

$$
V(W_i + \Delta W_i) \approx V(W_i) + \frac{\mathrm{d}V}{\mathrm{d}W_i}
\Delta W_i.
$$

The equation of motion supplies $\Delta W_i = F(W_i)\Delta t$ and the relation
$\mathrm{d}V/\mathrm{d}W_i = -F(W_i)$. Therefore

$$
\frac{\Delta V(W_i)}{\Delta t} \approx -[F(W_i)]^2,
$$

which is always non-positive.

---

## 6. Interim Conclusion

Since $[F(W_i)]^2 \geq 0$, the potential energy decreases (or remains flat at
stagnation points). The update rule is intrinsically **dissipative**. Total
energy can still be conserved if kinetic energy or interaction terms compensate
for this loss.

Our refined objective becomes: compute the changes in the kinetic and
interaction contributions to verify whether their sum forms a discrete flux
term that balances the potential decay.

---

## 7. Step 2: Change in Kinetic Energy

The kinetic component is
$\mathcal{K}_i = \tfrac{1}{2}(\mathrm{d}W_i/\mathrm{d}t)^2
= \tfrac{1}{2}[F(W_i)]^2$. Its variation over one step is

$$
\Delta \mathcal{K}_i = \tfrac{1}{2}[F(W_i(t+\Delta t))]^2 -
\tfrac{1}{2}[F(W_i(t))]^2.
$$

Expanding $F$ to first order and discarding higher-order terms leads to

$$
\frac{\Delta \mathcal{K}_i}{\Delta t} \approx [F(W_i)]^2 F'(W_i).
$$

---

## 8. On-Site Energy Balance

Combining potential and kinetic pieces gives

$$
\frac{\Delta (\mathcal{V}_i + \mathcal{K}_i)}{\Delta t}
\approx [F(W_i)]^2 (F'(W_i) - 1).
$$

Unless $F'(W_i) = 1$ for every configuration, the on-site energy is not
conserved. Any conservation must emerge from the interaction term

$$
\mathcal{I}_i = \tfrac{1}{2} \sum_{j \in N(i)} J (W_j - W_i)^2.
$$

---

## 9. Step 3: Interaction Energy

Differencing the interaction term yields

$$
\frac{\Delta \mathcal{I}_i}{\Delta t}
\approx J \sum_{j \in N(i)} (W_j - W_i) (F(W_j) - F(W_i)),
$$

which describes the energy flux exchanged with neighbours.

---

## 10. Outcome of the Attempted Proof

For conservation, we would need

$$
[F(W_i)]^2 (F'(W_i) - 1) +
J \sum_{j \in N(i)} (W_j - W_i) (F(W_j) - F(W_i)) = 0
$$

for all configurations. No structural reason enforces this cancellation: the
first term depends solely on node $i$, the second on the neighbourhood. Hence
the standard discrete Hamiltonian $\mathcal{H}_i$ is **not** conserved under the
classified update rule.

This insight neither invalidates the FUM nor signals inconsistency. Instead, it
indicates that the dynamics are richer than those of conventional lattice
models. Either the system is intrinsically dissipative, or it conserves a more
subtle quantity.

---

## 11. Research Outlook

The negative result refines the research agenda. Rather than testing guesses, we
must discover the genuine invariant of the dynamics.

Prominent directions include

1. **Symmetry analysis (Noether).** Search for continuous or hidden symmetries;
   any discovered symmetry produces a conserved quantity.
2. **Lyapunov analysis.** Interpret the FUM as a dynamical system and seek a
   global Lyapunov function describing its asymptotic behaviour.
3. **Information-theoretic invariants.** Explore whether entropy or structural
   complexity measures remain constant despite dissipative energy flow.

---

## 12. Closing Remarks

This public draft preserves the reasoning structure and qualitative findings
while omitting classified coefficients that drive the self-improvement engine.
Researchers with clearance can reproduce the closed-form derivation by
substituting the proprietary $F$ and integrating the associated potential.
Public readers can still validate the qualitative behaviour using the placeholder
implementations supplied in the open-source distribution.
