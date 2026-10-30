# Arcs in projective Hjelmslev planes over chain rings of order 16 and 25: raise a lower bound in the Honold-Kiermaier-Landjev tables

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours (orbit ILP or local search; verification is instant) · open as of 2026-10-30

## The problem

Let R be a finite chain ring of length 2 with |R| = q^2. The projective Hjelmslev plane PHG(2,R) has as points the free rank-1 submodules of R^3 and as lines the free rank-2 submodules. A projective (k,n)-arc is a set of k points with at most n on any line, and m_n(R) is the largest such k. Honold, Kiermaier and Landjev, 'New Results on Arcs in Projective Hjelmslev Planes over Small Chain Rings' (arXiv:2409.02099, Sept 2024), give updated bounds for all |R| <= 25. These improve Kiermaier-Kohnert, Boumova-Landjev, Koch-Kurz and others, and the tables also appear in Kiermaier's online tables. The rings of order 4 and 9 are settled. Many cells are open for the rings of order 16 (G4 = Z4[X]/(X^2+X+1), S4 = F4[X]/(X^2), T4 = F4[X;a->a^2]/(X^2)) and of order 25 (Z25, S5 = F5[X]/(X^2)). Examples: G4: m_3 29-30, m_7 94-101, m_10 152-160, m_14 224-228, m_15 236-248; S4 and T4: m_6 81-83, m_8 120-125; Z25: m_2 21-25, m_3 40-43, m_5 85-102, m_13 310-311; S5: m_7 152-156. The authors' open problem (3) asks for (q-1)^2(q^2+q+1)-point arcs with n = q^2-q. For q = 4 and 5 these are the upper bounds 189 and 496.

## What counts as a win

Name the ring R (one of G4, S4, T4, Z25, S5, with explicit multiplication) and give k distinct points of PHG(2,R). Each point is a vector of R^3 with at least one unit coordinate, taken up to right multiplication by units, and each is given in a canonical form. Every line must contain at most n of the points. Lines are the sets {x : a.x = 0} for row vectors a with a unit coordinate, taken up to left multiplication by units. The check runs over all q^2(q^2+q+1) lines. k must be STRICTLY GREATER (direction: max) than the live lower bound for m_n(R) in arXiv:2409.02099 (Tables 5-6), or than any later published value found by a fresh search, and must not exceed the published upper bound.

## Partial wins

- **p1:** Lower a published upper bound for one open cell with a nonexistence proof the skeptic reruns (exhaustive search or exact ILP infeasibility with a checkable certificate).

## How a win is checked

Implement the ring and self-check it: associativity, the chain ideal structure, and the unit count q^2-q. Enumerate the points and confirm there are q^2(q^2+q+1) of them. Enumerate the lines and confirm each has q(q+1) points. Confirm the input points are distinct after canonicalisation, count the arc points on every line, and compare the maximum with n.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2409.02099>

## Sources

- <https://arxiv.org/abs/2409.02099>
- <http://www.algorithm.uni-bayreuth.de/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The structure theorems in the paper relate PHG(2,R) arcs to arcs in PG(2,q) and AG(2,q) through neighbour classes. Search over multiplicity distributions per neighbour class first, then lift.
- Use a Kramer-Mesner style orbit ILP with subgroups of the collineation group of PHG(2,R).
- For the n = q^2 - q problem, each point class must carry (q-1)^2 points and the missing points form a blocking set in AG(2,q): build from known blocking sets.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- T4 is a skew ring: left and right modules differ, so fix the convention stated in the criterion.
- Kiermaier's online tables (algorithm.uni-bayreuth.de) did not respond on 2026-10-30, so the arXiv tables are the bar. Recheck both, and search the 2024-2026 literature, before claiming.
- Z4[X]/(X^2+X+1) (Galois ring GR(16,4)) is not Z16.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/hjelmslev-plane-arcs-chain-rings-16-25.md
```

Already set up? Say `run V3R1T4S on hjelmslev-plane-arcs-chain-rings-16-25`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hjelmslev-plane-arcs-chain-rings-16-25`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
