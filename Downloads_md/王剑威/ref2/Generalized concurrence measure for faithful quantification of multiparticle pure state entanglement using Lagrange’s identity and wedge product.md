# Generalized concurrence measure for faithful quantification of multiparticle pure state entanglement using Lagrange's identity and wedge product

Vineeth S. Bhaskara<sup>1</sup>  $\cdot$  Prasanta K. Panigrahi<sup>2</sup>

Received: 26 November 2016 / Accepted: 4 March 2017 / Published online: 21 March 2017  
 $\text{©}$  Springer Science+Business Media New York 2017

Abstract Concurrence, introduced by Hill and Wootters (Phys Rev Lett 78:5022, 1997), provides an important measure of entanglement for a general pair of qubits that is faithful: strictly positive for entangled states and vanishing for all separable states. Such a measure captures the entire content of entanglement, providing necessary and sufficient conditions for separability. We present an extension of concurrence to multiparticle pure states in arbitrary dimensions by a new framework using the Lagrange's identity and wedge product representation of separability conditions, which coincides with the "I-concurrence" of Rungta et al. (Phys Rev A 64:042315, 2001) who proposed by extending Wootters's spin-flip operator to a so-called universal inverter superoperator. Our framework exposes an inherent geometry of entanglement and may be useful for the further extensions to mixed and continuous variable states.

Keywords Quantum entanglement  $\cdot$  Separability  $\cdot$  Multiparticle pure states  $\cdot$  Lagrange's identity  $\cdot$  Wedge product

# 1 Introduction

A deeper understanding of inseparability or entanglement is of fundamental importance for the understanding of intrinsic quantum correlations. It has far-reaching

applications in quantum computation and information theory [1]. Entanglement forms an elementary resource in quantum computation and various quantum communication protocols [2,3]. Detecting and quantifying this resource is of great practical application.

Quantifying entanglement faithfully in a multiparticle scenario is central to quantum information theory so that one can estimate how close quantum states are to classical ones, and characterize the efficiency of protocols deterministically, which use entanglement as a resource [4-6]. Recent interest on the connections between quantum entanglement and the emergence of space-time [7,8] also calls for a systematic study of the geometry-entanglement relationship with the quantification of entanglement playing a subtler role in the context of quantum gravity.

For the two-qubit case, an important measure of entanglement is the concurrence [9], which is strictly positive for entangled states and vanishing for separable states. It provides the necessary and sufficient conditions of separability for a general pair of qubits. An extension of concurrence for multiparticle pure states is the "I-concurrence" introduced by Rungta et al. [10]. They generalized the spin-flip superoperator to act on quantum systems of arbitrary dimensions and introduced the corresponding generalized concurrence for joint pure states of bipartite quantum systems.

In this paper, we present a similar generalization of concurrence to multiparticle pure states of arbitrary dimensions that is faithful by a new framework using the Lagrange's identity and wedge product representation, leading to a measure of entanglement identical to the I-concurrence. This framework reveals an essential geometry of entanglement and may be useful for further extension of concurrence to other complex systems of interest.

There have been works on a similar spirit, of which some include the study by Sawicki et al. [11] on the symplectic geometry of entanglement, Nielsen [12] on the connection between the algebra of majorization and entanglement transformations, Zhu [13] on the structure of quantum correlations of many-body systems, Duan et al. [14] and Simon [15] on the entanglement in continuous variable systems.

# 2 Separability for pure multiparticle states and the central result

For future convenience, we define separability for pure multiparticle states. Consider a  $n$ -particle pure quantum system. Let  $P|Q$  be a bipartition of this composite(whole) system  $P \cup Q$ , with respective Hilbert spaces  $\mathcal{H}_P$  and  $\mathcal{H}_Q$  for the states of the subsystems  $P$  and  $Q$ ; then, the state space of the composite system is given by the tensor product  $\mathcal{H} = \mathcal{H}_P \otimes \mathcal{H}_Q$ . If a pure state  $|\psi \rangle \in \mathcal{H}$  of the composite system can be written in the form

$$
| \psi \rangle = | \phi \rangle_ {P} \otimes | \chi \rangle_ {Q},
$$

where  $|\phi \rangle_{P} \in \mathcal{H}_{P}$  and  $|\chi \rangle_{Q} \in \mathcal{H}_{Q}$  are the pure states of the sub-systems  $P$  and  $Q$ , respectively, then the system is said to be separable across the bipartition  $P|Q$ . Alternatively, the sub-system  $P$  is separable from the composite system  $P \cup Q$ . Otherwise, the sub-systems  $P$  and  $Q$  are said to be entangled.

To state the central result of the paper, consider a  $n$ -particle system with particles labeled by  $(k)$ ,  $k = 1,2,\ldots,n$ . Suppose  $|\psi\rangle$  is any pure state of the system and  $\rho = |\psi\rangle \langle \psi|$  be its density matrix. Let  $\mathcal{M}$  be the set of the particular particles whose bipartite separability from the composite system is of interest with cardinality  $m (< n)$ . Then the generalized concurrence,  $E_{\mathcal{M}}$ , for the bipartition  $\mathcal{M}|\overline{\mathcal{M}}$  is given, in equivalent forms, as  $(\overline{\mathcal{M}}$  being the complementary set of  $\mathcal{M}$ ):

$$
\begin{array}{l} E _ {\mathcal {M}} ^ {2} = 4 \sum_ {i <   j} \left(\rho_ {i i} ^ {\mathcal {M}} \rho_ {j j} ^ {\mathcal {M}} - \rho_ {i j} ^ {\mathcal {M}} \rho_ {j i} ^ {\mathcal {M}}\right) = 4 \sum_ {i <   j} \lambda_ {i} \lambda_ {j} \\ = 2 \left[ 1 - \operatorname {t r} \left[ (\rho^ {\mathcal {M}}) ^ {2} \right] \right], \\ \end{array}
$$

where  $\rho^{\mathcal{M}}\stackrel {\mathrm{def}}{=}\sum_{j}\langle j|\overline{\mathcal{M}} (|\psi \rangle \langle \psi |)|j\rangle_{\overline{\mathcal{M}}} = \mathrm{Tr}_{\overline{\mathcal{M}}}(\rho)$  is the reduced density matrix on the sub-system  $\mathcal{M}$  obtained by tracing out the sub-system  $\overline{\mathcal{M}}$  , and  $\lambda_{i}$  are the eigenvalues of  $\rho^{\mathcal{M}}$

$E_{\mathcal{M}}$  vanishes iff the system is separable across the bipartition  $\mathcal{M}|\overline{\mathcal{M}}$  and takes the maximum value iff  $\rho^{\mathcal{M}}$  is maximally mixed. A measure of global entanglement would then be the sum of measures for distinct bipartitions of the system. Evidently, a composite system is separable across all bipartitions if and only if every single-particle bipartition is separable. Therefore, the necessary and sufficient criterion for separability across all bipartitions is  $\sum_{k=1}^{n} E_{(k)}^{2} = 0$ , where  $\rho^{(k)}$  is the single-particle reduced density matrix of  $\rho$  on particle  $(k)$ .

One can arrive at the result by considering the simple case of a two-qubit system and subsequently generalizing the framework to multiparticle systems in arbitrary dimensions.

