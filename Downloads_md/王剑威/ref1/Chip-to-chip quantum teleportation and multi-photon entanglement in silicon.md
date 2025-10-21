# Chip-to-chip quantum teleportation and multi-photon entanglement in silicon

Daniel Llewellyn $^{1,11}$ , Yunhong Ding $^{2,3,11}$ , Imad I. Faruque $^{1,11}$ , Stefano Paesani $^{1}$ , Davide Bacco $^{2,3}$ , Raffaele Santagati $^{1}$ , Yan-Jun Qian $^{4}$ , Yan Li $^{4,5}$ , Yun-Feng Xiao $^{4,5,6}$ , Marcus Huber $^{7}$ , Mehul Malik $^{8}$ , Gary F. Sinclair $^{1}$ , Xiaqi Zhou $^{9}$ , Karsten Rottwitt $^{2,3}$ , Jeremy L. O'Brien $^{10}$ , John G. Rarity $^{1}$ , Qihuang Gong $^{4,5,6}$ , Leif K. Oxenlowe $^{2,3}$ , Jianwei Wang $^{1,4,5,6*}$  and Mark G. Thompson $^{1}$

Integrated optics provides a versatile platform for quantum information processing and transceiving with photons $^{1-8}$ . The implementation of quantum protocols requires the capability to generate multiple high-quality single photons and process photons with multiple high-fidelity operators $^{9-11}$ . However, previous experimental demonstrations were faced by major challenges in realizing sufficiently high-quality multi-photon sources and multi-qubit operators in a single integrated system $^{4-8}$ , and fully chip-based implementations of multi-qubit quantum tasks remain a significant challenge $^{1-3}$ . Here, we report the demonstration of chip-to-chip quantum teleportation and genuine multipartite entanglement, the core functionalities in quantum technologies, on silicon-photonic circuitry. Four single photons with high purity and indistinguishability are produced in an array of microresonator sources, without requiring any spectral filtering. Up to four qubits are processed in a reprogrammable linear-optic quantum circuit that facilitates Bell projection and fusion operation. The generation, processing, transceiving and measurement of multiphoton multi-qubit states are all achieved in micrometre-scale silicon chips, fabricated by the complementary metal-oxide-semiconductor process. Our work lays the groundwork for large-scale integrated photonic quantum technologies for communications and computations.

Entanglement and teleportation form the backbone of quantum technologies $^{9-14}$ . Photons are unique in their ability to transmit quantum information over long distances and process quantum information with the low noise, positioning entanglement and teleportation of photonic qubits that are at the heart of quantum communications, quantum networks and quantum computations. For example, quantum communication networks $^{15}$ —where small-scale quantum processors are coherently connected via quantum channels—are based on the long-range distribution of multi-photon entangled states and the teleportation of qubit states $^{12,13}$ . In the Knill-Laflamme-Milburn optical quantum computing scheme $^{9}$ , teleportation of non-deterministic entangling gates allows an efficient improvement of the success probability $^{14}$ .

Measurement-based quantum computing models, which are more resource-efficient for optical quantum computing $^{10}$ , are fully based on cluster entangled states and the teleportation of logical operations between qubit sites.

Integrated photonics provides a versatile platform for quantum information processing and communications $^{16}$ . Previous demonstrations have shown the integration of two-photon sources and circuits $^{6}$ , as well as precise control of photonic states $^{3}$ . However, the difficulties in realizing high-performance multi-photon sources and multi-qubit operators present major challenges in implementing advanced quantum tasks. Here, by developing state-of-the-art multi-photon multi-qubit quantum devices in silicon, we demonstrate the chip-to-chip quantum teleportation of arbitrary single-qubit states and the generation of four-photon four-qubit Greenberger-Horne-Zeilinger (GHZ) genuine entangled states.

In silicon, single photons can be generated in centimetre-length waveguides via the spontaneous four-wave mixing (SFWM) process[6-8]. However, the produced photon pairs are highly correlated in frequency[7], and improving their spectral purity requires narrowband spectral filtering, causing a significant reduction of photon rates and heralding efficiency. The waveguide sources thus present fundamental challenges in scaling up to multi-photon implementations[7,8,18]. Instead, microring resonators (MRRs) have been proposed for the generation of single photons with high spectral purity[19] as well as high heralding efficiency by removing the requirement for a spectral filtering process[20]. Although MRRs have been adopted to produce two-photon[4,21] and multi-photon states[5,22], they have not yet been used to demonstrate single photons with a high level of purity, indistinguishability and heralding efficiency. In addition, when using waveguide sources, photons are generated uniformly in the sources and also circuits[6-8], which induces noise in the quantum operations. Locally enhancing the SFWM using MRRs can greatly suppress the noise outside the MRRs by allowing the use of weak pump light. In this work, we realize an array of MRRs to generate multiple high-quality single photons, which are monolithically integrated with linear-optic circuits that process multiple qubits with high fidelity and low noise.

![](images/bca9faee2747165e95969514b2c54a1e23dda2414af7a3a88a6b915968a429a3.jpg)  
b

![](images/5811f846a44e1fad4a0a5fb532683381982b8785c5df5874ca3df3082573d791.jpg)  
c

![](images/fa88483fc9b414ece9dd142d06bef8c36d8ca27f54f9a4ca83248df431f0114e.jpg)  
d

