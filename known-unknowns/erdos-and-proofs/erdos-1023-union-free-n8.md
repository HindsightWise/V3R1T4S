# Erdős #1023 small cases: 80 subsets of an 8-set with no member a union of others (OEIS A347025; best known 79, upper bound 89)

✏️ **Erdős problems and proofs** · standard · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

F(n) is the largest family of nonempty subsets of {1..n} in which no member is the union of other members (OEIS A347025, Jukka Kohonen 2021, keyword more). Equivalently, it is the maximum number of meet-irreducible elements in a lattice with n join-irreducibles (Süskind, Sep 2026). Erdős Problem #1023 asks for its asymptotics; they follow from Kleitman's solution of #447: F(n) ~ C(n, n/2). Known values for n = 0..7 are 0, 1, 2, 4, 7, 13, 24, 44. a(6) = 24 is due to Jinyuan Wang (2022). a(7) = 44 is due to William Blair (6 Jun 2026), who closed Wang's 44 <= a(7) <= 45 with an exhaustive OR-Tools CP-SAT search under two independent encodings and published a 44-set witness and verifier. For n = 8 the best lower bound is 79, from Jon E. Schoenfield's 2022 construction family, which gives 79, 144 and 270 for n = 8, 9, 10 (against C(n, ceil(n/2)) = 70, 126, 252). Andy Loo's recursive bound a(n) <= min_h a(h) + 2^h·a(n-h) (arXiv:1511.00170) with a(7) = 44 gives a(8) <= 1 + 2·44 = 89. So 79 <= a(8) <= 89 on 2026-10-30, with the entry last edited 2026-09-27.

## What counts as a win

Success means an explicit list of at least 80 distinct nonempty subsets of {1..8} (direction: max, strictly above 79) such that no member S equals the union of the other members contained in S. The verifier checks this for every S, which covers unions of any number of other members. The size must exceed every value in the live https://oeis.org/A347025 entry, its comments, links and history, re-fetched immediately before claiming, and any value found in a fresh literature check. More than 89 sets contradicts Loo's bound and means a bug.

## Partial wins

- **p1:** An explicit union-free family (same check) of at least 145 subsets of {1..9} or at least 271 subsets of {1..10}, beating Schoenfield's construction values 144 and 270.
- **p2:** A certified upper bound a(8) <= 88 or lower, i.e. an LRAT-checked UNSAT proof (or VIPR certificate) that no union-free family of size 89 on {1..8} exists, on a CNF/ILP the skeptic regenerates from the published encoding.
- **p3:** The exact value of a(8) (including the case a(8) = 79): an explicit family of that size plus an optimality certificate of the p2 standard.

## How a win is checked

For each member S, OR together all other members T with T ⊂ S and assert the result is not S. Check distinctness and non-emptiness. For upper bounds, regenerate the encoding (x_S selects S; S selected implies some element of S is covered by no selected proper subset of S) and check the proof with cake_lpr or a VIPR checker. Reproduce a(4..7) with the same code first.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A347025>

## Sources

- <https://www.erdosproblems.com/1023>
- <https://oeis.org/A347025>
- <https://arxiv.org/abs/1511.00170>
- <https://www.erdosproblems.com/447>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reuse Blair's published CP-SAT model and verifier (linked from A347025): it reproduces a(4..7), so add S_8 symmetry breaking and a solution hint from Schoenfield's 79-set family, and run with many workers.
- Build structured families: a near-middle layer plus extra sets in adjacent layers chosen so that no added set is covered by its subsets in the family; Schoenfield's formula is one such scheme, so try other layer profiles by ILP over orbit counts.
- Local search with incremental checks: maintain for every set the union of its family subsets; add/remove moves update only supersets and subsets, so tabu search on 255 candidates is fast.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- 'Union of other members' includes unions of any number of members, not only of two (two is Erdős #447, a different problem).
- The empty set is excluded in A347025's convention (it would be the empty union).
- Loo's table predates a(6) and a(7); recompute the recursive upper bound with the current values rather than copying the published table.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-1023-union-free-n8.md
```

Already set up? Say `run V3R1T4S on erdos-1023-union-free-n8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-1023-union-free-n8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
