# Concurrence-based entanglement measures for isotropic states

Pranaw Rungta and Carlton M. Caves  
Department of Physics and Astronomy, University of New Mexico, Albuquerque, New Mexico 87131-1156  
(Received 2 August 2002; published 14 January 2003)

We discuss properties of entanglement measures called  $I$ -concurrence and tangle. For a bipartite pure state,  $I$ -concurrence and tangle are simply related to the purity of the marginal density operators. The  $I$ -concurrence (tangle) of a bipartite mixed state is the minimum average  $I$ -concurrence (tangle) of ensemble decompositions of pure states of the joint density operator. Terhal and Vollbrecht [Phys. Rev. Lett. 85, 2625 (2000)] have given an explicit formula for the entanglement of formation of isotropic states in arbitrary dimensions. We use their formalism to derive comparable expressions for the  $I$ -concurrence and tangle of isotropic states.

DOI: 10.1103/PhysRevA.67.012307

PACS number(s): 03.67.Lx, 03.65.Ud

# I. INTRODUCTION

Entanglement among quantum systems is a distinctive feature of quantum mechanics [1-3] and an indispensable ingredient in various kinds of quantum information processing protocols [4,5], e.g., quantum teleportation. It is desirable to have a general theory of entanglement, but though important results have been obtained, a general theory has proven elusive because of the complex nature of entanglement for all but the very simplest joint quantum systems. Several measures of entanglement have been suggested and investigated: the entanglement of formation [6,7], the entanglement of distillation [6,7], the relative entropy [8,9], the robustness of entanglement [10], and others. In this paper, we explore a measure of entanglement called the  $I$ -concurrence, which was introduced by Hill and Wootters [11,12] for pairs of qubits and generalized to arbitrary bipartite systems by Rungta et al. [13]. Before turning to the  $I$ -concurrence, we summarize here relevant results from entanglement theory which will facilitate the discussion of  $I$ -concurrence.

Work on entanglement has served to identify certain  $a$  priori axioms for a good measure of entanglement [14]. Entanglement characterizes intrinsically quantum-mechanical correlations between quantum systems. If  $E(\rho)$  denotes an amount of entanglement in the joint state  $\rho$  of several quantum systems, a fundamental requirement for  $E$  to be a good measure of entanglement is the following:

(1)  $E(\rho)$  does not increase, on average, under local operations and classical communication (LOCC). Such a measure is called an entanglement monotone [14].  
An entanglement monotone must remain the same under the action of reversible LOCC. Hence, it is invariant under local unitary transformations since these can be locally reversed. Moreover, any state  $\rho$  can be converted into any separable state using LOCC; therefore, an entanglement monotone takes a common minimum value for all separable states, which can always be adjusted to zero [14]. Thus, we can impose an additional, nonnegativity requirement for a good entanglement measure:  
(2)  $E(\rho) \geqslant 0$  and goes to zero if and only if  $\rho$  is a separable state.

Henceforth, we restrict our discussion to bipartite quantum systems. In three or more Hilbert-space dimensions, more than one measure is required to characterize the en

tanglement of bipartite states [10,14,15]: to specify completely a joint pure state of a  $d \times d$  system, up to local actions, requires  $d - 1$  independent Schmidt coefficients. Vidal [14] showed how to construct an infinite family of entanglement monotones for bipartite systems. This family of entanglement measures, denoted by  $\nu(\rho)$ , is characterized by the following conditions.

(i) For a pure state  $|\Psi \rangle \langle \Psi |$  , the measure is a function of the marginal density operator  $\rho_{A} = \mathrm{tr}_{B}(|\Psi \rangle \langle \Psi |)$  , i.e.,  $\nu (\Psi)$ $= f(\rho_{A})$  , where the function  $f$  has the following properties: (a) invariance under unitary transformations, i.e.,  $f(U\rho_{A}U^{\dagger}) = f(\rho_{A})$  , which implies that  $f(\rho_{A})$  is a function of the eigenvalues of  $\rho_{A}$  , and (b) concavity, i.e.,  $f(\lambda_1\rho_1 + \lambda_2\rho_2)\geqslant \lambda_1f(\rho_1) + \lambda_2f(\rho_2)$  , where  $\lambda_{1},\lambda_{2}\geqslant 0$  and  $\lambda_{1}$ $+\lambda_{2} = 1$  
(ii) For a mixed state  $\rho$ , the measure is defined to be the convex-roof extension of the pure-state measure, i.e., the minimum average value of the measure over all ensemble decompositions of  $\rho$ ,

$$
\nu (\rho) \equiv \min  _ {\left\{p _ {j}, | \Psi_ {j} \rangle \right\}} \left\{\sum p _ {j} \nu (\Psi_ {j}) \left| \sum_ {j} p _ {j} | \Psi_ {j} \rangle \langle \Psi_ {j} | = \rho \right. \right\}. \tag {1.1}
$$

Vidal [14] showed that if a measure belongs to the above family, it satisfies property 1 and thus, is an entanglement monotone. The  $I$ -concurrence, as we show in Sec. II, belongs to this family. Vidal also showed that when restricted to pure states, any entanglement monotone satisfies condition (i).

A privileged example of an entanglement monotone comes from choosing the unitarily invariant concave function of condition (i) to be the von Neumann entropy,  $f(\rho_A) = S(\rho_A) = -\mathrm{tr}(\rho_A \log_2 \rho_A)$ . This entanglement measure plays a special role because of the asymptotic reversibility of the processes of entanglement dilution and concentration for pure states, with von Neumann entropy entering as the currency for these reversible transformations [16]:  $nS(\rho_A)$  Bell states can be converted by LOCC to  $n$  copies of  $|\Psi\rangle$  in the limit as  $n$  goes to infinity and vice versa [6]. The corresponding entanglement monotone for pure states,  $E_f(\Psi) = S(\rho_A)$ , when extended to mixed states by the convex roof, is called the entanglement of formation [6,7],

$$
E _ {f} (\rho) \equiv \min  _ {\left\{p _ {j}, | \Psi_ {j} \rangle \right\}} \left\{\sum p _ {j} E _ {f} \left(\Psi_ {j}\right) \Bigg | \rho = \sum_ {j} p _ {j} | \Psi_ {j} \rangle \langle \Psi_ {j} | \right\}. \tag {1.2}
$$

Unlike the situation for pure states, however, it is not known whether the entanglement of formation gives the asymptotic cost in Bell states for creating many copies of a mixed state  $\rho$  using LOCC. This identification depends on whether  $E_{f}(\rho)$  is additive [3,12]. Though  $E_{f}(\Psi)$  is additive on pure states, this only implies that  $E_{f}(\rho)$  is subadditive on mixed states. If  $E_{f}(\rho)$  is strictly subadditive, then some other entanglement monotone, given by the von Neumann entropy for pure states, but less than  $E_{f}(\rho)$  for mixed states, quantifies the asymptotic cost of creating many copies of a mixed state [3,17].

