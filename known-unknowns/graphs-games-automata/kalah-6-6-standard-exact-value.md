# Kalah(6,6) under standard capture rules: the exact perfect-play margin (proven only 'first player wins by at least 4')

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (Rawlings' empty-capture solve of Kalah(6,6) took searches totalling 106 days and 55 trillion nodes, with endgame databases for all 38.9 billion positions of 34 or fewer seeds; the standard-rule analysis has been 'ongoing' since 2015) · open as of 2026-10-30

## The problem

Kalah(6,6): 6 houses per side, 6 seeds per house (72 seeds). Standard rules: sow counter-clockwise including your own store but not the opponent's; a last seed in your store gives another move; a last seed in an empty house of your own captures it together with the opposite house's seeds only if that opposite house is non-empty; when one side's houses are empty the game ends and the other player takes the seeds left on their side. Irving, Donkers and Uiterwijk (2000) solved Kalah for all sizes up to 6 houses and 6 seeds except (6,6); Anders Carstensen (2011) proved (6,6) a first-player win under four rule sets, without the margin. Mark Rawlings (2015) found the exact margins of Kalah(6,4) (win by 8) and Kalah(6,5) (win by 10) under standard rules, and of (6,6) under the empty-capture variant (win by 2). For standard Kalah(6,6), Wikipedia's Kalah article (section restored October 2025) gives only: first move 1-2 proven win by at least 2, 1-3 proven win by at least 4, 1-6 and 6 proven losses by at least 2, 2 'trending towards a win', and 1-4, 1-5, 3, 4 and 5 probable ties from very deep searches but unproven; it says further analysis is ongoing. So the game value is known to be at least +4 for the first player, and the article states no upper bound. Task: determine the exact value. Status checked 2026-10-30 on the Wikipedia article.

## What counts as a win

CONFIRMED: the exact perfect-play final store difference of Kalah(6,6) under the standard rules stated above (no capture when the opposite house is empty). The difference is first player minus second player, with seeds left in a side's houses at the end going to that side's owner. It counts only while Wikipedia's Kalah article still lists it as unproven and no other published source gives it. It must be established by two independent exact solvers that share no search, move-generation or endgame-database code. Each solver first reproduces the published empty-capture values of Irving, Donkers and Uiterwijk, Kalah(6,4) = +10 and Kalah(6,5) = +12. Each also reports its standard-rule values for Kalah(6,4) and Kalah(6,5); Wikipedia gives +8 and +10, and any disagreement must be documented with a principal variation. For Kalah(6,6) each run gives the exact value V of a best first move and a proven upper bound of at most V for every other of the 10 distinct first moves (1-2 to 1-6 and 2 to 6). The two runs must agree on V. Endgame databases used by either solver must be built by that solver's own code.

## Partial wins

- **p1:** The exact value of one first move listed as unproven (1-4, 1-5, 2, 3, 4 or 5), or of 1-2 or 1-3 (bounded only from below), confirmed by two independent solvers as in the success criterion.
- **p2:** The first independent confirmation of Rawlings' empty-capture result for Kalah(6,6) (win by 2, with his per-move table) by a solver sharing no code with his.

## How a win is checked

Build both solvers; run the control games; compare per-move values for Kalah(6,6) standard rules. Check the rules implementation on hand-made positions (a capture with an empty opposite house must not capture; extra move on store landing; end-of-game seed assignment). Replay the published principal variations in a third, trivial move generator.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Kalah>

## Sources

- <https://en.wikipedia.org/wiki/Kalah>
- <http://kalaha.krus.dk/>
- <http://graphics.stanford.edu/~irving/papers/irving2000_kalah.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Seed-count endgame databases (all positions with at most k seeds on the board) make the lower part of the tree free; Rawlings' went to 34 seeds, and modern RAM allows more.
- MTD(f) with a null-window solver and enhanced transposition cutoffs; prove 'value >= v' and 'value <= v' as separate searches.
- Start with the move-3 or move-5 lines claimed as probable ties: proving a tie needs both bounds, but each is a narrow-window search.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Rule variants abound (empty capture, end-of-game counting, Kalaha vs Kalah); Carstensen's numbered variations and Wikipedia's 'standard' use different names. State the rules exactly.
- The Rawlings analysis is unpublished and the Wikipedia section is tagged unreferenced; treat its per-move bounds as claims to re-check, not as given.
- 'Win by at least 4' is a lower bound from one move; the true value may be higher or the same.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/kalah-6-6-standard-exact-value.md
```

Already set up? Say `run V3R1T4S on kalah-6-6-standard-exact-value`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `kalah-6-6-standard-exact-value`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
