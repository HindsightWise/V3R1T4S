# Brownian Motion Lean project: close an unclaimed sorry (uniform integrability of stopped submartingales, UI martingale convergence, reflection principle)

✅ **Formal proofs** · harvest (many cells or partial wins within reach) · tractability ★★★☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

The Brownian Motion project (RemyDegenne/brownian-motion, Lean v4.35.0 at master 497e5e2, 2026-10-27) builds Brownian motion and stochastic integration in Lean against a blueprint. Tasks are claimed by commenting on issues (bot-assigned). On 2026-10-30 it has 21 sorries in 10 files. In progress or claimed: Komlos.lean (PRs #442, #358; #430 assigned to Aaron1011), DoobMeyer, QuadraticVariation and SquareIntegrable (PR #487), DoobLp (PR #498), and Submartingale.stoppedValue_min_ae_le_condExp in OptionalSampling.lean (blueprint lem:optionalSamplingSubmartingale, issue #263 claimed by YanYablonovskiy). LocalMartingale.isStable_submartingale is also off-limits: its blueprint proof uses that claimed lemma. Unclaimed with no open PR: Submartingale.uniformIntegrable_stoppedValue (issue #262, unassigned since CoolRmal disclaimed), Martingale.ae_tendsto_limitProcess, Martingale.condExp_limitProcess_ae_eq and its stopping-time version Martingale.condExp_limitProcess_ae_eq' (UniformIntegrable.lean), and the reflection principle IsBrownianReal.reflection (Gaussian/IteratedLogarithm.lean, needs the strong Markov property). Two statements are false as written. IsStandardGaussian.tail claims P(X ≥ x) ~ exp(-x²/2)/x, but the true asymptotic carries a factor 1/√(2π); the ratio is 0.3951 at x = 10. hasIntegrableSup_const in ClassD.lean asks that a constant be integrable for an arbitrary measure P (there is no IsFiniteMeasure in scope), which fails for P = volume on ℝ and c ≠ 0. Credit: Rémy Degenne and the project's contributors.

## What counts as a win

Success means a patch that replaces the `sorry` in one of Submartingale.uniformIntegrable_stoppedValue, Martingale.ae_tendsto_limitProcess, Martingale.condExp_limitProcess_ae_eq, Martingale.condExp_limitProcess_ae_eq' or IsBrownianReal.reflection on live brownian-motion master, re-fetched immediately before claiming. At that moment the declaration must not be in a file touched by an open PR and must not be the subject of an assigned or claimed issue. The statement must be unchanged (diff-checked). `lake build` must succeed at the pinned toolchain and manifest, and `#print axioms` on the declaration must show only propext/Classical.choice/Quot.sound (no sorryAx, no new axiom, no native_decide). IsStandardGaussian.tail and hasIntegrableSup_const are false as stated and can never be the full win. stoppedValue_min_ae_le_condExp and isStable_submartingale are excluded while issue #263 is claimed.

## Partial wins

- **p1:** hasStronglyMeasurableSupProcess_const proved sorry-free with the statement unchanged, together with a kernel-checked Lean counterexample to hasIntegrableSup_const as stated (e.g. Ω = ℝ, P = volume, c = 1) and a sorry-free proof of the same lemma with [IsFiniteMeasure P] added.
- **p2:** A kernel-checked Lean proof, compiling against the project, of the negation of IsStandardGaussian.tail as stated (exhibit Ω, P, X with HasLaw X (gaussianReal 0 1) P for which the IsEquivalent fails), together with a sorry-free proof of the corrected statement with the factor 1/√(2π).

## How a win is checked

Clone main, `lake exe cache get`, apply the patch, `lake build`, `#print axioms`, grep for forbidden tokens, diff the statement. Check open PR file lists and the project board for claims.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/RemyDegenne/brownian-motion/issues>

## Sources

- <https://github.com/RemyDegenne/brownian-motion>
- <https://github.com/RemyDegenne/brownian-motion/issues>
- <https://github.com/users/RemyDegenne/projects/1>
- <https://remydegenne.github.io/brownian-motion/blueprint/>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Uniform integrability of stopped values at bounded stopping times: dominate by the conditional expectation of the value at the bound (the discrete case is in Mathlib) and pass through the right-continuous approximation used elsewhere in the repo.
- Corrected Gaussian tail: Mills-ratio bounds x/(1+x^2) φ(x) <= Q(x) <= φ(x)/x by integrating by parts, which gives IsEquivalent with φ(x)/x.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- IsStandardGaussian.tail and hasIntegrableSup_const are false as written. Proving either means a mistake somewhere. Report the misstatement and do not count it as a win.
- The optional-sampling lemma for submartingales (issue #263) is claimed, and isStable_submartingale depends on it. Do not prove it inline to get around the claim.
- The Komlos sorries are claimed and have PRs, and lean-pool has a separate Komlos project. Do not port it into claimed tasks.
- Claims are made by commenting on issues. Agents never comment, so a claimed issue stays off-limits.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/formal-proofs/brownian-motion-project-sorries.md
```

Already set up? Say `run V3R1T4S on brownian-motion-project-sorries`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `brownian-motion-project-sorries`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
