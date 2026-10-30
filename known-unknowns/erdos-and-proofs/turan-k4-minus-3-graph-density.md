# Frankl-Füredi K4^- problem: a certified upper bound on pi(K4^-) below 0.286504, or a K4^--free 3-graph denser than 2/7

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: needs cluster (Lidický-Volec ran K4^- with 8-vertex flags: 9,895,719 K4^--free 3-graphs on 8 vertices, a 1,400 GB SDP in dat-s form solved in about 1,100 GB RAM with their lpsdp solver; re-checking the published interval-arithmetic certificates is much cheaper, but the paper does not state its cost) · open as of 2026-10-30

## The problem

K4^- is the 3-graph with three edges on four vertices. Its Turán density pi(K4^-) is conjectured to be 2/7 = 0.285714, the density of the recursive construction of Frankl and Füredi (1984), the iterated blow-up of the 10-edge (6,3,2)-design; this is the corrected form of Erdős problem #794 (whose statement as written was disproved by Harris). Upper bounds came from flag algebras: Razborov (0.2978), Baber and Talbot (0.2871), Vaughan's Flagmatic 2.0 (0.28689), and most recently Bernard Lidický and Jan Volec (arXiv:2610.33850, v1 24 Oct 2026), who report 0.286504 from an 8-vertex flag computation solved with their LP/cutting-plane solver lpsdp, with certificates checked in floating-point interval arithmetic (MPFI/MPFR; certificates at lidicky.name/pub/lpsdp/). The same paper gives the codegree-squared (l2-norm) version: lower bound 4/43 = 0.093023 (Balogh-Clemen-Lidický, arXiv:2108.10406), previous upper bound 0.09307 (same authors), new upper bound 0.093058. Both versions are conjectured to have the same unique maximizer. Both gaps are open as of 2026-10-30.

## What counts as a win

Success means EITHER (a) a certified proof that pi(K4^-) <= U with U STRICTLY LESS (direction: min) than the exact value certified by the published Lidický-Volec K4^- certificate (reported as 0.286504; compare against the certificate's exact value, not the rounded figure) and than any smaller bound found in a fresh check of arXiv:2610.33850 (latest version), arXiv:2108.10406 and papers citing them; the proof must be a flag-algebra certificate with exact rational or rigorous interval PSD verification that an independent checker re-runs, or a compiling Lean 4 proof; OR (b) an explicit K4^--free 3-graph construction (finite pattern with optional recursion, with a written freeness proof) whose limiting density is computed exactly and is STRICTLY GREATER (direction: max) than 2/7, which would refute the Frankl-Füredi conjecture.

## Partial wins

- **p1:** Codegree-squared version: a certified upper bound on pi_l2(K4^-) strictly below the exact value certified by Lidický-Volec (reported as 0.093058), or an explicit K4^--free construction whose limiting normalised codegree-squared sum is strictly above 4/43, verified to the same standard as the main criterion.
- **p2:** A complete Lean 4 proof (no sorry, no new axioms) of pi(K4^-) <= U for some U strictly below 0.28689 (the Flagmatic 2.0 value), provided no Lean-formalised bound of that strength is already public at claim time.

## How a win is checked

Enumerate all K4^--free 3-graphs on the certificate's vertex count up to isomorphism independently, recompute flag densities and products, check PSD matrices exactly (rational LDL^T) or with interval Cholesky, and confirm the bound on every graph. For constructions, brute-force K4^--freeness of the pattern under every map of 4 vertices to parts, verify the recursion argument, and compute the density symbolically. For l2, recompute the codegree-squared objective as defined in arXiv:2108.10406. Re-fetch arXiv:2610.33850 for later versions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.33850>

## Sources

- <https://arxiv.org/abs/2610.33850>
- <https://arxiv.org/html/2610.33850v1>
- <https://lidicky.name/pub/lpsdp/>
- <https://arxiv.org/abs/2108.10406>
- <https://www.erdosproblems.com/794>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The l2 gap (0.093023 vs 0.093058, about 3.5e-5) is far narrower than the plain one (0.285714 vs 0.286504, about 7.9e-4), and Balogh-Clemen-Lidický solved the l2 tetrahedron problem exactly, so the l2 version of K4^- may be the nearer target.
- Use the published lpsdp solver (github.com/BLL4/lpsdp) and certificates as warm starts. The K4^- run already used 8-vertex flags (Table 3 of arXiv:2610.33850), so a gain probably needs extra valid constraints (for example degree or stationarity conditions), not a rerun of the same 8-vertex SDP.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- erdosproblems.com/794 discusses 2/9 vs 2/7; the conjectured density is 2/7 (Frankl-Füredi). Do not compare against 2/9.
- A construction exactly at 2/7 (the Frankl-Füredi iterated blow-up of the (6,3,2)-design, conjectured to be the unique extremal configuration) is not a win.
- 0.286504 and 0.093058 are rounded figures. A bound between the rounded figure and the certificate's exact value is not an improvement, so read the exact value from the certificate files.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/turan-k4-minus-3-graph-density.md
```

Already set up? Say `run V3R1T4S on turan-k4-minus-3-graph-density`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `turan-k4-minus-3-graph-density`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
