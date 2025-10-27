# Experimental quantum fast hitting on hexagonal graphs

Hao Tang $^{1,2,3}$ , Carlo Di Franco $^{4,5}$ , Zi-Yu Shi $^{1,3}$ , Tian-Shen He $^{1}$ , Zhen Feng $^{1,3}$ , Jun Gao $^{1,3}$ , Ke Sun $^{1}$ , Zhan-Ming Li $^{1,3}$ , Zhi-Qiang Jiao $^{1,3}$ , Tian-Yu Wang $^{1}$ , M.S. Kim $^{6,7}$  and Xian-Min Jin $^{1,2,3*}$

Quantum walks are powerful kernels in quantum computing protocols, and possess strong capabilities in speeding up various simulation and optimization tasks. One striking example is provided by quantum walkers evolving on glued trees<sup>1</sup>, which demonstrate faster hitting performances than classical random walks. However, their experimental implementation is challenging, as this involves highly complex arrangements of an exponentially increasing number of nodes. Here, we propose an alternative structure with a polynomially increasing number of nodes. We successfully map such graphs on quantum photonic chips using femtosecond-laser direct writing techniques in a geometrically scalable fashion. We experimentally demonstrate quantum fast hitting by implementing two-dimensional quantum walks on graphs with up to 160 nodes and a depth of eight layers, achieving a linear relationship between the optimal hitting time and the network depth. Our results open up a scalable path towards quantum speed-up in classically intractable complex problems.

Adapting well-known classical mathematical models in a way to include quantum-mechanical laws has led to the emergence of new interesting behaviours. In some cases, the modified protocols have revealed an advantage with respect to the original protocols in solving specific problems. This has triggered the interest of the scientific community in the quest for a better understanding and exploitation of these new tools<sup>2</sup>. A striking example is provided by quantum walks—the adaptation of the classical random walk to the world of quantum mechanics<sup>3</sup>. Quantum walks have already found applications in several scenarios, including spatial search problems<sup>4,5</sup>, the element distinctness problem<sup>6</sup>, testing matrix identities<sup>7</sup>, evaluating Boolean formulae<sup>8</sup> and judging graph isomorphism<sup>9,10</sup>, which all theoretically promise quantum speed-up and may inspire breakthrough into real-life applications.

One feature of quantum walks on complex graphs that is key in quantum algorithms is their ability to propagate from one node to another distant one in an efficient way. This is often termed 'fast hitting'. Fast hitting on a structure known as a glued tree is particularly attractive because of its clear speed-up in performance compared with classical random walks (that is, a particle following the laws of classical mechanics)[1,11]. A glued tree is obtained by connecting the 'final leaves' of two binary tree graphs[12] of the same depth, as shown in Fig. 1a. The process assumes a particle starting in the left-most vertex (called the Entry site), evolving through the graph, and finally hitting the right-most vertex (called the Exit site). It has been

shown previously that with a normal glued tree the classical random walk may provide some fast algorithms, but in the scenario where the end of each branch in one tree is randomly connected to two branches of the other tree any algorithm exploiting a classical walker would require, on average, a time scaling exponentially with the graph depth to reach the Exit. However, a quantum walker will always require a time that scales only linearly<sup>1,13,14</sup>. Due to the close relation between binary trees and decision trees in computer science, this could generate enormous benefits if properly incorporated into real optimization problems.

Unfortunately, the implementation of quantum walks on this class of graphs is not feasible with current technology. The fact that the number of vertices grows exponentially with the size of the graph is one of the main hurdles for their realization. However, showing the speed-up by a quantum walker over a classical walker on a more simple graph (where, for instance, the number of vertices grows quadratically) is already of great interest: this would be a pioneering experimental demonstration of the quantum advantage in algorithms based on quantum walks on tree structures. So far, one-dimensional quantum walks have been successfully realized in various physical systems[15-23], and two-dimensional quantum walks have been demonstrated with time-polarization degrees of freedom[24,25] or genuine spatial two-dimensional structures[26]. However, an experimental demonstration of the hitting time advantage given by quantum walks on complex structures has never been shown.

Here we present a modified version of the glued tree structure that can be mapped into a photonic chip, with excellent extendibility for larger complexity. We study the hitting efficiency against evolution time when increasing the network layer depth (representing network complexity) from two to eight layers. We demonstrate that the time for optimal hitting increases linearly with the layer depth, giving a quadratic speed-up over the hitting performance by classical random walks.

