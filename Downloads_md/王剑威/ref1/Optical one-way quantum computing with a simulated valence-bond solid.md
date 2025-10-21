# Optical one-way quantum computing with a simulated valence-bond solid

Rainer Kaltenbaek $^{1\star\dagger}$ , Jonathan Lavoie $^{1\dagger}$ , Bei Zeng $^{2,3}$ , Stephen D. Bartlett $^{4}$  and Kevin J. Resch $^{1\star}$

One-way quantum computation proceeds by sequentially measuring individual spins in an entangled many-spin resource state<sup>1</sup>. It remains a challenge, however, to efficiently produce such resources. Is it possible to reduce the task of their production to simply cooling a quantum many-body system to its ground state? Cluster states, the canonical resource for one-way quantum computing, do not naturally occur as ground states of physical systems<sup>2,3</sup>, leading to a significant effort to identify alternatives that do appear as ground states in spin lattices<sup>4-8</sup>. An appealing candidate is a valence-bond-solid state described by Affleck, Kennedy, Lieb and Tasaki<sup>9</sup> (AKLT). It is the unique, gapped ground state for a two-body Hamiltonian on a spin-1 chain, and can be used as a resource for one-way quantum computing<sup>4-7</sup>. Here, we experimentally generate a photonic AKLT state and use it to implement single-qubit quantum logic gates.

In the circuit model of quantum computation, information is carried by two-level systems called qubits. The computation proceeds dynamically using unitary single-qubit logic gates and multiple-qubit entangling gates. Apart from these entangling gates the qubits are fully isolated from each other. Computations in the one-way model, on the other hand, are carried out using single-qubit measurements on a strongly correlated, that is, entangled, resource state. The one-way model has led to some of the highest estimated error thresholds for fault-tolerant quantum computation $^{10}$ , and to a series of experimental demonstrations of quantum logic gates $^{11-16}$ , wherein the technical requirements can be much simpler than for the circuit model. This is particularly true of optical implementations, where the resource requirements for one-way quantum computing are significantly lower $^{17}$ , and the predicted error thresholds significantly higher $^{18}$ , than for any other approach to quantum computation.

As qubits in the one-way model are not isolated but rather interact strongly with each other, this approach lends itself more naturally to implementations in condensed-matter systems. However, out of the vast variety of strongly coupled quantum many-body systems, can we find one that has a ground state we can use as a resource for quantum computing? That seems unlikely if this ground state is to be the cluster state, because the cluster state is not the ground state of a strongly coupled many-body system with a Hamiltonian consisting of two-body interactions $^{2,3}$ . As a result, the search for alternative resource states has attracted a lot of interest recently. Although up to now little is known about the requirements potential resource states for the one-way model have to meet, and although most states are in fact useless for this task $^{19}$ , a handful of alternative states have been identified $^{4-8}$ . All of these states can be

described in the framework of matrix product states or projected entangled pair states $^{4-6,20}$ .

A promising candidate is the ground state of a spin model studied by Affleck, Kennedy, Lieb and Tasaki (AKLT). This valence-bond-solid state (see Fig. 1a) appears as the unique gapped ground state of a rotationally invariant nearest-neighbour two-body Hamiltonian on a spin-1 chain. The AKLT state possesses diverging localizable entanglement length[21] and, remarkably, can serve as a resource for one-way quantum computation[4,6,7,22]. As the Hamiltonian is frustration free, that is, the ground state minimizes the energy of each local term of the Hamiltonian, measurements in the course of the computation leave the remaining particles in their ground state. Operations leaving the computational subspace are penalized by the energy gap protecting the AKLT state. Universal quantum computation can be achieved through dynamical coupling of several AKLT states, where each can be regarded as 'quantum computational wires'[4,6,7,22].

Quantum computation with AKLT states is different from computing with cluster states in a number of ways. The elementary physical units are spin-1 systems (qutrits) instead of spin-1/2 systems (qubits), although qubits are still encoded as 'logical' information. Adaptive measurements allow non-Pauli operations, including Clifford gates, to be carried out. Single-qubit rotations can be carried out around any Cartesian axis. These operations are probabilistic, rather than deterministic, and succeed with probability 2/3. When an operation fails, it carries out a heralded logical-identity operation (up to a known Pauli error). The operation can then be reattempted on the next qutrit until it succeeds. Combinations of such rotations allow the implementation of arbitrary single-qubit quantum logic gates.

