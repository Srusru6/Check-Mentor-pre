ARTICLE

Received 8 Jul 2014 | Accepted 21 Oct 2014 | Published 25 Nov 2014

DOI: 10.1038/ncomms6617

# Hidden two-qubit dynamics of a four-level Josephson circuit

Elisha Svetitsky $^{1,\star}$ , Haim Suchowski $^{2,3,\star}$ , Roy Resh $^{1}$ , Yoni Shalibo $^{1}$ , John M. Martinis $^{4}$  & Nadav Katz $^{1}$

Multi-level control of quantum coherence exponentially reduces communication and computation resources required for a variety of applications of quantum information science. However, it also introduces complex dynamics to be understood and controlled. These dynamics can be simplified and made intuitive by employing group theory to visualize certain four-level dynamics in a 'Bell frame' comprising an effective pair of uncoupled two-level qubits. We demonstrate control of a Josephson phase qudit with a single multi-tone excitation, achieving successive population inversions between the first and third levels and highlighting constraints imposed by the two-qubit representation. Furthermore, the finite anharmonicity of our system results in a rich dynamical evolution, where the two Bell-frame qubits undergo entangling-disentangling oscillations in time, explained by a Cartan gate decomposition representation. The Bell frame constitutes a promising tool for control of multi-level quantum systems, providing an intuitive clarity to complex dynamics.

Quantum information science, where quantum dynamics meets information theory $^{1-3}$ , promises to revolutionize critical aspects of our ability to compute and communicate. The theoretical framework of quantum information calls for controlled quantum machinery, typically based on two-level transitions, coherence and readout, a.k.a. qubits. Many physical systems commonly used as qubits, such as trapped ions $^{4,5}$  and superconducting circuits $^{6,7}$ , are in reality multi-level systems whose dynamics are manually limited by researchers to two levels to preserve simplicity and fidelity. Such systems can easily be employed as multi-level qubits by accessing additional levels, allowing a significant reduction of the resources and gates required for a variety of quantum information applications $^{8-10}$ , yet also introducing a complex multi-level problem. The usefulness and popularity of multi-level qubits are limited by a dearth of theoretical methods for understanding and controlling their dynamics. In this paper we study the reduction of four-level dynamics to a pair of two-level qubits, providing a familiar geometric representation for a multi-level system. The recently proposed control scheme of Pythagorean coupling $^{11}$ , which introduces a family of solutions for successive complete inversions in a four-level system, is a suitable springboard for this purpose.

Continuous group theory plays a central role in quantum dynamical systems, providing powerful tools to describe their evolution in terms of quantum states and control operations $^{12-15}$ . For quantum information, the relevant groups are the SU(2) and SU(4) symmetry groups, which serve as building blocks of a universal quantum computer. The dynamics of a two-level quantum system is described by the SU(2) group, which is represented with 2 by 2 unitary matrices. Systems possessing this symmetry lend themselves to straightforward geometric interpretation as a Bloch vector, where a normalized quantum state is mapped to a point on a sphere. This picture is extremely useful in quantum information, as single-qubit gates rotate the Bloch vector and decoherence has the effect of pulling it towards the  $z$ -axis $^{16}$ . While SU(2) dynamics are used for local qubit manipulation, SU(4) dynamics allow nonlocal manipulation of qubit pairs. With the machinery of Cartan decomposition $^{17}$ , the SU(4) group can be factored into local qubit rotations and a nonlocal two-qubit entanglement operation. As the SU(4) group also describes a four-level quantum system, such a decomposition allows the dynamics of a four-level qudit to be mapped onto and subsequently visualized by a pair of coupled two-level qubits. Anticipating local control of the qubit pair as described below, we relate the 'Lab frame' qudit states  $\{|0\rangle, |1\rangle, |2\rangle, |3\rangle\}$  and the 'Bell frame' two-qubit states  $\{|00\rangle, |01\rangle, |10\rangle, |11\rangle\}$  through the following transformation:

$$
| 0 \rangle = \frac {| 0 0 \rangle + | 1 1 \rangle}{\sqrt {2}} \quad | 1 \rangle = \frac {| 0 1 \rangle + | 1 0 \rangle}{\sqrt {2}}
$$

$$
| 2 \rangle = \frac {| 0 1 \rangle - | 1 0 \rangle}{\sqrt {2}} \quad | 3 \rangle = \frac {| 0 0 \rangle - | 1 1 \rangle}{\sqrt {2}}.
$$

