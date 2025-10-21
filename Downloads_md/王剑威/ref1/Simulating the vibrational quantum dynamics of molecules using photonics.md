# Simulating the vibrational quantum dynamics of molecules using photonics

Chris Sparrow<sup>1,2</sup>, Enrique Martín-López<sup>3</sup>, Nicola Maraviglia<sup>1</sup>, Alex Neville<sup>1</sup>, Christopher Harrold<sup>1</sup>, Jacques Carolan<sup>4</sup>, Yogesh N. Joglekar<sup>5</sup>, Toshikazu Hashimoto<sup>6</sup>, Nobuyuki Matsuda<sup>7</sup>, Jeremy L. O'Brien<sup>1</sup>, David P. Tew<sup>8</sup> & Anthony Laing<sup>1*</sup>

Advances in control techniques for vibrational quantum states in molecules present new challenges for modelling such systems, which could be amenable to quantum simulation methods. Here, by exploiting a natural mapping between vibrations in molecules and photons in waveguides, we demonstrate a reprogrammable photonic chip as a versatile simulation platform for a range of quantum dynamic behaviour in different molecules. We begin by simulating the time evolution of vibrational excitations in the harmonic approximation for several four-atom molecules, including  $\mathrm{H}_2\mathrm{CS}$ ,  $\mathrm{SO}_3$ ,  $\mathrm{HNCO}$ ,  $\mathrm{HFHF}$ ,  $\mathrm{N}_4$  and  $\mathrm{P}_4$ . We then simulate coherent and dephased energy transport in the simplest model of the peptide bond in proteins— $N$ -methylacetamide—and simulate thermal relaxation and the effect of anharmonicities in  $\mathrm{H}_2\mathrm{O}$ . Finally, we use multi-photon statistics with a feedback control algorithm to iteratively identify quantum states that increase a particular dissociation pathway of  $\mathrm{NH}_3$ . These methods point to powerful new simulation tools for molecular quantum dynamics and the field of femtochemistry.

Early electronic computers exploited analogies with acoustic, thermal or mechanical phenomena, such as capacitance for spring stiffness, to simulate a range of practically relevant physical systems. Whereas modern digital simulations have become versatile foundational tools in science and engineering, all classical computers are fundamentally inefficient at tackling exponentially complex microscopic behaviour such as the quantum dynamics of molecules $^{1,2}$ . A proposed solution is to engineer quantum mechanical components into devices that are then inherently capable of simulating quantum systems $^{3-6}$ . Here, we demonstrate how integrated quantum photonics can be used to develop simulation methods for molecular quantum dynamics, by building on the analogies between optical modes in waveguides and vibrational modes in molecules and between single photons and quantized vibrational excitations.

Advances in the control of ultrafast molecular dynamics have revealed the importance of quantum interference among vibrational modes in behaviour such as bond-selective chemistry $^{2}$ . In applying optimal control theory to a harmonic model of chained atoms $^{7}$ , it has been shown in principle how a control field could drive the dynamics of quantum interference between vibrational modes $^{8}$  to excite local bonds. However, laboratory demonstrations of selective bond dissociation required adaptive feedback control to put the principles into practice $^{9}$ . Further control over vibrational wavepackets has enabled selective dissociation governed by a single quantum of vibrational energy $^{10}$ , manipulation of individual molecules at ambient conditions $^{11}$ , preparations of coherent superpositions on sub-femtosecond timescales $^{12}$ , and single vibrational states of ultracold molecules $^{13}$ . Molecular dynamics are now observable on their ultrafast intrinsic timescale $^{14}$ .

The prospect of more sophisticated control with quantum states of light and for larger molecules increases the challenge of simulating dynamic behaviour. Light-matter interaction with squeezed states has been demonstrated experimentally in several contexts (see, for example, ref. 15); enhanced spectroscopy and the control of molecules with

multi-mode, multi-photon states has been shown theoretically (see, for example, ref. 16), with techniques for pulse shaping of quantum states of light also demonstrated (see, for example, ref. 17). Evolving a multi-excitation state across many vibrational modes is computationally inefficient even for the basic model in which normal modes are described as independent quantum harmonic oscillators. Owing to their bosonic nature, the probability amplitudes for input-output transitions among the modes are determined by matrix permanents, the calculation of which is generally extremely complex<sup>18</sup>. More detailed molecular models, for example, with anharmonic corrections to the potentials, are also likely to be computationally complex.

Quantum algorithms for the efficient simulation of Hamiltonian dynamics $^{4,19}$  have been a strong motivator for digital quantum computers, such as those that use trapped ions $^{20}$ . Promising digital algorithms for simulating reaction dynamics $^{21}$  and obtaining thermal rate constants $^{22}$  have been presented that harness the exponential quantum speed-up. Yet, achieving fault tolerance $^{23}$  and the high logical-gate counts $^{24}$  that enable these applications is extremely challenging. Ansatz-based methods, such as the variational approach for solving the eigenvalue problem $^{25}$ , have reduced demands, as demonstrated recently with superconducting qubits $^{26}$ , but the difficulties associated with applying such an approach to Hamiltonian dynamics have yet to be overcome. Analogue quantum simulations $^{6}$ , in which a quantum system of interest can be mapped directly onto a quantum technological platform, may enable practical advantages in the nearer-term.

Progress in photonic quantum technologies over the past decade has seen the introduction of on-chip processing of photonic quantum information $^{27-29}$ , full reprogrammability for linear optical circuitry $^{30}$ , and the integration of photon generation $^{31,32}$  and detection $^{33}$ . Solid-state single-photon sources $^{34}$  and high-efficiency detectors $^{35}$  have recently been demonstrated as a solution to achieving large numbers of photons. Ultimately, basic methods to correct for photon loss are likely to be required before photonic quantum simulations outperform

