# Hex 10x10: solve a second opening move (only the central f5/e6 pair is solved, since 2013)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (the one solved 10x10 opening, f5, took about 64 days of Scalable Parallel DFPN search in 2012-2013; the hardest 9x9 opening, a6, took 111 days); an edge opening with a short refutation could fall in laptop-days with a modern neural-guided solver · open as of 2026-10-30

## The problem

Hex on an n x n rhombus (Black connects top-bottom, White left-right, no draws possible; first-player win by strategy stealing, played here without the swap rule). Computer solutions of single opening moves: all 8x8 openings by Henderson, Arneson and Hayward (IJCAI 2009); all 9x9 openings by Jakub Pawlewicz and Ryan Hayward's Scalable Parallel DFPN in Benzene (finished April 2012, published Computers and Games 2013; the hardest opening, a6, took 111 days); and on 10x10 exactly one opening, the centremost f5 (Black wins, 63 days), which by the board's 180-degree symmetry also settles e6. Hayward's Hex page (last modified January 2022) records 'Mar 2013: Solver shows centre wins on 10x10' and no later 10x10 result. Wikipedia's Hex article says one (the most central) 10x10 opening was solved in 2013. Xinyue Chen's 2025 University of Alberta MSc thesis still summarizes the state as all 9x9 first moves and 2 winning 10x10 first moves [PH13]. Randall, Mueller, Wei and Hayward's Expected Work Search (IJCAI 2024) says Hex has been solved up to the 10x10 board and reports no new 10x10 opening. The 10x10 board has 100 opening cells in 50 classes under 180-degree rotation. No class other than {f5, e6} has a published computer solution. Published general results on inferior edge cells may already settle some first-row openings, so check before claiming one. Task: determine the outcome (Black stone on the opening cell, White to move, no swap) of any other 10x10 opening. Status checked 2026-10-30 on Hayward's Hex page, the Wikipedia Hex article and the 2025 thesis.

## What counts as a win

CONFIRMED: for an opening cell X on the 10x10 Hex board, not in the 180-degree symmetry class {f5, e6} and not reported solved by Hayward's group or in the literature at verification time, a solution tree proving the outcome of the position 'Black stone on X, White to move' (no swap). Every node where the winning side moves names one move; every node where the losing side moves lists all legal moves, except moves removed by inferior-cell or fill-in rules only if each such rule is a published theorem (cite it) and the checker re-applies it from its stated pattern. Each leaf must be a completed connection or a virtual connection (a second-player connection strategy on a stated carrier) that the checker proves by exhaustive search on that carrier. The tree must be accepted by a checker written independently of the solver that produced it (sharing no code with Benzene or the solver used), with its own move generator and connection test.

## Partial wins

- **p1:** An independent re-verification of the 2013 10x10 f5 result, or of the 9x9 opening a6 (the hardest of the 2012 batch, 111 days), by a solver sharing no code with Benzene, with the solution tree accepted by an independent checker as in the success criterion.
- **p2:** The outcome of a 10x10 Hex position after two moves (an opening X other than f5/e6, then a White reply Y), certified as in the success criterion. Y must be the reply ranked first for White after X by a named, publicly available engine build (for example MoHex from Benzene, or KataHex) at stated settings, with the engine run log published so the verifier can reproduce the ranking.

## How a win is checked

Rebuild the checker from source and test it on small boards (all 1-move openings on 6x6 and 7x7, whose values are published). Then walk the submitted tree: at each losing-side node regenerate all legal moves and subtract only cells covered by a cited, re-verified pruning pattern; at each winning-side node check the named move is legal; verify every virtual-connection leaf by exhaustive search over its carrier; check that the root position is the claimed opening and that no swap move is used. Compare the outcome with an independent strong engine as a sanity check (an engine evaluation is not proof).

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://sites.ualberta.ca/~hayward/hex/>

## Sources

- <https://sites.ualberta.ca/~hayward/hex/>
- <https://sites.ualberta.ca/~hayward/papers/pawlhayw.pdf>
- <https://sites.ualberta.ca/~hayward/theses/xinyue.pdf>
- <https://sites.ualberta.ca/~hayward/papers/ews.pdf>
- <https://en.wikipedia.org/wiki/Hex_(board_game)>
- <https://github.com/cgao3/benzene-vanilla-cmake>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Corner and edge openings on large boards are widely believed to lose for Black. Proving a loss needs one White reply plus a full tree, and some obtuse-corner or edge-adjacent openings may have short refutations built from edge templates.
- Gao, Mueller and Hayward's focused DFPN with a convolutional net (IJCAI 2017) and Expected Work Search (IJCAI 2024) both cut proof effort; a modern GPU-trained policy can order moves inside a parallel DFPN.
- Reuse Benzene's fill-in, inferior-cell and virtual-connection machinery for search, but export the tree in a plain format for an independent checker.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The 2013 paper counts one solved 10x10 opening (f5); later summaries say two, because e6 is its 180-degree image. Do not count e6 as new.
- Swap-rule Hex is a different question. The criterion is the no-swap value of the stated opening.
- Pruning by mustplay, dead cells and captured cells is sound only for the theorems that prove it; a home-made pattern without proof invalidates the tree.
- Some first-row and edge openings may already be settled for all board sizes by published inferior-cell or edge-template theorems (Henderson and Hayward's papers, the book Hex, Inside and Out). Check before claiming an edge opening.
- Hayward's Hex page was last modified in January 2022; also check recent Alberta theses and papers before claiming.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/hex-10x10-opening-moves.md
```

Already set up? Say `run V3R1T4S on hex-10x10-opening-moves`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `hex-10x10-opening-moves`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
