# Entanglement-assisted qutrit code `[[33, 3, 20; 18]]_3` (table: `19-30`)

## What

The 48 x 66 GF(3) matrix S in claim/object/eaqecc_33_3_20_18.json (sha256 6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961) has s = 48, c = rank(S J S^T)/2 = 18, k = 3 and exact EA minimum distance d = 20 by exhaustive enumeration of all 3^18 vectors of span(S)^perp, which is strictly above the d_lower = 19 (d_upper = 30) of the cell [[33,3,19-30;18]]_3 on https://eaqecc.codetables.de/qutrit.php as fetched 2026-10-24T23:59:31Z (HTTP 200, sha256 37bbf731030c113e2e2e75fe7b5ed0b1d11829cfc4a5f1ad948a38b1ac7c936c).

Note: the sentence above is quoted word for word from `panel/gate.md` (the CRITERION skeptic's `confirmed_scope`).
The gate re-read the page once more at 2026-10-25T00:13:20Z: same page hash, same cell
(`the-record-we-beat/README.md`). The object's full SHA-256 is
`6df8f7ad262805a139a95fc294196094ee33b78b2fe9e1795c5bc0ba12421961`.

Paths: the sentence is quoted from the panel files, which are shipped unchanged from the contributor's run folder
and use that folder's paths. `claim/object/eaqecc_33_3_20_18.json` is `object/eaqecc_33_3_20_18.json` here (same sha256), and the
panel's `claim/`, `CLAIM.md`, `REPRODUCE.md`, `checkers/` and `rebuild/` are this package's root, `README.md`,
`RUN_IT_YOURSELF.md`, `verify-it-yourself/` and `how-we-built-it/`. The exhaustive enumeration of all 3^18 vectors
that the sentence names was run by the panel's skeptics with their own enumerators (`enum.c` and `enum_n.c` in their
`mine/` folders), which are not shipped; the shipped checks reach d = 20 by other exact methods (see "Check it yourself"). Other files the
panel names (`claim/table/`, `panel/claim.sha256`, `self_break/`, `data/gate_fetch/` and the skeptics' work folders
`mine/`, `author_run/`, `fetched/`, `scripts/`) are not included either; the table record is in
`the-record-we-beat/README.md`.

The code is a Construction X code over GF(9) from two algebraic-geometry codes of the Hermitian curve
`y^3 + y = x^4` whose divisors are supported on a place `Q` of degree 3 and the point at infinity:
`C(D_28, 4Q - P_inf)` `[28, 9, 17]_9` contains `C(D_28, 3Q - P_inf)` `[28, 6, 20]_9`, glued to a `[5, 3, 3]_9`
Reed-Solomon tail, with a column sign pattern chosen so that the Hermitian hull has dimension 6 (the exact maximum
over every Construction X code of this pair). The result is a `[33, 9, 20]_9` code with Hermitian hull 6, which gives
`[[33, 9 - 6, 20; 33 - 9 - 6]]_3 = [[33, 3, 20; 18]]_3`. The object holds the GF(9) generator `G9`, its Hermitian
dual `D9`, and the stabilizer matrix `S = phi(D9)` over GF(3).

## Check it yourself

From this package folder, run:

```sh
sh verify-it-yourself/run_checks.sh
```

- **Requirements:** `python3` (standard library only) and a C compiler (`cc`).
- **Rough laptop time:** about 2 seconds with 3 free cores (2.14 s measured, see `verify-it-yourself/RECEIPTS.md`).
- **Expected last line:** `PASS`

It computes `s`, `c` and `k` from `S`, recovers from `S` the GF(9)-linear `[33, 9]` code `C` with
`phi(C) = span(S)^perp` (so symplectic weight there is Hamming weight on `C`), checks every one of the
818,809,200 sets of 14 coordinates for an information set of `C` (none fails, so every nonzero vector of
`span(S)^perp` has weight at least 20), and checks an explicit weight-20 vector of `span(S)^perp` outside `span(S)`
(so `d <= 20`). It then proves `d >= 20` a second way without any codeword search (`goppa_x.py`: the head and
zero-tail codes are identified exactly as the two AG codes, the Goppa bound gives 17 and 20, and Construction X gives
`min(20, 17 + 3) = 20`). `RUN_IT_YOURSELF.md` has the expected output and more independent exact checks (a GF(3)
position-subset rank test over all 818,809,200 sets of 19 positions and a Brouwer-Zimmermann distance computation).

## Compared to

| table | cell | table value | our value | URL | fetched (UTC) |
|---|---|---|---|---|---|
| Grassl, Bounds on the minimum distance of entanglement-assisted qutrit quantum codes (`Last change: 10.07.2025`) | `(n=33, k=3, c=18)` | `[[33,3,19-30;18]]_3` (`d_lower = 19, d_upper = 30`) | `[[33, 3, 20; 18]]_3` (`d = 20`) | https://eaqecc.codetables.de/qutrit.php | 2026-10-25T00:13:20Z |

Details, HTTP headers, page hash and the listed `(33, 3)` row are in `the-record-we-beat/README.md`.

