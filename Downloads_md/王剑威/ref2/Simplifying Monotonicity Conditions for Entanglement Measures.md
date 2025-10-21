# Simplifying Monotonicity Conditions for Entanglement Measures

Michal Horodecki

Institute of Theoretical Physics and Astrophysics  
University of Gdańsk, 80-952 Gdańsk, Poland

(Received: December 29, 2004)

Abstract. We show that for a convex function the following, rather modest conditions, are equivalent to monotonicity under local operations and classical communication. The conditions are: (i) invariance under local unitaries, (ii) invariance under adding local ancilla in arbitrary state (iii) on mixtures of states possessing local orthogonal flags the function is equal to its average. The result holds for multipartite systems. It is intriguing that the obtained conditions are equalities. The only inequality is hidden in the condition of convexity.

Basic condition for a function to quantify entanglement is that it should be nonincreasing under local operations and classical communication (LOCC) [1,2,3] (see [4] for a review). The condition called LOCC monotonicity is usually not easy to prove for candidates for entanglement measures. The purpose of the paper is to derive conditions equivalent to LOCC monotonicity for convex functions. In other words, we consider a convex function  $f$  and ask what conditions it should satisfy, to be monotone under LOCC. Surprisingly, we obtain that the conditions are rather modest. They are the following: (i) invariance under local unitaries, (ii) invariance under adding local ancilla in standard pure state, (iii) on mixtures of states possessing local orthogonal flags the function should be equal to its average:

$$
f \left(\sum_ {i} p _ {i} \rho_ {i} \otimes | i \rangle \langle i |\right) = \sum_ {i} p _ {i} f \left(\rho_ {i} \otimes | i \rangle \langle i |\right). \tag {1}
$$

The last condition can be called affinity on locally orthogonal states. For convex functions, one way inequality follows from convexity. It is rather intuitive that the condition (iii) is necessary for LOCC monotonicity. However it is rather surprising that it is also sufficient together with rather modest conditions (i) and (ii). Our proofs will be carried out for bipartite states, however they immediately generalize to multipartite case.

To begin with, let us state more precisely what we mean by monotonicity under LOCC. A possible formulation is that for any quantum operation  $\Lambda$  that can be

carried out by means of local operations and classical communication we have

$$
f \left(\rho_ {A B}\right) \geq f \left(\Lambda \left(\rho_ {A B}\right)\right). \tag {2}
$$

If we treat LOCC operation as measurement with outcomes  $i$ , we can rewrite the condition

$$
f \left(\rho_ {A B}\right) \geq f \left(\sum_ {i} p _ {i} \sigma_ {A B} ^ {i}\right) \tag {3}
$$

where  $p_i$  are probabilities of outcomes, and  $\sigma_{AB}^i$  is state given outcome  $i$  was obtained. However, in this paper we will use the following, stronger definition of monotonicity:

DEFINITION 1 A function  $f$  is LOCC monotone iff it satisfies the following condition

$$
f \left(\rho_ {A B}\right) \geq \sum_ {i} p _ {i} f \left(\sigma_ {A B} ^ {i}\right) \tag {4}
$$

where  $i$  are outcomes of the LOCC operation,  $p_i$  are the probabilities of outcomes, and  $\sigma_{AB}^i$  is the state given that outcome  $i$  was obtained.

We will need the following result of Vidal [3]:

THEOREM 1 A convex function  $f$  is LOCC monotone in the sense of Definition 1 if and only if it does not increase under

a) adding local ancilla

$$
f \left(\rho_ {A B} \otimes \sigma_ {X}\right) \leq f \left(\rho_ {A B}\right), \quad X = A ^ {\prime}, B ^ {\prime} \tag {5}
$$

b) local partial trace

$$
f \left(\rho_ {A B}\right) \leq f \left(\rho_ {A B X}\right) \tag {6}
$$

c) local unitaries

$d)$  local von Neumann measurements (not necessarily complete),

$$
f \left(\rho_ {A B}\right) \geq \sum_ {i} p _ {i} f \left(\sigma_ {A B} ^ {i}\right) \tag {7}
$$

where  $\sigma_{AB}^{i}$  is the state after obtaining outcome  $i$ , and  $p_i$  is the probability of such outcome.

