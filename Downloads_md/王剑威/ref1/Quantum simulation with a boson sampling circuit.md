# Quantum simulation with a boson sampling circuit

Diego González Olivares, $^{1}$  Borja Peropadre, $^{2}$  Alán Aspuru-Guzik, $^{2}$  and Juan José García-Ripoll $^{1}$

$^{1}$  Instituto de Física Fundamental IFF-CSIC, Calle Serrano 113b, Madrid E-28006, Spain

$^{2}$ Department of Chemistry and Chemical Biology, Harvard University, Cambridge, Massachusetts 02138, USA

(Received 2 May 2016; published 17 August 2016)

In this work we study a system that consists of  $2M$  matter qubits that interact through a boson sampling circuit, i.e., an  $M$ -port interferometer, embedded in two different architectures. We prove that, under the conditions required to derive a master equation, the qubits evolve according to effective bipartite  $XY$  spin Hamiltonians, with or without local and collective dissipation terms. This opens the door to the simulation of any bipartite spin or hard-core boson models and exploring dissipative phase transitions as the competition between coherent and incoherent exchange of excitations. We also show that in the purely dissipative regime this model has a large number of exact and approximate dark states, whose structure and decay rates can be estimated analytically. We finally argue that this system may be used for the adiabatic preparation of boson sampling states encoded in the matter qubits.

DOI: 10.1103/PhysRevA.94.022319

# I. INTRODUCTION

Optical circuits are linear devices that route photons along different paths. They can be found at a variety of scales, from classical circuits built using macroscopic lenses and mirrors [1,2] to photonic crystals that achieve routing and confinement by means of nanostructuring a metamaterial [3,4], on-chip waveguides [5], waveguides imprinted using femtosecond pulses [6], or reconfigurable optical microchips [7,8].

In addition to their widespread use in telecommunications, optical circuits have found two extraordinary applications in quantum science. Photonic pathways enable the engineering of electromagnetic environments for atoms or quantum dots, to enhance and control light-matter interactions [4,9], implement nonlinear transformations on light [10], or engineer photon-mediated interactions [11,12].

An additional novel application is the study of computational models based on boson sampling [13-23]. Within this paradigm, a particular kind of optical circuit known as a multiport interferometer is fed with a nonclassical input of one photon in  $N$  out of  $M \gg N$  ports. Aaronson and Arkhipov [13] showed that the events with exactly  $N$  photons exiting  $M$  distinct ports have a probability distribution that, under reasonable conjectures, is classically hard to simulate for arbitrary circuits [24]. Therefore, optical circuits are good candidates to demonstrate the supremacy of quantum computing models [25].

In this work, we merge the two research lines mentioned above into an application that studies the long-time effective dynamics between matter qubits interacting through boson sampling circuits [cf. Fig. 1(a)]. We build on the idea that the time evolution with general spin  $XY$  Hamiltonians is formally linked to boson sampling [26]. Here, we show that this relation emerges not only at a mathematical level but also in physical implementations. More precisely, we consider a setup with  $2M$  two-level systems coupled to the ports of an  $M$ -line interferometer—symbolized by green circles and blue waveguides in Fig. 1(a). We show that this system exhibits an effective spin-spin interaction which may be dissipative [cf. Fig. 1(b)] or coherent [cf. Fig. 1(c)]. In the first case, the dissipative interaction has got a collective nature. We prove

that these models have a large space of dark and quasidark states, which we can analyze for arbitrary random unitaries. In the second case, our system implements arbitrary bipartite  $XY$  spin models with long-range interactions, whose dynamics are classically hard to simulate. Moreover, the same setup can be used to directly prepare and study boson sampling states directly in the matter qubits. The main conclusion of this work is that the combination of optical circuits and few-level systems offers unique opportunities for quantum simulation and quantum information processing.

The structure of this work is as follows. Throughout Sec. II we introduce the physical setup and its description in terms of abstract unitary transformations. Starting from these spin-boson models, Sec. III derives the effective interaction between emitters, in both the coherent and incoherent regimes. These models are then used in Sec. IV to study applications in quantum simulations, the potential of achieving quantum supremacy, and dissipative state engineering. Section V summarizes the results and discusses their potential impact in various fields. Finally, for the sake of readability, we group several appendices with the explicit calculations for the interferometer transformation, the effective models, and the boson-sampling state preparation.

# II. PHYSICAL SETUP

We consider two arrays of qubits or two-level systems that interact through an optical circuit. The circuit is regarded as a linear transformation  $U$  of the annihilation operators, from  $M$  input channels to  $M$  output channels,

$$
a _ {m k} ^ {\prime} = U _ {m n} (k) a _ {n k}, \tag {1}
$$

where the linear transformation depends in general on the linear momentum,  $k$ , associated with the bosonic modes with the anihilation operators  $a_{mk}$  and  $a_{mk}'$ . As explained in Appendix A, this unitary map can be built using beam splitters and phase shifters. Nevertheless, the same idea can be extended to more general setups with optical [15-17,20] or microwave media [21] that propagate photons through a finite number of channels.

![](images/9f38560e6b1d527170de3215ca3643dbc4e403cb9375f01dca7a828018575cc2.jpg)  
FIG. 1. (a) Our setup consists of two sets of matter qubits or two-level systems (green) effectively connected with each other by the photons that propagate through a linear optics circuit (blue waveguides). Such a circuit could be built, for instance, from beam splitters and phase shifters. This circuit may be open (b), with free photons, or it may be converted into a resonator by terminating the ends with mirrors or closing it periodically (c) with additional optical paths.

![](images/e50729515214bdd0951215cddcf13da81dadcac97e600194aba1b7df49fa3e77.jpg)

![](images/d63af5e5a94f703195f7cc39dadf2afbdf4ed43cedf12b80fa996b1b853a12ab.jpg)

We consider an architecture in which we have one matter qubit coupled to each of the input or output ports of the photonic circuit [cf. Fig. 1(a)]. This architecture may be embedded in two different physical configurations. In the first of them, shown in Fig. 1(b), the photonic channels extend in both directions well beyond the qubits and support propagating waves. The Hamiltonian reads

$$
\begin{array}{l} H = \sum_ {m = 1} ^ {M} \frac {\Delta}{2} \left(\sigma_ {\text {i n}, m} ^ {z} + \sigma_ {\text {o u t}, m} ^ {z}\right) + \sum_ {m = 1} ^ {M} \sum_ {k} \omega_ {k} a _ {m k} ^ {\dagger} a _ {m k} \\ + \sum_ {m, k} g _ {k} \sigma_ {\mathrm {i n}, m} ^ {x} \left(a _ {m k} ^ {\dagger} + a _ {m k}\right) \\ + \sum_ {m, n, k} g _ {k} \sigma_ {\text {o u t}, m} ^ {x} \left(U _ {m n} (k) a _ {n k} ^ {\dagger} + U _ {m n} ^ {*} (k) a _ {n k}\right), \tag {2} \\ \end{array}
$$

