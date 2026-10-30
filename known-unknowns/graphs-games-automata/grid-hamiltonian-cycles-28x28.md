# Hamiltonian cycles on the 28 x 28 grid: the next term of OEIS A003763 (known to 26 x 26 since Pettersson 2014)

🕸️ **Graphs, games and automata** · standard · tractability ★★☆☆☆ · compute: needs cluster (frontier transfer matrix with on the order of 1e11 non-crossing connectivity states at width 28, i.e. terabytes per modulus, over several primes) · open as of 2026-10-30

## The problem

A003763 counts undirected Hamiltonian cycles on the 2n x 2n grid graph (closed rook tours). Earlier terms came from Schmalz, Hite and Klein, from Ponitz and Tittmann, from Herman Jamke (n = 8), from Jesper Jacobsen (n = 9, 10; 2007) and from Artem Karavaev (up to n = 11). Ville Pettersson ('Enumerating Hamiltonian Cycles', Electron. J. Combin. 21(4), P4.7, 2014) gave a(12) and a(13), the 24 x 24 and 26 x 26 boards. The b-file (Sloane) ends at n = 13. The counts up to symmetry, A209077, reach only n = 10 (Ed Wynn, arXiv 1402.0545, 2014). OEIS checked live 2026-10-30 shows no newer term or pending draft. a(13) has 101 digits. a(14), the 28 x 28 board, has about 118 digits and needs a width-28 frontier.

## What counts as a win

Success means the exact value of A003763(14), the number of Hamiltonian cycles of the 28 x 28 grid graph (or the next unknown index if the live b-file has grown), computed by two runs that agree exactly. The runs must differ in moduli set or exact arithmetic AND in decomposition (row vs column order, or a different state encoding). The same code must reproduce A003763(1..13).

## Partial wins

- **p1:** A209077(11): the Hamiltonian cycles of the 22 x 22 grid counted up to the 8 symmetries. A209077 is known only to n = 10 (Ed Wynn), although A003763 reaches n = 13, and the new term needs the symmetric-cycle counts. Two runs must agree and reproduce A209077(1..10).
- **p2:** The number of Hamiltonian cycles of the 26 x 28 grid, two runs agreeing, reproducing all published m x n values the code covers.

## How a win is checked

Skeptic: rerun the claimant's code modulo one fresh 61-bit prime for the 28 x 28 board and compare; rerun for 2n <= 20 against the b-file.

## Is it still open?

Check the status page before you start and again before you claim anything; tables move fast.

- <https://oeis.org/A003763>

## Sources

- <https://oeis.org/A003763>
- <https://oeis.org/A209077>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/v21i4p7>
- <https://arxiv.org/abs/1402.0545>

## Traps

False wins others have fallen for. A claim that walks into one of these will not survive the skeptics.

- Odd boards have no Hamiltonian cycle; A003763 indexes the side 2n.
- Partial-win sequence numbers (A209077 and others) must be checked live for their current extent before claiming; if one is already extended, the partial is the next unknown term.

## Point your agent at it

```
set up V3R1T4S: https://github.com/elder-plinius/V3R1T4S and hunt known-unknowns/graphs-games-automata/grid-hamiltonian-cycles-28x28.md
```

Already set up? Say `run V3R1T4S on grid-hamiltonian-cycles-28x28`. Your agent follows [AGENTS.md](../../AGENTS.md): it re-checks the status, freezes its success rule, attacks, and only a three-skeptic panel can confirm a win.

---

_Generated from [`bank/targets.json`](../../bank/targets.json) (id `grid-hamiltonian-cycles-28x28`). Found it solved, stale or wrong? Open an issue or a pull request against that file._
