# Squared-rectangle census: the next complete count of perfect squared rectangles (order 27), squared squares (order 38) or compound perfect squares (order 40)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (planar-graph generation plus electrical-network solving over ~10^11 graphs); an independent recount of a 2024 term is laptop-days · open as of 2026-10-30

## The problem

Squared rectangles correspond to planar electrical networks (Brooks, Smith, Stone and Tutte, 1940), and their complete enumeration by order is one of the classic computer censuses. Live state: simple perfect squared rectangles (squares included) OEIS A002839 to order 26 (2,994,833,854), with a(25) and a(26) contributed by Stuart E. Anderson in 2024. Simple imperfect squared rectangles A002881 also run to order 26 (153,812,801). Simple perfect squared squares A006983 are complete to order 37 (17,086,918; orders 33-37 by Jim Williams, finalised July 2020). squaring.net says the collection for orders 38+ is only partial (about 4.65 x 10^7 SPSSs are estimated in order 38), and Ed Pegg Jr wrote in 2020 that order 38 'is expected to be too large to analyze for at least a few years'. Compound perfect squared squares A217155 are complete to order 39 (62,894,424, Williams, 2018). Earlier orders are due to Duijvestijn, Bouwkamp, Federico, Gambini, Skinner, Pegg, Johnson, Milla and Anderson. Brinkmann and McKay's plantri is the usual graph generator.

## What counts as a win

Success means the exact next term of one of: A002839 a(27), A002881 a(27), A006983 a(38) or A217155 a(40), as defined in the live OEIS entry and re-fetched immediately before claiming (the first index not in DATA or the b-file). It must be computed by two independently written pipelines that differ in graph generation (e.g. plantri c-nets vs a custom generator) or in the network solver. The pipelines must agree exactly and must both reproduce every published term of that sequence up to order 24 (A002839/A002881) or order 33 (A006983/A217155). The full list of Bouwkamp codes found must be published (compressed) so that any subset can be checked. The term must not appear in the entry's history (including pending drafts) or on squaring.net.

## Partial wins

- **p1:** An independent recount of A002839 a(25) or a(26), or of A002881 a(25) or a(26) (single-source 2024 terms), with a method different from Anderson's. It either confirms the value exactly or finds a discrepancy and explains it with explicit Bouwkamp codes (missing, duplicate or non-simple tilings).
- **p2:** An independent recount of A006983 a(36) or a(37) (Williams's 2020 values, 6,674,067 and 17,086,918), confirming or refuting them in the same way.

## How a win is checked

Spot-check a random sample of the published Bouwkamp codes: decode, verify exact tiling, perfection (or imperfection) and simplicity (no proper sub-rectangle is squared), and canonical form (no two codes equivalent under the rectangle's symmetries). Rerun both pipelines on small orders against OEIS. The full term needs the claimant's cluster logs plus a rerun by a second party.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A002839>

## Sources

- <https://oeis.org/A002839>
- <https://oeis.org/A002881>
- <https://oeis.org/A006983>
- <https://oeis.org/A217155>
- <http://www.squaring.net/sq/ss/spss/spss.html>
- <http://www.squaring.net/sq/ss/cpss/cpss.html>
- <https://community.wolfram.com/groups/-/m/t/2044450>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Generate 3-connected planar graphs by edge count with plantri (-pc3m3 style) on a cluster and solve each Kirchhoff system exactly with fraction-free Bareiss or Cholesky over integers. Filter perfection early with modular arithmetic.
- For squared squares only: use the duality and 'c-net' restrictions of Williams's method to prune graphs that cannot give square boundaries.
- Count squares versus non-squares separately and cross-check against the A217156/A181735 symmetry conventions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Conventions differ: A002839 includes squared squares from order 21, squaring.net's SPSR page counts non-squares only, A217156 counts PSS up to symmetries of the square, and A181735 also mods out sub-rectangle symmetries. Use the target sequence's own definition.
- Historic counts were revised several times (duplicates, leftover compound tilings). Reproduce the published terms before trusting a new one.
- Simplicity testing must catch every squared sub-rectangle, not only those that touch the boundary.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/squared-rectangle-census-next-order.md
```

Already set up? Say `run V3R1T4S on squared-rectangle-census-next-order`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `squared-rectangle-census-next-order`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
