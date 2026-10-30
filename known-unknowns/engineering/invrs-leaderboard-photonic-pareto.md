# invrs-gym photonic inverse design: a manufacturable design beating the frozen invrs leaderboard's efficiency-vs-length-scale front

🛠️ **Engineering and chips** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (JAX; FMMAX RCWA or ceviche FDFD per evaluation; a GPU helps for metalens and Bayer sorter) · open as of 2026-10-30

## The problem

invrs-gym (Martin F. Schubert, invrs.io; arXiv 2410.24132) packages photonic inverse design problems behind one JAX interface, using FMMAX (RCWA) and ceviche (FDFD) for the physics and imageruler (NanoComp) to measure the minimum width and spacing of a design. The companion invrs leaderboard (github.com/invrs-io/leaderboard) lists every evaluated solution with eval_metric (higher is better), minimum_width, minimum_spacing and binarization_degree. All invrs-io repositories were archived in late October 2025 (last leaderboard push 2025-10-23), so the table is frozen at commit ed27c5c (PR #85, 2025-10-22). That PR removed the 2025 entries of riarrieta (Arrieta, Romano and Johnson, arXiv 2507.16108) and smartalecH (Alec Hammond, subpixel-smoothed projection); they stay public in git history and count as records here. They were the last additions; none moved the seven main fronts, and nothing was added after the archive. Fronts of metric against L = min(width, spacing) in pixels, recomputed 2026-10-30 (selected points): - metagrating: 0.99603 at L=5, 0.98224 at 7, 0.96441 at 9, 0.96017 at 11, 0.93853 at 15. - metalens: 19.955 at 3, 18.801 at 5, 15.246 at 7, 14.593 at 11, 7.867 at 12. - bayer_sorter: 0.55110 at 8, 0.51050 at 10, 0.49273 at 12. - diffractive_splitter: 0.59640 at 10, 0.53885 at 17. - meta_atom_library: 0.95139 at 10, 0.86868 at 24. - photon_extractor: 13.9314 at 10, 12.0894 at 16. - ceviche_mode_converter: 0.90951 at 6, 0.76166 at 10, 0.61101 at 14, 0.17374 at 16. Credits: Ian Williamson, Ardavan Oskooi, Mo Chen, Rasmus Christiansen, Jiaqi Jiang, You Zhou and the photonics-opt-testbed authors (Chen et al., JOSA B 2024), Martin Schubert, Aaditya Chandrasekhar and Rahul Padhy, Rodrigo Arrieta, Giuseppe Romano, Steven G. Johnson and Alec Hammond.

## What counts as a win

A design for one of bayer_sorter, ceviche_mode_converter, diffractive_splitter, meta_atom_library, metagrating, metalens or photon_extractor, evaluated with invrs-gym 1.6.2, imageruler 0.3.0 (the leaderboard does not pin it), jax_enable_x64, and the leaderboard's own evaluation path (scripts/eval.py at commit ed27c5c: default challenge, eval_metric, imageruler minimum width and spacing). The design must have binarization_degree exactly 1.0. Let L = min(minimum_width, minimum_spacing); L must not exceed the largest L among that challenge's record entries. The record set is the challenge's leaderboard.txt at ed27c5c plus the lines removed in PR #85. Every record entry whose stored OR re-evaluated length scale is at least L is a competitor. The design's eval_metric must be STRICTLY GREATER (direction: max) than both the stored and the re-evaluated (same environment) eval_metric of every competitor, by at least 1e-4 x max(1, |that value|). It must also beat any design published after the freeze for the same invrs-gym challenge with length scale at least L, found by a literature search re-run just before claiming (papers or repositories reporting the gym's eval_metric, or releasing a design that can be re-evaluated).

## Partial wins

- **p1:** The same rules on ceviche_beam_splitter, ceviche_wdm, ceviche_power_splitter or ceviche_waveguide_bend, whose record sets hold 1-3 entries (fronts: beam splitter -0.45719 at L=11, which also dominates L<=11; wdm 0.05395 at L=4 and 0.04377 at L=11; power splitter 0.009037 at L=8; waveguide bend -1.25043 at L=7): a binarized design that beats every competitor with length scale at least its own.
- **p2:** A script a skeptic reruns that re-evaluates every record entry of one main challenge under invrs-gym 1.6.2 and imageruler 0.3.0 and prints, for each entry, the re-evaluated eval_metric, width and spacing beside the stored values. It counts when the skeptic's rerun matches the script's printed values to 1e-9 relative, and either every entry reproduces (eval_metric within the leaderboard's own RTOL 1e-5, width and spacing exactly) or each mismatch is listed with both numbers.
- **p3:** A binarized design whose length scale is at least 2 pixels larger than the largest record L of a main challenge, with eval_metric strictly above the best record value at that largest L (extends the front to a more manufacturable regime).

## How a win is checked

pip install invrs-gym==1.6.2 imageruler==0.3.0 and the leaderboard package from the archived repo at ed27c5c. Load the claimed .json (totypes json_utils) or .csv density, then run the leaderboard's eval path in float64: challenge.eval_metric plus the imageruler width and spacing. Re-evaluate every competitor record entry (stored or re-evaluated L at least the claim's L, including the PR #85 lines restored from git history) in the same run. Compare using the criterion's tolerance. Minutes to an hour per design on a laptop CPU.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/invrs-io/leaderboard/tree/main/challenges>

## Sources

- <https://github.com/invrs-io/leaderboard>
- <https://github.com/invrs-io/leaderboard/tree/main/challenges>
- <https://github.com/invrs-io/leaderboard/pull/85>
- <https://github.com/invrs-io/gym>
- <https://arxiv.org/abs/2410.24132>
- <https://pypi.org/project/invrs-gym/>
- <https://github.com/NanoComp/photonics-opt-testbed>
- <https://github.com/NanoComp/imageruler>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Density topology optimisation with the subpixel-smoothed projection, or hyperparameter-free length-scale constraints (the two removed 2025 methods), aimed at L values where the front drops steeply (metalens L=11-12, mode converter L=14-16).
- Level-set or shape-library parameterisations (PhoTOS) that enforce a minimum feature size by construction, followed by a final binarized polish.
- Start from the best record design at a smaller L and apply morphological opening and closing to reach the target L. Then re-optimise with the length-scale constraint active.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The leaderboard repository is archived: no pull request can be accepted, and opening one is not part of a win.
- eval_metric definitions differ by challenge. Several are min-over-wavelengths or synthetic scores, not average efficiency, so a higher average efficiency is not a win.
- Version drift: stored numbers come from older invrs-gym and imageruler versions, and imageruler is not pinned by the leaderboard. Evaluate both the record entries and the claim under the same pinned versions, and beat both the stored and the re-evaluated values.
- Designs that are not fully binary, or that only meet the length scale after thresholding outside the evaluator, are not wins.
- Entries removed in PR #85 are part of the record set, even though they no longer appear at HEAD; on ceviche_beam_splitter and ceviche_wdm they are the only entries.
- Large-L points on some fronts are weak (mode converter: 0.17374 at L=16, negative beyond); check that a claimed L is within the largest record L, otherwise only p3 applies.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/invrs-leaderboard-photonic-pareto.md
```

Already set up? Say `run V3R1T4S on invrs-leaderboard-photonic-pareto`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `invrs-leaderboard-photonic-pareto`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
