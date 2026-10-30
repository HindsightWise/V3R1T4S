# Neural Latents Benchmark '21 (test data now public): beat the final EvalAI leaderboard's top co-smoothing bits/spike on an NLB dataset split

🧠 **Neuroscience** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours (each dataset is tens to hundreds of MB of binned spikes on DANDI; transformer or SSM models train in hours on one GPU, slower on CPU) · open as of 2026-10-30

## The problem

NLB'21 (Pei, Ye, Zoltowski, Wu, Chowdhury, Sohn, O'Doherty, Shenoy, Kaufman, Churchland, Jazayeri, Miller, Pillow, Park, Dyer, Pandarinath; arXiv:2109.04463) asks models of neural population activity to predict the spiking of held-out neurons from held-in neurons on the same trials. The main metric is co-smoothing bits per spike (co-bps). There are five datasets on DANDI: MC_Maze, MC_RTT, Area2_Bump, DMFC_RSG, and MC_Maze Small/Medium/Large (the 'Scaling' split). Each is scored at 5 ms and at 20 ms bins. The EvalAI challenge (1256) ended on 2026-01-31. In January 2026 the organisers published the previously private test evaluation data in the data/ folder of neurallatents/nlb_tools, so anyone can now score models locally. These are the final leaderboard tops by co-bps. At 5 ms: MC_Maze 0.3862 (STNDT ensemble, Trung Le and Eli Shlizerman, UW NeuroAI); MC_RTT 0.2296 and DMFC_RSG 0.2020 (S5, Linderman Lab); Area2_Bump 0.2931 (Neural RoBERTa+RNNF ensemble, Makin lab); Scaling 100/250/500 trials 0.3711 and 0.3358 (NDT-U, Domenick Mifsud) and 0.3981 (Makin lab). At 20 ms: MC_Maze 0.3650, MC_RTT 0.2010, Area2_Bump 0.2881 and DMFC_RSG 0.1904 (LangevinFlow, team YueAndyMax, 2024); Scaling 0.3458/0.3329/0.3831 (MINT, Perkins, Cunningham and Churchland). Submissions kept arriving until 2025 (for example DLFM, 2025-07-13), so the bars are current as of the leaderboard's close. Outside the leaderboard, GRAFT (Xiangsheng Ge and Yang Xie, arXiv:2606.11066, June 2026) reports 0.3866 co-bps on MC_Maze at 5 ms on the public test split (ensemble; single model 0.3742), which raises that split's bar to 0.3866.

## What counts as a win

Pick one leaderboard split: a dataset, a bin size and, for Scaling, a trial count. Submit held-out-neuron rate predictions for its test trials, made by a model trained only on the train/val data (the test trials' held-in spikes are allowed as input, as in the challenge) and frozen before the public test evaluation data in nlb_tools/data is read. The skeptic computes co-bps with nlb_tools.evaluation.evaluate against that data. The score must be STRICTLY HIGHER (direction: max), by at least 0.005 bps, than both the top co-bps of that split on the final EvalAI leaderboard (re-fetched from eval.ai/api/jobs/challenge_phase_split/ < id > /leaderboard/ immediately before claiming) and any co-bps for the same split found by the NOVELTY check. For MC_Maze at 5 ms, the NOVELTY values include GRAFT's 0.3866 (arXiv:2606.11066). The other metrics of that split (vel R2 or tp corr, psth R2, fp-bps) are reported alongside.

## Partial wins

- **p1:** A single non-ensembled model whose co-bps on a 5 ms split strictly exceeds the best leaderboard entry on that split that is not labelled [Ensemble], by at least 0.003, under the same frozen-model rule.
- **p2:** On MC_RTT at 5 ms, a model whose vel R2 strictly exceeds the leaderboard's best vel R2 (0.6705, BAND, Ctrl-TNDM) while its co-bps is at least 0.2168, under the same frozen-model rule.
- **p3:** On any 20 ms split, beat the leaderboard top co-bps by at least 0.005 with a model that trains in under 4 hours on one consumer GPU or laptop CPU, with code released.

## How a win is checked

The skeptic clones nlb_tools at a commit on or after 2026-01-27 and fetches data/eval_data_test.h5 through git LFS (about 106 MB; the plain checkout holds only a pointer). They load the dataset from DANDI, run nlb_tools.evaluation.evaluate on the submitted prediction h5 file against that test evaluation data, and compare the result with the EvalAI leaderboard API (eval.ai/api/jobs/challenge_phase_split/ < 3179-3188 > /leaderboard/). They audit the training code and check that the eval data file is never opened before the final scoring. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://eval.ai/api/jobs/challenge_phase_split/3188/leaderboard/>

## Sources

- <https://github.com/neurallatents/nlb_tools>
- <https://neurallatents.github.io/>
- <https://eval.ai/web/challenges/challenge-page/1256/leaderboard>
- <https://arxiv.org/abs/2109.04463>
- <https://arxiv.org/abs/2606.11066>
- <https://dandiarchive.org/dandiset/000128>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensembles of diverse latent models (LFADS-style RNNs, NDT/STNDT transformers, S5 state-space models) took most 5 ms tops; averaging predicted rates from heterogeneous models is cheap.
- Pretraining on all five NLB datasets jointly, or on public DANDI motor-cortex data that is not an NLB test session, then fine-tuning per dataset.
- LangevinFlow is the 2024 leader at 20 ms; a 5 ms version of it may be competitive.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The test evaluation data is now public. Model selection or early stopping on it is leakage, and a claim must show that it was not read.
- Only public leaderboard entries are visible through the API; papers may report higher same-split numbers (GRAFT, arXiv:2606.11066, already does for MC_Maze at 5 ms). The NOVELTY check must cover the NLB papers linked from neurallatents.github.io and any 2026 papers that use the released test data.
- 5 ms and 20 ms are separate leaderboards with different tops; do not compare across bin sizes.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/neuroscience/nlb21-released-test-cobps.md
```

Already set up? Say `run V3R1T4S on nlb21-released-test-cobps`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nlb21-released-test-cobps`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
