# Number of unique legal chess positions with 9 pieces (next term of OEIS A318266, Kryukov's NULP)

🎲 **Recreational math** · standard · tractability ★★★☆☆ · compute: laptop-days with a combinatorial (inclusion-exclusion) counter; brute-force enumeration of about 1e18 positions needs a cluster · open as of 2026-10-30

## The problem

Kirill Kryukov's NULP project counts chess positions with n pieces (kings included). A position is a placement, side to move, castling rights and en-passant rights. It is illegal if a side does not have exactly one king, a pawn stands on its last rank or behind its second rank, or the side to move can capture the enemy king. Positions are counted once per equivalence class under these transformations: swapping the colours of all pieces together with the top-bottom mirror of the board (and of e.p. squares), swapping castling rights and side to move (always); the left-right mirror (only for positions without castling rights); and, for pawnless positions without castling rights, also the top-bottom mirror alone and the a8-h1 diagonal reflection. Values for 2 to 8 pieces: 462, 368079, 125246598, 25912594054, 3787154440416, 423836835667331, 38176306877748245 (8 pieces: Kryukov, 27 December 2013; split by castling and en-passant rights, 14 April 2014). These are OEIS A318266 (entry by Cyril Banderier, 2018). Kryukov's page invites confirmations or corrections of any of his results. Checked 2026-10-30: the NULP page (updated 2025-03-05) and OEIS A318266 both stop at 8 pieces, and no 9-piece count is listed.

## What counts as a win

CONFIRMED: the exact 9-piece NULP under Kryukov's published definitions of legality, uniqueness, castling and en passant, computed by a counter that also reproduces all of Kryukov's 2- to 8-piece totals exactly, the 8-piece split by castling and e.p. rights (38043599567172213 / 68239052958566 / 64406325285316 / 61932332150), and his per-endgame 8-piece values for at least 100 randomly chosen endgames. A second, independently written counter must give the same 9-piece total and the same per-endgame breakdown. The 9-piece value must be absent from the NULP page and OEIS A318266 at verification time.

## Partial wins

- **p1:** The first independent confirmation of the full 8-piece table (total, all four castling/e.p. columns, and every per-endgame value in Kryukov's linked text files), or a documented correction that Kryukov's own definitions support.
- **p2:** The exact 9-piece NULP restricted to pawnless endgames (or to endgames with pawns), agreed by two independent counters that also reproduce the matching 8-piece subtotals.

## How a win is checked

Run both counters. Reproduce 2- to 8-piece values and the per-endgame files, then compare the 9-piece per-endgame breakdowns line by line. For small endgames (up to 5 pieces), brute-force enumerate positions with python-chess and canonicalize under the stated symmetries to cross-check the combinatorial method.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://kirill-kryukov.com/chess/nulp/>

## Sources

- <https://kirill-kryukov.com/chess/nulp/>
- <https://oeis.org/A318266>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Count all placements per material, then subtract those where the side to move attacks the enemy king, by inclusion-exclusion over attackers, with slider rays required empty. Burnside's lemma handles the symmetry quotient without enumeration.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Kryukov's symmetry rules differ for pawnless positions without castling rights; positions fixed by a symmetry (pieces on the long diagonal) must be counted once.
- Kryukov counts e.p. positions under his own e.p.-right definition; reproduce his 8-piece E column before trusting the 9-piece one.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/chess-endgame-nulp-nine-pieces.md
```

Already set up? Say `run V3R1T4S on chess-endgame-nulp-nine-pieces`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chess-endgame-nulp-nine-pieces`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
