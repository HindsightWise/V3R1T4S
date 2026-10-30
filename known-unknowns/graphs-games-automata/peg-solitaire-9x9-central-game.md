# Peg solitaire on the 9x9 square board: a central-game solution shorter than Alain Maye's 34 moves

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

On the 81-hole 9x9 square board (orthogonal jumps), the central game starts with only the centre hole empty and must finish with one peg in the centre. A move is one or more consecutive jumps by the same peg. George Bell's peg solitaire site (re-fetched 2026-10-30, page last modified 23 October 2026, 9x9 subpage dated 2015) calls the shortest central-game solution 'currently an open question'. The shortest known solution, 34 moves, was found by hand by Alain Maye in 2004. Bell gives a lower bound of 24 moves, generalizing Robin Merson's 1962 argument for the 6x6 board, and expects the minimum to be around 30 by analogy with the 10x8 board. The odd side length makes the techniques used to settle the 8x8 and 10x8 boards much weaker here. Bell also poses as challenges reaching the board's symmetric 32-loops from single-vacancy starts.

## What counts as a win

A legal central-game solution on the 9x9 board (centre vacancy to one peg in the centre, orthogonal jumps only) using at most 33 moves, where a move is a maximal run of consecutive jumps by the same peg, verified by a simulator that replays every jump and counts moves. It must be strictly shorter than the best solution on Bell's page at claim time (34 moves as of 2026-10-30).

## Partial wins

- **p1:** A single-vacancy-to-single-survivor solution on the 9x9 board that finishes with a 33-sweep or a 32-loop ending at a5 (or a symmetric equivalent), or a machine-checked proof that neither can be reached from any single-vacancy start. Bell's 9x9 page leaves both unresolved; this counts only if the page still lists the question as open at claim time.
- **p2:** A rigorous lower bound of 25 or more moves for the 9x9 central game, either as a written proof whose case analysis is machine-checked, or as an exhaustive-search certificate re-runnable by a skeptic.

## How a win is checked

A short simulator on the 9x9 grid applies each jump (a peg jumps an orthogonally adjacent peg into an empty hole two steps away, removing the jumped peg), checks legality, counts moves as maximal runs of jumps by the same peg, and confirms the start and final states.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.gibell.net/pegsolitaire/>

## Sources

- <https://www.gibell.net/pegsolitaire/>
- <http://www.gibell.net/pegsolitaire/9x9/9x9index.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Bidirectional or backward search from the finish with pattern-based pruning (Barker and Korf 2012) settled smaller boards; combine it with long-sweep endings, since the board supports sweeps of up to 34 jumps.
- Beam search over positions ranked by Bell's position-class and resource counts is a cheap way to look for 30-33 move solutions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Count moves, not jumps: every central-game solution has 79 jumps, far more than 34 moves.
- Diagonal jumps are not allowed on this board.
- The finish must be in the centre hole, not anywhere.
- Bell proves that no 32-sweep ending at e5 can be reached from a single-vacancy start, so do not target it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/peg-solitaire-9x9-central-game.md
```

Already set up? Say `run V3R1T4S on peg-solitaire-9x9-central-game`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `peg-solitaire-9x9-central-game`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
