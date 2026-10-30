# Conway's subprime Fibonacci sequences: a seventh non-trivial cycle, or an exhaustive check of starting pairs beyond 10^6

🔢 **Number hunts** · standard · tractability ★★☆☆☆ · compute: laptop-days (about 2.4*10^12 coprime starting pairs for N = 2*10^6, with memoised node tables); a new cycle verifies in milliseconds · open as of 2026-10-30

## The problem

John Conway's subprime Fibonacci rule: from a pair (x, y) of positive integers, the next term is s = x + y if s is prime, and otherwise s divided by its least prime factor. Richard K. Guy, Tanya Khovanova and Julian Salazar ('Conway's subprime Fibonacci sequences', arXiv:1207.5099, v2 2014) studied these orbits, which behave pseudo-randomly, much like 3x+1 trajectories. A start (a, a) gives the trivial cycle a, a, a, .... Coprime pairs stay coprime, so their sequences are non-trivial, and every non-trivial sequence eventually has coprime consecutive terms. Six non-trivial cycles are known: lengths 10, 11, 18, 19, 56 and 136, through the nodes (127, 509), (37, 199), (48, 13), (23, 27), (119, 109) and (47, 23), with largest terms 827, 607, 97, 191, 5693 and 347. The paper checked every starting pair with both terms at most 10^6 and found no other non-trivial cycle. It conjectures that no orbit grows without bound. Conway's sequence from (1, 1), A214674, enters the 18-cycle at (48, 13). OEIS A214897 and A214898 (Wouter Meeussen) list the lengths 1, 10, 11, 18, 19, 56, 136 (the 1 is a trivial cycle) and largest elements. Their comment still says 'checked to [10^5, 10^5]', and A214898 gives 239 for the 18-cycle, but 239 lies on A214674's pre-period and the cycle's largest term is 97 (rechecked with an independent program that reproduces the paper's Table 1). Tables A282812-A282814 give per-start data for small pairs.

## What counts as a win

CONFIRMED (full win) for a coprime starting pair (x, y) of positive integers and an explicit non-trivial cycle: a cyclic list of terms t_1..t_L with consecutive terms coprime, such that the rule maps each pair (t_i, t_{i+1}) to (t_{i+1}, t_{i+2}), with indices taken mod L. Every step must be checked with exact arithmetic and proven primality. The cycle's set of terms must differ from each of the six known non-trivial cycles, those generated from the nodes (127, 509), (37, 199), (48, 13), (23, 27), (119, 109) and (47, 23), and the orbit of (x, y) must be shown to reach it. Trivial cycles a, a, a, ... never count. Re-fetch https://oeis.org/A214897 and the arXiv paper before the claim. Direction: max on the number of known non-trivial cycles.

## Partial wins

- **p1:** An exhaustive certificate that every coprime starting pair in [1, N] x [1, N] with N >= 2*10^6 (beyond the 10^6 of Guy, Khovanova and Salazar) enters one of the six known non-trivial cycles. It must give per-cycle counts, which a second, independently written program reproduces exactly, along with the longest pre-period and the largest term seen.

## How a win is checked

Iterate the rule from the given pair with Python integers. Compute least prime factors by trial division or a sieve, and check primality with a deterministic Miller-Rabin test below 3.3*10^24 (or with ECPP). Confirm that the cycle closes, that it is not trivial, and that its term set differs from the six known cycles, regenerated from their nodes. First reproduce the paper's Table 1 for a, b <= 10^3 (cycle lengths 1/10/11/18/19/56/136 with counts 10022/33/390/467014/30490/21990/470061) and A214674 entering the 18-cycle at (48, 13). For p1, rerun both programs and diff the per-cycle counts.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A214897>

## Sources

- <https://arxiv.org/abs/1207.5099>
- <https://oeis.org/A214897>
- <https://oeis.org/A214898>
- <https://oeis.org/A214674>
- <https://oeis.org/A282814>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Memoise orbit outcomes over visited pairs (a hash or Bloom set of pairs known to reach each loop) so that a new start stops as soon as it hits a known pair.
- Look for loops directly rather than from starts: search cycles of the pair map over pairs with a large prime term, since every known loop's largest element is prime.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Trivial cycles: any start (a, a) loops on a forever, and non-coprime starts can end in such cycles. They are not new cycles.
- A rotation of a known cycle, or the same cycle entered from another pair, is not new. Compare term sets with the six cycles regenerated from their nodes, not with A214898's maxima (its 18-cycle entry, 239, is wrong; the maximum is 97).
- Primality errors (Fermat-only tests) can create fake cycles; use deterministic tests.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/conway-subprime-fibonacci-new-loop.md
```

Already set up? Say `run V3R1T4S on conway-subprime-fibonacci-new-loop`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `conway-subprime-fibonacci-new-loop`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
