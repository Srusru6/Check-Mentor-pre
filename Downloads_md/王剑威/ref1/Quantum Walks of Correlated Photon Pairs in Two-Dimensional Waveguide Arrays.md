# Quantum Walks of Correlated Photon Pairs in Two-Dimensional Waveguide Arrays

Konstantinos Poulios, $^{1}$  Robert Keil, $^{2}$  Daniel Fry, $^{1}$  Jasmin D. A. Meinecke, $^{1}$  Jonathan C. F. Matthews, $^{1}$  Alberto Politi, $^{1,*}$  Mirko Lobino, $^{1,†}$  Markus Grafe, $^{2}$  Matthias Heinrich, $^{2,‡}$  Stefan Nolte, $^{2}$  Alexander Szameit, $^{2}$  and Jeremy L. O'Brien $^{1,§}$ $^{1}$ Centre for Quantum Photonics, H. H. Wills Physics Laboratory and Department of Electrical and Electronic Engineering, University of Bristol, Merchant Venturers Building, Woodland Road, Bristol BS8 1UB, United Kingdom  
 $^{2}$ Institute of Applied Physics, Friedrich-Schiller-Universität Jena, Max-Wien-Platz 1, D-07743 Jena, Germany  
(Received 17 July 2013; published 10 April 2014)

We demonstrate quantum walks of correlated photons in a two-dimensional network of directly laser written waveguides coupled in a "swiss cross" arrangement. The correlated detection events show high-visibility quantum interference and unique composite behavior: strong correlation and independence of the quantum walkers, between and within the planes of the cross. Violations of a classically defined inequality, for photons injected in the same plane and in orthogonal planes, reveal nonclassical behavior in a nonplanar structure.

DOI: 10.1103/PhysRevLett.112.143604

PACS numbers: 42.50.-p, 05.60.Gg, 42.50.Ex, 42.82.Et

Quantum walks (QWs) are an illustrative example for the indeterminism inherent to quantum mechanics [1]. They are used to model a variety of processes from excitation transfer across spin chains [2,3] to energy transport in photosynthetic complexes [4]. They enable studying large scale quantum interference [5] and their simulation on a quantum computer provides a route to universal quantum computing [6]. One-dimensional (1D) networks provide a conceptually straight-forward and readily implementable way of realising QWs.

There is now a plethora of single particle Qw implementations across different platforms [7-17]; however, the dynamics of single particle QWs can be described in the context of classical wave theory [18]. QWs of multiple indistinguishable particles, on the other hand, have been shown to exhibit nonclassical correlations. In general, they cannot be described by considering separately the quantum state of each particle and their features cannot be mimicked with classical light without limiting the visibility of observed quantum interference [19] or the introduction of an increasing number of experiments [20-22]. Furthermore, the Hilbert space that describes multiparticle QWs grows exponentially with the linear increase in particle number and network size [5,23].

An additional physical dimension in the network can, in principle, entail the degrees of freedom offered by two walkers on a 1D network [22,24,25]. Moreover, the additional physical dimension enables network configurations (directly mapping to graph structures) that are not otherwise available, allowing for example a selective degree of connectivity for different single sites (vertices) in the structure and asymmetries in the network. Many interesting problems, such as energy transport in biological systems [4,26], graph theory problems [27] and quantum search algorithms [28-30], require two-dimensional (2D) graphs,

with a high degree of connectivity, where vertices are connected to multiple edges.

A promising route towards the realisation of networks with topologies beyond 1D, nearest-neighbor coupled geometries is the direct laser inscription of waveguides in transparent substrates. This technique allows fabrication of complex 2D networks on a single optical chip. It overcomes the limitations of established lithographic methods and allows implementation of intricate topologies in an integrated fashion. The quantum behavior of single photons in simple planar arrangements of laser written waveguides, such as directional couplers, has been demonstrated with high visibility [31]. The additional dimension allowed by the direct laser write technique has also been employed to compensate for polarization dependent coupling [32] and altering the boundary conditions of 1D QWs [33].

