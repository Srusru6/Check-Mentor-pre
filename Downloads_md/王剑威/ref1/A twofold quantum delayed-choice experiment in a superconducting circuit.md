# QUANTUM MECHANICS

# A twofold quantum delayed-choice experiment in a superconducting circuit

Ke Liu, $^{1}$  Yuan Xu, $^{1}$  Weiting Wang, $^{1}$  Shi-Biao Zheng, $^{2*}$  Tanay Roy, $^{3}$  Suman Kundu, $^{3}$  Madhavi Chand, $^{3}$  Arpit Ranadive, $^{3}$  Rajamani Vijay, $^{3}$  Yipu Song, $^{1}$  Luming Duan, $^{1,4*}$  Luyan Sun $^{1*}$

Wave-particle complementarity lies at the heart of quantum mechanics. To illustrate this mysterious feature, Wheeler proposed the delayed-choice experiment, where a quantum system manifests the wave- or particle-like attribute, depending on the experimental arrangement, which is made after the system has entered the interferometer. In recent quantum delayed-choice experiments, these two complementary behaviors were simultaneously observed with a quantum interferometer in a superposition of being closed and open. We suggest and implement a conceptually different quantum delayed-choice experiment by introducing a which-path detector (WPD) that can simultaneously record and neglect the system's path information, but where the interferometer itself is classical. Our experiment is realized with a superconducting circuit, where a cavity acts as the WPD for an interfering qubit. Using this setup, we implement the first twofold delayed-choice experiment, which demonstrates that the system's behavior depends not only on the measuring device's configuration that can be chosen even after the system has been detected but also on whether we a posteriori erase or mark the which-path information, the latter of which cannot be revealed by previous quantum delayed-choice experiments. Our results represent the first demonstration of both counterintuitive features with the same experimental setup, significantly extending the concept of quantum delayed-choice experiment.

2017 © The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC).

# INTRODUCTION

Wave-particle duality is among the most fundamental properties of quantum mechanics. According to Bohr's principle of complementarity, a quantum system has complementary and mutually exclusive properties that cannot be observed at the same time (1-3). Whether a quantum system behaves as a wave or as a particle depends on the arrangement of measurement apparatus, as demonstrated by the delayed-choice experiment with a Mach-Zehnder (MZ) interferometer, in which the choice of inserting the second beam splitter  $\mathrm{BS}_2$  or not is made after the photon has entered the interferometer (4-9), as shown in Fig. 1A. When  $\mathrm{BS}_2$  is inserted, no path information is available so that the probability for detecting the photon at either outport depends on the relative phase  $\phi$  between the two paths, showing the interference effect. In the absence of  $\mathrm{BS}_2$ , detecting the photon at each outport unambiguously reveals which route the photon has traveled so that no interference appears. The delayed-choice nature rules out the assumption that the photon could know beforehand what type of experimental apparatus it will be confronted with, and then behaves accordingly.

Recently, a quantum delayed-choice experiment was proposed by Ioniciou and Terno (10), where the action of  $\mathrm{BS}_2$  is controlled by a quantum ancilla: When the ancilla is in the state  $|0\rangle_{\mathrm{a}}, \mathrm{BS}_2$  is removed; for the ancilla state  $|1\rangle_{\mathrm{a}}, \mathrm{BS}_2$  is inserted. The process, in terms of quantum circuits (11), is shown in Fig. 1B, where the Hadamard gates  $\mathrm{H}_{1}$  and  $\mathrm{H}_2$  represent the corresponding beam splitters. When the ancilla is in a superposition of  $|0\rangle_{\mathrm{a}}$  and  $|1\rangle_{\mathrm{a}}$ , the wave- and particle-like behaviors of the test system can be observed at the same time; these two

complementary phenomena are encoded in the same output state and postselected depending on the measured value of the ancilla. This proposal has been successfully demonstrated in experiments using photons (12-14) and other systems (15-17).

Here, we propose and experimentally demonstrate a twofold quantum delayed-choice experiment by introducing a which-path detector (WPD) in a superposition of its on and off states. Unlike the beam splitter that is used to split or recombine the particle's path, the WPD is used to determine the path taken by the particle. Compared to the qubit used to control the action of the output beam splitter in the previous quantum delayed-choice experiments (10, 12-17), a quantum WPD works in a larger Hilbert space and thus enables one to have two chances to postselect the behavior of the test quantum system, as will be shown. As illustrated in Fig. 1C through a double-slit apparatus, when the WPD is in its on state  $|O\rangle$ , it collects the path information of the incoming quantum particle and changes its state to  $|O_1\rangle$  and  $|O_2\rangle$ , which correspond to paths 1 and 2 of the particle with wave functions  $\psi_{1}(\mathbf{r})$  and  $\psi_{2}(\mathbf{r})$ , respectively. When the WPD is in its off state  $|F\rangle$ , it does not record any information of the incoming particle. If the WPD starts at a superposition of its on and off states  $(|O\rangle + |F\rangle) / \sqrt{2}$ , the combined state of the WPD and the quantum particle becomes

