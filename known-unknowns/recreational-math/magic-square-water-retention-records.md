# Water retention of magic squares (Knecht): a normal magic square of order 10-15 retaining more water than the OEIS A201126 lower bounds, or better order 16-28, semi-magic and associative records

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Craig Knecht's topographical model treats a magic square as a height map. Pour water on it: a cell's water level is the minimum, over all orthogonal paths from the cell to the outer boundary, of the maximum height on the path, and water drains off the edge. Retention is the sum over cells of (level - height). OEIS A201126 gives the maximum retention of a normal magic square of order n: 0, 15, 69, 192, 418, 797, 1408 for n = 3..9. It lists the lower bounds a(10) >= 2267, a(11) >= 3492, a(12) >= 5185, a(13) >= 7445, a(14) >= 10397 and a(15) >= 14154. These come mostly from Al Zimmermann's spring 2010 Retaining Water contest (winner Walter Trump, second Hermann Jurksch), which set the known values for orders 4 to 28. Its final report (azspcs.com/Contest/MagicWater/FinalReport, loaded 2026-10-30) publishes the best square for each order. It gives 7442 for order 13, three below the OEIS bound, and for orders 16 to 28 it gives 18887, 24730, 31871, 40473, 50754, 62877, 77098, 93623, 112710, 134598, 159565, 187880 and 219822. This audit recomputed all 25 published squares (orders 4 to 28): each is a normal magic square whose retention equals its listed score. Related records: the semi-magic analogue A201127 (a(10) >= 2280, Hugo Pfoertner 2012); and the associative analogue A261798 (a(7) = 361, a(8) = 704, a(9) = 1247; a(11) >= 3226, a(12) >= 4840, a(13) >= 6972). For associative squares, OEIS states that no value above order 5 is proven maximal. See also Knecht, Trump, ben-Avraham and Ziff, PRL 108 (2012) 045703. This lane brute-forced all 7,040 normal 4 x 4 magic squares with orthogonal drainage and got a maximum of 15, which matches a(4) and confirms the drainage model.

## What counts as a win

A normal magic square of order n, for some 10 <= n <= 15 (entries 1..n^2, all rows, columns and both main diagonals summing to n(n^2+1)/2), whose water retention under the orthogonal-drainage model is strictly greater than the A201126 lower bound for that n at verification time.

## Partial wins

- **p1:** A normal semi-magic square of order 10 (rows and columns only) retaining at least 2281 units, beating A201127's a(10) >= 2280.
- **p2:** A normal associative magic square (a(i,j) + a(n+1-i, n+1-j) = n^2 + 1) of order 7, 8, 9, 11, 12 or 13 retaining strictly more than the A261798 value or lower bound for that order (361, 704, 1247, 3226, 4840, 6972).
- **p3:** A normal magic square of order n, 16 <= n <= 28, retaining strictly more water than the best score in the AZsPCs Retaining Water final report for that order (16: 18887, 17: 24730, 18: 31871, 19: 40473, 20: 50754, 21: 62877, 22: 77098, 23: 93623, 24: 112710, 25: 134598, 26: 159565, 27: 187880, 28: 219822), and strictly more than any larger value published for that order (OEIS or elsewhere) at verification time.

## How a win is checked

Check the entry set and the magic, semi-magic or associative conditions in exact integers. Compute retention with a priority-flood (Dijkstra-style) algorithm: seed the boundary cells at their own heights, propagate level = max(height, neighbour level) through the 4 orthogonal neighbours, and sum (level - height). Validate the implementation on all 4 x 4 magic squares (maximum 15) and on the best squares published in the AZsPCs Retaining Water final report, orders 4 to 28, each of which must reproduce its listed score exactly.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A201126>

## Sources

- <https://oeis.org/A201126>
- <https://oeis.org/A201127>
- <https://oeis.org/A261798>
- <https://doi.org/10.1103/PhysRevLett.108.045703>
- <http://azspcs.com/Contest/MagicWater/FinalReport>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Drainage is orthogonal only. With 8-neighbour drainage the 4 x 4 maximum drops to 5. Boundary cells hold no water.
- For order 13 the contest final report's 7442 is below OEIS's a(13) >= 7445. Always use the larger of the two published values for an order. For orders 16 to 28 only the 2010 contest values were found. Later improvements may exist unpublished or elsewhere, so recheck before claiming p3.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/magic-square-water-retention-records.md
```

Already set up? Say `run V3R1T4S on magic-square-water-retention-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `magic-square-water-retention-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
