# Three qubits can be entangled in two inequivalent ways

W. Dur, G. Vidal, and J. I. Cirac

Institut fur Theoretische Physik, Universität Innsbruck, A-6020 Innsbruck, Austria

(Received 26 May 2000; published 14 November 2000)

Invertible local transformations of a multipartite system are used to define equivalence classes in the set of entangled states. This classification concerns the entanglement properties of a single copy of the state. Accordingly, we say that two states have the same kind of entanglement if both of them can be obtained from the other by means of local operations and classical communication (LOCC) with nonzero probability. When applied to pure states of a three-qubit system, this approach reveals the existence of two inequivalent kinds of genuine tripartite entanglement, for which the Greenberger-Horne-Zeilinger state and a  $W$  state appear as remarkable representatives. In particular, we show that the  $W$  state retains maximally bipartite entanglement when any one of the three qubits is traced out. We generalize our results both to the case of higher-dimensional subsystems and also to more than three subsystems, for all of which we show that, typically, two randomly chosen pure states cannot be converted into each other by means of LOCC, not even with a small probability of success.

PACS number(s): 03.67.Hk, 03.65.Bz, 03.65.Ca

# I. INTRODUCTION

The understanding of entanglement is at the very heart of quantum information theory (QIT). In recent years, there has been an ongoing effort to characterize qualitatively and quantitatively the entanglement properties of multiparticle systems. A situation of particular interest in QIT consists of several parties that are spatially separated from each other and share a composite system in an entangled state. This setting requires the parties—which are typically allowed to communicate through a classical channel—to only act locally on their subsystems. But even restricted to local operations assisted with classical communication (LOCC), the parties can still modify the entanglement properties of the system and in particular they can try to convert one entangled state into another. This possibility leads to natural ways of defining equivalence relations in the set of entangled states—where equivalent states are then said to contain the same kind of entanglement—as well as establishing hierarchies between the resulting classes.

For instance, we could agree in identifying any two states which can be obtained from each other with certainty by means of LOCC. Clearly, this criterion is interesting in QIT because the parties can use these two states indistinguishably for exactly the same tasks. It is a celebrated result [1] that, when applied to many copies of a state, this criterion leads to identifying all bipartite pure-state entanglement with that of the Einstein-Podolsky-Rosen (EPR) state  $(1 / \sqrt{2})(|00\rangle + |11\rangle)$  [2]. That is, the entanglement of any pure state  $|\psi\rangle_{AB}$  is asymptotically equivalent, under deterministic LOCC, to that of the EPR state, the entropy of entanglement  $E(\psi_{AB})$  —the entropy of the reduced density matrix of either system  $A$  or  $B$  —quantifying the amount of EPR entanglement contained asymptotically in  $|\psi\rangle_{AB}$ . In contrast, recent contributions have shown that in systems shared by three or more parties, there are several inequivalent forms of entanglement under asymptotic LOCC [3,4].

This paper is essentially concerned with the entanglement properties of a single copy of a state, and thus asymptotic results do not apply here. For single copies it is known that

two pure states  $|\psi \rangle$  and  $|\phi \rangle$  can be obtained with certainty from each other by means of LOCC if and only if they are related by local unitaries (LU) [5,4]. But even in the simplest bipartite systems,  $|\psi \rangle$  and  $|\phi \rangle$  are typically not related by LU, and continuous parameters are needed to label all equivalence classes [6-10]. That is, one has to deal with infinitely many kinds of entanglement. In this context, an alternative, simpler classification would be advisable.

One such classification is possible if we just demand that the conversion of the states is through stochastic local operations and classical communication (SLOCC) [4]; that is, through LOCC but without imposing that it has to be achieved with certainty. In that case, we can establish an equivalence relation stating that two states  $|\psi \rangle$  and  $|\phi \rangle$  are equivalent if the parties have a nonvanishing probability of success when trying to convert  $|\psi \rangle$  into  $|\phi \rangle$ , and also  $|\phi \rangle$  into  $|\psi \rangle$  [11]. This relation has been termed stochastic equivalence in Ref. [4]. Their equivalence under SLOCC indicates that both states are again suited to implement the same tasks of QIT, although this time the probability of a successful performance of the task may differ from  $|\phi \rangle$  to  $|\psi \rangle$ . Notice in addition that since LU are a particular case of SLOCC, states equivalent under LU are also equivalent under SLOCC, the new classification being a coarse graining of the previous one.

The main aim of this work is to identify and characterize all possible kinds of pure-state entanglement of three qubits under SLOCC. Unentangled states, and also those which are product in one party while entangled with respect to the remaining two, appear as expected, to be trivial cases. More surprising is the fact that there are two different kinds of genuine tripartite entanglement. Indeed, we will show that any (nontrivial) tripartite entangled state can be converted, by means of SLOCC, into one of two standard forms, namely either the GHZ state [12]

$$
\left| \mathrm {G H Z} \right\rangle = (1 / \sqrt {2}) (\left| 0 0 0 \right\rangle + \left| 1 1 1 \right\rangle) \tag {1}
$$

or else a second state

$$
| W \rangle = (1 / \sqrt {3}) (| 0 0 1 \rangle + | 0 1 0 \rangle + | 1 0 0 \rangle), \tag {2}
$$

and that this splits the set of genuinely trifold entangled states into two sets which are unrelated under LOCC. That is, we will see that if  $|\psi \rangle$  can be converted into the state  $|\mathrm{GHZ}\rangle$  in Eq. (1) and  $|\phi \rangle$  can be converted into the state  $|W\rangle$  in Eq. (2), then it is not possible to transform, even with only a very small probability of success,  $|\psi \rangle$  into  $|\phi \rangle$  nor the other way round.

The previous result is based on the fact that, unlike the GHZ state, not all entangled states of three qubits can be expressed as a linear combination of only two product states. Remarkably enough, the inequivalence under SLOCC of the states  $|\mathrm{GHZ}\rangle$  and  $|W\rangle$  can alternatively be shown from the fact that the 3-tangle (residual tangle), a measure of tripartite correlations introduced by Coffman et al. [14], does not increase on average under LOCC, as we will prove here.

We will then move to the second main goal of this work, namely the analysis of the state  $|W\rangle$ . It cannot be obtained from a state  $|\mathrm{GHZ}\rangle$  by means of LOCC and thus one could expect, in principle, that it has some interesting, characteristic properties. Recall that in several aspects the GHZ state can be regarded as the maximally entangled state of three qubits. However, if one of the three qubits is traced out, the remaining state is completely unentangled. Thus, the entanglement properties of the state  $|\mathrm{GHZ}\rangle$  are very fragile under particle losses. We will prove that, oppositely, the entanglement of  $|W\rangle$  is maximally robust under disposal of any one of the three qubits, in the sense that the remaining reduced density matrices  $\rho_{AB},\rho_{BC}$ , and  $\rho_{AC}$  retain, according to several criteria, the greatest possible amount of entanglement, compared to any other state of three qubits, either pure or mixed.

We will finally analyze entanglement under SLOCC in more general multipartite systems. We will show that, for most of these systems, there is typically no chance at all to transform locally a given state into some other if they are chosen randomly, because the space of entangled pure states depends on more parameters than those that can be modified by acting locally on the subsystems.

The paper is organized as follows. In Sec. II, we characterize mathematically the equivalence relation established by stochastic conversions under LOCC, and illustrate its performance by applying it to the well-known bipartite case. In Sec. III, we move to consider a system of three qubits, for which we prove the existence of six classes of states under SLOCC, including the two genuinely tripartite ones. Section IV is devoted to studying the endurance of the entanglement of the state  $|W\rangle$  against particle losses. In Sec. V, more general multipartite systems are considered. Section VI contains some conclusions. Finally, Appendices A-C prove, respec

tively, some needed results related to SLOCC, the monotonicity of the 3-tangle under LOCC, and the fact that  $|W\rangle$  retains optimally bipartite entanglement when one qubit is traced out.

# II. KINDS OF ENTANGLEMENT UNDER STOCHASTIC LOCC

In this work we define as equivalent the entanglement of two states  $|\psi \rangle$  and  $|\phi \rangle$  of a multipartite system iff local protocols exist that allow the parties to convert each of the two states into the other one with some a priori probability of success. In this approach, we follow the definition for stochastic equivalence as given in [4]. The underlying motivation for this definition is that, if the entanglement of  $|\psi \rangle$  and  $|\phi \rangle$  is equivalent, then the two states can be used to perform the same tasks, although the probability of a successful performance of the task may depend on the state that is being used.

# A. Invertible local operators

Sensible enough, this classification would remain useless if in practice we would not be able to find out which states are related by SLOCC. Let us recall that, all in all, no practical criterion is known so far that determines whether a generic transformation can be implemented by means of LOCC. However, we can think of any local protocol as a series of rounds of operations, where in each round a given party manipulates locally its subsystem and communicates classically the result of its operation (if it included a measurement) to the rest of the parties. Subsequent operations can be made dependent on previous results and the protocol splits into several branches. This picture is useful because for our purposes we need only focus on one of these branches. Suppose that state  $|\psi \rangle$  can be locally converted into state  $|\phi \rangle$  with nonzero probability. This means that at least one branch of the protocol does the job. Since we are concerned only with pure states, we can always characterize mathematically this branch as an operator which factors out as the tensor product of a local operator for each party. For instance, in a three-qubit case we would have that  $|\psi \rangle$  can be locally converted into  $|\phi \rangle$  with some finite probability iff an operator  $A \otimes B \otimes C$  exists such that

$$
\left| \phi \right\rangle = A \otimes B \otimes C | \psi \rangle , \tag {3}
$$

where operator  $A$  contains contributions coming from any round in which party  $A$  acted on its subsystem, and similarly for operators  $B$  and  $C$ . Carrying on with the three-qubit example, let us now consider for simplicity that both states

