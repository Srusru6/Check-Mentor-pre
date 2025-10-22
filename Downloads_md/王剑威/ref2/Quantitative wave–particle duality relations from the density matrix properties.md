# Quantitative wave-particle duality relations from the density matrix properties

Marcos L. W. Basso<sup>1</sup> · Diego S. S. Chrysosthemos<sup>1</sup> · Jonas Maziero<sup>1</sup>

Received: 10 February 2020 / Accepted: 7 July 2020 / Published online: 21 July 2020  
 $\text{©}$  Springer Science+Business Media, LLC, part of Springer Nature 2020

# Abstract

We derive upper bounds for Hilbert-Schmidt's quantum coherence of general states of a  $d$ -level quantum system, a qudit, in terms of its incoherent uncertainty, with the latter quantified using the linear and von Neumann's entropies of the corresponding closest incoherent state. Similar bounds are obtained for Wigner-Yanase's coherence. The reported inequalities are also given as coherence-populations trade-off relations. As an application example of these inequalities, we derive quantitative wave-particle duality relations for multi-slit interferometry. Our framework leads to the identification of predictability measures complementary to Hilbert-Schmidt's, Wigner-Yanase's, and  $l_{1}$ -norm quantum coherences. The quantifiers reported here for the wave and particle aspects of a quanton follow directly from the defining properties of the quantum density matrix (i.e., semi-positivity and unit trace), contrasting thus with most related results from the literature.

Keywords Wave-particle duality  $\cdot$  Quantum coherence  $\cdot$  Predictability measures

# 1 Introduction

Quantum information science (QIS) is a rapidly developing interdisciplinary field harnessing and instigating some of the most advanced results in physics, information theory, computer science, mathematics, material science, engineering, and artificial intelligence [1-11]. Nowadays we know of several aspects of quantum systems that contrast them from the classical ones. Of particular interest in QIS is to investigate how these quantum features can be harnessed to devise more efficient protocols for information processing, transmission, storage, acquisition, and protection.

A few examples of connections among quantum features and advantages in QIS protocols are as follows. Of special relevance for the whole of QIS, and in particular for the development of a quantum internet, is the use of quantum entanglement as a channel for quantum teleportation [12,13]. As for one of the most advanced branches of QIS, it is known that quantum non-locality and quantum steering are needed for device independent and semi-independent quantum communication, respectively [14, 15]. By its turn, the use of quantum squeezing and quantum discord was related to increased precision of measurements in quantum metrology [16,17]. Besides, quantum contextuality and quantum coherence (QC) were connected with the speedup of some algorithms in quantum computation [18,19].

Quantum coherence, a kind of quantum superposition [20], is directly related to the existence of incompatible observables in quantum mechanics and is somewhat connected to most of the quantumnesses mentioned above. Therefore, it is a natural research program trying to understand QC from several perspectives. Recently, researchers have been developing a resource theory framework to quantify QC, the so-called resource theory of coherence (see, e.g., Refs. [21-24] and references therein). In this resource theory, given an orthonormal reference basis  $\{|\beta_n\rangle\}_{n=1}^d$ , with  $d = \dim \mathcal{H}$  for a system with state space  $\mathcal{H}$ , the free states are incoherent mixtures of these base states:

$$
\iota = \sum_ {n = 1} ^ {d} \iota_ {n} | \beta_ {n} \rangle \langle \beta_ {n} |, \tag {1}
$$

where  $\{|t_n\rangle \}_{n = 1}^d$  is a probability distribution. A geometrical way of defining functions to quantify coherence is via the minimum distance from  $\rho$  to incoherent states:

$$
C _ {D} (\rho) = \min  _ {\iota} D (\rho , \iota) =: D \left(\rho , \iota_ {\rho} ^ {D}\right), \tag {2}
$$

where  $\iota_{\rho}^{D}$  is the closest incoherent state to  $\rho$  under the distance measure  $D$ . If  $C_D$  does not increase under incoherent operations, which are those quantum operations mapping incoherent states to incoherent states, then its dubbed a coherence monotone.

In quantum mechanics [25], the more general description of a system state is given by its density operator  $\rho = \sum_{m} p_{m} |\psi_{m}\rangle \langle \psi_{m}|$ , where  $\{p_{m}\}$  is a probability distribution and  $\{| \psi_{m} \rangle\}$  are state vectors [26]. Because of this ensemble interpretation, the density operator is required to be a positive (semi-definite) linear operator, besides having trace equal to one [27]. If we consider, for instance, two-level systems whose density operator represented in the orthonormal basis  $\{| \beta_{n} \rangle\}_{n=1}^{2}$  reads

$$
\rho = \left[ \begin{array}{l l} \langle \beta_ {1} | \rho | \beta_ {1} \rangle & \langle \beta_ {1} | \rho | \beta_ {2} \rangle \\ \langle \beta_ {2} | \rho | \beta_ {1} \rangle & \langle \beta_ {2} | \rho | \beta_ {2} \rangle \end{array} \right] =: \left[ \begin{array}{c c} \rho_ {1, 1} & \rho_ {1, 2} \\ \rho_ {1, 2} ^ {*} & 1 - \rho_ {1, 1} \end{array} \right], \tag {3}
$$

these properties impose a well-known restriction on the off-diagonal elements of  $\rho$ , its coherences, by the product of its diagonal elements, its populations:

$$
\rho_ {1, 1} (1 - \rho_ {1, 1}) \geq | \rho_ {1, 2} | ^ {2}. \tag {4}
$$

The product of the populations of  $\rho$  can be seen as the incoherent uncertainty we have about measurements of an observable with eigenvectors  $\{|\beta_n\rangle\}_{n=1}^2$ , since it is independent of the whole ensemble coherences. On the other hand, the presence of non-null off-diagonal elements of  $\rho$  implies that one or more members of the ensemble are a coherent superposition of the base states  $\{|\beta_n\rangle\}_{n=1}^2$ .

It is an interesting mathematical, physical, and possibly practical problem to derive quantum coherence-incoherent uncertainty trade-off relations regarding general-discrete quantum systems. In this article, we obtain such trade-offs for one-qudit  $(d$ -level) quantum systems. We start considering Hilbert-Schmidt's coherence (HSC) function [28] that has a convenient algebraic structure but is known not to be a coherence monotone [29]. We also regard Wigner-Yanase's coherence (WYC) [30], which is a coherence monotone. To quantify the incoherent uncertainty of a state  $\rho$ , we employ linear entropy and von Neumann's entropy of its closest incoherent state or of the diagonal of  $\sqrt{\rho}$ . It is worthwhile mentioning that the relation between "quantum" and "classical" uncertainties and other complementarity relations have been investigated in other contexts elsewhere [31-36].

Wave-particle duality has been at the center stage of conceptual discussions in quantum mechanics since its early days [37]. Recently, several authors have investigated about possible definitions of predictability and visibility quantifiers for  $d$ -slits interferometers. For a review of the literature, see, e.g., Ref. [38]. Durr's [39] and Englert et al.'s [40] criteria can be taken as a standard for checking for the reliability of newly defined predictability measures  $P(\rho)$  and interference pattern visibility quantifiers  $W(\rho)$ . For  $P$ , these required properties can be restated as follows:

P1  $P$  must be a continuous function of the diagonal elements of the density matrix.  
P2  $P$  must be invariant under permutations of the paths' indexes.  
P3 If  $\rho_{j,j} = 1$  for some  $j$ , then  $P$  must reach its maximum value.  
P4 If  $\{\rho_{j,j} = 1 / d\}_{j = 1}^{d}$ , then  $P$  must reach its minimum value.  
P5 If  $\rho_{j,j} > \rho_{k,k}$  for some  $(j,k)$ , the value of  $P$  cannot be increased by setting  $\rho_{j,j} \to \rho_{j,j} - \epsilon$  and  $\rho_{k,k} \to \rho_{k,k} + \epsilon$ , for  $\epsilon \in \mathbb{R}_+$  and  $\epsilon \ll 1$ .  
P6  $P$  must be a convex function, i.e.,  $P(\omega \xi + (1 - \omega)\eta) \leq \omega P(\xi) + (1 - \omega)P(\eta)$ , for  $0 \leq \omega \leq 1$  and for  $\xi$  and  $\eta$  being valid density matrices.

One can also write down a list of required properties for the functions to be used to quantify the wave aspect  $W$  of a quanton in a  $d$ -slit interferometer [39,40]:

W1  $W$  must be a continuous function of the elements of the density matrix.  
W2  $W$  must be invariant under permutations of the paths' indexes.  
W3 If  $\rho_{j,j} = 1$  for some  $j$ , then  $W$  must reach its minimum value.  
W4 If  $\rho$  is a pure state and  $\{\rho_{j,j} = 1 / d\}_{j = 1}^{d}$ , then  $W$  must reach its maximum value.  
W5  $W$  cannot be increased when decreasing  $|\rho_{j,k}|$  by an infinitesimal amount, for  $j \neq k$ .  
W6  $W$  must be a convex function, i.e.,  $W(\omega \xi + (1 - \omega)\eta) \leq \omega W(\xi) + (1 - \omega)W(\eta)$ , for  $0 \leq \omega \leq 1$  and  $\xi$  and  $\eta$  are well-defined density matrices.

There are convincing arguments indicating quantum coherence as a good measure for the wave aspect of a quanton [41]. And we will show that our coherence-incoherent uncertainty trade-off relations can be applied to obtain quantitative wave-particle

duality relations, with the associated predictability and visibility measures satisfying the criteria listed above. The framework devised in this article shows that the semipositivity and unit trace of the quantum density matrix leads to the identification of predictability measures complementary to HSC, to WYC, and to  $l_{1}$ -norm quantum coherence (L1C).

We organized the remainder of this article in the following manner. In Sect. 2, we present the Gell-Mann matrix basis (GMB), defined using any vector basis of  $\mathbb{C}^d$ , and discuss the representation of general and diagonal matrices in the GMB. We obtain trade-off relations between quantum coherence and incoherent uncertainty measuring the first with Hilbert-Schmidt coherence in Sect. 3.1. We obtain analogous relations using Wigner-Yanase's coherence in Sect. 3.2. We show how to write these inequalities as coherence-populations trade-off relations in Sect. 4. In Sect. 5.1, we report quantitative visibility-predictability duality relations identified directly from our coherence-incoherent uncertainty inequalities. In Sects. 5.2 and 5.3, we apply the positivity and unit trace of the density matrix to identify predictability measures complementary to WYC and L1C, respectively. We give our conclusions in Sect. 6.

# 2 Gell-Mann basis for  $\mathbb{C}^{dxd}$

Let  $\{| \beta_{m} \rangle \}_{m=1}^{d}$  be any given vector basis for  $\mathbb{C}^d$ . Using this basis, we can define the generalized Gell-Mann's matrices as [42]:

$$
\Gamma_ {j} ^ {d} := \sqrt {\frac {2}{j (j + 1)}} \sum_ {m = 1} ^ {j + 1} (- j) ^ {\delta_ {m, j + 1}} | \beta_ {m} \rangle \langle \beta_ {m} |, \tag {5}
$$

$$
\Gamma_ {k, l} ^ {s} := \left| \beta_ {k} \right\rangle \left\langle \beta_ {l} \right| + \left| \beta_ {l} \right\rangle \left\langle \beta_ {k} \right|, \tag {6}
$$

$$
\Gamma_ {k, l} ^ {a} := - i \left(\left| \beta_ {k} \right\rangle \left\langle \beta_ {l} \right| - \left| \beta_ {l} \right\rangle \left\langle \beta_ {k} \right|\right), \tag {7}
$$

where, if not stated otherwise, we use the following possible values for the indexes  $j, k, l$  up to Sect. 4 of this article:

$$
j = 1, \dots , d - 1 \text {a n d} 1 \leq k <   l \leq d. \tag {8}
$$

One can easily see that these matrices are Hermitian and traceless. Besides, if we use  $\Gamma_0^d$  for the  $d\times d$  identity matrix, it is not difficult to verify that under the Hilbert-Schmidt's inner product,

$$
\langle A | B \rangle_ {\mathrm {h s}} := \operatorname {T r} \left(A ^ {\dagger} B\right), \tag {9}
$$

with  $A, B \in \mathbb{C}^{d \times d}$ , the set

$$
\left\{\frac {\Gamma_ {0} ^ {d}}{\sqrt {d}}, \frac {\Gamma_ {j} ^ {d}}{\sqrt {2}}, \frac {\Gamma_ {k , l} ^ {\tau}}{\sqrt {2}} \right\}, \tag {10}
$$

with  $\tau = s, a$ , forms an orthonormal basis for  $\mathbb{C}^{d\times d}$  [42]. So, any matrix  $X\in \mathbb{C}^{d\times d}$  can be decomposed in this basis, called hereafter of Gell-Mann's basis (GMB), as follows:

$$
X = \frac {\operatorname {T r} (X)}{d} \Gamma_ {0} ^ {d} + \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} | X \right\rangle \Gamma_ {j} ^ {d} + \frac {1}{2} \sum_ {k, l, \tau} \left\langle \Gamma_ {k, l} ^ {\tau} | X \right\rangle \Gamma_ {k, l} ^ {\tau}. \tag {11}
$$

We observe that the most general decomposition in GMB of a matrix  $X_{d}\in \mathbb{C}^{d\times d}$  which is diagonal in the basis  $\{| \beta_m\rangle \}_{m = 1}^d$  shall be given by:

$$
X _ {d} = \frac {\operatorname {T r} \left(X _ {d}\right)}{d} \Gamma_ {0} ^ {d} + \frac {1}{2} \sum_ {j} \langle \Gamma_ {j} ^ {d} | X _ {d} \rangle \Gamma_ {j} ^ {d}, \tag {12}
$$

i.e., only the diagonal elements of the GMB can have non-null components in this decomposition.

# 3 Trade-off relations between quantum coherence and incoherent uncertainty

# 3.1 Upper bound for Hilbert-Schmidt's coherence

The Hilbert-Schmidt's coherence (HSC) of a quantum state  $\rho$  is defined as [28]

$$
C _ {\mathrm {h s}} (\rho) := \min  _ {\iota} | | \rho - \iota | | _ {\mathrm {h s}} ^ {2}, \tag {13}
$$

with the Hilbert-Schmidt's norm of a matrix  $A \in \mathbb{C}^{d \times d}$  being defined as

$$
\left| \left| A \right| \right| _ {\mathrm {h s}} := \sqrt {\langle A | A \rangle_ {\mathrm {h s}}}, \tag {14}
$$

and here the minimization is taken over the incoherent states of Eq. (1). For general one-qudit states, using the decompositions in GMB:

$$
\rho = \frac {1}{d} \Gamma_ {0} ^ {d} + \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} \right| \rho \rangle \Gamma_ {j} ^ {d} + \frac {1}{2} \sum_ {k, l, \tau} \left\langle \Gamma_ {k, l} ^ {\tau} \right| \rho \rangle \Gamma_ {k, l} ^ {\tau}, \tag {15}
$$

$$
\iota = \frac {1}{d} \Gamma_ {0} ^ {d} + \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} \right| \iota \rangle \Gamma_ {j} ^ {d}, \tag {16}
$$

the analytical formulas for the HSC and for the associated closest incoherent state were obtained in Ref. [28] and read, respectively:

$$
C _ {\mathrm {h s}} (\rho) = \frac {1}{2} \sum_ {k, l, \tau} \left\langle \Gamma_ {k, l} ^ {\tau} \right| \rho \rangle^ {2}, \tag {17}
$$

$$
\iota_ {\rho} ^ {\mathrm {h s}} = \frac {1}{d} \Gamma_ {0} ^ {d} + \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} \right| \rho \rangle \Gamma_ {j} ^ {d}. \tag {18}
$$

The main tool we use to obtain some of the results reported in this article is a condition for matrix positivity. The eigenvalues of a matrix  $A \in \mathbb{C}^{d \times d}$ , let us call them  $a$ , can be obtained from [43]:

$$
\begin{array}{l} 0 = \det  (A - a \Gamma_ {0} ^ {d}) (19) \\ = \sum_ {\left(j _ {1}, j _ {2}, \dots , j _ {d}\right)} \operatorname {s g n} _ {d} \left(j _ {1}, j _ {2}, \dots , j _ {d}\right) \left(A _ {1, j _ {1}} - a \delta_ {1, j _ {1}}\right) \left(A _ {2, j _ {2}} - a \delta_ {2, j _ {2}}\right) \dots \left(A _ {d, j _ {d}} - a \delta_ {d, j _ {d}}\right) (20) \\ = (- 1) ^ {d} c _ {d} a ^ {d} + (- 1) ^ {d - 1} c _ {d - 1} a ^ {d - 1} + (- 1) ^ {d - 2} c _ {d - 2} a ^ {d - 2} + \dots + c _ {2} a ^ {2} - c _ {1} a + c _ {0}. (21) \\ \end{array}
$$

By Descartes rule of signs (see, e.g., Ref. [44] and references therein), we see that for  $A$  to be a positive matrix, we have to have nonnegativity for all the coefficients  $\{c_m \geq 0\}_{m=0}^d$ . In this article, we shall look at the positivity of:

$$
\begin{array}{l} c _ {d - 2} = \sum_ {(j _ {1}, j _ {2})} \operatorname {s g n} _ {d} (j _ {1}, j _ {2}, 3 \dots , d) A _ {1, j _ {1}} A _ {2, j _ {2}} \\ + \dots + \sum_ {(j _ {1}, j _ {d})} \operatorname {s g n} _ {d} (j _ {1}, 2, \dots , d - 1, j _ {d}) A _ {1, j _ {1}} A _ {d, j _ {d}} \\ + \sum_ {(j _ {2}, j _ {3})} \operatorname {s g n} _ {d} (1, j _ {2}, j _ {3}, 4, \dots , d) A _ {2, j _ {2}} A _ {3, j _ {3}} \\ + \dots + \sum_ {(j _ {2}, j _ {d})} \operatorname {s g n} _ {d} (1, j _ {2}, 3, \dots , d - 1, j _ {d}) A _ {2, j _ {2}} A _ {d, j _ {d}} \\ + \dots + \sum_ {\left(j _ {d - 1}, j _ {d}\right)} \operatorname {s g n} _ {d} (1, 2, \dots d - 2, j _ {d - 1}, j _ {d}) A _ {d - 1, j _ {d - 1}} A _ {d, j _ {d}} (22) \\ = \sum_ {m = 1} ^ {d - 1} \sum_ {n = m + 1} ^ {d} \left(A _ {m, m} A _ {n, n} - A _ {m, n} A _ {n, m}\right) (23) \\ = \frac {1}{2} \left(\left(\operatorname {T r} (A)\right) ^ {2} - \operatorname {T r} \left(A ^ {2}\right)\right) \geq 0. (24) \\ \end{array}
$$

Using the orthonormality of GMB, i.e., the inner product between different elements of the GMB is zero and  $\langle \Gamma_0^d |\Gamma_0^d\rangle = d$  and  $\langle \Gamma_j^d |\Gamma_j^d\rangle = \langle \Gamma_{k,l}^\tau |\Gamma_{k,l}^\tau \rangle = 2$ , the positivity condition for the coefficient in Eq. (24) applied to the density matrix of Eq. (15), as  $\mathrm{Tr}(\rho) = 1$ , can be rewritten as

$$
\begin{array}{l} 0 \leq 1 - \operatorname {T r} \left(\rho^ {2}\right) (25) \\ = 1 - \frac {1}{d} - \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} | \rho \right\rangle^ {2} - \frac {1}{2} \sum_ {k, l, \tau} \left\langle \Gamma_ {k, l} ^ {\tau} | \rho \right\rangle^ {2}. (26) \\ \end{array}
$$

Now, if we use the formula for the HSC in Eq. (17), this inequality can be cast as a restriction to the HSC:

$$
C _ {\mathrm {h s}} (\rho) \leq \frac {d - 1}{d} - \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} | \rho \right\rangle^ {2}. \tag {27}
$$

If we utilize again the orthonormality of the GMB, the right hand side of this inequality is easily seen to be the incoherent uncertainty of the state  $\rho$  measured using the linear entropy of its closest incoherent state [Eq. (18)], i.e.,

$$
S _ {l} \left(\iota_ {\rho} ^ {\mathrm {h s}}\right) = 1 - \operatorname {T r} \left(\left(\iota_ {\rho} ^ {\mathrm {h s}}\right) ^ {2}\right) = \frac {d - 1}{d} - \frac {1}{2} \sum_ {j} \langle \Gamma_ {j} ^ {d} | \rho \rangle^ {2}. \tag {28}
$$

Now, using  $-\ln x \geq 1 - x$  [45], we can get an upper bound for the linear entropy in terms of von Neumann's entropy as follows:

$$
\begin{array}{l} S _ {\mathrm {v n}} (x) := \operatorname {T r} (x (- \ln x)) (29) \\ \geq \operatorname {T r} (x (1 - x)) = \operatorname {T r} (x) - \operatorname {T r} \left(x ^ {2}\right) = S _ {l} (x) + \operatorname {T r} (x) - 1. (30) \\ \end{array}
$$

Gathering the results above, as  $\mathrm{Tr}(t_{\rho}^{\mathrm{hs}}) = 1$ , we have obtained the following quantum coherence-incoherent uncertainty trade-off relations:

