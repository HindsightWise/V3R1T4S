# Binary codes correcting one adjacent transposition at length 12: first unknown terms of OEIS A057608 and A057657 (Sloane's 1tc/1et graphs)

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (exact maximum independent set on 13 weight components with up to 924 vertices each; checking takes milliseconds) · open as of 2026-10-30

## The problem

A binary code of length n corrects one adjacent transposition when the sets {x, and x with one pair of adjacent unequal bits swapped} of distinct codewords are disjoint. A057657 also allows swapping the end bits ('end-around' transposition). Transpositions preserve weight, so the conflict graph (Sloane's 1tc.2^n and 1et.2^n graphs) splits into n+1 components by Hamming weight. The maximum code size is the sum of the per-weight maxima, given in triangles A085684 (1tc) and A085685 (1et). OEIS A057608 gives 1, 2, 3, 4, 8, 12, 20, 38, 63, 110, 196, 352 for n = 0..11; n = 11 was proved by Brian Borchers in 2009 with SDP branch and bound, after two weeks on the middle components. A057657 gives ..., 100, 171, 316 for n = 9, 10, 11 (Butenko, Pardalos, Sergienko, Shylo and Stetsyuk for the lower bounds; Borchers 2005 and 2009 for optimality, the latter with Gurobi). The weight-2 case without end-around is solved for all n (Gomez Soto, Leanos, Rios-Castro and Rivera 2018, OEIS A085680; 15 at n = 12). The end-around weight-2 component is a different graph (A085685 T(11,2) = 11 against A085684 T(11,2) = 13). Gomez Soto et al. state that A057608 is known only for n <= 11. The OEIS entries (A057608 last edited 2018, A057657 Jan 2026) list no term for n = 12. A checker written for this entry reproduces A057608, A057657 and rows 0-8 of both triangles. At n = 12 the components have C(12,k) vertices: 220, 495, 792 and 924 for k = 3..6.

## What counts as a win

For A057608 (1tc) or A057657 (1et) at n = 12: for every weight k = 0..12, an explicit code of length 12 and weight k plus a certificate that no larger one exists. The certificate is a VeriPB proof log of a maximum-independent-set/clique run verified by VeriPB (preferably CakePB), or an exact-arithmetic ILP certificate (VIPR, checked by viprchk), each for a model rebuilt from the definition. Together these give the exact value a(12), the first unknown term. Components of weight 0, 1, 11 and 12 are trivial. For A057608 the weight-2 and weight-10 components follow from A085680 (15 each). For A057657 the end-around weight-2 and weight-10 components are not covered by A085680 and need their own code and certificate (they are small, 66 vertices).

## Partial wins

- **p1:** The exact value, with an explicit code and a certificate as above, of T(12,k) in A085684 or A085685 for one weight k with 3 <= k <= 9.
- **p2:** The exact value, with code and certificate, of the central component T(12,6) of either triangle: 924 words of weight 6, the hardest component.

## How a win is checked

Rebuild the conflict graph from the definition: two words conflict iff their transposition balls intersect, with the end-around swap of positions 1 and n included only for A057657. Check that the code is an independent set and count it. Run VeriPB/CakePB or viprchk on the certificates. Cross-check the builder by reproducing A085684/A085685 rows for n <= 10 and Sloane's 1tc/1et files for n <= 11. Then re-read the OEIS entries and search for later results.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A057608>

## Sources

- <https://oeis.org/A057608>
- <https://oeis.org/A057657>
- <https://oeis.org/A085684>
- <https://oeis.org/A085685>
- <https://oeis.org/A265032/a265032.html>
- <https://arxiv.org/abs/1711.03682>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Reversal (and complement, which maps weight k to 12-k) are symmetries; break them with orbital branching, and use weight k vs 12-k equality so only k <= 6 needs solving.
- Modern exact clique/MIS solvers with proof logging (Glasgow subgraph solver with VeriPB) are much faster than the 2009 SDP code that needed two weeks for the n = 11 middle components.
- Seed lower bounds with structured constructions (cyclic-shift orbits, run-length classes) and local search, then prove optimality with the exact solver given the incumbent.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Adjacent transposition only: swapping non-adjacent bits, or the deletion metric, gives different graphs. Build the graph from the definition and match it against Sloane's 1tc/1et files for n <= 11.
- A085684's data currently stop at row 10 even though a(11) = 352 is known; row 11 per weight is on Sloane's page (1,4,13,32,55,71,71,55,32,13,4,1). Re-deriving it is not new.
- A solver log is not a certificate; each component needs its own checkable bound.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/single-transposition-codes-length-12.md
```

Already set up? Say `run V3R1T4S on single-transposition-codes-length-12`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `single-transposition-codes-length-12`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
