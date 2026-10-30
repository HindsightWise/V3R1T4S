# Average edit distance of two random binary strings (C_91): a certified bound beating 0.216276 <= alpha_2 <= 0.315514

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days for the lower side (transfer-matrix certificates); the upper side's Lueker-type automata needed 100 GB RAM at h = 17 (Rosenfeld) and grow about 4x per extra h, so h >= 18 needs a large-memory server or symmetry reduction · open as of 2026-10-30

## The problem

alpha_2 = lim e_n/n, where e_n is the expected Levenshtein distance (insertions, deletions, substitutions) between two independent uniform binary strings of length n; the limit exists by subadditivity and alpha_2 <= e_n/n for every n. Upper bounds: Bilardi-Schimd (Information 17 (2026) 685, arXiv:2211.07644) give exact e_n up to n = 24, so alpha_2 <= 0.36932, and M. Rosenfeld (arXiv:2407.18113, 2024) adapted Lueker's automaton method (h = 17) to get 0.315514. Lower bounds: alpha_2 >= 1 - gamma_2 gives 0.178037 from Tomar's gamma_2 <= 0.821963 (2026); Bilardi-Schimd 0.170552; L. Jack (Oct 2026, repository leandrejack-afk/chvatal-sankoff-bound, commit 574220e) 0.216276 from a first-moment count of canonical optimal alignments with an exact rational certificate, proposed as new constant C_91 in teorth/optimizationproblems PR #273 (open, 26 Oct 2026); Jack also gives 0.424710 for k = 4. Monte Carlo at n = 2^15 suggests alpha_2 ~ 0.27496 (Bilardi-Schimd). The gap 0.216-0.316 is wide. Open as of 2026-10-30.

## What counts as a win

CONFIRMED requires a rigorous bound on alpha_2 strictly better than the best rigorous bound at verification time on that side (direction: upper min, lower max), over PR #273 / the 91a page of teorth/optimizationproblems if merged, Jack's repository, Rosenfeld (arXiv:2407.18113 and later versions), Bilardi-Schimd, and any newer arXiv/Zenodo claim; on 2026-10-30 the bars are 0.315514 (upper) and 0.216276 (lower). The improvement must be at least 1e-6 and come with a re-runnable certificate: for an upper bound the automaton, parameter and positive vector checked with outward rounding (or an exact e_n with e_n/n below the bar); for a lower bound an exact rational or outward-rounded transfer-matrix certificate plus a written proof of the counting argument. Monte Carlo estimates never count.

## Partial wins

- **p1:** For an alphabet of size 4, a certified bound on the expected normalized edit distance strictly better (on either side) than the best rigorous value at verification time, counting Jack's 0.424710 lower bound and Rosenfeld's and Bilardi-Schimd's tables.
- **p2:** The exact rational value of e_25 (binary, n = 25), one length past Bilardi-Schimd's exact table, computed by two independent programs that agree and that reproduce the published e_n for n <= 24, provided no exact e_25 is published at verification time.

## How a win is checked

Recompute the certificate independently: for transfer-matrix lower bounds, verify the matrix entries from the stated canonical-alignment rules by exhaustive enumeration on small n, then check A v < v (or the stated inequality) in exact rationals; for upper bounds re-run the automaton check with directed rounding. Calibrate by reproducing Rosenfeld's 0.315514 and Jack's 0.216276 with the same code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/teorth/optimizationproblems/pull/273>

## Sources

- <https://github.com/teorth/optimizationproblems/pull/273>
- <https://arxiv.org/abs/2407.18113>
- <https://arxiv.org/abs/2211.07644>
- <https://github.com/leandrejack-afk/chvatal-sankoff-bound>
- <https://zenodo.org/records/23610945>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lower side: add more local rules to the canonical-alignment normal form (each rule cuts the first-moment count) and re-solve the transfer matrix.
- Upper side: Rosenfeld's h = 17 automaton with symmetry reduction under bit complement and string swap, as Jack did for the LCS case, to reach h = 18-20.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- alpha_2 >= 1 - gamma_2 lower bounds move whenever gamma_2's upper bound moves; recompute the bar from the best gamma_2 bound before claiming.
- The constant is for Levenshtein distance with unit costs; LCS-only (indel) distance is 2(1 - gamma_2), a different constant.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/random-edit-distance-constant-c91-bounds.md
```

Already set up? Say `run V3R1T4S on random-edit-distance-constant-c91-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `random-edit-distance-constant-c91-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
