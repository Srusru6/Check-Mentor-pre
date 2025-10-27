ARTICLE

Received 26 Oct 2012 | Accepted 20 Feb 2013 | Published 19 Mar 2013

DOI: 10.1038/ncomms2616

OPEN

# Three-photon bosonic coalescence in an integrated tritter

Nicolò Spagnolo<sup>1</sup>, Chiara Vitelli<sup>1,2</sup>, Lorenzo Aparo<sup>1</sup>, Paolo Mataloni<sup>1</sup>, Fabio Sciarrino<sup>1</sup>, Andrea Crespi<sup>3,4</sup>, Roberta Ramponi<sup>3,4</sup> & Roberto Osellame<sup>3,4</sup>

The main features of quantum mechanics reside in interference deriving from the superposition of different quantum states. While current quantum optical technology enables two-photon interference both in bulk and integrated systems, simultaneous interference of more than two particles, leading to richer quantum phenomena, is still a challenging task. Here we report the experimental observation of three-photon interference in an integrated three-port directional coupler realized by ultrafast laser writing. By exploiting the capability of this technique to produce three-dimensional structures, we realized and tested in the quantum regime a three-port beam splitter, namely a tritter, which allowed us to observe bosonic coalescence of three photons. These results open new important perspectives in many areas of quantum information, such as fundamental tests of quantum mechanics with increasing number of photons, quantum state engineering, quantum sensing and quantum simulation.

The Hong-Ou-Mandel effect is a purely quantum phenomenon deriving from the interference of two photons<sup>1</sup>. It is a consequence of the bosonic nature of light and it can be observed when two identical photons impinge simultaneously on a two-port balanced beam splitter and, as a result, they are forced to exit from the same port. This effect can be exploited to quantify the amount of indistinguishability of correlated photons<sup>2,3</sup> or to project a quantum state onto the maximally entangled singlet Bell state, representing an important resource in many research areas of quantum information, from quantum computation to quantum metrology<sup>4-6</sup>. The interaction of single-photon states on a beam splitter and successive post selection may indeed lead to the generation of entangled states such as N00N and GHZ states<sup>8</sup>. As a matter of fact, achieving interference of more than two particles on a beam splitter is a challenging task<sup>9</sup>. However, it could open the door to the observation of quantum phenomena in increasing size systems and to the engineering of quantum states for quantum information processing<sup>10,11</sup>.

The adoption of a multiport beam splitter has been proposed to perform additional classes of possible EPR-Bell experiments in a Hilbert space with dimension higher than two $^{12}$ . Furthermore the capability of implementing multipath interferometers by multiport beam splitters could be adopted to perform quantum computation tasks $^{13}$ . Recently a generalized  $N$ -port beam splitter has been theoretically addressed in refs 14,15, and the behaviour of  $N$  photons impinging onto the  $N$ -port beam splitter has been studied by using a statistical approach, as the complexity of this problem grows faster than exponentially with growing  $N$ . Very recently, the application to quantum interferometry of three- and four-port beam splitters have been theoretically investigated, and a quantum enhancement in terms of sensitivity has been predicted $^{16}$ . However, three-particle interferometry is mostly unexplored territory, both experimentally and theoretically. The three-beam extension of a beam splitter, the so called 'tritter', was first addressed in ref. 12, and its proposed implementation consisted of the combination of two-port beam splitters and phase shifters (see Fig. 1a) (refs 12,17). Three-dimensional implementations of three- and four-port beam splitters, based on fused optical fibres $^{18}$  or femtosecond laser waveguide

writing $^{19-21}$ , have been proposed. However, only classical light or two-photon interference experiments were carried out on such devices. Therefore, an experimental investigation of quantum interference of more than two photons is still lacking.

