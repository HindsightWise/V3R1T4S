# MOONSHOT - The exact number of groups of order 2048

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (counting about 1.77e15 2-groups mostly without listing them; new theory needed) · open as of 2026-10-30

## The problem

gnu(n), the number of groups of order n up to isomorphism (OEIS A000001), is known for every n < 2048. A000679 (groups of order 2^n) stops at a(10) = 49,487,367,289 (a(9) and a(10) by Eamonn O'Brien; a(10) corrected by David Burrell in 2022). gnu(2048) is unknown. Eick and O'Brien's methods give 1,774,274,116,992,170 groups of order 2^11 with exponent-2 class 2, which is a strict lower bound. Conway, Dietrich and O'Brien ('Counting groups: gnus, moas and other exotica', Math. Intelligencer 2008) expect the true value to agree with it in the first three digits. Eick, Horn and Hulpke ('Constructing groups of small order: recent results and open problems', 2018) treat orders divisible by 2^10 as infeasible to enumerate. Max Horn's table (groups.quendi.de, data of 2023-12-12, site updated 2026-09-14) still lists 2048 as unknown.

## What counts as a win

Success means the exact integer gnu(2048), which must be STRICTLY GREATER than 1,774,274,116,992,170. It must be produced by public, re-runnable code (for example a p-group generation or enumeration method in GAP or Magma, with the split by 2-class and rank reported) and reproduced either by an independent second method or by an independent re-run on separate hardware. The method must reproduce gnu(512) = 10,494,213 and gnu(1024) = 49,487,367,289 as a sanity check.

## Partial wins

- **p1:** The exact number of groups of order 2048 with exponent-2 class exactly 3, from re-runnable code that, run at order 512, reproduces the exponent-2 class-3 count obtained directly from the SmallGroups library (PClassPGroup over the 10,494,213 groups of order 512).

## How a win is checked

Re-run the released code (GAP or Magma) on independent hardware. Check that the per-class or per-rank breakdown sums to the total, that the class-2 part equals 1,774,274,116,992,170, and that the same code gives the known values for orders 2^n with n <= 10.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://groups.quendi.de/>

## Sources

- <https://groups.quendi.de/>
- <https://www.quendi.de/data/papers/EHH2018-small-groups.pdf>
- <https://www.math.auckland.ac.nz/~obrien/research/gnu.pdf>
- <https://oeis.org/A000679>
- <https://oeis.org/A000001>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 2002/2008 value 49,487,365,422 for order 1024 is wrong; the corrected value is 49,487,367,289 (Burrell 2022). Use the corrected value as the sanity check.
- Counting a group twice across p-classes, or mixing exponent-2 class with nilpotency class, gives a wrong total.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/groups-of-order-2048-count.md
```

Already set up? Say `run V3R1T4S on groups-of-order-2048-count`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `groups-of-order-2048-count`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
