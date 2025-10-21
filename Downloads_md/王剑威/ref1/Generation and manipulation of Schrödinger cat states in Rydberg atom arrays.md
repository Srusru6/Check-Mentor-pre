# REPORT

# QUANTUM PHYSICS

# Generation and manipulation of Schrödinger cat states in Rydberg atom arrays

A. Omran $^{1*}$ , H. Levine $^{1*}$ , A. Keesling $^{1}$ , G. Semeghini $^{1}$ , T. T. Wang $^{1,2}$ , S. Ebadi $^{1}$ , H. Bernien $^{3}$ , A. S. Zibrov $^{1}$ , H. Pichler $^{1,4}$ , S. Choi $^{5}$ , J. Cui $^{6}$ , M. Rossignolo $^{7}$ , P. Rembold $^{6}$ , S. Montangero $^{8}$ , T. Calarco $^{6,9}$ , M. Endres $^{10}$ , M. Greiner $^{1}$ , V. Vuletic $^{11}$ , M. D. Lukin $^{1}$ †

Quantum entanglement involving coherent superpositions of macroscopically distinct states is among the most striking features of quantum theory, but its realization is challenging because such states are extremely fragile. Using a programmable quantum simulator based on neutral atom arrays with interactions mediated by Rydberg states, we demonstrate the creation of "Schrodinger cat" states of the Greenberger-Horne-Zeilinger (GHZ) type with up to 20 qubits. Our approach is based on engineering the energy spectrum and using optimal control of the many-body system. We further demonstrate entanglement manipulation by using GHZ states to distribute entanglement to distant sites in the array, establishing important ingredients for quantum information processing and quantum metrology.

Greenberger-Horne-Zeilinger (GHZ) states constitute an important class of entangled many-body states (1). Such states provide an important resource for applications that range from quantum metrology (2) to quantum error correction (3). However, these are among the most fragile many-body states because a single error on any one of the  $N$  qubits collapses the superposition, resulting in a statistical mixture. Remarkably, despite their highly entangled nature, GHZ states can be characterized by just two diagonal and two off-diagonal terms in the  $N$ -particle density matrix. In contrast to quantifying the degree of entanglement in general many-body states, which is extremely challenging, the GHZ states are not necessarily entangled.

lenging (4-6), the GHZ state fidelity  $(\mathcal{F} > 0.5)$  constitutes an accessible witness for  $N$  -partite entanglement (7). For these reasons, GHZ state creation can serve as an important benchmark for characterizing the quality of any given quantum hardware. Such states have been previously generated and characterized by using systems of nuclear spins (8, 9), individually controlled optical photons (10-12), trapped ions (7, 13-15), and superconducting quantum circuits (16, 17). Large-scale superposition states have also been generated in systems of microwave photons (18) and atomic ensembles without individual particle addressing (2).

Here, we demonstrate the preparation of  $N$ -particle GHZ states

$$
\left| \mathrm {G H Z} _ {N} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 1 0 1 \dots \right\rangle + \left| 1 0 1 0 \dots \right\rangle\right) \tag {1}
$$

$^{1}$ Department of Physics, Harvard University, Cambridge, MA 02138, USA.  $^{2}$ Department of Physics, Gordon College, Wenham, MA 01984, USA.  $^{3}$ Institute for Molecular Engineering, University of Chicago, Chicago, IL 60637, USA.  $^{4}$ Institute for Theoretical Atomic Molecular and Optical Physics (ITAMP), Harvard-Smithsonian Center for Astrophysics, Cambridge, MA 02138, USA.  $^{5}$ Department of Physics, University of California, Berkeley, Berkeley, CA 94720, USA.  $^{6}$ Forschungszentrum Jülich, Institute of Quantum Control (PGI-8), D-52425 Jülich, Germany.  $^{7}$ Institute for Quantum Optics and Center of Integrated Quantum Science and Technology (IQST), Universität Ulm, D-89081 Ulm, Germany.  $^{8}$ Dipartimento di Fisica e Astronomia "G. Galilei," Università degli Studi di Padova and Istituto Nazionale di Fisica Nucleare (INFN), I-35131 Padova, Italy.  $^{9}$ Institute for Theoretical Physics, University of Cologne, D-50937 Cologne, Germany.  $^{10}$ Division of Physics, Mathematics and Astronomy, California Institute of Technology, Pasadena, CA 91125, USA.  $^{11}$ Department of Physics and Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, MA 02139, USA. *These authors contributed equally to this work †Corresponding author. E-mail: lukin@physics.harvard.edu

