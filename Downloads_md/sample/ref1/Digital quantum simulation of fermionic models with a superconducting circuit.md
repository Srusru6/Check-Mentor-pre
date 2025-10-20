ARTICLE

Received 16 Mar 2015 | Accepted 24 May 2015 | Published 8 Jul 2015

DOI: 10.1038/ncomms8654

OPEN

# Digital quantum simulation of fermionic models with a superconducting circuit

R. Barends<sup>1</sup>, L. Lamata<sup>2</sup>, J. Kelly<sup>3,†</sup>, L. García-Álvarez<sup>2</sup>, A.G. Fowler<sup>1</sup>, A. Megrant<sup>3,4</sup>, E. Jeffrey<sup>1</sup>, T.C. White<sup>3</sup>, D. Sank<sup>1</sup>, J.Y. Mutus<sup>1</sup>, B. Campbell<sup>3</sup>, Yu Chen<sup>1</sup>, Z. Chen<sup>3</sup>, B. Chiaro<sup>3</sup>, A. Dunsworth<sup>3</sup>, I.-C. Hoi<sup>3</sup>, C. Neill<sup>3</sup>, P.J.J. O'Malley<sup>3</sup>, C. Quintana<sup>3</sup>, P. Roushan<sup>1</sup>, A. Vainsencher<sup>3</sup>, J. Wenner<sup>3</sup>, E. Solano<sup>2,5</sup> & John M. Martinis<sup>1,3</sup>

One of the key applications of quantum information is simulating nature. Fermions are ubiquitous in nature, appearing in condensed matter systems, chemistry and high energy physics. However, universally simulating their interactions is arguably one of the largest challenges, because of the difficulties arising from anticommutativity. Here we use digital methods to construct the required arbitrary interactions, and perform quantum simulation of up to four fermionic modes with a superconducting quantum circuit. We employ in excess of 300 quantum logic gates, and reach fidelities that are consistent with a simple model of uncorrelated errors. The presented approach is in principle scalable to a larger number of modes, and arbitrary spatial dimensions.

<sup>1</sup>Google Inc., Santa Barbara, California 93117, USA. <sup>2</sup>Department of Physical Chemistry, University of the Basque Country UPV/EHU, Apartado 644, Bilbao E-48080, Spain. <sup>3</sup>Department of Physics, University of California, Santa Barbara, California 93106, USA. <sup>4</sup>Department of Materials, University of California, Santa Barbara, California 93106, USA. <sup>5</sup>IKERBASQUE, Basque Foundation for Science, Maria Diaz de Haro 3, Bilbao 48013, Spain. <sup>†</sup>Present address: Google Inc., Santa Barbara, California 93117, USA. Correspondence and requests for materials should be addressed to R.B. (email: barends@gmail.com) or to L.L. (email: lucas.lamata@gmail.com).

Simulating quantum physics with a device which itself is quantum mechanical, a notion Richard Feynman originated<sup>1</sup>, would be an unparalleled computational resource. However, the universal quantum simulation of fermionic systems is daunting due to their particle statistics<sup>2</sup>, and Feynman left as an open question whether it could be done, because of the need for physically implementing non-local control. Quantum simulation of fermionic models is highly desirable, as computing the properties of interacting particles is classically difficult. Determining static properties with quantum Monte Carlo techniques is already complicated due to the sign problem<sup>3</sup>, arising from anticommutation, and dynamic behaviour is even harder.

The key to quantum simulation is mapping a model Hamiltonian onto a physical system. When the physical system natively mimics the model, the mapping can be direct and simulations can be performed using analogue techniques. Already, fermionic models have been simulated at scale using large clouds of natively fermionic gases $^{4,5}$ . A complementary approach is digital quantum simulation $^{6}$ . It allows for constructing arbitrary interactions, and holds the promise that it can be implemented on an error-corrected quantum computer, but at the cost of many gates. However, the digital approach is in its infancy—so far, the only experiment is the simulation of a spin Hamiltonian in ion traps $^{7}$ —because it requires complex sequences of logic gates, especially for non-local control, which hinge on carefully constructed interactions between subsets of qubits in a larger system; a demanding task for any platform. A digital fermionic simulation can therefore be regarded as a hard test.

