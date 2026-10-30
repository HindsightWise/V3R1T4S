# Number of groups of order n: settle an order up to 20,000 that is still unknown in Max Horn's table (smallest: 3072, 4096, 4608, 5120, 6144, 6400, 6912, 7168)

🃏 **Wildcard** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (GAP GrpConst / Frattini-extension or Eick-Horn-Hulpke counting methods; some orders need cluster) · open as of 2026-10-30

## The problem

Max Horn's table of gnu(n) for n <= 50,000 (groups.quendi.de; data from the SmallGroups library of Besche, Eick and O'Brien, GrpConst, Archer's Zphi method, and Burrell 2023) shows 134 orders as unknown. Up to 20,000 it shows 37 unknown orders: 2048, 3072, 4096, 4608, 5120, 6144, 6400, 6912, 7168, 7680, 8192, 8748, 9216, 10240, 10368, 10752, 11264, 11520, 12288, 12544, 12800, 13122, 13312, 13824, 14336, 15360, 16000, 16128, 16384, 16896, 17408, 17496, 17920, 18432, 19200, 19456 and 19968. The raw data file gap/grps.json marks one more, 19683 = 3^9, as unknown, but the page fills it in with Burrell's count 5,937,876,645 (Comm. Algebra 51 (2023)). Eick, Horn and Hulpke (2018) sort the hard cases into orders divisible by 2^10 or 3^9, orders with 2^9 p as a proper divisor (p in {3,5,7}), and orders divisible by 2^8 p^2. Their 'exceptional' orders 8748 = 2^2 3^7, 10368 = 2^7 3^4, 13122 = 2 3^8, 16000 = 2^7 5^3 and 17496 = 2^3 3^7 have known nilpotent counts but unknown solvable counts (18816 has since been filled in the table). 2048 is a separate moonshot entry in this bank.

## What counts as a win

Success means the exact value gnu(n) for at least one order n <= 20,000, other than 2048 and 19683, that groups.quendi.de lists as unknown at verification time. It must come from public, re-runnable GAP/Magma code and be reproduced by a second independent method or an independent re-run, as Eick-Horn-Hulpke did for their 1,875 doubly checked orders. The nilpotent part must match the known count where one is published (for example 18,620 for 8748, 34,920 for 10368, 1,396,077 for 13122, 11,640 for 16000, 46,550 for 17496).

## Partial wins

- **p1:** The exact gnu(n) for an order 20,000 < n <= 50,000 listed as unknown on groups.quendi.de, with the same reproducibility standard.
- **p2:** For one of the exceptional orders 8748, 10368, 13122, 16000 or 17496 (all solvable by Burnside's p^a q^b theorem): the exact number of groups of that order that have a normal Sylow subgroup, reproduced by two independent methods (for example orbit counting of Hom(Q, Aut(P)) and an explicit GAP construction).

## How a win is checked

Re-run the released scripts on independent hardware. Check that the counts split into nilpotent, solvable non-nilpotent and non-solvable parts that match the table's known parts, and that the same pipeline reproduces several neighbouring known orders from the table (for example 2304 = 15,756,130 and 1536 = 408,641,062).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://groups.quendi.de/>

## Sources

- <https://groups.quendi.de/>
- <https://www.quendi.de/data/papers/EHH2018-small-groups.pdf>
- <https://github.com/alex-konovalov/gnu>
- <https://oeis.org/A000001>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The table's JSON (gap/grps.json) stores [non-solvable, solvable, ...] per order, so the total is the sum of the first two fields; a -1 in the second field means unknown. For prime-power orders the page ignores the JSON and uses its own nilpotent-count table in js/code.js, so read the rendered page, not only the JSON.
- 19683 shows as -1 in the JSON but the page lists it as known (5,937,876,645, Burrell 2023); do not claim it.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/gnu-unknown-orders-below-20000.md
```

Already set up? Say `run V3R1T4S on gnu-unknown-orders-below-20000`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `gnu-unknown-orders-below-20000`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
