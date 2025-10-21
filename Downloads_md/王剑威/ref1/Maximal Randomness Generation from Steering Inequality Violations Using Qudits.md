# Maximal Randomness Generation from Steering Inequality Violations Using Qudits

Paul Skrzypczyk<sup>1</sup> and Daniel Cavalcanti<sup>2</sup>

<sup>1</sup>H. H. Wills Physics Laboratory, University of Bristol, Tyndall Avenue, Bristol, BS8 1TL, United Kingdom

$^{2}$ ICFO-Institut de Ciencies Fotoniques, The Barcelona Institute of Science and Technology,

08860 Casteldefels (Barcelona), Spain

(Received 14 March 2018; revised manuscript received 16 May 2018; published 26 June 2018)

We consider the generation of randomness based upon the observed violation of an Einstein-Podolsky-Rosen (EPR) steering inequality, known as one-sided device-independent randomness generation. We show that in the simplest scenario--involving only two parties and two measurements for the uncharacterised party with  $d$  outcomes--that there exist EPR steering inequalities whose maximal violation certifies maximal randomness generation, equal to  $\log(d)$  bits. We further show that all pure partially entangled full-Schmidt-rank states in all dimensions can achieve maximal violation of these inequalities, and thus lead to maximal randomness generation in the one-sided device-independent setting. More generally, the amount of randomness that can be generated is given by a semidefinite program, which we use to study the behavior for nonmaximal violations of the inequalities.

DOI: 10.1103/PhysRevLett.120.260401

Randomness is an important resource which has widespread use, ranging from Monte Carlo simulations to cryptographic keys. Generating "good" randomness is a notoriously difficult task, where the notion of good depends precisely on the context—whether it be the absence of subtle correlations which might lead to false conclusions in Monte Carlo simulations, or being perfectly uncorrelated from an adversary, and therefore private, in a cryptographic setting. In a classical, and therefore deterministic setting, there are two main approaches to generating randomness. The first is to use pseudo-random-number generators, which are able to turn a small amount of initial randomness (a seed), in a much larger string of numbers which appear random, under reasonable assumptions about the computational power available to test their quality. The second is to use chaotic systems, whose long-time behavior is essentially impossible to predict without perfect knowledge of the initial conditions.

Quantum theory, being fundamentally nondeterministic, provides an alternative route [1-3]. As a simple example, which path a photon takes after passing through a beam splitter is a fundamentally probabilistic event, and thus serves as a basic quantum random number generator. Quantum theory, as a fundamentally nonlocal theory [4], also provides a second route to randomness, which is much stronger than the first. Nonlocality is necessarily accompanied by uncertainty, with the latter providing the mechanism by which nonlocal effects can be possible at all without leading to signalling, i.e., to observable influences at a distance, which are forbidden by relativity. Thus observing nonlocality ensures that randomness is present, and due to monogamy—the fact that nonlocality cannot be simultaneously shared among multiple systems—this randomness must also have an element of privacy.

Bell nonlocality [4,5] is the most famous form of quantum nonlocality, and considers the correlations between distant measurement outcomes. From a modern perspective it is understood to constitute a device-independent (DI) form of nonlocality, since it does not rely on any characterization or trust of the underlying quantum state or measuring devices used. Device-independent randomness generation (DIRG) [6,7] was the first application of nonlocality to randomness generation. A user, who has access to a pair of devices, uses an initial seed of randomness to choose the measurement settings in a Bell test. If a Bell inequality is violated, the measurement outcomes are guaranteed to contain randomness, with the exact amount being a function of the observed violation. Thus, given the initial seed of randomness, a large amount of new private randomness can be generated [8]. The ratio between the seed size and the randomness generated is known as the expansion rate, and original scheme of Ref. [7] was able to achieve quadratic expansion, while later, more sophisticated schemes have now been shown to achieve better expansion, including exponential and unbounded expansion [11-17].

Einstein-Podolsky-Rosen (EPR) steering [18] is a second form of quantum nonlocality, that considers the correlations between measurement outcomes of one party, and the states prepared (or "steered") for a second party. From a modern perspective it is understood to constitute a one-sided-device-independent (1SDI) form of nonlocality, since it only relies on the characterization of one set of measuring devices [19]. Randomness generation can also be considered in the 1SDI setting (1SDIRG), with the user generating randomness from the measurement outcomes of the uncharacterized device [20-22]. Nonlocality in the form of EPR

