# ARTICLE OPEN

Check for updates

# Quantum Fredkin and Toffoli gates on a versatile programmable silicon photonic chip

Yuan Li $^{1}$ , Lingxiao Wan $^{1}$ , Hui Zhang $^{1}$ , Huihui Zhu $^{1}$ , Yuzhi Shi $^{2}$ , Lip Ket Chin $^{3}$ , Xiaqi Zhou $^{4\boxtimes}$ , Leong Chuan Kwek $^{1,5,6\boxtimes}$  and Ai Qun Liu $^{1\boxtimes}$

Quantum logic gates are backbones of quantum information processing (QIP), wherein the typical three-qubit Fredkin and Toffoli gates are essential in quantum computation and communication. So far, the quantum Fredkin gate has only been demonstrated with pre-entangled input states in free-space optics, which limits its usage for independent input photons. Here, we put forward an exquisite scheme and experimentally perform a proof-of-principle demonstration of three-qubit Fredkin and Toffoli gates on a programmable quantum photonic chip. Our scheme can also be used to realize a series of other two-qubit quantum gates. Our work sheds light on the merits of quantum photonic chip in implementing quantum logic gates, and paves the way for advanced quantum chip processors.

npj Quantum Information (2022)8:112; https://doi.org/10.1038/s41534-022-00627-y

# INTRODUCTION

Quantum computation<sup>1</sup> is one of the great challenges in quantum information processing, while it enables the exponential speedup of computations and solves numerous NP-hard problems which cannot be effectively tackled by the classical computing<sup>2,3</sup>. Recently, extensive attention has been raised in realizing large-scale universal quantum computing with instinctive systems including superconducting qubits<sup>4</sup>, linear optics<sup>5</sup>, atoms<sup>6</sup> and NMR qubits<sup>7</sup>. Quantum logic gates acting as key components of quantum circuits are essential for quantum computation. However, the efficient realization of more qubits quantum logic gates still remains a significant challenge due to the difficulty in chaining various gates together in a circuit, e.g., the three-qubit Toffoli gate requires six CNOT gates<sup>8</sup>, while the Fredkin gate corresponds to a more difficult decomposition. Some ingenious methods of realizing three-qubit Toffoli and Fredkin gates have been experimentally demonstrated with large-scale bulk optics systems<sup>9,10</sup>. By expanding the qubit space to a higher dimensional Hilbert space, Lanyon et al. exhibited the realization of Toffoli gate with a photonic system<sup>9</sup>. A quantum Fredkin gate acting on photons is experimentally demonstrated with the pre-entangled input states, which cannot act as an independent gate device<sup>10</sup>. The inherent limited programmability, less scalability and instability of bulky optical gates restrict their wide deployment.

Nowadays, the burgeoning development of integrated photonic circuits has manifested themselves as paradigms for large-scale quantum computation due to the precise programming of the large-scale circuit $^{5,11-17}$ . In this paper, we propose a scheme to construct the quantum logic gates and fabricate a programmable silicon-based photonic chip for realizing a diversity of quantum logic gates, such as three-qubit quantum Fredkin and Toffoli gates. Instead of decomposing a multi-qubit gate into the basic single-qubit gates and two-qubit CNOT gates, the independent encoded photons pass through an optical circuit that implements

a specific (usually non-unitary) transformation correspond to the desired quantum logic gate, which is programmed by controlling phases of each Mach-Zehnder interferometer (MZI). We then perform post-selective measurements on the output photons to directly implement the multi-qubit gate. Moreover, our method can be extended to realize large-scale  $n$ -qubit Toffoli gate<sup>18</sup>. The diverse quantum logic gates implemented in a single photonic integrated chip will facilitate the development of future quantum processors, and endow a great number of potential applications.

# RESULTS

# Theoretical framework

