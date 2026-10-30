# DeepVariant case-study accuracy: beat DeepVariant 1.10's documented F1 on its own public held-out inputs, above all ONT R10.4.1 indels (0.9302) and RNA-seq

🧫 **Genomes** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for a chr20 cell (5.9 GB ONT chr20 BAM); a large cloud VM or cluster for whole-genome cells (the HG003 ONT BAM is 131 GB) · open as of 2026-10-30

## The problem

Google's DeepVariant team (Pi-Chuan Chang, Andrew Carroll, Kishwar Shafin and colleagues) keeps a public accuracy table for each release: docs/metrics.md and docs/pangenome-aware-metrics.md on branch r1.10 (release v1.10.0, 2026-03-05, still the newest on 2026-10-30). They are whole-genome hap.py (vcfeval) runs against the NIST/GIAB v4.2.1 benchmarks maintained by Justin Zook and Nathan Olson. HG003 has been left out of training since v1.1 and chr20-22 have never been used; HG005 is held out of the RNA-seq model. Current HG003 F1: Illumina WGS 35x, INDEL 0.99598, SNP 0.996136; pangenome-aware WGS (vg Giraffe BAM of the same reads), INDEL 0.996976, SNP 0.998139; WES, INDEL 0.98328, SNP 0.992926 (pangenome-aware SNP 0.993544); PacBio Revio SPRQ, INDEL 0.994173, SNP 0.99852; ONT R10.4.1, INDEL 0.930243 (recall 0.912496, precision 0.948695), SNP 0.998451; hybrid PacBio+Illumina, INDEL 0.996838. HG005 poly-A RNA-seq, GENCODE CDS at 3x or more: SNP 0.951595, INDEL 0.806842. The ONT case-study page adds a chr20 cell (80x ultra-long simplex): INDEL 0.897772, SNP 0.999031. ONT indels (mostly homopolymer length) and RNA-seq calls are where a strong open caller is still well below 0.99. Input BAMs (named in scripts/inference_deepvariant.sh r1.10), truth files and DeepVariant outputs are public over HTTPS on storage.googleapis.com/deepvariant.

## What counts as a win

A VCF for one cell (a row of the r1.10 metrics pages, or the chr20 ONT case study), called only from that cell's reads (the BAM named in inference_deepvariant.sh r1.10 or the case-study page; realigning those same reads is allowed) on GRCh38 no-alt, with no other data from HG002, HG003, HG004 or HG005, including pangenomes or panels that contain them. The skeptic scores it with hap.py v0.3.12 --engine=vcfeval --pass-only against that preset's truth VCF and BED (HG003: v4.2.1 benchmark_noinconsistent.bed). For RNA-seq the region is the case study's protocol extended to chr1-22 (GENCODE v41 basic CDS, 3x or more coverage, intersected with the HG005 v4.2.1 BED), and the comparator is the higher of the listed value and DeepVariant 1.10 RNASEQ rerun by the skeptic on that region. F1 for the stated variant type must be STRICTLY HIGHER (direction: max) than the best DeepVariant value for that sample and technology on the live pages (for Illumina WGS and WES, the higher of the standard and pangenome-aware rows): by at least 0.005 absolute where that value is below 0.99, otherwise by at least a 10% relative cut in (1 - F1). The other variant type may not fall more than 0.0005 below its best listed F1. The same margins must hold against Clair3 (newest release, matching model; Clair3-RNA for RNA-seq) on the same input; for the hybrid PacBio+Illumina cell, which has no matching Clair3 model, only the DeepVariant comparator applies. The method is released and uses no HG003 or HG005 truth and no chr20-22 truth of any GIAB sample in training or tuning.

## Partial wins

