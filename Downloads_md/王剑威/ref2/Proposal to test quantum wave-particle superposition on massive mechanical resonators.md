# ARTICLE OPEN

# Proposal to test quantum wave-particle superposition on massive mechanical resonators

Wei Qin $^{1,2}$ , Adam Miranowicz $^{1,3}$ , Guilu Long $^{4,5,6}$ , J. Q. You $^{2,7}$  and Franco Nori $^{1,8}$

We present and analyze a proposal for a macroscopic quantum delayed-choice experiment with massive mechanical resonators. In our approach, the electronic spin of a single nitrogen-vacancy impurity is employed to control the coherent coupling between the mechanical modes of two carbon nanotubes. We demonstrate that a mechanical phonon can be in a coherent superposition of wave and particle, thus exhibiting both behaviors at the same time. We also discuss the mechanical noise tolerable in our proposal and predict a critical temperature below which the morphing between wave and particle states can be effectively observed in the presence of environment-induced fluctuations. Furthermore, we describe how to amplify single-phonon excitations of the mechanical-resonator superposition states to a macroscopic level, via squeezing the mechanical modes. This approach corresponds to the phase-covariant cloning. Therefore, our proposal can serve as a test of macroscopic quantum superpositions of massive objects even with large excitations. This work, which describes a fundamental test of the limits of quantum mechanics at the macroscopic scale, would have implications for quantum metrology and quantum information processing.

npj Quantum Information (2019)5:58; https://doi.org/10.1038/s41534-019-0172-9

# INTRODUCTION

Wave-particle duality lies at the heart of quantum physics. According to Bohr's complementarity principle, a quantum system may behave either as a wave or as a particle depending on the measurement apparatus, and both behaviors are never observed simultaneously. This can be well demonstrated via a single photon Mach-Zehnder interferometer, as depicted in Fig. 1a. An incident photon is split, at an input beam-splitter  $\mathrm{BS}_1$ , into an equal superposition of being in the upper and lower paths. This is followed by a phase shift  $\phi$  in the upper path. At the output beam-splitter  $\mathrm{BS}_2$ , the paths are recombined and the detection probability in the detector  $\mathrm{D}_1$  or  $\mathrm{D}_2$  depends on the phase  $\phi$ , heralding the wave nature of a single photon. If, however,  $\mathrm{BS}_2$  is absent, the photon is detected with probability  $1/2$  in each detector, and thus, shows its particle nature. In Wheeler's delayed-choice experiment, the decision of whether or not to insert  $\mathrm{BS}_2$  is randomly made after a photon is already inside the interferometer. The arrangement rules out a hidden-variable theory, which suggests that the photon may determine, in advance, which behavior, wave or particle, to exhibit through a hidden variable. Recently, a quantum delayed-choice experiment, where  $\mathrm{BS}_2$  is engineered to be in a quantum superposition of being present and absent, has been proposed. Such a version allows a single system to be in a quantum superposition of a wave and a particle, so that both behaviors can be observed in a single measurement apparatus at the same time. This extends the conventional boundary of Bohr's complementarity principle. The quantum delayed-choice experiment has already been implemented in nuclear magnetic resonance, optics, and

superconducting circuits. $^{24,25}$  However, all these experiments were performed essentially at the microscopic scale.

Here, as a step in the macroscopic test for a coherent wave-particle superposition on massive objects, we propose and analyze an approach for a mechanical quantum delayed-choice experiment. Mechanical systems are not only being explored now for potential quantum technologies,[26,27] but they also have been considered as a promising candidate to test fundamental principles in quantum theory.[28] In this manuscript, we demonstrate that, similar to a single photon, the mechanical phonon can be prepared in a quantum superposition of both a wave and a particle. The basic idea is to use a single nitrogen-vacancy (NV) center in diamond to control the coherent coupling between two separated carbon nanotubes (CNTs).[29,30] We focus on the electronic ground state of the NV center, which is a spin  $S = 1$  triplet with a zero-field splitting  $D \simeq 2\pi \times 2.87 \mathrm{GHz}$  between spin states  $|0\rangle$  and  $|\pm 1\rangle$  [see Fig. 1b]. If the spin is in  $|0\rangle$ , the mechanical modes are decoupled, and otherwise are coupled. Moreover, the mechanical noise tolerated by our proposal is evaluated and we show a critical temperature, below which the coherent signal is resolved.

# RESULTS

# Physical model

We consider a hybrid system $^{31,32}$  consisting of two (labelled as  $k = 1, 2$ ) parallel CNTs and an NV electronic spin, as illustrated in Fig. 1c. The CNTs, both suspended along the  $\hat{x}$ -direction, carry dc currents  $I_{1}$  and  $I_{2}$ , respectively, while the spin is placed between

![](images/339a0f805fd6097607d6a58a1566ec43235d43d4d83a257bd30fb0738b590e9d.jpg)

![](images/4c92c085668a912e1a007f3334d9bac09e9ec21e9a39ce01cd71c070acda388d.jpg)

![](images/3475f2908ce279ee43c5e063a6818418ca7e72fa6cedbd4475c664a2913c5639.jpg)  
Fig. 1 a Demonstration of the wave-particle duality using a Mach-Zehnder interferometer. A single photon is first split at the input beam-splitter  $\mathrm{BS}_1$ , then undergoes a phase shift  $\phi$  and finally is observed at detectors  $\mathrm{D}_1$  and  $\mathrm{D}_2$ . The photon behaves as a wave if the output beam-splitter  $\mathrm{BS}_2$  is inserted, or as a particle if  $\mathrm{BS}_2$  is removed. In quantum delayed-choice experiments,  $\mathrm{BS}_2$  is set in a quantum superposition of being present and absent, and consequently, the photon can simultaneously exhibit its wave and particle nature. b Level structure of the driven NV spin in the electronic ground state. Here we have assumed that the Zeeman splitting between the spin states  $|\pm 1\rangle$  is eliminated by applying an external field. c Schematic representation of a mechanical quantum delayed-choice experiment with an NV electronic spin and two CNTs. The mechanical vibrations of the CNTs are completely decoupled or coherently coupled, depending, respectively, on whether or not the intermediate spin is in the spin state  $|0\rangle$ , with the dc current  $I_{k}$  through the kth CNT, and the distance  $d_{k}$  between the spin and the kth CNT

them, at a distance  $d_{1}$  from the first CNT and at a distance  $d_{2}$  from the second CNT. When vibrating along the  $\hat{y}$ -direction, the CNTs can parametrically modulate the Zeeman splitting of the intermediate spin through the magnetic field, yielding a magnetic coupling to the spin. $^{33-37}$  For simplicity, below we assume that the CNTs are identical such that they have the same vibrational frequency  $\omega_{m}$  and the same vibrational mass  $m$ . The mechanical vibrations are modelled by quantized harmonic oscillators with a Hamiltonian

$$
H _ {\mathrm {m v}} = \sum_ {k = 1, 2} \hbar \omega_ {m} b _ {k} ^ {\dagger} b _ {k}, \tag {1}
$$

where  $b_{k}(b_{k}^{\dagger})$  denotes the phonon annihilation (creation) operator. The Hamiltonian characterizing the coupling of the mechanical modes to the spin is

$$
H _ {\text {i n t}} = \sum_ {k = 1, 2} \hbar g _ {k} S _ {z} q _ {k}, \tag {2}
$$

