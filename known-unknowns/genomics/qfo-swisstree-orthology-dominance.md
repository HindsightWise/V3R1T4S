# Quest for Orthologs 2022 SwissTree benchmark: ortholog predictions that beat every public method on recall and precision at once

🧫 **Genomes** · standard · tractability ★★☆☆☆ · compute: laptop-days (orthology inference on the 78 QfO 2022_02 reference proteomes; the QfO benchmark pipeline runs in Docker/Nextflow) · open as of 2026-10-30

## The problem

The Quest for Orthologs benchmark service (Nevers, Jones, Jyothi et al., NAR 2022; maintained by the Dessimoz lab with OpenEBench) scores ortholog predictions on fixed reference proteomes. It checks them against curated gene phylogenies, species-tree discordance and function conservation. SwissTree is an expert-curated set of reference gene trees. On it, the public 2022 results list 20 methods by true positive rate (recall) and positive predictive value (precision) of ortholog pairs. On 2026-10-30 the highest recall was pbDOOD (midpoint) at TPR 0.854 / PPV 0.950, then pbDOOD (eggnog v7) 0.847 / 0.952, OrthoFinder 0.825 / 0.917 and PANTHER v18 (all) 0.811 / 0.943. The highest precision was FastOMA v0.1.4 at PPV 0.953 (TPR 0.699). No listed method has both. OrthoFinder v3 (Emms, Liu, Belcher, Holmes and Kelly, Nature Methods 2026) reports the highest SwissTree recall among the methods it plots, which leave out pbDOOD. Its points (Fig. 5e: OrthoFinder3 about 0.83 / 0.93, OrthoFinder3_Linear about 0.845 / 0.92) lie below pbDOOD's recall and FastOMA's precision. On TreeFam-A the maxima are TPR 0.7367 (OrthoFinder) and PPV 0.9566 (PANTHER v18 LDO).

## What counts as a win

Ortholog pair predictions on the QfO 2022_02 reference proteomes, produced by released deterministic code that does not use SwissTree, TreeFam-A or any curated reference tree as input, whose SwissTree evaluation by the official QfO benchmark pipeline (2022 release) gives TPR STRICTLY GREATER than 0.854 AND PPV STRICTLY GREATER than 0.953 (direction: max on both), exceeding every method on the public results page https://orthology.benchmarkservice.org/proxy/results/2022/ (re-fetched immediately before claiming) on both axes, and not dominated on SwissTree by either OrthoFinder v3 point published in Emms et al. 2026, Fig. 5e (OrthoFinder3 about 0.83 / 0.93, OrthoFinder3_Linear about 0.845 / 0.92; the paper's Supplementary Data hold no QfO values).

## Partial wins

- **p1:** TreeFam-A (2022): TPR STRICTLY GREATER than 0.7367 together with PPV of at least 0.9300, beating every listed method's recall while keeping precision at Hieranoid 2's level.
- **p2:** SwissTree (2022): TPR STRICTLY GREATER than 0.854 with PPV of at least 0.950, strictly dominating pbDOOD (midpoint), and not dominated by OrthoFinder v3's published point.
- **p3:** Species tree discordance, Eukaryota (2022): more than 16,000 completed tree samplings with average Robinson-Foulds distance below 0.0400. That exceeds both the public page maximum (MetaPhOrs v2.5, 14,689 at RF 0.0735) and OrthoFinder3_Linear's published point (about 15,700 at RF about 0.064, Emms et al. 2026 Fig. 5a).

## How a win is checked

Skeptic runs the QfO benchmark pipeline (github.com/qfo/benchmark-webservice, Docker plus Nextflow, with the 2022 reference data) on the released ortholog file, reads the SwissTree TPR and PPV, and compares with the public 2022 table and the OrthoFinder v3 figure. Uploading to OpenEBench is a human-only action and optional. Hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://orthology.benchmarkservice.org/proxy/results/2022/>

## Sources

- <https://orthology.benchmarkservice.org/proxy/results/2022/>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9252809/fullTextXML>
- <https://github.com/qfo/benchmark-webservice>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13346109/fullTextXML>
- <https://ftp.ebi.ac.uk/pub/databases/reference_proteomes/previous_releases/qfo_release-2022_02_with_updated_UP000000437/QfO_release_2022_02_with_updated_UP000000437.tar.gz>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The high-recall methods (pbDOOD, OrthoFinder) are tree-based and lose precision through spurious pairs in deep paralog families; a precision filter that rejects pairs unsupported by both a gene tree and a graph-based method might keep the recall.
- Reconcile gene trees against the species tree with explicit loss modelling before calling pairs.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- SwissTree is small (error bars about +-0.03), so a claim near the bounds is within noise; report the interval.
- The 2020_04 and 2022_02 proteome sets have separate results pages; do not mix them.
- The benchmark-webservice README still describes older reference years. Use the 2022 reference data (fetch_reference_data.py maps '2022' to release 2022.1, which matches the updated-UP000000437 proteome set) and state the pipeline version.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/genomics/qfo-swisstree-orthology-dominance.md
```

Already set up? Say `run V3R1T4S on qfo-swisstree-orthology-dominance`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `qfo-swisstree-orthology-dominance`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
