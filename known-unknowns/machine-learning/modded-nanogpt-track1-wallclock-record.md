# Modded-NanoGPT speedrun: train to 3.28 FineWeb val loss on 8xH100 faster than the 39.9 s README record (and the pending claims)

🤖 **Machine learning** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (8x H100 node; each attempt costs minutes but needs several runs for p < 0.01) · open as of 2026-10-30

## The problem

The NanoGPT speedrun (github.com/KellerJordan/modded-nanogpt) asks for the least wall-clock time on 8x NVIDIA H100 to train a language model reaching mean validation cross-entropy <= 3.28 on the first 10,485,760 FineWeb validation tokens. The train and val token streams are fixed, the time is training only, and records need p < 0.01 that the mean is <= 3.28 and must be faster than the prior record on the same hardware. Karpathy's llm.c GPT-2-small baseline took 45 minutes; Keller Jordan and a large community (YouJiacheng, ClassicLarry, jvarho, snimu and many others) cut it to README record #92: 0.665 min (39.9 s), 08/30/26, by @DevenPzak (PR #360, merged 2026-09-28). Track 2 (GPT-2 Medium, target 2.92) has README record #18: 17.35 min (12/31/25). Live check 2026-10-30: open, unmerged track-1 PRs claim much less. #367 (hermabr) 6.702 s and #380 (devenpzak) 9.65 s use CPU-built n-gram or retrieval tables held in host RAM, as does #366; #393 31.29 s (MoE on #379 + #375 + #371) and #391 34.856 s stay on the GPUs. Commenters on #367 and #380 note that the rules say nothing about CPU or host-RAM use, and no rule change has been made. A comment on #380 (ldmberman) reports 2.87 track-2 loss in 221 s with an adapted host-table recipe; the lowest open track-2 PR is #261, 14.34 min.

## What counts as a win

A training script and logs, run on one 8x H100 SXM node under the README rules re-read live (train and val pipelines unchanged, no extra torch._inductor or torch.compile flags, p < 0.01 over all runs launched that mean val loss <= 3.28). The training time must be STRICTLY LESS (direction: min) than the live README track-1 record (39.9 s on 2026-10-30), with the incumbent re-timed on the same node, AND strictly less than the smallest time claimed in any open track-1 PR at claim time (6.702 s, #367, on 2026-10-30). Submitting a PR is not part of the target.

## Partial wins

- **p1:** A rule-compliant track-1 run set (p < 0.01, mean <= 3.28) that keeps all learned state and lookup tables on the GPUs (no host-RAM or CPU-built n-gram or retrieval tables). It must be strictly faster than the live README record and than every open track-1 PR claim without such tables (31.29 s, #393, on 2026-10-30), both re-timed on the same node.
- **p2:** Track 2 (GPT-2 Medium): a rule-compliant run set with no host-RAM or CPU-built tables, reaching mean val loss <= 2.92 at p < 0.01. Its training time must be strictly below both the live README track-2 record (17.35 min) and the lowest open track-2 PR claim (14.34 min, #261, on 2026-10-30), with #261 re-timed on the same node.

## How a win is checked

Rent an 8x H100 SXM node, run the claimed script and the current README record script back to back, and repeat the claim enough times to recompute the p-value from all logs. Confirm that the data loaders read the canonical FineWeb shards unchanged and that the val loss is computed over the standard 10,485,760 tokens with a valid probability model. Re-fetch the README and the open PR list.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/KellerJordan/modded-nanogpt/master/README.md>

## Sources

- <https://github.com/KellerJordan/modded-nanogpt>
- <https://raw.githubusercontent.com/KellerJordan/modded-nanogpt/master/README.md>
- <https://github.com/KellerJordan/modded-nanogpt/pull/360>
- <https://github.com/KellerJordan/modded-nanogpt/pull/367>
- <https://github.com/KellerJordan/modded-nanogpt/pull/380>
- <https://github.com/KellerJordan/modded-nanogpt/pull/393>
- <https://github.com/KellerJordan/modded-nanogpt/pull/261>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The frontier is in flux: the README record and the pending PR claims differ by about 6x, and the rules on host-RAM n-gram or retrieval tables may change; re-read both before attacking.
- Timing differs between cloud H100 hosts; the incumbent must be re-timed on the same node.
- Systems-only speedups are exempt from the p-value rule only if the ML is unchanged.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/modded-nanogpt-track1-wallclock-record.md
```

Already set up? Say `run V3R1T4S on modded-nanogpt-track1-wallclock-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `modded-nanogpt-track1-wallclock-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
