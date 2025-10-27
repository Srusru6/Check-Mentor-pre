# On-chip generation of high-dimensional entangled quantum states and their coherent control

Michael Kues $^{1,2*}$ , Christian Reimer $^{1*}$ , Piotr Roztocki $^{1}$ , Luis Romero Cortés $^{1}$ , Stefania Sciara $^{1,3}$ , Benjamin Wetzel $^{1,4}$ , Yanbing Zhang $^{1}$ , Alfonso Cino $^{3}$ , Sai T. Chu $^{5}$ , Brent E. Little $^{6}$ , David J. Moss $^{7}$ , Lucia Caspani $^{8,9}$ , José Azaña $^{1}$  & Roberto Morandotti $^{1,10,11}$

Optical quantum states based on entangled photons are essential for solving questions in fundamental physics and are at the heart of quantum information science. Specifically, the realization of high-dimensional states (D-level quantum systems, that is, quids, with  $D > 2$ ) and their control are necessary for fundamental investigations of quantum mechanics, for increasing the sensitivity of quantum imaging schemes, for improving the robustness and key rate of quantum communication protocols, for enabling a richer variety of quantum simulations, and for achieving more efficient and error-tolerant quantum computation. Integrated photonics has recently become a leading platform for the compact, cost-efficient, and stable generation and processing of non-classical optical states. However, so far, integrated entangled quantum sources have been limited to qubits ( $D = 2$ ) $^{8-11}$ . Here we demonstrate on-chip generation of entangled qudit states, where the photons are created in a coherent superposition of multiple high-purity frequency modes. In particular, we confirm the realization of a quantum system with at least one hundred dimensions, formed by two entangled quids with  $D = 10$ . Furthermore, using state-of-the-art, yet off-the-shelf telecommunications components, we introduce a coherent manipulation platform with which to control frequency-entangled states, capable of performing deterministic high-dimensional gate operations. We validate this platform by

measuring Bell inequality violations and performing quantum state tomography. Our work enables the generation and processing of high-dimensional quantum states in a single spatial mode.

Integrated photonics makes use of the well developed semiconductor industry to fabricate optical waveguides and functional devices on compact and mass-produced chips $^{12}$ , which are increasingly being used to realize stable, low-cost and practical components for optical quantum systems $^{7}$ . Among the many such on-chip optical quantum sources are devices emitting single photons $^{13}$ , as well as entangled two-photon states making use of the polarization $^{8,9}$ , spatial $^{10,14}$ , or temporal $^{11,15}$  degree of freedom. Large-scale quantum states, which are necessary for meaningful quantum information processing, for example, can be achieved by increasing the number of entangled photons and/or their dimensionality $^{16}$ . Recently the on-chip generation of two-dimensional four-photon entangled states was demonstrated $^{17}$ . However, this approach is limited in that the detection rate of multi-photon states fundamentally diminishes with an increasing number of photons, in turn reducing the information processing performance $^{16}$ . Remarkably, the use of higher-dimensional states enables the amount of quantum information to be increased without reducing the detection rate $^{16}$ . Making use of spatial modes in free-space experiments, high-dimensional Bell inequality violations $^{18}$  and Einstein-Podolsky-Rosen experiments $^{19}$  have, for example, been

![](images/bcd078b0e34b0f43fbec1d0900711610f99e9666a53453f6c7539e7636ff8e22.jpg)  
Figure 1 | Experimental setup for high-dimensional quantum state generation and control. A passively mode-locked laser was coupled into the integrated micro-ring resonator after being spectrally filtered to excite precisely a single resonance. Spontaneous four-wave mixing (SFWM) (see left inset) led to the generation of photon pairs (signal and idler) spectrally  
symmetric to the excitation and in a quantum superposition of the frequency modes defined by the resonances. Programmable filters and a modulator were used for manipulating the state (the right inset shows frequency sideband generation by the modulator as a function of frequency  $\nu$ ), before the signal and idler photons were detected by two single photon counters.

achieved. In contrast, no integrated source has managed to produce such desired high-dimensional qudit states of  $D > 2$ . This is because current approaches for on-chip entanglement require, for the generation and processing of high-dimensional states, a large increase in quantum circuit complexity. In particular, path-entanglement qudit schemes necessitate  $D$  coherently excited identical sources and a complex concatenation of beam splitters $^{20}$ , while high-dimensional temporal entanglement demands complicated stabilized multi-arm interferometers $^{21}$ .

Here we show that the frequency domain $^{22-24}$  offers a unique framework within which to generate high-dimensional states on a photonic chip and to manipulate them in a single spatial mode. Our method exploits spontaneous four-wave mixing (SFWM) in an integrated nonlinear micro-ring resonator $^{17}$ , as schematized in Fig. 1. In particular, we used a spectrally filtered mode-locked laser to excite a single resonance of the micro-ring at a wavelength of about  $1,550 \mathrm{~nm}$ , in turn producing pairs of correlated signal and idler photons spectrally symmetric to the excitation field and which cover multiple resonances; see Fig. 1. The individual photons were generated in a superposition of multiple frequency modes, and owing to the energy conservation of SFWM, this approach leads to the realization of a two-photon high-dimensional frequency-entangled state.

