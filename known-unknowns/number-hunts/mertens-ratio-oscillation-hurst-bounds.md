# Mertens function oscillations: a certified bound beating Hurst's liminf M(x)/sqrt(x) < -1.837625 or limsup > 1.826054

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster (or one multi-core workstation for weeks: Hurst's fplll runs at N = 800, nu = 17,000 took about 35 days each, and he projected 2 months for +-1.90 by the same method); laptop-days for about 15,000 zeta zeros to 5,000+ digits and for partial win p1 · open as of 2026-10-30

## The problem

Let q(x) = M(x)/sqrt(x) for the Mertens function M(x) = sum_{n<=x} mu(n). Odlyzko and te Riele (1985) disproved the Mertens conjecture by showing limsup q > 1.06 and liminf q < -1.009, using Ingham's theorem and LLL. Ingham's theorem (Hurst, Theorem 4.2) needs no RH: for any real y and any N, liminf q <= h(y,N) <= limsup q, where h(y,N) = 2 sum_{i<=N} a_i f(gamma_i/gamma_N) cos(gamma_i y + psi_i), with a_i = 1/|rho_i zeta'(rho_i)|, psi_i = arg(rho_i zeta'(rho_i)) and f(t) = (1-t)cos(pi t) + sin(pi t)/pi. A y that makes the cosines line up gives a bound, and finding one is a simultaneous Diophantine approximation (lattice) problem. Best and Trudgian (2015) showed limsup |q| >= 1.6383. Greg Hurst (Math. Comp. 87, 2018, arXiv:1610.08551) used fplll with nu = 17,000 and N = 800, about 35 days per run, to find y- = 1.50546e5096 and y+ = -2.58842e5097, giving h(y-,14400) = -1.837625 and h(y+,14400) = 1.826054. He estimated that bounds of +-1.90 / 1.95 / 2.00 need about 2 / 5 / 10 months with the same method. Kim and Nguyen (ANTS XVI, 2024) still cite Hurst's values as the record. They note that pruned lattice enumeration, which sped up their own counterexample search by a factor of millions, 'seems likely' to reach a larger value in much shorter time. Wikipedia (edited 2026-03-15) still lists Hurst's bounds. Target: a strictly better certified bound on either side.

## What counts as a win

Success means a real y (given exactly, as a rational or a decimal string), an N, and the list of zeros used, such that h(y,N), evaluated in rigorous interval arithmetic (Arb/FLINT ball arithmetic with certified enclosures of gamma_i and zeta'(rho_i)), has an enclosure lying entirely above 1.826054 (limsup side, direction: max) or entirely below -1.837625 (liminf side, direction: min). Before claiming, check that these remain the best published values: re-fetch the Wikipedia Mertens conjecture page, check arXiv for 2024-2026 work citing Hurst or Kim-Nguyen, and beat any newer value. The skeptic recomputes h(y,N) with an independently written evaluator, using zeros computed by separate software (mpmath zetazero at high precision cross-checked against Arb). The zero list must be complete up to gamma_N, which is verified by Turing's method or by matching N(T).

## Partial wins

- **p1:** A certified |h(y,N)| >= 1.75 from a y found by the agent's own lattice search (not Hurst's), evaluated in ball arithmetic over a complete zero list, showing the pipeline works end to end.
- **p2:** A certified |h(y,N)| >= 1.81 from the agent's own search, matching Hurst's N = 700 level (-1.81111 / 1.81252), with timings.

## How a win is checked

Compute the first N zeros and zeta'(rho) with python-flint (acb_dirichlet_zeta_zeros plus derivatives) at about 1.2 x log10|y| + 50 digits, confirm completeness with N(T), evaluate the finite sum in ball arithmetic, and check the sign of the enclosure. This takes hours on a laptop for N of about 15,000.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Mertens_conjecture>

## Sources

- <https://arxiv.org/abs/1610.08551>
- <https://antsmath.org/ANTSXVI/papers/KimNguyen.pdf>
- <https://en.wikipedia.org/wiki/Mertens_conjecture>
- <https://www-users.cse.umn.edu/~odlyzko/doc/arch/mertens.disproof.pdf>
- <https://zenodo.org/records/10775723>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Replace one long LLL run with BKZ plus pruned enumeration around the target vector (the Kim-Nguyen pipeline, code on Zenodo), aimed at maximising h rather than proving |h| > 1.
- Order zeros by weight a_i rather than by height (Hurst section 4) and put only the heaviest few hundred in the lattice; evaluate the full sum with N = 15,000 afterwards.
- Cross-domain import (phase retrieval / beamforming): maximising a weighted sum of cosines over one real parameter y is the array-steering problem; local refinement of y after the lattice step (Newton on h'(y)) can add a few thousandths.
- Kernel choice: Ingham's theorem holds for other admissible kernels; a kernel with a heavier tail at fixed N may raise the achievable value (prove admissibility).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Precision: y is about 10^5097, so gamma_i y mod 2 pi needs gamma_i to about 5,100 or more significant digits; double or 100-digit zeros give garbage.
- The bound uses h(y,N) with the f(gamma/gamma_N) taper; dropping the taper or using a raw partial sum of the explicit formula gives values that do not bound limsup q.
- A missed or duplicated zero below gamma_N invalidates the certificate; check the count against N(T).
- Hurst's exact y-values and zero data were linked only through a Wolfram Cloud notebook (wolfr.am/mertens), which returned 404 on 2026-10-30; do not plan on re-evaluating his y.
- Not a counterexample: these bounds do not exhibit any x with |M(x)| > sqrt(x).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/mertens-ratio-oscillation-hurst-bounds.md
```

Already set up? Say `run V3R1T4S on mertens-ratio-oscillation-hurst-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mertens-ratio-oscillation-hurst-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