In this work we implement QWs of two indistinguishable photons in a 2D waveguide lattice with sites that have a high degree of connectivity. This lattice was fabricated in fused silica with the direct laser write technique [34]. We observe correlations that strongly violate the limit for classical light propagating in the network, illustrating high-visibility quantum interference at the single photon level.

The Hamiltonian for a system of  $N$  evanescently coupled waveguides is given by [20]

$$
\hat {H} = \sum_ {q = 1} ^ {N} \left(\beta_ {q} a _ {q} ^ {\dagger} a _ {q} + \sum_ {r = 1} ^ {N} C _ {q, r} a _ {r} ^ {\dagger} a _ {q}\right) \tag {1}
$$

and is equivalent to the adjacency matrix of the graph representing the waveguide structure, where  $a_{q}^{(\dagger)}$  is the bosonic annihilation (creation) operator for a photon in waveguide  $q$ ,  $\beta_{q}$  is the propagation constant of guide  $q$  and  $C_{q,r}$  is the coupling strength between waveguides  $q$  and  $r$ . In general each waveguide can be coupled to several other waveguides, enabling the fabrication of structures that

directly map to graphs with a high degree of connectivity, with different coupling strengths for nearest and non-nearest neighboring waveguides.

For two indistinguishable input photons in waveguides  $q$  and  $r$ , the probability of detecting one photon in output waveguide  $q'$ , coincident with the other photon in waveguide  $r'$  is given by the correlation function [35]:

$$
\Gamma_ {q ^ {\prime}, r ^ {\prime}} ^ {(q, r)} = \frac {1}{1 + \delta_ {q ^ {\prime} , r ^ {\prime}}} \left| U _ {q ^ {\prime}, q} U _ {r ^ {\prime}, r} + U _ {q ^ {\prime}, r} U _ {r ^ {\prime}, q} \right| ^ {2}. \tag {2}
$$

with  $U = \exp(-iHz)$  as the evolution unitary of the system and  $z$  as the evolution length.

A sufficient criterion for nonclassical behavior is a violation of the inequality [5,19],

$$
V _ {q, r} = \frac {2}{3} \sqrt {\Gamma_ {q , q} ^ {c l} \Gamma_ {r , r} ^ {c l}} - \Gamma_ {q, r} ^ {c l} <   0, \tag {3}
$$

with  $\Gamma^{cl}$  here referring to intensity correlations between classical light beams. This inequality imposes a limit to the magnitude of the on-diagonal terms in the correlation matrix in comparison to the associated off-diagonal elements. Its violation in the quantum regime is a sign of photon bunching.

The waveguides of the QW network in this work are labeled as in Fig. 1(a), where waveguides that have first order coupling in the horizontal (vertical) plane are denoted with a prefix  $X(Y)$ . The central waveguide has first order coupling in both the horizontal and vertical plane and is labeled as  $C$ . For a single particle walk the size of the Hilbert space coincides with the size of the physical network structure. For a two-particle input the Hilbert space grows larger. This two-particle configuration space can be interpreted as the Hilbert space of a single-particle QW on a more complex graph with a probability distribution equalling the original two-particle correlation function. The on-site potentials and hopping amplitudes in this simulated single particle graph can be deduced from considering the Heisenberg equation of motion  $(d / dz)\hat{A} (z) = [\hat{H},\hat{A}]$  for the Hamiltonian of the physical

![](images/bae249018f6f993d4f474bf2f25a16f2c8c08c2600bc7943a11124fd56e21b96.jpg)  
FIG. 1 (color online). (a) Schematic of the 2D evanescently coupled waveguide array. The coupling constant  $C^{(1)}$  is for adjacent waveguides and the second order coupling is denoted as  $C^{(2)}$ . (b) Schematic of the interface section of our waveguide circuit, showing the input waveguides fanning from a planar configuration to the 2D, swiss cross configuration.

