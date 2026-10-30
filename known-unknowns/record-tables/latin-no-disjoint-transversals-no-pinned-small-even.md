# Latin squares of even order 10..26, or odd order, whose transversals pairwise intersect yet share no common cell (Ghafari-Wanless Conjecture 3 small orders)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (finding transversals is cheap; certifying that NO two are disjoint needs a full enumeration of the square's transversals) · open as of 2026-10-30

## The problem

Ghafari and Wanless (arXiv:2607.17547, 20 Jul 2026), answering a question of Nick Wormald, construct for every even n >= 28 except n = 30 a Latin square of order n with no two disjoint transversals. They prove (Theorem 6) that for n = 28 and every even n with 32 <= n <= 10000 the square also has no pinned entry (no cell lies in every transversal). Their Conjecture 3 says such a square exists for all even n >= 28. It is false for n <= 8 (Egan-Wanless enumeration). The authors write that it may also hold for some n < 28, and that it would be most interesting to know whether it can hold for any odd n. Their own construction fails at small orders: G_18 and H_16 have disjoint transversals and H_32 has none. The order 30 that the paper leaves out was settled publicly on 21 Sep 2026 in GitHub issue the-omega-institute/trureturing#9291. That issue gives an explicit square obtained from Z_30 by four cyclic trades, a Delta-sum proof that every transversal contains two of three marked entries, and three transversals with no common entry; an audit on 2026-10-30 rebuilt the square and re-checked the witnesses and the proof's finite steps. Small open orders: even n in {10, 12, ..., 26}. Odd n >= 11 is also open. n = 9 appears ruled out by the order-9 data on Wanless's page, where the square with the fewest disjoint transversals still has 3. Even n > 10000 is open too, but out of reach of the enumeration-based check below.

## What counts as a win

Success means an explicit Latin square L of order n, with n in {10,12,14,16,18,20,22,24,26} or n odd >= 11. L must satisfy all three of: (a) it has at least two transversals; (b) every two transversals share at least one cell; (c) no cell lies in every transversal. Each property is confirmed by two independently written programs that enumerate all transversals of L, or for (c) by exhibiting, for each cell, a transversal that avoids it. Before claiming, re-fetch arXiv:2607.17547 and search arXiv and public repositories (including the-omega-institute/trureturing issues) for a later construction at that order. An order already settled there, or n = 30 (settled in trureturing#9291), is not a win.

## Partial wins

- **p1:** An exhaustive search over an explicitly stated, enumerable family of Latin squares of one of the open orders, run by two independent programs that agree. Example families: every square obtained from the Cayley table of Z_n or of Z_2 x Z_(n/2) by at most two cycle switches, or every square of order 10 with a stated nontrivial autotopism. The search either finds a square with properties (a)-(c), which is then a full win, or shows that none in the family has them. It publishes the family's definition, the list of squares checked and, for each square, a witness of failure: two disjoint transversals, a pinned cell, or a certificate that it has fewer than two transversals.

## How a win is checked

Check L is Latin. Enumerate all transversals with two independent programs that agree on the count. Check that every pair intersects, using bitset cell masks. Check that the intersection of all transversals is empty, or verify one avoiding transversal per cell. Confirm that the order is not covered by the paper.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2607.17547>

## Sources

- <https://arxiv.org/abs/2607.17547>
- <https://users.monash.edu.au/~iwanless/data/transversals/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Adapt the paper's section-3 construction (a perturbed group-based square whose transversals are forced through a small region) to orders below 28, then repair with local trades while monitoring the transversal set.
- Squares of even order with few transversals (turn-squares of Z_2 x Z_m) are natural seeds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A square with NO transversals satisfies (b) and (c) vacuously; it does not count, which is why (a) is required.
- For order 26 the full transversal enumeration may be large; budget for it before claiming (b).
- n = 30 is already done (the-omega-institute/trureturing#9291, 21 Sep 2026). That square forces pairwise intersection with a Delta-sum argument (the sum of L(r,c) - r - c over a transversal is fixed mod n) rather than a full enumeration; such a proof is welcome, but the two-program checks of the criterion are still required.
- An odd-order win with n = 3 mod 4 also makes every transversal of L dominant, so it is also a win for the bank entry dominant-transversal-order-3-mod-4.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/latin-no-disjoint-transversals-no-pinned-small-even.md
```

Already set up? Say `run V3R1T4S on latin-no-disjoint-transversals-no-pinned-small-even`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `latin-no-disjoint-transversals-no-pinned-small-even`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
