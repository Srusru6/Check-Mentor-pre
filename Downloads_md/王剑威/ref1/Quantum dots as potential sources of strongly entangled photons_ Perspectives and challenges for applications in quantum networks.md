PERSPECTIVE | MARCH 09 2021

# Quantum dots as potential sources of strongly entangled photons: Perspectives and challenges for applications in quantum networks

Christian Schimpf ; Marcus Reindl; Francesco Basso Basset ; Klaus D. Jons ; Rinaldo Trotta; Armando Rastelli

![](images/0c6a531484e3078ea2b76e748a4704aca12c4c311dd184ca66cd7656bc7bd83c.jpg)

Check for updates

Appl.Phys.Lett.118,100502 (2021)

https://doi.org/10.1063/5.0038729

![](images/e868ad0991f1b90b89e2ca8d8ed2efdbc1a5fcf86061b966b012eeae56fc7cb4.jpg)

View Online

![](images/8978f79c4542b61cd362773edff1d8aad87aa4624cf600e74f6cdbaf0a5d1613.jpg)

Export Citation

# Articles You May Be Interested In

Compact chirped fiber Bragg gratings for single-photon generation from quantum dots

APL Photonics (October 2023)

Rydberg superatoms: An artificial quantum system for quantum information processing and quantum optics

Appl. Phys. Rev. (August 2024)

Webinar From Noise to Knowledge

May 13th - Register now

![](images/bfabf8ae6aeae73b2b2d0c13c1928b84f7663a1a9b50c07be61e7b82a2a33dd0.jpg)

Zurich Instruments

Universität Konstanz

![](images/7185784f37ca61316e1b8f078b40fca1387e7e97bb79afa348bfb73270b2b97d.jpg)

![](images/6d3e32efb1f1e43f8eef1d7c176215f985b5382c1e863e4fe1ff99160a2868d2.jpg)

# Quantum dots as potential sources of strongly entangled photons: Perspectives and challenges for applications in quantum networks EP

Cite as: Appl. Phys. Lett. 118, 100502 (2021); doi: 10.1063/5.0038729

Submitted: 25 November 2020 · Accepted: 12 February 2021

Published Online: 9 March 2021

![](images/bc2a2fe3e12e4fce9f422866f020185d24138a16a685b8041adcae458c840d7c.jpg)  
View Online

![](images/079cbc11e2cacfcdd260066367a146a0fbbd0fc982c98d73b2af6166f1180e61.jpg)  
Export Citation

![](images/4da40fc7b1101ba7371b89e4994e9a20a2902ce133f47e2703b2cf03bb2275bf.jpg)  
CrossMark

Christian Schimpf, $^{1,a)}$  Marcus Reindl, $^{1}$  Francesco Basso Basset, $^{2}$  Klaus D. Jöns, $^{3}$  Rinaldo Trotta, $^{2}$  and Armando Rastelli $^{1}$

# AFFILIATIONS

$^{1}$ Institute of Semiconductor and Solid State Physics, Johannes Kepler University, Linz 4040, Austria  
$^{2}$ Department of Physics, Sapienza University of Rome, 00185 Rome, Italy  
<sup>3</sup>Department of Physics, Paderborn University, 33098 Paderborn, Germany  
$^{a)}$ Author to whom correspondence should be addressed: christian.schimpf@jku.at

# ABSTRACT

The generation and long-haul transmission of highly entangled photon pairs is a cornerstone of emerging photonic quantum technologies with key applications such as quantum key distribution and distributed quantum computing. However, a natural limit for the maximum transmission distance is inevitably set by attenuation in the medium. A network of quantum repeaters containing multiple sources of entangled photons would allow overcoming this limit. For this purpose, the requirements on the source's brightness and the photon pairs' degree of entanglement and indistinguishability are stringent. Despite the impressive progress made so far, a definitive scalable photon source fulfilling such requirements is still being sought after. Semiconductor quantum dots excel in this context as sub-Poissonian sources of polarization entangled photon pairs. In this work, we present the state-of-the-art set by GaAs based quantum dots and use them as a benchmark to discuss the challenges toward the realization of practical quantum networks.

© 2021 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1063/5.0038729

# I. INTRODUCTION

After decades of fundamental research, quantum entanglement emerged as a pivotal concept in a variety of fields, such as quantum computation, $^{1}$  -communication, $^{2-4}$  and -metrology. $^{5}$  A manifold of quantum systems are being investigated and photons stand out in many areas due to their robustness against environmental decoherence and their compatibility with existing optical fiber $^{6}$  and free-space $^{7}$  infrastructure. Non-local correlations were demonstrated in several photonic degrees of freedom such as time-bin, $^{8,9}$  time-energy, $^{10}$  orbital angular momentum, $^{11}$  polarization, $^{12}$  spin-polarization, $^{13,14}$  or in a combination of them ("hyper-entanglement" $^{15,16}$ ). In quantum information processing the manipulation and measurement of entangled qubits plays a major role. Applications like quantum key distribution (QKD) with entangled qubits $^{4,17,18}$  require high source brightness, high degree of entanglement, transmission through a low-noise quantum channel, and finally a straightforward measurement at remote communication partners, all with minimal losses. These prerequisites could be met by polarization entangled photon pairs. $^{19}$  Besides the

most prominent sources based on spontaneous parametric downconversion (SPDC),[20-22] semiconductor quantum dots  $(\mathrm{QDs})^{23-28}$  are also capable of generating polarization entangled photon pairs with a fidelity to a maximally entangled state above 0.97.[26] The probabilistic emission characteristics of SPDC sources prohibit so far a high brightness in combination with a high degree of entanglement.[29] This is not the case for QDs due to their sub-poissonian photon statistics.[30] Furthermore, in a real-world context, applications like QKD require entanglement to be communicated over large distances[6,7] to be practically relevant. Most transmission channels, like optical fibers, underlie damping, which severely limits the transmission range. This limitation can be alleviated by exploiting a concept of quantum communication:[2] The interconnection of multiple light sources in quantum networks[2,3] via the realization of a cascaded quantum repeater scheme with entangled photons and quantum memories.[3,31,32] In order to reach this goal, properties of the photon sources beyond the maximum entanglement fidelity become relevant, such as the photon

indistinguishability. $^{33}$  In this work, we examine the key figures of merit of entangled photon pairs with an emphasis on the distribution of entanglement in a quantum network. We will start from the state-of-the-art focusing on GaAs QDs. Although the emission wavelength of about  $785\mathrm{nm}$  is currently non-ideal for efficient fiber-based applications, GaAs QDs represent an excellent model system for the here discussed ideas due to their performance. All of the general concepts introduced in the following, however, are also valid for different material systems, such as InGaAs QDs, $^{23,34-37}$  whose emission wavelength can be extended to the telecom C-band, where the attenuation in silica fibers has a minimum. In the final section, we will outline recent approaches toward the realization of a viable quantum network.

# II. POLARIZATION ENTANGLED PHOTON PAIRS FROM QUANTUM DOTS

