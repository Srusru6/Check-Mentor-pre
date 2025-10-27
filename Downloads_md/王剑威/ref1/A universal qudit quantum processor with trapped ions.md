# A universal qudit quantum processor with trapped ions

Martin Ringbauer  $①$ $\boxtimes$ , Michael Meth $^{1}$ , Lukas Postler $^{1}$ , Roman Stricker  $①$ , Rainer Blatt $^{1,2,3}$ , Philipp Schindler  $①$  and Thomas Monz  $①$

Most quantum computers use binary encoding to store information in qubits—the quantum analogue of classical bits. Yet, the underlying physical hardware consists of information carriers that are not necessarily binary, but typically exhibit a rich multilevel structure. Operating them as qubits artificially restricts their degrees of freedom to two energy levels<sup>1</sup>. Meanwhile, a wide range of applications—from quantum chemistry<sup>2</sup> to quantum simulation<sup>3</sup>—would benefit from access to higher-dimensional Hilbert spaces, which qubit-based quantum computers can only emulate<sup>4</sup>. Here we demonstrate a universal quantum processor using trapped ions that act as quuds with a local Hilbert-space dimension of up to seven. With a performance similar to qubit quantum processors<sup>5</sup>, this approach enables the native simulation of high-dimensional quantum systems<sup>3</sup>, as well as more efficient implementation of qubit-based algorithms<sup>6,7</sup>.

Quantum information processing (QIP) successfully builds on the paradigm of binary information processing that has fuelled classical computers for decades. Quantum bits, just like their classical counterparts, are two-level systems with basis states labelled  $|0\rangle$  and  $|1\rangle$ . The underlying physical systems, however, almost always consist of higher-dimensional Hilbert spaces that need to be artificially restricted to fit our binary paradigm. This multilevel structure presents a powerful resource for QIP. Using auxiliary levels as a cache memory for quantum information has enabled the implementation of highly complex quantum algorithms and dissipative processes<sup>1</sup>, as well as improved decomposition of multiqubit gates<sup>6</sup>. Much more substantial advantages, however, are expected when using multilevel systems as quuds (quantum digits) as the primary resource for computation for applications that are naturally formulated in high-dimensional Hilbert spaces, such as quantum simulation of lattice gauge models<sup>3</sup> or quantum chemistry<sup>2</sup>. Yet, experimental realizations of qudit control in various platforms are limited to proposals or proof-of-concept demonstrations<sup>9-18</sup>.

Compared with their binary counterpart, qubits feature nontrivial coherence $^{19}$ , which can be exploited in quantum sensing, as well as much richer entanglement structures $^{20}$ , which cannot be replicated with qubits $^{21}$ . Intuitively, although two-state superpositions are sufficient for phase estimation, tasks that involve the discrimination of multiple phase shifts $^{22}$  or estimation of multiparameter signals $^{23}$  necessarily require multilevel systems. Qudit entanglement, on the other hand, is essential, not only for our fundamental understanding of quantum entanglement $^{24}$  but also from a practical perspective, as it offers new avenues for quantum error correction (QEC) $^{21}$ . These features, combined with higher thresholds for topological QEC codes $^{25}$  and more efficient magic state distillation $^{26}$ ,

make qubits a prime candidate for the next generation of quantum devices.

Here we demonstrate a universal qudit trapped-ion quantum processor (TIQP) using the native multilevel structure of chains of  $^{40}\mathrm{Ca}^+$  ions. Building on the native interactions in the trapped-ion platform, we implement a universal gate set for qudit QIP at a performance approaching that of comparable qubit systems. We further introduce a scalable detection scheme that allows for full qudit readout and develop composite pulse techniques for crosstalk compensation.

