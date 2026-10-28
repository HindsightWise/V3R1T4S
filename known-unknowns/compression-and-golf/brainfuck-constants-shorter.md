# Brainfuck constants: a shorter BF program producing a constant than the esolangs table

🗜️ **Compression and code golf** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The esolangs.org 'Brainfuck constants' page (last edited 25 June 2025) lists the shortest known Brainfuck code to leave value n in the cell (8-bit; separate wrapping and non-wrapping lists) for n = 0..255 plus larger numbers, with instruction count and cells used, under the convention that the code never touches cells left of the start. This is a Kolmogorov-complexity record table with a trivial mechanical checker. Find a program strictly shorter than the listed shortest for some n in the same category (wrapping / non-wrapping).

## What counts as a win

A Brainfuck string for some n listed on https://esolangs.org/wiki/Brainfuck_constants (re-fetched live immediately before claiming) such that a reference interpreter with unbounded right tape, 8-bit cells (wrapping only if claimed in the wrapping category), starting at all zeros, halts with the pointer on a cell holding n (mod 256 rules exactly as the page defines), never moves left of the start cell, and whose instruction count is strictly less than the smallest listed count for n in that category (and for numbers > 255, the page's stated cell-size conventions).

## Partial wins

- **nonwrap-2cell-improvement:** Improve any non-wrapping entry for n in 128..255.
- **exhaustive-optimality:** An exhaustive search certificate (enumeration log + checker) proving the listed wrapping program is optimal for all n up to some length L (e.g. all programs of length <= 14), publishing optimality for a range of n.
- **over-255:** A shorter program for one of the listed constants above 255.

## How a win is checked

20-line Python BF interpreter with step limit (e.g. 10^7), asserting final pointer cell value, no left-of-origin access, and length; the skeptic runs each candidate in milliseconds.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://esolangs.org/wiki/Brainfuck_constants>

## Sources

- <https://esolangs.org/wiki/Brainfuck_constants>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exhaustive enumeration of all syntactically balanced programs up to length 16-18 with a fast C/Rust interpreter, pruning by canonical forms (no '+-', '<>' adjacent pairs) and memoizing tape states; collect min length per n.
- Grammar-guided search over loop templates (multiplication loops, wrapping 'divide' loops like -[----->+<]) with parameter sweeps.
- Cross-domain import (superoptimization in compilers, e.g. STOKE/Souper): stochastic MCMC over programs with a cost = length + distance-to-target, then exhaustive verification.
- Cross-domain import (number theory/addition chains): use modular-inverse wrapping tricks (k*x == n mod 256) to design 1-loop programs; search over pairs (step, decrement) solving linear congruences.
- Cross-domain import (program synthesis / RL in AlphaDev style): Monte Carlo tree search over instruction sequences with interpreter feedback.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Convention: must not modify or rely on cells left of the starting pointer; some short programs violate this.
- Wrapping vs non-wrapping vs '(soft)' entries are different categories; compare within category.
- Final pointer position matters: the value must be in the cell under the pointer at halt.
- Programs must halt; the step limit must not be tight enough to reject a valid long-running program, nor loose enough to hang.
- Small n are likely already exhaustively optimal; check the talk page/history for prior exhaustive results before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/compression-and-golf/brainfuck-constants-shorter.md
```

Already set up? Say `run V3R1T4S on brainfuck-constants-shorter`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `brainfuck-constants-shorter`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