where  $\Delta$  is the qubit splitting,  $\omega_{k}$  is the photon frequency,  $k$  is the corresponding momentum, and the  $\sigma_{\alpha,m}^{\beta}$  are the Pauli operators for the two sets of  $\alpha = \mathrm{in}$  and out of  $M$  matter qubits each. The qubit-mode coupling constant is of the form  $g_{k} = \bar{g}_{k} / \sqrt{L} = \mu \sqrt{2\pi\omega_{k}} / \sqrt{L}$ , with  $L$  being a quantization length for the waveguide modes and  $\mu$  being the dipolar coupling strength. We will eventually take the continuum limit replacing the sum over momenta with an integral,  $\sum_{k} g_{k}^{2} \rightarrow \frac{1}{2\pi} \int_{-\infty}^{+\infty} dk \bar{g}_{k}^{2}$ , but the sums are kept for convenience throughout the calculations.

Note also the difference in the coupling amplitudes of the input and output qubits in Eq. (2). The output qubits couple through the unitary transformation  $U(k)$  implemented by the optical circuit, which in general is a function of the photon momentum  $k$  with the only constraint being  $U(-k) = U^{*}(k)$  (cf. Appendix A).

An alternative setup would be an optical circuit where the output ports are closed with mirrors, thereby creating a resonator. The analysis of such circuits might be complicated in general, because the unitary  $U$  depends on photon momentum and the modes need to satisfy zero-field boundary conditions. For the sake of simplicity we have devised a configuration of the form shown in Fig. 1(c). This configuration ensures

that we may define photonic modes provided that  $kL' = 2\pi z$ , where  $z \in \mathbb{Z}$  and  $L'$  is the total length of the resonator. In addition, input and output qubits perceive the same distribution of fields in this configuration as they do in the setup of Fig. 1(b). Consequently, the Hamiltonian of this alternative configuration is the same as Eq. (2), with the difference that we will never replace the sums with integrals.

# III. EFFECTIVE MODELS

So far we have considered linear transformations on a collection of bosonic modes connecting two sets of qubits. We now derive effective models for the qubits by tracing out those bosonic degrees of freedom in the two different setups considered. We begin with the resonator system, in which the discrete spectrum gives rise to a purely coherent interaction. We then continue with the open waveguide circuit, for which both Hamiltonian interactions and collective dissipation coexist.

# A. Closed circuit: Spin Hamiltonian

We work with the model for the resonator setup shown in Fig. 1(c), where the optical circuit is introduced twice to have appropriate boundary conditions. We assume a dispersive limit in which the frequency spacing between cavity modes  $\delta \omega = c2\pi /L$  is much larger than the qubit-resonator coupling  $g_{k}\sim g$ . In this regime, if qubits are off-resonant from all cavity modes and  $|\omega_{k} - \Delta | > g$ , we can use second-order perturbation theory to derive an effective qubit interaction mediated by the exchange of virtual photons:

$$
\begin{array}{l} H _ {\mathrm {s p i n}} = \sum_ {m = 1} ^ {M} \left(\frac {\tilde {\Delta}}{2} \sigma_ {\mathrm {i n}, m} ^ {z} + \frac {\tilde {\Delta}}{2} \sigma_ {\mathrm {o u t}, m} ^ {z}\right) \\ + \sum_ {m, n} J _ {m n} \left(\sigma_ {\text {o u t}, m} ^ {+} \sigma_ {\text {i n}, n} ^ {-} + \sigma_ {\text {i n}, m} ^ {+} \sigma_ {\text {o u t}, n} ^ {-}\right). \tag {3} \\ \end{array}
$$

The virtual photon exchange gives rise to a renormalization of the qubit frequency  $\tilde{\Delta} = \Delta +\delta$  , where

$$
\delta = \sum_ {k} \frac {g _ {k} ^ {2}}{\Delta - \omega_ {k}} \tag {4}
$$

is the effective shift, and the effective exchange interaction is given by

$$
J _ {m n} = \sum_ {k} \operatorname {R e} [ U _ {m n} (k) ] \frac {g _ {k} ^ {2}}{\Delta - \omega_ {k}}, \tag {5}
$$

which depends on the transformation  $U(k)$  implemented by the optical circuit for each value of the photon momentum  $k$ . In most cases, one of the contributions in Eq. (5) will dominate with respect to all the others, allowing a direct identification of  $J_{mn}$  with  $\mathrm{Re}[U_{mn}(\omega_k\approx \Delta)]$ .

# B. Open circuit: Master equation

We now work with the model (2), in which the photons form a continuum of modes propagating in both directions. Following the derivation in Appendix B, we obtain an effective master equation for the reduced density matrix of the qubits

$\rho_0$ . This equation only depends on the unitary transformation that represents the optical circuit at the resonance point,  $U \equiv U(k_{\Delta})$ , and the spontaneous emission rate  $\Gamma$  of each qubit onto its corresponding photonic channel [cf. Eq. (B8)]:

$$
\frac {d \rho_ {0}}{d t} = - i [ H _ {\text {e f f}}, \rho_ {0} ] + \Gamma \mathcal {L} [ \rho_ {0} ]. \tag {6}
$$

This equation contains an effective Hamiltonian,

$$
H _ {\text {e f f}} = \Gamma \sum_ {m, n} \operatorname {I m} \left[ U _ {m n} \right] \sigma_ {\text {o u t}, m} ^ {+} \sigma_ {\text {i n}, n} ^ {-} + \mathrm {H}. c., \tag {7}
$$

and a dissipation term,

$$
\begin{array}{l} \mathcal{L}[\rho_{0}] = \sum_{m}\sum_{\alpha \in \{\mathrm{in,out}\}}\mathcal{L}_{1}[\rho_{0};\sigma_{\alpha ,m}^{-},\sigma_{\alpha ,m}^{+}] \\ + \sum_ {m, n} \operatorname {R e} \left[ U _ {m n} \right] \mathcal {L} _ {1} \left[ \rho_ {0}; \sigma_ {\text {o u t}, m} ^ {+}, \sigma_ {\text {i n}, n} ^ {-} \right] + \mathrm {H . c .}, \tag {8} \\ \end{array}
$$

defined in terms of the Lindblad superoperator

$$
\mathcal {L} _ {1} \left[ \rho_ {0}; A, B \right] = B \rho_ {0} A - \frac {1}{2} \left\{\rho_ {0}, A B \right\}. \tag {9}
$$

