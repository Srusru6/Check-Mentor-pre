# Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit

P. J. Shadbolt, M. R. Verde, A. Peruzzo, A. Politi, A. Laing, M. Lobino, J. C. F. Matthews, M. G. Thompson and J. L. O'Brien*

Entanglement is the quintessential quantum-mechanical phenomenon understood to lie at the heart of future quantum technologies and the subject of fundamental scientific investigations. Mixture, resulting from noise, is often an unwanted result of interaction with an environment, but is also of fundamental interest, and is proposed to play a role in some biological processes. Here, we report an integrated waveguide device that can generate and completely characterize pure two-photon states with any amount of entanglement and arbitrary single-photon states with any amount of mixture. The device consists of a reconfigurable integrated quantum photonic circuit with eight voltage-controlled phase shifters. We demonstrate that, for thousands of randomly chosen configurations, the device performs with high fidelity. We generate maximally and non-maximally entangled states, violate a Bell-type inequality with a continuum of partially entangled states, and demonstrate the generation of arbitrary one-qubit mixed states.

Quantum mechanics is known to allow fundamentally new modes of information processing $^{1,2}$ , simulation $^{3,4}$  and communication $^{5}$ , as well as enhanced precision of measurement and sensing $^{6,7}$ . Single photons provide a particularly promising physical system with which to develop such quantum technologies $^{8}$  due to their low-noise, high-speed transmission and ease of manipulation at the single-photon level, and have long been a leading approach by which to explore fundamental quantum science. The ability to precisely prepare, control and measure multi-photon states therefore holds considerable scientific and technological interest.

Recently it has been shown that it is possible to miniaturize quantum optical circuits using optical fibre $^{9,10}$  and integrated waveguide chips $^{11-17}$ . Monolithic waveguide circuits are inherently stable and can be many orders of magnitude smaller than their bulk optical equivalents, enabling the fabrication of multi-purpose, reconfigurable quantum circuits of unprecedented size and complexity. Control of a single phase shifter in this architecture has been used to manipulate time bin qubits $^{18}$  and up to four photons in two spatial modes $^{12}$ ; however, the large-scale reconfigurability required to generate arbitrary multi-photon states, including mixture and entanglement, has so far been out of reach.

Here, we report an integrated quantum photonic device composed of a two-qubit entangling gate, several Hadamard-like gates, and eight variable phase shifters. We demonstrate that it can be reconfigured with high fidelity across the complete space of possible configurations. We use this device to generate all four Bell states and perform quantum state tomography on them, to realize a Bell inequality 'manifold' (obtained from a continuum of measurement settings and states with a variable amount of entanglement) and to prepare and measure arbitrary single-photon mixed states.

# A reconfigurable quantum photonic circuit

The device described here is a silica-on-silicon entangling circuit (Fig. 1). Two photonic qubits  $A$  and  $B$  are encoded in pairs of

waveguides—path or dual rail encoding. The two qubits are input in the logical zero state  $|0_A\rangle \otimes |0_B\rangle$  (that is, a single photon in each upper waveguide) and are then acted upon by the quantum circuit shown in Fig. 1.

The first part of this circuit enables arbitrary state preparation of each qubit. The central part of the circuit implements a maximally entangling post-selected controlled-NOT (CNOT) logic gate<sup>1</sup> (the canonical two-qubit entangling gate). The CNOT gate is a post-selected linear optical gate that works with probability 1/9 (refs 19,20). The final stage of the circuit is the mirror image of the first stage and

![](images/e82912c85b2a07ecad7fe26ed30643bb8d1e6e09e670e8049619e19b296e0e0f.jpg)

![](images/d13ce185b81fedb0d49a145e8c672b55bf95edd16c0f5e36978489e880d42e4e.jpg)  
Figure 1 | A two-photon reconfigurable quantum circuit for generating, manipulating and detecting entanglement and mixture. a, Quantum circuit diagram consisting of pairs of Hadamard-like gates  $H' = e^{i\pi /2}e^{-i\pi \sigma_2 / 4}$ .  $H e^{-i\pi \sigma_z / 4}$  (where  $H$  is the usual Hadamard gate) and  $R_{z}(\phi) = e^{-i\phi \sigma_{z} / 2}$  rotations, that together implement  $\hat{U}_{i,j}(\phi_j,\phi_k)$ , and two  $H'$  gates and a controlled-SIGN or CZ gate, that together implement a CNOT. b, Waveguide implementation of the circuit composed of directional couplers and voltage-controlled thermo-optic phase shifters (marked as orange triangles). Directional couplers with splitting ratio  $\eta = 1 / 3$  are marked as dots; all other couplers have  $\eta = 1 / 2$ .

