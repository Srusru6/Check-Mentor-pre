# ARTICLE OPEN

Check for updates

# Deterministic photon source interfaced with a programmable silicon-nitride integrated circuit

Ying Wang $^{1}$ , Carlos F. D. Faurby $^{1}$ , Fabian Ruf $^{2}$ , Patrik I. Sund $^{1}$ , Kasper Nielsen $^{1}$ , Nicolas Volet $^{2}$ , Martijn J. R. Heck $^{2}$ , Nikolai Bart $^{3}$ , Andreas D. Wieck $^{3}$ , Arne Ludwig $^{3}$ , Leonardo Midolo $^{1}$ , Stefano Paesani $^{1\boxtimes}$  and Peter Lodahl $^{1\boxtimes}$

We develop a quantum photonic platform that interconnects a high-quality quantum dot single-photon source and a low-loss photonic integrated circuit made in silicon nitride. The platform is characterized and programmed to demonstrate various multiphoton applications, including bosonic suppression laws and photonic entanglement generation. The results show a promising technological route forward to scale-up photonic quantum hardware.

npj Quantum Information (2023)9:94; https://doi.org/10.1038/s41534-023-00761-1

# INTRODUCTION

Single photons are a key enabler in emerging quantum technologies including secure quantum communications $^{1,2}$  and quantum computing $^{3-5}$ . A central challenge in developing scalable photonic quantum hardware is to realize high-quality single-photon sources (SPSs) and interface them with advanced photonic integrated circuits (PICs). SPSs based on solid-state quantum emitters, such as quantum dots (QDs) or color defect centers, are suitable platforms to deterministically generate near-ideal single photons $^{6-8}$ . These high-quality photon sources are embedded in III-V semiconductor materials like gallium arsenide (GaAs) or diamond, and large-scale PICs have not yet been realized on these material platforms since fabrication processes are relatively immature. Consequently, a hybrid approach is favorable where the photon source chip is feeding a PIC fabricated on a mature material platform to realize a multi-chip photonic quantum processor $^{9}$ . Ultimately the sources may be heterogeneously integrated on the PIC platform $^{10-14}$ .

To build a scalable quantum photonic platform, multiple key requirements need to be simultaneously fulfilled. The source must generate highly pure (i.e., emit only one photon at a time) and highly indistinguishable photons as generally required for quantum information processing. Subsequently, the inevitable loss associated with coupling between the source chip and the processor PIC should be reduced in order to eventually scale up the technology to many photons. Finally, the PIC chip needs to be low-loss at the operation wavelength of the photon source.

In this work, we report on the development of a modular photonic platform with all the key functionalities described above. We demonstrate the coupling of single photons from an InGaAs QD embedded in a planar GaAs photonic-crystal waveguide to a programmable low-loss PIC in SiN. Being a mature and CMOS-compatible platform, SiN is highly promising for developing the scalable and low-loss PICs required for photonic quantum technologies, with complex programmable circuits $^{15,16}$ , losses as low as  $\sim 1$  dB/m $^{17}$ , and cryogenic operation $^{18}$  recently demonstrated.

The capabilities to program large PIC circuits in SiN for quantum operations have been successfully demonstrated, but so far using only probabilistic photon sources based on spontaneous nonlinear processes $^{5,15,19}$ . Importantly, SiN is also highly transparent at

the typical emission wavelengths of QDs and enables heterogeneous integration $^{10,14,17,20}$ , although processing of photons from QD sources has yet to be demonstrated on this platform. We have realized this and report on high-fidelity multiphoton on-chip operations with a programmable SiN PIC. These capabilities are showcased via exemplary photonic quantum information protocols: tests of bosonic suppression laws, i.e., experiments on generalized HOM interference, and the probabilistic generation of entangled photonic Bell states.

# RESULTS

# Platform configuration