Remark 1 From the proof in [3] it is easy to see that the above theorem works also for multipartite systems.

We are now in position to state and prove our new conditions equivalent to LOCC monotonicity for convex functions.

THEOREM 2 A convex function  $f$  does not increase under LOCC if and only if (i)  $f$  is invariant under local unitary operations

$$
f \left(U _ {A} \otimes U _ {B} \rho_ {A B} U _ {A} ^ {\dagger} \otimes U _ {B} ^ {\dagger}\right) = f \left(\rho_ {A B}\right) \tag {8}
$$

(ii)  $f$  is invariant under adding local ancilla in arbitrary state at Alice or Bob's site

$$
f \left(\rho_ {A B} \otimes \sigma_ {X}\right) = f \left(\rho_ {A B}\right) \tag {9}
$$

for  $X = A^{\prime},B^{\prime}$

(iii)  $f$  is affine on locally orthogonal states, i.e.,

$$
f \left(\sum_ {i} p _ {i} \rho_ {A B} ^ {i} \otimes | i \rangle \langle i |\right) = \sum_ {i} p _ {i} f \left(\rho_ {A B} ^ {i} \otimes | i \rangle_ {X} \langle i |\right) \tag {10}
$$

for  $X = A', B'$ , where  $|i\rangle$  are local orthogonal flags.

Remark 2 Since  $f$  is assumed to be convex, in condition (ii) it is enough to check inequality in one direction. One can formulate the conditions in a more elegant way as follows

THEOREM 3 For a convex function  $f$  does not increase under LOCC if and only if [LUI]  $f$  satisfies local unitary invariance (LUI)

$$
f \left(U _ {A} \otimes U _ {B} \rho_ {A B} U _ {A} ^ {\dagger} \otimes U _ {B} ^ {\dagger}\right) = f (\rho_ {A B}) \tag {11}
$$

[FLAGS]  $f$  satisfies

$$
f \left(\sum_ {i} p _ {i} \rho_ {A B} ^ {i} \otimes | i \rangle_ {X} \langle i |\right) = \sum_ {i} p _ {i} f \left(\rho_ {A B} ^ {i}\right) \tag {12}
$$

for  $X = A^{\prime},B^{\prime}$  where  $|i\rangle$  are local orthogonal flags.

The condition FLAGS is very intuitive: if we have a mixture of states with local flags, then it is very reasonable to assume that the mixture has entanglement equal to average entanglement of the states.

Remark 3 In the proof we will not use the fact that the system is bipartite, so that the theorem holds also for multipartite systems. It is also worth mentioning that the condition LUI is usually immediate to verify, so that for convex functions monotonicity is in a sense reduced just to the condition FLAGS.

Proof of equivalence. Let us argue that the Theorems 2 and 3 are equivalent. Since the condition LUI is a restatement of condition (i) of Theorem 2, we need to show that FLAGS is equivalent to conditions (ii) and (iii). First let us see

that the condition FLAGS implies condition (ii) of Theorem 2. To this end, we consider spectral decomposition of the state  $\sigma_{X} = \sum_{k}q_{k}|\phi_{k}\rangle \langle \phi_{k}|.$  Now in condition FLAGS, we take probabilities to be equal to  $q_{k}$ , flags to be  $\phi_{k}$  and the states  $\rho_{AB}^{i} = \rho_{AB}$ , and get the condition (ii). Now let us derive condition (iii). To get it from FLAGS we need the following equality

$$
f \left(\rho_ {A B} ^ {i}\right) = f \left(\rho_ {A B} ^ {i} \otimes | i \rangle_ {X} \langle i |\right). \tag {13}
$$

This however is a consequence of condition (ii), which as we have just shown follows from FLAGS.

Now we need to prove that conditions (ii) and (iii) imply FLAGS. Obviously condition (ii) implies (13), which together with (iii) gives FLAGS. This ends the proof of the equivalence of theorems.

