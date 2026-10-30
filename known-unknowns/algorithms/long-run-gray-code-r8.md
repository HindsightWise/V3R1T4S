# Gray codes with long bit runs: an 8-bit Gray code whose bit runs all have length at least 6, or a proof that r(8) = 5

⚡ **Algorithms** · standard · tractability ★★☆☆☆ · compute: laptop-days (SAT/CP or clever backtracking; naive DFS does not even reproduce r(7) = 5 in 30 s) · open as of 2026-10-30

## The problem

For a cyclic n-bit Gray code, the run length of a coordinate is the number of steps between two consecutive flips of that coordinate. Let r(n) be the largest r such that some n-bit Gray code has all run lengths at least r. Knuth (TAOCP 4A, Sec. 7.2.1.1) gives r(n) = 1, 2, 2, 2, 4, 4, 5 for n = 1..7, and his Fig. 34 shows an 8-bit code with all runs at least 5. The value r(8) is unknown. Goddyn and Gvozdjak (Electron. J. Combin. 10, 2003) proved r(n) >= ceil(n - 2.001 log2 n), building on Evdokimov and on Goddyn-Lawrence-Nemeth; that bound gives only 2 for n = 8. Mütze's survey (arXiv:2202.01280 v4, 30 Jul 2024, Problem P8) lists r(n) for n >= 8 as open. Such codes are used in image detectors and structured light. A Semantic Scholar citation check on 2026-10-30 found no paper settling r(8).

## What counts as a win

Success means settling whether r(8) >= 6. (a) An explicit cyclic 8-bit Gray code (256 distinct words, single-bit steps including last to first) in which, for every coordinate, any two cyclically consecutive flips of that coordinate are at least 6 steps apart. This shows r(8) >= 6 (direction: max; context: best known 5, Knuth Fig. 34). It must pass two independent checkers. (b) A proof that r(8) = 5: an UNSAT certificate (DRAT/LRAT, checked by a verified checker) of a published encoding with a correctness note.

## Partial wins

- **p1:** An explicit 8-bit Gray path (all 256 words, single-bit steps, not necessarily closing) in which any two consecutive flips of the same coordinate are at least 6 steps apart. It counts only if none is published at claim time.

## How a win is checked

Compute the transition sequence d_1..d_256 (cyclic) and check that all words are distinct. For each coordinate, list its flip positions and check that every cyclic gap between consecutive flips is >= 6. Calibrate the gap convention by verifying Knuth's 8-bit code (gaps >= 5), finding 5-bit codes with gaps >= 4, and confirming that no 5-bit code has gaps >= 5 (r(5) = 4).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2202.01280>

## Sources

- <https://arxiv.org/abs/2202.01280>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v10i1r27>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Encode the transition sequence directly: 256 positions over 8 values, with each coordinate absent from any window of 6 consecutive positions containing it (a sliding-window cardinality constraint) and a Hamiltonicity side condition checked lazily or by prefix-XOR distinctness.
- Look for codes whose transition sequence is periodic under a coordinate permutation (for example 4 blocks of 64 related by a cyclic relabelling).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Gap conventions: a run of length r means flips at positions i and i + r. Calibrate on r(5) = 4 and r(7) = 5.
- The code must be cyclic for the full win; the wrap-around gaps count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/long-run-gray-code-r8.md
```

Already set up? Say `run V3R1T4S on long-run-gray-code-r8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `long-run-gray-code-r8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
