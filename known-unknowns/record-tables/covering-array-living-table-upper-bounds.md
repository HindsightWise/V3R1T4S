# Covering arrays CA(N;t,k,v), t = 2..6, v = 2..25: fewer rows than the best known in the living covering-array table

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (exhaustive check is C(k,t) column sets x N rows; arrays with k in the thousands need a C or GPU checker, chunked) · open as of 2026-10-30

## The problem

A covering array CA(N;t,k,v) is an N x k array over v symbols in which every choice of t columns shows all v^t tuples in some row; CAN(t,k,v) is the least such N. Charles Colbourn's covering array tables (t = 2..6, v = 2..25) were the reference for two decades but are now behind an ASU sign-in wall (Cloudflare Access, checked 2026-10-30). Ulrike Groemping preserved their November 2024 status (ugroempi/CAs, ColbournTables.md). Christopher Smolen's living table (chrispbsmolen/ca-tools, generated 2026-10-29) uses that snapshot as a baseline and adds checked arrays: 14,450 rows, 648 verified in full, 152 sizes cited from Torres-Jimenez and Izquierdo-Marquez 2024 (Mathematics 12, 1908, order-seven CPHFs), 3 disputed rungs. 110 verified rows are already below the 2024 snapshot. They come from the CAs package data (Torres-Jimenez binary arrays, ordered-design constructions), from Smolen's own Paley-doubling and cyclic-CPHF arrays, and from Mickael Bergeron's strength-3 Raaphorst-Moura-Stevens extension (MichelBacon/covering-arrays-rms-extension, 78 entries for v = 5..19). Rows also come from Shokri, Moura and Stevens (arXiv:2510.13122v3, Oct 2026, strength 4) and from the Dwyer database and NIST library arrays. Numaro's July 2026 report claims 40 improvements but lists only eight cells (largest CA(14928;3,8,24)); all eight are matched or beaten in the live table. Smolen notes that improvements are not yet pushed through recursive constructions, so many derived rows are probably stale. The table takes new arrays by pull request and changes daily.

## What counts as a win

Success means an explicit N x k array over v symbols (2 <= t <= 6, 2 <= v <= 25, k > t) in which every t-subset of columns contains all v^t tuples, checked exhaustively. N must be STRICTLY SMALLER (direction: min) than the best known N at k in the live table, re-fetched at verification time from https://raw.githubusercontent.com/chrispbsmolen/ca-tools/main/table/ca_table.csv. The stair-step rule applies: the best known N at k is the least N over CITED or VERIFIED rows with at least k columns. SCREENED rows do not count. A CITED row that has a DISPUTED twin still counts. N must also be strictly below the frozen Colbourn value (ugroempi/CAs ColbournTables.md) and below every value found for that (t,k,v) in the MichelBacon/covering-arrays-rms-extension improvements.csv, the Numaro list, and any 2024-2026 arXiv or journal paper found by search (for example arXiv:2510.13122v3). N >= v^t always; going below a published exact CAN means a bug. Making a pull request to the table is a human action and is not part of the win.

## Partial wins

- **p1:** First explicit witness: for a live-table row at strength t >= 3 that is CITED only (no VERIFIED or SCREENED array on file at that (t,v,k,N) or at any row that dominates it), an explicit array of exactly that N and at least that k, verified exhaustively, with its construction named.
- **p2:** Settle a disputed rung: an explicit, exhaustively verified array at the size of one of the three CITED rows that the table marks DISPUTED (CA(762;3,128,6), CA(43220;3,2162,20), CA(48531;3,2312,21)), or an independently written construction showing those sizes are attained.

## How a win is checked

Write an independent checker in C or numpy; do not reuse ca_verify.c. Parse the array, map symbols to 0..v-1 (reject don't-care entries unless the claim fills them), and assert the shape is N x k. For every t-subset of columns, encode each row's tuple as an integer in [0, v^t) and confirm that all v^t codes appear. Bitsets over v^t and chunking over column subsets parallelise well. Re-download ca_table.csv at check time and compute the stair-step best N at k for the claimed (t,v), using CITED and VERIFIED tiers. Then check the Groemping frozen table, the Bergeron improvements.csv and a fresh arXiv search for the same (t,k,v). Record the SHA-256 of the checked file. Claim only if N is strictly below all of them.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://chrispbsmolen.github.io/ca-tools/>

## Sources

- <https://chrispbsmolen.github.io/ca-tools/>
- <https://raw.githubusercontent.com/chrispbsmolen/ca-tools/main/table/ca_table.csv>
- <https://github.com/ugroempi/CAs/blob/main/ColbournTables.md>
- <https://github.com/MichelBacon/covering-arrays-rms-extension>
- <https://arxiv.org/abs/2510.13122>
- <https://doi.org/10.3390/math12121908>
- <https://numaro.tech/research/covering-arrays-colbourn-2026/>
- <https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software/acts-library/covering-array-library>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Propagate the new verified rows: run standard recursive constructions (Roux-type and Chateauneuf-Kreher doubling, products, fusion, column extension, CPHF composition) on the 110 post-2024 ingredients. The table's propagation engine is not connected to submissions, so derived rows are probably stale.
- Generalise Bergeron's Raaphorst-Moura-Stevens extension (add m columns to the orthogoval-plane CA(2q^3-1;3,q^2+q+1,q)) to strength 4 with the Shokri-Moura-Stevens truncated-Mobius-plane arrays as the base.
- Search cyclic covering perfect hash families CPHF(n;k,v,t) over GF(q) with prescribed multipliers (Smolen's route for t = 5, 6). Each CPHF row expands to q^t - q CA rows, so one saved CPHF row saves many CA rows.
- Post-optimise stored arrays: delete rows and repair the uncovered tuples with simulated annealing or SAT, focusing on (t,v) blocks whose rows are all CITED and old.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The ASU Colbourn pages are login-walled, so do not compare against the Feb 2025 Wayback crawl alone; the live table and the frozen copy are the baselines.
- Use the stair-step rule: an entry (k,N) covers every smaller k, so a 'new' row can already be dominated by a row with more columns.
- SCREENED arrays (random column windows only) do not count as best known, and neither do claims checked only on samples.
- The table and the CAs package are edited several times a day (four pushes on 2026-10-29), so re-fetch right before claiming.
- Arrays may be stored with symbols 1..v or with don't-care entries; normalise before checking. Mixed-alphabet arrays and t >= 7 are outside this table.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/covering-array-living-table-upper-bounds.md
```

Already set up? Say `run V3R1T4S on covering-array-living-table-upper-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `covering-array-living-table-upper-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
