# Fundamental limit of jet tagging (GPT-generated top/QCD jets with known likelihood ratio): beat the best tagger's rejection 553 at 50% top efficiency

💥 **Particle physics** · standard · tractability ★★☆☆☆ · compute: needs cluster (Zenodo 14824930 is a 24.4 GB zip, about 154 GB unpacked; the reference taggers train on 10M jets per class on GPUs) · open as of 2026-10-30

## The problem

Geuskens, Gite, Kramer, Mikuni, Muck, Nachman and Reyes-Gonzalez ('The Fundamental Limit of Jet Tagging', arXiv 2411.02628v2) trained autoregressive transformer density models on JetClass top and QCD jets. They then generated 11.2M jets of each class from them (Zenodo 14824930, version 2 of the record, released 6 Feb 2025 with arXiv v2), so the exact likelihood ratio, which is the Neyman-Pearson optimal tagger, is known for every generated jet. At 50% top efficiency, the optimal QCD rejection is 2843 (Fig. 1 legend; the text says about 3300). Taggers trained on 10M generated jets per class fall far short: fine-tuned OmniLearn 553 +- 14, OmniLearn from scratch 543 +- 20, ParT 504 +- 9, ParticleNet 498 +- 8, Deep Sets with attention 450 +- 8, LorentzNet 447 +- 43, PELICAN 409 +- 5, the baseline transformer 319 +- 10 and PFN 116 +- 1 (Fig. 1). The authors report that going from 1M to 10M training jets gains little. The v2 release includes the likelihood-ratio predictions, the baseline-transformer, ParT, PFN and Deep Sets with attention predictions, and OmniLearn classifier weights. Version 1 of the record (Zenodo 14023638, with arXiv v1) holds different samples, on which v1 reported optimum 2941 and ParT 608 +- 28; it is superseded and is not this benchmark. Pang, Faroughy, Shih, Das and Kasieczka (SURF, arXiv 2511.15779) later argued that GPT-type generators add unphysical artefacts that inflate the optimum. That makes this a test of learning a known likelihood ratio from samples, not a statement about real jets. No tagger above 553 on these samples has been published.

## What counts as a win

A tagger trained only on generated jets from Zenodo 14824930 (version 2): at most 10M top and 10M QCD jets, taken from top/raw/train_noseed_nsamples2000000_trunc_5000_nonan_0..4.h5 and qcd/raw/train_noseed_nsamples2000000_trunc_5000_nonan_1..5.h5, or their discretized equivalents in top/discretized/2M_noseed and qcd/discretized/2M_noseed. Files from version 1 of the record (Zenodo 14023638) may not be used. The tagger must not load the released generative transformer models (GenModels), or any file under ClassificationResults (likelihood-ratio predictions, classifier predictions or classifier weights), for training, distillation or scoring. It is evaluated once on the held-out generated test jets top/raw/test_noseed_nsamples200000_trunc_5000_nonan_.h5 and qcd/raw/test_noseed_nsamples200000_trunc_5000_nonan_.h5 (200,000 per class). The discretized files samples_samples_noseed_nsamples200000_trunc_5000_0.h5 may be used instead only once the verifier confirms they hold the same jets. No file of 200,000 samples may be used for training or model selection. The mean QCD rejection at exactly 50% top efficiency (ROC interpolation) over at least 3 seeds must be STRICTLY GREATER (direction: max) than 581. That is 553 + 2 x 14: the fine-tuned OmniLearn value of Fig. 1 of arXiv 2411.02628v2 plus twice its spread, which also absorbs any difference in evaluation sample.

## Partial wins

- **p1:** Under the same rules, mean rejection at 50% top efficiency over 3 seeds strictly greater than 553 (fine-tuned OmniLearn).
- **p2:** Under the same rules, mean rejection strictly greater than 504 (ParT) with a model of at most 200k trainable parameters.
- **p3:** Under the same rules, mean rejection strictly greater than 553 using at most 1M training jets per class.

## How a win is checked

Download Zenodo 14824930 (version 2, ForZenodov2.zip), rerun the released tagger weights on the stated test files, and compute QCD rejection at 50% top efficiency from the ROC curve. Recompute the optimal curve from ClassificationResults/LLRpredictions/predictions_LLR_correct_128.npz and check that it gives about 2843, and that the claimed result is below it (anything above it is a bug). Audit the code to confirm that GenModels, LLRpredictions and the other ClassificationResults files are never opened during training or inference, and that no version-1 file is used. Rerun one seed.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2411.02628>

## Sources

- <https://arxiv.org/abs/2411.02628>
- <https://zenodo.org/records/14824930>
- <https://zenodo.org/records/14023638>
- <https://github.com/hreyes91/fun-jet-tagging>
- <https://arxiv.org/abs/2511.15779>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The generator works on discretised, pT-ordered constituent tokens; a tagger that sees the same tokens in the same order can pick up autoregressive structure that permutation-invariant taggers discard.
- An autoregressive classifier that models p(constituent | previous constituents) for each class reproduces the structure of the likelihood ratio without touching the released models.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Using the released generative models or their likelihoods in any way is computing the optimum, not learning it.
- The optimum (2843) is a hard ceiling; a claim above it signals leakage or an evaluation bug.
- Zenodo 14023638 is version 1, with different samples: ParT already reached 608 +- 28 on it (arXiv v1). Results on version-1 files do not count; use 14824930.
- Physical relevance is disputed (SURF, arXiv 2511.15779): claim a benchmark result, never a statement about real jets.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/particle-physics/jet-tagging-fundamental-limit-gpt-jets-gap.md
```

Already set up? Say `run V3R1T4S on jet-tagging-fundamental-limit-gpt-jets-gap`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `jet-tagging-fundamental-limit-gpt-jets-gap`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
