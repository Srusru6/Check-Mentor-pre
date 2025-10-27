# Quantum nonlocality in two three-level systems

A. Acín, $^{1,2}$  T. Durt, $^{3}$  N. Gisin, $^{1}$  and J. I. Latorre $^{2}$

$^{1}$ GAP-Optique, 20 rue de l'École-de-Médecine, CH-1211 Geneva 4, Switzerland

$^{2}$ Departament d'Estructura i Constituents de la Materia, Diagonal 647, E-08028 Barcelona, Spain

$^{3}$ TONA, Vrije Universiteit Brussel, Pleinlaan 2, B-1050 Brussels, Belgium

(Received 29 November 2001; published 8 May 2002)

Recently a new Bell inequality has been introduced by Collins et al. [Phys. Rev. Lett. 88, 040404 (2002)], which is strongly resistant to noise for maximally entangled states of two  $d$ -dimensional quantum systems. We prove that a larger violation, or equivalently a stronger resistance to noise, is found for a nonmaximally entangled state. It is shown that the resistance to noise is not a good measure of nonlocality and we introduce some other possible measures. The nonmaximally entangled state turns out to be more robust also for these alternative measures. From these results it follows that two von Neumann measurements per party may be not optimal for detecting nonlocality. For  $d = 3,4$ , we point out some connections between this inequality and distillability. Indeed, we demonstrate that any state violating it, with the optimal von Neumann settings, is distillable.

DOI: 10.1103/PhysRevA.65.052325

PACS number(s): 03.67.-a, 03.65.Ta

# I. INTRODUCTION

Since the seminal work of Bell [1], it is known that no local variable (LV) theory [2] can reproduce all the statistical results predicted by quantum mechanics for states of composite systems. In fact, it was proven that the correlations observed between two spin- $\frac{1}{2}$  particles in the singlet state violate some inequalities, called Bell inequalities, that any LV theory satisfies. This provided a possible definition of quantum nonlocality: a quantum state is said to be nonlocal when it violates a Bell inequality. More recently, it was shown that any pure state that is not separable [3], i.e., such that the parties cannot prepare it using only local operations and classical communication (LOCC), violates a Bell inequality [4,5]. Unfortunately, the distinction between local and nonlocal states is not as clear for density matrices. Indeed there exist mixed states that, despite being entangled, do not violate any Bell inequality [6] (see, however, Ref. [7]). Consequently, there are two different ways of considering quantum nonlocality: entanglement (quantum nonlocal resources are required for preparing the state) and violation of Bell inequalities.

The interest in entanglement has dramatically increased during the last two decades due to the fact that entanglement is the key ingredient in many of the recent quantum information applications. Many efforts have been devoted to quantify entanglement (see, for instance, Refs. [8,9]) as a resource, and nowadays bipartite pure-state entanglement is well understood. The maximally entangled state of a bipartite system,  $|\Psi \rangle \in \mathcal{C}^d\otimes \mathcal{C}^d$ , reads

$$
| \Psi \rangle = \frac {1}{\sqrt {d}} \sum_ {i = 0} ^ {d - 1} | j j \rangle , \tag {1}
$$

where  $|j\rangle$  are the orthonormal bases in each subsystem. Given an entangled state in  $\mathcal{C}^d\otimes \mathcal{C}^d$ , it is important to know if it can be distilled, i.e., if  $N$  copies of it can be transformed by

LOCC into  $M$  copies of  $|\Psi \rangle$ . State distillability, or useful quantum correlations, offers an alternative way of analyzing quantum nonlocality. All bipartite entangled pure states can be reversibly transformed using LOCC into  $|\Psi \rangle$  (in the so-called asymptotic regime). The ratio of the conversion is equal to the entropy of entanglement [8]. For the mixed-state case, however, the picture is again not clear: indeed it is not known when a given entangled density matrix is distillable. It is also not known how distillability properties of mixed states are connected to Bell inequality violation [10-13].

All these questions about nonlocality in mixed states are essentially solved for the simplest case of two two-level systems, also called qubits. There, the Peres-Horodecki criterion of positivity of the partial transposition [14,15] detects if a given state is separable or entangled. Furthermore, all two-qubit entangled states are distillable [16]. As far as the Bell inequality is concerned, the CHSH inequality [17] plays a very important role [18], and it is already known when a quantum state violates it [19]. Its maximal violation is only obtained for the maximally entangled state of two spin- $\frac{1}{2}$  particles.

Recently an inequality [20,21] has been found, which generalizes the CHSH inequality to systems of arbitrary dimension,  $d$ , often referred to as qudits. This offers the opportunity of testing some of the concepts seen above for this inequality. This is the scope of the present paper. We see that, surprisingly, the maximal violation of the inequality, under von Neumann measurements, is not obtained for the maximally entangled state of two three-level systems or qutrits (Sec. III). This leads us to analyze if the resistance to noise is a correct measure of nonlocality. By a simple example we see that it is not. Furthermore, we prove that any state violating the inequality with the optimal settings is distillable, and the witness that comes from it [11] is decomposable (Sec. IV).

# II. BELL INEQUALITY FOR QUTRITS

In this section we review the Bell inequality for qutrits obtained in Refs. [20,21]. The two parties,  $A$  and  $B$ , are al-

lowed to perform two different three-outcome measurements,  $A_{1}$  and  $A_{2}$  for  $A$ , and  $B_{1}$  and  $B_{2}$  for  $B$ . Denoting by  $P(A_{i} = B_{j} + k)$  the probability that the outcomes for parties  $A$  and  $B$ , measuring  $A_{i}$  and  $B_{j}$ , differ by  $k$  modulo  $d$  (in this case  $d = 3$ ), one can consider the following Bell inequality:

$$
\begin{array}{l} I _ {3} = P \left(A _ {1} = B _ {1}\right) + P \left(B _ {1} = A _ {2} + 1\right) + P \left(A _ {2} = B _ {2}\right) + P \left(B _ {2} = A _ {1}\right) \\ - P \left(A _ {1} = B _ {1} - 1\right) - P \left(B _ {1} = A _ {2}\right) - P \left(A _ {2} = B _ {2} - 1\right) \\ - P \left(B _ {2} = A _ {1} - 1\right) \leqslant 2. \tag {2} \\ \end{array}
$$

The authors of Refs. [20,21] analyzed the violation of this inequality by the maximally entangled state (1) of two qubits. They consider the following settings: first the two parties apply a unitary operation on each subsystem with only nonzero terms in the diagonal equal to  $e^{i\phi_a(j)}$  for  $A$  and  $e^{i\varphi_b(j)}$  for  $B$ , with  $j = 0,1,2$  and  $a,b = 1,2$ . These unitary operations are denoted by  $U(\vec{\phi}_a)$ , where  $\vec{\phi}_a \equiv [\phi_a(0),\phi_a(1),\phi_a(2)]$ , for party  $A$ , and the same for  $B$  with  $\varphi$  instead of  $\phi$ . The values of these phases are

$$
\phi_ {1} (j) = 0, \quad \phi_ {2} (j) = \frac {\pi}{3} j, \quad \varphi_ {1} (j) = \frac {\pi}{6} j, \quad \varphi_ {2} (j) = - \frac {\pi}{6} j, \tag {3}
$$

with  $j = 0,1,2$ . In this scenario, the freedom in the choice of the measurement the parties apply is given by this first unitary transformation. Then, party  $A$  carries out a discrete Fourier transform,  $U_{\mathrm{FT}}$  [22], and  $B$  applies  $U_{\mathrm{FT}}^*$ , and finally they measure in the initial basis  $|j\rangle$ . With these experimental settings, quantum mechanics predicts that  $I_3(|\Psi \rangle) = 4(2\sqrt{3} + 3)/9 \simeq 2.8729$ . Numerical simulations [20,23] show that this is the maximum value of  $I_3$  achieved starting from the maximally entangled state,  $|\Psi \rangle$ . It is then conjectured that the described experimental settings are optimal for  $|\Psi \rangle$  with this inequality.

It is possible to define a more absolute measure of nonlocality in the following way: the initial entangled state,  $|\Psi \rangle$ , is mixed with some amount of noise, the resulting state being equal to

$$
\rho = \lambda | \Psi \rangle \langle \Psi | + (1 - \lambda) ^ {\frac {1}{9}}, \tag {4}
$$

when  $0 \leqslant \lambda \leqslant 1$ . The entanglement in  $\rho$  decreases with  $\lambda$ , so one can look for the maximal amount of noise, or minimum  $\lambda$ , such that it is still not possible to build a LV model for the predicted probabilities. This measure of nonlocality, known as the resistance to noise, depends on the experimental settings, that is, on the number and the type of measurements each party can apply. The inequality (2) reproduces for Eq. (1) the same resistance to noise as it was found numerically in Ref. [23], with two von Neumann measurements on each

side. This means that the probabilities resulting from performing these measurements on the state (4) admit a LV model when

$$
0 \leqslant \lambda \leqslant \frac {2}{I _ {3} (| \Psi \rangle)} \simeq 0. 6 9 6 2. \tag {5}
$$

# III. MAXIMAL VIOLATION OF THE INEQUALITY

The authors of Refs. [20,21] focused their attention onto the violation of this inequality for the maximally entangled state of two qutrits. However, it may happen that a larger value of  $I_{3}$  is found if we consider a different initial state.

For the experimental settings (3), one can derive the Bell operator [24] associated with this inequality. The joint probability,  $P(A_{a} = j, B_{b} = k)$ , of detecting result  $j$  in  $A$ ,  $k$  in  $B$ , when  $A_{a}$  and  $B_{b}$  are measured and the initial state is  $|\Phi \rangle \in \mathcal{C}^3 \otimes \mathcal{C}^3$ , is given by

$$
\begin{array}{l} \operatorname {t r} \left[ \Pi_ {j} \otimes \Pi_ {k} V (\vec {\phi} _ {a}) \otimes V (\vec {\varphi} _ {b}) | \Phi \rangle \langle \Phi | V (\vec {\phi} _ {a}) ^ {\dagger} \otimes V (\vec {\varphi} _ {b}) ^ {\dagger} \right] \\ = \operatorname {t r} \left[ V \left(\vec {\phi} _ {a}\right) ^ {\dagger} \otimes V \left(\vec {\varphi} _ {b}\right) ^ {\dagger} \Pi_ {j} \otimes \Pi_ {k} V \left(\vec {\phi} _ {a}\right) \otimes V \left(\vec {\varphi} _ {b}\right) | \Phi \rangle \langle \Phi | \right], \tag {6} \\ \end{array}
$$

where  $V(\vec{\phi}_a) \equiv U_{\mathrm{FT}}U(\vec{\phi}_a)$  and  $V(\vec{\varphi}_b) \equiv U_{\mathrm{FT}}^* U(\vec{\varphi}_b)$ . From this formula the Bell operator,  $B$ , such that

$$
I _ {3} (\left| \Phi \right\rangle) = \operatorname {t r} (B | \Phi) \left\langle \Phi \right|) = \left\langle B \right\rangle_ {\Phi}, \tag {7}
$$

is found, and it reads

$$
B = \left( \begin{array}{c c c c c c c c c} 0 & 0 & 0 & 0 & \frac {2}{\sqrt {3}} & 0 & 0 & 0 & 2 \\ 0 & 0 & 0 & 0 & 0 & \frac {2}{\sqrt {3}} & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac {2}{\sqrt {3}} & 0 \\ \frac {2}{\sqrt {3}} & 0 & 0 & 0 & 0 & 0 & 0 & 0 & \frac {2}{\sqrt {3}} \\ 0 & \frac {2}{\sqrt {3}} & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & \frac {2}{\sqrt {3}} & 0 & 0 & 0 & 0 & 0 \\ 2 & 0 & 0 & 0 & \frac {2}{\sqrt {3}} & 0 & 0 & 0 & 0 \end{array} \right). \tag {8}
$$