Proof of Theorem 2.  $(\Rightarrow)$  We will first show that from conditions (i)-(iii) we obtain monotonicity. Since our function is assumed to be convex, and by conditions (i) and (ii) is nonincreasing under local unitaries and nonincreasing under adding local ancilla (we also assume that it is nondecreasing under adding local ancilla) it remains to show that it satisfies conditions b) and d) of Theorem 1. Let us first show that  $f$  does not increase under local partial trace. For definiteness let the subsystem be at Bob's site. The initial state is  $\rho_{ABB'}$ , the final state is  $\rho_{AB}$ . Let us note that removing a subsystem can be performed in two stages: first one can apply suitable random unitaries, to turn the state into  $\rho_{AB} \otimes \tau_{B'}$  (where  $\tau_{B'}$  is maximally mixed state on the subsystem  $B'$ ) and then remove completely the decoupled subsystem  $B'$ . In the first stage  $f$  will not increase, because of convexity and LUI. In the second stage it will not increase because of condition (ii).

Now we will prove that  $f$  does not increase under local von Neumann measurement (e.g. on Bob's site). Consider then Bob's von Neumann measurement given by a set of projectors  $\{P_B^i\}$ . Let the measurement transform the state  $\rho_{AB}$  into  $\sigma_{AB}^{i}$  with probability  $p_i$ . Note that it can be performed in the following way:

Bob attaches local ancilla  $B^{\prime}$  in the standard state  $|0\rangle$  
- Bob applies unitary operation  $U_{BB'} = \sum_i P_B^i \otimes U_{B'}^i$ , where  $U_{B'}^i |0\rangle_{B'} = |i\rangle_{B'}$  with  $|i\rangle_{B'}$  being orthonormal basis  
Bob measures the ancilla  $B^{\prime}$  in the basis  $|i\rangle_{B^{\prime}}$  
Bob discards the ancilla, and tells the outcome to Alice.

Given the outcome  $i$  of the measurement on  $B'$ , the state on  $AB$  collapses to the state  $\sigma_{AB}^{i}$ . Now, we will replace the stage of measuring the ancilla with dephasing it in the basis  $|i\rangle_{B'}$ . The dephasing can be performed by applying at random some unitary operations on the system  $B'$ . The resulting total state will be then

$$
\sum_ {i} p _ {i} \sigma_ {A B} ^ {i} \otimes | i \rangle_ {B ^ {\prime}} \langle i |. \tag {14}
$$

Note that during operations leading to this state,  $f$  has not increased. Indeed, the operations are either mixing, or local unitaries, or adding ancilla. In the first case

the function does not increase because of convexity, in the second by condition (i) (LUI), in the third one by condition (ii). Thus

$$
f \left(\rho_ {A B}\right) \geq f \left(\sum_ {i} p _ {i} \sigma_ {A B} ^ {i} \otimes | i \rangle_ {B ^ {\prime}} \langle i |\right). \tag {15}
$$

Now, using (ii) and (iii) we get

$$
f \left(\rho_ {A B}\right) \geq \sum_ {i} p _ {i} f \left(\sigma_ {A B} ^ {i}\right), \tag {16}
$$

which is precisely the condition d).

$(\Leftarrow)$  Let us now prove the converse. Thus we assume that a function is convex and it is LOCC monotone. The condition LUI is simply condition c), and the conditions a) and b) together imply condition (ii), so that it is enough to show that (iii) is implied. The inequality “ $\leq$ ” in the condition follows from the fact that the function is convex. Let us now prove inequality “ $\geq$ ”. This follows immediately from condition d), if one takes the (incomplete) measurement to be the measurement of the flags. This ends the proof.

We will illustrate our theorem by several examples.

EXAMPLE 1 A well known measure of entanglement is negativity [5, 6] given by

$$
E _ {N} (\rho) = \left\| \rho^ {T _ {A}} \right\| _ {1} = \left\| \rho^ {T _ {B}} \right\| _ {1}, \tag {17}
$$

where  $T_{X}$  is the partial transpose performed on subsystem  $X$  [7], and  $\| \cdot \|_1$  is the trace norm. It was shown to be LOCC monotone in the sense of Definition 1 in [6]. A simple proof of monotonicity in the sense of (2) was provided in [8, 9]. Now, using our result, we are able to provide equally simple proofs of stronger monotonicity of Definition 1. Of course, the function  $E_N$  is convex, because partial transpose is linear, and norm is convex. We have to prove the conditions LUI and FLAGS. The condition LUI follows from the fact that partial transpose in a sense commutes with local unitaries. Namely, for unitaries  $U_A$  and  $W_B$  we have

