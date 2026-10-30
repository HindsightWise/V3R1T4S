# Erdos #628 (Erdos-Lovasz Tihany, a = 2 branch): a noncomplete double-critical graph, or the order-14 census

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days for order 14 with k >= 8; needs cluster for (k,n) = (6,14) (estimated about 10^4 core-hours) · open as of 2026-10-30

## The problem

Erdos-Lovasz Tihany conjecture (Erdos 1968): a K_k-free graph with chromatic number k is (a,b)-splittable for all a,b >= 2 with a+b = k+1. The case a=b=3 was proved by Brown and Jung. The a=2 case reduces to the Double-Critical Graph Conjecture: every connected double-critical k-chromatic graph (chi(G - x - y) = k-2 for every edge xy) is K_k. It is known for k <= 5 at every order (Stiebitz 1987). Kawarabayashi-Pedersen-Toft (EJC 2010, Prop. 9) show that a noncomplete connected example with k >= 6 has minimum degree >= k+1, hence at least k+2 vertices, and that no two vertices of degree k+1 are adjacent. Orders <= 12 are excluded (A. S. Pedersen's 2012 note, cited in Kriesell-Pedersen 2015). An unrefereed 2008 UBC undergraduate report by Edward Lui already claims at least 14 vertices, and minimum degree >= 8 for k = 6; only its abstract is online. Order 13 is now closed by computation: the erdosproblemaday.com report (Jul 2026) did k = 8..11, and BitterLemma (forum, 17 Aug 2026, github.com/bitterlemma/erdos-628) did k = 6 and 7. The (6,13) cell held 12,371,706,156 generated graphs (geng -c -d7 13), 2,468,617,015 of them 6-chromatic, with 0 survivors. Order 14 was not attempted. Z. Song's survey records many special cases; the conjecture is open.

## What counts as a win

CONFIRMED: an explicit graph (edge list) that is connected and noncomplete, has chromatic number k >= 6 (exact), and is double-critical: chi(G - {x,y}) = k-2 for every edge xy, checked exactly. This is a counterexample to the Double-Critical Graph Conjecture and so to Erdos-Lovasz Tihany at (2, k-1). Also accepted: any K_k-free graph with chi = k and some a,b >= 2, a+b = k+1, that is provably not (a,b)-splittable, with an exhaustive certificate.

## Partial wins

- **p1:** Complete order-14 census for every k in {8,...,12}: all connected graphs on 14 vertices with minimum degree >= k+1, zero noncomplete double-critical k-chromatic survivors. Per-cell counts (generated, K_k-free, chi = k, survivors) must be reproduced by two independent runs with different shard splits.
- **p2:** The same order-14 census for k = 7 (connected graphs on 14 vertices with minimum degree >= 8).
- **p3:** The same order-14 census for k = 6 (connected graphs on 14 vertices with minimum degree >= 7).

## How a win is checked

For a counterexample: compute chi(G) and chi(G - x - y) for every edge with two unrelated exact colouring codes (DSATUR branch and bound, and a SAT encoding). For a census: regenerate the candidate stream with nauty geng (-c -d(k+1) 14 res/mod) and check that shard totals agree across two different moduli. Re-decide a random sample plus every chi = k graph with a second chromatic-number implementation, and check that chi = k equals the splittable count plus survivors in every cell.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/628>

## Sources

- <https://www.erdosproblems.com/628>
- <https://www.erdosproblems.com/forum/thread/628>
- <https://github.com/bitterlemma/erdos-628>
- <https://arxiv.org/abs/0810.3133>
- <https://oldwww.math.ubc.ca/Ugrad/NSERC/USRA-PDF/S08_lui.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the KPT structure (delta >= k+1, no two vertices of degree k+1 adjacent, no K_k, every edge in many (k-1)-cliques of G-x-y) to prune geng output early. Augmentation from 13-vertex near-misses may beat plain generation.
- For p1 the minimum degree is >= 9 on 14 vertices, so the complements have maximum degree <= 4. Generate complements instead, which is far cheaper.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- geng res/mod is 0-based. The degree flag is -d(k+1), not -dk; the wrong flag gives a plausible wrong universe.
- Connectedness matters: K_k plus an isolated vertex is double-critical.
- A census is finite evidence only; it does not prove the conjecture.
- Survivors must be re-checked with an independent chromatic-number code before any claim.
- Lui's 2008 claim of delta >= 8 for k = 6 is unrefereed and its proof is not public. A p3 census must still cover the full delta >= 7 universe; a delta >= 8 run alone does not count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-628-double-critical-order-14.md
```

Already set up? Say `run V3R1T4S on erdos-628-double-critical-order-14`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-628-double-critical-order-14`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