The dissipation terms in Eq. (8) are consistent with the application of Fermi's golden rule to the degrees of freedom of this system. The  $\mathrm{Re}[U_{nm}]$  factors accompanying the nonlocal spin-flip terms arise from the fact each spin can excite photons in both directions,  $k > 0$  and  $k < 0$ , and that the dependence on  $k$  of the corresponding matrix elements for the associated transitions satisfies  $U(-k) = U(k)^*$  (cf. Appendix A).

# IV. APPLICATIONS

# A. Quantum simulation of spin models and spin-boson sampling

Working in the resonator regime, Eq. (3) opens the door to the simulation of any bipartite spin or hard-core boson model. More precisely, for any bipartite spin-spin interaction described by a real and symmetric matrix  $J$ , we can identify a unitary matrix  $U$  such that  $J \propto \mathrm{Re}[U]$  in an elementwise manner. The procedure for this would start by diagonalizing  $J = W^{\dagger} \Lambda W$ , for a certain unitary transformation  $W$  and a diagonal form  $\Lambda_{mn} = \lambda_m \delta_{mn}$ . We then would find out the largest eigenvalue  $\delta = \max |\Lambda_{mm}|$  and construct  $U = W^{\dagger} \exp (i\Theta)W$ , where the diagonal matrix  $\Theta_{mn} = \theta_m \delta_{mn}$  is chosen such that  $\cos (\theta_m) = \lambda_m / \delta$ .

A very relevant subset of problems in this context corresponds to spin sampling. In this case  $U \in SO(M) \in \mathbb{R}^{M \times M}$  would be a random orthogonal matrix drawn from the Haar measure. As it was proven in Ref. [26], an  $XY$  model with random, long-range interactions implements a short-time dynamics that is as complex as boson sampling. Our resonator setup provides a possible physical implementation of this idea. More precisely, if we excite  $N \ll M$  input spins and probe the output qubits after a time  $T \simeq \pi / \delta$ , the distribution of excitations in this subsystem would be described by the permanent of an  $N \times N$  minor of  $U$ , just as in the case of boson sampling [13]. Provided that  $M$  is large enough, the resulting dynamics would be classically hard to simulate.

# B. Dissipative regime and dark states

It is also interesting to take the opposite limit in which coherent tunneling is completely suppressed and we only

have collective dissipation. In this case,  $U = O$ , where  $O$  is an orthogonal transformation, and we can write the master equation as

$$
\frac {d \rho_ {0}}{d t} = \Gamma \mathcal {L} _ {O} [ \rho_ {0} ] = \Gamma \sum_ {m = 1} ^ {M} \mathcal {L} _ {1} [ \rho_ {0}; S _ {m} ^ {-}, S _ {m} ^ {+} ], \tag {10}
$$

in terms of collective spin operators

$$
S _ {m} ^ {+} = \frac {1}{\sqrt {2}} \left(\sigma_ {\text {i n}, m} ^ {+} + \sum_ {n} O _ {n m} \sigma_ {\text {o u t}, n} ^ {+}\right). \tag {11}
$$

We may now look for stationary states, solving the equation  $\mathcal{L}_O[\rho_0] = 0$ . Besides the trivial stationary solution that is the ground state  $|0\rangle = \otimes_{m=1}^{2M} |\downarrow m\rangle$ , we find  $M$  exact dark states  $W^{+}|0\rangle$  of the dynamics that correspond to delocalized spin excitations. These states, which are created by the operators

$$
W _ {m} ^ {+} = \frac {1}{\sqrt {2}} \left(\sum_ {n} O _ {m n} \sigma_ {\text {i n}, n} ^ {+} - \sigma_ {\text {o u t}, m} ^ {+}\right), \tag {12}
$$

are called dark states because they are exactly decoupled from the photonic fields. The states (12) appear as a generalization of the singlet states [12] that are the dark states of a system consisting of two qubits interacting with a lossless photonic waveguide.

In addition to these exact dark states, in our problem we also find other quasistationary states that are constructed by repeatedly applying different  $W_{m}^{+}$ operators. As explained in Appendix C, we find that a state with  $N$  distinct dark-state quasiparticle excitations decays at the rate

$$
\gamma_ {N} = \Gamma \sqrt {\sum_ {n = 2} ^ {N} \frac {(- 1) ^ {n}}{2 ^ {n + 1}} \frac {N !}{(N - n) !} \frac {n !}{M ^ {n}}}, \tag {13}
$$

with  $\gamma_{1} := 0$ . Thus, in the very dilute limit,  $\gamma_{N}$  can be very small and the resulting states may be regarded as de facto dark states. This limit of diluteness is reached even for moderate circuit sizes. We have verified this by performing a Monte Carlo simulation of the circuit and estimating the decay rates with up to  $M = 50$  modes and up to  $N = 5$  excitations. These results are shown in Fig. 2 alongside the theoretical predictions.

# C. Adiabatic preparation of boson sampling states

An attractive feature of model (3) is that it can be used to adiabatically prepare the boson sampling state. Given a random unitary transformation  $U$  sampled with the Haar measure, the boson sampling state with  $N$  excitations in  $M$  modes is given by

$$
\left| \phi_ {\mathrm {B S}} \right\rangle = \prod_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} U _ {m n} a _ {m} ^ {\dagger} | 0 \rangle . \tag {14}
$$

This state is the one obtained by injecting  $N$  bosons in the first  $N \ll M$  modes of a multiport interferometer implementing the transformation  $U$ . We now show how to encode an

![](images/3cb07b9b29a7184a86222b7d2ea369e5e6d08a41858e0f9be016f5b9fdfcc0ee.jpg)  
FIG. 2. Effective decay rates averaged over random unitary operators  $U$  for different numbers of modes  $M$  and quasiparticle filling  $N = 2, \ldots, 5$ . Dashed lines represent the analytic results (13) for increasing values of  $N$  (from bottom to top), while the corresponding sets of points with error bars represent the decay rates estimated from a Monte Carlo simulation of the system.

approximately similar state in the qubits:

$$
\left| \psi_ {\mathrm {B S}} \right\rangle = \prod_ {n = 1} ^ {N} \sum_ {m = 1} ^ {M} U _ {m n} \sigma_ {\text {o u t}, m} ^ {+} | 0 \rangle + O (\varepsilon), \tag {15}
$$

where the error  $\varepsilon = \psi -\phi$  can be made arbitrarily small.

Our protocol builds on the results of Ref. [26], which states that the dynamics of a multimode bosonic system with few excitations  $(N\ll M)$  can be approximated by the evolution of a spin model with a similarly small number of excitations. The protocol assumes that we can build a random spin-spin interaction of the form (3) where  $J = U\in \mathbb{R}^{M\times M}$  is our randomly sampled orthogonal transformation. We also assume that in the effective model we can tune the energies of the input and output qubits, using external fields. The time-dependent Hamiltonian reads

