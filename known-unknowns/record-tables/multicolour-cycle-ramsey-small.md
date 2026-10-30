# Multicolour Ramsey numbers of short cycles: close R5(C4) 27-29, R6(C4) 34-38, R4(C6) 18-20, R(C3,C3,C4,C4) 30-36, R(C4,C4,K4) 20-21 or a similar DS1 cell

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for lower bounds (colourings of K_17..K_87); needs cluster or flag algebras for upper bounds · open as of 2026-10-30

## The problem

R(G1,...,Gk) is the least N such that every k-colouring of the edges of K_N has a colour-i copy of G_i for some i. DS1 revision #18 (Apr 2026), Sections 6.3.2-6.3.3, lists: 27 <= R5(C4) <= 29 (lower Lazebnik-Woldar), 34 <= R6(C4) <= 38 (Exoo; Boza), 33 <= R4(C5) <= 77 (flag algebras, Lidicky-Pfender), 18 <= R4(C6) <= 20 (Sun et al.; Zhang-Sun-Wu), 24 <= R(C3,C4,C4,C4) <= 27, 30 <= R(C3,C3,C4,C4) <= 36, 49 <= R(C3,C3,C3,C4) <= 57, 18 <= R(C4,C6,C6,C6) <= 20, 18 <= R(C4,C4,C6,C6) <= 20, 20 <= R(C4,C4,K4) <= 21, 27 <= R(C3,C4,K4) <= 29, 52 <= R(C4,K4,K4) <= 66, 34 <= R(C4,C4,C4,K4) <= 48, 49 <= R(C3,C4,C4,K4) <= 75, 87 <= R(C4,C4,K4,K4) <= 177. In three colours, Dzido's conjecture R3(C10) = 20 and the Bondy-Erdos case R3(C9) = 33 are the first open cases. Credit: Dybizbanski-Dzido, Xu-Radziszowski, Boza-Radziszowski, Lazebnik-Woldar, Exoo, Wesley (arXiv:2509.03784), Lidicky-Pfender, Sun Yongqi and coauthors, Zhang-Sun-Wu.

## What counts as a win

Either (a) an explicit k-colouring of the edges of K_N (an N x N symmetric colour matrix) with no colour-i copy of G_i for every i, checked by two independent exact programs, with N+1 STRICTLY GREATER (direction: max) than the lower bound for that cell in the live DS1 and any newer paper; or (b) an upper bound STRICTLY BELOW (direction: min) the DS1 upper bound, certified by an exact-rational flag-algebra certificate or a DRAT/LRAT UNSAT proof with a checkable reduction. Off-by-one: a colouring of K_N proves R >= N+1.

## Partial wins

- **p1:** A certified proof of R3(C10) <= 20 or R3(C9) <= 33 (each matching the known lower bound and settling a first open case of the Dzido or Bondy-Erdos conjecture).
- **p2:** Any upper-bound improvement by at least 1 for R5(C4), R6(C4) or R4(C6) with a re-checkable certificate.

## How a win is checked

For each colour class, test for the forbidden graph exactly: C4 via common-neighbour counts (A_i^2 off-diagonal at most 1), C_k for k >= 5 via exact cycle search, K4 via clique enumeration; cross-check each with a SAT query that must be UNSAT. Confirm the matrix is symmetric, complete and uses only k colours. Certificates via drat-trim/cake_lpr or an exact SDP checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://arxiv.org/abs/2509.03784>
- <https://arxiv.org/abs/1704.03592>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Multicolour classical numbers with only complete graphs (R(3,3,3,3) and the like) belong to the small-ramsey-lower-bounds and classical-upper-bound targets, not this one.
- R4(C4) = 18 and R5(C6) = 26 are settled.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/multicolour-cycle-ramsey-small.md
```

Already set up? Say `run V3R1T4S on multicolour-cycle-ramsey-small`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `multicolour-cycle-ramsey-small`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
