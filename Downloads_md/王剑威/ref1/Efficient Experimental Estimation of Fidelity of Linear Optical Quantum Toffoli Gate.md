# Efficient Experimental Estimation of Fidelity of Linear Optical Quantum Toffoli Gate

M. Mičuda, M. Sedlák, I. Straka, M. Miková, M. Dušek, M. Ježek, and J. Fiurášek

Department of Optics, Palacky University, 17. listopadu 1192/12, CZ-771 46 Olomouc, Czech Republic (Received 5 June 2013; published 17 October 2013)

We propose an efficiently measurable lower bound on quantum process fidelity of  $N$ -qubit controlled- $Z$  gates. This bound is determined by average output state fidelities for  $N$  partially conjugate product bases. A distinct advantage of our approach is that only fidelities with product states need to be measured while keeping the total number of measurements much smaller than what is necessary for full quantum process tomography. As an application, we use this method to experimentally estimate quantum process fidelity  $F$  of a three-qubit linear optical quantum Toffoli gate and we find that  $F \geq 0.83$ . We also demonstrate the entangling capability of the gate by preparing Greenberger-Horne-Zeilinger-type three-qubit entangled states from input product states.

DOI: 10.1103/PhysRevLett.111.160407

PACS numbers: 03.65.Wj, 03.67.-a, 42.50.Ex

As the complexity of quantum information processing devices increases, there is a growing demand for reliable and efficient methods of their characterization. Traditionally, the experimentally implemented quantum operations are characterized by quantum process tomography which provides their full description [1,2]. However, a complete quantum tomography requires resources which grow exponentially with the number of qubits. In recent years, increasing attention has been therefore paid to methods such as compressed sensing [3,4] or Monte Carlo sampling [5-7], that allow us to reduce the overhead of quantum process characterization. This is possible if we make some a priori assumption about the structure of the reconstructed quantum object or if we do not seek a complete tomographic description and we are satisfied instead with determination of a particular parameter such as fidelity [8-10].

In 2005, it was shown by Hofmann that the quantum process fidelity can be estimated by measuring the average quantum state fidelities  $F_{1}$  and  $F_{2}$  for only two conjugate bases [11]. The quantum process fidelity  $F_{\chi}$  is then lower bounded according to

$$
F _ {\chi} \geq F _ {1} + F _ {2} - 1. \tag {1}
$$

This procedure has received a considerable amount of attention and it was utilized in several experiments to estimate the fidelity of a quantum CNOT gate [12-17]. In this case, it is sufficient to measure the CNOT truth table in the computational basis and in the dual basis obtained from the computational basis by single-qubit Hadamard transformations. In this dual basis, the gate also acts as a CNOT but the roles of control and target qubits are reversed. The great practical advantage of this characterization of a CNOT gate is that all the required input probe states as well as all the corresponding output states whose fidelity should be measured are product states. Therefore, the fidelities can be directly determined by single-qubit measurements. The fidelity bound (1) is applicable to arbitrary multiqubit

quantum gates. However, going beyond the two-qubit CNOT gate, it would typically require measurements of fidelities of output states that are entangled [18].

In this Letter, we propose a generalization of the Hofmann fidelity bound to multiqubit controlled-  $Z$  gates which preserves all the experimentally desired features present for the two-qubit CNOT gate. In particular, product multiqubit probe states are considered and only fidelities of product states have to be measured. Furthermore, the total required number of measurement settings is only  $N2^{N}$  while at least  $2^{3N}$  measurement settings are necessary for a full quantum process tomography of an  $N$ -qubit gate specified by  $2^{4N} - 2^{2N}$  parameters for deterministic gates or  $2^{4N}$  parameters for probabilistic gates. Here a measurement setting represents a specific combination of input state preparation and an output measurement. As an application, we employ this method to experimentally estimate quantum process fidelity of a three-qubit linear optical controlled-controlled-  $Z$  (CCZ) gate that is equivalent to the Toffoli gate up to single-qubit Hadamard transform on a target qubit. The Toffoli gate is a crucial part of many quantum information processing schemes [1] and it represents one of the most complex quantum circuits experimentally implemented to date [19,20]. A peculiar feature of linear optical quantum gates is that they are probabilistic [21]. In practice, it may happen due to various imperfections that the success probability of the gate depends on the input state and is not a constant. We shall show that the fidelity bounds hold even in such a case but the average state fidelities must be calculated as weighted averages, with the weights given by relative probabilities of success.