$|\psi \rangle$  and  $|\phi \rangle$  have rank two reduced density matrices  $\rho_{A}\equiv \mathrm{tr}_{BC}(|\psi \rangle \langle \psi |)$ ,  $\rho_{B}$ , and  $\rho_{C}$ . Then clearly the rank of operators  $A, B$ , and  $C$  needs to be 2 (see Appendix A). In other words, each of these operators is necessarily invertible, and in particular

$$
\left| \psi \right\rangle = A ^ {- 1} \otimes B ^ {- 1} \otimes C ^ {- 1} \mid \phi \rangle . \tag {4}
$$

Thus we see that, under the assumption of maximal rank for the reduced density matrices, two-way convertibility implies the existence of invertible operators  $A$ ,  $B$ , and  $C$  as in Eq. (3) [actually, one-way convertibility alone has already implied that an invertible local operator (ILO)  $A \otimes B \otimes C$  exists]. Obviously, the converse also holds, namely that if an ILO  $A \otimes B \otimes C$  exists, then for each direction of the conversion a local protocol can be built that succeeds with nonzero probability. As explained in Appendix A in detail, we can get rid of the previous assumption on the ranks and announce with generality the following.

Result. States  $|\psi \rangle$  and  $|\phi \rangle$  are equivalent under SLOCC if an ILO relating them [as in, for instance, Eq. (3)] exists.

# B. Bipartite entanglement under SLOCC

What does this classification imply in the well-known case [15-17] of bipartite systems? Since LU are included in SLOCC, we can take the Schmidt decomposition of a pure state  $|\psi \rangle \in \mathbb{C}^n\otimes \mathbb{C}^m$ $n\leqslant m$  , as the starting point for our analysis. Thus,

$$
\sum_ {i = 1} ^ {n _ {\psi}} \sqrt {\lambda_ {i}} | i \rangle \otimes | i \rangle = U _ {A} \otimes U _ {B} | \psi \rangle , \quad \lambda_ {i} > 0, n _ {\psi} \leqslant n, \tag {5}
$$

where  $U_{A}$  and  $U_{B}$  are some proper local unitaries, the coefficients  $\lambda_{i}$  decrease with  $i$ , and  $n_{\psi}$  is the number of nonvanishing terms in the Schmidt decomposition. Clearly, the ILO

$$
\frac {1}{\sqrt {n _ {\psi}}} \left(\sum_ {i = 1} ^ {n _ {\psi}} \frac {1}{\sqrt {\lambda_ {i}}} | i \rangle \langle i | + \sum_ {i = n _ {\psi} + 1} ^ {n} | i \rangle \langle i |\right) \otimes 1 _ {B} \tag {6}
$$

transforms Eq. (5) into a maximally entangled state

$$
\frac {1}{\sqrt {n _ {\psi}}} \sum_ {i} ^ {n _ {\psi}} | i \rangle \otimes | i \rangle , \tag {7}
$$

which depends only on the Schmidt number  $n_{\psi}$ . Since SLOCC cannot modify the rank of the reduced density matrices  $\rho_{A}$  and  $\rho_{B}$ , which is given by  $n_{\psi}$ , we conclude that in  $\mathbb{C}^n \otimes \mathbb{C}^m$ ,  $n \leqslant m$ , there are  $n$  different kinds of entangled states, corresponding to  $n$  different classes under SLOCC. Each of these classes is characterized by a given Schmidt number, and we can choose as their representatives the state (7) with  $n_{\psi} = 1, \ldots, n$ . Clearly,  $n_{\psi} = 1$  corresponds to states that are less entangled than the rest (they are, after all, unentangled). This hierarchical relation can be extended to the rest of the classes by noting that noninvertible local operators can project out some of the Schmidt terms and thus diminish the Schmidt number of a state. Therefore, the state  $|\psi\rangle$  can be locally converted into the state  $|\phi\rangle$  with some finite prob

ability iff  $n_{\psi} \geqslant n_{\phi}$ , or in terms of kinds of entanglement, we can say that the entanglement of the class characterized by a given Schmidt number is more powerful than that of a class with a smaller Schmidt number.

For later reference we also note that in a two-qubit system,  $\mathcal{H} = \mathbb{C}^2\otimes \mathbb{C}^2$ , we can write any state, after using a convenient LU, uniquely as

$$
| \psi \rangle = c _ {\delta} | 0 \rangle \otimes | 0 \rangle + s _ {\delta} | 1 \rangle \otimes | 1 \rangle , \quad c _ {\delta} \geqslant s _ {\delta} \geqslant 0, \tag {8}
$$

where  $c_{\delta}, s_{\delta}$  stand for  $\cos \delta$  and  $\sin \delta$ . This is either a product (unentangled) state  $|\psi_{A - B}\rangle = |0\rangle \otimes |0\rangle$  for  $c_{\delta} = 1$  or else an entangled state that can be converted into the EPR state,

$$
\frac {1}{\sqrt {2}} \left(\left| 0 \right\rangle \otimes \left| 0 \right\rangle + \left| 1 \right\rangle \otimes \left| 1 \right\rangle\right), \tag {9}
$$

with probability  $p = E_2(\psi)$ , where  $E_2(\psi) \equiv \lambda_2$  is the entanglement monotone that provides a quantitative description of the nonlocal resources contained in a single copy of a two-qubit pure state [18]. Any state  $|\psi\rangle$  can be obtained from state (9) with certainty, this contributing to the fact that the EPR state is considered the maximally entangled state of two qubits.

# III. ENTANGLEMENT OF PURE STATES OF THREE QUBITS

In this section, we analyze a system of three qubits. We show that SLOCC split the set of pure states into six inequivalent classes, which further structure themselves into a three-grade hierarchy when noninvertible local operations are used to relate them. At the top of the hierarchy we find two inequivalent classes of true tripartite entanglement, which we name GHZ class and  $W$  class after our choice of corresponding representatives. The three possible classes of bipartite entanglement are accessible (with some nonvanishing probability) from any state of the  $W$  and GHZ classes by means of a noninvertible local operator. Finally, at the bottom of the hierarchy we find nonentangled states.

The ranks  $r(\rho_A)$ ,  $r(\rho_B)$ , and  $r(\rho_C)$  of the reduced density matrices, together with the range  $R(\rho_{BC})$  of  $\rho_{BC}$ , will be the main mathematical tools used through the first part of this section. By analyzing them we will be able to make an exhaustive classification of three-qubit entanglement. Later on we will rephrase some of these results in terms of well-known measures of entanglement. In particular, we will see that the existence of two inequivalent kinds of true tripartite entanglement under SLOCC is very much related to the fact that the 3-tangle, a measure of tripartite entanglement introduced in [14], is an entanglement monotone (see Appendix B).

At the end of the section also a practical way to identify the class that an arbitrary state belongs to will be discussed.

# A. Nonentangled states and bipartite entanglement

If at least one of the local ranks  $r(\rho_A)$ ,  $r(\rho_B)$ , or  $r(\rho_C)$  is 1, then the pure state of the three qubits factors out as the tensor product of two pure states, and this implies that at

least one of the qubits is uncorrelated with the other two. SLOCC distinguish states with this feature depending on which qubits are uncorrelated from the rest.

# 1. Class  $A - B - C$  (product states)

This class corresponds to states with  $r(\rho_A) = r(\rho_B) = r(\rho_C) = 1$ . They can be taken, after using some convenient LU, into the form

$$
\left| \psi_ {A - B - C} \right\rangle = | 0 \rangle | 0 \rangle | 0 \rangle , \tag {10}
$$

where we have already relaxed the notation for  $|0\rangle \otimes |0\rangle$ $\otimes |0\rangle$

# 2. Classes  $A - BC, AB - C,$  and  $C - AB$  (bipartite entanglement)

These three classes of states contain only bipartite entanglement between two of the qubits, one of the reduced density matrices having rank 1 and the other two having rank 2. For example, the states in class  $A - BC$  possess entanglement between the systems  $B$  and  $C$ $[r(\rho_B) = r(\rho_C) = 2]$  and are product with respect to system  $A$ $[r(\rho_A) = 1]$ . LU allows us to write uniquely states of the class  $A - BC$  as

$$
\left| \psi_ {A - B C} \right\rangle = | 0 \rangle \left(c _ {\delta} | 0 \rangle | 0 \rangle + s _ {\delta} | 1 \rangle | 1 \rangle\right), \quad c _ {\delta} \geqslant s _ {\delta} > 0, \tag {11}
$$

and similarly for  $|\psi_{B - AC}\rangle$  and  $|\psi_{C - AB}\rangle$ . We choose the maximally entangled state

$$
\frac {1}{\sqrt {2}} | 0 \rangle (| 0 \rangle | 0 \rangle + | 1 \rangle | 1 \rangle) \tag {12}
$$

as representative of the class  $A - BC$ . Any other state within this class can be obtained from (12) with certainty by means of LOCC.

The proof that these four marginal classes are inequivalent under SLOCC is very simple. We only need to recall that the local ranks are invariant under ILO (see Appendix A). In what follows we will analyze the more interesting case of  $r(\rho_{\kappa}) = 2$ ,  $\kappa = A, B, C$ . To see that there are two inequivalent classes fulfilling this condition, we will have to study possible product decompositions of pure states.

# B. True three-qubit entanglement

There turns out to be a close connection between convertibility under SLOCC and the way entangled states can be expressed minimally as a linear combination of product states. For instance, as we shall prove later on, the GHZ and  $W$  states have a different number of terms in their minimal product decompositions (1) and (2), namely two and three product terms, respectively, and this readily implies that there is no way to convert one state into the other by means of an ILO  $A \otimes B \otimes C$ . Indeed, let us consider, e.g., the most general pure state that can be obtained reversibly from a  $\left|\mathrm{GHZ}\right\rangle$ . It reads

