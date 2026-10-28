# Unrestricted binary codes A(n,d), n <= 28: new lower bound in Brouwer's table

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

A(n,d) is the maximum size of a binary code (not necessarily linear) of length n and minimum Hamming distance d. Brouwer's 'Table of general binary codes' (updated version of Best-Brouwer-MacWilliams-Odlyzko-Sloane 1978; page last modified 2026-10-21) gives lower-upper ranges for n=17..28 (even d only, since A(n,2e-1)=A(n+1,2e)), e.g. on 2026-10-28: A(21,10) 42-47, A(22,10) 64-84, A(23,10) 84-150, A(24,10) 136-268, A(25,10) 196-466, A(25,12) 52-55, A(26,12) 65-96, A(27,12) 128-169, A(28,12) 192-288, A(25,8) 4096-5421. Lower-bound improvements since 1978 came from computer searches (Kaikkonen, Ostergard, Laaksonen-Ostergard, Elssel-Zimmermann, Milshtein), and the table is moving fast in October 2026: Kazuki Ota, Takayuki Osa and Tatsuya Harada (arXiv:2610.11609, 8 Oct 2026) gave A(23,10) >= 84, A(25,10) >= 196, A(26,12) >= 65; Oscar Sanchez (email to Brouwer, 2026-10-17) gave A(18,4) >= 6144; Moshe Milshtein (arXiv:2610.23626, 16 Oct 2026) gave (16,3072,3), (17,6144,3), (18,12288,3) and (19,24576,3) codes, i.e. A(17,4) >= 3072, A(18,4) >= 6144, A(19,4) >= 12288, A(20,4) >= 24576; Zhiyang Chen (email, 2026-10-21) gave A(28,12) >= 192, A(21,6) >= 3072, A(27,6) >= 81920, A(28,6) >= 139264. This is the unrestricted A(n,d) table, distinct from the constant-weight A(n,d,w) table already in the bank.

## What counts as a win

Success means an explicit list of M distinct binary words of length n such that an independent script confirms all pairwise Hamming distances >= d (exhaustive over all M(M-1)/2 pairs, bit operations) and M is STRICTLY GREATER (direction: max) than the lower bound for A(n,d) in https://aeb.win.tue.nl/codes/binary-1.html re-fetched live immediately before claiming (the table lists even d only: for odd d compare against the even-d cell A(n+1,d+1), since A(n,d) = A(n+1,d+1)), M does not exceed the table's upper bound for that cell, and no arXiv/journal result found on the day already gives >= M.

## Partial wins

- **p1:** A code meeting the live lower bound for some (n,d) with n in 21..28 that is provably inequivalent to the published code (different distance distribution or automorphism group order), verified exactly.
- **p2:** A strictly improved lower bound for A(n,d) with n = 29..32 (outside the table) beating the best value in the literature (e.g. Kaikkonen's A(29,10) >= 1460), with literature check.

## How a win is checked

Load words as Python ints; check M distinct, all lengths n; pairwise popcount(x^y) >= d via numpy uint32 XOR + popcount (M up to ~10^4 is 5*10^7 pairs, seconds); fetch the live table and parse the cell. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://aeb.win.tue.nl/codes/binary-1.html>

## Sources

- <https://aeb.win.tue.nl/codes/binary-1.html>
- <https://aeb.win.tue.nl/codes/binary.html>
- <https://arxiv.org/abs/1604.06022>
- <https://arxiv.org/abs/2610.11609>
- <https://arxiv.org/abs/2610.23626>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Codes invariant under a prescribed permutation group (Kaikkonen's affine permutation groups; Laaksonen-Ostergard): choose a group G of order 20-500 acting on n coordinates, compute orbits of words, then solve maximum-weight clique on the orbit compatibility graph (Cliquer / KaMIS).
- Unions of cosets of a good linear code (e.g. punctured/shortened BCH or QR codes) selected by clique search on coset representatives.
- Construction X / Plotkin (u|u+v) and concatenation from the best ternary or quaternary codes via Gray maps (Z4-linear codes give nonlinear binary codes beating linear ones, cf. Nordstrom-Robinson).
- Cross-domain import (combinatorial chemistry / max independent set heuristics from graph ML): use ReduMIS / KaMIS evolutionary MIS solvers, which dominate on huge sparse graphs, on the 'distance < d' conflict graph restricted to an orbit space.
- Cross-domain import (statistical physics, hard-core lattice gas): simulated annealing / parallel tempering of a hard-core gas on the hypercube with fugacity schedule, a direct analogue of packing particles.
- Cross-domain import (SAT / exact cover from puzzle solving): Knuth's dancing-links or SAT with symmetry breaking to extend a large partial code by the last few words.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Verify the minimum distance over ALL pairs (nonlinear codes) or all codewords (linear), never by sampling.
- Literature-ahead-of-table trap: Brouwer's pages are updated irregularly but are very active right now (binary table last modified 2026-10-21, ternary and 5-ary 2026-10-17, mixed binary/ternary 2026-10-17, quaternary not since 2017-09-07, with four independent groups sending improvements in October 2026); search arXiv for the specific (n,d) and re-fetch the page immediately before claiming.
- Odd-d cells are equivalent to the even-d cell of length n+1; claim against the correct cell.
- A code for (n,d) obtained by trivially shortening/puncturing a known record is implied by known results, not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/brouwer-binary-unrestricted-a-n-d.md
```

Already set up? Say `run V3R1T4S on brouwer-binary-unrestricted-a-n-d`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `brouwer-binary-unrestricted-a-n-d`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
