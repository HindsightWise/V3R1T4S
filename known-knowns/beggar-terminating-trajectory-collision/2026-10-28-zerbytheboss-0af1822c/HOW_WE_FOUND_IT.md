# How We Found It — `beggar-terminating-trajectory-collision`

contributor text, unverified

We formulated the problem of discovering a terminating collision in Beggar-My-Neighbour based on the open challenge in Section 13 of Nicolas Andorno, Giulio Cernoia, Simone Duiz, and Alessandro Michelangeli, "The Dynamical Landscape of Beggar-My-Neighbour: Ultra-long Matches, Loops, and Infinite Matches" (arXiv:2602.23406 v2, 2 Jul 2026).

Section 13 explicitly asks whether backward determinism / injectivity of the trick transition map F on reachable states is lost only when entering infinite loops, or also on trajectories that merge and proceed to finite termination.

To answer this:
1. We targeted the legal small four-suit setting (N, R) = (16, 2) (16 cards: four 1s, four 2s, eight 0s, 8 cards per player), as permitted and encouraged by the authors.
2. We built two independent simulation and state-exploration engines: a high-throughput compiled Rust engine and a pure Python engine.
3. We calibrated against equations (7.4)–(7.6) of Andorno et al. (confirming trick-boundary non-injectivity) and against the 52-card infinite loop of Casella et al. (arXiv:2403.13855, period 62 loop at trick 4).
4. By screening forward trajectories from balanced initial deals with Player A leading, we isolated two distinct initial deals s1 != s2 whose first tricks yield distinct playable nonterminal trick states x != y.
5. In trick 2, both x and y transition to the exact same successor state z = F(x) = F(y) = (dA=[1,2,0,2,1,1,2,0,2,0,0], dB=[0,0,0,1,0], leader=A).
6. From z, the game legally terminates in exactly 3 suffix tricks with Player A accumulating all 16 cards and Player B holding 0 cards.
7. This gives an exact, certified, finite witness resolving Section 13.