![](images/15247667778353619eecdf773a6494513f00ed5e0b558d232b0844045215a509.jpg)  
Fig. 1 | Microresonator-enhanced multi-photon multi-qubit quantum devices in silicon. a, Schematic for the multi-qubit entanglement generator, or the teleportation transmitter. It integrates a network of nonlinear multi-photon sources and linear-optic multi-qubit circuits. Two pairs of non-degenerate photons (red idler, blue signal) are generated in an array of four MRR single-photon sources. Small blue/red circles (photons) with coloured links indicate whether the two photons are entangled or separable. The MRRs allow high-count-rate, pure and indistinguishable photon generation while also suppressing background noise from all waveguides and linear circuits. A linear-optic quantum circuit  $(\hat{O})$  is programmed to work as a bosonic Bell operator and a fusion entangling operator on the two blue photons. The four photons are demultiplexed by asymmetric MZIs and routed via waveguide crossovers  $(\hat{R})$ . An array of MZIs and phase-shifters allow the preparation  $(\hat{P})$  and projective measurement  $(\hat{M})$  of multi-qubit states. Yellow parts indicate electronically controllable thermal-optic phase-shifters. b, Schematic for the teleportation receiver. The transmitter and receiver are coherently linked by a  $10\mathrm{m}$  single-mode fibre. The bottom idler qubits in the transmitter can be switched to implement either single-chip (via 1D SGCs) or chip-to-chip (via 2D SGCs) tasks. The receiver chip converts polarization-encoded qubits to the path, which are subsequently measured on the device. c,d, SEM images of an MRR single-photon source coupled to a bus waveguide (red lines) (c) and a metasurface-assisted low-loss SGC with bonded aluminium reflectors (d). d, Top: 1D SGC for fibre-chip interface. Bottom: 2D SGC for path-polarization conversion. |TE> refers to the transverse electric state in waveguide, and |H> (|V>) refers to the horizontal (vertical) state in optical fibre. Inset: Enlarged view of a metasurface cell. White arrows denote the polarized state of the photon.

Photonic qubit-qubit interactions are based on quantum interference and success of measurement. This has enabled demonstrations of controlled-Z operation and single-chip teleportation on a silica platform. However, full integration of multi-photon sources and multi-qubit operators in this system remains a major challenge. Our chip-to-chip teleportation was realized between two separate silicon chips, and the measured state fidelities are among the highest reported so far due to the full integration of all necessary components with high performance (Fig. 1a,b). Recently, a similar scheme for three-photon GHZ entanglement has been theoretically proposed using MRRs and circuits, although its further scaling ability may be challenging. In our device (Fig. 1a), four-photon four-qubit GHZ genuine states were generated and certified, and can be further scaled up to a larger system. Figure 1 presents the multi-photon multi-qubit devices, fabricated on a silicon-on-insulator platform. The Si MRR sources array (scanning electron microscopy (SEM) image in Fig. 1c) can produce two pairs of signal  $(\lambda_{\mathrm{s}})$  and idler  $(\lambda_{\mathrm{i}})$  photons via SFWM. Four dual-rail qubits are encoded in the four generated photons. Each qubit is represented in the logical basis  $\{|0\rangle_k,|1\rangle_k\}$ $(k = 1,2,3,4)$  and can be prepared  $(\hat{\mathbf{P}})$  and measured  $(\hat{\mathbf{M}})$  by a network of Mach-Zehnder interferometers (MZI) and phase-shifters. Another key component is the reprogrammable two-qubit operator  $(\hat{\mathrm{O}})$ , which can entangle two qubits (previously never interacted) in two different manners: Bell projection and fusion operation. The MRR sources, qubit generator, entangling operator and qubit analyser are all individually controllable and fully programmable. To preserve coherent teleportation between the transmitter and receiver chips, we exploit a polarization-path conversion technique relying on two-dimensional (2D) subwavelength grating couplers (SGCs; Fig. 1d). The chips are coupled to optical fibres via an array of 1D SGCs (Fig. 1d), and photons are then detected off-chip by eight superconducting single-photon detectors ( $\sim 0.85$  efficiency). Details on the device and set-up are provided in Supplementary Section 1.

As shown in Fig. 2b, the generated two-photon rate is enhanced by a factor of  $\sim 43$  when the MRR is on versus off resonance. For each MRR, a raw rate of  $\sim 20\mathrm{kcts}\mathrm{s}^{-1}$  at a coincidences-to-accidents ratio of  $\sim 50$  was detected, using a pump laser with  $15\mathrm{ps}$  pulse width and  $500\mathrm{MHz}$  repetition rate at  $800\mu \mathrm{W}$  power. Because the MRR

sources only require a weak pump, negligible photons are created in the surrounding waveguides and circuits, greatly suppressing noise there. We also measured the photon number purity of the single photons by performing the Hanbury-Brown-Twiss measurement of photons to obtain the heralded second-order correlation  $g^{(2)}(0)$ . At the same power, we observed  $g^{(2)}(0) = 0.05$ , corresponding to  $95\%$  photon number purity (Fig. 2c). A high heralding efficiency of  $\sim 50\%$  after the resonators was measured.

The four MRRs are designed to be identical. The high-yield fabrication enables nearly identical free spectral ranges (FSRs  $\approx 400\mathrm{GHz}$ , Fig. 2a) and high spectral overlap at resonances (Supplementary Fig. 5). Each MRR can be individually tuned and frequency-locked (Supplementary Section 2), ensuring photon wavefunctions that are highly overlapped in the spectral mode. The photon indistinguishability is estimated by the visibility of heralded two-photon quantum interference. We interfere two signal photons on a MZI (heralding two idler photons), which are emitted from two independent MRRs. Figure 2e reports a quantum interference fringe with multi-pair corrected visibility of  $90.99 \pm 3.91\%$ , which agrees within error to the fundamental limit of  $92\%$  spectral purity for our MRR design. The asymmetric modulation in the fringe is due to the use of imperfect beamsplitters[22] (see discussions in Supplementary Section 2). Figure 2d presents the raw uncorrected visibility as a function of the mean photon number per pulse  $(\overline{n})$ , which shows  $\sim 84\%$  raw visibility at  $\overline{n} = 0.05$ , for example. Figure 2f shows the pairwise indistinguishability of the four MRR sources, with a mean raw visibility of  $71.9 \pm 2.4\%$  in a high pumping configuration, which, if multi-pair corrected, reaches  $87.3 \pm 1.9$  mean visibility. Remarkably, in all of our indistinguishability measurements, we have not used any spectral filtering process to improve the spectral purity. The MRR sources demonstrate significantly better performance compared with the waveguide sources (for a quantitative analysis see Supplementary Section 2).

