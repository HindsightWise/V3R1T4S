# ISPD 2026 contest (post-placement buffering and sizing): a result that dominates the per-design winner on every non-runtime metric

🛠️ **Engineering and chips** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days per design (OpenROAD global route and OpenSTA on 0.1M to 1M-instance ASAP7 designs; evaluation flows of 10 to 1,700 s) · open as of 2026-10-30

## The problem

The ISPD 2026 contest, 'Post-Placement Buffering and Sizing', was organised by Andrew B. Kahng, Sayak Kundu, Yiting Liu and Davit Markarian (UCSD), Zhiang Wang (Fudan) and Seokhyeong Kang and Seonghyeon Park (POSTECH). Starting from a placed, debuffered ASAP7 netlist, a tool may only insert buffers and inverters and resize cells (drive strength and VT). Results must pass a legality check and a logic equivalence check before an open OpenROAD global-routing and OpenSTA flow reports TNS, dynamic and leakage power, cap/slew/fanout violation sums, GR overflow and average displacement. The final leaderboard (results announced 2026-03-18) gives full rows for the top three teams. Per-design top rows with published numbers are: ariane, Team29: TNS -18254.21 ns, dynamic 140.20 mW, leakage 4.80, slew over 46.91, disp 0.02; bsg_chip, Team33: TNS -44875.21, 747.20 mW, cap over 98.01, slew over 40659.66; jpeg_encoder, Team33: TNS -488.89, 93.60 mW, no violations; ariane_h2 (hidden), Team33: TNS -3271.86, 157.14 mW, slew over 993.40. Each contest score mixes in tool runtime, so this target counts quality only. The winners were IRISLab (NTU and NTUST: Huang, Fang Chiang, Kuo, Liang, Jiang), PTSD (NTHU: Pai, Tsai, Chen, Huang, Xu, Wang) and HLFC (NTHU: Fu, Chiu, Hung, Lin, Wang).

## What counts as a win

An output .v netlist and .def for one of ariane, ariane_v2, bsg_chip, bsg_chip_v2, jpeg_encoder, jpeg_encoder_v2 or ariane_h2, from the public or hidden benchmarks on the contest page. The official evaluation flow in ABKGroup/ISPD26-Contest must report it legal and logically equivalent: scripts/evaluation.tcl as called by the base design's eval.sh (scripts/ariane, scripts/bsg_chip or scripts/jpeg_encoder; for the _v2 and _h2 designs, the same script pointed at that variant's benchmark files), run in the provided Docker image, plus the equiv_check flow. On every one of TNS, dynamic power, leakage power, Cap/Slew/Fanout Over Sum, Max and Total GR overflow, and Avg Disp, it must be no worse than the README's final-leaderboard row of the per-design top team. That team is named in 'Leaderboard per design' and must have a published row: Team29 for ariane, Team33 for the others. TNS must be strictly better (less negative). Runtime is excluded. The README is re-fetched at claim time.

## Partial wins

- **p1:** A legal, equivalent result that dominates the 2nd-place (Team31) published row on all non-runtime metrics listed above for one of these designs, with strictly better TNS.
- **p2:** A legal, equivalent result on ariane_h1, bsg_chip_h1 or bsg_chip_h2 that dominates all three published final rows (Teams 33, 31 and 29) on every non-runtime metric with strictly better TNS than the best of them. Team6, the unpublished per-design leader there, may still be better, so this is a partial win only.

## How a win is checked

Clone ABKGroup/ISPD26-Contest (ASAP7 platform, eval scripts, equivalence scripts, Dockerfile). Download the benchmarks from the contest page and record hashes. Run the design's eval.sh in the provided Docker image (or with a locally built OpenROAD of the pinned version) on the claimed .v/.def. Confirm that the legality and equivalence steps pass, then read the reported metrics. Calibrate by running the pre_opt contest.def and the OpenROAD RSZ baseline script, and check that they match the README's pre_opt and RSZ rows. Compare metric by metric with the live README rows. An hour or more per large design.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/ABKGroup/ISPD26-Contest/main/README.md>

## Sources

- <https://github.com/ABKGroup/ISPD26-Contest>
- <https://raw.githubusercontent.com/ABKGroup/ISPD26-Contest/main/README.md>
- <https://www.ispd.cc/contests/26/index.html>
- <https://www.ispd.cc/contests/26/ISPD26_contest_description.pdf>
- <https://vlsicad.ucsd.edu/ISPD26-Contest/ispd26.html>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A contest 'Design Score' includes tool and flow runtime and so depends on hardware. This target is quality-only dominance; never claim a higher contest score.
- Only buffer and inverter insertion and sizing (drive strength and VT) are allowed. Any other netlist change fails equivalence; moving macros or I/Os, changing the floorplan or PDN, or placing logic gates in soft blockages fails legality.
- The README was last changed on 2026-05-03 and the organisers say next year's evaluation will be stricter. Use the live table and re-fetch it at claim time.
- The per-design 'Top Team' is chosen by the runtime-weighted Design Score, so other published rows can be better on single metrics (Team33's ariane TNS -6377.76 beats Team29's); the criterion is dominance of the named row only.
- The repo's eval.sh scripts hard-code DESIGN_NAME for the four base designs only; for a _v2 or hidden design, record exactly how the base script was pointed at the variant's files so the skeptic can rerun it.
- The ISPD 2027 contest (ABKGroup/ISPD27-Contest, MCMM post-CTS buffering and sizing, prizes, final deadline 2027-03-20) is a different, live setter challenge. A result here is not an ISPD 2027 entry, and agents never register or submit to it; that is a human decision.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/ispd2026-buffering-sizing-dominance.md
```

Already set up? Say `run V3R1T4S on ispd2026-buffering-sizing-dominance`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ispd2026-buffering-sizing-dominance`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