$$
A \otimes B \otimes C | \mathrm {G H Z} \rangle = \frac {1}{\sqrt {2}} (| A 0 \rangle | B 0 \rangle | C 0 \rangle + | A 1 \rangle | B 1 \rangle | C 1 \rangle), \tag {13}
$$

where  $|A0\rangle$  and  $|A1\rangle$  are linearly independent vectors (since  $A$  is invertible) and similarly for the other two qubits. That is, the minimal number of terms in a product decomposition for the state (13) is also 2. Actually, we observe the following for a general multipartite system.

Observation. The minimal number of product terms for any given state remains unchanged under SLOCC.

This simple observation tells us already that in three qubits there are at least two inequivalent kinds of genuine tripartite entanglement under SLOCC, that of  $|\mathrm{GHZ}\rangle$  and that of  $|W\rangle$ .

However, we still have to prove that the state  $|W\rangle$  cannot be expressed as a linear combination of just two product vectors. In order to complete our classification, we also have to show that any pure state of three qubits with maximal local ranks can be reversibly converted into either the state  $|\mathrm{GHZ}\rangle$  or the state  $|W\rangle$ . We start with an obvious lemma regarding product decompositions.

Lemma. Let  $\Sigma_{i=1}^{l}|e_i\rangle|f_i\rangle$  be a product decomposition for the state  $|\eta\rangle\in\mathcal{H}_E\otimes\mathcal{H}_F$ . Then the set of states  $\{|e_i\rangle\}_{i=1}^l$  spans the range of  $\rho_E\equiv\mathrm{Tr}_F|\eta\rangle\langle\eta|$ .

Proof. We have that  $\rho_{E} = \Sigma_{i,j=1}^{l}\langle f_{i}|f_{j}\rangle|e_{j}\rangle\langle e_{i}|$ . On the other hand,  $|\nu\rangle$  is in the range of  $\rho_{E}$  if a state  $|\mu\rangle$  exists such that  $|\nu\rangle = \rho_{E}|\mu\rangle$ , that is,  $|\nu\rangle = \Sigma_{i,j=1}^{l}\langle f_{i}|f_{j}\rangle\langle e_{i}|\mu\rangle|e_{j}\rangle$ .

In particular,  $r(\rho_A) = 2$  implies that at least two product terms are needed to expand  $\left|\psi \right\rangle \in \mathbb{C}^2\otimes \mathbb{C}^2\otimes \mathbb{C}^2$  . Let us suppose that a product decomposition with only two terms is possible, namely

$$
| \psi \rangle = | a _ {1} \rangle | b _ {1} \rangle | c _ {1} \rangle + | a _ {2} \rangle | b _ {2} \rangle | c _ {2} \rangle . \tag {14}
$$

Then, also according to the previous lemma,  $|b_{1}\rangle |c_{1}\rangle$  and  $|b_{2}\rangle |c_{2}\rangle$  have to span the range of  $\rho_{BC}$ ,  $R(\rho_{BC})$ .

But  $R(\rho_{BC})$  is a two-dimensional subspace of  $\mathbb{C}^2 \otimes \mathbb{C}^2$ . Therefore, it always contains either only one or only two product states [19] [unless  $R(\rho_{BC})$  was supported in  $\mathbb{C} \otimes \mathbb{C}^2$  or  $\mathbb{C}^2 \otimes \mathbb{C}$ , but we already excluded this possibility because we are considering  $r(\rho_B) = r(\rho_C) = 2$ ]. Notice that a two-term decomposition (14) requires that  $R(\rho_{BC})$  contain at least two product vectors. Only one product vector in  $R(\rho_{BC})$ , and thus the impossibility of decomposition (14), is going to be precisely the trait of the states in the  $W$  class.

# 1. GHZ class

Let us suppose first that  $R(\rho_{BC})$  contains two product vectors,  $|b_1\rangle |c_1\rangle$  and  $|b_2\rangle |c_2\rangle$ . Then decomposition (14) is possible, and actually unique, with  $|a_i\rangle = \langle \xi_i|\psi \rangle$ ,  $i = 1,2$ , where  $|\xi_i\rangle$  are the two vectors supported in  $R(\rho_{BC})$  that are biorthonormal to the  $|b_i\rangle |c_i\rangle$ . In this case we can use LU in order to take  $|\psi \rangle$  into the useful standard product form (see also [20])

$$
\left| \psi_ {\mathrm {G H Z}} \right\rangle = \sqrt {K} \left(c _ {\delta} | 0 \rangle | 0 \rangle | 0 \rangle + s _ {\delta} e ^ {i \varphi} \left| \varphi_ {A} \right\rangle \mid \varphi_ {B} \right\rangle \left| \varphi_ {C} \right\rangle), \tag {15}
$$

where

$$
\left| \varphi_ {A} \right\rangle = c _ {\alpha} \left| 0 \right\rangle + s _ {\alpha} \left| 1 \right\rangle ,
$$

$$
\left| \varphi_ {B} \right\rangle = c _ {\beta} | 0 \rangle + s _ {\beta} | 1 \rangle , \tag {16}
$$

$$
\left| \varphi_ {C} \right\rangle = c _ {\gamma} \left| 0 \right\rangle + s _ {\gamma} \left| 1 \right\rangle ,
$$

and  $K = (1 + 2c_{\delta}s_{\delta}c_{\alpha}c_{\beta}c_{\gamma}c_{\varphi})^{-1}\in (\frac{1}{2},\infty)$  is a normalization factor. The ranges for the five parameters are  $\delta \in (0,\pi /4],\alpha ,\beta ,\gamma \in (0,\pi /2]$  and  $\varphi \in [0,2\pi)$ .

All these states are in the same equivalence class as the  $|\mathrm{GHZ}\rangle$  (1) under SLOCC. Indeed, the ILO

$$
\sqrt {2 K} \left( \begin{array}{l l} c _ {\delta} & s _ {\delta} c _ {\alpha} e ^ {i \varphi} \\ 0 & s _ {\delta} s _ {\alpha} e ^ {i \varphi} \end{array} \right) \otimes \left( \begin{array}{c c} 1 & c _ {\beta} \\ 0 & s _ {\beta} \end{array} \right) \otimes \left( \begin{array}{c c} 1 & c _ {\gamma} \\ 0 & s _ {\gamma} \end{array} \right) \tag {17}
$$

applied to  $|\mathrm{GHZ}\rangle$  produces the state (15).

The GHZ state is a remarkable representative of this class. It is maximally entangled in several senses [21]. For instance, it maximally violates Bell-type inequalities, the mutual information of measurement outcomes is maximal, it is maximally stable against (white) noise, and one can locally obtain from a GHZ state with unit probability an EPR state shared between any two of the three parties. Another relevant feature is that when any one of the three qubits is traced out, the remaining two are in a separable—and therefore unentangled—state.

# 2. W class

Let us move to analyze the case where  $R(\rho_{BC})$  contains only one product vector. We already argued that decomposition (14) is now not possible. Instead we can (uniquely) write

$$
| \psi \rangle = | a _ {1} \rangle | b _ {1} \rangle | c _ {1} \rangle + | a _ {2} \rangle | \phi_ {B C} \rangle , \tag {18}
$$

where  $|\phi_{BC}\rangle$  is the vector of  $R(\rho_{BC})$  which is orthogonal to  $|b_1\rangle |c_1\rangle$ , and  $|a_1\rangle$  and  $|a_2\rangle$  are given by  $\langle b_1|\langle c_1|\psi \rangle$  and  $\langle \phi_{BC}|\psi \rangle$ . By means of LU, Eq. (18) can always be rewritten as

$$
| \psi \rangle = (\sqrt {c} | 1 \rangle + \sqrt {d} | 0 \rangle) | 0 0 \rangle + | 0 \rangle (\sqrt {a} | 0 1 \rangle + \sqrt {b} | 1 0 \rangle). \tag {19}
$$

Indeed, we first take  $|b_{1}\rangle |c_{1}\rangle$  into  $|0\rangle |0\rangle$ . Then, since  $|\phi_{BC}\rangle$  has been chosen orthogonal to  $|b_{1}\rangle |c_{1}\rangle$ , it must become  $x|01\rangle +y|10\rangle +z|11\rangle$ . By requiring that a linear combination of these two vectors has no second product vector, we obtain that  $z = 0$  [22]. In addition, the coefficients  $\sqrt{a} \equiv x$ ,  $\sqrt{b} \equiv y$ ,  $\sqrt{c}$ , and  $\sqrt{d}$  can be made positive by absorbing the three relative phases into the definition of state  $|1\rangle$  of subsystems  $A$ ,  $B$ , and  $C$ . Thus case (i) has been taken into the form (19) by just using LU. Before we showed that two terms could not suffice in a product decomposition of the state. Now we see that three product terms always do the job, for instance  $(\sqrt{c}|1\rangle +\sqrt{d}|0\rangle)|00\rangle$ ,  $\sqrt{a}|0\rangle |01\rangle$ , and  $\sqrt{b}|0\rangle |10\rangle$  once we took the original state into the standard, unique form

$$
\left| \psi_ {W} \right\rangle = \sqrt {a} | 0 0 1 \rangle + \sqrt {b} | 0 1 0 \rangle + \sqrt {c} | 1 0 0 \rangle + \sqrt {d} | 0 0 0 \rangle , \tag {20}
$$

where  $a,b,c > 0$  and  $d\equiv 1 - (a + b + c)\geqslant 0$

The parties can locally obtain the state (20) from the state  $|W\rangle$  in Eq. (2), which we choose as a representative of the class—and whose study we postpone for later on—by application of an ILO of the form

