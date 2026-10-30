# Erdős #82 small cases: a graph on 21 vertices with no regular induced subgraph of order >= 6, or on 30 vertices with none of order >= 7

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (SAT/local search over graphs on 20-30 vertices) · open as of 2026-10-30

## The problem

Erdős, Fajtlowicz and Staton: let N_{ > =k} be the least n such that every n-vertex graph has a regular induced subgraph on at least k vertices (the page's G(k)); #82 asks to prove F(n)/log n -> infinity, i.e. N_{ > =k} = 2^{o(k)}. Known: N_{ > =3} = 5, N_{ > =4} = 7 (Fajtlowicz-McColgan-Reid-Staton 1995), N_{ > =5} = 17 (Brendan McKay 1997, confirmed by Boris Alexeev 2025), N_{ > =6} >= 21 and N_{ > =7} >= 30 (Paul Dyson and Brendan McKay, 'Ramsey numbers for regular induced subgraphs', arXiv:2604.08215 v3, Theorem 1.2; OEIS A394563). For exact order k (OEIS A394564): N_5 = 21, N_6 >= 28, N_7 >= 71; also N_{6,7} >= 28 and N_{7,8} >= 31 (605,961,088 graphs on 30 vertices with no regular induced subgraph of order 7 or 8). McKay's data page (users.cecs.anu.edu.au/~bdm/data/ramsey.html) posts samples of 1,000,000 graphs on 20 vertices (none of order >= 6) and on 29 vertices (none of order >= 7). Dyson-McKay v3 section 5 report 49,871,540 graphs on 20 vertices and 174,775,920 on 29 vertices, none of which extends by one vertex; more than 6,000 further 29-vertex graphs from a random-restart process were all outside that collection, so they judge it far from complete and call a 30-vertex extension 'a good possibility'. Forum, arieledgardolevy (2026-08-07): a SAT extension test certifies 66 sampled 29-vertex graphs non-extendable to 30. Asymptotically N_{ > =k} >= (1/(2e) - o(1))k^2 (Dyson-McKay v3, Theorem 1.1; the problem page still shows the earlier 9/163, corrected by a forum update of 2026-08-14). Status: open on erdosproblems.com and in the teorth database.

## What counts as a win

CONFIRMED: a graph (graph6) on 21 vertices with no induced regular subgraph on 6 or more vertices (giving N_{ > =6} >= 22), or on 30 vertices with none on 7 or more vertices (N_{ > =7} >= 31), strictly beyond the values in Dyson-McKay and on the #82 thread at verification time. Regular includes empty and complete subgraphs. Alternatively a certified proof (exhaustive search with DRAT/LRAT-checked SAT certificates) that N_{ > =6} = 21.

## Partial wins

- **p1:** A graph on 28 vertices with no induced regular subgraph of order exactly 6 (N_6 >= 29), or on 71 vertices with none of order exactly 7 (N_7 >= 72), strictly beyond Dyson-McKay Theorem 1.2 at verification time.
- **p2:** A graph on 31 vertices with no induced regular subgraph of order 7 or 8 (N_{7,8} >= 32), beyond Dyson-McKay's N_{7,8} >= 31.

## How a win is checked

Independent exhaustive check of every vertex subset of the relevant sizes for regularity (with pruning: a subset is regular iff all induced degrees are equal), plus an independent SAT encoding whose UNSAT result is checked with a proof checker. Compare against McKay's posted collections to confirm the graph is new and the bound improves.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/82>

## Sources

- <https://www.erdosproblems.com/82>
- <https://www.erdosproblems.com/forum/thread/82>
- <https://arxiv.org/abs/2604.08215>
- <https://users.cecs.anu.edu.au/~bdm/data/ramsey.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- One-vertex extension of known extremal graphs is hopeless by clause density (Levy); search for structured graphs (circulants, Cayley graphs, blow-ups of Paley-type graphs) on 21 or 30 vertices directly.
- For exact-order N_7 >= 72, random-like constructions with degree constraints from the Dyson-McKay first-moment model are a natural start.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 'Order at least k' (N_{ > =k}) and 'order exactly k' (N_k) are different quantities with different records.
- Empty and complete induced subgraphs are regular; a construction must avoid large cliques and independent sets too.
- McKay's posted 20- and 29-vertex graphs are samples, not complete collections; non-extension of them proves nothing about exact values.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-82-regular-induced-subgraph-ramsey.md
```

Already set up? Say `run V3R1T4S on erdos-82-regular-induced-subgraph-ramsey`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-82-regular-induced-subgraph-ramsey`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
