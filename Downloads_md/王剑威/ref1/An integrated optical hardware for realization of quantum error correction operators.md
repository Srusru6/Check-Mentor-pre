OPEN

# An integrated optical hardware for realization of quantum error correction operators

S. Armaghani $^{1}$  & A. Rostami $^{1,2}$

The efficient error correction subsystem is essential for quantum computing and communication systems due to challenges like no-cloning and destructive measurements. Error-correction codes and fault-tolerant technologies are vital for mitigating errors. Our focus is on implementing fault-tolerant encoding circuits based on Steane code within optical integrated circuits using two C-NOT structures that utilize nonlinear optics. A Mach-Zehnder structure made from  $\mathrm{Si}_3\mathrm{N}_4$  and nonlinear material with a nonlinear coefficient of  $n_2 = -3.5\times 10^{-15}\mathrm{m}^2 /\mathrm{W}$  (the nanocrystal of PbS), is exposed to  $1.55\mu \mathrm{m}$  wavelength waves, where propagated modes serve as qubits. The main input state delivers  $25~\mu \mathrm{W}$  per  $100\mathrm{nm}^2$ , and secondary inputs provide  $15~\mu \mathrm{W}$  per  $100\mathrm{nm}^2$ , allowing entanglement and error detection among qubits. The design has achieved a fidelity of  $F > 0.89$ , crucial for effective error correction in photon-based quantum computations.

Keywords Error correction algorithm, Quantum computing, Steane code, Optical integrated circuit, Nonlinearity, Emitted modes, Qubits, Fidelity

Quantum error correction (QEC) plays a pivotal role in mitigating quantum noise and incoherence within the realms of quantum computation and key distribution<sup>1</sup>. The attainment of fault tolerance in encryption circuits, syndrome measurement circuits, and logic gate operations is essential for ensuring reliable quantum computation<sup>2-5</sup>. Quantum computation leverages principles such as superposition and entanglement; however, it remains vulnerable to environmental perturbations that can induce complex quantum errors, including bit and phase errors<sup>6-9</sup>. To address these challenges, fault-tolerant quantum computing employs QEC techniques<sup>4,9</sup>. QEC, supplementary, plays a vital role in the context of quantum key distribution (QKD), as it not only enhances the precision of the generated keys but also significantly fortifies the overall security of the quantum communication infrastructure<sup>10,11</sup>. These correction methodologies facilitate the reliable transmission of secure keys between parties by mitigating the risks associated with noise and potential eavesdropping<sup>12,13</sup>. The basic strategy of QEC involves encoding a qubit in such a way that errors can be detected and corrected without directly measuring the qubit value. To this end, recent research has achieved a significant breakthrough by performing a set of logical operations on a pair of entangled logical qubits separated by a distance of two. These operations are preserved through repeated cycles of error detection and demonstrate a combination of precise logical operations and a scalable method for repeated stabilization<sup>14-18</sup>. Various QEC protocols have also been demonstrated in quantum systems in nuclear magnetic resonance approaches, ion traps<sup>19</sup>, and in the field of linear optics quantum computing<sup>20-22</sup>.

The implementation of quantum error-correcting codes in conjunction with high-precision quantum gates can substantially reduce error rates in quantum processors, contingent upon the components operating within an established gate error threshold[23-25]. Reliable execution of the Steane code algorithm necessitates a fault-tolerant framework founded on a transverse architecture. Introduced in 1996, the Steane code represents a well-established method for error correction. This algorithm underscores the design of fault-tolerant coding circuits that incorporate logical operations and the marking of qubits, facilitating accurate error detection. This code is utilized in the context of quantum systems, as illustrated in Fig. 1. According to Fig. 1, suppose the initial state of a single qubit, expressed as  $\alpha |0\rangle +\beta |1\rangle$ , has been successfully encoded as  $\alpha |000\rangle +\beta |111\rangle$ . Subsequently, each of the three qubits undergoes an independent application of the bit flip channel. If a bit flip occurs on one or fewer of the qubits, a straightforward two-stage error correction procedure can be implemented to restore the accurate quantum state. The first stage involves error detection, or syndrome diagnosis, where a measurement is performed to identify any errors that may have occurred in the quantum state, producing the error syndrome.

<sup>1</sup>Photonics and Nanocrystal Research Lab. (PNRL), Faculty of Electrical and Computer Engineering, University of Tabriz, Tabriz 5166614761, Iran. <sup>2</sup>SP-EPT Lab., ASEPE Company, Industrial Park of Advanced Technologies, Tabriz, Iran. <sup>3</sup>email: rostami@tabrizu.ac.ir

![](images/35997f1bafc859a375b4816dd06d846486a1940b964986efac33a54517b17472.jpg)  
Fig. 1. Encoding and decoding circuit for n-qubit Steane code. The data to enter the circuit on the q-line $^{6,27}$ .

The second stage, recovery, uses the value of the error syndrome to determine the appropriate procedure for restoring the initial state $^{6,14,26}$ .

The implementation of quantum code algorithms in the fields of optics and photonics seems to be essential for the advancement of various technologies, especially in information processing and secure communications[28]. Quantum optics facilitates quantum computation by exploiting the distinctive properties of photons and utilizing the ability to manipulate quantum states to generate qubits from light particles[28,29]. These qubits enable quantum algorithms to solve complex problems more efficiently than classical systems, especially in areas such as simulation and data analysis. The continuous advancement of quantum technologies has significant implications for industries such as healthcare, telecommunications, and materials science[30-32]. As researchers strive to develop large-scale quantum communication networks and advanced quantum processors, the integration of quantum algorithms into optics and photonics is becoming increasingly critical. Innovations arising from this research are poised to revolutionize our understanding of information processing and our interactions with the physical world[33,34].

