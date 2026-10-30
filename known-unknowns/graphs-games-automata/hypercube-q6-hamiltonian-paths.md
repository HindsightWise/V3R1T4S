# Gray codes: the number of Hamiltonian paths in the 6-cube (A091299(6), open since 2005)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (or laptop-weeks): meet-in-the-middle over the bipartite halves in the style of Haanpaa and Ostergard · open as of 2026-10-30

## The problem

A091299 counts directed Hamiltonian paths (not necessarily cyclic Gray codes) in the n-cube: 2, 8, 144, 91392, 187499658240. The value for n = 5 is from Janez Brank (2005), and A003043 (paths with a marked start) has 5859364320 for n = 5. For Hamiltonian cycles the 6-cube is done: A066037(6) = 35,838,213,722,570,883,870,720 (Harri Haanpaa and Patric Ostergard, 'Counting Hamiltonian cycles in bipartite graphs', Math. Comp. 2014, correcting Deza-Shklyar 2010). The 6-cube path counts A091299(6) and A003043(6) are still missing, and so is the 7-cube cycle count A066037(7), which is the famous moonshot behind this one. OEIS checked live 2026-10-30: A091299 (last edit 2026-10-27, links only) and A003043 both end at n = 5 with keyword 'more', no pending drafts.

## What counts as a win

Success means the exact value of A091299(6), the number of directed Hamiltonian paths in Q6 (equivalently A003043(6) = A091299(6)/64, the factor 2^n checked against n = 5), computed by two independent methods or decompositions that agree exactly. The code must reproduce A091299(1..5), and run in cycle mode it must reproduce A066037(6) of Haanpaa and Ostergard. OEIS re-fetched before claiming must still lack the value.

## Partial wins

- **p1:** N3 or N5: the number of (undirected) Hamiltonian paths in Q6 between a fixed vertex and a fixed vertex at distance 3 (N3) or distance 5 (N5). It must come from two methods that agree, and the code must also reproduce the analogous Q5 class counts and N1 = 2*A066037(6)/6 = 11946071240856961290240 (paths with adjacent ends, known from the cycle count). The decomposition is A091299(6) = 64*(6*N1 + 20*N3 + 6*N5).
- **p2:** An independent recomputation of A066037(6) by an algorithm different from Haanpaa and Ostergard's, agreeing exactly, with source and logs.

## How a win is checked

Skeptic: check the endpoint decomposition A091299(n) = 2^n * sum over odd d of C(n,d)*N_d, against the Q5 data and with N1 = 2*A066037(n)/n. Recompute one class with the claimant's code modulo a fresh prime. Rerun the code for Q5 paths and Q6 cycles.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A091299>

## Sources

- <https://oeis.org/A091299>
- <https://oeis.org/A003043>
- <https://oeis.org/A066037>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A091299 counts directed paths with a distinguished start; A003043 marks the start node differently. Recheck the factor against n = 5 (187499658240 vs 5859364320 differ by 32 = 2^5, the number of start nodes).
- The Deza-Shklyar 6-cube cycle value was wrong; use Haanpaa-Ostergard's corrected value as the cycle-mode check.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/hypercube-q6-hamiltonian-paths.md
```

Already set up? Say `run V3R1T4S on hypercube-q6-hamiltonian-paths`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hypercube-q6-hamiltonian-paths`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
