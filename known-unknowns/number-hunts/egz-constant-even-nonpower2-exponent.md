# Erdős–Ginzburg–Ziv constants s(C_n^r) for even n that is not a power of two: beat s(C_6^4) >= 85, s(C_6^5) >= 177, s(C_10^4) >= 153 or s(C_6^3) >= 41

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (checking a candidate takes seconds; the search for one takes hours) · open as of 2026-10-30

## The problem

For a finite abelian group G of exponent n, the Erdős–Ginzburg–Ziv constant s(G) is the least l such that every sequence of l elements of G (repetition allowed) has a subsequence of exactly n terms summing to 0. eta(G) is the least l that guarantees a zero-sum subsequence of length 1..n. Harborth (1973) showed s(C_n^r) >= 2^r(n-1)+1 by repeating each vertex of {0,1}^r n-1 times, with equality when n is a power of two. For even n that is not a power of two, Guoqing Wang and Xiangneng Zeng (arXiv:2610.25271, v2 25 Oct 2026) showed this bound is not sharp in every rank r >= 4. They add 2^(r-3)(m-1), where m is the odd part of n, which disproves the Property C problem of Gao-Hou-Schmid-Thangadurai and the Property D conjecture of Gao-Geroldinger. Christian Elsholtz (arXiv:2610.35819, v2 27 Oct 2026; Table 1 and Theorems 1.3/1.4, computer-checked certificates) raised the excess to (m-1)2^(r-3)floor(r/4) in general, and further for n = 2 mod 4. Current lower bounds include s(C_6^4) >= 85, s(C_6^5) >= 177, s(C_6^6) >= 353, s(C_10^4) >= 153, s(C_10^5) >= 321, s(C_12^4) >= 181 and eta(C_6^5) >= 172. In rank 3 only Harborth's 8n-7 is known: s(C_6^3) >= 41 and s(C_10^3) >= 73. Elsholtz reports that a search for n = 6 and 10 found no rank-3 sequence reaching the subgroup value 17q-9 (n = 2q, one light block beyond Harborth's 16q-8), and that the weak form of Property D is open. Find an explicit sequence that beats a current lower bound.

## What counts as a win

Success means an explicit sequence S over C_n^r, given as a list of r-tuples over Z_n with multiplicities, where n is even and not a power of two, 3 <= r <= 7 and n^r <= 10^7. No subsequence of exactly n terms of S may sum to 0, verified by two independent programs. |S|+1 must be STRICTLY GREATER (direction: max) than the best known lower bound for s(C_n^r) at verification time. That bound is the maximum over the formulas and tables of the latest versions of arXiv:2610.35819 and arXiv:2610.25271 (re-fetched immediately before claiming), any certificates the authors have released, and a fresh arXiv search over the last 24 months for 'Erdős–Ginzburg–Ziv' and 'Property D'. Bounds that those sources obtain through product or inductive formulas count toward this bar. Off-by-one: a sequence of length L proves s >= L+1, so C_6^4 needs L >= 85 and C_6^3 needs L >= 41. The claim itself must be an explicit sequence checked as above; a bound derived only by plugging known blocks into a product or inductive formula is not a win.

## Partial wins

- **p1:** Short zero-sums (eta): an explicit sequence over C_n^r (n even, not a power of two, 4 <= r <= 7, n^r <= 10^7) of length L with no zero-sum subsequence of length 1..n, where L+1 strictly exceeds the best known lower bound for eta(C_n^r) in the same sources (for example, beat eta(C_6^5) >= 172), verified by two programs.
- **p2:** Rank-3 weak Property D: a sequence over C_6^3 of length 40 (or over C_10^3 of length 72) with no zero-sum subsequence of exactly n terms in which no element occurs n-1 times, verified by two programs. If s(C_6^3) = 41, this refutes the weak form of Property D, which arXiv:2610.35819 lists as open.

## How a win is checked

Encode the group elements as integers. Run a DP over subsequence size: R_0 = {0}, and for each term g, for j from n-1 down to 0, set R_{j+1} |= R_j + g. The claim fails if and only if 0 is in R_n. The cost is O(|S| * n * n^r) bitset operations, about 10^7 for C_6^5. For the second implementation, group the terms by distinct element and use a count-limited generating function over multiplicities, or meet-in-the-middle. Run both on Harborth's construction, which must pass, and on that construction plus any one extra element, which must fail. For p1, test every length 1..n. Check that every coordinate lies in Z_n and that |S| is the claimed length. Then re-fetch arXiv:2610.35819 and 2610.25271.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.35819>

## Sources

- <https://arxiv.org/abs/2610.35819>
- <https://arxiv.org/abs/2610.25271>
- <https://arxiv.org/abs/2610.21577>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Elsholtz's constructions combine 'heavy' points (multiplicity n-1, on {0,1}^r) with 'light' blocks carrying the odd part m. Search for new light blocks in rank 5 with light density 1/4 for n = 0 mod 4, which Elsholtz asks for explicitly.
- Formulate an ILP or SAT instance over multiplicities on a fixed support (for example {0,1}^r plus a few extra points). The no-n-term-zero-sum condition is checked lazily: solve, test with the DP, add a cut for the zero-sum found, and repeat.
- Use symmetry: GL_r(Z_n) and translations (when n divides the length shift) preserve the property, so search over orbit representatives of supports.
- For rank 3 with n = 6, start from Harborth's 40-term sequence and try to swap one heavy term for a light pair (the rank-3 subgroup-bound gap 17q-9 that Elsholtz mentions).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The records are days old, from two preprints revised within the last week. Re-fetch both and read the latest version before taking any number as the baseline.
- Off-by-one: a sequence of length L proves s >= L+1. Matching a bound is not a record.
- s needs zero-sums of EXACTLY n terms; eta allows any length 1..n. Do not mix the checkers up.
- A sequence over C_n^r is a multiset. Any element with multiplicity n gives an immediate zero-sum, so multiplicities must be at most n-1.
- The C_n^r results for n a power of two are exact (Harborth equality). Do not attack n = 2, 4 or 8.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/egz-constant-even-nonpower2-exponent.md
```

Already set up? Say `run V3R1T4S on egz-constant-even-nonpower2-exponent`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `egz-constant-even-nonpower2-exponent`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