steering is more robust than Bell nonlocality to imperfections in the untrusted components, such as loss and noise, due to the additional assumptions made. This in turn translates into better robustness for 1SDIRG. Thus, there is a trade-off between the assumptions and the robustness, and if the use of the 1SDI paradigm can be justified over the DI setting, which will typically depend upon the specific details of any actual implementation, then one can expect to obtain advantages for randomness generation.

Here we demonstrate an advantage of using the 1SDI setting, by demonstrating that unbounded randomness generation can be achieved using the simplest form of steering inequality (something that has not been observed in the DI scenario). We consider a linear steering test with only two choices of measurements that is naturally tailored to  $d$ -dimensional systems. We show that a maximal violation (which can be achieved using any pure full-rank entangled qudit) is only consistent with uniformly random outcomes, hence leading to  $\log_2 d$  bits of private randomness generated in the 1SDI setting. The amount of randomness generated from the initial seed can thus be arbitrarily large as  $d \to \infty$ .

Consider a situation where a user has two devices, labeled  $A$  and  $B$ . Device  $A$  accepts an input  $x$ , labeling a choice of measurement, and produces an outcome  $a$ , labeling an outcome. The device accepts one out of  $n$  inputs,  $x \in \{0, \dots, n - 1\}$ , and produces one out of  $d$  outcomes,  $a \in \{0, \dots, d - 1\}$ . Apart from the observable input-output behavior of the device, no further characterization will be assumed. Device  $B$ , on the other hand, will be assumed to be fully characterized. In particular, it will be assumed that the dimension of the system is known, and that known measurements can be performed. In particular, full tomography of the states of system  $B$  could be performed, although in general this is not necessary.

The information obtained in this scenario can be summarized by the conditional (unnormailed) states prepared for system  $B$ , conditioned on the different measurement choices  $x$  and outcomes  $a$  of system  $A$ :

$$
\sigma_ {a | x} ^ {B} = \operatorname {t r} _ {A} \left[ \left(M _ {a | x} \otimes \mathbb {I}\right) \rho^ {A B} \right], \tag {1}
$$

where  $\rho^{AB}$  is the (unknown) state shared between the two devices and  $M_{a|x}$  are the (unknown) measurement operators applied in  $A$ . The set  $\{\sigma_{a|x}^B\}$  is usually referred as to the assemblage [23,24]. Notice that one can recover both the conditional probability distributions,  $p(a|x) = \mathrm{tr}[\sigma_{a|x}]$ , and the normalized states  $\rho_{a|x}^B = \sigma_{a|x} / p(a|x)$ .

EPR steering is observed when the assemblage cannot be explained by a classical mechanism, called a local-hidden-state (LHS) model (see [24] for a review), which is witnessed by the violation of EPR steering inequalities of the form

$$
\beta := \operatorname {t r} \sum_ {a, x} F _ {a | x} ^ {B} \sigma_ {a | x} ^ {B} \leq \beta^ {\mathrm {L H S}}. \tag {2}
$$

$\{F_{a|x}\}_{a,x}$  is a collection of Hermitian operators, that should be measured by device  $B$  in the case of measurement  $x$  and outcome  $a$ , and  $\beta^{\mathrm{LHS}} \coloneqq \max_{\sigma_{a|x}^{\mathrm{LHS}}} \operatorname{tr} \sum_{a,x} F_{a|x} \sigma_{a|x}^{\mathrm{LHS}}$  is the maximal value of  $\beta$  that can be obtained by any classical assemblage.

When an assemblage violates an EPR steering inequality (i.e.,  $\beta >\beta^{\mathrm{LHS}}$ ) it is impossible that for all  $a$  and  $x$  that  $p(a|x)\in \{0,1\}$ . This means that the outcomes of system  $A$  must contain some randomness. This randomness can be quantified in the following way [22]. We assume the presence of an eavesdropper (Eve) holding a measurement device  $E$  which might share a tripartite state  $|\psi^{ABE}\rangle \langle \psi^{ABE}|$  with devices  $A$  and  $B$ . Eve is assumed to know the shared state and the form of the measurements in  $A$  and  $B$ . Eve's goal is to guess  $A$ 's outcomes when  $x = x^{*}$ , which happens successfully with probability

