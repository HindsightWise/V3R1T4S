# Polycube trees and edge-unzipping: a polycube tree with no edge zipper unfolding, or certified unzippings of all small ones (Demaine-Demaine-Eppstein-O'Rourke Question 1)

🎲 **Recreational math** · standard · tractability ★★★☆☆ · compute: laptop-hours (Hamiltonian-path enumeration on small surfaces; integer-exact overlap tests) · open as of 2026-10-30

## The problem

An edge zipper unfolding (edge-unzipping, Shephard's Hamiltonian unfolding) cuts a polycube surface along a single simple path of cube edges that visits every non-flat vertex and may pass through flat ones, and unfolds it to one weakly simple polygon. Demaine, Demaine, Eppstein and O'Rourke ('Some polycubes have no edge zipper unfolding', CCCG 2020, Geombinatorics XXXI(3) 2022, arXiv 1907.08433) built polycubes with no edge-unzipping by forcing the absence of a suitable Hamiltonian path (parity arguments on the 1-skeleton). They proved (their Lemma 1) that for a single cube and for every polycube tree (cube-adjacency graph a tree) the whole 1-skeleton, flat vertices included, has a Hamiltonian cycle, so their method does not apply to trees. Their closing open problem, Question 1, asks: does every polycube tree have an edge zipper unfolding? O'Rourke's 2019 survey table lists polycube edge-unzipping as negative in general, and the GFALOP update 22.5 (Sep 2025) still cites the 2022 paper as the state of the art.

## What counts as a win

Either (a) a COUNTEREXAMPLE: a polycube tree (unit cubes glued face to face, cube-adjacency graph a tree, boundary a 2-manifold), plus a complete certificate that every simple cut path along surface cube edges containing all non-flat vertices unfolds with two unit squares in the same lattice cell. The certificate is an exhaustive path enumeration reproduced by two independent implementations, or a SAT encoding with a checked DRAT or LRAT UNSAT proof plus an independent second encoding. Or (b) a machine-checked proof (Lean 4, Coq or Isabelle) that every polycube tree has an edge zipper unfolding. In both cases, literature check at claim time.

## Partial wins

- **p1:** A certified census: for every polycube tree with n <= N cubes, up to rotation and reflection, an explicit edge-unzipping (cut path plus lattice net) checked by an independent verifier, for N >= 12 and beyond any published census (literature check required).
- **p2:** A genus-0 polycube that is not a tree, whose corner vertices DO admit a Hamiltonian cut path along surface edges, yet has no edge-unzipping because every such path overlaps. Certified exhaustively. Prior negative examples work by ruling out Hamiltonian paths altogether.

## How a win is checked

Rebuild the surface, check the tree property and manifoldness, enumerate the admissible cut paths (or check the DRAT or LRAT proof and the second encoding), and unfold each path on Z^2 with integer arithmetic, testing for cell collisions. For p1, check each net and its refolding, and the completeness of the enumeration of polycube trees of each size.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1907.08433>

## Sources

- <https://arxiv.org/abs/1907.08433>
- <https://erikdemaine.org/papers/PolycubeZipper_CCCG2020/paper.pdf>
- <https://www.gfalop.org/updates/22.5.pdf>
- <https://arxiv.org/abs/1908.07152>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Long thin polycube trees with many branch points ('crosses' and 'combs') constrain the path most; their paper's P+ cross gadget is a natural seed.
- Encode path plus positions in SAT. Because positions are integral, the whole check is finite and exact.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A cut path must include every non-flat vertex; flat vertices are optional. Getting this wrong changes the answer.
- Weakly simple nets (touching boundaries) count as unzippings.
- The polycube must be a tree in the cube-adjacency sense, not just genus 0.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/recreational-math/polycube-tree-edge-unzipping.md
```

Already set up? Say `run V3R1T4S on polycube-tree-edge-unzipping`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `polycube-tree-edge-unzipping`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
