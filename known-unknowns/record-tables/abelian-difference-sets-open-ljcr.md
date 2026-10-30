# Abelian difference sets: settle an 'Open' group entry with v <= 1000 in Gordon's La Jolla Difference Set Repository

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★☆☆☆☆ · compute: laptop-hours to laptop-days (orbit-restricted exact searches; character-sum and field-descent computations) · open as of 2026-10-30

## The problem

A (v,k,lambda) difference set in an abelian group G of order v is a k-subset D such that every non-identity element is a difference d - d' (d, d' in D) in exactly lambda ways. Daniel Gordon's La Jolla Difference Set Repository (dmgordon.org/difference-sets; data file ds.json in github.com/dmgordo/difference-sets, last commit 2026-04-24; site updated 2026-09-03) lists every parameter set with v < 100000 passing the counting, Schützenberger and Bruck-Ryser-Chowla tests, for each abelian group, with status Yes, All, No or Open. At this check ds.json held 1,085,783 group entries, 102,719 of them Open; 106 Open entries (51 parameter sets) have v <= 1000. The smallest include the Paley-Hadamard parameters (243,121,60) in Z3 x Z9 x Z9 and (343,171,85) in Z7 x Z49; the Menon parameters (400,190,90) in Z10 x Z40, Z20 x Z20 and Z2 x Z10 x Z20; (416,166,66), (425,160,60) and (448,150,50) in several groups; and the cyclic cases (465,145,45), (469,208,92), (639,232,84), (703,325,150), (741,185,46), (781,300,115), (910,405,180), (921,161,28), (936,375,150), (944,369,144), (963,222,51), (981,196,39) and (990,345,120). Settling an entry needs a new construction or a nonexistence argument beyond the Turyn self-conjugacy, Lander and Schmidt field-descent results the repository already applies. Gordon's circulant weighing matrix, signed and relative difference set repositories belong to the separate circulant-weighing-matrices-open entry.

## What counts as a win

Success means, for an entry DS(v,k,lambda,G) with v <= 1000 whose status is 'Open' in the live ds.json (re-downloaded from github.com/dmgordo/difference-sets immediately before claiming), either (a) an explicit k-subset D of G, written in the group's invariant-factor coordinates, such that every non-identity element of G arises exactly lambda times as d - d' with d, d' in D, checked by two independent programs, or (b) a nonexistence proof for that group whose computational part (character sums, field descent, exhaustive search or a DRAT/LRAT certificate) the skeptic re-runs; and in both cases a fresh arXiv search shows the entry is not already settled in the literature, including by Menon-Turyn product theorems, Davis-Jedwab recursive constructions or Schmidt's 2026 Gauss-type Hadamard difference sets (arXiv:2609.07088) (direction: none; existence target).

## Partial wins

- **p1:** The same for an 'Open' entry with 1000 < v < 100000, after checking that it does not follow from a known product or recursive theorem (the repository has not applied all of them at large v; see pitfalls).

## How a win is checked

Parse G from the entry name (invariant factors, e.g. [3,9,9], or the entry's G_rep if given) and represent elements as tuples modulo the factors. For a claimed D check |D| = k, tally all k(k-1) differences and require every non-identity element to appear exactly lambda times; cross-check with |chi(D)|^2 = k - lambda for every nontrivial character, computed exactly in a cyclotomic field or numerically with a rounding margin next to the exact tally. Use two independent programs; ds_code.py may be read for conventions, never executed. For nonexistence claims re-run every computational step and check each cited theorem's hypotheses.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/dmgordo/difference-sets/blob/main/ds.json>

## Sources

- <https://dmgordon.org/difference-sets/>
- <https://github.com/dmgordo/difference-sets>
- <https://github.com/dmgordo/difference-sets/blob/main/ds.json>
- <https://arxiv.org/abs/2609.07088>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Multiplier theorems (Hall and its abelian-group versions): where a prime p dividing n = k - lambda qualifies as a numerical multiplier, D can be taken as a union of orbits of x -> p x, turning the search into a small exact cover.
- Automate character-sum and field-descent nonexistence tests over every Open group with v <= 1000, as Tan did for circulant weighing matrices; an entry marked Open may fall to a sharper bound.
- Paley-Hadamard entries (4n-1, 2n-1, n-1) in non-elementary abelian p-groups (243 in Z3 x Z9 x Z9, 343 in Z7 x Z49): try cyclotomic and Galois-ring constructions, or prove exponent bounds.
- Menon entries (400, 576, 676, 784, 900): combine building sets with the Davis-Jedwab recursive framework, or prove exponent bounds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The repository lags theory at large v: DS(2304,1128,552) in Z4 x Z4 x Z12 x Z12 is Open in ds.json but follows from the Menon-Turyn product theorem applied to (16,6,2) in Z4 x Z4 and (144,66,30) in Z12 x Z12. Such entries are corrections to report, not wins.
- Status is per group: a difference set with the same parameters in another group of order v does not settle the entry.
- Signed, relative and circulant-weighing objects belong to the separate circulant-weighing-matrices-open entry.
- Most small Open entries have resisted decades of work; budget accordingly and prefer automated nonexistence sweeps to blind search.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/abelian-difference-sets-open-ljcr.md
```

Already set up? Say `run V3R1T4S on abelian-difference-sets-open-ljcr`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `abelian-difference-sets-open-ljcr`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
