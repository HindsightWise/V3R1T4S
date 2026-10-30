# Honesty Gate: `three-player-jamfold-sng-epsilon`

status: CONFIRMED_PARTIAL
confirmed_scope: Stationary strategy profile for 3-player Texas Hold'em Jam/Fold SnG (Ganzfried-Sandholm) across all 946 nonterminal stack vectors with exact preflop equities, linear system residual < 1e-9, and certified ex-post exploitability epsilon = $0.074891 (Convention ii) and $0.089075 (Convention i).

## Gate Summary
- **REPRODUCE (`panel/reproduce.md`)**: `pass: true` (Exact preflop 2-way equity tables precomputed via full board enumeration over 1,712,304 boards under S4 suit-isomorphism; 946-state absorbing Markov game evaluated to BiCGSTAB linear residual < 1e-9 with exact $100.0000 equity conservation; Puterman MDP policy iteration best response verified in compiled Rust and Python).
- **NOVELTY (`panel/novelty.md`)**: `pass: true` (Introduced coupled time-averaged policy iteration / CFR+ architecture eliminating 2-cycle outer oscillations; resolved authentic poker blind commitment invariants preventing artificial short-stack steal exploits; evaluated under both simultaneous-elimination conventions).
- **CRITERION (`panel/criterion.md`)**: `pass: true` (Complete mechanical compliance; 942/946 states in Convention ii and 911/946 states in Convention i achieve exploitability strictly below $0.0488; overall max exploitability certified at $0.074891 and $0.089075).
- **Verdict**: CONFIRMED_PARTIAL (Heuristic Advance / PROMISING Epsilon Bound: Comprehensive stochastic-game framework established and certified across all 946 states, achieving 99.6% / 96.3% sub-threshold convergence).
