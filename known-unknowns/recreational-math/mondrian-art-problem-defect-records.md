# Mondrian Art Problem: a smaller defect than the best known for some n = 67..96 (OEIS A276523), or the exact a(67)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (local search or SAT per n; exact optimality proofs are laptop-days) · open as of 2026-10-30

## The problem

Split an n x n square into at least two integer-sided rectangles, no two congruent (1x2 and 2x4 may both appear, two 1x2 may not). The defect is the largest rectangle area minus the smallest, and a(n) = OEIS A276523(n) is the least defect. Ed Pegg Jr posed it in 2016 as Gordon Hamilton's Mondrian Art Puzzle. Robert Gerbicz computed the optimal values for n = 3..57 and Michel Gaillard for 58..65. DATA now runs to a(66) = 14 (Mia Muessig). On 2025-11-19 Muessig posted best-known tilings for n = 67..96 (file a276523_2.txt). They are marked optimal ('=') for n = 68-70, 72-75, 78 and 83-85 and are only upper bounds ('<=') for 67 (16), 71 (18), 76 (18), 77 (17), 79 (16), 80 (18), 81 (17), 82 (18), 86 (18), 87 (22), 88 (18), 89 (19), 90 (20), 91 (17), 92 (20), 93 (22), 94 (20), 95 (20) and 96 (24). On 2026-10-30 all 31 tilings in that file were re-checked with an independently written checker: each is a valid partition with exactly the stated defect. García-Colín, Leemans, Müßig and Roldán (arXiv:2311.02385, 2023) showed that no perfect (defect 0) partition exists for n <= 1000. Garrison, Seiler and Semchankau (arXiv:2609.01998, 2026) proved an O(n^{5/6}) upper bound but give no per-n values. Pegg's conjectured upper bound ceil(n/log n)+3 is OEIS A278970. The soft cells are 87, 93 and 96, whose values sit well above their neighbours.

## What counts as a win

Success means an explicit partition of an n x n square, with n one of 67, 71, 76, 77, 79, 80, 81, 82 or 86..96 (any n whose live A276523 entry still marks the value as only best known), into k >= 2 axis-parallel integer-sided rectangles that are pairwise non-congruent (no two share the same unordered side pair), tile the square exactly and have defect (max area - min area) STRICTLY less than the best-known value for that n in the live A276523 entry, its linked a276523_2.txt and records/values.txt of https://github.com/PhoenixSmaug/mondrian-heuristic (Muessig and Garrison's best-value table for every n up to 3000; on 2026-10-30 it agrees with the OEIS values for 67..96). All three must be re-fetched immediately before claiming, and the OEIS history (including pending drafts) checked for a newer value. The partition is given as a list of rectangles (x, y, w, h) or as an n x n letter grid in Muessig's format.

## Partial wins

- **p1:** The exact value of a(67) (best known 16): an exhaustive search proving that no valid partition of the 67 x 67 square has defect <= 15 (or a better tiling, which is a full win), done by two independently written programs that both reproduce every DATA value a(3)..a(66) of A276523.
- **p2:** An extension of the García-Colín–Leemans–Müßig–Roldán result: a computer proof by two independent programs that no perfect (defect 0) Mondrian partition exists for every n <= N, with N >= 1100. It is labelled as a bounded result.
- **p3:** A perfect (defect 0) Mondrian partition of an n x n square for some n > 1000. Nobody has proved it impossible. Verified exactly.

## How a win is checked

Parse the grid or rectangle list. Check that it covers n x n exactly with no overlap (each letter's cells form a full w x h block), that the unordered dimension pairs are pairwise distinct and that k >= 2. Compute max area minus min area and compare with the live value for n. This takes milliseconds. For p1/p2, rerun both programs, check that they reproduce the b-file, and compare their logs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A276523>

## Sources

- <https://oeis.org/A276523>
- <https://oeis.org/A276523/a276523_2.txt>
- <https://github.com/PhoenixSmaug/mondrian-heuristic>
- <https://arxiv.org/abs/2311.02385>
- <https://arxiv.org/abs/2609.01998>
- <https://oeis.org/A278970>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Fix the rectangle multiset first: choose a window of allowed areas [A, A+d] and enumerate the distinct dimension pairs with area in the window and sides <= n. Their total area must reach n^2 with distinct shapes. Then run an exact-cover / SAT packing of the square (Gerbicz's and Muessig's approach).
- Exploit near-symmetric layouts: many optimal tilings for large n are 'pinwheel plus strips'. Search over guillotine and pinwheel skeletons first, then refine with CP-SAT.
- From VLSI floorplanning: represent candidate tilings as sequence pairs and anneal over them, with an exact feasibility check per window.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Congruent means the same unordered dimensions. Similar rectangles are allowed, and rotated copies of one shape are NOT allowed.
- Muessig's comment and the a(66)..a(96) file supersede the older 2024 best-known list (also in the comments). Compare with the newest one.
- Values marked '=' or '*' (68-70, 72-75, 78, 83-85) are proven optimal and cannot be beaten.
- A single 1-rectangle 'tiling' is excluded (k >= 2).
- The Muessig-Garrison hierarchical heuristic (github.com/PhoenixSmaug/mondrian-heuristic, October 2026 census at 240 s per n) is tuned for large n: at every open n in 67..96 it lands 3 to 12 above the best known (23 vs 16 at n = 67), so running it unchanged will not win here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/mondrian-art-problem-defect-records.md
```

Already set up? Say `run V3R1T4S on mondrian-art-problem-defect-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mondrian-art-problem-defect-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
