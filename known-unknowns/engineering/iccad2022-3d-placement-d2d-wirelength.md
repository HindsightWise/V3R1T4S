# ICCAD 2022 CAD Contest Problem B (3D placement with D2D vertical connections): a shorter legal 3D placement than the best published

🛠️ **Engineering and chips** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (2.7k to 221k cells); the evaluator runs in seconds to minutes · open as of 2026-10-30

## The problem

ICCAD 2022 CAD Contest Problem B, set by Synopsys Taiwan (K.-S. Hu, I.-J. Lin, Y.-H. Huang, H.-Y. Chi, Y.-H. Wu and C.-F. C. Shen, ICCAD 2022), asks for a partition of a netlist into two face-to-face bonded dies, possibly in different technologies. Each die has its own maximum utilisation and row structure. Hybrid bonding terminals (HBTs) of fixed size and spacing must be placed for every cut net, and the objective is the total HPWL of both dies, counted through the terminals. The contest is over. The public cases (case2, case3, case4), the hidden cases (case2h, case3h, case4h) and the official evaluator are on the contest's Problems page (public Google Drive links). The best published results are from Liao, Zhao, Guo, Lin and Yu ('Analytical Die-to-Die 3-D Placement With Bistratal Wirelength Model and GPU Acceleration', IEEE TCAD 43(6) 2024; arXiv 2310.07424, Table II, official evaluator): case2 1944656, case2h 2462553, case3 30062713, case3h 26727327, case4 267400694 and case4h 289245472. In the same table the contest first place scored 2072075 / 2555461 / 30580336 / 27650329 / 281315669 / 301193374, the second place 274026687 on case4, and the analytical placer MTWA (Chen et al., DAC 2023) 2011447 / 2514597 / 30302643 / 27135602 / 272327370 / 296655075. CoPlace (Fu et al., ASP-DAC 2024) reports 270141472 on case4 and 292195136 on case4h, which is not better.

## What counts as a win

A placement output in the contest's output format, for one of case2, case2h, case3, case3h, case4 or case4h as released on the ICCAD 2022 contest Problems page. The official Problem B evaluator must report it legal: every cell on a row of its assigned die with no overlap, per-die utilisation within the stated maximum, and terminals of the stated size and spacing inside the die. Its reported total wirelength (score) must be strictly below the value listed for that case from Liao et al. TCAD 2024 Table II. Direction: minimise. It must also be below any later published value for the same case found at claim time.

## Partial wins

- **p1:** A legal solution for any of the six cases whose evaluator score is strictly below every other published value for that case (the 1st, 2nd and 3rd place and MTWA columns of Liao et al. TCAD 2024 Table II, and CoPlace ASP-DAC 2024 Table II), but not below Liao et al.'s.
- **p2:** A legal solution for case4h with evaluator score below 301193374 (contest first place) using fewer HBTs than the 47712 of Liao et al.'s published case4h result.

## How a win is checked

Download the case files and the evaluator from the Problems page (record sha256). Run the official evaluator on the claimed output and read its legality report and wirelength. Independently, a short script parses the case and output files, recomputes each net's HPWL on each die through its terminal, and checks for overlaps, row alignment, utilisation and terminal spacing. Calibrate the script against the evaluator on a trivial legal placement before use. Compare with TCAD 2024 Table II. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2310.07424>

## Sources

- <https://www.iccad-contest.org/2022/Problems.html>
- <https://arxiv.org/abs/2310.07424>
- <https://www.cse.cuhk.edu.hk/~byu/papers/J106-TCAD2024-3DPlace.pdf>
- <https://bunchgrape.github.io/docs/aspdac24_3dplace.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Polish the published-style flow: alternate die reassignment of boundary cells (FM with an HPWL gain) and per-die 2D detailed placement (independent-set matching, global swap), then re-optimise terminal locations exactly per net (median of the two dies' pin boxes).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The evaluator binary and case files were updated several times in 2022 (hidden cases 11/4). Use the final versions and record the file hashes.
- Scores are the official evaluator's wirelength, not a self-computed HPWL with different terminal handling. Two dies may use different technologies (cell sizes differ per die).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/iccad2022-3d-placement-d2d-wirelength.md
```

Already set up? Say `run V3R1T4S on iccad2022-3d-placement-d2d-wirelength`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `iccad2022-3d-placement-d2d-wirelength`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