![](images/0a76800e9092f6acb97428d8aa4d9d36bcb911f1b90b6ad902720fde735e6a5e.jpg)  
Figure 2 | Classical and quantum interference fringes. a, Interference fringe measured at the two outputs of a single MZ interferometer on the chip. Experimental data are presented as black circles. Solid lines show fits. b, HOM dip, measured using a single MZ interferometer as a beamsplitter. Two-photon coincidence counts are shown as black circles. The red line shows a fit to these data with Gaussian and sinc components, due to quantum interference and determined by the spectral filters used, and a linear term accounting for slight decoupling of the source. The blue line shows a fit to the measured rate of accidental coincidences, with Gaussian and linear components. Error bars in both figures assume Poissonian statistics.

![](images/1060b6f17d89488c79a003a1ffa570a6e66aad55245eab30bece853ea6c34614.jpg)

is followed by measurement in the computational basis, which together enables projective measurement of each qubit in an arbitrary basis.

The initial and final stages of the device can be reconfigured, and are each implemented using two Mach-Zehnder (MZ) interferometers, each composed of two voltage-controlled thermal phase shifters and two directional couplers $^{12}$ . This architecture allows reconfigurable single-qubit unitary operations to be performed. In general, any unitary in  $SU(2)$  can be realized using three phase shifters and an MZ interferometer $^{21}$  as  $\hat{U}_{\mathrm{arb}}(\varphi_a,\varphi_b,\varphi_c) = e^{i\varphi_c\sigma_z / 2}e^{i\varphi_b\sigma_y / 2}e^{i\varphi_a\sigma_z / 2}$ . Here, we use two phase shifters per MZ to realize  $\hat{U}_i(\varphi_b,\varphi_c) = e^{-i\varphi_c\sigma_z / 2}e^{-i\varphi_b\sigma_y / 2}$  on each of the two input qubits, and  $\hat{U}_f = \hat{U}_i^\dagger$  on each output qubit of the CNOT gate. This is adequate for arbitrary, separable two-qubit state preparation and measurement, up to a global phase. Explicitly, the entire circuit shown in Fig. 1 implements the unitary matrix

$$
\left[ \hat {U} _ {f} \left(\phi_ {5}, \phi_ {6}\right) \otimes \hat {U} _ {f} \left(\phi_ {7}, \phi_ {8}\right) \right] \cdot \hat {U} _ {\mathrm {C N O T}} \cdot \left[ \hat {U} _ {i} \left(\phi_ {1}, \phi_ {2}\right) \otimes \hat {U} _ {i} \left(\phi_ {3}, \phi_ {4}\right) \right]
$$

where  $\hat{U}_{\mathrm{CNOT}} = |00\rangle \langle 00| + |01\rangle \langle 01| + |11\rangle \langle 10| + |10\rangle \langle 11|$  and  $\phi_{1-8}$  are set by the external control voltages.

![](images/59c8171887e33cf07ac49d53c3ec430c85e281a914020c87b06cdde95717f417.jpg)  
Figure 3 | Statistical fidelity of photon coincidence count rates. The histogram shows the distribution of statistical fidelity between ideal and measured coincidence probabilities, over 995 sets of eight randomly selected phases  $\tilde{\varphi}$ .  $96\%$  of phase settings produced statistics corresponding with theory to  $f > 0.97$ .

Benchmarking of reconfigurability

This circuit can be reconfigured to perform a number of different tasks, including arbitrary two-qubit pure (entangled) state preparation, arbitrary one-qubit (mixed) state preparation, state tomography, process tomography, and so on, as detailed in the following. To characterize the precision and accuracy with which the device can be reconfigured, we injected single photons into the device via a polarization-maintaining optical fibre array, and measured interference fringes across each of the eight phase shifters on the chip, finding an average contrast  $C = 0.988 \pm 0.008$  (see Methods for details). An example of a pair of such fringes is shown in Fig. 2a. From these measurements, we estimate the average accuracy in phase across all eight heaters to be  $\delta_{\phi} \approx 0.05$  rad (see Supplementary information).