Although a number of one-dimensional spin chains are well described by the AKLT Hamiltonian, most prominently  $\mathrm{Ni(C_2H_8N_2)_2NO_2(ClO_4)}$  (ref. 23), up to now experimental techniques do not allow the single-spin measurements necessary for one-way quantum computation. One of the fundamental and most appealing motivations for quantum computing is the possibility to simulate aspects of quantum systems that cannot directly be studied[24]. As the AKLT state is a valence-bond-solid state (see Fig. 1a), we can simulate it using a chain of spin-  $1 / 2$  singlet states, for example polarization-entangled photon pairs, where adjoining particles of neighbouring pairs are projected on the symmetric triplet subspace (see Fig. 1b). Although this approach does not allow for an analysis of the dynamics of the corresponding solid-state system, it does allow us to directly produce the AKLT state and use it for one-way quantum computation.

Here, we experimentally demonstrate the generation of photonic AKLT states and their application for one-way quantum

![](images/a21c89145436860e8f98df2270c9cdfe4e4fec37b5f9f3f770fb7b28c60e4f07.jpg)  
a

![](images/8e0c69cddfb089e7143ca6dc7f1b3ad7fbabe632823432bce103ee5e27a8b13a.jpg)  
b

![](images/047010511d2e89e714cd3ba0f9e78f8fb13fd72ee7b784344033040e921a253a.jpg)  
Outrit

![](images/e77b5003fe486ab23ba6cabbe5806f31924dc7e0f88fde2f8246f20b848698da.jpg)  
Qubit

![](images/9f81d04e0177af97f6a4a2a6b794396f7e0ea60093153b47c8f5aa55da5ce187.jpg)

![](images/131baf35d895e9f254d6cb5ce7c067d046388dbe72b4e338fb1be362df07ed76.jpg)  
Singlet

![](images/560e9465313106285f37c23054b62169766e7628210a2a2bc90a675aa0411275.jpg)  
Figure 1 | AKLT states. a, The AKLT state $^{9}$  is the ground state of a spin-1 chain with a two-body nearest-neighbour interaction. It is the unique ground state if the boundary conditions are chosen accordingly. The figure illustrates a common way to set these boundary conditions: by coupling the spin-1 particles to spin-1/2 particles on either end of the chain $^{9,27}$ . The AKLT state, as a valence-bond solid, can be represented by a chain of virtual spin-1/2 particles in singlet states where adjoining qubits of neighbouring pairs are projected on the triplet subspace, that is, the subspace symmetric with respect to swapping of the two qubits. b, One can simulate an AKLT state with a chain of sources producing singlet states and projecting pairs of particles on the triplet subspace.  
Projection

computation. We produce two singlet states,  $|\psi^{-}\rangle = (|\mathrm{HV}\rangle - |\mathrm{VH}\rangle) / \sqrt{2}$ , in four distinct spatial modes using spontaneous parametric down conversion. Here,  $|\mathrm{H}\rangle$  and  $|\mathrm{V}\rangle$  denote horizontal and vertical polarization. From these two singlets we create an AKLT state consisting of two boundary spin-1/2 systems and one spin-1 system. The spin-1 system is realized using a biphoton[25,26], symmetrized by projecting a pair of photons into the triplet subspace. This projection is achieved by overlapping these two photons at a beam splitter and by postselecting those cases where both photons exit through the same output mode of the beam splitter. The resulting biphoton represents our qutrit. Qutrit measurements are carried out probabilistically by splitting the photons on a beam splitter and measuring the individual photons in polarization analysers. More details can be found in the Methods section and the Supplementary Information. For the qutrit analyser settings, see Supplementary Table S1. The experimental set-up is shown in Supplementary Figure S1. A discussion of the theoretical aspects of the simulation of AKLT states using quantum optics and their use in one-way quantum computation is given in a separate paper[27].

