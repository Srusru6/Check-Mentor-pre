# Generation of genuine entanglement up to 51 superconducting qubits

https://doi.org/10.1038/s41586-023-06195-1

Received: 14 August 2022

Accepted: 11 May 2023

Published online: 12 July 2023

Check for updates

Sirui Cao $^{1,2,3,6}$ , Bujiao Wu $^{4,5,6}$ , Fusheng Chen $^{1,2,3,6}$ , Ming Gong $^{1,2,3,6}$ , Yulin Wu $^{1,2,3}$ , Yangsen Ye $^{1,2,3}$ , Chen Zha $^{1,2,3}$ , Haoran Qian $^{1,2,3}$ , Chong Ying $^{1,2,3}$ , Shaojun Guo $^{1,2,3}$ , Qingling Zhu $^{1,2,3}$ , He-Liang Huang $^{1,2,3}$ , Youwei Zhao $^{1,2,3}$ , Shaowei Li $^{1,2,3}$ , Shiyu Wang $^{1,2,3}$ , Jiale Yu $^{1,2,3}$ , Daojin Fan $^{1,2,3}$ , Dachao Wu $^{1,2,3}$ , Hong Su $^{1,2,3}$ , Hui Deng $^{1,2,3}$ , Hao Rong $^{1,2,3}$ , Yuan Li $^{1,2,3}$ , Kaili Zhang $^{1,2,3}$ , Tung-Hsun Chung $^{1,2,3}$ , Futian Liang $^{1,2,3}$ , Jin Lin $^{1,2,3}$ , Yu Xu $^{1,2,3}$ , Lihua Sun $^{1,2,3}$ , Cheng Guo $^{1,2,3}$ , Na Li $^{1,2,3}$ , Yong-Heng Huo $^{1,2,3}$ , Cheng-Zhi Peng $^{1,2,3}$ , Chao-Yang Lu $^{1,2,3}$ , Xiao Yuan $^{3,4,5}$ , Xiaobo Zhu $^{1,2,3}$  & Jian-Wei Pan $^{1,2,3}$

Scalable generation of genuine multipartite entanglement with an increasing number of qubits is important for both fundamental interest and practical use in quantum-information technologies $^{1,2}$ . On the one hand, multipartite entanglement shows a strong contradiction between the prediction of quantum mechanics and local realization and can be used for the study of quantum-to-classical transition $^{3,4}$ . On the other hand, realizing large-scale entanglement is a benchmark for the quality and controllability of the quantum system and is essential for realizing universal quantum computing $^{5-8}$ . However, scalable generation of genuine multipartite entanglement on a state-of-the-art quantum device can be challenging, requiring accurate quantum gates and efficient verification protocols. Here we show a scalable approach for preparing and verifying intermediate-scale genuine entanglement on a 66-qubit superconducting quantum processor. We used high-fidelity parallel quantum gates and optimized the fidelities of parallel single- and two-qubit gates to be  $99.91\%$  and  $99.05\%$ , respectively. With efficient randomized fidelity estimation $^{9}$ , we realized 51-qubit one-dimensional and 30-qubit two-dimensional cluster states and achieved fidelities of  $0.637 \pm 0.030$  and  $0.671 \pm 0.006$ , respectively. On the basis of high-fidelity cluster states, we further show a proof-of-principle realization of measurement-based variational quantum eigensolver $^{10}$  for perturbed planar codes. Our work provides a feasible approach for preparing and verifying entanglement with a few hundred qubits, enabling medium-scale quantum computing with superconducting quantum systems.

Recent progress in quantum hardware, especially superconducting quantum processors $^{11-13}$ , has verified the potential of programmable quantum devices that use shallow-depth circuits consisting of multilayers of single- and two-qubit gates on tens of qubits. Although these devices have successfully been used for realizing random quantum circuits sampling and demonstrating quantum-computational advantages on tens of qubits, the state fidelity reported is relatively low  $(< 1\%)$ ^{11-13}, which is sufficient for use in realistic applications.

Because essential ingredients of most quantum-computing algorithms and quantum-information processing protocols rely on quantum entanglement $^{3-8}$ , great efforts have also been made in implementing high-fidelity entangled multi-qubit states $^{14-18}$ . In the field of superconducting quantum computing, the largest genuine entanglement is the 18-qubit Greenberger-Horne-Zeilinger (GHZ) states $^{14}$ , realized with collective interactions. However, such a scheme requires coupling all qubits to the common bus resonator without using digital quantum gates, this may be hard to generalize to other entangled

states or to extend to larger systems. The largest genuine entangled state using digital superconducting gates has only 12 qubits $^{18}$ , a much smaller size than those of state-of-the-art superconducting devices. Entangling a larger number of qubits is a much more challenging task, requiring notable experimental improvements in the device quality and efficient theoretical means for entanglement verification.

Here we present a systematic study to prepare one-dimensional (1D) and two-dimensional (2D) cluster states with varying system sizes and verify genuine entanglement of up to 51 qubits. The success of our experiment relies on both experimental and theoretical improvements. First, we realized high-fidelity parallel two-qubit gates on a high-performance 2D quantum processor $^{12,13}$  with a tunable coupling architecture, notably reducing the operating time to generate the entanglement. Second, we applied an efficient and accurate readout calibration process, eliminating most of the errors. Third, we used randomized fidelity estimation $^9$  to verify genuine entanglement, which significantly reduced the number of measurements for state verification.

<sup>1</sup>Hefei National Research Center for Physical Sciences at the Microscale and School of Physical Sciences, University of Science and Technology of China, Hefei, China. <sup>2</sup>Shanghai Research Center for Quantum Science and CAS Center for Excellence in Quantum Information and Quantum Physics, University of Science and Technology of China, Shanghai, China. <sup>3</sup>Hefei National Laboratory, University of Science and Technology of China, Hefei, China. <sup>4</sup>Center on Frontiers of Computing Studies, Peking University, Beijing, China. <sup>5</sup>School of Computer Science, Peking University, Beijing, China. <sup>6</sup>These authors contributed equally: Sirui Cao, Bujiao Wu, Fusheng Chen, Ming Gong. <sup>e</sup>-mail: xiaoyuan@pku.edu.cn; xbzhu16@ustc.edu.cn; pan@ustc.edu.cn

![](images/4d29953a471918ab73e24cbbc29ee7bf3c7819ab59e0c5ecbacfc536fcd6c3e8.jpg)  
Fig. 1| Generation and verification of cluster states. a, The cluster state is prepared by initializing the states in  $|0\rangle^{\otimes n}$ , followed by sequential single-qubit gates  $\sqrt{Y}$  and layers of CZ gates. The state is then measured using random stabilizers generated with a classic computer to verify the fidelity. The stabilizer measurement is realized by using a layer of local Clifford gates. We choose the identity matrix  $I$  (no shading) or the generator  $S_{k}$  (with shading) for each qubit. Different choices of the operator thus determine different stabilizers corresponding to different Pauli measurement basics for each

![](images/6227c1628c0a371076b020fda62cc5ad6a0dee03f7402408d239af301fe99968.jpg)  
qubit. The random stabilizer measurements of the cluster state are then fed forward to the classic computer to estimate the state fidelity and to verify the genuine entanglement of the prepared cluster states.  $\mathbf{b}$ , Realization of the CZ layers. On a 2D quantum processor with tunable couplers, we can experimentally realize CZ operations connecting all nearest-neighbouring qubit pairs with only four layers. In each layer, the CZ gates are applied simultaneously. We note that the pattern of the four layers is adjustable in practice. QPU, quantum-processing unit.

These improvements enable the consistent generation and verification of genuinely entangled 1D and 2D cluster states with near-term quantum devices. Furthermore, using high-fidelity cluster states as the resource, we realized a measurement-based variational quantum eigensolver $^{10}$  for perturbed planar codes and observed accurately prepared ground states and phase transitions with different perturbations.

We first briefly introduce the basics of cluster states and the entanglement witness. Cluster states, a typical class of graph states $^{19}$ , is the critical resource for one-way quantum computing $^{20-23}$  and the measurement-based variational quantum eigensolver $^{10}$ . An  $n$ -qubit cluster state on a 1D or 2D graph  $G(V,E)$  can be denoted as

$$
| \mathrm {C L} \rangle = \prod_ {(i, j) \in E} \mathrm {C Z} ^ {(i, j)} | + \rangle^ {\otimes n}, \tag {1}
$$