in a one-dimensional array of individually trapped neutral  $^{87}\mathrm{Rb}$  atoms, in which the qubits are encoded in an atomic ground state  $|0\rangle$  and a Rydberg state  $|1\rangle$  [phase convention is provided in (19)]. Our entangling operation relies on the strong van der Waals interaction between atoms in states  $|1\rangle$  and on engineering the energy spectrum of the quantum many-body system to allow for a robust quantum evolution from an initial product state to a GHZ state. For both generating and characterizing GHZ states (Fig. 1), all the atoms were homogeneously coupled to the Rydberg state  $|1\rangle$  by means of a two-photon transition with an effective coupling strength  $\Omega(t)$  and detuning  $\Delta(t)$  (20, 21). In addition, we used addressing beams to introduce local energy shifts  $\delta_{i}$  on specific sites  $i$

along the array (Fig. 1A). The resulting many-body Hamiltonian is

$$
\begin{array}{l} \frac {H}{\hbar} = \frac {\Omega (t)}{2} \sum_ {i = 1} ^ {N} \sigma_ {x} ^ {(i)} - \sum_ {i = 1} ^ {N} \Delta_ {i} (t) n _ {i} \\ + \sum_ {i <   j} \frac {V}{\left| i - j \right| ^ {6}} n _ {i} n _ {j} \tag {2} \\ \end{array}
$$

where  $\sigma_x^{(i)} = |0\rangle \langle 1|_i + |1\rangle \langle 0|_i$  is the qubit flip operator,  $\Delta_t(t) = \Delta (t) + \delta_i$  is the local effective detuning set by the Rydberg laser and the local light shift,  $n_i = |1\rangle \langle 1|_i$  is the number of Rydberg excitations on site  $i$ , and  $V$  is the interaction strength of two Rydberg atoms on neighboring sites. The separation between adjacent sites was chosen so that the nearest-neighbor interaction  $V = 2\pi \cdot 24\mathrm{MHz}\gg \Omega$  results in the Rydberg blockade (22-24), forbidding the simultaneous excitation of adjacent atoms into the state  $|1\rangle$ .

To prepare GHZ states, we used arrays with an even number  $N$  of atoms. For large negative detuning  $\Delta$  of the Rydberg laser, the many-body ground state of the Hamiltonian (Eq. 2) is  $|G_N\rangle = |0000\cdot \cdot \cdot \rangle$ . For large uniform positive detuning  $\Delta_{i} = \Delta$ , the ground-state manifold consists of  $N / 2 + 1$  nearly degenerate classical configurations with  $N / 2$  Rydberg excitations. These include in particular the two target antiferromagnetic configurations  $|A_N\rangle = |0101\dots 01\rangle$  and  $|\bar{A}_N\rangle = |1010\dots 10\rangle$  (25) as well as other states with nearly identical energy (up to a weak second-nearest neighbor interaction), with both edges excited, such as  $|10010\dots 01\rangle$ . To isolate a coherent superposition of states  $|A_N\rangle$  and  $|\bar{A}_N\rangle$ , we introduced local light shifts  $\delta_e$  using off-resonant laser beams at  $840~\mathrm{nm}$ , generated with an acousto-optic deflector (AOD), which energetically penalize the excitation of edge atoms (Fig. 1A) and effectively eliminate the contribution of undesired components. In this case, the ground state for positive detuning is given by the GHZ state  $(I)$ , and there exists in principle an adiabatic pathway that transforms the state  $|G_N\rangle$  into  $|\mathrm{GHZ}_N\rangle$  by adiabatically increasing  $\Delta(t)$  from negative to positive values (Fig. 1B).

