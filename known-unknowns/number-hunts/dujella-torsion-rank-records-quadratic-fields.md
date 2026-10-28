# High-rank elliptic curves with prescribed torsion over quadratic fields: beat or certify a cell

🔢 **Number hunts** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Over quadratic fields K = Q(sqrt d) there are 26 possible torsion groups (Kenku-Momose, Kamienny). Dujella's table lists, for each T, the best known lower bound B(T) for the rank of a curve over some quadratic field with torsion T, the squarefree d of the field Q(sqrt d) for the record, and in brackets bounds that are only conditional on the parity conjecture (on 2026-10-28 only T = 0, 34 (35), and Z/2xZ/10, 4 (5), have bracketed values). Small cells on 2026-10-28 include Z/11 (3, d = 12601), Z/13 (2, d = 193), Z/14 (3, d = 430), Z/15 (2, d = 190), Z/16 (4, d = -183443183), Z/18 (2, d = 9049), Z/2xZ/10 (4, conditional 5), Z/2xZ/12 (5, d = -295935), Z/3xZ/3 (9, d = -3), Z/3xZ/6 (6, d = -3), Z/4xZ/4 (8, d = -1). Most recent entries are by M. Voznyy (personal communications 2021-2026); S. Li raised Z/2xZ/2 to 22 in October 2026.

## What counts as a win

CONFIRMED (full win) for a quadratic field K = Q(sqrt d) (d squarefree), an elliptic curve E over K with torsion subgroup over K computed exactly as T, and r explicit K-points with positive height-regulator (two precisions, margin as for the Q table), where r is STRICTLY GREATER (direction: max) than the unconditional value B(T) on https://web.math.pmf.unizg.hr/~duje/tors/torsquad.html, re-fetched live immediately before the claim. Bracketed (parity-conditional) values are not the bar; the unconditional value is.

## Partial wins

- **p1:** Unconditional upgrade: for a cell whose table entry has a bracketed conditional value, exhibit that many independent K-points explicitly (e.g. Z/2xZ/10 at rank 5), making the conditional value unconditional.
- **p2:** Smaller field: a curve with torsion T reaching the live record rank B(T) over a quadratic field with |d| STRICTLY SMALLER than the d listed for T at verification time.

## How a win is checked

PARI/GP: K=nfinit(y^2-d); E=ellinit(a,K); elltors(E) over K; check each point on E; ellheightmatrix(E,P) over K at two precisions; matdet > 0 with margin. Check d squarefree and compare against the listed d. If E is defined over Q, cross-check with rank E(K) = rank E(Q) + rank E^d(Q) using independent points on E and on the twist.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://web.math.pmf.unizg.hr/~duje/tors/torsquad.html>

## Sources

- <https://web.math.pmf.unizg.hr/~duje/tors/torsquad.html>
- <https://web.math.pmf.unizg.hr/~duje/tors/tors.html>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Quadratic points on modular curves X1(N) (hyperelliptic or bielliptic for the relevant N) give explicit families of curves with torsion Z/N over quadratic fields; sieve over small-height points of these parametrizations.
- Base-change trick: for torsion groups realisable by curves defined over Q, rank E(Q(sqrt d)) = rank E(Q) + rank E^d(Q); search for a high-rank Q-curve and a twist d that also has many points.
- Treat d as an arm of a multi-armed bandit (imported from reinforcement learning): allocate 2-descent effort across candidate fields by the upper confidence bound of Nagao-type sums computed over split primes of K.
- Metropolis random walk over family parameters (imported from statistical physics) with energy = minus the Nagao sum, cooling slowly; good for the small Z/13, Z/15, Z/18 families where exhaustive grids are sparse.
- For p1, search for missing points by height-bounded enumeration plus LLL on the Mordell-Weil lattice of the known points (the lattice-reduction idea from cryptanalysis), since the conditional rank already tells you a further point exists.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Torsion over K larger than T, or points defined only over a bigger field (check every coordinate lies in K).
- Parity-conjecture or analytic-rank arguments do not count; explicit points only.
- d not squarefree, or d and d*k^2 treated as different fields.
- Confusing rank over Q with rank over K, or quoting a Q-record as a quadratic-field record.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/dujella-torsion-rank-records-quadratic-fields.md
```

Already set up? Say `run V3R1T4S on dujella-torsion-rank-records-quadratic-fields`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `dujella-torsion-rank-records-quadratic-fields`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
