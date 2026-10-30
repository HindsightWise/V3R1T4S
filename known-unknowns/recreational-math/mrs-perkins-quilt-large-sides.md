# Mrs Perkins's quilt: a coprime squared square with at most n squares and a larger side than the best known (OEIS A089047/A089046, n >= 19)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (search over squared-rectangle building blocks); exact proofs laptop-days · open as of 2026-10-30

## The problem

Mrs Perkins's quilt: tile a k x k square with integer squares whose sides have gcd 1, using as few squares as possible. A005670(k) is that minimum, and Ed Wynn's exhaustive generation (arXiv:1308.5420, 2013) proved it correct for k <= 120. The inverse sequences give the largest square side reachable with at most n squares (A089047) and the least side forcing at least n squares (A089046). Wynn proved A089047 through a(18) = 91. The rest are best known only: A089047(19..33) = 126, 158, 216, 276, 386, 488, 675, 866, 1179, 1544, 2136, 2739, 3755, 4988, 6443. Ed Pegg Jr (2017-07-06) added further best-known terms for n = 34..39 as an OEIS comment: 8568, 11357, 14877, 19594, 26697, 34632. He calls the tables 'almost certainly correct up to 5000', and N. J. A. Sloane deleted DATA terms above 5000. Pegg's July 2017 update on Stuart Anderson's squaring.net extends the best-known quilts to every side up to 40,000. It was built from the squaring.net SPSS and SISS collections (Duijvestijn, Skinner, Anderson, Pegg, Johnson, Milla, Williams and others) by recursive 'builds' from about 65 million prime quilts. Pegg calls that list very reliable only up to 33 squares and says the records are fragile. He expected about 10 solutions up to size 10000 to change once the complete SPSS/SISS collections to order 37 were processed. Jim Williams completed the SPSS enumeration to order 37 in 2020. Earlier contributors include Richard K. Guy, Lance Gay and Geoffrey Morley. J. H. Conway and G. B. Trustrum showed that the answer grows like log k. The weakest records are those for n >= 34 and sides above about 5000.

## What counts as a win

Success means an explicit dissection of a k x k square into m integer-sided squares with gcd of all sides = 1 and 2 <= m <= n, for some n with 19 <= n <= 39, where k is STRICTLY greater than the best-known value of A089047(n) (DATA for n <= 33, Pegg's listed further terms for n = 34..39), both re-fetched live immediately before claiming. Squares need not be distinct. The dissection is given as a list of (x, y, s) or a Bouwkamp code. It must not already appear in squaring.net's Mrs Perkins's Quilts list or the OEIS history.

## Partial wins

- **p1:** For some side k with 121 <= k <= 40000, a coprime dissection of the k x k square into fewer squares than the count on Pegg's best-known list (squaring.net MrsPerkinssQuilts.txt.zip, July 2017), verified exactly.
- **p2:** An extension of Wynn's proved range: exact A005670(k) for every k from 121 up to some K >= 130, by an exhaustive search run with two independent programs that both reproduce Wynn's b-file for k <= 120.
- **p3:** A proof (exhaustive, two independent programs, with checkable logs) that A089047(19) = 126 is optimal, i.e. that no coprime quilt with at most 19 squares has side > 126.

## How a win is checked

Check exact coverage of the k x k grid by the listed squares (an integer sweep or cell count with no overlap), that gcd of the sides is 1, and that the number of squares is <= n. Compare k with the live A089047 entry. This takes milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A089047>

## Sources

- <https://oeis.org/A089047>
- <https://oeis.org/A089046>
- <https://oeis.org/A005670>
- <http://www.squaring.net/quilts/mrs-perkins-quilts.html>
- <https://arxiv.org/abs/1308.5420>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Large good quilts glue a near-square imperfect squared rectangle to one big square. Search over squared rectangles of order <= n-1 with aspect close to 1 (Bouwkamp codes from plantri-generated c-nets) and complete each to a square.
- Run Pegg's construction in reverse: start from his best quilts for n = 33..39 and try local Bouwkamp-code mutations that keep the square shape while growing the side.
- From electrical network theory: the side equals a spanning-tree-count determinant. Optimise the network's complexity over planar graphs with n+1 edges using Kirchhoff's theorem.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- gcd = 1 is required: scaling a smaller quilt is not allowed.
- Values for k <= 120 (A005670) are proven, so a quilt with side <= 120 cannot be a win.
- A089046 and A089047 are inverse sequences with different directions. Use the stated criterion (larger side with at most n squares).
- Pegg's further terms are in comments, not DATA. Re-read the live entry: terms may have been added or corrected.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/mrs-perkins-quilt-large-sides.md
```

Already set up? Say `run V3R1T4S on mrs-perkins-quilt-large-sides`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mrs-perkins-quilt-large-sides`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
