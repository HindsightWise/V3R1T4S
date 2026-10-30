# Maximum number of transversals T(n): a Latin square of order 10 with more than Parker's 5504, or a new record for n = 11..20

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (counting transversals of an order-20 square takes minutes to hours) · open as of 2026-10-30

## The problem

T(n), the maximum number of transversals in a Latin square of order n (OEIS A090741), is known only for n <= 9 (McKay, McLeod and Wanless, Des. Codes Cryptogr. 40 (2006); Bedford; Parker). For n = 10 the best known is 5504 transversals, in a turn-square of E. T. Parker. McKay et al. report that none of the several billion order-10 squares met in an earlier search, which included every square with a nontrivial symmetry, had more. Their upper bound is T(10) <= 75000. Ian Wanless's data page lists provisional winners: n=10: 5504, 11: 37851, 12: 198144, 13: 1030367, 14: 3477504, 15: 36362925, 16: 244744192, 17: 1606008513, 18: 6434611200 (two turn-squares of Z_9 x Z_2), 19: 87656896891, 20: 697292390400. For odd n >= 11 these are the cyclic-group counts (OEIS A006717). E. I. Vatutin's A287644 comments (diagonal Latin squares) match them where they give a value. The cyclic square is optimal for n = 3, 5 and 7 but not for n = 9, where Z_3 x Z_3 (2241) beats Z_9 (2025), so the cyclic records at larger odd orders need not be optimal.

## What counts as a win

Success means an explicit Latin square of order n, 10 <= n <= 20, whose number of transversals is STRICTLY GREATER than the larger of the provisional winner on Wanless's data page and any larger value in OEIS A090741 or A287644 (comments and example files), re-fetched immediately before claiming. Also counted: for odd n in {21, 23}, a square with more transversals than the cyclic Latin square of that order (A006717((n-1)/2): 5778121715415 and 452794797220965). The McKay-McLeod-Wanless group table shows these beat every other group table of those orders. Counts must agree across two independently written programs.

## Partial wins

- **p1:** For some n in {10, ..., 20} other than 18 (which already has two inequivalent record squares), a Latin square whose transversal count equals the provisional winner on Wanless's data page exactly. It must not be in the same main class (species) as the square in that page's file for n, or as any square in the OEIS A090741 or A287644 example files. Show this with canonical forms under paratopy computed by two independent programs.
- **p2:** An independent recount that fails to reproduce a listed provisional-winner count (an error in the table), with both programs and the square.

## How a win is checked

Check the square is Latin. Count transversals with two independent exact counters (for example DLX exact cover, and row-by-row backtracking with column and symbol bitmasks). For p1, compute canonical forms under the full paratopy group (rows, columns, symbols and conjugates) using, for example, a nauty graph encoding.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://users.monash.edu.au/~iwanless/data/transversals/>

## Sources

- <https://users.monash.edu.au/~iwanless/data/transversals/>
- <https://oeis.org/A090741>
- <https://oeis.org/A287644>
- <https://oeis.org/A006717>
- <https://users.monash.edu.au/~iwanless/papers/numtransvDCC.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Even orders: perturb group tables of Z_2 x Z_m, Z_2^2 x Z_m or other groups with few cycle switches or turns, as the order-18 record was found; count transversals incrementally after each switch.
- Simulated annealing on the transversal count using fast incremental counting restricted to the rows that changed.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The order-18 turn-squares are described incorrectly in the McKay-McLeod-Wanless paper; use the count 6434611200 and the files on Wanless's page.
- These OEIS A-numbers are covered here, not by the generic OEIS 'more' entry.
- Do not count diagonal transversals (Vatutin's A287648) by mistake.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/latin-max-transversals-n10-20.md
```

Already set up? Say `run V3R1T4S on latin-max-transversals-n10-20`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `latin-max-transversals-n10-20`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