where  $S_{z} = |+1\rangle \langle +1| - |-1\rangle \langle -1|$  is the  $z$ -component of the spin,  $q_{k} = b_{k} + b_{k}^{\dagger}$  represents the canonical phonon position operator, and  $g_{k} = \mu_{B}g_{s}y_{\mathrm{zp}}G_{k} / \hbar$  refers to the Zeeman shift corresponding to the zero-point motion  $y_{\mathrm{zp}} = [\hbar /(2m\omega_{m})]^{1 / 2}$ . Here,  $\mu_{B}$  is the Bohr magneton,  $g_{s}\simeq 2$  is the Landé factor, and  $G_{k} = \mu_{0}I_{k} / (2\pi d_{k}^{2})$  is the magnetic-field gradient, where  $\mu_0$  is the vacuum permeability. In order to mediate the coherent coupling of the CNT mechanical modes through the spin, we apply a time-dependent magnetic

field

$$
B _ {x} (t) = B _ {0} \cos \left(\omega_ {0} t\right), \tag {3}
$$

with amplitude  $B_0$  and frequency  $\omega_0$ , along the  $\hat{x}$ -direction, to drive the  $|0\rangle \rightarrow |\pm 1\rangle$  transitions with Rabi frequency

$$
\Omega = \frac {\mu_ {B} g _ {s} B _ {0}}{2 \sqrt {2} \hbar}. \tag {4}
$$

We apply a static magnetic field

$$
B _ {z} = \sum_ {k = 1, 2} (- 1) ^ {k} d _ {k} G _ {k}, \tag {5}
$$

along the  $\hat{z}$ -direction to eliminate the Zeeman splitting between the spin states  $|\pm 1\rangle$ .<sup>36</sup> This causes the same Zeeman shift,

$$
\Delta = \Delta_ {-} + \frac {3 \Omega^ {2}}{\Delta_ {+}}, \tag {6}
$$

where  $\Delta_{\pm} = D \pm \omega_0$ , to be imprinted on  $|\pm 1\rangle$ , and a coherent coupling, of strength  $\Omega^2 / \Delta_{+}$ , between them, as shown in Fig. 1b. We can, thus, introduce a dark state

$$
\left| D \right\rangle = \left(\left| + 1 \right\rangle - \left| - 1 \right\rangle\right) / \sqrt {2}, \tag {7}
$$

and a bright state

$$
\left| B \right\rangle = \left(\left| + 1 \right\rangle + \left| - 1 \right\rangle\right) / \sqrt {2}, \tag {8}
$$

with an energy splitting  $\simeq 2\Omega^2 /\Delta_{+}$ . In this case, the spin state  $|0\rangle$  is decoupled from the dark state, and is dressed by the bright state. Under the assumption of  $\Omega /\Delta \ll 1$ , the dressing will only increase the energy splitting between the dark and bright states to

$$
\omega_ {q} \simeq 2 \Omega^ {2} \left(\frac {1}{\Delta} + \frac {1}{\Delta_ {+}}\right). \tag {9}
$$

This yields a spin qubit with  $|D\rangle$  as the ground state and  $|B\rangle$  as the exited state. The spin-CNT coupling Hamiltonian is accordingly transformed to

$$
H _ {\text {i n t}} \simeq \sum_ {k = 1, 2} \hbar g _ {k} \sigma_ {x} q _ {k}, \tag {10}
$$

where  $\sigma_{x} = \sigma_{+} + \sigma_{-}$ , with  $\sigma_{-} = |D\rangle \langle B|$  and  $\sigma_{+} = \sigma_{-}^{\dagger}$ . When we further restrict our discussion to a dispersive regime  $\omega_{q} \pm \omega_{m} \gg |g_{k}|$ , the spin qubit becomes a quantum data bus, allowing for mechanical excitations to be exchanged between the CNTs. By using a time-averaging treatment,[38,39] the unitary dynamics of the system is then described by an effective Hamiltonian (see Supplementary Section 1 for a detailed derivation),  $H_{\mathrm{eff}} = H_{\mathrm{cnt}} \otimes \sigma_{z}$ , where

$$
H _ {\text {c n t}} = \frac {2 \hbar \omega_ {q}}{\omega_ {q} ^ {2} - \omega_ {m} ^ {2}} \left[ \sum_ {k = 1, 2} g _ {k} ^ {2} b _ {k} ^ {\dagger} b _ {k} + g _ {1} g _ {2} \left(b _ {1} b _ {2} ^ {\dagger} + \mathrm {H . c .}\right) \right], \tag {11}
$$

and  $\sigma_z = |B\rangle\langle B| - |D\rangle\langle D|$ . The Hamiltonian  $H_{\mathrm{cnt}}$  includes a coherent spin-mediated CNT-CNT coupling in the beam-splitter form, which is conditioned on the spin state. Here, we neglect the direct CNT-CNT coupling much smaller than the spin-mediated coupling, as is described in Supplementary Section 1. Furthermore, we find that the decoupling of one CNT from the spin gives rise to a spin-induced shift of the vibrational resonance of the other CNT. Hence, the dynamics described by  $H_{\mathrm{eff}}$  can be used to implement controlled Hadamard and phase gates.

Quantum delayed-choice experiment with mechanical resonators Let us first discuss the Hadamard gate. Having  $I_{k} = I$  and  $d_{k} = d$  gives a symmetric coupling  $g_{k} = g$ , and a mechanical beam-splitter coupling of strength

$$
J = \frac {2 g ^ {2} \omega_ {q}}{\omega_ {q} ^ {2} - \omega_ {m} ^ {2}}. \tag {12}
$$

Unitary evolution for a time  $\tau_0 = \pi /(4J)$  then leads to

$$
b _ {1} \left(\tau_ {0}\right) = \left(b _ {1} - i b _ {2}\right) / \sqrt {2}, \tag {13}
$$

$$
b _ {2} \left(\tau_ {0}\right) = \left(b _ {2} - i b _ {1}\right) / \sqrt {2}. \tag {14}
$$

For the phase gate, we can turn off the current, for example, of the second CNT, so that  $g_{1} = g$  and  $g_{2} = 0$ . In this case, a dispersive shift of  $\simeq J$  is imprinted into the vibrational resonance of the first CNT, which in turn introduces a relative phase  $\phi \simeq J\tau_{1}$  after a time  $\tau_{1}$  under unitary evolution. Note that, here, both Hadamard and phase gates are controlled operations conditional on the spin state, as mentioned before. The two gates and their timing errors are analyzed in detail in the Supplementary Section 2.

We now turn to the quantum delayed-choice experiment with the macroscopic CNTs. We assume that the hybrid system is initially prepared in the state

$$
\left| \Psi \right\rangle_ {i} = \left(\boldsymbol {b} _ {1} ^ {\dagger} \otimes \mathcal {I} _ {2} | \mathrm {v a c} \rangle\right) \otimes | D \rangle , \tag {15}
$$

where  $|\mathrm{vac}\rangle$  refers to the phonon vacuum and  $\mathcal{I}_k$  is the identity operator for the kth CNT. After the initialization, the currents are tuned to be  $I_{k} = I$ , to drive the system for a time  $\tau_0$ , and the resulting Hadamard operation splits the single phonon into an equal superposition across both CNTs. Then, we turn off  $I_{2}$  for a time  $\tau_{1}$  to accumulate a relative phase between the CNTs. While achieving the desired phase  $\phi$ , we turn on  $I_{2}$  following a spin single-qubit rotation  $|D\rangle \rightarrow \cos (\varphi)|0\rangle +\sin (\varphi)|D\rangle^{40 - 42}$  with  $\varphi$  a rotation angle, and hold for another  $\tau_0$  for a Hadamard operation. Therefore, this Hadamard gate is in a quantum superposition of being both present and absent. The three steps correspond, respectively, to the input beam-splitter, the phase shifter and the quantum output beam-splitter acting in sequence on a single photon in the Mach-Zehnder interferometer, as shown in Fig. 1a. The final state of the system therefore becomes

