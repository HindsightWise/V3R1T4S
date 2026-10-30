# Quaternary Legendre pairs: settle an open even length up to 100 (70, 76, 88, 92, 94 or 100)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (compression and meet-in-the-middle over Gray-mapped rows; checking is instant) · open as of 2026-10-30

## The problem

A quaternary Legendre pair (qLP) of length l is a pair A, B in {1, -1, i, -i}^l with PAF_A(k) + PAF_B(k) = -2 for every shift k = 1..l-1, where PAF_X(k) = sum_j X_j conj(X_{j+k mod l}). Kotsireas and Winterhof introduced them (arXiv:2212.10953): a qLP of length l gives a quaternary Hadamard matrix of order 2l+2 and a binary Hadamard matrix of order 4l+4, and one is conjectured to exist for every even l. Kotsireas, Koutschan and Winterhof (arXiv:2408.16318 v2, 2025) found lengths 28, 30, 32 and 34, and Jedwab and Pender (arXiv:2408.08472 v2; Combinatorial Theory 5(2), 2025) gave infinite families l = (q-1)/2 for prime powers q = 1 mod 4 and l = 2p for odd primes p with 2p-1 a prime power; both 2025 papers leave 14 lengths up to 100 open: 42, 46, 52, 58, 64, 66, 70, 72, 76, 80, 88, 92, 94, 100. N. Lebedev (arXiv:2609.04589, 4 Sep 2026) printed pairs at 42, 46, 52, 58, 66, 72 and 80 and exhausted specific reflection-symmetric search queues at 64, 70 and 76 without finding a pair (explicitly not a nonexistence proof); H. Verma (arXiv:2609.25573, 22 Sep 2026) gave the first pair of length 64. Open at this check: 70, 76, 88, 92, 94, 100 (K. Kumar's NOTES.md in github.com/vatskishan03/Hadamard, October 2026, gives the same list).

## What counts as a win

Success means an explicit pair A, B of a length l in {70, 76, 88, 92, 94, 100} with entries in {1, -1, i, -i} and PAF_A(k) + PAF_B(k) = -2 exactly (Gaussian-integer arithmetic) for every k = 1..l-1, verified by two independent programs, where no qLP of that length is reported at claim time in a fresh arXiv search for 'quaternary Legendre' (direction: none; existence target). A rigorous nonexistence proof for one of these lengths (DRAT/LRAT-checked on a CNF the skeptic regenerates, or an exhaustive search the skeptic re-runs) also counts.

## Partial wins

- **p1:** A certified exhaustion, at l = 70 or 76, of a precisely stated structured family that Lebedev's recorded queues do not cover and that no publication or public note already rules out, with code and logs the skeptic re-runs to the same empty result. Examples: pairs whose four Gray rows are invariant under a stated multiplier subgroup of Z_l^*, or decompositions in which only one Gray-row pair is symmetric about a common integer centre. Families already excluded by a short necessary condition do not count. At l = 70 and 76 the midpoint-frequency identity (the four squared alternating sums of the Gray rows add to 4l + 4) rules out every family in which some Gray-row pair is symmetric about a half-integer centre, because l + 1 = 71 or 77 is not a sum of two squares (Kumar, NOTES.md section 8).

## How a win is checked

Map each symbol to an exponent e in Z_4 (X_j = i^(e_j)). For each shift k, count the residues of e_j - e_{j+k} mod 4 as c0..c3 and form PAF_X(k) = (c0 - c2) + i(c1 - c3), so no floating point is used. Require PAF_A(k) + PAF_B(k) = -2 + 0i for all k = 1..l-1. Sanity check: |sum A|^2 + |sum B|^2 = 2. This is the zero-frequency value; the constant 2l + 2 holds only at nonzero frequencies. Calibrate the checker on Lebedev's printed pair of length 42 (arXiv:2609.04589, digits 0,1,2,3 = 1, i, -1, -i) before use. Use two independent checkers, then search arXiv.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.25573>

## Sources

- <https://arxiv.org/abs/2609.04589>
- <https://arxiv.org/abs/2609.25573>
- <https://arxiv.org/abs/2408.16318>
- <https://arxiv.org/abs/2408.08472>
- <https://arxiv.org/abs/2212.10953>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Gray map (Lebedev): write A = ((p+q) + i(p-q))/2 and B = ((r+s) + i(r-s))/2 with four +-1 rows; the condition becomes a sum of four periodic autocorrelations equal to -4 plus an amicability condition, which holds automatically when each pair (p, q) and (r, s) is symmetric about a common centre.
- Power spectral density filter: |DFT_A(w)|^2 + |DFT_B(w)|^2 = 2l + 2 at every nonzero frequency, and the exact midpoint-frequency constraint at w = l/2; Kotsireas-Koutschan-Winterhof sharpen the PSD test with Galois theory in cyclotomic fields.
- Compression along divisor chains (70 = 2*5*7, 76 = 4*19, 88 = 8*11, 92 = 4*23, 94 = 2*47, 100 = 4*25), then meet-in-the-middle matching of autocorrelation vectors, then lifting with SAT.
- Separate the even- and odd-indexed subsequences (arXiv:2408.16318) to cut the search.
- Kumar's unrefereed note argues from the midpoint-frequency condition that at l = 70 and 76 a qLP needs a Gray-row pair that is not symmetric about a common centre, while a mixed-centre family is possible at 88 and 100 and lies outside Lebedev's queues.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The autocorrelation must conjugate the shifted entry; without the conjugate the -2 condition is a different equation.
- Lebedev's exhaustions at 64, 70 and 76 cover recorded queues only; they are not nonexistence results, and 64 was later found by Verma.
- Lengths 42, 46, 52, 58, 64, 66, 72 and 80 are settled; odd lengths are the binary Legendre pair problem (separate entry).
- FFT checks in floating point are filters, not proofs; the final check must be exact.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/quaternary-legendre-pairs-open-lengths.md
```

Already set up? Say `run V3R1T4S on quaternary-legendre-pairs-open-lengths`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quaternary-legendre-pairs-open-lengths`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