A common scheme to generate entangled photon pairs with semiconductor QDs embedded in photonic structures [see Fig. 1(a)] is by resonantly populating the biexciton (XX) state by a two-photon excitation (TPE) process.[38] The XX radiatively decays via the biexciton-exciton(X)-ground state cascade,[39] as depicted in Fig. 1(b). Ideally, the emitted photon pairs are in the maximum entangled Bell state  $|\phi^{+}\rangle = 1 / \sqrt{2}(|HH\rangle + |VV\rangle)$ , with  $|H\rangle$  and  $|V\rangle$  being the horizontal and vertical polarization basis states, respectively. The fidelity  $f_{|\phi^{+}\rangle}$  of the real photon pair's state to  $|\phi^{+}\rangle$  is mostly determined by the fine structure splitting (FSS)  $S$  and lifetime  $T_{1,X}$  of the intermediate X state. In the absence of other dephasing mechanisms, the maximum achievable fidelity of an ensemble of photon pairs to a maximum entangled state is given by[40]

$$
f _ {| \phi^ {+} \rangle} ^ {\max } = \frac {1}{4} \left(2 - g _ {0} ^ {(2)} + \frac {2 \left(1 - g _ {0} ^ {(2)}\right)}{\sqrt {1 + \left(S T _ {1 , X} / \hbar\right) ^ {2}}}\right), \tag {1}
$$

where  $g_{0}^{(2)}$  is the multi-photon emission probability. In the case of GaAs QDs obtained by the Al droplet etching technique,[24] a high in-plane symmetry[25] results in average FSS values below  $5\mu \mathrm{eV}$ , while the weak lateral carrier confinement[41] causes radiative lifetimes of about  $T_{1,\mathrm{XX}} = 120~\mathrm{ps}$  and  $T_{1,\mathrm{X}} = 270~\mathrm{ps}$ . The wavelength of the emitted light hereby lies around  $780\mathrm{nm}$  [see Fig. 1(c)], with the XX and X photons separated by about  $2\mathrm{nm}$  (4 meV), allowing them to be split by color. In contrast to SPDC-based sources,[42] the pair-generation probability and the  $g_{0}^{(2)}$  of QDs are decoupled due to the subpoissonian emission characteristics.[39] This led to demonstrated values of  $g_{0}^{(2)} = 7.5(16)\times 10^{-5}$  under pulsed TPE,[30] as illustrated by the corresponding auto-correlation measurement in Fig. 1(d). Figure 1(e) displays a resulting two-photon density matrix  $\rho$  in the polarization space of the XX and X photons for an as-grown GaAs QD with  $S\approx 0.4\mu \mathrm{eV}$ , acquired by full-state tomography[43] under pulsed TPE at an excitation rate of  $R = 80\mathrm{MHz}$ . The fidelity deduced from this matrix as  $f_{|\phi^{+}\rangle} = \langle \phi^{+}|\rho |\phi^{+}\rangle$  is 0.97(1). By utilizing a specifically designed piezo-electric actuator,[44] capable of restoring the in-plane symmetry and erasing the FSS of the QDs by strain, fidelity values up to 0.978(5) were demonstrated.[26] These results suggest that a modest Purcell enhancement of a factor 3 could alleviate remaining dephasing effects and push the fidelity up to 0.99, which would match with the best results from SPDC sources.[45] The minimum time delay  $1 / R$  between the pulses depends on the lifetimes  $T_{1,\mathrm{XX}}$  and  $T_{1,\mathrm{X}}$ , allowing for excitation rates up to  $R\approx 1\mathrm{GHz}$  (without Purcell enhancement). This makes GaAs QDs a viable source for applications like QKD with

![](images/53a9d6c91d3020feb099ffee90edfc4c44fbe183b2ab36607663db71f904bd85.jpg)

![](images/7a15eed9617b6b9a010072e126528068c1642443968884d96d07fd72ef8694b9.jpg)

![](images/2ab1af57cff438602d28ced68a1d8cb1772ed1b5d1d061f1d9a42a0de4762ef5.jpg)

![](images/059ccf2a4c3b7eba314858a3f70aeb791b29b406e05c2dd7c5a463f92cdf3f65.jpg)

![](images/d582521aa98707c420fe49a5ec3c82a200fb016ef28c6c15bbea73c41f2d501c.jpg)  
FIG. 1. Compilation of measurements for GaAs QDs. (a) Common sample structure with GaAs QDs in a lambda-cavity sandwiched between distributed Bragg reflectors (DBRs). In combination with a solid immersion lens (SIL), this yields an extraction efficiency of about 0.11. (b) Scheme of entangled photon pair generation using the resonant two-photon excitation (TPE) process. (c) Emission spectrum of under TPE. (d) Autocorrelation of the XX signal from a GaAs QD excited by TPE and measured by superconducting nanowire single photon detectors (SNSPDs), with a resulting  $g^{(2)}(0) = 7.5(16)\times 10^{-5}$ . Reproduced with permission from Schweickert et al., Appl. Phys. Lett. 112, 093106 (2018), Copyright 2018 AIP Publishing. (e) Real and imaginary part of the two-qubit density matrix of the X and XX in the horizontal (H) and vertical (V) polarization basis. The derived fidelity is  $f_{|\phi^{+}} = 0.97(1)$ . (f) Two-photon interference visibility from one doubly excited QD with a time delay of 2 ns. (g) Two-photon interference visibility for two remote QDs with a resulting interference visibility of  $V = 0.51(5)$ . Reproduced with permission from Reindl et al., Nano Lett. 17, 4090-4095 (2017). Copyright 2017 Authors, licensed under a Creative Commons Attribution (CC BY) license.

![](images/eba43ae90d406f17d59b4c939b650b616bd2ecb90a0fe3f978005694c8a0921d.jpg)

![](images/d598ba91eba876f7e996827e00b242dea921453ea959bfe953236d2b67a1b386.jpg)

![](images/db9c436062f9a35cd2f5ed24c47f26e6ab9a8e37bf5fc4a8688de00dfe517273.jpg)

entangled photons, $^{4,17,18,46}$  where near-unity entanglement fidelity is required in order to reach practical secure key rates. In the case of the widely used InGaAs QDs, presumably the intrinsically longer transition lifetimes currently prevent similarly high degree of entanglement in the absence of time filtering. $^{6,47}$

The source brightness of QDs is mostly bound to the extraction efficiency, which is naturally limited in semiconductor structures due to total internal reflection at the air/semiconductor interface. A simple approach to increase the pair extraction efficiency  $\eta_{E}^{(2)}$  from less than  $10^{-4}$  to about 0.01 is to embed the QDs in a lambda cavity defined between two distributed Bragg reflectors and adding a solid immersion lens on top,[48] see Fig. 1(a). A pair extraction efficiency of 0.373(2) has been recently reported for GaAs QDs embedded in antenna structures consisting of a semiconductor membrane with a back metal mirror and a top solid immersion lens made of GaP.[49] Recently, circular Bragg resonators (CBRs) have demonstrated values of  $\eta_{E}^{(2)} = 0.65(4)^{50}$  and Purcell enhancement up to a factor 11.3.[51] Although a non-ideal entanglement fidelity due to the high FSS was reported in Ref. 50, these structures are compatible with the aforementioned strain tuning techniques, which could cancel the FSS to create a bright source of highly entangled photon pairs, applicable for QKD with key rates potentially in the GHz range.