$$
| \Psi \rangle_ {f} = \cos (\varphi) | \text {p a r t i c l e} \rangle | 0 \rangle + \sin (\varphi) | \text {w a v e} \rangle | D \rangle , \tag {16}
$$

where

$$
\left| \text {p a r t i c l e} \right\rangle = \frac {1}{\sqrt {2}} \left[ \exp (i \phi) b _ {1} ^ {\dagger} + i b _ {2} ^ {\dagger} \right] | \mathrm {v a c} \rangle , \tag {17}
$$

$$
| \text {w a v e} \rangle = \frac {1}{2} \left\{\left[ \exp (i \phi) - 1 \right] b _ {1} ^ {\dagger} + i \left[ \exp (i \phi) + 1 \right] b _ {2} ^ {\dagger} \right\} | \text {v a c} \rangle , \tag {18}
$$

describe the particle and wave behaviors, respectively. The coherent evolution of the system is given in more detail in Supplementary Section 2. We find from Eq. (16) that the mechanical phonon is in a quantum superposition of both a wave and a particle, and thus can exhibit both characteristics simultaneously. By applying microwave pulse sequences to tune the rotation angle  $\varphi$ , an arbitrary wave-particle superposition state can be prepared on demand. In the case of  $\varphi = 0$ , the single phonon behaves completely as a particle, but as a wave for  $\varphi = \pi/2$ . The morphing between them can also be observed by tuning the rotation angle  $\varphi$ . The probability,  $P_{k}$ , of finding a phonon in the  $k$ th CNT is given by

$$
P _ {k} = \frac {1}{2} + (- 1) ^ {k} \frac {1}{2} \sin^ {2} (\varphi) \cos (\phi), \tag {19}
$$

which includes two physical contributions, one from the particle nature and the other from the wave nature. Note that the spin in a mixed state  $\cos^2 (\varphi)|0\rangle \langle 0| + \sin^2 (\varphi)|D\rangle \langle D|$  is capable of reproducing the same measured statistics as in Eq. (19).<sup>11</sup> Thus, in order to exclude the classical interpretation and prove the existence of the coherent wave-particle superposition, the quantum coherence between the states  $|0\rangle$  and  $|D\rangle$  should be verified.<sup>19,20,24,25</sup> Experimentally, such a verification can be implemented by performing quantum state tomography to show all elements of the density matrix of the spin.<sup>42</sup>

Next, we consider how to initialize and measure the mechanical system. Initially, the NV spin needs to be in the state  $|D\rangle$  (i.e., the ground state of the spin qubit), one CNT, e.g., the first CNT, needs to be in its single-phonon state, and the other CNT, e.g., the second CNT, needs to be in its vacuum state. To prepare such an initial state, we can begin with an arbitrary state  $\rho_{\mathrm{ini}} = \rho_1\otimes \rho_2\otimes$ $\rho_{\mathrm{spin}}$  where  $\rho_{k}$ $(k = 1,2)$  and  $\rho_{\mathrm{spin}}$  are the density matrices of the kth CNT resonator and the spin, respectively. One can apply a  $532~\mathrm{nm}$  laser pulse to initialize the spin qubit in the state  $|0\rangle$ , and then apply a microwave  $\pi /2$ -pulse to it, to obtain the superposition state  $\frac{1}{\sqrt{2}}(|0\rangle + | - 1\rangle)$ , which is followed by a microwave  $\pi$ -pulse to obtain the spin-qubit excited state  $|B\rangle$ . By using the sideband-cooling technique,[43-47] the CNT resonators can be cooled down to their quantum ground state, i.e., the acoustic vacuum  $|\mathrm{vac}\rangle$ . For example, one can couple an auxiliary qubit with a large spontaneous-emission rate to the CNT resonators.[48] Once the mechanical ground state is achieved, one can tune the spin-qubit transition frequency  $\omega_{q}$  to be close to the CNT resonance frequency  $\omega_{m}$ , such that the spin-CNT coupling is then approximately given by a Jaynes-Cummings-type Hamiltonian

$$
H _ {\text {i n t}} \simeq \hbar g \left(\sigma_ {+} b _ {1} + \sigma_ {-} b _ {1} ^ {\dagger}\right). \tag {20}
$$

When acting for a time equal to  $\pi/(2g)$ , such a Hamiltonian can, with the spin qubit in the excited state  $|B\rangle$ , transfer a mechanical excitation to the left CNT.49 Meanwhile, the spin qubit goes to its ground state  $|D\rangle$ . The desired initial state  $|\Psi\rangle_i = \left(b_1^\dagger \otimes \mathcal{I}_2|\mathrm{vac}\rangle\right) \otimes |D\rangle$  is then obtained. For the phonon number measurement, we still need  $\omega_q \simeq \omega_m$  as in the initialization, but the spin qubit is required to be in the ground state  $|D\rangle$ . In this situation, the Rabi frequency between the spin and the mechanical resonator depends on the number of phonons in the resonator.49-53 Thus by directly measuring the occupation probability of  $|B\rangle$ , the phonon number in each CNT can be obtained. The measurement of the spin state is enabled by the different fluorescence of the states  $|0\rangle$  and  $|\pm 1\rangle$ .54 To measure the state of the spin qubit, one can first apply a microwave  $\pi$  pulse to map  $|D\rangle \rightarrow \frac{1}{\sqrt{2}}(|0\rangle - | - 1\rangle)$  and  $|B\rangle \rightarrow \frac{1}{\sqrt{2}}(|0\rangle + | - 1\rangle)$ , and then apply a microwave  $\pi/2$  pulse to map  $\frac{1}{\sqrt{2}}(|0\rangle - | - 1\rangle) \rightarrow |0\rangle$  and  $\frac{1}{\sqrt{2}}(|0\rangle + | - 1\rangle) \rightarrow | - 1\rangle$ . By measuring the Rabi oscillations between the states  $|0\rangle$  and  $| - 1\rangle$  according to spin-state-dependent fluorescence,55 one can read-out the spin-qubit state. If one employs the repetitive-readout technique with auxiliary nuclear spins, the readout fidelity can be further improved.56

# Mechanical noise

Before discussing the mechanical noise, we need to analyze the total operation time,  $\tau_{T} = 2\tau_{0} + \tau_{1}$ , required for our quantum delayed-choice experiment. Note that during  $\tau_{T}$ , we have neglected the spin single-qubit operation time due to the driving pulse length  $\sim$ ns.[57,58] Since  $0 \leq \tau_{1} \leq 2\pi / J$ , we focus on the maximum  $\tau_{T}$ :  $\tau_{T}^{\max} = 5\pi / (2J)$ . A modest spin-CNT coupling  $g / 2\pi = 100\mathrm{kHz}$ , which can be obtained by tuning the current  $I$  and the distance  $d$  (see Supplementary Section 1), is able to mediate an effective CNT-CNT coupling  $J / 2\pi \simeq 12\mathrm{kHz}$ , thus giving  $\tau_{T}^{\max} \simeq 0.1$  ms. The relaxation time  $T_{1}$  of a single NV spin at low temperatures can reach up to a few minutes. Moreover, with spin echo techniques, a single spin in an ultra-pure diamond example typically has a dephasing time  $T_{2} \simeq 2$  ms even at room temperature,[59] corresponding to a dephasing rate  $\gamma_{s} / 2\pi \simeq 80\mathrm{Hz}$ . When dynamical decoupling pulse sequences are employed, the dephasing time can be made even close to one second at low temperatures.[60] These justify neglecting the spin decoherence. In this case, the mechanical noise dominates the dissipative processes. The dynamics of the system is therefore governed by

