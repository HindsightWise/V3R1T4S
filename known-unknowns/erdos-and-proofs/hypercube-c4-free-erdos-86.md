# C4-free subgraphs of the hypercube (Erdős #86): settle ex(Q7,C4) in [304,308], beat 682 for Q8, or certify a bound below Baber's 0.60318

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (SAT/ILP on Q7, which has 448 edges, with hypercube symmetry breaking; flag-algebra work on the hypercube needs more) · open as of 2026-10-30

## The problem

Let f(n) = ex(Q_n, C4), the most edges in a C4-free subgraph of the n-cube. Erdős asked whether f(n) <= (1/2 + o(1)) n 2^(n-1) ($100, Erdős problem #86, page edited 2025-12-27). Lower bounds: Brass, Harborth and Nienborg (1995), (1/2 + c/sqrt(n)) n 2^(n-1). Upper bounds on limsup f(n)/(n 2^(n-1)): Chung 0.62284, Thomason and Wagner 0.62256, Balogh, Hu, Lidický and Liu (arXiv:1201.0209) 0.6068, and Baber 0.60318, the best published value, quoted by erdosproblems.com/86. Lidický and Volec (arXiv:2610.33850, Section 7, 24 Oct 2026) add that Layman and Lidický claimed, by private communication, a bound below 0.59143, with no public certificate. Exact values (OEIS A245762): 1, 3, 9, 24, 56, 132 for n = 1..6 (a(6) = 132 by Harborth and Nienborg 1994, recomputed by Scheucher and Tabatabai in 2015 with an ILP whose generator script is linked from the OEIS page, without a checkable certificate). Paweł Kwaczyński (OEIS comment, 2026-08-27) gives 304 <= a(7) <= 308 from a(n) <= floor(2n a(n-1)/(n-1)). Minamo Minamoto (arXiv:2603.29127 v5, 28 Aug 2026) gives explicit sets showing ex(Q7,C4) >= 304 and ex(Q8,C4) >= 682 (the OEIS comment still says 680). a(7), a(8) and the asymptotic constant are open as of 2026-10-30.

## What counts as a win

Success means EITHER (a) the exact value of ex(Q7,C4): an explicit C4-free edge set of Q7 with e edges (e >= 304) plus a proof that no C4-free subgraph has e+1 edges, with the computational part certified (LRAT/DRAT checked by cake_lpr or drat-trim, VeriPB, or an exact ILP infeasibility certificate re-verified in rational arithmetic) and any symmetry reduction written out; OR (b) a certified proof that limsup f(n)/(n 2^(n-1)) <= c with c STRICTLY LESS (direction: min) than 0.59143 (the value Layman and Lidický claimed, as reported in arXiv:2610.33850 Section 7) and than any smaller published or claimed constant found at claim time. The proof must be a flag-algebra certificate with exact rational or rigorous interval PSD verification that an independent checker re-runs, or a compiling Lean 4 proof. Bounds are compared with OEIS A245762, erdosproblems.com/86, arXiv:2603.29127 and arXiv:2610.33850, all re-fetched at claim time.

## Partial wins

- **p1:** A new lower bound: an explicit C4-free subgraph of Q7 with at least 305 edges, or of Q8 with at least 683 edges, strictly above the best values in OEIS A245762 and the latest arXiv:2603.29127 at claim time, checked exhaustively for 4-cycles.
- **p2:** A new certified upper bound ex(Q7,C4) <= 307 (or lower, but at least 304), with the same certificate standard as success part (a).
- **p3:** An independently checkable certificate (LRAT/DRAT, VeriPB or exact ILP) that ex(Q6,C4) <= 132. The value is due to Harborth and Nienborg (1994) and was recomputed by Scheucher and Tabatabai (2015) with an uncertified ILP; Minamoto notes it is not independently verified in his paper. Counts unless such a certificate is already public at claim time.
- **p4:** A publicly released certified bound limsup f(n)/(n 2^(n-1)) <= c with c strictly below 0.60318 (Baber, the best published bound), to the certificate standard of success part (b), even if c is not below the unpublished 0.59143, provided no public certificate of such a bound exists at claim time.

## How a win is checked

Parse the edge set, check every edge joins two vertices of Q_n at Hamming distance 1, and check every 4-cycle of Q_n (each is a 2-dimensional subcube: n(n-1)2^(n-3) of them) misses at least one chosen edge. Count edges. For upper bounds, re-run the certificate through its checker and review the encoding and any symmetry-breaking lemma. For an asymptotic bound, recompute the certificate exactly. Re-fetch OEIS A245762, arXiv:2603.29127 and erdosproblems.com/86.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A245762>

## Sources

- <https://www.erdosproblems.com/86>
- <https://oeis.org/A245762>
- <https://arxiv.org/abs/2603.29127>
- <https://arxiv.org/abs/1201.0209>
- <https://arxiv.org/abs/2610.33850>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The 308 upper bound comes from a simple averaging recurrence on a(6); a SAT model of Q7 with the hyperoctahedral symmetry broken should push it down.
- Minamoto relates optimal sets to odd-square edge sets and frustrated spin models; that structure suggests where to seed local search on Q8.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- OEIS comment (680) and arXiv:2603.29127 v5 (682) disagree for Q8; use the larger.
- Erdős's question is asymptotic; finite values settle nothing about it on their own.
- The unpublished Layman-Lidický claim (below 0.59143) is the bar for the full asymptotic win; a public bound between 0.59143 and 0.60318 is only partial win p4.
- Minamoto's g(n) is the maximum of odd-square edge sets, a restricted class; his optimality results for g(7) and g(8) are not upper bounds on ex(Q_n,C4).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/hypercube-c4-free-erdos-86.md
```

Already set up? Say `run V3R1T4S on hypercube-c4-free-erdos-86`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypercube-c4-free-erdos-86`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
