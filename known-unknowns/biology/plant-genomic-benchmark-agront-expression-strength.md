# Plants Genomic Benchmark (AgroNT): beat the published R^2 for plant gene expression on held-out gene families or for promoter and terminator strength

🦠 **Biology** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for promoter and terminator strength (170 bp, tens of thousands of sequences); needs a GPU for gene expression (6 kb inputs, 10^4-10^5 genes x tissues) · open as of 2026-10-30

## The problem

The Plants Genomic Benchmark (PGB) was released with AgroNT (Javier Mendoza-Revilla, Evan Trop, ..., Thomas Pierrot and Marie Lopez, InstaDeep; Communications Biology 7, 835, 2024) at huggingface.co/datasets/InstaDeepAI/plant-genomic-benchmark, with fixed splits and the numeric data behind every figure. Values (as R^2, from the paper and its Figures folder): promoter strength (plant STARR-seq of Jores et al. 2021), AgroNT in the maize protoplast system 0.62 (A. thaliana promoters), 0.68 (S. bicolor), 0.71 (Z. mays), and in the tobacco leaf system 0.62, 0.74, 0.75, against the Jores CNN at 0.57-0.73. Terminator strength (Gorjifard et al.): AgroNT 0.65-0.77 against the Gorjifard CNN at 0.64-0.77; they tie in two tobacco cells (0.77 for A. thaliana, 0.76 for Z. mays), and the CNN is higher in one cell (Z. mays terminators in the maize system, 0.67 against 0.65; Figures/Fig3_panelf.txt). Tissue-specific gene expression from promoter-proximal 6 kb (5 kb upstream, 1 kb downstream of the TSS), on test genes from held-out gene families: squared Pearson between predicted and observed across all held-out gene x tissue values, recomputed from Figures/Fig5_panela.txt: A. thaliana 0.617, Z. mays 0.621, S. lycopersicum 0.552, G. max 0.533, O. sativa 0.419. For Z. mays only, AgroNT trained on windows shifted downstream reached up to 0.662 (1 kb upstream, 5 kb downstream; Figures/Fig6_panelb.txt), so that is the Z. mays bar. The paper calls tissue-specific expression an open challenge; AgroNT is a 1B-parameter model, so a smaller model that matches it is also informative.

## What counts as a win

Predictions for every test example of a PGB task (promoter_strength, terminator_strength, or gene_exp for one species), from a model trained only on that task's PGB train split (validation for selection; pretrained weights allowed if declared; for gene_exp, extra genomic context around the same genes is allowed if declared, but no gene from a test gene family may enter training), whose metric, computed by the skeptic on the PGB test split (R^2 as in the paper; for gene expression, squared Pearson over all test gene x tissue values), is STRICTLY HIGHER (direction: max) than the best published value for that cell (AgroNT, or the Jores or Gorjifard CNN where higher) by at least 0.02 and higher than any later published value on the same split found by a novelty check. Bars as of 2026-10-30: promoter maize system 0.62 / 0.68 / 0.71 and tobacco 0.62 / 0.74 / 0.75; terminator maize 0.69 / 0.68 (GC) / 0.67 (Z. mays, Gorjifard CNN) and tobacco 0.77 / 0.67 / 0.76; gene expression A. thaliana 0.617, Z. mays 0.662 (Fig. 6b), S. lycopersicum 0.552, G. max 0.533, O. sativa 0.419.

## Partial wins

- **p1:** Gene expression: beat AgroNT's O. sativa value (0.419) by at least 0.03 squared Pearson on the PGB test split with a model of at most 100M parameters.
- **p2:** Promoter strength: one recipe that beats AgroNT on all six promoter cells (both systems, three species) at once, mean of three seeds.
- **p3:** Terminator strength: beat both AgroNT and the Gorjifard CNN by at least 0.02 R^2 on any terminator cell.

## How a win is checked

Skeptic downloads the task's raw files from the Hugging Face dataset (without running its loading script), checks prediction coverage of the test split, computes R^2 or squared Pearson, compares with the Figures/*.txt values (Fig3_panele, Fig3_panelf, Fig5_panela), reruns one seed, and checks that no test gene family or test sequence is in training. Under an hour for strength tasks.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://huggingface.co/datasets/InstaDeepAI/plant-genomic-benchmark>

## Sources

- <https://www.nature.com/articles/s42003-024-06465-2>
- <https://huggingface.co/datasets/InstaDeepAI/plant-genomic-benchmark>
- <https://huggingface.co/datasets/InstaDeepAI/plant-genomic-benchmark/tree/main/Figures>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Promoter strength is short-sequence MPRA regression; DREAM-challenge style CNN/RNN recipes (LegNet, DREAM-RNN) are strong and cheap.
- Gene expression: the paper's own window scan (Fig. 6) shows that more downstream context helps; try 3' UTR and gene-body features as well.
- Cross-domain import (multi-task learning): predict all tissues jointly with a low-rank output head, since tissue profiles are strongly correlated.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The dataset's loading script is code; read the raw files directly instead of executing it.
- Gene-expression test genes are held out by gene family; any training gene from the same family breaks the design.
- Gene-expression R^2 is pooled over genes x tissues; a per-tissue mean gives different numbers, so state which one, and compare like with like.
- Promoter-strength labels differ by assay system (maize protoplast versus tobacco leaf); do not mix the two bars.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/plant-genomic-benchmark-agront-expression-strength.md
```

Already set up? Say `run V3R1T4S on plant-genomic-benchmark-agront-expression-strength`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `plant-genomic-benchmark-agront-expression-strength`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