$$
\begin{array}{l} \left| \Phi (\mathbf {r}) \right\rangle = \frac {1}{2} \left[ \left(\left| \psi_ {1} (\mathbf {r}) \right\rangle \left| O _ {1} \right\rangle + \left| \psi_ {2} (\mathbf {r}) \right\rangle \left| O _ {2} \right\rangle\right) + \right. \\ \left. \left(| \psi_ {1} (\mathbf {r}) \rangle + | \psi_ {2} (\mathbf {r}) \rangle\right) | F \rangle \right] \tag {1} \\ \end{array}
$$

If we measure the interference pattern of the quantum particle in the state  $|\Phi(\mathbf{r})\rangle$ , the interference fringes given by the cross terms  $\langle \psi_1(\mathbf{r})|\psi_2(\mathbf{r})\rangle + \langle \psi_2(\mathbf{r})|\psi_1(\mathbf{r})\rangle$  appear or disappear, depending on whether we postproject the WPD's state to the vector  $|F\rangle$  or the subspace  $O$  spanned by  $|O_1\rangle$  and  $|O_2\rangle$ . This corresponds to a quantum delayed-choice experiment enabled by a quantum WPD in a classical interferometer instead of by a quantum interferometer, which is conceptually different

![](images/19377c701bc88121c30761a4b184ea3f813ac65cefa375d3731ec96c0c25676a.jpg)

![](images/d7868771a756631c946ee76cd273ef23359425681aa5c70b7bcee86f494a3f6f.jpg)

![](images/45a2af5a54757fb46d23e74e3f621d30f29095d118197d6e2a70d59070c0bc7f.jpg)  
Fig. 1. Schematic diagrams of delayed-choice experiments with a two-path interferometer. (A) Wheeler's delayed-choice thought experiment. The decision of whether to insert  $\mathrm{BS}_2$  or not is delayed until after the photon has entered the interferometer. (B) Quantum delayed-choice experiment with a quantum beam splitter. Whether the second beam splitter-like (Hadamard) operation,  $H_{2}$ , is applied or not depends on whether the ancilla is in the state  $|1\rangle_{\mathrm{a}}$  or  $|0\rangle_{\mathrm{a}}$ . When the ancilla is in a superposition of these states, the test system can simultaneously behave as a wave and a particle. (C) Quantum delayed-choice experiment with a double-slit apparatus, where a WPD is placed in front of slit 2. When the WPD is switched on, it can store the which-path information of the incoming particle, destroying the interference. If the WPD is switched off, no path information is available. When the WPD is in a superposition of its on and off states, the wave and particle behaviors are encoded in the same output state. (D) Quantum delayed-choice experiment using a Ramsey interferometer, where a cavity acts as the WPD for a qubit's evolution in its quantum state space  $\{|g\rangle, |e\rangle\}$ . When the WPD contains a coherent field  $|\alpha\rangle$ , the conditional cavity  $\pi$ -phase shift  $U$  keeps track of the which-path information in the field's phase. For the vacuum state  $|0\rangle$ , which-path information is not collected. The qubit's particle and wave behaviors can be simultaneously observed by putting the WPD in a superposition state. Two successive measurements on the WPD enable implementation of a twofold delayed-choice procedure.

![](images/1f805641109b23537338c766000134569090af9e6a43034d4a61f7f6f5b68392.jpg)

from previous quantum delayed-choice experiments (10, 12-17). This important difference leads to a distinction of the outcome: In our experiment, we can later erase the which-path information of the quantum particle (18-23) to recover the interference fringes even after we have projected the WPD to the "on" subspace  $O$ . This is achieved by measuring the WPD in the subspace  $O$  along the basis of  $|\pm \rangle = (|O_1\rangle \pm |O_2\rangle) / \sqrt{2}$ , which fully restores the interference terms  $\mathrm{Re}[\langle \psi_1(\mathbf{r})\psi_2(\mathbf{r})\rangle]$ . In contrast, if we measure the WPD in the basis of  $\{|O_1\rangle ,|O_2\rangle \}$ , the interference fringe is completely lost. Therefore, we can realize a twofold quantum delayed-choice experiment, where we have two chances to choose the wave or particle behavior of the already detected quantum system, pushing the test of wave-particle complementarity to an unprecedented level of controllability.

Previous experiments either demonstrated that the behavior of a system depends on the detecting device's configuration that can be arranged in a delayed-choice manner (4-10, 12-17) or showed that one can a posteriori choose if the system behaves as a wave or as a particle by erasing or marking the which-path information stored in the WPD (18-23). We further note that the latter feature cannot be demonstrated by the previous quantum delayed-choice experiments, where the which-path information associated with the system's particle behavior was acquired by classical detectors after the interferometer, instead of being stored in the state of another quantum system, and thus cannot be erased at a later time (10, 12-17). Our experiment, realized with a superconducting circuit, demonstrates both features with the same measurement apparatus for the first time, greatly extending the concept of quantum delayed-choice experiment. We note that the quantum delayed-choice experiment reported by Zheng et al. (17) was also performed with a superconducting circuit, where the microwave field in a resonator prepared in a cat state served as a beam splitter for the quantum state of a qubit, and the interferometer is in a superposition of being closed and open. In distinct contrast, in the