# 3 Two-qubit concurrence using Lagrange's identity and wedge product framework

Consider a two-qubit system with qubits  $A$  and  $B$ . Let  $|\psi \rangle$  be a normalized pure state of the system with

$$
| \psi \rangle = p | 0 _ {A} 0 _ {B} \rangle + q | 0 _ {A} 1 _ {B} \rangle + r | 1 _ {A} 0 _ {B} \rangle + s | 1 _ {A} 1 _ {B} \rangle
$$

$(p,q,r,s\in \mathbb{C})$  . Rewriting the state as:

$$
\begin{array}{l} | \psi \rangle = | 0 _ {A} \rangle \left(p | 0 _ {B} \rangle + q | 1 _ {B} \rangle\right) + | 1 _ {A} \rangle \left(r | 0 _ {B} \rangle + s | 1 _ {B} \rangle\right) \\ = | 0 _ {A} \rangle \langle 0 _ {A} | \psi \rangle + | 1 _ {A} \rangle \langle 1 _ {A} | \psi \rangle , \tag {1} \\ \end{array}
$$

the bipartition  $A|B$  is separable if and only if the vectors  $\langle 0_A|\psi \rangle = p|0_B\rangle +q|1_B\rangle$  and  $\langle 1_A|\psi \rangle = r|0_B\rangle +s|1_B\rangle$  (or equivalently  $\langle 0_B|\psi \rangle$  and  $\langle 1_B|\psi \rangle$ ) are parallel, i.e., if and only if

$$
\frac {p}{r} = \frac {q}{s} \Rightarrow p s - q r = 0. \tag {2}
$$

Then the modulus of  $ps - qr$  is a faithful measure of entanglement for two qubits, which vanishes only for separable states. This condition may be elegantly written using the notation of a wedge product, which generalizes easily to multiparticle systems in arbitrary dimensions, as we show subsequently.

In geometric algebra [16], the wedge product of two vectors is seen as a particular generalization of cross product to higher dimensions and is defined as follows. Consider any two vectors  $\vec{a}$  and  $\vec{b}$  in  $\mathbb{C}^m$  written in the orthonormal basis  $\{\hat{e}_i\}_{i=1}^m$ . Their wedge product is a bivector in the  $^m C_2$ -dimensional exterior space with basis  $\{\hat{e}_i\}_{i=1}^m \wedge \{\hat{e}_j\}_{j=1}^m$  defined, by stipulating that  $\hat{e}_i \wedge \hat{e}_j = -\hat{e}_j \wedge \hat{e}_i$  and  $\hat{e}_i \wedge \hat{e}_i = 0$ , as:

$$
\overrightarrow {a} \wedge \overrightarrow {b} = \sum_ {i = 1} ^ {m - 1} \sum_ {j = i + 1} ^ {m} \left(a _ {i} b _ {j} - a _ {j} b _ {i}\right) \hat {e} _ {i} \wedge \hat {e} _ {j}, \tag {3}
$$

with  $\overrightarrow{a} \wedge \overrightarrow{a} = 0$  and  $\overrightarrow{a} \wedge \overrightarrow{b} = (-1)\overrightarrow{b} \wedge \overrightarrow{a}$ . In the coordinate notation  $\overrightarrow{a} \wedge \overrightarrow{b}$  may be written as:

$$
\begin{array}{l} (a _ {1} b _ {2} - a _ {2} b _ {1}, a _ {1} b _ {3} - a _ {3} b _ {1}, \dots , a _ {1} b _ {m} - a _ {m} b _ {1}, a _ {2} b _ {3} - a _ {3} b _ {2}, \dots , \\ a _ {2} b _ {m} - a _ {m} b _ {2}, \dots , a _ {m - 1} b _ {m} - a _ {m} b _ {m - 1}). \\ \end{array}
$$

This representation allows one to write the separability conditions in a compact and useful form. We note  $||\langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle || = ||\langle 0_B|\psi \rangle \wedge \langle 1_B|\psi \rangle || = |ps - qr|$ , which is the measure of entanglement for the case of a two-qubit pure state.  $||\langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle ||$  geometrically represents the area of the complex parallelotope formed by the vectors  $\langle 0_A|\psi \rangle$  and  $\langle 1_A|\psi \rangle$  in the Hilbert space of qubit B. We write the two-qubit measure of entanglement as  $E = 2||\langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle || = 2||\langle 0_B|\psi \rangle \wedge \langle 1_B|\psi \rangle || = 2|ps - qr|$ , which is the concurrence [9] for two-qubit pure states defined by Hill and Wootters as  $C(\psi) = |\langle \psi |\tilde{\psi}\rangle | = 2|ps - qr|$ , where  $|\tilde{\psi}\rangle = \sigma_y|\psi^*\rangle$ ,  $\sigma_y = \left( \begin{array}{cc}0 & -i\\ i & 0 \end{array} \right)$  and  $|\psi^{*}\rangle$  is the complex conjugate of  $|\psi\rangle$ .

For maximal entanglement by this measure, the area of the parallelotope,  $|ps - qr|$ , must be maximum, which implies that the parallelotope must be a square with its sides taking the maximum possible value. As the sum of the squares of the sides is constrained to be 1 (by normalization), i.e.,  $|\langle 0_A|\psi \rangle|^2 + |\langle 1_A|\psi \rangle|^2 = 1$ , the area is maximized when each of the side of the square equals  $\frac{1}{\sqrt{2}}$ . Then,  $E_{(max)} = 1$ $0 \leq E \leq 1$ . Therefore, for maximal entanglement,

$$
\begin{array}{l} | \langle 0 _ {A} | \psi \rangle | = | \langle 1 _ {A} | \psi \rangle | = \frac {1}{\sqrt {2}}, | \langle 0 _ {B} | \psi \rangle | = | \langle 1 _ {B} | \psi \rangle | = \frac {1}{\sqrt {2}}, \\ (\langle 0 _ {A} | \psi \rangle) ^ {\dagger} \langle 1 _ {A} | \psi \rangle = 0, (\langle 0 _ {B} | \psi \rangle) ^ {\dagger} \langle 1 _ {B} | \psi \rangle = 0. \\ \end{array}
$$

These conditions for maximal entanglement are identical to the condition of the reduced density matrix being maximally mixed.

Recall the generalized Lagrange's identity [17] for vectors in  $\mathbb{C}^m$ , which is a generalization of the Brahmagupta-Fibonacci identity [18] and a special form of

the Binet-Cauchy identity [19,20]. Consider two vectors  $\vec{a}$ ,  $\vec{b} \in \mathbb{C}^m$ . Then the Lagrange's identity takes the form:  $\| \vec{a} \|^{2} \| \vec{b} \|^{2} - |\vec{a} \cdot \vec{b}|^{2} = \| \vec{a} \wedge \vec{b} \|^{2}$  ( $\| \cdot \|$  representing the norm of a vector and  $|\cdot|$  the modulus of a scalar), i.e.,

$$
\left(\sum_ {k = 1} ^ {m} \left| a _ {k} \right| ^ {2}\right) \left(\sum_ {k = 1} ^ {m} \left| b _ {k} \right| ^ {2}\right) - \left| \sum_ {k = 1} ^ {m} a _ {k} \overline {{b _ {k}}} \right| ^ {2} = \sum_ {i = 1} ^ {m - 1} \sum_ {j = i + 1} ^ {m} \left| a _ {i} b _ {j} - a _ {j} b _ {i} \right| ^ {2} \tag {4}
$$

