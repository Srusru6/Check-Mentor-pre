# Demonstration of a small programmable quantum computer with atomic qubits

S. Debnath<sup>1</sup>, N. M. Linke<sup>1</sup>, C. Figgatt<sup>1</sup>, K. A. Landsman<sup>1</sup>, K. Wright<sup>1</sup> & C. Monroe<sup>1,2,3</sup>

Quantum computers can solve certain problems more efficiently than any possible conventional computer. Small quantum algorithms have been demonstrated on multiple quantum computing platforms, many specifically tailored in hardware to implement a particular algorithm or execute a limited number of computational paths $^{1-10}$ . Here we demonstrate a five-qubit trapped-ion quantum computer that can be programmed in software to implement arbitrary quantum algorithms by executing any sequence of universal quantum logic gates. We compile algorithms into a fully connected set of gate operations that are native to the hardware and have a mean fidelity of 98 per cent. Reconfiguring these gate sequences provides the flexibility to implement a variety of algorithms without altering the hardware. As examples, we implement the Deutsch-Jozsa $^{11}$  and Bernstein-Vazirani $^{12}$  algorithms with average success rates of 95 and 90 per cent, respectively. We also perform a coherent quantum Fourier transform $^{13,14}$  on five trapped-ion qubits for phase estimation and period finding with average fidelities of 62 and 84 per cent, respectively. This small quantum computer can be scaled to larger numbers of qubits within a single register, and can be further expanded by connecting several such modules through ion shuttling $^{15}$  or photonic quantum channels $^{16}$ .

Implementing a scalable programmable quantum computing architecture requires high-fidelity initialization and detection at the individual qubit level and pristine control of interactions between qubits. Whereas most physical platforms have nearest-neighbour interactions only, a multi-qubit trapped-ion system features an intrinsic long-range interaction that is optically gated and connects any pair of qubits $^{17,18}$ . Unlike solid-state implementations $^{19,20}$ , the quantum circuitry is determined by external fields, and hence can be programmed and reconfigured without altering the structure of the qubits themselves. By optically resolving individual ions, we implement single-qubit rotations and arbitrary two-qubit gates by directly addressing pairs of ions without additional overhead such as moving information through local couplings $^{19,21}$  or hiding qubit populations in additional auxiliary states $^{10}$ . Such native gates can then be used to construct modular logic gates that can be called in reconfigurable algorithm sequences. We observe a mean fidelity of  $98\%$  in these native operations without the use of spin echo or dynamical decoupling techniques $^{10,22,23}$ . This bottom-up approach can be adapted for large-scale computation using micro-fabricated ion traps with integrated optics $^{24}$  and high optical access, and we expect that gate fidelities could exceed  $99.9\%$  with straightforward improvements to the classical control $^{23,25}$ .

The programmable and reconfigurable nature of the trapped-ion quantum computer is illustrated by a hierarchy of operations from software to hardware, shown in Fig. 1a. At the top is a high-level user interface that specifies the desired algorithm, represented by a standard family of modular universal logic gates such as Hadamard (H), controlled-NOT (CNOT), and controlled-phase (CP) gates $^{14}$ . Next, a quantum compiler translates the universal gates into gates native to the hardware, which in our case are two-qubit Ising (XX) gates $^{18}$  and

single-qubit rotation (R) gates<sup>14</sup>. Finally, these native gates are decomposed into laser pulses that are pre-calculated to effect the desired qubit operation through the Coulomb-coupled motion while disentangling the motion at the end of the gates<sup>26</sup>.

At the hardware level, the processor consists of trapped  $^{171}\mathrm{Yb}^+$  atomic ion qubits with information stored in the hyperfine 'clock' states  $|0\rangle \equiv |F = 0;m_F = 0\rangle$  and  $|1\rangle \equiv |F = 1;m_F = 0\rangle$  of the  $^2\mathrm{S}_{1 / 2}$  electronic ground level with a qubit frequency splitting of  $\nu_{0} = 12.642821\mathrm{GHz}$  (ref. 27). Here,  $F$  and  $m_{F}$  denote the quantum numbers associated with the total atomic angular momentum and its projection along the quantization axis defined by an applied magnetic field of  $5.2\mathrm{G}$ . We measure a qubit coherence time in excess of  $0.5\mathrm{s}$ , and with magnetic shielding we expect this to improve dramatically (ref. 28).

We confine the ions in a linear radio-frequency Paul trap, with radial and axial trap frequencies  $\nu_{x} = 3.07\mathrm{MHz}$  and  $\nu_{z} = 0.27\mathrm{MHz}$ , respectively. The ions are laser-cooled to near their radial motional ground state and form a linear crystal with a spacing of approximately  $5\mu \mathrm{m}$  for  $n = 5$  ions. A computation is performed by first initializing all qubits to state  $|0\rangle$  through optical pumping[27]. This is followed by quantum gates, implemented by a series of coherent rotations using stimulated Raman transitions driven by a  $355\mathrm{nm}$  mode-locked laser, where the beat-note between two counterpropagating Raman beams drives qubit and motional transitions[29]. To achieve individual addressing, we split one of the Raman beams into a static array of beams, each of which is directed through an individual channel of a multi-channel acoustooptic modulator (AOM) and focused onto its respective ion, as shown in Fig. 1b. Finally, the qubit register is measured with high fidelity (see Methods) by driving the  ${}^{2}\mathrm{S}_{1/2} \rightarrow {}^{2}\mathrm{P}_{1/2}$  cycling transition near  $369\mathrm{nm}$  and simultaneously collecting the resulting state-dependent fluorescence from each ion using high-resolution optics and a multi-channel photo-multiplier tube (PMT).