$$
P _ {\text {g u e s s}} \left(x ^ {*}\right) = \max  _ {\rho_ {e} ^ {A B}, p (e), M _ {a | x}} \sum_ {e} p (e) p (a = e | x ^ {*}, e), \tag {3}
$$

where  $\rho_{e}^{AB}$  is the state, labeled by  $e$ , that Eve distributes to the devices with probability  $p(e)$ , and without loss of generality Eve will guess  $a = e$  as the outcome of the measurement  $x = x^{*}$  for this particular state. Finally,

$$
p (a = e | x ^ {*}, e) = \operatorname {t r} \left[ \left(M _ {a = e | x = x ^ {*}} \otimes \mathbb {I}\right) \rho_ {e} ^ {A B} \right] \tag {4}
$$

is the probability that  $a = e$  when the measurement  $x = x^{*}$  is performed on the state  $\rho_{e}^{AB}$ . Crucially, in (3), the maximization takes place only over those strategies of Eve consistent with the observable data of the user, that is, given the observed violation  $\beta^{\mathrm{obs}}$  of a steering inequality. This constraint is formally given by

$$
\operatorname {t r} \sum_ {a, x} F _ {a | x} \sum_ {e} p (e) \operatorname {t r} _ {A} \left[ \left(M _ {a | x} \otimes \mathbb {I}\right) \rho_ {e} ^ {A B} \right] = \beta^ {\mathrm {o b s}}. \tag {5}
$$