As is shown in Fig. 1a,b, the hexagonal structure proposed here resembles the glued binary tree, as they are both obtained by gluing two tree-like structures. In our mapping into a three-dimensional waveguide scheme (Fig. 1c), the cross-section of the three-dimensional array corresponds to the desired graph, with each waveguide representing a node, while the longitudinal propagation direction corresponds to the evolution time.

When photons are injected into the Entry site, they propagate along this waveguide and meanwhile evanescently couple to other waveguides[26,27]. As the coupling coefficient decays exponentially

![](images/00634f8d7b0cd11edd1e482bf1e3f86ea50bbbccebdde3e23d2bce8f963013d4.jpg)  
Fig. 1 | Theoretical graphs and their implementation on photonic chips. a, Schematic diagram of a glued binary tree. b, Schematic diagram of the proposed hexagonal graph. c, Schematic diagram of the quantum fast hitting experiment on hexagonal graphs based on femtosecond laser-written waveguide arrays.

when the waveguide spacing increases $^{28}$ , only coupling between the most adjacent waveguides is considered here, representing a connected path in the graph (for example, Site A-B in Fig. 1a and Site D-E in Fig. 1b). Waveguides further apart can be considered disconnected due to the marginal coupling coefficient (for example, Site A-C and Site D-F). In the hexagonal structure, the layer depth corresponds to the number of hexagons in the central column, as shown in Fig. 1b. When the layer depth increases, having an exponentially increasing number of waveguides disconnected in the photonic chips for the glued binary trees is clearly not feasible. Here, we use the hexagonal structure that grows in a regular way and is possible to map on a photonic chip.

For a quantum walk evolving along the waveguides, the propagation length  $z$  is proportional to the propagation time  $t$  according to  $z = \nu t$ , where  $\nu$  is the speed of light in the waveguide. In this Letter, all the terms that are a function of  $t$  will therefore use  $z$ , for simplicity. The initial wavefunction  $|\Psi (0)\rangle$  evolves according to

$$
| \Psi (z) \rangle = e ^ {- i H z} | \Psi (0) \rangle \tag {1}
$$

where  $H$  is the Hamiltonian that contains the information on the couplings within the photonic network. The evolved wavefunction can be obtained by matrix exponential methods when  $H$  is

known $^{26,29}$ . For classical random walks, we use the versatile quantum stochastic walk model $^{30}$  and set it to the purely classical domain without the quantum term. We obtain continuous-time dynamics for classical random walks that can be compared to our continuous-time quantum walks. More theoretical details are provided in Supplementary Note 1.

It is worth noting that quantum walks intrinsically yield nonstationary solutions<sup>31</sup>, which means that there is an optimal hitting scenario at a certain evolution length. We take note of the optimal hitting efficiency and its corresponding optimal evolution length  $z_{\mathrm{o}}$ .

Given the theoretical predictions, we used femtosecond-laser direct writing techniques[28,32-34] to fabricate seven sets of hexagonal graphs with layer depth varying from two to eight. For each layer depth  $i$ , we prepared nine samples with evolution length varying from  $z_{oi} - 4\mathrm{mm}$  to  $z_{oi} + 4\mathrm{mm}$ , with intervals of  $1\mathrm{mm}$ , where  $z_{oi}$  is the calculated optimal length for this structure. We characterized all samples and identified  $z_{oi}$  for each set of graphs by injecting a vertically polarized  $780\mathrm{nm}$  laser beam into the Entry site and capturing the evolution pattern with a charge-coupled device (CCD) camera (Supplementary Notes 2 and 3 and Supplementary Figs. 1-8). With heralded single photons, we then directly observed the evolution pattern of the characterized  $z_{oi}$  (see Methods for details of single-photon generation and measurement).

![](images/b4f40aaf644cd678b453489f3c6e9829461075f39af71df4804b00583ebef5d6.jpg)