In addition to high-fidelity classical interference, as demonstrated in Fig. 2a, the CNOT gate in the middle of the circuit shown in Fig. 1 relies on high-fidelity quantum interference $^{16}$ . Figure 2b shows a Hong-Ou-Mandel (HOM) dip $^{22}$  measured at a single MZ interferometer (that containing  $\phi_{1}$ ) on the chip. We produced degenerate photon pairs, sharing the same spectral and polarization mode, via type-I spontaneous parametric downconversion $^{23}$  (see Methods); these were injected into the two inputs A of the chip as shown in Fig. 1. The phase in the interferometer was then set to  $\pi / 2$ , rendering it equivalent to a  $1/2$  reflectivity beamsplitter, and the two-photon coincidence count  $N$  across the outputs of the interferometer was measured as a function of an off-chip optical delay between the arrival times of the two photons. The visibility of the dip  $V = (N_{\mathrm{classical}} - N_{\mathrm{quantum}}) / N_{\mathrm{classical}}$  was measured to be  $0.978 \pm 0.007$ , taking into account the measured rate of accidental coincidences $^{24}$ . Birefringence, mode mismatch and other such imperfections in the circuit could limit the visibility of this dip. The high visibility of the HOM dip therefore indicates the high quality of the device.

Having observed high-fidelity classical and quantum interference at individual MZ interferometers on the chip, we then used a stochastic method to characterize the operational performance of the quantum circuit as a whole, across the full space of possible configurations. We chose, at random, 995 vectors  $\tilde{\varphi}_j$  representing possible configurations of the device

$$
\tilde {\varphi} _ {j} = \left[ \phi_ {1} ^ {j}, \phi_ {2} ^ {j}, \dots , \phi_ {8} ^ {j} \right] \tag {1}
$$

with  $0 \leq \phi_i^j \leq 2\pi$ . Injecting photon pairs as shown in Fig. 1, the probability-theoretic fidelity  $f = \sum_{k} \sqrt{p_k \cdot p_k'}$  between experimentally measured coincidence probabilities at the output of the device ( $p_{00}, p_{01}, p_{10}, p_{11}$ ) and the ideal theoretical values ( $p_{00}', p_{01}'$ ,

![](images/c70c1fbbfab2980d40c5cf5dbad113abbc49bb75f4717f24cb60415acffa6bd5.jpg)

![](images/2ed38391592cc987ea24c7a1f84a93576be5886f005e4a8201c1bc8cb7be6346.jpg)

![](images/6184addd43e44bb33ea1fc6b21761df8cd8b796d1504326bc004b6d49ba3a169.jpg)  
Figure 4 | Bell states generated and characterized on-chip. a-d, Real parts of the density operators of the Bell states  $|\Phi^{+}\rangle$ ,  $|\Phi^{-}\rangle$ ,  $|\Psi^{+}\rangle$  and  $|\Psi^{-}\rangle$  (a,b,c,d, respectively).

![](images/86f51c1ab8be74187c92a8a4fd1b372ac3ebcf9f0fc18d25c75feab9d2c486ca.jpg)

$p_{10}^{\prime}, p_{11}^{\prime}$ ) was calculated for each  $\tilde{\varphi}_j$ . The statistical distribution of these fidelities is shown in Fig. 3a. The average fidelity across 995 configurations (equivalent to many truth tables in many bases) was measured to be  $0.990 \pm 0.009$ , with  $96\%$  of configurations  $\tilde{\varphi}_j$  producing photon statistics with  $f > 0.97$ . This result depends on simultaneous high-fidelity quantum and classical interference, as well as accurate and precise joint control of all eight phase controllers. Poor performance of any of these component parts would result in lower fidelity output for some subset of  $\{\tilde{\varphi}_j\}$ . The high-fidelity operation observed in these tests of reconfigurability bodes well for the operations described in the following.

# Generating and characterizing entanglement

Entangled states of quantum systems are the fundamental resource in quantum information and represent the most non-classical implication of the formalism of quantum mechanics. The circuit shown in Fig. 1 can be used to prepare a continuum of entangled, partially entangled, and separable states with only computational-basis product states as input.