Let  $|0\rangle$  and  $|1\rangle$  denote the computational basis states of a qubit. The CCZ gate flips the sign if and only if all three qubits are in state  $|1\rangle$ ,

$$
U _ {\mathrm {C C Z}} = \mathbb {I} - 2 | 1 1 1 \rangle \langle 1 1 1 |, \tag {2}
$$

where  $\mathbb{I}$  denotes the identity operator. In the computational basis, we explicitly have  $U_{\mathrm{CCZ}}|abc\rangle = (-1)^{abc}|abc\rangle$

A Hadamard transform  $H$  on a target qubit converts the sign flip of the CCZ gate into the bit flip of the Toffoli gate. Recall that  $H|0\rangle = | + \rangle$  and  $H|1\rangle = |-\rangle$ , where  $|\pm \rangle = (1 / \sqrt{2})(|0\rangle \pm |1\rangle)$ .

According to the Choi-Jamiolkowski isomorphism [22,23], any quantum operation  $\mathcal{E}$  can be represented by a positive semidefinite operator  $\chi$  on a tensor product of input and output Hilbert spaces. Let  $|\Phi_3^+ \rangle = \sum_{a,b,c=0}^{1} |abc\rangle_{\mathrm{in}} |abc\rangle_{\mathrm{out}}$  denote a maximally entangled state on two copies of a three-qubit Hilbert space. The Choi matrix of operation  $\mathcal{E}$  can be determined by applying this operation to one part of the maximally entangled state,  $\chi = I_{\mathrm{in}} \otimes \mathcal{E}_{\mathrm{out}}(\Phi_3^+)$ , where  $\Phi_3^+ = |\Phi_3^+ \rangle \langle \Phi_3^+\|$  is a shorthand notation for a density matrix of a pure state. For any input density matrix  $\rho_{\mathrm{in}}$ , the corresponding output density matrix  $\rho_{\mathrm{out}} = \mathcal{E}(\rho_{\mathrm{in}})$  can be calculated as  $\rho_{\mathrm{out}} = \mathrm{Tr}_{\mathrm{in}}[\rho_{\mathrm{in}}^T \otimes \mathbb{I}_{\mathrm{out}}\chi]$ , where  $\mathrm{Tr}_{\mathrm{in}}$  denotes partial trace and  $T$  stands for transposition. We shall consider general probabilistic operations and  $\mathrm{Tr}[\rho_{\mathrm{out}}] = \mathrm{Tr}[\rho_{\mathrm{in}}^T \otimes \mathbb{I}_{\mathrm{out}}\chi]$  then represents the success probability for the input  $\rho_{\mathrm{in}}$ . In particular, the Choi matrix of a unitary CCZ gate reads

$$
\chi_ {\mathrm {C C Z}} = (\mathbb {I} \otimes U _ {\mathrm {C C Z}}) \Phi_ {3} ^ {+} (\mathbb {I} \otimes U _ {\mathrm {C C Z}} ^ {\dagger}). \qquad (3)
$$

The process fidelity of a quantum gate  $\chi$  with respect to the ideal CCZ gate can be defined as a normalized overlap of the Choi matrices,  $F_{\chi} = \mathrm{Tr}[\chi \chi_{\mathrm{CCZ}}] / (8\mathrm{Tr}[\chi])$ , where the factor  $8 = \mathrm{Tr}[\chi_{\mathrm{CCZ}}]$  accounts for the normalization of  $\chi_{\mathrm{CCZ}}$ .

Our goal is to lower bound the gate fidelity by suitably chosen average state fidelities. Motivated by the symmetry of the CCZ gate which is invariant with respect to the permutation of the qubits, we propose to characterize the CCZ gate by measuring the average output state fidelities for three complementary product bases where two of the qubits are prepared in the computational basis states  $|0\rangle$ ,  $|1\rangle$  while the third qubit is prepared in the Hadamard basis states  $|+\rangle$ ,  $|-\rangle$ . The probe product states  $|\psi_{j,k}\rangle$  are specified in Table I for all three bases  $k = 1, 2, 3$ . It can be easily checked that all the corresponding output states  $|\psi_{j,k}^{(\mathrm{out})}\rangle = U_{\mathrm{CCZ}}|\psi_{j,k}\rangle$  are also product states and the two bases  $\{|\psi_{j,k}\rangle\}_{j=1}^{8}$  and  $\{|\psi_{j,k}^{(\mathrm{out})}\rangle\}_{j=1}^{8}$  coincide. Let

