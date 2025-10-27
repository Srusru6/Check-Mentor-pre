# Large-scale silicon quantum photonics implementing arbitrary two-qubit processing

Xiaogang Qiang $^{1,2,3}$ , Xiaoqi Zhou $^{4\star}$ , Jianwei Wang $^{1,5}$ , Callum M. Wilkes $^{1}$ , Thomas Loke $^{6}$ , Sean O'Gara $^{1}$ , Laurent Kling $^{1}$ , Graham D. Marshall $^{1}$ , Raffaele Santagati $^{1}$ , Timothy C. Ralph $^{7}$ , Jingbo B. Wang $^{6}$ , Jeremy L. O'Brien $^{1}$ , Mark G. Thompson $^{1}$  and Jonathan C. F. Matthews $^{1\star}$

Photonics is a promising platform for implementing universal quantum information processing. Its main challenges include precise control of massive circuits of linear optical components and effective implementation of entangling operations on photons. By using large-scale silicon photonic circuits to implement an extension of the linear combination of quantum operators scheme, we realize a fully programmable two-qubit quantum processor, enabling universal two-qubit quantum information processing in optics. The quantum processor is fabricated with mature CMOS-compatible processing and comprises more than 200 photonic components. We programmed the device to implement 98 different two-qubit unitary operations (with an average quantum process fidelity of  $93.2 \pm 4.5$ ), a two-qubit quantum approximate optimization algorithm, and efficient simulation of Szegedy directed quantum walks. This fosters further use of the linear-combination architecture with silicon photonics for future photonic quantum processors.

The range and quality of control that a device has over quantum physics determines the extent of quantum information processing (QIP) tasks that it can perform. Designing one device that is capable of performing any given QIP task is an ultimate goal, and silicon quantum photonics has attractive traits to achieve this. For example, photonic qubits are robust to environmental noise, single-qubit operations can be performed with high precision, a high density of reconfigurable components have been used to manipulate coherent light and established fabrication processes are CMOS compatible. However, quantum control needs to include entangling operations to be relevant to QIP—this is recognized as one of the most challenging tasks for photonics because of the extra resources required for each entangling step. Here, we demonstrate a programmable silicon photonics chip that generates two photonic qubits, on which it then performs arbitrary two-qubit unitary operations, including arbitrary entangling operations. This is achieved by using silicon photonics to reach the complexity required to implement an iteration of the linear combination of unitaries architecture that we have adapted to realize universal two-qubit processing. The device's performance shows that the design and fabrication techniques used in its implementation work well with the linear-combination architecture and can be used to realize larger and more powerful photonic quantum processors.

Miniaturization of quantum-photonic experiments into chip-scale waveguide circuits started $^{10}$  with a need to realize many-mode devices with high sub-wavelength stability for generalized quantum interference experiments, such as multi-photon quantum walks $^{11}$ , boson sampling $^{12-14}$  and high-dimensional quantum entanglement $^{15}$ . Universal six-mode linear optics implemented with a silica

waveguide chip (coupled to free-space photon sources and fibre-coupled detectors) demonstrated the principle that single photonic devices can be configured to perform any given linear optics task $^{16}$ . Silicon waveguides promise even greater capability for large-scale photonic processing, because of their third-order nonlinearity that enables photon-pair generation within integrated structures $^{17}$ , their capacity for integration with single-photon detectors $^{18}$  and their component density, which can be more than three orders of magnitude higher than that of silica $^{2}$ .

Programmable quantum processors have been reported with up to five trapped-ion qubits $^{19}$ , eleven NMR qubits $^{20}$  and tens of superconducting qubits $^{21}$ . However, for photons, up to two sequential two-qubit entangling operations implemented with free-space optics $^{22,23}$  and silicon quantum photonics $^{24,25}$  is the state of the art in qubit control. However, the degree of control and utility of these photonic demonstrators is limited intrinsically because arbitrary two-qubit processing requires the equivalent of three consecutive entangling gates in the circuit model of quantum computing, as demonstrated experimentally in 2010 with ion-trap quantum processing $^{26}$ . Effective QIP with three sequential entangling operations is beyond the level of complexity that can be practically constructed and maintained with free-space quantum optics or a hybrid of free-space nonlinear optics and integrated linear optics $^{16}$ .

Our scheme realizes arbitrary two-qubit unitary operation via a linear combination of four easy-to-implement unitaries—each being a tensor product of two single-qubit unitaries. The presented chip monolithically integrates four spontaneous four-wave mixing (SFWM) photon-pair sources, four pump rejection filters, 58 thermo-optical phase shifters, 82 multi-mode interferometer

![](images/4ccf3fa4466198cc413d0582075ec2645b7217d1113f52943bc4767011d78933.jpg)

![](images/396c75daf164337ae11d35dc821132720a4af9d61bf53f33c4eb4214ddea95d1.jpg)

