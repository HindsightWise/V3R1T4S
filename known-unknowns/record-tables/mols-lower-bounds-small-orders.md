# MOLS table: more mutually orthogonal Latin squares of some order n < 500 than the current lower bound (e.g. 4 MOLS of order 22)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days (difference-matrix / permutation-code searches; SAT for small orders) · open as of 2026-10-30

## The problem

N(n) is the largest number of mutually orthogonal Latin squares (MOLS) of order n. The current table of lower bounds for n < 500 is Table 1 of Alice Miller, R. Julian R. Abel, Ivaylo Valkov and Douglas Fraser, 'Implementing the MOLS table for n up to 500', Symmetry 16 (2024) 1678 (CC BY). It updates the Abel-Colbourn-Dinitz Handbook table (2007) with N(14) >= 4 (Todorov), N(18) >= 5 and N(60) >= 5 (Abel), N(35) >= 6, N(48) >= 10, N(63) >= 8 (Janiszczak-Staszewski, J. Combin. Des. 2019), and N(54) >= 8, N(96) >= 10, N(108) >= 9 (Abel-Janiszczak-Staszewski, arXiv:2412.00480), plus the new N(486) >= 8. Selected current lower bounds, as n:N(n) >= value: 14:4, 15:4, 18:5, 20:4, 21:5, 22:3, 24:7, 26:4, 28:5, 30:4, 33:5, 34:4, 35:6, 36:8, 38:4, 39:5, 40:7, 42:5, 44:5, 45:6, 46:4, 50:6, 51:5, 52:5, 54:8, 55:6, 56:7, 57:7, 58:5, 60:5, 62:5. The paper notes that 22 is the only n other than 4 for which three MOLS are known but four are not. Orders 10 and 12 are covered by other bank entries.

## What counts as a win

Success means k MOLS of order n (equivalently a TD(k+2,n), or an (n,k+1,1) difference matrix, which gives k MOLS) with k STRICTLY GREATER than the order-n entry of Table 1 of Miller-Abel-Valkov-Fraser (Symmetry 2024, 16, 1678). The order must satisfy 2 < n <= 499, must not be a prime power, and must not be 6 (N(6) = 1 is proven), 10 or 12. The squares must be verified by two independent checkers. Before claiming, re-fetch the Glasgow eprint and arXiv:2412.00480, and search arXiv for any 2025-2026 improvement at that n. A value already matched in print is not a win.

## Partial wins

- **p1:** k MOLS of order n for one of the orders 567, 622, 635, 754, 756, 764, 766, 774, 778, 802, 810, 822, 826, 894, 906, 916, 920 or 936, with k strictly greater than the value Miller et al. give in their Theorem 4 (8 for 567 and 936, 10 for the others), verified by two independent checkers.

## How a win is checked

For each square, check rows and columns are permutations of 0..n-1. For each pair of squares, check all n^2 ordered symbol pairs are distinct. For a difference matrix over a group G, check that every pair of rows has every element of G exactly once as a difference, then expand to MOLS and run the MOLS check. Use two independent programs.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://eprints.gla.ac.uk/343648/1/343648.pdf>

## Sources

- <https://eprints.gla.ac.uk/343648/>
- <https://eprints.gla.ac.uk/343648/1/343648.pdf>
- <https://doi.org/10.3390/sym16121678>
- <https://arxiv.org/abs/2412.00480>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Order 22: Miller et al. suggest the method of Todorov (used for 4 MOLS(14) and 3 MOLS(22)) with a special (22,6,2) difference matrix; a targeted SAT/exact-cover search over that structure is the classic attack.
- Separable permutation codes and difference matrices with a large automorphism group (the Janiszczak-Staszewski method) produced most recent records; try them at 20, 26, 30, 34, 38.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Prime powers already have N(n) = n-1; they are not targets.
- Orders 10 and 12 belong to the bank entries three-mols-order-10 and erdos-723-projective-plane-order-12; claims there count only there.
- (n,k,1) difference matrices give k-1 MOLS, not k; off-by-one errors are common.
- The Handbook table is stale; compare against Miller et al. Table 1 and newer papers.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/mols-lower-bounds-small-orders.md
```

Already set up? Say `run V3R1T4S on mols-lower-bounds-small-orders`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `mols-lower-bounds-small-orders`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
