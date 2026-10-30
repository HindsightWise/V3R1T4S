# Tiny Tag busy beaver: the first exact value beyond n = 10 (all 2,048 length-11 strings classified)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★★☆ · compute: laptop-minutes to laptop-hours · open as of 2026-10-30

## The problem

Tiny Tag (bbchallenge wiki page created 2025-12-02 by Discord user Jack, last edited 2026-08-11) is a self-describing cyclic tag system: the runs of an initial binary string b (maximal blocks of equal bits) become the production rules p_1..p_k, used cyclically; each step deletes the first bit and, if it was 1, appends the current rule, then advances the rule pointer; it halts when the string is empty. f(n) is the largest finite number of steps taken by any length-n string. The page lists f(1..10) = 1, 5, 9, 13, 15, 334, 404, 670, 12,584, 2,180,995 (the last for 0100011110), says values beyond n = 10 are 'not currently known', and gives a deliberately weak bound f(48) >> 971,038 from eight copies of 010111. Determining f(11) means classifying 2,048 strings, each halting or proved non-halting.

## What counts as a win

Success means an exact f(n) for some n >= 11 while https://wiki.bbchallenge.org/wiki/Tiny_Tag (re-fetched before claiming) lists no exact value for it: every one of the 2^n strings either halts (step count by direct simulation) or carries a non-halting certificate re-checked by an independent program (an exact repeated (pointer, string) state, or a translated-cycle or block-growth proof checked symbolically), and the maximum halting step count is reported with its string.

## Partial wins

- **p1:** Exact f(11), with all non-halting length-11 strings certified.
- **p2:** Exact f(12).
- **p3:** A classification of the 2,048 length-11 strings in which every string either halts (with its step count) or carries a re-checked non-halting certificate, except at most 20 strings, which are published as an explicit holdout list.

## How a win is checked

Independent simulator from the page's definition (calibration reproduced: f(1..10) champions halt after 1, 5, 9, 13, 15, 334, 404, 670, 12,584 and 2,180,995 steps). Re-check every non-halting certificate, and confirm the classified strings number exactly 2^n.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Tiny_Tag>

## Sources

- <https://wiki.bbchallenge.org/wiki/Tiny_Tag>
- <https://wiki.bbchallenge.org/wiki/Cyclic_Tag>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Most non-halting strings grow linearly: detect a fixed pointer phase in which the string's suffix repeats with a growing prefix, and prove it symbolically.
- Complementary symmetry: the rules depend only on run lengths and the first bit, so strings with the same run structure can share analysis.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The rules are the runs of the INITIAL string and never change; the pointer advances on every step, including steps that delete a 0.
- A quick 2e7-step run (made while this entry was written, not published) left several hundred length-11 strings running; most are probably growers, but each needs a certificate.
- The page is young and has few contributors; re-fetch it, and check its history, before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/tiny-tag-busy-beaver-exact.md
```

Already set up? Say `run V3R1T4S on tiny-tag-busy-beaver-exact`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `tiny-tag-busy-beaver-exact`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