The guessing probability  $P_{\mathrm{guess}}(x^{*})$  quantifies the optimal probability with which Eve can guess the outcome of device  $A$ . Whenever the guessing probability is less than unity this implies that Eve cannot perfectly guess the outcome, and hence it is inherently probabilistic (even given Eve's side information). The randomness in the outcomes is quantified by the min-entropy

$$
H _ {\min } \left(x ^ {*}\right) = - \log P _ {\text {g u e s s}} \left(x ^ {*}\right). \tag {6}
$$

Before proceeding to the main results, one final preliminary fact is needed, which concerns the uniqueness of probability distributions which can arise in the steering scenario. In particular, we can also prove the following:

Fact 1. Consider two sets of linearly independent states in  $\mathbb{C}^d$ ,  $\{| \phi_a \rangle \}_a$  and  $\{| \lambda_i \rangle \}_i$ , both of which span the Hilbert space. Assume that the expansion coefficients  $u_i^a$  and  $v_i^a$  do not vanish for all  $a, i$ , where  $|\phi_a\rangle = \sum_i u_i^a |\lambda_i\rangle$  and  $|\lambda_i\rangle = \sum_i v_i^a |\phi_a\rangle$ . Then there exists unique vectors  $\{q_a\}_a$  and  $\{\lambda_i\}_i$  (up to normalization) such that

$$
\sum_ {a} q _ {a} \left| \phi_ {a} \right\rangle \left\langle \phi_ {a} \right| = \sum_ {i} \lambda_ {i} \left| \lambda_ {i} \right\rangle \left\langle \lambda_ {i} \right|. \tag {7}
$$

In particular, up to normalization, these vectors are given by

$$
q _ {a} \propto \frac {\left\langle \psi_ {a} \mid \lambda_ {i} \right\rangle}{\left\langle \phi_ {a} \mid \omega_ {i} \right\rangle}, \quad \lambda_ {i} \propto \frac {\left\langle \phi_ {a} \mid \omega_ {i} \right\rangle}{\left\langle \psi_ {a} \mid \lambda_ {i} \right\rangle}, \tag {8}
$$

where  $\{| \psi_{a} \rangle \}_{a}$  and  $\{| \omega_{i} \rangle \}_{i}$  are the (unique) dual sets of vectors with respect to  $\{| \phi_{a} \rangle \}_{a}$  and  $\{| \lambda_{i} \rangle \}_{i}$ , satisfying  $\langle \psi_{b} | \phi_{a} \rangle = \delta_{ab}$ ,  $\langle \omega_{j} | \lambda_{i} \rangle = \delta_{ij}$ , which always exist due to the linear independence of the original sets [25].

Proof. This claim is proved by left-multiplying (7) by  $\langle \psi_b|$  and right-multiplying by  $|\omega_j\rangle$ . Note that the denominator of each expression is one of the (complex conjugate) expansion coefficients,  $\langle \phi_a|\omega_i\rangle = (u_i^a)^*$  and  $\langle \psi_a|\lambda_i\rangle = (v_a^i)^*$  and hence are nonvanishing by assumption.

In the case where  $q_{a} \geq 0 \forall a$  and  $\lambda_{i} \geq 0 \forall i$ , then (7) provide two ensemble decompositions of the same density operator. The above fact says that given only the vectors in these two ensembles, the probabilities are uniquely specified. It also says that two sets of linearly independent vectors with nonvanishing expansion coefficients uniquely specify a density operator.

In what follows it will be shown that obtaining the maximal violation of a certain EPR steering inequality involving only two measurements leads to maximal randomness generation. In particular, we will prove the following result:

Result 1. Consider a steering scenario where device  $A$  accepts 2 inputs and produces one of  $d$  outcomes, preparing states for system  $B$  in  $\mathbb{C}^d$ . Consider an EPR steering functional with elements

$$
F _ {a | x} = \left| \phi_ {a | x} \right\rangle \left\langle \phi_ {a | x} \right| \tag {9}
$$

where  $\{\left|\phi_{a|x}\right\rangle\}_{a}$  is a linearly independent set of  $d$  states in  $\mathbb{C}^d$ , for both values of  $x$ , and such that the expansion coefficients of one set in terms of the other is nonvanishing. The maximal value the steering functional can take is  $\beta = 2$ , and when this value is observed, the amount of randomness generated for the input  $x^{*}$  is

$$
H _ {\min } \left(x ^ {*}\right) = - \log \max  _ {a} q _ {a | x ^ {*}} \tag {10}
$$

where  $\{q_{a|0}\}_a$  and  $\{q_{a|1}\}_a$  are the unique probability distributions that satisfy  $\sum_{a} q_{a|0} |\phi_{a|0} \rangle \langle \phi_{a|0}| = \sum_{a} q_{a|1} |\phi_{a|1} \rangle \langle \phi_{a|1}|$ , as given by (8).

Proof. First note that the maximal value of the steering functional  $\beta = 2$  can only be achieved by an assemblage with elements  $\sigma_{a|x} = q(a|x)|\phi_{a|x}\rangle \langle \phi_{a|x}|$ . To see this, note that the value of the functional for a general assemblage with elements  $\sigma_{a|x} = p(a|x)\rho_{a|x}$  is  $\beta = \sum_{a,x}p(a|x)\langle \phi_{a|x}|\rho_{a|x}|\phi_{a|x}\rangle$ . For every  $a$  and  $x$  such that  $p(a|x)\neq 0$ , it must be that  $\langle \phi_{a|x}|\rho_{a|x}|\phi_{a|x}\rangle = 1$ ; otherwise  $\beta < 2$ . The only choice of  $\rho_{a|x}$  that satisfies this is  $\rho_{a|x} = |\phi_{a|x}\rangle \langle \phi_{a|x}|$ . For  $a$  and  $x$  such that  $p(a|x) = 0$ , the choice of  $\rho_{a|x}$  is arbitrary and can therefore be chosen to be  $|\phi_{a|x}\rangle \langle \phi_{a|x}|$  without loss of generality.

From Fact 1, it follows that the  $q(a|x)$  are uniquely determined, as the only pair of probability distributions  $\{q_{a|0}\}_{a}$  and  $\{q_{a|1}\}_{a}$  which satisfy  $\sum_{a} q_{a|0} |\phi_{a|0} \rangle \langle \phi_{a|0}| = \sum_{a} q_{a|1} |\phi_{a|1} \rangle \langle \phi_{a|1}|$  [26].

Turning our attention to randomness generation, when a violation  $\beta = 2$  is observed, the above implies that the most general strategy of Eve is to prepare assemblages of the form

$$
\sigma_ {a | x} ^ {e} = q (a, e | x) \left| \phi_ {a | x} \right\rangle \left\langle \phi_ {a | x} \right|, \tag {11}
$$

such that  $\sum_{e}q(a,e|x) = q_{a|x}$ . Indeed, the reduced assemblage of the devices of the user,  $\sum_{e}\sigma_{a|x}^{e}$ , by virtue of attaining a maximal violation, from the above must have elements of the form  $q_{a|x}|\phi_{a|x}\rangle \langle \phi_{a|x}|$ . The only way for a sum of operators to be rank 1 is for each element to be proportional to the same rank-1 element, and hence the claim follows. The nonsignaling constraint from (3) then takes the form

$$
\begin{array}{l} \sum_ {a} q (a | e, 0) q (e) \left| \phi_ {a | 0} \right\rangle \left\langle \phi_ {a | 0} \right| \\ = \sum_ {a} q (a | e, 1) q (e) \left| \phi_ {a | 1} \right\rangle \left\langle \phi_ {a | 1} \right|, \tag {12} \\ \end{array}
$$

where we have used no-signaling to write  $q(a, e|x) = q(a|e, x)q(e|x) = q(a|e, x)q(e)$ . However, (12) has the same form as (7) from Fact 1, and hence it must be the case that  $q(a|e, x) = q_{a|x}$ , due to the uniqueness of the distributions. Crucially this shows that  $a$  is conditionally independent of  $e$ . Therefore, Eve's guessing probability in this case is a simple optimization over the probability distribution  $\{p(e)\}_e$ , given by

$$
P _ {\text {g u e s s}} \left(x ^ {*}\right) = \max  _ {\{q (e) \} _ {e}} \sum_ {e} p (e) q _ {e | x ^ {*}} = \max  _ {e} q _ {e | x ^ {*}}. \tag {13}
$$

Using the definition of the min-entropy (6) the result follows.

This shows that Eve can do no better than guess the most probable outcome of device  $A$ , which is the same as could be achieved without the use of quantum theory. Moreover, using the above, by considering a situation

where  $q_{a|x^*} = 1 / d$ , i.e., where the only assemblage consistent with the violation of the inequality has a uniformly random outcome for the measurement  $x^*$ , then  $H_{\min}(x^*) = \log(d)$  bits of randomness are generated in a 1SDI scenario. In what follows we show that this can be achieved by making appropriate measurements on all pure partially entangled Schmidt-rank- $d$  states. In particular, note the following:

Result 2. Consider a pure partially entangled Schmidt-rank-  $d$  state in  $\mathbb{C}^d\otimes \mathbb{C}^d$ , given by  $|\Psi \rangle = \sum_{i}\sqrt{\lambda_{i}} |i\rangle |i\rangle$ , where  $\lambda_{i} > 0$  for all  $i$ , and  $\sum_{i}\lambda_{i} = 1$  are the Schmidt coefficients. Consider two measurements with elements  $M_{a|0} = |a\rangle \langle a|$  and  $M_{a|1} = F|a\rangle \langle a|F^{\dagger}$ , where  $F$  is the  $d$ -dimensional discrete Fourier transform. Finally consider an EPR steering functional with elements  $F_{a|0} = |a\rangle \langle a|$  and  $F_{a|1} = |\chi_a\rangle \langle \chi_a|$ , where  $|\chi_{a}\rangle = \sum_{i}\sqrt{\lambda_{i}}\langle a|F^{\dagger}|i\rangle |i\rangle /\sqrt{d}$ . Then, (i) using the measurements  $\{M_{a|x}\}_{a}$  on the state  $|\Psi \rangle$  leads to an assemblage which maximally violates the EPR steering functional with elements  $F_{a|x}$ , i.e., achieves  $\beta = 2$ , and (ii) the outcome probabilities are uniformly random for the second measurement of device A,  $p(a|1) = 1 / d$  for all  $a$ . Together, the above two facts imply that maximal randomness can be generated using this 1SDIRG scheme,  $H_{\mathrm{min}}(x = 1) = \log d$ .

Proof. Performing the measurements with elements  $M_{a|x}$  on the state  $|\Psi \rangle$  leads to an assemblage with elements  $\sigma_{a|0} = \lambda_a|a\rangle \langle a|$  and  $\sigma_{a|1} = (1 / d)|\chi_a\rangle \langle \chi_a|$ , where we used the fact that  $|\langle i|F|a\rangle |^2 = 1 / d$  for all  $a$ ,  $i$  to evaluate  $p(a|1) = \mathrm{tr}[F|a\rangle \langle a|F^\dagger \otimes \mathbb{I})|\Psi \rangle \langle \Psi |] = \sum_i\lambda_i|\langle i|F|a\rangle |^2 = 1 / d$ . This demonstrates the second claim. Direct calculation shows that this assemblage achieves the value  $\beta = 2$  for the EPR steering functional given, proving the first claim.