To demonstrate this ability, we first prepared and analysed each of the four maximally entangled Bell states. Inputting the  $|0_A\rangle |0_B\rangle$  state as before, the state preparation stage of the circuit was used to generate each of the superposition states  $|\pm_A\rangle |0_B\rangle$ ,  $|\pm_A\rangle |1_B\rangle$ , where  $|\pm\rangle \equiv (|0\rangle \pm |1\rangle)/\sqrt{2}$ , at the input of the CNOT gate. The corresponding Bell states ( $|\Phi^{\pm}\rangle$  and  $|\Psi^{\pm}\rangle$  respectively) are ideally produced by the CNOT gate.

We used the arbitrary single-qubit measurement capability of the circuit to perform maximum-likelihood quantum state tomography  $(\mathrm{QST})^{25}$  on these four states: phase shifters  $\phi_{5 - 8}$  were used to implement each of the 16 measurements necessary to reconstruct the density operator of the state. The measured density matrices of all four Bell states are shown in Fig. 4, with quantum state fidelities  $F = \left(\mathrm{Tr}\sqrt{\sqrt{\rho_{\mathrm{th}}}\rho_{\mathrm{exp}}\sqrt{\rho_{\mathrm{th}}}}\right)^{2}$  of  $0.947\pm 0.002$ $0.945\pm 0.002$ $0.933\pm 0.002$  and  $0.885\pm 0.002$  , respectively.

# A Bell-type inequality manifold

The Clauser, Horne, Shimony and Holt (CHSH)[26] test of local hidden-variable models of quantum mechanics requires that the sum

$$
S = \left\langle \hat {A} _ {1} \hat {B} _ {1} \right\rangle + \left\langle \hat {A} _ {1} \hat {B} _ {2} \right\rangle + \left\langle \hat {A} _ {2} \hat {B} _ {1} \right\rangle - \left\langle \hat {A} _ {2} \hat {B} _ {2} \right\rangle \tag {2}
$$

satisfies the Bell-CHSH inequality  $-2 \leq S \leq 2$  for any local hidden-variable model, where  $\hat{A}_i$ ,  $\hat{B}_i$  are measurement operators chosen by two observers, Alice and Bob.

The Bell-CHSH experiment provides a well-known test for the presence of entanglement that we use here to examine the performance of the device, as it is reconfigured across a large parameter space. Specifically, we use  $\phi_{1 - 4}$  and the CNOT gate to prepare the state

$$
\left| \psi_ {\text {o u t}} \right\rangle = \frac {1}{2 \sqrt {2}} \left[ \left(1 - e ^ {i \alpha}\right) | 0 0 \rangle + \left(1 + e ^ {i \alpha}\right) | 1 1 \rangle \right] \tag {3}
$$

![](images/5d62bd949a5ce7cf7335379dec24d36f6e80e9d42156b475e05b8b9dc6b13714.jpg)  
Figure 5 | CHSH manifold. a, The Bell-CHSH sum  $S$ , plotted as a function of phases  $\alpha$  and  $\beta$ . In the  $\alpha$ -axis, the state shared between Alice and Bob is tuned continuously between product states at  $\alpha = 0$ ,  $\pi$  and maximally entangled states at  $\alpha = \pi /2$ ,  $3\pi /2$ . The  $\beta$ -axis shows  $S$  as a function of Bob's variable measurements, which can be thought of as two operator axes in the real plane of the Bloch sphere, fixed with respect to each other at an angle of  $\pi /2$  but otherwise free to rotate with angle  $\beta$  between 0 and  $2\pi$ . The blue curves show a projection of the manifold onto each axis. Yellow contours mark the edges of regions of the manifold that violate  $-2 \leq S \leq 2$ . Red lines on the axes also show this limit. b, Experimentally measured manifold. Data points are drawn as black circles. Data points that violate the CHSH inequality are drawn as yellow circles. The surface shows a fit to the experimental data.

![](images/9a2a2eb14e8a6a5a8c143aa7c5bc043c7b058bb77981b657691c9e47905e051f.jpg)

![](images/495ef800a98b02c914919faf0f483677c0e20da78b352c3f0b72e829b845067f.jpg)  
Figure 6 | Histogram showing the statistical distribution of quantum-state fidelity between 119 randomly chosen single-qubit target states and the corresponding mixed states generated and characterized on-chip. Inset:  $\Psi$  drawn in the Bloch sphere using 63 mixed states, again generated and characterized on-chip. These states are chosen from the real plane of the sphere for clarity. Note that each point is derived from a different bipartite partially entangled state.

