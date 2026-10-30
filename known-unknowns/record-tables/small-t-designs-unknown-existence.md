# Small simple t-designs of unknown existence: 3-(20,5,2), 3-(21,7,15), 4-(16,8,15), 4-(18,9,14), 4-(19,9,21), 5-(16,7,5), 5-(17,8,20), 2-(55,10,3) and kin

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (Kramer-Mesner with prescribed automorphism groups) · open as of 2026-10-30

## The problem

For given t, v and k, admissible indices of t-(v,k,lambda) designs are multiples m * lambda_min, and simple designs (no repeated blocks) can exist only up to lambda_max = C(v-t,k-t). V. Krcadinac (J. Combin. Des. 26 (2018) 193-200, arXiv:1706.01682) and Krcadinac and Pavcevic constructed many designs with prescribed automorphism groups. These improve Table 4.46 of the Handbook of Combinatorial Designs (Khosrovshahi-Laue, t >= 3) and the Mathon-Rosa BIBD table (Table 1.35). His online table (newdesigns.html, last modified 2024-11-03) still marks the following as unknown: 2-(55,10,lambda) for lambda = 3, 6, 7 (lambda = 1, 2 impossible); 3-(20,5,2); 3-(21,7,15); 4-(16,8,lambda) for lambda = 15, 30; 4-(18,9,lambda) for lambda = 14, 28; 4-(19,9,lambda) for lambda = 21, 42; 5-(16,7,5); 5-(17,8,20). In each row the higher multiples are known to exist. Block counts are b = lambda C(v,t)/C(k,t): 2-(55,10,3) has 99 blocks (a Mathon-Rosa open entry, r = 18); 3-(20,5,2) has 228; 4-(18,9,14) has 340; 4-(16,8,15) has 390; 3-(21,7,15) has 570; 4-(19,9,21) has 646; 5-(16,7,5) has 1040; 5-(17,8,20) has 2210. 4-(15,5,1) = S(4,5,15) is known not to exist. Steiner 3-designs are covered by the bank target small-steiner-3-designs-open and are excluded here.

## What counts as a win

Success means an explicit simple t-(v,k,lambda) design for a (t,v,k,lambda) listed as '?' in the live table (https://web.math.pmf.unizg.hr/~krcko/results/newdesigns.html): b distinct k-subsets of a v-set such that every t-subset lies in exactly lambda blocks. Two independent programs must verify it. At claim time the entry must still be '?' and a fresh literature search must find no construction or non-existence proof. The supplementary design (all k-subsets not in the design, with index lambda_max - lambda) counts for the same row.

## Partial wins

- **p1:** A machine-checked non-existence proof for a listed (t,v,k,lambda), for example 3-(20,5,2) or 5-(16,7,5), with a DRAT/LRAT or exact-ILP certificate that an independent checker re-verifies.
- **p2:** A non-simple t-(v,k,lambda) design (repeated blocks allowed, every t-subset in exactly lambda blocks counted with multiplicity) for a listed row, verified by two programs, provided a fresh literature search finds no earlier non-simple example.

## How a win is checked

Check b = lambda C(v,t)/C(k,t), that the blocks are k-subsets of range v, and (for the main win) that they are distinct. Count, for every t-subset, the blocks containing it (C(20,3) = 1140 up to C(17,5) = 6188 subsets: instant). Two independent checkers. Kramer-Mesner claims must expand the orbit representatives with the verifier's own group code before checking.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~krcko/results/newdesigns.html>

## Sources

- <https://web.math.pmf.unizg.hr/~krcko/results/newdesigns.html>
- <https://arxiv.org/abs/1706.01682>
- <https://site.uvm.edu/jdinitz/?page_id=384>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Kramer-Mesner: pick a group G acting on v points, form the t-orbit vs k-orbit incidence matrix, and solve A x = lambda * 1 over {0,1} with an ILP, lattice basis reduction (Wassermann) or SAT. Krcadinac used nonabelian groups for the existing rows.
- Derived and residual links: a 5-(17,8,20) design derives to 4-(16,7,20) designs. Check whether known 4-designs extend.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The table is about simple designs; a design with repeated blocks is only p2.
- Index multiples: the open entries are the smallest multiples m listed as '?'; larger m are already known.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/small-t-designs-unknown-existence.md
```

Already set up? Say `run V3R1T4S on small-t-designs-unknown-existence`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `small-t-designs-unknown-existence`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
