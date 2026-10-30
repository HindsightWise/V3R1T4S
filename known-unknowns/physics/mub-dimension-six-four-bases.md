# MOONSHOT - Four mutually unbiased bases in C^6 (only three known), or a checkable proof that none exist

⚛️ **Physics** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days (numerical search plus certification); a non-existence proof is pure thought or needs cluster for exact certificates · open as of 2026-10-30

## The problem

Two orthonormal bases {a_i}, {b_j} of C^d are mutually unbiased (MUB) if | < a_i|b_j > |^2 = 1/d for all i, j. In prime-power dimensions d+1 MUBs exist (Ivanovic; Wootters and Fields). Dimension 6 is the smallest open case: only triples are known, including infinite families of MUB triplets (Jaming, Matolcsi, Mora, Szollosi and Weiner), and no fourth basis has been found. Numerical searches by Butterley and Hall (quant-ph/0701122) and Brierley and Weigert found no four MUBs. Raynal, Lu and Englert (PRA 83, 062303 (2011), arXiv:1103.1025) maximised the average squared distance D^2 = (1/6) sum_{a < b} [1 - (1/(d-1)) sum_{i,j} (| < a_i|b_j > |^2 - 1/d)^2] over four bases; D^2 = 1 exactly for four MUBs, and their numerical global maximum is 0.9983 (closed form (71 - 3((r^2+12r-3)/(14r))^2)/70, r = (21 sqrt3 - 36)^(1/3), = 0.998291692700...), reached by a two-parameter family plus the identity. A lemma of Chen and Yu (arXiv:1610.04875) on product vectors has a wrong proof, which invalidates three later theorems (McNulty and Weigert, Comment, arXiv:2504.13067, 2025). The McNulty-Weigert review (Quantum 10, 2051, 1 April 2026) gives fourteen equivalent formulations and says no more than three MUBs have been found in d = 6 and that a complete set of seven is unresolved. The complete classification of order-6 complex Hadamard matrices by Cardenes Wuttig and Tindall (arXiv:2608.18053, Aug 2026) states that it does not settle the MUB question. Dimension 10 is also open, with three MUBs known.

## What counts as a win

Success means EITHER (a) four orthonormal bases of C^6 that are pairwise mutually unbiased, given with exact entries (elements of an explicit number field, e.g. cyclotomic or a stated algebraic extension) for which orthonormality and | < a_i|b_j > |^2 = 1/6 for all 6x6 overlaps of every pair of bases are verified exactly, or given to at least 40 significant digits together with a rigorous certificate that an exact solution of the FULL MUB system exists nearby (an interval Newton/Krawczyk certificate counts only for a square, gauge-fixed system, with a proof that the remaining equations follow from it; interval residuals that merely contain zero are not proof); the number of MUBs, 4, is STRICTLY GREATER (direction: max) than the 3 known for d = 6 per the McNulty-Weigert 2026 review (re-fetched before claiming, with an arXiv check for newer papers); OR (b) a proof that no four MUBs exist in C^6, either machine-checked (Lean, Isabelle, Coq) or as an exact algebraic certificate (e.g. rational SOS / Positivstellensatz or Groebner certificate) that an independent tool re-verifies.

## Partial wins

- **p1:** Four orthonormal bases of C^6 whose ASD (Raynal-Lu-Englert Eq. 2-3), computed in mpmath at 50 digits, exceeds 0.998291692700 by at least 1e-10, contradicting the published global numerical maximum.
- **p2:** A machine-checked or exact-certificate proof that no complete set of seven MUBs exists in C^6 (weaker than excluding four), re-verifiable by independent software.
- **p3:** Four pairwise mutually unbiased bases in C^10, certified as in (a).

## How a win is checked

(a) Load the 24 vectors; check exact orthonormality inside each basis and all 36 overlaps for each of the 6 pairs of bases with exact arithmetic (sympy/flint over the stated field), or re-run the existence certificate with an independent implementation (mpmath.iv or Arb), checking that the certified system is square and gauge-fixed and that the argument that the remaining equations follow is valid. (b) Re-run the proof checker or verify the certificate identity exactly. p1: recompute the ASD at 50 digits from the posted bases after normalisation, having first checked that the code gives distance 1 for every pair of a known MUB triple. Literature check against the 2026 review and arXiv.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://quantum-journal.org/papers/q-2026-04-01-2051/>

## Sources

- <https://quantum-journal.org/papers/q-2026-04-01-2051/>
- <https://arxiv.org/abs/1103.1025>
- <https://arxiv.org/abs/quant-ph/0701122>
- <https://arxiv.org/abs/1610.04875>
- <https://arxiv.org/abs/1012.3147>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lift the Raynal-Lu-Englert two-parameter family or the Jaming et al. Fourier-family triplets and search for a fourth basis by Riemannian optimisation on U(6), as a stress test of the 0.9983 ceiling.
- Polynomial optimisation: the Gribling-Polak symmetry-reduced hierarchy for MUBs and Delsarte-type LP bounds are routes to an exact certificate for (b) or p2.
- The 2026 Cardenes Wuttig-Tindall classification of order-6 complex Hadamard matrices gives a complete domain in which to impose the joint compatibility conditions of three Hadamards for (b).
- Product-vector constraints can cut the search space, but check each one against the 2025 McNulty-Weigert Comment (arXiv:2504.13067): some theorems built on Chen and Yu's lemma are invalid.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Near-MUBs: numerically optimised bases with overlap residuals around 1e-8 are not MUBs; given the 0.9983 numerical ceiling, a claimed quadruple without a certificate is almost certainly a bug.
- Conventions: the ASD averages over the k(k-1)/2 pairs; check the formula on a known MUB triple (each pair gives distance 1) before comparing with 0.99829.
- Normalisation and conjugation errors: compute overlaps as conjugate(a).b with unit-normalised vectors.
- Unverified solver claims (numerical SDP values without an exact dual certificate) are not proofs for (b) or p2.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/mub-dimension-six-four-bases.md
```

Already set up? Say `run V3R1T4S on mub-dimension-six-four-bases`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mub-dimension-six-four-bases`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