The classical code behind it is listed but not at this hull: `codetables.de` lists `[33,9]` over GF(9) at 20-23
(construction DNX, the same Construction X of AG codes `[28,9,17] > [28,6,20]` with a `[5,3,3]` tail), and the table's
source paper (arXiv:2207.05647) uses this classical code at Hermitian hull 2, as `[[33,7,20;22]]_3`.
The closure of the table under its own propagation rules, of the codes in this repository's open pull requests
(#405's `[[33,3,23;24]]_3` and #710's `[[33,8,16;15]]_3` included), of this workspace's other codes and of the
newest qutrit EA codes the NOVELTY skeptic found (arXiv:2607.02170, July 2026, length at most 25) gives at most 19 at
this cell. The same row lists `[[33,3,20-30;19]]_3`, so d = 20 was known only with one more entangled pair.

## Not claimed

- Optimality for `(n=33, k=3, c=18)` is not claimed; the table's upper bound is 30.
- Only cell `(n=33, k=3, c=18)` is claimed in this package (one cell per package). Cells that follow from it by the
  table's propagation rules are not claimed here.
- This is an improvement of the table cell, not a new technique: the Hermitian construction, Construction X and AG
  codes from places of higher degree are published. The classical `[33, 9, 20]_9` code is not ours either:
  `codetables.de` lists it (Ding, Niederreiter and Xing). What is new is a version of it with Hermitian hull 6, and
  the qutrit EA code it gives.
- The construction string inside the object says the gluing matrix fills "rows 11..13 of the tail"; for this pair
  the rows are 6..8 of `G9` (a fixed phrase in the builder, checked; no value depends on it).
- The table also has cells marked "using teleportation" (`c = k`). If they were fed into the page's six propagation
  rules this cell would get 27, but the same seeding pushes 2700 listed cells above their own upper bounds, so the
  page does not propagate them; this package follows the page.
- The NOVELTY skeptic read abstracts for most papers (the full text of arXiv:2607.02170); two journal papers
  (Cao-Li-Zhu, IEEE TIT 2025; Liu-Li-Shi, AMC 2025) were judged from the codes arXiv:2607.02170 cites from them, and
  journal papers without an arXiv version may be missed.
- Not yet submitted to or listed by the table maintainer (`eaqecc.codetables.de`).
- Not peer reviewed; verified by a three-skeptic panel (`panel/`) and by the standalone checker in
  `verify-it-yourself/`.

## Credits

- **Markus Grassl**, maintainer of the online EAQECC bounds tables (https://eaqecc.codetables.de/ and
  https://eaqecc.codetables.de/qutrit.php) and `codetables.de` (https://codetables.de/).
- **Gaojun Luo, Martianus Frederic Ezerman, Markus Grassl, and San Ling**, "Constructing quantum error-correcting
  codes that require a variable amount of entanglement", *Quantum Information Processing* 23, 4 (2024),
  https://doi.org/10.1007/s11128-023-04211-x (preprint https://arxiv.org/abs/2207.05647), whose Hermitian
  construction (Proposition 1) turns a GF(9) code with a given Hermitian hull into the qutrit EA code, and whose
  propagation rules the table uses.
- **Todd A. Brun, Igor Devetak, and Min-Hsiu Hsieh**, "Correcting quantum errors with entanglement", *Science* 314,
  436-439 (2006), https://arxiv.org/abs/quant-ph/0610092.
- **Carlos Galindo, Fernando Hernando, Ryutaroh Matsumoto, and Diego Ruano**, "Entanglement-assisted quantum
  error-correcting codes over arbitrary finite fields", *Quantum Information Processing* 18, 116 (2019),
  https://doi.org/10.1007/s11128-019-2234-5 (preprint https://arxiv.org/abs/1812.05312).
- **Cunsheng Ding, Harald Niederreiter, and Chaoping Xing**, "Some new codes from algebraic curves", *IEEE Transactions on Information Theory* 46 (2000)
  2638-2642, https://doi.org/10.1109/18.887873, the reference `codetables.de` gives for its `[33, 9, 20]_9` construction (Construction X with
  algebraic-geometry codes from divisors of degree 3).
- **V. D. Goppa** (algebraic-geometry codes, https://en.wikipedia.org/wiki/Algebraic_geometry_code) and **Henning
  Stichtenoth**, "A note on Hermitian codes over GF(q^2)", *IEEE Transactions on Information Theory* 34 (1988)
  1345-1348, https://doi.org/10.1109/18.21267, whose distance bound
  gives `d >= 28 - deg` for the two AG codes, and **N. J. A. Sloane, S. M. Reddy and C.-L. Chen**, "New binary codes",
  *IEEE Transactions on Information Theory* 18 (1972) 503-510, https://doi.org/10.1109/TIT.1972.1054833 (Construction X).
- **Andries Brouwer and Karl-Heinz Zimmermann**, whose minimum-distance algorithm the bz64 distance check uses (as
  described by Hernando, Igual and Quintana-Orti, https://arxiv.org/abs/1603.06757).
- Contributor credit: Abshalom Dayan, using the V3R1T4S kit (https://github.com/elder-plinius/V3R1T4S).