In this work, we present a proposal for the utilization of a discrete waveguide state set to implement an encryption circuit based on the Steane code. Our approach entails a comprehensive optical framework designed to facilitate quantum computations through the use of a multi-mode Mach-Zehnder waveguide interferometer (MZI), directional couplers (DCs), and nonlinear optics $^{35,36}$ . Significant research on nonlinear materials has been conducted within the field of chemistry, emphasizing their applications in engineering and photonics, which aids in the design of such structures $^{37-39}$ . Indeed, through the utilization of a dual-mode waveguide MZI employing direct current and Kerr-like media, we have formulated an optical model for a quantum controlled-NOT (C-NOT) gate, showcasing a fidelity exceeding 0.96, which will be discussed in the next section. The rest of our contribution is organized as follows: "Methods" Section introduces the general structure of the proposed encoding circuit based on the Steane code and its operating principles. "Discussion" Section investigates the quantum C-NOT gate with optical waveguide modes. "Results" Section explains the finite-difference time-domain (FDTD) simulation process and results. The final section is devoted to conclusions.

# Methods

# The proposed encoding circuit based on Steane code

In order for a quantum algorithm to be effectively implemented on an appropriate platform, whether electrical, optical, photonic, or otherwise, it is essential to incorporate a precise logic circuit. This integration facilitates the design on the intended platform, whether utilizing classical or quantum forms. In the context of the Steane code, we employ the logic circuit detailed in the referenced materials, as illustrated in Fig. 1, to inform our photonic structure design. This circuit caters specifically to a qubit configuration requiring the integration of two C-NOT gates operating in parallel. In this arrangement, the primary qubit functions as the control qubit, transmitting its information to two auxiliary qubits. In the Steane code,  $CN_{12}^{x}$  and  $CN_{13}^{x}$ , are C-NOT operators and are written in the following form:

$$
C N _ {i j} ^ {x} = \left| 0 _ {i} 0 _ {j} \right\rangle \left\langle 0 _ {i} 0 _ {j} \right| ^ {x} + \left| 0 _ {i} 1 _ {j} \right\rangle \left\langle 0 _ {i} 1 _ {j} \right| ^ {x} + \left| 1 _ {i} 0 _ {j} \right\rangle \left\langle 1 _ {i} 1 _ {j} \right| ^ {x} + \left| 1 _ {i} 1 _ {j} \right\rangle \left\langle 1 _ {i} 0 _ {j} \right| ^ {x} \tag {1}
$$

In our framework, "i" represents the modes assigned to the control photon, while "j" denotes the modes assigned to the target photon. In a basic three-layer waveguide setup, we have derived a solution for Maxwell's Equations to describe the guided modes within the structure. This leads to the determination of electric-field profiles, referred to as the normal modes and other orthogonal modes. These components of the transverse electric (TE) field satisfy the scalar wave Equation, where  $n_{xy}$ , represents the refractive index profile, and  $k = 2\pi /\lambda$

with  $\lambda$  denoting the free-space wavelength. The solution  $|\psi_{1,2,3}\rangle$  of the scalar wave Equation, along with its first derivatives, are universally continuous and therefore bounded, resulting in an eigenvalue Equation for the discrete values of  $\beta^{35}$ . The eigenfunctions with discrete eigenvalues are termed the normal modes of the waveguide, forming a comprehensive set of functions such that any solution of the scalar wave Equation can be expressed in terms of these modes. Given a specific geometry and optical wavelength, Fig. 2 illustrates the structure supporting two normal modes: the  $\mathrm{TE}_0$  mode and the  $\mathrm{TE}_1$  mode. Thus, the input state depicted in Fig. 2 corresponds to  $|\psi_{in}\rangle = |\psi_1\rangle \otimes |\psi_2\rangle \otimes |\psi_3\rangle$ , resulting in  $|\psi_{in}\rangle = (\alpha |0_1\rangle +\beta |1_1\rangle)|0_2\rangle |0_3\rangle$ . Finally, when the C-NOT operators act on this input state, the output is the entangled state of the qubits, as described by Eq. (2).

$$
\left| \psi_ {o u t} \right\rangle = C N _ {1 3} ^ {x} C N _ {1 2} ^ {x} \left| \psi_ {i n} \right\rangle = \alpha \left| 0 _ {1} 0 _ {2} 0 _ {3} \right\rangle + \beta \left| 1 _ {1} 1 _ {2} 1 _ {3} \right\rangle \tag {2}
$$

The results obtained from Eq. (2) demonstrate the successful entanglement of three qubits. The output from all three waveguides must replicate the initial input state,  $|\psi_1\rangle$ .

Referencing Fig. 2, we focus on the  $CN_{12}^{x}$  and  $CN_{13}^{x}$ , the section of the gate, which consists of three main components: (1) Y-branch, (2) DCs, and (3) phase shifter. Each section was analyzed separately, with particular emphasis on the DCs section. The initial analysis involves examining a two-mode waveguide with a uniform coupling region of length "t". The power transfer between modes is accurately described by coupling Equations. By neglecting the weak coupling between different order modes, we can effectively characterize how the field amplitude in each of the two waveguides varies based on specific parameters.

In the field of optics, various degrees of freedom are utilized to create qubits, enabling quantum calculations and operations. Each degree of freedom corresponds to a unique Hilbert space and specific basis states, denoted as  $B_{i}$  (e.g.,  $\mathfrak{a}$ ,  $\mathfrak{n}$ , etc.). Each input or output can be represented in the form of  $\sum_{i}|B_{i}\rangle$ . This section explores two types of photon motion introduced by the double-rail configuration and the motion modes of each photon within the waveguide. The Y-branch structure allows for the transformation of calculations from the mode field to the location field, facilitating the investigation of the C-NOT structure within the location field. Consequently, the sequence of calculations and state verification is conducted in the coupler and phase change sections. The transfer matrix for both illustrates the movement paths of waves in the upper and lower waveguides separately, in different modes, along with the associated coupling coefficient  $(\kappa_{a})$ . Finally, the parameters presented in each section of Table 1 are defined as follows:

