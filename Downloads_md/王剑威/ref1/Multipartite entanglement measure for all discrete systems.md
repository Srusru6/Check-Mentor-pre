# Multipartite entanglement measure for all discrete systems

Beatrix C. Hiesmayr and Marcus Huber

Faculty of Physics, University of Vienna, Boltzmanngasse 5, A-1090 Vienna, Austria

(Received 3 December 2007; revised manuscript received 12 June 2008; published 22 July 2008)

Via a multidimensional complementarity relation we derive an operational entanglement measure for any discrete quantum system, i.e., for any multidimensional and multipartite system. This measure admits a separation into different classes of entanglement obtained by using a flip operator  $2,3,\ldots,n$  times, defining a  $m$ -flip concurrence. This operator sum has the practical feature to allow one to calculate for mixed states bounds on this  $m$ -flip concurrence. Moreover, the information content of an  $n$ -partite multidimensional system admits a simple and intuitive interpretation in terms of single particle obtainable information, entanglement, and information due to lack of classical knowledge of the quantum state under investigation. Explicitly, the three qubit system is analyzed and, e.g., the physical difference in entanglement of the W state, the Greenberger-Horne-Zeilinger (GHZ) state, or a biseparable state is revealed.

DOI: 10.1103/PhysRevA.78.012342

PACS number(s): 03.67.Mn, 03.65.Ud

# I. INTRODUCTION

For many quantum mechanical applications entanglement is the basic ingredient. Mathematically entanglement is well-defined. However, no simple operational criterion to detect entanglement versus separability is known. Especially with multipartite entanglement, which is subject to recent research (Refs. [1-8]), there are still many open questions regarding its properties. Moreover, it is known that there exist different "kinds" of entanglement; see, e.g., Ref. [9]. It is therefore highly desirable to first find an operational measure of entanglement and second, it should provide a good classification of the different kinds of entanglement as this is the physical property which is explored by various applications such as, e.g., quantum cryptography or quantum communication; see also Refs. [10-12].

In this paper we provide both by defining a very intuitive entanglement measure which is additive for pure states and has the advantage to separate entanglement into  $2-3-\ldots,n$ -flip entanglement and for certain cases even into bipartite, tripartite, ...,  $n$ -partite entanglement. It works for any dimension and any number of particles.

Explicitly, we show for three qubit systems how this measure admits the separation of entanglement into genuine bipartite and tripartite entanglement, moreover, how its substructure is revealed, i.e., the entanglement property of each qubit with all others [see also Fig. 1].

For that we start by proposing the following separation of the information content in a  $n$ -partite quantum state of arbitrary dimension  $\rho$ :

$$
\underbrace {I (\rho) + R (\rho)} + \underbrace {E (\rho)} = n,
$$

single property entanglement

where

(1)

$$
I (\rho) := \sum_ {s = 1} ^ {n} \qquad \underbrace {\mathcal {S} _ {s} ^ {2} (\rho)} \qquad .
$$

single property of subsystem s

We will show that for certain cases:

(1)  $I(\rho)$  contains all locally obtainable information,

(2)  $E(\rho)$  contains all information encoded in entanglement, and  
(3)  $R(\rho)$  is the complementing missing information, due to a classical lack of knowledge about the quantum state.

Moreover, we show how the total amount of entanglement can be separated into  $m$ -flip concurrences:

$$
E (\rho) := \underbrace {\mathbf {C} _ {(2)} ^ {2} (\rho)} + \underbrace {\mathbf {C} _ {(3)} ^ {2} (\rho)} + (\dots)
$$

two-flip concurrence three-flip concurrence

$$
+ \quad \mathbf {C} _ {(n)} ^ {2} (\rho) \quad .
$$

n-flip concurrence

Furthermore we show that with help of the  $m$ -flip concurrence we can, at least for three qubits and possibly for even more complex systems, indeed find a quantity interpretable as

$$
E (\rho) = \underbrace {E _ {(2)} (\rho)} + \underbrace {E _ {(3)} (\rho)}
$$

bipartite entanglement tripartite entanglement

with the substructure

$$
E _ {(2)} (\rho) = E _ {(1 2)} (\rho) + E _ {(2 3)} (\rho) + E _ {(1 3)} (\rho). \tag {5}
$$

We proceed in defining or deriving step by step the involved quantities and discuss their physical content.

# II. SINGLE PROPERTY  $S_{s}$  AND BOHR'S COMPLEMENTARY RELATION

Bohr's complementary relation was first discussed to understand the double slit experiment; its information theoretic content can be formulated by the following formula [13,14]:

$$
\mathcal {S} ^ {2} (\rho) := \mathcal {P} ^ {2} (\rho) + \mathcal {C} _ {\mathrm {c o h}} ^ {2} (\rho) \leqslant 1, \tag {6}
$$

