# Kob-Andersen binary Lennard-Jones crystals: a periodic 80:20 structure with lower zero-pressure energy than the Cambridge Cluster Database records (-7.4903 per atom at N = 60, -7.5015 at N = 320)

⚪ **Packings and physics** · standard · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The Kob-Andersen (KA) 80:20 binary Lennard-Jones mixture is the standard model glass-former (Walter Kob and Hans C. Andersen, PRL 73, 1376, 1994; sigma_AA = 1, sigma_AB = 0.8, sigma_BB = 0.88, eps_AA = 1, eps_AB = 1.5, eps_BB = 0.5). Its crystalline ground state is a crystal-structure-prediction benchmark. Thomas Middleton, Javier Hernández-Rojas, Paul Mortenson and David Wales (PRB 64, 184201, 2001) posted low-energy crystals for 60-, 256- and 320-atom periodic cells at number density 1.2 on the Cambridge Cluster Database (CCD). Maximilian Amsler and Stefan Goedecker (J. Chem. Phys. 133, 224104, 2010; arXiv:1007.2003) then ran variable-cell minima hopping at zero pressure, with each pair potential cut at 2.5 sigma_ab and smoothed by the Stoddard-Ford quadratic term. They found several thousand structures below the earlier ones. The CCD index links their putative ground states as BLJ60, BLJ256 and BLJ320 (files dated 2011-02-28): - N = 60 (48 A + 12 B; a 30-atom P2_1/m primitive cell): -7.4903 eps_AA per atom. - N = 256 (205 A + 51 B; P1): -7.4281. - N = 320 (256 A + 64 B; a 40-atom Bbmm primitive cell): -7.5015. An independent lattice sum written for this update reproduces -7.490330, -7.428094 and -7.501546. Later KA crystal studies do not test these records: the Pedersen-Schrøder-Dyre phase diagram (PRL 120, 165501, 2018) and the USPEX convex hull of Yu. D. Fomin and N. M. Chtchelkatchev (arXiv:2409.00710, 2024) both use a plain truncate-and-shift at P* = 10.19. The Fernández-Harrowell picture of coexisting fcc A and CsCl AB puts the phase-separated thermodynamic limit at zero pressure at or below about -7.585 per atom. That value is the lever rule over lattice sums with this potential (fcc A -6.80362, CsCl AB -8.75686). A-rich compounds that Fernández and Harrowell (2004) and Pedersen et al. report as low in energy (PuBr3-, Fe3C- and Ni3P-type A3B, Al2Cu-type A2B) could make the limit lower still if they fall below the fcc/CsCl tie line under this truncation. Lower energies therefore exist for large cells, and the fixed-N records are about fitting two phases and their interfaces into 60 or 320 atoms. No published improvement on the hosted records was found.

## What counts as a win

Success means a periodic cell (lattice vectors and Cartesian coordinates to at least 12 significant digits, with A/B labels) containing exactly N = 60 atoms (48 A + 12 B) or N = 320 atoms (256 A + 64 B). The checker computes its potential energy per atom E/N as a full lattice sum (all periodic images within the cutoff, never minimum-image) of phi_ab(r) = 4 eps_ab [(sigma_ab/r)^12 - (sigma_ab/r)^6] + 4 eps_ab [6 (sigma_ab/rc)^12 - 3 (sigma_ab/rc)^6] (r/rc)^2 - 4 eps_ab [7 (sigma_ab/rc)^12 - 4 (sigma_ab/rc)^6] for r < rc = 2.5 sigma_ab, and zero beyond, with the KA parameters. After the checker's variable-cell relaxation to residual forces below 1e-8 and stress below 1e-7 (reduced units), E/N must be STRICTLY LOWER (direction: min) by at least 1e-4 than the checker's re-evaluation of the CCD-hosted structure for that N, re-fetched immediately before claiming (-7.490330 for N = 60 and -7.501546 for N = 320 on 2026-10-28). The target pressure is zero, so enthalpy equals energy and cell shape and volume are free. A literature search must find no lower published value for the same N, potential and truncation, and the search is reported with the claim.

## Partial wins

