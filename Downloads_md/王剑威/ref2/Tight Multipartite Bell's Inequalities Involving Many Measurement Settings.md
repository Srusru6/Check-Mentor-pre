# Tight Multipartite Bell's Inequalities Involving Many Measurement Settings

Wiesław Laskowski, $^{1}$  Tomasz Paterek, $^{1}$  Marek Žukowski, $^{1,2}$  and Časlav Brukner $^{2,3}$ \
 $^{1}$ Instytut Fizyki Teoretycznej i Astrofizyki, Universiryetet Gdańsk, PL-80-952 Gdańsk, Poland\
 $^{2}$ Institut für Experimentalphysik, Universität Wien, Boltzmanngasse 5, A-1090 Wien, Austria\
 $^{3}$ Blackett Laboratory, Imperial College London, London SW7 2BW, United Kingdom\
(Received 16 September 2003; revised manuscript received 30 August 2004; published 8 November 2004)

We derive tight Bell's inequalities for  $N > 2$  observers involving more than two alternative measurement settings. We give a necessary and sufficient condition for a general quantum state to violate the new inequalities. The inequalities are violated by some classes of states, for which all standard Bell's inequalities with two measurement settings per observer are satisfied.

DOI: 10.1103/PhysRevLett.93.200401

PACS numbers: 03.65.Ud, 03.67.Mn

Which quantum states do not allow a local realistic (LR) description? This question still remains open, mainly because our present tools to test local realism are not optimal. Most of Bell's inequalities are for the case in which only two measurement settings can be chosen by each observer, e.g., the Clauser-Horne-Shimony-Holt (CHSH) inequality [1], inequalities for bipartite higher-dimensional systems [2], multipartite Bell's inequalities [3-6]. One can call such inequalities "standard" ones.

One can expect that allowing the observers to choose between more than two observables should give more stringent constraints on LR models. Thus, new inequalities may extend the class of nonseparable states which cannot be described by LR variables. Violation of local realism is an important ingredient for building quantum information protocols that decrease the communication complexity [7] and is a criterion for the efficient quantum key distribution [8]. Multisetting Bell's inequalities may lead to such novel schemes.

Although various nonstandard Bell's inequalities are known [9-13], we still lack an efficient method for their derivation. A general way is to define the facets of the correlation polytope [9,13]. Yet, this is a computationally hard  $NP$  problem [14]. Recently, Wu and Zong [15] derived an inequality for three parties, which involves four local settings for two observers and two settings for the third one, and showed that it is stronger than the standard three-particle Bell inequalities.

Here, by generalizing the method of Ref. [15], we derive a wide class of tight Bell's inequalities for  $N > 2$  parties and many measurement settings. We find a single (general) Bell's inequality that generates all inequalities from this class. We also give a necessary and sufficient condition for the violation of the new inequalities by quantum predictions. Most importantly, the inequalities reveal violation of local realism for the classes of states, for which all standard Bell's inequalities [5,6] are satisfied.

We start with the case of  $N = 3$  observers. Suppose that the first two observers can choose between four settings, and the third one between two settings. We denote such

problem as  $4 \times 4 \times 2$ . Let  $A_{i}$  with  $i \in \{1, 2, 3, 4\}$  stand for the predetermined local realistic values for the first observer under the local setting  $i$ ,  $B_{j}$  with  $j \in \{1, 2, 3, 4\}$  for similar values for the second observer, and  $C_{k}$  with  $k \in \{1, 2\}$  for the values for the third observer (for the given run of the experiment). We assume that  $A_{i}, B_{j}$ , and  $C_{k}$  can take values  $+1$  or  $-1$ . Then the LR values satisfy the following algebraic identity:

$$
A _ {1 2, S ^ {\prime}} \equiv \sum_ {k, l = 1, 2} S ^ {\prime} (k, l) \left[ A _ {1} + (- 1) ^ {k} A _ {2} \right] \left[ B _ {1} + (- 1) ^ {l} B _ {2} \right] = \pm 4, \tag {1}
$$

