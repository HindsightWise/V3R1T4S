# Randomized list update (partial cost model): a lower bound above Ambuhl's 1.50115, or a 5-item algorithm certified below COMB's 1.6

⚡ **Algorithms** · standard · tractability ★★☆☆☆ · compute: laptop-days (game trees over list states: 5! = 120 states for five items, 720 for six; exact rational LPs) · open as of 2026-10-30

## The problem

In list update an online algorithm keeps a list of n items. Accessing the item in position i costs i - 1 in the partial cost model. The accessed item may move forward for free; other swaps cost 1. Randomized algorithms face an oblivious adversary. The optimal randomized competitive ratio is open. The best algorithm is COMB (Albers, von Stengel and Werchner 1995), which runs BIT with probability 4/5 and TIMESTAMP with probability 1/5 and is 1.6-competitive. With two items a lower bound of 1.5 is easy. Ambuhl, Gartner and von Stengel (TCS 268, 2001) proved 1.50084 for five-item lists by game trees and a modified Teia argument. Ambuhl's ETH thesis (2002) improved this to 1.50115. Their TALG 2013 paper (arXiv:1002.2440) states the ratio lies between 1.50115 and 1.6, with the true value unknown. It also proves that no projective algorithm beats 1.6. A non-projective partial-order algorithm is 1.5-competitive for lists of up to four items. Extending that approach to five items 'is not straightforward', and no non-projective algorithm is known to beat 1.6 there.

## What counts as a win

Either (a) a lower bound c >= 1.5012 on the randomized competitive ratio in the partial cost model (higher is better; the margin covers rounding of 1.50115). It is given as an explicit Yao-type certificate: a finite list length n, a finite family of request phases with rational probabilities (or a game tree as in Ambuhl-Gartner-von Stengel), and an exact rational computation. The computation shows that every deterministic online algorithm, from every list state, pays in expectation at least c times the offline optimum per phase, up to an additive constant that vanishes over repeated phases. A claim below 1.5012 counts only by an exact comparison with Ambuhl's certificate. Or (b) a randomized online algorithm, possibly non-projective, with a machine-checkable proof that it is c'-competitive for all list lengths with c' < 1.6. Re-check arXiv and recent ICALP/ESA/SODA papers for newer list update bounds before claiming. Values in unmerged pull requests are not bars.

## Partial wins

- **p1:** Lists of exactly five items: a randomized (necessarily non-projective) online algorithm whose competitive ratio in the partial cost model is certified strictly below 1.6. The certificate is finite and exact, for example a potential-function LP over (list state, algorithm memory state, OPT list state) with a rational solution.

## How a win is checked

For (a), enumerate list states (n! permutations) and compute exactly, by DP over each phase's request sequences, the minimum expected online cost against the adversary's distribution and OPT's cost with paid exchanges. Check the per-phase inequality and the amortisation argument. Calibrate on the two-item 1.5 bound and on reproducing 1.50084 for five items. For p1 and (b), verify the potential-function inequalities for every transition in exact rational arithmetic, including paid exchanges by OPT. Calibrate on COMB (1.6) and on the four-item 1.5-competitive algorithm.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1002.2440>

## Sources

- <https://arxiv.org/abs/1002.2440>
- <https://doi.org/10.1145/2500120>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The 1.50084 to 1.50115 gain came from better game trees on five items. Six-item lists (720 states) are now cheap; a larger tree search with LP-optimised phase distributions is the direct route.
- For p1, the four-item 1.5 algorithm uses partial orders as memory. Search small memory automata for five items with an LP whose feasibility certifies competitiveness.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Partial and full cost models differ (access cost i - 1 vs i); in the full cost model the best randomized lower bound is Teia's 1.5 and needs long lists. Do not mix them.
- AGvS's 1.6 lower bound for projective algorithms is not a bound for all algorithms. Only non-projective algorithms can win (b) or p1.
- Oblivious adversary only; adaptive adversaries give deterministic-like bounds.
- Other list update models are different cells: the uniform-cost model, where every swap costs 1 (Basiak, Bienkowski, Bohm, Chrobak, Jez, Sgall and Tatarczuk, arXiv:2503.17264: 3.3904); the paid-exchange model P^d (Albers and Janke, STACS 2020); and iid request models.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/randomized-list-update-partial-cost-bounds.md
```

Already set up? Say `run V3R1T4S on randomized-list-update-partial-cost-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `randomized-list-update-partial-cost-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
