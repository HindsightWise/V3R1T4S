# No three collinear in the n x n x n grid (OEIS A399138): beat a(7) >= 73, a(8) >= 94, a(9) >= 116, a(10) >= 138 or a(11) >= 164

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (CP-SAT or local search inside symmetry strata; a witness is checked in seconds) · open as of 2026-10-30

## The problem

a(n) is the largest number of points of {0..n-1}^3 with no three collinear in R^3. Pór and Wood (Algorithmica 2007) proved a(n) = Theta(n^2). The trivial upper bound is 2n^2, since each of the 3n^2 axis-parallel lines holds at most two points. Aleksei Kudriashov, 'Certified computations on no-three-in-line problems...', arXiv:2609.25133 (v1, 20 Sep 2026), determined a(1..6) = 1, 8, 16, 28, 40, 64 with SAT decision procedures. Single-call instances carry drat-trim-checked DRAT proofs; the split n = 6 instances rest on one solver, with certificates regenerated on demand. The sequence became OEIS A399138 in Aug 2026. He gave verified lower bounds a(7) >= 73, found by restricting the search to a cyclic axis symmetry after randomised search stalled at 71. The bounds a(8) >= 94, a(9) >= 116, a(10) >= 138 and a(11) >= 164 came from a CP-SAT sweep over the 33 conjugacy classes of subgroups of the cube group (25-40 minutes per class). He also proved a(p) >= p^2 for every prime p. He calls the randomised bounds weak. Earlier, on SeqFan (June 2026), Ed Pegg and Lucas Brown gave a(1..5) and the bounds a(7) >= 72, a(8) >= 91, and Rob Pratt confirmed a(5) = 40 and a(6) = 64 by integer linear programming; Henry Nance (SeqFan, 24 Oct 2026) independently found 73, 92, 116 and 134 for n = 7..10 with symmetry-restricted CP-SAT, none above Kudriashov's values. The layer pattern of the small optima suggests 2n^2-2n+4 = 88 at n = 7; that exact layer profile is infeasible, but the value 88 is not excluded. A399138 (revision #39, 27 Oct 2026, comment updated by Eric W. Weisstein) lists a(7) >= 73 and a(8) >= 94 with keyword 'more'. MathWorld (updated 29 Oct 2026) gives the same values and notes that they beat a 93-point n = 8 example illustrated by Ed Pegg (2026).

## What counts as a win

A set S in {0..n-1}^3 for some n in 7..11 with no three points collinear (checked over all C(|S|,3) triples with exact integer cross products), and |S| STRICTLY GREATER (direction: max) than the best lower bound for that n at verification time. On 2026-10-30 these were 73 (n=7), 94 (n=8), 116 (n=9), 138 (n=10) and 164 (n=11), from arXiv:2609.25133 and OEIS A399138. Re-read the live OEIS entry, its linked files and the Kudriashov repository first. |S| > 2n^2 is impossible and means a bug.

## Partial wins

- **p1:** The exact value a(7) or a(8). Give a witness of size m together with a checked DRAT/LRAT (or cake_lpr-verified) proof that no set of size m+1 with no three collinear exists in [n]^3. The proof file can be published outside git.
- **p2:** A certified upper bound a(7) <= 97, that is, any bound below the trivial 2n^2 = 98, given by a checked unsatisfiability proof without the matching witness. The skeptic first confirms that no published argument already gives a bound below 98 at n = 7.

## How a win is checked

An independent script: confirm the coordinates lie in [0,n-1] and are distinct, and test every triple (p,q,r) by checking that (q-p) x (r-p) is the zero vector in integers. Calibrate on the a(6) = 64 witness from the OEIS a399138.txt file (must pass) and on a corrupted copy with one point moved onto a line (must fail). For p1 and p2, re-encode the CNF from the problem definition and check that it is identical (up to variable renaming) to the one the proof refers to, then run drat-trim or cake_lpr.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A399138>

## Sources

- <https://arxiv.org/abs/2609.25133>
- <https://oeis.org/A399138>
- <https://github.com/iwasborninbali/saturation>
- <https://doi.org/10.1007/s00453-006-0158-9>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Symmetry strata: the best n = 8 witnesses came from order-4 subgroups; medium-size groups (orders 3-6) balance solver reach against richness of solutions.
- For n = 11 and 13 compare with the quadratic-form construction (x, y, Q(x,y) mod p) plus extra points in unused fibres.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Collinearity is in R^3, not mod n.
- Do not confuse with the planar problem (A000769, already a bank target) or with the no-four-coplanar problem (A280537).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/no-three-collinear-cube-a399138.md
```

Already set up? Say `run V3R1T4S on no-three-collinear-cube-a399138`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `no-three-collinear-cube-a399138`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