where for all pure states the equality sign is valid.  $\mathcal{C}_{\mathrm{coh}}$  is the coherence or in the case of the double slit scenario the fringe visibility which quantifies the sharpness or contrast of the interference pattern (the "wavelike property") whereas  $\mathcal{P}$  denotes the path predictability, i.e., the a priori knowledge one can have on the path taken by the interfering system (the

![](images/1f3b1beb3d3933cf971dade2d709353e79a1d6f0d91cd225f845c5ed95dd82c3.jpg)  
(a)  
Any 3 qubit state:

![](images/f3855c4f446640aea92d953dc5cd9c9650f2ec101cdaa220932a3b1682fd0ee3.jpg)  
W--3 qubit state:  
(c)  
3

![](images/37be6a3b42ce4d6e1dfb0cf21b655300363ce87e9d5ef85f9dbe353bc7b2fa99.jpg)  
GHZ state:  
(b)  
FIG. 1. (Color online) Here the information content of three qubit states,  $3 = \Sigma_{s=1}^{3}(S_{s}^{2} + M_{s}^{2}) = \Sigma_{s=1}^{3}S_{s}^{2} + E_{12} + E_{23} + E_{13} + E_{123}$ , is visualized. In (a) Bohr's complementarity relation for each qubit is drawn. (b) visualizes the GHZ state,  $\frac{1}{\sqrt{2}}\{|000\rangle + |111\rangle\}$ , which is a genuine tripartite state; the bipartite and single properties are zero. In (c) the W state,  $\frac{1}{\sqrt{3}}\{|001\rangle + |010\rangle + |100\rangle\}$ , is visualized; the single properties are nonzero as well as the bipartite entanglement. In (d) the "bi-" separable state, Eq. (26), is drawn, which shows as desired only bipartite entanglement though the 3-flip concurrence is nonzero. Therefore, as desired, particle 3 is independent of particles 1 and 2.

![](images/89c7ee22757db284f1e2036acaa5f2afc1ce1e0c39c2885929792ff4c962f152.jpg)  
"bi"-separable:  
(d)  
3

"particlelike property"). In a double slit experiment it is simply defined by  $\mathcal{P} = |P_{\mathrm{I}} - P_{\mathrm{II}}|$ , where  $P_{\mathrm{I}}$  and  $P_{\mathrm{II}}$  are the probabilities for taking each path ( $P_{\mathrm{I}} + P_{\mathrm{II}} = 1$ ). Thus given a density matrix of a two level system

$$
\rho = \frac {1}{2} \left\{\right. \left. \right] _ {2} + \vec {n} \cdot \vec {\sigma} \}, \tag {7}
$$

where the Bloch vector  $\vec{n} \in \mathbb{R}^3$  and  $|\vec{n}|^2 \leqslant 1$  and  $\sigma$ 's denote the Pauli matrices, the predictability and visibility can be expressed by

$$
\mathcal {P} = \left| \operatorname {T r} \left(\sigma_ {z} \rho\right) \right| = \left| n _ {z} \right|, \tag {8}
$$

$$
\mathcal {C} _ {\mathrm {c o h}} = 2 \left| \operatorname {T r} \left(\sigma^ {+} \rho\right) \right| = \left| n _ {x} + i n _ {y} \right|. \tag {9}
$$

For all pure states,  $|\vec{n}|^2 = 1$ , Bohr's complementary relation is fulfilled, and no information is lost. For mixed states,  $|\vec{n}|^2 \leqslant 1$ , Bohr's complementary relation is lower than 1, and this loss of information is due to ignorance of individual particles; thus it is a purely classical loss.

As has been shown this complementary relation is useful to understand several interfering two state systems as, e.g., particle-antiparticle mixing systems [15,16] or Mott scattering experiments of identical nuclei [16] or even specific thermodynamical quantum systems [17].

One can make Bohr's complementary relation always exact by adding the quantity (dimensionality  $d$ , here 2)

$$
M ^ {2} (\rho) = \frac {d}{d - 1} [ 1 - \operatorname {T r} \left(\rho^ {2}\right) ] \tag {10}
$$

to the single particle property  $\mathcal{S}$

$$
\mathcal {S} ^ {2} (\rho) + M ^ {2} (\rho) = 1 \tag {11}
$$

for all states [pure:  $M(\rho) = 0$ ].  $M(\rho)$  measures the mixedness or linear entropy which equals in this case the uncertainty of individual particles under investigation, clearly a "classical" uncertainty.

The complementarity principle seems to be an intrinsic property of all discrete quantum systems. So even considering various dynamics that a quantum system can be exposed

to [15], the two-dimensional complementarity relation still holds true. The next logical step is trying to generalize this relation for a qudit system.

# III. BOHR'S COMPLEMENTARY RELATION FOR  $d$ -DIMENSIONAL SYSTEMS

For a qudit system or a multislit system the definition of predictability is not straightforward. One approach has recently been introduced in Refs. [18,19], however, we introduce a similar approach which makes a generalization to multipartite systems possible. To do that we will first introduce the following useful quantity:

$$
P _ {i, j} := \operatorname {T r} (\rho | i \rangle \langle j |) \tag {12}
$$

and propose the generalized predictability for a quudit state  $\rho$

$$
P _ {g} (\rho) := \sqrt {\frac {d - 1}{d} \sum_ {\pi} \left| P _ {0 , 0} - \frac {P _ {1 , 1} + P _ {2 , 2} + \left(\cdots\right) + P _ {d - 1 , d - 1}}{d - 1} \right| ^ {2}} = \sqrt {\frac {d}{d - 1} \sum_ {i} \left| P _ {i , i} - \frac {1}{d} \right| ^ {2}} = \sqrt {\frac {d}{d - 1} \sum_ {i} P _ {i , i} ^ {2} - \frac {1}{d - 1}}, \tag {13}
$$