$$
U _ {A} \otimes W _ {B} \rho_ {A B} ^ {T _ {A}} U _ {A} ^ {\dagger} \otimes W _ {B} ^ {\dagger} = \left(U _ {A} \otimes \tilde {W} _ {B} \rho_ {A B} U _ {A} ^ {\dagger} \otimes \tilde {W} _ {B} ^ {\dagger}\right) ^ {T _ {A}}, \tag {18}
$$

where  $\tilde{W}_B$  is again some unitary. Let us now pass to condition FLAGS. First of all, it is easy to see that for operators  $A_{i}$  of disjoint supports we have

$$
\left\| \sum_ {i} A _ {i} \right\| _ {1} = \sum_ {i} \| A _ {i} \| _ {1}. \tag {19}
$$

We will now take  $A_{i} = p_{i}(\rho_{AB}^{i})^{T_{A}} \otimes |i\rangle_{B^{\prime}}\langle i|$ . Because of the orthogonality of flags, the operators have disjoint supports, so that we get

$$
\left\| \sum_ {i} p _ {i} \left(\rho_ {A B} ^ {i}\right) ^ {T _ {A}} \otimes | i \rangle_ {B ^ {\prime}} \langle i | \right\| _ {1} = \sum_ {i} p _ {i} \left\| \left(\rho_ {A B} ^ {i}\right) ^ {T _ {A}} \otimes | i \rangle_ {B ^ {\prime}} \langle i | \right\| _ {1} = \sum_ {i} p _ {i} \| \left(\rho_ {A B} ^ {i}\right) ^ {T _ {A}} \| _ {1} \tag {20}
$$

the last inequality follows from the property of trace norm  $\| A\otimes B\| _1 = \| A\| _1\otimes \| B\| _1$

EXAMPLE 2 Consider the relative entropy of entanglement [2] given by

$$
E _ {R} (\rho) = \inf  _ {\sigma \in S} S (\rho | \sigma), \tag {21}
$$

where  $S$  is the set of separable states, and  $S(\rho|\sigma) = \operatorname{tr} \rho \log \rho - \operatorname{tr} \rho \log \sigma$ . Though the proof of weaker monotonicity (2) is immediate, the proof of stronger monotonicity of Definition 1 is somewhat more involved [2]. However, due to the double convexity of relative entropy, we know that the relative entropy of entanglement is convex. Then we can apply our criteria. LUI follows immediately from the invariance of the set  $S$  under local unitary operations. Let us prove that also FLAGS is satisfied. Again, we have to prove inequality “ $\geq$ ” i.e.,

$$
E _ {r} \left(\sum_ {i} p _ {i} \rho_ {A B} ^ {i} \otimes | i \rangle_ {B ^ {\prime}} \langle i |\right) \geq \sum_ {i} p _ {i} E _ {r} \left(\rho_ {A B} ^ {i}\right). \tag {22}
$$

To see it, consider the quantity

$$
S \left(\sum_ {i} p _ {i} \rho_ {A B} ^ {i} \otimes | i \rangle_ {B ^ {\prime}} \langle i | \mid \sigma_ {A B B ^ {\prime}}\right), \tag {23}
$$

where  $\sigma_{ABB'}$  is an arbitrary separable state. Since relative entropy does not increase under dephasing applied to both its arguments, and the set of separable states is closed under local dephasing, we can dephase the state  $\sigma_{ABB'}$  on subsystem  $B'$  in the basis given by flags  $|i\rangle$  and the obtained state can be only a better candidate for infimum on the lhs of (22). The new state is of the form  $\sum_{i} p_i \sigma_{AB}^i \otimes |i\rangle \langle i|$  where  $\sigma_{AB}^i$  are again separable states. Because of orthogonality of flags we have

$$
S \left(\sum_ {i} p _ {i} \rho_ {A B} ^ {i} \otimes | i \rangle_ {B ^ {\prime}} \langle i | | \sum_ {i} p _ {i} \sigma_ {A B} ^ {i} \otimes | i \rangle_ {B ^ {\prime}} \langle i |\right) = \sum_ {i} p _ {i} S \left(\rho_ {A B} ^ {i} \mid \sigma_ {A B} ^ {i}\right). \tag {24}
$$

