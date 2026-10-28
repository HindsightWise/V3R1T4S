# Relevant variables of degree-d Boolean functions (C_44): beat the 3/2 lower bound with an explicit function

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Tao's optimization-constants repository, constant 44: R_d is the maximum number of relevant variables of a Boolean function f:{0,1}^n -> {0,1} whose real multilinear degree is at most d, and C_44 = sup_d R_d / 2^d. Upper bounds: 6.614 (Chiarelli-Hatami-Saks 2020), 4.416 (Wellens 2019), 4.394 (Wellens, Discrete Analysis 2022, best published), then two unrefereed exact-certificate refinements of Wellens's recurrence listed with asterisks: 4.3654674227* (BakeLab/Epi, reviewed 11 Sep 2026) and 4.3576549226* (Ricardo Pinho, 23 Oct 2026, degree-three weighted cap 5/4). Lower bound 3/2 from the Chiarelli-Hatami-Saks construction R_d >= 3*2^{d-1} - 2 (also observed by Shinkar and Tal), unchanged on the page as of 2026-10-28. Exact small values: R_3 = 10 (Tarannikov-Kirienko via the translation R_d = p(d+1) to correlation-immune functions, cf. Krotov-Valyuzhenich 2024). Target: an explicit Boolean function f of some degree d with more than 1.5 * 2^d relevant variables, or (partial) a new record R_4 >= 23.

## What counts as a win

Success means an explicit Boolean function f (truth table, or a circuit/decision tree that is expanded to a truth table) on n variables such that (i) its multilinear polynomial over the reals, computed exactly by Mobius inversion of the truth table, has degree d, (ii) all n variables are relevant, and (iii) n / 2^d is STRICTLY GREATER (direction: max) than the lower bound listed on the live page https://teorth.github.io/optimizationproblems/constants/44a.html and in any open pull request touching constants/44a.md at https://github.com/teorth/optimizationproblems/pulls, both re-fetched live immediately before claiming. An infinite family counts if a proof of the recursion is supplied and its base case is checked by computer.

## Partial wins

- **p1:** A degree-4 Boolean function with at least 23 relevant variables (beating the CHS value 22 = 3*2^3 - 2 at d = 4), provided a literature search (correlation-immune / resilient function tables, the quantity p(5)) shows 23 is not already known.
- **p2:** A computer proof that R_4 = 22 (or the exact value of R_4), with a checkable certificate (for example an ILP/SAT unsatisfiability proof with DRAT/LRAT output).

## How a win is checked

Given the truth table on n <= 30 variables, compute the Mobius transform over the reals (integer arithmetic) in O(n 2^n), read off the maximal monomial size, and check each variable appears in some nonzero monomial. Two independent implementations (e.g. numpy and a C bit-sliced version). Seconds to minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/44a.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/44a.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/44a.md>
- <https://arxiv.org/abs/1801.08564>
- <https://arxiv.org/abs/1903.08214>
- <https://arxiv.org/abs/2005.00566>
- <https://arxiv.org/abs/2311.05566>
- <https://eprint.iacr.org/2000/050>
- <https://github.com/rpinho/c44-certificate/tree/f3fb25dfb88de3da8b1a0b30f03fdb51b78ccef9>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search in the correlation-immune world: by the R_d = p(d+1) translation, look for unbalanced perfect colourings / correlation-immune functions of the needed order with more variables, using the Krotov-Valyuzhenich framework and existing tables.
- Composition: study which compositions f(g_1,...,g_k) multiply degree and relevant-variable counts favourably; the CHS construction is a recursion, so a better base case at d = 4 or 5 may lift to all d.
- Cross-domain import (cryptography): resilient and plateaued Boolean functions are designed for spectral constraints that are equivalent to low Fourier degree on subcubes; port cryptographic search tools (e.g. evolutionary search for bent/resilient functions) with degree as a hard constraint.
- Cross-domain import (SAT/ILP): encode 'degree <= 4' as linear constraints on the truth table (all Mobius coefficients of size >= 5 vanish) and maximise the number of relevant variables with an ILP solver on n = 23..25; symmetry-break by assuming invariance under a chosen permutation group to shrink the search.
- Decision-tree view: functions with small decision-tree depth have small degree; search non-read-once trees and sensitivity-style constructions where the degree is less than the depth.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Degree over GF(2) vs over R: the constant uses the real multilinear degree; algebraic degree over GF(2) is different and usually smaller.
- A variable that appears only in cancelled monomials is not relevant; check by Mobius coefficients, not by syntactic occurrence in a formula.
- R_d / 2^d > 3/2 must hold strictly; 3*2^{d-1}-2 approaches 3/2 from below, so matching the CHS family at a larger d is not a win.
- Known values in another language: correlation-immunity tables may already list the value you find; search that literature before claiming p1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/boolean-degree-relevant-variables-c44.md
```

Already set up? Say `run V3R1T4S on boolean-degree-relevant-variables-c44`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `boolean-degree-relevant-variables-c44`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