In practice, the time necessary to adiabatically prepare such a GHZ state grows with system size and becomes prohibitively long for large  $N$ , owing to small energy gaps in the many-body spectrum. To address this limitation, we used optimal control methods to find laser pulses that maximize the GHZ state preparation fidelity while minimizing the amount of time necessary. Our specific implementation, the remote dressed chopped-random basis algorithm (RedCRAB) (26, 27), yields optimal shapes of the laser intensity and detuning for the given experimental conditions (19). For  $N \leq 8$  atoms, we performed this optimization using  $\delta_{e} / (2\pi) \approx -4.5$  MHz light shifts on the edge atoms. For larger systems of  $N > 8$ , the preparation was found to be more robust by increasing the edge light shifts to  $\delta_{e} / (2\pi) \approx -6$  MHz and adding  $\delta_{4,N-3} / (2\pi) \approx -1.5$  MHz light shifts on the third site from both edges.

Our experiments are based on the optical tweezer platform and experimental procedure described previously (21). After the initialization

of a defect-free  $N$ -atom array, the traps were switched off, while the atoms were illuminated with the Rydberg and local light shift beams. We subsequently measured the internal state of the atoms by imaging state  $|0\rangle$  atoms recaptured in the traps, while Rydberg atoms are repelled by the trapping light (28). The results of such experiments for a 20-atom array are demonstrated in Fig. 2. After applying the optimized pulse shown in Fig. 2B, we measured the probability of observing different patterns  $p_n = \langle n|\rho |n\rangle$  in the computational basis, where  $\rho$  is the density operator of the prepared state. The measured probability to observe each of the  $2^{20}$  possible patterns in a 20-atom array is shown in Fig. 2A. The states  $|\bar{A}_{20}\rangle$  and  $|\bar{A}_{20}\rangle$  clearly stand out (Fig. 2A, blue bars), with a combined probability of 0.585(14) and almost equal probability of observing each one.

To characterize the experimentally prepared state  $\rho$ , we evaluated the GHZ state fidelity

$$
\begin{array}{l} \mathcal {F} = \left\langle \mathrm {G H Z} _ {N} | \rho | \mathrm {G H Z} _ {N} \right\rangle \\ = \frac {1}{2} \left(p _ {A _ {N}} + p _ {\bar {A} _ {N}} + c _ {N} + c _ {N} ^ {*}\right) \tag {3} \\ \end{array}
$$

where  $p_{A_N}$  and  $p_{\bar{A}_N}$  are the populations in the target components, and  $c_{N} = \langle \bar{A}_{N}|\rho |A_{N}\rangle$  is the off-diagonal matrix element, which can be measured by using the maximal sensitivity of the GHZ state to a staggered magnetic field. Specifically, evolving the system with the Hamiltonian  $H_{p} = \hbar \delta_{p} / 2\sum_{i = 1}^{N}(-1)^{i}\sigma_{z}^{(i)}$ , the amplitude  $c_{N}$  acquires a phase  $\phi$  at a rate of  $\dot{\phi} = N\delta_p$ . Measuring an observable that oscillates at this frequency provides a lower bound on the coherence  $|c_{N}|$  through the oscillation contrast (I9, 29). In our experiments, the staggered field was implemented by applying off-resonant focused beams of equal intensity at  $420~\mathrm{nm}$ , generated by another AOD, to every other site of the array (Fig. 1C), resulting in a local energy shift  $\delta_p$  (27). Subsequently, we drove the atoms resonantly, applying a unitary operation  $\mathcal{U}_x$  in order to change the measurement basis (I9), so that a measurement of the parity  $\mathcal{P} = \prod_i\sigma_z^{(i)}$  becomes sensitive to the phase of  $c_{N}$ . The measured parity is shown in Fig. 2C as a function of the phase accumulated on each atom, demonstrating the coherence of the created state.

