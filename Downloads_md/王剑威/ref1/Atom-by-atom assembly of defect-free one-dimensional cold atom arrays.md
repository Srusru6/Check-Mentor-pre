# Atom-by-atom assembly of defect-free one-dimensional cold atom arrays

Manuel Endres, $^{1,2*}$  Hannes Bernien, $^{1*}$  Alexander Keesling, $^{1*}$  Harry Levine, $^{1*}$  Eric R. Anschuetz, $^{1}$  Alexandre Krajenbrink, $^{1\ddagger}$  Crystal Senko, $^{1}$  Vladan Vuletic, $^{3}$  Markus Greiner, $^{1}$  Mikhail D. Lukin $^{1}$

$^{1}$ Department of Physics, Harvard University, Cambridge, MA 02138, USA.  $^{2}$ Division of Physics, Mathematics, and Astronomy, California Institute of Technology, Pasadena, CA 91125, USA.  $^{3}$ Department of Physics and Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA.

*These authors contributed equally to this work.

†Corresponding author. Email: mendres@caltech.edu

Present address: CNRS-Laboratoire de Physique Theorique de l'Ecole Normale Superieure, 24 Rue L'Homond, 75231 Paris Cedex, France.

The realization of large-scale fully controllable quantum systems is an exciting frontier in modern physical science. We use atom-by-atom assembly to implement a platform for the deterministic preparation of regular one-dimensional arrays of individually controlled cold atoms. In our approach, a measurement and feedback procedure eliminates the entropy associated with probabilistic trap occupation and results in defect-free arrays of over 50 atoms in less than 400 milliseconds. The technique is based on fast, real-time control of 100 optical tweezers, which we use to arrange atoms in desired geometric patterns and to maintain these configurations by replacing lost atoms with surplus atoms from a reservoir. This bottom-up approach may enable controlled engineering of scalable many-body systems for quantum information processing, quantum simulations, and precision measurements.

The detection and manipulation of individual quantum particles, such as atoms or photons, is now routinely performed in many quantum physics experiments (1, 2); however, retaining the same control in large-scale systems remains an outstanding challenge. For example, major efforts are currently aimed at scaling up ion-trap and superconducting platforms, where high-fidelity quantum computing operations have been demonstrated in registers consisting of several qubits (3, 4). In contrast, ultracold quantum gases composed of neutral atoms offer inherently large system sizes. However, arbitrary single atom control is highly demanding and its realization is further limited by the slow evaporative cooling process necessary to reach quantum degeneracy. Only in recent years has individual particle detection (5, 6) and basic single-spin control (7) been demonstrated in low entropy optical lattice systems.

Here we demonstrate atom-by-atom assembly of large defect-free 1D arrays of cold neutral atoms  $(\mathcal{S},\mathcal{G})$

We use optical microtraps to directly extract individual atoms from a laser-cooled cloud (10-12) and employ recently demonstrated trapping techniques (13-16) and single-atom position control (17-20) to create desired atomic configurations. Central to our approach is the use of single-atom detection and real-time feedback (17, 20) to eliminate the entropy associated with the probabilistic trap loading (10) [currently limited to ninety percent loading probability even with advanced techniques (21-23)]. Related to the fundamental concept of "Maxwell's demon" (8, 9), this method

allows us to rapidly create large defect-free arrays, and when supplemented with appropriate atom-atom interactions (15, 16, 24-30) provides a potential platform for scalable experiments with individually controlled neutral atoms.

The experimental protocol is illustrated in Fig. 1A. An array of 100 tightly focused optical tweezers is loaded from a laser-cooled cloud. The collisional blockade effect ensures that each individual tweezer is either empty or occupied by a single atom (10). A first high-resolution image yields single-atom resolved information about the trap occupation, which we use to identify empty traps and to switch them off. The remaining occupied traps are rearranged into a regular, defect-free array and we detect the final atom configuration with a second high-resolution image.

