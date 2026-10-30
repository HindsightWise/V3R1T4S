# MOONSHOT - Positronium negative ion Ps- (e- e+ e-): a variational ground-state energy below Frolov's 2023 record -0.26200507023298010777040211998

⚛️ **Physics** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (multiprecision linear algebra at 40-60 digits, 3,000-6,000 three-body exponential basis functions) · open as of 2026-10-30

## The problem

Ps- is the bound three-body Coulomb system e- e+ e-. All three masses are equal, so there is no mass-ratio convention to pin down. Its only bound state is the 1^1S (L = 0) ground state, with the two electrons in a spin singlet. The nonrelativistic energy in atomic units (hbar = m_e = e = 1) is a classic three-body benchmark, next to helium and H-. The record is held by Alexei M. Frolov (arXiv:2212.03723v7, 2 April 2023, 'the most recent, updated and corrected version'). His Table I uses a three-body exponential expansion in perimetric coordinates under two optimisation strategies. The best value, N = 3842 functions with variant B, is E = -0.26200507023298010777040211998 a.u. The abstract and conclusions call it 'the lowest variational energy ever obtained for this ion'. His previous best variational value (arXiv:1502.01691v3, 2015) was -0.26200507023298010777040051. Frolov's estimate of the limit (Chem. Phys. Lett. 626, 49, 2015, as quoted in arXiv:2405.08818) is -0.2620050702329801077704065(55), about 4e-24 below the 2023 record. The record has not converged: between N = 3800 and N = 3842 it still drops by 1.1e-24, so a larger or better-optimised basis should lower it. Frolov's arXiv listing, checked 2026-10-30, shows later papers on PsH (2024), muonic ions (2025), one-electron diatomic ions (2026) and muonic helium (2026), but none revisits the Ps- energy, and no paper citing 2212.03723 was found. Frolov publishes no wavefunction, so no open certificate for the record exists. The bar is a raw variational eigenvalue (Table I, not an extrapolation), so a strictly lower upper bound is possible in principle.

## What counts as a win

Success means a published file giving an explicit L = 0 trial function, symmetric under exchange of the two electrons, for the e- e+ e- Hamiltonian H = -1/2 (nabla_1^2 + nabla_2^2 + nabla_3^2) - 1/r31 - 1/r32 + 1/r21, with equal unit masses and the centre of mass removed. The file holds the basis type, every nonlinear parameter as an exact decimal or rational, and the linear coefficients (or the checker may re-solve for them). The checker computes the Rayleigh quotient E_var with interval certification. E_var must be STRICTLY LOWER (direction: min) than -0.26200507023298010777040211998 by at least 1e-27, i.e. E_var <= -0.26200507023298010777040212098 with the whole error ball below that value. It must also be lower than any later published variational energy for Ps- found by a literature search (arXiv, Google Scholar, Phys. Rev. A, Mol. Phys., Chem. Phys. Lett.) immediately before claiming. Extrapolated or estimated energies, such as Frolov's 2015 estimate -0.2620050702329801077704065(55), do not count.

## Partial wins

- **p1:** The first openly published, independently checkable Ps- certificate whose interval-certified Rayleigh quotient is <= -0.262005070232980107770 (agreement with the record to 21 significant digits). No record is claimed.
- **p2:** Basis efficiency: a certified variational energy below Frolov's N = 3800 variant-B value -0.26200507023298010777040100869 using at most 3,000 basis functions (the file's function count is checked).

## How a win is checked

Checker (minutes to a few hours): parse the basis. For exponentials in r21, r31, r32 (or perimetric u1, u2, u3), use the closed-form three-body integrals (the volume element 8 pi^2 r21 r31 r32 dr21 dr31 dr32 reduces every overlap, kinetic and Coulomb matrix element to rational functions of the exponents). Assemble S and H in python-flint arb ball arithmetic at >= 60 digits. Take the Rayleigh quotient c^T H c / c^T S c with the given coefficients, or solve the generalized eigenproblem in arb and certify the lowest root. Check that the upper end of the error ball is below the threshold, and that the function count matches for p2.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2212.03723>

## Sources

- <https://arxiv.org/abs/2212.03723>
- <https://arxiv.org/pdf/2212.03723v7>
- <https://arxiv.org/abs/1502.01691>
- <https://arxiv.org/abs/2405.08818>
- <https://doi.org/10.1103/PhysRevA.60.2834>
- <https://arxiv.org/search/?query=Frolov%2C+Alexei+M&searchtype=author&order=-announced_date_first>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Korobov-style randomly tempered exponentials with complex exponents (exp(-a r31 - b r32 - c r21), with a, b and c drawn from several nested intervals) converge to 30+ digits for equal-mass systems with fewer functions than real exponents.
- The record still drops about 1.1e-24 per 40 added functions near N = 3800-3842, and Frolov's own estimate of the limit lies about 4e-24 lower. Extending a good tempered basis to 5,000-6,000 functions at 50-digit precision is the straightforward route. The closed-form integrals make the matrices cheap; the cost is the multiprecision eigensolve.
- Use the symmetric structure (equal masses, exchange of the two electrons) to halve the matrix size. Do the eigensolve by inverse iteration in multiprecision, preconditioned by a double-double factorisation.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The bar is Frolov's printed Table I raw eigenvalue for N = 3842, variant B. Variant A at N = 3842 is slightly higher (-0.26200507023298010777040206643), so do not use it as the bar.
- Double or quad precision is far from enough. The overlap matrices become nearly singular, and only interval or ball-arithmetic results at >= 50 digits count.
- Conventions: equal masses m_e, centre-of-mass motion removed, no relativistic, QED or annihilation corrections; values in Rydberg (twice as large in magnitude) appear in the older literature.
- H- and helium are other bank entries (helium-ground-state-energy-digits); this target is Ps- only.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/ps-minus-ground-state-energy-digits.md
```

Already set up? Say `run V3R1T4S on ps-minus-ground-state-energy-digits`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ps-minus-ground-state-energy-digits`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
