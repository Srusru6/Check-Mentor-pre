# Nonclassical moments and their measurement

E. V. Shchukin* and W. Vogel†

Arbeitsgruppe Quantenoptik, Fachbereich Physik, Universität Rostock, D-18051 Rostock, Germany

(Received 3 June 2005; published 12 October 2005; corrected 14 October 2005)

Practically applicable criteria for the nonclassicality of quantum states are formulated in terms of different types of moments. For this purpose the moments of the creation and annihilation operators, of two quadratures, and of a quadrature and the photon number operator turn out to be useful. It is shown that all the required moments can be determined by homodyne correlation measurements. An example of a nonclassical effect that is easily characterized by our methods is amplitude-squared squeezing.

DOI: 10.1103/PhysRevA.72.043808

PACS number(s): 42.50.Dv, 03.65.Wj, 42.50.Ar

# I. INTRODUCTION

Nonclassical effects have attracted substantial interest during the last decades. In particular due to the improvements of experimental techniques in the field of quantum optics nonclassical quantum states could be created in practice. After the first demonstration of photon antibunching [1] also sub-Poissonian photon statistics [2] and quadrature squeezing [3] could be realized.

In view of new possibilities of measurement and characterization of quantum states it became possible to more precisely consider the characterization of nonclassical effects. The experimental reconstruction of quantum states was demonstrated by balanced homodyne tomography [4] and some other methods, for a review see Ref. [5]. In principle, this allows one to completely characterize the quantum states of elementary quantum systems. On this basis an old question receives new interest: What are the typical signatures of non-classical effects?

In addition to balanced homodyne detection also homodyne correlation measurements have been considered. In the particular case of a weak local oscillator it has been shown that the method renders it possible to determine unusual types of moments, such as normally ordered moments composed of both a field quadrature and the field intensity [6-8]. An important advantage of these measurement techniques consists in the fact that even for small quantum efficiencies the correlation properties of interest are not smoothed out, as it is known in balanced homodyning [5]. For the following it is of some interest that the experimental determination of homodyne correlations in a multichannel device can be performed in practice [9].

The definition of nonclassicality that is widely accepted in quantum optics is based on the existence of a well-behaved  $P$  function. This means that a state is considered to have a classical counterpart if the  $P$ -function has the properties of a probability measure [10,11], for a nonclassical state it fails to be interpreted as a probability. However, in addition to this definition also states have been considered to be nonclassical, whose mean photon number is small [11] or whose quan-

tum fluctuations are close to the vacuum-noise level [12]. It is also interesting that nonclassical effects in weak measurements have been considered to appear even for coherent states and for thermal states of small photon numbers [13,14]. The latter example would support both additional signatures of nonclassicality. However, the coherent-state example is only consistent with the requirement of the quantum noise being close to the vacuum level [12], it does not require a small photon number. We also note that nonclassical states having negativities in the Wigner function are included in the class of nonclassical states we are dealing with.

Let us consider some recent developments of characterizing nonclassical effects of a single-mode quantum state. The attempt was made to formulate criteria that allow one to relate the nonclassicality to observable quantities. One approach consists in the use of characteristic functions of the quadrature distributions [12]. The usefulness of the nonclassicality criterion formulated in this way was successfully demonstrated in an experiment [15]. Later on this criterion turned out to be the lowest order of a hierarchy of necessary and sufficient conditions for nonclassicality [16]. This hierarchy is equivalent to the failure of Bochner's old criterion for the existence of a classical characteristic function [17,18], when it is applied to the characteristic function of the  $P$  function.

More recently the attempt was made to reformulate the notion of nonclassicality in a form which allows us to derive necessary and sufficient conditions in various representations [19]. For example, necessary and sufficient conditions in terms of quadrature moments have been obtained in this manner. These conditions in terms of moments are equivalent to those in terms of characteristic functions and to the failure of the  $P$  function to be a probability distribution. The reformulation of the problem in terms of moments includes, as special cases, some previously discussed conditions [20-22]. The connection of nonclassicality criteria with the 17th Hilbert problem has also been considered [23]. Last, but not least, it has been proposed to measure the nonclassicality of a single-mode quantum state via the entanglement potential [24]. This is of particular interest since it shows that the further investigation of the nonclassicality of single-mode quantum states is of importance even for applications that require entangled state.

The aim of the present paper consists in a more general formulation of the conditions for the nonclassicality on the

basis of observable moments [19]. Three different types of criteria will be analyzed in detail, which are formulated in terms of moments of annihilation and creation operators, of two quadrature operators, and of a quadrature and the number operator. In the latter case we will also discuss the relation of the criteria to Artin's solution of the 17th Hilbert problem. We will show that all the considered moments can be observed in a straightforward manner by homodyne correlation measurements. As a particular example for the usefulness of the methods under study we consider the characterization and detection of amplitude-squared squeezing [25].

The paper is organized as follows. Necessary and sufficient criteria for the nonclassicality are derived in terms of appropriately chosen moments in Sec. II. In Sec. III we propose some approaches for the measurement of the moments needed in the new versions of nonclassicality criteria. Special types of sufficient criteria for nonclassicality are consider in Sec. IV, with particular emphasis on the characterization of amplitude-squared squeezing. In Sec. V the concept is illustrated for a special type of minimum-uncertainty amplitude-squared squeezed states. A summary and some conclusions are given in Sec. VI.

# II. NONCLASSICALITY CRITERIA

The density operator  $\hat{\varrho}$  of any quantum state can be written in the diagonal coherent-state representation [26,27]

$$
\hat {\varrho} = \int P (\alpha) | \alpha \rangle \langle \alpha | d ^ {2} \alpha . \tag {1}
$$

A quantum state is said to be nonclassical if the corresponding  $P$  function (1) fails to be interpreted as a probability distribution on the complex plane [10,11]. Since the  $P$  function may be highly singular, the criterion must be reformulated in terms of measured quantities before it could be applied for the interpretation of experiments.

In the following we will derive different versions of criteria for the nonclassicality of a quantum state in terms of normally ordered moments of two appropriately chosen observables. It will be shown that among the possibilities of choosing two operators that completely describe the algebra of the harmonic oscillator there are at least two choices that lead to necessary and sufficient conditions for nonclassicality in terms of moments, for a brief consideration of one of these two cases see Ref. [19]. Other choices of operators, however, may only allow one to derive sufficient conditions for the nonclassicality in terms of moments. The reason for this is closely related to Artin's solution of the 17th Hilbert problem [28].

We will start with a brief review of the reformulation of the nonclassicality criteria in terms of characteristic functions [12]. In this manner it became possible to formulate a complete hierarchy of nonclassicality criteria that can be related to experimental data [16]. This approach will also be needed as the basis for a rigorous formulation of criteria in terms of moments.

# A. Characteristic functions

The characteristic function  $\Phi (\beta)$  of  $P(\alpha)$ , that is its two dimensional Fourier transform, is defined as

$$
\Phi (\beta) = \int P (\alpha) e ^ {\alpha \beta^ {*} - \alpha^ {*} \beta} d ^ {2} \alpha . \tag {2}
$$

It is easy to verify that it obeys the conditions

$$
\Phi (0) = \operatorname {T r} (\hat {\varrho}) = 1, \quad \Phi (- \beta) = \Phi^ {*} (\beta). \tag {3}
$$

Moreover,  $\Phi (\beta)$  is a continuous function of  $\beta$  for any quantum state. Therefore it obeys all the requirements to apply the following theorem introduced by Bochner [17,18].

Theorem 1 (Bochner theorem). The function  $P(\alpha)$  is a probability distribution on the complex plane if and only if for any smooth function  $f(\alpha)$  with compact support the following expression is nonnegative

$$
\int \int \Phi (\alpha - \beta) f ^ {*} (\alpha) f (\beta) d ^ {2} \alpha d ^ {2} \beta \geqslant 0. \tag {4}
$$

The Bochner theorem can also be formulated in a discrete version by replacing the integrations in Eq. (4) with sums.

The necessary and sufficient conditions for  $P(\alpha)$  being a probability measure can thus be reformulated in terms of the characteristic function. The relation (4) is fulfilled, if and only if for any order  $k = 2,3,\ldots$ , and for all complex  $\beta_{1},\dots ,\beta_{k}$  the determinants

$$
D _ {k} = D _ {k} \left(\beta_ {1}, \dots , \beta_ {k}\right) = \left| \begin{array}{c c c c} 1 & \Phi_ {1 2} & \dots & \Phi_ {1 k} \\ \Phi_ {1 2} ^ {*} & 1 & \dots & \Phi_ {2 k} \\ \Phi_ {1 k} ^ {*} & \Phi_ {2 k} ^ {*} & \dots & 1 \end{array} \right| \tag {5}
$$

obey the conditions

$$
D _ {k} \geqslant 0, \tag {6}
$$

where  $\Phi_{ij} = \Phi (\beta_i - \beta_j)$ . Consequently we arrive at the following theorem [16].

