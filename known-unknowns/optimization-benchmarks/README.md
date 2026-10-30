# 🚚 Optimization benchmarks

Best-known solutions on public routing, scheduling and MIP benchmark libraries.

**56 open problems**, easiest first. Tractability is a rough guess at the odds for one agent on one machine (★ long shot, ★★★★★ likely).

| Odds | Problem | Kind | Compute |
|---|---|---|---|
| ★★★★☆ | [Flexible job shop with worker flexibility (FJSSP-W benchmark, 402 instances): lower a bes…](fjssp-w-worker-flexibility-bks.md) | harvest | laptop-hours |
| ★★★★☆ | [QOBLIB minimum Birkhoff decomposition: an exact decomposition of B5_25_2 with at most 13…](qoblib-birkhoff-small-exact-records.md) | harvest | laptop-hours to laptop-days for search; exact checking takes seconds; 5x5 and 6x6 integer matrices, respectively 120 and 720 possible permutation columns |
| ★★★★☆ | [QOBLIB node-disjoint Steiner tree packing (multi-layer switchbox routing): a cheaper pack…](qoblib-steiner-tree-packing-records.md) | harvest | laptop-hours (multi-layer grid graphs up to 100 x 100 per layer and 5 layers; the 14 best-known instances are at most 70 x 70; the official checker runs in seconds) |
| ★★★★☆ | [QOBLIB ten-asset portfolio: close the exact optimum gap for a010_t10_orig_b004_l1e-03](qoblib-portfolio-ten-assets-exact.md) | standard | laptop-hours to laptop-days; 10 assets, 10 periods, 600 position binaries before presolve, plus 110 slack bits; exploit interchangeable unit copies and the four-position budget |
| ★★★☆☆ | [ARPA-E GO Competition Challenge 3 (multi-period AC unit commitment): beat the best Event…](go3-event4-synthetic-best-scores.md) | harvest | laptop-hours (73- and 617-bus scenarios; the 4,000- to 23,643-bus ones need laptop-days and 16+ GB RAM) |
| ★★★☆☆ | [Gset Max-k-Cut (k = 3, 4): a better k-partition than the best published for a Gset graph](gset-max-k-cut-records.md) | harvest | laptop-hours to laptop-days (local search on graphs of 800 to 20,000 vertices; checking a partition takes milliseconds) |
| ★★★☆☆ | [IHTC-2024 competition (m01-m30) instances: lower a best known integrated surgery-admissio…](ihtp-ihtc2024-hidden-m-instances-upper-bounds.md) | harvest | laptop-hours |
| ★★★☆☆ | [Integrated Healthcare Timetabling (IHTC-2024): lower the best known cost of a public (i01…](ihtp-ihtc2024-upper-bounds.md) | harvest | laptop-hours |
| ★★★☆☆ | [MMLIB / Boctor multi-mode resource-constrained project scheduling: shorter makespan for a…](mmlib-multimode-rcpsp-ub.md) | harvest | laptop-hours |
| ★★★☆☆ | [MaxSAT Evaluation benchmarks: beat the best known cost of an instance whose optimum is un…](maxsat-evaluation-best-known-cost.md) | harvest | laptop-hours per instance (anytime MaxSAT solvers, SAT-based local search, LNS); instance archives are large (2-5 GB zips per 2026 track) |
| ★★★☆☆ | [Multi-activity multi-day shift scheduling (Curtois-Qu MATSP instances 1-225): beat a best…](matsp-multi-activity-shift-scheduling.md) | harvest | laptop-hours |
| ★★★☆☆ | [OptiWindNet RouteSets: a shorter offshore wind-farm array-cable network than the best sto…](optiwindnet-routesets-cable-routing-records.md) | harvest | laptop-hours (16-210 turbines per site; MILP or HGS/LKH-style heuristics) |
| ★★★☆☆ | [QPLIB: better solution point for a quadratic (including QAP-type and Max-Cut-type binary)…](qplib-better-solution-point.md) | harvest | laptop-hours |
| ★★★☆☆ | [RCPLIB (Vanhoucke-Coelho) RG300 and DC2 resource-constrained project scheduling: shorter…](rcplib-rg300-dc2-rcpsp-ub.md) | harvest | laptop-hours |
| ★★★☆☆ | [SMT-COMP 2026 P4/DFA bit-vector holdouts: one exact SAT model or UNSAT certificate](smt2026-p4-dfa-unknown-certificates.md) | harvest | laptop-hours to laptop-days using alternative preprocessing and solver configurations; require model/proof checking within laptop-hours |
| ★★★☆☆ | [SteinLib PUC and I640: a cheaper Steiner tree for one of the 32 unsolved instances (hyper…](steinlib-puc-i640-open-upper-bounds.md) | harvest | laptop-hours to laptop-days per instance (graphs of 640 to 4,096 vertices and up to 28,512 edges; checking a tree takes milliseconds) |
| ★★★☆☆ | [XHSTT high school timetabling (Post archive): beat a best known solution cost on an open…](xhstt-2014-high-school-timetabling-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [2D irregular strip packing (nesting, ESICUP and Gardeyn instances): a shorter strip than…](esicup-nesting-sparrow-strip-length-records.md) | harvest | laptop-hours (multi-core helps; the records came from 20-minute 16-core runs and longer record hunts) |
| ★★☆☆☆ | [ARPA-E GO Competition Challenge 1 (continuous SCOPF): beat the best Final Event score on…](go1-final-event-scopf-best-scores.md) | harvest | laptop-hours (networks of a few hundred to tens of thousands of buses; contingency evaluation dominates) |
| ★★☆☆☆ | [CHC-COMP 2026: first validated model or refutation for a Horn-clause task no solver answe…](chc-comp-2026-unknown-status-first-solve.md) | harvest | laptop-hours to laptop-days per task (portfolio of Eldarica, Golem, Spacer, MuCyc and custom invariant search); validating a model or refutation takes seconds to minutes |
| ★★☆☆☆ | [CVRPLIB VRPTW (Gehring-Homberger, DIMACS truncated-distance objective): beat an open best…](cvrplib-vrptw-gh-dimacs-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [CVRPLIB: beat a best-known solution on an open X, XL or Arnold-XXL CVRP instance](cvrplib-x-xl-xxl-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Flexible job shop (FJSPLib: Brandimarte mk10, Dauzere-Peres-Paulli, Behnke-Geiger, Hurink…](fjsplib-flexible-jobshop-open-ub.md) | harvest | laptop-hours |
| ★★☆☆☆ | [ITC-2007 examination timetabling (track 1): beat the best known penalty on one of the 12…](itc2007-exam-timetabling-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [ITC2021 sports timetabling: lower the best known penalty of an open instance](itc2021-sports-timetabling-ub.md) | harvest | laptop-hours |
| ★★☆☆☆ | [MIPLIB 2017: improve the best known objective of an open collection instance](miplib2017-open-primal-bound.md) | harvest | laptop-hours |
| ★★☆☆☆ | [QOBLIB network design (Bienstock-Gunluk demands): a 2-in/2-out digraph and routing with l…](qoblib-network-design-max-flow.md) | standard | laptop-hours (n = 11..24 nodes; scoring a topology is one min-congestion multicommodity-flow LP) |
| ★★☆☆☆ | [SINTEF Li & Lim PDPTW benchmark: hierarchically beat a best-known solution on a 600/800/1…](sintef-lilim-pdptw-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [SINTEF VRPTW (Gehring-Homberger, hierarchical objective): fewer vehicles, or equal vehicl…](sintef-vrptw-gh-hierarchical-bks.md) | harvest | laptop-hours |
| ★★☆☆☆ | [SMT-LIB nonlinear integer arithmetic (QF_NIA): a checked answer for an unknown-status ben…](smtlib-qf-nia-unknown-certificates.md) | harvest | laptop-hours per benchmark (cvc5, z3, Yices, local search for NIA, bit-blasting with bounds); certificate checks seconds to hours |
| ★★☆☆☆ | [TimPassLib: a periodic timetable with lower total passenger travel time than the best kno…](timpasslib-integrated-timetabling-routing.md) | harvest | laptop-hours (instances from 32 to 21,328 events; evaluating one timetable is a series of shortest-path runs, seconds) |
| ★★☆☆☆ | [Traveling Tournament Problem (RobinX repository): shorter total travel for an open NL, NF…](robinx-ttp-traveling-tournament-ub.md) | harvest | laptop-hours |
| ★★☆☆☆ | [0-1 multidimensional knapsack: beat a best known value on an OR-Library 30.500 (Chu-Beasl…](orlib-mkp-chu-beasley-30-500-and-gk.md) | harvest | laptop-hours (a 500 x 30 instance file is about 70 KB; record runs used 2 h per seed with a MIP solver inside an evolutionary loop) |
| ★★☆☆☆ | [ARPA-E GO Competition Challenge 2 (SCOPF with switching): beat a Monarch of the Mountain…](go2-monarch-of-the-mountain-scopf.md) | harvest | laptop-days (617- to 31,777-bus networks with hundreds of contingencies; 16+ GB RAM for the largest) |
| ★★☆☆☆ | [Curriculum-based course timetabling (ITC-2007 track 3, UD2): beat the best known penalty…](cb-ctt-itc2007-comp-open-instances.md) | harvest | laptop-days |
| ★★☆☆☆ | [Gset Max-Cut: a larger cut than the best published for a non-toroidal Gset graph (G60 141…](gset-maxcut-nontoroidal-records.md) | harvest | laptop-days (GPU or many-core local search on graphs of 800 to 10,000 vertices; checking a cut takes milliseconds) |
| ★★☆☆☆ | [HWMCC'25: first certified answer for a hardware model-checking benchmark that no particip…](hwmcc25-unsolved-first-certified.md) | harvest | laptop-days per benchmark (IC3/PDR, BMC, k-induction portfolios; a 16-core machine helps); certificate checking takes minutes to hours |
| ★★☆☆☆ | [Job-shop scheduling: lower the makespan upper bound on an open Taillard / Demirkol / SWV…](jsp-optimizizer-open-upper-bounds.md) | harvest | laptop-hours |
| ★★☆☆☆ | [MINLPLib finance and marketing instances still open: beat saa_2 (strategic asset allocati…](minlplib-finance-open-instances.md) | standard | laptop-hours (saa_2 has 4,408 variables and 400 binaries but may reduce to a few asset weights plus a funding scalar; pricing050 has 50 continuous variables) |
| ★★☆☆☆ | [MINLPLib: better feasible point for an open mixed-integer nonlinear instance](minlplib-open-primal-bound.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Nurse rostering benchmark (Curtois / schedulingbenchmarks.org): close an open gap on BCV-…](curtois-nrp-open-gaps-bcv-mer-instance24.md) | standard | laptop-hours |
| ★★☆☆☆ | [PESPlib periodic timetabling: lower the best known weighted slack of a railway instance R…](pesplib-periodic-timetabling-records.md) | harvest | laptop-hours (instances have 2,600-8,400 events and 6,400-18,000 activities; files are a few hundred KB) |
| ★★☆☆☆ | [PSPLIB J120 (single-mode RCPSP): lower a best known heuristic makespan on an unproven ins…](psplib-j120-rcpsp-upper-bounds.md) | harvest | laptop-hours |
| ★★☆☆☆ | [Permutation flow shop (Taillard benchmarks): a makespan below the best known for one of t…](pfsp-taillard-open-makespans.md) | harvest | laptop-hours to laptop-days (50-200 jobs x 20 machines; VRF up to 800 x 60; one makespan evaluation takes microseconds) |
| ★★☆☆☆ | [SAT Competition 2026: first certified solve of a Main-track instance whose result is unkn…](sat-competition-2026-unknown-first-solve.md) | harvest | laptop-days per instance (portfolio of CDCL and local-search solvers, cube-and-conquer on a multi-core machine); an UNSAT proof from a multi-day run can need tens to hundreds of GB of disk |
| ★★☆☆☆ | [Sartori-Buriol real-road PDPTW instances (100-5000 locations): hierarchically beat a best…](sartori-buriol-pdptw-bks.md) | harvest | laptop-hours (instance files carry full OSRM travel-time matrices, up to 5000 x 5000 integers) |
| ★★☆☆☆ | [Social Golfer Problem (CSPLib 010): more rounds than the 2026 Miller-Valkov-Abel table fo…](social-golfer-design-table-gaps.md) | harvest | laptop-hours (SAT/CP or design-theoretic search; schedules are a few kilobytes) |
| ★★☆☆☆ | [VLSI TSP collection (Bonn / Waterloo): a shorter tour for one of the 30 unsolved instance…](tsp-vlsi-open-tours.md) | harvest | laptop-hours to laptop-days (EUC_2D, 14k-745k cities; checking a tour takes seconds) |
| ★★☆☆☆ | [Walshaw Graph Partitioning Archive: beat a best known edge cut (k = 2..64, 0/1/3/5% imbal…](walshaw-graph-partitioning-archive.md) | harvest | laptop-hours |
| ★★☆☆☆ | [DIMACS graph colouring: a proper colouring with fewer colours than the best known for an…](dimacs-colouring-open-upper-bounds.md) | harvest | laptop-hours to laptop-days (250 to 4,000 vertices; checking a colouring takes seconds) |
| ★★☆☆☆ | [National TSPs: a shorter tour for Burma (bm33708) or China (ch71009), the two unsolved Wa…](tsp-national-bm33708-ch71009.md) | standard | laptop-days (33,708 and 71,009 cities, EUC_2D; checking a tour takes seconds) |
| ★★☆☆☆ | [PGLib-OPF v23.07: an AC-feasible dispatch cheaper than the published baseline on a large…](pglib-opf-v2307-ac-cheaper-dispatch.md) | harvest | laptop-hours (1,803- to 78,484-bus cases; multistart Ipopt or global-solver heuristics) |
| ★★☆☆☆ | [QAPLIB: a permutation beating the best known value of one of the 28 unsolved instances (t…](qaplib-open-instances-bkv.md) | harvest | laptop-hours to laptop-days (n = 35..256; evaluating a permutation is O(n^2), a swap delta O(n)) |
| ★★☆☆☆ | [TSP Art (Bosch): a shorter tour for vangogh120K, venus140K, pareja160K, courbet180K or ea…](tsp-art-bosch-five-instances.md) | standard | laptop-days (120k-200k cities, EUC_2D; checking a tour takes seconds) |
| ★★☆☆☆ | [TSPTW makespan (Lopez-Ibanez collection): beat the best-known makespan 917.83 of rc_204.1…](tsptw-lopez-ibanez-open-cells.md) | standard | laptop-hours to laptop-days (one 46-node asymmetric instance with 4-decimal travel times; anytime DP, beam search or LNS runs) |
| ★☆☆☆☆ | [MOONSHOT - World TSP (1,904,711 cities): a tour shorter than Nagata's 7,515,755,912](world-tsp-shorter-tour.md) | moonshot | laptop-days to weeks (1.9M cities with the GEOM great-circle metric; 11.5 MB instance; checking a tour takes about a minute in Python) |

← [All categories](../README.md)
