# Busy Beaver for 2-tag systems: settle BB_PT(8) (7 holdouts) or beat a size 8-11 champion

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-minutes to laptop-hours · open as of 2026-10-30

## The problem

A 2-tag system has an alphabet {0, 1, ...} and one production word w_a per symbol: while the tape has at least 2 symbols, read the first symbol a, delete the first 2 symbols and append w_a. Size is |A| + sum of |w_a|. BB_PT(S) is the most steps any size-S 2-tag system takes before halting when started on 00. The bbchallenge wiki's Post Tag System page (last edited 2026-09-16) lists exact values through size 7 (BB_PT(7) = 10, champion 0111_1) and lower bounds above: BB_PT(8) >= 19 (111_20_, 7 holdouts), BB_PT(9) >= 49 (11_021_2, 154 holdouts), BB_PT(10) >= 779 (112_1_002, 1,933 holdouts), BB_PT(11) >= 196,841 (120221_0_2, 11,759 holdouts). It also lists a size-11 Collatz-like cryptid, 11111_20_1, constructed by realsheepthe. Search tools: Shawn Ligocki's Rust enumerator (sligocki/etc, post_tag) and AzertyWasTaken's Busy-Beaver repository.

## What counts as a win

Success means (a) a 2-tag system of size S, 8 <= S <= 11 (size and step conventions of https://wiki.bbchallenge.org/wiki/Post_Tag_System), that halts from 00 after STRICTLY more steps than the bound listed for S on that page, re-fetched live before claiming, verified by direct simulation; or (b) an exact value of BB_PT(S) for some S in 8..11 that the page still lists with ' > =': every size-S system either halts (with its step count) or carries a checkable non-halting certificate (cycle, translated cycle, or another proof re-checked by an independent decider or a proof assistant), and the largest halting count is reported.

## Partial wins

- **p1:** Exact BB_PT(8): all size-8 systems classified, the 7 wiki holdouts each with a non-halting certificate (or a new champion).
- **p2:** Exact BB_PT(9), with all size-9 holdouts certified.
- **p3:** A new champion at size 10 or 11 (criterion (a)).

## How a win is checked

Independent simulator: queue starting 00, at each step read the first symbol, delete two, append its word, stop when fewer than two symbols remain, counting steps (calibration: 0111_1 halts after 10 steps, 111_20_ after 19, 120221_0_2 after 196,841; all reproduced). For exact values, re-enumerate all systems of size S with independent code, check the count, and re-run each non-halting certificate.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Post_Tag_System>

## Sources

- <https://wiki.bbchallenge.org/wiki/Post_Tag_System>
- <https://github.com/sligocki/etc/tree/main/post_tag>
- <https://github.com/AzertyWasTaken/Busy-Beaver/tree/main/Post%20Tag%20System>
- <https://en.wikipedia.org/wiki/Tag_system>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Most holdouts are growing queues; certify them with translated-cycler or 'immortal substring' style arguments (a substring that regenerates itself), as in AzertyWasTaken's decider list.
- Collatz-like holdouts can often be reduced to a closed-form recurrence on block counts, like the cryptid 11111_20_1.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Two conventions are in use: the wiki counts size as |A| + sum |w_a| and does not count an extra halting step, while AzertyWasTaken's results.md counts size as sum |w_a| and counts the halting step (its 'BBPT(5) = 19' is a different function). Use the wiki convention.
- Systems that differ only by renaming non-initial symbols are equivalent; say how duplicates were handled in an exhaustive count.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/post-tag-busy-beaver-bbpt.md
```

Already set up? Say `run V3R1T4S on post-tag-busy-beaver-bbpt`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `post-tag-busy-beaver-bbpt`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
