# Binary orthogonal arrays with 2^m runs beyond every linear OA: higher strength than MinT's best known (smallest: OA(256, 20, 2, 4))

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

An orthogonal array OA(2^m, s, 2, k) is a 2^m x s binary array in which every k columns contain each binary k-tuple equally often. Linear OAs are duals of linear codes (covered by codetables-binary-linear). Non-linear ones can be stronger: the Nordstrom-Robinson, Kerdock, Preparata and Delsarte-Goethals codes give, e.g., OA(2^8,16,2,5) and OA(2^7,15,2,4), which no linear OA matches. MinT's orthogonal-array table (Schurer and Schmid, University of Salzburg; database footer 2024-09-05, no new methods listed after 2008-03-11) lists the best known strength and upper bounds for OAs with 2^m runs. On 2026-10-30, for m <= 25 and s <= 40, 131 base-2 cells have a best known strength below the general upper bound while already equal to the linear upper bound, so only a non-linear array can improve them. Smallest (by m): (m,s) = (8,20), best k = 3, bound 4; (9,21) 4 vs 5; (9,24)-(9,29) 3 vs 4; (10,25)-(10,30) 4 vs 5; (10,34)-(10,40) 3 vs 4; (11,35)-(11,40) 4 vs 5; (12,25), (12,26) 5 vs 6; (13,26), (13,27) 6 vs 7; (13,28)-(13,34) 5 vs 6; (14,18)-(14,20) 7 vs 8. For arrays without repeated rows this is equivalent to a binary code of length s and size 2^m whose dual distance (Delsarte) is at least k+1.

## What counts as a win

Success means an explicit 2^m x s array over {0,1} such that every set of k columns contains each of the 2^k binary k-tuples exactly 2^(m-k) times (checked exhaustively, or via all Walsh-Fourier coefficients of weight 1..k vanishing, in exact integer arithmetic), with k STRICTLY GREATER (direction: max) than both MinT's live best known strength for (m,s) on http://mint.sbg.ac.at/query.php?i=o&b=2&m= < m > &s= < s > &p=smk&de=1 (or the table in status_source) and that page's 'Upper bound on k (linear)'. The array is then necessarily non-linear; cells where a linear array could still win belong to codetables-binary-linear. k must also be at most MinT's general upper bound (above it means a bug). No paper, preprint or public table of any date may already reach that strength for (m,s) (MinT lists no new methods after 2008).

## Partial wins

- **p1:** A lowered upper bound: a re-checkable exact certificate proving that no OA(2^m, s, 2, k) exists for k equal to MinT's live upper bound in one of the 131 gap cells, so that the upper bound drops to the best known strength. The certificate is either an LP or SDP dual solution (Delsarte LP with added constraints, or a semidefinite bound) verified in exact rational arithmetic, or a re-runnable exhaustive classification (DRAT proof checked by drat-trim, or two independent programs that agree). It counts only if no paper or preprint already proves that nonexistence (check, e.g., the Bulutoglu-Margot integer-programming classifications and the Boyvalenkov et al. and Kiss-Nagy nonexistence papers).

## How a win is checked

Independent checker: for every k-subset of columns, count the 2^k patterns over all 2^m rows and require 2^(m-k) each; for s = 20, k = 4 this is 4845 subsets of 256 rows. Alternatively compute the Walsh transform of the row multiset and require zero coefficients at all weights 1..k. Read the live MinT cell over http for both the best known value and the bound.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://mint.sbg.ac.at/table.php?i=o&b=2&col=1&mode=e&opt=b&de=1&p=smk&minx=1&maxx=40&miny=0&maxy=25>

## Sources

- <http://mint.sbg.ac.at/table.php?i=o&b=2&col=1&mode=e&opt=b&de=1&p=smk&minx=1&maxx=40&miny=0&maxy=25>
- <http://mint.sbg.ac.at/table.php?i=o&b=2&col=1&mode=ed&opt=bd&de=1&p=smk&minx=1&maxx=40&miny=0&maxy=25>
- <http://mint.sbg.ac.at/query.php?i=o&b=2&s=20&m=8&p=smk&de=1>
- <http://mint.sbg.ac.at/history.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search Z4-linear codes (Gray images) and their shortenings: the known non-linear winners are all of this kind.
- Union-of-cosets constructions: take a linear OA of strength k-1 and choose cosets of a subcode so that the strength-k Fourier coefficients cancel; solve as an exact cover or SAT.
- Lengthen known non-linear OAs (Kerdock K(4), Delsarte-Goethals) by appending columns and repairing with local search on the Walsh spectrum.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A linear array cannot win in these cells: the linear upper bound is a proof.
- MinT counts runs as exactly 2^m; arrays with other run sizes belong to other tables.
- Do not confuse strength (dual distance minus one) with minimum distance.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mint-binary-nonlinear-oa-strength.md
```

Already set up? Say `run V3R1T4S on mint-binary-nonlinear-oa-strength`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mint-binary-nonlinear-oa-strength`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