where  $\overline{b_k}$  represents the complex conjugate of  $b_{k}$  (see "Appendix" for proof). The norm of the wedge product  $\vec{a} \wedge \vec{b}$  calculated by RHS of Eq. (4) takes  $\mathcal{O}(m^2)$  steps, while calculating the same using the LHS takes only  $\mathcal{O}(m)$  steps. Therefore, this identity when applied to the wedge product representation of the separability conditions results in a computationally lesser intensive expression, asymptotically with increasing number of particles and dimensions, in terms of the traces of the squared reduced density matrices of the pure state.

By this identity, one may write  $E_A^2 = 4||\langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle ||^2 = 4||(p,q)\wedge (r,s)||^2$  as  $\left[4(|p|^2 +|q|^2)(|r|^2 +|s|^2) - 4|p\overline{r} +q\overline{s}|^2\right]$ . By noting this to be the determinant of the reduced density matrix on qubit A  $(\rho^{A})$ , by definition, as  $\rho$  in this case is

$$
\rho = \left( \begin{array}{c c c c} | p | ^ {2} & p \overline {{q}} & p \overline {{r}} & p \overline {{s}} \\ q \overline {{p}} & | q | ^ {2} & q \overline {{r}} & q \overline {{s}} \\ r \overline {{p}} & r \overline {{q}} & | r | ^ {2} & r \overline {{s}} \\ s \overline {{p}} & s \overline {{q}} & s \overline {{r}} & | s | ^ {2} \end{array} \right),
$$

and therefore the reduced density matrix on  $\mathbf{A}$ ,  $\rho^A$ , takes the form:

$$
\begin{array}{l} \rho^ {A} = \langle 0 _ {B} | \rho | 0 _ {B} \rangle + \langle 1 _ {B} | \rho | 1 _ {B} \rangle \\ = \left( \begin{array}{c c} | p | ^ {2} + | q | ^ {2} & p \overline {{r}} + q \overline {{s}} \\ r \overline {{p}} + s \overline {{q}} & | r | ^ {2} + | s | ^ {2} \end{array} \right), \\ \end{array}
$$

one may, thus, rewrite the two-qubit measure of entanglement as  $E = 2\sqrt{det(\rho^A)} = 2\sqrt{det(\rho^B)}$ . This may further be written as

$$
\begin{array}{l} E _ {A} ^ {2} = 4 d e t (\rho^ {A}) = 4 \sum_ {i <   j} \left(\rho_ {i i} ^ {A} \rho_ {j j} ^ {A} - \rho_ {i j} ^ {A} \rho_ {j i} ^ {A}\right) \\ = 4 \left[ \frac {1}{2} \sum_ {i, j} \left(\rho_ {i i} ^ {A} \rho_ {j j} ^ {A} - \rho_ {i j} ^ {A} \rho_ {j i} ^ {A}\right) \right] \\ \end{array}
$$

$$
\begin{array}{l} = 4 \left[ \frac {1}{2} \left(\left[ \operatorname {t r} \left(\rho^ {A}\right) \right] ^ {2} - \operatorname {t r} \left[ (\rho^ {A}) ^ {2} \right]\right) \right] (5) \\ = 2 \left[ 1 - \operatorname {t r} \left[ \left(\rho^ {A}\right) ^ {2} \right] \right], (6) \\ \end{array}
$$

since the trace of a valid density matrix is unity and for any square matrix  $M$ ,  $\sum_{i,j} M_{ij} M_{ji} = \operatorname{tr}(M^2)$ , and  $\sum_{i,j} M_{ii} M_{jj} = \sum_i M_{ii} \sum_j M_{jj} = \operatorname{tr}(M)^2$ .

The characteristic polynomial of a  $m \times m$  matrix  $M$  in  $t$  is given by:

$$
t ^ {m} - (\operatorname {t r} M) t ^ {m - 1} + \frac {1}{2} \left(\operatorname {t r} (M) ^ {2} - \operatorname {t r} (M ^ {2})\right) t ^ {m - 2} + \dots + (- 1) ^ {m} (\det  M).
$$

So Eq. (5) is the  $t^{m - 2}$  coefficient (except for a constant) of the characteristic polynomial of the  $m\times m$  reduced density matrix  $\rho^A$ . This can be thought of as the first step, interpolating between the trace of  $\rho^A$  (which is the  $t^{m - 1}$  coefficient) and the determinant of  $\rho^A$  (which is the constant coefficient). The roots of the characteristic polynomial are precisely the eigenvalues of  $\rho^A$ . If the eigenvalues of  $\rho^A$  are  $\lambda_1,\ldots ,\lambda_m$  then [21]

$$
E _ {A} ^ {2} = 4 \left[ \frac {1}{2} \left(1 - \sum_ {i} \lambda_ {i} ^ {2}\right) \right] = 4 \sum_ {i <   j} \lambda_ {i} \lambda_ {j}. \tag {7}
$$

This mathematical setting extends in a straightforward way to more general cases in higher dimensions, and a global faithful measure of entanglement may be written down by summing over the contribution of each of the independent bipartitions of the general pure state as we show subsequently.

# 4 Extension to multiparticle states in arbitrary dimensions

Consider a  $n$ -particle pure state  $|\psi \rangle$  in arbitrary dimensions with the particles labeled by  $\{1, 2, \dots, n\}$  in an orthonormal basis as

$$
| \psi \rangle = \sum_ {j _ {1}, j _ {2}, \dots , j _ {n} = 0} ^ {d _ {1} - 1, d _ {2} - 1, \dots , d _ {n} - 1} a _ {j _ {1} j _ {2} \dots j _ {n}} | j _ {1} \rangle \otimes | j _ {2} \rangle \otimes \dots \otimes | j _ {n} \rangle , \tag {8}
$$

where particle  $i$  has access to a  $d_{i}$ -dimensional Hilbert space, and  $a_{j_1j_2\dots j_n}$  are the complex amplitudes. That is, particle  $i$ , when isolated, may be described by  $d_{i}$  discrete orthonormal basis set  $\{|0\rangle ,|1\rangle ,\ldots ,|d_i - 1\rangle \}$ . Therefore,  $|\psi \rangle$  exists in a  $D$ -dimensional Hilbert space where  $D = \prod_{i = 1}^{n}d_{i}$ . For convenience, one might omit the upper limits of the summation in Eq. (8) by noting that each summation index  $j_{i}$  appropriately goes from 0 to  $d_{i} - 1$ .

Consider the bipartite separability of a particular set  $\mathcal{M}$  of  $m$ -particles ( $m < n$ ) out of the  $n$ -particle system. Without any loss of generality, let the  $m$ -particles be labeled by  $\{1, 2, \ldots, m\}$ , so that the particles labeled by  $\{m + 1, m + 2, \ldots, n\}$  represent the

rest of  $(n - m)$ -particles belonging to the complement set  $\overline{\mathcal{M}}$ . One may rewrite the state  $|\psi \rangle$  as