The set  $\{|a\rangle \}_{a}$  forms an orthonormal basis for  $\mathbb{C}^d$ . The set  $\{|\chi_a\rangle \}_a$  forms a nonorthogonal basis for  $\mathbb{C}^d$  with dual basis  $|\theta_{a}\rangle = \sqrt{d}\sum_{i}1 / \sqrt{\lambda_{i}}\langle i|F^{\dagger}|a\rangle |i\rangle$ . It follows that the expansion coefficients of  $|\chi_{a}\rangle$  in terms of  $|a\rangle$ , and vice versa, are nonvanishing. Result 1 can thus be applied, since all of the required conditions hold. In conjunction with the fact that  $p(a|1) = 1 / d$ , this leads to

$$
H _ {\min } (x = 1) = - \log \max  _ {a} p (a | 1) = \log d. \tag {14}
$$

There are two points worth noting. First, if we consider maximally entangled states, where  $\lambda_{i} = 1 / d$ , then  $p(a|0) = 1 / d$  also. In this case, one can naturally consider obtaining randomness from both inputs. Moreover, in this case  $F_{a|x} = (|\phi_{a|x}\rangle \langle \phi_{a|x}|)^{\intercal}$  forms a measurement for each  $x$ , and hence only two measurements need to be performed at  $B$ , as opposed to  $d + 1$  different measurements in the general case.

