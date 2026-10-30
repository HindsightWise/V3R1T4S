# Conway's Topswops: the maximum number of steps for 22 cards (next term of OEIS A000375 after Chaffin's f(21) = 282), or longer 22- and 23-card decks

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: needs cluster for the exact f(22) (f(21) took about 181,000 CPU-days); finding a longer deck is laptop-days of local search · open as of 2026-10-30

## The problem

Topswops (John Conway; Martin Gardner; Knuth, TAOCP 4A, section 7.2.1.2, exercise 107): shuffle cards 1..n. While the top card m is not 1, reverse the top m cards. f(n), OEIS A000375, is the largest number of steps over all decks. Known values: f(1..17) through Knuth's and later exhaustive searches; f(18) = 191 and f(19) = 221 (Kimura, Takahashi, Araki and Amano, arXiv:2103.08346, 2021); f(20) = 249 with a unique deck, and f(21) = 282 with five decks (Ben Chaffin, April 2026). Chaffin's searches took about 7,200 and 181,000 CPU-days. This lane re-checked Chaffin's 20-card and 21-card decks with its own simulator: they take 249 and 282 steps. The OEIS gives lower bounds f(22) >= 335 and f(23) >= 382 (Hugo Pfoertner, updated 2016), which come from optimisation searches, including Al Zimmermann's 2010-11 Topswops contest (winner Jarek Wroblewski, second Tomas Rokicki). That contest used prime deck sizes only, from 2 to 97. Its final report (azspcs.com/Contest/Cards/FinalReport, loaded 2026-10-30) gives 382 as the best 23-card score, first reached on 6 December 2010 and matched by about a dozen entrants, and it had no 22-card problem. Known bounds: a quadratic lower bound (Morales and Sudborough, 2010) and a Fibonacci upper bound.

## What counts as a win

The exact value of f(22), the first unknown term of OEIS A000375 at verification time. It must come with a complete, re-runnable exhaustive search (for example Knuth's forward algorithm with Chaffin-style pruning). The search must be independently re-run or cross-checked (for example by splitting the search tree and re-running a random sample of sub-trees with independent code), and the same code must reproduce f(n) for n <= 19.

## Partial wins

- **p1:** A 22-card deck taking at least 336 steps, or a 23-card deck taking at least 383 steps, strictly above the OEIS lower bounds f(22) >= 335 and f(23) >= 382, provided those bounds are unchanged on A000375 at verification time.

## How a win is checked

Simulate the deck: repeatedly reverse the top m cards, where m is the top card, until the top card is 1, and count the reversals. This takes microseconds. For an exact value, rerun the search on independent hardware, or audit it by re-running randomly chosen sub-trees with an independent implementation, and require exact agreement on the per-subtree maxima.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A000375>

## Sources

- <https://oeis.org/A000375>
- <https://benchaffin.com/topswops/topswops.html>
- <https://arxiv.org/abs/2103.08346>
- <http://azspcs.com/Contest/Cards/FinalReport>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The game stops when the top card is 1, not when the deck is sorted.
- The AZsPCs Topswops final report (azspcs.com/Contest/Cards/FinalReport) lists only prime sizes. Its best 23-card deck takes exactly 382 steps, the same as the OEIS bound, and it has no 22-card entry, so it does not raise either p1 bar. Its 23-card bar has resisted many strong entrants since 2010.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/topswops-22-cards.md
```

Already set up? Say `run V3R1T4S on topswops-22-cards`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `topswops-22-cards`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
