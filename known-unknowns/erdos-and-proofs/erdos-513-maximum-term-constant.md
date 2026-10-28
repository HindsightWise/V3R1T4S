# Erdos #513 (maximum-term constant C_51): a transcendental entire function with liminf mu(r)/M(r) above the record

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

For transcendental entire f, beta(f) = liminf_{r->inf} mu(r,f)/M(r,f), where mu is the largest term |a_n| r^n and M the maximum modulus. B = sup beta(f) (Erdos #513, Tao's constant 51) satisfies 4/7 < B <= 2/pi - c (Clunie-Hayman 1964). He and Tang (arXiv:2602.12217) generalised the Clunie-Hayman scaling-identity construction to a two-parameter family and certified B > 0.5850724 with ball arithmetic; Sothanaphan's GPT-assisted run nudged it to 0.5850788 and reported that more ambitious attempts failed; open pull request #184 claims 0.5850788196744* with exact parameters in the same family. The He-Tang family looks exhausted; a real improvement needs a new family. Target: a certified lower bound strictly above the best live value.

## What counts as a win

Success means an explicit construction of a transcendental entire function f (or a family with a proven formula for beta(f), as in He-Tang's identity beta = 1/max_{|z|=1}|k(z)|) together with a rigorous ball/interval-arithmetic certificate that beta(f) >= L with L STRICTLY GREATER (direction: max) than the largest lower bound listed on the live page https://teorth.github.io/optimizationproblems/constants/51a.html and in any open pull request touching constants/51a.md at https://github.com/teorth/optimizationproblems/pulls, both re-fetched live immediately before claiming, by at least 1e-9. The proof of the reduction from beta(f) to the certified quantity must be written out and checked by the skeptic; the maximum over the circle must be enclosed rigorously (not sampled).

## Partial wins

- **p1:** A new multi-parameter generalisation of the Clunie-Hayman/He-Tang construction (three or more parameters) with a proven beta-formula that reproduces the record within the new family, even if it does not beat it.
- **p2:** An independent rigorous replay of the open PR #184 value (exact parameters, circle maximum enclosed by arb), confirming or refuting it.

## How a win is checked

Recompute max_{|z|=1}|k(z)| for the stated Laurent series k with arb (python-flint) using a certified branch-and-bound on the circle and an explicit tail bound for the series; check the claimed functional identity numerically on random points as a sanity check; compare 1/max to the live record.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/51a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/51a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/51a.md>
- <https://www.erdosproblems.com/513>
- <https://arxiv.org/abs/2602.12217>
- <https://github.com/QuanyuTang/ep513-arb-certification>
- <https://github.com/teorth/optimizationproblems/pull/184>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Replace the single scaling identity k(Kz) = (stuff) k(z) by a two-scale or matrix-valued identity (a vector of Laurent series satisfying a linear system under z -> Kz), which still allows exact M(r) on a geometric sequence of radii.
- Cross-domain import (signal processing, filter design): maximising the peak term against the sup norm on the circle is a 'peak-to-average' problem; borrow Chebyshev/minimax filter design (Remez exchange) to shape |k| on |z| = 1.
- Cross-domain import (dynamical systems): the scaling identity is a renormalisation fixed point; look for other fixed points of the renormalisation operator by Newton's method in a space of Laurent coefficients.
- Upper-bound side for context: work out the explicit c in Clunie-Hayman's 2/pi - c (noted as missing on the forum); a numeric value would bound how much room there is.
- Gap structure: use lacunary power series with geometrically growing gaps where mu and M are both controlled by a few dominant terms, then optimise the coefficients.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Polynomials are excluded (they give 1); truncations used in computations must still correspond to a transcendental function with the stated liminf.
- Sampling the circle: max |k(z)| on |z| = 1 must be enclosed rigorously; a sampled max underestimates it and overstates beta.
- liminf vs limsup: the ratio along a favourable sequence of radii only bounds limsup; the reduction must control all large r.
- Rounding: records differ in the 7th-12th decimal; compare exact or certified values, not printed roundings, and include open PR #184.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-513-maximum-term-constant.md
```

Already set up? Say `run V3R1T4S on erdos-513-maximum-term-constant`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-513-maximum-term-constant`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
