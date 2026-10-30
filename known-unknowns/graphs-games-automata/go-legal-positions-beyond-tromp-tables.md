# Legal Go positions: 20x20 (OEIS A094777 a(20)) and the first unknown cells of Tromp's rectangular m x n tables

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days for the rectangular partial cells (m <= 13); needs cluster with tens of TB of disk for m >= 14 and for 20x20 (19x19 took most of 2015 on servers) · open as of 2026-10-30

## The problem

A Go position (any point empty, black or white) is legal if every group has a liberty. John Tromp, with Gunnar Farneback (early dynamic-programming code) and Michal Koucky (most of the computation for n = 14 to 16), counted legal positions exactly on n x n boards for n <= 19. L(19,19), about 2.0817e170, was finished on 2016-01-20. The method is a transfer-matrix count modulo many primes, combined by the Chinese remainder theorem. Tromp's site also has tables of L(m,n) for each m <= 19. For m <= 8 they list linear recurrences, so every n is known. For larger m the tables end at: m = 9: n = 208, m = 10: 187, m = 11: 170, m = 12: 156, m = 13: 42, m = 14 to 18: 19, m = 19: 20. The asymptotic form is L(m,n) ~ 0.8506399258457 x 0.965535059338374^(m+n) x 2.9757341920433572493^(mn). Checked 2026-10-30: OEIS A094777 has terms to n = 19, and the legal.html table pages (served with Last-Modified 2026-09-24) end where listed above. No 20x20 value is published.

## What counts as a win

CONFIRMED: the exact value of L(20,20) = A094777(20), the number of legal positions on the 20 x 20 board, absent from OEIS A094777 and Tromp's legal.html at verification time. The claiming code must reproduce A094777(1..16) exactly, and the same 20-wide run must output L(20,n) for n = 1..13 and n = 19 that match Tromp's published L(n,20) values (tables L1 to L13 and L19) reduced modulo every prime the run used. It must be confirmed by an independent check: residues modulo at least three fresh primes (not used in the claim), computed by an independently written transfer-matrix program, must match the claimed integer.

## Partial wins

- **p1:** A new exact cell L(m,n) for 9 <= m <= 13 with n one or more beyond the last entry of Tromp's Lm.html table (for example L(13,43)), computed by code that reproduces that table up to its last entry and A094777(1..13) exactly, and confirmed by residues modulo at least three fresh primes from an independently written transfer-matrix program that match the claimed integer.
- **p2:** A new exact cell L(m,20) for 14 <= m <= 18, or L(19,21), computed by code whose same run reproduces Tromp's published L(m,1..19) (or L(19,1..20)) and which reproduces A094777(1..13) exactly, and confirmed by residues modulo at least three fresh primes from an independently written transfer-matrix program that match the claimed integer.

## How a win is checked

Compile an independent transfer-matrix counter (border states tracking colours and group connectivity, with pending-liberty flags). Reproduce A094777(1..13) in full and Tromp's L9 to L13 tables up to their ends. Then compute the claimed value modulo three random 61-bit primes and compare with the claimed integer reduced mod those primes. Sanity check: the ratio to the asymptotic formula should be 1 to many digits for large boards.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://tromp.github.io/go/legal.html>

## Sources

- <https://tromp.github.io/go/legal.html>
- <https://tromp.github.io/go/L13.html>
- <https://tromp.github.io/go/L19.html>
- <https://oeis.org/A094777>
- <https://github.com/tromp/golegal>
- <https://tromp.github.io/go/gostate.pdf>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- For m <= 8 the cells follow from published recurrences and do not count as new.
- L(m,n) = L(n,m): a cell is new only if neither orientation is listed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/go-legal-positions-beyond-tromp-tables.md
```

Already set up? Say `run V3R1T4S on go-legal-positions-beyond-tromp-tables`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `go-legal-positions-beyond-tromp-tables`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