The lowest level of qubit control consists of native single- and two-qubit operations. We perform single-qubit rotations  $R_{\phi}(\theta)$  by tuning the Raman beat-note to qubit resonance  $\nu_{0}$ . Here, the rotation angle  $\theta$  and axis  $\phi$  are determined by the duration and phase offset of the beat-note, which is programmed through radio-frequency signals on appropriate AOM channels. Two-qubit XX-gates are performed by invoking an effective spin-spin Ising interaction between qubits mediated by the collective modes of motion of the chain[18]. Here, we apply Raman beat-notes tuned close to  $\nu_{0} \pm \nu_{x}$  that coherently couple the spins to all X-modes of motion. A pulse shaping technique[26] disentangles the motion at the end of the gate, resulting in a two-qubit entangling rotation of any amount  $XX(\chi_{i,j})$ . Here, the geometric phase  $\chi_{i,j}$  originates from the integrated Ising interaction[18,26], the sign  $\alpha_{i,j} = \pm 1$  of which arises from the Coulomb interaction between qubits  $i$  and  $j$  (Fig. 1b inset). We pre-calculate and optimize XX-gate pulse shapes off-line for all  $\{i,j\}$  to achieve high fidelity while keeping the gates relatively fast (see Methods).

We use these native R- and XX-gates to construct standard logic gates, which can be called by a quantum algorithm. For instance, we

![](images/1c2da13bbb80d70e0576819badec6ee1ec0861794c800298df16cd7d3d7b9ac5.jpg)

![](images/deb924d164969b8e766055cd6de71ac4e813e36f1e58302a3ae697f3c362beb1.jpg)  
Figure 1 | Computation architecture. a, Hierarchy of operations from software to hardware. See main text for details. b, Hardware setup. A linear chain of trapped ion qubits along the  $Z$  axis is shown at the centre of the panel ('Ion chain'). An imaging objective ('Detection optics') collects ion fluorescence along the  $Y$  axis and maps each ion onto a multichannel photo-multiplier tube (PMT) for measurement of individual qubits. Counterpropagating Raman beams ('Global' and 'Individual') along the  $X$  axis perform qubit operations. A diffractive beam splitter creates an array of static Raman beams that are individually switched using a multi-channel acousto-optic modulator (AOM) driven by radio frequency ('Control radio-frequency signals') to perform qubit-selective gates. By modulating appropriate addressing beams, any single-qubit rotation or two-qubit Ising (XX) gate can be realized. For the two-qubit gates between qubits  $i$  and  $j$ , we can continuously tune the nonlinear gate angle  $\chi_{ij}$ . This represents a system of qubits with fully connected and reconfigurable spin-spin Ising interactions (inset).

implement the single-qubit Hadamard gate as  $H = R_{x}(-\pi)R_{y}(\pi /2)$  and the Z-rotation as  $R_z(\theta) = R_y(-\pi /2)R_x(\theta)R_y(\pi /2)$ . Two-qubit logic gates such as CP and CNOT are compiled to account for the signs of the CP rotation angle  $\beta$  and the Ising interaction  $\alpha_{i,j}$ , making them independent of  $\{i,j\}$  and therefore modular (Fig. 2). At the highest level we program arbitrary sequences of such logic gates as required to implement any quantum algorithm.

We first implement the Deutsch-Jozsa algorithm $^{11}$ , which determines whether a given function (the 'oracle') is constant or balanced. A function that has an  $n$ -bit input and a 1-bit output ( $f: \{0, 1, 2, \dots, 2^n - 1\} \to \{0, 1\}$ ) is balanced when exactly half of the inputs result in the output 0 and the other half in the output 1, while a constant function assumes a single value irrespective of the input. In our setup we program 7 out of the 70 possible oracles of three-qubit balanced functions by using seven different sequences of CNOT gates between each of the three qubits in the control register  $x = \{X_1X_2X_3\}$  and the function register  $X_4$  (Fig. 3a). We program the two constant functions by setting  $X_4$  to either 0 or 1. Executing the algorithm starts with preparing the control register in the superposition state  $|x\rangle = \frac{1}{\sqrt{8}}\sum_{k=0}^{7}|k\rangle$ , followed

![](images/6bddb96ce02755426d2dafb7942b45d2e0ff2a12fc424fa5d3ffd56126177973.jpg)

![](images/f854e07418dbfbdbc04b09561347b71805fb6af5256068fff917aaa7b6ecde25.jpg)  
Figure 2 | Two-qubit modular gates. a, Decomposition of the controlled-NOT (CNOT) gate. The geometric phase  $\chi_{ij}$  of the XX-gate is  $\pm \pi /4$ , and we define  $\alpha_{ij} = \mathrm{sgn}(\chi_{ij})$ . b, Decomposition of the controlled-phase (CP) gate where  $\beta = \mathrm{sgn}(\theta)$  for the controlled phase  $\theta$ . The geometric phase of the XX-gate is adjusted such that  $\chi_{ij} = \alpha_{ij}|\theta | / 4$ . See main text for details.

by the function evaluation oracle. A CNOT is then performed between the function register  $X_{4}$  and the ancilla qubit  $X_{5}$  (initially set to  $\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$ ). All qubits are then rotated and measured (except for the ancilla) as shown in Fig. 3a. Finally, a measurement of  $x$  (conditioned upon  $X_{4} = 1$ , occurring with  $50\%$  probability) determines if the function is constant or balanced. Measurement of the output  $x = \{111\}$  indicates a constant function, while any other value indicates a balanced function (see Methods). The average success probability is 0.967(2) for constant and 0.932(3) for balanced functions (Fig. 3b), where the number in parentheses is the statistical uncertainty (1 s.d.).

