# Honesty Gate — `ab-offlattice-protein-3d-best-energies`

status: CONFIRMED_SOLUTION
confirmed_scope: An explicit 87-angle conformation and 46-residue 3D Cartesian coordinate set in object/1CRN_L46_negE95.720530.json for the standard crambin benchmark sequence 1CRN (L = 46, BBAAABAAABBBBBAABAAABABAAAABBBAAAAAAAABAAABBAB) in the 3D AB off-lattice protein model achieves energy E* = -95.720529801173 (-E* = 95.720529801173, E_bb = 1.626304826130, E_lj = -97.346834627302) verified in both float64 and 50-digit arithmetic with all 45 unit bond lengths exact within 2.22e-16 and angle-space gradient norm ||grad E||_2 = 4.72e-12 < 1e-8 (||grad E||_inf = 1.52e-12 < 1e-8), improving on the best published energy -E = 95.3159 in Table 10 of Boskovic and Brest (arXiv:1903.01456) by +0.404630 energy units alongside a complete independent reproduction and discrepancy audit of all 23 published conformations in Tables 11 and 12 (identifying the Table 2 1PCH sequence-length discrepancy L = 87, D = 169 vs printed L = 88, D = 171).

## Gate Audit Summary
- **REPRODUCE (`panel/reproduce.md`)**: `pass: true` (fresh subagent invocation; independent verifier written from mathematical definition before inspecting package checker; exact SHA-256, 50-digit `mpmath` energy, unit bond lengths, angle-space gradient norm, and positive-definite 87x87 Hessian verified).
- **NOVELTY (`panel/novelty.md`)**: `pass: true` (fresh subagent invocation; single honest HTTP 200 fetches with zero retries across `arXiv:1903.01456`, Cambridge Cluster Database, 2024-2026 literature, `TROPHY_CASE.md`, and all open/merged pull requests).
- **CRITERION (`panel/criterion.md`)**: `pass: true` (fresh subagent invocation; literal verification against `bank/targets.json` full `success_criterion` and partial win `p2`).
- **Downgrade Checks**: Zero hedging panelists, zero reproduction mismatches, zero stretched criteria, zero path or secret leaks. Final status is `CONFIRMED_SOLUTION`.
