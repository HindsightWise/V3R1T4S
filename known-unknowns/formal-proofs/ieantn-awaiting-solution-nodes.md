# IEANTN (explicit analytic number theory network): a Comparator-verified solution for an unclaimed node (e.g. the cotangent zeta-value expansion)

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

IEANTN (teorth/IEANTN, the Integrated Explicit Analytic Number Theory Network maintained by Terence Tao and contributors; main ec66e38, 2026-10-18, Lean v4.34.0-rc2) records explicit analytic number theory as a graph of nodes. Each node's Challenge.lean states conditional theorems with deliberate sorries. A node becomes Lean-backed when a separate Solutions/ < Family > . < version> project proves the challenge and Comparator accepts it. STATE.md (generated) lists 63 node versions and 132 conclusions: 47 lean-comparator (17 of those receipts are stale after a Mathlib bump), 45 literature, 32 numerical, 4 none-yet, 3 bridged, 1 asserted. Tasks are claimed by commenting 'claim' on an issue (a bot assigns it and moves the card on github.com/users/teorth/projects/3); CONTRIBUTING.md calls claiming a courtesy, not a lock. Unclaimed awaiting-solution nodes on 2026-10-30 include CotangentSeries.v1, cot_series_zeta_values: π cot πz = 1/z − 2 Σ ζ(2n) z^{2n−1} as a HasSum for 0 < |z| < 1. Mathlib lacks this: it has Euler's partial fractions (cot_series_rep) and riemannZeta_two_mul_nat, but not the expansion at the origin. The node has no linked issue and no open PR. Another is GammaAsymptotics.v1, digamma_sub_log_isBigO (ψ(w) − log w = O(1/|w|) on Re w ≥ 1). Its linked issue #64 is closed, though it still lists teorth as assignee. The node itself records that its recurrence route does not prove it and that a Binet or Gauss integral representation is needed. The sibling GammaAsymptotics.v2 strip version is already lean-comparator. Claimed nodes are excluded: BKLNW (#50, xinjiegit), FKS (#52, marcosadriano27), Buthe (#56, AlstonTZ), DudekPlatt (#63, elmismisimoxhunca). On #111 (closed 2026-09-26) Tao wrote that other matters have limited his time on the project; 13 PRs are open, none touching these two nodes. Target: supply a Solution for an unclaimed node version.

## What counts as a win

Success means a Lake project under Solutions/ < Family > . < version> for one node version. Re-fetch live IEANTN main immediately before claiming. At that point the node version must have no Solutions directory, no lean-comparator receipt, no open issue that is assigned to or claimed for it (a closed issue, such as #64, does not count), and no open PR that touches it. leanprover/comparator must accept it against the node's generated Challenge.lean: same statements, only propext/Classical.choice/Quot.sound, and the node's imports used only as the hypotheses the scaffold provides. Excluded: nodes in the RosserSchoenfeld families (they overlap the PNT+ bank entry), the claimed BKLNW, FKS, Buthe and DudekPlatt families while their issues are open and assigned, and statements that are the headline problem of an active lean-eval problem. No PR is opened.

## Partial wins

- **p1:** CotangentSeries.v1 challenge_cot_series_zeta_values proved and accepted by Comparator, provided Mathlib at the pinned revision does not already contain the expansion.
- **p2:** For a node version that meets every exclusion and claim condition of the success criterion and whose evidence is `literature`, a Comparator-accepted proof of at least one of its conclusions as a conditional theorem from the node's declared imports, with the other conclusions of that node left open.

## How a win is checked

Clone IEANTN at the stated commit, build the core (`lake build`; one sorry warning per conclusion is expected), build the Solution project, and run Comparator against the challenge as docs/SOLUTIONS.md and CONTRIBUTING.md describe. Check the board and open PRs for claims.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/teorth/IEANTN/blob/main/STATE.md>

## Sources

- <https://github.com/teorth/IEANTN>
- <https://github.com/teorth/IEANTN/blob/main/STATE.md>
- <https://github.com/teorth/IEANTN/blob/main/docs/SOLUTIONS.md>
- <https://github.com/users/teorth/projects/3>
- <https://github.com/leanprover/comparator>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Cotangent: start from Mathlib's cot_series_rep (Euler's partial fractions), expand each 1/(z±n) geometrically for |z| < 1 and swap the double sum (summable by comparison with Σ |z|^{2k}/n^{2k}), then identify Σ_n n^{-2k} with riemannZeta (2k).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Audit the challenge statement against the source before proving, as SOLUTIONS.md insists. On FKS2 such an audit found four wrong statements.
- An upstream development that 'does' a theorem may thread numerics as deliberate sorries. Comparator rejects that.
- Mathlib moves; if the cotangent expansion has landed upstream, p1 is a cleanup, not a win.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/ieantn-awaiting-solution-nodes.md
```

Already set up? Say `run V3R1T4S on ieantn-awaiting-solution-nodes`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `ieantn-awaiting-solution-nodes`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