To extract the entanglement fidelity for large atomic states, we carefully characterized our detection process used to identify atoms in  $|0\rangle$  and  $|1\rangle$  because it had a small but finite error. We have independently determined the probability to misidentify the state of a particle to be  $p(1|0) = 0.0063(1)$  and  $p(0|1) = 0.0227(42)(19)$ . Subsequently, we used a maximum-likelihood estimation procedure to infer the properties of created states on the basis of the raw measurement results. Using this procedure, we inferred a probability of preparing states  $|\bar{A}_{20}\rangle$  and  $|\bar{A}_{20}\rangle$  to be 0.782(32) (Fig. 2A, orange bars) and an amplitude of oscillation of 0.301(18) (Fig. 2C, orange points). From these measurements, we extracted a lower bound for the 20-atom GHZ state fidelity of  $\mathcal{F} \geq 0.542(18)$ .

![](images/14208357f3e96eefd68485bda95e630239e266b76f502b7aa3f407d85e43fa16.jpg)  
A  
Fig. 1. Experimental scheme and entanglement procedure. (A)  $^{87}\mathrm{Rb}$

![](images/e9bf15172675e4db6bd8cae8060f55a3d7bb803292d099b013e827cc4b35b7ff.jpg)  
B

![](images/1af2d0229c9339693c4febbf7d113de4cd38ffad2a45ed105e23072e96e205f1.jpg)  
C

atoms initially in a ground state  $|0\rangle = |5S_{1 / 2},F = 2,m_F = -2\rangle$  are coupled to a Rydberg state  $|1\rangle = |70S_{1 / 2}$ $m_J = -1 / 2\rangle$  by a light field with a coupling strength  $\Omega /(2\pi)\leq 5$  MHz and a variable detuning  $\Delta$  . Local addressing beams at  $840~\mathrm{nm}$  target the edge atoms, reducing the energy of  $|0\rangle$  at those sites by a light shift  $\delta_{e}$  (B) Many-body energy gap spectrum of  $N = 8$  atoms, including energy shifts on the edge atoms. For positive detuning, the states with one ground-state atom on the edges are favored over states with a Rydberg atom on both edges. An adiabatic pathway connects the state  $|G_N\rangle = |000\dots \rangle$  with the two GHZ components. Gray lines in the spectrum are energies associated with antisymmetric states, which are not coupled to the initial state by the Hamiltonian Eq. 2. (C) Method to control the phase  $\phi$  of GHZ states. Every other site of the array is illuminated with a local addressing beam at  $420~\mathrm{nm}$  which imposes a negative differential light shift  $\delta_p$  on the  $|0\rangle$  -to-  $|1\rangle$  transition. The offset in state  $|0101\dots \rangle$  relative to  $|1010\dots \rangle$  leads to an evolving dynamical phase.

This protocol was applied for multiple system sizes of  $4 \leq N \leq 20$ , using  $1.1 - \mu s$  control pulses optimized for each  $N$  individually. Consistent with expected GHZ dynamics (Fig. 1C) (13), the frequency of the measured parity oscillations grows linearly with  $N$  (Fig. 3A). Extracting the GHZ fidelity from these measurements shows that we surpass the threshold of  $\mathcal{F} = 0.5$  for all system sizes studied (Fig. 3B and table S1). We further characterized the lifetime of the created GHZ state by measuring the parity signal after a variable delay (Fig. 3C). These observations are most consistent with Gaussian decay, while characteristic lifetimes are reduced relatively slowly for increasing system sizes, indicating the presence of a non-Markovian environment (3, 14).

As an application of our entanglement-manipulation technique, we demonstrate its use for entanglement distribution between distant atoms. Specifically, we consider the preparation of Bell states between atoms at the two opposite edges of the array. Our approach was based on first creating the GHZ state by using the above procedure, followed by an operation that disentangles all but two target atoms. The latter is realized by shifting the transition frequencies of the two target edge atoms by using two strong, blue-detuned addressing beams at  $420~\mathrm{nm}$ . Subsequently, we performed a reverse detuning sweep of the Rydberg laser that effectively disentangles all atoms except those at the edges. The resulting state corresponds to a coherent superposition of two pinned excitations that can be converted into a Bell state  $\left|\Phi^{+}\right\rangle = \left(|00\rangle +|11\rangle\right) / \sqrt{2}$  by apply

