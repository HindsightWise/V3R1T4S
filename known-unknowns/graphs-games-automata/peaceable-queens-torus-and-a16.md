# Peaceable queens: beat Clinch-Drescher-Huynh-Saffidine's odd-torus records (n = 19..63), or determine a(16)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Peaceable queens: place white and black queens so that no queen attacks one of the opposite colour, maximising the smaller army. On the ordinary n x n board, a(n) (OEIS A250000) is known exactly only through n = 15 (a(14), a(15) = 28, 32 by Paul Tabatabai with integer programming, 2018). For n >= 16 only bounds are known. Rob Pratt's 2014 IP gives 37 <= a(16) <= 64. Stephen Ainley's 1977 constructions (values for n <= 30, general lower bound floor(7n^2/48)) have been beaten only once, by Dmitry Kamenetsky's n = 27 solution with 106 queens against Ainley's 105. Peter Karpov notes that all known values equal floor(7n^2/48) except at n = 5, 9. On the toroidal board, Katie Clinch, Matthew Drescher, Tony Huynh and Abdallah Saffidine (arXiv 2406.06974, latest v3 of 27 Oct 2024) give bounds. In Appendix A they list their best odd-torus solutions, found by local search, for every odd n from 13 to 63 (e.g. 19: 32, 25: 56, 41: 156, 43: 162, 45: 184, 51: 252, 53: 250, 63: 348). The authors note there is no regular pattern and that n = 53 is below n = 51, so improvements are plausible. The toroidal sequence OEIS A279405 (m white and m black queens, equivalent to maximising min(|B|,|W|)) is now exact through n = 18 (a(13)-a(14) from Jaideep Padhi, Jun 2026; a(15)-a(18) from Jan P. Harries, Jul 2026). Its values a(13) = 16, a(15) = 20, a(17) = 28 equal Appendix A, so the open odd-torus cases start at n = 19. Score on the torus is min(|B|, |W|).

## What counts as a win

Success means one of three things. (a) For some odd n in 19..63: sets B, W of cells of the n x n TORUS (rows, columns, and both diagonal families taken mod n) with no queen in B attacking a queen in W along any wrapped line, and min(|B|,|W|) STRICTLY greater than all of: the value listed for that n in Appendix A of the latest version of https://arxiv.org/abs/2406.06974 (v3 as of 2026-10-28), any term for that n in OEIS A279405 (https://oeis.org/A279405), and any later published value found by search, all re-fetched live immediately before claiming. (b) For some n >= 16 on the ordinary board: a peaceful configuration with min(|B|,|W|) STRICTLY greater than both floor(7n^2/48) and every lower bound or construction cited for that n in OEIS A250000 (https://oeis.org/A250000), re-fetched live (comments, links and b-file; e.g. 106 for n = 27). (c) A certified determination of a(16): a configuration achieving the claimed value plus an upper-bound proof for value+1 (ILP with an exact-arithmetic certificate such as VeriPB, or SAT with DRAT checked by drat-trim), with two independent encodings.

## Partial wins

- **p1:** An odd-torus record improvement for any single odd n in 19..63 (criterion (a)) - the most realistic target.
- **p2:** Even-torus: for an even n larger than every n in the live DATA of OEIS A279405 (n >= 20 as of 2026-10-28), a configuration on the n x n torus beating the paper's Theorem 1.1 construction value for that n and not dominated by any configuration the paper or a later source (e.g. Harries 2026 on even tori) reports (state the value used).
- **p3:** A certified upper bound a(16) <= 38 (or any improvement on the best published upper bound), without the matching construction.

## How a win is checked

Read B and W as cell lists; check B and W are disjoint; for every b in B and w in W check they do not share a row, column, diagonal (i-j) or anti-diagonal (i+j) - mod n on the torus, plain on the board. Count. Milliseconds. For a(16), re-run the certificate checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2406.06974>

## Sources

- <https://arxiv.org/abs/2406.06974>
- <https://arxiv.org/pdf/2406.06974v3>
- <https://oeis.org/A279405>
- <https://oeis.org/A250000>
- <https://oeis.org/A260680>
- <https://arxiv.org/abs/1902.05886>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exploit the irregularities: n = 43 and n = 53 sit well below the trend of their neighbours; start local search from the n = 41/45 and n = 51 solutions rescaled or with rows/columns inserted.
- Torus symmetry: impose invariance under a translation subgroup (Z_n acts transitively), turning the problem into choosing periodic 'argyle' or 'plaid' motifs plus a defect; enumerate motifs exactly, then repair defects with CP-SAT.
- Import from statistical physics: this is a two-species hard-core lattice gas with long-range exclusion; use parallel tempering / replica exchange with cluster (swap-colour region) moves.
- Import from image segmentation: the two armies occupy regions bounded by lines of four slopes; optimise region shapes as polygons (graph-cut style) in the continuum limit, then discretise, as Jubin's and Ainley's pentagon constructions do.
- For a(16): IP with orbital branching over the 16-element symmetry group (rotations, reflections, colour swap), plus cuts from the 'amicable rooks' bound.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- On the torus, lines wrap around: a queen at (0,0) attacks (n-1,n-1) diagonally. Checking with board (non-wrapped) lines gives fake torus records.
- The score is the SMALLER army, min(|B|,|W|); a bigger total with an unbalanced split is not a record.
- Even and odd tori behave very differently; Appendix A lists only odd n.
- Odd tori n = 13, 15, 17 are already settled by OEIS A279405 (exact values equal Appendix A); do not target them. A279405 is actively extended (2026 additions), so re-check its DATA for n = 19 and up.
- The paper may be revised (v4+) with better numbers, and later papers or apps by the same authors or others (e.g. Harries 2026) may host newer results; re-fetch the latest arXiv version and search before claiming.
- On the ordinary board, matching floor(7n^2/48) is the known best, not a record; for n = 27 the bar is already 106 (Kamenetsky).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/peaceable-queens-torus-and-a16.md
```

Already set up? Say `run V3R1T4S on peaceable-queens-torus-and-a16`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `peaceable-queens-torus-and-a16`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