The MRR source array is programmed to create either entangled or separable bipartite states by controlling the pump excitation in the MRRs and reconfiguring asymmetric MZIs. When the operator  $\hat{O}$  between qubits 2,3 is turned off (Fig. 3a) the original bipartite states from the MRR array are measured. We implement quantum state tomography (QST) to reconstruct the density matrix  $\rho$ .

![](images/4578e4f842b0ea18001a3175c0499c8b627b4ba3caa857baaaa96acea9dbd248.jpg)  
a

![](images/a9f1e858df400f157b4d18c2433d8d8147d3d1cdabfa25644f628156b709743d.jpg)  
b

![](images/a4e216ac52722f12de09891a7827bf82497409bd7dba65dd83ebed4c378b9d9d.jpg)  
c

![](images/ac31893f4adc983791ff622c6995432073816b5b26b95d324f2eaa348a8c7dfe.jpg)  
d

![](images/39f322ccac5a4de6ae6a6873811f4c18fa81c15979aef88ef6761da035db9a5f.jpg)  
e

![](images/f84e95fbe42ed803d0d9b6d78c4251dcd5f5f9bd5be7af67f5440afde002f2c0.jpg)  
Fig. 2 | Photon pair generation in an array of microresonator nonlinear sources. a, The measured transmission spectra for an MRR (top) and asymmetric MZI (bottom), with free spectral ranges  $\mathrm{FSR}_{\mathrm{MRR}} = 400\mathrm{GHz}$  and  $\mathrm{FSR}_{\mathrm{AMZI}} = 320\mathrm{GHz}$ . Signal photons are created at  $\lambda_{s} = 1,539.758\mathrm{nm}$  and idler photons at  $\lambda_{i} = 1,559.015\mathrm{nm}$ , with pump light at  $\lambda_{p} = 1,549.30\mathrm{nm}$ , all at the resonances of the MRR. Asymmetric MZIs can demultiplex the  $\lambda_{s}$  and  $\lambda_{i}$  photons. Residual pump photons are removed by off-chip filters with  $\sim 1.1\mathrm{nm}$  bandwidth, much wider than the linewidth of MRRs,  $37.7\pm 1.9\mathrm{pm}$ . b, FWM enhancement in the MRR on-resonance. Background noise in the whole device is efficiently suppressed (off resonance). c, Tests of photon number purity by measuring the heralded  $g^{(2)}(0)$ . d, Measured raw visibility of the heralded quantum interference, as a function of mean photon number  $\bar{n}$  per pulse. The  $V = 0.92$  dotted line is the maximum achievable visibility for our MRR designs. e, Tests of spectral indistinguishability, with a subtraction of multi-pair events. A visibility of  $90.99\pm 3.91\%$  is obtained, in agreement with the theoretical limit. Fourfold coincidences (CC) are accumulated in two minutes. f, Measured visibility of quantum interference between pairwise MRRs in the array. Mean visibilities of  $87.3\pm 1.9\%$  and  $71.9\pm 2.4\%$  are measured, with and without multi-pair corrections. Points are all experimental data; lines in d are theoretical values and lines in b,c,e are fittings. All error bars refer to  $\pm 1\mathrm{s.d}$  estimated from Poissonian photon-counting statistics.  
f

As examples, Fig. 3d,e shows the measured  $\rho$  for separable states  $|10\rangle_{2,3}$  and  $|++\rangle_{2,3}$  with fidelities of  $0.964 \pm 0.072$  and  $0.966 \pm 0.024$ , respectively. The fidelity is defined as  $F = \langle \psi_0 | \rho |\psi_0 \rangle$ , where  $|\psi_0\rangle$  is the ideal state. We simultaneously prepared and measured two Bell pairs  $|\Phi\rangle_{1,2}^{+}$  and  $|\Phi\rangle_{3,4}^{+}$  from the four MRRs, with fidelities of  $0.917 \pm 0.002$  and  $0.915 \pm 0.003$ , respectively.

