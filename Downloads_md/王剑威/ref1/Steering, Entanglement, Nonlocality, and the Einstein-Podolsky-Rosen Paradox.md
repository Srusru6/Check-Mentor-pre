# Steering, Entanglement, Nonlocality, and the Einstein-Podolsky-Rosen Paradox

H. M. Wiseman, $^{1}$  S. J. Jones, $^{1}$  and A. C. Doherty $^{2}$

<sup>1</sup>Centre for Quantum Computer Technology, Centre for Quantum Dynamics, Griffith University, Brisbane 4111 Australia

$^{2}$ School of Physical Sciences, University of Queensland, Brisbane 4072 Australia

(Received 22 December 2006; published 6 April 2007)

The concept of steering was introduced by Schrödinger in 1935 as a generalization of the Einstein-Podolsky-Rosen paradox for arbitrary pure bipartite entangled states and arbitrary measurements by one party. Until now, it has never been rigorously defined, so it has not been known (for example) what mixed states are steerable (that is, can be used to exhibit steering). We provide an operational definition, from which we prove (by considering Werner states and isotropic states) that steerable states are a strict subset of the entangled states, and a strict superset of the states that can exhibit Bell nonlocality. For arbitrary bipartite Gaussian states we derive a linear matrix inequality that decides the question of steerability via Gaussian measurements, and we relate this to the original Einstein-Podolsky-Rosen paradox.

DOI: 10.1103/PhysRevLett.98.140402

PACS numbers: 03.65.Ud, 03.65.Ta, 03.67.Mn

The nonlocality of entangled states, a key feature of quantum mechanics (QM), was first pointed out in 1935 by Einstein, Podolsky, and Rosen (EPR) [1]. They considered a general nonfactorizable pure state of two systems, held by two parties (say Bob and Alice):

$$
| \Psi \rangle = \sum_ {n = 1} ^ {\infty} c _ {n} | \psi_ {n} \rangle | u _ {n} \rangle = \sum_ {n = 1} ^ {\infty} d _ {n} | \varphi_ {n} \rangle | v _ {n} \rangle , \tag {1}
$$

where  $\{|u_n\rangle\}$  and  $\{|v_n\rangle\}$  are two orthonormal bases for Alice's system. If Alice chose to measure in the  $\{|u_n\rangle\}$  ( $\{|v_n\rangle\}$ ) basis, then she could instantaneously project Bob's system into one of the states  $|\psi_n\rangle$  ( $|\varphi_n\rangle$ ). For EPR, the fact that the ensemble of  $|\psi_n\rangle$ s is different from the ensemble of  $|\varphi_n\rangle$ s was problematic because "the two systems no longer interact, [so] no real change can take place in [Bob's] system in consequence of anything that may be done to [Alice's] system." Thus, they thought (wrongly) that this nonlocality must be an artefact of the incompleteness of QM. This intuition was supported by their famous example (the EPR "paradox") involving position and momentum, which could be trivially resolved by considering local hidden variables (LHVs) for  $q$  and  $p$ .

The EPR paper provoked an interesting response from Schrödinger [2], who introduced the terms entangled state for states of the form of Eq. (1) and steering for Alice's ability to affect Bob's state through her choice of measurement basis. Schrödinger had invented the quantum state  $\psi$  for atoms [3], and, unlike EPR, believed it gave a complete and correct description for a localized, isolated system. Thus, he rejected their suggested explanation of steering in terms of LHVs. However, like EPR, he could not easily accept nonlocality, and so suggested that QM was incorrect in its description of delocalized entangled systems [2]. That is, he thought (wrongly) that Bob's system has a definite state, even if it is unknown to him, so that steering would never be seen experimentally. We call this a local hidden state (LHS) model for Bob.

In this Letter we revisit Schrödinger's concept of steering (which has received increasing attention in recent years [4-8]) from a quantum information perspective. That is, we define it according to a task.

First, let us define the more familiar concept of Bell nonlocality [9] as a task, in this case with three parties. Alice and Bob can prepare a shared bipartite state, and repeat this any number of times. Each time, they measure their respective parts. Except for the preparation step, communication between them is forbidden. Their task is to convince Charlie (with whom they can communicate) that the state they can prepare is entangled. Charlie accepts QM as correct, but trusts neither Alice nor Bob. If the correlations can be explained by a LHV model then Charlie will not be convinced that the state is entangled; the results could have been fabricated from shared classical randomness. Conversely, if the correlations between the results they report cannot be so explained, then the state must be entangled. Therefore, they will succeed in their task iff (if and only if) they can demonstrate Bell nonlocality.