present experiment, the field in a cavity plays the role of a WPD for a qubit, and the interferometer is definitely closed; the delayed choice is enabled by the quantum superposition of the WPD. Furthermore, here, the which-path information associated with the postselected qubit's particle-like behavior is stored in the cavity, instead of being detected after the second beam splitter-like transformation so that one has the second chance to a posteriori choose if the qubit behaves as a wave or as a particle by erasing or marking the which-path information.

# RESULTS

# Observing transition between wave- and particle-like behaviors

We implement the twofold quantum delayed-choice experiment with a superconducting Ramsey interferometer. The circuit diagram is shown in Fig. 1D, which is similar to that of an MZ interferometer, with the  $\pi /2$  pulses  $\mathrm{P_1}$  and  $\mathrm{P}_2$  representing the beam splitters for the quantum state of a qubit, whose basis vectors  $|g\rangle$  and  $|e\rangle$  correspond to the two paths in the MZ interferometer. Here, each of the classical microwave pulses produces a  $\pi /2$  rotation on the Bloch sphere. The qubit, initially in the state  $|g\rangle$ , is transformed to the superposition state  $(|g\rangle + |e\rangle) / \sqrt{2}$  by  $\mathrm{P_1}$ . Then, a relative phase shift between  $|g\rangle$  and  $|e\rangle$  is introduced to get the state  $(|g\rangle + e^{i\varphi}|e\rangle) / \sqrt{2}$ , mimicking the relative phase  $\varphi$  between the two interferometer arms. The WPD is represented by a cavity in the dispersive region, with its coupling to the qubit described by the Hamiltonian

$$
H _ {e} = \hbar \chi_ {\mathrm {q s}} a ^ {\dagger} a \otimes | e \rangle \langle e | \tag {2}
$$

where  $\chi_{\mathrm{qs}}$  denotes the dispersive coupling, and  $a^+$  and  $a$  are the creation and the annihilation operators for the cavity mode. At interaction

time  $\tau = \pi /\chi_{\mathrm{qs}}$  , this coupling leads to a qubit state-dependent  $\pi$  -phase shift,  $U = e^{i\pi a^{\dagger}a\otimes |e\rangle \langle e|}$  (24-26). When the cavity is in the vacuum state  $|0\rangle$  (corresponding to the off state  $|F\rangle$  of the WPD), the qubit state is not affected by the cavity coupling operator  $U$  . After the  $\pi /2$  pulse  $\mathrm{P}_2$  , the probability for recording the qubit in the state  $|g\rangle$  is given by  $P_{g} = (1 - \cos \varphi) / 2$  , which shows a perfect interference fringe with respect to the relative phase  $\varphi$  . However, if the cavity starts in a coherent state  $|\alpha \rangle$  (corresponding to the on state  $|O\rangle$  of the WPD), the coupling operator  $U$  evolves the qubit-cavity system to the entangled state  $(|g\rangle |\alpha \rangle +e^{i\varphi}|e\rangle |-\alpha \rangle)\big{/}\sqrt{2}$  . The probability for getting the qubit in the state  $|g\rangle$  after  $\mathrm{P}_2$  is given by  $P_{g} = (1 - e^{-2|\alpha |^{2}}\cos \varphi) / 2$  . When the overlap of the two labeling states  $|\alpha \rangle$  and  $| - \alpha \rangle$  is negligible, that is,  $e^{-2|\alpha |^2} = 1$  , the interference fringe disappears. In our experiment, the cavity is prepared in a superposition cat state

$$
| \phi \rangle = \cos \theta | 0 \rangle + \sin \theta | \alpha \rangle \tag {3}
$$

and the probability for recording the qubit in state  $|g\rangle$  is given by

$$
P _ {g} \approx [ \cos^ {2} \theta (1 - \cos \varphi) + \sin^ {2} \theta ] / 2 \tag {4}
$$

where the two terms of  $P_{g}$  show the wave behavior (interference) and the particle behavior (no interference) of the superconducting qubit, respectively.

The experimental implementation is based on a three-dimensional (3D) circuit quantum electrodynamics (QED) architecture (see the Supplementary Materials for details) (27). The experiment starts with preparing the cavity in a coherent superposition of  $|0\rangle$  and  $|\alpha \rangle$ , as in Eq. 3. The experimental pulse sequence (in fig. S1) and detailed description are presented in the Supplementary Materials. We experimentally generate these states with  $\alpha = 2\sqrt{2}$ . For  $\theta = \pi /4$ , the fidelity  $F = \langle \phi |\rho_p|\phi \rangle = 0.93$ , where  $\rho_{p}$  is the density operator of the produced cavity state (measured Wigner function is shown in fig. S2). After creating the cat state, we sandwich the conditional  $\pi$ -phase shift gate  $U$  between the two  $\pi /2$  pulses  $\mathrm{P_1}$  and  $\mathrm{P}_2$  for the Ramsey interference measurement. In our experiment, the tunable phase shift  $\varphi$  is incorporated into the first  $\pi /2$  pulse  $\mathrm{P_1}$  by adjusting the phase of the corresponding microwave pulse. In Fig. 2 (A and B), we present the measured probability  $P_{g}$  as a function of  $\varphi$  for different values of  $\theta$ . As expected, the qubit exhibits a continuous transition between wave- and particle-like behavior by varying  $\theta$  that determines the initial state of the WPD.

