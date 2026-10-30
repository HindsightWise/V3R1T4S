# Pattern-avoiding involutions: the next exact count of involutions avoiding 1324 (n = 35) or 4231 (n = 41)

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: needs cluster (Bean-Guttmann-Pantone's Mosaic adaptation ran for several weeks on 60 CPU cores with 300 GB of RAM to reach n = 34 and n = 40; one more term needs comparable resources or a faster algorithm) · open as of 2026-10-30

## The problem

Among the involutions avoiding a single pattern of length 4, the classes avoiding 1324 (OEIS A230554) and 4231 (A230556) are the only ones with no known generating function. Of the eight Wilf classes, four had been settled earlier: 1234 by Ira Gessel, 2413 by Robert Brignall, Sophie Huczynska and Vincent Vatter, and 1342 and 2341 by Miklos Bona, Cheyne Homberger, Jay Pantone and Vincent Vatter (2016). Christian Bean, Anthony J. Guttmann and Jay Pantone ('Enumerating Pattern-Avoiding Involutions using Combinatorial Exploration', arXiv:2609.04352, 3 Sep 2026) found algebraic generating functions for 2431 and 3421. By adapting the Mosaic method (a forthcoming counting algorithm of Bean and Pantone), they extended the 1324 count to n = 34 and the 4231 count to n = 40 (ancillary files inv-1324-up-to-34.txt and inv-4231-up-to-40.txt); that computation took several weeks on 60 CPU cores with 300 GB of RAM. On 2026-10-30 the OEIS entries A230554 and A230556 list terms only to n = 20 (last edited 14 Sep 2026; both carry keyword 'more' and cite the 2026 paper), and arXiv v1 is the only version.

## What counts as a win

Success means an exact count of involutions of length n avoiding 1324 for some n >= 35, or avoiding 4231 for some n >= 41 (strictly beyond the paper's ancillary files and the live OEIS b-files, re-checked before claiming), computed by two independently written programs that agree and that both reproduce every term of the corresponding ancillary file exactly.

## Partial wins

- **p1:** An independently written program, using a different method from the Mosaic adaptation (for example a transfer matrix on arc diagrams, or Combinatorial Exploration with an involution-aware strategy), that reproduces all terms in both ancillary files (1324 to n = 34, 4231 to n = 40); reproduction only.

## How a win is checked

Brute force over all involutions for n <= 12 (about 140,000 involutions at n = 12) must match both programs; then compare both programs' outputs with the ancillary files term by term and with each other for the new term. Ratio check: successive ratios should continue the smooth trend used in the paper's asymptotic analysis.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2609.04352>

## Sources

- <https://arxiv.org/abs/2609.04352>
- <https://arxiv.org/src/2609.04352v1/anc/inv-1324-up-to-34.txt>
- <https://arxiv.org/src/2609.04352v1/anc/inv-4231-up-to-40.txt>
- <https://oeis.org/A230554>
- <https://oeis.org/A230556>
- <https://arxiv.org/abs/1310.7003>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- An involution is a matching plus fixed points; encode it as an arc diagram and run a left-to-right transfer method whose state records just enough of the open arcs to detect 1324 (an import of the CGZ transfer matrix to involutions).
- 4231 is reached to n = 40 but 1324 only to n = 34: the 1324 case is harder, so a new idea helps most there.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Reversal does not preserve involutions; 1324 and 4231 involution counts differ from n = 7 on (126 vs 128), so do not transfer terms between the two sequences.
- The ancillary files index by length n starting at n = 1; the OEIS entries start at n = 0.
- a(40) for 4231 is 241,382,018,779,553,682 (about 2.4 * 10^17): it still fits in signed 64-bit, but the next terms (ratio about 3) and intermediate sums in a transfer method soon overflow; use 128-bit or arbitrary precision.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/involutions-avoiding-1324-4231-next-terms.md
```

Already set up? Say `run V3R1T4S on involutions-avoiding-1324-4231-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `involutions-avoiding-1324-4231-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
