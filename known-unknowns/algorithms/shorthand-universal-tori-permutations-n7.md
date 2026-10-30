# Shorthand universal tori for permutations of [7]: an R x C torus with 2x3 windows for some R >= 3 (only 2-row tori are known)

⚡ **Algorithms** · standard · tractability ★★☆☆☆ · compute: laptop-days (backtracking or SAT over 5040 cells; a torus checks instantly) · open as of 2026-10-30

## The problem

A shorthand universal torus is an R x C toroidal array over [n] with R*C = n!. Each (n-1)-permutation of [n] (a permutation with its redundant last value dropped) must appear exactly once as an r x c window read in row-major order, where r*c = n - 1 and windows wrap in both directions. Gerlach, Hartung, Herkenrath, Sawada and Williams, 'Shorthand Universal Tori for Permutations: Existence, Symmetry, and Generation of Twori' (arXiv:2609.27583 v1, 23 Sep 2026), prove that 2-row tori with 2 x m windows exist for every odd n = 2m + 1 (Theorem 1). They settle n = 5 with 2 x 2 windows completely: tori exist for 2x60, 4x30, 6x20 and 8x15, and none exist for 1x120, 3x40, 5x24 and 10x12. Two independent backtracking programs established this, with hand proofs for 3x40 and 5x24. Their final remarks name as the main open problem 'for which values (R,C,r,c) do shorthand universal tori exist'. For n = 7 (2 x 3 windows, or 3 x 2 on the transpose) only R = 2 is settled; no search beyond n = 5 is reported.

## What counts as a win

Success means an explicit R x C array over {1..7} with R*C = 5040, R dividing 5040 and 3 <= R <= 1680 (so that C >= 3), in which every 2 x 3 window (read row-major, wrapping toroidally) is a 6-permutation of [7] and all 5040 such 6-permutations occur exactly once. Two independent checkers must confirm it. A torus with 3 x 2 windows counts as the transposed case. Existence for any R other than 2 is new as of 2026-10-30: arXiv:2609.27583 and later sources settle no n = 7 case except R = 2.

## Partial wins

- **p1:** A rerunnable nonexistence proof for one n = 7 case (R, C) with 2 x 3 windows and R >= 3: a written proof, an UNSAT certificate (DRAT/LRAT, checked by a verified checker) of a published encoding, or two independent exhaustive programs that agree (labelled computational). It counts only if that case is unsettled in the latest version of arXiv:2609.27583 at claim time.
- **p2:** An explicit shorthand universal torus for n = 9 with 2 x 4 windows and R >= 3 rows, verified the same way.

## How a win is checked

For each of the R*C top-left positions, read the window cells (i+a mod R, j+b mod C) for a < 2 and b < 3 in row-major order, check that the six values are distinct, and insert the tuple into a set. Check that the set has 5040 elements. Calibrate on the paper's n = 5 example tori (Figure 3, 2 x 2 windows) and on its 2-row construction (Theorem 1).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.27583>

## Sources

- <https://arxiv.org/abs/2609.27583>
- <http://debruijnsequence.org/db/perm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Count symbol occurrences per column first, as in the paper's 3 x 40 argument; this decides quickly which R values for n = 7 are blocked by counting, so search effort goes only to the rest.
- Stack copies of a 2-row twori with shifted symbol relabellings so that the window rows crossing the seam are also new.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Windows are read row-major, and the omitted last symbol is the one missing from the window.
- Some (R, C) may fall to a simple counting argument; a nonexistence proof is only a partial win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/shorthand-universal-tori-permutations-n7.md
```

Already set up? Say `run V3R1T4S on shorthand-universal-tori-permutations-n7`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `shorthand-universal-tori-permutations-n7`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