classical algorithms $^{36}$ , but the demands on error correction for specialized quantum simulators could be much lower than those for universal digital quantum simulators $^{37}$ . Here, our focus is on establishing programmable linear optical circuitry as a core capability for simulating the vibrational dynamics of the atoms within molecules.

# Simulation procedure

Diagonalizing the Hessian matrix of a molecule in mass-weighted coordinates provides its vibrational spectrum and normal modes, which define a Hamiltonian of independent quantum harmonic oscillators:

$$
\hat {H} = \sum_ {i} \hbar \omega_ {i} a _ {i} ^ {\dagger} a _ {i}
$$

where  $\hbar$  is the reduced Planck constant,  $\omega_{i}$  is the angular frequency of the  $i$ th mode, and  $a_{i}^{\dagger}$  and  $a_{i}$  are the bosonic creation and annihilation operators of the  $i$ th mode. The spatial localization of vibrational energy is important for understanding many molecular phenomena, such as energy transport and dissociation. We therefore consider a basis transformation

$$
a _ {i} ^ {\dagger} \rightarrow \sum_ {k} U _ {k i} ^ {\mathrm {L}} a _ {k} ^ {\dagger}
$$

where  $U^{\mathrm{L}}$  is a unitary matrix, to a set of modes localized around a single atomic site or chemical bond. Dynamics in the localized basis can then be simulated via the model Hamiltonian

$$
\hat {H} _ {\mathrm {L}} = \sum_ {k, j} H _ {k j} ^ {\mathrm {L}} a _ {k} ^ {\dagger} a _ {j}
$$

where

$$
H _ {k j} ^ {\mathrm {L}} = \sum_ {i} \hbar \omega_ {i} U _ {k i} ^ {\mathrm {L}} \overline {{U _ {j i} ^ {\mathrm {L}}}}
$$

and the overbar denotes complex conjugation.

This general model can be simulated directly for  $m$  vibrational modes of any given molecule with a linear optical chip that can be programmed to implement any unitary operation over  $m$  modes. Reconfiguring such a device to implement the unitary transfer matrix  $U(t_{i}) = \exp (-iH^{\mathrm{L}}t_{i} / \hbar)$  for a series of time steps  $\{t_i\}$  enables simulation of the Hamiltonian  $\hat{H}_{\mathrm{L}}$  on any initial multi-mode vibrational state via its mapping to a multi-mode optical input state. Here, we use a silica-on-silicon integrated photonic chip that is fully programmable over six waveguides via 30 thermo-optic phase shifters<sup>30</sup> to perform molecular simulations of up to six-mode vibrational systems. We simulate initial states of up to four vibrational quanta, with states of up to four single photons, produced from spontaneous parametric downconversion sources. Photons are detected with single-photon counting modules. The number and pattern of photons collected at the output of the optical modes for each circuit configuration are governed by the probabilities for the molecule to be found in the corresponding vibrational states at the corresponding time step.

# Vibrational dynamics of four-atom molecules

Thioformaldehyde  $(\mathrm{H}_2\mathrm{CS})$ , a key molecule for spectroscopic experiments, is shown in Fig. 1a with its normal-mode spectrum. The six localized vibrational modes of  $\mathrm{H}_2\mathrm{CS}$  comprise two CH stretch modes, two CH bend modes, a CS stretch mode and a wagging mode, which are mapped to our photonic chip from the normal-mode basis, as depicted conceptually in Fig. 1b. We initialized the simulation for the state  $|\mu\rangle \propto \mu |1_{\mathrm{CHs1}}, 1_{\mathrm{CHs2}}\rangle + \mu^2 |2_{\mathrm{CHs1}}, 2_{\mathrm{CHs2}}\rangle$  (with small squeezing parameter  $\mu$ ), which consists of multiple excitations superposed over the two CH stretch modes ('CHs1' and 'CHs2'), by injecting the two-mode squeezed vacuum state that was produced by the spontaneous parametric downconversion source, into the two waveguides that correspond to the CH stretch modes. Photons were collected over a series of circuit configurations that correspond to time steps of the  $\mathrm{H}_2\mathrm{CS}$

local-basis Hamiltonian. In Fig. 1c we display the experimentally simulated evolution of the probabilities for excitations to be found in only the CH stretch modes, in only the CH bend modes and shared between these stretch and bend modes, for the two-excitation (upper panel) and four-excitation subspace (lower panel).

Dynamics in the two-excitation subspace involve both excitations oscillating between stretch and bend modes via the intermediate state in which one excitation is in each of the subspaces. The  $L^1$  distance

$$
\mathcal {D} (\boldsymbol {p}, \boldsymbol {q}) = \frac {1}{2} \sum_ {i} | p _ {i} - q _ {i} |
$$

between the results for an experimentally simulated time step  $(\pmb{p})$  and the ideal distribution  $(q)$  is averaged over all time steps to give  $\bar{\mathcal{D}} = 0.06 \pm 0.03$ . In the four-excitation subspace, in which both of the stretch modes are initially doubly occupied, the experimentally simulated evolutions of probabilities for both stretch modes to remain doubly occupied, for both bend modes to become doubly occupied, and for combinations of one doubly occupied stretch mode and one doubly occupied bend mode are shown. The apparent damping of the oscillatory behaviour between these probabilities is attributable to the combinatorially growing space of multiple excitations available to the evolving state. The distance between the experimentally simulated and ideal evolutions for the full four-photon distributions, averaged over all time steps, is  $\bar{\mathcal{D}} = 0.16 \pm 0.07$ . The full distributions for these and all subsequent experiments are provided in Supplementary Information.

