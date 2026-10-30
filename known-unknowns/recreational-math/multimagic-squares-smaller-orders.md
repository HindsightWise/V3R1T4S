# Smallest multimagic squares and cubes: a tetramagic square below order 243, a pentamagic below 729, a hexamagic below 4096, a trimagic of order 13 or 15, or a bimagic cube below order 16

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: pure thought (algebraic or product constructions) with laptop-hours of search and checking · open as of 2026-10-30

## The problem

A normal k-multimagic square of order n uses 1..n^2 once each, and the sums of the entries' j-th powers are equal along every row, column and both main diagonals, for each j = 1..k. Christian Boyer's multimagie.com keeps the records. Bimagic: smallest order 8 (G. Pfeffermann, 1890; orders below 8 are impossible). Trimagic: smallest 12 (Walter Trump, 2002; below 12 is impossible, as is 14). Orders 13 and 15 are open: none is known, and none has been proven impossible. Nicolas Rouanet's best order-13 square has 13 trimagic rows, 11 trimagic columns and 1 trimagic diagonal. Tetramagic: smallest known 243 (Pan Fengchu, February 2004). Orders up to 23, and 25 and 26, are proven impossible, so the smallest is 24 or lies in 27..243. Pentamagic: smallest known 729 (Li Wen, June 2003). Hexamagic: smallest known 4096 (Pan Fengchu, December 2003). Cubes: the smallest known bimagic cube has order 16 (Christian Boyer, January 2003; below 8 is impossible). Boyer's order-32 perfect bimagic cube (2003) was superseded in April 2015 by Zhong Ming's perfect bimagic cubes of orders 16 and 25, so the smallest known perfect bimagic cube also has order 16. The Records, Unsolved problems, Smallest tetramagic and Multimagic cubes pages were re-fetched on 2026-10-30 and give these values. A web search found no smaller construction, though its coverage of recent preprints may be incomplete. Boyer's prize Enigmas, such as the 5x5 bimagic square in distinct integers and small add-mult squares, are separate live prize challenges and are not part of this target.

## What counts as a win

Any one of the following, built from consecutive integers (normal), strictly smaller than the record on multimagie.com at verification time: a tetramagic square of order < 243; a pentamagic square of order < 729; a hexamagic square of order < 4096; a trimagic square of order 13 or 15; or a bimagic cube of order < 16 (all rows, columns, pillars and the four space diagonals bimagic; a perfect bimagic cube of order < 16 also qualifies, since it is a bimagic cube). The object must be given in full.

## Partial wins

- **p1:** A normal 13 x 13 magic square (entries 1..169, all 28 lines summing to 1105) in which strictly more than 25 of the 28 lines (rows, columns, two diagonals) are also bimagic and trimagic, beating Rouanet's 13 rows + 11 columns + 1 diagonal.

## How a win is checked

Big-integer check of the entry set (exactly 1..n^2, or 1..n^3 for cubes), then the power sums for j = 1..k along every required line, compared with the magic sums S_j = (sum of i^j over the entries) / n. The check takes seconds even for order 242.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.multimagie.com/English/Records.htm>

## Sources

- <http://www.multimagie.com/English/Records.htm>
- <http://www.multimagie.com/English/Problems.htm>
- <http://www.multimagie.com/English/Smallesttetra.htm>
- <http://www.multimagie.com/English/Smallesttri.htm>
- <http://www.multimagie.com/English/Cube.htm>
- <http://www.multimagie.com/English/Smallestbicube.htm>
- <http://www.multimagie.com/English/News2006.htm>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Normal means consecutive integers 1..n^2. Squares in arbitrary distinct integers are a different (and partly prize-carrying) problem.
- Wikipedia's multimagic page still gives 256 as the smallest tetramagic order and omits Pan Fengchu's 243. Use multimagie.com.
- The top table on multimagie.com's Cube.htm still lists 32 as the smallest perfect bimagic cube. The Zhong Ming section further down the same page, and the Problems page, show that orders 16 and 25 were built in April 2015. A perfect bimagic cube of order 16 to 31 is not a new record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/multimagic-squares-smaller-orders.md
```

Already set up? Say `run V3R1T4S on multimagic-squares-smaller-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `multimagic-squares-smaller-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