$$
H = H _ {\text {s p i n}} + \epsilon \sum_ {m = 1} ^ {M} \left([ 1 - \lambda (t) ] \sigma_ {\text {o u t}, m} ^ {z} + \lambda (t) \sigma_ {\text {i n}, m} ^ {z}\right). \tag {16}
$$

The switching function  $\lambda(t)$  interpolates smoothly  $\lambda(0) = 1$  and  $\lambda(T) = 0$  over a long time  $T$ . We start with an initial state  $|\psi(0)\rangle = \prod_{m=1}^{N} \sigma_{\mathrm{in},m}^{+} |0\rangle$ , in a regime in which  $\epsilon \lambda(0) \gg |J|$  prevents tunneling. We then adiabatically shift  $\lambda$  to 0, until at time  $T$  we have  $\lambda(T) = 0$ . As shown in Appendix D, provided  $\dot{\lambda}$  remains small compared to  $|J|$ , the system should then converge to a ground state that consists of  $N$  excitations in the output qubits. In other words,  $|\psi(T)\rangle \simeq |\psi_{\mathrm{BS}}\rangle$ . The resulting state should be arbitrarily close to a boson sampling state, provided that the number of excitations is dilute enough.

# V. CONCLUSIONS

We have presented a setup and a model for engineering photon-mediated interactions between two-level emitters using optical circuits. This idea represents a rather general paradigm that encompasses and extends previous approaches

towards similar goals in one-dimensional photonic environments [11,12]. Using the tools in this paper we can reverse-engineer arbitrary bipartite interactions, such as high-dimensional  $XY$  spin Hamiltonians, finding the optical circuits that implement them, and rely on reconfigurable circuits [7] or single-purpose devices [5,6] to implement them.

We have discussed various applications of the resulting setups, which range from studies of quantum complexity and quantum supremacy through short time evolution [26] or through the preparation of boson sampling states to using the optical circuit dark states for quantum information and quantum optics applications.

These applications can be tested in a variety of state-of-the-art platforms. For instance, setups with trapped atoms in photonic crystals have demonstrated strong light-matter interactions [10] that are sufficient for implementing the dissipative models in this work. Solid-state devices such as quantum dots have also achieved sufficient coupling strengths [9], but in this case inhomogeneous broadening of levels might make them more suitable for studying disorder in our spin Hamiltonians.

All our proposals can be extended to work with superconducting quantum circuits, where microwave transformations such as beam splitters have been demonstrated [27,28]. In this case, the enhanced light-matter interaction allows the ultrastrong coupling regime to reach the continuum [29] and we can no longer apply the Markov approximations. However, rather simple generalizations of our treatment based on the polaron transformation [30,31] show that we still recover spin-spin interactions, but now they become of the Ising type. This opens the door to simulating other types of dissipative phase transitions [32-35], but also opens questions regarding the quantum complexity of Ising models and their time evolution.

Another important generalization would be using only a subset of qubits, or placing qubits at a subset of ports and blocking other channels with mirrors or closed loops. These and other designs, which allow implementing more general spin Hamiltonians which are not bipartite, will be explored in further work.

Finally, this work has been developed under reasonable assumptions of Markovianity and long photon wave packets, where the time for photons to travel between qubits greatly exceeds the spontaneous emission rate. These open interesting questions about how to generalize our theoretical framework to include retardation effects.

# ACKNOWLEDGMENTS

The authors acknowledge support from the European Union FP7 project PROMISCE, Spanish MINECO Projects No. FIS2012-33022 and No. FIS2015-70856-P, and CAM Research Network QUITEMAD+. D.G.O. was supported by FPI Grant No. BES-2013-066486. B.P. and A.A.-G. acknowledge the Air Force of Scientific Research for support under Award No. FA9550-12-1-0046. A.A.-G. acknowledges support from the Army Research Office under Award No. W911NF-15-1-0256. B.P. and A.A.-G. acknowledge the Defense Security Science Engineering Fellowship managed by the Office of Naval Research under Award No. N00014-16-1-2008.

# APPENDIX A: WAVES FROM OPTICAL TRANSFORMATIONS

An arbitrary  $M \times M$  optical transformation  $U_{mn}$  may be decompose into a series of at most  $M^2$  interferometers and phase shifters [1,2] of the form shown in Fig. 3. Assuming this optical interpretation of the circuit, we find that the  $l$ th operation will couple  $m$ th and  $n$ th modes through the unitary transformation

$$
\binom {a _ {m} ^ {\prime} (+ k)} {a _ {n} ^ {\prime} (+ k)} = U _ {m n} (+ k) \binom {a _ {m} (+ k)} {a _ {n} (+ k)}, \tag {A1}
$$

which, following the conventions in Ref. [1], depends on two angular parameters:

$$
U _ {l} \left(\phi_ {l}, \theta_ {l}\right) := \left( \begin{array}{c c} \sin \left(\theta_ {l} v _ {k}\right) e ^ {i \phi_ {l} v _ {k} / 2} & \cos \left(\theta_ {l} v _ {k}\right) e ^ {i \phi_ {l} v _ {k} / 2} \\ \cos \left(\theta_ {l} v _ {k}\right) & - \sin \left(\theta_ {l} v _ {k}\right) \end{array} \right). \tag {A2}
$$

Note that the unitary transformation also depends on the momentum of the photon.

Taking as reference the unitary transformation that is implemented for the photons that are resonant with the qubits,  $k = k_{\Delta}$ , a general transformation will typically read

$$
U (+ k) = \prod_ {n = 1} ^ {M} U _ {n} \left(\phi_ {n}, \theta_ {n}, v _ {k}\right). \tag {A3}
$$

An important question is what happens to the photons propagating in the opposite direction. It is not difficult to convince oneself that by having a backward-moving plane wave we will obtain the relation

$$
\vec {a} (- k) = \prod_ {n = M} ^ {1} U _ {n} ^ {T} \left(\phi_ {n}, \theta_ {n}, v _ {k}\right) \vec {a} ^ {\prime} (- k), \tag {A4}
$$

where  $U^T$  arises from the particular form of the optical transformation (A2). Since the product of unitaries runs in an opposite order to that of Eq. (A3), when we apply the inverse transformations to extract  $\vec{a}'$  we recover the simple result

$$
\vec {a} ^ {\prime} (- k) = \prod_ {n = 1} ^ {M} U _ {n} ^ {*} \left(\phi_ {n}, \theta_ {n}, v _ {k}\right) \vec {a} (- k) =: U ^ {*} (+ k) \vec {a} (- k). \tag {A5}
$$

