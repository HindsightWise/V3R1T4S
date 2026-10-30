# Norm-Euclidean cyclotomic rings Z[zeta_m]: decide one of the open class-number-one cases (m = 17, 19, 25, 27, 28, 33, 35, 36, 40, 44, 45, 48, 60, 84)

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (box coverings in degree 12 to 24); the degree-9 and degree-10 real subfields in the partial wins are laptop-days · open as of 2026-10-30

## The problem

Z[zeta_m] (m != 2 mod 4) has class number 1 exactly for m = 1, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 24, 25, 27, 28, 32, 33, 35, 36, 40, 44, 45, 48, 60, 84 (Masley-Montgomery). Lemmermeyer's survey records these as norm-Euclidean: m = 1, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16, 20, 21, 24. This is the work of Gauss, Kummer, Eisenstein, Ojala, Lenstra (1975-78, including m = 11 and 24) and McKenzie (m = 13). Lenstra showed Q(zeta_32) is not norm-Euclidean. Kummer conjectured, in a letter to Kronecker, that m = 17 and 19 are Euclidean; the survey says this 'has not been verified so far'. Lezowski (Math. Comp. 83 (2014)) computed the exact Euclidean minimum of Q(zeta_n) for every n with phi(n) <= 8, but nothing higher. So m = 17, 19, 25, 27, 28, 33, 35, 36, 40, 44, 45, 48, 60, 84 remain undecided, with degrees 12 (m = 28, 36) up to 24. No later decision was found on 2026-10-30.

## What counts as a win

CONFIRMED (full win) for one m in {17, 19, 25, 27, 28, 33, 35, 36, 40, 44, 45, 48, 60, 84}, deciding whether Z[zeta_m] is norm-Euclidean. Either (i) a finite cover of the fundamental domain of R^phi(m)/Z[zeta_m] (power-basis coordinates) by rational boxes, each with an assigned gamma in Z[zeta_m] and an interval-arithmetic proof that |N(x - gamma)| < 1 on the whole box (or an equivalent certificate from Lezowski's 2014 algorithm proving M < 1); or (ii) an explicit xi in Q(zeta_m) with a finite certificate (Lenstra-style or Cerri-Lezowski critical-orbit certificate) proving |N(xi - gamma)| >= 1 for every gamma in Z[zeta_m]. The verifier rechecks the certificate with independent code. The case must still be undecided in the literature at verification time.

## Partial wins

- **p1:** A certificate as in (i) or (ii), for the ring of integers, deciding norm-Euclideanity of the maximal real subfield Q(zeta_m)^+ for one m in {19, 25, 27} (degrees 9, 10, 9), provided it is not decided in the literature or in Lezowski's table at verification time. Q(zeta_17)^+ (discriminant 17^7 = 410338673) is excluded: Lezowski's table (table_euc.db) lists it as norm-Euclidean, without an exact minimum.
- **p2:** The same for all three m in {19, 25, 27}.

## How a win is checked

Build the power basis; parse the cover and check exactly over Q that the boxes tile the unit cube modulo the lattice. Bound prod |sigma_i(x - gamma)| over each box with arb interval arithmetic. For (ii), verify the critical-orbit argument and every finite check with independent code; reject any argument that relies on floating point near |N| = 1.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.math.u-bordeaux.fr/~plezowsk/pdf/articles/algo.pdf>

## Sources

- <https://www.maths.dur.ac.uk/users/alexander.stasinski/Student%20projects/2024-2025/Lemmermeyer.pdf>
- <https://www.math.u-bordeaux.fr/~plezowsk/pdf/articles/algo.pdf>
- <https://arxiv.org/abs/1311.5163>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Lenstra's norm-Euclidean proofs pick a finite set of gamma that are differences of units ('exceptional sequences') and a Minkowski-type covering. Reuse that for m = 28 and 36.
- Adaptive box subdivision guided by the Galois action (the group (Z/m)^x permutes coordinates) cuts the covering size by phi(m).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Being Euclidean is weaker than being norm-Euclidean; only the norm counts here.
- The plain box cover grows exponentially with degree; for phi(m) >= 16 a naive cover is hopeless, and unit-based reductions are needed.
- Upper bounds of Bayer-Fluckiger-Maciak type that are >= 1 decide nothing.
- Lezowski's table (https://www.math.u-bordeaux.fr/~plezowsk/tables/table_euc.db; its HTML page served raw PHP on 2026-10-30) marks a field norm-Euclidean with euclidean < 0 even when the M1 column is empty; check it before claiming a real-subfield partial win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/cyclotomic-norm-euclidean-open-cases.md
```

Already set up? Say `run V3R1T4S on cyclotomic-norm-euclidean-open-cases`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cyclotomic-norm-euclidean-open-cases`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