Because time is a programmable parameter in our simulator, we are able to study molecular vibrations whose evolution involves different timescales, such as the local CH stretch mode in  $\mathrm{H}_2\mathrm{CS}$ , which is a superposition of normal modes with lower and higher frequencies. The probability for a single excitation to remain localized in a CH stretch mode was simulated on two timescales that differ by an order of magnitude. Heralded single photons were injected into the mode that corresponds to a local CH stretch. The circuit was programmed to implement sets of unitary transformations that correspond to a short (30 fs) high-resolution window and that correspond to a longer (300 fs) low-resolution window, the behaviour of which can be observed by averaging over the high-resolution windows. In Fig. 1d we display data for these simulations, which exhibit both higher- and lower-frequency oscillations. Averaging over both evolutions gives a mean distance of  $\bar{\mathcal{D}} = 0.014 \pm 0.006$ .

Our six-mode simulator can explore the full space of vibrational dynamics for a general molecule of up to four atoms, as we demonstrate for  $\mathrm{P_4}$ ,  $\mathrm{SO}_3$ , HNCO, HFHF and  $\mathrm{N}_4$ . In Fig. 1e-i we show the time evolution of a single excitation initially prepared in a local stretch mode. The change in the occupation probability to a second, spectrally overlapped (coupled) local mode is plotted. We observe dynamics with varying characteristic times governed by the vibrational spectra of the molecules. Owing to its geometry and bonding structure,  $\mathrm{P_4}$  has the longest-period oscillations between opposing stretches, with  $\mathrm{SO}_3$  showing similar stretch-mode coupling behaviour on shorter timescales. By contrast, HNCO and HFHF display faster dynamics with increased mode coupling between hydrogen-bond stretches and bends. In Fig. 1i we show the dynamics of both a single excitation and two excitations initially prepared in stretch modes of  $\mathrm{N}_4$ . The additional structure in the vibrational spectrum and the introduction of multi-photon quantum interference results in a more complex time dependence of the detection probabilities. The average  $L^1$  distance over all of these experiments is  $\bar{\mathcal{D}} = 0.022 \pm 0.007$ .

# Decoherence and energy transfer in NMA

The flow of vibrational energy in molecules is a fundamental process for chemical reaction rates and functionality in biomolecules[38]. The vibrational quantum dynamics of a molecule within an environment can be described by the interplay of coherent unitary evolution and incoherent dephasing that results from random fluctuations of the

![](images/bea3cd3b8674b0a1058db1d496ff9e295d3d5f3756c22b78d61a531a1d9b589a.jpg)

![](images/fe0c871805ba24bec0d47fe107392d21a7e9de7918f770ea71d474ffa750700b.jpg)

![](images/b3ff71c444869152ced5c668967abdefdee6eacfb4612ae37f51c9c34a6990ac.jpg)

![](images/939bc25a642e2de243a9a5e1266a863aa653a7c9d3adcca4eab3df9d3f619140.jpg)

![](images/8bf243a464036a05836261e226f925ba93448acaae1fd65b3389d6f97db0f3da.jpg)

![](images/c9af912f5fc1b5cf220913c7fbae0ff9ce06ff3929bcf35e8278a2a4d26a6557.jpg)

![](images/b93e49402a18f522a706acceceadead45b1d3e2db297eeb3016da4723e21f7b1.jpg)

![](images/3b5f9c6ff2ab04416c4bdc31e4ff01b5bc2f63b3752287e97a3c992b3ede256e.jpg)

![](images/83d42baa752efe5a4338840f250d85f43f589fbf91c66835b85513365755414e.jpg)

![](images/abc7ffd8f3ab05987187ba3be27a5fa81f3f73c64af73ca9701d1b0f7fae9d2a.jpg)

![](images/f7c78c13021ecd61c98969d9cebdbf7007176d4b3ea56a5c431c4cebacdef907.jpg)

![](images/c5d1a793b214c0e5e35fad383d77c68a53bebd7af8d589fc051ae38433011515.jpg)  
Fig. 1 | Simulating the vibrational dynamics of four-atom molecules in the harmonic approximation. a, Schematic evolution of a localized CH stretch mode (diagonal black arrow) in  $\mathrm{H}_2\mathrm{CS}$ , with its composition from normal modes plotted below. b, The evolution of the normal modes  $(\exp (-i\hat{H} t / \hbar))$ , shown schematically in the center of the top layer, is unitarily mapped  $(U_{\mathrm{L}}$  and  $U_{\mathrm{L}}^{\dagger})$  to a set of local vibrational modes, shown schematically at the ends of the top layer. This transformation is then mapped to a time-dependent unitary transfer matrix  $(U(t)$ ; middle layer). Simulations of photonic states under this evolution are then implemented by a reconfigurable photonic chip (bottom layer). c, An initial superposition of two and four excitations evolving in the localized stretch modes is simulated by injecting a two-mode squeezed vacuum state into the corresponding optical modes and collecting photon statistics for the

![](images/462c53658f632df41ba7674e8d9c01df5c8228d8294113496a038bd43c10d9ee.jpg)  
sequence of simulated time steps. Top and bottom panels show results for the two- and four-excitation subspaces, respectively (see insets). d, Simulations on two timescales of the evolving probability for a single excitation to remain in a CH stretch mode. Blue squares represent the mean probability over a 30-fs window (as per left panel). e-i, The simulated evolution of a single excitation in  $\mathrm{P_4(e)}$ ,  $\mathrm{SO}_3(\mathbf{g})$ , HNCO (f) and HFHF (h) between a local stretch mode (black) and another coupled local mode (blue). The local modes are represented diagrammatically alongside the spectral intensities of the normal modes involved. For  $\mathrm{N_4(i)}$ , results are also shown for the evolution of two excitations. All data are plotted together with ideal theoretical curves; error bars displaying 1 s.d. from Poissonian statistics are very small.

![](images/7ba0fd5510309d2831c0fe65ad16845fde30652fd25105ec6fa4ee6c1233f861.jpg)