The analogous definition for steering uses a task with two parties. Alice can prepare a bipartite quantum state and send one part to Bob and repeat this any number of times. Each time, they measure their respective parts and communicate classically. Alice's task is to convince Bob that the state she can prepare is entangled. Bob (like Schrödinger) accepts that QM describes the results of the measurements he makes. However, Bob does not trust Alice. If the correlations between Bob's measurement results and the results Alice reports can be explained by a LHS model for Bob then Bob will not be convinced that the state is entangled; Alice could have drawn a pure state at random from some ensemble and sent it to Bob, and then chosen her result based on her knowledge of this LHS. Conversely, if the correlations cannot be so explained then the state must be entangled. Therefore, Alice will succeed in her task iff she can create genuinely different ensembles for Bob by steering Bob's state.

As EPR and Schrödinger noted, steering may be demonstrated using any pure entangled state, and the same is true of Bell nonlocality [10]. But in the laboratory, states are mixed. In a seminal paper, Werner [11] asked the question: can all entangled states be used to demonstrate Bell nonlocality? As Werner showed [11], the surprising answer is: no—a hint of the complexity of bound entanglement [12] still being uncovered.

In this Letter, we address the following questions: can all entangled states be used to demonstrate steering? Does a demonstration of steering also demonstrate Bell nonlocality? We prove that in both cases the answer is again: no. Thus, steerability is a distinct nonlocal property of some bipartite quantum states, different from both Bell nonlocality and nonseparability.

This Letter is structured as follows. We begin by finding the mathematical formulation of the above operational definition of steering. From this it follows that steerability is stronger than nonseparability and weaker than Bell nonlocality. We then show, using two-qubit Werner states and isotropic states, that this is a strict hierarchy. Lastly, we consider Gaussian states with Gaussian measurements. We determine the condition under which steering can be demonstrated, and relate this to the Reid criterion for the EPR paradox [13].

Concepts of quantum nonlocality. Let the set of all observables on the Hilbert space for Alice's system be denoted  $\mathfrak{D}_{\alpha}$ . We denote an element of  $\mathfrak{D}_{\alpha}$  by  $A$ , and the set of eigenvalues  $\{a\}$  of  $A$  by  $\lambda(A)$ . By  $P(a|A;W)$  we mean the probability that Alice will obtain the result  $a$  when she measures  $A$  on a system with state matrix  $W$ . We denote the measurements that Alice is able to perform by the set  $\mathfrak{M}_{\alpha} \subseteq \mathfrak{D}_{\alpha}$ . (Note that, following Werner [11], we are restricting to projective measurements.) The corresponding notations for Bob, and for Alice and Bob jointly, are obvious. Thus, for example,

$$
P (a, b | A, B; W) = \operatorname {T r} \left[ \left(\Pi_ {a} ^ {A} \otimes \Pi_ {b} ^ {B}\right) W \right], \tag {2}
$$

where  $\Pi_{a}^{A}$  is the projector satisfying  $A\Pi_{a}^{A} = a\Pi_{a}^{A}$ .

The strongest sort of nonlocality in QM is Bell nonlocality [9]. This is exhibited in an experiment on state  $W$  iff the correlations between  $a$  and  $b$  cannot be explained by a LHV model. That is, if it is not the case that for all  $a \in \lambda(A)$ ,  $b \in \lambda(B)$ , for all  $A \in \mathfrak{M}_{\alpha}$ ,  $B \in \mathfrak{M}_{\beta}$ , we have

$$
P (a, b | A, B; W) = \sum_ {\xi} \wp (a | A, \xi) \wp (b | B, \xi) \wp_ {\xi}. \tag {3}
$$

Here, and below,  $\wp(a|A, \xi), \wp(b|B, \xi)$ , and  $\wp_{\xi}$  denote some (positive, normalized) probability distributions, involving the LHV  $\xi$ . We say that a state is Bell nonlocal iff there exists a measurement set  $\mathfrak{M}_{\alpha} \times \mathfrak{M}_{\beta}$  that allows Bell nonlocality to be demonstrated.

