# Least quadratic non-residue records: the next term of A000229 (least prime whose least QNR is the 39th prime, 167) or of a sibling prescribed-character sequence

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (CRT/wheel enumeration of candidates with prescribed Legendre symbols; minutes to verify) · open as of 2026-10-30

## The problem

Lehmer, Lehmer and Shanks (Math. Comp. 24, 1970) studied integers with prescribed quadratic character modulo the first primes, the extreme cases of the least quadratic non-residue problem. OEIS keeps several such record sequences, and they have been extended very unevenly. On 2026-10-30: A000229 (least m, always a prime q, whose least quadratic non-residue is prime(n)) has b-file terms n = 1..38 from Tomas Oliveira e Silva's tables, ending a(38) = 70864718555231 (least QNR 163). His exhaustive, double-checked run over all primes up to 10^14 (table q_B, the column the b-file comes from) has no entry for 167, so a(39) > 10^14. The sibling b-files bracket it much more tightly. Since 2 must be a QR, q = 1 or 7 mod 8. A002223 (least prime q = 7 mod 8 with the first n primes all QRs; b-file n = 1..57 by Jinyuan Wang, ending a(57) = 3546374752298322551) has a(38) = 317398900373231, whose least QNR is exactly 167, so a(39) <= 317398900373231. A002224 (the same with q = 1 mod 8; b-file n = 1..41 by Michael Hortmann, more terms from Mike Oakes, 2022) has a(38) = a(39) = 112434732901969 with least QNR 173, so any q = 1 mod 8 with least QNR 167 exceeds it. Hence a(39) is either 317398900373231 or the least prime q = 1 mod 8 in (112434732901969, 317398900373231) with least QNR 167, a window nobody has searched for this condition. The same b-files already imply a(40) = 112434732901969 and a(42) = 178936222537081 (= A002224(41), least QNR 181), which OEIS cannot list before a(39); a(41) (least QNR 179) exceeds 1.789 x 10^14 and is open. Further siblings: A002224 ends at a(41) = 178936222537081, A045535 (least negative pseudosquare) at a(50) = 423414931359807911 (Bert Dobbelaere, 2021), A001992 (least prime = 5 mod 8 that is a QNR of every odd prime <= p) at a(55) = 637754768063384837 (b-file by Jinyuan Wang, extended 2026), and the pseudosquares A002189 at L_373 = a(73) = 4235025223080597503519329 (J. Sorenson's 2010 parallel doubly focused sieve, which also showed L_379 > 10^25; b-file by Charles R Greathouse IV from D. J. Bernstein's page). Target: the next term of any of these sequences, with a proof of minimality.

## What counts as a win

Success means a value q for the next unknown index of A000229 (n = 39), A002223 (n = 58), A002224 (n = 42), A045535 (n = 51), A001992 (n = 56) or A002189 (n = 74). Those indices are re-fetched from the live OEIS b-files immediately before claiming and must still be absent. The claim must satisfy two checks. (1) Property: q has exactly the prescribed character, verified by an independent script (Euler's criterion or the Jacobi symbol for every prime up to the bound), plus a deterministic primality proof where the sequence requires a prime (BPSW plus a Pocklington/ECPP certificate above 3.3e24). (2) Minimality: a complete search shows that no smaller integer has the property. For A000229(39) the search may start from the bracket, so that only primes q = 1 mod 8 in (112434732901969, 317398900373231) need checking, but only if the claimant's enumerator first reproduces A002223(38) = 317398900373231 and A002224(38) = 112434732901969 from 1. Otherwise it starts from 1. The skeptic re-runs that search with a separately written enumerator (a different modulus split, or a plain sieve on a sub-range), and it must find nothing below q. Direction: a new term (index strictly beyond the b-file). No OEIS submission is made by the agent.

## Partial wins

- **p1:** A certified lower bound when the next term is not settled: an independently re-run exhaustive search showing either that no prime q = 1 mod 8 in (112434732901969, 2 x 10^14] has least QNR 167 (which narrows A000229(39) to (2 x 10^14, 317398900373231]), or that A002224(42) exceeds 10^16.
- **p2:** An independent re-computation that confirms (or corrects) the last five listed terms of A000229, A002223 or A002224 by a method different from the original sieve.

## How a win is checked

Property check with Python big integers: pow(p, (q-1)/2, q) for each prime p up to the index prime (seconds). Minimality: re-run the claimant's enumeration from scratch using a different split of the CRT modulus (e.g. Bernstein-style doubly focused enumeration against a wheel sieve over residues mod 8*3*5*...*37). Cross-check it on known values: A000229 a(30)..a(38), A002223(38) = 317398900373231 and A002224(38) = 112434732901969.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A000229>

## Sources

- <https://oeis.org/A000229>
- <https://oeis.org/A000229/b000229.txt>
- <https://oeis.org/A002224>
- <https://oeis.org/A045535>
- <https://oeis.org/A001992>
- <https://oeis.org/A002189>
- <https://arxiv.org/abs/1001.3316>
- <https://cr.yp.to/focus.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Doubly focused enumeration (Bernstein; Sorenson 2010): split the prime set into two groups, enumerate residues mod M1 and M2 that satisfy the character conditions, and combine them in sorted order, so the work is about sqrt of the candidate count.
- For A000229(39) only q = 1 mod 8 below 317398900373231 is left. For such q, (p/q) = (q/p) by reciprocity, so q needs (q/p) = 1 for the odd primes p < 167 and (q/167) = -1. These are residue conditions mod 8*3*5*...*167, with density about 2^-38 among q = 1 mod 8. Expect a handful of hits in the 2 x 10^14-wide window.
- Calibrate on the known terms first: an enumerator that reproduces A000229 a(30)..a(38), A002224(35..41) and A002223(35..38) is trustworthy.
- Keep going past the bracket: the same q = 1 mod 8 pass beyond 1.789 x 10^14, plus a q = 7 mod 8 pass beyond A002223(40) = 501108392233679, settles A000229(41) (least QNR 179), and the 1 mod 8 pass also serves A002224(42).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A000229's offset: a(n) is the least prime whose least QNR is prime(n), counting 2 as prime(1); A002189 and A045535 index by odd primes. Off-by-one indices give wrong targets.
- Minimality is the hard part: listing a q with the right character is not a term unless no smaller q exists. Partial windows do not count.
- Deterministic Miller-Rabin base sets are proven only up to about 3.3e24; above that, give a real primality certificate.
- The sibling b-files constrain A000229: a(39) <= A002223(38) = 317398900373231, and a(40) and a(42) are already implied, so they are not new results. A claimed a(39) above 317398900373231 is wrong.
- Re-check the b-files on the day: these sequences are being extended by individuals (A001992 and A002223 changed in April 2026).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/least-qnr-prescribed-quadratic-character-next-terms.md
```

Already set up? Say `run V3R1T4S on least-qnr-prescribed-quadratic-character-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `least-qnr-prescribed-quadratic-character-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