Here, we explore fermionic interactions with digital techniques in a superconducting circuit. Focusing on the Hubbard model $^{8,9}$ , we perform time evolutions with constant interactions as well as a dynamic phase transition with up to four fermionic modes encoded in four qubits, using the Jordan-Wigner transformation $^{10}$ . The implemented digital approach is universal and allows for the efficient simulation of fermions. The required number of gates scales only polynomially with the number of modes $^{9}$ , even with physical nearest-neighbour qubit coupling only. Moreover, the model system is not limited to the dimensionality of the physical system, allowing for the simulation of fermionic models in two and three spatial dimensions $^{9,11}$ . We use in excess of 300 single-qubit and two-qubit gates, to implement fermionic models that require fully, yet separately tunable  $\hat{X}\hat{X}$ ,  $\hat{Y}\hat{Y}$  and  $\hat{Z}\hat{Z}$  interactions. We reach global fidelities that are limited by gate errors in an intuitive error model. These results are made possible by recent advances in architecture and control of superconducting qubits $^{12-14}$ . Our experiment is a critical step on the path to creating an analogue-digital quantum simulator—we foresee one using discrete fermionic modes combined with discrete $^{15}$  or continuous $^{16}$  bosonic modes, highlights the digital approach and is a demonstration of digital quantum simulation in the solid state.

# Results

Implementing the Hubbard model with gates. At low temperatures, classes of fermionic systems can be accurately described by the Hubbard model. Here hopping (strength  $V$ ) and repulsion (strength  $U$ ) compete (see Fig. 1a), capturing the rich physics of many-body interactions such as insulating and conducting phases in metals[17,18]. The generic Hubbard Hamiltonian is given by:  $H = -V \sum_{\langle i,j \rangle} (b_i^\dagger b_j + b_j^\dagger b_i) + U \sum_{i=1}^{N} n_{i\uparrow} n_{i\downarrow}$ , with  $b$  the fermionic annihilation operator and  $i,j$  running over all adjacent lattice sites. The first term describes the hopping between sites and the last term the on-site repulsion. It is

![](images/5ebb582267c789a7f3a57a02b4e4f527dbf7d6c6d84aa95c1d41bed277ca7005.jpg)  
Figure 1 | Model and device. (a) Hubbard model picture with two sites and four modes, with hopping strength  $V$  and on-site interactions  $U$ . The creation of one excitation from the groundstate is shown for each mode. (b) Optical micrograph of the device. The scale bar (bottom left) denotes  $200\mu m$ . The coloured cross-shaped structures are the used Xmon transmon qubits. The construction of the fermionic operators for four modes is shown on the right. Colours highlight the corresponding sites, qubits and operators.

insightful to look at a fermionic two-mode example,

$$
H = - V \left(b _ {1} ^ {\dagger} b _ {2} + b _ {2} ^ {\dagger} b _ {1}\right) + U b _ {1} ^ {\dagger} b _ {1} b _ {2} ^ {\dagger} b _ {2}. \tag {1}
$$

We can express the fermionic operators in terms of Pauli and ladder operators using the Jordan-Wigner transformation $^{10}$ :  $b_{1}^{\dagger} = I \otimes \sigma^{+}$  and  $b_{2}^{\dagger} = \sigma^{+} \otimes \sigma_{z}$ , where the  $\sigma_{z}$  term ensures anticommutation. In essence, we use non-local control and map a local fermionic Hamiltonian to a local spin Hamiltonian. The qubits act as spins, and carry the fermionic modes (Fig. 1a,b). A fermionic mode is either occupied or unoccupied, and spinless—the spin degree of freedom is implemented here by using four modes to simulate two sites with two spins. We note that for higher spatial dimensions this approach is still viable, the only difference is that the local fermionic Hamiltonian now maps to a non-local spin Hamiltonian, which can be efficiently implemented as recently shown $^{9,11}$ . Using the above transformation, the Hamiltonian becomes

$$
H = \frac {V}{2} \left(\sigma_ {x} \otimes \sigma_ {x} + \sigma_ {y} \otimes \sigma_ {y}\right) + \frac {U}{4} \left(\sigma_ {z} \otimes \sigma_ {z} + I \otimes \sigma_ {z} + \sigma_ {z} \otimes I\right), \tag {2}
$$