A holistic scheme is presented to implement an  $n$ -qubit quantum gate with  $n$  photons and a  $2n \times 2n$  linear optical network. For simplicity, we choose a three-qubit quantum logic gate as an example. The functionality of the three-qubit gate can be described by a  $2^3 \times 2^3$  matrix  $\left[\left[X_{ij}\right]\right]$  which determines the relations between eight input and output states in the computational basis, e.g.,  $\left|000\right\rangle_{in} \rightarrow X_{11}\left|000\right\rangle_{out} + X_{12}\left|001\right\rangle_{out} + \ldots + X_{18}\left|111\right\rangle_{out}$ . Here, we consider a  $6 \times 6$  nonunitary circuit  $\left[Y_{ij}\right]$  with three input photons encoded in two adjacent modes labelled as  $(a_0, a_1)$ ,  $(b_0, b_1)$ ,  $(c_0, c_1)$  as shown in Fig. 1. For each three-qubit input state in eight computational states, the amplitude of the corresponding eight output state is the permanent of  $Y_S$  due to the indistinguishability of bosons, where  $Y_S$  is the  $3 \times 3$  submatrix of  $\left[Y_{ij}\right]$ , corresponding to the input and output states[19,20] (See Supplementary Note 1.2 for details of constructing  $\left[Y_{ij}\right]$ ). By calculating the appropriate matrix  $Y_{Fre}$  and  $Y_{Tof}$  (see Fig. 1), we can obtain the amplitude matrices for the input-output relation which are exactly the desired  $\left[\left[X_{ij}\right]\right]$  of quantum Fredkin gate and Toffoli gate. Since all evolutions of the photons via passing the optical circuit are coherent, our constructed gate also works well for arbitrary input three-qubit state with density matrix  $\rho_{in} = \sum_{ij} \rho_{ij}|i\rangle \langle j|$ , where

![](images/908fbb5ef99d45134103be074c46e24081af05d949f8db8f79e55095c421f830.jpg)

![](images/729e0614b0ceb532a56409c851f1b49273b4d3246285f5eaa0e12251814286b0.jpg)

![](images/2eb16d0039f38b046d0ef97bd365eda9f701d3962445f62f510785efc5314d69.jpg)

![](images/2a67ff564ebf28ecab290831582228dcc039655108d470decd6f75e2cf096ae0.jpg)  
Fig. 1 Scheme of constructing three-qubit quantum logic gates. Three independent photons encoded in  $(a_0, a_1), (b_0, b_1), (c_0, c_1)$  pass through a  $6 \times 6$  photonic circuit described by a nonunitary matrix  $[Y_{ij}]$ , the output distribution of the three-photon coincidence counts at each port is determined by the permanent of the  $3 \times 3$  submatrix  $Y_S$  defined as  $\mathrm{Per}(Y_S)$ . By calculating the appropriate nonunitary matrix  $Y_{Fre}$  and  $Y_{Tof}$  for the photonic circuit  $[Y_{ij}]$ , the output amplitude is exactly the matrix  $[[X_{ij}]]$  of the Fredkin gate and Toffoli gate respectively which infers the implementation of the three-qubit logic gates. Other quantum logic gates can also be reconstructed with the same method by adjusting the nonunitary matrix  $[Y_{ij}]$ .

![](images/ebf48ca6243f9f2cc96ca24d6f17f7cd8b8e0fbf40c264b09f77f285316748a8.jpg)

$|i\rangle, |j\rangle = |000\rangle, |001\rangle, \ldots, |111\rangle$  and  $\rho_{ij}$  is the element of density matrix in computational basis.

$\left[Y_{ij}\right]$  is usually a nonunitary matrix which cannot be realized experimentally by Reck's decomposition scheme directly<sup>21</sup>. By performing the Singular Value Decomposition (SVD) of matrix  $\left[Y_{ij}\right]$ , we obtain:

$$
Y = U \Sigma V ^ {\dagger}, \tag {1}
$$

where  $U$  and  $V^{\dagger}$  are unitary matrices which can be realized directly $^{21,22}$ .  $\Sigma = diag(\gamma_{1},\gamma_{2},\dots,\gamma_{6})$  ( $\gamma_{1} \geq \gamma_{2} \geq \dots \geq \gamma_{6} \geq 0$ ) is the diagonal matrix and  $\gamma_{1}$  is the largest eigenvalue. Usually, the matrix  $\Sigma$  cannot be realized experimentally due to  $\gamma_{1} > 1$ . We then define  $\Sigma_{Att} = \Sigma /\gamma_{1} = diag(1,\gamma_{2} / \gamma_{1},\dots,\gamma_{6} / \gamma_{1})$ , which means that different attenuations are added for the six paths. By connecting the three unitary matrices in order, we can experimentally realize the attenuated matrix as

$$
[ Y ] _ {A t t} = \frac {Y}{Y _ {1}} = U \Sigma_ {A t t} V ^ {\dagger}, \tag {2}
$$