ing a resonant  $\pi /2$  pulse on the edge atoms (Fig. 4A).

To demonstrate this protocol experimentally, we prepared a GHZ state of eight atoms and turned on the detuned  $420\mathrm{-nm}$  addressing beams on the edge atoms, resulting in a shift of  $\delta_{1,\mathrm{S}} / (2\pi) = 6\mathrm{MHz}$ . We then used an optimized Rydberg laser pulse to distribute the entanglement and observed the patterns  $|0000000\rangle$  and  $|10000001\rangle$ , with a total probability of 0.729(9) after accounting for detection errors (Fig. 4B). We verified the coherence of the remote Bell pair by applying an additional  $\pi /2$  pulse with a variable laser phase and observed parity oscillations with an amplitude of 0.481(24) (Fig. 4C). Combining these results, we obtained the edge atom Bell state fidelity of 0.605(13).

Regarding our experimental observations, the optimal control provides a substantial improvement over naive analytic pulses (Fig. 3B) while bringing our protocol close to the speed set by a more conventional protocol of building up entanglement through a series of two-qubit operations (19). By contrast, a simple linear detuning sweep only allows for the creation of GHZ states for  $N \leq 16$  within a fixed  $1.1\text{-}\mu s$  window (Fig. 3B), even under ideal conditions. Our analysis reveals that the reason for this improvement stems from diabatic excitations and excitations in the many-body spectrum, related to the recently proposed mechanisms for quantum optimization speedup (19, 30, 31).

The measured entanglement fidelity is partially limited by imperfect qubit rotations used for parity measurements. Specifically, the qubit rotation operation  $\mathcal{U}_x$  in our experiment is induced

![](images/af6b4e308723d5d8da25f26ba445cae930e4fb2c03bc5c443fe020d27eddaf4e.jpg)  
Fig. 2. Characterization of a 20-atom GHZ state. (A) Probability of observing different patterns, showing a large population of the two target patterns out of  $2^{20} = 1,048,576$  possible states. Shown here are the raw measured values (blue bars) and the populations inferred by using maximum likelihood estimation (orange bars) for the two target states. (Insets) Fluorescence images of the two target patterns, where red circles mark empty sites corresponding to atoms in state |1>. (B) Optimal control pulse used for state preparation. (C) Parity oscillations produced by acquiring a relative phase between the GHZ components. We apply a staggered field with a shift of  $\delta_p / (2\pi) = \pm 3.8$  MHz on all sites, followed by an operation  $\mathcal{U}_x$  so that subsequent parity measurements are sensitive

![](images/d69cfa0242fc8b003acc7baeccf6eb8964bd8ef9b753e30c6cc98537c35f7915.jpg)  
to  $\phi$  (19). From the population measurement and the oscillation amplitude, we infer a lower bound on the 20-atom GHZ fidelity of  $\mathcal{F} \geq 0.542(18)$ . Error bars denote  $68\%$  confidence intervals.

![](images/e2b2687e940cecca4e4fb6922f48578f988b5e8cf253784817174b0cef5bdc5a.jpg)

Fig. 3. Quantifying entanglement for different system sizes. (A) Parity oscillations measured on different system sizes. We apply a staggered field with a shift of  $\delta_p / (2\pi) = \pm 3.8$  MHz on all sites and observe a scaling of the phase accumulation rate proportional to the system size  $N$ . (B) Inferred GHZ fidelity for different system sizes (orange circles) (19). Blue diamonds show the result of simulations that account for dephasing during state preparation, decay from off-resonant photon scattering, and imperfect detection of coherence through parity oscillations (19). Pale blue triangles show identical simulations for the initial guess pulses for the RedCRAB optimization, consisting of a  $T = 1.1~\mu s$  linear detuning sweep and  $\Omega(t) = \Omega_{\mathrm{max}}[1 - \cos^{12}(\pi t / T)]$ . The gray shaded area marks a region not measurable with our parity observable (19). (C) Lifetime of the GHZ state coherence. For all system sizes  $N$ , we measure the state parity after a variable delay following the GHZ state preparation, which (inset) decays to  
![](images/8d0cc28a5dddd9c8c12735db8e7c545b456af870dfa253bea30922973de6bdc7.jpg)  
zero. We fit the individual parity data to the tail of a Gaussian decay curve because we assume that the dephasing started during state preparation—before  $\tau = 0$ . The gray line shows a theoretical prediction with no free parameters, accounting for known dephasing mechanisms in our system.