where  $\alpha = \phi_1$ . By changing  $\alpha$  it is thus possible to tune continuously between two orthogonal maximally entangled states: for  $\alpha = 0, \pi$ ,  $|\psi_{\mathrm{out}}\rangle$  is a product state, and with  $\alpha = \pi /2, 3\pi /2$ ,  $|\psi_{\mathrm{out}}\rangle$  is the maximally entangled state  $1 / \sqrt{2} (|00\rangle \pm i|11\rangle)$  (up to a global phase). In the course of this preparation, we pass through a continuum of partially entangled states. To evaluate  $S$  we make four two-qubit measurements on the state emerging from the CNOT gate, which correspond to combinations of observables chosen by Alice and Bob. While Alice's two measurement settings,  $\phi_6 = \pi /4$ ,  $-\pi /4$ , do not change, Bob's two measurement settings are varied continuously, as  $\phi_8 = \beta$ ,  $\beta + \pi /2$ . We measured  $S(\alpha, \beta)$  for  $\alpha \in [0, 2\pi]$  and  $\beta \in [0, 2\pi]$ , with step size  $2\pi /15$ , producing the 'Bell manifold' shown in Fig. 5. We measured maximum and minimum values of  $S$  of  $2.49 \pm 0.03$  and  $-2.54 \pm 0.03$ , respectively. Errors were again determined by a Monte-Carlo technique, assuming Poissonian statistics.

To quantitatively compare the theoretical manifold with experimental data, we used the quantity

$$
R ^ {2} = 1 - \frac {\sum_ {i} \left(S _ {i} - T _ {i}\right) ^ {2}}{\sum_ {i} \left(S _ {i} - \bar {S}\right) ^ {2}} \tag {4}
$$

where  $S_{i}$  are experimentally measured values of the Bell-CHSH sum,  $\overline{S}$  is the average over  $S_{i}$ , and  $T_{i}$  are the theoretical values of  $S$  shown in Fig. 5a. In the ideal case,  $R^{2} = 1$ . For the data shown in Fig. 5b,  $R^{2} = 0.935$ .

# Generating and characterizing mixture

Mixture is often associated with noise or decoherence in quantum processes and its deliberate and controlled implementation is critical for characterization of devices; furthermore, it has been shown that quantum computing can be performed despite mixture $^{27}$ . More significantly, recent work has suggested that decoherence may play an important role in biological processes that exhibit quantum coherence $^{28,29}$ , and photonic waveguide systems show great promise for simulating these processes $^{30,31}$ . However, such simulations will require the controlled introduction of mixture.

By tracing over one of the two output photons, our device can prepare an arbitrary state of a single qubit including any amount of mixture<sup>32</sup>. The amount of entanglement in the two-qubit state

prepared by the first stage of the device determines the degree of mixture, which can range from zero (a pure state) to one (a maximally mixed state).

In general, the state

$$
\left| \psi_ {\text {o u t}} \right\rangle = \alpha \gamma \left| 0 _ {A} 0 _ {B} \right\rangle + \alpha \delta \left| 0 _ {A} 1 _ {B} \right\rangle + \beta \gamma \left| 1 _ {A} 1 _ {B} \right\rangle + \beta \delta \left| 1 _ {A} 0 _ {B} \right\rangle \tag {5}
$$

is generated after the CNOT gate in the circuit, where  $\alpha$ ,  $\beta$ ,  $\gamma$ ,  $\delta$  are complex parameters related to  $\phi_{1-4}$ . Tracing out the second qubit, we find the reduced density operator of qubit A,

$$
\begin{array}{l} \rho_ {A} = | \alpha | ^ {2} | 0 \rangle \langle 0 | + \alpha \beta^ {*} (\gamma \delta^ {*} + \delta \gamma^ {*}) | 0 \rangle \langle 1 | \tag {6} \\ + \beta \alpha^ {*} (\gamma \delta^ {*} + \delta \gamma^ {*}) | 1 \rangle \langle 0 | + | \beta | ^ {2} | 1 \rangle \langle 1 | \\ \end{array}
$$

By choosing  $\alpha, \beta, \gamma, \delta$ , by setting  $\phi_{1-4}$ , the amount of mixture in this reduced density matrix can be continuously varied between 0 and 1.