the following master equation,

$$
\begin{array}{l} \dot {\rho} (t) = \frac {i}{\hbar} [ \rho (t), H (t) ] - \frac {\gamma_ {m}}{2} n _ {\text {t h}} \sum_ {k = 1, 2} \mathcal {L} \left(b _ {k} ^ {\dagger}\right) \rho (t) \tag {21} \\ - \frac {\gamma_ {m}}{2} (n _ {\text {t h}} + 1) \sum_ {k = 1, 2} \mathcal {L} (b _ {k}) \rho (t), \\ \end{array}
$$

where  $\rho(t)$  is the density operator of the system,  $\gamma_{m}$  is the mechanical decay rate,  $n_{\mathrm{th}} = [\exp (\hbar \omega_{m} / k_{B}T) - 1]^{-1}$  is the equilibrium phonon occupation at temperature  $T$ , and  $\mathcal{L}(o)\rho(t) = o^{\dagger}o\rho(t) - 2o\rho(t)o^{\dagger} + \rho(t)o^{\dagger}o$  is the Lindblad superoperator. Here,  $H(t)$  is a binary Hamiltonian of the form,

$$
H (t) = \left\{ \begin{array}{l l} H _ {0}, & 0 <   t \leq \tau_ {0}, \text {a n d} \tau_ {0} + \tau_ {1} <   t \leq \tau_ {T} \\ H _ {1}, & \tau_ {0} <   t \leq \tau_ {0} + \tau_ {1}, \end{array} \right. \tag {22}
$$

with

$$
H _ {0} = J \left(\sum_ {k = 1, 2} b _ {k} ^ {\dagger} b _ {k} + b _ {1} b _ {2} ^ {\dagger} + b _ {2} b _ {1} ^ {\dagger}\right) \sigma_ {z} \tag {23}
$$

and  $H_{1} = Jb_{1}^{\dagger}b_{1}\sigma_{z}$ . In Eq. (22), we did not include the spin single-qubit operation before the third time interval because the length of the driving pulse is very short, as mentioned above. The master equation in Eq. (21) drives the phonon occupation of the kth CNT to be

$$
n _ {k} = \left\langle b _ {k} ^ {\dagger} b _ {k} \right\rangle \left(\tau_ {T}\right) = P _ {k} \exp \left(- \gamma_ {m} \tau_ {T}\right) + n _ {\text {t h}} \left[ 1 - \exp \left(- \gamma_ {m} \tau_ {T}\right) \right], \tag {24}
$$

at time  $t = \tau_T$ . For a realistic CNT, we can set the mechanical linewidth to be  $\gamma_m / 2\pi = 0.4\mathrm{Hz}$ , leading to a single-phonon lifetime of  $\tau_{m} = 1 / \gamma_{m}\simeq 400~\mathrm{ms}$ . In this situation,  $\tau_{m}$  is much longer than the total operation time  $\tau_T$ ,  $\gamma_{m}\tau_{T}\ll 1$  and, thus, we obtain

$$
n _ {k} = P _ {k} + n _ {\mathrm {t h}} \gamma_ {m} \tau_ {T}. \tag {25}
$$

This shows that, in addition to the coherent signal  $P_{k}$ , the final occupation has a thermal contribution  $n_{\mathrm{th}}\gamma_{m}\tau_{T}$ . In Fig. 2, we demonstrate the morphing behavior between particle and wave at  $T \simeq 10 \mathrm{mK}$ , according to Eq. (25). To confirm this, we also plot numerical simulations, which are in exact agreement with our analytical expression. The thermal occupation,  $n_{\mathrm{th}}\gamma_{m}\tau_{T}$ , increases as the phase  $\phi$ , because such a phase arises from the dynamical accumulation as discussed above. However, an extremely long phonon lifetime causes it to become negligible even at finite temperatures, as shown in Fig. 2.

We now consider the fluctuation noise. In the limit  $\gamma_{m}\tau_{T} \ll 1$ , the fluctuation noise  $\delta n_{k}^{\mathrm{noise}}$  in the phonon occupation  $n_{k}$  is expressed, according to the analysis in the Supplementary Section 4, as

$$
\left(\delta n _ {k} ^ {\text {n o i s e}}\right) ^ {2} = P _ {k} \left(2 P _ {k} - 1\right) \gamma_ {m} \tau_ {m} + \left(2 P _ {k} + 1\right) n _ {\text {t h}} \gamma_ {m} \tau_ {T}, \tag {26}
$$

where the first term is the vacuum fluctuation, which can be neglected, and the second term is the thermal fluctuation, which increases with temperature. To quantitatively describe the ability to resolve the coherent signal from the fluctuation noise, we typically employ the signal-to-noise ratio defined as

$$
\mathcal {R} _ {k} = \frac {P _ {k}}{\delta n _ {k} ^ {\text {n o i s e}}}. \tag {27}
$$

The signal-resolved regime often requires  $\mathcal{R}_k > 1$  for any  $P_k$ . However, the probability  $P_k$  in the range zero to unity indicates that there always exist some  $P_k$  such that  $\mathcal{R}_k < 1$ , in particular, at finite temperatures. Nevertheless, we find that the total fluctuation noise

$$
\mathcal {S} ^ {2} = \left(\delta n _ {1} ^ {\text {n o i s e}}\right) ^ {2} + \left(\delta n _ {2} ^ {\text {n o i s e}}\right) ^ {2} \tag {28}
$$

is kept below an upper bound

$$
\mathcal {B} ^ {2} = \gamma_ {m} \tau_ {T} ^ {\max } + 4 n _ {\text {t h}} \gamma_ {m} \tau_ {T} ^ {\max }, \tag {29}
$$

and further that assuming  $\mathcal{B}^2 < 1 / 2$  can make either or both of  $\mathcal{R}_1$

![](images/ebe1ecd73561227788357a6445d02e2290795024d33f224538f9e85658b7c540.jpg)

![](images/e8a5241fd89ceb2a91be46cc8de727159c8540d32f78cb760518a7d840f7c567.jpg)  
Fig. 2 Morphing between particle and wave characteristics of a CNT mechanical phonon. Phonon occupation  $\mathbf{a} n_{1}$  and  $\mathbf{b} n_{2}$  as a function of the relative phase  $\phi$  and the rotation angle  $\varphi$ . The analytical results (colored surfaces) are in excellent agreement with the numerical simulations (black symbols). Here, in addition to  $\gamma_{s} / 2\pi = 200\gamma_{m} / 2\pi = 80\mathrm{Hz}$ , we assume that  $g / 2\pi = 100\mathrm{kHz}$ ,  $\omega_{m} / 2\pi = 2\mathrm{MHz}$ ,  $\Omega = 10\omega_{m}$ , and  $\Delta_{-} = 142\omega_{m}$ , resulting in  $\omega_{q} \simeq 1.5\omega_{m}$  and then  $J / 2\pi \simeq \times 12\mathrm{kHz}$ , and that  $n_{\mathrm{th}} = 100$ , corresponding to an environmental temperature of  $\simeq 10\mathrm{mK}$

and  $\mathcal{R}_2$  greater than 1. In this case, at least one CNT signal is resolved for each measurement. The conservation of the coherent phonon number equal to 1 ensures that the unresolved signal can be inferred from the resolved one, which allows the morphing between wave and particle to be effectively observed from the fluctuation noise. To quantify this, we define a signal visibility as,

$$
\mathcal {R} = \frac {\sqrt {2}}{2 \mathcal {B}}, \tag {30}
$$

in analogy to the signal-to-noise ratio  $\mathcal{R}_k$ . The ratio  $\mathcal{R}$  describes the visibility of the total signal rather than the single CNT signals. At zero temperature ( $n_{\mathrm{th}} = 0$ ), the noise originates only from the vacuum fluctuation, and this yields  $\mathcal{R} \gg 1$ . However, at finite temperatures,  $n_{\mathrm{th}}$  increases as  $T$ , causing a decrease in  $\mathcal{R}$ , as shown in Fig. 3. Therefore, the requirement of  $\mathcal{R} > 1$  sets an upper bound on the temperature, and as a result, leads to a critical

![](images/ddf4f9875b19c2489f799aaeb5e9be0fb90bee82485befdb81d5652b71cb0090.jpg)  
Fig. 3 Signal visibility  $\mathcal{R}$  as a function of the temperature  $T$ . The yellow shaded area represents the signal-resolved regime, where the morphing between wave and particle can be effectively observed in the fluctuation noise. The vertical line corresponds to the critical temperature  $T_{c}$ . The inset shows a linear increase in  $T_{c}$  with increasing the ratio of the spin-mediated CNT-CNT coupling strength  $J$  to the mechanical-mode decay rate  $\gamma_{m}$ . Here, all parameters are set to be the same as in Fig. 2

temperature,

$$
T _ {c} = \frac {\hbar \omega_ {m}}{k _ {B} \ln [ (1 + 1 5 \pi \gamma_ {m} / J) / (1 - 5 \pi \gamma_ {m} / J) ]}. \tag {31}
$$

The critical temperature linearly increases with  $J / \gamma_{m}$ , as plotted in the inset of Fig. 3. To increase  $J$ , we can increase the current  $I$  through the CNTs, decrease the distance  $d$  between the CNTs, or decrease the spin-qubit transition frequency  $\omega_{q}$ . Furthermore, the increase in the CNT resonance frequency  $\omega_{m}$  or the decrease in the CNT loss rate  $\gamma_{m}$  can also lead to an increase in the critical temperature. For modest parameters of  $J / 2\pi = 12\mathrm{kHz}$  and  $\gamma_{m} / 2\pi = 0.4\mathrm{Hz}$ , a critical temperature  $T_{c}$  of  $\simeq 47\mathrm{mK}$ , which is routinely accessible in current experiments, can be achieved.

# Test of macroscopicity

We have described the implementation of a quantum paradox with massive mechanical objects with experimentally distinguishable single-phonon excitations. The question arises whether this proposal can be considered as a test of macroscopicity.[62,63] Typical proposals of such tests (as cited below) have been based on implementing superpositions of macroscopically distinguishable states of classical-like systems, which are often referred to as Schrödinger's cat states (see, e.g., ref. [64]). Sometimes, the meaning of Schrödinger's cat states is limited to "superposition states of macroscopic systems, where the amplitude of their excitations is large".[65] Note, however, that the term "large amplitude" can be understood in various ways. These include the cases (criteria) when (i) the amplitudes of the constituent states of a given superposition are large as in classical systems, or (ii) when these amplitudes are large enough concerning their experimental distinguishability (i.e., compared to the resolution of detectors). Strictly speaking, a state satisfying one of these conditions, does not necessarily satisfy the other. For example, a superposition of coherent states,  $|\psi \rangle = \mathcal{N}(|\alpha \rangle + |\beta \rangle$ ) with  $\mathcal{N}$  being a normalization constant, is a cat state according to criterion (i) if  $|\alpha|, |\beta| \gg 1$ , but cannot be considered as a cat state according to criterion, (ii) if  $\epsilon \equiv |\alpha - \beta| \ll 1$  is beyond the resolution of detectors. Conversely,  $|\psi \rangle$  is a cat state according to criterion (ii) if  $\epsilon$  can be resolved experimentally even if  $|\alpha|, |\beta| \approx 1$ , i.e., when criterion (i) is not satisfied. In the latter case, when the amplitude of such excitations is not large in classical terms, but still macroscopically distinguishable, the states are sometimes referred to as Schrödinger's kitten

states, as, e.g., those generated and measured in ref. 66. In this sense, the single-phonon wave-particle superposition, given in Eq. (16), can be referred to as a Schrödinger kitten state, since the excitations of the macroscopic mechanical systems are small, i.e., at the single-phonon level. Indeed, the amplitudes of single-phonon excitations are not large enough to satisfy criterion (i). However, such superpositions of single phonons are large enough that the constituent states of the superposition, given in Eqs. (17) and (18), are experimentally distinguishable, thus satisfying criterion (ii). Therefore, such a test of a quantum principle at the low-excitation level of massive mechanical objects can also be viewed as a test at the macroscopic scale, as claimed, e.g., in refs. 67-69 and references therein.

We note that a collective degree of freedom of many atoms does not necessarily imply that the system is in a macroscopic quantum state. However, we showed that the studied system of macroscopic resonators can be in a maximally entangled two-mode state. This state is described by a non-positive Glauber-Sudarshan  $P$  function. This implies that the system itself is quantum. Below we describe the method to amplify the small-excitation kitten states, given in Eqs. (17) and (18), to a cat state with large excitation.

# Amplification of the Schrodinger kitten states

Here we apply the idea and method of ref.  $^{70}$  to show how to amplify the phonon numbers of the single-phonon superposition states  $|\mathrm{particle}\rangle$  and  $|\mathrm{wave}\rangle$ , given in Eqs. (17) and (18), by squeezing the mechanical modes  $b_{1}$  and  $b_{2}$ . Thus, these states can become Schrödinger's cat-like states. For simplicity, but without loss of generality, here we consider a squeezing operator

$$
U _ {k} = \exp \left[ \frac {r}{2} \left(b _ {k} ^ {\dagger 2} - b _ {k} ^ {2}\right) \right], \tag {32}
$$

acting on the mode  $b_{k}$  ( $k = 1, 2$ ), with  $r$  being a squeezing parameter. This squeezing leads to

$$
\left| S _ {1 0} \right\rangle = \left(U _ {1} b _ {1} ^ {\dagger} \otimes U _ {2}\right) \left| \operatorname {v a c} \right\rangle = \left| S _ {1} \right\rangle_ {1} \left| S _ {0} \right\rangle_ {2}, \tag {33}
$$

$$
\left| S _ {0 1} \right\rangle = \left(U _ {1} \otimes U _ {2} b _ {2} ^ {\dagger}\right) | \text {v a c} \rangle = \left| S _ {0} \right\rangle_ {1} | S _ {1} \rangle_ {2}, \tag {34}
$$

where we have defined the phonon squeezed Fock states  $|S_0\rangle_k = U_k|0\rangle_k$  and  $|S_1\rangle_k = U_kb_k^\dagger |0\rangle_k$ , with  $|0\rangle_k$  being the vacuum state of the mechanical-mode  $b_k$ . As a result, the states  $|\mathrm{particle}\rangle$  and  $|\mathrm{wave}\rangle$  become

$$
\left| \mathcal {P} _ {r} \right\rangle = \frac {1}{\sqrt {2}} \left[ \exp (i \phi) \left| S _ {1 0} \right\rangle + i \left| S _ {0 1} \right\rangle \right], \tag {35}
$$

$$
\left| \mathcal {W} _ {r} \right\rangle = \frac {1}{2} \left\{\left[ \exp (i \phi) - 1 \right] \left| S _ {1 0} \right\rangle + i \left[ \exp (i \phi) + 1 \right] \left| S _ {0 1} \right\rangle \right\}, \tag {36}
$$

respectively. The final state  $|\Psi \rangle_{f}$  becomes

$$
\left| \Psi \right\rangle_ {f} = \cos (\varphi) \left| \mathcal {P} _ {r} \right\rangle | 0 \rangle + \sin (\varphi) \left| \mathcal {W} _ {r} \right\rangle | D \rangle . \tag {37}
$$

The modes  $b_{k}$  for  $k = 1,2$  are transformed, via squeezing, to the Bogoliubov modes described by

$$
U _ {k} ^ {\dagger} b _ {k} U _ {k} = \cosh (r) b _ {k} + \sinh (r) b _ {k} ^ {\dagger}. \tag {38}
$$

By using this unitary transformation, one obtains the average phonon numbers of  $|S_0\rangle_k$  and  $|S_1\rangle_k$  equal to

$$
{ } _ { k } \langle S _ { 0 } | b _ { k } ^ { \dagger } b _ { k } | S _ { 0 } \rangle _ { k } = \sinh ^ { 2 } ( r ) , \tag {39}
$$

$$
{ } _ { k } \langle S _ { 1 } | b _ { k } ^ { \dagger } b _ { k } | S _ { 1 } \rangle _ { k } = 3 \sinh ^ { 2 } ( r ) + 1 . \tag {40}
$$

We note that by applying this unconditional amplification method, one can exponentially increase the distinguishability of the states  $|S_{10}\rangle$  and  $|S_{01}\rangle$ . Although, a single-shot distinguishability of the mechanical-mode states  $|\mathcal{P}_r\rangle$  and  $|\mathcal{W}_r\rangle$  is not increased, a tomographic distinguishability of these states in the phase space

![](images/c3ae09334ec84a5c8f16d5868b773df196a2aef76752d1bac614b7dfd2bb9789.jpg)  
Fig. 4 Wigner function for the states  $|S_0\rangle_k = U_k|0\rangle_k$  (solid curves) and  $|S_1\rangle_k = U_k|1\rangle_k$  (dashed curves) for  $r = 0$  in a and 1 in b. Here,  $k = 1, 2$ . The Wigner function is defined as  $W(a) = \pi^{-2}\int d^2\beta \exp(-i\beta a^* - i\beta^*a)\mathrm{Tr}\left[\exp(i\beta^*a)\exp(i\beta a^\dagger)\varrho\right]$ . For both plots, we have assumed  $\mathrm{Re}(a) = 0$ . It is seen that the region marked in yellow, corresponding to the negative Wigner function for  $|S_1\rangle_k$ , increases with increasing squeezing parameter  $r$

is increased with the amplified amplitudes of the mechanical-mode excitations. Indeed, the distinguishability of  $|\mathcal{P}\rangle_r$  and  $|\mathcal{W}_r\rangle$ , as measured by the infidelity,  $\left|\mathrm{IF} = 1 - \left|\langle \mathcal{W}_r|\mathcal{P}_r\rangle\right|^2 = 1 - \left|\langle \mathcal{W}_r|\mathcal{P}_r\rangle\right|^2\right|$ , is independent of the squeezing parameter  $r$  for a given  $\phi$ . For any  $\phi \neq \pm \pi /2$ , the states are distinguishable, and the highest distinguishability is for  $\phi = 0,\pi$ , for which the infidelity is  $\mathrm{IF} = 1 / 2$ . Thus, even for such optimal values of  $\phi$ , it is impossible to deterministically distinguish the states  $|\mathcal{P}_r\rangle$  and  $|\mathcal{W}_r\rangle$  from each other in a single-shot experiment. We refer to this property as a single-shot distinguishability. Anyway, these mechanical states can be macroscopically distinguished by performing, e.g., Wigner-function tomography on a number of their copies. Such tomographic distinguishability in phase space indeed increases with the squeezing parameter  $r$ , as shown in Fig. 4.

Finally, we note that the famous optical prototypes of the Schrödinger's cat states, which are given by the odd and even coherent states,  $|\psi_{\pm}\rangle = \mathcal{N}(|a\rangle \pm | - a\rangle)$ , cannot be distinguished deterministically in a single-shot experiment either. This is because the coherent states  $|a\rangle$  and  $|-a\rangle$  are not orthogonal for finite values of  $a$ . Their overlap decreases exponentially with increasing  $a$ , so  $|a\rangle$  and  $|-a\rangle$  become orthogonal in the limit of large  $|a|$ . However, this amplification of  $a$  cannot be done deterministically, because this process is prohibited by the non-cloning and no-signalling theorems. Indeed, non-orthogonal states cannot be deterministically transformed to orthogonal (thus, completely distinguishable) states. Note that popular methods of amplifying small-amplitude states are based on either (i) probabilistic but accurate amplification or (ii) deterministic but inaccurate cloning. For example, the method described, e.g., in refs. [66,71] is probabilistic, because it is based on conditional measurements performed on two copies of  $|\psi_{\pm}\rangle$ . In contrast to this, the amplification method in ref. [70], as applied here,

corresponds to approximate quantum cloning, i.e., phase-covariant cloning by stimulated emission.

# DISCUSSION

We have presented a proposal for a quantum delayed-choice experiment with nanomechanical resonators, which enables a macroscopic test of an arbitrary quantum wave-particle superposition. The ability to tolerate the mechanical noise has also been given here, demonstrating that our proposal can be implemented with current experimental techniques. While we have chosen to focus on a spin-nanomechanical setup, the present method could be directly extended to other hybrid systems, for example, mechanical devices coupled to a superconducting atom.[32,49,72] Recently, an experimental work reported that photons can be entangled in their wave-particle degree of freedom.[22] This indicates that the wave-particle nature of photons may be used to encode flying qubits for long-distance quantum communication. Photons are ideal quantum information carriers, but they are difficult to store. In contrast to photons, long-lived phonons could be used for optical information storage.[73] Our study shows that phonons can also be prepared in a wave-particle superposition state, and that the wave-particle nature of phonons is not more special than their other degrees of freedom. Thus, the wave-particle degree of freedom of phonons may be exploited for storing quantum information encoded in the wave-particle degree of freedom of photons. In addition, optomechanical interactions can couple a mechanical mode to optical modes at different frequencies.[74] Thus, the mechanical wave-particle degree of freedom may be employed to map quantum information encoded in the wave-particle degree of freedom from photons at a given frequency to photons at any desired frequency. The mechanical wave-particle nature, as a new degree of freedom, may find various applications in quantum information.

We believe that the macroscopicity of our single-phonon wave-particle superposition is highly counter-intuitive, as based on a refined version of the quantum paradox, even if the mechanical resonators are in the single-phonon-excitation regime. Indeed, we analyzed a "nested" kitten state, as given in Eq. (16), where the particle and wave states, given in Eqs. (17) and (18), are purely mechanical kitten states for  $\phi \neq \pm \pi /2$ . Moreover, we have described a method, based on mechanical-mode squeezing, which enables the amplification of small-excitation Schrödinger kitten states, given in Eqs. (17) and (18), to large-excitation Schrödinger cat states of the massive mechanical resonators. For these reasons, an experimental realization of our proposal can be a fundamental test of a coherent wave-particle superposition of massive objects with phonon excitations, which can be increased exponentially by squeezing. Hence, this proposed quantum delayed-choice experiment of massive mechanical resonators not only leads to a better understanding of quantum theory at the macroscopic scale, but also indicates that, like the vertical and horizontal polarizations of photons, the mechanical wave-particle nature, as an additional degree of freedom of phonons, may be widely exploited for quantum information applications.

# DATA AVAILABILITY

The data that supports the findings of this study are available in the Supplementary Information file. Additional data are also available from the corresponding authors upon reasonable request.

# ACKNOWLEDGEMENTS

W.Q. thanks Peng-Bo Li for valuable discussions. W.Q. and J.Q.Y. were supported in part by the National Key Research and Development Program of China (Grant No. 2016YFA0301200), the China Postdoctoral Science Foundation (Grant No. 2017M610752), and the NSFC (Grant No. 11774022). G.L.L. is supported in part by

National Key Research and Development Program of China (2017YFA0303700); Beijing Advanced Innovation Center for Future Chip (ICFC). A.M. and F.N. acknowledge the support of a grant from the John Templeton Foundation. F.N. is supported in part by the MURI Center for Dynamic Magneto-Optics via the Air Force Office of Scientific Research (AFOSR) (FA9550-14-1-0040), Army Research Office (ARO) (Grant No. Grant No. W911NF-18-1-0358), Asian Office of Aerospace Research and Development (AOARD) (Grant No. FA2386-18-1-4045), Japan Science and Technology Agency (JST) (Q-LEAP program, ImpACT program, and CREST Grant No. JPMJCR1676), Japan Society for the Promotion of Science (JSPS) (JSPS-RFBR Grant No. 17-52-50023, and JSPS-FWO Grant No. VS.059.18N), and RIKEN-AIST Challenge Research Fund.

# AUTHOR CONTRIBUTIONS

W.Q. and A.M. developed the theory and performed the calculations. G.L.L., J.Q.Y., and F. N. supervised the project. All authors researched, collated, and wrote this paper.

# ADDITIONAL INFORMATION

Supplementary information accompanies the paper on the npj Quantum Information website (https://doi.org/10.1038/s41534-019-0172-9).

Competing interests: The authors declare no competing interests.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# REFERENCES

1. Bohr, N. in Quantum Theory and Measurement, (eds Wheeler, J. A. & Zurek, W. H.) 9-49 (Princeton University Press, Princeton, 1984).  
2. Wheeler, J. A. in Mathematical Foundations of Quantum Theory, (eds Marlow, A. R.) 9-48 (Academic Press, Cambridge, 1978).  
3. Ma, X.-s, Kofler, J. & Zeilinger, A. Delayed-choice gedanken experiments and their realizations. Rev. Mod. Phys. 88, 015005 (2016).  
4. Hellmuth, T., Walther, H., Zajonc, A. & Schleich, W. Delayed-choice experiments in quantum interference. Phys. Rev. A 35, 2532 (1987).  
5. Kim, Y.-H., Yu, R., Kulik, S. P., Shih, Y. & Scully, M. O. Delayed "Choice" Quantum Eraser. Phys. Rev. Lett. 84, 1 (2000).  
6. Jacques, V. et al. Experimental realization of Wheeler's delayed-choice gedanken experiment. Science 315, 966-968 (2007).  
7. Jacques, V. et al. Delayed-choice test of quantum complementarity with interfering single photons. Phys. Rev. Lett. 100, 220402 (2008).  
8. Manning, A. G., Khakimov, R. I., Dall, R. G. & Truscott, A. G. Wheeler's delayed-choice gedanken experiment with a single atom. Nat. Phys. 11, 539 (2015).  
9. Liu, Y., Lu, J. & Zhou, L. Information gain versus interference in Bohr's principle of complementarity. Opt. Express 25, 202-211 (2017).  
10. Vedovato, F. et al. Extending Wheeler's delayed-choice experiment to space. Sci. Adv. 3, e1701180 (2017).  
11. Chaves, R., Lemos, G. B. & Pienaar, J. Causal modeling the delayed-choice experiment. Phys. Rev. Lett. 120, 190401 (2018).  
12. Ioniciou, R. & Terno, D. R. Proposal for a quantum delayed-choice experiment. Phys. Rev. Lett. 107, 230406 (2011).  
13. Adesso, G. & Girolami, D. Quantum optics: wave-particle superposition. Nat. Photon. 6, 579 (2012).  
14. Shadbolt, P., Mathews, J. C. F., Laing, A. & O'Brien, J. L. Testing foundations of quantum mechanics with photons. Nat. Phys. 10, 278 (2014).  
15. Roy, S. S., Shukla, A. & Mahesh, T. S. NMR implementation of a quantum delayed-choice experiment. Phys. Rev. A 85, 022109 (2012).  
16. AuCCaise, R. et al. Experimental analysis of the quantum complementarity principle. Phys. Rev. A 85, 032121 (2012).  
17. Xin, T., Li, H., Wang, B.-X. & Long, G.-L. Realization of an entanglement-assisted quantum delayed-choice experiment. Phys. Rev. A 92, 022126 (2015).  
18. Tang, J.-S. et al. Realization of quantum Wheeler's delayed-choice experiment. Nat. Photon. 6, 600-604 (2012).  
19. Peruzzo, A., Shadbolt, P., Brunner, N., Popescu, S. & O'Brien, J. L. A quantum delayed-choice experiment. Science 338, 634-637 (2012).  
20. Kaiser, F., Coudreau, T., Milman, P., Ostrowsky, D. B. & Tanzilli, S. Entanglement-enabled delayed-choice experiment. Science 338, 637-640 (2012).  
21. Yan, H. et al. Experimental observation of simultaneous wave and particle behavior in a narrowband single-photon wave packet. Phys. Rev. A 91, 042132 (2015).  
22. Rab, A. S. et al. Entanglement of photons in their dual wave-particle nature. Nat. Commun. 8, 915 (2017).

23. Long, G.-L., Qin, W., Yang, Z. & Li, J.-L. Realistic interpretation of quantum mechanics and encounter-delayed-choice experiment. Sci. China Phys. Mech. Astron. 61, 030311 (2018).  
24. Zheng, S.-B. et al. Quantum delayed-choice experiment with a beam splitter in a quantum superposition. Phys. Rev. Lett. 115, 260403 (2015).  
25. Liu, K. et al. A twofold quantum delayed-choice experiment in a superconducting circuit. Sci. Adv. 3, e1603159 (2017).  
26. Blencowe, M. Quantum electromechanical systems. Phys. Rep. 395, 159-222 (2004).  
27. Aspelmeyer, M., Kippenberg, T. J. & Marquardt, F. Cavity optomechanics. Rev. Mod. Phys. 86, 1391 (2014).  
28. Poot, M. & van der Zant, H. S. J. Mechanical systems in the quantum regime. Phys. Rep. 511, 273-335 (2012).  
29. Iijima, S. Helical microtubules of graphitic carbon. Nature 354, 56 (1991).  
30. Liu, D. E. Sensing Kondo correlations in a suspended carbon nanotube mechanical resonator with spin-orbit coupling. Quantum Eng. 1, e10 (2019).  
31. Buluta, I., Ashhab, S. & Nori, F. Natural and artificial atoms for quantum computation. Rep. Prog. Phys. 74, 104401 (2011).  
32. Xiang, Z. L., Ashhab, S., You, J. Q. & Nori, F. Hybrid quantum circuits: superconducting circuits interacting with other quantum systems. Rev. Mod. Phys. 85, 623 (2013).  
33. Rabl, P. et al. Strong magnetic coupling between an electronic spin qubit and a mechanical resonator. Phys. Rev. B 79, 041302 (2009).  
34. Rabl, P. et al. A quantum spin transducer based on nanoelectromechanical resonator arrays. Nat. Phys. 6, 602 (2010).  
35. Kolkowitz, S. et al. Coherent sensing of a mechanical resonator with a single-spin qubit. Science 335, 1603-1606 (2012).  
36. Li, P.-B., Xiang, Z.-L., Rabl, P. & Nori, F. Hybrid quantum device with nitrogen-vacancy centers in diamond coupled to carbon nanotubes. Phys. Rev. Lett. 117, 015502 (2016).  
37. Cao, P., Betzholz, R., Zhang, S. & Cai, J. Entangling distant solid-state spins via thermal phonons. Phys. Rev. B 96, 245418 (2017).  
38. Gamel, O. & James, D. F. V. Time-averaged quantum dynamics and the validity of the effective Hamiltonian model. Phys. Rev. A 82, 052106 (2010).  
39. Qin, W. et al. Exponentially enhanced light-matter interaction, cooperativities, and steady-state entanglement using parametric amplification. Phys. Rev. Lett. 120, 093601 (2018).  
40. Huang, P. et al. Observation of an anomalous decoherence effect in a quantum bath at room temperature. Nat. Commun. 2, 570 (2011).  
41. Lillie, S. E. et al. Environmentally mediated coherent control of a spin qubit in diamond. Phys. Rev. Lett. 118, 167204 (2017).  
42. Xing, J. et al. Experimental investigation of quantum entropic uncertainty relations for multiple measurements in pure diamond. Sci. Rep. 7, 2563 (2017).  
43. Xue, F., Wang, Y. D., Liu, Y.-x & Nori, F. Cooling a micromechanical beam by coupling it to a transmission line. Phys. Rev. B 76, 205302 (2007).  
44. You, J. Q., Liu, Y.-x & Nori, F. Simultaneous cooling of an artificial atom and its neighboring quantum system. Phys. Rev. Lett. 100, 047001 (2008).  
45. Grajcar, M., Ashhab, S., Johansson, J. R. & Nori, F. Lower limit on the achievable temperature in resonator-based sideband cooling. Phys. Rev. B 78, 035406 (2008).  
46. Ma, Y., Yin, Z.-q, Huang, P., Yang, W. L. & Du, J. F. Cooling a mechanical resonator to the quantum regime by heating it. Phys. Rev. A 94, 053836 (2016).  
47. Clark, J. B., Lecocq, F., Simmonds, R. W., Aumentado, J. & Teufel, J. D. Sideband cooling beyond the quantum backaction limit with squeezed light. Nature 541, 191-195 (2017).  
48. Wang, X., Miranowicz, A., Li, H.-R. & Nori, F. Hybrid quantum device with a carbon nanotube and a flux qubit for dissipative quantum engineering. Phys. Rev. B 95, 205415 (2017).  
49. O'Connell, A. D. et al. Quantum ground state and single-phonon control of a mechanical resonator. Nature 464, 697 (2010).  
50. Scully, M. O. & Zubairy, M. S. Quantum Optics. (Cambridge University Press, Cambridge, 1997).  
51. Liu, Y.-x, Wei, L. F. & Nori, F. Generation of nonclassical photon states using a superconducting qubit in a microcavity. Europhys. Lett. 67, 941 (2004).  
52. Hofheinz, M. et al. Generation of Fock states in a superconducting quantum circuit. Nature 454, 310 (2008).  
53. Hofheinz, M. et al. Synthesizing arbitrary quantum states in a superconducting resonator. Nature 459, 546 (2009).  
54. Doherty, M. W. et al. The nitrogen-vacancy colour centre in diamond. Phys. Rep. 528, 1-45 (2013).  
55. Jelezko, F., Gaebel, T., Popa, I., Gruber, A. & Wrachtrup, J. Observation of coherent oscillations in a single electron spin. Phys. Rev. Lett. 92, 076401 (2004).  
56. Jiang, L. et al. Repetitive readout of a single electronic spin via quantum logic with nuclear spin ancillae. Science 326, 267-272 (2009).  
57. Liu, G.-Q. et al. Demonstration of entanglement-enhanced phase estimation in solid. Nat. Commun. 6, 6726 (2015).

58. Liu, G.-Q. et al. Single-shot readout of a nuclear spin weakly coupled to a nitrogen-vacancy center at room temperature. Phys. Rev. Lett. 118, 150504 (2017).  
59. Balasubramanian, G. et al. Ultralong spin coherence time in isotopically engineered diamond. Nat. Mater. 8, 383-387 (2009).  
60. Bar-Gill, N., Pham, L. M., Jarmola, A., Budker, D. & Walsworth, R. L. Solid-state electronic spin coherence time approaching one second. Nat. Commun. 4, 1743 (2013).  
61. Moser, J., Eichler, A., Guttinger, J., Dykman, M. I. & Bachtold, A. Nanotube mechanical resonators with quality factors of up to 5 million. Nat. Nanotechnol. 9, 1007-1011 (2014).  
62. Leggett, A. J. Testing the limits of quantum mechanics: motivation, state of play, prospects. J. Phys. 14, R415 (2002).  
63. Korsbakken, J. I., Whaley, K. B., Dubois, J. & Cirac, J. I. Measurement-based measure of the size of macroscopic quantum superpositions. Physi. Rev. A 75, 042106 (2007).  
64. Gerry, C. & Knight, P. Introductory Quantum Optics. (Cambridge University Press, Cambridge, 2005).  
65. Agarwal, G. S. Quantum Optics. (Cambridge University Press, Cambridge, 2013).  
66. Ourjoumtsev, A., Tualle-Brouri, R., Laurat, J. & Grangier, P. Generating optical Schrödinger kittens for quantum information processing. Science 312, 83-86 (2006).  
67. Hofer, S. G., Lehnert, K. W. & Hammerer, K. Proposal to Test Bell's Inequality in Electromechanics. Phys. Rev. Lett. 116, 070406 (2016).  
68. Marinković, I. et al. Optomechanical bell test. Phys. Rev. Lett. 121, 220404 (2018).  
69. Ockeloen-Korppi, C. F. et al. Stabilized entanglement of massive mechanical oscillators. Nature 556, 478 (2018).  
70. Sekatski, P., Brunner, N., Branciard, C., Gisin, N. & Simon, C. Towards quantum experiments with human eyes as detectors based on cloning via stimulated emission. Phys. Rev. Lett. 103, 113601 (2009).

71. Lund, A. P., Jeong, H., Ralph, T. C. & Kim, M. S. Conditional production of superpositions of coherent states with inefficient photon detection. Phys. Rev. A 70, 020101(R) (2004).  
72. Gu, X., Kockum, A. F., Miranowicz, A., Liu, Y.-x & Nori, F. Microwave photonics with superconducting quantum circuits. Phys. Rep. 718-719, 1-102 (2017).  
73. Fiore, V. et al. Storing optical information as a mechanical excitation in a silica optomechanical resonator. Phys. Rev. Lett. 107, 133601 (2011).  
74. Dong, C., Fiore, V., Kuzyk, M. C. & Wang, H. Optomechanical dark mode. Science 338, 1609-1613 (2012).

![](images/b40188caf96e9066ada8dd1d89d26e551dd0deea95532a95afe19a862b89f8d3.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2019