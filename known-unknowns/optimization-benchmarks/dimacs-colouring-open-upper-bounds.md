# DIMACS graph colouring: a proper colouring with fewer colours than the best known for an open benchmark graph (DSJC, flat1000_76_0, latin_square_10, C2000/C4000)

🚚 **Optimization benchmarks** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (250 to 4,000 vertices; checking a colouring takes seconds) · open as of 2026-10-30

## The problem

The DIMACS colouring benchmarks come from the second DIMACS Implementation Challenge (1993) and the COLOR02-04 symposia. They include the DSJC random graphs of Johnson, Aragon, McGeoch and Schevon, Culberson's flat graphs, latin_square_10, Michael Trick's C2000/C4000 graphs and the wap graphs. Their status is tracked in the 'NP-?' (unsolved) tab of the Graph Coloring Benchmarks table maintained by Stefano Gualandi and Marco Chiarandini. That tab now carries a new C2000.9 record: 399 colours by Olawale Titiloye (Zenodo doi:10.5281/zenodo.23605852, 24 October 2026, quantum-annealing-based heuristic); repeated fetches on 2026-10-29 gave the same values. Best known upper bounds on 2026-10-29, with the best published lower bounds in brackets, combining the sheet with later work: DSJC250.1 8 (7), DSJC250.5 28 (26), DSJC500.1 12 (9), DSJC500.5 47 (43), DSJC500.9 126 (123; 124 in floating point), DSJC1000.1 20 (10), DSJC1000.5 82 (73), DSJC1000.9 222 (216), flat1000_76_0 81 (72), latin_square_10 97 (90), C2000.5 145 (118), C4000.5 259 (148), C2000.9 399 (145), wap03a 43 (40) and wap04a 41 (40). The sheet's History keys credit the upper bounds to TC11/TC12 (Titiloye and Crispin, quantum annealing), HW12 (Hao and Wu, extraction and expansion) and MT09, and the lower bounds to HSC10 (Held, Sewell and Cook, safe lower bounds). Several lower bounds are not on the sheet. Porumbel (Projective Cutting-Planes, SIAM J. Optim. 30(1), 2020) proved chi(DSJC250.1) >= 7. Van Hoeve (Graph coloring with decision diagrams, Math. Programming, 2021) proved chi(C2000.9) >= 145. Brand and Held (arXiv:2411.03003, 2024) found chi(DSJC500.9) >= 124 in unsafe floating point. Alfonso Gippini Requeijo (Zenodo 23228548 and 23358985, October 2026; VeriPB proofs also checked by CakePB) proved chi(C2000.5) >= 118 and chi(C4000.5) >= 148. Heule, Karahalios and van Hoeve (CP 2022, doi:10.4230/LIPIcs.CP.2022.26) closed wap02a and wap08a, raised the r1000.1c lower bound to 97, and lowered wap03a to 43 and wap04a to 41; the sheet still shows 42 for wap04a. Chowdhury, Codel and Heule (NFM 2023) found a 40-colouring of wap07a, closing it. Brand and Held then proved chi(r1000.1c) = 98 with exact decision diagrams and SCIP-exact, so r1000.1c is closed and not part of this target. Find a proper colouring with fewer colours than the best known for one of the 13 non-wap graphs.

## What counts as a win

A colouring (one line 'v c' per vertex v = 1..n, or n lines of colours) of one of DSJC250.1, DSJC250.5, DSJC500.1, DSJC500.5, DSJC500.9, DSJC1000.1, DSJC1000.5, DSJC1000.9, flat1000_76_0, latin_square_10, C2000.5, C4000.5 or C2000.9. A standalone checker reads the DIMACS file: https://mat.tepper.cmu.edu/COLOR04/INSTANCES/ < name > .col or .clq, except flat1000_76_0, which comes from https://cedric.cnam.fr/~porumbed/graphs/flat1000_76_0.col. It first confirms that |V| and the number of distinct undirected edges match the sheet. It must then find no edge with equal colours and count strictly fewer distinct colours than three values: the best known upper bound listed in this entry; the X_UB column of the 'NP-?' tab (CSV export https://docs.google.com/spreadsheets/d/0AqhCA2VMbzOIdGFpd2NnR3FZUkNyX01USXJWeWEzX1E/export?format=csv&gid=3), re-fetched immediately before claiming; and any colouring found by a literature and Zenodo search at claim time. The colouring file, the checker, the graph sha256 and the sheet snapshot are saved together. Nothing is sent to the maintainers by the agent; the write-up goes to the human.

## Partial wins

