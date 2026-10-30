# Cosmetic crossing conjecture: a certified non-nugatory crossing change that preserves the knot type (KnotInfo lists 1,216 knots up to 13 crossings as open)

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

A crossing change is cosmetic if the new diagram represents the same oriented knot, and nugatory if some 2-sphere meets the knot only at the two points of the crossing. Nugatory crossing changes are always cosmetic. The cosmetic crossing conjecture (Kirby problem list 1.58) says they are the only cosmetic ones. It is proven for 2-bridge knots (Torisu), fibered knots (Kalfagianni), genus-one knots with nontrivial Alexander polynomial (Ito, after Balm-Friedl-Kalfagianni-Powell), Whitehead doubles of prime non-cable knots (Balm-Kalfagianni) and special alternating knots (Boninger, after Lidman-Moore). For alternating (more generally Khovanov-thin) knots, Lidman-Moore (a condition on the homology of the branched double cover) and Boninger (an Alexander polynomial condition) give obstructions that together settle alternating knots with square-free determinant; Ito gives a further obstruction via the Casson-Walker invariant. KnotInfo (Livingston and Moore) marks a knot U when the conjecture is open for it, and cites Lidman-Moore for 10_128 and Ito for 10_67. In database_knotinfo 2026.10.5, 1,216 prime knots are U: 4 at 10 crossings (10_87, 10_98, 10_129, 10_147), 38 at 11, 172 at 12 and 1,002 at 13.

## What counts as a win

A PD code D of a knot K and a crossing x of D with two properties, both certified by the skeptic's own computation. (1) The diagram D' obtained by changing x represents the same oriented knot as D. For hyperbolic K this means SnapPy verified hyperbolic structures plus an orientation-preserving isometry of the exteriors that preserves the meridian and longitude; for any K, Regina knot recognition with orientation and mirror handled. (2) x is not nugatory: the link K union C, where C is the crossing circle around x, is non-split, certified for example by SnapPy verify_hyperbolicity on its exterior, or by a Regina proof that the exterior is irreducible. A crossing circle that bounds a disk disjoint from K would make K union C split.

## Partial wins

- **p1:** For one of the four 10-crossing U knots (10_87, 10_98, 10_129, 10_147), or any U knot, a reproducible computation showing that it satisfies the hypotheses of a published theorem ruling out cosmetic crossings (name the theorem, e.g. a Lidman-Moore, Boninger or Ito criterion). It counts only if KnotInfo has not applied that theorem, and every invariant must be recomputed from a verified diagram.

## How a win is checked

Skeptic rebuilds D and D', certifies the knot-type equality with SnapPy (verified isometry with peripheral data and orientation) and Regina, builds the crossing-circle link K union C, and certifies non-splitness by verified hyperbolicity or irreducibility. Under an hour.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://knotinfo.org/descriptions/cosmetic_crossing.html>

## Sources

- <https://knotinfo.org/descriptions/cosmetic_crossing.html>
- <https://arxiv.org/abs/1507.00699>
- <https://arxiv.org/abs/2407.12763>
- <https://arxiv.org/abs/2103.15277>
- <https://arxiv.org/abs/math/0610440>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Conventional: for each U knot and many diagrams, change each crossing and compare hyperbolic invariants (volume, Chern-Simons, cusp shape) before attempting a verified isometry.
- Conventional: search the crossing-circle exteriors K union C directly. A cosmetic crossing gives a pair of fillings of the same 2-cusped manifold yielding isotopic knots, a SnapPy-searchable condition.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Orientation matters. K and its reverse or mirror can have isometric exteriors, so an isometry that reverses orientation or the meridian is not a cosmetic crossing.
- Many diagram crossings are visibly nugatory. Certify non-splitness of K union C, not just the absence of an obvious sphere.
- Expect the conjecture to hold. Record negative searches honestly, and never claim from matching invariants alone.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/cosmetic-crossing-conjecture-counterexample.md
```

Already set up? Say `run V3R1T4S on cosmetic-crossing-conjecture-counterexample`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cosmetic-crossing-conjecture-counterexample`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