$$
\begin{array}{l} | \psi \rangle = \sum_ {j _ {1}, j _ {2}, \dots , j _ {n}} a _ {j _ {1} j _ {2} \dots j _ {n}} (| j _ {1} \rangle \otimes | j _ {2} \rangle \otimes \dots \otimes | j _ {m} \rangle) \otimes (| j _ {m + 1} \rangle \otimes | j _ {m + 2} \rangle \otimes \dots \otimes | j _ {n} \rangle) \\ = \sum_ {j _ {1}, j _ {2}, \dots , j _ {m}} \sum_ {j _ {m + 1}, \dots , j _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} j _ {m + 1} \dots j _ {n}} | j _ {1} j _ {2} \dots j _ {m} \rangle \otimes | j _ {m + 1} \dots j _ {n} \rangle \\ = \sum_ {j _ {1}, j _ {2}, \dots , j _ {m}} \left[ | j _ {1} j _ {2} \dots j _ {m} \rangle \otimes \left(\sum_ {j _ {m + 1}, \dots , j _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} j _ {m + 1} \dots j _ {n}} | j _ {m + 1} \dots j _ {n} \rangle\right) \right]. \tag {9} \\ \end{array}
$$

By noting that

$$
\langle k _ {1} k _ {2} \dots k _ {m} | \psi \rangle = \sum_ {j _ {m + 1}, \dots , j _ {n}} a _ {k _ {1} k _ {2} \dots k _ {m} j _ {m + 1} \dots j _ {n}} | j _ {m + 1} \dots j _ {n} \rangle , \tag {10}
$$

Eq. (9) may be expressed as

$$
| \psi \rangle = \sum_ {j _ {1}, \dots , j _ {m}} | j _ {1} j _ {2} \dots j _ {m} \rangle \otimes [ \langle j _ {1} j _ {2} \dots j _ {m} | \psi \rangle ]. \tag {11}
$$

Therefore, for the separability of  $|\psi \rangle$  across  $\mathcal{M}|\overline{\mathcal{M}}$  bipartition, one needs the set of vectors  $\{\langle j_1j_2\ldots j_m|\psi \rangle \}_{j_1,\dots,j_m}$  in  $\mathbb{C}^{D_{n - m}}$  (where  $D_{n - m} = \prod_{i = m + 1}^{n}d_{i}$ ) to be parallel for the  $m$ -particle state to factor out of  $|\psi \rangle$ . Therefore, the mutual wedge products among  $\{\langle j_1j_2\ldots j_m|\psi \rangle \}_{j_1,\dots,j_m}$  must vanish for the required bipartite separability. This is a necessary and sufficient condition of separability across  $\mathcal{M}|\overline{\mathcal{M}}$  as noted before. Hence, one may construct a faithful measure of entanglement across the bipartition as

$$
E _ {\mathcal {M}} ^ {2} = 4 \sum_ {i _ {1}, \dots , i _ {m}} \sum_ {\substack {j _ {1} \geq i _ {1}, \dots , j _ {m} \geq i _ {m} \\ | i _ {1} - j _ {1} | + \dots + | i _ {m} - j _ {m} | \neq 0}} \left| \left| \langle i _ {1} i _ {2} \dots i _ {m} \mid \psi \rangle \wedge \langle j _ {1} j _ {2} \dots j _ {m} \mid \psi \rangle \right| \right| ^ {2}, \tag{12}
$$

where the norm is computed in the orthogonal basis  $\{|k_{m + 1}\ldots k_n\rangle \wedge |l_{m + 1}\ldots l_n\rangle \}$ , and  $|i_1 - j_1| + \dots +|i_m - j_m|\neq 0$  ensures that not all  $i_p$  are equal to  $j_{p}$  simultaneously  $\forall p$  in which case the wedge product trivially vanishes. There are  $D_{m}C_{2}$  terms in the above summation where  $D_{m} = \prod_{i = 1}^{m}d_{i}$ . Noting that  $|k_{m + 1}\ldots k_n\rangle \wedge |l_{m + 1}\ldots l_n\rangle = -|l_{m + 1}\ldots l_n\rangle \wedge |k_{m + 1}\ldots k_n\rangle$  by definition, consider

$$
\begin{array}{l} \langle i _ {1} i _ {2} \dots i _ {m} | \psi \rangle \wedge \langle j _ {1} j _ {2} \dots j _ {m} | \psi \rangle \\ = \left(\sum_ {k _ {m + 1}, \dots , k _ {n}} a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} | k _ {m + 1} \dots k _ {n} \rangle\right) \\ \wedge \left(\sum_ {l _ {m + 1}, \dots , l _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} l _ {m + 1} \dots l _ {n}} | l _ {m + 1} \dots l _ {n} \rangle\right) \\ = \sum_ {k _ {m + 1}, \dots , k _ {n}} \sum_ {l _ {m + 1}, \dots , l _ {n}} a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} l _ {m + 1} \dots l _ {n}} | k _ {m + 1} \dots k _ {n} \rangle \wedge | l _ {m + 1} \dots l _ {n} \rangle \\ = \sum_{k_{m + 1},\ldots ,k_{n}}\sum_{\substack{l_{m + 1}\geq k_{m + 1},\ldots ,l_{n}\geq k_{n}\\ |i_{m + 1} - k_{m + 1}| + \dots +|l_{n} - k_{n}|\neq 0}} \\ \end{array}
$$

$$
\left(a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} l _ {m + 1} \dots l _ {n}} - a _ {i _ {1} i _ {2} \dots i _ {m} l _ {m + 1} \dots l _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} k _ {m + 1} \dots k _ {n}}\right)
$$

$$
\left| k _ {m + 1} \dots k _ {n} \right\rangle \wedge \left| l _ {m + 1} \dots l _ {n} \right\rangle .
$$

Therefore,

$$
\begin{array}{l} \left| \left| \left\langle i _ {1} i _ {2} \dots i _ {m} | \psi \right\rangle \wedge \left\langle j _ {1} j _ {2} \dots j _ {m} | \psi \right\rangle \right| \right| ^ {2} \\ = \sum_{k_{m + 1},\ldots ,k_{n}}\sum_{\substack{l_{m + 1}\geq k_{m + 1},\ldots ,l_{n}\geq k_{n}\\ |i_{m + 1} - k_{m + 1}| + \dots +|l_{n} - k_{n}|\neq 0}} \\ \left| a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} l _ {m + 1} \dots l _ {n}} - a _ {i _ {1} i _ {2} \dots i _ {m} l _ {m + 1} \dots l _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} k _ {m + 1} \dots k _ {n}} \right| ^ {2}. \\ \end{array}
$$

By the generalized Lagrange's identity Eq. (4), one may write the above expression equivalently as

$$
\begin{array}{l} = \left(\sum_ {k _ {m + 1}, \dots , k _ {n}} \left| a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} \right| ^ {2}\right) \left(\sum_ {l _ {m + 1}, \dots , l _ {n}} \left| a _ {j _ {1} j _ {2} \dots j _ {m} l _ {m + 1} \dots l _ {n}} \right| ^ {2}\right) \\ \left. - \left| \sum_ {k _ {m + 1}, \dots , k _ {n}} \left(a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} \bar {a} _ {j _ {1} j _ {2} \dots j _ {m} k _ {m + 1} \dots k _ {n}}\right) \right| ^ {2}. \right. \\ \end{array}
$$