A strictly weaker [11] concept is that of nonseparability or entanglement. A nonseparable state is one that cannot be written as  $W = \sum_{\xi} \sigma_{\xi} \otimes \rho_{\xi} \wp_{\xi}$ . Here, and below,  $\sigma_{\xi} \in \mathfrak{D}_{\alpha}$  and  $\rho_{\xi} \in \mathfrak{D}_{\beta}$  are some (positive, normalized) quantum

states. We can also give an operational definition by allowing Alice and Bob the ability to measure a quorum of local observables so that they can reconstruct the state  $W$  by tomography [14]. Thus a state  $W$  is nonseparable iff it is not the case that for all  $a \in \lambda(A)$ ,  $b \in \lambda(B)$ , for all  $A \in \mathfrak{D}_{\alpha}$ ,  $B \in \mathfrak{D}_{\beta}$ , we have

$$
P (a, b | A, B; W) = \sum_ {\xi} P (a | A; \sigma_ {\xi}) P (b | B; \rho_ {\xi}) \wp_ {\xi}. \tag {4}
$$

Bell nonlocality and nonseparability are both concepts that are symmetric between Alice and Bob. However, steering, Schrödinger's term for the EPR effect, is inherently asymmetric. It is about whether Alice, by her choice of measurement  $A$ , can collapse Bob's system into different types of states in the different ensembles  $E^A \equiv \{\tilde{\rho}_a^A : a \in \lambda(A)\}$ . Here  $\tilde{\rho}_a^A \equiv \mathrm{Tr}_{\alpha}[W(\Pi_a^A \otimes \mathbf{I})] \in \mathfrak{D}_{\beta}$ , where the tilde denotes that this state is unnormalized (its norm is the probability of its realization). Of course, Alice cannot affect Bob's unconditioned state  $\rho = \mathrm{Tr}_{\alpha}[W] = \sum_{a} \tilde{\rho}_a^A$  that would allow superluminal signaling. Nevertheless, as Schrödinger said in 1935 [2], "It is rather discomforting that the theory should allow a system to be steered ... into one or the other type of state at the experimenter's mercy in spite of [her] having no access to it." As stated earlier, he was "not satisfied about there being enough experimental evidence for [it].

The "experimental evidence" required by Schrödinger is precisely that required for Alice to succeed in the "steering task" defined in the introduction. The experiment can be repeated at will, and we assume Bob's measurements enable him to do state tomography. Prior to all experiments, Bob demands that Alice announce the possible ensembles  $\{E^A:A\in \mathfrak{M}_\alpha \}$  into which she can steer Bob's state. In any given run (after he has received his state), Bob should randomly pick an ensemble  $E^{A}$ , and ask Alice to prepare it. Alice should then do so, by measuring  $A$  on her system, and announce to Bob the particular member  $\rho_{a}^{A}$  she has prepared. Over many runs, Bob can verify that each state announced is indeed produced, and with the correct frequency  $\mathrm{Tr}[\tilde{\rho}_a^A ]$ .

If Bob's system did have a preexisting LHS  $\rho_{\xi}$ , then Alice could attempt to fool Bob, using her knowledge of  $\xi$ . This state would be drawn at random from some prior ensemble of LHSs  $F = \{\wp_{\xi} \rho_{\xi}\}$  with  $\rho = \sum_{\xi} \wp_{\xi} \rho_{\xi}$ . Alice would then have to announce a LHS  $\tilde{\rho}_{a}^{A}$  according to some stochastic map from  $\xi$  to  $a$ . If, for all  $A \in \mathfrak{M}_{\alpha}$ , and for all  $a \in \lambda(A)$ , there exists a  $\wp(a|A, \xi)$  such that

$$
\tilde {\rho} _ {a} ^ {A} = \sum_ {\xi} \wp (a | A, \xi) \rho_ {\xi} \wp_ {\xi}, \tag {5}
$$

then Alice would have failed to convince Bob that she can steer his system. Conversely, if Bob cannot find any ensemble  $F$  and map  $\wp(a|A, \xi)$  satisfying Eq. (5) then Bob must admit that Alice can steer his system.

We can recast this definition as a "hybrid" of Eqs. (3) and (4): Alice's measurement strategy  $\mathfrak{M}_{\alpha}$  on state  $W$  exhibits steering iff it is not the case that for all  $a \in \lambda(A)$ ,

