# Fejes Toth problem: N points on the unit sphere whose convex hull has larger volume than the best known (Hardin-Sloane-Smith and Deeter tables, N = 10..130 except 12)

⚪ **Packings and physics** · harvest (many cells or partial wins within reach) · tractability ★★☆☆☆ · compute: laptop-hours · open as of 2026-10-30

## The problem

Maximise the volume of the convex hull of N points on the unit sphere S^2 (the Fejes Toth problem, 1964). Berman and Hanes (1970) solved N <= 8. Fejes Toth's inequality V <= (N-2)/6 * cot(w) * (3 - cot^2 w), w = pi N/(6(N-2)), is attained by the regular icosahedron, so N = 12 is settled (bound = table value 2.536150710120). S. Hoehner and J. Ledford (arXiv:2608.04392, Aug 2026) proved N = 9: the maximum is 3*sqrt(2*sqrt(3)-3) = 2.043750115900, the table value. Mutoh (2003) gave numerical candidates for N <= 30. Horvath and Langi (arXiv:1402.6496) solved d+2 points in d dimensions, and d+3 when d is odd. Hardin, Sloane and Smith tabulated putatively optimal arrangements for N = 4..130 in 1994 (neilsloane.com/maxvolumes, 12 decimals, files maxvol.3. < N > .txt) and icosahedral-symmetric ones for N = 72..78032 (neilsloane.com/icosahedral.codes, 12 decimals). Henry Cohn now maintains these tables (cohn.mit.edu/sloane, 7 decimals rounded DOWN, 267 icosahedral rows, data set hdl.handle.net/1721.1/147004) and invites improvements. W. Deeter's table (deetour.net/oppp/maxvols/maxvol-summary.html, N = 4..492, 12 decimals, coordinates maxvol. < N > .txt, last modified 26 Feb 2018, linked from OEIS A081314), built by optimising duals of roundest polyhedra, is strictly better than Sloane and Cohn at N = 62 (3.825221379534 vs 3.825219246599) and N = 124 (4.005307382615 vs 4.005226779889) and agrees with Sloane to 12 decimals at every other N <= 130. An auditor's checker reproduced both Deeter values from his files on 2026-10-30, and BFGS polishing of Sloane's files for 62 and 124 gains nothing (different basins). The AlphaEvolve survey (Georgiev, Gomez-Serrano, Tao, Wagner, arXiv:2511.02864, Nov 2025) calls Sloane's table 'the most up to date database'; it matched the first ~60 rows to all 13 digits, improved none, and did not try the remaining ~70 rows. On 2026-10-30 the posted Sloane files for N = 9, 12, 20, 61, 77, 100 and 130 reproduced the table to 12 decimals (N = 130: 4.013655508770), and BFGS polishing changed none by more than 2e-15. Any gains are therefore in other basins, most likely for N = 61..130. Credit: Berman, Hanes, Fejes Toth, Mutoh, Hardin, Sloane, Smith, Deeter, Cohn, Hoehner, Ledford.

## What counts as a win

Success means N unit vectors ( > = 20 significant digits) for some N in 10..130 other than N = 12 (N <= 9 and N = 12 are proven optimal and can never count), such that the convex-hull volume V*, computed in mpmath at 40 digits after normalisation, is STRICTLY LARGER (direction: max) than the best known value for N by at least 1e-10, where the best known value is the maximum of the 12-decimal value at https://neilsloane.com/maxvolumes/index.html, the 12-decimal value at https://deetour.net/oppp/maxvols/maxvol-summary.html and the 7-decimal value at https://cohn.mit.edu/sloane (all re-fetched immediately before claiming; at N = 62 and N = 124 Deeter's value is the bar). It must also be a different basin: polishing the posted Sloane file maxvol.3. < N > .txt and Deeter's maxvol. < N > .txt with the same routine stays below V* - 1e-10. And no published value for N found in an arXiv / Google Scholar check ('maximal volume' 'inscribed' polyhedra N) or among the links of OEIS A081314 is larger, and no paper proves the posted value for N optimal.

## Partial wins

