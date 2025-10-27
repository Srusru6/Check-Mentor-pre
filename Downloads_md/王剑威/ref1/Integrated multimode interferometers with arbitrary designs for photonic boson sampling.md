# Integrated multimode interferometers with arbitrary designs for photonic boson sampling

Andrea Crespi $^{1,2}$ , Roberto Osellame $^{1,2\star}$ , Roberta Ramponi $^{1,2}$ , Daniel J. Brod $^{3}$ , Ernesto F. Galvão $^{3\star}$ , Nicolò Spagnolo $^{4}$ , Chiara Vitelli $^{4,5}$ , Enrico Maiorino $^{4}$ , Paolo Mataloni $^{4}$  and Fabio Sciarrino $^{4\star}$

The evolution of bosons undergoing arbitrary linear unitary transformations quickly becomes hard to predict using classical computers as we increase the number of particles and modes. Photons propagating in a multiport interferometer naturally solve this so-called boson sampling problem, thereby motivating the development of technologies that enable precise control of multiphoton interference in large interferometers[2-4]. Here, we use novel three-dimensional manufacturing techniques to achieve simultaneous control of all the parameters describing an arbitrary interferometer. We implement a small instance of the boson sampling problem by studying three-photon interference in a five-mode integrated interferometer, confirming the quantum-mechanical predictions. Scaled-up versions of this set-up are a promising way to demonstrate the computational advantage of quantum systems over classical computers. The possibility of implementing arbitrary linear-optical interferometers may also find applications in high-precision measurements and quantum communication[5].

Large-scale quantum computers hold the promise of solving otherwise intractable computational problems such as factoring. Despite the experimental efforts made to date, this prospect is still far from feasible in all proposed physical implementations. It is thus very important to establish intermediate experimental milestones for the field. One such example is provided by the recent study by Aaronson and Arkhipov on the computational complexity of simulating the output distribution of bosons propagating in linear-optical interferometers, a task that has become known as boson sampling. It is well known that a linear-optical quantum computer, composed only of passive optical elements (such as beamsplitters and phase shifters), becomes universal for quantum computation if adaptive measurements are possible. It was shown in ref. 1 that such a device, even without adaptive measurements, produces an output that is hard to simulate classically, given reasonable computational complexity assumptions. More precisely, ref. 1 shows that a linear-optical quantum process comprising (i) the input of photons in a Fock state, (ii) unitary evolution implemented only via beamsplitters and phase shifters, and (iii) simultaneous photon-counting measurement of all modes generates a probability distribution of outcomes that cannot be sampled efficiently (even approximately) using a classical computer. This suggests a feasible experiment to demonstrate the computational capabilities of quantum systems, consisting essentially of observing the multiphoton interference of Fock states in a sufficiently large multimode linear-optical interferometer.

At the core of this hardness-of-simulation result is the fact that the probability associated with each experimental outcome is

proportional to the permanent of a matrix associated with the interferometer (see Methods for details), and the permanent is a function that is notoriously hard to compute<sup>10</sup>. In ref. 1 it was estimated that a system of approximately 20 photons in  $m \approx 400$  modes would already pose severe difficulties for its classical simulation. At present, the most promising technology for achieving this regime involves inputting Fock states into multimode integrated photonic chips<sup>2-4,11-13</sup>.

In this Letter we report on the experimental implementation of a small instance of the Aaronson-Arkhipov proposal, using up to three photons interfering in a randomly chosen, five-mode integrated photonic chip. We have made two important choices that provably make the quantum experiment harder to simulate classically: we avoid any structure by choosing a random interferometer, and the interferometer has more modes than the number of input photons. Implementing this arbitrary interferometer also serves as a stringent test of our novel manufacturing techniques. This allowed us to verify that non-interacting bosons evolve according to the permanent of matrices of size up to  $3 \times 3$ .

Any  $m$ -mode linear interferometer can be decomposed into basic linear-optical elements (phase shifters and beamsplitters) using the decomposition given in ref. 14. The general layout of this decomposition is depicted in Fig. 1a for the case where  $m = 5$ . It consists of a network of beamsplitters with different transmissivities  $t_i$  (where  $T_i = t_i^2$  is the transmission probability of the photon), interspersed by phase shifters restricted, without loss of generality, to the  $[0,\pi]$  range, as discussed in Supplementary Section SI. Unfortunately, large interferometers built with these discrete elements tend to suffer from mechanical instabilities. A more promising approach involves integrating these linear-optical elements using optical waveguides in a glass chip[15,16]. In this work, waveguides were fabricated using the femtosecond laser micromachining technique[17,18], which exploits nonlinear absorption of focused femtosecond pulses to induce a permanent and localized refractive index increase in transparent materials. Arbitrary three-dimensional circuits can be directly written by translating the sample along the desired path, keeping the velocity constant with respect to the laser beam. This maskless and single-step technique allows fast and cost-effective prototyping of new devices, enabling the implementation of three-dimensional layouts that are impossible to achieve with conventional lithography[4].