$|\alpha \rangle$ : The first mode is denoted as  $\alpha = 0$  and the second mode as  $\alpha = 1$ , corresponding to the propagation constants  $\beta_{0}$  and  $\beta_{1}$ , respectively. When the profile  $n_{xy}$ , is independent of  $z$ , arbitrary local fields  $\psi$  propagating in the waveguide at position  $z$  can be expressed as a superposition of the two normal modes,  $\alpha = 0$  (the  $\mathrm{TE}_0$  mode) and  $\alpha = 1$  (the  $\mathrm{TE}_1$  mode), represented as:  $|\psi \rangle = C_0|0\rangle +C_1|1\rangle$ , where  $C_0$  and  $C_1$  are the amplitudes of the modes  $\alpha = 0$  and  $\alpha = 1$ , respectively<sup>35,36</sup>.  
$|n\rangle$ : In this representation of a qubit, the presence of a photon in the upper waveguide signifies the state  $|0\rangle$ , while a photon in the lower waveguide signifies the state  $|1\rangle$ . An arbitrary single-photon qubit state can be expressed as a superposition of these states:  $a|0\rangle + b|1\rangle$  Where  $|a|^2$  and  $|b|^2$  denote the probabilities of finding a photon in the upper and lower waveguides, respectively.

Additionally,  $|\bar{a}|^2 + |b|^2 = 1$ . To realize functional quantum circuits, precise control and manipulation of qubits are essential, which can be achieved through combinations of beam splitters and phase shifters  $(\varphi)$ . According to the Fourier transform performed by the Y-branch structure, we can express the transformation function of the upper waveguide at the position of the Y-branch (marked in green in Fig. 2) as follows:

$$
T = e ^ {i \frac {\varphi}{2}} \left( \begin{array}{c c} \cos \left(2 \kappa_ {a} l\right) \cos \left(\frac {\varphi}{2}\right) - i \sin \left(\frac {\varphi}{2}\right) & - i \sin \left(2 \kappa_ {a} l\right) \cos \left(\frac {\varphi}{2}\right) \\ - i \sin \left(2 \kappa_ {a} l\right) \cos \left(\frac {\varphi}{2}\right) & \cos \left(2 \kappa_ {a} l\right) \cos \left(\frac {\varphi}{2}\right) + i \sin \left(\frac {\varphi}{2}\right) \end{array} \right) \tag {3}
$$

![](images/eba21ac15a672ee5549d3dfc4d9df0a4a01b5fa8e8b16647a0dc2b8066d51b89.jpg)  
Fig. 2. The supposed circuit of the encoding in the Steane code is implemented on the integrated optical waveguide.

Table 1. Analysis of different components of the quantum optical C-Not gate.  

<table><tr><td>Structure</td><td>Graph</td><td>Transfer matrix</td><td>Output state</td></tr><tr><td>Y-branch40</td><td>|α) → n = 0 → n = 1 →</td><td>1/√2 [1 -1n -1n]</td><td>|α) = 1/√2 ∑n=0,1 e(iπ)αn |n)</td></tr><tr><td>DCs41,42</td><td>n = 0 → n = 0 → k l n = 1 → n = 1 →</td><td>[ cos (καl) isin (καl) i sin (καl) cos (καl) ]</td><td>|ψn) = 1/√2 ∑α=0,1 (e-(iπ)αn cos (καl) +ie-(iπ)αn sin (καl)) |α)</td></tr><tr><td>Phase-shifter42,43</td><td>nonlinear matrial n = 0 → n = 1 →</td><td>[ exp (jφ) 0 0 1 ]</td><td>|ψn) = exp (i (1 - n) φ) |n)</td></tr></table>

The phase transition discussed in this section governs the final output, which varies depending on the strength of the incoming waves from the input side, represented as  $|\psi_1\rangle$ . This occurs due to the use of a non-linear material, designed based on the principles of nonlinear optics. The input  $|\psi_1\rangle$ , acts as a control parameter, determining when phase transitions take place. A complete transition, termed mode TE1, results in a  $\pi$ -phase shift, while no transition, termed mode  $\mathrm{TE}_0$ , leads to no phase change. In our scenarios, the difference between 0 and  $\pi$  can vary significantly.

To encapsulate, our optical configuration enabled the duplication of the original qubit into two additional waveguides, integrating it into the circuits of the quantum optical complex for quantum computations and operations. In this setup, any disruption or error in one of the waveguide modes will be reflected in the output, making the use of high-fidelity devices with error correction structures essential. Reference $^{20}$  is claimed to introduce a comprehensive optical framework for quantum computation utilizing the optical transverse modes found in multimode waveguides. The proposed C-NOT gate shows promise for straightforward realization, leveraging optical waveguide technology. Our proposed circuit, in turn, utilizes the C-NOT structure developed in this reference, wherein the number of qubits is represented by waveguides. The state of each qubit is characterized by the propagating modes, suggesting that these qubits can be implemented using two distinct states of two-state waveguides. Specifically, the logical state  $|0\rangle$ $|0\rangle$  is encoded within one normal state  $(\mathrm{TE}_0\rightarrow 0)$ , while the logical state  $|1\rangle$ $|1\rangle$  is represented by the orthogonal normal state  $(\mathrm{TE}_1\rightarrow 1)$ . The qubit state space encompasses all superpositions of these fundamental normal states  $|0\rangle$  and  $|1\rangle$ .

# Discussion

# Waveguide coupling design rules

In scenarios where the waveguide exhibits variations along its length in the  $z$  direction, the propagation of the field  $\Psi(x,y,z)$  can be effectively modeled using a set of coupled equations derived from the normal modes  $\{\Psi_0,\Psi_1\}$ . The first mode is denoted as  $\Psi_0(x,y)$ , while the second mode is labeled as  $\Psi_1(x,y)$ . Each mode is associated with its respective propagation constants,  $\beta^0$ , and  $\beta_{1}$ . When the refractive index profile,  $n(x,y)$ , remains uniform along the  $z$  direction, any local field  $\Psi (x,y,z)$  propagating through the waveguide can be expressed as a linear combination of these two normal modes—the  $\mathrm{TE}_0$  mode  $(\Psi_0)$  and the  $\mathrm{TE}_1$  mode  $(\Psi_{1})$ . This modeling approach captures the complex interactions that occur due to changes in the waveguide structure. This work investigates a two-mode waveguide featuring a uniform coupling region measuring  $90~\mu \mathrm{m}$  in length. The analysis of power transfer between the modes is effectively articulated through coupling equations. By neglecting the weak coupling effects between modes of different orders, this research offers a detailed characterization of the field amplitude variations within each of the two waveguides, based on specific parameters. The amplitudes of the coupled modes are represented as  $C_0$  and  $C_1$ . Employing the principles of coupled mode theory, this study formulates the governing equations for the coupled modes across multiple two-mode waveguides.