Hence, the entanglement measure may be explicitly written in terms of the amplitudes of the wavefunction in equivalent forms as

$$
\begin{array}{l} E_{\mathcal{M}}^{2} = 4\sum_{i_{1},\ldots ,i_{m}}\sum_{\substack{j_{1}\geq i_{1},\ldots ,j_{m}\geq i_{m}\\ |i_{1} - j_{1}| + \dots +|i_{m} - j_{m}|\neq 0}}\sum_{k_{m + 1},\ldots ,k_{n}}\sum_{\substack{l_{m + 1}\geq k_{m + 1},\ldots ,l_{n}\geq k_{n}\\ |i_{m + 1} - k_{m + 1}| + \dots +|l_{n} - k_{n}|\neq 0}} \\ \left| a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} l _ {m + 1} \dots l _ {n}} - a _ {i _ {1} i _ {2} \dots i _ {m} l _ {m + 1} \dots l _ {n}} a _ {j _ {1} j _ {2} \dots j _ {m} k _ {m + 1} \dots k _ {n}} \right| ^ {2} \\ \end{array}
$$

$$
\begin{array}{l} = 4\sum_{i_{1},\ldots ,i_{m}}\sum_{\substack{j_{1}\geq i_{1},\ldots ,j_{m}\geq i_{m}\\|i_{1} - j_{1}| + \dots +|i_{m} - j_{m}|\neq 0}}\left[\left(\sum_{k_{m + 1},\ldots ,k_{n}}\bigl|a_{i_{1}i_{2}\ldots i_{m}k_{m + 1}\ldots k_{n}}\bigr|^{2}\right) \\ \left(\sum_ {l _ {m + 1}, \dots , l _ {n}} \left| a _ {j _ {1} j _ {2} \dots j _ {m} l _ {m + 1} \dots l _ {n}} \right| ^ {2}\right) \\ - \left| \sum_ {k _ {m + 1}, \dots , k _ {n}} a _ {i _ {1} i _ {2} \dots i _ {m} k _ {m + 1} \dots k _ {n}} \bar {a} j _ {1} j _ {2} \dots j _ {m} k _ {m + 1} \dots k _ {n} \right| ^ {2} \Bigg ]. \tag {13} \\ \end{array}
$$

The measure  $E_{\mathcal{M}}$  is constructed (with appropriate constants) so that it coincides with Wootters's concurrence for the case of a two-qubit system.

Considering the pure state density matrix of the system as

$$
\begin{array}{l} \rho = | \psi \rangle \langle \psi | \\ = \left(\sum_ {j _ {1}, j _ {2}, \dots , j _ {n}} a _ {j _ {1} j _ {2} \dots j _ {n}} | j _ {1} j _ {2} \dots j _ {n} \rangle\right) \left(\sum_ {i _ {1}, i _ {2}, \dots , i _ {n}} \bar {a} _ {i _ {1} i _ {2} \dots i _ {n}} \langle i _ {1} i _ {2} \dots i _ {n} |\right) \\ = \sum_ {j _ {1}, j _ {2}, \dots , j _ {n}} \sum_ {i _ {1}, i _ {2}, \dots , i _ {n}} a _ {j _ {1} j _ {2} \dots j _ {n}} \bar {a} _ {i _ {1} i _ {2} \dots i _ {n}} | j _ {1} j _ {2} \dots j _ {n} \rangle \langle i _ {1} i _ {2} \dots i _ {n} |, \tag {14} \\ \end{array}
$$

one may define the reduced density matrix  $\rho_{\mathcal{M}}$  of  $\mathcal{M}$  by tracing out  $\overline{\mathcal{M}}$  as

$$
\begin{array}{l} \rho^ {\mathcal {M}} \stackrel {\text {d e f}} {=} \operatorname {T r} _ {\overline {{\mathcal {M}}}} (\rho) = \sum_ {k _ {m + 1}, \dots , k _ {n}} \langle k _ {m + 1} \dots k _ {n} | \rho | k _ {m + 1} \dots k _ {n} \rangle \\ = \sum_ {k _ {m + 1}, \dots , k _ {n}} \sum_ {j _ {1}, \dots , j _ {n}} \sum_ {i _ {1}, \dots , i _ {n}} a _ {j _ {1} \dots j _ {m} j _ {m + 1} \dots j _ {n}} \bar {a} _ {i _ {1} \dots i _ {m} i _ {m + 1} \dots i _ {n}} \\ \end{array}
$$

$$
\begin{array}{l} \langle k _ {m + 1} \dots k _ {n} | j _ {1} \dots j _ {m} j _ {m + 1} \dots j _ {n} \rangle \\ \langle i _ {1} \dots i _ {m} i _ {m + 1} \dots i _ {n} | k _ {m + 1} \dots k _ {n} \rangle \\ = \sum_ {j _ {1}, \dots , j _ {n}} \sum_ {i _ {1}, \dots , i _ {n}} \underbrace {\left[ \sum_ {k _ {m + 1} , \dots , k _ {n}} a _ {j _ {1} \dots j _ {m} k _ {m + 1} \dots k _ {n}} \bar {a} _ {i _ {1} \dots i _ {m} k _ {m + 1} \dots k _ {n}} \right]} | j _ {1} \dots j _ {m} \rangle \langle i _ {1} \dots i _ {m} | \\ \text {m a t r i x e l e m e n t o f t h e r e d u c e d d e n s i t y m a t r i x} \\ = \sum_ {j _ {1}, \dots , j _ {n}} \sum_ {i _ {1}, \dots , i _ {n}} \rho_ {j i} ^ {\mathcal {M}} | j _ {1} \dots j _ {m} \rangle \langle i _ {1} \dots i _ {m} |, \tag {15} \\ \end{array}
$$

where  $j$  and  $i$  are the indices of the reduced density matrix. The matrix element at the index  $ji$  is given by  $\rho_{ji}^{\mathcal{M}} = \langle j_1 \ldots j_m | \rho^{\mathcal{M}} | i_1 \ldots i_m \rangle$ . Therefore, one arrives at the result considering

$$
\begin{array}{l} 2 \left[ 1 - \operatorname {T r} \left[ \left(\rho^ {\mathcal {M}}\right) ^ {2} \right] \right] \\ = 4 \sum_ {i <   j} \left(\rho_ {i i} ^ {\mathcal {M}} \rho_ {j j} ^ {\mathcal {M}} - \rho_ {i j} ^ {\mathcal {M}} \rho_ {j i} ^ {\mathcal {M}}\right) [ \text {b y E q . (6)} ], \\ = 4\sum_{i_{1},\ldots ,i_{m}}\sum_{\substack{j_{1}\geq i_{1},\ldots ,j_{m}\geq i_{m}\\ |i_{1} - j_{1}| + \dots +|i_{m} - j_{m}|\neq 0}} \\ \left(\langle i _ {1} \dots i _ {m} | \rho^ {\mathcal {M}} | i _ {1} \dots i _ {m} \rangle \langle j _ {1} \dots j _ {m} | \rho^ {\mathcal {M}} | j _ {1} \dots j _ {m} \rangle \right. \\ \left. \left. - \langle i _ {1} \dots i _ {m} | \rho^ {\mathcal {M}} | j _ {1} \dots j _ {m} \rangle \langle j _ {1} \dots j _ {m} | \rho^ {\mathcal {M}} | i _ {1} \dots i _ {m} \rangle\right) \right. \\ = E _ {\mathcal {M}} ^ {2} [ \text {f r o m E q . (1 3) a n d E q . (1 5)} ]. \\ \end{array}
$$