$$
C _ {\mathrm {h s}} (\rho) \leq S _ {l} \left(\iota_ {\rho} ^ {\mathrm {h s}}\right) \leq S _ {\mathrm {v n}} \left(\iota_ {\rho} ^ {\mathrm {h s}}\right), \tag {31}
$$

which are valid for any one-qudit state. The "verification" of these entropic inequalities using random states is presented in Fig. 1. We observe that the upper bound given by linear entropy is tight for qubits  $(d = 2)$ . However, as the dimension increases, and typicality is approached [46], the upper bounds get less and less tight.

# 3.2 Upper bound for Wigner-Yanase's coherence

In this subsection, we shall deal with Wigner-Yanase's coherence (WYC) [30]:

$$
\begin{array}{l} C _ {\mathrm {w y}} (\rho) := \sum_ {j = 1} ^ {d} I _ {\mathrm {w y}} (\rho , | \beta_ {j} \rangle \langle \beta_ {j} |) := - \frac {1}{2} \sum_ {j = 1} ^ {d} \operatorname {T r} \left(\left[ \sqrt {\rho}, | \beta_ {j} \rangle \langle \beta_ {j} | \right]\right) ^ {2}) (32) \\ = \frac {1}{2} \sum_ {j = 1} ^ {d} \left(\left\langle \beta_ {j} \right| \rho \left| \beta_ {j} \right\rangle + \sum_ {k = 1} ^ {d} \left| \left\langle \beta_ {j} \right| \sqrt {\rho} \left| \beta_ {k} \right\rangle \right| ^ {2} - 2 \left\langle \beta_ {j} \right| \sqrt {\rho} \left| \beta_ {j} \right\rangle^ {2}\right), (33) \\ \end{array}
$$

with  $[\cdot, \cdot]$  being the commutator. Identifying the following relation between a diagonal element of  $\rho$  and the elements in the corresponding row of  $\sqrt{\rho}$ :

$$
\langle \beta_ {j} | \rho | \beta_ {j} \rangle = \sum_ {k = 1} ^ {d} \langle \beta_ {j} | \sqrt {\rho} | \beta_ {k} \rangle \langle \beta_ {k} | \sqrt {\rho} | \beta_ {j} \rangle = \sum_ {k = 1} ^ {d} | \langle \beta_ {j} | \sqrt {\rho} | \beta_ {k} \rangle | ^ {2}, \tag {34}
$$

![](images/0c6363de79e8cbfe1d66737b78254df7241c0913e3e46f67d25d551ba4626382.jpg)

![](images/48623f938d862ca0df9485a5f4f5f970d671551d03d007cde0cb1b994a8805b6.jpg)

![](images/aa3ba99b253c9f8079e1fdc025efb6513bd30461899b0dd2212f5c6cd7dc4dba.jpg)  
Fig. 1 (Color online) "Verification" of the Hilbert-Schmidt quantum coherence-incoherent uncertainty trade-off relations of Eq. (31) for one thousand random density matrices generated for each value of the system dimension  $d$ . The random states were created using the standard method described in Refs. [47,48]. The  $y$  axis is for  $C_{\mathrm{hs}}(\rho)$  and the  $x$  axis is for  $S_l(\iota_\rho^{\mathrm{hs}})$  or  $S_{\mathrm{vn}}(\iota_\rho^{\mathrm{hs}})$ , with  $\iota_\rho^{\mathrm{hs}}$  given in Eq. (18). The black lines stand for  $C_{\mathrm{hs}}(\rho) = S_l(\iota_\rho^{\mathrm{hs}})$  and for  $C_{\mathrm{hs}}(\rho) = S_{\mathrm{vn}}(\iota_\rho^{\mathrm{hs}})$ .

![](images/f9d36dec616649b6d2c76c5a74b4d2e586222e2102831e9fdb6009687a375922.jpg)

we can write

$$
\begin{array}{l} C _ {\mathrm {w y}} (\rho) = \sum_ {j = 1} ^ {d} \sum_ {k = 1} ^ {d} | \langle \beta_ {j} | \sqrt {\rho} | \beta_ {k} \rangle | ^ {2} - \sum_ {j = 1} ^ {d} \langle \beta_ {j} | \sqrt {\rho} | \beta_ {j} \rangle^ {2} (35) \\ = \sum_ {j \neq k} | \langle \beta_ {j} | \sqrt {\rho} | \beta_ {k} \rangle | ^ {2}. (36) \\ \end{array}
$$

Now, by using  $\langle \Gamma_{k,l}^s |\sqrt{\rho}\rangle = 2\mathrm{Re}((\sqrt{\rho})_{k,l})$  and  $\langle \Gamma_{k,l}^{a}|\sqrt{\rho}\rangle = -2\mathrm{Im}((\sqrt{\rho})_{k,l})$ , where  $\mathrm{Re}((\sqrt{\rho})_{k,l})$  and  $\mathrm{Im}((\sqrt{\rho})_{k,l})$  are the real and imaginary parts of  $(\sqrt{\rho})_{k,l}$ , respectively, we get

$$
C _ {\mathrm {w y}} (\rho) = \frac {1}{2} \sum_ {k, l, \tau} \left\langle \Gamma_ {k, l} ^ {\tau} \right| \sqrt {\rho} \rangle^ {2}. \tag {37}
$$

A quantum state, with spectral decomposition  $\rho = \sum_{m=1}^{d} r_m |r_m\rangle \langle r_m|$ , is a positive matrix [45], i.e.,  $\{r_m \geq 0\}_{m=1}^d$ . So,  $\sqrt{\rho} = \sum_{m=1}^{d} \sqrt{r_m} |r_m\rangle \langle r_m|$  is also a positive matrix. If we apply the positivity condition of Eq. (24) to  $\sqrt{\rho}$  decomposed in GMB as

$$
\sqrt {\rho} = \frac {\operatorname {T r} (\sqrt {\rho})}{d} \Gamma_ {0} ^ {d} + \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} \right| \sqrt {\rho} \rangle \Gamma_ {j} + \frac {1}{2} \sum_ {k, l, \tau} \left\langle \Gamma_ {k, l} ^ {\tau} \right| \sqrt {\rho} \rangle \Gamma_ {k, l} ^ {\tau}, \tag {38}
$$

the following inequality is obtained:

$$
\begin{array}{l} 0 \leq (\operatorname {T r} (\sqrt {\rho})) ^ {2} - \operatorname {T r} ((\sqrt {\rho}) ^ {2}) (39) \\ = \left(\operatorname {T r} (\sqrt {\rho})\right) ^ {2} \left(1 - \frac {1}{d}\right) - \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} \mid \sqrt {\rho} \right\rangle^ {2} - \frac {1}{2} \sum_ {k, l, \tau} \left\langle \Gamma_ {k, l} ^ {\tau} \mid \sqrt {\rho} \right\rangle^ {2}. (40) \\ \end{array}
$$

Using WYC in Eq. (37) and the linear and von Neumann's entropies of

$$
\sqrt {\rho} _ {\text {d i a g}} := \frac {\operatorname {T r} (\sqrt {\rho})}{d} \Gamma_ {0} ^ {d} + \frac {1}{2} \sum_ {j} \left\langle \Gamma_ {j} ^ {d} \right| \sqrt {\rho} \rangle \Gamma_ {j}, \tag {41}
$$

we obtain the following upper bounds for WYC:

$$
\begin{array}{l} C _ {\mathrm {w y}} (\rho) \leq \left(S _ {l} \left(\sqrt {\rho} _ {\text {d i a g}}\right) + \left(\operatorname {T r} \left(\sqrt {\rho} _ {\text {d i a g}}\right)\right) ^ {2} - 1 =: \Upsilon\right) (42) \\ \leq \left(S _ {\mathrm {v n}} \left(\sqrt {\rho} _ {\mathrm {d i a g}}\right) + \operatorname {T r} \left(\sqrt {\rho} _ {\mathrm {d i a g}}\right) \left(\operatorname {T r} \left(\sqrt {\rho} _ {\mathrm {d i a g}}\right) - 1\right) =: \Omega\right). (43) \\ \end{array}
$$

In the particular case of pure states,  $\rho = |\psi \rangle \langle \psi|$ $\therefore \sqrt{\rho} = \rho$ , we have  $C_{\mathrm{wy}}(\rho) = C_{\mathrm{hs}}(\rho)$ . Hence, in this case, the inequalities above are equivalent to the ones obtained for Hilbert-Schmidt's coherence in Eq. (31), i.e.,

$$
C _ {\mathrm {w y}} (| \psi \rangle \langle \psi |) \leq S _ {l} \left(\iota_ {\rho} ^ {\mathrm {h s}}\right) \leq S _ {\mathrm {v n}} \left(\iota_ {\rho} ^ {\mathrm {h s}}\right). \tag {44}
$$

The upper bounds for WYC were also "verified" using random states, as shown in Fig. 2. Here, the restrictiveness of those upper bounds is also seen to diminish with the increase of the system dimension.

# 4 Coherence-populations trade-off relations

In this section, we start rewriting the upper bound for Hilbert-Schmidt's coherence given in Eq. (27) by expressing the components of the so-called Bloch's vector corresponding to the diagonal elements of Gell-Mann's basis,  $\langle \Gamma_j^d |\rho \rangle$  with  $j = 1,\ldots ,d - 1$ , in terms of the density matrix populations,  $\rho_{m,m} = \langle \beta_m|\rho |\beta_m\rangle$  with  $m = 1,\dots ,d$ . For that purpose, after some algebraic manipulations, one can infer that for  $m = 2,\ldots ,d - 1$ :

$$
\rho_ {m, m} = \frac {1}{d} - \sqrt {\frac {m - 1}{2 m}} \left\langle \Gamma_ {m - 1} ^ {d} \right| \rho \rangle + \sum_ {j = 1} ^ {d - 1} \frac {\left\langle \Gamma_ {j} ^ {d} \right| \rho \rangle}{\sqrt {2 j (j + 1)}} \sum_ {n = m} ^ {d - 1} \delta_ {n, j}. \tag {45}
$$

![](images/97aef784daf61fc75bbf56511722fdf37ed22fd3d825a712be6f61cb44e4fc3d.jpg)

![](images/a7969de37bec8d41cc8dd8f5d2c4579b6e12d2186bc99cc1dd4e858d122e0158.jpg)

![](images/ffa82c809def896f611c2543b9efbc0d8410b6bd3075f396f840b3f3f9647e2f.jpg)  
Fig. 2 (Color online) "Verification" of the upper bounds for Wigner-Yanase quantum coherence in Eqs. (42) and (43) for five thousand random density matrices generated for each value of the system dimension  $d$ . The method used to create the random states is the same as the one mentioned in Fig. 1. The black lines stand for  $C_{\mathrm{wy}}(\rho) = \Upsilon$  and for  $C_{\mathrm{wy}}(\rho) = \Omega$

