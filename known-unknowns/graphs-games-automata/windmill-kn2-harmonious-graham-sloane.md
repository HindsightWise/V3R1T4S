# Graham-Sloane windmill conjecture: is K_8^(2) (two K_8 sharing a vertex) harmonious? (first open case of 'K_n^(2) harmonious iff n = 4')

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

A graph with q edges is harmonious (Graham and Sloane 1980) if its vertices get distinct labels in Z_q so that the edge sums f(u)+f(v) mod q are all distinct. The windmill K_n^(2) is two copies of K_n sharing one vertex: 2n-1 vertices and q = n(n-1) edges. Equivalently: two n-subsets A, B of Z_q meeting in exactly one element, each with all C(n,2) pairwise sums distinct mod q, whose 2*C(n,2) = q sums together cover Z_q exactly once. Ron Graham and Neil Sloane conjectured that K_n^(2) is harmonious if and only if n = 4 and verified it for n odd and n = 6; B. Liu (1994) proved non-harmonious when n is even and has a prime factor p = 3 mod 4 with odd exponent. Gallian's Dynamic Survey DS6 (28th ed., 30 Oct 2025, Section 2.4 and Table 2) still lists the conjecture as open. By our reading of Liu's condition the open n up to 50 are 8, 10, 16, 18, 20, 26, 32, 34, 36, 40, 50; the smallest is n = 8 (15 vertices, q = 56). Our own small checker reproduces the known facts (n = 4 harmonious, n = 3, 5, 6 not). Credit: Graham, Sloane; Liu; Gallian.

## What counts as a win

Success means, for n = 8, EITHER (a) an explicit assignment of 15 distinct residues mod 56 to the vertices of K_8^(2) such that the 56 edge sums are pairwise distinct mod 56 (refuting the conjecture), OR (b) a certified proof that no such labeling exists: an exhaustive search by two independent programs, or a SAT/CP encoding whose UNSAT result carries a DRAT/LRAT proof checked by drat-trim or cake_lpr plus an independent second method, with every symmetry reduction used (translation f -> f+t, multiplication by a unit mod 56) justified in the write-up. Before claiming, re-check the latest DS6 edition (Table 2, 'windmills') and the literature for a published decision of K_8^(2).

## Partial wins

- **p1:** The same (a) or (b) decision for n = 10 (19 vertices, q = 90).
- **p2:** A decision, (a) or (b), for any other n in {16, 18, 20, 26, 32, 34, 36, 40, 50} that DS6 and the literature do not already settle.

## How a win is checked

For (a): check the 15 labels are distinct mod 56 and that the 28 + 28 pair sums of the two cliques (both containing the shared vertex) are 56 distinct residues; milliseconds. For (b): check the proof certificate, rebuild the CNF or the search independently, and confirm the symmetry-breaking lemmas (translation by t shifts every sum by 2t; multiplication by a unit u permutes Z_56).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS6>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS6/pdf/>
- <https://doi.org/10.1137/0601045>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Enumerate all n-subsets of Z_q containing 0 with distinct pair sums, up to multiplication by units, then pair them with bitset tests for disjoint sum sets.
- Necessary congruence: summing all edge sums gives 7(sum of the 14 non-central labels) + 14c = 28 mod 56; use such sum and sum-of-squares identities to prune.
- Exact-cover formulation over the 56 residues, solved with DLX or a SAT solver with symmetry breaking.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The shared vertex's label belongs to both cliques; both sum sets include its sums.
- For graphs that are not trees the labels must be injective (no repeated label).
- Multiplying by a non-unit mod 56 is not a symmetry.
- The list of open n is derived from Liu's theorem as quoted in DS6 (Math. Practice Theory 1994); re-check Liu's exact hypotheses before claiming a case other than n = 8.
- The Graham-Sloane paper's ResearchGate copy returned 403 and the SIAM version may be paywalled; the status rests on DS6 Section 2.4.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/windmill-kn2-harmonious-graham-sloane.md
```

Already set up? Say `run V3R1T4S on windmill-kn2-harmonious-graham-sloane`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `windmill-kn2-harmonious-graham-sloane`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
