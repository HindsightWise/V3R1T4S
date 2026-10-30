# 🦠 Biology

Protein, DNA and evolution benchmarks and record tables with mechanical checkers.

**47 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [CARE benchmark: beat the best published accuracy for retrieving the enzyme class (EC numb…](care-enzyme-reaction-retrieval-hard.md) | harvest | laptop-hours |
| ★★★★☆ | [Open Problems single-cell denoising: beat every listed method on the molecular-cross-vali…](openproblems-scrna-denoising-beat-leaderboard.md) | harvest | laptop-hours |
| ★★★★☆ | [Open Problems spatial decomposition: beat the best listed R^2 for cell-type proportions o…](openproblems-spatial-decomposition-r2.md) | harvest | laptop-hours |
| ★★★★☆ | [RNAGym ncRNA fitness: beat the top signed-Spearman macro score on the live zero-shot lead…](rnagym-ncrna-fitness-zero-shot-macro.md) | harvest | laptop-hours |
| ★★★★☆ | [Trastuzumab CDR-H3 variant binding (PLMFit herH3 one-vs-rest): beat the scoreboard MCC of…](plmfit-trastuzumab-cdrh3-binding-mcc.md) | standard | laptop-hours (174 training sequences, 36,386 test; the variable region is 10 aa, so CPU-only models suffice) |
| ★★★☆☆ | [ATOM3D RSR: beat the published Spearman for ranking RNA structural models by RMSD](atom3d-rsr-rna-model-ranking.md) | standard | laptop-hours (dataset is a few GB; CPU training of a modest model) |
| ★★★☆☆ | [BEACON RNA benchmark: beat the best listed score on an unsaturated task (CRISPR off-targe…](beacon-rna-benchmark-unsaturated-tasks.md) | harvest | laptop-hours (most tasks are short RNA sequences with 10^3-10^5 training examples; fine-tuning a 100M RNA language model wants a GPU) |
| ★★★☆☆ | [Burnt pancake sorting: settle T(n) for an even n by finding a flipping sequence that atta…](burnt-pancake-even-n-exact-flips.md) | standard | laptop-hours |
| ★★★☆☆ | [CATH 4.2 inverse folding: beat the best published sequence recovery (0.63, Refold) on the…](cath42-inverse-folding-recovery-record.md) | harvest | laptop-hours to laptop-days (GPU helps; the CATH 4.2 split is a few hundred MB) |
| ★★★☆☆ | [Eterna100-V2 under ViennaRNA 2: an automated RNA design algorithm that solves a puzzle no…](eterna100-v2-vienna2-algorithmic-solve.md) | harvest | laptop-hours |
| ★★★☆☆ | [FLAb antibody developability: beat the released zero-shot scores on a therapeutic-propert…](flab-antibody-developability-zero-shot.md) | standard | laptop-hours |
| ★★★☆☆ | [FLIP GB1 fitness landscape: beat the PLMFit scoreboard Spearman on the one-vs-rest or thr…](flip-gb1-plmfit-scoreboard-spearman.md) | harvest | laptop-hours (8,733 rows, 8,705 of them test under one-vs-rest; sequences are 265 aa with only four positions varying, so one-hot features or frozen small-ESM2 embeddings train on CPU in minutes) |
| ★★★☆☆ | [Genomic Benchmarks (Gresova et al.): beat the best published test accuracy on Human Enhan…](genomic-benchmarks-gresova-hard-datasets-accuracy.md) | harvest | laptop-hours (small CNN/SSM from scratch on sequences of 200-4,700 bp; a fine-tuned 100M+ model needs a GPU for hours) |
| ★★★☆☆ | [Minimizer schemes: beat the lowest published DNA density for a (w, k) pair in the public…](minimizer-density-record-tables.md) | harvest | laptop-hours |
| ★★★☆☆ | [Motif scaffolding benchmark (24 tasks): more unique in-silico successes than the publishe…](motif-scaffolding-24-task-unique-successes.md) | harvest | needs cluster (GPU for sampling plus ProteinMPNN/AlphaFold2 self-consistency over thousands of designs) |
| ★★★☆☆ | [Nucleotide Transformer benchmark: beat the best published MCC on a genomic regulatory task](nucleotide-transformer-benchmark-mcc.md) | standard | laptop-hours |
| ★★★☆☆ | [Open Problems batch integration: beat every listed method on the metrics where single-cel…](openproblems-batch-integration-hard-metrics.md) | standard | laptop-hours |
| ★★★☆☆ | [Open Problems label projection: beat the best listed accuracy/macro-F1 for transferring c…](openproblems-label-projection-cross-dataset.md) | harvest | laptop-hours |
| ★★★☆☆ | [Open Problems spatially variable genes: beat the best ranking correlation on the hardest…](openproblems-spatially-variable-genes-correlation.md) | harvest | laptop-hours |
| ★★★☆☆ | [PEER fold classification: beat the leaderboard's 32.1% accuracy on held-out SCOP superfam…](peer-fold-classification-superfamily-holdout.md) | harvest | laptop-hours |
| ★★★☆☆ | [ProteinBench apo-holo: beat TMens 0.873 for predicting both states of 91 conformational-c…](proteinbench-apo-holo-multistate-tmens.md) | standard | needs cluster (GPU; 20 conformations for each of 91 proteins) |
| ★★★☆☆ | [RNA secondary structure across families: beat the best published family-fold F1 on Archiv…](archiveii-interfamily-secondary-structure-f1.md) | standard | laptop-hours |
| ★★★☆☆ | [TraitGym Mendelian traits: beat CADD zero-shot AUPRC on causal non-coding variants for ra…](traitgym-mendelian-zero-shot-auprc.md) | harvest | laptop-hours |
| ★★★☆☆ | [TraitGym complex traits: beat the best AUPRC for picking the causal regulatory variant am…](traitgym-complex-traits-auprc.md) | standard | laptop-hours |
| ★★☆☆☆ | [DNA codes with GC-content and reverse-complement constraint: beat a lower bound in the A_…](dna-codes-gc-rc-king-table.md) | harvest | laptop-hours |
| ★★☆☆☆ | [DNA codes with constant GC-content: beat a lower bound in the Gaborit-King A_4^GC(n,d,w)…](dna-codes-gc-king-table.md) | harvest | laptop-hours |
| ★★☆☆☆ | [HomFam multiple sequence alignment: beat learnMSA2's best 66.92% mean total-column score…](homfam-msa-total-column-score.md) | standard | laptop-days (94 families of 93 to 93,681 sequences; protein-language-model embeddings need a GPU or many CPU hours) |
| ★★☆☆☆ | [Leakage-free protein-protein interaction prediction: beat the best published AUPR on the…](ppi-bernett-gold-standard-auprc.md) | standard | laptop-hours |
| ★★☆☆☆ | [Open Problems predict modality: beat the best listed RMSE for predicting protein abundanc…](openproblems-predict-modality-cite-rmse.md) | standard | laptop-hours |
| ★★☆☆☆ | [Plants Genomic Benchmark (AgroNT): beat the published R^2 for plant gene expression on he…](plant-genomic-benchmark-agront-expression-strength.md) | harvest | laptop-hours for promoter and terminator strength (170 bp, tens of thousands of sequences); needs a GPU for gene expression (6 kb inputs, 10^4-10^5 genes x tissues) |
| ★★☆☆☆ | [Protein Engineering Tournament pilot (supervised track): beat the best team Spearman on a…](protein-engineering-tournament-supervised-spearman.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Protein Engineering Tournament pilot (zero-shot track): beat the best team score on an un…](protein-engineering-tournament-zeroshot-spearman.md) | harvest | laptop-hours |
| ★★☆☆☆ | [T2T human genome compression: beat the best bits-per-base entry in the public human-genom…](t2t-human-genome-compression-record.md) | standard | laptop-days |
| ★★☆☆☆ | [geneRNIB: beat the best listed gene-regulatory-network inference scores on a perturbation…](genernib-grn-inference-beat-leaderboard.md) | standard | laptop-hours |
| ★★☆☆☆ | [Automated cryo-EM model building: raise completeness above ModelAngelo's 77% on its 177-m…](cryoem-automated-model-building-completeness.md) | standard | needs cluster (GPU; 177 maps, hundreds of GB of EMDB downloads) |
| ★★☆☆☆ | [CryoBench: beat the best published per-image FSC AUC for cryo-EM heterogeneity on a groun…](cryobench-heterogeneity-fsc-auc.md) | standard | needs cluster (GPU; 100k-335k simulated particles per dataset, tens of GB) |
| ★★☆☆☆ | [FLIP AAV capsid fitness: beat the PLMFit scoreboard Spearman on the one-vs-rest (one_vs_m…](flip-aav-capsid-plmfit-spearman.md) | standard | laptop-days (82,583 sequences; the mutated region is 28 aa so one-hot or small-embedding models are cheap, full-length embeddings are not) |
| ★★☆☆☆ | [FLIP meltome mixed split: beat the PLMFit scoreboard Spearman for melting temperature fro…](flip-meltome-mixed-plmfit-spearman.md) | standard | laptop-days (24,817 train / 3,134 test full-length proteins; CPU embedding of long sequences dominates, small-ESM2 features are feasible) |
| ★★☆☆☆ | [HP lattice protein folding: beat a best-known energy on a standard 2D/3D benchmark sequen…](hp-lattice-folding-benchmark-energies.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Maximum parsimony: a tree with fewer steps than the best-known score on a classic benchma…](parsimony-benchmark-best-scores.md) | standard | laptop-hours |
| ★★☆☆☆ | [ProteinBench (ATLAS): beat the best published conformational-ensemble distribution metric…](proteinbench-atlas-ensemble-distribution.md) | standard | needs cluster (GPU; 250 conformations for each of 82 proteins, plus metric computation) |
| ★★☆☆☆ | [Random Promoter DREAM Challenge: beat the best published Pearson/Spearman score for predi…](dream-random-promoter-yeast-expression.md) | standard | laptop-days (GPU shortens training; scoring is minutes) |
| ★★☆☆☆ | [SKEMPI 2.0 binding ddG: beat the published external-validation Pearson on the fixed S1131…](skempi2-binding-ddg-external-validation.md) | standard | laptop-hours to laptop-days (7,085 mutations with public complex structures; CPU-trainable graph and descriptor models) |
| ★★☆☆☆ | [Single-point folding stability ddG: beat the published Pearson on the leak-controlled S46…](folding-ddg-s461-megascale-records.md) | standard | laptop-hours for S461 inference and for training on the public ddG sets; laptop-days if the Megascale split is used for training |
| ★★☆☆☆ | [scTab cross-tissue cell-type annotation: beat macro F1 0.8441 on the CELLxGENE donor-held…](sctab-cellxgene-donor-holdout-macro-f1.md) | standard | needs cluster or a GPU workstation (22.2M cells; the processed train/val/test archive is 164 GB; inference on the 3.45M test cells fits on one GPU) |
| ★★☆☆☆ | [Edit-distance DNA codes with GC/homopolymer constraints: beat a published lower bound](edit-metric-dna-codes-gc.md) | standard | laptop-hours |
| ★★☆☆☆ | [ProteinGym zero-shot substitutions: beat every listed model's Spearman on a single DMS as…](proteingym-per-assay-zero-shot.md) | standard | laptop-hours |

← [All categories](../README.md)
