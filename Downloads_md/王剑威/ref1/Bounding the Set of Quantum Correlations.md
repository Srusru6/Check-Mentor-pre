# Bounding the Set of Quantum Correlations

Miguel Navascués,* Stefano Pironio,† and Antonio Acín‡

ICFO-Institut de Ciencies Fotoniques, Mediterranean Technology Park, 08860 Castelldefels (Barcelona), Spain (Received 18 July 2006; published 4 January 2007)

We introduce a hierarchy of conditions necessarily satisfied by any distribution  $P_{\alpha \beta}$  representing the probabilities for two separate observers to obtain outcomes  $\alpha$  and  $\beta$  when making local measurements on a shared quantum state. Each condition in this hierarchy is formulated as a semidefinite program. Among other applications, our approach can be used to obtain upper bounds on the quantum violation of an arbitrary Bell inequality. It yields, for instance, tight bounds for the violations of the Collins et al. inequalities.

DOI: 10.1103/PhysRevLett.98.010401

PACS numbers: 03.65.Ud, 03.67.-a

The correlations between two separated physical systems can be characterized by the joint probabilities  $P_{\alpha \beta}$  that an observer who performs a measurement  $X$  on the first system gets an outcome  $\alpha \in X$  and that an observer making a measurement  $Y$  on the second system gets an outcome  $\beta \in Y$ . If the observed system is in an entangled state, these joint probabilities may violate a Bell inequality, implying that quantum theory is not, in Bell's terminology, locally causal [1]. Although quantum correlations are not constrained by Bell's locality principle, they are not arbitrary, since a general joint distribution  $P_{\alpha \beta}$  cannot always be viewed as originating from measurements performed on a shared quantum system [2].

In this Letter, we investigate the restrictions on bipartite correlations imposed by the quantum formalism. The question that we seek to answer is the following: Given an arbitrary distribution  $P_{\alpha \beta}$ , do there exist a quantum state  $\rho$  on a joint Hilbert space  $\mathcal{H}_A \otimes \mathcal{H}_B$  and local measurement operators  $E_{\alpha} = \tilde{E}_{\alpha} \otimes I$  and  $E_{\beta} = I \otimes \tilde{E}_{\beta}$ , such that  $P_{\alpha \beta} = \mathrm{Tr}(E_{\alpha}E_{\beta}\rho)$ ?

From a fundamental point of view, one motivation for studying this problem is simply to understand which correlations can arise between two systems within our current description of nature. Another is to develop tools to detect the possible nonquantumness of some set of empirically observed correlations. Answering the above question is also of practical interest for various applications in quantum science, for instance, for the design of nonlocality tests more resistant to experimental noise and detector inefficiencies. In general, characterizing the set of quantum correlations is essential to understand better the extent to which quantum mechanics is useful in information processing tasks such as communication complexity [3] and key distribution [4,5]. An usual problem in these contexts is to determine what is the maximal violation of a Bell inequality allowed by quantum mechanics.

Answering the above question is in general a difficult task; the simple strategy of searching over all quantum states  $\rho$  and measurement operators  $E_{\mu}$ , which in principle can be of arbitrary dimension, is clearly unfeasible. The first to tackle this problem was Tsirelson [6], who derived

the maximal quantum violation for the Clauser-Horne-Shimony-Holt (CHSH) inequality [7]. Following his seminal work, many attempts have been made to understand better how the quantum formalism constrains the correlations between two parties [8], but most of the obtained results only apply to a restricted set of situations or lack an efficient generalization. Among these, we mention the works of Landau [9] and Wehner [10] who realized that the problem of deciding if a set of "correlation functions" obtained from measurements with binary outcomes admits a quantum representation can be cast as a semidefinite program (SDP). Their approach is interesting in that semidefinite programs are convex optimization problems for which powerful computational and theoretical methods have been developed [11].

We show here how to design criteria that distinguish correlations that can be reproduced through local measurements on a quantum state from those which cannot. Testing any one of these criteria amounts to solve a SDP. Contrary to previous constructions, our method can be applied to any distribution  $P_{\alpha \beta}$  of joint probabilities, corresponding to a configuration with an arbitrary number of measurement choices and outcomes. Seen as a whole, the tests that we introduce exhibit a hierarchical structure, in the sense that they can be organized as a sequence of conditions, each condition in the sequence being stronger than the preceding one. As an illustration of the effectiveness of our approach, we present two applications of it. First, we derive a nonlinear inequality satisfied by quantum mechanics which strengthens a previous inequality due to Tsirelson [12], Landau [9], and Masanes [13]. As a second application, we give a tight bound for the violation of the Collins et al. inequalities [14].

