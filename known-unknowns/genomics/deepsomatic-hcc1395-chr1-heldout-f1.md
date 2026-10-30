# DeepSomatic on held-out HCC1395 chr1: beat DeepSomatic 1.10's somatic F1, especially ONT (SNV 0.858, indel 0.737) and tumor-only modes

🧫 **Genomes** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours per cell (the tumor and normal chr1 BAMs are 8-10 GB each); a GPU helps but is not required · open as of 2026-10-30

## The problem

DeepSomatic (Jimin Park, Daniel Cook, Alexey Kolesnikov, Andrew Carroll, Pi-Chuan Chang and colleagues at Google with Benedict Paten's group at UCSC; Nature Biotechnology 2026, doi 10.1038/s41587-025-02839-x, preprint bioRxiv 10.1101/2024.08.16.608331) calls somatic SNVs and indels from tumor-normal or tumor-only reads. Its case-study pages on github.com/google/deepsomatic, branch r1.10 (DeepSomatic 1.10.0, the newest release on 2026-10-30), score chr1 of HCC1395/HCC1395BL, which is held out during training, with som.py against the SEQC2 high-confidence truth v1.2.1 (Li Tai Fang, Wenming Xiao and the SEQC2 Somatic Mutation Working Group, Nat Biotech 2021). From recall and precision, the chr1 F1 values are (3,440 truth SNVs, 133 truth indels): Illumina WGS, SNV 0.9761 and indel 0.9091; PacBio, SNV 0.9489 and indel 0.8188; ONT, SNV 0.8576 (recall 0.7608) and indel 0.7373; FFPE WGS, SNV 0.8817 and indel 0.7766; tumor-only Illumina WGS, SNV 0.7480 and indel 0.3741; PacBio tumor-only, SNV 0.7751 and indel 0.5178; ONT tumor-only, SNV 0.6705 and indel 0.3653. The metrics.md table reports whole-genome numbers that include training chromosomes. The chr1 BAMs (1-15 GB each), truth VCF and BED are public over HTTPS, so each cell is a self-contained, laptop-scale record.

## What counts as a win

A somatic VCF for HCC1395 chr1, for one stated mode (tumor-normal or tumor-only) and one technology, called only from that mode's case-study chr1 BAMs, plus declared public population resources (for example gnomAD or a 1000 Genomes panel of normals) that contain no HCC1395 data. It is scored by the skeptic with som.py exactly as in the case-study page: truth high-confidence_sINDEL_sSNV_in_HC_regions_v1.2.1.merged.vcf.gz, -R High-Confidence_Regions_v1.2.bed, -l chr1, --feature-table generic. Its F1 = 2PR/(P+R) for SNVs or indels must be STRICTLY HIGHER (direction: max) than the DeepSomatic value on the newest case-study page for that mode, re-fetched live: by at least 0.01 for SNVs or 0.03 for indels, with the other type no more than 0.005 below its listed F1. It must also beat ClairS (tumor-normal) or ClairS-TO (tumor-only), newest release with the matching model, run on the same BAMs and scored the same way, by the same margin. No HCC1395 chr1 truth, and no SEQC2 callset used to build the truth, may be used in training, tuning or filtering. The method is released.

## Partial wins

- **p1:** ONT tumor-normal chr1: SNV recall of at least 0.810756 (0.760756 plus 0.05) with SNV precision of at least 0.97, and SNV F1 above ClairS (newest release, matching ONT model) on the same BAMs.
- **p2:** Illumina WGS tumor-only chr1: SNV F1 of at least 0.7780 (0.7480 plus 0.03) and above ClairS-TO (newest release) on the same BAM, using only declared public germline resources for germline filtering.
- **p3:** FFPE WGS tumor-normal chr1: SNV F1 of at least 0.9017 (0.8817 plus 0.02) and above ClairS (newest release, Illumina model) on the same BAMs.

## How a win is checked

Skeptic downloads the chr1 BAMs and reference from storage.googleapis.com/deepvariant/deepsomatic-case-studies/deepsomatic-chr1-case-studies and the truth from .../SEQC2-S1395-truth over plain HTTPS, reruns the claimant's released caller, runs the case-study som.py command in the pkrusche/hap.py container, reruns ClairS or ClairS-TO on the same BAMs, and compares with the live case-study page. One to a few hours per cell.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/google/deepsomatic/r1.10/docs/deepsomatic-case-study-ont.md>

## Sources

- <https://raw.githubusercontent.com/google/deepsomatic/r1.10/docs/deepsomatic-case-study-ont.md>
- <https://raw.githubusercontent.com/google/deepsomatic/r1.10/docs/deepsomatic-case-study-wgs.md>
- <https://raw.githubusercontent.com/google/deepsomatic/r1.10/docs/deepsomatic-case-study-pacbio.md>
- <https://raw.githubusercontent.com/google/deepsomatic/r1.10/docs/deepsomatic-case-study-wgs-tumor-only.md>
- <https://raw.githubusercontent.com/google/deepsomatic/r1.10/docs/deepsomatic-case-study-ffpe-wgs.md>
- <https://raw.githubusercontent.com/google/deepsomatic/r1.10/docs/metrics.md>
- <https://doi.org/10.1038/s41587-025-02839-x>
- <https://www.biorxiv.org/content/10.1101/2024.08.16.608331>
- <https://github.com/HKU-BAL/ClairS>
- <https://github.com/HKU-BAL/ClairS-TO>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- ONT tumor-normal loses mostly recall (823 of 3,440 SNVs missed), so the gap is in low-VAF candidate generation, not in classification; haplotype-aware candidate rescue (somatic variants sit on one haplotype) is the obvious lever.
- Cross-domain import (radio astronomy stacking): pool weak evidence across reads on the same haplotype block before thresholding, rather than deciding per site.
- In tumor-only mode the false positives are mostly germline; phase-aware germline/somatic separation using allele fraction relative to local copy number can cut them without a panel of normals.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The whole-genome numbers in metrics.md include chromosomes DeepSomatic was trained on; only chr1 is held out, so only chr1 counts here.
- ClairS's README reports HCC1395 numbers against HighConf plus MedConf truth at VAF 0.05 or more, a different truth subset; never compare them with the som.py numbers here.
- With 133 truth indels, one or two variants move F1 by about 0.01, which is why the indel margin is 0.03.
- SEQC2 consensus callsets were built from the same cell line's data; using them as features or filters leaks the truth.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/deepsomatic-hcc1395-chr1-heldout-f1.md
```

Already set up? Say `run V3R1T4S on deepsomatic-hcc1395-chr1-heldout-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `deepsomatic-hcc1395-chr1-heldout-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