We performed two experiments to characterize the dimensionality of the generated state. The large free spectral range (FSR) of the ring cavity (about  $200\mathrm{GHz}$ )—that is, the spectral separation between adjacent resonance modes—enabled us to use a commercially available telecommunications programmable filter (see Methods) to individually select and manipulate the states in these modes (given the filter's operational bandwidth of  $1527.4\mathrm{nm}$  to  $1567.5\mathrm{nm}$ , we were able to access ten signal and ten idler resonances). We measured the joint spectral intensity, describing the two-photon state's frequency distribution (see Methods). Specifically, we routed different frequency modes of the signal and idler photons to two single photon detectors and counted photon coincidences for all sets of mode combinations. As shown in Fig. 2a, photon coincidences were measured only for mode combinations spectrally symmetric to the excitation, a characteristic of frequency-entangled states. In addition, we evaluate the Schmidt number of our source. This parameter describes the lowest number of relevant orthogonal modes in a bipartite system, and therefore describes its effective dimension. Through a Schmidt mode decomposition of the correlation matrix (see Methods), we extracted the lower bound for the Schmidt number to be 9.4; see Fig. 2b.

Owing to the narrow spectral linewidth of the photons (about  $800\mathrm{MHz}$ ) and the related long coherence time (about 0.6 ns), the effective time resolution of our full detection system (about 100 ps) was sufficient to perform time-domain measurements and extract the maximal dimensionality of the state (see Methods). Specifically, we measured the second-order coherence of the signal and idler fields using a Hanbury Brown and Twiss setup comprised of a 50:50 beam splitter and a photon coincidence detection system. The maximum of the second-order coherence function is directly related to the number of effective modes  $N_{\mathrm{eff}}$ , that is,  $g_{s,s}^{(2)}(t = 0) = 1 + \frac{1}{N_{\mathrm{eff}}};$  where subscript 's,s' refers to 'signal, signal' (see Methods). By individually selecting ten signal and ten idler resonances, we confirmed that the photons from each single resonance are in a high-purity quantum state (one measured effective mode per resonance); see inset to Fig. 2b. In turn, the two-photon state, defined over a pair of single resonances (one signal and one idler) symmetric to the excitation frequency, is separable and has a Schmidt number approaching one, that is, it does not contain any frequency entanglement. Consequently, a two-photon entangled quantum state comprised of multiple such pure frequency mode pairs has a Schmidt number with an upper bound given by the sum of the individual Schmidt numbers, which we measured to be  $10.45 \pm 0.53$  for the ten resonance pairs considered; see Fig. 2b. As the lower and upper bound practically coincide, we conclude that the number of relevant orthogonal modes is indeed ten.

![](images/620cbeeee8e3aae6c1e175f4befe6e4ade17b72c2d4d35a43dc4e8dd9e5c449c.jpg)

![](images/6c9dbecdde72696ac570372e11ce5faedc1a8100485c79f01cf99d2721eead1e.jpg)  
Figure 2 | Characterization of the quantum state dimensionality. a, Measured joint spectral intensity of the high-dimensional quantum state, showing photon coincidences only at symmetric mode pairs (that is, on the diagonal of the matrix) and revealing a frequency correlation. b, Two-photon state dimensionality (Schmidt number) as a function of the considered resonance pairs, symmetric to the excitation frequency, with the upper bound (blue crosses) obtained from the second-order coherence, and lower bound (red circles) calculated from the correlation matrix. The inset in b shows the measured second-order coherence  $g^{(2)}$  of a single photon emitted at one specific resonance with a maximum of  $1.92 \pm 0.03$ , corresponding to  $1.086 \pm 0.03$  effective modes. The experiment was repeated for each signal and idler resonance, returning comparable values. The error bars represent the  $95\%$  confidence bounds of the coefficient retrieved from a fit to the second-order coherence curve. Source Data for this figure is available online.

These measurements confirmed that one photon pair simultaneously spans multiple frequency modes, forming a high-dimensional entangled state of the form:

$$
| \Psi \rangle = \sum_ {k = 1} ^ {D} c _ {k} | k \rangle_ {\mathrm {s}} | k \rangle_ {\mathrm {i}}, \text {w i t h} \sum | c _ {k} | ^ {2} = 1 \tag {1}
$$

Here  $|k\rangle_{\mathrm{s}}$  and  $|k\rangle_{\mathrm{i}}$  are the pure, single-frequency quantum states of the signal and idler photons, respectively, and  $k = 1,2,\dots,D$  is the mode number, as indicated in Fig. 3a. Such a state (equation (1)) is of particular importance for quantum information processing[25]. In

![](images/f57ee3604b40194e5d698827043a2cde92a700cb09bc7439b780835c5b96cb3f.jpg)  
Figure 3 | Experimental implementation of the coherent control of frequency-entangled high-dimensional quantum states. Individual steps to control, manipulate and characterize the high-dimensional quantum states are displayed, showing for each one the equipment used and a schematic of the modification imposed on the quantum state in the spectral domain. a, The initial states  $|\Psi \rangle$  were generated using the microring resonator (MRR)-based operational principle illustrated in Fig. 1. b, Using a programmable filter (PF1), any arbitrary spectral phase and amplitude mask can be imposed on the quantum states for manipulation. c, An electro-optic modulator (Mod) driven by a radio-frequency synthesizer was used to coherently mix different frequency components of the high-dimensional states. In particular, such an operation can be

particular, only pure states show efficient Hong-Ou-Mandel interference for gate implementation, which is at the basis of linear optical quantum computation<sup>1</sup>. Furthermore, this entangled state can be turned under a single-photon unitary transformation into a linear cluster state<sup>26</sup>, required for the measurement-based quantum computation concept<sup>27</sup>.

In general, the exploitation of audit states for quantum information processing motivates the need for high-dimensional operations that enable access to multiple modes with a minimum number of components. Although the individual elements (phase shifters and beam splitters) employed in the framework of spatial-mode quantum information processing usually operate on only one or two modes at a

precisely controlled by using appropriate electronic radio-frequency signals for the mixing of 2, 3, 4 or (in principle) more adjacent frequency modes. d, A second programmable filter (PF2) can impose an amplitude and phase mask and route the signal and idler to two different paths. e, The photons were then detected using single photon counters and timing electronics. This step, together with the previous adjustable coherent control, allows the implementation of adaptable projections, which can then be used, for example, for Bell measurements or quantum state tomography (shown in Fig. 4). The complete mathematical description of all operations (indicated by  $A_{\mathrm{PF1}}$ ,  $A_{\mathrm{PF2}}$  and  $A_{\mathrm{Mod}}$ ) can be found in Methods.

time $^{1}$ , the frequency domain is ideally suited for global operations, that is, it can act on all system modes simultaneously. Through the merging of the fields of quantum state manipulation and ultrafast optical signal processing, state-of-the-art, yet established radio-frequency and telecommunications technologies $^{28}$  can be used to address multiple frequency modes simultaneously and enact high-dimensional coherent control and fundamental optical gate operations, achieving a scalable and practical quantum platform $^{29}$ . In particular, optical phase gates for manipulating high-dimensional quuds can be directly implemented using programmable phase filters. The coherent mixing of multiple modes (a high-dimensional 'beam splitting' in the frequency domain) can be achieved through deterministic frequency conversion in

![](images/d2d0b418cf15e057515e29c17b194ce6eafd86e10d85d671f067e7dd6336ab0e.jpg)  
Qudit two-photon interference

![](images/585acaebc2f61104f1ca3e1deefba021ec9963254660eae7c8f2a0c8cbc67c04.jpg)  
Reconstructed density matrix

![](images/cc491a3f980023f49e6a1d15610e59594e69e02fa57d36b8e6d7311fcea61a8b.jpg)

![](images/487522550166bf1fb8110399d09bf66ed1ee22bddb34668b5252fb91680b1f16.jpg)

![](images/07a21dd3169e381be0cb5d59b0fe36018e0c39073d7663835a93e8d690271192.jpg)

![](images/a2c546653e5c75bd756725695680b6944dced1319ba6f79f8cf15e7a7f73fae4.jpg)  
Figure 4 | Bell inequality violation and quantum state tomography of frequency-entangled states. To demonstrate the viability of the coherent control scheme described in Fig. 3, we performed a set of projection measurements. For the quantum interference characterization of qubits with  $D = 2$  (a),  $D = 3$  (b) and  $D = 4$  (c), such states were projected on a superposition of  $D$  frequency modes with different phases. By changing these phases, a variation in the coincidence counts was measured (the flat black curve being the recorded background). Raw visibilities of  $83.6\%$ ,  $86.6\%$  and  $86.4\%$  for the quantum interference were obtained (without  
background subtraction), exceeding the visibilities of  $71\%$ ,  $77\%$  and  $81.7\%$ , that are respectively required to violate a Bell inequality for the  $D = 2$ ,  $D = 3$  and  $D = 4$  states. By exploiting the ability to carry out arbitrary projection measurements on the signal and idler photon independently, we performed full quantum state tomography to reconstruct experimentally the density matrix of the entangled qudit states. We achieved fidelities of  $88.5\%$ ,  $80.9\%$ , and  $76.6\%$  for  $D = 2(\mathbf{d})$ ,  $D = 3(\mathbf{e})$  and  $D = 4(\mathbf{f})$ , respectively, demonstrating very good agreement between the measured and the expected maximally entangled states. Source Data for this figure is available online.

electro-optic modulators. More importantly, because these two components are electronically tunable, versatile operations can be performed in real time without modifying the experimental setup (or the device), simply by adjusting the filter control and electrical modulation signal. By combining these elements, high-dimensional photon operations can be implemented in a single and robust spatial mode.

To implement this concept, we realized a setup to perform basic gate operations for coherent state control using a configuration composed of two programmable filters and one electro-optic phase modulator, as schematized in Fig. 1 and explained in more detail in Fig. 3. The first programmable filter was used to impose an arbitrary spectral amplitude and phase mask on the high-dimensional state; see Fig. 3b. This manipulated state was then sent to an electro-optic phase modulator, which was driven by a radio-frequency synthesizer (see Methods). The imposed phase modulation generated coherent sidebands from the input frequency modes; see inset in Fig. 1. When the sideband frequency shift was chosen to match the spectral mode separation of the quantum state (that is, the FSR), these input frequency modes were coherently mixed; see Methods and Fig. 3c. Then, a second programmable filter (Fig. 3d) was used to select different, individual frequency components of the manipulated state through the application of a second amplitude mask. Finally, each of the two photons was routed to a separate single photon detector for coincidence counting (Fig. 3e).

We used this manipulation scheme to design well defined quantum operations, which we exploited for Bell-test measurements and

quantum state tomography. In particular, we prepared the radiofrequency driving signal in such a way to enable the mixing of two, three or four adjacent frequency modes (see Methods). In combination with single photon detection, this allowed us to perform projection measurements of the form  $|\Psi_{\mathrm{proj}}\rangle = \sum_{k=0}^{D-1} \alpha_k e^{i\varphi_k} |\overline{k} + k\rangle$ , for a given frequency mode  $\overline{k}$ , where the projection amplitudes  $\alpha_k$  as well as the phases  $\varphi_k$ , can be arbitrarily chosen for each photon.

Since the state amplitudes  $c_k$  in equation (1) were measured to be very similar (see Fig. 2a) we assumed the generation of maximally entangled states with equal amplitudes, that is,  $|\Psi\rangle = \sum_{k=1}^{D}c_k|k\rangle_s|k\rangle_i \approx \frac{1}{\sqrt{D}}\sum_{k=1}^{D}|k\rangle_s|k\rangle_i$ .

By considering any two, three and four adjacent frequency modes, we characterized the entangled quantum states and compared our measurements to these ideal cases. Using the projections for both photons  $|\Psi_{\mathrm{proj}}\rangle = \frac{1}{\sqrt{D}}\sum_{k = 0}^{D - 1}e^{ik\theta}|\overline{k} +k\rangle$ , quantum interference was measured in the coincidence counts as a function of the phase  $\theta$  (see Methods). The quantum interference for  $D = 2,3$  and 4 is shown in Fig. 4a-c with raw visibilities (without background subtraction) of  $V_{2} = 83.6\%$ ,  $V_{3} = 86.6\%$  and  $V_{4} = 86.4\%$  (where 'visibility' provides a measure for the quantum interference, defined for the different dimensions in Methods). These values violate the respective Bell inequalities<sup>2</sup>, as they exceed the thresholds of  $71\%$ ,  $77\%$  and  $81.7\%$ , respectively, thus confirming entanglement

(see Methods). Furthermore, a larger set of projection measurements was used to perform quantum state tomography, a method that allows the full experimental characterization of an unknown quantum state by reconstructing its density matrix (see Methods). Figure 4d–f illustrates these matrices for  $D = 2$ , 3 and 4, showing very good agreement between the maximally entangled and measured quantum states, with fidelities of  $88.5\%$ ,  $80.9\%$  and  $76.6\%$ , respectively.

In conclusion, by exploiting a frequency-domain approach, our scheme allows the direct generation of high-dimensional entangled two-photon states (composed of a quantum superposition of high-purity states) in an integrated platform. We achieved flexible coherent control of these states through the manipulation of their frequency components using state-of-the-art, yet commercially available programmable telecommunications filters and off-the-shelf radio-frequency photonics components. This makes possible the simple execution of  $D$ -dimensional manipulations and mode-mixing operations in a single, robust spatial mode, and furthermore enabling their combination with other entanglement concepts. Our scheme finds immediate application, for example, in fundamental investigations of quantum nonlocality and high-dimensional quantum state characteristics, as well as in large-alphabet fibre-based quantum communications. By sending the entangled states through a 24.2-km-long fibre telecommunications system (standard single mode and dispersion-compensating fibre elements), and then repeating the Bell inequality test, we confirmed that the entanglement was preserved over large propagation distances; see Methods and Extended Data Fig. 1. Furthermore, the concatenation<sup>30</sup> of the basic manipulation units shown here, as well as the implementation of arbitrary radio-frequency modulation waveforms and phase masks, will enable the realization of more complex and efficient gates, thus allowing access to high-dimensional quantum computing logic in optical circuits of manageable experimental complexity. For this, the quality and detection efficiency of the states can be considerably enhanced by reducing insertion losses of the coherent control elements (here 14.5 dB). Using on-chip wavelength and phase filters together with integrated phase modulators will greatly reduce the losses and enable the implementation of several components in a compact platform<sup>12</sup>.

Remarkably, our approach can also easily support the generation and control of even higher dimensional states. This can be achieved, for example, by decreasing the FSR of the resonator and using a programmable filter with a higher frequency resolution to access the full dimensionality of the generated state. For example, the maximum modulation bandwidth of  $600\mathrm{GHz}$  used here together with an FSR of about  $6.25\mathrm{GHz}$  would readily lead to a  $96\times 96$  dimensional system, corresponding to as many as 13 qubits.

Online Content Methods, along with any additional Extended Data display items and Source Data, are available in the online version of the paper; references unique to these sections appear only in the online paper.

# Received 30 December 2016; accepted 9 May 2017.

1. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
2. Collins, D., Gisin, N., Linden, N., Massar, S. & Popescu, S. Bell inequalities for arbitrarily high-dimensional systems. Phys. Rev. Lett. 88, 040404 (2002).  
3. Lloyd, S. Enhanced sensitivity of photodetection via quantum illumination. Science 321, 1463-1465 (2008).  
4. Ali-Khan, I., Broadbent, C. J. & Howell, J. C. Large-alphabet quantum key distribution using energy-time entangled bipartite states. Phys. Rev. Lett. 98, 060503 (2007).  
5. Neeley, M. et al. Emulation of a quantum spin with a superconducting phase qudit. Science 325, 722-725 (2009).  
6. Lanyon, B. P. et al. Simplifying quantum logic using higher-dimensional Hilbert spaces. Nat. Phys. 5, 134-140 (2009).  
7. Tanzilli, S. et al. On the genesis and evolution of integrated quantum optics. *Laser Photonics* Rev. 6, 115-143 (2012).  
8. Matsuda, N. et al. A monolithically integrated polarization entangled photon pair source on a silicon chip. Sci. Rep. 2, 817 (2012).  
9. Horn, R. T. et al. Inherent polarization entanglement generated from a monolithic semiconductor chip. Sci. Rep. 3, 2314 (2013).  
10. Silverstone, J. W. et al. Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat. Commun. 6, 7948 (2015).

11. Xiong, C. et al. Compact and reconfigurable silicon nitride time-bin entanglement circuit. Optica 2, 724-727 (2015).  
12. Simply silicon. Nat. Photon. 4, 491 (2010).  
13. Babinec, T. M. et al. A diamond nanowire single-photon source. Nat. Nanotechnol. 5, 195-199 (2010).  
14. Solntsev, A. S. & Sukhorukov, A. A. Path-entangled photon sources on nonlinear chips. Rev. Phys. 2, 19-31 (2016).  
15. Grassani, D. et al. Micrometer-scale integrated silicon source of time-energy entangled photons. Optica 2, 88-94 (2015).  
16. Zhang, Y. et al. Engineering two-photon high-dimensional states through quantum interference. Sci. Adv. 2, e1501165 (2016).  
17. Reimer, C. et al. Generation of multiphoton entangled quantum states by means of integrated frequency combs. Science 351, 1176-1180 (2016).  
18. Dada, A. C., Leach, J., Buller, G. S., Padgett, M. J. & Andersson, E. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nat. Phys. 7, 677-680 (2011).  
19. Howell, J. C., Bennink, R. S., Bentley, S. J. & Boyd, R. W. Realization of the Einstein-Podolsky-Rosen paradox using momentum and position-entangled photons from spontaneous parametric down conversion. Phys. Rev. Lett. 92, 210403 (2004).  
20. Schaeff, C. et al. Scalable fiber integrated source for higher-dimensional path-entangled photonic quNits. Opt. Express 20, 16145 (2012).  
21. Thew, R., Acin, A., Zbinden, H. & Gisin, N. Experimental realization of entangled qutrits for quantum communication. Quantum Inf. Comput. 4, 93 (2004).  
22. Olislager, L. et al. Frequency-bin entangled photons. Phys. Rev. A 82, 013804 (2010).  
23. Pe'er, A., Dayan, B., Friesem, A. A. & Silberberg, Y. Temporal shaping of entangled photons. Phys. Rev. Lett. 94, 073601 (2005).  
24. Bernhard, C., Bessire, B., Feurer, T. & Stefanov, A. Shaping frequency-entangled quids. Phys. Rev. A 88, 032322 (2013).  
25. Walmsley, I. A. & Raymer, M. G. Toward quantum-information processing with photons. Science 307, 1733-1734 (2005).  
26. Zhou, D., Zeng, B., Xu, Z. & Sun, C. Quantum computation based on  $d$ -level cluster state. Phys. Rev. A 68, 062303 (2003).  
27. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
28. Finot, C. Photonic waveform generator by linear shaping of four spectral sidebands. Opt. Lett. 40, 1422-1425 (2015).  
29. Barreiro, J. T., Meschede, D., Polzik, E., Arimondo, E. & Lugiato, L. Atoms, photons and entanglement for quantum information technologies. Procedia Comput. Sci. 7, 52-55 (2011).  
30. Lukens, J. M. & Lougovski, P. Frequency-encoded photonic qubits for scalable quantum information processing. Optica 4, 8-16 (2017).

Acknowledgements This work was supported by the Natural Sciences and Engineering Research Council of Canada (NSERC) through the Steacie, Strategic, Discovery and Acceleration Grants Schemes, by the MESI PSR-SIIRI Initiative in Quebec, by the Canada Research Chair Program and by the Australian Research Council Discovery Projects scheme (DP150104327). C.R. and P.R. acknowledge the support of NSERC Vanier Canada Graduate Scholarships. M.K. acknowledges funding from the European Union's Horizon 2020 Research and Innovation programme under the Marie Sklodowska-Curie grant agreement number 656607. S.T.C. acknowledges support from the CityU APRC programme number 9610356. B.E.L. acknowledges support from the Strategic Priority Research Program of the Chinese Academy of Sciences (grant number XDB24030300). B.W. acknowledges support from the People Programme (Marie Curie Actions) of the European Union's FP7 Programme under REA grant agreement INCIPIT (PIOF-GA-2013-625466). L.C. acknowledges support from the People Programme (Marie Curie Actions) of the European Union's FP7 Programme under REA Grant Agreement number 627478 (THREEPLE). R.M. acknowledges additional support by the Government of the Russian Federation through the ITMO Fellowship and Professorship Program (grant 074-U 01) and from the 1000 Talents Sichuan Program. We thank R. Helsten and M. Islam for technical insights; A. Tavares, T. Hansson and A. Bruhacs for discussions; T.A. Denidni and S.O. Tatu for lending us some of the required experimental equipment; P. Kung from QPS Photonics for help and the use of processing equipment; as well as Quantum Opus and N. Bertone of OptoElectronics Components for their support and for providing us with state-of-the-art photon detection equipment.

Author Contributions C.R. and M.K. developed the idea and contributed equally. C.R., M.K., P.R., L.R.C., B.W. and Y.Z. designed the experiment, performed the measurements and analysed the experimental results. S.S. and L.C. led the theoretical analysis. B.E.L. and S.T.C. designed and fabricated the integrated device. A.C. and D.J.M. participated in scientific discussions. R.M. and J.A. supervised and managed the project. All authors contributed to the writing of the manuscript.

Author Information Reprints and permissions information is available at www.nature.com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of the paper. Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. Correspondence and requests for materials should be addressed to M.K. (michael.kues@emt.inrs.ca) or R.M. (morandotti@emt.inrs.ca).

# METHODS

Experimental quantum state generation and control. We use an on-chip microring resonator fabricated from a high refractive index glass $^{17}$ , with a free spectral range of  $200\mathrm{GHz}$  and a  $Q$ -factor of 235,000. The input and output waveguides are featured with mode converters and are connected to polarization-maintaining fibres, resulting in coupling losses of  $<1.6\mathrm{dB}$  per facet $^{17}$ . In addition to the photonic chip, we used the following standard components, where all optical parts were connected using polarization-maintaining single-mode optical fibres: a mode-locked laser (PriTel), an electro-optic phase modulator (EO-Space), a radio-frequency signal generator (Agilent Technologies), programmable filters (Finisar Waveshaper), single photon detectors (Quantum Opus), and timing electronics (PicoQuant).

During our measurements, we ensured that the micro-ring excitation was stable, that is, it was showing power fluctuations of less than  $3\%$ . Furthermore, the electro-optical modulation (frequency shift and intensity distribution) and programmable optical filtering (applied spectral phase and attenuation) presented no measurable fluctuations. Our experimental implementation can be further optimized as follows. First, the losses can be reduced, which increases the measured coincidence-to-accidental ratio and thus the visibility of the quantum interference and the fidelity of the tomography measurements. Second, the quantum states themselves can be purified, that is, through quantum state distillation.

The total transmission loss of the coherent control setup amounted to  $14.5\mathrm{dB}$  (1 dB for the notch filter, 4.5 dB for the first programmable filter, 3.5 dB for the modulator, and 5.5 dB for the second programmable filter). These losses can be reduced through the use of integrated devices[12] (optical modulators, filters and phase controllers) and/or specially designed programmable filters, for example, based on combinations of fibre Bragg gratings and fibre-based phase shifters.

The nature of the SFWM process results in the generated states not having equal amplitudes over all frequency modes. This slight imbalance reduces the measured quantum interference visibility and state fidelity, as their determination is based on the assumption of maximally entangled states. By performing quantum state distillation $^{31}$ , these amplitudes can be made equal to maximize the entanglement. Frequency mixing using electro-optic phase modulation. The frequency mixing of the single-photon modes was performed by means of electro-optic phase modulation, driven by a single radio-frequency tone $^{32,33}$ . For the case of a single optical frequency mode input, phase modulation creates sidebands, the amplitudes and spectral spacing of which can be controlled via the modulation voltage and radio frequency, respectively. If an integer multiple of this sidebands spacing matches the FSR of the ring resonator, the mixing of optical signals in neighbouring resonances takes place. This process is governed by a linear, unitary and time-dependent operator, which has the following form in the time domain:

$$
H _ {t} = \mathrm {e} ^ {i V _ {\mathrm {m}} \kappa \sin (2 \pi \nu_ {\mathrm {m}} t + \phi_ {\mathrm {m}})}
$$

Here  $i$  is the imaginary unit,  $t$  represents time,  $V_{\mathrm{m}}$  is the voltage amplitude of the radio-frequency tone,  $\kappa$  is the electro-optical coefficient of the phase modulator,  $\nu_{\mathrm{m}}$  is the radio frequency, and  $\phi_{\mathrm{m}}$  is the initial phase. Owing to its intrinsic time-periodicity, this operator can be expressed in the form of an infinite trigonometric series:

$$
H _ {t} = \mathrm {e} ^ {i V _ {\mathrm {m}} \kappa \sin (2 \pi \nu_ {\mathrm {m}} t + \phi_ {\mathrm {m}})} = \sum_ {n = - \infty} ^ {\infty} a _ {n} \mathrm {e} ^ {i 2 n \pi \nu_ {\mathrm {m}} t}
$$

The sideband coefficient  $a_{n}$  is determined by the Jacobi-Anger expansion:

$$
a _ {n} = J _ {n} (V _ {\mathrm {m}} \kappa) e ^ {i n \phi_ {\mathrm {m}}}
$$

where  $J_{n}(V_{\mathrm{m}}\kappa)$  is the Bessel function of the first kind and of order  $n$ , evaluated at  $V_{\mathrm{m}}\kappa$ . The Bessel coefficients determine the sideband amplitudes, and thus for a given input optical signal, the phase-modulated output is described by a series of harmonic functions weighted by these coefficients. Each frequency mode is split into a series of modulation products (frequency modes), spectrally spaced by multiples of the driving frequency  $\nu_{\mathrm{m}}$ .

The advantage of this method is that the achievable modulation bandwidth is not only dependent on the driving frequency (as is the case for amplitude modulation), but also on the voltage  $V_{\mathrm{m}}$ . This means that a low-radio-frequency tone (low  $\nu_{\mathrm{m}}$ ) can generate modulation products at high frequencies, provided that a sufficiently high value of  $V_{\mathrm{m}}$  is supplied.

In our experiments,  $\mathrm{FSR} = 200\mathrm{GHz}$  and  $\nu_{\mathrm{m}}\approx 33.3\mathrm{GHz}$ . Using a sine-wave radio-frequency signal, we achieved, for the  $D = 2$  and  $D = 3$  cases,  $11\%$  power transfer to each of the  $\pm 200\mathrm{GHz}$  modes, while  $8\%$  of the power remained (unmodulated) in the fundamental frequency, leading to the mixing of a resonance mode with its two first-neighbours. For  $D = 4$ , we achieved a  $4\%$  power transfer to the  $\pm 100\mathrm{GHz}$  as well as  $\pm 300\mathrm{GHz}$  modulation sidebands, leading to

a mixing of four resonance modes in a vacuum mode; see Extended Data Fig. 2. The rest of the power was lost to other modulation sidebands, not required for the targeted mixing process. This loss and slight imbalance in the power distribution can be mitigated by using more complex modulation functions, for example, those produced by arbitrary waveform generators. Furthermore, by using higher-bandwidth electro-optic modulation schemes $^{34}$  or/and decreasing the micro-ring  $\mathrm{FSR}^{35,45}$ , it is possible to mix a larger number of frequency modes, which can also enable the direct interference of signal and idler photons.

Quantum mechanically, an operator that describes this process and which transforms the input into the output state is defined as<sup>36,37</sup>:

$$
A _ {\text {M o d}} ^ {\{s, i \}} = \sum_ {\bar {k} = 1} ^ {D} \sum_ {\bar {l} = 1} ^ {D} c _ {\{s, i \}, \bar {k} - \bar {l}} ^ {\text {M o d}} | \bar {l} \rangle \langle \bar {k} |
$$

for the signal (s) and idler (i) photons. The mixing coefficients are related to the sideband modulation terms by  $c_{\{\mathrm{s},\mathrm{i}\} ,x}^{\mathrm{Mod}} = a_{x\cdot P}$  where  $p$  is a natural number such that  $p\nu_{\mathrm{m}}$  matches the FSR of the ring resonator.

Schmidt mode decomposition. A frequency-entangled two-photon state can be described using its joint spectral amplitude $^{38}$ $F(\omega_{s}, \omega_{i})$ . The dimensionality of such an entangled state can be estimated by performing a Schmidt mode decomposition. In particular, the Schmidt number  $K$  represents the lowest amount of relevant orthogonal modes in the system $^{39}$  (defined as  $K = \left(\sum \lambda_{n}^{2}\right)^{-1}$ , where  $\lambda_{n}$  are the Schmidt eigenvalues with  $\sum \lambda_{n} = 1$ ). However, it is experimentally challenging to extract the joint spectral amplitude because the measurement requires the reconstruction of the state's full phase information. Instead, a lower bound for the Schmidt number can be experimentally determined by measuring the joint spectral intensity  $|F(\omega_{s}, \omega_{i})|^{2}$  of the two-photon state. The joint spectral intensity can be measured by performing spectrally resolved coincidence measurements, as shown in Fig. 2a. Even without the full phase information, the joint spectral intensity can be used to approximate the joint spectral amplitude as  $F(\omega_{s}, \omega_{i}) \approx \sqrt{|F(\omega_{s}, \omega_{i})|^{2}}$ . This assumption can in turn be used to determine the lower bound for the Schmidt number, by extracting the Schmidt eigenvalues  $\lambda_{n}$  using a singular value decomposition of  $\sqrt{|F(\omega_{s}, \omega_{i})|^{2}}$ , and calculating  $K = \left(\sum \lambda_{n}^{2}\right)^{-1}$ .

Time-domain mode measurements. The time-domain second-order coherence function of a state is directly correlated to the number of effective modes ( $N_{\mathrm{eff}}$ ) in the system<sup>40</sup>. Assuming that the amplitudes of these modes are equal, the maximum of the second-order coherence function is given by<sup>40</sup>  $g_{s,\mathrm{s}}^{(2)}(t = 0) = 1 + \frac{1}{N_{\mathrm{eff}}}$ . If a state is measured to have only a single mode ( $g_{s,\mathrm{s}}^{(2)} = 2$ ), the state is pure<sup>41</sup>. If both signal and idler are measured to be single mode, the joint two-photon state is fully separable and no entanglement is present<sup>41</sup>. The generation of pure states is intimately linked to the pump configuration used to excite the photon pairs<sup>42</sup>. In particular, if the excitation bandwidth is equal to the bandwidth of the signal and idler photons, such a desirable high-purity frequency state can be generated<sup>42</sup>. This condition can be achieved if the micro-ring resonator is pumped by means of a broadband pulsed laser, which is spectrally filtered to excite only a single resonance. Such a resonance acts as an additional spectral filter, ensuring that the input pulse matches the full resonance bandwidth, so that the effective frequency mode per signal/idler resonance is expected to approach one.

Quantum interference measurement. We performed Bell tests, that is, measurements that show the violation of classical inequalities. In the experiments presented here, we considered states with  $D = 2$ ,  $D = 3$  and  $D = 4$ . For a  $D$ -dimensional bipartite system, a Bell parameter  $I_{D}$  can be defined, where  $I_{D} > 2$  denotes entanglement<sup>2</sup>. The value of  $I_{D}$  can be extracted from the visibility associated with the quantum interference measurements, which can be obtained by projecting the states onto the vectors:

$$
\left| \Psi_ {\mathrm {p r o j}} \right\rangle = \frac {1}{D} \left(\sum_ {k = 0} ^ {D - 1} e ^ {i k \theta} | \bar {k} + k \rangle_ {\mathrm {s}}\right) \left(\sum_ {k = 0} ^ {D - 1} e ^ {i k \theta} | \bar {k} + k \rangle_ {\mathrm {i}}\right)
$$

for  $D = 2$ ,  $D = 3$  and  $D = 4$ . We implemented these projections by adjusting the first programmable filter and choosing the modulation frequency in such a way that the modes  $|k\rangle$ ,  $|k + 1\rangle$ ,  $|k + 2\rangle$  and  $|k + 3\rangle$  were mixed. This allowed us to measure:

$$
\left| \left\langle \Psi_ {\operatorname {p r o j}, D = 2} (\theta) \mid \psi_ {D = 2} \right\rangle \right| ^ {2}
$$

$$
\left| \left\langle \Psi_ {\operatorname {p r o j}, D = 3} (\theta) \mid \psi_ {D = 3} \right\rangle \right| ^ {2}
$$

$$
\left| \right.\left\langle \right. \Psi_ {\operatorname {p r o j}, D = 4} (\theta) \left. \right| \psi_ {D = 4} \left. \right\rangle\left. \right| ^ {2}
$$

The expected quantum interference signal takes the form:

$$
C _ {D = 2} (\theta) = 1 + \varepsilon_ {2} \cos (2 \theta)
$$

$$
C _ {D = 3} (\theta) = 3 + 2 \varepsilon_ {3} [ 2 \cos (2 \theta) + \cos (4 \theta) ]
$$

$$
C _ {D = 4} (\theta) = 4 + 2 \varepsilon_ {4} [ 3 \cos (2 \theta) + 2 \cos (4 \theta) + \cos (6 \theta) ]
$$

where  $\varepsilon_{D}$  (for  $D = 2,3$  or 4) emerges from a symmetric noise model, and describes the deviation from a pure, maximally entangled quantum state. This coefficient is related to the visibility through the expressions:

$$
V _ {2} = \varepsilon_ {2}
$$

$$
V _ {3} = \frac {3 \varepsilon_ {3}}{2 + \varepsilon_ {3}}
$$

$$
V _ {4} = \frac {4 \varepsilon_ {4}}{2 + 2 \varepsilon_ {4}}
$$

To achieve a violation of the Bell inequality, here expressed in terms of visibilities, the following relations must all be fulfilled<sup>2</sup>:

$$
\frac {1}{\sqrt {2}} \approx 0. 7 0 7 1 <   V _ {2}
$$

$$
\frac {3 (6 \sqrt {3} - 9)}{6 \sqrt {3} - 5} \approx 0. 7 7 4 6 <   V _ {3}
$$

$$
\frac {6}{3 + \sqrt {2} + \sqrt {1 0 - \sqrt {2}}} \approx 0. 8 1 7 0 <   V _ {4}
$$

Density matrix reconstruction. A very detailed and instructive summary of how to perform quantum state tomography on qubits has been presented by ref. 43, and then extended to quids $^{44}$ . In short, quantum state tomography is an experimental method that allows the extraction of the density matrix of a quantum state. For a given  $|\Psi \rangle$  the density matrix is defined as  $\rho = |\Psi \rangle \langle \Psi|$ . It is possible to reconstruct  $\rho$  by performing a series of measurements described via projection wavevectors  $|\Psi_{\nu}\rangle$ . The coincidence counts collected for each projection are given by:

$$
n _ {V} = C \langle \Psi_ {V} | \rho | \Psi_ {V} \rangle
$$

where  $C$  is a constant depending on the integration time. The measured density matrix can then be reconstructed using the relations:

$$
\rho = C ^ {- 1} \sum_ {v} M _ {v} n _ {v}
$$

$$
M _ {\nu} = \sum_ {x} \Gamma_ {x} (B ^ {- 1}) _ {x, \nu}
$$

$$
B _ {x, y} = \langle \Psi_ {x} | \Gamma_ {y} | \Psi_ {x} \rangle
$$

$$
C = \sum_ {k} n _ {k} \text {f o r} \operatorname {t r} \{M _ {k} \} = 1
$$

To deduce  $\rho$  from the measured values, a set of linearly independent and normalized matrices  $\Gamma$  is required. Any set of such matrices can be used as long as they fulfill the requirement $^{43}$ $\mathrm{tr}\{\Gamma_x\Gamma_y\} = \delta_{x,y}$ . The density matrix can then be extracted from any set of projection measurements that results in an invertible matrix  $B$ .

For the reconstruction of qubits  $(D = 2)$ , we chose the following projections for each photon:  $|\bar{k}\rangle$ ,  $|\bar{k} + 1\rangle$ ,  $\frac{1}{\sqrt{2}}\left(|\bar{k}\rangle + |\bar{k} + 1\rangle\right)$  and  $\frac{1}{\sqrt{2}}\left(|\bar{k}\rangle + i|\bar{k} + 1\rangle\right)$ , resulting in 16 different two-photon projection measurements. For the  $D = 3$  case, each photon has to be projected onto nine different vectors, and all 81 combinations have to be measured. We chose the following single photon projections:

$$
\frac {1}{\sqrt {2}} \left(| \bar {k} \rangle + | \bar {k} + 1 \rangle\right)
$$

$$
\frac {1}{\sqrt {2}} \left(| \bar {k} \rangle + | \bar {k} + 2 \rangle\right)
$$

$$
\frac {1}{\sqrt {2}} \left(| \bar {k} + 1 \rangle + | \bar {k} + 2 \rangle\right)
$$

$$
\left. \frac {1}{\sqrt {2}} \left(\mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} \rangle + \mathrm {e} ^ {- \frac {2 \pi}{3} i} | \bar {k} + 1 \rangle\right) \right.
$$

