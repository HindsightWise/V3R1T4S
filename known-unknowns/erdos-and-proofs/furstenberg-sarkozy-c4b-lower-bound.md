# Furstenberg-Sarkozy exponent C_4b: a larger square-difference-free set exponent

✏️ **Erdős problems and proofs** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Tao's optimization-constants repository, constant 4b: C_4b is the least constant with r(N) <= N^{C_4b+o(1)}, where r(N) is the largest subset of {1..N} with no difference equal to a nonzero perfect square. For forty years the lower bound sat near 0.7334 (Ruzsa 1984; Beigel-Gasarch 2008 / Lewko 2015, base 205). In August-October 2026 it moved fast: Krachun 0.752796 (Paley chains, arXiv:2608.01325), JD Jones 0.753742 and 0.75806770413 (Lean-formalised), Naslund 0.75806746 and then 0.7580758 (exact 473797394875551/625000000000000; interval-moment criterion with new finite witnesses, Hexagon preprint 2610.00151, Lean on Palomar), which is now the page record after pull request #219 was merged on 18 Oct 2026. Naslund notes this is close to the limit of the current approach. The page also records OpenAI's first power-saving upper bound C_4b <= 1 - c (preprint of 24 Sep 2026), with no useful numerical c. As of 2026-10-28 no open pull request touches constants/4b.md. Target: a certified lower bound strictly above the best live value, including open pull requests.

## What counts as a win

Success means a construction (base-expansion components, chains, codes or a new mechanism) with an exact rational exponent alpha and a machine-checkable certificate showing r(N) >= c N^alpha for all large N, such that alpha is STRICTLY GREATER (direction: max) than the largest lower bound listed on the live page https://teorth.github.io/optimizationproblems/constants/4b.html and in any open pull request at https://github.com/teorth/optimizationproblems/pulls touching constants/4b.md, both re-fetched live immediately before claiming. The certificate must be checked in exact arithmetic by an independent verifier written from the criterion's statement (for interval-moment constructions: every modular square edge respects the interval order, every moment inequality holds exactly, and sum of moment powers exceeds alpha), and a brute-force check must confirm that the finite blocks are square-difference-free modulo their bases.

## Partial wins

- **p1:** A strictly better finite component for an existing criterion (for example a longer Paley chain at some prime p = 3 mod 4, or a composite-modulus digraph with larger longest-path ratio) that provably increases that component's moment power, even if the total exponent does not pass the record.

## How a win is checked

Recompute every finite object: for each component (base m, digit set or chain), check all pairwise differences of residues for being nonzero squares mod m (or mod p for each prime factor), check the claimed interval/moment inequalities in exact rationals, and recompute alpha. Optionally build the set for N up to 10^7 and verify no square difference by a sieve over squares. Minutes on a laptop.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://teorth.github.io/optimizationproblems/constants/4b.html>

## Sources

- <https://teorth.github.io/optimizationproblems/constants/4b.html>
- <https://raw.githubusercontent.com/teorth/optimizationproblems/main/constants/4b.md>
- <https://github.com/teorth/optimizationproblems/pull/219>
- <https://arxiv.org/abs/2608.01325>
- <https://arxiv.org/abs/0804.4892>
- <https://github.com/enaslund/sarkozy-lower-bound-0.758>
- <https://github.com/JD-Jones-ASES/nk-lean>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search new components: exhaustive or SAT search for longest Paley-type chains (every forward difference a nonzero square mod p) at primes p = 3 mod 4 beyond 103, and for acyclic square-difference digraphs on square-free composite moduli (the 235 and 299 examples came from such searches).
- Cross-domain import (scheduling / longest-path in DAGs): the interval-moment criterion is an interval-scheduling problem on a digraph; use LP duality to find the optimal widths for a fixed digit set, then local-search the digit set.
- Cross-domain import (coding theory): the composite three-low-digit codes at 215^6 and 437^6 are codes avoiding a 'square difference' metric; search better codes with clique-finding (cliquer / max-clique on the compatibility graph) as for constant-weight code records.
- Re-optimise the binary 25-state recursion: treat its transition weights as a matrix and maximise the spectral radius (growth factor) with exact rational certification, as the 0.75806770413 entry did by reallocation.
- Look for a genuinely new mechanism (e.g. using residues mod p^2 that are non-squares but where higher digits repair the difference) since Naslund reports the current approach is near its limit.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Confusing the finite-N record with the exponent: a large finite set does not prove an exponent; only a construction valid for all N does.
- Squares modulo m vs squares in Z: a block free of square differences mod m may still have differences that are squares in Z when digits carry; the criterion's lifting lemma must actually apply to the new component.
- Ignoring pending pull requests: always check open PRs touching constants/4b.md; beating an older page value (for example 0.75806770413) is not a record once 0.7580758 is listed.
- Floating-point exponents: the record entries are exact rationals; compare exactly, not to 6 decimals.
- Using composite moduli where 'z^2 mod m' squares include zero divisors without checking the lemma's hypotheses (the Jones construction states 'any nonzero z^2 mod m counts as a square').

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/furstenberg-sarkozy-c4b-lower-bound.md
```

Already set up? Say `run V3R1T4S on furstenberg-sarkozy-c4b-lower-bound`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `furstenberg-sarkozy-c4b-lower-bound`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
