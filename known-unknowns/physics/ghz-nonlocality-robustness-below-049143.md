# Three-qubit GHZ nonlocality robustness: a certified Bell violation at white-noise visibility below 0.49143 (Designolle-Vertesi-Pokutta)

⚛️ **Physics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (Frank-Wolfe search plus exact local-bound computation; symmetry reduction needed beyond about 16 settings) · open as of 2026-10-30

## The problem

For the N-qubit GHZ state mixed with white noise, v|GHZ> < GHZ| + (1-v) I/2^N, the nonlocality robustness v_c is the smallest visibility at which some Bell inequality with finitely many projective measurement settings is violated. For N = 3, Mermin's inequality gives 1/2; Vertesi and Pal (arXiv:1108.1998) found 0.496057 with 5x5x5 settings. Sebastien Designolle, Tamas Vertesi and Sebastian Pokutta (PRA 109, 022205 (2024); arXiv:2310.20677, v3 revised 5 Oct 2026) used symmetry-adapted Frank-Wolfe algorithms (BellPolytopes.jl) with each party measuring a regular m-gon in the XY plane of the Bloch sphere and certified the local bound exactly: N = 3 reaches 0.49143 with m = 22; N = 4: 0.32493 (m = 20); N = 5: 0.20872 (m = 18); N = 6: 0.13422 (16); N = 7: 0.08569 (12); N = 8: 0.05544 (11); N = 9: 0.03521 (10); N = 10: 0.02301 (9) (Table III). With m = 224 they reach 0.49132 for N = 3, but that local bound is out of reach, so it is not a certified value. They also prove the rigorous lower bound v_XY >= 0.49129 for N = 3 when all measurements are restricted to the XY plane, so planar strategies have at most 1.4e-4 left, while strategies using the full Bloch sphere are not bounded that way. These are the best known upper bounds on GHZ nonlocality robustness for 3 to 10 parties.

## What counts as a win

Success means a tripartite Bell functional with rational coefficients and binary outcomes (m_A, m_B, m_C settings), its EXACT local bound L (maximum over all deterministic local strategies, certified as in verification_method), and projective qubit measurements on the three-qubit GHZ state with value Q_GHZ and white-noise value Q_noise, such that the critical visibility v* = (L - Q_noise)/(Q_GHZ - Q_noise), recomputed in exact or 40-digit interval arithmetic, is STRICTLY LESS (direction: min) than 0.49143, the best certified value in arXiv:2310.20677 Table III (re-fetched live before claiming, plus an arXiv check for newer results), by at least 1e-5 (v* <= 0.49142).

## Partial wins

- **p1:** The same certified improvement by at least 1e-5 for N in 4..10 parties over the corresponding certified value in arXiv:2310.20677 Table III (0.32493, 0.20872, 0.13422, 0.08569, 0.05544, 0.03521, 0.02301).
- **p2:** An exact certification of the local bound of one of the arXiv:2310.20677 instances listed as out of reach (e.g. N = 3 with m = 32 or more planar settings), turning its uncertified visibility into a certified one below the Table III value for that N.

## How a win is checked

Recompute the quantum value from the posted measurement angles (exact trigonometric or 40-digit). Compute L: for a full-correlation functional, L = max over a in {+-1}^mA, b in {+-1}^mB of sum_k |sum_ij M_ijk a_i b_j|, so brute force over 2^(mA+mB) is laptop-hours when mA + mB <= 32 in C; for larger instances require a symmetry-reduced orbit enumeration whose correctness is independently re-implemented and agrees, or an exact branch-and-bound certificate re-run with an open solver. For functionals with marginal terms enumerate the third party's best response per setting. Compare v* with the live table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2310.20677>

## Sources

- <https://arxiv.org/abs/2310.20677>
- <https://arxiv.org/abs/1108.1998>
- <https://github.com/ZIB-IOL/BellPolytopes.jl>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Leave the XY plane: the 0.49129 floor only binds planar measurements, so non-planar symmetric configurations (e.g. polyhedral orbits on the Bloch sphere) are the room left.
- Use the paper's orbit-reduction trick to certify local bounds for larger m, as p2 asks.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Heuristic local bounds (a QUBO or Frank-Wolfe value not proven maximal) give an invalid visibility.
- Noise model: the state must be mixed with the maximally mixed state I/8; other noise models are not comparable.
- Uncertified values in Table VI of the paper (large m) are not the record to beat; the certified Table III values are.
- Margins below 1e-5 are within rounding of the published 5-decimal values and are not wins.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/ghz-nonlocality-robustness-below-049143.md
```

Already set up? Say `run V3R1T4S on ghz-nonlocality-robustness-below-049143`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ghz-nonlocality-robustness-below-049143`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
