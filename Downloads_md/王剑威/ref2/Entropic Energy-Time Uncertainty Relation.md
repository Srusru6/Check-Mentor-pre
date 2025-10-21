# Entropic Energy-Time Uncertainty Relation

Patrick J. Coles, $^{1}$  Vishal Katariya, $^{2}$  Seth Lloyd, $^{3,4}$  Iman Marvian, $^{5}$  and Mark M. Wilde $^{2,6}$

$^{1}$ Theoretical Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA

$^{2}$ Hearne Institute for Theoretical Physics, Department of Physics and Astronomy,

Louisiana State University, Baton Rouge, Louisiana 70803, USA

$^{3}$ Department of Mechanical Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA

$^{4}$ Research Laboratory of Electronics, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139, USA

$^{5}$ Departments of Physics & Electrical and Computer Engineering, Duke University, Durham, North Carolina 27708, USA

$^{6}$ Center for Computation and Technology, Louisiana State University, Baton Rouge, Louisiana 70803, USA

![](images/01713106b37635d9270d9c0da8f63b5ac2f1c2f6614433ea014752eb621b7392.jpg)

(Received 11 June 2018; published 12 March 2019)

Energy-time uncertainty plays an important role in quantum foundations and technologies, and it was even discussed by the founders of quantum mechanics. However, standard approaches (e.g., Robertson's uncertainty relation) do not apply to energy-time uncertainty because, in general, there is no Hermitian operator associated with time. Following previous approaches, we quantify time uncertainty by how well one can read off the time from a quantum clock. We then use entropy to quantify the information-theoretic distinguishability of the various time states of the clock. Our main result is an entropic energy-time uncertainty relation for general time-independent Hamiltonians, stated for both the discrete-time and continuous-time cases. Our uncertainty relation is strong, in the sense that it allows for a quantum memory to help reduce the uncertainty, and this formulation leads us to reinterpret it as a bound on the relative entropy of asymmetry. Because of the operational relevance of entropy, we anticipate that our uncertainty relation will have information-processing applications.

DOI: 10.1103/PhysRevLett.122.100401

Introduction.-The uncertainty principle is one of the most iconic implications of quantum mechanics, stating that there are pairs of observables that cannot be simultaneously known. It was first proposed by Heisenberg [1] for the position  $\hat{q}$  and momentum  $\hat{p}$  observables and then rigorously stated by Kennard [2] in the familiar form using standard deviations:  $\Delta \hat{q} \Delta \hat{p} \geq \hbar / 2$ . Robertson [3] later formulated a similar relation for a different class of observables, namely, for pairs of bounded Hermitian observables  $\hat{X}$  and  $\hat{Z}$  (e.g., the Pauli spin operators), as  $\Delta \hat{X} \Delta \hat{Z} \geq \frac{1}{2} |\langle [\hat{X}, \hat{Z}] \rangle|$ . Since then, many alternative formulations have been proven for similar Hermitian operator pairs (e.g., Refs. [4,5]).

Unfortunately, these relations do not apply to energy and time since time does not, in general, correspond to a Hermitian operator. In particular, Pauli's theorem states that the semiboundedness of a Hamiltonian precludes the existence of a Hermitian time operator, or in other words, if there was such an operator, then the Hamiltonian would be unbounded from below and thus unphysical [6]. Hence, formulating a general energy-time uncertainty relation is a nontrivial task. We point to Ref. [7] for an overview on time in quantum mechanics.

Nevertheless, the energy-time pair is of significant importance both fundamentally and technologically. Energy-time uncertainty was already discussed by the founders of quantum mechanics: Bohr, Heisenberg, Schrödinger, and Pauli (see Ref. [8] for a review). In the

special case of the harmonic oscillator, this pair corresponds to number and phase, and number-phase uncertainty is relevant to metrology [9], e.g., phase estimation in interferometry. The energy-time pair is arguably the most general observable pair in the sense that it applies to all physical systems (i.e., all systems have a Hamiltonian).

Despite the lack of a Hermitian observable associated with time, relations with the feel of energy-time uncertainty relations have been formulated. Mandelstam and Tamm [10] related the energy standard deviation  $\Delta E$  to the time  $\tau$  that it takes for a state to move to an orthogonal state:  $\tau \Delta E \geq (\pi \hbar / 2)$ . This relation can be thought of as a speed limit—a bound on how fast a quantum state can move—and other similar speed limits have been formulated [11]. Alternatively, it can be thought of as bounding how well a quantum system acts as a clock, since the time resolution of the clock is related to the time  $\tau$  for the system to move to an orthogonal state.

In this work, we take the clock perspective on time uncertainty: one's uncertainty about time corresponds to how well one can "read off" the time from measuring a quantum clock. A natural measure for this purpose is to consider the information-theoretic distinguishability of the various time states. As such, we propose using entropy to quantify time uncertainty, and our main result is an entropic energy-time uncertainty relation.

Entropy has been widely employed in uncertainty relations for position-momentum [12] and finite-dimensional

observables [13,14]—see Ref. [15] for a recent detailed review of entropic uncertainty relations. The key benefits of entropy as an uncertainty measure are its clear operational meaning and its relevance to information-processing applications. Indeed, entropic uncertainty relations form the cornerstone of security proofs for quantum key distribution and other quantum cryptographic tasks [15]. They furthermore allow one to recast the uncertainty principle in terms of a guessing game, as we do below for energy and time.

An entropic uncertainty relation for energy and time was previously given in Ref. [16] by constructing an almost-periodic time observable and using a so-called almost-periodic entropy for time. This approach was extended in Ref. [17], where the Holevo information bound was used to derive an entropic energy-time uncertainty relation. However, as indicated in Ref. [16], an almost-periodic time observable serves as a poor quantum clock for aperiodic systems. In Ref. [18], the entanglement between a system and a clock was used to derive an entropic energy-time uncertainty relation for a Hamiltonian with a uniformly spaced spectrum.

In this Letter, we derive entropic energy-time uncertainty relations for general, time-independent Hamiltonians. We first derive a relation for discrete and arbitrarily spaced time, and then we extend this relation to infinitesimally closely spaced (i.e., continuous) time. Our results apply to systems with either finite- or infinite-dimensional Hamiltonians.

A novel aspect of our energy-time uncertainty relation is that it allows the observer to reduce their uncertainty through access to a quantum memory system, as was the case in prior uncertainty relations [19]. The two main benefits of allowing for quantum memory are that (1) it dramatically tightens the relation when the clock is in a mixed state, and (2) it makes the relation more relevant to cryptographic applications in which the eavesdropper may hold the memory system (e.g., see Ref. [19]). Furthermore, by allowing for quantum memory, we can reinterpret our uncertainty relation as a bound on the relative entropy of asymmetry [20], and we discuss below the implications of this reinterpretation.

The fact that our uncertainty relation is stated using operationally relevant entropies implies that it should be useful for information processing applications. For example, if one can distinguish between the time states well, then it is possible to extract randomness by performing an energy measurement. True random bits are critical to the execution of secure protocols and numerical computations. In this case, the randomness of energy measurement outcomes is certified by our bound. Entropic uncertainty relations also find use in proving the security of quantum key distribution (QKD) protocols [21]. If one party is able to prepare states in both the phase and number bases of photons, and if another party is able to perform measurements in these two bases, then both parties can distill a

secret key whose security is guaranteed by our relation. We provide more details regarding applications in the Supplemental Material (Appendix A) [22].

Uncertainty relations can be understood in the framework of a guessing game involving two players, Alice and Bob [15,19], and Fig. 1 shows this game for the energy-time pair. Bob prepares system  $A$  in an arbitrary state  $\rho_{A}$  and sends it to Alice. Alice then flips a coin. If she gets heads, she performs an energy measurement, and Bob then must guess the outcome (possibly with the help of a memory system  $R$  that is initially correlated to  $A$ ). If she gets tails, she applies a time evolution  $e^{-iHt}$  in which  $t$  is randomly chosen from some predefined set, and then sends  $A$  back to Bob, who then tries to guess which time  $t$  Alice applied. All of our uncertainty relations can be understood in terms of this guessing game and can be viewed as constraints on Bob's probability of winning this game (i.e., guessing both the energy and time correctly). There are other variations of this energy-time uncertainty guessing game that are possible, one of which is discussed in the Supplemental Material (Appendix B) [22].

In what follows, we give some necessary preliminaries before stating our main result for the Rényi entropy family in the discrete-time case, and then we extend to the continuous-time case for the von Neumann entropy. Finally, we apply our relation to an illustrative example of a spin-1/2 particle.

Preliminaries.-We begin by considering a finite-dimensional Hamiltonian  $H$  that acts on a quantum system  $A$ , and suppose that it has  $N_{E} \in \mathbb{Z}^{+}$  real energy eigenvalues taken from a set  $\mathcal{E} \subset \mathbb{R}$ . We thus write the Hamiltonian as  $H_{A} = \sum_{\varepsilon \in \mathcal{E}} \varepsilon \Pi_{A}^{\varepsilon}$ , where  $\Pi_{A}^{\varepsilon}$  denotes the projector onto the subspace spanned by energy eigenstates with eigenvalue  $\varepsilon$ . The projectors obey  $\Pi^{\varepsilon} \Pi^{\varepsilon'} = \Pi^{\varepsilon} \delta_{\varepsilon, \varepsilon'}$ , where  $\delta_{\varepsilon, \varepsilon'} = 1$  if  $\varepsilon = \varepsilon'$  and  $\delta_{\varepsilon, \varepsilon'} = 0$  otherwise.

We now recall how to encode the classical state of a clock into a quantum system. Inspired by the Feynman-Kitaev history state formalism [33-35], as well as the

![](images/e536fbd5c2c3354e2b3f191dabbe42278c68034b20d2f814648c3a1b5d5e2033.jpg)  
FIG. 1. Guessing game for energy-time uncertainty. (1) Bob prepares a quantum clock in the state  $\rho_{A}$  and sends it to Alice. (2) Alice flips a coin and (3) either measures the clock's energy or randomly sets the clock's time (i.e., applies a time evolution  $e^{-iHt}$  with  $t$  randomly chosen from a predefined set). Bob's goal is to, depending on Alice's coin flip, guess the clock's energy or guess  $t$  by reading the clock. Our uncertainty relations constrain Bob's ability to win this game.

quantum time proposal of Ref. [36], we introduce a register  $T$  for storing the time, which can be interpreted as a background reference clock. A measurement on the time register is treated in this framework as a time measurement. Let  $\mathcal{T} = \{t_1,\dots,t_K\}$  denote a set of times, for integer  $K\geq 2$ , such that  $t_k\in \mathbb{R}$  for all  $k\in \{1,\ldots ,K\}$ , and  $t_1\leq t_2\leq \ldots \leq t_K$ . We suppose that the register  $T$  has a complete, discrete, and orthonormal basis  $\{|t_k\rangle \}_{k = 1}^K$ . The time values need not be evenly spaced, which means that the basis for register  $T$  can include any combination of  $|\mathcal{T}| = K$  distinct and orthonormal kets.

Now consider a clock system  $A$  that may initially be correlated to a memory system  $R$ , together in a joint state  $\rho_{AR}$  with  $\rho_{A} = \mathrm{Tr}_{R}(\rho_{AR})$ . Let random variable  $E$  capture the outcomes of an energy measurement on the system  $A$ . The outcomes can be stored in a classical register, which we also denote without ambiguity by  $E$  in what follows. To quantify energy uncertainty, we employ the Rényi conditional entropy  $S_{\alpha}(E|R)$  (defined below) of the classical-quantum state

$$
\omega_ {E R} \equiv \sum_ {\varepsilon \in \mathcal {E}} | \varepsilon \rangle \langle \varepsilon | _ {E} \otimes \operatorname {T r} _ {A} \left\{\Pi_ {A} ^ {\varepsilon} \rho_ {A R} \right\}, \tag {1}
$$

where the kets  $\{| \varepsilon \rangle \}_{\varepsilon \in \mathcal{E}}$  are orthonormal, obeying  $\langle \varepsilon'|\varepsilon\rangle = \delta_{\varepsilon', \varepsilon}$ , and thus serve as classical labels for the energies of the Hamiltonian. To quantify the time uncertainty, we employ the Rényi conditional entropy  $S_{\alpha}(T|A)$  of the following classical-quantum state:

$$
\kappa_ {T A} \equiv \frac {1}{| \mathcal {T} |} \sum_ {k = 1} ^ {K} \left| t _ {k} \right\rangle \left\langle t _ {k} \right| _ {T} \otimes e ^ {- i H t _ {k}} \rho_ {A} e ^ {i H t _ {k}}. \tag {2}
$$

In the above and henceforth, we set  $\hbar = 1$ . The state  $\kappa_{TA}$  can be interpreted as the joint state of system  $A$  (the local quantum clock) and the background reference clock  $T$ , at an unknown time  $t_k \in \mathcal{T}$  chosen according to the uniform distribution. Equivalently, this state can be understood as a time-decohered version of the Feynman-Kitaev history state [33-35], the latter of which has the entire history of the state  $\rho_A(t)$  encoded and entangled with a time register in superposition. The classical-quantum states in Eqs. (1) and (2) are in one-to-one correspondence with the following labeled ensembles, respectively:

$$
\left\{p (\varepsilon), | \varepsilon \rangle \langle \varepsilon | _ {E} \otimes \operatorname {T r} _ {A} \left\{\Pi_ {A} ^ {\varepsilon} \rho_ {A R} \right\} / p (\varepsilon) \right\} _ {\varepsilon \in \mathcal {E}},
$$

$$
\left\{1 / | \mathcal {T} |, \left| t _ {k} \right\rangle \left\langle t _ {k} \right| _ {T} \otimes e ^ {- i H t _ {k}} \rho_ {A} e ^ {i H t _ {k}} \right\} _ {t _ {k} \in \mathcal {T}},
$$

where  $p(\varepsilon) = \mathrm{Tr}\{\Pi_A^\varepsilon \rho_{AR}\}$ .

Renyi entropies.-For a probability distribution  $\{p_j\}$ , the Renyi entropies are defined for  $\alpha \in (0,1) \cup (1,\infty)$  by  $S_{\alpha}(\{p_j\}) = [1 / (1 - \alpha)] \log_2 \sum_j p_j^\alpha$ , and for  $\alpha \in \{0,1,\infty\}$  in the limit. This entropy family is generalized to quantum states via the sandwiched Renyi conditional entropy [37], defined for a bipartite state  $\rho_{AB}$  with  $\alpha \in (0,\infty]$  as

$$
S _ {\alpha} (A | B) _ {\rho} = - \inf  _ {\sigma_ {B}} D _ {\alpha} \left(\rho_ {A B} \| I _ {A} \otimes \sigma_ {B}\right), \tag {3}
$$

where the optimization is with respect to all density operators  $\sigma_B$  on system  $B$ . The quantity  $S_{\alpha}(A|B)_{\rho}$  is in turn defined from the sandwiched Rényi relative entropy of a density operator  $\xi$  and a positive semi-definite operator  $\zeta$ , which is defined for  $\alpha \in (0,1) \cup (1,\infty)$  as [37,38]

$$
D _ {\alpha} (\xi \| \zeta) = \frac {1}{\alpha - 1} \log_ {2} \operatorname {T r} [ (\zeta^ {(1 - \alpha) / 2 \alpha} \xi \zeta^ {(1 - \alpha) / 2 \alpha}) ^ {\alpha} ]. \tag {4}
$$

If  $\alpha > 1$  and the support of  $\xi$  is not contained in the support of  $\zeta$ , then it is defined to be equal to  $+\infty$ . The quantity  $D_{\alpha}(\xi \| \zeta)$  is defined for  $\alpha \in \{1, \infty\}$  in the limit.

Entropic energy-time uncertainty relation. Let us now state our uncertainty relation for energy and time. For a pure state  $\rho_{A} = |\psi \rangle \langle \psi |_{A}$  uncorrelated with a reference system  $R$ , it is as follows:

$$
S _ {\alpha} (T | A) _ {\kappa} + S _ {\beta} (\{p (\varepsilon) \}) \geq \log_ {2} | \mathcal {T} |, \tag {5}
$$

holding for all  $\alpha \in [1/2, \infty]$ , with  $\beta$  satisfying  $1 / \alpha + 1 / \beta = 2$ , where  $p(\varepsilon) = \langle \psi | \Pi_A^\varepsilon | \psi \rangle$ . The above inequality [Eq. (5)] is saturated, e.g., when  $|\psi\rangle$  is an energy eigenstate. Such states also maximize the time uncertainty,  $S_\alpha(T|A)_\kappa = \log_2 |\mathcal{T}|$ , since they are stationary states.

The concavity of entropy and concavity of conditional entropy [39] then directly imply that the same inequality in Eq. (5) holds for a mixed state uncorrelated with a reference system  $R$ . However, if  $\rho_{A}$  is a maximally mixed state, the inequality in Eq. (5) yields a trivial bound on the total uncertainty. This is because the inequality does not capture the inherent uncertainty of the initial state.

One of our main results remedies this deficiency, capturing the inherent uncertainty mentioned above and holding nontrivially for mixed states:

$$
S _ {\alpha} (T | A) _ {\kappa} + S _ {\beta} (E | R) _ {\omega} \geq \log_ {2} | T |. \tag {6}
$$

The entropic energy-time uncertainty relation in Eq. (6) holds for all  $\alpha \in [1/2,\infty]$ , where  $\beta$  satisfies  $1 / \alpha + 1 / \beta = 2$ , with the proof given in the Supplemental Material [22] (Appendix C). The quantity  $S_{\alpha}(T|A)_{\kappa}$  represents the uncertainty about the time  $t_k$  from the perspective of someone holding the  $A$  system of the state  $\kappa_{TA}$  in Eq. (2). The quantity  $S_{\beta}(E|R)_{\omega}$ , which is determined by the state  $\rho_{AR}$  and the Hamiltonian  $H_A$ , represents the uncertainty about the outcome of an energy measurement from the perspective of someone who possesses the  $R$  system of the state  $\omega_{\mathrm{ER}}$  in Eq. (1). In the case that  $\rho_{AR}$  is pure, then the quantity  $S_{\beta}(E|R)_{\omega}$  is determined by the reduced state  $\rho_{A}$  and the Hamiltonian  $H_A$ . According to Eq. (6), a good quantum clock state  $\rho_{A}$ , for which  $S_{\alpha}(T|A)_{\kappa} \approx 0$ , necessarily has a large uncertainty in the energy measurement, in the sense that  $S_{\beta}(E|R)_{\omega} \gtrsim \log_2|\mathcal{T}|$ . Conversely, a state with

a small uncertainty in the energy measurement, i.e.,  $S_{\beta}(E|R)_{\omega} \approx 0$ , is necessarily a poor quantum clock state, i.e.,  $S_{\alpha}(T|A)_{\kappa} \approx \log_2|\mathcal{T}|$ .

Note that the uncertainties in Eq. (6) are entropic and hence do not quantify the uncertainties of time and energy in their units, but rather the amount of information (in bits) that we do not know about the respective quantities. For example, if a system can equally likely take on one of two energies  $E_{1}$  and  $E_{2}$ , then the entropic uncertainty in energy constitutes only one bit, and it does not depend on the magnitudes of  $E_{1}$  or  $E_{2}$ . Each entropy in Eq. (6) is analogous to a guessing probability, which quantifies how well one can guess the time  $t$  given the state  $\rho_{A}(t)$ , or the energy given the ability to measure a memory system  $R$ . In fact,  $S_{\alpha}(A|B)$  converges to the negative logarithm of the guessing probability as  $\alpha \to \infty$  [37,40].

Considering the special case of  $|\mathcal{T}| = 2$ , one finds a simple, yet interesting corollary of Eq. (6): under the Hamiltonian  $H_{A}$ , a quantum state  $\rho_{A}$  can evolve to a perfectly distinguishable state, only if  $S_{\beta}(E|R)_{\omega} \geq 1$  for  $\beta \in [1/2,\infty]$ . In other words, for  $S_{\beta}(E|R)_{\omega} < 1$ , the orthogonalization time  $\tau$  in the Mandelstam-Tamm bound is infinite, which cannot be seen using Mandelstam-Tamm or other standard quantum speed limits.

By means of a quantum memory, one can also reduce the time uncertainty instead of only reducing the energy uncertainty. This can be accomplished by considering the memory system  $R$  to be a bipartite system  $R_{1}R_{2}$ . One can then write the uncertainty relation in Eq. (6) as follows:

$$
S _ {\alpha} \left(T \mid A R _ {1}\right) _ {\kappa} + S _ {\beta} \left(E \mid R _ {2}\right) _ {\omega} \geq \log_ {2} | T |, \tag {7}
$$

with full details given in the Supplemental Material [22] (Appendix D). This shows that the tightening of Eq. (5) to give Eq. (6) using quantum memory can reduce the uncertainties in both energy and time. We note that this rewriting is achieved only by relabeling systems, and is thus a consequence of our earlier result in Eq. (6).

An important special case of Eq. (6) is  $\alpha = \beta = 1$  where both entropies are the von Neumann conditional entropy. This results in the following entropic uncertainty relation:

$$
S (T | A) _ {\kappa} + S (E | R) _ {\omega} \geq \log_ {2} | \mathcal {T} |, \tag {8}
$$

where the von Neumann conditional entropy of a bipartite state  $\tau_{CD}$  can be written as  $S(C|D)_{\tau} = -\mathrm{Tr}[\tau_{CD}\log_2\tau_{CD}] + \mathrm{Tr}[\tau_D\log_2\tau_D]$ . In fact, we show in Appendix E of the Supplemental Material [22] that the following equality holds for the von Neumann case when  $\rho_{AR}$  is pure:

$$
S (T | A) _ {\kappa} + S (E | R) _ {\omega} = \log_ {2} | \mathcal {T} | + D \left(\kappa_ {A} \| \sum_ {\varepsilon} \Pi^ {\varepsilon} \rho_ {A} \Pi^ {\varepsilon}\right).
$$

As discussed in the Supplemental Material (Appendix E) [22], when  $\rho_{AR}$  is pure, equality in Eq. (8) is achieved [equivalently,  $D(\kappa_A\| \sum_\varepsilon \Pi^\varepsilon \rho_A\Pi^\varepsilon) = 0]$  if and only if

$$
\frac {1}{| \mathcal {T} |} \sum_ {k = 1} ^ {K} e ^ {- i H t _ {k}} \rho_ {A} e ^ {i H t _ {k}} = \sum_ {\varepsilon} \Pi^ {\varepsilon} \rho_ {A} \Pi^ {\varepsilon}. \tag {9}
$$

One way to satisfy Eq. (9) is if  $[\rho_A, H] = 0$ , and hence the relation is tight for states  $\rho_A$  that are diagonal in the energy eigenbasis. Another way to satisfy Eq. (9) is if  $(1 / |\mathcal{T}|)\sum_{k=1}^{K}e^{i(\varepsilon - \varepsilon')t_k} = \delta_{\varepsilon, \varepsilon'}$  for all combinations of  $\varepsilon, \varepsilon'$ . If the  $|\mathcal{T}|$  times are equally spaced, this implies that  $e^{i(\varepsilon - \varepsilon')t_K} = 1$  and  $(\varepsilon - \varepsilon')t_K = 2\pi$ . This can be understood as an exact inverse relationship between the conjugate variables, which is a signature of a saturated uncertainty relation.

Equation (8) can be generalized to nonuniform probabilities for the various times. As shown in the Supplemental Material (Appendix E) [22], the right-hand side of Eq. (8) gets replaced by the entropy  $S(T)_{\kappa}$  of the time distribution for this generalization.

Relative entropy of asymmetry formulation.-As shown in the Supplemental Material (Appendix F) [22], an alternative way of stating our main result in Eq. (6) is by employing the sandwiched Rényi relative entropy of asymmetry [41], which generalizes an asymmetry measure put forward in Ref. [20]:

$$
S _ {\alpha} (T | A) _ {\kappa} + \inf  _ {\sigma : [ H, \sigma ] = 0} D _ {\alpha} (\rho \| \sigma) \geq \log_ {2} | \mathcal {T} |, \tag {10}
$$

and holds for all  $\alpha \in (0,\infty ]$ . The inequality in Eq. (10) delineates a trade-off, given the Hamiltonian  $H$ , between how well a state  $\rho_{A}$  can serve as a quantum clock and the asymmetry of  $\rho_{A}$  with respect to time translations. Moreover, this connection is exact for pure states.

In the limit  $\alpha \to 1$ , the quantity  $\inf_{\sigma : [H, \sigma] = 0} D_{\alpha}(\rho \| \sigma)$  reduces to the relative entropy of asymmetry [20]

$$
\begin{array}{l} \lim  _ {\alpha \rightarrow 1} \inf  _ {\sigma : [ H, \sigma ] = 0} D _ {\alpha} (\rho \| \sigma) = \inf  _ {\sigma : [ H, \sigma ] = 0} D (\rho \| \sigma) \\ \equiv \Gamma_ {H} (\rho) = S (\Delta (\rho)) - S (\rho), \qquad (1 1) \\ \end{array}
$$

where the quantum relative entropy is defined as  $D(\rho \| \sigma) \equiv \mathrm{Tr}[\rho [\log_2\rho -\log_2\sigma ]]$  [42] and  $\Delta (\rho) = \sum_{\varepsilon \in \mathcal{E}}\Pi^{\varepsilon}\rho \Pi^{\varepsilon}$  (in the context of asymmetry, the function  $S(\Delta (\rho)) - S(\rho)$  was first studied in Ref. [43]). Then the entropic uncertainty relation in Eq. (10) reduces to  $S(T|A)_K + \Gamma_H(\rho)\geq \log_2|T|$ .

Extension to continuous time. We now extend the uncertainty relation in Eq. (6) so that it is applicable to continuous, as opposed to discrete, time, and to Hamiltonians with countable spectrum. From Eq. (6) and Ref. [44], we derive an inequality applicable to the von Neumann entropies. Full details are available in the Supplemental Material (Appendix G) [22]. Consider time to be continuous in the interval  $[0, T_F]$ . Given a state  $\rho_A$  and a Hamiltonian  $H_A = \sum_{\varepsilon \in \mathcal{E}} \varepsilon \Pi_A^\varepsilon$ , with  $\mathcal{E}$  countably infinite, we then have that

![](images/81581669272ad4e0c4f76eeda41d4a4e1bea541087ff01b9d30b99b667f983d1.jpg)  
FIG. 2. Our uncertainty relations applied to a spin-1/2 particle in a magnetic field. For Hamiltonian  $H = \kappa \sigma_z$  and  $|\mathcal{T}| = 2$  (in the discrete-time case) or  $T_{F} = 2$  (in the continuous-time case), the plot shows the variation in the uncertainties with  $\theta$ , the angle the state makes with the  $z$  axis of the Bloch sphere. The quantity  $\inf_{\sigma : [H, \sigma] = 0} D(\rho_A \| \sigma)$  is the energy uncertainty, while  $S(T|A)$  and  $s(T|A)$  are respectively the time uncertainties for discrete and continuous time. The black dotted line shows  $\log_2 |\mathcal{T}| = \log_2 T_F$ , i.e., our lower bounds on the total uncertainty from Eqs. (6) and (12).

$$
\inf  _ {\sigma : [ H, \sigma ] = 0} D \left(\rho_ {A} \| \sigma\right) + s (T | A) \geq \log_ {2} T _ {F}. \tag {12}
$$

For a continuously parametrized ensemble of states  $\{p(x), \rho_B^x\}_{x \in \mathcal{X}}$ , the differential conditional quantum entropy  $s(X|B)$  is defined as  $s(X|B) = -\int_{\mathcal{X}} dx D(p(x) \rho_B^x \| \rho_{\mathrm{avg}})$ , where  $\rho_{\mathrm{avg}} = \int_{\mathcal{X}} dxp(x) \rho_B^x$  [44]. For our case, this means

$$
\begin{array}{l} s (T | A) = - \int_ {0} ^ {T _ {F}} d t D (\rho (t) / T _ {F} \| \bar {\rho}), \\ \bar {\rho} = \frac {1}{T _ {F}} \int_ {0} ^ {T _ {F}} d t e ^ {- i H t} \rho_ {A} e ^ {i H t}. \\ \end{array}
$$

Example: Spin in a magnetic field. Consider a spin-1/2 particle in a magnetic field  $\mathbf{B} = B\hat{\mathbf{z}}$ . This is described by the Hamiltonian  $\hat{H} = \kappa \sigma_z$ , where  $\kappa$  is a constant proportional to  $B$ , and  $\sigma_z$  is the  $z$ -Pauli operator. Consider a pure state  $\rho_A = |\psi(0)\rangle \langle \psi(0)|$  that makes an angle  $\theta$  with the  $z$  axis of the Bloch sphere, given by  $|\psi(0)\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle$ . After a time  $t$ , this state evolves to  $|\psi(t)\rangle = e^{-iHt}|\psi(0)\rangle$ . Figure 2 plots the variation of the uncertainty (time, energy, and total uncertainty) with  $\theta$  for both our discrete- and continuous-time relations. For  $\theta = \pi/2$ , the energy uncertainty is maximal (one bit) while the time uncertainty is minimal (although still nonzero in this example). At the other extreme, for  $\theta = 0$  or  $\pi$ , the energy uncertainty is zero while the time uncertainty is maximal (one bit), meaning that the clock's time states cannot be distinguished. One can see in Fig. 2 that our uncertainty relation is tight in this extreme case.

Discussion.-We gave a conceptually clear and operational formulation of the energy-time uncertainty principle.

We stated an entropic energy-time uncertainty relation for the Rényi entropies for discrete time sets. This relation was strengthened for mixed states by allowing the observer to possess a quantum memory, a feature that also allowed us to reinterpret our relation as a bound on the relative entropy of asymmetry. For the von Neumann entropy, we extended our uncertainty relation to continuous time sets. Our relation is saturated for all states  $\rho_{A}$  diagonal in the energy eigenbasis.

Expressed in terms of entropies, which are operationally important in information theory, our result should have uses in various tasks. Entropic uncertainty relations have been used previously to certify randomness and prove security of quantum cryptography protocols, and we believe our result will be an important tool used to develop such protocols further.

P. J. C. acknowledges support from the Los Alamos National Laboratory ASC Beyond Moore's Law project. V. K. acknowledges support from the Department of Physics and Astronomy at Louisiana State University. S. L. was supported by IARPA under the QEO program, NSF, and ARO under the Blue Sky Initiative. M. M. W. acknowledges support from the US National Science Foundation through Grant No. 1714215. M. M. W. is grateful to S. L. for hosting him for a research visit to University of Oxford, during which some of this research was conducted.

[1] W. Heisenberg, Über den anschaulichen inhalt der quantentheoretischen kinematik und mechanik, Z. Phys. 43, 172 (1927).  
[2] E. H. Kennard, Zur quantenmechanik einfacher bewegungstypen, Z. Phys. 44, 326 (1927).  
[3] H. P. Robertson, The uncertainty principle, Phys. Rev. 34, 163 (1929).  
[4] P. Busch, P. Lahti, and R. F. Werner, Heisenberg uncertainty for qubit measurements, Phys. Rev. A 89, 012129 (2014).  
[5] L. Maccone and A. K. Pati, Stronger Uncertainty Relations for all Incompatible Observables, Phys. Rev. Lett. 113, 260401 (2014).  
[6] W. Pauli and N. Straumann, Die allgemeinen Prinzipien der Wellenmechanik (Springer, Berlin, Heidelberg, 1990).  
[7] J. Butterfield, On time in quantum physics, in A Companion to the Philosophy of Time, edited by H. Dyke and A. Bardon (John Wiley & Sons, Ltd., Hoboken, 2013), pp. 220-241.  
[8] V.V. Dodonov and A.V. Dodonov, Energy-time and frequency-time uncertainty relations: Exact inequalities, Phys. Scr. 90, 074049 (2015).  
[9] V. Giovannetti, S. Lloyd, and L. Maccone, Quantum-enhanced measurements: Beating the standard quantum limit, Science 306, 1330 (2004).  
[10] L. Mandelstam and Ig. Tamm, The Uncertainty Relation between Energy and Time in Non-Relativistic Quantum Mechanics, In Selected Papers (Springer, Berlin, Heidelberg, 1991), pp. 115–123.

[11] N. Margolus and L. B. Levitin, The maximum speed of dynamical evolution, Physica (Amsterdam) 120D, 188 (1998).  
[12] I. I. Hirschman, A note on entropy, Am. J. Math. 79, 152 (1957).  
[13] D. Deutsch, Uncertainty in Quantum Measurements, Phys. Rev. Lett. 50, 631 (1983).  
[14] H. Maassen and J.B.M. Uffink, Generalized Entropic Uncertainty Relations, Phys. Rev. Lett. 60, 1103 (1988).  
[15] P.J. Coles, M. Berta, M. Tomamichel, and S. Wehner, Entropic uncertainty relations and their applications, Rev. Mod. Phys. 89, 015002 (2017).  
[16] M. J. W. Hall, Almost-periodic time observables for bound quantum systems, J. Phys. A 41, 255301 (2008).  
[17] M. J. W. Hall, Entropic Heisenberg limits and uncertainty relations from the Holev information bound, J. Phys. A 51, 364001 (2018).  
[18] A. Boette, R. Rossignoli, N. Gigena, and M. Cerezo, System-time entanglement in a discrete-time model, Phys. Rev. A 93, 062127 (2016).  
[19] M. Berta, M. Christandl, R. Colbeck, J.M. Renes, and R. Renner, The uncertainty principle in the presence of quantum memory, Nat. Phys. 6, 659 (2010).  
[20] G. Gour, I. Marvian, and R. W. Spekkens, Measuring the quality of a quantum reference frame: The relative entropy of frameness, Phys. Rev. A 80, 012307 (2009).  
[21] C. H. Bennett and G. Brassard, Quantum cryptography: Public key distribution and coin tossing, in Proceedings of IEEE International Conference on Computers Systems and Signal Processing (IEEE, Bangalore, India, 1984), pp. 175-179.  
[22] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.122.100401 for these applications and mathematical details of some derivations, as well as Refs. [23-32].  
[23] R. Impagliazzo, L. A. Levin, and M. Luby, Pseudo-random generation from one-way functions, in Proceedings of the twenty-first annual ACM symposium on Theory of computing—STOC '89, Seattle, Washington, USA (ACM Press, New York, 1989), pp. 12-24.  
[24] C. H. Bennett, G. Brassard, C. Crepeau, and U. M. Maurer, Generalized privacy amplification, IEEE Trans. Inf. Theory, 41, 1915.  
[25] G. Vallone, D. G. Marangon, M. Tomasin, and P. Villoresi, Quantum randomness certified by the uncertainty principle, Phys. Rev. A 90, 052327 (2014).  
[26] D.G. Marangon, G. Vallone, and P. Villoresi, Source-Device-Independent Ultrafast Quantum Random Number Generation, Phys. Rev. Lett. 118, 060503 (2017).  
[27] Z. Zhang, J. Mower, D. Englund, F.N.C. Wong, and J.H. Shapiro, Unconditional Security of Time-Energy Entanglement Quantum Key Distribution Using Dual-Basis Interferometry, Phys. Rev. Lett. 112, 120506 (2014).

[28] M. Yuezhen Niu, F. Xu, F. Furrer, and J. H. Shapiro, Finite-key analysis for time-energy high-dimensional quantum key distribution, arXiv:1606.08394.  
[29] B. Qi, Single-photon continuous-variable quantum key distribution based on the energy-time uncertainty relation, Opt. Lett. 31, 2795 (2006).  
[30] P. J. Coles, Unification of different views of decoherence and discord, Phys. Rev. A 85, 042103 (2012).  
[31] S. Beigi, Sandwiched Rényi divergence satisfies data processing inequality, J. Math. Phys. 54, 122202 (2013).  
[32] M. Junge, R. Renner, D. Sutter, M.M. Wilde, and A. Winter, Universal recovery maps and approximate sufficiency of quantum relative entropy, Ann. Henri Poincaré 19, 2955 (2018).  
[33] R. P. Feynman, Quantum mechanical computers, Opt. News 11, 11 (1985).  
[34] R. Feynman, Quantum mechanical computers, Found. Phys. 16, 507 (1986).  
[35] A. Yu. Kitaev, A. H. Shen, and M. N. Valyi, Classical and Quantum Computation (American Mathematical Society, Boston, MA, USA, 2002).  
[36] V. Giovannetti, S. Lloyd, and L. Maccone, Quantum time, Phys. Rev. D 92, 045033 (2015).  
[37] M. Müller-Lennert, F. Dupuis, O. Szehr, S. Fehr, and M. Tomamichel, On quantum Rényi entropies: A new generalization and some properties, J. Math. Phys. 54, 122203 (2013).  
[38] M. M. Wilde, A. Winter, and D. Yang, Strong converse for the classical capacity of entanglement-breaking and Hadamard channels via a sandwiched Rényi relative entropy, Commun. Math. Phys. 331, 593 (2014).  
[39] E. H. Lieb and M. Beth Ruskai, A Fundamental Property of Quantum-Mechanical Entropy, Phys. Rev. Lett. 30, 434 (1973).  
[40] R. König, R. Renner, and C. Schaffner, The operational meaning of min- and max-entropy, IEEE Trans. Inf. Theory 55, 4337 (2009).  
[41] L. Gao, M. Junge, and N. LaRacuente, Strong subadditivity inequality and entropic uncertainty relations, arXiv:1710.10038.  
[42] H. Umegaki, Conditional expectations in an operator algebra IV (entropy and information), Kodai Math. Sem. Rep. 14, 59 (1962).  
[43] J. Vaccaro, F. Anselmi, H. Wiseman, and K. Jacobs, Tradeoff between extractable mechanical work, accessible entanglement, and ability to act as a reference system, under arbitrary superselection rules, Phys. Rev. A 77, 032114 (2008).  
[44] F. Furrer, M. Berta, M. Tomamichel, V. B. Scholz, and M. Christandl, Position-momentum uncertainty relations in the presence of quantum memory, J. Math. Phys. 55, 122205 (2014).