Theorem 2. A quantum state is nonclassical, if and only if there exist values  $\beta_{i}(i = 1,\dots ,k)$  for which at least one of the determinants  $D_{k}(k = 2,\ldots ,\infty)$  attains negative values:

$$
D _ {k} <   0. \tag {7}
$$

We note that it is straightforward to relate the characteristic functions  $\Phi (\beta)$  to observable characteristic functions of quadrature distributions, for more details see Refs. [12,15,16].

# B. Moments of  $\hat{a}^{\dagger},\hat{a}$

In order to derive criteria for nonclassicality in terms of moments, let us start with the normally ordered expectation value of Hermitian operators of the form [19,23]

$$
\langle : \hat {f} ^ {\dagger} \hat {f}: \rangle = \int | f (\alpha) | ^ {2} P (\alpha) d ^ {2} \alpha . \tag {8}
$$

We will consider only such functions  $\hat{f} = \hat{f} (\hat{a}^{\dagger},\hat{a})$  of the creation and annihilation operators,  $\hat{a}^{\dagger}$  and  $\hat{a}$ , respectively,

whose normally ordered form exists. From the equation above it immediately follows that on a classical state the mean value (8) is nonnegative for any operator  $\hat{f}$ . Hence the occurrence of negative mean values

$$
\langle : \hat {f} ^ {\dagger} \hat {f}: \rangle <   0 \tag {9}
$$

is a clear signature of the nonclassicality of the quantum state under consideration.

Let us first derive conditions for classicality in terms of the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$ . The fact that the mean value (8) is nonnegative for any polynomial function

$$
\hat {f} \left(\hat {a} ^ {\dagger}, \hat {a}\right) = \sum_ {k = 0} ^ {K} \sum_ {l = 0} ^ {L} c _ {k l} \hat {a} ^ {\dagger k} \hat {a} ^ {l} \tag {10}
$$

of  $\hat{a}^{\dagger}$  and  $\hat{a}$  leads to the nonnegativity of the following quadratic form:

$$
\langle : \hat {f} ^ {\dagger} \hat {f}: \rangle = \sum_ {n, k = 0} ^ {K} \sum_ {m, l = 0} ^ {L} c _ {k l} ^ {*} c _ {n m} \langle \hat {a} ^ {\dagger n + l} \hat {a} ^ {m + k} \rangle , \tag {11}
$$

where the coefficients  $c_{nm}$  are considered as independent variables. Due to Silvester's criterion it is equivalent to express this condition in terms of the determinants  $d_N$  defined by

$$
d _ {N} = \left[ \begin{array}{c c c c c c c} 1 & \langle \hat {a} \rangle & \langle \hat {a} ^ {\dagger} \rangle & \langle \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} \rangle & \langle \hat {a} ^ {\dagger 2} \rangle & \dots \\ \langle \hat {a} ^ {\dagger} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} \rangle & \langle \hat {a} ^ {\dagger 2} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} \rangle & \langle \hat {a} ^ {\dagger 3} \rangle & \dots \\ \langle \hat {a} \rangle & \langle \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} \rangle & \langle \hat {a} ^ {3} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} \rangle & \dots \\ \langle \hat {a} ^ {\dagger 2} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} \rangle & \langle \hat {a} ^ {\dagger 3} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger 3} \hat {a} \rangle & \langle \hat {a} ^ {\dagger 4} \rangle & \dots \\ \langle \hat {a} ^ {\dagger} \hat {a} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} ^ {3} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger 3} \hat {a} \rangle & \dots \\ \langle \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {3} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {4} \rangle & \langle \hat {a} ^ {\dagger} \hat {a} ^ {3} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} ^ {2} \rangle & \dots \\ N & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\ & & & & & & \\
$$

The conditions for classicality than read as

$$
d _ {N} \geqslant 0. \tag {13}
$$

To this end, however, these conditions have only been demonstrated to be necessary for the state to be classical. In order to show that they are necessary and sufficient, we will make use of Bochner's theorem.

To apply the Bochner theorem to moments, let us introduce the following operator  $\hat{f}$  for any smooth function  $f(\alpha)$  with compact support:

$$
\hat {f} = \int \underline {{f}} (\alpha): \hat {D} (\alpha): d ^ {2} \alpha . \tag {14}
$$

Due to the properties of  $f(\alpha)$  and the following expansion of the normally ordered displacement operator:  $\hat{D} (\alpha)$ :,

$$
: \hat {D} (\alpha) := \sum_ {k, l = 0} ^ {+ \infty} \frac {\alpha^ {k} (- \alpha^ {*}) ^ {l}}{k ! l !} \hat {a} ^ {\dagger k} \hat {a} ^ {l}, \tag {15}
$$

the operator (14) is correctly defined and its normally ordered form

$$
\hat {f} = \sum_ {k, l = 0} ^ {+ \infty} c _ {k l} \hat {a} ^ {\dagger k} \hat {a} ^ {l} \tag {16}
$$

exists.

The left-hand side of the expression (4) appearing in the Bochner theorem is nothing else but the mean value (8) for the operator (14),

$$
\langle : \hat {f} ^ {\dagger} \hat {f}: \rangle = \int \int \Phi (\alpha - \beta) \underline {{f}} ^ {*} (\alpha) \underline {{f}} (\beta) d ^ {2} \alpha d ^ {2} \beta . \tag {17}
$$

On the other hand, the mean value  $\langle : \hat{f}^{\dagger} \hat{f} : \rangle$  can be represented as the following series:

$$
\langle : \hat {f} ^ {\dagger} \hat {f}: \rangle = \sum_ {n, k, m, l = 0} ^ {+ \infty} c _ {k l} ^ {*} c _ {n m} \langle \hat {a} ^ {\dagger n + k} \hat {a} ^ {m + l} \rangle . \tag {18}
$$

Suppose that all the determinants (12) are nonnegative. Then all finite sums [11] are also nonnegative. As the series (18) converges, it can be approximated by finite sums (11) and due to this it must be also nonnegative. Eventually the Bochner theorem states that this is equivalent to the nonnegativity of the  $P$  function or the classicality of the state under consideration. Consequently we formulate another theorem for the nonclassicality of a quantum state.

Theorem 3. A quantum state is nonclassical if and only if at least one of the determinants  $d_{N}$  violates the condition (13), that is,

$$
d _ {N} <   0, \quad N = 3, 4, \dots . \tag {19}
$$

Note that  $d_{2}$  represent the incoherent part of the photon number

$$
d _ {2} = \langle \hat {a} ^ {\dagger} \hat {a} \rangle - \langle \hat {a} ^ {\dagger} \rangle \langle \hat {a} \rangle . \tag {20}
$$

Since this quantity is always nonnegative it yields no condition for nonclassicality.

It is possible to formulate other (sufficient) conditions for nonclassicality by considering subdeterminants of  $d_{N}$ . These subdeterminants are obtained by any pairwise cancellation of such lines and columns in  $d_{N}$  that cross in a diagonal element of the matrix. The negativity of any such subdeterminant is a sufficient condition for nonclassicality. Criteria of this type may be useful for characterizing the nonclassical properties of special quantum states. Examples for such subdeterminants and for states that can be properly characterized by the resulting sufficient conditions will be studied in Sec. IV.

# C. Moments of  $\hat{x}_{\varphi}, \hat{p}_{\varphi}$

Let us now consider two quadrature operators  $\hat{x}_{\varphi}$  and  $\hat{p}_{\varphi}$ . As the quadrature operators are defined as linear combinations of  $\hat{a}$  and  $\hat{a}^{\dagger}$ , the latter can be simply expressed in terms of the quadratures as

$$
\hat {a} = \frac {e ^ {i \varphi}}{2} \left(\hat {x} _ {\varphi} + i \hat {p} _ {\varphi}\right), \quad \hat {a} ^ {\dagger} = \frac {e ^ {- i \varphi}}{2} \left(\hat {x} _ {\varphi} - i \hat {p} _ {\varphi}\right). \tag {21}
$$

