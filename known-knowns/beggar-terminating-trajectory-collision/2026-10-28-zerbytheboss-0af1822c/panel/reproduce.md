# Reproduce Skeptic Report — `beggar-terminating-trajectory-collision`

context: subagent (fresh invocation)
target_id: beggar-terminating-trajectory-collision
review_utc: 2026-10-28T18:40:00Z

## Reproduction Audit

1. **Independent Verification of Calibration Controls**:
   - Evaluated equations (7.4)–(7.6) of Andorno et al. (arXiv:2602.23406): confirmed exact non-injectivity step where $s_1 = (\text{dA}=[1,0,0,0,2], \text{dB}=[0,1,0], \text{leader}=A)$ and $s_2 = (\text{dA}=[0,1,0,0], \text{dB}=[2,0,1,0], \text{leader}=A)$ both map under $\mathfrak{F}$ to $(\text{dA}=[0,0,0,2,1,0], \text{dB}=[1,0], \text{leader}=A)$.
   - Evaluated Casella et al. (arXiv:2403.13855) 52-card deal: confirmed that the match enters a periodic orbit at trick 4 that recurs at trick 66 with period 62 tricks. Both Lens 1 (Rust) and Lens 2 (Python) reproduced these calibrations with exact parity.

2. **Verification of the Discovered Collision Witness**:
   - Setting: $(N, \mathfrak{R}) = (16, 2)$ (16 cards: four 1s, four 2s, eight 0s).
   - Initial Deal 1: $s_1 = (\text{dA}=[0,0,2,1,0,2,1,2], \text{dB}=[1,0,1,2,0,0,0,0], \text{leader}=A)$. Balanced ($8$ cards each), exact multiset $\{0: 8, 1: 4, 2: 4\}$.
   - Initial Deal 2: $s_2 = (\text{dA}=[0,0,0,2,1,0,2,1], \text{dB}=[1,2,1,2,0,0,0,0], \text{leader}=A)$. Balanced ($8$ cards each), exact multiset $\{0: 8, 1: 4, 2: 4\}$.
   - Separation: $s_1 \ne s_2$. Neither deal lies on the trajectory of the other.
   - Trick 1 from $s_1$ yields state $x = (\text{dA}=[2,1,0,2,1,2], \text{dB}=[0,1,2,0,0,0,0,0,1,0], \text{leader}=B)$.
   - Trick 1 from $s_2$ yields state $y = (\text{dA}=[0,2,1,0,2,1], \text{dB}=[2,1,2,0,0,0,0,0,1,0], \text{leader}=B)$.
   - States $x$ and $y$ are distinct ($x \ne y$) and both are playable non-terminal states ($|L_x|=6, |R_x|=10$; $|L_y|=6, |R_y|=10$).
   - Trick 2 from state $x$ executes 9 plays and results in $z = (\text{dA}=[1,2,0,2,1,1,2,0,2,0,0], \text{dB}=[0,0,0,1,0], \text{leader}=A)$.
   - Trick 2 from state $y$ executes 10 plays and results in the exact same state $z = (\text{dA}=[1,2,0,2,1,1,2,0,2,0,0], \text{dB}=[0,0,0,1,0], \text{leader}=A)$.
   - Thus $\mathfrak{F}(x) = \mathfrak{F}(y) = z$.

3. **Verification of Continuation to Termination**:
   - Suffix Trick 1: moves `[(A,1),(B,0)]` -> Player A wins pile `[1,0]`. State: `(dA=[2,0,2,1,1,2,0,2,0,0,1,0], dB=[0,0,1,0], leader=A)`.
   - Suffix Trick 2: moves `[(A,2),(B,0),(B,0)]` -> Player A wins pile `[2,0,0]`. State: `(dA=[0,2,1,1,2,0,2,0,0,1,0,2,0,0], dB=[1,0], leader=A)`.
   - Suffix Trick 3: moves `[(A,0),(B,1),(A,2),(B,0)]` -> Player B fails to supply required 2nd card; Player A wins all cards.
   - Final state: Player B has 0 cards, Player A has all 16 cards.
   - Total match length from start: exactly 5 tricks (2 to collision + 3 suffix tricks).
   - Match legally terminates without entering any loop.

pass: true