A widely discussed and researched topic is the distribution of entanglement over basically arbitrary distances, for which sources operating at high pair emission rates are especially relevant. One approach is free-space transmission via satellites, where recently a distance of  $1120\mathrm{km}$  was covered.

From the practical point of view, it would be desirable to exploit the existing and well-established telecom optical fiber networks. The obvious effect of fibers on the transmitted light is a uniform damping, which is about  $0.2\mathrm{dB / km}$  for typical fibers in the telecom C-Band at a wavelength of  $1550\mathrm{nm}$  wavelength (compared to about  $2.5\mathrm{dB / km}$  for  $785\mathrm{nm}$ ). When transmitting polarization entangled photons through optical fibers, however, also polarization mode dispersion (PMD) has to be taken into account. PMD causes the principal states of polarization (PSPs) of the photons' wave packets to drift apart in time, leading to a degradation of the entanglement. The latter is proportional to the ratio of the total induced PMD  $\tau$  between the two entangled photons and the length of the photon wave packets, given by  $2T_{1}$ . The maximum achievable fidelity to a perfectly entangled state, derived from the 2-qubit density matrix in polarization space, is then given by

$$
f _ {\mathrm {P M D}} (\tau) = \frac {1}{2} + \left(\frac {1}{2} + \frac {\tau}{4 T _ {1}}\right) e ^ {\frac {- \tau}{2 T _ {1}}}. \tag {2}
$$

For simplicity, we assume that  $T_{1} = \min (T_{1,\mathrm{X}}, T_{1,\mathrm{XX}})$ , which represents a worst case scenario. If the two entangled photons experience exactly the opposite relative drift due to a maximum mismatch of the input modes with the PSPs, the PMD from the individual fibers add up to  $\tau = \tau_{1} + \tau_{2}$ . A typical value for the PMD of a single mode fiber is  $D = 0.1\mathrm{ps} / \sqrt{\mathrm{km}}$  (e.g., the type "SMF-28e+" from "Corning"), thus with the given lifetimes and a length of  $l = 200\mathrm{km}$  for both the X and the XX photon's fibers, the maximum possible fidelity for  $T_{1} = 120\mathrm{ps}$  is still  $f_{\mathrm{PMD}}(2D\sqrt{l}) > 0.99$ . For  $T_{1} = 10\mathrm{ps}$ , the  $f_{\mathrm{PMD}}$  degrades to about 0.98. For  $T_{1} = 1\mathrm{ps}$ , which is approximately the case for sources based on the SPDC process, the maximum fidelity drops to

about 0.79, unless resorting to lossy measures like frequency filtering $^{53}$  or conversion to time-bin entanglement. $^{9,54}$  If the input polarization modes are aligned with the PSPs, the total PMD reads  $\tau = \tau_{1} - \tau_{2}$ . Therefore, given that  $\tau_{1} = \tau_{2}$ , a configuration exists which exactly cancels out the effect of PMD and preserves the entanglement. This could be achieved by realigning the input modes to the PSPs during operation by polarization controllers. $^{55}$  An additional effect besides PMD in the context of a fiber-based network is chromatic dispersion, which leads to a temporal broadening of the wavefunctions. $^{35,56}$  This lowers the success probability of two-photon interference, but can be countered by the design of the optical setup, as we will discuss in Sec. III.

From these considerations, we realize that fiber-based networks with QDs can greatly benefit from the robustness against PMD, especially compared to SPDC sources. However, for emission wavelengths significantly below the telecom bands, as in the case of GaAs QDs and most used InGaAs QDs coherently grown on GaAs substrates, the range remains severely limited. For this purpose, different material systems for QDs emitting in the telecom bands are being developed. An entanglement distribution experiment with an InGaAs QD emitting in the telecom O-band over a distance of about  $18\mathrm{km}$  has already been demonstrated,[6] while the quality of QDs emitting in the telecom C-band is rapidly approaching that of dots emitting at shorter wavelengths.[34,37,57] As an alternative, frequency conversion techniques can be utilized to adapt the emission wavelengths, although at the cost of efficiency.[35]

# III. QUANTUM DOTS IN A QUANTUM REPEATER BASED NETWORK

Although transport of highly polarization entangled photons through fibers is possible,[58] the exponential damping will inevitably lead to an insufficient qubit rate. A possible solution to this problem is the realization of a quantum repeater scheme. The commonly proposed approach is based on the DLCZ protocol (and its variants) that relies on spin-photon entanglement.[59] However, the probabilistic nature of the entangling scheme limits the entanglement creation.[60] Although an improved, deterministic version of the spin-photon based scheme was developed,[61] the achieved rates are still modest. An alternative scheme relies on the use of entangled photon pair sources, like QDs, interfaced with quantum memories capable of receiving and storing entangled states to increase the qubit rate.[32] This scheme relies on a cascade of entanglement swapping processes[62,63] among entangled photon pairs emitted by independent emitters. The teleportation of the entanglement is enabled by two-photon interference to perform a so-called Bell state measurement (BSM). The success of a BSM strongly depends on the photon indistinguishability, which, in turn, depends on the photon sources and can be experimentally accessed by probing the interference visibility in a Hong-Ou-Mandel (HOM) experiment.[56] For maximum visibility, the spatiotemporal wave packets of the two photons involved in the BSM have to be identical and pure, i.e., no other physical system should contain information about the photon's origin. The latter point plays a crucial role in the case of QDs exploiting the decay cascade for entangled photon generation. The XX and X photons are correlated in their decay times,[8,64,65] which limits the maximum possible indistinguishability for both the XX and X photons according to[65]

$$
V _ {\text {c a s c}} = \frac {1}{1 + T _ {1 , \mathrm {X X}} / T _ {1 , \mathrm {X}}}. \tag {3}
$$

Figure 1(f) shows the result of a HOM experiment with two XX photons generated by a GaAs QD, upon excitation with two pulses separated by a 2 ns delay. The resulting visibility of 0.69 is typical for both the XX and X photons under TPE $^{48}$  and is close to the maximum according to Eq. (3). As a comparison: For single X photons generated by resonant excitation, a visibility of over 0.9 is achieved for the same QDs. $^{65}$  When interfacing two dissimilar QDs, the inherently stochastic nature of the epitaxial growth has to be considered, which primarily leads to varying emission energies. Further, imperfections in the solid-state environment of the QDs lead to inhomogeneous broadening due to charge noise. $^{66}$  This results in a jitter of the central emission energy by  $\delta E$  (full width at half maximum) around a mean value typically in the microsecond to millisecond timescale. $^{66}$  The jitter leads to a degradation of the indistinguishability described by $^{67}$

$$
V _ {\delta E} = \frac {\hbar \operatorname {R e} [ \mathrm {F} (z) ]}{\sqrt {8 \pi} \sigma T _ {1}}, \tag {4}
$$