$$
\frac {d C _ {j} ^ {(k)} (z)}{d z} = \frac {i \omega}{4} \frac {\beta_ {j} ^ {(k)}}{\left| \beta_ {j} ^ {(k)} \right|} \sum_ {\acute {k}} \sum_ {l = 0, 1} K _ {j l} ^ {k \acute {k}} C _ {l} ^ {(\acute {k})} (z) e ^ {i \left(\beta_ {j} ^ {(k)} - \beta_ {l} ^ {(k)}\right) z} \tag {5a}
$$

$$
K _ {j l} ^ {k \acute {k}} = \int \Psi_ {j} ^ {(k) *} \left(n ^ {2} (x, y, z) - n ^ {2} (x, y)\right) \Psi_ {j} ^ {(\acute {k}) *} d x d y \tag {5b}
$$

Additionally, the notation  $n(x,y,z)$  indicates that the refractive index is dependent on the  $z$ -axis. The superscript  $k$  signifies the  $k$ th waveguide, while the subscript  $j$  refers to the  $j$ th order state. In the field of optics, various degrees of freedom are utilized to generate qubits for quantum computations and operations, with each degree of freedom corresponding to a distinct Hilbert space and specific basis states. This discussion also addresses the two types of photon motion that arise from the two-Rayleigh configuration, along with the associated excited states for each photon within the waveguide. Furthermore, the Y-branch structure facilitates the transition from mode field calculations to spatial field analysis, allowing for a comprehensive examination of the proposed structure within the spatial domain. To sum up, by selecting a coupling length of  $90~\mu \mathrm{m}$ , our analysis of power

transfer between modes, based on the coupling equations, indicates that the excited mode achieves complete coupling. This phenomenon occurs in a scenario where the ground mode does not couple with the second waveguide, which serves as the foundation of our design. The variation in the qubits is contingent upon the amplitude of the excited mode. When the ground mode functions as the control qubit, or the primary qubit, no alterations are instituted.

# Nonlinear phase modulation mechanisms

The proposed C-NOT gate shows promise for straightforward realization, leveraging optical waveguide technology. This gate can be implemented using a MZI equipped with PbS nanocrystals in its arms. The PbS nanocrystals demonstrate significant Kerr-like nonlinearity even at relatively low light intensities, thereby overcoming intensity attenuation caused by two-photon absorption, as described in Reference $^{44}$ . The researchers employed the Z-scan technique to measure the nonlinear refractive index  $(n_2)$  and absorption coefficient  $(\beta)$  of PbS quantum dots around  $1550~\mathrm{nm}$ , using a picosecond pulsed laser. They found that  $\mathfrak{n}_2$  can be adjusted based on wavelength and aligns with the absorbance spectrum of  $\mathrm{PbS}^{44,45}$ . Consequently, in our proposed circuit (see Fig. 2), we utilize two C-NOT structures to perform the C-NOT operation using nonlinear optics. The circuit incorporates an MZI structure composed of  $\mathrm{Si}_3\mathrm{N}_4 / \mathrm{SiO}_2$  and nanocrystalline PbS. The nanocrystalline PbS exhibits a nonlinear coefficient of  $\mathrm{n}_2 = -3.5\times 10^{-15}\mathrm{m}^2 /\mathrm{W}$  and is exposed to waves with a wavelength of  $1.55\mu \mathrm{m}^{45}$ .

In nonlinear optics, phase alterations stem from fluctuations in the refractive index. The amplitude of the input state  $|\psi_1\rangle$ , In the mode, TE1 is directly related to the coupling occurring. Thus, changes in the refractive index within the non-linear medium produce different phases at varying distances. To achieve full coupling in mode  $\mathrm{TE}_1$  (transitioning from  $n = 1$  to  $n = 0$  or vice versa) while preventing coupling in mode  $\mathrm{TE}_0$  (maintaining the state within the same waveguide), we plotted the changes in the input amplitude of the control state,  $|\psi_1\rangle$ , against the length of the nonlinear material, as shown in Fig. 3. This resulted in a phase differential of  $\pi$  degrees.

The nonlinear material used in this study is PbS nanocrystals. According to the provided diagrams, the optimal length for the input of the primary qubit port, set at  $1.15350 \times 10^{7}$ , is determined to be  $297~\mu \mathrm{m}$ . In contrast, the input for the auxiliary qubit ports carries an amplitude of  $7.69 \times 10^{6}$  ( $|\psi_{2,3}\rangle = 7.69 \times 10^{6}|TE_0\rangle$ ). Upon traversing the Y-branch structure, this input will reach the upper branch of the structure at a magnitude of  $1 / \sqrt{2}$  times greater. In the context of cross-phase modulation (XPM), which is a phenomenon in non-linear optics, the coefficient of failure undergoes corresponding changes[43]. It is understood that the primary qubit can exist in different states across two modes. The subsequent figures depict the combined effect of these two modes in various states, taking into account different refractive indices and phases within the same length of  $297~\mu \mathrm{m}$ . The diagrams represent the normalized probability of the mode  $\mathrm{TE}_1$  amplitude. Also, the occurrence of the  $\mathrm{TE}_1$  mode along the qubit's path is influenced by variations in the intensity of the input field applied to the non-linear material, specifically PbS nanocrystals. These variations in intensity directly affect the material's refractive index. Furthermore, adjusting the Schiff refraction multiplier significantly impacts the signal phase.

Therefore, in Fig. 4 we can see that it is essential to examine two critical ratios: (a) the ratio of changes in the likelihood of occurrence to changes in the refractive index, and (b) the ratio of the likelihood of occurrence to the phase shift.

# Propagation loss mitigation strategies

To mitigate propagation loss in lead sulfide (PbS) integrated photonic circuits on silicon dioxide  $(\mathrm{SiO}_2)$  substrates, several strategic measures must be implemented to enhance optical performance. Firstly, surface passivation is critical, as PbS waveguides are particularly vulnerable to oxidation losses. The application of protective coatings,

