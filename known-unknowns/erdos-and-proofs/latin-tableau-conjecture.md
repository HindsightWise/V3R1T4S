# Latin Tableau Conjecture (Chow et al.): a Young diagram with no Latin tableau of type delta, or a certified extension of the 12 x 12 verification

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (13 x 13 box: about 10.4 million partitions, roughly half up to conjugation; each needs a max-flow and a small SAT/ILP colouring) · open as of 2026-10-30

## The problem

A Latin tableau of shape lambda is a colouring of the boxes of the Young diagram of lambda with no colour repeated in any row or column. Its type mu lists the colour multiplicities in decreasing order. Let alpha_k be the maximum number of boxes that can be coloured with k colours under this rule, and let delta_k = alpha_k - alpha_{k-1} (the chromatic difference sequence). If a tableau of type mu exists, delta must dominate mu. The Latin Tableau Conjecture, posed by T. Y. Chow et al. in their work on the wide partition conjecture (a generalisation of Rota's basis conjecture), says this necessary condition is also sufficient. A positive answer implies the wide partition conjecture for free matroids. T. Y. Chow and M. G. Tiefenbruck (Electronic J. Combin. 32(2) (2025) P2.48, published 2025-06-20) reduce the conjecture to the existence of a Latin tableau of shape lambda and type exactly delta. Equivalently, the rook-type graph on the boxes of lambda is CDS-colourable; this is the form in the formal-conjectures file Paper/LatinTableau.lean, tagged research open as of 2026-10-30. They prove that a tableau can always match the first four parts of delta, and they report a computer check of every partition lambda that fits inside a 12 x 12 square. They have computed characterisations up to r = 7 terms without publishing proofs. A single partition lambda admitting no Latin tableau of type delta(lambda) would disprove the conjecture.

## What counts as a win

Success means a partition lambda together with: (i) its sequence delta(lambda), computed exactly by two independent programs; (ii) a proof that no Latin tableau of shape lambda and type delta(lambda) exists, given as a CNF encoding whose correctness is argued in a short note, plus a DRAT/LRAT unsatisfiability proof accepted by a verified checker (cake_lpr or an equivalent formally verified checker); (iii) the check that the conjecture is still open, i.e. the formal-conjectures file is still tagged research open and no newer paper settles it, re-fetched before claiming. Equivalently, a lambda whose box graph is not CDS-colourable, certified the same way. Notifying the authors is an action for a human.

## Partial wins

- **p1:** A reproducible verification of the conjecture for every partition lambda inside a 13 x 13 square (one row or column longer than the published 12 x 12 range). It must ship, for each lambda, or for one of lambda and its conjugate with the symmetry argued, an explicit Latin tableau of type delta(lambda) as a witness file, so that the verifier checks witnesses rather than trusting a search. The partition count must match binomial(26,13) = 10,400,600 including the empty partition.

## How a win is checked

Compute alpha_k by maximum flow: cells are edges of the bipartite row-column graph, and a subgraph of maximum degree k splits into k matchings (Koenig), so alpha_k is the largest number of cells with at most k per row and per column. Compute delta, then check each supplied tableau (no repeated colour in any row or column, colour counts sorted equal to delta). For a counterexample, regenerate the CNF from lambda and delta with your own encoder, check that it equals the supplied CNF up to variable renaming or re-derive the UNSAT proof, and run a verified LRAT checker. Re-run small cases against the paper's examples (Figure 1: shape (4,2,1), type (2,2,2,1)).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Paper/LatinTableau.lean>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i2p48>
- <https://doi.org/10.37236/13248>
- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Paper/LatinTableau.lean>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The paper proves that the first four parts of delta can always be realised, so a counterexample must fail at part 5 or later. Restrict the search to shapes whose normalised CDS (delta-bar_2, ..., delta-bar_7) falls into the long case lists the authors computed but did not publish, and test those shapes far beyond 12 x 12.
- Encode 'type exactly delta' with cardinality constraints, one colour class per colour of size delta_i, each a partial transversal, and use an incremental SAT solver across neighbouring shapes (adding a box changes delta locally).
- Conjugation (transposing lambda, which maps Latin tableaux to Latin tableaux and preserves delta) halves the work, and Proposition 5 means only type delta itself needs testing for each shape. Shapes with many equal parts (rectangles with staircase additions) are the hardest for greedy colourings, so stress-test those first.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Domination of mu by delta is necessary. A shape with no tableau of some arbitrary type mu is not a counterexample unless delta dominates that mu. Test type delta itself.
- alpha_k must be computed exactly by flow or matching, not by a greedy colouring, which underestimates delta and creates false counterexamples.
- A SAT solver's UNSAT answer without a checked proof is not a certificate.
- The 12 x 12 range is already covered, so search outside it.
- Two recent papers prove cases of the different wide partition conjecture (Latin tableaux of shape lambda and type lambda), not this conjecture: Daugherty et al., arXiv:2610.29291 (Oct 2026), and Allsop-Kotlar-Wanless, arXiv:2511.10548. An Academia.edu upload titled 'A constructive AI proof of the Latin Tableau Conjecture with applications' claims a proof. It is unrefereed and could not be read on 2026-10-30 (HTTP 403). If a valid proof exists, no counterexample exists and only p1 remains winnable, so check its status before a long counterexample search.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/latin-tableau-conjecture.md
```

Already set up? Say `run V3R1T4S on latin-tableau-conjecture`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `latin-tableau-conjecture`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
