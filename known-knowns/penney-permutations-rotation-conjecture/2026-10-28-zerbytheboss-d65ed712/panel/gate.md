# Honesty Gate — `penney-permutations-rotation-conjecture`

status: CONFIRMED_PARTIAL
confirmed_scope: Partial win p1: rigorous certification that Bob's right cyclic rotation beats Alice's pattern with Pr(sigma precedes tau) < 1/2 across all 24 permutations in S_4, each certified by an exact big-integer horizon certificate (A(H)+R(H))/H! < 1/2 at H <= 36.

## Gate Audit Summary
- **REPRODUCE (`panel/reproduce.md`)**: `pass: true` (Independent verification of Table 1 calibration; exact 42-digit integer match at H=36 for 2341 -> 1234; exact big-integer horizon certificates (A+R)/H! < 1/2 across all 24 permutations in S_4).
- **NOVELTY (`panel/novelty.md`)**: `pass: true` (Literature proved conjecture only for S_3; arXiv:2404.06585 left S_4 uncertified; TROPHY_CASE.md and open PRs contain zero competing claims; first certified mathematical proof for S_4).
- **CRITERION (`panel/criterion.md`)**: `pass: true` (Satisfies all requirements for partial win p1: Pr(sigma precedes tau) < 1/2 rigorously proved for all sigma in S_4; S_5 and full conjecture remain open, correctly gated as CONFIRMED_PARTIAL).
- **Downgrade Checks**: Zero hedging, zero reproduction mismatches, zero stretched criteria, zero leaks. Final status is CONFIRMED_PARTIAL.
