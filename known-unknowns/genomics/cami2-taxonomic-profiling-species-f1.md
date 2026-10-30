# CAMI II taxonomic profiling at species rank: beat ganon2's F1 on the plant-associated samples in the CAMI Benchmarking Portal

🧫 **Genomes** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (21 plant-associated samples of about 5 Gbp each; building an index over the 2019-01-08 NCBI RefSeq snapshot is the heavy step, 64 GB RAM helps) · open as of 2026-10-30

## The problem

Taxonomic profilers estimate which taxa are present and in what relative abundance. CAMI II (Meyer et al., Nature Methods 2022) evaluated profilers with OPAL against gold-standard profiles. The CAMI Benchmarking Portal (Meyer, Robertson et al., NAR 2025) now ranks uploaded profiles, sample-averaged, rank by rank. Genus level on marine is close to saturated (mOTUs 3.1: genus L1 error 0.10); species level is not. The best species-rank presence/absence F1 scores on 2026-10-30 were as follows. Plant-associated: 0.436 (ganon2 2.1.0, completeness 0.512, purity 0.381, L1 norm error 0.803), then sourmash gather 3.3.2 at 0.394 and MetaPhlAn 2.9.21 at 0.387. Strain-madness: 0.610 (ganon2 2.1.0, L1 0.294), then MetaPhlAn 2.9.22 at 0.568. Marine: 0.875 (Sylph 0.8.0), then mOTUs 3.1.0 at 0.869. The gold standards are public, as is the reference snapshot given to participants (NCBI RefSeq, nt, nr and taxonomy of 2019-01-08).

## What counts as a win

A set of CAMI-format profiles for all 21 plant-associated short-read samples, produced by released deterministic code using only references frozen at or before 2019-01-08 (the CAMI II snapshot or an earlier NCBI release; no database containing the CAMI II source genomes), whose sample-averaged species-rank F1, computed by OPAL with the portal's options and the same 'filter out plasmid, circular element, virus' setting as the record row, is STRICTLY GREATER than 0.436 (ganon2 2.1.0, direction: max) and greater than every row of the live table at https://cami-challenge.org/datasets/plant-associated/avg/group_4/taxonomic_profiling/species/ (re-fetched immediately before claiming), with a species L1 norm error no worse than 0.803.

## Partial wins

- **p1:** Strain-madness (100 samples, averaged): species-rank F1 STRICTLY GREATER than 0.610 (ganon2 2.1.0) with species L1 norm error no worse than 0.294, under the same rules.
- **p2:** Marine (10 samples, averaged): species-rank F1 STRICTLY GREATER than 0.875 (Sylph 0.8.0) using only 2019-01-08 references.
- **p3:** Plant-associated: species-rank L1 norm error below 0.169 (sourmash gather 3.3.2, the lowest listed) with F1 of at least 0.394.

## How a win is checked

Skeptic downloads the plant-associated gold-standard profiles (frl.publisso.de/data/frl:6425521/plant_associated/), runs OPAL (github.com/CAMI-challenge/OPAL) on the claimed profiles with the record row's filter option, averages over the 21 samples as the portal does, and checks the reference database build date and contents in the released code. Minutes to evaluate.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cami-challenge.org/datasets/plant-associated/avg/group_4/taxonomic_profiling/species/>

## Sources

- <https://cami-challenge.org/datasets/plant-associated/avg/group_4/taxonomic_profiling/species/>
- <https://cami-challenge.org/datasets/strain-madness/avg/group_30/taxonomic_profiling/species/>
- <https://cami-challenge.org/datasets/marine/avg/group_1/taxonomic_profiling/species/>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12230735/fullTextXML>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9007738/fullTextXML>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Plant-associated purity is the weak side (0.381): most errors are false-positive species, so calibrated abundance thresholds or containment-based filtering may lift F1 without losing completeness.
- Combine a k-mer containment profiler (sylph/sourmash style) with a marker-gene profiler and keep only species that both support.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Newer databases (GTDB, RefSeq after 2019) can contain the CAMI II source genomes, which were deposited after the challenge; some portal rows may use them, but a claim here must not.
- Rows differ in the 'Filter out' option; match the record row's setting.
- Do not filter the rarest taxa to inflate purity unless the same filter percentage is reported and the record is compared with that filter.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/cami2-taxonomic-profiling-species-f1.md
```

Already set up? Say `run V3R1T4S on cami2-taxonomic-profiling-species-f1`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cami2-taxonomic-profiling-species-f1`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