![](images/b1306abc67a0b0844da40f18bffd46edbd94a9fd9bd23e8fd426e02ce6aff90a.jpg)  
(a)

![](images/3537735d1d56fd6dfd929fcab4ed91998ee8f058fc81f5a671c0cc8c345b2c2f.jpg)  
Fig. 3. (a) The changes in the input intensity of the port  $|\psi_1\rangle$ , are proportional to the changes in the length of the non-linear material that creates a phase shift equal to  $\pi$ -degrees. (b) For the input amplitude equal to  $1.15350\times 10^{7}$  in mode TE1 from the main qubit port  $\left(|\psi_{1}\rangle = 1.15350\times 10^{7}|TE_{1}\rangle\right)$ , the amount of phase shift that occurs in different lengths of the non-linear material line occurs.  
(b)

![](images/f496d03b75e4dfd9c0ab5c97f05b8e3254c6d07bfc7037b1a1e1e6771a7f27bb.jpg)  
(a)  
Fig. 4. The occurrence of mode TE1 in the qubit's path varies with changes in the input field intensity to the non-linear material (Pbs-nanocrystal), affecting the refractive index. Adjusting the Schiff refraction multiplier also alters the phase, prompting an examination of two ratios: (a) the ratio between changes in the likelihood of occurrence and the refractive index, and (b) the ratio of the likelihood of occurrence to the phase shift.

![](images/187b518895e5af6c56d01385c46d46d18363c99312d36ef7918f7d7d72969854.jpg)  
(b)

such as silicon nitride, can help preserve waveguide integrity and prolong the device's operational lifespan. Secondly, the optimization of waveguide design is vital in minimizing scattering losses. By refining geometric parameters, including width, height, and refractive index, engineers can achieve improved optical confinement. The incorporation of thermally grown  $\mathrm{SiO}_2$  hard masks during the fabrication process can further enhance etch selectivity, leading to smoother sidewalls and a reduction in propagation losses. Moreover, the composition and microstructure of materials are of significant importance; polycrystalline silicon waveguides on  $\mathrm{SiO}_2$  substrates exhibit ultra-low propagation losses. Employing advanced fabrication techniques, such as chemical vapor deposition (CVD) and precise annealing, can improve crystalline quality and increase transmission efficiency. Finally, high-quality fabrication processes are indispensable. The utilization of methods such as reactive ion etching (RIE) and precise deposition techniques ensures the uniformity of waveguides, thereby minimizing mode mismatch and further reducing propagation losses in integrated photonic circuits.

To reduce propagation losses in silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)$  waveguides on  $\mathrm{SiO}_2$  substrates within photonic integrated circuits, it is essential to first recognize that these waveguides can experience scattering due to roughness along their sidewalls. One effective method to minimize these losses during the coupling process is to use tapered mode transfer. Additionally, material defects may contribute to unwanted losses, which can be partially mitigated through surface passivation using a  $\mathrm{SiO}_2$  coating to protect against oxidation. Other key factors that can help reduce losses in photonic structures include advanced fabrication techniques, phase-sensitive loss measurements for precise optical analysis, and resonator-based characterization to evaluate intrinsic losses.

In conclusion, by integrating these strategies—surface passivation, optimized waveguide design, careful material engineering, and advanced fabrication techniques—significant enhancements in the performance of  $\mathrm{SiO}_2$  substrate photonic integrated circuits can be realized, thereby expanding their applicability across various optical communication systems.

# Results

In our work on integrated optical circuits, we focused on designing a structure capable of executing the C-NOT operation with high fidelity. By employing enhanced non-linear techniques, we improved the efficiency of the C-NOT gate in quantum integrated circuits, particularly in its application to quantum cryptography and error correction. As is known, in the C-NOT operation, the target qubit mirrors the state of the control qubit; if the target qubit is in the 0 state, the state of the control qubit is fully transferred to it.

The results presented in Fig. 5 validate the accuracy of our findings. The structure we developed is an MZI setup composed of  $\mathrm{Si}_3\mathrm{N}_4$ , incorporating nanocrystalline PbS with a non-linear coefficient of  $\mathrm{n}_2 = -3.5\times 10^{-15}\mathrm{m}^2 /\mathrm{W}$  as the nonlinear material. This structure operates under  $1.55~{\mu\mathrm{m}}$  wavelength waves, with the resultant modes utilized as qubits for quantum computation and interference. By using the primary quantum state as a control pump, replication occurs in other segments of the system. The control input state has a power of  $25~{\mu\mathrm{m}}$  per  $100~\mathrm{nm}^2$ , while the target input states have a power of  $15~{\mu\mathrm{m}}$  per  $100~\mathrm{nm}^2$ . For a better understanding of the positioning of y and dm, please refer to Fig. 2. Here, the subscript mm denotes the number of waveguides, while  $\mathrm{d}_{\mathrm{m}}$  indicates the center of the waveguides in the y direction.

One important aspect of proper design in quantum circuits also is to express the fidelity parameter for each logic gate and to calculate the average fidelity of all designed quantum gates. In this section, we will discuss the results of the  $CN^x$ , gate in detail and compare its fidelity, calculated using the following relationship, with that of other similar gates. The fidelity of a state in quantum devices is defined as follows  $F = |\langle \psi | \phi \rangle|^{246}$ . We denote the actual state as  $\psi$  and the target state as  $\phi$ .

In our analysis, we computed this parameter for a single  $CN^x$ , gate in two entangled states and the base state, and then compared our results with values documented in other scholarly works. This comparative analysis is conveniently summarized in Table 2.

![](images/53f6ab4503b4d63bcdb23390514b8d5771f91570e3dce5d78b5ea5d4d3f885b6.jpg)

![](images/81375c586ebb16be80dbb617df47bd2bca90daa1385019dde29b1f217748411e.jpg)

![](images/3bc6d52e62c350554b1049e1e1c7ba3c42a6b51bd012fbc474dd147b62c67551.jpg)

![](images/2daef9b3e61cb8ec70d77c57fed02821d69c6d264e3ed5026168b0983f38ef07.jpg)

