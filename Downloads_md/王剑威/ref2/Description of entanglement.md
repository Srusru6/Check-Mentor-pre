# Description of entanglement

J. Schlienz and G. Mahler  
Institut für Theoretische Physik, Universität Stuttgart, Pfaffenwaldring 57, 70550 Stuttgart, Germany  
(Received 28 June 1995)

We propose a measure of entanglement between two subsystems of arbitrary (but finite) number of levels. This measure is invariant under unitary transformations of the subsystems and varies between 0 (product states) and 1 (maximum entangled states). The case of two two-level systems is worked out explicitly, where the known complementarity between one- and two-particle interference results in a very natural way from a sum rule. Generalizations to more than two subsystems are discussed. Here we show that for three particles there cannot exist a pure state that is completely characterized by three-particle entanglement alone. For the example of the Greenberger-Horne-Zeilinger (GHZ) state, an experimental setup is proposed, in which its corresponding two-particle entanglement would show up.

PACS number(s): 03.65.Bz, 07.60.Ly, 42.79.Ta

# I. INTRODUCTION

One of the most striking features of quantum mechanics is the concept of entanglement. Here the word entanglement is used for states of composite systems that cannot be separated into product states in terms of the subsystems ("particles"). The term "particle" is interpreted to denote a subsystem with which we can associate a classical index (i.e., for which index-selective measurements are possible). In typical situations this index will be related to discrete spatial areas (defined, e.g., by the interaction range of the respective detectors and/or the localization range of the states in question): This is to guarantee that entanglement becomes accessible to experiment, even if the basic entities (such as photons) are indistinguishable.

Those entangled states can have properties associated with nonlocal information, which are out of range of classical physics and therefore often hard to understand intuitively. So the results of (gedanken) correlation measurements tend to appear as paradoxes, culminating in the famous paradox of Einstein, Podolsky, and Rosen [1]. Although the paradoxical character of this result was originally regarded as an incompleteness of quantum mechanics describing nature, it became clear after the discovery and experimental verification of Bell's inequalities [2-4] that the nonlocal character and therefore the entanglement is not an artifact of quantum theory but rather an experimental fact. So, in order to describe nature appropriately, one has to abandon the locality of physical laws.

Besides the question concerning fundamental properties of physics, there has recently been a growing interest also in applications of entanglement. Examples are quantum cryptography [5] and teleportation [6], where the nonlocality shows up in a very direct way, as well as quantum computation [7], in which the additional degrees of freedom related to nonlocality are taken for speeding up computation.

Due to the importance of entanglement, a general description would be highly welcome. In the case of a two-particle system, several descriptions have already been proposed [8-12] ([8,9] also consider the general case of  $n$  particles), each having their own advantages and disadvantages. We will give a brief discussion of those in Sec. III. The situation

simplifies if the particles involved are two-level systems. The state, and so the entanglement strength, can then be specified by a single real number. In the case of subsystems with more than two levels, there are already discrepancies between the various definitions [9]. The situation becomes even more involved when more than two particles are entangled. The description then concerns not only the strength but also the possible subsets of particles involved. Special cases are, for example, products of a single-particle and a two-particle entangled state, which are used in quantum teleportation, or states with no single-particle properties such as the so-called Greenberger-Horne-Zeilinger (GHZ) states [13]. So a classification scheme of different entanglement possibilities should be made available. This of course raises the question whether the resulting entanglement features are independent or whether there are relations between them.

In this paper, we propose a general description of entanglement. This definition is entirely based on the decomposition of a given state without necessity of any diagonalization or maximization procedure. This simplifies the calculation and can make the results more transparent. We also consider unitary transformations on the single particles and show that the corresponding transformation properties of the entanglement are of tensorial character. In the case of two particles, we introduce a measure of entanglement satisfying certain upper and lower bounds as well as invariance properties under the above-mentioned unitary transformations.

For a description of coupled quantum systems we use the density-matrix formalism rather than state vectors. Within this description there is, in addition to the possibility of an extension to mixed states, the advantage that single-particle properties and correlations between the particles can conveniently be separated. This separation can easily be done by constructing the reduced density matrix for each subsystem and comparing the resulting product of reduced density matrices with the matrix of the total system. This difference is then interpreted as the entanglement between subsystems. Depending on the number  $n$  of subsystems involved, one can then distinguish between two-particle, three-particle,...,  $n$ -particle entanglement: Together with the respective local (i.e., reduced) state descriptions, this hierarchy of nonlocal properties uniquely specifies the  $n$ -particle state.

This paper is organized as follows. In Sec. II we first give a short review of the  $\mathrm{SU}(N)$ -algebra formalism of the single-particle density matrix and analyze the transformation properties of the corresponding coherence vector. We then introduce in Sec. III our definition of entanglement in the two-particle case and finally specialize on two two-level systems, where, in particular, interference effects are discussed. In Sec. IV we give a short discussion of the three-particle entanglement and an outlook to the general case. The above-mentioned relations between the different orders of entanglement will be demonstrated in an example of the GHZ state vector, where also an experimental setup is proposed to observe the yet unknown two-particle interference property of this state. In Sec. V, we give an outlook to questions on the further development of entanglement measures.

# II.  $\mathbf{SU}(N)$  DESCRIPTION

Since any Hermitian operator on a discrete  $N$ -dimensional Hilbert space  $\mathcal{H}$  can be expanded into the unit operator and the generators of the  $\mathrm{SU}(N)$  algebra, we can specify any density operator by the coefficients of these generators. Such a description has been introduced by Hioe and Eberly [14].

To obtain the generators of the  $\mathrm{SU}(N)$  algebra, one can introduce the transition-projection operators

$$
\hat {P} _ {j k} = | j \rangle \langle k |, \tag {1}
$$

where  $|n\rangle$  are the orthonormalized eigenstates of a linear hermitian operator on  $\mathcal{H}$ . Constructing the  $N^2 - 1$  operators,

$$
\hat {w} _ {l} = - \sqrt {\frac {2}{l (l + 1)}} \left(\hat {P} _ {1 1} + \hat {P} _ {2 2} + \dots + \hat {P} _ {l l} - l \hat {P} _ {l + 1, l + 1}\right),
$$

$$
\hat {u} _ {j k} = \hat {P} _ {j k} + \hat {P} _ {k j},
$$

$$
\hat {v} _ {j k} = i \left(\hat {P} _ {j k} - \hat {P} _ {k j}\right), \tag {2}
$$

where  $1 \leqslant l \leqslant N - 1$  and  $1 \leqslant j < k \leqslant N$ , the set of the resulting operators

$$
\{\hat {\lambda} _ {j} \}: = \{\hat {u} _ {1 2}, \hat {u} _ {1 3}, \dots , \hat {v} _ {1 2}, \hat {v} _ {1 3}, \dots , \hat {w} _ {1}, \hat {w} _ {2}, \dots , \hat {w} _ {N - 1} \}
$$

$$
(j = 1, \dots , N ^ {2} - 1) \tag {3}
$$

fulfills the relations

$$
\operatorname {t r} \left\{\hat {\lambda} _ {i} \right\} = 0, \tag {4}
$$

