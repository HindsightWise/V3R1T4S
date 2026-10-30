# CryoBench: beat the best published per-image FSC AUC for cryo-EM heterogeneity on a ground-truth dataset

🦠 **Biology** · standard · tractability ★★☆☆☆ · compute: needs cluster (GPU; 100k-335k simulated particles per dataset, tens of GB) · open as of 2026-10-30

## The problem

CryoBench (Minkyu Jeon, Rishwanth Raghu, Miro Astore, Geoffrey Woollard, Ryan Feathers, Alkin Kaz, Sonya Hanson, Pilar Cossio and Ellen Zhong; NeurIPS 2024 spotlight, arXiv:2408.05526) provides simulated cryo-EM datasets with known ground-truth structures for the heterogeneity problem: IgG-1D (100 Fab rotation states, 100k images), IgG-RL (100 linker-driven conformations, 100k images), Ribosembly (16 bacterial ribosome assembly states, 335,240 images) and Tomotwin-100 (100 distinct cellular complexes, 100k images), with code, per-image FSC and embedding metrics in the repository and data on Zenodo (records 11629428 and 12528292). In the CryoBench tables RECOVAR led IgG-1D at 0.386, IgG-RL at 0.363 and Ribosembly at 0.429 mean per-image FSC AUC, and CryoDRGN led Tomotwin-100 at 0.316, all with poses given. Three later papers have moved those rows. CryoSPIRE (Shayan Shekarforoush, David B. Lindell, Marcus A. Brubaker and David J. Fleet, arXiv:2506.09063) raised IgG-1D to 0.396 and IgG-RL to 0.375 with poses given, while reporting 0.422 on Ribosembly and not evaluating Tomotwin-100. SOLVAR (arXiv:2602.17603) reports 0.388 / 0.369 / 0.431 on the three and 0.333 on Tomotwin-100 at rank 50. CryoHype (arXiv:2512.06332) reports 0.346 on Tomotwin-100 with poses given, against a backprojection upper bound of 0.364. So the current fixed-pose bests are IgG-1D 0.396, IgG-RL 0.375, Ribosembly 0.431 and Tomotwin-100 0.346. Ab initio remains far behind: CryoDRGN-AI 0.351 / 0.329 / 0.341 / 0.072 and 3D Class abinit 0.130 on IgG-1D, with SOLVAR's RELION-initialised pose-optimising run the best published ab initio pipeline at 0.385 / 0.334 / 0.424 / 0.103. On clustering, RECOVAR reaches ARI 0.968 on Ribosembly and CryoDRGN 0.956 on Tomotwin-100, but every ab initio method collapses on Tomotwin-100 (best ARI 0.116, CryoDRGN2), and the authors state that current ab initio reconstruction cannot recover the 100 ground-truth structures. This target covers those four datasets only.

## What counts as a win

For a declared CryoBench dataset among IgG-1D, IgG-RL, Ribosembly and Tomotwin-100: the reconstructed per-particle volumes (or a generator plus the per-particle latent codes needed to produce them) for the full released dataset, such that the skeptic, running the repository's metrics/fsc code against the released ground-truth volumes, obtains a mean per-image FSC AUC STRICTLY HIGHER (direction: max) than the best published value for that dataset - IgG-1D 0.396 and IgG-RL 0.375 (CryoSPIRE, arXiv:2506.09063), Ribosembly 0.431 (SOLVAR, arXiv:2602.17603) and Tomotwin-100 0.346 (CryoHype, arXiv:2512.06332), all re-fetched live immediately before claiming - by at least 0.010, and higher than any later published value for the same dataset and metric found by the novelty check; with the input regime declared (poses given, or ab initio) and compared only against published rows of the same regime, no ground-truth volume, conformational label or ground-truth embedding used at any stage, and code, configs, seeds and latent codes published so the metric recomputes.

## Partial wins

- **p1:** In the ab initio regime (poses not supplied, pose estimation part of the attacker's own pipeline), a mean per-image FSC AUC on a declared dataset strictly above the best published ab initio value for it - SOLVAR with RELION initialisation and pose optimisation at 0.385 on IgG-1D, 0.334 on IgG-RL, 0.424 on Ribosembly and 0.103 on Tomotwin-100 (arXiv:2602.17603), above CryoDRGN-AI's 0.351 / 0.329 / 0.341 / 0.072 - by at least 0.010.
- **p2:** On Tomotwin-100, a clustering ARI strictly above 0.116 (best published ab initio, CryoDRGN2) by at least 0.05 in the ab initio regime, or strictly above 0.956 (CryoDRGN, poses given) by at least 0.005 in the fixed-pose regime, computed with the repository's metrics.
- **p3:** A reproduction artefact: reproducing a published CryoBench row (method, dataset, FSC AUC) to within 0.010 with the public code and data, with runtime and hardware reported, published as a reproduction.

## How a win is checked

Skeptic downloads the declared dataset from its Zenodo record and the ground-truth volumes, installs cryodrgn and the CryoBench metrics code at the pinned versions, recomputes mean per-image FSC AUC (and ARI/AMI where claimed) from the attacker's volumes or latents, checks that every particle of the released dataset is covered, reads the configs to confirm no ground-truth volume, label or embedding was used and that the pose regime matches the rows compared against, and re-fetches the paper's tables. Scoring is hours of GPU time; the reconstruction is the attacker's cost.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/html/2408.05526v2>

## Sources

- <https://arxiv.org/html/2408.05526v2>
- <https://arxiv.org/abs/2506.09063>
- <https://arxiv.org/abs/2602.17603>
- <https://arxiv.org/abs/2512.06332>
- <https://github.com/ml-struct-bio/cryobench>
- <https://zenodo.org/records/11629428>
- <https://zenodo.org/records/12528292>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The compositional datasets punish continuous latent models: try a discrete-plus-continuous latent (mixture over states with a per-state deformation) instead of one smooth embedding.
- Tomotwin-100 is the clearest failure: 100 unrelated complexes with shared pose estimation, so a pipeline that alternates clustering and per-cluster ab initio refinement may beat joint embedding.
- Cross-domain import (mixture modelling and clustering): initialise with a robust covariance/PCA step (the route RECOVAR takes) before any neural model, which fixes the collapse that random initialisation causes.
- Spend effort on pose accuracy in the ab initio regime; the paper reports pose error separately and it is the dominant term in the FSC gap.
- Report the per-conformation FSC curve, not only its AUC, so a gain concentrated on the easiest states is visible.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Ground-truth volumes, state labels and reference embeddings ship with the datasets; touching them anywhere in the pipeline (even for model selection) invalidates the result.
- Fixed-pose and ab initio numbers are not comparable; a fixed-pose result quoted against an ab initio row is not a win, and a pipeline that takes poses from a prior consensus refinement must say so.
- On Tomotwin-100 the headroom is small: CryoHype reports a backprojection upper bound of 0.364 against its own 0.346, so a gain there has to be close to that ceiling.
- FSC AUC is sensitive to box size, downsampling and masking; use the repository's code unchanged and state the resolution of the images used.
- The datasets are simulated, so a gain here is a benchmark result and need not transfer to experimental micrographs; claims must stop at the benchmark.
- The paper's Spike-MD dataset is outside this target's scope; results on it do not count toward this win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/biology/cryobench-heterogeneity-fsc-auc.md
```

Already set up? Say `run V3R1T4S on cryobench-heterogeneity-fsc-auc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cryobench-heterogeneity-fsc-auc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