with  $\sigma = \delta E / 2\sqrt{2\ln 2}$  being the standard deviation of the Gaussian distribution of the energy jitter and  $\mathrm{Re}[\mathrm{F}(z)]$  being the real part of the Faddeeva function of  $z = i\hbar /\left(2\pi \sqrt{2}\sigma T_1\right)$ . Although measurements

under resonant single-photon excitation reveal that pure dephasing is not fully negligible,[65] we focus here on the far more dominant energy jitter and do not include pure dephasing in Eq. (4). Figure 1(g) shows the result of a HOM experiment with two X photons from GaAs QDs with  $\delta E \approx 4\mu \mathrm{eV}$  and a resulting visibility of  $V = 0.51(5)$ ,[68] which corresponds, to our knowledge, to the maximum value measured so far for QDs initially prepared into the biexciton state (via phonon-assisted TPE). The center wavelengths were previously matched by tuning the energy of one QD via a monolithic piezo-electric actuator.

We will now discuss possible solutions to overcome the two major indistinguishability degrading mechanisms in QDs discussed so far: The partial temporal entanglement in the XX-X decay cascade [Eq. (3)] and frequency jitter [Eq. (4)]. Both effects are influenced by the radiative lifetimes  $T_{1,\mathrm{XX}}$  and  $T_{1,\mathrm{X}}$ , which can be modified by exploiting the Purcell effect in a cavity.[50,51] Figure 2 illustrates concatenated entanglement swapping processes with a depth of  $L = \{1,2,3\}$ , i.e., a chain of quantum relays forming the backbone of quantum repeaters. The number of QDs required is  $2^{L}$ , while the range covered scales with  $2^{L}l_{0}$ , with  $l_{0}$  being the total length of both fibers departing from one QD. This example serves as a demonstration on how the entanglement fidelity evolves over multiple layers of swapping operations with photons generated by QDs. Figure 2(a) depicts the final entanglement fidelity as a function of the Purcell factor  $P$  and

![](images/1855c684d075937724aa8ae780ac48b6607090e11572c74bea1324ce878dde8c.jpg)  
FIG. 2. Entanglement fidelity in a chain of quantum relays. Simulated entanglement fidelity of the final entangled photon pair in a chain of quantum relays performing entanglement swapping operations among pairs of polarization entangled photons emitted by QDs under TPE. The chain depths are  $L = \{1,2,3\}$ . All QDs are assumed to have an FSS of  $0.05\mu \mathrm{eV}$ . (a) Fidelity as a function of Purcell factor  $P$  and Gaussian energy jitter  $\delta E$  in multiples of the natural  $X$  linewidth of  $\delta E_0 = 2.4\mu \mathrm{eV}$  at  $P = 1$ . (b) Fidelity with a frequency selective cavity, so that  $P_{X} = P$  and  $P_{XX} = 7P$ . (c) Fidelity as a function of the Lorentzian width of a frequency filter  $\delta E_f$  and the Gaussian energy jitter  $\delta E$  (full width at half maximum), for fixed Purcell factors of  $P_{X} = 2$  and  $P_{XX} = 10$ .

the energy jitter  $\delta E$  in multiples of the natural X linewidth of  $\delta E_0 = 2.4\mu \mathrm{eV}$  at  $P = 1$ , corresponding to  $T_{1,\mathrm{X}} = 270$  ps. Values of  $P > 15$  are unpractical, as the total relaxation time of the QD then approaches the typical excitation pulse width of about 10 ps. This primarily leads to an increasing re-excitation probability,[69,70] which is detrimental to the indistinguishability and the entanglement. In addition, PMD effects in optical fibers start to become relevant for such short wave packets. For the calculation of the fidelity, we utilize the density matrix formalism for describing one entanglement swapping process with QDs[63] with a type of BSM which can detect two Bell states[40,71] ( $|\psi^{+}\rangle$  and  $|\psi^{-}\rangle$ ). In order to model a chain of entanglement swapping processes, the formalism is applied recursively, assuming uncorrelated BSM success probabilities in successive steps. We simultaneously account for varying lifetimes caused by  $P$  and a decreased BSM success rate due to  $\delta E$  (see the supplementary material for details). From the simulations, we observe that already for two swapping processes the homogeneous Purcell enhancement alone cannot recover the entanglement fidelity sufficiently, as it merely alleviates the impact from inhomogeneous broadening on the indistinguishability, but the visibility degrading effect from the XX-X cascade is still at full force. Figure 2(b) depicts the case for an energy selective cavity,[64] which enhances the XX decay rate by a factor of 7 compared to the X, so that  $P_{X} = P$  and  $P_{XX} = 7P$ . This approach could strongly increase the BSM success rate and therefore the resulting entanglement fidelity. However, the finite temporal width of the excitation pulse, whose minimum value is set by the limited spectral separation between X and XX and the necessity of suppressing laser stray light, sets a lower limit to the lifetimes—and therefore an upper limit to the Purcell enhancement—in order to limit re-excitation.[69] A compromise could be achieved by mild frequency filtering of the X photon, as illustrated in Fig. 2(c). Filtering partially erases the temporal information held by the X photon, leading to the same outcome as prolonging the X lifetime and hence decreasing the XX/X lifetime ratio as with the selective Purcell enhancement. In the simulations, we assume a filter with Lorentzian transmission characteristics and a FWHM of  $\delta E_f$  and an energy jitter with a FWHM of  $\delta E$  for both the X and the XX (see the supplementary material for details). We assume a frequency selective cavity with fixed Purcell enhancement of  $P_{\mathrm{X}} = 2$  and  $P_{\mathrm{XX}} = 10$ . This asymmetry in enhancement could be achieved by carefully designing the lateral size of the previously introduced CBRs.[50] As a result of the filtering, the effective lifetime of the X signal increases while simultaneously reducing the impact of the energy jitter. Note that for the here investigated values of  $\delta E$  the interference visibility again drops for  $\delta E_f$  values below the inhomogeneous broadening  $\delta E$ . In addition, in the presence of a finite FSS, the BSM success rate drops when the filtered linewidth is on the order of the FSS or below.[63] From the simulations, we can observe that with a low inhomogeneous broadening ( $< 0.1\delta E_0$ ) and a moderate frequency filtering of about  $1.5\delta E_0$  one could achieve an entanglement fidelity of approximately 0.93 at  $L = 2$  and 0.85 at  $L = 3$ .

A complete repeater scheme requires also quantum memories,[72] which can store and retrieve a photonic qubit with high fidelity. To address the noise and bandwidth limitation of quantum memories, two groups invented a cascaded absorption memory scheme, which is intrinsically noise-free.[73,74] Furthermore, the possibility to use an off-resonant Raman transition in this cascaded scheme allows for large storage bandwidth, limited mainly by the available control laser power. Currently, the main drawback of these schemes is the limited storage

time, which is determined by the radiative lifetime of the upper state of the cascade (below 100 ns). Another promising approach is to use rare-earth doped crystals as quantum memories,[75] featuring performances that equalize, if not outperform, those of cold atomic ensembles[76,77] or trapped emitters in terms of efficiency[78] and coherence times.[79] These memories have shown a full quantum storage protocol with telecom-heralded quantum states of light,[80] and the first photonic quantum state transfer between nodes of different nature.[81] Furthermore, atomic frequency comb quantum memories were the first to be successfully interfaced with single photons emitted from a quantum dot.[82]