$$
\operatorname {t r} \left\{\hat {\lambda} _ {i} \hat {\lambda} _ {j} \right\} = 2 \delta_ {i j}, \tag {5}
$$

thus generating the  $\mathrm{SU}(N)$  algebra. In the case  $N = 2$  these operators can be represented by the Pauli matrices.

The density operator then has the representation

$$
\hat {\rho} = \frac {1}{N} \hat {1} + \frac {1}{2} \sum_ {j = 1} ^ {N ^ {2} - 1} \lambda_ {j} \hat {\lambda} _ {j}, \tag {6}
$$

where the factor  $1 / N$  expresses the normalization condition  $\operatorname{tr}\{\hat{\rho}\} = 1$  and

$$
\lambda_ {j} = \operatorname {t r} \left\{\hat {\lambda} _ {j} \hat {\rho} \right\}. \tag {7}
$$

$\pmb{\lambda} = \{\lambda_{j}\}$  is an  $(N^2 -1)$ -dimensional vector, the coherence vector or generalized Bloch vector, which is real due to the hermiticity of  $\hat{\rho}$ .

In this formalism, the unitary transformation  $\hat{U}$

$$
\hat {\rho} \rightarrow \hat {\rho} ^ {\prime} = \hat {U} \hat {\rho} \hat {U} ^ {+} \tag {8}
$$

can also be described as a rotation of the coherence vector  $\lambda$ . Decomposing  $\hat{\rho}'$  in the form (6) with coefficients  $\lambda_i'$  and using the invariance of the trace under cyclic permutation, the components  $\lambda_i'$  of the transformed coherence vector are found to be

$$
\lambda_ {i} ^ {\prime} = \operatorname {t r} \left\{\hat {\lambda} _ {i} \hat {\rho} ^ {\prime} \right\} = \operatorname {t r} \left\{\hat {U} ^ {+} \hat {\lambda} _ {i} \hat {U} \hat {\rho} \right\}. \tag {9}
$$

Since  $\hat{U}^{+}\hat{\lambda}_{i}\hat{U}$  is a Hermitian operator it can be expanded into the  $\mathrm{SU}(N)$  generators, leading to

$$
\hat {U} ^ {+} \hat {\lambda} _ {i} \hat {U} = \frac {1}{2} \operatorname {t r} \left\{\hat {U} ^ {+} \hat {\lambda} _ {i} \hat {U} \hat {\lambda} _ {j} \right\} \hat {\lambda} _ {j} =: T _ {i j} \hat {\lambda} _ {j}. \tag {10}
$$

$T_{ij}$  defines a real  $(N^2 - 1) \times (N^2 - 1)$  matrix. Finally, inserting (10) into (9) and taking into account (7) one gets the result

$$
\lambda_ {i} \rightarrow \lambda_ {i} ^ {\prime} = T _ {i j} \lambda_ {j}. \tag {11}
$$

Using the completeness relation for  $\mathrm{SU}(N)$  matrices

$$
\sum_ {j = 1} ^ {N ^ {2} - 1} \left(\hat {\lambda} _ {j}\right) _ {k i} \left(\hat {\lambda} _ {j}\right) _ {m n} = 2 \delta_ {i m} \delta_ {k n} - \frac {2}{N} \delta_ {k i} \delta_ {m n}, \tag {12}
$$

one can show that  $\mathbf{T}$  is an orthonormal matrix, i.e.,

$$
\sum_ {i = 1} ^ {N ^ {2} - 1} T _ {i j} T _ {i k} = \delta_ {j k}, \sum_ {i = 1} ^ {N ^ {2} - 1} T _ {j i} T _ {k i} = \delta_ {j k}. \tag {13}
$$

Furthermore, as the special case  $\hat{U} = \hat{1}$  implies, the determinant of  $\mathbf{T}$  is equal to unity.

Applying two consecutive unitary transformations  $\hat{U}_1$  and  $\hat{U}_2$  to the density matrix, the corresponding transformation matrix  $\mathbf{T}$  obeys

$$
T _ {i k} \left(\hat {U} _ {1} \hat {U} _ {2}\right) = T _ {i j} \left(\hat {U} _ {1}\right) T _ {j k} \left(\hat {U} _ {2}\right). \tag {14}
$$

In other words,  $\mathbf{T}$  describes an  $(N^2 - 1)$ -dimensional representation of the special unitary group  $\mathrm{SU}(N)$ . This can be used, e.g., to investigate invariant subspaces.

# III. TWO PARTICLES

# A. Arbitrary number of levels

In this section we consider the case of  $n = 2$  particles defined in the Hilbert spaces  $\mathcal{H}_1$  and  $\mathcal{H}_2$  with dimension  $N_1$  and  $N_2$ , respectively. We extend the results of [15-17], which are briefly reviewed.

The direct product of the base states of the single particles serves as a basis in the composite system. The density operator then reads

$$
\begin{array}{l} \hat {\rho} = \frac {1}{N _ {1} N _ {2}} (\hat {1} \otimes \hat {1}) + \frac {1}{2 N _ {2}} \sum_ {i = 1} ^ {N _ {1} ^ {2} - 1} \lambda_ {i} (1) (\hat {\lambda} _ {i} \otimes \hat {1}) \\ + \frac {1}{2 N _ {1}} \sum_ {i = 1} ^ {N _ {2} ^ {2} - 1} \lambda_ {i} (2) (\hat {1} \otimes \hat {\lambda} _ {i}) \\ + \frac {1}{4} \sum_ {i = 1} ^ {N _ {1} ^ {2} - 1} \sum_ {j = 1} ^ {N _ {2} ^ {2} - 1} K _ {i j} (1, 2) \left(\hat {\lambda} _ {i} \otimes \hat {\lambda} _ {j}\right). \tag {15} \\ \end{array}
$$

Again, the factor  $1 / N_{1}N_{2}$  is due to the normalization condition  $\operatorname{tr}[\hat{\rho}] = 1$ . The two coherence vectors  $\lambda(1)$  and  $\lambda(2)$ , respectively, with

$$
\lambda_ {i} (1) = \operatorname {t r} \left\{\hat {\rho} \cdot \hat {\lambda} _ {i} \otimes \hat {1} \right\}
$$

$$
\lambda_ {i} (2) = \operatorname {t r} \left\{\hat {\rho} \cdot \hat {1} \otimes \hat {\lambda} _ {i} \right\}, \tag {16}
$$

determine the properties of the individual particles, while the second-rank tensor

$$
K _ {i j} (1, 2) = \operatorname {t r} \left\{\hat {\rho} \cdot \hat {\lambda} _ {i} \otimes \hat {\lambda} _ {j} \right\} \tag {17}
$$

accounts for correlations. Performing the partial trace over subsystem 2, one obtains the reduced density operator for system 1,

$$
\hat {\rho} ^ {(1)} = \operatorname {t r} _ {2} \left\{\hat {\rho} \right\} = \frac {1}{N _ {1}} \hat {1} + \frac {1}{2} \sum_ {i = 1} ^ {N _ {1} ^ {2} - 1} \lambda_ {i} (1) \hat {\lambda} _ {i}. \tag {18}
$$