The special role of von Neumann entropy has been reconciled with the existence of many other entanglement monotones by Vidal [14] and Nielsen [18]. Vidal considered a class of entanglement monotones that are additive on pure states and showed that they have different asymptotic properties than the entanglement of formation. Nielsen formulated a precise property of asymptotic continuity that is satisfied by the von Neumann entropy and showed that this property is the key to relating entanglement monotones to the asymptotic reversibility of entanglement dilution and concentration that holds for pure states. Indeed, Nielsen showed that any entanglement monotone that is additive on pure states and that satisfies his asymptotic continuity property is given, for pure states, by the von Neumann entropy of the marginal density operator. This result of Nielsen's leaves open the question of the entanglement cost for mixed states.

Entanglement monotones other than the entanglement of formation, though they are not related to asymptotic transformations, are nonetheless important for characterizing LOCC transformations between finite numbers of copies of states. Indeed, they have been used to quantify the probability and fidelity of exact and approximate LOCC transformations between pure states [15,19-21]. In this paper, we investigate the properties of entanglement monotones related to a particular entanglement measure called the  $I$ -concurrence.

Hill and Wootters [11] introduced the concurrence as a measure of entanglement for pairs of qubits. The concurrence for a pure state of two qubits is defined with the help of the qubit spin-flip operator, and it is extended to mixed states as the convex roof. Wootters [3,12] went on to derive an explicit formula for concurrence of an arbitrary joint state  $\rho$  of two qubits in terms of the eigenvalues of  $\sqrt{\rho}\widetilde{\rho}\sqrt{\rho}$ , where  $\widetilde{\rho}$  is obtained by spin flipping  $\rho$ , and showed how to calculate the corresponding entanglement of formation from the concurrence.

Rungta et al. [13] generalized the notion of concurrence to pairs of quantum systems of arbitrary dimension. This generalized concurrence for a joint pure state  $|\Psi \rangle$  of a  $d_A\times d_B$  system is simply related to the purity of the marginal density operators,

$$
C (\Psi) = \sqrt {2 \left[ 1 - \operatorname {t r} \left(\rho_ {A} ^ {2}\right) \right]} = \sqrt {2 \left[ 1 - \operatorname {t r} \left(\rho_ {B} ^ {2}\right) \right]}. \tag {1.3}
$$

The generalized concurrence is known as the  $I$ -concurrence because it is defined in terms of the universal-inverter superoperator [13], which was shown to be a natural generalization to higher dimensions of the spin flip for qubits. For the purposes of this paper, we need not introduce the universal inverter, simply taking Eq. (1.3) as the definition of the  $I$ -concurrence for pure states. The  $I$ -concurrence is extended to mixed states  $\rho$  by the convex roof,

$$
C (\rho) \equiv \min  _ {\left\{p _ {j}, | \Psi_ {j} \rangle \right\}} \left\{\sum p _ {j} C (\Psi_ {j}) \left| \sum_ {j} p _ {j} | \Psi_ {j} \rangle \langle \Psi_ {j} | = \rho \right. \right\}. \tag {1.4}
$$

For pairs of qubits, Coffman, Kundu, and Wooters [22] called  $C^2 (\rho)$  the tangle of the state  $\rho$ . In this paper, we prefer to refer to  $C^2 (\rho)$  simply as the squared I-concurrence and to reserve the term tangle for the quantity obtained by extending  $\tau (\Psi)\equiv C^2 (\Psi)$  to mixed states by the convex roof,

$$
\tau (\rho) \equiv \min  _ {\left\{p _ {j}, \mid \Psi_ {j} \right\rangle \}} \left\{\sum p _ {j} C ^ {2} \left(\Psi_ {j}\right) \left| \sum_ {j} p _ {j} \mid \Psi_ {j} \right\rangle \langle \Psi_ {j} \mid = \rho \right\}. \tag {1.5}
$$

Osborne [23] has calculated the tangle of rank-2 density operators in  $2 \times d$  systems. As noted by Osborne, the definition of tangle in Eq. (1.5) does no violence to the original usage of Coffman, Kundu, and Wootters, because  $\tau(\rho) = C^2(\rho)$  for bipartite qubit states, the reason being that all pure states in the optimal ensemble decomposition have the same concurrence. Osborne found the tangle as defined in Eq. (1.5) to be a more natural quantity in his analysis of rank-2 density operators, just as we find it to be more natural for isotropic states in our analysis below.

The motivation for this paper is to show that, like the entanglement of formation, the  $I$ -concurrence and tangle are entanglement monotones (Sec. II) and then to provide explicit formulas for the  $I$ -concurrence and tangle of isotropic states (Sec. III). For our analysis of isotropic states, we use the formalism developed by Terhal and Vollbrecht [24] to calculate the entanglement of formation for isotropic states. We find that the tangle for isotropic states is closely related to the corresponding entanglement of formation (Sec. IV).

# II. PROPERTIES OF I CONCURRENCE AND TANGLE

Henceforth, we will omit the "  $I$  " when referring to the  $I$ -concurrence. Consider the Schmidt decomposition of an arbitrary joint pure state  $|\Psi \rangle$  of a  $d_A\times d_B$  system,

$$
\left| \Psi \right\rangle = \sum_ {j} \sqrt {\mu_ {j}} \left| a _ {j} \right\rangle \otimes \left| b _ {j} \right\rangle = \sum_ {j} \sqrt {\mu_ {j}} U _ {A} \left| e _ {j} \right\rangle \otimes U _ {B} \left| e _ {j} \right\rangle . \tag {2.1}
$$

The squared Schmidt coefficients  $\mu_{j}$  are the eigenvalues of the marginal density operators,  $\rho_{A}$  and  $\rho_{B}$ , of the two systems, and the vectors  $|a_j\rangle$  and  $|b_j\rangle$  make up the orthonormal bases that diagonalize the marginal density operators. These bases are connected to a fiducial orthonormal basis  $\{|e_j\rangle\}$  by

unitary transformations  $U_{A}$  and  $U_{B}$ . The state  $|\Psi \rangle$  is specified by its Schmidt vector  $\pmb{\mu} \equiv (\sqrt{\mu_1},\dots ,\sqrt{\mu_d})$  and the unitary operators  $U_{A}$  and  $U_{B}$ .

The tangle, or squared concurrence, of the pure state  $|\Psi \rangle$  [see Eq. (1.3)] is given in terms of the Schmidt coefficients by

$$
\tau (\Psi) = C ^ {2} (\Psi) = 2 \left(1 - \sum_ {j} \mu_ {j} ^ {2}\right) = 4 \sum_ {j <   k} \mu_ {j} \mu_ {k} \equiv C ^ {2} (\boldsymbol {\mu}). \tag {2.2}
$$