TABLE I. List of the input three-qubit product states  $\left| {\psi }_{j,k}\right\rangle$  .  

<table><tr><td>j</td><td>k=1</td><td>k=2</td><td>k=3</td><td>k=3&#x27;</td></tr><tr><td>1</td><td>|+00)</td><td>|0+0)</td><td>|00+)</td><td>|++0)</td></tr><tr><td>2</td><td>|+01)</td><td>|0+1)</td><td>|00-)</td><td>|++1)</td></tr><tr><td>3</td><td>|+10)</td><td>|0-0)</td><td>|01+)</td><td>|+-0)</td></tr><tr><td>4</td><td>|+11)</td><td>|0-1)</td><td>|01-)</td><td>|+-1)</td></tr><tr><td>5</td><td>|-00)</td><td>|1+0)</td><td>|10+)</td><td>|--0)</td></tr><tr><td>6</td><td>|-01)</td><td>|1+1)</td><td>|10-)</td><td>|--1)</td></tr><tr><td>7</td><td>|-10)</td><td>|1-0)</td><td>|11+)</td><td>|--0)</td></tr><tr><td>8</td><td>|-11)</td><td>|1-1)</td><td>|11-)</td><td>|--1)</td></tr></table>

$\rho_{j,k} = \mathrm{Tr}_{\mathrm{in}}[\psi_{j,k}^T\otimes \mathbb{I}_{\mathrm{out}}\chi ]$  denote the (unnormized) output state for the input  $|\psi_{j,k}\rangle$  . The fidelity of this output state with the ideal output can be expressed as

$$
f _ {j, k} = \frac {\left\langle \psi_ {j , k} ^ {(\mathrm {o u t})} \right| \rho_ {j , k} \left| \psi_ {j , k} ^ {(\mathrm {o u t})} \right\rangle}{\operatorname {T r} [ \rho_ {j , k} ]} = \frac {1}{p _ {j , k}} \operatorname {T r} \left[ \psi_ {j, k} ^ {T} \otimes \psi_ {j, k} ^ {(\mathrm {o u t})} \chi \right]. \tag {4}
$$

Here  $p_{j,k} = \mathrm{Tr}[\psi_{j,k}^T\otimes \mathbb{I}_{\mathrm{out}}\chi ]$  denotes the probability of success for input  $|\psi_{j,k}\rangle$  and  $\psi_{j,k} = |\psi_{j,k}\rangle \langle \psi_{j,k}|$  denotes a density matrix of a pure state  $|\psi_{j,k}\rangle$ . We define the average state fidelity for  $k$ th basis as a weighted mean of  $f_{j,k}$  with weights equal to the success probabilities  $p_{j,k}$  [24],

$$
F _ {k} = \frac {\sum_ {j = 1} ^ {8} p _ {j , k} f _ {j , k}}{\sum_ {j = 1} ^ {8} p _ {j , k}}. \tag {5}
$$

Since  $\sum_{j=1}^{8} \psi_{j,k} = \mathbb{I}$  for all  $k$ , it holds that  $\sum_{j=1}^{8} p_{j,k} = \operatorname{Tr}[\chi]$  and we can express the mean fidelities in a compact matrix form  $F_k = \operatorname{Tr}[R_k \chi] / \operatorname{Tr}[\chi]$ , where

$$
R _ {k} = \sum_ {j = 1} ^ {8} \psi_ {j, k} ^ {T} \otimes U _ {\mathrm {C C Z}} \psi_ {j, k} U _ {\mathrm {C C Z}} ^ {\dagger}. \tag {6}
$$

The gate fidelity  $F_{\chi}$  can be lower bounded by the three above defined average state fidelities as follows:

$$
F _ {\chi} \geq F _ {1} + F _ {2} + F _ {3} - 2, \tag {7}
$$

which generalizes the Hofmann bound (1) and is valid for both deterministic and probabilistic quantum operations. In order to prove this bound, we rewrite it as

$$
F _ {\chi} - F _ {1} - F _ {2} - F _ {3} + 2 = \frac {\operatorname {T r} [ R \chi ]}{\operatorname {T r} [ \chi ]} \geq 0, \tag {8}
$$