network Eq. (1) with single particle input  $\hat{A} = a_q^\dagger$  and two particle input  $\hat{A} = a_q^\dagger a_r^\dagger$  as described in [5]. The single-particle graph structure corresponding to two-particles on the swiss cross structure is shown in Fig. 2 [36].

We measured correlation matrices for two different input states, one corresponding to injection of the twin photons in waveguides located on the same plane (waveguides  $X1$  and  $X4$ ) and also in waveguides located on orthogonal planes ( $X1$  and  $Y1$ ) [36]. By varying the relative temporal delay between the two input photons, their degree of indistinguishability was tuned. The nonclassical nature of the correlations measured can be quantified by the violations of inequality (3).

In the correlation matrices summarized in Fig. 3 one can identify four regions, two for correlated detection events between output waveguides in the same plane  $(\Gamma_{X1 - X4,X1 - X4};$ $\Gamma_{Y1 - Y4,Y1 - Y4})$  and two for events between waveguides in different planes  $(\Gamma_{X1 - X4,Y1 - Y4};\Gamma_{Y1 - Y4,X1 - X4})$ . From these it can be seen that the distinct features that appear for indistinguishable photons and the violations of the classical limit spread throughout the 2D network. The observed behavior therefore cannot be attributed to independent, 1D, single photon QWs, but rather is characteristic of a single 2D QW

![](images/031de631526dd6f3759922a449a37441f5816e6a9d3c3e31196a70b45acf6d4f.jpg)  
FIG. 2 (color online). Graph structure simulated with a two-photon input state in the swiss cross structure shown in Fig. 1(a). Each of the 45 vertices corresponds to a two-particle state, with different degrees of connectivity (up to degree 8), and there are 126 links between different vertices corresponding to allowed transitions between two-particle states. Red lines and red vertices correspond to coupling strengths of  $C$  and potentials of  $\beta$ , respectively, so they coincide with the ones in the swiss cross structure. For vertices corresponding to a state with two particles in the same waveguide, the on site potential and the coupling are enlarged by a factor of 2 and  $\sqrt{2}$  respectively, due to normalisation of the two-particle wavefunction. We mark these vertices and links in green. The two yellow vertices represent the two different two-photon input states in the experiment ( $X1 - X4$  and  $X1 - Y1$ ). Two different complete connecting paths ( $|X1X1\rangle$  to  $|X4X4\rangle$  and  $|X1X1\rangle$  to  $|Y1Y1\rangle$ ) are labeled as examples.

![](images/9aa3a9c4fa33246336d4720a8837bbe349bcf643ff25d3e5a48ee0f196f82e69.jpg)  
(a)

![](images/cb386d47c3d2d0257ecee39e47f3cf3c43d4b737a1c541a30f6aa55c42442eff.jpg)  
(b)

![](images/970b901bf43f82526034b449a4091b8385f4c7792d2652c819f764f7cd8274c6.jpg)  
(c)

![](images/25660a0ec928f1debb3126753fca579106700ce0a10cc58fcd89ca79d5979ae9.jpg)  
(d)

![](images/329db8fa7e2a20647cbc73a3cda19708885257cbb70f70e0f3cac759dd91d11b.jpg)  
(e)  
FIG. 3 (color online). Correlation matrices for the two different input combinations. Top row is for inputting the two photons on the same plane in opposite corners  $(X1$  and  $X4)$ . The measured results for delays leading to (a) distinguishable and (b) indistinguishable photons are presented together with (c) the numerical simulation and (d) the violations (V) of inequality (3) (measured in standard deviations  $\sigma$ , assuming Poissonian statistics for each individual coincidence count and propagating the error—white cells represent no violation), both for the case of indistinguishable photons. The bottom row shows the corresponding results for inputting the two photons in different planes in adjacent corners  $(X1$  and  $Y1)$ . For both inputs, violations of the inequality for distinguishable photons were not observed, as was expected.

![](images/6203c13f654a92ab5137d0050b71bc1ac0705f44faaa48fbca3f5a29ac5864b2.jpg)  
(f)