![](images/094a77f46b745b08445cf48786471cb3afd2d36ead92ebeba6bb1f021edc49ad.jpg)  
Fig. 2 | Fast hitting on a two-layered hexagonal graph. a-e, Photographed evolution patterns for a two-layered hexagonal graph at different evolution lengths: 20.7 mm (a); 22.7 mm (b); 24.7 mm (c); 26.7 mm (d); 28.7 mm (e). f, Hitting efficiency versus evolution length for quantum hitting and classical hitting. g,h, Evolution patterns for the same sample with an evolution length of 25.2 mm, by injecting a laser beam (g) and heralded single photons (h).

![](images/e6c3dc9758411d456294f02745bd5421ca6a28d550e442e297fdfefd899691ad.jpg)

![](images/27f298b006cc48743b992b4270468b919f47400a76730f49b719c27c3a2a8d4a.jpg)

![](images/6cba5d67c495810d38ed5d7abaef6d71ba996f7d9e088c23b0de35b5397399b1.jpg)

![](images/7c95eb5f1db3265ebfc87f68b371517e3af47bf1c1c8e6b2528ba61324b8f3e1.jpg)

![](images/4be6da87e3f17c7338380d19ef2ad1c80c5939d1a16dc8d3861e438c905a3b90.jpg)

![](images/b29e68812c9ced2c80e349418d3e9be5cf11c784eaf0ecafcf9b250278967333.jpg)  
Fig. 3 | Increasing the complexity of hexagonal graphs. a-f, Photographed evolution patterns for hexagonal graphs of different layer depths from three to eight. Each panel shows the optimal hitting scenario among the nine samples of the same layer depth. The single-photon-level imaged evolution patterns are for the three-layered graph at an evolution length of  $30.4\mathrm{mm}$  (a), the four-layered graph at  $43.7\mathrm{mm}$  (b), the five-layered graph at  $48.4\mathrm{mm}$  (c), the six-layered graph at  $61.8\mathrm{mm}$  (d), the seven-layered graph at  $70.8\mathrm{mm}$  (e) and the eight-layered graph at  $85.8\mathrm{mm}$  (f). The experimental dynamics of hitting efficiency versus evolution time agrees well with our simulation.

![](images/37bc0640eafefd66db9b770ccfbd1fea1a2aeb118990fe0fb9cf3ba88e531511.jpg)

In the photographed patterns of two-layered hexagonal graphs in Fig. 2a–e, the brightest spot at the Exit site occurs in Fig. 2c, which corresponds to the optimal hitting efficiency among these figures.

In Fig. 2f, the hitting efficiency against  $z$  obtained from the experiments agrees very well with the theoretical results in terms of both the value of optimal hitting efficiency ( $\sim 90\%$ ) and the evolution

![](images/0f5c4d9e42a8b769874a56233f188124457b5cb9e3fa3e5f12df351d3b92cd93.jpg)  
Fig. 4 | Comparison between quantum hitting and classical hitting. a,b, Optimal hitting efficiency (a) and the evolution length at which the optimal hitting occurs (b) for hexagonal graphs of different layer depths. Error bars for the experimental optimal distance, which may not be visible in the double-logarithmic axes, are  $1\mathrm{mm}$  above and below the measured value because the real optimal length may lie between two samples (which have discrete length values with an interval of  $1\mathrm{mm}$ ). As for classical hitting, the hitting efficiency slowly converges to a stationary value  $P_{\mathrm{a}}$  that is equal to the inverse of the number of nodes in the glued tree, so we consider that classical hitting becomes optimal when the probability of each waveguide has a maximum deviance of no more than  $10^{-4}P_{\mathrm{a}}$  from  $P_{\mathrm{a}}$ . The error bars for classical hitting scenarios correspond to a range of criteria for judging the convergence: the upper bound corresponds to a deviance threshold of  $10^{-5}P_{\mathrm{a}}$  and the lower bound corresponds to  $10^{-3}P_{\mathrm{a}}$ . O(n) and  $\mathsf{O}(n^2)$  represent the limiting behaviour of evolution length as a function of layer depth for quantum hitting and classical hitting, respectively.

![](images/e6c417b2bbd57ae8c72360f45269276923d648d506bcd50d67ad7231b8e42ea5.jpg)