One can reformulate the criteria for nonclassicality in terms of the normally ordered moments  $\langle : \hat{x}_{\varphi}^{n} \hat{p}_{\varphi}^{m} : \rangle$  of the quadratures, as has been considered in Ref. [19]. We note that instead of using  $\hat{x}_{\varphi}$  and  $\hat{p}_{\varphi}$  the criteria could also be formulated with two arbitrary noncommuting quadratures  $\hat{x}_{\varphi}$  and  $\hat{x}_{\varphi'}$ , where  $\varphi \neq \varphi' \pm k\pi (k = 0, 1, 2, \ldots)$ . This more general form of the criteria is simply obtained by replacing  $\hat{p}_{\varphi}$  with  $\hat{x}_{\varphi'}$  in the criteria derived below.

In the following we will make use of the fact that any operator  $\hat{f}$  whose normally ordered form exists can be written as a normally ordered power series with respect to  $\hat{x}_{\varphi}$  and  $\hat{p}_{\varphi}$ ,

$$
\hat {f} = \sum_ {n, m = 0} ^ {+ \infty} \widetilde {c} _ {n m}: \hat {x} _ {\varphi} ^ {n} \hat {p} _ {\varphi} ^ {m}. \tag {22}
$$

It is important that we use normally ordering here. An expansion of  $\hat{f}$  of the same structure, but the normally ordered terms:  $\hat{x}_{\varphi}^{n}\hat{p}_{\varphi}^{m}$ : being replaced with  $\hat{x}_{\varphi}^{n}\hat{p}_{\varphi}^{m}$ , may not exist. From the representation (22) it follows that the state is classical if and only if all the determinants  $\widetilde{d}_N$  defined by

$$
\widetilde {d} _ {N} = \left\{ \begin{array}{c c c c} 1 & \langle : \hat {x} _ {\varphi}: \rangle & \langle : \hat {p} _ {\varphi}: \rangle & \dots \\ \langle : \hat {x} _ {\varphi}: \rangle & \langle : \hat {x} _ {\varphi} ^ {2}: \rangle & \langle : \hat {x} _ {\varphi} \hat {p} _ {\varphi}: \rangle & \dots \\ \langle : \hat {p} _ {\omega}: \rangle & \langle : \hat {x} _ {\omega} \hat {p} _ {\omega}: \rangle & \langle : \hat {p} _ {\omega} ^ {2}: \rangle & \dots \\ \hline N & & & \end{array} \right\} \tag {23}
$$

are nonnegative:

$$
\widetilde {d} _ {N} \geqslant 0. \tag {24}
$$

Consequently, the criteria for nonclassicality can be equivalently formulated by the following theorem.

Theorem 4. A quantum state is nonclassical if and only if

at least one of the determinants  $\widetilde{d}_N$  violates the condition (24), that is,

$$
\widetilde {d} _ {N} <   0, \quad N = 2, 3, \dots . \tag {25}
$$

In this version already the condition  $\tilde{d}_2 < 0$  gives insight into the nonclassicality of quantum states. It represents the condition for quadrature squeezing

$$
\widetilde {d} _ {2} = \langle : (\Delta \hat {x} _ {\varphi}) ^ {2}: \rangle <   0. \tag {26}
$$

Note that from the nonclassicality conditions in Eq. (25) together with Eq. [23] we may derive further conditions by pairwise cancellation of such lines and columns in the determinants that cross in the main diagonal. For example, one may formulate conditions such as

$$
s _ {\varphi} ^ {(2)} = \left| \begin{array}{l l} \langle : \hat {x} _ {\varphi} ^ {2} \cdot \rangle & \langle : \hat {x} _ {\varphi} ^ {2} \hat {p} _ {\varphi} \cdot \rangle \\ \langle : \hat {x} _ {\varphi} ^ {2} \hat {p} _ {\varphi} \cdot \rangle & \langle : \hat {x} _ {\varphi} ^ {2} \hat {p} _ {\varphi} ^ {2} \cdot \rangle \end{array} \right| <   0. \tag {27}
$$

Conditions formulated in terms of such subdeterminants in some cases may be more efficient to describe particular non-classical effects as the formal application of the hierarchy of the determinants  $d_{N}$ , for an example see Ref. [19].

# D. Moments of  $\hat{x}_{\varphi}, \hat{n}$

It is also possible to use other pairs of operators that together with the unit operator generate the whole operator algebra of the harmonic oscillator. Let us consider the position operator  $\hat{x}_{\varphi}$  and the photon number operator  $\hat{n}$ . The annihilation and creation operators  $\hat{a}$  and  $\hat{a}^{\dagger}$  are expressed in terms of the  $\hat{x}_{\varphi}$  and  $\hat{n}$  as follows:

$$
\hat {a} = \frac {1}{2} (\hat {x} _ {\varphi} + [ \hat {x} _ {\varphi}, \hat {n} ]) e ^ {i \varphi}, \quad \hat {a} ^ {\dagger} = \frac {1}{2} (\hat {x} _ {\varphi} - [ \hat {x} _ {\varphi}, \hat {n} ]) e ^ {- i \varphi}. \tag {28}
$$

In the present case, however, we need to use the commutation relation  $[\hat{a},\hat{a}^{\dagger}] = 1$  to express the operators  $\hat{a}$ ,  $\hat{a}^{\dagger}$  in terms of  $\hat{x}_{\varphi}$ ,  $\hat{n}$ . Therefore it is no longer possible to substitute the expressions (28) into the expansion (16) and to rewrite the normally ordered form [16] of the operator  $\hat{f}$  in terms of normally ordered expressions in  $\hat{x}_{\varphi}$  and  $\hat{n}$  as follows:

$$
\hat {f} = \sum_ {k, l = 0} ^ {+ \infty} \tilde {\hat {c}} _ {k l}: \hat {x} _ {\varphi} ^ {k} \hat {n} ^ {l}:.. \tag {29}
$$

To make this more clear, already a linear term in Eq. (16), such as  $c_{01}\hat{a}$ , has no representation in the form of Eq. (29).

As a consequence of this fact one cannot conclude that the determinants that are similar to Eqs. (12) and (23), but with the moments  $\langle : \hat{x}_{\varphi}^{k} \hat{n}^{l} : \rangle$  instead of  $\langle (\hat{a}^{\dagger})^{k} \hat{a}^{l} \rangle$  and  $\langle : \hat{x}_{\varphi}^{k} \hat{p}_{\varphi}^{l} : \rangle$ , respectively, form a complete hierarchy of criteria. The reason for this is the following. The nonexistence of a representation of the form (29) for a general operator prevents one from relating these determinants to the Bochner theorem. Thus the corresponding determinants do not lead to necessary and sufficient conditions for nonclassicality.

Because of this situation we will formulate only necessary conditions for classicality or, the other way around, we will derive sufficient conditions for nonclassicality in terms of the

moments  $\langle : \hat{x}_{\varphi}^{k} \hat{n}^{l} : \rangle$ . The mean value of the normally ordered operator:  $\hat{F}(\hat{x}_{\varphi}, \hat{n})$ : can be expressed in terms of the  $P$  function as

$$
\langle : \hat {F} (\hat {x} _ {\varphi}, \hat {n}): \rangle = \int F [ 2 \operatorname {R e} (\alpha e ^ {- i \varphi}), | \alpha | ^ {2} ] P (\alpha) d ^ {2} \alpha . \tag {30}
$$

For any classical state and for any operator  $F(\hat{x}_{\varphi}, \hat{n})$  with a nonnegative associated  $c$ -number function  $F(2 \operatorname{Re} \alpha, |\alpha|^2)$  the mean value (30) is nonnegative. If we identify  $\hat{F}(\hat{x}, \hat{n})$ : with  $\hat{f}^{\dagger} \hat{f}$ : together with the special form  $\hat{f}$  given in Eq. (29), we derive necessary conditions for classicality in terms of the determinants

$$
d _ {N} ^ {(1)} = \underbrace {\left| \begin{array}{c c c c} 1 & \langle : \hat {x} _ {\varphi}: \rangle & \langle : \hat {n}: \rangle & \dots \\ \langle : \hat {x} _ {\varphi}: \rangle & \langle : \hat {x} _ {\varphi} ^ {2}: \rangle & \langle : \hat {x} _ {\varphi} \hat {n}: \rangle & \dots \\ \langle : \hat {n}: \rangle & \langle : \hat {x} _ {\varphi} \hat {n}: \rangle & \langle : \hat {n} ^ {2}: \rangle & \dots \\ \hline N & \end{array} \right|} _ {N} \tag {31}
$$

as

$$
d _ {N} ^ {(1)} \geqslant 0. \tag {32}
$$

Consequently, if

$$
d _ {N} ^ {(1)} <   0, \quad N = 2, 3, \dots , \tag {33}
$$

the nonclassical properties of the considered quantum state have been verified by a sufficient but not necessary condition.

The latter can be illustrated as follows. There exist operators  $F(\hat{x}_{\varphi}, \hat{n})$  of different kind whose associated  $c$ -number function  $\hat{F}(2 \operatorname{Re}(\alpha e^{i\varphi}), |\alpha|^2)$  is nonnegative. Let us consider

$$
F \left(\hat {x} _ {\varphi}, \hat {n}\right) = \left(4 \hat {n} - \hat {x} _ {\varphi} ^ {2}\right) \hat {f} ^ {\dagger} \left(\hat {x} _ {\varphi}, \hat {n}\right) \hat {f} \left(\hat {x} _ {\varphi}, \hat {n}\right). \tag {34}
$$

It is clear that the corresponding function is nonnegative

$$
\begin{array}{l} F (2 \operatorname {R e} (\alpha e ^ {- i \varphi}), | \alpha | ^ {2}) = 4 \operatorname {I m} ^ {2} (\alpha e ^ {- i \varphi}) \\ \times | f [ 2 \operatorname {R e} (\alpha e ^ {- i \varphi}), | \alpha | ^ {2} ] | ^ {2} \geqslant 0. \tag {35} \\ \end{array}
$$

This leads to the following necessary conditions for the nonnegativity of the  $P$  function:

$$
d _ {N} ^ {(2)} \geqslant 0, \tag {36}
$$

which is formulated in terms of the determinants

$$
d _ {N} ^ {(2)} = \underbrace {\left| \begin{array}{l l l} 4 m _ {0 1} - m _ {2 0} & 4 m _ {0 2} - m _ {2 1} & \dots \\ 4 m _ {0 2} - m _ {2 1} & 4 m _ {0 3} - m _ {2 2} & \dots \\ & N \end{array} \right|} \tag {37}
$$

with

$$
m _ {k l} = \left\langle : \hat {x} _ {\varphi} ^ {k} \hat {n} ^ {l}: \right\rangle . \tag {38}
$$

Consequently, the violation of the nonnegativity of one such determinant

$$
d _ {N} ^ {(2)} <   0, \quad N = 1, 2, \dots , \tag {39}
$$

is sufficient to demonstrate the nonclassical behavior of a quantum state. Note that these conditions already characterize nonclassical effects by the first order determinant  $d_{1}$ . By inspection of its expression,

$$
d _ {1} = 4 \langle \hat {n} \rangle - \left\langle : \hat {x} _ {\varphi} ^ {2}: \right\rangle = \left\langle : \hat {p} _ {\varphi} ^ {2}: \right\rangle = \left\langle : \hat {x} _ {\varphi + \pi / 2} ^ {2}: \right\rangle , \tag {40}
$$

we observe that the condition  $d_1^{(2)} < 0$  reproduces the condition for quadrature squeezing provided that  $\langle \hat{x}_{\varphi + \pi / 2} \rangle = 0$ , that is for quantum states whose mean amplitude is vanishing, as, for example, in a squeezed vacuum state.

# E. Relation to the 17th Hilbert problem

In his famous address to the 1900 International Congress of Mathematicians Hilbert formulated 23 problems that he considered to be the most important problems to be solved in the following century. The 17th problem, in its simplest form, was solved by Artin in 1926. Artin's solution can be formulated in the following theorem (see, e.g., Ref. [28]):

Theorem 5 (17th Hilbert problem). Any nonnegative polynomial  $F(x_{1},\ldots ,x_{n})\in \mathbf{R}[x_{1},\ldots ,x_{n}]$

$$
F \left(x _ {1}, \dots , x _ {n}\right) \geqslant 0, \quad \forall \left(x _ {1}, \dots , x _ {n}\right) \in \mathbf {R} ^ {n}, \tag {41}
$$

can be represented as a finite sum of squares of rational functions

$$
F \left(x _ {1}, \dots , x _ {n}\right) = \sum_ {k = 1} ^ {N} R _ {k} ^ {2} \left(x _ {1}, \dots , x _ {n}\right), \tag {42}
$$

where  $R_{k}(x_{1},\ldots ,x_{n})\in \mathbf{R}(x_{1},\ldots ,x_{n})$  , i.e.,

$$
R _ {k} \left(x _ {1}, \dots , x _ {n}\right) = \frac {F _ {k} \left(x _ {1} , \dots , x _ {n}\right)}{G _ {k} \left(x _ {1} , \dots , x _ {n}\right)}, \tag {43}
$$

and all  $F_{k}$  and  $G_{k}$ ,  $k = 1, \ldots, N$  are polynomials

$$
F _ {k} \left(x _ {1}, \dots , x _ {n}\right), \quad G _ {k} \left(x _ {1}, \dots , x _ {n}\right) \in \mathbf {R} \left[ x _ {1}, \dots , x _ {n} \right]. \tag {44}
$$

This theorem is useful for getting deeper insight in the general problem of formulating conditions for the nonclassicality of quantum states in such cases as discussed in the preceding subsection. For this purpose let us consider the nonnegativity condition to be fulfilled for any quantum state that has a classical counterpart. Let us restrict the class of functions  $F(x_{1},x_{2})$ , with  $x_{1} = 2\operatorname{Re}(\alpha e^{-i\varphi})$  and  $x_{2} = |\alpha|^{2}$ , on the right-hand side (RHS) of Eq. (30) to polynomials. Now we may formulate the nonclassicality conditions in terms of the operators  $\hat{x}_{\varphi}$  and  $\hat{n}$  by using Artin's solution of the 17th Hilbert problem as follows:

$$
\langle : \hat {F} (\hat {x} _ {\varphi}, \hat {n}): \rangle = \sum_ {k = 1} ^ {N} \left\langle : \frac {\hat {F} _ {k} ^ {2} (\hat {x} _ {\varphi} , \hat {n})}{\hat {G} _ {k} ^ {2} (\hat {x} _ {\varphi} , \hat {n})}: \right\rangle <   0. \tag {45}
$$

That is, the condition for nonclassicality leads to normally ordered expectation values of fractions of squares of polynomials. The extension of the conditions beyond polynomial functions is not obvious, nor it is straightforward to formulate necessary and sufficient conditions for nonclassicality in

terms of normally ordered moments of  $\hat{x}_{\varphi}$  and  $\hat{n}$ . Also other types of operators, even if they render it possible to span the algebra of the harmonic oscillator by using commutation rules, are expected to lead to similar problems.

In the cases of the operators  $\hat{a}^{\dagger}$  and  $\hat{a}$ , on one hand, and  $\hat{x}_{\varphi}$  and  $\hat{p}_{\varphi}$ , on the other, these problems do not exist. The general form of functions according to the solution of the 17. Hilbert problem is not needed due to the direct relation of the considered expectation values  $\langle : \hat{f}^{\dagger} \hat{f} : \rangle$  to the Bochner theorem. This allowed us to directly formulate necessary and sufficient conditions for the nonclassicality in terms of the moments of these operators. In the following we will consider the possibilities to measure these moments. This eventually allows one to characterize nonclassical states by measurable moments.

# III. MEASUREMENT OF MOMENTS

In the preceding section we have considered the formulation of criteria for the nonclassicality of quantum states in terms of moments. Such criteria are only of practical interest if one can design measurement principles that allow one to determine the corresponding moments. Since these schemes will depend on the types of moments, we will consider them separately. All these detection schemes will be based on homodyne correlation measurements. An important advantage of such measurements consists in the fact that the accessible information on a quantum state is not smoothed out by small detection efficiencies.

Homodyne correlation measurements with a weak local oscillator have been proposed for measuring squeezing and anomalous moments, containing nonequal powers in the annihilation and creation operators, in resonance fluorescence [6]. This measurement principle was studied in more detail [7], where the detection of quantum correlations of the photon number and a quadrature operator has been analyzed. Later on such measurements have also been considered for determining particular nonclassical properties of light [8]. In the following we will modify the method in such a way that it becomes possible to determine the different types of moments considered in the preceding section.

# A. Detection of  $\langle \hat{a}^{\dagger k}\hat{a}^l\rangle$

Let us consider the detection scheme presented in Fig. 1. As an example we have shown a measurement scheme of depth  $d = 2$ , where the depth is the number of beam splitters between the entrance beam splitter  $\mathrm{BS}_0$  and any of the detectors  $\mathrm{PD}_1, \ldots, \mathrm{PD}_4$ . An auxiliary photodetector  $\mathrm{PD}_a$  is used here and in the following measurement schemes to record, simultaneously with the correlation measurements of interest, the intensity of the local oscillator. In principle the measurement device could be further extended to an arbitrary value of depth  $d$ . Below we will show that such a scheme allows one to measure the moments  $\langle \hat{a}^{\dagger k}\hat{a}^l\rangle$  for  $k,l = 0,1,\dots,2^{d}$ .

The entrance beam splitter for the signal field  $\mathrm{BS}_0$  is characterized by the parameters  $T_{0}$  and  $R_0$  with

![](images/5e05de38eda918ed84317fff78d407f80c86ebfbcd16efe2513a90112b027c65.jpg)  
FIG. 1. (Color online) Scheme for measuring the moments  $\langle (\hat{a}^{\dagger})^{k}\hat{a}^{l}\rangle$

$$
\left| T _ {0} \right| \gg \left| R _ {0} \right|, \tag {46}
$$

so that the signal field of interest is almost completely used for the correlation measurements. In our scheme the strength of the local oscillator on the detectors is typically of the same order of magnitude as the signal field, which is easily realized with a weakly reflecting entrance beam splitter. All the other beam splitters in the device are  $50\% - 50\%$ , so that their parameters  $T_{k}$  and  $R_{k}$  can be written in the simple form

$$
T _ {k} = \frac {1}{\sqrt {2}} e ^ {i \varphi_ {k}}, \quad R _ {k} = \frac {i}{\sqrt {2}} e ^ {i \varphi_ {k}}. \tag {47}
$$

The operator  $\hat{a}_0$  describing the field behind the entrance beam splitter  $\mathrm{BS}_0$  reads as

$$
\hat {a} _ {0} = \frac {1}{\sqrt {2}} \left(T _ {0} \hat {a} + R _ {0} \hat {a} _ {\mathrm {L O}}\right). \tag {48}
$$

It is clear that all the operators  $\hat{a}_k^{(d)}$ , that describe the fields on the  $k$ th detector, are proportional to the operator  $\hat{a}_0$ ,

$$
\hat {a} _ {k} ^ {(d)} = \frac {e ^ {i \Phi_ {k}}}{\sqrt {2 ^ {d}}} \hat {a} _ {0} + \dots , \tag {49}
$$

where the ellipsis stands for a combination of the corresponding vacuum-channel operators which gives no contribution to the quantities considered below. The phase  $\Phi_k$  depends on the path leading from the beam splitter  $\mathrm{BS}_0$  to the  $k$ th photodetector  $\mathrm{PD}_k$ .

The measurement scheme can be used to detect the coincidences registered by all  $n$  photodetectors, which are described by the normally ordered correlation functions  $\Gamma_{k_1,\dots ,k_n}$  of the form

$$
\Gamma_ {k _ {1}, \dots , k _ {n}} = \langle : \hat {a} _ {k _ {1}} ^ {(d) \dagger} \hat {a} _ {k _ {1}} ^ {(d)} \dots \hat {a} _ {k _ {n}} ^ {(d) \dagger} \hat {a} _ {k _ {n}} ^ {(d)}: \rangle . \tag {50}
$$

Using Eq. (49) it is clear that these correlations do not depend on  $k_{1},\ldots ,k_{n}$  and they can be written as

$$
\Gamma^ {(n)} = \Gamma_ {k _ {1}, \dots , k _ {n}} = \frac {1}{2 ^ {n d}} \left\langle \hat {a} _ {0} ^ {\dagger n} \hat {a} _ {0} ^ {n} \right\rangle . \tag {51}
$$

Summing up over all possible combinations of  $n$  photodetectors, in order to avoid loss of measured data, we get the following function:

$$
F _ {n} = \sum_ {\left\{k _ {1}, \dots , k _ {n} \right\}} \Gamma_ {k _ {1}, \dots , k _ {n}} = \binom {2 ^ {d}} {n} \Gamma^ {(n)} = \sum_ {m = - n} ^ {n} f _ {n} (m) e ^ {i m \varphi}, \tag {52}
$$

where  $\varphi = \varphi_{\mathrm{LO}} - \pi /2$  and the coefficients  $f_{n}(m)$  read

$$
f _ {n} (m) = \frac {\binom {2 ^ {d}} {n}}{2 ^ {n d}} \sum_ {k - l = m} \binom {n} {k} \binom {n} {l} \times | T _ {0} | ^ {k + l} | R _ {0} \alpha | ^ {2 n - k - l} \langle \hat {a} ^ {\dagger k} \hat {a} ^ {l} \rangle . \tag {53}
$$

The function  $F_{n}$  in Eq. (52) is a function of the phase  $\varphi$

$$
F _ {n} = F _ {n} (\varphi), \tag {54}
$$

and the coefficients  $f_{n}(m)$  can be obtained from this function using Fourier transform

$$
f _ {n} (m) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} F _ {n} (\varphi) e ^ {- i m \varphi} d \varphi . \tag {55}
$$

Each coefficient  $f_{n}(m)$  in Eq. (53) is a combination of some moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$ . From these combinations it is possible to extract the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$  themselves step by step. The moments  $\langle \hat{a}\rangle$ ,  $\langle \hat{a}^{\dagger}\rangle$ , and  $\langle \hat{a}^{\dagger}\hat{a}\rangle$  can be obtained directly from  $F_{1}(\varphi)$ ,

$$
\langle \hat {a} \rangle = \frac {f _ {1} (- 1)}{| T _ {0} R _ {0} \alpha |},
$$

$$
\langle \hat {a} ^ {\dagger} \rangle = \frac {f _ {1} (1)}{| T _ {0} R _ {0} \alpha |},
$$

$$
\langle \hat {a} ^ {\dagger} \hat {a} \rangle = \frac {f _ {1} (0) - \left| R _ {0} \alpha \right| ^ {2}}{\left| T _ {0} \right| ^ {2}}. \tag {56}
$$

Using these moments the next step gives the explicit expressions for the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$ ,  $k,l = 1,2$ . We present the expressions only for the moments  $\langle \hat{a}^2\rangle$  and  $\langle \hat{a}^\dagger \hat{a}^2\rangle$ ,

$$
\langle \hat {a} ^ {2} \rangle = \frac {8}{3} \frac {f _ {2} (- 2)}{\left| T _ {0} R _ {0} \alpha \right| ^ {2}},
$$

$$
\langle \hat {a} ^ {\dagger} \hat {a} ^ {2} \rangle = \frac {1}{3} \frac {4 f _ {2} (- 1) - 3 \left| R _ {0} \alpha \right| ^ {2} f _ {1} (- 1)}{\left| T _ {0} ^ {3} R _ {0} \alpha \right|}. \tag {57}
$$

Figure 2 illustrates the possibility to extract the general moments  $\langle \hat{a}^{\dagger k}\hat{a}^l\rangle$ ,  $0\leqslant k$ ,  $l\leqslant 2^{d}$  step by step. The nth step is the extraction of the moments  $\langle \hat{a}^{\dagger k}\hat{a}^l\rangle$  with  $0\leqslant k$ ,  $l\leqslant n$ , i.e., the

![](images/e652900032c6cf35c8eac5ebd0d1a599d6b520be1b6123b340cafc7b0085219b.jpg)  
FIG. 2. (Color online) Step by step extraction of the moments  $\langle \hat{a}^{\dagger k}\hat{a}^l\rangle$

moments  $\langle \hat{a}^{\dagger k}\hat{a}^l\rangle$  with  $(k,l)$  corresponding to the square

$$
S _ {n} = \{(k, l) \in \mathbf {Z} ^ {2} | 0 \leqslant k, l \leqslant n \}. \tag {58}
$$

But, in fact, we do not measure the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$  themselves, we measure their combinations  $f_{n}(m)$ ,  $m = -n,\dots ,n$ , that consist of the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$ ,  $0\leqslant k$ ,  $l\leqslant n$  with additional condition  $k - l = m$ . Geometrically the combination  $f_{n}(m)$  contains the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$  with  $(k,l)$  in the intersection of the square  $S_{n}$  and the inclined line  $L_{m}:k - l = m$ . This means that using the data obtained on one step only it is impossible to extract the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$ , but assuming we have the data of previous steps it is: each combination  $f_{n + 1}(m)$  contains one new moment by comparison with  $f_{n}(m)$ . Note that  $f_{n + 1}(n + 1)$  and  $f_{n + 1}(-n - 1)$  contain one moment only,  $\langle \hat{a}^{\dagger n + 1}\rangle$  and  $\langle \hat{a}^{n + 1}\rangle$  correspondingly, so that these moments can be measured without keeping the information of previous steps. Geometrically this means that  $S_{n + 1}\cap L_m$  contains one point more by comparison with  $S_{n}\cap L_{m}$ . So, step by step it is possible to extract all the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$ ,  $0\leqslant k$ ,  $l\leqslant 2^{d}$ . The last step, the  $2^{d}$ -th, consists in the extraction of the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$  with  $k$  or  $l$  (or both) being equal to  $2^{d}$ .

# B. Detection of  $\langle : \hat{x}_{\varphi}^{k} \hat{p}_{\varphi}^{l} : \rangle$

The moments  $\langle : \hat{x}_{\varphi}^{k} \hat{p}_{\varphi}^{l} : \rangle$  can be measured with the scheme presented on the Fig. 3, as it has been proposed in Ref. [19]. In fact, this is a slightly modified version of the Noh-Fougères-Mandel device [29]. The lowest-order moments are explicitly expressed in terms of the correlation functions  $\Gamma_{j}$ ,  $\Gamma_{jk}$  according to the following formulas:

![](images/4af8d0929b8c8c8e99343976be05f6981cf1520d27cfd18c18f0355905683eb6.jpg)  
FIG. 3. (Color online) Scheme for measuring the moments  $\langle :x_{\varphi}^{k}\hat{p}_{\varphi}^{l}:.\rangle$

$$
\langle \hat {x} _ {\varphi} \rangle = \sqrt {2} \frac {\Gamma_ {3} - \Gamma_ {4}}{| \alpha |}, \quad \langle \hat {p} _ {\varphi} \rangle = \sqrt {2} \frac {\Gamma_ {1} - \Gamma_ {2}}{| \alpha |}. \tag {59}
$$

The second-order moments are of the form

$$
\langle : \hat {x} _ {\varphi^ {*}} ^ {2}: \rangle = 4 \frac {\Gamma_ {1 2} - \Gamma_ {3 4}}{| \alpha | ^ {2}} + \langle \hat {n} \rangle ,
$$

$$
\langle : \hat {p} _ {\varphi} ^ {2}: \rangle = 4 \frac {\Gamma_ {3 4} - \Gamma_ {1 2}}{| \alpha | ^ {2}} + \langle \hat {n} \rangle ,
$$

$$
\langle : \hat {x} _ {\varphi} \hat {p} _ {\varphi}. \rangle = 4 \frac {\Gamma_ {1 3} + \Gamma_ {2 4} - \Gamma_ {1 2} - \Gamma_ {3 4}}{| \alpha | ^ {2}} - \langle \hat {n} \rangle , \tag {60}
$$

where

$$
\langle \hat {n} \rangle = \Gamma_ {1} + \Gamma_ {2} + \Gamma_ {3} + \Gamma_ {4} - | \alpha | ^ {2}. \tag {61}
$$

The amplitude  $|\alpha|$  of the local oscillator is detected by the auxiliary photodetector  $\mathrm{PD}_a$ . Note that one could also try to use the measured data more efficiently as discussed in detail in the preceding subsection. However, this would lead to somewhat more complex expressions for the moments. Since the procedure is straightforward, we do not present it here.

The scheme in the form shown in Fig. 3 allows one to determine all the moments  $\langle : \hat{x}_{\varphi}^{k} \hat{p}_{\varphi}^{l} : \rangle$  up to the order of  $k + l = 4$ . The further extension of the method is straightforward. For example, each of the detectors  $\mathrm{PD}_i (i = 1, \dots, 4)$  can be replaced with a beam splitter, each of which mixing the field with a vacuum input. In their output ports the output fields are detected by pairs of photodetectors. This allows us to extract the moments up to the order of  $k + l = 8$ , and so forth.

# C. Detection of  $\langle : \hat{x}_{\varphi}^{k} \hat{n}^{l} : \rangle$

Figure 4 illustrates the possibility of measuring moments  $\langle : \hat{x}_{\varphi}^{k} \hat{n}^{l}: \rangle$  by an extended version of the homodyne cross correlation scheme considered in Ref. [7]. The moments  $\langle \hat{n} \rangle$  and  $\langle \hat{x}_{\varphi} \rangle$  can be obtained according to the following relations:

$$
\langle \hat {n} \rangle = \Gamma_ {1} + \Gamma_ {2} + \Gamma_ {3} + \Gamma_ {4} - | \alpha | ^ {2},
$$

![](images/371936732ffb6f56b5a80f1a07c0a2aa3fd9c5a1241e7ebf65b07c8d73d48e14.jpg)  
FIG. 4. (Color online) Scheme for measuring the moments  $\langle :x_{\varphi}^{k}\hat{n}^{l}:\rangle$

$$
\langle \hat {x} _ {\varphi} \rangle = \frac {1}{| \alpha | ^ {2}} \left(\Gamma_ {1} + \Gamma_ {2} - \Gamma_ {3} - \Gamma_ {4}\right). \tag {62}
$$

Higher-order moments can be extracted from the measured data step by step.

We give explicit expressions only for the second-order moments. The moment  $\langle : \hat{n}^2 : \rangle$  can be directly measured with blocked local oscillator. Note that this moment and the first-order moments together allow one to calculate the moment  $\langle : \hat{x}_{\varphi}^2 : \rangle$ :

$$
\begin{array}{l} \Gamma_ {1 3} + \Gamma_ {1 4} + \Gamma_ {2 3} + \Gamma_ {2 4} = \frac {1}{4} (\langle : \hat {n} ^ {2}: \rangle + 2 | \alpha | ^ {2} \langle \hat {n} \rangle + | \alpha | ^ {4} \\ - \left| \alpha \right| ^ {2} \left\langle : \hat {x} _ {\varphi} ^ {2}: \right\rangle). \tag {63} \\ \end{array}
$$

The moment  $\langle : \hat{n} \hat{x}_{\varphi} : \rangle$  can be obtained from the simple relation

$$
\Gamma_ {1 2} - \Gamma_ {3 4} = \frac {1}{4} \left(\left| \alpha \right| \langle : \hat {n} \hat {x} _ {\varphi}; \rangle + \left| \alpha \right| ^ {2} \langle \hat {x} _ {\varphi} \rangle\right). \tag {64}
$$

All higher-order moments can be measured in such a way with an appropriately extended version of the scheme shown in Fig. 4.

# IV. AMPLITUDE-SQUARED SQUEEZING

In this section we will consider a particular nonclassical effect which can be well described in terms of the moments-based nonclassicality criteria derived in Sec. II. The examples will also be simple from the viewpoint of the measurement of the needed moments, when the measurement principles of Sec. III are used. This example is the amplitude squared squeezing [25]. We note that for the measurement of amplitude-squared squeezing to our knowledge there exists no direct measurement principle. It has been proposed to measure the effect after the interaction with a Kerr medium [30]. Such techniques are, however, not easy to use and require sufficiently strong signal fields for realizing the nonlinear interaction before the detection. Hence a possibility of a more direct measurement of the effect would be of interest.

Let us start with the characterization of the nonclassical effects we are interested in. As a special choice of  $\hat{f}$  in the nonclassicality condition (9) let us consider the following operator:

$$
\hat {X} _ {\varphi} = \hat {a} ^ {2} e ^ {i \varphi} + \hat {a} ^ {\dagger 2} e ^ {- i \varphi}. \tag {65}
$$

According to Eq. (8) for any number  $c$  the mean value

$$
\langle : (\hat {X} _ {\varphi} - c) ^ {2}: \rangle \geqslant 0 \tag {66}
$$

is nonnegative for all classical states. For  $c = \langle \hat{X}_{\varphi} \rangle$  this gives the following condition:

$$
\langle : (\Delta \hat {X} _ {\varphi}) ^ {2:} \rangle \geqslant 0 \tag {67}
$$

or, in other words, the condition

$$
\langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle <   0 \tag {68}
$$

is sufficient for nonclassicality. We note that the condition for amplitude-squared squeezing can be easily expressed as

$$
s _ {\varphi} ^ {(2)} = \left| \begin{array}{c c c} 1 & \langle : \hat {x} _ {\varphi} \hat {p} _ {\varphi}: \rangle \\ \langle : \hat {x} _ {\varphi} \hat {p} _ {\varphi}: \rangle & \langle : \hat {x} _ {\varphi} ^ {2} \hat {p} _ {\varphi} ^ {2}: \rangle \end{array} \right| <   0, \tag {69}
$$

in terms of the moments of two quadratures.

Another way to formulate the condition for amplitudesquared squeezing is based on the moments of the operators  $\hat{a}^{\dagger},\hat{a}$ . Let us consider the subdeterminant  $s_3$  that results from the determinant (12) by canceling all its rows and columns except those beginning with the elements 1,  $\langle \hat{a}^2\rangle$  and  $\langle \hat{a}^{\dagger 2}\rangle$ . This leads to a nonclassicality condition of the form

$$
s _ {3} = \left| \begin{array}{c c c} 1 & \langle \hat {a} ^ {\dagger 2} \rangle & \langle \hat {a} ^ {2} \rangle \\ \langle \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} ^ {2} \rangle & \langle \hat {a} ^ {4} \rangle \\ \langle \hat {a} ^ {\dagger 2} \rangle & \langle \hat {a} ^ {\dagger 4} \rangle & \langle \hat {a} ^ {\dagger 2} \hat {a} ^ {2} \rangle \end{array} \right| <   0. \tag {70}
$$

