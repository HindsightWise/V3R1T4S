# OGB ogbg-molpcba: beat the leaderboard's top test AP (0.3204) on 128 PubChem bioassays

💊 **Drug discovery** · standard · tractability ★★☆☆☆ · compute: laptop-days (437,929 molecules, 128 tasks; a GPU shortens training, fingerprint forests run on CPU) · open as of 2026-10-30

## The problem

ogbg-molpcba (Open Graph Benchmark, Hu et al. 2020, from MoleculeNet's PCBA) asks 128 sparse binary bioactivity questions about each of 437,929 molecules. It uses a fixed scaffold split and is scored by test average precision (AP), averaged over tasks and over at least 10 runs. Among entries without external data, HyperFusion (Xinwei Zhang, Tsinghua, 2024-02-24) leads at 0.3204 +- 0.0001. It is followed by PDF (Mingqi Yang, 2023) at 0.3031, PAS (Xu Wang, 4Paradigm) at 0.3012 and the Nested GIN + virtual node ensemble (Muhan Zhang) at 0.3007. The strongest classic-GNN entry, GatedGCN+ (Yuankai Luo, PolyU, 2025-02-13), reaches 0.2981. Entries pretrained on PCQM4M (HIG 0.3167, Graphormer 0.3140) are marked as using external data. The best CPU entry is MorganFP + Random Forest (Cyrus Maher) at 0.2054. Can a model without external data beat 0.3204?

## What counts as a win

Saved code, seeds and per-run test predictions such that, on the official ogbg-molpcba scaffold split with ogb's Evaluator, the mean test AP over at least 10 runs (seeds 0-9 or the first 10 runs, all reported; selection by validation AP only) is STRICTLY GREATER (direction: max) than the highest 'Test AP' among 'Ext. data' = 'No' rows of the ogbg-molpcba table at https://ogb.stanford.edu/docs/leader_graphprop/, re-fetched live immediately before claiming (0.3204 on 2026-10-30). Fingerprints and descriptors computed from the molecules themselves are allowed. Models pretrained on any outside molecular data are not.

## Partial wins

- **p1:** A model with fewer than 4,000,000 learned parameters whose 10-run mean test AP is strictly above 0.3031 (PDF, Mingqi Yang, 3,842,048 params, the best entry under 4M on 2026-10-30), under the full-win protocol and the no-external-data rule.
- **p2:** A method with no neural network (tree ensembles, kernel or linear models on fingerprints and descriptors computed from the molecules themselves), trained entirely on CPU, whose 10-run mean test AP is strictly above 0.2500, beating the board's only non-neural entry (MorganFP+Rand. Forest, Cyrus Maher, 0.2054) by a wide margin, under the full-win protocol and the no-external-data rule. Re-running a listed GNN on CPU does not count.

## How a win is checked

Load ogbg-molpcba with ogb and re-run 2 of the 10 seeds. Score all saved predictions with ogb.graphproppred.Evaluator('ogbg-molpcba'), which ignores NaN labels. Check validation-only selection and that no pretrained checkpoint is loaded, then re-fetch the leaderboard.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ogb.stanford.edu/docs/leader_graphprop/>

## Sources

- <https://ogb.stanford.edu/docs/leader_graphprop/>
- <https://ogb.stanford.edu/docs/graphprop/>
- <https://ogb.stanford.edu/docs/leader_rules/>
- <https://arxiv.org/abs/2005.00687>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Multi-task structure: the 128 assays share chemistry, so task-relationship priors (assay-assay label correlations from training data) can regularise rare tasks.
- Self-supervised pretraining on the 437k unlabelled molecules of this dataset only (allowed), then fine-tuning.
- Per-task fingerprint gradient boosting blended with a GNN, weighted by validation AP per task.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Pretraining on PCQM4M, ZINC or ChEMBL is external data and moves the entry to the other comparison.
- AP averages only over tasks with both classes in the test split; use the evaluator rather than a hand-rolled metric.
- HyperFusion's spread is tiny (0.0001); a claim must exceed its mean, not its lower bound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/drug-discovery/ogbg-molpcba-beat-leaderboard-ap.md
```

Already set up? Say `run V3R1T4S on ogbg-molpcba-beat-leaderboard-ap`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ogbg-molpcba-beat-leaderboard-ap`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