Fig. 5. The outcomes derived from the implementation of the quantum NOT control gate  $(CN^x)$  in the optical integrated circuit across three states: (a) Base state:  $|\psi_{2,3}\rangle = 7.69\times 10^{6} |TE_{0}\rangle$ ,  $|\psi_{1}\rangle = 1.15350\times 10^{7} |TE_{0}\rangle$  
![](images/cb123257160c6be736223eb2dcf363b5cc0fe583a844e02b5b5e0c866ab0ac8b.jpg)  
(b) Bell states:  $|\psi_{2,3}\rangle = 7.69\times 10^{6} |TE_{0}\rangle ,|\psi_{1}\rangle = 1.15350\times 10^{7}\left(\frac{|TE_{0}\rangle + |TE_{1}\rangle}{\sqrt{2}}\right)$ . (c) Base state:

![](images/92e68f7ce99b7615d57e2155b749a836bf39a5a878117205b4f78f962cd36784.jpg)

$$
\left| \psi_ {2, 3} \right\rangle = 7. 6 9 \times 1 0 ^ {6} \left| T E _ {0} \right\rangle , \left| \psi_ {1} \right\rangle = 1. 1 5 3 5 0 \times 1 0 ^ {7} \left| T E _ {1} \right\rangle .
$$

Our collaborative effort has led to the development of a  $CN^x$ , gate with exceptional fidelity, positioning it as a strong candidate for the proposed encoding framework in optical integrated circuits, as illustrated in Fig. 2. By employing two consecutive C-NOTs, we can entangle the primary qubit state with two additional states, facilitating its integration into complex quantum circuits for computational purposes. It is important to note that each trajectory corresponds to a unique Hilbert space, with qubits encoded based on two propagation modes. Consequently, the expected output of the encoding circuit across all three waveguides should exhibit uniformity. In Fig. 6, it is evident that the state of the original qubit, serving as the control signal in the  $CN^x$ , gates, is replicated in the output of both gates. Furthermore, the states of all three outputs are intricately interconnected,

Table 2. Fidelity comparison between the proposed  $CN^x$  and other works.  

<table><tr><td>Reference</td><td>Fidelity on C-NOT gate (approximately)</td><td>Structure</td><td>Input state of control</td></tr><tr><td>47</td><td>0.66</td><td>Ion trapping</td><td>Bell state</td></tr><tr><td>48</td><td>0.81</td><td>Photonically</td><td>Bell state</td></tr><tr><td>21</td><td>0.83</td><td>Photonically</td><td>Bell state</td></tr><tr><td>49</td><td>0.834</td><td>Photonically</td><td>Bell state</td></tr><tr><td>50</td><td>0.87</td><td>Photonically</td><td>Bell state</td></tr><tr><td>51</td><td>0.92</td><td>Integrated optical circuit</td><td>Bell state</td></tr><tr><td>52</td><td>0.96</td><td>Nonphotonic</td><td>Bell state</td></tr><tr><td>53</td><td>0.89</td><td>Integrated optical circuit</td><td>Bell state</td></tr><tr><td>Our contribution</td><td>0.91</td><td>Photonically</td><td>Bell state</td></tr><tr><td>47</td><td>0.82</td><td>Ion trapping</td><td>Base state</td></tr><tr><td>49</td><td>0.88</td><td>Photonically on free space</td><td>Base state</td></tr><tr><td>54</td><td>0.84</td><td>Photonically on free space</td><td>Base state</td></tr><tr><td>51</td><td>094</td><td>Integrated optical circuit</td><td>Base state</td></tr><tr><td>55</td><td>0.95</td><td>Photonically integrated circuit</td><td>Base state</td></tr><tr><td>21</td><td>0.95</td><td>Photonically</td><td>Base state</td></tr><tr><td>56</td><td>0.99</td><td>Large-scale silicon photonics</td><td>Base state</td></tr><tr><td>53</td><td>0.82</td><td>Integrated optical circuit</td><td>Base state</td></tr><tr><td>Our contribution</td><td>0.97</td><td>Photonically</td><td>Base state</td></tr></table>

aligning with the fundamental principles of quantum coding in the Steane code algorithm. Our work involved the successful design and simulation of photon movement within an optical integrated circuit, resulting in the generation of emission waves. These simulations were conducted using the Finite-Difference Time-Domain (FDTD) method in Numerical software[57].

At this stage, we will calculate the fidelity of two  $\mathrm{CN}^{\mathrm{x}}$  gates within the coded structure, as outlined in Table 3. This table includes three modes: two basic states and one of the four Bell states.

Figure 7 illustrates the fidelity of the input quantum state of the primary qubit, depicting the input state to the coding structure in the Bell state and the resulting changes in the output for the auxiliary qubits. Remarkably, the original qubit remains unchanged, indicating an intuitive replication of the original qubit across two alternate pathways. By entangling three qubits across distinct Hilbert spaces, error detection can be efficiently performed following quantum computation on the qubits. In this approach, if an error occurs in one of the qubits, the remaining two qubits can reliably represent the result of the computation. This technique is unique to quantum computing circuits. The probability of errors affecting two qubits must be lower than that for a single qubit to ensure the effective operation of majority voting[26].

# Calculation

In the field of quantum computing, a significant challenge arises from error detection due to the inability to clone quantum information, the presence of continuous errors, and the disruptive nature of measurement. Various solutions have been proposed to tackle this issue, one of which is Steane coding. Our study aimed to implement the Steane coding technique within an optical integrated circuit. By utilizing non-linear optical effects, we achieved a fidelity exceeding  $96\%$  for the gates used in this setup. The input powers in our proposed structure are set at 25 and  $15\mu \mathrm{m}$  per  $100\mathrm{nm}^2$ . In our research, we investigated the error correction mechanism by introducing separate fields for the quantum ground states of photonic qubits. Our results indicated that the primary qubit is initially copied into at least two auxiliary qubits before entering the computational domain within quantum structures. Through successive computational nodes (C-NOTs), we observed this process for the input states. It is noteworthy that photonic qubits were generated based on mode propagation in the waveguide, with each waveguide representing a distinct qubit within a unique Hilbert space. Additionally, we introduced a method for transitioning the state from the mode domain to the position domain for a qubit, accomplished through Fourier transformation. Accurately defining qubits and their associated Hilbert space in quantum computing is crucial due to the extensive freedom of photons in encoding quantum information. Therefore, integrating accuracy and efficiency into the error correction framework, based on the structure of the calculation circuit, is essential. We recommend that future research should concentrate on photon qubits derived from emission modes in the realm of quantum computing, where we have successfully implemented error correction coding with a high-fidelity level.