We then exploit a single programmable circuit to implement two key multi-qubit operations in quantum applications, that is, entangling initially separable qubits and measuring qubits in the Bell basis. Figure 3b,c shows the diagrams for the bosonic Bell projector  $\hat{\mathrm{O}}_{\mathrm{Bell}}$  and fusion operator  $\hat{\mathrm{O}}_{\mathrm{fusion}}$  that are devised for dual-rail qubits. We here study a case where the state  $|0\rangle^{\otimes 4}$  is initially prepared, then  $\rho_{2,3}$  is processed with the herald of photons 1, 4.  $\hat{\mathrm{O}}_{\mathrm{Bell}}$  is capable of distinguishing the Bell states  $|\Psi\rangle^{\pm}$  from the others. We distinguish  $|\Psi\rangle^{+}$  when observing joint clicks in {D3, D4} or {D5, D6} (Fig. 3a,b).  $\hat{\mathrm{O}}_{\mathrm{fusion}}$  transmits  $|0\rangle$  and swaps the  $|1\rangle$  mode, and is able to fuse a two-qubit separable state into an entangled state when detecting only one photon in {D3, D4} and another in {D5, D6} (Fig. 3a,c). To verify these new on-chip building blocks, heralded quantum interference and Bell state generation are performed. Figure 3f reports the two-qubit  $(|10\rangle_{2,3})$  interference, gradually rotating the qubit 2 around the  $\hat{\sigma}_{y}$  axis. The observed  $80.5 \pm 3.2\%$  visibility confirms high-quality interference of two bosons at  $\hat{\mathrm{O}}_{\mathrm{Bell}}$ . Figure 3g shows the two-qubit (input  $|++\rangle_{2,3}$ ) interference at  $\hat{\mathrm{O}}_{\mathrm{fusion}}$ , with  $85.8 \pm 4.4\%$  visibility, when rotating the qubit 2 around the  $\hat{\sigma}_{z}$  axis. In general, performing  $\hat{\mathrm{O}}_{\mathrm{Bell}}$  and  $\hat{\mathrm{O}}_{\mathrm{fusion}}$  enables the generation of entangled states, transforming the state  $|10\rangle_{2,3}$  (Fig. 3d) to  $|\Psi\rangle_{2,3}^{-}$  (Fig. 3h), and  $|++\rangle_{2,3}$  (Fig. 3e) to  $|\Phi\rangle_{2,3}^{+}$  (Fig. 3i). We obtained an entangled state with fidelities of  $0.851 \pm 0.040$  and  $0.830 \pm 0.032$ , respectively. More details are provided in Supplementary Section 3.

In the teleportation protocol, an unknown quantum state can be transmitted to another location by locally collapsing the state and

remotely reconstructing it $^{11}$ . This requires access to Bell states and Bell measurements. The single-chip teleportation experiment is initially implemented (Fig. 1a), in which we prepare an arbitrary single-qubit state  $|\psi \rangle_{2}$  in photon 2 ('B') via a unitary  $\hat{\mathrm{P}}$ , and a Bell pair  $|\varPhi\rangle_{3,4}^{+}$  in photon 3 ('C') and photon 4 ('D'). Photon 1 ('A') is used as a trigger. The  $\hat{\mathrm{O}}_{\mathrm{Bell}}$  measurement is performed at B and C, projecting the state into the  $|\Psi \rangle_{2,3}^{+}$ basis. This process allows the teleportation of B's state  $|\psi \rangle_{2}$  to D up to a local rotation  $\hat{\sigma}_{x}$ . We prepare six different  $|\psi \rangle_{2}$  states at B and reconstruct at D, obtaining  $|\phi \rangle_{4}$ . Full QST is implemented to reconstruct density matrices for the six  $|\phi \rangle_{4}$  states (for experimental data see Supplementary Fig. 12). On a single chip, we obtained high-fidelity teleported states with mean  $\overline{F} = 0.906 \pm 0.014$ .

We then implement the chip-to-chip teleportation. We ensure the preservation of coherent teleportation between two chips using the path-polarization conversion technique[25]. In our experiments, the  $|\varPhi\rangle_{3,4}^{+}$  state is created on the transmitter (Fig. 1a), and qubit 4 is distributed to the receiver chip (Fig. 1b) via a  $10\mathrm{m}$ -long optical fibre. We remark that the states of the entangled channel after distribution remain highly coherent with negligible degradation of fidelity (for the full set of distributed entangled states see Supplementary Fig. 11).  $\hat{\mathrm{O}}_{\mathrm{Bell}}$  is carried out on the transmitter. We implement teleportation of the six pure states, this time between the transmitter and receiver devices (for full data see Fig. 4a). The teleported states  $|\phi\rangle_{4}$  are recovered on the receiver, and QST reports average fidelities of  $\overline{F} = 0.885 \pm 0.037$ .

Teleportation of entanglement (that is, entanglement swapping) is a protocol whereby the sets of entanglement, say  $\{\mathrm{A},\mathrm{B}\}$  and  $\{\mathrm{C},\mathrm{D}\}$ , can be swapped<sup>11</sup>. This means that collapsing  $\{\mathrm{B},\mathrm{C}\}$  onto a Bell state will result in the entanglement of  $\{\mathrm{A},\mathrm{D}\}$ , which is unique in the sense that  $\{\mathrm{A},\mathrm{D}\}$  are not required to have ever interacted with one another. Figure 4b shows the circuit for entanglement swapping, where two Bell pairs  $|\varPhi\rangle_{1,2}^{+} \otimes |\varPhi\rangle_{3,4}^{+}$  are created in the MRR array and  $\hat{\mathcal{O}}_{\mathrm{Bell}}$  is performed on qubits 2, 3, projecting qubits 1, 4

![](images/1f92129e80e0dd4218088157950e51c5ef900f9a11f689a75b4374e0079a300a.jpg)

![](images/153f77b0bdb7885bd018dff41f5bcb555172ac7068f4ad8386f8a22f484435a6.jpg)  
d

![](images/43e14beb5880502d98cdcb971791c94ec84383c798e05ff504b4a0be481bfc1f.jpg)  
h

![](images/2d6903774f8a6278a281187b12c7367d1ed52fb8390abd3086d95ea6197f856c.jpg)  
f

![](images/f2fa430f9295ce36eb4a0e5c36aa202016db32372497a69eb9a329d7eedc025e.jpg)  
e