Our implementation relies on fast, real-time control of the tweezer positions (Fig. 1B), which we achieve by employing an acousto-optic deflector (AOD) that we drive with a multi-tone radio-frequency (RF) signal.

This generates an array of deflected beams, each controlled by its own RF-tone (15, 16). The resulting beam array is then focused into our vacuum chamber and forms an array of optical tweezers, each with a Gaussian waist of  $\approx 900\mathrm{nm}$ , a wavelength of  $809\mathrm{nm}$ , and a trap depth of  $U / k_{B} \approx 0.9\mathrm{mK}$  ( $k_{\mathrm{B}}$ , Boltzmann constant) that is homogeneous across the array within  $2\%$  (31).

The tweezer array is loaded from a laser-cooled cloud of Rubidium-87 atoms in a magneto-optical trap (MOT). After

the loading procedure, we let the MOT cloud disperse and we detect the occupation of the tweezers with fluorescence imaging. Fast, single-shot, single-atom resolved detection with  $20~\mathrm{ms}$  exposure is enabled by a sub-Doppler lasercooling configuration that remains active during the remainder of the sequence (31) (see Fig. 2, A to C). Our fluorescence count statistics show that individual traps are either empty or occupied by a single atom (10, 31), and we find probabilistically filled arrays with an average single atom loading probability of  $p \approx 0.6$  (see Figs. 2A and 3A).

The central part of our scheme involves the rearrangement procedure for assembling defect-free arrays (31) (see Fig. 1A). In the first step, unoccupied traps are switched off by setting the corresponding RF-amplitudes to zero. In a second step, all occupied tweezers are moved to the left until they stack up with the original spacing of  $2.6\mu \mathrm{m}$ . This movement is generated by sweeping the RF-tones to change the deflection angles of the AOD and lasts 3 ms (31). Finally, we detect the resulting atom configuration with a second high-resolution image. These steps implement a reduction of entropy via measurement and feedback. The effect is immediately visible in the images shown in Fig. 2, A and B. The initial filling of our array is probabilistic, whereas the rearranged configurations show highly ordered atom arrays. Our approach also allows us to construct flexible atomic patterns (Fig. 2C).

The rearrangement procedure creates defect-free arrays with high fidelity. This can be quantified by considering the improvement of single atom occupation probabilities (Fig. 3A) and the success probabilities,  $p_N$ , for creating defect-free arrays of length  $N$  (Fig. 3B). The single atom occupation probability in the left-most forty traps increases from  $\approx 0.6$  before rearrangement to 0.988(3) after rearrangement, demonstrating our ability for high-fidelity single-atom preparation. Furthermore, the success probabilities for creating defect-free arrays show an exponential improvement. Prior to rearrangement, the probability of finding a defect-free array of length  $N$  is exponentially suppressed with  $p_N = p^N$  where  $p \approx 0.6$  (blue circles, Fig. 3B). After rearrangement, we find success probabilities as high as  $p_{30} = 0.75(1)$  and  $p_{50} = 0.53(1)$  (red circles, Fig. 3B).

The same exponential improvement is observed by considering the average wait time for producing defect-free arrays, given by  $T / p_N$ , where  $T = 200$  ms is the cycling time of our experiment (see Fig. 3B). For example, we are able to generate defect-free arrays of 50 atoms with an average wait time of less than  $400$  ms (red circles, Fig. 3C).

The success probabilities can be further enhanced through multiple repetitions of the rearrangement protocol. Figure 4 illustrates the procedure in which we target an atomic array of fixed length and create a reservoir from surplus atoms in a separate zone. After the initial arrangement

of atoms into the target and reservoir zones, we periodically take images to identify defects in the target array and pull atoms from the reservoir to fill in these defects. This enhances our initial success probabilities at producing defect-free arrays within one MOT-loading cycle to nearly the ideal limit (Fig. 4C).