![](images/05df62da1df7013ffd7359f2fbfcf45f6db4ac85466f63c7b29344e76db99f33.jpg)  
Fig. 1 | Quantum information processing circuits and schematic of the experimental set-up. a, Conventional quantum circuit model of QIP, which is a multiplication of quantum logic gates in series. b, Probabilistic linear combination of quantum gates (Supplementary Section 1A). The operation  $\sum_{i=0}^{k-1}\alpha_iV_i$  is implemented when all  $n$  control qubits are measured to be 0.  $U_{\mathrm{LC}}$  is a unitary operation with the first row in its matrix representation given as  $\{\alpha_0,\alpha_1,\dots,\alpha_{n-1}\}$ , where  $\sum_{i=0}^{k-1}|\alpha_i|^2 = 1$ ,  $k = 2^n$  and the success probability is  $1/k$ . Other rows are chosen accordingly to make  $U_{\mathrm{LC}}$  unitary. c, Deterministic linear-combination circuit for universal two-qubit unitary operation (Supplementary Section 1C). For a  $U \in \mathrm{SU}(4)$ , being decomposed as equation (1),  $U_{\mathrm{LC}}$  is defined as  $[\alpha_0,\alpha_1,\alpha_2,\alpha_3;\alpha_1,\alpha_0,-\alpha_3,-\alpha_2;\alpha_2,-\alpha_3,\alpha_0,-\alpha_1,\alpha_3,-\alpha_2,-\alpha_1,\alpha_0]$ .  $|\varphi_{12}\rangle$  is an arbitrary two-qubit state. The required two auxiliary control qubits can also be replaced by a quark (four-level system) and then  $U_{\mathrm{LC}}$  is a single-quark operation. d, Schematic of the chip and external set-up. A tunable continuous-wave laser is amplified with an optical erbium-doped fibre amplifier (EDFA), spectrally filtered by a dense wavelength-division multiplexing (DWDM) module and launched into the device through a V-groove fibre array (VGA). Photons emerging from the device are collected by the same VGA and two DWDMs are used to separate the signal (red) and idler (blue) photons. Photons are detected by two fibre-coupled superconducting nanowire single-photon detectors (SNSPDs). The polarizations of input/output photons are optimized by in-line polarization controllers (PCs). Coincidence counting logic records the two-photon coincidence events. Phase shifters on the device are configured through a digital-to-analog converter (DAC), controlled from a computer. The device includes five functional parts, which carry out the following: (1) generating quark entanglement; (2) preparing initial single-qubit states; (3) implementing single-qubit operations; (4) realizing linear combination; (5) changing the measurement basis. Parts (1), (3) and (4), as a whole, are used to implement a given SU(4) operation, where part (1) encodes the linear-combination coefficients, part (3) implements linear terms  $A_i$  and  $B_i$ , and part (4) realizes the linear combination of terms  $A_i \otimes B_i$  together with post-selection. Part (2) prepares arbitrary separable two-qubit states  $|\varphi_{\mathrm{ini}}\rangle$  ( $<=|\varphi_i\rangle \otimes |\varphi_2\rangle$ ) as the input, which is independent of the implemented gate. Part (5) rotates the output state so that it can be measured at desired basis. For further details of the device and set-up see Supplementary Sections 4 and 5.

(MMI) beamsplitters, 18 waveguide-crossers and 40 optical grating couplers. This constructs and exploits high-dimensional entanglement to implement the equivalent capability of three sequential entangling gates in the circuit model while using only two photons. It performs universal two-qubit processing with high fidelity while all thermal phase shifters in the device are simultaneously active, and it possesses high phase stability of the optical paths and waveguide interferometric structures. The chip is also repeatable under continuous operation and it can be reprogrammed at kilohertz rate. We demonstrate the chip's performance by performing process tomography on 98 implemented two-qubit quantum logic gates, by realizing the quantum approximate optimization algorithm (QAOA)[27,28] applied to three example constraint satisfaction problems (CSPs), and by simulating Szegedy quantum walks (SQWs)[29,30] over an example two-node weighted graph. Altogether, the results presented required 98,480 experiment configurations.

# Linear combination of unitaries on a chip for QIP

The conventional quantum circuit model for QIP is a sequence of quantum gates (Fig. 1a). The linear combination of unitary operations

is an alternative approach (Fig. 1b) that is central to various QIP tasks $^{8,31-35}$ . A universal two-qubit unitary  $U \in \mathrm{SU}(4)$  can be implemented by the four-operator linear combination

$$
U = \sum_ {i = 0} ^ {3} \alpha_ {i} \left(P _ {1} \sigma_ {i} Q _ {1}\right) \otimes \left(P _ {2} \sigma_ {i} Q _ {2}\right) \tag {1}
$$

where  $P$  and  $Q$  are single-qubit gates,  $\sigma_{i}$  are identity and Pauli gates  $(I,\sigma_x,\sigma_y,\sigma_z)$ , and  $\alpha_{i}$  are complex coefficients satisfying  $\sum_{i = 0}^{3}|\alpha_{i}|^{2} = 1$  (Supplementary Section 1B). This linear combination can be implemented immediately through a two-qubit version of the  $n$ -qubit circuit shown in Fig. 1b, with an intrinsic success probability of  $1 / 4$ . However, we also note that a deterministic implementation of the linear combination of  $U$  can in principle be achieved with extra classical controlled gates (Supplementary Section 1C), as shown in Fig. 1c. In the presented chip, the linear decomposition of  $U$  is implemented probabilistically by expanding the dimension of qubits into quids and using pre-entanglement between qudit systems that can be generated from parametric photon-pair generation[8,24].

![](images/a5140aeca49fec0fd86e1189c4e1856028a82b9c1c143522c9cf075ecc7a56b6.jpg)  
a

b  

<table><tr><td>Gate</td><td>Fidelity (%)</td></tr><tr><td>CNOT</td><td>98.85 ± 0.06</td></tr><tr><td>CZ</td><td>96.90 ± 0.17</td></tr><tr><td>CH</td><td>97.57 ± 0.07</td></tr><tr><td>SWAP</td><td>95.33 ± 0.24</td></tr><tr><td>iSWAP</td><td>94.45 ± 0.27</td></tr><tr><td>√ SWAP</td><td>92.41 ± 0.33</td></tr></table>