We randomly chose 119 target states with various amounts of mixture using the Hilbert-Schmidt measure[33], then generated each state and reconstructed its density matrix by maximum likelihood state tomography using phase shifters  $\phi_7$  and  $\phi_8$ . Figure 6 shows the fidelity of these reconstructed states. The average quantum state fidelity across all 119 states was measured to be  $0.98 \pm 0.02$ , with  $91\%$  of states having fidelity  $>0.95$ . We then chose 63 specific mixed states that mapped out the symbol  $\Psi$  inside the Bloch sphere, and generated them with high-fidelity (Fig. 6, inset).

We note that the device shown in Fig. 1 could be used to generate mixture by applying random voltages to phase shifters on a single qubit, without the need for entanglement. We chose to use the entanglement approach as a more demanding test of our device, demonstrating sufficient control to obtain the data shown in Fig. 6. An advantage of using the entanglement approach in practical applications is that it does not require pseudo-/quantum-random number generators.

# Discussion

Quantum information science and technology with photons will require circuits that are complex, stable and highly reconfigurable in a straightforward manner. High-fidelity production and measurement of states of arbitrary entanglement and mixture will be essential for the characterization of quantum devices, and will provide a reliable means with which to test the unique properties of quantum physics. The generation of mixed states may also be important in quantum photonic analogues of biochemical systems that rely on decoherence[28,29].

Although on-chip polarization encoding is possible $^{15}$ , the inherent interferometric stability of integrated optics makes path-encoding of qubits a natural choice, with the further advantage that encoding of higher-dimensional qubits $^{34}$  is immediately possible. This is in contrast with bulk optics, where two-level polarization encoding is more natural, and stable path encoding requires a considerable resource overhead. Furthermore, this architecture could be used to manipulate hyper-entanglement $^{35}$  encoded with multiple degrees of freedom $^{36,37}$ . Circuits such as the one presented here could be used in conjunction with adaptive (classical) algorithms to bypass the need for calibration of the phase shifters in particular applications. For example, repeated measurement and feedback onto the voltage-controlled phase shifters based on comparison of the output state with a desired target state could be used to reconfigure the circuit via a genetic algorithm.

# Methods

Device. The waveguide device was fabricated on a silicon wafer, upon which a  $16\mu \mathrm{m}$  layer of undoped silica was deposited to form the lower cladding of the waveguides. Waveguides  $(3.5\mu \mathrm{m}$  wide) were then patterned in a  $3.5\mu \mathrm{m}$  layer of silica doped with germanium and boron oxides. A  $16\mu \mathrm{m}$  layer of silica, doped with phosphorous and boron so as to be index-matched with the lower layer, constituted the upper

cladding. Resistive heaters and corresponding electric contacts were then patterned in metal on top of the chip using standard lithographic techniques. Dimensions of the chip were  $70\mathrm{mm}\times 3\mathrm{mm}$

Photon source. Degenerate pairs of  $808~\mathrm{nm}$  photons were generated by focusing a  $404~\mathrm{nm}$ ,  $60~\mathrm{mW}$  laser onto a 2-mm-thick bisumuth borate  $\mathrm{BiB_4O_6}$  (BiBO) nonlinear crystal, phase-matched for type I spontaneous parametric downconversion (opening angle of  $3^{\circ}$ ).

Photon pairs were spectrally filtered using  $3\mathrm{nm}$  full-width at half-maximum interference filters. The interference filters were designed with a central wavelength of  $808~\mathrm{nm}$  and were tilted to ensure that photon pairs were identically filtered. Photons were then collected into polarization maintaining fibre (PMF) using  $11\mathrm{mm}$  aspheric lenses. Typical two-photon coincidence count rates of  $100\mathrm{kHz}$  were achieved using  $\sim 60\%$  efficient, silicon-based avalanche photodiode single-photon counting modules (SPCM). The photons were then launched into the waveguide chip by butt-coupling arrays of PMF with  $250~{\mu\mathrm{m}}$  spacing (matched to the input and output waveguide pitch). Photons were also collected from the output of the chip using arrays of polarization maintaining fibre to PMF and detected with fibre-coupled SPCMs. A typical facet-to-facet coupling efficiency of  $\sim 60\%$  was achieved.

Calibration of phase shifters. Each thermal phase shifter  $\phi_{i}$  had a nonlinear phase voltage relationship given by