TABLE I. Violation of the inequality (10) for two quuds,  $\mathcal{C}^d \otimes \mathcal{C}^d$ , up to  $d = 8$ . The values obtained for the maximally entangled state (1) and the maximal violation of the inequality corresponding to the largest eigenvalue of the Bell operator are shown.  

<table><tr><td>Dimension</td><td>Violation for |Ψ⟩</td><td>Maximal violation (for |Ψmv⟩)</td><td>Difference (%)</td></tr><tr><td>3</td><td>2.8729</td><td>2.9149</td><td>1.4591</td></tr><tr><td>4</td><td>2.8962</td><td>2.9727</td><td>2.6398</td></tr><tr><td>5</td><td>2.9105</td><td>3.0157</td><td>3.6133</td></tr><tr><td>6</td><td>2.9202</td><td>3.0497</td><td>4.4345</td></tr><tr><td>7</td><td>2.9272</td><td>3.0776</td><td>5.1411</td></tr><tr><td>8</td><td>2.9324</td><td>3.1013</td><td>5.7588</td></tr></table>

The maximal violation of the inequality with these settings corresponds to the maximum eigenvalue of  $B$ , which is equal to  $1 + \sqrt{11 / 3} \simeq 2.9149$ . Note that this value is a bit larger than the violation obtained for  $|\Psi \rangle$ . Indeed its corresponding eigenvector is a nonmaximally entangled state of two qutrits, which reads,

$$
\left| \Psi_ {m v} \right\rangle = \frac {1}{\sqrt {n}} \left(\left| 0 0 \right\rangle + \gamma \left| 1 1 \right\rangle + \left| 2 2 \right\rangle\right), \tag {9}
$$

where  $\gamma = (\sqrt{11} -\sqrt{3}) / 2\cong 0.7923$  and  $n = 2 + \gamma^2$  (the same results are obtained starting from the inequality in Ref. [21]). All the details of the calculation are given in the Appendix.

It is natural to ask about the optimality of the chosen set of measurements. We have performed a numerical search for this inequality, varying freely the two von Neumann measurements performed by each of the parties and the initial state. The maximal violation is indeed obtained by the configuration shown above. Moreover, in the Appendix we prove that these experimental settings give a local maximum for the largest eigenvalue of  $B$ .

The Bell inequality (2) was also extended to arbitrary dimension in Ref. [20]. There it was shown that the combination of joint probabilities

$$
\begin{array}{l} I _ {d} = \sum_ {k = 0} ^ {[ d / 2 ] - 1} \left(1 - \frac {2 k}{d - 1}\right) [ P (A _ {1} = B _ {1} + k) + P (B _ {1} = A _ {2} + k + 1) \\ + P \left(A _ {2} = B _ {2} + k\right) + P \left(B _ {2} = A _ {1} + k\right) - P \left(A _ {1} = B _ {1} - k - 1\right) \\ - P \left(B _ {1} = A _ {2} - k\right) - P \left(A _ {2} = B _ {2} - k - 1\right) \\ - P \left(B _ {2} = A _ {1} - k - 1\right) ] \leqslant 2, \tag {10} \\ \end{array}
$$

for LV models. However, this inequality can be violated if we consider the maximally entangled state (1) and similar experimental settings with  $\phi_1(j) = 0$ ,  $\phi_2(j) = j\pi /d$ ,  $\varphi_{1}(j)$ $= j\pi /(2d)$ , and  $\varphi_{2}(j) = -j\pi /(2d)$ , where  $j = 0,\dots ,d - 1$ . Indeed, this inequality reproduces the resistance to noise obtained numerically in Ref. [23], but now for two Bell multi

ports [25] on each side. Starting from Eq. (10) we can derive the corresponding Bell operator and a larger violation is again found for partially entangled states of two quuds. Table I summarizes these results up to  $d = 8$ . Note that the difference between the violation for  $|\Psi \rangle$  and  $|\Psi_{mv}\rangle$  increases with increase in the dimension.

These results are quite surprising. Previous numerical work in Ref. [23] showed that the resistance to noise for the maximally entangled state of two qubits with two von Neumann measurements per party is indeed the one predicted by this Bell inequality (5). Nevertheless, there exists a nonmaximally entangled state,  $|\Psi_{mv}\rangle$ , whose quantum correlations are more resistant to noise, since its violation of Eq. (2) is larger. Let us mention here that the parties, if they start with the maximally entangled state  $|\Psi \rangle$ , are always able to prepare by LOCC and with probability one the state  $|\Psi_{mv}\rangle$ , and then to check the violation of the Bell inequality. This leads us to analyze more precisely whether the resistance to noise is a good measure of nonlocality (see also Ref. [26]).

Take the following two-qudit state,

$$
\left| \Psi_ {2} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 0 \right\rangle + \left| 1 1 \right\rangle\right), \tag {11}
$$

where  $d - 2$  of the Schmidt coefficients are zero. Now, consider the CHSH inequality [17]

$$
\left\langle A _ {1} \left(B _ {1} + B _ {2}\right) + A _ {2} \left(B _ {1} - B _ {2}\right) \right\rangle \leqslant 2, \tag {12}
$$

where  $A_{i}$  and  $B_{i}$ ,  $i = 1,2$ , are measurements of two outcomes, labeled by  $+1$  and  $-1$ . The maximum violation of this inequality attained by quantum states is  $2\sqrt{2}$  [27]. The following choice of measurements achieves this maximum for the state (11):

$$
A _ {1} ^ {+ 1} = P _ {0}, \quad A _ {2} ^ {+ 1} = P _ {\pi / 2}, \quad B _ {1} ^ {+ 1} = P _ {- \pi / 4}, \quad B _ {2} ^ {+ 1} = P _ {\pi / 4}, \tag {13}
$$

