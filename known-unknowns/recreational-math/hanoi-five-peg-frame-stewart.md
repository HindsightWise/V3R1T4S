# MOONSHOT - Tower of Hanoi with five or more pegs: a move sequence shorter than Frame-Stewart, or an extension of the exhaustive verification beyond Hinz-Petr's frontier

🎲 **Recreational math** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (Hinz and Petr ran their Hanoi-graph BFS on SuperMUC-NG; checking a claimed short sequence is laptop-minutes) · open as of 2026-10-30

## The problem

Move a tower of n discs from one peg to another with p pegs, never placing a larger disc on a smaller one. The Frame-Stewart algorithm (1941) uses FS_p(n) = min over m of 2*FS_p(m) + FS_{p-1}(n-m), with FS_3(n) = 2^n - 1 (OEIS A007664 for 4 pegs, A007665 for 5, A182058 for 6). Frame-Stewart is proven optimal for 4 pegs (Thierry Bousch, 2014). For p >= 5 its optimality is the open Frame-Stewart conjecture. Exhaustive breadth-first search on Hanoi graphs has confirmed it for p = 5 and n <= 20, p = 6 and n <= 16, and p = 7 and n <= 21, as reported by Andreas M. Hinz and Ciril Petr at the SuperMUC-NG Status and Results Workshop on 2023-05-10 (LRZ project pr87mo). Earlier large exhaustive searches (Korf 2004; Korf and Felner 2007; Houston and Masum 2004) concerned four pegs. This lane recomputed the next unverified values from the recurrence: FS_5(21) = 127, FS_6(17) = 65, FS_7(22) = 79.

## What counts as a win

For some p >= 5 and n, an explicit legal move sequence that transfers a perfect tower of n discs from peg 0 to peg 1 in strictly fewer than FS_p(n) moves, where FS_p(n) is computed from the recurrence. That would disprove the Frame-Stewart conjecture. By Hinz-Petr, such an n must exceed 20 for p = 5, 16 for p = 6 and 21 for p = 7.

## Partial wins

- **p1:** A complete, re-runnable exhaustive search, with released code and per-layer (or per-distance) state counts, that confirms d_p(0^n, 1^n) = FS_p(n) for a case beyond Hinz-Petr's frontier: (p, n) = (5, 21) with value 127, (6, 17) with value 65, or (7, 22) with value 79. It must be independently re-run, at least on a reduced instance and on a random sample of the search.

## How a win is checked

For a move sequence: simulate on p stacks, check that every move takes the top disc and places it on an empty peg or a larger disc, check the final state, and count the moves. Compare with FS_p(n) from the recurrence in exact integers. For a verification claim: rerun the search over all legal states (a breadth-first search on the Hanoi graph, as Hinz and Petr ran it, or a Korf-Felner-style search that exploits the symmetry of the 0^n to 1^n problem), reproduce the published smaller cases and per-layer counts, and check that the code computes the true distance and not a restricted subtower distance.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://doku.lrz.de/files/10746622/10746632/5/1721986246983/Hinz_Petr_Eccentricities_in_Hanoi_Graphs.pdf>

## Sources

- <https://doku.lrz.de/files/10746622/10746632/5/1721986246983/Hinz_Petr_Eccentricities_in_Hanoi_Graphs.pdf>
- <https://oeis.org/A007665>
- <https://oeis.org/A182058>
- <https://oeis.org/A007664>
- <https://arxiv.org/abs/2511.07501>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Searching only Frame-Stewart-style (subtower) strategies cannot disprove the conjecture. The search must range over all legal states.
- The four-peg case is settled (Bousch 2014). A shorter four-peg sequence is impossible.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/hanoi-five-peg-frame-stewart.md
```

Already set up? Say `run V3R1T4S on hanoi-five-peg-frame-stewart`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hanoi-five-peg-frame-stewart`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
