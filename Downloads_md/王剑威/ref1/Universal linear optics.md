# QUANTUM OPTICS

# Universal linear optics

Jacques Carolan, $^{1}$  Christopher Harrold, $^{1}$  Chris Sparrow, $^{1,2}$  Enrique Martin-López, $^{3}$  Nicholas J. Russell, $^{1}$  Joshua W. Silverstone, $^{1}$  Peter J. Shadbolt, $^{2}$  Nobuyuki Matsuda, $^{4}$  Manabu Oguma, $^{5}$  Mikitaka Itoh, $^{5}$  Graham D. Marshall, $^{1}$  Mark G. Thompson, $^{1}$  Jonathan C. F. Matthews, $^{1}$  Toshikazu Hashimoto, $^{5}$  Jeremy L. O'Brien, $^{1}$  Anthony Laing $^{1*}$

Linear optics underpins fundamental tests of quantum mechanics and quantum technologies. We demonstrate a single reprogrammable optical circuit that is sufficient to implement all possible linear optical protocols up to the size of that circuit. Our six-mode universal system consists of a cascade of 15 Mach-Zehnder interferometers with 30 thermo-optic phase shifters integrated into a single photonic chip that is electrically and optically interfaced for arbitrary setting of all phase shifters, input of up to six photons, and their measurement with a 12-single-photon detector system. We programmed this system to implement heralded quantum logic and entangling gates, boson sampling with verification tests, and six-dimensional complex Hadamards. We implemented 100 Haar random unitaries with an average fidelity of  $0.999 \pm 0.001$ . Our system can be rapidly reprogrammed to implement these and any other linear optical protocol, pointing the way to applications across fundamental science and quantum technologies.

Photonics has been crucial in establishing the foundations of quantum mechanics (1) and more recently has pushed efforts in understanding new nonclassical computational possibilities. Typical protocols involve nonlinear operations, such as the generation of quantum states of light through optical frequency conversion (2, 3), or measurement-induced nonlinearities for quantum logic gates (4), together with linear operations between optical modes so as to implement core processing functions (5). Encoding qubits in the polarization of photons has been particularly appealing for the ability to implement arbitrary linear operations on the two polarization modes by using a series of wave plates (6). For path encoding, the same operations can be mapped to a sequence of beamsplitters and phase shifters. Because any linear optical (LO) circuit is described by a unitary operator, and a specific array of basic two-mode operations is mathematically sufficient to implement any unitary operator on optical modes (7), it is theoretically possible to construct a single device with sufficient versatility to implement any possible LO operation up to the specified number of modes.

Here, we report the realization of a six-mode device that is completely reprogrammable and universal for LO. The versatility of this universal LO processor (LPU) is demonstrated for several quantum information protocols, includ

$^{1}$ Centre for Quantum Photonics, H. H. Wills Physics Laboratory, and Department of Electrical and Electronic Engineering, University of Bristol, Merchant Venturers Building, Woodland Road, Bristol BS8 1UB, UK.  $^{2}$ Department of Physics, Imperial College London, London SW7 2AZ, UK.  $^{3}$ Nokia Technologies, Broers Building, 21 J. J. Thomson Avenue, Cambridge CB3 0FA, UK.  $^{4}$ NTT Basic Research Laboratories, Nippon Telegraph and Telephone (NTT) Corporation, 3-1 Morinosato-Wakamiya, Atsugi, Kanagawa 243-0198, Japan.  $^{5}$ NTT Device Technology Laboratories, NTT Corporation, 3-1 Morinosato-Wakamiya, Atsugi, Kanagawa 243-0198, Japan.

*Corresponding author. E-mail: anthony.laing@bristol.ac.uk

ing tasks that were previously not possible. We implemented heralded quantum logic gates at the heart of the circuit model of LO quantum computing (4) and new heralded entangling gates that underpin the measurement-based model of LO quantum computing (8-10), both of which are the first of their kind in integrated photonics. We performed 100 different boson sampling (11-15) experiments, with new verification protocols realized simultaneously. Last, we used multiparticle quantum interference to distinguish six-dimensional complex Hadamard operations, including newly discovered examples, in which full classification remains an open mathematical problem. The results presented required reconfiguration of this single device to implement  $\sim 1000$  experiments.

Isolated quantum mechanical processes, including lossless LO circuits acting on photons, preserve orthogonality between input and output states and are therefore described by unitary operators. Although the relevant mathematics for parameterizing unitary matrices has been known for at least a century (16), the theoretical formulation of a LO circuit in which an arbitrary unitary operator could be realized is more recent (7). The full space of  $m$ -dimensional unitary matrices (or unitaries) can be parametrized as a product of  $\approx m^2 / 2$  two-dimensional unitary primitives, each with two free parameters. Any given unitary then corresponds to a specific set of parameter values. An arbitrarily reconfigurable LO network would be realized by implementing these unitary primitives as two-mode Mach-Zehnder interferometers (MZIs) with two beamsplitters (or integrated directional couplers) and two phase shifters, so that any given LO network corresponds to a set of phase-shift values.

Such operation can be understood, with reference to the schematic shown in Fig. 1A, as a sequence of  $m - 1$  subunits  $D_{i}$  (Fig. 1A, di

agonal dashed boxes), each of which is guaranteed to enable transformation of the state of an input photon (Fig. 1A, left) in waveguide  $i$  to an arbitrary superposition of quantum mechanical amplitudes in all its output waveguides (Fig. 1A, right). The top MZI in each  $D_{i}$  is set to give the desired probability and phase for the input photon to output in waveguide  $i$ . The other parts of the quantum mechanical amplitude of the photon undergo similar operations in each successive MZI of a given  $D_{i}$  in order to set the amplitudes and phases in subsequent waveguides. Full reconfigurability is realized by feeding all output waveguides from one  $D_{i'}$  into all but the uppermost input waveguide of the following  $D_{i'-1}$  (17).