In the integrated optics approach (Fig. 1b) the role of beamsplitters is performed by directional couplers, devices that bring two waveguides close together to redistribute the light propagating in

![](images/66d4fcc283cf6f13a701a367580aa7dc89ec04bc301c297cef1307ae61afd6a6.jpg)

![](images/b379a022a17a420679f03f20864190c1df89a7bf7c172e7b17ce98b471260178.jpg)  
Figure 1 | Layout of multimode interferometers. a, Realization of an arbitrary  $5 \times 5$  mode transformation using a network of beamsplitters with different transmissivities  $t_{i}$ . The blue and red boxes indicate different phase shifters. b, Implementation of the same scheme adopting integrated photonics; one can appreciate the one-to-one correspondence between elements in the two approaches.

them by means of evanescent field coupling $^{13,19}$ . Our main challenge in implementing the integrated layout of Fig. 1b is to independently control each of the 10 transmissivities  $t_i$  and 15 physically relevant  $[0,\pi]$  phase shifts  $\alpha_i$ ,  $\beta_i$  of an arbitrary, five-mode chip. This is because, in a typical optical circuit (Fig. 2a), changes in the

coupler geometry to modulate the transmissivity will change the optical path (and the phase shifts), and vice versa.

The phase shifters are implemented by deforming the S-bent waveguides at the input of each directional coupler in order to stretch the optical path. The profile of the S-bends is deformed by a suitable coordinate transformation (Supplementary Section SII) that stretches the curve in a smooth fashion to avoid adding waveguide losses, and does not modify the overall footprint of the S-bend to avoid affecting the transmissivity of the surrounding couplers. Figure 2b shows both an undeformed S-bend and a deformed S-bend. Several Mach-Zehnder interferometers with increasingly larger S-bend deformations were fabricated to calibrate the introduced phase shift. This allowed us to verify that a phase shift of up to  $\pi$  can be introduced without causing additional losses to the device.

Achieving independent control of the transmission of each directional coupler is even more difficult. Two parameters that change the transmission are the interaction length and the waveguide spacing. Changing either parameter induces, as a side effect, a variation in the optical path that could bring about a significant, and unwanted, phase shift. We overcome this limitation by using our three-dimensional design capability to rotate one arm of the directional coupler out of the main circuit plane, as depicted in Fig. 2c. This rotation is an effective way of modifying the waveguide distance in the coupling region (which changes the transmission between paths) without affecting the path lengths (and phase shifts). We found that rotation by a few degrees already enables us to span the full range of transmission (Fig. 2c).

To choose which chip to fabricate, we sampled a uniformly random  $5 \times 5$  unitary and found its decomposition into directional couplers and phase shifters (see Supplementary Section SI for more details). This chip was manufactured and used in single-, two- and three-photon experiments using the sources and detection apparatus described in Fig. 3. The input-output transmission of the device was  $30\%$ . However, losses do not jeopardize the boson

![](images/13ec57a8e06b30292398cc316dbf06ec3d42d10f9fde652c4b595b544914e66c.jpg)

![](images/5028373e1787e1c94d6c4daf3baa3945e1e86543c3b1dff3a9c7f32228652da2.jpg)

![](images/8ccd7805d315487b8aece94fcd113d5995973b61b2c15f35018dba35e00d349f.jpg)  
Figure 2 | Independent control of the phase shift and transmission at each directional coupler. a, Controlled deformation of the S-bent waveguide at the input of each directional coupler and the coupling geometry allow independent control over the phase shift and transmission. b, The deformation is given by a nonlinear coordinate transformation, which is a function of a deformation coefficient  $d$ . The drawing shows the undeformed S-bend together with a deformed one; the experimental dependence (squares) of the induced phase shift on the deformation parameter  $d$  (Supplementary Information) at  $\lambda = 806\mathrm{nm}$  is provided in the plot, compared to the expected one (solid line). c, Control over the transmission of the directional coupler is performed by modulating the coupling coefficient; this is achieved by changing the waveguide spacing in the coupling region by rotating one arm of the directional coupler out of the main circuit plane. A calibration of the experimental transmission dependence on the rotation angle at  $\lambda = 806\mathrm{nm}$  is provided (squares), compared to the theoretical expectation (solid line).