We shall use the states  $|-1\rangle$ ,  $|0\rangle$  and  $|1\rangle$  to denote a basis in a spin-1 system. In our case these states correspond to the biphoton states  $(1/\sqrt{2})a_{\mathrm{H}}^{\dagger}a_{\mathrm{H}}^{\dagger}|vac\rangle$ ,  $a_{\mathrm{H}}^{\dagger}a_{\mathrm{V}}^{\dagger}|vac\rangle$  and  $(1/\sqrt{2})a_{\mathrm{V}}^{\dagger}a_{\mathrm{V}}^{\dagger}|vac\rangle$ , respectively, where both photons are in the same spatial mode,  $|vac\rangle$  is the vacuum state and  $a_{\mathrm{H}}^{\dagger}$  and  $a_{\mathrm{V}}^{\dagger}$  are photon creation operators. Using this notation, the AKLT state for our qubit-qutrit-qubit system is  $|\psi_{\mathrm{AKLT}}\rangle = (1/\sqrt{6})|\mathrm{H},0,\mathrm{V}\rangle + (1/\sqrt{6})|\mathrm{V},0,\mathrm{H}\rangle - (1/\sqrt{3})|\mathrm{H},1,\mathrm{H}\rangle - (1/\sqrt{3})|\mathrm{V}, -1,\mathrm{V}\rangle$ . Here, the tensor-product structure of our state is according to physical systems in separate spatial modes, that is, photon-biphoton-photon. To verify the faithful production of the AKLT state in our experiment, we carry out quantum-state tomography and use a maximum-likelihood technique based on a semi-definite-programming algorithm to reconstruct the density matrix shown in Fig. 2. For a detailed list of the states measured and of the corresponding counts, see Supplementary Tables S2 and S3. The fidelity<sup>28</sup> of the reconstructed maximum-likelihood density matrix with the ideal AKLT state is  $(87.4 \pm 0.4)\%$ . The uncertainty in that value is determined by using a Monte Carlo simulation with 420 iterations on the observed counts.

To experimentally demonstrate the use of AKLT states for quantum computation, we realize single-qubit rotations of several input states around the  $\hat{x}, \hat{y}$  and  $\hat{z}$  axes of the Bloch sphere. As in one-way quantum computing the quantum information

![](images/f3a0cf8272fff4b0770804150dd285fa3fb028d5914a8bb1490bdc0a852da6a3.jpg)  
a

![](images/8ed6fe79547f29a3a07652d51575c2981834d5178ddd5b673a2f51332ec1576e.jpg)  
b  
Figure 2 | Tomographic reconstruction of our photonic AKLT state.  
a,b, The real (a) and imaginary (b) parts of the density matrix reconstructed from an over-complete set of qubit-qutrit-qubit tomography measurements (for the measurement settings and the counts measured, see Supplementary Tables S2 and S3). The fidelity with the ideal AKLT state is  $(87.1\pm 0.4)\%$ .

Table 1 | Qutrit measurement bases and Pauli corrections.  

<table><tr><td rowspan="2">Rotations</td><td colspan="2">plus</td><td colspan="2">minus</td><td colspan="2">id</td></tr><tr><td>State</td><td>Correction</td><td>State</td><td>Correction</td><td>State</td><td>Correction</td></tr><tr><td>Rx(θ)</td><td>cosθ/2|y) + i sinθ/2|z)</td><td>XZ</td><td>i sinθ/2|y) + cosθ/2|z)</td><td>Z</td><td>|x)</td><td>X</td></tr><tr><td>Ry(θ)</td><td>cosθ/2|z) + sinθ/2|x)</td><td>Z</td><td>- sinθ/2|z) + cosθ/2|x)</td><td>X</td><td>|y)</td><td>XZ</td></tr><tr><td>Rz(θ)</td><td>cosθ/2|x) + i sinθ/2|y)</td><td>X</td><td>i sinθ/2|x) + cosθ/2|y)</td><td>XZ</td><td>|z)</td><td>Z</td></tr></table>

Single-qubit rotations  $R_{x}(\theta), R_{y}(\theta)$  or  $R_{z}(\theta)$  around the respective Cartesian axes  $\hat{x},\hat{y}$  or  $\hat{z}$  are realized by a projective qudit measurement. Each qudit measurement has three possible outcomes (plus, minus and id) and can be described by projecting onto the corresponding qudit states. We provide the state for each rotation axis and qudit measurement outcome, and we specify the Pauli correction  $(X,XZ = -IY$  or  $Z$  ) required for each measurement outcome. The qudit basis states  $|x\rangle ,|y\rangle$  and  $|z\rangle$  are defined as  $1 / 2(a_{\uparrow H\downarrow H}^{\dagger} - a_{\downarrow V}^{+}a_{V}^{\dagger})|\mathrm{vac}\rangle ,1 / 2(a_{\uparrow H\downarrow H}^{\dagger} + a_{\downarrow V}^{+}a_{V}^{\dagger})|\mathrm{vac}\rangle$  and  $a_{H}^{\dagger}a_{V}^{\dagger}|\mathrm{vac}\rangle$  , respectively.