Finally, a similar procedure can be used for correcting errors associated with atomic loss. This becomes a significant limitation for large arrays because for a given lifetime of an individual atom in the trap  $\tau$ , the corresponding lifetime of the  $N$  atom array scales as  $\tau / N$ . To counter this loss, we repeatedly detect the array occupation after longer time intervals and replenish lost atoms from the reservoir. This procedure leads to exponentially enhanced lifetimes of our arrays (Fig. 4D).

These results demonstrate the ability to generate and control large, defect-free arrays at a fast repetition rate. The success probabilities are limited by two factors: the initial number of loaded atoms and losses during rearrangement. For example, the average total atom number in our array is  $59 \pm 5$  (31), which results in the cutoff in the success probability in Fig. 3B starting from  $N \approx 50$  (solid line). For shorter arrays, the fidelity is mostly limited by losses during rearrangement. These losses are dominated by our finite vacuum-limited lifetime, which varies from  $\tau \approx 6$  s to  $\tau \approx 12$  s (depending on the setting of our atomic dispenser source), and are only minimally increased by the movement of the atoms (31). The single atom occupation probability is correspondingly reduced by a factor  $\exp(-t_r / \tau)$ , where  $t_r = 50$  ms is the time for the whole rearrangement procedure (31). This results in the success probabilities of creating length- $N$  arrays scaling as  $\exp(-t_r N / \tau)$ , which dominates the slope for  $N = 50$  in Fig. 3B (dashed line). Currently, we reach vacuum limited lifetimes only with sub-Doppler cooling applied throughout the sequence. However, the lifetime without cooling could be improved, for example, by using a different trapping laser and trapping wavelength (31).

The size of the final arrays can be considerably increased by implementing a number of realistic experimental improvements. For example, the initial loading probability could be enhanced to 0.9 (21-23) and the vacuum limited lifetime could be improved to  $\tau \approx 60\mathrm{s}$  in an upgraded vacuum chamber. Increasing the number of traps in the current configuration is difficult because of the AOD bandwidth of  $\approx 50\mathrm{MHz}$  and strong parametric heating introduced when the frequency spacing of neighboring traps approaches  $\approx 450\mathrm{kHz}$  (31). However, implementing two-dimensional (2D) arrays could provide a path toward realizing thousands of traps, ultimately limited by the availability of laser power and the field of view of high-resolution objectives. Such 2D configurations could be realized by either directly using a 2D-AOD or by creating a static 2D lattice of

traps [using spatial light modulators (14) or optical lattices (12)] and sorting atoms with an independent AOD (31). With increased loading efficiencies (21-23), realistic estimates for the rearrangement time  $t_r$  in such 2D arrays indicate that the robust creation of defect-free arrays of hundreds of atoms is feasible (31). Finally, the repetitive interrogation techniques, in combination with periodic reservoir reloading from a cold atom source (such as a MOT), could be used to maintain arrays indefinitely.

Atom-by-atom assembly of defect-free arrays forms a scalable platform with unique possibilities. It combines features that are typically associated with ion trapping experiments, such as single-qubit addressability (32, 33) and fast cycling times, with the flexible optical trapping of neutral atoms in a scalable fashion. Furthermore, in contrast to solid-state platforms, such atomic arrays are highly homogeneous (31) and mostly decoupled from their environment. The homogeneity of our array should also allow for cooling of the atomic motion via simultaneous sideband cooling in all tweezers at once (34, 35).

These features provide an excellent starting point for multi-qubit experiments, studies of quantum many body effects and for exploring future applications. The required interactions between the atoms can be engineered using several approaches. Even without sideband cooling, exciting the atoms into high-lying Rydberg states would introduce strong dipole interactions that can be used for fast entangling gates (24, 25, 27). The parallelism afforded by our flexible atom rearrangement enables efficient diagnostics of such Rydberg-mediated entanglement. These interactions may also enable approaches to quantum simulations that involve both coherent coupling and engineered dissipation (26, 27), as well as large-scale entangled quantum states for applications in precision measurements (36).

An alternative approach to engineering interactions involves the integration of atom arrays with nanophotonic platforms as demonstrated previously (28, 29). These enable photon-mediated interactions that can be employed to couple the atoms within a local multi-qubit register or for efficient communication between the registers using a modular quantum network architecture (3).