![](images/11956cda6ebef38acd2c0ab90ec9ee3e0d98da6de3ec4589a7aaee86e71c5af4.jpg)  
Figure 3 | Experimental set-up for characterization of the chip. a, Schematic representation of the interferometer, realized by a laser writing technique in a glass substrate. b, One-photon, two-photon and three-photon states, generated by parametric downconversion, are injected into the interferometer. APD, avalanche photodiode; IF, interferential filter; PC, polarization controller; PBS, polarizing beamsplitter; PDC, parametric downconversion; HWP, half wave plate. Spatial delay lines are used to synchronize the three photons. c, Single-, two- and threefold coincidence detection is performed at the output ports of the chip to reconstruct the probability of obtaining a given output state realization.

sampling experiment because even lossy systems are likely to be classically hard to simulate $^{20}$ . As a first step we characterized our five-mode chip by injecting single photons into each input port  $i$  and measuring the probability  $P_{\mathrm{exp}}^{\mathrm{l}}(i, K)$  of detecting it in output mode  $K$ . The probability distribution obtained experimentally is shown in Fig. 4a, together with the theoretical prediction  $P_{t}^{\mathrm{l}}(i, K)$  of the sampled unitary  $U^{\mathrm{t}}$ . Each output probability corresponds to the absolute value of one matrix element of  $U^{\mathrm{t}}$  squared. To quantify the agreement between theory and experiment we calculated the variation distance, defined as  $d = (1/2)\sum_{k}|p_k - q_k|$  for two generic probability distributions  $p_k$  and  $q_k$ . We obtained  $d_{\mathrm{exp,t}}^{\mathrm{l}} = 0.158 \pm 0.003$  by averaging over the values corresponding to all the different inputs. This small distance provides a first confirmation of the proper functioning of the device.

To obtain a complete characterization of the implemented interferometer we probed the device with pairs of photons. This was done by simultaneously injecting two single photons on all ten combinations of two different input modes  $(i,j)$ . For each input combination we estimated the ten output probabilities of the photons coming out in two distinct modes  $(K,L)$ . In all, this corresponds to doing 100 Hong-Ou-Mandel two-photon interference experiments. The experimental probability distribution  $P_{\mathrm{exp}}^2 (i,j,K,L)$  is reported in Fig. 4b together with the theoretical distribution  $P_{t}^{2}(i,j,K,L)$  expected from the sampled  $U^{\mathrm{t}}$ . Each theoretically predicted probability is obtained by calculating the permanent of a  $2\times 2$  submatrix of  $U^{\mathrm{t}}$ . We observe a good agreement between the experimentally obtained probabilities and those given by the variation distance  $d_{\mathrm{exp,t}}^2 = 0.221\pm 0.013$  (averaged over all the inputs), thus confirming good control over the fabrication parameters of the chip.

We applied an adapted version of the algorithm described in ref. 21, which is insensitive to losses, to obtain a reconstructed

unitary  $U^{\mathrm{r}}$  on the basis of one- and two-photon experimental data (see Methods). The average variation distances between the predictions of our reconstructed  $U^{\mathrm{r}}$  and our experimental data are  $d_{\mathrm{exp,r}}^{1} = 0.065 \pm 0.003$  for single-photon experiments and  $d_{\mathrm{exp,r}}^{2} = 0.103 \pm 0.013$  for two-photon experiments, which indicates a good characterization of the unitary implemented experimentally.