In other words, we have found the relationship

$$
U (- k) = U ^ {*} (+ k), \tag {A6}
$$

which is a generalization of the relation between forward-moving and backward-moving waves,  $\exp (\pm ikx)$ , in one-dimensional waveguides.

![](images/18d9cbdb9275a5766db45eef98af66da102a06a5336cdb6dfc0b4e7d24a738fd.jpg)  
FIG. 3. A two-port interferometer built with two 50-50 beam splitters and two phase shifters,  $\theta$  and  $\phi$ , implements the most general unitary transformation from input modes  $(a_{i}, a_{j})$  into output modes  $(a_{m}^{\prime}, a_{n}^{\prime})$ .

# APPENDIX B: DERIVATION OF A MASTER EQUATION FOR THE OPEN CIRCUIT

A master equation that describes the effective qubit dynamics generated by the Hamiltonian (2) may be derived in the Markovian regime. This limit assumes that the traveling time of the photons through the optical circuit is much shorter than the spontaneous emission rate of the qubits, which is of the order of the spectral function  $J(\omega) = \pi \sum_{k} g_{k}^{2} \delta(\omega_{k} - \omega)$  at the resonance point  $\omega = \Delta$ . We also assume a weak coupling limit  $g_{k} \ll \Delta$ ,  $\omega_{k}$ . Under these approximations, a procedure similar to the one described in the Supplemental Material of Ref. [36] may be followed.

We start from the Liouville-von Neumann equation after having performed the Born-Markov approximation:

$$
\begin{array}{l} \frac {d \rho_ {0}}{d t} = - \int_ {0} ^ {\infty} d \tau \operatorname {t r} _ {B} \left\{H _ {I} (t), [ H _ {I} (t - \tau), \rho_ {0} (t) \rho_ {B} ] \right\} \\ = + \int_ {0} ^ {\infty} d \tau \operatorname {t r} _ {B} \left\{H _ {I} (t - \tau) \rho_ {0} (t) \rho_ {B} H _ {I} (t) \right\} + \mathrm {H . c}. \\ - \int_ {0} ^ {\infty} d \tau \operatorname {t r} _ {B} \left\{H _ {I} (t) H _ {I} (t - \tau) \rho_ {0} (t) \rho_ {B} \right\} + \mathrm {H . c .} \tag {B1} \\ \end{array}
$$

Here  $H_{I}(t)$  refers to the interacting part of the Hamiltonian (2) in the interaction picture, and  $\mathrm{tr}_B$  refers to the partial trace over the bosonic degrees of freedom.

The next step consists of expanding these expressions and performing the rotating wave approximation, while assuming that the equilibrium state of the photonic degrees of freedom is close to the ground state. This yields the following for the first term in Eq. (B1):

$$
\begin{array}{l} \int_ {0} ^ {\infty} d \tau \operatorname {t r} _ {B} \left\{H _ {I} (t - \tau) \rho_ {0} (t) \rho_ {B} H _ {I} (t) \right\} \\ = \pi \sum_ {m, k} g _ {k} ^ {2} \delta \left(\omega_ {k} - \Delta\right) \sum_ {\alpha \in \{\text {i n , o u t} \}} \sigma_ {\alpha , m} ^ {-} \rho_ {0} \sigma_ {\alpha , m} ^ {+} + i \Xi \\ + \pi \sum_ {m, n, k} g _ {k} ^ {2} \delta \left(\omega_ {k} - \Delta\right) \mathcal {U} _ {n m} (k) \sigma_ {\text {i n}, m} ^ {-} \rho_ {0} \sigma_ {\text {o u t}, m} ^ {+} + \mathrm {H . c .}, \tag {B2} \\ \end{array}
$$

where  $\Xi \equiv \Xi[\rho_0, \ldots]$  is a complicated functional which is Hermitian and therefore disappears when adding the term (B2) to its complex conjugate in Eq. (B1).

Following the same procedure with the second term in Eq. (B1) gives a more complicated contribution:

$$
\begin{array}{l} \int_ {0} ^ {\infty} d \tau \operatorname {t r} _ {B} \left\{H _ {I} (t) H _ {I} (t - \tau) \rho_ {0} (t) \rho_ {B} \right\} \\ = \pi \sum_ {m, k} g _ {k} ^ {2} \delta \left(\omega_ {k} - \Delta\right) \sum_ {\alpha \in \{\text {i n , o u t} \}} \sigma_ {\alpha , m} ^ {+} \sigma_ {\alpha , m} ^ {-} \rho_ {0} \\ + \pi \sum_ {m, n, k} g _ {k} ^ {2} \delta (\omega_ {k} - \Delta) U _ {n m} (k) \sigma_ {\text {i n}, m} ^ {+} \sigma_ {\text {o u t}, m} ^ {-} \rho_ {0} + \mathrm {H . c}. \\ - i \mathrm {P V} \left\{\sum_ {m, k} \frac {g _ {k} ^ {2}}{\omega_ {k} - \Delta} \right\} \sum_ {\alpha \in \{\text {i n , o u t} \}} \sigma_ {\alpha , m} ^ {+} \sigma_ {\alpha , m} ^ {-} \rho_ {0} \\ - i \mathrm {P V} \left\{\sum_ {m, n, k} \frac {g _ {k} ^ {2}}{\omega_ {k} - \Delta} U _ {n m} (k) \sigma_ {\text {i n}, m} ^ {+} \sigma_ {\text {o u t}, m} ^ {-} \rho_ {0} + \mathrm {H . c .} \right\} \\ \end{array}
$$

$$
\begin{array}{l} - i \mathrm {P V} \left\{\sum_ {m, k} \frac {g _ {k} ^ {2}}{\omega_ {k} + \Delta} \right\} \sum_ {\alpha \in \{\text {i n , o u t} \}} \sigma_ {\alpha , m} ^ {-} \sigma_ {\alpha , m} ^ {+} \rho_ {0} \\ - i \mathrm {P V} \left\{\sum_ {m, n, k} \frac {g _ {k} ^ {2}}{\omega_ {k} + \Delta} U _ {n m} (k) \sigma_ {\text {i n}, m} ^ {-} \sigma_ {\text {o u t}, m} ^ {+} \rho_ {0} + \mathrm {H . c .} \right\}, \tag {B3} \\ \end{array}
$$

where PV means that the Cauchy principal value of the integrals in momenta  $k$  should be computed.

The aforementioned integrations in  $k$  may be substituted by integrals in the photon frequency  $\omega \equiv \omega_{k}$  by making use of the property (A6) of  $U(k)$ , and including the density of states  $\mathcal{D}(\omega) = d_k\omega_k$ . After this change of variable, all the integrals can be evaluated explicitly; either as a consequence of the definition of the  $\delta$  distribution or by using the Kramers-Kronig relations,

