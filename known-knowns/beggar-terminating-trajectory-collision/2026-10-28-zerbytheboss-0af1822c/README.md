# Beggar-My-Neighbour Terminating Trajectory Collision Witness

## What

Two valid, distinct balanced initial deals in the legal (N,R)=(16,2) Beggar-My-Neighbour setting reaching distinct playable trick-boundary states x!=y on disjoint orbits such that F(x)=F(y)=z and the common continuation from z legally terminates after 3 tricks (5 tricks total from start), proving non-injectivity of F on terminating trajectories.

## Check It Yourself

Run the standalone verification suite:
```bash
sh verify-it-yourself/run_checks.sh
```
This recomputes every trick transition from the initial balanced deals, checks all multiset card conservation laws, confirms the predecessor separation x != y, verifies the exact collision F(x) == F(y) == z, and replays the 3-trick continuation to legal termination where Player A collects all 16 cards.

## Compared To

In Nicolas Andorno, Giulio Cernoia, Simone Duiz, and Alessandro Michelangeli, "The Dynamical Landscape of Beggar-My-Neighbour: Ultra-long Matches, Loops, and Infinite Matches" (arXiv:2602.23406 v2, 2 Jul 2026), Section 13, the authors explicitly ask:
> "Specifically, determine whether injectivity is lost only when a trajectory enters a loop, or also when two distinct trajectories merge and proceed to termination."

All previous non-injective transitions documented in the literature led into infinite periodic orbits. This work establishes the first explicit, certified mathematical witness of merging trajectories that proceed to finite termination.

## Not Claimed

- We do not claim an exhaustive classification of all terminating collisions in Beggar-My-Neighbour.
- We do not claim a terminating collision witness in the standard (52, 4) setting; our witness is in the legal four-suit (N, R) = (16, 2) setting from the paper's defined game family.
- We do not claim an analytical proof of the asymptotic density of terminating collisions.

## Credits

- Nicolas Andorno, Giulio Cernoia, Simone Duiz, and Alessandro Michelangeli for formulating the dynamical landscape and Section 13 open question of Beggar-My-Neighbour (arXiv:2602.23406).
- Casella et al. for the discovery of the first non-terminating Beggar-My-Neighbour game (arXiv:2403.13855, Amer. Math. Monthly 2025).