where  $\Sigma_{\pi}$  denotes the sum over all possible permutations of  $P_{i,i}$ , i.e.,  $|P_{0,0} - \dots|^2 + |P_{1,1} - (P_{0,0} + P_{2,2} + \dots) / (d - 1)|^2 + \dots$ . The first line admits for a multislit scenario the following simple interpretation: it is the difference of the probability that the particle transverses the slit, e.g.,  $P_{0,0}$ , minus the probabilities that the particle takes the way through all the other slits weighted by  $d - 1$ , summed over all slits. For  $d = 2$  it is clearly equivalent to the prior definition of predictability, it ranges from zero to one and is equal to one if one has  $100\%$  information about a possible measurement outcome and it is equal to zero if one does not have any information about which degree of freedom would most likely be measured. Thus it meets all of our conceptual requirements.

Of course it is only one of many ways to describe multilevel predictability, but one that meets all of our conceptual requirements. A different one was introduced in Ref. [18].

The coherence is easier to define; it is more straightforward. We can just take the sum over all two-dimensional coherences:

$$
\begin{array}{l} C _ {c o h, g} (\rho) := \left(\frac {2 d}{d - 1} \sum_ {j = 1} ^ {d - 1} \sum_ {i <   j} | P _ {i, j} | ^ {2}\right) ^ {1 / 2} \\ = \left[ \frac {d}{d - 1} \left(\operatorname {T r} \left(\rho^ {2}\right) - \sum_ {i} P _ {i, i} ^ {2}\right) \right] ^ {1 / 2}. \tag {14} \\ \end{array}
$$

The last equation is obtained by using  $\mathrm{Tr}(\rho^2) = \Sigma |P_{i,j}|^2$ $= \Sigma P_{i,i}^{2} + 2\Sigma_{i,j,i <   j}|P_{i,j}|^{2}$ . Again it meets also the conceptual requirements as for  $d = 2$  it is equivalent to the prior definition of coherence, it ranges from zero to one and is equal to one if one has the most coherent superposition of all degrees of freedom and it is equal to zero if one has  $100\%$  information about a possible measurement outcome.

Let us now consider the sum of generalized predictability and coherence,

$$
P _ {g} ^ {2} (\rho) + C _ {c o h, g} (\rho) ^ {2} = \frac {d}{d - 1} \operatorname {T r} \left(\rho^ {2}\right) - \frac {1}{d - 1} = - M ^ {2} + 1 \Rightarrow P _ {g} ^ {2} (\rho) + \underbrace {C _ {c o h , g} (\rho) ^ {2} + M ^ {2} (\rho)} _ {\mathcal {S} _ {g} ^ {2} (\rho)} = 1. \tag {15}
$$

The last equation is the generalized Bohr complementary relation for  $d$ -dimensional systems we searched for and helps to understand entanglement in multiqudit systems.

# IV. ENTANGLEMENT MEASURE AND ITS BOUNDS

Let us now proceed to entangled systems. For pure states it is well-known that entanglement can be solely quantified

by considering the mixedness or entropy of the subsystems. For an  $n$ -partite system where each subsystem  $s$  is given by the reduced density matrix  $\rho_{s} = \mathrm{Tr}_{[1,\ldots ,s - 1,s + 1,\ldots ,n]}(|\psi \rangle \langle \psi |)$  of dimensionality  $d_{s}$ , the sum of the mixednesses defines an entanglement measure

$$
E (| \psi \rangle) := \sum_ {s = 1} ^ {n} M ^ {2} \left(\rho_ {s}\right) := \sum_ {s = 1} ^ {n} M _ {s} ^ {2} (\rho). \tag {16}
$$

This is an entanglement measure, i.e., nonincreasing under local operations and classical communications (LOCC), additive, and meeting all requirements to be an entanglement monotone (see, e.g., Ref. [23]). The same is true for the Von Neumann entropies of the subsystems defining entanglement of formation [20], but the linear entropy  $M^2$  bears the benefit

that it can be operationally obtained and therefore simple bounds can be derived as we will show.

# A. Example: Tripartite qubit state

For convenience and clarity we consider now a tripartite qubit system and generalize then for the multipartite case. Consider the tripartite qubit state

$$
| \psi \rangle = \sum_ {i, j, k = 0} ^ {1} a _ {i j k} | i j k \rangle , \tag {17}
$$

then the mixednesses of the subsystem, e.g., of the first qubit, is straightforwardly calculated and equivalent to the following expressions obtained by simple algebra:

$$
\begin{array}{l} M_{1}^{2}(\psi) = M^{2}(\rho_{1}) = \sum_{k = 0}^{1}\sum_{\substack{\{i_{1}\neq i_{1}^{\prime}\} ;\{i_{2}\neq i_{2}^{\prime}\}}}\big|\langle \psi |(\sigma \otimes \sigma \otimes \mathbb{1})(|i_{1}i_{2}k\rangle \langle i_{1}i_{2}k| - |i_{1}^{\prime}i_{2}^{\prime}k\rangle \langle i_{1}^{\prime}i_{2}^{\prime}k|)|\psi^{*}\rangle |^{2} \\ + \sum_ {k = 0} ^ {1} \sum_ {\left\{i _ {1} \neq i _ {1} ^ {\prime} \right\}; \left\{i _ {3} \neq i _ {3} ^ {\prime} \right\}} \left| \langle \psi | (\sigma \otimes \mathbb {1} \otimes \sigma) \left(\left| i _ {1} k i _ {3} \rangle \langle i _ {1} k i _ {3} \right| - \left| i _ {1} ^ {\prime} k i _ {3} ^ {\prime} \rangle \langle i _ {1} ^ {\prime} k i _ {3} ^ {\prime} \right|\right) | \psi^ {*} \rangle \right| ^ {2} \\ + \sum_ {\{i _ {1} \neq i _ {1} ^ {\prime} \}; \{i _ {2} \neq i _ {2} ^ {\prime} \}; \{i _ {3} \neq i _ {3} ^ {\prime} \}} | \langle \psi | (\sigma \otimes \sigma \otimes \sigma) (| i _ {1} i _ {2} i _ {3} \rangle \langle i _ {1} i _ {2} i _ {3} | - | i _ {1} ^ {\prime} i _ {2} ^ {\prime} i _ {3} ^ {\prime} \rangle \langle i _ {1} ^ {\prime} i _ {2} ^ {\prime} i _ {3} ^ {\prime} |) | \psi^ {*} \rangle | ^ {2}, \\ \end{array}
$$

where  $|\psi^{*}\rangle$  denotes the complex conjugation of  $|\psi\rangle$  and  $\sigma$  is the flip operator, which equals in this case the Pauli matrix  $\sigma_{x}$ . One sees that the squared mixedness of one subsystem is obtained by flipping once in each other subsystem and flipping in all subsystems. Straightforwardly one obtains the squared mixednesses of the two other systems. As the sum of all mixednesses,  $E(\psi)$ , is an entanglement measure it is obvious to add all terms which contain two flips to one quantity which we denote by  $(\mathbf{C}_{(2)})^2$  and all terms with three flips to  $(\mathbf{C}_{(3)})^2$ . Thus we have separated the total entanglement,  $E(\psi)$  into a sum of terms containing two or three flips, which we name in the following as  $m$ -flip concurrence.

# B.  $m$ -concurrence for pure states

For multipartite quudit systems the same works. The flip operators can be defined in the following way for a quudit system of dimension  $d$ :

$$
\sigma_ {k l} ^ {d \times d} | k \rangle = | l \rangle , \quad \sigma_ {k l} ^ {d \times d} | l \rangle = | k \rangle ,
$$

$$
\text {a n d} \quad \sigma_ {k l} ^ {d \times d} | t \rangle = 0 \quad \forall \quad t \neq k, l \tag {18}
$$

with  $k, l \in \{0, 1, \ldots, d - 1\}$ . Note that this is just another definition of the  $d$ -dimensional symmetric Gellmann matrices. The squared  $m$ -flip entanglement is given by the sum over all possible permutations of  $m$  flips, i.e., for  $n$  systems there are  $\binom{n}{m}$  possibilities and each system where a flip is performed is

denoted by  $\alpha_{j}$  and in order to avoid multiple counting we order the set:  $\{\alpha_{j}\} := \alpha_{1},\alpha_{2},\ldots ,\alpha_{m}$ , where  $\alpha_{1} < \alpha_{2} < \dots < \alpha_{m}$ :

$$
\left(\mathbf {C} _ {(m)}\right) ^ {2} = \sum_ {\left\{\alpha_ {j} \right\}} \mathbf {C} _ {\left\{\alpha_ {j} \right\}} ^ {2}. \tag {19}
$$

Each possibility of  $m$  flips is derived by

$$
\mathbf {C} _ {\{\alpha_ {j} \}} ^ {2} := \sum_ {s e t} | \langle \psi | \hat {O} _ {\{\alpha_ {j} \}} (| \{i _ {n} \} \rangle \langle \{i _ {n} \} | - | \{i _ {n} ^ {\prime} \} \rangle \langle \{i _ {n} ^ {\prime} \} |) | \psi^ {*} \rangle | ^ {2}
$$

where

$$
\sum_ {s e t} := \sum_ {i \in \left\{\alpha_ {j} \right\}} \sum_ {l _ {i} = 1} ^ {d _ {i} - 1} \sum_ {k _ {i} <   l _ {i}} \underbrace {\sum_ {\left\{i _ {n} \right\} \neq \left\{i _ {n} ^ {\prime} \right\}}} _ {i _ {t} = i _ {t} ^ {\prime} \forall t \notin \left\{\alpha_ {j} \right\}} \tag {20}
$$

and

$$
\hat {O} _ {\{\alpha_ {j} \}} := \left(\sigma_ {k _ {i} l _ {i}} ^ {s \in \{\alpha_ {j} \}}, \mathbb {1} ^ {s \notin \{\alpha_ {j} \}}\right), \tag {21}
$$