$$
\phi_ {i} \left(V _ {i}\right) = \alpha_ {i} + \beta_ {i} V ^ {2} + \gamma_ {i} V ^ {3} + \delta_ {i} V ^ {4} \tag {7}
$$

where  $V_{i}$  is the voltage applied across phase shifter  $i$  and  $\phi_{i}$  is the resulting phase shift.  $\alpha_{i}, \beta_{i}, \gamma_{i}$  and  $\delta_{i}$  are real numbers associated with the response of a particular heater. Each phase shifter can be seen to occupy one particular MZ interferometer in the circuit.  $\phi_{2}$  and  $\phi_{5}$  can be seen as acting on a single, lossy MZ interferometer.

Each phase shifter in the circuit was calibrated as follows. Bright light from an  $810~\mathrm{nm}$ ,  $1.3\mathrm{mW}$  laser was injected into one input port of each MZ interferometer, and the intensity at each output port was measured as a function of the voltage applied across the heater, which was swept linearly between  $0\mathrm{V}$  and  $7\mathrm{V}$ . This produced classical interference fringes, distorted by the nonlinear phase-voltage relationship (equation (7)). We then fitted the function

$$
I (V) = A \left(1 - C \cdot \cos^ {2} (\phi (V) / 2)\right) \tag {8}
$$

to each set of experimental data with  $A, C, \alpha, \beta, \gamma$  and  $\delta$  as fitting parameters. This yielded the complete (approximate) phase-voltage relationship for each heater. No evidence of crosstalk between phase shifters (due to thermal effects or otherwise) was observed in these experiments.

Single-photon fringes. We measured single-photon fringes for each phase shifter using photon pairs from the source. Injecting photons from one arm of the source into the chip, we counted coincidences between single photon events from a particular output of the interferometer, and those from the other arm of the source. This approach largely mitigates the contribution of SPCM dark counts. The fit shown in Fig. 2 has the form  $A(1 - C \cdot \cos^2(\phi / 2))$  where  $C$  is the fringe contrast and  $A$  is the amplitude. Each fringe is normalized with respect to its amplitude for clarity.

Received 11 May 2011; accepted 11 October 2011; published online 11 December 2011

# References

1. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
2. Deutsch, D. Quantum theory, the Church-Turing principle and the universal quantum computer. Proc. R. Soc. Lond. A 400, 97-117 (1985).  
3. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phy. 21, 467-488 (1982).  
4. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
5. Gisin, N. & Thew, R. Quantum communication. Nature Photon. 1, 165-171 (2007).  
6. Giovannetti, V., Lloyd, S. & Maccone, L. Quantum-enhanced measurements: beating the standard quantum limit. Science 306, 1330-1336 (2004).  
7. Dowling, J. P. Quantum optical metrology - the lowdown on high-N00N states. Contemp. Phys. 49, 125-143 (2008).  
8. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nature Photon. 3, 687-695 (2009).  
9. Clark, A. S., Fulconis, J., Rarity, J. G., Wadsworth, W. J. & O'Brien, J. L. All-optical-fiber polarization-based quantum logic gate. Phys. Rev. A 79, 030303 (2009).  
10. Hall, M. A., Altepeter, J. B. & Kumar, P. Ultrafast switching of photonic entanglement. Phys. Rev. Lett. 106, 053901 (2011).  
11. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
12. Matthews, J. C. F., Politi, A., Stefanov, A. & O'Brien, J. L. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nature Photon. 3, 346-350 (2009).