Second, if in the above we were to replace the Schmidt-rank-  $d$  state with a Schmidt-rank-  $k$  state, for  $k < d$ , then the analysis can still be applied on the support of the reduced

state of system  $B$ , which will be rank  $k$ , and  $H_{\min}(x = 1) = \log k$  bits of randomness will be generated, the maximal possible using projective measurements for such a state.

Note that in the above analysis we have performed only the ideal analysis, assuming infinite statistics. To implement the above in practice, with only finite statistics, the protocol of [7], which is outlined in full detail in [9], for DIRG can be applied also to the 1SDIRG scheme studied here.

In total, the above demonstrates the power of the 1SDI paradigm for randomness generation. The steering functionals presented constitute the simplest possible functionals, comprising only two choices of measurement for the uncharacterized or untrusted device. Nevertheless, they are powerful enough to generate the maximal amount of randomness possible when considering projective measurements on a partially entangled state. By allowing the local dimension  $d$  to tend to infinity, this scheme can generate an unbounded amount of randomness from this simple scheme.

So far, we have only considered the case of a perfect violation of the steering inequalities, and shown that this leads to maximal randomness generation. Since a perfect violation can never be observed in practice, it is also important to analyse what happens for an arbitrary violation  $\beta < 2$ . This can be carried out efficiently numerically by solving the semidefinite program (SDP) presented in the Supplemental Material [27]. This method easily allows one to consider dimensions up to  $d = 32$  on a standard desktop computer [29]. As an illustration, in Fig. 1 we plot the amount of generated randomness as a function of  $\beta^{\mathrm{obs}}$  for  $d = 4, 8, 16$ . In the inset, we also compare the randomness generated using our 1SDIRG scheme to the a DIRG scheme, as function of visibility of the maximally entangled state.

![](images/23ea008c2df3c0863aac6b03ccadd1bdd01bcb43e782e6c7fd74d767a1d3d849.jpg)  
FIG. 1. Randomness generated  $H_{\mathrm{min}}(x = 1)$ , as a function of the observed violation of the steering inequality,  $\beta^{\mathrm{obs}}$ , for dimension  $d = 4, 8, 16$ . Inset: comparison to DIRG. We consider local randomness generation using an isotropic state  $\rho_w = w|\Phi^+ \rangle \langle \Phi^+| + (1 - w)\mathbb{1} / d^2$  and optimal measurement settings for violating the Collins-Gisin-Linden-Massar-Popescu (CGLMP) [31] and Salavrakos-Augusiak-Tura-Wittek-Acin-Pironio (SATWAP) [32] Bell inequalities for  $d = 8$ . The code used to generate this figure is available at [33].