The reduced density operator  $\hat{\rho}^{(2)}$  for subsystem 2 is calculated in an analogous way. Comparing the direct product  $\hat{\rho}^{(1)}\otimes \hat{\rho}^{(2)}$  with (15), one can identify the difference by a tensor  $\mathbf{M}(1,2)$

$$
M _ {i j} (1, 2) := K _ {i j} (1, 2) - \lambda_ {i} (1) \lambda_ {j} (2). \tag {19}
$$

[For the remainder of this section we will drop the redundant pair index (1,2).] It follows from Eq. (19) that  $\mathbf{M}$  vanishes for any product state. Hence  $\mathbf{M}$  can be regarded as an entanglement tensor. Any two-particle state is uniquely specified by  $M_{ij}$  and the Bloch vectors  $\lambda_i(1),\lambda_j(2)$ .

Based on  $\mathbf{M}$ , we go on to introduce a measure of entanglement, i.e., a number  $\beta$ , consistent with the following requirements. (i)  $\beta$  should vanish for any product state and be positive else. (ii)  $\beta$  should be maximal for any pure state with vanishing Bloch vectors  $\lambda(1)$  and  $\lambda(2)$ . Such states have no single-particle properties, i.e., any reduced density matrix is in the maximal mixed state. (iii)  $\beta$  should be invariant under local unitary transformations, by which we mean any unitary transformation on the single particles separately. Formally, these are transformations of the type

$$
\hat {U} _ {1} = \hat {U} (1) \otimes \hat {U} (2). \tag {20}
$$

Here  $\hat{U}(m)$  is supposed to act on Hilbert space of particle  $m$  only. An example of this kind of transformation is implemented in two-particle interferometry [11,12], where each particle is a two-level system (Fig. 1). A source  $S$  emits two particles (e.g., two photons with two polarization states), each in the opposite direction. The outputs of the source

![](images/90112a4a671170e7d03df384d7b1899ca0ad7a347a33e6043aa88dcee651cff5.jpg)  
FIG. 1. Schematic two-particle interferometry experiment  $(|1\rangle = |\downarrow \rangle, |2\rangle = |\uparrow \rangle)$ .

correspond to the two states necessary to describe each particle. The different directions ("modes") of the emitted particles define the subsystem index  $m = 1,2$  and are necessary to distinguish the photons by the location of the measurement apparatus.

The unitary transformation (20) on the two-particle density matrix amounts to the following transformation of the coefficients:

$$
\lambda_ {i} (m) \rightarrow T _ {i k} (m) \lambda_ {k} (m),
$$

$$
K _ {i j} \rightarrow T _ {i k} (1) T _ {j n} (2) K _ {k n}, \tag {21}
$$

where  $m = 1,2$  labels the single particles and  $T(m)$  denotes the rotation matrix corresponding to (11) [with  $\hat{U} = \hat{U}(m)$ ]. From these properties and the definition (19) the transformation of the entanglement tensor is the same as that of  $K_{ij}$ ,

$$
M _ {i j} \rightarrow T _ {i k} (1) T _ {j n} (2) M _ {k n}. \tag {22}
$$

Let us now consider an invariant of any unitary transformation, the expectation value of the density operator itself:

$$
\langle \hat {\rho} \rangle = \operatorname {t r} \left\{\hat {\rho} ^ {2} \right\}. \tag {23}
$$

In the single-particle case,  $\operatorname{tr}\{\hat{\rho}^2\}$  expresses the conservation of the length of the generalized Bloch vector  $\pmb{\lambda}$ . The corresponding expression for the two-particle case reads

$$
\begin{array}{l} \operatorname {t r} \left\{\hat {\rho} ^ {2} \right\} = \frac {1}{N _ {1} N _ {2}} + \frac {1}{2 N _ {2}} | \boldsymbol {\lambda} (1) | ^ {2} + \frac {1}{2 N _ {1}} | \boldsymbol {\lambda} (2) | ^ {2} \\ + \frac {1}{4} [ | \boldsymbol {\lambda} (1) | ^ {2} | \boldsymbol {\lambda} (2) | ^ {2} + 2 \boldsymbol {\lambda} ^ {\mathbf {T}} (1) \mathbf {M} \boldsymbol {\lambda} (2) + \operatorname {t r} \{\mathbf {M} ^ {\mathbf {T}} \mathbf {M} \} ]. \tag {24} \\ \end{array}
$$

This expression is invariant as a whole, whereas the individual terms may change in general. This can be seen in the case of the unitary transformation

$$
\hat {U} = \frac {1}{2} \left( \begin{array}{c c c c} 0 & \sqrt {2} & \sqrt {2} & 0 \\ \sqrt {2} & 1 & - 1 & 0 \\ - \sqrt {2} & 1 & - 1 & 0 \\ 0 & 0 & 0 & 2 \end{array} \right). \tag {25}
$$

This transformation cannot be decomposed into the product form (20); it transforms the product state  $|\psi \rangle = |\uparrow \uparrow \rangle$  to the singlet state  $|\tilde{\psi}\rangle = 1 / \sqrt{2} (|\uparrow \downarrow \rangle -|\downarrow \uparrow \rangle)$ . The product state has

the coherence vectors  $\lambda_z(1) = \lambda_z(2) = 1$ , while all other components vanish. The singlet state, on the other hand, is completely described by  $M_{xx} = M_{yy} = M_{zz} = -1$ , so the individual components of (24) are obviously not invariant. However, in the case of the above-mentioned local unitary transformation, each term in (24) turns out to be invariant. To prove this, one has to perform the transformation (21) and (22) using the orthonormality conditions (13). Finally, we show that each term in (24) is positive definite, i.e., also

$$
\boldsymbol {\lambda} ^ {T} (1) \mathbf {M} \boldsymbol {\lambda} (2) \geqslant 0 \tag {26}
$$

for any state vector in  $\mathcal{H}(1)\otimes \mathcal{H}(2)$ . To show this, we use the fact that this term is also invariant under local unitary

transformations. So we can use the Schmidt decomposition [19,20]

$$
\left| \psi \right\rangle = \sum_ {i = 1} ^ {N} \alpha_ {i} \left| i i \right\rangle , \tag {27}
$$

where  $N = \min (N_1,N_2)$ . The expansion coefficients  $\alpha_{i}$  can be chosen as real numbers and the state vectors  $|ii\rangle := |i(1)\rangle \otimes |i(2)\rangle$  are direct products of state vectors of the individual particles. Of course, these single-particle state vectors in general do not have the same direction in the corresponding coordinate system. The density operator of this state vector reads