where  $S^{\prime}(k,l)$  is any "sign" function, i.e., such that  $S^{\prime}(k,l) = \pm 1$ . Since  $|A_{i}| = |B_{j}| = 1$ , only one term in Eq. (1) does not vanish, and its value is  $\pm 4$ .

In an analogous way, one can define  $A_{34,S^{\prime \prime}}$  by replacing  $A_1, A_2, B_1, B_2$  by  $A_3, A_4, B_3, B_4$ , respectively, and  $S^{\prime}$  by  $S^{\prime \prime}$ . Depending on the value of  $m = \pm 1$  one has  $[A_{12,S^{\prime}} + (-1)^{m}A_{34,S^{\prime \prime}}] = \pm 8$  or 0. By analogy to (1) one has

$$
\begin{array}{l} A _ {1 2 3 4, 1 2} \equiv \sum_ {k, l = 1, 2} S (k, l) \left[ A _ {1 2, S ^ {\prime}} + (- 1) ^ {k} A _ {3 4, S ^ {\prime \prime}} \right] \left[ C _ {1} + (- 1) ^ {l} C _ {2} \right] \\ = \pm 1 6. \tag {2} \\ \end{array}
$$

After averaging over many runs of the experiment and introducing the correlation functions  $E_{ijk} \equiv \langle A_i B_j C_k \rangle_{\mathrm{avg}}$ , one obtains multisetting Bell's inequalities. Because of the freedom to choose the sign functions  $S, S', S''$ , we have  $(2^4)^3 = 2^{12}$  Bell's inequalities.

We now show that the family of  $2^{12}$  inequalities can be reduced to a single "generating" one. This inequality will be obtained for nonfactorable sign functions  $S, S', S''$ . Below we show that the choice of a factorable sign function is equivalent to having a nonfactorable one, and some of the local measurement settings equal. Thus, one does not need to consider factorable sign functions; one obtains inequalities for such sign functions from the generating Bell's inequality by making some settings equal.

To show this consider function  $S(k, l)$  as an example. In general  $S(k, l) = a(k) + b(k)(-1)^l$ , with either  $a(k) = 0$  or  $b(k) = 0$ , and  $|a(k)| + |b(k)| = 1$ . If  $S(k, l)$  is factor-

able (i.e., of the form  $S(k,l) = s_1(k)s_2(l)$  with  $s_1(k) = \pm s_2(l) = \pm 1$ ), then either  $b(k) \equiv 0$  or  $a(k) \equiv 0$ . If we choose, e.g.,  $b(k) \equiv 0$ , then the last factor on the left-hand side of Eq. (2) has the following form:

$$
\begin{array}{l} \sum_ {l = 1, 2} S (k, l) \left[ C _ {1} + (- 1) ^ {l} C _ {2} \right] (3) \\ = \sum_ {l = 1, 2} [ a (k) + b (k) (- 1) ^ {l} ] [ C _ {1} + (- 1) ^ {l} C _ {2} ] (4) \\ = 2 a (k) C _ {1} + 2 b (k) C _ {2} = 2 a (k) C _ {1}. (5) \\ \end{array}
$$

The setting "2" for the third observer drops out. The final expression (5) can be also obtained, for the nonfactorable  $S$ , by putting  $C_1 = C_2$ . Further, if one inserts this result into Eq. (2), and, say,  $a(k) \equiv 1$ , then after the summation over  $k$  the whole term with settings 3, 4 for the first two observers vanishes. What we get is a trivial extension of the CHSH inequalities.

The whole family of multisetting Bell's inequalities can be reduced to one generating inequality which is obtained for  $S, S', S''$  nonfactorable. In such cases  $a(k) = \pm \frac{1 \pm (-1)^k}{2}$  and  $b(k) = \pm \frac{1 \mp (-1)^k}{2}$  (the front signs are free; those in the numerators have to be different for the two functions). Any other cases are obtainable by the sign changes  $X_i \to -X_i$  ( $X = A, B, C$ ). The generating Bell's inequality can be chosen as

