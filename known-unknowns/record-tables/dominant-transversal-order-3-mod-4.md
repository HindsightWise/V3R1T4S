# Dominant transversals: a Latin square of order 11 (or 15, 19, ...) with a transversal that meets every other transversal (Ghafari-Wanless Question 1)

📊 **Record tables** · standard · tractability ★★★☆☆ · compute: laptop-hours (enumerating all transversals of an order-11 square takes seconds; the search over squares is the cost) · open as of 2026-10-30

## The problem

A transversal of a Latin square of order n is a set of n cells, one in each row, column and symbol. Afsane Ghafari and Ian M. Wanless (arXiv:2607.17547, 20 Jul 2026, 'Latin squares whose transversals intersect in unusual ways') call a transversal dominant if it intersects every other transversal of the square. They prove (Theorem 4/13) that a Latin square with a dominant transversal exists for every n > 4 with n not 3 mod 4 and n != 6; for n = 7 the Egan-Wanless enumeration finds exactly 19 species with one, while orders 2, 3, 4 and 6 have none. Their Question 1 asks whether one exists for every n >= 7. All 36,007 order-9 species with a dominant transversal get it from a subsquare of order 4 via a parity argument that cannot work when n is 3 mod 4, and the authors report failing to find examples of orders 11 and 15. So the smallest open case is n = 11, then 15, 19, 23, ... Wanless's data page (users.monash.edu.au/~iwanless/data/transversals/) lists examples only for orders 5, 7, 8, 9.

## What counts as a win

Success means an explicit Latin square L of order n with n = 3 mod 4 and n >= 11, plus one transversal T of L, such that T shares at least one cell with every other transversal of L. Both facts are confirmed by two independently written programs that each enumerate ALL transversals of L. Before claiming, re-fetch arXiv:2607.17547 (latest version) and the Wanless data page, and search arXiv for any later paper settling the same order. If an example of that order has been published since, the claim fails.

## Partial wins

- **p1:** A Latin square of order 11 or 15 with a transversal T that is disjoint from exactly one other transversal of L (all other transversals meet T), confirmed by two independent full enumerations of the transversals.
- **p2:** An exhaustive search, run by two independent programs that agree, showing that no Latin square of order 11 with a stated nontrivial autotopism (for example a given cycle-structure class not already excluded by Theorems 11-12 of arXiv:2607.17547) has a dominant transversal, with the full list of squares checked published.

## How a win is checked

Check L is Latin. Enumerate every transversal (a DLX or bitmask backtrack; order 11 has at most a few tens of thousands). Check T is among them. Check T has nonempty intersection, as cell sets, with every other transversal. Use two independent programs and compare the transversal counts. (The lane's own checker reproduced the paper's order-7 and order-8 examples: 24 transversals with 3 dominant; 3 with 4 pinned cells; 31 with 9 dominant.)

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2607.17547>

## Sources

- <https://arxiv.org/abs/2607.17547>
- <https://users.monash.edu.au/~iwanless/data/transversals/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Seek squares of order 11 with very few transversals (e.g. near Wanless's 778-transversal square) and test each transversal for dominance; fewer transversals make dominance cheaper to reach.
- Generalise the parity argument of the paper (equation (15)) to a Z_m-valued labelling that works modulo another prime; the order-9 data says the Z_2 trick alone is exhausted.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The order 7 case is already settled (19 species); n = 7 does not count.
- Cayley tables of groups and diagonally cyclic squares have no dominant transversal (Theorems 11 and 12 of the paper); do not search them.
- A square with a pinned entry makes every transversal dominant. That is allowed, and the paper's order-5 and order-7 examples have pinned entries, but confirm the pinned entry with both full enumerations.
- Dominance must be checked against ALL transversals of L, never a sample.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/dominant-transversal-order-3-mod-4.md
```

Already set up? Say `run V3R1T4S on dominant-transversal-order-3-mod-4`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dominant-transversal-order-3-mod-4`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
