# Skew-Hadamard matrices: an order where none is known (smallest 356 = 4*89)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (Goethals-Seidel difference families with a skew block, multiplier-orbit searches; checking takes laptop-seconds) · open as of 2026-10-30

## The problem

A Hadamard matrix H is skew if H + H^T = 2I; Seberry conjectured that skew-Hadamard matrices exist at every order divisible by 4. Known sources include Paley's q+1 (q = 3 mod 4), doubling, Spence's family, good matrices and Goethals-Seidel arrays with a skew supplementary difference set. D. Ž. Đoković (arXiv:2301.02751 v3, 24 Nov 2024) constructed the first skew-Hadamard matrices of orders 276 (v = 69) and 292 and listed the odd v < 200 for which order 4v was undecided: 89, 101, 107, 119, 149, 153, 167, 177, 179, 191, 193. Cati and Pasechnik (arXiv:2411.18897 v2, 30 Aug 2025) implemented every known construction up to order 1208 in SageMath and count 41 orders up to 1208 with no known skew-Hadamard matrix (their Table 5 gives, for odd v <= 999, the least m with a skew matrix of order 2^m v known; the v listed there have none at 4v). Table 3 of Egan, Kotsireas, London and Ó Catháin (arXiv:2610.27175, 19 Oct 2026) gives 356 as the smallest open skew order. In October 2026 K. Kumar (github.com/vatskishan03/Hadamard, folder skew/) posted skew-Hadamard matrices at about 110 further orders, measured against an unpublished Đoković-Seberry census of May 2025; the smallest are 476 = 4*119 (added 23 Oct 2026, after the survey), 820, 836, 980 = 4*245 (added 24 Oct 2026), 996, 1012, 1036, 1044, 1100, 1140, 1148 and 1204. Remaining small open orders: 356, 404, 428, 596, 612, 708, 764, 772 (v = 89, 101, 107, 149, 153, 177, 191, 193). At 668 = 4*167 and 716 = 4*179 Hadamard matrices were announced in 2026; the sources read here do not say whether any of them is skew.

## What counts as a win

Success means an explicit n x n matrix H with entries +-1, H + H^T = 2I and H H^T = nI (both checked exactly) for n in {356, 404, 428, 596, 612, 708, 764, 772}, verified by two independent programs, where no skew-Hadamard matrix of that order is reported at claim time in Table 3 of the latest version of arXiv:2610.27175, in the skew/ folder and README of github.com/vatskishan03/Hadamard, or in a fresh arXiv search (direction: none; existence target).

## Partial wins

- **p1:** A skew-Hadamard matrix of order 4v for odd v with 200 < v < 300 that Cati-Pasechnik's Table 5 (arXiv:2411.18897 v2) leaves without a construction and that Kumar's skew/ folder does not contain at claim time: 804, 900, 916, 932, 940, 1004, 1028, 1060, 1076, 1108, 1156, 1180 or 1196, with the census status reported in Kumar's skew/README.md also checked, verified as in the main criterion.
- **p2:** A skew-Hadamard matrix of order 668, 716, 892 or 1132 (orders with 2026 Hadamard matrices of unstated type), exhibited in skew form H + H^T = 2I, after the claimant shows that no skew matrix of that order is public.

## How a win is checked

Check entries are +-1, H + H^T = 2I exactly (diagonal all +1 and H_ij = -H_ji off the diagonal) and H H^T = nI in integer arithmetic; use two independent checkers. A matrix that is only equivalent to a skew one must be presented in skew form. If the claim is a Goethals-Seidel difference family with a skew block, expand it into the array with the verifier's own code and check the full matrix.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.27175>

## Sources

- <https://arxiv.org/abs/2610.27175>
- <https://arxiv.org/abs/2301.02751>
- <https://arxiv.org/abs/2411.18897>
- <https://github.com/vatskishan03/Hadamard/blob/main/skew/README.md>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Goethals-Seidel array with a cyclic difference family (v; k0, k1, k2, k3; lambda) whose first block is skew (X0 and -X0 partition Z_v minus 0); Đoković's order-292 matrix used blocks that are unions of cosets of the order-9 subgroup of Z_73^*.
- Multiplier orbits: for prime v (89, 101, 107, 149, 179, 191, 193) the group Z_v^* has many subgroups; prescribing invariance reduces the search to orbit unions.
- Good matrices, G-matrices and skew-propus families give skew matrices of order 4v from four circulants of order v; SAT+CAS found new good matrices (Bright, Đoković, Kotsireas, Ganesh 2019).
- Amicable orthogonal designs with Seberry's theorem, Wallis's product and Kumar's skew 3(q+1) theorem: check whether an open order follows from a 2026 ingredient before searching.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A Hadamard matrix of the same order is not enough: 428, 668 and 716 have Hadamard matrices but, as far as these sources say, no skew one.
- Skew means H + H^T = 2I (diagonal +1), not H = -H^T.
- The 2007 Handbook table listed 63 for 69, and the Seberry-Yamada 2020 book lists some settled values as unknown; use the 2024-2026 lists.
- The Đoković-Seberry census is not public; Kumar's README reports its statuses, and the survey's Table 3 row also says 'known for 4n with odd n < 250', which conflicts with its own smallest-open value 356 and with Đoković's list. Treat that phrase as a misprint and re-check every source before claiming.
- Kumar's folder moves fast: 476 (v = 119) and 980 (v = 245) were added on 23-24 Oct 2026, after the survey, so the survey and Cati-Pasechnik still show them as open. Re-read skew/README.md and its commit history on the day of the claim.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/skew-hadamard-unknown-orders.md
```

Already set up? Say `run V3R1T4S on skew-hadamard-unknown-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `skew-hadamard-unknown-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