where  $P_{\omega}$  is the projector onto the state  $1 / \sqrt{2} (|0\rangle +e^{i\omega}|1\rangle)$ , and  $X_{i}^{-1} = 1 - X_{i}^{+1}$ , with  $X = A,B$  and  $i = 1,2$ . Since  $\mathrm{tr}(X_i^{+1})$ $= 1$  and  $\mathrm{tr}(X_i^{-1}) = d - 1$ , the contribution of the maximally mixed noise to Eq. (12) for these settings is not zero. Indeed it is not difficult to see that in this case the resistance to noise for  $|\Psi_2\rangle$  is

$$
\lambda = \frac {1 - \left(\frac {d - 2}{d}\right) ^ {2}}{\sqrt {2} - \left(\frac {d - 2}{d}\right) ^ {2}}, \tag {14}
$$

which tends to zero when  $d \to \infty$ . One can argue that Eq. (11) is not really a two-qudit state, but similar results can be obtained for states of full Schmidt number that are infinitesimally close to it. This example shows that the resistance to noise is not a good measure of nonlocality. Let us briefly explore here other alternative candidates.

The first possibility consists of studying the resistance of entangled states when they are mixed with the state resulting from the tensor product of the reduced density matrices. Then, given an entangled state  $|\Phi \rangle \in \mathcal{C}^d\otimes \mathcal{C}^d$ , we want to determine the minimum value of  $\lambda^\prime$  such that there is no LV model for the state

$$
\rho^ {\prime} = \lambda^ {\prime} | \Phi \rangle \langle \Phi | + (1 - \lambda^ {\prime}) \rho_ {A} \otimes \rho_ {B}, \tag {15}
$$

where  $\rho_{A} \equiv \mathrm{tr}_{B}(|\Phi\rangle \langle \Phi|)$  and similarly for  $B$ . This measure has the advantage of being equal to the resistance to noise for maximally entangled states, and avoids problems as the one previously discussed. A second possibility can be to consider mixtures of the initial entangled states with the closest separable one,  $\sigma_{AB}$ . Similarly as for the relative entropy of entanglement [28], one can choose the relative entropy as a measure of distance,  $S(\rho, \sigma) = \mathrm{tr}(\rho \ln \rho - \rho \ln \sigma)$ . Therefore  $\sigma_{AB}$  is defined as the state minimizing  $S(|\Phi\rangle \langle \Phi|, \sigma)$  over the set of separable states [29]. Now, we look for the minimum  $\lambda''$  such that the state

$$
\rho^ {\prime \prime} = \lambda^ {\prime \prime} | \Phi \rangle \langle \left. \Phi \right| + (1 - \lambda^ {\prime \prime}) \rho_ {A B} \tag {16}
$$

does not admit a LV description. Remarkably, for the states (1) and (9), the settings defined above and the inequality (2), the three numbers for each state coincide, i.e.,  $\lambda_{\min} = \lambda_{\min}' = \lambda_{\min}''$ . Thus, no change is observed by using these alternative measures of nonlocality.

All these reasonings suggest that two von Neumann measurements are not optimal for detecting nonlocality in two-qutrit systems. A possible way out can be that more general measurements [positive operator valued measures (POVM)] are required for having a larger violation for  $|\Psi \rangle$ . It seems more likely that more observables for each party, and a new Bell inequality, are needed. Another interesting scenario consists of the analysis of these quantum correlations under sequences of measurements as in Ref. [26]. Indeed, states (4) are entangled and distillable for  $1 / (N + 1) < \lambda \leqslant 1$  [30]. Finally, it also follows from this result that it is not correct even for pure states to quantify entanglement by means of the violation of a particular Bell inequality [31].

# IV. DISTILLABILITY AND BELL INEQUALITIES

Violation of Bell inequalities is a possible manifestation of nonlocality, but, as it has been discussed in the Introduction, there are other ways of thinking about nonlocality. From the point of view of quantum information it is interesting to know if the correlations in a quantum state are useful, i.e., if the state is distillable. It is usually conjectured that Bell inequality violation implies the distillability of the state [10]. In this section we show that, for the experimental settings seen above, the corresponding entanglement witness is decomposable. This implies that any bound entangled state with positive partial transposition [32] does not violate this inequality. Moreover, from our construction, it can be proven that any state violating the inequality is distillable.

From Eq. (2) it is possible to construct the Bell operator [24],  $B$ , and from it the entanglement witness [11],  $W = 2$

$-B$ , such that  $\mathrm{tr}(\rho_S W) \geqslant 0$  for all separable states  $\rho_S$ , and there exists an entangled state,  $\rho$ , that is detected, i.e.,  $\mathrm{tr}(\rho W) < 0$ . There exists a class of entanglement witnesses, called decomposable,  $W_d$ , that can be written as

$$
W _ {d} = P + Q ^ {T _ {A}}, \tag {17}
$$

where  $P$  and  $Q$  are positive operators, and  $T_{A}$  denotes partial transposition with respect to subsystem  $A$ . Note that these entanglement witnesses are not able to detect entangled states with positive partial transposition, since if  $\rho^{T_A} \geq 0$  we have  $\mathrm{tr}(\rho W) = \mathrm{tr}(\rho P) + \mathrm{tr}(\rho^{T_A} Q) \geq 0$ . Thus, they are not very useful for checking the separability of a given state (see, for instance, Refs. [15,33]), since they do not provide more information than the partial transposition operation. In the following lines we show that the witness coming from Eq. (2) is decomposable.

Our aim is to prove that there exist some positive operators,  $P$  and  $Q$  satisfying Eq. (17). Note that the role of  $Q$  is to detect the entangled state, so we will choose an operator  $Q$  maximizing  $\mathrm{tr}(|\Psi_{mv}\rangle \langle \Psi_{mv}|Q^{T_A}) = \mathrm{tr}(|\Psi_{mv}\rangle \langle \Psi_{mv}|^TA_Q)$ . We will take then  $Q$  proportional to the projector onto the space of negative eigenvalues of  $|\Psi_{mv}\rangle \langle \Psi_{mv}|^T_A$ , the state that gives the maximal violation of the inequality. If we work in the Schmidt basis of this state, it is easy to see that  $Q$  is proportional to the projector onto the antisymmetric space of two qutrits,

