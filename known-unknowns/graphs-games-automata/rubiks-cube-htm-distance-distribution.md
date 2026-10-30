# Rubik's Cube, half-turn metric: the exact number of positions at distance 16 (next term of OEIS A080601), or new distance-20 positions

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: needs cluster for the distance-16 count; laptop-hours per optimal solve for distance-20 hunting · open as of 2026-10-30

## The problem

God's number for the 3x3x3 Rubik's Cube in the half-turn metric is 20 (Tomas Rokicki, Herbert Kociemba, Morley Davidson and John Dethridge, 2010), but the full distance distribution is not known. cube20.org (re-fetched 2026-10-30) gives exact counts for distances 0 to 15, the last being 91,365,146,187,124,313 (Rokicki, independently confirmed), and only estimates beyond: about 1.1e18 at 16, 1.2e19 at 17, 2.9e19 at 18, 1.5e18 at 19 and about 490 million at 20. OEIS A080601 (re-fetched the same day) also ends at n = 15, with terms by Jerry Bryan, Rokicki, Kociemba, Thomas Scheunemann, Davidson and Dethridge. The distance-20 list on cube20.org/distance20s holds 102,772,698 known positions as of 25 July 2025 and Rokicki says he is still finding new ones sporadically, so the list is known to be incomplete. The bank's rubiks-cube-qtm-distance-25-26 entry covers the quarter-turn metric; this entry is HTM only.

## What counts as a win

The exact number of 3x3x3 positions at HTM distance exactly 16 (the next term of A080601), computed by a complete coset enumeration whose per-coset counts are released and reproduced independently, and consistent with the exact counts for distances 0 to 15 and the group order 43,252,003,274,489,856,000. It must be strictly new versus the live A080601 entry and cube20.org at claim time.

## Partial wins

- **p1:** A 3x3x3 position whose HTM distance is certified to be exactly 20 by an optimal solver (no solution of length 19 or less, plus a 20-move solution), and which is not in the current htm4.txt list on cube20.org/distance20s, up to the 48 cube symmetries and inversion, checked at claim time. Several new positions count as one partial win per batch.
- **p2:** The exact number of positions at HTM distance 20 within a stated complete set of cosets of Kociemba's subgroup H = <U, D, R2, L2, F2, B2 > , computed by optimal coset solving with released code and per-coset counts and reproduced on a sample by the skeptic, where the solved cosets contain at least one distance-20 position that is not in the current htm4.txt list (up to symmetry and inversion), so the count is not already implied by that list. Cosets with no distance-20 positions, or whose distance-20 positions all appear in htm4.txt, do not count. Families defined by a nontrivial symmetry or antisymmetry do not qualify, since cube20.org/symmetry already gives the distance of every such position.

## How a win is checked

For p1, run an independent optimal solver (for example Kociemba's Cube Explorer optimal mode or a twsearch-based solver) to confirm distance 20, and canonicalize under symmetry and inversion to check absence from htm4.txt. For the main win, rerun a random sample of cosets and check that the per-coset counts sum to the claimed total and match the exact lower-distance counts.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.cube20.org/>

## Sources

- <https://www.cube20.org/>
- <https://www.cube20.org/distance20s/>
- <https://oeis.org/A080601>
- <http://tomas.rokicki.com/rubik20.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Neighbours of known distance-20 positions and positions with symmetry are rich in new distance-20 positions; Rokicki's own hunting uses such seeds.
- For exact counts, the Kociemba subgroup coset method with the prepass trick (described in the SIAM paper) gives per-coset distance tables.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Half-turn metric only; QTM counts are A080602 and belong to the other bank entry.
- Positions equal up to symmetry or inversion are not new; canonicalize before comparing with the list.
- A heuristic two-phase solver gives upper bounds only; distance 20 needs a proof that 19 moves fail.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/rubiks-cube-htm-distance-distribution.md
```

Already set up? Say `run V3R1T4S on rubiks-cube-htm-distance-distribution`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rubiks-cube-htm-distance-distribution`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