13. Smith, B. J., Kundys, D., Thomas-Peter, N., Smith, P. G. R. & Walmsley, I. A. Phase-controlled integrated photonic quantum circuits. Opt. Express 17, 13516-13525 (2009).  
14. Politi, A., Matthews, J. C. F. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
15. Sansoni, L. et al. Polarization entangled state measurement on a chip. Phys. Rev. Lett. 105, 200503 (2010).  
16. Laing, A. et al. High-fidelity operation of quantum photonic circuits. Appl. Phys. Lett. 97, 211109 (2010).  
17. Peruzzo, A., Laing, A., Politi, A., Rudolph, T. & O'Brien, J. L. Multimode quantum interference of photons in multiport integrated devices. Nature Commun. 2, 224 (2011).  
18. Honjo, T., Inoue, K. & Takahashi, H. Differential-phase-shift quantum key distribution experiment with aplanar light-wave circuit Mach-Zehnder interferometer. Opt. Lett. 29, 2797-2799 (2004).  
19. Ralph, T. C., Langford, N. K., Bell, T. B. & White, A. G. Linear optical controlled-NOT gate in the coincidence basis. Phys. Rev. A 65, 062324 (2002).  
20. Hofmann, H. F. & Takeuchi, S. Quantum phase gate for photonic qubits using only beam splitters and postselection. Phys. Rev. A 66, 024308 (2002).  
21. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
22. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
23. Burnham, D. C. & Weinberg, D. L. Observation of simultaneity in parametric production of optical photon pairs. Phys. Rev. Lett. 25, 84-87 (1970).  
24. Natarajan, C. M. et al. Operating quantum waveguide circuits with superconducting single-photon detectors. Appl. Phys. Lett. 96, 211101 (2010).  
25. James, D. F. V., Kwiat, P. G., Munro, W. J. & White, A. G. Measurement of qubits. Phys. Rev. A 64, 052312 (2001).  
26. Clauser, J. F., Horne, M. A., Shimony, A. & Holt, R. A. Proposed experiment to test local hidden-variable theories. Phys. Rev. Lett. 23, 880-884 (1969).  
27. Lanyon, B. P., Barbieri, M., Almeida, M. P. & White, A. G. Experimental quantum computing without entanglement. Phys. Rev. Lett. 101, 200501 (2008).  
28. Mohseni, M., Rebentrost, P., Lloyd, S. & Guzik, A. A. Environment-assisted quantum walks in photosynthetic energy transfer. J. Chem. Phys. 129, 174106 (2008).  
29. Plenio, M. B. & Huelga, S. F. Dephasing-assisted transport: quantum networks and biomolecules. New J. Phys. 10, 113019 (2008).  
30. Perets, H. B. et al. Realization of quantum walks with negligible decoherence in waveguide lattices. Phys. Rev. Lett. 100, 170506 (2008).  
31. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
32. Peters, N. A., Barreiro, J. T., Goggin, M. E., Wei, T. C. & Kwiat, P. G. Remote state preparation: arbitrary remote control of photon polarization. Phys. Rev. Lett. 94, 150502 (2005).  
33. Zyczkowski, K. & Sommers, H-J. Induced measures in the space of mixed quantum states. J. Phys. A. 34, 7111-7125 (2001).  
34. Rossi, A., Vallone, G., Chiuri, A., De Martini, F. & Mataloni, P. Multipath entanglement of two photons. Phys. Rev. Lett. 102, 153902 (2009).  
35. Ceccarelli, R., Vallone, G., De Martini, F., Mataloni, P. & Cabello, A. Experimental entanglement and nonlocality of a two-photon six-qubit cluster state. Phys. Rev. Lett. 103, 160401 (2009).  
36. Saleh, M. F., Di Giuseppe, G., Saleh, B. E. A. & Teich, M. C. Modal and polarization qubits in Ti:LiNbO $_3$  photonic circuits for a universal quantum logic gate. Opt. Express 18, 20475-20490 (2010).  
37. Saleh, M. F., Di Giuseppe, G., Saleh, B. E. A. & Teich, M. C. Photonic circuits for generating modal, spectral, and polarization entanglement. IEEE Photon. J. 2, 736-752 (2010).

# Acknowledgements

The authors thank N. Brunner, J. G. rarity and P. Ivanov for helpful contributions. This work was supported by the Engineering and Physical Sciences Research Council (EPSRC), the European Research Council (ERC), Intelligence Advanced Research Projects Activity (IARPA), the Leverhulme Trust, the Centre for Nanoscience and Quantum Information (NSQI), PHORBITECH, the Quantum Information Processing Interdisciplinary Research Collaboration (QIP IRC), and the Quantum Integrated Photonics (QUANTIP) project. J.L.O'B. acknowledges a Royal Society Wolfson Merit Award. M.L. acknowledges the Marie Curie International Incoming Fellowship.

# Author contributions

All authors contributed extensively to the work presented in this paper.

# Additional information

The authors declare no competing financial interests. Supplementary information accompanies this paper at www.nature.com/naturephotonics. Reprints and permission information is available online at http://www.nature.com/reprints. Correspondence and requests for materials should be addressed to J.L.O.