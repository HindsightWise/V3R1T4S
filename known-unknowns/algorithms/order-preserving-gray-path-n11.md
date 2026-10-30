# Felsner-Trotter order-preserving Gray paths: one for n = 11 (open for all n >= 11), or the exact count for n = 8 (OEIS A259839)

⚡ **Algorithms** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (backtracking or SAT; a path of 2048 subsets checks in milliseconds) · open as of 2026-10-30

## The problem

An order-preserving Gray path lists all 2^n subsets of [n] as x_1 = empty set, ..., x_N with consecutive sets differing in one element, such that whenever x_i is obtained from x_j by removing one element (a 1->0 flip), i <= j + 1. Felsner and Trotter posed the problem (Discrete Math. 144, 1995) and built such paths of length 2^(n-1)(1 + o(1)); see also Jackson-Stevens-Hurlbert, Research problems on Gray codes and universal cycles, Problem 483. OEIS A259839 (Torsten Mütze, 2015; revision 27, 30 May 2026) counts these paths up to renaming coordinates: 1, 1, 1, 1, 1, 10, 123, 1492723 for n = 0..7. It states that a(n) >= 1 is known for n = 8, 9, 10 (found by Trotter and Mütze independently) and that it is unknown whether a(n) >= 1 for n >= 11. Biró and Howard (Order 26, 2009) built, for all n >= 11, an order-preserving path through every subset of size at most 3. Mütze's survey (arXiv:2202.01280 v4, Problem P6) calls existence for n >= 11 a challenging open problem. Independent backtracking counters reproduced 10 and 123 for n = 5 and 6 (labelled counts 1200 and 88560 divided by n!).

## What counts as a win

Success means an explicit order-preserving Gray path for some n >= 11: a list of all 2^n subsets of [n], each exactly once, starting from the empty set, consecutive sets at symmetric-difference size 1, and for every pair A ⊂ B with |B| = |A| + 1 the position of A at most the position of B plus 1. It must be verified by two independent checkers, and it must also satisfy the stronger all-subset-pairs reading (A ⊂ B of any sizes) used in the OEIS comment. Existence is the criterion: none is known at any n >= 11 (context 2026-10-30, OEIS A259839).

## Partial wins

- **p1:** The exact value a(8) of OEIS A259839 (order-preserving paths in the 8-cube up to coordinate renaming), computed by two independently written programs that agree, each first reproducing a(5) = 10, a(6) = 123 and a(7) = 1492723. It counts only if a(8) is still absent from the OEIS entry at claim time; the result is labelled computational.

## How a win is checked

Record the position pos[S] of each subset. Check that all 2^n subsets appear, that pos[empty] = 0, and that consecutive sets differ in exactly one element. For every S and every element e of S, check that pos[S minus e] <= pos[S] + 1. Run the all-pairs version (for all A ⊂ B) as a second check; for n = 11 it takes 3^11 pair checks. Calibrate by enumerating n = 5, 6 and reproducing 10 and 123 (labelled counts divided by n!).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A259839>

## Sources

- <https://oeis.org/A259839>
- <https://arxiv.org/abs/2202.01280>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The rule forces strong structure: after visiting a set, at most one unvisited lower cover may remain and it must come next. Paths are level-accurate (Felsner-Trotter), which allows level-by-level dynamic programming with pruning.
- Extend the n = 10 solution: search for paths whose restriction to sets not containing element 11 resembles a known n = 10 path, then repair with SAT.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The rule says that a set may not come more than one step after any set obtained from it by adding an element: subsets are visited before their supersets, or immediately after them. A monotone or level-accurate path (Savage-Winkler) is not enough.
- Counts in A259839 are up to coordinate renaming: divide labelled counts by n!.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/order-preserving-gray-path-n11.md
```

Already set up? Say `run V3R1T4S on order-preserving-gray-path-n11`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `order-preserving-gray-path-n11`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