We want to mention at this point that recently an alternative repeater scheme $^{83}$  was proposed, which eliminates the necessity of quantum memories, but instead shifts the challenge toward the realization of large-scale photonic cluster states.

# IV. FUTURE OUTLOOK

We conclude that bright and nearly on-demand sources of highly entangled photon pairs are on the verge of becoming reality. The ground work has been laid through the development of semiconductor quantum dots (QDs) emitting highly entangled photons,[26] of advanced optical cavity structures[50,51] and technology capable of manipulating the symmetry and emission energy of QDs.[44] On-chip integration of QDs[84] and the implementation of electric excitation schemes[85] can further increase the practicability in emerging quantum technology.

The optimal wavelength (about  $1550\mathrm{nm}$ ) for transporting entangled photons through fibers is currently determined by the established telecom fiber infrastructure. Material systems to obtain QDs emitting at this wavelength are under development,[6,34,37,57] and existing sources with emission at shorter wavelengths could be adapted by frequency conversion.[35] Recently, a basic GHz-clocked quantum relay with QDs emitting directly in the Telecom-C band was demonstrated.[86] One of the greatest, yet rewarding challenges is the interfacing of dissimilar sources of entangled photons for multi-photon applications[36] and long-haul entanglement distribution[6,7] in quantum networks.[2,3] The physical limits to the indistinguishability[8,65] set by the currently employed cascade for entangled photon pair generation[26,39] and fluctuations stemming from the solid state environment of QDs[25,66] pose intricate challenges for the years to come. As demonstrated in this work, the application of selective Purcell enhancement together with mild frequency filtering could alleviate the limit of indistinguishability of the entangled photon pairs. The different emission energies and radiative lifetimes of the biexciton (XX) or exciton (X) in QDs could be matched by utilizing strain[44] and electric[87] degrees of freedom independently. Considering the quantum relay chains depicted in Fig. 2, three strain degrees of freedom can cancel the fine structure splitting (FSS) and adapt the central energy of the XX or X to the next neighbor's. The electric degree of freedom can simultaneously be used to fine-tune the respective radiative lifetime and therefore the shape of the photonic wave-packet. By repeating this strategy through the whole relay chain for each QD, one could optimize the resulting entanglement fidelity of the final photon pair.

With these tools at hand, the next leap toward the demonstration of a functional quantum network will be the interconnection of two

dissimilar quantum dots via entanglement swapping.[62,63] Several groups are currently developing devices which merge the concepts of circular Bragg reflectors (CBRs)[50,51] with the tuning of the in-plane stress tensors[44] of the QDs. CBRs are ideally suited for this purpose, since they are fabricated on a dielectric-metal structure which can be virtually placed on any other substrate, and in particular, on piezoelectric actuators. By carefully designing the dimensions of the CBRs, these devices could provide the necessary magnitude and asymmetry of the Purcell factors for the XX and the X emission for a high photon indistinguishability, while eliminating remaining FSS and matching the energies of the involved QD's photons via the three strain degrees of freedom. These concepts are compatible with alternative material systems emitting at telecom wavelength,[6,34,37,57] which will allow to reach longer distances with optical fibers and possibly to utilize the established telecom fiber network. The next steps could be to interface the photons performing the Bell state measurement with quantum memories[72,73,75,78-82] and use the resulting entangled photon pairs for quantum key distribution[4,17,18] with efficiencies beating the direct transmission through fibers. From there on, the goal is to expand the system to a chain of multiple QDs and implement a quantum repeater scheme[3,31,32] in order to enhance the resulting entanglement fidelity and efficiency compared to a repeater-less distribution scheme.

# SUPPLEMENTARY MATERIAL

See the supplementary material for theoretical considerations about the evolution of entangled states in a chain of quantum relays.

# ACKNOWLEDGMENTS

Christian Schimpf is a recipient of a DOC Fellowship of the Austrian Academy of Sciences at the Institute of Semiconductor Physics at Johannes Kepler University, Linz, Austria. This project has received funding from the Austrian Science Fund (FWF): FG 5, P 29603, P 30459, I 4380, I 4320, and I 3762, the Linz Institute of Technology (LIT) and the LIT Secure and Correct Systems Lab funded by the state of Upper Austria and the European Union's Horizon 2020 research and innovation program under Grant Agreement Nos. 820423 (S2QUIP), 899814 (Qurope), 871130 (ASCENT+), and 679183 (SQPRel).

# DATA AVAILABILITY

Data sharing is not applicable to this article as no new data were created or analyzed in this study.

# REFERENCES

$^{1}$ J. L. O'Brien, A. Furusawa, and J. Vuckovic, "Photonic quantum technologies," Nat. Photonics 3, 687-695 (2009).  
$^{2}$ N. Gisin and R. Thew, “Quantum Communication,” Nat. Photonics 1, 165-171 (2007).  
$^{3}$ H. J. Kimble, "The quantum internet," Nature 453, 1023-1030 (2008).  
4A. K. Ekert, "Quantum cryptography based on Bell's theorem," Phys. Rev. Lett. 67, 661-663 (1991).  
5C. L. Degen, F. Reinhard, and P. Cappellaro, "Quantum sensing," Rev. Mod. Phys. 89, 035002 (2017).  
$^{6}$ Z. H. Xiang, J. Huwer, R. M. Stevenson, J. Skiba-Szymanska, M. B. Ward, I. Farrer, D. A. Ritchie, and A. J. Shields, "Long-term transmission of entangled photons from a single quantum dot over deployed fiber," Sci. Rep. 9, 4111 (2019).

