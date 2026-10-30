# MOONSHOT - Perfect matchings of the 8-cube: the exact count A005271(8)

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (exact count far beyond direct methods; the modular partial is laptop-days) · open as of 2026-10-30

## The problem

This counts perfect matchings of the n-cube Q_n, a problem in Propp's 'Enumeration of matchings: problems and progress' (Problem 19) and his 'Twenty open problems in enumeration of matchings'. The counts are 1, 2, 9, 272, 589185, 16332454526976 for n = 1..6. D. H. Wiedemann first found n = 6 (unpublished), and Per Hakan Lundow published it (1996). For n = 7 the count is 391,689,748,492,473,664,721,077,609,089 (Patric Ostergard and Ville Pettersson, 'Enumerating Perfect Matchings in n-Cubes', Order 30 (2013), using classification under the cube's symmetry group). Q8 has 256 vertices and its count is unknown. OEIS checked live 2026-10-30: A005271 ends at n = 7, with keyword 'more' and no pending draft.

## What counts as a win

Success means the exact integer A005271(8), the number of perfect matchings of Q8, computed by two independent methods (different algorithm or decomposition, and different moduli or exact arithmetic) that agree exactly. The code must reproduce A005271(1..7), including Ostergard-Pettersson's n = 7 value. The live OEIS entry must still lack it.

## Partial wins

- **p1:** The exact number of perfect matchings of the folded 8-cube (Q7 plus its antipodal matching; 128 vertices, 8-regular, bipartite). This equals the number of perfect matchings of Q8 invariant under the antipodal map. It must come from two independent methods that agree. The code must also reproduce the analogous counts for folded 4-, 5- and 6-cubes computed by brute force, plus A005271(1..7) in plain-cube mode. Literature check: the value must not already be published.
- **p2:** A005271(8) modulo a prime p >= 3 obtained by any method other than computing the full count (for example by counting matchings fixed by a Sylow p-subgroup of Aut(Q8), for p in {3, 5, 7}). A second independent implementation must agree, and the method must reproduce A005271(7) mod p.

## How a win is checked

Skeptic: run the claimant's modular permanent code on Q6 and Q7 and compare with the known counts reduced mod 2^k or p; for the full count, check that the residues mod several fresh primes or 2^k computed independently match.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A005271>

## Sources

- <https://oeis.org/A005271>
- <https://arxiv.org/abs/math/9801061>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Perfect matchings of Q8 equal the permanent of the bipartite 128 x 128 biadjacency matrix, not its determinant. Q8 is not planar, so Kasteleyn's method does not apply.
- Burnside on a p-subgroup P gives A005271(8) = (number of P-fixed matchings) mod p. For a residue claim, state the subgroup used and report the fixed-point count itself. A residue already given in the literature does not count.
- A005271(n) has the parity of n (Lovasz, in Propp's progress report), and residues modulo powers of 2 follow from fixed points of the coordinate reflections. That is why p2 asks for p >= 3; a power-of-2 residue is not a partial win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/hypercube-q8-perfect-matchings.md
```

Already set up? Say `run V3R1T4S on hypercube-q8-perfect-matchings`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypercube-q8-perfect-matchings`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