length at which the optimal hitting occurs (at  $\sim 25\mathrm{mm}$ ). To show the advantage provided by quantum walks, a comparison is made by adding into Fig. 2f the theoretical result for classical random walks on the same structure: the classical hitting efficiency of only  $6.25\%$  is outperformed by more than one order of magnitude. The low efficiency for the classical hitting is a result of the diffusive nature of the classical random walk, and the optimal hitting efficiency is in fact the inverse of the total number of sites. On the other hand, the impressive advantage in the quantum case for the hitting task in networks with many binary paths comes from the interference governing the quantum evolution of the walker. We then polished the chip to seek the even higher hitting efficiency suggested by the fitting result. The measured optimal evolution patterns at  $z = 25.2\mathrm{mm}$  with both laser beam and heralded single photons are shown in Fig. 2g,h. Our results confirm that, for one walker, single photons and a laser beam produce very consistent results. Furthermore, implementation with genuine single photons represents a substantial step towards a faithful realization of quantum fast hitting.

Extending the size of the hexagonal structure to a layer depth up to eight, we were able to show the quantum advantage in fast hitting for graphs of higher complexity. Evolution patterns with an optimal hitting efficiency in nine samples for each structure were measured using heralded single photons (Fig. 3a-f). We can see that the Exit site attracts more light than the others, and at least  $50\%$  of the sites have barely any probability, a situation very different from the even distribution in the classical hitting.

We then analysed the performance of quantum and classical hitting on the hexagonal structures as a function of layer depth. The optimal quantum hitting efficiency from both experiments and theory always remains more than one order of magnitude larger than the classical case, as shown in Fig. 4a. In this hexagonal structure, the total number of sites is  $2n^{2} + 4n$ , where  $n$  is the layer depth. The classical optimal hitting efficiency thus scales as  $n^{-2}$ . Figure 4b presents the evolution length at which the optimal hitting efficiency occurs. This shows a clear linear trend for the quantum scenario, while classical hitting requires a quadratically larger evolution length.

# Discussion

In conclusion, we have demonstrated quantum fast hitting on hexagonal structures in photonic chips, and have experimentally observed that the time for optimal quantum hitting increases linearly with layer depth. In comparison, the classical scenario is

characterized by a quadratic relation; our investigation is therefore a demonstration of the speed-up given by the interference that governs the evolution of the quantum walker, a key point in many tasks based on quantum walks. Overall, there is very good agreement between the experimental data and the theoretical predictions, for both the optimal efficiency and its corresponding evolution length. This work was made possible through the precise and versatile techniques of fabricating three-dimensional integrated photonic chips using femtosecond-laser direct writing. Such capability paves the way for a broader and useful exploitation of quantum walks on complex graphs.

In the future, it would be interesting to investigate the role of defects, asymmetry and the photon bunching effect $^{27}$  in quantum fast hitting. The experimental demonstration can also be extended to other interesting structures, such as the Sierpinski gaskets $^{35}$ , to check other possible quantum advantages of fast hitting. Finally, as binary trees are closely related to decision trees in computer science, we may utilize the quantum speed-up to improve the performance in tasks such as optimization, management and information searching.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of data availability and associated accession codes are available at https://doi.org/10.1038/s41566-018-0282-5.

Received: 15 March 2018; Accepted: 26 September 2018; Published online: 29 October 2018

# References

1. Childs, A. M., Farhi, E. & Gutmann, S. An example of the difference between quantum and classical random walks. Quantum Inf. Process. 1, 35-43 (2002).  
2. Mohseni, M. et al. Commercialize quantum technologies in five years. Nature 543, 171-174 (2017).  
3. Childs, A. M. & van Dam, W. Quantum algorithms for algebraic problems. Rev. Mod. Phys. 82, 1-52 (2008).  
4. Szegedy, M. in Proceedings of the 45th Annual IEEE Symposium on Foundations of Computer Science 32-41 (IEEE Computer Society, Washington, 2004).  
5. Childs, A. M. & Goldstone, J. Spatial search by quantum walk. Phys. Rev. A 70, 022314 (2004).  
6. Aaronson, S. & Shi, Y. Quantum lower bounds for the collision and the element distinctness problems. J. ACM 51, 595-605 (2004).