The experimental setup for the developed modular platform is shown in Fig. 1a. We adopt InAs QDs embedded in a p-i-n GaAs diode heterostructure as solid-state photon emitters[21]. The heterostructure is grown with molecular beam epitaxy, and a distributed Bragg reflector (DBR) is implemented below the sacrificial layer (Supplementary Note 1). The QDs are capped using a monolayer of higher band-gap material (AlAs) enabling the elimination of undesired coupling of QD exciton to the wetting layer continuum improving for the coherence of QD exciton emission[22,23]. Moreover, the QD density is modulated by gradient growth of the buffer layer thickness[24] (Supplementary Fig. 2). High-quality metal gates are realized to quench the charge noise and to tune the emitter emission wavelength via a Stark shift. A photonic crystal waveguide (PCW) planar structure, shown in Fig. 1b, is used to interface with the QDs, enabling efficient optical coupling via a combination of radiative leakage suppression and Purcell enhancement featuring broadband operation[25]. A photonic crystal mirror terminates one side of the PCW to enable single-sided emission from the device, see Fig. 1b. The sample is mounted in a closed-system cryostat at  $1.6\mathrm{K}$ . A stretched pulsed laser (pulse duration 18 ps, repetition rate of  $72\mathrm{MHz}$  and wavelength of  $942\mathrm{nm}$ ) is used to coherently excite the QD source whereby a neutral exciton in the QD is resonantly excited and subsequently emits triggered single photons. Our implementation closely follows the work of Uppu et al.[21], and the relevant differences are discussed in Supplementary Note 4. The emitted photons are routed to a shallow-etched grating (SEG) for

![](images/e34a72e6f18981bd2ee92a2bee1740d6fdfae55175f347fa7af61618dedee92a.jpg)  
Fig. 1 Experimental set-up overview. a A schematic display of the full picture of the experimental configuration. A QD embedded in a planar nanophotonic chip is excited within a cryostat to emit a stream of single photons (lower left). The stream of single photons is then converted into two streams of simultaneous photons via a free space two-mode demultiplexer (upper left), which relies on a resonant electro-optic modulator (EOM) and a polarizing beams splitter (PBS). The photon streams are coupled into a programmable SiN PIC operating at room temperature (lower right) and the output is measured via superconducting-nanowire-single-photon-detectors (SNSPDs) (upper right) (b) Scanning electron microscope (SEM) image of the GaAs nanophotonic device. c Image of the SiN device and set-up.

![](images/d754dccaf46aa8064b3354eb52eb3650fe87f96eea1d6ea3b072d43ec092a50c.jpg)

![](images/2af15b6fa373400e9e3e519a8a510d57eaa8a43746297c61b445ba5e274ea183.jpg)

collection. To achieve high collection efficiency, a DBR layer is grown below the waveguide to enhance the out-of-plane vertical emission. We designed and implemented SEGs that exploit the DBR to boost the reflection of downward emission to significantly enhance the off-plane collection efficiency from the integrated waveguide (Supplementary Note 2). We measure the efficiency to be  $21.5\%$ , corresponding to a detected  $15.6\mathrm{MHz}$  photon rate (see Fig. 2a). This efficiency is mainly limited by the not fully optimized coupling from the SEG to the fiber and by the limited efficiency of the etalon used for phononic-sideband filtering, and can readily be further improved. Notably the demonstrated source efficiency is the highest reported to date on planar GaAs nanostructures[21], which enables the integration of the source with the SiN PIC. For a detailed description of the source efficiency, see Supplementary Note 3.

The photon-emitter platform is optically interfaced to the PIC through optical fibers, as shown in Fig. 1a. Low-loss photonic circuits are realized on the SiN platform, with SiN waveguides consisting of a rectangular cross-section (100 nm thick, 1000 nm wide) surrounded by a  $\mathrm{SiO}_2$  cladding. The reconfigurability of the circuit is realized using thermal phase shifters that can be operated at switching rates in the range of  $\mathrm{kHz}^{26}$ . The length of a phase shifter is  $2\mathrm{mm}$  and it is operated at a heating power up to  $20\mathrm{mW}$  in order to implement any phase shift from 0 to  $\pi$ . Coupling to and from the chip is implemented using a fiber array and on-chip waveguide tapers, as shown in Fig. 1c. To develop photonic circuitry compatible with the QD source, we designed and optimized components required for programmable photonic quantum circuits tailored to the QD emission wavelength of  $940\mathrm{nm}$ , and in particular directional couplers for low-loss 50:50 splitters (Supplementary Note 7). These SiN components are fabricated in a multi-project wafer run, and compatible with complementary metal-oxide-semiconductor (CMOS) foundry manufacturing processes, allowing for efficient and scalable fabrication of complex PICs. In addition to smaller structures used for preliminary characterization of the platform, we implement the reconfigurable four-mode circuit shown in Fig. 1a which constitutes a tunable Fourier transform interferometer. This type of circuit finds broad use in photonic quantum information processing[27-32], and we use it to explore various classes of experiments as reported in the next sections. The propagation loss in the single-mode SiN waveguides is estimated via the cut-back method[33] to be  $\sim 0.3\mathrm{dB/cm}$  at the QD emission wavelength. The