![](images/63e6daf18055ab3466a37a504a0e4ab5ba3f9cb510ed7b0ba0757b01b11498aa.jpg)  
a

![](images/dbc1e7d7d9127296673fa493bd1ee5d226043f067f3581c466bd5426fd8087ac.jpg)  
d

![](images/4f1ba1f71a4c404707a7f75261b0b484c7cd6921206d845c057f8821f5c61e4a.jpg)  
b

![](images/b2cd2b8da246e6c6fb83a4ba06f9eb3d5928841af1d94fc3715eeb2610ce215e.jpg)  
e

![](images/00ac2856e70dc956583746476c261a2f934e06c7d3d47400ee458e4ff602df9c.jpg)  
c

![](images/ff1f55fb9c9fb67fb1c3fd58f1a392554138162d3818b85a8f4b2139724ac916.jpg)  
Figure 3 | Measurement results for single-qubit rotations. a-c, The coordinates of the Bloch vectors of the reconstructed output density matrices for rotations of a logical input state  $|\mathrm{H}\rangle$  around the  $\hat{x},\hat{y}$  and  $\hat{z}$  axes. Note that the results shown are for the plus outcome of the qutrit measurement, and that we have applied the necessary Pauli corrections to the reconstructed density matrices for all plots shown in the figure. Error bars are 1 s.d. calculated from Monte Carlo simulation. The solid and dashed lines indicate the theoretical expectations given the ideal AKLT state and the tomographically reconstructed AKLT state (see Fig. 2), respectively. d-f, The Bloch vectors of the measured (and Pauli-corrected) density matrices corresponding to the Bloch coordinates shown in a-c for the rotation angles  $0,\pi /4$  and  $\pi /2$  
f

<table><tr><td>Rx data — Rx ideal — Rx predicted</td></tr><tr><td>Ry data — Ry ideal — Ry predicted</td></tr><tr><td>Rz data — Rz ideal — Rz predicted</td></tr></table>

Table 2 | Single-qubit logic gate fidelities.  

<table><tr><td colspan="7">Gate fidelities for logical input |H)</td></tr><tr><td rowspan="2">Outcomes</td><td colspan="2">Rx</td><td colspan="2">Ry</td><td colspan="2">Rz</td></tr><tr><td>ρth</td><td>ρexp</td><td>ρth</td><td>ρexp</td><td>ρth</td><td>ρexp</td></tr><tr><td>Plus</td><td>0.91±0.04</td><td>0.98±0.02</td><td>0.90±0.05</td><td>0.98±0.02</td><td>0.90±0.03</td><td>0.98±0.02</td></tr><tr><td>Minus</td><td>0.93±0.03</td><td>0.97±0.03</td><td>0.91±0.03</td><td>0.99±0.01</td><td>0.92±0.04</td><td>0.97±0.02</td></tr><tr><td>Id</td><td>0.90±0.03</td><td>0.98±0.02</td><td>0.92±0.02</td><td>0.9993+0.0004-0.0089</td><td>0.97±0.02</td><td>0.987+0.006-0.026</td></tr><tr><td colspan="7">Gate fidelities averaged over all input states</td></tr><tr><td rowspan="2">Outcomes</td><td colspan="2">Rx</td><td colspan="2">Ry</td><td colspan="2">Rz</td></tr><tr><td>ρth</td><td>ρexp</td><td>ρth</td><td>ρexp</td><td>ρth</td><td>ρexp</td></tr><tr><td>All</td><td>0.92±0.04</td><td>0.97±0.02</td><td>0.91±0.04</td><td>0.99+0.01-0.02</td><td>0.92±0.04</td><td>0.97±0.02</td></tr></table>

We compare the experimentally determined output density matrices with the ones expected given an ideal AKLT state,  $\rho_{\mathrm{th}}$  and given the AKLT state measured in our set-up,  $\rho_{\mathrm{exp}}$ . The upper part of the table shows the fidelities for a logical input state  $|\mathsf{H}\rangle$ . For the plus and minus outcomes the fidelities are averaged over all rotation angles; for the id outcome we carried out one measurement per rotation axis. The lower part shows the corresponding fidelities averaged over all logical input states prepared and over all three qutrit measurement outcomes. See Supplementary Information for more detailed results and a description of how the errors were calculated.

