# precisionFDA Truth Challenge V2 (finished, answers released): beat the best submission's F1 in difficult-to-map regions or the MHC for HG003/HG004 from the challenge reads

🧫 **Genomes** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days per sample for the Illumina 35x cells (alignment plus calling); needs cluster for the 85x ONT and the multi-technology cells · open as of 2026-10-30

## The problem

The precisionFDA Truth Challenge V2 (May-June 2020; Olson, Wagner, McDaniel, Zook and colleagues at NIST GIAB with the precisionFDA team, Cell Genomics 2022) gave participants about 35x Illumina NovaSeq, 35x PacBio HiFi (Sequel II) and about 85x ONT R9.4.1 (Guppy 3.6) FASTQs for the then semi-blinded parents HG003 and HG004, with HG002 as the unblinded training sample. Winners were chosen on F1 in all benchmark regions, in difficult-to-map regions (low mappability plus segmental duplications, v2.0 stratifications) and in the MHC. The challenge is over: NIST record mds2-2336 holds the FASTQs, all 64 submitted callsets (192 VCFs, one each for HG002, HG003 and HG004) and their hap.py results, and the v4.2.1 truth for both parents is on the GIAB FTP. Winning F1 values (challenge_winners.tsv): difficult-to-map, Illumina 0.9693 (DRAGEN), PacBio 0.9929 (Sentieon), ONT 0.9825 (PEPPER-DeepVariant), multi-technology 0.9944 (Roche); MHC, Illumina 0.9923 (Seven Bridges GRAF), PacBio 0.9949 (Sentieon), ONT 0.9717 (NanoCaller/Clair/Medaka ensemble), multi-technology 0.9979 (Sentieon). The all-regions Illumina cell (0.9971) is already passed on the same HG003 reads by pangenome-aware DeepVariant 1.10 (SNP 0.998139, INDEL 0.996976), so only the difficult-to-map and MHC cells are offered here, each checked against current tools.

## What counts as a win

For one technology (ILLUMINA, PACBIO, ONT or MULTI) and one stratum (difficult-to-map = v2.0 union/GRCh38_alllowmapandsegdupregions.bed.gz, or MHC = v2.0 OtherDifficult/GRCh38_MHC.bed.gz): VCFs for HG003 and HG004 made only from that technology's challenge FASTQs in mds2-2336, with HG002 data used only as the challenge allowed and no HG003 or HG004 truth in training or tuning. Besides GRCh38, public graphs, panels or haplotype catalogues may be used only if they contain no sequence or genotypes from HG002, HG003 or HG004 (for example an HPRC graph with HG002 removed). The skeptic scores them with hap.py --engine=vcfeval against each parent's v4.2.1 benchmark (HG00x_GRCh38_1_22_v4.2.1_benchmark.vcf.gz with its benchmark_noinconsistent.bed) restricted to the stratum and takes the harmonic mean of the two parents' combined SNV+INDEL F1. The result must be STRICTLY HIGHER (direction: max), by at least a 10% relative cut in (1 - F1), than (a) the best 2020 submission in that technology category, every one rescored by the skeptic with the identical pipeline, and (b) on HG003 alone, a current caller run on the same HG003 reads with its official preset: DeepVariant 1.10 (the better of WGS and WGS_PANGENOME) for Illumina, PACBIO for PacBio, HYBRID_PACBIO_ILLUMINA for MULTI, and Clair3 (newest release, r941_prom_hac_g360+g422 model) for ONT R9.4.1, for which DeepVariant has no preset. The method is released.

## Partial wins

- **p1:** MHC, Illumina only: harmonic-mean parental F1 above the best Illumina submission rescored under the identical pipeline (the GRAF winner was listed at 0.9923), by a 10% relative cut in (1 - F1), with no HG003 or HG004 truth used.
- **p2:** MHC, ONT R9.4.1 only: harmonic-mean parental F1 above the best ONT submission rescored under the identical pipeline (the winning ensemble was listed at 0.9717), by at least 0.005, with no HG003 or HG004 truth used.
- **p3:** A published, reproducible rescoring of every 2020 submission in the eight difficult-to-map and MHC cells with hap.py vcfeval, v4.2.1 and the v2.0 stratifications, giving each cell's best rescored value and any change from challenge_winners.tsv, which fixes comparator (a) for this target.

## How a win is checked

Skeptic downloads the claimant's VCFs, the winner's VCFs from mds2-2336 (data.nist.gov, plain HTTPS), the v4.2.1 truth and the v2.0 stratification BEDs, runs hap.py with vcfeval on both, aggregates per the challenge README, and for (b) runs the newest DeepVariant on the HG003 reads or a stated chromosome subset. Hours on a workstation for scoring; the DeepVariant rerun needs a cloud VM.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://raw.githubusercontent.com/usnistgov/giab-pFDA-2nd-challenge/master/data/challenge_winners.tsv>

## Sources

- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9205427/fullTextXML>
- <https://raw.githubusercontent.com/usnistgov/giab-pFDA-2nd-challenge/master/data/challenge_winners.tsv>
- <https://raw.githubusercontent.com/usnistgov/giab-pFDA-2nd-challenge/master/data/anonymized_challenge_results_v5.txt>
- <https://data.nist.gov/od/id/mds2-2336>
- <https://precision.fda.gov/challenges/10>
- <https://raw.githubusercontent.com/google/deepvariant/r1.10/docs/pangenome-aware-metrics.md>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The MHC is about 4 Mb of extreme polymorphism: local diploid assembly of reads recruited to the MHC, followed by assembly-to-reference calling, sidesteps reference bias in a way read-pileup callers cannot.
- Cross-domain import (population genetics): HLA haplotypes are well catalogued, so a graph built from public HLA/MHC haplotypes (IPD-IMGT/HLA, HPRC assemblies with HG002 removed) gives short reads somewhere to map; first confirm that no HG002, HG003 or HG004 haplotype is in the catalogue.
- In segmental duplications, paralog-specific variants decide mappability; modelling copy number per duplicated block before calling turns false positives into informative sites.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The data README describes the results table as a geometric mean of the parents' F1, the paper's main text as a harmonic mean (its Methods equation uses the geometric mean); the criterion fixes the harmonic mean and compares rescored VCFs, never printed numbers.
- Under rescoring the best submission in a cell may not be the 2020 winner; comparator (a) is the best rescored submission.
- Current DeepVariant and Clair3 models train on HG004 (only HG003 is excluded), so they cannot be components of a claim, and comparator (b) is taken on HG003 only.
- The all-regions cells are not offered: on the Illumina reads they are already passed by public tools.
- Using HiFi or ONT reads for an Illumina-only cell, or any other HG003/HG004 data, breaks the single-technology rule.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/precisionfda-truth-challenge-v2-difficult-mhc.md
```

Already set up? Say `run V3R1T4S on precisionfda-truth-challenge-v2-difficult-mhc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `precisionfda-truth-challenge-v2-difficult-mhc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