Preliminaries.-Before entering in the details of our construction, let us first give some definitions and state the assumptions made through this Letter. We assume that the two parties, Alice and Bob, choose their measurements from a finite set of possibilities, and that each measurement may yield one out of a finite set of outcomes. Note that we think of outcomes corresponding to different measurements as being labeled distinctly, so that each outcome  $\alpha$

of Alice (or  $\beta$  of Bob) is unambiguously associated to a unique measurement  $X$  (or  $Y$ ).

Refining the statement made earlier, we say that a distribution  $P_{\alpha \beta}$  admits a quantum representation if there exist a joint quantum state  $\rho$  on  $\mathcal{H}_A\otimes \mathcal{H}_B$ , a set of projection operators  $E_{\alpha} = \tilde{E}_{\alpha}\otimes I$  acting on Alice's system and a set of projection operators  $E_{\beta} = I\otimes \tilde{E}_{\beta}$  acting on Bob's system, such that

$$
P _ {\alpha \beta} = \operatorname {T r} \left(E _ {\alpha} E _ {\beta} \rho\right). \tag {1}
$$

Projectors corresponding to outcomes belonging to the same measurement  $M$  should (i) be orthogonal:  $E_{\mu}E_{\nu} = 0$  for  $\mu, \nu \in M, \mu \neq \nu$ , and (ii) sum to the identity:  $\sum_{\mu \in M} E_{\mu} = I$ . By definition, we also have that (iii)  $E_{\mu}^{2} = E_{\mu}^{\dagger} = E_{\mu}$  and that (iv) the projectors on Alice and Bob's side commute with each other:  $[E_{\alpha}, E_{\beta}] = 0$ .

Note that the most general description of a quantum measurement corresponds to a positive operator valued measure (POVM) rather than a set of projection operators. But since a POVM can be viewed as a projective measurement on a system of larger dimension, and since we do not impose any constraints on the dimension of the Hilbert space  $\mathcal{H}_A\otimes \mathcal{H}_B$ , no generality is lost with our definition.

Necessary conditions for quantum probabilities. We now introduce a family of conditions satisfied by any quantum distribution  $P_{\alpha \beta}$ . We thus start by assuming that there is a quantum state  $\rho$  and a set  $\{E_{\mu}\}$  of projection operators satisfying Eq. (1) and properties (i)-(iv), and seek new implications from these assumptions.