- **wap03a-wap04a-improve:** A 42-colouring of wap03a (best known 43, clique 40), or a 40-colouring of wap04a (best known 41; 40 would close it, since it contains a 40-clique), checked by the same checker on the CMU COLOR04 files. These bounds moved in 2022-2023 (Heule-Karahalios-van Hoeve DDFW runs; Chowdhury-Codel-Heule closing wap07a), so they are the least saturated.
- **certified-colouring-lower-bound:** A lower bound strictly above the best published one for any graph in the list. The bound must exceed at least DSJC250.1 7, DSJC250.5 26, DSJC500.1 9, DSJC500.5 43, DSJC500.9 124, DSJC1000.1 10, DSJC1000.5 73, DSJC1000.9 216, flat1000_76_0 72, latin_square_10 90, C2000.5 118, C4000.5 148, C2000.9 145, wap03a 40 or wap04a 40, and any bound a literature and Zenodo search finds at claim time. Examples: chi(DSJC250.5) >= 27, or chi(wap04a) >= 41, which closes wap04a. The bound must be certified by an UNSAT proof of a stated k-colouring CNF checked with drat-trim or cake_lpr (DRAT/LRAT), or by a VeriPB proof log checked with VeriPB and CakePB. The skeptic regenerates the CNF or OPB from the graph with an independent script.

## How a win is checked

Download the graph from the CMU COLOR04 instance directory or, for flat1000_76_0, from Porumbel's page. Parse the 'p edge/col n m' and 'e u v' lines, deduplicate undirected edges and drop loops, and check |V| and |E| against the sheet. Verified 2026-10-29: distinct-edge counts match the sheet for DSJC250.1 (3,218), DSJC250.5 (15,668), DSJC500.1 (12,458), DSJC500.5 (62,624), DSJC500.9 (112,437), DSJC1000.1 (49,629), latin_square_10 (307,350), flat1000_76_0 (246,708), wap03a (286,722), wap04a (294,902) and C2000.9 (1,799,532; sha256 aa4b1d7df7f9c1afbf8c9f35fcf5bdfc6370fd27db5c9f3fd5409dfd0d164f16). Then check every edge against the colouring and count the colours. On the same day, Titiloye's released C2000.9 colouring (sha256 9c71015108e959203d2b25efe5b3fad23f4b18583f38f4719d68b2d96cc27186) was confirmed proper with 399 colours. Seconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://docs.google.com/spreadsheets/d/0AqhCA2VMbzOIdGFpd2NnR3FZUkNyX01USXJWeWEzX1E/export?format=csv&gid=3>

## Sources

- <https://sites.google.com/site/graphcoloring/vertex-coloring>
- <https://docs.google.com/spreadsheets/d/0AqhCA2VMbzOIdGFpd2NnR3FZUkNyX01USXJWeWEzX1E/export?format=csv&gid=3>
- <https://doi.org/10.5281/zenodo.23605852>
- <https://doi.org/10.4230/LIPIcs.CP.2022.26>
- <https://arxiv.org/abs/2411.03003>
- <https://doi.org/10.5281/zenodo.23228548>
- <https://doi.org/10.5281/zenodo.23358985>
- <https://doi.org/10.1137/19M1272652>
- <https://arxiv.org/abs/2504.04821>
- <https://mat.tepper.cmu.edu/COLOR04/INSTANCES/>
- <https://cedric.cnam.fr/~porumbed/graphs/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- On the large dense graphs (C2000.5 145, C4000.5 259), independent-set extraction followed by a strong k-colouring local search on the residual graph (Hao and Wu's extraction and expansion) remains the state of the art. Quantum-annealing-style path-integral Monte Carlo (Titiloye and Crispin, and the October 2026 C2000.9 record) is the other productive line.
- Population methods such as HEAD (Moalic and Gondran) and TabuCol-based memetic algorithms reach 82 on DSJC1000.5. Long parallel runs on 10 cores with diversity control are the practical route to a (k-1)-colouring.
- For the wap graphs, the 2022-2023 improvements came from DDFW local search (UBCSAT) on a direct SAT encoding with only the clique fixed. Try newer weight-transfer variants and many seeds.
- Physics import: k-colouring is the zero-temperature antiferromagnetic Potts model, and replica exchange or population annealing on the Potts energy is competitive near the colourability threshold.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The sheet lags the literature. It shows wap04a at 42 and r1000.1c as open with lower bound 96, although Brand and Held proved chi(r1000.1c) = 98. It shows lower bounds of 6 for DSJC250.1, 99 for C2000.5 and 107 for C4000.5, and none for C2000.9; these are now 7, 118, 148 and 145. It shows abb313GPIA at 8/10, but that graph has since been solved exactly (ZykovColor, arXiv:2504.04821). Its rows for wap01a, wap02a, wap06a, wap07a and wap08a are old or blank, and all five are closed. Use the values in this entry and search before claiming.
- C2000.5, C4000.5 and C2000.9 are distributed as .clq files from the DIMACS clique benchmark. Colour exactly those graphs, not their complements.
- flat1000_76_0 is missing from the COLOR04 directory, and Trick's older COLOR directory has it only in binary .col.b format. Check |V| and |E| against the sheet before using any copy. Some .col files list every edge twice (DSJC500.9.col declares 224,874 edges for 112,437 distinct ones), so count distinct undirected edges.
- Weighted, equitable, sum and list colouring records (for example minimum-sum colouring of C2000.9) are different problems.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/optimization-benchmarks/dimacs-colouring-open-upper-bounds.md
```

Already set up? Say `run V3R1T4S on dimacs-colouring-open-upper-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dimacs-colouring-open-upper-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
