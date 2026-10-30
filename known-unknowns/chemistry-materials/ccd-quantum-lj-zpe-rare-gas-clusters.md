# Quantum-corrected Lennard-Jones clusters (Xe, Ar, Ne with harmonic zero-point energy): lower a global minimum in the Calvo-Doye-Wales table (N < 100)

⚗️ **Chemistry and materials** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The Cambridge Cluster Database hosts the table of Florent Calvo, Jonathan Doye and David Wales (J. Chem. Phys. 114, 7312, 2001; page dated 12/12/2000) for the 36 sizes N in 17..98 where quantum delocalisation changes the global minimum of LJ_N. Each row is a classical LJ minimum with its energy E_LJ and E_Xe, E_Ar, E_Ne (5 decimals, reduced units): the classical energy plus the harmonic zero-point energy at that minimum (no re-optimisation). A check on 2026-10-30 found that, on 27 posted point files that match their rows, E_sp = E_LJ + (q/2) * sum_i sqrt(lambda_i) reproduces all four columns to 1.1e-4 or better (to 3e-5 for every row except 44B). Here E_LJ = 4 sum (r^-12 - r^-6), the lambda_i are the 3N-6 nonzero eigenvalues of the analytic Hessian of that E_LJ (unit masses), and q is the de Boer parameter hbar/(sigma sqrt(m epsilon)): 0.01 (Xe), 0.03 (Ar) or 0.095 (Ne). Examples of the bar: N = 38 Ne -107.42431 (38B, C1, beating the classical Oh 38A at -106.47765); N = 98 Ne -349.46688 (98B, Cs). The candidate sets were drawn from low-lying LJ minima known in 2000. For Ne, open low-frequency structures win, and no later re-search of this table with a ZPE-aware objective is posted on the CCD. The classical LJ global minima are a separate entry (lennard-jones-ccd-doye-table).

## What counts as a win

Coordinates ( > = 12 digits) of N atoms, for an N with rows on the live table (https://www-wales.ch.cam.ac.uk/~florent/LJZPE/table.html, re-fetched immediately before claiming), that form a certified local minimum of the classical E_LJ = 4 sum (r^-12 - r^-6): gradient norm < 1e-9, analytic Hessian of that E_LJ with exactly 6 eigenvalues of magnitude < 1e-6 and none below -1e-6. In addition, E_sp = E_LJ + (q/2) sum sqrt(lambda_i) over the 3N-6 nonzero eigenvalues, with q = 0.01 (Xe), 0.03 (Ar) or 0.095 (Ne), must be STRICTLY LOWER (direction: min) by at least 5e-4 than the lowest tabulated value in that species' column for that N (minimum over the A/B/C rows), and lower by at least 5e-4 than any published harmonic-ZPE value for the same N and q that the skeptic finds. The checker must first reproduce the table rows 17A, 31B, 38A and 38B from their posted point files to 5e-5 with the same code. Structures re-optimised on the quantum-corrected surface do not count: the convention is a classical minimum plus its harmonic ZPE.

## Partial wins

- **p1:** For a size N in 13..99 that has no rows in the table (the table implies the classical global minimum stays lowest for all three species), a certified classical LJ local minimum whose E_Ne (q = 0.095) is lower by at least 5e-4 than E_Ne of the CCD/Doye classical global-minimum point file for that N evaluated with the same rule.
- **p2:** For a size N in 100..150, beyond the table, a certified classical LJ local minimum whose E_Ne (q = 0.095) is lower by at least 5e-4 than E_Ne of the CCD classical global-minimum point file for that N (a literature frontier, not a table record).

## How a win is checked

Python checker (minutes): parse the live table; evaluate E_LJ, the analytic gradient and the Hessian in double precision (mpmath for the final energy); polish with BFGS or Newton; take the eigenvalues; drop the 6 zero modes; apply the ZPE rule; calibrate on rows 17A, 31B, 38A and 38B (http://www-wales.ch.cam.ac.uk/~florent/LJZPE/points/ < label > ); compare with the minimum of the tabulated column for N; for p1 and p2, evaluate the classical GM point file from https://doye.chem.ox.ac.uk/jon/structures/LJ.html (LJ.tar) or the LJ310+ pages the same way.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www-wales.ch.cam.ac.uk/~florent/LJZPE/table.html>

## Sources

- <https://www-wales.ch.cam.ac.uk/~florent/LJZPE/LJzpe.html>
- <https://www-wales.ch.cam.ac.uk/~florent/LJZPE/table.html>
- <http://www-wales.ch.cam.ac.uk/~florent/LJZPE/points/38B>
- <https://www-wales.ch.cam.ac.uk/~jon/abstracts/jcp01.html>
- <https://doye.chem.ox.ac.uk/jon/structures/LJ.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Ne at q = 0.095 rewards low-frequency, less compact minima: enumerate many low-lying LJ_N minima (basin-hopping or a disconnectivity database) and rank them by E_LJ + ZPE, not by E_LJ alone.
- Run basin-hopping on the objective E_LJ + ZPE(local minimum), quenching on the classical surface at each step, so the search is ZPE-aware while the convention is kept.
- For p1, scan sizes next to listed ones (e.g. 39-43, 58-64, 94-97), where the table's authors may have stopped.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Several posted point files do not match their rows (checked 2026-10-30): 67B, 75B, 77C, 78B, 82B, 83B, 84B and 86B evaluate to E_LJ values other than the tabulated ones (e.g. 82B gives -439.48103 against the row's -440.04139). The tabulated number, not the file, is the bar.
- Point files for 65A-C, 69A-B, 79A-B, 85A-B and 87A to 93B return 404 (2026-10-30); the tabulated values still stand.
- Factor-of-sqrt-2 trap: the rule is (q/2) sum sqrt(lambda) with the Hessian of 4 sum (r^-12 - r^-6). A gradient or Hessian that double-counts pairs is twice too large and then seems to need q/(2 sqrt 2); an earlier draft of this entry made exactly that error. Always calibrate on 17A, 31B, 38A and 38B first.
- Row 44B is reproduced only to 1.1e-4 even with an analytic Hessian; use rows that reproduce to 5e-5 for calibration.
- Emailing the CCD maintainers is an outbound message for the human, never for the agent.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/chemistry-materials/ccd-quantum-lj-zpe-rare-gas-clusters.md
```

Already set up? Say `run V3R1T4S on ccd-quantum-lj-zpe-rare-gas-clusters`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ccd-quantum-lj-zpe-rare-gas-clusters`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
