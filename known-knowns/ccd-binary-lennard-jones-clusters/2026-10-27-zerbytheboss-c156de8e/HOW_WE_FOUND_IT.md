# How We Found It: Binary Lennard-Jones Clusters Audit (`p2`) & Literature Frontier (`p3`)

_contributor text, unverified_

## Methodology

### 1. Database & Improvement Archives Recomputation Audit (`p2`)
We downloaded and parsed raw Cartesian coordinates across all point files from:
1. Canonical archive `all.tar` (576 structures).
2. Huang Wenqi & Ye Tao (JCIM 2011) archives: `Wenqi_Tao_BLJ.zip` (12 structures) and `Wenqi_Tao_BLJ2.zip` (17 structures).
3. Istvan Kolossvary (PRE 2010) archive: `Istvan_Kolossvary_new_BLJ_minima.tgz` (17 structures).
4. Sicher, Mohr & Goedecker (JCP 2011) archive: `NEW_BINARY_LJ_MINIMA/` (17 cluster structures).

For every structure, we computed the pairwise binary Lennard-Jones potential without cutoff:
$$E = \sum_{i < j} 4 \left( \left(\frac{\sigma_{ij}}{r_{ij}}\right)^{12} - \left(\frac{\sigma_{ij}}{r_{ij}}\right)^6 \right)$$
with Lorentz-Berthelot arithmetic mean $\sigma_{AB} = (1 + \text{ratio}) / 2$, $\sigma_{AA} = 1.0$, $\sigma_{BB} = \text{ratio}$.

We verified:
- Analytical positive control: dimer $N=2$ at $r = 2^{1/6}$ gives $E = -1.000000000000$.
- Analytical negative control: perturbed dimer at $r = 1.25$ gives $E = -0.773698093056 > -1.0$.
- 100% of all posted point files in the canonical archive reproduce their posted header energies within $10^{-5}$ (max discrepancy $4.99 \times 10^{-11}$).
- Exactly 33 cells across the 600-cell space have hosted archive files that beat the live table by $> 10^{-4}$.

### 2. Literature Frontier Putative Minima Certification (`p3`)
For size ratio $\sigma_{BB}/\sigma_{AA} = 1.50$ (where no entries exist in the canonical CCD table), we constructed putative global minima across $N \in [51..60]$:
1. Seeded initial structures with Mackay icosahedral and polytetrahedral cores.
2. Optimized chemical ordering using distance-from-center-of-mass sorting, placing small A atoms in the core and large B atoms on the surface.
3. Relaxed with L-BFGS-B and performed analytical Newton-Raphson polish in 30-digit `mpmath` until gradient norm $\|\nabla V\| < 10^{-10}$ in reduced units.
4. Evaluated and diagonalized the full $3N \times 3N$ analytical Hessian:
   - Exactly 6 zero modes ($|\lambda| < 10^{-5}$) corresponding to continuous rigid body translations and rotations.
   - Zero negative eigenvalues, certifying true local minima.