![](images/d2ee6840063fc5e0bab4639938409a32316aee2cee090f67ce8eb206806af19c.jpg)  
(a)

![](images/1ec92a324661a93bf9eacb711f2269a6881f53c629c51dfb2276923b83551aec.jpg)

![](images/ff73326aedcfae50017d620534a1e5c5005c22a9ab720cbade1ded09f2abf9f4.jpg)  
(b)  
(c)

![](images/906bcdd932adf8904f19625cf9952c219d1301d010f6820e01a8caf221c3dbbb.jpg)

![](images/88322b49dc738695a511bc3b8c2db4b2e59d192ab208556420e9e0221c419f6a.jpg)  
Fig. 6. The proposed framework for quantum encoding would be implemented utilizing the Steane code method across three distinct states: (a, c) Base state, and (b) Bell state.

![](images/5b8a428478236ae51a9c7637dac78d330e75969a76b312d1295ba9446f4e0fd8.jpg)

Table 3. The fidelity level of quantum gates in the proposed quantum coding structure.  

<table><tr><td>Q-gate</td><td>|00⟩base state</td><td>|11⟩base state</td><td>\( \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) \)</td></tr><tr><td>\( CN_{12}^{x} \)</td><td>97.4</td><td>92.98</td><td>89.55</td></tr><tr><td>\( CN_{13}^{x} \)</td><td>97.28</td><td>98.65</td><td>91.29</td></tr></table>

![](images/9431c5f97e453c6ec3f740c66b9298470e1da8c9c2679cc7f2e3798cd7335c49.jpg)  
Fig. 7. The entangled state is created from the input state of the Bell state, which involves copying the main qubit into auxiliary qubits.

# Data availability

The datasets used and/or analyzed during the current study are included in the body of the paper.

Received: 19 November 2024; Accepted: 11 September 2025

Published online: 15 October 2025

# References

1. Guruswami, V. & Rudra, A. Explicit codes achieving list decoding capacity: Error-correction with optimal redundancy. IEEE Trans. Inf. Theory 54(1), 135-150 (2008).  
2. Cane, R. et al. Mitigation of decoherence-induced quantum-bit errors and quantum-gate errors using Steane's code. IEEE Access 8, 83693-83709 (2020).  
3. Paler, A. & Devitt, S. J. An introduction to fault-tolerant quantum computing. in Proceedings of the 52nd Annual Design Automation Conference (2015).  
4. Zheng, M. et al. A Bayesian approach for characterizing and mitigating gate and measurement errors. ACM Trans. Quant. Comput. 4(2), 1-21 (2023).  
5. Alvarez-Sanchez, J., Alvarez-Bravo, J. & Nieto, L. A quantum architecture for multiplying signed integers. in Journal of Physics: Conference Series (IOP Publishing, 2008).  
6. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge University Press, 2010).  
7. Djordjevic, I. Quantum Information Processing and Quantum Error Correction: An Engineering Approach (Academic Press, 2012).  
8. Gaitan, F. Quantum Error Correction and Fault-Tolerant Quantum Computing (CRC Press, 2008).  
9. Zhou, H., et al. Algorithmic fault tolerance for fast quantum computing. arXiv preprint http://arxiv.org/abs/2406.17653 (2024).  
10. Johnson, J. S. et al. An analysis of error reconciliation protocols used in quantum key distribution systems. J. Defen. Model. Simulat. 12(3), 217-227 (2015).  
11. Nwaga, P. C. & Nwagwughiagwu, S. Exploring the significance of quantum cryptography in future network security protocols. World J. Adv. Res Rev. 24(3), 817-833 (2024).  
12. Boyd, C. & Mao, W. Designing secure key exchange protocols. in Computer Security—ESORICS 94: Third European Symposium on Research in Computer Security Brighton, United Kingdom, November 7–9, 1994 Proceedings 3 (Springer, 1994)  
13. Boyd, C., Mathuria, A. & Stebila, D. Protocols for Authentication and Key Establishment Vol. 1 (Springer, 2003).  
14. Marques, J. F. et al. Logical-qubit operations in an error-detecting surface code. Nat. Phys. 18(1), 80-86 (2022).  
15. Andersen, C. K. et al. Repeated quantum error detection in a surface code. Nat. Phys. 16(8), 875-880 (2020).  
16. Armaghani, S., Rostami, A. & Mirtagioglu, H. Bragg grating based entangled biphoton dispersion management. Phys. Scr. 98(10), 105112 (2023).  
17. Armaghani, S. & Rostami, A. Higher-order dispersion properties of Bragg gratings and their impact on entangled biphoton dispersion management. J. Mod. Opt. https://doi.org/10.1080/09500340.2025.2495662 (2025).  
18. Armaghani, S. & Rostami, A. Superimposed Bragg gratings and entangled biphoton dispersion management. Opt. Contin. 3(3), 354-367 (2024).  
19. Farouk, M., et al. Parallel implementation of CNOTN and C2NOT2 gates via homonuclear and heteronuclear Förster interactions of Rydberg atoms. in Photonics (MDPI, 2023).  
20. Adcock, J. C. et al. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10(1), 3528 (2019).  
21. Harris, N. C. et al. Large-scale quantum photonic circuits in silicon. Nanophotonics 5(3), 456-468 (2016).  
22. Pittman, T., Jacobs, B. & Franson, J. Demonstration of quantum error correction using linear optics. Phys. Rev. A: Atom. Mol. Opt. Phys. 71(5), 052332 (2005).  
23. Du, F.-F. & Ren, X.-M. A deterministic qudit-dependent high-dimensional photonic quantum gate with weak cross-kerr nonlinearity. Opt. Laser Technol. 180, 111440 (2025).  
24. Du, F.-F. et al. Refined Kerr-effect-based high-dimensional quantum gate. Opt. Lett. 50(4), 1113-1116 (2025).  
25. Zhu, Y. et al. Implementation of double Feynman gate in high dimensional quantum systems. Sci. Rep. 15(1), 12184 (2025).  
26. Djordjevic, I. B. Quantum Information Processing, Quantum Computing, and Quantum Error Correction: An Engineering Approach (Academic Press, 2021).  
27. Bhattacharai, P. Design and Simulation of Automated Quantum Error Correction Protocols for Encoded Single Qubits (Western Illinois University, 2022).  
28. Su, D. et al. Implementing quantum algorithms on temporal photonic cluster states. Phys. Rev. A 98(3), 032316 (2018).  
29. Qiang, X. et al. Implementing graph-theoretic quantum algorithms on a silicon photonic quantum walk processor. Sci. Adv. 7(9), eabb8375 (2021).

