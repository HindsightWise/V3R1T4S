# HG002 nanopore read correction scored against the Q100 genome: corrected ONT reads with fewer errors per megabase than HERRO's 88 (GQC readbench)

🧫 **Genomes** · standard · tractability ★★☆☆☆ · compute: needs cluster or a GPU workstation for the full about 115 Gb read set; laptop-days for a single-chromosome partial · open as of 2026-10-30

## The problem

Correcting ONT reads before assembly is what made ONT-based telomere-to-telomere assembly practical. The HERRO corrector (Dominik Stanojević, Mile Šikić and colleagues) is the reference method used with Verkko and hifiasm. The Q100 team (Nancy Hansen and colleagues; Hansen et al., Cell 2026, supplementary Table S14) aligns read sets to the diploid HG002 benchmark and counts every discrepancy with GQC readbench, publishing the results under T2T/HG002/assemblies/benchmarking/analyses/read_evaluation on the human-pangenomics S3 bucket. Current values (gqc_sep2025 runs): ONT Q28 HERRO-corrected reads, 10,193,695 errors in 115,022,133,633 aligned bases, or 88.62 errors per Mb (3 substitutions and 84 indels per Mb, 277,178,935 clipped bases). Its BAM header shows the input was HG002.experimentalUL.corrected.fasta.gz, aligned with Winnowmap 2.03 (--MD -W repetitive_k15.txt -ax map-pb -I12g -y) and filtered with samtools view -F0x104. The HERRO README publishes that file (Zenodo record 13252378) as HERRO-corrected reads of ONT's experimental high-accuracy ultra-long GM24385 release (EPI2ME gm24385_ncm23_preview, s3://ont-open-data/gm24385_2023.12/, 125 Gbp at Q10 or more, read N50 91 kbp), so the raw input is public. Uncorrected ONT Epi2Me Q28 reads have 3,055 per Mb, ONT R10 ultra-long Dorado v0.3.4 reads 26,113 per Mb, PacBio Revio SPRQ HiFi 1,060 per Mb and the best short reads (Onso) 470 per Mb. Corrected reads already beat HiFi, but nearly all remaining errors are indels, mostly in homopolymers and short tandem repeats. Raw ONT reads and the scored BAMs are public, so a better corrector shows up as a mechanical error count when compared with HERRO on the same input.

## What counts as a win

A corrected read set derived only from public HG002 ONT reads, with the source accessions stated. Correction may not use HiFi, Illumina, Element or Onso reads, any assembly, or any reference genome. The reads are aligned to the hg002v1.1 diploid benchmark with Winnowmap 2.03 using the listed run's options (--MD -W repetitive_k15.txt -ax map-pb -I12g -y), unmapped and secondary alignments are removed with samtools view -F0x104 (as in the listed BAM), and they are scored with GQC readbench (no downsampling) with the hg002v1.1 resources. Errors per Mb of aligned bases must be STRICTLY LOWER (direction: min), by at least 10% relative, than both (a) the HERRO-corrected row in the live read_evaluation results (88.62 per Mb as of 2026-10-30, so at most 79.76) and (b) HERRO (newest release) run by the skeptic on the same raw input reads, aligned and scored identically. Aligned bases must be at least 115.0 Gb and at least those of (b), and clipped bases no more than 0.25% of aligned bases. The corrector is released.

## Partial wins

- **p1:** Restricted to reads whose primary alignment is to chr20 (either haplotype): errors per Mb at least 10% lower than HERRO run by the skeptic on the same raw input and scored the same way, with aligned bases on chr20 no lower than HERRO's.
- **p2:** Indel errors per Mb at least 15% lower than HERRO's on the same raw input (and below the listed row's 84.96 per Mb), at equal or greater aligned yield, even if substitutions rise, provided total errors per Mb stay at most 88.62.

## How a win is checked

Skeptic confirms that the corrector's inputs are ONT reads only, runs HERRO on the same raw reads (or a stated chromosome subset), aligns both corrected sets to hg002v1.1 with Winnowmap 2.03 -ax map-pb, runs GQC readbench on both with the same resources, and compares errors per Mb, aligned bases and clipped bases with each other and with the live read_evaluation generalstats file. GPU hours for HERRO, then hours to a day per readbench run.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/HG002/assemblies/benchmarking/analyses/read_evaluation/ont/ont_herro_corrected/ont_herro_corrected_gqc_sep2025/ont_herro_corrected.generalstats.txt>

## Sources

- <https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/HG002/assemblies/benchmarking/analyses/read_evaluation/README.txt>
- <https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/HG002/assemblies/benchmarking/analyses/read_evaluation/ont/ont_herro_corrected/ont_herro_corrected_gqc_sep2025/ont_herro_corrected.generalstats.txt>
- <https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/HG002/assemblies/polishing/HG002/v1.1/mapping/ont_HERRO_corrected/hg002v1.1_ont_herro_corrected.pri.bam>
- <https://raw.githubusercontent.com/marbl/GQC/main/README.md>
- <https://raw.githubusercontent.com/marbl/hg002/main/README.md>
- <https://doi.org/10.1016/j.cell.2026.06.016>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Indels are 84 of the 88 errors per Mb, so the target is homopolymer and short-tandem-repeat length; correcting run lengths jointly across overlapping reads from the same haplotype is the direct attack.
- Cross-domain import (speech and duration modelling): estimate homopolymer length as a duration with an explicit length distribution conditioned on context, rather than a per-base vote.
- Use the raw signal or the move tables where they are public: run length is better resolved in signal space than in called bases, and this stays ONT-only.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Dropping hard reads or clipping hard regions lowers the error rate trivially; hence the aligned-yield and clipping constraints.
- Newer or deeper raw ONT data alone lowers the error rate; that is why the claim must also beat HERRO run on the same raw input.
- Correction toward GRCh38, CHM13, HPRC assemblies or the Q100 genome is not ONT-only correction and is forbidden, even indirectly as k-mer filters.
- The Q100 v1.1 benchmark was itself polished using HG002 reads, which may include the ONT data being corrected; report which read set you used.
- Aligner choice changes clipping and error counts; use the listed run's aligner and settings.
- Downsampling in readbench changes counts; the listed rows use full alignments.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/hg002-ont-read-correction-gqc-error-rate.md
```

Already set up? Say `run V3R1T4S on hg002-ont-read-correction-gqc-error-rate`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hg002-ont-read-correction-gqc-error-rate`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
