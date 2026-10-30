# Quasi-symmetric 2-designs: construct one for an open feasible parameter set with v <= 78 (smallest 2-(33,15,35), x=6, y=9)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (Kramer-Mesner with prescribed automorphism groups) · open as of 2026-10-30

## The problem

A quasi-symmetric 2-(v,k,lambda) design (QSD) has no repeated blocks, and any two blocks meet in x or y points (x < y). Neumaier's table of feasible parameters was updated by M. S. Shrikhande (Handbook of Combinatorial Designs, 2007) and others. V. Krcadinac's 2016/17 lecture notes 'Kvazisimetricni dizajni' give Table 1: 94 feasible (v,k,lambda,x,y) with v <= 78, leaving out strongly resolvable designs, Steiner 2-designs and biplane residuals. Each row lists the number of known QSDs (Nqsd) and of block-graph strongly regular graphs (Nsrg). His live page (quasisym.html, last modified 2024-11-03) lists the parameter sets with v <= 70, plus three extra rows, for which a QSD is known. No QSD is known for the rows marked '?' in Table 1, for example (33,15,35,6,9), (39,12,22,3,6), (41,9,9,1,3), (41,20,57,8,11), (42,18,51,6,9), (42,21,60,9,12), (43,16,40,4,7), (45,15,42,3,6), (45,18,34,6,9), (45,21,70,9,13), (46,16,72,4,7), (49,13,13,1,4) and (52,16,20,4,7). Six '?' rows are now settled as impossible and are excluded: (35,14,13,5,8), since its block graph srg(85,14,3,2) does not exist (Brouwer's table, Shpectorov-Zhao); (46,16,8,4,6), since srg(69,20,7,5) does not exist (Brouwer's table, Koval + AI); (56,15,42,3,6), since srg(616,205,90,57) is marked non-existent (Koval + AI); (76,26,52,6,10), since srg(456,325,236,220) is marked non-existent; (37,9,8,1,3), by Harada, Munemasa and Tonchev (J. Combin. Des. 25 (2017)); and (56,12,9,0,3), by Munemasa and Tonchev (J. Combin. Des. 28 (2020) 745-752, via ternary codes of biplanes on 56 points). Block graphs were checked against Brouwer's live table on 2026-10-30.

## What counts as a win

Success means the incidence matrix of a 2-(v,k,lambda) design with no repeated blocks whose pairwise block intersections all lie in {x,y}, with both values occurring. The design must match a row of Krcadinac's Table 1 marked Nqsd '?', other than the six excluded rows (35,14,13,5,8), (37,9,8,1,3), (46,16,8,4,6), (56,12,9,0,3), (56,15,42,3,6) and (76,26,52,6,10). Two independent programs must verify it. At claim time the row must still be unsettled: absent from the live quasisym.html, its block graph srg(b,a,c,d) not marked '-' in Brouwer's live table, and no existence or non-existence result found by a fresh literature search. The complementary design counts for the same row.

## Partial wins

- **p1:** A machine-checked non-existence proof for a non-excluded '?' row (for example via the self-orthogonal code or block-graph route plus an exhaustive search), with a DRAT/LRAT or exact-ILP certificate a skeptic re-runs.
- **p2:** A certified exhaustive search showing that no QSD with a non-excluded '?' row's parameters admits a stated automorphism group of prime order p >= 3, for a (row, group) pair not already excluded in the literature, reproduced by an independent program.

## How a win is checked

Check that every t-subset count matches (each pair of points in exactly lambda blocks), that b = v r / k with r = lambda(v-1)/(k-1), that the blocks are distinct, and that every pairwise block intersection lies in {x,y}. Optionally build the block graph (adjacency = intersection y) and confirm it is srg(b,a,c,d) as in Table 1. Compare the row with Krcadinac's Table 1 and the live quasisym.html, and look up the block graph in Brouwer's table.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~krcko/results/quasisym.html>

## Sources

- <https://web.math.pmf.unizg.hr/~krcko/results/quasisym.html>
- <https://web.math.pmf.unizg.hr/~krcko/nastava/kvazisim.pdf>
- <https://aeb.win.tue.nl/graphs/srg/srgtab.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Kramer-Mesner with tactical decompositions (Krcadinac-Vlahovic) under prescribed groups: this method produced the 2-(56,16,18) and many 2-(28,12,11) QSDs.
- For x = 1, y = 3 rows (for example (41,9,9)), the binary code spanned by the blocks is self-orthogonal-like. Search through doubly even codes of the right length, as was done for (49,9,6) via self-dual [50,25,10] codes.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Feasibility tables omit designs with repeated blocks; a design with repeated blocks does not count.
- Always check the block graph in Brouwer's live SRG table: a '-' there settles the QSD row as impossible.
- Table 1 (2016/17) is older than some non-existence proofs that do not show up in Brouwer's table: (56,12,9,0,3) is still '?' there and its block graph srg(210,176,148,144) is '?', but Munemasa-Tonchev (JCD 2020) proved non-existence.
- Published partial results limit p2: for (41,9,9,1,3), Munemasa-Tonchev (AAECC 33 (2022) 855-866) prove that no cyclic QSD exists and that any automorphism of prime order p < 41 has p <= 5, so only p = 3 and p = 5 remain; Krcadinac-Vlahovic Kruc (Adv. Math. Commun. 15 (2021)) exclude (56,20,19,5,8) for certain prescribed automorphism groups. Check these before claiming a (row, group) pair.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/quasi-symmetric-2-designs-open-feasible.md
```

Already set up? Say `run V3R1T4S on quasi-symmetric-2-designs-open-feasible`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quasi-symmetric-2-designs-open-feasible`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