A unique subgroup of the full SU(4) is the SO(4), the Euclidean four-dimensional rotation symmetry, defined by six independent parameters. The useful identity  $\mathrm{SO}(4)\cong \mathrm{SU}(2)\otimes \mathrm{SU}(2)$  implies one-to-one mapping of the four-dimensional rotational dynamics to those of an uncoupled pair of Bloch vectors<sup>11</sup>. In other words, if the dynamics of a four-level qudit was limited to SO(4), the dynamics in the Bell frame would be comprised solely of single-qubit rotations without inter-qubit coupling (see Fig. 1).

We first note that a Hamiltonian generating SO(4) dynamics is  $H_{\mathrm{A}} = \sum_{i=1}^{3} V_{i-1,i} |i-1\rangle \langle i| + V_{i-1,i}^{*} |i\rangle \langle i-1|$ , which is readily realized in the laboratory on a system with a ladder-type level configuration. In the theory of Pythagorean coupling<sup>11</sup>, this

Figure 1 | The four-level Lab-frame system and the two-qubit Bell-frame system. (a) The phase  $\varphi$  of a flux-biased superconducting Josephson qudit  
![](images/b3ee5a5052240b9bf5ccd9ef969f52a31acc32e2bd9f6cc156b95facaa401439.jpg)  
is localized in a shallow potential well, giving rise to a number of anharmonically spaced energy levels. The multi-level qudit state is

![](images/637825cbb11d776ba266d15ac74e27f08ad7a6009fe53081a5e9d4568d2c1a29.jpg)  
measured by lowering the potential barrier, causing the phase to tunnel out of the shallow well. (b) The states of a four-level qubit can be mapped onto a pair of two-level qubits. For example, the two-qubit state  $\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$  depicted here by the Bloch spheres corresponds to the state  $|0\rangle$  of the physical Lab-frame qudit. SO(4) rotations in the Lab frame factor exactly into local rotations of the Bell-frame qubits, while SU(4) rotations couple them together. (c) The depicted two-qubit state  $\frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$

![](images/81433c945409197652a958b7c1758df65a9cf9f952600b33760cf55abb3ed554.jpg)  
corresponds to the state  $|2\rangle$  in the Lab frame. The Pythagorean coupling scheme achieves population inversion between the Lab-frame states  $|0\rangle$  and  $|2\rangle$  by synchronizing rotations of the Bell-frame qubits.

Hamiltonian is shown to cause complete population transfer between  $|0\rangle$  and  $|2\rangle$  in the Lab frame by rotating the  $\frac{|00\rangle + |11\rangle}{\sqrt{2}}$  state into the  $\frac{|01\rangle - |10\rangle}{\sqrt{2}}$  state in the Bell frame, contingent on the amplitudes  $(V_{01}, V_{12}, V_{23})$  being proportional to a primitive Pythagorean triple: for two odd integers  $p$  and  $q$ , the set  $(c, a, b) \equiv \left(\frac{p^2 + q^2}{2}, pq, \frac{p^2 - q^2}{2}\right)$  is a primitive Pythagorean triple, so called because  $c^2 = a^2 + b^2$  and the three elements do not possess a common divisor<sup>18</sup>. This solution for a four-level system stands in striking contrast to the resonant two-level problem, where complete population transfer is achievable for any coupling strength.

With Pythagorean coupling, complete population transfer to the third level is attained when both Bell-frame qubits simultaneously complete an odd number of half-rotations, which is equivalent to  $p$  and  $q$  obeying the constraint  $\frac{p}{q} = \frac{2m + 1}{2n + 1}$  for  $m, n \in \mathbb{Z}$ . Here we experimentally show the effect on four-level dynamics of this rationality condition, which is in essence the fingerprint of the two-qubit picture. Moreover, we show that our experimental system, based on the flux-biased Josephson phase qudit, not only offers an elegant and useful way for exploiting detunings and decoherences, but also allows exploring the strongly interacting regime. Harnessing the anharmonicity of the physical qudit thus opens a gateway for optimal control in multilevel circuits.

# Results

Experimental demonstration of Pythagorean coupling. Our four-level quantum system is a flux-biased Josephson phase circuit<sup>19</sup>. We sweep two numbers,  $p$  and  $q$ , in the range [0, 2] and for each pair generate the corresponding Pythagorean triple. We then multiply the Pythagorean triple by a Rabi frequency  $\Omega / 2\pi = 47.62\mathrm{MHz}$  to obtain the amplitudes  $(V_{01}, V_{12}, V_{23}) = \hbar \Omega \times (c, a, b)$  and synthesize a three-tone pulse  $V(t) = V_{01}\cos(\omega_{01}t) + \frac{1}{\sqrt{2}} V_{12}\cos(\omega_{12}t) + \frac{1}{\sqrt{3}} V_{23}\cos(\omega_{23}t)$ ,

