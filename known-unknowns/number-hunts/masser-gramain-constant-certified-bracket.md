# Masser-Gramain constant delta: a certified bracket narrower than Melquiond-Nowak-Zimmermann's 1.819776 < delta < 1.819833 (2013)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

Let r_k be the smallest radius of a closed disc (any centre) containing at least k Gaussian integers. The Masser-Gramain constant is delta = lim_{n -> inf} (sum_{k=2}^{n} 1/(pi r_k^2) - log n), a two-dimensional analogue of Euler's constant. It arose in the Gelfond-Polya problem for entire functions taking Gaussian-integer values on Z[i]: Masser (1980) proved a sufficient growth threshold expressed through delta, and Gramain (1981) determined the best constant (OEIS A086056); MathWorld gives both. Gramain conjectured delta = 1.822825249...; OEIS A086058 lists 102 digits of this conjectured value. Gramain and Weber (Math. Comp. 1985, corrected 1987) proved 1.811447299 < delta < 1.897327117. Guillaume Melquiond, W. Georg Nowak and Paul Zimmermann (Math. Comp. 82 (2013) 1235-1246) proved 1.819776 < delta < 1.819833, disproving Gramain's conjecture, so delta is known to only four decimals. MathWorld (Masser-Gramain Constant), OEIS A086058 and Zimmermann's publication list show no later improvement (checked 2026-10-30). The HAL copy hal-00644166 showed a bot check (BLOCKED) and the AMS page returned 403. Each r_k^2 is an exact rational (the circumradius of two or three lattice points), so the head of the sum is exactly computable; the difficulty is a rigorous tail estimate from lattice-point counting in discs.

## What counts as a win

Success means a rigorous bracket a < delta < b with a > 1.819776 or b < 1.819833 (direction: narrower, strictly improving at least one end), and no wider at the other end than the published bounds or any later published bounds found by search immediately before claiming. The certificate has (i) exact r_k^2 for all k <= N, each with a witness disc and an exact minimality proof, computed by two independent implementations, and (ii) an explicit tail bound for k > N with a written proof (or exact citation of a published explicit estimate with its constants), evaluated in interval arithmetic by a supplied program.

## Partial wins

- **p1:** A published dataset of exact r_k^2 for all k <= 10^6 with witness discs, produced by two independently written programs that agree on every entry, together with the resulting exact head sums S(n) = sum_{k=2}^{n} 1/(pi r_k^2) - log n in interval arithmetic for n = 10^3, 10^4, 10^5, 10^6.

## How a win is checked

Skeptic: recompute r_k^2 for a random sample of 1,000 k <= N, and for all k <= 2,000, by brute-force enumeration of candidate circles through two or three lattice points. Check monotonicity and the 'at least k' convention. Rerun the interval tail evaluation and check that its inputs match the cited theorem's hypotheses. Expected: hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://mathworld.wolfram.com/Masser-GramainConstant.html>

## Sources

- <https://oeis.org/A086058>
- <https://mathworld.wolfram.com/Masser-GramainConstant.html>
- <https://doi.org/10.1090/S0025-5718-2012-02635-4>
- <https://hal.inria.fr/hal-00644166>
- <https://members.loria.fr/PZimmermann/papers/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Computational-geometry import: r_k is the k-th order minimum enclosing circle problem on a lattice; incremental algorithms over candidate centres (circumcentres and midpoints) make k up to 10^7 feasible.
- Analytic-number-theory import: the tail is governed by the lattice-point discrepancy in discs (the Gauss circle problem); use the best explicit discrepancy bounds with explicit constants rather than asymptotic exponents.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The disc centre need not be a Gaussian integer; restricting centres to lattice or half-lattice points overestimates r_k.
- OEIS A086058 lists Gramain's disproved conjectured value 1.82282..., not delta; do not use it as a comparator.
- 'At least k points' versus 'exactly k points' changes the sequence.
- A 2024-2026 literature search could not be completed when this entry was written (search budget exhausted); re-check for newer bounds before attacking.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/masser-gramain-constant-certified-bracket.md
```

Already set up? Say `run V3R1T4S on masser-gramain-constant-certified-bracket`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `masser-gramain-constant-certified-bracket`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