![](images/f5517770947da058f1b497efa03253dd1f9b402b4fc5b39ab1652b3f1174b20d.jpg)

For  $m = d$  and  $m = 1$ , we can use this same expression for the populations, but without the last and second terms, respectively. By inverting the expressions in Eq. (45) iteratively, we obtain the general expression we need to rewrite the trade-offs in Eq. (31) in terms of  $\rho$ 's populations:

$$
\langle \Gamma_ {d - j} ^ {d} | \rho \rangle = \sqrt {\frac {2}{(d - j + 1) (d - j)}} \left(1 - \sum_ {n = 1} ^ {j} (d - n + 1) ^ {\delta_ {j, n}} \rho_ {d - n + 1, d - n + 1}\right). \tag {46}
$$

As examples, let us start considering qubit and qutrit systems. For  $d = 2$ ,  $\langle \Gamma_1^d |\rho \rangle = 1 - 2\rho_{2,2}$  and, from Eq. (27), we get  $C_{\mathrm{hs}}(\rho) = 2|\rho_{1,2}|^2 \leq 2\rho_{1,1}\rho_{2,2}$ , which is equivalent to Eq. (4). For  $d = 3$ ,  $\langle \Gamma_1^d |\rho \rangle = 1 - \rho_{3,3} - 2\rho_{2,2}$ ,  $\langle \Gamma_2^d |\rho \rangle = (1 - 3\rho_{3,3}) / \sqrt{3}$  and

$$
C _ {\mathrm {h s}} (\rho) \leq 2 \left(\rho_ {1, 1} \rho_ {2, 2} + \rho_ {1, 1} \rho_ {3, 3} + \rho_ {2, 2} \rho_ {3, 3}\right). \tag {47}
$$

As this same pattern appears also for  $d = 4$  and for  $d = 5$ , one would conjecture that for any one-qudit state the following inequality will be satisfied:

$$
C _ {\mathrm {h s}} (\rho) \leq 2 \sum_ {m = 1} ^ {d - 1} \sum_ {n = m + 1} ^ {d} \rho_ {m, m} \rho_ {n, n}. \tag {48}
$$

We could not give limitations for the Wigner-Yanase's coherence of a state  $\rho$  directly in terms of the density matrix populations. Notwithstanding, relations identical to the ones above shall follow for this quantum coherence measure if we replace  $\rho$  by  $\sqrt{\rho}$  in Eqs. (45) and (46) and on the right hand side of Eq. (48), i.e.,

$$
C _ {\mathrm {w y}} (\rho) \leq 2 \sum_ {m = 1} ^ {d - 1} \sum_ {n = m + 1} ^ {d} (\sqrt {\rho}) _ {m, m} (\sqrt {\rho}) _ {n, n}. \tag {49}
$$

A simpler and general proof of this kind of inequality can be given as follows. It is known from matrix analysis [49] that all principal sub-matrices of a positive semi-definite matrix are also positive semi-definite. In particular,  $A \geq \mathbb{O} \Rightarrow \begin{bmatrix} A_{j,j} & A_{j,k} \\ A_{k,j} & A_{k,k} \end{bmatrix} \geq \mathbb{O} \forall j, k$ . It follows then that

$$
\sum_ {j \neq k} | A _ {j, k} | ^ {2} = \sum_ {j, k} | A _ {j, k} | ^ {2} - \sum_ {j} A _ {j, j} ^ {2} \leq \sum_ {j, k} A _ {j, j} A _ {k, k} - \sum_ {j} A _ {j, j} ^ {2} = \sum_ {j \neq k} A _ {j, j} A _ {k, k}, \tag {50}
$$

from which we can obtain the inequalities in Eqs. (48) and (49).

In the next section, we will use one of these two expressions for giving closed formulas for measures of path information and interference pattern visibility.

# 5 Quantitative complementarity relations for  $d$ -slits interferometers

# 5.1 Complementarity relations with Hilbert-Schmidt's coherence

Here, we use HSC written in terms of the density matrix elements:

$$
\begin{array}{l} C _ {\mathrm {h s}} (\rho) := \min  _ {\iota} | | \rho - \iota | | _ {\mathrm {h s}} ^ {2} = \min  _ {\iota} \sum_ {j, k = 1} ^ {d} | (\rho - \iota) _ {j, k} | ^ {2} = \min  _ {\iota} \sum_ {j, k = 1} ^ {d} | \rho_ {j, k} - \iota_ {j} \delta_ {j, k} | ^ {2} (51) \\ = \sum_ {j \neq k} \left| \rho_ {j, k} \right| ^ {2}. (52) \\ \end{array}
$$

In the sequence, we show that  $W \coloneqq C_{\mathrm{hs}}$  satisfies the properties listed in the introduction. One can easily see from the expression for  $C_{\mathrm{hs}}$  that it has the properties  $W1$  and  $W2$ , i.e.,  $C_{\mathrm{hs}}$  is continuous and invariant under paths' indexes exchanges. Besides:

W3 If  $\rho_{j,j} = 1$  for any  $j$ , then all the other populations and all the coherences are null (by the restrictions  $|\rho_{j,k}|^2 \leq \rho_{j,j}\rho_{k,k} \forall j, k$ ). Therefore,  $C_{\mathrm{hs}} = 0$ , which is the required minimum, since we have  $C_{\mathrm{hs}} \geq 0$ .

W4 If  $\rho_{j,j} = 1 / d\forall j$  , we shall have from  $\begin{bmatrix} \rho_{j,j}\rho_{j,k}\\ \rho_{k,j}\rho_{k,k} \end{bmatrix} \geq \mathbb{O}$  that  $|\rho_{j,k}|\leq 1 / d\forall j\neq k.$  So, for the maximum value for the density matrix coherences  $\rho_{j,k} = 1 / d\forall j\neq k,$  we see that  $Tr(\rho^2) = 1$  and that  $C_\mathrm{hs}$  reaches its maximum value,  $(d - 1) / d$

W5 If we set  $\rho_{j,k} \rightarrow \tilde{\rho}_{j,k} = \rho_{j,k} - \epsilon$ , with  $\mathrm{Re}(\rho_{j,k})\mathrm{Re}(\epsilon) \geq 0$  and  $\mathrm{Im}(\rho_{j,k})\mathrm{Im}(\epsilon) \geq 0$ , then  $|\tilde{\rho}_{j,k}|^2 \approx |\rho_{j,k}|^2 - 2(\mathrm{Re}(\rho_{j,k})\mathrm{Re}(\epsilon) + \mathrm{Im}(\rho_{j,k})\mathrm{Im}(\epsilon)) \leq |\rho_{j,k}|^2$ , which implies that  $\tilde{C}_{\mathrm{hs}} \leq C_{\mathrm{hs}}$ .

W6 For  $0 \leq \omega \leq 1$  and  $\xi$  and  $\eta$  valid density operators, we verify that  $C_{\mathrm{hs}}$  is convex as follows:

$$
\begin{array}{l} C _ {\mathrm {h s}} (\omega \xi + (1 - \omega) \eta) - \omega C _ {\mathrm {h s}} (\xi) - (1 - \omega) C _ {\mathrm {h s}} (\eta) \\ = \sum_ {j \neq k} | (\omega \xi + (1 - \omega) \eta) _ {j, k} | ^ {2} - \omega \sum_ {j \neq k} | \xi_ {j, k} | ^ {2} - (1 - \omega) \sum_ {j \neq k} | \eta_ {j, k} | ^ {2} (53) \\ = \sum_ {j \neq k} \omega (\omega - 1) \left(\left(\operatorname {R e} \left(\xi_ {j, k}\right) - \operatorname {R e} \left(\eta_ {j, k}\right)\right) ^ {2} + \left(\operatorname {I m} \left(\xi_ {j, k}\right) - \operatorname {I m} \left(\eta_ {j, k}\right)\right) ^ {2}\right) (54) \\ \leq 0. (55) \\ \end{array}
$$

Let us define

$$
S _ {\tau} ^ {\max } := \max  _ {\rho} S _ {\tau} (\rho), \text {w i t h} \tau = l, v n. \tag {56}
$$

For  $d$ -dimensional density matrices,  $\rho = \mathbb{I}_d / d$  gives the maximum for the entropies:

$$
S _ {l} ^ {\max } = (d - 1) / d \text {a n d} S _ {\mathrm {v n}} ^ {\max } = \ln d. \tag {57}
$$

Now, we can rewrite the inequalities in Eqs. (31) as

$$
C _ {\mathrm {h s}} (\rho) + S _ {\tau} ^ {\max } - S _ {\tau} \left(t _ {\rho} ^ {\tau}\right) \leq S _ {\tau} ^ {\max }. \tag {58}
$$

By defining the Hilbert-Schmidt's predictability measures

$$
P _ {\mathrm {h s}} ^ {l} (\rho) := S _ {l} ^ {\max } - S _ {l} \left(t _ {\rho} ^ {\mathrm {h s}}\right) = \frac {d - 1}{d} - 2 \sum_ {m = 1} ^ {d - 1} \sum_ {n = m + 1} ^ {d} \rho_ {m, m} \rho_ {n, n}, \tag {59}
$$

$$
P _ {\mathrm {h s}} ^ {\mathrm {v n}} (\rho) := S _ {\mathrm {v n}} ^ {\max } - S _ {\mathrm {v n}} \left(u _ {\rho} ^ {\mathrm {h s}}\right) = \ln d + \sum_ {j = 1} ^ {d} \rho_ {n, n} \ln \rho_ {n, n}, \tag {60}
$$

we obtain the coherence-predictability complementarity relations:

$$
C _ {\mathrm {h s}} (\rho) + P _ {\mathrm {h s}} ^ {\tau} (\rho) \leq S _ {\tau} ^ {\max } \tag {61}
$$

One could put the upper bounds for these inequalities in the usual form, equal to one, by normalizing  $C_{\mathrm{hs}}$  and  $P_{\mathrm{hs}}^{\tau}$ .

In the sequence, we shall verify that the predictability measures introduced here satisfy the criteria listed in Sect. 1:

P1 As  $S_{\tau}(l_{\rho}^{\mathrm{hs}})$  is a continuous function of  $\{\rho_{j,j}\}_{j = 1}^{d}$ , so is  $P_{\mathrm{hs}}^{\tau}(\rho)$ .  
P2 It is straightforward to see in the right hand side of Eqs. (59) and (60) that  $P_{\mathrm{hs}}^{l}$  and  $P_{\mathrm{hs}}^{l}$  are invariant under exchange of paths' labels.  
P3 If  $\rho_{j,j} = 1$  for some  $j$ , then  $\rho_{k,k} = 0 \forall k \neq j$  and  $S_l = 1 - \rho_{j,j}^2 - \sum_{k \neq j} \rho_{k,k}^2 = 0$  and  $S_{\mathrm{vn}} = -\rho_{j,j} \ln \rho_{j,j} - \sum_{k \neq j} \rho_{k,k} \ln \rho_{k,k} = 0$ . So  $P_{\mathrm{hs}}^{\tau} := S_{\tau}^{\max}$ .  
P4 If  $\{\rho_{j,j} = 1 / d\}_{j = 1}^{d}$ , then  $S_{l} = 1 - \sum_{j = 1}^{d}(1 / d^{2}) = S_{l}^{\max}$  and  $S_{\mathrm{vn}} = -\sum_{j = 1}^{d}(1 / d)\ln (1 / d) = S_{\mathrm{vn}}^{\max}$ . So  $P_{\mathrm{hs}}^{\tau} = 0$ .  
P5 Once  $P_{\mathrm{hs}}^{\tau}$  is invariant under exchange  $\rho_{j,j} \leftrightarrow \rho_{k,k} \forall j, k$  we can, without loss of generality, consider  $\rho_{1,1} > \rho_{2,2}, \rho_{1,1} \rightarrow \rho_{1,1} - \epsilon$ , and  $\rho_{2,2} \rightarrow \rho_{2,2} + \epsilon$  for  $\epsilon > 0$  and  $\epsilon \ll 1$ . Thus,

$$
\begin{array}{l} \tilde {P} _ {\mathrm {h s}} ^ {l} = S _ {l} ^ {\max } - 1 + \left(\rho_ {1, 1} - \epsilon\right) ^ {2} + \left(\rho_ {2, 2} + \epsilon\right) ^ {2} + \sum_ {j = 3} ^ {d} \rho_ {j, j} ^ {2} (62) \\ = S _ {l} ^ {\max } - \left(1 - \sum_ {j = 1} ^ {d} \rho_ {j, j} ^ {2}\right) - 2 \epsilon \left(\rho_ {1, 1} - \rho_ {2, 2}\right) + \mathcal {O} \left(\epsilon^ {2}\right) (63) \\ \leq P _ {\mathrm {h s}} ^ {l} (64) \\ \end{array}
$$

and

$$
\begin{array}{l} \tilde {P} _ {\mathrm {h s}} ^ {\mathrm {v n}} = S _ {\mathrm {v n}} ^ {\max } + (\rho_ {1, 1} - \epsilon) \ln (\rho_ {1, 1} - \epsilon) + (\rho_ {2, 2} + \epsilon) \ln (\rho_ {2, 2} + \epsilon) + \sum_ {j = 3} ^ {d} \rho_ {j, j} \ln \rho_ {j, j} \\ = S _ {\mathrm {v n}} ^ {\max } + \sum_ {j = 1} ^ {d} \rho_ {j, j} \ln \rho_ {j, j} - \epsilon (\ln \rho_ {1, 1} - \ln \rho_ {2, 2}) (65) \\ + \left(\rho_ {1, 1} - \epsilon\right) \left(- \epsilon / \rho_ {1, 1}\right) + \left(\rho_ {2, 2} + \epsilon\right) \left(\epsilon / \rho_ {2, 2}\right) + \mathcal {O} \left(\epsilon^ {2}\right) (66) \\ = P _ {\mathrm {h s}} ^ {\mathrm {v n}} - \epsilon (\ln \rho_ {1, 1} - \ln \rho_ {2, 2}) + \mathcal {O} \left(\epsilon^ {2}\right) (67) \\ \leq P _ {\mathrm {h s}} ^ {\mathrm {v n}}. (68) \\ \end{array}
$$

Above we used  $\ln (1\pm x)\approx \pm x$  for  $x > 0$  and  $x\ll 1$

P6 The convexity of the predictability measure  $P_{\mathrm{hs}}^{l}$  is verified as follows:

$$
\begin{array}{l} P _ {\mathrm {h s}} ^ {l} (\omega \xi + (1 - \omega) \eta) - \omega P _ {\mathrm {h s}} ^ {l} (\xi) - (1 - \omega) P _ {\mathrm {h s}} ^ {l} (\eta) (69) \\ = \frac {d - 1}{d} - \sum_ {j \neq k} \left(\omega \xi_ {j, j} + (1 - \omega) \eta_ {j, j}\right) \left(\omega \xi_ {k, k} + (1 - \omega) \eta_ {k, k}\right) (70) \\ \end{array}
$$

$$
\begin{array}{l} - \omega \left(\frac {d - 1}{d} - \sum_ {j \neq k} \xi_ {j, j} \xi_ {k, k}\right) - (1 - \omega) \left(\frac {d - 1}{d} - \sum_ {j \neq k} \eta_ {j, j} \eta_ {k, k}\right) (71) \\ = \omega (1 - \omega) \sum_ {j \neq k} \left(\xi_ {j, j} - \eta_ {j, j}\right) \left(\xi_ {k, k} - \eta_ {k, k}\right) = \omega (\omega - 1) \sum_ {j \neq k} \left(\xi_ {j, j} - \eta_ {j, j}\right) ^ {2} (72) \\ \leq 0. (73) \\ \end{array}
$$

For Hilbert-Schmidt's predictability quantifier  $P_{\mathrm{hs}}^{\mathrm{vn}}$ , convexity follows from the concavity of von Neumann's entropy [50].

With this, we have shown that although Hilbert-Schmidt distance does not provide a coherence monotone, it can be used, in conjunction with the positivity of the density matrix, to provide bona fide measures for the particle and wave aspects of a quantum in  $d$ -slits interferometry.

In order to exemplify the application of our complementarity relations, we shall regard a generalized Werner's state of a ququart  $(d = 4)$  [51]:

$$
\rho_ {w, a} = (1 - w) \frac {\mathbb {I} _ {4}}{4} + w | \psi \rangle \langle \psi |, \tag {74}
$$

with  $|\psi \rangle = \sqrt{a} |\beta_0\rangle +\sqrt{1 - a} |\beta_1\rangle$ . The Hilbert-Schmidt coherence function, the linear- and von Neumann-Hilbert-Schmidt predictability measures, their sum, and the associated upper bounds are shown graphically in Fig. 3 as a function of  $a$  for some values of  $w$ .

This figure shows that  $P_{\mathrm{hs}}^{I}$  and  $P_{\mathrm{hs}}^{\mathrm{vn}}$  reach the respective upper bounds for  $\rho_{w = 1,a = 1} = |\beta_0\rangle \langle \beta_0|$  and for  $\rho_{w = 1,a = 0} = |\beta_1\rangle \langle \beta_1|$ . Besides, the equality in the complementarity relation  $C_{\mathrm{hs}} + P_{\mathrm{hs}}^{I}\leq (d - 1) / d$  is obtained for all  $\rho_{w = 1,a}$ , while the inequality  $C_{\mathrm{hs}} + P_{\mathrm{hs}}^{\mathrm{vn}}\leq \ln d$  is saturated only for  $\rho_{w = 1,a = 1}$  and  $\rho_{w = 1,a = 0}$ .

# 5.2 Complementarity relations with Wigner-Yanase's coherence

In this subsection, we will start by using the defining properties of a density matrix,  $\rho \geq 0$  and  $\mathrm{Tr}(\rho) = 1$ , to show that  $\langle \beta_j|\sqrt{\rho} |\beta_j\rangle \geq \langle \beta_j|\rho |\beta_j\rangle$ . If we define  $|r_j\rangle \coloneqq \sum_{k = 1}^{d}U_{j,k}|\beta_k\rangle$ , from the spectral decomposition  $\rho = \sum_{j = 1}^{d}r_{j}|r_{j}\rangle \langle r_{j}| = \sum_{k,l = 1}^{d}\left(\sum_{j = 1}^{d}r_{j}U_{j,k}U_{j,l}^{*}\right)|\beta_{k}\rangle \langle \beta_{l}|$ , we have  $\sqrt{\rho} = \sum_{j = 1}^{d}\sqrt{r_{j}} |r_{j}\rangle \langle r_{j}| = \sum_{k,l = 1}^{d}\left(\sum_{j = 1}^{d}\sqrt{r_{j}} U_{j,k}U_{j,l}^{*}\right)|\beta_{k}\rangle \langle \beta_{l}|$  and thus

$$
(\sqrt {\rho}) _ {j, j} = \sum_ {k} \sqrt {r _ {k}} | U _ {k, j} | ^ {2} \geq \sum_ {k} r _ {k} | U _ {k, j} | ^ {2} = \rho_ {j, j}. \tag {75}
$$

So

$$
C _ {\mathrm {w y}} (\rho) = 1 - \sum_ {j = 1} ^ {d} \left\langle \beta_ {j} \right| \sqrt {\rho} \left| \beta_ {j} \right\rangle^ {2} \tag {76}
$$

![](images/17cc8e83ef8d47ae6820a676098aaf7d27175ec0ecc5b0a5c6a9b475f1832615.jpg)

![](images/6a9962a8c1a1f96e392a050a83fbf6a99a9f60c2d5e4898616997d09e57b9ef9.jpg)  
Fig. 3 (Color online) Hilbert-Schmidt coherence function  $C_{\mathrm{hs}}$  (upper-left and lower-left plots), linear-Hilbert-Schmidt predictability  $P_{\mathrm{hs}}^{l}$  (upper-center plot), von Neumann-Hilbert-Schmidt predictability  $P_{\mathrm{hs}}^{\mathrm{vn}}$  (lower-center plot), and the sums  $C_{\mathrm{hs}} + P_{\mathrm{hs}}^{l}$  (upper-right plot) and  $C_{\mathrm{hs}} + P_{\mathrm{hs}}^{\mathrm{vn}}$  (lower-right plot) of the modified Werner's state of Eq. (74) as a function of  $a$  for some values of  $w$

![](images/162f4834661052322ab33111a18acb0c5f4c856742b3ac5dc1015dbfa1dbc602.jpg)

![](images/ae402aa6ea5165eef4691dfb92eb9764f9717dd91aebd5cd7ab6d025cec3f367.jpg)

![](images/045a5596b2ecd4ddecc0e104e50b5329e67bf3a549512090f1e0a5023d91fd37.jpg)

![](images/5b6af00fc35dd793ca9e00dc13a6e9f8528d631b2357dbae578dcb0d859f8754.jpg)

$$
\leq 1 - \sum_ {j = 1} ^ {d} \left\langle \beta_ {j} \right| \rho | \beta_ {j} \rangle^ {2} = S _ {l} \left(\rho_ {\mathrm {d i a g}}\right) \leq S _ {\mathrm {v n}} \left(\rho_ {\mathrm {d i a g}}\right), \tag {77}
$$