Our quantum processor uses a string of  $^{40}\mathrm{Ca}^{+}$ ions in a linear Paul trap<sup>1</sup>. Quantum information is encoded in the  $S_{1/2}$  electronic ground state and the metastable  $D_{5/2}$  excited state, which has a lifetime of  $\tau_1 \approx 1.1$  s (Fig. 1). Two sets of permanent magnets generate a magnetic field of about  $4.2\mathrm{G}$ , which splits the ground state into two Zeeman sublevels ( $m = \pm 1/2$ ) separated by about  $11.7\mathrm{MHz}$ , and the excited state into six Zeeman sublevels ( $m = \pm 5/2$ ,  $\pm 3/2$ ,  $\pm 1/2$ ), with a splitting of about  $7\mathrm{MHz}$  between the adjacent states. This gives rise to ten allowed transitions due to the selection rules ( $\Delta m = 0$ ,  $\pm 1$ ,  $\pm 2$ ), with the coupling strength controlled by laser polarization and orientation of the magnetic field. These transitions differ in their sensitivity to magnetic-field fluctuations by up to a factor of five, such that optical qubits are typically encoded in the least-sensitive states, namely,  $|0\rangle = S_{1/2,-1/2}$  and  $|1\rangle = D_{5/2,-1/2}$ . However, with magnetic shielding, spin coherence times on the order of  $100\mathrm{ms}$ , which is at least three orders of magnitude larger than typical gate times, can be achieved for all transitions (Supplementary Information). Each  $^{40}\mathrm{Ca}^{+}$ ion, therefore, natively supports a qudit with eight levels, featuring a highly connected Hilbert space (Fig. 1).

Ions are initialized close to the electronic and motional ground state by optical pumping and a combination of Doppler cooling, polarization-gradient cooling $^{27}$  and resolved sideband cooling $^{1}$ . The native operations available in the TIQP are equatorial rotations on any  $S - D$  transition:

$$
\mathrm {R} ^ {i, j} (\theta , \phi) = \exp (- \mathrm {i} \theta \sigma_ {\phi} ^ {i, j} / 2), \tag {1}
$$

where  $\theta$  denotes the rotation angle;  $\sigma_{\phi}^{i,j} = (\cos(\phi)\sigma_x^{i,j} \pm \sin(\phi)\sigma_y^{i,j})$  for Pauli matrices  $\sigma_x, \sigma_y$  and  $\sigma_z$ ; and  $i$  and  $j$  indicate the addressed transition according to Fig. 1. Note that the phase rotation for  $\phi$  in  $\sigma_{\phi}^{i,j}$  is positive (negative) when  $|i\rangle$  ( $|j\rangle$ ) is in the  $S$  manifold (that is, lower energy). The rotations (equation (1)) enable arbitrary SU(2) operations and are thus universal for qubit quantum computing[28] when combined with a two-qubit entangling operation such as the Mølmer-Sørensen gate[29]:

![](images/d5af0168891cb66e38960a5a5f5ba28741e1d84f39fdf8883f837bc63faf468f.jpg)  
Fig. 1 | Level scheme of the  $^{40}\mathrm{Ca}^+$  ion. Quantum information is encoded in the  $S_{1/2}$  and  $D_{5/2}$  states, where each transition between  $S$  and  $D$  is accessible using a single narrowband laser at  $729\mathrm{nm}$ .

$$
\mathrm {M S} ^ {i, j} (\theta , \phi) = \exp \left(- \frac {\mathrm {i} \theta}{4} \left(\sigma_ {\phi} ^ {i, j} \otimes \mathbb {1} + \mathbb {1} \otimes \sigma_ {\phi} ^ {i, j}\right) ^ {2}\right). \tag {2}
$$

This interaction is achieved by coupling the internal degrees of freedom of the ions to the common motion in the trap using a bichromatic light field. Using multiple focused laser beams, entangling gate operations can also be performed on arbitrary subsets of ions in the string (Supplementary Information). All the native operations can be performed with error rates below  $1\%$  and at least three orders of magnitude faster than the coherence time of the system<sup>5</sup>. Finally, the state of each ion is readout by electron shelving using the short-lived  $S_{1/2} \leftrightarrow P_{1/2}$  transition and detecting fluorescence on a charge-coupled device camera.

We now demonstrate how to extend the above platform to qudit up to dimension seven (one level remains unoccupied for readout). As for qubits, this requires arbitrary single-qudit gates, supplemented with one two-qudit entangling gate<sup>30</sup>. For simplicity, we will primarily focus on  $d = 3$  (qutrits) or  $d = 5$  (ququints) and outline generalizations to other dimensions.

