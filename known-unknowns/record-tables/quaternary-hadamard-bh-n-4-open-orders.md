# Quaternary Hadamard matrices BH(n,4): settle an open even order below 2000 (smallest 334, then 438, 446, 478)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (bordered and plug-in arrays, multiplier-orbit searches, SAT/CP-SAT; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A quaternary (Butson) Hadamard matrix BH(n,4) is an n x n matrix with entries in {1,-1,i,-i} and H H* = nI. Seberry conjectured that one exists at every even order (Problem 8 of Egan, Kotsireas, London and O Cathain, arXiv:2610.27175, 2026); this implies the Hadamard conjecture, since a BH(n,4) gives a real Hadamard matrix of order 2n (Turyn). V. Zaitsev's page 'Quaternary Hadamard matrices' (with H. Kharaghani, A. Mohammadian and B. Tayfeh-Rezaie; last updated 14 October 2026, re-fetched 2026-10-30) lists 115 even orders below 2000 with no known BH(n,4): 334, 358, 418, 438, 446, 478, 498, 502, 506, 550, ... 1990. Recent progress: F. Szollosi settled 94 (arXiv:2603.09572); Kharaghani, Mohammadian, Tayfeh-Rezaie and Zaitsev found 118, 130, 134, 206 and 266 from near-Williamson matrices (arXiv:2605.08661); the page authors added many more. K. Kumar (github.com/vatskishan03/Hadamard, complex-hadamard/, October 2026) gives BH(n,4) at six orders still on Zaitsev's list: 358, 418, 498 (character-bordered and Paley plug-in arrays) and 1286, 1718, 1910 (quaternary conference matrices), leaving 109 open orders below 2000, the smallest 334, 438, 446, 478, 502, 506, 550. Kumar's README states 334 is the smallest open quaternary order and reports exhaustive structured searches that failed there. A BH(1198,4) would also give the smallest open real Hadamard order 2396.

## What counts as a win

Success means an explicit n x n matrix with entries in {1,-1,i,-i} (stored as exponents 0..3 of i) with H H* = nI checked exactly over Z[i] by two independent programs, for an even n < 2000 that is on the live unknown list of https://www.cs.uleth.ca/~zaitsevv/quaternary.html (re-fetched immediately before claiming) and is not settled by any other public source at claim time: not in the complex-hadamard/ folder or README of github.com/vatskishan03/Hadamard, not in the latest version of arXiv:2610.27175 or arXiv:2605.08661, and not found by a same-day arXiv/GitHub search for BH(n,4) at that order (direction: none; existence target). A non-existence proof for one listed order also counts if it is machine-checked (Lean, Isabelle or Coq) or its computational part (exhaustive search with logs, or a DRAT/LRAT certificate for a CNF the skeptic regenerates) is re-run by the skeptic to the same result.

## Partial wins

- **p1:** A certified exclusion, not previously published, of BH(334,4) within a precisely stated structured class (for example a stated bordered or block-circulant array with a stated multiplier group, beyond the classes Kumar's search/NOTES.md already reports as excluded), with a DRAT/LRAT or CP-SAT certificate or an exhaustive search the skeptic re-runs to the same empty result.

## How a win is checked

Read the matrix as exponents e_rj in Z_4. For each pair of rows r != s count c_m = #{j : e_rj - e_sj = m mod 4}; the Hermitian inner product is (c0 - c2) + i(c1 - c3), so orthogonality holds exactly when c0 = c2 and c1 = c3. Check all pairs with two independent programs (no floating point). Optionally build the real Hadamard matrix of order 2n by Turyn's map and verify H H^T = 2nI. Then confirm the order is on Zaitsev's live list and absent from Kumar's complex-hadamard folder and the papers named.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.cs.uleth.ca/~zaitsevv/quaternary.html>

## Sources

- <https://www.cs.uleth.ca/~zaitsevv/quaternary.html>
- <https://github.com/vatskishan03/Hadamard/blob/main/complex-hadamard/README.md>
- <https://arxiv.org/abs/2610.27175>
- <https://arxiv.org/abs/2605.08661>
- <https://arxiv.org/abs/2603.09572>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Szollosi's modified Kharaghani-Seberry block array over circulants of order n/2 (how BH(94,4) was found); for n = 2p with p prime try multiplier-invariant circulants.
- Near-Williamson quadruples (A circulant, B, C, D symmetric circulant) of odd order w give BH(2w,4); arXiv:2605.08661 v2 (Sep 2026) classifies them for odd w <= 47 and shows existence for every odd w <= 69.
- Character-bordered arrays over abelian groups of order n/2 (Kumar's route to 358 and 498) and quaternary conference matrices of order (n+2)/2 or similar plug-ins.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Zaitsev's list (14 Oct 2026) lags: 358, 418, 498, 1286, 1718 and 1910 are on it but have explicit matrices in Kumar's repository.
- Use the conjugate transpose: H H^T = nI over the complex numbers is the wrong test.
- A quaternary conference matrix or a real Hadamard matrix of order 2n is not itself a BH(n,4).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/quaternary-hadamard-bh-n-4-open-orders.md
```

Already set up? Say `run V3R1T4S on quaternary-hadamard-bh-n-4-open-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quaternary-hadamard-bh-n-4-open-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
