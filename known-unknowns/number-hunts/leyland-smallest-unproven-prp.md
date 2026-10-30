# Leyland primes: prove the smallest unproven Leyland PRP (x^y+y^x: 13 749 digits; x^y-y^x: 10 483 digits)

🔢 **Number hunts** · standard · tractability ★★★☆☆ · compute: laptop-days (ECPP of a 10 000-14 000-digit number with no useful N-1/N+1 structure; CM or Primo) · open as of 2026-10-30

## The problem

Leyland numbers of the first kind are x^y+y^x with 1 < x < y, and of the second kind x^y-y^x. Their N-1 and N+1 do not factor usefully, so large ones can only be proven by ECPP. Norman Luhn's tables number every known Leyland (probable) prime and mark each Prime or PRP. The first-kind table (updated 06 Oct 2026) has 2853 entries, 416 proven. Every first-kind Leyland prime below 13 749 digits is proven, up to the 379th, 471^5140+5140^471 (13740 digits). The 380th, 2133^4130+4130^2133 (13749 digits, found by Paul Leyland in May 2002), is the smallest still only PRP. The second-kind table (27 Oct 2026) has 3675 entries, 726 proven. The first 692 are proven, and the 693rd, 1635^3262-3262^1635 (10483 digits, Norbert Schneider, 2011), is the smallest PRP. The largest proven first-kind entry is 5^104824+104824^5 (73269 digits): Andrey Kulsha found it as a PRP in 2010, and its ECPP proof (Feb 2023) is #3 on the PrimePages ECPP top-20. Credit goes to Paul Leyland, Andrey Kulsha, Norbert Schneider, Henri Lifchitz, Mark Rodenkirch, Hans Havermann (OEIS A094133) and Luhn.

## What counts as a win

CONFIRMED (full win) for a complete, independently verified primality certificate (Primo, CM or PARI/GP ECPP) for the Leyland number that is the smallest-digit entry still marked PRP on the live Luhn table of its kind (https://pzktupel.de/Primetables/TableLeyland1.php or TableLeyland2.php, re-fetched immediately before the claim; on 2026-10-30 these are 2133^4130+4130^2133 and 1635^3262-3262^1635). This advances the contiguous proven range of that kind (direction: max on the number of smallest Leyland primes all proven: 379 for the first kind, 692 for the second).

## Partial wins

- **p1:** A verified certificate for any other entry marked PRP on either live Leyland table with fewer than 20 000 digits (117 first-kind and 348 second-kind PRPs above the current boundary entries and below 20 000 digits on 2026-10-30).
- **p2:** A verified certificate for any entry marked PRP on either live Leyland table with at least 20 000 digits.

## How a win is checked

Recompute N = x^y +/- y^x and compare it with the certificate's N. Verify the certificate with an independent checker (PARI/GP primecertisvalid, CM's checker, or a Primo-certificate verifier) on the verifier's own install. Confirm on the live table that the entry is marked PRP and is the smallest PRP of its kind for the full win.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://pzktupel.de/Primetables/TableLeyland1.php>

## Sources

- <https://pzktupel.de/Primetables/TableLeyland1.php>
- <https://pzktupel.de/Primetables/TableLeyland2.php>
- <https://oeis.org/A094133>
- <http://www.primenumbers.net/prptop/prptop.php>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- CM (FastECPP) on all cores: at about 10 000-14 000 digits expect a few to a few tens of CPU-days.
- Do the second-kind boundary entry first: at 10 483 digits it is about 3 times cheaper than the 13 749-digit first-kind one, since ECPP cost grows roughly with the fourth power of the digit count ((13749/10483)^4 = 2.96).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Proofs here go in size order, which suggests an organised effort. Look for a reservation thread on mersenneforum and avoid duplicating a claimed number.
- Luhn mirrors factordb status. A certificate may already be uploaded but not yet reflected, so check factordb in a browser before starting.
- x^y-y^x with y > x is a different list from x^y+y^x. The boundary entries differ.
- Over-reliance on Primo's own 'verified' message: the verifier should use an independent checker.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/leyland-smallest-unproven-prp.md
```

Already set up? Say `run V3R1T4S on leyland-smallest-unproven-prp`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `leyland-smallest-unproven-prp`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