which can be implemented with separately tunable  $\hat{X}\hat{X},\hat{Y}\hat{Y}$  and  $\hat{Z}\hat{Z}$  interactions. Here we use the convention to map an excited fermionic mode  $|1\rangle$  (excited logical qubit) onto a qubit's physical groundstate  $|g\rangle$ , and a vacuum fermionic mode  $|0\rangle$  (ground logical qubit) onto a qubit's physical excited state  $|e\rangle$ .

Our experiments use a superconducting nine-qubit multipurpose processor, see Fig. 1b. Device details can be found in ref. 19. The qubits are the cross-shaped structures[20] patterned out of an aluminium film on a sapphire substrate. They are arranged in a linear chain with nearest-neighbour coupling. Qubits have individual control, using microwave and frequency-detuning pulses (top), and readout is done through dispersive measurement (bottom)[21]. By frequency tuning of the qubits, interactions between adjacent pairs can be separately turned on and off. This system allows for implementing non-local gates, as it has a high level of controllability, and is capable of performing high-fidelity gates[12,22]. Importantly, single- and two-qubit gate fidelities are maintained when scaling the system to larger numbers of qubits, as shown by the consistency of errors with the five-qubit device[12].

The basic element used to generate all the interactions is a simple generalization of the controlled-phase (CZ) entangling

gate (Fig. 2a,b). We implement a state-dependent frequency pull by holding one qubit steady in frequency and bringing a second qubit close to the avoided level crossing of  $|ee\rangle$  and  $|gf\rangle$  using an adiabatic trajectory[23]. By tuning this trajectory, we can implement a tunable  $\mathrm{CZ}_{\phi}$  gate. During this operation, adjacent qubits are detuned away in frequency to minimize parasitic interactions. The practical range for  $\phi$  is 0.5-4.0 rads; below this range, parasitic  $\hat{Z}\hat{Z}$  interactions with other qubits become relevant, and above this range population starts to leak into higher-energy levels (see Supplementary Note 5 and refs 12,19). Using single-qubit gates and two entangling gates, we can implement the tunable  $\hat{Z}\hat{Z}$  interactions, as shown in Fig. 2c. In this gate construction, the  $\pi$ -pulses naturally suppress dephasing[24].

Verifying operator anticommutativity. First, we have experimentally verified that the encoded fermionic operators anticommute, see Fig. 3, by implementing the following anticommutation relation  $\{b_1, b_2^\dagger\} + \{b_2, b_1^\dagger\} = 0$ . The latter can be separated into two non-trivial Hermitian terms:  $b_1b_2^\dagger + b_2b_1^\dagger$  (Fig. 3a) and  $b_1^\dagger b_2 + b_2^\dagger b_1$  (Fig. 3b). Their associated unitary

![](images/892466aabe20a2fb16f20778604bf37c731457cce3bbb2057ce93a4ac9695722.jpg)

![](images/7bfcd89ab0c7266d6722369d6b4a84feee1784dc758599e223282cffc1e6646d.jpg)  
Figure 2 | Gate construction. (a) Construction of the gate  $U = \exp \left(-i\frac{\phi}{2}\sigma_z \otimes \sigma_z\right)$  from single-qubit rotations and the tunable  $CZ_{\phi}$ -entangling gate. To enable small and negative angles, we include  $\pi$  pulses around the  $x$  axis  $(\mathbf{A} = \mathbf{X})$  or  $y$  axis  $(\mathbf{A} = \mathbf{Y})$ . The unitary diagonals are  $(1e^{i\phi}e^{i\phi}1)$ . (b) Tunable  $CZ_{\phi}$  gate, implemented by moving  $|ee\rangle$  (red) close to  $|gf\rangle$  (blue). Coupling strength is  $g / 2\pi = 14\mathrm{MHz}$ , pulse length is 55 ns, and typically  $\Delta / 2\pi = 0.7\mathrm{GHz}$  when idling. (c) Measured versus desired phase of the full sequence, determined using quantum state tomography.

![](images/e2904719d5f71ed037126fdcc8aac90d21f0bbe049d21647773d792b5e4a0a66.jpg)