Finally, our platform could enable new bottom-up approaches to studying quantum many-body physics in Hubbard models (15, 16, 30), where atomic Mott insulators with fixed atom number and complex spin patterns could be directly assembled. This requires atom temperatures close to the ground state, coherent tunneling between the traps, and sizable on-site interactions. With side-band cooling, ground state fractions in excess of  $90\%$  have already been demonstrated (34, 35), and can likely be improved via additional optical trapping along the longitudinal tweezer axes, which would also increase on-site interaction strengths. Coherent

tunneling of Rb atoms between similarly sized tweezers has been observed before by reducing the tweezer distance (15, 16). The parametric heating, currently limiting the minimal distance between our traps, could be reduced by working with shallower traps, as needed for tunneling, and by employing fewer traps to increase the frequency separation between neighboring traps. Eventually, this approach could be applied to create ultracold quantum matter composed of exotic atomic species or complex molecules (37, 38) that are difficult to cool evaporatively.

# REFERENCES AND NOTES

1. S. Haroche, Controlling photons in a box and exploring the quantum to classical boundary. Ann. Phys. 525, 753-776 (2013). doi:10.1002/andp.201300737  
2. D. J. Wineland, Nobel Lecture: Superposition, entanglement, and raising Schrödinger's cat. Rev. Mod. Phys. 85, 1103-1114 (2013). doi:10.1103/RevModPhys.85.1103  
3. C. Monroe, J. Kim, Scaling the ion trap quantum processor. Science 339, 1164-1169 (2013). Medline doi:10.1126/science.1231298  
4. M. H. Devoret, R. J. Schoelkopf, Superconducting circuits for quantum information: An outlook. Science 339, 1169-1174 (2013). Medline doi:10.1126/science.1231930  
5. W. S. Bakr, A. Peng, M. E. Tai, R. Ma, J. Simon, J. I. Gillen, S. Fölling, L. Pollet, M. Greiner, Probing the superfluid-to-Mott insulator transition at the single-atom level. Science 329, 547–550 (2010). Medline doi:10.1126/science.1192368  
6. J. F. Sherson, C. Weitenberg, M. Endres, M. Cheneau, I. Bloch, S. Kuhr, Single-atom-resolved fluorescence imaging of an atomic Mott insulator. Nature 467, 68-72 (2010). Medline doi:10.1038/nature09378  
7. C. Weitenberg, M. Endres, J. F. Sherson, M. Cheneau, P. Schauss, T. Fukuhara, I. Bloch, S. Kuhr, Single-spin addressing in an atomic Mott insulator. Nature 471, 319-324 (2011). Medline doi:10.1038/nature09827  
8. D. S. Weiss, J. Vala, A. V. Thapliyal, S. Mygren, U. Vazirani, K. B. Whaley, Another way to approach zero entropy for a finite system of atoms. Phys. Rev. A 70, 040302 (2004). doi:10.1103/PhysRevA.70.040302  
9. J. Vala, A. V. Thapliyal, S. Myrgren, U. Vazirani, D. S. Weiss, K. B. Whaley, Perfect pattern formation of neutral atoms in an addressable optical lattice. Phys. Rev. A 71, 032324 (2005). doi:10.1103/PhysRevA.71.032324  
10. N. Schlosser, G. Reymond, I. Protsenko, P. Grangier, Sub-poissonian loading of single atoms in a microscopic dipole trap. Nature 411, 1024-1027 (2001). Medline doi:10.1038/35082512  
11. M. Weber, J. Volz, K. Saucke, C. Kurtsiefer, H. Weinfurter, Analysis of a single-atom dipole trap. Phys. Rev. A 73, 043406 (2006). doi:10.1103/PhysRevA.73.043406  
12. K. D. Nelson, X. Li, D. S. Weiss, Imaging single atoms in a three-dimensional array. Nat. Phys. 3, 556-560 (2007). doi:10.1038/nphys645  
13. M. J. Piotrowicz, M. Lichtman, K. Maller, G. Li, S. Zhang, L. Isenhower, M. Saffman, Two-dimensional lattice of blue-detuned atom traps using a projected Gaussian beam array. Phys. Rev. A 88, 013420 (2013). doi:10.1103/PhysRevA.88.013420  
14. F. Nogrette, H. Labuhn, S. Ravets, D. Barredo, L. Béguin, A. Vernier, T. Lahaye, A. Browaecs, Single-atom trapping in holographic 2D arrays of microtraps with arbitrary geometries. Phys. Rev. X 4, 021034 (2014); http://journals.aps.org/prx/abstract/10.1103/PhysRevX.4.021034.  
15. A. M. Kaufman, B. J. Lester, C. M. Reynolds, M. L. Wall, M. Foss-Feig, K. R. Hazzard, A. M. Rey, C. A. Regal, Two-particle quantum interference in tunnel-coupled optical tweezers. Science 345, 306-309 (2014). Medline doi:10.1126/science.1250057  
16. A. M. Kaufman, B. J. Lester, M. Foss-Feig, M. L. Wall, A. M. Rey, C. A. Regal, Entangling two transportable neutral atoms via local spin exchange. Nature 527, 208-211 (2015). Medline doi:10.1038/nature16073  
17. Y. Miroshnychenko, W. Alt, I. Dotsenko, L. Förster, M. Khudaverdyan, D. Meschede, D. Schrader, A. Rauschenbeutel, Quantum engineering: An atom