$$
\operatorname {R e} \{f (\Delta) \} = \frac {1}{\pi} \int_ {- \infty} ^ {+ \infty} \frac {d \omega}{\omega - \Delta} \operatorname {I m} \{f (\omega) \}, \tag {B4}
$$

$$
\operatorname {I m} \{f (\Delta) \} = - \frac {1}{\pi} \int_ {- \infty} ^ {+ \infty} \frac {d \omega}{\omega - \Delta} \operatorname {R e} \{f (\omega) \}, \tag {B5}
$$

which hold provided that  $f(\omega)$  is an analytic function in the upper half of the complex plane.

Besides a renormalization of the qubit frequencies, which does not affect the dynamics in the interaction picture, the result of integrating Eqs. (B2) and (B3) is

$$
\begin{array}{l} \int_ {0} ^ {\infty} d \tau \operatorname {t r} _ {B} \left\{H _ {I} (t - \tau) \rho_ {0} (t) \rho_ {B} H _ {I} (t) \right\} + \mathrm {H . c .} \\ = \Gamma \sum_ {m} \left(\sigma_ {\text {o u t}, m} ^ {-} \rho_ {0} \sigma_ {\text {o u t}, m} ^ {+} + \sigma_ {\text {i n}, m} ^ {-} \rho_ {0} \sigma_ {\text {i n}, m} ^ {+}\right) \\ + \Gamma \sum_ {m, n} \operatorname {R e} \left[ U _ {n m} \right] \sigma_ {\text {o u t}, n} ^ {-} \rho_ {0} \sigma_ {\text {i n}, m} ^ {+} + \mathrm {H . c .}, \tag {B6} \\ \end{array}
$$

$$
\begin{array}{l} \int_ {0} ^ {\infty} d \tau \operatorname {t r} _ {B} \left\{H _ {I} (t) H _ {I} (t - \tau) \rho_ {0} (t) \rho_ {B} \right\} \\ = \frac {\Gamma}{2} \sum_ {m} \left(\sigma_ {\text {o u t}, m} ^ {+} \sigma_ {\text {o u t}, m} ^ {-} + \sigma_ {\text {i n}, m} ^ {+} \sigma_ {\text {i n}, m} ^ {-}\right) \rho_ {0} \\ + \frac {\Gamma}{2} \sum_ {m, n} U _ {n m} \left(\sigma_ {\text {o u t}, n} ^ {+} \sigma_ {\text {i n}, m} ^ {-} + \sigma_ {\text {i n}, m} ^ {+} \sigma_ {\text {o u t}, n} ^ {-}\right) \rho_ {0}, \tag {B7} \\ \end{array}
$$

where the spontaneous emission rate parameter

$$
\Gamma = J (\Delta) = 2 \bar {g} _ {\Delta} ^ {2} \mathcal {D} (\Delta) \tag {B8}
$$

is the natural time scale for the dipolar qubit-waveguide interaction and  $U \equiv U(k_{\Delta})$ .

Substituting Eqs. (B6) and (B7) into (B1) gives as a result the effective master equation (6), with the different contributions discussed in Sec. III B.

# APPENDIX C: CROWDING OF ASYMPTOTIC SOLUTIONS

The stationary solutions (12) obtained in Sec. IV B are delocalized excitations that, by construction, are not dissipated according to the dynamics described by the master equation (10). However, there is no prescription in these dynamics preventing a state with more than one such an excitation

from dissipating. Even though this point is rigorously true, under certain conditions the decay of these "crowded" dark states may be superseded by the typical time scale  $1 / \Gamma$  of the effective dynamics.

The magnitude of the decay of a crowded dark state,

$$
| \psi_ {\text {d a r k}} (j _ {1}, \dots , j _ {N}) \rangle = \prod_ {\alpha = 1} ^ {N} W _ {j _ {\alpha}} ^ {+} | 0 \rangle , \tag {C1}
$$

is determined, in units of  $\Gamma$ , by the norm of the state resulting from the application of a collective annihilator  $S_{i}^{-}$  on this state:

$$
\mathcal {N} = \sqrt {\langle 0 | \prod_ {\alpha = N} ^ {1} W _ {j _ {\alpha}} ^ {-} S _ {i} ^ {+} S _ {i} ^ {-} \prod_ {\beta = 1} ^ {N} W _ {j _ {\beta}} ^ {+} | 0 \rangle}, \tag {C2}
$$

where it is assumed that all  $j_{\alpha}$  indices are different.

The norm (C2) can be calculated by commuting the  $S_{i}^{-}$  operator with the string of  $W_{j_{\beta}}^{+}$  operators that lay to the right, following at the same time an identical path by commuting  $S_{i}^{+}$  with the  $W_{j_{\alpha}}^{-}$  operators to the left. The commutator of  $S_{i}^{-}$  and  $W_{j_{\alpha}}^{+}$  is

$$
\left[ S _ {i} ^ {-}, W _ {j _ {\beta}} ^ {+} \right] = \frac {1}{2} O _ {j _ {\beta} i} \left(\sigma_ {\text {o u t}, j _ {\beta}} ^ {z} - \sigma_ {\text {i n}, i} ^ {z}\right) \tag {C3}
$$

and is required in order to conduct these operations. We also need to know that

$$
\left[ \sigma_ {\text {i n}, j _ {\alpha}} ^ {z}, W _ {j _ {\beta}} ^ {\pm} \right] = \pm \sqrt {2} O _ {j _ {\beta} j _ {\alpha}} \sigma_ {\text {i n}, j _ {\alpha}} ^ {\pm}, \tag {C4}
$$

$$
\left[ \sigma_ {\text {o u t}, j _ {\alpha}} ^ {z}, W _ {j _ {\beta}} ^ {\pm} \right] = \mp \sqrt {2} \delta_ {j _ {\beta} j _ {\alpha}} \sigma_ {\text {o u t}, j _ {\alpha}} ^ {\pm}. \tag {C5}
$$

After each successive commutation (C3)-(C5) performed on Eq. (C2), we get either terms with the same number of Pauli matrices or terms with one less Pauli matrix. Most of these are 0 upon explicit inspection, either because  $(\sigma_{\mathrm{out},j_{\beta}}^{z} - \sigma_{\mathrm{in},i}^{z})|0\rangle = 0$ , or as a consequence of having assumed that no  $j_{\alpha}$  index is repeated, or because the application of (C4) leaves a vanishing product of Pauli matrices.

