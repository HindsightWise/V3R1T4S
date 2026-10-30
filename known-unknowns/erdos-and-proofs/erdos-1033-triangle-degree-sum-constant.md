# Erdos #1033 (Bollobas-Erdos): a construction below 1.463877226961 n, or a certified lower bound of at least 1.453 n, for the forced triangle degree sum

✏️ **Erdős problems and proofs** · standard · tractability ★★☆☆☆ · compute: laptop-hours (blow-up optimisation in exact or interval arithmetic); laptop-days for a flag-algebra SDP with exact rounding · open as of 2026-10-30

## The problem

Let h(n) be the largest value such that every graph on n vertices with more than n^2/4 edges has a triangle whose three vertex degrees sum to at least h(n). Bollobas and Erdos conjectured h(n) >= (2(sqrt3-1)-o(1))n, which matches the Erdos-Laskar/Fan construction (about 1.46410n). That conjecture is now false. rickyc, working with GPT-5.5 Pro, posted a blow-up of the butterfly graph (two triangles sharing a vertex) reaching about 1.46393n (forum, 27 Jun 2026). Wouter CvB optimised the part weights and partial densities (note dated 27 Jul 2026). This gives c+ = y0 = 1.463877226961..., the smallest positive root of P(y) = 384y^7 + 1744y^6 - 832y^5 - 86712y^4 + 379016y^3 - 697963y^2 + 617212y - 215708. Blow-ups of all graphs on at most 8 vertices did not beat it. The published lower bound is Fan's 21/16 = 1.3125 (1988). On the forum RealBelgian reports flag-algebra lower bounds of about 1.45016 (1 Aug 2026) and then about 1.4525 (7 Aug 2026), with no paper or certificate public yet. So 1.4525 <= liminf h(n)/n <= y0, with the lower value claimed and not yet verified. The problem page is open; the question is to estimate h(n).

## What counts as a win

CONFIRMED by either of two routes. (A) Construction. Give a template: a graph H with independent parts V_1..V_t, rational or algebraic weights x_i > 0 summing to 1, and pair densities f_ij in [0,1] on the edges of H, each realised by near-regular bipartite graphs. In exact or rigorous interval arithmetic, the edge density sum_{ij in E(H)} f_ij x_i x_j must be strictly greater than 1/4, and the largest degree sum d_i + d_j + d_k over triangles ijk of H, where d_i = sum_j f_ij x_j, must be c < 1.463877226961 (strictly less than y0, and below any smaller construction posted on the forum thread at verification time). Any equivalent explicit graph family with a proof of the same two limits also counts. (B) Lower bound. An exact flag-algebra or other machine-checkable certificate (rational SDP with exact rounding, checked by independent code) proving h(n) >= (c - o(1))n with c >= 1.453, and c strictly greater than every lower bound posted on the forum thread or in a paper at verification time. The 1.453 threshold sits clearly above RealBelgian's approximate 1.4525 claim.

## Partial wins

- **p1:** A publicly released exact certificate proving liminf h(n)/n >= 1.40, provided no public certificate or paper with c >= 1.40 exists at verification time.
- **p2:** A publicly released exact certificate proving liminf h(n)/n >= 1.45, provided no public certificate or paper with c >= 1.45 exists at verification time.

## How a win is checked

(A) Recompute the edge density and every triangle degree sum of H from the stated weights. Use exact algebraic arithmetic (sympy/flint) or interval arithmetic with outward rounding. Confirm the parts are independent, so every triangle of the blow-up comes from a triangle of H. Then build G_N for N = 10^4 with near-regular bipartite realisations, count edges and scan all triangles as a sanity check. (B) Re-run the SDP certificate check in exact rational arithmetic with code written independently of the prover: positive semidefiniteness via exact LDL^T, and the flag identities recomputed from scratch.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://www.erdosproblems.com/forum/thread/1033>

## Sources

- <https://www.erdosproblems.com/1033>
- <https://www.erdosproblems.com/forum/thread/1033>
- <https://woutercvb.github.io/Erdos1033_smalloptimization.pdf>
- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/1033.lean>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Leave the butterfly support. rickyc reports (forum, 1 Aug 2026, GPT-assisted, unverified) that Wouter CvB's point is optimal among all graphons with the butterfly support pattern, even with arbitrary measurable structure in its two partial blocks. Wouter CvB found nothing better among constant-density blow-ups of graphs on <= 8 vertices. A gain probably needs a different support graph: 9+ vertices, three or more partial pairs, or non-constant density on a pair of a new template.
- Flag algebras on 3-graphs of the pair (G, degree-class labelling), or on graphs with vertex weights encoding degree. For the lower bound, start from Fan's 21/16 argument and add degree-type flags.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Edge density must be strictly above 1/4. A template at exactly 1/4 needs the perturbation argument written out.
- Degree sums are over triangles of the whole graph. Non-independent parts create extra triangles.
- RealBelgian's ~1.4525 is an approximate forum claim with no public certificate. Do not cite it as proven, and do not claim p1/p2 if a certificate or paper has appeared in the meantime.
- Floating-point optimisation near y0 is not a proof; certify the strict inequality. Even y0 itself needs exact arithmetic: a naive double-precision root finder returns 1.4638772262, while the true root is 1.463877226961326.
- The problem page (last edited 3 Apr 2026) still lists 2(sqrt3-1) and 21/16 as the bounds; the current state is in the forum thread and Wouter CvB's note.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/erdos-1033-triangle-degree-sum-constant.md
```

Already set up? Say `run V3R1T4S on erdos-1033-triangle-degree-sum-constant`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `erdos-1033-triangle-degree-sum-constant`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
