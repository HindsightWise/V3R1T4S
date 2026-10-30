# Wieferich primes to other bases: a new p with b^(p-1) == 1 (mod p^2) beyond Richard Fischer's searched limits (incl. Mirimanoff base 3)

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (per base or batch of bases; composite bases come almost free from prime-base residues) · open as of 2026-10-30

## The problem

A base-b Wieferich prime is a prime p with b^(p-1) == 1 (mod p^2). Base 2 is a separate target, wieferich-base-2-beyond-2-64. Richard Fischer (fermatquotient.com, building on Wilfrid Keller and Joerg Richstein's tables) maintains two tables. The first, FermQ_Sort.txt, covers bases 2 to 1052. Its stated limits: bases whose largest prime factor is at most 149 are searched to 2.00e14, the other bases to 7.4e13, and bases 3, 5 and 7 beyond 1.2e15. Its latest record is base 770 with p = 194092950328757 (2024-11-01), and News.txt was dated 2025-09-01. The second, FermQ_Sorg.txt, covers bases 2 to 10125, all searched to 4.8e12, and was updated 2026-10-21. Its statistics table matches the heuristic ln-ln count well (549 hits observed against 552.2 expected for 1e12 to 4.8e12). Base 3 (the Mirimanoff primes, OEIS A014127) has only 11 and 1006003 known; OEIS cites Dorais-Klyve's search to 9.7e14, and Fischer gives more than 1.2e15. Extending all 10000 bases from 4.8e12 to 1e13 should yield about 10000*ln(ln 1e13/ln 4.8e12), roughly 250 new pairs. A new pair can be checked with one modular exponentiation.

## What counts as a win

CONFIRMED (full win) for each pair (b, p): an integer base 3 <= b <= 10125 that is not a perfect power (a pair for b = a^k with p not dividing k is the same pair as for a), and a proven prime p not dividing b with pow(b, p-1, p^2) == 1. The p must also be STRICTLY GREATER than that base's searched limit stated in the live FermQ_Sort.txt (for b <= 1052) or FermQ_Sorg.txt (for 1053 <= b <= 10125), and absent from that base's row in both files and from OEIS (the base-b Wieferich sequence, if one exists). All of these are re-fetched immediately before the claim. Each new pair counts once. Direction: maximize the number of new pairs. A new Mirimanoff prime (b = 3, p > 1.2e15) or a new double Wieferich pair (with p^(b-1) == 1 mod b^2 as well, absent from SwitchFermQ.txt) is flagged as a headline result.

## Partial wins

- **p1:** New pair for a base 10125 < b < 65537 that is not a perfect power, with p above 1e12, b^(p-1) == 1 mod p^2 checked exactly, and absent from both Fischer tables and OEIS.
- **p2:** Range certificate: one base b <= 1052 extended contiguously from its stated limit by at least 20%, with Fermat quotients q_p(b) mod p published in hashed blocks and surviving a random 1% recomputation by the verifier.

## How a win is checked

Prove p prime (BPSW plus PARI isprime). Check pow(b, p-1, p*p) == 1 with Python big integers. Read the base's row and the stated limit lines in the live Fischer file (latin-1 text) and check that p is greater and absent. For double pairs, also check pow(p, b-1, b*b) == 1.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.fermatquotient.com/FermatQuotienten/FermQ_Sorg.txt>

## Sources

- <http://www.fermatquotient.com/>
- <http://www.fermatquotient.com/FermatQuotienten/FermQ_Sort.txt>
- <http://www.fermatquotient.com/FermatQuotienten/FermQ_Sorg.txt>
- <http://www.fermatquotient.com/FermatQuotienten/News.txt>
- <http://www.fermatquotient.com/FermatQuotienten/FermatQ3.txt>
- <http://www.fermatquotient.com/FermatQuotienten/SwitchFermQ.txt>
- <https://oeis.org/A014127>
- <https://cs.uwaterloo.ca/journals/JIS/VOL14/Klyve/klyve3.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- For each prime p, compute q_p(r) mod p for the 1229 prime bases r <= 10125, then get every composite base's quotient additively (q_p(ab) = q_p(a) + q_p(b) mod p). This tests all 10000 bases at the cost of the prime bases.
- Montgomery arithmetic modulo p^2 with p < 2^50 fits in 128-bit words; a GPU segmented sieve feeds primes.
- Prioritise the bases 1053-10125 range at 4.8e12, where yield per CPU-hour is highest.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The two Fischer tables have different limits: a p between 4.8e12 and 7.4e13 for a base <= 1052 is already searched.
- Perfect-power bases (4, 8, 9, 16, 25, ...) repeat their root's pairs and are excluded; a pair for a power of 2 is a base-2 Wieferich prime, which is the separate target wieferich-base-2-beyond-2-64.
- Base 65537 appears in FermQ_Sort.txt with its own limit (1.2e14 on 2026-10-30).
- p dividing b is trivially excluded.
- The files are latin-1 German text; read the limit lines carefully ('durchsucht bis').

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/wieferich-other-bases-fischer-table.md
```

Already set up? Say `run V3R1T4S on wieferich-other-bases-fischer-table`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `wieferich-other-bases-fischer-table`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
