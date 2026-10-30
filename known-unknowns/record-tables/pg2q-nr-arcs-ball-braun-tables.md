# (n,r)-arcs in PG(2,q), 11 <= q <= 31: raise a lower bound on m_r(2,q) in Ball's table or Braun's q = 23..31 table

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (ILP or local search over orbits of a prescribed subgroup of GL(3,q); verification is instant) · open as of 2026-10-30

## The problem

An (n,r)-arc in PG(2,q) is a set of n points with at most r on any line. Equivalently it is a projective [n,3,n-r]_q code; its complement is a (q+1-r)-fold blocking set. m_r(2,q) is the largest such n. It is exactly known for q <= 9. Simeon Ball's online table (codebounds.html, last updated 12 Nov 2019) covers q = 11, 13, 16, 17, 19. Its credits include Kohnert, Daskalov, Metodieva, Gulliver, Zwanzger, Cook, Bartoli-Marcugini-Pambianco, Hamada-Maruta-Oya, Heger-Csajbok and Braun. Michael Braun's arXiv:1808.02702 Table 3 compiles q = 23..31 from Daskalov, Daskalov-Metodieva, Daskalov-Manev, Csajbok-Heger and others. His arXiv:2106.05908 update (2021) raised seven lower bounds. About 43 cells are open for q <= 19, for example m_5(2,11) in 43-45, m_9(2,11) in 89-90, m_4(2,13) in 38-40, m_10(2,13) in 118-119, m_11(2,13) in 132-133, m_9(2,16) in 129-130, m_12(2,16) in 180-181, m_3(2,17) in 28-33 and m_3(2,19) in 31-39. Most q = 23..31 cells are open, for example m_3(2,23) in 37-47 and m_3(2,25) in 39-51. Braun showed that putative (44,5)- and (90,9)-arcs in PG(2,11) and (39,4)-arcs in PG(2,13) would have to be rigid (trivial automorphism group). The q <= 9 cells are exact, and they are codetables.de cells, so they are excluded here.

## What counts as a win

Give a list of n distinct points of PG(2,q), each a nonzero 3-vector over GF(q) normalised so that its first nonzero coordinate is 1, with q in {11,13,16,17,19,23,25,27,29,31}. State the field polynomial for non-prime q. Every line of PG(2,q) must contain at most r of the points, checked exhaustively over all q^2+q+1 lines. n must be STRICTLY GREATER (direction: max) than the best lower bound on m_r(2,q) at claim time: the maximum of Ball's live table, Braun's Table 3 updated by arXiv:2106.05908, and any later publication found by a fresh literature search. Context on 2026-10-30: the values quoted in the statement. n must not exceed the cell's published upper bound; a larger n means a checker bug. Values in unmerged pull requests do not set the bar.

## Partial wins

- **p1:** Lower a published upper bound for one cell (q in 11..31): show that no (u,r)-arc exists, where u is the live upper bound for that cell. The proof is an exhaustive search whose code the skeptic reruns to the same result, or an exact LP/ILP certificate checked in exact arithmetic.
- **p2:** For one of the putative arcs in PG(2,13) that Braun (arXiv:2106.05908) left either rigid or with a unique, up to conjugation, automorphism group of order 2 ((50,5), (65,6), (119,10), (133,11) or (146,12)): a rerunnable computer proof that no such arc admits that involution, or an arc that admits it (which is also a main win). The skeptic reruns the code.

## How a win is checked

Implement GF(q) (prime fields directly; GF(16), GF(25), GF(27) with a stated irreducible polynomial). Check that all points are distinct, nonzero and normalised. Enumerate all q^2+q+1 lines as normalised dual vectors and count the incident points of each (a.x = 0). Confirm the maximum count is <= r and n > bar. As a cross-check, build the 3 x n generator matrix and compute the minimum distance of the [n,3]_q code by enumerating all q^3-1 codewords: it must be n - r.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.mat.upc.edu/simeon.michael.ball/codebounds.html>

## Sources

- <https://web.mat.upc.edu/simeon.michael.ball/codebounds.html>
- <https://arxiv.org/abs/1808.02702>
- <https://arxiv.org/abs/2106.05908>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Braun's method: prescribe a cyclic or small subgroup G of GL(3,q), build the G-orbit incidence matrix, and solve max w.x subject to M x <= r with an ILP. Sweep subgroups that his paper did not list.
- For the single-gap cells, run tabu or simulated annealing with an exact line-count objective, seeded from the known record arcs (Daskalov's example files are linked from Ball's page).
- Use complements: search for small (q+1-r)-fold blocking sets instead, which suits large r.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Ball's page was last updated in 2019, so q = 23..31 values live in Braun's papers. Always take the maximum over all sources and repeat a 2020-2026 literature search before claiming. An audit search on 2026-10-30 found no later improvement (Daskalov 2022, IJMSI 17(1), gives arcs already in Ball's table).
- The arc definition requires at most r points per line; Braun also requires one line with exactly r points. Report both counts.
- For q = 16 and 25, arithmetic modulo q is not GF(q).
- q <= 9 cells are exact and duplicate codetables.de; they do not count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/pg2q-nr-arcs-ball-braun-tables.md
```

Already set up? Say `run V3R1T4S on pg2q-nr-arcs-ball-braun-tables`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pg2q-nr-arcs-ball-braun-tables`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
