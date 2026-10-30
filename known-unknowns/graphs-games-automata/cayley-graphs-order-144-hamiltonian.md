# Lovász conjecture, smallest open order: is every connected Cayley graph on a group of order 144 Hamiltonian?

🕸️ **Graphs, games and automata** · standard · tractability ★★★☆☆ · compute: laptop-days (GAP enumeration of irredundant generating sets up to automorphism for the 197 groups of order 144, plus LKH or a SAT search per graph) · open as of 2026-10-30

## The problem

A special case of the Lovász conjecture asks whether every connected Cayley graph on a finite group (order > 2) has a Hamiltonian cycle. Morris and Wilk ('Cayley graphs of order kp are hamiltonian for k < 48', Art Discrete Appl. Math. 3 (2020), arXiv 1805.00149) proved it, with computer help, for all orders kp with k < 48. Their Corollary 1.2 deduces that every connected Cayley graph on a group of order < 144 is Hamiltonian. Earlier work covers prime-power orders (Witte 1986), kpq (k < 6), pqr, kp^2 (k < 5) and kp^3 (k < 3) (Kutnar, Marušič, Morris, Morris and Šparl 2012), 16p, 27p and 30p. Later work adds 8pq (Abedi, Morris, Rezaee and Salarian 2025) and pqrs (Lehner, Maghsoudi and Miraftab, arXiv 2607.14440, 2026). No result we found covers order 144 = 2^4 3^2. By our reading, the next orders up to 300 outside all published families are 162, 192, 216, 240, 270, 288 and 300. A Hamiltonian-path version of the question for symmetric generating sets is Kourovka Notebook 20.32 (posed by E. Rapaport Strasser, submitted by B. Green; 21st ed., arXiv 1401.0300v49).

## What counts as a win

Success means a complete certificate for order 144: for each of the 197 groups SmallGroup(144,i), a list of irredundant generating sets that represents every irredundant generating set up to automorphisms of the group and inversion of generators, and for each listed set either a Hamiltonian cycle in the undirected Cayley graph, given as a sequence of generators, or a proof of non-Hamiltonicity. A non-Hamiltonian example would be a counterexample, which also counts if machine-checked by exhaustive search. Supersets of generating sets need no separate check.

## Partial wins

- **p1:** The same complete certificate restricted to irredundant generating sets of size 2, for all 197 groups of order 144.
- **p2:** The same complete certificate for all irredundant generating sets of size at most 3, for all 197 groups of order 144.

## How a win is checked

For each cycle, multiply the generator sequence in the group (GAP or a permutation representation): the 144 partial products must be distinct and the full product must be the identity. Completeness: an independent GAP run recomputes the irredundant generating sets up to Aut(G) and inversion (as IrredUndirGenSetsUpToAut does in Morris-Wilk's ancillary code) and checks that each is covered.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://deductivepress.ca/dmorris/graphtheory>

## Sources

- <https://arxiv.org/abs/1805.00149>
- <https://arxiv.org/abs/1009.5795>
- <https://deductivepress.ca/dmorris/graphtheory>
- <https://arxiv.org/abs/2607.14440>
- <https://arxiv.org/abs/1401.0300>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reuse Morris-Wilk's GAP ancillary code (HamiltonianCycles.gap, LKH.gap, IsHamiltonianCycle.gap) as a reference; write your own checker.
- Many groups of order 144 fall under structural theorems (abelian, cyclic commutator subgroup of prime-power order, commutator subgroup of order 2p, and so on); a direct computer search over all of them is still the cleanest certificate.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Equivalence must use automorphisms of G plus inversion of individual generators; cutting the list down with a coarser equivalence leaves gaps.
- A Hamiltonian path is not enough; the cycle must close.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/cayley-graphs-order-144-hamiltonian.md
```

Already set up? Say `run V3R1T4S on cayley-graphs-order-144-hamiltonian`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `cayley-graphs-order-144-hamiltonian`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