Realizing this scheme requires subwavelength stability and high-fidelity components to support both classical and quantum interference-possibilities opened up with integrated quantum photonics (18-26). Our LPU (Fig. 1B), made with planar lightwave circuit (PLC) technology (27, 28), comprises an array of 30 silica-on-silicon waveguide directional couplers with 30 electronically controlled thermo-optic phase shifters to form a cascade of 15 MZIs across six modes (fabrication details are available in the supplementary materials, section S1). This LPU can implement any six-dimensional unitary operator up to undetected output phases and any three-dimensional nonunitary matrix (17) by using operator dilation (29). Here, we focus on several protocols at the forefront of quantum information science and technology.

# Quantum gates

With the addition of single-photon sources and measurements, and rapid feed-forward of classical information, both the circuit (4) and measurement-based (8-10) models of digital quantum computing can be efficiently implemented with LO. Basic two-qubit processes are realized probabilistically with LO circuitry; therefore, a key requirement for scalability is that a successful operation is heralded by the detection of ancillary photons (ancillas) in order to signal that the processed photonic qubits are available for use in the larger architecture (30). These are typically referred to as "heralded gates."

We programmed our device to implement a new compact four-photon scheme suitable for measurement-based quantum computing, which generates the maximally entangled state of two photonic qubits upon the detection of another two ancilla photons (Fig. 2, A and B). For Bell states, measurements in common bases should be correlated, whereas measurements in different bases should be uncorrelated. We implemented both types of measurement (Fig. 2C), finding the mean statistical fidelity  $\mathcal{F}_{\mathrm{s}} = \sum_{i}\sqrt{p_{i}^{\mathrm{exp}}\cdot p_{i}^{\mathrm{th}}}$  (3I) between all four experimental  $p^{\mathrm{exp}}$  and theoretical  $p^{\mathrm{th}}$  probability distributions to be  $\mathcal{F}_{\mathrm{s}} = 0.966\pm 0.004$  (an explanation of error analysis is provided in the supplementary materials, section S2.1). These measurements were used to verify the entanglement of our state by calculating

$E = 1 / 2(\langle \sigma_x\otimes \sigma_x\rangle +\langle \sigma_z\otimes \sigma_z\rangle)$  finding a value of  $E = 0.673\pm 0.031$  , where  $E > 1 / 2$  witnesses entanglement (a full description of gate implementation and analysis is provided in the supplementary materials, section S3.3) (32).

Next, the device was reprogrammed to realize a quantum logic gate designed to be scalable for the circuit model of quantum computing (Fig. 2, D and E). The gate receives four photons: Two photons are each encoded with a qubit, and two photons act as ancillas. Detecting one photon in each of the two heralding modes signals the implementation of a controlled-NOT (CNOT) operation  $(4,33,34)$  between the two photonic qubits: The logical state of the target qubit is flipped  $(0\leftrightarrow 1)$  if the control qubit is in the state 1 and left unchanged if the control qubit is in state 0. We measured the logical truth table for this operation in the computational basis (Fig. 2F), finding its mean statistical fidelity averaged over all computational inputs to be  $\mathcal{F}_{\mathrm{s}} = 0.930\pm 0.003$  with the ideal case (supplementary materials, section S3.4).

Although the truth table measures the map between logical basis states, capturing complete phase information requires full process tomography, which we were able to perform

for an unheralded CNOT gate. With no ancillas, this unscalable gate requires two photons, which are consumed as part of its operation. Several examples of photonic chips specifically fabricated to implement such two-qubit gates (21, 35, 36) have been reported. To compare the performance of our universal processor against devices fabricated for a specific task, we implemented a two-photon unheralded CNOT gate (37-39) with single-qubit preparation and measurement capabilities (Fig. 2, G and H) and performed full quantum process tomography (Fig. 2I) (40). The process fidelity was found to be  $\mathcal{F}_{\mathrm{p}} = 0.909 \pm 0.001$  and the average gate fidelity was  $\mathcal{F}_{\mathrm{g}} = 0.927 \pm 0.001$  which is greater than those previously reported (gate implementation is provided in section S3.5 and quantum process tomography details are in section S2.4 of the supplementary materials) (21, 35, 41).

Combined with two-qubit operations, a small set of single-qubit gates (Fig. 2J), including the Hadamard  $(\hat{H})$  and  $\pi /8$ $(\hat{T})$  gates, are sufficient to realize a universal gate set for quantum computing (42). We implemented and performed full quantum process tomography for these two gates and for the three Pauli gates (Fig. 2K), finding an average process fidelity of  $F_{\mathrm{p}} = 0.992\pm 0.008$

In multiphoton experiments, deviations from unit fidelity are primarily caused by imperfections in the photon source, such as reduced quantum interference between different pair creation events (43), and higher-order terms in the spontaneous parametric down-conversion (SPDC) process. To omit these effects and measure the performance of our LPU directly, we used one- and two-photon ensembles to recover the raw transfer matrix  $M$  (44) implemented by the device, making no assumptions about its unitarity. We calculated the circuit fidelity  $\mathcal{F}_{\mathrm{c}} = \mathrm{Tr}(|U^{\dagger}\cdot M|^{2}) / 6$  with the intended unitary  $U$ . For the Bell state generator and the heralded and unheraldined CNOT, we found  $\mathcal{F}_{\mathrm{c}} = 0.943\pm 0.004$ ,  $0.941\pm 0.018$ , and  $0.939\pm 0.040$ , respectively (supplementary materials, section S2.3).

