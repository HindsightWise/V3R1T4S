# Modded-NanoGPT track 3 (optimization): reach 3.28 FineWeb val loss with the fixed GPT-2-small setup in fewer than 2,690 steps (2,450 pending)

🤖 **Machine learning** · standard · tractability ★★☆☆☆ · compute: needs cluster (one A100/H100 suffices because only steps count, but each run is about 1.4B tokens through a 124M model and n >= 6 runs are needed) · open as of 2026-10-30

## The problem

Keller Jordan's modded-nanogpt added a third track in April 2026, the optimization benchmark (records/track_3_optimization). Architecture, data (FineWeb10B in the fixed order), batch size (524,288 tokens per step) and one forward-backward pass per step are frozen; the optimizer, its hyperparameters, schedules and initialization are free. The score is the number of steps needed to reach FineWeb validation loss 3.28, with no wall-clock limit (the quickstart runs on any {1,2,4,8}x A100/H100). A result must satisfy (3.28 - mean val loss) * sqrt(n) >= 0.004 over n non-cherry-picked runs (one-sided z-test, sigma 0.0013, p < .001), with no per-run early stopping on validation. Keller Jordan's first Muon-with-aux-Adam run took 3,600 steps (n=1) and Adam 5,625 (2026-04-26). Records fell through Kaiyue Wen, nilin, eliebak, OscarYau525, jn2clark and others to the current README record #46: 2,690 steps, val 3.2783 (n=8), 2026-06-19, by @ypwang61 (SOAP-Muon stack, tail-EMA readout, row-wise update floor, cautious weight decay; PR #328). Live check 2026-10-30: the README still lists #46. Open, unmerged PRs claim fewer steps: #395 2,450 pooled (n=39, 2026-10-28, newstzpz; SOAP-Shampoo + spectral annealing + head eigen-Adam; the PR says seed choice and stopping in its automated search were partly data-dependent, and its one pre-planned 8-seed batch passes only at 2,455), #384 2,540 (n=14), #377 2,580, #341 2,600 (n=12), #388 2,615 (n=16) and #339 2,635. The best AdamW-only result is 4,950 steps (PR #353, konstmish, n=10, open).

## What counts as a win

A training script that differs from records/track_3_optimization/train_gpt_simple.py only in what the README allows (optimizer, hyperparameters, schedules, initialization). The architecture, data stream, 524,288-token batch and single forward-backward per step stay unchanged, and no third-party optimizer is imported. Its fixed final step S, the same in every trial and fixed in code, must satisfy the README significance rule (3.28 - mean val loss) * sqrt(n) >= 0.004 over all n runs launched, with n >= 6 and every log kept. S must be STRICTLY LESS (direction: min) than the live track-3 README record (2,690 on 2026-10-30) and than the smallest step count claimed in any open or closed track-3 PR (2,450 in #395 on 2026-10-30), both re-checked live before claiming.

## Partial wins

- **p1:** Pre-registered confirmation: a run set whose seed list and fixed stop step S were committed before any run launched, every launched run counted, meeting the significance rule at an S strictly below 2,455. That is the lowest step count passed by a pre-planned run set in any track-3 PR on 2026-10-30 (#395's 8-seed batch).
- **p2:** AdamW per-optimizer record: AdamW (or Adam) as the only optimizer on all parameters, with no orthogonalization or Newton-Schulz step, no Shampoo/SOAP/K-FAC or other matrix preconditioning and no hyperball projection (schedules, initialization, per-group hyperparameters and weight decay free). It must meet the significance rule at a fixed step count strictly below 4,950 (PR #353, konstmish, on 2026-10-30) and below any lower AdamW-only claim in the README table or PRs, re-checked live.

## How a win is checked

Diff the claimed script against train_gpt_simple.py and confirm that only permitted sections changed. Re-run at least two seeds on an A100 or H100 and check that val loss at step S is within the claimant's per-run spread and that the pooled mean of all logs satisfies the formula. Confirm the stopping step is fixed in code and not chosen from validation. Re-fetch the track-3 README and the open PR list to confirm the bar.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/KellerJordan/modded-nanogpt/tree/master/records/track_3_optimization>

## Sources

- <https://github.com/KellerJordan/modded-nanogpt/tree/master/records/track_3_optimization>
- <https://raw.githubusercontent.com/KellerJordan/modded-nanogpt/master/records/track_3_optimization/README.md>
- <https://github.com/KellerJordan/modded-nanogpt/pulls>
- <https://github.com/KellerJordan/modded-nanogpt/pull/395>
- <https://github.com/KellerJordan/modded-nanogpt/pull/328>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Combine the orthogonal pending ideas (#395 SOAP-Shampoo with spectral annealing, #341 bi-Maxwell K-FAC momentum, tail-EMA readout) and ablate on a reduced-step proxy before full runs.
- Iterate cheaply on a shortened proxy (a smaller target or fewer steps) on one GPU, then confirm at full scale.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Per-run early stopping on validation is banned; the stopping step must be constant across trials.
- Third-party optimizer libraries must be copied into the script, not imported.
- The significance formula uses all runs launched; discarding bad seeds invalidates the claim.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/machine-learning/modded-nanogpt-track3-fewest-steps.md
```

Already set up? Say `run V3R1T4S on modded-nanogpt-track3-fewest-steps`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `modded-nanogpt-track3-fewest-steps`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