total coupling losses to the PIC were measured to be between 4.25 and  $7\mathrm{dB}$  at the QD emission wavelength (see Supplementary Note 8). This loss value was due to the fabricated devices having an optimal wavelength (with significantly reduced losses of  $\sim 2\mathrm{dB}$ ) different from the targeted one, and can be readily improved by adjusting the taper width at the facet.

To perform multi-photon on-chip experiments, we add a free-space demultiplexer setup, as shown in Fig. 1a, to spatially separate and temporally synchronize consecutive photons emitted by the QD, yielding simultaneous photons pairs at two different input modes of the PIC.

# Platform characterization

The single-photon source was initially characterized in a free-space setup. The lifetime of the neutral exciton was measured to be 917 ps (see Fig. 2b). A near-unity single-photon purity of  $99.2\%$  at  $\pi$  pulse excitation (see Fig. 2c) was recorded together with an intrinsic Hong-Ou-Mandel (HOM) interference of subsequently emitted photons of  $\mathrm{V}_{\mathrm{HOM}} = (94.5 \pm 1.7)\%$  (see Fig. 2d) after sideband filtering with an etalon. This corresponds to a pure dephasing rate of  $0.03 \, \mathrm{ns}^{-134}$ . To characterize the quality of the PIC, we test how these near-ideal properties are affected by the circuit. To do so, we characterize the on-chip photon purity by implementing an integrated Hanbury-Brown and Twiss experiment where photons from the QD are directly injected into the SiN PIC and routed to a Mach-Zehnder interferometer (MZI) with the internal phase difference set to  $\pi / 2$  to implement a 50:50 beam-splitter.  $g^{(2)}(0)$  is measured by recording coincidences between the two outputs normalized by coincidences between different pulses, as shown in Fig. 2e, obtaining a purity of  $99.5\%$ , which is compatible with the free-space value.

To perform a HOM experiment of the on-chip photon indistinguishability, we use the demultiplexer to send single photons into each of the two input ports of the MZI structure, while scanning the internal phase shifter and coincidences between the two output detectors were recorded. By scanning the internal phase shifter of the MZI, we obtain the HOM quantum interference fringe shown in Fig. 2f, from which the corresponding HOM visibility is extracted[35]. We find  $V_{\mathrm{HOM}} = (94.3 \pm 1.2)\%$  in full agreement with the free-space value, indicating that no degradation of the photon properties was observed due to the PIC platform.

![](images/e18dff951779c5a6edf1470fdc30d824d507ab60d1c97d091e4ff72e6ddf9fb9.jpg)  
QD

![](images/a82fef28c0dd769b0396b718f4a3147fa91231f4739da24987e81fd7060c23ea.jpg)

![](images/32d83a61512427abcd70d7244808c3ed64679be8116813f996e33439411a48f8.jpg)  
Modular platform (QD + SiN Circuits)

![](images/35f0ad71044234ac8aa716c5ba0b536b597bc86f1b9ecdf95363c4a655e41229.jpg)  
Fig. 2 Single-photon source characterization performed with free-space optics (left) and on-chip using the SiN PICs (right). a Resonance fluorescence data showing the onset of Rabi oscillations when resonantly pumping the QD with a laser of pulse duration 18 ps. The QD is biased at a fixed external voltage of  $1.256\mathrm{V}$  at a wavelength of  $942\mathrm{nm}$ . b Time-resolved fluorescence measurement of the spontaneous emission rate of the emitter (green data), modeled with a single exponential decay (orange curve). The blue curve represents the characterized intrinsic instrument response function from the excitation laser pulse. c Single-photon purity  $g^{(2)}(0)$  characterization performed with a free-space Hanbury Brown and Twiss (HBT) setup (details in Supplementary Note 5), and (e) using the SiN PIC. Indistinguishability data obtained (d) in the free-space setup and (f) using an on-chip MZI circuit. In all figures, data are shown as dots and numerical fittings are shown as solid lines (Supplementary Note 6). Error bars, visible when larger than markers, represent 1 s.d. calculated assuming Poissonian photon statistics.

![](images/80aa879419ae1a73c30febf9616de38c2daeb5274603a98359268bd3008b905a.jpg)