with  $\rho_{\mathrm{diag}} = \mathrm{diag}(\rho_{1,1},\rho_{2,2},\ldots ,\rho_{d,d})$  and the linear and von-Neumann entropies are defined in Sect. 3.1. Thus, we identify the complementarity relations:

$$
C _ {\mathrm {w y}} (\rho) + P _ {\mathrm {h s}} ^ {\tau} (\rho) \leq S _ {\tau} ^ {\max }, \tag {78}
$$

with  $\tau = l$ ,  $vn$  and with the predictability measures complementary to Wigner-Yanase's coherence being the same as for Hilbert-Schmidt's coherence, since  $\rho_{\mathrm{diag}} = \iota_{\rho}^{\mathrm{hs}}$ . These functions appear, together with  $S_{\tau}^{\mathrm{max}}$ , in Sect. 5.1. We observe that other candidate predictability measures  $P_{\mathrm{wy}}$  could be defined using the inequalities in Eqs. (42) and (43). But we do not include such functions here because for them we succeed in verifying axioms P1-P6 only in terms of changes in  $\sqrt{\rho}_{\mathrm{diag}}$ , which still lacks physical significance.

In the sequence, we verify that Wigner-Yanase's coherence satisfies the properties listed in the Introduction for a measure of the wave character of a quanton:

W1 Continuity if  $C_{\mathrm{wy}}$  follows from the continuity of  $\{(\sqrt{\rho})_{j,j}\}_{j=1}^{d}$ .  
W2 Once  $\sum_{j=1}^{d}((\sqrt{\rho})_{j,j})^2$  does not change under  $|\beta_j\rangle \leftrightarrow |\beta_k\rangle$ ,  $C_{\mathrm{wy}}$  is invariant under paths' indexes exchanges.  
W3 If  $\rho_{j,j} = 1$  for some  $j$ , then by  $\mathrm{Tr}(\rho) = 1$  we have to have  $\rho_{k,k} = 0 \forall k \neq j$ , which implies that  $\rho = |\beta_1\rangle \langle \beta_1| = \sqrt{\rho}$ . Therefore,  $(\sqrt{\rho})_{j,j} = 1$  and  $(\sqrt{\rho})_{k,k} = 0 \forall k \neq j$ . So  $C_{\mathrm{wy}} = 1 - 1 = 0$ , which is its minimum value.  
W4 If  $\rho$  is a pure state, then  $\sqrt{\rho} = \rho$ . Therefore, if  $\{\rho_{j,j} = 1 / d\}\}_{j=1}^{d}$ , then  $C_{\mathrm{wy}} = (d - 1) / d$ , which is its maximum value.  
W5 We can diminish  $|\rho_{j,k}|$  infinitesimally by taking  $\rho_{j,k}\to (1 - \epsilon)\rho_{j,k}$ , with  $\epsilon \in \mathbb{R}_{+}$  and  $\epsilon \ll 1$ . By noticing that  $\rho_{j,k} = \sum_l(\sqrt{\rho})_{j,l}(\sqrt{\rho})_{l,k}$ , we see that this change leads to  $\rho_{j,k}\rightarrow \sum_l((1 - \epsilon)(\sqrt{\rho})_{j,l})(\sqrt{\rho})_{l,k}$ , which is equivalent to multiplying the  $j$ -th row of  $\sqrt{\rho}$  by  $1 - \epsilon$ . Thus, it follows that

$$
\begin{array}{l} \tilde {C} _ {\mathrm {w y}} = \sum_ {l \neq j} | (1 - \epsilon) (\sqrt {\rho}) _ {j, l} | ^ {2} + \sum_ {k \neq j} \sum_ {l \neq k} | (\sqrt {\rho}) _ {k, l} | ^ {2} (79) \\ \approx (1 - 2 \epsilon) \sum_ {l \neq j} | (\sqrt {\rho}) _ {j, l} | ^ {2} + \sum_ {k \neq j} \sum_ {l \neq k} | (\sqrt {\rho}) _ {k, l} | ^ {2} (80) \\ = C _ {\mathrm {w y}} (\rho) - 2 \epsilon \sum_ {l \neq j} | (\sqrt {\rho}) _ {j, l} | ^ {2} (81) \\ \leq C _ {\mathrm {w y}} (\rho). (82) \\ \end{array}
$$

W6 Convexity of  $C_{\mathrm{wy}}$  follows from the convexity of Wigner-Yanase's skew information  $I_{\mathrm{wy}}$  [52].

In Fig. 4, we exemplify the application of the complementarity relations of Eq. (78) for the state of Eq. (74). The general aspects of the obtained results are similar to those described above for the Hilbert-Schmidt coherence.

![](images/ae19e29bb89204634fc2886d4aba93f838a7b49f9cf5c8f042d2f3c415aeb9d9.jpg)  
Fig. 4 (Color online) Wigner-Yanase's coherence (left plot),  $C_{\mathrm{wy}} + P_{\mathrm{hs}}^{l}$  (center plot), and  $C_{\mathrm{wy}} + P_{\mathrm{hs}}^{\mathrm{vn}}$  (right plot) for the modified Werner's state of Eq. (74) as a function of  $a$  for some values of  $w$

![](images/c3e760d13ea2774023d8443b9135d0636805457a9d4f4aba43d7cdde25f67d9f.jpg)

![](images/28b36927016b90af6aed7d60471a87c0c6604ea37e00c29b190cf1aba223a342.jpg)

# 5.3 Complementarity relations with  $I_{1}$ -norm coherence

In this subsection, we derive quantitative complementarity relations for  $d$ -dimensional systems by applying  $l_{1}$ -norm coherence [29]:

$$
\begin{array}{l} C _ {l _ {1}} (\rho) = \min  _ {\iota} | | \rho - \iota | | _ {l _ {1}} = \min  _ {\iota} \sum_ {j, k = 1} ^ {d} | (\rho - \iota) _ {j, k} | = \min  _ {\iota} \sum_ {j, k = 1} ^ {d} | \rho_ {j, k} - \iota_ {j} \delta_ {j, k} | (83) \\ = \sum_ {j \neq k} | \rho_ {j, k} |. (84) \\ \end{array}
$$

Here, we will use again  $\rho \geq \mathbb{O} \Rightarrow |\rho_{j,k}|^2 \leq \rho_{j,j} \rho_{k,k} \forall j, k$  to obtain

$$
C _ {l _ {1}} (\rho) \leq \sum_ {j \neq k} \sqrt {\rho_ {j , j} \rho_ {k , k}} \leq d - 1, \tag {85}
$$

from which follows the complementarity relation:

$$
C _ {l _ {1}} (\rho) + P _ {l _ {1}} (\rho) \leq d - 1, \tag {86}
$$

with the  $l_{1}$ -norm predictability defined as:

$$
\begin{array}{l} P _ {l _ {1}} (\rho) := d - 1 - \sum_ {j \neq k} \sqrt {\rho_ {j , j} \rho_ {k , k}} (87) \\ = d - 1 - 2 \sum_ {j <   k} \sqrt {\rho_ {j , j} \rho_ {k , k}}. (88) \\ \end{array}
$$

It worthwhile mentioning that for  $d = 2$  we can write  $P_{\mathrm{hs}}^{l}(\rho) = (\rho_{1,1} - \rho_{2,2})^{2}$ , which is similar to predictability measure used in [39,40]. But we notice that  $P = (f(\rho_{1,1}) - f(\rho_{2,2}))^{2}$  is also a bona-fide measure of predictability, with  $f$  being any monotonic increasing function of the probabilities  $\rho_{j,j}$ ,  $j = 1,2$ . Hence, for  $f(x) = \sqrt{x}$  the  $l_{1}$ -norm predictability is a generalization of two dimensional function  $P = (\sqrt{\rho_{1,1}} - \sqrt{\rho_{2,2}})^{2}$ .

Next, we verify that  $C_{l_1}$  satisfy the axioms for a measure of the wave aspect of a quanton:

W1 Continuity follows from the continuity of the absolute value function.  
W2 Invariance under paths' indexes exchange follows directly from the analytical expression for  $C_{l_1}$ .  
W3 If  $\rho_{j,j} = 1$  for some  $j$ , then  $\rho_{k,k} = 0 \forall k \neq j$  and, by  $|\rho_{j,k}|^2 \leq \rho_{j,j} \rho_{k,k}$ ,  $\rho_{j,k} = 0 \forall j \neq k$ . Therefore,  $C_{l_1} = 0$ .  
W4 If  $\{\rho_{j,j} = 1 / d\}_{j = 1}^{d}$ , then the same inequality used to prove W3 leads to  $|\rho_{j,k}| \leq 1 / d$ . The equality gives  $\mathrm{Tr}(\rho^2) = 1$  and  $C_{l_1} = d - 1$ , which is its maximum value.

W5 For  $\epsilon \in \mathbb{C}$ ,  $|\epsilon| \ll 1$ ,  $\operatorname{Re}(\rho_{j,k})\operatorname{Re}(\epsilon) > 0$ ,  $\operatorname{Im}(\rho_{j,k})\operatorname{Im}(\epsilon) > 0$ , we set  $\tilde{\rho}_{j,k} = \rho_{j,k} - \epsilon$ . Then

$$
| \tilde {\rho} _ {j, k} | = \sqrt {\left(\rho_ {j , k} - \epsilon\right) \left(\rho_ {j , k} ^ {*} - \epsilon^ {*}\right)} \tag {89}
$$

$$
\approx \sqrt {\left| \rho_ {j , k} \right| ^ {2} - 2 \operatorname {R e} \left(\rho_ {j , k} \epsilon^ {*}\right)} \tag {90}
$$

$$
\approx | \rho_ {j, k} | \left(1 - \operatorname {R e} \left(\rho_ {j, k} \epsilon^ {*}\right) / \left| \rho_ {j, k} \right| ^ {2}\right), \tag {91}
$$

which gives  $\tilde{C}_{l_1} = C_{l_1} - \mathrm{Re}(\rho_{j,k}\epsilon^*) / |\rho_{j,k}|\leq C_{l_1}$

W6 For  $0 \leq \omega \leq 1$  and  $\xi$  and  $\eta$  valid density operators, we verify convexity of  $C_{l_1}$  as follows:

$$
\begin{array}{l} C _ {l _ {1}} (\omega \xi + (1 - \omega) \eta) = \sum_ {j \neq k} | (\omega \xi + (1 - \omega) \eta) _ {j, k} | (92) \\ = \sum_ {j \neq k} | \omega \xi_ {j, k} + (1 - \omega) \eta_ {j, k} | (93) \\ \leq \sum_ {j \neq k} \left(\left| \omega \xi_ {j, k} \right| + \left| (1 - \omega) \eta_ {j, k} \right|\right) (94) \\ = \omega C _ {l _ {1}} (\xi) + (1 - \omega) C _ {l _ {1}} (\eta). (95) \\ \end{array}
$$