The Bernstein-Vazirani algorithm is a variant of the Deutsch-Jozsa algorithm where the oracle function is an inner product of two  $n$ -bit strings:  $f_{c}(\pmb{x}) = \pmb{c} \cdot \pmb{x}$ . Here, the aim is to determine the vector  $c = \{c_1c_2\dots c_n\}$  in a single trial[12]. We program all 16 instances of the four-bit oracle that evaluate the function  $f_{c}(\pmb{x}) \oplus X_{5}$ . This is achieved by applying a particular pattern of CNOT gates, determined by  $c$ , between  $\pmb{x} = \{X_{1}X_{2}X_{3}X_{4}\}$  and  $X_{5} = \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$  (Fig. 3c). For example, if  $c = \{0101\}$  then CNOT gates are applied between  $X_{2}, X_{5}$  and  $X_{4}, X_{5}$ . We start with a superposition state  $|x\rangle = \frac{1}{\sqrt{16}}\sum_{k=0}^{15}|k\rangle$ , followed by the oracle. Finally, applying a global  $R_{y}(\pi/2)$  rotation produces the output state  $\overline{\pmb{c}}$ , which is the inverse of  $c$ . In the experiment, a single-shot measurement of the correct outcome  $\overline{\pmb{c}}$  is obtained with a probability of 0.903(2) (Fig. 3d), averaged over all possible oracle states.

Exponential speed-up of many quantum algorithms arises from the fact that parallel function evaluation is performed on a superposition of all classical input states of an  $n$ -bit string. These evaluation paths are then interfered using a quantum Fourier transform (QFT) to produce the desired solution<sup>14</sup>. One such example is the order-finding protocol in Shor's quantum factorization algorithm<sup>13</sup>. Another application is solving the eigenvalue problem  $A|\phi\rangle = e^{i\phi}|\phi\rangle$ , where the phase  $\phi$  can be estimated to  $n$ -bit precision using an  $n$ -bit QFT<sup>14</sup>. These algorithms have been implemented in experiments using a semi-classical version of the QFT that consists of single-qubit rotations based on classical feed-forward and qubit recycling which reduces the required register size<sup>5,10,30</sup>. The coherent QFT, on the other hand, is reversible and can be concatenated within an algorithm sequence.

Here, we construct a coherent QFT on five qubits using all 10 modular CP gates and involving a total of 80 single- and two-qubit native gates. This circuit fully exploits the high connectivity of a trapped ion system and illustrates how it can be scaled to larger modules (Fig. 4a). We apply the QFT in a period-finding protocol where we first prepare an input superposition state  $\sum_{k=0}^{31} C_k |k\rangle$  such that the coefficients  $\{C_k\}$  exhibit a periodic amplitude or phase modulation (see Methods), which is followed by the QFT operation. The modulation periodicity then appears in the output state populations (Fig. 4b).

We further examine the performance of the QFT in a phase estimation protocol where the eigenvalue  $\phi$  is estimated to 5-bit precision. In this case the input state is prepared in the form  $\frac{1}{\sqrt{32}}\otimes_{j = 1}^{5}(|0\rangle +\mathrm{e}^{-i2^{j - 1}\phi}|1\rangle)$ , which exhibits a  $\phi$ -dependent phase modulation

![](images/e8775f2cf5f6ea96075c4a663b7b464c304f26a0b9deccda44f15af364464029.jpg)

![](images/015d14584b7548a9a4102eef774ffec0562ae422cf4c357ae51a6c38debb84f9.jpg)

![](images/55107d049b111c1980c707aa26bf3fc9f122ee6690191f0f2ee24dbfc9f773b7.jpg)  
Figure 3 | Quantum algorithms. a, The Deutsch-Jozsa algorithm circuit on 5 ions. The oracle is implemented through gates shown in the shaded regions of the circuit. For balanced function oracles we apply each of the seven possible CNOT combinations, indicated in light grey. For the constant functions, we prepare  $X_4 = 0$  or 1 as indicated in dark grey. b, Measured populations of the output state for various functions, conditioned upon measuring  $X_4 = 1$ . The two constant functions  $f = 0$  and  $f = 1$  are indicated in dark grey, and the seven balanced functions given by particular CNOT gate combinations are indicated in light grey. Measurement of the output  $\{X_1X_2X_3\} = \{111\} = 7$  indicates a constant

![](images/31e08ba826eec30bde337f93c47691a7bdecd092a4e7c9b432ada5338f9fec04.jpg)  
function, while any other value (0-6) indicates a balanced function. c, The Bernstein-Vazirani algorithm circuit. The shaded region contains programmed CNOT gate combinations used to implement different oracle states  $\mathbf{c}$ ,  $\mathbf{d}$ , Measured output population for various oracle states. The output is the inverted oracle state  $\bar{\mathbf{c}}$ . Data represented in  $\mathbf{b}$ ,  $\mathbf{d}$  are obtained by sampling over 20,000 experimental repetitions for each function or the oracle state  $\mathbf{c}$  and the errors for the success probabilities in each case are statistical uncertainties within 1 s.d. The displayed probabilities are colour coded (key at right).

![](images/355c9efa57d14bb205036105f55112913644bec898397ccca4cb3f3daaa5b6be.jpg)

![](images/5f597e6cdc9c7a3a4864bb99af8cfe5542f541d873b1b05e682811def25c9756.jpg)