Since  $1 / D_{m} \leq \mathrm{Tr}\left[\left(\rho \mathcal{M}\right)^{2}\right] \leq 1$  (where the minimum is achieved when  $\rho_{\mathcal{M}}$  is maximally mixed),  $0 \leq E_{\mathcal{M}}^{2} \leq 2 - 2 / D_{m}$ . Maximal entanglement across  $\mathcal{M}|\overline{\mathcal{M}}$  is attained with  $E_{\mathcal{M}} = \sqrt{2 - 2 / D_{m}}$  iff  $\rho_{\mathcal{M}}$  is maximally mixed, by this measure. We analyze the above construction for the cases of a three-qubit, four-qubit and two-qutrit system to assess the generalization.

Three-qubit states Consider the three-qubit case. Let a normalized pure state of the three-qubit system be  $|\psi \rangle$  with density matrix  $\rho = |\psi \rangle \langle \psi |$  and with qubits labeled by  $A, B$  and  $C$ . Let

$$
\begin{array}{l} | \psi \rangle = p | 0 _ {A} 0 _ {B} 0 _ {C} \rangle + q | 0 _ {A} 0 _ {B} 1 _ {C} \rangle + r | 0 _ {A} 1 _ {B} 0 _ {C} \rangle + s | 0 _ {A} 1 _ {B} 1 _ {C} \rangle \\ + t \left| 1 _ {A} 0 _ {B} 0 _ {C} \right\rangle + u \left| 1 _ {A} 0 _ {B} 1 _ {C} \right\rangle + v \left| 1 _ {A} 1 _ {B} 0 _ {C} \right\rangle + w \left| 1 _ {A} 1 _ {B} 1 _ {C} \right\rangle \\ = | 0 _ {A} \rangle \left[ p | 0 _ {B} 0 _ {C} \rangle + q | 0 _ {B} 1 _ {C} \rangle + r | 1 _ {B} 0 _ {C} \rangle + s | 1 _ {B} 1 _ {C} \rangle \right] \\ + \left| 1 _ {A} \right\rangle \left[ t \left| 0 _ {B} 0 _ {C} \right\rangle + u \left| 0 _ {B} 1 _ {C} \right\rangle + v \left| 1 _ {B} 0 _ {C} \right\rangle + w \left| 1 _ {B} 1 _ {C} \right\rangle \right] \\ = | 0 _ {A} \rangle \langle 0 _ {A} | \psi \rangle + | 1 _ {A} \rangle \langle 1 _ {A} | \psi \rangle \\ \end{array}
$$

$(p,q,r,s,t,u,v,w\in \mathbb{C})$ . Similar to the two-qubit case, for separability of qubit A (i.e., the bipartition  $A|BC$  ) here, the vectors  $\langle 0_A|\psi \rangle ,\langle 1_A|\psi \rangle$  must be parallel. This yields the condition for separability of qubit A to be:

$$
\frac {p}{t} = \frac {q}{u} = \frac {r}{v} = \frac {s}{w}. \tag {16}
$$

The separability condition may be written in the wedge product representation as  $\langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle = 0$ , which is equivalent to the relations in Eq. (16) on cross-multiplying, since:

$$
\begin{array}{l} (p, q, r, s) \wedge (t, u, v, w) \\ = (p u - q t, p v - r t, p w - s t, q v - r u, q w - s u, r w - s v), \\ \end{array}
$$

by the coordinate notation of the wedge product defined previously. Therefore, the bipartite separability  $A|BC \Leftrightarrow \langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle = 0$ . Hence, its norm is a deterministic measure of entanglement of qubit  $A$  with system  $BC$ . By the Lagrange's identity,  $\| \langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle \| ^2$  turns out to be equal to the determinant of qubit  $A$ 's reduced density matrix  $\rho^A$  by definition, similar to the previous case. Therefore, one can write the global measure of entanglement for a three-qubit system, considering independent bipartitions, as:

$$
\begin{array}{l} E = E _ {A} + E _ {B} + E _ {C} \\ = 2 | | \langle 0 _ {A} | \psi \rangle \wedge \langle 1 _ {A} | \psi \rangle | | + 2 | | \langle 0 _ {B} | \psi \rangle \wedge \langle 1 _ {B} | \psi \rangle | | + \\ 2 | | \langle 0 _ {C} | \psi \rangle \wedge \langle 1 _ {C} | \psi \rangle | | \\ = 2 \left[ \sqrt {d e t (\rho^ {A})} + \sqrt {d e t (\rho^ {B})} + \sqrt {d e t (\rho^ {C})} \right]. \\ \end{array}
$$

This can be rewritten in terms of eigenvalues of the reduced density matrices by the derivation in Eq. (7). The maximum norm of each of the wedge products above is  $= \frac{1}{2}$ . Therefore,  $0 \leq E \leq 3$ . The  $|GHZ\rangle_3$  state is maximally entangled three-qubit state with  $E = 3$ , by this measure, and for the  $|W\rangle_3$  state,  $E = 2\sqrt{2} \simeq 2.828$ , which suggests that it is highly entangled but lesser than  $|GHZ\rangle_3$  state, where:  $|GHZ\rangle_3 = \frac{1}{\sqrt{2}}(|0_A0_B0_C\rangle + |1_A1_B1_C\rangle)$  and  $|W\rangle_3 = \frac{1}{\sqrt{3}}(|1_A0_B0_C\rangle + |0_A1_B0_C\rangle + |0_A0_B1_C\rangle)$ .

Analogously, for a  $n$ -qubit system with pure state  $|\psi \rangle$  and density operator  $\rho$ , separability of qubit labeled by " $i$ " ( $\leq n$ )  $\Leftrightarrow \langle 0_i |\psi \rangle \wedge \langle 1_i |\psi \rangle = 0$ . By Lagrange's identity this simplifies to:  $det(\rho^i) = 0$ . Therefore, a particular qubit is separable from a  $n$ -qubit system if and only if its corresponding single-qubit reduced density matrix is singular. For the separability of the system across every bipartition, each single-qubit reduced density matrix being singular is necessary and sufficient.

Four-qubit states Consider a four-qubit system with qubits labeled by  $A$ ,  $B$ ,  $C$  and  $D$ . Let  $|\psi \rangle$  be its pure state with density matrix  $\rho = |\psi \rangle \langle \psi|$ .  $E_A = 2\| \langle 0_A|\psi \rangle \wedge \langle 1_A|\psi \rangle \| = 2\sqrt{det(\rho^A)}$  determines the separability of qubit A or qubit system (BCD) from the composite system (ABCD), similar to the previous cases. Analogous to the previous construction, for the separability of qubits (AB) or (CD) from the system, the vectors  $\langle 0_A0_B|\psi \rangle$ ,  $\langle 0_A1_B|\psi \rangle$ ,  $\langle 1_A0_B|\psi \rangle$ ,  $\langle 1_A1_B|\psi \rangle$  in the Hilbert space  $\mathcal{H}_{\mathcal{CD}}$  of qubit system (CD) must be parallel. This can be seen by writing  $|\psi \rangle$  as  $[|0_A0_B\rangle \langle 0_A0_B|\psi \rangle + |0_A1_B\rangle \langle 0_A1_B|\psi \rangle + |1_A0_B\rangle \langle 1_A0_B|\psi \rangle + |1_A1_B\rangle \langle 1_A1_B|\psi \rangle]$ . Therefore, a non-vanishing wedge product of one of the vectors with any other among  $\langle 0_A0_B|\psi \rangle$ ,  $\langle 0_A1_B|\psi \rangle$ ,  $\langle 1_A0_B|\psi \rangle$  and  $\langle 1_A1_B|\psi \rangle$  indicates entanglement of the subsystems (AB) and (CD). Therefore, define  $E_{AB}$  as:

$$
\begin{array}{l} E _ {A B} ^ {2} = 4 \left[ | | \langle 0 _ {A} 0 _ {B} | \psi \rangle \wedge \langle 0 _ {A} 1 _ {B} | \psi \rangle | | ^ {2} + | | \langle 0 _ {A} 0 _ {B} | \psi \rangle \wedge \langle 1 _ {A} 0 _ {B} | \psi \rangle | | ^ {2} \right. \\ + | | \langle 0 _ {A} 0 _ {B} | \psi \rangle \wedge \langle 1 _ {A} 1 _ {B} | \psi \rangle | | ^ {2} \\ + | | \langle 0 _ {A} 1 _ {B} | \psi \rangle \wedge \langle 1 _ {A} 0 _ {B} | \psi \rangle | | ^ {2} + | | \langle 0 _ {A} 1 _ {B} | \psi \rangle \wedge \langle 1 _ {A} 1 _ {B} | \psi \rangle | | ^ {2} \\ \left. + \left| \left| \langle 1 _ {A} 0 _ {B} | \psi \rangle \wedge \langle 1 _ {A} 1 _ {B} | \psi \rangle \right| \right| ^ {2} \right]. \tag {17} \\ \end{array}
$$

Therefore, separability of bipartition  $AB|CD \Leftrightarrow E_{AB} = 0$ . Again by the Lagrange's identity, the expression Eq. (17) for  $E_{AB}^{2}$  simplifies to the similar form as:

$$
\begin{array}{l} E _ {A B} ^ {2} = 4 \sum_ {i, j = 1, i <   j} ^ {2 ^ {2}} \left(\rho_ {i i} ^ {A B} \rho_ {j j} ^ {A B} - \rho_ {i j} ^ {A B} \rho_ {j i} ^ {A B}\right) \\ = 4 \sum_ {i <   j} \lambda_ {i} \lambda_ {j} = 2 \left[ 1 - \operatorname {t r} [ (\rho^ {A B}) ^ {2} ] \right], \\ \end{array}
$$

where  $\lambda_{i}$  are the eigenvalues of  $\rho^{AB}$ . Note that the term  $\sum_{i,j=1,i<j}^{2^2} \left( \rho_{ii}^{AB} \rho_{jj}^{AB} - \rho_{ij}^{AB} \rho_{ji}^{AB} \right)$  above is not the determinant of  $\rho^{AB}$ . Therefore, the generalizing expression is in terms of the traces of the squared reduced density matrices but not in terms of their determinants for general cases. Similar expressions follow for  $E_{AC}^2$  and  $E_{AD}^2$ . Considering independent bipartitions, one can write the global measure of entanglement for the four-qubit system as:

$$
E = E _ {A} + E _ {B} + E _ {C} + E _ {D} + E _ {A B} + E _ {A C} + E _ {A D}.
$$

Evidently,  $E$  takes the maximum value only when the reduced density matrices are maximally mixed. Therefore,  $E_{(max)} = 4 + \frac{3\sqrt{6}}{2} \simeq 7.674$  for maximal entanglement, by this measure. But this may not be attained for the case of a four-qubit system, as shown by Higuchi et al. [22]. Therefore,  $0 \leq E < 4 + \frac{3\sqrt{6}}{2}$ .

For  $|GHZ\rangle_4 = \frac{1}{\sqrt{2}}(|0_A0_B0_C0_D\rangle + |1_A1_B1_C1_D\rangle)$  state,  $E = 7$ , and for the four-qubit Higuchi-Sudbery state found numerically by Higuchi et al. [22]:

$$
| H S \rangle = \frac {1}{\sqrt {6}} [ | 0 0 1 1 \rangle + | 1 1 0 0 \rangle + \omega (| 1 0 1 0 \rangle + | 0 1 0 1 \rangle) + \omega^ {2} (| 1 0 0 1 \rangle + | 0 1 1 0 \rangle) ],
$$

where  $\omega = e^{2\pi i / 3}$ ,  $E = 4 + 2\sqrt{3} \simeq 7.464$ , which is close to the unattainable bound of  $\simeq 7.674$ , showing that it is more entangled than the  $|GHZ\rangle_4$  state, by this measure.

Two-qutrit states Consider a two-qutrit system with levels  $|0\rangle, |1\rangle, |2\rangle$  and qutrits labeled by  $A$  and  $B$ . Let  $|\psi \rangle$  be its pure state and  $\rho$  its density matrix. Similar to the previous reasoning, for separability of qutrit A, the vectors  $\langle 0_A|\psi \rangle$ ,  $\langle 1_A|\psi \rangle$ ,  $\langle 2_A|\psi \rangle$  must be parallel. This is clear once the state is written as:  $|\psi \rangle = |0_A\rangle (\langle 0_A|\psi \rangle) + |1_A\rangle (\langle 1_A|\psi \rangle) + |2_A\rangle (\langle 2_A|\psi \rangle)$ . Therefore, define the measure of entanglement of qutrit A with qutrit B as:

$$
E _ {A} ^ {2} = 4 \left[ | | \langle 0 _ {A} | \psi \rangle \wedge \langle 1 _ {A} | \psi \rangle | | ^ {2} + | | \langle 0 _ {A} | \psi \rangle \wedge \langle 2 _ {A} | \psi \rangle | | ^ {2} + | | \langle 1 _ {A} | \psi \rangle \wedge \langle 2 _ {A} | \psi \rangle | | ^ {2} \right].
$$

Applying the Lagrange's identity gives (where  $\lambda_{i}$  are the eigenvalues of  $\rho^A$ ):

$$
E _ {A} ^ {2} = 4 \sum_ {i, j = 1, i <   j} ^ {3} \left(\rho_ {i i} ^ {A} \rho_ {j j} ^ {A} - \rho_ {i j} ^ {A} \rho_ {j i} ^ {A}\right) = 4 \sum_ {i <   j} \lambda_ {i} \lambda_ {j} = 2 \left[ 1 - \operatorname {t r} [ (\rho^ {A}) ^ {2} ] \right].
$$

One thus arrives at the result for pure multiparticle states in arbitrary dimensions (which also includes systems of mixed dimensions such as qubit-qutrit) by noting the generalizing structure from the various cases above. A global measure of entanglement for the multiparticle system may be constructed by summing over the measures for distinct bipartitions of the system.

# 5 Conclusion

