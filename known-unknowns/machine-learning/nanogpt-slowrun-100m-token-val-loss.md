# NanoGPT Slowrun: lowest FineWeb val loss from a fixed 100M-token training set (1-hour track 3.183, unlimited 2.987)

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (8x H100 node; tiny track 15 min, main track 1 h, two-hour track 2 h, unlimited track used 80 h on 5 nodes) · open as of 2026-10-30

## The problem

NanoGPT Slowrun (github.com/qlabs-eng/slowrun, Q Labs: Akshay Vegesna, Samip Dahal, Chinmay Karkar, Bishwas Mandal, Shmuel Berman, Zhiwei Xu) is the fixed-data, high-compute counterpart of the speedrun. Training uses exactly 100M GPT-2-tokenised FineWeb tokens (prepare_data.py; fineweb_train.pt sha256 36e7c95c...), and the score is cross-entropy on a fixed 10M-token validation set (fineweb_val.pt sha256 6868ed37...), lower is better. Tracks: limited (one 8xH100 node, <= 1 h), tiny (<= 15 min), two hour (<= 2 h) and unlimited compute. README records, checked live 2026-10-30: limited #21 3.183 (09/05/26, @xingyudang, first-order meta-gradient on MLP matrices), down from the 3.402 baseline of a 2.7B Muon transformer with dropout 0.1 and weight decay 1.6. Tiny #15 3.295 (09/05/26, @xingyudang). Two-hour #6 3.139 (07/02/26, @AjAnubolu). Unlimited #12 2.987 (05/28/26, @not-nonymous; snapshot ensembles plus gradient-based model selection, 80 h on 5 nodes). Contributors include @ms337, @shmublu, @ChinmayK0607, @clarkkev, @samacqua and @L-z-Chen. Open PRs: #102 (2026-10-29) claims tiny 3.284 in 14.2 min; #67 (samacqua) reaches tiny 3.273 only with strided scoring and per-document test-time training at evaluation, outside the standard scoring; #63 (NCA pre-pretraining, 3.207) is older than the current limited record.

## What counts as a win

A training script, run within the limited track's cap (one 8x H100 node, at most 60 minutes of training) on the hash-verified 100M-token fineweb_train.pt only, whose validation loss on the hash-verified fineweb_val.pt, computed by the repository's evaluation code, is STRICTLY LESS (direction: min) than the live README limited-track record (3.183 on 2026-10-30) and than any lower limited-track claim in an open PR, re-checked before claiming. The skeptic's re-run must also come in below the record. The validation set must never be used for training or model selection.

## Partial wins

- **p1:** Tiny track: within 15 minutes of training on one 8x H100 node, val loss from the track's standard evaluation strictly below both the live README tiny record (3.295) and the lowest open tiny-track PR claim under standard evaluation (3.284, #102, on 2026-10-30).
- **p2:** Two-hour track: within 2 hours on one 8x H100 node, val loss from the standard evaluation strictly below the live README two-hour record (3.139 on 2026-10-30).
- **p3:** Unlimited track: any compute within the README's practical cap (64 H100s for 7 days), the same 100M training tokens and val set, and the standard evaluation, with val loss strictly below the live README unlimited record (2.987 on 2026-10-30).

## How a win is checked

Run prepare_data.py and confirm both sha256 hashes. Read the claimed train.py to confirm that only fineweb_train.pt feeds training and that val.pt is touched only for the final score (no checkpoint or ensemble-member selection on val; gradient-based selection must use train-derived signals). Re-run on an 8x H100 node with wall-clock logging and compare the final val loss to the README value of the track.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/qlabs-eng/slowrun/main/README.md>

## Sources

- <https://github.com/qlabs-eng/slowrun>
- <https://raw.githubusercontent.com/qlabs-eng/slowrun/main/README.md>
- <https://raw.githubusercontent.com/qlabs-eng/slowrun/main/prepare_data.py>
- <https://github.com/qlabs-eng/slowrun/pulls>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Selecting checkpoints or ensemble members by validation loss is leakage; the unlimited record's gradient-based model selection must be checked for this before copying it.
- The data cap is 100M tokens: extra FineWeb tokens, distillation from a model trained on other data, or pretrained weights are excluded.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/nanogpt-slowrun-100m-token-val-loss.md
```

Already set up? Say `run V3R1T4S on nanogpt-slowrun-100m-token-val-loss`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nanogpt-slowrun-100m-token-val-loss`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
