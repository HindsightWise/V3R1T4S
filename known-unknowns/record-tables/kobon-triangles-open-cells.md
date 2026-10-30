# Kobon triangles: more triangular faces from n straight lines than the best known, for an n where the record is below the upper bound

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (SAT on pseudoline tables, then straightening; exact integer verification in seconds) · open as of 2026-10-30

## The problem

K(n) is the largest number of triangular faces in an arrangement of n straight lines in the plane (Kobon Fujimura; OEIS A006066). The OEIS table (rev #276, approved 28 Oct 2026) lists these open cells as best known / upper bound U: 11 (32/33, Honma and Kabanovitch; Savchuk, arXiv:2507.07951 v2, excludes 33 only for simple perfect pseudoline arrangements, and Parpalak and Utkin found a counterexample to a Clement-Bader 2007 lemma used to reduce to that case), 18 (93/94), 22 (143/144), 24 (172/173), 26 (204/205), 28 (238/239), 30 (275/276), 32 (315/316), 34 (357/358), 36 (402/404), 38 (450/451), 42 (553/555), 46 (667/669), 50 (792/794). Rows 39, 40, 44, 47 and 48 show '?', and the table stops at n = 50. Pending revision #277 (Fraser King, 29 Oct 2026, github.com/frasertheking/kobon-results) sets 39 >= 475, 40 >= 495, 47 >= 693 and 48 >= 722. The previous values were 471 (lavaskiller, team HTPeo, at the Open Problems Hack at MIT, 2 Oct 2026), 494, 691 and 721; the last three equal the general lower bound below. Row 44 has no OEIS value, but 608 is known (rsi-kobon-triangles table, github.com/Rohith18p/rsi-kobon-triangles, Sep-Oct 2026; King reports that none of the 88 perfect 43-line arrangements in the Parpalak-Utkin gallery gives more with one added line), against U = floor(n(n-7/3)/3) = 611. The King repo gives upper bounds 481, 502, 705 and 736; the even-n bound floor(n(n-7/3)/3) gives 730 for 48. The repo also lists 74 >= 1763 (Parpalak-Utkin have 1764) and 98 >= 3119. Parpalak proposed 53 = 901 and 54 >= 927 in Oct 2026 (revisions #273-275, withdrawn for resubmission). Parpalak and Utkin (arXiv:2607.29236, Jul 2026) found perfect pseudoline arrangements (floor(n(n-2)/3) triangles) for odd n including 39 and 47 by depth-first search; these are combinatorial only, and whether they can be drawn with straight lines is open. General lower bound for n >= 4: floor(n(n-3)/3) + 1 + (n mod 2) (Zarzuelo Urdiales, Zenodo 2026). Records are due to Grünbaum, Kabanovitch, Honma, Suzuki, Bader, Wood, Bartholdi-Blanc-Loisel, Maiorana, Parpalak and Utkin (arXiv:2604.22035), Savchuk, Zarzuelo Urdiales, King, lavaskiller, the rsi-kobon-triangles team and others. The area moves weekly.

## What counts as a win

n distinct straight lines, with 3 <= n <= 50, each given as an integer triple (a,b,c) meaning ax+by+c=0, whose arrangement has T triangular faces (bounded faces with exactly three sides, no line crossing the interior). T is counted with exact integer/rational arithmetic by two independent implementations and must be STRICTLY GREATER (direction: max) than the best known value for that n at verification time. The best known value is the maximum over: the live OEIS A006066 page, its revisions including pending ones (oeis.org/history?seq=A006066) and the illustrations linked from it (including the Parpalak-Utkin galleries), github.com/frasertheking/kobon-results, github.com/Rohith18p/rsi-kobon-triangles (kobon-triangles/RESULTS.md), arXiv:2604.22035, arXiv:2607.29236 and arXiv:2507.07951 (latest versions), Zarzuelo's Zenodo record (including the general bound floor(n(n-3)/3) + 1 + (n mod 2)), and a fresh check. The best known value for n must be below the upper bound U: the U in the OEIS row (or a pending revision) for n or, for a row showing '?', floor(n(n-2)/3) for odd n and floor(n(n-7/3)/3) for even n (481, 502, 611, 705 and 730 for n = 39, 40, 44, 47 and 48). If T exceeds U, the claim goes to review: either the checker or the bound is wrong.

## Partial wins

- **p1:** For some n in 51..100, a verified arrangement (exact integer triples) whose triangle count is strictly greater than floor(n(n-3)/3) + 1 + (n mod 2) and strictly greater than the best value for that n in every source named in the success criterion at verification time (including pending OEIS revisions, the King and rsi-kobon-triangles tables and the Parpalak-Utkin galleries). Re-deriving a known value does not count.
- **p2:** An exact from-scratch recount of a listed record arrangement for an open cell (for example King's 39-, 40-, 47- or 48-line arrangements), published as a replay note that confirms or corrects the listed triangle count.
- **p3:** A certified settlement of the 11-pseudoline case: either a DRAT/LRAT-checked UNSAT proof, with an independently re-derived encoding, that no arrangement of 11 pseudolines (simple or not, parallel classes allowed) has 33 triangular faces, or an explicit such pseudoline arrangement (wiring table) whose 33 triangular faces are checked exactly.

## How a win is checked

Parse the integer triples; reject duplicates. Compute all pairwise intersections exactly (fractions), sort them along each line, and count triples of lines that meet pairwise at three distinct points that are consecutive on each of the three lines and have no other line separating the three vertices. Cross-check with a DCEL face walk that counts 3-sided bounded faces. Both must agree. Re-fetch the OEIS page, its history and the repositories, and record the best value for n with fetch times.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A006066>

## Sources

- <https://oeis.org/A006066>
- <https://oeis.org/history?seq=A006066>
- <https://github.com/frasertheking/kobon-results>
- <https://github.com/Rohith18p/rsi-kobon-triangles>
- <https://arxiv.org/abs/2604.22035>
- <https://arxiv.org/abs/2607.29236>
- <https://arxiv.org/abs/2507.07951>
- <https://doi.org/10.5281/zenodo.23355255>
- <https://arxiv.org/abs/0706.0723>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Savchuk's pipeline: encode a pseudoline arrangement as a wiring table, use SAT (kissat) to force a target number of triangles, then straighten heuristically into lines. Run it on even n near open cells.
- Straighten the perfect 39- and 47-pseudoline arrangements of arXiv:2607.29236 (repository linked there): a straight-line realisation gives 481 or 705 triangles, the upper bound. Prescribing symmetry or fixing many crossings first can help the straightener.
- Bartholdi-Blanc-Loisel and Parpalak-Utkin iterative doubling: extend a base arrangement that meets their conditions to 2n-1 or 18*2^t+1 lines, then do local search on neighbouring n.
- For large n, start from the Füredi-Palasti / Zarzuelo affine construction and do exact integer local moves (perturb one line and re-count) to recover the 1-12 triangle gap to the upper bound.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Counting triangles that are not faces (a line passes through the interior), or counting unbounded 3-sided regions.
- Floating-point intersection ordering; near-coincident vertices flip the combinatorics. Use exact integers.
- Comparing only with the approved OEIS table: pending revisions and the King, rsi-kobon-triangles and Parpalak-Utkin repositories hold newer records (39, 40, 44, 47, 48, 74, 98).
- Pseudoline (wiring) solutions are not line arrangements until straightened and verified with actual lines.
- The upper bounds rest partly on the Clement-Bader lemmas, one of which has a published counterexample; do not cite a U value as proved without checking its source.
- The rsi-kobon-triangles table lists tighter bounds for simple arrangements at some even n (93 at n = 18, 608 at n = 44); check their status, because a win there may need triple points.
- The Open Problems Hack at MIT AutoLab hill (alejandrozu/kobon-triangles) closed with the event on 3 Oct 2026. The bar here is the literature, not the hill; never submit to it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/kobon-triangles-open-cells.md
```

Already set up? Say `run V3R1T4S on kobon-triangles-open-cells`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kobon-triangles-open-cells`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
