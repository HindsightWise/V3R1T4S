# Google Willow surface-code memory (public data): decode the distance-7 experiment to a logical error per cycle below the neural decoder's 1.43e-3

⚛️ **Physics** · standard · tractability ★☆☆☆☆ · compute: laptop-days (50,000 shots per duration and basis at d = 7; neural decoders need a GPU) · open as of 2026-10-30

## The problem

Google Quantum AI and collaborators (Rajeev Acharya et al., 'Quantum error correction below the surface code threshold', Nature 638, 920 (2025), arXiv:2408.13687) ran distance-3, 5 and 7 surface-code memories on the 105-qubit Willow processor. They published the data on Zenodo (record 13273331, CC BY 4.0, file google_105Q_surface_code_d3_d5_d7.zip). For the distance-7 patch (d7_at_q6_7), each basis holds 50,000 shots at each of 13 memory durations, r10, r30, ..., r250 cycles. It also holds a one-cycle run (r01) and a 13-cycle calibration run (r13). With a fine-tuned neural network decoder of the AlphaQubit line (Johannes Bausch, Andrew W. Senior et al., Nature 2024, arXiv:2310.05900) they report a distance-7 logical error per cycle eps_7 = (1.43 +- 0.03) x 10^-3 and Lambda = 2.14 +- 0.02. Ensembled matching synthesis (Libra, with a reinforcement-learning-optimised prior; its predictions ship in the release) gives eps_7 = (1.71 +- 0.03) x 10^-3 and Lambda = 2.04 +- 0.02 (Table S1). eps_d is fitted separately for each basis by a weighted line through ln(1 - 2 p_L) over the 13 durations up to 250 cycles, and averaged over X and Z. For the distance-7 data the neural decoder was cross-validated on an even/odd shot split. AlphaQubit 2 (Andrew W. Senior, Thomas Edlich, Francisco J. H. Heras, Lei M. Zhang, Oscar Higgott et al., arXiv:2512.07737, v2 11 Mar 2026) is reported comparable to the first AlphaQubit and better than Libra on this dataset, with values shown only in its Fig. 3c. A sim-to-real benchmark by Shay J. Manor, Leila S. Erhili and Yassine Jebbouri (arXiv:2609.04557, Sep 2026) ranks Tesseract first in its six-decoder panel on the real data, at 1.67 x 10^-3 per cycle at d = 7. That figure is a mean per-cycle rate over a 2-30-round window, not the fitted eps above.

## What counts as a win

Success means a decoder and its outputs on the 105-qubit distance-7 memory data of Zenodo record 13273331 (patch d7_at_q6_7) such that the following gives eps_7 STRICTLY BELOW 1.40 x 10^-3 (direction: min; the published 1.43e-3 minus its quoted 0.03e-3 uncertainty). Decode every shot of the 13 scored durations r10, r30, ..., r250 in both bases. The r01 and r13 runs are not scored, and r13 (the 13-cycle calibration run) may be used to fit priors. For each basis separately, fit ln F(n) = ln F_0 + n ln(1 - 2 eps) to F(n) = 1 - 2E(n) over the 13 durations by weighted least squares, with weights 1/s_n^2 where s_n = 2 sqrt(E(n)(1 - E(n))/N_n) / (1 - 2E(n)). Average the X and Z values. Before its own number counts, the same script must reproduce eps_7 = 1.71 x 10^-3 (to within 0.01e-3) from the release's libra_decoder_with_rl_optimized_prior predictions. An unweighted fit gives about 1.65e-3 there and is not allowed. No decoder parameter (weights, priors, edge weights, ensemble or model choices) may be fitted on any shot it is scored on. Either nothing is fitted on the scored shots, or the even/odd protocol is used: fit on even-indexed shots and score odd-indexed ones, then the reverse, so every scored shot is scored once. The result must also beat any later d = 7 value on this dataset found by an arXiv search immediately before claiming. AlphaQubit 2 gives its d = 7 value only graphically (Fig. 3c of arXiv:2512.07737). A claim must lie below the lower end of that point's plotted 95% interval. If this cannot be read unambiguously, the claim is PROMISING, not CONFIRMED, until the value is known numerically.

## Partial wins

- **p1:** No parameter may be fitted on any scored shot; priors come only from the r13 calibration run, the release's own detector-error-model files, simulation, or none. Under these conditions, eps_7 under the same weighted fit must be strictly below 1.71 x 10^-3. That is the value of Libra with the RL-optimised prior (Acharya et al. Table S1), whose predictions ship in decoding_results/libra_decoder_with_rl_optimized_prior. Tesseract must also be re-run by the claimant with the same prior under the identical fit as a control, and beaten.

## How a win is checked

Download the Zenodo archive (data only; no code from it needs to run). Rerun the claimant's decoder on every scored distance-7 shot (bases X and Z, durations r10 to r250) with the stated fold assignment. Recompute E(n) per duration and basis against obs_flips_actual.b8. Refit eps per basis with the weighted least-squares fit of the criterion and average X and Z. As a calibration, the same script applied to the release's libra_decoder_with_rl_optimized_prior predictions must give 1.71e-3 (a check run for this review gave 1.711e-3 weighted and 1.652e-3 unweighted). Confirm from the training scripts and data hashes that no fitting step reads a shot of the fold it is scored on, and that r01 and r13 are not scored.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2512.07737>

## Sources

- <https://arxiv.org/abs/2408.13687>
- <https://doi.org/10.5281/zenodo.13273331>
- <https://arxiv.org/abs/2310.05900>
- <https://arxiv.org/abs/2512.07737>
- <https://arxiv.org/abs/2609.04557>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Tesseract (A* search) is the strongest non-neural decoder on this data. Combine it with a detector error model re-fitted on the even fold (correlations and leakage-induced hyperedges) and score on the odd fold.
- Ensemble heterogeneous decoders (correlated matching variants, Tesseract, BP-based) through calibrated soft outputs; Acharya et al. already ensemble five neural models.
- The data contains rare correlated bursts. A decoder conditioned on recent detection density within a shot may help, but must respect the fold rule.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Using the observable flips of the scored fold for anything (training, early stopping, prior fitting, model selection) voids the claim.
- The fit is inverse-variance weighted. An unweighted fit lowers eps_7 by about 3.5% on the same predictions, which is more than the margin to the record.
- eps from a single duration via (1 - (1-2E)^(1/n))/2 is not the fitted eps; use the fit over the 13 scored durations.
- Each basis directory also holds r01 and r13 runs; r13 is the calibration data behind the released priors. Do not score them.
- The 72-qubit processor datasets (surface-code sets 1 and 2 and the repetition code) in the same Zenodo record are different experiments with different published values.
- Manor et al.'s 1.67e-3 for Tesseract is a mean per-cycle rate over a 2-30-round window, not the fitted eps; do not compare it with fitted values.
- With the quoted +-0.03e-3 uncertainty, a result of 1.42e-3 is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/willow-surface-code-d7-decoding.md
```

Already set up? Say `run V3R1T4S on willow-surface-code-d7-decoding`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `willow-surface-code-d7-decoding`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