sorting machine. Nature 442, 151 (2006). Medline doi:10.1038/442151a  
18. J. Beugnon, C. Tuchendler, H. Marion, A. Gaetan, Y. Miroshnychenko, Y. R. P. Sortais, A. M. Lance, M. P. A. Jones, G. Messin, A. Browaeks, P. Grangier, Two-dimensional transport and transfer of a single atomic qubit in optical tweezers. Nat. Phys. 3, 696-699 (2007). doi:10.1038/nphys698  
19. M. Schlosser, J. Kruse, C. Gierl, S. Teichmann, S. Tichelmann, G. Birkl, Fast transport, atom sample splitting and single-atom qubit supply in two-dimensional arrays of optical microtraps. New J. Phys. 14, 123034 (2012). doi:10.1088/1367-2630/14/12/123034  
20. H. Kim, W. Lee, H.-g. Lee, H. Jo, Y. Song, J. Ahn, In situ single-atom array synthesis using dynamic holographic optical tweezers. arXiv:1601.03833 (2016); https://arxiv.org/pdf/1601.03833.pdf.  
21. T. Grünzweig, A. Hilliard, M. McGovern, M. F. Andersen, Near-deterministic preparation of a single atom in an optical microtrap. Nat. Phys. 6, 951-954 (2010). doi:10.1038/nphys1778  
22. B. J. Lester, N. Luick, A. M. Kaufman, C. M. Reynolds, C. A. Regal, Rapid production of uniformly filled arrays of neutral atoms. Phys. Rev. Lett. 115, 073003 (2015). Medline doi:10.1103/PhysRevLett.115.073003  
23. Y. H. Fung, M. F. Andersen, Efficient collisional blockade loading of a single atom into a tight microtrap. New J. Phys. 17, 073011 (2015). doi:10.1088/1367-2630/17/7/073011  
24. D. Jaksch, J. I. Cirac, P. Zoller, S. L. Rolston, R. Cote, M. D. Lukin, Fast quantum gates for neutral atoms. Phys. Rev. Lett. 85, 2208-2211 (2000). Medline doi:10.1103/PhysRevLett.85.2208  
25. M. Saffman, T. G. Walker, K. Mølmer, Quantum information with Rydberg atoms. Rev. Mod. Phys. 82, 2313-2363 (2010). doi:10.1103/RevModPhys.82.2313  
26. H. Weimer, M. Müller, I. Lesanovsky, P. Zoller, H. P. Buchler, A Rydberg quantum simulator. Nat. Phys. 6, 382-388 (2010). doi:10.1038/nphys1614  
27. A. Browaeks, D. Barredo, T. Lahaye, Experimental investigations of dipole-dipole interactions between a few Rydberg atoms. J. Phys. B 49, 152001 (2016). doi:10.1088/0953-4075/49/15/152001  
28. J. D. Thompson, T. G. Tiecke, N. P. de Leon, J. Feist, A. V. Akimov, M. Gullans, A. S. Zibrov, V. Vuletic, M. D. Lukin, Coupling a single trapped atom to a nanoscale optical cavity. Science 340, 1202-1205 (2013). Medline doi:10.1126/science.1237125  
29. A. Goban, C. L. Hung, S. P. Yu, J. D. Hood, J. A. Muniz, J. H. Lee, M. J. Martin, A. C. McClung, K. S. Choi, D. E. Chang, O. Painter, H. J. Kimble, Atom-light interactions in photonic crystals. Nat. Commun. 5, 3808 (2014). Medline doi:10.1038/ncomms4808  
30. S. Murmann, F. Deuretzbacher, G. Zurn, J. Bjerlin, S. M. Reimann, L. Santos, T. Lompe, S. Jochim, Antiferromagnetic Heisenberg spin chain of a few cold atoms in a one-dimensional trap. Phys. Rev. Lett. 115, 215301 (2015). Medline doi:10.1103/PhysRevLett.115.215301  
31. See supplementary materials on Science Online.  
32. T. Xia, M. Lichtman, K. Maller, A. W. Carr, M. J. Piotrowicz, L. Isenhower, M. Saffman, Randomized benchmarking of single-qubit gates in a 2D array of neutral-atom qubits. Phys. Rev. Lett. 114, 100503 (2015). Medline doi:10.1103/PhysRevLett.114.100503  
33. Y. Wang, X. Zhang, T. A. Corcovilos, A. Kumar, D. S. Weiss, Coherent addressing of individual neutral atoms in a 3D optical lattice. Phys. Rev. Lett. 115, 043003 (2015). Medline doi:10.1103/PhysRevLett.115.043003  
34. A. M. Kaufman, B. J. Lester, C. A. Regal, Cooling a single atom in an optical tweezer to its quantum ground state. Phys. Rev. X 2, 041014 (2012); http://journalsaps.org/prx/abstract/10.1103/PhysRevX.2.041014.  
35. J. D. Thompson, T. G. Tiecke, A. S. Zibrov, V. Vuletic, M. D. Lukin, Coherence and Raman sideband cooling of a single atom in an optical tweezer. Phys. Rev. Lett. 110, 133001 (2013). Medline doi:10.1103/PhysRevLett.110.133001  
36. P. Kómar, T. Topcu, E. M. Kessler, A. Derevianko, V. Vuletic, J. Ye, M. D. Lukin, Quantum network of atom clocks: A possible implementation with neutral atoms. Phys. Rev. Lett. 117, 060506 (2016). Medline doi:10.1103/PhysRevLett.117.060506  
37. J. F. Barry, D. J. McCarron, E. B. Norrgard, M. H. Steinecker, D. DeMille, Magnetooptical trapping of a diatomic molecule. Nature 512, 286-289 (2014). Medline doi:10.1038/nature13634  
38. N. R. Hutzler, L. R. Liu, Y. Yu, K.-K. Ni, Eliminating light shifts in single-atom

