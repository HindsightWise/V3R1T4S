# Erdos #580 (Erdos-Furedi-Loebl-Sos n/2-n/2-n/2 conjecture): a counterexample, or certified verification for n = 20

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-days (SAT with DRUP/LRAT proofs over the trees on 10 vertices) · open as of 2026-10-30

## The problem

Conjecture of Erdos, Furedi, Loebl and Sos (Erdos #580): if at least n/2 vertices of an n-vertex graph G have degree at least n/2, then G contains every tree on at most n/2 vertices. Ajtai-Komlos-Szemeredi proved an approximate version, and Zhao (EJC 18 (2011) P27) proved it for all sufficiently large n, with no explicit threshold. The problem's status on the site database is 'decidable'. Zeraoulia Rafik (forum proof claim of 14 Jul 2026, updated 16 Jul 2026, with a manuscript and a Zenodo archive of CNF files and DRUP certificates) claims the vertex formulation for every n <= 19. The main new computer case is n = 18: of the 47 trees on 9 vertices, 42 are handled by theory, and the other 5 reduce to four rooted-core configurations whose SAT instances are certified UNSAT; each odd order follows from the even order below it by deleting a high-degree vertex. A moderator reclassified it as a partial proof claim (23 Jul 2026), and it is not verified by the site. In the same thread Johan Land (23 Jul 2026) said he had extended the check to n <= 21, but posted no code or certificates.

## What counts as a win

CONFIRMED: an explicit graph G on n vertices with at least ceil(n/2) vertices of degree >= n/2, and an explicit tree T on at most n/2 vertices that is not a subgraph of G. Non-containment is certified by an exhaustive embedding search (or an UNSAT certificate) that two independent implementations reproduce.

## Partial wins

- **p1:** A certified verification for n = 20: every graph satisfying the degree hypothesis contains every tree on at most 10 vertices. Reductions are written out, every SAT case comes with a DRAT/LRAT proof checked by a verified checker, and the tree list matches the 106 unlabelled trees on 10 vertices (OEIS A000055). This counts only if no certified n = 20 verification (code and proofs) is public at verification time; Johan Land's 23 Jul 2026 forum statement, with nothing posted, does not count as one.
- **p2:** The same certified verification for n = 22 (every tree on at most 11 vertices; 235 unlabelled trees on 11 vertices, OEIS A000055). n = 21 alone does not count, since it follows from n = 20 by the odd-order reduction.

## How a win is checked

For a counterexample: check the degree condition, then run two independent subgraph-isomorphism searches (for example a VF2-style search and a SAT encoding) showing T is not in G. For p1/p2: referee the reduction, regenerate the CNF instances from the stated encoding, and check every proof with cake_lpr or drat-trim.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/580>

## Sources

- <https://www.erdosproblems.com/580>
- <https://www.erdosproblems.com/forum/thread/580>
- <https://www.erdosproblems.com/forum/thread/580/proof-claims>
- <https://doi.org/10.5281/zenodo.21348157>
- <https://doi.org/10.37236/514>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reuse the edge-minimal-counterexample reduction to a bipartite structure from the n <= 19 manuscript, and encode only the trees that the embedding theorems do not handle.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The n <= 19 result is a proof claim, not yet accepted; read it before building on it.
- There are two formulations: the site's vertex version (every tree on at most n/2 vertices) and the stronger classical EFLS/Zhao edge version (every tree with at most n/2 edges), plus Komlos-Sos variants with k. The n <= 19 claim covers only the vertex version; state which one is verified.
- Zhao's 'sufficiently large n' gives no explicit threshold, so finite checks cannot close the problem.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-580-efls-small-cases.md
```

Already set up? Say `run V3R1T4S on erdos-580-efls-small-cases`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-580-efls-small-cases`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