![](images/96286b5de9a1423cf1e8b82052dca441649a2ebe2bd96af51590f015d2c4aafe.jpg)  
(g)

![](images/7a632281d25e040b8bcdb3591a655b3d5166c99e9a9955cbaaac7c7378780d40.jpg)  
(h)

of two correlated photons. Different strengths of the violations observed for each individual waveguide pair, reflect the fact that bunching is not equally likely, due to the variety of photon paths contributing to the quantum interference.

A measure of the quality of nonclassical interference within the network can be obtained by looking at the diagonal elements of the correlation matrices, i.e., the coincidence of the two photons in the same output waveguide. The maximum visibility of nonclassical interference for these diagonal elements depends solely on the quality of the indistinguishability between the two photons inside the quantum network, irrespective of the network structure and the evolution length of the coupling region [35,37]. Fig. 4 shows one of the peaks measured with visibility  $V = 96.8 \pm 2.5\%$ , demonstrating the high quality non-classical interference in our devices.

For a comparison of our experimental results with theory, we calculated the similarities  $S = \left(\sum_{q',r'}\sqrt{\Gamma_{q',r'}^{\exp}\cdot\Gamma_{q',r'}^{th}}\right)^2 / \left(\sum_{q',r'}\Gamma_{q',r'}^{\exp}\sum_{q',r'}\Gamma_{q',r'}^{th}\right)$  between the experiments and simulations. For the simulations the propagation and coupling constants were deduced from classical light measurements via numerical optimisation and the input coupling efficiencies of single waveguides from single photon measurements [36]. Exhibiting a similarity of 93.97% with respect to the simulations, the experimental results for photons injected in the same plane are in good agreement with the theoretical predictions [Fig. 3(c)]. However the similarity drops to 81.7% for injection of the photons in orthogonal

planes [Fig. 3(g)]. The similarities for distinguishable photons are  $98.5\%$  for both input cases.

The observable discrepancy between Figs. 3(f) and (g) shows that our model does not fully incorporate all lattice parameters (additional phases or whether the array maintains indistinguishability [36]). Support of quantum interference by our 2D structure is proven by the violations in Figs. 3(d) and (h) and the following evidence: (i) The diagonal peaks, corresponding to the probability to detect bunched photons, in Fig. 3(f) are substantially increased due to constructive interference—the majority of them is doubled as predicted by theory—in comparison to the distinguishable case in Fig. 3(e). (ii) We observe clearly differing behavior of correlations in the  $X$  and  $Y$  plane of the structure for distinguishable and indistinguishable cases. For example, if we consider photon  $q^{\prime}$  to occupy either  $X1$  or  $X3$ , two of the four highest peaks  $[(X1, C)$ ,  $(X1, Y2)$ ,  $(X3, C)$  and  $(X3, Y2)]$  in the distinguishable case [Fig. 3(e)] vanish in the indistinguishable case [Fig. 3(f);  $(X1, Y2)$ ,  $(X3, C)]$  even though they are allowed by the single photon trajectories—while the other two increase.

To elucidate the impact of the particular swiss cross geometry on the QW, it is instructive to investigate the correlation among the branches [left -  $L$ , right -  $R$ , up -  $U$ , down -  $D$ , Fig. 5(a)], as obtained by summation over their constituent waveguides' individual coincidences  $\Gamma_{q',r'}^{(X1,X4)}$ . Figures 5(b)-(d) show the results of this analysis. Strong violations arise across the planes spanned by the input

![](images/4fab69fbf1c895246efdc0d406135a833b3afe98a7f49d90860050e6bf088b03.jpg)  
FIG. 4 (color online). Quantum interference peak observed when varying the relative free-space delay of the twin photons and monitoring the presence of both photons in the same waveguide using a balanced fiber beam splitter butt-coupled to the output waveguide. This particular peak is for both photons input on the same plane  $(X1, X4)$  and monitoring output waveguide  $X3$ , showing a visibility of  $96.8 \pm 2.5\%$ . (Error bars indicate the standard deviation of the underlying Poissonian photon counting statistics.)

