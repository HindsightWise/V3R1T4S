# Single-deletion-correcting binary codes of length 12: is the Varshamov-Tenengolts code (316 words) optimal? (bounds 316-320)

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (exact independent-set or ILP search on a 4,096-vertex graph with symmetry; checking a code takes milliseconds) · open as of 2026-10-30

## The problem

A binary code of length n corrects one deletion when no two codewords share a subsequence of length n-1. Equivalently, it is an independent set in Sloane's graph 1dc.2^n. The Varshamov-Tenengolts code VT_0(n) has A000016(n+1) words: 30, 52, 94, 172, 316 for n = 8..12. It has long been conjectured optimal (Levenshtein; N. J. A. Sloane, 'On single-deletion-correcting codes', 2002). Optimality is proved for n <= 10 (n = 10 by Brian Borchers in 2005 with Lovasz-theta branch and bound, recorded on Sloane's challenge page). For n = 11, Kazuhisa Nakasho, Manabu Hagiwara, Austin Anderson and J. B. Nation proved that 172 is optimal (arXiv:2309.14736, 2023), by integer linear programming with added linear constraints. For n = 12 their method could not go below the upper bound of 320 from Albert No (Entropy 21:1202, 2019), so the maximum size M(12) lies in 316..320 (their Table 1). Sloane's challenge page (oeis.org/A265032/a265032.html, last updated Dec 2015) still lists 1dc.2048 as 'most wanted' and has no 4,096-vertex graph. No later result was found on 2026-10-30.

## What counts as a win

Either (a) RECORD: an explicit set of at least 317 distinct binary words of length 12 whose single-deletion balls are pairwise disjoint (checked for all pairs), which would show VT_0(12) is not optimal; or (b) CLOSURE: a proof that M(12) = 316 with a certificate checkable without trusting the search. That means a VeriPB proof log for a maximum-independent-set or ILP formulation verified by VeriPB (preferably CakePB), or an exact-arithmetic branch-and-bound certificate (VIPR, checked by viprchk), together with a short argument that the encoding is correct and that any symmetry breaking is valid. Direction: (a) max size, (b) upper bound equal to 316.

## Partial wins

- **p1:** A certified upper bound of 319, 318 or 317 on M(12), below No's 320. This means an exact rational certificate of an LP/ILP relaxation or a verified proof log as in (b), rebuilt by the checker from the definition.

## How a win is checked

For a code: compute every word's deletion ball (the set of length-11 subsequences) and check that the balls are pairwise disjoint. Rebuild the 1dc-type graph on 4,096 words from the definition and confirm independence. For a bound: run VeriPB/CakePB on the proof log, or viprchk on the VIPR file. Rebuild the model from the definition, not from the claimant's files. Before claiming, re-read arXiv:2309.14736 (and later versions) and search for later work on single-deletion code bounds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2309.14736>

## Sources

- <https://arxiv.org/abs/2309.14736>
- <https://oeis.org/A000016>
- <https://oeis.org/A265032/a265032.html>
- <https://www.mdpi.com/1099-4300/21/12/1202>
- <https://neilsloane.com/doc/dijen.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Use the symmetries of the deletion metric (reversal and complement, which generate a group of order 4) to break symmetry, and split the words by weight and by number of runs. Deletion balls of words with r runs have size r, which gives strong weighted clique-cover constraints.
- Nakasho et al. needed extra valid inequalities to close n = 11; derive families of clique inequalities from shared subsequences (each length-11 string's preimage set is a clique) and add Lovasz-theta or SDP cuts.
- A closure via proof-logged search (Glasgow solver with VeriPB) on a reduced, symmetry-broken model is more checkable than a commercial-solver log.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Sloane's challenge page is stale: it still lists 1dc.2048 (n = 11) as open, but 172 was proved optimal in arXiv:2309.14736.
- Codes correcting one insertion are the same as single-deletion codes, but codes correcting a deletion OR a substitution, multiple deletions (see the bank's multiple-deletion entry) or deletions over larger alphabets are different problems.
- A Gurobi or CPLEX 'optimal' log is not a certificate; the closure needs an independently checked proof.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/single-deletion-codes-length-12.md
```

Already set up? Say `run V3R1T4S on single-deletion-codes-length-12`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `single-deletion-codes-length-12`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