We also probed the behaviour of the chip in the multiphoton regime by injecting three single photons into modes 1, 3 and 5 of our interferometer and measuring the probability ratios of all events in which we find photons exiting the chip in three different modes (the input mode combination was chosen randomly). In Fig. 4c we compare three distributions: the ideal distribution  $P_{\mathrm{t}}^{3}$  obtained from  $U^{\mathrm{t}}$ , the distribution  $P_{\mathrm{r}}^{3}$  arising from our reconstructed  $U^{\mathrm{r}}$ , and the distribution  $P_{\mathrm{r,p}}^{3}$  taking into consideration the partial indistinguishability  $p$  of the sources we used (for more details see Supplementary Section SIII.D). Figure 4d shows good agreement between the distribution  $P_{\mathrm{r,p}}^{3}$  and our experimental results  $P_{\mathrm{exp}}^{3}$ , as quantified by the variation distance between these two distributions,  $d_{\mathrm{exp,rp}}^{3} = 0.105 \pm 0.024$ . As these probabilities are proportional to the permanents of the  $3 \times 3$  submatrices of the corresponding unitary, this is an experimental confirmation of the permanent formula in the three-photon, five-mode regime. We repeated the same experiment with a second input mode combination, and obtained similar results (Supplementary Section SIII.C).

We experimentally confirmed that the permanent formula that governs the quantum-mechanical behaviour of non-interacting bosons holds for up to three photons interfering in a randomly chosen, five-mode interferometer. Scaling up experiments of this type would provide strong evidence of hard-to-simulate quantum behaviour, even in the presence of noise $^{20}$ . This would require developing integrated multiphoton sources $^{22}$  and detectors $^{23}$ , and improving the manufacturing process to minimize losses and increase accuracy in the specification of each optical element.

![](images/aee7bed748e1bc718d58179ae49bbf6b296b08895a0ad444e417dd57c6e25d83.jpg)

![](images/68be04739ee42e2bf558181d223878d2c095b1b6f6dfffce651c5ef38a5700ce.jpg)

![](images/86834d9234d1887d70e70dedac36ad1091a3e905e1d9df843c9fe9f15026de31.jpg)

![](images/7ba89f1ef77cad661b9e8b94430f4cccc9d70f995db82d90d45a87aae6d695fd.jpg)

![](images/2b37fe4f6760382f01eeedf7ffbea8d4e7fa37da3635f550ad2667b81904290d.jpg)

![](images/d7d18fd8a21c977f47665e47394b6dde51628ee96573e7290ed296fa989d557c.jpg)

![](images/dd9abcada1b8e12515cca03e4b7f279331d11abf5eba37403bbb79f92b9a61a9.jpg)  
Figure 4 | Experimental results. a, One-photon probability distribution: theoretical distribution  $(P_{\mathrm{t}}^{1}(i,K))$ , experimental distribution  $(P_{\mathrm{exp}}^{1}(i,K))$  and reconstructed distribution  $(P_{\mathrm{r}}^{1}(i,K))$ . b, Two-photon probability distribution: theoretical distribution  $(P_{\mathrm{t}}^{2}(i,j,K,L))$ , experimental distribution  $(P_{\mathrm{exp}}^{2}(i,j,K,L))$  and reconstructed distribution  $(P_{\mathrm{r}}^{2}(i,j,K,L))$ . c, Expected three-photon probability distribution for an input state (10101): theoretical distribution  $(P_{\mathrm{t}}^{3})$ , reconstructed distribution  $(P_{\mathrm{r}}^{3})$  and reconstructed distribution with partial distinguishability  $(P_{\mathrm{r,p}}^{3})$ . d, Three-photon probability distribution for an input state (10101): experimental distribution  $(P_{\mathrm{exp}}^{3})$  and reconstructed distribution with partial distinguishability  $(P_{\mathrm{r,p}}^{3})$ . Error bars in the experimental data are due to the Poissonian statistics of the measured events, while error bars on the theoretical predictions were obtained from a Monte Carlo simulation.

![](images/fa7b6a8d828f79fffe01bf22eb1dfba7f9babf14cc329418e905146cc4ac2765.jpg)

The capability of implementing arbitrary unitary transformations may find other applications, such as in the discrete Fourier transforms required in the original KLM scheme for linear optical quantum computation $^{8}$ , and basis-changing unitaries used in quantum state and process tomography $^{24}$ .

Other boson sampling experiments have been reported during the reviewing process of this manuscript[25-27].

# Methods

Calculation of boson sampling probabilities. It has long been known that systems of non-interacting bosons evolve according to permanents of matrices $^{28}$ . Suppose we have  $m$  bosonic modes in the initial Fock state,

$$
| G \rangle = | g _ {1} g _ {2} \dots g _ {m} \rangle = a _ {1} ^ {\dagger g _ {1}} a _ {2} ^ {\dagger g _ {2}} \dots a _ {m} ^ {\dagger g _ {m}} | \odot \rangle \tag {1}
$$