is not encoded locally in one particle but rather in the state of the remaining particles of the entangled resource state, it is referred to as 'logical' information. The logical input state,  $|\psi \rangle$ , of a computation is prepared by projecting the first boundary qubit onto the state  $|\psi^{\perp}\rangle$ , such that  $\langle \psi |\psi^{\perp}\rangle = 0$ . Here, we demonstrate rotations  $R_{x}(\theta), R_{y}(\theta)$  or  $R_{z}(\theta)$  of the logical input state  $|\psi\rangle = |\mathrm{H}\rangle$  by an angle  $\theta$  around the respective Cartesian axis (experimental results for other input states are given in the Supplementary Information). We do so for a set of ten angles  $\theta = \{0,\pi /8,\pi /4,3\pi /8,\pi /2,3\pi /4,\pi ,5\pi /4,3\pi /2,7\pi /4\}$ . Each rotation is realized by carrying out a specific measurement on the qutrit in our AKLT state. Each qutrit measurement has three possible outcomes, which we denote as plus, minus and id. Each outcome occurs with probability  $1/3$  and corresponds to a projection of the qutrit on one out of three orthogonal qutrit states as indicated in Table 1. In one-way quantum computing with cluster states, measurement outcomes can lead to known Pauli errors<sup>1,6,7</sup>, which can be corrected. Pauli corrections are also necessary in AKLT-based schemes, and in Table 1 we indicate which Pauli correction is needed for a given qutrit measurement outcome. The outcomes plus and minus signal a successful rotation, and the outcome id signals the logical identity, that is, no rotation has been carried out, only a Pauli error. As a result, a successful rotation is achieved with probability  $2/3$ . For  $\theta = 0$ , every outcome heralds the logical identity (modulo a Pauli correction). This can be used to teleport logical information along the wire, for example to a position where the wire is coupled to another, or to the read-out position. We reconstruct the density matrix of each computational outcome by carrying out a tomographically over-complete set of measurements on the last qubit, using the measurement settings:  $|\mathrm{H}\rangle, |\mathrm{V}\rangle, |\pm\rangle = (|\mathrm{H}\rangle \pm |\mathrm{V}\rangle)/\sqrt{2}, |\mathrm{R}\rangle = (|\mathrm{H}\rangle + i|\mathrm{V}\rangle)/\sqrt{2}$ , and  $|\mathrm{L}\rangle = (|\mathrm{H}\rangle - i|\mathrm{V}\rangle)/\sqrt{2}$ .

Figure 3 shows the measurement results for the single-qubit rotations of our logical input state  $|\mathrm{H}\rangle$  for plus outcomes of the qutrit measurement. In Fig. 3a-c we give the coordinates of the Bloch vectors corresponding to the reconstructed single-qubit density matrices, and we compare them to the theoretical expectations. Figure 3d-f shows the Bloch-sphere representation of some of these vectors. Note, that we Pauli-corrected the reconstructed density matrices. In Table 2 we provide the fidelities of the reconstructed density matrices with the corresponding ideal rotations as well as the averaged fidelities for the complete set of logical input states prepared. From the count rates observed for all input states and rotations, we calculate the average frequencies for the occurrence of each of the three qutrit measurement outcomes

to be  $0.34 \pm 0.03, 0.30 \pm 0.05$  and  $0.36 \pm 0.04$  for the plus, the minus and the id outcome, respectively, comparing well to the expected probability of  $1/3$  for each outcome. The output fidelities for each input state and rotation are provided in Supplementary Tables S4-S6. On average that fidelity is  $(92 \pm 4)\%$ , demonstrating the high quality of our single-qubit quantum logic gates using a photonic AKLT state.