evolution,  $U = \exp(-i\frac{\phi}{2}(b_1b_2^\dagger + b_2b_1^\dagger))$  for the first one, has been implemented using gates with strength  $\phi = \pi$ . The measured process matrices  $(\chi)$  for these terms are determined using quantum process tomography, and constrained to be physical (Supplementary Note 2). We find that the processes are close to the ideal, with fidelities  $\mathrm{Tr}(\chi_{\mathrm{ideal}}\chi) = 0.95$ , 0.96. As the Hermitian terms sum up to zero, their unitary evolutions combine to the identity (Fig. 3c). We find that the sequence of both processes yields in fact the identity, as expected for anticommutation, with a fidelity of 0.91.

Simulations with two fermionic modes. We now discuss the simulation of fermionic models. We use the Trotter approximation $^{25}$  to digitize the evolution of Hamiltonian  $H = \sum_{k} H_{k} : U = \exp(-iHt) \simeq [\exp(-iH_{1}t/n)\exp(-iH_{2}t/n)\dots]^n$ , with each part implemented using single- and two-qubit gates ( $\hbar = 1$ ). We benchmark the simulation by comparing the experimental results with the exact digital outcome. Discretization unavoidably leads to deviations, and the digital errors are quantified in Supplementary Note 4.

We start by visualizing the kinetic interactions between two fermionic modes. The construction of the Trotter step is shown in Fig. 4a and directly follows from the Hamiltonian in equation (2). The step consists of the  $\hat{X}\hat{X},\hat{Y}\hat{Y}$  and  $\hat{Z}\hat{Z}$  terms, constructed from  $\hat{Z}\hat{Z}$  terms and single-qubit rotations. We simulate the evolution during time  $\Delta t$  by setting  $\phi_{xx} = \phi_{yy} = V\Delta t$  and  $\phi_z = \phi_{zz} = U\Delta t / 2$  and using  $V = U = 1$ . We evolve the system to a time of  $T = 5.0$  and increase the number of steps ( $\Delta t = T / n$ , with  $n = 1,\dots,8$ ). The data show hallmark oscillations, Fig. 4b, indicating that the modes interact and exchange excitations. We find that the end-state fidelity, taken at the same simulated time, decreases approximately linearly by 0.054 per step (Fig. 4c).

The above example shows that fermionic simulations, clearly capturing the dynamics arising from interactions, can be performed digitally using single-qubit gates and the tunable  $\mathrm{CZ}_{\phi}$  gate. Moreover, increasing the number of steps improves the time resolution, but at the price of increasing errors. A crucial result is that the per-step decrease in the end-state fidelity is consistent with the gate fidelities. Using the typical values of  $7.4\times 10^{-3}$  entangling gate error and  $8\times 10^{-4}$  single-qubit gate error as previously determined for this platform[12], we arrive at an expected Trotter step process error of 0.07, considering the step consists of six entangling gates and 28 single-qubit gates (including X, Y rotations as well as idles). In addition, we have determined the Trotter step gate error in a separate interleaved

![](images/023df28d68a079a43c10e719440590438e7a780e2ada368bdb66305a5452d8eb.jpg)  
Figure 3 | Quantum process tomography of operator anticommutation. The process matrices are shown for the non-trivial Hermitian terms of the anticommutation relations. (a) Process matrix of the unitary  $U = \exp(-i\frac{\pi}{2}[b_1b_2^\dagger + b_2b_1^\dagger])$ . (b) Process matrix of the unitary  $U = \exp(-i\frac{\pi}{2}[b_1^\dagger b_2 + b_2^\dagger b_1])$ . (c) The sequence of both processes,  $U = \exp(-i\frac{\pi}{2}[b_1b_2^\dagger + b_2b_1^\dagger + b_1^\dagger b_2 + b_2^\dagger b_1])$ , yields the identity. The significant matrix elements, red for the real and blue for the imaginary elements, are close to the ideal (transparent).

![](images/a171c29bcff8df6daecb336ae278b87d0d9e141d53fca092a6923e48f2101113.jpg)

![](images/fd322f4de6952bdc75b13e4832dfcaac0aaec0526b52ec9d6e31c6391c4dd74d.jpg)

![](images/93410bbcfd19b348841275ab97a475e87528cf61b6ab9f24684923cf0e79854f.jpg)