optical traps. arXiv:1605.09422 (2016); https://arxiv.org/abs/1605.09422.  
39. D. Barredo, S. de Leseleuc, V. Lienhard, T. Lahaye, A. Browaeys, An atom-byatom assembler of defect-free arbitrary 2d atomic arrays. arXiv: 1607.03042; https://arxiv.org/abs/1607.03042  
40. C. Klempt, T. van Zoest, T. Henninger, O. Topic, E. Rasel, W. Ertmer, J. Arlt, Ultraviolet light-induced atom desorption for large rubidium and potassium magneto-optical traps. Phys. Rev. A 73, 013410 (2006). doi:10.1103/PhysRevA.73.013410  
41. Y. R. P. Sortais, H. Marion, C. Tuchendler, A. M. Lance, M. Lamare, P. Fournet, C. Armellin, R. Mercier, G. Messin, A. Browaeys, P. Grangier, Diffraction-limited optics for single-atom manipulation. Phys. Rev. A 75, 013406 (2007). doi:10.1103/PhysRevA.75.013406

# ACKNOWLEDGMENTS

We thank K.-K. Ni, N. Hutzler, A. Mazurenko, and A. Kaufman for insightful discussion. This work was supported by NSF, CUA, NSSEFF, and Harvard Quantum Optics Center. H.B. acknowledges support by a Rubicon Grant of the Netherlands Organization for Scientific Research (NWO). During the completion of this work, we became aware of a related approach (39).

