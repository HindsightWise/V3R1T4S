# Salem-Spencer sets: settle r_3(212) in {43, 44}, or beat a Wróblewski nonaveraging record a(n)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: needs cluster for a complete UNSAT certificate (Ergezer's campaign used Slurm nodes and still left 26 of 6,071 chunks open); a 44-set search or a better split is laptop-days · open as of 2026-10-30

## The problem

r_3(N) is the largest subset of {1..N} with no 3-term arithmetic progression (OEIS A003002). Exact values are known for N <= 211 (Dybizbański 2012 to 120; Fausto A. C. Cariboni's b-file to 211, r_3(211) = 43). The first open case is N = 212. Mehmet Ergezer (arXiv:2606.04016, v1 31 May 2026; Zenodo 10.5281/zenodo.21413746, 17 Jul 2026; GitHub README snapshot mpc-submission-v1.3) gives a verified 43-element witness and a large CP-SAT/HiGHS/CaDiCaL/kissat campaign. No 44-set was found, but the complete cube cover has not been certificate-checked: 6,045 of 6,071 T2 chunks closed without proof logging, 26 UNKNOWN. So r_3(212) is in {43, 44}, an explicitly stated open unit gap. Equivalently, the threshold A065825(44) (least M with a 44-element 3-AP-free subset of [1..M]) is in [212, 215]. Jarek Wróblewski's nonaveraging-sets site keeps best-known a(n) for n <= 1024 (BEST.TXT, last modified 2023-08-31) and modular records m(n) (BESTMOD.TXT). It lists a(44) <= 215, a(45) <= 227, a(100) <= 762 and a(1024) <= 25958, from searches and constructions by Gavin Theobald, Clyde Kruskal, William Rex Marshall, Fumitaka Yura and Rodolfo Niborski. Target: decide r_3(212).

## What counts as a win

Success means either (a) an explicit 44-element subset of {1..212} with no three elements a < b < c satisfying a+c=2b, checked exhaustively by two independent programs (this proves r_3(212) = 44 and beats Wróblewski's a(44) <= 215); or (b) a complete proof that no such 44-set exists: a cube or chunk cover of the whole search space whose completeness is checked by an independent script, with every cube UNSAT by a DRAT/LRAT proof accepted by drat-trim or cake_lpr, on a CNF that an independent generator reproduces byte for byte from the definition (all 3-APs in [1,212], cardinality 44). Together with the known 43-witness this proves r_3(212) = 43. Before claiming, re-fetch https://oeis.org/A003002 (b-file), https://oeis.org/A065825 and the Ergezer README/Zenodo/arXiv versions: success needs r_3(212) to be undetermined there on the day.

## Partial wins

- **p1:** A Wróblewski integer record: for some n with 44 <= n <= 1024, an n-element 3-AP-free subset of {1..M}, checked by two programs, with M STRICTLY SMALLER (direction: min) than the effective bar for n. The bar is the minimum over k >= n of a(k) - (k - n) and m(k) - (k - n), with a(k) from http://www.math.uni.wroc.pl/~jwr/non-ave/BEST.TXT and m(k) from http://www.math.uni.wroc.pl/~jwr/non-ave/BESTMOD.TXT, both re-fetched live. This works because deleting the largest element of a k-set lowers its maximum by at least 1, and a k-set mod m lifts to a k-set in [1..m]. M must also be smaller than any value for that n in OEIS A065825 (including drafts shown in its history) or a newer paper. For n = 44 the bar is 215, so a 44-set with maximum 213 or 214 counts here; maximum 212 is the full win. On 2026-10-30 the bar is below the listed a(n) only at n = 59 (330), 254 (3178) and 255 (3179).
- **p2:** A Wróblewski modular record: for some n <= 1024, an n-element subset of Z_m with no 3-term progression mod m (no x, y, z, not all equal, with x + z = 2y mod m), with m STRICTLY SMALLER (direction: min) than m(n) in http://www.math.uni.wroc.pl/~jwr/non-ave/BESTMOD.TXT re-fetched live, checked by two programs over all pairs modulo m.

## How a win is checked

For (a) and p1, enumerate all pairs (a,c) with a+c even and test whether (a+c)/2 is in the set, in two independently written programs; check size, range and distinctness. For p2, check all ordered pairs mod m, including the even-m case where x and x+m/2 exclude each other. For (b), regenerate the CNF from the definition with a separate script, check cube-cover completeness (every assignment of the split variables is covered, or the union of cube constraints is a tautology, checked by SAT), and run drat-trim or cake_lpr on every proof. Calibrate the pipeline by reproducing r_3(211) = 43 (or Ergezer's regressions at N = 80, 90, 100). Then compare with the live OEIS b-file and Wróblewski files.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/memoatwit/erdos_1194/blob/main/erdos_r3/README.md>

## Sources

- <https://oeis.org/A003002>
- <https://oeis.org/A065825>
- <https://arxiv.org/abs/2606.04016>
- <https://doi.org/10.5281/zenodo.21413746>
- <https://github.com/memoatwit/erdos_1194/blob/main/erdos_r3/README.md>
- <http://www.math.uni.wroc.pl/~jwr/non-ave.htm>
- <http://www.math.uni.wroc.pl/~jwr/non-ave/index.htm>
- <http://www.math.uni.wroc.pl/~jwr/non-ave/BEST.TXT>
- <http://www.math.uni.wroc.pl/~jwr/non-ave/BESTMOD.TXT>
- <https://doi.org/10.37236/2061>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Ergezer's released split and the 26 UNKNOWN chunks. Try a different split (endpoint plus middle-window cardinalities from A003002) together with kissat or CaDiCaL with proof logging, then close the leftovers with cube-and-conquer (march_cu) instead of CP-SAT.
- Use window-cardinality constraints from the exact r_3 values: every interval of length L inside [1,212] holds at most r_3(L) elements. Add them as native cardinality constraints and also as clauses, and compare.
- To look for a 44-set, take the Wróblewski records near a(44) = 215 (Theorem 22 construction), shrink by local search and SAT repair, and use the 3-AP hypergraph's reflection symmetry.
- For p1, many Wróblewski records come from product/split methods (methods.htm) and never had a dedicated search: run modern SAT/local search at mid-range n (100-300) seeded by the modular records.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Wróblewski's index page (non-ave/index.htm) warns that some 'Search' records have no stored solution and that the published results 'are not reliable'. BEST.TXT is also not monotone-consistent: a(59) = a(60) = 331, and a(254), a(255) exceed what a(256) = 3180 implies. So p1 uses the effective bar, not the raw listed value. Beating a value only counts if no newer source (OEIS A065825, papers) already lists a smaller one.
- Ergezer's no-proof closures (kissat without proof logging) are solver-attested, not certified. A full proof needs proofs for every cube plus a checked cover.
- Offsets: A003002 has offset 0, and A065825(n) is the least M (not M-1). A 44-set in [1,212] means A065825(44) <= 212.
- A CNF must forbid every triple a < b < c with a+c=2b in [1,212]; a missed triple gives a fake SAT witness.
- A fresh search on 2026-10-30 found nothing that settles r_3(212). It covered arXiv, the A003002 and A065825 histories, the Ergezer README and the erdos-frontier-atlas gap map, which lists the cell as open. A pending A065825 draft (Zachary Sharp, 20 Oct 2026) lists upper bounds for a(49..60), none below Wróblewski's. Other groups are working on this cell, so repeat the search before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/r3-212-salem-spencer-unit-gap.md
```

Already set up? Say `run V3R1T4S on r3-212-salem-spencer-unit-gap`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `r3-212-salem-spencer-unit-gap`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
