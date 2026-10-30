# Lebesgue's universal covering problem (C13b): a certified lower bound above 0.8344 or a convex cover below 0.8440935944

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (rigorous branch-and-bound over placements of a few diameter-1 sets) · open as of 2026-10-30

## The problem

C13b is the least area of a convex set that contains a congruent copy of every planar set of diameter 1 (Lebesgue 1914). It suffices to cover all sets of constant width 1 (Vrećica 1981). Upper bounds: Pál 1920 (2 - 2/sqrt3 = 0.8452994616), Sprague 1936 (0.844137708436), Hansen 1992, Baez-Bagdasaryan-Gibbs 2015 (0.844115297128419..., computer-assisted, numerics checked by Greg Egan), and Philip Gibbs 2018, arXiv:1810.10089 (only version v1), 0.8440935944, still the best. Lower bounds: Elekes 1994 (0.8257, 0.8271), then Brass and Sharifi 2005, 0.832, by a rigorous computer search with a disk, an equilateral triangle and a regular pentagon. Three unrefereed 2026 preprints raise the lower bound. Niantao Xie, arXiv:2606.04458 (v4, 8 Jul 2026), certifies 0.833 in the Brass-Sharifi framework. Shuai Zeng, arXiv:2609.01284 (1 Sep 2026), certifies 0.834 with an outward-rounded interval certificate on a regular Reuleaux subtest. Ujjwal Mishra, arXiv:2608.30538 (v2, 1 Sep 2026), certifies 0.8344 with a disc, a Reuleaux triangle and a Reuleaux pentagon. He uses an erosion reduction and an exhaustive subdivision certificate of 486,799,600 nodes checked by a separate verifier. He also shows that the disk/triangle/pentagon family admits a placement with hull area below 0.8336, so it cannot reach 0.8344. Tao's optimisation-constants page 13b (which notes a 2025 paper, arXiv:2512.04023, on asymptotic and higher-dimensional variants only) and Wikipedia still list 0.832 and 0.8440935944.

## What counts as a win

(A) A finite family of planar sets of diameter 1 (polygons with exact vertices, disks, Reuleaux polygons or other exactly described sets) and a re-runnable rigorous certificate that every convex set containing congruent copies of all of them has area at least L. The certificate is outward-rounded interval arithmetic or exact arithmetic over a finite subdivision of the relative placements, including rotations and reflections, or a formal proof. L must be STRICTLY GREATER (direction: max) than the best lower bound on https://teorth.github.io/optimizationproblems/constants/13b.html and than every certified lower bound found by a fresh literature check at verification time (0.8344, Mishra arXiv:2608.30538, on 2026-10-30). Or (B) an exactly described convex set of area STRICTLY LESS (direction: min) than the best upper bound listed there and found by a fresh check (0.8440935944 on 2026-10-30), with a machine-checked proof that it is a universal cover for diameter-1 sets, or a complete written proof whose computational steps are re-runnable in exact or interval arithmetic.

## Partial wins

- **p1:** An independent rigorous replay of one of the 2026 lower-bound certificates (Mishra 0.8344, arXiv:2608.30538; Zeng 0.834, arXiv:2609.01284; or Xie 0.833, arXiv:2606.04458) in a separate checker with outward-rounded interval or exact arithmetic, published as a re-runnable replay note that confirms the bound or reports a defect.
- **p2:** An independent exact or interval-arithmetic re-verification of Gibbs's 2018 preprint bound 0.8440935944 (area computation and the covering argument's numeric steps), published as a replay note that confirms it or reports an error.

## How a win is checked

(A) Check each set's diameter exactly. Re-run the certificate: the subdivision must cover the full compact space of relative placements (justify the compactness reduction), each cell carrying a rigorous lower bound on the area of the convex hull of the placed sets that is at least L. (B) Build any formal proof from source; otherwise referee the reduction and re-run each numeric step with interval arithmetic. Compute the cover's area exactly. Re-fetch Tao's 13b page.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/13b.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/13b.html>
- <https://arxiv.org/abs/2608.30538>
- <https://arxiv.org/abs/2609.01284>
- <https://arxiv.org/abs/2606.04458>
- <https://arxiv.org/abs/1810.10089>
- <https://arxiv.org/abs/1502.01251>
- <https://en.wikipedia.org/wiki/Lebesgue%27s_universal_covering_problem>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The disk/triangle/pentagon family is capped below 0.8336 (Mishra), and Mishra already swapped in Reuleaux triangle and pentagon for 0.8344. The next push is a fourth set (a Reuleaux heptagon, a regular 3^j-gon as in Elekes, or another constant-width body), certified with modern interval branch-and-bound.
- Pick the extra shapes by first solving the numerical min-hull-area problem for candidate families, then certify only the best family.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Numerical optimisation over placements gives no lower bound; only a rigorous cover of the whole placement space does.
- Reflections are allowed in Lebesgue's problem (congruent copies); a certificate that ignores reflected placements proves nothing.
- The upper bounds differ in the 7th decimal; compute areas exactly or with certified intervals, never in double precision alone.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/lebesgue-universal-cover-bounds.md
```

Already set up? Say `run V3R1T4S on lebesgue-universal-cover-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `lebesgue-universal-cover-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
