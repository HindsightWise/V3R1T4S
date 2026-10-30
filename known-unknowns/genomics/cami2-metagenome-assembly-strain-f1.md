# CAMI II metagenome assembly: beat MetaHipMer 2.2.0's strain F1 on the marine short-read co-assembly in the CAMI Benchmarking Portal

🧫 **Genomes** · standard · tractability ★★☆☆☆ · compute: needs cluster (co-assembling 10 marine samples of about 5 Gbp short reads each needs roughly 100-500 GB RAM; MetaQUAST against 977 reference genomes takes hours) · open as of 2026-10-30

## The problem

CAMI II (Meyer et al., Nature Methods 2022) released the reads and source genomes of its simulated marine metagenome. The CAMI Benchmarking Portal (Meyer, Robertson et al., NAR 2025) evaluates assemblies with MetaQUAST. It ranks them on strain recall (the fraction of genomes assembled at >=90% completeness and <=5 mismatches per 100 kb), strain precision, their F1, auNGA, IDY and genome fraction. On 2026-10-30 the live table for the marine Illumina pooled co-assembly was led by MetaHipMer 2.2.0, with strain F1 29.27% (recall 17.21%, precision 97.67%, genome fraction 38.49%). Next by F1 were HipMer 1.0 (20.59%), metaSPAdes 4.0.0 (17.09%), Ray Meta 2.3.1 (16.71%), MEGAHIT 1.2.7 (15.06%) and GATB 1.0 (13.54%). The gold-standard assembly reaches 63.32% strain recall and 76.98% genome fraction. On plant-associated short reads, MetaHipMer 2.0.0 leads with strain F1 13.21%. Strain-madness remains the hardest: the best strain recall is 3.92% (HipMer 1.0), against 90.2% for the gold standard. Assembling closely related strains from short reads is the open core of the problem.

## What counts as a win

A co-assembly (FASTA) of the 10 CAMI II marine short-read samples, produced by released code from the reads alone (no reference genomes, no CAMI gold-standard contigs, no long reads). Its F1 strain score must be STRICTLY GREATER than 29.27% (MetaHipMer 2.2.0; direction: max) and greater than every row in the live table at https://cami-challenge.org/datasets/marine/marmgCAMI2_short_read_pooled_assembly/assembly/, re-fetched immediately before claiming. The score is computed with the portal's MetaQUAST settings (min identity 95%, the record row's options) against the same marine reference sequence set the portal uses. The assembly must also have IDY of at least 99.0%.

## Partial wins

- **p1:** Plant-associated short-read pooled co-assembly: F1 strain score STRICTLY GREATER than 13.21% (MetaHipMer 2.0.0) under the same rules and the portal's evaluation.
- **p2:** Strain-madness short-read pooled co-assembly: strain recall STRICTLY GREATER than 3.92% (HipMer 1.0) with strain precision of at least 90%.
- **p3:** Plant-associated Oxford Nanopore pooled assembly from the ONT reads alone: strain recall STRICTLY GREATER than 3.02% (metaFlye 2.8) with strain precision of at least 77.14%.
- **p4:** Marine short-read pooled co-assembly: genome fraction above 46.58% (A-STAR, the table's highest) with strain precision of at least 90%.

## How a win is checked

Skeptic reruns the released assembler on the public reads (or takes the released FASTA plus its command log), runs MetaQUAST with the portal's options against the marine genome set from frl.publisso.de/data/frl:6425521, computes strain recall and precision as the NAR 2025 portal paper defines them, and compares with the live table. Hours of compute.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cami-challenge.org/datasets/marine/marmgCAMI2_short_read_pooled_assembly/assembly/>

## Sources

- <https://cami-challenge.org/datasets/marine/marmgCAMI2_short_read_pooled_assembly/assembly/>
- <https://cami-challenge.org/datasets/plant-associated/rhimgCAMI2_short_read_pooled_assembly/assembly/>
- <https://cami-challenge.org/datasets/strain-madness/strmgCAMI2_short_read_pooled_assembly/assembly/>
- <https://cami-challenge.org/datasets/plant-associated/rhimgCAMI2_long_read_ont_pooled_assembly/assembly/>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12230735/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9007738/fullTextXML>
- <https://frl.publisso.de/data/frl:6425521/marine/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Strain recall needs genomes assembled at >=90% completeness with <=5 mismatches per 100 kb, so polishing and strain-aware graph resolution may pay more than raw contiguity.
- Start from MetaHipMer 2.2.0's iterative k-mer scheme and add coverage-aware bubble resolution across the 10 samples.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not mix the hybrid, long-read and short-read tables: they are separate assemblies with separate records.
- The F1 strain score is missing ('-') for strain-madness rows on the portal, so p2 uses recall and precision explicitly.
- The marine long-read pooled table has no tool submissions, only the gold standard, so a first entry there is not a record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/cami2-metagenome-assembly-strain-f1.md
```

Already set up? Say `run V3R1T4S on cami2-metagenome-assembly-strain-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cami2-metagenome-assembly-strain-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