$C^2 (\Psi)$  is conserved by local unitary transformations because it is a function only of the Schmidt coefficients [property (ia)]. It varies smoothly from 0, for pure product states, to  $2(d - 1) / d$ , where  $d\equiv \min (d_A,d_B)$ , for maximally entangled pure states.

That  $C^2(\Psi)$  is a concave function of  $\rho_A(\rho_B)$  [property (ib)] follows from the fact that  $f(x) = -x^2$ ,  $0 \leqslant x \leqslant 1$ , is a concave function, since for any concave function  $f$ , the mapping  $\rho \to \mathrm{tr}[f(\rho)]$  is concave [25]. To see this, let  $\rho = \lambda_1 \rho_1 + \lambda_2 \rho_2$ , with  $\lambda_1, \lambda_2 \geqslant 0$  and  $\lambda_1 + \lambda_2 = 1$ , and let  $\rho = \sum_j p_j | \phi_j \rangle \langle \phi_j |$ ,  $\rho_1 = \sum_k q_k | \xi_k \rangle \langle \xi_k |$ , and  $\rho_2 = \sum_l r_l | \eta_l \rangle \langle \eta_l |$  be eigendecompositions. Then we have

$$
\begin{array}{l} \operatorname {t r} [ f (\rho) ] = \sum_ {j} f \left(\left\langle \phi_ {j} \mid \rho \right| \phi_ {j} \right\rangle) \\ = \sum_ {j} f \left(\lambda_ {1} \left\langle \phi_ {j} \right| \rho_ {1} \mid \phi_ {j} \right\rangle + \lambda_ {2} \left\langle \phi_ {j} \mid \rho_ {2} \mid \phi_ {j} \right\rangle) \\ \geqslant \sum_ {j} \lambda_ {1} f (\left\langle \phi_ {j} \mid \rho_ {1} \mid \phi_ {j} \right\rangle) + \lambda_ {2} f (\left\langle \phi_ {j} \mid \rho_ {2} \mid \phi_ {j} \right\rangle) \\ = \lambda_ {1} \sum_ {j} f \left(\sum_ {k} | \langle \phi_ {j} | \xi_ {k} \rangle | ^ {2} q _ {k}\right) \\ + \lambda_ {2} \sum_ {j} f \left(\sum_ {l} | \langle \phi_ {j} | \eta_ {l} \rangle | ^ {2} r _ {l}\right) \\ \geqslant \lambda_ {1} \sum_ {j, k} | \langle \phi_ {j} | \xi_ {k} \rangle | ^ {2} f (q _ {k}) + \lambda_ {2} \sum_ {j, l} | \langle \phi_ {k} | \eta_ {l} \rangle | ^ {2} f (r _ {l}) \\ = \lambda_ {1} \sum_ {k} f (q _ {k}) + \lambda_ {2} \sum_ {l} f (r _ {l}) \\ = \lambda_ {1} \operatorname {t r} [ f (\rho_ {1}) ] + \lambda_ {2} \operatorname {t r} [ f (\rho_ {2}) ], \tag {2.3} \\ \end{array}
$$

where the two inequalities follow from the concavity of  $f$ . Since adding a constant and multiplying by a positive constant does not change concavity,  $C^2(\Psi)$  is a concave function of  $\rho_A$ . Since  $C^2(\Psi)$  satisfies property (i), its extension (1.5) by the convex roof to give the tangle  $\tau(\rho)$  of mixed states is an entanglement monotone.

The square root being an increasing concave function, it preserves concavity. Thus, the concurrence  $C(\Psi)$  is also a concave function of  $\rho_{A}$ , and its extension (1.4) to give the concurrence  $C(\rho)$  of mixed states is an entanglement mono

tone. Notice that since  $C(\Psi)$  is zero if and only if  $|\Psi\rangle$  is a pure product state,  $\tau(\rho)$  and  $C(\rho)$  are zero if and only if  $\rho$  is separable.

From the properties of an entanglement monotone or directly from the convex-roof construction, it is clear that the concurrence  $C(\rho)$  is a convex function of bipartite density operators. Since the square is an increasing convex function, it preserves convexity, thus making the squared concurrence  $C^2 (\rho)$  a convex function of bipartite density operators. As a convex function that agrees with the convex roof  $\tau (\rho)$  on pure states, the squared concurrence is guaranteed to satisfy  $C^2 (\rho)\leqslant \tau (\rho)$ . We are unable to say whether  $C^2 (\rho)$  is itself an entanglement monotone, although it seems unlikely that it satisfies the property of not increasing under local measurements.

# III. TANGLE AND CONCURRENCE OF ISOTROPIC STATES

# A. Isotropic states

In this section, we derive the tangle and concurrence of isotropic states. At the end of the section, we compare our results with the those for the entanglement of formation of isotropic states obtained by Terhal and Vollbrecht [24]. The tangle of isotropic states shares important features with the entanglement of formation, but the concurrence is significantly different.

Isotropic states are a class of mixed states for  $d \times d$  systems (two quuds); they are convex mixtures of the maximally mixed state  $I_{d^2} = I \otimes I / d^2$  with a maximally entangled state,

$$
| \Psi^ {+} \rangle \equiv \frac {1}{\sqrt {d}} \sum_ {j = 1} ^ {d} | e _ {j} \rangle \otimes | e _ {j} \rangle . \tag {3.1}
$$

Such mixtures can be expressed as

$$
\rho_ {F} = \frac {1 - F}{d ^ {2} - 1} (I - | \Psi^ {+} \rangle \langle \Psi^ {+} |) + F | \Psi^ {+} \rangle \langle \Psi^ {+} |, \tag {3.2}
$$

where  $F = \langle \Psi^{+}|\rho_{F}|\Psi^{+}\rangle$ , satisfying  $0\leqslant F\leqslant 1$ , is the fidelity of  $\rho_F$  and  $|\Psi^{+}\rangle$ . These states were shown to be separable for  $F\leqslant 1 / d$  [26,27].

The isotropic states are special in the sense that they are invariant under the action of the twirling superoperator  $\mathcal{T}$  [27],

$$
\mathcal {T} \left(\rho_ {F}\right) = \int d U U \otimes U ^ {*} \rho_ {F} U ^ {\dagger} \otimes U ^ {* \dagger} = \rho_ {F}. \tag {3.3}
$$

Indeed, the twirling superoperator reduces any two-qudit state  $\rho$  to an isotropic state,

$$
\mathcal {T} (\rho) = \rho_ {F (\rho)}, \tag {3.4}
$$