# Implementing boson sampling

The realization of a large-scale quantum computer that demonstrates an intrinsic exponential advantage over classical machines would be in conflict with a foundational tenet in computer science: the extended Church Turing thesis (ECT). The ECT conjectures that all realistic physical systems can be efficiently simulated with a probabilistic Turing machine, or classical computer.

![](images/0035b45da61ef0b1519a54040daed667f3f7549e4aa24cba226cf25c131062ab.jpg)  
Fig. 1. Universal LPU. (A) Decomposition of a fully parametrized unitary for an  $m$ -mode circuit to realize any LO operation. Subunitaries  $D_{i}$  consist of MZIs  $M_{i,j}$  built from phase shifters (yellow) and beam splitters, to control photon amplitudes  $(\alpha_{i,j})$  and phases  $(\varphi_{i,j})$ . (B) Multiphoton ensembles are generated via SPDC, comprising a BiBO crystal, dichroic mirrors (DM), and interference filter (IF), preceded by a pulsed Ti:sapphire laser and second harmonic generation from a BBO crystal. Photons are collected into polarization-maintaining fibers and delivered to the LPU via a packaged v-groove fiber  
array (VGA). The processor is constructed over six modes as a cascade of 15 MZIs, controlled with 30 thermo-optic phase shifters, set with a digital-to-analog converter (DAC), and actively cooled with a Peltier cooling unit. Photons are then out-coupled into a second packaged VGA and sent to six (or 12 with fiber splitters for single-mode photon-number resolving capability) SPADs and counted by using a 12-channel time-correlated single-photon counting module (TCSPC) (supplementary materials, section S1).

Measurement-based Quantum Computation

![](images/4f59f8961fe6254b514811a0bee13875ed6d590990fc7c0620960ad3f7d5e646.jpg)  
A

Circuit Model Quantum Computation

![](images/a737dda5767535aefeb4d3a54fc15b7093b7fef937310e6a60dac3436e33698b.jpg)  
B

![](images/c706cab9f4df90415e084fcb32d810825dea5adb43ceb1a0ebdce02551a8504b.jpg)  
C

![](images/71d9cdd18c5361a06d6af1be5369c5daa71b1a6b13ee62c597b551821efcc022.jpg)  
D

Quantum Process Tomography

![](images/dc42e8895dbd134172c00bf55a4ac3427760ecf336fb7e87577527b7983cd2ec.jpg)  
E  
F

![](images/a64a667e1e61298308ad489b689bf56a793e31b3204fed660ae09579f04ab401.jpg)

![](images/47bc233a17e2c40c6d12c646179419d4bd91245d5a3c55c1d2ac544d861d4621.jpg)  
G

![](images/2e211a6ef028ad61224b6fb01ed5efc7f9607f305815240090970bac57204fa1.jpg)  
J  
K

![](images/e1add34294dbbce67734c213211c4f79ef02b0d83231408e67dab9bfb12c5d3e.jpg)  
H

![](images/40e380bbedcdc4200db1f279b21b2a6a6b5874b0b9d256e8ccb78b3d37ec962d.jpg)  
Fig. 2. Gates for LO quantum computing. (A) The heralded Bell state generator receives four photons and emits two of them in a maximally entangled state upon detection of the remaining two. (B) Our LO protocol emits a Bell state on modes  $\{a, b\}$ , with input and heralding modes labeled  $|1\rangle$ . (C) Experimental data measuring Bell state correlations in a given basis (blue), with ideal theoretical values overlaid. Error bars assume Poissonian counting statistics. (D) The heralded CNOT gate is successfully implemented on the two photonic qubits, upon detection of the two ancilla photons. (E) The LO protocol realizing the heralded CNOT operation on the control  $c_{0,1}$  and target  $t_{0,1}$  qubits. (F) Experimental data showing the computational truth table, with the ideal theoretical truth table overlaid. (G) Quantum process tomography of

![](images/4146dfb3fdbdbb6f1557b8b254cd23a7908f5f50cf83f02f07b1eba692133e9c.jpg)

![](images/01a3d56211254b75b2e2443cad13cdec9496da69f38d717914aa9e97205409f6.jpg)

![](images/470ee6d7acf43336672bb90c412a33fabaf18f75c3587faa6e281c4d627b71a3.jpg)  
an unheralded two-qubit CNOT gate can be performed with the addition of arbitrary single-qubit preparation and measurement operations. (H) The LO circuit realizing the unheralded CNOT gate, with MZIs (inset) allowing single-qubit operations. (I) Experimentally determined process matrix, with ideal theoretical values overlaid. (J) An arbitrary single-qubit rotation  $R_{\hat{n}}(\theta)$  about some vector  $(\hat{n})$  on the Bloch sphere can be realized with a MZI and additional phase shifters. Three consecutive MZIs allow us to perform full-process tomography on any single-qubit operation. (K) Experimental data showing the measured process matrices for the three Pauli operations, the Hadamard gate  $(\hat{H})$ , and the  $\pi /8$  phase gate  $(\hat{T})$ . Experimental data are corrected for measured detector efficiencies.