where CZ is the controlled-phase gate between qubits  $i$  and  $j$ ,  $| + \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$  and  $E$  represents the edges of the lattice graph  $G$ . For an experimentally prepared noisy cluster state  $\hat{\rho}_{\mathrm{CL}}$ , we can detect its entanglement using an entanglement witness

$$
\mathcal {W} = \frac {I}{2} - \rho_ {\mathrm {C L}}, \tag {2}
$$

where  $\rho_{\mathrm{CL}} = |\mathrm{CL}\rangle \langle \mathrm{CL}|$  is the density matrix of the ideal cluster state, and  $I$  is the density matrix. As  $\operatorname{tr}(\mathcal{W}\sigma)\geq 0$  for all biseparable states  $\sigma$ , the noisy state  $\hat{\rho}_{\mathrm{CL}}$  is genuinely entangled if  $\langle \mathcal{W}\rangle = \operatorname{tr}(\hat{\rho}_{\mathrm{CL}}\mathcal{W}) < 0$ . To measure  $\mathcal{W}$ , we consider an explicit expansion of the density matrix<sup>24</sup> with respect to its stabilizer as

$$
\rho_ {\mathrm {C L}} = \prod_ {k \in V} \frac {I + S _ {k}}{2}, \tag {3}
$$

where  $S_{k} = X_{k}\prod_{(j,k)\in E}Z_{j}$  are the generators of the stabilizers, and  $V$  is the vertices set of graph  $G$ . As there are  $2^{n}$  stabilizers in total that increase exponentially with the number of qubits, we cannot directly measure all the stabilizers<sup>25</sup>. Instead, we use the randomized fidelity estimation method<sup>9</sup>. At the  $j$ th run, the stabilizer  $P^{(j)}$  can be selected as

$$
P ^ {(j)} = \prod_ {k} P _ {k} ^ {(j)}, \tag {4}
$$

where each  $P_{k}^{(j)}$  is randomly chosen to be the identity or the generator  $S_{k}$  at node  $k$  with uniform probability. Denoting the average outcome of the stabilizer  $P^{(j)}$  as  $\mathrm{tr}(\hat{\rho}_{\mathrm{CL}}P^{(j)})$  and the number of random stabilizers as  $m$ , we can show that the average measurement

$$
\bar {v} = \frac {1}{m} \sum_ {j} \operatorname {t r} \left(\hat {\rho} _ {\mathrm {C L}} P ^ {(j)}\right) \tag {5}
$$

