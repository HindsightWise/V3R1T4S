# Anarchy Golf: a strictly shorter solution than the best-ranked one in some language on a post-mortem problem

🗜️ **Compression and code golf** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-minutes · open as of 2026-10-28

## The problem

golf.shinh.org (anarchy golf, run by shinh; 116 languages, active today: recent records dated 2026-10-28 JST, eight active problems up to #1831) keeps per-problem, per-language rankings of shortest correct programs. Only problems in post-mortem state are targets: after the deadline the page says 'all source codes will be revealed', so the full ranking and code are public. Active problems (solutions hidden until the deadline) and endless problems (no deadline, submissions never revealed) are live contests and are out of scope. Find a program in some language that is strictly shorter (bytes) than the current best for that post-mortem problem+language and passes all of the problem's published test cases on the same interpreter version.

## What counts as a win

A source file for a named anagol problem whose page http://golf.shinh.org/p.rb?<Problem> shows post-mortem state ('now post-mortem time, all source codes will be revealed'), and a language, such that (a) running it locally with the interpreter version listed on http://golf.shinh.org/version.rb against every published test input of that problem produces byte-identical expected output (trailing-whitespace rules as the server defines), and (b) its byte size is strictly smaller than the best entry for that language on the problem page re-fetched live immediately before claiming. No submission to the server is made by the agent.

## Partial wins

- **mainstream-lang-improvement:** Improve the best Python 3, Ruby, Perl or JavaScript solution on any post-mortem problem (strong-competition languages), checked the same way.
- **overall-first:** A solution shorter than the overall #1 across all languages for some post-mortem problem, checked the same way.

## How a win is checked

Download test inputs/outputs from the problem page, run with the matching interpreter version in a sandbox, diff outputs, count bytes with wc -c. Minutes.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <http://golf.shinh.org/>

## Sources

- <http://golf.shinh.org/>
- <http://golf.shinh.org/recent.rb>
- <http://golf.shinh.org/version.rb>
- <http://golf.shinh.org/l.rb?py>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Target languages with few golfers per problem (from l.rb per-language result pages) and port the overall-best algorithm from a terse language into them.
- Brute-force superoptimization of short expressions (e.g. magic-number/modular lookup tricks) with a search over Python expression grammars.
- Kolmogorov problems (fixed output): try zlib/base-N string compression with language-native decompressors vs hand-crafted generators.
- Cross-domain import (data compression): use LZ77/arith-coding analysis of the target output to find repeated structure, then encode via language string-repetition idioms.
- Cross-domain import (genetic programming / evolutionary computation): evolve programs with byte-length fitness under test-case constraints.
- Cross-domain import (number theory/hash design): search for perfect-hash magic constants mapping inputs to outputs (classic golfing 'magic formula' search) using SAT/brute force on 10 cores.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Interpreter version mismatch: a program passing on a newer local Python may fail on the server's version; use the exact versions on version.rb.
- Problems with hidden/randomized tests: only use post-mortem problems whose full test sets are visible.
- Trailing newline/whitespace rules; byte vs character counting for non-ASCII.
- Active and endless problems are out of scope: their code is hidden and they are live contests; never publish a solution to one. Post-mortem rankings also keep changing, so re-fetch the problem page before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/compression-and-golf/anagol-per-language-shortest.md
```

Already set up? Say `run V3R1T4S on anagol-per-language-shortest`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `anagol-per-language-shortest`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
