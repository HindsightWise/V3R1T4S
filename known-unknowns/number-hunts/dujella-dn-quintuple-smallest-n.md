# Diophantine D(n)-quintuples: a quintuple with -255 < n < 256 (beat Dujella's n1 <= 256 or n2 >= -255)

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

A set of m positive integers has property D(n) if a_i*a_j + n is a perfect square for all i < j. Andrej Dujella's survey page (section 3.2 of the Diophantine m-tuples page, which cites results up to Bonciocat-Cipu-Mignotte 2022) asks for the least positive n1 and the greatest negative n2 for which a D(n)-quintuple exists. It records n1 <= 256 and n2 >= -255, from {1, 33, 105, 320, 18240} and {5, 21, 64, 285, 6720} (property D(256)) and {8, 32, 77, 203, 528} (property D(-255)), all checked by us. Some cases are proven impossible: no D(1)-quintuple (He-Togbe-Ziegler 2019), no D(4)-quintuple (Bliznac Trebjesanin-Filipin 2019), no D(-1)- or D(-4)-quadruple (Bonciocat-Cipu-Mignotte 2022), and no D(n)-quadruple for n = 2 mod 4 (Brown; Gupta-Singh; Mohanty-Ramasamy 1985). Our own exhaustive checks (2026-10-30) found no D(n)-quintuple with all elements <= 100000 for 0 < |n| < 256 (the same search recovers exactly the three record sets above). Target: a D(n)-quintuple with -255 < n < 256. Credit: Dujella and coauthors, Filipin, Fuchs, He, Togbe, Ziegler, Bonciocat, Cipu, Mignotte.

## What counts as a win

CONFIRMED for five distinct positive integers a1..a5 and an integer n with n != 0 and -255 < n < 256, such that a_i*a_j + n is a perfect square (math.isqrt) for all 10 pairs. It must also strictly beat (direction: smaller |n| on that sign side) the n1/n2 bounds stated on https://web.math.pmf.unizg.hr/~duje/dn.html at verification time (n1 <= 256, n2 >= -255 on 2026-10-30, context only). Claims for n = 1, n = 4, n = -1, n = -4 or n = 2 mod 4 contradict published theorems and are bugs.

## Partial wins

- **p1:** Search certificate: for every n with 0 < |n| < 256 that no theorem above excludes, an exhaustive search proving that there is no D(n)-quintuple with all elements <= B. B must be at least 10^8 and strictly greater than any bound published for this question. The verifier reimplements it independently, for example by extending D(n)-triples through the standard Pell-system bound, and reruns randomly chosen n, comparing the per-n counts of D(n)-quadruples found.
- **p2:** A new record-side example: a D(256)- or D(-255)-quintuple of distinct positive integers that is not, as a set, any of the three on dn.html and not in the papers dn.html cites for them (its references [62] and [68]), as checked by the verifier at verification time.

## How a win is checked

Ten exact isqrt checks plus the range and exclusion checks, under 1 second. For p1, independent reimplementation and sampled per-n reruns with count and hash comparison.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~duje/dn.html>

## Sources

- <https://web.math.pmf.unizg.hr/~duje/dn.html>
- <https://web.math.pmf.unizg.hr/~duje/dtuples.html>
- <https://arxiv.org/abs/2011.01684>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Extend D(n)-quadruples instead of searching blindly. For a quadruple {a,b,c,d}, the fifth element e satisfies four simultaneous conditions a*e+n = square and so on. Use the regular-extension formulas and the elliptic curve y^2 = (ax+n)(bx+n)(cx+n) to find rational points that happen to be integers.
- Scale rational D(1)-quintuples (Dujella-Kazalicki-Mikic-Szikszai) with small common denominator q. Multiplying by q gives integer D(q^2)-quintuples, so q <= 15 would beat n1 = 256.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The definition on dn.html uses positive integers. Quintuples with negative or zero elements (allowed in some papers) are not the same record.
- Repeated elements are not allowed. Quintuples of the form k*S for a D(n/k^2)-quintuple S are fine but must still have |n| inside the range.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/dujella-dn-quintuple-smallest-n.md
```

Already set up? Say `run V3R1T4S on dujella-dn-quintuple-smallest-n`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dujella-dn-quintuple-smallest-n`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
