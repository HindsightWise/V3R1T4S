# Count the rings of order 32: the smallest unknown value of OEIS A027623 (only a(32) > 18,590 is known)

🃏 **Wildcard** · standard · tractability ★★☆☆☆ · compute: laptop-days · open as of 2026-10-30

## The problem

A027623 counts the rings with n elements: associative and distributive, not necessarily unital or commutative. It is known for every n <= 31 and for 33..63, but a(32) is unknown. Christof Noebauer ('The Numbers of Small Rings', 2000) computed a(16) = 390 and reported only a(32) > 18,590. Commutative rings of order 32 (A037289) likewise have only a(32) > 876. Unital rings of order 32 are known (A037291(32) = 208; commutative unital A127707(32) = 109, as corrected by Bernard Schott in 2022). The count is multiplicative over prime powers and every smaller order is known, so a(32) is the smallest open value. A027623 and A037234 (re-fetched 2026-10-30) still say a(32) is unknown. The rings split by additive group: Z32, Z16+Z2, Z8+Z4, Z8+Z2^2, Z4^2+Z2, Z4+Z2^3 and Z2^5. The last case is the classification of 5-dimensional associative algebras over F_2 without identity, where nilpotent algebras dominate. For nonassociative rings (A037292, a(8) = 801288), the data stop at n = 15; a comment gives values up to n = 24, but a(16) is unknown.

## What counts as a win

Success means the exact value of A027623(32). It needs a complete list of representatives (additive group plus structure constants), with a checker confirming each is an associative ring; pairwise non-isomorphism certified by canonical forms; and completeness certified independently: for each additive group A, the sum over representatives R of |Aut(A)|/|Aut(R)| must equal the number of associative bilinear products on A, counted by a separate program. The same code must reproduce A027623(8) = 52, A027623(16) = 390, A027623(27) = 59 and A037289(16) = 162. A027623 must be re-fetched live, and a literature search must find no earlier value.

## Partial wins

- **p1:** A037289(32), the number of commutative rings of order 32 (only > 876 known), with the same representative-list and orbit-counting certificate, reproducing A037289(16) = 162.
- **p2:** A037292(16), the number of nonassociative rings of order 16 (the first missing value of A037292, whose comment lists every other n <= 24), by orbit counting of bilinear maps under Aut(A) for each abelian group A of order 16, with a second independent method agreeing and the code reproducing a(4) = 55, a(8) = 801288 and the listed values for n = 17..24.

## How a win is checked

Check the ring axioms on every listed table (seconds). Recompute canonical forms to confirm non-isomorphism. Independently count the associative bilinear products on each additive group (for example by SAT model counting or a structured enumeration) and check the orbit-stabilizer identity.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A027623>

## Sources

- <https://oeis.org/A027623>
- <https://oeis.org/A037234>
- <https://oeis.org/A037289>
- <https://oeis.org/A037291>
- <https://oeis.org/A127707>
- <https://oeis.org/A037292>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Unital rings of order 32 are known; any ring embeds into its Dorroh extension or splits off a unital summand, so count by the annihilator/nilpotent structure and reuse the unital classification.
- For the Z2^5 case, build nilpotent F_2-algebras by central extensions (the p-group generation analogue, as de Graaf does for nilpotent Lie algebras).

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A027623 includes non-unital and noncommutative rings, A037291 only unital ones, and A037289 only commutative ones; do not mix them.
- Rings on Z8+Z4 need products respecting the orders of the generators; an unconstrained bilinear map over Z may not descend.
- Noebauer's original files (ftp at algebra.uni-linz.ac.at) are offline; take the small values from OEIS.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/wildcard/rings-of-order-32.md
```

Already set up? Say `run V3R1T4S on rings-of-order-32`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `rings-of-order-32`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
