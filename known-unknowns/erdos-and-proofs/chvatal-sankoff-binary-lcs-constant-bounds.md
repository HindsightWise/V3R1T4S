# Chvatal-Sankoff constant (C_31a): a certified bound on the expected LCS of two random binary strings beating 0.792665992 <= gamma_2 <= 0.821963

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (Lueker-type automata at the frontier need 10^8 to 10^11 states; the binary upper side now needs a cluster or a new idea, the k-ary partial wins fit a big laptop) · open as of 2026-10-30

## The problem

gamma_2 = lim E[LCS(X,Y)]/n for independent uniform binary strings X, Y of length n (Chvatal-Sankoff 1975). The exact value is unknown; simulations suggest about 0.812. Rigorous upper bounds: Lueker (JACM 2009) 0.826280 with his history-length-h automaton at h = 8; L. Jack (2026) 0.825101 (h = 9) and 0.824120 (h = 10), merged on Tao's page 31a and independently replayed by C. Toledo and Jeetu SK (teorth/optimizationproblems PR #249, open); T. S. Tomar (Zenodo 10.5281/zenodo.23610945, v5, 24 Oct 2026) pushed Lueker's method to h = 13 (1.66e11 states after symmetry), gamma_2 <= 0.821963, with h <= 12 kernel-checked in Lean 4 and h = 13 as compiled code. Rigorous lower bounds: Dancik 1994 0.773911, Lueker 2009 0.788071, Heineman-Miller-Reichman-Salls-Sarkozy-Soiffer (arXiv:2407.10925, 2024) 0.792665992. The 0.79970 'lower bound' of Archivara Agent (2026) is a Monte Carlo/Hoeffding estimate, not a proof, and Tao's page labels it so. For larger alphabets Jack (Oct 2026; PR #272, open) reports 0.686509 <= gamma_3 < 0.737495 and 0.617356 <= gamma_4 < 0.679701. Open as of 2026-10-30.

## What counts as a win

CONFIRMED requires a rigorous bound on gamma_2 strictly better than the best rigorous bound found at verification time on that side (direction: upper bound min, lower bound max), taken over Tao's live page https://teorth.github.io/optimizationproblems/constants/31a.html, the open PRs at https://github.com/teorth/optimizationproblems/pulls touching 31a/31b/91, the latest version of Tomar's Zenodo record, and any newer arXiv or Zenodo claim; on 2026-10-30 these bars are 0.821963 (upper) and 0.792665992 (lower). Probabilistic (Monte Carlo/Hoeffding) bounds never count as bars or as wins. The bound must come with a certificate a skeptic re-runs: for Lueker-type upper bounds the automaton (or the code that generates it), z, and a positive vector v with A_z v <= lambda v checked with outward rounding, giving gamma_2 <= 2 log(2z)/log(lambda); for lower bounds the finite-length computation with exact or outward-rounded arithmetic. Improvements must be at least 1e-6 absolute.

## Partial wins

- **p1:** For one alphabet size k with 3 <= k <= 15 (two strings), a certified bound on gamma_k strictly better than the best rigorous value at verification time on that side, counting Jack's Oct 2026 values (repository leandrejack-afk/chvatal-sankoff-bound and PR #272), Rosenfeld (arXiv:2407.18113) and Heineman et al. (arXiv:2407.10925).
- **p2:** An independent, code-disjoint replay of Tomar's h = 11, 12 or 13 certificate (re-deriving the automaton from Lueker 2009 and certifying lambda with outward rounding), or a concrete error in it, recorded with logs; this is credited only while no independent replay of that h is listed on Tao's page or in an open PR.

## How a win is checked

Rebuild the automaton from Lueker 2009 independently, reproduce Lueker's Table II for h <= 8 and Jack's h = 9 value as calibration, then check the claimed positive vector entrywise in directed rounding (or exact rationals) and recompute 2 log(2z)/log(lambda) with interval arithmetic. For lower bounds, rerun the published computation with exact integers. Compare against the bars freshly fetched from the sources named in the criterion.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/31a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/31a.html>
- <https://zenodo.org/records/23610945>
- <https://arxiv.org/abs/2407.10925>
- <https://dl.acm.org/doi/pdf/10.1145/1516512.1516519>
- <https://github.com/leandrejack-afk/chvatal-sankoff-bound>
- <https://github.com/teorth/optimizationproblems/pull/249>
- <https://github.com/teorth/optimizationproblems/pull/272>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lower side: Lueker's lower-bound method with the Heineman et al. memory scheme, plus Jack's symmetry reduction (one stored value per class under alphabet permutation and swapping), which has not been applied to k = 2 at larger n.
- Upper side: instead of raising h uniformly, refine only the automaton states with large eigenvector weight (adaptive histories), keeping a valid domination certificate.
- Store the eigenvector in compressed form and certify A_z v <= lambda v by streaming, as Jack's verify_cert_stream does.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Tao's main table can lag the constant pages and the PR queue: Tomar's 0.821963 was not on the 31a page on 2026-10-30.
- Float power iteration gives a number, not a certificate: the domination A_z v <= lambda v must be checked with directed rounding.
- The Monte Carlo 0.79970 row is not a rigorous lower bound; beating it proves nothing.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/chvatal-sankoff-binary-lcs-constant-bounds.md
```

Already set up? Say `run V3R1T4S on chvatal-sankoff-binary-lcs-constant-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chvatal-sankoff-binary-lcs-constant-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
