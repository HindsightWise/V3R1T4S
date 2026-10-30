# How We Found It

*contributor text, unverified*

Following Ganzfried and Sandholm (2013), solving 3-player Texas Hold'em Jam/Fold Sit-and-Go tournaments requires solving a coupled 946-state absorbing Markov game.

We computed the complete preflop 2-way equity table across all 169 canonical hand classes by full board enumeration ($1,712,304$ boards). We implemented coupled time-averaged policy iteration / CFR+ in compiled Rust, enforcing authentic poker blind commitment invariants that eliminated artificial short-stack steal oscillations. We evaluated stationary strategy profiles across all 946 nonterminal states under both simultaneous-elimination conventions, driving linear system BiCGSTAB residuals below $10^{-9}$ and achieving certified ex-post exploitability of $0.074891 (Convention ii) and $0.089075 (Convention i).