where  $1 / \gamma_1^6$  is the experimental success probability of the three-qubit quantum gate. For the calculated matrices show in Fig. 1 for Fredkin gate and Toffoli gate, we obtained a success probability of 0.056 for the Fredkin gate and 0.017 for the Toffoli gate. The success probability of the Toffoli gate is higher than 1/72 (0.014) achieved in the previous experiment<sup>9</sup>.

Besides the three-qubit Toffoli and Fredkin gates, our scheme can also be potentially used to implement quantum gates with more qubits such as the  $n$ -qubit Toffoli gates  $(n > 3)$  (see Supplementary Note 3). An even more interesting point is that our scheme can also be used to realize a heralded Toffoli gate with ancillary photons (see Supplementary Note 4 for details). Using the multiplexing approach[23], the success probability of such heralded Toffoli gate can be boosted to near-deterministic level, thus making it potentially promising for future applications in scalable optical quantum circuits.

# Experimental setup

A series of quantum logic gates including a three-qubit Fredkin gate, a three-qubit Toffoli gate, and other two-qubit quantum gates are implemented in a silicon quantum photonic chip as shown in Fig. 2. A pump laser beam containing central wavelengths of  $1546.8\mathrm{nm}$  and  $1553.2\mathrm{nm}$  (See Methods and Supplementary Note 1.1 for details) is fed into the photonic chip which mainly consists of two parts: (i) the generation of degenerated photonic source pair and (ii)-(iv) the photonic circuit for realizing the quantum logic gate.

Generation of degenerated photonic source pair. After entering into the part (i) of the chip, the pump light is divided into four paths with equal intensity by three MZIs (each consisting of two multi-mode interferometers and two phase shifters  $\theta$  and  $\phi$ , see the inset of Fig. 2a). Each pump beam passes through a silicon waveguide spiral to generate the degenerated squeezed light source simultaneously through the spontaneous four wave mixing (SFWM) process. The residual pump pulse is filtered by two asymmetric MZIs (AMZIs), and the remaining parametric photons at  $1550~\mathrm{nm}$  are in the N00N state  $|\psi\rangle = 1 / \sqrt{2}(|20\rangle + |02\rangle)$  when only one pair photon term is considered. Here, we tested the two-photon N00N state[24] by interfering them by a 50:50 beam splitter with an adjustable phase of  $\theta$ . The coincidence counts are measured at two outputs with a visibility of  $0.909 \pm 0.004$ , see the inset of Fig. 2a. When  $\theta = \pi/2$ , the output photon pair state  $|\psi\rangle = |11\rangle$  is generated. Two such pair sources are pumped out with the same input intensity and labelled as a, b and c, d when realizing the three-qubit gate. We then measure the Hong-Ou-Mandel (HOM) interference between the two photon pair sources and obtained a visibility of  $V_{HOM} = 0.82 \pm 0.05$  at a coincidence count of  $\sim 3000\mathrm{Hz}$  for both two photon pairs. The HOM interference visibility is calculated as:  $V_{HOM} = (C_{\max} - C_{\min}) / (C_{\max} + C_{\min})$  where  $C_{\max}$  and  $C_{\min}$  are the peak and dip four-photon coincidence counts.

The photonic circuit for realizing the quantum logic gate. The d photon is sent to the detector as a trigger signal, and the other three photons are sent to the circuit with three parts: (ii) the

![](images/d494ecc72c4997cdd240297777ce76c63d6d7afd49aa0f8c93568f4cdea58031.jpg)

![](images/96e654db6b28436a362246e2b3670519f2a87e22793b9b02d32c7ca04a21fa4d.jpg)  
Fig. 2 Experimental realization of quantum logic gates. a A dual-wavelength pump beam is injected into the photonic chip composed of four parts: (i) the generation of two pairs of degenerated photons labelled as a, b and c, d via the interference of the N00N state; (ii) the preparation of initial states; (iii) the photonic circuit to realize the  $6 \times 6$  nonunitary matrix  $\left[Y_{ij}\right]$  by the SVD decomposition into three unitary matrices  $V^{\dagger}$ ,  $\Sigma_{Att}$  and  $U$ ; (iv) the measurement part at different bases. The photons at the outputs are coupled into fibers and detected by SNSPDs. SNSPD: superconducting nanowire single-photon detector. Inset: The left subpicture is the results of the N00N state. At the angle  $\theta = \pi / 2$ , the maximum coincidence counts mean one photon pair is generated at port a, b. The right subpicture is the construction of an MZI on chip which is composed of two multi-mode interferometers (MMIs) and two phase shifters. b The optical micrograph of the whole chip. In our chip, the  $6 \times 3$  nonunitary matrix is divided into three parts:  $V^{\dagger}$ , the attenuation and  $U^{\prime}$ .  $V^{\dagger}$  is a  $3 \times 3$  unitary matrix, thus only two attenuations should be inserted in path 2 and 3 which are labelled as Att $_2$  and Att $_3$ . The attenuated photons are leaked out of the chip shown as leak $_2$  and leak $_3$ . The red box represents the main parts (i)-(iv) in our experiment.