We show that the negativity of this determinant is equivalent to the following condition:

$$
\langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle <   0, \quad \forall \varphi . \tag {71}
$$

In fact, the determinant (70) can be written as follows:

$$
s _ {3} = \frac {1}{4} \min  _ {\varphi} \langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle \max  _ {\varphi} \langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle . \tag {72}
$$

It is not difficult to see that the last term in the product on the right-hand side of this equality is always nonnegative

$$
\max  _ {\varphi} \langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle \geqslant 0. \tag {73}
$$

The explicit expressions for the minimum and the maximum of the variance of the operator  $\hat{X}_{\varphi}$  are

$$
\min  _ {\varphi} \langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle = 2 [ \langle \Delta \hat {a} ^ {\dagger 2} \Delta \hat {a} ^ {2} \rangle - | \langle (\Delta \hat {a} ^ {2}) ^ {2} \rangle | ],
$$

$$
\max  _ {\varphi} \langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle = 2 [ \langle \Delta \hat {a} ^ {\dagger 2} \Delta \hat {a} ^ {2} \rangle + | \langle (\Delta \hat {a} ^ {2}) ^ {2} \rangle | ]. \tag {74}
$$

It is clear that the mean value  $\langle \Delta \hat{a}^{\dagger 2}\Delta \hat{a}^{2}\rangle$  is always nonnegative. Due to the second of the equalities (74) the maximal

