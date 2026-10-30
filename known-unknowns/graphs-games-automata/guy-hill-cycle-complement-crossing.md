# Guy-Hill conjecture for the complement of a cycle: determine cr(complement of C_11) (conjectured 36)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact crossing-number search on 11 vertices, 44 edges) · open as of 2026-10-30

## The problem

Guy and Hill (1973) gave drawings of the complement of the n-cycle with (n-3)^2(n-5)^2/64 crossings for odd n and n(n-4)(n-6)^2/64 for even n, and conjectured that these are optimal. They proved equality for n <= 10, and showed that equality at an odd n implies equality at n+1. The Clancy-Haythorpe-Newcombe dynamic survey (arXiv 1901.05155 v5, Dec 2021) still lists n >= 11 as open. Guy and Hill's general lower bound is trivial unless n > 20. The smallest open case is n = 11: an 8-regular graph on 11 vertices with 44 edges and conjectured value 36. Proving 36 would also settle n = 12 (conjectured 54). Our own arithmetic: deleting any vertex leaves K_10 minus a 10-vertex path, which contains the complement of C_10 (crossing number 15). Each crossing involves 4 vertices and so survives in 7 of the 11 deletions, which gives cr(complement of C_11) >= ceil(11*15/7) = 24. The October 2026 Harary-Hill proof (OpenAI; exposition by Balko, arXiv 2610.34444) has corollaries for K_2k - M, K_2k - e, K_2k x P_t, K_m x C_even and Sierpiński graphs, but none for complements of cycles. The OpenAI 2026 manuscript catalogue has no such item either. Credit: Guy and Hill, and the survey authors.

## What counts as a win

Either (A) a planarization of a drawing of the complement of C_11 with at most 35 crossings, certified planar by two independent testers, which refutes the conjecture; or (B) a certified proof that cr(complement of C_11) >= 36: a formal proof, or an exact crossing-number certificate (ILP/SAT over planarizations or Kuratowski constraints with a checked DRAT/LRAT/VeriPB log and an independently re-derived encoding). Before claiming, re-fetch https://arxiv.org/abs/1901.05155 (latest version) and search the literature after 2021, including Harary-Hill follow-ups, to confirm the case is still open.

## Partial wins

- **p1:** A certified lower bound cr(complement of C_11) >= L for some L >= 25, strictly above the vertex-deletion counting bound 24 and strictly above any bound found by a fresh literature search (state it), to the certificate standards of (B).
- **p2:** A certified lower bound cr(complement of C_11) >= 30, to the certificate standards of (B).

## How a win is checked

Rebuild the complement of C_11 (vertices 0..10, i ~ j iff j - i is not +-1 mod 11). Check that the planarization's edge paths reproduce the 44 edges and that the graph is planar (two testers plus an Euler check), then count dummies. For lower bounds, regenerate the encoding and check the proof log; validate the pipeline by reproducing Guy-Hill's n = 9 and n = 10 values (9 and 15).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1901.05155>

## Sources

- <https://arxiv.org/abs/1901.05155>
- <https://arxiv.org/abs/2610.34444>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The complement of C_11 has a dihedral symmetry of order 22; use it to break symmetry in an exact ILP/SAT search.
- The new Harary-Hill proof technique may adapt to near-complete graphs; check whether its counting argument gives 36 directly.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The two formulas differ by parity of n; n = 11 uses the odd formula (8^2 * 6^2 / 64 = 36).
- The complement of C_11 is 8-regular (44 edges); check your graph construction against this.
- On 2026-10-30 the survey (v5, 2021), Balko's exposition (Corollaries 7-11: none for cycle complements) and web, arXiv, Crossref and DataCite searches for 2022-2026 work were checked; no value or improved bound for n = 11 was found. Exact crossing-number tools (Chimani-Wiedera-style ILP proof systems) could in principle already have computed this small case unpublished; search again, including Graph Drawing proceedings, before attacking.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/guy-hill-cycle-complement-crossing.md
```

Already set up? Say `run V3R1T4S on guy-hill-cycle-complement-crossing`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `guy-hill-cycle-complement-crossing`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