![](images/fad4b9c0c53d202eeb55ea441c48c93932014fa74dd96d474f3773ff82fdc7e3.jpg)  
c

![](images/4e6d7fb29bce833cce0d8c67f63ee8ea1af04082fae8d0e344061c6c29e6037d.jpg)  
d  
Fig. 2 | Experimental realization of arbitrary two-qubit gates. a,

![](images/fdf7dfd45fecc12cce07b8a5288ccca426b7c55ea8583168ac4f43a6dcf9397b.jpg)  
e

Histogram of measured process fidelities for 98 two-qubit quantum gates  $(\overline{F} = 93.15 \pm 4.53\%)$ . b, Measured process fidelities for example two-qubit gates: CNOT, CZ, CH, SWAP, iSWAP and  $\sqrt{\mathrm{SWAP}}$ . Errors are estimated by adding random noise to the raw data and performing many reconstructions. For definitions of CNOT, CZ, CH, SWAP, iSWAP and  $\sqrt{\mathrm{SWAP}}$ , see Supplementary Section 6A. c, Real part of experimentally determined process matrices of SWAP, with ideal theoretical values overlaid. d, Logical basis truth tables for entanglement filter. e, Logical basis truth tables for entanglement splitter.

This Hilbert-space-expansion approach implements arbitrary two-qubit unitaries using resources of only a two-photon entangled-quark state and multi-mode interferometry, which is highly stable on our chip.

Figure 1d presents a schematic of our silicon photonic chip operated with external electrical control, laser input and fibre-coupled superconducting detectors. The  $7.1\mathrm{mm}\times 1.9\mathrm{mm}$  chip consists of 4 spiral-waveguide spontaneous four-wave mixing (SFWM) photon-pair sources36, 4 laser pump rejection filters, 82 multi-mode interferometer (MMI) beamsplitters and 58 simultaneously running thermo-optic phase shifters36. Within the device, the four SFWM sources are used to create possible (signal-idler) photon pairs when pumped with a laser that is launched into the chip and split across the four sources according to complex coefficients  $\alpha_{i}$ . The spatially bunched photon pairs are coherently generated in any one of the four sources. Post-selecting when signal and idler photons exit at

the top two output modes (qubit 1) and the bottom two (qubit 2), respectively, yields a path-entangled ququart state  $|\varPhi\rangle$  as

$$
\alpha_ {0} | 1 \rangle_ {a} | 1 \rangle_ {e} + \alpha_ {1} | 1 \rangle_ {b} | 1 \rangle_ {f} + \alpha_ {2} | 1 \rangle_ {c} | 1 \rangle_ {g} + \alpha_ {3} | 1 \rangle_ {d} | 1 \rangle_ {h} \tag {2}
$$

at the end of stage (1), marked on the device shown in Fig. 1d, with intrinsic success probability of  $1/4$ .  $|1\rangle_{j}$  represents the Fock state in spatial modes labelled by  $j = a, b, c, d, e, f, g, h$ .

Spatial modes  $a - h$  are each extended into two modes to form path-encoded single-qubit states  $|\varphi_1\rangle$  or  $|\varphi_{2}\rangle$  with arbitrary amplitude, and phase-controlled with Mach-Zehnder interferometers (MZIs) and an extra phase shifter. Single-qubit operations  $A_{i}$ $(= P_{1}\sigma_{i}Q_{1})$  and  $B_{i}$ $(= P_{2}\sigma_{i}Q_{2})$  are applied using MZIs and phase shifters to  $|\varphi_1\rangle$  and  $|\varphi_{2}\rangle$  respectively, evolving  $|\varPhi\rangle$  into

$$
\sum_ {i = 0} ^ {3} \alpha_ {i} A _ {i} \left| \varphi_ {1} \right\rangle_ {u ^ {i}} B _ {i} \left| \varphi_ {2} \right\rangle_ {v ^ {i}} \tag {3}
$$

where  $u^i \in \{a, b, c, d\}$  and  $\nu^i \in \{e, f, g, h\}$ . Next, qubits  $a, b, c, d$  are combined into one final-stage qubit, and qubits  $e, f, g, h$  into the remaining final-stage qubit, as shown in stage (4) of Fig. 1d with intrinsic success probability 1/16. This removes path information of the signal (idler) photon and thus we obtain the final evolved two-photon state as

$$
\left(\sum_ {i = 0} ^ {3} \alpha_ {i} A _ {i} \otimes B _ {i}\right) | \varphi_ {\text {i n i}} \rangle \tag {4}
$$

where  $|\varphi_{\mathrm{ini}} \rangle (= |\varphi_1 \rangle \otimes |\varphi_2 \rangle)$  is an arbitrary separable two-qubit state. Once photons are generated, the overall intrinsic success probability of our design is 1/64, which is higher than the two main schemes considered for universal linear optical quantum computation: the Knill-Laflamme-Milburn (KLM) scheme and linear optical measurement-based quantum computation (MBQC)[37] (Supplementary Section 2A). The success probability of this optical implementation could be further increased to 1/4 if we were to separate signal and idler photons with certainty and use also an advanced linear-combination circuit that utilizes the unused optical ports in our current chip design (Supplementary Section 2B).

# Realizing individual quantum gates

The linear-combination scheme can simplify the implementation of families of two-qubit gates. For example, an arbitrary two-qubit controlled-unitary gate (CU) can be implemented as the linear combination of two terms:

$$
\mathrm {C U} = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} 1 & 0 \\ 0 & i \end{array} \right) \otimes \frac {I - i U}{\sqrt {2}} + \frac {1}{\sqrt {2}} \left( \begin{array}{c c} 1 & 0 \\ 0 & - i \end{array} \right) \otimes \frac {I + i U}{\sqrt {2}} \tag {5}
$$

and a SWAP gate can be implemented by a linear combination of only identity and Pauli gates:

$$
\mathrm {S W A P} = \frac {1}{2} (I \otimes I + \sigma_ {x} \otimes \sigma_ {x} + \sigma_ {y} \otimes \sigma_ {y} + \sigma_ {z} \otimes \sigma_ {z}) \tag {6}
$$

To show the reconfigurability and performance of our chip, we implemented 98 different two-qubit quantum logic gates, for which we performed on-chip full quantum process tomography and reconstructed the process matrix using the maximum likelihood estimation technique for each gate. A histogram of measured process fidelities for these 98 gates is shown in Fig. 2a, with a mean statistical fidelity of  $93.15 \pm 4.53\%$ . The implemented gates include many common instances—as shown in Fig. 2b—achieving high

![](images/16ed03caa075f62de8cf7a92867cac394b25e7980376d1326e615891c4808df0.jpg)  
a

![](images/a4c4af5226d1a2f262ac74d4cfdda7db6ccc5e7169adcd66ced989c7bbef5c7f.jpg)

![](images/561d8de938c67f0ad06f99fd9c2926c4ad5c3cba710d1727151cb6dd73987a37.jpg)

![](images/b6017622ee552f806ce3bab36b9ccb73399a1ee9b1535db74d7ee1cec73ba2d5.jpg)  
b

![](images/1df7f6757a457309b67d50c2eb18aa3088e9dc78f7ab6f334c3f2a8cc828986e.jpg)

![](images/5c121a36bb040cc2a86c3b04772931f22218252a11e96a65d40657a168ce0c48.jpg)

![](images/d5471486717b9bb28527334848aea1fe15e70b4f3a8c0bc15e2fcf1037eff497.jpg)  
c

![](images/1ad6c7d7417577dc1bb177803f212dae84e6fa782323214956131b2dab3dd517.jpg)

![](images/884f22fbf88f95603d463c2548cd7fb9cc5d8bbc761ec36fa7dbba4bcc4b2266.jpg)

![](images/08b26171f9b0601b6fb041e648f768af8b2878a0260b4da6ce7d769d43de26ab.jpg)  
d  
Fig. 3 | Experimental realization of a two-qubit quantum approximate optimization algorithm. Panels are arranged into three columns that correspond to three example CSPs, labelled 1-3. a, Quantum circuits of QAOA for each CSP. b,c, Theoretical (b) and experimentally (c) determined values of  $\langle \gamma ,\beta |C|\gamma ,\beta \rangle$  over the grid of  $[\gamma ,\beta ]\in [0,2\pi ]\times [0,\pi ]$  for  $\mathrm{CSP}_1$ ,  $\mathrm{CSP}_2$  and  $\mathrm{CSP}_3$ , with step size  $\delta_{\gamma} = \frac{2\pi}{20},\delta_{\beta} = \frac{\pi}{30}$ , for finding the optimized  $|\gamma ,\beta \rangle$  states. d, Experimental measurement results of the optimized  $|\gamma ,\beta \rangle$  states, outputting the searched target string  $z$  for each CSP 1-3. The s.d. of each individual probability is calculated by propagating error assuming Poissonian statistics.

![](images/993a0e64f2bc189df0be97e4b50879ff22cd1ed7ceb74251e0f9881533aa47cd.jpg)

![](images/5cf673345b8f458387bbb05e7aac47108a2fc83390dfb68c32f27d7c264a4914.jpg)

fidelities, such as a controlled-NOT (CNOT) with  $98.85 \pm 0.06\%$  and SWAP with  $95.33 \pm 0.24\%$ . Our device also allows implementation of non-unitary quantum operations. The entanglement filter  $(\mathrm{EF})^{8,38}$  and the entanglement splitter  $(\mathrm{ES})^8$  can be implemented by

$$
\mathrm {E F} = \left(I \otimes I + \sigma_ {z} \otimes \sigma_ {z}\right) / \sqrt {2} \tag {7}
$$

$$
\mathrm {E S} = \left(I \otimes I - \sigma_ {z} \otimes \sigma_ {z}\right) / \sqrt {2} \tag {8}
$$

The results are shown in Fig. 2d in the form of logical basis truth tables, with the classical fidelities of  $95.31 \pm 0.45\%$  and  $97.69 \pm 0.31\%$  respectively. Details of the experimental results and a further discussion about the experimental fidelities is presented in Supplementary Section 6.

# Implementing a two-qubit QAOA for CSPs

The QAOA was proposed for finding approximate solutions to combinatorial search problems such as  $\mathrm{CSPs}^{27,28}$ . It is a promising candidate to run on primitive quantum computers because of its possible use for optimization and its conjectured potential as a route to establishing quantum supremacy<sup>39</sup>. A general CSP is specified by  $n$  bits and a collection of  $m$  constraints, each of which involves a small subset of the bits. For a CSP, QAOA outputs a binary string  $z$  that (approximately) maximizes the number of satisfied constraints, that is,  $C(z) = \sum_{l=1}^{m} C_l(z)$  where  $C_l(z) = 1$  if  $z$  satisfies the  $l$ th constraint, otherwise 0—this is the goal of CSP.