The only nonvanishing terms are those which depend on quadratic powers of sets of  $2,3,\ldots ,N$  coefficients of the  $i$ th column of the unitary transformation  $U$ , with the rows being chosen among the dark-state indices  $j_{\alpha}$  appearing in Eq. (C1):

$$
\mathcal {N} = \sqrt {\sum_ {\alpha <   \beta} \frac {O _ {j _ {\alpha} i} ^ {2} O _ {j _ {\beta} i} ^ {2}}{2} \left[ 1 - \sum_ {\gamma \neq \alpha , \beta} \frac {O _ {j _ {\gamma} i} ^ {2}}{2} (1 - \dots) \right]}. \tag {C6}
$$

When averaged over the Haar measure, the expected values of the matrix elements of  $O$  are  $\mathcal{E}(O_{ji}) \sim O(\frac{1}{\sqrt{M}})$ . Counting the number of different possible combinations of  $n < N$  coefficients appearing in Eq. (C6) yields

$$
\begin{array}{l} \mathcal {E} (\mathcal {N} ^ {2}) = \sum_ {n = 2} ^ {N} \frac {(- 1) ^ {n}}{2 ^ {n - 1}} \binom {N} {2} P _ {n - 2} ^ {N - 2} \binom {n} {2} P _ {n - 2} ^ {n - 2} \\ = \sum_ {n = 2} ^ {N} \frac {(- 1) ^ {n}}{2 ^ {n + 1}} \frac {N !}{(N - n) !} \frac {n !}{M ^ {n}}. \tag {C7} \\ \end{array}
$$

Where the decay parameter of these quasistationary dark states is given by  $\Gamma \times \mathcal{E}(\mathcal{N})$ . Considering the dilute limit  $M \gg$

$N > 1$ , it follows that  $\mathcal{E}(\mathcal{N}) \sim M^{-1} \ll 1$ . The consequence of this being that the typical time scales associated with the decay of a state with multiple dark-state excitations are much larger than the characteristic time scale  $\Gamma^{-1}$  of the dynamics described by Eq. (10).

# APPENDIX D: ADIABATIC CONNECTION TO BOSON SAMPLING

Let us start by proving that, when using harmonic oscillators and nonclassical states, it is possible to adiabatically prepare a boson sampling distribution. The setup that we have in mind is a collection of  $M$  input and  $M$  output bosonic modes (i.e., resonators) connected between themselves through an optical transformation such as the one in Fig. 1. Provided that these resonators satisfy the same requirements as in Sec. III B, we will be able to write down an effective Hamiltonian of the form

$$
\begin{array}{l} H _ {\mathrm {B S}} = \sum_ {i} \tilde {\Delta} (a _ {\mathrm {i n}, n} ^ {\dagger} a _ {\mathrm {i n}, n} + a _ {\mathrm {o u t}, n} ^ {\dagger} a _ {\mathrm {o u t}, n}) \\ + \sum_ {m, n} J _ {n, m} \left(a _ {\text {o u t}, n} ^ {\dagger} a _ {\text {i n}, m} + \mathrm {H . c}\right) \\ + \epsilon \sum_ {n} ([ 1 - \lambda (t) ] a _ {\text {o u t}, n} ^ {\dagger} a _ {\text {o u t}, n} + \lambda (t) a _ {\text {i n}, n} ^ {\dagger} a _ {\text {i n}, n}). \quad (\mathrm {D} 1) \\ \end{array}
$$

Since  $J_{n,m}\propto U_{n,m}$  , we may define new collective operators,

$$
c _ {\text {o u t}, m} = \sum_ {n} U _ {m n} a _ {\text {o u t}, n}, \tag {D2}
$$

which diagonalize the previous Hamiltonian

$$
\begin{array}{l} H _ {\mathrm {B S}} = \sum_ {i} \left(\Delta_ {\mathrm {i n}} (t) a _ {\mathrm {i n}, n} ^ {\dagger} a _ {\mathrm {i n}, n} + \Delta_ {\mathrm {o u t}} (t) a _ {\mathrm {o u t}, n} ^ {\dagger} a _ {\mathrm {o u t}, n}\right) \\ + \delta \sum_ {m} \left(c _ {\text {o u t}, n} ^ {\dagger} a _ {\text {i n}, m} + \mathrm {H . c}\right), \tag {D3} \\ \end{array}
$$

where we have introduced  $\Delta_{\mathrm{in}} = \tilde{\Delta} +\epsilon \lambda (t)$  and  $\Delta_{\mathrm{out}}(t) =$

$\tilde{\Delta} + \epsilon [1 - \lambda(t)]$ . It is now rather simple to apply the adiabatic theorem to each of the  $M$  local Hamiltonians that connect  $a_{\mathrm{in},m}$  to the corresponding  $c_{\mathrm{out},m}$ . The result is that by switching off  $\lambda(t)$  in a time  $T \gg 1 / |\delta|$ , and provided  $|\epsilon| \gg |\delta|$ , we will adiabatically transfer the state  $a_{\mathrm{in},m}^{\dagger}|0\rangle$  onto an output state  $c_{\mathrm{out},m}^{\dagger}|0\rangle$ . This way, if we start with  $N$  excitations,

$$
| \phi (0) \rangle = \prod_ {m = 1} ^ {N} a _ {\mathrm {i n}, m} ^ {\dagger} | 0 \rangle , \tag {D4}
$$

the final state will be, up to small corrections, the output of the interferometer with  $N$  input photons,

$$
| \phi (T) \rangle \simeq \prod_ {m = 1} ^ {N} \sum_ {n} U _ {n m} a _ {\text {o u t}, n} ^ {\dagger} | 0 \rangle . \tag {D5}
$$

It remains to be proven that we achieve a similar state when using the spin Hamiltonian (3) and the input state

$$
| \psi (0) \rangle = \prod_ {m} \sigma_ {m} ^ {+} | 0 \rangle . \tag {D6}
$$

For this we invoke the result in Ref. [26] which establishes that the distance between the hard-core boson state  $|\psi(t)\rangle$ , evolved under Eq. (3), and the soft-boson state  $|\phi(t)\rangle$ , evolved under Eq. (D1), is bounded by

$$
\| \psi - \phi \| \leqslant \int_ {0} ^ {T} d t \| Q H _ {\mathrm {B S}} P _ {1 \text {p a i r}} \| _ {2} \| P _ {1 \text {p a i r}} \phi (t) \| _ {2}, \tag {D7}
$$

where  $Q$  and  $P_{1\mathrm{pair}}$  project onto the hard-core subspace and the space of states with at most one bunched mode. Therefore, it can be concluded that

$$
\| \psi - \phi \| \leqslant O \left(T \frac {N ^ {2}}{\sqrt {M}}\right), \tag {D8}
$$

so that it becomes possible to decrease the error arbitrarily by either making the system more dilute or adjusting the evolution time.

