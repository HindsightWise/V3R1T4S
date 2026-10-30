# Quaternary Hermitian self-dual codes: an extremal [32,16,12] code, or a better minimum weight at length 42, 48, 54 or 60

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days for quasi-twisted / four-circulant searches over GF(4); exact minimum weight of a [32,16] GF(4) code takes laptop-minutes · open as of 2026-10-30

## The problem

A Hermitian self-dual code over GF(4) of length n has d <= 2*floor(n/6)+2 (extremal when equal). Harada (arXiv:2401.15265, Jan 2024) notes that the largest minimum weight d(n) is determined only for n <= 30. At length 32 the currently known largest minimum weight is 10, against the extremal value 12. Kalra and Prakash (arXiv:2501.10163, v3 Mar 2026, Theorem 4) prove that no extremal Hermitian self-dual code of length 12m exists. At x = 1, y = i/sqrt(3) the weight enumerator equals c_{2m}(-16/27)^{2m}, which their magic-state argument shows is non-negative, while the extremal enumerator has c_{2m} < 0. This rules out [36,18,14], [48,24,18] and [60,30,22] and recovers the known non-existence at 12 and 24, so d(36) = 12, attained by the known [36,18,12] codes. Araya and Harada (arXiv:2212.01080, DCC 2023, Table 2) give dH4(6m) as 12, 14 or 16 at 42 and 16, 18 or 20 at 54. With Kalra-Prakash the ranges at 48 and 60 shrink to 14 or 16 and to 16, 18 or 20. Araya-Harada state that existence of a near-extremal code (d = 2*floor(n/6)) is unknown at lengths 42 to 60. Harada's 2024 modified four mu-circulant search gives the same lower bounds and the first Hermitian self-dual [56,28,16] codes. Kim and Lee (IEEE Trans. Inf. Theory 59 (2013)) classified extremal codes of lengths 30 and 32 that have an automorphism of odd prime order and showed that an extremal [32,16,12] code has none.

## What counts as a win

Success means a generator matrix over GF(4) = {0,1,w,w^2} of a Hermitian self-dual code with one of the parameters [32,16,12], [42,21, > =14], [48,24,16], [54,27, > =18] or [60,30, > =18]. (1) Rank n/2. (2) G conj(G)^T = 0, where conj squares each entry. (3) The exact minimum weight is verified by two independent implementations and is strictly above the lower bound stated in the sources above. (4) A fresh literature search shows no earlier code with those parameters.

## Partial wins

- **p1:** A quaternary Hermitian self-dual code of length 40, 44, 52 or 56 whose exact minimum weight, verified by two independent implementations, is strictly greater than the largest known value in Table 8 of Harada (arXiv:2401.15265), which is 12 at 40, 12 at 44, 14 at 52 and 16 at 56 (upper bounds 14, 16, 18, 20). It must also beat any code of that length published later.

## How a win is checked

Implement GF(4) arithmetic with exact tables. Check rank and that the Hermitian Gram matrix G conj(G)^T is zero. Compute the minimum weight by full enumeration when 4^(n/2) is small enough, or by a Brouwer-Zimmermann algorithm over GF(4), with a second independent check. For n = 32, enumerating the 4^16 codewords (or one per scalar multiple) takes minutes. For any claimed extremal length-12m code, evaluate its weight enumerator at y^2 = -1/3 first: Kalra-Prakash show it cannot exist.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2401.15265>

## Sources

- <https://arxiv.org/abs/2212.01080>
- <https://arxiv.org/abs/2401.15265>
- <https://arxiv.org/abs/2501.10163>
- <http://yuki.cs.inf.shizuoka.ac.jp/WE/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search beyond the modified four mu-circulant family, which Harada exhausted at 32 without beating 10: try bordered constructions, quasi-twisted codes, or automorphisms of order 2 or 4 (Kim-Lee exclude odd prime orders for an extremal [32,16,12] code).
- Neighbour walks from the known [32,16,10] codes, minimising the number of weight-10 codewords.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Hermitian self-duality uses conjugation (x -> x^2). Euclidean self-dual GF(4) codes are a different family.
- Additive self-dual GF(4) codes (quantum codes) are not linear Hermitian self-dual codes and do not count.
- No extremal Hermitian self-dual code of length 12m exists (Kalra-Prakash, arXiv:2501.10163, Theorem 4): [36,18,14], [48,24,18] and [60,30,22] are impossible, and d(36) = 12 is settled.
- Kim-Lee (2013): an extremal [32,16,12] code has no automorphism of odd prime order, so searches built on an order-3, 5, 7, ... automorphism at length 32 cannot succeed.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/quaternary-hermitian-self-dual-largest-min-weight.md
```

Already set up? Say `run V3R1T4S on quaternary-hermitian-self-dual-largest-min-weight`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `quaternary-hermitian-self-dual-largest-min-weight`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