variance of  $\hat{X}_{\varphi}$  is always nonnegative. Hence the condition for the negativity of  $s_3$  in Eq. (72) is a direct demonstration of amplitude-squared squeezing.

An advantage of this method for demonstrating amplitude squared squeezing consists in the fact that we do not need to adjust the local oscillator phase to the noise minimum. The negativity of the considered subdeterminant demonstrates the negativity of the minimum of the normally ordered variance already. Moreover, the moments  $\langle \hat{a}^2\rangle$ ,  $\langle \hat{a}^4\rangle$ , and  $\langle \hat{a}^{\dagger 2}\hat{a}^2\rangle$  needed in the condition (70) are easily obtained by the methods of the preceding section.

# V. MINIMUM-UNCERTAINTY AMPLITUDE-SQUARED SQUEEZED STATES

Let us consider amplitude squared-squeezed states in more detail ([25,31,32]). By definition, a state is amplitude-squared squeezed if

$$
\min  _ {\varphi} \langle : (\Delta \hat {X} _ {\varphi}) ^ {2}: \rangle <   0, \tag {75}
$$

which can be rewritten in the equivalent form as

$$
\exists \varphi : \left\langle \left(\Delta \hat {X} _ {\varphi}\right) ^ {2} \right\rangle <   4 \langle \hat {n} \rangle + 2. \tag {76}
$$

