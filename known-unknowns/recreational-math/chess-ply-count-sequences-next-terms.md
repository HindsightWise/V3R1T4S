# Chess from the opening position: the next term of the per-ply counts (distinct positions at ply 12, checkmates at ply 14, perft(16))

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster for perft(16) and checkmates at ply 14 (GPU-weeks); distinct positions at ply 12 is laptop-weeks with tens of TB of disk, or a small cluster · open as of 2026-10-30

## The problem

Four OEIS sequences count what can happen in the first n plies of chess. A048987 counts move sequences (perft), known to n = 15: perft(14) = 61885021521585529237 and perft(15) = 2015099950053364471960 (Ankan Banerjee, GPU perft, talkchess 2016 and 2017; perft(14) also Peter Osterlund). A083276 counts distinct positions (placement, side to move, castling rights, an en passant square only when an e.p. capture is legal), known to n = 11: a(11) = 726155461002 (Peter Osterlund 2013, verified by Francois Labelle 2017). A089957 counts uniquely realizable positions, also to n = 11: a(11) = 1994236773. A079485 counts games ending in checkmate at exactly ply n, known to n = 13: a(13) = 346742245764219 (Labelle, 2017). Earlier terms are by Richard Bean, Paul Byrne, Steven Edwards, Arkadiusz Wesolowski and Labelle. Checked 2026-10-30: OEIS A048987 (edited June 2026) stops at a(15), A083276 and A089957 at a(11), and A079485 at a(13). The Chessprogramming wiki Perft Results page has only a Monte Carlo estimate of perft(16) (Ajedrecista, CCC, Feb 2024). Wikipedia's Shannon number table leaves positions blank after ply 11 and checkmates after ply 13. Labelle's page on statistics of chess positions (last updated 2017) gives more per-ply tables: checkmate diagrams to ply 13, mirror-symmetric diagrams to ply 15, at-home diagrams to ply 16.

## What counts as a win

CONFIRMED: an exact value, absent from the OEIS entry and from any published source at verification time, for at least one of A083276 a(12), A089957 a(12), A079485 a(14) or A048987 a(16), under the exact definitions of the OEIS entries (A083276 follows Labelle's definition 2: en passant is recorded only when an e.p. capture is legal; A079485 counts games, not distinct positions). The claim must include (1) per-first-move or per-ply-k subtotals (a 'divide'), (2) code that reproduces every known term of the same sequence exactly, and (3) agreement with a second run by an independently written move generator or counting method, on all subtotals or on a random 2% of them. A finished full second run counts the same.

## Partial wins

- **p1:** An independent recomputation of perft(15) = 2015099950053364471960 (the Chessprogramming wiki credits only Ankan Banerjee's 2017 GPU run), with a per-first-move divide, by code that shares nothing with Banerjee's perft_gpu.
- **p2:** The next row of one of Labelle's per-ply diagram tables (checkmate diagrams at ply 14, mirror-symmetric diagrams at ply 16, or at-home diagrams at ply 17) under his definitions, with code that reproduces every earlier row of that table exactly and a second independent check as in the success criterion.

## How a win is checked

Rebuild the claimant's counter and an independent one (for example python-chess's legal move generator for small depths, plus a fast bitboard generator) and confirm both reproduce every known term of the claimed sequence exactly (A048987 a(0..15), A083276 a(0..11), A089957 a(0..11) or A079485 a(0..13)), or for p2 every earlier row of the claimed Labelle table. Then recompute a random 2% of the claimed subtotals (each subtotal is the count below one position at a fixed split depth) with the independent generator and check that the subtotals sum to the claimed total. For distinct-position counts, check the dedup key (placement, side to move, castling rights, legal-e.p. square only) and test it on known transpositions.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A083276>

## Sources

- <https://oeis.org/A048987>
- <https://oeis.org/A083276>
- <https://oeis.org/A089957>
- <https://oeis.org/A079485>
- <https://www.chessprogramming.org/Perft_Results>
- <https://www.wismuth.com/chess/statistics-positions.html>
- <https://en.wikipedia.org/wiki/Shannon_number>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Distinct positions: a level-by-level BFS over position sets partitioned by material and pawn structure (pawn moves and captures are irreversible, so partitions are small and independent), with sorted external-memory dedup per partition.
- Checkmates at ply 14: perft with a transposition table keyed by position plus remaining depth, counting mates at the leaves; the counts depend only on the position, so transpositions can be merged.
- Use the colour-and-board mirror only where it is valid: chess positions with castling rights are not left-right symmetric.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Counting positions with the FEN en passant field set after every double pawn push gives a different, larger sequence; A083276 records e.p. only when the capture is legal.
- A079485 counts games, not distinct mate positions; Labelle's 'checkmate diagrams' table is a different quantity.
- Perft(16) Monte Carlo estimates are not values.
- A value posted on talkchess.com or elsewhere but not yet in the OEIS counts as published: check before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/chess-ply-count-sequences-next-terms.md
```

Already set up? Say `run V3R1T4S on chess-ply-count-sequences-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `chess-ply-count-sequences-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
