# MOONSHOT - Eulerian synchronizing automata: a reset threshold above floor((n^2-3)/2) (refuting the Szykuła-Vorel conjecture), or binary Eulerian records

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (heuristic search; the exact reset threshold is a BFS over 2^n subsets) to needs cluster (exhaustive extensions) · open as of 2026-10-30

## The problem

A complete DFA is Eulerian if its underlying digraph is Eulerian: strongly connected, with every state having in-degree equal to the alphabet size. Kari (Theoret. Comput. Sci. 295, 2003) proved the upper bound n^2 - 3n + 3 for Eulerian synchronizing automata. Szykuła ('Synchronizing Automata: Open Problems', arXiv:2608.24245, Corollary 20) recently improved it slightly, to n^2 - n log2 n + O(n). Szykuła and Vorel (DLT 2016, LNCS 9840; arXiv:1604.02879) gave a 4-letter series with n = 4m + 1 states and reset threshold (n^2-3)/2, and conjectured that floor((n^2-3)/2) is the maximum for n >= 3 (their Conjecture 19, which also asks for (n^2-5)/2 in the binary case). Their exhaustive searches confirmed it for 2 letters with at most 11 states, 4 letters with at most 7, 8 letters with at most 5, and all DFAs with at most 4 states. At n = 7 they also found 2 ternary and 12 quaternary automata meeting the bound. Volkov's living list (arXiv:2508.15655 v4, 13 Jan 2026, item A6) reports all of this. For binary Eulerian automata, Pavel Martyugin (unpublished) proposed a series conjectured to reach (n^2-5)/2 (for odd n in Volkov's list). The 2016 searches found the binary maximum (n^2-5)/2 met uniquely by Martyugin's automata for n in {5, 7, 8, 9, 11} and not reachable for n = 6 and 10. The best published binary lower bound is (n^2 - 3n + 4)/2 (Gusev, Reachability Problems 2011).

## What counts as a win

Success means an explicit Eulerian synchronizing complete DFA with n states whose exact reset threshold is STRICTLY GREATER than floor((n^2 - 3)/2), refuting Szykuła-Vorel Conjecture 19. Two independent programs must confirm the Eulerian property and the threshold. It must have at most 30 states, so that exact BFS is feasible.

## Partial wins

- **p1:** An explicit binary Eulerian synchronizing automaton with odd n >= 13 states and exact reset threshold >= (n^2 - 5)/2, which makes Martyugin's conjectured value explicit beyond n = 11 and beats the published (n^2 - 3n + 4)/2. It counts only if no such automaton for that n is published at claim time.
- **p2:** An exhaustive verification of the floor((n^2-3)/2) bound for a range not covered in Szykuła-Vorel 2016 or Volkov's list: binary Eulerian automata with 12 or 13 states, or 3- or 4-letter Eulerian automata with 8 states. Two independently written programs must agree and must first reproduce the published small cases; the result is labelled computational.

## How a win is checked

Check completeness, that in-degree equals |Σ| at every state, and strong connectivity. Check synchronization with the pair-automaton test, then compute the exact reset threshold by BFS over subset images from Q (bitsets; 2^n subsets). Run a second implementation independently. Calibrate on the Szykuła-Vorel 4-letter series A_m (n = 4m + 1) at n = 5 ((25-3)/2 = 11) and n = 9 ((81-3)/2 = 39), and on the Černý automaton (not Eulerian; expect the Eulerian check to fail).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2508.15655>

## Sources

- <https://arxiv.org/abs/2508.15655>
- <https://doi.org/10.1007/978-3-662-53132-7_31>
- <https://doi.org/10.1016/S0304-3975(02)00405-X>
- <https://arxiv.org/abs/2608.24245>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search near the Szykuła-Vorel series with 3 letters or 5-6 letters, where the reported exhaustive ranges stop; Eulerian moves can be done as transition swaps that preserve in-degrees.
- For p1, reconstruct Martyugin's series from the n <= 11 extremal automata (found by a quick search on binary Eulerian automata with 5-9 states), then extend the pattern to n = 13 and 15.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Eulerian means in-degree equal to the alphabet size at every state, counted with multiplicity; strong connectivity is required.
- Martyugin's series is unpublished; the published binary lower bound is Gusev's (n^2 - 3n + 4)/2.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/eulerian-synchronizing-szykula-vorel-bound.md
```

Already set up? Say `run V3R1T4S on eulerian-synchronizing-szykula-vorel-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `eulerian-synchronizing-szykula-vorel-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