where  $R = \frac{1}{8}\chi_{\mathrm{CCZ}} - R_1 - R_2 - R_3 + 2\mathbb{I}$ . It can be shown by explicit calculation that the matrix  $R$  is positive semi-definite, which immediately implies the inequality (8). Note that  $R \geq 0$  holds irrespective of the actual form of the unitary  $U_{\mathrm{CCZ}}$ . Thus the fidelity bound (7) is actually completely general and it holds for all three-qubit unitary operations. The output states  $|\psi_{j,k}^{\mathrm{(out)}}\rangle$  will be product states for all unitaries  $U$  that are diagonal in the computational basis [25]. However, for other gates the output states may be entangled. We stress that it is important to calculate  $F_{k}$  as weighted means (5) because if  $F_{k}$  would be calculated as ordinary means,  $F_{k} = \sum_{j=1}^{8} f_{j,k} / 8$ , then the bounds (1) and (7) could actually overestimate the gate fidelity for certain trace-decreasing operations. The fidelity bound (7) can be generalized to  $N$ -qubit gates and it can be shown that

$$
F _ {\chi} \geq \sum_ {k = 1} ^ {N} F _ {k} - N + 1, \tag {9}
$$

where  $F_{k}$  is the average fidelity for input product basis states where all qubits are prepared in the computational basis states except for the  $k$ th qubit which is prepared in the

![](images/9dad080e158e9f09fa1d04348e53ca268fdab445f9245d0ff7b7dc3f5d21eb59.jpg)  
FIG. 1 (color online). Experimental setup. BD—calcite beam displacer, PPBS—partially polarizing beam splitter, PBS—polarizing beam splitter, HWP—half-wave plate, QWP—quarter-wave plate, D—single-photon detector.

Hadamard basis states. A detailed analytical proof of the bound (9) can be found in the Supplemental Material [25]. The bound will be tight and equality will hold in Eq. (9) if  $\chi$  is either the desired unitary  $U$ , the unitary  $U$  preceded by a  $\pi$  phase flip on a single qubit, or any mixture or coherent superposition of these unitary operations [25].

The experimental setup is shown in Fig. 1. Orthogonally polarized time-correlated photon pairs with central wavelength of  $810~\mathrm{nm}$  are generated in the process of spontaneous parametric down-conversion in a  $2\mathrm{mm}$  thick BBO crystal pumped by a cw laser diode with  $75\mathrm{mW}$  pump power [26]. The first qubit is encoded into the spatial degree of freedom of the signal photon while the second and third qubits are encoded into the polarization of the signal and idler photons, respectively. The polarization states are prepared and analyzed using half- and quarterwave plates and polarizing beam splitters. The calcite beam displacer BD1 transforms the input polarization state of the signal photon into the state of spatial qubit and the beam displacer BD2 maps the spatial qubit back onto polarization. The pair of beam displacers forms an inherently stable Mach-Zehnder interferometer. The half-wave plates HWP1 and HWP2 which address only one path in the interferometer disentangle input polarization and spatial qubits of the signal photon and ensure correct signal collection by BD2.

The CCZ gate is implemented by two-photon interference on a partially polarizing beam splitter (PPBS) with intensity transmittances  $T_{H} = 1$  and  $T_{V} = 1 / 3$  for horizontally and vertically polarized photons, respectively [12,27-30]. The scheme also requires two additional

PPBSs for balancing the amplitudes. The  $\pi$  phase shift due to two-photon interference on the central PPBS occurs only if the signal photon travels through the lower interferometer arm and both photons are vertically polarized (logical qubit states  $|1\rangle$ ). This probabilistic CCZ gate operates in the coincidence basis [21] and its successful operation is indicated by detection of two-photon coincidences D1 and D3, D1 and D4, D2 and D3, or D2 and D4 at the output. Other detection events correspond to gate failure and are rejected and not used in the subsequent analysis. Ideal success probability of the CCZ gate is  $1/9$  which is the maximum value achievable without the use of ancilla photons [31].