![](images/8a1f5d2736ea792184749cf231c5b7422f7c71ffed7f7987ee3889b08214914f.jpg)  
Fig. 3 | Programmable linear-optic quantum circuits for Bell projection and fusion operation. a, Simplified diagram for a general operator, in this case  $\hat{O} = \hat{l}\otimes \hat{l}$  on qubits 2, 3, that is,  $\hat{O}$  is off. Each pair of lines refers to the dual-rail logical state  $|0\rangle$  and  $|1\rangle$ . b,c, Diagrams for the Bell operator  $\hat{O}_{\mathrm{Bell}}(\mathbf{b})$  and fusion operator  $\hat{O}_{\mathrm{fusion}}(\mathbf{c})$  in the spatial mode. For  $\hat{O}_{\mathrm{Bell}}$ , a photon has  $50\%$  probability of being measured in either  $2^{\prime}$  or  $3^{\prime}$ , regardless of its input in 2 or 3.  $\hat{O}_{\mathrm{fusion}}$  transmits  $|0\rangle$  and swaps the  $|1\rangle$  mode. In the dashed boxes the circuits are reconfigured as a Hadamard-like or swap-like operator. d,e, The generated states in the source array can be programmed as either bipartite entangled (see Supplementary Information) or separable  $|10\rangle_{2,3}$  (d) and  $|++\rangle_{2,3}$  (e) (two red photons are in herald). The values in parentheses refer to the measured state fidelity  $(F)$  to their ideal states. f,g, Quantum interference when the two blue qubits  $|10\rangle_{2,3}$  ( $f$ ) ( $|++\rangle_{2,3}$  ( $\mathbf{g}$ )) meet at the  $\hat{O}_{\mathrm{Bell}}(\mathbf{f})$  ( $\hat{O}_{\mathrm{fusion}}(\mathbf{g})$ ) and rotate qubit 2 along the  $\hat{\sigma}_y$  axis (along the  $\hat{\sigma}_z$  axis). Points are experimental data measured in the  $\hat{\sigma}_y\hat{\sigma}_x$  basis, and lines are fitted with a sinusoidal function. h,i, Reconstructed density matrices for entangled states  $\rho_{2,3'}$  when performing  $\hat{O}_{\mathrm{Bell}}(\mathbf{h})$  or  $\hat{O}_{\mathrm{fusion}}(\mathbf{i})$  on the separable states in d and e. Small blue/red pulses indicate different photons in the experiment, while joining lines indicate entangled states and  $\otimes$  represents separable states. The  $\rho$  are reconstructed by performing full QST on chip. Column heights represent  $|\rho|$  while colours represent  $|\arg (\rho)|$ . All error bars refer to  $\pm 1$  s.d. estimated from Poissonian photon-counting statistics.

![](images/be627c3d0ab304d6902537450b0d96fc54a1e131ff38d245fae8176786dded3f.jpg)

![](images/0709248f87773b376fca0fcd216b676eeaf1031e8ee218280881d1b25c646551.jpg)  
g

into the entangled state  $|\Psi \rangle_{1,4}^{+}$ . Additionally, performing  $\hat{\mathrm{O}}_{\mathrm{fusion}}$  and measuring qubits 2, 3 in the  $\hat{\sigma}_x\hat{\sigma}_x$  basis produces the entangled state  $|\Phi \rangle_{1,4}^{+}$ . We perform QST on qubits 1, 4 and reconstruct  $|\Psi \rangle_{1,4}^{+}$  and  $|\Phi \rangle_{1,4}^{+}$  each from nine global measurement settings. Figure 4b(ii) reports the measured  $\rho$ , with fidelities of  $0.776 \pm 0.018$  and  $0.737 \pm 0.019$ , respectively, demonstrating successful on-chip entanglement swapping of photonic states.

We then generate three- and four-photon GHZ entangled states on  $\mathrm{chip}^{26}$ . Performing  $\hat{\mathrm{O}}_{\mathrm{fusion}}$  on the two Bell pairs  $|\varPhi\rangle_{1,2}^{+}\otimes |\varPhi\rangle_{3,4}^{+}$ enables fusion between qubits 2 and 3, thus yielding the four-qubit GHZ state  $|\varPhi\rangle_{\mathrm{GHZ}}^n = (|0\rangle^{\otimes n} + |1\rangle^{\otimes n}) / \sqrt{2}, n = 4$ . This entangling process succeeds with 0.5 probability, when detecting only one photon in each of  $\{\mathrm{D}1,\mathrm{D}2\}$ ,  $\{\mathrm{D}3,\mathrm{D}4\}$ ,  $\{\mathrm{D}5,\mathrm{D}6\}$  and  $\{\mathrm{D}7,\mathrm{D}8\}$  (Fig. 4c). The four-photon coincidence events arise from one of two cases—either all photons are in the  $|0\rangle$  mode or in the  $|1\rangle$  mode—which are quantum-mechanically indistinguishable in the superposition basis and thus result in coherent entanglement. The  $|\varPhi\rangle_{\mathrm{GHZ}}^3$  and

$|\varPhi\rangle_{\mathrm{GHZ}}^2$  (that is,  $|\varPhi\rangle_{1,4}^{+}$ ) states can be produced by locally measuring the remaining qubits in the  $\hat{\sigma}_x$  basis.

To verify genuine multipartite entanglement (GME) for the states where all subsystems are genuinely entangled, we measure an entanglement witness operator  $\hat{W}_n = \hat{I} /2 - |\Phi_{\mathrm{GHZ}}^n\rangle \langle \Phi_{\mathrm{GHZ}}^n |$  (ref. 27). Figure 4c reports the probability distribution in the basis  $\hat{\sigma}_{z}^{\otimes n}$ ,  $\hat{\sigma}_{x}^{\otimes n}$ , and the general basis  $\hat{\Omega}_{\theta}^{\otimes n} = (\cos \theta \hat{\sigma}_{x} + \sin \theta \hat{\sigma}_{y})^{\otimes n}$ , where  $\{\hat{\sigma}_{x},\hat{\sigma}_{y},\hat{\sigma}_{z}\}$  are the Pauli operators. The fringes of  $\langle \hat{\Omega}_{\theta}^{\otimes n}\rangle$  show the measured coherence of the GHZ states, and the variable oscillatory frequency confirms the correlation nature of  $n$ -photon GHZ entanglement. With a total of  $n + 1$  measurements, we calculate the  $F_{n = 3,4}^{\prime}$  fidelities for  $|\Phi \rangle_{\mathrm{GHZ}}^{n}$  with values of  $0.683\pm 0.014$  and  $0.735\pm 0.017$  and obtain  $\langle \hat{W}\rangle_{n = 3,4}$  values of  $-0.235\pm 0.017$  and  $-0.183\pm 0.014$  respectively, certifying the genuine entanglement of the four-photon and three-photon GHZ states with at least  $13\sigma$ .

![](images/ef4bd0629beb8c17fe186342b930d5892411ed76ef6d819f1f1b257618dccda6.jpg)  
a

![](images/9ac8ac944ed277ecf4814cf03ef598d804bd4eab63f9b302d03222871c06801d.jpg)  
(ii)

![](images/b0818700c216f8653446d848610cf51604e21ba253182110dc9cb0e66cf58760.jpg)  
$| + \rangle \to 0.832 \pm 0.048$

![](images/30e29cd0a2226ea4c3cbbac33cd3104b59527f0f12f0937cfc4acaa25c66e813.jpg)  
$| + i \rangle \rightarrow 0.894 \pm 0.026$

![](images/4366bade18e5776039017fd2039468ce8c19493bc9cd33f52c7798db1f6418a3.jpg)

![](images/1d04a5a0c9f9f624b4cce52e29d85872a87774f25fa8ed90f53fc18a034f8684.jpg)  
$\mid -\rangle \rightarrow 0.845\pm 0.041$

![](images/9d711a239516ae7cb85c78100c6f642d6ad58d1c75e468bd4cac377c68a1fe0a.jpg)  
$\vert -i\rangle \to 0.839\pm 0.039$

![](images/3553d7b5047684a3ee9c161bb1dc17c14483c8447b25c529e6c97ca13290f66f.jpg)  
b

![](images/aa7cba8df92c3a2bcedbd891fe3c3e06240396f3f631c83d100936438acc02f6.jpg)  
(ii)

![](images/e0e08ab23e852a26935f81241a192da163c6a7725f8ae712672435369c3ed48f.jpg)

![](images/95875c77cbda294f5dbb41773d15428838358374806ea810f2068ab5769a81d4.jpg)

![](images/d734ea78dfacb8406a648438402a85137568256f11d1d7858d1311d58570e602.jpg)  
c

![](images/54766d899fbe9fa0d01e38494d0ef9bf8c88b723c50ef96990498bd7893ded0e.jpg)  
$\langle \varOmega_{\theta}^{\otimes 2}\rangle$

![](images/0d5c52ca31970f9b1b348aa937107239c4be1ee67daa9e83b7ce2662168da916.jpg)  
$\langle \varOmega_{\theta}^{\otimes 3}\rangle$

![](images/d5752aae5e18441d992f202dc48432c47a8bce185304b78a527d01657d67ac0d.jpg)

![](images/a53b57480325a7d095807bab68a881b31ac483baa83b5a5ec5073cc522822bc8.jpg)  
(iii)

![](images/f0b01ec239c3a8f76d9e34f3291076fca67b910be4b6b4cfffb4af589a326bf6.jpg)  
Fig. 4 | Chip-to-chip quantum teleportation and multi-photon multi-qubit entanglement. a(i)-c(i) Quantum circuit diagrams for the teleportation of arbitrary single-qubit states from  $|\psi\rangle_{2}$  to  $|\phi\rangle_{4'}$  by performing Bell measurement of qubits 2, 3 (a); teleportation (entanglement swapping) of two-qubit entangled states from two Bell pairs  $\{|\Phi\rangle_{1,2}', |\Phi\rangle_{3,4}^{+}\}$  to  $|\Psi\rangle_{1,4}^{+}$  or  $|\Phi\rangle_{1,4}^{+}(\mathbf{b})$ ; generation of three-photon and four-photon GHZ entangled states  $|\Phi\rangle_{\mathrm{GHZ}}^{n}$ , by fusing  $|\Phi\rangle_{1,2}^{+}$  and  $|\Phi\rangle_{3,4}^{+}(\mathbf{c})$ . Each red (blue) line denotes the evolution of one qubit in the logical representation. Small blue/red pulses indicate different photons in the experiment, while joining lines indicate entangled states and  $\otimes$  represents separable states. a(ii), Experimental results for the chip-to-chip single-qubit teleportation. A full set of six states  $\{|0\rangle, |1\rangle, | + \rangle, | - \rangle, | + i\rangle, | - i\rangle\}$  was teleported from the transmitter to the receiver, respectively, reporting a mean fidelity of  $0.885 \pm 0.037$ . The  $\rho$  of six teleported states were reconstructed by full QST on the receiver chip. b(ii), Experimental results for two-qubit entanglement swapping. Performing  $\hat{\mathcal{O}}_{\mathrm{Bell}}(\hat{\mathcal{O}}_{\mathrm{fusion}})$  on  $|\Phi\rangle_{1,2}^{+}$  and  $|\Phi\rangle_{3,4}^{+}$  results in swapped entanglement  $|\Psi\rangle_{1,4}^{+}(|\Phi\rangle_{1,4}^{+})$  between photons that have not interacted. c(ii),(iii), Verification and quantification of GHZ genuine entanglement. Measured fourfold coincidences (normalized) in the  $\hat{\sigma}_{z}^{\otimes n}$  basis (ii) and  $\hat{\sigma}_{x}^{\otimes n}$  basis (iii) for  $n = 2, 3, 4$  photons. Grey boxes are theoretical probability distributions.  $\{|X\rangle, |\overline{X}\rangle\}$  refers to the  $(|0\rangle \pm |1\rangle) / \sqrt{2}$  states. In c(iii), expectation values of the coherence term  $\hat{\Omega}_{\theta}^{\otimes n}$  for  $n = 1, 2, 3, 4$  are shown. Each point is derived from a set of 16 fourfold coincidences in the general  $(\cos \theta \hat{\sigma}_{x} + \sin \theta \hat{\sigma}_{y})^{\otimes n}$  basis. The fringe in  $\theta \in [0, \pi]$  is fitted with a sinusoidal function. All error bars refer to  $\pm 1$  s.d. and are estimated from Poissonian photon-counting statistics. Errors in the fidelity of the reconstructed density matrices are estimated using Monte-Carlo simulations of the Poissonian counting statistics.

![](images/edc15780698c58374aa869195423c508a7024919a3d8359b1216cf3775c2dc20.jpg)

![](images/c67bff2d98e2e7755379da6c0b125c51a20888b98d9abc7098c69df0f3bbc83c.jpg)  
$\langle \Omega_{\theta}^{\otimes 4}\rangle$

We further quantify the GME of the generated GHZ states without QST or other assumptions on the state itself using GME-concurrence  $(C_{\mathrm{GME}})^{28}$ , which has computable bounds that turn out to be exact for GHZ-diagonal states. We use an efficient framework to lower bound the GME-concurrence from only two global measurement settings. Using only the outcome statistics of two measurements,

$\hat{\sigma}_{z}^{\otimes n}$  in Fig. 4c(ii) and  $\hat{\sigma}_{x}^{\otimes n}$  in Fig. 4c(iii), we arrive at values of  $C_{\mathrm{GME}}^{3} \leq 0.390 \pm 0.04$  and  $C_{\mathrm{GME}}^{4} \leq 0.192 \pm 0.039$  for three- and four-photon GHZ states respectively, thus efficiently quantifying genuine multipartite entanglement. The two-basis measurements can also be used to efficiently lower bound the state fidelity<sup>29</sup>, with values of  $0.593 \pm 0.019$  and  $0.693 \pm 0.020$  for the four- and three-photon states,

respectively. See Supplementary Section 5 for more details on the generation, verification and quantification of GME.

We have presented state-of-the-art silicon-photonic quantum devices that are able to produce, process, transmit and measure multi-photon multi-qubit states. With these devices, chip-based teleportation and genuine multi-photon entanglement have been demonstrated. The achieved teleportation with an  $\sim 0.90$  fidelity is among the highest seen $^{11}$ , owing to the realizations of high-quality multi-photon sources and multi-qubit operators. The photon sources are approaching the optimal levels of photon purity and indistinguishability, while the heralding efficiency can be further improved $^{20}$ . With the developed technologies, we expect the generation of 10-photon entangled states to be achievable in the near future $^{18}$ . Our MRRs provide the essential ingredients for integrated multiplexing sources $^{30}$ , which promise the near-deterministic generation of single photons. Moreover, with the 'near-zero change' of the complementary metal-oxide-semiconductor process, silicon offers the capability of integrating very large-scale quantum photonic circuits $^{6}$ . Our demonstrations pave the way for a complex integration of quantum nonlinear and linear-optic devices in silicon, which can find applications in quantum communications $^{12,13}$ , quantum-enhanced measurements $^{31}$ , quantum computing $^{10,18}$  and distributed quantum information processing networks $^{15}$ .

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of code and data availability and associated accessions codes are available at https://doi.org/10.1038/s41567-019-0727-x.

Received: 27 February 2019; Accepted: 18 October 2019; Published online: 23 December 2019

# References

1. Politi, A., Cryan, M. J., Parity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
2. Metcalf, B. J. et al. Quantum teleportation on a photonic chip. Nat. Photon. 8, 770-774 (2014).  
3. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).  
4. Silverstone, J. W. et al. Qubit entanglement between ringresonator photon-pair sources on a silicon chip. Nat. Commun. 6, 7948 (2015).  
5. Reimer, C. et al. Generation of multiphoton entangled quantum states by means of integrated frequency combs. Science 351, 1176-1180 (2016).  
6. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
7. Zhang, M. et al. Generation of multiphoton entangled quantum states with a single silicon nanowire. Light Sci. Appl. 8, 41 (2019).