30. Memon, Q. A., Al Ahmad, M. & Pecht, M. Quantum computing: Navigating the future of computation, challenges, and technological breakthroughs. Quant. Rep. 6(4), 627-663 (2024).  
31. Palai, G. et al. Architecting of the quantum algorithm for Z-gate optical qubit to realize efficient quantum communication system. J. Opt. https://doi.org/10.1007/s12596-025-02488-y (2025).  
32. Wayo, D. D. K., Goliatt, L. & Ganji, D. Linear Optics to Scalable Photonic Quantum Computing. arXiv preprint http://arxiv.org/abs/2501.02513 (2025).  
33. Larasati, H. T. & Choi, B.-S. Towards Fault-Tolerant Distributed Quantum Computation (FT-DQC): Taxonomy, Recent Progress, and Challenges (ICT Express, 2025).  
34. Belghachi, M., Quantum Networks: Emerging Research Areas, Challenges, and Opportunities (2023).  
35. Fu, J. Quantum computations with optical waveguide modes. in Quantum Information and Computation (SPIE, 2003).  
36. Fu, J. et al. Classical simulation of quantum entanglement using optical transverse modes in multimode waveguides. Phys. Rev. A: Atom. Mol. Opt. Phys. 70(4), 042313 (2004).  
37. Mokhtarpour, M. et al. Thermal properties of novel phase change materials based on protic ionic liquids containing ethanolamines and stearic acid for efficient thermal energy storage. Phys. Chem. Chem. Phys. 26(18), 13839-13849 (2024).  
38. Zarghami, A. et al. High-efficiency upconversion process in cobalt and neodymium-doped graphene QDs for biomedical applications. Sci. Rep. 13(1), 10277 (2023).  
39. Dortaj, H. et al. High-speed and high-precision PbSe/PbI2 solution process mid-infrared camera. Sci. Rep. 11(1), 1533 (2021).  
40. Tamir, T., Griffel, G. & Bertoni, H. L. Guided-Wave Optoelectronics: Device Characterization, Analysis, and Design (Springer Science & Business Media, 2013).  
41. Saleh, B. E. & Teich, M. C. Guided-wave optics. Fundam. Photon. 1 (2001).  
42. Thompson, M. G. et al. Integrated waveguide circuits for optical quantum computing. IET Circuits Dev. Syst. 5(2), 94-102 (2011).  
43. Ferreira, M. F. Nonlinear Effects in Optical Fibers (Wiley, 2011).  
44. Moreels, I. et al. Spectroscopy of the nonlinear refractive index of colloidal PbSe nanocrystals. Appl. Phys. Lett. 89(19), 193106 (2006).  
45. Omari, A. et al. Role of interband and photoinduced absorption in the nonlinear refraction and absorption of resonantly excited PbS quantum dots around  $1550\mathrm{nm}$ . Phys. Rev. B: Condens. Matter Mater. Phys. 85(11), 115318 (2012).  
46. Qin, H. et al. Experimental direct quantum fidelity learning via a data-driven approach. Phys. Rev. Lett. 132(19), 190801 (2024).  
47. McDonnell, K., Keary, L. & Pritchard, J. Demonstration of a quantum gate using electromagnetically induced transparency. Phys. Rev. Lett. 129(20), 200501 (2022).  
48. Ciampini, M. A. et al. Path-polarization hyperentangled and cluster states of photons on a chip. Light: Sci. Appl. 5(4), e16064-e16064 (2016).  
49. Li, J.-P. et al. Heralded nondestructive quantum entangling gate with single-photon sources. Phys. Rev. Lett. 126(14), 140501 (2021).  
50. Peruzzo, A. et al. A variational eigenvalue solver on a photonic quantum processor. Nat. Commun. 5(1), 4213 (2014).  
51. Politi, A. et al. Silica-on-silicon waveguide quantum circuits. Science 320(5876), 646-649 (2008).  
52. Chen, X. et al. A generalized multipath delayed-choice experiment on a large-scale quantum nanophotonic chip. Nat. Commun. 12(1), 2712 (2021).  
53. Feng, L.-T. et al. Transverse mode-encoded quantum gate on a silicon photonic chip. Phys. Rev. Lett. 128(6), 060501 (2022).  
54. He, H., Wu, J. & Zhu, X. An introduction to all-optical quantum controlled-NOT gates. in Advanced Computer Architecture: 11th Conference, ACA 2016, Weihai, China, August 22-23, 2016, Proceedings 11 (Springer, 2016).  
55. Carolan, J. et al. Universal linear optics. Science 349(6249), 711-716 (2015).  
56. Qiang, X. et al. Large-scale silicon quantum photonics implementing arbitrary two-qubit processing. Nat. Photon. 12(9), 534-539 (2018).  
57. Solutions, L. F. Lumerical FDTD Solutions (Lumerical Inc, 2024).

# Author contributions

S.A. wrote the paper and simulated the results and A.R. wrote and edited the paper, supervised the project.

# Declarations

# Competing interests

The authors declare no competing interests.

# Additional information

Correspondence and requests for materials should be addressed to A.R.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025