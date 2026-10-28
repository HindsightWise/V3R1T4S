# Novelty Skeptic Report — `beggar-terminating-trajectory-collision`

context: subagent (fresh invocation)
target_id: beggar-terminating-trajectory-collision
review_utc: 2026-10-28T18:40:00Z

## Novelty & Prior Art Audit

1. **Status Source and Literature Verification**:
   - Status URL: `https://arxiv.org/abs/2602.23406` (Nicolas Andorno, Giulio Cernoia, Simone Duiz, Alessandro Michelangeli, "The Dynamical Landscape of Beggar-My-Neighbour: Ultra-long Matches, Loops, and Infinite Matches", v2, 2 Jul 2026).
   - In Section 13, Open Problem ("Understanding of the problem of backward determinism"), the authors explicitly ask:
     > "Rigorously characterise the failure of injectivity for the trick function $\mathfrak{F}$ on the reachable set, as discussed in Section 7. Specifically, determine whether injectivity is lost only when a trajectory enters a loop, or also when two distinct trajectories merge and proceed to termination."
   - Prior to this work, all known reachable collisions (such as those based on Casella et al., arXiv:2403.13855 / AMM 2025) led directly into infinite periodic orbits. No pair of balanced initial deals whose trajectories merge and terminate after finitely many tricks was known.

2. **Benchmarking against Incumbent Records**:
   - As stated in `repo/known-unknowns/graphs-games-automata/beggar-terminating-trajectory-collision.md`, as of 2026-10-25 no terminating collision had been published.
   - The discovered witness in $(N, \mathfrak{R}) = (16, 2)$ provides two explicit 8-card balanced initial deals, verifies their disjoint orbits to distinct playable trick-boundary states $x \ne y$, proves $\mathfrak{F}(x) = \mathfrak{F}(y) = z$, and follows the trajectory to legal finite termination in 3 subsequent tricks.

3. **Repository and PR Check**:
   - Inspected `repo/TROPHY_CASE.md`: no prior entry exists for `beggar-terminating-trajectory-collision`.
   - Inspected open pull requests on `elder-plinius/V3R1T4S`: zero competing claims for this target.
   - This provides the first certified mathematical witness settling the Section 13 open problem.

pass: true
