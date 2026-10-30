# Regular Hadamard matrix (Menon design) of order 4u^2 with u = 47 (order 8836), the first unknown order

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (structured searches with a prescribed automorphism group; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A Hadamard matrix is regular if all its row and column sums are equal; this forces order n = 4u^2 and row sum +-2u, and is equivalent to a Menon design, a symmetric (4u^2, 2u^2 - u, u^2 - u) design. Whether every even square is the order of a regular Hadamard matrix is open (Kharaghani conjectured that it is; Wikipedia's 'Regular Hadamard matrix' lists the question as unsolved). D. Crnkovic (A series of regular Hadamard matrices, Des. Codes Cryptogr. 39 (2006) 247-251) gave a regular Hadamard matrix of order 4p^2 whenever p and 2p - 1 are prime powers and p = 3 mod 4, which covers p = 7, 31 and 79 (2p - 1 = 13, 61, 157) but not p = 47 (93 = 3*31); Leung, Ma and Schmidt (J. Combin. Theory Ser. A 113 (2006) 822-838) cover some primes p = 7 mod 16, and 47 = 15 mod 16. Shi, Li, Cheng, Crnkovic, Krotov and Sole (Self-dual Hadamard bent sequences, arXiv:2203.16439 v2, June 2022) state that the first unknown order seems to be 4u^2 with u = 47, i.e. 8836. That 2022 sentence is the newest explicit status statement found; no later construction was found in this check. Abelian Menon difference sets of order 4p^2 with p > 3 prime do not exist (McFarland), so a solution cannot be developed over an abelian group; Kronecker products of smaller regular matrices give only even u, and the Bush-type family of Muzychuk and Xiang only u = m^2.

## What counts as a win

Success means an explicit 8836 x 8836 matrix H with entries +-1, H H^T = 8836 I, and every row sum and every column sum equal to the same value 94 or -94, all checked exactly by two independent programs (equivalently the 0/1 incidence matrix of a symmetric (8836, 4371, 2162) or (8836, 4465, 2256) design, checked by computing N N^T = (k - lambda) I + lambda J and N J = kJ), where a same-day arXiv and web search finds no earlier regular Hadamard matrix or Menon design of order 8836 (direction: none; existence target).

## Partial wins

- **p1:** A certified exclusion, not previously published, of regular Hadamard matrices of order 8836 within a precisely stated class (for example those invariant under a stated group of order at least 47 acting semiregularly, or group-developed over a stated non-abelian group of order 8836), with code and logs the skeptic re-runs to the same empty result or a DRAT/LRAT certificate.

## How a win is checked

Check entries +-1, compute H H^T exactly (or verify the design equations for the 0/1 matrix), and check all 2*8836 row and column sums equal the same value +-94, with two independent programs. If the claim is given as a group-developed or orbit-matrix description, expand it to the full matrix with the verifier's own code first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2203.16439>

## Sources

- <https://arxiv.org/abs/2203.16439>
- <https://doi.org/10.1007/s10623-005-3634-3>
- <https://en.wikipedia.org/wiki/Regular_Hadamard_matrix>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Orbit-matrix method (Crnkovic and coauthors): prescribe an automorphism group, solve for the orbit matrix, then refine to the full design.
- Product and Kronecker-type constructions from regular Hadamard or Bush-type matrices of smaller orders, or from symmetric designs with Hadamard parameters over non-abelian groups of order 8836.
- Look for constructions combining a Hadamard matrix of order 188 = 4*47 with a 47-ary structure, as in families giving 4p^2 for special primes p.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The status source is from 2022 ('seems to be'); search carefully for a 2022-2026 construction before claiming.
- Row sums must all be equal (not just constant up to sign per row); normalising a Hadamard matrix by row negations destroys regularity.
- Do not confuse with regular Hadamard matrices of order 196 or 4*47 = 188; the order is 4*47^2.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/regular-hadamard-order-8836.md
```

Already set up? Say `run V3R1T4S on regular-hadamard-order-8836`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `regular-hadamard-order-8836`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