We have prepared the input states  $|\psi_{j,k}\rangle$ ,  $k = 1,2,3$ , as listed in Table I and for each input we have performed projective measurement on the output in the product basis  $\{|\psi_{j,k}\rangle \}_{j = 1}^{8}$ . The results are shown in Fig. 2 and they can also be interpreted as the computational basis truth tables of the Toffoli gates where the target qubit is the first, the second, and the third qubit, respectively. The parameters  $f_{j,k}$  and  $p_{j,k}$  necessary for evaluation of the average state fidelities  $F_{k}$  were determined as follows. Let  $C_{j,j^{\prime}}^{k}$  denote the number of detected coincidences corresponding to projection onto  $U_{\mathrm{CCZ}}|\psi_{j^{\prime},k}\rangle$  for input  $|\psi_{j,k}\rangle$ . Then  $f_{j,k} = C_{j,j}^{k} / S_{j}^{k}$ , where  $S_{j}^{k} = \sum_{j^{\prime} = 1}^{8}C_{j,j^{\prime}}^{k}$  is the total number of coincidences for a given input. In our measurement,  $S_{j}^{k}\approx 6.6\times 10^{4}$  on average. Since all  $C_{j,j^{\prime}}^{k}$  were measured for the same time interval of  $100\mathrm{s}$ , the relative success probabilities can be determined as the normalized total number of coincidences,  $p_{j,k} = 8S_j^k /S^k$  where  $S^k = \sum_{j = 1}^{8}S_j^k$

![](images/b3eee864b73089f2f46d013795f5b910352a6f2a602d67edc25d670897d72c4c.jpg)  
FIG. 2 (color online). Experimentally determined truth tables characterizing performance of the CCZ gate in three partially conjugate product bases  $k = 1$  (a),  $k = 2$  (b) and  $k = 3$  (c).

![](images/eb6e7af685bdc1821f92f80dab9759cf1ed28d93b7caef67f6b814f4e544a21e.jpg)

![](images/1095ff28036fb98483634c0ca5742b963aa4aba2f3d098241cfa27392ebfd206.jpg)

The estimated  $p_{j,k}$  lie in the interval [0.902, 1.079]. On inserting the expressions for  $f_{j,k}$  and  $p_{j,k}$  into Eq. (5) we get  $F_{k} = \sum_{j=1}^{8} C_{j,j}^{k} / S^{k}$ , which yields

$$
F _ {1} = 0. 9 2 8 (1), \quad F _ {2} = 0. 9 4 7 (1), \quad F _ {3} = 0. 9 5 5 (1). \tag {10}
$$

The statistical errors represent 3 standard deviations  $\sigma_{k}$ , which were determined assuming Poissonian statistics of the measured coincidences,  $\sigma_{k}^{2} = F_{k}(1 - F_{k}) / S^{k}$ . If we plug the fidelities (10) into formula (7) we obtain a lower bound on the fidelity of the implemented linear optical CCZ gate,

$$
F _ {\chi} \geq 0. 8 3 0 (2). \tag {11}
$$

