# New open cluster in Gaia DR3 absent from the Unified Cluster Catalogue (UCC 260615) and the Hunt and Reffert census

🔭 **Sky archives** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours per field (Gaia DR3 TAP cone queries of a few deg; a full Galactic-plane blind search is laptop-days; the UCC_cat.csv is a few MB, UCC_members.parquet ~100 MB) · open as of 2026-10-30

## The problem

Hunt and Reffert (2023, A&A 673, A114) ran HDBSCAN over all of Gaia DR3 and recovered 7167 clusters, 2387 of them candidate new objects (739 in the stringent subset). Hunt and Reffert (2024, arXiv:2403.05143) found only 5647 compatible with bound clusters. They estimated that the Milky Way holds ~1.3e5 open clusters, only ~4% of them known, and that the census is complete within 1.8 kpc only above ~230 Msun. Hunt et al. (arXiv:2510.18343) published the census selection function. The Unified Cluster Catalogue (UCC; Perren, Pera, Navone and Vazquez 2023, MNRAS 526, 4107; maintained by Gabriel I. Perren at ucc.ar) merges 152 articles into 18,299 clusters with fastMP members. Version 260615 (Zenodo record 20705026, 2026-06-15) is the latest, and 2026 papers keep adding clusters (e.g. arXiv:2603.26572, 2606.01418, 2601.09670). Open task: find a statistically significant, CMD-coherent and preferably bound stellar cluster in Gaia DR3 that is in neither UCC nor any later paper. Gaia DR4 (66 months) is due 2026 December 2 and will change the data; a claim based on DR3 must say so and use DR3 values throughout.

## What counts as a win

A saved bundle (ADQL queries and Gaia DR3 source_ids of >= 20 members with 5- or 6-parameter astrometry, RUWE < 1.4, G < 20; clustering code; isochrone fit) where: (1) the Hunt and Reffert astrometric significance test (CST) gives >= 5 sigma, run in their public code or in a re-implementation shown to reproduce CST within 1 sigma for 20 HR23 clusters; (2) parallaxes are consistent with one distance (reduced chi^2 < 2 about the weighted mean) and the error-corrected proper-motion dispersion is <= 2 km/s at that distance; (3) a single PARSEC isochrone (free age, distance, A_V) puts >= 80% of members within 0.15 mag of colour, while the same pipeline on 20 field control samples (same pm/parallax window, other positions) puts < 50%; (4) the half-mass radius is inside the Jacobi radius computed from a photometric mass as in Hunt and Reffert 2024; (5) no entry in UCC_cat.csv (latest Zenodo version) lies within max(3 r50, 10 arcmin) with |delta pm| < 1 mas/yr and |delta plx| < 0.3 mas, and no paper after the UCC changelog date reports it (status pages re-fetched immediately before claiming). The win is one new object passing (1)-(5).

## Partial wins

- **p1:** A blind pipeline run on a declared sky region ( > = 100 deg^2 of the plane) that recovers >= 90% of the Hunt and Reffert high-quality clusters inside it, with the recovered list and the misses saved.
- **p2:** A new group that passes (1), (2), (3) and (5) but not the boundness test (4): a new unbound association or moving group, logged as such.
- **p3:** A new object passing (1)-(5) at a distance < 1 kpc, where the census is supposed to be most complete.

## How a win is checked

Skeptic re-runs the saved ADQL against the Gaia archive TAP, recomputes CST, the dispersion and the isochrone fit with the saved code, and cross-matches against the newest UCC_cat.csv from Zenodo and the UCC changelog. Under an hour per object.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://ucc.ar/changelog/>

## Sources

- <https://ucc.ar/database/>
- <https://ucc.ar/changelog/>
- <https://zenodo.org/records/20705026>
- <https://arxiv.org/abs/2303.13424>
- <https://arxiv.org/abs/2403.05143>
- <https://arxiv.org/abs/2510.18343>
- <https://gea.esac.esa.int/archive/>
- <https://www.cosmos.esa.int/web/gaia/release>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Distant (2-5 kpc), low-N groups where the Hunt and Reffert selection function predicts a low detection probability (high parallax error, dense fields): most of the ~96% of clusters still unknown are expected there.
- Run HDBSCAN in rescaled (l, b, pmra, pmdec, parallax) with a smaller min_cluster_size than HR23 in narrow parallax slices, then demand CST >= 5 sigma.
- Cross-domain import (epidemiology): spatial-scan statistics (Kulldorff) give a calibrated significance for compact overdensities in a 5D space.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- UCC lists anything ever called an open cluster, under many names (FSR, UBC, CWNU, HSC, OCSN, Theia...); match by position and astrometry, not by name.
- Gaia scanning-law patterns and extinction holes create fake overdensities; check the CMD and the field control samples.
- Binaries and blends inflate the proper-motion dispersion; use RUWE cuts.
- Gaia DR4 (2026-12-02) will redefine members and errors; state which release every number comes from.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/sky-archives/gaia-dr3-open-cluster-not-in-ucc.md
```

Already set up? Say `run V3R1T4S on gaia-dr3-open-cluster-not-in-ucc`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gaia-dr3-open-cluster-not-in-ucc`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
