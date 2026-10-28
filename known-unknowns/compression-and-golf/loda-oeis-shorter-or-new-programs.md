# LODA: a new verified LODA program for an OEIS sequence that has none

🗜️ **Compression and code golf** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The LODA project (loda-lang.org; programs repo loda-lang/loda-programs, last program maintenance commit 2026-09-30, last commit 2026-10-18; loda-cpp release v26.8.1 of 1 Aug 2026) mines short assembly-like programs that generate OEIS sequences and checks them mechanically against the OEIS b-files. LODA does not rank programs by length: loda-cpp's Checker::isOptimizedBetter replaces a program only when the new one is simpler by static checks (shorter only for sequences with at most 100 known terms), corrects it, computes more terms, or runs faster, so the repo often keeps longer, faster programs (A000045's is a 31-operation logarithmic-time method) and a shorter program is not a LODA record. Produce a LODA program for an OEIS sequence that has no program in the repo and is not on its deny list, verified against the OEIS b-file.

## What counts as a win

A .asm program for an OEIS id such that the official loda evaluator (loda-cpp, latest release built from source) reproduces every term of the OEIS b-file https://oeis.org/A<id>/b<id>.txt exactly, the b-file having at least 100 terms, where no file oeis/<NNN>/A<id>.asm exists on https://github.com/loda-lang/loda-programs main and the id is not listed in that repo's oeis/deny.txt, both re-fetched live immediately before claiming.

## Partial wins

- **ten-new-programs:** Ten new programs for sequences with no LODA program and not in deny.txt, each verified on >= 200 b-file terms.
- **new-program-low-anumber:** A new program for a sequence in A000001-A099999 that has no LODA program and is not in deny.txt, verified the same way.

## How a win is checked

Build loda-cpp from its GitHub source, run 'loda eval' on the program for as many terms as the b-file has, and diff against the b-file; then confirm on loda-programs main that oeis/<NNN>/A<id>.asm does not exist and the id is not in oeis/deny.txt. Seconds to minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/loda-lang/loda-programs>

## Sources

- <https://github.com/loda-lang/loda-programs>
- <https://loda-lang.org/>
- <https://loda-lang.org/programs/>
- <https://github.com/loda-lang/loda-cpp/releases>
- <https://github.com/loda-lang/loda-cpp/blob/main/src/mine/checker.cpp>
- <https://oeis.org/A000045/b000045.txt>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run the LODA miner locally (mutation + pattern templates) focused on OEIS keyword:easy sequences lacking programs.
- Formula-to-program compiler: parse OEIS FORMULA fields (linear recurrences, products, gcd/divisor sums) and emit LODA code directly.
- Cross-domain import (symbolic regression in physics): use PySR-style equation search on sequence terms, then compile the found formula to LODA.
- Cross-domain import (program reuse): many sequences are transforms (partial sums, binomial transforms, characteristic functions) of sequences that already have programs; LODA's seq operation can call them.
- Cross-domain import (linear-feedback shift registers / coding theory): Berlekamp-Massey to detect linear recurrences (also modulo primes) and emit minimal recurrence loops.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Matching the b-file is not a proof of correctness for all n; the claim is 'verified on N terms', not 'proved'.
- The repo moves quickly (miners run continuously and add programs daily); re-fetch before claiming absence.
- Some sequences are excluded by LODA deliberately: check the repo's oeis/deny.txt (not suitable for LODA) before claiming.
- Shorter is not better in LODA: the project prefers simpler, correct and faster programs, so a shorter program for a sequence that already has one is not a win here.
- A program that uses seq to call the target sequence itself is rejected by LODA's checker; calls to other sequences must reference programs that exist in the repo.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/compression-and-golf/loda-oeis-shorter-or-new-programs.md
```

Already set up? Say `run V3R1T4S on loda-oeis-shorter-or-new-programs`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `loda-oeis-shorter-or-new-programs`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
