# Automated cryo-EM model building: raise completeness above ModelAngelo's 77% on its 177-map held-out set

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: needs cluster (GPU; 177 maps, hundreds of GB of EMDB downloads) · open as of 2026-10-30

## The problem

ModelAngelo (Kiarash Jamali, Lukas Käll, Rui Zhang, Alan Brown, Dari Kimanius and Sjors Scheres; Nature 628:450-457, 2024, open access as PMC11006616) set the current bar for automated model building into cryo-EM maps. Its held-out test set is 177 protein-containing structures at 4 A resolution or better, released between the 1 April 2022 training cut-off and 9 February 2023. Structures above 30,000 residues and icosahedral viruses were excluded, as were structures with a chain above 10 percent identity to a training chain. The EMDB/PDB list is published as Supplementary Information, and ModelAngelo's built models are on Figshare (10.6084/m9.figshare.25218434). After one standard Servalcat refinement cycle, ModelAngelo built 77 percent of the 410,585 residues, or 85 percent after excluding the 51,446 residues whose deposited Q-score is below 0.4. Completeness here means the fraction of deposited residues whose Ca lies within 3 A of the built model with the correct amino acid. On a 27-structure subset, DeepTracer, the best alternative, reaches about 80 percent only at 2.5-3 A local resolution, against ModelAngelo's roughly 80 percent at 3.5-4 A; Phenix, Buccaneer and Demo-EM are considerably lower. Nucleic acids are much weaker: on ribosomes at 1.98-3.80 A, completeness with correct base identity falls from about 80 percent in the best regions to roughly 20 percent in the worst, and the paper gives no aggregate figure. Maps and depositions are public in EMDB and the PDB. Later preprints claim improvements: CryFold (B. Su, K. Huang, Z. Peng, A. Amunts and J. Yang; bioRxiv 10.1101/2024.11.13.623164, several versions) benchmarks on the same 177 maps and reports more complete models than ModelAngelo. EM3DFold (bioRxiv 10.64898/2026.09.16.752067) and CryoZeta (2026) use other benchmark sets. Any of these may already move the bar, so the novelty check must settle their figures on this list before any claim.

## What counts as a win

An automated pipeline that, given only the released map and the sequences of the chains present, builds models for every entry of the 177-structure test list in the ModelAngelo supplementary information. The skeptic computes completeness with a published script implementing the paper's definition: the fraction of all deposited protein residues whose Ca lies within 3 A of the built model with the correct residue identity, pooled over residues, with failed entries counted as zero. That completeness must be STRICTLY HIGHER (direction: max) by at least 2 percentage points than the published value: 77 percent over all 410,585 residues, or 85 percent on the Q-score >= 0.4 subset (Nature 628:450-457, re-fetched live immediately before claiming). It must also be higher than any later published value on the same list and definition found by the novelty check, including CryFold's. The run must have no human intervention per map (one fixed configuration for the whole list, published) and must not use the deposited coordinates of a test entry at any stage. Declared training data must exclude every test entry and every chain above 10 percent sequence identity to a test chain. Built models, configs, the per-entry completeness table and runtimes must be published.

## Partial wins

- **p1:** On the 177-structure list, completeness strictly above 77 percent by at least 2 points on the full residue count, or strictly above 85 percent by at least 2 points on the Q-score >= 0.4 subset, with both numbers reported.
- **p2:** On a list of at least 10 EMDB ribosome maps at 1.9-4.0 A released after 1 April 2022 (ModelAngelo's training cut-off), declared and published before any building, nucleotide completeness with correct base identity must be strictly higher by at least 5 percentage points than the attacker's own re-run of the released ModelAngelo weights on the same maps under one fixed configuration. Completeness is computed over all deposited nucleotides as the fraction whose P atom lies within 3 A of a built nucleotide with the correct base, as in the paper's Extended Data Table 2. Both per-map tables and both sets of built models must be published.
- **p3:** A reproduction artefact: reproducing ModelAngelo's published completeness within 2 points on at least 30 entries of the test list with the released weights, publishing the end-to-end harness (map download, build, refinement, score) and the per-entry table.

## How a win is checked

Skeptic takes the test list from the paper's supplementary information, downloads the maps from EMDB and the deposited models from the PDB, runs a published completeness script on the attacker's built models (Ca/C1' within 3 A plus identity match), checks every entry of the list is covered with failures counted as zero completeness, verifies one fixed configuration was used for all entries and that no deposited coordinates of a test entry were inputs, and audits declared training data against the test list with a 10 percent identity search. Days of download and compute; the model building is the attacker's cost.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11006616/fullTextXML>

## Sources

- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11006616/fullTextXML>
- <https://europepmc.org/articles/PMC11006616>
- <https://github.com/3dem/model-angelo>
- <https://doi.org/10.6084/m9.figshare.25218434>
- <https://doi.org/10.1101/2024.11.13.623164>
- <https://github.com/SBQ-1999/CryFold>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The residues ModelAngelo misses concentrate at low local resolution and low Q-score; an explicit local-resolution-aware decision rule (build, or build backbone-only, or abstain) targets the reported 51,446 low-Q residues.
- Nucleic acids are the open flank: base identity is where completeness collapses, and a dedicated base-type classifier conditioned on sugar-phosphate geometry is a narrow, checkable improvement.
- Cross-domain import (sequence alignment): treat built fragments as noisy reads and assign them to sequences with a profile HMM over fragment-derived residue posteriors, the trick that makes identification work, then re-thread using the assignment.
- Iterate build-refine-rebuild with an open refinement program rather than one forward pass; refinement improves local map agreement and lets a second pass extend chains.
- Report completeness per local-resolution bin, since a gain limited to the best bins is not a gain on the headline number.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The deposited models are public, so pipelines that read them (even for masking, chain assignment or stopping) are leaking; the per-entry audit must show map and sequence inputs only.
- Per-map manual intervention is not an automated result: one fixed configuration must run the whole list, which is also what makes the comparison fair.
- Completeness definitions differ (Ca within 3 A with or without identity, residue vs atom counts, per-map mean vs pooled residues); the paper's definition and the exact test list must be used, with the script published.
- ModelAngelo's 77 percent is after one Servalcat refinement cycle; compare refined with refined, or report both.
- CryFold's figures on the same 177 maps could not be read on 2026-10-30 (bioRxiv rate-limit block); a claim that has not settled CryFold's number on this list and definition is not a claim.
- The paper's alternative-tool numbers come from Extended Data tables that are images in the full text, so the published comparison values must be read from the article's tables or supplementary files before any head-to-head claim.
- Averaging over entries instead of over residues changes the number; the published 77 percent is over all 410,585 residues.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/cryoem-automated-model-building-completeness.md
```

Already set up? Say `run V3R1T4S on cryoem-automated-model-building-completeness`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cryoem-automated-model-building-completeness`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
