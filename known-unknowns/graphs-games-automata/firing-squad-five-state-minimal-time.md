# MOONSHOT - Firing squad synchronization: a 5-state minimal-time solution, or a certified proof that none exists (Mazoyer's 6 states have stood since 1987)

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (SAT on joint space-time diagrams for all lengths n = 2..N with an unknown transition table) · open as of 2026-10-30

## The problem

The firing squad synchronization problem (Myhill 1957) concerns a line of n identical finite automata with a boundary marker * beyond each end. At time 0 the leftmost cell is the general G and all others are quiescent Q. Each cell updates from (left, self, right) by one shared table. Q must be stable: (Q,Q,Q) -> Q and (Q,Q,*) -> Q. All n cells must enter the firing state F for the first time simultaneously. Minimal time is 2n-2. Mazoyer (1987) gave a 6-state minimal-time solution, the smallest known (states counted including F). Balzer (1967) claimed, and Sanders (1994) confirmed with a corrected exhaustive search, that no 4-state minimal-time solution exists. Wikipedia still says it is unknown whether a five-state solution exists. The Correa-Gustavo-Lemos-Settle survey (arXiv 2017) calls the existence of a complete 5-state solution (minimal-time or not) the most significant open problem in the area. Only partial 5-state solutions are known: e.g. Umeo-Yanagihara (2007, 2009) synchronize lengths n = 2^k in 3n-3 steps, which is neither all lengths nor minimal time. Clergue, Verel and Formenti (2018) found 718 further 6-state minimal-time solutions, and Nguyen and Maignan (2020) generated millions more, but none with 5 states. A minimal-time solution must synchronize every n, so nonexistence follows from the unsatisfiability of the finite family n = 2..N for some N.

## What counts as a win

Either (A) or (B), under the stated conventions (left-end general, n >= 2, boundary symbol *, F never appears before time 2n-2, all cells F at exactly time 2n-2; the mirror-image right-end convention is equivalent). (A) A 5-state transition table with a machine-checked proof (Lean, Coq or Isabelle) that it is a minimal-time solution for every n >= 2. (B) A DRAT/LRAT UNSAT certificate, checked by drat-trim or cake_lpr, showing that no 5-state table synchronizes all lengths n = 2..N in exactly 2n-2 steps, for an explicitly stated N. Two independently written encodings must both be UNSAT. Sanity checks on the same encoders: SAT, with Mazoyer's table (or another verified 6-state solution) found or accepted, when 6 states are allowed; UNSAT when 4 states are allowed.

## Partial wins

- **p1:** A 5-state table, with Q, G, F and two further states under the conventions above, that a simulator verifies synchronizes every length n = 2..200 in exactly 2n-2 steps, with no F before then. No proof for all n is needed.
- **p2:** A DRAT/LRAT-certified machine proof of the Balzer-Sanders theorem (no 4-state minimal-time solution), by UNSAT of n = 2..N with two independent encodings that pass the 6-state SAT sanity check. It counts only if the verifier's literature check finds no earlier formal or certified proof.

## How a win is checked

For tables: simulate every n in the claimed range with an independent 30-line simulator, checking that F first appears at time 2n-2 in all cells simultaneously. For (A): build the proof assistant file and check that the statement matches the conventions. For (B) and p2: check the certificates, read both encodings (variables for table entries delta(l,c,r) over the non-F centre states, and space-time cell variables for every n), and re-run the 6-state SAT and 4-state UNSAT sanity checks.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://en.wikipedia.org/wiki/Firing_squad_synchronization_problem>

## Sources

- <https://en.wikipedia.org/wiki/Firing_squad_synchronization_problem>
- <https://arxiv.org/abs/1701.01045>
- <https://arxiv.org/abs/2005.08570>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Incremental SAT: add the lengths n = 2, 3, 4, ... as constraints on one shared table, break the symmetry between the two free states, and watch whether the solution count collapses.
- Seed the table structure from the 6-state families (Clergue-Verel-Formenti, Nguyen-Maignan local simulations): try to merge two states of a known solution and repair with SAT.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Convention drift. Sanders states the restriction with the initiator at the right end (the mirror image). Some papers allow the general anywhere (the generalized problem, which is a different open question) or use rings.
- A table that works for n <= N but whose UNSAT or SAT status depends on an encoding bug. Run the 4-state and 6-state sanity checks.
- Non-minimal-time 5-state solutions do not count toward (A) or (B), although a complete one would settle the survey's broader open question.
- Hybrid (non-uniform) CA 'solutions', e.g. arXiv 1212.3069's 4-state rule 60/102 hybrid, are a different model and do not count.
- An audit on 2026-10-30 found no 2021-2026 arXiv paper or web result on 5-state minimal-time solutions, and Wikipedia (edited 2026-10-22) still calls the question open. Journal papers off arXiv (Umeo, Yunes, Kobayashi) were not searched exhaustively, so re-check them before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/firing-squad-five-state-minimal-time.md
```

Already set up? Say `run V3R1T4S on firing-squad-five-state-minimal-time`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `firing-squad-five-state-minimal-time`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
