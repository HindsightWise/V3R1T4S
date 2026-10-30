# (k,s)-SAT threshold: an unsatisfiable 5-CNF in which every variable occurs at most 7 times, proving f(5) <= 6

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days (SAT Modulo Symmetries style search; candidate formulas can be large) · open as of 2026-10-30

## The problem

A (k,s)-CNF has clauses of exactly k literals on k distinct variables, and every variable occurs, positively or negatively, in at most s clauses. Kratochvíl, Savický and Tuza showed that there is a threshold f(k) such that every (k, f(k))-CNF is satisfiable while (k, f(k)+1)-SAT is NP-complete. Known values are f(3) = 3 (Tovey) and f(4) = 4. Hoory and Szeider (SAT 2004 and later papers) built unsatisfiable formulas inside the class MU(1), giving f(5) <= 7, f(6) <= 11, f(7) <= 17, f(8) <= 29 and f(9) <= 51. Gebauer, Szabó and Tardos (arXiv:1006.0744) record that Hoory-Szeider determined f1(5..9) = 7, 11, 17, 29, 51 exactly, where f1 is the MU(1)-restricted threshold, and that these remain the best upper bounds. Zhang, Peitl and Szeider (SAT 2024, arXiv:2405.16149 v3) state f(5) is in [5, 7]. They found the smallest unsatisfiable (3,s) and (3,p,q) formulas for all parameters, and cut the smallest known unsatisfiable (4,5)-CNF from Knuth's 257 clauses to 235 by searching outside MU(1). Their conclusion names the exact value of f(5) as open. An unsatisfiable (5,7)-CNF would show f(5) <= 6.

## What counts as a win

Success means a DIMACS CNF in which every clause has exactly 5 literals on 5 distinct variables, and every variable occurs in at most 7 clauses (counting both polarities), together with a DRAT or LRAT proof of unsatisfiability checked by drat-trim or cake_lpr (or an explicit tree-like resolution certificate that the skeptic checks). The occurrence bound 7 must be STRICTLY LESS (direction: min) than 8, the smallest s for which an unsatisfiable (5,s)-CNF is published (Hoory-Szeider; f(5) <= 7 in arXiv:2405.16149 v3), unless a fresh search for '(k,s)-SAT' or 'f(5)' over the last 24 months shows a published unsatisfiable (5,7)-CNF, in which case the target is solved.

## Partial wins

- **p1:** An unsatisfiable (4,5)-CNF with at most 234 clauses (beating Zhang-Peitl-Szeider's 235), with clause width exactly 4, at most 5 occurrences per variable, and a checked DRAT/LRAT proof.
- **p2:** An unsatisfiable (6,11)-CNF, proving f(6) <= 10 and beating Hoory-Szeider's f(6) <= 11, certified the same way.
- **p3:** An unsatisfiable (7,17)-, (8,29)- or (9,51)-CNF, beating f(7) <= 17, f(8) <= 29 or f(9) <= 51, certified the same way.

## How a win is checked

Parse the CNF. Assert that every clause has exactly k literals with pairwise distinct variables, and count the occurrences of each variable (both polarities) to confirm the maximum is <= s. Then run drat-trim or cake_lpr on the supplied proof; a second solver run, such as kissat, gives a sanity cross-check. For p1, also count the clauses. Then re-fetch arXiv:2405.16149 and search for newer bounds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2405.16149>

## Sources

- <https://arxiv.org/abs/2405.16149>
- <http://www.satisfiability.org/SAT04/programme/43.pdf>
- <https://arxiv.org/abs/1006.0744>
- <https://arxiv.org/abs/math/0411167>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Follow the enforcer route: find a small satisfiable (5,7)-formula that forces a backbone literal false, then join 5 copies with one 5-clause. Search for enforcers with SAT Modulo Symmetries, as Zhang-Peitl-Szeider did for (3,s) and (4,5).
- Leave MU(1): since f1(5) = 7 exactly, any improvement must use minimal unsatisfiable formulas of deficiency >= 2. Combine disjunctive splitting with extra axioms, as in Zhang-Peitl-Szeider's (4,5) construction.
- Design 5-CNFs from combinatorial designs, for example orbit-closed clause sets under a group action, where occurrence counts are uniform by construction, then test unsatisfiability.
- For p1, restart Zhang-Peitl-Szeider's SMS pipeline with new auxiliary axioms. Their artifact is on Zenodo (doi:10.5281/zenodo.11282310); write your own encoder rather than running downloaded code.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Clauses with fewer than k literals, or with a repeated variable, are not allowed. The width must be exactly k.
- Count occurrences of variables, not of literals: x and not-x both count toward s.
- Formulas in MU(1) cannot beat f1(5) = 7, so a search restricted to MU(1) is a dead end for the main criterion.
- An UNSAT claim without a checked proof does not count, and for large formulas the proof file is the deliverable.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/ks-sat-threshold-f5-unsat-5cnf.md
```

Already set up? Say `run V3R1T4S on ks-sat-threshold-f5-unsat-5cnf`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ks-sat-threshold-f5-unsat-5cnf`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
