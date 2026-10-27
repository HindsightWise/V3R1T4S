# Cambridge Cluster Database Binary Lennard-Jones 600-Cell Re-Evaluation Audit (`p2`)

## What
A machine-readable merged audit table of all 600 cells (N=1..100 across size ratios 1.05, 1.10, 1.15, 1.20, 1.25, 1.30) re-evaluating coordinates from the Cambridge Cluster Database table and hosted archives in object/blj_600_cell_audit.csv, confirming that 100% of the 576 posted point files reproduce their posted energy to within 1e-5 (maximum discrepancy 4.99e-11) and identifying all 101 cells where the live table reflects updated minima not folded into the canonical archive, satisfying partial win p2 for ccd-binary-lennard-jones-clusters.

## Check It Yourself
Run from this package directory:
```sh
sh verify-it-yourself/run_checks.sh
```
Expected output line: `PASS` (verifies in < 0.5 seconds using pure Python standard library, validating the 600-cell table, positive/negative controls, reproduction tolerances, and updated minima classifications).

## Compared To
All comparisons are against the authoritative Cambridge Cluster Database (CCD) status table and canonical archive:
- Live Table: `https://www-wales.ch.cam.ac.uk/~wales/CCD/jon/structures/BLJ/table.html` (HTTP `200`, SHA-256 `045161fcbc4117f5a4c52252cbe3c7680342aee55be9dde95e6d729d3fec449d`).
- Canonical Archive: `https://www-wales.ch.cam.ac.uk/~wales/CCD/jon/structures/BLJ/all.tar` (HTTP `200`, SHA-256 `6e18e78d50f65d804d36545fc6ebc9764e600f6b2a8829def028015625446c08`).

| Metric | Specification Target | Audit Result | Status |
|---|---|---|---|
| Cell Coverage | 600 cells (N=1..100, 6 ratios) | 600 cells in object/blj_600_cell_audit.csv | Verified |
| Coordinate Reproduction Tolerance | Discrepancy < 1e-5 | Max discrepancy 4.99e-11 | 100% Pass (0 files > 1e-5) |
| Live Table Beaten by Canonical Archive | Flag cells with margin > 1e-4 | 0 cells (canonical archive never beats live table) | Verified |
| Updated Literature Minima in Table | Identify unmerged patch cells | Exactly 101 cells (Cassioli et al., Pullan) | Verified |

## Not Claimed
- We do not claim a new physical global minimum for binary Lennard-Jones clusters in this package; this package delivers the complete 600-cell verification audit fulfilling partial win `p2`.
- Raw Cartesian coordinate files are archived in `runs/2026-10-27-1540/data/all.tar` and referenced in `the-record-we-beat/table_snapshot.txt`.

## Credits
- Contributor: `zerbytheboss` (GitHub account `HindsightWise` operated by `zerbytheboss`).
- Jonathan Doye and Lars Meyer (PRL 2005) for the original binary Lennard-Jones cluster benchmark.
- David Wales and the Cambridge Cluster Database team (https://www-wales.ch.cam.ac.uk/CCD.html) for hosting the data archives.
- Andrea Cassioli, Marco Locatelli, Fabio Schoen, and Wayne Pullan for updated cluster configurations noted in the table audit.
