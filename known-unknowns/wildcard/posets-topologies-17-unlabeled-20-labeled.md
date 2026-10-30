# MOONSHOT - Posets and topologies: unlabeled counts on 17 points (A000112, A001930) or labeled counts on 20 points (A001035, A000798)

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (Ayala's P(19) swept all 6.8e13 posets on 15 points; P(20) or unlabeled 17-point counts need a sweep over the 4.5e15 posets on 16 points or an equivalent shortcut) · open as of 2026-10-30

## The problem

Unlabeled posets (A000112) and unlabeled topologies or quasi-orders (A001930) have been known to n = 16 since Gunnar Brinkmann and Brendan McKay (Order 19 (2002) 147-179): there are 4,483,130,665,195,087 posets on 16 points. The labeled counts moved in 2026. Rafael Ayala (arXiv 2606.31526, 30 Jun 2026; code at github.com/Rafael-Ayala/posets-and-topologies-19) obtained P(19) = A001035(19) = 646099441937791106493755218560442089979 and, by the Stirling transform, A000798(19). He used the Erne-Stege moment reduction: the 16-point moment G(16,3) was harvested by inserting one element into each of the 68,275,077,901,156 unlabeled 15-point posets. He also reported G(16,4), an input for P(20). The b-files, re-fetched 2026-10-30, stop at n = 16 for the unlabeled sequences and n = 19 for the labeled ones.

## What counts as a win

Success means the exact value of A000112(17), A001930(17), A001035(20) or A000798(20), re-fetched live and still missing immediately before claiming. Two independent methods or codes must agree exactly. The pipeline must reproduce all published terms, and for the moment route also Ayala's G(16,k) values. Per-shard residues modulo several primes must be published so a skeptic can recompute random shards. A literature search must find no earlier value.

## Partial wins

- **p1:** An independent confirmation of A001035(19) (Ayala 2026, a single computation), using a different code and either a different route (for example direct counting over 16-point posets) or an independently written moment kernel, agreeing on G(16,3) and P(19).

## How a win is checked

Rerun the shard pipeline on a random sample of shards with independent code and compare the residues. Check the CRT reconstruction and the Erne-Stege assembly. Check the modular periodicity of A001035 as a sanity test.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A001035/b001035.txt>

## Sources

- <https://oeis.org/A000112>
- <https://oeis.org/A001930>
- <https://oeis.org/A001035>
- <https://oeis.org/A000798>
- <https://arxiv.org/abs/2606.31526>
- <https://github.com/Rafael-Ayala/posets-and-topologies-19>
- <https://users.cecs.anu.edu.au/~bdm/papers/posets.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- P(20) needs only one new 17-point moment, which can be harvested from the 16-point posets by one-point insertion; the work splits naturally into shards.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Labeled vs unlabeled, and posets (T0) vs quasi-orders (all topologies): four different sequences.
- Moments must be accumulated modulo several primes; 128-bit sums overflow at these sizes.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/posets-topologies-17-unlabeled-20-labeled.md
```

Already set up? Say `run V3R1T4S on posets-topologies-17-unlabeled-20-labeled`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `posets-topologies-17-unlabeled-20-labeled`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
