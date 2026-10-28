# OEIS 'keyword:more' sequences: compute the next term(s) beyond the live entry and b-file

🎲 **Recreational math** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

The OEIS flags sequences needing more terms with keyword 'more': on 2026-10-28 the search keyword:more returned 27,020 sequences, and keyword:more keyword:nice alone returned 845. Many are combinatorial counts or searches whose next term is within laptop reach with a better algorithm. Target: a new term (the next unknown index) for a 'more' sequence, computed by two independent programs.

## What counts as a win

Success means one new term for one OEIS sequence A-number that carries keyword 'more' in its live entry (https://oeis.org/Annnnnn and its b-file, re-fetched immediately before claiming). The term must be at least one new value at the first index not present in DATA or the b-file. It must be computed by two independently written programs (different algorithms or languages) that agree, and both must reproduce all existing terms. The term must not appear in the entry's comments/links/extensions, in the OEIS edit history (https://oeis.org/Annnnnn/history, including pending drafts), or in an OEIS search for the term value. Excluded: any A-number named in another entry of the V3R1T4S bank (bank/targets.json or an open bank proposal), e.g. A075458, A088202, A292192, A250000, A279405, A006075, A028420, A389689, A389690, A392305, A391791, A387261, A387262, A357271; those terms count only under their own targets. Near-repdigit/repunit prime-index sequences are excluded unless the claimed term lies beyond the searched limit reported by the external search project that covers them (e.g. Makoto Kamada's pages), checked live. No submission to the OEIS.

## Partial wins

- **p1:** An independent verification that FAILS to reproduce an existing term (an error in the OEIS entry), with both programs and a hand-checkable explanation.
- **p2:** A proven lower or upper bound for the next term (e.g. exhaustive search to a limit with no hit) for a 'search' sequence, with logs.

## How a win is checked

Run both programs from a clean checkout on the skeptic's machine (≤ 1 hour, choose sequences accordingly); diff against the live b-file; fetch the history page for drafts.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/search?q=keyword:more>

## Sources

- <https://oeis.org/search?q=keyword:more>
- <https://oeis.org/search?q=keyword:more&fmt=json>
- <https://oeis.org/search?q=keyword%3Amore+keyword%3Anice>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Mine the JSON search API for 'more' sequences whose last term was added long ago, with small terms and a short definition (counting problems on graphs, permutations, polyforms).
- Transfer-matrix and dynamic-programming rewrites of brute-force counts (often gain 2-3 terms).
- Cross-domain import (statistical physics): enumerations of lattice objects via the corner transfer matrix / finite-lattice method used for Potts and self-avoiding-walk series.
- Cross-domain import (database engines): meet-in-the-middle with hash joins and columnar bitsets for 'number of solutions' searches; treat the count as a join cardinality.
- Use SAT/#SAT model counters (ganak, d4) for constraint-defined counts.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Ambiguous definitions: the OEIS entry's DATA defines the sequence; reproduce all existing terms before trusting a new one.
- Terms may be in the b-file or a pending draft but not in DATA; check both and the history page.
- Off-by-one offsets (index base) produce a 'new' term that is actually an existing one.
- Prime-search 'more' sequences (repunit-like) have external searched limits; a 'new' term below that limit would already be known.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/oeis-keyword-more-new-terms.md
```

Already set up? Say `run V3R1T4S on oeis-keyword-more-new-terms`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `oeis-keyword-more-new-terms`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