![](images/13a172ee036849a191f86d278aa4f0e0f966bd30db7e20a04eee6e693296ea54.jpg)

![](images/ca9bc7055f53cc44ed04f24cce67a5f221cf940687a4ea4968bee18eeb8e8623.jpg)

by an interacting Hamiltonian, which complicates this step (19). The resulting evolution can be understood in terms of quantum many-body scars (21, 32), which gives rise to coherent qubit rotations, even in the presence of strong interactions. The deviations from an ideal parity measurement arise from the Rydberg blockade constraint and long-range interactions (19). These grow with the system size, resulting in finite fidelities even for a perfect initial GHZ

state (Fig. 3B, gray shaded area). Our quoted fidelity values do not include the correction for this imperfection and represent the lower bound on the actual GHZ state fidelities.

Entanglement generation, manipulation, and lifetime are further limited by several sources of decoherence. The finite temperature of the atoms leads to random Doppler shifts on every site as well as position fluctuations that influence interaction energies. These thermal de

phasing mechanisms lead to a Gaussian decay of the GHZ state coherence, whose time scale decreases with the system size as  $1 / \sqrt{N}$ , which is in good agreement with our observations (Fig. 3C). Additionally, off-resonant laser scattering introduces a small rate of decoherence on each site in the array. We found that numerical simulations of the state preparation accounting for these imperfections predict higher GHZ fidelities than those obtained experimentally

![](images/319cf826b5e84639a5c0ac5820406583c7c58ff29e455d177eb1ee074bb5fb1c.jpg)  
A

![](images/3b28173f29df398f239ac0b831015ed4eb85d26da5c83f8d54686408694250ae.jpg)  
B  
C  
Fig. 4. Demonstration of entanglement distribution. (A) Experimental protocol for  $N = 8$ . Edge atoms are addressed by light shift beams, and a reverse sweep of the Rydberg laser detuning is performed to disentangle the bulk of the array, leaving a Bell state  $|\Psi^{+}\rangle^{\infty}|1\dots 0\rangle +|0\dots 1\rangle$  on the edge. A  $\pi /2$  pulse resonant only with the edge atoms is applied to convert the state  $|\Psi^{+}\rangle$  to  $|\Phi^{+}\rangle^{\infty}|0\dots 0\rangle +|1\dots 1\rangle$ .

![](images/5960c7842c7bb799248965ede3dd570998db9f346f3ad10a1b319dfafa2d6ea5.jpg)

(B) Measured Rydberg populations on each site after entanglement distribution. (Inset) Probabilities for different patterns on the edge atoms, which are consistent with the Bell state  $|\Phi^{+}\rangle$ . Blue bars show the raw data, and orange bars are the statistically inferred probabilities given our detection errors. (C) Measurement of the Bell state coherence. GHZ entanglement is distributed to the edges, and a  $\pi /2$  pulse is applied at laser phase  $\phi = 0$ , followed by a second  $\pi /2$  pulse at varying phase  $\phi$ . The amplitude of the parity oscillation provides a lower bound on the coherence of the Bell state, yielding a fidelity of  $\mathcal{F} \geq 0.605(13)$ .

(Fig. 3B) (19). We can attribute this discrepancy to several additional sources of errors. Laser phase noise likely contributes to the finite fidelity of the state preparation. Drifts in the beam positions of the Rydberg lasers can lead to changing light shifts, giving rise to uncontrolled detunings, and drifts in the addressing beam positions can lead to an imbalance in the local energy shifts and thereby in the populations of the two GHZ components, limiting the maximum possible coherence. This analysis highlights the utility of GHZ states for uncovering sources of errors. We emphasize that all of these known error sources can be mitigated through technical improvements (19).

