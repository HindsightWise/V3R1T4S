# Giuga numbers: find one not yet known

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

A Giuga number is a composite n such that p divides n/p - 1 for every prime p dividing n (equivalently, sum of 1/p over p | n minus 1/n is a positive integer). Giuga's primality conjecture says no Giuga number is a Carmichael number. OEIS A007850 (credited to D. Borwein, J. M. Borwein, P. B. Borwein and R. Girgensohn) lists 12 terms up to 1910667181420507984555759916338506, records Fred Schneider's 2006 exhaustive search showing no further Giuga numbers with 8 or fewer prime factors, and mentions one further 97-digit Giuga number with 10 prime factors (Butske, Jaje and Mayernik, 2000) that may not be the next term. All known Giuga numbers have sum 1/p - 1/n = 1.

## What counts as a win

CONFIRMED (full win) for a squarefree composite n given with its complete proven prime factorisation such that for every prime p | n, (n/p - 1) mod p == 0, and n is absent from the data, comments and b-file of https://oeis.org/A007850 (re-fetched immediately before the claim), from the Butske-Jaje-Mayernik paper's list, and from the mersenneforum Giuga thread.

## Partial wins

- **p1:** Exhaustive 9-factor certificate: a complete search, reimplemented by the verifier, listing every Giuga number with exactly 9 prime factors (extending Schneider's 8-factor search), with the search tree logs saved so that random branches can be rerun.
- **p2:** A Giuga number with sum 1/p - 1/n = 2 (or larger); none is known.

## How a win is checked

Python big integers: multiply the primes, prove each prime (BPSW + PARI isprime), check squarefree, check (n//p - 1) % p == 0 for every p, compute sum 1/p - 1/n with fractions.Fraction. Diff n against the OEIS data, b-file and comments.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A007850>

## Sources

- <https://oeis.org/A007850>
- <https://oeis.org/A007850/b007850.txt>
- <https://en.wikipedia.org/wiki/Giuga_number>
- <http://www.mersenneforum.org/showthread.php?t=4666>
- <https://doi.org/10.1090/S0025-5718-99-01088-1>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Borwein-Girgensohn completion: fix the first m-2 primes; the last two primes are determined by factoring a single explicit integer, so the search is a tree whose leaves are factorisations.
- Branch-and-bound on Egyptian fractions (imported from operations research): the condition sum 1/p - 1/n = 1 is an Egyptian-fraction equation over primes; bound remaining sums tightly to prune.
- Arithmetic-derivative fixed points (Grau and Oller-Marcen): n is Giuga iff n' = a*n + 1; search for fixed points of the map n -> n' - n with structured n.
- Perfectly weighted graphs (Butske, Jaje, Mayernik): use the graph-theoretic reformulation to enumerate compatible prime sets as a constraint-satisfaction problem (imported from combinatorial search / SAT).
- Use ECM/SIQS-friendly ordering: choose search branches whose completion integer is smooth or small so the factoring at each leaf finishes in seconds.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Non-squarefree n are not Giuga numbers.
- Primary pseudoperfect numbers satisfy sum 1/p + 1/n = 1 (plus sign) and are a different sequence (A054377).
- The 97-digit 10-factor example is already known (in the OEIS comments); rediscovering it is not new.
- An unproven large prime factor leaves the claim unproven.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/giuga-numbers-new.md
```

Already set up? Say `run V3R1T4S on giuga-numbers-new`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `giuga-numbers-new`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
