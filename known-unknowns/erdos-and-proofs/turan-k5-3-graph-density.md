# Turán's K5^(3) conjecture: a certified upper bound on pi(K5^(3)) below 0.757017, or a K5^(3)-free construction above 3/4

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: needs cluster (7-vertex 3-graph flag-algebra programs; certificate checking is laptop-hours) · open as of 2026-10-30

## The problem

pi(K5^(3)) is the Turán density of the complete 3-graph on 5 vertices. Turán conjectured 3/4, attained by Turán's and Sidorenko's constructions; Erdős offered $500 for any pi(K_k^(r)) with k > r > 2 (Erdős problem #712). For over a decade (since Flagmatic 2.0, 2013) the best upper bound was Vaughan's flag-algebra value 0.7696 (stated as 0.769533 in Balogh-Clemen-Lidický, arXiv:2108.10406). Lidický and Volec (arXiv:2610.33850, 24 Oct 2026) lowered it to 0.757017 with a new LP cutting-plane flag-algebra method, certified with MPFI interval arithmetic (certificates at lidicky.name/pub/lpsdp/), and say their runs were stopped before reaching optimality. The gap 0.75 to 0.757017 is open as of 2026-10-30.

## What counts as a win

Success means EITHER (a) a certified proof that pi(K5^(3)) <= U with U STRICTLY LESS (direction: min) than 0.757017 and than any smaller bound in a fresh check of arXiv:2610.33850 (latest version) and papers citing it, delivered as a flag-algebra certificate with exact rational or rigorous interval PSD verification that an independent checker re-runs, or as a compiling Lean 4 proof; OR (b) an explicit K5^(3)-free construction (finite pattern, optional recursion, written freeness proof) with exactly computed limiting density STRICTLY GREATER (direction: max) than 3/4.

## Partial wins

- **p1:** A complete Lean 4 proof (no sorry, no new axioms) of pi(K5^(3)) <= U for some U strictly below 0.769533 (Flagmatic 2.0, quoted as 0.7696 in arXiv:2610.33850 Table 2), provided no Lean-formalised bound of that strength is already public at claim time.

## How a win is checked

Independently enumerate all K5^(3)-free 3-graphs on n vertices up to isomorphism (for n <= 7), recompute flag densities and products, verify PSD matrices exactly or by interval Cholesky, and check the inequality on every graph. For constructions, brute-force K5^(3)-freeness of the pattern and compute the density symbolically. Re-fetch arXiv:2610.33850.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.33850>

## Sources

- <https://arxiv.org/abs/2610.33850>
- <https://arxiv.org/html/2610.33850v1>
- <https://lidicky.name/pub/lpsdp/>
- <https://www.erdosproblems.com/712>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The bound dropped by 0.0126 in one step, which suggests the 7-vertex program is far from exhausted; resume from the published lpsdp certificates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several non-isomorphic constructions at density 3/4 are known (Turán's, Sidorenko's and others); matching 3/4 is not a win.
- Bounds from 6-vertex flags are not known to beat 0.7696; the realistic route to any win is 7-vertex flags, starting from the published lpsdp certificates (the Lidický-Volec K5 run used about 350 GB RAM).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/turan-k5-3-graph-density.md
```

Already set up? Say `run V3R1T4S on turan-k5-3-graph-density`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `turan-k5-3-graph-density`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
