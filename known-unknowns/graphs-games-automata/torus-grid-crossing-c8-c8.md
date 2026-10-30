# Harary-Kainen-Schwenk conjecture: is cr(C_8 x C_8) = 48? (smallest open toroidal grid)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: laptop-days (exact ILP/SAT lower-bound search); pure thought for a structural proof · open as of 2026-10-30

## The problem

Harary, Kainen and Schwenk (1973) conjectured that the Cartesian product of cycles has cr(C_m x C_n) = (m-2)n for 3 <= m <= n. It is proved for m <= 7: Ringeisen-Beineke for m = 3, Beineke-Ringeisen and Dean-Richter for m = 4, Richter-Thomassen and Klešč-Richter-Stobert for m = 5, Anderson-Richter-Rodney and Richter-Salazar for m = 6, Anderson et al. and Adamsson-Richter for m = 7. Glebsky and Salazar (JGT 2004) proved it for all n >= m(m+1). Adamsson and Richter sketched that m = 8 follows for every n once cr(C_8 x C_8) = 48 is shown. As of the Clancy-Haythorpe-Newcombe dynamic survey (arXiv 1901.05155 v5, Dec 2021), cr(C_8 x C_8) is open. The standard drawing gives 48. The best published lower bound that applies seems to be Shahrokhi et al. (1998), cr(C_m x C_n) >= 3mn/5 for n <= 5(m-1)/4, which gives 39. Our own arithmetic: deleting the 8 edges of any one of the 16 C_8-cycles leaves a subdivision of C_7 x C_8 (crossing number 40), and each crossing of a good drawing is lost in at least one of the 16 deletions, so 15 cr >= 16 * 40 and cr(C_8 x C_8) >= 43. An unrefereed Zenodo preprint (Q. Gu, 'The Crossing Number of C_8 x C_8', concept DOI 10.5281/zenodo.22162314, issued 2026-08-29, prepared with ChatGPT and stated not to be peer reviewed) claims cr(C_8 x C_8) = 48 by a reduction of a hypothetical 47-crossing drawing to weighted subcubic intersection graphs. On 2026-10-30 its version record returned HTTP 410 Gone. No refereed or machine-checked proof is known. Credit: Harary-Kainen-Schwenk, Richter, Salazar, Adamsson, Glebsky, Anderson, Klešč, Shahrokhi et al., and the survey authors.

## What counts as a win

Either (A) a planarization of a drawing of C_8 x C_8 with at most 47 crossings, certified planar by two independent testers, which disproves the conjecture at its smallest open case (and Gu's 2026 preprint claim); or (B) a proof that cr(C_8 x C_8) >= 48, formalised in a proof assistant or given as an exact crossing-number certificate (for example an ILP/SAT encoding over planarizations or Kuratowski constraints, with a checked proof log and an independently re-derived encoding). A human-readable argument alone, including a re-statement of Gu's preprint, does not count for (B). Before claiming, re-fetch the Clancy-Haythorpe-Newcombe survey (https://arxiv.org/abs/1901.05155, latest version), check the status of Gu's Zenodo preprint (doi 10.5281/zenodo.22162314) and search for papers after 2021 to confirm that no refereed or machine-checked proof has appeared.

## Partial wins

- **p1:** A certified lower bound cr(C_8 x C_8) >= L for some L >= 44 (strictly above 43, the bound from counting the 16 cycle deletions to C_7 x C_8) and strictly above any bound found by a fresh literature search, to the certificate standards of (B): a formal proof, or an exact ILP/SAT crossing-number certificate with a checked DRAT/LRAT/VeriPB log and an independently re-derived encoding.
- **p2:** A certified lower bound cr(C_8 x C_8) >= 46, to the same certificate standards as (B).

## How a win is checked

(A) Check that the planarization's edge paths reproduce the 128 edges of C_8 x C_8 and that the graph is planar (two testers plus an Euler check), then count dummies. (B, p1, p2) Regenerate the encoding from the written reduction, check the DRAT/LRAT/VeriPB log, and reproduce known values (cr(C_6 x C_6) = 24, cr(C_7 x C_7) = 35) with the same pipeline as a sanity test.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/1901.05155>

## Sources

- <https://arxiv.org/abs/1901.05155>
- <https://en.wikipedia.org/wiki/Crossing_number_(graph_theory)>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The m <= 7 proofs rest on case analyses of how the 'tight' cycles cross; encode those lemmas as constraints to prune an exact ILP for C_8 x C_8.
- Use the 16-fold rotational symmetry of the torus grid to break symmetry in a SAT search for a 47-crossing planarization.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- C_m x C_n here is the Cartesian product (the toroidal grid), not the strong or direct product.
- Exact crossing-number ILP solvers are reliable only with proof logging; a bare 'optimal' from a MIP solver is not a certificate.
- The cycle-deletion count already gives cr(C_8 x C_8) >= 43 by hand from cr(C_7 x C_8) = 40; bounds of 43 or less are not wins.
- Gu's August 2026 Zenodo preprint claims the full value 48 (unrefereed, AI-assisted; its record returned HTTP 410 Gone on 2026-10-30 and could not be read). A (B) win must be a formal or certified proof, not a restatement of that argument; check whether a revised or refereed version has appeared.
- On 2026-10-30 the survey (v5, 2021), Balko's Harary-Hill exposition (arXiv 2610.34444) and web, Crossref and DataCite searches were checked; apart from Gu's preprint nothing on C_8 x C_n after 2021 was found. Search again before attacking.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/torus-grid-crossing-c8-c8.md
```

Already set up? Say `run V3R1T4S on torus-grid-crossing-c8-c8`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `torus-grid-crossing-c8-c8`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
