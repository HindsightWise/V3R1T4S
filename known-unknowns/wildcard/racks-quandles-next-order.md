# Racks and quandles: count those of order 14 (OEIS A181770/A181769), or the connected quandles of order 48 (A181771)

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days for the kei and representative-list partial wins; racks or quandles of order 14, and connected quandles of order 48 over the full degree-48 transitive-group library, likely need a cluster · open as of 2026-10-30

## The problem

Racks and quandles are set-theoretic solutions of the Yang-Baxter equation, and quandles give knot invariants. Petr Vojtechovsky and Seung Yeop Yang (Math. Comp. 88 (2019) 2523-2540, arXiv 1911.04991) enumerated racks and quandles of order n <= 13 up to isomorphism: 25,794,670,618 racks and 469,250,886 quandles of order 13. Their method combined conjugacy classes of subgroups of small symmetric groups, the Joyce-Blackburn representation, and the Jedlicka-Pilitowska-Stanovsky-Zamojska-Dzienio enumeration of 2-reductive racks and quandles. They list representatives only for racks of order <= 11 and quandles of order <= 12; larger orders were counted only, and their Problem 6.1 asks for order 14. Kei (involutory quandles, A178432) are known to order 12 (6,926,801; Choiwah Chow, 2023). Connected quandles (A181771) are known for every order <= 47, from the libraries of transitive permutation groups: order < 36 by Leandro Vendramin (arXiv 1105.5341) and order < 48 by Alexander Hulpke, David Stanovsky and Petr Vojtechovsky (J. Pure Appl. Algebra 220 (2016) 735-758), with the library in Vendramin's Rig package. The transitive groups of degree 48 were classified later (Holt, Royle and Tracey, 2022). OEIS A181769, A181770, A178432 and A181771, re-fetched 2026-10-30, carry 'more' and stop at those orders.

## What counts as a win

Success means the exact value of A181769(14), A181770(14) or A181771(48), re-fetched live and still missing immediately before claiming. Two independent methods or codes must agree exactly, and the code must reproduce every published term of that sequence. For A181771(48), every connected quandle class must come from a transitive group of degree 48 with an explicit construction, plus a non-isomorphism check. A literature search (Vojtechovsky, Vendramin, Stanovsky and coauthors, arXiv 2019-2026) must find no earlier value.

## Partial wins

- **p1:** A178432(13), the number of kei (involutory quandles) of order 13, by code reproducing a(n) for n <= 12 and a second independent method agreeing.
- **p2:** An explicit representative list (canonical Cayley tables) of all racks of order 12 (836,395,102) or all quandles of order 13 (469,250,886), which Vojtechovsky and Yang counted but did not list. A checker must confirm the axioms, pairwise non-isomorphism by canonical form, and a total equal to the published count.

## How a win is checked

Check the axioms on any table in milliseconds. Rerun the counting code for small n against OEIS. For a new count, split by an isomorphism invariant (orbit structure of the displacement or operator group) and recompute random parts with independent code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A181769>

## Sources

- <https://oeis.org/A181769>
- <https://oeis.org/A181770>
- <https://oeis.org/A178432>
- <https://oeis.org/A181771>
- <https://arxiv.org/abs/1911.04991>
- <https://arxiv.org/abs/1105.5341>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Extend the Vojtechovsky-Yang subgroup-of-S_n method to n = 14: count conjugacy classes of subgroups of S_14 with the needed properties rather than listing every rack.
- For connected quandles of order 48, a connected quandle's inner automorphism group acts transitively, so filter the degree-48 transitive groups by Vendramin's criterion before constructing.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Racks vs quandles vs kei vs connected quandles are four different sequences with different offsets (A181771 starts at n = 1).
- Iso-classes of racks are not counted by orbits of the labeled count under S_n without care for automorphisms.
- The degree-48 transitive-group data is large; check that the whole library was processed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/racks-quandles-next-order.md
```

Already set up? Say `run V3R1T4S on racks-quandles-next-order`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `racks-quandles-next-order`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