$b\in \lambda (B)$  , for all  $A\in \mathfrak{M}_{\alpha}$ $B\in \mathfrak{D}_{\beta}$  , we have

$$
P (a, b | A, B; W) = \sum_ {\xi} \wp (a | A, \xi) P (b | B; \rho_ {\xi}) \wp_ {\xi}. \tag {6}
$$

If there exists a measurement strategy  $\mathfrak{M}_{\alpha}$  that exhibits steering, we say that the state  $W$  is steerable (by Alice).

Clearly steerability is stronger than nonseparability, but Bell nonlocality is stronger than steerability. At least one of these relations must be "strictly stronger", because of Werner's result [11]. In the following sections we prove that both are "strictly stronger"; see Fig. 1.

Conditions for steerability. Below we derive necessary and sufficient conditions for steerability for three families of states. Crucial to the derivations is the concept of an optimal ensemble  $F^{\star} = \{\rho_{\xi}^{\star}\wp_{\xi}^{\star}\}$ . This is an ensemble such that if it cannot satisfy Eq. (5) then no ensemble can satisfy it. In finding an optimal ensemble  $F^{\star}$  we use the symmetries of  $W$  and  $\mathfrak{M}_{\alpha}$ :

Lemma 1. Consider a group  $G$  with a unitary representation  $U_{\alpha \beta}(g) = U_{\alpha}(g)\otimes U_{\beta}(g)$  on the Hilbert space for Alice and Bob. Say that  $\forall A\in \mathfrak{M}_\alpha ,\forall a\in \lambda (A),\forall g\in G$  we have  $U_{\alpha}^{\dagger}(g)AU_{\alpha}(g)\in \mathfrak{M}_{\alpha}$  and

$$
\tilde {\rho} _ {a} ^ {U _ {\alpha} ^ {\dagger} (g) A U _ {\alpha} (g)} = U _ {\beta} (g) \tilde {\rho} _ {a} ^ {A} U _ {\beta} ^ {\dagger} (g). \tag {7}
$$

Then there exists an optimal ensemble that is  $G$  covariant:  $\forall g\in G,\{\rho_{\xi}^{\star}\wp_{\xi}^{\star}\} = \{U_{\beta}(g)\rho_{\xi}^{\star}U_{\beta}^{\dagger}(g)\wp_{\xi}^{\star}\} .$

Proof.-Say there exists an ensemble  $F = \{\rho_{\xi}\wp_{\xi}\}$  satisfying Eq. (5). Then under the conditions of lemma 1, the  $G$  -covariant ensemble  $F^{\star} = \{\rho_{(g,\xi)}^{\star}\wp_{\xi}d\mu_{G}(g)\}$  with  $\rho_{(g,\xi)}^{\star} = U_{\beta}(g)\rho_{\xi}U_{\beta}^{\dagger}(g)$  satisfies Eq. (5) with the choice  $\wp^{\star}(a|A,(g,\xi)) = \wp (a|U_{\alpha}^{\dagger}(g)AU_{\alpha}(g),\xi).$

(i) Werner states.—This family of states in  $\mathbb{C}_d\otimes \mathbb{C}_d$  was introduced in Ref. [11]. We parametrize it by  $\eta \in \mathbb{R}$  such that  $W_{d}^{\eta}$  is linear in  $\eta$ ,  $W_{d}^{\eta}$  is a product state for  $\eta = 0$ , and the largest permissible value for  $\eta$  is 1:

$$
W _ {d} ^ {\eta} = \left(\frac {d - 1 + \eta}{d - 1}\right) \frac {\mathbf {I}}{d ^ {2}} - \left(\frac {\eta}{d - 1}\right) \frac {\mathbf {V}}{d}. \tag {8}
$$

![](images/aff1a72ddbe580c9993679488c23a0c777ac0860324f3b1545eef6d9422432de.jpg)  
FIG. 1 (color online). Boundaries between classes of entangled states for Werner (a) and isotropic (b) states  $W_{d}^{\eta}$ . The bottom (blue) line is  $\eta_{\mathrm{ent}}$  (states are entangled iff  $\eta > \eta_{\mathrm{ent}}$ ). The next (red) line is  $\eta_{\mathrm{steer}}$ , defined analogously for steering. The top (green) line with down arrows is an upper bound on  $\eta_{\mathrm{Bell}}$ , defined analogously for Bell nonlocality. The up arrows are lower bounds on  $\eta_{\mathrm{Bell}}$  for  $d = 2$ . The three classes are thus distinct. Dots join values at finite  $d$  with those at  $d = \infty$ .