$$
\begin{array}{l} | \psi \rangle \langle \psi | = \sum_ {i = 1} ^ {N} \alpha_ {i} ^ {2} \bigg (\frac {1}{N _ {1} N _ {2}} \hat {1} \otimes \hat {1} + \frac {1}{2 N _ {2}} \sum_ {l = 1} ^ {N _ {1} - 1} w _ {l} ^ {(i)} \hat {w} _ {l} \otimes \hat {1} + \frac {1}{2 N _ {1}} \sum_ {\tilde {l} = 1} ^ {N _ {2} - 1} w _ {\tilde {l}} ^ {(i)} \hat {1} \otimes \hat {w} _ {\tilde {l}} + \frac {1}{4} \sum_ {l = 1} ^ {N _ {1} - 1} \sum_ {\tilde {l} = 1} ^ {N _ {2} - 1} w _ {l} ^ {(i)} w _ {\tilde {l}} ^ {(i)} \hat {w} _ {l} \otimes \hat {w} _ {\tilde {l}} \bigg) \\ + \frac {1}{2} \sum_ {\substack {i, j = 1 \\ i <   j}} ^ {N} \alpha_ {i} \alpha_ {j} \left(\hat {u} _ {i j} \otimes \hat {u} _ {i j} - \hat {v} _ {i j} \otimes \hat {v} _ {i j}\right), \tag{28} \\ \end{array}
$$

with  $\Sigma_{i = 1}^{N}\alpha_{i}^{2} = 1$ . The coherence vectors and the correlation tensor  $K_{ij}$  can be read off from this expression. It is remarkable that the only nonvanishing coefficients of the coherence vectors are those associated with the diagonal matrices  $\hat{w}_l$ . This is consistent with the fact that the reduced density matrix of a state vector written in Schmidt decomposition must be diagonal [10]. Calculating now the corresponding expression for the entanglement tensor  $\mathbf{M}$  and applying the sum rule (A4) one obtains

$$
\boldsymbol {\lambda} ^ {\mathbf {T}} (1) \mathbf {M} \boldsymbol {\lambda} (2) = 4 \sum_ {\substack {i, j = 1 \\ i \neq j}} ^ {N} \alpha_ {i} ^ {4} \alpha_ {j} ^ {2} [ \alpha_ {i} ^ {2} - \alpha_ {j} ^ {2} ]. \tag{29}
$$

Both indices have the same range, so for every index pair  $(i,j)$  there also exists a pair  $(j,i)$ . Summing such a couple of index pairs, one obtains

$$
4 \alpha_ {i} ^ {4} \alpha_ {j} ^ {2} \left(\alpha_ {i} ^ {2} - \alpha_ {j} ^ {2}\right) + 4 \alpha_ {j} ^ {4} \alpha_ {i} ^ {2} \left(\alpha_ {j} ^ {2} - \alpha_ {i} ^ {2}\right) = 4 \alpha_ {i} ^ {2} \alpha_ {j} ^ {2} \left(\alpha_ {i} ^ {2} - \alpha_ {j} ^ {2}\right) ^ {2} \geqslant 0. \tag {30}
$$

The sum (29) can thus be decomposed into single terms, which are all  $\geqslant 0$ . This proves the positivity of (26).

As an appropriate measure of entanglement we now use the last term in (24),  $\mathrm{tr}\{\mathbf{M}^{\mathrm{T}}\mathbf{M}\}$ : This term vanishes for product states, is invariant under local unitary transformation, and is maximal for zero Bloch vectors for any pure state. To get rid of the explicit dependence on the number of levels  $N$ , we normalize according to

$$
\beta = \frac {N ^ {2}}{4 \left(N ^ {2} - 1\right)} \operatorname {t r} \left\{\mathbf {M} ^ {\mathrm {T}} \mathbf {M} \right\}, \tag {31}
$$

so that

$$
0 \leqslant \beta \leqslant 1, \tag {32}
$$

where  $\beta = 1$  corresponds to the maximal entangled pure state.

For a geometrical interpretation of  $\beta$ , we write the entanglement matrix  $\mathbf{M}$  as a vector  $\mathbf{m}$ . This can be done by considering the index pair  $\{i,j\}$  as one index. The components of  $\mathbf{m}$  are then given by

$$
m _ {\{i j \}} := M _ {i j}. \tag {33}
$$

From (22) it follows that under local unitary transformation the components of  $\mathbf{m}$  transform as

$$
m _ {\{i j \}} \rightarrow V _ {\{i j \} \{k m \}} m _ {\{k m \}} \quad \text {w i t h} \quad V _ {\{i j \} \{k m \}} = T _ {i k} (1) T _ {j m} (2). \tag {34}
$$

The orthonormality of the transformation matrix  $\mathbf{V}$  follows from the orthonormality of  $\mathbf{T}(m)$ . Hence, in the vector form (33) the local unitary transformation (20) corresponds to a rotation of the  $(N_{1} \times N_{2})$ -dimensional vector  $\mathbf{m}$ .  $\beta$  is then the normalized square length of  $\mathbf{m}$ , which, of course, is invariant under rotation.

Other measures of entanglement are possible. Barnett and Phoenix [10] considered a quantum-mechanical system partitioned into subsystems by partial tracing over the variables of the other system. The difference between the entropy of the total system and the sum of the partial entropies was then introduced as an index of correlation. It also satisfies our three requirements. However, due to the logarithm function in the definition of the entropy, this measure is often difficult to calculate analytically and furthermore has the disadvantage that it is not accessible to direct physical measurement. It is more pertinent to the problem of the information content of physical systems.

On the other hand, at least for special cases, such an experimental interpretation exists for  $\beta$ : In Sec. III B it will be

shown that in a network of two two-level systems,  $\beta$  is for pure states related to the two-particle interference. Another approach to this subject has been given by Jaeger, Shimony, and Vaidman [12]. Since their approach is directly described in terms of physical measurements, there are no interpretation problems. In the case of two two-level systems their definition is related to ours, while it lacks a straightforward generalization to three- or more-level systems. A description of entanglement completely based on a comparison of the state vector with product states was recently given by Shimony [8,9]: The entanglement  $M_{1}[\mid \phi \rangle ]$  of a state vector  $\left|\phi \right\rangle$  in the product Hilbert space of  $n$  particles  $\mathcal{H} = \mathcal{H}_1\otimes \mathcal{H}_2\otimes \dots \otimes \mathcal{H}_n$  is defined as the distance of  $|\phi \rangle$  to the nearest product state:

$$
M _ {1} [ | \phi \rangle ] = \mathrm {g l b} \| | \phi \rangle - | \psi \rangle \|, \tag {35}
$$

where  $|\psi \rangle$  varies over all possible product states in  $\mathcal{H}$ . Applied to the case of two particles,  $M_{1}[|\phi \rangle]$  depends only on one coefficient, namely, that  $\alpha_{j}$  with the largest absolute value in Schmidt decomposition [8]. The measure of entanglement is then defined as

$$
M _ {1} [ | \phi \rangle ] = \left[ 2 \left(1 - \alpha_ {j}\right) \right] ^ {1 / 2}. \tag {36}
$$

In the case of two two-level systems, this measure is equivalent to the above-mentioned ones and also to our measure  $\beta$  in the sense that for any sequence of state vectors with nondecreasing  $M_{1}[\mid \phi \rangle ]$ , the other measures are also nondecreasing. However, in the case of two three-level systems, different orderings may occur. As an example, consider the two three-level state vectors

$$
| \phi_ {i} \rangle = \alpha_ {1} | 1 1 \rangle + \alpha_ {2} | 2 2 \rangle + \alpha_ {3} | 3 3 \rangle ,
$$

with

