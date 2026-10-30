# Steiner systems S(2,6,v): settle one of the 27 undecided admissible v (smallest 51), or an undecided case with block size 7, 8 or 9

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (difference-family or orbit-prescribed exact-cover search; checking a design takes laptop-seconds) · open as of 2026-10-30

## The problem

A Steiner system S(2,k,v) is a family of k-subsets (blocks) of a v-set such that every pair of points lies in exactly one block; v is admissible when k-1 divides v-1 and k(k-1) divides v(v-1). For k <= 5 every admissible v is realised (Hanani); for k >= 6 Wilson's theorem gives existence only for large v. For k = 6 (v = 1 or 6 mod 15), S(2,6,36) is excluded by Bruck-Ryser and S(2,6,46) by computer search, and the Handbook of Combinatorial Designs (2nd ed., 2007) lists 29 undecided values: 51, 61, 81, 166, 226, 231, 256, 261, 286, 316, 321, 346, 351, 376, 406, 411, 436, 441, 471, 501, 561, 591, 616, 646, 651, 676, 771, 796, 801. Banakh, Hetman and Ravsky (arXiv:2511.05191 v3, 18 May 2026) found seven 1-rotational S(2,6,226) over (Z5 x Z5 x Z3) ⋊ Z3 with a fixed point and six point-transitive S(2,6,441) over (Z7 ⋊ Z3) x (Z7 ⋊ Z3), leaving 27 undecided. For k = 7 the Handbook lists 21 undecided v; I. Hetman settled 505 and 589 (arXiv:2604.04975 v4, 12 Oct 2026) and names S(2,7,127) and S(2,7,211) as undecided (arXiv:2511.20708 v3, Feb 2026). For k = 8 and 9 the Handbook lists 38 and 91 undecided v; Hetman settled S(2,8,225) and S(2,9,289) (arXiv:2509.10673 v4) and S(2,9,369), which by recursion also gives S(2,9,3321) (arXiv:2511.20708). All of these 2025-2026 results came from computer searches with prescribed automorphism groups; Hetman publishes the block files in github.com/Ihromant/math-utils.

## What counts as a win

Success means an explicit S(2,6,v) for v in {51, 61, 81, 166, 231, 256, 261, 286, 316, 321, 346, 351, 376, 406, 411, 436, 471, 501, 561, 591, 616, 646, 651, 676, 771, 796, 801}: exactly v(v-1)/30 blocks, each a 6-subset of a v-set, with every one of the v(v-1)/2 pairs in exactly one block, checked exhaustively by two independent programs on the full block list (base blocks plus a group count only after the verifier expands them with its own code), where no S(2,6,v) for that v is reported at claim time in the latest version of arXiv:2511.05191, in Hetman's later papers or in a fresh arXiv search (direction: none; existence target).

## Partial wins

- **p1:** An explicit S(2,7,127) or S(2,7,211) (v(v-1)/42 blocks of size 7, every pair exactly once), checked as in the main criterion, with no S(2,7,v) for that v reported at claim time.
- **p2:** An explicit S(2,k,v) with k in {7, 8, 9}, checked as in the main criterion, for another admissible v that an openly accessible source states to be undecided. The source must be an arXiv paper or a maintained online table, cited by URL in the claim. The settled 505 and 589 (k = 7), 225 (k = 8), and 289, 369 and 3321 (k = 9) do not count, nor does any v settled since. A value whose undecided status is documented only in the printed Handbook does not qualify.
- **p3:** A complete, independently re-run proof that no S(2,6,51) has an automorphism of a stated prime order p (or that none is 1-rotational or point-transitive over a stated group), where that exclusion is not already published; delivered as a DRAT/LRAT-checked proof on a CNF the skeptic regenerates, or as exhaustive search code and logs the skeptic re-runs.

## How a win is checked

Read the blocks; check each has k distinct points in range and that there are v(v-1)/(k(k-1)) of them. Build a v x v pair-count table and require every off-diagonal entry to be exactly 1. For designs given as difference families, expand every base block under the stated group (plus the fixed point for 1-rotational designs) with the verifier's own group arithmetic before counting; the shortcut that base-block differences partition the group is valid only for full regular orbits. Use two independently written checkers, then search arXiv and Hetman's repository for that v.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2511.05191>

## Sources

- <https://arxiv.org/abs/2511.05191>
- <https://arxiv.org/abs/2604.04975>
- <https://arxiv.org/abs/2511.20708>
- <https://arxiv.org/abs/2509.10673>
- <https://arxiv.org/abs/2507.16009>
- <https://github.com/Ihromant/math-utils>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- 1-rotational designs: a group of order v-1 acting on itself plus one fixed point, with base blocks whose differences cover each non-identity element once, as for S(2,6,226). For v = 51, 81 and 256 try all groups of order 50, 80 and 255 from the GAP small-groups library.
- Point-transitive designs over non-abelian groups of order v, as for S(2,6,441) over (Z7 ⋊ Z3)^2; v = 231 = 3*7*11, 261 = 9*29 and 351 = 27*13 have several non-abelian groups.
- Hetman's G-space method: take a subgroup of the automorphism group of a known design with related parameters, use its orbit structure on points as the prescribed action, and solve the orbit exact cover (Kramer-Mesner) with a SAT solver or dancing links.
- Mirroring (arXiv:2604.04975): replacing some base blocks by their inverses turns one difference family into many non-isomorphic designs, useful as seeds for local repair at nearby v.
- Before searching, check whether a new ingredient makes an undecided value follow from a PBD or product construction.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Excluded or inadmissible v: S(2,6,36) and S(2,6,46) do not exist; v must be 1 or 6 mod 15 for k = 6 and 1 or 7 mod 42 for k = 7.
- Settled values: 226 and 441 (k = 6), 505 and 589 (k = 7), 225 (k = 8), 289, 369 and 3321 (k = 9). New non-isomorphic designs for decided v are not wins.
- Short orbits: when the group does not act regularly on blocks, the base-block difference test miscounts; expand and count pairs.
- The Handbook's undecided lists for k = 7, 8 and 9 exist only in the printed book. The open arXiv papers give their sizes (21, 38, 91) but name only 127 and 211 (k = 7), so p2 needs an open source that names the value.
- Block files in Ihromant/math-utils are data; parse them and never run code from the repository.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/steiner-2-designs-block-6-undecided.md
```

Already set up? Say `run V3R1T4S on steiner-2-designs-block-6-undecided`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `steiner-2-designs-block-6-undecided`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
