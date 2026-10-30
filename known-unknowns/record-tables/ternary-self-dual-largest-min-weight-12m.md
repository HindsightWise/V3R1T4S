# Ternary self-dual codes: raise the largest known minimum weight at length 84, 108 or 120

📊 **Record tables** · standard · tractability ★★☆☆☆ · compute: laptop-days for structured (four-negacirculant, bordered double circulant) searches and for exact minimum weight at length 84; exact verification at lengths 108 and 120 may need cluster unless a large automorphism group is used · open as of 2026-10-30

## The problem

A ternary self-dual code of length n exists iff 4 | n and has d <= 3*floor(n/12)+3 (Mallows-Sloane). Extremal codes cannot exist at n = 72, 96, 120 or any n >= 144, because the extremal weight enumerator has a negative coefficient (see Rains-Sloane). Araya and Harada (arXiv:2212.01080, Des. Codes Cryptogr. 91 (2023) 1813-1843, Table 1) list the current largest minimum weight d3(12m). It is 12, 15, 18 and 18 for m = 3..6 and 24 for m = 8, all settled. The open cells are d3(84) = 21 or 24, d3(108) = 27 or 30 and d3(120) = 24, 27 or 30. At 84 the extended QR code QR84 and the Pless symmetry code P84 give 21. At 108 two near-extremal codes are known. For m >= 7 the only ternary near-extremal self-dual codes Araya-Harada list are QR84, P84, P96 and those two codes of length 108. QR84 and P84 have 2368488 and 1259520 codewords of weight 21. Harada's later note on near-extremal codes of lengths 36, 48 and 60 (arXiv:2412.04795v2, 3 Jul 2025) leaves these values unchanged.

## What counts as a win

Success means a generator matrix over GF(3) of a ternary self-dual code with one of the parameters [84,42,24], [108,54,30], [120,60,27] or [120,60,30]. (1) Rank n/2 over GF(3). (2) G G^T = 0 mod 3. (3) The exact minimum Hamming weight is at least the stated value and strictly above the lower bound in Araya-Harada Table 1, computed exactly by two independent minimum-distance implementations and never by sampling. (4) A fresh search shows no earlier publication of a ternary self-dual code with that length and minimum weight.

## Partial wins

- **p1:** A ternary self-dual [84,42,21] code whose exact number of weight-21 codewords differs from 2368488 (QR84) and 1259520 (P84), which proves it inequivalent to both. A fresh search must show that no such code has been published since Araya-Harada (2023). Rank, G G^T = 0 mod 3 and minimum weight are checked as in the main criterion, and two independent implementations compute the weight-21 count exactly.

## How a win is checked

Check rank and G G^T = 0 with exact mod-3 arithmetic. Compute the minimum weight with a Brouwer-Zimmermann algorithm over GF(3) using several information sets, cross-checked by a second independent implementation, or confirm that the low-weight counts match the coefficients forced by Gleason's theorem for ternary self-dual codes. Then compare against Araya-Harada Table 1 and search arXiv for newer values.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2212.01080>

## Sources

- <https://arxiv.org/abs/2212.01080>
- <https://arxiv.org/abs/2412.04795>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Four-negacirculant and bordered double-negacirculant constructions, which Harada and coauthors classified up to length 60 and which hold most known extremal ternary codes.
- Neighbours of QR84, P84 and the Pless symmetry codes, scored by the exact number of weight-21 codewords.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Lengths 72, 96 and 120 cannot reach the extremal bound (d = 21, 27, 33); the open values listed above are below it.
- Ternary self-dual means Euclidean self-dual over GF(3) with G G^T = 0 mod 3, not mod 2.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/record-tables/ternary-self-dual-largest-min-weight-12m.md
```

Already set up? Say `run V3R1T4S on ternary-self-dual-largest-min-weight-12m`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ternary-self-dual-largest-min-weight-12m`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