At last we verify that  $P_{l_1}$  satisfies the axioms listed in Sect. 1 for a measure of predictability:

P1 Continuity of  $P_{l_1}$  follows from the continuity of the square root.  
P2 The sum  $\sum_{j\neq k}\sqrt{\rho_{j,j}\rho_{k,k}}$  warrants invariance under paths' indexes exchanges.  
P3 If  $\rho_{j,j} = 1$  for some  $j$ , then  $\rho_{k,k} = 0 \forall k \neq j$ . Thus,  $P_{l_1} = d - 1 - 0$ , which is its maximum value.  
P4 If  $\{\rho_{j,j} = 1 / d\}_{j = 1}^{d}$ , then  $\sum_{j\neq k}\sqrt{\rho_{j,j}\rho_{k,k}} = d - 1$ , and  $P_{l_1} = 0$ , which is its minimum value.  
P5 In view of  $P_{2}$ , we set  $\rho_{1,1} > \rho_{2,2}$ ,  $\rho_{1,1} \to \rho_{1,1} - \epsilon$ , and  $\rho_{2,2} \to \rho_{2,2} + \epsilon$  with  $\epsilon \in \mathbb{R}_{+}$  and  $\epsilon \ll 1$ . So

$$
\begin{array}{l} \tilde {P} _ {l _ {1}} = d - 1 - 2 \sqrt {\rho_ {1 , 1} - \epsilon} \sqrt {\rho_ {2 , 2} + \epsilon} - 2 \sqrt {\rho_ {1 , 1} - \epsilon} \sum_ {k = 3} ^ {d} \sqrt {\rho_ {k , k}} \\ - 2 \sqrt {\rho_ {2 , 2} + \epsilon} \sum_ {k = 3} ^ {d} \sqrt {\rho_ {k , k}} - 2 \sum_ {j = 3} ^ {d - 1} \sum_ {k = j + 1} ^ {d} \sqrt {\rho_ {j , j} \rho_ {k , k}} \tag {96} \\ \approx d - 1 - 2 \sqrt {\rho_ {1 , 1} \rho_ {2 , 2}} (1 - \epsilon / 2 \rho_ {1, 1}) (1 + \epsilon / 2 \rho_ {2, 2}) \\ - 2 \sqrt {\rho_ {1 , 1}} (1 - \epsilon / 2 \rho_ {1, 1}) \sum_ {k = 3} ^ {d} \sqrt {\rho_ {k , k}} \\ \end{array}
$$

$$
\begin{array}{l} - 2 \sqrt {\rho_ {2 , 2}} (1 + \epsilon / 2 \rho_ {2, 2}) \sum_ {k = 3} ^ {d} \sqrt {\rho_ {k , k}} - 2 \sum_ {j = 3} ^ {d - 1} \sum_ {k = j + 1} ^ {d} \sqrt {\rho_ {j , j} \rho_ {k , k}} (97) \\ \approx P _ {l _ {1}} - \epsilon \left(\sqrt {\frac {\rho_ {1 , 1}}{\rho_ {2 , 2}}} - \sqrt {\frac {\rho_ {2 , 2}}{\rho_ {1 , 1}}}\right) - \epsilon \left(\frac {1}{\sqrt {\rho_ {2 , 2}}} - \frac {1}{\sqrt {\rho_ {1 , 1}}}\right) \sum_ {k = 3} ^ {d} \sqrt {\rho_ {k , k}} (98) \\ <   P _ {l _ {1}}. (99) \\ \end{array}
$$

P6 We will prove convexity through the positivity of the Hessian matrix  $(H_{n,m}) = (\partial_n\partial_mf)$ , with  $\partial_n\coloneqq \frac{\partial}{\partial x_n}$  and  $f = \alpha -\sum_{j\neq k}\sqrt{x_jx_k}$  where  $\alpha$  is a constant, i.e., we will verify that  $\langle y|H|y\rangle = \sum_{n,m}y_n^* y_mH_{n,m}\geq 0|\mathcal{V}|y\rangle \in \mathbb{C}^d$ . Once the diagonal and off-diagonal elements of  $H$  are given, respectively, by:  $\partial_m\partial_mf = \frac{1}{2}\sum_{j\neq m}\sqrt{x_j / x_m^3}$  and  $\partial_n\partial_mf = -1 / 2\sqrt{x_nx_m}$ , we shall have:

$$
\begin{array}{l} \langle y | H | y \rangle = \sum_ {m} | y _ {m} | ^ {2} \frac {1}{2} \sum_ {n \neq m} \sqrt {\frac {x _ {n}}{x _ {m} ^ {3}}} + \sum_ {n \neq m} y _ {n} ^ {*} y _ {m} \frac {- 1}{2 \sqrt {x _ {n} x _ {m}}} (100) \\ = \frac {1}{4} \sum_ {m \neq n} \left(\frac {\left| y _ {m} \right| ^ {2} x _ {n} ^ {1 / 2}}{x _ {m} ^ {3 / 2}} + \frac {\left| y _ {n} \right| ^ {2} x _ {m} ^ {1 / 2}}{x _ {n} ^ {3 / 2}} - \frac {y _ {n} ^ {*} y _ {m} + y _ {m} ^ {*} y _ {n}}{\sqrt {x _ {n} x _ {m}}}\right) (101) \\ = \frac {1}{4} \sum_ {m \neq n} x _ {n} ^ {1 / 2} x _ {m} ^ {1 / 2} \left(\frac {\left| y _ {m} \right| ^ {2}}{x _ {m} ^ {2}} + \frac {\left| y _ {n} \right| ^ {2}}{x _ {n} ^ {2}} - \frac {y _ {n} ^ {*} y _ {m} + y _ {m} ^ {*} y _ {n}}{x _ {n} x _ {m}}\right) (102) \\ = \frac {1}{4} \sum_ {m \neq n} x _ {n} ^ {1 / 2} x _ {m} ^ {1 / 2} \left| \frac {y _ {m}}{x _ {m}} - \frac {y _ {n}}{x _ {n}} \right| ^ {2} \geq 0. (103) \\ \end{array}
$$

In Fig. 5, we instantiate the application of the inequality of Eq. (86) for the quantum state in Eq. (74). We observe that although  $C_{l_1}$  does not reach the upper bound and  $P_{l_1}$  does reach this value only for  $\rho_{w = 1,a = 0}$  and for  $\rho_{w = 1,a = 1}$ , the coherence-predictability relation is saturated for all  $\rho_{w = 1,a}$ .

# 6 Conclusions

Quantum coherence (QC) is an important resource in Quantum Information Science [19,53-68]. In this article, we proved upper bounds for Hilbert-Schmidt's QC of a general one-qudit state  $\rho$  by its associated incoherent uncertainty measured using the linear entropy and von Neumann's entropy of the closest incoherent mixture. Similar bounds were obtained for Wigner-Yanase QC in terms of entropies of the diagonal part of  $\sqrt{\rho}$ . We also wrote these inequalities with the upper bound given in terms of the populations of the density matrix or of its square root.

We have presented numerical examples of the proven inequalities using random quantum states. These examples showed that the given upper bounds are tight for qubits and that they have their restrictiveness progressively weakened as the system dimension grows. So, in the future it would be interesting to investigate if the positivity

![](images/9ac8366c81fa1b8a46b286912168806889d21ff935758c601017b769c4bdba98.jpg)  
Fig. 5 (Color online)  $l_{1}$ -norm coherence (left plot),  $l_{1}$ -norm predictability (center plot), and  $C_{l_1} + P_{l_1}$  (right plot) for the modified Werner's state of Eq. (74) as a function of  $a$  for some values of  $w$

![](images/d3c757972d52107320524f17f26ac5008fd5c48f6b66c82d49a698b97728c72c.jpg)

![](images/d1cb308f5b3376752808d42860f7889b908e15094b5a52f8a308efa4dd2a461d.jpg)

of coefficients in Eq. (21) others than the one considered in this article (see, e.g., [69,70]) may be used to obtain similar but more generally stronger upper bounds for quantum coherence.

We showed that our inequalities can be used to derive quantitative wave-particle duality relations. In our formalism, these relations appear naturally, with the predictability measures defined by the inequalities themselves, which, by its turn, follows directly from the positivity of the density matrix (akin to what was implicitly done for 2-slit interferometers in Ref. [71]). Finding another applications for the reported inequalities is another natural continuation for the present research. One possibility for investigation is regarding coherence generation via quantum operations with restrictions on the possible density matrix populations changes [72,73]. Other promising candidate area for application of quantum coherence-incoherent uncertainty trade-off relations reported here is quantum thermodynamics [74-77]. In this scenario, if the reference basis is the energy basis, restrictions on populations changes shall be related to restrictions on energy changes. And these restrictions may be useful for analyzing thermodynamical processes that consume or create quantum coherence.

Acknowledgements This work was supported by the Coordenação de Aperfeicoamento de Pessoal de Nível Superior (CAPES), process 88882.427924/2019-01, by the Fundação de Amparo à Pesquisa do Estado do Rio Grande do Sul (FAPERGS), and by the Instituto Nacional de Ciência e Tecnologia de Informação Quántica (INCT-IQ), process 465469/2014-0.

# References

1. Fallani, L., Kastberg, A.: Cold atoms: a field enabled by light. EPL 110, 53001 (2015)  
2. Simmons, M.: A new horizon for quantum information. npj Quantum Inf. 1, 15013 (2015)  
3. Pirandola, S., Braunstein, S.L.: Physics: unite to build a quantum Internet. Nat. News 532, 169 (2016)  
4. Schleier-Smith, M.: Editorial: hybridizing quantum physics and engineering. Phys. Rev. Lett. 117, 100001 (2016)  
5. Institute of Physics Publications, The age of the qubit, (2011)  
6. Fitzsimons, J., Rieffel, F.E.G., Scarani, V.: The quantum Frontier. arXiv:1206.0785  
7. Adesso, G., Franco, R.L., Parigi, V.: Foundations of quantum mechanics and their impact on contemporary society. Philos. Trans. R. Soc. A 376, 20180112 (2018)  
8. Stuhler, J.: Quantum optics route to market. Nat. Phys. 11, 293 (2015)  
9. Preskill, J.: Quantum information and physics: some future directions. J. Mod. Opt. 47, 127 (2000)  
10. Cowen, R.: The quantum source of space-time. Nature 527, 290 (2015)  
11. Biamonte, J., Wittek, P., Pancotti, N., Rebentrost, P., Wiebe, N., Lloyd, S.: Quantum machine learning. Nature 549, 195 (2017)  
12. Popescu, S.: Bell's inequalities versus teleportation: What is nonlocality? Phys. Rev. Lett. 72, 797 (1994)  
13. Cavalcanti, P.S.D., Supic, I.: All entangled states can demonstrate nonclassical teleportation. Phys. Rev. Lett. 119, 110501 (2017)  
14. Brunner, N., Cavalcanti, D., Pironio, S., Scarani, V., Wehner, S.: Bell nonlocality. Rev. Mod. Phys. 86, 419 (2014)  
15. Branciard, C., Cavalcanti, E.G., Walborn, S.P., Scarani, V., Wiseman, H.M.: One-sided device-independent quantum key distribution: security, feasibility, and the connection with steering. Phys. Rev. A 85, 010301(R) (2012)  
16. Schnabel, R.: Squeezed states of light and their applications in laser interferometers. Phys. Rep. 684, 1 (2017)