We consider here a special class of amplitude-squared squeezed states that satisfy the minimum uncertainty relation [31]. For this purpose we introduce the operators

$$
\hat {X} = \hat {X} _ {\varphi}, \quad \hat {Y} = \hat {X} _ {\varphi + \pi / 2}. \tag {77}
$$

They fulfill the uncertainty relation

$$
\left\langle \left(\Delta \hat {X}\right) ^ {2} \right\rangle^ {1 / 2} \left\langle \left(\Delta \hat {Y}\right) ^ {2} \right\rangle^ {1 / 2} \geqslant 4 \langle \hat {n} \rangle + 2. \tag {78}
$$

A state satisfies the minimum uncertainty relation if

$$
\left\langle \left(\Delta \hat {X}\right) ^ {2} \right\rangle^ {1 / 2} \left\langle \left(\Delta \hat {Y}\right) ^ {2} \right\rangle^ {1 / 2} = 4 \langle \hat {n} \rangle + 2. \tag {79}
$$

In the following we will only consider pure quantum states.

As has been shown in Ref. [32], a pure state  $|\psi \rangle$  satisfies the condition (79) if it is a solution of the eigenvalue problem

$$
(\hat {X} + i \lambda \hat {Y}) | \psi \rangle = \beta | \psi \rangle , \tag {80}
$$