![](images/e577084a0409d8495449f0aa040fed69dcf12d57245a43f1ef6d0e99ff2ad9d2.jpg)

Here  $\mathbf{I}$  is the identity and  $\mathbf{V}$  the "flip" operator ( $\mathbf{V} \varphi \otimes \psi \equiv \psi \otimes \varphi$ ). Werner states are nonseparable iff  $\eta > \eta_{\mathrm{ent}} = 1 / (d + 1)$  [11]. For  $d = 2$ , the Werner states violate a Bell inequality if  $\eta > 1 / \sqrt{2}$  [15]. This places an upper bound on  $\eta_{\mathrm{Bell}}$ , defined by  $W_d^\eta$  being Bell nonlocal iff  $\eta > \eta_{\mathrm{Bell}}$ . For  $d > 2$  only the trivial upper bound of 1 is known. However, Werner found a lower bound on  $\eta_{\mathrm{Bell}}$  of  $1 - 1 / d$  [11], which is strictly greater than  $\eta_{\mathrm{ent}}$ .

We now show that Werner's lower bound is in fact equal to  $\eta_{\mathrm{steer}}$ , defined by  $W_d^\eta$  being steerable iff  $\eta > \eta_{\mathrm{steer}}$ . We allow Alice all possible measurement strategies:  $\mathfrak{M}_{\alpha} = \mathfrak{D}_{\alpha}$ , and without loss of generality take the projectors to be rank one:  $\Pi_a^A = |a\rangle \langle a|$ . For Werner states, the conditions of lemma 1 are then satisfied for the  $d$ -dimensional unitary group  $\mathfrak{U}(d)$ . Specifically,  $g \to U$ , and  $U_{\alpha \beta}(g) \to U \otimes U$  [11]. Again, without loss of generality we can take the optimal ensemble to consist of pure states, in which case there is a unique covariant optimal ensemble,  $F^{\star} = \{| \psi \rangle \langle \psi | d \mu_H(\psi) \}$ , where  $d \mu_H(\psi)$  is the Haar measure over  $\mathfrak{U}(d)$ . Werner used the same construction; his LHVs for Bob were in fact these LHSs.

Now we determine when Eq. (5) can be satisfied by this  $F^{\star}$ . Using  $\tilde{\rho}_a^A = \langle a|W_d^\eta |a\rangle$  it is simple to show that, for any  $A\in \mathfrak{D}_{\alpha}$  and  $a\in \lambda (A)$ ,

$$
\langle a | \tilde {\rho} _ {a} ^ {A} | a \rangle = (1 - \eta) / d ^ {2}. \tag {9}
$$

Using the methods of Werner's proof we show that for any positive normalized distribution  $\wp(a|A, \psi)$ ,

$$
\langle a | \int d \mu_ {H} (\psi) | \psi \rangle \langle \psi | \wp (a | A, \psi) | a \rangle \geq 1 / d ^ {3}. \tag {10}
$$

The upper bound is attained for the choice [11]