where  $\hbar \omega_{i-1,i}$  is the energy spacing between levels  $i$  and  $j$  and the denominators serve as harmonic-approximate corrections for the stronger coupling of the radiation to higher oscillator modes. The drive produces the Hamiltonian  $H_{\mathrm{B}} = \sum_{i=1}^{3} \hbar \omega_{i-1,i}|i\rangle \langle i| + \sqrt{i} V|i\rangle \langle i-1| + \sqrt{i} V^{*}|i-1\rangle \langle i|$ . Each coupling term includes off-resonant terms (see Supplementary Note 1). In the rotating wave approximation, valid at low drive amplitudes or, alternatively, for large anharmonicity, the Hamiltonian reduces to the form of  $H_{\mathrm{A}}$ . In such a circuit, related SU(2)-like controls have been demonstrated by emulating larger spin-states[20]. Pythagorean coupling generalizes this control to a four-level system, with two separate oscillation frequencies and subsequent rich dynamics. The Bell-frame approach can also be viewed as an analogue simulation of any coupled two-qubit control[21].

For each pair of  $(p, q)$  values, we initially apply the corresponding three-tone pulse for a duration of 60 ns and measure the populations of the four qudit states. Figure 2a shows the results in what we call the  $pq$  plane, where the axes correspond to the  $(p, q)$  values used to generate the Pythagorean triple. We observe nine distinct third-level excitation peaks with  $p/q$  ratios of 1/1, 1/3, 1/5, 3/1, 3/3, 3/5, 5/1, 5/3, 5/5 and obtain a maximum excitation of  $56\%$ .

Figure 2b shows simulation using the Hamiltonian  $H_{\mathrm{A}}$  and decoherence assuming a Markovian noise source. Simulation and experiment agree very well for  $p, q < 1.5$  but begin to differ farther from the origin of the  $pq$  plane, where  $(p, q)$  values correspond to large drive amplitudes. We postpone discussion of this issue for the moment, and note that numerical simulation using the Hamiltonian  $H_{\mathrm{B}}$  fits the data remarkably well, reproducing even minor features both in the  $pq$  plane as well as in time-domain measurements (see Supplementary Figs 1,2).

Bell-frame constraints on Lab-frame dynamics. In the resonant two-level Rabi problem, changing the duration of the drive is equivalent to changing its amplitude; this is the well-known area theorem<sup>16</sup>. Similarly, as each point in the pq plane corresponds to a set of drive amplitudes, changing the pulse duration results in

the excitation peaks of Fig. 2a appearing at different  $(p, q)$  values. However, optimal population transfer between the first and third states always requires a rational value of  $p / q$ , as this is a simple consequence of the dynamics in the Bell frame.

To confirm that our qudit obeys this constraint, we sweep the pulse duration in the range 14-98 ns at intervals of 7 ns and measure the third-level population in the  $pq$  plane at each step. Figure 2c shows the locations of nine excitation peaks at different times as they move through the  $pq$  plane, each maintaining its characteristic value of the ratio  $p / q$ . This result showcases the physical importance and intuitive clarity of the Bell-frame dynamics, in contrast to the inherent complexity of multi-level dynamics.

SO(4)-SU(4) crossover. The difference between measurement and simulation shown in Fig. 2a,b is explained by noting that the Hamiltonian  $H_{\mathrm{B}}$  in the rotating wave approximation reduces to  $H_{\mathrm{A}}$  only in the limit of large anharmonicity. In the case of finite anharmonicity the off-resonant terms survive into the rotating frame. In this case,  $H_{\mathrm{B}}$  in the rotating frame can be written as the sum of  $H_{\mathrm{A}}$  and another matrix containing detuned coupling terms (see Supplementary Note 1). The latter operator takes the dynamics out of SO(4) into the full SU(4) dynamical space. As the identity  $\mathrm{SO}(4)\cong \mathrm{SU}(2)\otimes \mathrm{SU}(2)$  is central to the theory of Pythagorean coupling, this symmetry is of the essence. As the coupling amplitudes grow large the off-resonant correction to  $H_{\mathrm{A}}$  becomes significant and so does the deviation of the qudit dynamics from SO(4) rotations.

