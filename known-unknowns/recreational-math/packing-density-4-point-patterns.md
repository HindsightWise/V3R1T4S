# Packing densities of 2413, 1342 and 1324: beat a Sliacan-Stromquist or Presutti-Stromquist bound with an explicit permuton or a flag-algebra certificate

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours for lower bounds (optimising a few dozen layer/part sizes with exact or interval evaluation); laptop-days for flag-algebra upper bounds at N = 8 · open as of 2026-10-30

## The problem

The packing density p(S) of a pattern S of length k is the limit over n of the maximum fraction of k-point subsets of a length-n permutation that form a copy of S. For 4-point patterns, 1234, 1432, 2143 and 1243 are solved; three remain open. Current bounds (Jakub Sliacan and Walter Stromquist, 'Improving bounds on packing densities of 4-point permutations', DMTCS 19(2), 2018, Table 3): 0.244054321 < p(1324) < 0.244054540 (lower bound from the layered permuton Gamma with 132-maximiser tails, whose own density is 0.2440543210...; the upper bound is 0.244054549 in Theorem 2 by Flagmatic, sharpened in the same paper to 0.244054540 by the Permpack certificate cert1324permpack.js); 0.198836597 < p(1342) < 0.198837286342 (lower from a 7-part construction Pi whose part sizes are in cert1342lb.txt, and whose own density is 0.198836597...; upper by flag algebras); p(2413) lower bound ~ 0.104724 from the Presutti-Stromquist measure (C. B. Presutti and W. Stromquist, 2010, conjectured optimal) and upper bound 0.10478046354353523761779 (Sliacan-Stromquist, flag algebras at N = 7, in the same range as Balogh et al. 2015). The upper-bound certificates and Sage scripts are public in github.com/jsliacan/permpack. An arXiv search and a citation check of arXiv:1704.02959 on 2026-10-30 found no later paper improving any of these bounds.

## What counts as a win

Success means a strictly better bound for p(2413): either a lower bound strictly above 0.1047245 (this exceeds the density of the Presutti-Stromquist 2010 construction, listed as ~0.104724 in Sliacan-Stromquist Table 3, whatever its later digits), given by an explicitly specified permuton whose 2413-density is evaluated exactly or with certified interval arithmetic, or an upper bound strictly below 0.10478046354353523761779, given by a flag-algebra certificate (rational positive-semidefinite matrices or their rational Cholesky factors) that an exact-arithmetic checker verifies. Floating-point SDP output alone does not count. Re-check arXiv and the permpack repository for newer bounds before claiming.

## Partial wins

- **p1:** A lower bound for p(1324) strictly above 0.244054322 (above the density 0.2440543210... of the Sliacan-Stromquist permuton Gamma itself, so a sharper evaluation of Gamma does not count), from an explicit layered permuton (finite list of layer sizes, possibly with stated recursive or geometric tails) whose 1324-density is evaluated exactly or by certified interval arithmetic.
- **p2:** A lower bound for p(1342) strictly above 0.198836598 (above the density 0.198836597... of the Sliacan-Stromquist construction Pi with the cert1342lb.txt part sizes, so a sharper evaluation of Pi does not count), from an explicit permuton with certified density evaluation.
- **p3:** An upper bound for p(1324) strictly below 0.244054540 (the Permpack certificate cert1324permpack.js) or for p(1342) strictly below 0.198837286342, from an exactly verified rational flag-algebra certificate.

## How a win is checked

Lower bounds: the skeptic writes an independent evaluator of pattern density in a permuton built from blocks (sums, skew sums, inflations of monotone or recursive parts): for block structures this is a finite polynomial (or a convergent series with an explicit tail bound) in the part sizes; evaluate it in exact rationals or interval arithmetic, and cross-check by sampling random 4-point subsets from a large finite approximation (statistical sanity only). Reproduce the Sliacan-Stromquist values for Gamma (1324) and Pi (1342) first. Upper bounds: run an exact checker (permpack's exactify output or a fresh one) confirming the certificate's matrices are PSD over the rationals and that the resulting bound is below the record; reproduce cert2413.js first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1704.02959>

## Sources

- <https://arxiv.org/abs/1704.02959>
- <https://doi.org/10.23638/DMTCS-19-2-3>
- <https://github.com/jsliacan/permpack>
- <https://github.com/jsliacan/permpack/tree/master/certificates>
- <https://arxiv.org/abs/1510.07312>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For 1324 (layered, so a layered maximiser exists by Price 1997), the authors fixed the tails to 132-maximisers and optimised only two parameters; optimising more layers with free sizes is a smooth finite-dimensional problem. An audit run on 2026-10-30 (float64, not certified) reached about 0.2440545239 with symmetric layered permutons having a few free layer sizes per side and a free geometric tail ratio, well above Gamma's 0.2440543210 and about 1.6e-8 below the 0.244054540 upper bound; the work for p1 is to certify such a value.
- For 1342 the authors say the extremal construction might use a different layer formation than their Pi; search over small block structures (inflations of 2-4 point skeletons with recursive parts) numerically, then certify.
- For 2413 upper bounds, move flag algebras to N = 8 with symmetry reduction; the authors stopped at N = 7 for cost reasons.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A finite permutation with high pattern density is NOT a lower bound for p(S): maximum densities decrease with n. Lower bounds need a permuton (or an explicit sequence whose density limit is computed).
- For 1324 the bounds are 0.24405432 vs 0.24405454: margins are 10^-7, so float64 evaluation of a polynomial with cancellation is not trustworthy; use exact or interval arithmetic.
- The flagmatic (digraph) certificate for 1324 relies on Lemma 1 of the paper (an equivalent digraph problem); a new upper bound by that route must state and use the same reduction.
- The published lower bounds are truncations of the densities of Gamma and Pi (0.2440543210... and 0.198836597...). Evaluating Gamma more precisely already gives a number above 0.244054321; that is not an improvement, which is why p1 and p2 set their bars just above the constructions' own densities.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/packing-density-4-point-patterns.md
```

Already set up? Say `run V3R1T4S on packing-density-4-point-patterns`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `packing-density-4-point-patterns`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
