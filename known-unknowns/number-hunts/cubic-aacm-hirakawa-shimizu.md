# Cubic Ankeny-Artin-Chowla-Mordell conjecture (Hirakawa-Shimizu): a prime p with p | beta for the fundamental unit of Q(p^(1/3)) or Q((2p)^(1/3)), or a certified verification for all p < 1e7 and beyond

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for a counterexample search beyond 1e7 (one unit computation per pure cubic field); the p1 certificate file (about 1.3 million fields) is laptop-days on 10 cores · open as of 2026-10-30

## The problem

Hirakawa and Shimizu (Proc. AMS 150 (2022) 1821-1835, arXiv 1912.04600, Conjecture 1.2): for a prime p != 3 and P in {p, 2p}, write the fundamental unit of Q(P^(1/3)) as epsilon = (alpha + beta*P^(1/3) + gamma*P^(2/3))/3 with alpha, beta, gamma integers. Then beta != 0 mod p. It is a cubic analogue of the AAC and Mordell conjectures, and it is what their construction of counterexamples to the local-global principle for plane curves of degree divisible by p needs. They verified it in Magma for both P = p and P = 2p and all p < 1e5. Reinhart (arXiv 2410.21864 v3, 15 Dec 2025, Section 4) says it is still open, although its real-quadratic ancestors have both been refuted. His Remark 4.1 lists every squarefree d <= 1e7 with d | b in Q(d^(1/3)): 17 values, none a prime p >= 5 and none of the form 2p. That settles P = p for all primes 5 <= p <= 1e7, from a PARI/GP computation that was not independently checked. For P = 2p it only rules out 2p | b, not p | b, so P = 2p is fully verified only for p < 1e5. A naive 1/p heuristic suggests a counterexample exists: roughly 0.25 expected with P = p for 1e7 < p < 1e9 and roughly 0.6 with P = 2p for 1e5 < p < 1e9.

## What counts as a win

CONFIRMED (full win) for a prime p >= 5 and P in {p, 2p}, not listed in the literature at verification time, with an unconditional certificate: a unit eta of O_L, L = Q(P^(1/3)), in compact representation, such that (i) N(eta) = +-1 and eta is integral (valuation check); (ii) log|eta| != 0; (iii) writing eta = (a + b*theta + c*theta^2)/3 with theta = P^(1/3), b = 0 mod p, computed in O_L/pO_L = O_L/q^3, where q is the prime above p, which ramifies totally (reducing modulo q alone keeps only a mod p and loses b; track the q-valuations of the factors of the compact representation); (iv) eta is not a p-th power in L, witnessed by a prime ideal l with N(l) = 1 mod p and eta^((N(l)-1)/p) != 1 mod l. The units with b = 0 mod p form a subgroup of index dividing p: it is the unit group of the order {b = 0 mod p}, and (O/pO)^x has order (p-1)p^2. The unit rank is 1, so (i)-(iv) prove that the fundamental unit has beta = 0 mod p.

## Partial wins

- **p1:** An unconditional certificate file that verifies the conjecture for every prime 5 <= p < 1e7 and both P = p and 2p: for each P, a unit eta_P in compact representation with N = +-1 and b != 0 mod p. Any such unit proves the conjecture for P (Hirakawa-Shimizu, footnote 1). Every unit is rechecked by the verifier's independent code.
- **p2:** The same unconditional certificate file for every prime 5 <= p < 1e8 (both P), if no larger verified range is in the literature at verification time.

## How a win is checked

Independent PARI/GP or Sage code: rebuild L = Q(P^(1/3)) and its maximal order, expand each compact representation modulo pO_L (that is, modulo q^3 for the totally ramified prime q above p; modulo q alone does not determine b) and modulo the witness prime l, check norms exactly from the factor norms, check integrality from valuations, and read off b mod p. Recompute the fundamental unit with bnfinit for a random sample as a cross-check.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2410.21864>

## Sources

- <https://arxiv.org/abs/1912.04600>
- <https://arxiv.org/abs/2410.21864>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Compute units with PARI bnfinit(x^3-P,1) using compact units (nf flag), then reduce the compact representation modulo pO_L = q^3 at the totally ramified prime q, keeping track of q-valuations of the factors. Never expand the unit.
- Use Voronoi's algorithm for units of cubic fields of negative discriminant as an independent unit source.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- For P = 2p use theta = (2p)^(1/3) and theta^2 = (4p^2)^(1/3). Mixing the normalisations of Hirakawa-Shimizu and Reinhart only matters by units mod p, but be consistent.
- Squarefree d with 3 | d (e.g. 6, 57, 1185) appear in Reinhart's list of d | b. They are not counterexamples, since the conjecture concerns P = p or 2p with p prime, p != 3.
- p = 2 and p = 3 are excluded or trivial; start at p = 5.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/cubic-aacm-hirakawa-shimizu.md
```

Already set up? Say `run V3R1T4S on cubic-aacm-hirakawa-shimizu`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cubic-aacm-hirakawa-shimizu`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
