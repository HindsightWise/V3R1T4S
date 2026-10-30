# Restricted additive 2-bases (restricted postage stamp, A006638): beat the Challis-Robinson symmetric-basis ranges for 48 <= k <= 82, or settle a(48)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-days for preamble searches (s = 27, 28) and constructions; an exhaustive a(48) needs cluster (about 4,000 CPU-hours extrapolated from Kohonen's 812 h at k = 47) · open as of 2026-10-30

## The problem

An additive 2-basis A = {0 = a_0 < a_1 < ... < a_k} has range n_2(A), the largest n with {0..n} in A+A. It is restricted if n_2(A) = 2a_k. OEIS A006638 gives the largest range of a restricted basis with k positive elements. Jukka Kohonen determined it exactly for k <= 41 (J. Integer Seq. 17, 2014) and k <= 47 (arXiv:1503.03416, 2015). For k = 42..47 the values are 588, 614, 644, 674, 704 and 734; the k = 47 prefix search took 812 CPU-hours. All extremal bases there are symmetric and are exactly those of the preamble-amble construction of Michael F. Challis and John P. Robinson (J. Integer Seq. 13 (2010) 10.2.3, corrected Tables 2 and 3). Their Table 3 gives the best symmetric ranges as piecewise-linear formulas: 30k-676 for 43 <= k <= 52 (764 at k = 48), 32k-780 (52-56), 34k-892 (56-58), 38k-1124 (58-62), 40k-1248 (62-67), 44k-1516 (67-80), 48k-1836 (80-82), and an open-ended 52k-2164 from k = 82. They come from the most efficient preambles PA(s, a_s), known up to s = 26. No exact value is known for k >= 48 (A006638 b-file 1..47). The formulas are linear, while quadratic constructions in the literature (e.g., Mrose 1979, about (2/7)k^2) overtake them for k beyond roughly 100. This target is therefore limited to 48 <= k <= 82, where Table 3 is the best published range found. It differs from the unrestricted postage-stamp numbers n(2,k) (A001212). Target: a restricted basis beating the best published range for some 48 <= k <= 82.

## What counts as a win

Success means, for some k with 48 <= k <= 82, an explicit set A = {0 < a_1 < ... < a_k} of integers with {0..2a_k} in A+A, checked by two programs. That is, every integer 0..2a_k is a sum of two not necessarily distinct elements of A. Its range 2a_k must be STRICTLY GREATER (direction: max) than the best published restricted (or symmetric) range for that k, all checked live. The sources are the Challis-Robinson Table 3 formula value, OEIS A006638 and its links, Mossige's symmetric-basis results, any explicit construction in the literature (e.g., Mrose-type) evaluated at that k, and a fresh literature search. If the unrestricted range exceeds 2a_k, report it, but the restricted condition must hold as defined.

## Partial wins

- **p1:** A certified exact value of A006638(48): an independently re-runnable exhaustive search (Kohonen-style prefix and suffix enumeration, or a checked UNSAT certificate) proving that no restricted basis with k = 48 has range above some R, together with a basis of range R (expected R = 764).
- **p2:** An exhaustive determination of the most efficient preamble PA(s, a_s) for s = 27 or s = 28 in the Challis-Robinson sense (extending their Table 2), with the search independently re-runnable, and the resulting linear range formula for the derived symmetric bases stated and checked on at least one explicit basis.

## How a win is checked

Compute A+A with a bitset of size 2a_k+1 and check coverage of 0..2a_k, in two independent implementations; also report the full range n_2(A). Compare 2a_k with the Table 3 formula for that k (calibrate by reproducing 734 at k = 47 from Kohonen's listed bases and 588 at k = 42). For p1, rerun the exhaustive search on the verifier's side, and calibrate by reproducing A006638(41..47).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A006638>

## Sources

- <https://oeis.org/A006638>
- <https://arxiv.org/abs/1503.03416>
- <https://cs.uwaterloo.ca/journals/JIS/VOL17/Kohonen2/kohonen5.html>
- <https://cs.uwaterloo.ca/journals/JIS/VOL13/Challis/challis6.html>
- <https://cs.uwaterloo.ca/journals/JIS/VOL13/Challis/challis6.pdf>
- <https://oeis.org/A001212>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Table 3 keeps only the best formula from the most efficient preamble for each s. Near the row crossovers (k = 52, 56, 58, 62, 67, 80), try other preambles, near-optimal PAs, or two-period ambles; one of them may beat the tabulated line at a single k.
- Try non-symmetric restricted bases built from a symmetric skeleton with a modified middle 'amble' (period-changing ambles), searched by SAT over the middle segment.
- Kohonen's element-wise lower bounds depend on the exact unrestricted values A001212 (known to k = 24); better bounds there speed up the exhaustive p1 search.
- For p2, extend Challis's look-up-table preamble search to s = 27 or 28 and check whether the derived linear formula beats Table 3 anywhere in 48..82.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Restricted means range exactly 2a_k. A basis with larger unrestricted range but 2a_k smaller is not a restricted record.
- Off-by-one in k: k counts the positive elements (A006638(1) = 2 with A = {0,1}).
- Challis-Robinson Table 2 originally had errors for s = 16 and s = 24 (non-symmetricizable preambles), corrected in the 2010 paper; use the corrected tables.
- The unrestricted numbers n(2,k) (A001212, exact only to k = 24; Friedman's Math Magic postage-stamp page 0403 shows k = 25 as '?') belong to the bank entry friedman-mathmagic-archive-records; do not claim them here.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/restricted-additive-2-bases-k48.md
```

Already set up? Say `run V3R1T4S on restricted-additive-2-bases-k48`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `restricted-additive-2-bases-k48`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