![](images/32480cde1ec196f3a7a9437b6936141591e0666aee36a95457eba2604699932c.jpg)  
Figure 4 | Quantum Fourier transform protocol. a, Experimental sequence for implementation and verification of the quantum Fourier transform (QFT). 'State preparation' consists of single qubit rotations that create a phase and amplitude modulation of the coefficients  $\{C_k\}$  of the input state  $\sum_{k=0}^{31} C_k |k\rangle$ . The shaded grey region contains a sequence of modular gates for implementing the QFT, which is then followed by a measurement of the register. b, Quantum period finding. Input states are prepared using single-qubit rotations to modulate the 32 state amplitudes with periods 1, 3, 4, 8, 16, and 32 (see Methods). The squared statistical

![](images/04355de84b7cd947248d1dc4b6351cd6d0cfd93f7615057d6020e08ca71c66c4.jpg)

![](images/696fc7ed000b78c092d650fdc471eae066ed5e491974845edea31bb842b239f8.jpg)  
overlap (SSO) $^5$  signifies the fidelity of the protocol where the error is a statistical estimate over 8,000 experimental repetitions. The grey and red bars represent populations calculated from theory and measured in the experiment, respectively. c, Quantum phase estimation using five measurement qubits. The plot shows populations in the output state that estimates the given phase modulation  $\phi$  of the input state amplitudes  $\{C_k\}$ . Probabilities in the output state population are colour coded. We observe the correct value of the phase in each case with a probability  $>0.6$ . The experiment is repeated 8,000 times for each value of  $\phi$ .

$C_k = \frac{1}{\sqrt{32}} e^{-ik\phi}$ . We apply the QFT on this state to estimate  $\phi$  by mapping its value onto populations of the output state, as shown in Fig. 4c. This is repeated for several cases where  $\phi$  is incremented in steps of  $2\pi/64$  over the range 0 to  $2\pi$ . Values of  $\phi$  that are integer multiples of  $2\pi/32$  result in the output state  $|32\phi/2\pi\rangle$ . This is achieved with an average fidelity of 0.619(5). For non-integer values, the population is distributed between the nearest 5-bit approximate states<sup>14</sup>.

In our experiments, each algorithm fidelity is limited mainly by the native gate errors  $(< 2\%)$ , which propagate into the standard logic gate errors  $(< 5\%)$  (see Methods). These errors are dominated by Raman beam imperfections and therefore can be reduced by mitigating Raman beam intensity noise[23] and individual addressing crosstalk (see Methods). Systematic shifts in the axes of the gate rotations accumulate due to unequal Stark shifts across the qubits, which result in algorithmic errors that depend upon the circuit structure. This type of error can be easily eliminated by feeding forward known shifts to the radio frequency of individual qubit control beams.

The algorithms presented here illustrate the computational flexibility provided by the trapped-ion quantum architecture. Within a single module, this system can be scaled to dozens of qubits by linearly increasing the number of radio-frequency controls and AOM- and PMT-channels at the hardware level. In software, the number of XX- and R-gate calibrations required to compile any logic gate scale as  $\mathcal{O}(n^2)$ . As more ions are added to the chain, the axial confinement must be weakened to maintain a linear crystal. This will slow down the XX-gate duration roughly as  $n^{1.7}$ , but the crosstalk is not expected to get worse (see Methods). Finally, implementing this architecture on multi-zone ion traps such as surface traps will provide further control over the connectivity of qubits though shuttling $^{15}$  for scalable computation. This will also enable selective measurement of qubits that can be fed-forward classically to perform conditional operations in the module $^{5}$  as required for fault-tolerant computing.

Online Content Methods, along with any additional Extended Data display items and Source Data, are available in the online version of the paper; references unique to these sections appear only in the online paper.

# Received 21 March; accepted 1 June 2016.

1. Linden, N., Barjat, H. & Freeman, R. An implementation of the Deutsch-Jozsa algorithm on a three-qubit NMR quantum computer. Chem. Phys. Lett. 296, 61-67 (1998).  
2. Vandersypen, L. M. K. et al. Experimental realization of Shor's quantum factoring algorithm using nuclear magnetic resonance. Nature 414, 883-887 (2001).  
3. Gulde, S. et al. Implementation of the Deutsch-Jozsa algorithm on an ion-trap quantum computer. Nature 421, 48-50 (2003).  
4. Brainis, E. et al. Fiber-optics implementation of the Deutsch-Jozsa and Bernstein-Vazirani quantum algorithms with three qubits. Phys. Rev. Lett. 90, 157902 (2003).  
5. Chiaverini, J. et al. Implementation of the semiclassical quantum Fourier transform in a scalable system. Science 308, 997-1000 (2005).  
6. Brickman, K.-A. et al. Implementation of Grover's quantum search algorithm in a scalable system. Phys. Rev. A 72, 050306(R) (2005).  
7. DiCarlo, L. et al. Demonstration of two-qubit algorithms with a superconducting quantum processor. Nature 460, 240-244 (2009).  
8. Shi, F. et al. Room-temperature implementation of the Deutsch-Jozsa algorithm with a single electronic spin in diamond. Phys. Rev. Lett. 105, 040504 (2010).

