# IEA Wind Task 37 case study 4 (Borssele III/IV, 81 x 10 MW): a feasible layout with higher AEP than DEBO's 2,913,220.604 MWh

🛠️ **Engineering and chips** · standard · tractability ★★☆☆☆ · compute: laptop-hours (vectorised AEP about 0.1 s for 81 turbines x 360 directions x 20 speeds) · open as of 2026-10-30

## The problem

IEA Wind Task 37 case study 4 places 81 IEA37 10 MW turbines (D = 198 m, cut-in 4, rated 11, cut-out 25 m/s). The site is five disjoint polygonal regions adapted from Borssele III and IV by Sebastian Sanchez Perez-Moreno and Erik Quaeghebeur and modified by N. F. Baker. Turbines may be placed inside any region but not between regions, and every pair must be at least 2D = 396 m apart. The wake model is the simplified Bastankhah Gaussian (k = 0.0324555, CT = 8/9, root sum of squares) over the 360-direction x 20-speed wind rose iea37-windrose-cs4.yaml. Thomas, Baker, Malisani, Quaeghebeur, Sanchez Perez-Moreno, Jasa, Bay, Tilli, Bieniek, Robinson, Stanley, Holt and Ning compared eight methods ('A comparison of eight optimization methods applied to a wind farm layout optimization problem', Wind Energ. Sci. 8, 865-891, 2023; data on Zenodo 10.5281/zenodo.7125349). The best layout came from discrete exploration-based optimization (DEBO): 2,913,220.60417 MWh. Next best: DPA 2,910,537.867, SNOPT+WEC 2,910,115.644, ADREMOG 2,909,489.259; the provided base layout scores 2,851,096.413. An independent re-implementation run on 2026-10-30 reproduces all nine posted layouts to 1e-5 MWh. The DEBO layout lies inside the regions with zero excess and a minimum spacing of 2.058D. Note that debo.yaml's stored 'default' value (2,861,182.5) comes from an older 20-bin rose; the 360-bin value matches the paper's 2913.221 GWh. I found no later absolute record (Valotta Rodrigues et al. 2024 and Perez-Rua et al. 2023 use case study 1).

## What counts as a win

81 turbine positions, each inside or on one of the five polygons of iea37-boundary-cs4.yaml (IIIa, IIIb, IVa, IVb, IVc; point-in-polygon with zero tolerance, edges included), with every pair at least 396 m apart (no tolerance). The AEP, computed with the provided_model.py equations from the Zenodo record using the 360-bin iea37-windrose-cs4.yaml and iea37-10mw.yaml, must be STRICTLY GREATER (direction: max) than 2,913,220.60417 MWh (DEBO, Thomas et al. 2023) by at least 1 MWh.

## Partial wins

- **p1:** A feasible layout (same zero-tolerance checks) with AEP strictly above 2,910,537.86749 MWh (DPA, second best) by at least 1 MWh, such that under the minimum-total-distance one-to-one matching to the DEBO layout at least 27 of the 81 turbines are more than 198 m (1D) from their partner (an independent layout, not a perturbed DEBO).
- **p2:** An independent evaluator (not running provided_model.py) that reproduces all nine posted 360-bin AEPs (base, snoptwec, debo, gps, cmaes, gagb, adremog, pg, dpa) to within 1e-3 MWh, plus a per-layout boundary-excess and minimum-spacing report.

## How a win is checked

Load the claimed positions. Run a point-in-polygon test against the five region polygons, with the distance to the nearest edge reported, and a pairwise spacing check. Compute AEP from the wake-model equations over 360 directions x 20 speeds with the per-direction speed probabilities and direction frequencies, x 8760 h / 1e6. First reproduce snoptwec.yaml = 2,910,115.64377 and debo.yaml = 2,913,220.60417. Under a minute.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wes.copernicus.org/articles/8/865/2023/>

## Sources

- <https://wes.copernicus.org/articles/8/865/2023/>
- <https://doi.org/10.5281/zenodo.7125349>
- <https://github.com/jaredthomas68/thomas2022-8-opt-algs-wflop>
- <https://github.com/byuflowlab/iea37-wflo-casestudies/tree/master/cs3-4>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- DEBO-style sequential discrete allocation on a fine candidate grid inside each region, followed by continuous gradient polishing with exact boundary projections.
- Region-wise turbine-count reallocation: enumerate how many of the 81 turbines go in each of the five regions, then optimise each split.
- Wake expansion continuation with SNOPT or IPOPT from many DEBO-like seeds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- debo.yaml's stored AEP (2,861,182.5) was computed with the older 20-bin wind rose. Always evaluate with the 360-bin file.
- Only DEBO and GPS lie inside the regions with zero tolerance. The others sit slightly outside: CMA-ES 0.23 m, DPA 0.087 m, base 0.065 m, GA-GB 0.020 m, SNOPT+WEC 3.8 mm, ADREMOG and ADREMOG+PG about 0.1 mm. Feasibility here is judged with zero tolerance.
- Turbines between regions are infeasible even if inside the convex hull of the site.
- No later paper publishes an absolute CS4 AEP above DEBO as far as checked, but re-check before claiming; a literature search could not be repeated on 2026-10-30.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/engineering/iea37-cs4-borssele-81-turbine-layout.md
```

Already set up? Say `run V3R1T4S on iea37-cs4-borssele-81-turbine-layout`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `iea37-cs4-borssele-81-turbine-layout`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