where  $F(\rho) = \langle \Psi^{+}|\rho |\Psi^{+}\rangle$  is the fidelity of  $\rho$  and  $|\Psi^{+}\rangle$ . Twirling the pure state  $|\Psi \rangle$  of Eq. (2.1) yields an isotropic state,

$$
\mathcal {T} \left(\left| \Psi \right\rangle \left\langle \Psi \right|\right) = \rho_ {F (\boldsymbol {\mu}, V)}, \tag {3.5}
$$

where the fidelity is given by

$$
\begin{array}{l} F (\boldsymbol {\mu}, V) = | \langle \Psi^ {+} | \Psi \rangle | ^ {2} = \frac {1}{d} \left| \sum_ {j, k} \sqrt {\mu_ {k}} \langle e _ {j} | U _ {A} | e _ {k} \rangle \langle e _ {j} | U _ {B} | e _ {k} \rangle \right| ^ {2} \\ = \frac {1}{d} \left| \sum_ {j, k} \sqrt {\mu_ {k}} (U _ {A}) _ {j k} (U _ {B}) _ {j k} \right| ^ {2} \\ = \frac {1}{d} \left| \sum_ {k} \sqrt {\mu_ {k}} \left(U _ {A} ^ {T} U _ {B}\right) _ {k k} \right| ^ {2} = \frac {1}{d} \left| \sum_ {k} \sqrt {\mu_ {k}} V _ {k k} \right| ^ {2}, \tag {3.6} \\ \end{array}
$$

$V = U_A^T U_B$  being a unitary matrix. It is easy to see that

$$
F (\boldsymbol {\mu}, V) \leqslant F (\boldsymbol {\mu}, I), \tag {3.7}
$$

since  $|V_{kk}| \leqslant 1$ ; equality holds if and only if  $V = I \exp(i\delta)$ .

# B. Reduction to a single extremization

We turn now to finding the tangle and concurrence of isotropic states, using the technique developed for entanglement of formation by Terhal and Vollbrecht [24]. We proceed with the analysis in terms of the tangle. The reader should note that nothing would change in the analysis if we replaced pure-state tangle  $C^2(\Psi)$  with pure-state concurrence  $C(\Psi)$ , thus, analyzing  $C(\rho)$  instead of  $\tau(\rho)$ , till we get to Sec. III D. At that point, we explicitly note the differences between the results for tangle and concurrence.

The tangle of an arbitrary bipartite state  $\rho$  satisfies the following inequality,

$$
\begin{array}{l} \tau (\rho) \equiv \min  _ {\left\{p _ {j}, | \Psi_ {j} \rangle \right\}} \left\{\sum_ {j} p _ {j} C ^ {2} \left(\Psi_ {j}\right) \left| \sum_ {j} p _ {j} | \Psi_ {j} \rangle \langle \Psi_ {j} | = \rho \right. \right\} (3.8) \\ \geqslant \min  _ {\left\{p _ {j}, \boldsymbol {\mu} _ {j}, V _ {j} \right\}} \left\{\sum_ {j} p _ {j} C ^ {2} \left(\boldsymbol {\mu} _ {j}\right) \middle | \sum_ {j} p _ {j} F \left(\boldsymbol {\mu} _ {j}, V _ {j}\right) = F (\rho) \right\}. (3.9) \\ \end{array}
$$

The inequality in Eq. (3.9) follows because an optimal decomposition of  $\rho$ , i.e., one which achieves the minimum in Eq. (3.8), automatically generates a set  $\{p_j, \boldsymbol{\mu}_j, V_j\}$  that satisfies the constraint in Eq. (3.9). In contrast, a set  $\{p_j, \boldsymbol{\mu}_j, V_j\}$  that achieves the minimum in Eq. (3.9) generally does not generate an ensemble decomposition of  $\rho$ . Additional simplification is achieved by splitting the minimization in Eq. (3.9) into two parts, i.e.,

$$
\begin{array}{l} \tau (\rho) \geqslant \min  _ {\left\{p _ {j}, V _ {j}, F _ {j} \right\}} \left\{\sum_ {j} p _ {j} C _ {V _ {j}} ^ {2} (F _ {j}) \middle | \sum_ {j} p _ {j} F _ {j} = F (\rho) \right\} \\ \equiv \tau [ F (\rho) ], \tag {3.10} \\ \end{array}
$$

with

$$
C _ {V} ^ {2} (F) \equiv \min  _ {\boldsymbol {\mu}} \left\{ \right.C ^ {2} (\boldsymbol {\mu}) \left| F (\boldsymbol {\mu}, V) \equiv \frac {1}{d} \right| \sum_ {k} V _ {k k} \sqrt {\mu_ {k}} \left. \right| ^ {2} = F \left. \right\}. \tag {3.11}
$$

The function  $\tau(F)$  defined in Eq. (3.10) is a function of the single parameter  $F = F(\rho)$ .

We can reduce the minimization problem further by noting that if  $\pmb{\nu}$  is the vector of Schmidt coefficients that provides the minimum for  $C_V^2 (F)$ , then  $F^{\prime}\equiv F(\pmb {\nu},I)\geqslant F(\pmb {\nu},V) = F$  [Eq. (3.7)] and

$$
C ^ {2} \left(F ^ {\prime}\right) \equiv C _ {I} ^ {2} \left(F ^ {\prime}\right) \leqslant C ^ {2} (\boldsymbol {\nu}) = C _ {V} ^ {2} (F). \tag {3.12}
$$

We find an explicit expression for  $C^2 (F)$  below and show that it is monotonically increasing, from which it follows that

$$
C _ {V} ^ {2} (F) \geqslant C ^ {2} \left(F ^ {\prime}\right) \geqslant C ^ {2} (F). \tag {3.13}
$$

Applying Eq. (3.13) to Eqs. (3.10) and (3.11) yields

$$
\tau (F) = \min  _ {\left\{p _ {j}, F _ {j} \right\}} \left\{\sum_ {j} p _ {j} C ^ {2} \left(F _ {j}\right) \middle | \sum_ {j} p _ {j} F _ {j} = F \right\}, \tag {3.14}
$$

$$
C ^ {2} (F) = \min  _ {\boldsymbol {\mu}} \left\{C ^ {2} (\boldsymbol {\mu}) \left| \frac {1}{d} \left(\sum_ {k} \sqrt {\mu_ {k}}\right) ^ {2} = F \right. \right\}. \tag {3.15}
$$