branches  $(L$  and  $R)$  on one side and  $U$  and  $C$  on the other side as visible in Fig. 5(d). This is reflected in a suppression of the off-diagonals  $\Gamma_{L(R),U(C)}^{(X1,X4)}$  in Fig. 5(c) compared to the distinguishable case in Fig. 5(b). Hence, the photons tend to occupy either the input branches or the vertical branch/center. This phenomenon is reminiscent of photon bunching observed in 1D lattices [5,19]. In contrast, large off-diagonals  $\Gamma_{U,C}^{(X1,X4)}$  and  $\Gamma_{L,R}^{(X1,X4)}$  persist in Fig. 5(c), which means that no bunching, and consequently no violation, occurs within the two planes. Moreover, the single waveguide violations matrix [Fig. 3(d)] reveals no intrabranch violations either. These observations imply that

the photons are distributed almost independently, i.e., behave like distinguishable particles, in each of the two regions. This composite behavior of path entanglement and independence is a direct consequence of the nonplanar geometry of the 2D network, confirming theoretical predictions [20]. One also notices the low probability for detecting photons in the lower branch  $(D)$ . The simulations suggest that this can be attributed to weaker coupling between this branch and the others—most likely induced by positioning errors during fabrication—with some contribution of unevenly distributed losses in the interface segment as well (Fig. 1(b) and [36]).

We have experimentally implemented a 2D, two-photon QW by using waveguide arrays in a swiss cross geometry—a building block for larger lattice-based structures. We demonstrated two-photon quantum interference with high visibility on fully 3D integrated waveguide device with features that cannot be observed in planar arrangements, including the combination of strong correlation and independence of the quantum walkers between and within the planes of the cross. The ability to inscribe waveguides in three dimensions enables implementation of networks with topologies that go beyond the restriction of lithographic methods. Furthermore, QWs of multiple particles enable the simulation of graph structures which are not implementable as a physical waveguide structure, e.g., the corresponding simulated graph for the swiss cross network in Fig. 2. The implications from using entanglement to simulate boson and fermion statistics [32,38] as well as precise control of the boundary conditions of the system [39] in 2D settings remain to be investigated. Together with the possibility of introducing interactions between particles (e.g., measurement-induced [40] or simulating 1D interactions with 2D lattices [41]), this may open ways for new directions in analogue quantum simulations and quantum computing [42].

The authors would like to thank Lana Beck for helpful discussions. This work was supported by EPSRC, ERC,

![](images/e02c3d5a256e2e45073c0e4447804e00334f688ceb6c8672109d64b56d4ca12e.jpg)  
FIG. 5 (color online). (a) Schematic of the 2D waveguide array when summing correlations over sites within the different branches. (b)-(c) Correlation matrices between the branches for inputting the two photons on the same plane in opposite corners  $(X1$  and  $X4)$ , showing the (b) distinguishable and (c) indistinguishable case. (d) Violations (V) of inequality (3) (measured in standard deviations  $\sigma$ , assuming Poissonian statistics for each individual coincidence count and propagating the error—white cells represent no violation) for indistinguishable photons. No violations were observed for distinguishable photons, as was expected.

![](images/25c64a60abcae986b4e220430357b25e0445e722d9886c8ad8deea023db66e6d.jpg)

![](images/211ebf0f4129f59538e643d6f45a7e56ec5467e7f5ab604b343c7d89861adb7f.jpg)

![](images/41ad0f82f2c173fb61382cd9f0ecfbaf2a8a70a1ac70390e2cb26be0fcd04b7e.jpg)

QUANTIP, PHORBITECH, BMBF (ZIK 03Z1HN31, Ultra Optics 2015) and TMBWK (Research group Spacetime, Grant No. 11027-514). R.K. was supported by the Abbe School of Photonics. J.C.F.M. is supported by a Leverhulme Trust Early Career Fellowship. M.H. was supported by the German National Academy of Sciences Leopoldina (Grant No. LPDS 2012-01). J.L. O'B. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies.

