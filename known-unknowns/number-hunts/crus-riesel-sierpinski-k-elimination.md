# Conjectures 'R Us: eliminate a remaining k from a Riesel or Sierpinski base conjecture

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

For each base b <= 1030 the Riesel (resp. Sierpinski) conjecture says a specific conjectured k is the smallest k for which k*b^n-1 (resp. k*b^n+1) is composite for every n. Proving it means finding a prime for every smaller eligible k. The Conjectures 'R Us project (Gary Barnes, Mark Rodenkirch and contributors) lists for each base the k's still without a prime and the n-range tested; the unproven page is regenerated continually (last update 2026-10-28). Several Riesel bases still have hundreds of thousands of k's tested only to n = 2500 (on 2026-10-28: base 891 with 763087 k's, 690 with 739852, 876 with 612567, 756 with 604445, 801 with 494394), where candidates have about 7000 digits and a probable-prime test takes about a second.

## What counts as a win

CONFIRMED (full win) for a base b and a k that is listed as remaining for b on the live CRUS Riesel or Sierpinski pages (http://www.noprimeleftbehind.net/crus/vstats_new/crus-unproven.htm and the per-base remaining-k files it links), re-fetched immediately before the claim, plus an exponent n STRICTLY GREATER than the tested n-limit listed for that k, such that k*b^n-1 (Riesel) or k*b^n+1 (Sierpinski) is PROVEN prime (an N+1 or N-1 proof, since b^n is fully factored; probable-prime results alone do not count). Each such prime removes one k (direction: min on the remaining count). Work only on k's or bases marked available, not on reserved ones.

## Partial wins

- **p1:** Base proven: the last remaining k of some base b eliminated, so the base appears among unproven conjectures at verification time but now has a prime for every remaining k.
- **p2:** Range extension certificate: an available k (or a whole available base) sieved and tested with no prime from the listed limit up to at least 1.5 times that limit, with the sieve file and test residues saved so a verifier can re-test a random 2% sample of survivors and re-sieve a random sub-range.

## How a win is checked

Check k is listed as remaining on the live page and n exceeds its listed limit. Prove primality: Sierpinski form with PFGW -tp/-tm or LLR/PRST (Proth/Pocklington N-1 test), or PARI isprime(N,1) for small cases; Riesel form with LLR/PRST (Lucas-Lehmer-Riesel / N+1 test) or PFGW -tp. Confirm k is not a multiple of b (MOB) that maps to another listed k, and that k is not excluded for algebraic factors.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://www.noprimeleftbehind.net/crus/vstats_new/crus-unproven.htm>

## Sources

- <http://www.noprimeleftbehind.net/crus/vstats_new/crus-unproven.htm>
- <http://www.noprimeleftbehind.net/crus/>
- <http://www.noprimeleftbehind.net/crus/Riesel-conjecture-reserves.htm>
- <http://www.noprimeleftbehind.net/crus/Sierp-conjecture-reserves.htm>
- <http://www.noprimeleftbehind.net/crus/Riesel-conjectures.htm>
- <http://www.noprimeleftbehind.net/crus/tab/CRUS_tab.htm>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Pick available bases with huge k-counts at n = 2500: sieve all k together with srsieve2/sr2sieve to depth ~1e9, then PRP-test in n order. Each prime found removes a k, so expected yield per hour is high.
- Portfolio allocation (imported from finance, Kelly criterion): weight each k by its Nash weight / expected primes per CPU-second given candidate size, and rebalance the queue every hour as k's drop out.
- Survival analysis (imported from biostatistics): model 'time to first prime' per k from its sieve survival rate and stop testing k's whose hazard falls below the base average.
- Error-checked arithmetic (imported from numerical analysis): use PRST/LLR with Gerbicz error checking so a hardware glitch never produces a false prime or a false composite.
- Look for k's with partial algebraic factorizations (k = m^2 for Riesel, k = m^4 forms, etc.) on the remaining lists: proving such a k can never yield a prime for an n-class also shrinks the problem, but must follow CRUS conventions.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A probable prime is not a proof; CRUS-style eliminations need an N-1 or N+1 primality proof.
- Multiples of the base (k divisible by b) duplicate another k at n+1; they are excluded from the lists and do not count.
- A prime with n below the listed test limit means a transcription error or a wrong k, not a discovery.
- Confusing Riesel (-1) with Sierpinski (+1), or base b with base b^2 lists.
- Working on reserved k's duplicates someone's running effort; the claim may already exist unreported.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/crus-riesel-sierpinski-k-elimination.md
```

Already set up? Say `run V3R1T4S on crus-riesel-sierpinski-k-elimination`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `crus-riesel-sierpinski-k-elimination`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
