# Blanking and Beeping Busy Beavers: beat a small-domain champion (BLB(2,4), BLB(2,5), BBB(2,4)) or settle BLB(4)

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-28

## The problem

Variants of the Busy Beaver game tracked on the bbchallenge wiki. Blanking Beaver BLB(n,m): most steps an n-state m-symbol Turing machine takes before the tape first becomes all blank (halting or not). Beeping Busy Beaver BBB(n,m) (Scott Aaronson, 2020): most steps before the last visit to a 'beep' state for machines that beep finitely often (quasihalt; term coined by Nick Drozd). As listed on 2026-10-28 (Blanking_Beaver page last edited 2026-10-17, Beeping_Busy_Beaver page last edited 2026-10-25), with most small-domain champions from Nick Drozd's searches: BLB(2) = 8, BLB(3) = 34, BLB(4) >= 32,779,477 (listed as a lower bound, not proven exact), BLB(5) > 10^14,006, BLB(2,3) = 77, BLB(2,4) >= 1,367,361,263,049, BLB(2,5) > 10^32, BLB(3,3) > 10^^6.54 (Drozd, September 2026); BBB(3) = 55, BBB(4) = 32,779,478 (Coq-BBB4), BBB(2,3) = 59, BBB(2,4) > 2 x 10^23, BBB(3,3) > 10^^6.74. 2-state, 4- and 5-symbol spaces are small enough for laptop enumeration in tree normal form, unlike the 5- and 6-state domains.

## What counts as a win

Success means a Turing machine in standard bbchallenge text format with the stated number of states and symbols that (a) blanks the tape for the first time at a step count STRICTLY greater than the champion listed for that domain on https://wiki.bbchallenge.org/wiki/Blanking_Beaver, or (b) quasihalts at a step count strictly greater than the BBB champion listed on https://wiki.bbchallenge.org/wiki/Beeping_Busy_Beaver, both pages re-fetched live immediately before claiming; the step count is verified by direct simulation (counts up to about 10^13) or, for larger counts, by a machine-checkable accelerated proof (e.g. a Coq/Lean proof, or an exact macro-machine simulation whose rules are independently re-derived) and, for quasihalting, a translated-cycler certificate showing no further beeps. OR (c) an exact value BLB(4) = 32,779,477 (or a larger value with a new champion): every 4-state 2-symbol machine in tree normal form either blanks by that step, never blanks (with a checkable certificate), as reproduced by an independent decider.

## Partial wins

- **p1:** A new BLB(2,4) champion (criterion (a)), verified by direct C simulation with step count printed.
- **p2:** The exact value of BLB(4), with certificates, if the page still lists it with '>='.
- **p3:** A full enumeration of the 2-state 4-symbol domain in tree normal form with a published list of fewer than 1000 machines whose blanking status is undecided, plus the decider code.

## How a win is checked

Simulate the machine with an independent C or Rust simulator on a two-way infinite tape (blank symbol 0), counting steps until the tape is all 0 (blanking) or until the last beep; for very large counts, use an independent macro-machine/accelerated simulator and cross-check the first 10^9 steps against direct simulation. For non-blanking or non-quasihalting certificates (exact-value claims), re-run independent deciders (cyclers, translated cyclers, backward reasoning, finite automata reduction) and check every holdout is closed.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Blanking_Beaver>

## Sources

- <https://wiki.bbchallenge.org/wiki/Blanking_Beaver>
- <https://wiki.bbchallenge.org/wiki/Beeping_Busy_Beaver>
- <https://wiki.bbchallenge.org/wiki/Champions>
- <https://bbchallenge.org/>
- <https://www.scottaaronson.com/papers/bb.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Exhaustive tree-normal-form enumeration of 2-state 4-symbol machines (roughly 10^8-10^9 candidates after TNF) with a cheap 'tape returns to blank' detector; run every candidate to 10^7 steps and promote survivors to accelerated simulation.
- Look for blanking machines among known BB(2,4) and BBB(2,4) long-runners: Shawn Ligocki's 2x4 machine lists contain machines whose tape may blank later than the current BLB champion.
- Import from cellular-automaton glider analysis: blanking events come from 'counters' that sweep and erase; model the macro behaviour as a recurrence (Collatz-like) and solve it in closed form to predict the blanking step exactly, as done for BB(5)/BB(6) champions.
- Import from model checking: encode 'tape blank at step t' as a bounded model-checking query with a SAT solver over the TNF parameters, to search for machines with long blanking times without simulating each.
- For BLB(4) exactness, reuse bbchallenge's BB(5) decider stack (cyclers, translated cyclers, backward reasoning, FAR) adapted from halting to blanking.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Blanking means the WHOLE tape is blank at some step after the start; a machine that halts with ones on the tape does not blank, and step 0 does not count.
- BBB counts steps until the LAST beep; a machine that beeps forever never quasihalts, and claiming quasihalting needs a proof that no later beep occurs.
- Champion step counts are off-by-one sensitive (whether the final transition counts); calibrate your simulator on the listed champions first (e.g. BLB(2,3) = 77, BLB(3) = 34, BBB(3) = 55, BBB(2,3) = 59).
- Machine format and symbol/state counting must match the wiki's (TNF, '---' for undefined transitions, Z for halt).
- These variants are actively studied on the Busy Beaver Discord and wiki; re-fetch the champion tables immediately before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/blanking-beeping-beaver-small-domains.md
```

Already set up? Say `run V3R1T4S on blanking-beeping-beaver-small-domains`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `blanking-beeping-beaver-small-domains`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