By taking products of the operators  $E_{\mu}$  and linear combinations of such products, we can define new operators, for instance  $E_{\alpha}E_{\beta}E_{\alpha'}$  or  $\sum_{\alpha}c_{\alpha}E_{\alpha}$  (note that these new operators are not necessarily projection operators anymore, nor even Hermitian operators). Let  $S = \{S_1,\ldots ,S_n\}$  be a set of  $n$  such operators. Associate to the set  $S$  a  $n\times n$  matrix  $\Gamma$  through

$$
\Gamma_ {i j} = \operatorname {T r} \left(S _ {i} ^ {\dagger} S _ {j} \rho\right). \tag {2}
$$

By construction, the matrix  $\Gamma$  is Hermitian, it satisfies the linear identities

$$
\sum_ {i, j} c _ {i j} \Gamma_ {i j} = 0 \quad \text {i f} \sum_ {i, j} c _ {i j} S _ {i} ^ {\dagger} S _ {j} = 0, \tag {3}
$$

$$
\sum_ {i, j} c _ {i j} \Gamma_ {i j} = \sum_ {\alpha , \beta} d _ {\alpha \beta} P _ {\alpha \beta} \quad \text {i f} \sum_ {i, j} c _ {i j} S _ {i} ^ {\dagger} S _ {j} = \sum_ {\alpha , \beta} d _ {\alpha , \beta} E _ {\alpha} E _ {\beta}, \tag {4}
$$

and it is positive semidefinite,

$$
\Gamma \succeq 0. \tag {5}
$$

The linear constraints (3) directly follow from the linearity of the trace in (2). The important point is that they partly reflect the properties (i)-(iv) satisfied by the operators  $E_{\mu}$ . For instance, suppose that  $S$  contains an operator  $S_{j} = E_{\mu}$  and a subset of operators  $\{S_{k} \mid k \in \mathcal{K}\} = \{E_{\mu}E_{\nu} \mid \nu \in$

$M\}$  for some measurement  $M$ . Then, property (ii) implies  $\sum_{k\in \mathcal{K}}S_k = \sum_{\nu \in M}E_\mu E_\nu = E_\mu = S_j$  and thus  $\sum_{k\in \mathcal{K}}\Gamma_{ik} = \Gamma_{ij}$ . As another example, suppose that  $S_i = E_\alpha$  and  $S_j = E_\beta E_{\alpha'}$  with  $\alpha, \alpha' \in X$ , and  $\alpha \neq \alpha'$ . Then, using successively properties (iii), (iv), and (i), we find  $S_i^\dagger S_j = E_\alpha E_\beta E_{\alpha'} = E_\alpha E_{\alpha'}E_\beta = 0$ , and thus  $\Gamma_{ij} = 0$ . The conditions (4) are obtained by making use of (1) in (2) and relate the entries of the matrix  $\Gamma$  to the specific set of probabilities  $P_{\alpha\beta}$  under consideration. Finally, to establish (5), remember that an  $n \times n$  matrix  $\Gamma$  is semidefinite positive if and only if  $\nu^\dagger \Gamma \nu \geq 0$  for all  $\nu \in \mathbb{C}^n$ . Expanding this expression, we get

$$
\begin{array}{l} v ^ {\dagger} \Gamma v = \sum_ {i, j} v _ {i} ^ {*} \operatorname {T r} \left(S _ {i} ^ {\dagger} S _ {j} \rho\right) v _ {j} \\ = \operatorname {T r} \left[ \left(\sum_ {i} v _ {i} S _ {i}\right) ^ {\dagger} \left(\sum_ {j} v _ {j} S _ {j}\right) \rho \right] \\ \geq 0, \tag {6} \\ \end{array}
$$

since  $\rho$  is a positive operator.

We thus just showed that for any quantum distribution  $P_{\alpha \beta}$ , there necessarily exists for each set  $S$  a matrix  $\Gamma$  satisfying the linear constraints (3) and (4) and the condition of positivity (5). If for some  $S$  it is not possible to find a matrix  $\Gamma$  satisfying these properties, we can therefore conclude that the correlations characterized by the distribution  $P_{\alpha \beta}$  cannot be reproduced through local measurements on a quantum state. Determining if there exists a matrix  $\Gamma$  satisfying conditions (3)-(5) amounts to finding a positive semidefinite matrix satisfying a set of linear constraints and is a typical instance of semidefinite programming (see [11] for a review of SDP). All the techniques developed in this context can thus be applied to evaluate our conditions.

To give a concrete example of our method, consider the case where  $S = \{E_{\alpha}\} \cup \{E_{\beta}\}$  is simply the set of projectors of Alice and Bob. Suppose that there are  $m$  different measurement outcomes  $\alpha = 1, \ldots, m$  for Alice and  $m$  different outcomes  $\beta = m + 1, \ldots, 2m$  for Bob. Then  $S = \{E_1, \ldots, E_m, E_{m + 1}, \ldots, E_{2m}\}$  and applying the construction defined by (2), we find that  $\Gamma$  is a  $2m \times 2m$  matrix of the form

$$
\Gamma = \left( \begin{array}{c c} Q & P \\ P ^ {T} & R \end{array} \right), \tag {7}
$$

where the submatrix  $P$  is simply the  $m \times m$  table of probabilities with entries  $P_{\alpha \beta}$ , and the submatrices  $Q$  and  $R$  satisfy

$$
Q _ {\alpha \alpha} = P _ {\alpha}, \quad Q _ {\alpha \alpha^ {\prime}} = 0 \quad (\alpha , \alpha^ {\prime} \in X \text {a n d} \alpha \neq \alpha^ {\prime}),
$$

$$
R _ {\beta \beta} = P _ {\beta}, \qquad R _ {\beta \beta^ {\prime}} = 0 \qquad (\beta , \beta^ {\prime} \in Y \text {a n d} \beta \neq \beta^ {\prime}),
$$

where  $P_{\alpha} = \sum_{\beta \in Y} P_{\alpha \beta}$  and  $P_{\beta} = \sum_{\alpha \in X} P_{\alpha \beta}$  are the marginal probabilities for Alice and Bob, respectively. The form of the matrix (7) is defined by the linear constraints

(3) and (4). The only entries of  $\Gamma$  which are not determined by these constraints are the entries  $Q_{\alpha \alpha'}$  with  $\alpha \in X$  and  $\alpha' \in X'$  belonging to different measurements of Alice  $(X \neq X')$ , and the entries  $R_{\beta \beta'}$  with  $\beta \in Y$  and  $\beta' \in Y'$  belonging to different measurements of Bob  $(Y \neq Y')$ . In a quantum scenario, these entries would correspond to noncommuting measurements performed on each subsystem and would thus be unobservable. Nonetheless, if the correlations  $P_{\alpha \beta}$  have a quantum origin it is possible to assign values to these undetermined entries such that the overall matrix (7) is positive semidefinite, in accordance with (5). As mentioned earlier, semidefinite programming can be used to determine if the matrix (7) can be completed in such a way.

A hierarchy of conditions. We have shown how to design tests that distinguish quantum from nonquantum correlations. Each set  $S$  of operators used in our construction yields a different condition, and the choice of a particular  $S$  may thus seem arbitrary. But in fact not all conditions built according to our instructions are independent. Moreover, they can be organized in a hierarchical structure, such that they can all be checked in a systematic way.

To see this point, first note the easily established fact that if every operator in a set  $S$  can be written as a linear combination of operators in another set  $S'$ , then the conditions obtained from  $S'$  are at least as constraining as the one obtained from  $S$ . By this we mean that if there exists a matrix  $\Gamma'$  satisfying the constraints (3)-(5) associated to  $S'$ , then there also exists a matrix  $\Gamma$  satisfying the corresponding constraints associated to  $S$ . The second observation is that the set  $\mathcal{T}_m = \{E_{\mu_1} \ldots E_{\mu_m}\}$  of all possible products of  $m$  projectors generates by linear combinations all the operators that are linear combinations of products of  $m'$  projectors, with  $m' \leq m$ .

Using these two properties, it is possible to remove the apparent arbitrariness on the choice of the set  $S$ , and check all the conditions that can be built using our method in a comprehensive way. Start first with the condition based on the set  $\mathcal{T}_1 = \{E_\alpha\} \cup \{E_\beta\}$ , which consists only of the projectors of Alice and Bob, and which we denote shortly as  $\mathcal{T}_1 = \{E_\mu\}$ . If this condition is satisfied, consider the bigger set  $\mathcal{T}_2 = \{E_\mu E_\nu\}$  consisting of all products of two projectors. If the corresponding test is passed, move to  $\mathcal{T}_3 = \{E_\mu E_\nu E_\tau\}$ , and so on. Since the elements of  $\mathcal{T}_{n-1}$  can be generated by linear combinations of the elements of  $\mathcal{T}_n$ , each successive test is at least as good as the previous ones. The sets  $\mathcal{T}_n$  then define a hierarchy of necessary conditions for testing the quantum origin of  $P_{\alpha\beta}$ . Note that if a test fails at some point in this hierarchy, we can immediately conclude that the correlations under consideration are not quantum and there is no need to proceed with the successive tests. The condition based on the matrix (7) corresponds to the first test in this infinite hierarchy. As an illustration, we now present two applications of our method.

Application 1.-The first example involves two measurements for Alice,  $X = 1$ , 2, and two for Bob,  $Y = 3$ , 4, where each measurement yields one out of two outcomes,  $+1$  or  $-1$ . This situation is thus characterized by 16 probabilities  $P_{(\pm X)(\pm Y)}$ , to which we can associate eight projectors  $E_{\pm M}$  ( $M = 1, \ldots, 4$ ). Alternatively, one can characterize this scenario by specifying the correlation functions  $C_{XY} = \sum_{a,b} ab P_{(aX)(bY)}$  and the marginal quantities  $C_X = \sum_{a} a P_{aX}$  and  $C_Y = \sum_{b} b P_{bY}$  for each measurement. The first test in the hierarchy corresponds to the set  $\mathcal{T}_1 = \{E_{\pm 1}, \ldots, E_{\pm 4}\}$ , or, equivalently, to the set  $\mathcal{S} = \{I, \sigma_1, \ldots, \sigma_4\}$ , where  $\sigma_M = E_{+M} - E_{-M}$ , which is linearly equivalent to  $\mathcal{T}_1$ . The corresponding  $5 \times 5$  matrix  $\Gamma$  is

$$
\Gamma = \left( \begin{array}{c c c c c} 1 & C _ {1} & C _ {2} & C _ {3} & C _ {4} \\ & 1 & u & C _ {1 3} & C _ {1 4} \\ & & 1 & C _ {2 3} & C _ {2 4} \\ & & & 1 & v \\ & & & & 1 \end{array} \right), \tag {8}
$$

where we have only given the upper triangular part of  $\Gamma$  since it is Hermitian. The parameters  $u, v$  correspond to entries that are not determined by our construction; but if the correlations represented by the quantities  $\{C_X, C_Y, C_{XY}\}$  are quantum, it is possible to find values for  $u$  and  $v$  such that the matrix (8) is semidefinite positive.

Note that a necessary condition for the matrix (8) to be semidefinite positive is that the bottom-right  $4 \times 4$  submatrix satisfies

$$
\bar {\Gamma} = \left( \begin{array}{c c c c} 1 & u & C _ {1 3} & C _ {1 4} \\ & 1 & C _ {2 3} & C _ {2 4} \\ & & 1 & v \\ & & & 1 \end{array} \right) \succeq 0. \tag {9}
$$

This condition for the correlation functions  $C_{XY}$  was already introduced by Landau [9] and Wehner [10]. It is shown in [9] that there are values  $u$  and  $v$  such that (9) holds if and only if the correlations  $C_{XY}$  satisfy the inequality

$$
\left| \operatorname {a s i n} C _ {1 3} + \operatorname {a s i n} C _ {1 4} + \operatorname {a s i n} C _ {2 3} - \operatorname {a s i n} C _ {2 4} \right| \leq \pi , \tag {10}
$$

and the three other ones obtained by permutation of the measurements. These inequalities have also been derived from a different perspective by Tsirelson [12] and Masanes [13].

The correlation functions  $C_{XY}$ , however, only provide partial information about the full probability distribution. Our construction (8), on the other hand, deals with the full probability distribution, including the marginals  $C_X$  and  $C_Y$ . Using the same techniques as used in [9] to derive (10) from (9), it can be shown that the condition that the matrix (8) is semidefinite positive is equivalent to the inequality

$$
\left| \operatorname {a s i n} D _ {1 3} + \operatorname {a s i n} D _ {1 4} + \operatorname {a s i n} D _ {2 3} - \operatorname {a s i n} D _ {2 4} \right| \leq \pi , \tag {11}
$$

where  $D_{ij} = (C_{ij} - C_iC_j) / \sqrt{(1 - C_i^2)(1 - C_j^2)}$ , and to the inequalities obtained from (11) by permutation of the

measurement choices. If we neglect the marginals by imposing  $C_M = 0$  we recover (10). As a test on the full distribution, however, our inequality is stronger than (10) since there are probability distributions that satisfy (10) but which violate (11). Yet, (11) is not a sufficient condition for a full probability distribution to admit a quantum representation, as we have examples of correlations that satisfy (11) but which fail the successive step in the hierarchy.

Application 2.—By maximizing the violation of a Bell inequality over the set of probability distributions satisfying one of our conditions, we obtain an upper bound on the violation of this inequality by quantum mechanics (since such conditions are satisfied by every quantum distributions). A Bell inequality is a linear combination of the probabilities  $P_{\alpha \beta}$ , and since these probabilities are related in a linear way to the entries of the matrices  $\Gamma$ , obtaining such an upper-bound can be cast as a SDP. Let us stress that this bound is an upper bound on the global maximum of the inequality since we do not suppose anything about the measurements and states except that they are quantum.

As an example, consider the CHSH inequality, which reads  $C_{13} + C_{14} + C_{23} - C_{24} \leq 2$ . Maximizing this expression over all distribution satisfying the criterion (9) presented in application 1 corresponds to the SDP,

maximize  $C_{13} + C_{14} + C_{23} - C_{24}$  subject to  $\bar{\Gamma}\succeq 0.$  (12)

The solution to this optimization problem is  $2\sqrt{2}$ , as noted by Wehner [10], and we thus recover the well-known Tsirelson bound. More generally, for any given Bell inequality, SDPs can be associated to each of the conditions  $\mathcal{T}_1, \mathcal{T}_2, \ldots$  of our hierarchy, the solutions of which would yield a sequence  $I_1 \geq I_2 \geq \ldots$  of upper bounds on the quantum violation of the inequality. Note that a tight bound may already be reached after a finite number of such iterations, as the CHSH example shows.

We have applied the approach just outlined to the Collins et al. inequalities [14]. This family of inequalities involves two measurement choices per party and  $d$  outputs per measurement, and can be viewed as a generalization of the CHSH inequality for systems of dimension greater than two. In [15], lower-bounds for the maximal violation of the Collins et al. inequalities are given for  $d = 3,\ldots ,8$  by exhibiting a particular set of measurements and states of dimension  $d\times d$  yielding high violations of the inequalities. These quantum states have the particularity to be nonmaximally entangled. For  $d = 3$ , the reported violation is  $I_{*} = 2.9149$ , the local bound of the inequality being  $I_{\mathrm{loc}}\leq 2$ . We have numerically solved the SDP corresponding to the first tests in our hierarchy using the SeDuMi Matlab toolbox [16]. For  $d = 3$ , the condition  $\mathcal{T}_1$  yields the bound  $I\leq 3.1547$ , which is about  $10\%$  higher than the violation reported in [15]. The second condition  $\mathcal{T}_2$ , however, yields the bound  $I\leq I_{*} = 2.9149$ , proving that the partially entangled state and the measurements described in [15] are optimal. We have also

solved the SDP for  $d = 4, \ldots, 8$ . As for the  $d = 3$  case, the first tests in the hierarchy are about  $10\%$  above the values of [15], but the second tests give the same results as the ones reported in [15], demonstrating that these are the optimal quantum violations.

Conclusion.-The approach given in this work opens a new way to study the correlations between two separate quantum systems. There are several possible extensions of our technique, for instance, to systems of more than two parties, and many potential applications of it, among others to study nonlocal properties of quantum correlations, such as their monogamous character [17]. Two questions that remain open is whether the hierarchy of conditions that we have introduced is complete, in the sense that a set of correlations satisfies every condition in the hierarchy if and only if it admits a quantum representation, and, if this is the case, whether it is in general necessary to check all the conditions in this infinite hierarchy or whether it is sufficient to stop after a finite number of steps.

We acknowledge support by the Spanish Project No. FIS2004-05639-C02-02 and the EU Qubit Applications Project (QAP), Contract No. 015848. A.A. acknowledges support from a Spanish "Ramon y Cajal" Grant. M.N. is supported by the Fundacion Ramon Areces.

*Electronic address: Miguel.Navascues@icfo.es  
Electronic address: Stefano.Pironio@icfo.es  
Electronic address: Antonio.Acin@icfo.es

[1] J.S. Bell, Speakable and Unspeakable in Quantum Mechanics (Cambridge University Press, Cambridge, England, 1987).  
[2] L. A. Khalfi and B. S. Tsirelson, in Symposium on the Foundations of Modern Physics, edited by P. Lahti and P. Mittelstaedt (World Scientific, Singapore, 1985), p. 441.  
[3] R. Cleve et al., in Proceedings of the 19th IEEE Conference on Computational Complexity (CCC 2004) (IEEE Computer Society, Los Alamitos, 2004), p. 236.  
[4] J. Barrett, L. Hardy, and A. Kent, Phys. Rev. Lett. 95, 010503 (2005).  
[5] A. Acín, S. Massar, and S. Pironio, New J. Phys. 8, 126 (2006).  
[6] B. S. Cirel'son, Lett. Math. Phys. 4, 93 (1980).  
[7] J. F. Clauser et al., Phys. Rev. Lett. 23, 880 (1969).  
[8] See, for instance, H. Buhrman and S. Massar, Phys. Rev. A 72, 052103 (2005), and references therein.  
[9] L. J. Landau, Found. Phys. 18, 449 (1988).  
[10] S. Wehner, Phys. Rev. A 73, 022110 (2006).  
[11] L. Vandenberghe and S. Boyd, SIAM Rev. 38, 49 (1996).  
[12] B. S. Tsirel'son, J. Sov. Math. 36, 557 (1987).  
[13] L. Masanes, quant-ph/0309137.  
[14] D. Collins et al., Phys. Rev. Lett. 88, 040404 (2002).  
[15] A. Acin et al., Phys. Rev. A 65, 052325 (2002).  
[16] J. Sturm and Advanced Optimization Laboratory, SeDuMi, http://sedumi.mcmaster.ca.  
[17] J. Barrett, A. Kent, and S. Pironio, Phys. Rev. Lett. 97, 170409 (2006).