$$
\left\langle \left(C _ {1} + C _ {2}\right) \left[ A _ {1} \left(B _ {1} + B _ {2}\right) + A _ {2} \left(B _ {1} - B _ {2}\right) \right] + \right.
$$

$$
\left. \left(C _ {1} - C _ {2}\right) \left[ A _ {3} \left(B _ {3} + B _ {4}\right) + A _ {4} \left(B _ {3} - B _ {4}\right) \right] \right\rangle_ {\text {a v g}} \leq 4. \tag {6}
$$

Other inequalities can be obtained by making some settings equal. For example, the  $3 \times 3 \times 2$  ones can be obtained by choosing the settings 1 and 2 identical for the first two observers.

The method can be generalized for various choices of the number of parties and the measurement settings. Here we present the  $2^{N - 1} \times 2^{N - 1} \times 2^{N - 2} \times \dots \times 2$  ones.

Take the case of  $N = 4$  observers. We start with the identity (2). One can introduce a similar identity for the settings  $\{5,6,7,8\}$ , for the first two observers, and  $\{3,4\}$ , for the third one. The fourth observer chooses between two settings with LR values  $D_{1}$  and  $D_{2}$ . Applying the same method as before, one obtains an identity which generates Bell's inequalities of the  $8 \times 8 \times 4 \times 2$  type:

$$
\begin{array}{l} \sum_ {k, l = 1, 2} S (k, l) \left[ A _ {1 2 3 4, 1 2} + (- 1) ^ {k} A _ {5 6 7 8, 3 4} \right] \times \\ [ D _ {1} + (- 1) ^ {l} D _ {2} ] = \pm 6 4, \tag {7} \\ \end{array}
$$

where  $A_{1234,12}$  and  $A_{5678,34}$  depend on some three sign functions. One may apply this method iteratively, increasing the number of observers by one, to obtain inequalities involving an exponential (in  $N$ ) number of measurement settings as given above.

The inequalities are tight. We give the proof for the case of  $4 \times 4 \times 2$  inequalities. It can be adapted to all inequalities discussed here. The left-hand side of the

identity (2) is equal to  $\pm 16$  for any combination of predetermined LR results. In a 32-dimensional real space, one can build a convex polytope, containing all possible LR models of the correlation functions for the specified settings, with vertices (generators) given by the tensor products of  $\nu = (A_{1}, A_{2}, A_{3}, A_{4}) \otimes (B_{1}, B_{2}, B_{3}, B_{4}) \otimes (C_{1}, C_{2})$ . It has 256 different vertices. Tight Bell inequalities define the half-spaces in which is the polytope, which contain a face of it in their border hyperplane. If 32 linearly independent vertices belong to a hyperplane, this hyperplane defines a tight inequality. Half of the vertices saturate the inequality bounded by 16 and another half saturate the inequality with  $-16$  bound. Every vertex,  $\nu$ , saturating the first inequality, has a partner  $-\nu$ , which saturates the other one. Any set of 128 vertices  $\nu$ , which does not contain pairs  $\nu$  and  $-\nu$  contains a set of 32 linearly independent points (basis). Thus, each inequality is tight.

The necessary and sufficient condition for violation of multisetting Bell's inequalities.-To this end we first rederive the necessary and sufficient condition for violation of the CHSH inequality by an arbitrary two-qubit state [16]. The derivation uses certain mathematical ideas that are later applied in the analysis of more general cases. We use a decomposition of general mixed state of  $N$  qubits in terms of the identity operator  $\sigma_0 = \mathbb{1}$  in the Hilbert space of individual qubits and the Pauli operators  $\sigma_{i}$  for three orthogonal directions  $i\in \{1,2,3\}$ , given by  $\rho = \frac{1}{2^N}\times \sum_{k_1,\ldots ,k_N = 0}^{3}T_{k_1\dots k_N}\sigma_{k_1}\otimes \dots \otimes \sigma_{k_N}$ . The (real) coefficients  $T_{k_1\dots k_N}$ , with  $k_{j} = 1,2,3$ , form the correlation tensor  $\hat{T}$ .

