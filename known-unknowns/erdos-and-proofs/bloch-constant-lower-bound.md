# Bloch's constant B (C_57a): a certified lower bound above Wikstrom's sqrt(3)/4 + 0.0153 = 0.448312701 (claimed upper bound 0.471861652113, Zhang 2026)

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (interval-arithmetic verification of a refined Bonk-type argument) · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 57a. Bloch's constant B is the infimum, over holomorphic f on the unit disc with f'(0) = 1, of the radius of the largest disc onto which some subdomain is mapped univalently. Ahlfors and Grunsky (Math. Z. 1937) proved B <= A_AG = (1/sqrt(1+sqrt 3)) Gamma(1/3)Gamma(11/12)/Gamma(1/4) = 0.4718616534... and conjectured equality. Teng Zhang (arXiv 2610.16808, 12 Oct 2026, unrefereed; Lean 4 formalization generated with Codex at github.com/zhangteng2000/Bloch-constant) claims to disprove that conjecture. Shearing cylinders of a genus-two translation surface tiled by equilateral triangles gives normalized f with B <= b(f) < A_AG exp(-113569/(4*10^13)) < 0.471861652113 < A_AG - 1.3e-9 (Proposition 8.4; the integrals are interval-enclosed in Lemma 8.3). Lower bounds: sqrt(3)/4 = 0.4330 (Ahlfors), sqrt(3)/4 + 1e-14 (Mario Bonk 1990), sqrt(3)/4 + 2e-4 (Huaihui Chen and Paul Gauthier, J. Anal. Math. 1996) and sqrt(3)/4 + 3e-4 (Xiong Chengji 1998). Frank Wikstrom (arXiv 2608.17660, 18 Aug 2026, unrefereed) refined Bonk's method with 'computer-assisted estimates rigorously verified using interval arithmetic' and proved B >= sqrt(3)/4 + 0.0153 = 0.448312701.... The live page still lists Chen-Gauthier and the Ahlfors-Grunsky bound. Open PR #223 (opened 12 Oct 2026; on 26 Oct the maintainer asked for it to be rebased and split) proposes adding Wikstrom's row, and no pull request yet adds Zhang's bound. The interval [0.448312701, 0.471861652113] is open. Known relation: B <= B_l <= L <= B_u (locally univalent Bloch, Landau and univalent Bloch constants; L and B_u are separate entries).

## What counts as a win

Main win: a lower bound B >= b* with b* STRICTLY GREATER (direction: max) than the largest lower bound on https://teorth.github.io/optimizationproblems/constants/57a.html, in any open pull request touching constants/57a.md (currently 0.448312701 from Wikstrom via PR #223), and in any later paper an arXiv search finds, all re-checked immediately before claiming. It needs a complete written proof whose analytic steps follow published lemmas cited precisely (for example Bonk's distortion theorem) and whose every numerical inequality is certified by a supplied interval-arithmetic program. Alternative main win: an upper bound B <= u* with u* STRICTLY LESS (direction: min) than the smallest upper bound on the 57a page, in any open pull request, or in any later paper. That bound is currently 0.471861652113, from Zhang (arXiv 2610.16808, Proposition 8.4). The win must give an explicit normalized f and a complete proof that every univalent disc in f(D) has radius at most u*. Every numerical step must be certified by a supplied interval-arithmetic program, or the whole proof kernel-checked (Lean, Rocq or Isabelle, no sorry or extra axioms). Refuting the Ahlfors-Grunsky conjecture alone no longer counts, since Zhang already claims it.

## Partial wins

- **p1:** An independent interval-arithmetic replay of every numerical inequality in Wikstrom's arXiv 2608.17660 proof, written from the paper without the author's code. It ends in either confirmation or a specific inequality and parameter value where the claimed bound fails, with a rerunnable script.
- **p2:** An independent interval-arithmetic replay of Zhang's numerical enclosure (arXiv 2610.16808, Lemma 8.3: q_C in (-370/10^6, -337/10^6)) and of the scalar comparisons in Proposition 8.4, written from the paper without the author's code or Lean files. It ends in confirmation or a specific failing step, with a rerunnable script.

## How a win is checked

Skeptic: map every analytic step to the published lemma it cites, then rerun the interval program at two working precisions (for example Arb at 30 and 60 digits). Every box or case in the cover must be closed, and the union of boxes must cover the full parameter domain, which is checked by a separate covering script. Expected: hours.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/57a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/57a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/57a.md>
- <https://arxiv.org/abs/2608.17660>
- <https://arxiv.org/abs/2610.16808>
- <https://github.com/zhangteng2000/Bloch-constant>
- <https://github.com/teorth/optimizationproblems/pull/223>
- <https://doi.org/10.1007/BF02787110>
- <https://doi.org/10.4153/S0008439523000346>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Wikstrom's jump from +3e-4 to +0.0153 came from making Bonk's estimates computer-assisted; tighten the same chain with finer case splits and higher-order distortion estimates.
- Optimisation import: write the extremal problem over the low Taylor coefficients of a Bloch function as a semidefinite or moment relaxation, as Wikstrom did for Landau's constant, and certify the dual.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The Ahlfors-Grunsky value 0.4718616534... is no longer the upper-bound comparator: Zhang (arXiv 2610.16808, unrefereed) claims B < 0.471861652113, so an explicit f that merely beats the Ahlfors-Grunsky value is not a record.
- The page table still shows Chen-Gauthier (sqrt(3)/4 + 2e-4); beating that alone is not a record, since the comparator is Wikstrom's 0.448312701.
- Confusing Bloch's constant (univalent subdisc) with Landau's constant (any disc in the image) or the locally univalent constant B_l.
- Floating-point LP or SDP solutions are discovery tools, not certificates; the dual must be re-verified in rigorous arithmetic.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/bloch-constant-lower-bound.md
```

Already set up? Say `run V3R1T4S on bloch-constant-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bloch-constant-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
