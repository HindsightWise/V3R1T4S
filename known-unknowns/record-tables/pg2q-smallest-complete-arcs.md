# Smallest complete arcs in PG(2,q), q >= 37: beat a smallest known size in the Bartoli-Davydov-Faina-Kreshchuk-Marcugini-Pambianco tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (randomised greedy and local search; completeness check is O(n^2 q) and takes seconds for q <= 10^4) · open as of 2026-10-30

## The problem

An n-arc in PG(2,q) has no three points collinear. It is complete if no point can be added, so every point off the arc lies on a bisecant. t_2(2,q), the smallest size of a complete arc, is exactly known only for q <= 32 (t_2(2,31) = t_2(2,32) = 14, Bartoli-Faina-Marcugini-Pambianco). Bartoli, Davydov, Faina, Kreshchuk, Marcugini and Pambianco, arXiv:1312.2155v3 (June 2015), tabulate the smallest known sizes for every prime power q <= 160001 and 34 sporadic q up to 430007 (Tables 1-6, Table 4 for q <= 10000). Their sources include Pace and their own randomised greedy searches. Examples from Table 4: q = 37: 15, 41: 16, 43: 16, 47: 18, 49: 18, 53: 18, 59: 20, 64: 22, 101: 30, 127: 35, 256: 55, 1024: 124. Known lower bounds are about sqrt(2q)+1, or sqrt(3q)+1/2 for q = p^h with h <= 3, so every cell with q >= 37 is open. A complete arc is a parity-check matrix of a [n, n-3, 4]_q code with covering radius 2. Kéri's covering-codes entry covers only q <= 4 unrestricted codes, so this is a distinct record.

## What counts as a win

Give a set A of points of PG(2,q), with q a prime power >= 37 that appears in the arXiv:1312.2155v3 tables, as normalised 3-vectors over GF(q) (state the field polynomial for non-prime q). Three checks: (1) no three points of A are collinear; (2) every point of PG(2,q) not in A lies on a line through two points of A (exhaustive over all q^2+q+1 points); (3) |A| is STRICTLY SMALLER (direction: min) than the smallest known t_2(2,q) at claim time. The bar for (3) is the 1312.2155v3 value or any smaller published value found by a fresh literature search. |A| must exceed the proved lower bound for that q; otherwise the checker has a bug.

## Partial wins

- **p1:** Determine t_2(2,37) exactly. Give a complete arc of some size s in PG(2,37), checked as in the main criterion, together with an exhaustive search, rerun by the skeptic, proving that no complete arc of size s-1 or less exists. This counts only if no publication already determines t_2(2,37). If s is below the live smallest known size (15 on 2026-10-30), it is also a main win.

## How a win is checked

Read the points, normalise them and check distinctness. Mark all bisecant lines: for each pair, compute the cross product, which gives the line. Check that no line contains three arc points by counting arc points on each bisecant. Then mark every point on every bisecant (n(n-1)/2 lines times q+1 points) and confirm that every non-arc point is marked. As an independent check, confirm that a point P is uncovered exactly when A + {P} is still an arc.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1312.2155>

## Sources

- <https://arxiv.org/abs/1312.2155>
- <https://arxiv.org/abs/1404.0469>
- <https://www.moi.math.bas.bg/~ACCT2012/b10.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The table values come mostly from randomised greedy algorithms. Try large-neighbourhood search: remove k points, then exactly re-cover the uncovered points with k-1 new points by ILP or SAT.
- Prescribe a stabiliser: arcs that are unions of orbits of a small cyclic group of PGL(3,q) cut the search space (Pace's A5-invariant arcs gave several small-q records).
- Small q (37-200) is where exhaustive-style methods can still compete with the 2015 numbers.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The table snapshot is from June 2015. An audit search on 2026-10-30 found no smaller published value for any q (the 2008 Lisoněk-Marcugini-Pambianco 15-arcs in PG(2,37) already match the table; Davydov's iitp.ru table could not be fetched). Repeat the 2016-2026 literature search before claiming.
- Completeness is checked over all points, not by sampling.
- Do not confuse complete arcs with 1-saturating sets: a saturating set need not be an arc, and the record here requires the arc property.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/pg2q-smallest-complete-arcs.md
```

Already set up? Say `run V3R1T4S on pg2q-smallest-complete-arcs`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pg2q-smallest-complete-arcs`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
