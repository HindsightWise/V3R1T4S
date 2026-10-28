# Prime k-tuplets: a larger proven prime k-tuplet than the largest known for a stale (k, pattern) row (k = 11..17)

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Norman Luhn's pzktupel.de 'Largest known prime k-tuplets to given pattern' table (last updated 18 Oct 2026) lists, for each k and admissible minimal pattern, the largest known proven prime k-tuplet. Small k are dominated by Riecoin (whose 8- and 9-tuplets fill the 2026 history) and by Ryan Propper and Serge Batalov (k = 11, May 2026), but some rows for k >= 12 are old and small (e.g. k=12 pattern d = 0,6,10,12,16,22,24,30,34,36,40,42: 75 digits, Michael Stocker, 30 Sep 2014). Target: a proven prime k-tuplet for some (k, pattern) row with more digits/larger value than that row's entry.

## What counts as a win

Success means an explicit integer n such that n + d is prime for every offset d of one admissible minimal pattern row on https://pzktupel.de/largest.php (re-fetched live immediately before claiming), with each member PROVEN prime (PARI/GP `primecertify` ECPP certificate verified by an independent run of `primecertify`/`checkprimecert`, or Primo certificate), and n STRICTLY GREATER (direction: max) than the start of that row's listed tuplet; also not in the page's 'Recent additions' or kthist2026 history.

## Partial wins

- **p1:** Any proven k-tuplet that would enter the site's top-10 list for that k (top10.php), verified.
- **p2:** A proven tuplet beating a row for a SECOND pattern of the same k.

## How a win is checked

Independent PARI/GP: for each member isprime() and primecertify(); check pattern offsets equal the row's admissible pattern; compare against the live table. Seconds to minutes for <= 150-digit numbers.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pzktupel.de/largest.php>

## Sources

- <https://pzktupel.de/largest.php>
- <https://pzktupel.de/top10.php>
- <https://pzktupel.de/ktuplets.php>
- <https://pzktupel.de/KTHIST/kthist2026.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search form n = m·P# + c with c chosen so the pattern is admissible mod every prime ≤ P (CRT on residue classes), then sieve m over a large range for all k offsets simultaneously.
- Pick rows with the smallest digit counts relative to neighbours (stale rows), estimate expected time from the Hardy-Littlewood constant for that pattern (the site's ktpatt_hl.php) and pick the cheapest.
- Cross-domain import (bioinformatics k-mer seeding / spaced seeds): treat the pattern as a spaced seed and use bit-parallel shift-and over sieve bitmaps to find positions where all k offsets survive.
- Cross-domain import (lottery/wheel design in operations research): choose the primorial wheel and residue classes by a covering-design-style optimisation to maximise surviving density per unit of sieve work.
- Fermat-test (base 2) filter in gmpy2 on survivors, BPSW, then ECPP only on full hits.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Patterns must be the exact admissible minimal pattern listed (different patterns of the same k are different rows).
- PRP is not enough for this table; all members must be proven.
- The table also lists 'early discoveries'; compare against the 'largest known' column only.
- Riecoin miners can produce large 9/10-tuplets daily; avoid those rows and re-fetch before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/pzktupel-largest-ktuplet-stale-patterns.md
```

Already set up? Say `run V3R1T4S on pzktupel-largest-ktuplet-stale-patterns`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pzktupel-largest-ktuplet-stale-patterns`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
