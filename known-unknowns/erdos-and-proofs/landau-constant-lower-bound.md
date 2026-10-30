# Landau's constant L (C_57b): a certified lower bound above Wikstrom's 0.51 (covering radius 0.51003; upper bound 0.5433)

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (LP or SDP relaxations plus an Arb box covering) · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 57b. Landau's constant L is the infimum, over holomorphic f on the unit disc with f'(0) = 1, of the radius of the largest disc contained in f(D). Rademacher (1943) proved L <= Gamma(1/3)Gamma(5/6)/Gamma(1/6) = 0.5433... and conjectured equality. The live page lists L > 1/2 + 1e-335 (Yanagihara 1995). Frank Wikstrom (arXiv 2609.23236, 19 Sep 2026, unrefereed) proved B_l > 0.51 and L > 0.51, where B_l is the locally univalent Bloch constant and B_l <= L, improving the 1/2 + 2e-8 of Chen and Shiba. He works with g = log f', where the Bloch condition becomes a one-sided linear constraint on Re g, and uses positive Toeplitz moment matrices as a finite relaxation for the low logarithmic coefficients. Floating-point LP dual vectors are re-verified by an independent Arb program at 80 digits over 1,179 boxes; the smallest certified radius in the final covering is 0.51003. Open PR #223 proposes the 0.51 row. Chain: B <= B_l <= L <= B_u.

## What counts as a win

Main win: a lower bound L >= l* (or B_l >= l*, which implies the same for L) with l* STRICTLY GREATER (direction: max) than 0.51003 and than every lower bound on https://teorth.github.io/optimizationproblems/constants/57b.html, in open pull requests touching constants/57b.md, and in any later paper an arXiv search finds, all re-checked immediately before claiming. Proof standard: a written reduction (the relaxation and why it is valid) plus dual certificates and a box covering that a supplied rigorous-arithmetic program verifies. Alternative main win, refuting Rademacher's conjecture: an explicit f with f'(0) = 1 and a rigorous certificate that every disc contained in f(D) has radius at most rho for an explicit rho STRICTLY LESS than the exact Rademacher value Gamma(1/3)Gamma(5/6)/Gamma(1/6) = 0.5432589653429767... (Rademacher's own extremal function attains this value and does not count).

## Partial wins

- **p1:** An independent replay of Wikstrom's 2609.23236 certificate: rebuild the relaxation from the paper, re-derive dual vectors and re-verify a box covering of the normalised coefficient body in rigorous arithmetic, confirming L > 0.51 or exhibiting a box where the certificate fails.

## How a win is checked

Skeptic: check the relaxation's validity argument (the Toeplitz positivity follows from the cited Herglotz/Caratheodory representation). Rerun the certifier at two precisions and confirm that the boxes cover the full normalised coefficient body (separate covering check). Check that each box's dual certificate gives a radius of at least the claimed l*. Expected: hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/57b.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/57b.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/57b.md>
- <https://arxiv.org/abs/2609.23236>
- <https://github.com/teorth/optimizationproblems/pull/223>
- <https://doi.org/10.1007/BF02788763>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Raise the truncation order of the moment relaxation and add higher-order Toeplitz or Hankel constraints; the 0.51003 margin suggests the relaxation, not the method, is the bottleneck.
- Polynomial-optimisation import: Lasserre hierarchy with rational rounding of SDP duals (as in flag-algebra certificates) gives exact certificates without box splitting.
- Adaptive box refinement driven by the dual gap, as in branch-and-bound global optimisation.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The live page still shows 1/2 + 1e-335; the comparator is Wikstrom's 0.51 (covering radius 0.51003).
- Bounds for the Bloch constant B do not transfer upward: B <= L, so a lower bound on B says nothing new about L, while a lower bound on B_l does bound L.
- Truncating to finitely many coefficients needs a rigorous tail bound; dropping it gives an invalid bound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/landau-constant-lower-bound.md
```

Already set up? Say `run V3R1T4S on landau-constant-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `landau-constant-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
