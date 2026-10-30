# Noise: pretraining a fixed 37.7M transformer without backpropagation, below 3.338 val loss on 30M FineWeb tokens

🤖 **Machine learning** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster (8x H100 node; current records take 23 s to 3 h of training, and a Mac run would take days) · open as of 2026-10-30

## The problem

Noise (github.com/qlabs-eng/noise, Q Labs, created 2026-10-12) is a speedrun for learning algorithms that never run a backward pass. The model is the fixed 37.7M-parameter transformer of Q Labs' Dust paper. Data: data/train.pt, 30M FineWeb sample-10BT tokens with the fixed BPE-4096 tokenizer, at most one epoch. Score: utils/eval.py mean next-token cross-entropy over the 1,114,112 predictions of Dust's data/val.pt, with both files pinned by hash. Rules: no autograd (reverse or forward mode) and no hand-written backward pass; every error signal comes from forward evaluation and may take at most one step through a nonlinear part, with no chained credit; seed 0; no checkpoint selection on val. The 10M-token tracks were archived on 2026-10-22. Live 30M records on 2026-10-30: Track 1 (val loss, no time limit) 3.338 by @CharlesDDDD (forward readout of cross-token credit, 56 min), after 3.409 by JaydenTeoh, spicylemonade, hoo0681, Lazarus-931, CharlesDDDD and NotDesigned, and the Dust-with-Adam baseline at 3.767. Track 2 (time to 3.5 on 8xH100) 22.9 s at 3.498 by @RobertTLange (PR #52, merged 2026-10-28), after 2 min 3 s by @conglu1997. Track 3 (open architecture) 3.211 by @RobertTLange (12x1024 GPT with hashed n-gram value embeddings). Backprop on the same model, data and epoch scores 3.419 with Adam and 3.340 with ANVIL II plus Adam, so the Track-1 record is now level with the best backprop baseline; the README's stated goal is to beat backprop by a large margin.

## What counts as a win

A training script that obeys the README rules re-read live (fixed model loading into utils/model.py with a strict state-dict match, only data/train.pt for at most one epoch, no autograd or hand-written backward pass, no chained credit, seed 0). The final weights, scored by utils/eval.py on the pinned data/val.pt, must give a validation loss STRICTLY LESS (direction: min) than the live Track-1 record (3.338 on 2026-10-30) and than any lower Track-1 claim in an open PR, re-checked before claiming.

## Partial wins

- **p1:** Track 2: reach val loss <= 3.5 under the same rules with training time on one 8x H100 node strictly below the live Track-2 record (22.9 s on 2026-10-30), timed as the README specifies (first update to last, excluding validation), with the incumbent re-timed on the same node.
- **p2:** Track 3: with the architecture in train/arch/model.py changed (interface kept), val loss strictly below the live Track-3 record (3.211 on 2026-10-30).

## How a win is checked

Run utils/prepare_data.py and confirm the pinned hashes. Grep and read the training code: no torch.autograd, .backward(), torch.func.grad/jvp/vjp or custom autograd Functions, and no tensor with requires_grad=True during training (or training under torch.no_grad or inference_mode). Check by hand that no error signal is propagated through more than one nonlinearity. Re-run with seed 0 and rescore the saved final.pt with uv run utils/eval.py. Confirm that the strict state-dict load into utils/model.py succeeds for tracks 1 and 2.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/qlabs-eng/noise/main/README.md>

## Sources

- <https://github.com/qlabs-eng/noise>
- <https://raw.githubusercontent.com/qlabs-eng/noise/main/README.md>
- <https://github.com/qlabs-eng/dust>
- <https://qlabs.sh/research/dust>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The no-backprop rule is judged by its spirit (methods must still apply to non-differentiable networks); a hidden local-derivative chain is disqualifying even if no autograd call appears.
- The benchmark is two weeks old and records move daily (track 2 went from 8 min 20 s to 22.9 s in a week); always re-fetch.
- The archived 10M-token records are not comparable to the 30M-token tracks.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/noise-backprop-free-pretraining-records.md
```

Already set up? Say `run V3R1T4S on noise-backprop-free-pretraining-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `noise-backprop-free-pretraining-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