The full set of inequalities for the  $2 \times 2$  problem is derivable from the identity (1) and reads

$$
\left| \left\langle \sum_ {k, l = 1, 2} S (k, l) \left[ A _ {1} + (- 1) ^ {k} A _ {2} \right] \left[ B _ {1} + (- 1) ^ {l} B _ {2} \right] \right\rangle_ {\text {a v g}} \right| \leq 4. \tag {8}
$$

The quantum correlation function  $E(\vec{A}, \vec{B})$  is given by the scalar product of the correlation tensor  $\hat{T}$  with the tensor product of the local measurement settings represented by unit vectors  $\vec{A} \otimes \vec{B}$ , i.e.,  $E(\vec{A}, \vec{B}) = (\vec{A} \otimes \vec{B}) \cdot \hat{T}$ . Thus, the condition for a quantum state endowed with the correlation tensor  $\hat{T}$  to satisfy the inequality (8) is that for all directions  $\vec{A}_1, \vec{A}_2, \vec{B}_1, \vec{B}_2$  one has

$$
\left| \left\{\sum_ {k, l = 1, 2} S (k, l) [ \vec {A} _ {1} + (- 1) ^ {k} \vec {A} _ {2} ] \otimes [ \vec {B} _ {1} + (- 1) ^ {l} \vec {B} _ {2} ] \right\} \cdot \hat {T} \right| \leq 4.
$$

One can use the following fact. If  $\vec{X}_1$  and  $\vec{X}_2$  are unit vectors, then  $\vec{X}_1 + \vec{X}_2$  and  $\vec{X}_1 - \vec{X}_2$  are orthogonal, and  $|\vec{X}_1 + \vec{X}_2|^2 + |\vec{X}_1 - \vec{X}_2|^2 = 4$ . Therefore one can always find two orthogonal unit vectors  $\vec{X}(m)$ , with  $m = 1, 2$ , given by  $\vec{X}_1 + (-1)^m \vec{X}_2 = 2x_m \vec{X}(m)$ , such that the coefficients satisfy  $\sum_{m} x_m^2 = 1$ . Using this convention for  $\vec{X}_i = \vec{A}_i$ ,  $\vec{B}_i$  and  $x_i = a_i$ ,  $b_i$  one obtains

$$
\left| \left[ \sum_ {k, l = 1, 2} S (k, l) a _ {k} b _ {l} \vec {A} (k) \otimes \vec {B} (l) \right] \cdot \hat {T} \right| \leq 1. \tag {9}
$$

However,  $[\vec{A}(k) \otimes \vec{B}(l)] \cdot \hat{T} = T_{kl}$  are components of the tensor  $\hat{T}$  in some local coordinate systems of Alice and Bob which involve vectors  $\vec{A}(k)$  and  $\vec{B}(l)$  as orthogonal Cartesian coordinate directional vectors. Put  $\vec{A}(1) = \hat{x} = \hat{x}_1$ ,  $\vec{A}(2) = \hat{y} = \hat{x}_2$  for Alice's coordinate system, and similarly  $\vec{B}(1) = \hat{x} = \hat{x}_1$ ,  $\vec{B}(2) = \hat{y} = \hat{x}_2$  for Bob's system. Thus the inequality (9) can be expressed as  $\sum_{k,l=1,2} S(k, l) a_k b_l T_{kl} \leq 1$ . Since one can always make the vector  $(\pm a_1 b_1, \pm a_1 b_2, \pm a_2 b_1, \pm a_2 b_2)$  parallel to any vector  $(T_{11}, T_{12}, T_{21}, T_{22})$ , the maximal value of the left-hand side of the inequality (9) is equal to  $\max[\sum_{k,l=1,2} T_{kl}^2]$ . Thus,  $\max[\sum_{k,l=1,2} T_{kl}^2] \leq 1$  is the necessary and sufficient condition for the inequality to hold, for any measurement settings, provided the maximization is taken over all local coordinate systems of two observers.

