# Andrews-Curtis: an AC-trivialisation of AK(3), or of one of the last two open length-14 Miller-Schupp classes

🃏 **Wildcard** · moonshot (famous, long odds) · tractability ★★☆☆☆ · compute: laptop-days (search over balanced presentations; RL or breadth-first search with supermoves) · open as of 2026-10-30

## The problem

The Andrews-Curtis conjecture says every balanced presentation of the trivial group reduces to <x,y|x,y> by AC moves: inverting a relator, multiplying one relator by another, and conjugating a relator by a generator. AK(n) = <x,y | x^n = y^(n+1), xyx = yxy> (Akbulut and Kirby, 1985) has total relator length 2n+7. AK(3), of length 13, is the shortest potential counterexample: balanced trivial-group presentations of length <= 12 are AC-trivial (Miasnikov-Myasnikov), and those of length 13 are AC-trivial or AC-equivalent to AK(3) (Havas-Ramsay), as summarised by Carreras (2026). Shehper, Medina-Mardones, Fagan, Lewandowski, Gruen, Qiu, Kucharski, Wang and Gukov (arXiv 2408.15332, v2 Feb 2025) showed AK(3) is stably AC-trivial (re-derived by Lisitsa, arXiv 2501.18601); the unstable question is open. Their Miller-Schupp study (MS(n,w) = <x,y | x^-1 y^n x = y^(n+1), x = w > ) left six hard length-14 presentations, four of which they asserted without proof to be AC-equivalent to AK(3). Carreras (arXiv 2607.23611, v1 July 2026) gave the first explicit certificates for the two MS(3) ones, MS(3, y x^2 y) and MS(3, y^-1 x^2 y^-1). He also linked the two MS(2) holdouts, MS(2, y x^2 y x^-2) and MS(2, y x^2 y^-1 x^-2), to the uncertified MS(2, x^-2 y^-1 x^2 y) and MS(2, x^-2 y^-1 x^2 y^-1) via the automorphism y -> y^-1, and related the classical candidate <x,y | x^-1 y^2 x = y^3, y^-1 x^2 y = x^3> to them. None of these MS(2) presentations is certified AC-trivial or AC-equivalent to AK(3). Fagan et al. (ICML 2026, arXiv 2606.21611) released the AC-19 and AC-1M datasets of solved instances.

## What counts as a win

Success means an explicit finite sequence of elementary AC moves (r_i -> r_i^-1; r_i -> r_i r_j with i != j; r_i -> g^±1 r_i g^∓1 for a generator g; free reduction allowed) that starts at AK(3) = <x,y | x^3 y^-4, xyx y^-1 x^-1 y^-1> and ends at <x,y | x, y> (up to relabelling and inverting relators). An independent free-group replayer must check it. A machine-checked proof (Lean, Coq or Isabelle) that AK(3) is NOT AC-trivial also counts. A trivialisation of AK(3) through stabilisation (adding generators) does not count, because that is already known.

## Partial wins

- **p1:** An elementary AC-move certificate that takes any of MS(2, y x^2 y x^-2), MS(2, y x^2 y^-1 x^-2), MS(2, x^-2 y^-1 x^2 y) or MS(2, x^-2 y^-1 x^2 y^-1) (Carreras 2026 notation) to the trivial presentation <x,y | x, y > .
- **p2:** An elementary AC-move certificate that one of those four MS(2) presentations is AC-equivalent to AK(3), certifying the Shehper et al. assertion for the MS(2) branch of the length-14 collapse.
- **p3:** An elementary AC-move trivialisation of AK(4) = <x,y | x^4 = y^5, xyx = yxy> or of any AK(n) with n >= 4.

## How a win is checked

Replay the move list with a small free-group word library: apply each move, freely reduce, and confirm the final pair is (x, y) up to inversion and order, or reaches the stated target presentation up to cyclic permutation and inversion of relators. Carreras's paper ships a dependency-free Python replayer that can serve as a second implementation. Also confirm the starting presentation is exactly AK(3) (or the named MS presentation).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2607.23611>

## Sources

- <https://arxiv.org/abs/2607.23611>
- <https://arxiv.org/abs/2408.15332>
- <https://arxiv.org/abs/2501.18601>
- <https://arxiv.org/abs/2606.21611>
- <https://github.com/shehper/AC-Solver>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Start from Carreras's MS(3) certificates (13 and 66 packaged moves) as entry points into the AK(3) class. His exhaustive GS-substitution-graph searches show any GS path from MS(2, x^-2 y^-1 x^2 y) or MS(2, x^-2 y^-1 x^2 y^-1) to AK(3) must reach total relator length 27 or more, so search above that bottleneck or use multiplications the GS generator omits.
- Use the AC-1M 'hard but solvable' data to train a policy with supermoves, then run it on the AK(3) class with a large length cap.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A stable trivialisation (extra generators) is already known and does not count.
- Carreras's 19 and 27 bottleneck results apply only to his GS substitution graph and to specific representatives. They are not AC-distance lower bounds and prove nothing about non-triviality.
- Carreras's preprint is v1 and not peer reviewed; re-run its certificates with an independent replayer before building on them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/andrews-curtis-ak3-trivialisation.md
```

Already set up? Say `run V3R1T4S on andrews-curtis-ak3-trivialisation`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `andrews-curtis-ak3-trivialisation`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