- **p1:** On the chr20 ONT R10.4.1 case study (HG003_R104_sup_merged.80x.chr20.bam, scored with the case-study hap.py command, -l chr20): INDEL F1 of at least 0.907772 (0.897772 plus 0.01) with SNP F1 of at least 0.998531, and INDEL F1 above Clair3 (newest release, matching R10.4.1 model) on the same BAM by at least 0.01.
- **p2:** On the HG005 RNA-seq cell under the genome-wide region of the success criterion: SNP F1 above the comparator by at least 0.005, INDEL F1 no lower than the comparator's, and SNP F1 above Clair3-RNA (newest release) on the same BAM and region.
- **p3:** On the HG003 WES cell (HG003.novaseq.wes_idt.100x.dedup.bam with the script's capture BED): INDEL F1 of at least 0.98828 (0.98328 plus 0.005) with SNP F1 of at least 0.993044, and INDEL F1 above Clair3 (newest release, Illumina model) on the same BAM.

## How a win is checked

Skeptic downloads the cell's input BAM, reference, truth VCF and BED over plain HTTPS from storage.googleapis.com/deepvariant and the GIAB FTP, reruns the claimant's released pipeline (or checks the VCF's provenance against a rerun on chr20), and runs hap.py --engine vcfeval with the same flags as the r1.10 case-study script. The skeptic compares the PASS rows with the live metrics.md, reruns Clair3 on chr20 as a spot check, and greps the training configuration for HG003, HG005 and chr20-22 truth.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/google/deepvariant/r1.10/docs/metrics.md>

## Sources

- <https://raw.githubusercontent.com/google/deepvariant/r1.10/docs/metrics.md>
- <https://raw.githubusercontent.com/google/deepvariant/r1.10/docs/pangenome-aware-metrics.md>
- <https://raw.githubusercontent.com/google/deepvariant/r1.10/docs/deepvariant-ont-r104-simplex-case-study.md>
- <https://raw.githubusercontent.com/google/deepvariant/r1.10/docs/deepvariant-rnaseq-case-study.md>
- <https://raw.githubusercontent.com/google/deepvariant/r1.10/scripts/inference_deepvariant.sh>
- <https://storage.googleapis.com/deepvariant/case-study-outputs/1.10.0/deepvariant_case_study_summaries/happy.summary.md>
- <https://github.com/google/deepvariant/releases>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- ONT indel errors are dominated by homopolymer length calls; a model that reads per-read base qualities and move tables (or that is phasing-aware within homopolymers) attacks exactly the missing 44,146 false negatives.
- Cross-domain import (speech recognition): homopolymer length is a duration-estimation problem, so duration models from speech (explicit length distributions rather than per-frame labels) may beat pileup classification.
- Combine DeepVariant and Clair3 candidates with a learned arbiter trained only on HG002/HG004 non-chr20-22 regions; disagreement sites are where both are weakest.
- For RNA-seq, model allele-specific expression and RNA editing (A-to-I) explicitly: many RNA false positives are editing sites, not DNA variants.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Training or tuning on HG003 truth (or on chr20-22 of any GIAB sample) is leakage; DeepVariant itself excludes them, so a fair comparison must too.
- HG002 is the son of HG003 and HG004 and carries one haplotype of each parent; a pangenome, panel or model input containing HG002 leaks HG003 genotypes. Use HPRC graphs with HG002 removed.
- Use the same BED as the table (for HG003 that is v4.2.1 benchmark_noinconsistent.bed); the plain benchmark BED gives different numbers.
- hap.py with its default xcmp engine and with vcfeval can disagree on complex indels; the table used vcfeval through the case-study script.
- For Illumina WGS the standard row (0.99598 INDEL) is already beaten by DeepVariant's own pangenome-aware mode on the same reads; the comparator is the better of the two rows.
- The sample_sheet.tsv linked from metrics.md returns NoSuchKey; the whole-genome input BAM names are in inference_deepvariant.sh r1.10.
- Re-basecalling raw signal or adding HiFi reads changes the input and is not a win for a single-technology cell.
- The chr20 case-study cells and the whole-genome metrics rows are different cells; never compare a chr20 F1 with a whole-genome F1. The RNA-seq case-study page scores only chr20 (SNP 0.968421 on 287 truth SNPs), not the 11,349-SNP metrics row.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/deepvariant-case-study-accuracy-records.md
```

Already set up? Say `run V3R1T4S on deepvariant-case-study-accuracy-records`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `deepvariant-case-study-accuracy-records`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
