# Chirikov standard map: shrink the rigorous window [0.9716, 0.9718] around the breakup of the golden invariant circle

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-days (multiprecision FFT-based a posteriori KAM near criticality needs many Fourier modes) · open as of 2026-10-30

## The problem

The standard map is y' = y - (k/2 pi) sin(2 pi x), x' = x + y'. Greene's residue criterion and MacKay's renormalization put the breakup of the golden-mean rotational invariant circle (RIC), believed to be the last RIC to break, at k_c = 0.971635406... The rigorous results lag behind: Mather proved there are no RICs for |k| > 4/3; MacKay and Percival (Commun. Math. Phys. 98, 1985; converse KAM) proved none for |k| >= 63/64 = 0.984375; Jungreis (Ergodic Th. Dyn. Sys. 11 (1991) 79-84) proved non-existence at several given parameters, including k = 0.9718. On the existence side, Celletti and Chierchia (J. Stat. Phys. 65, 1991) got the golden circle for every |k| <= 0.838, and Jordi-Lluis Figueras, Alex Haro and Alejandro Luque (arXiv 1601.00084; Found. Comput. Math. 17 (2017) 1123-1193) validated the golden circle at k = 0.9716 with an a posteriori KAM theorem. Salvador Addas-Zanata (arXiv 2610.28449, 20 Oct 2026) restates exactly this state. He notes that existence at a given parameter does not give the whole interval, that non-existence at 0.9718 does not give every larger k, and that the conjecture that the set of k with RICs is [-k_c, k_c] is unproven.

## What counts as a win

Either (a) a computer-assisted proof that an analytic invariant circle with rotation number (sqrt5 - 1)/2 exists at some k >= 0.97161, or (b) a computer-assisted proof that no rotational invariant circle exists at some k <= 0.97179. Direction: the window [0.9716, 0.9718] gets strictly narrower by at least 1e-5 on one side, and the result also beats any later rigorous value found by a literature search re-run just before claiming. All inequalities must be verified in outward-rounded interval arithmetic.

## Partial wins

- **p1:** A computer-assisted proof that no rotational invariant circle exists for every k in the whole closed interval [0.9718, 0.98], uniform in the parameter, for example by covering parameter subintervals with interval-valued Jungreis or MacKay-Percival cone-crossing certificates.
- **p2:** The same uniform non-existence for the whole interval [0.9718, 63/64], which together with MacKay-Percival proves that there are no RICs for any k >= 0.9718.
- **p3:** An independent, publicly posted, interval-checked a posteriori KAM certificate for the golden circle at k = 0.9716, written with a code base different from that of Figueras-Haro-Luque. Reproduction only; it validates the tooling for (a).

## How a win is checked

Existence: the certificate gives the Fourier coefficients of the parameterization K(theta) and of the approximate inverse, the analyticity strip and the Diophantine constants of the golden mean. A checker evaluates every hypothesis of the stated a posteriori KAM theorem (Figueras-Haro-Luque form), with rigorous FFT error bounds, in arb or MPFR interval arithmetic; this takes hours. Non-existence: the certificate gives finite orbit segments and cone data; a checker iterates them in interval arithmetic and verifies the cone-crossing condition, for each parameter subinterval in p1 and p2.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2610.28449>

## Sources

- <https://arxiv.org/abs/2610.28449>
- <https://arxiv.org/abs/1601.00084>
- <https://arxiv.org/abs/nlin/0609024>
- <https://amath.colorado.edu/faculty/jdm/papers/StdMapEncylopedia.pdf>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Existence: near criticality the needed Fourier dimension grows fast. Use the critical-circle renormalization scaling to choose the grid, and use mixed precision: Newton steps in double, the final validation in multiprecision.
- Non-existence just above k_c: periodic orbits with Fibonacci rotation numbers have large residues there, and their stable and unstable manifolds supply the orbit segments for a converse-KAM certificate.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Normalisation: some papers write lambda V(theta) with V = -(1/2 pi) sin(2 pi theta); check that sup|V'| = 1 so that lambda = k.
- Existence at the critical value itself is expected to give only a non-analytic critical circle; aim strictly between 0.9716 and 0.971635.
- A non-existence claim below 0.971635 contradicts Greene's numerics and almost surely means a bug.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/standard-map-golden-circle-breakup-rigorous-window.md
```

Already set up? Say `run V3R1T4S on standard-map-golden-circle-breakup-rigorous-window`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `standard-map-golden-circle-breakup-rigorous-window`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