In [34] the steering inequalities presented here were recently tested. In particular, [34] presented an integrated silicon quantum photonic device with path encoded qubits up to  $d = 16$ . In the device each photon can be prepared in a superposition over up to 16 spatial modes and entanglement can be generated between a pair of photons using coherent and controllable excitation of  $d$  integrated identical photon pair sources. Arbitrary projective measurements can also be performed, using an integrated reconfigurable interferometric network.

This device was used to prepare maximally entangled states in dimensions  $d = 2$  to 16, and a steering inequality of the form (9) was tested, using as the two bases the path basis and its Fourier transform. The authors demonstrated that higher dimensional systems require lower visibilities (lower inequality violation) to achieve the same amount of randomness.

In this work we have considered the task of one-sided device-independent randomness generation. We have presented a general construction based on steering functionals in arbitrary dimension in the simplest scenario (consisting of only two inputs to the uncharacterized device). We have shown that a maximal violation of the associated steering inequality certifies that the outcomes of the uncharacterized device are completely unpredictable, even for a potential adversary, and hence maximal private randomness can be generated. We have shown that for every entangled state it is possible to construct a steering functional using our construction that is maximally violated, and hence that all entangled states in arbitrary dimension lead to maximal randomness generation using the simplest possible 1SDIRG scheme.

In the case of nonmaximal violation of the steering inequality the amount of randomness that can be generated in a 1SDI manner can be computed using the technique of semidefinite programming. This provides a feasible method for dimensions up until  $d \leq 32$ . An important open problem is to obtain analytic lower bounds on the amount of randomness that can be obtained for near perfect violation which apply for arbitrary dimension  $d$ . This will provide a practical solution for arbitrary experimental situations. A route to achieve this would be to generalize Fact 1 to allow for some uncertainty in the sets of states, and to see how much freedom this allows for in the associated probability distributions, which might be of independent interest.

In a related direction, it would be interesting to understand what role loss plays for 1SDIRG. The inequalities considered here are closely related to those put forward in [35] for loss-tolerant EPR steering demonstrations. It would be interesting to extend the analysis here to these inequalities.

Finally, the construction here is tailored to projective measurements, and hence in dimension  $d$ , up to  $H_{\min}(x^*) = \log d$  bits of randomness are generated. By using generalized

positive-operator-valued measurements, it is in principle possible to generate up to  $H_{\min}(x^{*}) = 2 \log d$  bits of randomness, by using measurements with  $d^2$  outcomes. An interesting open question is whether the construction presented here can be generalized to this case also.

D.C. acknowledges the Ramón y Cajal fellowship, Spanish MINECO (QIBEQI FIS2016-80773-P and Severo Ochoa SEV-2015-0522), Fundació Cellex, and Generalitat de Catalunya (SGR875 and CERCA Program). P.S. acknowledges support from a Royal Society URF (UHQT).

[1] A. Acín and L. Masanes, Certified randomness in quantum physics, Nature (London) 540, 213 (2016).  
[2] M. Herrero-Collantes and J.C. Garcia-Escartin, Quantum random number generators, Rev. Mod. Phys. 89, 015004 (2017).  
[3] M. N. Bera, A. Acin, M. Kuš, M. W. Mitchell, and M. Lewenstein, Randomness in quantum mechanics: Philosophy, physics and technology, Rep. Prog. Phys. 80, 124001 (2017).  
[4] J. S. Bell, On the Einstein Podolsky Rosen paradox, Physics 1, 195 (1964).  
[5] N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani, and S. Wehner, Bell nonlocality, Rev. Mod. Phys. 86, 419 (2014).  
[6] R. Colbeck, Quantum and relativistic protocols for secure multi-party computation, arXiv:0911.3814.  
[7] S. Pironio et al., Random numbers certified by Bell's theorem, Nature (London) 464, 1021 (2010).  
[8] Under certain natural assumptions [9,10], the initial source of randomness can be assumed to be public. In this case the process can be seen as converting public into private randomness.  
[9] S. Pironio and S. Massar, Security of practical private randomness generation, Phys. Rev. A 87, 012336 (2013).  
[10] S. Pironio, Random, “choices”, and the locality loophole, arXiv:1510.00248.  
[11] R. Colbeck and A. Kent, Private randomness expansion with untrusted devices, J. Phys. A 44, 095305 (2011).  
[12] U. Vazirani and T. Vidick, Certifiable quantum dice, Phil. Trans. R. Soc. A 370, 3432 (2012).  
[13] M. Coudron and M. H. Yuen, Infinite randomness expansion and amplification with a constant number of devices, arXiv:1310.6755.  
[14] C.A. Miller and Y. Shi, Robust protocols for securely expanding randomness and distributing keys using untrusted quantum devices, J. ACM, 63, 33 (2016).  
[15] K.M. Chung, Y. Shi, and X. Wu, Physical randomness extractors: Generating random numbers with minimal assumptions, arXiv:1402.4797.  
[16] C. A. Miller and Y. Shi, Universal security for randomness expansion from the spot-checking protocol, SIAM J. Computing 46, 1304 (2017).  
[17] R. Arnon-Friedman, R. Renner, and T. Vidick, Simple and tight device-independent security proofs, arXiv:1607.01797.