where  $g_{i}$  and  $a_{i}^{\dagger}$  denote, respectively, the occupation number and creation operator for mode  $i$ , and  $|\odot \rangle$  denotes the vacuum state. A linear optical evolution can be described by an  $m \times m$  unitary transformation  $U$  on the space of creation operators, which induces a unitary transformation  $U_{\mathrm{F}}$  on the (exponentially larger) Fock space. The probability amplitude associated with input  $|G\rangle$  and output  $|H\rangle = |h_1h_2\dots h_m\rangle$  is given by

$$
\langle H | U _ {\mathrm {F}} | G \rangle = \frac {\operatorname {p e r} \left(U _ {G , H}\right)}{\sqrt {g _ {1} ! . . g _ {m} ! h _ {1} ! . . h _ {m} !}} \tag {2}
$$

where  $U_{G,H}$  is the matrix obtained by repeating  $g_i$  times the  $i$ th column of  $U$ , and  $h_j$  times its  $j$ th row $^{29}$ , and per(A) denotes the permanent of matrix  $A$  (ref. 10), which is defined similarly to the determinant, but without negative signs for odd permutations of matrix elements.

Despite the similarity in the definitions, the permanent and the determinant are surprisingly different in terms of their computational complexity. The

determinant of an  $n \times n$  matrix can be calculated in polynomial time, but the permanent has been proven to be computationally #P-hard $^{10}$ , belonging to a class of intractable problems that includes the more well-known NP-hard problems. Note, however, that non-interacting bosons cannot be used directly to calculate permanents efficiently, as a typical experiment will have an exponentially large number of outcomes, each predicted by a hard-to-estimate, exponentially small probability associated to a permanent by equation (2).

Femtosecond laser waveguide writing. The optical circuit for the five-mode interferometer was fabricated by direct waveguide writing with the second harmonic  $(\lambda = 515~\mathrm{nm})$  of a femtosecond Yb:KYW cavity-dumped laser oscillator. Our technique consists of focusing femtosecond laser pulses (using a microscope objective,  $0.6\mathrm{NA}$ $\times 50$  ) into the volume of a transparent borosilicate glass (EAGLE 2000, Corning). Under suitable irradiation conditions (300 fs pulse duration,  $1\mathrm{MHz}$  repetition rate,  $120\mathrm{nJ}$  energy) this creates a localized refractive index increase that can be exploited to write buried optical waveguides by translating the sample with respect to the laser beam at a uniform tangential velocity of  $20\mathrm{mm}\mathrm{s}^{-1}$  (Aerotech FiberGLIDE 3D air-bearing stages). The average depth of the fabricated devices under the glass surface was  $170~{\mu\mathrm{m}}$  . The footprint of the five-mode integrated circuit was  $42\mathrm{mm}\times 0.7\mathrm{mm}$

Experimental apparatus. Four photons were produced by means of parametric downconversion by pumping a 2-mm-long beta barium borate (BBO) crystal with a  $392.5\mathrm{nm}$  wavelength pump field<sup>30</sup>. The four photons were generated at  $785\mathrm{nm}$ , spectrally filtered by  $3\mathrm{nm}$  interferential filters and coupled into single-mode fibres. One photon acts as the trigger for coincidence detection, while the other three are coupled into the chip after passing through different delay lines. The output modes were detected using multimode fibres and single-photon avalanche photodiodes. Coincidences between different detectors allowed us to reconstruct the probability of obtaining a given output state.

Reconstructing the unitary of the chip. To reconstruct the unitary that best approximates the experimental data, we used an adaptation of the method reported in ref. 21. The method in ref. 21 obtains a unitary that approximates the experimental data, in the form of the full one-photon outcome statistics (16 independent parameters in our five-mode chip) and a sufficient subset of the two-photon statistics (25 additional independent parameters). By choosing different subsets of the two-photon statistics used by the method, we obtained 25 different unitaries, each of which best fits the subset of data used to obtain it. We compared the predictions of these 25 unitaries with the full data, picking the one with the best agreement. This served as a starting point for a numerical search to maximize agreement with the experimental data, resulting in the reconstructed unitary  $U^{\mathrm{T}}$  reported in Supplementary Section SI.

Received 12 December 2012; accepted 10 April 2013; published online 26 May 2013

# References