Here we report the first experimental investigation of three-photon interference in a tritter. The tritter is realized by femtosecond laser waveguide writing and it consists of three waveguides approaching three-dimensionally, thus enabling simultaneous interaction of the three photons without having to decompose the process into cascaded two-mode interactions and phase shifters (Fig. 1b). The three photons, each coupled to a different waveguide, mutually interfere in the three-arm directional coupler by evanescent field interaction. The behaviour of a three-photon state entering the tritter is investigated by comparing the output state probabilities with the expected classical ones, evidencing the purely quantum effects involved in bosonic coalescence.

# Results

Theoretical description of the tritter output probabilities. Let us first address the action of a tritter on a generic input state  $|\psi \rangle$ . It can be expressed by a unitary matrix  $\mathcal{U}$ , mapping the input field operators  $a_{i}^{\dagger}$  to the output field operators  $b_{i}^{\dagger}$  with  $b_{i}^{\dagger} = \sum_{j} \mathcal{U}_{ij} a_{j}^{\dagger}$ , (refs 12,15,17; see Supplementary Note 1). In the case of an ideally symmetric tritter, where a photon entering in one input port has the same probability of exiting through anyone of the output ports, the unitary matrix  $\mathcal{U}$  reads:

$$
\mathcal {U} ^ {t} = \frac {1}{\sqrt {3}} \left( \begin{array}{c c c} 1 & 1 & 1 \\ 1 & e ^ {i 2 \pi / 3} & e ^ {i 4 \pi / 3} \\ 1 & e ^ {i 4 \pi / 3} & e ^ {i 8 \pi / 3} \end{array} \right). \tag {1}
$$

Let us consider what happens when an ideal titter is injected by a three-photon state  $|1,1,1\rangle$ . The corresponding output state after the evolution induced by  $\mathcal{U}^t$  reads:

$$
\left| 1, 1, 1 \right\rangle \xrightarrow {\mathcal {U} ^ {t}} c _ {1, 1, 1} \left| 1, 1, 1 \right\rangle + c _ {\{3, 0, 0 \}} \left| \{3, 0, 0 \} \right\rangle . \tag {2}
$$

![](images/a4fcfefa5aa4458ade33ede15be635a802e6020e572314fe69066509a129adf5.jpg)  
a

![](images/8dcc3043b60c984d38e25147f19c473064f5541c50a4e08b24d23a08d4358279.jpg)  
c

![](images/0cdb2ce62bd45244c87bc8feb95fb1177a17ce87e9ae246d5bee8667cf6d23d7.jpg)

![](images/628872ac58573046de529111da356776168b9134e974f713ef6838587b3085d6.jpg)

![](images/70968868e90511a88f2875153b224e1f9fccbe99c9f4e8547830991c6641fa68.jpg)

![](images/dd9cbac4455312ecb81729dda5260cac21d6272d7b1b74392d6f471e3bb45664.jpg)  
b  
Figure 1 | Schematic representation of a tritter and related bosonic coalescence. (a) Optical scheme for a three-mode splitter obtained by a set of conventional beam splitters (grey cubes) and phase shifters (green plates) $^{12,17}$ , where  $\mathbf{k}_i$  with  $i = 1,2,3$  represent input-output spatial modes. (b) Integrated three-dimensional scheme for a laser-written tritter. (c) Three-photon bosonic coalescence effect in a tritter when each photon is injected into a different input spatial mode: all the terms with two photons exiting on the same output port vanish due to bosonic coalescence.

![](images/8d45544741447c1407d365cb9320f9d5e2529f13abe28a4603d047237c7ab96d.jpg)

![](images/b033f05fb05924916a410ed04dba09728a1807e179dce0f1f20ddf28e60961f0.jpg)

![](images/09650eda7bb1c9d51cd45661db3a57d2bc980b04d4643eaf305972b289129dc6.jpg)

