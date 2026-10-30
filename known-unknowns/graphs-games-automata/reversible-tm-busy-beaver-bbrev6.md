# Busy Beaver for reversible Turing machines: decide BBrev(6)'s 388 holdouts or beat the 537,556-step champion

🕸️ **Graphs, games and automata** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours (bbchallenge-style deciders on 388 machines) · open as of 2026-10-30

## The problem

BBrev(n, m) is the longest run of a halting n-state, m-symbol Turing machine that is reversible in Bennett's sense, using Bruce Smith's 'microscopic reversibility' condition for one-tape quintuple machines: for every state, all transitions into it move in the same direction and write different symbols. The bbchallenge wiki's Reversible Turing Machine page (last edited 2026-07-16) lists exact values BBrev(2) = 6, BBrev(3) = 17, BBrev(4) = 48 (Matthew House and Shawn Ligocki) and BBrev(5) = 388 (champion 1RB0RD_1RC0RB_1RD1RZ_1LE1LA_0LE0LA, Shawn Ligocki and Matthew House), and lower bounds BBrev(6) >= 537,556 (1RB1LD_1LC1RE_0LD0LC_0RE0RF_0RA1RZ_1RF1RA, Ligocki), with 388 holdouts in BBrev6_holdouts_388.txt, and a BBrev(7) lower bound from an early enumeration.

## What counts as a win

Success means (a) a reversible (per the page's condition) 6-state 2-symbol machine in bbchallenge text format that halts from a blank tape after STRICTLY more than the BBrev(6) bound listed on https://wiki.bbchallenge.org/wiki/Reversible_Turing_Machine, re-fetched live before claiming, verified by direct or proved-accelerated simulation; or (b) an exact BBrev(6) while the page still shows ' > =': every machine on the current holdout list decided. Each non-halter carries a certificate an independent decider re-checks (cycler, translated cycler, finite automata reduction, backward reasoning, or a Coq/Lean proof). Each holdout that reaches an undefined ('---') transition is reported with the step at which it does so, and is then expanded into all of its reversible tree-normal-form completions (halting there, or each reversible new transition), every one of which is decided the same way, with each halter's step count given.

## Partial wins

- **p1:** Non-halting certificates, re-checked by an independent decider, for at least 300 of the 388 machines in BBrev6_holdouts_388.txt, with the remaining list published.
- **p2:** Exact BBrev(6) (criterion (b)).
- **p3:** A reversible 7-state 2-symbol machine beating the BBrev(7) lower bound listed on the page, with a proved step count.

## How a win is checked

Check the reversibility condition mechanically for every state. Simulate with an independent TM simulator using the bbchallenge step convention (calibration reproduced: BBrev(5) champion halts after 388 steps, BBrev(6) champion after 537,556). For holdout claims, re-run independent deciders on each certificate and confirm that the decided set equals the published holdout list.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://wiki.bbchallenge.org/wiki/Reversible_Turing_Machine>

## Sources

- <https://wiki.bbchallenge.org/wiki/Reversible_Turing_Machine>
- <https://wiki.bbchallenge.org/w/images/8/86/BBrev6_holdouts_388.txt>
- <https://doi.org/10.1147/rd.176.0525>
- <https://scottaaronson.blog/?p=4916#comment-1851339>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Run the BB(5) decider stack (Coq-BB5 deciders: cyclers, translated cyclers, backward reasoning, FAR) on the 388 machines first; reversibility makes backward reasoning especially strong, because each configuration has at most one predecessor.
- For new champions, search reversible machines built from known 6-state counters, or enumerate in tree normal form with the reversibility constraint pruning early.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The holdout file contains undefined transitions ('---'); a machine can halt by reaching one. Count steps the way the page's champions do.
- Reversibility is a constraint on the whole transition table including transitions added later in tree normal form; check it on the completed machine.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/reversible-tm-busy-beaver-bbrev6.md
```

Already set up? Say `run V3R1T4S on reversible-tm-busy-beaver-bbrev6`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `reversible-tm-busy-beaver-bbrev6`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