$$
| \phi_ {1} \rangle : \alpha_ {1} = \alpha_ {2} = \frac {1}{\sqrt {2}}, \alpha_ {3} = 0,
$$

$$
\left| \phi_ {2} \right\rangle : \alpha_ {1} = \frac {1}{\sqrt {2}} + \delta , \alpha_ {2} = \alpha_ {3} = \frac {1}{2} (1 - \sqrt {2} \delta), \tag {37}
$$

where  $\delta > 0$  is regarded as being arbitrary small, so that all terms proportional to  $\delta^2$  can be neglected. Clearly,  $M_1[|\phi_1\rangle] > M_1[|\phi_2\rangle]$  since  $\alpha_{1}$  is in both cases the largest coefficient. Calculating  $\beta$ , however, we find  $\beta[|\phi_1\rangle] = 0.84$  and  $\beta[|\phi_2\rangle] = 0.93$  for  $\delta = 0$ , so  $\beta[|\phi_2\rangle]_{\delta=0} > \beta[|\phi_1\rangle]$ . Due to the continuity of  $\beta$ , this ordering will not be reversed with finite but sufficiently small  $\delta$ . Thus the two definitions, one expressing the distance to the nearest product state, the other depending on the length of a vector based on comparison with the reduced density matrices, turn out to be of different character. Of course, the reason is that  $M_1[|\phi\rangle]$  depends only on the largest coefficient of the Schmidt decomposition of  $|\phi\rangle$ , whereas  $\beta$  is sensitive to all coefficients, so  $\beta$  takes also into account the distribution of the entanglement on the different levels. For example, in the above example the difference of  $\beta[|\phi_1\rangle]$  and  $\beta[|\phi_2\rangle]$  is due to the fact that in  $|\phi_1\rangle$  there are only two states entangled, whereas in  $|\phi_2\rangle$  all

three states are in a genuine entangled state. So, with the different approaches to describe entanglement, different aspects of it are illuminated.

# B.  $\mathbf{SU}(2)\otimes \mathbf{SU}(2)$  states

In this section we will apply the above formalism to the case of two two-level systems. Special emphasize will be given to the problem of complementarity of one- and two-particle interference.

For pure states there is a simple relation between  $\beta$  and the Schmidt decomposition

$$
\left| \psi \right\rangle = \cos (\alpha) \left| \uparrow \uparrow \right\rangle + \sin (\alpha) \left| \downarrow \downarrow \right\rangle \tag {38}
$$

[cf. (28)]. The nonvanishing Bloch vectors and entanglement tensors are

$$
\lambda_ {z} (1) = \lambda_ {z} (2) = \cos (2 \alpha),
$$

$$
M _ {x x} = - M _ {y y} = \sin (2 \alpha),
$$

$$
M _ {z z} = \sin^ {2} (2 \alpha). \tag {39}
$$

The coefficient  $\beta$  is a function of the angle  $\alpha$ :  $\beta (\alpha) = 1 / 3\sin^2 (2\alpha)[2 + \sin^2 (2\alpha)]$ . Knowing the Schmidt decomposition, we also know  $\beta$ . However, there are two advantages to prefer  $\beta$ . First, it can be generalized to mixed states. Second, in the calculation of the Schmidt decomposition, one has to perform a diagonalization in the single-particle Hilbert space [10], while for the determination of  $\beta$ , only decompositions are necessary. This diagonalization yields more information than necessary, i.e., the directions of the single-particle coordinate systems in the respective Hilbert spaces are also determined, which in turn make the calculations more involved. However, due to the invariance of  $\beta$  with respect to local unitary transformations, this additional information is not necessary in our approach.

The above-mentioned invariance of  $\beta$  under local unitary transformations further implies that for a given pure state with nonvanishing  $\beta$ , there exists no state vector in the form of a product state, so due to the theorem of Gisin [21], every pure state with a finite  $\beta$  violates a Bell inequality. In the case of mixed states, however, the situation is more complicated. We do not discuss this problem in this paper; the interested reader is referred to [22,23].

Considering now interference experiments, one has to take into account the fringe visibility  $v_{m}$  of particle  $m$  in ordinary one-particle interferometry and visibility of two-particle fringes  $v_{12}$ , which are defined in the following way [11,12]:

$$
v _ {m} = \frac {\left[ P \left(s _ {m}\right) \right] _ {\max } - \left[ P \left(s _ {m}\right) \right] _ {\min }}{\left[ P \left(s _ {m}\right) \right] _ {\max } + \left[ P \left(s _ {m}\right) \right] _ {\min }},
$$

$$
v _ {1 2} = \frac {\left[ \bar {P} \left(s _ {1} s _ {2}\right) \right] _ {\max } - \left[ \bar {P} \left(s _ {1} s _ {2}\right) \right] _ {\min }}{\left[ \bar {P} \left(s _ {1} s _ {2}\right) \right] _ {\max } + \left[ \bar {P} \left(s _ {1} s _ {2}\right) \right] _ {\min }}. \tag {40}
$$

Here  $s_m$  ( $s_m = \uparrow, \downarrow$ ) refers to the spin component of the  $m$ th particle as found in some local measurement basis,  $P(s_m)$  denotes the probability that a measurement of the particle  $m$  will yield the result  $s_m$ , and  $\bar{P}(s_1 s_2)$  is defined as

$$
\bar {P} \left(s _ {1} s _ {2}\right) = P \left(s _ {1} s _ {2}\right) - P \left(s _ {1}\right) P \left(s _ {2}\right) + \frac {1}{4}, \tag {41}
$$

where  $P(s_{1}s_{2})$  is the joint probability of measuring the spin component  $s_{1}$  on the first particle and  $s_{2}$  on the second. The subtraction of the product of the single-particle probabilities is performed to ensure that this quantity really measures the two-particle correlations; the term  $\frac{1}{4}$  was introduced to ensure positivity. The suffix min and max denote the minimal and maximal values of the corresponding terms with respect to any unitary transformation of the form (20), respectively (i.e., with respect to any measurement basis).

To be explicit, we consider the measurement probabilities of the spin component in the  $z$  direction and assume to measure, without loss of generality, the states  $|\downarrow (m)\rangle$ . The measurement probability of particle  $m$  is then given by the expectation value of the projection operator of the ground state  $\hat{P}_{\downarrow \downarrow}(m)$ , i.e.,

$$
P (\downarrow m) = \operatorname {t r} \left\{\hat {P} _ {\downarrow \downarrow} (m) \hat {\rho} \right\} = \frac {1}{2} [ 1 - \lambda_ {z} (m) ]. \tag {42}
$$

Taking into account the equivalence of the groups  $\mathrm{SU}(2)$  and  $\mathrm{SO}(3)$ , there is a unitary transformation, which transforms the whole vector  $\pmb{\lambda}(m)$  into the single component  $\lambda_z(m)$ . So we have

$$
P (\downarrow m) _ {\text {m i n}} ^ {\max } = \frac {1}{2} [ 1 \pm | \boldsymbol {\lambda} (m) | ], \tag {43}
$$

from which

$$
v _ {m} = \left| \lambda_ {z} (m) \right| _ {\max } = \left| \lambda (m) \right| \tag {44}
$$

