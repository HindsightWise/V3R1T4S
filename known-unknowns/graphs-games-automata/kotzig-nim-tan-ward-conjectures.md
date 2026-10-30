# Kotzig's Nim: refute a Tan-Ward periodicity conjecture or extend its verified range (G(1,5;n) beyond n = 140, G(3,5;n) beyond 111, ...)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (memoised search over visited sets; the 2014 database was computed in C++ on an 8-core Mac Pro) · open as of 2026-10-30

## The problem

Kotzig's Nim (Anton Kotzig, 1946; Winning Ways pp. 515-517) is played on a circle of n locations with a move set M. From the current location a player moves m steps clockwise (m in M) and marks the landing location, which must not already be marked. Location 0 is marked at the start, and the player unable to move loses. Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem A6) asks whether the outcome is eventually periodic in n for every finite M. Xin Lu Tan and Mark Daniel Ward (Integers 14 (2014) G06) proved one primitive theorem and published a database of 185,134 outcomes (all 1 <= m1 < m2 <= 72 with n <= 72, plus longer runs for chosen pairs). They made six conjectures for two-move sets, verified as follows: {1,5} to n <= 140; {2,5} to n <= 114; {3,5} to n <= 111 (P exactly for odd n outside {9, 11, 17}); {4,5} to n <= 109; {4,7} to n <= 115; {5,6} to n <= 112. They also verified Fraenkel et al.'s conjecture for {3,4} (the first player wins for n = +-3 mod 7) to n <= 115. The database (re-read 2026-10-30) still ends at those n, and GONC6 reports no later progress.

## What counts as a win

CONFIRMED: a board size n beyond the verified range at which the outcome of G(m1, m2; n) contradicts one of Tan and Ward's Conjectures 4.1-4.6 or Fraenkel et al.'s {3, 4} conjecture, computed by two independently written solvers that both reproduce the Tan-Ward database entries for that move set. A proof of one of these conjectures for all n, formalised in Lean 4, Coq or Isabelle, also counts. The result must not be published at verification time (Integers, arXiv, the GONC Unsolved Problems column).

## Partial wins

- **p1:** The verified range of one of Conjectures 4.1-4.6 (or of the {3, 4} conjecture) extended by at least 20 consecutive board sizes beyond the published bound (for example G(3, 5; n) for all n <= 131), by two independent solvers that agree and both reproduce the Tan-Ward database for that move set.

## How a win is checked

Rerun the claimed G(m1, m2; n) with two solvers (memoised search on (visited set, current location), or a smarter state encoding), using the convention of Tan and Ward's Section 1: location 0 is marked, Player I moves first, and P means the second player wins. Both solvers must first reproduce kotzigdatabase.txt for that move set. The lane checked such a solver against the database for six move sets and n <= 30 on 2026-10-30.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.stat.purdue.edu/~mdw/kotzig/kotzigdatabase.txt>

## Sources

- <https://math.colgate.edu/~integers/og6/og6.pdf>
- <https://www.stat.purdue.edu/~mdw/kotzig/kotzigdatabase.txt>
- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- With two step sizes the game is a walk with at most two choices per move. Prune by symmetry and store only the reachable visited sets, which are far fewer than 2^n for small step sizes.
- Conjecture 4.3 ({3,5}) is the simplest to state and its exceptional set {9, 11, 17} is small, which makes it a good first extension.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The two conventions in the literature (an empty board versus location 0 pre-marked) swap N and P; use Tan and Ward's.
- The database's http address redirects; use the https URL.
- Extending a verified range is only a partial win; it proves nothing about periodicity.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/kotzig-nim-tan-ward-conjectures.md
```

Already set up? Say `run V3R1T4S on kotzig-nim-tan-ward-conjectures`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kotzig-nim-tan-ward-conjectures`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
