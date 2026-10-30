# Strongly regular configurations: construct a (v_k; lambda, mu) configuration marked '?' in the Abreu-Funk-Krcadinac-Labbate table (smallest (41_5; 9,10))

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (SAT / prescribed-automorphism searches) · open as of 2026-10-30

## The problem

A symmetric configuration (v_k) has v points and v lines, k points on each line and k lines through each point, and any two points on at most one line. It is a strongly regular configuration (v_k; lambda, mu) if its point (collinearity) graph is strongly regular with parameters (v, k(k-1), lambda, mu). M. Abreu, M. Funk, V. Krcadinac and D. Labbate (Des. Codes Cryptogr. 90 (2022) 1881-1897; arXiv:2104.04880) tabulated feasible parameters of proper, primitive strongly regular configurations. Krcadinac's online table (srconf.html, last modified 2024-11-03) gives 41 rows and marks existence unknown ('?') for (41_5;9,10), (61_6;14,15), (81_8;37,42), (85_6;11,10), (85_7;20,21), (99_7;21,15), (105_9;51,45), (113_8;27,28), (121_6;11,6), (121_9;43,42), (121_10;65,72), (125_9;45,36), (136_6;15,4), (136_9;36,40), (145_9;35,36), (153_8;19,21), (169_9;31,30), (169_12;101,110), (171_11;73,66), (175_6;5,5), (181_10;44,45), (196_10;40,42), (196_13;122,132) and (196_13;125,120). Two of these are excluded. Brouwer's SRG table marks srg(99,42,21,15) as non-existent (Koval + AI), so (99_7;21,15) cannot exist. (136_6;15,4) cannot exist either: srg(136,30,15,4) is unique, the triangular graph T(17), and as in the paper's rook-graph argument (Theorem 5.2) the lines inside each 16-clique of T(17) would form an S(2,6,16), which violates Fisher's inequality (b = 8 < 16). For the smallest open row, (41_5;9,10), the point graph would have the parameters of the Paley graph P(41).

## What counts as a win

Success means a list of v lines, each a k-subset of v points, for a row marked '?' in the live table (https://web.math.pmf.unizg.hr/~krcko/results/srconf.html), other than (99_7;21,15) and (136_6;15,4). Every point must lie on exactly k lines, any two points must share at most one line, and the collinearity graph must be strongly regular with parameters (v, k(k-1), lambda, mu). Two independent programs must verify it. At claim time the row must still be '?', the point-graph srg must not be marked '-' in Brouwer's live table, and a fresh literature search must find no construction or non-existence proof.

## Partial wins

- **p1:** A machine-checked non-existence proof for a '?' row other than (99_7;21,15) and (136_6;15,4), with a DRAT/LRAT or exact-ILP certificate (or, where every srg with the point-graph parameters is known, an exhaustive clique search over all of them) that an independent checker re-verifies.
- **p2:** For a row whose count of known configurations in the live table is a lower bound (not boldface), a new strongly regular configuration not isomorphic to any in the table's linked files, certified by canonical forms (nauty/Traces on the point-line incidence graph).

## How a win is checked

Parse the lines. Check v lines of size k, point degrees k and pairwise line intersections of at most 1 (a partial linear space). Build the collinearity graph and check that it is k(k-1)-regular, with exactly lambda common neighbours for adjacent pairs and mu for non-adjacent pairs. For p2, compare canonical forms of incidence graphs against the table's linked files, parsed as data.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~krcko/results/srconf.html>

## Sources

- <https://web.math.pmf.unizg.hr/~krcko/results/srconf.html>
- <https://arxiv.org/abs/2104.04880>
- <https://aeb.win.tue.nl/graphs/srg/srgtab.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the known strongly regular graphs with the right parameters (for example Paley(41), Paley(61), Paley(113)). Look for a partition of their edge sets into v cliques of size k with each vertex in k cliques: a clique-partition problem suited to SAT.
- Cyclic ansatz: for prime v, search for a k-subset of Z_v whose development is a configuration (a planar-difference-set condition) with the required collinearity graph.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rows whose point-graph SRG is marked non-existent in Brouwer's table are settled; (99_7;21,15) is the current example.
- (136_6;15,4) is ruled out by hand (unique point graph T(17), and Fisher's inequality inside each 16-clique). It is not open and does not count for p1.
- When the point graph is unique (for example srg(105,72,51,45) and srg(125,72,45,36) are marked '!'), a full clique search may settle the row quickly. Check the literature before claiming it as new.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/strongly-regular-configurations-open.md
```

Already set up? Say `run V3R1T4S on strongly-regular-configurations-open`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `strongly-regular-configurations-open`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
