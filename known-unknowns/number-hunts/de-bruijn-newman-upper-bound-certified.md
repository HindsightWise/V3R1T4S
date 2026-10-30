# de Bruijn-Newman constant: a certified upper bound below every claim on Tao's C_21 page (refereed record 0.2; unrefereed claims down to 0.107964910079)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (interval-arithmetic barrier and finite-region checks; pushing the verified RH height would need a cluster) · open as of 2026-10-30

## The problem

Tao's optimization-constants repository, constant 21: the de Bruijn-Newman constant Lambda is the threshold such that H_t(z) = integral_0^inf e^{t u^2} Phi(u) cos(zu) du has only real zeros exactly when t >= Lambda. RH is equivalent to Lambda = 0, and Brad Rodgers and Terence Tao (Forum Math. Pi 2020) proved Lambda >= 0. Refereed upper bounds: 1/2 (de Bruijn 1950), < 1/2 (Ki, Kim and Lee 2009), 0.22 (D.H.J. Polymath 2019, arXiv 1904.12438) and 0.2 (Dave Platt and Tim Trudgian 2021, arXiv 2004.09765, from RH verified to 3e12). Since 2026 the live page has carried unrefereed, asterisked certificate packages: 0.1965 and 0.1875 (Mosaic Intelligence), 0.172422 (Daniel Martin Kornaus, Zenodo 22658444), and 0.16 and 0.1595 (Mosaic Intelligence). The README cell reads '0.2 (0.1595*)'. Open pull request #291 (updated 30 Oct 2026) proposes six more asterisked rows: 0.163297, 0.149396, 0.116398 and 0.107964910079 (Raymond, Zenodo), 0.13963 (Hakimoglu-Brown, arXiv 2610.12803) and 0.148612 (Planat, arXiv 2610.18214). Three of them import an unrefereed theorem from an OpenAI preprint (zeta has no zeros with Re s > 7/8). The page says none of its post-2021 rows has been independently replayed. The PR reports that Planat reproduced the finite comparisons behind 0.149396 and 0.116398 (arXiv:2609.37164v2 Section 8; arXiv:2610.18214 Appendix A), and notes that a numerical replay does not validate the analytic foundation. Two kinds of work are useful and checkable: a bound below all claims that rests only on refereed inputs, and an independent replay that confirms or refutes a claimed package.

## What counts as a win

Main win: an unconditional bound Lambda <= t* with t* STRICTLY LESS (direction: min) than the smallest upper bound on https://teorth.github.io/optimizationproblems/constants/21a.html, in every open pull request touching constants/21a.md (currently 0.107964910079 in PR #291), and in any paper, preprint or Zenodo deposit found by a fresh check, all re-fetched immediately before claiming. The bound must come with (a) a written argument naming each input theorem by its exact published statement, every input being refereed (no unrefereed imported theorem, no RH beyond a verified height, no GRH or other hypothesis); and (b) a supplied program that certifies every numerical inequality in interval or exact arithmetic (barrier winding number, finite-region zero exclusion, tail and error bounds). A skeptic reruns (b) and finds no failure.

## Partial wins

- **p1:** An independent from-scratch interval-arithmetic replay of the finite certificate of one asterisked row on the live page or in PR #291 for which no replay has been reported. This excludes 0.149396 and 0.116398, which Planat reports reproducing. Examples are Mosaic Intelligence 0.1875 and Kornaus 0.172422. The replay must use code that shares nothing with the claimant's bundle. It ends either in agreement with every stated certified inequality, or in a concrete parameter point (t, x, y) where a claimed certified inequality fails, with a rerunnable script that shows the failure.
- **p2:** A rerunnable interval-arithmetic replay bundle, written independently of the Polymath 15 code (github.com/km-git-acc/dbn_upper_bound), reproducing the refereed 0.2 bound of Platt-Trudgian (or Polymath's 0.22) from the published parameters, taking RH up to 3e12 (Platt-Trudgian) as the only cited input and certifying every other numerical step (barrier, finite-region and tail estimates).

## How a win is checked

Skeptic: check the provenance of every cited input (journal version, exact statement). Rerun the certificate program with python-flint/arb or Arb at two working precisions. Spot-check the effective approximation of H_t (the Polymath A + B - C form with error terms) against direct quadrature at 20 random points. Recompute the final arithmetic from the certified parameters. For p1, rerun the claimant's replay and any reported failing point with an independent evaluator.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/21a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/21a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/21a.md>
- <https://github.com/teorth/optimizationproblems/pull/291>
- <https://arxiv.org/abs/1904.12438>
- <https://arxiv.org/abs/2004.09765>
- <https://arxiv.org/abs/1801.05914>
- <https://zenodo.org/records/22658444>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the refereed Polymath-15 barrier framework and optimise its parameters (t0, y0, barrier location X) with certified evaluation; the framework's limits show what new analytic input any lower bound needs.
- Rigorous-numerics import: the argument principle on a rectangle needs a certified lower bound on |H_t| along the contour; use Taylor models in t and x rather than dense meshes.
- Formal-methods import: a Lean statement of the barrier lemma with numerics discharged by an external certificate would end the refereed-versus-asterisk ambiguity.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Comparing against the README cell '0.2 (0.1595*)' instead of the smallest claim in open PR #291 (0.107964910079 as of 2026-10-30).
- Importing an unrefereed theorem (the 7/8 zero-free claim, or an asterisked package used as a starting row) makes the bound conditional; under this criterion it does not count.
- Floating-point winding numbers on a coarse mesh can miss zeros; every contour step needs a certified lower bound on |H_t|.
- Lambda >= 0 is proven, so a computation suggesting Lambda <= 0 points to a bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/de-bruijn-newman-upper-bound-certified.md
```

Already set up? Say `run V3R1T4S on de-bruijn-newman-upper-bound-certified`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `de-bruijn-newman-upper-bound-certified`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
