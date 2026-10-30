# Moser's worm problem (convex covers, C13a): certify a lower bound above 0.239 or a rotation-only convex cover below 0.257883595

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (branch-and-bound over arc placements with interval arithmetic) · open as of 2026-10-30

## The problem

C13a is the smallest area of a convex region that contains a congruent copy (translation and rotation, no reflections) of every planar arc of length 1 (Moser's worm problem). Tao's optimisation-constants page 13a lists as best cover pi/12 = 0.2617993878, the 30-degree circular sector of radius 1 (Wetzel's sector), proved a cover by Panraksa and Wichiramala (2021), building on Movshovich and Wetzel (2017). Earlier covers: Wang 2006 (0.270911861), Norwood-Poole-Laidacker 1992, Gerriets-Poole 1974. Three unrefereed 2026 preprints go lower, and the page lists none of their covers. Wichiramala and Panraksa, arXiv:2606.14625 (12 Jun 2026), give a scaled 30-60-90 triangle of area 0.260956.... Zhipeng Deng, arXiv:2609.04591 (v1, 4 Sep 2026), gives an isosceles triangle of area 0.257883595... with exact rational certificates and reported Lean code. The triangle is mirror-symmetric, so it covers without reflections if it covers with them. Ethan Keller, arXiv:2609.21968 (v1, 18 Sep 2026), lets reflections count as congruent copies and proves 0.239 <= alpha <= 0.2463322372. The lower bound uses four polygonal unit arcs and a finite subdivision certificate, the proof is reported as formalised in Lean 4, and the bound also holds for the rotation-only problem. The upper bound is a convex quadrilateral without mirror symmetry whose proof uses reflections, so it is not shown to cover without them. Tao's page 13a lists 0.239 with an asterisk (author-reported formalisation, no independent replay recorded). Earlier lower bounds: 0.23743658 (Lech Mazur, unrefereed, ProofAtlas, Sep 2026), 0.232239 (Khandhawit, Pagonakis and Sriswasdi 2013) and 0.227498 (Khandhawit and Sriswasdi 2009). Non-convex covers (Ploymaklam-Wichiramala 0.26007) are a different problem.

## What counts as a win

(A) A finite family of arcs of length exactly 1 (polygonal with exact rational or algebraic vertices, or explicitly parametrised) and a re-runnable certificate (a finite subdivision of the space of relative placements with rigorous interval-arithmetic or exact area bounds, or a Lean/Isabelle/Coq proof) that every convex set containing a translated and rotated copy of each arc has area at least L, with L STRICTLY GREATER (direction: max) than the best lower bound on https://teorth.github.io/optimizationproblems/constants/13a.html and in a fresh check at verification time (0.239 on 2026-10-30). Or (B) a convex set whose area is STRICTLY LESS (direction: min) than that of every convex cover listed there or claimed in a paper or preprint found by a fresh literature check, counting only covers valid without reflections; a mirror-symmetric cover proved with reflections allowed counts. On 2026-10-30 the bar is 0.257883595 (Deng's triangle, arXiv:2609.04591). It needs a machine-checked proof that the set contains a translated and rotated copy of every unit arc. If Keller's 0.2463322372 quadrilateral (or another cover) is later shown to cover without reflections, it becomes the bar. The convention on reflections must match the status page.

## Partial wins

- **p1:** A certified lower bound of at least 0.239 obtained with at most three arcs, with a re-runnable certificate.
- **p2:** An independent replay of Keller's certificate (arXiv:2609.21968) in a separate checker (for example, interval arithmetic in a different language, or rebuilding the Lean development from source with the kernel check logged), published as a replay note that confirms it or reports a defect.

## How a win is checked

(A) Check each arc's length exactly. Re-run the subdivision certificate: every cell of the placement space must carry a rigorous lower bound on the convex-hull area of the placed arcs that is at least L, computed with outward-rounded interval arithmetic or exact arithmetic, and the cells must cover the whole compact placement space (check the reduction to a compact space separately). For Lean, build from source and confirm the theorem statement matches the definition, with no axioms beyond the standard ones. (B) Build and check the formal proof; compute the area exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/13a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/13a.html>
- <https://arxiv.org/abs/2609.21968>
- <https://arxiv.org/abs/2609.04591>
- <https://arxiv.org/abs/2606.14625>
- <https://en.wikipedia.org/wiki/Moser%27s_worm_problem>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Add a fifth or sixth arc to Keller's family (zigzags, near-semicircles, broadworms) chosen to maximise the minimum hull area found by numerical optimisation, then certify only the winning family.
- Use the Khandhawit-Pagonakis-Sriswasdi reduction (fix one arc, parametrise the others by angle and offset) and spend the compute on adaptive subdivision near the minimising placements.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Reflections: Keller's paper allows reflected copies and the status page does not. A lower bound proved with reflections allowed also holds without them, but a cover proved with reflections allowed (Keller's 0.24633 quadrilateral) is not a rotation-only cover unless it is mirror-symmetric or is shown separately.
- A machine-checked proof that Keller's quadrilateral (or another set below the bar) covers every unit arc using rotations and translations only would count for (B); replaying Keller's reflection-allowed proof does not.
- Tao's page does not list the 2026 triangle covers. The bar for (B) is Deng's 0.257883595 isosceles triangle (arXiv:2609.04591), not pi/12.
- Numerical (non-rigorous) minimisation over placements gives an upper estimate of the hull-area minimum, not a lower bound.
- Non-convex covers are a separate problem and do not count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/moser-worm-convex-cover-bounds.md
```

Already set up? Say `run V3R1T4S on moser-worm-convex-cover-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `moser-worm-convex-cover-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
