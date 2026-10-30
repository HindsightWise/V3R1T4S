# Five voters: a tournament on at most 21 alternatives that no five voters can induce by majority (13 <= N(5) <= 22, Chindelevitch-Harutyunyan Question 1)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days per candidate (symmetry-broken SAT/cube-and-conquer over five linear orders of 21 alternatives); certificates are LRAT proofs · open as of 2026-10-30

## The problem

A tournament is k-inducible if k voters with linear orders produce it by pairwise majority. N(k) is the least number of alternatives on which some tournament is not k-inducible. McGarvey, Stearns and Erdős-Moser fix the asymptotics. N(3) = 8 (Shepardson-Tovey 2009; Eggermont, Hurkens and Woeginger 2013). Bachmeier et al. (2019) left the 23-vertex Paley tournament P23 undecided. Chindelevitch and Harutyunyan (arXiv:2607.26690, v2 22 Oct 2026) proved 12 <= N(5) <= 38. Their 'Tournaments not inducible by five voters' (arXiv:2609.13924, v2 22 Oct 2026) narrows this to 13 <= N(5) <= 22. The upper bound comes from nine 22-vertex obstructions: eight one-vertex deletions of doubly regular 23-vertex tournaments, plus one arc reversal. The lower bound comes from a census showing every 12-vertex tournament is 5-inducible. Four negative results come with machine-checked proofs (code at github.com/Leonardini/TournamentsBeyond5Voters). Of 4,108 21-vertex classes obtained by deleting two vertices of a doubly regular 23-vertex tournament, 2,916 are still undecided (Appendix G). Section 4.2 asks Question 1 (is N(5) = 22, i.e. is every 21-vertex tournament 5-inducible?). It also lists Conjecture 2 (P_q is not 5-inducible for every prime q >= 23 with q = 3 mod 4; P23, P31 and P43 are settled), Open problem 1 (P31 or P43 minus two vertices), Open problem 2 (a tournament 5-inducible but not with margin <= 3) and Conjecture 3 (k-inducible implies (k+2)-inducible with unit margin).

## What counts as a win

An explicit tournament on n <= 21 vertices (adjacency matrix) with a certificate that it is NOT 5-inducible: an LRAT (or DRAT) refutation, checked by an independent checker, of a CNF that the verifier regenerates with their own encoder. The CNF encodes five linear orders (transitivity), with each arc u -> v carried by at least three of the five orders. This sets N(5) <= n < 22 (direction: lower is better) and answers Question 1 of arXiv:2609.13924 negatively. Cube-and-conquer is fine if the cube partition is itself checked to be exhaustive. A symmetry-breaking step must be justified (the paper's Theorem 2.1 style) and re-derived by the verifier.

## Partial wins

- **p1:** Open problem 2 of arXiv:2609.13924: a tournament that is 5-inducible, shown by five explicit orders, but not 5-inducible with margin <= 3 (every arc carried 3-2 or 4-1), certified by a checked refutation.
- **p2:** Open problem 1: decide whether P31 or P43 minus two vertices is 5-inducible, by an explicit witness or a checked refutation.
- **p3:** Conjecture 2 at a new prime: for a specific prime q with 47 <= q <= 103 and q = 3 mod 4, either a checked LRAT/DRAT refutation (of a CNF the verifier regenerates) showing P_q is not 5-inducible, or an explicit five-voter witness refuting the conjecture.
- **p4:** A counterexample to Conjecture 3 for some odd k: a tournament that is k-inducible (explicit witness) but not (k+2)-inducible with unit margin (checked refutation). For k = 3 it needs at least 13 vertices.

## How a win is checked

Positive claims (witnesses) take seconds: check that the orders are permutations, recompute every pairwise majority and margin, and compare with the tournament. Negative claims: regenerate the CNF independently, with order variables per voter and pair, transitivity clauses and a cardinality encoding of 'at least 3 of 5' per arc. Add only symmetry breaking the verifier can justify. Check the solver's LRAT with lrat-trim or cake_lpr. Negative controls: one of the paper's nine 22-vertex obstructions must give UNSAT with a checked proof; P19 must be SAT (5-inducible) but UNSAT at unit margin; random 12-vertex tournaments must be SAT.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.13924>

## Sources

- <https://arxiv.org/abs/2609.13924>
- <https://arxiv.org/abs/2607.26690>
- <https://github.com/Leonardini/TournamentsBeyond5Voters>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The authors searched only classes near doubly regular tournaments (their Appendix G). Low-predictability tournaments far from that family, such as quadratic-residue-like constructions on 21 vertices, circulants or products, are unexplored.
- Use the paper's necessary condition: tournaments whose maximum acyclic subgraph fraction is below 3/5 are not 5-inducible with no search. Look for 21-vertex tournaments just above that threshold.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Unit-margin obstructions at n = 19 and 21 are known and do not move N(5); the full win needs plain majority.
- Deleting vertices from the 22-vertex obstructions gives 5-inducible tournaments; the paper checked all of them.
- A solver timeout or an unchecked UNSAT is not a certificate.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/five-voter-tournaments-n5.md
```

Already set up? Say `run V3R1T4S on five-voter-tournaments-n5`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `five-voter-tournaments-n5`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