![](images/c850c8457709696c1ea013369efc478a10fdf4a93474b53117179484a5b98af5.jpg)  
Figure 2 | Hong-Ou-Mandel effect for a  $|1,1,1\rangle$  input state in an ideal tritter. Theoretical output probabilities  $P_{1,1,1}$  (a),  $P_{2,1,0}$  (b), and  $P_{3,0,0}$  (c) as a function of the delays  $x_i = c\tau_i$  of the impinging photons. (d-f) Theoretical output probabilities  $P_{i,j,k}^{q}$  for three indistinguishable input photons,  $P_{i,j,k}^{cl}$  for three photons out of interference and  $P_{i,j,k}^{(2)}$  for two indistinguishable and one delayed input photons. The red bars take into account the presence of partial distinguishability between the three impinging photons with indistinguishability  $p = 0.65$  whereas blue bars refer to perfectly indistinguishable photons with  $p = 1$  (see Supplementary Note 4). The dashed horizontal lines represent the classical boundaries.

![](images/abc8a032d6caa4b8e0ad0553fb937c40c1a704c30d1e92a18a28956e0963f2a0.jpg)

![](images/6e54c2df9e9d3ad86100b436ac0901276a4bd59444bf8944cb2d8b5c454c04e2.jpg)

Here  $c_{1,1,1} = -1 / \sqrt{3}$  and  $c_{\{3,0,0\}} = \sqrt{2 / 3}$ , where  $|\{i,j,k\} \rangle$  is the symmetric superposition of the three-photon states corresponding to  $(i,j,k)$  photons exiting in the three output ports. We first observe that, as a consequence of bosonic coalescence, all the terms of two photons exiting from the same output port disappear (Fig. 1c). To fully describe three-photon interference we need to introduce two relative delays between the three bosons. We theoretically calculated the probability of the different output states [(1,1,1), (2,1,0), (3,0,0)] as a function of the relative delays  $x_{m} = c\tau_{m}$  ( $m = 1, 2$ ) between the three photons. These probabilities are represented in Fig. 2a-c as surfaces in a three-dimensional space and represent an extension of the well-known Hong-Ou-Mandel curves. This representation enables a deeper insight into three-photon interference, evidencing non-trivial features as a function of the two delays. In particular, we observe the presence of three regions: (i) the three input photons are indistinguishable  $(P_{i,j,k}^{\mathrm{q}})$  when  $x_{1} \sim x_{2} \sim 0$ , this leads to a three-photon coalescence effect, resulting in a dip or a peak depending on the detected output state; (ii) only two of the three input photons are indistinguishable  $(P_{i,j,k}^{(2)})$  when  $x_{m} \sim 0 \neq x_{n}$  or  $x_{m} \sim x_{n} \neq 0$ ; (iii) the three input photons are distinguishable  $(P_{i,j,k}^{\mathrm{cl}})$  when  $x_{1} \neq x_{2} \neq 0$ , leading to classically correlated outcomes. Here, the superscript q indicates the quantum nature of the three-photon coalescence, while the superscript cl highlights that the photons behave as classical particles. Figure 2d-f compares the different probabilities corresponding to cases i-iii for each output state.

Tritter fabrication by ultrafast laser writing. The tritter device was realized by adopting femtosecond laser-writing technology[22-24]. This technique exploits nonlinear absorption of focused femtosecond laser pulses that create permanent and