[1] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, Phys. Rev. Lett. 73, 58 (1994).  
[2] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley, arXiv:1603.08788.  
[3] T. Lund-Hansen, S. Stobbe, B. Julsgaard, H. Thyrestrup, T. Sinner, M. Kamp, A. Forchel, and P. Lodahl, Phys. Rev. Lett. 101, 113903 (2008).  
[4] A. Goban, C.-L. Hung, S.-P. Yu, J. D. Hood, J. A. Muniz, J. H. Lee, M. J. Martin, A. C. McClung, K. S. Choi, D. E. Chang, O. Painter, and H. J. Kimble, Nat. Commun. 5, 3808 (2014).  
[5] A. Politi, M. J. Cryan, J. G. Rarity, S. Yu, and J. L. O'Brien, Science (New York, NY) 320, 646 (2008).  
[6] T. Meany, M. Gräfe, R. Heilmann, A. Perez-Leija, S. Gross, M. J. Steel, M. J. Withford, and A. Szameit, Laser Photonics Rev. 9, 363 (2015).  
[7] J. Carolan, C. Harrold, C. Sparrow, E. Martin-López, N. J. Russell, J. W. Silverstone, P. J. Shadbolt, N. Matsuda, M. Oguma, M. Itoh, G. D. Marshall, M. G. Thompson, J. C. F. Matthews, T. Hashimoto, J. L. O'Brien, and A. Laing, Science (New York, N.Y.) 349, 711 (2015).

[8] N. C. Harris, G. R. Steinbrecher, J. Mower, Y. Lahini, M. Prabhu, T. Baehr-Jones, M. Hochberg, S. Lloyd, and D. Englund, arXiv:1507.03406.  
[9] P. Lodahl, S. Mahmoodian, and S. Stobbe, Rev. Mod. Phys. 87, 347 (2015).  
[10] T. G. Tiecke, J. D. Thompson, N. P. de Leon, L. R. Liu, V. Vuletic, and M. D. Lukin, Nature (London) 508, 241 (2014).  
[11] D. E. Chang, A. S. Sørensen, P. R. Hemmer, and M. D. Lukin, Phys. Rev. Lett. 97, 053002 (2006).  
[12] A. Gonzalez-Tudela, D. Martin-Cano, E. Moreno, L. Martin-Moreno, C. Tejedor, and F. J. Garcia-Vidal, Phys. Rev. Lett. 106, 020501 (2011).  
[13] S. Aaronson and A. Arkhipov, in Proceedings of the 43rd Annual ACM Symposium on Theory of Computing (ACM, New York, 2011), Vol. 9, p. 143.  
[14] B. T. Gard, K. R. Motes, J. P. Olson, P. P. Rohde, and J. P. Dowling, An introduction to boson-sampling, in From Atomic to Mesoscale (World Scientific, Singapore, 2015), Chap. 8, pp. 167-192.

[15] M. A. Broome, A. Fedrizzi, S. Rahimi-Keshari, J. Dove, S. Aaronson, T. C. Ralph, and A. G. White, Science 339, 794 (2013).  
[16] J. B. Spring, B. J. Metcalf, P. C. Humphreys, W. S. Kolthammer, X.-M. Jin, M. Barbieri, A. Datta, N. Thomas-Peter, N. K. Langford, D. Kundys, J. C. Gates, B. J. Smith, P. G. R. Smith, and I. A. Walmsley, Science 339, 798 (2013).  
[17] M. Tillmann, B. Dakic, R. Heilmann, S. Nolte, A. Szameit, and P. Walther, Nat. Photonics 7, 540 (2013).  
[18] A. Crespi, R. Osellame, R. Ramponi, D. J. Brod, E. F. Galvao, N. Spagnolo, C. Vitelli, E. Maiorino, P. Mataloni, and F. Sciarrino, Nat. Photonics 7, 545 (2013).  
[19] C. Shen, Z. Zhang, and L.-M. Duan, Phys. Rev. Lett. 112, 050504 (2014).  
[20] K. R. Motes, A. Gilchrist, J. P. Dowling, and P. P. Rohde, Phys. Rev. Lett. 113, 120501 (2014).  
[21] B. Peropadre, G. G. Guerreschi, J. Huh, and A. Aspuru-Guzik, arXiv:1510.08064.  
[22] K. R. Motes, J. P. Olson, E. J. Rabeaux, J. P. Dowling, S. J. Olson, and P. P. Rohde, Phys. Rev. Lett. 114, 170802 (2015).  
[23] J. Huh, G. G. Guerreschi, B. Peropadre, J. R. McClean, and A. Aspuru-Guzik, Nat. Photonics 9, 615 (2015).  
[24] When  $U$  is sampled randomly from the set of unitaries using the Haar measure.

[25] J. Preskill, arXiv:1203.5813.  
[26] B. Peropadre, A. Aspuru-Guzik, and J. J. Garcia-Ripoll, arXiv:1509.02703.  
[27] E. Hoffmann, F. Deppe, T. Niemczyk, T. Wirth, E. P. Menzel, G. Wild, H. Huebl, M. Mariantoni, T. Weiβl, A. Lukashenko, A. P. Zhuravel, A. V. Ustinov, A. Marx, and R. Gross, Appl. Phys. Lett. 97, 222508 (2010).  
[28] M. Pechal, J.-C. Besse, M. Mondal, M. Oppliger, S. Gasparinetti, and A. Wallraff, arXiv:1606.01031, Bull. Am. Phys. Soc. (2016).  
[29] P. Forn-Díaz, J. J. García-Ripoll, B. Peropadre, M. A. Yurtalan, J. L. Orgiazzi, R. Belyansky, C. M. Wilson, and A. Lupascu, arXiv:1602.00416.  
[30] A. Kurcz, A. Bermudez, and J. J. García-Ripoll, Phys. Rev. Lett. 112, 180405 (2014).  
[31] G. Díaz-Camacho, A. Bermudez, and J. J. García-Ripoll, Phys. Rev. A 93, 043843 (2016).  
[32] D. Rossini and R. Fazio, Phys. Rev. Lett. 99, 186401 (2007).  
[33] G. Falci, R. Fazio, G. M. Palma, J. Siewert, and V. Vedral, Nature (London) 407, 355 (2000).  
[34] F. Nissen, S. Schmidt, M. Biondi, G. Blatter, H. E. Tureci, and J. Keeling, Phys. Rev. Lett. 108, 233603 (2012).  
[35] J. Eisert, M. P. Müller, and C. Gogolin, Nat. Phys. 11, 124 (2015).  
[36] A. González-Tudela and D. Porras, Phys. Rev. Lett. 110, 080502 (2013).