$$
P _ {a} = \frac {1}{2} \sum_ {j} \sum_ {k \neq j} (| j k \rangle - | k j \rangle) (\langle j k | - \langle k j |). \tag {18}
$$

Our guess then for the decomposition (17) of  $W$  is

$$
W = P + k P _ {a} ^ {T _ {A}}, \tag {19}
$$

where  $k$  is a positive number to be determined. Now, we look for a value of this constant such that  $P = W - kP_{a}^{T_{A}} \geqslant 0$ , or equivalently, its minimum eigenvalue is positive. In Fig. 1 we have represented the minimum of these eigenvalues as a function of the constant  $k$ . There exists a range of  $k$  where  $P$  is positive, which means that the witness is decomposable (for instance, taking  $k = 1.2$ ).

This decomposition gives us an insight into the nonlocal properties of these states violating the inequality (2) with the optimal settings described above. First, all the states with positive partial transposition do not violate this inequality. Moreover, if a given state  $\rho$  is detected by the corresponding witness,  $\mathrm{tr}(\rho W) < 0$ , it follows that  $\mathrm{tr}(\rho P_a^{T_A}) < 0$ , and since  $P_{a}^{T_{A}} = 1 / 2(1 - d|\Psi \rangle \langle \Psi |)$ , we have

$$
\langle \Psi | \rho | \Psi \rangle > \frac {1}{d}, \tag {20}
$$

which means that the state is distillable [30]. Thus, for these settings, Bell inequality violation implies state distillability [13].

![](images/89ff72283a7ab99179bddfa1c918fe8ab490d66a2939f7d332d85690f1dbb1f3.jpg)  
FIG. 1. Variation of the minimum eigenvalue of  $P$  in Eq. (19) with  $k$ .

It would be nice if the recipe for finding this decomposition was general and if it worked for other choices of the experimental settings, or higher dimension. Unfortunately this is not the case. Indeed we have seen numerically that the same procedure does not work for other settings violating (2), i.e., such that there exists a state that is detected by the corresponding witness or Bell operator. We have also considered higher dimensional systems, with the corresponding Bell inequality (10) and optimal settings. A similar decomposition is found for  $d = 4$  but our method fails for  $d = 5,6$ . Looking at the variation of the Bell operator spectrum (for the optimal settings), when  $d$  increases, we can somehow understand why this procedure does not work anymore. For  $d = 3$ ,  $(d = 4)$ , the maximum eigenvalue of  $B$  is  $\simeq 2.9149$  ( $\simeq 2.9727$ ), while for the maximally entangled state, having the same Schmidt basis, we have  $\simeq 2.8729$  ( $\simeq 2.8962$ ). This may mean that this maximally entangled state is quite close to the region of maximal violation, and then Eq. (20) holds for those states violating the inequality. For higher dimension the difference between these two values increases (3.0517 vs 2.9105 for  $d = 5$ ), what can explain why the decomposition is not possible? Let us mention here that in the case of two-qubits we are able to find  $P$  and  $Q$  for any witness associated to the CHSH inequality following a similar approach [34] (actually, it is a known result that any two-qubit entanglement witness is decomposable [15]). Whether a better generalization of the CHSH inequality exists also satisfying this construction is an interesting open question.

# V. CONCLUDING REMARKS

In this work we analyzed different manifestations of quantum nonlocality in two-qutrit systems. The starting point was the Bell inequality introduced in Refs. [20,21].

First, we observed that the largest violation of the inequality over all possible von Neumann measurements and initial states is not obtained for the maximally entangled state of two qutrits. We also proved that the resistance to noise is not a good measure of nonlocality, and we proposed some simple alternatives. However, even for these measures, the maximal resistance seems not to be given by the maximally entangled state (further research in this direction is needed). Our results suggest that two von Neumann measurements per site do not detect two-qutrit nonlocality in an optimal way. Notice that the results in Table I may imply that indeed two measurements on each side become less efficient for the detection of nonlocality when the dimension increases. It is not excluded that POVMs would give a larger Bell inequality violation for the two-qutrit maximally entangled state. However, it seems more likely that more observables on each side are needed. In this sense, we still lack a good generalization of the CHSH inequality to qutrits.

We also related the violation of this inequality to other manifestations of nonlocality. For the optimal settings, we demonstrated that the corresponding witness is decomposable by explicitly deriving its decomposition (17) in terms of  $P$  and  $Q$ . Moreover, our construction sheds light on the distillability properties of those states violating the inequality. In fact, bound entangled states do not violate the inequality for the optimal settings (see also Ref. [12]).

Our last point is more general and concerns the characterization of nonlocality. As it has been mentioned, the resistance to noise has proven to be an incorrect criterion for the analysis of nonlocality. Is a single number enough for describing all the nonlocal features of quantum states for bipartite systems of dimension greater than qubits, even for the

pure-state case? Or, as it happens for other questions related to entanglement, are more parameters needed?

# ACKNOWLEDGMENTS

We thank Marek Zukowski for many useful comments. A.A. and N.G. acknowledge financial support from the Swiss FNRS and OFES, within the European project EQUIP, and the Swiss NCCR "Quantum Photonics." A.A. also thanks the Spanish MEC and ESF-QIT for funding. J.I.L. acknowledges financial support from CICYT (AEN99-0766), CIRIT (1999SGR-00097), and EQUIP (IST-1999-11053).

# APPENDIX: MAXIMIZATION OF THE BELL INEQUALITY VIOLATION BY ENTANGLED QUTRITS