9. Martin-López, E. et al. Experimental realization of Shor's quantum factoring algorithm using qubit recycling. Nat. Photon. 6, 773-776 (2012).  
10. Monz, T. et al. Realization of a scalable Shor algorithm. Science 351, 1068-1070 (2016).  
11. Deutsch, D. & Jozsa, R. Rapid solution of problems by quantum computation. Proc. R. Soc. Lond. A 439, 553-558 (1992).  
12. Bernstein, E. & Vazirani, U. Quantum complexity theory. SIAM J. Comput. 26, 1411-1473 (1997).  
13. Shor, P. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM J. Comput. 26, 1484-1509 (1997).  
14. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information 1st edn (Cambridge Univ. Press, 2002).  
15. Kielpinski, D., Monroe, C. & Wineland, D. J. Architecture for a large-scale ion-trap quantum computer. Nature 417, 709-711 (2002).  
16. Monroe, C. et al. Large scale modular quantum computer architecture with atomic memory and photonic interconnects. Phys. Rev. A 89, 022317 (2014).  
17. Cirac, J.I. & Zoller, P. Quantum computations with cold trapped ions. Phys. Rev. Lett. 74, 4091-4094 (1995).  
18. Mølmer, K. & Sørensen, A. Multipartite entanglement of hot trapped ions. Phys. Rev. Lett. 82, 1835-1838 (1999).  
19. Barends, R. et al. Superconducting quantum circuits at the surface code threshold for fault tolerance. Nature 508, 500-503 (2014).  
20. Hill, C. D. et al. A surface code quantum computer in silicon. Sci. Adv. 1, e1500707 (2015).  
21. Gottesman, D. Fault-tolerant quantum computation with local gates. J. Mod. Opt. 47, 333-345 (2000).  
22. Green, T. J. & Biercuk, M. J. Phase-modulated decoupling and error suppression in qubit-oscillator systems. Phys. Rev. Lett. 114, 120502 (2015).  
23. Ballance, C. J. et al. Laser-driven quantum logic gates with precision beyond the fault-tolerant threshold. Preprint at http://arxiv.org/abs/1512.04600 (2016).  
24. True Merrill, J. et al. Demonstration of integrated microscale optics in surface-electrode ion traps. New J. Phys. 13, 103005 (2011).  
25. Gaebler, J. P. et al. High-fidelity universal gate set for  $^9\mathrm{Be}^+$  ion qubits. Preprint at http://arxiv.org/abs/1604.00032 (2016).  
26. Choi, T. et al. Optimal quantum control of multimode couplings between trapped ion qubits for scalable entanglement. Phys. Rev. Lett. 112, 190502 (2014).  
27. Olmschenk, S. et al. Manipulation and detection of a trapped  $\mathrm{Yb^{+}}$  hyperfine qubit. Phys. Rev. A 76, 052314 (2007).  
28. Fisk, P. T. H., Sellars, M. J., Lawn, M. A. & Coles, C. Accurate measurement of the 12.6GHz "clock" transition in trapped  $^{171}\mathrm{Yb}^+$  ions. IEEE Trans. Ultrasonics Ferroelectrics Frequency 44, 344-354 (1997).  
29. Hayes, D. et al. Entanglement of atomic qubits using an optical frequency comb. Phys. Rev. Lett. 104, 140501 (2010).  
30. Higgins, B. L., Berry, D. W., Bartlett, S. D., Wiseman, H. M. & Pryde, G. J. Entanglement-free Heisenberg-limited phase estimation. Nature 450, 393-396 (2007).

Acknowledgements We thank K. R. Brown, J. Kim, T. Choi, Z.-X. Gong, T. A. Manning, D. Maslov and C. Volin for discussions. This work was supported by the US Army Research Office with funds from the IARPA MQCO and LogiQ Programs, the Air Force Office of Scientific Research MURI on Quantum Measurement and Verification, and the National Science Foundation Physics Frontier Center at JQI.

Author Contributions S.D., N.M.L, C.F., K.A.L., K.W. and C.M. all contributed to the experimental design, construction, data collection and analysis of this experiment. All authors contributed to this manuscript.

Author Information Reprints and permissions information is available at www.nature.com/reprints. The authors declare competing financial interests: details are available in the online version of the paper. Readers are welcome to comment on the online version of the paper. Correspondence and requests for materials should be addressed to S.D. (sdebnath@umd.edu).

Reviewer Information Nature thanks S. Bartlett and T. Northup for their contribution to the peer review of this work.

# METHODS

Experimental techniques. We use a linear radio-frequency Paul trap made of four segmented blade electrodes driven at  $23.83\mathrm{MHz}$  where the transverse secular frequency of the trap is actively stabilized[31]. For measurement, state-dependent fluorescence is collected by a 0.38 numerical aperture objective that images ions with  $0.55\mu \mathrm{m}$  resolution. For a single qubit, single-shot detection fidelities for states  $|0\rangle$  and  $|1\rangle$  are  $99.74(3)\%$  and  $99.09(5)\%$ , respectively. For  $n = 5$  qubits, detection is degraded by signal crosstalk between PMT channels, and the average single-shot fidelity is  $95.3(2)\%$  for the  $2^{n}$  states. For the population distributions measured in Figs 3 and 4 and the reported algorithm fidelities, multi-qubit detection is performed by signal-averaging the populations of all  $2^{n}$  states over a few thousand experimental repetitions. In this way, detection and crosstalk errors are removed by decomposing the measurements into the known detector array response of all 32 possible qubit states. The individual addressing Raman beams are modulated using a multi-channel AOM (Model H-601 Series 32-Channel UV Acousto-Optic Modulator, PN: 66948-226460-G01, Harris Corporation) and focused down to a beam waist of approximately  $1.5\mu \mathrm{m}$  at the ions. Addressing crosstalk between neighbouring ions due to Raman beam spillover is  $< 4\%$ , which can be improved using higher resolution optics[32].

