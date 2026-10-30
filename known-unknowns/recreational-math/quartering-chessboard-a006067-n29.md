# Ways to quarter an n x n chessboard into four congruent connected pieces: the next term A006067(29) or A006067(30), open since Howroyd's n = 28 in 2016

🎲 **Recreational math** · standard · tractability ★★★☆☆ · compute: laptop-days (transfer matrix over rotationally symmetric partitions) · open as of 2026-10-30

## The problem

A006067(n) counts the ways to dissect an n x n board (central square removed for odd n) into four congruent polyominoes. The problem comes from Popular Computing (Problem 15, 1973, edited by Audrey Gruenberger) and was analysed by Thomas R. Parkin in 1974 (his letters are linked from A257952). For even n the dissections fall into Parkin's two classes: four pieces with 90-degree rotational symmetry, or the board halved into two rectangles and each half cut in two. Both are counted up to rotation and reflection. For odd n every solution has 90-degree symmetry. M. F. Hasler clarified the definition for odd n and the connectivity of the pieces in Jun 2025. Even n is A257952 and odd n is A272070. Andrew Howroyd corrected a(8), computed a(9)-a(22) in Apr 2016 and supplied the b-file to n = 28 (a(28) = 1.12e42); Giovanni Resta illustrated a(8) = 766. Re-fetched 2026-10-30: the A006067 b-file ends at n = 28, and the DATA of A257952 and A272070 ends at n = 14 and n = 13.

## What counts as a win

The exact integer A006067(29) (equivalently A272070(14)) or A006067(30) (A257952(15)), not in the b-file when re-fetched immediately before claiming. It must come from two independent runs that agree exactly, and the same code must reproduce every term of the A006067 b-file for n <= 28.

## Partial wins

- **p1:** An independent program (not Howroyd's) that reproduces every b-file term of A006067 for n <= 28, with code published.
- **p2:** Both A006067(29) and A006067(30), under the same two-run rule.

## How a win is checked

Skeptic: compare the code with the b-file for n <= 16 (minutes) and with Parkin's hand counts for small n, then rerun the claimed term modulo a fresh prime.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A006067/b006067.txt>

## Sources

- <https://oeis.org/A006067>
- <https://oeis.org/A257952>
- <https://oeis.org/A272070>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The definition counts both of Parkin's classes and identifies dissections up to symmetry in a specific way; reproduce the small terms (1,1,1,5,7,37,104,766) before scaling up.
- For odd n the central square is removed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/quartering-chessboard-a006067-n29.md
```

Already set up? Say `run V3R1T4S on quartering-chessboard-a006067-n29`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quartering-chessboard-a006067-n29`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