![](images/d610647dc8379e535d389b544ac5411d778fbb11d9d63ff4cb7e1f2ea59f9edd.jpg)  
Figure 4 | Simulation of two fermionic modes. (a) Construction of the two-mode Trotter step, showing the separate terms of the Hamiltonian (equation (2)). See Supplementary Note 1 for the pulse sequence and gate count. (b) Occupation of the modes versus simulated time for  $n = 1,\dots,8$  steps. Colour coding denotes the state probabilities. Input state is  $\left[\left(|0\rangle +|1\rangle\right)\otimes |1\rangle\right] / \sqrt{2}$ , and  $V = U = 1$ . The ideal dependence is shown in the bottom right. The final simulation time is  $T = 5$ . (c) The end-state fidelity decreases with step by 0.054, following a linear trend.

![](images/2d905a3abdd71124f811fc13ca92e20868815059f214e35521fe71816aae5d63.jpg)

randomized benchmarking experiment (Supplementary Note 3), and found a process error of 0.074, which is consistent with the observed per-step state error. We find that the process fidelity is thus a useful estimate, even though the simulation fidelity depends on the state and implemented model.

Simulations with three and four fermionic modes. Simulations of fermionic models with three and four modes are shown in Fig. 5. The three-mode Trotter step and its pulse sequence are shown in Fig. 5a,b. An implementation of the  $\hat{Y}\hat{Y}$  gate is highlighted: the top qubit (red) is passive and detuned away, the middle qubit (blue) is tuned to an optimal frequency for the interaction, and the bottom qubit (green) performs the adiabatic trajectory.  $\pi$ -pulses on the passive qubit suppress dephasing and parasitic interactions. Figure 5c shows the simulation results for  $V = 1$ ,  $U = 0$  (hopping only) and  $V = 1$ ,  $U = 1$  (with on-site repulsion). Input state generation is shown in Supplementary Note 1. The simulation data (closed symbols) follows the exact digital outcome (open symbols), accumulating a per-step error of 0.15 (Fig. 5f) and gradually populating other states (black symbols). The fidelity is the relevant figure of merit; the per-step error being the same for different model parameters indicates that the simulation outcomes are distinct.

For the four-mode experiment, we simulate an asymmetric variation on the Hubbard model. Here the repulsive interaction is between the middle modes only (right well in Fig. 1a), while the hopping terms are kept equal. Asymmetric models are used in describing anisotropic fermionic systems[26]. In addition, the simulation can be optimized: gate count is reduced by the removal of interaction between the top and bottom modes, and the Trotter expansion can be rewritten in terms of odd and even steps such that the starting and ending single-qubit gates cancel (Supplementary Note 6). The Trotter step is shown in Fig. 5d. The results are plotted in Fig. 5e. We find that the state fidelity decreases by 0.17 for the four-mode simulation, see Fig. 5f.

The three- and four-mode experiments underline that fermionic models can be simulated digitally with large numbers of gates. The three-mode simulation uses in excess of 300 gates. We perform three Trotter steps, and per step we use: 12 entangling gates, 53 microwave  $\pi$  and  $\pi /2$  gates, 19 idle gates, 3 single-qubit phase gates and for the non-participating qubit during the entangling operation: 12 frequency-detuning gates where phases need to be accurately tracked. Using the above typical errors for gates, we arrive at an estimated process error of 0.16 for the three-mode simulation, and an error of 0.15 for the four-mode simulation (per four-mode Trotter step: 10 entangling gates and 98 single-qubit gates). The process errors are close to the observed drop in state fidelity. The data are summarized in Table 1. Importantly, these results strongly suggest that the simulation errors scale with the number of gates, not qubits (modes), which is a crucial aspect of scalably implementing models on our platform. Therefore, the appreciable drop in total fidelity is currently the optimal for any quantum platform considering the large number of gates that we have implemented in this experiment. Moreover, the precision achieved in our experiment allows us to observe the expected fermionic behaviour at every Trotter step of the implemented protocol.

Time-varying interactions. We now address the simulation of fermionic systems with time-dependent interactions. In Fig. 6a, we show an experiment where we ramp the hopping term  $V$  from 0 to 1 while keeping the on-site repulsion  $U$  at 1, essentially changing the system from an insulating to a metallic phase. This transition is simulated for two modes using two Trotter steps, see inset, and with one step for three modes. For the latter case, we take the average of  $V$  over the relevant time domain. The data are shown in Fig. 6b,c, and clearly mirror the dynamics of the hopping term. At time smaller than 1.0, the system is frozen and the mode occupations are virtually