The most important and most numerous reason for the localized increase of the refractive index in transparent materials. Waveguides are directly fabricated in the material bulk by translating the sample at constant speed along the desired path. This technique has the unique capability of producing integrated devices with three-dimensional geometries. Ultrafast laser-writing technique has rapidly become a powerful tool for demonstrating new quantum integrated devices, able to perform quantum logic operations[25], as well as two-photon quantum walks[26,27]. The femtosecond laser-written tritter consists of three waveguides approaching and interacting in the coupling region (Fig. 1b). Thanks to this configuration equal coupling coefficients may be obtained, in a way that a single photon entering in any input port has the same probability to exit from any of the three output ports. This three-dimensional approach, enabled by femtosecond laser writing, avoids the use of cascaded beam splitters and phase shifters that are difficult to control and provides a compact device that can be effectively scaled in more complex architectures. Although conceptually simple, the tritter needs accurate dimensioning. As a first order arrangement, we consider the waveguides lying at the vertex of an equilateral triangle, where key parameters are waveguide spacing and length in the interaction region. Actually these two parameters are not independent as, in order to achieve an equal output distribution, the coupling coefficient  $k$  and interaction length  $L$  need to satisfy the relation  $kL = 2\pi /9$  (see Supplementary Note 2). Sizing of the tritter starts from choosing the waveguide spacing  $d$  to the smallest value that avoids overlap (this will keep the device as short as possible). The chosen value of  $d$  in turn defines the coupling coefficient  $k$  and, thus, according to the previous relation, the interaction length  $L$ . However, the slightly elliptical-guided mode of the femtosecond laser-written optical waveguides and other fabrication imperfections require performing a second-order fine tuning of the device that can be accomplished by slightly shifting one of the

![](images/5a48692659326a40a5c214a747a052b4e633709e02bc23f2b6a7c8f10e80924e.jpg)

![](images/2ea7f6996b9d7996a2a0aae086625992ae4cdfed7198f3633664d709bda89832.jpg)

![](images/2a59f98e6ce472c0a32c56f3dbb9cfa08c206963fb91addcb8d0b1f16af8465f.jpg)

![](images/da789fa1224d601249f0c887716d6c75eac3801d526971ad814f5af710192c14.jpg)

![](images/9efef214edd73a1e70e43023cac261bcf385481d034d5d26f5a82e5c0f57b556.jpg)  
Figure 3 | Two-photon experimental reconstruction of the unitary matrix  $\mathcal{U}^r$  of the implemented tritter. Experimental two-photon Hong-Ou-Mandel interference for input states: (a)  $|1, 1, 0\rangle$ , (b)  $|1, 0, 1\rangle$  and (c)  $|0, 1, 1\rangle$ . For each input state all possible output ones are acquired. Error bars in the experimental points are due to poissonian statistics of the measured signal. (d-e) Real and imaginary parts of  $\mathcal{U}^r$ . (f-g) Real and imaginary parts of the theoretical tritter  $\mathcal{U}^l$ .

![](images/332bb671b1fa8b0f1b9c2eb1728cb47f36095d096ac9b0aebc6d0256dde8c53b.jpg)

![](images/328a8c6e5602f1f1fe3aebe4d3d50c64256f15bf6d8b69c38133df17772eaad4.jpg)

![](images/22b9d847c11e9116abefd220e3d217ba183e8cd22268b06b94f8cd868278a71c.jpg)

![](images/5874f1da72a8335663edd156cacb4a85f008f76d5f8a37a5bc738505369605f5.jpg)  
Figure 4 | Experimental layout. Experimental setup for the characterization of the tritter and the three-photon coalescence experiment. Two-photon and three-photon states, generated by parametric down conversion, are injected in the tritter device after the propagation through spatial delay lines. Then, coincidence detection at the output ports is performed to reconstruct the probability of obtaining a given output state realization  $(i,j,k)$ . Labels 1, 2, 3 stand for spatial modes, while letter a refers to indistinguishable photons and b to the partially distinguishable one. BBO,  $\beta$ -barium borate crystal.

three waveguides in a scalene triangle geometry. This fine tuning is performed most efficiently by an iterative procedure, where we take full advantage of the rapid prototyping capabilities of femtosecond laser waveguide writing (see Supplementary Fig. S1 for the final optimized geometry).

Two-photon characterization of the tritter device. To characterize the implemented device and to compare its unitary evolution with respect to the ideal case, we implemented the reconstruction method proposed in ref. 28. This technique consists in measuring all the possible two-photon Hong-Ou-Mandel interference fringes and then reconstructing the elements of the evolution matrix  $\mathcal{U}^r$  through a minimization procedure (see Supplementary Note 3 for more details). We show in Fig. 3