provides an unbiased estimation of the fidelity  $\mathrm{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$  and correspondingly the witness value  $\mathrm{tr}(\hat{\rho}_{\mathrm{CL}}\mathcal{W}) = 1 / 2 - \mathrm{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$ . According to Hoeffding's inequality, we can choose the number of stabilizers to be  $m\propto \log (1 / \delta) / \varepsilon^2$  (independent of the number of qubits) to have a small estimation error  $\varepsilon$  with a small failure probability  $\delta$  (Methods).

On the quantum processor with a 2D structure, the CZ operations connecting all adjacent qubits can be realized with four CZ layers (Fig. 1b). Once the CZ layer can be experimentally realized in parallel, such a feature can significantly shorten the total operation time in entanglement generation and is scalable to larger systems. We carried out the experiments on a 66-qubit superconducting quantum processor with tunable coupling structure $^{12}$ . Leveraging the advanced features of the state-of-the-art quantum device, including the design

![](images/f6ebb607e272ba20be1a4697017cca5b02cdaef3e24d3c3114f94bac8e0c4bf5.jpg)  
a

![](images/a9a61e03a27f08aeff22282e603903805814add2e586115b007c46357b9861e0.jpg)  
b

![](images/ad5aba8e204fbaa69fabb7b3b168b9732b5c0284c3e221b0fd09c4feb51b6a2a.jpg)  
C

![](images/989a9397b6e617bb2c07d40fe73d1a55f7971a4b33d44d21e94a729ea4bc7a01.jpg)  
d  
Fig. 2 | Performance of the quantum processor. a, Realization of CZ gates between a pair of qubits with a tunable coupler. Z control pulses are applied to the involved qubits to tune them to the interacting frequencies. Then, the coupling strength is adjusted by applying a Slepian-shaped waveform to the coupler $^{26}$ . The overall operation takes about 50 ns. b, Distribution of average errors of the single-qubit (blue) and CZ (red and purple) gates and readout (yellow) errors. The overall average errors are  $0.09\%$  (blue),  $0.95\%$  (red),  $1.02\%$  (purple) and  $4.91\%$  (yellow), respectively. The number of CZ gates in the groups for generating the largest 1D (red) and 2D (purple) cluster states is 50 and 46, respectively. The average error of CZ gates takes all gates in the two groups into account. c, We run an independent circuit that prepares random initial states on a computational basis, followed by a computational-basis measurement. It enables us to detect the correlation and construct the error model of the state readout. d, Correlations of the readout errors  $1_{j}1_{k} \rightarrow 0_{j}0_{k}$  for all of the qubit pairs  $(j,k)$ . The correlation of two-qubit error on sites  $j$  and  $k$ ,  $\mathrm{cov}[x_j x_k \rightarrow \overline{x}_j \overline{x}_k]$ , is defined as the covariance of events that  $x_{j}$  and  $x_{k}$  flip, which equals  $\mathrm{Pr}[1_{j}1_{k} \rightarrow 0_{j}0_{k}] - \mathrm{Pr}[1_{j} \rightarrow 0_{j}] \mathrm{Pr}[1_{k} \rightarrow 0_{k}]$ . The average correlation is around  $3 \times 10^{-4}$ , which is negligible.

of tunable couplers and the application of the flip-chip technique, we achieved ultralow crosstalk during gate operations. We can thus simultaneously apply CZ gates between adjacent qubit pairs. We used the tunable couplers to perform the CZ gates $^{26}$  (Fig. 2a). After resolving the pulse distortion on the couplers and optimizing the parallel CZ gates (Methods), we obtained high-fidelity parallel gates. Finally, using cross-entropy benchmarking $^{27}$  to characterize the gates, we obtained fidelities of  $99.91\%$  and  $99.05\%$  for the parallel single-qubit and CZ gates, respectively (Fig. 2b). This high level of quantum-gate fidelity provides a basis for generating genuine multi-qubit entanglement states.

In our experiment, there are also non-negligible readout errors. To characterize such errors, we ran 5,298 and 1,800 different random initial states on a computational basis, with each accumulating 10,000 single-shot measurements for the 51-qubit 1D and 30-qubit 2D cluster states, respectively (Fig. 2c). We evaluated the correlation of readout errors of different qubits from the random initial-state preparation and calculated the covariance (Fig. 2d). We found that their correlation is negligible for our device. Thus, we can independently correct these errors for each qubit (Methods). We estimated the average readout error  $\varepsilon_r$  of each qubit to be 0.06 with vanishing uncertainties for the 1D and 2D cluster states. The readout error-correction process introduces an overhead  $\mathrm{e}^{4n\varepsilon_r}$  on the number of measurements. We thus need more measurements for larger systems.

In our experiment, we first prepared 1D cluster states with 3 to 51 qubits, the topology of which is shown in Fig. 3a. The quantum circuit (Fig. 1a) consists of a layer of  $\sqrt{Y}$  ( $R_{y}(\pi /2)$ ) gates, two layers of parallel CZ gates and randomly generated stabilizer measurements realized using a layer of local Clifford gates. Because the CZ gates are applied in parallel, the total operation time for the state generation is only 135 ns. To verify the 51-qubit cluster state, we generated  $M = 43,992$  uniformly random stabilizers to estimate the cluster-state fidelity. Each stabilizer repeated  $T = 10^{4}$  single-shot measurements, with a total of  $4.3992\times 10^{8}$  single-shot measurements. The measurement took 31 hours in total. For the generation of cluster states with other sizes, we left those qubits that were not involved idle and turned off the coupling by turning the couplers. Finally, we plotted the fidelities of the

![](images/5097ccba8f9d7e9bedf5a85dd6299de7ebcd9de29cf4aea8d40844430d9c1b8e.jpg)  
a

![](images/3fc885552ac689d0eea660ee76bf682bf30f634e334edc39f9bd57c591a9d48a.jpg)  
b  
Fig. 3 | Generation and verification of genuine 1D and 2D cluster states. a,c, The structures for 1D (a) and 2D (c) cluster states. Edges with the same colour indicate simultaneously applied CZ gates. The structures for 1D and 2D cluster states consist of two and four layers of CZ gates, respectively. b,d, Estimated fidelities of 1D (b) and 2D (d) cluster states with varying numbers of qubits. The error bars correspond to a  $99.7\%$  confidence interval. All the witness values have negative values, indicating genuine entanglement of all the generated states.

![](images/1cc46e8d331df1a7634eb5abf49e1f1374923a5ed574a79744431b16d0cd6afd.jpg)  
c

![](images/98e3a8fa32c307b19861fb1e0b92bed5fcc6f3ddebecf35b46d338c54cbc3258.jpg)  
d

![](images/c3bf36e20733a0c3d019342d7fd839f8f3bca72fe5c489a678b36542299e01fe.jpg)  
a

![](images/ee973d86d73bdbba7e6609b8fa43b1a38c3b52c52aa081155b826d97f81f53a0.jpg)  
b

![](images/e84310a94453c8a690b400f42d041562dc93e2f02b66f91856903a23763cf9bb.jpg)

![](images/c87a5e1b239dd18b2bef436d6b32244ec6b521edcfa4f24e6f8b415a77e24182.jpg)  
Fig. 4 | A proof-of-principle implementation of MBVQE for perturbed planar codes. a, Schematic of MBVQE for perturbed planar codes: (1) prepare a cluster state of seven qubits; (2) sequentially measure the first three qubits in the parameterized basis  $(1 / \sqrt{2})\{|0\rangle \pm \mathrm{e}^{\mathrm{i}\theta_k}|1\rangle \}$  with  $\theta_{k} = (-1)^{m_{k - 1}}\phi_{k^{*}}$  tunable basis parameters  $\phi_{k}$  and binary measurement outcomes of the  $k$ th qubit  $m_{k}$  for  $k\in \{1,2,3\}$ , and let  $m_0 = 0$ ; (3) measure observable  $M$  (equivalent to the Hamiltonian  $\mathbf{H}(\lambda)$  up to local unitary rotations) for the remaining four qubits; (4) optimize the parameters classically to minimize the expectation value. b, Realization of MBVQE on the quantum processor. We choose seven qubits with reference to the pattern in a. Starting from  $|0^{\otimes 7}\rangle$ , we applied  $\sqrt{Y}$  gates, followed by four layers of CZ gates, to generate the cluster state. Then the

![](images/934c897c417a46b19b7291a85951676f866d083194594496f26896dcbaa03e0f.jpg)  
qubits  $Q_{1}$  to  $Q_{3}$  are measured in basis  $(1 / \sqrt{2})\{|0\rangle \pm \mathrm{e}^{\mathrm{i}\theta_{k}}|1\rangle \}$ , which are realized with the single-qubit gates  $U(\theta_k) = R_Z(\theta_k)\cdot \sqrt{Y} R_Z(\theta_k)$  and  $Z$  projection measurements. The remaining four qubits are also measured simultaneously with two Pauli observables XZZZ and ZXXX. The feedforward operation is simplified with a measurement-based post-selection step, in which we select parts of the basis such that  $\theta_{k} = (-1)^{m_{k}}\phi_{k}$  for  $k\in \{1,2,3\}$ . c,d, The energy and order parameter  $Z_{1}$  for different  $\lambda$  values. The blue and purple solid lines are the exact solutions for the ground and first excited states, respectively. The orange circles are the experimentally obtained results. The yellow crosses correspond to simulated numerical results with the experimentally obtained parameters  $\Phi$  without considering readout errors.

3- to 51-qubit 1D cluster states generated in Fig. 3b. We estimated the fidelities using the following equation:

$$
v = \frac {1}{M T} \sum_ {j = 1} ^ {M} \sum_ {t = 1} ^ {T} \operatorname {s i g n} \left(P ^ {(j)}\right) \prod_ {k = 1} ^ {n} \sum_ {x _ {k} \in \{0, 1 \}} \left(1 - 2 x _ {k}\right) \langle x _ {k} | \Lambda_ {k} ^ {- 1} | s _ {j, t, k} \rangle \tag {6}
$$

where stabilizer  $P^{(j)}$  is defined in equation (4),  $s_{j,t} \in \{0,1\}^n$  is the  $t$ th single-shot measurement outcomes with stabilizer  $P^{(j)}$  and  $\Lambda_k \in \mathbb{R}^{2 \times 2}$  is the transformation matrix of the  $k$ th qubit (Methods). Equation (6) provides an unbiased estimation of  $\mathrm{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$  and corrects readout errors for estimations in equation (5). We observed that the estimated fidelities of the different sizes are higher than 0.5. In particular, the fidelity of the 51-qubit cluster state is  $0.637 \pm 0.030$  with a confidence interval of  $99.7\%$ .

Next, we considered the preparation and verification of 2D cluster states. As shown in Fig. 3c, similar to the generation of the linear 1D cluster states, the two-qubit CZ gates are applied in parallel, and all CZ gates are realized in four layers. The total operation time for generating the 2D cluster state is 265 ns. We considered the preparation of 2D cluster states ranging from 5 to 30 qubits. The estimated fidelity for the 30-qubit state is obtained by randomly picking  $M = 11,223$  stabilizer settings with uniform probability. The total number of single-shot measurements is  $1.1223 \times 10^8$ , and the preparation and measurements

took 8 hours in total. As shown in Fig. 3d, the estimated fidelities of the different sizes are higher than 0.5; the fidelity of the 30-qubit 2D cluster state is  $0.671 \pm 0.006$ . In the Supplementary Information, we consider two more-effective entanglement witnesses, the fully decomposable witness and the fully positive partial transposition witness[28,29]. The witness values are all negative, demonstrating genuine entanglement for all the generated states.

The preparation of high-fidelity cluster states plays an important part in quantum computing. A notable recent theoretical proposal is the measurement-based variational quantum eigensolver (MBVQE) $^{10}$ , which leverages ideas from both measurement-based and variational quantum computing and solves eigenstate problems using a shallow circuit. Here we demonstrate a proof-of-principle implementation of the MBVQE for perturbed planar codes. We consider a square lattice with Hamiltonian  $\mathbf{H}_0 = X_1X_2X_3X_4 + Z_1Z_2 + Z_2Z_3 + Z_3Z_4$  acting on four qubits. The ground state of  $\mathbf{H}_0$  is exactly solvable as a specific cluster state followed by certain single-qubit operations, which could be prepared directly using our hardware. Now, we consider a perturbed Hamiltonian  $\mathbf{H}(\lambda) = -\mathbf{H}_0 - \lambda Z_1$  with different  $\lambda$  and the task is to find the ground state of  $\mathbf{H}(\lambda)$ . The basic idea of MBVQE is to extend the cluster state for  $\mathbf{H}_0$  with more entangled ancillas, measure the ancillary states in a parameterized basis and apply feedforward operations to prepare the ground state of  $\mathbf{H}(\lambda)$  (Fig. 4a). The simplified quantum circuit for MBVQE is shown in Fig. 4b (Methods). We plot the energy of the experimentally found

# Article

states (Fig. 4c), which is consistent with the exact solution. We also plot the order parameter  $Z_{1}$  (Fig. 4d) and observe a phase transition with different  $\lambda$ .

This work shows systematic ways to generate 1D and 2D cluster states and verify their genuine entanglement with up to 51 and 30 qubits, respectively. Our techniques could be extended to prepare even larger entanglement, say a few hundred qubits, a foundation for median-scale quantum computing and quantum simulation. Furthermore, the 2D cluster state used could be exploited to realize one-way quantum computing, which requires further steps of entanglement distillation and feedforward manipulations. Our high-fidelity state implies the possibility of successful entanglement distillation to improve the state fidelity further; recent experiments also showed the feasibility of feedforward manipulations $^{30,31}$ . These achievements enable the realization of universal one-way quantum computing. Furthermore, cluster states have also been shown as a useful resource in quantum computing with near-term quantum hardware—that is, the protocol of MBVQE $^{10}$ . Our results show an alternative way of realizing quantum advantages for practical problems in the near term.

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-023-06195-1.

1. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2010).  
2. Horodecki, R., Horodecki, P., Horodecki, M. & Horodecki, K. Quantum entanglement. Rev. Mod. Phys. 81, 865-942 (2009).  
3. Einstein, A., Podolsky, B. & Rosen, N. Can quantum-mechanical description of physical reality be considered complete? Phys. Rev. 47, 777-780 (1935).  
4. Greenberger, D. M., Horne, M. A., Shimony, A. & Zeilinger, A. Bell's theorem without inequalities. Am. J. Phys. 58, 1131-1143 (1990).  
5. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
6. Buluta, I. & Nori, F. Quantum simulators. Science 326, 108-111 (2009).  
7. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
8. Giovannetti, V., Lloyd, S. & Maccone, L. Advances in quantum metrology. Nat. Photon. 5, 222-229 (2011).  
9. Flammia, S. T. & Liu, Y.-K. Direct fidelity estimation from few Pauli measurements. Phys. Rev. Lett. 106, 230501 (2011).

10. Ferguson, R. R. et al. Measurement-based variational quantum eigensolver. Phys. Rev. Lett. 126, 220501 (2021).  
11. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505-510 (2019).  
12. Wu, Y. et al. Strong quantum computational advantage using a superconducting quantum processor. Phys. Rev. Lett. 127, 180501 (2021).  
13. Zhu, Q. & et al. Quantum computational advantage via 60-qubit 24-cycle random circuit sampling. Sci. Bull. 67, 240-245 (2022).  
14. Song, C. et al. Generation of multicomponent atomic Schrödinger cat states of up to 20 qubits. Science 365, 574-577 (2019).  
15. Pogorelov, I. et al. Compact ion-trap quantum computing demonstrator. PRX Quant. 2, 020343 (2021).  
16. Omran, A. et al. Generation and manipulation of Schrödinger cat states in Rydberg atom arrays. Science 365, 570-574 (2019).  
17. Wang, X.-L. et al. 18-qubit entanglement with six photons' three degrees of freedom. Phys. Rev. Lett. 120, 260502 (2018).  
18. Gong, M. et al. Genuine 12-qubit entanglement on a superconducting quantum processor. Phys. Rev. Lett. 122, 110501 (2019).  
19. Gühne, O., Toth, G., Hyllus, P. & Briegel, H. J. Bell inequalities for graph states. Phys. Rev. Lett. 95, 120405 (2005).  
20. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188 (2001).  
21. Briegel, H. J., Browne, D. E., Dür, W., Raussendorf, R. & Van den Nest, M. Measurement-based quantum computation. Nat. Phys. 5, 19-26 (2009).  
22. Raussendorf, R., Browne, D. E. & Briegel, H. J. Measurement-based quantum computation on cluster states. Phys. Rev. A 68, 022312 (2003).  
23. Greganti, C., Roehsner, M.-C., Barz, S., Morimae, T. & Walther, P. Demonstration of measurement-only blind quantum computing. New J. Phys. 18, 013020 (2016).  
24. Gühne, O. & Toth, G. Entanglement detection. Phys. Rep. 474, 1-75 (2009).  
25. Tiurev, K. & Sørensen, A. S. Fidelity measurement of a multiqubit cluster state with minimal effort. Phys. Rev. Res. 4, 033162 (2022).  
26. Ye, Y. et al. Realization of high-fidelity controlled-phase gates in extensible superconducting qubits design with a tunable coupler. Chin. Phys. Lett. 38, 100301 (2021).  
27. Neil, C. et al. A blueprint for demonstrating quantum supremacy with superconducting qubits. Science 360, 195-199 (2018).  
28. Jungnitsch, B., Moroder, T. & Gühne, O. Taming multiparticle entanglement. Phys. Rev. Lett. 106, 190502 (2011).  
29. Jungnitsch, B., Moroder, T. & Gühne, O. Entanglement witnesses for graph states: general theory and examples. Phys. Rev. A 84, 032310 (2011).  
30. Salathé, Y. et al. Low-latency digital signal processing for feedback and feedforward in quantum computing and communication. Phys. Rev. Appl. 9, 034011 (2018).  
31. Andersen, C. K. et al. Entanglement stabilization using ancilla-based parity detection and real-time feedback in superconducting circuits. npj Quantum Inf. 5, 69 (2019).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2023

# Methods

# Parallel CZ gates

In our experiment, high-fidelity parallel CZ gates are critical for achieving high-fidelity cluster states. On the Zuchongzhi 2.0 superconducting quantum processor, we can tune both the frequencies of the transmon qubits and the coupling strength between them. Therefore, we can use resonance coupling between the  $|11\rangle$  and  $|20\rangle$  of the qubits by applying the flux pulses of the qubits and the coupler (see Fig. 2 for the implementation of the CZ gates). To realize high-fidelity parallel CZ gates, the most important thing is to optimize the interaction frequencies in a set of CZ gates. We need to consider factors such as coherence, residual coupling between qubits,  $Z$  pulse distortions<sup>12</sup>.

Coupler trailing and correction. Instead of optimizing iswap-like two-qubit gates as in ref. 12, we added a correction of the coupler flux pulse. Owing to the non-ideal transmission characteristics in the setup, the flux applied to the coupler will generate unwanted pulse distortion, increasing the gate error in the quantum circuit. Therefore, we used a correction for coupler tailing.

The tailing of the flux pulse of the coupler will cause a shift in the frequency of the qubit, resulting in phase accumulation. We therefore use the pulse sequence in Extended Data Fig. 1a to measure the coupler flux-pulse distortion by analysing the phase accumulation of the qubits corresponding to the coupler. In our experiment, we first prepare the qubit in the  $|0\rangle$  state, then apply a square-wave pulse with a length of 500 ns and an amplitude of  $V$  to the coupler, followed by an  $X / 2$  pulse to  $Q_{0}(Q_{1})$  after a delay time. After waiting for the phase accumulation time of 400 ns, we measure the phase of the qubits. Because the flux pulse distortion of a coupler will affect two qubits associated with it, we measure its impact on the two qubits separately. We calculate the response function by fitting the two measurement curves and achieve the correction through reverse waveform compensation[32]. Finally, the comparison of the phase accumulation is shown before and after correction in Extended Data Fig. 1b.

Optimization process for parallel CZ gates. For each group of parallel CZ gate patterns in the cluster-state preparation circuit, we first calculate a set of initial CZ interaction-frequency arrangements using the optimization algorithm and then perform the calibration and optimization of the parallel CZ gates according to the following process.

(1) We prepare the qubits involved in the CZ gate in their  $|11\rangle$  states, scan the detuning of the low-frequency qubits and the coupling strength of the couplers and then measure the state leakage to  $|20\rangle$  (Extended Data Fig. 2a) and the conditional phase  $\Phi$  (Extended Data Fig. 2b). The summary of normalized leakage and conditional phase is used as the cost function (Extended Data Fig. 2c). The parameter corresponding to the minimum value is used as the initial value of the CZ waveform parameter.  
(2) We use the cross-entropy benchmarking fidelity with a fixed cycle of 20 and random circuits of 70 as the cost function to search for the parameters of CZ gates in parallel. We then get a set of optimized CZ waveform parameters.  
(3) We use parallel cross-entropy benchmarking to calibrate the fidelity of the CZ gates corresponding to this group of waveform parameters. For qubits with CZ speckle purity benchmarking (SPB) $^{11}$  Pauli errors greater than  $2\%$ , we sweep their SPB fidelities at a fixed depth of 15 cycles with 70 random circuit instances at different interaction frequencies (Extended Data Fig. 2d) and then select the interaction points with higher SPB fidelity and no frequency conflicts.  
(4) We repeat steps 1, 2 and 3 until the fidelity of the parallel CZ gates no longer improves.

After the above parallel optimization process, we can obtain a set of high-fidelity parallel CZ gates. Finally, the single-qubit, two-qubit and readout fidelities are shown in Extended Data Fig. 3.

# Introduction to entanglement witness

The density matrix of a cluster state  $|G\rangle = \sum_{(i,j)\in E}\mathsf{CZ}^{(i,j)}| + \rangle^n$  can be represented as

$$
\rho_ {\mathrm {C L}} := | G \rangle \langle G | = \prod_ {j = 1} ^ {n} \frac {I + S _ {j}}{2}, \tag {7}
$$

where  $S_{j}\coloneqq X_{j}\prod_{k\in N(j)}Z_{k}$  are generators of the stabilizers of  $\rho_{\mathrm{CL}}$

Using equation (7), we can decompose a cluster state  $\rho_{\mathrm{CL}}$  into

$$
\rho_ {\mathrm {C L}} = \frac {1}{2 ^ {n}} \sum_ {j = 1} ^ {2 ^ {n}} \operatorname {s i g n} (P ^ {(j)}) P ^ {(j)} \tag {8}
$$

where  $P^{(j)} \in \{I, X, Y, Z\}^n$  is an  $n$ -qubit Pauli operator, and each  $P^{(j)}$  associated with its sign can be represented as

$$
\operatorname {s i g n} (P ^ {(j)}) P ^ {(j)} = \prod_ {k = 1} ^ {n} \widetilde {S} _ {k} ^ {\prime}, \tag {9}
$$

where each  $\widetilde{S}_k$  is either  $S_{k}$  or  $I$ . We call  $P^{(j)}$  a Pauli string.

We define an entanglement witness

$$
\mathcal {W} = \frac {I}{2} - \rho_ {\mathrm {C L}}. \tag {10}
$$

A quantum state  $\rho$  is a genuine entangled state if

$$
\langle \mathcal {W} \rangle = \operatorname {t r} (\rho \mathcal {W}) <   0. \tag {11}
$$

Equivalently, a state  $\rho$  is a genuine entangled state if the fidelity  $F(\rho) = \mathrm{tr}(\rho \rho_{\mathrm{CL}}) > 0.5$ . In our experiment, we focus on estimating the fidelity of the prepared noisy cluster state  $\hat{\rho}_{\mathrm{CL}}$  to the ideal cluster state  $\rho_{\mathrm{CL}}$ .

# Measurement scheme

Here we consider the sampling approach to give an estimation of  $\operatorname{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$ , originally introduced in ref. 9. Let  $\mathcal{P}$  denote the set of all of Pauli bases for  $\rho_{\mathrm{CL}}$  in equation (8). Given a prepared cluster state  $\rho_{\mathrm{CL}}$ , a uniformly randomly sampled Pauli measurement setting  $Q \in \mathcal{P}$ , the approximation of  $\operatorname{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$  can be denoted as

$$
v = \sum_ {j = 1} ^ {2 ^ {n}} \mu (P ^ {(j)}) \delta (Q, P ^ {(j)}) \operatorname {s i g n} (P ^ {(j)}) \tag {12}
$$

where  $\mu(P^{(j)}) = \prod_k \mu(P_k^{(j)}) \in \{\pm 1\}^n$ ,  $\mu(P_k^{(j)})$  is the single-shot outcome by measuring the  $k$ th qubit with single-qubit Pauli operator  $P_k^{(j)}$ ,  $\delta(Q, P^{(j)}) = 1$  if  $Q = P^{(j)}$  and  $0$  otherwise. By the definition, we have

$$
\mathbb {E} _ {Q, \mu} [ v ] = \frac {1}{2 ^ {n}} \sum_ {j = 1} ^ {2 ^ {n}} \operatorname {t r} \left(\hat {\rho} _ {\mathrm {C L}} P ^ {(j)}\right) = \operatorname {t r} \left(\hat {\rho} _ {\mathrm {C L}} \rho_ {\mathrm {C L}}\right). \tag {13}
$$

Hence, equation (12) is an unbiased estimation of  $\mathrm{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$ . The error of the estimation is bounded to within  $\varepsilon$  with success probability  $1 - \delta$  if we have the number of  $\mathcal{O}((\log (1 / \delta)) / \varepsilon^2)$  copies of prepared state  $\rho$ , as shown in the following proposition.

Proposition 1. Let  $\rho_{\mathrm{CL}}$  be defined as in equation (8). Given  $(2\log(1/(2\delta))) / \varepsilon^2$  copies of the quantum state  $\rho$ , we can approximate  $\operatorname{tr}(\rho \rho_{\mathrm{CL}})$  to within  $\varepsilon$  error, and  $1 - \delta$  success probability.

This proposition can be obtained using Hoeffding's inequality.

# Correlations of the measurement noise

We show that the Zuchongzhi 2.0 superconducting quantum processor has very weak correlations of measurement errors. Specifically, we show that the covariance for the error of any qubit pairs  $(q_j, q_k)$  is

# Article

very small. We also give the comparison for the covariances of two qubits with different distances in the Supplementary Information.

Let  $E_{1}$  denote the event that the flip error appears in  $q_{j}$  with input  $i_{j}$ , and  $E_{2}$  denote the event that the flip error appears in  $q_{k}$  with input  $i_{k}$ . Let  $\bar{i}_{t} = 1 - i_{t}$ , then

$$
\mathbb {E} \left[ E _ {1} \right] = \Pr \left[ \bar {i} _ {j} \mid i _ {j} \right], \mathbb {E} \left[ E _ {2} \right] = \Pr \left[ \bar {i} _ {k} \mid i _ {k} \right], \mathbb {E} \left[ E _ {1} \wedge E _ {2} \right] = \Pr \left[ \bar {i} _ {j} \bar {i} _ {k} \mid i _ {j} i _ {k} \right] \tag {14}
$$

$$
\operatorname {c o v} \left[ E _ {1}, E _ {2} \right] = \mathbb {E} \left[ E _ {1} \wedge E _ {2} \right] - \mathbb {E} \left[ E _ {1} \right] \mathbb {E} \left[ E _ {2} \right] \tag {15}
$$

To measure the covariance using equation (15) for 51-qubit and 30-qubit quantum devices, we uniformly randomly choose 5,298 initial input settings in  $\{0,1\}^{51}$  and 1,800 initial input settings in  $\{0,1\}^{30}$ , respectively, and independently repeat 10,000 times for each measurement setting. Extended Data Fig. 4 shows the correlations of any two-qubit pairs in 51-qubit and 30-qubit quantum devices. Furthermore, we show the correlations of readout errors  $1_{j}1_{k} \rightarrow 0_{j}0_{k}$  for all pairs of two-qubit gates in the 51-qubit experiment (Fig. 2d).

# Correction of readout errors

Owing to the error introduced during the measurement process, the raw measurement outcomes usually give a much lower fidelity estimation of the prepared state than the real one. The measurement noise can be represented as a stochastic transformation matrix that contains the conditional probabilities for measuring each erroneous state given each ideally measured state.

We carry out the Pauli measurement by performing the stabilizer of the associated Pauli operator to the prepared state, and then measure the state in the computational basis. Let  $s_j \in \{0,1\}^n$  denote the measurement outcomes. Then

$$
\mu \left(s _ {j}\right) := (- 1) ^ {s _ {j}} = \mu \left(P ^ {(j)}\right). \tag {16}
$$

Let  $\Lambda$  be the transformation matrix such that  $\mathbb{E}[s_j] = \Lambda |q\rangle$ , where  $q$  is the ideal outcome without measuring error. The following lemma implies that the estimation

$$
v _ {c} = \frac {1}{M T} \sum_ {j = 1} ^ {M} \operatorname {s i g n} (P ^ {(j)}) \sum_ {t = 1} ^ {T} \sum_ {x \in \{0, 1 \} ^ {n}} \mu (x) \langle x | \Lambda^ {- 1} | s _ {j, t} \rangle
$$

is an unbiased estimation of  $\mathrm{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$  with standard deviation  $\sigma_{\nu_c}\leq \Delta /\sqrt{MT}$ , where  $\mu (x) = \prod_{j = 1}^{n}\mu (x_j),\mu (x_i) = 1 - 2x_i$  is the measured outcome of the ith qubit and  $s_{i,t}\in \{0,1\} ^n$  is the measured bit string.

Lemma 1. Let  $\hat{\rho}_{\mathrm{CL}}$  be the input noisy cluster state,  $\Lambda$  be defined as above. Let  $\upsilon_{\mathrm{c}} = \mathrm{sign}(P_i)\sum_x\mu (x)\langle x|\Lambda^{-1}|s_i\rangle$  be the estimation with a uniformly randomly picked measurement  $P_{i}$  and measurement outcomes  $s_i$ . Then  $\upsilon_{\mathrm{c}}$  is an unbiased estimation of  $\mathrm{tr}(\hat{\rho}_{\mathrm{CL}}\rho_{\mathrm{CL}})$  with standard deviation  $\sigma_{\upsilon_{\mathrm{c}}}\leq \Delta$  where

$$
\Delta = \max  _ {z} \sum_ {x} | \langle x | \Lambda^ {- 1} | z \rangle |. \tag {17}
$$

This lemma can be obtained following a previously published proof<sup>33</sup>. For self-consistency, we give a simpler proof here. It can also be shown that  $|\upsilon_{c}| \leq \Delta$ .

Proof. Let  $\hat{\rho}_{\mathrm{CL}}$  represent the quantum state before measuring, and  $s_i$  be the outcome measured by uniformly randomly picked  $P_i$ . Using the definition of  $\Lambda$  and  $v_{c}$ , we have

$$
\begin{array}{l} \mathbb {E} \left[ v _ {\mathrm {c}} \right] = \sum_ {i} \frac {\operatorname {s i g n} \left(P _ {i}\right)}{2 ^ {n}} \sum_ {x \in \{0, 1 \} ^ {n}} \mathbb {E} \left[ \mu (x) \langle x | \Lambda^ {- 1} | s _ {i} \rangle \right] \\ = \sum_ {i} \operatorname {s i g n} \left(P _ {i}\right) \operatorname {t r} \left(\hat {\rho} _ {\mathrm {C L}} P ^ {(i)}\right) / 2 ^ {n} \tag {18} \\ = \operatorname {t r} \left(\hat {\rho} _ {\mathrm {C L}} \rho_ {\mathrm {C L}}\right) \\ \end{array}
$$

and

$$
\begin{array}{l} \mathbb {E} \left[ v _ {\mathrm {c}} ^ {2} \right] = \sum_ {i} \frac {1}{2 ^ {n}} \sum_ {x, y} \mu (x) \mu (y) \mathbb {E} \left[ \langle x | \Lambda^ {- 1} | s _ {i} \rangle \langle y | \Lambda^ {- 1} | s _ {i} \rangle \right] \\ \leq \max  _ {z} \sum_ {x, y} | \langle x | \Lambda^ {- 1} | z \rangle | | \langle y | \Lambda^ {- 1} | z \rangle | \tag {19} \\ = \Delta^ {2}. \\ \end{array}
$$

Hence,  $\sigma_{\nu_c} = \sqrt{\mathbb{E}[\nu_c^2] - \mathbb{E}[\nu_c]^2}\leq \sqrt{\mathbb{E}[\nu_c^2]}\leq \Delta$

As the readout error in the superconducting device is significantly larger than the preparation error, we address only the readout error and do not consider the preparation error as an important concern. We consider two types of measurement noise: the noise in different qubits that are independent and correlated Markovian noise. In the section 'Correlations of the measurement noise', we demonstrate that the impact of correlated noise is negligible. As a result, we can state that the mitigated estimations using either of the two methods are nearly identical, and both are highly consistent with the mitigated estimation obtained using a complete transformation matrix. Further details can be found in the Supplementary Information, in which we provide a comprehensive analysis of the upper limit of the standard deviation. Furthermore, in the Supplementary Information, we provide a more refined estimate of the upper bound for the error of the estimation.

# VQE on MBQC

Given parameterized Hamiltonian

$$
\mathbf {H} (\lambda) = - \mathbf {H} _ {0} - \mathbf {H} _ {\mathrm {p}} (\lambda) \tag {20}
$$

where  $\mathbf{H}_0 = X_1X_2X_3X_4 + Z_1Z_2 + Z_2Z_3 + Z_3Z_4$  and  $\mathbf{H}(\lambda) = \lambda Z_{1}$ , it is easy to check that the ground state of  $\mathbf{H}(\lambda)$  equals Greenberger-Horne-Zeilinger states when  $\lambda = 0$ . Here we would like to calculate the ground states for other non-trivial values of  $\lambda$  using the measurement-based quantum computing (MBQC) method, in which we generate the ground state and energy simply by generating graph states and measuring it using local parameterized basis associated with parameterized angles  $\Phi = (\phi_{1},\phi_{2},\phi_{3})$ . We approximate the ground state of  $\mathbf{H}(\lambda)$  by finding the optimized  $\rho_{\Phi}$  to minimize  $\operatorname {tr}(\rho_{\Phi}\mathbf{H})$ , where  $\rho_{\Phi}$  is the parameterized state with parameterized angles  $\Phi$ . We also estimate the order parameter  $Z_{1}$  with the generated ground states  $\rho_{\Phi}$ .

Ground-state generation and energy estimation. Using insights from the MBQC method (Supplementary Information), we find that an arbitrary single-qubit unitary  $U(\phi_1, \phi_2, \phi_3)$  can be implemented by the circuit in Fig. 4b and some classic postprocessing. Here we give the ansatz circuit of the ground state of  $\mathbf{H}(\lambda)$  for the MBQC method.

The circuit in Fig. 4b except for the measurements of the last four qubits (in the blue box) generates the ansatz state for the MBVQE $^{10}$ . Figure 4b shows the 2D cluster state for the computation. The first three qubits are ancilla bits to embed the parameters into the quantum state by parameterized measurements, and the last four qubits are work qubits to conserve the generated ground state. Let  $m_{i}$  denote the measurement outcome of the qubit  $Q_{i}$ . After preparing the 1D cluster state on the first four qubits and measuring in basis  $(1 / \sqrt{2})\{|0\rangle \pm \mathrm{e}^{\mathrm{i}\theta_{k}}|1\rangle \}$  for  $k\in \{1,2,3\}$ , the current state in the fourth qubit is equal to

$$
\begin{array}{l} \left| \psi_ {1} \right\rangle = H Z ^ {m _ {3}} R _ {Z} \left(\theta_ {3}\right) H Z ^ {m _ {2}} R _ {Z} \left(\theta_ {2}\right) H Z ^ {m _ {1}} R _ {Z} \left(\theta_ {1}\right) | + \rangle \tag {21} \\ = X ^ {m _ {3}} Z ^ {m _ {2}} X ^ {m _ {1}} R _ {\chi} ((- 1) ^ {m _ {2}} \theta_ {3}) R _ {Z} ((- 1) ^ {m _ {1}} \theta_ {2}) R _ {\chi} (\theta_ {1} | 0 \rangle \\ \end{array}
$$

where the first equation holds because of the previous knowledge of the MBQC (Supplementary Information) and the second equation holds because  $\sigma_{j}R_{\sigma_{i}}(\theta)\sigma_{j} = R_{\sigma_{i}}(-\theta)$ , where  $i\neq j,i,j\in \{1,2,3\}$  and

$\sigma_{1} = X, \sigma_{2} = Y, \sigma_{3} = Z$ . For the convenience of the expression, here we let indices  $1, 2, 3, 4$  denote qubit  $Q_{4}, Q_{5}, Q_{6}, Q_{7}$  in Fig. 4b, respectively. After performing CZ gates on the last four qubits, the output ansatz state is equal to

$$
\begin{array}{l} \left| \psi_ {0} \right\rangle = \mathrm {C Z} _ {1, 2} \mathrm {C Z} _ {1, 3} \mathrm {C Z} _ {1, 4} \left| \psi_ {1} \right\rangle + + + \rangle \tag {22} \\ = P _ {0} C Z _ {1, 2} C Z _ {1, 3} C Z _ {1, 4} R _ {X 1} \left(\phi_ {3}\right) R _ {Z 1} \left(\phi_ {2}\right) R _ {X 1} \left(\phi_ {1}\right) | O \rangle | + + + \rangle \\ \end{array}
$$

where  $P_{0} = (-1)^{m_{1}m_{2}}X_{1}^{m_{1} + m_{3}}Z_{1}^{m_{2}}Z_{2}^{m_{1} + m_{3}}Z_{3}^{m_{1} + m_{3}}Z_{4}^{m_{1} + m_{3}},\phi_{3} = (-1)^{m_{2}}\theta_{3},\phi_{2} = (-1)^{m_{1}}\theta_{2},\phi_{1} = \theta_{1}$ . The second equation holds because the CZ transformation of  $X$  gate is equal to  $CZ_{1,k}X_1CZ_{1,k} = X_1Z_k$ . Our expected ansatz state for the parameterized Hamiltonian  $\mathbf{H}(\lambda)$  is equal to

$$
\begin{array}{l} \left| \psi_ {\phi} \right\rangle = \mathrm {C N O T} _ {\mathrm {I}, 2} \mathrm {C N O T} _ {\mathrm {I}, 3} \mathrm {C N O T} _ {\mathrm {I}, 4} R _ {X 1} \left(\phi_ {3}\right) R _ {Z 1} \left(\phi_ {2}\right) R _ {X 1} \left(\phi_ {1}\right) | 0 \rangle | 0 0 0 \rangle (23) \\ = H _ {2} H _ {3} H _ {4} \mathrm {C Z} _ {1, 2} \mathrm {C Z} _ {1, 3} \mathrm {C Z} _ {1, 4} R _ {\chi 1} \left(\phi_ {3}\right) R _ {\chi 1} \left(\phi_ {2}\right) R _ {\chi 1} \left(\phi_ {1}\right) | O \rangle + + + \rangle (24) \\ = H _ {2} H _ {3} H _ {4} P _ {\mathrm {o}} ^ {\dagger} \left| \psi_ {o} \right\rangle . (25) \\ \end{array}
$$

Let  $\rho_{\phi} = |\psi_{\phi}\rangle \langle \psi_{\phi}|$  and  $\rho_0 = |\psi_0\rangle \langle \psi_0|$ . We would like to find the ground state of  $\mathbf{H}(\lambda) = -\mathbf{H}_0 - \mathbf{H}_{\mathrm{p}}(\lambda)$  by minimizing  $\operatorname{tr}(\rho_{\phi}\mathbf{H}(\lambda))$ , where  $\mathbf{H}(\lambda)$  is defined in equation (20). Then our goal is to

$$
\min  _ {\phi} \langle \psi_ {\phi} | \mathbf {H} (\lambda) | \psi_ {\phi} \rangle = \min  _ {\phi} \langle \psi_ {o} | \mathbf {H} _ {a} (\lambda) | \psi_ {o} \rangle , \tag {26}
$$

where  $\mathbf{H}_{\mathrm{a}}(\lambda) = P_{\mathrm{o}}H_{2}H_{3}H_{4}\mathbf{H}(\lambda)H_{2}H_{3}H_{4}P_{\mathrm{o}}^{\dagger}$ . With careful simplification, we have

$$
- \mathbf {H} _ {\mathrm {a}} (\lambda) = (- 1) ^ {m _ {2}} X _ {1} Z _ {2} Z _ {3} Z _ {4} + Z _ {1} X _ {2} + X _ {2} X _ {3} + X _ {3} X _ {4} + (- 1) ^ {(m _ {1} \oplus m _ {3})} \lambda Z _ {1}.
$$

Therefore, after optimization, we get the optimized state  $\rho^{*} =$  arg min  $\operatorname {tr}(\rho_0\mathbf{H}_a(\lambda))$  and the ground state  $\rho (\lambda) = U_0\rho_0^* U_0^\dagger$  , where  $U_{0}^{\rho} =$ $H_{2}H_{3}H_{4}P_{0}^{\dagger}$  as defined in equation (25).

Order parameter  $Z_{1}$ . Now we calculate the order parameter  $Z_{1}$  for different  $\lambda$  values—that is, calculate  $\operatorname{tr}(\rho_{\phi}Z_{1})$  by leveraging the optimized output state  $\rho_{0}^{*}$ . Note that

$$
\operatorname {t r} \left(\rho_ {\phi} Z _ {1}\right) = \operatorname {t r} \left(U _ {\mathrm {o}} \rho_ {\mathrm {o}} U _ {\mathrm {o}} ^ {\dagger} Z _ {1}\right) = \operatorname {t r} \left(\rho_ {\mathrm {o}} U _ {\mathrm {o}} ^ {\dagger} Z _ {1} U _ {\mathrm {o}}\right) \tag {27}
$$

where  $U_{0} = H_{2}H_{3}H_{4}P_{0}^{\dagger}$ . As we have already generated the optimized state  $\rho_{0}^{*}$  and the ground state  $\rho(\lambda) = U_{0}\rho_{0}^{*}U_{0}^{\dagger}$ , we need to calculate only  $\operatorname{tr}(\rho_{0}^{*}P_{0})$  where  $P_{0} = U_{0}^{\dagger}Z_{1}U_{0} = (-1)^{m_{1} + m_{3}}Z_{1}$ . This can be approximated with measurement  $Z_{1}$  on the optimized parameterized state  $\rho_{o}^{*}$ .

Experimental procedure. In this section, we provide the MBVQE procedure that connects the quantum device and the classic computer.

After optimizing the performance of our quantum processor, we select seven qubits to conduct the MBVQE experiment. The system parameters for the seven qubits are listed in Extended Data Fig.3c.

The target of the MBVQE experiment is to solve the ground state of  $\mathbf{H}(\lambda) = -\mathbf{H}_0 - \mathbf{H}_{\mathrm{p}}(\lambda)$ . When  $\lambda = 0$ , the Greenberger-Horne-Zeilinger states are the ground state of  $-\mathbf{H}_0$ . Because of the tiny step of  $\lambda$ , we minimize the energy estimation started from the experimental results of the last  $\mathbf{H}(\lambda)$ . Here are the specific experimental procedures.

First, we need a sub-procedure to generate an estimation of  $\operatorname{tr}(\rho_{\Phi}\mathbf{H}(\lambda))$  for the given  $\Phi$  and  $\lambda$ . In this sub-procedure, we calculate the expectation of  $\mathbf{H}(\lambda)$  on a given parameterized state associated with angle  $\Phi = (\phi_1,\phi_2,\phi_3)$ . The sub-procedure is as follows:

(1) For the given parameterized angle  $\Phi = (\phi_1, \phi_2, \phi_3)$  and  $\lambda$ , we ran the MBQC circuits with the four parameter sets  $\pmb{\theta} = (\phi_1, \pm \phi_2, \pm \phi_3)$ . For each parameter set, two observables  $XZZZ$  and  $ZXXX$  were measured. Each measurement is repeated  $T = 1 \times 10^4$  times.

(2) With the single-shot measurements, we selected the data according to the ancilla qubits measurements and estimated  $\mathrm{tr}(\rho_{\Phi}\mathbf{H}(\lambda))$  on the parameterized state with a classic computer. The energy was then estimated with the post-selected data.

The whole MBVQE procedure is as follows:

(1) We initialize the parameterized angle for  $\lambda = 0$  as  $\phi_0 = (\pi /2,\pi /2,\pi /2)$  
(2) We uniformly randomly select 10 groups of parameters around the optimized  $\Phi$  obtained in the previous step ( $\Phi = \phi_0$  for  $\lambda = 0$ ).  
(3) The VQE algorithm applies the L-BFGS-B algorithm $^{34}$  to an optimized  $\Phi$  with local minimum  $\operatorname{tr}(\rho_{\Phi} \mathbf{H}(\lambda))$ .  
(4) After the optimization, we ran the sub-procedure with the eventually optimized parameter sets  $\theta = (\phi_1, \pm \phi_2, \pm \phi_3)$  and  $\lambda$  to approximate the ground-state energy. We then measured the parameterized ground state with measurement  $Z_1$  and repeated this measurement  $T = 2 \times 10^4$  times and post-selected the data to extract the order parameter  $Z_1$ .  
(5) For each  $\lambda$  ranging from 0 to 4.5 with step as 0.5, we repeat steps 2-4.

In Extended Data Fig. 5, we show the whole process for the optimization of different  $\lambda$ , which are shown in different colours. The error analysis of the energy and order parameter values can be found in the Supplementary Information.

Simulation results. The output state in quantum devices is not perfect because of the noise of gates and measurements. Let  $\hat{\rho}$  denote the noisy quantum implementation of  $\rho$ . We give the numerical simulation to show the influence of gate noise and measurements on the approximation of ground state energy and order parameter  $Z_{1}$ . The simulation is done using Qiskit<sup>35</sup>.

Here we compare the simulation results for the MBVQE procedure and show the influence of the gate noise and measurement noise ( $Q_{1}$ ,  $Q_{2}$  and  $Q_{3}$  in Fig. 4b) on the ground-state energy and order parameter  $Z_{1}$ . Extended Data Fig. 6 shows the simulation of the MBVQE algorithm to calculate the ground-state energy and order parameter  $Z_{1}$  under different error models. The simulation results in Extended Data Fig. 6 show that the main origin of the deviation is the measurement noise of the first three measurements and the error of the work qubit can be fully removed by the error mitigation method in the 'Qubit independent noise' section (Supplementary Information). The details of the analysis of the error bar for the estimation are given in the Supplementary Information.

# Data availability

The data shown in this paper are available from the corresponding authors upon reasonable request.

# Code availability

The code for this paper is available from the corresponding authors upon reasonable request.

32. Yan, Z. et al. Strongly correlated quantum walks with a 12-qubit superconducting processor. Science 364, 753-756 (2019).  
33. Bravyi, S., Sheldon, S., Kandala, A., Mckay, D. C. & Gambetta, J. M. Mitigating measurement errors in multiqubit experiments. Phys. Rev. A 103, 042605 (2021).  
34. Zhu, C., Byrd, R. H., Lu, P. & Nocedal, J. Algorithm 778: L-BFGS-B: Fortran subroutines for large-scale bound-constrained optimization. ACM Trans. Math. Softw. 23, 550-560 (1997).  
35. Aleksandrowicz, G. et al. Qiskit: an open-source framework for quantum computing (0.7.2). Zenodo https://doi.org/10.5281/zenodo.2562111 (2019).

Acknowledgements We thank the USTC Center for Micro- and Nanoscale Research and Fabrication for supporting the sample fabrication and the QuantumCTek for supporting the fabrication and maintenance of room-temperature electronics. This research was supported by the Innovation Program for Quantum Science and Technology (grant no. 2021ZD0300200), Shanghai Municipal Science and Technology Major Project (grant no. 2019SHZDX01),

# Article

Anhui Initiative in Quantum Information Technologies and the Chinese Academy of Sciences. H.R. acknowledges support from Natural Science Foundation of Shandong Province (grant no. ZR202209080019). H.-L.H. acknowledges support from the Youth Talent Lifting Project (grant no. 2020-JCJQ-QT-030), National Natural Science Foundation of China (grant nos 12274464 and 11905294), China Postdoctoral Science Foundation and the Open Research Fund from State Key Laboratory of High Performance Computing of China (grant no. 201901-01). M.G. was supported by Shanghai Rising-Star Program (grant no. 23QA1410000) and the Youth Innovation Promotion Association of CAS (grant no. 2022460). X.Y. acknowledges support from the National Natural Science Foundation of China (no. 12175003) and the High-Performance Computing Platform of Peking University.

Author contributions X.Z. and J.-W.P. conceived the research. X.Y., B.W., M.G., F.C., S.C., H.-L.H. and C.-Y.L. designed the experiment. S.C., F.C., S.G., H.Q., Y.W. and M.G. performed the measurements. X.Y., B.W., F.C., S.C. and M.G. analysed the results. Q.Z., Y.Y., C.Y., F.C. and S.L. designed the processor. S.C., Y.L., K.Z., S.G., H.Q., T.-H.C., H.R., H.D. and Y.-H.H. fabricated the

processor. M.G., S.W., C.Z., Y.Z., S.L., C.Y., J.Y., D.F., D.W. and H.S. contributed to the construction of the ultracold and low-noise measurement system. J.L., Y.K., F.L., C.G., L.S., N.L. and C.-Z.P. developed the room-temperature electronics. All authors contributed to the discussion of the results and drafting of the manuscript. X.Z. and J.-W.P. supervised the whole project.

Competing interests The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41586-023-06195-1.

Correspondence and requests for materials should be addressed to Xiao Yuan, Xiaobo Zhu or Jian-Wei Pan.

Peer review information Nature thanks Otfried Gühne and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available.

Reprints and permissions information is available at http://www.nature.com/reprints.

![](images/9f8a582cf9c325be6af03527efdccc6b01c021129afcae41d80416f99020bfa9.jpg)  
a

Extended Data Fig.1| The correction of coupler flux pulse distortion.  
b  
![](images/9d30f81521c1974b28c93fb09ee4eb0feaddf054a8d402a8935b33eb61a68e53.jpg)  
a. The waveform sequences are used to measure the effect of distortion.  
We apply a square wave pulse to the coupler, after a variable delay time, and  
measure the phase of the qubit using the Ramsey experiment. b. Qubit phase as  
a function of the delay time, with and without distortion corrections.

![](images/c0b250b8ad93f15bcda6b76a64426940ff17ccd1f9735813f74bacb93fa51774.jpg)

![](images/470b40130355224500a508ca7c2fa2157ca06ab616a4ee2114934e34f3f803d7.jpg)  
Extended Data Fig. 2 | Parallel CZ gates optimization process. a. The state leakage to |20> with a CZ gate. b. The conditional phase of a CZ gate. c. The cost function for initial value selection. The red point is the value chosen for the

![](images/d94f74a23a00e68700ab5d8e60d8aea941c1c7e05dab0b72c7ba299d12765ff2.jpg)

![](images/9e3746230d907b60a5018d9ac45d78e93282820a765a3ded75b6c5888ffad6a1.jpg)  
next optimization. d. The SPB sequence fidelity of the random circuit instances at different interaction frequencies. The magenta line represents the qubit's current detuning. All these optimization procedures can be realized in parallel.

![](images/989c523f3c2c47efcc69326294526e77326d3599c1702d6efc456edf85c660e5.jpg)  
a

![](images/4c06e9c368bac36fe92df09cf85e53785a5997c1cdd043ab05c08a723ab60774.jpg)

![](images/67da94a958b392f60e680e2c20d64adf7a936ec8ef83f91c9db522b14b7bc352.jpg)

![](images/f4cca944253da69951ef074fdf0248c9e97a4f2181e1027106ec1dfc9c4b8325.jpg)  
b

![](images/215de41ebbcc39eef10d4d9c9ca89651b609fae2eaf4a50cc5ed89f5f66ee868.jpg)

![](images/d7bc1f3656c3868fffbac31906bca52a2c8fbcd4c2c78409c00cebc1410acc5b.jpg)

![](images/00ca2296078b9cb80e24d729748f3d622d33db673f71459732c0802f93174954.jpg)  
C

![](images/807e126c0e9a42c474ad72708a3771e0e1124e5d6f4dcab2be612008d301c5cd.jpg)  
Extended Data Fig. 3 | The performance of the quantum processor after calibration. a. The single-qubit gate, readout, and CZ gate error for the generation of 1D cluster state. b. The single-qubit gate, readout, and CZ gate

![](images/3b46f140d915f78d42f18bceb3026f8c63c3ae79f546ddd80fce4c0c16923bd6.jpg)  
error for the generation of the 2D cluster state. c. The single-qubit gate, readout, and CZ gate error for the experiment of MBVQE.

![](images/26026c5837d4e789c389438c835663f409d0b3269b90d691ca1d8222648af3a9.jpg)  
a

![](images/864213f2c1bc543aaa7f8fb6fbd317fb11e90f126d804f6b8510ae524e5a4d89.jpg)

![](images/055140b1f41fd5e454020caa2591fad4d15c111e0e77f47168d4246faac38f01.jpg)  
Extended Data Fig. 4 | Correlations of qubit pairs for all of the flip errors. a. The covariance of all of the flip errors of the qubit pairs having the same device as 51-qubit 1D cluster state. b. The covariance of all of the flip errors of

![](images/889cfdc0ff184fbd957118f039afdcda498edffea1c4f0edeb9b783dffb9382d.jpg)

![](images/a691a5b4ea55784007548645c65447e051b93e2e66536f57d2180c682f06a3ca.jpg)  
b

![](images/32d1ff282703e9156c7eeb1d9b2fac61050e77dfe15b1d576e4a52613a5a497b.jpg)

![](images/ba118202ca367a6a64a953bcbe294e27d3e41e713f7366c9a21782cf90a64681.jpg)  
the qubit pairs having the same device as 30-qubit 2D cluster state, where  $ij \rightarrow \bar{ij}$  denotes the covariance of two qubits with input state  $|ij\rangle$  and output state  $|(1 - i)(1 - j)\rangle$ .

![](images/7da703e2431e0d0085ef80eca8b20c627d43bb4427a0533f5ae4d11b9bc923d0.jpg)

![](images/6c0c65de5aa7bdc5931c81ec8747a1ed8882fa61ba9d0ce337d308f59a28795f.jpg)  
Extended Data Fig. 5 | The whole iteration process of energy estimation. Different colors represent different  $\lambda$  values. The first 10 points in every lambda regime are random ancillary states and the last point is the final state.

![](images/6e63f25422bc9ebfa0d907ee0532534c88f7bb9d2baab854012f449bbe7205e3.jpg)  
a

![](images/641d44909fadc493421a85b56da7f10e3997c9eaf8abe7a81ef20e9b75d63c05.jpg)  
Extended Data Fig. 6 | Simulation of the MBVQE algorithm under different error models. (a) Ground state energy estimation and (b) Order parameter  $Z_{1}$ . 'Simulated_0' denotes the ideal case where no error happens; 'Simulated_1' denotes the simulation with gate error to be depolarizing error, where error rate equals 0.002/0.01 for single/two-qubit gates; 'Simulated_2' denotes the simulation with depolarizing error (same error as Simulated_1) and  
b  
measurement noise where error rate equals 0.05 for the first three ancillas qubits; 'Simulated' denotes the simulation with all of the errors in 'Simulated_2' and additional measurement noise for the rest four qubits. As a benchmark, we also plot the theoretical value for ground state energy, the first excited state energy, and the order parameter  $Z_{1}$ . The simulation result leverage 20,000 repetitions of measurements for each circuit and measurement setting.