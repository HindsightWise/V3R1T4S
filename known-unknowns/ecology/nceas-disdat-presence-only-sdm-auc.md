# NCEAS/disdat species distribution benchmark: beat the best published presence-absence AUC for presence-only models in six regions

🐦 **Ecology and bioacoustics** · standard · tractability ★★★☆☆ · compute: laptop-hours (disdat point data a few MB; optional OSF raster grids for spatial-context models) · open as of 2026-10-30

## The problem

The NCEAS benchmark (Elith et al. 2006) was released as the disdat R package and OSF node kwc4v by Elith, Graham, Valavi, Hijmans and the NCEAS working group (Biodiversity Informatics 15:69-80, 2020). It gives presence-only training records and background points for 225 anonymised species (birds, plants, bats, reptiles) in six regions (AWT, CAN, NSW, NZ, SA, SWI), plus independent presence-absence (PA) survey sites for evaluation. The standard score is AUC-ROC per species on the PA sites, averaged within each region and then across the six regions. Table 2 of the DeepMaxent paper (fetched 2026-10-30) collects the published values: Valavi et al. 2022 single-species models up to 0.723 (RF down-sampled, ensemble), Maxent with target-group background (Phillips et al. 2009) 0.760, the Zbinden et al. 2024 multi-species model 0.755. DeepMaxent with target-group background (Ryckewaert, Marcos, Botella, Servajean, Bonnet, Joly; arXiv 2412.19217v4, Jan 2026; Methods in Ecology and Evolution 2026, doi 10.1111/2041-210x.70262) has the best average, 0.768. The best region means in that table are AWT 0.732 (Maxent TGB), CAN 0.732, NSW 0.752, NZ 0.753 and SWI 0.850 (DeepMaxent TGB), and SA 0.815 (Zbinden). Doi, Osawa and Tsutsumida (tabfm-distribution repository, Oct 2026, paper submitted) benchmark TabPFN and TabICL under the Valavi protocol and release per-species result tables. Their best six-region average is 0.736 and their best median over the 217-species subset is 0.758. Their Table S2 leave-one-region-out fine-tuning arms, which use no PA data, reach NZ 0.759 and SA 0.820, so those are now the best known region means. Anand, Deneu and Radeloff (PNAS 2026) report a median per-species AUC of 0.774 for a CNN with augmentation on the environmental grids, over the 217 species with fewer than 1,000 presence records (ensemble 0.744 on that subset, 0.749 over all 225). A Google heterogeneous GNN (Harrell et al., arXiv 2503.11900) reports per-region values only in a figure. The Valavi paper page on Wiley returned 403 (BLOCKED) on 2026-10-30, so its numbers are taken from the DeepMaxent table.

## What counts as a win

Saved per-species predictions at every disdat PA evaluation site for all 225 species, from models fitted only on the disdat presence-only and background data (and, optionally, the OSF environmental grids). Two conditions must both hold. First, the AUC-ROC averaged within each region and then across the six regions is STRICTLY GREATER (direction: max) than 0.768 by at least 0.005. Second, the median per-species AUC-ROC over the 217 species with fewer than 1,000 presence records (the Anand et al. subset; the claim lists the species) is strictly greater than 0.774. Both values must also exceed any value for the same aggregation that the NOVELTY skeptic finds in a paper or released result table from the last 24 months. That includes the HGNN figure where it can be read and the tabfm-distribution results tables (checked 2026-10-30: 0.736 average, 0.758 median). The PA data must not be used for fitting, tuning, variable selection or model selection; tuning uses cross-validation within the presence-only data. NSW species are scored only on the evaluation sites of their own group, as disdat defines them.

## Partial wins

- **p1:** Average of the six region-mean AUCs strictly above 0.768 (DeepMaxent, target-group background), under the same no-PA-tuning rule, without the median condition.
- **p2:** One fixed configuration that beats the best known region mean in at least three of the six regions (AWT 0.732, CAN 0.732, NSW 0.752, NZ 0.759, SA 0.820, SWI 0.850; NZ and SA from the tabfm-distribution Table S2 fine-tuning arms), under the same no-PA-tuning rule.
- **p3:** A model using only the point covariates shipped in disdat (no rasters) whose median per-species AUC over the same 217-species subset is strictly above 0.774.

## How a win is checked

The skeptic installs disdat from CRAN and recomputes every per-species AUC from the saved predictions against the PA files (pROC or sklearn), then recomputes both aggregations. They re-run the fitting script for one region and check that the predictions agree. They read the code to confirm that the PA data are loaded only in the scoring step.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://export.arxiv.org/api/query?search_query=abs:%22presence-only%22+AND+abs:%22species+distribution%22&sortBy=submittedDate&sortOrder=descending&max_results=25>

## Sources

- <https://github.com/rspatial/disdat>
- <https://journals.ku.edu/jbi/article/view/13384>
- <https://osf.io/kwc4v/>
- <https://arxiv.org/abs/2412.19217>
- <https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12974460/fullTextXML>
- <https://arxiv.org/abs/2503.11900>
- <https://github.com/hideyuki-doi/tabfm-distribution>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Multi-species neural models with target-group background and Maxent-style losses (DeepMaxent), ensembled with down-sampled random forests.
- Cross-domain import (survey statistics): treat presence-only data as a biased sample and model observer effort explicitly (thinned point processes) before predicting.
- Spatial context from the OSF grids (patch CNNs, multi-scale summaries) for the median-AUC condition.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several published ablation tables choose hyperparameters by PA test AUC; such numbers are not a fair bar, and such tuning disqualifies a claim.
- Mean versus median per-species AUC, and region-average versus pooled average, give different numbers; the criterion fixes both.
- Species counts differ between papers (225 vs 226; one NSW species with two records is usually dropped); state the species list.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/ecology/nceas-disdat-presence-only-sdm-auc.md
```

Already set up? Say `run V3R1T4S on nceas-disdat-presence-only-sdm-auc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nceas-disdat-presence-only-sdm-auc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