![](images/1c467a5c5cd35773ec5265b9b3208877037cad712a8fc903badbcf60ea1fe462.jpg)

![](images/7878c2c626b1fcb2dc787435aac6c7da2efd4a3cc9e8d70ab003e14e717d768e.jpg)

![](images/806c86dfadbe2fed3735131f9db904ce18ef04f9fd15bf7322108b1cd871a812.jpg)

![](images/eccbca2ef1d535f96b2fe6836c70c0f15c15f68b5cf78b2432ba44b014433cc5.jpg)  
Figure 5 | Fermionic models with three and four modes. (a) Three-mode Trotter step, with the Trotter step pulse sequence in b. The Trotter step consists of 12 entangling gates and 87 single-qubit gates (see text). The  $\hat{Y}\hat{Y}$  interaction is highlighted (dashed). The amplitudes of the rotations are controlled by the values of  $V$  and  $U$ :  $\frac{\phi_{xx}}{2} = \frac{\phi_{yy}}{2} = \frac{V}{2}\Delta t$ , and  $\frac{\phi_x}{2} = \frac{\phi_{zz}}{2} = \frac{U}{4}\Delta t$ . (c) Simulation results for three modes with and without on-site interaction. Full symbols: experiment. Open symbols: ideal digitized. Black symbols: population of other states. Input state is  $[|1\rangle \otimes (|01\rangle + |10\rangle)] / \sqrt{2}$ , and  $V = 1$ . (d) Construction of the four-mode Trotter step. The amplitudes of the rotations are:  $\frac{\phi_{V1}}{2} = \frac{V_1}{2}\Delta t$ ,  $\frac{\phi_{V2}}{2} = \frac{V_2}{2}\Delta t$  and  $\frac{\phi_U}{2} = \frac{U}{4}\Delta t$ . (e) Four-mode simulation results for  $V_1 = V_2 = 1$ ,  $U_{23} = 1$  and  $U_{14} = 0$ . Input state is  $[(|01\rangle + |10\rangle)\otimes (|01\rangle + |10\rangle)] / \sqrt{2}$ . (f) Fidelities versus Trotter step for the three-mode simulation (dots) and the four-mode simulation (triangles).

unchanged, reflecting the insulating state. Interactions become visible when hopping is turned on, effectively melting the system, and follow the generic features of the exact digital outcome (dashed). The simulation fidelities lie around 0.9-0.95 for two modes and 0.7-0.8 for three modes, see Fig. 6d. These fidelities are around or somewhat below those for time evolution with constant interactions, presumably due to control errors related to parasitic qubit interactions, which also lead to the populating of other states (black symbols). The dynamic simulation highlights

the possibilities of exploring parameter spaces and transitions with few steps.

# Discussion

We have demonstrated the digital quantum simulation of fermionic models. Simulation fidelities are close to the expected values, and with improvements in gates and architecture, the construction of larger testbeds for fermionic systems appears viable.

Table 1 | Gate counts for the two-, three- and four-mode Trotter steps.  

<table><tr><td></td><td>Two-mode</td><td>Three-mode</td><td>Four-mode</td></tr><tr><td>Entangling CZφ gates</td><td>6</td><td>12</td><td>10</td></tr><tr><td>Single-qubit gates</td><td>28</td><td>87</td><td>98</td></tr><tr><td>Microwave π and π/2</td><td>20</td><td>53</td><td>56</td></tr><tr><td>Idle</td><td>6</td><td>19</td><td>22</td></tr><tr><td>Detuning</td><td>0</td><td>12</td><td>18</td></tr><tr><td>Virtual phase</td><td>2</td><td>3</td><td>2</td></tr><tr><td>est. Trotter step error</td><td>0.067</td><td>0.16</td><td>0.15</td></tr><tr><td>exp. Trotter step error</td><td>0.054</td><td>0.15</td><td>0.17</td></tr></table>

Est., estimated; exp., experimental.  
We count idles as having the same duration as the microwave  $\pi$  and  $\pi /2$  gates; this is the relevant approach for estimating total process fidelities. The gate counts are for a single Trotter step only, and exclude input state preparation. Estimated and experimental errors per Trotter step are tabulated at the bottom.