*Present address: School of Physics and Astronomy, University of Southampton, Southampton SO17 1BJ, United Kingdom.  
Present address: Centre for Quantum Dynamics and Queensland Micro and Nanotechnology Centre, Griffith University, Brisbane QLD 4111, Australia.  
Present address: CREOL, The College of Optics and Photonics, University of Central Florida, 4000 Central Florida Blvd., Orlando FL 32816, USA.  
Jeremy.OBrien@bristol.ac.uk  
[1] Y. Aharonov, L. Davidovich, and N. Zagury, Phys. Rev. A 48, 1687 (1993).  
[2] S. Bose, Phys. Rev. Lett. 91, 207901 (2003).  
[3] M. Christandl, N. Datta, A. Ekert, and A. J. Landahl, Phys. Rev. Lett. 92, 187902 (2004).  
[4] M. B. Plenio and S. F. Huelga, New J. Phys. 10, 113019 (2008).  
[5] A. Peruzzo, M. Lobino, J.C.F. Matthews, N. Matsuda, A. Politi, K. Poulios, X.-Q. Zhou, Y. Lahini, N. Ismail, K. Worhoff, Y. Bromberg, Y. Silberberg, M.G. Thompson, and J.L. O'Brien, Science 329, 1500 (2010).  
[6] A.M. Childs, Phys. Rev. Lett. 102, 180501 (2009).  
[7] H. Schmitz, R. Matjeschk, C. Schneider, J. Glueckert, M. Enderlein, T. Huber, and T. Schaetz, Phys. Rev. Lett. 103, 090504 (2009).  
[8] F. Zähringer, G. Kirchmair, R. Gerritsma, E. Solano, R. Blatt, and C. F. Roos, Phys. Rev. Lett. 104, 100503 (2010).  
[9] M. Karski, L. Forster, J.-M. Choi, A. Steffen, W. Alt, D. Meschede, and A. Widera, Science 325, 174 (2009).  
[10] D. Bouwmeester, I. Marzoli, G. P. Karman, W. Schleich, and J. P. Woerdman, Phys. Rev. A 61, 013410 (1999).  
[11] C. A. Ryan, M. Laforest, J. C. Boileau, and R. Laflamme, Phys. Rev. A 72, 062317 (2005).  
[12] J. Du, H. Li, X. Xu, M. Shi, J. Wu, X. Zhou, and R. Han, Phys. Rev. A 67, 042316 (2003).  
[13] B. Do, M. L. Stohler, S. Balasubramanian, D. S. Elliott, C. Eash, E. Fischbach, M. A. Fischbach, A. Mills, and B. Zwickl, J. Opt. Soc. Am. B 22, 499 (2005).  
[14] M. A. Broome, A. Fedrizzi, B. P. Lanyon, I. Kassal, A. Aspuru-Guzik, and A. G. White, Phys. Rev. Lett. 104, 153602 (2010).  
[15] A. Schreiber, K. N. Cassemiro, V. Potoček, A. Gábris, P. J. Mosley, E. Andersson, I. Jex, and C. Silberhorn, Phys. Rev. Lett. 104, 050502 (2010).  
[16] A. Schreiber, K. N. Cassemiro, V. Potoček, A. Gabris, I. Jex, and C. Silberhorn, Phys. Rev. Lett. 106, 180403 (2011).  
[17] H. B. Perets, Y. Lahini, F. Pozzi, M. Sorel, R. Morandotti, and Y. Silberberg, Phys. Rev. Lett. 100, 170506 (2008).