Notice that the inequality  $C^2 (F') \geqslant C^2 (F)$  in Eq. (3.14) requires us to assume that  $F \geqslant 1 / d$ , since the minimum that defines  $C^2 (F)$  does not exist for  $F < 1 / d$ . This is not a problem for the analysis of isotropic states, since isotropic states with  $F \leqslant 1 / d$  are separable, having  $\tau (\rho_F) = 0$  and  $C(\rho_F) = 0$ . The function  $\tau (F)$  is by definition a convex function of  $F$ . Indeed,  $\tau (F)$  can be defined as the largest convex function that is bounded above by  $C^2 (F)$ ; it is given either by  $C^2 (F)$  or by straight-line segments that connect points on the graph of  $C^2 (F)$  and lie beneath  $C^2 (F)$ .

We have shown that the tangle for any bipartite pure state is bounded below by  $\tau (\rho)\geqslant \tau [F(\rho)]$ . Now, we use the twirling superoperator to show that isotropic states achieve this lower bound. To do so, consider an isotropic state  $\rho_F$ . Let  $\{p_j,F_j,\pmb {\mu}_j\}$  be a set that achieves the minimum in Eqs. (3.14) and (3.15) with this value of  $F$ , and let  $\{| \Psi_{j} \rangle \}$  be states constructed from the Schmidt vectors  $\{\pmb {\mu}_j\}$  with  $V_{j}$ $= I$ . The state formed from this ensemble,

$$
\rho = \sum_ {j} p _ {j} | \Psi_ {j} \rangle \langle \Psi_ {j} |, \tag {3.16}
$$

has a tangle that satisfies  $\tau (\rho)\leqslant \Sigma_{j}p_{j}C^{2}(\Psi_{j}) = \tau (F)$ . Twirling  $\rho$  gives

$$
\mathcal {T} (\rho) = \sum_ {j} p _ {j} \mathcal {T} \left(\left| \Psi_ {j} \right\rangle \langle \Psi_ {j} |\right) = \sum_ {j} p _ {j} \rho_ {F _ {j}} = \rho_ {F}, \tag {3.17}
$$

where we have made use of Eq. (3.5) to write  $\mathcal{T}(|\Psi_j\rangle \langle \Psi_j|) = \rho_{F_j}$ . Since the local operations involved in twirling cannot increase the tangle, we have  $\tau (\rho)\geqslant \tau (\rho_F)$ , from which follows the upper bound  $\tau (\rho_F)\leqslant \tau (F)$ .

Combined with the lower bound  $\tau (\rho_F)\geqslant \tau (F)$  , this shows that the tangle of an isotropic state  $\rho_{F}$  is given by the function  $\tau (F)$  . We have, thus, reduced the problem of finding the tangle of an isotropic state to a single minimization, that of finding the function  $C^2 (F)$  , from which  $\tau (\rho_F) = \tau (F)$  can be constructed as described above. If we follow through the steps of this subsection for the concurrence, instead of the

tangle, we find that the concurrence of an isotropic state,  $C(\rho_F)$ , is the largest convex function that is bounded above by  $C(F)$ .

# C. The extremization

Following the method of Terhal and Vollbrecht [24], we calculate  $C^2 (F)$  using the method of Lagrange multipliers; i.e., we minimize  $C^2 (\pmb {\mu})$  [Eq. (2.2)] subject to the constraints

$$
\sum_ {j} \mu_ {j} = 1, \tag {3.18}
$$

$$
\sum_ {j} \sqrt {\mu_ {j}} = \sqrt {F d}, \tag {3.19}
$$

with  $Fd \geqslant 1$ . In doing the extremization, we allow for the possibility that the minimum might not have all nonzero Schmidt coefficients by explicitly considering all the cases, where the number of nonzero Schmidt coefficients varies from 1 to  $d$ . The condition for an extremum is

$$
(\sqrt {\mu_ {j}}) ^ {3} + \lambda_ {1} \sqrt {\mu_ {j}} + \lambda_ {2} = 0, \tag {3.20}
$$

where  $\lambda_{1}$  and  $\lambda_{2}$  are Lagrange multipliers. The three solutions of this cubic equation for  $\sqrt{\mu_j}$  sum to zero, so there are at most two real, positive solutions. Letting  $\gamma$  and  $\delta$  denote these two positive solutions, with  $\gamma >\delta$ , the possible Schmidt vectors  $\pmb{\mu}$  have coefficients

$$
\mu_ {j} = \left\{ \begin{array}{l l} \gamma^ {2}, & j = 1, \dots , n \\ \delta^ {2}, & j = n + 1, \dots , n + m \\ 0, & j = n + m + 1, \dots , d, \end{array} \right. \tag {3.21}
$$

where  $n + m \leqslant d$  and  $n \geqslant 1$ . The corresponding extrema of  $C^2(\pmb{\mu})$  are

$$
C _ {n m} ^ {2} (F) = 2 \left(1 - n \gamma^ {4} - m \delta^ {4}\right), \tag {3.22}
$$

with the constraints

$$
n \gamma^ {2} + m \delta^ {2} = 1,
$$

$$
n \gamma + m \delta = \sqrt {F d}. \tag {3.23}
$$

Solving Eqs. (3.23), we obtain

$$
\gamma_ {n m} ^ {\pm} (F) = \frac {n \sqrt {F d} \pm \sqrt {n m (n + m - F d)}}{n (n + m)}, \tag {3.24}
$$

$$
\delta_ {n m} ^ {\pm} (F) = \frac {\sqrt {F d} - n \gamma_ {n m} ^ {\pm}}{m} = \frac {m \sqrt {F d} \mp \sqrt {n m (n + m - F d)}}{m (n + m)}. \tag {3.25}
$$

The relation  $\delta_{nm}^{\pm}(F) = \gamma_{mn}^{\mp}(F)$  means that as we vary  $n$  and  $m$  over all possible values, we need only to consider the upper sign; henceforth, we drop the signs, using always the upper sign. For the expressions (3.24) and (3.25) to give real values, the quantity inside the square root must be nonnegative, which implies that  $Fd\leqslant n + m$ ; moreover, in order that

$\delta_{nm}$  be nonnegative, we must have  $Fd \geqslant n$ . It is easy to see that  $\delta_{nm}(F) \leqslant \sqrt{Fd} / (n + m) \leqslant \gamma_{nm}(F)$ , confirming that the choice of the upper sign corresponds to our assumption that  $\gamma > \delta$ . Notice also that  $n = 0$  is ill defined, as expected, thus requiring  $n \geqslant 1$ .

The function  $C^2 (F)$ , we seek is the minimum of  $C_{nm}^2 (F)$  over all choices of  $n$  and  $m$ . We can perform the minimization explicitly by regarding  $n$  and  $m$  as continuous variables (here our treatment departs from that of Terhal and Vollbrecht). The task is to minimize  $C_{nm}^2 (F)$  on the parallelogram defined by  $1\leqslant n\leqslant Fd$  and  $Fd\leqslant n + m\leqslant d$ . Notice that the parallelogram collapses to a line when  $Fd = 1$ , i.e., at the separability boundary. As already noted, within the parallelogram we have  $\gamma_{nm}(F)\geqslant \delta_{nm}(F)\geqslant 0$ ;  $\gamma_{nm}(F) = \delta_{nm}(F)$  if and only if  $n + m = Fd$ , and  $\delta_{nm}(F) = 0$  if and only if  $n = Fd$ . We first calculate the derivatives of  $\gamma_{nm}(F)$  and  $\delta_{nm}(F)$  with respect to  $n$  and  $m$  by differentiating the constraints (3.23),

$$
\frac {\partial \gamma}{\partial n} = \frac {1}{2 n} \frac {2 \gamma \delta - \gamma^ {2}}{\gamma - \delta},
$$

$$
\frac {\partial \delta}{\partial n} = - \frac {1}{2 m} \frac {\gamma^ {2}}{\gamma - \delta},
$$

$$
\frac {\partial \delta}{\partial m} = - \frac {1}{2 m} \frac {2 \gamma \delta - \delta^ {2}}{\gamma - \delta},
$$

$$
\frac {\partial \gamma}{\partial m} = \frac {1}{2 n} \frac {\delta^ {2}}{\gamma - \delta}. \tag {3.26}
$$

These can be used in Eq. (3.22) to calculate the partial derivatives of  $C_{nm}^2 (F)$ ,

$$
\frac {\partial C ^ {2}}{\partial n} = 2 \gamma^ {2} [ \gamma^ {2} - 2 \delta (\gamma + \delta) ], \tag {3.27}
$$

$$
\frac {\partial C ^ {2}}{\partial m} = 2 \delta^ {2} [ \delta^ {2} - 2 \gamma (\gamma + \delta) ] \leqslant - 6 \delta^ {4} \leqslant 0. \tag {3.28}
$$

It is useful to introduce coordinates  $u \equiv m - n$  and  $v \equiv m + n$ , which correspond to motion parallel to and perpendicular to the  $m + n =$  constant boundaries of the parallelogram. The derivative of  $C^2$  with respect to  $u$  is

$$
\frac {\partial C ^ {2}}{\partial u} = - \frac {1}{2} (\gamma + \delta) (\gamma - \delta) ^ {3} \leqslant 0. \tag {3.29}
$$

The inequalities in Eqs. (3.28) and (3.29) follow immediately from the fact that  $\gamma \geqslant \delta \geqslant 0$  within the parallelogram. It should be clear that  $\partial C_{nm}^2 /\partial m$  is strictly negative within the parallelogram and  $\partial C_{nm}^2 /\partial u$  is strictly negative except on the boundary  $m + n = Fd$ , where it is zero. These results mean that the minimum of  $C_{nm}^2 (F)$  occurs at the vertex  $n = 1$ ,  $m = d - 1$ , thus giving

$$
C ^ {2} (F) = C _ {1, d - 1} ^ {2} (F) = 2 \left(1 - \gamma_ {1, d - 1} ^ {4} - (d - 1) \delta_ {1, d - 1} ^ {4}\right). \tag {3.30}
$$

Here

$$
\gamma_ {1, d - 1} (F) = \sqrt {F / d} (1 + w \sqrt {d - 1}), \tag {3.31}
$$

$$
\delta_ {1, d - 1} (F) = \sqrt {F / d} (1 - w / \sqrt {d - 1}), \tag {3.32}
$$

with  $w \equiv \sqrt{(1 - F) / F}$ . Henceforth, we omit the subscripts that specify the case  $n = 1$  and  $m = d - 1$ , this being the only case of interest.

We need to confirm that  $C^2 (F)$  is monotonically increasing. Differentiating the constraints (3.23) gives

$$
\frac {\partial \gamma}{\partial F} = - \frac {1}{2} \sqrt {\frac {d}{F}} \frac {\delta}{\gamma - \delta}, \tag {3.33}
$$

$$
(d - 1) \frac {\partial \delta}{\partial F} = \frac {1}{2} \sqrt {\frac {d}{F}} \frac {\gamma}{\gamma - \delta}, \tag {3.34}
$$

from which we calculate

$$
\frac {\partial C ^ {2}}{\partial F} = 4 \sqrt {\frac {d}{F}} \gamma \delta (\gamma + \delta) \geqslant 0, \tag {3.35}
$$

equality holding if and only if  $\delta = 0$ , which requires  $Fd = 1$ , i.e., the separability boundary. We conclude that  $C^2 (F)$  [and  $C(F)]$  are monotonically increasing for  $1 / d\leqslant F\leqslant 1$ , as promised. It will be useful below to write  $\partial C^2 /\partial F$  explicitly in terms of  $F$  and  $d$

$$
\begin{array}{l} \frac {\partial C ^ {2}}{\partial F} = 8 \frac {F}{d} (1 + w \sqrt {d - 1}) \left(1 - \frac {w}{\sqrt {d - 1}}\right) \\ \times \left[ 1 + w \frac {1}{2} \left(\sqrt {d - 1} - \frac {1}{\sqrt {d - 1}}\right) \right]. \tag {3.36} \\ \end{array}
$$

# D. Results

# 1. Two qubits

The case of two qubits  $(d = 2)$  is special, so we discuss it separately. For two qubits, there is one extremum,  $C^2 (F) = C_{11}^2 (F) = (2F - 1)^2$ ,  $1 / 2\leqslant F\leqslant 1$ . Since  $C^2 (F)$  is a convex function of  $F$ , it follows that the tangle of an isotropic state  $\rho_F$  is given by

$$
\tau \left(\rho_ {F}\right) = \left\{ \begin{array}{l l} 0, & 0 \leqslant F \leqslant 1 / 2 \\ (1 - 2 F) ^ {2}, & 1 / 2 \leqslant F \leqslant 1, \end{array} \right. \tag {3.37}
$$

and that the pure states in an optimal ensemble decomposition for the tangle all have the same tangle. The same conclusions hold for the concurrence,  $C(\rho_F) = C(F) = 1 - 2F$ ,  $1/2 \leqslant F \leqslant 1$ , which agrees with the general expression derived by Wootters [12].

# 2. Two qutrits

We consider the case of two qutrits  $(d = 3)$  separately as an illustration of what happens in the general qudit case. Of the three extrema,  $C_{11}^{2}(F), C_{21}^{2}(F)$ , and  $C_{12}^{2}(F)$ , we already know that the minimum is given by  $C_{12}^{2}(F)$ , i.e.,  $C^2 (F)$

![](images/c4da94e4474b62ea3612ca879b937c87830d8292ec7da3673777f822b7249ab9.jpg)  
FIG. 1. Plots of  $C_{11}^{2}(F)$  (dashed line),  $C_{21}^{2}(F)$  (dotted line), and  $C_{12}^{2}(F) = C^{2}(F)$  (solid line) for  $d = 3$ .

$= C_{12}^{2}(F)$ ,  $1/3 \leqslant F \leqslant 1$ . This fact can also be seen from Fig. 1, where we have plotted the three extrema.

To calculate  $\tau (\rho_F)$ , it is necessary to analyze the behavior of  $C^2 (F)$ . In Fig. 2, we plot the first and second derivatives of  $C^2 (F)$ . The first derivative confirms that  $C^2 (F)$  is monotonically increasing. The second derivative changes sign from positive to negative;  $C^2 (F)$  changes from convex to concave where the second derivative vanishes. The tangle  $\tau (\rho_F)$  is the largest convex function bounded above by  $C^2 (F)$ , which is constructed in the following way. Find the (unique) line tangent to  $C^2 (F)$  that passes through the point  $(F = 1,C^{2} = 4 / 3)$ ; for  $F$  smaller than the tangent point, the tangle is given by  $C^2 (F)$ , but for  $F$  larger than the tangent point, the tangle is given by the line. The tangent point is found by solving the equation  $\partial C^2 /\partial F = [4 / 3 - C^2 (F)] / (1 - F)$ , which gives  $F = 8 / 9$ . The slope of the line is  $(\partial C^2 /\partial F)|_{F = 8 / 9} = 3$ , and the tangle at the tangent point is  $C^2 (8 / 9) = 1$ . Thus, the tangle for  $d = 3$  is

$$
\tau \left(\rho_ {F}\right) = \left\{ \begin{array}{l l} 0, & F \leqslant 1 / 3 \\ C ^ {2} (F), & 1 / 3 \leqslant F \leqslant 8 / 9 \\ 3 (F - 1) + 4 / 3, & 8 / 9 \leqslant F \leqslant 1. \end{array} \right. \tag {3.38}
$$

This function is plotted in Fig. 3.

The behavior of  $C^2 (F)$  means that the pure states in an optimal ensemble decomposition for the tangle all have the

![](images/ed54329da5e4bcfad0c3b5d22bb9c624738c80cf31d805de0008d861934b0b79.jpg)  
FIG. 2. First (solid line) and second (dotted line) derivatives of  $C^2(F) = C_{12}^2(F)$  for  $d = 3$ .

![](images/757bfa1a1451f3a9ddb86678773a7979cb7cc6a66c2c756b8a0b3d3cdd7ef24f.jpg)  
FIG. 3. Tangle  $\tau (\rho_F)$  for  $d = 3$  (dotted),  $d = 10$  (short dashed),  $d = 100$  (long dashed), and  $d = 10000$  (solid). The solid line is indistinguishable from the asymptotic tangle.

same tangle for  $F \leqslant 8/9$ , but have two values of tangle, 1 and 4/3 (maximal entanglement), for  $F > 8/9$ .

Of the three extrema for the concurrence,  $C_{11}(F)$ ,  $C_{21}(F)$ , and  $C_{12}(F)$ , the minimum is given by  $C_{12}(F) = C(F)$ , a fact confirmed by the plots in Fig. 4. In contrast to the situation with the tangle, however, the second derivative of  $C(F) = C_{12}(F)$  is always negative (see Fig. 5), which means that  $C(F)$  is concave. Therefore, the qutrit concurrence is the straight line passing through the points  $(F = 1/3, C = 0)$  and  $(F = 1, C = \sqrt{4/3})$ , i.e.,

$$
C \left(\rho_ {F}\right) = \left\{ \begin{array}{l l} 0, & F \leqslant 1 / 3 \\ \sqrt {3} (F - 1 / 3), & 1 / 3 \leqslant F \leqslant 1. \end{array} \right. \tag {3.39}
$$

The concavity of  $C(F)$  means that the pure states in an optimal ensemble decomposition for the concurrence are either product states or maximally entangled states.

# 3. Two qudits

For arbitrary  $d$ , we have already established that  $C^2 (F) = C_{1,d - 1}^2 (F)$ . It turns out that for arbitrary  $d \geqslant 3$ ,  $C^2 (F)$  has the same behavior as for  $d = 3$ ; i.e., it changes from convex

![](images/a8a9176e0a16bad5f26fe5aec8ccb7062f47b72abf1b38fe536cea5bd583f661.jpg)  
FIG. 4. Plots of  $C_{11}(F)$  (dashed line),  $C_{21}(F)$  (dotted line), and  $C_{12}(F) = C(F)$  (solid line) for  $d = 3$ .

to concave as  $F$  increases. We get at this behavior by calculating the second derivative of  $C^2$  from Eq. (3.36),

$$
\begin{array}{l} \frac {\partial^ {2} C ^ {2}}{\partial F ^ {2}} = - \frac {1}{2 w F ^ {2}} \frac {\partial}{\partial w} \left(\frac {\partial C ^ {2}}{\partial F}\right) = - \frac {6}{w} \frac {d - 2}{d \sqrt {d - 1}} \\ \times \left(1 + \frac {2}{3} \frac {d ^ {2} - 8 d + 8}{(d - 2) \sqrt {d - 1}} w - 2 w ^ {2} - \frac {1}{3} w ^ {4}\right). \tag {3.40} \\ \end{array}
$$

Notice that for  $d = 2$  this expression simplifies to  $\partial^2 C^2 /\partial F^2 = 8$ , as it should. For  $d\geqslant 3$ , the polynomial in large parentheses in Eq. (3.40) clearly has one root for positive  $w$ ; it is easy to verify that this one root occurs in the range of interest, i.e., between  $F = 1 / d$  ( $w = \sqrt{d - 1}$ ) and  $F = 1$  ( $w = 0$ ), showing that  $C^2 (F)$  changes from convex to concave as  $F$  increases.

We find the tangle  $\tau (\rho_F)$  just as for  $d = 3$ , i.e., by finding the line tangent to  $C^2 (F)$  that passes through the point  $(F$ $= 1,C^{2} = 2(d - 1) / d)$ . Solving the equation  $\partial C^2 /\partial F = [2(d$ $-1) / d - C^2 (F)] / (1 - F)$  gives a tangent point at  $F = 4(d$ $-1) / d^{2}$ , where the tangle and slope are  $C^2 = 2(2d$ $-3) / d(d - 1)$  and  $\partial C^2 /\partial F = 2d / (d - 1)$ . Thus, the tangle is given by

$$
\tau \left(\rho_ {F}\right) = \left\{ \begin{array}{l l} 0, & F \leqslant 1 / d \\ C ^ {2} (F), & 1 / d \leqslant F \leqslant 4 (d - 1) / d ^ {2} \\ 2 d (F - 1) / (d - 1) + 2 (d - 1) / d, & 4 (d - 1) / d ^ {2} \leqslant F \leqslant 1. \end{array} \right. \tag {3.41}
$$

The tangle is plotted for a few representative values of  $d$  in Fig. 3. The pure states in an optimal ensemble decomposition for the tangle all have the same tangle for  $F \leqslant 4(d - 1) / d^2$ , but have two values of tangle,  $2(2d - 3) / d(d - 1)$  and  $2(d - 1) / d$  (maximal entanglement), for  $F > 4(d - 1) / d^2$ . As  $d \to \infty$ ,  $\tau(\rho_F) \to 2F$  becomes a linear function.

The concurrence also has the same behavior generally as for  $d = 3$ . A calculation of  $\partial^2 C / \partial F^2$  using Eqs. (3.36) and (3.40) shows that  $C(F)$  is a concave function on the range of

interest. Thus, the concurrence of isotropic states is a linear function between zero concurrence at the separability boundary and maximal entanglement at  $F = 1$ ,

$$
C \left(\rho_ {F}\right) = \left\{ \begin{array}{l l} 0, & F \leqslant 1 / d \\ \sqrt {2 d / (d - 1)} (F - 1 / d), & 1 / d \leqslant F \leqslant 1. \end{array} \right. \tag {3.42}
$$

The pure states in an optimal ensemble decomposition for

![](images/2d55e7e5c1730a0d79e6d3bec84574e06463d20bcdbeccc59012f8c83b3298fe.jpg)  
FIG. 5. First (solid line) and second (dotted line) derivatives of  $C(F) = C_{12}(F)$  for  $d = 3$ .

the concurrence are either product states or maximally entangled states. As  $d\to \infty$ $C(\rho_F)\rightarrow \sqrt{2} F$

# IV. CONCLUSION

It is informative to conclude the paper by comparing our results for the tangle of isotropic states with the results

of Terhal and Vollbrecht [24] for the entanglement of formation.

If one follows through the procedure of Terhal and Vollbrecht [24] for finding the entanglement of formation, one finds that the function  $C^2 (F)$  is replaced by the function

$$
E (F) \equiv H _ {2} (\gamma^ {2}) + (1 - \gamma^ {2}) \log_ {2} (d - 1), \tag {4.1}
$$

where  $\gamma = \gamma_{1,d - 1}$  and  $H_{2}(x) = -x\log_{2}x - (1 - x)\log_{2}(1 - x)$  is the binary entropy function. The entanglement of formation  $E(\rho_F)$  is given by the largest convex function that is bounded above by  $E(F)$ . Terhal and Vollbrecht conjecture that  $E(F)$  has the properties that we find here for  $C^2 (F)$ , i.e., that  $E(F)$  has a single inflection point in the range  $1 / d\leqslant F$ $\leqslant 1$ , changing from convex to concave as  $F$  increases. Given this conjecture, the entanglement of formation is found by finding the straight line tangent to  $E(F)$  that passes through the point  $(F = 1,E = \log_2d)$ . Remarkably, the tangent point for  $E(F)$  is the same as for  $C^2 (F)$ , which gives the entanglement of formation as

$$
E _ {f} \left(\rho_ {F}\right) = \left\{ \begin{array}{l l} 0, & F \leqslant 1 / d \\ E (F), & 1 / d \leqslant F \leqslant 4 (d - 1) / d ^ {2} \\ d \log_ {2} (d - 1) (F - 1) / (d - 2) + \log_ {2} d, & 4 (d - 1) / d ^ {2} \leqslant F \leqslant 1. \end{array} \right. \tag {4.2}
$$

Asymptotically, as  $d \to \infty$ , the entanglement of formation becomes  $E_{f}(\rho_{F}) \rightarrow F\log_{2}d$ . The similarity of the tangle and entanglement of formation must reflect a deep connection between the two, at least for isotropic states, but we have not been able to find a simple reason for this similarity.

# ACKNOWLEDGMENT

This work was supported in part by Office of Naval Research Contract No. N00014-00-1-0578.

[1] A. Einstein, B. Podolski, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[2] J.S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964).  
[3] W.K. Wootters, Quantum Inf. Comput. 1, 27 (2001).  
[4] Introduction to Quantum Computation and Information, edited by H.-K. Lo, S. Popescu, and T. Spiller (World Scientific, Singapore, 1998).  
[5] M.A. Nielsen and I.L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2000).  
[6] C.H. Bennett, H.J. Bernstein, S. Popescu, and B. Schumacher, Phys. Rev. A 53, 2046 (1996).  
[7] C.H. Bennett, D.P. DiVincenzo, J.A. Smolin, and W.K. Wootters, Phys. Rev. A 54, 3824 (1996).  
[8] V. Vedral and M.B. Plenio, Phys. Rev. A 57, 1619 (1996).  
[9] V. Vedral, Rev. Mod. Phys. 74, 197 (2002).  
[10] G. Vidal and R. Tarrach, Phys. Rev. A 59, 141 (1999).

[11] S. Hill and W.K. Wootters, Phys. Rev. Lett. 78, 5022 (1997).  
[12] W.K. Wootters, Phys. Rev. Lett. 80, 2245 (1998).  
[13] P. Rungta, V. Buzek, C.M. Caves, M. Hillary, and G.J. Milburn, Phys. Rev. A 64, 042315 (2001).  
[14] G. Vidal, J. Mod. Opt. 47, 355 (2000).  
[15] G. Vidal, Phys. Rev. Lett. 83, 1046 (1999).  
[16] S. Popescu and D. Rohrlich, Phys. Rev. A 56, R3319 (1997).  
[17] P. Hayden, M. Horodecki, and B.M. Terhal, J. Phys. A 34, 6891 (2001).  
[18] M.A. Nielsen, Phys. Rev. A 61, 064301 (2000).  
[19] M.A. Nielsen, Phys. Rev. Lett. 83, 436 (1999).  
[20] D. Jonathan and M.B. Plenio, Phys. Rev. Lett. 83, 1455 (1999).  
[21] G. Vidal, D. Jonathan, and M.A. Nielsen, Phys. Rev. A 62, 012304 (2000).  
[22] V. Coffman, J. Kundu, and W.K. Wootters, Phys. Rev. A 61, 052306 (2000).

[23] T.J. Osborne, e-print quant-ph/0203087.  
[24] B.M. Terhal and K.G.H. Vollbrecht, Phys. Rev. Lett. 85, 2625 (2000).  
[25] A. Wehrl, Rev. Mod. Phys. 50, 221 (1978).  
[26] P. Rungta, W.J. Munro, K. Nemoto, P. Deuar, G.J. Milburn,

and C.M. Caves, in Directions in Quantum Optics: A Collection of Papers Dedicated to the Memory of Dan Walls, edited by H.J. Carmichael, R.J. Glauber, and M.O. Scully (Springer, Berlin, 2001), p. 149.  
[27] M. Horodecki and P. Horodecki, Phys. Rev. A 59, 4206 (1999).