We hope our work provides new insights into the deeply interesting phenomenon of entanglement, exposing its essential geometry and mathematical structure, and is of relevance to various related problems such as separability of mixed states and continuous variable systems, classification of entanglement transformations and entanglement characterization. This framework gives a faithful, computable measure of entanglement for pure states and may further be useful in generalizing concurrence for mixed and continuous variable states. The measure may also be used in numerical searches for highly entangled multiparticle states [23-25], without missing any useful state, to improve existing and discover new quantum information processing protocols [26, 27].

Acknowledgements Bhaskara is thankful to Oliver Knill for pointing out the Binet-Cauchy identity. This work was supported by the National Initiative on Undergraduate Science (NIUS) undertaken by the Homi Bhabha Centre for Science Education, Tata Institute of Fundamental Research (HBCSE-TIFR), Mumbai, India. The authors acknowledge Vijay Singh and Praveen Pathak for continuous encouragement.

# Appendix: Proof of Lagrange's identity

Consider

$$
\begin{array}{l} R H S = | | \vec {d} \wedge \vec {b} | | ^ {2} \\ = \sum_ {i = 1} ^ {m - 1} \sum_ {j = i + 1} ^ {m} \left| a _ {i} b _ {j} - a _ {j} b _ {i} \right| ^ {2} \\ = \frac {1}{2} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \left| a _ {i} b _ {j} - a _ {j} b _ {i} \right| ^ {2} \\ = \frac {1}{2} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} (a _ {i} b _ {j} - a _ {j} b _ {i}) (\bar {a} _ {i} \bar {b} _ {j} - \bar {a} _ {j} \bar {b} _ {i}) \\ = \frac {1}{2} \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \left(\left| a _ {i} \right| ^ {2} \left| b _ {j} \right| ^ {2} - 2 R e \left(a _ {i} b _ {j} \bar {a} _ {j} \bar {b} _ {i}\right) + \left| a _ {j} \right| ^ {2} \left| b _ {i} \right| ^ {2}\right) \\ \end{array}
$$

$$
\begin{array}{l} = \left(\sum_ {i = 1} ^ {m} \left| a _ {i} \right| ^ {2}\right) \left(\sum_ {j = 1} ^ {m} \left| b _ {j} \right| ^ {2}\right) - R e \sum_ {i = 1} ^ {m} \sum_ {j = 1} ^ {m} \left(a _ {i} b _ {j} \bar {a} _ {j} \bar {b} _ {i}\right) \\ = \left(\sum_ {i = 1} ^ {m} \left| a _ {i} \right| ^ {2}\right) \left(\sum_ {j = 1} ^ {m} \left| b _ {j} \right| ^ {2}\right) - \left| \sum_ {i = 1} ^ {m} a _ {i} \bar {b} _ {i} \right| ^ {2} \\ = \| \vec {a} \| ^ {2} \| \vec {b} \| ^ {2} - | \vec {a} \cdot \vec {b} | ^ {2} = L H S. \\ \end{array}
$$

Hence the identity.

# References

1. Nielsen, M.A., Chuang, I.L.: Quantum Computation and Quantum Information. Cambridge University Press, Cambridge (2002)  
2. Bouwmeester, D., Pan, J.W., Mattle, K., Eibl, M., Weinfurter, H., Zeilinger, A.: Experimental quantum teleportation. Nature 390, 575-579 (1997)  
3. Zhang, Q., Goebel, A., Wagenknecht, C., Chen, Y.A., Zhao, B., Yang, T., Mair, A., Schmiedmayer, J., Pan, J.W.: Experimental quantum teleportation of a two-qubit composite system. Nat. Phys. 2, 678-682 (2006)  
4. Vedral, V.: Quantum entanglement. Nat. Phys. 10, 256-258 (2014). (and references therein)  
5. Zhang, B., Liu, X., Wang, J., Tang, C.: Quantum teleportation of an arbitrary N-qubit state via GHZ-like states. Int. J. Theor. Phys. 55, 1601-1611 (2016)  
6. Tan, X., Zhang, X., Fang, J.: Perfect quantum teleportation by four-particle cluster state. Inf. Proc. Lett. 116(5), 347-350 (2016)  
7. Cowen, R.: The quantum source of space-time. Nature 527, 290-293 (2015)  
8. Van Raamsdonk, M.: Building up spacetime with quantum entanglement. Gen. Relativ. Gravit. 42, 2323-2329 (2010)  
9. Hill, S., Wootters, W.K.: Entanglement of a pair of quantum bits. Phys. Rev. Lett. 78, 5022 (1997)  
10. Rungta, P., Buzek, V., Caves, C.M., Hillary, M., Milburn, G.J.: Universal state inversion and concurrence in arbitrary dimensions. Phys. Rev. A 64, 042315 (2001)  
11. Sawicki, A., Huckleberry, A., Kus, M.: Symplectic geometry of entanglement. Commun. Math. Phys. 305, 441-468 (2011)  
12. Nielsen, M.A.: Conditions for a class of entanglement transformations. Phys. Rev. Lett. 83, 436 (1999)  
13. Zhu, J.M.: Quantum correlation properties in composite parity-conserved matrix product states. Int. J. Theor. Phys 55, 4157-4175 (2016)  
14. Duan, L.M., Giedke, G., Cirac, J.I., Zoller, P.: Inseparability criterion for continuous variable systems. Phys. Rev. Lett. 84, 2722 (2000)  
15. Simon, R.: Peres-Horodecki separability criterion for continuous variable systems. Phys. Rev. Lett. 84, 2726 (2000)  
16. Doran, C.J.L., Lasenby, A.N.: Geometric Algebra for Physicists. Cambridge University Press, Cambridge (2003)  
17. Ahlfors, L.V.: Complex Analysis, 3rd edn. McGraw-Hill Book Co., New York (1978)  
18. Stillwell, J.: Mathematics and Its History, 2nd edn. Springer, New York (2002)  
19. Marcus, M., Minc, H.: Introduction to Linear Algebra. Dover Publications, New York (1965)  
20. Knill, O.: Cauchy-Binet for pseudo-determinants. Linear Algebra Appl. 459, 522-547 (2014)  
21. van der Waerden, B.L.: Algebra, vol. 1. Springer, New York (2003)  
22. Higuchi, A., Sudbery, A.: How entangled can two couples get? Phys. Lett. A 273, 213-217 (2000)  
23. Enriquez, M., Wintrowicz, I., Zyczkowski, K.: Maximally entangled multipartite states. J. Phys. Conf. Ser. 698, 012003 (2016)  
24. Brown, I.D.K., Stepney, S., Sudbery, A., Braunstein, S.L.: Searching for highly entangled multi-qubit states. J. Phys. A 38, 1119 (2005)  
25. Borras, A., Plastino, A.R., Batle, J., Zander, C., Casas, M., Plastino, A.: Multiqubit systems: highly entangled states and entanglement distribution. J. Phys. A 40, 13407 (2007)

26. Muralidharan, S., Panigrahi, P.K.: Perfect teleportation, quantum-state sharing, and superdense coding through a genuinely entangled five-qubit state. Phys. Rev. A 77, 032321 (2008)  
27. Gao, C., Ma, S.Y., Chen, W.L.: Controlled remote preparation via the brown state with no restriction. Int. J. Theor. Phys. 55, 2643-2652 (2016)