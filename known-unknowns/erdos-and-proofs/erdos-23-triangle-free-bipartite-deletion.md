# Erdős #23: a triangle-free graph on 5n vertices needing more than n^2 deletions to be bipartite, or a certified extension of Ferudun's n <= 40 range

✏️ **Erdős problems and proofs** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (flag-algebra SDP for the bound; exact max-cut for counterexample checks) · open as of 2026-10-30

## The problem

Can every triangle-free graph on 5n vertices be made bipartite by deleting at most n^2 edges (Erdős; Erdős-Faudree-Pach-Spencer 1988)? The balanced blow-up of C_5 shows n^2 would be sharp. Balogh, Clemen and Lidický (2021, flag algebras, 'Max cuts in triangle-free graphs', arXiv:2103.14179) prove that deleting at most (2/47)N^2 = 1.0638...n^2 edges suffices for N = 5n vertices, and that N^2/25 suffices for large N when the edge density is at most 0.2486 or at least 0.3197; 1.064n^2 is still the bound on the problem page. Alper Ferudun (arXiv:2606.28041, 26 Jun 2026; computer-assisted, unrefereed, ancillary exact-arithmetic verifier) claims a(5n) = n^2 for every 1 <= n <= 40 (N <= 200): an order-10 flag-algebra certificate bounds the medium density band by 2/25 + delta with an explicit rational delta ~ 4.8558e-5, the tails are transferred to every N by blow-up, and integrality turns beta(G) <= n^2 + (25/2)n^2 delta into beta(G) <= n^2 while (25/2)n^2 delta < 1. n = 41 would need delta < 4.7591e-5, which the paper says its order-10 relaxation does not reach (order 11 is out of reach computationally). The same argument gives beta(G) <= (1/25 + delta/2)N^2 ~ 0.0400243 N^2 for every triangle-free G, far below 2/47, though the paper does not state it as a theorem. OEIS A389646 gives the exact maximum number of deletions needed for N <= 23 vertices (Brendan McKay; a(23) = 20 from a 4,5,4,5,5 blow-up of C_5 plus extra edges); its comment by Ferudun (2026-06-29) records a(5k) = k^2 for k <= 40. Status: open on erdosproblems.com (last edited 2026-01-18, no proof claims).

## What counts as a win

CONFIRMED: (A) an explicit triangle-free graph G on N = 5n vertices with a certificate that its maximum cut has fewer than e(G) - n^2 edges (exhaustive search or an exact branch-and-bound/ILP log for small N, or a rational SDP or LP dual certificate bounding the max cut), triangle-freeness and the cut bound verified independently (Ferudun's arXiv:2606.28041 claims no such G exists for n <= 40, so a graph with n <= 40 also refutes that certificate and is checked with extra care); or (B) a complete proof that n^2 deletions always suffice (machine-checked flag-algebra certificate plus a rigorous rounding argument, or a line-by-line proof).

## Partial wins

- **p1:** A rigorous certificate in exact rational arithmetic (flag-algebra or other, with the PSD and identity checks independently reproduced) that either proves a(5n) = n^2 for every n <= m with m >= 41, beyond Ferudun's n <= 40 (arXiv:2606.28041) and any larger range on the #23 page, thread, OEIS A389646 or arXiv at verification time (on Ferudun's route this means a medium-band delta below 4.7591e-5), or proves that every triangle-free graph on N vertices can be made bipartite by deleting at most c N^2 + o(N^2) edges for an explicit c strictly below 1/25 + delta_F/2 ~ 0.0400243, delta_F being the exact rational of Ferudun's Theorem 3.2, and below any smaller constant posted at verification time.
- **p2:** The exact value A389646(24) (or the next missing term at verification time), with an extremal graph and a reproducible optimality proof (exhaustive enumeration of triangle-free graphs on that many vertices via nauty-type generation, two independent implementations).

## How a win is checked

For (A) recompute max cut exactly with an independent solver (or check the dual certificate in exact arithmetic) and test triangle-freeness. For p1, verify the SDP certificate in exact rationals (positive semidefiniteness via LDL^T over Q) and the flag-algebra identities with independent code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/23>

## Sources

- <https://www.erdosproblems.com/23>
- <https://www.erdosproblems.com/forum/thread/23>
- <https://oeis.org/A389646>
- <https://arxiv.org/abs/2606.28041>
- <https://arxiv.org/abs/2103.14179>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Asymptotic statements (c N^2 + o(N^2)) do not settle the exact n^2 claim for small n; keep (A) and p1 separate.
- Erdős's general odd-girth version (Er92b) is a different statement; only the triangle-free 5n version counts here.
- Blow-ups of C_5 are extremal at n^2 exactly; perturbations must beat it strictly.
- The problem page still shows only Balogh-Clemen-Lidický's 1.064n^2; the live bar is Ferudun's arXiv:2606.28041 (n <= 40, constant ~0.0400243), so a bound between 1/25 + delta_F/2 and 2/47 is not new.
- Ferudun reports that the order-10 per-root-MaxCut envelope is essentially at its ceiling (it cannot reach the 4.7591e-5 needed for n = 41); more solver precision on the same relaxation will not extend the range.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-23-triangle-free-bipartite-deletion.md
```

Already set up? Say `run V3R1T4S on erdos-23-triangle-free-bipartite-deletion`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-23-triangle-free-bipartite-deletion`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
