---
agent: 54
chapter: 12
sections: 111-112
status: completed
timestamp: 2026-03-18T00:00:00Z
---

## Summary

Relativistic generalisation of Chapter XII §111–112 (capillary instability of jets).

### §111: Capillary instability of a relativistic jet
- **Surface tension**: Introduced relativistic surface energy-momentum tensor S^{mu nu} via Israel junction conditions. Surface energy density is a Lorentz scalar, so the Young-Laplace equation is unchanged.
- **Rayleigh-Plateau in SR**: Derived implicit dispersion relation with relativistically modified radial wave number kappa^2 = k^2 + sigma^2/c_s^2 and enthalpy density w = (epsilon+p)/c^2 replacing rho. Stability threshold (x < 1) unchanged (geometric result); growth rates modified by enhanced inertia and finite sound speed.
- **Hollow jet**: Extended to relativistic hollow jet with K-functions replacing I-functions and external enthalpy density.
- **Viscosity (Israel-Stewart)**: Replaced Navier-Stokes viscosity with frequency-dependent Israel-Stewart effective viscosity nu_eff = eta_s / [w(1 + tau_pi sigma)]. Derived relativistic viscous dispersion relation and viscosity-dominated limit.
- **Causality**: Proved capillary wave phase speeds < c; stated Israel-Stewart constraint tau_pi >= eta_s/(w c^2).

### §112: Axial B-field on capillary instability
- **Ideal relativistic MHD**: Dispersion relation with rho -> w; relativistic Alfven speed v_A^2 = v_A,cl^2/(1+v_A,cl^2/c^2) < c^2 automatically. Critical field for complete stabilisation is EOS-independent.
- **Finite conductivity (resistive MHD)**: Full implicit dispersion relation generalising eqs. (194)-(195) with enthalpy replacement. Verified zero-resistivity and infinite-resistivity limits.
- **High resistivity limit**: First-order expansion giving relativistic z-parameter and approximate roots.
- **General case**: Non-dimensional formulation with relativistic S-parameter; solution procedure same as classical.
- **Causality**: All MHD signal speeds (Alfven, fast magnetosonic) bounded by c; no additional constraints needed.

## Key relativistic modifications
1. rho -> w = (epsilon + p)/c^2 throughout (enhanced inertia)
2. Finite sound speed c_s introduces implicit kappa(sigma) coupling
3. Israel-Stewart causal viscosity with frequency-dependent nu_eff
4. Relativistic Alfven speed automatically < c
5. All Newtonian limits verified explicitly

## Output file
`output/chapters/relativistic/rel_chapter_12_sec111-112.tex`
