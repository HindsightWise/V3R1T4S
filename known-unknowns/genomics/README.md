# 🧫 Genomes

Genome assembly, variant calling, metagenome binning and comparative genomics scored against released truth sets.

**10 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [CAMI II genome binning: recover more near-complete genomes from the gold-standard co-asse…](cami2-genome-binning-recovered-genomes.md) | harvest | laptop-days (pooled gold-standard assemblies of a few Gbp plus 10, 100 or 21 short-read samples of about 5 Gbp each to map for coverage; 32-64 GB RAM advisable, GPU optional) |
| ★★★☆☆ | [CAMI II taxonomic binning of reads at species rank: beat ganon2's per-bin F1 on the plant…](cami2-taxonomic-binning-species-f1.md) | standard | laptop-days (classify 21 short-read samples of about 5 Gbp each against an index of the 2019-01-08 RefSeq snapshot; 64 GB RAM helps) |
| ★★★☆☆ | [CAMI II taxonomic profiling at species rank: beat ganon2's F1 on the plant-associated sam…](cami2-taxonomic-profiling-species-f1.md) | harvest | laptop-days (21 plant-associated samples of about 5 Gbp each; building an index over the 2019-01-08 NCBI RefSeq snapshot is the heavy step, 64 GB RAM helps) |
| ★★★☆☆ | [DeepSomatic on held-out HCC1395 chr1: beat DeepSomatic 1.10's somatic F1, especially ONT…](deepsomatic-hcc1395-chr1-heldout-f1.md) | harvest | laptop-hours per cell (the tumor and normal chr1 BAMs are 8-10 GB each); a GPU helps but is not required |
| ★★☆☆☆ | [DeepVariant case-study accuracy: beat DeepVariant 1.10's documented F1 on its own public…](deepvariant-case-study-accuracy-records.md) | harvest | laptop-hours for a chr20 cell (5.9 GB ONT chr20 BAM); a large cloud VM or cluster for whole-genome cells (the HG003 ONT BAM is 131 GB) |
| ★★☆☆☆ | [HG002 nanopore read correction scored against the Q100 genome: corrected ONT reads with f…](hg002-ont-read-correction-gqc-error-rate.md) | standard | needs cluster or a GPU workstation for the full about 115 Gb read set; laptop-days for a single-chromosome partial |
| ★★☆☆☆ | [precisionFDA Truth Challenge V2 (finished, answers released): beat the best submission's…](precisionfda-truth-challenge-v2-difficult-mhc.md) | harvest | laptop-days per sample for the Illumina 35x cells (alignment plus calling); needs cluster for the 85x ONT and the multi-technology cells |
| ★★☆☆☆ | [CAMI II metagenome assembly: beat MetaHipMer 2.2.0's strain F1 on the marine short-read c…](cami2-metagenome-assembly-strain-f1.md) | standard | needs cluster (co-assembling 10 marine samples of about 5 Gbp short reads each needs roughly 100-500 GB RAM; MetaQUAST against 977 reference genomes takes hours) |
| ★★☆☆☆ | [HG002 vs the Q100 genome benchmark: an automated diploid assembly with fewer GQC errors t…](hg002-q100-gqc-automated-assembly-errors.md) | standard | needs cluster (a diploid human assembly takes hundreds of CPU-hours and over 100 GB of RAM; GQC takes about 64 GB and 4 hours per assembly) |
| ★★☆☆☆ | [Quest for Orthologs 2022 SwissTree benchmark: ortholog predictions that beat every public…](qfo-swisstree-orthology-dominance.md) | standard | laptop-days (orthology inference on the 78 QfO 2022_02 reference proteomes; the QfO benchmark pipeline runs in Docker/Nextflow) |

← [All categories](../README.md)