![](images/e42163ff8c29d49794b094bd52d29f3e7d8e1007d6a605901820d442cc495169.jpg)

vibrational frequencies—a process referred to as spectral diffusion.  $N$ -methylacetamide (NMA) is the simplest molecular model (Fig. 2a) of the peptide bond in proteins, where quantum coherence may have a role in energy transfer[39]. In this section, we simulate a model for intramolecular energy transport in NMA in the presence of dephasing.

We consider a subspace that spans six backbone vibrational modes, which support a basis of approximately localized vibrational modes, including two rocking modes (curved arrows in Fig. 2) and two stretch modes (straight arrows in Fig. 2). Uniform dephasing between all modes is achieved by a time-dependent statistical averaging over the set of experiments with transfer

![](images/052e1a9acde687b2084b9122743afc9aaa925f7192209a192dbcecc67bb58f8f.jpg)

![](images/3e62cfae4ac6661b7c5a9b988fc35fe314f51d946b223e8cdb0d380f7e08aee2.jpg)

![](images/77d13b31eb07b5d7471e738e6c4eedae6924fc51aadffb98331c83a8557a6831.jpg)  
Fig. 2 | Quantum energy transfer and dephasing in NMA. a, A six-mode vibrational subspace of the NMA molecule is considered, with the spectral components of three localized modes colour-coded as per the arrows in b. b, Experimental simulation results for the probability of a single excitation (black points) that is initially in a local rocking mode (black arrow) at one end of the molecule and its transfer (blue and grey points) to local modes at the opposite end (blue and grey arrows) when subject to a dephasing channel with  $T_{2} = 0.53$  ps. c, Experimental simulation results for the evolution of a two-excitation state (black points) that is initially in separate local modes (black arrows) and its probability (blue points)

![](images/3fd9d0dcd80685412fde436c144130c7d985c96e4edb9d04fda939a4cb55c16e.jpg)  
of being found bunched in the NH stretch mode (blue arrows) under the same dephasing channel. Solid lines represent theory. The dashed blue line plots a theoretical curve for distinguishable (or classical) excitations to be found bunched in the NH stretch mode. d, Experimental simulation results for the total probability of measuring a fully anti-bunched state of two excitations with the same initial state as for c (black points with solid black theory curve) and of measuring a fully anti-bunched state of three excitations initialized in the modes shown in b (black points with dot-dashed theory curve). All error bars represent 1-s.d. estimates from Poissonian statistics.

matrices  $U(t_{i},k) = U_{\mathrm{L}}Z(k)U_{\mathrm{L}}^{\dagger}\exp (-iH^{\mathrm{L}}t_{i} / \hbar)$ , where  $Z(k)$  are Heisenberg-Weyl matrices (defined in Supplementary Information) labelled by  $k$  and the average is taken over  $k$  at each time step.

Using a single photon, we simulated the probability for a single excitation initialized in a local rocking mode at one end of the molecule to be transferred to two localized modes (a rocking mode and a CC stretch mode) at the opposite end of the molecule. The experimental results shown in Fig. 2b show dynamics that are initially oscillatory, with vibrational energy transfer between the rocking modes at either end of the molecule via an intermediate CC stretch mode. The increasing effect of the suppression of coherence from dephasing results in evolution towards a steady state. Peak probabilities for energy to be localized at either end of the molecule are higher under quantum coherent dynamics than under purely ballistic classical dynamics. We used a  $T_{2}$  time constant of coherence decay of  $0.53\mathrm{ps}$ , but any time constant can be simulated by changing only the post-processing of data.

Simulating multiple excitations allows us to investigate the interplay of dephasing and quantum interference for multi-excitation energy transport. By injecting one photon into the waveguide that corresponds to the rocking mode and another photon into the waveguide that corresponds to the CC stretch mode, which are each localized at opposite ends of the NMA molecule (black arrows in Fig. 2c), we simulated the change in the probability for this state and for the state in which both excitations 'bunch' in an NH stretch mode (double blue arrows in Fig. 2c). The results in Fig. 2c show more complex oscillatory transfer between these bunched and anti-bunched states, which again tends towards a steady state. However, after full dephasing has occurred, the probability for two excitations to be bunched in the NH stretch mode is twice as high for excitations that behave as indistinguishable bosonic particles than for excitations that behave as distinguishable or classical particles (such as two excitations that pass through the molecule at different times).

For a given molecule, the probability that no bunching occurs (multiple excitations not localized around the same bond) generally decreases as the number of excitations increases $^{40}$ . In Fig. 2d the probability for the subspace of no-bunching events is simulated for two and three

excitations under fully coherent dynamics. The initial state for the two-excitation evolution is the same as in the previous example; the initial state for the three-excitation evolution comprises an excitation in each of the local modes shown in Fig. 2b. The average distances across all single-, two- and three-excitation distributions in these examples are  $0.017 \pm 0.005$ ,  $0.05 \pm 0.01$  and  $0.14 \pm 0.07$ , respectively.

# Vibrational relaxation in liquid water

We now consider extensions to the idealized model of uncoupled harmonic oscillators to account for more realistic situations, including energy dissipation and anharmonic potentials. We choose models for  $\mathrm{H}_2\mathrm{O}$  to demonstrate our techniques.

For a molecule that interacts with its environment, vibrational energy is exchanged via intra- and intermolecular coupling to other degrees of freedom, eventually leading to thermalization. This process is known as vibrational relaxation, and its pathways for  $\mathrm{H}_2\mathrm{O}$  remain an area of investigation[41,42]. Here we simulate the relaxation of  $\mathrm{H}_2\mathrm{O}$  via an amplitude-damping model (Fig. 3a).

