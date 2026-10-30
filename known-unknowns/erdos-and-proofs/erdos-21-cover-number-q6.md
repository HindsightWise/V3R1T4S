# Erdős #21 small cases (Erdős-Lovász): an intersecting 6-uniform family with cover number 6 and at most 17 edges (best known 18, lower bound 14)

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

Erdős Problem #21 (Erdős-Lovász 1975) asks about q(r), the fewest edges in an r-uniform intersecting hypergraph whose cover number is r (OEIS A391599): no set of r-1 vertices meets every edge. Kahn (1994) proved q(r) = O(r). The Erdős-Lovász lower bound 8r/3 - 3 stood until Sivashankar (arXiv:2606.24878, v1 23 Jun 2026, v2 29 Jul 2026). He proved q(r) >= 3r - 4 for every r by an elementary argument, and q(r) >= ((41 - sqrt 19)/12 - o(1))r, about 3.053r. Exact values: q(3) = 6 and q(4) = 9 (Tripathi 2014), and q(5) = 13. That last value is due to János Barát (J. Combin. Des. 29 (2021) 193-209, arXiv:2011.04444, three examples on 17 vertices). erdosproblems.com and OEIS credit 'Barát and Wanless', but the paper has Barát as its sole author. Barát also showed the q(4) example is unique. For r = 6 the best construction is Barát's 18-line subset of PG(2,5) with cover number 6, the unique optimum among line sets of PG(2,5) (his Corollary 7.5). So 14 <= q(6) <= 18. The erdosproblems page (edited 2025-12-03) still says 13 <= q(6) <= 18, and OEIS A391599 (edited 2026-06-24) lists terms only through q(5). For r = 8 the oval construction ((r^2+r)/2 lines; Aharoni-Barát-Wanless 2016, Lemma 7.1 in Barát's paper) is the set of 36 secant and tangent lines of a conic in PG(2,7). On 2026-10-30 its cover number 8 was re-checked by SAT and again by an exact branch-and-bound search, and no single line can be removed. Barát's exhaustive deletion search in PG(2,7) ran out of storage. His remark that the oval construction suggests m(8) < 28 computes (7^2+7)/2 = 28, which is not the size of the r = 8 oval construction (36), so 28 is not a known value. Sivashankar's bound gives q(8) >= 20.

## What counts as a win

Success means an explicit list of at most 17 distinct 6-element sets (direction: min, strictly below 18) that pairwise intersect and have cover number exactly 6, so that no set of 5 points meets every member. The skeptic checks pairwise intersection directly. The cover number is checked by brute force over all 5-subsets of the vertex set (at most C(102,5), and in practice the vertex count is small), or by SAT with an LRAT-checked UNSAT proof that no 5-cover exists. The skeptic also confirms on https://oeis.org/A391599, https://www.erdosproblems.com/21 and a fresh arXiv check that no value at or below the claimed one is already published. Fewer than 14 edges contradicts Sivashankar's proven bound q(r) >= 3r - 4 and means a bug.

## Partial wins

- **p1:** An explicit 8-uniform intersecting family with cover number 8 and at most 35 edges (lines of PG(2,7) or any other construction), verified as in the success criterion. This beats the 36-line conic (oval) construction and counts only if the skeptic finds no published family of that size or smaller.
- **p2:** A certified lower bound q(6) >= 15 (or the exact value q(6) = 18): a complete proof with the case reductions written out as checkable lemmas, whose computational part ends in LRAT-checked UNSAT certificates or a Lean proof, on CNFs the skeptic regenerates from the published encoding.

## How a win is checked

Check that all sets have size r and are distinct, and that every pair meets. Compute the cover number by exhaustive search over (r-1)-subsets with bitmasks and, independently, by a SAT/ILP minimum hitting set; for UNSAT claims check LRAT proofs with cake_lpr. Re-fetch A391599 and erdosproblems.com/21 and search arXiv for newer small values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A391599>

## Sources

- <https://www.erdosproblems.com/21>
- <https://oeis.org/A391599>
- <https://arxiv.org/abs/2011.04444>
- <https://arxiv.org/abs/2606.24878>
- <https://arxiv.org/abs/1409.4610>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Barát's three q(5) = 13 examples and his 18-line PG(2,5) example; look for non-geometric 6-uniform families on 18-25 vertices with a cyclic or affine symmetry.
- CEGAR search: choose candidate edges as orbit unions, ask a SAT/ILP for a 5-cover, add the cover as a forbidden pattern (some edge must avoid it), and repeat; keep pairwise intersection as hard constraints.
- Use counting constraints from Erdős-Lovász and Sivashankar's proof (degree bounds forced by cover number r) to prune vertex degrees and vertex counts before searching.
- For p1, search subsets of the 57 lines of PG(2,7) under its collineation group, as Barát did for PG(2,5), but with symmetry reduction or SAT instead of storing every intermediate subhypergraph; the 36-line conic set is edge-critical, so start from larger sets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Do not confuse q(r) (cover number r) with q*(r), the smallest maximal intersecting family (no blocking set of size at most r; Dow-Drake-Füredi-Larson, q*(4) = 12); they differ.
- The erdosproblems page still shows the old lower bound 13 for r = 6; the current lower bound is 14 (Sivashankar 2026).
- Barát's 'm(6) = 18' is the optimum within PG(2,5) only, not the global q(6).
- arXiv:2011.04444 / J. Combin. Des. 29 (2021) 193-209 has János Barát as sole author; erdosproblems.com and OEIS A391599 say 'Barát and Wanless'. Cite the paper, not the attribution.
- A family can be pairwise intersecting with cover number r - 1 if some r - 1 points block every edge; always run the full cover-number check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-21-cover-number-q6.md
```

Already set up? Say `run V3R1T4S on erdos-21-cover-number-q6`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-21-cover-number-q6`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