Our experiments demonstrate a new promising approach for the deterministic creation and manipulation of large-scale entangled states, enabling the realization of GHZ-type entanglement in system sizes of up to  $N = 20$  atoms. These results show the utility of this approach for benchmarking quantum hardware, demonstrating that Rydberg atom arrays constitute a competitive platform for quantum information science and engineering. Specifically, the entanglement generation and distribution could potentially be used for applications that range from quantum metrology and quantum networking to quantum error correction and quantum computation. Our method can be extended by mapping the Rydberg qubit states used here to ground-state hyperfine sublevels, so that the entangled atoms can remain trapped and maintain their quantum coherence over very long times (19, 23, 24, 33). This could enable the sophisticated manipulation of entanglement and realization of deep quantum circuits for applications such as quantum optimization (30, 31).

During the completion of this work, we became aware of related results that demonstrate

large GHZ state preparation using superconducting quantum circuits (34, 35).

# REFERENCES AND NOTES

1. D. M. Greenberger, M. A. Horne, A. Zeilinger, in Bell's Theorem, Quantum Theory and Conceptions of the Universe, M. Kafatos, Ed. (Springer 1989), pp. 69-72.  
2. L. Pezzè, A. Smerzi, M. K. Oberthaler, R. Schmied, P. Treutlein, Rev. Mod. Phys. 90, 035005 (2018).  
3. M. A. Nielsen, I. L. Chuang, Quantum Computation and Quantum Information: 10th Anniversary Edition (Cambridge Univ. Press, ed. 10, 2011).  
4. L. Amico, R. Fazio, A. Osterloh, V. Vedral, Rev. Mod. Phys. 80, 517-576 (2008).  
5. O. Gühne, G. Toth, Phys. Rep. 474, 1-75 (2009).  
6. R. Islam et al., Nature 528, 77-83 (2015).  
7. C. A. Sackett et al., Nature 404, 256-259 (2000).  
8. R. Lafflamme, E. Knill, W. H. Zurek, P. Catasti, S. V. S. Mariappan, Philos. Trans. R. Soc. London A 356, 1941-1948 (1998).  
9. P. Neumann et al., Science 320, 1326-1329 (2008).  
10. D. Bouwmeester, J.-W. Pan, M. Daniell, H. Weinfurter, A. Zeilinger, Phys. Rev. Lett. 82, 1345-1349 (1999).  
11. J.-W. Pan, M. Daniell, S. Gasparoni, G. Weihs, A. Zeilinger, Phys. Rev. Lett. 86, 4435-4438 (2001).  
12. X.-L. Wang et al., Phys. Rev. Lett. 120, 260502 (2018).  
13. D. Leibfried et al., Nature 438, 639-642 (2005).  
14. T. Monz et al., Phys. Rev. Lett. 106, 130506 (2011).  
15. N. Friis et al., Phys. Rev. X 8, 021012 (2018).  
16. L. Dicarlo et al., Nature 467, 574-578 (2010).  
17. C. Song et al., Phys. Rev. Lett. 119, 180511 (2017).  
18. B. Vlastakis et al., Science 342, 607-610 (2013).  
19. Materials and methods are available as supplementary materials.  
20. H. Labuhn et al., Nature 534, 667-670 (2016).  
21. H. Bernien et al., Nature 551, 579-584 (2017).  
22. D. Jaksch et al., Phys. Rev. Lett. 85, 2208-2211 (2000).  
23. T. Wilk et al., Phys. Rev. Lett. 104, 010502 (2010).  
24. L. Isenhower et al., Phys. Rev. Lett. 104, 010503 (2010).  
25. R. Islam et al., Science 340, 583-587 (2013).  
26. N. Rach, M. M. Müller, T. Calarco, S. Montangero, Phys. Rev. A 92, 062343 (2015).  
27. R. Heck et al., Proc. Natl. Acad. Sci. U.S.A. 115, E11231-E11237 (2018).  
28. S. de Leseleuc, D. Barredo, V. Lienhard, A. Browaeks, T. Lahaye, Phys. Rev. A 97, 053803 (2018).  
29. M. Gartner et al., Nat. Phys. 13, 781-786 (2017).  
30. E. Farhi, J. Goldstone, S. Gutmann, A quantum approximate optimization algorithm. arXiv:1411.4028 [quant-ph] (2014).

