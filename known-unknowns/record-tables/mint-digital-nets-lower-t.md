# Digital (t,m,s)-nets: a smaller quality parameter t than MinT's best known digital net (bases 2-9)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (exact rank checks over F_b take seconds; the search is the cost) · open as of 2026-10-30

## The problem

A digital (t,m,s)-net over F_b is given by s generator matrices C_1..C_s in F_b^{m x m}; its quality t is the least t such that for every (d_1..d_s) with d_i >= 0 and d_1+...+d_s = m-t the first d_i rows of the C_i together have rank m-t. Smaller t means better equidistribution. MinT, the database of Rudolf Schurer and Wolfgang Ch. Schmid (University of Salzburg; footer: database last updated 2024-09-05, but its history page lists no new methods after 2008-03-11; reachable over http only on 2026-10-30), lists for each base b and (m,s) the best known digital t and the digital lower bound. On 2026-10-30, for m <= 25 and s <= 30, base 2 has 301 cells where the constructive digital t exceeds the digital lower bound, base 3 has 355 and base 4 has 347. Smallest base-2 gaps: (m,s) = (8,11), best t = 4 (s-reduction of a digital (4,8,17)-net from net-embeddable BCH codes), bound t >= 3; (9,10) 4 vs 3; (10,8) and (10,9) 4 vs 3. Smallest base-3 gap: (6,8), t = 2 (Niederreiter-Xing sequence, genus 2) vs bound 1. Records come from Niederreiter-Xing sequences (Pirsic implementation), Sobol' and Niederreiter sequences, Edel's net-embedding search, BCH-code nets (Ling-Ozbudak; Helleseth-Klove-Levenshtein), shift nets (Schmid), the (u,u+v) construction and propagation rules. Cells where a digital net is only known to exist (MinT 'Digital' below 'Constructive and digital'), in the same range: 4 in base 2 ((23,13), (24,13), (25,13), (24,30), from a manYPoints curve), 11 in base 3, 61 in base 4, 23 in base 5, 301 in base 7 (e.g. (6,22): digital t = 2 from a Gilbert-Varshamov OOA embedding, constructive t = 3), 54 in base 8 and none in base 9.

## What counts as a win

Success means explicit generator matrices C_1..C_s in F_b^{m x m} (b in MinT's list 2, 3, 4, 5, 7, 8, 9; for b = 4, 8, 9 the field model, e.g. F_4 = F_2[x]/(x^2+x+1), is stated) such that: (1) they form a digital (t,m,s)-net, i.e. for every composition (d_1..d_s) of m-t into s non-negative parts the first d_i rows of the C_i together have rank m-t over F_b, checked exhaustively; (2) t is STRICTLY SMALLER (direction: min) than the 'Constructive and digital' value on the live MinT query page http://mint.sbg.ac.at/query.php?b= < b > &m= < m > &s= < s > &p=smt at verification time; (3) t is at least MinT's digital lower bound on that page (below it means a bug); (4) no paper, preprint or public table of any date already gives a digital (t,m,s)-net over F_b with that t (MinT lists no new methods after 2008, so the literature since then must be checked). Two independent rank checkers must agree.

## Partial wins

- **p1:** A first explicit construction: generator matrices of a digital (t,m,s)-net over F_b (b = 3, 4 or 5) for a cell where MinT's 'Digital' (existence) value is strictly below its 'Constructive and digital' value (e.g. base 3, (m,s) = (16,23): existence t = 8, constructive t = 9), reaching the existence value, verified as in the main criterion.
- **p2:** A raised digital lower bound: a re-runnable exhaustive classification (with a DRAT proof checked by drat-trim, or two independent search programs that agree) showing that no digital (t,m,s)-net over F_b exists for t equal to MinT's live digital lower bound in a gap cell, e.g. no digital (3,8,11)-net over F_2.

## How a win is checked

Write an independent checker: for each composition (d_1..d_s) of k = m-t with 0 <= d_i <= k, stack the first d_i rows of each C_i and compute the rank over F_b by Gaussian elimination (bitsets for b = 2, table arithmetic for prime powers). The number of compositions is C(k+s-1, s-1), at most a few million for the tabulated range. Confirm that rank = k for all of them. Fetch the live MinT cell over http and compare with both the constructive digital value and the digital bound. Search arXiv and MathSciNet-indexed journals for newer net constructions with the same (b,m,s).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://mint.sbg.ac.at/table.php?b=2&col=1&p=smt&mode=cd&opt=bd&minx=1&maxx=30&miny=0&maxy=25>

## Sources

- <http://mint.sbg.ac.at/table.php?b=2&col=1&p=smt&mode=cd&opt=bd&minx=1&maxx=30&miny=0&maxy=25>
- <http://mint.sbg.ac.at/table.php?b=3&col=1&p=smt&mode=cd&opt=bd&minx=1&maxx=30&miny=0&maxy=25>
- <http://mint.sbg.ac.at/query.php?b=2&s=11&m=8&p=smt>
- <http://mint.sbg.ac.at/history.php>
- <http://mint.sbg.ac.at/about.php>
- <https://link.springer.com/chapter/10.1007/978-3-642-04107-5_10>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search for digital nets with a prescribed automorphism (cyclic or quasi-cyclic generator matrices, shift-net structure), so a few first rows define all matrices and the rank checks reduce by symmetry.
- Use the duality with linear ordered codes (NRT codes): search for a dual NRT code of large NRT distance, then convert, as Edel's net-embedding search did.
- Run an exact SAT or CP-SAT model only on the first m-t rows of each C_i; deeper rows do not affect t.
- After any win, apply MinT's propagation rules (s-reduction, m-reduction, base change) to fill neighbouring cells.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- MinT answers on http://mint.sbg.ac.at only; https was refused on 2026-10-30.
- MinT table URLs need the range parameters minx, maxx, miny and maxy (as in status_source); without them MinT returns 'ERROR: Argument dx is missing'. The per-cell query.php pages need none.
- MinT's history page lists no new methods after 2008-03-11 (database footer 2024-09-05), so check the literature since 2008 before claiming, not only since 2024.
- Base 2 cells have been searched intensively; the lane check's 60 s randomized search found nothing for the (3,8,11) cell.
- For prime-power bases, arithmetic must be in F_q, not in Z_q.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mint-digital-nets-lower-t.md
```

Already set up? Say `run V3R1T4S on mint-digital-nets-lower-t`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mint-digital-nets-lower-t`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