7J. Yin, Y.-H. Li, S.-K. Liao, M. Yang, Y. Cao, L. Zhang, J.-G. Ren, W.-Q. Cai, W.-Y. Liu, S.-L. Li, R. Shu, Y.-M. Huang, L. Deng, L. Li, Q. Zhang, N.-L. Liu, Y.-A. Chen, C.-Y. Lu, X.-B. Wang, F. Xu, J.-Y. Wang, C.-Z. Peng, A. K. Ekert, and J.-W. Pan, "Entanglement-based secure quantum cryptography over 1,120 kilometres," Nature 582, 501 (2020).  
8C. Simon and J. P. Poizat, "Creating single time-bin-entangled photon pairs," Phys. Rev. Lett. 94, 030502 (2005).  
$^{9}$ H. Jayakumar, A. Predojevic, T. Kauten, T. Huber, G. S. Solomon, and G. Weihs, "Time-bin entangled photons from a quantum dot," Nat. Commun. 5, 4251 (2014).  
10S. Tanzilli, W. Tittel, M. Halder, O. Alibart, P. Baldi, N. Gisin, and H. Zbinden, "A photonic quantum information interface," Nature 437, 116-120 (2005).  
A. Mair, A. Vaziri, G. Weihs, and A. Zeilinger, "Entanglement of the orbital angular momentum states of photons," Nature 412, 313-316 (2001).  
12 A. Aspect, P. Grangier, and G. Roger, "Experimental tests of realistic local theories via Bell's theorem," Phys. Rev. Lett. 47, 460-463 (1981).  
13 M. Bock, P. Eich, S. Kucera, M. Kreis, A. Lenhard, C. Becher, and J. Eschner, "High-fidelity entanglement between a trapped ion and a telecom photon via quantum frequency conversion," Nat. Commun. 9, 1998 (2018).  
14 R. Vasconcelos, S. Reisenbauer, C. Salter, G. Wachter, D. Wirtitsch, J. Schmiedmayer, P. Walther, and M. Trupke, "Scalable spin-photon entanglement by time-to-polarization conversion," NPJ Quantum Inf. 6, 9 (2020).  
15P. G. Kwiat, "Hyper-entangled states," J. Mod. Opt. 44, 2173-2184 (1997).  
16 M. Prilmüller, T. Huber, M. Müller, P. Michler, G. Weihs, and A. Predojevic, "Hyperentanglement of photons emitted by a quantum dot," Phys. Rev. Lett. 121, 110503 (2018).  
17C. H. Bennett, G. Brassard, and N. D. Mermin, "Quantum cryptography without Bell's theorem," Phys. Rev. Lett. 68, 557-559 (1992).  
18 A. Acín, N. Brunner, N. Gisin, S. Massar, S. Pironio, and V. Scarani, "Device-independent security of quantum cryptography against collective attacks," Phys. Rev. Lett. 98, 230501 (2007).  
19S. Wengerowsky, S. K. Joshi, F. Steinlechner, J. R. Zichi, S. M. Dobrovolskiy, R. van der Molen, J. W. Los, V. Zwiller, M. A. Versteegh, A. Mura, D. Calonico, M. Inguscio, H. Hubel, L. Bo, T. Scheidl, A. Zeilinger, A. Xuereb, and R. Ursin, "Entanglement distribution over a 96-km-long submarine optical fiber," Proc. Natl. Acad. Sci. U. S. A. 116, 6684-6688 (2019).  
20P. G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A. V. Sergienko, and Y. Shih, "New high-intensity source of polarization-entangled photon pairs," Phys. Rev. Lett. 75, 4337-4341 (1995).  
21M. Giustina, M. A. Versteegh, S. Wengerowsky, J. Handsteiner, A. Hochrainer, K. Phelan, F. Steinlechner, J. Kofler, J. Å. Larsson, C. Abellán, W. Amaya, V. Pruneri, M. W. Mitchell, J. Beyer, T. Gerrits, A. E. Lita, L. K. Shalm, S. W. Nam, T. Scheidl, R. Ursin, B. Wittmann, and A. Zeilinger, "Significant-loophole-free test of Bell's theorem with entangled photons," Phys. Rev. Lett. 115, 250401 (2015).  
22 L. K. Shalm, E. Meyer-Scott, B. G. Christensen, P. Bierhorst, M. A. Wayne, M. J. Stevens, T. Gerrits, S. Glancy, D. R. Hamel, M. S. Allman, K. J. Coakley, S. D. Dyer, C. Hodge, A. E. Lita, V. B. Verma, C. Lambrocco, E. Tortorici, A. L. Migdall, Y. Zhang, D. R. Kumor, W. H. Farr, F. Marsili, M. D. Shaw, J. A. Stern, C. Abellan, W. Amaya, V. Pruneri, T. Jennewein, M. W. Mitchell, P. G. Kwiat, J. C. Bienfang, R. P. Mirin, E. Knill, and S. W. Nam, "Strong loophole-free test of local realism," Phys. Rev. Lett. 115, 250402 (2015).  
23N. Akopian, N. H. Lindner, E. Poem, Y. Berlatzky, J. Avron, D. Gershoni, B. D. Gerardot, and P. M. Petroff, "Entangled photon pairs from semiconductor quantum dots," Phys. Rev. Lett. 96, 130501 (2006).  
24 M. Gurioli, Z. Wang, A. Rastelli, T. Kuroda, and S. Sanguinetti, “Droplet epitaxy of semiconductor nanostructures for quantum photonic devices,” Nat. Mater. 18, 799–810 (2019).  
25Y. H. Huo, A. Rastelli, and O. G. Schmidt, "Ultra-small excitonic fine structure splitting in highly symmetric quantum dots on GaAs (001) substrate," Appl. Phys. Lett. 102, 152105 (2013).  
D. Huber, M. Reindl, S. F. Covre da Silva, C. Schimpf, J. Martin-Sanchez, H. Huang, G. Piredda, J. Edlinger, A. Rastelli, and R. Trotta, "Strain-tunable GaAs quantum dot: a nearly dephasing-free source of entangled photon pairs on demand," Phys. Rev. Lett. 121, 033902 (2018).  
27M. E. Reimer, G. Bulgariini, N. Akopian, M. Hocevar, M. B. Bavinck, M. A. Verheijen, E. P. Bakkers, L. P. Kouwenhoven, and V. Zwiller, "Bright single

