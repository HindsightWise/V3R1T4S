# How We Found It — `ccd-binary-lennard-jones-clusters` (p2 Audit)

Contributor text, unverified.

## Brief & Observation
The Cambridge Cluster Database (CCD) binary Lennard-Jones cluster benchmark (Doye & Meyer, PRL 2005) tabulates putative global energy minima across 600 cells covering cluster sizes N in [1..100] and 6 size ratios sigma_BB / sigma_AA in {1.05, 1.10, 1.15, 1.20, 1.25, 1.30}. Partial win p2 requires a comprehensive machine-readable merged audit table covering all 600 cells, re-evaluating energies directly from Cartesian coordinates, identifying any posted point files that do not reproduce their stated energies within 1e-5, and cataloging any discrepancy where hosted files or the live table diverge by > 1e-4.

## What Failed
Naive assumption that the canonical archive `all.tar` is identical to the live web table `table.html` failed: cross-referencing revealed that 101 cells in the live table link to updated structures (such as `1.2/100new` with energy -591.743842 by Cassioli, Locatelli & Schoen, and Wayne Pullan) while `all.tar` retains the older 2005 structures (e.g. -589.539621 at N=100, ratio 1.20).

## What Worked
In `runs/2026-10-27-1540/`, Lens 1 implemented the exact pairwise binary Lennard-Jones potential engine with Lorentz-Berthelot arithmetic mixing (sigma_AB = (1 + ratio)/2, eps = 1, no cutoff) and re-evaluated all 576 Cartesian coordinate files extracted from `all.tar` alongside analytic baselines for N in [1..4]. The audit proved:
1. Every one of the 576 posted coordinate files reproduces its internal header energy to within machine double precision (maximum absolute discrepancy 4.99e-11, zero files exceeding 1e-5).
2. Exactly 101 cells exhibit table-vs-archive discrepancies > 1e-4 due to post-2005 literature updates integrated into the HTML table but omitted from the tar archive.
3. Zero files in the canonical archive beat the live table by > 1e-4.
All 600 cells are compiled into the machine-readable table `object/blj_600_cell_audit.csv`.