[18] A. Einstein, B. Podolsky, and N. Rosen, Can quantum-mechanical description of physical reality be considered complete?, Phys. Rev. 47, 777 (1935).  
[19] H. M. Wiseman, S. J. Jones, and A. C. Doherty, Steering, Entanglement, Nonlocality, and the Einstein-Podolsky-Rosen Paradox, Phys. Rev. Lett. 98, 140402 (2007).  
[20] C. Branciard, E. G. Cavalcanti, S. P. Walborn, V. Scarani, and H. M. Wiseman, One-sided device-independent quantum key distribution: Security, feasibility, and the connection with steering, Phys. Rev. A 85, 010301(R) (2012).  
[21] Y.Z. Law, L.P. Thinh, J.D. Bancal, and V. Scarani, Quantum randomness extraction for various levels of characterization of the devices, J. Phys. A 47, 424028 (2014).  
[22] E. Passaro, D. Cavalcanti, P. Skrzypczyk, and A. Acin, Optimal randomness certification in the quantum steering and prepare-and-measure scenarios, New J. Phys. 17, 113010 (2015).  
[23] M. F. Pusey, Negativity and steering: A stronger Peres conjecture, Phys. Rev. A 88, 032313 (2013).  
[24] D. Cavalcanti and P. Skrzypczyk, Quantum steering: A review with focus on semidefinite programming, Rep. Prog. Phys. 80, 024001 (2017).  
[25] Note that the right-hand side of each equation depends on both  $i$  and  $a$ . However, after normalizing, it is indeed the case that the correct dependence is obtained, i.e., the right-hand side of the left-hand equation becomes independent of  $i$ , and vice versa.

[26] Note that Fact 1 did not guarantee that these are probability vectors. Here we will restrict our discussion to situations where this is the case. These are in fact the only situations that can arise in a steering experiment.  
[27] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.120.260401, which includes Ref. [28], for the SDP formulation of the guessing probability.  
[28] S. Boyd and L. Vandenberghe, Convex Optimization (Cambridge University Press, Cambridge, England, 2004).  
[29] Using the CVX package [30] for MATLAB, less than 10 min were required to obtain a solution.  
[30] M. Grant and S. Boyd, CVX: Matlab software for disciplined convex programming, version 2.1, http://cvxr.com/cvx.  
[31] D. Collins, N. Gisin, N. Linden, S. Massar, and S. Popescu, Bell Inequalities for Arbitrarily High-Dimensional Systems, Phys. Rev. Lett. 88, 040404 (2002).  
[32] A. Salavrakos, R. Augusiak, J. Tura, P. Wittek, A. Acín, and S. Pironio, Bell Inequalities Tailored to Maximally Entangled States, Phys. Rev. Lett. 119, 040402 (2017).  
[33] Code available at https://git.io/vxkmL.  
[34] J. Wang et al., Multidimensional quantum entanglement with large-scale integrated optics, Science 360, 285 (2018).  
[35] P. Skrzypczyk and D. Cavalcanti, Loss-tolerant Einstein-Podolsky-Rosen steering for arbitrary-dimensional states: Joint measurability and unbounded violations under losses, Phys. Rev. A 92, 022354 (2015).