# ⚪ Packings and physics

Circle, sphere and point configurations and energy minima vs live tables.

**36 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [Packomania: equal 4D/5D/6D hyperspheres in a hypersphere (hsp4, hsp5, hsp6), beat a per-N…](packomania-hyperspheres-hsp4-hsp6.md) | harvest | laptop-hours |
| ★★★★☆ | [Spherical codes (Tammes problem and higher dimensions): beat an entry in Cohn's spherical…](spherical-codes-cohn-table.md) | harvest | laptop-hours |
| ★★★☆☆ | [Grassmannian packings: N subspaces of R^m (m <= 16) with larger minimal squared chordal d…](cohn-grassmannian-packings-table.md) | harvest | laptop-hours |
| ★★★☆☆ | [Harmonic energy on spheres in 4 to 32 dimensions: lower the best known energy in the Ball…](cohn-harmonic-energy-spheres-dim4-32.md) | harvest | laptop-hours |
| ★★★☆☆ | [Kob-Andersen binary Lennard-Jones crystals: a periodic 80:20 structure with lower zero-pr…](ccd-kob-andersen-crystal-ground-states.md) | standard | laptop-hours |
| ★★★☆☆ | [Maximum-determinant (Fekete-type interpolation) points on S^2: a larger log det than Wome…](womersley-maxdet-points-s2.md) | harvest | laptop-hours (n <= 40) to laptop-days (n near 100; (n+1)^2 x (n+1)^2 Gram matrices up to 10201 x 10201) |
| ★★★☆☆ | [Packomania: equal spheres in a cube (scu), beat a per-N record radius](packomania-scu-spheres-in-cube.md) | harvest | laptop-hours |
| ★★★☆☆ | [Spherical t-designs on S^3 (including SO(3) Chebyshev rules) with fewer points: beat the…](spherical-designs-s3-fewest-points.md) | harvest | laptop-days (N up to ~12000 points in R^4; high-precision polishing is the bottleneck) |
| ★★☆☆☆ | [Binary Lennard-Jones clusters: lower a putative global minimum in the Doye-Meyer table (N…](ccd-binary-lennard-jones-clusters.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Finnis-Sinclair molybdenum and iron clusters (N = 3..100): lower a putative global minimu…](ccd-finnis-sinclair-mo-fe-clusters.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Gupta and Murrell-Mottram metal clusters (Zn, Cd <= 125; Pb <= 150; Na <= 379/380): lower…](ccd-gupta-murrell-mottram-metal-clusters.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Gupta cobalt clusters (N = 2..200): lower a putative global minimum on the Cambridge Clus…](ccd-gupta-cobalt-clusters-n200.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Minimal-energy clusters of hard spheres: N unit spheres in R^3 (N <= 99) or R^4 (N <= 32)…](sloane-hard-sphere-clusters-second-moment.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Packomania: equal circles in a circle (cci), beat a per-N record radius](packomania-cci-equal-circles-in-circle.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Packomania: equal circles in a square (csq), beat a per-N record radius](packomania-csq-equal-circles-in-square.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Positive-weight quadrature on the sphere S^2: exact to degree t with fewer nodes than Gra…](spherical-quadrature-s2-positive-fewest-nodes.md) | standard | laptop-hours (orbit-structured nonlinear least squares, then high-precision polishing) |
| ★★☆☆☆ | [Spherical coverings: N points on the sphere with a smaller covering radius than the Hardi…](sloane-cohn-spherical-coverings-s2.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Spherical t-designs on S^2 with fewer points: beat the smallest known N for a degree t (H…](spherical-designs-s2-fewest-points.md) | harvest | laptop-days (numerical design search plus high-precision polishing; N up to ~5000) |
| ★★☆☆☆ | [Thinnest coverings by n equal circles: cover the unit square (Nurmela-Ostergard table, n…](equal-circle-coverings-square-disk.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Thomson problem: lower the best known Coulomb energy for some N (Deeter / Cambridge Clust…](thomson-problem-live-tables.md) | harvest | laptop-hours |
| ★★☆☆☆ | [(C60)_N molecular clusters (Pacheco-Prates-Ramalho N <= 105, Girifalco N < 81): lower a p…](ccd-c60-molecular-clusters.md) | harvest | laptop-hours |
| ★★☆☆☆ | [(NaCl)_N Cl- cluster anions (N <= 35, Tosi-Fumi Coulomb plus Born-Mayer and Welch potenti…](ccd-nacl-cluster-anions-born-mayer.md) | harvest | laptop-hours |
| ★★☆☆☆ | [3D AB off-lattice protein model: beat the best published energy for a standard Fibonacci…](ab-offlattice-protein-3d-best-energies.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Binary Gupta nanoalloys (Ag-Au, Cu-Ag, Cu-Au 55-atom; Cu-Au 38-atom; Li-Na and Na-K 55-at…](ccd-binary-gupta-nanoalloys-38-55.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Dzugutov, modified-Dzugutov and Z1/Z2 clusters: lower a putative global minimum in the Do…](ccd-dzugutov-zetterling-polytetrahedral-clusters.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Fejes Toth problem: N points on the unit sphere whose convex hull has larger volume than…](sloane-cohn-max-volume-polyhedra-s2.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Glue-potential aluminium (N <= 190) and lead (N <= 160) clusters: lower a putative global…](ccd-glue-potential-al-pb-clusters.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Lennard-Jones clusters: lower a putative global minimum in the Cambridge Cluster Database…](lennard-jones-ccd-doye-table.md) | standard | laptop-hours |
| ★★☆☆☆ | [MOONSHOT - Archimedean solids without central symmetry: beat 207/208 for truncated tetrah…](truncated-tetrahedra-snub-solids-packing.md) | moonshot | laptop-days (floppy-box or adaptive-shrinking-cell Monte Carlo, small cells; exact check in minutes) |
| ★★☆☆☆ | [Sutton-Chen metal clusters (12-6, 9-6, 10-8; N <= 80): lower a putative global minimum in…](ccd-sutton-chen-clusters.md) | harvest | laptop-hours |
| ★☆☆☆☆ | [Largest small polygons: a convex n-gon of diameter 1 with larger area than Bingane-Mossin…](largest-small-even-polygons-area.md) | standard | laptop-hours |
| ★☆☆☆☆ | [MOONSHOT - Congruent ellipsoids: a periodic packing denser than the Donev-Stillinger-Chai…](congruent-ellipsoids-densest-packing.md) | moonshot | laptop-days (event-driven or Monte Carlo compression of small periodic cells; certification in minutes) |
| ★☆☆☆☆ | [MOONSHOT - Regular heptagons in the plane: a packing of congruent regular heptagons dense…](regular-heptagon-densest-packing.md) | moonshot | laptop-hours (small periodic cells; exact certification in seconds) |
| ★☆☆☆☆ | [MOONSHOT - Regular tetrahedra: a packing of congruent regular tetrahedra denser than the…](regular-tetrahedra-densest-packing.md) | moonshot | laptop-days (periodic hard-polyhedron compression of small cells, then exact certification in minutes) |
| ★☆☆☆☆ | [MOONSHOT - Torquato-Jiao conjecture: a non-lattice packing of a centrally symmetric Plato…](torquato-jiao-centrosymmetric-polyhedra.md) | moonshot | laptop-days (multi-particle periodic compression; exact certification in minutes) |
| ★☆☆☆☆ | [Rigid-water clusters (TIP4P, TIP5P): lower a putative global minimum for (H2O)_N, N <= 21…](ccd-water-clusters-tip4p-tip5p.md) | standard | laptop-hours |

← [All categories](../README.md)