The set of local operations on a qudit is described by the group  $\mathrm{SU}(d)$ . In the case of a qutrit, the Lie algebra of  $\mathrm{SU}(3)$  is spanned by Gell-Mann matrices<sup>31</sup>, which are a natural generalization of the Pauli matrices from  $\mathrm{SU}(2)$  to  $\mathrm{SU}(3)$ , with further generalizations towards  $\mathrm{SU}(d)$ . The Gell-Mann matrices are a set of traceless, Hermitian matrices, satisfying  $\mathrm{Tr}[\lambda_i\lambda_j] = 2\delta_{ij}$ , where  $\delta_{ij}$  is the Kronecker delta:

$$
\lambda_ {1} = \left( \begin{array}{c c c} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), \lambda_ {2} = \left( \begin{array}{c c c} 0 & - i & 0 \\ i & 0 & 0 \\ 0 & 0 & 0 \end{array} \right), \lambda_ {3} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & 0 \end{array} \right),
$$

$$
\lambda_ {4} = \left( \begin{array}{l l l} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{array} \right), \lambda_ {5} = \left( \begin{array}{l l l} 0 & 0 & - i \\ 0 & 0 & 0 \\ i & 0 & 0 \end{array} \right), \tag {3}
$$

$$
\lambda_ {6} = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right), \lambda_ {7} = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & - i \\ 0 & i & 0 \end{array} \right), \lambda_ {8} = \frac {1}{\sqrt {3}} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & - 2 \end{array} \right).
$$

Notably, one can identify three independent SU(2) sub-algebras:  $\{\lambda_1,\lambda_2,\lambda_3\}$ ,  $\{\lambda_4,\lambda_5,(\lambda_3 + \sqrt{3}\lambda_8) / 2\}$  and  $\{\lambda_6,\lambda_7,(-\lambda_3 + \sqrt{3}\lambda_8) / 2\}$ . This reflects the physical implementation in the trapped-ion platform via two-level couplings and makes the Gell-Mann operations a natural starting point for a qudit quantum processor.

Beyond basis operations, an important class of single-qudit gates is the Clifford group, as used in  $\mathrm{QEC}^{32}$ . Following Ref.  $^{33}$ , we introduce generalized Pauli  $Z$  and  $X$  operations:

$$
Z _ {d} = \sum_ {j} \omega_ {d} ^ {j} | j \rangle \langle j |, \tag {4}
$$

$$
X _ {d} = \sum_ {j} | j + 1 (\mod d) \rangle \langle j |, \tag {5}
$$

where  $\omega_{d} = \mathrm{e}^{\frac{2\pi i}{d}}$  and  $\{|j)\}_{j=0}^{d-1}$  denotes the computational basis in dimension  $d$ . These operations generate the  $d$ -dimensional analogue of the Pauli group, from which one constructs the  $d$ -dimensional Clifford group, with the following generators:

$$
H _ {d} = \frac {1}{\sqrt {d}} \sum_ {j, k} \omega_ {d} ^ {j k} | k \rangle \langle j |, \tag {6}
$$

$$
S _ {d} = \sum_ {j} \omega_ {d} ^ {j (j + 1) / 2} | j \rangle \langle j |. \tag {7}
$$

Achieving universal single-qudit operations requires not only Clifford gates but also one additional non-Clifford gate. A popular choice for such a gate is the  $\pi /8$  or 'T' gate $^{32}$ , which, for qutrits, is given by $^{34}$

$$
T _ {3} = \left( \begin{array}{l l} 1 & 0 \\ 0 & \mathrm {e} ^ {\frac {2 \pi \mathrm {i}}{9}} \\ 0 & 0 \end{array} \right). \tag {8}
$$

In our TIQP, any single-qudit operation can be constructed from at most  $\mathcal{O}(d^2)$  two-level rotations of equation (1) via a decomposition into Givens rotations $^{30}$  (Supplementary Information). A notable challenge in qudit compared with qubit QIP is that the elementary two-level operations lose their 'global-phase' gauge freedom. For example, a qubit  $Z$  rotation by an angle  $\theta$  can be understood as a phase shift  $\theta$  applied to  $|1\rangle$ , or equivalently as phase shifts of  $\pm \theta / 2$  applied to  $|0\rangle$  and  $|1\rangle$ , respectively. In the qudit case, this equivalence breaks down, because any phase shift is measured relative to the spectator level. Supplementary Information discusses how to overcome this technical challenge when decomposing qudit gates.