1. Aaronson, S. & Arkhipov, A. in Proceedings of the 43rd Annual ACM Symposium on Theory of Computing 333-342 (ACM Press, 2011).  
2. Politi, A., Matthews, J. C. F. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
3. Peruzzo, A. et al. Quantum walks of correlated photons. Science 17, 1500-1503 (2010).  
4. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
5. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nature Photon. 3, 687-695 (2009).  
6. Shor, P. W. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM J. Comput. 26, 1484-1509 (1997).  
7. Ladd, T. D. et al. Quantum computers. Nature 264, 45-53 (2010).  
8. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
9. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
10. Valiant, L. G. The complexity of computing the permanent. Theor. Comput. Sci. 8, 189-201 (1979).

11. Matthews, J. C. F., Politi, A., Stefanov, A. & O'Brien, J. L. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nature Photon. 3, 346-350 (2009).  
12. Smith, B. J., Kundys, D., Thomas-Peter, N., Smith, P. G. R. & Walmsley, I. A. Phase-controlled integrated photonic quantum circuits. Opt. Express 17, 13516-13525 (2009).  
13. Crespi, A. et al. Integrated photonics quantum gates for polarization qubits. Nature Commun. 2, 566 (2011).  
14. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
15. Meany, T. et al. Non-classical interference in integrated 3D multiports. Opt. Express 20, 26895-26905 (2012).  
16. Spagnolo, N. et al. Three-photon bosonic coalescence in an integrated titter. Nature Commun. 4, 1606 (2012).  
17. Gattass, R. R. & Mazur, E. Femtosecond laser micromachining in transparent materials. Nature Photon. 2, 219-225 (2008).  
18. Della Valle, G., Osellame, R. & Laporta, P. Micromachining of photonic devices by femtosecond laser pulses. J. Opt. A 11, 013001 (2009).  
19. Szameit, A., Dreisow, F., Pertsch, T., Nolte, S. & Tünnermann, A. Control of directional evanescent coupling in fs laser written waveguides. Opt. Express 15, 1579-1587 (2007).  
20. Rohde, P. P. & Ralph, T. C. Error tolerance of the boson-sampling model for linear optics quantum computing. Phys. Rev. A 85, 022332 (2012).  
21. Laing, A. & O'Brien, J. L. Super-stable tomography of any linear optical device. Preprint at http://lanl.arxiv.org/abs/1208.2868v1 (2012).  
22. Patel, R. B. et al. Two-photon interference of the emission from electrically tunable remote quantum dots. Nature Photon. 4, 632-635 (2010).  
23. Divochiy, A. et al. Superconducting nanowire photon number resolving detector at telecom wavelength. Nature Photon. 2, 302-306 (2008).  
24. Durt, T., Englert, B.-G., Bengtsson, I. & Zyczkowski, K. On mutually unbiased bases. Int. J. Quant. Inf., 8, 535-640 (2010).  
25. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
26. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
27. Tillmann, M. et al. Experimental boson sampling. Nature Photon. http://dx.doi.org/10.1038/nphoton2013.102.  
28. Troyansky, L. & Tishby, N. in Proceedings of Physics and Computation (PhysComp 96) 314-318 (New England Complex Systems Institute, 1996).  
29. Scheel, S. Permanents in linear optical networks. Preprint at http://lanl.arxiv.org/ abs/quant-ph/0406127v1 (2004).  
30. Kwiat, P., Mattle, K., Weinfurter, H. & Zeilinger, A. New high-intensity source of polarization-entangled photon pairs. Phys. Rev. Lett. 75, 4337-4341 (1995).

# Acknowledgements

This work was supported by the ERC-Starting Grant 3D-QUEST (3D-Quantum Integrated Optical Simulation; grant agreement no. 307783): http://www.3dquest.eu. D.B. and E.G. acknowledge support from the Brazilian National Institute for Science and Technology of Quantum Information (INCT-IQ/CNPq). The authors acknowledge support from G. Milani in assessing the data acquisition system.

# Author contributions

A.C., R.O., R.R., D.B., E.G., N.S., C.V., P.M. and F.S. conceived the experimental approach for hard-to-simulate experiments with integrated photonics. A.C., R.O. and R.R. developed the technique for three-dimensional circuits, and fabricated and characterized the integrated devices using classical optics. N.S., C.V., E.M., P.M. and F.S. carried out the quantum experiments. D.B., E.G., N.S., C.V., E.M. and F.S. elaborated the data. All authors discussed the experimental implementation and results, and contributed to writing the paper.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to R.O., E.F.G. and F.S.

# Competing financial interests

The authors declare no competing financial interests.