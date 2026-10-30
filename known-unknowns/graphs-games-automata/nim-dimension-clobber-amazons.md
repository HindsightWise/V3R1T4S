# Nim-dimension of Amazons: a position equal to *8 (only *4 is known)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (canonical-form search over small Amazons regions, which grow explosively) · open as of 2026-10-30

## The problem

Carlos Santos defined the nim-dimension of a ruleset: it is n if the ruleset has a position of value *2^(n-1) but none of value *2^n. Toppling Dominoes, Thinning Thickets and Konane have infinite nim-dimension, and Col has nim-dimension 1 (Winning Ways). Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem E17) conjectures that Amazons has nim-dimension 3: only *4 is known, and no position of value *8. In Amazons each player moves one of her amazons like a chess queen through empty squares and then shoots an arrow from its landing square, also like a queen, which burns the square it lands on; the player unable to move loses. Regions separated by burnt squares add as a sum, so *5, *6 and *7 follow from known positions, but *8 does not. Any position of value *k with k >= 8 also gives a *8. The canonical form of *k has *8 among its options for both players, and every option of a canonical form is the value of a position reachable from the original one, so some reachable Amazons position equals *8. The same column conjectures that Clobber has nim-dimension 1, but that is false on small positions (see pitfalls), so Clobber is not part of this target.

## What counts as a win

CONFIRMED: a position of standard Amazons on a rectangular board (amazons of either or both colours, burnt squares allowed) whose canonical value is *k for some k >= 8, computed exactly by two independent programs (for example CGSuite, which implements Amazons, and one written by the claimant). The position must not be published at verification time (Games of No Chance volumes, Theoret. Comput. Sci., arXiv, CGSuite example libraries).

## How a win is checked

Recompute the canonical form of the claimed position with two independent canonical-form engines and check that it equals *k exactly, not just its outcome class. An outcome-only cross-check is that G + *k is a second-player win while G + *j is a first-player win for every j < k. First check the move generator on small published values: a queen move for the amazon, then a queen-move arrow from its landing square that burns a square, where the arrow may cross or land on the square just vacated.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Sources

- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>
- <https://library.slmath.org/books/Book70/files/1005.pdf>
- <https://en.wikipedia.org/wiki/Clobber>
- <https://en.wikipedia.org/wiki/Game_of_the_Amazons>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from the known *4 and search for small regions whose options include *4, *2, * and 0 for both sides.
- Nimbers appear early: an audit search on 2026-10-30 found a *2 on a 3 x 4 board with one amazon of each colour. Enumerate regions of 12 to 20 empty squares inside burnt borders, caching canonical forms by region shape and amazon placement, and keep only positions whose canonical form is a nimber.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- This is a counterexample hunt: the conjecture may be true.
- A position equal to *8 plus an infinitesimal is not *8; compare canonical forms exactly.
- E17's companion conjecture that Clobber has nim-dimension 1 is false on small positions. The one-row position o o x x o x o o x x equals *2 (checked 2026-10-30 with a canonical-form engine and a separate outcome-only search). The column's Amazons claim may be just as stale, so search the Amazons literature first, for example Snatzke's exhaustive searches (Theoret. Comput. Sci. 313, 2004) and the 2 x n Amazons work.
- Domineering is left out: its nim-dimension question depends on whether positions with holes count (Drummond-Cole's *2 has holes).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/nim-dimension-clobber-amazons.md
```

Already set up? Say `run V3R1T4S on nim-dimension-clobber-amazons`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nim-dimension-clobber-amazons`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
