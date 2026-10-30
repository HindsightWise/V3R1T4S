# Fraenkel's N-heap Wythoff conjectures: prove the three-heap case with smallest heap 11 (Sun-Zeilberger stopped at 10)

🕸️ **Graphs, games and automata** · standard · tractability ★★★★☆ · compute: laptop-hours (P-position tables for a fixed smallest heap, plus a check of Sun-Zeilberger's eight finite conditions) · open as of 2026-10-30

## The problem

In Fraenkel's N-heap Wythoff game a move removes tokens from one heap, or removes (a_1, ..., a_N) from all heaps with 0 <= a_i <= p_i, sum a_i > 0 and a_1 xor ... xor a_N = 0; the last player to move wins (N = 2 is Wythoff's game). Fix the N - 2 smallest heaps K. Fraenkel conjectured (1) that from some m(K) on, the n-th P-position has A_n^N = A_n^(N-1) + n with A_n^(N-1) = mex({A_i^(N-1), A_i^N : i < n} union T) for a small set T, and (2) that A_n^(N-1) = floor(n*phi) + eps_n + a with eps_n in {-1, 0, 1}. Fraenkel and Krieger, and Sun (Discrete Math. 300, 2005), proved that (1) implies (2), along with structural results for N = 3. Xinyu Sun and Doron Zeilberger (Ann. Comb. 8 (2004) 225-238) gave a finite sufficient condition: their Claim 3.5, which asks for integers n2 < n1 beyond a computable N satisfying eight checkable conditions on the P-positions. With it they proved both conjectures for N = 3 when the smallest heap A1 is at most 10, listing T, S, alpha, N1 and N2 for each case in their Table 1. Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem A4) still lists only these cases as proved, and no 2026 arXiv math.CO title extends them.

## What counts as a win

CONFIRMED: both of Fraenkel's conjectures for N = 3 with smallest heap A1 = 11 (or any larger single value, once 11 is done). The proof gives explicit integers n2 < n1 and the derived constants (T, S, alpha, N1, N2, N3 and the set S1(n1) of Claim 3.3) satisfying every hypothesis of Sun and Zeilberger's Claims 3.4 and 3.5. Their Table 1 supplies T, S, alpha, N1 and N2 for the cases i < 11 but not N3, so the claim must also state N3^i and B^i_{N3^i} for every i < 11, recomputed. A program that shares no code with the claimant's must check this by recomputing the P-positions directly from the game rules. A general proof for all A1, formalised in Lean 4, Coq or Isabelle, also counts. The case must not be published as proved at verification time (GONC Unsolved Problems column, arXiv, journals citing Sun-Zeilberger).

## Partial wins

- **p1:** An independent recomputation of Sun and Zeilberger's Table 1 (T, S, alpha, N1, N2 for A1 = 0..10) from the game rules, by a program that shares no code with their Maple package, confirming every entry or demonstrating an error.

## How a win is checked

Compute the P-positions (A1, A_n^2, A_n^3) for a fixed A1 by a direct mex/retrograde construction from the rules, not from the conjectured recurrences, and cross-check small cases by brute-force game search. Then evaluate each condition of Claims 3.4 and 3.5 for the claimed n1 and n2. This includes N3^i for every i < 11, and membership in S1(n1) decided by the three rules of Claim 3.3; the third rule checks a window of length p(m) = 2^(floor(log2 m) + 1), which is 16 for m = 11, using the periodicity of (a xor b) - b. Finally compare the constants with the claim.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Sources

- <https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/wythoff.html>
- <https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimPDF/wythoff.pdf>
- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Sun and Zeilberger's epilogue says a numerical rather than symbolic implementation could improve performance, provided Claim 3.3 (deciding membership in S) is redone without generating functions. The periodicity of (a xor b) - b with period p(m) makes that a finite check. A C program for the P-position table and the eight conditions should then handle A1 = 11..20 quickly.
- Their Table 1 shows the thresholds N1 and N2 growing into the hundreds by A1 = 10, so allow n1 in the tens of thousands.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Sun and Zeilberger's notation differs from Fraenkel's: their [a, b, c] is the position with heaps a, a + b and a + b + c, and some signs are reversed. State the convention.
- Claim 3.5 needs N1, N2 and N3 for all smaller first heaps, and Table 1 omits N3, so a gap in the chain for some i < 11 invalidates the argument.
- A pattern seen in a long table is not a proof; only the eight conditions (or a formal proof) count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/three-heap-wythoff-fraenkel-a1-11.md
```

Already set up? Say `run V3R1T4S on three-heap-wythoff-fraenkel-a1-11`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `three-heap-wythoff-fraenkel-a1-11`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