which defines an  $n$ -tensor product where the flip operators are positioned at  $\alpha_{j}$  and everywhere else the unity is taken. Note that this works for  $n$ -partite systems with dimensions  $d_{1}$  to  $d_{n}$ ; and the total entanglement is given by

$$
E (\psi) := \sum_ {m = 2} ^ {n} \mathbf {C} _ {(m)} ^ {2} = \sum_ {s = 1} ^ {n} M _ {s} ^ {2} (| \psi \rangle \langle \psi |). \tag {22}
$$

This, for pure systems, is equal to the sum of the squared mixednesses of the subsystems. Also if we set  $d = n = 2$  this is just the definition of Wootter's concurrence [21] multiplied by 2.

# C.  $m$  concurrence for mixed states

Pure states are quite a strong restriction and for mixed states, the mixedness of the subsystem will not suffice because it stems from both entanglement and classical uncertainty. The  $m$ -flip concurrence for mixed density matrices can be defined by

$$
\left[ \mathbf {C} _ {g} ^ {m} (\rho) \right] ^ {2} := \inf  _ {\left| \psi_ {i} \right\rangle , p _ {i}} \sum_ {\left| \psi_ {i} \right\rangle , p _ {i}} p _ {i} \left[ \mathbf {C} _ {(m)} \left(\left| \psi_ {i} \right\rangle\right) \right] ^ {2}. \tag {23}
$$

That this is part of an analytically correct entanglement measure is obvious because:

(1)  $\Sigma_{m=2}^{n}[\mathbf{C}_{(m)}(|\psi\rangle)]^2$  is an entanglement measure for pure states.  
(2) Any separable density matrix can be decomposed into a convex sum of pure separable states, hence the infimum equals zero for all separable states.  
(3) Any entangled density matrix's decomposition contains at least one entangled pure state, hence  $\mathbf{C}_g^m (\rho)$  is part of an entanglement measure which is nonzero for all entangled states.

# D. Bounds on the  $m$ -flip concurrence

We can derive bounds for the  $m$ -flip concurrence by defining in an analogous way to Hill and Wootters' flip density matrix [21] the  $m$ -flip density matrix

$$
\begin{array}{l} \tilde {\rho} _ {\{\alpha_ {j} \}} ^ {m} = O _ {\{\alpha_ {j} \}} (| \{i _ {n} \} \rangle \langle \{i _ {n} \} | - | \{i _ {n} ^ {\prime} \} \rangle \langle \{i _ {n} ^ {\prime} \} |) \rho^ {*} \\ \times O _ {\left\{\alpha_ {j} \right\}} \left(\left| \left\{i _ {n} \right\} \right\rangle \left\langle \left\{i _ {n} \right\} \right| - \left| \left\{i _ {n} ^ {\prime} \right\} \right\rangle \left\langle \left\{i _ {n} ^ {\prime} \right\} \right|\right) \tag {24} \\ \end{array}
$$

and calculating the  $\lambda_{m}^{\{\alpha_{j}\}}$ 's which are the squared roots of the eigenvalues of  $\widetilde{\rho}_{\{\alpha_{j}\}}^{m}\rho$ . The bound can be derived as (using and improving the results of Ref. [22] by applying the Cauchy-Schwarz inequality)

$$
B ^ {m} (\rho) := \left(\sum_ {\left\{\alpha_ {j} \right\}} \sum_ {\text {s e t}} \mathbf {m a x} \left[ 0, 2 \mathbf {m a x} \left(\left\{\lambda_ {m} ^ {\left\{\alpha_ {j} \right\}} \right\}\right) - \sum \left\{\lambda_ {m} ^ {\left\{\alpha_ {j} \right\}} \right\} \right] ^ {2}\right) ^ {1 / 2}. \tag {25}
$$

This is not equivalent to the convex roof except for bipartite qubits, but a good boundary  $B^{m}(\rho) \leqslant \mathbf{C}_{g}^{m}(\rho)$  as it agreed in all cases we tried with the criterion of partial positive transposition. In the literature there exist several possible suggestions on how to improve these bounds, see, e.g., [22].

# V. m-FLIP CONCURRENCE AND  $m$ -PARTITE ENTANGLEMENT

Does the  $m$ -flip concurrence,  $\mathbf{C}_{(m)}$ , also describe the desired  $m$ -partite entanglement? The answer is no, a simple counterexample, e.g., for tripartite qubits, is

$$
\frac {1}{\sqrt {2}} \left\{\left| 0 0 \right\rangle + \left| 1 1 \right\rangle \right\} \otimes \left(\cos \alpha | 0 \rangle + \sin \alpha | 1 \rangle\right). \tag {26}
$$

Here only the first and second particles are entangled and the third ones are not; thus the tripartite entanglement should be zero, but the 3-flip entanglement derives to

$$
\mathbf {C} _ {(3)} ^ {2} = 4 | \cos \alpha \sin \alpha | ^ {2}. \tag {27}
$$

Moreover, the  $m$ -flip concurrence is not invariant under local unitaries. However, if we introduce "corrections" to the  $m$ -flip concurrence such that these new quantities are invariant under local unitaries we obtain the desired  $m$ -partite entanglement. For sake of simplicity we stick here to the case of three qubits.