As more ions are added to a chain, the ratio of axial-to-transverse confinement must be weakened to maintain a linear crystal  $(\nu_{z} / \nu_{x} < 0.6n^{-0.86})^{33}$ . For constant transverse confinement, this means that the minimum ion spacing remains the same. However, this will slow the gates down. In our setup (for  $n = 5$ ) two-qubit XX-gates for any ion pair  $\{i,j\}$  have a duration of  $\tau_{\mathrm{g}} = 235\mu \mathrm{s}$ , which depends on the spectral splitting of the transverse modes  $(\tau_{\mathrm{g}}\sim \nu_{x} / \nu_{z}^{2}\sim n^{1.7})$ . The XX-gate pulse shape is a 9-segment piecewise-constant Rabi frequency modulation  $\{\varOmega_k\}_{ij}$  (where  $1\leq k\leq 9$ ), which is implemented by modulating the global Raman beam. Optimized pulse shapes are calculated for each ion pair such that  $\{\varOmega_k\}_{ij}$  is within practical limits and the gate fidelity is maximized. The number of classical calculations to find the pulse shapes scales as  $\mathcal{O}(n^2)$ . The XX-gates are calibrated by setting the product of the laser intensities on the two qubits such that  $\chi_{i,j} = \pi /4$  (refs 26, 34-36). For CP gates that require other values of  $\chi_{ij}$ , we scale the laser intensity accordingly. Single-qubit rotations are calibrated by measuring the Rabi frequency  $\varOmega_{i}$  of individual qubits. Single-qubit native R-gates have a duration of approximately  $0.1\tau_{\mathrm{g}}$ .

Implementation of the Deutsch-Jozsa algorithm. The Deutsch-Jozsa algorithm is implemented by starting with an equal superposition of all classical input states to the function  $f(x)$ :  $\{0, 1, \dots, 7\} \rightarrow \{0, 1\}$ . We prepare this by initializing all qubits to  $|0\rangle$ , followed by  $R_{y}(\pi /2)$  rotations on the qubits in the control register  $x = X_{1}X_{2}X_{3}$ . Then we rotate the ancilla qubit  $X_{5}$  using  $R_{y}(-\pi /2)$ . The resulting 5-qubit state is

$$
| \psi \rangle_ {0} = \frac {1}{\sqrt {8}} \sum_ {x = 0} ^ {7} | x \rangle_ {1 2 3} \otimes | 0 \rangle_ {4} \otimes \frac {| 0 \rangle_ {5} - | 1 \rangle_ {5}}{\sqrt {2}}
$$

where  $x$  is the decimal representation of qubits  $X_{1}X_{2}X_{3}$ . Then we apply the function on the input superposition state such that the value is written to  $X_{4}$ . The resulting state is

$$
\left| \psi \right\rangle_ {1} = \frac {1}{\sqrt {8}} \sum_ {x = 0} ^ {7} \left| x \right\rangle_ {1 2 3} \left| f (x) \right\rangle_ {4} \otimes \frac {\left| 0 \right\rangle_ {5} - \left| 1 \right\rangle_ {5}}{\sqrt {2}}
$$

This is followed by a CNOT between the function register  $X_{4}$  and the ancilla  $X_{5}$  which provides a phase 'kick-back' to produce the state

$$
| \psi \rangle_ {2} = \frac {1}{\sqrt {8}} \sum_ {x = 0} ^ {7} (- 1) ^ {f (x)} | x \rangle_ {1 2 3} | f (x) \rangle_ {4} \otimes \frac {| 0 \rangle_ {5} - | 1 \rangle_ {5}}{\sqrt {2}}
$$

This is followed by a single-qubit rotation  $R_{y}(\pi /2)$  on all qubits. Then we measure the first four qubits to reach the solution and ignore the ancilla qubit since it is not entangled with the other qubits. The state of qubits  $X_{1}X_{2}X_{3}X_{4}$  before measurement can be written as

$$
\begin{array}{l} \left| \psi \right\rangle_ {3} = \frac {1}{8} \sum_ {y = 0} ^ {7} \sum_ {x = 0} ^ {7} (- 1) ^ {f (x)} (- 1) ^ {\bar {y} \cdot x} \left| \bar {y} \right\rangle_ {1 2 3} \otimes \frac {\left| 1 \right\rangle_ {4} + (- 1) ^ {f (x)} \left| 0 \right\rangle_ {4}}{\sqrt {2}} \tag {1} \\ = C _ {0 0 0 0} | 0 0 0 0 \rangle + C _ {0 0 0 1} | 0 0 0 1 \rangle + \dots \\ \dots + C _ {1 1 1 0} \left| 1 1 1 0 \right\rangle + C _ {1 1 1 1} \left| 1 1 1 1 \right\rangle \\ \end{array}
$$

where  $\overline{y}$  is the bit-wise inversion of  $y$ . If  $f(x) = a$  is a constant function (with  $a = \{0,1\}$ ), the coefficients of the basis states  $|1110\rangle$  and  $|1111\rangle$  are

$$
\begin{array}{l} C _ {1 1 1 0} = \frac {1}{8 \sqrt {2}} (- 1) ^ {a} \sum_ {x = 0} ^ {7} (- 1) ^ {0 0 0 \cdot x} = \frac {(- 1) ^ {a}}{\sqrt {2}} \\ C _ {1 1 1 1} = \frac {1}{8 \sqrt {2}} \sum_ {x = 0} ^ {7} (- 1) ^ {0 0 0 \cdot x} = \frac {1}{\sqrt {2}} \\ \end{array}
$$

If  $f(x)$  is a balanced function, then the coefficients are

$$
\begin{array}{l} C _ {1 1 1 0} = \frac {1}{8 \sqrt {2}} \sum_ {x = 0} ^ {7} (- 1) ^ {0 0 0 \cdot x} (- 1) ^ {f (x)} (- 1) ^ {f (x)} = \frac {1}{\sqrt {2}} \\ C _ {1 1 1 1} = \frac {1}{8 \sqrt {2}} \sum_ {x = 0} ^ {7} (- 1) ^ {0 0 0 \cdot x} (- 1) ^ {f (x)} = 0 \\ \end{array}
$$

