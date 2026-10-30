# English checkers from the start: the number of move sequences of 30 plies (OEIS A133046 a(30))

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster, or several weeks on one workstation with a transposition-hashed perft (a(30) is about 3.6e20; a(29) was reached in 2020) · open as of 2026-10-30

## The problem

A133046 counts distinct move sequences of n plies from the standard 12-versus-12 English checkers (draughts) position, with forced captures; duplicate king captures (the same pieces captured in different directions) are counted separately. Values to a(28) = 16377718018836900735 come from Aart Bik (a(12)-a(20) in 2009; a(21)-a(28) from distributed runs completed in September 2012; ICGA Journal, December 2012), whose page also gives per-first-move divides for depths 18 to 28. Rein Halbersma was first to compute a(22); Murray Cash confirmed a(23) and a(24), and Paul Byrne confirmed a(23) to a(28). a(29) = 76309690522352444005 was added by Murray Cash on 2020-11-20, and the entry credits no independent confirmation. Checked 2026-10-30: OEIS A133046 (last edited December 2024) ends at a(29), and Bik's page ends at depth 28.

## What counts as a win

CONFIRMED: the exact value of A133046 a(30), absent from OEIS and from any published source (forum posts included) at verification time, from a perft that reproduces a(0..29) exactly (including Bik's per-move divides for depths 18 to 28), published with subtotals over a fixed split ply and confirmed by an independently written checkers move generator on all subtotals or on a random 2% of them, or by a full second run.

## Partial wins

- **p1:** An independent confirmation of a(29) = 76309690522352444005 (or proof of an error) with a per-first-move divide, by code that shares nothing with Murray Cash's program.

## How a win is checked

Reproduce a(0..28) and Bik's divides with the independent generator. Recompute a random 2% of the claimed subtotals at the split ply and check their sum.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A133046>

## Sources

- <https://oeis.org/A133046>
- <http://www.aartbik.com/MISC/checkers.html>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Duplicate captures (a king capturing the same pieces in different directions) are counted separately, per the OEIS comment and Bik's generator; reproduce Bik's divides exactly before running deep.
- The rules are English/American checkers (men capture forward only, no flying kings), not international draughts.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/checkers-perft-ply-30.md
```

Already set up? Say `run V3R1T4S on checkers-perft-ply-30`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `checkers-perft-ply-30`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