The QAOA process can be summarized as follows. Suppose two operators  $C$  and  $B$  are defined as

$$
C | z \rangle := C (z) | z \rangle , B := \sum_ {i = 1} ^ {n} \sigma_ {x} ^ {(i)} \tag {9}
$$

where  $\sigma_x^{(i)}$  represents  $\sigma_{x}$  acting on the  $i$ th qubit, and a quantum state  $|\pmb {\gamma},\pmb {\beta}\rangle$  is defined as

$$
| \boldsymbol {\gamma}, \boldsymbol {\beta} \rangle = e ^ {- i \beta_ {p} B} e ^ {- i \gamma_ {p} C} \dots e ^ {- i \beta_ {1} B} e ^ {- i \gamma_ {1} C} H ^ {\otimes n} | 0 \rangle^ {\otimes n} \tag {10}
$$

where  $\pmb{\gamma} := (\gamma_1, \dots, \gamma_p) \in [0, 2\pi]^p$  and  $\pmb{\beta} := (\beta_1, \dots, \beta_p) \in [0, \pi]^p$ . QAOA seeks the target string  $z$  by searching the  $\pmb{\gamma}$  and  $\pmb{\beta}$  that maximize  $\langle \pmb{\gamma}, \pmb{\beta} | C | \pmb{\gamma}, \pmb{\beta} \rangle$  and then the corresponding state  $|\pmb{\gamma}, \pmb{\beta} \rangle$  in the computational basis encodes the solution. For a given  $\pmb{\gamma}$  and  $\pmb{\beta}$ ,  $\langle \pmb{\gamma}, \pmb{\beta} | C | \pmb{\gamma}, \pmb{\beta} \rangle$  can be evaluated through a quantum computer, which can further be used as a subroutine in an enveloping classical algorithm—for example, run the quantum computer with angles  $(\pmb{\gamma}, \pmb{\beta})$  from a fine grid on the set  $[0, 2\pi]^p \times [0, \pi]^p$  to find the best  $\pmb{\gamma}$  and  $\pmb{\beta}$  for maximizing  $\langle \pmb{\gamma}, \pmb{\beta} | C | \pmb{\gamma}, \pmb{\beta} \rangle^{39}$ . With  $p$  increasing, the quality of the approximation of QAOA improves[27].

In our experiments, we restricted ourselves to the  $p = 1$  case of QAOA, and applied QAOA to three 2-bit CSPs. The corresponding quantum circuits are shown in Fig. 3a. The first CSP (denoted as  $\mathrm{CSP}_1$ ) is the 2-bit Max2Xor problem which has just one constraint as  $C(z) = \frac{1}{2} + \frac{1}{2} z_1z_2$  where  $z_1, z_2 \in \{\pm 1\}$ . The other two CSPs have three constraints:

$$
\mathrm {C S P} _ {2}: C _ {1} (z) = \frac {1}{2} + \frac {1}{2} z _ {1}; C _ {2} (z) = \frac {1}{2} + \frac {1}{2} z _ {2}; C _ {3} (z) = \frac {1}{2} + \frac {1}{2} z _ {1} z _ {2} \tag {11}
$$

$$
\mathrm {C S P} _ {3}: C _ {1} (z) = \frac {1}{2} + \frac {1}{2} z _ {1}; C _ {2} (z) = \frac {1}{2} + \frac {1}{2} z _ {2}; C _ {3} (z) = \frac {1}{2} + \frac {1}{2} z _ {1} z _ {2} \tag {12}
$$

For the  $p = 1$  QAOA, there are only two angles,  $\gamma$  and  $\beta$ , to be found for optimizing  $\langle \gamma, \beta | C| \gamma, \beta \rangle$ . We search  $\gamma$  and  $\beta$  along a fine grid on the compact set  $[0, 2\pi] \times [0, \pi]$  and show each obtained value of  $\langle \gamma, \beta | C| \gamma, \beta \rangle$  as in Fig. 3b and c, where the target angles are marked as the reddest block. By measuring the corresponding  $|\gamma, \beta\rangle$  state in the computational basis for  $\mathrm{CSP}_1$ , we obtain '00' or '11' with highest probability, corresponding to the target string of  $\mathrm{CSP}_1$ :  $\{z_1, z_2\} = \{1, 1\}$  or  $\{-1, -1\}$ . Similarly, the obtained results for  $\mathrm{CSP}_2$  is  $\{z_1, z_2\} = \{1, 1\}$  and for  $\mathrm{CSP}_3$  are  $\{z_1, z_2\} = \{1, 1\}$ ,  $\{1, -1\}$  or  $\{-1, 1\}$  —either of which is a solution of  $\mathrm{CSP}_3$ . The experimental results are shown in Fig. 3d, with the classical fidelities between experiment and theory of  $99.88 \pm 0.10\%$ ,  $96.98 \pm 0.56\%$  and  $99.48 \pm 0.27\%$ , respectively.

# Simulating SQWs

Quantum walks model a quantum particle's random movement in a discretized space according to a given set of rules known as a graph. They are of interest for developing quantum computing $^{40}$  and quantum algorithms $^{41}$  and as an observable quantum phenomenon $^{11}$ . The SQW $^{29,30}$  is a particular class that allows unitary evolution on directed and weighted graphs—which the standard discrete-time and continuous-time quantum walk formalisms do not permit—and has been proposed for application to quantum speedup for ranking the relative importance of nodes in a connected database $^{42-44}$ . The realization of SQW-based algorithms on a quantum computer requires an efficient quantum circuit implementation for the walk itself. Although SQW in general cannot be implemented efficiently, efficient quantum circuit simulations of SQWs on families of graphs have been developed theoretically $^{45,46}$ . Here we have implemented SQW experimentally on an example two-node graph with four weighted directed edges—the largest SQW that can be implemented on our two-qubit processor.