![](images/b3b94f9041cf358c2cf107c1387a41a6c396bcff41d06e33f12725627b68fa66.jpg)

# Bosonic suppression laws

To investigate the performance of our platform for practical photonic quantum information processing applications, we use it to test generalized HOM quantum interference in the form of bosonic suppression laws in a discrete Fourier transform (DFT) interferometer. Introduced by Tichy et al. $^{27,28,36}$ , they are a generalization of the HOM quantum interference, which is a suppression of coincidences when photons are interfered on a balanced beam splitter (two-mode DFT), to higher number of modes and photons. Applications of bosonic suppression laws in photonic quantum technologies include the verification of quantum advantage experiments via boson sampling $^{27,28}$  and schemes for high-dimensional photonic quantum computing $^{29}$ .

By programming the phase shifters in the SiN PIC shown in Fig. 1, we implement a four-mode DFT described by the unitary transformation matrix  $U_{j,k} = \exp[(j - 1)(k - 1)2\pi i / 4] / 2$ , where  $j, k \in \{1, 2, 3, 4\}$  label the circuit spatial modes (Supplementary Note 7). The suppression law states that whenever a cyclic input configuration of  $n$  photons is injected to the DFT all output configurations where the value of  $\sum_{i=1}^{n}(c_i \bmod n)$  is different than zero are suppressed (i.e., have zero amplitude), where  $c_i$  represents the output mode number of the  $i$ -th photon<sup>36</sup>. For example, considering  $n = 2$  photons in a four-mode DFT, a cyclic input configuration could be sending two photons in the input modes (1, 3), for which suppression is expected at the output mode

configurations  $(c_{1} = 1, c_{2} = 2)$ ,  $(c_{1} = 1, c_{2} = 4)$ ,  $(c_{1} = 2, c_{2} = 3)$ , and  $(c_{1} = 3, c_{2} = 4)$  such that  $c_{1} + c_{2}$  is an odd number.

We experimentally test the suppression law by demultiplexing photon pairs from the quantum emitter and injecting them in all six possible pairs of different input modes of the integrated DFT. The output statistics for all antibunched two-photon output configurations are measured via four superconducting nanowire single-photon detectors connected to the output modes (see Fig. 1) and analyzed with a time-tagster. The results are shown in Fig. 3a, where the expected suppressed and enhanced configurations are highlighted in red and green, respectively. The experimental data show good agreement with the theoretical expectations, i.e., showing clear suppression of the configurations which sum to an odd number for the cyclic inputs. The remaining contributions to the amplitudes of suppressed configurations can be well explained considering the finite degree of indistinguishability of the photons generated by the quantum emitter, as analyzed in Supplementary Note 7.

# Photonic entanglement generation and characterization

We now proceed to investigate the generation of photon-photon entanglement, a key building block in photonic quantum information processing. A pair of path-encoded qubits can be encoded in two photons propagating in the four-mode SiN PIC associating the occupation of each mode to the computational

![](images/ecbe14ecfa72566183d9fd19ba91167a4a6a98f602dc18775270446cd1ed25ff.jpg)  
a  
Out (1,2) Out (1,3) Out (1,4) Out (2,3) Out (2,4) Out (3,4)

![](images/5c1a4677ab3988c2790c2e069cbfdf489613f4e8ff9838af61a226f2509d14f1.jpg)  
b

![](images/3c4cded5a3cff74a7f3f52f5385feff69819a0b55bd17461e8c5fec83062191e.jpg)  
Fig. 3 Quantum information processing experimental results. a Experiment result of Bosonic suppression laws. Raw detection histograms are reported for all anti-bunched input-output configurations, together with the associated measurement probabilities obtained where the raw data is plotted in red while the expected curve is in black. The combinations that are expected to be suppressed and enhanced by the suppression law are highlighted in red and green, respectively. b Correlation data for Pauli  $X_{1}X_{2}, Y_{1}Y_{2}$ , and  $Z_{1}Z_{2}$  qubit measurements on the generated Bell state  $|\psi^{+}\rangle$ . Top histograms are measured expectation values, while bottom values are theoretical expectations. c Density matrix reconstruction of the post-selected Bell state via state tomography. The red pillars represent the absolute values of the reconstructed density matrix, with transparent dashed pillars representing theoretical expectations. The corresponding measured state fidelity for  $|\psi^{+}\rangle$  is  $92\%$ .  
C