![](images/4df6d1d3d7d2ccf82e519906f956d63b92e0177cf7a2fc7827edf1c195474ea5.jpg)  
a

![](images/50fab74b951ad4bdf53e7dacde8b2b1504ca436beb98c6e3bf77d391d792ec49.jpg)  
b

![](images/b078418c51293bcd748746f965c7ab0044cde11e5e79d712d552a2f1ffc247fb.jpg)  
C

![](images/c6119a2419b25e228e5bb4b47a02bcd1eab569ad979f10254cce3a3204e341f3.jpg)  
d  
Figure 6 | Simulations with time-varying interactions. (a) The system is changed from an insulating state (denoted by the blue background) to a conducting phase (denoted by a red background), by ramping the hopping term  $V$  from zero to one. Solid line:  $U$ , dashed line:  $V$ . Inset shows the choice of digitization on the ramp for the two-mode simulation. (b) Two-mode simulation showing dynamic behaviour starting at the onset of the  $V$  ramp. Dashed lines denote the ideal digitized evolution. (c) Three-mode simulation, showing non-trivial dynamics when the hopping term is non-zero. Dashed lines denote the ideal digitized evolution. Black symbols indicate the population of other states. (d) Simulation fidelities.

Moreover, a future implementation of quantum error correction in combination with these techniques will enable the efficient and scalable digital quantum simulation of fermionic models. Bosonic modes can be elegantly introduced by adding linear resonators to the circuit, establishing a fermion-boson analogue-digital system<sup>15,16</sup> as a distinct paradigm for quantum simulation.

# Methods

Experimental details. Experiments are performed in a wet dilution refrigerator with a base temperature of  $20\mathrm{mK}$ . Qubit frequencies are chosen in a staggered

pattern to minimize unwanted interaction. Typical qubit frequencies are 5.5 and  $4.8\mathrm{GHz}$ . Exact frequencies are optimized based on the qubits'  $|e\rangle$  and  $|f\rangle$  state spectra along the fully tunable trajectory of the  $\mathrm{CZ}_{\phi}$ -gate, as well as on minimizing the interactions between next-nearest neighbouring qubits. Used qubits are Q1-Q4 in ref. 19. Data are corrected for measurement fidelity, typical measurement errors are 0.01 for qubits Q1 and Q3 and 0.04 for Q2 and Q4 (refs 19,27).

State fidelity. The state fidelity is computed using  $\left|\sum_{k}\sqrt{P_{k,\mathrm{ideal}}P_{k}}\right|^{2}$ , which is equal to  $|\langle \Psi_{\mathrm{ideal}}|\Psi \rangle |^2$  to first order. Here  $P_{k,\mathrm{ideal}}$  and  $P_{k}$  are mode occupations and  $k$  runs over the computational basis. The consistency with measured process fidelities, and the scaling of the simulation fidelity with steps justify this approach.

# References

1. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phys. 21, 467-488 (1982).  
2. Altland, A. & Simons, B. Condensed Matter Field Theory (Cambridge Univ. Press, 2010).  
3. Troyer, M. & Wiese, U.-J. Computational complexity and fundamental limitations to fermionic quantum Monte Carlo simulations. Phys. Rev. Lett. 94, 170201 (2005).  
4. Schneider, U. et al. Fermionic transport and out-of-equilibrium dynamics in a homogeneous Hubbard model with ultracold atoms. Nat. Phys. 8, 213-218 (2012).  
5. Greif, D. et al. Short-range quantum magnetism of ultracold fermions in an optical lattice. Science 340, 1307-1310 (2013).  
6. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
7. Lanyon, B. P. et al. Universal digital quantum simulation with trapped ions. Science 334, 57-61 (2011).  
8. Hubbard, J. Electron correlations in narrow energy bands. Proc. R. Soc. London Ser. A 276, 238-257 (1963).  
9. Las Heras, U., García-Álvarez, L., Mezzacapo, A., Solano, E. & Lamata, L. Fermionic models with superconducting circuits. EPJ Quant. Technol. 2, 8 (2015).  
10. Jordan, P. & Wigner, E. Über das Paulische Äquivalenzverbot. Z. Phys. 47, 631-651 (1928).  
11. Casanova, J., Mezzacapo, A., Lamata, L. & Solano, E. Quantum simulation of interacting fermion lattice models in trapped ions. Phys. Rev. Lett. 108, 190502 (2012).  
12. Barends, R. et al. Superconducting quantum circuits at the surface code threshold for fault tolerance. Nature 508, 500-503 (2014).  
13. Corcoles, A. D. et al. Process verification of two-qubit quantum gates by randomized benchmarking. Phys. Rev. A 87, 030301(R) (2013).  
14. Vesterinen, V., Saira, O.-P., Bruno, A. & DiCarlo, L. Mitigating information leakage in a crowded spectrum of weakly anharmonic qubits. Preprint at http://arxiv.org/abs/1405.0450 (2014).  
15. Lamata, L., Mezzacapo, A., Casanova, J. & Solano, E. Efficient quantum simulation of fermionic and bosonic models in trapped ions. *EPI Quant. Technol.* 1, 9 (2014).  
16. García-Alvarez, L. et al. Fermion-fermion scattering in quantum field theory with superconducting circuits. Phys. Rev. Lett. 114, 070502 (2015).  
17. Jördens, R. et al. A Mott insulator of fermionic atoms in an optical lattice. Nature 455, 204-207 (2008).  
18. Schneider, U. et al. Metallic and insulating phases of repulsively interacting fermions in a 3D optical lattice. Science 322, 1520-1525 (2008).  
19. Kelly, J. et al. State preservation by repetitive error detection in a superconducting quantum circuit. Nature 519, 66-69 (2015).  
20. Barends, R. et al. Coherent Josephson qubit suitable for scalable quantum integrated circuits. Phys. Rev. Lett. 111, 080502 (2013).

21. Wallraff, A. et al. Strong coupling of a single photon to a superconducting qubit using circuit quantum electrodynamics. Nature 431, 162-167 (2004).  
22. Barends, R. et al. Rolling quantum dice with a superconducting qubit. Phys. Rev. A 90, 030303(R) (2014).  
23. Martinis, J. M. & Geller, M. R. Fast adiabatic qubit gates using only  $\sigma_z$  control. Phys. Rev. A 90, 022307 (2014).  
24. O'Malley, P. J. J. et al. Qubit metrology of ultralow phase noise using randomized benchmarking. Phys. Rev. Appl. 3, 044009 (2015).  
25. Suzuki, M. Fractal decomposition of exponential operators with applications to many-body theories and Monte Carlo simulations. Phys. Lett. A 146, 319 (1990).  
26. Dutta, O. et al. Non-standard Hubbard models in optical lattices: a review. Rep. Prog. Phys. 78, 066001 (2015).  
27. Jeffrey, E. et al. Fast accurate state measurement with superconducting qubits. Phys. Rev. Lett. 112, 190504 (2014).

# Acknowledgements

We thank A.N. Korotkov for discussions. We acknowledge support from Spanish MINECO FIS2012-36673-C03-02; Ramón y Cajal Grant RYC-2012-11391; UPV/EHU UF1 11/55 and EHUA14/04; Basque Government IT472-10; a UPV/EHU PhD grant; PROMISCE and SCALEQIT EU projects. Devices were made at the UC Santa Barbara Nanofabrication Facility, a part of the NSF-funded National Nanotechnology Infrastructure Network, and at the NanoStructures Cleanroom Facility.

# Author contributions

R.B., L.L. and L.G.-A. designed the experiment, with J.M.M. and E.S. providing supervision. L.G.-A., L.L. and E.S. provided the theoretical framework. R.B. and L.L. cowrote the manuscript with J.M.M. and E.S. The experiment and data were performed and analysed by R.B., J.K., L.L. and L.G.-A. R.B. and J.K. designed the device. J.K., R.B. and A.M. fabricated the sample. All authors contributed to the fabrication process, experimental set-up and manuscript preparation.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Barends, R. et al. Digital quantum simulation of fermionic models with a superconducting circuit. Nat. Commun. 6:7654 doi: 10.1038/ncomms8654 (2015).

![](images/baa099cdef263ebc9061a077d90d2c12968bd427e18fb97c94f66cafc46233b4.jpg)

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this

article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/