For comparison, we have also experimentally determined the original Hofmann bound on the process fidelity (1). For this purpose we consider two bases labeled  $k = 3$  and  $k = 3'$  connected by Hadamard transforms of all three qubits,  $|\psi_{j,3'}\rangle = H \otimes H \otimes H|\psi_{j,3}\rangle$ . The input states  $|\psi_{j,3'}\rangle$  are explicitly listed in the last column of Table I. It holds that  $F_{\chi} \geq F_3 + F_{3'} - 1$ , where both fidelities are given by Eq. (5). This inequality can be equivalently expressed as  $\mathrm{Tr}[R' \chi] / \mathrm{Tr}[\chi] \geq 0$ , where  $R' = \frac{1}{8} \chi_{\mathrm{CCZ}} - R_3 - R_{3'} + \mathbb{I}$ . Similarly as before, one can explicitly show that  $R' \geq 0$ , which proves the above inequalities. The determination of  $F_{3'}$  requires measurement of fidelities of entangled output states, since for instance  $U_{\mathrm{CCZ}}|++1\rangle = (1/\sqrt{2})(|0+\rangle + |1-\rangle)|1\rangle$ . Fortunately, in our setup the projection onto the maximally entangled states of qubits 1 and 2 can be accomplished deterministically because both these qubits are carried by a single photon. We only have to rotate the HWP2 by  $45^\circ$  which acts as a CNOT gate between the polarization and spatial qubits carried by a single photon and transforms the maximally entangled states onto product states. From the measurements we have determined  $F_{3'} = 0.921(1)$  which together with  $F_3 = 0.955(1)$  as given in Eq. (10) yields  $F_{\chi} \geq 0.876(2)$ . We can see that at the cost of measuring fidelities of entangled states we obtain a slightly higher fidelity bound. This is universally valid because  $R - R' \geq 0$ . Since  $R_k - \frac{1}{8} \chi_{\mathrm{CCZ}} \geq 0$  for all

$k = 1,2,3,3^{\prime}$  , the average state fidelities also provide an upper bound on the gate fidelity [11],  $F_{\chi}\leq \min (F_k)$  Specifically, we get  $F_{\chi}\leq 0.921(1)$

Finally, we explicitly demonstrate the capability of the three-qubit CCZ gate to generate entanglement from input separable states  $|\psi_1\rangle |\psi_2\rangle |\psi_3\rangle$ , where  $|\psi_j\rangle = c_0^j |0\rangle +c_1^j |1\rangle$  (partially entangled inputs are considered in the Supplemental Material [25]). The corresponding output state reads  $U_{\mathrm{CCZ}}|\psi_1\psi_2\psi_3\rangle = |\psi_1\psi_2\psi_3\rangle -2c_1^1 c_1^2 c_1^3 |111\rangle$ ; hence, the gate generates Greenberger-Horne-Zeilinger - type three-qubit entangled states [32,33]. As an example, in Fig. 3 we plot the reconstructed output state corresponding to the input product state  $| + + + \rangle$ . The fidelity of the reconstructed state with the ideal state is  $F = 0.951$  and its purity  $\mathcal{P} = \mathrm{Tr}[\rho^2]$  reads  $\mathcal{P} = 0.959$ .

In summary, we have proposed a lower bound on the quantum process fidelity of multiqubit quantum gates which generalizes the original Hofmann bound and we used it to experimentally characterize a linear optical quantum CCZ gate. The advantage of our generalized fidelity bound is that only fidelities of product multiqubit quantum states need to be measured and the required number of measurement settings is much smaller than what is needed for full quantum process tomography or gate fidelity estimation by Monte Carlo sampling (see the Supplemental Material [25]). We hope that our work will represent a useful addition to the toolbox of methods for the efficient and experimentally feasible characterization of quantum devices.

![](images/81865e609b1e6d24e20fac05cf180dde85ee264adc9f20d1b10df14a7729a422.jpg)  
FIG. 3 (color online). Real (a) and imaginary (b) parts of the reconstructed density matrix of a three-qubit state generated by the CCZ gate from input product state  $| + + + \rangle$ .

![](images/93c56c031d08bb5848b44c8e2fbb9434a87d7f88972bbb9367ccd42ea5b008b2.jpg)

This work was supported by the Czech Science Foundation (13-20319S). M. S. acknowledges support by the Operational Program Education for Competitiveness—European Social Fund (Project No. CZ.1.07/2.3.00/30.0004) of the Ministry of Education, Youth, and Sports of the Czech Republic.

[1] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2000).  
[2] Quantum State Estimation, Lecture Notes in Physics Vol. 649, edited by M. Paris and J. Reháček (Springer, Heidelberg, 2004).  
[3] D. Gross, Y.-K. Liu, S.T. Flammia, S. Becker, and J. Eisert, Phys. Rev. Lett. 105, 150401 (2010).  
[4] A. Shabani, R.L. Kosut, M. Mohseni, H. Rabitz, M.A. Broome, M.P. Almeida, A. Fedrizzi, and A.G. White, Phys. Rev. Lett. 106, 100401 (2011).  
[5] S. T. Flammia and Y.-K. Liu, Phys. Rev. Lett. 106, 230501 (2011).  
[6] M. P. da Silva, O. Landon-Cardinal, and D. Poulin, Phys. Rev. Lett. 107, 210404 (2011).  
[7] L. Steffen, M.P. da Silva, A. Fedorov, M. Baur, and A. Wallraff, Phys. Rev. Lett. 108, 260506 (2012).  
[8] A. Bendersky, F. Pastawski, and J. P. Paz, Phys. Rev. Lett. 100, 190403 (2008).  
[9] J. Emerson, M. Silva, O. Moussa, C. Ryan, M. Laforest, J. Baugh, D. G. Cory, and R. Laflamme, Science 317, 1893 (2007).  
[10] D. M. Reich, G. Gualdi, and C. P. Koch, Phys. Rev. A 88, 042309 (2013); arXiv:1305.5649.  
[11] H.F. Hofmann, Phys. Rev. Lett. 94, 160504 (2005).  
[12] R. Okamoto, H.F. Hofmann, S. Takeuchi, and K. Sasaki, Phys. Rev. Lett. 95, 210506 (2005).  
[13] X.H. Bao, T.Y. Chen, Q. Zhang, J. Yang, H. Zhang, T. Yang, and J.W. Pan, Phys. Rev. Lett. 98, 170502 (2007).  
[14] A. S. Clark, J. Fulconis, J. G. Rarity, W. J. Wadsworth, and J. L. OBrien, Phys. Rev. A 79, 030303(R) (2009).  
[15] W. B. Gao, P. Xu, X.-C. Yao, O. Gühne, A. Cabello, C.-Y. Lu, C.-Z. Peng, Z. B. Chen, and J. W. Pan, Phys. Rev. Lett. 104, 020501 (2010).  
[16] W.B. Gao, A.M. Goebel, C.Y. Lu, H.N. Dai, C. Wagenknecht, Q.A. Zhang, B. Zhao, C.Z. Peng, Z.B. Chen, Y.A. Chen, and J.W. Pan, Proc. Natl. Acad. Sci. U.S.A. 107, 20869 (2010).

[17] X.Q. Zhou, T.C. Ralph, P. Kalasuwan, M. Zhang, A. Peruzzo, B.P. Lanyon, and J.L. O'Brien, Nat. Commun. 2, 413 (2011).  
[18] B.P. Lanyon, C. Hempel, D. Nigg, M. Müller, R. Gerritsma, F. Zähringer, P. Schindler, J.T. Barreiro, M. Rambach, G. Kirchmair, M. Hennrich, P. Zoller, R. Blatt, and C.F. Roos, Science 334, 57 (2011).  
[19] B.P. Lanyon, M. Barbieri, M.P. Almeida, T. Jennewein, T.C. Ralph, K.J. Resch, G.J. Pryde, J.L. O'Brien, A. Gilchrist, and A.G. White, Nat. Phys. 5, 134 (2009).  
[20] T. Monz, K. Kim, W. Hänsel, M. Riebe, A. S. Villar, P. Schindler, M. Chwalla, M. Hennrich, and R. Blatt, Phys. Rev. Lett. 102, 040501 (2009).  
[21] Pieter Kok, W.J. Munro, Mae Nemoto, T.C. Ralph, Jonathan P. Dowling, and G.J. Milburn, Rev. Mod. Phys. 79, 135 (2007).  
[22] A. Jamiolkowski, Rep. Math. Phys. 3, 275 (1972).  
[23] M.-D. Choi, Linear Algebra Appl. 10, 285 (1975).  
[24] B. Bell, A. S. Clark, M. S. Tame, M. Halder, J. Fulconis, W. J. Wadsworth, and J. G. Rarity, New J. Phys. 14, 023021 (2012).  
[25] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.111.160407 for detailed proof of the bound (9), comparison of our technique with Monte Carlo sampling, and discussion of generation of a maximally entangled three-qubit Greenberger-Horne-Zeilinger state.  
[26] M. Ježek, I. Straka, M. Mičuda, M. Dusek, J. Fiurášek, and R. Filip, Phys. Rev. Lett. 107, 213602 (2011).  
[27] N. K. Langford, T. J. Weinhold, R. Prevedel, K. J. Resch, A. Gilchrist, J. L. O'Brien, G. J. Pryde, and A. G. White, Phys. Rev. Lett. 95, 210504 (2005).  
[28] N. Kiesel, C. Schmid, U. Weber, R. Ursin, and H. Weinfurter, Phys. Rev. Lett. 95, 210505 (2005).  
[29] T.C. Ralph, N.K. Langford, T.B. Bell, and A.G. White, Phys. Rev. A 65, 062324 (2002).  
[30] H.F. Hofmann and S. Takeuchi, Phys. Rev. A 66, 024308 (2002).  
[31] K. Lemr, A. Cernoch, J. Soubusta, K. Kieling, J. Eisert, and M. Dušek, Phys. Rev. Lett. 106, 013602 (2011).  
[32] D. M. Greenberger, M. Horne, and A. Zeilinger, in *Bells Theorem*, Quantum Theory, and Conceptions of the Universe, edited by M. Kafatos (Kluwer, Dordrecht, 1989), p. 69.  
[33] W. Dü, G. Vidal, and J. I. Cirac, Phys. Rev. A 62, 062314 (2000).