Experimentally, we demonstrate universal single-qutrit control in an eight-ion register by implementing the fundamental Gell-Mann rotations of equation (3), as well as the Clifford  $+\mathrm{T}$  gate set of equations (5)-(8). Supplementary Information shows the process tomography results for each of these operations. To benchmark the performance of our single-qudit operations in a way that is not limited by state-preparation-and-measurement errors, we perform randomized benchmarking of the qutrit and ququint Clifford operations[35] (Fig. 2 and Supplementary Information). For qutrits and ququints, we obtain error rates per Clifford operation of  $2(2)\times 10^{-3}$  and  $1.0(2)\times 10^{-2}$ , respectively, compared with the average error for a qubit Clifford gate of  $6(3)\times 10^{-4}$ . Uncertainties on all the quantities and data points correspond to one standard deviation, unless stated otherwise. Crucially, the increase in error rate with qudit dimension is primarily due to the fact that the number of laser pulses required for a quudit Clifford gate scales quadratically with the dimension. The error rate per laser pulse, on the other hand, remains comparable for increasing dimension, which indicates that the system performance does not degrade with qudit dimension. In case this quadratic overhead in the number of laser pulses is limiting, such as for very high-dimensional systems, it may be beneficial to explore native single-qudit gate schemes via multiple driving fields[22]. The measured error rates also compare well with the thresholds for QEC, which, for qubits, are as high as  $\approx 1\%$  (ref. [36]) and are expected to improve further with qudit dimension[25].

![](images/e69de4922c95e1fe68966307a380dffc6c7981c93d770c3f8b3c31ccbb47f4db.jpg)  
Fig. 2 | Single-qudit randomized benchmarking in an eight-ion register.

For increasingly long sequences of randomly chosen Clifford-gate decompositions of the identity, we measure the survival probability as the fraction of runs where the system ends in the initial state  $|0\rangle$ . From a fit to the decay of the average survival probability, we can estimate the average error per gate<sup>35</sup> (Supplementary Information). For qubits (blue data points), qubits (orange data points) and ququints (green data points), we obtain average Clifford error rates of  $6(3)\times 10^{-4}$ ,  $2(2)\times 10^{-3}$  and  $1.0(2)\times 10^{-2}$ , respectively. For each length, we performed at least 20 random sequences (data points), with the mean shown in red. The fits to the mean (blue, orange and green lines) and the  $99\%$  confidence interval of the mean (shaded regions) are shown, too.

Completing the universal toolbox requires at least one qudit entangling gate. The most basic choice here is a two-level controlled-NOT (CNOT) gate embedded in a qudit Hilbert space. We call this a controlled-exchange (CEX) gate since it exchanges two states, namely,  $|t_1\rangle$  and  $|t_2\rangle$ , of the target qudit if and only if the control qudit is in state  $|c\rangle$ :