follows. Hence the fringe visibility of a single two-level particle is completely determined by the length of the corresponding Bloch vector.

In the same way, one can determine the two-particle interference (41).  $P(\downarrow 1\downarrow 2)$  is defined as the expectation value of the two-particle projection operator  $\hat{P}_{\downarrow \downarrow}(1)\hat{P}_{\downarrow \downarrow}(2)$ . Inserting this into (41), one gets

$$
\bar {P} (\downarrow 1, \downarrow 2) = \frac {1}{4} (1 + M _ {z z}). \tag {45}
$$

[Measurements in the  $i$  direction of particle 1 and  $j$  direction of particle 2 yield, correspondingly,  $\tilde{P} = \frac{1}{4}(1 \pm M_{ij})$ , with the plus sign for measuring on both particles spin up or spin down in the corresponding direction  $i$  and  $j$ , respectively, and the minus sign for mixed spin directions; see also [15]. The equations below can be formulated correspondingly.] Performing now a unitary transformation on particle 1 and choosing the parameters so that the corresponding orthogonal transformation has the form  $\mathbf{T} = \mathrm{diag}(1, -1, -1)$ , the matrix element  $M_{zz}$  transforms to  $-M_{zz}$ . From this consideration it follows that

$$
(M _ {z z}) _ {\max } = - (M _ {z z}) _ {\min } \tag {46}
$$

and the two-particle visibility can be written as

$$
v _ {1 2} = \left(M _ {z z}\right) _ {\max }, \tag {47}
$$

where the extremum is to be sought by the most general local unitary transformation (20). We note in passing that the results (44) and (47) are also valid for mixed states.

Considering the decomposition (39) of a general  $2\otimes 2$  state vector and performing the variation of  $M_{zz}$  under the local unitary transformation (20), the maximum of  $M_{zz}$  is given by  $(M_{zz})_{\mathrm{max}} = \sin (2\alpha)$ . So we have the visibilities

$$
v _ {m} = \cos (2 \alpha),
$$

$$
v _ {1 2} = \sin (2 \alpha). \tag {48}
$$

The complementarity

$$
v _ {m} ^ {2} + v _ {1 2} ^ {2} = 1 \tag {49}
$$

is then seen to be trivially fulfilled. However, it must be emphasized that in order to get this result, the most general form of the single-particle unitary transformation should be considered. An example was given in [11,12], where it was shown that there are state vectors with interference properties being very sensitive to the full generality of the manipulations performed on the single particles. We want to describe this briefly in terms of Bloch vectors in order to demonstrate the simplicity of interpretation in our approach. The transformation matrix corresponding to the proposed interferometry experiment in [11] is given by (B2) with  $\theta = -\pi /4$ ,  $2\varphi = \phi$  and  $\varphi +\chi = 3\pi /2$ . Written explicitly, this reads

$$
\boldsymbol {\lambda} (m) \rightarrow \boldsymbol {\lambda} ^ {\prime} (\mathbf {m}) = \left(\begin{array}{c}\cos \left(\phi_ {m}\right) \lambda_ {x} (m) + \sin \left(\phi_ {m}\right) \lambda_ {y} (m)\\\lambda_ {z} (m)\\\sin \left(\phi_ {m}\right) \lambda_ {x} (m) - \cos \left(\phi_ {m}\right) \lambda_ {y} (m)\end{array}\right). \tag {50}
$$

From this equation it can be seen that in the case of state vectors with a nonvanishing  $z$  component, it is no longer possible to transform this vector completely into the  $z$  direction. So the equality  $v_{m}^{2} + v_{12}^{2} = 1$  cannot be verified for arbitrary states; the general unitary transformation is necessary here [12].

Finally, we remark that this complementarity can already be visualized by inspecting the sum rule (24). For a maximal length of the Bloch vectors, the relation  $\mathrm{tr}\{\hat{\rho}^2\} = 1$  is already fulfilled by the terms without the entanglement tensor, so this tensor must vanish due to the positivity of (26). On the other hand, however, with a maximum value of  $\beta = 1$ , which leads to a maximal  $v_{12}$ , this relation can be fulfilled only when all components of the Bloch vector vanish, so there is no fringe visibility of the single particles.

# IV. THREE PARTICLES AND THE GENERAL CASE

The definition of entanglement can be generalized to more subsystems. In this section we define the three-particle entanglement explicitly and give a brief outlook to the general case.

The general three-particle density matrix can be defined extending the two-particle case (15). It is described by three generalized Bloch vectors  $\lambda(m)$ ,  $m = 1,2,3$ , three two-particle correlation tensors  $\mathbf{K}_{ij}(m,n)$ ,  $1 \leqslant m < n \leqslant 3$ , and one three-particle correlation tensor  $\mathbf{K}_{ijk}(1,2,3)$  defined by

$$
\mathbf {K} _ {i j k} (1, 2, 3) = \operatorname {t r} \left\{\hat {\lambda} _ {i} (1) \otimes \hat {\lambda} _ {j} (2) \otimes \hat {\lambda} _ {k} (3) \cdot \hat {\rho} \right\}. \tag {51}
$$

To get the corresponding entanglement tensors, we subtract from the correlation tensors the products of all the generalized Bloch vectors and entanglement tensors of lower order:

$$
M _ {i j} (m, n) = K _ {i j} (m, n) - \lambda_ {i} (m) \lambda_ {j} (n),
$$

$$
\begin{array}{l} M _ {i j k} (1, 2, 3) = K _ {i j k} (1, 2, 3) - \lambda_ {i} (1) M _ {j k} (2, 3) - \lambda_ {j} (2) M _ {i k} (1, 3) \\ - \lambda_ {k} (3) M _ {i j} (1, 2) - \lambda_ {i} (1) \lambda_ {j} (2) \lambda_ {k} (3). \tag {52} \\ \end{array}
$$

This decomposition of the correlation tensors can be considered as a kind of cluster expansion as in statistical mechanics [18].  $M_{ijk}(1,2,3)$  is zero if  $K_{ijk}(1,2,3)$  can be expressed in terms of two-particle entanglements and local Bloch vectors. In general, any three-particle state is uniquely specified by the tensors  $M_{ijk}(1,2,3), M_{ij}(1,2), M_{ij}(1,3), M_{ij}(2,3)$ , and  $\lambda_i(m)$ ,  $m = 1,2,3$ . Performing the partial trace over subsystem 3, say, one obtains the reduced density operator  $\hat{\rho}^{(1,2)}$  as given by Eq. (15):  $M_{ij}(1,2)$  and  $\lambda_i(1)\lambda_j(2)$  are the pertinent parameters, which can be read off from Eq. (52).

One may ask whether there could exist pure states, which only show three-particle entanglement without having any entanglement of two particles or single-particle coherence. Considering the special case for three  $N$ -level systems, this state would have the following density matrix:

$$
\hat {\rho} = \frac {1}{N ^ {3}} \hat {1} \otimes \hat {1} \otimes \hat {1} + \frac {1}{8} M _ {i j k} \hat {\lambda} _ {i} \otimes \hat {\lambda} _ {j} \otimes \hat {\lambda} _ {k}, \quad i, j, k = 1, \dots , N. \tag {53}
$$

