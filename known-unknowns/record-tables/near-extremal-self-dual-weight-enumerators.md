# Near-extremal self-dual codes with new weight enumerators: realize an admissible ternary (lengths 36-72) or quaternary Hermitian (lengths 24-36) enumerator not yet known to exist

📊 **Record tables** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-hours: negacirculant and neighbour searches plus exact counting of minimum-weight codewords · open as of 2026-10-30

## The problem

For a near-extremal ternary self-dual code of length 12m (d = 3m) the weight enumerator depends on the number alpha of minimum-weight codewords. Araya and Harada (arXiv:2212.01080, Des. Codes Cryptogr. 91 (2023) 1813-1843) derived restrictions on admissible alpha for m = 3, 4, 5, 6 (lengths 36, 48, 60, 72) and listed the alpha values known to be realized (their Question 1). They did the same for near-extremal quaternary Hermitian self-dual codes of length 6m, with an explicit Question 2: settle the remaining admissible alpha for m = 4, 5, 6 (lengths 24, 30, 36). Rukavina and Tonchev (J. Combin. Des. 32 (2024) 606-624; Ex. Countex. 5 (2024) 100130) and Pender (Discrete Math. 347 (2024) 113968) added ternary values at lengths 36 and 48. Harada (arXiv:2412.04795v2, 3 Jul 2025; Discrete Math. 349 (2026) 114675) collected those lists, realized many new ternary alpha values at lengths 36, 48 and 60 with a negacirculant construction, and corrected the length-72 list of Araya-Harada Proposition 4.2; his extensive negacirculant search found no near-extremal code of length 72. At length 36 the values still open are alpha = 8 beta with beta in {1..5, 84, 86..89, 92, 94..111}. Harada's 2024 Hermitian paper (arXiv:2401.15265) adds no new near-extremal Hermitian values (its [24,12,8] and [36,18,12] codes have alpha = 513, 594, 837 and 19548, 20844). Weight enumerators and code data are posted at http://yuki.cs.inf.shizuoka.ac.jp/WE/ and https://www.math.is.tohoku.ac.jp/~mharada/F3-9nega/. A 2026-10-30 arXiv search found no later paper. Many admissible values remain unrealized; each new value is a separate cell. A related bank entry asks for larger minimum weights; this one fixes the minimum weight and asks for new enumerators.

## What counts as a win

Success means an explicit ternary self-dual code of length 36, 48, 60 or 72 with minimum weight exactly 3m, or a quaternary Hermitian self-dual code of length 24, 30 or 36 with minimum weight exactly 2m. Its weight enumerator parameter(s), computed exactly, must be admissible by Araya-Harada (2023) and must differ from every value listed as realized in Araya-Harada (2023), Rukavina-Tonchev (2024), Pender (2024), Harada (arXiv:2412.04795v2 = Discrete Math. 349 (2026) 114675) and any later paper found by a fresh search. Equivalent codes count once; each new parameter value counts as one cell.

## Partial wins

- **p1:** A re-runnable non-existence certificate for an admissible weight enumerator listed as open by Araya-Harada (2023) or Harada (2025), for example a classification of all codes with that many minimum-weight codewords under a stated structural restriction proved to be without loss of generality.

## How a win is checked

Check self-duality: G G^T = 0 mod 3 for ternary codes, G conj(G)^T = 0 over GF(4) for Hermitian codes. Compute the exact number of codewords of minimum weight and confirm that no smaller weight occurs, with two independent implementations (for ternary length 60, enumerate weight-15 codewords exactly via information-set splitting). Derive alpha (and beta where the enumerator has two parameters) and compare with the published realized lists.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2412.04795>

## Sources

- <https://arxiv.org/abs/2212.01080>
- <https://arxiv.org/abs/2412.04795>
- <http://yuki.cs.inf.shizuoka.ac.jp/WE/>
- <https://www.math.is.tohoku.ac.jp/~mharada/F3-9nega/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Harada's negacirculant method (arXiv:2412.04795) found new values quickly at lengths 36, 48 and 60, but his extensive search with it found no near-extremal code of length 72. At 72 try other structures (four-negacirculant, bordered double circulant, codes with an automorphism of odd prime order); for Hermitian length 30 try an omega-circulant or negacirculant analogue.
- Neighbour walks: each neighbour step changes alpha by a computable amount, so steer towards unrealized values.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- alpha must lie in the admissible set. Values excluded by Araya-Harada's restrictions cannot be realized.
- The length-72 ternary list in Araya-Harada Proposition 4.2 was corrected by Harada (2025); use the corrected list.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/near-extremal-self-dual-weight-enumerators.md
```

Already set up? Say `run V3R1T4S on near-extremal-self-dual-weight-enumerators`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `near-extremal-self-dual-weight-enumerators`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