17. Girolami, D., Souza, A.M., Giovannetti, V., Tufarelli, T., Filgueiras, J.G., Sarthour, R.S., Soares-Pinto, D.O., Oliveira, I.S., Adesso, G.: Quantum discord determines the interferometric power of quantum states. Phys. Rev. Lett. 112, 210401 (2014)  
18. Howard, M., Wallman, J.J., Veitch, V., Emerson, J.: Contextuality supplies the magic for quantum computation. Nature 510, 351 (2014)  
19. Shi, H.-L., Liu, S.-Y., Wang, X.-H., Yang, W.-L., Yang, Z.-Y., Fan, H.: Coherence depletion in the Grover quantum search algorithm. Phys. Rev. A 95, 032307 (2017)  
20. Theurer, T., Killoran, N., Egloff, D., Plenio, M.B.: Resource theory of superposition. Phys. Rev. Lett. 119, 230401 (2017)  
21. Åberg, J.: Catalytic coherence. Phys. Rev. Lett. 113, 150402 (2014)  
22. von Prillwitz, K., Rudnicki, L., Mintert, F.: Contrast in multipath interference and quantum coherence. Phys. Rev. A 92, 052114 (2015)  
23. Streltsov, A., Adesso, G., Plenio, M.B.: Quantum coherence as a resource. Rev. Mod. Phys. 89, 041003 (2017)  
24. Chitambar, E., Ma, X., Streltsov, A.: Preface: quantum coherence. J. Phys. A Math. Theor. 51, 410301 (2018)  
25. Messiah, A.: Quantum Mechanics. Dover, New York (2014)  
26. Fano, U.: Description of states in quantum mechanics by density matrix and operator techniques. Rev. Mod. Phys. 29, 74 (1957)  
27. Wilde, M.: Quantum Information Theory. Cambridge University Press, New York (2013)  
28. Maziero, J.: Hilbert-Schmidt quantum coherence in multi-qudit systems. Quantum Inf. Process. 16, 274 (2017)  
29. Baumgratz, T., Cramer, M., Plenio, M.B.: Quantifying coherence. Phys. Rev. Lett. 113, 140401 (2014)  
30. Yu, C.-S.: Quantum coherence via skew information and its polygamy. Phys. Rev. A 95, 042337 (2017)  
31. Puchała, Z., Rudnicki, L., Chabuda, K., Paraniak, M., Žyczkowski, K.: Certainty relations, mutual entanglement and non-displacable manifolds. Phys. Rev. A 92, 032109 (2015)  
32. Korzekwa, K., Lostaglio, M., Jennings, D., Rudolph, T.: Quantum and classical entropic uncertainty relations. Phys. Rev. A 89, 042122 (2014)  
33. Bagan, E., Bergou, J.A., Cottrell, S.S., Hillary, M.: Relations between coherence and path information. Phys. Rev. Lett. 116, 160406 (2016)  
34. Singh, U., Bera, M.N., Dhar, H.S., Pati, A.K.: Maximally coherent mixed states: complementarity between maximal coherence and mixedness. Phys. Rev. A 91, 052115 (2015)  
35. Cheng, S., Hall, M.J.W.: Complementarity relations for quantum coherence. Phys. Rev. A 92, 042101 (2015)  
36. Liu, F., Li, F., Chen, J., Xing, W.: Uncertainty-like relations of the relative entropy of coherence. Quantum Inf. Process. 15, 3459 (2016)  
37. Pessoa Jr., O.: Conceitos de Física Quántica. Editora Livraria da Física, São Paulo (2006)  
38. Qureshi, T.: Coherence, interference and visibility. Quanta 8, 24 (2019)  
39. Durr, S.: Quantitative wave-particle duality in multibeam interferometers. Phys. Rev. A 64, 042113 (2001)  
40. Englert, B.-G., Kaszlikowski, D., Kwek, L.C., Chee, W.H.: Wave-particle duality in multi-path interferometers: general concepts and three-path interferometers. Int. J. Quantum Inf. 6, 129 (2008)  
41. Mishra, S., Venugopalan, A., Qureshi, T.: Decoherence and visibility enhancement in multi-path interference. Phys. Rev. A 100, 042122 (2019)  
42. Bertlmann, R.A., Krammer, P.: Bloch vectors for qudits. J. Phys. A Math. Theor. 41, 235303 (2008)  
43. Kuttler, K.: Elementary Linear Algebra. Saylor Foundation, Washington, DC (2012)  
44. Avendaño, M.: Descartes' rule of signs is exact!. J. Algebra 324, 2884 (2010)  
45. Nielsen, M.A., Chuang, I.L.: Quantum Computation and Quantum Information. Cambridge University Press, Cambridge (2000)  
46. Ledoux, M.: The Concentration of Measure Phenomenon. American Mathematical Society, Providence (2001)  
47. Maziero, J.: Random sampling of quantum states: a survey of methods. Braz. J. Phys. 45, 575 (2015)  
48. Maziero, J.: Fortran code for generating random probability vectors, unitaries, and quantum states. Front. ICT 3, 4 (2016)  
49. Horn, R.A., Johnson, C.R.: Matrix Analysis. Cambridge University Press, Cambridge (2013)  
50. Wehrl, A.: General properties of entropy. Rev. Mod. Phys. 50, 221 (1978)

51. Hiroshima, T., Ishizaka, S.: Local and nonlocal properties of Werner states. Phys. Rev. A 62, 044302 (2000)  
52. Wigner, E.P., Yanase, M.M.: Information contents of distributions. Proc. Nat. Acad. Sci. USA 49, 910 (1963)  
53. Hillary, M.: Coherence as a resource in decision problems: the Deutsch-Jozsa algorithm and a variation. Phys. Rev. A 93, 012111 (2016)  
54. Kammerlander, P., Anders, J.: Coherence and measurement in quantum thermodynamics. Sci. Rep. 6, 22174 (2016)  
55. Streltsov, A., Chitambar, E., Rana, S., Bera, M.N., Winter, A., Lewenstein, M.: Entanglement and coherence in quantum state merging. Phys. Rev. Lett. 116, 240405 (2016)  
56. Yu, C., Yang, S., Guo, B.: Total quantum coherence and its applications. Quantum Inf. Process. 15, 3773 (2016)  
57. Yuan, X., Liu, K., Xu, Y., Wang, W., Ma, Y., Zhang, F., Yan, Z., Vijay, R., Sun, L., Ma, X.: Experimental quantum randomness processing. Phys. Rev. Lett. 117, 010502 (2016)  
58. Giorda, P., Allegra, M.: Coherence in quantum estimation. J. Phys. A Math. Theor. 51, 025302 (2018)  
59. Zhang, F.-L., Wang, T.: Intrinsic coherence in assisted sub-state discrimination. EPL 117, 10013 (2017)  
60. Pozzobom, M.B., Maziero, J.: Environment-induced quantum coherence spreading of a qubit. Ann. Phys. 377, 243 (2017)  
61. Buruaga, D.N.S., Sabín, C.: Quantum coherence in the dynamical Casimir effect. Phys. Rev. A 95, 022307 (2017)  
62. Li, L., Zou, J., Li, H., Li, J.-G., Wang, Y.-M., Shao, B.: Controlling energy flux into a spatially correlated environment via quantum coherence. Eur. Phys. J. D 71, 62 (2017)  
63. Brandner, K., Bauer, M., Seifert, U.: Universal coherence-induced power losses of quantum heat engines in linear response. Phys. Rev. Lett. 119, 170602 (2017)  
64. Scholes, G.D., Fleming, G.R., Chen, L.X., Aspuru-Guzik, A., Buchleitner, A., Coker, D.F., Engel, G.S., van Grondelle, R., Ishizaki, A., Jonas, D.M., Lundeen, J.S., McCusker, J.K., Mukamel, S., Ogilvie, J.P., Olaya-Castro, A., Ratner, M.A., Spano, F.C., Whaley, K.B., Zhu, X.: Using coherence to enhance function in chemical and biophysical systems. Nature 543, 647 (2017)  
65. Bengtson, C., Sjöqvist, E.: The role of quantum coherence in dimer and trimer excitation energy transfer. New J. Phys. 19, 113015 (2017)  
66. Pinto, D.F., Maziero, J.: Entanglement production by the magnetic dipolar interaction dynamics. Quantum Inf. Proc. 17, 253 (2018)  
67. Southwell, K.: Quantum coherence. Nature 453, 1003 (2008)  
68. Li, F., Bao, W.-S., Zhang, S., Huang, H., Li, T., Wang, X., Fu, X.: Role of coherence in adiabatic search algorithms. Phys. Lett. A 382, 2709 (2018)  
69. Byrd, M.S., Khaneja, N.: Characterization of the positivity of the density matrix in terms of the coherence vector representation. Phys. Rev. A 68, 062322 (2003)  
70. Kimura, G.: The Bloch vector for N-level systems. Phys. Lett. A 314, 339 (2003)  
71. Englert, B.-G.: Fringe visibility and which-way information: an inequality. Phys. Rev. Lett. 77, 2154 (1996)  
72. Brandão, F.G.S.L., Gour, G.: The general structure of quantum resource theories. Phys. Rev. Lett. 115, 070503 (2015)  
73. Chitambar, E., Gour, G.: Quantum resource theories. Rev. Mod. Phys. 91, 025001 (2019)  
74. Huber, M., Perarnau-Llobet, M., Hovhannisyan, K.V., Skrzypczyk, P., Klöckl, C., Brunner, N., Acín, A.: Thermodynamic cost of creating correlations. New J. Phys. 17, 065008 (2015)  
75. Goold, J., Huber, M., Riera, A., del Rio, L., Skrzypczyk, P.: The role of quantum information in thermodynamics—a topical review. J. Phys. A Math. Theor. 49, 143001 (2016)  
76. Anders, J., Esposito, M.: Focus on quantum thermodynamics. New J. Phys. 19, 010201 (2017)  
77. Lostaglio, M.: An introductory review of the resource theory approach to thermodynamics. Rep. Prog. Phys. 82, 114001 (2019)

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.