for all real nonnegative  $\lambda$  and any complex  $\beta$ . One can easily check that form Eq. (80) it follows that

$$
\left\langle \left(\Delta \hat {X}\right) ^ {2} \right\rangle = \lambda \left(4 \left\langle \hat {n} \right\rangle + 2\right),
$$

$$
\langle (\Delta \hat {Y}) ^ {2} \rangle = \frac {1}{\lambda} (4 \langle \hat {n} \rangle + 2). \tag {81}
$$

For either  $\lambda > 1$  or  $1 / \lambda > 1$  one of the variations on the left-hand sides of Eqs. (81) satisfies the condition (76). Therefore the state (80) is always amplitude-square squeezed, except for  $\lambda = 1$ .

It was shown in Ref. [31] that there exist solutions of Eq. (80) of the form

$$
\left| \psi (m, \lambda) \right\rangle = c _ {m} (\lambda) \hat {S} (z) H _ {m} \left(i \gamma \hat {a} ^ {\dagger}\right) | 0 \rangle , \tag {82}
$$

where

![](images/14688bc888bcbe07e23c4a5dfeb8068ac6cbf97f24f3f09fdd22c2a635582513.jpg)  
(a)  $\lambda = 1.01$

![](images/3a29ac2f845ba499511c141a094073c98c4739cfe06cf9e11adf12514d04803e.jpg)  
(c)  $\lambda = 1.1$

![](images/6ec03d4253e64f8c5de43ad22d7b3d42aff6e7abaf5bbe48da8e6522bbaab0b6.jpg)  
(b)  $\lambda = 1.05$  
FIG. 5. The  $Q$  function of amplitude square squeezed states (82) for  $m = 2$ .

![](images/cb8426ff216728f18c53c2c88ac8916a8a0cffcab5938797c406e182922183dc.jpg)  
(d)  $\lambda = 2$

