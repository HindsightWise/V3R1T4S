# 2D irregular strip packing (nesting, ESICUP and Gardeyn instances): a shorter strip than a record in sparrow's live records folder

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (multi-core helps; the records came from 20-minute 16-core runs and longer record hunts) · open as of 2026-10-30

## The problem

Irregular strip packing (nesting): place every copy of a set of polygons, using only each item's allowed rotations, without overlap in a strip of fixed height, and make the strip as short as possible. The classic benchmarks (albano, blaz1 = shapes2, dagli, fu, jakobs1/2, mao, marques, shapes0/1, shirts, swim, trousers) come from 1980s-2000s papers and are kept in the ESICUP datasets repository (github.com/ESICUP/datasets, moved from euro-online.org in 2025). For about ten years the best layouts came from Leung et al. 2012, Elkeran 2013, Wang et al. 2017 and Sato et al. 2019. Jeroen Gardeyn, Greet Vanden Berghe and Tony Wauters (KU Leuven) then released the open-source sparrow heuristic (arXiv:2509.13329, v4 6 Oct 2026), which beats or ties every previous best density (swim 75.94% to 79.83%, shirts 88.96% to 90.92%), plus ten real-world instances gardeyn0-9. The repository's data/records folder keeps the best layouts as exact SVGs and is maintained: on 2026-10-06 the maintainer merged refinements by Touko Ursin (Helios One; PR #175) that shortened gardeyn0/2/4/5/6 and shapes0. Record lengths (strip height) on 2026-10-30: albano 9692.056 (4900), blaz1 25.049 (15.0015), dagli 56.087 (60), jakobs1 10.980 (40.004), mao 1696.802 (2550), marques 75.176 (104), shapes0 56.996 (40.004), shirts 59.393 (40), swim 5541.653 (5752), trousers 235.172 (79), gardeyn0 48629.967 (20000), gardeyn1 16181.270 (20000), gardeyn2 47305.935 (10000), gardeyn3 60397.832 (20000), gardeyn4 4724.856 (1500), gardeyn5 4301.942 (2000), gardeyn6 17037.131 (3990), gardeyn7 5067.831 (1524), gardeyn8 48718.980 (20000), gardeyn9 65.793 (44). fu, jakobs2 and shapes1 are left out: there sparrow only ties the older literature. The paper claims no optimality and expects large gains on gardeyn4, 5 and 7.

## What counts as a win

For one of the 20 instances listed in the statement (not fu, jakobs2 or shapes1), a layout that places every item copy listed in https://github.com/JeroenGar/sparrow/tree/main/data/input/ < name > .json (same polygons, same demands, only the rotations that file allows, no mirroring) inside a strip whose height equals that file's strip_height, with every item inside the strip and pairwise disjoint item interiors (touching allowed). Its strip length must be STRICTLY SHORTER (direction: min) than the container width of data/records/final_best_ < name > .svg, read from the container path 'M0,0 L < w > ,0' (not the rounded footer text), re-fetched immediately before claiming; if the file has been replaced since 2026-10-30, the new value is the bar. If any published layout for that instance, at a strip height no greater than that strip_height, is shorter still, the claim must beat it too. Feasibility is judged by an independent exact checker, not by the generating heuristic.

## Partial wins

- **p1:** For blaz1, jakobs1 or shapes0, a layout in the ORIGINAL ESICUP strip height (15, 40, 40 respectively) whose length is at most the live record length in data/records (whose records use sparrow's 0.01%-inflated height), passing the exact checker. The stored records are only claimed at the inflated height (the shapes0 one is stated to be invalid at height 40), so this would be a new best at the original height.
- **p2:** For any gardeyn0-gardeyn9 instance, a layout that passes the exact checker and is within 0.5% of the live record length, found from scratch (no published layout used as a start) by code other than sparrow, released with the command and seed so that a rerun reproduces it.
- **p3:** For any of albano, dagli, mao, marques, shirts, swim or trousers, a layout that passes the exact checker and is within 0.1% of the live record length, found from scratch (no published layout used as a start) by code other than sparrow, released with the command and seed so that a rerun reproduces it.

## How a win is checked

Parse the claimed layout (sparrow-format SVG or JSON: item id, rotation, translation) and rebuild each placed polygon from data/input/ < name > .json. Check the item multiset against the demands and each rotation against the allowed set. Check containment in [0, L] x [0, strip_height] and pairwise interior-disjointness in exact rational arithmetic (Python fractions on the decimal coordinates exactly as written, after rotating by the allowed multiples of 90 degrees, which are exact; segment-intersection and point-in-polygon tests; touching boundaries allowed, positive-area overlap not). Compare L with the container-path width of the live final_best_ < name > .svg. For p2/p3, rerun the released code with the stated seed and check its output the same way. A few hundred lines of independent code; seconds per layout.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/JeroenGar/sparrow/tree/main/data/records>

## Sources

- <https://github.com/JeroenGar/sparrow/tree/main/data/records>
- <https://github.com/JeroenGar/sparrow/tree/main/data/input>
- <https://arxiv.org/abs/2509.13329>
- <https://github.com/JeroenGar/sparrow/blob/main/data/experiments/README.md>
- <https://github.com/JeroenGar/sparrow/pull/175>
- <https://github.com/JeroenGar/sparrow/discussions/174>
- <https://github.com/ESICUP/datasets/tree/main/2d_irregular>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the published record SVGs and run long compaction or overlap-minimisation searches (sparrow's own strategy splits the work into a series of feasibility problems at shrinking lengths). The gardeyn instances have hundreds of items and the newest records, so they are the likeliest to have slack.
- Exact feasibility at a fixed length for small instances (shapes, jakobs, blaz1) via no-fit-polygon MIP or dotted-board models, to test whether the record length can be pushed down by a provable step.
- Cross-domain import from rigid-body physics (gravity-and-shake compaction with collision resolution) and from the strip-packing 'squeaky wheel' and guided local search literature (Egeblad-Nielsen-Odgaard, Umetani et al.).
- Separation: sparrow keeps a tiny positive gap between items, but exact touching is allowed in the classical problem, so closing those gaps under an exact checker can shave length on high-density instances.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Strip-height inflation: sparrow's input files raise the ESICUP height by 0.01% for blaz1, fu, jakobs1, jakobs2, shapes0 and shapes1 (e.g. 40.004 instead of 40). Densities printed in the SVGs use the inflated height, the paper's Table 3 uses the original one (89.247% vs 89.26% for jakobs1). Compare strip lengths at a stated height, never densities across conventions.
- Footer rounding: the SVG footer prints 3 decimals (jakobs2 shows 22.000 while the container is 22.000465). Use the container path value.
- fu, jakobs2 and shapes1 are excluded: sparrow only ties Elkeran 2013 / Sato 2019 there, those older layouts at the original height may already be shorter than the inflated-height records, and these small integer-coordinate instances may be at or near optimal.
- Rounding: the record coordinates are written at full f64 precision and the refined layouts sit about 1e-6 apart; re-serialising with fewer digits (or reading as f32) creates tiny overlaps that a tolerant floating-point or buffered Shapely test will miss. Check exactly.
- Rotations vary by instance (shapes0 allows only 0, several only 0/180); a forbidden orientation or a reflected item is infeasible.
- Literature versions of some instances (swim, shirts, trousers) differ slightly in vertex data. Use the polygons in sparrow's data/input, which the records refer to, and say so.
- The records folder changes (six records replaced on 2026-10-06 by an outside contributor). Re-fetch before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/esicup-nesting-sparrow-strip-length-records.md
```

Already set up? Say `run V3R1T4S on esicup-nesting-sparrow-strip-length-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `esicup-nesting-sparrow-strip-length-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