$$
\left( \begin{array}{c c} \sqrt {a} & \sqrt {d} \\ 0 & \sqrt {c} \end{array} \right) \otimes \left( \begin{array}{c c} \sqrt {3} & 0 \\ 0 & \frac {\sqrt {3 b}}{\sqrt {a}} \end{array} \right) \otimes \left( \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right). \tag {21}
$$

Before moving to relate these classes by means of noninvertible local operators, we note that states within the GHZ class and the  $W$  class depend, respectively, on five and three parameters that cannot be changed by means of LU. Previous works [6,7,20,9] have shown that a generic state of three qubits depends, up to LU, on five parameters. This means that states typically belong to the GHZ class, or equivalently, that a generic pure state of three qubits can be locally transformed into a GHZ with a finite probability of success (see also [23]). The  $W$  class is of zero measure compared to the GHZ class. This does not mean, however, that it is irrelevant. In a similar way as separable mixed states are not of zero measure with respect to entangled states, even though product states are, it is in principle conceivable that mixed states having only  $W$ -class entanglement are also not of zero measure in the set of mixed states.

# C. Relating SLOCC classes by means of noninvertible operators

In this subsection, we investigate the hierarchical relation of the six SLOCC-equivalence classes under noninvertible operators, i.e., under general LOCC.

A noninvertible local operator transforms  $|\psi \rangle$  into  $|\phi \rangle$  according to Eq. (3), but with at least one of the local operators  $A, B,$  and  $C$  having rank 1. This means that the local ranks of the pure states can be diminished. For instance, if the initial state  $|\psi \rangle$  belongs either to the GHZ or  $W$  class, then a noninvertible operator will diminish at least one of the local ranks. That is,  $|\phi \rangle$  belongs necessarily to one of the bipartite classes  $\kappa - \mu \nu$  ( $\kappa \neq \mu \neq \nu \in \{A, B, C\}$ ) or else is a product state  $A - B - C$ .

Thus we have that the classes GHZ and  $W$  are also inequivalent even under most general LOCC, whereas, e.g., a measurement of the projector  $P = | + \rangle \langle +|$  with  $| + \rangle$ $= 1 / \sqrt{2} (|0\rangle +|1\rangle)$  in party  $A$  maps states within the classes  $W$  (20) and GHZ (15) to states within the class  $A - BC$ . In a similar way, noninvertible local operators (local, standard measurements) can convert states within one of the classes  $\kappa -\mu \nu$  to states within the class  $A - B - C$ . Note that in all cases described above, the inverse transformations, e.g., from the class  $A - B - C$  to one of the classes  $\kappa -\mu \nu$ , are impossible as they would imply an increase of the rank of at least one of the reduced density operators  $\rho_{A},\rho_{B},\rho_{C}$ . These results are summarized in Fig. 1.

![](images/c5c7ef8c98e0095f45b79e3121d5b3420bb4453ccc4d43d0abcbc502c86ddac4.jpg)  
FIG. 1. Different local classes of tripartite pure states. The direction of the arrows indicates which noninvertible transformations between classes are possible.

# D. Measures of entanglement and classes under SLOCC

Several measures have been introduced so far in the literature in order to quantify entanglement. Although this section is mainly concerned with qualitative aspects of multipartite quantum correlations, we would like to relate some of these measures, namely some bipartite ones and the tripartite 3-tangle [14] (see Appendix B), to our classification. Remarkably, the existence of two kinds of genuine tripartite entanglement in a three-qubit system, as well as the inequivalence between bipartite and tripartite entanglement, can be easily understood from the nonincreasing character of these measures under LOCC. In addition, the 3-tangle allows for a systematic and practical identification of to which class under SLOCC any pure state belongs.

For each  $\kappa = A$ ,  $B$ , and  $C$  we can regard the three-qubit system as a bipartite system, with qubit  $\kappa$ , say  $A$  for concreteness, being one part of the system and the remaining two qubits,  $B$  and  $C$ , being the other. Correspondingly, a state  $|\psi\rangle$  of the three qubits can be viewed as a bipartite state  $|\psi_{A(BC)}\rangle$ . For bipartite states several measures are known, which are entanglement monotones [5], that is, which cannot be increased, on average, under LOCC. For instance, we already mentioned the entropy of entanglement  $E(\psi)$  for asymptotic conversions—given by the entropy  $S_A$  of the eigenvalues of  $\rho_A$ —and the monotone  $E_2(\psi)$  for the single copy case, which is given by the smallest eigenvalue  $\lambda_2$  of  $\rho_A$ . They all vanish for product states (corresponding to  $\rho_A$  with rank 1) while having a positive value for any other state (corresponding to  $\rho_A$  with rank 2). Thus we can interpret the inequivalence under SLOCC of states whose reduced density matrices differ in rank also in terms of the impossibility of creating any of the bipartite measures. For instance, a state in the  $A - BC$  class has  $S_A = 0$ , and thus cannot be transformed with any finite probability into a state of the  $AB - C$  class, because this would have  $S_A > 0$ . We conclude that the monotonicity of these measures readily split the set of pure states of three qubits into five subsets which are inequivalent under SLOCC, namely unentangled states  $A - B - C$ , the three classes  $A - BC$ ,  $AB - C$ , and  $C - AB$  containing only bipartite entanglement, and a fifth subset of entangled states with  $S_A, S_B, S_C \neq 0$  [i.e.,  $r(\rho_A) = r(\rho_B) = r(\rho_C) = 2$ ]. Bipartite measures cannot, however, determine the inequivalence of the GHZ and  $W$  classes.

Is there any known measure of tripartite entanglement which can distinguish between these two classes? The 3-tangle does. Indeed, it can be computed from the product decompositions (15) and (20) (see [14] for details), and reads

TABLE I. Values of the local entropies  $S_A, S_B, S_C$  and the 3-tangle  $\tau$  for the different classes.  

<table><tr><td>Class</td><td>SA</td><td>SB</td><td>SC</td><td>τ</td></tr><tr><td>A-B-C</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>A-BC</td><td>0</td><td>&gt;0</td><td>&gt;0</td><td>0</td></tr><tr><td>B-AC</td><td>&gt;0</td><td>0</td><td>&gt;0</td><td>0</td></tr><tr><td>C-AB</td><td>&gt;0</td><td>&gt;0</td><td>0</td><td>0</td></tr><tr><td>W</td><td>&gt;0</td><td>&gt;0</td><td>&gt;0</td><td>0</td></tr><tr><td>GHZ</td><td>&gt;0</td><td>&gt;0</td><td>&gt;0</td><td>&gt;0</td></tr></table>

$$
\tau \left(\psi_ {\mathrm {G H Z}}\right) = \left(2 K s _ {\alpha} s _ {\beta} s _ {\gamma} s _ {\delta} c _ {\delta}\right) ^ {2} \neq 0 \tag {22}
$$

for any state in the GHZ class, while it vanishes for any state in the  $W$  class. In Appendix B we prove that the 3-tangle is an entanglement monotone, a very desirable property for any quantity aiming at measuring entanglement. Consequently, a state in the  $W$  class cannot be transformed by means of LOCC (and in particular SLOCC) to a state in the GHZ class, which is an independent proof of the fact that the two kinds of true tripartite entanglement are indeed inequivalent under SLOCC.

# E. Practical identification

Given an arbitrary state  $|\psi \rangle$  of three qubits, expressed in any basis, it may be interesting to know, for instance, whether it can be converted by means of LOCC into a GHZ or a  $W$  state, if any, or into an EPR state shared between two of the parties. In our original analysis of the classes, we have already provided a constructive method, based on the analysis of  $r(\rho_{\kappa})$  and  $R(\rho_{BC})$ , to determine the class of  $|\psi \rangle$  under SLOCC. Analyzing the  $R(\rho_{BC})$  may, however, not be the most practical way to proceed. Here we suggest to proceed instead according to the following two steps.

(i) Compute  $\rho_{\kappa}$ ,  $\kappa = A, B$ , and  $C$ , and check whether they have a vanishing determinant [note that  $\operatorname{det} \rho_{\kappa} = 0 \Leftrightarrow S_{\kappa} = 0 \Leftrightarrow r(\rho_{\kappa}) = 1$ ].  
(ii) If none of the previous determinants vanish (that is,  $|\psi \rangle$  has true tripartite entanglement), then compute the 3-tangle using the recipe introduced in [14].

Then Table I, which summarizes the relation between classes under SLOCC and measures of entanglement, can be used to catalog state  $|\psi \rangle$ .

# IV. STATE  $|W\rangle$  AND RESIDUAL BIPARTITE ENTANGLEMENT

As mentioned in the preceding section, in several aspects the state  $|\mathrm{GHZ}\rangle$  is the maximally entangled state of three qubits. It also has the feature that when one of the qubits is traced out, then the remaining two are completely unentangled. This means, in particular, that if one of the three parties sharing the system decides not to cooperate with the other two, then they cannot use the entanglement resources

of the state at all. The same happens if for some reason the information about one of the qubits—namely the identity of the corresponding states  $|0\rangle$  and  $|1\rangle$  in (1)—is lost.

Here we would like to investigate the robustness of the entanglement of a three-qubit state  $|\psi \rangle$  against disposal of one of the qubits [24]. The residual, two-qubit states  $\rho_{AB}$ ,  $\rho_{AC}$ , and  $\rho_{BC}$  are in general mixed states. There are several measures of entanglement of mixed states and therefore multiple ways of quantifying how much (mixed-state) bipartite entanglement the state  $|\psi \rangle$  turns into when one of the qubits is traced out. Nevertheless, most of the criteria we have examined coincide in pointing out the state  $|W\rangle$  as the one that maximally retains bipartite entanglement. Note that the reduced density matrix of  $|W\rangle$  is identical for any two subsystems and is, e.g., given by