- **p1:** For an N with 132 <= N <= 2000 listed in the icosahedral maximal-volume table, a configuration of any symmetry whose hull volume, with the same checker, beats by at least 1e-10 the larger of the 12-decimal icosahedral value at https://neilsloane.com/icosahedral.codes/index.html and, for N <= 492, Deeter's 12-decimal value at https://deetour.net/oppp/maxvols/maxvol-summary.html, and is not a re-polish of a posted file (polishing the posted ivol.3. < N > .*.txt and Deeter's maxvol. < N > .txt stays below V* - 1e-10). Cohn's 7-decimal icosahedral values are rounded down and are not the bar: re-posting Sloane's own file already beats them by up to 1e-7. At N = 492 Deeter's 4.142251571462 already beats the icosahedral 4.142250389453, so Deeter's value is the bar there. Rows with N <= 130 do not count.
- **p2:** A table-integrity finding in the 127 general rows (N = 4..130): at least one N whose posted Sloane file maxvol.3.N.txt or Deeter file maxvol.N.txt does not reproduce its own table's 12-decimal value to 1e-11, or polishes more than 1e-10 higher (an under-converged row, reported as such and not counted as a record). The known Sloane-versus-Deeter gaps at N = 62 and 124 are different basins and do not count.

## How a win is checked

Checker (seconds): normalise in mpmath. Get the hull facets from scipy. Assert all N points are hull vertices and the origin is inside. V* = sum over facets of |det(a,b,c)|/6 in mpmath at 40 digits. Compare with all three live tables (Sloane 12-decimal, Deeter 12-decimal, Cohn 7-decimal) and take their maximum as the bar. Run the same polish (BFGS on the normalised coordinates, then a high-precision Newton step) on Sloane's and Deeter's files for N and confirm the distinct-basin margin. Sanity-check against the Fejes Toth bound. Verified 2026-10-30 on Sloane's files for N = 9, 12, 20, 61, 77, 100, 130 and Deeter's files for N = 62, 124, 492.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://cohn.mit.edu/sloane>

## Sources

- <https://cohn.mit.edu/sloane>
- <https://neilsloane.com/maxvolumes/index.html>
- <https://deetour.net/oppp/maxvols/maxvol-summary.html>
- <https://neilsloane.com/icosahedral.codes/index.html>
- <https://neilsloane.com/maxvolumes/dim3/maxvol.3.130.txt>
- <https://arxiv.org/abs/2608.04392>
- <https://arxiv.org/abs/2511.02864>
- <https://arxiv.org/abs/1402.6496>
- <https://oeis.org/A081314>
- <https://hdl.handle.net/1721.1/147004>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- The Berman-Hanes necessary condition (each vertex is the normalised sum of its neighbours' cross products) gives a fixed-point iteration that converges fast inside a hull topology. Combine it with topology moves (edge flips, which switch between degree-5/6 vertex patterns) as a basin-hopping step.
- For N = 61..130, AlphaEvolve did not even try. Seed from Thomson and covering optima at the same N, since maximal-volume polyhedra are close to uniform.
- Deeter's route (take duals of near-roundest circumscribed polyhedra, then optimise for volume) found better basins than Hardin-Sloane-Smith at N = 62 and 124; apply it systematically to the other N.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- The bar is the maximum of three tables. Deeter's table is higher than Sloane's and Cohn's at N = 62 and 124; Sloane's 12-decimal values are sharper than Cohn's 7-decimal values, which are rounded down, so beating only Cohn by rounding is not a win.
- N <= 9 (Berman-Hanes 1970; Hoehner-Ledford 2026 for N = 9) and N = 12 (Fejes Toth's bound, attained by the icosahedron) are proven, so a 'win' there is a bug. Re-check arXiv for new optimality proofs before claiming.
- neilsloane.com point files need a browser-like User-Agent (plain curl gets 403).
- Do not confuse with Deeter's roundest-polyhedra (minimal circumscribed) tables on the same site; only the maxvol summary is the bar.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/packings-physics/sloane-cohn-max-volume-polyhedra-s2.md
```

Already set up? Say `run V3R1T4S on sloane-cohn-max-volume-polyhedra-s2`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `sloane-cohn-max-volume-polyhedra-s2`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