![](images/eb379bdc2f01e2e0f97a5e2f44c5793caf8d3dbb136bbb78b8507ff33d9e41fd.jpg)  
1

![](images/8a03abc630c18490140e423818c3e5a0d0f3f123a0ffd8002ed1b47223309c2a.jpg)

![](images/dd9aa8127a68d3690c19921f60738c949e7a94afeab8bb1f23db845b1cfe06e0.jpg)  
H

![](images/cfb7dae8f3ec8ef1e8efecd3343e7e70cf8378df77c34ebf4d67f65ce7120951.jpg)  
Reflectivities

Designed for LO—with no requirement for quantum logic gates, qubit entangling operations, or number-resolved photon detection—boson sampling (11-15) is a quantum protocol that has been developed as a rapid route to challenge the ECT and demonstrate that quantum physics can be harnessed to provide fundamentally new and nonclassical computational capabilities.

Based on the foundations of computer science, boson sampling is a mathematical proof

(using plausible conjectures) that a many-photon state, when acted on by a large LO circuit set to implement a Haar-random unitary, will give rise to a probability distribution that cannot be efficiently sampled by a classical algorithm. Quantum interference among the photons (45) contributes to the pattern of the probability distribution. The classical intractability arises because the probability amplitude for each correlated photon detection event is given by a classically hard function, known as the "permanent"

(46), of the submatrix that describes a particular route of photons through the circuit. Experimentally, each detection event represents a sample drawn from that classically forbidden probability distribution.

Acting on three-photon ensembles, our device was programmed to implement 100 different boson sampling routines. Each circuit configuration was chosen randomly from the Haar measure, which was implemented via a direct parameterization of phase shifters (47), the probability

![](images/55ee998d070ec7de100fcc022421cd762c60b7bea004d96f1f1549770456f1e6.jpg)  
Boson Sampling

![](images/6a369bc98bdd0a21cd021f3777ce0b0db7d5b26f3f69b6d73dad0a4c3931a38f.jpg)

![](images/8902455e6224472ffa719303dbc092ea20b444dc91adbcb669ccc7fcd9d93952.jpg)

![](images/e600a48775f3403d39ff76f0f4c180df1bb551ab151e80f9c4ee1b41a970c8ef.jpg)

![](images/c9be9d9d3e663208ec035ad3647f4101f07fe5e287578c5c75cb2aabd70b5f58.jpg)

![](images/5089a4e69e3c3d2d128b8dc0cd1764e33e37f0b921af4610f1686fe4c0ffbf54.jpg)

![](images/c2e46b50eb83c1288ca2b9396e13ad6d05d538d4f7bf1a1510a04ae77591b3e6.jpg)  
Fig. 3. Boson sampling and complex Hadamard matrices. (A and B) A Haar random unitary can be directly implemented by choosing beamsplitter reflectivities [or equivalently MZI phases  $\alpha$  (inset 1)], and phase-shifter values  $\varphi$  (inset 2) from the probability density functions in (A). (C) A histogram of measured statistical fidelities for 100 three-photon boson sampling experiments, with one- and two-photon histograms inset ( $\overline{F}_{\mathrm{s}} = 0.999 \pm 0.001$ ,  $0.990 \pm 0.007$ , respectively). (D and E) The  $F_{6}^{(2)}$  two-parameter  $(\theta_{1}, \theta_{2})$  family of six-dimensional complex Hadamard matrices. (F) Dynamic updating of the confidence that six-photon detection events are sampled from a distribution

![](images/cba54d508b2a6894f67cf258ae7c3c3e805bebe4ee4e0f46d0f0436aaef5a8df.jpg)  
of indistinguishable (quantum, blue) or distinguishable (classical, red) photons. (G) Three-photon violations (v) of the zero-transmission law from scanning over  $F_{6}^{(2)}(\theta_{1},\theta_{2})$ . Experimental points in red are plotted with the ideal theoretical manifold. (H) Two-photon correlation manifolds in  $F_{6}^{(2)}$  for the probability of a given detection event [as color coded in (E)], with experimental points in red. (I and J) The measured probability for a given detection event when two photons are injected into an instance of  $G_{6}^{(4)}$  and  $S_{6}^{(0)}$ , with ideal theoretical black bars (error bars assume Poissonian counting statistics). Experimental data are corrected for measured detector efficiencies.

![](images/8a21c4dcadee3fac80da3c1a82af31f79d1ca6964f41cef28e9eba39e1f4997b.jpg)

density functions of which are displayed in Fig. 3A. For each implementation (Fig. 3B), detection events were counted for each of the 20 collision-free ways in which three photons can exit the six output ports of the device. A histogram of fidelities is displayed in Fig. 3C with statistics based on calculations of matrix permanents, with a mean statistical fidelity of  $\overline{\mathcal{F}}_{\mathrm{s}} = 0.950 \pm 0.020$ . These results demonstrate the performance of our LPU over many circuit configurations, randomly and unbiasedly chosen from the full space of all possible configurations.

# Verifying boson sampling

An open and important question, particularly in light of the ECT, is how to verify that boson sampling continues to be governed by the laws of quantum mechanics when experiments reach the scale that classical computers can no longer simulate (48-51). Unlike certain algorithms for digital quantum computers—including Shor's factoring algorithm (52), whereby the solution to a problem believed to be classically hard can be efficiently checked—there seems to be no analogous way to check that large-scale boson sampling is sampling from a probability distribution that arises from many-photon quantum interference.