qubit states as  $1 \mapsto |0\rangle_1$ ,  $2 \mapsto |1\rangle_1$ ,  $3 \mapsto |0\rangle_2$ , and  $4 \mapsto |1\rangle_2$ . When we inject a photon in each of the input modes 1 and 3, the SiN circuit transforms the input state into a superposition, which leads to the entangled Bell state  $|\psi^{+}\rangle = (|0\rangle_{1}|1\rangle_{2} + |1\rangle_{1}|0\rangle_{2}) / \sqrt{2}$ . This state is obtained after post-selecting on the two-photon coincidence events where each photon ends up in separate qubit modes $^{37-39}$ , which happens with a success probability of  $50\%$ . The MZIs and phase-shifters at the output of the circuit (see Fig. 1) can be used to measure the two qubits in arbitrary qubit bases, which we use to perform a tomographic reconstruction and analysis of the generated entangled state. More details on the functioning of the circuit can be found in Supplementary Note 7.

The experimental results are reported in Fig. 3b, c. The two input photons are again obtained by demultiplexing the stream of photons from the QD. Correlation data in the Pauli matrices bases  $X_{1}X_{2}$ ,  $Y_{1}Y_{2}$ , and  $Z_{1}Z_{2}$  are shown in Fig. 3b, showing high correlations in the first case and anticorrelations for the latter two, as expected for the  $|\psi^{+}\rangle$  state. Measuring the qubits in other additional Pauli bases allows us to reconstruct the density matrix of the output state via quantum state tomography $^{40}$ . The obtained density matrix is reported in Fig. 3c, which presents a fidelity of  $92\%$  with the ideal  $|\psi^{+}\rangle$  entangled state, providing another confirmation of the good performance of the PIC. The remaining infidelity can again be attributed to partially distinguishable photons, as analyzed in Supplementary Note 7.

# DISCUSSION

We have demonstrated a modular quantum photonic platform based on a high-quality and efficient QD single-photon source interfaced with a low-loss and scalable SiN PIC. This allowed us to demonstrate various on-chip multiphoton quantum experiments relevant to emerging photonic quantum technologies. The Bosonic suppression laws were realized for the first time for a solid-state photon source, which was enabled by the controllable integrated circuits. Several improvements of the experiments are readily possible by further optimization of the components design and improved packaging of the chips in order to reduce coupling losses. This will enable experiments with an increasing number of photons and ultimately

large-scale photonic quantum technologies. The direct heterogeneous integration of the solid-state photon sources with SiN PICs represents a potentially important route to further reduce losses. In which case the PIC is required to operate at cryogenic temperatures. We note that the thermal phase shifters used here are not well suited to such cryogenic environment. Phase shifters based on electro-optomechanical (MEMS) devices or heterogeneous integration with electro-optic materials, such as  $\mathrm{BaTiO_3}$ , represent more suitable alternatives. For example, recent advances have shown the possibility of large-scale integration of quantum emitters and waveguides with pick-and-place techniques in similar platforms. Such techniques can be readily adapted also to our high-quality photon sources as they are embedded in photonic nanostructures suitable for transfer-printing onto SiN. Achieving a platform that explores both state-of-the-art QD photon sources with the scalability of CMOS-compatible PICs in SiN represents a promising avenue for developing photonic quantum technologies. In this work, we have taken the first steps to explore such opportunities.

# DATA AVAILABILITY

Data underlying the results presented in this paper are available https://doi.org/10.17894/ucph.9000be18-5de4-4dac-bb2c-5f2b1c9ba4fb.

# CODE AVAILABILITY

The data analysis codes used in this paper are available from the corresponding authors upon reasonable request.

Received: 14 March 2023; Accepted: 8 September 2023; Published online: 25 September 2023

# REFERENCES

1. Kolodnyński, J. et al. Device-independent quantum key distribution with single-photon sources. Quantum 4, 260 (2020).  
2. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
3. Knill, E., Laflamme, R. T. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).