$$
\mathrm {C E X} _ {c, t _ {1}, t _ {2}}: \left\{\begin{array}{l l}| c, t _ {1} \rangle \leftrightarrow | c, t _ {2} \rangle\\| j, k \rangle \rightarrow | j, k \rangle&\text {f o r} j \neq c, k \neq t _ {1}, t _ {2}.\end{array}\right. \tag {9}
$$

A slightly generalized version of the CEX gate is the controlled-increment (CINC) gate $^{30}$ , which increments the state of the target qudit by 1, if and only if the control qudit is in the state  $d - 1$ :

$$
\operatorname {C I N C}: \left\{\begin{array}{l l}| j, k \rangle \rightarrow | j, k \rangle&\text {i f} j <   d - 1\\| j, k \rangle \rightarrow | j, k \oplus 1 \rangle&\text {i f} j = d - 1\end{array}, \right. \tag {10}
$$

where  $\oplus$  denotes the addition modulo  $d$ . Other entangling gates, such as the controlled-sum gate (CSUM $|i\rangle|j\rangle = |i\rangle|j + i\rangle$ ) can be obtained from multiple applications of CINC or CEX gate.

The most direct way to implement two-qudit gates, which we follow here, is to decompose them into two-level rotations, as per equation (1), and two-level MS gates, as per equation (2). A crucial challenge here is again the 'global' phase factor  $(\exp (\mathrm{i}\theta /2))$  of the MS gate, which imparts unwanted phases on the spectator states (Supplementary Information provides the details and design considerations). In the case of the CEX gate, we find a decomposition up to a phase into 2 two-level MS gates independent of the qudit dimension; for the CINC gate, we require  $2d$  MS gates. Other two-qudit gates can be synthesized in a similar fashion. Alternatively, one could directly generalize the MS gate to a native qudit gate by simultaneously driving multiple transitions. This reduces the gate count,

however, only at the cost of increased complexity of the classical control system and more challenging experimental calibration<sup>37</sup>.

Experimentally, we estimate the error rates of the CEX and CINC gates by applying a sequence of entangling gates of increasing length to a fixed input state and measuring both the fraction of runs that end in the correct state (population) and the contrast of the resulting interference fringes (coherence) (Fig. 3 and Supplementary Information). Fitting the average of these values, we obtain error estimates of  $0.050(3)$  and  $0.082(1)$  for the CEX and CINC gates, respectively, compared with  $0.031(1)$  for a standard qubit MS gate. The achievable error rates are limited by the relatively low trap frequency of  $\approx 470\mathrm{kHz}$ , chosen to suppress crosstalk errors at the cost of amplifying errors due to motional heating and decoherence (Supplementary Information). This could be alleviated by using improved addressing optics, coupling to radial motional modes or using detuned MS gates[39-45] with qudit phase tracking. Importantly, however, the error rates are consistent with the performance of the individual two-level building blocks, indicating that the entangling gate performance does not degrade with qudit dimension.

The final challenge is quudit readout, which requires us to distinguish  $d$  different states, whereas conventional fluorescence

![](images/2f69e65044aa7699f573d03ef4f0c644cc61ee57ea16dc5e5d09d1e237a89136.jpg)

![](images/c8e2fc3e9202c8db2e6218b9ffbe64b6217c49e44dda12236c2e56de58a548f8.jpg)  
Fig. 3 | Qutrit entangling gates in an eight-ion register. a, Experimentally measured truth table for a CINC gate with 100 shots per measurement basis. b, Fidelity decays for a CEX gate in a qutrit Hilbert space and a qutrit CINC gate with initial states  $(|0\rangle + |1\rangle)$ $|0\rangle / \sqrt{2}$  and  $(|0\rangle + |2\rangle)$ $|0\rangle / \sqrt{2}$ , respectively. The data points correspond to the average of population and coherence of the output state at each sequence length, with the error bars representing one standard deviation of quantum shot noise for 100 shots per measurement (Supplementary Information). The lines are exponential fits from which we extract the average fidelity values, and the shaded regions represent  $95\%$  confidence intervals of the mean. Note that the different number of data points is due to the periodicity of 2 for the CEX gate and 3 for the CINC gate.

![](images/bb3d64fe632481490041302441c558416611f75b57c0a6e2fd0b99e2c76f80b9.jpg)  
a

![](images/9e50e55183ee54c1add6aebca3cb694fbc141f3626c4fd5f4204afd254d115c2.jpg)  
b

![](images/013587b73dd12540f8452217bb9b6c20335710131428389cade5f43b70e4e6c0.jpg)  
c  
Fig. 4 | Full qudit readout. a, Qudit readout is achieved by successive electron shelving and scattering steps with interleaved re-cooling.

b, Qudit-readout pulse sequence, consisting of Doppler cooling (DC), polarization gradient cooling (PGC), sideband cooling (SBC), the experimental sequence and a final sequence of fluorescence detections (Det) and re-cooling steps (DC/PGC). c, Qudit readout error. The data points represent the measured discrimination uncertainty between the bright and dark states at a given measurement time. The solid blue line indicates the fit to these data with  $99\%$  confidence regions on the mean in orange. The dotted blue line represents the error from spontaneous decay for two detections (qutrit), with  $2,500\mu s$  of polarization-gradient cooling between detections. The combined detection error in the worst case is given by the dashed black line, indicating an optimum of  $3\times 10^{-3}$  for  $500\mu s$  detection time. For reference, the grey dashed lines indicate the detection error for the qubit and  $d = 7$  cases.

readout can only distinguish the  $S$  and  $D$  manifold. To circumvent this problem, we employ a sequential readout scheme<sup>10</sup>. First, we shelve the  $|2\rangle$  state to the  $D$  manifold (thus, one of the eight levels needs to remain unpopulated). Then, we perform a standard fluorescence readout, which projects each ion in the string onto  $\{|0\rangle \langle 0|, \mathbb{1} - |0\rangle \langle 0|\}$ , allowing us to identify the  $|0\rangle$  state without perturbing the rest. This is followed by a reordering pulse, which brings the state  $|1\rangle$  into the  $S$  manifold and another fluorescence readout. This sequence is repeated until the state of all the ions is identified, which lets us assign a unique qudit quantum state to the string of ions. The readout time for this scheme increases only linearly with the qudit dimension (Fig. 4a).

An additional challenge with longer strings of ions is scattering-induced heating of the ion crystal. This increases the error rate of subsequent reordering pulses and therefore contributes to detection errors. We counter this effect by applying broadband polarization-gradient cooling between detection events (Fig. 4b). This unavoidably increases the time required for a full readout,

leading to a qutrit readout error of  $\approx 3\times 10^{-3}$  for  $500\mu s$  detection time and  $2,500\mu s$  re-cooling time compared with  $\approx 5\times 10^{-4}$  for qubits. Note, however, that this is a worst-case error, since those states measured earlier will experience lower spontaneous decay errors than those measured later. Although this readout error is already well below other error sources, it could be further reduced by about an order of magnitude by using fast re-cooling techniques<sup>1</sup> and more efficient collection optics<sup>38</sup>. With these improvements, we anticipate that a readout error on the order of  $10^{-3}$  or better can be achieved up to a dimension of seven.

We demonstrate a universal qudit quantum processor built on state-of-the-art trapped-ion hardware. Our approach requires only a minimal overhead in classical control capabilities and can be integrated into existing experiments. Although a qudit approach is expected to benefit a large part of QIP<sup>7</sup>, we particularly highlight those applications that are naturally formulated in terms of high-dimensional Hilbert spaces, such as higher spin models, quantum chemistry<sup>2</sup> and quantum simulation of lattice gauge theories<sup>3</sup>. Translating these applications into qubits leads to significant overheads, not only in the number of quantum particles required, but particularly in terms of interactions where two-qudit interactions are turned into multiqubit interactions, which are often extremely demanding to realize. Hence, the slightly lower fidelities achieved in a qudit quantum processor are more than compensated by the gain in efficiency for many high-profile applications (Supplementary Information).

Two key challenges for getting the best performance out of qudit hardware are (1) low crosstalk errors due to the large number of local operations required and (2) fast re-cooling and readout capabilities to reduce state-preparation-and-measurement errors. Improvements to the optics and control electronics could improve these numbers by at least an order of magnitude with current technology. Finally, the higher number of accessible carrier transitions in a qudit makes collisions between carrier transitions and motional sidebands more likely compared with a qubit system. Hence, for working with larger chains of quitts with more motional modes, a somewhat larger magnetic field on the order of  $10\mathrm{G}$  is desirable to ensure sufficient spectral separation. Such magnetic fields are easily achieved with permanent magnets and are not expected to cause any additional complications. Conceptually, an important challenge for making the best use of the system we present remains in compiling quantum algorithms into the qudit framework. To facilitate such a compilation, it will be highly beneficial to complement the embedded two-level entangling gates we present here with a suite of native qudit entangling gates[37] and genuine multilevel entangling gates for different dimensions. Explicit proposals for trapped-ion implementations of such gates remain lacking, making this a crucial area for further research.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41567-022-01658-0.

Received: 23 July 2021; Accepted: 30 May 2022

Published online: 21 July 2022

# References

1. Schindler, P. et al. A quantum information processor with trapped ions. New J. Phys. 15, 123012 (2013).  
2. MacDonell, R. J. et al. Analog quantum simulation of chemical dynamics. Chem. Sci. 12, 9794-9805 (2021).  
3. Rico, E. et al. SO(3) 'nuclear physics' with ultracold gases. Ann. Phys. 393, 466-483 (2018).

4. Bullock, S., O'Leary, D. & Brennen, G. Asymptotically optimal quantum circuits for  $d$ -level systems. Phys. Rev. Lett. 94, 230502 (2005).  
5. Bermudez, A. et al. Assessing the progress of trapped-ion processors towards fault-tolerant quantum computation. Phys. Rev. X 7, 041061 (2017).  
6. Lanyon, B. P. et al. Simplifying quantum logic using higher-dimensional Hilbert spaces. Nat. Phys. 5, 134-140 (2008).  
7. Wang, Y., Hu, Z., Sanders, B. C. & Kais, S. Qudits and high-dimensional quantum computing. Front. Phys. 8, 589504 (2020).  
8. Martinez, E. A. et al. Real-time dynamics of lattice gauge theories with a few-qubit quantum computer. Nature 534, 516-519 (2016).  
9. Senko, C. et al. Realization of a quantum integer-spin chain with controllable interactions. Phys. Rev. X 5, 021026 (2015).  
10. Leupold, F. M. et al. Sustained state-independent quantum contextual correlations from a single ion. Phys. Rev. Lett. 120, 180401 (2018).  
11. Malinowski, M. et al. Probing the limits of correlations in an indivisible quantum system. Phys. Rev. A 98, 050102 (2018).  
12. Ahn, J., Weinacht, T. & Bucksbaum, P. Information storage and retrieval through quantum phase. Science 287, 463-465 (2000).  
13. Godfrin, C. et al. Operating quantum states in single magnetic molecules: implementation of Grover's quantum algorithm. Phys. Rev. Lett. 119, 187702 (2017).  
14. Anderson, B. E., Sosa-Martinez, H., Riofrio, C. A., Deutsch, I. H. & Jessen, P. S. Accurate and robust unitary transformations of a high-dimensional quantum system. Phys. Rev. Lett. 114, 240401 (2015).  
15. Morvan, A. et al. Qutrit randomized benchmarking. Phys. Rev. Lett. 126, 210504 (2021).  
16. Hu, X.-M. et al. Beating the channel capacity limit for superdense coding with entangled ququarts. Sci. Adv. 4, eaat9304 (2018).  
17. Weggemans, J. R. et al. Solving correlation clustering with QAOA and a Rydberg qudit system: a full-stack approach. Quantum 6, 687 (2022).  
18. Kasper, V. et al. Universal quantum computation and quantum error correction with ultracold atomic mixtures. Quantum Sci. Technol. 7, 015008 (2022).  
19. Ringbauer, M. et al. Certification and quantification of multilevel quantum coherence. Phys. Rev. X 8, 041007 (2018).  
20. Kraft, T., Ritz, C., Brunner, N., Huber, M. & Gühne, O. Characterizing genuine multilevel entanglement. Phys. Rev. Lett. 120, 060502 (2018).  
21. Scott, A. J. Multipartite entanglement, quantum-error-correcting codes, and entangling power of quantum evolutions. Phys. Rev. A 69, 052330 (2004).  
22. Shlyakhov, A. R. et al. Quantum metrology with a transmon qutrit. Phys. Rev. A 97, 022115 (2018).  
23. Kristen, M. et al. Amplitude and frequency sensing of microwave fields with a superconducting transmon qudit. npj Quantum Inf. 6, 57 (2020).  
24. Huber, M. & de Vicente, J. I. Structure of multidimensional entanglement in multipartite systems. Phys. Rev. Lett. 110, 030501 (2013).  
25. Campbell, E. T. Enhanced fault-tolerant quantum computing in  $d$ -level systems. Phys. Rev. Lett. 113, 230501 (2014).

26. Campbell, E. T., Anwar, H. & Browne, D. E. Magic-state distillation in all prime dimensions using quantum Reed-Muller codes. Phys. Rev. X 2, 041021 (2012).  
27. Joshi, M. K. et al. Polarization-gradient cooling of 1D and 2D ion Coulomb crystals. New J. Phys. 22, 103013 (2020).  
28. Barenco, A. et al. Elementary gates for quantum computation. Phys. Rev. A 52, 3457-3467 (1995).  
29. Sorensen, A. & Molmer, K. Entanglement and quantum computation with ions in thermal motion. Phys. Rev. A 62, 022311 (2000).  
30. Brennen, G. K., Bullock, S. S. & O'Leary, D. P. Efficient circuits for exact-universal computations with qubits. Quantum Inf. Comput. 6, 436-454 (2005).  
31. Gell-Mann, M. Symmetries of baryons and mesons. Phys. Rev. 125, 1067-1084 (1962).  
32. Gottesman, D. Theory of fault-tolerant quantum computation. Phys. Rev. A 57, 127-137 (1998).  
33. Clark, S. Valence bond solid formalism for  $d$ -level one-way quantum computation. J. Phys. A 39, 2701-2721 (2006).  
34. Howard, M. & Vala, J. Qudit versions of the qubit  $\pi /8$  gate. Phys. Rev. A 86, 022316 (2012).  
35. Magesan, E., Gambetta, J. M. & Emerson, J. Characterizing quantum gates via randomized benchmarking. Phys. Rev. A 85, 042311 (2012).  
36. Fowler, A. G., Mariantoni, M., Martinis, J. M. & Cleland, A. N. Surface codes: towards practical large-scale quantum computation. Phys. Rev. A 86, 032324 (2012).  
37. Low, P. J., White, B. M., Cox, A. A., Day, M. L. & Senko, C. Practical trapped-ion protocols for universal qudit-based quantum computing. Phys. Rev. Res. 2, 033128 (2020).  
38. Pogorelov, I. et al. Compact ion-trap quantum computing demonstrator. PRX Quantum 2, 020343 (2021).  
39. Parrado-Rodriguez, P., Ryan-Anderson, C., Bermudez, A. & Muller, M. Crosstalk suppression for fault-tolerant quantum error correction with trapped ions. Quantum 5, 487 (2021).  
40. Kim, S.: Acousto-Optic Devices for Optical Signal Processing and Quantum Computing. Dissertation, University of Colorado (2008).  
41. Debnath, S. et al. Demonstration of a small programmable quantum computer with atomic qubits. Nature 536, 63-66 (2016).  
42. Häffner, H. et al. Precision measurement and compensation of optical Stark shifts for an ion-trap quantum processor. Phys. Rev. Lett. 90, 143602 (2003).  
43. O'Leary, D. P., Brennen, G. K. & Bullock, S. S. Parallelism for quantum computation with quuds. Phys. Rev. A 74, 032334 (2006).  
44. Ringbauer, M. et al. Characterizing quantum dynamics with initial system-environment correlations. Phys. Rev. Lett. 114, 090402 (2015).  
45. Ferrie, C. & Blume-Kohout, R. Estimating the bias of a noisy coin. AIP Conf. Proc. 1443, 14-21 (2012).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2022

# Data availability

Source data are provided with this paper. The data underlying this work are available via Zenodo at https://doi.org/10.5281/zenodo.6527605.

# Code availability

All the codes used for data analysis are available from the corresponding author upon reasonable request.

# Acknowledgements

We thank M. Huber and J. Wallman for discussions. This project has received funding from the European Union's Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie grant agreement no. 840450. It reflects only the author's view; the EU Agency is not responsible for any use that may be made of the information it contains. We also acknowledge support by the Austrian Science Fund (FWF), through the SFB BeyondC (FWF project no. F7109); by the Institut für Quanteninformation GmbH; by the US Army Research Office (ARO) through grant no. W911NF-21-1-0007; by the US Air Force Office of Scientific Research (AFOSR) via IOE grant no. FA9550-19-1-7044 LASCEM; and by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA), via the US ARO grant no. W911NF-16-1-0070. This project has received funding from the European Union's

Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement no. 801110 and the Austrian Federal Ministry of Education, Science and Research (BMBWF).

# Author contributions

M.R. developed the concepts. M.R., M.M., L.P., R.S., P.S. and T.M. performed the experiments. M.R. analyzed the data. T.M. and R.B. supervised the project. All the authors contributed to writing the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41567-022-01658-0.

Correspondence and requests for materials should be addressed to Martin Ringbauer.

Peer review information Nature Physics thanks Winfried Hensinger and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.