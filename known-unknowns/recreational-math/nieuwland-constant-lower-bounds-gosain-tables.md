# Nieuwland constants of the Platonic, Archimedean, Catalan and Johnson solids: a Rupert passage with a larger scale than Gosain-Grimmer's tables

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours per solid (nonsmooth local optimisation; 16 h per Johnson solid is all that stands behind most cells) · open as of 2026-10-30

## The problem

The Nieuwland constant mu(P) of a Rupert polyhedron P is the supremum of scales s for which sP passes through a hole in P, that is, s*pi(R1 P) + t lies inside the interior of pi(R2 P) for some rotations and translation. It is known exactly only for the cube: 3*sqrt(2)/4 (Nieuwland; proof by Bezdek, Guan, Hujter and Joos). Gosain and Grimmer (arXiv 2509.08190, Sept 2025) ran a customised high-accuracy subgradient method: 48 h per Platonic, Archimedean and Catalan solid, 16 h per Johnson solid. Tables 1-4 give their 12-digit lower bounds (computed at 50 digits, rounded down), and Tables 1-3 print the previous best values beside them. Passages are at github.com/RajGosain13/RupertResults, but that repository's Results CSVs (last commit 28 Jul 2025, before the preprint) do not all match the tables: for example, truncated cube 1.028166 (table 1.030661650181), truncated octahedron 1.014467 (table 1.014566571546), rhombic dodecahedron 1.027215 (table 1.027180977829). They improved more than half of the solids, but for five the previous best printed in their tables is still higher: truncated octahedron 1.014602, rhombicuboctahedron 1.012819, truncated cuboctahedron 1.006563, truncated icosidodecahedron 1.002048 and rhombic dodecahedron 1.027201 (their values 1.014566571546, 1.012785597490, 1.006561784960, 1.002046507167, 1.027180977829). Other examples: octahedron 1.06066017177981 (conjectured 3*sqrt(2)/4); icosahedron 1.01082306075264 and dodecahedron 1.01082306075208 (conjectured, after Steininger and Yurkevich, to be the smallest positive root of 2025x^8 - 11970x^6 + 17009x^4 - 9000x^2 + 2000); disdyakis triacontahedron 1.000743186023; triakis tetrahedron 1.000004055715; J25 1.000082039977; J45 1.000020986354; J71 1.000882983008. For most Johnson solids no value was published before 2025. Only the cube's constant is proven.

## What counts as a win

For a solid P listed with a value in Tables 1-4 of Gosain and Grimmer (arXiv 2509.08190) other than the cube, an explicit passage of scale mu. Give rational rotations (rational quaternions) or exactly specified algebraic ones, a rational translation t and a rational scale mu. Exact or rigorous interval arithmetic must show that every vertex of mu*pi(R1 P) + t lies strictly inside the convex hull of pi(R2 P), with P built from its standard exact coordinates. mu must be STRICTLY GREATER (direction: max) than the largest of (i) Gosain-Grimmer's own value for that solid printed in Tables 1-4, (ii) the scale of their stored passage for that solid in their repository's Results CSV, recomputed at 50 digits, (iii) the previous-best value printed for that solid in their tables, and (iv) any value published later for that solid (literature check at claim time). The printed table values are rounded down to 12 digits, so mu must exceed value (i) by more than 1e-12.

## Partial wins

- **p1:** For a solid in Tables 2-4 (Archimedean, Catalan or Johnson) whose best-known value has no published exact closed form (literature check at claim time), an exact closed-form passage (algebraic coordinates, verified in exact arithmetic) whose scale is at least the solid's best-known value as defined in the success criterion. Gosain and Grimmer did this for the tetrahedron; the Platonic solids are excluded.
- **p2:** A rigorous upper bound mu(P) <= U for some Platonic or Archimedean solid other than the cube, certified by an exact or interval-arithmetic covering of the configuration space and re-run by an independent checker, with U strictly smaller than every previously published upper bound for that solid (literature check required) and U < L + 0.01, where L is that solid's best-known lower bound as defined in the success criterion.

## How a win is checked

Load the passage, rebuild P exactly, apply the rotations and scale in rational or interval arithmetic, and check strict containment of every scaled inner vertex in the outer hull (seconds per solid). Recompute Gosain-Grimmer's stored passage for the same solid from their repository's Results CSV at 50 digits with mpmath, and compare the claimed scale with it, with their printed table value and with the printed previous best. For p2, re-run the covering certificate with an independent checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2509.08190>

## Sources

- <https://arxiv.org/abs/2509.08190>
- <https://github.com/RajGosain13/RupertResults>
- <https://arxiv.org/abs/2210.00601>
- <https://arxiv.org/abs/2112.13754>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Johnson solids got 16 h each against 48-180 h elsewhere. Systematic multi-start runs with different initial distributions are the cheapest wins.
- Gosain-Grimmer say local optimisation is likely exhausted near their optima. Global moves (different combinatorial types of passage: which vertices touch which hull edges) are needed to find a better basin.
- Exploit symmetry: restrict to passages respecting a subgroup of the solid's symmetry to cut dimension, then polish without the restriction.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The cube is proven optimal. Do not claim a cube improvement.
- The repository CSVs predate the preprint, and some stored passages are weaker than the printed tables (truncated cube 1.028166 against 1.030661650181). Beat the largest of all the values in the success criterion, not the stored passage alone, and clear the 12 printed digits by more than 1e-12.
- Use the same normalisation and coordinates as the table (a scaled or slightly perturbed solid is a different polyhedron).
- The nine solids still open for Rupertness belong to the separate entry rupert-open-classical-solids, not here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/nieuwland-constant-lower-bounds-gosain-tables.md
```

Already set up? Say `run V3R1T4S on nieuwland-constant-lower-bounds-gosain-tables`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `nieuwland-constant-lower-bounds-gosain-tables`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
