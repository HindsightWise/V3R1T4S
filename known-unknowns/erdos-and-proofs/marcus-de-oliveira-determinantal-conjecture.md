# MOONSHOT - Marcus-de Oliveira determinantal conjecture: normal A, B with det(A + B) outside the convex hull of the n! eigenvalue products

✏️ **Erdős problems and proofs** · moonshot (famous, long odds) · tractability ★☆☆☆☆ · compute: laptop-hours (an exact check is n! products plus one determinant over Q(i); n = 4..7 is instant) · open as of 2026-10-30

## The problem

The determinantal conjecture of M. Marcus (1972) and G. N. de Oliveira (1982): if A and B are n x n normal complex matrices with eigenvalues a_1..a_n and b_1..b_n, then det(A + B) lies in the convex hull of the n! points prod_i (a_i + b_sigma(i)), sigma in S_n. Without loss of generality A = diag(a) and B = U diag(b) U* with U unitary, so the conjecture is a statement about how det(diag(a) + U diag(b) U*) varies over the unitary group. Fiedler (1971) proved the case where both matrices are Hermitian, where the hull is an interval. The case n = 2 is classical, and further special classes are treated in the literature (for example essentially Hermitian pairs). The general conjecture is open: the formal-conjectures file Wikipedia/DeterminantalConjecture.lean, which formalises exactly this statement with A = U1 D1 U1* and B = U2 D2 U2*, is tagged research open as of 2026-10-30, and the Wikipedia article lists it as a conjecture. A single explicit pair of normal matrices with det(A + B) strictly outside the hull would disprove it.

## What counts as a win

Success means an integer n, eigenvalue vectors a, b with entries in Q(i), and an exactly unitary matrix U with entries in Q(i), with U U* = I checked exactly (rational unitaries come, for example, from the Cayley transform of a skew-Hermitian matrix over Q(i)). With A = diag(a) and B = U diag(b) U*, the value D = det(A + B) must be computed exactly by two independent programs. The claim must also give a separating certificate: w in Q(i) with Re(conj(w) D) STRICTLY GREATER than max over all sigma in S_n of Re(conj(w) prod_i (a_i + b_sigma(i))), checked exactly over all n! permutations. The conjecture must still be open, i.e. the formal-conjectures file is still tagged research open and no newer paper settles it, re-checked before claiming.

## Partial wins

- **p1:** A Lean 4 proof, compiling against the pinned toolchain of google-deepmind/formal-conjectures, of the file's statement determinantal_conjecture specialised to n = Fin 2. The statement must be unchanged apart from fixing the index type. The proof may use no sorry, no native_decide and no new axioms (#print axioms shows a subset of propext, Classical.choice, Quot.sound), and the n = 2 case must not already carry a formal proof in the repository or an open pull request there.

## How a win is checked

Represent Gaussian rationals exactly (pairs of Fractions). Check U U* = I entrywise, form B = U diag(b) U*, and compute det(diag(a) + B) by exact fraction-free elimination, cross-checked by a Leibniz or Laplace expansion for n <= 7. Enumerate all n! permutations, form the products, and check the separating inequality exactly. Optionally confirm by an exact rational LP that D is outside the hull.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/DeterminantalConjecture.lean>

## Sources

- <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Wikipedia/DeterminantalConjecture.lean>
- <https://en.wikipedia.org/wiki/Determinantal_conjecture>
- <https://doi.org/10.1080/03081087.1982.11882087>
- <https://doi.org/10.1512/iumj.1973.22.22094>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Search with an adversarial optimiser: for fixed eigenvalues, maximise the signed distance of det(diag(a) + U diag(b) U*) outside the hull over U, using Riemannian gradient steps on U(n) in float. Then round promising U to an exact rational unitary via the Cayley transform and recheck exactly.
- Choose eigenvalues far from collinear (for example vertices of regular polygons with different radii) for n = 4..6, since Hermitian or nearly collinear spectra are covered by Fiedler-type arguments.
- The hull has at most n! vertices, but many products coincide for symmetric spectra. Use spectra with few hull vertices so that the hull is thin and det(A + B) has room to escape.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Floating-point: a determinant just outside the hull by 1e-12 is noise. Only an exact U, exact D and exact separating certificate count.
- U must be exactly unitary. A rounded unitary changes the spectrum of B, which is then not normal with eigenvalues b.
- Both-Hermitian pairs are covered by Fiedler (1971), and n = 2 is classical. Check the literature for the other settled classes before searching.
- The point must be strictly outside the hull. Landing on the boundary is consistent with the conjecture.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/erdos-and-proofs/marcus-de-oliveira-determinantal-conjecture.md
```

Already set up? Say `run V3R1T4S on marcus-de-oliveira-determinantal-conjecture`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `marcus-de-oliveira-determinantal-conjecture`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