A general weighted graph  $G$  with  $N$  nodes can be described by its transition matrix  $P$  where an element  $P_{i,j}$  is given by the weight

![](images/0bb3a9c44546d79dd19766810524b847a741d29d07e73c2cef5dfd5b6bfed6d9.jpg)

![](images/b060308fa8e513f4dc9b6483b27ec501d9ba2a6df207347ae0e1a04306f1b898.jpg)

![](images/bcd1cbb8270bb83f2762698a249e78c0724813a4a8be554cc17d752c2f5d56f5.jpg)

![](images/ccc324948d0af0f80e547be974d25e71278e20f9cdce3fce8fe8c19748402fc2.jpg)  
Fig. 4 | Experimental quantum simulation of Szegedy directed quantum walks. a, A weighted two-node graph. Edge weights are decided by  $\alpha, \beta \in [0,1]$ . b, Quantum circuit for a single-step SQW on the two-node graph.  $R(\theta)$  is defined as  $R(\theta) = [\cos\theta, -\sin\theta, \sin\theta, \cos\theta]$  with  $\theta \in \{\theta_1, -\theta_1, (\theta_1 - \theta_2), (\theta_2 - \theta_1)\}$ , where  $\theta_1 = \arccos(\sqrt{1 - \alpha})$  and  $\theta_2 = \arccos(\sqrt{\beta})$ . c-f, Theoretical (red points) and experimental (grey bars) probability distributions (of the walker being at node 1) of SQWs with initial state  $|00\rangle$ :  $\alpha = \beta = 0.25$ ,  $F_{avg} = 98.46 \pm 0.04\%$  (c);  $\alpha = \beta = 0.5$ ,  $F_{avg} = 98.48 \pm 0.04\%$  (d);  $\alpha = \beta = 0.43$ ,  $F_{avg} = 98.02 \pm 0.04\%$  (e);  $\alpha = 0.1$ ,  $\beta = 0.9$ ,  $F_{avg} = 98.35 \pm 0.15\%$  (f). The s.d. of each individual probability is also plotted, calculated by propagating error assuming Poissonian statistics.

![](images/1dfb4d653316e49ac89cea87b62430d5c5d3f5972500280b64c4bb1f863c0ce6.jpg)

of a directed edge from node  $i$  to  $j$ , satisfying  $\sum_{i=0}^{N-1} P_{i,j} = 1$ . A SQW on  $G$  is defined as a discrete-time unitary time evolution on a Hilbert space  $H = H_1 \otimes H_2$  where  $H_1$  and  $H_2$  are both  $N$ -dimensional Hilbert spaces, and thus its quantum circuit implementation requires  $2 \log N$  many qubits. The single-step operator of an SQW is given by  $U_{sz} = S(2\Pi - I)$ , where  $S$  is a SWAP operator defined as  $S = \sum_{i=0}^{N-1} \sum_{j=0}^{N-1} |i,j\rangle \langle j,i|$ , and  $\Pi$  is a projection operator as  $\Pi = \sum_{i=0}^{N-1} |\phi_i\rangle \langle \phi_i|$  with  $|\phi_i\rangle = |i\rangle \otimes \sum_{j=0}^{N-1} \sqrt{P_{j+1,i+1}} |j\rangle$  for  $i \in \{0,\dots,N-1\}$ . For the example two-node graph that we label  $\mathcal{E}$  and sketch in Fig. 4a, a quantum circuit implementation for a single-step SQW operator can be constructed by using the scheme proposed in ref. [46], as shown in Fig. 4b. Repeating this circuit generates an efficient quantum circuit implementation of multiple-step SQWs, which can easily simulate the dynamics of SQWs on the example graph and its variants.

The periodicity of SQWs is determined by the eigenvalues of the single-step operator  $U_{sz}$ , and it has been studied on several families of finite graphs $^{47}$ .  $U_{sz}$  of the graph  $\mathcal{E}$  has four eigenvalues:  $\{-1, 1, 1 - s - \sqrt{s^2 - 2s}, 1 - s + \sqrt{s^2 - 2s}\}$  where  $s = \alpha + \beta$  and  $\alpha, \beta \in [0, 1]$ .  $U_{sz}$  is periodic if and only if there exists an integer  $n$  such that  $\lambda_i^n = 1$  for all four eigenvalues  $\lambda_i$  of  $U_{sz}$ . The period is then given by the lowest common multiple of the periods of the eigenvalues.  $\mathcal{E}$  has a symmetric transition matrix when  $\alpha = \beta$ . For SQWs on a symmetric graph  $\mathcal{E}$ , periodic walks exist in the cases  $\alpha = \beta = \frac{1}{4}, \frac{1}{2}, \frac{3}{4}, 1$  with periods of 6, 4, 6 and 2 steps, respectively—of which the first two are experimentally verified as shown in Fig. 4c and d. SQWs on a general instance of  $\mathcal{E}$  do not exhibit perfect periodicity, as shown by Fig. 4e, which shows the behaviour of SQWs on  $\mathcal{E}$  with  $\alpha = \beta = 0.43$ .  $\mathcal{E}$  has an asymmetric transition matrix when  $\alpha \neq \beta$ , and perfect periodicities of SQWs can exist in particular cases, such as  $\alpha + \beta = 1$ , which has a period of four steps. An example of this kind,  $\alpha = 0.1, \beta = 0.9$ , is shown in Fig. 4f. In our device, we can also perform state tomography on a given time-evolved state of SQWs; we have performed quantum state tomography for more than 500 time-evolved states, observing an average state fidelity of  $93.95 \pm 2.52\%$  with theoretical prediction.

