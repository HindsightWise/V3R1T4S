# Pairwise maximin share (PMMS): an additive instance whose best PMMS factor is below Gölz's 78/79 (goods) or above 1.102065 (chores)

🃏 **Wildcard** · standard · tractability ★★★☆☆ · compute: laptop-minutes to laptop-hours; a 3-agent, 9-good instance checks in under a second (3^9 allocations), and 4-5 agents with 10-12 items check in minutes · open as of 2026-10-30

## The problem

An allocation X of indivisible goods is PMMS if, for every pair of agents i and j, v_i(X_i) >= mu_i(2, X_i u X_j), the best worst bundle agent i can get by splitting the pair's pooled goods in two. Its PMMS factor is the min over pairs of v_i(X_i)/mu_i(2, X_i u X_j) (pairs with mu = 0 skipped). alpha*(I) is the best factor over all allocations; chores are defined dually with rho*(I). Whether PMMS always exists for additive goods was open from Caragiannis et al. (2016) until September 2026, when three groups answered it negatively: Aziz (arXiv:2609.06282, four agents), Gölz (arXiv:2609.08954, three agents and nine goods) and Bei, Lin, Liu, Luan and Tao (arXiv:2609.10493). Gölz also gave a 3-agent, 9-good instance with alpha* = 78/79, checked by exhaustive enumeration. Bei et al. give goods 226/227 and a five-agent, twelve-chore instance with rho* = 220413/200000 = 1.102065, prove every additive chores instance has a 4/3-PMMS allocation, and pose closing 0.7808 <= alpha_PMMS <= 78/79 and 1.102065 <= rho_PMMS <= 4/3 as open problems. Kurokawa's (sqrt 17 - 1)/4 ~ 0.781 is the best goods guarantee. This lane checker reproduced 78/79 exactly on Gölz's instance.

## What counts as a win

An explicit additive instance with nonnegative integer values (or costs) such that either (goods) alpha*(I) < 78/79, or (chores) rho*(I) > 220413/200000, both strictly (direction: goods lower, chores higher). The definitions follow Section 2 of arXiv:2609.10493: two-way maximin share mu_i(2,S), and the factor is the min over ordered pairs i != j with mu_i(2, X_i u X_j) > 0 (dually for chores). The claim gives the exact optimal factor as a fraction, an allocation attaining it, and an exhaustive exact certificate checkable in laptop-hours. Bars are re-checked at claim time against the latest versions of arXiv:2609.08954 and 2609.10493 and any newer paper.

## Partial wins

- **p1:** A strictly positive additive goods instance with n = 3 and at most 8 goods that has no exact PMMS allocation (alpha* < 1). Gölz found none and believes 9 is minimal or nearly so; PMMS exists when m <= n + 2 (Amanatidis et al.).
- **p2:** An additive chores instance with exactly three agents and no exact PMMS allocation (rho* > 1), provided no published three-agent chores PMMS counterexample exists at claim time.

## How a win is checked

Independent exact checker: precompute mu_i(2,T) for every subset T by subset-sum reachability, enumerate all n^m complete allocations, and compute each allocation's factor with fractions.Fraction. Negative control: Gölz's instance (u1 = 1 3 4 5 8 14 16 18 23, u2 = 10 2 15 6 8 22 31 30 32, u3 = 14 2 22 13 15 27 42 38 48) must return exactly 78/79, attained at allocation (2,0,2,0,2,2,1,1,0). Bei et al.'s Table 2 instance must return 226/227. Re-fetch the status source before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.10493>

## Sources

- <https://arxiv.org/abs/2609.10493>
- <https://arxiv.org/abs/2609.08954>
- <https://arxiv.org/abs/2609.06282>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Bei et al.'s chores-to-goods reduction (their Lemma 1) preserves PMMS existence. A strong chores instance may transfer to goods with a computable factor.
- Gölz's instances have three large goods plus small goods and a makeweight. Use them as seeds for local search with the exact factor as objective; 4-agent seeds include Aziz's instance.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- For n = 2, PMMS coincides with MMS and always exists for additive goods (cut and choose). Use at least 3 agents.
- Several conventions exist for pairs with mu = 0 and for empty bundles. Use the convention in Section 2 of arXiv:2609.10493 and state it.
- Exact PMMS non-existence alone is already published; a new instance must beat the quantitative bar.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/pmms-impossibility-factors.md
```

Already set up? Say `run V3R1T4S on pmms-impossibility-factors`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pmms-impossibility-factors`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
