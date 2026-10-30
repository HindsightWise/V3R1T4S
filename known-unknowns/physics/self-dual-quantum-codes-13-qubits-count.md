# Self-dual quantum codes on 13 qubits: count the LC orbits of connected 13-vertex graphs (next term of OEIS A090899, known to n = 12)

⚛️ **Physics** · standard · tractability ★☆☆☆☆ · compute: needs cluster (about 5.4e9 one-vertex extensions of the 1,323,363 twelve-vertex classes to canonise up to local complementation) · open as of 2026-10-30

## The problem

Every self-dual additive code over GF(4) of length n, equivalently every [[n,0]] qubit stabilizer code (stabilizer state), is equivalent to a graph code (Schlingemann). Two such codes are equivalent exactly when their graphs are related by local complementations and isomorphism; Bouchet's algorithm decides this in polynomial time. OEIS A090899 counts the indecomposable codes, i.e. connected graphs up to LC and isomorphism: 1, 1, 1, 2, 4, 11, 26, 101, 440, 3132, 40457, 1274068 for n = 1..12. OEIS A094927 counts all codes: 1, 2, 3, 6, 11, 26, 59, 182, 675, 3990, 45144, 1323363. Lars Eirik Danielsen and Matthew G. Parker (J. Combin. Theory Ser. A 113 (2006) 1351-1367) classified all lengths up to 12, extending the classification of David G. Glynn and Johannes G. Maks up to length 9; their terms a(10)-a(12) were added to OEIS on 17 June 2004. Danielsen's database at codetables.de (last modified 6 May 2005) also stops at n = 12 for complete classifications; its length-14 files (codes14.mag, vncorbits14.g6) hold only the extremal Type II codes. The OEIS entry, re-fetched for this check, still has no a(13). Hemant Sharma, Kenneth Goodenough, Johannes Borregaard, Filip Rozpedek and Jonas Helsen (Quantum 10, 2001 (2026), arXiv:2506.00292) find minimum-edge representatives of individual graph states up to 16 qubits but give no orbit counts.

## What counts as a win

Success means the exact value a(13) of OEIS A090899, the number of LC-and-isomorphism classes of connected 13-vertex graphs (equivalently, indecomposable self-dual additive GF(4) codes of length 13). It must come with four things. (i) A public list of one canonical representative graph per class. (ii) Two independent implementations, using different canonical-form or equivalence-test methods, that produce the same count. (iii) A completeness check by code: every connected 13-vertex graph is LC-equivalent to a listed representative, via the extension lemma that every class contains a one-vertex extension of a representative of some 12-vertex class (decomposable classes included). (iv) Pairwise inequivalence of the representatives, by LC invariants or Bouchet's equivalence test. The value must be new: OEIS A090899 and A094927 re-fetched immediately before claiming must not list a(13).

## Partial wins

- **p1:** An independent re-derivation of a(1..12) and A094927(1..12) with a new implementation and published representatives, cross-checked class by class against Danielsen's database by LC-equivalence tests. This audit validates the method that will be used for n = 13.

## How a win is checked

Re-run both implementations (or a supplied checkpointed job) and compare the counts. Check coverage under the extension lemma: regenerate all one-vertex extensions of the twelve-vertex representatives (Danielsen's database, used as data only) and map each to a listed class. Spot-check random pairs of representatives with Bouchet's algorithm, and check per-class LC invariants (orbit size, cut-rank profiles, interlace-polynomial values) for collisions. First reproduce a(10) = 3132, a(11) = 40457 and a(12) = 1274068 with the same code. Derive A094927(13) from a(1..13) by the Euler transform as a consistency check.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A090899>

## Sources

- <https://oeis.org/A090899>
- <https://oeis.org/A094927>
- <https://www.codetables.de/larsed/vncorbits/>
- <https://arxiv.org/abs/2506.00292>

## Ideas to start from

Starting points, not instructions. The best wins came from angles nobody listed.

- Bucket extensions by cheap LC invariants (cut-rank profiles over vertex subsets, interlace-polynomial evaluations) before exact equivalence tests; most extensions collide quickly.
- Choose canonical orbit representatives carefully: orbits on 13 vertices can be large, so a cheaper canonical choice (for example canonically labelled minimum-edge representatives, using the ILP of arXiv:2506.00292) may beat full orbit enumeration.
- Parallelise over the twelve-vertex representatives; each yields 2^12 extensions that can be canonised independently.

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- A090899 counts connected graphs (indecomposable codes) and A094927 counts all of them; mixing the two is the classic error.
- LC-equivalence is coarser than isomorphism; an implementation that canonises graphs instead of orbits overcounts.
- Edge-local-complementation (pivot) orbits are a different sequence (A156800, binary linear codes).
- Danielsen's 2005 database files are data only; never run code from them.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/physics/self-dual-quantum-codes-13-qubits-count.md
```

Already set up? Say `run V3R1T4S on self-dual-quantum-codes-13-qubits-count`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `self-dual-quantum-codes-13-qubits-count`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