photon sources in bottom-up tailored nanowires," Nat. Commun. 3, 1746 (2012).  
28G. Juska, V. Dimastrodonato, L. O. Mereni, A. Gocalinska, and E. Pelucchi, "Towards quantum-dot arrays of entangled photon emitters," Nat. Photonics 7, 527-531 (2013).  
29 A. Orieux, M. A. Versteegh, K. D. Jons, and S. Ducci, "Semiconductor devices for entangled photon pair generation: A review," Rep. Prog. Phys. 80, 076001 (2017).  
30L. Schweickert, K. D. Jons, K. D. Zeuner, S. F. Covre Da Silva, H. Huang, T. Lettner, M. Reindl, J. Zichi, R. Trotta, A. Rastelli, and V. Zwiller, "On-demand generation of background-free single photons from a solid-state source," Appl. Phys. Lett. 112, 093106 (2018).  
31H. J. Briegel, W. Dur, J. I. Cirac, and P. Zoller, "Quantum repeaters: The role of imperfect local operations in quantum communication," Phys. Rev. Lett. 81, 5932-5935 (1998).  
32S. Lloyd, M. S. Shahriar, J. H. Shapiro, and P. R. Hemmer, "Long distance, unconditional teleportation of atomic states via complete bell state measurements," Phys. Rev. Lett. 87, 167903 (2001).  
33C. K. Hong, Z. Y. Ou, and L. Mandel, "Measurement of subpicosecond time intervals between two photons by interference," Phys. Rev. Lett. 59, 2044 (1987).  
34F. Olbrich, J. Höschele, M. Müller, J. Kettler, S. Luca Portalupi, M. Paul, M. Jetter, and P. Michler, "Polarization-entangled photons from an InGaAs-based quantum dot emitting in the telecom C-band," Appl. Phys. Lett. 111, 133106 (2017).  
35J. H. Weber, B. Kambs, J. Kettler, S. Kern, J. Maisch, H. Vural, M. Jetter, S. L. Portalupi, C. Becher, and P. Michler, "Two-photon interference in the telecom C-band after frequency conversion of photons from remote quantum emitters," Nat. Nanotechnol. 14, 23-26 (2019).  
36H. Vural, S. L. Portalupi, and P. Michler, “Perspective of self-assembled InGaAs quantum-dots for multi-source quantum implementations,” Appl. Phys. Lett. 117, 030501 (2020).  
37M. Anderson, T. Müller, J. Skiba-Szymanska, A. B. Krysa, J. Huwer, R. M. Stevenson, J. Heffernan, D. A. Ritchie, and A. J. Shields, "Coherence in single photon emission from droplet epitaxy and Stranski-Krastanov quantum dots in the telecom C-band," Appl. Phys. Lett. 118, 014003 (2021).  
38S. Stufler, P. Machnikowski, P. Ester, M. Bichler, V. M. Axt, T. Kuhn, and A. Zrenner, "Two-photon Rabi oscillations in a single  $\mathrm{In_xGa_{1 - x}}$  As GaAs quantum dot," Phys. Rev. B 73, 125304 (2006).  
39 O. Benson, C. Santori, M. Pelton, and Y. Yamamoto, "Regulated and entangled photons from a single quantum dot," Phys. Rev. Lett. 84, 2513-2516 (2000).  
40F. Basso Basset, F. Salusti, L. Schweickert, M. B. Rota, D. Tedeschi, S. F. Covre da Silva, E. Roccia, V. Zwiller, K. D. Jons, A. Rastelli, and R. Trotta, "Quantum teleportation with imperfect quantum dots," NPJ Quantum Inf. 7, 7 (2021).  
4D. Huber, B. U. Lehner, D. Csontosova, M. Reindl, S. Schuler, S. F. Covre Da Silva, P. Klenovsky, and A. Rastelli, "Single-particle-picture breakdown in laterally weakly confining GaAs quantum dots," Phys. Rev. B 100, 235425 (2019).  
42J. Schneeloch, S. H. Knarr, D. F. Bogorin, M. L. Levangie, C. C. Tison, R. Frank, G. A. Howland, M. L. Fanto, and P. M. Alsing, "Introduction to the absolute brightness and number statistics in spontaneous parametric down-conversion," J. Opt. 21, 043501 (2019).  
43D. F. V. James, P. G. Kwiat, W. J. Munro, and A. G. White, "Measurement of qubits," Phys. Rev. A 64, 052312 (2001).  
44 R. Trotta, J. Martin-Sanchez, I. Daruka, C. Ortiz, and A. Rastelli, "Energy-tunable sources of entangled photons: A viable concept for solid-state-based quantum relays," Phys. Rev. Lett. 114, 150502 (2015).  
45K. D. Jons, L. Schweickert, M. A. Versteegh, D. Dalacu, P. J. Poole, A. Gulinatti, A. Giudice, V. Zwiller, and M. E. Reimer, "Bright nanoscale source of deterministic entangled photon pairs violating Bell's inequality," Sci. Rep. 7, 1700 (2017).  
46T. Jennewein, C. Simon, G. Weihs, H. Weinfurter, and A. Zeilinger, "Quantum cryptography with entangled photons," Phys. Rev. Lett. 84, 4729-4732 (2000).  
47R. Trotta, J. Martin-Sanchez, J. S. Wildmann, G. Piredda, M. Reindl, C. Schimpf, E. Zallo, S. Stroj, J. Edlinger, and A. Rastelli, "Wavelength-tunable sources of entangled photons interfaced with atomic vapours," Nat. Commun. 7, 10375 (2016).

D. Huber, M. Reindl, Y. Huo, H. Huang, J. S. Wildmann, O. G. Schmidt, A. Rastelli, and R. Trotta, "Highly indistinguishable and strongly entangled photons from symmetric GaAs quantum dots," Nat. Commun. 8, 15506 (2017).  
Y. Chen, M. Zopf, R. Keil, F. Ding, and O. G. Schmidt, "Highly-efficient extraction of entangled photons from quantum dots using a broadband optical antenna," Nat. Commun. 9, 2994 (2018).  
50J. Liu, R. Su, Y. Wei, B. Yao, S. F. C. da Silva, Y. Yu, J. Iles-Smith, K. Srinivasan, A. Rastelli, J. Li, and X. Wang, "A solid-state source of strongly entangled photon pairs with high brightness and indistinguishability," Nat. Nanotechnol. 14, 586-593 (2019).  
51H. Wang, H. Hu, T. H. Chung, J. Qin, X. Yang, J. P. Li, R. Z. Liu, H. S. Zhong, Y. M. He, X. Ding, Y. H. Deng, Q. Dai, Y. H. Huo, S. Hofling, C. Y. Lu, and J. W. Pan, "On-demand semiconductor source of entangled photons which simultaneously has high fidelity, efficiency, and indistinguishability," Phys. Rev. Lett. 122, 113602 (2019).  
52C. Antonelli, M. Shtaif, and M. Brodsky, "Sudden death of entanglement induced by polarization mode dispersion," Phys. Rev. Lett. 106, 080404 (2011).  
53 H. T. Lim, K. H. Hong, and Y. H. Kim, "Effects of polarization mode dispersion on polarization-entangled photons generated via broadband pumped spontaneous parametric down-conversion," Sci. Rep. 6, 25846 (2016).  
54K. Sanaka, K. Kawahara, and T. Kuga, "Experimental probabilistic manipulation of down-converted photon pairs using unbalanced interferometers," Phys. Rev. A 66, 040301 (2002).  
55R. Simon and N. Mukunda, "Minimal three-component SU(2) gadget for polarization optics," Phys. Lett. A 143, 165-169 (1990).  
56 A. Lenhard, J. Brito, S. Kucera, M. Bock, J. Eschner, and C. Becher, "Single telecom photon heralding by wavelength multiplexing in an optical fiber," Appl. Phys. B 122, 20 (2016).  
57K. D. Zeuner, K. D. Jons, L. Schweickert, C. R. Hedlund, C. N. Lobato, T. Lettner, K. Wang, S. Gyger, E. Schöll, S. Steinhauer, M. Hammar, and V. Zwiller, "On-demand generation of entangled photon pairs in the telecom c-band for fiber-based quantum networks," arXiv:1912.04782 (2019).  
58S. Wengerowsky, S. K. Joshi, F. Steinlechner, J. R. Zichi, B. Liu, T. Scheidl, S. M. Dobrovolskiy, R. van der Molen, J. W. Los, V. Zwiller, M. A. Versteegh, A. Mura, D. Calonico, M. Inguscio, A. Zeilinger, A. Xuereb, and R. Ursin, "Passively stable distribution of polarisation entanglement over  $192\mathrm{km}$  of deployed optical fibre," NPJ Quantum Inf. 6, 5 (2020).  
59 L. M. Duan, M. D. Lukin, J. I. Cirac, and P. Zoller, "Long-distance quantum communication with atomic ensembles and linear optics," Nature 414, 413-418 (2001).  
60M. Riebe, H. Häffner, C. F. Roos, W. Hansel, J. Benhelm, G. P. T. Lancaster, T. W. Körber, C. Becher, F. Schmidt-Kaler, D. F. V. James, and R. Blatt, "Deterministic quantum teleportation with atoms," Nature 429, 734-737 (2004).  
$^{61}$ P. C. Humphreys, N. Kalb, J. P. J. Morits, R. N. Schouten, R. F. L. Vermeulen, D. J. Twitchen, M. Markham, and R. Hanson, "Deterministic delivery of remote entanglement on a quantum network," Nature 558, 268-273 (2018).  
62B. T. Kirby, S. Santra, V. S. Malinovsky, and M. Brodsky, "Entanglement swapping of two arbitrarily degraded entangled states," Phys. Rev. A 94, 012336 (2016).  
63F. Basso Basset, M. B. Rota, C. Schimpf, D. Tedeschi, K. D. Zeuner, S. F. C. da Silva, M. Reindl, V. Zwiller, K. D. Jons, A. Rastelli, and R. Trotta, "Entanglement swapping with photons generated on-demand by a quantum dot," Phys. Rev. Lett. 123, 160501 (2019).  
64T. Huber, A. Predojevi, H. Zoubi, G. S. Solomon, and G. Weihs, "Measurement and modification of biexciton-exciton time correlations," Opt. Express 21, 9890-9898 (2013).  
65 E. Scholl, L. Schweickert, L. Hanschke, K. D. Zeuner, F. Sbresny, T. Lettner, R. Trivedi, M. Reindl, S. F. Covre Da Silva, R. Trotta, J. J. Finley, J. Vuckovic, K. Müller, A. Rastelli, V. Zwiller, and K. D. Jön's, "Crux of using the cascaded emission of a three-level quantum ladder system to generate indistinguishable photons," Phys. Rev. Lett. 125, 233605 (2020).  
66A. V. Kuhlmann, J. Houel, A. Ludwig, L. Greuter, D. Reuter, A. D. Wieck, M. Poggio, and R. J. Warburton, "Charge noise and spin noise in a semiconductor quantum device," Nat. Phys. 9, 570-575 (2013).  
67B. Kambs and C. Becher, "Limitations on the indistinguishability of photons from remote solid state sources," New J. Phys. 20, 115003 (2018).

