# Kotzig's perfect 1-factorisation conjecture: a perfect 1-factorisation of K_64 (or K_66, 70, 76, 78, 88, 96, 100)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (exact-cover or SAT search over symmetric starters; checking takes seconds) · open as of 2026-10-30

## The problem

A 1-factorisation of K_{2t} partitions its edges into 2t-1 perfect matchings. It is perfect (a P1F) if the union of every two matchings is a Hamilton cycle. Kotzig conjectured in 1963 that K_{2t} has a P1F for every t >= 2. Known results are two infinite families (2t = p+1 and 2t = 2p, p an odd prime) plus sporadic orders found mostly by computer searches for starters with multiplicative symmetry (Dinitz-Stinson quotient-coset starters, Ihrig-Seah-Stinson, and the list kept by Ian Wanless). The smallest orders were settled one at a time, most recently 52 by Wolfe and 56 by David Pike (2019). Tomasz Maciosowski (arXiv:2610.20408, 14 Oct 2026) constructed two non-isomorphic P1Fs of K_92 from starters in Z_91 invariant under a multiplier subgroup of order 3. He states that the open orders up to 100 were 64, 66, 70, 76, 78, 88, 92, 96 and 100, so 64, 66, 70, 76, 78, 88, 96 and 100 remain open, with K_64 the smallest. A 2026 preprint (arXiv:2607.09459) proves an asymptotic version, which leaves every small order open.

## What counts as a win

Success means an explicit 1-factorisation of K_{2t} for some 2t in {64, 66, 70, 76, 78, 88, 96, 100} that is still listed as open at verification time. It is given as 2t-1 lists of t edges each, or as a starter in a stated group together with its development rule. Verification must show that (i) the matchings partition all C(2t,2) edges, each being a perfect matching, and (ii) for each of the C(2t-1,2) pairs of matchings, the union is a single cycle through all 2t vertices. The result must be new (direction: existence where none is published): re-fetch arXiv:2610.20408 and search for P1F results on that order over the last 24 months. K_64 is the headline cell.

## Partial wins

- **p1:** A verified perfect 1-factorisation of K_{2t} for one of the orders that Maciosowski's Section 3 table (arXiv:2610.20408) lists as having no known P1F but an admissible multiplier subgroup: 2t in {248, 260, 342, 404, 428, 452, 470, 512, 560, 590, 638, 672, 680, 704, 722, 764, 782, 872, 890, 932, 950, 962}, provided a fresh literature search shows no published P1F of that order.

## How a win is checked

Expand any starter into explicit matchings. Assert that every edge of K_{2t} appears exactly once and that each matching covers every vertex once. For every pair of matchings, build the union (a 2-regular multigraph) and confirm that it is one cycle of length 2t by walking it. That is C(63,2) = 1953 walks of 64 steps for K_64, which takes milliseconds. Two independent implementations must agree. Then do the literature check.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.20408>

## Sources

- <https://arxiv.org/abs/2610.20408>
- <https://users.monash.edu.au/~iwanless/data/P1F/newP1F.html>
- <https://arxiv.org/abs/1810.08734>
- <https://arxiv.org/abs/2607.09459>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Maciosowski's U-invariant cyclic starters cannot reach the eight remaining orders up to 100: by his Lemma 2.12, Z*_{2t-1} has no admissible subgroup U != 1 for 2t-1 = 63, 65, 69, 75, 77, 87, 95, 99. So for K_64 and the others, use starters or one-point extensions in non-cyclic groups of order 2t-1 (for 63 the only non-cyclic abelian group is Z_3 x Z_21 = Z_3 x Z_3 x Z_7), or prescribe automorphism groups that act on 2t-2 points with two fixed points.
- Use SAT with a lazy Hamiltonicity check: encode the starter (or the symmetric 1-factorisation) as exact cover, and add a blocking clause each time a pair of factors fails to form a single cycle (CEGAR loop).
- For p1, apply Maciosowski's method directly: his table gives the largest admissible |U| and the number c of Hamilton-cycle conditions for each order (for example 2t = 248 with |U| = 3 and c = 41, or 2t = 962 with |U| = 15 and c = 32).
- Use non-abelian groups of order 2t-1 where they exist, or Ihrig-Seah-Stinson style automorphism prescriptions, to break the obstruction that applies to cyclic multiplier symmetry.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The patterned starter {x, -x} never gives a P1F when 2t-1 is composite (Maciosowski Lemma 2.10), so do not search near it.
- Checking only pairs (F_0, F_d) is sound only when the factorisation is induced by a starter. For an arbitrary factorisation, check all pairs.
- K_92 is now solved (Oct 2026) and orders up to 56 were already done. Re-check the open list before claiming.
- A union consisting of two cycles of total length 2t is not a Hamilton cycle. Walk the cycle; do not just check degrees.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/perfect-1-factorisation-open-orders.md
```

Already set up? Say `run V3R1T4S on perfect-1-factorisation-open-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `perfect-1-factorisation-open-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