$$
\rho_ {A B} = \frac {2}{3} | \Psi^ {+} \rangle \langle \Psi^ {+} | + \frac {1}{3} | 0 0 \rangle \langle 0 0 |, \tag {23}
$$

with  $|\Psi^{+}\rangle = (1 / \sqrt{2})(|01\rangle + |10\rangle)$  being a maximally entangled state of two qubits. Note that one can obtain from a single copy of Eq. (23) a state which is arbitrarily close to the state  $|\Psi^{+}\rangle$  by means of a filtering measurement [25].

# A. Average residual entanglement

Let us consider first which is the amount of bipartite entanglement, according to some measure  $\mathcal{E}(\rho)$ , that the two remaining qubits retains on average when a third one is traced out, that is,

$$
\bar {\mathcal {E}} (\psi) \equiv \frac {1}{3} \left[ \mathcal {E} \left(\rho_ {A B}\right) + \mathcal {E} \left(\rho_ {A C}\right) + \mathcal {E} \left(\rho_ {B C}\right) \right]. \tag {24}
$$

In general, computing the amount of entanglement  $\mathcal{E}(\rho)$  for bipartite mixed states is a difficult problem. However, numerical results have shown that  $|W\rangle$  maximizes the average entanglement of formation, that is the choice  $\mathcal{E}(\rho) = E_f(\rho)$ , where  $E_{f}(\rho)^{5}$  is the minimal amount of bipartite pure-state entanglement [as quantified by means of the entropy of entanglement] required to prepare locally one single copy of the state  $\rho$  [26].

In addition, we have managed to show analytically (see Appendix C) for the particular choice  $\mathcal{E}(\rho) = \mathcal{C}(\rho)^2$ , where  $\mathcal{C}(\rho)$  is the concurrence (for a definition of the concurrence, see, e.g., [14]), that the state  $|W\rangle$  reaches the maximal average value  $\overline{\mathcal{C}}^2(W) = \frac{4}{9}$ , which no other state can match.

# B. Least entangled pair

Another way of quantifying how resilient the entanglement of a tripartite state  $|\psi \rangle$  is to the dismissal of one part of the system consists in looking at the least entangled of the three possible remaining parts, namely at the function

$$
\mathcal {E} _ {\min } (\psi) \equiv \min  \left(\mathcal {E} \left(\rho_ {A B}\right), \mathcal {E} \left(\rho_ {A C}\right), \mathcal {E} \left(\rho_ {B C}\right)\right). \tag {25}
$$

For this "worst case scenario" we have been able to prove analytically (see Appendix C) that the maximal value of  $\mathcal{E}_{\min}(\psi)$  is obtained by the state  $|W\rangle$  for any bipartite measure  $\mathcal{E}(\rho)$  which is monotonic with the concurrence,  $\mathcal{C}(\rho)$ , such as the entanglement of formation  $E_{f}(\rho)$  and the monotone  $E_{2}(\rho)$ , which denotes the minimal amount of bipartite pure-state entanglement [quantified by means of  $E_{2}(\psi)$ ] required to prepare locally one single copy of the state  $\rho$ .

