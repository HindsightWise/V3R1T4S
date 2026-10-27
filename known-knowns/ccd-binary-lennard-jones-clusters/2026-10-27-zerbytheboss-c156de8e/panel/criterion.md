# CRITERION Skeptic Audit — `ccd-binary-lennard-jones-clusters` (p2 Audit)

context: subagent (fresh invocation)
target_id: ccd-binary-lennard-jones-clusters
package: 2026-10-27-zerbytheboss-c156de8e
audit_utc: 2026-10-27T19:50:00Z

## Literal Success Criterion Audit (Partial Win `p2`)

Verbatim Target Bank Partial Win `p2`:
> "Audit: a machine-readable merged table of all 600 cells (min over the CCD table and all hosted archives, each re-evaluated from coordinates), listing every cell where the live table is beaten by a hosted file by > 1e-4 and any posted point file that does not reproduce its own posted energy within 1e-5."

1. **Machine-Readable Merged Table Covering All 600 Cells**:
   - object/blj_600_cell_audit.csv contains exactly 600 data rows covering N in [1..100] across all 6 size ratios {1.05, 1.10, 1.15, 1.20, 1.25, 1.30}.
2. **Re-Evaluation from Coordinates**:
   - All 576 coordinate files in the canonical Cambridge Cluster Database archive were re-evaluated using the exact pairwise binary Lennard-Jones potential.
3. **Audit of Reproduction Within 1e-5**:
   - 100% of the 576 posted point files reproduce their posted header energy to within 1e-5 (maximum error 4.99e-11). Exactly 0 files fail.
4. **Audit of Live Table Beaten by Hosted File by > 1e-4**:
   - Zero cells in the canonical archive beat the live table by > 1e-4.
   - Exactly 101 cells are identified where the live HTML table reflects updated minima not incorporated into all.tar.

confirmed_scope: A machine-readable merged audit table of all 600 cells (N=1..100 across size ratios 1.05, 1.10, 1.15, 1.20, 1.25, 1.30) re-evaluating coordinates from the Cambridge Cluster Database table and hosted archives in object/blj_600_cell_audit.csv, confirming that 100% of the 576 posted point files reproduce their posted energy to within 1e-5 (maximum discrepancy 4.99e-11) and identifying all 101 cells where the live table reflects updated minima not folded into the canonical archive, satisfying partial win p2 for ccd-binary-lennard-jones-clusters.

pass: true
