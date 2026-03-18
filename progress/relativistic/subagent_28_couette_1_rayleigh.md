---
agent: 28
chapter: 7
sections: 64-66
status: completed
timestamp: 2026-03-18T12:00:00Z
---

## Summary

Created relativistic generalization of Chandrasekhar Chapter VII §64-66 (Rayleigh criterion for Couette flow).

### §64 — Introduction: Relativistic Rotating Flows
- Motivating astrophysical contexts: accretion disks, relativistic jets, neutron-star interiors
- Key distinction: enthalpy density w = (epsilon+p)/c^2 replaces rest-mass density as inertia

### §65 — Physical Problem: Relativistic Couette Flow
- Steady circular flow with 4-velocity and Lorentz factor
- Relativistic centrifugal balance: (epsilon+p)/c^2 * v_phi^2/r = -dp/dr
- Relativistic Bernoulli integral with logarithmic form
- Relativistic specific angular momentum: l = gamma * r * v_phi * (epsilon+p)/(rho_0 c^2)
- Canonical angular momentum: l_tilde = gamma^2 r^2 Omega

### §66 — Rayleigh Criterion: Relativistic Version
- Interchange argument adapted to relativistic centrifugal potential
- Stability condition: d(l_tilde^2)/dr > 0
- Relativistic Rayleigh discriminant Phi_rel
- Epicyclic frequency kappa_rel^2 — connection to ISCO in accretion disks
- Non-relativistic limit recovers all classical results
- Application to viscous Couette profile: relativistic correction to critical mu
- Causality constraints: v_phi < c and c_s < c

## Conventions
- Metric signature (-,+,+,+), c explicit throughout
- Equation labels: eq:rel-7-N
- Section labels: sec:rel-7-64 through sec:rel-7-66

## Files Created
- `output/chapters/relativistic/rel_chapter_7_sec64-66.tex`
- `progress/relativistic/subagent_28_couette_1_rayleigh.md`