Consider now  $4 \times 4 \times 2$  inequalities:

$$
\left| \left\langle \sum_ {k, l} S (k, l) \left[ A _ {1 2, S ^ {\prime}} + (- 1) ^ {k} A _ {3 4, S ^ {\prime \prime}} \right] \left[ C _ {1} + (- 1) ^ {l} C _ {2} \right] \right\rangle_ {\text {a v g}} \right| \leq 1 6, \tag {10}
$$

where  $S, S', S''$  are some nonfactorable sign functions. The three-qubit quantum correlation functions  $E(\vec{A}_i, \vec{B}_j, \vec{C}_k)$  can be represented as  $(\vec{A}_i \otimes \vec{B}_j \otimes \vec{C}_k) \cdot \hat{T}$  (with the same meaning of the symbols as before;  $\hat{T}$  is now a three index tensor). Thus the condition for the  $4 \times 4 \times 2$  inequalities to hold, in the quantum case, transforms into

$$
\left. \right.\left|\left[ \hat {A} _ {1 2, S ^ {\prime}} \otimes (\vec {C} _ {1} + \vec {C} _ {2}) + \hat {A} _ {3 4, S ^ {\prime \prime}} \otimes (\vec {C} _ {1} - \vec {C} _ {2}) \right] \cdot \hat {T} \right| \leq 8, \tag {11}
$$

where, e.g.,

$$
\hat {A} _ {1 2, S ^ {\prime}} = \sum_ {k, l = 1, 2} S ^ {\prime} (k, l) [ \vec {A} _ {1} + (- 1) ^ {k} \vec {A} _ {2} ] \otimes [ \vec {B} _ {1} + (- 1) ^ {l} \vec {B} _ {2} ].
$$

To write down (11) we have used the freedom of introducing the sign changes  $\vec{X}_i\rightarrow -\vec{X}_i$  ; compare (6). By defining  $\vec{C}_1 + \vec{C}_2 = 2c_2\vec{C} (2)$  and  $\vec{C}_1 - \vec{C}_2 = 2c_1\vec{C} (1)$  in Eq. (11), which have the properties of  $\vec{X} (m)$  , one obtains

$$
\left| c _ {2} \hat {A} _ {1 2, S ^ {\prime}} \otimes \vec {C} (2) \cdot \hat {T} + c _ {1} \hat {A} _ {3 4, S ^ {\prime \prime}} \otimes \vec {C} (1) \cdot \hat {T} \right| \leq 4. \tag {12}
$$

One can always choose  $c_2$  and  $c_1$  that maximize the left-hand side. Since  $\sum_{i=1,2} c_i^2 = 1$  this leads to the condition

$$
[ \hat {A} _ {1 2, S ^ {\prime}} \cdot \hat {T} ^ {(2)} ] ^ {2} + [ \hat {A} _ {3 4, S ^ {\prime \prime}} \cdot \hat {T} ^ {(1)} ] ^ {2} \leq 4 ^ {2}, \tag {13}
$$

where  $\hat{T}^{(l)}$  is defined by  $T_{ij}^{(l)} = \sum_{k=1}^{3} C(l)_k T_{ijk}$ , where in turn  $C(l)_k$  is the  $k$ th component of vector  $\vec{C}(l)$ . Note that since  $\vec{C}(1)$  and  $\vec{C}(2)$  are orthogonal and normalized this procedure amounts to fixing of two (new) Cartesian axes for the third observer, and accordingly transforming the

