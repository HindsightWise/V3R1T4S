# Busy Beaver for cyclic tag systems: settle BBCT(8) or beat a size 8-14 champion

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-minutes to laptop-hours · open as of 2026-10-30

## The problem

A cyclic tag system is a list of binary production words used in rotation: the string starts as 1 with the head on the first word; each step deletes the first bit, appends the current word if that bit was 1, and moves the head to the next word, cyclically; it halts when the string is empty. Size is the total length of the words plus their number. BBCT(n) is the longest halting run of a size-n system. Cyclic tag is the model Matthew Cook used for the universality of rule 110. The bbchallenge wiki's Cyclic Tag page (last edited 2026-10-11) gives exact values through n = 7 (BBCT(7) = 13, champion 0110__) and lower bounds: BBCT(8) >= 28 (101_10_), 9 >= 717 (1011_00_), 10 >= 1,626,862 (1001_1_00), 11 >= 1,859,166 (10_10010_0), 12 >= 6,328 (0111__010_0), 13 >= 5,217,735 (001110_1_0_0), 14 >= 154,171,565 (01011__0_0100). AzertyWasTaken's repository (documentation, deciders, holdout lists) reported 1 holdout at size 8, 17 at size 9 and 133 at size 10 when its table was written.

## What counts as a win

Success means (a) a cyclic tag system of size n, 8 <= n <= 14 (conventions of https://wiki.bbchallenge.org/wiki/Cyclic_Tag), that halts after STRICTLY more steps than the bound listed for n on that page, re-fetched live before claiming, verified by direct simulation; or (b) an exact BBCT(n) for some n in 8..14 that the page still lists with ' > =', with every size-n system either halting (step count given) or carrying a checkable non-halting certificate re-checked by an independent decider.

## Partial wins

- **p1:** Exact BBCT(8), with every non-halting size-8 system certified.
- **p2:** A size-12 system halting after more than 6,328 steps (verified by direct simulation).
- **p3:** Exact BBCT(9), or a new champion at any size from 9 to 14.

## How a win is checked

Independent simulator with the stated rules (calibration: 010_ halts after 7 steps, 010_0 after 8, 0110__ after 13, 101_10_ after 28; all reproduced). For exact values, enumerate all word lists of the given size, confirm the count, and re-check every certificate (exact cycles of (head, string) states; translated cycles, where the string's suffix repeats at the same head position while the prefix grows).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Cyclic_Tag>

## Sources

- <https://wiki.bbchallenge.org/wiki/Cyclic_Tag>
- <https://github.com/AzertyWasTaken/Busy-Beaver/tree/main/Cyclic%20Tag%20System>
- <https://en.wikipedia.org/wiki/Tag_system#Cyclic_tag_systems>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Seed the size-12 search with the size-10 and size-11 champions plus an extra empty or one-bit word, then search the neighbourhood.
- Certify growing holdouts by finding a period of the head together with a repeating block structure (translated-cycler style).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The repository's results.md is older than the wiki (for example it lists BBCT(10) >= 209 where the wiki lists >= 1,626,862), and its spec.md halts at fewer than two symbols, not at the empty string; the wiki's definitions and table are the authority.
- Empty words count toward size through the word count (each '_' separator closes a word); size 8 means total word length plus number of words equals 8.
- BBCT is not obviously monotone in n, because adding a word changes the rotation. A skeptic's exhaustive run of all 177,147 size-12 systems to 3,000,000 steps (cutting off strings above 200,000 bits) found no halter above 6,328, so a size-12 record needs a long-running system, not a quick search.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/cyclic-tag-busy-beaver-bbct.md
```

Already set up? Say `run V3R1T4S on cyclic-tag-busy-beaver-bbct`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cyclic-tag-busy-beaver-bbct`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