preparation stage, (iii) the SVD decomposition stage and (iv) the tomography stage. For the state preparation, three MZIs are linked to encode the photons  $\mathbf{a}$ ,  $\mathbf{b}$  and  $\mathbf{c}$  into dual-rail qubit, which are denoted as  $(a_0,a_1)$ ,  $(b_0,b_1)$  and  $(c_0,c_1)$ . Subsequently, they are injected into the  $6\times 6$  non-unitary matrix composed of two  $6\times 6$  unitary matrices  $V^{\dagger}$  and  $U$ , which are both composed of 15 MZIs and a total of 36 thermo-optic phase shifters[22]. The connected attenuation matrix  $\Sigma_{Att}$  is composed of 6 MZIs. While in our experiment for the proof-of-principle demonstrating the quantum gate, our fabricated photonic chip is not large enough to realize a  $6\times 6$  nonunitary matrix. But luckily, we can construct a  $6\times 3$  nonunitary matrix which combines the state preparation and measurement parts for each encoded input state of a three-qubit gate. It can be used to proof-of-principle demonstrate the three-qubit gate since the evolution for each input to output is determined by the  $6\times 3$  submatrix (See Supplementary Note 1. 3 for details). The  $6\times 3$  nonunitary matrix can be decomposed into the matrices  $3\times 3$  unitary matrix  $V^{\prime \dagger}$  and  $6\times 6$  unitary matrix  $U^{\prime}$  by the SVD decomposition which are experimentally realized in our photonic chip (Fig. 2b). The three photons are fed into the superconducting nanowire single-photon detectors (SNSPDs) for the fourfold coincidence measurement.

# Results for three-qubit gates

In quantum information processing, Fredkin gate and Toffoli gate are the most commonly used three-qubit gates. The Fredkin gate is the controlled-swap gate which means the qubit states of the two target qubits  $(T_{1},T_{2})$  are swapped when the control qubit  $(C)$  is  $|1\rangle$ . While the Toffoli gate is the controlled-controlled-NOT gate where the target qubit  $(T)$  is flipped when the two control bits  $(C_{1},C_{2})$  are both  $|1\rangle$ . These two logic gates are fundamental components of universal reversible computation and have a great

usage in quantum error correction, thus playing important roles in the quantum network $^{25-28}$ . In order to realize these two three-qubit gates separately, we calculate the non-unitary matrices  $\left[Y_{ij}\right]$  for both Fredkin gate  $Y_{Fre}$  and Toffoli gate  $Y_{Tof}$  as shown in Fig. 1. In the experiment, the detected four-fold coincidence counts were averaged  $\sim 3$  per hour for the Fredkin gate and  $\sim 1$  per hour for the Toffoli gate, and we measured about 100 events for each input basis. Although such low count rates are not sufficient to perform a full process tomography of the prepared three-qubit gate within a reasonable time frame, they are sufficient to verify whether the prepared gate can fulfil the core functions of the three-qubit gate.

First, we verify whether it can achieve the classical behavior of Fredkin and Toffoli gates, i.e., whether it can convert all eight logical input states into the correct eight logical output states in the computational basis. Mathematically, the fidelity  $F_Z = \mathrm{Tr}(M_{ideal}.M_{exp}) / \mathrm{Tr}(M_{ideal}.M_{ideal})$  is calculated to quantify the overlap between two truth tables, where  $M_{ideal}$  is the ideal truth table and  $M_{exp}$  is the experimental one. Figure 3a, b show the experimental results for constructed Fredkin gate and Toffoli gate with a fidelity of  $0.75 \pm 0.02$  and  $0.79 \pm 0.03$ , respectively, which reflects the performance of the classic action of our prepared three-qubit gates.

