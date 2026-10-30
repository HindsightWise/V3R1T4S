# Grundy's game: certify an eventual period (or that of 0.6111...), beyond Flammenkamp's 2^39 computation

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for a new range (Flammenkamp's 2012 run took 25 days to reach 2.85e11; his table now reaches 2^39 = 5.5e11); laptop-days for p1 with a sparse-space evaluator · open as of 2026-10-30

## The problem

In Grundy's game a move splits one heap into two non-empty heaps of different sizes. Its Sprague-Grundy sequence (OEIS A002188) begins 0,0,0,1,0,2,1,0,2,... Berlekamp, Conway and Guy (Winning Ways) conjectured that it is eventually periodic, and Nowakowski's Unsolved Problems column (Games of No Chance 6, 2025, problem A2) still lists it as unsolved. Dan Hoey reached 1.1e10 (1995-96), and Achim Flammenkamp reached 2^35 (2002) and 284,944,236,543 (2012-11-25). Flammenkamp's octal-games table (last updated 2026-10-28) and its statistics file stat_grundys now give all G(n) for n < 2^39: 1,287 rare values (the sparse set), the last rare one at n = 48,399,022, depth 51,335,130, largest value 297 (first at n = 21,544,358,589), and 42 zeroes, the last at 1,222. No period. The same table lists 0.6111... (remove one token leaving one or two heaps, or remove a whole heap of at least two tokens), computed to 2^43 with 171 rare values, the last at 2,026, also without a period. The bank's octal entry (octal-games-unsettled-periodicity) excludes exactly these two games. Couples-are-forever is not included here, because Flammenkamp shows it is a shifted copy of the octal game .6, which that entry covers. Flammenkamp remarks that if the rare values die out the sequence must become periodic. Because a heap may be split anywhere, the Guy-Smith window for finite octal games does not apply as stated; a residue argument suggests that checking G(n + p) = G(n) for n0 <= n < 2*n0 + 2p would suffice, but whatever window is used must be proved or cited.

## What counts as a win

CONFIRMED: for Grundy's game or for 0.6111..., an explicit preperiod n0 and period p such that G(n + p) = G(n) for every n >= n0, established by both of the following. (1) An exact check of every value over the finite window that the sufficient condition requires, by a program that shares no code with the claimant's. (2) The sufficient condition itself: either a theorem already published in a refereed source, with its hypotheses verified for this game, or a theorem proved in the submission and formalised in Lean 4, Coq or Isabelle. The recomputed sequence must match Flammenkamp's frequency tables (nim/stat_grundys or nim/stat_.6111) up to his max n, and octal.html must still show the game without a period at verification time. A machine-checked proof that either game is never periodic is an equally full win. A long repeated block or a hash match without (2) does not count.

## Partial wins

- **p1:** The first published independent reproduction of Flammenkamp's Grundy's-game statistics up to heap size 2^35 - 1 (the first table of nim/stat_grundys: the count of every value, the 1,287 rare values and their positions), by a program that shares no code with his or with the programs of Tyler Satchel Orden and Udo Sprute that supported his table in 2026, matching exactly; a demonstration that an entry is wrong also counts.
- **p2:** Grundy's game computed exactly up to 2^40, one doubling beyond Flammenkamp's 2^39, reproduced by a second independent program. Publish the full frequency table, the sparse set, the largest value and its first index; the range up to 2^39 must match stat_grundys. A new rare value beyond n = 48,399,022 found on the way is reported as part of this win.

## How a win is checked

Write an evaluator from the definition (G(n) = mex of G(a) xor G(n - a) for 1 <= a < n/2) and test it on OEIS A002188 (b-file to 20,000 and a.txt to 200,000). Then run it with a sparse-space acceleration whose common/rare split is re-derived, not copied, and compare the value counts with nim/stat_grundys. For a period claim, check G(n + p) = G(n) exactly over the stated window and check the cited or formalised sufficient condition line by line. For 0.6111..., use nim/stat_.6111 and nim/sparse_.6111 in the same way.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://wwwhomes.uni-bielefeld.de/achim/octal.html>

## Sources

- <http://wwwhomes.uni-bielefeld.de/achim/octal.html>
- <http://wwwhomes.uni-bielefeld.de/achim/grundy.html>
- <http://wwwhomes.uni-bielefeld.de/achim/nim/stat_grundys>
- <http://wwwhomes.uni-bielefeld.de/achim/nim/sparse_grundys>
- <http://wwwhomes.uni-bielefeld.de/achim/nim/stat_.6111>
- <https://oeis.org/A002188>
- <https://en.wikipedia.org/wiki/Grundy%27s_game>
- <https://library.slmath.org/books/Book71/files/GONC6-04.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- All the rare values lie below n = 48,399,022, so beyond that point every G(n) is a common value fixed by the xors with the 1,287 rare positions. A proof that no new rare value can appear, plus a shift-register argument of length about last + depth, is the natural route to a sufficient condition.
- For 0.6111... the rare set is tiny (171 values, the last at 2,026) and the run already reaches 2^43, so it may be the cheaper of the two to certify once a valid sufficient condition exists.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- grundy.html (last updated 2021) still says the computation stopped at 284,944,236,543. octal.html and the stat_grundys header ('total=2^39') are newer and are the authority.
- OEIS A002188's data and b-file reach only 200,000 terms; they are a calibration, not the record.
- Couples-are-forever and the octal game .6 are the same game shifted (octal.html), so a period for either belongs to the octal entry, not here.
- Flammenkamp and others are extending these runs; re-fetch octal.html and the stat file before and after a run.
- octal.html credits Tyler Satchel Orden (July 2026) and Udo Sprute (October 2026, a parallel C/OpenMP program) with extending the octal-games sequences, and the 2^39 table of stat_grundys ('total=2^39 bitmask=1') is in a newer output format than the 2^35 table, so it may come from one of those programs: a reproduction for p1 or p2 must share no code with them either.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/grundys-game-periodicity.md
```

Already set up? Say `run V3R1T4S on grundys-game-periodicity`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `grundys-game-periodicity`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