4. Zhong, H.-S. et al. Quantum computational advantage using photons. Science 370, 1460-1463 (2020).  
5. Madsen, L. S. et al. Quantum computational advantage with a programmable photonic processor. Nature 606, 75-81 (2022).  
6. Lodahl, P., Ludwig, A. & Warburton, R. J. A deterministic source of single photons. Phys. Tod. 75, 44-50 (2022).  
7. Aharonovich, I., Englund, D. & Toth, M. Solid-state single-photon emitters. Nat. Photon. 10, 631-641 (2016).  
8. Zhou, X., Zhai, L. & Liu, J. Epitaxial quantum dots: a semiconductor launchpad for photonic quantum technologies. Photonics Insights 1, R07 (2023).  
9. Uppu, R., Midolo, L., Zhou, X., Carolan, J. & Lodahl, P. Quantum-dot-based deterministic photon-emitter interfaces for scalable photonic quantum technology. Nat. Nanotechnol. 16, 1308-1317 (2021).  
10. Davanco, M. et al. Heterogeneous integration for on-chip quantum photonic circuits with single quantum dot devices. Nat. Commun. 8, 889 (2017).  
11. Singh, A. et al. Quantum frequency conversion of a quantum dot single-photon source on a nanophotonic chip. Optica 6, 563-569 (2019).  
12. Shadmani, A. et al. Integration of GaAs waveguides on a silicon substrate for quantum photonic circuits. Opt. Express 30, 37595-37602 (2022).  
13. Osada, A. et al. Strongly coupled single-quantum-dot-cavity system integrated on a cmos-processed silicon photonic chip. Phys. Rev. Applied. 11, 024071 (2019).  
14. Wan, N. H. et al. Large-scale integration of artificial atoms in hybrid photonic circuits. Nature 583, 226-231 (2020).  
15. Taballione, C. et al.  $8 \times 8$  reconfigurable quantum photonic processor based on silicon nitride waveguides. Opt. Express 27, 26842-26857 (2019).  
16. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
17. Chanana, A. et al. Ultra-low loss quantum photonic circuits integrated with single quantum emitters. Nat. Commun. 13, 7693 (2022).  
18. Dong, M. et al. High-speed programmable photonic circuits in a cryogenically compatible, visible-near-infrared 200 mm cmos architecture. Nat. Photon. 16, 59-65 (2022).  
19. Smith, D. et al. A universal 20-mode quantum photonic processor in silicon nitride. In Quantum 2.0, QW4B-2 (Optica Publishing Group, 2022).  
20. Tien, M.-C. et al. Ultra-high quality factor planar  $\mathrm{Si}_{3}\mathrm{N}_{4}$  ring resonators on Si substrates. Opt. Express 19, 13551-13556 (2011).  
21. Uppu, R. et al. Scalable integrated single-photon source. Sci. Adv. 6, eabc8268 (2020).  
22. Ludwig, A. et al. Ultra-low charge and spin noise in self-assembled quantum dots. J. Cryst. Growth 477, 193-196 (2017).  
23. Lobl, M. C. et al. Excitons in InGaAs quantum dots without electron wetting layer states. Commun. Phys. 2, 93 (2019).  
24. Bart, N. et al. Wafer-scale epitaxial modulation of quantum dot density. Nat. Commun. 13, 1633 (2022).  
25. Javadi, A., Mahmoodian, S., Söllner, I. & Lodahl, P. Numerical modeling of the coupling efficiency of single quantum emitters in photonic-crystal waveguides. J. Opt. Soc. Am. B 35, 514-522 (2018).  
26. Roeloffzen, C. G. et al. Low-loss si3n4 triplet optical waveguides: technology and applications overview. IEEE J. Sel. Top. Quantum Electron. 24, 1-21 (2018).  
27. Tichy, M. C., Mayer, K., Buchleitner, A. & Mølmer, K. Stringent and efficient assessment of boson-sampling devices. Phys. Rev. Lett. 113, 020502 (2014).  
28. Crespi, A. et al. Suppression law of quantum states in a 3d photonic fast fourier transform chip. Nat. Commun. 7, 10469 (2016).  
29. Paesani, S., Bulmer, J. F., Jones, A. E., Santagati, R. & Laing, A. Scheme for universal high-dimensional quantum computation with linear optics. Phys. Rev. Lett. 126, 230504 (2021).  
30. Bacco, D., Bulmer, J. F., Erhard, M., Huber, M. & Paesani, S. Proposal for practical multidimensional quantum networks. Phys. Rev. A 104, 052618 (2021).  
31. Marshall, J. Distillation of indistinguishable photons. Phys. Rev. Lett. 129, 213601 (2022).  
32. Bell, T. J. et al. Protocol for generation of high-dimensional entanglement from an array of non-interacting photon emitters. New J. Phys. 24, 013032 (2022).  
33. Peczek, A., Mai, C., Winzer, G. & Zimmermann, L. Comparison of cut-back method and optical backscatter reflectometry for wafer level waveguide characterization. In Proc. 33rd International Conference on Microelectronic Test Structures (ICMTS), 1-3 (IEEE, 2020).  
34. Tighineanu, P., DreeBen, C. L., Flindt, C., Lodahl, P. & Sorensen, A. S. Phonon decoherence of quantum dots in photonic structures: broadening of the zero-phonon line and the role of dimensionality. Phys. Rev. Lett. 120, 257401 (2018).  
35. Adcock, J. C., Vigliar, C., Santagati, R., Silverstone, J. W. & Thompson, M. G. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10, 1-6 (2019).  
36. Tichy, M. C., Tiersch, M., de Melo, F., Mintert, F. & Buchleitner, A. Zero-transmission law for multiport beam splitters. Phys. Rev. Lett. 104, 220405 (2010).  
37. Ralph, T. C., Langford, N. K., Bell, T. & White, A. Linear optical controlled-not gate in the coincidence basis. Phys. Rev. A 65, 062324 (2002).