Then, we verify the quantum behaviour of the prepared three-qubit gate, i.e., its ability to operate correctly on the input quantum superposition states. For the Fredkin gate, we choose  $|+,0,1\rangle$  as the input state, where  $|+ \rangle = 1 / \sqrt{2} (|0\rangle + |1\rangle)$  to verify whether the prepared gate can manipulate the input state  $|+,0,1\rangle$  correctly. The reason for verifying the performance of the prepared gate in manipulating the input state  $|+,0,1\rangle$  is the fact that it is one of the most experimentally challenging cases that reflects the core quantum functionality of a Fredkin gate. The challenges originate from that it requires all three qubits to

![](images/4a70ff20298708c0b7b02ef9b71ff3d2a72884098846d1720fa48b0ff5c5dfc2.jpg)  
a

![](images/f805093b9d863b59f053d69abd12d9fc1bfc69c1124e57c0a8b4705ac5ab11b1.jpg)  
b

![](images/9f5271988de00fc1fc53132daedd4ea1d5883d98ac4a66fe23a166fab6d49d4b.jpg)  
C  
Fig. 3 Experimental results for three-qubit logic gates. a and b show truth tables of the constructed Fredkin and Toffoli logic gates, respectively. The  $x$  and  $y$  axes are eight calculation basis for input and output states. c Measured results for determining the fidelity of target qubits for the input state  $|+,0,1\rangle$  of the Fredkin gate.  $|R / L\rangle = (|0\rangle \pm i|1\rangle) / \sqrt{2} \mathbf{d},\mathbf{e}$ . The measured results of control qubit  $C_2$  and target qubit  $T$  for the input state  $|1, + ,0\rangle$  and  $|0, + ,0\rangle$  respectively of the Toffoli gate. All error bars refer to  $\pm 1$  standard deviation estimated from Poissonian photon-counting statistics.

![](images/585f4ce15774204e89d8de3b9145d2c809780009fd0953ca853715da9824d0b0.jpg)  
d

![](images/ccf49fd84214dbc186eb9f62aba65e5a20c4b14f7cfb92f58a6346012612da46.jpg)  
e

interact with each other which could generate a maximally entangled state at output ports. It is functionally important because it verifies the Fredkin gate's ability to generate and control the entanglement, which is a key capability necessary for quantum computing. An ideal Fredkin gate can transform the input state  $|+, 0, 1\rangle$  into a superposition state of  $|001\rangle$  and  $|110\rangle$ . After projecting the control qubit  $C$  to  $|+ \rangle$ , the state of the two target qubits will become the Bell state  $(|01\rangle + |10\rangle) / \sqrt{2}$ , which is a superposition of the original quantum state of the two target qubits  $(|01\rangle)$  and the quantum state of the two target qubits after swapping  $(|10\rangle)$ . The final output of this entangled state of the two target qubits embodies the core function of the Fredkin gate for its controlled-swapping operation. As shown in Fig. 3c, we measured the output state of the two target qubits in ZZ, XX and YY bases whereby Z, X and Y are Pauli operators. The fidelity with respect to the ideal Bell state was calculated as  $F = 0.70 \pm 0.03$ , affirming the performance of the quantum action of our prepared Fredkin gate.

For the Toffoli gate, the input superposition states are chosen as  $|1, +, 0\rangle$  and  $|0, +, 0\rangle$  which theoretically give rise to the output state  $|1\rangle(|00\rangle + |11\rangle) / \sqrt{2}$  and  $|0\rangle(|00\rangle + |10\rangle) / \sqrt{2}$  after passing through the Toffoli gate. A maximum Bell state is generated between  $C_2$  qubit and  $T$  qubit when  $C_1$  is  $|1\rangle$  and a product state when  $C_1$  is  $|0\rangle$  which expresses the functionality of the Toffoli gate, i.e., the target qubit is only flipped when both control qubits are  $|1\rangle$ . Figure 3d shows the results for the entanglement state  $C_2$  qubit and  $T$  qubit with corresponding detection of control qubit  $C_1 = |1\rangle$ . The sampling time of the Toffoli gate is almost two times longer than

that of the Fredkin gate for each basis. Thus, for the entangled state generated by the Toffoli gate, we only measured them in the ZZ and XX bases, whose data are enough to determine the lower bound on the fidelity of the entangled state[29]. The fidelity of the maximum two-qubit Bell state measured can be estimated to be  $F \geq 0.64 \pm 0.04$  which exceeds the entanglement limit 0.5 over 3 standard deviations. Figure 3e shows the coincidence results for the product state measured in the XZ basis with a calculated fidelity of  $F = 0.84 \pm 0.03$ . These results manifest the good functions of qubit Toffoli gate for the superposition state.