correlation tensor. Since  $\hat{A}_{12,S'}$  depends on different vectors than  $\hat{A}_{34,S''}$ , one can maximize the two terms separately. Furthermore, since the problem of maximization of  $\hat{A}_{nm,S} \cdot \hat{T}^{(l)}$  is equivalent to the  $2 \times 2$  case studied earlier, the overall maximization process gives the following necessary and sufficient condition for quantum correlations to satisfy the inequality:

$$
\max  \sum_ {x = 1, 2} \sum_ {k _ {x}, l _ {x} = 1, 2} T _ {k _ {x} l _ {x} x} ^ {2} \leq 1. \tag {14}
$$

When compared with the sufficient condition for  $2 \times 2 \times 2$  inequalities to hold [6], namely,

$$
\max  \left[ \sum_ {k, l, m = 1, 2} T _ {k l m} ^ {2} \right] \leq 1,
$$

the new condition is more demanding because the Cartesian coordinate systems denoted by the indices  $k_{1}, l_{1}$  and  $k_{2}, l_{2}$  do not have to be the same.

Consider now Bell's inequalities of the type  $8 \times 8 \times 4 \times 2$ . They are given by the average of Eq. (7) over many runs of the experiment. The generating Bell's inequality has the form

$$
\left| \left\langle A _ {1 2 3 4, 1 2} \left(D _ {1} + D _ {2}\right) + A _ {5 6 7 8, 3 4} \left(D _ {1} - D _ {2}\right) \right\rangle_ {\text {a v g}} \right| \leq 3 2.
$$

For the quantum predictions  $E(\vec{A}_i, \vec{B}_j, \vec{C}_k, \vec{D}_s)$ , given by  $(\vec{A}_i \otimes \vec{B}_j \otimes \vec{C}_k \otimes \vec{D}_s) \cdot \hat{T}$ , the inequality holds if

$$
\left(\left[ \hat {A} _ {1 2 3 4, 1 2} \otimes \vec {D} (1) \right] \cdot \hat {T}\right) ^ {2} + \left(\left[ \hat {A} _ {5 6 7 8, 3 4} \otimes \vec {D} (2) \right] \cdot \hat {T}\right) ^ {2} \leq 1 6 ^ {2}.
$$

The problem of maximization of either squared expression is similar to the problem of the  $4 \times 4 \times 2$  case, where now  $\hat{T}^{(l)}$  has components  $T_{ijk}^{(l)} = \sum_{r=1}^{3} D(l)_r T_{ijk r}$ . We can use the same maximization algorithm as before. We get the following sufficient and necessary condition for violation of  $8 \times 8 \times 4 \times 2$  inequalities:

$$
\max  \sum_ {y = 1, 2} \sum_ {x _ {y} = 1, 2} \sum_ {k _ {x y}, l _ {x y} = 1, 2} T _ {k _ {x y} l _ {x y}. x _ {y}. y} ^ {2} \leq 1. \tag {15}
$$

Obviously in a similar way one can reach analogous conditions for violation of  $2^{N - 1} \times 2^{N - 1} \times 2^{N - 2} \times \dots \times 2$  inequalities by quantum predictions.

The new conditions lead to more stringent constraints on a LR description of quantum predictions than that for the standard inequalities. We now show some classes of states that violate multisetting Bell's inequalities, but for which all standard inequalities, as of Refs. [4-6] are satisfied. As a measure of the violation we use the minimal amount of white noise that must be admixed to a quantum state for a conflict with LR prediction to disappear.

Generalized GHZ states:  $|\psi \rangle = \cos \alpha |00\cdots 0\rangle + \sin \alpha |11\cdots 1\rangle$ . These states, although pure, satisfy all standard Bell's inequalities for correlation functions for  $\sin 2\alpha \leq 1 / \sqrt{2^{N - 1}}$  and  $N$  odd [17,18]. Their nonvanishing correlation tensor components are (directions  $x, y, z$  are

denoted by  $1,2,3$ ; the basis  $\{|0\rangle ,|1\rangle \}$  is the eigenbasis of  $\sigma_z$ :  $T_{3\dots 3} = \cos 2\alpha$ , for  $N$  odd, and  $1$  for  $N$  even,  $T_{1\dots 1} = \sin 2\alpha$ , and the components with  $2k$  indices equal to  $2$  and the rest equal to  $1$  take the value  $(-1)^{k}\sin 2\alpha$  (there are  $2^{N - 2}$  such components). Let us assume that the last observer can choose only between settings  $x$  and  $z$ . Thus, we obtain for the condition for violation of multi-setting Bell's inequality for  $N$  observers [generalization of condition (15)]

$$
\begin{array}{l} \sum_ {k _ {1}, \dots , k _ {N - 1} = x, y} T _ {k _ {1}} ^ {2} \dots . _ {k _ {N - 1} x} + \\ \sum_ {k _ {1}, \dots , k _ {N - 1} = x, z} T _ {k _ {1} \dots k _ {N - 1} z} ^ {2} = 2 ^ {N - 2} \sin^ {2} 2 \alpha + \cos^ {2} 2 \alpha > 1. \tag {16} \\ \end{array}
$$

Thus, Bell's inequalities are violated for the whole range of  $\pi /4\geq \alpha >0$  and for arbitrary  $N$  in contrast to the case of standard Bell's inequalities. Note that we did not perform any maximization.

The  $|W\rangle$  state.

$$
1 / \sqrt {N} (| 1 0 0 \dots 0 \rangle + | 0 1 0 \dots 0 \rangle + \dots + | 0 0 0 \dots 1 \rangle).
$$

Assume that all  $N$  observers choose between observables in the plane spanned by  $y$  and  $z$  axes. Nonvanishing correlation tensor components are  $T_{z:\dots z} = 1$  and components, of modulus equal to  $2 / N$ , with only two indices  $x$  (or  $y$ ) and all other indices equal to  $z$ . Therefore the  $\sum_{k_1,k_2,\ldots ,k_N = y,z}T_{k_1\dots k_N}^2$  can be at least (no optimization was made)  $1 + \binom{N}{2}\frac{4}{N^2} = 3 - 2 / N > 1$ . Thus, if one considers a noise admixture to the  $|W\rangle$  states, in such a form that one arrives at a mixed state  $\rho_{|W\rangle} = (1 - V)\rho_{\mathrm{noise}} + V|W\rangle \langle W|$ , with  $\rho_{\mathrm{noise}} = \mathbb{1} / 2^{N}$ , then the new inequalities show that for  $V > V_{\mathrm{thr}} = 1 / \sqrt{3 - 2 / N}$  there is no LR description for correlations. This is a bigger range of  $V$  than for the standard correlation function Bell inequalities; compare [19].

Finally consider the state [4]

$$
\begin{array}{l} | \Psi \rangle = \sqrt {1 / 3} [ | 0 0 0 0 \rangle + | 1 1 1 1 \rangle + \frac {1}{2} (| 1 0 1 0 \rangle + | 0 1 0 1 \rangle \\ + \left. \left| 0 1 1 0 \right\rangle + \left| 1 0 0 1 \right\rangle\right) ] \\ = \sqrt {2 / 3} | \mathrm {G H Z} \rangle_ {1 2 3 4} + \sqrt {1 / 3} | \mathrm {E P R} \rangle_ {1 2} | \mathrm {E P R} \rangle_ {3 4}, \tag {17} \\ \end{array}
$$

where  $|\mathrm{EPR}\rangle = 1 / \sqrt{2} (|01\rangle + |10\rangle)$  is the maximally entangled (Bell-EPR) two-qubit state. This entangled state was produced in a recent experiment [20]. Its nonvanishing correlation tensor components are

$$
T _ {x x x x} = T _ {y y y y} = T _ {z z z z} = 1,
$$

$$
T _ {x x y y} = T _ {x x z z} = T _ {y y x x} = T _ {y y z z} = T _ {z z x x} = T _ {z z y y} = - 1 / 3,
$$

$$
T _ {x z x z} = T _ {x z z x} = T _ {z x x z} = T _ {z x z x} = 2 / 3,
$$

$$
\begin{array}{l} T _ {x y x y} = T _ {x y y x} = T _ {y x x y} = T _ {y x y x} = T _ {y z y z} = T _ {y z z y} = T _ {z y y z} \\ = T _ {z y z y} = - 2 / 3. \\ \end{array}
$$

The left-hand side of (15) is equal to 4, e.g., if all local summations are over  $x$  and  $y$ . Thus the  $8 \times 8 \times 4 \times 2$  inequality is violated by the factor 2. Therefore a state  $(1 - V)\rho_{\mathrm{noise}} + V|\Psi \rangle \langle \Psi|$  gives nonclassical correlations

for  $V > 0.5$ . In contrast, standard Bell inequalities cannot be violated for  $V \leq 0.5303$ .

In summary, we present multipartite Bell's inequalities involving many measurement settings and prove that they give more stringent conditions on the possibility of a local realistic description of quantum states than the standard Bell's inequalities for two settings per observer.

We thank Marcin Wiesniak for discussions. The work is part of the Austrian-Polish project Quantum Communication and Quantum Information (2004-2005) and the MNiI Grant No. PBZ-MIN-008/P03/2003. C.B. is supported by Austrian FWF Project No. F1506 and by the European Commission, Marie Curie Fellowship, Project No. 500764. W.L. and T.P. are supported by FNP. M.Z. is supported by the Subsydium Profesorskie FNP. Numerical calculations were carried out at the Academic Computer Center in Gdańsk.

[1] J. Clauser et al., Phys. Rev. Lett. 23, 880 (1969).  
[2] D. Kaszlikowski et al., Phys. Rev. Lett. 85, 4418 (2000); D. Collins et al., ibid. 88, 040404 (2002).  
[3] N.D. Mermin, Phys. Rev. Lett. 65, 1838 (1990); M. Ardehali, Phys. Rev. A 46, 5375 (1992); A.V. Belinskii and D.N. Klyshko, Phys. Usp. 36, 653 (1993).  
[4] H. Weinfurter and M. Zukowski, Phys. Rev. A 64, 010102(R) (2001).  
[5] R. F. Werner and M. W. Wolf, Phys. Rev. A 64, 032112 (2001).  
[6] M. Zukowski and C. Brukner, Phys. Rev. Lett. 88, 210401 (2002).  
[7] R. Cleve and H. Burhman, Phys. Rev. A 56, 1201 (1997); C. Brukner, M. Zukowski, and A. Zeilinger, Phys. Rev. Lett. 89, 197901 (2002); C. Brukner et al., ibid. 92, 127901 (2004); H. Buhrman et al., ibid. 91, 047903 (2003).  
[8] V. Scarani and N. Gisin, Phys. Rev. Lett., 87, 117901 (2001); A. Acin, N. Gisin, and V. Scarani, Quantum Inf. Comput. 3 No. 6, 563 (2003).  
[9] I. Pitowsky and K. Svozil, Phys. Rev. A 64, 014102 (2001).  
[10] M. Zukowski, Phys. Lett. A 177, 290 (1993).  
[11] N. Gisin, Phys. Lett. A 260, 1 (1999); S. Massar, Phys. Rev. A 65, 032121 (2002); S. Massar et al., Phys. Rev. A 66, 052112 (2002).  
[12] S. Massar and S. Pironio, Phys. Rev. A 68, 062109 (2003).  
[13] C. Sliwa, Phys. Lett. A 317, 3 (2003); 317, 165 (2003); D. Collins and N. Gisin, J. Phys. A 37, 1775 (2004).  
[14] I. Pitowsky, Math. Programming 50, 395 (1991).  
[15] X.-H. Wu and H.-S. Zong, Phys. Lett. A 307, 262 (2003); for generalization, see X.-H. Wu and H.-S. Zong, Phys. Rev. A 68, 032102 (2003).  
[16] R. Horodecki, P. Horodecki, and M. Horodecki, Phys. Lett. A 200, 340 (1995).  
[17] V. Scarani and N. Gisin, J. Phys. A 34, 6043 (2001).  
[18] M. Žukowski et al., Phys. Rev. Lett. 88, 210402 (2002).  
[19] A. Sen(De) et al., Phys. Rev. A 68, 062306 (2003).  
[20] M. Eibl et al., Phys. Rev. Lett. 90, 200403 (2003).