Three qubit states. There exist two entangled states, the well-known Greenberger-Horne-Zeilinger (GHZ) state and the W state, which are obviously in a physically different way entangled. If one traces over one subsystem, in the first case one gets a separable state and in the second case an entangled state.

For that let us discuss the states  $\rho_{\alpha} = |\phi (\alpha)\rangle \langle \phi (\alpha)|$  with

$$
\left| \phi (\alpha) \right\rangle = \frac {\sin \alpha}{\sqrt {3}} \left\{\left| 0 0 1 \right\rangle + \left| 0 1 0 \right\rangle + \left| 1 0 0 \right\rangle \right\} + \cos \alpha | 1 1 1 \rangle , \tag {28}
$$

which are superpositions of the W state and a separable state. It is also plotted in Fig. 2. For  $\alpha = \frac{\pi}{3} / \frac{2\pi}{3}$  the state is unitary equivalent to the GHZ state  $(\frac{1}{2}\{|000\rangle + |111\rangle\})$ . This is at the first side surprising, because the 3-flip and the 2-flip concurrences derive to

$$
\mathbf {C} _ {(3)} ^ {2} = 0,
$$

$$
\mathbf {C} _ {(2)} ^ {2} = \frac {8}{3} \left[ \sin^ {4} (\alpha) + 3 \cos^ {2} (\alpha) \sin^ {2} (\alpha) \right], \tag {29}
$$

![](images/e6bf40d833b49eb505e137007abdf16250308e08ee95b10b74d39db43f150fb5.jpg)  
FIG. 2. (Color online) Here the information content in bits of the state  $\rho_{\alpha}$ , Eq. (28), is plotted. The colored, thickened, and dashed curves are the single properties  $I = \Sigma_{s=1}^{3} S_{s}$  (blue), the 2-partite entanglement  $E_{(2)} = E_{12} + E_{13} + E_{23}$  (green), and the 3-partite entanglement  $E_{(3)} = E_{123}$  (red). For the GHZ state  $\alpha = \frac{\pi}{3} / \frac{2\pi}{3}$  the 3-partite entanglement is maximal while for the W state  $\alpha = \frac{\pi}{2}$  the 2-partite entanglement is maximal. For  $\alpha = \frac{\pi}{6} / \frac{5\pi}{6}$  we obtain another interesting state, the 2-partite entanglement has a second maximum.

i.e., the 3-flip is zero. For the W state  $(\alpha = \frac{\pi}{2})$  on the other side the 2-flip has a local minimum. These facts suggest that we have to "correct" the flip concurrences to obtain the  $m$ -partite entanglement in the following way:

$$
\begin{array}{l} E _ {(2)} = E _ {1 2} + E _ {1 3} + E _ {2 3} \\ = \mathbf {C} _ {(2)} ^ {2} [ \mathrm {T r} _ {1} (\rho_ {\alpha}) ] + \mathbf {C} _ {(2)} ^ {2} [ \mathrm {T r} _ {2} (\rho_ {\alpha}) ] + \mathbf {C} _ {(2)} ^ {2} [ \mathrm {T r} _ {3} (\rho_ {\alpha}) ]. \\ \end{array}
$$

$$
\begin{array}{l} E _ {(3)} = E _ {1 2 3} \\ = \max  \left[ \mathbf {C} _ {(3)} ^ {2} \left(\rho_ {\alpha}\right) + \mathbf {C} _ {(2)} ^ {2} \left(\rho_ {\alpha}\right), E _ {(2)} \right] - \left\{\mathbf {C} _ {(2)} ^ {2} \left[ \operatorname {T r} _ {1} \left(\rho_ {\alpha}\right) \right. \right] \\ + \mathbf {C} _ {(2)} ^ {2} [ \operatorname {T r} _ {2} (\rho_ {\alpha}) ] + \mathbf {C} _ {(2)} ^ {2} [ \operatorname {T r} _ {3} (\rho_ {\alpha}) ] \}. \tag {30} \\ \end{array}
$$

It is clear that the sum is unchanged because we add the sum of the 2-flip concurrence of the reduced density matrices and subtract it. As the 2-flip concurrence of the subsystems are here equivalent to two times the Wootters-Hill concurrence [21] this sum is clearly invariant under local unitaries. The physical motivation for this correction is that the information available in entanglement of any bipartite subsystem for any experiment is given by ignoring all the other subsystems and then calculating its entanglement.

Note that the reduced density matrices are in general mixed and therefore the expression  $\mathbf{C}_{(2)}^{2}$  includes the convex roof calculation. In our example we have only bipartite qubits, thus the convex roof is known to be equivalent to the bound, Eq. (25), of the 2-flip operators [21]. If the 3-qubit case is mixed, then in general the bounds are not exact.