7. Buhrman, H. & Špalek, R. in Proceedings of the Seventeenth Annual ACM-SIAM Symposium on Discrete Algorithm 880-889 (SIAM, Philadelphia, 2006).  
8. Farhi, E., Goldstone, J. & Gutmann, S. A quantum algorithm for the Hamiltonian NAND tree. Theory Comput. 4, 169-190 (2008).  
9. Douglas, B. L. & Wang, J. B. A classical approach to the graph isomorphism problem using quantum walks. J. Phys. A 41, 075303 (2008).  
10. Bruderer, M. & Plenio, M. B. Decoherence enhances performance of quantum walks applied to graph isomorphism testing. Phys. Rev. A 94, 062317 (2016).  
11. Childs, A. M. et al. in Proceedings of the Thirty-fifth Annual ACM Symposium on Theory of Computing 59-68 (ACM, New York, 2003).  
12. Farhi, E. & Gutmann, S. Quantum computation and decision trees. Phys. Rev. A 58, 915-928 (1998).  
13. Douglas, B. L. & Wang, J. B. Efficient quantum circuit implementation of quantum walks. Phys. Rev. A 79, 052335 (2009).  
14. Carneiro, I. et al. Entanglement in coined quantum walks on regular graphs. New J. Phys. 7, 156 (2005).  
15. Schmitz, H. et al. Quantum walk of a trapped ion in phase space. Phys. Rev. Lett. 103, 090504 (2009).  
16. Karski, M. et al. Quantum walk in position space with single optically trapped atoms. Science 325, 174-177 (2009).  
17. Broome, M. et al. Discrete single-photon quantum walks with tunable decoherence. Phys. Rev. Lett. 104, 153602 (2010).  
18. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
19. Cardano, F. et al. Quantum walks and wavepacket dynamics on a lattice with twisted photons. Sci. Adv. 1, e1500087 (2015).  
20. Du, J. et al. Experimental implementation of the quantum random-walk algorithm. Phys. Rev. A 67, 042316 (2003).  
21. Perets, H. B. et al. Realization of quantum walks with negligible decoherence in waveguide lattices. Phys. Rev. Lett. 100, 170506 (2008).  
22. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
23. Preiss, P. M. et al. Strongly correlated quantum walks in optical lattices. Science 347, 1229-1233 (2015).  
24. Schreiber, A. et al. A 2D quantum walk simulation of two-particle dynamics. Science 336, 55-58 (2012).  
25. Jeong, Y. C., Di Franco, C., Lim, H. T., Kim, M. S. & Kim, Y. H. Experimental realization of a delayed-choice quantum walk. Nat. Commun. 4, 2471 (2013).  
26. Tang, H. et al. Experimental two-dimensional quantum walk on a photonic chip. Sci. Adv. 4, eaat3174 (2018).  
27. Gao, J. et al. Non-classical photon correlation in a two-dimensional photonic lattice. Opt. Express 24, 12607-12616 (2016).  
28. Szameit, A., Dreisow, F., Pertsch, T., Nolte, S. & Tunnermann, A. Control of directional evanescent coupling in fs laser written waveguides. Opt. Express 15, 1579-1587 (2007).  
29. Izaac, J. A. & Wang, J. B. pyctqw: a continuous-time quantum walk simulator on distributed memory computers. Comput. Phys. Commun. 186, 81-92 (2015).  
30. Whitfield, J. D., Rodríguez-Rosario, C. A. & Aspuru-Guzik, A. Quantum stochastic walks: a generalization of classical random walks and quantum walks. Phys. Rev. A 81, 022323 (2010).

31. Sánchez-Burillo, E., Duch, J., Gómez-Gardenes, J. & Zueco, D. Quantum navigation and ranking in complex networks. Sci. Rep. 2, 605 (2012).  
32. Crespi, A. et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat. Photon. 7, 545-549 (2013).  
33. Chaboyer, Z., Meany, T., Helt, L. G., Withford, M. J. & Steel, M. J. Tunable quantum interference in a 3D integrated circuit. Sci. Rep. 5, 9601 (2015).  
34. Feng, Z. et al. Invisibility cloak printed on a photonic chip. Sci. Rep. 6, 28527 (2016).  
35. Darázs, Z., Anishchenko, A., Kiss, T., Blumen, A. & Mülken, O. Transport properties of continuous-time quantum walks on sierpinski fractals. Phys. Rev. E 90, 032113 (2014).

# Acknowledgements