31. L. Zhou, S.-T. Wang, S. Choi, H. Pichler, M. D. Lukin, Quantum approximate optimization algorithm: Performance, mechanism, and implementation on near-term devices. arXiv:1812.01041 [quant-ph] (2018).  
32. C. J. Turner, A. A. Michailidis, D. A. Abanin, M. Serbyn, Z. Papić, Nat. Phys. 14, 745-749 (2018).  
33. C. J. Picken, R. Legaie, K. McDonnell, J. D. Pritchard, Quantum Sci. Technol. 4, 015011 (2018).  
34. C. Song et al., Observation of multi-component atomic Schrödinger cat states of up to 20 qubits. arXiv:1905.00320 [quant-ph] (2019).  
35. K. X. Wei et al., Verifying multipartite entangled GHZ states via multiple quantum coherences. arXiv:1905.05720 [quant-ph] (2019).

# ACKNOWLEDGMENTS

We thank D. Sels and C. Reimer for helpful discussions. Funding: The authors acknowledge financial support from the Center for Ultracold Atoms, the National Science Foundation, Vannevar Bush Faculty Fellowship, the U.S. Department of Energy, and the Office of Naval Research. H.L. acknowledges support from the National Defense Science and Engineering Graduate (NDSEG) fellowship. G.S. acknowledges support from a fellowship from the Max Planck/Harvard Research Center for Quantum Optics. J.C., S.M., and T.C. acknowledge funding from the EC H2020 grants 765267 (QuScO), 817482 (PASQuANS), and QuantERA QTFLAG; the DFG SPP 1929 (GiRyd) and TWITTER; the IQST Alliance; and the Italian PRIN 2017. Author contributions: A.O.,

H.L., A.K., G.S., T.T.W., S.E., H.B., A.S.Z., and M.E. built the experimental setup. A.O., H.L., A.K., and G.S. performed the measurements and analyzed the data. H.P., S.C., J.C., and S.M. performed theoretical analysis. J.C., M.R., P.R., S.M., and T.C. provided and maintained the optimal control server. All work was supervised by M.G., V.V., and M.D.L. All authors discussed the results and contributed to the manuscript. Competing interests: M.G., V.V., and M.D.L. have an equity interest in and serve on the advisory board of QuEra Computing. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and the supplementary materials.

# SUPPLEMENTARY MATERIALS

science.sciencemag.org/content/365/6453/570/suppl/DC1 Materials and Methods

Figs. S1 to S9

Table S1

References (36-55)

13 May 2019; accepted 8 July 2019

10.1126/science.aax9743

# Generation and manipulation of Schrödinger cat states in Rydberg atom arrays

A. Omran, H. Levine, A. Keesling, G. Semeghini, T. T. Wang, S. Ebadi, H. Bernien, A. S. Zibrov, H. Pichler, S. Choi, J. Cui, M. Rossignolo, P. Rembold, S. Montangero, T. Calarco, M. Endres, M. Greiner, V. Vuletic and M. D. Lukin

Science 365 (6453), 570-574. DOI: 10.1126/science.aax9743

# Entanglement goes large

The success of quantum computing relies on the ability to entangle large-scale systems. Various platforms are being pursued, with architectures based on superconducting qubits and trapped atoms being the most advanced. By entangling up to 20 qubits, Omran et al. and Song et al.—working with Rydberg atom qubits and superconducting qubits, respectively—demonstrate how far these platforms have reached. The demonstrated controllable generation and detection of entanglement on such quantum systems is promising for the development of large-scale quantum processors.

Science, this issue p. 570, p. 574

# ARTICLE TOOLS

http://science.sciencemag.org/content/365/6453/570

# SUPPLEMENTARY MATERIALS

http://science.sciencemag.org/content/suppl/2019/08/07/365.6453.570.DC1

# REFERENCES

This article cites 51 articles, 4 of which you can access for free http://science.sciencemag.org/content/365/6453/570#BIBL

# PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service