With these definitions of the 2- and 3-partite entanglement we obtain a simple interpretation of the physical difference of the W and the GHZ entanglement. The state  $\rho_{\alpha}$ , Eq. (28), is for  $\alpha = 0$  separable; the single property in each subsystem is maximal (see also Fig. 2). As  $\alpha$  increases the single properties  $I(\rho_{\alpha}) = \Sigma_{s=1}^{3} S_{s}^{2}$  have to decrease due to Bohr's complementary relation  $(S_{s}^{2} + M_{s}^{2} = 1)$  as their mixednesses increase. For  $\alpha = \frac{\pi}{3}$  or  $\alpha = \frac{2\pi}{3}$  the single properties are zero, thus entanglement is maximal and it is a genuine 3-partite entangled state, the GHZ state. For  $\alpha = \frac{\pi}{2}$  the 2-partite entanglement is maximal, while the single properties obtain a local maximal and the 3-partite entanglement is zero as desired. There is another interesting state, e.g., at  $\alpha = \frac{\pi}{6} / \frac{5\pi}{6}$ ; here 2-partite entanglement has another maximum (see Fig. 2).

Also the above counterexample of a biseparable state, Eq. (26), obtains the desired interpretation as the 3-partite entanglement  $E_{(3)}$  derives to zero and the 2-partite entanglement to  $E_{(2)} = E_{12} + E_{13} + E_{23} = 2 + 0 + 0$ ; see also Fig. 1.

In Fig. 3 we show the superposition of W and GHZ:

$$
\tau_ {\alpha} = | \psi (\alpha) \rangle \langle \psi (\alpha) |,
$$

$$
\left| \psi (\alpha) \right\rangle = \frac {\sin \alpha}{\sqrt {3}} \left\{\left| 0 0 1 \right\rangle + \left| 0 1 0 \right\rangle + \left| 1 0 0 \right\rangle \right\} + \frac {\cos \alpha}{\sqrt {2}} \left\{\left| 1 1 1 \right\rangle + \left| 0 0 0 \right\rangle \right\}. \tag {31}
$$

The single properties are symmetric; however, the tripartite and the bipartite entanglement depend on the particular superposition. One finds, for example, another interesting state at  $(\alpha = \simeq 0.8\pi)$  which maximizes the bipartite entanglement

![](images/8d086ae880ebc77cfec43f491a2476a80160c8c71e099dc7f1a49b36e51332af.jpg)  
FIG. 3. (Color online) Here the information content in bits of the state  $\tau_{\alpha}$ , Eq. (31), is plotted. The colored, thickened, and dashed curves are the single properties  $I = \sum_{s=1}^{3} S_{s}$  (blue), the 2-partite entanglement  $E_{(2)} = E_{12} + E_{13} + E_{23}$  (green), and the 3-partite entanglement  $E_{(3)} = E_{123}$  (red). The single properties  $I$  are symmetric, however, the genuine 2- and 3-partite entanglements are not.

$E_{(2)}$  while the tripartite entanglement  $E_{(3)}$  is zero (see Fig. 3).

For mixed states, if the optimal bounds are known, the  $m$  entanglement derives in the very same way. In Fig. 4 we have chosen a mixture of the GHZ state and the W state, i.e.,

$$
\sigma (\alpha) = \sin^ {2} \left(\frac {\alpha}{2}\right) \rho_ {\mathrm {W}} + \cos^ {2} \left(\frac {\alpha}{2}\right) \rho_ {\mathrm {G H Z}}. \tag {32}
$$

We checked the optimality of the bounds (25) by comparing numerically with the partial transpose criterion which is for the above state necessary and sufficient. The complementing missing information, due to classical lack of knowledge about the quantum state,  $R(\sigma(\alpha))$ , is maximal for  $\alpha = \frac{\pi}{2}$  as expected.

To sum up for 3 qubits we have shown that in a simple and evident way the 2-flip and 3-flip concurrences can be made invariant under local unitaries and these new quantities, the 2- and 3-partite entanglements, capture then the desired physical differences, e.g., of the GHZ state, the W state, the biseparable state, and mixed states.

![](images/58682cb63270ad7e3a1c9dc7dcc3dff38432cb663afe8853950af278693c174c.jpg)  
FIG. 4. (Color online) Here the information content in bits of the state  $\sigma (\alpha)$ , Eq. (32), is plotted. The colored, thickened, and dashed curves are the single properties  $I = \sum_{s = 1}^{3}S_{s}$  (blue), the 2-partite entanglement  $E_{(2)} = E_{12} + E_{13} + E_{23}$  (green), and the 3-partite entanglement  $E_{(3)} = E_{123}$  (red). The thin (not dashed) curve is  $R(\rho)$ , which is the lack of information about the state.

# VI. INFORMATION CONTENT OF  $n$ -PARTITE MULTIDIMENSIONAL SYSTEMS

Now returning to the first equation, Eq. (1), we see the separation of information in multiqudit systems:  $I(\rho)$  quantifies all locally obtainable information as it is just the sum over all obtainable information in every subsystem. Every physical system with  $d$ -degrees of freedom can carry one dit of information, which can be separated into predictability and coherence. Of course the combination of  $n$  systems can carry  $n$  dit of information, just as in classical systems. The main difference then is that they cannot all be locally obtained, as for pure entangled systems the sum over all locally obtainable information does not yield  $n$ . Here the information is encoded in entanglement, which in itself seems to be separable into different classes of entanglement, as we have seen for the three qubit example. Note that the local information  $I(\rho)$  is always additive and for the entanglement  $E(\rho)$  strict additivity is only proven for pure states. For mixed systems only subadditivity of  $E(\rho)$  can be proven (in the very same way as with entanglement of formation), but additivity is strongly expected [in this case  $R(\rho)$  can clearly only contain classical uncertainty].