We have experimentally demonstrated one-way quantum computation using a new resource, the AKLT state, implementing single-qubit rotations around any coordinate axis. Quantum computation using AKLT, instead of cluster states, promises to combine the inherent advantages of the one-way model with resources that occur naturally in physical systems. Our scheme for creating AKLT states uses entangled states and linear optics similar in requirements to optical implementations using cluster states[17]. In contrast to some other optical approaches to one-way quantum computation[11,12], our scheme is phase insensitive and achieves significantly higher experimental fidelities. Our implementation of a valence-bond-solid state is a realization of a projected entangled pair state[20]. Such states offer a promising framework for understanding the properties of entangled states that make them useful computational resources[4-6,8]. Generalizations of our approach might allow simulating other classes of resource states with linear optics and their study for quantum computing. Future challenges will be to find efficient methods of coupling quantum wires, to study solid-state compounds with ground states that can be used as computational resources and to implement techniques to address such systems on a single-particle level. Ideally, this and related research will lead to implementations in solid-state architectures, allowing one to tap the power of one-way quantum computation while taking full advantage of the appealing characteristics of novel resource states such as AKLT.

# Methods

The light source in our experiment is a titanium:sapphire femtosecond laser, centred at  $790\mathrm{nm}$  with  $10\mathrm{nm}$  full-width-at-half-maximum (FWHM) bandwidth,  $2.9\mathrm{W}$  average output power and  $80\mathrm{MHz}$  repetition rate. Second-harmonic generation in a 2-mm-thick bismuth borate crystal yields a beam of  $780\mathrm{mW}$  power, centred at  $395\mathrm{nm}$ , with about  $1.5\mathrm{nm}$  FWHM bandwidth. With this beam we pump two separate type-I spontaneous parametric down-conversion sources[29,30], each a pair of 1-mm-thick  $\beta$ -barium borate crystals. Longitudinal and transverse walk-off occurring in the down-conversion crystals is compensated with a combination of birefringent crystals ( $\alpha$ -barium borate, quartz and bismuth borate, see ref. 30 and Supplementary Information). All photons pass through  $3\mathrm{nm}$  FWHM bandwidth filters. In each source, the polarization of the photons in one mode is measured directly at the source; the photons in the other modes are coupled into single-mode

fibres and sent to a quantum interferometer and analyser set-up. The input modes of the interferometer are overlapped at a 50:50 beam splitter, where, depending on the two-photon state, two-photon interference leads to both photons leaving through the same or through different beam-splitter output modes<sup>31</sup>. By measuring a two-photon event in one output mode of the beam splitter, the biphoton is projected onto a qutrit subspace. This mode is input in a qutrit analyser, where we implement qutrit projections by probabilistically separating the two photons at another beam splitter and carrying out appropriate polarization measurements on each photon<sup>25,26</sup>. For a more detailed discussion of the set-up and the qutrit projections, see Supplementary Information.

# Received 16 April 2010; accepted 10 August 2010; published online 17 October 2010

# References

1. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
2. Nielsen, M. A. Cluster-state quantum computation. Rep. Math. Phys. 57, 147-161 (2006).  
3. Bartlett, S. D. & Rudolph, T. Simple nearest-neighbor two-body Hamiltonian system for which the ground state is a universal resource for quantum computation. Phys. Rev. A 74, 040302 (2006).  
4. Verstraete, F. & Cirac, J. I. Valence-bond states for quantum computation. Phys. Rev. A 70, 060302 (2004).  
5. Gross, D. & Eisert, J. Novel schemes for measurement-based quantum computation. Phys. Rev. Lett. 98, 220503 (2007).  
6. Gross, D., Eisert, J., Schuch, N. & Perez-Garcia, D. Measurement-based quantum computation beyond the one-way model. Phys. Rev. A 76, 052315 (2007).  
7. Brennen, G. K. & Miyake, A. Measurement-based quantum computer in the gapped ground state of a two-body Hamiltonian. Phys. Rev. Lett. 101, 010502 (2008).  
8. Chen, X., Zeng, B., Gu, Z-C., Yoshida, B. & Chuang, I. L. Gapped two-body Hamiltonian whose unique ground state is universal for one-way quantum computation. Phys. Rev. Lett. 102, 220501 (2009).  
9. Affleck, I., Kennedy, T., Lieb, E. H. & Tasaki, H. Rigorous results on valence-bond ground states in antiferromagnets. Phys. Rev. Lett. 59, 799-802 (1987).  
10. Raussendorf, R., Harrington, J. & Goyal, K. A fault-tolerant one-way quantum computer. Ann. Phys. 321, 2242-2270 (2006).  
11. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169-176 (2005).  
12. Prevedel, R. et al. High-speed linear optics quantum computing using active feed-forward. Nature 445, 65-69 (2007).  
13. Vallone, G., Pomarico, E., De Martini, F. & Mataloni, P. One-way quantum computation with two-photon multiqubit cluster states. Phys. Rev. A 78, 042335 (2008).  
14. Tokunaga, Y., Kuwashiro, S., Yamamoto, T., Koashi, M. & Imoto, N. Generation of high-fidelity four-photon cluster state and quantum-domain demonstration of one-way quantum computing. Phys. Rev. Lett. 100, 210501 (2008).  
15. Biggerstaff, D. N. et al. Cluster-state quantum computing enhanced by high-fidelity generalized measurements. Phys. Rev. Lett. 103, 240504 (2009).