Although it is likely that boson sampling is in principle mathematically unverifiable, methods have been proposed to gather supporting or circumstantial evidence for the correct operation of the protocol (51, 53, 54). The essence of these methods is to implement experiments that share basic quantum mechanical features with boson sampling, but where certain properties of the experimental output can be predicted and therefore checked. The zero-transmission law (ZTL) predicts that correlated photon detection for most of the exponentially growing number of configurations is strictly suppressed if the circuit is set to implement the Fourier transform (FT) on optical modes (Fig. 3, D and E) (55). This is known because the structure of the FT allows these matrix permanents to be efficiently evaluated without explicit calculation. Because large-scale many-photon quantum interference is at the core of the ZTL, it has been proposed as a certificate for the capability of a device to implement boson sampling (54).

The LPU was programmed to implement 16 examples of the  $F_{6}^{(2)}(\theta_{1},\theta_{2})$  two-parameter set of six-dimensional matrices, including  $F_{6}$  (the six-dimensional FT), which occurs at  $\theta_{\mathrm{b}},\theta_{2} = \pi ,0$  Using statistics from three-photon ensembles, the experimental violation of the ZTL was calculated as  $\nu = N_{\mathrm{s}} / N$  the ratio of the number of predicted suppressed events  $N_{s}$  to the total number of events  $N$  the results of which are plotted in Fig.3G alongside the theoretical manifold. The experimental points follow the shape of the manifold, with the minimal violation of the ZTL  $\mathrm{v}_{\mathrm{min}} = 0.319\pm 0.009$  occurring when  $F_{6}$  is implemented. The average ZTL violation of the nine points that are predicted to maximally violate is  $\overline{\mathbf{v}}_{\mathrm{max}} = 0.638\pm 0.029$  . Crucially, this verification protocol is implemented in the same device

and with the same procedure as that for the boson sampling experiments above.

# Six-photon verification

An essential requirement of boson sampling is that of indistinguishability among photons. With the LPU set to implement  $F_{6}$ , the six-photon state  $|3_1,3_2\rangle$  was injected, and six-photon statistics were counted with an all-fiber beam-splitter between each output mode and two single-photon avalanche diodes (SPADs) to give probabilistic number-resolved photon detection over a total of 12 SPADs. Although the complexity of states that are not one-photon-per-mode is less understood, the input state used here allows us to implement a protocol designed to verify indistinguishability among many photons with only a small number of detection events.

Bayesian model comparison was used to update, in real time, the confidence that events are sampled from a (precalculated) quantum probability distribution (arising from completely indistinguishable photons) or from a classical probability distribution (arising from completely distinguishable photons) (Fig. 3F) (51). After collecting 15 sixfold coincidence events, a confidence of  $P = 0.998$  was determined that these are drawn from a quantum (not classical) distribution.

# Complex Hadamard operations

The FT and  $F_{6}^{(2)}$  are examples in the more general class of complex Hadamard matrices (CHMs), which are related to mutually unbiased bases (56) and are of fundamental interest in quantum information theory (57). CHMs are defined as  $N \times N$  unitary matrices with entries of squared absolute value equal to  $1/N$ . Although this definition is straightforward, classification of these matrices is far from trivial and is concerned with identifying CHMs that are inequivalent up to pre- and postmultiplication with permutation matrices and diagonal unitaries (58). In the  $N = \{2, 3, 5\}$  case, all CHMs are equivalent to the respective FT matrix, whereas for  $N = 4$ , there exists a one-parameter equivalence class. Although a full classification of  $N = 6$  CHMs is unknown, it is currently conjectured that the set consists of an isolated matrix  $S_{6}^{(0)}$  that does not belong to any family (59) and a newly discovered four-parameter generic family  $G_{6}^{(4)}$  (60).

In LO experimental implementations, discrimination among CHMs can be accomplished via the observation of characteristic patterns of photonic quantum interference (61-64). Up until now, these observations have been too experimentally challenging for the six-dimensional case. We reconstructed correlation manifolds of two-photon detection events by scanning over the  $F_{6}^{(2)}$  matrices, displaying four (out of the 15 sets collected) in Fig. 3H. A mean statistical fidelity of  $\overline{\mathcal{F}}_{\mathrm{s}} = 0.979 \pm 0.007$  was found.

Last, we implemented an instance of  $G_6^{(4)}$  [that is not contained in  $F_6^{(2)}$ ] and  $S_6^{(0)}$  and observed predicted characteristic two-photon quantum interference patterns (Fig. 3, I and J, respectively), with respective statistical fidelities of  $\mathcal{F}_{\mathrm{s}} = 0.986 \pm 0.001$  and  $\mathcal{F}_{\mathrm{s}} = 0.998 \pm 0.001$ . The

intractability of calculating the permanents of certain CHMs is an interesting research line, as is the possibility of searching for new CHMs by using photonic statistics.

# Concluding remarks

Photonic approaches to quantum information science and technology promise new scientific discoveries and new applications. LO circuits lie at the heart of all of these protocols, and a single LPU device with the ability to arbitrarily "dial up" such operations promises to replace a multitude of existing and future prototype systems. Combining LPUs with existing higher-efficiency sources and detectors will expand their capabilities, and the development of LPUs with high-speed modulation (65) will enable the dynamically adaptive circuitry necessary for LO quantum computing. Integration of these components (66, 67) with larger low-loss circuits (68) will open up new avenues of research and application.

# REFERENCES AND NOTES