The experimental crossover from SO(4) to SU(4) dynamics is quantified by conducting a high-resolution measurement of the time-domain dynamics of the qudit population along the diagonal of the  $pq$  plane, sweeping the duration of the three-tone pulse in the range 1-200 ns (Fig. 3a). At lower amplitudes the excitation peaks of the  $|2\rangle$  state behave as predicted by Pythagorean coupling theory. At higher amplitudes we observe a chevron pattern, which is readily understood in the Bell frame where SU(4) dynamics are mapped to single-qubit rotations with the addition of inter-qubit coupling. This coupling term changes the qubit resonance frequencies, thus affecting their respective

![](images/63282e84eb0d99dc34ff4de85962b94ff9bc44d1b0430af36792aca3e39aac3d.jpg)

![](images/36ad0f305f31453f42fd1a4e08f782d751343d1b6905451a864964718f4ca2ee.jpg)

![](images/5b02e2e08cd975215c57618a115c1ba6ee935db947ead80c1f1912dba7f1791f.jpg)

![](images/7e4a274395d3d118e1f45c659bb08441a89864bece61cb13fa3371a56fd67b4b.jpg)

![](images/3ffd9be5d5c625f9ea7becf29cb3a9e0f9c4b68d5e311d8fb0af4b998ba494ce.jpg)  
Figure 2 | Pythagorean dynamics in the Lab frame. (a) Experimental data taken after a 60 ns three-tone pulse. Axes correspond to  $(p, q)$  values used to generate a primitive Pythagorean triple, which is multiplied by a Rabi frequency to produce three coupling amplitudes. Excitation peaks of the third level appear when the two Bell-frame qubits simultaneously complete an odd number of half-rotations. (b) Simulation with ideal (infinite) qudit anharmonicity. The dynamics factor into  $\mathrm{SU}(2) \otimes \mathrm{SU}(2)$  everywhere on the  $pq$  plane, producing a regular pattern of third-level excitation peaks. The deviation of the experimental results from ideal Pythagorean dynamics sufficiently far from the origin of the  $pq$  plane is attributed to the finite anharmonicity, and is probed by the higher drive amplitudes. (c) Third-level excitation peaks in the  $pq$  plane at different times. Each  $p/q$  ratio is characteristic of a particular excitation peak and is preserved over time. Peaks are measured at 7 ns increments and move towards the origin over time. The constraint of each peak to a straight line in the  $pq$  plane is the hallmark of SO(4) dynamics and is the Lab-frame expression of the synchronization of the Bell-frame qubits necessary for third-level excitation.

![](images/fdaa4bac4eeded02c547677ac134c5c6dab88fe2da33b58ae42a3be39770a573.jpg)

![](images/9831da4b97cf154a6c7d1834c37de57c5d33292df9e5115b9f1078a8e362143e.jpg)

![](images/c480508989acbbbdd4513f675dff4263b1bb17a26406f84bf94233d142c7a562.jpg)

![](images/427b8f862606ec96b1d1ee85cb56a143289ffaf19f4ff891ff4cb994620bdef1.jpg)

![](images/82f84e3b0f13ff69b592d584d64bff0e5a7a8d02de0fca1fde4088739f6c267a.jpg)  
Figure 3 | Impact of finite anharmonicity on Bell-frame dynamics. The transition from SU(4) to SO(4) dynamics is measured by scanning (vertical) along the diagonal  $(p = q)$  of the pq plane (with a distance  $r = \sqrt{p^2 + q^2}$ ) and sweeping (horizontal) the duration of the three-tone pulse in the range 1-200 ns. (a) Population of the third qudit level. At low amplitudes excitation peaks move towards the origin so that  $r \propto \frac{1}{\text{Time}}$  consistent with Pythagorean dynamics. At high amplitudes the dynamics transition from SO(4) to SU(4) because of the finite qudit anharmonicity. The larger group SU(4) does not factor into SU(2)  $\otimes$  SU(2), but rather includes a term that couples together the Bell-frame qubits. The coupling terms shift their respective resonance frequencies, resulting in the chevron pattern. (b) Calculated von Neumann entanglement entropy of the Bell-frame qubits using the relation  $S = -\operatorname{Tr}(\rho_{\mathrm{A}}\log_2\rho_{\mathrm{A}})$ , where  $\rho_{\mathrm{A}}$  is the reduced density matrix of one of the Bell-frame qubits. For low drive amplitudes where the dynamics factor into SU(2)  $\otimes$  SU(2) the entanglement entropy is constant and maximum. The coupling terms become visible at high drive amplitudes and induce disentanglement-entanglement oscillations in the time domain.

