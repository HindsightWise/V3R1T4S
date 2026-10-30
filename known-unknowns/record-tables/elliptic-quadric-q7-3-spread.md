# Spread of the elliptic quadric Q^-(7,3): 82 generator planes partitioning its 1066 points, or a rerunnable nonexistence proof

📊 **Record tables** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days to needs cluster (exact cover with 22960 candidate planes over 1066 points; verification instant) · open as of 2026-10-30

## The problem

A spread of a polar space is a set of generators (maximal totally singular subspaces) partitioning its points. Spreads of Q^-(2n+1,q) exist for n <= 2 and, for q even, for all n. For q odd and n >= 3 their existence is a long-standing open question, stated as open by Kiermaier, Schmidt and Wassermann in 'Designs in finite classical polar spaces' (DCC 2025; arXiv:2403.11188v3, Oct 2025, citing Sec. 7.5 of their ref. [17]). In their notation these are 1-(r,r,1) designs in Omega^-(2r+2,q). The smallest open case is Q^-(7,3) = Omega^-(8,3), of rank 3. It has 13 * 82 = 1066 points and (3^2+1)(3^3+1)(3^4+1) = 22960 generator planes, each with 13 points. A spread consists of 82 planes. By computer search they showed that the order of the automorphism group of any spread of Omega^-(8,3) can only have prime divisors 2 and 3.

## What counts as a win

Either (a) existence: using the quadratic form Q(x) = x1x2 + x3x4 + x5x6 + x7^2 + x8^2 over GF(3), whose x7^2 + x8^2 part is anisotropic so the form is elliptic, give 82 planes as 3 x 8 basis matrices over GF(3). Each must have rank 3 and be totally singular, and together they must cover each of the 1066 singular points exactly once. Or (b) nonexistence: an exhaustive search for spreads of this quadric whose code the skeptic reruns to the same conclusion, with every symmetry-breaking step justified, or a checkable DRAT/LRAT certificate for a published CNF encoding. Either settles a problem open on 2026-10-30 (direction: settle).

## Partial wins

- **p1:** A rerunnable computer proof that no spread of Q^-(7,3) admits an automorphism of order 2 (or of order 3), extending the restriction in Kiermaier-Schmidt-Wassermann that only the primes 2 and 3 can divide the order of an automorphism. The skeptic reruns the code.

## How a win is checked

Enumerate GF(3)^8, find the singular points (expect 1066) and normalise them. For each given plane, check rank 3, that Q vanishes on the basis vectors and that the polar bilinear form vanishes on all basis pairs. List its 13 points and confirm that the union over 82 planes is all 1066 points with no repeats. For (b), rerun the supplied solver on the published encoding and check the certificate with drat-trim or cake_lpr.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2403.11188>

## Sources

- <https://arxiv.org/abs/2403.11188>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Prescribe a group with order divisible only by 2 and 3, as the paper's restriction allows, and solve the orbit exact-cover with an ILP or DLX.
- Exact cover with symmetry breaking: fix a first plane and use the stabiliser in PGO^-(8,3) to canonicalise later choices (orderly generation).
- Use the relation with ovoids and spreads of related polar spaces (field reduction, triality-free reductions) to obtain extra structural constraints.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Q^-(7,3) generators are planes (projective dimension 2), not solids.
- With a different form, prove it is elliptic. A hyperbolic Q^+(7,3) has spreads by other theory and does not count.
- An exhaustive nonexistence claim without independently checkable certificate or rerunnable code is not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/elliptic-quadric-q7-3-spread.md
```

Already set up? Say `run V3R1T4S on elliptic-quadric-q7-3-spread`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `elliptic-quadric-q7-3-spread`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