- **p1:** A periodic cell with any N from 321 to 5,000 and exactly N_A = 4 N_B whose relaxed E/N, under the same potential and relaxation rules, is below -7.501546 (the lowest value hosted for any size) by at least 1e-3, reported with its N. Phase-separated fcc-A/CsCl-AB arrangements approach about -7.585 as N grows, so this locates the cell size at which coexistence first wins.

## How a win is checked

Checker script, under 5 minutes on a laptop: parse the cell, assert the composition, compute E/N by a float64 lattice sum (re-checked in mpmath at 30 digits for the final value), compute forces and the virial stress, and re-run a variable-cell FIRE/BFGS relaxation. Calibrate on the three hosted files first: they must reproduce -7.490330, -7.428094 and -7.501546 to within 1e-5.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www-wales.ch.cam.ac.uk/CCD.html>

## Sources

- <https://www-wales.ch.cam.ac.uk/~tfm21/bljcryst/BLJ.html>
- <https://www-wales.ch.cam.ac.uk/~wales/CCD/NEW_BINARY_LJ_MINIMA/BLJ_60_prim.ascii>
- <https://www-wales.ch.cam.ac.uk/~wales/CCD/NEW_BINARY_LJ_MINIMA/BLJ_256_prim.ascii>
- <https://www-wales.ch.cam.ac.uk/~wales/CCD/NEW_BINARY_LJ_MINIMA/BLJ_320_prim.ascii>
- <https://www-wales.ch.cam.ac.uk/CCD.html>
- <https://arxiv.org/abs/1007.2003>
- <https://arxiv.org/abs/2409.00710>
- <https://arxiv.org/abs/1803.08956>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Interface engineering: build fcc-A/CsCl-AB (or fcc-A plus an A3B-type compound) slab-coexistence cells with commensurate interfaces, scan interface orientations and strain matching, and relax them at zero pressure.
- Variable-cell random structure search (AIRSS-like) or genetic algorithms with symmetry constraints on 20- to 80-atom cells, then tile the winners to N = 60 or 320.
- Seed from the 40-atom Bbmm BLJ320 cell and the 30-atom BLJ60 cell; add A/B identity-swap moves to minima hopping.
- Cross-domain (materials interfaces): compute fcc(A)|CsCl(AB) interface energies for candidate orientations first, then predict the N at which slabs beat -7.5015 before searching.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Truncation matters. The records use the Stoddard-Ford quadratic smoothing at 2.5 sigma_ab: not the plain KA truncate-and-shift, not RUMD's linear shifted force, and not the 1.842 cutoff column on the same page. Energies under different truncations are not comparable.
- The Middleton et al. fixed-density (1.2) table on the same CCD page is stale. Uniformly rescaling the hosted 320-atom structure to density 1.2 already gives -7.4077 (Stoddard-Ford, cutoff 2.5), below the tabulated -7.33, so beating a density-1.2 cell is not a win here.
- The 30- and 40-atom primitive cells are about 1.1 sigma thick along one axis, so the energy needs full image sums; minimum-image code silently drops neighbours.
- Composition must be exact (60: 48/12; 320: 256/64). A 4:1 cell of another size counts only under p1.
- The hosted files are already zero-pressure minima of this potential (residual forces about 3e-7 and stress about 1e-8 in reduced units, checked for this update). Re-relaxing them gains nothing, so a win must be a different basin.
- The hosted BLJ256 (P1, -7.4281) is far from optimal, which is why N = 256 is not a target. A coherent fcc-A/CsCl-AB column stacked along [001] with one atom per layer (205 A + 51 B) already relaxes at zero pressure to -7.4911.
- Coherent [001] (Bain-path) stacking of fcc A and CsCl AB cannot reach the records. The in-plane mismatch between fcc A (a/sqrt(2) = 1.1006) and CsCl AB (a = 1.0422) is about 5.5% and costs strain energy. Such columns level off near -7.4957 per atom: -7.4890 at N = 60 and -7.4944 at N = 320. Strain relief, other interface orientations or other A-rich motifs are needed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/ccd-kob-andersen-crystal-ground-states.md
```

Already set up? Say `run V3R1T4S on ccd-kob-andersen-crystal-ground-states`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ccd-kob-andersen-crystal-ground-states`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
