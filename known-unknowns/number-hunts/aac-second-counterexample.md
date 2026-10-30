# Ankeny-Artin-Chowla after Reinhart's counterexample: a second prime p = 1 mod 4 with p | y, or an independent check below 3.4e14

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (Reinhart's search of [1e14, 3.4e14] took about 1200 hours on 162 cores); a partial-win interval of 1e12 is laptop-days on 10 cores · open as of 2026-10-30

## The problem

For a prime p = 1 mod 4 let K = Q(sqrt p), omega = (1 + sqrt p)/2, and let epsilon = x + y*omega > 1 be the fundamental unit. The Ankeny-Artin-Chowla (AAC) conjecture (1952; restated by Kiselev-Slavutskii 1959 and Mordell 1960) says p does not divide y. It was verified to 2e11 by van der Poorten, te Riele and Williams (Math. Comp. 2001, corrigenda 2003), then to 1.5e12 (2023) and 5.325e13 (2024) by Andreas Reinhart. Reinhart (arXiv 2410.21864, v3 of 15 Dec 2025) then refuted it: p = 331914313984493 is prime and p | y. He found it by searching every p = 1 mod 4 in [1e14, 3.4e14], and stresses that [2e11, 3.4e14] was never checked independently, so he does not claim it is the smallest counterexample. Mordell's Pellian analogue for p = 3 mod 4 was also disproved by Reinhart (Acta Arith. 215, 2024). Under the usual heuristic that y mod p is random, counterexamples have density about 1/p, so a second one is rare but expected to exist. Still open: a second AAC prime, and an independent confirmation that 331914313984493 is the smallest.

## What counts as a win

CONFIRMED (full win) for a prime p = 1 mod 4, p != 331914313984493, that is absent from Reinhart's papers and any later literature at verification time, with this unconditional certificate: (i) a primality proof (ECPP or Pocklington, or PARI isprime as a second check); (ii) a unit eta of O_K, given in compact representation (a product of explicit elements alpha_i^e_i) or as explicit integers (as with Reinhart's u, v with u^2 - p^3 v^2 = -4 and eta = (u + v p sqrt p)/2), with N(eta) = +-1, integrality checked by valuations, and log|eta| != 0; (iii) the omega-coefficient of eta is 0 mod p, computed exactly in O_K/pO_K (handling valuations at the ramified prime), so eta lies in the order Z + pO_K; (iv) eta is not a p-th power in K, witnessed by a degree-1 prime ideal l with N(l) = 1 mod p and eta^((N(l)-1)/p) != 1 mod l, or by 1 < eta < eps^p as in Reinhart's Lemma 2.2 with an explicit bound. Since [O_K^x : (Z+pO_K)^x] divides p and the unit rank is 1, (ii)-(iv) force p | y for the fundamental unit (Reinhart, Lemma 2.2). A computation that only reports p | y without this certificate counts as PROMISING.

## Partial wins

- **p1:** An independent check, with a different algorithm or implementation and reproduced by the verifier, of every prime p = 1 mod 4 in a contiguous interval of length >= 1e12 inside [2e11, 3.4e14]. It reports no AAC counterexample, or exactly 331914313984493 if the interval contains it. Logs must allow random spot checks, and every spot-checked prime comes with a unit eta whose omega-coefficient is nonzero mod p.
- **p2:** The full independent double-check of [2e11, 3.4e14] under the same rules as p1, proving that 331914313984493 is the smallest AAC counterexample.

## How a win is checked

Recompute in PARI/GP (or Sage) from the certificate: prove p prime; rebuild eta from its compact representation and check its norm and integrality; reduce it in F_p[t]/(t^2) (p ramifies) to read off the omega-coefficient mod p; check the p-th-power-residue witness. As an independent check, recompute the fundamental unit with bnfinit(x^2-x-(p-1)/4,1) and bnfcertify, and confirm that its y-coordinate is 0 mod p. For p1 and p2, rerun random sub-intervals with independent code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2410.21864>

## Sources

- <https://arxiv.org/abs/2410.21864>
- <https://doi.org/10.1090/S0025-5718-00-01234-5>
- <https://arxiv.org/abs/2404.03038>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reinhart's large-step (baby-step giant-step on the infrastructure) algorithm decides p | y in roughly O(p^(1/4+e)) time without writing out the unit; an independent reimplementation (for example on GPUs) is the natural route to p1.
- Fermat-quotient and Bernoulli-number criteria (p | y iff p | B_((p-1)/2), Ankeny-Artin-Chowla, Mordell) give a second, independent test for each p.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The fundamental unit of a field near 3e14 has millions of digits. Work with compact representations or the infrastructure, never with expanded integers.
- For p = 1 mod 4, O_K = Z[(1+sqrt p)/2], not Z[sqrt p]. Using the wrong order flips the meaning of y.
- An unchecked GRH-conditional unit can be a power of the true fundamental unit. Witness (iv) is what excludes p-th powers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/aac-second-counterexample.md
```

Already set up? Say `run V3R1T4S on aac-second-counterexample`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `aac-second-counterexample`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