the real and imaginary parts of the reconstructed matrix  $\mathcal{U}^r$  at  $795\mathrm{nm}$  wavelength, compared with the corresponding theoretical matrix  $\mathcal{U}^t$ . To quantify the quality of the fabrication process, we evaluated the similarity  $S$  between the two corresponding Hong-Ou-Mandel visibility matrices, defined as  $\mathcal{S}_{r,t} = 1 - \sum_{i\neq j}\sum_{k\neq l}\left|\left(\mathcal{V}^t\right)_{ij;k,l} - \left(\mathcal{V}^r\right)_{ij;k,l}\right| / 18$ . The obtained value  $\mathcal{S}_{r,t} = 0.9768\pm 0.0004$  demonstrates a high correspondence of the implemented device with an ideal tritter.

Experimental three-photon interference. We experimentally tested the three-photon coalescence by adopting the experimental setup shown in Fig. 4. Four photons are produced by parametric down conversion: one of them acts as the trigger for coincidence detection, while the other three are coupled into the tritter, after

Figure 5 | Experimental results with a three-photon input state. (a) Output probabilities for different choices of the delayed photon and of the measured output state contribution. Case I: three-photon interference  $P_{i,j,k}^{q}$ . Case II: distinguishable photon on input port 2 delayed (two-photon interference)  
![](images/fa661d4f2f9ed7990ac6b7dd24392f210c5ccbcf809570c4feee1efb22f0cced.jpg)  
$P_{i,j,k}^{(2)}$ . Case III: identical photon on input port 3 delayed (two-photon interference)  $P_{i,j,k}^{(2)'}$ . Blue bars: theoretical prediction obtained from the reconstructed tritter matrix  $\mathcal{U}^r$  and partially distinguishable photon pairs. Red bars: experimental results. (b) Visibilities  $V = (\Gamma_{\infty} - \Gamma_0) / \Gamma_{\infty}$  for different choices of the delayed photon and of the measured output state contribution. Here,  $\Gamma_{\infty}$  and  $\Gamma_0$  correspond respectively to the number of four-fold coincidences when the delayed photon is, respectively, out or inside the interference region. Case A: distinguishable photon on input port 2 delayed (three-photon interference). Case B: identical photon on input port 3 delayed (three-photon interference). Case C: distinguishable photon on input port 2 out of interference region and identical photon on input port 3 delayed (two-photon interference). Blue bars: theoretical prediction obtained from the reconstructed tritter matrix  $\mathcal{U}^r$  and partially distinguishable photon pairs. Red bars: experimental results. Cyan bars: expected visibilities with classical states. Error bars are due to poissonian statistics of the measured signal.

![](images/b41904643dba3134e12c4ca8d7adeb3183a3008f37b6911f8b19164ba205b8eb.jpg)

passing through different delay lines. The output modes are detected by using optical fibre beam splitters and single-photon avalanche photodiodes. Coincidences between different detectors allow us to reconstruct the probability of obtaining a given output state. By changing the relative delays between the three photons, it is possible to observe the coalescence effects in the different experimental conditions, as shown in Fig. 2a-c. The tritter device, first characterized by single- and two-photon states at wavelength  $795\mathrm{nm}$  (see Fig. 3) has then been tested by three photons at wavelength  $785\mathrm{nm}$ , due to availability of higher transmissivity spectral filters at that wavelength. It has to be noted that the unitary matrix of the tritter  $\mathcal{U}'$  at  $785\mathrm{nm}$  is still in very good agreement with that of an ideal tritter (see equation 1), yielding a similarity  $S_{r,t}' = 0.9595 \pm 0.0003$  (see Supplementary Note 3 and Supplementary Fig. S4). We have injected a three-photon state  $|1,1,1\rangle$  and observed the different output contributions  $|1,1,1\rangle$ ,  $|2,1,0\rangle$ ,  $|3,0,0\rangle$ . Due to the partial distinguishability between photons belonging to different pairs, the expected visibilities of peaks (or dips depending on the observed contributions) change depending on which photon is delayed. We compare in Fig. 5a the experimental and theoretical output states probabilities, obtained by delaying photons in different input modes for each measured output state. The expected probability values have been calculated by introducing in the theoretical model the distinguishability parameter  $p$ , which quantifies the distinguishability between the two different pairs, and by including six-photon events generated by the source. We investigated in Fig. 5b three-photon interference when delaying the partially distinguishable photon (case A in the figure) or when delaying one of the two indistinguishable ones (case B in the figure). In addition, we also considered the case when the partially distinguishable photon is kept out of the interference region and the two indistinguishable ones have a relative delay (case C in the figure). The latter case corresponds to two-photon interference although three photons are input and measured. It is observed that cases A and B are clearly different from case C. This demonstrates that the output states that we observe in cases A and B are indeed due to three

photon interference and cannot be attributed to two-photon interaction. To characterize whether the measured three-photon interference can be attributed to a quantum effect, we also compared the obtained visibilities with the classical bounds, calculated by injecting the tritter with three equal-amplitude coherent states with randomized phases[29]. We observe that the results obtained with the  $|1,1,1\rangle$  input state outperform classical predictions, thus demonstrating the quantum origin of the measured three-photon interference. Details on the data analysis can be found in the Supplementary Note 4.

# Discussion

We reported on the experimental observation of three-photon bosonic coalescence effect occurring within an integrated, three-dimensional, three-port beam splitter realized by the ultrafast laser-writing technique. To the best of our knowledge, this result represents the first experimental observation of the bosonic coalescence of three indistinguishable photons in a symmetric three-port device. The intrinsically stable and compact nature of this device makes it a fundamental building block for future complex networks implemented by integrated optical circuits. These devices are expected to open new perspectives in many research areas of quantum information. Indeed, the  $N$ -port beam splitters may find a wide range of applications in both quantum interferometry and quantum metrology. A first theoretical analysis performed in ref. 16 shows that these devices can be exploited to build  $N$ -mode interferometers, where the adoption of quantum input states can lead to a significant enhancement in phase estimation protocols. Furthermore, the capability of conditionally generating path-entangled states may be increased by adopting structures composed of  $N$ -port beam splitters rather than conventional two-mode couplers<sup>30</sup>. This is expected to lead to a corresponding reduction in complexity of the experimental schemes in terms of the number of optical elements.

Several other contexts may benefit from the adoption of  $N$ -port beam splitters. For instance, they can be adopted for the realization of 'proof-of-principle' quantum simulators<sup>31</sup>, and,

combined in a modular structure, they can be used to realize full-scale quantum simulators for large-size quantum systems. The adoption of multiphoton-multimode platforms may indeed disclose the 'hard-to-simulate' scenario by adopting linear optics to implement a computational power beyond the one of a classical computer[32]. Furthermore, the development of complex integrated quantum devices may lead to implement fundamental tests of quantum mechanics, such as nonlocality tests, for quantum systems of increasing dimensionality[33].

# Methods

Waveguide fabrication. Waveguides are directly written in borosilicate glass substrate (EAGLE2000, Corning Inc.) using a cavity-dumped Yb:KYW oscillator, which provides 300 fs pulses at 1 MHz repetition rate. The laser beam is focused, by a  $0.6\mathrm{-NA}\times 50$  microscope objective, at  $170\mu \mathrm{m}$  (average) depth under the glass surface. Optimum irradiation parameters for single-mode waveguiding at  $795~\mathrm{nm}$  wavelength are  $220\mathrm{nJ}$  pulse energy and  $40\mathrm{mm / s}$  translation speed. Sample translation at uniform speed is provided by high precision, three-axis air-bearing stages (Aerotech FiberGlide3D, Aerotech Inc.). The produced tritter is subsequently pigtailed by bonding fibre arrays on both sides of the device in order to obtain a compact and portable device.

Four-photon source and detection apparatus. Let us refer to the experimental setup shown in Fig. 4 in the main text. A  $2\mathrm{-mm}$ -thick  $\beta$ -barium borate crystal cut for type-II phase matching is pumped by the second harmonic of a Ti:sapphire mode-locked laser beam, and generates via spontaneous parametric down conversion at second-order two polarization photon pairs over two different spatial modes. The four photons<sup>34,35</sup> of the generated state are spectrally filtered by interferential filters (wavelength  $\lambda = 785\mathrm{nm}$ ,  $\Delta \lambda = 3\mathrm{nm}$ ) and selected by four single-mode fibres placed at the output of two polarizing beam splitters. The spatial and temporal walk-off is compensated by inserting a waveplate and a  $1\mathrm{-mm}$  thick  $\beta$ -barium borate crystal crystal on each spatial mode. One of the four photons is detected to work as the trigger of the experiment. The other three photons are injected each into a single-mode fibre and, after passing through three delay lines and after polarization compensation, are coupled inside the tritter device. The output modes are sent to the detection stage. Four-fold coincidence detections are measured. The  $|1,1,1\rangle$  contribution is measured by directly sending each output mode to a single-photon detector. The  $|2,1,0\rangle$  ( $|3,0,0\rangle$ ) contribution is measured by splitting mode 1 in two (three) equal parts by means of fibre beam splitters and by placing a single-photon detector on each of the two (three) outputs of the fibre beam splitter system. The efficiencies for the three schemes including the trigger detector are respectively  $\eta^4$ ,  $(2/3)\eta^4$  and  $(2/9)\eta^4$ , being  $\eta$  the quantum efficiency of a single detector.

# References

1. Hong, C. K., Ou, Z. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
2. Ou, Z. Temporal distinguishability of an n-photon state and its characterization by quantum interference. Phys. Rev. A 74, 063808 (2006).  
3. Yamamoto, T., Koashi, M., Ozdemir, S. & Imoto, N. Experimental extraction of an entangled photon pair from two identically decohered pairs. Nature 421, 343-346 (2003).  
4. Walther, P. et al. De Broglie wavelength of a non-local four-photon state. Nature 429, 158-161 (2004).  
5. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
6. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2000).  
7. Shih, Y. H. & Alley, C. O. New type of Einstein-Podolsky-Rosen-Bohm experiment using pairs of light quanta produced by optical parametric down conversion. Phys. Rev. Lett 61, 2921-2924 (1988).  
8. Zou, X., Pahlke, K. & Mathis, W. Generation of entangled photon states by using linear optical elements. Phys. Rev. A 66, 014102 (2002).  
9. Greenberger, D. M., Home, M. A. & Zeilinger, A. Multiparticle interferometry and the quantum superposition principle. Phys. Today 46, 22-29 (1993).  
10. Greenberger, D. M., Home, M. A. & Zeilinger, A. Similarities and differences between two-particle and three-particle interference. *Fortschr. Phys.* **48**, 243-252 (2000).  
11. Pan, J.-W. et al. Multiphoton entanglement and interferometry. Rev. Mod. Phys. 84, 777-838 (2012).  
12. Zukowski, M., Zeilinger, A. & Horne, M. A. Realizable higher-dimensional two-particle entanglements via multiport beam splitters. Phys. Rev. A 55, 2564-2579 (1997).  
13. Howell, J. C. & Yeazell, J. A. Quantum computation through entangling single photons in multipath interferometers. Phys. Rev. Lett. 85, 198-201 (2000).

14. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
15. Tichy, M. C., Tiersch, M., de Melo, F., Mintert, F. & Buchleitner, A. Zero-transmission law for multiport beam splitters. Phys. Rev. Lett. 104, 220405 (2010).  
16. Spagnolo, N. et al. Quantum interferometry with 3-dimensional geometry. Sci. Rep 2, 862 (2012).  
17. Campos, R. A. Three-photon Hong-Ou-Mandel interference at a multiport mixer. Phys. Rev. A 62, 013809 (2000).  
18. Weihs, G., Reck, M., Weinfurter, H. & Zeilinger, A. Two-photon interference in optical fiber multiports. Phys. Rev. A 54, 893-897 (1996).  
19. Kowalevicz, A. M. et al. Three-dimensional photonic devices fabricated in glass by use of a femtosecond laser oscillator. Opt. Letters 30, 1060-1062 (2005).  
20. Suzuki, K., Sharma, V., Fujimoto, J. G., Ippen, E. P. & Nasu, Y. Characterization of symmetric  $[3\times 3]$  directional couplers fabricated by direct writing with a femtosecond laser oscillator. Phys. Rev. A 80, 032318 (2009).  
21. Meany, T. et al. Non-classical interference in integrated 3d multiports. Opt. Express 20, 26895-26905 (2012).  
22. Gattass, R. R. & Mazur, E. Femtosecond laser micromachining in transparent materials. Nat. Photon. 2, 219-225 (2008).  
23. Della Valle, G., Osellame, R. & Laporta, P. Micromachining of photonic devices by femtosecond laser pulses. J. Opt. A 11, 013001 (2009).  
24. Osellame, R., Hoekestra, H. J. W. M., Cerullo, G. & Pollnau, M. Femtosecond laser microstructuring: an enabling tool for optofluidic lab-on-chips. *Laser Phot. Rev.* 5, 442-463 (2011).  
25. Crespi, A. et al. Integrated photonics quantum gates for polarization qubits. Nat. Commun. 2, 566 (2011).  
26. Owens, J. O. et al. Two-photon quantum walks in an elliptical direct-write waveguide array. New J. Phys. 13, 075003 (2011).  
27. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
28. Peruzzo, A., Laing, A., Politi, A., Rudolph, T. & O'Brien, J. L. Multimode quantum interference of photons in multiport integrated devices. Nat. Commun. 2, 244 (2011).  
29. Metcalf, B. J. et al. Multi-photon quantum interference in a multi-port integrated photonic device. Nat. Commun. 4, 1356 (2013).  
30. Pryde, G. J. & White, A. G. Creation of maximally entangled photon-number states using optical fiber multiports. Phys. Rev. A 68, 052315 (2003).  
31. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
32. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. Preprint at http://arxiv.org/abs/1011.3245 (2010).  
33. Gruca, J., Laskowski, W. & Zukowski, M. Nonclassicality of pure two-qutrit entangled states. Phys. Rev. A 85, 022118 (2012).  
34. Eibl, M. et al. Experimental observation of four-photon entanglement from parametric down-conversion. Phys. Rev. Lett. 90, 200403 (2003).  
35. Radmark, M., Zukowski, M. & Bourennane, M. Experimental test of fidelity limits in six-photon interferometry and of rotational invariance properties of the photonic six-qubit entanglement singlet state. Phys. Rev. Lett. 103, 150501 (2009).

# Acknowledgements

This work was supported by FIRB-Future in Ricerca HYTEQ and ERC (European Research Council)—Starting Grant 3D-QUEST (3D-Quantum Integrated Optical Simulation; grant agreement no. 307783): http://www.3dquest.eu.

# Author contributions

All the authors coceived the experiment. A.C., R.R. and R.O. designed and fabricated the integrated tritter chip and performed the characterization measurements in the classical regime. N.S., C.V., L.A., F.S. and P.M. developed the quantum theory underlying the experiment and carried out the measurements in the quantum regime. All authors discussed the results and participated in the manuscript preparation.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Spagnolo, N. et al. Three-photon bosonic coalescence in an integrated tritter. Nat. Commun. 4:1606 doi: 10.1038/ncomms2616 (2013).

This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/3.0/