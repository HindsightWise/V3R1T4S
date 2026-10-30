# 16 x 16 Sudoku with 54 or fewer clues: beat the 55-clue record (OEIS A198297, 15 <= a(4) <= 55)

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-days (one uniqueness check by SAT takes seconds; the cost is the search) · open as of 2026-10-30

## The problem

OEIS A198297(n) is the fewest givens in a uniquely solvable n^2 x n^2 Sudoku. a(3) = 17 (McGuire, Tugemann and Civario, Exp. Math. 2014). For 16 x 16 with 4 x 4 boxes the entry states 15 <= a(4) <= 55. The lower bound is the trivial n^2 - 1 bound (David Radcliffe, 2019); the entry carries keywords hard and more and was last edited in January 2026 with the bound unchanged. The 55-clue record was posted by 'ton' on the New Sudoku Players' Forum (thread 'Minimum givens on larger puzzles', 1 Apr 2015, citing a Japanese puzzle book) and transcribed by m_b_metcalf. It improved T_Shirakawa's 56 (May 2011) and gsf's 77 (2006). No smaller puzzle has been posted since: the thread's last post is from June 2024, and the separate thread 'minimum number of clues 16x16 and higher' ends in 2017 pointing to the 55. We re-verified the 55-clue puzzle printed in A198297 on 2026-10-30 with two independent SAT checks: unique solution, and minimal. ton's empirical formula floor(N^2/4) - (h-1)(w-1) gives exactly 55 here. His records also meet it for 3x4, 3x5 and 4x5 boxes, so 54 would beat both the record and the community's heuristic. Target: a 16 x 16 puzzle with at most 54 clues and a unique solution, or a certified proof that a(4) = 55.

## What counts as a win

Success means either (a) a 16 x 16 array of givens (values 1..16; standard rows, columns and 4 x 4 boxes) with at most 54 givens (STRICTLY fewer than 55; direction: min) that has exactly one completion; or (b) a machine-checked proof that no 16 x 16 puzzle with at most 54 givens has a unique completion. Uniqueness in (a) must be shown either by a solution plus a DRAT/LRAT-checked UNSAT proof (drat-trim or cake_lpr) for 'givens AND NOT that solution', or by two independent exact solvers (e.g. DLX and a CDCL SAT solver) each reporting exactly one solution. In both cases, re-fetch OEIS A198297 (https://oeis.org/A198297 and https://oeis.org/history?seq=A198297) and the last page of http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801.html immediately before claiming; they must still show 55 as the best known.

## Partial wins

- **p1:** A uniquely solvable, minimal 16 x 16 puzzle with exactly 55 clues that provably differs from every 55-clue puzzle posted in A198297 or the 'Minimum givens on larger puzzles' thread (on 2026-10-30 only ton's). Proof of difference: its sorted per-digit clue counts, or its sorted per-box clue counts, differ from each known 55's. Both are invariant under Sudoku symmetries and relabelling.
- **p2:** A certified proof that a(4) >= 16, i.e. that no 16 x 16 puzzle with 15 givens has a unique completion. It needs a DRAT/LRAT certificate, or an exhaustive search reproduced by two independent implementations.

## How a win is checked

Parse the 256 cells and count the givens. Encode the puzzle as CNF (4096 variables). Get one model, block it, and check UNSAT with a proof log (about 3 s with pysat/CaDiCaL for the 55-clue example). Cross-check with a DLX solver. For p1, recompute the two invariants. For (b), check the proof with drat-trim or cake_lpr, and check that the encoding reproduces a(2) = 4 and known 9 x 9 facts.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A198297>

## Sources

- <https://oeis.org/A198297>
- <http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801.html>
- <http://forum.enjoysudoku.com/minimum-givens-on-larger-puzzles-t4801-30.html>
- <https://arxiv.org/abs/1201.0749>
- <https://oeis.org/A372224>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Neighbourhood search {-k+m} around ton's 55 (remove k clues, add m) as was done for 9 x 9 17s and 39s, using a fast 16 x 16 SAT/bitset uniqueness test.
- Pick solution grids with many automorphisms or few unavoidable sets, as with the 9 x 9 'MC grid' studies; hitting-set enumeration over unavoidable sets (McGuire et al.) for a fixed grid finds its minimum-clue puzzles.
- Start from the qiuyanzhe / hkociemba constructions (about floor(N^2/4) = 64 clues) and reduce.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Only 4 x 4 boxes count here; other box shapes are the separate rectangular-box target.
- Hex formats (0-F vs 1-G vs 1-16) cause off-by-one transcription errors; ton's 55 was hard to read even for forum veterans.
- Lass (2012) and Cooper-Kirkpatrick (Discrete Math 2014) study critical sets of generalized Sudoku; check them before claiming any lower bound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/sudoku-16x16-fewer-than-55-clues.md
```

Already set up? Say `run V3R1T4S on sudoku-16x16-fewer-than-55-clues`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sudoku-16x16-fewer-than-55-clues`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