Consider the situation that was described in Sec. II. Two three-dimensional subsystems  $A$  and  $B$  are prepared in an arbitrary entangled state  $|\Phi \rangle \in \mathcal{C}^3\otimes \mathcal{C}^3$ . Then, the two parties apply a unitary operation on each subsystem with only nonzero terms in the diagonal equal to  $e^{i\phi_a(j)}$  for  $A$  and  $e^{i\varphi_b(j)}$  for  $B$ , with  $j = 0,1,2$  and  $a,b = 1,2$ . The setting of the six phases  $\phi_{a}(j)$  and  $\varphi_{b}(\widetilde{j})$  ( $j = 0,1,2$ ) defines an experimental configuration. Later,  $A$  carries out a discrete Fourier transform,  $U_{\mathrm{FT}}$ , and  $B$  applies  $U_{\mathrm{FT}}^*$ . Finally, at the output of such devices, the states are detected in the local bases  $|k_A\rangle$  and

$\left|l_{B}\right\rangle$  . When the state is prepared initially in the pure state  $\left|\Phi \right\rangle = \sum_{j,\tilde{j} = 0}^{2}\alpha_{j,\tilde{j}}|j\tilde{j}\rangle$  the probability of a joint detection in the  $k$  th detector in  $A$  and in the  $l$  th detector in  $B$  is equal to

$$
P (k, l) = \frac {1}{9} \left| \sum_ {j, j = 0} ^ {2} \exp \left[ i \left(\phi_ {a} (j) + \varphi_ {b} (\tilde {j}) + (j k - \tilde {j} l) \frac {2 \pi}{2}\right) \right] \alpha_ {j, \tilde {j}} \right| ^ {2}. \tag {A1}
$$

It was shown in Ref. [23] by numerical methods that when the state is maximally entangled [Eq. (1)], the maximal resistance of nonlocality against noise, when all the possible phases  $\phi_{a}(j),\varphi_{b}(j)$  are considered (with  $a,b = 1,2$  and  $j = 0,1,2$ ) corresponds to the optimal phase settings (3).

Let us now consider the associated Bell inequality (2). When Eq. (3) is satisfied and we let vary the state  $|\Phi \rangle \in \mathcal{C}^3 \otimes \mathcal{C}^3$ , the violation of this inequality is maximal when the state  $|\Phi \rangle$  is, up to normalization,  $|00\rangle + \gamma |11\rangle + |22\rangle$ , with  $\gamma = (\sqrt{11} - \sqrt{3}) / 2 \simeq 0.7923$ . The violation is equal to 1 +  $\sqrt{11/3} \approx 2.91485$ .

Indeed, take the general state  $|\Phi \rangle = \Sigma_{j,\tilde{j} = 0}^{2}\alpha_{j,\tilde{j}}|j\tilde{j}\rangle$  (where  $\Sigma_{j,\tilde{j} = 0}^{2}|\alpha_{j,\tilde{j}}|^{2} = 1$  by normalization). Then, Eq. (2) can be rewritten as follows:

$$
\begin{array}{l} I _ {3} (| \Phi \rangle) = \frac {1}{9} \sum_ {j, \tilde {j}, m, \tilde {m} = 0} ^ {2} \alpha_ {m, \tilde {m}} ^ {*} \alpha_ {j, \tilde {j}} \sum_ {k = 0} ^ {2} \exp \left\{i \frac {2 \pi}{3} [ k (j - m) - k (\tilde {j} - \tilde {m}) ] \right\} \left\{\exp \left\{i [ \phi_ {1} (j) - \phi_ {1} (m) + \varphi_ {1} (\tilde {j}) - \varphi_ {1} (\tilde {m}) ] \right\} \right. \\ \times \left[ 1 - \exp \left(- i \frac {2 \pi}{3} (j - m)\right) \right] + \exp \left\{i \left[ \phi_ {2} (j) - \phi_ {2} (m) + \varphi_ {1} (\tilde {j}) - \varphi_ {1} (\tilde {m}) \right] \right\} \left[ \exp \left(- i \frac {2 \pi}{3} (\tilde {j} - \tilde {m}) - 1 \right. \right] \\ + \exp \left\{i \left[ \phi_ {2} (j) - \phi_ {2} (m) + \varphi_ {2} (\tilde {j}) - \varphi_ {2} (\tilde {m}) \right] \right\} \left[ 1 - \exp \left(- i \frac {2 \pi}{3} (j - m)\right) \right] \\ + \exp \left\{\left[ \phi_ {1} (j) - \phi_ {1} (m) + \varphi_ {2} (\tilde {j}) - \varphi_ {2} (\tilde {m}) \right] \right\} \left[ 1 - \exp \left(i \frac {2 \pi}{3} (\tilde {j} - \tilde {m}) \right] \right\}. \tag {A2} \\ \end{array}
$$

$I_{3}(|\Phi \rangle)$  can be expressed as  $\langle \Phi |B|\Phi \rangle$  where  $B$  is the (selfadjoint) Bell operator. The maximal value of  $I_{3}$  is thus reached when  $|\Phi \rangle$  is the eigenstate associated with the maximal eigenvalue of  $B$ ,  $|\Psi_{mv}\rangle$ . We must now determine what this eigenvalue is. The problem is considerably simplified if we note that  $\Sigma_{k = 0}^{2}\exp (i2\pi /3k(p - q) = 3\delta_{pq}^{(3)}$ , where  $\delta_{pq}^{(3)} = 1$  when  $p = q$  modulo 3 and 0 otherwise. This means that  $B$  can be decomposed into the sum of three operators that are decoupled and act individually inside the subspaces spanned by the vectors  $\{|00\rangle |11\rangle ,|22\rangle \}$ ,  $\{|01\rangle ,|12\rangle ,|20\rangle \}$ , and  $\{|02\rangle ,|10\rangle ,|21\rangle \}$ , respectively. Inside the subspace spanned by the vectors  $\{|00\rangle ,|11\rangle ,|22\rangle \}$ ,  $j - m = \tilde{j} -\tilde{m}$  and the reduced Bell operator obeys the following equation:

$$
\begin{array}{l} \left(B ^ {\text {r e d} 1}\right) _ {m j} = \frac {2}{3} \left\{\exp \left(i \frac {2 \pi}{3} \frac {(j - m)}{4}\right) - \exp \left(\frac {2 \pi}{3} \frac {(- 2) (j - m)}{4}\right) \right. \\ + \exp \left(i \frac {2 \pi}{3} \frac {(- 1) (j - m)}{4}\right) \\ - \exp \left(i \frac {2 \pi}{3} \frac {3 (j - m)}{4}\right), \tag {A3} \\ \end{array}
$$

and in matricial notation,

$$
B ^ {\mathrm {r e d 1}} = \frac {2}{3} \left( \begin{array}{c c c} 0 & \sqrt {3} & 3 \\ \sqrt {3} & 0 & \sqrt {3} \\ 3 & \sqrt {3} & 0 \end{array} \right). \tag {A4}
$$

Inside the two other subspaces, we obtain in a similar fashion the following expression for the reduced Bell operator:

$$
B ^ {\text {r e d} 2} = B ^ {\text {r e d} 3} = \frac {2}{3} \left( \begin{array}{c c c} 0 & \sqrt {3} & 0 \\ \sqrt {3} & 0 & 0 \\ 0 & 0 & 0 \end{array} \right). \tag {A5}
$$

The problem consists now of determining the maximal eigenvalues of these  $3 \times 3$  matrices. One can check directly that in this matrical notation  $|\Psi\rangle$  is not an eigenstate of  $B^{\mathrm{red1}}$  so that it does not certainly maximize the violation of the Bell inequality. The eigenvalues of  $B^{\mathrm{red1}}$  are equal to  $-2, 1 - \sqrt{11/3}$ , and  $1 + \sqrt{11/3}$  while for  $B^{\mathrm{red2,3}}$  we have  $-2/\sqrt{3}, 0$ , and  $2/\sqrt{3}$ , so that the maximal violation is equal to  $1 + \sqrt{11/3} \approx 2.91485$ . It is easy to check that the corresponding eigenvector is, up to normalization,  $|00\rangle + |\gamma|11\rangle + |22\rangle$ , with  $\gamma = (\sqrt{11} - \sqrt{3})/2 \simeq 0.7923$ .

Note that at first sight it could seem strange that the maximally entangled state does not maximize the violation of the inequality (2), because it seems that the states  $|00\rangle$ ,  $|11\rangle$ , and  $|22\rangle$  are indistinguishable in our approach. The discrete Fourier transforms are well known for their cyclic properties, and in this inequality all the detectors are treated on an equal footing (the Bell operator contains cyclic summations of probabilities of coincident firings). Nevertheless, if we consider Eq. (A2), we can notice that the matrix coefficient  $\langle m\tilde{m}|B|j\tilde{j}\rangle$  contains expressions of the type  $\exp \{i[\phi_a(j) - \phi_a(m) + \varphi_b(\tilde{j}) - \varphi_b(\tilde{m})]\}$  where  $\phi_{a}(j)$  and  $\varphi_{b}(\tilde{j})$  are locally adjustable phases. Due to the presence of factors of this type, the cyclic invariance is broken (in the sense that when  $j - m = j' - m'$  modulo 3 and  $\tilde{j} - \tilde{m} = \tilde{j}' - \tilde{m}'$  modulo 3, it is not necessarily true that  $\langle m\tilde{m}|B|j\tilde{j}\rangle = \langle m'\tilde{m}'|B|j'\tilde{j}'\rangle$ ). Note that when the phase settings are optimal, they depend linearly on the indices  $j, m, \tilde{j}, \tilde{m}$  according to Eq. (3) and  $\langle m\tilde{m}|B|j|\tilde{j}\rangle$  depends on  $j, m, \tilde{j}, \tilde{m}$  only through the combi

nations  $j - m$  and  $\widetilde{j} -\widetilde{m}$ . Thus, the matrix coefficients  $\langle m\widetilde{m}|B|j\widetilde{j}\rangle$  and  $\langle (m + \delta)(\widetilde{m} +\widetilde{\delta})|B|(j + \delta)(\widetilde{j} +\widetilde{\delta})\rangle$  are equal. This explains why  $B^{\mathrm{red2}} = B^{\mathrm{red3}}$  and also why the states  $|00\rangle$  and  $|22\rangle$  appear symmetrically in the matrix  $B^{\mathrm{red1}}$ . Nevertheless, the cyclic invariance is still broken (in the sense made precise above), which explains why  $B^{\mathrm{red1}}$  is singularized relatively to  $B^{\mathrm{red2}}$  and  $B^{\mathrm{red3}}$ , as  $|11\rangle$  relatively to  $|00\rangle$  and  $|22\rangle$ .

Finally, we prove that we must not expect a larger violation of the inequality (2) if we modify the phase settings defined in Eq. (3). Indeed, let us vary  $\vec{\phi}_1$ , keeping the other phases fixed,

$$
\phi_ {1} (0) = 0, \quad \phi_ {1} (1) = \alpha , \quad \phi_ {1} (2) = \beta ,
$$

$$
\phi_ {2} (j) = \frac {\pi}{3} j, \quad \varphi_ {1} (j) = \frac {\pi}{6} j, \quad \varphi_ {2} (j) = - \frac {\pi}{6} j. \tag {A6}
$$

Then,

$$
\begin{array}{l} B _ {\text {v a r i e d}} ^ {\text {r e d}} = \frac {1}{3} \left( \begin{array}{c c c} 0 & \sqrt {3} & 3 \\ \sqrt {3} & 0 & \sqrt {3} \\ 3 & \sqrt {3} & 0 \end{array} \right) \\ + \frac {1}{3} \left( \begin{array}{c c c} 0 & \sqrt {3} e ^ {i \alpha} & 3 e ^ {i \beta} \\ \sqrt {3} e ^ {- i \alpha} & 0 & \sqrt {3} e ^ {i (\beta - \alpha)} \\ 3 e ^ {- i \beta} & \sqrt {3} e ^ {i (\alpha - \beta)} & 0 \end{array} \right). \tag {A7} \\ \end{array}
$$

It is easy to check that the two matrices that appear in Eq. (A7) have the same eigenvalue equation and thus the same spectrum, which is  $-1$ ,  $(1 - \sqrt{11 / 3}) / 2$ , and  $(1 + \sqrt{11 / 3}) / 2$ . The maximal eigenvalue of these matrices is also equal to their norm in the present case, so that the norm of  $B_{\mathrm{varied}}^{\mathrm{redI}}$ , and thus its maximal eigenvalue, is certainly not larger than  $1 + \sqrt{11 / 3}$ . Entirely similar results can be obtained when  $\vec{\phi}_2$ ,  $\vec{\varphi}_1$ , or  $\vec{\varphi}_2$  are varied. This proves that the phase settings defined in Eq. (3) maximize locally (in the space of all possible phase settings) the violation of the Bell inequality (2).

[1] J. S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964).  
[2] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[3] Take a composite system of  $N$  particles,  $\mathcal{C}^{d_1}\otimes \mathcal{C}^{d_2}\otimes \dots \otimes \mathcal{C}^{d_N}$  where  $d_{i}$  is the dimension of the local space of party  $i$ . A pure state,  $|\Phi \rangle$ , belonging to the global space, is said to be separable when it can be written as a tensor product of pure states in each subsystem, i.e.,  $|\Phi \rangle = |\psi_1\rangle \otimes |\psi_2\rangle \otimes \dots \otimes |\psi_N\rangle$ . This definition is easily extended to mixed states, and a density matrix  $\rho$  is separable when it can be expressed as a convex sum of projectors into separable pure states, i.e.,  $\rho = \Sigma_i p_i|\Psi^s\rangle\langle\Psi^s|$ , where  $|\Psi^s\rangle$  are separable. Physically, separable states are those that the different parties can prepare if they are allowed to use only local operations in each local system and to communicate

classically. States that are not separable are called entangled.  
[4] N. Gisin, Phys. Lett. A 154, 201 (1991).  
[5] S. Popescu and D. Rohrlich, Phys. Lett. A 166, 293 (1992).  
[6] R. F. Werner, Phys. Rev. A 40, 4277 (1989).  
[7] S. Popescu, Phys. Rev. Lett. 74, 2619 (1995).  
[8] C. H. Bennett, H. J. Bernstein, S. Popescu, and B. Schumacher, Phys. Rev. A 53, 2046 (1996).  
[9] C. H. Bennett, D. P. Di Vincenzo, J. A. Smolin, and W. K. Wootters, Phys. Rev. A 54, 3824 (1996); S. Popescu and D. Rohrlich, ibid. 56, R3319 (1997); G. Vidal, J. Mod. Opt. 47, 355 (2000).  
[10] A. Peres, Found. Phys. 29, 589 (1999); R. F. Werner and M. M. Wolf, Phys. Rev. A 61, 062102 (2000); W. Dür, Phys. Rev. Lett. 87, 230402 (2001); A. Acín, ibid. 88, 027901 (2002).

[11] B. Terhal, Phys. Lett. A 271, 319 (2000).  
[12] D. Kaszlikowski, M. Zukowski, and P. Gnacinski, Phys. Rev. A 65, 032107 (2002).  
[13] A. Acín and V. Scarani, e-print quant-ph/0112102.  
[14] A. Peres, Phys. Rev. Lett. 77, 1413 (1996).  
[15] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 223, 1 (1996).  
[16] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Rev. Lett. 78, 574 (1997).  
[17] J. F. Clause, M. A. Horne, A. Shimony, and R. A. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[18] A. Fine, Phys. Rev. Lett. 48, 291 (1982).  
[19] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 200, 340 (1995).  
[20] D. Collins, N. Gisin, N. Linden, S. Massar, and S. Popescu, Phys. Rev. Lett. 88, 040404 (2002).  
[21] D. Kaszlikowski, L. C. Kwek, J. L. Chen, M. Zukowski, and C. H. Oh, Phys. Rev. A 65, 032118 (2002).  
[22] The matrix elements of the Fourier transform in  $\mathcal{C}^d$  are given by  $(U_{\mathrm{FT}})_{jk} = \exp [(j - 1)(k - 1)2\pi /d]$ .  
[23] D. Kaszlikowski, P. Gnacinski, M. Zukowski, W. Miklaszewski, and A. Zeilinger, Phys. Rev. Lett. 85, 4418 (2000); T.

Durt, D. Kaszlikowski, and M. Zukowski, e-print quant-ph/0101084.  
[24] S. L. Braunstein, A. Mann, and M. Revzen, Phys. Rev. Lett. 68, 3259 (1992).  
[25] M. Zukowski, A. Zeilinger, and M. A. Horne, Phys. Rev. A 55, 2564 (1997).  
[26] D. Collins and S. Popescu, e-print quant-ph/0106156.  
[27] B. S. Cirel'son, Lett. Math. Phys. 4, 93 (1980).  
[28] V. Vedral, M. B. Plenio, M. A. Rippin, and P. L. Knight, Phys. Rev. Lett. 78, 2275 (1997); V. Vedral and M. B. Plenio, Phys. Rev. A 57, 1619 (1998).  
[29] Note that for the case in which the entangled state is pure, the expression for the closest separable state is known [28].  
[30] M. Horodecki and P. Horodecki, Phys. Rev. A 59, 4206 (1999).  
[31] W. J. Munro, K. Nemoto, and A. G. White, J. Mod. Opt. 48, 1239 (2001).  
[32] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Rev. Lett. 80, 5239 (1998); P. Horodecki, Phys. Lett. A 232, 333 (1997).  
[33] M. Lewenstein, B. Kraus, J. I. Cirac, and P. Horodecki, Phys. Rev. A 62, 052310 (2000).  
[34] A. Acin, J. I. Latorre, and P. Pascual (unpublished).