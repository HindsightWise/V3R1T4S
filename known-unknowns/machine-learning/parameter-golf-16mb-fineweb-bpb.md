# Parameter Golf (finished): a 16 MB language-model artifact trained in 10 min on 8xH100 that beats 1.0565 bits per byte on FineWeb val

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: needs cluster (8x H100 SXM for the 10-minute win and in practice for the unlimited-compute p1; the Mac partial p2 is laptop-days on Apple silicon via train_gpt_mlx.py) · open as of 2026-10-30

## The problem

OpenAI's Model Craft Challenge 'Parameter Golf' (github.com/openai/parameter-golf) ran from 2026-03-18 to 2026-04-30. The task is the best language model whose artifact (train_gpt.py code bytes plus the compressed model) fits in 16,000,000 bytes and trains in under 10 minutes on 8x H100 SXM, with evaluation also under 10 minutes. The score is tokenizer-agnostic bits per byte (val_bpb) on the fixed FineWeb validation split (the first 50k documents). Training on validation data is banned, and test-time training may use only tokens already scored. Records had to beat the previous one by >= 0.005 nats at p < 0.01. The naive baseline scored 1.2244. The final audited leaderboard (last commit 2026-05-04, 'May 1 audited rows', PR #2146 by cocohearts) is topped by codemath3000, 1.0565 (3-seed mean 1.05651, PR #2135, 2026-05-01: token-only n-gram + AsymLogit stack). Next come simonbissonnette 1.0576, andrewbaggio1 1.0586 and alertcat 1.0594, building on work by dexhunter, romeerp, Kevin Clark, bigbag, samacqua, msisovic and many others. The unlimited-compute 16 MB list's best non-record entry is 1.1239 (CiprianFlorin-Ifrim, 1-bit, 2 h), and Will DePue's 4-hour 8xH100 baseline scored 1.2074. The challenge is over and nothing has been added to either leaderboard since the 2026-05-04 audit. Many open PRs claim lower scores, but none was accepted. #2153 (rixhavraj, 2026-05-04) claims 0.9627 from a ~1.13 MB model after a 36-hour optimisation, with no evidence that it used the full validation split or followed the rules. Earlier sub-record claims were withdrawn or failed review: #875's 1.0226 had a broken evaluation, and #2071's 1.0066 had wrong byte accounting. The audit also excluded byte/PPM mixers that failed its full-normalised-distribution check, and CaseOps entries whose locally prepared data put validation documents into training (#2018, #2130). Post-challenge PRs are code fixes, non-record experiments and a 1.06035 record claim (#2163) that does not beat the top row. The dataset, tokenizer and evaluation code remain public.

## What counts as a win

A records-style folder (train_gpt.py, logs, submission.json-style metadata) whose total artifact (code bytes plus compressed model bytes) is <= 16,000,000 bytes, that trains in under 10 minutes and evaluates in under 10 minutes on one 8x H100 SXM node. It must follow the README evaluation rules: no network or training-data access at evaluation, no validation data during training (including through tokenizer or data preparation), and test-time training only on already-scored tokens. Every scored position must use a predictive distribution that is fully normalised over the model's output alphabet, and bytes must be counted from the raw validation text; this is the test the 2026-05-04 audit applied to n-gram and PPM mixers and to CaseOps transforms. Its mean val_bpb over at least 3 seeds must be STRICTLY LESS (direction: min) than 1.05651 (the top row of the frozen leaderboard at https://raw.githubusercontent.com/openai/parameter-golf/main/README.md, re-read before claiming), with a one-sided p < 0.01 that the mean is below 1.05651. Opening a PR is not part of the target.

## Partial wins

- **p1:** Unlimited-compute variant: the same 16,000,000-byte artifact limit and evaluation rules, any training hardware and duration. The mean val_bpb over at least 2 seeds must be strictly below 1.05651 (better than every entry on either leaderboard) and below any open-PR claim (such as #2153's 0.9627) that the skeptic can reproduce under the same rules.
- **p2:** Mac variant: an artifact under 16,000,000 bytes trained from scratch entirely on one Apple-silicon Mac in at most 24 hours (for example via train_gpt_mlx.py), scoring val_bpb strictly below 1.2074 (the 4-hour 8xH100 baseline) on the full validation split.

## How a win is checked

Fetch the cached dataset with data/cached_challenge_fineweb.py and confirm that validation runs on the full fineweb_val split. Run the claimed train_gpt.py on 8x H100 SXM, timing training and evaluation separately, and measure the artifact size (code bytes plus compressed model) against the 16,000,000-byte cap. Read the code for any validation access during training and for TTT that scores tokens after adapting on them. If the tokenizer changed, recompute bytes from the raw validation text independently. Repeat with the claimed seeds and run the one-sided test against 1.05651.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/openai/parameter-golf/main/README.md>

## Sources

- <https://github.com/openai/parameter-golf>
- <https://raw.githubusercontent.com/openai/parameter-golf/main/README.md>
- <https://github.com/openai/parameter-golf/pull/2135>
- <https://github.com/openai/parameter-golf/pull/2146>
- <https://github.com/openai/parameter-golf/pull/2153>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Score-first TTT legality: adapting on validation tokens before scoring them is cheating; the leaderboard entries use only already-scored tokens.
- Byte accounting under custom tokenizers (such as the CaseOps transforms) was a source of disputes; recompute bytes from raw text.
- The audit (PR #2146) rejected byte/PPM mixers whose mixed distribution was not fully normalised. It also rejected CaseOps runs whose local data preparation overlapped the validation documents (the 'train_shards: 1499' fingerprint discussed there). Build data from the canonical sources and check normalisation explicitly.
- Open PRs with scores far below 1.0565 have so far turned out to be evaluation bugs; do not treat an unreviewed PR claim as the bar or as a working recipe.
- Record reproduction depends on a fixed Brotli decoder (open PR #2171 pins it); an unpinned brotli build can fail to decode artifacts.
- 16,000,000 bytes is decimal, not 16 MiB.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/parameter-golf-16mb-fineweb-bpb.md
```

Already set up? Say `run V3R1T4S on parameter-golf-16mb-fineweb-bpb`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `parameter-golf-16mb-fineweb-bpb`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