We conclude that the state  $|W\rangle$  is the state of three qubits whose entanglement has the highest degree of endurance against loss of one of the three qubits. We conceive this property as important in any situation where one of the three parties sharing the system, say Alice, may suddenly decide not to cooperate with the other two. Notice that even in the case that Alice would decide to try to destroy the entanglement between Bob and Claire, this would not be possible, since any local action on  $A$  cannot prevent Bob and Claire from sharing, at least, the entanglement contained in  $\rho_{BC}$  (for instance, by simply ignoring Alice's actions). Therefore, although essentially tripartite, the entanglement of the state  $|W\rangle$  is also readily bipartite, in contrast to that of the state  $|\mathrm{GHZ}\rangle$ , which only after some local manipulation can be brought into a bipartite form.

# V. GENERALIZATION TO  $N$  PARTIES

In this final section, we would like to apply the same techniques to analyze the entanglement of more general multipartite systems. We will learn that the set of entangled states is a rather inaccessible jungle for the local explorer, for two pure states  $|\psi \rangle$  and  $|\phi \rangle$  are typically not connected by means of LOCC, so that the parties are usually unable to convert states locally. We will also study generalizations to  $N$  qubits of the state  $|W\rangle$ .

# A. Local inaccessibility of states in general multipartite systems

Let us consider first  $N$  parties each possessing a qubit. The Hilbert space of the system is

$$
\mathcal {H} ^ {(N)} = \underbrace {\mathbb {C} ^ {2} \otimes \mathbb {C} ^ {2} \otimes \cdots \otimes \mathbb {C} ^ {2}} _ {N}, \tag {26}
$$

and therefore up to a global, physically irrelevant complex constant, a generic vector depends on  $2(2^{N} - 1)$  real parameters. On the other hand, we want to identify vectors which are related by means of an ILO. A general one-party, invertible operator  $A$  must have a nonvanishing determinant, which we can fix to one,  $\operatorname{det}A = 1$ , because the operator  $kA$  only differs in that it introduces in the transformed states an extra constant factor  $k \in \mathbb{C}$ , which we have already addressed. That is,  $A \in SL_2(\mathbb{C})$ , and it depends on six real parameters. There-

fore, the set of equivalence classes under SLOCC,

$$
\underbrace {\mathcal {H} ^ {(N)}} _ {N}, \tag {27}
$$

depends at least on  $2(2^{N} - 1) - 6N$  parameters. This lower bound allows for a finite number of classes for  $N = 3$ , but shows that for any larger number  $N$  of qubits there are infinitely many classes, labeled by at least one continuous parameter. The reason is that the number of parameters from a state  $|\psi \rangle$  which the parties can modify by means of a general ILO  $A \otimes B \otimes \dots \otimes N$  grows linearly with  $N$  (6N for the multi-qubit case), whereas the number of parameters required to specify  $|\psi \rangle$  grows exponentially with  $N$ .

More generally, if the Hilbert space is given by  $\mathcal{H} = \mathbb{C}^{n_1}\otimes \dots \otimes \mathbb{C}^{n_N}$ , then the set of equivalence classes under SLOCC,

$$
\frac {\mathrm {C} ^ {n _ {1}} \otimes \cdots \otimes \mathrm {C} ^ {n _ {N}}}{S L _ {n _ {1}} (\mathrm {C}) \times \cdots \times S L _ {n _ {N}} (\mathrm {C})}, \tag {28}
$$

depends at least on  $2(n_{1}n_{2}\dots n_{N} - 1) - 2\Sigma_{i = 1}^{N}(n_{i}^{2} - 1)$ . This shows that only for  $N = 3$  there are still some systems with (potentially) only a finite number of classes under SLOCC, namely those with Hilbert space  $\mathbb{C}^2\otimes \mathbb{C}^{n_2}\otimes \mathbb{C}^{n_3}$ , that is, having a qubit as at least one of the subsystems. In all other cases, one finds an infinite number of classes.

We notice that even allowing for noninvertible local operations, the amount of parameters that can be changed by local manipulations is typically smaller than what the state depends on. That is, the subset of states that can be reached locally from a given state  $|\psi \rangle$  is of zero measure in the set of states of the multipartite system. Recall that in the bipartite scenario,  $\mathcal{H} = \mathbb{C}^n\otimes \mathbb{C}^m$ , there is always a maximally entangled state from which all the other states can be locally prepared with certainty of success. We see now that, in constraint, there is typically in a multipartite system no state from which all the others can be prepared, not even with some probability of success. Of course, the parties can always resort to, say, using a sufficient amount of EPR states distributed among them to prepare any multipartite state by standard teleportation. This implies, however, using an initial state (that of many EPR states) which belongs to a Hilbert space much larger than the Hilbert space of the state the parties are trying to create, and thus does not change the previous conclusion.

# B. State  $|W\rangle$  in multiqubit systems

Let us have a look at the generalized form  $\left|W_{N}\right\rangle$  of the state  $\left|W\right\rangle$  (2). We define the state

$$
\left| W _ {N} \right\rangle \equiv (1 / \sqrt {N}) | N - 1, 1 \rangle , \tag {29}
$$

where  $|N - 1,1\rangle$  denotes the totally symmetric state including  $N - 1$  zeros and 1 ones. For example, we obtain for  $N = 4$

$$
\left| W _ {4} \right\rangle = (1 / \sqrt {4}) \left(\left| 0 0 0 1 \right\rangle + \left| 0 0 1 0 \right\rangle + \left| 0 1 0 0 \right\rangle + \left| 1 0 0 0 \right\rangle\right). \tag {30}
$$

One immediately observes that the entanglement of this state is again very robust against particle losses, i.e., the state  $\left|W_{N}\right\rangle$  remains entangled even if any  $N - 2$  parties lose the information about their particle. This means that any two out of  $N$  parties possess an entangled state, independently of whether the remaining  $(N - 2)$  parties decide to cooperate with them or not. This can be seen by computing the reduced density operator  $\rho_{AB}$  of  $\left|W_{N}\right\rangle$ , i.e., by tracing out all but the first and the second systems. By symmetry of the state  $\left|W_{N}\right\rangle$ , we have that all reduced density operators  $\rho_{\kappa \mu}$  are identical and we obtain

$$
\rho_ {\kappa \mu} = \frac {1}{N} (2 | \Psi^ {+} \rangle \langle \Psi^ {+} | + (N - 2) | 0 0 \rangle \langle 0 0 |). \tag {31}
$$

The concurrence can easily be determined to be

$$
\mathcal {C} _ {\kappa \mu} \left(W _ {N}\right) = \frac {2}{N}, \tag {32}
$$

which shows that  $\rho_{\kappa \mu}$  is entangled, even distillable. We conjecture that the average value of the square of the concurrence for  $|W_N\rangle$

$$
\frac {2}{N (N - 1)} \sum_ {\kappa} \sum_ {\mu \neq \kappa} \mathcal {C} _ {\kappa \mu} ^ {2} \left(W _ {N}\right) = \frac {4}{N ^ {2}}, \tag {33}
$$

is again the maximal value achievable for any state of  $N$  qubits.

# VI. SUMMARY AND CONCLUSIONS

In this work, we investigated equivalence classes of multipartite states specified by stochastic local operations and classical communication. We showed that for pure states of three qubits there are six different classes of this kind. In particular, we found that there are two inequivalent types of genuine tripartite entanglement, represented by the GHZ state and the state  $W$ . We showed that the state  $W$  is the state of three qubits that retains a maximal amount of bipartite entanglement when any one of the three qubits is traced out. For multipartite ( $N \geq 4$ ) and multilevel systems, we showed that there exist infinitely many inequivalent kinds of entanglement (i.e., classes under SLOCC).

# ACKNOWLEDGMENTS

This work was supported by the Austrian Science Foundation under the SFB "control and measurement of coherent quantum systems" (Project 11), the European Community under the TMR Network ERB-FMRX-CT96-0087, Project EQUIP (Contract No. IST-1999-11053), and the European Science Foundation and the Institute for Quantum Information GmbH. G.V. also acknowledges funding from the EC through Grant No. HPMF-CT-1999-00200.

# APPENDIX A: SLOCC AND LOCAL RANKS

In this appendix we show that states  $|\psi \rangle$  and  $|\phi \rangle$  belong to the same class under SLOCC iff they are related by means of an invertible local operator (ILO). From this connection it follows easily that the local ranks of a pure state,  $r(\rho_{\kappa})$ ,  $\kappa = A, B, \ldots$ , are invariant under SLOCC, whereas under LOCC they can only decrease.

Lemma. If the bipartite vectors  $|\psi \rangle$  and  $|\phi \rangle \in \mathbb{C}^n\otimes \mathbb{C}^m$  fulfill

$$
\left| \phi \right\rangle = A \otimes 1 _ {B} | \psi \rangle , \tag {A1}
$$

then the ranks of the corresponding reduced density matrices satisfy  $r(\rho_A^\psi) \geqslant r(\rho_A^\phi)$  and  $r(\rho_B^\psi) \geqslant r(\rho_B^\phi)$ .

Proof. We consider the Schmidt decomposition of  $|\psi \rangle$

$$
| \psi \rangle = \sum_ {i = 1} ^ {n _ {\psi}} \sqrt {\lambda_ {i} ^ {\psi}} | i \rangle | i \rangle , \quad \lambda_ {i} ^ {\psi} > 0, \quad n _ {\psi} \leqslant \min  (n, m), \tag {A2}
$$

and write the operator  $A$  as

$$
A = \sum_ {i = 1} ^ {n} | \mu_ {i} \rangle \langle i |, \tag {A3}
$$

where  $|\mu_i\rangle \in \mathbb{C}^n$  do not need to be normalized nor linearly independent. Then we have that  $\rho_A^\psi = \Sigma_{i=1}^{n_\psi} |i\rangle \langle i|$  and  $\rho_A^\phi = A \rho_A^\psi A^\dagger = \Sigma_{i=1}^{n_\psi} |\mu_i\rangle \langle \mu_i|$ , so that  $r(\rho_A^\phi) \leqslant n_\psi$ . The second inequality of the lemma follows from the fact that for any bipartite vector  $r(\rho_A) = r(\rho_B)$ .

Corollary. If the vectors  $|\psi \rangle, |\phi \rangle \in \mathcal{H}_A \otimes \mathcal{H}_B \otimes \dots \otimes \mathcal{H}_N$  are connected by a local operator as  $|\phi \rangle = A \otimes B \otimes \dots \otimes N|\psi \rangle$ , then the local ranks satisfy  $r(\rho_{\kappa}^{\psi}) \geqslant r(\rho_{\kappa}^{\phi})$ ,  $\kappa = A, B, \ldots, N$ .

Proof. Indeed, for each of the parties, say Alice for concreteness, we can view the operator  $A \otimes B \otimes \dots \otimes N$  as the composition of two local operators,  $A \otimes 1_{B\dots N}$  and  $1_A \otimes (B \otimes \dots \otimes N)$ , and the Hilbert space as  $\mathcal{H}_A \otimes \mathcal{H}_{B\dots N}$ . Then, because of the previous lemma, application of the first operator cannot increase  $r(\rho_A)$ , and the same happens with the second operator, which cannot increase  $r(\rho_{B\dots N})$  [recall that for any pure state  $r(\rho_A) = r(\rho_{B\dots N})$ ].

Theorem. Two pure states of a multipartite system are equivalent under SLOCC if they are related by a local invertible operator.

Proof. If

$$
| \phi \rangle = A \otimes B \otimes \dots \otimes N | \psi \rangle , \tag {A4}
$$

then a local protocol exists for the parties to transform  $|\psi \rangle$  into  $|\phi \rangle$  with a finite probability of success. Indeed, each party needs simply to perform a local POVM including a normalized version of the corresponding local operator in Eq. (A4). For instance, Alice has to apply a POVM defined by operators  $\sqrt{p_A} A$  and  $\sqrt{1_A - p_A A^\dagger A}$ , where  $p_A \leqslant 1$  is a positive weight such that  $p_A A^\dagger A \leqslant 1_A$ , and similarly for the rest of the parties. Then such a local protocol converts  $|\psi \rangle$  successfully into  $|\phi \rangle$  with probability  $p_A p_B \cdots p_N$ . If, in addition,  $A, B, \ldots, N$  are invertible operators, then obviously

$$
\left| \psi \right\rangle = A ^ {- 1} \otimes B ^ {- 1} \otimes \dots \otimes N ^ {- 1} \mid \phi \rangle \tag {A5}
$$

and the conversion can be reversed locally. Let us then move to prove the converse. We already argued (Sec. II A) that if  $|\psi \rangle$  can be converted into  $|\phi \rangle$  by LOCC, then a local operator relates them. We want to prove now that the equivalence of  $|\psi \rangle$  and  $|\phi \rangle$  under SLOCC implies that this operator can always be chosen to be invertible. For simplicity, we will assume that  $|\psi \rangle$  and  $|\phi \rangle$  are related by a local operator acting nontrivially only in Alice's part,

$$
| \phi \rangle = A \otimes 1 _ {B \dots N} | \psi \rangle . \tag {A6}
$$

[The general case would correspond to composing operator  $A \otimes 1_{B \dots N}$  with operator  $1_{A} \otimes B \otimes 1_{C \dots N}$ , and similarly for the rest of the parties. The following argumentation should then be applied sequentially to each party individually.] We can then consider the Schmidt decomposition of the states with respect to part  $A$  and part  $B \dots N$ ,

$$
\left| \psi \right\rangle = \sum_ {i = 1} ^ {n _ {\psi}} \sqrt {\lambda_ {i} ^ {\psi}} \left| i \right\rangle \left| \tau_ {i} \right\rangle , \quad \lambda_ {i} ^ {\psi} > 0, \tag {A7}
$$

$$
\left| \phi \right\rangle = \sum_ {i = 1} ^ {n _ {\phi}} \sqrt {\lambda_ {i} ^ {\phi}} \left(U _ {A} | i \rangle\right) \left| \tau_ {i} \right\rangle , \quad \lambda_ {i} ^ {\phi} > 0, \tag {A8}
$$

where the local unitary  $U_{A}$  relates the two local Schmidt bases in Alice's part,  $\{|i\rangle \}_{i = 1}^{n}\in \mathcal{H}_{A} = \mathbb{C}_{i}^{n},\left|\tau_{i}\right\rangle \in \mathcal{H}_{B}\otimes \dots \otimes \mathcal{H}_{N}$ , and  $n_{\psi} = n_{\phi}$  because of the previous corollary. Now, operator  $A$  in Eq. (A6) must be of the form (up to some irrelevant permutations in the Schmidt basis)

$$
A = U _ {A} \left(A _ {1} + A _ {2}\right),
$$

$$
A _ {1} \equiv \sum_ {i = 1} ^ {n _ {\psi}} \sqrt {\frac {\lambda_ {i} ^ {\phi}}{\lambda_ {i} ^ {\psi}}} | i \rangle \langle i |, \tag {A9}
$$

$$
A _ {2} \equiv \sum_ {i = n _ {l r} + 1} ^ {n} | \mu_ {i} \rangle \langle i |, \tag {A10}
$$

where  $|\mu_i\rangle$  are arbitrary unnormalized vectors. Notice that vectors  $|\mu_i\rangle$  play no role in Eq. (A6) since  $A_{2}\otimes 1_{B\dots N}|\psi \rangle = 0$ . Therefore, we can redefine

$$
A _ {2} \equiv \sum_ {i = n _ {\psi} + 1} ^ {n} | i \rangle \langle i |, \tag {A11}
$$

which implies that  $A$  is an invertible operator.

# APPENDIX B:  $\tau$  IS AN ENTANGLEMENT MONOTONE

In this appendix, we show that the 3-tangle  $\tau$  is an entanglement monotone, i.e., decreasing on average under LOCC in all the three parties. We first note that any local protocol can be decomposed into POVM's such that only one party performs operations on the system. This, together with the invariance of the 3-tangle  $\tau$  under permutations of the parties, ensures that it is sufficient to consider a local

POVM in  $A$  only. Furthermore, we can restrict ourselves to two-outcome POVM's due to the fact that a generalized (local) POVM can be implemented by a sequence of two outcome POVM's. Let  $A_{1}, A_{2}$  be the two POVM elements such that  $A_{1}^{\dagger} A_{1} + A_{2}^{\dagger} A_{2} = \mathbb{1}$ . We can write  $A_{i} = U_{i} D_{i} V$ , where  $U_{i}, V$  are unitary matrices and  $D_{i}$  are diagonal matrices with entries  $(a, b) \left[ \left( \left( 1 - a^{2} \right)^{1/2}, \left( 1 - b^{2} \right)^{1/2} \right] \right]$ , respectively. Note that we used the singular value decomposition for  $A_{i}$ , and we have that the restriction that  $A_{1}, A_{2}$  constitute a POVM immediately implies that the unitary operation  $V$  can be chosen to be the same in both cases. We consider an initial state  $|\psi \rangle$  with 3-tangle  $\tau(\psi)$ . Let  $|\tilde{\phi}_{i}\rangle = A_{i}|\psi \rangle$  be the (unnormized) states after the application of the POVM. Normalizing them, we obtain  $|\phi_{i}\rangle = |\tilde{\phi}_{i}\rangle / \sqrt{p_{i}}$  with  $p_{i} = \langle \tilde{\phi}_{i} | \tilde{\phi}_{i} \rangle$  and  $p_{1} + p_{2} = 1$ . We want to show that  $\tau^{\eta}$ ,  $0 < \eta \leqslant 1$  is, on average, always decreasing and thus an entanglement monotone, i.e., for

$$
\langle \tau^ {\eta} \rangle = p _ {1} \tau^ {\eta} \left(\phi_ {1}\right) + p _ {2} \tau^ {\eta} \left(\phi_ {2}\right) \tag {B1}
$$

we have that

$$
\langle \tau^ {\eta} \rangle \leqslant \tau^ {\eta} (\psi) \tag {B2}
$$

is fulfilled for all possible choices of the POVM  $\{A_1,A_2\}$ . Using that  $\tau$  is invariant under local unitaries, we do not have to consider the unitary operations  $U_{i}$  in our calculations, i.e.,  $\tau (U_iD_iV\psi) = \tau (D_iV\psi)$ . Taking this simplification into account, a straightforward calculation shows that

$$
\tau \left(\phi_ {1}\right) = \frac {a ^ {2} b ^ {2}}{p _ {1} ^ {2}} \tau (\psi), \quad \tau \left(\phi_ {2}\right) = \frac {\left(1 - a ^ {2}\right) \left(1 - b ^ {2}\right)}{p _ {2} ^ {2}} \tau (\psi), \tag {B3}
$$

where we used that  $\tau (\epsilon \tilde{\phi}_i) = \epsilon^4\tau (\tilde{\phi}_i)$ , which can be checked by noting that  $\tau$  is a quartic function with respect to its coefficients in the standard basis [14]. Note that the dependence of  $\tau (\phi_i)$  on the unitary operation  $V$  is hidden in  $p_i$ . For  $\eta = \frac{1}{2}$ , one obtains for example  $\tau^{1 / 2}(\phi_1) = ab / p_1\tau^{1 / 2}(\psi)$ . Substituting in Eq. (B1), we find

$$
\langle \tau^ {1 / 2} \rangle = [ a b + \sqrt {\left(1 - a ^ {2}\right) \left(1 - b ^ {2}\right)} ] \tau^ {1 / 2} (\psi). \tag {B4}
$$

In this case, one can easily check that Eq. (B4)  $\leqslant \tau^{1 / 2}$  by noting that Eq. (B4) is maximized for  $a = b$ . We thus have that  $\tau^{1 / 2}$  is, on average, always decreasing and thus an entanglement monotone. In a similar way, one can check for  $0 < \eta \leqslant 1$  that  $\tau^{\eta}$  is an entanglement monotone. However, for  $\eta \neq \frac{1}{2}$ , the derivation is a bit more involved due to the fact that in this case the probabilities  $p_i$  in the expression for  $\langle \tau^{\eta} \rangle$  no longer cancel and have to be calculated explicitly.

# APPENDIX C:  $|W\rangle$  MAXIMIZES RESIDUAL BIPARTITE ENTANGLEMENT

Here we show that for all tripartite pure states, except the state  $|W\rangle$ , the following inequality holds:

$$
E _ {\tau} \equiv \mathcal {C} _ {A B} ^ {2} + \mathcal {C} _ {A C} ^ {2} + \mathcal {C} _ {B C} ^ {2} <   \frac {4}{3}, \tag {C1}
$$

while the state  $|W\rangle$  reaches the value  $E_{\tau} = \frac{4}{3}$ . Note that we used the short-hand notation  $\mathcal{C}_{AB}$  for the concurrence of the reduced density operator  $\rho_{AB},\mathcal{C}(\rho_{AB})$ , and similarly for  $\mathcal{C}_{AC}$ ,  $\mathcal{C}_{BC}$ .

Inequality (C1) already implies that the state  $|W\rangle$  reaches the maximum average value  $\overline{\mathcal{E}} (\psi)$  of Eq. (24) for the choice of  $\mathcal{E}(\rho) = \mathcal{C}(\rho)^2$ , namely  $\overline{\mathcal{E}} (W) = \frac{4}{9}$ .

At the same time, inequality (C1) also shows that the state  $|W\rangle$  maximizes the function  $\mathcal{E}_{\mathrm{min}}(\psi)$  (25) for the choice of  $\mathcal{E}(\rho) = \mathcal{C}(\rho)^2$ , since (C1) implies that

$$
\mathcal {C} _ {\min } ^ {2} (\psi) \equiv \min  \left(\mathcal {C} _ {A B} ^ {2}, \mathcal {C} _ {A C} ^ {2}, \mathcal {C} _ {B C} ^ {2}\right) <   \frac {4}{9} \tag {C2}
$$

for all states except the state  $|W\rangle$ , for which the value  $\frac{4}{9}$  is reached. From Eq. (C2) it follows that for any bipartite measure of entanglement  $\mathcal{E}(\rho)$  which is monotonically increasing with the square of the concurrence (and hence with the concurrence itself), the state  $|W\rangle$  maximizes the function  $\mathcal{E}_{\mathrm{min}}(\psi)$  (25), i.e.,

$$
\mathcal {E} _ {\min } (\psi) <   \mathcal {E} _ {\min } (W) = \mathcal {E} \left(\mathcal {C} ^ {2} = \frac {4}{9}\right). \tag {C3}
$$

Assume that this is not the case, i.e., there exists a state  $\psi$  for which  $\mathcal{E}_{\mathrm{min}}(\psi) > \mathcal{E}_{\mathrm{min}}(W)$ . Since by assumption  $\mathcal{E}$  is monotonically increasing with the concurrence, this would imply that  $\mathcal{C}_{\mathrm{min}}^2 (\psi) > \frac{4}{9}$ , which contradicts Eq. (C2) and is hence impossible.

Note in addition that any good measure of entanglement should be a convex function [5], as  $\mathcal{C}(\rho)$ ,  $E_{f}(\rho)$ , and  $E_{2}(\rho)$  are. This implies, when applied to Eqs. (24) and (25), that the optimal values for  $\overline{\mathcal{E}}$  and  $\mathcal{E}_{\mathrm{min}}$  are achieved for pure states.

The remainder of this appendix is devoted to prove inequality (C1). Using the definition of the 3-tangle,  $\tau \equiv \tau_{ABC} = \mathcal{C}_{A(BC)}^2 -\mathcal{C}_{AB}^2 -\mathcal{C}_{AC}^2$  [14] and the invariance of the 3-tangle under permutations of the parties, we can rewrite  $E_{\tau}$  as  $\frac{1}{2} (\mathcal{C}_{A(BC)}^2 +\mathcal{C}_{B(AC)}^2 +\mathcal{C}_{C(AB)}^2 -3\tau)$ . Using that  $\mathcal{C}_{\kappa (\mu \nu)}^2 = 4\operatorname *{det}\rho_{\kappa}$ , we can evaluate  $E_{\tau}$  for the different classes.

Starting with the class  $A - B - C$ , we immediately obtain that  $E_{\tau}(\Psi_{A - B - C}) = 0$ . For the class  $A - BC$ , we have that  $\tau = 0$  and  $\mathcal{C}_{A(BC)}^2 = 0$ . Since  $\mathcal{C}_{B(AC)}, \mathcal{C}_{C(AB)}^2 \leqslant 1$ , we have that  $E_{\tau}(\Psi_{A - BC}) \leqslant 1$  in this case (and similarly for the classes  $B - AC, C - AB$ ).

Now we consider the class  $W$ , specified by Eq. (20). Again, we have that  $\tau = 0$ . We find that  $E_{\tau}(\Psi_W) = 4(ab + ac + bc)$  (which does not depend on  $d$ ). Notice that  $E_{\tau}$  is maximized for  $a = b = c = \frac{1}{3}$  which corresponds to the state  $|W\rangle$  and leads to  $E_{\tau} = \frac{4}{3}$ . For all other values of  $a, b, c, d$ , we have that  $E_{\tau} < \frac{4}{3}$ .

Let us now turn to the class GHZ, specified in Eq. (15). Using that  $\tau (\Psi_{\mathrm{GHZ}})$  is given in Eq. (22) and  $\operatorname *{det}\rho_{A} = K^{2}c_{\delta}^{2}s_{\delta}^{2}s_{\alpha}^{2}(1 - c_{\beta}^{2}c_{\gamma}^{2})$  (and similarly for  $\operatorname *{det}\rho_{B,C}$ ), we obtain

$$
E _ {\tau} = \frac {4 c _ {\delta} ^ {2} s _ {\delta} ^ {2} \left[ \left(s _ {\alpha} ^ {2} s _ {\beta} ^ {2} + s _ {\alpha} ^ {2} s _ {\gamma} ^ {2} + s _ {\beta} ^ {2} s _ {\gamma} ^ {2}\right) - 3 s _ {\alpha} ^ {2} s _ {\beta} ^ {2} s _ {\gamma} ^ {2} \right]}{\left(1 + 2 c _ {\delta} s _ {\delta} c _ {\alpha} c _ {\beta} c _ {\gamma} c _ {\varphi}\right) ^ {2}}. \tag {C4}
$$

One readily checks that Eq. (C4) is maximized for  $\delta = \pi / 4$  and  $\varphi = \pi$  (which corresponds to  $c_{\delta} = s_{\delta} = 1 / \sqrt{2}$  and  $c_{\varphi} =$

$-1)$ , independent of the values of  $\alpha, \beta, \gamma \in (0, \pi/2]$ . Thus we have that  $E_{\tau} \leqslant E_{\tau} (\delta = \pi/4, \varphi = \pi)$  and after some algebra we obtain

$$
E _ {\tau} \leqslant \frac {\left(c _ {\alpha} ^ {2} + c _ {\beta} ^ {2} + c _ {\gamma} ^ {2}\right) - 2 \left(c _ {\alpha} ^ {2} c _ {\beta} ^ {2} + c _ {\alpha} ^ {2} c _ {\gamma} ^ {2} + c _ {\beta} ^ {2} c _ {\gamma} ^ {2}\right) + 3 c _ {\alpha} ^ {2} c _ {\beta} ^ {2} c _ {\gamma} ^ {2}}{\left(1 + c _ {\alpha} c _ {\beta} c _ {\gamma}\right) ^ {2}}. \tag {C5}
$$

We want to show that the right-hand side of Eq. (C5)  $< \frac{4}{3}$ . Let us call  $x\equiv c_{\alpha},y\equiv c_{\beta},z\equiv c_{\gamma}$  with  $0\leqslant x,y,z < 1$ . We thus have to show that

$$
\begin{array}{l} f (x, y, z) \equiv 3 \left(x ^ {2} + y ^ {2} + z ^ {2}\right) - 6 \left(x ^ {2} y ^ {2} + x ^ {2} z ^ {2} + y ^ {2} z ^ {2}\right) \\ + 5 \left(x ^ {2} y ^ {2} z ^ {2}\right) - 4 + 8 x y z \\ <   0. \tag {C6} \\ \end{array}
$$

Let us calculate the maximum of  $f(x,y,z)$ . We therefore take the derivatives of  $f(x,y,z)$  with respect to  $x,y,z$ , respectively (which we denote by  $f_{x},f_{y},f_{z}$ ) and set them to zero. One immediately observes [by considering the linear combination of the resulting equations, e.g.,  $xf_{x} - yf_{y}$ , where one, e.g., obtains  $(x^{2} - y^{2})(1 - 2z^{2}) = 0$ ] that for a maximum we

must have  $x = y = z$ . The possible solutions of the resulting polynomial of degree 5 can be checked to lie outside the interval [0,1), i.e., outside the range of  $x,y,z$  except for  $x = y = z = 0$ . It can, however, be easily verified that this solution gives rise to a minimum of  $f(x,y,z)$ , namely  $f(0,0,0) = -4$ . Thus the maximum of  $f(x,y,z)$  is obtained at the border of the range for  $x,y,z$ , which corresponds to the surfaces of a cube. Due to the fact that  $f(x,y,z)$  is invariant under permutations of the variables, we only have to check two of the surfaces, e.g., the surfaces specified by  $x = 0$  and  $x = 1$  (actually  $x = 1 - \epsilon$ , where  $\epsilon$  is an infinitesimally small positive number) and we find (i)  $f(0,x,y) = 3(y^2 + z^2) - 6y^2z^2 - 4 \leqslant -1$  (the maximum in this case is, e.g., obtained for  $y = 0,z = 1 - \epsilon$ ) and (ii)  $f(1,y,z) = 8yz - 3(y^2 + z^2) - y^2z^2 - 1 < 0$ . In (ii), it can be checked that a necessary condition for a maximum is  $y = z$  and that  $f(1,y,y)$  is monotonically increasing in [0,1) and is thus maximized for  $y = z = (1 - \epsilon)$ . One obtains  $f(x,y,z) \leqslant f(1,1 - \epsilon,1 - \epsilon) < 0$  as desired.

So we managed to show that the state  $|W\rangle$  is the only state which fulfills  $E_{\tau} = \frac{4}{3}$ , and for all other tripartite pure states we have that  $E_{\tau} < \frac{4}{3}$ .

[1] C. H. Bennett, H. J. Bernstein, S. Popescu, and B. Schumacher, e-print quant-ph/9511030 (unpublished).  
[2] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[3] N. Linden, S. Popescu, B. Schumacher, and M. Westmoreland, e-print quant-ph/9912039 (unpublished); G. Vidal, W. Dür, and J. I. Cirac, e-print quant-ph/0004009 (unpublished); S. Wu and Y. Zhang, e-print quant-ph/0004020 (unpublished).  
[4] C. H. Bennett, S. Popescu, D. Rohrlich, J. A. Smolin, and A. V. Thapliyal, quant-ph/9908073.  
[5] G. Vidal, J. Mod. Opt. 47, 355 (2000).  
[6] N. Linden and S. Popescu, Fortschr. Phys. 46, 567 (1998).  
[7] J. Schlienz, (unpublished).  
[8] A. Sudbery, e-print quant-ph/0001116.  
[9] H. A. Carteret and A. Sudbery, e-print quant-ph/0001091.  
[10] J. Kempe, Phys. Rev. A 60, 910 (1999).  
[11] Different classifications based on LU invariants were recently proposed in [20] and [9]. Depending on the values of these invariants, several classes of states in one case and types of entanglement in the other are identified. We want to remark that our classification is based on probabilistic conversions under LOCC, and therefore, as expected, our results are not fully compatible with those of these approaches.  
[12] D. M. Greenberger, M. Horne, and A. Zeilinger, Bell's Theorem, Quantum Theory, and Conceptions of the Universe, edited by M. Kafatos (Kluwer, Dordrecht, 1989), p. 69; D. Bouwmeester et al., Phys. Rev. Lett. 82, 1345 (1999).  
[13] A. Zeilinger, M. A. Horne, and D. M. Greenberger, NASA Conf. Publ. No. 3135 (National Aeronautics and Space Administration, Code NTT, Washington, DC, 1997).  
[14] V. Coffman, J. Kundu, and W. K. Wootters, Phys. Rev. A 61, 052306 (2000); see also e-print quant-ph/9907047 (unpublished).

[15] H. K. Lo and S. Popescu, e-print quant-ph/9707038 (unpublished).  
[16] G. Vidal, Phys. Rev. Lett. 83, 1046 (1999).  
[17] M. Nielsen, Phys. Rev. Lett. 83, 436 (1999).  
[18] Recall that the  $n$  entanglement monotones  $E_{k}(\psi)\equiv \Sigma_{i = k}^{n}\lambda_{i}$  where  $\lambda_{i}$  come from the Schmidt decomposition of  $|\psi \rangle$ $\in \mathbb{C}^n\otimes \mathbb{C}^n$

$$
| \psi \rangle = \sum_ {i = 1} ^ {n} \sqrt {\lambda_ {i}} | i \rangle \otimes | i \rangle , \quad \lambda_ {i} \geqslant \lambda_ {i + 1} \geqslant 0,
$$

are the measures that provide a quantitative description of the entanglement resources of a single copy of pure states, in that, for instance, they give the optimal probability  $P(\psi \rightarrow \phi)$  of conversion of the state  $|\psi\rangle$  into the state  $|\phi\rangle$  under LOCC [16], namely

$$
P (\psi \rightarrow \phi) = \min  \left\{\frac {E _ {1} (\phi)}{E _ {1} (\psi)}, \dots , \frac {E _ {n} (\phi)}{E _ {n} (\psi)} \right\}.
$$

In a two-qubit system we have only two nontrivial monotones,  $E_{1}(\psi) = \lambda_{1} + \lambda_{2} = 1$  and  $E_{2} = \lambda_{2} \leqslant \frac{1}{2}$ . In a similar way as  $E_{2}(\psi) > E_{2}(\phi)$  determines that  $|\psi\rangle$  can be transformed into  $|\phi\rangle$  with certainty by means of LOCC [17], the extension to mixed states  $\rho$  of two qubits,  $E_{2}(\rho)$ , also says when the entanglement of the pure state  $|\psi\rangle$  suffices to locally prepare  $\rho$  with certainty [26].

[19] A. Sampera, R. Tarrach, and G. Vidal, Phys. Rev. A 58, 826 (1998).  
[20] A. Acín, A. Andrianov, L. Costa, E. Jané, J. I. Latorre, and R. Tarrach, Phys. Rev. Lett. 85, 1560 (2000).  
[21] N. Gisin and H. Bechmann-Pasquinucci, e-print quant-ph/9804045 (unpublished).  
[22] A state  $t|00\rangle + x|01\rangle + y|10\rangle + z|11\rangle$  is produced if it can be written as  $(a|0\rangle + b|1\rangle)(c|0\rangle + d|1\rangle)$ , that is, if  $tz = xy$ . A

complex linear combination  $\lambda_1|00\rangle +\lambda_2(x|01\rangle +y|10\rangle$  
$+z|11\rangle)$  with  $\lambda_{2}\neq 0$  cannot be product for any  $\lambda_{1}$  if  $z = 0$  
[23] O. Cohen and T. A. Brun, Phys. Rev. Lett. 84, 5908 (2000).  
[24] A. Higuchi and A. Sudbery, e-print quant-ph/0005013 (unpub-

lished); H. J. Briegel and R. Raussendorf, e-print quant-ph/0004051 (unpublished).  
[25] N. Gisin, Phys. Lett. A 210, 151 (1996).  
[26] G. Vidal, e-print quant-ph/0003002 (unpublished).