# Verification of WPD's quantum coherence

The essence of quantum delayed-choice experiments is that the quantum coherence of the measuring device excludes the possibility of the qubit knowing the measurement choice in advance. To verify the presence of the quantum coherence between the on and off states of the WPD, we perform the Wigner tomography after the Ramsey interference experiment (24-26, 28). The Wigner function of a quantum harmonic oscillator, the quasi-probability distribution in phase space, contains all the information of the associated quantum state (29). In Fig. 3, we present the reconstructed state of the cavity without postselection on the qubit state (data conditional upon the qubit state  $|g\rangle$  and  $|e\rangle$  are presented in fig. S3) for  $\theta = \pi /4$  and  $\varphi = \pi /2$ . As expected, the measured Wigner function (Fig. 3B) exhibits interference fringes, with alternate positive and negative values between 0 and  $\alpha (-\alpha)$  in phase space, which are the signature of quantum coherence between  $|0\rangle$  and  $|\alpha \rangle$ $(| - \alpha \rangle)$ . To further characterize this coherence, we display the density matrix (Fig. 3C) in the Hilbert space obtained from the

![](images/a2de8867ada06f983c915f99a6457cb3a875278102d967ea91647f8344d05d73.jpg)  
Fig. 2. Ramsey interference pattern. (A) Observation of continuous morphing between the qubit's particle and wave behaviors. The cavity, acting as the WPD, is initially prepared in the cat state of Eq. 3 with  $\alpha = 2\sqrt{2}$ . The results show that the measured Ramsey interference pattern of the qubit, characterized by  $P_{g}$  as a function of  $\varphi$ , depends on the value of  $\theta$  that determines the state of the WPD. (B) Cuts in (A) for different values of  $\theta$ . Symbols are experimental data, which agree with the numerical simulations (solid lines) that take into account the experimental imperfections (except for measurement errors) including the qubit and cavity decoherence, the cross-Kerr interaction between the qubit and the cavity, and the self-Kerr interaction of the cavity. The SD for each measured value is less than 0.01 and not shown in the figure.

![](images/2a13e087e05f990554bc47f4f3a7ec99841399483e1275d125a9a45a6ad91739.jpg)

measured Wigner function, where each term represents the modulus of the corresponding matrix element (without including the phase). The quantum coherence between  $|0\rangle$  and  $|\alpha \rangle$  ( $|- \alpha \rangle$ ) is manifested in the off-diagonal elements  $|\rho_{n,0}|$  and  $|\rho_{0,n}|$ , which are responsible for the observed interference fringes in the Wigner function (24). These results unambiguously demonstrate that the qubit's behaviors with and without interference are observed with the same setup, where the WPD is in a quantum superposition of its on and off states.

# Twofold delayed choice

To postselect the qubit's behavior, we examine whether the cavity is filled with a coherent field or is empty by using a conditional qubit rotation. Because of the dispersive qubit-cavity coupling, the qubit's transition frequency depends on the photon number of the cavity field so that we can drive the qubit's transition conditionally on the cavity being in a specific Fock state. After the Ramsey interference experiment, we perform a  $\pi$  rotation on the qubit conditional on the cavity's vacuum state

$$
R _ {\pi , 0} ^ {Y} = \exp \left[ \frac {\pi}{2} | 0 \rangle \langle 0 | \otimes (| e \rangle \langle g | - | g \rangle \langle e |) \right]
$$

Because both  $|\alpha \rangle$  and  $|- \alpha \rangle$  are approximately orthogonal to  $|0\rangle$ , the qubit does not undergo transition for these two coherent state components. It should be noted that the coherent state  $|\alpha \rangle$  is not distinguished from  $|- \alpha \rangle$  after this procedure; that is, the which-path information is not read out. In Fig. 4A, we present the measured conditional probabilities  $P_{g;O}$  and  $P_{g;F}$  as functions of  $\varphi$ , which are defined as the probabilities for detecting the qubit in  $|g\rangle$  in the Ramsey interference experiment conditional on the measurement of the WPD's on state  $|\pm \alpha \rangle$  and off state  $|0\rangle$ , respectively. Here, the on and off states have equal weighting, that is,  $\theta = \pi /4$ .  $P_{g;F}$  manifests the qubit's interference behavior with a visibility of 0.89, whereas  $P_{g;O}$  shows almost no

![](images/48df4d8a47a621d611007cd940bf348d84c1760803022bca69d5d031adcb23cd.jpg)

![](images/6c45a761ad996cb027c2dd19fa604240fcb50818b46007c1a57fe594d8ea4be9.jpg)

