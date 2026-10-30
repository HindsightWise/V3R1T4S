# Avoiding words in synchronizing automata: an automaton with n >= 8 states and 1-avoiding threshold 2n-2 (largest known example has 7 states), or one above 2n-2

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-hours to laptop-days (random or structured search; the exact threshold of one n-state automaton takes a BFS over at most 2^n subsets) · open as of 2026-10-30

## The problem

A word w avoids state q of an automaton (Q, Σ, δ) if q is not in δ(Q, w). The 1-avoiding threshold is the maximum, over avoidable states, of the length of a shortest avoiding word. Kisielewicz, Kowalski and Szykuła ('Experiments with Synchronizing Automata', CIAA 2016, Conjecture 5) conjectured that for strongly connected synchronizing n-state automata the threshold is at most 2n - 2. Marek Szykuła restates this for all synchronizing automata as Conjecture 2 in 'Synchronizing Automata: Open Problems' (EPTCS 451 (2026) 33-47, arXiv:2608.24245, 25 Aug 2026). The survey notes that only two particular examples over a minimal alphabet reach 2n - 2, and that 2n - 3 is the best lower bound for all n >= 6. The classical upper bound is (n-2)(n-1) + 2; the survey's subspace-chain refinement lowers this to order n^2 - n log2 n + O(n). Ferens, Szykuła and Vorel (MFCS 2021) give a binary, strongly connected, synchronizing series reaching 2n - 3 for every n. Their examples meeting 2n - 2 include A5 (threshold 8) and a 7-state binary automaton with threshold 12 (their Fig. 3, 'a largest known automaton meeting this bound'). No binary synchronizing automaton exceeds 2n - 3 for n in {8, ..., 11}. Their Conjecture 13: at most 2n - 3, except finitely many cases (and trivial extensions) equal to 2n - 2.

## What counts as a win

Success means an explicit synchronizing automaton (complete DFA, any alphabet, given as a transition table) that is not a trivial extension of a smaller-alphabet automaton (no letter acts as the identity or as a copy of another letter), and that satisfies one of two conditions. (a) It has n >= 8 states and 1-avoiding threshold >= 2n - 2; this beats the largest known example meeting 2n - 2 (7 states, direction: max n). A binary automaton needs n >= 12, since binary n = 8..11 are excluded. (b) It has any n >= 2 states and 1-avoiding threshold >= 2n - 1, which refutes Conjecture 2 of arXiv:2608.24245. Synchronization and the threshold must be confirmed by two independent programs.

## Partial wins

- **p1:** The exact maximum 2-avoiding threshold of binary synchronizing automata with 11 states, computed by two independent exhaustive programs. Both must first reproduce the published values for n = 3..10 (6, 8, 12, 17, 19, 23, 25, 28; Ferens-Szykuła-Vorel MFCS 2021). It counts only if the value for n = 11 is unpublished at claim time. This is labelled computational.

## How a win is checked

Check that the automaton is synchronizing with the pair-automaton BFS. Then BFS from the full set Q over images δ(Q, w), expanding each image by every letter. For each state q, the shortest avoiding word length is the depth of the first image not containing q. Take the maximum over avoidable q. Calibrate by reproducing threshold 12 on the 7-state automaton of Ferens et al. Fig. 3 and 2n - 3 on their binary series, and by checking that the automaton is not a trivial extension.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2608.24245>

## Sources

- <https://arxiv.org/abs/2608.24245>
- <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2021.46>
- <https://doi.org/10.1007/978-3-319-40946-7_15>
- <https://arxiv.org/abs/2508.15655>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search over ternary and quaternary automata with 8-10 states, which earlier exhaustive binary experiments did not cover. Use hill-climbing on transitions with the exact avoiding threshold as the objective.
- Grow the Fig. 3 seven-state automaton: add one state and one letter at a time, keeping strong connectivity, and look for steps that raise the threshold by 2 per added state.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Trivial extensions (adding identity letters or copies of letters) do not count as new examples.
- A non-synchronizing automaton can have far larger avoiding thresholds; the conjecture concerns synchronizing automata only.
- Exhaustive ranges: KKS 2016 Table 2 checked the 2n - 2 bound (their Conjecture 5, stated for strongly connected automata) for all alphabets at n <= 4, up to 8 letters at n = 5, 4 letters at n = 6, 3 letters at n = 7 and 2 letters at n = 8..10. Ferens et al. add binary n = 11. Ternary and larger alphabets at n >= 8 are unchecked.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/synchronizing-avoiding-threshold-2n-2.md
```

Already set up? Say `run V3R1T4S on synchronizing-avoiding-threshold-2n-2`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `synchronizing-avoiding-threshold-2n-2`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