# VII. CONCLUSION

We started from Bohr's complementarity relation, which we generalized for  $d$ -dimensional systems, yielding the information content in every subsystem of a multipartite state  $\rho$  through the single property  $\mathcal{S}_s(\rho)$ . From this relation we are able to consistently quantify the information content in entanglement of pure  $n$ -partite states as the missing information

needed to complement the single properties of all subsystems as  $n - \Sigma_{s = 1}^{n}\mathcal{S}_{s}^{2}(\rho) = \Sigma_{s = 1}^{n}M_{s}^{2}(\rho)$ .

Then we showed that this entanglement measure can be operationally obtained if  $M_s^2(\rho)$  is chosen as the linear entropy, i.e., we found that by applying the flip operator  $2,3,\ldots,n$  times  $m$ -flip concurrences can be defined. In the case of mixed states this has the advantage that for these  $m$ -flip concurrences bounds can be derived, i.e., the measure gets computable.

Finally, we showed for three qubits that these sums of  $m$ -flip concurrences can be modified to meet our understanding of multipartite entanglement. This means that one can correct the  $m$ -flip concurrences to  $m$ -partite entanglement. This explains the different kind of entanglement of the GHZ state and the W state, summarized in Figs. 1 and 2. Moreover, it gives the correct entanglement of any biseparable state. Last but not least we presented a mixed state, where the single properties are complemented by the classical lack of knowledge about the quantum state under investigation. In what way this generalizes for multipartite systems consistently is left for further investigation.

In summary, we found a multidimensional, multipartite, and operational entanglement measure which admits a separation into different classes of entanglement and herewith we obtain the information content of any discrete state. This knowledge obviously helps to, e.g., decide given a certain state if quantum communication or quantum cryptography is possible and to what extent.

# ACKNOWLEDGMENT

The authors thank R.A. Bertlmann and Ph. Krammer for enlightening discussions.

[1] N. Linden, S. Popescu, B. Schumacher, and M. Westmoreland, e-print arXiv:quant-ph/9912039.  
[2] H. Aschauer, W. Dur, and H.-J. Briegel, Phys. Rev. A 71, 012319 (2005).  
[3] W. Dur, H. Aschauer, and H.-J. Briegel, Phys. Rev. Lett. 91, 107903 (2003).  
[4] J. Eisert and H.-J. Briegel, Phys. Rev. A 64, 022306 (2001).  
[5] A. Borras, A. R. Plastino, J. Batle, C. Zander, M. Casas, and A. Plastino, J. Phys. A 40, 13407 (2007).  
[6] Jian-Ming Cai, Zheng-Wei Zhou, and Guang-Can Guo, e-print arXiv:quant-ph/0609186.  
[7] David A. Meyer and Nolan R. Wallach, e-print arXiv:quant-ph/0108104v1.  
[8] S. Boixo and A. Monras, Phys. Rev. Lett. 100, 100503 (2008).  
[9] Ryszard Horodecki, Pawel Horodecki, Michal Horodecki, and Karol Horodecki, e-print arXiv:quant-ph/0702225v2.  
[10] D. Bruss, G. M. D'Ariano, M. Lewenstein, C. Macchiavello, A. Sen(De), and U. Sen, e-print arXiv:quant-ph/0507146.  
[11] H. Haeffner, W. Haensel, C. F. Roos, J. Benhelm, D. Chek-alkar, M. Chwalla, T. Koerber, U. D. Rapol, M. Riebe, P. O. Schmidt, C. Becher, O. Ghne, W. Dur, and R. Blatt, Nature

(London) 438, 643 (2005).  
[12] Almut Beige, Yuan Liang Lim, and Christian Schoen, J. Mod. Opt. 54, 397 (2007).  
[13] D. Greenberger and A. Yasin, Phys. Lett. A 128, 391 (1988).  
[14] B.-G. Englert, Phys. Rev. Lett. 77, 2154 (1996).  
[15] B. C. Hiesmayr and M. Huber, Phys. Lett. A 372, 3608 (2008).  
[16] A. Bramon, G. Garbarino, and B. C. Hiesmayr, Phys. Rev. A 69, 022112 (2004).  
[17] B. C. Hiesmayr and V. Vedral, e-print arXiv:quant-ph/0501015.  
[18] M. Jakob and J. A. Bergou, Phys. Rev. A 76, 052107 (2007).  
[19] M. Jakob and J. A. Bergou, e-print arXiv:quant-ph/0302075.  
[20] C. H. Bennett, D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters, Phys. Rev. A 54, 3824 (1996).  
[21] S. Hill and W. K. Wootters, Phys. Rev. Lett. 78, 5022 (1997).  
[22] F. Mintert, A. R. R. Carvalho, M. Kus, and A. Buchleitner, Phys. Rep. 415, 207 (2005).  
[23] R. Demkowicz-Dobrzanski, A. Buchleitner, M. Kus, and F. Mintert, Phys. Rev. A 74, 052303 (2006).