$$
\gamma = \gamma (\lambda) = \left\{ \begin{array}{l l} e ^ {i \pi / 4} \sqrt {\sqrt {1 - \lambda^ {2}} / 2}, & 0 <   \lambda <   1, \\ \sqrt {\sqrt {\lambda^ {2} - 1} / 2 \lambda}, & 1 <   \lambda \end{array} \right. \tag {83}
$$

and

$$
\left| c _ {m} (\lambda) \right| ^ {2} = \left\{ \begin{array}{l l} 1, & m = 0, \\ \frac {(- 1) ^ {m}}{m ! C _ {m} ^ {- m} (2 | \gamma (\lambda) | ^ {2})}, & m > 0. \end{array} \right. \tag {84}
$$

The parameter  $\beta$  in Eq. (80) is connected with  $m$  and  $\lambda$  by the expression

$$
\beta = \left\{ \begin{array}{l l} i \sqrt {1 - \lambda^ {2}} (2 m + 1), & 0 <   \lambda <   1, \\ \sqrt {\lambda^ {2} - 1} (2 m + 1), & 1 <   \lambda . \end{array} \right. \tag {85}
$$

The parameter  $z = z(\lambda) = re^{i\varphi}$  reads

$$
\tanh  ^ {2} r = \frac {\lambda - 1}{\lambda + 1} e ^ {- 2 i \varphi}, \quad \varphi = \left\{ \begin{array}{l l} \pi / 2, & 0 <   \lambda <   1, \\ 0, & 1 <   \lambda . \end{array} \right. \tag {86}
$$

Some examples of the  $Q$  function of the states (82) are shown in Fig. 5.

In Fig. 6 we illustrate examples of the determinants for the minimum-uncertainty amplitude-squared squeezed states under study. It is of great importance that all the moments appearing in the nonclassicality condition (70) can be determined by the homodyne correlation measurement technique proposed in Sec. III A. Unless the methods of quantum-state reconstruction, for a review see Ref. [5], the measurements proposed here are even possible in cases when the overall quantum efficiency of the detection device is small.

# VI. SUMMARY AND CONCLUSION

We have shown that condition for the nonclassicality of a single-mode quantum state, that is the failure of the  $P$  func

![](images/cbccc4793f47ceb3be8a12383b97672c7862e6acd88f4238915084efdb4e56da.jpg)  
FIG. 6. The determinants  $s_3$  (70) for  $m = 2$  (solid),  $m = 3$  (dashed), and  $m = 4$  (dash-dotted).

tion to be a probability measure, can be formulated in different ways. All the versions of necessary and sufficient conditions we have formulated in this paper turn out to be special representations of the violation of Bochner's condition for the existence of a classical characteristic function of the  $P$  function. The considered formulations of different forms of nonclassicality criteria include characteristic functions of quadratures and different types of normally ordered moments. Most importantly, all the quantities under study are accessible to observation. Their measurement, however, requires one to develop new types of measurement principles.

We have proposed rather simple and direct methods of measuring three kinds of normally ordered moments of a single-mode radiation field. For each type of moments a particular detection scheme is analyzed: for the moments  $\langle \hat{a}^{\dagger k}\hat{a}^{l}\rangle$  of the creation and annihilation operators, the moments  $\langle :x_{\varphi}^{k}\hat{p}_{\varphi}^{l}:.\rangle$  of two quadratures, and the moments  $\langle :x_{\varphi}^{k}\hat{n}^{l}:.\rangle$  of a quadrature and the photon number operator. In all the considered schemes the total number  $N$  of photodetectors needed to measure these moments is at most twice as large as the largest value of  $k$  and  $l:N < 2\max (k,l)$ . We also tried to present the extraction procedure for the moments in an optimal way form the viewpoint of an effective use of the available measured data. This means that one tries to use all the data obtained in measurements. Unfortunately this does not provide the expressions for the moments of interest in its simplest form. In the simplest form one would not need to sum up the correlation functions of all possible combinations of photodetectors to get the moments. However, one would lose part of the measured data and thus this simplified approach would be less precise from the experimental point of view.

Our methods of characterizing nonclassical effects by moments of annihilation and creation operators are applied to the characterization of amplitude-squared squeezing. We have shown that our criteria give a direct insight in the effect of amplitude-squared squeezing without the need of adjusting the phase of the local oscillator. More importantly, the demonstration of amplitude-squared squeezing until now was considered to require a rather difficult and indirect observation procedure, so that this effect received little attention in the context of experiments. The measurement procedures proposed in this paper turn out to be of particular simplicity for demonstrating the amplitude-squared squeez

ing effect. This may lead to new interest in this special non-classical effect.

In conclusion we have formulated criteria for characterizing nonclassical effects of radiation fields. For all versions of nonclassicality criteria we have proposed appropriate and simple measurement principles. These principles are based on homodyne correlation techniques with a weak local oscillator. They can be used even when the quantum efficiency of the device is small. The proposed methods may open new possibilities of demonstration and practical application of nonclassical effects of radiation fields.

# ACKNOWLEDGMENTS

The authors gratefully acknowledge valuable discussions with R. Knörr, F. Liese, and Th. Richter.

# APPENDIX: MOMENTS OF AMPLITUDE-SQUARED SQUEEZED STATES

The moments  $\langle \hat{a}^{\dagger k}\hat{a}^l\rangle_m$  of the state  $|\psi_{m}\rangle$  can be obtained in the following way. Let us take

$$
\left| \widetilde {\psi} _ {m} \right\rangle = c _ {m} ^ {- 1} \left| \psi_ {m} \right\rangle = \hat {S} (z) H _ {m} (i \gamma \hat {a} ^ {\dagger}) \left| 0 \right\rangle , \tag {A1}
$$

where the parameters  $z$  and  $\gamma$  are defined by the Eqs. (86) and (83) correspondingly. It is clear that

$$
\langle \hat {a} ^ {\dagger k} \hat {a} ^ {l} \rangle_ {m} = \left\langle \tilde {\psi} _ {m} \right| \hat {a} ^ {\dagger k} \hat {a} ^ {l} \left| \tilde {\psi} _ {m} \right\rangle . \tag {A2}
$$

We calculate the quantities  $\langle \widetilde{\psi}_m|\hat{a}^{\dagger k}\hat{a}^l |\widetilde{\psi}_m\rangle$  with the help of the generating function

$$
F (x, y, u, v) = \sum_ {n, m, k, l = 0} ^ {+ \infty} \left\langle \tilde {\psi} _ {n} \right| \hat {a} ^ {\dagger k} \hat {a} ^ {l} \left| \tilde {\psi} _ {m} \right\rangle \frac {x ^ {n} y ^ {m} u ^ {k} v ^ {l}}{n ! m ! k ! l !}. \tag {A3}
$$

Clearly,

$$
\begin{array}{l} \sum_ {n, m = 0} ^ {+ \infty} \left\langle \tilde {\psi} _ {n} \right| \hat {a} ^ {\dagger k} \hat {a} ^ {l} \left| \tilde {\psi} _ {m} \right\rangle \frac {x ^ {n} y ^ {m}}{n ! m !} = \left\langle 0 \right| e ^ {- x ^ {2} - 2 i \bar {\gamma} x \hat {a}} \\ \times \hat {S} ^ {\dagger} (z) \hat {a} ^ {\dagger k} \hat {a} ^ {l} \hat {S} (z) e ^ {- y ^ {2} + 2 i \gamma y \hat {a} ^ {\dagger}} | 0 \rangle , \tag {A4} \\ \end{array}
$$

and the function  $F(x,y,u,v)$  reads as

$$
F (x, y, u, v) = \langle 0 | e ^ {- x ^ {2} - 2 i \bar {\gamma} x \hat {a}} \hat {S} ^ {\dagger} (z) e ^ {u \hat {a} ^ {\dagger}} e ^ {v \hat {a}} \hat {S} (z) e ^ {- y ^ {2} + 2 i \gamma y \hat {a} ^ {\dagger}} | 0 \rangle . \tag {A5}
$$

Using the relation

$$
\hat {a} \hat {S} (z) = \hat {S} (z) \left(\mu \hat {a} + \nu \hat {a} ^ {\dagger}\right) \tag {A6}
$$

it can be further simplified to the following form:

$$
F (x, y, u, v) = \exp \left(- \frac {1}{2} \mathbf {w} ^ {T} A \mathbf {w}\right), \tag {A7}
$$

where  $\mathbf{w} = (x,y,u,v)^T$  and

$$
A = \left( \begin{array}{c c c c} 2 & - 4 | \gamma | ^ {2} & - 2 i \bar {\nu} \gamma & - 2 i \mu \gamma \\ - 4 | \gamma | ^ {2} & 2 & 2 i \mu \bar {\gamma} & 2 i \nu \bar {\gamma} \\ - 2 i \bar {\nu} \gamma & 2 i \mu \bar {\gamma} & - \mu \bar {\nu} & - | \nu | ^ {2} \\ - 2 i \mu \gamma & 2 i \nu \bar {\gamma} & - | \nu | ^ {2} & - \mu \nu \end{array} \right). \tag {A8}
$$

From this expression it follows that

$$
\langle \tilde {\psi} _ {n} | \hat {a} ^ {\dagger k} \hat {a} ^ {l} | \tilde {\psi} _ {m} \rangle = H _ {n m k l} ^ {\{A \}} (0, 0, 0, 0), \tag {A9}
$$

where  $H_{nmkl}^{\{A\}}(0,0,0,0)$  is a four-dimensional Hermite polynomial defined as  $[\mathbf{e} = (a,b,c,d)^T]$

$$
\sum_ {n, m, k, l = 0} ^ {+ \infty} H _ {n m k l} ^ {\{A \}} (a, b, c, d) \frac {x ^ {n} y ^ {m} u ^ {k} v ^ {l}}{n ! m ! k ! l !} = \exp \left(- \frac {1}{2} \mathbf {w} ^ {T} A \mathbf {w} + \mathbf {w} ^ {T} A \mathbf {e}\right). \tag {A10}
$$

Finally, we arrive at the result

$$
\left\langle \hat {a} ^ {\dagger k} \hat {a} ^ {l} \right\rangle_ {m} = \left| c _ {m} \right| ^ {2} H _ {m m k l} ^ {\{A \}} (0, 0, 0, 0), \tag {A11}
$$

for the moments we are interested in.

[1] H. J. Kimble, M. Dagenais, and L. Mandel, Phys. Rev. Lett. 39, 691 (1977).  
[2] R. Short and L. Mandel, Phys. Rev. Lett. 51, 384 (1983).  
[3] R. E. Slusher, L. W. Hollberg, B. Yurke, J. C. Mertz, and J. F. Valley, Phys. Rev. Lett. 55, 2409 (1985).  
[4] D. T. Smithey, M. Beck, M. G. Raymer, and A. Faridani, Phys. Rev. Lett. 70, 1244 (1993).  
[5] D.-G. Welsch, W. Vogel, and T. Opatny, Homodyne Detection and Quantum-state Reconstruction Vol. 39 of Progress in Optics (Elsevier Science, Amsterdam, 1999), Chap. 2, pp. 63-211.  
[6] W. Vogel, Phys. Rev. Lett. 67, 2450 (1991).  
[7] W. Vogel, Phys. Rev. A 51, 4160 (1995).  
[8] H. J. Carmichael, H. M. Castro-Beltran, G. T. Foster, and L. A. Orozco, Phys. Rev. Lett. 85, 1855 (2000).  
[9] M. Beck, C. Dorrer, and I. A. Walmsley, Phys. Rev. Lett. 87, 253601 (2001).  
[10] U. Titulaer and R. Glauber, Phys. Rev. 140, B676 (1965).  
[11] L. Mandel, Phys. Scr. T12, 34 (1986).  
[12] W. Vogel, Phys. Rev. Lett. 84, 1849 (2000).  
[13] L. M. Johansen, Phys. Lett. A 329, 184 (2004).  
[14] L. M. Johansen and A. Luis, Phys. Rev. A 70, 052115 (2004).  
[15] A. I. Lvovsky and J. H. Shapiro, Phys. Rev. A 65, 033830 (2002).

[16] T. Richter and W. Vogel, Phys. Rev. Lett. 89, 283601 (2002).  
[17] S. Bochner, Math. Ann. 108, 378 (1933).  
[18] T. Kawata, Fourier Analysis in Probability Theory (Academic Press, New York, 1972).  
[19] E. Shchukin, T. Richter, and W. Vogel, Phys. Rev. A 71, 011802(R) (2005).  
[20] G. S. Agarwal and K. Tara, Phys. Rev. A 46, 485 (1992).  
[21] G. S. Agarwal, Opt. Commun. 95, 109 (1993).  
[22] D. N. Klyshko, Phys. Usp. 39, 573 (1996).  
[23] J. K. Korbicz, J. I. Cirac, J. Wehr, and M. Lewenstein, Phys. Rev. Lett. 94, 153601 (2005).  
[24] J. K. Asbóth, J. Calsamiglia, and H. Ritsch, Phys. Rev. Lett. 94, 173602 (2005).  
[25] M. Hillary, Phys. Rev. A 36, 3796 (1987).  
[26] E. Sudarshan, Phys. Rev. Lett. 10, 277 (1963).  
[27] R. J. Glauber, Phys. Rev. 131, 2766 (1963).  
[28] A. Prestel and C. N. Delzell, Positive Polynomials: From Hilbert's 17th Problem to Real Algebra (Springer, Berlin, 2001).  
[29] J. W. Noh, A. Fougères, and L. Mandel, Phys. Rev. Lett. 67, 1426 (1991).  
[30] M. Hillary, Phys. Rev. A 44, 4578 (1991).  
[31] J. A. Bergou, M. Hillary, and D. Yu, Phys. Rev. A 43, 515 (1991).  
[32] D. Yu and M. Hillary, Quantum Opt. 6, 37 (1994).