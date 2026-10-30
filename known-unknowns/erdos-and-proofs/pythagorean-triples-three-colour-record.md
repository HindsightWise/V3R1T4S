# Pythagorean triples with three colours: a triple-free 3-colouring of {1..N} for N above 25,000,000

✏️ **Erdős problems and proofs** · standard · tractability ★★★★☆ · compute: laptop-hours (tens of millions of triples; SAT or local search with a streaming checker) · open as of 2026-10-30

## The problem

Erdős and Graham asked whether the positive integers can be finitely coloured with no monochromatic Pythagorean triple a^2 + b^2 = c^2. For two colours the answer is no: Heule, Kullmann and Marek (SAT 2016) proved that {1..7824} admits a triple-free 2-colouring and {1..7825} does not, with a 200 TB proof that was later formally verified. For three colours the question is open, and progress is measured by the longest interval {1..N} with a triple-free 3-colouring. Heule and Kullmann ('The science of brute force', CACM 60(8), 2017) reported a 3-partition of {1..10^7}. A Zenodo preprint by Python Song (record 23329356, v1 12 Oct 2026, not peer reviewed) claims a 3-colouring of {1..25,000,000} that avoids all 62,324,099 triples, with the colouring file data/pyth3col_N25000000.raw.gz and Lean checking code at github.com/Geeksongs/Three-Colour-Pythagorean-Triples-Problem. An independent check on 2026-10-30 decompressed the file (25,000,000 bytes, SHA-256 e1500d6c25b116bdf1cb237bd9954b6f5a90b102fb1a77cb754e8d7be153e7d6). An Euclid-formula enumerator written separately from the preprint's code counted 62,324,099 triples and found none monochromatic. Push N higher.

## What counts as a win

Success means an explicit colouring c:{1..N} -> {0,1,2} (raw bytes or text, with a SHA-256 hash) such that no Pythagorean triple a < b < c <= N with a^2 + b^2 = c^2, primitive or not, is monochromatic. Two independent triple enumerators must confirm this and agree on the triple count. N must be STRICTLY GREATER (direction: max) than the best published value at verification time: the maximum of 25,000,000 (Zenodo 23329356 and its GitHub data), 10^7 (Heule-Kullmann CACM 2017), and anything found by a fresh search for three-colour Pythagorean records over the last 24 months.

## How a win is checked

Enumerator A uses Euclid's formula: for coprime m > n of opposite parity, take the primitive triple (m^2 - n^2, 2mn, m^2 + n^2) and all its multiples with hypotenuse <= N. Enumerator B, for each c <= N and each a with a < c/sqrt(2), tests whether c^2 - a^2 is a perfect square using integer isqrt (slower; run it on a random sample of c plus the full range up to 10^6). Count the triples with A and compare with the count reported by the record holder. Check that no triple is monochromatic. Do not run downloaded code; treat the published colouring as data only.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://zenodo.org/records/23329356>

## Sources

- <https://zenodo.org/records/23329356>
- <https://github.com/Geeksongs/Three-Colour-Pythagorean-Triples-Problem>
- <https://www.cs.utexas.edu/~marijn/publications/ptn.pdf>
- <https://en.wikipedia.org/wiki/Boolean_Pythagorean_triples_problem>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Only integers that occur in some triple matter. Integers in no triple (Pythagorean-free numbers, such as those all of whose prime factors are 3 mod 4 except for powers of 2) can take any colour, which shrinks the instance a lot.
- Use incremental SAT or local search over a sliding window, but make the window large. Keeping the published colouring on {1..20,000,000} fixed already forces a clash at 25,000,365 (see pitfalls), so free several million integers below 25,000,000 together with the new ones.
- Use residue- or valuation-based seed colourings, such as colour determined by v_p(n) for small primes p, then repair the conflicts with local search. The Song preprint analyses which such families fail and where.
- Decompose by connected components of the triple hypergraph restricted to [1..N]: many components are small and can be solved exactly and independently.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 25,000,000 record is a single-author, unrefereed preprint. Its colouring passed an independent check on 2026-10-30, but re-verify it yourself (as data) and look for errata before claiming. If it ever fails, the baseline is 10^7.
- The published colouring cannot simply be extended. 25,000,030 is the hypotenuse of triples whose two legs are at most 25,000,000 and share a colour, and these pairs cover all three colours, so no colouring that keeps {1..25,000,000} fixed gets past 25,000,029. Keeping only {1..24,000,000} or {1..20,000,000} fixed still forces a clash at 25,000,081 or 25,000,365. A longer interval means recolouring millions of earlier integers, not appending new ones.
- Non-primitive triples (multiples of primitive ones) must be included.
- Matching N = 25,000,000 is not a record; N must be strictly larger.
- Two colours are already settled (7824). A 2-colour claim is not this target.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/pythagorean-triples-three-colour-record.md
```

Already set up? Say `run V3R1T4S on pythagorean-triples-three-colour-record`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `pythagorean-triples-three-colour-record`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
