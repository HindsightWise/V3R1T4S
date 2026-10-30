# Multi-controlled Z with fewer T gates: an exact C^nZ (n >= 4 controls) with T-count below Gidney-Jones' 4n - 6

⚛️ **Physics** · standard · tractability ★★☆☆☆ · compute: laptop-hours (exact Clifford+T simulation of candidates on <= ~20 qubits; finding the gadget is the hard part) · open as of 2026-10-30

## The problem

The n-controlled Z gate C^nZ (n controls plus one target, n + 1 qubits) appears in Grover reflections, multiplexers and arithmetic. Using Clifford gates, T gates, ancillas, Pauli measurements and classically controlled Cliffords, the logical-AND construction gives T-count 4n - 4. Craig Gidney and N. Cody Jones (arXiv:2106.11513, 2021) built a CCCZ with 6 T gates and reduced the general count to 4n - 6 for n > 2. Ken M. Nakanishi and Synge Todo (arXiv:2410.00910, v2 3 Oct 2024) systematised such decompositions and kept 4n - 6 as the minimum known T-count. At that T-count they lowered the CNOT count (CNOT plus CZ gates) to 3n - 3 to 4n - 4 (their Figs. 1a and 3a) or 3n - 2 to 4n - 5 (Figs. 1a' and 3a), depending on measurement outcomes (Table III). Lower bounds are far below. Michael Beverland, Earl Campbell, Mark Howard and Vadym Kliuchnikov (Quantum Sci. Technol. 5, 035009 (2020), arXiv:1904.01124) show via stabilizer nullity that an m-qubit multi-controlled Z needs at least m T states (Proposition 4.1), i.e. n + 1 here. Their stabilizer-extent value 9/4 for CCCZ|+ > ^4 (Table 4, computed to eight digits) gives at least 5.12, hence 6, T states for CCCZ (Table 1), so the Gidney-Jones CCCZ is optimal. Fixing one control to |1> turns a C^nZ protocol into a C^(n-1)Z protocol with the same T gates. So every C^nZ with n >= 3 needs at least max(6, n + 1) T gates. With every measurement outcome at probability 1/2, they also show that n - 1 CCZ states are necessary and sufficient (Lemma 6.6). Arul Rhik Mazumder's isotropy bound (arXiv:2610.01024, Oct 2026) is exact for Hadamard-free circuits but explicitly excludes measurement and feed-forward. Abhoy Kole, Till Schnittka and Rolf Drechsler (arXiv:2605.18159, May 2026) improve static clean-ancilla decompositions but stay above 4n - 6. David Gosset, Robin Kothari and Chenyi Zhang (arXiv:2510.07223, Oct 2025) implement the multi-qubit Toffoli to diamond-norm error epsilon with O(log(1/epsilon)) T gates, but only approximately. So for n = 4 the exact T-count lies between 6 and 10.

## What counts as a win

Success means, for some n with 4 <= n <= 12, an explicit protocol on the n + 1 data qubits plus any number of ancillas prepared in a fixed stabilizer state. It may use Clifford gates, T and T-dagger gates, Pauli measurements, and Clifford gates classically controlled by earlier outcomes. For EVERY measurement record, the map on the data qubits must be exactly C^nZ up to a record-dependent global phase, with all ancillas ending in a state independent of the data input. The number of T/T-dagger gates on the worst-case record, counting each classically controlled T gate wherever it could fire, must be at most 4n - 7 (direction: min; record 4n - 6, Gidney-Jones arXiv:2106.11513). An arXiv search re-run immediately before claiming must find no lower published count for that n. Magic states other than T states, catalyst states and approximate synthesis do not count.

## Partial wins

- **p1:** For some n in 4..10, T-count exactly 4n - 6 with a worst-case two-qubit gate count (CNOT or CZ, including classically controlled ones, over all measurement records) strictly below 4n - 5. That is the best worst case in Nakanishi-Todo Table III (Figs. 1a' and 3a).
- **p2:** A rigorous lower bound of at least 7 T gates for C^4Z in the model above, beating the bound of 6 inherited from CCCZ. Its numerical part must be certified, for example by an exact dual certificate for a stabilizer-extent-type monotone, and its monotonicity argument must cover measurement and feed-forward.

## How a win is checked

Simulate the protocol exactly over Z[1/2, e^{i pi/4}] (sympy, or integer vectors scaled by powers of sqrt2) on the n + 1 + a qubits. For every measurement record (2^r branches, pruning zero-probability ones), apply the record's operations to each computational basis input |x> with the ancillas in their initial state. Check that the output equals c_record * (-1)^{x_1 x_2 ... x_{n+1}} |x> (x) |anc_final > , with the same c_record for all 2^{n+1} inputs; by linearity this certifies the branch acts as C^nZ. Count T/T-dagger gates on the worst branch. For n <= 8 with <= 8 ancillas this is 2^17 amplitudes per branch, a matter of seconds. For p1, also count two-qubit gates per branch.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://arxiv.org/abs/2410.00910>

## Sources

- <https://arxiv.org/abs/2106.11513>
- <https://arxiv.org/abs/2410.00910>
- <https://arxiv.org/abs/1904.01124>
- <https://arxiv.org/abs/2610.01024>
- <https://arxiv.org/abs/2605.18159>
- <https://arxiv.org/abs/2510.07223>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Gidney-Jones save 2 T by merging two logical-ANDs into a 6-T CCCZ. A gadget that merges three ANDs (C^4Z) in fewer than 10 T, or a second independent 2-T saving, gives 4n - 7 or better by induction.
- Phase-polynomial view: with clean ancillas and measurement-based uncomputation, C^nZ is a degree-(n+1) phase. Look for identities in which several partial products share T gates, as in the Gidney-Jones CCCZ.
- Search small gadgets with SAT or ILP over Clifford+T circuits with one or two measurements and ancillas, using exact simulation as the oracle.
- Lower-bound side: the stabilizer extent of C^4Z|+ > ^5 is only 9/8 + 1/sqrt2 (Beverland et al. Table 4), worth about 3.8 T states. Going past the inherited bound of 6 needs another monotone, for example one adapted from the dyadic monotone, or a new LP/SDP certificate.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Relative-phase multi-controlled gates (Maslov, arXiv:1508.03273) are cheaper but are not C^nZ; they count only if every relative phase is undone inside the protocol.
- Every measurement record must be handled; a protocol that is exact only on the most likely record is not exact.
- Notation: C^nZ here has n controls and acts on n + 1 qubits; Beverland et al. write C^{n-1}Z for n qubits.
- Mazumder's isotropy bound does not apply when measurements are used: it gives 7 for CCZ, which measurement circuits beat with 4.
- For n = 3 the T-count 6 is optimal: the stabilizer extent of CCCZ|+ > ^4 is 9/4, worth at least 5.12 T states. Claims for n = 3 are out of scope.
- Approximate constructions do not count. The randomly chosen circuits of Gosset, Kothari and Zhang (arXiv:2510.07223) use O(log(1/epsilon)) T gates but implement C^nZ only to error epsilon.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/multi-controlled-z-t-count-below-4n-6.md
```

Already set up? Say `run V3R1T4S on multi-controlled-z-t-count-below-4n-6`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `multi-controlled-z-t-count-below-4n-6`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
