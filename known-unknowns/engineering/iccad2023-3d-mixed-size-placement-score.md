# ICCAD 2023 CAD Contest Problem B (3D placement with macros): a lower HPWL + 10 x HBT score than the best published

🛠️ **Engineering and chips** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (14k to 740k instances, 6 to 34 macros); the evaluator runs in minutes · open as of 2026-10-30

## The problem

ICCAD 2023 CAD Contest Problem B, '3D Placement with Macros' (Hu, Chi, Lin, Wu, Chen and Hsieh, Synopsys, ICCAD 2023), extends the 2022 face-to-face 3D placement problem to mixed-size designs with movable, rotatable macros on two dies, mostly in heterogeneous technologies. The official raw score is total D2D HPWL + beta * #HBTs, with beta = 10 in all cases. The contest is over. Cases case2, case2h1, case2h2, case3, case3h, case4 and case4h, the evaluator and the final results are linked from the 2023 Problems page. The contest first place (official) scored 16506066 / 18123044 / 18124483 / 98928220 / 122459408 / 1047716115 / 656528147; the second place was lower on case2 (16287082) and the third on case3h (117889705). Later records come from the CUHK group of Yibo Lin and Bei Yu: Zhao, Liao, Liu, Jiang, Lin and Yu, IEEE TCAD 44(2) 2025 (arXiv 2403.09070, Tables IV-V, CPU and GPU runs); and Liao, Zhao, Liu and Yu, 'Ultrafast Density Gradient Accumulation in 3D Analytical Placement with Divergence Theorem', ICCAD 2025 (paper Tables I-II, slides of Oct 28 2025). The lowest published score per case across them is case2 15443965 (ICCAD'25, GPU), case2h1 16569703 (TCAD'25, GPU), case2h2 16721757 (ICCAD'25, GPU), case3 97388944 (TCAD'25, CPU), case3h 107621590 (ICCAD'25 Table II, vanilla GPU), case4 1035731150 (ICCAD'25 Table II, vanilla GPU) and case4h 630601092 (ICCAD'25, GPU).

## What counts as a win

A placement output in the contest's output format for one of the seven cases, using the files released on the ICCAD 2023 contest Problems page. The official Problem B evaluator must report it legal (no overlap, macros and cells on legal sites of their die, utilisation limits, terminal size and spacing). Its raw score, HPWL + 10 * #HBTs as reported by the evaluator, must be strictly below the lowest published value listed above for that case. Direction: minimise. It must also be below any later published value found at claim time.

## Partial wins

- **p1:** A legal solution whose evaluator raw score is strictly below the TCAD 2025 Table IV (GPU) value for that case (case2 15635352, case2h2 16820960, case3 98206238, case3h 108166770, case4 1037676163, case4h 635259476), but not below the lowest value listed in the statement for that case.
- **p2:** A legal solution for case4 or case4h whose raw score is strictly below the contest first place (1047716115 or 656528147).

## How a win is checked

Download the case files and the evaluator (Google Drive links on the 2023 Problems page; record sha256). Run the evaluator, then read legality and raw score. An independent script recomputes HPWL per die through the HBTs and counts HBTs (score = HPWL + 10 * HBT), checks macro and cell overlap and terminal spacing, and is calibrated first on a trivial legal placement. Compare with the published tables: TCAD 2025 Tables IV-V and ICCAD 2025 paper Tables I-II. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.cse.cuhk.edu.hk/~byu/papers/C290-ICCAD2025-3DPlaceAcc.pdf>

## Sources

- <https://www.iccad-contest.org/2023/Problems.html>
- <https://arxiv.org/abs/2403.09070>
- <https://bonjuor-zyx.github.io/files/J2-TCAD2025-3DMacroPlace.pdf>
- <https://www.cse.cuhk.edu.hk/~byu/papers/C290-ICCAD2025-3DPlaceAcc.pdf>
- <https://www.cse.cuhk.edu.hk/~byu/papers/C290-ICCAD2025-3DPlaceAcc-slides.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The published runs vary by up to 1% between CPU and GPU runs and between seeds of the same placer, so multi-start plus a careful detailed placement and macro-rotation MILP (as in TCAD 2025, Fig. 10) is a natural first lever.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- case2h1 and case2h2 are two hidden versions of case2, and hidden case2 had a v1 and a v2 file. Name the exact file and hash.
- Use the evaluator's raw score (HPWL + 10*HBT), not the contest's runtime-weighted ranking score.
- Not checked at drafting (paywalled): Phan, Song, Huang, Fang, Chen, Hu and Shen, 'Multi-Die Concurrent Global Placement with Macro Flipping-aware Wirelength Model for 3D-ICs' (ISQED 2026), which reports up to 5% HPWL reduction on these benchmarks, and MOMC3D (Huang, Zhao and Liu, IEEE TCAD 2025, ICCAD 2023 case2). Read their tables before claiming; if either lists a lower raw score, that value is the bar.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/iccad2023-3d-mixed-size-placement-score.md
```

Already set up? Say `run V3R1T4S on iccad2023-3d-mixed-size-placement-score`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `iccad2023-3d-mixed-size-placement-score`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