# Discussion

The computational capacity of the linear-combination protocol can be expanded by increasing the dimensionality of each linear-combination term. Such a high-dimensional quantum state can be easily prepared, manipulated and measured with a Reck et al.-style linear optical network $^{16}$ . For example, a four-qubit Tofolli gate can be effectively implemented through a four-qubit version of the linear-combination protocol that utilizes two-photon six-dimensional entanglement and four-dimensional Reck et al.-style circuits (Supplementary Section 3). However, the linear-combination protocol has its limitation on scaling up for universal quantum computation, as its success probability is inversely proportional to the number of terms. Although the protocol cannot be targeted for the ultimate quantum computer, it possesses great potential in the near and mid term for situations where the photonic components are easier to create than the photons themselves and it is no less demanding of individual component performance than other linear optics approaches to QIP. Our range of demonstrations with a single device has shown that the linear-combination scheme is valuable in permitting QIP demonstrations with the current state of the art in photonics and that silicon photonics is capable of fulfilling its requirements. The device reported comprises nonlinear photon sources, optical filtering and reconfigurable linear optics, and it was fabricated with standard CMOS-based silicon photonics processes onto a single photonic chip. It generates photons, encodes quantum information on them, manipulates them and performs tomographic measurement, all with high-fidelity quantum control for thousands of configurations. From our experience, our demonstrations of the QAOA and SQWs are beyond the practicality and performance achievable with free-space bulk optical experiments and glass-based integrated photonics. Together with developing multi-photon sources $^{48}$  and integration with on chip detection $^{49}$ , future iterations of silicon photonics open the way to more sophisticated photonic experiments that are impossible to achieve otherwise, including eventual full-scale universal quantum technologies using light $^{50}$ .

Data availability. The data that support the plots within this paper and other findings of this study are available from ref. [51].

Received: 30 January 2018; Accepted: 13 July 2018; Published online: 20 August 2018

# References

1. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
2. Silverstone, J. W., Bonnaue, D., O'Brien, J. L. & Thompson, M. G. Silicon quantum photonics. IEEE J. Sel. Top. Quantum Electron. 22, 390-402 (2016).  
3. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nat. Photon. 3, 687-695 (2009).  
4. Wilkes, C. M. et al. 60 dB high-extinction auto-configured Mach-Zehnder interferometer. Opt. Lett. 41, 5318-5321 (2016).  
5. Sun, J., Timurdogan, E., Yaacobi, A., Hosseini, E. S. & Watts, M. R. Large-scale nanophotonic phased array. Nature 493, 195-199 (2013).  
6. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).  
7. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
8. Zhou, X. Q. et al. Adding control to arbitrary unknown quantum operations. Nat. Commun. 2, 413 (2011).  
9. Long, G. L. General quantum interference principle and duality computer. Commun. Theor. Phys. 45, 825-844 (2006).  
10. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
11. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
12. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
13. Tillmann, M. et al. Experimental boson sampling. Nat. Photon. 7, 540-544 (2013).  
14. Crespi, A. et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat. Photon. 7, 545-549 (2013).  
15. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
16. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
17. Sharping, J. E. et al. Generation of correlated photons in nanoscale silicon waveguides. Opt. Express 14, 12388-12393 (2006).  
18. Najafi, F. et al. On-chip detection of entangled photons by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2014).  
19. Debnath, S. et al. Demonstration of a small programmable quantum computer with atomic qubits. Nature 536, 63-66 (2016).  
20. Vandersypen, L. M. K. et al. Experimental realization of Shor's quantum factoring algorithm using nuclear magnetic resonance. Nature 414, 883-887 (2001).  
21. Song, C. et al. 10-qubit entanglement and parallel logic operations with a superconducting circuit. Phys. Rev. Lett. 119, 180511 (2017).  
22. Martin-López, E. et al. Experimental realization of Shor's quantum factoring algorithm using qubit recycling. Nat. Photon. 6, 773-776 (2012).  
23. Barz, S. et al. A two-qubit photonic quantum processor and its application to solving systems of linear equations. Sci. Rep. 4, 6115 (2014).  
24. Wang, J. et al. Experimental quantum Hamiltonian learning. Nat. Phys. 13, 551-555 (2017).  
25. Santagati, R. et al. Silicon photonic processor of two-qubit entangling quantum logic. J. Opt. 19, 114006 (2017).  
26. Hanneke, D. et al. Realization of a programmable two-qubit quantum processor. Nat. Phys. 6, 13-16 (2010).  
27. Farhi, E., Goldstone, J. & Gutmann, S. A quantum approximate optimization algorithm. Preprint at https://arxiv.org/abs/1411.4028 (2014).  
28. Farhi, E., Goldstone, J. & Gutmann, S. A quantum approximate optimization algorithm applied to a bounded occurrence constraint problem. Preprint at https://arxiv.org/abs/1412.6062 (2014).  
29. Szegedy, M. Spectra of quantized walks and a  $\sqrt{\delta\varepsilon}$  rule. Preprint at https:// arxiv.org/abs/quant-ph/0401053 (2004).  
30. Szegedy, M. in Proceedings of the 45th Annual IEEE Symposium on Foundations of Computer Science 32-41 (IEEE, 2004).  
31. Childs, A. M. & Wiebe, N. Hamiltonian simulation using linear combinations of unitary operations. Quantum Inform. Comput. 12, 901-924 (2012).  
32. Childs, A. M., Kothari, R. & Somma, R. D. Quantum algorithm for systems of linear equations with exponentially improved dependence on precision. SIAM J. Comput. 46, 1920-1950 (2017).  
33. Patel, R. B., Ho, J., Ferreyrol, F., Ralph, T. C. & Pryde, G. J. A quantum Fredkin gate. Sci. Adv. 2, e1501531 (2016).  
34. Wei, S. J., Ruan, D. & Long, G. L. Duality quantum algorithm efficiently simulates open quantum systems. Sci. Rep. 6, 30727 (2016).

