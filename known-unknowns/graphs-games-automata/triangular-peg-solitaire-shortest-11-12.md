# Triangular peg solitaire: shorter single-vacancy solutions on Triangle(11) and Triangle(12) (OEIS A127500 bounds 19..28 and 21..29)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

On the triangular board of side n (T(n) = n(n+1)/2 holes, jumps along the three lattice directions), A127500(n) is the length of the shortest solution to any problem that starts with one peg missing and ends with one peg, a move being one or more consecutive jumps by the same peg. George Bell computed the values for n = 4..10: 5, 9, 9, 12, 13, 16, 18. Triangle(10) needs 18 moves, and showing that no 17-move solution exists was the hard part. His page on large triangular boards (last modified 2007) and OEIS A127500 (re-fetched 2026-10-30, unchanged since 2015) give 19 <= a(11) <= 28 and 21 <= a(12) <= 29. The upper bounds are explicit solutions: 28 moves from a4 to a1 on Triangle(11) and 29 moves from e11 to a3 on Triangle(12). Bell writes that a(11) is believed to be 20, 21 or 22, so the known solutions are far from optimal, and his main triangular page (updated 27 April 2025) reports nothing better. A single shorter solution on either board is a strict improvement.

## What counts as a win

A legal solution on Triangle(11) in at most 27 moves, or on Triangle(12) in at most 28 moves, starting from a single vacancy and ending with a single peg, verified by a simulator; or an exact value of a(11) or a(12) with a re-runnable exhaustive certificate. The result must be strictly better than the bounds in the live OEIS A127500 entry and Bell's triangular page at claim time.

## Partial wins

- **p1:** Each further strict improvement of the best known upper bound for a(11) or a(12) beyond the first counts as a partial win once published with its solution.
- **p2:** A lower bound a(11) >= 20 or a(12) >= 22, from an exhaustive search certificate or a machine-checked counting argument.

## How a win is checked

Simulate the solution on a triangular-lattice board: check every jump (along one of the three lattice directions over an adjacent peg into an empty hole), count maximal same-peg runs as moves, and confirm a single starting vacancy and a single final peg.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A127500>

## Sources

- <https://oeis.org/A127500>
- <https://www.gibell.net/pegsolitaire/LargeTriangular/index.html>
- <https://www.gibell.net/pegsolitaire/tindex.html>
- <https://arxiv.org/abs/math/0703865>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Bell's solutions for Triangle(9) and Triangle(10) end with long sweeps; design endings with long sweeps for side 11 and 12 and search backward from them.
- The problem allows any starting vacancy and any finishing hole, which gives many targets for bidirectional search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Count moves, not jumps.
- Bell's later work may contain better unpublished solutions; check his triangular page and paper versions before claiming.
- Triangular boards of some sides have parity or position-class restrictions on which vacancy/finish pairs are solvable; use a solvable pair.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/triangular-peg-solitaire-shortest-11-12.md
```

Already set up? Say `run V3R1T4S on triangular-peg-solitaire-shortest-11-12`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `triangular-peg-solitaire-shortest-11-12`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