1. J.-W. Pan et al., Rev. Mod. Phys. 84, 777-838 (2012).  
2. Z.Y.Ou,S.F.Pereira,H.J.Kimble,K.C.Peng,Phys.Rev.Lett. 68,3663-3666 (1992).  
3. P. G. Kwiat et al., Phys. Rev. Lett. 75, 4337-4341 (1995).  
4. E. Knill, R. Laflamme, G. J. Milburn, Nature 409, 46-52 (2001).  
5. P. Kok et al., Rev. Mod. Phys. 79, 135-174 (2007).  
6. N. K. Langford, thesis, University of Queensland (2007).  
7. M. Reck, A. Zeilinger, H. J. Bernstein, P. Bertani, Phys. Rev. Lett. 73, 58-61 (1994).  
8. R. Raussendorf, H. J. Briegel, Phys. Rev. Lett. 86, 5188-5191 (2001).  
9. M. A. Nielsen, Phys. Rev. Lett. 93, 040503 (2004).  
10. D. E. Browne, T. Rudolph, Phys. Rev. Lett. 95, 010501 (2005).  
11. S. Aaronson, A. Arkhipov, in Proceedings of the ACM Symposium on Theory of Computing (ACM, New York, 2011), pp. 333-342.  
12. M. A. Broome et al., Science 339, 794-798 (2013)  
13. J. B. Spring et al., Science 339, 798-801 (2013).  
14. M. Tillmann et al., Nat. Photonics 7, 540-544 (2013).  
15. A. Crespi et al., Nat. Photonics 7, 545-549 (2013).  
16. A. Hurwitz, Nachr. Akad. Wiss. Gött. I. Math. Phys. KI. 1897, 71 (1897).  
17. D. A. B. Miller, Photon. Res. 1, 1 (2013)  
18. A. Politi, M. J. Cryan, J. G. Rarity, S. Yu, J. L. O'Brien, Science 320, 646-649 (2008).  
19. J. L. O'Brien, A. Furusawa, J. Vučković, Nat. Photonics 3, 687-695 (2009).  
20. G. D. Marshall et al., Opt. Exp. 17, 12546 (2009).  
21. A. Crespi et al., Nat. Commun. 2, 566 (2011).  
22. J. C. F. Matthews, A. Politi, A. Stefanov, J. L. O'Brien, Nat. Photonics 3, 346-350 (2009).  
23. B. J. Smith, D. Kundys, N. Thomas-Peter, P. G. R. Smith, I. A. Walmsley, Opt. Exp. 17, 13516 (2009).  
24. A. Laing et al., Appl. Phys. Lett. 97, 211109 (2010).  
25. A. Peruzzo et al., Science 329, 1500-1503 (2010).  
26. L. Sansoni et al., Phys. Rev. Lett. 108, 010502 (2012).  
27. A. Himeno, K. Kato, T. Miya, IEEE J. Sel. Top. Quantum Electron. 4, 913-924 (1998).  
28. H. Takahashi, Opt. Exp. 19, B173 (2011).  
29. P. R. Halmos, Summa Brasil. Math. 2, 125-134 (1950).  
30. S. Gasparoni, J.-W. Pan, P. Walther, T. Rudolph, A. Zeilinger, Phys. Rev. Lett. 93, 020504 (2004).  
31. M. Nielsen, I. Chuang, Quantum Computation and Quantum Information (Cambridge Univ. Press, 2010).  
32. H. Wunderlich, M. B. Plenio, J. Mod. Opt. 56, 2100-2105 (2009).  
33. T. C. Ralph, A. G. White, W. J. Munro, G. J. Milburn, Phys. Rev. A 65, 012314 (2001).  
34. R. Okamoto, J. L. O'Brien, H. F. Hofmann, S. Takeuchi, Proc. Natl. Acad. Sci. U.S.A. 108, 10067-10071 (2011).  
35. P. J. Shadbolt et al., Nat. Photonics 6, 45-49 (2011).  
36. H. W. Li et al., New J. Phys. 15, 063017 (2013).

37. T. C. Ralph, N. K. Langford, T. B. Bell, A. G. White Phys. Rev. A 65, 062324 (2002).  
38. H. Hofmann, S. Takeuchi, Phys. Rev. A 66, 024308 (2002).  
39. J. L. O'Brien, G. J. Pryde, A. G. White, T. C. Ralph, D. Branning, Nature 426, 264-267 (2003).  
40. I. L. Chuang, M. A. Nielsen, J. Mod. Opt. 44, 2455-2467 (1997).  
41. J. L. O'Brien et al., Phys. Rev. Lett. 93, 080502 (2004).  
42. Y. Shi, Quant. Inf. Comp. 3, 84 (2003).  
43. M. Tanida, R. Okamoto, S. Takeuchi, Opt. Exp. 20, 15275 (2012).  
44. A. Laing, J. L. O'Brien, http://arxiv.org/pdf/1208.2868v1.pdf (2012).  
45. C. K. Hong, Z. Y. Ou, L. Mandel, Phys. Rev. Lett. 59, 2044-2046 (1987).  
46. L. G. Valiant, Theor. Comput. Sci. 8, 189-201 (1979).  
47. N. J. Russell, J. L. O'Brien, A. Laing, http://arxiv.org/pdf/1506.06220.pdf (2015).  
48. C. Gogolin, M. Kliesch, L. Aolita, J. Eisert, http://arxiv.org/pdf/1306.3995v2.pdf (2013).  
49. S. Aaronson, A. Arkhipov, Quant. Inf. Comp. 14, 1383 (2014).  
50. N. Spagnolo et al., Nat. Photonics 8, 615-620 (2014).  
51. J. Carolan et al., Nat. Photonics 8, 621-626 (2014).