![](images/1b31c9ff3bf76299d422a35e05f4673a967f30f3666a5aa7c3a9119a54495d1c.jpg)  
Fig. 3. Reconstruction of the cavity states after the second Ramsey pulse without selection on the qubit state. (A) Ideal Wigner function, (B) measured Wigner function, and (C) reconstructed density matrix for  $\alpha = 2\sqrt{2}$ ,  $\theta = \pi /4$ , and  $\varphi = \pi /2$ . To illustrate the quantum coherence between  $|0\rangle$  and  $|\alpha \rangle$  ( $|-\alpha \rangle$ ), we here only present the moduli of the density matrix elements in the Hilbert space, which are obtained from the corresponding measured Wigner function. The overlap (fidelity) between the measured density matrix  $\rho_{\mathrm{m}}$  and ideal result  $\rho_{\mathrm{i}}$ , defined as  $F = [Tr(\sqrt{\rho_{\mathrm{i}}\rho_{\mathrm{m}}\sqrt{\rho_{\mathrm{i}}}})]^{2}$ , is about 0.80; the infidelity is mainly due to the finite bandwidth of the  $\pi /2$  qubit pulses.

dependence on  $\varphi$ , as expected. Because of the imperfection of the conditional  $\pi$  pulse (fig. S4G), there is a small probability that  $|0\rangle$  is taken for  $|\pm \alpha \rangle$ ; this accounts for the residual interference effects (with a fringe contrast of 0.04) in  $P_{g;O}$ . These results demonstrate that the qubit's behavior depends on the WPD's state; the quantum coherence of the on and off states, as shown in Fig. 3, excludes any model in which the choice corresponds to a classical variable that has been known in advance.

Unlike the previous quantum delayed-choice experiments (10, 12-17), here, the which-path information associated with the qubit's particle-like behavior is not read out during the observation of the interference pattern; instead, it is stored in the field's phase. This path distinguishability can be erased: When we measure the cavity's parity, instead of distinguishing between  $|0\rangle$  and  $|\pm \alpha \rangle$ , and correlating the outcomes with the qubit's data, two complementary interference patterns appear (fig. S5). More intriguingly, the quantum erasure (18-23) can be realized even after the particle-like behavior (the red line of Fig. 4A) has been postselected, resulting in the restoration of the fringes. In Fig. 4B, we plot the measured conditional probabilities  $P_{g;O,+}$  and  $P_{g;O,-}$  as functions of  $\varphi$ , defined as the probabilities for measuring the qubit in  $|g\rangle$  after  $\mathrm{P}_2$ , conditional on the detection of even and odd parities of the WPD following the postselection of its on state, respectively. The fringe contrasts associated with  $P_{g;O,+}$  and  $P_{g;O,-}$  are 0.53 and 0.48, respectively. The imperfection of these conditional interference patterns is mainly due to

![](images/c54c495f2207ca6feb6c7717edd782ee75f2c321baad1df26fbd9af317192e9a.jpg)

![](images/32e88f0906e46c8a7c33f1087c8b341c00c38dc3d02151032e529ac531bcd499.jpg)  
Fig. 4. Conditional Ramsey interference signals by postselection on the WPD's state. (A) Probabilities  $P_{g;O}$  and  $P_{g;F}$ , as functions of  $\varphi$ , for detecting the qubit in the state  $|g\rangle$  in the Ramsey interference experiment, conditional upon the postselection of the cavity's states  $|\pm \alpha\rangle$  and  $|0\rangle$ , respectively. (B) Probabilities  $P_{g;O,+}$  and  $P_{g;O,-}$  versus  $\varphi$ , for measuring the qubit in the state  $|g\rangle$ , conditional upon the measurement of even and odd parities of the WPD following the detection of the on state, respectively. (C) Probabilities  $P_{g;O,\alpha}$  and  $P_{g;O,-\alpha}$  for detecting the qubit in the state  $|g\rangle$ , conditional upon postselecting the WPD's on state and subsequently detecting the components  $|\alpha\rangle$  and  $|-\alpha\rangle$ , respectively. The parameters are  $\alpha = 2\sqrt{2}$  and  $\theta = \pi/4$ . Dots represent experimental data, with the SD less than 0.01 and not shown, in agreement with the numerical simulations (solid lines) based on the measured device parameters.

the infidelity of the  $\pi /2$  pulses used for qubit Ramsey interference and WPD parity discrimination, which is predominantly caused by cavity photons.

On the other hand, if we choose to read out the which-path information by distinguishing between  $|\alpha \rangle$  and  $|- \alpha \rangle$ , the qubit shows no interference, as shown in Fig. 4C, where  $P_{g;O,\alpha}$  and  $P_{g;O, -\alpha}$  denote the probabilities to detect the state  $|g\rangle$  after  $\mathrm{P}_2$ , conditional on the postselection of the WPD's on state and the subsequent measurements of  $|\alpha \rangle$  and  $|- \alpha \rangle$ , respectively. These two states can be distinguished by successively performing the cavity displacement  $D(-\alpha)$ , the conditional qubit  $\pi$  rotation  $R_{\pi,0}^{Y}$ , and the qubit state measurement. We note that the thus obtained  $|- \alpha \rangle$  state is mixed up with the residual vacuum, resulting in a slight oscillation in  $P_{g;O, -\alpha}$  with a contrast of 0.07. This fringe contrast can be further reduced by performing additional operations  $D(\alpha)$  and  $R_{\pi,0}^{Y}$  and then measuring the qubit state to remove the residual vacuum. The deviation of  $P_{g;O, -\alpha}$  from  $^1 / _2$  is mainly due to the qubit energy decay (see the Supplementary Materials).