$$
\wp (a | A, \psi) = \left\{ \begin{array}{l l} 1 & \text {i f} | \langle \psi | a \rangle | \leq | \langle \psi | a ^ {\prime} \rangle |, \forall a ^ {\prime} \neq a \\ 0 & \text {o t h e r w i s e .} \end{array} \right. \tag {11}
$$

Comparing this with Eq. (9) we see that steering can be demonstrated if  $\left(1 - \eta\right) / d^{2} < 1 / d^{3}$ . Moreover, it is easy to verify that when this inequality is saturated, Eq. (11) satisfies Eq. (5). Thus  $\eta_{\mathrm{steer}} = 1 - 1 / d$ .

Recently a new lower bound for  $\eta_{\mathrm{Bell}}$  was found for  $d = 2$  [16], greater than  $\eta_{\mathrm{steer}}$ , as shown in Fig. 1. This proves that steerability is strictly weaker than Bell nonlocality as well as being strictly stronger than nonseparability.

(ii) Isotropic states.—This family, introduced in [17], can be parametrized identically to the Werner states:

$$
W _ {d} ^ {\eta} = (1 - \eta) \mathbf {I} / d ^ {2} + \eta \mathbf {P} _ {+}, \tag {12}
$$

where  $\mathbf{P}_{+} = |\psi_{+}\rangle \langle \psi_{+}|,$  where  $|\psi_{+}\rangle = \sum_{i = 1}^{d}|i\rangle |i\rangle /\sqrt{d}$ . For  $d = 2$  the Isotropic states are identical to Werner states. Isotropic states are nonseparable iff  $\eta >\eta_{\mathrm{ent}} = 1 / (d + 1)$  [17]. A nontrivial upper bound on  $\eta_{\mathrm{Bell}}$  for all  $d$  is known [18]; Ref. [16] gives a lower bound for  $d = 2$ .

To determine  $\eta_{\mathrm{steer}}$  for isotropic states, we follow the same method as for Werner states, except that this time  $U_{\alpha \beta} = U^{*}\otimes U$  [17]. Instead of Eq. (9) we obtain

$$
\langle a | \tilde {\rho} _ {a} ^ {A} | a \rangle = \eta / d + (1 - \eta) / d ^ {2}, \tag {13}
$$

and instead of Eq. (10), we show that

$$
\int d \mu_ {H} (\psi) | \langle a | \psi \rangle | ^ {2} \wp (a | A, \psi) \leq H _ {d} / d ^ {2}, \tag {14}
$$

where  $H_{d} = \sum_{n=1}^{d}(1/n)$  is the Harmonic series. The upper bound is attained for the choice

$$
\wp (a | A, \psi) = \left\{ \begin{array}{l l} 1 & \text {i f} | \langle \psi | a \rangle | \geq | \langle \psi | a ^ {\prime} \rangle |, \forall a ^ {\prime} \neq a \\ 0 & \text {o t h e r w i s e .} \end{array} \right. \tag {15}
$$

Comparing this result with Eq. (13), we see that isotropic states are steerable if  $\eta > (H_d - 1) / (d - 1)$ . Moreover, it is easy to verify that when this inequality is saturated, Eq. (15) satisfies Eq. (5). Thus  $\eta_{\mathrm{steer}} = (H_d - 1) / (d - 1)$ .

(iii) Gaussian states.-Finally we investigate a general (multimode) bipartite Gaussian state  $W$  [19]. Such a state may be defined by its covariance matrix (CM)  $V_{\alpha \beta}$ . In (Alice, Bob) block form it appears as

$$
\operatorname {C M} [ W ] = V _ {\alpha \beta} = \left( \begin{array}{c c} V _ {\alpha} & C \\ C ^ {\top} & V _ {\beta} \end{array} \right). \tag {16}
$$

This represents a valid state iff  $V_{\alpha \beta} + i\Sigma_{\alpha \beta} \geq 0$  [19]. This is a linear matrix inequality (LMI), in which  $\Sigma_{\alpha \beta} = \Sigma_{\alpha} \oplus \Sigma_{\beta}$  is a symplectic matrix proportional to  $\hbar$ .

Rather than addressing steerability in general, we consider the case where Alice can only make Gaussian measurements, denoted by  $\mathfrak{G}_{\alpha}$ . A measurement  $A \in \mathfrak{G}_{\alpha}$  is described by a Gaussian positive operator with a CM  $T^{A}$  satisfying  $T^{A} + i\Sigma_{\alpha} \geq 0$  [19]. When Alice makes such a measurement, Bob's conditioned state  $\rho_{a}^{A}$  is Gaussian with a CM  $V_{\beta}^{A} = V_{\beta} - C(T^{A} + V_{\alpha})^{-1}C^{\top}$  [20].

Theorem 2. The Gaussian state  $W$  defined in Eq. (16) is not steerable by Alice's Gaussian measurements iff

$$
V _ {\alpha \beta} + \mathbf {0} _ {\alpha} \oplus i \Sigma_ {\beta} \geq 0. \tag {17}
$$

The proof has two parts. First, suppose Eq. (17) is true. Then using matrix inversion formulas [20], one sees that the matrix  $U \equiv V_{\beta} - CV_{\alpha}^{-1}C^{\top}$  satisfies

$$
U + i \Sigma_ {\beta} \geq 0 \quad \text {a n d} \quad \forall A \in \mathfrak {G} _ {\alpha}, V _ {\beta} ^ {A} - U \geq 0. \tag {18}
$$

The first LMI allows us to define an ensemble  $F^U = \{\rho_{\xi}^U \wp_{\xi}^U\}$  of Gaussian states with CM  $[\rho_{\xi}^U] = U$ , distinguished by their mean vectors  $(\xi)$ . The second LMI implies that  $\forall A, \rho_a^A$  is a Gaussian mixture (over  $\xi$ ) of such states. Therefore,  $W$  is not steerable by Alice.

Now suppose  $W$  is not steerable. Then there is some ensemble  $F$  satisfying Eq. (5). From the fact that  $V_{\beta}^{A}$  is independent of  $a$ , one sees that  $U = \sum_{\xi} \wp_{\xi} \times \mathrm{CM}[\rho_{\xi}]$  satisfies Eq. (18). But unless (17) is true, one sees that no such  $U$  satisfying Eq. (18) exists (again using standard matrix analysis [20]). Therefore, (17) must be true.

For the simplest case where Alice and Bob each have one mode with correlated positions  $q$  and momenta  $p$ , Reid

[13] has argued the EPR paradox is demonstrated iff the product of the conditional variances  $V(q_{\beta}|q_{\alpha})$  and  $V(p_{\beta}|p_{\alpha})$  violate the uncertainty principle. It is easy to verify that this occurs under precisely the same conditions as when Eq. (17) is violated. This confirms that the EPR paradox is merely a particular case of steering. As is well known [21], the Reid conditions are strictly stronger than the conditions for nonseparability.

We conclude with a brief listing of open questions. First, are there asymmetric states that are steerable by Alice but not by Bob? Second, Bell nonlocality is necessary and sufficient for certain tasks [22], and likewise nonseparability [23]. Is there a task (beyond the defining one) for which steerability is similarly useful? Third, do there exist steering analogs of Bell operators and entanglement witnesses? Finally, we note that we expect many applications of the concept of steering in quantum measurement theory and experimental quantum information.

This work was supported by the ARC and the State of Queensland. We thank Rob Spekkens, Volkher Scholz, Antonio Acin, and Michael Hall for useful discussions.

[1] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[2] E. Schrödinger, Proc. Cambridge Philos. Soc. 31, 553 (1935); 32, 446 (1936).  
[3] E. Schrödinger, Ann. Phys. (Berlin) 79, 361 (1926); 79, 489 (1926); 80, 437 (1926); 81, 109 (1926).  
[4] M. Vujicic and F. Herbut, J. Phys. A 21, 2931 (1988).  
[5] F. Verstraete, Ph.D. thesis, Katholieke University Leuven, 2002.  
[6] R. Clifton, J. Bub, and H. Halvorson, Found. Phys. 33, 1561 (2003).  
[7] R. W. Spekkens, Phys. Rev. A 75, 032110 (2007).  
[8] K.A. Kirkpatrick, Found. Phys. Lett. 19, 95 (2006).  
[9] J. S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964).  
[10] N. Gisin, Phys. Lett. A 154, 201 (1991).  
[11] R.F. Werner, Phys. Rev. A 40, 4277 (1989).  
[12] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Rev. Lett. 80, 5239 (1998).  
[13] M. D. Reid, Phys. Rev. A 40, 913 (1989).  
[14] G. M. D'Ariano, L. Maccone, and M. G. A. Paris, J. Phys. A 34, 93 (2001).  
[15] R. Horodecki, P. Horodecki, and M. Horodecki, Phys. Lett. A 200, 340 (1995).  
[16] A. Acin, N. Gisin, and B. Toner, Phys. Rev. A 73, 062105 (2006).  
[17] M. Horodecki and P. Horodecki, Phys. Rev. A 59, 4206 (1999).  
[18] D. Collins et al., Phys. Rev. Lett. 88, 040404 (2002).  
[19] G. Giedke and J. I. Cirac, Phys. Rev. A 66, 032316 (2002).  
[20] K. Zhou, J.C. Doyle, and K. Glover, Optimal and Robust Control (Prentice-Hall, Englewood Cliffs, NJ, 1996).  
[21] W.P. Bowen et al., Phys. Rev. A 69, 012304 (2004).  
[22] C. Brukner et al., Phys. Rev. Lett. 92, 127901 (2004).  
[23] L. Masanes, Phys. Rev. Lett. 96, 150501 (2006).