# Van der Waerden numbers: beat a small-parameter lower bound W(r,k) or w(2;k1,k2)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The van der Waerden number W(r,k) is the least N such that every r-colouring of {1..N} contains a monochromatic k-term arithmetic progression. Only seven nontrivial diagonal values are known exactly (W(2,3..6), W(3,3), W(3,4), W(4,3)). For other small cells the best lower bounds come from explicit colourings: Rabung and Lotts (2012, cyclic zippers), Daniel Monroe (arXiv:1603.03301, v7 2022, distributed search over primes up to 9.5e8; the arXiv comment says 'Version as published'), Heule ('Avoiding triples in arithmetic progression', J. Combinatorics 2017; certificates at github.com/marijnheule/vdWaerden) and Herwig-Heule-van Lambalgen-van Maaren (2007). Examples from the Wikipedia table on 2026-10-28: W(2,7) > 3,703; W(2,8) > 11,495; W(3,5) > 2,173; W(4,4) > 1,048; W(5,3) > 170; W(6,3) > 225. Off-diagonal two-colour values w(2;3,k) are exact up to k=20 (k=19 Ahmed-Kullmann-Snevily; w(2;3,20) = 389, conjectured by them and verified by Kouril 2015), w(2;4,k) up to k=9 and w(2;5,k) up to k=7; beyond those only conjectured or lower-bound values exist. Recent work by Fox and Hunter (arXiv:2606.02541, Jun 2026) and Cao (arXiv:2609.31798, Sep 2026) is asymptotic and does not settle small cells. Find an explicit colouring of {1..N} with no monochromatic forbidden progression where N+1 beats the best known lower bound for some small (r,k) or off-diagonal cell.

## What counts as a win

Success means an explicit colouring c:{1..N}->{1..r} (plain text, one colour per integer) with no monochromatic k-term arithmetic progression (or, for an off-diagonal cell w(r;k1,...,kr), no colour-i progression of length k_i), checked exhaustively by two independent programs, where N+1 is STRICTLY GREATER (direction: max) than the best lower bound for that cell at verification time. The best lower bound is the maximum over Monroe's tables (https://arxiv.org/abs/1603.03301, latest version, re-fetched immediately before claiming), the live table at https://en.wikipedia.org/wiki/Van_der_Waerden_number, Rabung-Lotts (E-JC 2012), Heule's certificate repository, and a fresh arXiv/Google Scholar search for that exact cell. Off-by-one: a colouring of {1..N} proves W > N, i.e. W >= N+1. Bounds derived only from product or recursive formulas, without an explicit checked colouring, do not count.

## Partial wins

- **p1:** An explicit 2-colouring of {1..N} with no blue 3-term and no red k-term progression proving w(2;3,k) > N for some k >= 21 (or w(2;4,k) for k >= 10, w(2;5,k) for k >= 8), where N strictly exceeds every lower bound and conjectured value published for that cell (Ahmed-Kullmann-Snevily tables and any newer paper found by a fresh search).
- **p2:** An exact new value: a certified determination of a currently open small off-diagonal number (for example w(2;3,21), w(2;4,10) or w(2;5,8)) via an explicit colouring of {1..N-1} plus an UNSAT proof at N that is checked with drat-trim or an LRAT checker on a laptop.

## How a win is checked

Write two independent checkers: (a) for each difference d and start a, test whether a, a+d, ..., a+(k-1)d all have the same colour (O(N^2/k) per colour); (b) a bitset-based checker that, for each colour class, ANDs shifted bitsets. Both must report zero monochromatic progressions. Confirm the colouring has exactly N entries and uses only r colours. Then re-fetch the Wikipedia table and grep arXiv for the exact cell (e.g. "W(3,5)", "w(3;5)") over the last 24 months before claiming.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1603.03301>

## Sources

- <https://arxiv.org/abs/1603.03301>
- <https://en.wikipedia.org/wiki/Van_der_Waerden_number>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/2363>
- <https://github.com/marijnheule/vdWaerden>
- <https://arxiv.org/abs/2606.02541>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Rabung's method with a twist: colour x by the discrete logarithm of x modulo a prime p, reduced mod r, then repeat the block. Monroe searched primes up to 9.5e8 for the plain version; search instead over composite moduli, two-prime CRT colourings, or Rabung colourings followed by SAT repair of the last few hundred cells.
- Cyclic zippers (Rabung-Lotts) generalised: interleave two or three good cyclic colourings of smaller length and use a SAT solver (CaDiCaL, kissat) to fix the junction cells.
- From coding theory: a k-AP-free colouring is like a code avoiding a fixed pattern on every arithmetic 'line'. Borrow quasi-cyclic and multiplier-group constructions from code tables, i.e. require the colouring to be invariant under x -> g*x mod p for a subgroup g, which shrinks the SAT instance by the subgroup order.
- From statistical physics: run parallel tempering or population annealing with an energy equal to the number of monochromatic progressions, starting from the best published colouring padded by a few cells.
- Incremental SAT: fix a known record colouring on {1..N}, append cells N+1..N+m as free variables plus a free window at the end of the old colouring, and solve with assumptions; slide the window.
- For multicolour cells such as W(5,3) and W(6,3), try colourings that are products or lifts of good colourings modulo small primes, then use local search, since small-k multicolour cells have been searched less than 2-colour ones.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Off-by-one: a valid colouring of {1..N} proves W > N. Claiming W >= N or W > N+1 is a false record.
- Mixing up notations: W(r,k) (colours first) versus W(k;r), and diagonal versus off-diagonal w(2;3,k). Read the table header carefully.
- Checking only progressions with common difference up to some limit, or only progressions starting at 1. The checker must cover every start a >= 1 and every difference d >= 1 with a+(k-1)d <= N.
- Comparing with a stale table: neither Wikipedia (last edited 2026-07-14) nor Monroe's arXiv tables (v7, 2022) is guaranteed current. Do a fresh search for the specific cell.
- Claiming an asymptotic bound (Green, Hunter, Fox-Hunter, Cao) as a small-cell record. Only explicit colourings count here.
- A periodic colouring of length p verified only on one period: progressions that wrap around the period boundary must be checked on the actual interval {1..N}.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/vdw-small-lower-bounds.md
```

Already set up? Say `run V3R1T4S on vdw-small-lower-bounds`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `vdw-small-lower-bounds`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