The delayed-choice quantum eraser embedded in the quantum delayed-choice experiment is only enabled by using the quantum properties of the WPD, significantly extending the concept of delayed-choice experiment. The twofold delayed-choice procedure provides a clear demonstration that the behavior with or without interference is not a realistic property of the test system: It depends not only on the delayed choice of the WPD's state but also on how we later measure the WPD and correlate the outcomes with the data of the test system.

# DISCUSSION

In summary, we have proposed a twofold quantum delayed-choice experiment that is enabled by using a WPD prepared in a superposition of its on and off states. We implemented the experiment in circuit QED, observing both behaviors with and without interference for a superconducting qubit in the same experiment by using a cavity in a cat state as the WPD. We confirmed the existence of quantum coherence between the on and the off states of the WPD, excluding interpretations of the results based on classical models. The quantum properties of the WPD allow erasure of the which-path information associated with the postselected particle-like behavior, implementing the first twofold delayed-choice procedure. Our results show whether the qubit behaves as a wave or as a particle depends not only on the configuration of the measuring device, which can be chosen even after the qubit has been detected, but also on whether one a posteriori erases or marks the which-path information, unambiguously demonstrating that the wave- or particle-like behavior of a quantum system is not a reality.

# MATERIALS AND METHODS

Our experiment was implemented with a 3D circuit QED architecture (27), as shown in fig. S6, where a single transmon qubit in a waveguide trench was dispensively coupled to two 3D cavities (25, 26): One cavity served as the storage cavity, and the other was used to read out the qubit's state. The transmon qubit was fabricated on a  $c$ -plane sapphire  $(\mathrm{Al}_2\mathrm{O}_3)$  substrate with a double-angle evaporation of aluminum after a single electron-beam lithography step. The qubit had a transition frequency  $\omega_{\mathrm{q}} / 2\pi = 5.577\mathrm{GHz}$  with an anharmonicity of  $\alpha_{\mathrm{q}} / 2\pi = (\omega_{\mathrm{ge}} - \omega_{\mathrm{ef}}) / 2\pi = 246\mathrm{MHz}$ , an energy relaxation time of  $T_{1} = 9.5~\mu \mathrm{s}$ , a Ramsey time of  $T_{2}^{*} = 7.5~\mu \mathrm{s}$ , and a pure dephasing time of  $T_{\phi} = 12.4~\mu \mathrm{s}$ .

Both the storage and readout cavities were made of aluminum alloy 6061 with a frequency of 8.229 and  $7.292\mathrm{GHz}$ , respectively. The photon lifetimes in the storage and readout cavities were  $\tau_{\mathrm{s}} = 66~\mu \mathrm{s}$  and  $\tau_{\mathrm{r}} = 44$  ns, respectively. The dispersive coupling between the qubit and the storage (readout) cavity was  $\chi_{\mathrm{qs}} / 2\pi = -1.64\mathrm{MHz}$ $(\chi_{\mathrm{qr}} / 2\pi = -4.71\mathrm{MHz})$ . The storage cavity acted as the WPD for the qubit in the Hilbert space. During the unitary evolution of the system combined by the qubit and the storage cavity, the readout cavity remained in the ground state, and we discarded it when describing the quantum state of the system.

The sample was placed in a cryogen-free dilution refrigerator at a base temperature of about  $10\mathrm{mK}$ . Even at the lowest base temperature, the qubit was measured to have a probability about  $8.5\%$  of being populated in the excited state  $|e\rangle$  in the steady state. The exact source for this excitation is unknown; it may be caused by stray infrared photons or other background noise leaking into the cavity. This excitation can be removed through an initialization measurement of the qubit state by postselecting the projection of the system onto the ground state  $|\mathrm{g}\rangle$  (see the Supplementary Materials) (30).

The schematic of the measurement setup is shown in fig. S7. We applied a Josephson parametric amplifier (JPA) (31, 32) operating in a double-pumped mode (red enclosed part in fig. S7 shows the biasing circuit) (33, 34) as the first stage of amplification between the readout cavity at base and the high-electron-mobility-transistor amplifier at  $4\mathrm{K}$ . To minimize pump leakage into the readout cavity for a longer  $T_{\phi}$  time, we typically operated the JPA in a pulsed mode. This JPA allowed for a high-fidelity and quantum non-demolition single-shot readout of the qubit state (see section S3).

# SUPPLEMENTARY MATERIALS

Supplementary material for this article is available at http://advances.sciencemag.org/cgi/ content/full/3/5/e1603159/DC1

section S1. Pulse sequence and parameters

section S2. The cavity's cat state preparation and Wigner tomography section S3. Readout properties

section S4. Quantum erasure

section S5. Analysis of errors in marking the which-path information

fig. S1. Schematic of the pulse sequences in the experiments.

fig. S2. Tomography of initial cavity state.

fig. S3. Reconstruction of the cavity states after the second Ramsey pulse.

fig. S4. Readout properties.

fig. S5. Conditional Ramsey interference patterns based on the cavity parity measurement.

fig. S6. Experimental device.

fig. S7. Schematic of the measurement setup. References (35, 36)

# REFERENCES AND NOTES

