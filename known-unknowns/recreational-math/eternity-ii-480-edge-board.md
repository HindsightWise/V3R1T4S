# MOONSHOT - Eternity II: the full 480-edge solution, or a board beating the 470/480 record (or the 465 five-clue record)

🎲 **Recreational math** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (the 470 boards took about a month on a 32-core home Threadripper with Blackwood's solver; scoring a board takes laptop-minutes) · open as of 2026-10-30

## The problem

Eternity II (designed by Christopher Monckton, sold by Tomy from 28 July 2007) is a 16 x 16 edge-matching puzzle: 256 square pieces, 22 colours, a grey frame, and a mandatory starter piece (id 138 counting from 0, piece 139 counting from 1) fixed at I8, which is cell 135 in row-major order counting from 0, rotation 0. A full solve matches all 2 x 15 x 16 = 480 internal edges. The $2M prize expired unclaimed at noon on 31 December 2010, and no 480 board on the official set has ever been published. Record history on the official set, starter clue only: 467 by Louis Verhaard (2008, won the $10,000 partial prize); 468 and then 470 by Joshua Blackwood (2020; 470 on 2021-03-30, eternity2 groups.io #10117); 469 by Peter McGavin (2020); Jef Bucas tied 470 on 2024-12-02. All five optional clue placements respected: 460 by Bruno Gauthier (2023), 464 by Benjamin Riotte (July 2026), then 465 from Riotte's shared five-clue fleet (August 2026). The community record page (Raphael Anjou's eternity2.dev, updated 2026-07-22) lists 470 and 465 as standing. This lane re-scored Blackwood's 470 board from the eternity2.dev viewer link with its own checker: the 256 cells are exactly the official piece multiset (after a colour relabelling), the frame is all grey, the starter piece sits at cell 135, rotation 0, and 470 internal edges match.

## What counts as a win

A 16 x 16 placement of the official 256 Eternity II pieces (each piece used exactly once, any rotation) in which every frame edge is grey, the starter piece (id 138 from 0) sits at cell 135 (I8) at its official rotation, and all 480 internal edges match. Use the piece set in raphael-anjou/eternity2 research/starter-kit/data/official.json, which is identical to the community e2pieces/CSV set. Boards on other piece sets do not count: Brendan Owen's Clue-1/Clue-2 sets, the unframed TopCoder variant, and mixed expansion sets.

## Partial wins

- **p1:** A starter-only board on the official set (same rules as the success criterion) with 471 to 479 matching internal edges, strictly above the open record of 470 (Blackwood 2021, tied by Bucas 2024), provided the record on eternity2.dev/research/records is still 470 at verification time.
- **p2:** A board that respects all five official clue placements listed in official.json (cell 135 with piece 138 at rotation 0, cell 210 with piece 180 at rotation 1, cell 34 with piece 207 at rotation 1, cell 221 with piece 248 at rotation 2, cell 45 with piece 254 at rotation 1; cells counted row-major from 0, rotation convention as in that file) and has at least 466 matching internal edges, strictly above the 465 five-clue record (Riotte and the five-clue fleet, August 2026), provided that record still stands at verification time.

## How a win is checked

Write an independent checker that does not reuse a solver's code. (1) Load official.json: 256 pieces as URDL edge integers, with 0 for grey. (2) Parse the claimed board as 256 cells of URDL colours. If the colour labels differ (the eternity2.dev viewer uses letters a..w), find the colour bijection that makes the multiset of rotation-canonical cells equal to the official multiset. This also proves each piece is used exactly once. (3) Check that every frame-facing edge is grey. (4) Check that the starter cell equals piece 138 at its official rotation, plus the other four clues for p2. (5) Count matching horizontal and vertical internal edges out of 480. Cross-check the score in Jef Bucas's viewer at e2.bucas.name or the eternity2.dev viewer, both of which re-score a board from its own edges.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://eternity2.dev/research/records/>

## Sources

- <https://eternity2.dev/research/records/>
- <https://eternity2.dev/status/>
- <https://github.com/raphael-anjou/eternity2/blob/main/research/starter-kit/data/official.json>
- <https://e2.bucas.name>
- <https://www.shortestpath.se/eii/eii_details.html>
- <https://github.com/jblackwood345/EternityII_Solver>
- <https://en.wikipedia.org/wiki/Eternity_II_puzzle>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Blackwood's solver (heuristic placement schedule with break-index limits) and Bucas's C rewrite libblackwood are the methods behind every 468-470 board. Retuning the break schedule took Blackwood from 469 to 470.
- Treat the last ten broken edges as an exact sub-problem: free a region around the breaks and re-solve it exactly by SAT, CP or DLX with all remaining pieces, as on eternity2.dev's 'tail as its own exact problem' page.
- Verhaard's 2008 approach annealed the composition of piece sets between regions, not only positions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Many '480/480' boards online use other piece sets (Clue-1/Clue-2, TopCoder unframed, mixed sets). They are not solutions of Eternity II.
- Starter-only and five-clue scores are different records. Do not compare a five-clue board with 470, or a starter-only board with 465.
- Record announcements sit on the eternity2 groups.io list, which needs an account to read. Agents never sign up for anything: use eternity2.dev's records page and board viewer instead.
- Piece files in different tools label colours differently. Always map colours back to official.json before claiming a score.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/eternity-ii-480-edge-board.md
```

Already set up? Say `run V3R1T4S on eternity-ii-480-edge-board`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `eternity-ii-480-edge-board`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
