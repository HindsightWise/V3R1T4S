# Busy Beaver for FRACTRAN: beat a BBf(22..24) champion, decide BBf(23)'s or BBf(24)'s holdouts, or settle a Fenrir cryptid

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours for enumeration and simple deciders; Lean proof checking per holdout in minutes · open as of 2026-10-30

## The problem

BBf(n) is the longest run, starting from 2, of a halting FRACTRAN program of size n. A rule a/b has size Omega(a) + Omega(b) (prime factors with multiplicity), and a program's size is its number of rules plus the sum of rule sizes. The bbchallenge wiki's Fractran page (last edited 2026-10-28) lists exact values through n = 21: BBf(20) = 746 (champion [7/15, 22/3, 6/77, 5/2, 9/5], Jason Yuen, 2025-11-13) and BBf(21) = 31,957,632 (champion [7/15, 4/3, 27/14, 5/2, 9/5], Jason Yuen, 2025-11-16; the last 140 holdouts proved non-halting with Lean proofs prompted from Claude Opus 4.6, March 2026). Beyond that it lists lower bounds: BBf(22) > 1.146 x 10^62 (Shawn Ligocki and Jason Yuen), BBf(23) > 4.393 x 10^124 (Ligocki, 2026-06-01), BBf(24) > 9.000 x 10^14448 (Yuen, 2026-09-09). Size 22 is decided except for the three Fenrir cryptids (sz22_3.txt; Jason Yuen and Claude Opus 4.6, 2026-03-22; non-halting if and only if a Hydra-type walk never stops). The holdout lists are kept in Jason Yuen's int-y1/BBFractran repository, whose README is newer than the wiki: size 23 has 13 holdouts (sz23_13.txt, official since 2026-10-16: Fenrir, 11 Hydra-like cryptids and #601), and size 24 has 3,580 (sz24_3580.txt, 2026-10-27, after Lean-verified progress certificates; the wiki still shows an older 231,432). The README's TODO names a size-24 program, [2/15, 1/6, 441/2, 11/3, 25/7, 6/11], that should beat the BBf(24) champion if it halts. The wiki lists it as 'Energy Vampire' (Jason Yuen and Claude Opus 5.5; Beaver Math Olympiad problem 12, still unsolved): a Hydra-type pseudo-random walk, Hydra(8, 3, [0, 3, 6], [-1, 0, 1], (1, 1)), that is expected to halt on probabilistic grounds, though it is unknown whether it does in practice.

## What counts as a win

Success means one of: (a) a FRACTRAN program of size n, 22 <= n <= 24 (size convention of https://wiki.bbchallenge.org/wiki/Fractran), that halts from 2 after STRICTLY more steps than the lower bound listed for n on that page, re-fetched live before claiming, with the step count established by exact simulation or by an accelerated simulation whose rules are proved (a Lean or Coq proof, or exactly re-derived macro rules); (b) all holdouts of sz23_13.txt or of the current size-24 holdout list decided, each non-halter with a Lean (or Coq) proof that compiles and each halter with an exact step count, so that BBf(23) or BBf(24) becomes exact; or (c) one Fenrir program from sz22_3.txt decided: a halting step count or a compiled non-halting proof.

## Partial wins

- **p1:** Compiled Lean proofs of non-halting for at least 100 programs on the current BBf(24) holdout list (sz24_3580.txt or its successor) that the repository does not already mark as proved.
- **p2:** Criterion (a) for n = 24: a size-24 program halting from 2 after more than 9.000 x 10^14448 steps, with a proved step count.
- **p3:** An independent re-enumeration of all programs of size at most 21, with its own deciders, that reproduces BBf(20) = 746 and BBf(21) = 31,957,632 and leaves no holdout without a certificate.

## How a win is checked

Simulate with exponent vectors: at each step apply the first fraction whose denominator divides the current number, counting rule applications until none applies (the BBf(21) champion halts after 31,957,632 steps, a calibration that was reproduced). Recompute program sizes from the fractions. Compile Lean proofs with the stated toolchain and check that their theorem statements name the exact program. For huge step counts, re-derive every acceleration rule by hand or with a proof assistant.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Fractran>

## Sources

- <https://wiki.bbchallenge.org/wiki/Fractran>
- <https://wiki.bbchallenge.org/wiki/Fenrir>
- <https://github.com/int-y1/BBFractran/blob/main/holdout/README.md>
- <https://github.com/int-y1/BBFractran/blob/main/holdout/sz23_13.txt>
- <https://en.wikipedia.org/wiki/FRACTRAN>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- FRACTRAN programs are vector addition systems with priorities; borrow VASS techniques (linear invariants, the 'Masked Linear Invariant' and 'Power Limit' deciders already used at sizes 18-21, Presburger acceleration with the FAST tool) to close most size-24 holdouts automatically.
- Group the size-24 holdouts into equivalence classes (the repository has an unofficial 2,245-class grouping) and prove one representative per class.
- For new champions, look for programs that simulate fast-growing Collatz-like maps, as the size-22 to 24 champions do.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Fenrir and the size-23 Hydra-like cryptids are as hard as the Hydra problem (see the bb33-bb25-cryptid-adjacent target); do not expect them to fall to generic deciders.
- Step counting: a step is one rule application; reaching a number no fraction applies to ends the run without an extra step.
- Rule order matters (first applicable fraction wins), so reordering a program gives a different program.
- The wiki and the repository README disagree on current holdout counts (the wiki is older); use the newest README list, quote its file name, and note that the size-21 errata show lists get corrected.
- The README's TODO candidate [2/15, 1/6, 441/2, 11/3, 25/7, 6/11] is public. It is the wiki's 'Energy Vampire' (BMO problem 12), and whether it halts at all is open, so a plain simulation may never end. Showing that it halts satisfies (a) and p2 only with a proved step count, and the claim must credit the README and the wiki for the candidate.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/fractran-busy-beaver-bbf.md
```

Already set up? Say `run V3R1T4S on fractran-busy-beaver-bbf`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `fractran-busy-beaver-bbf`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
