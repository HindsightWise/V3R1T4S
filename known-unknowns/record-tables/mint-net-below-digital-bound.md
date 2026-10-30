# MOONSHOT - A (t,m,s)-net that beats every digital net: t below MinT's proven digital lower bound, e.g. a (2,8,7)-net in base 2

📊 **Record tables** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (SAT or exact search over 2^m-point sets) · open as of 2026-10-30

## The problem

A (t,m,s)-net in base b is a set of b^m points in [0,1)^s such that every elementary box of volume b^(t-m) contains exactly b^t points. In MinT (Schurer and Schmid, University of Salzburg; database last updated 2024-09-05), on 2026-10-30 the best known arbitrary t equals the best digital t in every cell checked (bases 2, 3, 4, 5 and 8, m <= 25, s <= 30). So no non-digital net is known to beat digital nets anywhere in these tables. Yet in 49 base-2 cells, 110 base-3 cells and 105 base-4 cells the general lower bound on t is strictly below the proven digital lower bound, so only a non-digital net can improve them. Base-2 examples: (m,s) = (8,7): no digital (2,8,7)-net (Schmid-Wolf bound on the embedded linear OOA), but the general bound is only t >= 2 (generalized Rao bound); (9,7) has the same gap; (7,12) and (7,13): no digital (3,7,12)-net (Fontaine-Peterson bound on the embedded linear OA), general bound t >= 3 from the LP bound for OOAs, and a non-linear OA(2^7,12,2,4) does exist (Nordstrom-Robinson/Kerdock); (8,12), (8,18) to (8,20). Base-4 examples: (1,4,18) to (1,4,21) and (1,5,12).

## What counts as a win

Success means an explicit set of b^m points, each coordinate written as an integer a in [0, b^m) standing for a/b^m, that is a (t,m,s)-net in base b (every elementary box of volume b^(t-m) contains exactly b^t points, checked exhaustively), with t STRICTLY SMALLER (direction: min) than MinT's live digital lower bound for (b,m,s) (http://mint.sbg.ac.at/query.php?b= < b > &m= < m > &s= < s > &p=smt, 'Lower bound on t (digital)') and at least MinT's general lower bound on the same page (below it means a bug). Such a set is necessarily non-digital. No paper, preprint or public table of any date may already contain a net with these parameters (MinT lists no new methods after 2008).

## Partial wins

- **p1:** A closed cell: an exact certificate that no (t,m,s)-net in base b exists for t equal to MinT's general lower bound in one of the cells where it is below the digital bound (e.g. no (2,8,7)-net in base 2). The certificate is an exact rational dual solution of the linear-programming bound for the embedded OOA, verified in exact arithmetic, or a DRAT proof of unsatisfiability checked with drat-trim. MinT's general lower bound then rises.

## How a win is checked

For each composition (d_1..d_s) of k = m - t with d_i >= 0, map every point to the box index (floor(a_i / b^(m-d_i)))_i and check that each of the b^k boxes holds exactly b^t points. For (2,8,7) this is 924 compositions of 6 over 256 points. Check also that there are exactly b^m points. Read the digital and general bounds from the live MinT query page over http. For p1, re-verify the LP dual or the DRAT proof independently.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://mint.sbg.ac.at/query.php?b=2&s=7&m=8&p=smt>

## Sources

- <http://mint.sbg.ac.at/query.php?b=2&s=7&m=8&p=smt>
- <http://mint.sbg.ac.at/query.php?b=2&s=12&m=7&p=smt>
- <http://mint.sbg.ac.at/table.php?b=2&col=1&p=smt&mode=e&opt=b&minx=1&maxx=30&miny=0&maxy=25>
- <http://mint.sbg.ac.at/table.php?b=2&col=1&p=smt&mode=cd&opt=bd&minx=1&maxx=30&miny=0&maxy=25>
- <http://mint.sbg.ac.at/table.php?b=2&col=1&p=smt&mode=e&opt=ed&minx=1&maxx=30&miny=0&maxy=25>
- <http://mint.sbg.ac.at/history.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from non-linear objects that already beat linear ones: Nordstrom-Robinson, Kerdock and Preparata OAs and Z4-linear codes, and look for an ordering of digits that gives the extra depth a net needs.
- Encode the (2,8,7) net as SAT: 256 points x 7 coordinates x 6 digits (only the first m-t = 6 digits of each coordinate matter), with cardinality constraints per box; break symmetry by fixing the first coordinate to the van der Corput order.
- For base 4, Z4-linear (Gray-map) constructions are the natural non-digital candidates.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A digital net can never win here: the digital bounds are proofs.
- MinT's query page shows two different lines, 'Lower bound on t (digital)' and 'Lower bound on t'; compare with the right one.
- Check the general lower bound, too: a claimed t below it means a checker bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mint-net-below-digital-bound.md
```

Already set up? Say `run V3R1T4S on mint-net-below-digital-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mint-net-below-digital-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
