# MOONSHOT - The 28-queens count Q(28) (OEIS A000170(28), open since the Q27 project in 2016)

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (Q(27) took about a year on FPGAs in 2015-16 and 28.4 days on eight RTX 5090 GPUs in 2025; Yao-Li project Q(28) at about 11 months on 8 GPUs or about 50 days on 64) · open as of 2026-10-30

## The problem

Q(n) counts placements of n nonattacking queens on an n x n board. Q(25) took about 53 CPU-years (INRIA ProActive, 2005, confirmed by Yuh-Pyng Shieh's NTU project). Q(26) came from Queens@TUD (2009). Q(27) = 234,907,967,154,122,528 came from the Q27 project of Thomas B. Preusser and Matthias R. Engelhardt (FPGAs, 2016; 'Putting Queens in Carry Chains, No. 27', J. Signal Process. Syst. 2017). Guangchao Yao and Yali Li (arXiv 2511.12009, Nov 2025, PPoPP 2026) confirmed Q(27) independently in 28.4 days on eight RTX 5090 GPUs. They project Q(28) at about 11 months on that machine (about 50 days on 64 GPUs) and report no value. Michael Simkin (2021) gave the asymptotics, and Hugo Nielsen (arXiv 2601.05856, 2026) proved 4 | Q(n) for n >= 6. Related tables: point-symmetric solutions A032522 are known to n = 40 (W. Schubert), quarter-turn-symmetric solutions A033148 to n = 67 in the b-file (plus a(69) in a comment), and toroidal solutions A051906 to n = 34. QuantumBFS/quantum.harness issue #34 (June 2026, a summer-school challenge list, no prize) also names Q(28) as open; nothing has been posted there. OEIS checked live 2026-10-30: A000170 and A002562 (up to symmetry) end at n = 27, no pending drafts.

## What counts as a win

Success means the exact value Q(28) = A000170(28), computed by two independent runs that agree exactly. They must use different search decompositions (for example different first-row or symmetry splits) or different programs. The symmetry-class identity A002562(n) = (A000170(n) + A032522(n) + 2*A033148(n))/8 holds for every published n = 4..27. With the published A032522(28) = 1250901440 and A033148(28) = 32896 it gives A002562(28) = (Q(28) + 1250967232)/8, which must come out an exact integer, and it is reported. So Q(28) must be divisible by 8, which is stronger than Nielsen's 4 | Q(n). The program must reproduce Q(n) for n <= 23 and the Q27 project's published sub-counts where available. OEIS re-fetched before claiming must still lack Q(28).

## Partial wins

- **p1:** The next unknown term of A032522 (point-symmetric n-queens solutions, known to n = 40, so a(41)) or A033148(68) (rotationally symmetric solutions; the b-file ends at n = 67 and a(69) is already given in a comment, so it does not count), two runs agreeing, reproducing all published terms.
- **p2:** A051906(35): the number of n-queens solutions on the 35 x 35 toroidal board (first unknown; nonzero since gcd(35, 6) = 1), two runs agreeing, reproducing A051906 and A007705 published terms.

## How a win is checked

Skeptic: rerun the program for n <= 20; recompute a random sample of the claimed split subtotals for n = 28 independently; check that Q(28) is divisible by 8 and that (Q(28) + 1250967232)/8 is an integer (the symmetry-class identity with the published A032522(28) and A033148(28)).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A000170>

## Sources

- <https://oeis.org/A000170>
- <https://oeis.org/A002562>
- <https://github.com/preusser/q27>
- <https://arxiv.org/abs/2511.12009>
- <https://oeis.org/A032522>
- <https://oeis.org/A033148>
- <https://oeis.org/A051906>
- <https://arxiv.org/abs/2107.13460>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Distributed n-queens projects have reported wrong values before (A140393 records the NQueens@Home a(24) discrepancy); per-subproblem checksums and duplicate runs are essential.
- A002562 counts solutions up to the 8 board symmetries; symmetric solutions need separate counts to convert.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/n-queens-q28.md
```

Already set up? Say `run V3R1T4S on n-queens-q28`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `n-queens-q28`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