38. Pont, M. et al. High-fidelity generation of four-photon ghz states on-chip. Preprint at https://doi.org/10.48550/arXiv.2211.15626 (2022).  
39. Fyrillas, A. et al. Certified randomness in tight space. Preprint at https://doi.org/10.48550/arXiv.2301.03536 (2023).  
40. James, D. F., Kwiat, P. G., Munro, W. J. & White, A. G. Measurement of qubits. Phys. Rev. A 64, 052312 (2001).  
41. Sharma, S., Kohli, N., Briere, J., Nabki, F. & Menard, M. Integrated  $1 \times 3$  mem silicon nitride photonics switch. Opt. Express 30, 22200-22220 (2022).  
42. Eltes, F. et al. An integrated optical modulator operating at cryogenic temperatures. Nat. Mater. 19, 1164-1168 (2020).  
43. Roelkens, G. et al. Micro-transfer printing for heterogeneous si photonic integrated circuits. IEEE J. Quantum Electron. 29, 1-14 (2022).

# ACKNOWLEDGEMENTS

We thank Freja T. Østfeldt, Cecile T. Olesen, Camille Papon, Søren Preisler, and Mikkel T. Mikkelsen for experimental assistance. We acknowledge LioniX International B.V. for the SiN device fabrication. We acknowledge Larissa Vertchenko for assistance with producing Fig. 1a and Julian Curry Robinson-Tait for taking the photograph shown in Fig. 1c. We acknowledge funding from the Danish National Research Foundation (Center of Excellence "Hy-Q," grant number DNRF139), the Novo Nordisk Foundation (Challenge project "Solid-Q"), and Innovationsfonden (grant No. 9090-00031B, FIREQ). S.P. acknowledges funding from the Cisco University Research Program Fund (nr. 2021-234494), from the Marie Skłodowska-Curie Fellowship project QSun (nr. 101063763), and from the VILLUM FONDEN research grant VIL50326. L.M. acknowledges funding from the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation program (No. 949043, NANOMEQ). N.B., A.D.W., and A.L. acknowledge funding from the BMBF contract (No. 16KISQ009).

# AUTHOR CONTRIBUTIONS

F.R. simulated and designed the SiN components, assembled the circuit design, and taped it out to fabrication. N.B., A.D.W., and A.L. carried out the growth and design of the wafer for the photon source. Y.W. and L.M. designed and fabricated the nanostructures for the photon source. Y.W., C.F.D.F., P.I.S., K.N., and S.P. assembled the full experimental setup. Y.W. and C.F.D.F. carried out and analyzed the experiments. Y.W., C.F.D.F., F.R., S.P., and P.L. wrote the manuscript with inputs from all authors. N.V., M.J.R.H., S.P., and P.L. supervised the project.

# COMPETING INTERESTS

P.L. is a founder of the company Sparrow Quantum which commercializes single-photon sources. The authors declare no other conflicts of interest.

# ADDITIONAL INFORMATION

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41534-023-00761-1.

Correspondence and requests for materials should be addressed to Stefano Paesani or Peter Lodahl.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/707eda5f186779e337a5df836b7e7cd88ed26447bd4473cfda0e60cf941b8faf.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023