16. Gao, W-B. et al. Experimental realization of a controlled-NOT gate with four-photon six-qubit cluster states. Phys. Rev. Lett. 104, 020501 (2010).  
17. Browne, D. E. & Rudolph, T. Resource-efficient linear optical quantum computation. Phys. Rev. Lett. 95, 010501 (2005).  
18. Dawson, C. M., Haselgrove, H. L. & Nielsen, M. A. Noise thresholds for optical cluster-state quantum computation. Phys. Rev. A 73, 052306 (2006).  
19. Gross, D., Flammia, S. T. & Eisert, J. Most quantum states are too entangled to be useful as computational resources. Phys. Rev. Lett. 102, 190501 (2009).  
20. Verstraete, F., Murg, V. & Cirac, J. I. Matrix product states, projected entangled pair states, and variational renormalization group methods for quantum spin systems. Adv. Phys. 57, 143-224 (2008).  
21. Popp, M., Verstraete, F., Martin-Delgado, M. A. & Cirac, J. I. Localizable entanglement. Phys. Rev. A 71, 042306 (2005).  
22. Gross, D. & Eisert, J. Quantum computational webs. Preprint at http://arXiv.org/abs/0810.2542 (2008).  
23. Hagiwara, M., Katsumata, K., Affleck, I., Halperin, B. I. & Renard, J. P. Observation of  $S = 1 / 2$  degrees of freedom in an  $S = 1$  linear-chain Heisenberg antiferromagnet. Phys. Rev. Lett. 65, 3181-3184 (1990).  
24. Buluta, I. & Nori, F. Quantum simulators. Science 326, 108-111 (2009).  
25. Howell, J. C., Lamas-Linares, A. & Bouwmeester, D. Experimental violation of a spin-1 bell inequality using maximally entangled four-photon states. Phys. Rev. Lett. 88, 030401 (2002).  
26. Lanyon, B. P. et al. Manipulating biphotonic qutrits. Phys. Rev. Lett. 100, 060504 (2008).  
27. Darmawan, A. S. & Bartlett, S. D. Optical spin-1 chain and its use as a quantum-computational wire. Phys. Rev. A 82, 012328 (2010).  
28. Jozsa, R. Fidelity for mixed quantum states. J. Mod. Opt. 41, 2315-2323 (1994).  
29. Kwiat, P. G., Waks, E., White, A. G., Appelbaum, I. & Eberhard, P. H. Ultrabright source of polarization-entangled photons. Phys. Rev. A 60, R773-R776 (1999).  
30. Lavoie, J., Kaltenbaek, R. & Resch, K. J. Experimental violation of Svetlichny's inequality. New J. Phys. 11, 073051 (2009).  
31. Mattle, K., Weinfurter, H., Kwiat, P.G. & Zeilinger, A. Dense coding in experimental quantum communication. Phys. Rev. Lett. 76, 4656-4659 (1996).

# Acknowledgements

We thank W. A. Coish and R. Prevedel for valuable discussions, and we thank A. C. Doherty, A. Gilchrist and M. D. de Burgh for making their semidefinite-programming tomography algorithm available to us. We are grateful for financial support from NSERC, OCE, CFI, QuantumWorks, MRI ERA and Industry Canada. S.D.B. is grateful for support from the Perimeter Institute.

# Author contributions

B.Z. and S.D.B. proposed the experiment and provided theoretical support. R.K., J.L. and K.J.R. designed the experiment. J.L. and R.K. carried out the experiment. R.K. analysed the data. All authors prepared the manuscript.

# Additional information

The authors declare no competing financial interests. Supplementary information accompanies this paper on www.nature.com/naturephysics. Reprints and permissions information is available online at http://npg.nature.com/reprintsandpermissions.

Correspondence and requests for materials should be addressed to R.K. or K.J.R.