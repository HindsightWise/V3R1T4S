# Hofstadter's Q-sequence: does it die? Find an n where Q(n) is undefined, or push the existence frontier past 3*10^10

🔢 **Number hunts** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: needs cluster (memory of a few hundred GB to go past 3*10^10, since Q(n) refers back to about n/2) · open as of 2026-10-30

## The problem

Hofstadter's Q-sequence (Goedel, Escher, Bach, 1979; OEIS A005185) is Q(1) = Q(2) = 1 and Q(n) = Q(n - Q(n-1)) + Q(n - Q(n-2)). Its growth is chaotic and its rate unknown. It is not even known whether Q(n) is defined for all n: the sequence 'dies' at the first n where n - Q(n-1) < 1 or n - Q(n-2) < 1. Roman Pearce computed that Q(n) exists for n <= 10^10 (2014). M. Eric Carr extended this to n <= 3*10^10 (OEIS comment, July 2, 2023). The entry lists no larger frontier on 2026-10-30. Erdős Problem #422 (erdosproblems.com, no prize listed) asks the related question whether Q misses infinitely many integers, and notes that Q is not even known to be well-defined. Related sequences (Golomb, Conolly, the Hofstadter-Conway $10,000 sequence) are well understood; Q itself is not.

## What counts as a win

CONFIRMED (full win) for an index N such that Q(1..N-1) are defined and N - Q(N-1) < 1 or N - Q(N-2) < 1. Two independently written programs (different languages or memory layouts) must both reach N and agree on Q(N-1) and Q(N-2), and on checkpoint values Q(k*10^9) for every k up to N/10^9. Alternatively, a Lean proof (no sorry, standard axioms) that Q is defined for all n. Checked against the live https://oeis.org/A005185.

## Partial wins

- **p1:** Frontier extension: a computation showing that Q(n) is defined for all n <= M, with M at least TWICE the largest bound stated in the live A005185 entry (M >= 6*10^10 on 2026-10-30). It must publish Q(k*10^9) for every k <= M/10^9 and a hash of the whole sequence, reproduced exactly by a second, independently written program.

## How a win is checked

Rerun both programs (or a third, the verifier's own) to the claimed N or M, keeping Q values in 5-byte or bit-packed storage. Compare all checkpoints. For a death claim, print Q(N-2) and Q(N-1) and check the failing index condition by hand. Re-fetch A005185 for any newer frontier.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A005185>

## Sources

- <https://oeis.org/A005185>
- <https://oeis.org/A005185/b005185.txt>
- <https://www.erdosproblems.com/422>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Q(n) - n/2 stays small in relative terms, so Q(n) is about n/2. Store the offsets Q(n) - floor(n/2) in a compact signed format and keep only the window [n/2 - c, n] in RAM, streaming older blocks to disk.
- Pinn's generation structure (the sequence splits into 'generations' of doubling length) gives natural checkpoints and a way to parallelise the verification of later generations.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A death claim from a buggy indexing convention (1-based versus 0-based) is the most likely false positive. Reproduce Q(1..100) from the OEIS DATA first.
- 32-bit overflow in Q values or indices beyond 2^32 corrupts results silently.
- Reaching 3*10^10 again is a regression test, not a result.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/number-hunts/hofstadter-q-sequence-death.md
```

Already set up? Say `run V3R1T4S on hofstadter-q-sequence-death`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hofstadter-q-sequence-death`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
