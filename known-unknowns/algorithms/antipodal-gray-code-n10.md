# n-antipodal Gray codes: is there a 10-bit Gray code in which every word's complement is exactly 10 steps away? (Killian-Savage, open for even n >= 10)

⚡ **Algorithms** · standard · tractability ★★☆☆☆ · compute: laptop-days (SAT/CP on 1024 positions with heavy symmetry; a code checks instantly) · open as of 2026-10-30

## The problem

In a t-antipodal n-bit Gray code (a cyclic listing of all 2^n words with single-bit steps), the complement of every word appears exactly t steps before or after it. Killian and Savage ('Antipodal Gray codes', Discrete Math. 2004) studied t = n, attributing the question to Snevily. They showed that no n-antipodal code exists for odd n >= 5 or for n = 6, and gave a construction when n is a power of 2. They asked whether n-antipodal n-bit codes exist for even n >= 10. Chang, Eu and Yeh (2007) characterised t-antipodal codes for odd n (t = 2^(n-1) - 1 only) and gave codes for other values of t when n is even. Knuth (TAOCP 4A, Ex. 7.2.1.1-49) gives t = 2^(n-1). Mütze's survey (arXiv:2202.01280 v4, 30 Jul 2024, Problem P7) lists even n >= 10 as open. The smallest open case is n = 10. A Semantic Scholar check of papers citing the survey (2026-10-30) found no resolution.

## What counts as a win

Success means settling n = 10, in one of two ways. (a) An explicit cyclic 10-bit Gray code: all 1024 words, consecutive words (cyclically) differing in one bit, and for every position i the complement of word i at position i + 10 or i - 10 (mod 1024). It must pass two independent checkers. (b) A rerunnable nonexistence proof: an UNSAT certificate (DRAT/LRAT, checked by a verified checker) of a published encoding whose correctness is argued in a short note, or a written proof.

## Partial wins

- **p1:** An explicit n-antipodal n-bit Gray code for n = 12 or n = 14 (even, not a power of 2), verified the same way. It counts only if that case is unsettled in the survey and later literature at claim time.

## How a win is checked

Read the 1024 words into a position table. Check that it is a permutation of {0..1023}, that consecutive XORs (including last to first) are powers of 2, and that for each i, word[(i+10) mod 1024] or word[(i-10) mod 1024] equals word[i] XOR 1023. Calibrate on Killian-Savage's 8-antipodal 8-bit construction, and check that a SAT search finds nothing for n = 6.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2202.01280>

## Sources

- <https://arxiv.org/abs/2202.01280>
- <https://en.wikipedia.org/wiki/Gray_code>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- If the complement of word i sits at position i + n, the n transitions between them flip every coordinate exactly once. The transition sequence is therefore built from length-n windows that are permutations of [n]. Encode the transition sequence in SAT/CP with this window structure, and break symmetry by fixing the first n transitions as 0, 1, ..., n-1.
- Look for codes with a cyclic symmetry: the transition sequence invariant under a shift combined with a fixed coordinate permutation (for example a shift by 2n with a rotation of the coordinates). Generalise the structure of the Killian-Savage power-of-2 construction.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The distance must be exactly n in one direction, measured cyclically along the code, not in Hamming distance.
- For odd n the answer is known (impossible for t = n when n >= 5); only even n that are not powers of 2 are open.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/algorithms/antipodal-gray-code-n10.md
```

Already set up? Say `run V3R1T4S on antipodal-gray-code-n10`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `antipodal-gray-code-n10`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
