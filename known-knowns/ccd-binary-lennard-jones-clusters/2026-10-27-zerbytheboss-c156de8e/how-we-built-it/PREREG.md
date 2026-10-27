# Preregistered Evaluation Bar (`ccd-binary-lennard-jones-clusters`)

frozen_utc: 2026-10-27T15:08:00Z
target_id: ccd-binary-lennard-jones-clusters
category: packings-physics
null_test: not needed because deterministic checker evaluates analytical potential energy and Hessian eigenvalues on explicit coordinates

## 1. Verbatim Target Bank Criteria
> Success means an xyz file with N atoms labelled A/B (any composition) for a size ratio in {1.05,...,1.3} and N <= 100, whose energy E* = sum_{i<j} 4 eps (sigma_ij^12/r^12 - sigma_ij^6/r^6) (sigma_AA = 1, sigma_BB = ratio, sigma_AB = (1+ratio)/2, eps = 1, no cutoff) is STRICTLY LOWER (direction: min) by at least 1e-4 than the minimum of: the energy for that (N, ratio) on the CCD BLJ table re-fetched live immediately before claiming, the energies in every improvement archive linked from https://www-wales.ch.cam.ac.uk/CCD.html (re-downloaded and re-evaluated by the checker, not read from headers), and any value for that cell in Cassioli et al. (population basin hopping, 95 new minima), Marques-Pereira 2010 (Chem. Phys. Lett. 485, 211), Kolossvary-Bowers 2010, Sicher-Mohr-Goedecker 2011, Ye-Xu-Huang 2011, Rondina-Da Silva 2013 (J. Chem. Inf. Model. 53, 2282), Wu-Cheng 2014 (J. Chem. Phys. 141, 124110), Takeuchi (Comput. Theor. Chem. 1050, 68), or any later paper found by an arXiv/Google Scholar search for 'binary Lennard-Jones clusters global minima'; AND the structure is a certified local minimum: polish in float128 or mpmath (30 digits) to gradient norm < 1e-10 in reduced units, then the 3N x 3N Hessian in double precision has exactly 6 near-zero modes (|lambda| < 1e-6) and no negative eigenvalue; AND polishing every posted structure for that cell with the same routine gives an energy at least 1e-4 higher (distinct basin).

## 2. Partial Wins (Verbatim)
- p1: A certified improvement for some (N, ratio) with N in 101..150 over the best value in a fetchable published table (DOI or arXiv plus table reference); reported as a literature frontier, not a CCD record.
- p2: Audit: a machine-readable merged table of all 600 cells (min over the CCD table and all hosted archives, each re-evaluated from coordinates), listing every cell where the live table is beaten by a hosted file by > 1e-4 and any posted point file that does not reproduce its own posted energy within 1e-5.
- p3: A certified improvement at a size ratio in 1.4..2.0 for N <= 50 over Takeuchi's published value for the same (N, ratio) (his supplementary data), or a first certified putative global minimum for ratio 1.4..2.0 at N in 51..100 reported as a literature frontier.

## 3. Evaluation Metric & Thresholds
- Binary Lennard-Jones potential: $\varepsilon = 1$, $\sigma_{AA} = 1$, $\sigma_{BB} = \text{ratio}$, $\sigma_{AB} = (1 + \text{ratio})/2$.
- Gradient norm threshold: $\|\nabla E\|_2 < 10^{-10}$.
- Hessian spectrum: Exactly 6 eigenvalues $|\lambda| < 10^{-6}$ and $\lambda_{\min} \ge 0$ (all non-rigid modes strictly positive).
- Energy improvement threshold: $\Delta E \ge 10^{-4}$ below comparator minimum.