![](images/5720ddf444bab3d5a5732799bdc721631549dd0d124897b116326a0941c283d6.jpg)

detunings and Rabi oscillations. As the Bell-frame qubits are brought into resonance with their effective drives, their oscillation frequency decreases, manifesting as the chevron peak in the Lab-frame population.

This effect can be quantified by the bipartite entanglement in the Bell frame. Bipartite entanglement is parameterized by the von Neumann entropy, defined as  $S = -\mathrm{Tr}(\rho_{\mathrm{A}}\log_2\rho_{\mathrm{A}})$ , where  $\rho_{\mathrm{A}}$  is the reduced density matrix of one qubit[22]. Figure 3b shows the von Neumann entropy calculated from the Hamiltonian  $H_{\mathrm{B}}$ , ignoring decoherence to emphasize the point of interest. As the Lab-frame ground state corresponds to a maximally entangled state in the Bell frame, the von Neumann entropy attains its maximum value of unity. SO(4) operations do not affect the entanglement in the Bell frame, and accordingly for sufficiently low drive amplitudes the entropy retains its maximum value over time. In contrast, for large drive amplitudes the Bell-frame qubits are subjected to successive disentanglements and entanglements due to the  $\frac{\mathrm{SU}(4)}{\mathrm{SU}(2)\otimes\mathrm{SU}(2)}$  component of the control (see Supplementary Note 2), resulting in disruption of the Pythagorean dynamics.

# Discussion

In conclusion, we study the Bell-frame dynamics of a four-level system and demonstrate the first experimental implementation of a new coupling scheme—Pythagorean coupling, achieving population inversion between the ground state and the third state of a Josephson phase qudit with a single three-tone pulse. We obtain a peak third-level excitation of  $56\%$  consistent with simulation and qudit decoherence. The Bell-frame and Pythagorean dynamics apply to any generic four-level system, including longer coherence-time qubit circuits, such as the transmon/Xmon $^{23}$ , and the phase qudit was chosen for this work due to its highly convenient single-shot multi-level readout. Excitation of the third level depends strictly on the synchronization of the two Bloch vectors in the Bell frame, which is confirmed by following the excitation peaks through time in the  $pq$  plane. The finite anharmonicity of a physical qudit is shown to affect the dynamics by preventing their confinement to SO(4), causing oscillations in the Bell-frame bipartite entanglement entropy.

The two-qubit Bell frame was introduced through a transformation that exactly factors the SO(4) group, thus helping uncover Pythagorean coupling as a method for population inversion, but its usefulness is far from exhausted. Properly detuning certain couplings may counterbalance the limiting effect of finite anharmonicity discussed in this work; alternatively, finite anharmonicity can be exploited as a feature. Non-Pythagorean Bell-frame dynamics are also highly useful, especially when using quantum systems with more controllable couplings than diamond- or ladder-type configurations. We expect the inherent complexity of multi-level dynamics to undergo more simplifications as the Bell frame is explored for coupling and control of larger systems.

# Methods

Josephson circuit operation. The flux-biased Josephson phase qudit is magnetically coupled to an on-chip readout SQUID and cooled in a dilution refrigerator to a base temperature of  $\sim 20\mathrm{mK}$ . The phase of the Josephson junction is localized in a shallow potential well, giving rise to a number of anharmonic energy levels. The qudit state in the energy basis is measured via selective tunnelling of the phase to an adjacent deep well, which affects a detectable change in the SQUID critical current[24]. Measurements are averaged over  $\sim 1,000$  repetitions to obtain probabilities.

The qudit energy spectrum is controlled through a flux bias. The experiment was done with transition frequencies  $\omega_{01} / 2\pi = 6.730\mathrm{GHz}$ ,  $\omega_{12} / 2\pi = 6.613\mathrm{GHz}$  and  $\omega_{23} / 2\pi = 6.482\mathrm{GHz}$ . The relaxation and dephasing times of the  $|1\rangle$  state were measured to be  $T_{1} = 230$  ns and  $T_{2} = 110$  ns without echo. The three-tone microwave pulse irradiating the qudit is synthesized by an IQ-mixer modulating a carrier frequency of  $6.700\mathrm{GHz}$ . Other techniques are identical to those described in previous works on multi-level Josephson phase quudit's[25,26].

