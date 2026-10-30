# Collinear H3 benchmark potential energy curve: a lower variational Born-Oppenheimer energy than Ferenc and Matyus (2022) at the van der Waals minimum or at any of their 114 tabulated geometries

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (3-electron explicitly correlated Gaussians, 1,000-2,000 functions, nonlinear optimisation; Ferenc-Matyus used 12 cores for months on the best point) · open as of 2026-10-30

## The problem

H + H2 is the simplest chemical reaction, and its Born-Oppenheimer surface underlies reactive-scattering benchmarks. Dávid Ferenc and Edit Mátyus (arXiv:2203.11978, Chem. Phys. Lett. 2022, doi 10.1016/j.cplett.2022.139734) computed the clamped-nuclei, nonrelativistic ground-state (doublet) energy of collinear H3. They used explicitly correlated Gaussians built by fragment initialisation and Powell refinement in their QUANTEN program, and give energies to 9 decimals with sub-ppm precision. The geometry is three collinear protons, with H2 bond length R_H2 and the third proton at distance R from the H2 nuclear midpoint. Table 1: R_H2 = 1.4, R = 6.442 bohr, 1200 ECGs and 3000 Powell cycles: -1.674561687 Eh (extrapolated -1.67456175(3)). At R = 7.142 bohr they give -1.674547750, against -1.67454742100 by Pavanello, Tung and Adamowicz (J. Chem. Phys. 131, 184106, 2009, six months of computation). Table 2: R_H2 = 1.4015 and R = 6.51205 bohr, the MRCI van der Waals minimum of Mielke, Garrett and Peterson (2002): -1.674562264, 74 microhartree below the best MRCI. Their van der Waals well depth is 86.54(3) microhartree. Table 3 (Supplementary Material): 114 points at R_H2 = 1.4 with R = 3.942 to 15.242 bohr in 0.1 steps, each from 5 Powell cycles after basis rescaling. Its lowest point is -1.674561899 at R = 6.542. The gap between their raw values and the CBS extrapolation (about 6e-8 Eh at 6.442) shows that the energies are not converged at the printed digits.

## What counts as a win

Success means an explicit trial wavefunction for three electrons in the field of three fixed unit-charge protons at the Table 2 geometry. The protons are collinear: two at +-0.70075 bohr along z (R_H2 = 1.4015) and the third at z = 6.51205 bohr from their midpoint. The state is the doublet ground state with spin and permutation symmetry imposed. Its checker-computed energy expectation value must be STRICTLY LOWER (direction: min) than -1.674562264 Eh by at least 1e-9 Eh, i.e. <= -1.674562265 Eh. It must also be lower than any later published variational value for the identical geometry found by a literature search (arXiv, J. Chem. Phys., Chem. Phys. Lett.) immediately before claiming. Infinite nuclear masses; no relativistic, QED or adiabatic corrections.

## Partial wins

- **p1:** Any Table 3 geometry (R_H2 = 1.4 bohr, R in {3.942, 4.042, ..., 15.242} bohr from the H2 midpoint): a variational energy STRICTLY LOWER, by at least 2e-9 Eh, than the lowest value the paper prints for that geometry. That is the Table 3 value, except at R = 6.442, where Table 1's -1.674561687 is lower than Table 3's -1.674561676 and is the bar. At R = 7.142, Table 3's -1.674547764 is lower than Table 1's -1.674547750 and is the bar.
- **p2:** An openly published ECG wavefunction file for the Table 2 geometry (all centres, exponent matrices, linear coefficients and the spin function), built without starting from any basis parameters deposited by Ferenc and Matyus, whose checker-computed energy is <= -1.674562261 Eh, i.e. within 3e-9 Eh of Ferenc-Matyus's -1.674562264 or below it. Reformatting, rescaling or refining their Supplementary Material basis does not count for this partial (it does for p1 and the full win).

## How a win is checked

Checker (minutes for <= 2,000 functions): read the floating ECG basis (centres, exponent matrices, coefficients) and the spin function. Build the overlap, kinetic, electron-nucleus and electron-electron matrices with the standard Boys-Singer closed forms, using the Boys function for the Coulomb terms. Apply the three-electron antisymmetrizer with the doublet spin coupling explicitly (6 permutations). Compute the Rayleigh quotient in float64 with a quad-precision re-check, or solve the generalized eigenproblem, and confirm the overlap matrix is positive definite. Confirm the nuclear positions match the declared geometry to 1e-10 bohr, and compare with the bar.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2203.11978>

## Sources

- <https://arxiv.org/abs/2203.11978>
- <https://arxiv.org/pdf/2203.11978v1>
- <https://doi.org/10.1016/j.cplett.2022.139734>
- <https://doi.org/10.1063/1.3257592>
- <https://doi.org/10.1063/1.1446852>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from fragment products (H2 ECG ground state at 1.4 bohr times an H-atom Gaussian expansion), as Ferenc and Matyus did, then spend the budget on full-basis refinement at a single geometry. Their PEC points had only 5 Powell cycles each and are the softest cells.
- Stochastic variational method (Suzuki-Varga) with competitive selection over random floating centres along the molecular axis, and analytic energy gradients for the exponents and centres (Adamowicz-style), should beat Powell refinement at equal cost.
- The long-range points (R > 10 bohr) depend on describing the dispersion tail; add Gaussians with diffuse correlation factors between the H atom electron and the H2 electrons.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Geometry definition: R is measured from the H2 nuclear centre of mass (the midpoint), not from the nearer proton. Ferenc and Matyus show that the 2009 Pavanello et al. value belongs to the nearer-proton convention (7.142 vs 6.442 bohr).
- At R = 6.442 and 7.142 the paper prints different values in Tables 1 and 3 (Table 1: -1.674561687 and -1.674547750; Table 3: -1.674561676 and -1.674547764). The bar is the lower of the two.
- The extrapolated CBS value -1.67456175(3) is not variational and is not the bar. Beating the raw value by 1e-9 is required. A value below the extrapolated limit should trigger extra scrutiny of linear dependence and precision.
- Ferenc and Matyus deposited their optimised basis parameters in the Chem. Phys. Lett. Supplementary Material, so refining that basis is the cheapest route. For the Table 2 point, the text says 5 Powell cycles (4 hours) while footnote d says 1000 cycles. Either way it is less refined than the 3000-cycle point at 6.442 bohr.
- Literature status: the 9 works citing the paper (OpenAlex, checked 2026-10-30) report no lower energy. Ferenc-Matyus 2023 (arXiv:2208.03033) reuses -1.674561687. Repeat the search before claiming; it is part of the criterion.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/h3-collinear-benchmark-pec-ecg-energies.md
```

Already set up? Say `run V3R1T4S on h3-collinear-benchmark-pec-ecg-energies`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `h3-collinear-benchmark-pec-ecg-energies`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
