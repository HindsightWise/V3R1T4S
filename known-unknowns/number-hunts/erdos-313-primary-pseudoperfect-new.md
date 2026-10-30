# Erdős #313: a new primary pseudoperfect number (1/p_1 + ... + 1/p_k = 1 - 1/m), beyond the 11 known

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-hours (port-filling / extension search from known terms) · open as of 2026-10-30

## The problem

Erdős-Graham [ErGr80, p.40] ask whether 1/p_1 + ... + 1/p_k = 1 - 1/m has infinitely many solutions with distinct primes p_i; necessarily m = p_1...p_k, so solutions are the primary pseudoperfect numbers m (sum over p | m of 1/p plus 1/m = 1), OEIS A054377. As of 2026-10-30, 11 are known: the 8 in the OEIS data (2, 6, 42, 1806, 47058, 2214502422, 52495396602, 5998279018951962402), plus three in OEIS comments: 8490421583559688410706771261086 (long known, formerly in the data), 35979351189199316534587473905773572006 (Pedro Martins and Han M. Wang, Apr 2026; Wang, arXiv:2605.21518 'Port fillings', obtained as N(N+1) from N = 5998279018951962402 with N+1 prime), and a 61-digit term with 10 prime factors, 2318487344461212044808266715505249967391337588451045543300838 (Pedro Martins, OEIS comment 2026-09-27). Max Alekseyev: no other terms below 10^24 (OEIS comment, 2026-08-12). Original definition: Butske, Jaje and Mayernik (2000). The erdosproblems.com page still says '8 known'; the OEIS entry is the up-to-date record. Whether infinitely many exist, or any odd one, is open.

## What counts as a win

CONFIRMED: a squarefree integer N > 1 with its complete factorisation into PROVEN primes (deterministic test below 2^64, ECPP/Pocklington certificates above) such that 1/N + sum_{p | N} 1/p = 1 holds exactly (equivalently 1 + sum_{p|N} N/p = N), and N is not among the 11 numbers above nor in the data, comments or b-file of OEIS A054377 re-fetched at verification time.

## Partial wins

- **p1:** A reproducible exhaustive search proving there are no primary pseudoperfect numbers in [10^24, 10^26) other than any listed ones, extending Alekseyev's 10^24 bound, with code an independent verifier reruns.

## How a win is checked

Exact Fraction or integer arithmetic for the defining identity; primality certificates checked with an independent tool (e.g. PARI isprime with certificate, Primo, or a Pocklington check); comparison against the live OEIS entry.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A054377>

## Sources

- <https://www.erdosproblems.com/313>
- <https://oeis.org/A054377>
- <https://arxiv.org/abs/2605.21518>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Wang's port-filling framework: known terms arise from a 'port' (pair of primes/cofactor) that can be completed; enumerate ports systematically.
- Inheritance: if N is a term and N+1 is prime then N(N+1) is a term; test N+1 for each newly found term.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The erdosproblems.com page is stale ('8 known'); the record is the OEIS entry.
- 1 is not a primary pseudoperfect number.
- Giuga numbers (sum 1/p - 1/N integer) are a different sequence already in the bank (giuga-numbers-new).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/erdos-313-primary-pseudoperfect-new.md
```

Already set up? Say `run V3R1T4S on erdos-313-primary-pseudoperfect-new`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-313-primary-pseudoperfect-new`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