To see that such a state cannot exist as a pure state, one considers this three-particle system in terms of two parts and calculates the corresponding reduced density operators. For example, one can construct the two reduced density operators  $\hat{\rho}^{(1,2)}$  and  $\hat{\rho}^{(3)}$ : Due to the vanishing trace of the generators of the  $\mathrm{SU}(N)$  algebra, both are proportional to the unit operator, so they both represent maximal mixed states. The entropies of these parts are then  $\ln N^2$  and  $\ln N$ , respectively. This, however, contradicts the theorem of Araki and Lieb [24], which states that the entropies of the two parts (irrespective of their "size") must be equal when the composite system is in a pure state. So a three-particle entangled state necessarily involves second-order entanglement and/or single-particle coherence.

The generalization to an  $n$ -particle system is now straightforward. One has to generalize the density matrix (15) to  $n$  subsystems and perform the subtractions on the resulting correlation tensors analogous to (52) in the three-particle case. The explicit presentation of this procedure will not be given here.

As an example of three-particle entanglement let us consider the following state, proposed by Greenberger, Horne, and Zeilinger [13]:

$$
| \psi \rangle = \frac {1}{\sqrt {2}} (| \uparrow \uparrow \uparrow \rangle - | \downarrow \downarrow \downarrow \rangle). \tag {54}
$$

Decomposing this state into the entanglement tensors, one gets

$$
M _ {x x x} = - 1, \quad M _ {x y y} = M _ {y x y} = M _ {y y x} = 1,
$$

$$
M _ {z z} (1, 2) = M _ {z z} (1, 3) = M _ {z z} (2, 3) = 1. \tag {55}
$$

All other entanglement tensors vanish as well as the Bloch vectors  $\lambda_{i}(m)$ ,  $i = x,y,z$ . So this state contains genuine three-particle entanglement, but also entanglement of two particles, as expected.

Note that the reduced single-particle density operators  $\hat{\rho}^{(m)}$  can be written as a mixture of local states; likewise, the reduced density operators  $\hat{\rho}^{(m,n)}$  for any pair subspace  $(m < n)$  can be written as a mixture of pair states

$$
\hat {\rho} ^ {(m, n)} = \frac {1}{2} \left[ | \uparrow \uparrow \rangle \langle \uparrow \uparrow | + | \downarrow \downarrow \rangle \langle \downarrow \downarrow | \right], \tag {56}
$$

thus allowing an entirely "classical" interpretation: Bell inequalities are not violated. (This classical interpretation, to be sure, would be inconsistent when seen from the complete space point of view.)

How can this residual two-particle entanglement be made observable? The often used interferometric arrangement with a phase shifter in one state branch and a following symmetric beam splitter is not sufficient to show the desired interference effects. This is, on first sight, somewhat surprising because this arrangement seems to yield all the necessary conditions for an observation of interference effects: The beam splitter makes the single paths indistinguishable and the phase shifter can give an arbitrary phase difference between them. To see, however, the insensitivity of this arrangement to an important parameter, let us consider the corresponding rotation matrix, which can be read off from (50), where the same arrangement has been discussed. For definiteness we will consider interference effects between particles 1 and 2. Performing the corresponding transformation (22) of the entanglement tensor of these particles, one obtains

$$
\mathbf {M} ^ {\prime} (1, 2) = \operatorname {d i a g} (0, 1, 0). \tag {57}
$$

This tensor does not vary with the phase shift of the single particles, so despite a nonvanishing  $\mathbf{M}_{yy}$  there is no two-particle fringe visibility, not even in the  $y$  direction, as can be seen from (40) and (45). The apparent contradiction between this result and Eq. (47) is simply resolved by observing that this unitary transformation is not general enough to yield (46). The two-particle entanglement can be seen by replacing the phase shifter and the symmetric (50:50) beam splitter by a unitary transformation of the form

$$
\hat {U} _ {m} = \left( \begin{array}{c c} \cos \left(\frac {\phi_ {m}}{2}\right) & i \sin \left(\frac {\phi_ {m}}{2}\right) \\ i \sin \left(\frac {\phi_ {m}}{2}\right) & \cos \left(\frac {\phi_ {m}}{2}\right) \end{array} \right) \tag {58}
$$

for particle  $m$ , which can be realized, e.g., by a nonsymmetric beam splitter. The entanglement matrix will be transformed to

$$
\mathbf {M} ^ {\prime} (1, 2) = \left( \begin{array}{c c c} 0 & 0 & 0 \\ 0 & \sin \left(\phi_ {1}\right) \sin \left(\phi_ {2}\right) & - \sin \left(\phi_ {1}\right) \cos \left(\phi_ {2}\right) \\ 0 & - \cos \left(\phi_ {1}\right) \sin \left(\phi_ {2}\right) & \cos \left(\phi_ {1}\right) \cos \left(\phi_ {2}\right) \end{array} \right). \tag {59}
$$

So a variation of the entanglement tensor is now seen to occur with the variation of the symmetry (i.e., of the reflectivity) of the beam splitter. It must be mentioned, however, that this is no single-particle effect, as the Bloch vectors of the single systems remain zero. It is remarkable that the strength of this effect is the same as for a maximal entangled two-particle pure state: Regarding, for example, measurements of the  $z$  component in both particles, we obtain a maximum  $\mathbf{M}_{zz}(1,2) = 1$ , which, due to the complementarity relation  $v_{m}^{2} + v_{12}^{2} = 1$ , would be the maximal possible value for a pure two-particle state.

# V. CONCLUSIONS AND OUTLOOK

In this paper we have investigated some concepts pertaining to the description of entanglement. The  $\mathrm{SU}(N)$  formalism applied to the density matrix turned out to be a powerful tool to find general properties of composite quantum systems. Within this formalism we found for a system composed of two subsystems a measure of entanglement, which fulfills some reasonable requirements. This measure has several advantages over other proposals known to us. First, it is completely based on the decomposition of the density matrix. There is no need for any diagonalization or maximization procedure. Second, like in the entropic definition [10], it is applicable for pure states as well as for mixed states. The original definition of entanglement as a state in the product Hilbert space, which cannot be factored into product states of the respective local systems, is naturally generalized in this way. Third, a generalization to the case of more than two subsystems is done in a straightforward way. This allows the investigation of such systems without need for ever new concepts. Such an unbiased generalization is necessary because systems composed of more than two subsystems show properties that are sometimes hard to classify by intuition. An example was given by the GHZ state, where the three-particle entanglement is inevitably connected with that of two particles. So the question has been raised of the independence of the different entanglement tensors in a complete description of an  $n$ -particle state. In the case of only two subsystems, this question was trivial in the sense that entanglement necessarily involves these two particles. Having more particles, however, the classification of the different kinds of entanglement is not a priori clear. There can be two-particle entanglement between arbitrary pairs of subsystems, three-particle entanglement, and so on. The problem of their mutual dependence should be of great importance in applications of composite quantum systems. An investigation of the general three-particle state, with each particle having only two levels, could already hint at such constraints.

Returning to the two-particle system, there remains another question concerning our three requirements on the entanglement measure. These requirements do not determine this measure uniquely: for example, the approach based on