Thus for any candidate for infimum of the left-hand-side of inequality (22), we get suitable candidates for infima of its right-hand-side, which proves the inequality.

To summarize, we have shown, that for a convex function, the LOCC monotonicity is equivalent to two simple conditions, local unitary invariance and the condition called FLAGS which, roughly speaking, means that the measure should not go down if we mix states that can be locally distinguished without disturbance. It is rather obvious that the condition is necessary for monotonicity. However it might be surprising that for convex functions satisfying LUI it is also sufficient. It is also interesting, that the conditions are not inequalities, as might be expected from the nature of monotonicity. The only inequality is hidden in the condition of convexity.

Since the condition FLAGS turned out to be so powerful for functions that are convex and satisfy local unitary invariance, we think it can be also considered on its own as an important property in the context of distant lab paradigm. However we should remember that in presence of activation effects [10, 11] we would expect

that it does not hold for distillable entanglement. (The reason is the same for which the latter measure is expected to be nonconvex.) Finally, we hope that the conditions we derived will simplify proofs of monotonicity for new entanglement measures, in particular, it may help to determine, if candidates for entanglement measures proposed in [12] satisfy LOCC monotonicity (though we do not know whether the proposed functions are convex).

We also hope, that the result may increase our understanding of what is actually hidden behind the postulate of nonincreasing under local operations and classical communication.

The author would like to thank Ryszard Horodecki and Barbara Synak for discussion. This paper has been supported by the Polish Ministry of Scientific Research and Information Technology under the (solicited) grant No. PBZ-MIN-008/P03/2003 and by EC grants RESQ, Contract No. IST-2001-37559 and QUPRODIS, Contract No. IST-2001-38877.

# Bibliography

[1] C. H. Bennett, D. P. DiVincenzo, J. Smolin, and W. K. Wootters, Mixed-state entanglement and quantum error correction, Phys. Rev. A 54, 3824 (1997), quant-ph/9604024.  
[2] V. Vedral and M. B. Plenio, Entanglement measures and purification procedures, Phys. Rev. A 57, 1619 (1998), quant-ph/9707035.  
[3] G. Vidal, Entanglement monotones, J. Mod. Opt. 47, 355 (2000), quant-ph/9807077.  
[4] M. Horodecki, Entanglement measures, Quantum Inf. Comp. 1, 3 (2001).  
[5] K. Žyczkowski, P. Horodecki, A. Sanpera, and M. Lewenstein, On the volume of the set of mixed entangled states, Phys. Rev. A 58, 883 (1998), quant-ph/9804024.  
[6] G. Vidal and R. Werner, A computable measure of entanglement, Phys. Rev. A 65, 032314 (2002), quant-ph/0102117.  
[7] A. Peres, Separability criterion for density matrices, Phys. Rev. Lett. 77, 1413, (1996).  
[8] M. Horodecki, P. Horodecki, and R. Horodecki, Asymptotic entanglement manipulations can be genuinely irreversible, Phys. Rev. Lett. 84, 4260 (2000).  
[9] M. Horodecki, P. Horodecki, and R. Horodecki, Erratum: Asymptotic entanglement manipulations can be genuinely irreversible, [Phys. Rev. Lett. 84, 4260 (2000)], Phys. Rev. Lett. 86, 5844 (2001), quant-ph/9912076.  
[10] P. Horodecki, M. Horodecki, and R. Horodecki, Bound entanglement can be activated, Phys. Rev. Lett. 82, 1056 (1999), quant-ph/9806058.  
[11] P. W. Shor, J. Smolin, and B. Terhal, Nonadditivity of bipartite distillable entanglement follows from conjecture on bound entangled werner states, Phys. Rev. Lett. 86, 2681 (2001), quant-ph/0106052.  
[12] M. Horodecki, A. Sen(De), and U. Sen, *Dual entanglement measures based on no local cloning and no local deleting*, Phys. Rev. A **70**, 052326 (2004), quant-ph/0403169.