1. N. Bohr, in Quantum Theory and Measurement, J. A. Wheeler, W. H. Zurek, Eds. (Princeton Univ. Press, 1984), pp. 9-49.  
2. B.-G. Englert, Fringe visibility and which-way information: An inequality. Phys. Rev. Lett. 77, 2154-2157 (1996).  
3. S. Durr, T. Nonn, G. Rempe, Origin of quantum-mechanical complementarity probed by a 'which-way' experiment in an atom interferometer. Nature 395, 33-37 (1998).  
4. J. A. Wheeler, in Quantum Theory and Measurement, J. A. Wheeler, W. H. Zurek, Eds. (Princeton Univ. Press, 1984), pp. 182-213.  
5. X.-s. Ma, J. Kofler, A. Zeilinger, Delayed-choice gedanken experiments and their realizations. Rev. Mod. Phys. 88, 015005 (2016).  
6. T. Hellmuth, H. Walther, A. Zajonc, W. Schleich, Delayed-choice experiments in quantum interference. Phys. Rev. A 35, 2532-2541 (1987).  
7. B. J. Lawson-Daku, R. Asimov, O. Gorceix, C. Miniatura, J. Robert, J. Baudon, Delayed choices in atom Stern-Gerlach interferometry. Phys. Rev. A 54, 5042-5047 (1996).  
8. V. Jacques, E. Wu, F. Grosshans, F. Treussart, P. Grangier, A. Aspect, J.-F. Roch, Experimental realization of Wheeler's delayed-choice gedanken experiment. Science 315, 966-968 (2007).  
9. A. G. Manning, R. I. Khakimov, R. G. Dall, A. G. Truscott, Wheeler's delayed-choice gedanken experiment with a single atom. Nat. Phys. 11, 539-542 (2015).  
10. R. Ionicioui, D. R. Terno, Proposal for a quantum delayed-choice experiment. Phys. Rev. Lett. 107, 230406 (2011).  
11. M. A. Nielsen, I. L. Chuang, Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
12. J.-S. Tang, Y.-L. Li, X.-Y. Xu, G.-Y. Xiang, C.-F. Li, G.-C. Guo, Realization of quantum Wheeler's delayed-choice experiment. Nat. Photon. 6, 600-604 (2012).  
13. A. Peruzzo, P. Shadbolt, N. Brunner, S. Popescu, J. L. O'Brien, A quantum delayed-choice experiment. Science 338, 634-637 (2012).  
14. F. Kaiser, T. Coudreau, P. Milman, D. B. Ostrowsky, S. Tanzilli, Entanglement-enabled delayed-choice experiment. Science 338, 637-640 (2012).  
15. S. S. Roy, A. Shukla, T. S. Mahesh, NMR implementation of a quantum delayed-choice experiment. Phys. Rev. A 85, 022109 (2012).  
16. R. Auccase, R. M. Serra, J. G. Filgueiras, R. S. Sarhour, I. S. Oliveira, L. C. Celeri, Experimental analysis of the quantum complementarity principle. Phys. Rev. A 85, 032121 (2012).  
17. S.-B. Zheng, Y.-P. Zhong, K. Xu, Q.-J. Wang, H. Wang, L.-T. Shen, C.-P. Yang, J. M. Martinis, A. N. Cleland, S.-Y. Han, Quantum delayed-choice experiment with a beam splitter in a quantum superposition. Phys. Rev. Lett. 115, 260403 (2015).  
18. M. O. Scully, K. Druhl, Quantum eraser: A proposed photon correlation experiment concerning observation and "delayed choice" in quantum mechanics. Phys. Rev. A 25, 2208-2213 (1982).  
19. M. O. Scully, B.-G. Englert, H. Walther, Quantum optical tests of complementarity. Nature 351, 111-116 (1991).  
20. C. C. Gerry, Complementarity and quantum erasure with dispersive atom-field interactions. Phys. Rev. A 53, 1179-1182 (1996).  
21. T. J. Herzog, P. G. Kwiat, H. Weinfurter, A. Zeilinger, Complementarity and the quantum eraser. Phys. Rev. Lett. 75, 3034-3037 (1995).  
22. Y.-H. Kim, R. Yu, S. P. Kulik, Y. Shih, M. O. Scully, Delayed "choice" quantum eraser. Phys. Rev. Lett. 84, 1-5 (2000).  
23. X.-S. Ma, J. Kofler, A. Qarry, N. Tetik, T. Scheidl, R. Ursin, S. Ramelow, T. Herbst, L. Ratschbacher, A. Fedrizzi, T. Jennewein, A. Zeilinger, Quantum erasure with causally disconnected choice. Proc. Natl. Acad. Sci. U.S.A. 110, 1221-1226 (2013).