# SUPPLEMENTARY MATERIALS

www.sciencemag.org/cgi/content/full/science.ah3752/DC1

Materials and Methods

Figs. S1 to S5

Movies S1 to S3

References (40, 41)

17 June 2016; accepted 17 October 2016

Published online 3 November 2016

10.1126/science.aah3752

![](images/480c8680a8b14302126f5df8871df875b0b930155ae60138d304bf746682dc6b.jpg)

![](images/588a92f6fcfdb144becec73aa0f4e10a45122cf359cac0b3c8b454422aaf4088.jpg)  
Fig. 1. Protocol for creating defect-free arrays. (A) A first image identifies optical microtraps loaded with a single atom, and empty traps are turned off. The loaded traps are moved to fill in the empty sites and a second image verifies the success of the operation. (B) The trap array is produced by an acousto-optic deflector (AOD) and imaged with a 1:1 telescope onto a 0.5 NA microscope objective, which creates an array of tightly focused optical tweezers in a vacuum chamber. An identical microscope objective is aligned to image the same focal plane. A dichroic mirror allows us to view the trap light on a charge-coupled-device camera (CCD) while simultaneously detecting the atoms via fluorescence imaging on an electron-multiplied-CCD camera (EMCCD). The rearrangement protocol is realized through fast feedback onto the multi-tone radio-frequency (RF) field driving the AOD.

![](images/748b18c444356df48370f7d5156f37661c6c5ef5efa06d5f78fe598e73f36fc9.jpg)  
Fig. 2. Assembly of regular atom arrays. (A) Single-shot, single-atom resolved fluorescence images recorded with the EMCCD before (top) and after (bottom) rearrangement. Defects are identified and the loaded traps are rearranged according to the protocol in Fig. 1, indicated by arrows for a few selected atoms. (B) Two instances of successfully rearranged arrays (first two pictures), and one instance (last picture) where a defect is visible after rearrangement. (C) The final arrangement of atoms is flexible, and we generate, e.g., clusters of two (top) or ten (bottom) atoms. Non-periodic arrangements and adjustable lattice spacings are also possible. (D) High-resolution CCD image of trap array. Our default configuration for loading atoms consists of an array of 100 tweezers with a spacing of  $0.49\mathrm{MHz}$  between the RF-tones, corresponding to a real-space distance of  $2.6\mu \mathrm{m}$  between the focused beams (31).

![](images/ad4451b722c800d8e5724f62fae0442fa8ba70fcd5478d4f0d9a233e5bb0c514.jpg)  
A

![](images/dac99fa3b44c43bdbaceecdeb0d3747a39a42e14d54469f0df5544da155af605.jpg)  
B