8. Adcock, J. C., Vigliar, C., Santagati, R., Siverstone, J. & Thompson, M. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10, 3528 (2019).  
9. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2000).  
10. Nielsen, M. A. Optical quantum computation using cluster states. Phys. Rev. Lett. 93, 040503 (2004).  
11. Pirandola, S., Eisert, J., Weedbrook, C., Furusawa, A. & Braunstein, S. L. Advances in quantum teleportation. Nat. Photon. 9, 641-652 (2015).  
12. Valivarthi, R. et al. Quantum teleportation across a metropolitan fibre network. Nat. Photon. 10, 676-680 (2016).  
13. Ren, J.-G. et al. Ground-to-satellite quantum teleportation. Nature 549, 70-73 (2017).  
14. Gottesman, D. & Chuang, I. L. Demonstrating the viability of universal quantum computation using teleportation and single-qubit operations. Nature 402, 390-393 (1999).  
15. Wehner, S., Elkouss, D. & Hanson, R. Quantum internet: a vision for the road ahead. Science 362, eaam9288 (2018).  
16. Wang, J. et al. Integrated photonic quantum technologies. Nat. Photon. https://doi.org/10.1038/s41566-019-0532-1 (2019).  
17. Grice, W., U'Ren, A. & Walmsley, I. Eliminating frequency and space-time correlations in multiphoton states. Phys. Rev. A 64, 063815 (2001).  
18. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019).  
19. Vernon, Z. et al. Truly unentangled photon pairs without spectral filtering. Opt. Lett. 42, 3638-3641 (2017).  
20. Vernon, Z., Liscidini, M. & Sipe, J. E. No free lunch: the tradeoff between heralding rate and efficiency in microresonatorbased heralded single photon sources. Opt. Lett. 41, 788-791 (2016).  
21. Grassani, D. et al. Micrometer-scale integrated silicon source of time-energy entangled photons. Optica 2, 88-94 (2015).  
22. Faruque, I. I., Sinclair, G., Bonnaeu, D., Parity, J. G. & Thompson, M. G. On-chip quantum interference with heralded photons from two independent micro-ring resonator sources in silicon photonics. Opt. Express 26, 20379-20395 (2018).  
23. Bergamasco, N., Menotti, M., Sipe, J. E. & Liscidini, M. Generation of path-encoded Greenberger-Horne-Zeilinger states. Phys. Rev. Appl. 8, 054014 (2017).  
24. Ding, Y., Peucheret, C., Ou, H. & Yvind, K. Fully etched apodized grating coupler on the SOI platform with  $-0.58\mathrm{dB}$  coupling efficiency. Opt. Lett. 39, 5348-5350 (2014).  
25. Wang, J. et al. Chip-to-chip quantum photonic interconnect by path-polarization interconversion. Optica 3, 407-413 (2016).  
26. Greenberger, D. M., Horne, M. A., Shimony, A. & Zeilinger, A. Bell's theorem without inequalities. Am. J. Phys. 58, 1131-1143 (1990).  
27. Bourennane, M. et al. Experimental detection of multipartite entanglement using witness operators. Phys. Rev. Lett. 92, 087902 (2004). (8).  
28. Ma, Z.-H. et al. Measure of genuine multipartite entanglement with computable lower bounds. Phys. Rev. A 83, 062325 (2011).  
29. Bavaresco, J. et al. Measurements in two bases are sufficient for certifying high-dimensional entanglement. Nat. Phys. 14, 1032-1037 (2018).  
30. Kaneda, F. & Paul, K. High-efficiency single-photon generation via large-scale active time multiplexing. Sci. Adv. 5, eaaw8586 (2019).  
31. Tóth, G. & Apellaniz, I. Quantum metrology from a quantum information science perspective. J. Phys. A 47, 424006 (2014).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2019