# References

1. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge University Press, 2000).  
2. DiVincenzo, D. P. The physical implementation of quantum computation. Fortschr. Phys. 48, 771-783 (2000).  
3. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
4. Cirac, J. I. & Zoller, P. Quantum computations with cold trapped ions. Phys. Rev. Lett. 74, 4091-4094 (1995).  
5. Monroe, C., Meekhof, D. M., King, B. E., Itano, W. M. & Wineland, D. J. Demonstration of a fundamental quantum logic gate. Phys. Rev. Lett. 75, 4714-4717 (1995).  
6. Wendin, G. & Shumeiko, V. S. Quantum bits with Josephson junctions. Low Temp. Phys. 33, 724-744 (2007).

7. Martinis, J. M. Superconducting phase qubits. Quantum Information Processing 8, 81-103 (2009).  
8. Lanyon, B. P. et al. Simplifying quantum logic using higher-dimensional Hilbert spaces. Nat. Phys. 5, 134-140 (2008).  
9. Reed, M. D. et al. Realization of three-qubit quantum error correction with superconducting circuits. Nature 482, 382-385 (2012).  
10. Fedorov, A., Steffen, L., Baur, M., da Silva, M. P. & Wallraff, A. Implementation of a Toffoli gate with superconducting circuits. Nature 481, 170-172 (2012).  
11. Suchowski, H., Silberberg, Y. & Uskov, D. Pythagorean coupling: complete population transfer in a four-state system. Phys. Rev. A 84, 013414 (2011).  
12. Deutsch, D. Quantum computational networks. Proc. Roy. Soc. Lond. A 425, 73-90 (1989).  
13. Lloyd, S. Almost any quantum logic gate is universal. Phys. Rev. Lett. 75, 346-349 (1998).  
14. Divincenzo, D. P. Two-bit gates are universal for quantum computation. Phys. Rev. A 51, 1015-1022 (1995).  
15. Barenco, A. et al. Elementary gates for quantum computation. Phys. Rev. A 52, 3427-3467 (1995).  
16. Allen, L. & Eberly, J. H. Optical Resonance and Two-Level Atoms (Dover Publications, 1987).  
17. Kraus, B. & Cirac, J. I. Optimal creation of entanglement using a two-qubit gate. Phys. Rev. A 63, 062309 (2001).  
18. Euclid. The Thirteen Books of the Elements (Dover Publications, 1956).  
19. Simmonds, R. W. et al. Decoherence in Josephson phase qubits from junction resonators. Phys. Rev. Lett. 93, 077003 (2004).  
20. Neeley, M. et al. Emulation of a quantum spin with a superconducting phase qudit. Science 325, 722-725 (2009).  
21. Bushev, P. et al. Multiphoton spectroscopy of a hybrid quantum system. Phys. Rev. B. 82, 134530 (2010).  
22. Bennett, C. H., Bernstein, J. H., Popescu, S. & Schumacher, B. Concentrating partial entanglement by local operations. Phys. Rev. A 53, 2046-2052 (1996).

23. Barends, R. et al. Coherent Josephson qubit suitable for scalable quantum integrated circuits. Phys. Rev. Lett. 111, 080502 (2013).  
24. Clarke, J. & Wilhelm, F. K. Superconducting quantum bits. Nature 453, 1031-1042 (2008).  
25. Shalibo, Y. et al. Quantum and classical chirps in an anharmonic oscillator. Phys. Rev. Lett. 108, 037701 (2012).  
26. Shalibo, Y. et al. Direct Wigner tomography of a superconducting anharmonic oscillator. Phys. Rev. Lett. 110, 100404 (2013).

# Acknowledgements

We acknowledge the support of ISF Bikura Grant No. 1567/12 and ERC Grant No. 335933. We thank Christiane Koch for fruitful discussion.

# Author contributions

E.S., H.S., R.R. and N.K. designed the experiment. E.S., R.R. and Y.S. set up the experimental infrastructure. J.M.M. and N.K. participated in fabrication of the phase qudit. E.S. took the data. E.S., H.S. and N.K. analysed the experimental results. E.S. and R.R. performed numerical simulations. E.S., H.S. and N.K. wrote the manuscript.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Svetitsky, E. et al. Hidden two-qubit dynamics of a four-level Josephson circuit. Nat. Commun. 5:5617 doi: 10.1038/ncomms6617 (2014).