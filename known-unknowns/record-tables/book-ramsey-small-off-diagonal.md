# Book Ramsey numbers off the n-1,n diagonal: close a gap in DS1 Table IXa (R(B4,B7) 22-23, R(B4,B9) 27-28, R(B5,B9) 28-30, R(B7,B11) 37-38) or a lower-only cell of Table VII (books versus cycles)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (2-block polycirculant SAT/IP on 22-45 vertices); upper bounds via flag algebras · open as of 2026-10-30

## The problem

B_n = K_2 + nK_1 is the book of n triangles on a common edge. DS1 revision #18 (Apr 2026) Table IXa lists R(B_m,B_n) for m <= 10, n <= 11. After the 2026 papers, the open cells with printed bounds are: - R(B4,B7) 22-23 (lower bound by monotonicity from R(B4,B6) = 22) - R(B4,B9) 27-28 (lower bound from srg(26,10,3,4) via item 5.3.l, upper bound from Rousseau-Sheehan, item 5.3.k) - R(B5,B9) 28-30 (lower bound Van Overberghe, upper bound from item 5.3.k) - R(B7,B11) 37-38 Blank cells of the table (for example R(B4,B8), R(B4,B10), R(B5,B8), R(B5,B10), R(B6,B9)) are open too, with bounds implied by monotonicity (item 5.3.a) and items 5.3.k/l, for example 27 <= R(B4,B10) <= 30 and 28 <= R(B5,B10) <= 32. The cells R(B5,B7) = 25, R(B7,B9) = 33 and R(B8,B10) = 37, still lower-only in DS1, are settled by Dai-Lin's R(B_{n-2},B_n) <= 4n-3 for n >= 3, n != 6 (arXiv:2606.07214) and Kalfus-Lidicky (arXiv:2606.05629). Together with DS1 5.3.j this settles R(B_{n-2},B_n) = 4n-3 for all n <= 21 except n = 6, where R(B4,B6) = 22. The diagonal is closed for n <= 21: srg(65,32,15,16) (Gritsenko 2021) and srg(85,42,20,21) (Verma, arXiv:2610.08893) give R(B16,B16) = 66 and R(B21,B21) = 86. Table VII (books versus cycles) has lower-only cells R(B8,C9) >= 23, R(B9,C9) >= 25, R(B9,C10) >= 26, R(B10,C10) >= 28. This target excludes the nearly diagonal numbers R(B_{n-1},B_n), a live Epoch AI FrontierMath problem. Credit: Rousseau-Sheehan, Wesley, Van Overberghe, Lidicky-Pfender, Lidicky-McKinley-Pfender-Van Overberghe, Shao-Xu-Bao-Pan, Dai-Lin, Kalfus-Lidicky.

## What counts as a win

Either (a) an explicit graph G on N vertices with no B_m and whose complement has no B_n (or no C_k for Table VII cells), verified by two independent programs, with N+1 STRICTLY GREATER (direction: max) than the best lower bound for that cell in the live DS1, Wesley (arXiv:2410.03625), Dai-Lin (arXiv:2606.07214), Chung-Wesley (arXiv:2610.36522) and any newer paper; or (b) an upper bound STRICTLY BELOW (direction: min) the best published upper bound for that cell, certified by an exact-rational flag-algebra certificate or a DRAT/LRAT UNSAT proof with a checkable reduction. Published bounds include those implied by DS1 5.3.a (monotonicity), 5.3.k and 5.3.l (strongly regular graphs) and by Dai-Lin's R(B_{n-2},B_n) <= 4n-3. Cells of the form R(B_{n-1},B_n) do not count here, nor do settled cells (R(B_{n-2},B_n) for n <= 21, including R(B5,B7), R(B7,B9) and R(B8,B10); R(B_n,B_n) for n <= 21). Off-by-one: a graph on N vertices proves R >= N+1.

## Partial wins

- **p1:** Settle a lower-only cell of Table VII (R(B8,C9), R(B9,C9), R(B9,C10) or R(B10,C10)): either a certified proof (as in (b)) that the listed lower bound is the exact value, e.g. R(B9,C9) <= 25, or a verified graph raising its lower bound.
- **p2:** A new exact value R(B_{n-2},B_n) = 4n-3 for some n >= 22 not covered by Wesley (arXiv:2410.03625), Dai-Lin (arXiv:2606.07214) or any newer paper: an explicit verified graph on 4n-4 vertices with no B_{n-2} and no B_n in its complement (the matching upper bound is Dai-Lin's theorem).

## How a win is checked

B_n-freeness: for every edge uv of G count common neighbours and require fewer than n; for the complement do the same over non-edges with common non-neighbours. Implement twice (matrix product A^2 restricted to edges, and explicit set intersection). For C_k use an exact cycle search cross-checked by SAT. Certificates via drat-trim/cake_lpr or an exact SDP checker.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>

## Sources

- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://arxiv.org/abs/2407.07285>
- <https://arxiv.org/abs/2410.03625>
- <https://arxiv.org/abs/2606.07214>
- <https://arxiv.org/abs/2606.05629>
- <https://arxiv.org/abs/2610.08893>
- <https://arxiv.org/abs/2102.05432>
- <https://github.com/Steven-VO/circulant-Ramsey>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- R(B_{n-1},B_n) = 4n-1 (smallest open n = 64, Chung-Wesley arXiv:2610.36522) is a live Epoch AI problem with its own verifier; it is held, not part of this target.
- DS1 (Apr 2026) still shows R(B5,B7) >= 25, R(B7,B9) >= 33, R(B8,B10) >= 37 and 4n+1 <= R(B_n,B_n) <= 4n+2 for n <= 21. All of these are settled (Dai-Lin, Kalfus-Lidicky, and the srgs of Gritsenko and Verma).
- Lower bounds from strongly regular graphs: an srg(v,k,lambda,mu) avoids B_{lambda+1} and its complement avoids B_{v-2k+mu-1}. Check Brouwer's table before claiming a 'new' construction.
- Text extraction of DS1 Table IXa misplaces columns: the '27-28' and ' > = 28' entries sit in column n = 9 (R(B4,B9), R(B5,B9)), not n = 10. Read the rendered PDF.
- For p2: Dai-Lin's lemma gives R(B_{n-2},B_n) = 4n-3 whenever a symmetric Hadamard matrix of order 2n-2 with constant diagonal exists (the order must be 4u^2, so n = 2u^2+1). Any n for which such a matrix is already in the literature counts as covered.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/book-ramsey-small-off-diagonal.md
```

Already set up? Say `run V3R1T4S on book-ramsey-small-off-diagonal`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `book-ramsey-small-off-diagonal`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
