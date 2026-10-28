# Spencer discrepancy constant C_10c: an n x n matrix in [-1,1] whose discrepancy beats the record ratio disc(A)/sqrt(n)

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Tao's optimization-constants repository, constant 10c: C_10c is the least K with disc(A) <= K sqrt(n) for every n and every A in [-1,1]^{n x n}, where disc(A) = min over x in {+-1}^n of ||Ax||_inf (Spencer's 'six standard deviations suffice'). Upper bounds: 5.32 (Spencer 1985), 4.1 algorithmic (Pesenti-Vladu, corrected v2). Lower bounds are explicit small matrices with an exhaustively checked discrepancy: 4/sqrt(6), 5/3, 7/sqrt(17), and the current record 5/sqrt(8) ~ 1.767767 (an 8 x 8 matrix over {-1,0,1} built from the perfect [7,4] Hamming code, submitted to the repository on 5 Sep 2026; the page proves 5 is optimal at n = 8). Target: any explicit square matrix with entries in [-1,1] (rational entries allowed, not only signs) whose exact discrepancy divided by sqrt(n) strictly exceeds the live record.

## What counts as a win

Success means an explicit n x n matrix A with rational entries in [-1,1] (n arbitrary), saved as a file, such that the exact discrepancy d = min over all 2^n sign vectors x of max_i |(Ax)_i|, computed by exhaustive enumeration in exact rational arithmetic by two independent programs, satisfies d / sqrt(n) STRICTLY GREATER (direction: max) than the largest lower bound listed on the live page https://teorth.github.io/optimizationproblems/constants/10c.html and in any open pull request touching constants/10c.md at https://github.com/teorth/optimizationproblems/pulls, both re-fetched live immediately before claiming; the comparison d^2 / n > (record)^2 is done exactly. A rectangular or padded matrix counts only after it is made square without lowering d (duplicate rows or zero columns are allowed, as on the page).

## Partial wins

- **p1:** A sign matrix (entries exactly +-1) whose discrepancy ratio strictly beats the best sign-matrix entry on the live page (7/sqrt(17) as of 2026-10-28), showing that zeros/real entries are not needed to pass it.
- **p2:** For some specific n in 9..40, an n x n matrix with entries in [-1,1] whose exact discrepancy d satisfies d/sqrt(n) strictly greater than the best value obtainable at that same n from Keri's covering-code table by the page's reduction C_10c >= (n-2r)/sqrt(max(n,P)) (the claim computes and states that per-n value from the table), with exhaustive two-implementation verification; this is a per-size improvement, not a record unless it also beats the main bar.

## How a win is checked

Load the matrix as exact rationals; enumerate all 2^n sign vectors (Gray-code order, incremental update of Ax, exact integers after clearing denominators) and record min ||Ax||_inf; a second implementation in a different language (or a covering-radius check when the matrix is a sign matrix) must agree. Compare d^2*8 > 25*n style integer inequality against the live record. n up to about 40 runs in minutes on a laptop with bit-parallel code.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/10c.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/10c.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/10c.md>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/README.md>
- <https://github.com/teorth/optimizationproblems/pulls>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Leave the covering-code world: the page's reduction only covers sign rows. Real-valued rows can carve the cube into regions that no Hamming ball shape allows. Run local search on A in [-1,1]^{n x n} with the exact discrepancy as the objective for n = 9..24, using an LP inside the loop: fix the set of x that each row is responsible for and maximise the margin by linear programming over the row entries.
- Cross-domain import (coding theory, covering codes with weights): the n=8 record is the perfect Hamming code. Try weighted or nonbinary covering objects (ternary Golay, perfect codes over mixed alphabets) and translate them into rows with entries in {-1,-1/2,0,1/2,1}.
- Cross-domain import (adversarial ML / robust optimisation): treat x as the adversary and A as the defender; alternate a max-min game (best-response x by branch-and-bound, then a gradient or LP step on A against the current active set of worst x), which is how certified-robust training finds hard instances.
- Cross-domain import (SAT/MaxSAT): for a fixed sign pattern support and target discrepancy d, encode 'every x has some row with |<a_i,x>| >= d' as a covering problem and hand it to a MaxSAT or ILP solver; zero entries become 'don't care' literals.
- Kronecker and direct-sum constructions: check whether tensoring the 8 x 8 record with small matrices (or block-diagonal mixtures) keeps the ratio, and search for gluings that gain.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point discrepancy: a matrix with irrational or float entries can show a spurious ratio from rounding; only exact rationals and exhaustive enumeration count.
- Non-square matrices: more rows than columns trivially raise the discrepancy; the definition is n x n. Padding with duplicate rows is allowed only while rows <= columns are made square as on the page.
- Sampling x instead of enumerating all 2^n sign vectors overestimates the discrepancy.
- Comparing against a stale record: the page and its open pull requests move weekly; compare against the maximum live value, not the number in this entry.
- Entries outside [-1,1] (for example 1.0000001 after scaling) void the claim.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/spencer-discrepancy-c10c-lower-bound.md
```

Already set up? Say `run V3R1T4S on spencer-discrepancy-c10c-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `spencer-discrepancy-c10c-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