We consider a Lindblad master equation, which results in a set of time-dependent Kraus operators that can be simulated via an ensemble of transfer matrices. This evolution cannot be described as a convex sum of unitary evolutions as in the previous section; however, the transfer matrices can be realized within a unitary matrix of twice the size, via unitary dilation[43]. Because  $\mathrm{H}_2\mathrm{O}$  has three vibrational modes, its three-dimensional (non-unitary) transfer matrices can be realized within a six-dimensional unitary matrix and implemented on our six-mode chip (Fig. 3b). We used experimentally measured relaxation times  $\{\Gamma_i\}$  for liquid water at room temperature[41] in the model.

We simulated the thermalization of an excitation in a local OH stretch mode via the symmetric bend normal mode to its ground state of no excitations. In Fig. 3c we show the probability of measuring the excitation in the two local stretch modes (left panel) and the symmetric bend mode (right panel). Oscillations between the two high-energy stretch modes decay as the population is transferred via the lower-energy bend mode to the ground state. The average  $L^1$  distance in these experiments was  $\bar{D} = 0.024 \pm 0.007$ .

![](images/db10d31230851ca748772d4f3ebdb5bf68f271a505acee25ea367b75a785c112.jpg)

![](images/62e448492889f55fc54de5088c880a73f5be24711daa2170b433ce8281c99b6d.jpg)

![](images/c4438633099815ce41f0aa2e4a5ce25b88fc362dfbd81daab944498ad8aebe18.jpg)  
Fig. 3 | Vibrational relaxation and anharmonic evolution for  $\mathrm{H}_2\mathrm{O}$ . a, Energy-level diagram for single-excitation harmonic levels and the ground state of  $\mathrm{H}_2\mathrm{O}$  (right) along with the spectral components of the two local OH stretch modes (black and grey) and the symmetric bend normal mode (blue) (left).  $\Gamma_{1,2,3}$  are the characteristic decay rates obtained from experiments. b, The open-system dynamics of vibrational relaxation, described by the Lindblad equation  $\dot{\rho} = \hat{\mathcal{L}} (\rho)$  where  $\rho$  is the vibrational state, can be simulated by statistically averaging the evolution under a set of linear operators implemented via unitary dilation. The Krauss operators in the localized basis,  $K(t)$ , are dilated into a unitary matrix by increasing the dimension (blocked-out parts of the matrix). c, Experimental results for the simulated evolution of the probability for a single excitation that is initially in one OH stretch mode (black points) to be found in the other stretch mode (grey points) and in the symmetric bend (blue points) under

![](images/54d89273f1f8665d8806e09c3d961433cd15191a41a14eb75f83147ab9acb06d.jpg)

# Anharmonic potentials in  $\mathrm{H}_2\mathrm{O}$

Potential energy surfaces of real molecules are anharmonic, and we now consider simulations in this regime, depicted in Fig. 3d. In addition to the second derivative in the Taylor expansion of the potential energy surface, as per the harmonic approximation, we now include all third derivatives and the semi-diagonal quartic derivatives. Applying vibrational perturbation theory yields a new Hamiltonian:

$$
\hat {H} _ {\mathrm {a}} = \hat {H} + \hbar \sum_ {i \leq j} \frac {x _ {i j}}{2} \sqrt {\omega_ {i} \omega_ {j}} \left(a _ {i} ^ {\dagger} a _ {i} + a _ {j} ^ {\dagger} a _ {j} + 2 a _ {i} ^ {\dagger} a _ {j} ^ {\dagger} a _ {i} a _ {j}\right)
$$

where  $\hat{H}$  is the harmonic Hamiltonian and  $x_{ij}$  are the perturbation-theory coefficients.

Implementing this Hamiltonian requires interactions between photons—a key challenge in quantum information processing. Demonstrations of enhanced single-photon interactions have required, for example, an artificial Kerr medium using superconducting circuits $^{44}$ , fibre coupling a single atom and a microresonator $^{45}$ , or coupling to a single quantum dot in a micropillar cavity $^{46}$ . Importantly, the interactions that are required to implement perturbative models such as  $\hat{H}_{\mathrm{a}}$  can be weaker than the fully entangling operations and controlled  $\pi$  phase gates that are used for universal quantum computing, with a potentially lower demand for reprogrammable nonlinear optics.

![](images/97a6c2cfc93330bc49219e7cdbd0586a96905813a5a4f480ae89ee4c0cf60bb9.jpg)

![](images/2f7d500d1d7ae32157d7baa85323b592406df696ba87c578aead77aa3cc6d352.jpg)

![](images/317cbc34838776f75a44081cd21587c08b0b2f6d3a47038e9f1eeea110d24735.jpg)  
relaxation dynamics. Solid lines are theoretical curves. d, Spectrum of two excitations in bunched (black) and anti-bunched (blue) local stretch modes for a harmonic (dashed) and anharmonic (solid) model. e, The anharmonic evolution is characterized by anharmonic potentials for single oscillators (top inset, where  $R$  is the nuclear distance and  $V(R)$  is the potential energy at  $R$ ) and cross-mode coupling between oscillators (bottom inset). These are implemented via a measurement-induced nonlinearity using an ancillary photon and modes. f, Experimental results for the simulated evolution of the probability for two excitations that are initially bunched in local stretch modes to be found in the anti-bunched state (left) and the bunched state (right) under both models (dashed, harmonic; solid, anharmonic). All error bars represent 1-s.d. estimates from Poissonian statistics.

Here, instead, we demonstrate an approach based on measurement-induced nonlinearities, which are in principle scalable for all-linear-optical quantum computing but involve a large overhead. It is possible to implement a conditional  $\pi$  phase shift on a two-photon Fock state using an ancillary photon and additional optical modes<sup>47</sup>. Using newly derived nonlinear phase-shift gates, we are able to implement arbitrary phase shifts between the zero-, one- and two-photon Fock states of an optical mode.

