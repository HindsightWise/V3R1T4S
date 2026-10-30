# Bush-type Hadamard matrices of order 4n^2 with n odd: the first open case n = 7 (order 196)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (block-structured SAT/ILP and orbit-matrix searches; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A Bush-type Hadamard matrix of order 4n^2 is a Hadamard matrix H = [H_ij] partitioned into 2n x 2n blocks of size 2n with H_ii = J (all ones) and H_ij J = J H_ij = 0 for i != j. They exist at order 16n^2 whenever a Hadamard matrix of order 4n exists, but the odd-n case is hard: Bush-type matrices of order 4n^2 with n odd are known only for n = 3 (order 36, Janko 2001), n = 5 (order 100, Janko, Kharaghani and Tonchev 2001) and n = 9 (order 324, Janko, Kharaghani and Tonchev 2001), plus the infinite family of order 4m^4 for every odd m (Muzychuk and Xiang, Proc. Amer. Math. Soc. 134 (2006), arXiv:math/0501026). H. Kharaghani (On the Siamese twin designs) named order 196 = 4*7^2 as the smallest order for which existence is unknown and conjectured existence for all odd n; Crnkovic and Svob (Switching for 2-designs, arXiv:2108.02529 v2, 2022) restate that only n = 3, 5, 9 and the 4m^4 family are known, and no later arXiv paper on Bush-type matrices of these orders was found. Open odd n therefore include 7, 11, 13, 15, 17, 19, 21, 23 (orders 196, 484, 676, 900, 1156, 1444, 1764, 2116; n = 25 is covered by the 4m^4 family). A Bush-type matrix is regular, yields symmetric designs with Hadamard parameters, infinite families of symmetric designs when 2n - 1 or 2n + 1 is a prime power (Kharaghani), and self-dual bent sequences.

## What counts as a win

Success means an explicit 196 x 196 matrix with entries +-1 and H H^T = 196 I, partitioned into 14 x 14 blocks of size 14 with every diagonal block equal to J_14 and every off-diagonal block having all row sums and all column sums zero, checked exactly by two independent programs, where a same-day arXiv and web search finds no earlier Bush-type Hadamard matrix of order 196 (direction: none; existence target). A rigorous non-existence proof for order 196 (exhaustive search with a DRAT/LRAT certificate the skeptic re-checks) also counts.

## Partial wins

- **p1:** A Bush-type Hadamard matrix of order 4n^2 for some odd n in {11, 13, 15, 17, 19, 21, 23} (orders 484 to 2116), not previously published, checked as in the main criterion with blocks of size 2n.
- **p2:** A certified exclusion, not previously published, of Bush-type Hadamard matrices of order 196 within a stated structured class (for example block-negacyclic as in Janko-Kharaghani, or invariant under a stated automorphism group), with code and logs the skeptic re-runs to the same empty result or a DRAT/LRAT certificate.

## How a win is checked

Check entries +-1 and H H^T = 4n^2 I exactly; check each diagonal 2n x 2n block is all ones and each off-diagonal block has zero row and column sums. Use two independent checkers. If a block-circulant or orbit description is given, expand it with the verifier's own code first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2108.02529>

## Sources

- <https://www.cs.uleth.ca/~hadi/research/siamese.pdf>
- <https://arxiv.org/abs/2108.02529>
- <https://arxiv.org/abs/math/0501026>
- <https://web.math.pmf.unizg.hr/glasnik/forthcoming/pGM7107.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Block negacyclic or block circulant structure over Z_14 as in Janko-Kharaghani's order-36 example; reduce to a search over 13 block types.
- Orbit matrices under a prescribed automorphism group of order 7 or 13, then SAT completion (Crnkovic-Svob style).
- Switching (arXiv:2108.02529) only transforms existing Bush-type matrices; it can be used to diversify a found one, not to find the first.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The newest explicit status statement found is from 2022; re-search before claiming.
- Regular Hadamard matrices of order 196 are known (from symmetric (196, 91, 42) designs) but they are not Bush-type unless the block conditions hold.
- The symmetric Bush-type question is a different, murkier problem: sources conflict on whether any symmetric example with n odd is known.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/bush-type-hadamard-odd-n-196.md
```

Already set up? Say `run V3R1T4S on bush-type-hadamard-odd-n-196`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `bush-type-hadamard-odd-n-196`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
