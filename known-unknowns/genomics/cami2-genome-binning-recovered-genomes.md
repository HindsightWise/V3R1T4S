# CAMI II genome binning: recover more near-complete genomes from the gold-standard co-assembly than any binner on the CAMI Benchmarking Portal (marine, strain-madness, plant-associated)

🧫 **Genomes** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-days (pooled gold-standard assemblies of a few Gbp plus 10, 100 or 21 short-read samples of about 5 Gbp each to map for coverage; 32-64 GB RAM advisable, GPU optional) · open as of 2026-10-30

## The problem

Genome binning groups assembled contigs into per-genome bins. The second CAMI challenge (Fernando Meyer, Alice McHardy, Alexander Sczyrba and about 100 co-authors, Nature Methods 2022) released three simulated metagenomes with full gold standards: marine (10 samples, 976 bins in the binning gold standard), strain-madness (100 samples, 408 bins, many strains above 95% ANI) and plant-associated (21 samples, 831 bins). The CAMI Benchmarking Portal (Meyer, Robertson et al., NAR 2025) scores every public upload with AMBER against the gold standard and keeps a live table. On 2026-10-30, the best counts for binning the pooled short-read gold-standard assembly (GSA) at >90% completeness and <5% contamination were as follows. Marine: 351 (CompleteBin 1.1.0.2; 354 at <10%), then COMEBin 1.0.4 base (316), COMEBin 1.0.3 (313), COMEBERT-2 and COMEBERT-S (307 each), SemiBin 2.1.0 and Vamb fa045c0 (264) and UltraBinner (261). Strain-madness: 77 (CONCOCT 0.4.1; 82 at <10%). Plant-associated: 118 (VAMB 3.0.1; 119 at <10%). The COMEBin paper (Wang et al., Nat Commun 2024) reports 337 near-complete marine GSA bins under its own settings. The Briefings in Bioinformatics 2025 benchmark by Yazhini, Morice, Jochheim, Lieser and Söding finds SemiBin2 and COMEBin best overall. All three datasets remain far from their gold standards, strain-madness most of all.

## What counts as a win

A genome binning (CAMI binning format) of the pooled short-read gold-standard assembly of the CAMI II marine dataset, produced by released deterministic code with the seed stated, that AMBER (the version the portal uses, with the portal's default options and no filter or exclusion that the record row does not use) scores at STRICTLY MORE than 351 genomes recovered with >90% completeness and <5% contamination (direction: max). It must also beat the largest such count for the same assembly in the live portal table at https://cami-challenge.org/datasets/marine/marmgCAMI2_short_read_pooled_gold_standard_assembly/genome_binning/ (re-fetched immediately before claiming) and in any paper found by a novelty search that uses the same AMBER definition. No reference database, marker set or pretrained model may contain the CAMI II source genomes; anything taxonomy-based must use references frozen at or before 2019-01-08, the CAMI II cutoff.

## Partial wins

- **p1:** Strain-madness pooled GSA: STRICTLY MORE than 77 genomes at >90% completeness and <5% contamination by AMBER, beating the live portal maximum for that assembly, under the same rules.
- **p2:** Plant-associated pooled short-read GSA: STRICTLY MORE than 118 genomes at >90% completeness and <5% contamination by AMBER, beating the live portal maximum for that assembly, under the same rules.
- **p3:** Marine pooled GSA: one binning with adjusted Rand index (bp) STRICTLY GREATER than 0.887 and at least 300 genomes at >90% completeness and <5% contamination. No portal row on 2026-10-30 has both: the rows with 300 or more such genomes have ARI (bp) of at most 0.854 (CompleteBin 1.1.0.2; COMEBin 1.0.3 has 0.841), and the rows at or above 0.887 (MetaWRAP 1.3.2 at 0.990, SemiBin 2.1.0 at 0.887) recover at most 264.
- **p4:** Reproduce a portal row from scratch (for example COMEBin 1.0.3 at 313, or CompleteBin 1.1.0.2 at 351 genomes at <5% contamination) within 2% using released commands, confirming that the record is reproducible.

## How a win is checked

Skeptic downloads the CAMI II GSA and the genome-binning gold-standard mapping (frl.publisso.de/data/frl:6425521), runs AMBER (github.com/CAMI-challenge/AMBER) on the claimed binning file with the same options as the record row, reads the ' > 90% completeness, <5% contamination' count, and compares it with the live portal table. Optionally reruns the released binner to check that it reproduces the file. Minutes to evaluate, hours to rerun.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cami-challenge.org/datasets/marine/marmgCAMI2_short_read_pooled_gold_standard_assembly/genome_binning/>

## Sources

- <https://cami-challenge.org/datasets/marine/marmgCAMI2_short_read_pooled_gold_standard_assembly/genome_binning/>
- <https://cami-challenge.org/datasets/strain-madness/strmgCAMI2_short_read_pooled_gold_standard_assembly/genome_binning/>
- <https://cami-challenge.org/datasets/plant-associated/rhimgCAMI2_short_read_pooled_gold_standard_assembly/genome_binning/>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12230735/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9007738/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10794208/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12636519/fullTextXML>
- <https://frl.publisso.de/data/frl:6425521/marine/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ensemble refinement: the Nat Commun 2026 binning benchmark (PMC13079874) reports more than 30% more high-quality genomes from refining the top three binners' outputs together; no such ensemble row is on the portal yet.
- Exploit the multi-sample coverage (10 marine samples) with per-sample embedding splits, which the Briefings 2025 benchmark found helps.
- Strain-madness: cluster on coverage alone first (the COMEBin paper's no-k-mer variant beat full COMEBin there), then split strains by variant-aware coverage.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The portal shows separate <10% and <5% contamination columns. The headline here is <5%, so compare like with like.
- Pooled GSA, per-sample GSA and MEGAHIT assemblies are different tables. A count on one is not a record on another.
- The 'Filter out circular element' option changes completeness but barely moves the recovered-genome counts (CompleteBin shows 351 either way). State the option you use and match the record row.
- Most CAMI II genomes were newly sequenced for the challenge, but they have since become public. Newer GTDB/RefSeq releases and models pretrained on large genome sets can therefore leak the answer.
- Paper-reported counts (for example COMEBin's 337) come from different AMBER settings and are not directly comparable with portal rows.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/cami2-genome-binning-recovered-genomes.md
```

Already set up? Say `run V3R1T4S on cami2-genome-binning-recovered-genomes`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cami2-genome-binning-recovered-genomes`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
