# Greenberg's conjecture for p = 3: extend the Mercuri-Paoluzi-Schoof verification for real quadratic fields beyond discriminant 100,000

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-days (MPS needed about two weeks on one i5 workstation for f < 100,000) · open as of 2026-10-30

## The problem

Greenberg's conjecture (1976) says the Iwasawa invariants lambda and mu vanish for every totally real field F and prime p: the p-class groups A_n of the layers of the cyclotomic Z_p-extension stay bounded. Pietro Mercuri, Maurizio Paoluzi and Rene Schoof (arXiv 2503.00819, March 2025) proved it for p = 3 and all 30,394 real quadratic fields of discriminant f < 100,000. For each f they computed a cyclic Lambda-module C(f) = Lambda/J built from cyclotomic units, which is finite iff Greenberg's conjecture holds for F, and showed it is finite. C(f) is nonzero for 3,359 fields (2,118 of them with J = (3, T)). Their method finds elements of J (upper bounds) from cyclotomic units modulo auxiliary primes r, and lower bounds with G. and M.-N. Gras' high-precision method, until J + (omega_n) = J + (omega_(n+1)). Where the lower bound is infeasible for n >= 3, their Lemma 2.1 with m = 2 closes the case. The ideals J and their Magma code are on GitHub (mercuri-pietro/Iwasawa-modules). Earlier computations cited by MPS: Fukuda-Komatsu (1986), Kraft-Schoof (1995), Taya (1996), Ichimura-Sumida (1996-97). Beyond f = 100,000 no complete verification for p = 3 has been published; individual fields there are covered only by classical criteria (for example Iwasawa's theorem when 3 does not split in F and 3 does not divide h(F)).

## What counts as a win

CONFIRMED (full win): for every real quadratic field of fundamental discriminant 100,000 <= f < 200,000, a proof (in the MPS framework or an equivalent published criterion) that C(f), equivalently the 3-part of the class groups in the cyclotomic Z_3-tower, is finite. That means the ideal J or an equivalent invariant, with stabilisation J + (omega_n) = J + (omega_(n+1)), backed by both the upper-bound and the lower-bound computation, or by Lemma 2.1 of MPS (or by the upper bound alone when it already gives J + (omega_0) = Lambda). Output one file per residue class of f mod 3 in the PARI/GP list format of the MPS GitHub data, plus the code. The verifier reruns an independent implementation on every claimed f with J != Lambda and on a random sample of at least 300 further discriminants, and requires exact agreement. The range must not already be covered by a published or arXiv computation at verification time.

## Partial wins

- **p1:** The same certified computation for every fundamental discriminant 100,000 <= f < 110,000.
- **p2:** The same for every fundamental discriminant 100,000 <= f < 150,000.

## How a win is checked

Regression first: the verifier's implementation (PARI/GP or Sage, independent of the MPS Magma code where possible) must reproduce the MPS ideals for 200 random f < 100,000. Then rerun the sample of claimed f >= 100,000, checking the elements of J found modulo the auxiliary primes r, the Gras lower bounds at the stated precision, and the Nakayama stabilisation step.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2503.00819>

## Sources

- <https://arxiv.org/abs/2503.00819>
- <https://github.com/mercuri-pietro/Iwasawa-modules>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- About 89% of fields have C(f) = 0, which is settled at layer 0 or 1 with cheap modular computations. Spend the high-precision lower-bound budget only on the rest.
- Treat the three cases f = 0, 1, 2 mod 3 separately, as MPS do (Sections 2 and 4); the f = 1 mod 3 case uses the modified module B~_n.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Upper bounds alone (elements found in J) prove finiteness only when they already give J + (omega_0) = Lambda, i.e. C(f) = 0; otherwise the Gras lower bound or Lemma 2.1 of MPS is required.
- Use fundamental discriminants f, not squarefree d; MPS count 30,394 fields below 100,000.
- For f = 1 mod 3 the module is built from the modified group B~_n (MPS Section 4); do not reuse the f != 1 mod 3 recipe there.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/greenberg-p3-real-quadratic-beyond-1e5.md
```

Already set up? Say `run V3R1T4S on greenberg-p3-real-quadratic-beyond-1e5`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `greenberg-p3-real-quadratic-beyond-1e5`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
