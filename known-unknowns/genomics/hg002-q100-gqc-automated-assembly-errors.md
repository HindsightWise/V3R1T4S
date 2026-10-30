# HG002 vs the Q100 genome benchmark: an automated diploid assembly with fewer GQC errors than the best listed non-curated assembly (38,072)

🧫 **Genomes** · standard · tractability ★★☆☆☆ · compute: needs cluster (a diploid human assembly takes hundreds of CPU-hours and over 100 GB of RAM; GQC takes about 64 GB and 4 hours per assembly) · open as of 2026-10-30

## The problem

The T2T, HPRC and GIAB consortia's HG002 Q100 assembly (marbl/hg002; Hansen, Dwarshuis, Rhie, Koren, Phillippy and colleagues, Cell 2026, doi 10.1016/j.cell.2026.06.016) is a near-perfect diploid genome. Its GQC tool aligns a test assembly to it and counts every substitution and indel discrepancy, along with phase switches, coverage and mononucleotide-run accuracy. The consortium publishes GQC results against hg002v1.1 for many public HG002 assemblies under T2T/HG002/assemblies/benchmarking/analyses/assembly_comparison on the human-pangenomics S3 bucket. The best total outside the curated Q100 lineage (hg002v0.x and v1.x) is verkko_thic_assignedcontigs (v3 exclusion run, Aug 2025): 38,072 errors (6,174 substitutions, 31,898 indels), QV 53 without wrong-haplotype errors, 5,959,494,470 benchmark bases covered (99.3%), 5.51 switches per Mb, NGA50 115.5/115.9 Mb. Next come hifi_q28_trio_hic and verkko_asm_thic at 41,207, the HPRC release 2 assembly hprc_year2 (= hprc_year2_polished) at 42,963 (QV 53, NGA50 about 71 Mb), v2_trio at 48,276, hprc_year2_v2_thic at 51,089 and lc24_medaka_6b4 at 52,842. Every assembly run under both the v3 and the v4 (Feb 2026) exclusion configs has the same total in both. For scale, the curated hg002v1.0.1 has 3,370 errors, so automated pipelines still make about 11 times more. A v1.2 benchmark was released in August 2026, but every listed run is against v1.1. Inputs (HiFi, ONT ultra-long, Hi-C, trio short reads) are public on S3, and the score is a mechanical count.

## What counts as a win

A diploid HG002 assembly FASTA produced end to end by a released, deterministic pipeline (no manual edits) from public HG002 read data, and optionally public parental reads. It may not use the Q100 assemblies, their patches, the HG002-issues lists, any assembly in the GQC tables, or any reference genome as input. GQC (commit 1fe404c, as in the February 2026 runs, or newer) is run with the hg002v1.1 resources tarball and the v4 exclusion BED (or v3 for a like-for-like check). Total errors must be STRICTLY FEWER (direction: min) than the smallest non-Q100-lineage total in the live assembly_comparison tables (38,072 as of 2026-10-30) by at least 5%, that is at most 36,168. Total v1.1 bases covered must be at least 5,959,494,470, and the switch rate at most 5.5079 per Mb.

## Partial wins

- **p1:** An assembly from ONT reads only (no HiFi, Illumina, Element or Hi-C) with fewer total GQC errors than 52,842 (lc24_medaka_6b4's total), with at least 5,964,776,254 v1.1 bases covered.
- **p2:** Polishing: starting from the public HPRC release 2 HG002 assembly (hprc_year2, 42,963 errors), a released polisher using only public reads cuts its total GQC errors by at least 30% (to at most 30,074) without lowering bases covered or raising the switch rate.
- **p3:** Mononucleotide-run accuracy (runs of 10 bp or longer) above the best non-curated listed value (99.308%, hprc_year2_v2_thic) by at least 0.1 percentage point, with at least 5,953,357,669 v1.1 bases covered.

## How a win is checked

Skeptic checks the pipeline's inputs (read accessions only, with no Q100 or assembly files), reruns it or a chromosome-level subset if needed, runs GQC assemblybench against hg002v1.1 with the resources tarball and the exclusion config of the compared run set, and compares the generalstats totals with the live S3 tables. About 4 hours and 64 GB per GQC run.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://s3-us-west-2.amazonaws.com/human-pangenomics/index.html?prefix=T2T/HG002/assemblies/benchmarking/analyses/assembly_comparison/>

## Sources

- <https://raw.githubusercontent.com/marbl/hg002/main/README.md>
- <https://raw.githubusercontent.com/marbl/GQC/main/README.md>
- <https://s3-us-west-2.amazonaws.com/human-pangenomics/index.html?prefix=T2T/HG002/assemblies/benchmarking/analyses/assembly_comparison/>
- <https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/HG002/assemblies/benchmarking/analyses/assembly_comparison/verkko_thic_assignedcontigs/gqc_081625_v3excluded/verkko_thic_assignedcontigs/verkko_thic_assignedcontigs.generalstats.txt>
- <https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/HG002/assemblies/benchmarking/analyses/assembly_comparison/hprc_year2_polished/gqc_021126/README.txt>
- <https://doi.org/10.1016/j.cell.2026.06.016>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- In hprc_year2 errors split roughly evenly between substitutions and indels and about a quarter match the other haplotype, so better haplotype assignment in low-heterozygosity stretches is worth as much as better consensus; in the Verkko assemblies indels dominate.
- Polishing with a k-mer database built from accurate short reads (Element or Illumina) is how the Q100 lineage got from QV 53 to the 70s, and it can be automated.
- Cross-domain import (error-correcting codes): treat the HiFi, ONT and short-read layers as independent noisy channels and decode the consensus jointly, rather than polishing in sequence.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The hg002v0.x and v1.x entries are the curated benchmark lineage and are excluded from the comparison.
- Use the exclusion BED of a listed run set; adding further exclusions (as the hprc_year2_polished_nodiffregions run does, 2,108 errors) is not comparable.
- Listed runs use the v1.1 benchmark; a GQC run against the newer v1.2 resources (the GQC README default since August 2026) is not comparable with them.
- Anything derived from the Q100 effort (patch VCFs, HG002-issues, reads aligned to Q100 and used to filter) is leakage, even when used only for filtering.
- GQC QV and coverage percentages are rounded; the criterion uses total error counts and covered-base counts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/hg002-q100-gqc-automated-assembly-errors.md
```

Already set up? Say `run V3R1T4S on hg002-q100-gqc-automated-assembly-errors`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hg002-q100-gqc-automated-assembly-errors`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