# Results for two-qubit gates

In order to realize the two-qubit logic gates, one correlated photon pair source is chosen as the resource which is injected into the  $4 \times 4$  circuit constructed inside the  $6 \times 6$  circuit. Here, we choose the controlled-NOT (CNOT) gate, controlled-Hadamard (CH) gate,  $\sqrt{\mathrm{iSWAP}}$  gate and quantum Fourier transformation (QFT) gate for experimental testing examples. The success postselection probabilities for these gates are calculated to be  $1 / 9, 1 / 9, 0.17, 0.09$ , respectively. Our method achieves the same success probability with previous schemes for realizing the CNOT gate[13,30,31]. The matrix representations of these gates are listed in Supplementary Note 2. The evolution of a two-qubit state  $\rho$  after passing through a quantum logic gate is described by:  $\varepsilon (\rho) = \sum_{m,n=0}^{15} \chi_{mn} E_m \rho E_n^\dagger$ , where  $E_m$  and  $E_n^\dagger$  are Kronecker product of Pauli operators, and  $\chi_{mn}$  is a  $16 \times 16$  matrix which describes the process completely. By choosing the input state from the set

![](images/ec0741bf80b214dd2db19c8dfd2aee46cfb5fe024653a024f997d2fc1610b5dd.jpg)  
a CNOT  $F_{p} = 0.973\pm 0.007$

![](images/c8062ee395ee572eb5c099abd48cfed93aa59cfa31243f2ce50004420fe6bc64.jpg)

![](images/f978b5b9ce559a1d25dee87989d6fafd47426ba7e1e0ae23e9ffcd0b8cdeb1c2.jpg)  
b CH  $F_{p} = 0.873 \pm 0.006$  
C  $\sqrt{\mathrm{iSWAP}} F_{p} = 0.894\pm 0.006$

![](images/4af558d608d3272f343de3ff81dd7a4a0885023013bc1372a0398d9d0fcc9a06.jpg)

![](images/71cba55b5aa7386403b19aae286c90c4fb715413568305026401d275e5955f13.jpg)

![](images/3422e05b7a4e1974bee48cba6c7ec42d6f8b7b4dbdb5724739e272c42b525047.jpg)

![](images/7d028ade5788c1e507217620956a73350cf0f726d053e50179f6f814e3b20934.jpg)  
d QFT  $F_{p} = 0.876\pm 0.008$  
Fig. 4 Experimental results of quantum process tomography for a diversity of two-qubit quantum logic gates. CNOT gate (a), CH gate (b),  $\sqrt{\mathrm{iSWAP}}$  gate (c), QFT gate (d). The left and right parts are the real and imaginary parts of the quantum process tomography matrices. The fidelity errors are calculated with a 1000-times Monto Carlo simulation subjected to Poissonian statistics.

![](images/0169e2ae5bca28d376daef89ab94c0024037e8712b4e3b8dddf6d39261d990c3.jpg)

$\{|0\rangle, |1\rangle, |+ \rangle, |R\rangle\}$  for each qubit, we performed the quantum process tomography (QPT) $^8$  for the constructed gates and obtained  $\chi_{exp}$  matrices and the process fidelity  $F_p = \mathrm{Tr}(\chi_{exp} \chi_{ideal})$ , where  $\chi_{ideal}$  is the ideal  $\chi$  matrix as shown in Fig. 4.

# DISCUSSION

The main noise in our experiment exists in the higher order photon pair emission which becomes distinct at a low collection efficiency and the distinguishability of the photon pair sources.

Considering the high loss in the silicon chip including both the transmission loss and the coupling loss from the chip to the fiber, we can improve the experimental quality of our method by either using low-loss silicon nitride material (5 dB per meter) $^{32}$  or the integration the SNSPD detectors on chip $^{33}$ . In addition, we can combine high efficiency and HOM interference visibility SPDC-based source $^{2,34}$  with the reported ultralow coupling and transmission loss on a silicon nitride chip $^{35}$ , which can greatly increase the collection efficiency and the fidelity. With the precise thermal control $^{36}$  of the programming nonunitary matrix and the improvement of the total efficiency, our method can be extended to the on-chip large-scale implementation of the  $n$ -qubit Toffoli gate. And also, there still left some open questions for future work: whether our method can be used to realize high-dimensional quantum logical gates $^{37}$ .

