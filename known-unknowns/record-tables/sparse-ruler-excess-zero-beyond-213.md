# Sparse rulers (minimal difference bases): fewer marks than Pegg's best-known table at some length n >= 245

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for constructive search at a given length; exhaustive minimality proofs (partial wins) need cluster · open as of 2026-10-30

## The problem

A sparse ruler of length n is a set of integer marks 0 = m_0 < ... < m_{k-1} = n whose pairwise differences cover 1..n. A046693(n) is the fewest marks. Erdős problem #170 asks for lim A046693(n)/sqrt(n). Erdős-Gál showed the limit exists, and it lies in [1.56, sqrt(3)] (Leech 1956; Wichmann 1963). Exact values are verified for n <= 213 (Arch D. Robison 2014; A046693 b-file 0..213 by Ed Pegg Jr). The maximal lengths A004137(25) = 213 (Robison with Peter Luschny) and A004137(26) = 232 (Fabian Schwartau, Yannic Schröder, Lars Wolf, Joerg Schoebel, 2021) are proven. A004137(27) is unknown; Wichmann gives 251. The Schwartau et al. IEEE DataPort files (login required, not checked here) reportedly give the length/mark-count combinations up to length 244, so lengths 214..244 are left out. Write E(n) = marks - round(sqrt(3n + 9/4)) for the excess (A326499). Ed Pegg Jr's table (A326499 a-file a326499_2.txt, n = 1..10501; E <= 1 proved by Pegg, 2019) lists best-known rulers. 4,890 of the lengths 214..10501 have E = 1 (re-counted 2026-10-30). The entry says terms over n = 213 are unverified minimal; for example, n = 474 has E = 1, but an E = 0 ruler may exist. The smallest in-scope lengths listed with E = 1 are 245..249 (28 marks listed; 27 would be E = 0), then 262..268 and 282..287. Luschny's conjecture says the length-58 ruler 1^3 24^1 5^1 4^5 3^2 is the last non-Wichmann optimal ruler. It would imply many E = 1 entries are optimal, but it is unproven. Target: a ruler with fewer marks than the table at some n >= 245.

## What counts as a win

Success means, for some n >= 245, an explicit list of k integer marks 0 = m_0 < ... < m_{k-1} = n whose pairwise differences cover every integer 1..n, checked exhaustively by two programs. k must be STRICTLY SMALLER (direction: min) than the best-known mark count for n at verification time. That count is the minimum over Pegg's table https://oeis.org/A326499/a326499_2.txt, the A046693, A326499 and A308766 entries, Pegg's Wolfram Community 'Sparse ruler data' post, Luschny's ruler pages, and any newer paper or table found by a fresh search, all re-fetched live. Lengths 214..244 do not count. A count that contradicts the proven A004137 values (k <= 26 for any n >= 233) means a bug, not a win.

## Partial wins

- **p1:** A certified exact minimal mark count for some n in 245..249, currently listed with 28 marks (E = 1). This needs an independently re-runnable exhaustive search, with logs, proving that no 27-mark sparse ruler of that length exists, provided no live source already settles it.
- **p2:** A certified value of A004137(27), the maximum length of a 27-mark complete ruler. Either an exhaustive, independently re-runnable search proving that no 27-mark ruler of length 252 or more exists (confirming the Wichmann value 251), or an explicit 27-mark ruler of length >= 252 checked by two programs.

## How a win is checked

Compute all k(k-1)/2 differences into a boolean array of size n+1 and check that every 1..n appears; confirm 0 and n are marks and k is as claimed; two independent implementations. Recompute round(sqrt(3n+9/4)) exactly in integer arithmetic. For partial wins, rerun the exhaustive search independently and calibrate it by reproducing A004137(24) = 198 and A004137(25) = 213 or Robison's counts.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A326499>

## Sources

- <https://oeis.org/A046693>
- <https://oeis.org/A326499>
- <https://oeis.org/A326499/a326499_2.txt>
- <https://oeis.org/A004137>
- <https://oeis.org/A308766>
- <https://doi.org/10.1109/OJAP.2020.3043541>
- <https://dx.doi.org/10.21227/cd4b-nb07>
- <http://www.luschny.de/math/rulers/optimalconjecture.html>
- <https://community.wolfram.com/groups/-/m/t/2663076>
- <https://www.erdosproblems.com/170>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Non-Wichmann families: search over 'gap-word' templates 1^a x^b y^c z^d ... with more blocks than Wichmann's six, solving for block lengths by integer programming and then checking coverage exactly.
- Local repair: take an excess-1 ruler, delete one mark, and use a SAT model (marks as booleans, each difference covered by at least one pair) restricted to a window to recover full coverage.
- Target lengths where Pegg's table switches between excess 0 and 1 inside one batch of A289761; boundary lengths are the most plausible to drop.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Excess is defined with round(sqrt(3n + 9/4)), and Pegg's table rounds half to even (Mathematica Round). That differs from round-half-up at the 29 lengths n = 6, 36, 90, 168, 270, ... where sqrt(3n + 9/4) is a half-integer. Compare mark counts, not excess, using exact integer arithmetic.
- Pegg's table notation lists gap multiplicities (e.g., 1^4 4^1 8^5 ...). Expand to marks before comparing, and check the expanded ruler.
- Lengths 214..244 are out of scope because Schwartau et al.'s login-gated data reportedly cover them. 214, 215 and 233 are provably E = 1 in any case, from A004137(25) = 213 and A004137(26) = 232.
- Golomb rulers (distinct differences) are a different problem and are held separately; this target is about covering every difference.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/sparse-ruler-excess-zero-beyond-213.md
```

Already set up? Say `run V3R1T4S on sparse-ruler-excess-zero-beyond-213`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sparse-ruler-excess-zero-beyond-213`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