![](images/468d94f43cf2d5ead341f5c4f171c8f6353eb3cd32600a3fea08b9219a02ba4a.jpg)  
C  
Fig. 3. Quantifying the rearrangement performance. (A) The initial loading (blue circles) results in an occupation probability of  $\approx 0.6$  for each trap in the array. After rearrangement (red circles), close to unity filling is reached on the left side of the array. (B) In the initial image, the probability of finding a defect-free length- $N$  array (starting from the leftmost trap) falls off exponentially with  $N$  (blue circles). Following the rearrangement of all loaded traps to form the largest possible array, we demonstrate strongly enhanced success probabilities at producing defect-free arrays (red circles). Theory curves show limits set by the total initial atom number (solid line), the background limited lifetime of  $\tau = 6.2$  s (dashed line) and the product of both (dashed dotted line) (31). (C) Expected amount of time to wait on average to produce a defect-free array of a given size taking into account the experimental cycle time of 200 ms (150 ms without rearrangement). Without rearrangement, the wait time grows exponentially (blue circles). Employing the rearrangement procedure, we can produce arrays of length 50 in less than 400 ms (red circles). All error bars denote  $68\%$  confidence intervals, which are smaller than the marker size in (A) and (B).

![](images/a47cb6d64688603ce8c8dc55b2f8fe24f36ab5c3768b29b97c03a982bd22bb52.jpg)

![](images/2220dfef16177015955ffa96f55df3f2be377f3fbc78b23dfff51b7efa9ef56f.jpg)  
Fig. 4. Creating and maintaining regular arrays using an atomic reservoir. (A) For a given target array size, surplus atoms are kept in a reservoir and used for repetitive reloading of the array. (B) A 20 atom target array with a reservoir of atoms on the right. Defects occasionally develop in the target array and are replaced by atoms in the reservoir. The reservoir depletes as it is used to fill in defects. (C) By performing repeated rearrangements (once every  $50~\mathrm{ms}$ ) the probability to successfully produce a defect-free array in any of these attempts increases and approaches the limit set by the number of initially loaded atoms (dashed lines). We show data for targeting 40 (purple), 50 (yellow), and 60 (green) atom arrays. Solid lines are guides to the eye. (D) Probing for defects and filling them once every  $100~\mathrm{ms}$  from the reservoir extends the lifetime of a defect-free array. Shown is the success probability of maintaining arrays of 20 (circles) and 40 (triangles) atoms with (red) and without (blue) replenishing atoms from the reservoir. With replenishing, the probability to maintain a defect-free array remains at a fixed plateau for as long as we have surplus atoms in the reservoir. The initial plateau value is set by the probability that no atoms in the array are lost in  $100~\mathrm{ms}$  (calculated value for  $10~\mathrm{s}$  single atom lifetime shown as the dotted line). All error bars denote  $68\%$  confidence intervals, which are smaller than the marker size in (C).

![](images/a57e822bcc2bd4344919ac278d0b4d38cc6f22e1e29579c9140cde93e245de78.jpg)

![](images/f65966454de244562f2f47c6319009bb52069fbd8f63ae1e7b1094cdca9565c3.jpg)

EXTENDED PDF FORMAT

SPONSORED BY

![](images/f6d09b04680536274ec88e232f37f671f9ad9d82a724824dbe7ce96df564d1a4.jpg)

www.rndsystems.com

# Science

AAAS

Editor's Summary

# Atom-by-atom assembly of defect-free one-dimensional cold atom arrays

Manuel Endres, Hannes Bernien, Alexander Keesling, Harry Levine, Eric R. Anschuetz, Alexandre Krajenbrink, Crystal Senko, Vladan Vuletic, Markus Greiner and Mikhail D. Lukin (November 3, 2016) published online November 3, 2016

This copy is for your personal, non-commercial use only.

Article Tools Visit the online version of this article to access the personalization and article tools: http://science.sciencemag.org/content/early/2016/11/02/science.ah3752

Permissions Obtain information about reproducing this article: http://www.sciencemag.org/about/permissions.dtl

Science (print ISSN 0036-8075; online ISSN 1095-9203) is published weekly, except the last week in December, by the American Association for the Advancement of Science, 1200 New York Avenue NW, Washington, DC 20005. Copyright 2016 by the American Association for the Advancement of Science; all rights reserved. The title Science is a registered trademark of AAAS.