Here we use the property that  $f(x) = 0$  for exactly half of the values of  $x$  and 1 for the rest. Conditioned upon  $X_{4} = 1$ , there is unit probability of measuring  $X_{1}, X_{2}, X_{3} = 111$  for a constant function and 0 probability of measuring the same outcome when the function is balanced. In equation (1), note that the probability of measuring  $X_{4} = 1$  is 0.5 irrespective of the number of qubits in the input (control) register of the function.

Native single- and two-qubit rotations. Native single-qubit operations  $R_{\phi}(\theta)$  are rotations of the Bloch vector by an angle  $\theta$  about an axis on the equator of the Bloch sphere, where  $\phi$  is the angle between this rotation axis and the  $X$  axis. The single-qubit operator is

$$
R _ {\phi} (\theta) = \left[ \begin{array}{c c} \cos \left(\frac {\theta}{2}\right) & - i \sin \left(\frac {\theta}{2}\right) \mathrm {e} ^ {- i \phi} \\ - i \sin \left(\frac {\theta}{2}\right) \mathrm {e} ^ {i \phi} & \cos \left(\frac {\theta}{2}\right) \end{array} \right]
$$

The standard X and Y rotations used in the composite gates are simply  $R_{x}(\theta) = R_{0}(\theta)$  and  $R_{y}(\theta) = R_{\pi /2}(\theta)$ .

Native two-qubit XX-gates are performed by invoking a  $\sigma_{x}\sigma_{x}$ -Ising interaction between qubits  $i$  and  $j$ , which is mediated through the coupling of the qubits to the collective transverse motional modes of the ion chain. The resulting two-qubit entangling rotation  $XX(\chi_{ij})$  depends on the geometric phase  $\chi_{ij}$ , which is the integrated Ising interaction and can be varied by changing the Raman beam intensity. The sign of the geometric phase  $\alpha_{ij} = \mathrm{sgn}(\chi_{ij})$  depends on how ions  $i$  and  $j$  couple to the common transverse motional modes. The XX-gate operator is

$$
X X (\chi_ {i j}) = \left[ \begin{array}{c c c c} \cos (\chi_ {i j}) & 0 & 0 & - i \sin (\chi_ {i j}) \\ 0 & \cos (\chi_ {i j}) & - i \sin (\chi_ {i j}) & 0 \\ 0 & - i \sin (\chi_ {i j}) & \cos (\chi_ {i j}) & 0 \\ - i \sin (\chi_ {i j}) & 0 & 0 & \cos (\chi_ {i j}) \end{array} \right]
$$

In this experiment,  $\alpha_{12}$ ,  $\alpha_{45}$ ,  $\alpha_{14}$ ,  $\alpha_{25}$ ,  $\alpha_{35}$ ,  $\alpha_{23}$ ,  $\alpha_{34} = +1$  and  $\alpha_{15}$ ,  $\alpha_{25}$ ,  $\alpha_{13} = -1$ . Composite gate fidelity. Controlled-NOT (CNOT) gates are performed between all ion pairs and characterized in the following way. We perform the CNOT gate on all four classical input states  $|00\rangle$ ,  $|01\rangle$ ,  $|10\rangle$ ,  $|11\rangle$  and measure the fidelity from the population of the desired output state. The average fidelity of a CNOT on each ion pair is shown in Extended Data Table 1.

Controlled-phase (CP) gates are performed between all ion pairs and characterized by using a sequence of gates. We first initialize the qubits in the state  $\frac{1}{\sqrt{2}} |1\rangle(|0\rangle + |1\rangle)$ , where the first qubit is the control qubit and the second qubit is the target qubit. This is followed by a conditional phase gate  $\mathrm{CP}(\theta)$  that creates the state  $\frac{1}{\sqrt{2}} |1\rangle(|0\rangle + \mathrm{e}^{i\theta} |1\rangle)$ . A final rotation  $R_x(\pi/2)$  on the target qubit projects the conditional phase  $\theta$  onto the population of the target qubit as  $P(|1\rangle) = (1 - \sin \theta)/2$ . This is shown in Extended Data Figure 1.

We measure the fidelity of the CP gates at conditional phases  $\theta = \pm \pi /2$ , which correspond to the maximum and minimum values of  $\theta$ , respectively, which are used in a coherent QFT or  $\mathrm{QFT}^{-1}$ . At these values of  $\theta$ , where the geometric phase  $\chi_{ij} = \pi /4$ , the XX-gates are most sensitive to laser intensity fluctuations, which leads to maximum errors. This is evident from the data shown in Extended Data Figure 1, where a maximum deviation of the target qubit from the ideal output state occurs at  $\pm \pi /2$ . Therefore, the fidelity measure at these values is a lower bound on the CP gate fidelity. The fidelity is obtained by measuring the populations in

the  $|10\rangle$  and  $|11\rangle$  states for  $\theta = +\pi /2$  and  $\theta = -\pi /2$ , respectively. Extended Data Table 2 shows the fidelities of all CP gates.  
QFT state preparation. For the period-finding experiment, an amplitude or phase modulation is created in the coefficients  $C_k$  of the input state  $\sum_{k=0}^{31} C_k |k\rangle$  using individual single-qubit rotations. Extended Data Table 3 shows the input states for various measured periodicities.  
Sample size. No statistical methods were used to predetermine sample size.  
31. Johnson, K. G. et al. Active stabilization of ion trap radiofrequency potentials. Rev. Sci. Instrum. 87, 053110 (2016).