the entropy of the subsystems [10] also fulfills them. So an investigation of the general properties of these requirements alone without referring to a special choice of an explicit realization would be highly desirable.

# ACKNOWLEDGMENTS

The authors wish to thank Abner Shimony for very valuable and stimulating discussions and his helpful remarks on this paper. Comments by Chris Fuchs, Richard Jozsa and Anton Zeilinger are gratefully acknowledged.

# APPENDIX A: DIAGONAL MATRICES IN  $\mathrm{SU}(N)$

The  $\mathrm{SU}(N)$  algebra is of rank  $N - 1$ , so there are  $N - 1$  matrices of the  $\mathrm{SU}(N)$  matrix representation that can simultaneously be diagonalized. In our convention (2), these are the  $N - 1$  operators  $\hat{w}_l$ . Their eigenvalues follow from the definition (2) as

$$
w _ {l} ^ {(n)} = - \sqrt {\frac {2}{l (l + 1)}}, \quad l \leqslant n \leqslant l
$$

$$
w _ {l} ^ {(l + 1)} = l \sqrt {\frac {2}{l (l + 1)}} \tag {A1}
$$

$$
w _ {l} ^ {(n)} = 0, \quad l + 1 <   n \leqslant N.
$$

Denoting in (2) the basis states  $|j\rangle$  as the eigenstates of the density matrix, its diagonal representation then reads

$$
\hat {\rho} = \frac {1}{N} \hat {1} + \frac {1}{2} \sum_ {l = 1} ^ {N - 1} \lambda_ {l} \hat {w} _ {l}, \tag {A2}
$$

with  $\lambda_l = \mathrm{tr}\{\hat{w}_l\hat{\rho}\}$ . Applying the eigenvalue equation

$$
\hat {\rho} | n \rangle = \rho_ {n} | n \rangle \tag {A3}
$$

to the projection operator  $\hat{P}_{mm}$ , the following sum rule of the eigenvalues  $w_{l}^{(n)}$  results:

$$
\sum_ {l = 1} ^ {N - 1} w _ {l} ^ {(m)} w _ {l} ^ {(n)} = 2 \delta_ {m n} - \frac {2}{N}. \tag {A4}
$$

# APPENDIX B: ROTATION MATRIX FOR THE SU(2) DENSITY MATRIX

For the general unitary matrix in a two-dimensional Hilbert space one can make the ansatz

$$
\mathbf {U} = \left( \begin{array}{c c} \cos (\theta) \exp \{i \varphi \} & \sin (\theta) \exp \{i \chi \} \\ - \sin (\theta) \exp \{- i \chi \} & \cos (\theta) \exp \{- i \varphi \} \end{array} \right), \tag {B1}
$$

where  $\theta$ ,  $\varphi$ , and  $\chi$  are real numbers. The overall phase factor was set to zero due to (10). The corresponding  $3\times 3$  rotation matrix (11) then reads

$$
\mathbf {T} = \left( \begin{array}{c c c} \cos^ {2} (\theta) \cos (2 \varphi) & \cos^ {2} (\theta) \sin (2 \varphi) & - \sin (2 \theta) \cos (\varphi + \chi) \\ - \sin^ {2} (\theta) \cos (2 \chi) & + \sin^ {2} (\theta) \sin (2 \chi) & \\ \sin^ {2} (\theta) \sin (2 \chi) & \cos^ {2} (\theta) \cos (2 \varphi) & \sin (2 \theta) \sin (\varphi + \chi) \\ - \cos^ {2} (\theta) \sin (2 \varphi) & + \sin^ {2} (\theta) \cos (2 \chi) & \\ \sin (2 \theta) \cos (\chi - \varphi) & - \sin (2 \theta) \sin (\chi - \varphi) & \cos (2 \theta) \end{array} \right). \tag {B2}
$$

In group theory, an analogous matrix is known as Cayley parametrization of the group SO(3) [25]. The above matrix describes a rotation with respect to the axis

$$
\hat {\omega} _ {i} = \left( \begin{array}{l} \sin (\theta) \sin (\chi) \\ \sin (\theta) \cos (\chi) \\ \cos (\theta) \sin (\varphi) \end{array} \right) \tag {B3}
$$

by the rotation angle  $\xi$  with

$$
\cos \left(\frac {\xi}{2}\right) = \cos (\theta) \cos (\varphi). \tag {B4}
$$

[1] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[2] J. S. Bell, Physics (N.Y.) 1, 195 (1964).  
[3] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[4] J. F. Clauser and A. Shimony, Rep. Prog. Phys. 41, 1881 (1978); D. Home and F. Selleri, Riv. Nuovo Cimento 14, 1 (1991), and references therein.  
[5] A. K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[6] C. H. Bennett et al., Phys. Rev. Lett. 70, 1895 (1993).  
[7] J. Brown, New Sci. 143, 21 (1994).  
[8] A. Shimony, Ann. N. Y. Acad. Sci. 755, 675 (1995).  
[9] A. Shimony (unpublished).  
[10] S. M. Barnett and S. J. D. Phoenix, Phys. Rev. A 44, 535 (1991).  
[11] G. Jaeger, M. A. Horne, and A. Shimony, Phys. Rev. A 48, 1023 (1993).  
[12] G. Jaeger, A. Shimony, and L. Vaidman, Phys. Rev. A 51, 54 (1995).  
[13] D. M. Greenberger, M. Horne, and A. Zeilinger, in Bell's Theorem, Quantum Theory, and Conceptions of the Universe, edited by M. Kafatos (Kluwer Academic, Dordrecht, 1989), pp. 73-

76; D. M. Greenberger, M. A. Horne, A. Shimony, and A. Zeilinger, Am. J. Phys. 58, 1131 (1990).  
[14] F. T. Hioe and J. H. Eberly, Phys. Rev. Lett. 47, 838 (1981).  
[15] U. Fano, Rev. Mod. Phys. 55, 855 (1983).  
[16] M. Keller and G. Mahler, J. Mod. Opt. 41, 2537 (1994).  
[17] G. Mahler and V. A. Weberruβ, Quantum Networks: Dynamics of Open Nanostructures (Springer, Berlin, 1995).  
[18] S. Fujita, Introduction to Non-Equilibrium Quantum Statistical Mechanics (Krieger, Malabar, FL, 1983).  
[19] J. von Neumann, Mathematical Foundations of Quantum Mechanics (Princeton University Press, Princeton, 1955).  
[20] L. P. Hughston, R. Jozsa, and W. K. Wooters, Phys. Lett. A 183, 14 (1993).  
[21] N. Gisin, Phys. Lett. A 154, 201 (1991).  
[22] S. M. Barnett and S. J. D. Phoenix, Phys. Lett. A 167, 233 (1992).  
[23] R. Horodecki, P. Horodecki, and M. Horodecki, Phys. Lett. A 200, 340 (1995).  
[24] H. Araki and E. H. Lieb, Commun. Math. Phys. 18, 160 (1970).  
[25] E. Stiefel and A. Füssler, Gruppentheoretische Methoden und ihre Anwendung (Teubner, Stuttgart, 1979).