# Data availability

The data represented in Figs. 2-4 are available as source data in the Supplementary Information. All other data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

# Code availability

The computer code used for data analysis is available on request from the corresponding author.

# Acknowledgements

We thank G.J. Mendoza and D. Bonneau for useful discussions. We thank W.A. Murray, M. Louit, E. Johnston, J.W. Silverstone and L. Kling for experimental assistance. We acknowledge support from the National Key R&D Program of China (2019YFA0308700, 2018YFB1107205), the Natural Science Foundation of China (nos 61975001, 61590933, 11527901 and 11825402), Beijing Natural Science Foundation (Z190005), Beijing Academy of Quantum Information Sciences (Y18G21) and Key R&D Program of Guangdong Province (2018B030329001). D.L., I.I.F., J.G.R. and M.G.T. acknowledge support from UK Quantum Technology Hub for Quantum Communication Technologies funded by EPSRC: EP/M013472/1; programme grant no. EP/L024020/1. Y.D. acknowledges support from Denmark SPOC (DNRF123), Villum Fonden, QUANPIC (00025298). I.I.F. acknowledges support from the FP7 Marie Curie Initial Training Network PICQUE (608062). M.H. acknowledges support from the Austrian Science Fund (FWF) through the START project (Y879-N27) and the joint Czech-Austrian project MultiQUEST (I 3053-N27, GF17-33780L). M.M. acknowledges support from the Engineering and

Physical Sciences Research Council (EPSRC; EP/P024114/1) and the QuantERA ERA-NET co-fund (FWF Project I3773-N36). K.R. acknowledges support from QuantERA. J.L.O. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies. M.G.T. acknowledges support from a European Research Council (ERC) starter grant (ERC-2014-STG 640079) and an EPSRC Early Career Fellowship (EP/K033085/1).

# Author contributions

All authors contributed to the discussion and development of the project. J.W. devised the concept of the experiment. Y.D. designed and fabricated the device. D.L., Y.D., I.I.F., J.W., S.P., D.B. and R.S. performed the experiment. J.W., D.L., Y.D., I.I.F., Y.-J.Q., Y.L., Y.-F.X., M.H., M.M., G.F.S. and X.Z. performed the theoretical analysis. K.R., J.L.O., J.G.R., Q.G., L.K.O., Y.D., J.W. and M.G.T. managed the project. The manuscript was written by J.W., D.L., Y.D. and I.I.F., with input from all other authors.

# Competing interests

M.T. is involved in developing quantum photonic technologies at PsiQuantum Corporation.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41567-019-0727-x.

Correspondence and requests for materials should be addressed to J.W.

Reprints and permissions information is available at www.nature.com/reprints.