# Quantum chromatic number vs rank-1 quantum chromatic number: a graph on at most 20 vertices with chi_q(G) < chi_q^(1)(G) (smallest known: Lalonde's 21-vertex G21)

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (graph search, exact quantum colourings, and a rigorous orthogonal-rank lower bound) · open as of 2026-10-30

## The problem

In the quantum colouring game a graph G has quantum chromatic number chi_q(G) <= c if there are projectors P_{v,1..c} on C^D for each vertex with sum_i P_{v,i} = I and P_{u,i} P_{v,i} = 0 for every edge uv and colour i. chi_q^(r) restricts to rank-r projectors, and chi_q = min_r chi_q^(r). The orthogonal rank xi(G) is the least dimension of an orthogonal representation. It satisfies xi(G) <= chi_q^(1)(G) <= chi(G), and the two can differ (Scarpa and Severini; Mancinska and Roberson's 13-vertex G13 has xi = 3 and chi_q^(1) = 4). Olivier Lalonde (Electron. J. Combin. 32(1) P1.18, 2025; arXiv:2311.08194) proved the Mancinska-Roberson conjecture that their 14-vertex G14 is the smallest graph with chi_q < chi. He also constructed G21 (21 vertices, 72 edges, graph6 given in the paper) with chi_q = chi_q^(2) = 4 and xi = chi_q^(1) = chi = 5. G21 is the smallest known separation between chi_q and chi_q^(1). The previous one was the 57-vertex magic-square graph Gmsg from Mancinska and Roberson's 2016 paper, with chi_q = 3 and chi_q^(1) = xi = 4. G21 is also the first separation between chi_q^(1) and chi_q^(2). His lower bound xi(G21) > 4 needed a new algorithm, since no general practical method certifies orthogonal rank. In the paper's open problems he suggests looking for graphs on 20 vertices or fewer that separate chi_q and chi_q^(1), or for the smallest such graph. He also notes that no proof is known that all chi_q^(r) are distinct parameters. Lalonde's 'Quantum colorings of spheres' (arXiv:2606.10872, June 2026) gives a 19-vertex G19 with xi = 3 < chi_q = 4, which is the opposite direction and not a chi_q vs chi_q^(1) separation. The abstracts of the 2025-2026 citing papers seen in this check report no smaller separation.

## What counts as a win

Success means a graph G with at most 20 vertices (STRICTLY FEWER, direction: min, than the 21 of G21 in arXiv:2311.08194; re-check arXiv for newer separations before claiming), together with (i) and (ii). (i) An explicit quantum c-colouring: projectors P_{v,i} in C^D with entries in an explicit number field (e.g. cyclotomic), verified exactly to satisfy P^2 = P = P^dagger, sum_i P_{v,i} = I and P_{u,i}P_{v,i} = 0 on every edge. (ii) A rigorous, independently re-checkable proof that G has no rank-1 quantum c-colouring (chi_q^(1)(G) > c). Proving that G has no orthogonal representation in C^c (xi(G) > c) suffices, since xi <= chi_q^(1). The proof may be an exact algebraic certificate (e.g. a Groebner basis or Nullstellensatz certificate over Q(i) re-verified by independent software), a run of Lalonde's algorithm re-implemented independently that agrees, or a machine-checked proof.

## Partial wins

- **p1:** A graph of any size with chi_q^(3)(G) < chi_q^(2)(G), with the colouring verified exactly and the lower bound on chi_q^(2) proven by a re-checkable certificate: the first separation between the rank-2 and rank-3 quantum chromatic numbers.
- **p2:** A graph on at most 100 vertices with chi_q^(1)(G) - chi_q(G) >= 2, with no such graph of at most 100 vertices published before (literature check), certified as in the main criterion.

## How a win is checked

Parse G (graph6). Recompute the vertex and edge counts and the classical chromatic number by SAT. Check every projector identity exactly with sympy or flint over the stated field. Re-verify the lower-bound certificate (on xi or directly on chi_q^(1)) with independent software, e.g. Singular or Macaulay2 for a Groebner or Nullstellensatz certificate, or re-run an independent implementation of the stated algorithm. Confirm that the certificate excludes c-dimensional orthogonal representations, or rank-1 quantum c-colourings, and not a weaker real-only or SDP relaxation. Confirm no graph with fewer vertices is already published.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2311.08194>

## Sources

- <https://arxiv.org/abs/2311.08194>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i1p18>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- chi_q < chi is not the target: that separation is settled at 14 vertices (G14). Here the gap must be between chi_q and chi_q^(1).
- xi and chi_q^(1) are different parameters (xi <= chi_q^(1)). A graph with xi < chi_q, such as Lalonde's 19-vertex G19 (arXiv:2606.10872: xi = 3, chi_q = 4), goes the wrong way and does not count.
- Numerical failure to find a c-dimensional orthogonal representation is evidence, not proof; the criterion needs a certificate. A real-only search or an SDP bound (xi_SDP) below c+1 proves nothing about complex representations.
- Floating-point projectors with residual 1e-12 are not a quantum colouring until made exact.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/quantum-chromatic-orthogonal-rank-separation-under-21.md
```

Already set up? Say `run V3R1T4S on quantum-chromatic-orthogonal-rank-separation-under-21`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quantum-chromatic-orthogonal-rank-separation-under-21`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
