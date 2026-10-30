# Ways to cut an n x n square into integer squares: the next term a(26) of OEIS A045846, or new terms of the inequivalent count A224239

🎲 **Recreational math** · standard · tractability ★★☆☆☆ · compute: laptop-days for A224239 terms via Burnside; A045846 a(26) is laptop-days to needs cluster · open as of 2026-10-30

## The problem

OEIS A045846 (Erich Friedman) counts the ways to cut an n x n square into integer-sided squares of any sizes. Steve Butler computed terms to n = 20 (see 'Counting tilings by taking walks in a graph', with Ekstrand and Osborne), and Andrew Gozzard and Max Ward's b-file runs to n = 25 (a(25) ~ 5.48e81, 82 digits). The latest edit (2026-10-23) only changed a link, and no a(26) is recorded. The companion A224239 counts dissections up to rotation and reflection. Brendan J. Dee extended its b-file to n = 19 in 2026 (earlier terms Don Reble 2013 and Ed Wynn 2013), so it lags A045846 by six terms. By Burnside's lemma, A224239(n) = (A045846(n) + fixed counts under the seven non-trivial symmetries of the square)/8, and dissections fixed by a symmetry are much cheaper to count. The rectangular table A219924 (Alois P. Heinz, b-file antidiagonals 0..30) counts the k x n versions. This target is distinct from the bank's square-grid-lattice-gas entry, which covers only 1x1 and 2x2 tiles (A063443).

## What counts as a win

Success means the exact integer A045846(26), where 26 is the first index absent from the live DATA and b-file, re-fetched immediately before claiming; if the b-file has grown, the next absent index instead. It must be computed by two independently written programs (e.g. a profile/skyline transfer-matrix DP and a different decomposition or modular-CRT run) that agree exactly and both reproduce every b-file term a(0)..a(25). The value must not appear in the entry's history or pending drafts.

## Partial wins

- **p1:** New terms of A224239 (inequivalent dissections) beyond the live b-file (currently a(19)): at least a(20), obtained from A045846(n) plus independently computed counts of dissections fixed by each symmetry of the square. Two programs must agree and reproduce a(1)..a(19).
- **p2:** A new antidiagonal of A219924 (k x n rectangles tiled by integer squares) beyond Heinz's b-file (antidiagonals 0..30), with two agreeing programs that reproduce the existing antidiagonals.

## How a win is checked

Rerun both programs on a skeptic machine for n <= 20 against the b-file, then check the claimed a(26) modulo one or two fresh primes with a modular version of either program. Check that the Burnside identities hold exactly (integrality of A224239 terms) for p1.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A045846>

## Sources

- <https://oeis.org/A045846>
- <https://oeis.org/A045846/b045846.txt>
- <https://oeis.org/A224239>
- <https://oeis.org/A219924>
- <https://doi.org/10.1007/978-3-030-37853-0_5>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Skyline (profile) DP: the state is the height profile of the partially filled square, and placing the largest square at the lowest-leftmost gap keeps the state space canonical. Memoise with hashing and do the arithmetic modulo several 62-bit primes with CRT.
- For the symmetric counts in p1: a dissection fixed by a reflection is determined by one half plus a compatible diagonal or axis strip. Count with the same DP on the quotient region.
- Meet-in-the-middle across the horizontal midline: count top and bottom halves per boundary profile and pair them.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A045846 counts all dissections, including the trivial n^2 unit squares and the single n x n square (a(1) = 1). Reproduce the small terms first.
- The 'changed' keyword and Dee's 2026 activity on A224239 mean that new terms may already be in a pending draft. Check the history page before claiming.
- CRT with too few primes silently gives a residue. a(26) has about 90 digits, so use enough moduli with a wide margin.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/integer-square-dissections-count-a045846.md
```

Already set up? Say `run V3R1T4S on integer-square-dissections-count-a045846`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `integer-square-dissections-count-a045846`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