52. P. W. Shor, Proceedings of the 35th Annual Symposium on Foundations of Computer Science (Society for Industrial and Applied Mathematics, Philadelphia, PA, 1994), pp. 124-134.  
53. J. C. F. Matthews et al., Sci. Rep. 3, 1539 (2013).  
54. M. C. Tichy, K. Mayer, A. Buchleitner, K. Mølmer, Phys. Rev. Lett. 113, 020502 (2014).  
55. M. C. Tichy, M. Tiersch, F. de Melo, F. Mintert, A. Buchleitner, Phys. Rev. Lett. 104, 220405 (2010).  
56. I. Bengtsson et al., J. Math. Phys. 48, 052106 (2007).  
57. R. F. Werner, J. Phys. Math. Gen. 34, 7081-7094 (2001).  
58. W. Tadej, K. Žyczkowski, Open Syst. Inf. Dyn. 13, 133-177 (2006).  
59. T. Tao, Math Res. Lett. 11, 251-258 (2003).  
60. F. Szollosi, J. Lond. Math. Soc. 85, 616-632 (2012).  
61. K. Mattle, M. Michler, H. Weinfurter, A. Zeilinger, M. Zukowski, Appl. Phys. B 60, S111 (2004).  
62. A. Peruzzo, A. Laing, A. Politi, T. Rudolph, J. L. O'Brien, Nat. Commun. 2, 224 (2011).  
63. A. Laing, T. Lawson, E. Martin López, J. L. O'Brien, Phys. Rev. Lett. 108, 260505 (2012).  
64. N. Spagnolo et al., Nat. Commun. 4, 1606 (2013).  
65. D. J. Thomson et al., IEEE Photon. Technol. Lett. 24, 234-236 (2012).  
66. J. W. Silverstone et al., Nat. Photonics 8, 104-108 (2013).

67. J. P. Sprengers et al., Appl. Phys. Lett. 99, 18110 (2011).  
68. S. Sohma et al., Optical Communications, 2006. ECOC 2006. European Conference on (IEEE, New York, 2006), pp. 1-2.

# ACKNOWLEDGMENTS

The authors acknowledge support from the Engineering and Physical Sciences Research Council (EPSRC), the European Research Council (ERC), including BBOI, QUCHIP (H2020-FETPROACT-3-2014: Quantum simulation), PIQUE (FP7-PEOPLE-2013-ITN), the Centre for Nanoscience and Quantum Information (NSQI), the U.S. Army Research Office (ARO) grant W911NF-14-1-0133, and the U.S. Air Force Office of Scientific Research (AFOSR). J.C.F.M. was supported by a Leverhulme Trust Early Career Fellowship. J.L.O'B. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies.

# SUPPLEMENTARY MATERIALS

www.sciencemag.org/content/349/6249/711/suppl/DC1

Materials and Methods

Tables S1 to S5

References (69-72)

16 April 2015; accepted 26 June 2015

Published online 9 July 2015

10.1126/science.aab3642

# REPORTS

# MAGNETISM

# Imaging and control of ferromagnetism in LaMnO $_3$ /SrTiO $_3$  heterostructures

X. Renshaw Wang, $^{1*}$ †‡ C. J. Li, $^{2,3}$ † W. M. Lu, $^{2}$  T. R. Paudel, $^{4}$  D. P. Leusink, $^{1}$  M. Hoek, $^{1}$  N. Poccia, $^{1}$  A. Vailionis, $^{5}$  T. Venkatesan, $^{2,3,6,7*}$  J. M. D. Coey, $^{2,8}$  E. Y. Tsymbal, $^{4}$  Ariando, $^{2,6}$  H. Hilgenkamp $^{1}$

Oxide heterostructures often exhibit unusual physical properties that are absent in the constituent bulk materials. Here, we report an atomically sharp transition to a ferromagnetic phase when polar antiferromagnetic  $\mathrm{LaMnO_3}$  (001) films are grown on  $\mathrm{SrTiO_3}$  substrates. For a thickness of six unit cells or more, the  $\mathrm{LaMnO_3}$  film abruptly becomes ferromagnetic over its entire area, which is visualized by scanning superconducting quantum interference device microscopy. The transition is explained in terms of electronic reconstruction originating from the polar nature of the  $\mathrm{LaMnO_3}$  (001) films. Our results demonstrate that functionalities can be engineered in oxide films that are only a few atomic layers thick.

Modern thin-film deposition techniques enable the synthesis of complex oxide thin films with unit cell (uc)-level control over the thickness. Remarkably sharp phase transitions have been discovered

in several systems upon increasing film thickness (1-6). The most prominent example is the two-dimensional electron gas formed between insulating thin films of  $\mathrm{LaAlO_3}$  and insulating  $\mathrm{TiO_2}$ -terminated  $\mathrm{SrTiO_3}$  (STO) substrates, which occurs at a critical  $\mathrm{LaAlO_3}$  thickness of 4 uc (2). The possibility of selecting a different electronic or magnetic phase by adding a single layer of perovskite unit cells, with a lattice parameter of about  $0.4\mathrm{nm}$ , offers tantalizing opportunities for nanostructured electronic and spintronic devices.