We simulate and compare harmonic and anharmonic models of vibration for  $\mathrm{H}_2\mathrm{O}$ , restricting to the subspace of stretch modes. Two photons injected together into the top mode of the chip serves to simulate two excitations initialized in a superposition of the eigenstates of the harmonic model that correspond to a local OH stretch. As shown in Fig. 3e, when simulating the anharmonic model, this input state is understood as the same superposition of the new energy eigenstates of  $\hat{H}_{\mathrm{a}}$ , while a third photon injected into the third optical mode serves as the ancillary system.

In Fig. 3f we show the results of simulating the probabilities for these two vibrational excitations to remain bunched or to anti-bunch, under harmonic  $(\hat{H})$  and anharmonic  $(\hat{H}_{\mathrm{a}})$  models. The difference in the detection patterns between the two models is a function of their different spectra (Fig. 3d). The probability of detecting a single excitation in each of the modes (anti-bunched; Fig. 3f, left panel) acquires a simple frequency shift for the anharmonic evolution that corresponds to the

adjusted energy levels (Fig. 3d, top panel). By contrast, the probabilities for the state to remain doubly occupied display markedly different dynamics between the harmonic and anharmonic cases (Fig. 3f, right panel). This is a result of the three vibrational eigenstates no longer being equally spaced in energy (Fig. 3d, bottom panel), which introduces new frequencies in the evolution. For this set of experiments, the average distances between the ideal and experimental distributions for the harmonic and anharmonic cases are  $0.02 \pm 0.01$  and  $0.06 \pm 0.02$ , respectively.

# Quantum simulation with adaptive feedback

Adaptive feedback control (AFC) is a practical laboratory technique for finding optimal control fields for molecules. AFC naturally incorporates laboratory constraints to design control fields that would not be found either analytically or through numerical simulation. Nevertheless, models idealized for quantum simulation could help to identify new possibilities for molecular control, could enable their comparison over a large number of molecules and could include quantum control fields.

Our goal is to use our simulator with an adaptive feedback loop from its quantum measurement statistics to design initial quantum states for a molecule that maximally achieve a particular task over a period of evolution. Our example molecule is ammonia  $(\mathrm{NH}_3)$ , a prototype for studying dissociation, including vibrationally mediated pathways, in which the states of its products  $(\mathrm{NH}_2 + \mathrm{H})$  depend on the prior vibrational state in the ground electronic state<sup>10</sup>.

Our model (Fig. 4b) simulates the preparation of a vibrational state in the electronic ground state of the molecule. We then obtain the vibrational state that results from an electronic excitation by projecting the vibrational modes of the ground state onto the vibrational modes of the excited state. We approximate this projection by a unitary

transformation between the modes  $U_{\mathrm{GE}}$ ; however, this transformation can in general be achieved via single-mode squeezing, displacement and linear optical transformations[48]. The evolution of the vibrational state of the electronically excited molecule is simulated under the harmonic Hamiltonian for the normal modes. By measuring the evolved state in a localized basis we identify three local NH stretch modes.

The aim of this simulation, depicted in Fig. 4c, is to let an AFC algorithm find the initial states of two vibrational excitations (in the molecule in the electronic ground state) that result in a maximal total probability of bunching in any of the three NH stretch modes (of the electronically excited molecule) over the first 10 fs of evolution, which we associate with a preferred dissociation pathway, while suppressing other bunched events, which we associate with other pathways. The algorithm begins with a trial state of two photons that simulates two excitations superposed randomly over five of the normal vibrational modes. State preparation, which is parameterized by the vector  $\theta$ , is optimized iteratively by programming the simulator to implement  $U(\theta, t_i) = U_{\mathrm{L}} \exp(-iHt_i / \hbar) U_{\mathrm{GE}}^{\dagger} U(\theta)$ , where  $U_{\mathrm{GE}}$  relates to the transformation between the ground- and excited-state normal modes and  $U_{\mathrm{L}}$  relates to the transformation between the excited-state normal and local modes.

An example experimental trial is shown in Fig. 4d. We used a Nelder-Mead simplex method to minimize the cost function

$$
C = - \alpha \sum_ {i} w _ {i} \Delta p _ {i} \in [ - 1, 1 ]
$$

where  $\Delta p_{i}$  is the difference between the probability of bunching in the NH stretch modes and the remaining modes at time step  $i$ ,  $w_{i}$  are weighting factors and  $\alpha$  is a normalization factor. The final value in Fig. 4d is  $C = -0.771$ , starting from a random initial state with  $C = +0.337$ . We repeated this experiment with six random initial states;

![](images/488b6889d2fbfdc5bc36e46da16e64c82fd6e4b44c62e2ddde6b5dfa420f8eb2.jpg)

![](images/b8caf02f64330050c9f791a42a0b63e639012252bff5c5ef3bc6ad18ae3c051f.jpg)

![](images/575ab32c7136edd935ec53246e73bd78c705105192bd5154db046db9b4db09e4.jpg)

![](images/7e5d368ff4adbdff176fea67b907861925b6f47bb9ca9dca4f23b08fd4b72c7b.jpg)  
Fig. 4 | AFC algorithm for a dissociation pathway in  $\mathrm{NH}_3$ . a, The spectral decomposition of an NH stretch mode in the electronic excited state of  $\mathrm{NH}_3$ . b, A two-excitation vibrational state, parameterized by  $\theta$ , is initialized in the ground-state vibrational modes  $(|\psi_{\mathrm{g}}(\theta,0)\rangle)$  of  $\mathrm{NH}_3$ . The electronic state  $(|\psi_{\mathrm{e}}(\theta,t)\rangle)$  is excited and the localization of vibrational energy is measured over time. These measurements are used to feedback to the state preparation to increase energy localization in NH stretch modes, promoting a particular dissociation pathway for this molecule c, This scenario is simulated via a parameterized unitary for state preparation  $U(\theta)$ , a transformation between the ground-state and excited-state modes  
$U_{\mathrm{GE}}^{\dagger}$ , evolution under the excited-state modes  $(\exp (-i\hat{H} t / \hbar))$  and measurement in a localized basis via  $U_{\mathrm{L}}$ . The resulting photon statistics are fed back through an AFC algorithm to set  $\theta$  for the next iteration (after calculating the cost function  $C$ ). d, The left panel displays an example set of experimental results that show the full distributions for bunching in the NH stretch modes (red), bunching in the remaining three localized modes (blue) and detection in anti-bunched patterns (yellow) for five time steps at iteration numbers 1 (bottom), 175 (middle) and 399 (top). The right panel shows  $-C$  measured at every iteration.

