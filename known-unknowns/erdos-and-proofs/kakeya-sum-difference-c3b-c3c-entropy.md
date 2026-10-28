# Kakeya-type sum-difference constants C_3b and C_3c: beat the entropy-certificate lower bounds

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Tao's optimization-constants repository, constants 3b and 3c (Katz-Tao arithmetic Kakeya). C_3b is the least exponent with |A -_G B| <= max(|A|,|B|,|A +_G B|)^{C_3b}; equivalently (entropy form) H(X-Y) <= C_3b max(H(X),H(Y),H(X+Y)) for all discrete random variables X, Y. Every recent lower bound is an explicit finite joint distribution of (X,Y): 3b stands at 1.77898884 (Mosaic Intelligence, 13-point support, independently replayed by Toledo; Lemm 2015 had 1.77898; AlphaEvolve improved the 8th decimal) with upper bound 2 - 1/6. C_3c adds the constraint H(X+2Y): after pull request #221 was merged on 18 Oct 2026 the page record is 1.674894211307116 (Manvir Jaswal, n = 10^20 independent base-55 digits drawn from two laws on 51 and 47 points, independently replayed by Toledo), a jump of 1.6e-4 over Lin's 1.6747338950414058 (147-point support) after months of 1e-11 gains; PR #216 (merged) removed the asterisks on 3b and 3c. Upper bound for 3c: 2 - 1/4. As of 2026-10-28 the only open PR touching these pages (#282) corrects the 3b definition, not a bound. Target: a larger certified lower bound for C_3b (main), or for C_3c beyond the best live value including open pull requests.

## What counts as a win

Success means an explicit integer-valued law for (X,Y) with exact rational probabilities, saved as a file, given EITHER (a) as a finitely supported joint distribution, OR (b) as a product construction X = sum_i b^i X_i, Y = sum_i b^i Y_i of independent digit pairs (X_i, Y_i) drawn from finitely many explicit component laws (each saved as a file with exact rational weights) with stated exact multiplicities, where b >= 2K+1 and K is the largest absolute value taken on any component support by x, y, x+y, x-y (and, for 3c, x+2y), so that every form's digit map is injective and each entropy equals the multiplicity-weighted sum of the component entropies (the mechanism of Jaswal's 3c record, PR #221). The ratio H(X-Y) / max(H(X),H(Y),H(X+Y)) (for 3b; for 3c the max also includes H(X+2Y)) must be certified by outward-rounded interval arithmetic in two independent implementations to be STRICTLY GREATER (direction: max) than the largest lower bound for that constant on the live page (https://teorth.github.io/optimizationproblems/constants/3b.html or .../3c.html) AND in any open pull request at https://github.com/teorth/optimizationproblems/pulls touching that constant, all re-fetched live immediately before claiming, by at least 1e-9 for 3b and 1e-9 for 3c. The entropies are computed from exact pushforward distributions (all collisions in X-Y, X+Y, X+2Y merged exactly) of the finite law in case (a), or of each component law in case (b), where the injectivity bound b >= 2K+1 is also checked exactly. A main win is on 3b; a 3c win must beat the best live 3c value (1.674894211307116 as of 2026-10-28, or any later value or open PR).

## Partial wins

- **p1:** A C_3b certificate that beats 1.77898884 by less than 1e-9 but strictly, under the same exact-pushforward interval verification (an exact sub-threshold record).
- **p2:** A C_3c certificate that beats the live 3c record (1.674894211307116 as of 2026-10-28) by less than 1e-9 but strictly, under the same exact-pushforward interval verification (an exact sub-threshold record).

## How a win is checked

Read the support points and rational weights (for a product construction: each component law, its multiplicity and the base b). Compute pushforwards of X, Y, X+Y, X-Y (and X+2Y) with exact rational masses keyed by exact integer values, per component in the product case, and check b >= 2K+1 exactly. Evaluate -sum p log p with mpmath interval arithmetic (or arb) at 100+ bits in two independent codes, combining component entropies with their exact multiplicities. Compare the ratio's lower endpoint to the live record. Runs in seconds for finite supports (or component supports) up to 10^5 points.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/3b.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/3b.html>
- <https://teorth.github.io/optimizationproblems/constants/3c.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/3b.md>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/3c.md>
- <https://github.com/teorth/optimizationproblems/pull/221>
- <https://github.com/teorth/optimizationproblems/pull/216>
- <https://doi.org/10.5281/zenodo.20794135>
- <https://arxiv.org/abs/2511.02864>
- <https://doi.org/10.5281/zenodo.23289305>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Port the 'two independent digit laws' idea of Jaswal's merged 3c record (PR #221) to 3b: take X, Y as sums of independent scaled copies (base-b digits) of two different small distributions and optimise the pair jointly; entropy is additive under such products only when no carries collide, so search for bases where carries are rare.
- Grow the 13-point support by continuation: start from the published 13-point certificate, add points one at a time on a lattice neighbourhood and re-optimise weights by mirror descent on the ratio (a smooth objective once the max is replaced by a soft-max).
- Cross-domain import (information theory, channel capacity / Blahut-Arimoto): the problem is a max of a ratio of entropies over a polytope of joint distributions; alternating-maximisation updates of Blahut-Arimoto type often find better fixed points than generic gradient methods.
- Cross-domain import (statistical physics): treat log-weights as a field on Z^2 and anneal (parallel tempering) with the ratio as negative energy; low-temperature samples tend to form quasi-periodic, self-similar supports like the record certificates.
- Exploit the known structure behind Lemm's and Ruzsa's constructions (product sets in high dimensions projected to Z) and search over projection vectors rather than point weights.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rounding the weights after optimisation: the claimed ratio must be recomputed from the exact rational weights that are published, not from the floats used in the search.
- Missing collisions: X-Y and X+Y pushforwards must merge equal values exactly; hashing floats of x-y can split one atom into two and inflate H(X-Y).
- Mixing up the constants: 3b uses max(H(X),H(Y),H(X+Y)); 3c adds H(X+2Y); 3a (Gyarmati-Hennecart-Ruzsa, already a separate target) has a different normalisation. A 3c-type distribution scored with the 3b formula is not a 3b record.
- Beating the page while an open pull request already claims more: the bar is the maximum over the page and open PRs.
- Natural log vs log base 2 does not matter for the ratio, but mixing them between numerator and denominator does.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/kakeya-sum-difference-c3b-c3c-entropy.md
```

Already set up? Say `run V3R1T4S on kakeya-sum-difference-c3b-c3c-entropy`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kakeya-sum-difference-c3b-c3c-entropy`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
