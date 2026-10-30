# MOONSHOT - Euclid-Mullin sequence: the 52nd term (least prime factor of a 335-digit number)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (GNFS on a C335 is far beyond public records; ECM is the realistic route) · open as of 2026-10-30

## The problem

The Euclid-Mullin sequence (OEIS A000945) has a(1) = 2, and a(n+1) is the least prime factor of 1 + a(1)*...*a(n). Mullin (1963) asked whether it contains every prime, which is still open; 41 is the smallest prime absent from the known terms a(1)..a(51), and Booker and Irvine (2016) studied the related Euclid-Mullin graph. Wagstaff (1993) computed it through a(43). The 180-digit product+1 behind a(44) was factored by GNFS in March 2010 (mersenneforum). Ryan Propper found a(48), a 75-digit factor of a 256-digit number, by ECM in September 2012, and the OEIS b-file (Propper; first 47 terms by T. D. Noe) now runs through a(51) = 211. a(52) is the least prime factor of 1 + a(1)*...*a(51), a composite of 335 digits (checked: it fails a base-3 Fermat test and has no factor below 2*10^5). OEIS still flags this as hard (keywords nonn, nice, hard).

## What counts as a win

CONFIRMED (full win) for a prime p, proven prime, that divides N = 1 + a(1)*...*a(51) (terms taken from the OEIS A000945 b-file, re-fetched immediately before the claim), together with a proof that p is the least prime factor of N. Acceptable proofs: N/p proven prime with N/p > p, or a complete proven-prime factorisation of N.

## Partial wins

- **p1:** Any proven prime proper factor of N (the least or not), with its cofactor's status stated (prime, composite, or split further).

## How a win is checked

Rebuild N from the b-file with big integers (it has 335 digits), check N mod p = 0, prove every prime with ECPP, and when the factorisation is complete take the minimum factor. Then check the OEIS entry still ends at a(51).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A000945>

## Sources

- <https://oeis.org/A000945>
- <https://oeis.org/A000945/b000945.txt>
- <https://arxiv.org/abs/1508.03039>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Deep ECM (B1 >= 3e9) is the realistic route, as for a(48) in 2012; its value rests on how much ECM has already been done, which FactorDB's 'Status of EM51' records but which blocked automated fetches on 2026-10-30.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Finding a factor is not enough for a(52): the least prime factor needs the full factorisation (or a prime cofactor).
- OEIS's FactorDB link may hold new partial results; check it by hand before claiming novelty.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/euclid-mullin-a52.md
```

Already set up? Say `run V3R1T4S on euclid-mullin-a52`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `euclid-mullin-a52`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
