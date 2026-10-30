# MOONSHOT - a D(n)-quadruple for n in {-3, 3, 5, 8, 12, 20} (disprove Dujella's conjecture)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster · open as of 2026-10-30

## The problem

A D(n)-quadruple is four distinct positive integers with ab + n a perfect square for all six pairs. No such quadruple exists for n = 2 mod 4 (Brown; Gupta-Singh; Mohanty-Ramasamy 1985). Dujella (1993) proved that one exists for every other n outside S = {-4, -3, -1, 3, 5, 8, 12, 20}, and conjectured that none exists for n in S. Bonciocat, Cipu and Mignotte (2022) settled n = -1, which also gives n = -4. Filipin and Jurasic (Glasnik Mat. 57 (2022)) ruled out polynomial D(-3)-quadruples, which leaves the integer case open. Dujella's survey page (live 2026-10-30) still lists the conjecture as open for n in {-3, 3, 5, 8, 12, 20}. Our own check found no D(n)-quadruple with elements <= 3000 for these six n. Credit: Dujella, Filipin, Fuchs, Jurasic, Bonciocat, Cipu, Mignotte and the 1985 authors.

## What counts as a win

CONFIRMED for four distinct positive integers a < b < c < d and n in {-3, 3, 5, 8, 12, 20} with xy + n a perfect square (math.isqrt) for all six pairs. https://web.math.pmf.unizg.hr/~duje/dn.html must still list that n as conjectured impossible (not proven) at verification time, and a same-day check of the references on Dujella's ref.html must find no published proof that no D(n)-quadruple exists for that n. A claimed D(-1)- or D(-4)-quadruple contradicts a published theorem and is a bug.

## Partial wins

- **p1:** Search certificate: for one n in {-3, 3, 5, 8, 12, 20}, an exhaustive search proving that no D(n)-quadruple has largest element <= B, independently reimplemented by the verifier. B must be at least 10^10 and strictly greater than the largest such bound published (the claimant cites it and the verifier confirms). It must ship hashed logs of all D(n)-triples examined, and the verifier reruns sampled ranges.

## How a win is checked

Six exact isqrt checks, under 1 second. For p1, an independent reimplementation reruns sampled triple ranges and compares counts and log hashes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~duje/dn.html>

## Sources

- <https://web.math.pmf.unizg.hr/~duje/dn.html>
- <https://web.math.pmf.unizg.hr/glasnik/vol_57/no2_03.html>

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/dujella-dn-quadruple-exceptional-n.md
```

Already set up? Say `run V3R1T4S on dujella-dn-quadruple-exceptional-n`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dujella-dn-quadruple-exceptional-n`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