The authors thank J. D. Whitfield for a very useful conversation on numerical methods for the quantum stochastic walks, and J.-W. Pan for helpful discussions. This research is supported by the National Key R&D Program of China (2017YFA0303700), the National Natural Science Foundation of China (11690033, 61734005, 11761141014, 11374211), the Science and Technology Commission of Shanghai Municipality (STCSM) (15QA1402200, 16JC1400405, 17JC1400403), Shanghai Municipal Education Commission (SMEC) (16SG09, 2017-01-07-00-02-E00049) and the open fund from the State Key Laboratory of High Performance Computing (HPCL) (no. 201511-01). C.D.F. is funded by the Singapore National Research Foundation (Fellowship NRF-NRFF2016-02). M.S.K. is supported by the Samsung Global Research Outreach (GRO) project, the Korea Institute of Science and Technology (KIST) Institutional Program (2E26680-18-P025), the Engineering and Physical Sciences Research Council (EPSRC) (EP/K034480/1) and the Royal Society. X.-M.J. acknowledges support from the National Young 1000 Talents Plan.

# Author contributions

X.-M.J. and M.S.K. conceived and supervised the project. H.T. and X.-M.J. designed the experiment. C.D.F., M.S.K. and T.-S.H. conducted the theoretical work. H.T., Z.-Y.S., J.G., K.S., Z.-Q.J. and X.-M.J. performed the single-photon experiment. H.T., Z.-M.L. and T.-Y.W. analysed the experimental data. Z.F. and Z.-Y.S. conducted chip fabrication. H.T., C.D.F., M.S.K. and X.-M.J. wrote the paper, with input from all the other authors.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41566-018-0282-5.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to X.-M.J.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2018

# Methods

Fabrication of the hexagonal graph chip. The three-dimensional layout of the hexagonal structure was designed according to the characterized coupling coefficients and programmed by identically inputting the  $(x,y)$  coordinates of each site and the evolution length  $z$  for all sites in each sample. We fed a  $513\mathrm{nm}$  femtosecond laser (upconverted from a pump laser of  $10\mathrm{W}$ ,  $1,026\mathrm{nm}$ , 290 fs pulse duration,  $1\mathrm{MHz}$  repetition rate) into a spatial light modulator (SLM) to shape the laser pulse in the temporal and spatial domains. We then focused the pulse onto a borosilicate substrate with a  $\times 50$  objective lens (numerical aperture of 0.55) at a constant velocity of  $10\mathrm{mm s^{-1}}$ . The waveguide arrays were prepared in a hexagonal structure by mapping into the cross-section of the chip, and the designed evolution length determined the array length. Power and SLM compensation were used to improve uniformity[34].

Heralded single-photon preparation and single-photon-level imaging. A frequency-doubled  $390\mathrm{nm}$  femtosecond laser pump and a 2-mm-thick barium borate crystal were used to generate degenerate  $780\mathrm{nm}$  photon pairs via a type II spontaneous parametric downconversion process in the beam-like scheme<sup>36</sup>. The photons were then filtered by a  $3\mathrm{nm}$  bandpass filter and guided to the photonic chip. We injected the vertically polarized photon into the Entry waveguide in the photonic chip, and the horizontally polarized photon was connected to a single-photon detector that set a trigger for heralding the horizontally polarized photons on an ICCD camera<sup>37</sup> with a time slot of 10 ns. Without the external trigger,

the measured patterns would come from the thermal-state light rather than single photons. The intensified charge-coupled device (ICCD) camera captured each evolution pattern with a certain evolution length, after accumulating in the 'external' mode for  $1 - 1.5\mathrm{h}$ .

Hitting efficiency acquisition. When collecting the data from experiments, we obtained the corresponding ASCII file, which is essentially a matrix of pixels. We created a 'mask' containing the pixel coordinate of the circle centre and the radius in pixels for each waveguide, and summed the light intensity for all the pixels within each circle using Matlab. The normalized proportion of light intensity for each circle represents the probability at the corresponding waveguide. The hitting efficiency is the proportion of light intensity at the Exit site.

# Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

# References

36. Kim, Y. H. Quantum interference with beamlike type-II spontaneous parametric down-conversion. Phys. Rev. A 68, 013804 (2003).  
37. Sun, K. et al. Mapping and measuring large-scale photonic correlation with single-photon imaging. Preprint at https://arxiv.org/abs/1806.09569 (2018).