In conclusion, we have proposed a method to realize quantum logic gates and experimentally demonstrated proof-of-principle the three-qubit Fredkin gate and Toffoli gate with linear optics on chip, as well as a series of typical two qubit gates. The most important merit compared with the previous method to realize a three-qubit Fredkin gate $^{10}$  is that we don't need any pre-existing entanglement. It thus allows the constructed Fredkin gate can work as an independent device, which is more compatible with other optical systems, such as using the high efficiency quantum dot single photon sources as input qubits $^{38,39}$ . Our method will stimulate more efforts in building up manifold quantum circuits by means of integrated technologies, facilitating the development of future quantum processors.

# METHODS

# Experimental setup

A pump laser with a central wavelength of  $1550\mathrm{nm}$  and a pulse width of 2 ps is passed through an optical compressor to broaden its spectral width to  $10\mathrm{nm}$  (see Supplementary Note 1.1 for details). By passing the laser through a wavelength-division multiplexing (WDM) with  $0.8\mathrm{nm}$  channel spacing, two laser beams with central wavelengths of  $1546.8\mathrm{nm}$  and  $1553.2\mathrm{nm}$  are selected and then combined into a single beam by another WDM. A tunable optical delay is inserted between the two WDMs to ensure that the two beams are indistinguishable in time. The combined beam is then coupled into the silicon photonic chip by an optical fiber to generate the desired single photons through SFWM. After transforming through the on-chip optical circuit, the single photons are led out by the fiber array at the output. A WDM (isolation  $>100$  dB, bandwidth  $0.5\mathrm{nm}$ ) is connected to each channel of the fiber array to filter out all unwanted light, thus extracting single photons with a central wavelength of  $1550\mathrm{nm}$  and feeding them into SNSPDs with an average efficiency  $\sim 85\%$  for the detection. Taking into account the waveguide and optical element losses, the waveguide-to-fiber coupling losses, and the single-photon detection efficiency, the resulting single-photon heralding efficiency is  $\sim 3\%$ .

# Fabrication

The source part and photonic circuit are fabricated on the 220 nm-thick silicon-on-insulator (SOI) platform. All phases are thermally adjusted by adding the current at each heater to facilitate the construction of programmable nonunitary matrix to realize the logic gates. The transmission loss of the silicon waveguide is  $\sim 2$  dB per centimeter, and the loss for each Mach-Zehnder interferometer (MZI) is  $\sim 0.3$  dB.

# DATA AVAILABILITY

The data that support the findings of this study are available from the corresponding authors on reasonable request.

# CODE AVAILABILITY

The codes for simulation and data processing are available from the corresponding authors upon reasonable request.

Received: 23 March 2022; Accepted: 25 August 2022

Published online: 15 September 2022

# REFERENCES

1. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
2. Zhong, H. S. et al. Quantum computational advantage using photons. Science 370, 1460 (2020).  
3. Monz, T. et al. Realization of a scalable Shor algorithm. Science 351, 1068-1070 (2016).  
4. Gong, M. et al. Quantum walks on a programmable two-dimensional 62-qubit superconducting processor. Science 372, 948-952 (2021).  
5. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
6. Ebadi, S. et al. Quantum phases of matter on a 256-atom programmable quantum simulator. Nature 595, 227-232 (2021).  
7. Vandersypen, L. M. K. et al. Experimental realization of Shor's quantum factoring algorithm using nuclear magnetic resonance. Nature 414, 883-887 (2001).  
8. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
9. Lanyon, B. P. et al. Simplifying quantum logic using higher-dimensional Hilbert spaces. Nat. Phys. 5, 134-140 (2009).  
10. Patel, R. B., Ho, J., Ferreyrol, F., Ralph, T. C. & Pryde, G. J. A quantum Fredkin gate. Sci. Adv. 2, e1501531 (2016).  
11. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019).  
12. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
13. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-siliconwaveguide quantum circuits. Science 320, 646-649 (2008).  
14. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nat. Commun. 2, 566 (2011).  
15. Zhang, M. et al. Supercompact Photonic Quantum Logic Gate on a Silicon Chip. Phys. Rev. Lett. 126, 130501 (2021).  
16. Qiang, X. G. et al. Large-scale silicon quantum photonics implementing arbitrary two-qubit processing. Nat. Photonics 12, 534-539 (2018).  
17. Paesani, S. et al. Experimental Bayesian Quantum Phase Estimation on a Silicon Photonic Chip. Phys. Rev. Lett. 118, 100503 (2007).  
18. Shao, X. Q. et al. Efficient scheme for implementing an N-qubit Toffoli gate by a single resonant interaction with cavity quantum electrodynamics. Phys. Rev. A. 75, 034307 (2007).  
19. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proc. of the  $43^{rd}$  Annual ACM Symposium on Theory of Computing 333-342 (ACM, 2011).  
20. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
21. Reck, M. et al. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58 (1994).  
22. Clements, W. R. et al. Optimal design for universal multiport interferometers. Optica 3, 1460-1465 (2016).  
23. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
24. Nagata, T. et al. Beating the Standard Quantum Limit with Four-Entangled Photon's. Science 316, 726-729 (2007).  
25. Chuang, I. L. & Yamamoto, Y. Quantum bit regeneration. Phys. Rev. Lett. 76, 4281-4284 (1996).  
26. Cory, D. G. et al. Experimental quantum error correction. Phys. Rev. Lett. 81, 2152-2155 (1998).  
27. Buhrman, H. et al. Quantum fingerprinting. Phys. Rev. Lett. 87, 167902 (2001).  
28. Ekert, A. K. et al. Direct estimations of linear and nonlinear functionals of a quantum state. Phys. Rev. Lett. 88, 217901 (2002).  
29. Blinov, B. B. et al. Observation of entanglement between a single trapped atom and a single photon. Nature 428, 153-157 (2004).  
30. O'Brien, J. L. et al. Demonstration of an all-optical quantum controlled-NOT gate. Nature 426, 264-267 (2003).  
31. Okamoto, R. et al. Demonstration of an Optical Quantum Controlled-NOT Gate without Path Interference. Phys. Rev. Lett. 95, 210506 (2005).  
32. Pfeiffer, M. H. P. et al. Ultra-smooth silicon nitride waveguides based on the Damascene reflow process: fabrication and loss origins. Optica 5, 884 (2018).  
33. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).

34. Zhong, H. S. et al. 12-Photon Entanglement and Scalable Scattershot Boson Sampling with Optimal Entangled-Photon Pairs from Parametric Down-Conversion. Phys. Rev. Lett. 121, 250505 (2018).  
35. Taballione, C. et al. 20-Mode Universal Quantum Photonic Processor. Preprint at https://arxiv.org/abs/2203.01801 (2022).  
36. Wilkes, C. M. et al. 60 dB high-extinction auto-configured Mach-Zehnder interferometer. Opt. Lett. 41, 5318-5321 (2016).  
37. Imany, P. et al. High-dimensional optical quantum logic in large operational spaces. npj Quantum Inf. 5, 59 (2019).  
38. Wang, H. et al. Towards optimal single-photon sources from polarized microcavities. Nat. Photonics. 13, 770-775 (2019).  
39. He, Y. M. et al. Coherently driving a single quantum two-level system with dichromatic laser pulses. Nat. Phys. 15, 941-946 (2019).

# ACKNOWLEDGEMENTS

This work was supported by the Singapore Ministry of Education (MOE) Tier 3 grant (MOE2017-T3-1-001), the Singapore National Research Foundation (NRF) National Natural Science Foundation of China (NSFC) joint grant (NRF2017NRF-NSFC002-014).

# AUTHOR CONTRIBUTIONS

Y.L. and A.Q.L. jointly conceived the idea. Y.L. performed the numerical simulations and theoretical analysis. Y.L., L.W., H.H.Z. and H.Z. did the fabrication and experiments. Y.L., L.W., Y.S., X.Z. and L.C.K. involved in the discussion and data analysis. Y.L., Y.S., A.Q.L. X.Z. and L.K.C. wrote the manuscript. L.C.K. and A.Q.L. supervised and coordinated all the work. All authors commented on the manuscript.

# COMPETING INTERESTS

The authors declare no competing interests.

# ADDITIONAL INFORMATION

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41534-022-00627-y.

Correspondence and requests for materials should be addressed to Xiaoqi Zhou, Leong Chuan Kwek or Ai Qun Liu.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/6b10ec45c48b28e03529d033ce1efde6dd27999454ef0c1e5ac36b803b4a8e60.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2022