# Tight 5-cycle C5^(3) (Mubayi-Rödl conjecture): a certified upper bound on pi(C5^(3)) below 0.46503, or a C5^(3)-free construction above 2*sqrt(3)-3

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: needs cluster (6- and 7-vertex 3-graph flag-algebra programs; certificate checking is laptop-hours) · open as of 2026-10-30

## The problem

C5^(3) is the tight 3-uniform cycle on five vertices (edges 123, 234, 345, 451, 512). Mubayi and Rödl (JCTA 2002) gave a recursive construction of density 2*sqrt(3)-3 = 0.464101 and conjectured it is optimal. Kamčev, Letzter and Pokrovskiy proved that 2*sqrt(3)-3 is the Turán density of the tight cycle C_l^(3) for all sufficiently large l not divisible by 3, but C5 itself remains open. Flagmatic 2.0 (Vaughan) gave 0.46829; Lidický and Volec (arXiv:2610.33850, 24 Oct 2026) improved this to 0.46503 by solving the 7-vertex program with CSDP (pi(C5) <= 0.465031, on a machine with about 2 TB RAM; their LP cutting-plane method alone gives 0.46507), certificates at lidicky.name/pub/lpsdp/. In the codegree-squared (l2) setting the same paper has 0.25194 (lower, Balogh-Clemen-Lidický) against 0.252451 (upper). Open as of 2026-10-30.

## What counts as a win

Success means EITHER (a) a certified proof that pi(C5^(3)) <= U with U STRICTLY LESS (direction: min) than 0.46503 and than any smaller bound in a fresh check of arXiv:2610.33850 (latest version) and papers citing it, delivered as a flag-algebra certificate with exact rational or rigorous interval PSD verification that an independent checker re-runs, or as a compiling Lean 4 proof; OR (b) an explicit C5^(3)-free construction (finite pattern with optional recursion, written freeness proof) with exactly computed limiting density STRICTLY GREATER (direction: max) than 2*sqrt(3)-3, refuting the Mubayi-Rödl conjecture.

## Partial wins

- **p1:** Codegree-squared version: a certified upper bound on pi_l2(C5^(3)) strictly below 0.252451, or a C5^(3)-free construction with limiting normalised codegree-squared sum strictly above 0.25194, to the main criterion's standard.
- **p2:** A complete Lean 4 proof (no sorry, no new axioms) of pi(C5^(3)) <= U for some U strictly below 0.46829 (Flagmatic 2.0), provided no Lean-formalised bound of that strength is public at claim time.

## How a win is checked

Independently enumerate all C5^(3)-free 3-graphs on the certificate's vertex count up to isomorphism, recompute flag densities and products, verify PSD matrices exactly or by interval Cholesky, and check the inequality on every graph. For constructions, check C5^(3)-freeness of the pattern by brute force over all maps of the 5 cycle vertices, verify the recursive argument, and compute the density symbolically. Re-fetch arXiv:2610.33850.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.33850>

## Sources

- <https://arxiv.org/abs/2610.33850>
- <https://arxiv.org/html/2610.33850v1>
- <https://lidicky.name/pub/lpsdp/>
- <https://arxiv.org/abs/2108.10406>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not confuse C5^(3) with C5^- (tight 5-cycle minus an edge), whose density 1/4 is already known (see arXiv:2409.14257 for the related tight-cycle-minus-an-edge results).
- The 0.46503 value (0.465031 unrounded) comes from the CSDP computation, whose files are in anc_lpsdp_csdp.tar.gz rather than in the lpsdp certificates; read that archive before quoting it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/turan-tight-5-cycle-3-graph-density.md
```

Already set up? Say `run V3R1T4S on turan-tight-5-cycle-3-graph-density`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `turan-tight-5-cycle-3-graph-density`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
