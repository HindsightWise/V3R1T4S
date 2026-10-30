# Meanders and semi-meanders: the next exact term of OEIS A005316 (open meanders, known to n = 58) or A000682 (semi-meanders, known to n = 49)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (Jensen-type transfer matrix over arch configurations with modular arithmetic; memory is the bottleneck) · open as of 2026-10-30

## The problem

Arnold's meander numbers count ways a river can cross a road n times (A005316), with closed meanders A005315(n) = A005316(2n-1). Iwan Jensen's transfer-matrix method gave A005316 to n = 44 and semi-meanders A000682 to n = 45. Andrew Howroyd's C# software extended A005316 to n = 55 (and A005315 to 28). In 2026 Alexy Khrabrov ('Counting Arnold's Meanders with Verified Algorithms', with Lean 4, Rust and OxCaml programs) contributed the A005316 b-file to n = 58. Hunter Hogan (mapFolding, Oct 2026) extended A000682 to n = 49, and his repository lists A000682(50) as a planned computation (estimated at hours with 64 GB of memory). OEIS checked live 2026-10-30: no pending drafts. The field is active, so recheck before and after a run.

## What counts as a win

Success means the exact value of A005316(59) or A000682(50) (or the first index beyond each live b-file re-fetched immediately before claiming), computed by two runs that agree exactly. The runs must use different moduli sets or exact arithmetic AND a different decomposition or program. The same code must reproduce every published term of the sequence. Terms that follow from published ones by identities do not count (see pitfalls).

## Partial wins

- **p1:** An independent from-scratch reproduction of A005316(56..58) (Khrabrov) or A000682(46..49) (Hogan), by a program not derived from Jensen's, Howroyd's, Khrabrov's or Hogan's code. It must agree exactly with the b-file, with source and logs, using two runs with different moduli.
- **p2:** A new complete row of a published meander refinement table at the first unknown order, two runs agreeing. Examples: A008828 (closed meander systems by number of components, Howroyd's b-file through row 20), or semi-meanders by winding.

## How a win is checked

Skeptic: rerun the claimant's program modulo one fresh 61-bit prime for the claimed n and compare the residue; rerun for all n <= 40 against the b-files; check that a(n)/a(n-2) continues the slowly rising trend of the published ratios (about 10.93 for A005316 at n = 58 and 11.27 for A000682 at n = 49, approaching the limit of about 12.26 from below).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A005316>

## Sources

- <https://oeis.org/A005316>
- <https://oeis.org/A000682>
- <https://oeis.org/A005315>
- <https://oeis.org/A000136>
- <https://oeis.org/A001010>
- <https://oeis.org/A008828>
- <https://firstpair.org/books/arnold-meanders/>
- <https://github.com/querygraph/meander>
- <https://arxiv.org/abs/1302.2025>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A005315 (closed meanders) lags the A005316 b-file. Since A005315(n) = A005316(2n-1), A005315(29) = A005316(57) is already known though not in A005315's b-file. Adding it is bookkeeping, not a win.
- Stamp foldings follow from semi-meanders. A000136(n) = n*A000682(n), A001010(2m) = 2*A000682(m+1), A001010(2m-1) = 2*A007822(m) (A007822 is known to m = 26), and A001011(n) = (A001010(n) + A000136(n))/4. So A000136(46..49) and A001011(46..49) already follow from published terms and are not wins; likewise A077014(56..58) follows from A005316.
- Offsets differ: A005316 starts at 0, A000682 and A000136 at 1.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/meanders-semimeanders-next-terms.md
```

Already set up? Say `run V3R1T4S on meanders-semimeanders-next-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `meanders-semimeanders-next-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