35. Qiang, X., Zhou, X., Aungskunsiri, K., Cable, H. & O'Brien, J. L. Quantum processing by remote quantum control. Quantum Sci. Technol. 2, 045002 (2017).  
36. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photon. 8, 104-108 (2014).  
37. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
38. Okamoto, R. et al. An entanglement filter. Science 323, 483-485 (2009).  
39. Farhi, E. & Harrow, A. W. Quantum supremacy through the quantum approximate optimization algorithm. Preprint at https://arxiv.org/abs/1602.07674 (2016).  
40. Childs, A. M., Gosset, D. & Webb, Z. Universal computation by multiparticle quantum walk. Science 339, 791-794 (2013).  
41. Childs, A. M. & Goldstone, J. Spatial search by quantum walk. Phys. Rev. A 70, 022314 (2004).  
42. Paparo, G. D. & Martin-Delgado, M. A. Google in a quantum network. Sci. Rep. 2, 444 (2012).  
43. Paparo, G. D., Müller, M., Comellas, F. & Martin-Delgado, M. A. Quantum Google in a complex network. Sci. Rep. 3, 2773 (2013).  
44. Loke, T., Tang, J. W., Rodriguez, J., Small, M. & Wang, J. B. Comparing classical and quantum pageranks. Quantum Inf. Process. 16, 25 (2017).  
45. Chiang, C.-F., Nagaj, D. & Wocjan, P. Efficient circuits for quantum walks. Quantum Inform. Comput. 10, 420-434 (2010).  
46. Loke, T. & Wang, J. B. Efficient quantum circuits for Szegedy quantum walks. Ann. Phys. 382, 64-84 (2017).  
47. Highchi, Y., Konno, N., Sato, I. & Segawa, E. Periodicity of the discrete-time quantum walk on a finite graph. *Interdiscip. Inform.* Sci. 23, 75-86 (2017).  
48. Collins, M. J. et al. Integrated spatial multiplexing of heralded single-photon sources. Nat. Commun. 4, 2582 (2013).  
49. Khasminskaya, S. et al. Fully integrated quantum photonic circuit with an electrically driven light source. Nat. Photon. 10, 727-732 (2016).  
50. Gimeno-Segovia, M., Shadbolt, P. J., Browne, D. E. & Ruddolph, T. From three-photon Greenberger-Horne-Zeilinger states to ballistic universal quantum computation. Phys. Rev. Lett. 115, 020502 (2015).  
51. Qiang, X. et al. Underpinning data for 'Large-scale silicon quantum photonics implementing arbitrary two-qubit processing.' https://doi.org/10.5523/bris.1gbf7bpuazruz26cxh0tc0q9zq (2018).

# Acknowledgements

The authors thank S. Paesani, J. Silverstone, G. Sinclair, K. Aungskunsiri and C. Sparrow for helpful discussions and A. Murray and M. Louit for assistance with wire-bonding the device. This work was supported by EPSRC programme grant EP/L024020/1, US Army Research Office (ARO) grant no. W911NF-14-1-0133, US Air Force Office of Scientific Research (AFOSR) and the Centre for Nanoscience and Quantum Information (NSQI). X.Q. acknowledges support from the China Scholarship Council and the National Natural Science Foundation of China (NSFC no. 61632021). X.Z. acknowledges support from the National Key Research and Development Program (2017YFA0305200 and 2016YFA0301700), the National Young 1000 Talents Plan, and the Natural Science Foundation of Guangdong (2016A030312012). J.W. acknowledges support from the National Young 1000 Talents Plan. T.C.R. acknowledges support from the Australian Research Council Centre of Excellence for Quantum Computation and Communication Technology (project no. CE170100012). J.L.O.B. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies. M.G.T. acknowledges support from the ERC starter grant ERC-2014-STG 640079 and an EPSRC Early Career Fellowship EP/K033085/1. J.C.F.M acknowledges support from EPSRC Early Career Fellowship EP/M024385/1.

# Author contributions

X.Z., X.Q., T.C.R., J.L.O.B. and J.C.F.M. conceived and designed the project. X.Z. and X.Q. designed the device. X.Q., J.W., C.M.W., L.K., G.D.M. and R.S. built the experimental set-up and carried out the experiments. X.Q., X.Z., T.L., S.O.G., J.B.W. and J.C.F.M. performed the theoretical analysis. X.Z., J.L.O.B., M.G.T. and J.C.F.M. managed the project. All authors discussed the results and contributed to writing the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41566-018-0236-y.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to X.Z. or J.C.F.M.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.