# ProteinBench apo-holo: beat TMens 0.873 for predicting both states of 91 conformational-change proteins

🦠 **Biology** · standard · tractability ★★★☆☆ · compute: needs cluster (GPU; 20 conformations for each of 91 proteins) · open as of 2026-10-30

## The problem

ProteinBench (Fei Ye, Zaixiang Zheng, Dongyu Xue and co-authors; ICLR 2025, arXiv:2409.06744) includes a multiple-state prediction task built on 91 apo-holo protein pairs curated by Saldaño et al. (Bioinformatics 2022). The task is to sample 20 conformations per protein from the apo sequence and score how well the ensemble covers both experimental states. apo-TM and holo-TM are the best TM-score of any sample to each state, and TMens is their arithmetic mean; all three are averaged over the 91 proteins. Pairwise TM measures diversity, and CA-clash and peptide-bond-break percentages check validity. Published values (Table 14; the same rows are on the ProteinBench Hugging Face leaderboard, last changed 2024-12-10): AlphaFlow-PDB leads with TMens 0.873 (apo-TM 0.855, holo-TM 0.891). It is followed by MSA-depth256 and ConfDiff-Open-PDB at 0.867 and ESMFlow-PDB at 0.866, with AlphaFlow-MD best on apo-TM at 0.857; Str2Str variants fall to 0.68-0.77. The row that makes this a real open problem is the trivial reference: submitting the experimental apo structure as the only prediction scores TMens 0.895 (apo 1.000, holo 0.790). That is above every method, so no sampler yet covers the holo state well enough to beat a one-state baseline that models no change at all. Later papers that use 90 of these pairs with 5 samples per protein stay below 0.873: ConfDiff (arXiv:2403.14088) and the structure-language-model/ESMDiff paper (arXiv:2410.18403, AlphaFlow 0.864 mean). ProteinBench has no evaluation repository of its own. The 91-target list (revision1_86_plus_5.csv, from Saldaño et al. via EigenFold) and an apo-holo scoring script are public in the same group's ConfDiff repository (github.com/bytedance/ConfDiff, datasets/apo), and all structures are in the PDB.

## What counts as a win

At least 20 sampled conformations for each of the 91 apo-holo targets of revision1_86_plus_5.csv. They must be generated from the apo sequence alone, using sequence databases or MSAs only. No experimental apo or holo coordinates of a test protein may be used as input, template, starting conformation or selection signal, and no ligand identity taken from the holo entry may be used as input. The skeptic recomputes the metrics with the apo-holo evaluation in github.com/bytedance/ConfDiff (datasets/apo, src/analysis/apo.py, TMscore binary, 20 samples) and must obtain a TMens (mean over the 91 proteins, as the published table reports) STRICTLY HIGHER (direction: max) than 0.873 by at least 0.005. 0.873 is AlphaFlow-PDB, arXiv:2409.06744 Table 14, re-fetched live immediately before claiming. The TMens must also be higher than any later published TMens for the same task found by the novelty check. apo-TM, holo-TM, pairwise TM, CA clash percentage and peptide-bond-break percentage must all be reported, and validity must stay within the published range (CA clash at most 1.0 percent, peptide-bond breaks at most 10.0 percent). Conformations, configs and seeds must be published so the metrics recompute. Passing the 0.895 apo-structure reference row is the standing goal and should be stated when reached.

## Partial wins

- **p1:** A holo-TM strictly above 0.891 (AlphaFlow-PDB) by at least 0.005 with TMens at or above 0.867, under the same no-experimental-input rule.
- **p2:** TMens strictly above 0.873 by at least 0.005 while using at most 5 sampled conformations per protein instead of 20, with the sampling budget and compute reported.
- **p3:** A reproduction artefact: reproducing a published row (method, apo-TM, holo-TM, TMens) within 0.005 with public weights and the public metric code, with runtime and hardware published.

## How a win is checked

Skeptic builds the 91 apo and holo reference structures from revision1_86_plus_5.csv with the ConfDiff datasets/apo pipeline (make_csv.py from RCSB mmCIF files). The skeptic checks that the submission covers every protein with the required number of conformations and correct apo sequences, then recomputes apo-TM, holo-TM, TMens, pairwise TM and the validity metrics with the ConfDiff apo evaluation and the TMscore binary. The skeptic inspects configs and logs to confirm that no experimental structure of a test protein entered generation or model selection (including as a template or a starting conformation) and that no holo ligand was given as input, and re-fetches the published table. Hours of compute.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2409.06744v2>

## Sources

- <https://arxiv.org/html/2409.06744v2>
- <https://arxiv.org/abs/2409.06744>
- <https://proteinbench.github.io/>
- <https://huggingface.co/spaces/proteinbench/ProteinBench>
- <https://github.com/bytedance/ConfDiff/tree/main/datasets/apo>
- <https://arxiv.org/abs/2410.18403>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- MSA subsampling at depth 256 nearly matches the best flow models while being far cheaper; sweep depth jointly with a diversity-aware selection rule before training anything new.
- The metric rewards covering two specific states, not broad diversity: sample a few well-separated modes (for example by clustering a large cheap ensemble and keeping cluster centres) rather than 20 random draws.
- Cross-domain import (coverage/recall in generative models): optimise an explicit two-mode coverage objective, since TMens is a max-over-samples quantity per state and is dominated by the single best sample for each state.
- Ligand-free holo prediction is the hard half: test whether a pocket-closure prior (predicted cavity volume) helps steer samples toward the holo state.
- Watch validity: several methods trade peptide-bond integrity for diversity, and a short relaxation step recovers it cheaply.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 'apo model' row uses the experimental apo structure and is a reference, not a competitor; using any experimental coordinates of a test protein makes a result inadmissible.
- Co-folding with the bound ligand copies information from the holo experiment; ligand-conditioned runs may be reported as a separate row but do not count toward the bar.
- AlphaFlow/ESMFlow/ConfDiff variants trained on MD or PDB snapshots may have seen the holo states; training data and cutoffs must be declared.
- TMens, apo-TM and holo-TM move together; reporting only the one that improved hides a regression, so all are required.
- Sampling budget changes the max-over-samples metrics; 20 conformations per protein is the published protocol. Papers using 5 samples or EigenFold's 90-pair splits/apo.csv are not on the same footing.
- There is no official ProteinBench evaluation repo (github.com/bytedance/ProteinBench returns 404 as of 2026-10-30); use the ConfDiff apo scorer and state its commit.
- A benchmark gain on 91 pairs is not evidence about any particular protein's mechanism; claims must stop at the benchmark.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/proteinbench-apo-holo-multistate-tmens.md
```

Already set up? Say `run V3R1T4S on proteinbench-apo-holo-multistate-tmens`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `proteinbench-apo-holo-multistate-tmens`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
