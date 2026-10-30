# Motif scaffolding benchmark (24 tasks): more unique in-silico successes than the published best on a task

🦠 **Biology** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: needs cluster (GPU for sampling plus ProteinMPNN/AlphaFold2 self-consistency over thousands of designs) · open as of 2026-10-30

## The problem

The standard motif-scaffolding benchmark is the 25-task set curated by Joseph Watson, David Juergens, Nathaniel Bennett and colleagues for RFdiffusion, from six earlier publications. Genie 2 (Yeqing Lin, Minji Lee, Zhao Zhang and Mohammed AlQuraishi, arXiv:2405.15489) evaluates 24 of them (dropping 6VW1, whose motif spans chains) with a fully specified in-silico criterion: a design counts as a success when the self-consistency RMSD is at most 2 A, predicted pLDDT at least 70, predicted aligned error at most 5, and the motif backbone RMSD at most 1 A, and successes are clustered by single-linkage TM-score at 0.6 so only unique scaffolds count. Proteina (Tomas Geffner and co-authors, ICLR 2025, arXiv:2503.00710) re-ran that same criterion, clustering and sample budget (1,000 backbones per task) on the same 24 tasks and published the current record table, four columns wide: Proteina, Genie 2, RFdiffusion and FrameFlow (Jason Yim and co-authors), with 2,094 unique successes in total for Proteina against 1,445 for Genie 2. Per task the best published counts are now 6E6R_long 713, 6E6R_med 417, 1YCR 249, 5TRV_long 179, 6E6R_short 56, 7MRX_85 31, 4ZYP 11 and 5YUI 5 (Proteina); 6EXZ_long 403, 6EXZ_med 110, 1QJG 18 and 5WN9 3 (FrameFlow); 7MRX_128 66 (RFdiffusion); 3IXT 14, 5TPN 8, 7MRX_60 5, 5TRV_med 23 and 5TRV_short 3 (Genie 2); 6EXZ_short 3 (Proteina and FrameFlow); and 1PRW, 5IUS, 1BCF and 2KL8 at 1 each. Ten of the 24 tasks are still at or below 8 unique successes and 4JHW has no unique success in any of the four columns, while the scoring pipeline (ProteinMPNN plus a structure predictor) is public and the win is a file of backbones and sequences. Two later suites must be surveyed but are not this benchmark: MotifBench (arXiv:2502.12479) scores a different 30-problem set, including two 4JHW cases, under its own criterion and clustering; and GPFlow (arXiv:2607.09039) reports much higher counts on several of these tasks (for example 1PRW 42, 1BCF 11, 3IXT 398, 4ZYP 144, and 4JHW still 0) but clusters successes with FoldSeek and merges the length variants of a task, so its numbers are not counts under this criterion. This target is about in-silico benchmark scores only.

## What counts as a win

For a declared task of the 24-task benchmark: a published set of designed backbones with their designed sequences and the exact sampling configuration (model, N samples, seeds), such that the skeptic, re-running the benchmark's own public self-consistency pipeline (ProteinMPNN sequence design plus the declared structure predictor at a pinned version) and applying the published criterion (scRMSD <= 2 A, pLDDT >= 70, pAE <= 5, motif backbone RMSD <= 1 A, single-linkage TM-score clustering at 0.6), counts a number of unique successes STRICTLY HIGHER (direction: max) than the best published count for that task across the four columns of arXiv:2503.00710 Table 5 (Proteina, Genie 2, RFdiffusion, FrameFlow) and the Genie 2 table of arXiv:2405.15489, both re-fetched live immediately before claiming, and than any later published count for the same task and criterion found by the novelty check, at the same or a smaller sample budget N, with the per-sample metric table published. For 4JHW, at least one unique success under this criterion and the benchmark's own motif specification counts as the full win, provided the novelty check finds no earlier published unique success for 4JHW under this criterion. The motif specification must be the benchmark's own (same residues, same contiguity and length ranges), and no experimental structure of the benchmark's native scaffold may be used as a template.

## Partial wins

- **p1:** At least one unique success on 4JHW under the published criterion and the benchmark's own motif specification, verified by the skeptic's re-run of the scoring pipeline, with the novelty check reporting whether any earlier 4JHW success has been published under this, the MotifBench or the FoldSeek-clustered GPFlow criterion.
- **p2:** Strictly more unique successes than the best published count on at least three of the tasks still at or below 8 (1PRW 1, 5IUS 1, 1BCF 1, 2KL8 1, 5TRV_short 3, 6EXZ_short 3, 5WN9 3, 5YUI 5, 7MRX_60 5, 5TPN 8) at the same or a smaller sample budget.
- **p3:** A reproduction artefact: reproducing a published per-task unique-success count to within 20 percent on at least five tasks with public weights and the public scoring pipeline, with the harness and all per-sample metrics published.

## How a win is checked

Skeptic takes the attacker's backbones and sequences, re-runs ProteinMPNN and the declared structure predictor at the pinned versions, recomputes scRMSD, pLDDT, pAE and motif RMSD per design, applies the TM-score 0.6 clustering to count unique successes, checks the motif residues and length ranges against the benchmark specification, confirms the sample budget from the published seeds and configs, and re-fetches the published tables. Hours of GPU time for scoring; sampling is the attacker's cost.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2503.00710>

## Sources

- <https://arxiv.org/html/2405.15489>
- <https://arxiv.org/abs/2503.00710>
- <https://github.com/aqlaboratory/genie2>
- <https://arxiv.org/abs/2502.12479>
- <https://arxiv.org/abs/2607.09039>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Condition harder on the motif: increase the fraction of conditional training or inference-time guidance strength, which the Genie 2 ablation shows moves the success count substantially.
- Diversity is what is scored (unique clusters, not raw successes), so explicitly penalise similarity to already-accepted designs during sampling rather than drawing more independent samples.
- Cross-domain import (constrained generation): treat the motif as a hard constraint via projection or twisted sampling at every denoising step instead of a soft loss, which is what made TDS-style samplers work on hard motifs.
- The never-solved task is a long, mostly-helical epitope: try scaffolding it inside a larger designed fold with explicit secondary-structure conditioning, and report the per-sample metric distribution to see which threshold fails.
- Measure which of the four thresholds fails most often per task; if pAE is the binding constraint, more samples will not help and the fold choice must change.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Scoring details move the count a lot: predictor version, single-sequence vs MSA input, number of ProteinMPNN sequences per backbone and the clustering threshold must all be pinned and re-run by the skeptic.
- Counts clustered another way are not counts here: GPFlow clusters with FoldSeek and merges a task's length variants, and MotifBench uses its own criterion, so neither sets the bar for a task on this benchmark.
- Loosening or re-defining the motif (fewer residues, wider length ranges) makes the task easier and is not the benchmark; the specification must be the published one.
- Unique successes depend on the sample budget, so a count at 10,000 samples is not comparable to a published count at 1,000; the budget must be equal or smaller.
- Self-consistency success is an in-silico proxy: a win here says nothing about whether any design folds or functions in reality, and no claim beyond the benchmark is admissible.
- Templating from the native scaffold of the motif's source structure is leakage and is excluded by the criterion.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/motif-scaffolding-24-task-unique-successes.md
```

Already set up? Say `run V3R1T4S on motif-scaffolding-24-task-unique-successes`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `motif-scaffolding-24-task-unique-successes`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