[18] P. L. Knight, E. Roldán, and J. E. Sipe, Phys. Rev. A 68, 020301(R) (2003).  
[19] Y. Bromberg, Y. Lahini, R. Morandotti, and Y. Silberberg, Phys. Rev. Lett. 102, 253904 (2009).  
[20] R. Keil, A. Szameit, F. Dreisow, M. Heinrich, S. Nolte, and A. Tünnermann, Phys. Rev. A 81, 023834 (2010).  
[21] R. Keil, F. Dreisow, M. Heinrich, A. Tunnermann, S. Nolte, and A. Szameit, Phys. Rev. A 83, 013808 (2011).  
[22] A. Schreiber, A. Gabris, P. Rohde, K. Laiho, M. Štefánek, V. Potoček, C. Hamilton, I. Jex, and C. Silberhorn, Science 336, 55 (2012).  
[23] P. P. Rohde, A. Schreiber, M. Stefanak, I. Jex, A. Gilchrist, and C. Silberhorn, arXiv:1205.1850.  
[24] S. Longhi, Opt. Lett. 36, 3248 (2011).  
[25] M. Gräfe, A. S. Solntsev, R. Keil, A. A. Sukhorukov, M. Heinrich, A. Tünnermann, S. Nolte, A. Szameit, and Y. S. Kivshar, Sci. Rep. 2, 562 (2012).  
[26] M. Mohseni, P. Rebentrost, S. Lloyd, and A. A. Guzik, J. Chem. Phys. 129, 174106 (2008).  
[27] J. M. Harrison, J. P. Keating, and J. M. Robbins, Proc. R. Soc. A 467, 212 (2010).  
[28] A. M. Childs, R. Cleve, E. Deotto, E. Farhi, S. Gutmann, and D. A. Spielman, in Proceedings of the Thirty-Fifth Annual ACM Symposium on Theory of Computing, STOC '03 (ACM, New York, 2003), p. 59.  
[29] C. Di Franco, M. Mc Getrick, and T. Busch, Phys. Rev. Lett. 106, 080502 (2011).  
[30] Y.-C. Jeong, C. Di Franco, H.-T. Lim, M. Kim, and Y.-H. Kim, Nat. Commun. 4, 2471 (2013).  
[31] G. D. Marshall, A. Politi, J. C. F. Matthews, P. Dekker, M. Ams, M. J. Withford, and J. L. O'Brien, Opt. Express 17, 12546 (2009).  
[32] L. Sansoni, F. Sciarrino, G. Vallone, P. Mataloni, A. Crespi, R. Ramponi, and R. Osellame, Phys. Rev. Lett. 108, 010502 (2012).  
[33] J. O. Owens, M. A. Broome, D. N. Biggerstaff, M. E. Coggin, A. Fedrizzi, T. Linjoret, M. Ams, G. D. Marshall, J. Twamley, M. J. Withford, and A. G. White, New J. Phys. 13, 075003 (2011).  
[34] A. Szameit and S. Nolte, J. Phys. B 43, 163001 (2010).  
[35] K. Mattle, M. Michler, H. Weinfurter, A. Zeilinger, and M. Zukowski, Appl. Phys. B 60, 111 (1995).  
[36] For more information, see Supplemental Material at http:// link.aps.org/supplemental/10.1103/PhysRevLett.112.143604 for an outline of the experimental setup and the classical characterisation and losses of the waveguide network.  
[37] J. G. rarity and P. R. Tapster, J. Opt. Soc. Am. B 6, 1221 (1989).  
[38] J. C. F. Matthews, K. Poulios, J. D. A. Meinecke, A. Politi, A. Peruzzo, N. Ismail, K. Wörhoff, M. G. Thompson, and J. L. O'Brien, Sci. Rep. 3, 1539 (2013).  
[39] J. D. A. Meinecke, K. Poulios, A. Politi, J. C. F. Matthews, A. Peruzzo, N. Ismail, K. Wörhoff, J. L. O'Brien, and M. G. Thompson, Phys. Rev. A 88, 012308+ (2013).  
[40] E. Knill, R. Laflamme, and G. J. Milburn, Nature (London) 409, 46 (2001).  
[41] G. Corrielli, A. Crespi, G. Della Valle, S. Longhi, and R. Osellame, Nat. Commun. 4, 1555 (2013).  
[42] A. M. Childs, D. Gosset, and Z. Webb, Science 339, 791 (2013).