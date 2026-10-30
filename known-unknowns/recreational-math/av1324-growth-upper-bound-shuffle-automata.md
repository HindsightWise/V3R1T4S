# Stanley-Wilf limit of 1324: a certified upper bound below Brignall's 13.167248 (shuffle-automaton certificates)

🎲 **Recreational math** · standard · tractability ★★★☆☆ · compute: laptop-hours to laptop-days (thousands of states and tens of thousands of exact polynomial inequalities; the weight search is numerical optimisation, the check is exact arithmetic) · open as of 2026-10-30

## The problem

The growth rate gr(Av(1324)) = lim |Av_n(1324)|^(1/n) is the last unknown Stanley-Wilf limit of a length-4 pattern. Upper bounds: 16 (Claesson-Jelinek-Steingrimsson 2012), about 13.93 and 13.74 (Miklos Bona 2012, 2014), 13.5 (David Bevan, Robert Brignall, Andrew Elvey Price, Jay Pantone 2020, via dominoes) and, since 1 Oct 2026, 13.167248 (Robert Brignall, 'Shuffle automata and the growth of 1324-avoiding permutations', arXiv:2610.02535 v1, the only version on 2026-10-30). Brignall bounds gr(Av(1324)) <= lambda * mu(x, y) whenever a weighted shuffle automaton for the BR-avoiding shuffles of domino words admits a lambda-good positive state weighting (Proposition 4.4, from Corollary 4.3 and Proposition 4.2); mu(x, y) is the domino growth rate, the reciprocal of the root of a cubic functional equation (Theorem 3.4). His 3-lookahead automaton (384 states, 1536 inequalities, weights in 139 polynomials of a root t ~ 1.1584233 of 3T^5 + 10T^4 - T^3 - 11T^2 - 6T - 1) gives (1+t)(19+8t)/(4t) ~ 13.1672476; the finite inequalities are Lean-checked in github.com/rbrignall/1324-lookahead. His concluding remarks report unverified larger runs: a 5-lookahead automaton near 13.1498 (6144 states, 24,576 inequalities) and an enlarged-alphabet 3-lookahead near 13.143 (over 13,000 states). Neither has been certified. The best numerical estimate of the true value is 11.600 +- 0.003 (Conway-Guttmann-Zinn-Justin 2018); the best claimed lower bound, 10.412263 (Charles Norton, arXiv:2608.20292 v3, after two withdrawn claims), is not part of this target.

## What counts as a win

Success means a rigorous upper bound U < 13.167248 (strictly smaller, direction: min) on gr(Av(1324)), delivered as either (a) a certificate inside Brignall's framework of arXiv:2610.02535: an explicit finite weighted shuffle automaton (for example the k-lookahead automaton of Section 5 for some k >= 4, or the enlarged-alphabet variant of the concluding remarks) shown to meet the hypotheses of Corollary 4.3, explicit parameters x, y, lambda (exact algebraic numbers with isolating intervals), an explicit positive state weighting, and a checker in exact rational or certified interval arithmetic (or Lean) that verifies positivity and every lambda-good inequality, together with a certified enclosure of lambda * mu(x, y) below 13.167248; or (b) a kernel-checked formal proof (Lean, Rocq or Isabelle, with no sorry or extra axioms) of any bound below 13.167248. Floating-point checks, unverified optimiser output, or a bound conditional on the Claesson-Jelinek-Steingrimsson conjecture do not count. Before claiming, re-check arXiv:2610.02535 for a later version and search arXiv for a newer bound.

## Partial wins

- **p1:** An independent exact re-verification of Brignall's 3-lookahead certificate outside Lean (all 384 weights positive and all 1536 inequalities at the root t of m(T)), plus a Sturm-sequence or interval certificate that m(T) has exactly one root in (1.158423, 1.158424), with the automaton regenerated from the paper's definitions rather than copied from the repository CSV.
- **p2:** A certified bound from a 4-lookahead automaton (the next case after Brignall's 3-lookahead; arXiv:2610.02535 reports no k = 4 value), checked in exact arithmetic as in (a), whose certified value of lambda * mu(x, y) is at most 13.1673 (no worse than Brignall's 13.1672476 to four decimals), together with its exact closed form; a value below 13.167248 is the full win.

## How a win is checked

Run the claimant's checker in a clean environment: regenerate the automaton from the definitions in arXiv:2610.02535 Sections 4-5 (states, active transitions, run weights x^-i y^-r), confirm it reproduces Brignall's 384-state 3-lookahead case and his 13.1672476 bound, then check every inequality sum over active transitions tau(e) kappa(q_e) <= lambda kappa(q) exactly (rational arithmetic in Q(t) with a root-isolating interval, or a Lean build with an axiom audit). Separately compute mu(x, y) as 1/rho where rho is the unique zero of Phi(z; x, y) in (0, 1/2) using certified root isolation, and confirm lambda * mu < 13.167248. Any step that relies on numerical optimisation must only produce the weights; acceptance depends only on the exact check.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.02535>

## Sources

- <https://arxiv.org/abs/2610.02535>
- <https://github.com/rbrignall/1324-lookahead>
- <https://arxiv.org/abs/1711.10325>
- <https://arxiv.org/abs/1709.01248>
- <https://oeis.org/A061552>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Brignall's own pointers: the 5-lookahead (~13.1498) and enlarged-alphabet (~13.143) runs only need certification; set up exact LP feasibility for the weights at a fixed rational lambda slightly above the target, then round to rationals and re-check.
- Treat the lambda-good weighting as a Perron-eigenvector problem: lambda is at least the spectral radius of the weighted transfer matrix, so power iteration gives near-optimal weights quickly; certification then needs only rational rounding with slack.
- Use rational x, y and a rational lambda instead of algebraic parameters: a slightly worse but fully rational certificate is far easier to check and still counts if below 13.167248.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The bound is lambda * mu(x, y), not lambda alone; changing x and y changes both the run weights and the domino growth rate, so mu must be recomputed with a certified root of the domino equation at those parameters.
- Brignall notes that the naive and six-state automata give exactly 13.5 with no gain; a new automaton must still be in bijection with BR-avoiding shuffles (Corollary 4.3 hypothesis), which a checker of inequalities alone does not test.
- The 13.1498 and 13.143 values in the concluding remarks were reported as unverified ChatGPT-assisted computations; reproducing them numerically is not a win.
- Norton's lower-bound preprint has withdrawn earlier versions; do not use any lower bound as a sanity check beyond 10.271 (Bevan et al. 2020).

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/av1324-growth-upper-bound-shuffle-automata.md
```

Already set up? Say `run V3R1T4S on av1324-growth-upper-bound-shuffle-automata`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `av1324-growth-upper-bound-shuffle-automata`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
