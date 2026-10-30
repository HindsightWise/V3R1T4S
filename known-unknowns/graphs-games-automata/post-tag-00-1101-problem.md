# MOONSHOT - Post's 1921 tag problem (00, 1101; delete 3): a word that never halts or cycles, or a proof that none exists

🕸️ **Graphs, games and automata** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster for exhaustive extensions; pure thought for the full problem · open as of 2026-10-30

## The problem

Emil Post's tag system deletes the first 3 symbols of a binary word and appends 00 if the first symbol was 0, or 1101 if it was 1. Post found it 'hopeless' in 1921, and Minsky (1967) wrote that he and Post found it intractable. It is unknown whether every initial word eventually halts (length below 3) or enters a cycle. Shigeru Watanabe described the basic cycle families in 1963, and Liesbeth De Mol studied the system in a series of papers following her 2007 thesis. In March 2021 Stephen Wolfram reported that all initial words up to (uncompressed) length 84, about 2 x 10^25 words, end in a cycle or halt. The longest transient he found is 643,158,954,877 steps (compressed initial word 28:264107671:2, ending in a cycle of length 10). No word is known to grow forever.

## What counts as a win

CONFIRMED only for (a) an initial binary word with a machine-checked proof (Lean, Isabelle or Coq) that its evolution under (delete 3; 0 -> 00, 1 -> 1101) never reaches a word shorter than 3 and never repeats a word, or (b) a machine-checked proof that every initial word eventually halts or repeats. Long simulations without a proof never count.

## Partial wins

- **p1:** An exhaustive verification, by code that can be audited and was independently re-run, that every initial word of length 85 (or every length from 85 to some L) halts or enters a cycle, with the maximum transient and its word reported, provided no publication found at claim time already covers that length.
- **p2:** An initial word whose transient exceeds 643,158,954,877 steps before it halts or enters a cycle, verified by an independent simulator run to the cycle, with the cycle length reported.

## How a win is checked

Simulate exactly with an independent implementation (calibration reproduced: 100100100000100000 reaches a cycle of length 28 after 2,141 steps). For transient claims, run to the first repeated word and report the step at which the cycle starts and its length. For exhaustive claims, re-run a random sample plus all words with the longest transients on an independent simulator, and audit the compression or symmetry reductions used. For proofs, compile the formal development and check the theorem statement against the rule.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://writings.stephenwolfram.com/2021/03/after-100-years-can-we-finally-crack-posts-problem-of-tag-a-story-of-computational-irreducibility-and-more/>

## Sources

- <https://writings.stephenwolfram.com/2021/03/after-100-years-can-we-finally-crack-posts-problem-of-tag-a-story-of-computational-irreducibility-and-more/>
- <https://en.wikipedia.org/wiki/Tag_system>
- <https://archive.org/details/computationfinit0000mins/page/267>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Only every third symbol is read, so the word splits into three interleaved phases; Wolfram's compressed representation works on the read phase and makes exhaustive search far cheaper.
- Treat the evolution as a Collatz-like map on block counts and search for a self-similar 'highway' family with a provable invariant, which would give a candidate for (a).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The status rests on a 2021 article; the web search budget ran out while this entry was checked, so later extensions (De Mol, Wolfram, or others) were not ruled out. Search before claiming p1 or p2.
- Lengths in Wolfram's tables are often compressed lengths (28 compressed corresponds to 84 uncompressed); state which one you use.
- Halting means the word becomes shorter than 3 symbols; an empty word is not the only halting state.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/post-tag-00-1101-problem.md
```

Already set up? Say `run V3R1T4S on post-tag-00-1101-problem`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `post-tag-00-1101-problem`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