$$
\left. \frac {1}{\sqrt {2}} \left(\mathrm {e} ^ {- \frac {2 \pi}{3} i} | \bar {k} \rangle + \mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} + 1 \rangle\right) \right.
$$

$$
\begin{array}{l} \frac {1}{\sqrt {2}} \left(\mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} \rangle + \mathrm {e} ^ {- \frac {2 \pi}{3} i} | \bar {k} + 2 \rangle\right) \\ \frac {1}{\sqrt {2}} \left(\mathrm {e} ^ {- \frac {2 \pi}{3} i} | \bar {k} \rangle + \mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} + 2 \rangle\right) \\ \frac {1}{\sqrt {2}} \left(\mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} + 1 \rangle + \mathrm {e} ^ {- \frac {2 \pi}{3} i} | \bar {k} + 2 \rangle\right) \\ \frac {1}{\sqrt {2}} \left(\mathrm {e} ^ {- \frac {2 \pi}{3} i} | \bar {k} + 1 \rangle + \mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} + 2 \rangle\right) \\ \end{array}
$$

Finally, for the  $D = 4$  case, we chose the following:

$$
\begin{array}{l} \frac {1}{\sqrt {3}} \left(\left| \bar {k} + 1 \right\rangle + \left| \bar {k} + 2 \right\rangle + \left| \bar {k} + 3 \right\rangle\right) \\ \frac {1}{\sqrt {3}} \left(\left| \bar {k} + 1 \right\rangle + e ^ {\frac {2 \pi}{3} i} | \bar {k} + 2 \rangle + e ^ {- \frac {2 \pi}{3} i} | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(\left| \bar {k} + 1 \right\rangle + e ^ {- \frac {2 \pi}{3} i} \left| \bar {k} + 2 \right\rangle + e ^ {\frac {2 \pi}{3} i} \left| \bar {k} + 3 \right\rangle\right) \\ \frac {1}{\sqrt {3}} \left(\mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} + 1 \rangle + | \bar {k} + 2 \rangle + | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + | \bar {k} + 2 \rangle + | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + e ^ {\frac {2 \pi}{3} i} | \bar {k} + 2 \rangle + e ^ {- \frac {2 \pi}{3} i} | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + e ^ {- \frac {2 \pi}{3} i} | \bar {k} + 2 \rangle + e ^ {\frac {2 \pi}{3} i} | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + e ^ {\frac {2 \pi}{3} i} | \bar {k} + 2 \rangle + | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + | \bar {k} + 1 \rangle + | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + e ^ {\frac {2 \pi}{3} i} | \bar {k} + 1 \rangle + e ^ {- \frac {2 \pi}{3} i} | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + e ^ {- \frac {2 \pi}{3} i} | \bar {k} + 1 \rangle + e ^ {\frac {2 \pi}{3} i} | \bar {k} + 3 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(\left| \bar {k} \right\rangle + \left| \bar {k} + 1 \right\rangle + e ^ {\frac {2 \pi}{3} i} \left| \bar {k} + 3 \right\rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + | \bar {k} + 1 \rangle + | \bar {k} + 2 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(\left| \bar {k} \right\rangle + e ^ {\frac {2 \pi}{3} i} \left| \bar {k} + 1 \right\rangle + e ^ {- \frac {2 \pi}{3} i} \left| \bar {k} + 2 \right\rangle\right) \\ \frac {1}{\sqrt {3}} \left(| \bar {k} \rangle + e ^ {- \frac {2 \pi}{3} i} | \bar {k} + 1 \rangle + e ^ {\frac {2 \pi}{3} i} | \bar {k} + 2 \rangle\right) \\ \frac {1}{\sqrt {3}} \left(\mathrm {e} ^ {\frac {2 \pi}{3} i} | \bar {k} \rangle + | \bar {k} + 1 \rangle + | \bar {k} + 2 \rangle\right) \\ \end{array}
$$

A density matrix associated with a physical system has to be Hermitian and positive-definite; however, the matrix extracted from measurements usually does not comply with these requirements. To retrieve a meaningful  $\rho$ , we performed a maximum-likelihood estimation, which is a method used to find the physically realistic density matrix closest to the measured one[43].

The fidelity is a useful metric that can be extracted from the reconstructed density matrix, defined as the overlap between the ideal theoretical and measured  $\rho$ , and given by  $F = \mathrm{tr}\left(\left[\sqrt{\rho_{\mathrm{th}}}\rho_{\mathrm{exp}}\sqrt{\rho_{\mathrm{th}}}\right]^{1 / 2}\right)^{2}$ . A fidelity of one describes a perfect overlap with the ideal entangled state.

Frequency-entangled quantum state transmission over long fibre distances. To demonstrate that our approach is suitable for quantum communication, we sent the frequency-entangled states through  $20\mathrm{km}$  of standard single mode fibre (approximately  $4.5\mathrm{dB}$  loss) before being analysed by our coherent control setup (see Extended Data Fig. 1 for measured visibility). The chromatic fibre dispersion

caused a temporal walk-off of the frequency components  $(349\mathrm{ps}\mathrm{nm}^{-1}$  over the  $20\mathrm{km}$  propagation), as well as a constant phase shift among them. This shift does not degrade the quantum state, and can be compensated through phase modification by the first programmable filter. To achieve efficient frequency mixing, the temporal walk-off was corrected by adding  $4.2\mathrm{km}$  of dispersion-compensating fibre (3.6 dB loss,  $-350\mathrm{ps}\mathrm{nm}^{-1}$  at  $1,550\mathrm{nm}$ ).

Data availability. The raw data that support the findings of this study are available from the corresponding authors upon reasonable request.

31. Kwiat, P. G., Barraza-Lopez, S., Stefanov, A. & Gisin, N. Experimental entanglement distillation and 'hidden' non-locality. Nature 409, 1014-1017 (2001).  
32. Oppenheim, A. V. & Willsky, A. S. Signals and Systems (Prentice-Hall Signal Processing Series, 1997).  
33. Karpíński, M., Jachura, M., Wright, L. J. & Smith, B. J. Bandwidth manipulation of quantum light by an electro-optic time lens. Nat. Photon. 11, 53-57 (2017).  
34. Ishizawa, A. et al. Phase-noise characteristics of a 25-GHz-spaced optical frequency comb based on a phase- and intensity-modulated laser. Opt. Express 21, 29186-29194 (2013).  
35. Xuan, Y. et al. High-Q silicon nitride microresonators exhibiting low-power frequency comb initiation. Optica 3, 1171-1180 (2016).

36. Kumar, P. & Prabhakar, A. Evolution of quantum states in an electro-optic phase modulator. IEEE J. Quantum Electron. 45, 149-156 (2009).  
37. Capmany, J. & Fernandez-Pousa, C. R. Quantum model for electro-optical phase modulation. J. Opt. Soc. Am. B 27, A119-A129 (2010).  
38. Law, C. K., Walmsley, I. A. & Eberly, J. H. Continuous frequency entanglement: effective finite Hilbert space and entropy control. Phys. Rev. Lett. 84, 5304-5307 (2000).  
39. Fedorov, M. V. & Miklin, N. I. Schmidt modes and entanglement. Contemp. Phys. 55, 94-109 (2014).  
40. Christ, A., Laiho, K., Eckstein, A., Cassemiro, K. N. & Silberhorn, C. Probing multimode squeezing with correlation functions. New J. Phys. 13, 033027 (2011).  
41. Förtsch, M. et al. A versatile source of single photons for quantum information processing. Nat. Commun. 4, 1818 (2013).  
42. Helt, L. G., Yang, Z., Liscidini, M. & Sipe, J. E. Spontaneous four-wave mixing in microring resonators. Opt. Lett. 35, 3006-3008 (2010).  
43. James, D. F. V., Kwiat, P. G., Munro, W. J. & White, A. G. Measurement of qubits. Phys. Rev. A 64, 052312 (2001).  
44. Thew, R. T., Nemoto, K., White, A. G. & Munro, W. J. Qudit quantum-state tomography. Phys. Rev. A 66, 012303 (2002).  
45. Imany, P. et al. Demonstration of frequency-bin entanglement in an integrated optical microresonator. In Conf. on Lasers and Electro-Optics JTh5B.3 (OSA Technical Digest, Optical Society of America, 2017).

![](images/c1b6cadb35a94f4b54c355b6cbadebcb33f25afc77abd8b325445a5368b0ed1b.jpg)  
Extended Data Figure 1 | Bell inequality violation for frequency-entangled states after propagation through a  $24.2\mathrm{-km}$  fibre system. To show that frequency-entangled states can be used towards quantum communication schemes, we sent the signal and idler photon each through  $20\mathrm{km}$  of standard telecommunications fibre followed by a  $4.2\mathrm{-km}$ -long dispersion-compensating fibre. For  $D = 2$ , we measured (by tuning the relative phase  $\theta$  between each frequency bin of the signal and idler photon) a variation in coincidence counts (red crosses) with a quantum interference visibility  $V_{2}$  of  $79.8\%$  (violating a Bell inequality for  $D = 2$ ), thus demonstrating that entanglement was maintained over this distance (the black curve being the recorded background). Source Data for this figure is available online.

![](images/ed7a1e524d5c45a82b0e0bdd1c5d6d3ebbd4690cdcec1454d6be2967c85c6ca1.jpg)

![](images/67f5c0872435bbce81ac573297694790fdd740861202b00b578d7b934cf2f34c.jpg)

![](images/85ed7bf80b88ded8a58a2437c9087ea740e9505a1901227c6bfda971fcb878d3.jpg)  
Extended Data Figure 2 | Coherent mixing of multiple frequency modes.  $D$  modes (here,  $D = 2$ , 3 or 4) are spectrally selected (solid black line) (any mode  $\overline{k}$ ) and mixed (red arrows) by means of an electro-optic phase modulator. The frequency mode where all components overlap (red dashed line) is then selected via a narrow spectral filter (blue dashed window). For  $D = 2$  and 3, a frequency shift of  $200\mathrm{GHz}$  (equal to the FSR) is implemented, whereas for  $D = 4$  two different frequency shifts of  $100\mathrm{GHz}$  (equal to  $1/2$  FSR) and  $300\mathrm{GHz}$  (equal to  $3/2$  FSR) are enforced. In all cases, this is achieved through sideband generation. Note that for  $D = 4$ , and in contrast to  $D = 2$  and 3, the final frequency mode does not overlap with any microcavity resonance.