32. Crain, S., Mount, E., Baek, S. & Kim, J. Individual addressing of trapped  $^{171}\mathrm{Yb}^+$  ion qubits using a microelectromechanical systems-based beam steering system. Appl. Phys. Lett. 105, 181115 (2014).  
33. Schiffer, J. P. Phase transitions in anisotropically confined ionic crystals. Phys. Rev. Lett. **70**, 818–821 (1993).  
34. Zhu, S.-L., Monroe, C. & Duan, L.-M. Trapped ion quantum computation with transverse phonon modes. Phys. Rev. Lett 97, 050505 (2006).  
35. Solano, E., de Matos Filho, R. L. & Zagury, N. Deterministic Bell states and measurement of the motional state of two trapped ions. Phys. Rev. A 59, R2539-R2543 (1999).  
36. Milburn, G. J., Schneider, S. & James, D. F. V. Ion trap quantum computing with warm ions. Fortschr. Phys. 48, 801-810 (2000).

![](images/38d836022760e37374c1d625d5d6b60093fcef27e3ce3791e457b38ebc053caa.jpg)

![](images/41827957a28fd03fa13e2323bde479938a1226aa9768d2db25e233500722c17b.jpg)

![](images/6aab285927a4ee128c62e0b4d65936714f3ad28be0b172fca8ff6702e7a929c4.jpg)

![](images/16100e10a687bf41dade4158a89c6bf53a3092d316ae1d3d681995e38ac75ffe.jpg)

![](images/98e58e93923b33c5f1906822c5db8547741cf5d59d73cea4998b97f0847f1fc2.jpg)  
Extended Data Figure 1 | Controlled-phase gate. Shown is the performance of the controlled-phase (CP) gate between control (red) and target (blue) qubit for different qubit-pairs. The control qubit is prepared in the state  $|1\rangle$  which remains unchanged during the gate. Solid blue lines

![](images/94cbdd74e2de6811a28d33524b48bf12b8cfabeafe39acc108884c09c79120f5.jpg)

![](images/ae6201ad600cdf406cbd6bda0fc2f09c74acebf73d499556b17c1e466b65072e.jpg)

![](images/6bb74f9082b9c6d596cfbf235e1d49a7c313c7f9a1f5edbe523409b835be2be9.jpg)

![](images/c95234762bc33fb0ebfb875121989bd8aa7759d7a0c5a7b12dcde465957eac0b.jpg)

![](images/902f0479063a977060280594589d80c9c4c95ae7637af1383bd6a9d74d0d266a.jpg)  
indicate the theoretical probability of measuring the target qubit in  $|1\rangle$  whereas the data points show experimental data. Error bars are statistical, indicating a  $95\%$  confidence interval for 2,000 experimental repetitions.

Extended Data Table 1 | Controlled-NOT gate fidelities  

<table><tr><td>Ion pair</td><td>Fidelity (%)</td><td>Ion pair</td><td>Fidelity (%)</td></tr><tr><td>1,2</td><td>96.4(6)</td><td>2,4</td><td>98.5(7)</td></tr><tr><td>1,3</td><td>97.6(7)</td><td>2,5</td><td>96.8(7)</td></tr><tr><td>1,4</td><td>95.9(7)</td><td>3,4</td><td>96.6(5)</td></tr><tr><td>1,5</td><td>97.9(5)</td><td>3,5</td><td>97.6(6)</td></tr><tr><td>2,3</td><td>95.6(6)</td><td>4,5</td><td>97.2(5)</td></tr></table>

Gate fidelity is obtained by performing CNOT gates on all possible pairs of ions ('ion pair') in a chain of five qubits.

Extended Data Table 2 | Controlled-phase gate fidelities  

<table><tr><td>Ion pair</td><td>θ = π/2, fidelity (%)</td><td>θ = -π/2, fidelity (%)</td></tr><tr><td>1,2</td><td>91.1(6)</td><td>96.1(4)</td></tr><tr><td>1,3</td><td>93.6(5)</td><td>93.3(6)</td></tr><tr><td>1,4</td><td>91.6(6)</td><td>93.3(6)</td></tr><tr><td>1,5</td><td>95.9(4)</td><td>95.3(3)</td></tr><tr><td>2,3</td><td>90.7(6)</td><td>93.2(5)</td></tr><tr><td>2,4</td><td>94.2(5)</td><td>90.8(6)</td></tr><tr><td>2,5</td><td>95.8(4)</td><td>91.7(6)</td></tr><tr><td>3,4</td><td>91.0(6)</td><td>94.7(5)</td></tr><tr><td>3,5</td><td>96.0(4)</td><td>96.0(4)</td></tr><tr><td>4,5</td><td>93.5(6)</td><td>95.8(4)</td></tr></table>

Gate fidelity is obtained by performing CP gates on all possible pairs of ions ('ion pair') in a chain of five qubits for conditional phases  $\theta = \pm \pi /2$

Extended Data Table 3 | Input states in QFT-period finding  

<table><tr><td>Input state</td><td>Period</td></tr><tr><td>1/√32(|0⟩+|1))(|0⟩+|1))(|0⟩+|1))(|0⟩+|1))</td><td>1</td></tr><tr><td>1/√32(|0⟩+|1))(|0⟩+|1))(|0⟩+|1))(|0⟩+e i6.2π/16|1))(|0⟩+i|1))</td><td>3</td></tr><tr><td>1/√8(|0⟩+|1))(|0⟩+|1))(|0⟩+|1))|11)</td><td>4</td></tr><tr><td>1/2(|0⟩+|1))(|0⟩+|1))|111)</td><td>8</td></tr><tr><td>1/√2(|0⟩+|1))|1111)</td><td>16</td></tr><tr><td>|11111)</td><td>32</td></tr></table>

See Methods for details.