all resulted in similar final values of the cost function, with a mean of  $\overline{C} = -0.845$ .

# Discussion

We have introduced photonics as a platform for simulating the vibrational quantum dynamics of molecules within the harmonic, perturbatively anharmonic and Linblad models, with a photonic chip playing the part of a programmable molecule. Scaling up and extending these techniques to more involved Hamiltonians with highly anharmonic atomic potentials and electronic degrees of freedom, and to realize an advantage over classical simulation techniques<sup>36</sup>, presents important and interesting research directions.

Device errors that must be addressed include inevitable flaws in circuit fabrication and operation, photon distinguishability and photon loss. Although the precision that is required in the setting of any individual circuit parameter increases with dimension $^{49}$ , linear optical elements with extinction of more than 60 dB have been demonstrated $^{29}$ . Indistinguishability, or visibilities, between independent photons have been reported at  $95\%$  for on-chip sources $^{32}$  and at more than  $90\%$  for time bins of a solid-state photon source $^{34}$ . Although ultralow-loss integrated circuitry has been demonstrated $^{50}$ , photon loss is a fundamental error in photonics; basic methods that alleviate some of this error would provide substantial improvements in rates for the class of experiments demonstrated here. The development of programmable nonlinear optics at the quantum level is a key functionality for quantum technologies and remains an important challenge for the field. With modest progress in these areas, our approach could yield an early class of practical quantum simulations that operate beyond current classical limits.

# Data availability

The data shown in the plots and that support the findings of this study are available from the Research Data Repository of the University of Bristol at https://doi.org/10.5523/pris.2ymwd4m50qkt26mtrhpli3d1i.

Received: 11 October 2017; Accepted: 21 March 2018; Published online 30 May 2018.

1. Gatti, F. Molecular Quantum Dynamics. (Springer, Berlin, 2014).  
2. Brif, C., Chakrabarti, R. & Rabitz, H. Control of quantum phenomena: past, present and future. New J. Phys. 12, 075008 (2010).  
3. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phys. 21, 467-488 (1982).  
4. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
5. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nat. Phys. 8, 285-291 (2012).  
6. Georgescu, I. M., Ashhab, S. & Nori, F. Quantum simulation. Rev. Mod. Phys. 86, 153-185 (2014).  
7. Shi, S., Woody, A. & Rabitz, H. Optimal control of selective vibrational excitation in harmonic linear chain molecules. J. Chem. Phys. 88, 6870-6883 (1988).  
8. Shapiro, M. & Brumer, P. Coherent control of molecular dynamics. Rep. Prog. Phys. 66, 859-942 (2003).  
9. Assion, A. et al. Control of chemical reactions by feedback-optimized phase-shaped femtosecond laser pulses. Science 282, 919–922 (1998).  
10. Hause, M. L., Yoon, Y. H. & Crim, F. F. Vibrationally mediated photodissociation of ammonia: the influence of NH stretching vibrations on passage through conical intersections. J. Chem. Phys. 125, 174309 (2006).  
11. Brinks, D. et al. Visualizing and controlling vibrational wave packets of single molecules. Nature 465, 905-908 (2010).  
12. Alnaser, A. et al. Subfemtosecond steering of hydrocarbon deprotonation through superposition of vibrational modes. Nat Commun. 5, 3800 (2014).  
13. Tong, X., Winney, A. H. & Willitsch, S. Sympathetic cooling of molecular ions in selected rotational and vibrational states produced by threshold photoionization. Phys. Rev. Lett. 105, 143001 (2010).  
14. Wolter, B. et al. Ultrafast electron diffraction imaging of bond breaking in di-ionized acetylene. Science 354, 308-312 (2016).  
15. Clark, J. B., Lecocq, F., Simmonds, R. W., Augentado, J. & Teufel, J. D. Sideband cooling beyond the quantum backaction limit with squeezed light. Nature 541, 191-195 (2017).  
16. Dorfman, K. E., Schlawin, F. & Mukamel, S. Nonlinear optical signals and spectroscopy with quantum light. Rev. Mod. Phys. 88, 045008 (2016).  
17. Karpinski, M., Jachura, M., Wright, L. J. & Smith, B. J. Bandwidth manipulation of quantum light by an electro-optic time lens. Nat. Photon. 11, 53-57 (2017).

18. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. Theor. Comput. 9, 143-252 (2013).  
19. Berry, D. W., Childs, A. M., Cleve, R., Kothari, R. & Somma, R. D. Simulating Hamiltonian dynamics with a truncated Taylor series. Phys. Rev. Lett. 114, 090502 (2015).  
20. Lanyon, B. P. et al. Universal digital quantum simulation with trapped ions. Science 334, 57-61 (2011).  
21. Kassal, I., Jordan, S. P., Love, P. J., Mohseni, M. & Aspuru-Guzik, A. Polynomial-time quantum algorithm for the simulation of chemical dynamics. Proc. Nat'l Acad. Sci. USA 105, 18681-18686 (2008).  
22. Lidar, D. A. & Wang, H. Calculating the thermal rate constant with exponential speedup on a quantum computer. Phys. Rev. E 59, 2429-2438 (1999).  
23. Campbell, E. T., Terhal, B. M. & Vuillot, C. Roads towards fault-tolerant universal quantum computation. Nature 549, 172-179 (2017).  
24. Wecker, D., Bauer, B., Clark, B. K., Hastings, M. B. & Troyer, M. Gate-count estimates for performing quantum chemistry on small quantum computers. Phys. Rev. A 90, 022305 (2014).  
25. Peruzzo, A. et al. A variational eigenvalue solver on a photonic quantum processor. Nat. Commun. 5, 4213 (2014).  
26. Kandala, A. et al. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. Nature 549, 242-246 (2017).  
27. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
28. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nat. Commun. 2, 566 (2011).  
29. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).  
30. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
31. Silverstone, J.W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photon. 8, 104-108 (2014).  
32. Spring, J. B. et al. Chip-based array of near-identical, pure, heralded single-photon sources. Optica 4, 90-96 (2017).  
33. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).  
34. Wang, H. et al. Near-transform-limited single photons from an efficient solid-state quantum emitter. Phys. Rev. Lett. 116, 213601 (2016).  
35. Marsili, F. et al. Detecting single infrared photons with  $93\%$  system efficiency. Nat. Photon. 7, 210-214 (2013).  
36. Neville, A. et al. Classical boson sampling algorithms with superior performance to near-term experiments. Nat. Phys. 13, 1153-1157 (2017).  
37. Cubitt, T., Montanaro, A. & Piddock, S. Universal quantum Hamiltonians. Preprint at https://arxiv.org/abs/1701.05182 (2017).  
38. Leitner, D. M. Energy flow in proteins. Annu. Rev. Phys. Chem. 59, 233-259 (2008).  
39. Kobus, M., Nguyen, P. H. & Stock, G. Coherent vibrational energy transfer along a peptide helix. J. Chem. Phys. 134, 124518 (2011).  
40. Arkhipov, A. & Kuperberg, G. The bosonic birthday paradox. Geometry Topology Monogr. 18, 1-7 (2012).  
41. Lindner, J. et al. Vibrational relaxation of pure liquid water. Chem. Phys. Lett. 421, 329-333 (2006).  
42. Ramasesha, K., De Marco, L., Mandal, A. & Tokmakoff, A. Water vibrations have strongly mixed intra- and intermolecular character. Nat. Chem. 5, 935-940 (2013).  
43. Horn, R. A. & Johnson, C. R. Topics in Matrix Analysis 57-59 (Cambridge Univ. Press, Cambridge, 1991.  
44. Kirchmair, G. et al. Observation of quantum state collapse and revival due to the single-photon Kerr effect. Nature 495, 205-209 (2013).  
45. Shomroni, I. et al. All-optical routing of single photons by a one-atom switch controlled by a single photon. Science 345, 903-906 (2014).  
46. De Santis, L. et al. A solid-state single-photon filter. Nat. Nanotechnol. 12, 663-667 (2017).  
47. Knill, E., Laflamme, R. & Milburn, G. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
48. Huh, J., Guerreschi, G. G., Peropadre, B., McClean, J. R. & Aspuru-Guzik, A. Boson sampling for molecular vibronic spectra. Nat. Photon. 9, 615-620 (2015).  
49. Russell, N. J., Chakhmakhchyan, L., O'Brien, J. L. & Laing, A. Direct dialling of Haar random unitary matrices. New J. Phys. 19, 033007 (2017).  
50. Lee, H., Chen, T., Li, J., Painter, O. & Vahala, K. J. Ultra-low-loss optical delay line on a silicon chip. Nat. Commun. 3, 867 (2012).

Acknowledgements We thank A. Orr-Ewing and R. Santagati for helpful conversations, and J. Barton for assistance with figures. This work was supported by the Engineering and Physical Sciences Research Council (EPSRC), European Commission QUCHIP (H2020-FETPROACT-3-2014: quantum simulation) and the European Research Council (ERC). A.N. is grateful for support from the Wilkinson Foundation. J.C. is supported by EU H2020 Marie Sklodowska-Curie grant number 751016. Y.N.J. was supported by NSF grant number DMR-1054020. J.L.O'B. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies. Fellowship support from EPSRC is acknowledged by A.L. (EP/N003470/1).

Reviewer information Nature thanks A. Aspuru-Guzik and F. Gatti for their contribution to the peer review of this work.

Author contributions All authors contributed to discussions and project development. The concept of simulating molecular vibrations with photonics was proposed by A.L. The methodology for simulating evolutions in localized bases was developed by E.M.-L. and D.P.T., with input from A.L. and C.S. Chemical calculations were done by D.P.T., based on which C.S. and E.M.-L. developed and simulated datasets. Methods for simulating open-system dynamics were developed by C.S. with input from Y.N.J. and A.L. The concept of simulating anharmonics with nonlinear gates was proposed by A.L., with the methodology for finding the nonlinear phase shift gates developed by C.S. and A.N.; A.N. also developed this code. The concept of incorporating AFC into simulations was proposed by A.L., with methodology by C.S., N.Mar., A.N. and A.L.; A.N. also developed this code. The photonic chip was developed by N.Mat. and T.H. with input from A.L. and J.L.O'B. The experiment was built by C.H., J.C., N. Mat., N.Mar. and A.L. Data were collected by N.Mar., C.H., E.M.-L. and J.C.

Data were analysed by C.S., E.M.-L., N.Mar., A.N. and A.L. The manuscript was written by A.L., C.S. and E.M.-L. with input from D.P.T. and N.Mar. The project was conceived and managed by A.L.

Competing interests The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41586-018-0152-9.

Reprints and permissions information is available at http://www.nature.com/reprints.

Correspondence and requests for materials should be addressed to A.L.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.