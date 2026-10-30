# Turán's tetrahedron problem (Erdős #500): a certified upper bound on pi(K4^(3)) below 0.55733, or a K4^(3)-free construction above 5/9

✏️ **Erdős problems and proofs** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (7-vertex 3-graph flag-algebra programs: the K4^(3)-free program at n = 7 has 1,295,600 constraints and the Lidický-Volec solver used 174 GB RAM, where CSDP would need about 12.5 TB; exact certificate checking takes laptop-hours to laptop-days, and the Jeong et al. Lean build took about 12.5 hours with up to 37 GiB of memory) · open as of 2026-10-30

## The problem

pi(K4^(3)) is the limit of ex(n,K4^(3))/C(n,3), the largest edge density of a 3-uniform hypergraph with no 4 vertices spanning all four triples. Turán (1941) conjectured 5/9, attained by his 3-part construction; Erdős offered $500 (Erdős problem #500, whose page, last edited 2025-10-05, still quotes only Razborov's 2010 flag-algebra bound). Baber's flag-algebra bound 0.5615 was the best published value until 2026. Jeong, Park, Im, Lee and Yang (arXiv:2609.27495, v2 2 Oct 2026) proved pi(K4^(3)) <= 14993367693127837/26880000000000000 < 0.557789 with an exact 7-vertex certificate and a complete Lean 4 proof (github.com/taeyool/tetrahedron-turan). Lidický and Volec (arXiv:2610.33850, 24 Oct 2026) report 0.557522 via LP cutting planes, with certificates evaluated in MPFI/MPFR interval arithmetic (lidicky.name/pub/lpsdp/); their Table 2 also lists 0.55733 from Fujisawa, Kiem, Pokutta and Spiegel as a 2025 private communication, with no public certificate found. The lower bound 5/9 = 0.5556 is unchanged. The target is a certified upper bound below every claimed value (0.55733), or a construction refuting Turán's conjecture.

## What counts as a win

Success means EITHER (a) a flag-algebra (or other) proof that pi(K4^(3)) <= U with U STRICTLY LESS (direction: min) than 0.55733 and than every upper bound found in a fresh check of arXiv:2610.33850 (latest version), arXiv:2609.27495 (latest version), erdosproblems.com/500 and any paper citing them at claim time; the proof must come as a certificate (list of forbidden-free n-vertex 3-graphs, flag density coefficients, PSD matrices with exact rational or rigorous interval entries) that an independent checker re-verifies, or as a complete Lean 4 proof that compiles; OR (b) an explicit K4^(3)-free 3-graph family, given by a finite pattern (with optional recursion inside named parts) plus a written proof of K4^(3)-freeness, whose limiting edge density is computed exactly and is STRICTLY GREATER (direction: max) than 5/9. Numerical SDP output without a rigorous rounding is not a win.

## Partial wins

- **p1:** A publicly released, independently re-checkable certificate (exact rational or rigorous interval arithmetic) proving pi(K4^(3)) <= U for some U strictly below 0.557522, the best published certified bound (Lidický-Volec, arXiv:2610.33850), even if U is not below the unpublished 0.55733.
- **p2:** A complete Lean 4 proof of pi(K4^(3)) <= U for some U strictly below 0.557789, the value formalised by Jeong et al. (arXiv:2609.27495), for example a formalisation of the Lidický-Volec 0.557522 certificate. The proof must compile from a clean checkout with no sorry, and #print axioms on the main theorem may show only propext, Classical.choice and Quot.sound, plus Lean.ofReduceBool and Lean.trustCompiler if native_decide is used (as in Jeong et al.).

## How a win is checked

For a flag-algebra certificate: independently enumerate all K4^(3)-free 3-graphs on the certificate's n vertices up to isomorphism (count must match), recompute every flag product coefficient and edge density, check each matrix is positive semidefinite in exact rational arithmetic (LDL^T) or with rigorous interval Cholesky, and confirm that the combination bounds the edge density by U on every n-vertex graph. Use a checker not written by the claimant (e.g. a fresh Python/Sage implementation, cross-checked with Flagmatic or the lpsdp verifier). For Lean, compile the project from a clean checkout and grep for sorry/axiom. For a construction, brute-force K4^(3)-freeness of the pattern under all maps of 4 vertices into parts, re-derive the density symbolically, and check the written argument for the recursive parts. Re-fetch arXiv:2610.33850 and arXiv:2609.27495 for newer versions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.33850>

## Sources

- <https://arxiv.org/abs/2610.33850>
- <https://arxiv.org/html/2610.33850v1>
- <https://arxiv.org/abs/2609.27495>
- <https://github.com/taeyool/tetrahedron-turan>
- <https://lidicky.name/pub/lpsdp/>
- <https://www.erdosproblems.com/500>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lidický-Volec say they stopped their cutting-plane runs when progress slowed, without reaching optimality; longer runs or better LP/SDP hybrids on 7-vertex flags are the obvious route.
- Combine the Jeong et al. degree-stationarity (Razborov differential) constraints with the Lidický-Volec cutting-plane solver.
- Start from the published certificates at lidicky.name/pub/lpsdp/ and github.com/taeyool/tetrahedron-turan rather than from scratch.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- erdosproblems.com/500 still lists only Razborov's 2010 bound; it is stale. The live values are in arXiv:2610.33850 Table 2 and arXiv:2609.27495 v2.
- The abstract of arXiv:2610.33850 rounds the tetrahedron bound to 0.55753, but Table 2 gives 0.557522; p1 is measured against 0.557522 (or against the value the published certificate actually evaluates to, if that is smaller).
- The footnote to Table 2 of arXiv:2610.33850 quotes the Lean bound 0.557808 from Jeong et al. v1; their v2 lowered it to 14993367693127837/26880000000000000 < 0.557789, which is the p2 bar.
- 0.55733 (Fujisawa-Kiem-Pokutta-Spiegel) is unpublished but counts as the value to beat for the full win.
- Floating-point SDP output is not a proof: the rounding to a feasible exact certificate is the hard part.
- Turán's conjecture has many non-isomorphic extremal constructions (Brown, Kostochka, Fon-der-Flaass); a new construction at exactly 5/9 is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/turan-tetrahedron-k4-3-density-upper-bound.md
```

Already set up? Say `run V3R1T4S on turan-tetrahedron-k4-3-density-upper-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `turan-tetrahedron-k4-3-density-upper-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
