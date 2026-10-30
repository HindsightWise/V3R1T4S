# Equal sums of like powers for k = 7..32: a k.m.n solution with fewer terms than Meyrignac's EulerNet records

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (high-k cells); needs cluster for k = 7..10 · open as of 2026-10-30

## The problem

For a k.m.n equation x1^k+...+xm^k = y1^k+...+yn^k (positive integers, primitive, no term on both sides), Jean-Charles Meyrignac's EulerNet site (euler.free.fr, with database.txt, latest entry 2021) keeps the smallest known n for each (k, m) and the smallest known total m+n for each k. The record totals for k = 7..17 are 8, 8, 10, 11, 14, 14, 17, 18, 21, 23, 28, and for k = 18..32 they are 28, 32, 34, 39, 41, 44, 48, 52, 52, 61, 63, 67, 69, 72, 75. Recent moves include Duncan Moore's 10.5.6 (2020, the k = 10 record), Ian Stopher's 6.1.7 (2021), many cells by Scott I. Chase and Laurent Lucas (2011-2015), and new 7.2.7 and 7.3.6 solutions by J. Glickman on MathWorld (2026). LPS predicts m+n >= k, and for k = 8 the record already equals k (8.4.4 by Kuosa, 8.3.5 by Chase). MathWorld lists many cells as unknown, for example 7.1.6, 7.2.5, 7.3.4, 8.1.7, 8.2.6 and 9.4.5. Credit: Meyrignac, Wroblewski, Chase, Lucas, Childers, Yura, Alm, Kuosa, Ekl, Dodrill, Resta, Moore, Glickman, Lander-Parkin-Selfridge. Cases with k <= 6 are covered by other bank entries.

## What counts as a win

CONFIRMED for some 7 <= k <= 32 and positive integers x1..xm, y1..yn with sum x_i^k = sum y_j^k exactly (Python big integers), gcd of all terms 1, and no value on both sides. m+n must be STRICTLY SMALLER (direction: min) than three values at verification time: the 'LOWEST NUMBER OF TERMS' value for k on http://euler.free.fr/; every m+n for k in http://euler.free.fr/database.txt; and every m+n on MathWorld's 'Diophantine Equation--kth Powers' page for k where such a page exists (7th to 10th powers on 2026-10-30). The values above on 2026-10-30 are context only. For k = 8 such a solution has m+n <= 7 and disproves the LPS conjecture.

## Partial wins

- **p1:** Cell record: for some 7 <= k <= 32 and some m in the 'KNOWN LOWER BOUNDS' table on euler.free.fr, a primitive nontrivial solution of type (k, m, n) with m <= n (sides swapped if needed). n must be strictly smaller than the table's value for (k, m) and than any (k, m, n') in database.txt or on the MathWorld page for k (where one exists) at verification time. Cells whose table value already equals m cannot be improved this way.
- **p2:** New type at the record total: for some 7 <= k <= 32, a primitive nontrivial solution of type (k, m, n) with m+n equal to the current record total for k, where no solution of that exact type appears in database.txt or on the MathWorld page for k at verification time (for example 8.1.7, 8.2.6, 9.1.9, 9.3.7, 10.4.7, 10.3.8).

## How a win is checked

Exact big-integer evaluation of both sides, a gcd check, a check that no value is on both sides, and a lookup against the euler.free.fr table, database.txt and the MathWorld page for k. Under 1 second.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://euler.free.fr/>

## Sources

- <http://euler.free.fr/>
- <http://euler.free.fr/database.txt>
- <http://euler.free.fr/records.htm>
- <https://mathworld.wolfram.com/DiophantineEquation7thPowers.html>
- <https://mathworld.wolfram.com/DiophantineEquation8thPowers.html>
- <https://mathworld.wolfram.com/DiophantineEquation9thPowers.html>
- <https://mathworld.wolfram.com/DiophantineEquation10thPowers.html>
- <https://www.math.uni.wroc.pl/~jwr/eslp/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Wroblewski's congruence method: choose a modulus M where k-th powers take few residues (for example M = 2^a 3^b p with p-1 | k), fix congruence classes for all but two terms, then meet in the middle. His published congruence-solution files (math.uni.wroc.pl/~jwr/eslp) are the natural starting point.
- For high k (20..32), the gaps between neighbouring cells in the table are irregular, which suggests the cells were explored unevenly. Target the cells whose n is much larger than for the neighbouring m.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- MathWorld's 9th and 10th power pages lag euler.free.fr (for example, 10.5.6 by Duncan Moore 2020 is not on MathWorld, and 9.2.8 and 10.1.12 by Wroblewski are in database.txt while MathWorld says none are known). Check all three sources.
- Non-primitive solutions, solutions with a common term on both sides, and permuted repeats are not new.
- database.txt lists bases only, in the form (k,m,n) a+b+...=c+d+..., and writes x*c for c copies of the base x (for example 17*2 is two terms 17^k, not 34^k). Count terms with multiplicity when comparing m+n, and parse it exactly before calling a type new.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/eslp-min-terms-k7-to-k32.md
```

Already set up? Say `run V3R1T4S on eslp-min-terms-k7-to-k32`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `eslp-min-terms-k7-to-k32`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