Because various interesting properties have been demonstrated in  $\mathrm{LaMnO_3}$  (LMO) bulk, thin films, and multilayers, ranging from orbital waves to its use as a catalyst for water splitting (7-11), LMO is an ideal candidate for observing control of functionalities in oxide heterostructures. It is a Mott insulator with an orthorhombic  $Pbnm$  structure, based on a  $\sqrt{2} a_{0}$ ,  $\sqrt{2} a_{0}$ ,  $2a_{0}$  unit cell where  $a_0\approx 0.39\mathrm{nm}$  is the elementary perovskite uc parameter. In stoichiometric LMO, La and Mn are both  $3+$  ions. The oxide is therefore a polar material that contains alternately charged  $(\mathrm{LaO})^{1+}$  and  $(\mathrm{MnO}_2)^{1-}$  layers.  $\mathrm{Mn}^{3+}$ , with electronic configuration  $t_{2g}^3 e_g^{-1}$  and spin  $S = 2$ , is a Jahn-Teller ion. If LMO had a perfect cubic perovskite structure, one would expect a conducting ground state,

owing to the mobility of the unpaired electron in the degenerate  $e_{\mathrm{g}}$  band. However, the  $e_{\mathrm{g}}$  orbital degeneracy is lifted by the Jahn-Teller effect, and distorted  $\mathrm{MnO_6}$  octahedra line up with alternating long and short Mn-O bonds in the  $a - b$  plane, leading to orbital ordering, which results in electron localization (12). As a result of superexchange (13), the compound is an A-type antiferromagnet, with Mn spins ferromagnetically aligned within each plane and alternate (001) planes aligned antiferromagnetically. The Néel temperature is  $\sim 140~\mathrm{K}$ . The antiferromagnetism is slightly canted in the bulk to produce a weak ferromagnetic moment of  $\sim 0.18\mu_{\mathrm{B}}$  (where  $\mu_{\mathrm{B}}$  is the Bohr magneton) per uc (14-16) that is attributed to the antisymmetric Dzyaloshinskii-Moriya (DM) interaction associated with rotation of the  $\mathrm{MnO_6}$  octahedra. In thin films, ferromagnetism with a Curie temperature of  $\sim 115\mathrm{K}$  (17) accompanied by insulating behavior is often observed. The origin of this ferromagnetism is still unclear, but in addition to the above-mentioned DM mechanism, defects and epitaxial strain can be important factors (17-20). Here, we report a controllable monolayer-critical magnetic effect, whereby a uniform ferromagnetic state appears in  $\mathrm{LaMnO_3}$  at a critical thickness of 6 uc.

$^{1}$ MESA+ Institute for Nanotechnology, University of Twente, Enschede, Netherlands.  $^{2}$ NUSNNI-Nanocore, National University of Singapore, Singapore.  $^{3}$ NUS Graduate School for Integrative Sciences and Engineering, National University of Singapore, Singapore.  $^{4}$ Department of Physics and Astronomy and Nebraska Center for Materials and Nanoscience, University of Nebraska, Lincoln, NE, USA.  $^{5}$ Geballe Laboratory for Advanced Materials, Stanford University, Stanford, CA, USA.  $^{6}$ Department of Physics, National University of Singapore, Singapore.  $^{7}$ Department of Electrical and Computer Engineering and Department of Materials Science and Engineering, National University of Singapore, Singapore.  $^{8}$ School of Physics and Centre for Research on Adaptive Nanostructures and Nanodevices, Trinity College, Dublin, Ireland.

*Corresponding author. E-mail: wang.xiao@utwente.nl (X.R.W.); venky@nus.edu.sg (T.V.) †These authors contributed equally to this work. ‡Present address: Massachusetts Institute of Technology, Cambridge, MA, USA.

![](images/dcd6f88a6e8cfcc5607a4f0e5c16cb72cfd1947a6a9f4cb1801d9aba2f17875c.jpg)

# Universal linear optics

Jacques Carolan, Christopher Harrold, Chris Sparrow, Enrique Martin-Lopez, Nicholas J. Russell, Joshua W. Silverstone, Peter J. Shadbolt, Nobuyuki Matsuda, Manabu Oguma, Mikitaka Itoh, Graham D. Marshall, Mark G. Thompson, Jonathan C. F. Matthews, Toshikazu Hashimoto, Jeremy L. O'Brien and Anthony Laing (July 9, 2015)  
Science 349 (6249), 711-716. [doi: 10.1126/science.aab3642] originally published online July 9, 2015

Editor's Summary

# Complex quantum optical circuitry

Encoding and manipulating information in the states of single photons provides a potential platform for quantum computing and communication. Carolan et al. developed a reconfigurable integrated waveguide device fabricated in a glass chip (see the Perspective by Rohde and Dowling). The device allowed for universal linear optics transformations on six wave-guides using 15 integrated Mach-Zehnder interferometers, each of which was individually programmable. Functional performance in a number of applications in optics and quantum optics demonstrates the versatility of the device's reprogrammable architecture.

Science, this issue p. 711; see also p. 696

This copy is for your personal, non-commercial use only.

Article Tools Visit the online version of this article to access the personalization and article tools: http://science.sciencemag.org/content/349/6249/711

Permissions Obtain information about reproducing this article: http://www.sciencemag.org/about/permissions.dtl

Science (print ISSN 0036-8075; online ISSN 1095-9203) is published weekly, except the last week in December, by the American Association for the Advancement of Science, 1200 New York Avenue NW, Washington, DC 20005. Copyright 2016 by the American Association for the Advancement of Science; all rights reserved. The title Science is a registered trademark of AAAS.