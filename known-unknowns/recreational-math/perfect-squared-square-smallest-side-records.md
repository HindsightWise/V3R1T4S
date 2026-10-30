# Perfect squared squares: smaller side than the best known for an order 38..59 (OEIS A217148 table and squaring.net listings), or a nicer or more odd-sided record square

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (targeted planar-network search; no exhaustive census needed) · open as of 2026-10-30

## The problem

A perfect squared square (PSS) tiles a square with integer squares of pairwise distinct sizes, and its order is the number of squares. The smallest side for each order is known exactly for orders 21..37 (OEIS A217148 for all PSS, A129947 for simple ones). These values come from complete enumerations by Duijvestijn, Gambini, Skinner, Anderson, Pegg, Johnson, Milla and, for orders 33..37, Jim Williams (2014-2020). For orders 38..59 only upper bounds are known. A217148 lists them (Williams for 38 and 40-44, Ian Gambini's 1999 thesis for 39 and 45-47, the rest as tabulated): 38: 352, 39: 360, 40: 328, 41: 336, 42: 360, 43: 413, 44: 425, 45: 543, 46: 601, 47: 691, 48: 550, 49: 583, 50: 644, 51: 636, 52: 584, 53: 685, 54: 657, 55: 631, 56: 751, 57: 742, 58: 780, 59: 958. The table dates from 2013 and is stale in places. squaring.net's per-order SPSS tablecode files hold Bernard Moss's 2020 squares of order 58 with side 628 and of order 59 with side 887 (tilings re-checked 2026-10-30), below the table's 780 and 958. For orders 45-57 the smallest listed SPSS is above the table value. The non-monotone values (40 < 38, 52 < 50) show how soft the larger ones are. Stuart Anderson's 'Special' PSS page (squaring.net, items up to September 2026) also records other properties. The nicest SPSS (smallest ratio of largest to smallest element) is 2456/333 = 7.375 (order 36, side 7743, Williams 2020), and no PSS of order <= 37 does better. Among the completely enumerated SPSS orders (up to 37), the fewest even-sided elements is 6 (three SPSSs: two of order 26, one of order 34). The page asks whether 3 or 2 is possible, as it is for rectangles.

## What counts as a win

Success means an explicit perfect squared square (Bouwkamp code or (x, y, s) list) of order n, with 38 <= n <= 59, all n squares of pairwise distinct integer sizes and tiling exactly, whose side is STRICTLY less than the best known side for that n. The best known side is the smaller of the upper bound in the live A217148 table (re-fetched immediately before claiming) and the smallest PSS of that order in squaring.net's listings: the 'Special' PSS page, the per-order SPSS and CPSS pages and Bouwkamp-code/tablecode downloads, and Bernard Moss's 2018-2020 collections for orders 37-116. As of 2026-10-30 this makes the bar 628 for order 58 and 887 for order 59 (Moss 2020), not the table's 780 and 958. Simple or compound both count. The side must also be smaller than any value in a later OEIS edit.

## Partial wins

- **p1:** A perfect squared square of any order whose largest-to-smallest element ratio is strictly less than 2456/333 (the niceness record on squaring.net's 'Special' PSS page, Jim Williams 2020), verified exactly.
- **p2:** A perfect squared square of any order with at most 5 even-sided (reduced) elements. The fewest recorded on squaring.net is 6 (three SPSSs up to order 37), and the page asks whether 3 or 2 is possible. Verified exactly.

## How a win is checked

Decode the Bouwkamp code, check exact coverage of the s x s square, check pairwise distinct sizes and count the order. Compare the side with A217148's table entry, compute the ratio or the even-element count exactly. This takes milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A217148>

## Sources

- <https://oeis.org/A217148>
- <https://oeis.org/A129947>
- <http://www.squaring.net/sq/ss/s-pss.html>
- <https://community.wolfram.com/groups/-/m/t/2044450>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Small sides need c-nets with small spanning-tree count. Generate planar graphs of the right order with low complexity (few spanning trees) and solve only those.
- Build compound squares by gluing two small perfect squared rectangles with complementary aspect and a few connecting squares (Moroń/Willcocks style), then search the gluing space.
- For the even-element question: work mod 2 on the Kirchhoff currents to precompute which c-nets can give few even elements before solving exactly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A217148 (all PSS) and A129947 (simple only) differ in DATA at order 33 (233 vs 223), and their 38..59 tables differ from order 48 on. Use A217148's table for this target.
- Bouwkamp codes give sizes in reduced form. A PSS whose element sizes share a factor must be divided down before comparing sides.
- The table entries are upper bounds from different people, and squaring.net holds millions of post-2013 squares (Moss's transforms for orders 48-85, Anderson's substituted CPSSs for orders 41-60). Check those listings and the OEIS history for a smaller side before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/perfect-squared-square-smallest-side-records.md
```

Already set up? Say `run V3R1T4S on perfect-squared-square-smallest-side-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `perfect-squared-square-smallest-side-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