68 M. Reindl, K. D. Jons, D. Huber, C. Schimpf, Y. Huo, V. Zwiller, A. Rastelli, and R. Trotta, "Phonon-assisted two-photon interference from remote quantum emitters," Nano Lett. 17, 4090-4095 (2017).  
$^{69}$ C. Gustin and S. Hughes, “Pulsed excitation dynamics in quantum-dot-cavity systems: Limits to optimizing the fidelity of on-demand single-photon sources,” Phys. Rev. B 98, 045309 (2018).  
70L. Hanschke, K. A. Fischer, S. Appel, D. Lukin, J. Wierzbowski, S. Sun, R. Trivedi, J. Vuckovic, J. J. Finley, and K. Müller, "Quantum dot single-photon sources with ultra-low multi-photon probability," NPJ Quantum Inf. 4, 43 (2018).  
7K. Mattle, H. Weinfurter, P. G. Kwiat, and A. Zeilinger, “Dense coding in experimental quantum communication,” Phys. Rev. Lett. 76, 4656-4659 (1996).  
72 A. I. Lvovsky, B. C. Sanders, and W. Tittel, "Optical quantum memory," Nat. Photonics 3, 706-714 (2009).  
73K. T. Kaczmarek, P. M. Ledingham, B. Brecht, S. E. Thomas, G. S. Thekkadath, O. Lazo-Arjona, J. H. Munns, E. Poem, A. Feizpour, D. J. Saunders, J. Nunn, and I. A. Walmsley, "High-speed noise-free optical quantum memory," Phys. Rev. A 97, 042316 (2018).  
74 R. Finkelstein, E. Poem, O. Michel, O. Lahad, and O. Firstenberg, "Fast, noise-free memory for photon synchronization at room temperature," Sci. Adv. 4, eaap8598 (2018).  
75M. Afzelius, C. Simon, H. De Riedmatten, and N. Gisin, "Multimode quantum memory based on atomic frequency combs," Phys. Rev. A 79, 052329 (2009).  
76L. Li and A. Kuzmich, "Quantum memory with strong and controllable Rydberg-level interactions," Nat. Commun. 7, 13618 (2016).  
77M. Cao, F. Hoffet, S. Qiu, A. S. Sheremet, and J. Laurat, "Efficient reversible entanglement transfer between light and quantum memories," Optica 7, 1440 (2020).  
78 M. P. Hedges, J. J. Longdell, Y. Li, and M. J. Sellars, "Efficient quantum memory for light," Nature 465, 1052 (2010).

79M. Zhong, M. P. Hedges, R. L. Ahlefeldt, J. G. Bartholomew, S. E. Beavan, S. M. Wittig, J. J. Longdell, and M. J. Sellars, "Optically addressable nuclear spins in a solid with a six-hour coherence time," Nature 517, 177-180 (2015).  
80A. Seri, A. Lenhard, D. Rieländer, M. Gundogan, P. M. Ledingham, M. Mazzera, and H. de Riedmatten, "Quantum correlations between single telecom photons and a multimode on-demand solid-state quantum memory," Phys. Rev. X 7, 021028 (2017).  
N. Maring, P. Ferrera, K. Kutluer, M. Mazzera, G. Heinze, and H. De Riedmatten, "Photonic quantum state transfer between a cold atomic gas and a crystal," Nature 551, 485-488 (2017).  
82J. S. Tang, Z. Q. Zhou, Y. T. Wang, Y. L. Li, X. Liu, Y. L. Hua, Y. Zou, S. Wang, D. Y. He, G. Chen, Y. N. Sun, Y. Yu, M. F. Li, G. W. Zha, H. Q. Ni, Z. C. Niu, C. F. Li, and G. C. Guo, "Storage of multiple single-photon pulses emitted from a quantum dot in a solid-state quantum memory," Nat. Commun. 6, 9652 (2015).  
83K. Azuma, K. Tamaki, and H. K. Lo, "All-photonic quantum repeaters," Nat. Commun. 6, 6787 (2015).  
84C. Dietrich, A. Fiore, M. Thompson, M. Kamp, and S. Hofling, "Gaas integrated quantum photonics: Towards compact and multi-functional quantum photonic integrated circuits," Laser Photonics Rev. 10, 870-894 (2016).  
85C. L. Salter, R. M. Stevenson, I. Farrer, C. A. Nicoll, D. A. Ritchie, and A. J. Shields, "An entangled-light-emitting diode," Nature 465, 594-597 (2010).  
86M. Anderson, T. Müller, J. Skiba-Szymanska, A. B. Krysa, J. Huwer, R. M. Stevenson, J. Heffernan, D. A. Ritchie, and A. J. Shields, "Gigahertz-clocked teleportation of time-bin qubits with a quantum dot in the telecommunication C band," Phys. Rev. Appl. 13, 054052 (2020).  
87R. Trotta, E. Zallo, E. Magerl, O. G. Schmidt, and A. Rastelli, "Independent control of exciton and biexciton energies in single quantum dots via electroelastic fields," Phys. Rev. B 88, 155312 (2013).