24. S. Deleglise, I. Dotsenko, C. Sayrin, J. Bernu, M. Brune, J.-M. Raimond, S. Haroche, Reconstruction of non-classical cavity field states with snapshots of their decoherence. Nature 455, 510-514 (2008).  
25. B. Vlastakis, G. Kirchmair, Z. Lehtas, S. E. Nigg, L. Frunzio, S. M. Girvin, M. Mirrahimi, M. H. Devoret, R. J. Schoelkopf, Deterministically encoding quantum information using 100-photon Schrödinger cat states. Science 342, 607-610 (2013).  
26. L. Sun, A. Petrenko, Z. Leghtas, B. Vlastakis, G. Kirchmair, K. M. Sliwa, A. Narla, M. Hatridge, S. Shankar, J. Blumoff, J. Blumoff, L. Frunzio, M. Mirrahimi, M. H. Devoret, R. J. Schoelkopf, Tracking photon jumps with repeated quantum non-demolition parity measurements. Nature 511, 444-448 (2014).  
27. H. Paik, D. I. Schuster, L. S. Bishop, G. Kirchmair, G. Catelani, A. P. Sears, B. R. Johnson, M. J. Reagan, L. Frunzio, L. I. Glazman, S. M. Girvin, M. H. Devoret, R. J. Schoelkopf, Observation of high coherence in Josephson junction qubits measured in a three-dimensional circuit QED architecture. Phys. Rev. Lett. 107, 240501 (2011).  
28. L. G. Lutterbach, L. Davidovich, Method for direct measurement of the Wigner function in cavity QED and ion traps. Phys. Rev. Lett. 78, 2547-2550 (1997).  
29. W. P. Schleich, Quantum Optics in Phase Space (Wiley-VCH, 2001).  
30. D. Riste, J. G. van Leeuwen, H.-S. Ku, K. W. Lehnert, L. DiCarlo, Initialization by measurement of a superconducting quantum bit circuit. Phys. Rev. Lett. 109, 050507 (2012).  
31. M. Hatridge, R. Vijay, D. H. Slichter, J. Clarke, I. Siddiqi, Dispersive magnetometry with a quantum limited SQUID parametric amplifier. Phys. Rev. B 83, 134501 (2011).  
32. T. Roy, S. Kundu, M. Chand, A. M. Vadiraj, A. Ranadive, N. Nehra, M. P. Patankar, J. Aumentado, A. A. Clerk, R. Vijay, Broadband parametric amplification with impedance engineering: Beyond the gain-bandwidth product. Appl. Phys. Lett. 107, 262601 (2016).  
33. A. Kamal, A. Marblestone, M. H. Devoret, Signal-to-pump back action and self-oscillation in double-pump Josephson parametric amplifier. Phys. Rev. B 79, 184301 (2009).  
34. K. W. Murch, S. J. Weber, C. Macklin, I. Siddiqi, Observing single quantum trajectories of a superconducting quantum bit. Nature 502, 211-214 (2013).

35. P. Bertet, A. Auffeves, P. Maioli, S. Osnaghi, T. Meunier, M. Brune, J. M. Raimond, S. Haroche, Direct measurement of the Wigner function of a one-photon Fock state in a cavity. Phys. Rev. Lett. 89, 200402 (2002).  
36. F. Motzoi, J. M. Gambetta, P. Rebentrost, F. K. Wilhelm, Simple pulses for elimination of leakage in weakly nonlinear qubits. Phys. Rev. Lett. 103, 110501 (2009).

Acknowledgments: We thank M. H. Devoret for helpful discussions. Funding: This work was supported by the Ministry of Science and the Ministry of Education of China through its grant to Tsinghua University, the National Natural Science Foundation of China under grants 11474177 and 11674060, the Major State Basic Research Development Program of China under grant 2012CB921601, and the 1000 Youth Fellowship program in China. R.V. acknowledges funding from the Department of Atomic Energy, Government of India. Author contributions: K.L. performed the experiment and analyzed the data with the assistance of Y.X., W.W., and L.S. Y.X. fabricated the device. W.W. performed numerical simulations. L.S. directed the experiment. S.-B.Z. proposed the theoretical scheme. T.R., S.K., M.C., A.R., and R.V. provided the JPA. Y.S. contributed to device fabrication. S.-B.Z., L.D., and L.S. wrote the manuscript with feedback from all authors. Competing interests: The authors declare that they have no competing interests. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper may be requested from the authors.

Submitted 13 December 2016

Accepted 3 March 2017

Published 5 May 2017

10.1126/sciadv.1603159

Citation: K. Liu, Y. Xu, W. Wang, S.-B. Zheng, T. Roy, S. Kundu, M. Chand, A. Ranadive, R. Vijay, Y. Song, L. Duan, L. Sun, A twofold quantum delayed-choice experiment in a superconducting circuit. Sci. Adv. 3, e1603159 (2017).

This article is publisher under a Creative Commons license. The specific license under which this article is published is noted on the first page.

For articles published under CC BY licenses, you may freely distribute, adapt, or reuse the article, including for commercial purposes, provided you give proper attribution.

For articles published under CC BY-NC licenses, you may distribute, adapt, or reuse the article for non-commercial purposes. Commercial use requires prior permission from the American Association for the Advancement of Science (AAAS). You may request permission by clicking here.

The following resources related to this article are available online at http://advances.sciencemag.org. (This information is current as of May 7, 2017):

Updated information and services, including high-resolution figures, can be found in the online version of this article at: http://advances.sciencemag.org/content/3/5/e1603159.full

Supporting Online Material can be found at: http://advances.sciencemag.org/content/suppl/2017/05/01/3.5.e1603159.DC1

This article cites 32 articles, 5 of which you can access for free at: http://advances.sciencemag.org/content/3/5/e1603159#BIBL