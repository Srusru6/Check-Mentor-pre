# Graphical calculus for Gaussian pure states

Nicolas C. Menicucci, $^{1,*}$  Steven T. Flammia, $^{1}$  and Peter van Loock $^{2,3}$

<sup>1</sup>Perimeter Institute for Theoretical Physics, Waterloo, Ontario N2L 2Y5, Canada

$^{2}$ Optical Quantum Information Theory Group, Max Planck Institute for the Science of Light, Günther-Scharowsky-Str. 1, Building 26, D-91058 Erlangen, Germany

$^{3}$ Institute of Theoretical Physics I, Universität Erlangen-Nürnberg, Staudtstr. 7/B2, D-91058 Erlangen, Germany (Received 6 July 2010; published 28 April 2011)

We provide a unified graphical calculus for all Gaussian pure states, including graph transformation rules for all local and semilocal Gaussian unitary operations, as well as local quadrature measurements. We then use this graphical calculus to analyze continuous-variable (CV) cluster states, the essential resource for one-way quantum computing with CV systems. Current graphical approaches to CV cluster states are only valid in the unphysical limit of infinite squeezing, and the associated graph transformation rules only apply when the initial and final states are of this form. Our formalism applies to all Gaussian pure states and subsumes these rules in a natural way. In addition, the term "CV graph state" currently has several inequivalent definitions in use. Using this formalism we provide a single unifying definition that encompasses all of them. We provide many examples of how the formalism may be used in the context of CV cluster states: defining the "closest" CV cluster state to a given Gaussian pure state and quantifying the error in the approximation due to finite squeezing; analyzing the optimality of certain methods of generating CV cluster states; drawing connections between this graphical formalism and bosonic Hamiltonians with Gaussian ground states, including those useful for CV one-way quantum computing; and deriving a graphical measure of bipartite entanglement for certain classes of CV cluster states. We mention other possible applications of this formalism and conclude with a brief note on fault tolerance in CV one-way quantum computing.

DOI: 10.1103/PhysRevA.83.042335

PACS number(s): 03.67.-a, 02.10.Ox, 03.65.Ca

# I. INTRODUCTION

The invention of one-way quantum computing (QC) [1] launched an intensive research effort into this new method of QC that eliminates unitary evolution and relies solely on adaptive measurements on a highly entangled state of many qubits called a cluster state [2]. Concurrently, other work was under way generalizing qubit-based QC to QC using continuous-variable (CV) systems [3]. The two paths merged with the invention of CV cluster states [4], which were shortly thereafter shown to be capable of serving as the entangled resource in the CV version of one-way QC [5,6].

Initially, CV cluster states and the platform of one-way QC making use of them were not believed to be a promising contender for scalable QC [5]. It was, however, believed that CV cluster states would be convenient for demonstrating the basic principles of one-way QC since generating such states in the optical context was easier than making ordinary cluster states from optical qubits [7,8]. The main reason for this belief was that CV cluster states could be generated deterministically, while getting single photons to interact required nondeterministic gates whose (heralded) failure happens a large fraction of the time [9]. Nevertheless, ideal CV cluster states are not achievable since they are singular states (i.e., infinitely squeezed) and thus have an infinite average photon number and infinite energy. Approximate states must therefore be used instead, necessarily leading to errors in any CV one-way QC protocol [6,10] (we say more about fault tolerance in Sec. V). The most natural choice for these approximate states would be multimode squeezed states, but the originally proposed

method of making them [5] involved experimentally arduous inline squeezing operations [11-13]. This limited the expected usefulness of the technology.

Shortly after the invention of CV one-way QC, it was shown that inline squeezing was not required at all and that CV cluster states could be generated optically using offline squeezing plus interferometry [14]. This method involves preparing one single-mode squeezed vacuum state per node of the cluster and sending these states through an appropriately designed network of beamsplitters. In fact, this method can be used to make any Gaussian state at all [15]. This represented a vast simplification for experiments, which quickly demonstrated the viability of this method of generating CV cluster states and their usefulness for simple CV quantum information processing tasks [16-20].

Concurrent with this work was a separate initiative to generate optical CV cluster states in a single-shot, top-down fashion using just a single optical parametric oscillator (OPO) consisting of a nonlinear crystal within an optical cavity [21]. In this implementation, independent modes are not separated in space (as in previous optical proposals) but are instead taken to be the different frequencies within a single beam. The initial proposal showed that a single OPO and appropriately designed multifrequency pump beam could, in principle, generate any approximate CV cluster state with a bipartite graph, $^{1}$  which includes the universal family of square-lattice graphs. Further

work revealed that this method could generate a multitude of small CV cluster states [22] or a universal family of CV cluster states [23,24], using a method that has excellent scaling potential up to a few thousand optical modes with the currently available technology [25-28].

Yet another method [29] reintroduces the experimentally challenging  $C_Z$  gate. But in this case, only one such gate is needed because the modes are encoded temporally, each traversing the same optical path (but at different times) and each passing multiple times through the same optical hardware implementing the  $C_Z$  gate. This method has the additional advantage that the cluster state is extended as needed—simultaneously with measurements implementing an algorithm on it—in a manner analogous to repeatedly laying down additional track in front of a moving train car (a "Wallace and Gromit" approach; see footnote in Ref. [29]). Such a method eliminates the need for long-time coherence of a large cluster state because only a small piece of the state exists at any given time.

While every CV cluster state—regardless of how it is made—can be represented by a graph [6], the single-OPO generation method revealed another type of graph that is useful for describing Gaussian pure states [30]. This graph indicates the strength and pairings of the two-mode squeezing interactions that act within the OPO, and its adjacency matrix defines the interaction Hamiltonian directly. Thus, we call these graphs Hamiltonian graphs [21–24,31], or  $\mathcal{H}$  graphs. Despite this natural way of representing the Hamiltonian interactions by graphs, the resulting states are not "CV graph states" in the sense of a CV cluster state with the same graph as the  $\mathcal{H}$  graph, although they can be interpreted as CV cluster states with (in general) a different graph [21]. This creates an ambiguity in the meaning of a "CV graph state."

Independently of this work, Zhang showed that ideal CV cluster states admit graph transformation rules that correspond to local Gaussian (LG) operations mapping them to other ideal CV cluster states [32]. These rules bear some similarity to the corresponding rules for qubit cluster states [33,34] but they are not exactly equivalent. (Related work has also been done for qubit stabilizer states and local Clifford transformations [35-38].) Further revisions showed that ideal CV cluster states with weighted graphs were necessary for a more complete understanding of the graph transformation rules [39]—a consequence of the continuity of the quantum variables in question, as opposed to the binary nature of qubits, whose graphs are necessarily unweighted. The effect

in the present context, where "CV graph state" could have three different meanings (CV cluster state,  $\mathcal{H}$ -graph state, and general Gaussian pure state), this convention also serves a clarifying function.  
2In Ref. [21] the term "two-mode-squeezing graph" was used instead of  $\mathcal{H}$  graph. These terms are synonymous, and only the latter is used in this paper.  
3 Weighted graph states for qubits have been defined [40] but they are not stabilizer states. When dealing with CVs, however, weighted graphs occur naturally because the entangling operation that makes a CV cluster state necessarily has a strength (which can be—but need not be—chosen equal for all interactions). This strength becomes the weight for the corresponding edge in the graph. Unlike their similarly

of quadrature measurements, which can be used to implement any Gaussian operation in CV one-way QC [6,41], has recently been incorporated into the formalism, as well [42].

This original graphical calculus, while useful for demonstrating LG equivalence of CV cluster states, has several limitations. First, for the weighted as well as for the unweighted case, only ideal (i.e., infinitely squeezed) CV cluster states can be represented. As mentioned before, these states are not physical. Neither their approximating Gaussian states nor any other Gaussian state can be represented in the formalism. Second, there are many Gaussian operations (e.g., the very common Fourier transform) that do not map CV cluster states to other CV cluster states and thus cannot be represented as a graph transformation. Third, no connection is made with  $\mathcal{H}$  graphs; the rules apply only to CV cluster-state graphs. Nonetheless, Zhang's formalism is exciting because it promises an intuitive visual way of manipulating CV cluster states, paralleling similar tools for qubit cluster states [33,34].

In this paper we generalize these rules in a consistent fashion to cover all Gaussian pure states, including approximate CV cluster states. This includes physical states generated by the action of a Hamiltonian with an associated  $\mathcal{H}$  graph. Because the details of a Gaussian pure state are displayed in its graphical representation (and represented uniquely within it), this formalism can be used to quantify the deviations from ideality for any approximate CV cluster state. Furthermore, the formalism can also be used to identify the "closest" CV cluster state to any given Gaussian pure state, and it is useful when considering physical systems whose ground states would be useful for CV one-way QC [43]. We also make connections with a measure of bipartite entanglement in Gaussian pure states. In certain cases, this admits a simple graphical rule.

In what follows, we shall (i) define the unique graph associated with any Gaussian pure state; (ii) derive the transformation rules for all Gaussian unitary operations; (iii) illustrate the effect of LG unitary operations in graphical form, showing that they faithfully generalize Zhang's rules [39,42]; (iv) illustrate the connection of this formalism to approximate CV cluster state generation via an  $\mathcal{H}$ -graph Hamiltonian; and (v) provide several applications of the formalism to analysis of physical states and the  $\mathcal{H}$ -graph generation method, as well as Hamiltonian ground states and bipartite entanglement. The connection with  $\mathcal{H}$  graphs answers an important question about the method proposed in Refs. [21-24]—namely, what happens when the method is used on physical states. Previous connections between  $\mathcal{H}$  graphs and CV cluster-state graphs have only been rigorously made in the unphysical limit of infinite squeezing. This formalism allows the important effects of finite squeezing to be properly accounted for while remaining entirely within the intuitive framework of the graphical representation.

The mathematics behind this formalism is the complex matrix formalism for representing and manipulating Gaussian pure states [44]. When we interpret these matrices as adjacency matrices for complex-weighted graphs, transformations using

the symplectic representation can also be interpreted in graph-theoretic terms. In this formalism, real-weighted graphs, representing idealized, unphysical, infinitely squeezed Gaussian states [32,39,42], are generalized to complex-weighted graphs that uniquely specify realistic, physical, finitely squeezed Gaussian pure states. This extension includes generalizing the real-valued graph-state nullifiers for ideal CV cluster states [6] to complex-valued nullifiers for physical CV cluster states. These results are closely related to the stabilizer formalism for Gaussian pure states, which, though utilized to some extent for a proof of the CV version of the Gottesman-Knill theorem [45] and often mentioned as a straightforward generalization from finite-dimensional systems [46], has not been fully explored yet. While we are building on existing mathematics, what this work shows—beyond the straightforward graph-theoretic interpretation of that mathematics—is its natural connection to CV cluster states, plus all of the examples, applications, and avenues for future work that open up as a result. We have more to say about the context and importance of our work in Sec. V.

# II. GAUSSIAN PURE STATES AND COMPLEX-WEIGHTED GRAPHS

# A. CV cluster states

The motivation for a graphical study of Gaussian pure states begins with CV cluster states [4-6]. In the ideal case, CV cluster states are prepared beginning with a collection of  $N$  zero-momentum eigenstates, which we write as  $|0\rangle_p^{\otimes N}$ , where the  $p$ -subscripted kets satisfy  $\hat{p} |s\rangle_p = s|s\rangle_p$ . These states are then entangled via a collection of controlled- $Z$  operations, denoted  $\hat{\mathbf{C}}_Z = \exp (ig\hat{q}\otimes \hat{q})$ , where the real number  $g$  is the strength of the interaction. Since all  $\mathbf{C}_Z$  operations commute, they can be performed in any order (or simultaneously), which leads naturally to the use of graphs as recipes for generating particular CV cluster states. An example of such a graph—and the CV cluster-state recipe it encodes—is illustrated in Fig. 1. Each node represents a zero-momentum eigenstate, and edges indicate a  $\mathbf{C}_Z$  operation to be performed between the two connected nodes. The strength  $g$  of the interaction is indicated by the label, or weight, of the associated edge. As such, weighted graphs with real-valued weights are the natural language for depicting ideal CV cluster states.

Labeling the nodes of the graph in some arbitrary order, we can define a symmetric adjacency matrix  $\mathbf{A} = \mathbf{A}^{\mathrm{T}}$  whose  $(j,k)$ th entry  $A_{jk}$  is equal to the weight of the edge linking node  $j$  to node  $k$  (with no edge corresponding to a weight of 0). Since a graph is uniquely specified (up to isomorphism) by its adjacency matrix, we often omit the distinction between the two and refer unambiguously to "graph A." The collection of controlled-  $Z$  operations used to make the CV cluster state is now a function of  $\mathbf{A}$ , denoted  $\hat{\mathbf{C}}_Z[\mathbf{A}]$ . The CV cluster state associated with graph A is then

$$
\begin{array}{l} | \psi_ {\mathbf {A}} \rangle = \hat {\mathrm {C}} _ {Z} [ \mathbf {A} ] | 0 \rangle_ {p} ^ {\otimes N} \\ = \prod_ {j, k = 1} ^ {N} \exp \left(\frac {i}{2} A _ {j k} \hat {q} _ {j} \hat {q} _ {k}\right) | 0 \rangle_ {p} ^ {\otimes N} \\ = \exp \left(\frac {i}{2} \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {A} \hat {\mathbf {q}}\right) | 0 \rangle_ {p} ^ {\otimes N}, \tag {2.1} \\ \end{array}
$$

![](images/7fb587a7c3946efcbeae5999a9b5e83275bfbf8228dfe1245bfb39c2b8f45838.jpg)  
FIG. 1. (Color online) Original formulation of weighted graphs for ideal CV cluster states. Ideal CV cluster states are represented by undirected graphs with real-weighted edges [4-6,14,21-24]. (Unweighted graphs are a special case with all weights equal to 1.) Each graph uniquely defines a recipe (i.e., a quantum circuit) for creating a CV cluster state, as illustrated: (1) each node represents a state that is infinitely squeezed in the  $\hat{p}$  quadrature  $|0\rangle_p$ ; and (2)  $C_Z$  gates are applied between modes in accordance with the graph, with the weight  $g$  of an edge corresponding to the strength of the interaction  $\hat{C}_Z(g) = e^{ig\hat{q}\otimes \hat{q}}$  between the two nodes connected. These states are unphysical because they cannot be normalized. Instead they are approximated in physical applications by very highly squeezed states.

where  $\hat{\mathbf{q}} = (\hat{q}_1, \dots, \hat{q}_N)^{\mathrm{T}}$  is a column vector of Schrödinger-picture position operators. The factor of 2 is necessary because each edge weight appears twice in the sum (as  $A_{jk}$  and as  $A_{kj}$ ).

Ideal CV cluster states satisfy a set of nullifier relations [6,21], which can be written concisely as

$$
(\hat {\mathbf {p}} - \mathbf {A} \hat {\mathbf {q}}) | \psi_ {\mathbf {A}} \rangle = \mathbf {0}, \tag {2.2}
$$

where  $\hat{\mathbf{p}} = (\hat{p}_1, \dots, \hat{p}_N)^{\mathrm{T}}$  is a column vector of Schrödinger-picture momentum operators. This equation actually represents  $N$  independent equations, one for each component of the vector  $(\hat{\mathbf{p}} - \mathbf{A}\hat{\mathbf{q}})$ , which are called nullifiers for the state  $|\psi_{\mathbf{A}}\rangle$  because that state is a simultaneous zero eigenstate of them (and of any linear combination of them).

These ideal CV cluster states admit a convenient graphical representation in terms of the adjacency matrix  $\mathbf{A}$ . Some LG unitary operations [39] and quadrature measurements [42] can be represented as convenient graphical update rules. As discussed in Sec. I, this graphical formalism is elegant and intuitive but also has several limitations—most notably, the restriction to ideal (and hence unphysical) CV cluster states and to a subset of all LG unitaries (those that map ideal CV cluster states to other ideal CV cluster states).

Approximate CV cluster states are those for which measurements of each nullifier give values that are close to 0. Quantifying this, we would say that an approximate CV cluster state is any member of a family of Gaussian pure states, indexed by an overall squeezing parameter  $\alpha$ , for which

$$
\lim  _ {\alpha \rightarrow \infty} \operatorname {c o v} (\hat {\mathbf {p}} - \mathbf {A} \hat {\mathbf {q}}) = \mathbf {0}, \tag {2.3}
$$

where the covariance matrix of a vector of operators has components defined as the symmetrized expectation value

$$
\left(\operatorname {c o v} \hat {\mathbf {r}}\right) _ {j k} := \frac {1}{2} \left\langle \left\{\hat {r} _ {j} ^ {\dagger}, \hat {r} _ {k} \right\} \right\rangle , \tag {2.4}
$$

with the expectation taken over the state of interest—in this case, the  $\alpha$ -indexed approximate CV cluster state  $|\psi_{\mathbf{A}}(\alpha)\rangle$ . (Notice that this definition assumes that the state has zero

mean.) The limit in Eq. (2.3) is defined component-wise for all entries in the covariance matrix, but because the matrix is positive definite, it is sufficient to require that the relation holds only for the diagonal elements:

$$
\lim  _ {\alpha \rightarrow \infty} \left\langle \right. \psi_ {\mathbf {A}} (\alpha) \left. \right|\left(\hat {p} _ {j} - \sum_ {k} A _ {j k} \hat {q} _ {k}\right) ^ {2} | \psi_ {\mathbf {A}} (\alpha) \rangle = 0 \quad \forall j. \tag {2.5}
$$

Any  $\alpha$ -indexed family of Gaussian pure states  $\{|\psi_{\mathbf{A}}(\alpha)\}$  satisfying Eq. (2.3) [or Eq. (2.5)] defines a family of approximate CV cluster states with graph  $\mathbf{A}$ . We would like these Gaussian pure states to be representable directly in a graphical formalism in a manner that takes into account their unique deviation from ideality.

In addition to this, there are plenty of other useful Gaussian pure states that are not approximate CV cluster states at all. For instance, a two-mode squeezed state satisfies

$$
\operatorname {v a r} \left(\hat {q} _ {1} - \hat {q} _ {2}\right) = e ^ {- 2 \alpha}, \tag {2.6}
$$

$$
\operatorname {v a r} \left(\hat {p} _ {1} + \hat {p} _ {2}\right) = e ^ {- 2 \alpha}.
$$

Such states are readily made in the laboratory by passage of position-squeezed and momentum-squeezed beams through a 50:50 beamsplitter [3,47,48] or directly by nondegenerate parametric downconversion [3,49-52]. Despite being an  $\alpha$ -indexed family of multimode squeezed states whose variances tend to 0 as  $\alpha \rightarrow \infty$ , these states do not satisfy Eq. (2.3) for any choice of (finitely weighted) graph  $\mathbf{A}$ , which means they cannot be represented within the existing graphical formalism for CV cluster states [39]—even in the limiting case where  $\alpha \rightarrow \infty$ . This is unfortunate since the two-mode squeezed state is related to a two-mode CV cluster state by a Fourier transform on one of the modes—an LG unitary [21] that is one of the simplest to perform experimentally. That this equivalence cannot be represented in the graphical formalism—in either the ideal or the approximate case—is a significant drawback. Our formalism addresses all these concerns.

# B. Desired properties of the graphical calculus

In our attempt to generalize the formalism in Refs. [39] and [42], we desire a unified graphical calculus that has the following properties:

(1) All Gaussian pure states can be represented uniquely, up to phase-space displacements, as graphs.  
(2) All Gaussian unitaries—local or otherwise—can be represented uniquely, up to phase-space displacements, as graph transformations.  
(3) All local projective measurements of quadrature operators can be represented uniquely, up to phase-space displacements, as graph transformations.  
(4) The representation of a family of approximate CV cluster states faithfully limits to the standard graph representation of the associated ideal CV cluster state in the limit of large squeezing.  
(5) The representation of LG unitaries and projective measurements of quadrature operators acting on a family of approximate CV cluster states faithfully reproduces Zhang's rules [39,42] in the limit of large squeezing.

In addition to these requirements, we would also like the graphical calculus to be useful for the following purposes:

(i) Visualize the entanglement structure of a Gaussian pure state.  
(ii) Consider finite squeezing effects within the graphical formalism, including their effect on one-way QC using an approximate CV cluster state.  
(iii) Make a connection with  $\mathcal{H}$  graphs and their usefulness in generating CV cluster states [21-23], including possible graph transformation rules between the two types of graphs.

This is not meant to be an exhaustive list. We expect that other uses will present themselves as the formalism gets applied to actual calculations.

# C. Symplectic representation of Gaussian pure states

In the present and the following subsection, we review the complex-matrix formalism [44] for representing Gaussian pure states and their transformations among each other, adapt it to our notation, and recast it for our purposes.

It is well known that all  $N$ -mode Gaussian pure states can be created by acting on the ground state of  $N$  harmonic oscillator with a unitary operation whose Heisenberg action on the vector of quadrature operators is a symplectic transformation, followed by a phase-space displacement. These are sometimes called linear unitary Bogoliubov (LUBO) transformations [3], but we do not use this term. Furthermore, we neglect the phase-space displacement altogether since we only desire that our graphical formalism describe the noise properties of the state, which do not depend on overall displacement.

Stacking  $\hat{\mathbf{q}}$  on top of  $\hat{\mathbf{p}}$  to form a column vector called  $\hat{\mathbf{x}} = \binom{\hat{\mathbf{q}}}{\hat{\mathbf{p}}}$ , the Heisenberg action of a Gaussian unitary operation  $\hat{U}$  takes the form

$$
\hat {\mathbf {x}} ^ {\prime} = \hat {U} ^ {\dagger} \hat {\mathbf {x}} \hat {U} = \mathbf {S} \hat {\mathbf {x}}, \tag {2.7}
$$

where  $\mathbf{S}$  is a symplectic matrix of  $c$  numbers that acts via matrix multiplication on  $\hat{\mathbf{x}}$  as a vector, while  $\hat{U}$  is a unitary operator that acts on the individual operators within  $\hat{\mathbf{x}}$ . Specifically,

$$
\hat {x} _ {j} ^ {\prime} = \hat {U} ^ {\dagger} \hat {x} _ {j} \hat {U} = \sum_ {k = 1} ^ {2 N} S _ {j k} \hat {x} _ {k}. \tag {2.8}
$$

Notice that in general there would be a phase-space displacement term, which would give  $\hat{\mathbf{x}}' = \mathbf{S}\hat{\mathbf{x}} + \mathbf{y}$ , but we are neglecting this. There is a unique  $\mathbf{S}$  for every Gaussian  $\hat{U}$ , and there is a unique  $\hat{U}$  (up to an overall phase) for every symplectic  $\mathbf{S}$ . This correspondence can be chosen to faithfully preserve composition and map the identity operator  $\hat{I}$  to the identity matrix  $\mathbf{I}$ , thus giving a symplectic representation of the Gaussian unitary group [53].

The symplectic nature of  $\mathbf{S}$  is guaranteed because the commutation relations must be preserved, giving rise to a symplectic form  $\pmb{\Omega}$  to be preserved by the Heisenberg matrix action. The explicit form of  $\pmb{\Omega}$  may be deduced by writing out the commutation relations for  $\hat{\mathbf{x}}$  and requiring them to be unchanged under the Gaussian unitary operation. The

canonical commutation relations  $[\hat{q}_j,\hat{p}_k] = i\delta_{jk}$  (with  $\hbar = 1$  can be written succinctly as

$$
[ \hat {\mathbf {x}}, \hat {\mathbf {x}} ^ {\mathrm {T}} ] = i \left( \begin{array}{c c} \mathbf {0} & \mathbf {I} \\ - \mathbf {I} & \mathbf {0} \end{array} \right) =: i \boldsymbol {\Omega}, \tag {2.9}
$$

where the commutator of two operator-valued vectors is defined as

$$
[ \hat {\mathbf {r}}, \hat {\mathbf {s}} ^ {\mathrm {T}} ] := \hat {\mathbf {r}} \hat {\mathbf {s}} ^ {\mathrm {T}} - (\hat {\mathbf {s}} \hat {\mathbf {r}} ^ {\mathrm {T}}) ^ {\mathrm {T}}. \tag {2.10}
$$

Note that the transpose operation acts only on the entries in the matrix (or vector), leaving the actual operators involved alone.4 Requiring that the quadrature-operator commutators remain unchanged after the Gaussian operation gives

$$
i \boldsymbol {\Omega} = [ \hat {\mathbf {x}} ^ {\prime}, \hat {\mathbf {x}} ^ {\mathrm {T}} ] = [ \mathbf {S} \hat {\mathbf {x}}, (\mathbf {S} \hat {\mathbf {x}}) ^ {\mathrm {T}} ] = \mathbf {S} [ \hat {\mathbf {x}}, \hat {\mathbf {x}} ^ {\mathrm {T}} ] \mathbf {S} ^ {\mathrm {T}} = i \mathbf {S} \boldsymbol {\Omega} \mathbf {S} ^ {\mathrm {T}}. \tag {2.11}
$$

Noting that the  $i$ 's cancel, this equation is exactly the defining relation for any  $2N \times 2N$  square matrix  $\mathbf{S}$  to be a symplectic matrix with symplectic form  $\Omega$ . The symplectic nature of  $\mathbf{S}$  is therefore guaranteed and required by the need to preserve the canonical commutation relations, which themselves play the role of the symplectic form  $\Omega$  (up to an overall factor of  $i$ ), as shown in Eq. (2.9).

A Gaussian pure state (with zero mean) is uniquely specified by its covariance matrix. We write the symmetrized covariance matrix for an operator-valued vector as

$$
\operatorname {c o v} \hat {\mathbf {r}} = \frac {1}{2} \langle \{\hat {\mathbf {r}} ^ {\dagger}, \hat {\mathbf {r}} ^ {\mathrm {T}} \} \rangle , \tag {2.12}
$$

which accords with Eq. (2.4) if we define the anticommutator product as

$$
\left\{\hat {\mathbf {r}}, \hat {\mathbf {s}} ^ {\mathrm {T}} \right\} := \hat {\mathbf {r}} \hat {\mathbf {s}} ^ {\mathrm {T}} + \left(\hat {\mathbf {s}} \hat {\mathbf {f}} ^ {\mathrm {T}}\right) ^ {\mathrm {T}}, \tag {2.13}
$$

which is analogous to Eq. (2.10), and if we require that Hermitian conjugation (indicated by the superscript dagger)

4Note on notational conventions. Because we are dealing with operator-valued matrices (or vectors in this case), the transpose operation must be carefully defined. In fact, we define it in a natural way to simply exchange the indices of an operator-valued matrix  $\left[(\hat{\mathbf{A}}^{\mathrm{T}})_{jk} = (\hat{\mathbf{A}})_{kj}\right]$  and leave the entries themselves alone. That is, each entry in the matrix—which is itself an operator—does not get a transpose applied to it. It is then no longer the case that matrix transposition follows the usual distributive rule, i.e.,  $(\hat{\mathbf{A}}\hat{\mathbf{B}})^{\mathrm{T}}\neq \hat{\mathbf{B}}^{\mathrm{T}}\hat{\mathbf{A}}^{\mathrm{T}}$  because the operators end up in the wrong order. Rather than being a problem, we can use this feature to define the commutator-product of the two operator-valued column vectors  $\hat{\mathbf{r}}$  and  $\hat{\mathbf{s}}$  as in Eq. (2.10). This has the desired property of forming a matrix whose entries are the commutators in question:

$$
{(\left[ \hat {\mathbf {r}}, \hat {\mathbf {s}} ^ {\mathrm {T}} \right]) _ {j k} = \hat {r} _ {j} \hat {s} _ {k} - \hat {s} _ {k} \hat {r} _ {j} = [ \hat {r} _ {j}, \hat {s} _ {k} ].}
$$

This is how Eq. (2.9) should be interpreted. Also, note that  $c$ -number matrices acting on the vectors within the commutator factor out:

$$
\begin{array}{l} [ \mathbf {A} \hat {\mathbf {r}}, (\mathbf {B} \hat {\mathbf {s}}) ^ {\mathrm {T}} ] = \mathbf {A} \hat {\mathbf {r}} \hat {\mathbf {s}} ^ {\mathrm {T}} \mathbf {B} ^ {\mathrm {T}} - (\mathbf {B} \hat {\mathbf {s}} \hat {\mathbf {r}} ^ {\mathrm {T}} \mathbf {A} ^ {\mathrm {T}}) ^ {\mathrm {T}} \\ = \mathbf {A} \hat {\mathbf {r}} \hat {\mathbf {s}} ^ {\mathrm {T}} \mathbf {B} ^ {\mathrm {T}} - \mathbf {A} (\hat {\mathbf {s}} \hat {\mathbf {r}} ^ {\mathrm {T}}) ^ {\mathrm {T}} \mathbf {B} ^ {\mathrm {T}} = \mathbf {A} [ \hat {\mathbf {r}}, \hat {\mathbf {s}} ^ {\mathrm {T}} ] \mathbf {B} ^ {\mathrm {T}}. \\ \end{array}
$$

The usefulness here stems from the ability to "vectorize" expressions using operators in a natural way. This will be useful in what follows.

apply only to the operators within the vector, without transposing the vector itself. We use the superscript H notation to indicate transposition of the vector and conjugation of its entries:

$$
\hat {\mathbf {r}} ^ {\mathrm {H}} := \left(\hat {\mathbf {r}} ^ {\dagger}\right) ^ {\mathrm {T}} = \left(\hat {\mathbf {r}} ^ {\mathrm {T}}\right) ^ {\dagger}. \tag {2.14}
$$

These caveats are unimportant for our current purposes because  $\hat{\mathbf{x}} = \hat{\mathbf{x}}^{\dagger}$ , but they will be necessary later on when we wish to take the covariance matrix associated with non-Hermitian operators. Even in those cases, Eqs. (2.4) and (2.12) still hold.

Since every  $N$ -mode Gaussian pure state can be obtained by acting with a Gaussian unitary operation on the ground state of  $N$  independent harmonic oscillators, we can use the symplectic representation of this operation to parametrize these states. To eliminate units in  $\hat{\mathbf{q}}$  and  $\hat{\mathbf{p}}$ , we normalize the covariance matrix of the  $N$ -mode ground state to be

$$
\operatorname {c o v} \hat {\mathbf {x}} _ {0} = \frac {1}{2} \mathbf {I}, \tag {2.15}
$$

where  $\hat{\mathbf{x}}_0$  is the vector of Heisenberg operators associated with this state. This means that  $\mathrm{var}\hat{q}_{0j} = \mathrm{var}\hat{p}_{0j} = \frac{1}{2}$  for every mode  $j$ . The Heisenberg operators for any Gaussian pure state can be obtained from  $\hat{\mathbf{x}}_0$  by acting with a symplectic matrix, resulting in a covariance matrix of

$$
\begin{array}{l} \operatorname {c o v} \hat {\mathbf {x}} = \operatorname {c o v} (\mathbf {S} \hat {\mathbf {x}} _ {0}) = \frac {1}{2} \langle \left\{\left(\mathbf {S} \hat {\mathbf {x}} _ {0}\right) ^ {\dagger}, \left(\mathbf {S} \hat {\mathbf {x}} _ {0}\right) ^ {\mathrm {T}} \right\} \rangle = \frac {1}{2} \mathbf {S} \left\langle \left\{\hat {\mathbf {x}} _ {0} ^ {\dagger}, \hat {\mathbf {x}} _ {0} ^ {\mathrm {T}} \right\} \right\rangle \mathbf {S} ^ {\mathrm {T}} \\ = \mathbf {S} (\operatorname {c o v} \hat {\mathbf {x}} _ {0}) \mathbf {S} ^ {\mathrm {T}} = \frac {1}{2} \mathbf {S} \mathbf {S} ^ {\mathrm {T}}. \tag {2.16} \\ \end{array}
$$

(For some thoughts on how to generalize this to mixed Gaussian states, see Appendix D.) Since the covariance matrix uniquely defines a Gaussian state, by Eq. (2.16), so does  $\mathbf{S}\mathbf{S}^{\mathrm{T}}$ . To be practically useful for our purposes, we need a graph representation of  $\mathbf{S}$  (or, more accurately, of  $\mathbf{S}\mathbf{S}^{\mathrm{T}}$ ) and useful transformation rules for this representation. To this end, we will decompose  $\mathbf{S}$  and use the resulting matrix factors to define the adjacency matrix for an associated graph.

There are a number of ways to decompose a symplectic matrix, but the one we are interested in is the following unique decomposition for any symplectic  $\mathbf{S}$  [44]:

$$
\mathbf {S} = \binom {\mathbf {I}} {\mathbf {V}} \binom {\mathbf {U} ^ {- 1 / 2}} {\mathbf {0}} \binom {\mathbf {0}} {\mathbf {U} ^ {1 / 2}} \binom {\mathbf {X}} {\mathbf {Y}} \binom {- \mathbf {Y}} {\mathbf {X}}, \tag {2.17}
$$

where  $\mathbf{U}$  is symmetric and positive definite  $(\mathbf{U} = \mathbf{U}^{\mathrm{T}} > 0)$ ,  $\mathbf{V}$  is symmetric (but not necessarily positive definite), and the third matrix is orthogonal and thus irrelevant in the product  $\mathbf{S}\mathbf{S}^{\mathrm{T}}$ . Therefore, while this expansion is unique for a given  $\mathbf{S}$  [44], since we only care about  $\mathbf{S}\mathbf{S}^{\mathrm{T}}$ , we can fix  $\mathbf{X} = \mathbf{I}$  and  $\mathbf{Y} = \mathbf{0}$  and, after multiplying the right-hand side above, define

$$
\mathbf {S} _ {(\mathbf {U}, \mathbf {V})} := \left( \begin{array}{c c} \mathbf {U} ^ {- 1 / 2} & \mathbf {0} \\ \mathbf {V U} ^ {- 1 / 2} & \mathbf {U} ^ {1 / 2} \end{array} \right). \tag {2.18}
$$

Using Eq. (2.16), the covariance matrix associated with this state is

$$
\boldsymbol {\Sigma} _ {(\mathbf {U}, \mathbf {V})} = \frac {1}{2} \mathbf {S} _ {(\mathbf {U}, \mathbf {V})} \mathbf {S} _ {(\mathbf {U}, \mathbf {V})} ^ {\mathrm {T}} = \frac {1}{2} \left( \begin{array}{c c} \mathbf {U} ^ {- 1} & \mathbf {U} ^ {- 1} \mathbf {V} \\ \mathbf {V U} ^ {- 1} & \mathbf {U} + \mathbf {V U} ^ {- 1} \mathbf {V} \end{array} \right). \tag {2.19}
$$

Using this we can immediately write down the Wigner function for the state

$$
\begin{array}{l} W _ {(\mathbf {U}, \mathbf {V})} (\mathbf {x}) = (2 \pi) ^ {- N} (\det  \boldsymbol {\Sigma} _ {(\mathbf {U}, \mathbf {V})}) ^ {- 1 / 2} \exp \left[ - \frac {1}{2} \mathbf {x} ^ {\mathrm {T}} \boldsymbol {\Sigma} _ {(\mathbf {U}, \mathbf {V})} ^ {- 1} \mathbf {x} \right] \\ = \pi^ {- N} \exp \left[ - \left(\mathbf {S} _ {(\mathbf {U}, \mathbf {V})} ^ {- 1} \mathbf {x}\right) ^ {\mathrm {T}} \left(\mathbf {S} _ {(\mathbf {U}, \mathbf {V})} ^ {- 1} \mathbf {x}\right) \right], \tag {2.20} \\ \end{array}
$$

and since the state is pure, we can also write down its position-space wave function (up to an arbitrary overall phase),

$$
\psi_ {(\mathbf {U}, \mathbf {V})} (\mathbf {q}) = \pi^ {- N / 4} (\det  \mathbf {U}) ^ {1 / 4} \exp \left[ - \frac {1}{2} \mathbf {q} ^ {\mathrm {T}} (\mathbf {U} - i \mathbf {V}) \mathbf {q} \right]. \tag {2.21}
$$

Note that  $\mathbf{q}$ ,  $\mathbf{p}$ , and  $\mathbf{x} = \binom{\mathbf{q}}{\mathbf{p}}$  are  $c$ -number column vectors that correspond to their respective operator-valued counterparts. Any of these four equations can be used to define a Gaussian pure state from any pair of  $N\times N$  symmetric matrices,  $\mathbf{U}$  and  $\mathbf{V}$ , with  $\mathbf{U} > 0$  ensuring physicality of the state. Equation (2.18) defines the Heisenberg quadrature variables  $\hat{\mathbf{x}} = \mathbf{S}_{(\mathbf{U},\mathbf{V})}\hat{\mathbf{x}}_0$  associated with the state in question, and Eq. (2.19) gives the (symmetrized) covariance matrix, from which the Wigner function, Eq. (2.20), may be readily obtained. If one wishes to work with wave functions, then Eq. (2.21) can be used. Inversion of these relations to find  $\mathbf{U}$  and  $\mathbf{V}$  is straightforward. The ground state corresponds to  $\mathbf{U} = \mathbf{I}$  and  $\mathbf{V} = \mathbf{0}$ .

# D. Gaussian pure states as undirected graphs with complex-weighted edges

The complex combination  $\mathbf{U} - i\mathbf{V}$  that appears in Eq. (2.21) is suggestive of a way to unify the two symmetric matrices that define a Gaussian pure state. Instead, we multiply this by  $i$  and define

$$
\mathbf {Z} := \mathbf {V} + i \mathbf {U} \tag {2.22}
$$

for reasons that will become clear shortly. This complex, symmetric matrix  $\mathbf{Z}$  is only useful, of course, if it has nice transformation properties under Gaussian unitary operations. In fact, this is the case. Defining

$$
\mathbf {S} = \left( \begin{array}{l l} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right) \tag {2.23}
$$

as the symplectic matrix corresponding to the evolution in question, if the initial state corresponds to  $\mathbf{Z}$  as above, then the new state after the evolution will correspond to [44]

$$
\mathbf {Z} ^ {\prime} = (\mathbf {C} + \mathbf {D Z}) (\mathbf {A} + \mathbf {B Z}) ^ {- 1}. \tag {2.24}
$$

We interpret  $\mathbf{Z}$  as the adjacency matrix for an undirected graph with complex-valued edge weights, thus providing our graph representation for any Gaussian pure state. A rigorous derivation of this relation and of the unique map from Gaussian pure states to graphs is included in Appendix A.

# E. Gaussian graphs from expectation values of observables

An important operational question is, How can the graph for a Gaussian pure state be obtained from the statistics of measurements made on the system? To answer it, it is useful to consider the covariance matrix from Eq. (2.19). We can

immediately extract  $\mathbf{U}$  from the upper-left block:

$$
\mathbf {U} = (2 \operatorname {c o v} \hat {\mathbf {q}}) ^ {- 1} = \frac {1}{2} \langle \hat {\mathbf {q}} \hat {\mathbf {q}} ^ {\mathrm {T}} \rangle^ {- 1}. \tag {2.25}
$$

Once we have  $\mathbf{U}$ , extracting  $\mathbf{V}$  from the upper-right block is straightforward:

$$
\mathbf {V} = \mathbf {U} \langle \{\hat {\mathbf {q}}, \hat {\mathbf {p}} ^ {\mathrm {T}} \} \rangle = \frac {1}{2} \langle \hat {\mathbf {q}} \hat {\mathbf {q}} ^ {\mathrm {T}} \rangle^ {- 1} \langle \{\hat {\mathbf {q}}, \hat {\mathbf {p}} ^ {\mathrm {T}} \} \rangle . \tag {2.26}
$$

Putting these together gives

$$
\begin{array}{l} \mathbf {Z} = \mathbf {V} + i \mathbf {U} = \frac {1}{2} \langle \hat {\mathbf {q}} \hat {\mathbf {q}} ^ {\mathrm {T}} \rangle^ {- 1} (\langle \{\hat {\mathbf {q}}, \hat {\mathbf {p}} ^ {\mathrm {T}} \} \rangle + i \mathbf {I}) \\ = \frac {1}{2} \langle \hat {\mathbf {q}} \hat {\mathbf {q}} ^ {\mathrm {T}} \rangle^ {- 1} \left(\left\langle \left\{\hat {\mathbf {q}}, \hat {\mathbf {p}} ^ {\mathrm {T}} \right\} \right\rangle + \left\langle \left[ \hat {\mathbf {q}}, \hat {\mathbf {p}} ^ {\mathrm {T}} \right] \right\rangle\right) = \left\langle \hat {\mathbf {q}} \hat {\mathbf {q}} ^ {\mathrm {T}} \right\rangle^ {- 1} \left\langle \hat {\mathbf {q}} \hat {\mathbf {p}} ^ {\mathrm {T}} \right\rangle . \tag {2.27} \\ \end{array}
$$

Equation (2.27) shows how to extract  $\mathbf{Z}$  from the expectation values of  $\hat{q}_j\hat{q}_k$  and  $\hat{q}_j\hat{p}_k$ , with the latter obtainable from the observables  $(\hat{q}_j\hat{p}_k + \hat{p}_k\hat{q}_j)$  using the form on the first line.

# F. Approximate CV cluster states

The graph representative of a Gaussian pure state defined above is, in fact, the natural way to extend the graph representation of ideal CV cluster state to their finitely squeezed Gaussian approximants. The canonical method for creating a CV cluster state [5] is to squeeze all modes as much as possible in the momentum quadrature and then to apply  $\hat{C}_Z[\mathbf{A}]$  in accord with a (real-weighted) graph  $\mathbf{A}$ . An ideal cluster state  $|\psi_{\mathbf{A}}\rangle$  from Eq. (2.1) is obtained by taking the limit of infinite initial squeezing on all the modes. Let us see what this looks like in our formalism.

The symplectic transformation corresponding to the canonically generated CV cluster state consists of two parts: the initial single-mode squeezing and the controlled-  $Z$  operations. If we take all modes to be momentum squeezed such that their variance is reduced by a factor of  $e^{-2r}$ , followed by  $\hat{C}_Z[\mathbf{A}]$ , this corresponds to a total symplectic transformation of

$$
\binom {\mathbf {I}} {\mathbf {A}} \binom {e ^ {r} \mathbf {I}} {\mathbf {0}} \binom {\mathbf {0}} {e ^ {- r} \mathbf {I}}. \tag {2.28}
$$

Comparing this with Eq. (2.18), we can immediately read off that  $\mathbf{U} = e^{-2r}\mathbf{I}$  and  $\mathbf{V} = \mathbf{A}$ , and we find that

$$
\mathbf {Z} _ {r} := \mathbf {A} + i e ^ {- 2 r} \mathbf {I} \tag {2.29}
$$

corresponds to an  $r$ -indexed family of approximate CV cluster states with graph  $\mathbf{A}$  since

$$
\lim  _ {r \rightarrow \infty} \mathbf {Z} _ {r} = \mathbf {A}. \tag {2.30}
$$

However, there are many other families of Gaussian pure states that fit the bill, including one that will be useful later (in Sec. IV):

$$
\mathbf {Z} _ {\alpha} = i \operatorname {s e c h} 2 \alpha \mathbf {I} + \tanh 2 \alpha \mathbf {A}, \tag {2.31}
$$

which satisfies  $\lim_{\alpha \to \infty}\mathbf{Z}_{\alpha} = \mathbf{A}$ . Figure 2 illustrates the correspondence.

# G.  $\mathcal{H}$ -graph states

$\mathcal{H}$ -graph states are generated by a multimode OPO pumped by a multifrequency pump beam and have a mathematical connection to CV cluster states, even though the natures of the two types of graph are different [21-24]. In our graphical

![](images/1ec049b2105fa1f959183fcbe93c58796ca0fc506d38997c126181d49e32b129.jpg)  
(a)

![](images/7989d9c00a883668f7f3e3eba19df3d63f7d9c658759109becd30559fe596677.jpg)  
(b)

![](images/9ae2dd899730818b0360fade04b4b86ef42972e046cd9009fd5b98bfd2f1f8e2.jpg)  
FIG. 2. (Color online) Complex-weighted graph representation of approximate CV cluster states. Nodes no longer specify any particular input state on their own and are henceforth colored black to emphasize this distinction. Instead, the state represented by the graph is entirely specified by the edge weights, which can now be complex. The real part of the graph,  $\mathbf{V}$ , still has the same interpretation as in the original formalism, i.e., a collection of weights for the respective  $C_Z$  gates applied between the linked nodes, while the imaginary part,  $\mathbf{U}$ , corresponds to initial multimode squeezing that only mixes  $\hat{q}\mathrm{s}$  and  $\hat{p}\mathrm{s}$  separately (see text). (a) The graph from Fig. 1 is reinterpreted in this formalism. Because the graph has only real weights, it does not represent a physical state (since  $\mathbf{U} \neq 0$ )—and rightly so since ideal CV cluster states are infinitely squeezed. (b) Graph for an approximate CV cluster state made by the canonical method [5,6]. The imaginary-weighted self-loops indicate the amount of initial single-mode squeezing applied. In the limit of large squeezing ( $r \to \infty$ ), these physical Gaussian pure states limit to the ideal graph in (a). Note that in this context, states with large squeezing in  $\hat{p}$  are represented by black nodes with a vanishing imaginary self-loop weight, rather than by the white nodes in Fig. 1. (c) Another approximate CV cluster state, distinct from that in (b), that also limits to the ideal case (a) when  $\alpha \to \infty$ . States represented in (b) and (c) are physically distinct, but because they have the same large-squeezing behavior, they cannot be distinguished in the original graphical formalism (see Fig. 1). This new formalism allows them to be distinguished at the graph level.  
(c)

formalism, these states correspond to graphs with purely imaginary weights. Specifically,

$$
\mathbf {Z} = i e ^ {- 2 \alpha \mathbf {G}}, \tag {2.32}
$$

where the real, symmetric matrix  $\mathbf{G}$  is the  $\mathcal{H}$  graph for the state, and  $\alpha$  is a unitless overall squeezing strength. The term "  $\mathcal{H}$  graph" refers to the fact that  $\mathbf{G}$  specifies the (linearized) Hamiltonian for the OPO that acts on the vacuum of the cavity modes to generate the state. This Hamiltonian is defined by

$$
\begin{array}{l} \hat {\mathcal {H}} (\mathbf {G}) = i \hbar \kappa \sum_ {j, k} G _ {j k} (\hat {a} _ {j} ^ {\dagger} \hat {a} _ {k} ^ {\dagger} - \hat {a} _ {j} \hat {a} _ {k}) = i \hbar \kappa (\hat {\mathbf {a}} ^ {\mathrm {H}} \mathbf {G} \hat {\mathbf {a}} ^ {\dagger} - \hat {\mathbf {a}} ^ {\mathrm {T}} \mathbf {G} \hat {\mathbf {a}}) \\ = \hbar \kappa (\hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {G} \hat {\mathbf {p}} + \hat {\mathbf {p}} ^ {\mathrm {T}} \mathbf {G} \hat {\mathbf {q}}), \tag {2.33} \\ \end{array}
$$

where  $\kappa$  is a squeezing parameter per unit time [21]. If this Hamiltonian is applied for time  $t$ , acting on the vacuum state with  $\hat{U} = \exp [-\frac{i}{\hbar}\hat{\mathcal{H}} (\mathbf{G})t]$ , then  $\alpha = 2\kappa t$  in Eq. (2.32).

Most  $\mathcal{H}$ -graph states (i.e., those with a full-rank  $\mathbf{G}$ ) correspond to CV cluster states in the limit of large squeezing if one phase shifts modes appropriately [21]. Recent work shows that this method can be used, in a scalable fashion, to make many small, disconnected square-graph CV cluster states from a single OPO [22]. More importantly, a single OPO can also be used to make very large QC-universal CV cluster states in a scalable fashion [23,24].

The connection between the  $\mathcal{H}$  graph  $\mathbf{G}$  and the Gaussian graph  $\mathbf{Z}$ , as indicated by Eq. (2.32), is through the exponential map, which is generally a nontrivial operation on a graph. However, when  $\mathbf{G}$  is self-inverse  $(\mathbf{G}^2 = \mathbf{I})$ , this connection simplifies greatly:

$$
\mathbf {G} ^ {2} = \mathbf {I} \quad \Longrightarrow \quad \mathbf {Z} = i \cosh 2 \alpha \mathbf {I} - i \sinh 2 \alpha \mathbf {G}. \tag {2.34}
$$

In this case, the Gaussian graph  $\mathbf{Z}$  is just a rescaled version of  $\mathbf{G}$  with additional self-loops. We explore the close connection between  $\mathcal{H}$  graphs of this form and CV cluster states of the form of Eq. (2.31) in Sec. IV.

# H. Complex nullifiers

In Ref. [6], the real-valued nullifier formalism is used to illustrate the effect of quadrature measurements on ideal CV cluster states. (In an optical setting, this corresponds to homodyne detection.) Rules for updating the nullifiers under such measurements are derived, but they only apply to ideal CV cluster states. In addition, the resulting state after the measurement frequently is only an ideal CV cluster state up to phase shifts (if at all) and thus cannot be represented by any real-weighted CV cluster-state graph. Zhang has implemented these rules as a graph transformation [42], but the same restriction to ideal CV cluster states still applies. Here we extend the nullifier transformation rules from Ref. [6] to graph transformation rules for quadrature measurements made on any Gaussian pure state, including approximate CV cluster states, thus generalizing the results from Ref. [42]. We do this by first generalizing the real-valued nullifier formalism to complex-valued nullifiers, which can be used to represent all Gaussian pure states.

The nullifier formalism for CV cluster states, given by Eq. (2.2), can be extended to all Gaussian pure states using the simple replacement of the CV cluster-state graph  $\mathbf{A}$  with the Gaussian graph  $\mathbf{Z}$ :

$$
\begin{array}{l} (\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}) | \psi_ {\mathbf {Z}} \rangle = (- \mathbf {Z} \mathbf {I}) \hat {\mathbf {x}} \hat {U} _ {\mathbf {Z}} | 0 \rangle = \hat {U} _ {\mathbf {Z}} (- \mathbf {Z} \mathbf {I}) \mathbf {S} _ {\mathbf {Z}} \hat {\mathbf {x}} | 0 \rangle \\ = \hat {U} _ {\mathbf {Z}} \mathbf {U} ^ {1 / 2} (\hat {\mathbf {p}} - i \hat {\mathbf {q}}) | 0 \rangle = \mathbf {0}, \tag {2.35} \\ \end{array}
$$

where we have used Eq. (2.18) to plug in for  $\mathbf{S}_{\mathbf{Z}} = \mathbf{S}_{(\mathbf{U},\mathbf{V})}$ , and we note that  $\hat{\mathbf{p}} - i\hat{\mathbf{q}} = -i\sqrt{2}\hat{\mathbf{a}}$ , a vector of operators annihilating the ground state. Note that the nullifier vector  $\hat{\mathbf{p}} - \mathbf{Z}\hat{\mathbf{q}}$  is not unique for a given graph since any  $c$ -number matrix  $\mathbf{M}$ , acting from the left, will generate a new vector of nullifiers that are also satisfied by the state:

$$
(\mathbf {M} \hat {\mathbf {p}} - \mathbf {M Z} \hat {\mathbf {q}}) | \psi_ {\mathbf {Z}} \rangle = \mathbf {0}. \tag {2.36}
$$

The action of the matrix  $\mathbf{M}$  represents forming a new nullifier vector from linear combinations of the original nullifiers. If, in addition,  $\mathbf{M}$  is invertible, then this new nullifier vector also uniquely defines the state.

We can take the fact that  $\hat{\mathbf{p}} - i\hat{\mathbf{q}}$  is proportional to a vector of annihilation operations and make the analogy more explicit. Let us define

$$
\hat {\mathbf {a}} _ {\mathbf {Z}} := \frac {i}{\sqrt {2}} \mathbf {U} ^ {- 1 / 2} (\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}), \tag {2.37}
$$

$$
\hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\dagger} := \frac {- i}{\sqrt {2}} \mathbf {U} ^ {- 1 / 2} \left(\hat {\mathbf {p}} - \mathbf {Z} ^ {*} \hat {\mathbf {q}}\right), \tag {2.38}
$$

which have the usual commutation relations

$$
\begin{array}{l} \left[ \hat {\mathbf {a}} _ {\mathbf {Z}}, \hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\mathrm {H}} \right] = \frac {1}{2} \mathbf {U} ^ {- 1 / 2} (- \mathbf {Z} \quad \mathbf {I}) [ \hat {\mathbf {x}}, \hat {\mathbf {x}} ^ {\mathrm {T}} ] \binom {- \mathbf {Z} ^ {*}} {\mathbf {I}} \mathbf {U} ^ {- 1 / 2} \\ = \frac {1}{2} \mathbf {U} ^ {- 1 / 2} (- \mathbf {Z} \quad \mathbf {I}) i \boldsymbol {\Omega} \binom {- \mathbf {Z} ^ {*}} {\mathbf {I}} \mathbf {U} ^ {- 1 / 2} = \mathbf {I}, \tag {2.39} \\ \end{array}
$$

along with  $[\hat{\mathbf{a}}_{\mathbf{Z}},\hat{\mathbf{a}}_{\mathbf{Z}}^{\mathrm{T}}] = [\hat{\mathbf{a}}_{\mathbf{Z}}^{\dagger},\hat{\mathbf{a}}_{\mathbf{Z}}^{\mathrm{H}}] = \mathbf{0}$ . In the case of the ground state,  $\mathbf{Z} = i\mathbf{I}$ , and this expression reduces to the usual result  $(\hat{\mathbf{a}}_{\mathbf{Z}} = \hat{\mathbf{a}})$ . In the more general case, these operators can be used to derive a Hamiltonian for which the associated graph  $\mathbf{Z}$  is the ground state (see Sec. IV F).

With this notation in hand, we can calculate

$$
\begin{array}{l} \operatorname {c o v} (\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}) = \operatorname {c o v} (- i \sqrt {2} \mathbf {U} ^ {1 / 2} \hat {\mathbf {a}} _ {\mathbf {Z}}) = \mathbf {U} ^ {1 / 2} \left\langle \left\{\hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\dagger}, \hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\mathrm {T}} \right\} \right\rangle \mathbf {U} ^ {1 / 2} \\ = \mathbf {U} ^ {1 / 2} \left\{\left\langle 2 \hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\dagger} \hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\mathrm {T}} \right\rangle + \left\langle [ \hat {\mathbf {a}} _ {\mathbf {Z}}, \hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\mathrm {H}} ] \right\rangle \right\} \mathbf {U} ^ {1 / 2} \\ = \mathbf {U}, \tag {2.40} \\ \end{array}
$$

where we used Eqs. (2.35) and (2.39) to obtain the last line. For approximate CV cluster states, it is also useful to calculate the covariance matrix of just the real part of  $\mathbf{Z}$  (namely,  $\mathbf{V}$ ):

$$
\begin{array}{l} \operatorname {c o v} [ \hat {\mathbf {p}} - \mathbf {V} \hat {\mathbf {q}} ] = (- \mathbf {V} \mathbf {I}) (\operatorname {c o v} \hat {\mathbf {x}}) \left( \begin{array}{c} - \mathbf {V} \\ \mathbf {I} \end{array} \right) \\ = \frac {1}{2} (\mathbf {0} \mathbf {I}) \binom {\mathbf {U} ^ {- 1} \mathbf {0}} {\mathbf {0} \mathbf {U}} \binom {\mathbf {0}} {\mathbf {I}} = \frac {1}{2} \mathbf {U}, \tag {2.41} \\ \end{array}
$$

where we have used the explicit form for the covariance matrix—the explicit matrix in Eq. (2.19). Comparing this expression with Eq. (2.3), we get a nice interpretation of  $\mathbf{Z}$ 's real and imaginary parts:  $\mathbf{V}$  is the graph of the ideal CV cluster state approximated by  $\mathbf{Z}$ , and  $\frac{1}{2}\mathbf{U}$  is the error in the approximation—now expressed in quantitative terms as the covariance matrix of the nullifiers  $\hat{\mathbf{p}} -\mathbf{V}\hat{\mathbf{q}}$ . For this interpretation to make any sense, of course,  $\mathbf{U}$  must be small. Since  $\mathbf{U} > 0$ , we can use the trace to say that  $\frac{1}{2}\operatorname {tr}\mathbf{U}$  is the magnitude of the approximation error in approximating the ideal CV cluster state  $\mathbf{V}$  using  $\mathbf{Z}$ . This trace corresponds to the sum of the variances of each of the nullifiers:

$$
\frac {1}{2} \operatorname {t r} \mathbf {U} = \sum_ {j} \left\langle \psi_ {\mathbf {Z}} \right| \left(\hat {p} _ {j} - \sum_ {k} V _ {j k} \hat {q} _ {k}\right) ^ {2} | \psi_ {\mathbf {Z}} \rangle , \tag {2.42}
$$

which should be compared with Eq. (2.5).

This extension of the real nullifier formalism for real-weighted, ideal CV cluster states to a complex nullifier formalism for complex-weighted, physical CV cluster states—as well as all other Gaussian pure states—corresponds to a similar generalization on the level of the stabilizer operators, which, in the CV case, describe position and momentum shifts in phase space [6,14]. As we continue focusing on the nullifiers here, we give a brief derivation of the corresponding generalized stabilizer representation for Gaussian pure states in Appendix C.

# III. TRANSFORMATION RULES

In this section, we derive the rules for updating a graph after a LG unitary transformation is performed on one or more

of the modes or when a quadrature measurement is made. Since an arbitrary  $n$ -local transformation can be obtained by composing one- and two-local transformations, we treat those cases with additional care. We begin by deriving the effects of the symplectic transformations on the underlying matrix  $\mathbf{Z}$ , and following that, we make connection with the Gaussian unitary transformations they represent, and we illustrate these transformations graphically.

# A.  $n$ -Local Gaussian unitary operations

Consider a Gaussian pure state on  $n + p$  modes. Its graph  $\mathbf{Z}$  can be written in block form as

$$
\mathbf {Z} = \left( \begin{array}{c c} \mathbf {T} & \mathbf {R} ^ {\mathrm {T}} \\ \mathbf {R} & \mathbf {W} \end{array} \right), \tag {3.1}
$$

where  $\mathbf{T}$  is  $n\times n$ ,  $\mathbf{R}$  is  $p\times n$ , and  $\mathbf{W}$  is  $p\times p$ . The symmetric matrix  $\mathbf{T}$  is the adjacency matrix for the induced subgraph of  $\mathbf{Z}$  formed by considering only the  $n$  modes in question. The other symmetric matrix  $\mathbf{W}$  represents the induced subgraph corresponding to the untouched modes.  $\mathbf{R}$ , of course, represents the connection between the two sets of nodes.

Without loss of generality, we can represent an arbitrary  $n$ -local operation with the symplectic matrix

$$
\mathbf {S} = \left( \begin{array}{c c c c} \mathbf {A} & \mathbf {0} & \mathbf {B} & \mathbf {0} \\ \mathbf {0} & \mathbf {I} & \mathbf {0} & \mathbf {0} \\ \mathbf {C} & \mathbf {0} & \mathbf {D} & \mathbf {0} \\ \mathbf {0} & \mathbf {0} & \mathbf {0} & \mathbf {I} \end{array} \right), \tag {3.2}
$$

and

$$
\mathbf {S} _ {n - \text {l o c a l}} = \left( \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right) \tag {3.3}
$$

is the symplectic operation for just the  $n$  target nodes. Then, defining

$$
\mathbf {J} = (\mathbf {A} + \mathbf {B T}) ^ {- 1}, \tag {3.4}
$$

we follow Eq. (2.24) and write the transformed matrix as

$$
\begin{array}{l} \mathbf {Z} ^ {\prime} = \left[ \left( \begin{array}{c c} \mathbf {C} & \mathbf {0} \\ \mathbf {0} & \mathbf {0} \end{array} \right) + \left( \begin{array}{c c} \mathbf {D} & \mathbf {0} \\ \mathbf {0} & \mathbf {I} \end{array} \right) \mathbf {Z} \right] \left[ \left( \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ \mathbf {0} & \mathbf {I} \end{array} \right) + \left( \begin{array}{c c} \mathbf {B} & \mathbf {0} \\ \mathbf {0} & \mathbf {0} \end{array} \right) \mathbf {Z} \right] ^ {- 1} \\ = \binom {\mathbf {C} + \mathbf {D T}} {\mathbf {R}} \binom {\mathbf {D R} ^ {\mathrm {T}}} {\mathbf {W}} \binom {\mathbf {A} + \mathbf {B T}} {\mathbf {0}} \binom {\mathbf {B R} ^ {\mathrm {T}}} {\mathbf {I}} ^ {- 1} \\ = \left( \begin{array}{c c} \mathbf {C} + \mathbf {D T} & \mathbf {D R} ^ {\mathrm {T}} \\ \mathbf {R} & \mathbf {W} \end{array} \right) \left( \begin{array}{c c} \mathbf {J} & - \mathbf {J B R} ^ {\mathrm {T}} \\ \mathbf {0} & \mathbf {I} \end{array} \right) \\ = \binom {(\mathbf {C} + \mathbf {D T}) \mathbf {J}} {\mathbf {R J}} \begin{array}{c} - (\mathbf {C} + \mathbf {D T}) \mathbf {J B R} ^ {\mathrm {T}} + \mathbf {D R} ^ {\mathrm {T}} \\ \mathbf {W} - \mathbf {R J B R} ^ {\mathrm {T}} \end{array} . \tag {3.5} \\ \end{array}
$$

This matrix must be symmetric, so we know that the upper-right block must simply be  $\mathbf{J}^{\mathrm{T}}\mathbf{R}^{\mathrm{T}}$ , but let us work it out and see why. The first fact we will need is that  $(\mathbf{C} + \mathbf{D}\mathbf{T})(\mathbf{A} + \mathbf{B}\mathbf{T})^{-1}$  is symmetric, since it represents a Gaussian operation on a valid graph (recall that  $\mathbf{T}$  is symmetric and that  $\operatorname{Im}\mathbf{T} > 0$ ).

Therefore,

$$
\begin{array}{l} - (\mathbf {C} + \mathbf {D T}) \mathbf {J B R} ^ {\mathrm {T}} + \mathbf {D R} ^ {\mathrm {T}} \\ = - \mathbf {J} ^ {\mathrm {T}} (\mathbf {C} + \mathbf {D T}) ^ {\mathrm {T}} \mathbf {B} \mathbf {R} ^ {\mathrm {T}} + \mathbf {D} \mathbf {R} ^ {\mathrm {T}} \\ = \mathbf {J} ^ {\mathrm {T}} [ - (\mathbf {C} + \mathbf {D T}) ^ {\mathrm {T}} \mathbf {B} + \mathbf {J} ^ {- \mathrm {T}} \mathbf {D} ] \mathbf {R} ^ {\mathrm {T}} \\ = \mathbf {J} ^ {\mathrm {T}} \left[ - \mathbf {C} ^ {\mathrm {T}} \mathbf {B} - \mathbf {T D} ^ {\mathrm {T}} \mathbf {B} + \mathbf {A} ^ {\mathrm {T}} \mathbf {D} + \mathbf {T B} ^ {\mathrm {T}} \mathbf {D} \right] \mathbf {R} ^ {\mathrm {T}}. \tag {3.6} \\ \end{array}
$$

The properties of a symplectic matrix [53] include  $\mathbf{A}^{\mathrm{T}}\mathbf{D} - \mathbf{C}^{\mathrm{T}}\mathbf{B} = \mathbf{I}$  and  $\mathbf{D}^{\mathrm{T}}\mathbf{B} = \mathbf{B}^{\mathrm{T}}\mathbf{D}$ . Therefore, the quantity in brackets is equal to  $\mathbf{I}$ , and the  $n$ -local-transformed matrix is

$$
\mathbf {Z} ^ {\prime} = \binom {(\mathbf {C} + \mathbf {D T}) (\mathbf {A} + \mathbf {B T}) ^ {- 1}} {\mathbf {R} (\mathbf {A} + \mathbf {B T}) ^ {- 1}} \begin{array}{c} (\mathbf {A} + \mathbf {B T}) ^ {- \mathrm {T}} \mathbf {R} ^ {\mathrm {T}} \\ \mathbf {W} - \mathbf {R} (\mathbf {A} + \mathbf {B T}) ^ {- 1} \mathbf {B R} ^ {\mathrm {T}} \end{array}. \tag {3.7}
$$

This has a nice interpretation. The upper-left block is just the transformation that would result from applying the  $n$ -LG to the nodes in question, without any connection to other nodes. The bottom-right block reflects the fact that any changes to the other nodes' induced subgraph are mediated solely by connections with the target nodes and in an additive fashion on W. These are the two key observations—the induced subgraph on the target nodes cares not about connections to other nodes, and the effect on adjacent nodes is only through connection with the target nodes. The off-diagonal blocks illustrate the action of the transformation on the edges connecting the two sets. After discussing the important special cases of one- and two-local transformations, we illustrate these graphically to provide additional insight.

# B. Local Gaussian unitary operations

In the case of (one-)LG operations, with  $2 \times 2$  symplectic matrix

$$
\mathbf {S} _ {\mathrm {L G}} = \left( \begin{array}{c c} a & b \\ c & d \end{array} \right), \tag {3.8}
$$

this transformation is just

$$
\mathbf {Z} = \left( \begin{array}{l l} t & \mathbf {r} ^ {\mathrm {T}} \\ \mathbf {r} & \mathbf {W} \end{array} \right) \stackrel {{\mathbf {S} _ {\mathrm {L G}}}} {{\mapsto}} \left( \begin{array}{c c} \frac {c + d t}{a + b t} & \frac {\mathbf {r} ^ {\mathrm {T}}}{a + b t} \\ \frac {\mathbf {r}}{a + b t} & \mathbf {W} - \frac {b \mathbf {r r} ^ {\mathrm {T}}}{a + b t} \end{array} \right) = \mathbf {Z} ^ {\prime}. \tag {3.9}
$$

From these results, we calculate (below) local graph transformation rules corresponding to elementary LG operations.

# C. Two-local Gaussian operations

Arbitrary Gaussian operations can be constructed out of one-local (LG) and two-local (2LG) operations alone. In fact, given the availability of all LGs, only a single fiducial 2LG is needed to construct any Gaussian operation [54]. The most theoretically simple 2LG is just the  $C_Z$  gate. This operation just adds a real constant—proportional to the strength of the interaction—to the edge in question.

Considering the applicability of our results to optical implementations, we also consider another operation (or, actually, another class of operations), since the  $C_Z$  gate is difficult to implement experimentally [11]. This class will consist of beamsplitter interactions. Specifically, we consider only a fiducial type of photon-number-conserving interaction. This 2LG interaction can be used to model any beamsplitter when combined with appropriate phase shifts on the input and output modes:

$$
\mathbf {S} _ {\mathrm {B S}} (\theta) = \left( \begin{array}{c c} \mathbf {R} _ {\theta} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} _ {\theta} \end{array} \right) = \left( \begin{array}{c c c c} \cos \theta & - \sin \theta & 0 & 0 \\ \sin \theta & \cos \theta & 0 & 0 \\ 0 & 0 & \cos \theta & - \sin \theta \\ 0 & 0 & \sin \theta & \cos \theta \end{array} \right), \tag {3.10}
$$

where  $\sin \theta$  is the amplitude reflectivity of the beamsplitter [55]. This form is particularly simple because  $\mathbf{B} = \mathbf{C} = \mathbf{0}$  and  $\mathbf{A} = \mathbf{D} = \mathbf{R}_{\theta}$ , which gives  $(\mathbf{A} + \mathbf{B}\mathbf{T})^{-1} = \mathbf{R}_{\theta}^{\mathrm{T}} = \mathbf{R}_{-\theta}$ . This being the only quantity that affects nodes outside the target set, this is particularly convenient. The transformation of  $\mathbf{T}$  is given by

$$
\begin{array}{l} \mathbf {T} ^ {\prime} = \mathbf {R} _ {\theta} \mathbf {T R} _ {\theta} ^ {\mathrm {T}} = \left( \begin{array}{c c} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{array} \right) \left( \begin{array}{c c} T _ {1 1} & T _ {1 2} \\ T _ {1 2} & T _ {2 2} \end{array} \right) \left( \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right) \\ = \left( \begin{array}{c c} T _ {1 1} \cos^ {2} \theta + T _ {2 2} \sin^ {2} \theta - T _ {1 2} \sin 2 \theta & T _ {1 2} \cos 2 \theta + \frac {1}{2} (T _ {1 1} - T _ {2 2}) \sin 2 \theta \\ T _ {1 2} \cos 2 \theta + \frac {1}{2} (T _ {1 1} - T _ {2 2}) \sin 2 \theta & T _ {2 2} \cos^ {2} \theta + T _ {1 1} \sin^ {2} \theta + T _ {1 2} \sin 2 \theta \end{array} \right). \tag {3.11} \\ \end{array}
$$

The final result for the beamsplitter transformation is:

$$
\begin{array}{l} \mathbf {Z} ^ {\prime} = \left( \begin{array}{c c} \mathbf {T} ^ {\prime} & \mathbf {R} _ {\theta} \mathbf {R} ^ {\mathrm {T}} \\ \mathbf {R R} _ {\theta} ^ {\mathrm {T}} & \mathbf {W} \end{array} \right) \\ = \binom {\mathbf {R} _ {\theta}} {\mathbf {0}} \binom {\mathbf {T}} {\mathbf {R}} \binom {\mathbf {R} ^ {\mathrm {T}}} {\mathbf {W}} \binom {\mathbf {R} _ {\theta} ^ {\mathrm {T}}} {\mathbf {0}} \binom {\mathbf {0}} {\mathbf {I}}, \tag {3.12} \\ \end{array}
$$

where  $\mathbf{T}'$  is defined in Eq. (3.11), and we have included the second (expanded) form to show the formally simple effect that beamsplitter interactions of the form  $\mathbf{S}_{\mathrm{BS}}(\theta)$  have

on Gaussian graphs. (As previously mentioned, modeling a physical beamsplitter may additionally involve phase shifts, which are LG operations.)

# D. Quadrature measurements

According to the rules in Ref. [6], the first thing to do when considering quadrature measurements is to define the nullifier that corresponds to the measurement outcome. This is the new nullifier that the postmeasurement state must satisfy due to projection onto the measurement basis. (This rule applies

even if the measurement is destructive.) Next, we choose an appropriate invertible matrix  $\mathbf{M}$  such that the entries in the new (ideal) nullifier vector  $\mathbf{M} \hat{\mathbf{p}} - \mathbf{M} \mathbf{V} \hat{\mathbf{q}}$  are such that only one of them fails to commute with the nullifier corresponding to the measurement (something that can always be done). This new nullifier vector also uniquely defines the premeasurement state (since  $\mathbf{M}$  is invertible), but because only one of its entries (i.e., a single nullifier) fails to commute with the measurement nullifier, all the remaining ones will also be nullifiers for the postmeasurement state. The one that fails to commute is therefore discarded and replaced by the measurement nullifier to form the postmeasurement nullifier vector.

Everything said in the previous paragraph remains valid when considering the complex nullifiers from Sec. II H instead of the ideal ones from Ref. [6]. We therefore focus on one specific example:  $\hat{q}$  measurements. Such a measurement on node  $j$  with outcome  $s_j$  means that the new state has  $\hat{q}_j - s_j$  as one of its nullifiers (we assume the detector noise is negligible). However, since we are neglecting displacements, the postmeasurement state will instead have  $\hat{q}_j$  as the measurement nullifier. The usual nullifier vector for a Gaussian graph  $\mathbf{Z}$  is  $\hat{\mathbf{p}} -\mathbf{Z}\hat{\mathbf{q}}$ , which is already in a fortunate form since all of the nullifiers commute with  $\hat{q}_j$  except the  $j$ th one. This measurement on an ideal CV cluster state corresponds to deletion of the measured node from the cluster, along with all of its links. The effect is the same on Gaussian graphs and can be seen in the nullifier formalism, in that all references to  $\hat{p}_j$  are gone, and linear combinations of the postmeasurement nullifiers can be used to delete all references to  $\hat{q}_j$  as well (since  $\hat{q}_j$  alone is one of the nullifiers in the set). As an action on the adjacency matrix  $\mathbf{Z}$ , this corresponds to deleting its  $j$ th row and column.

Another useful quadrature measurement is a measurement of  $\hat{p}$ . For an ideal CV cluster state, such a measurement deletes the corresponding node but preserves the links between neighboring nodes, up to local phase shifts. Because of the phase shifts, the resulting state is often impossible to represent as an ideal CV cluster-state graph (although it still has a nullifier representation), but we can do it easily for approximate CV cluster states as a two-step process: (i) perform an inverse Fourier transform on the node to be measured and then (ii) perform a  $\hat{q}$  measurement as described above, thereby deleting it and its links from the graph. This is not equivalent in total to a simple disconnection, however, because the phase shift generates additional connections in the neighborhood of the measured node before that node is disconnected. It is through this mechanism that a measurement of  $\hat{p}$  preserves links in the graph while deleting the measured node [6]. Measurements of the general quadrature  $\hat{q}\cos \theta +\hat{p}\sin \theta$ , which can be used to perform Gaussian dynamics<sup>6</sup> on encoded CV quantum information in the cluster [6,41], are represented analogously, with a phase shift by  $\theta$  replacing the inverse Fourier transform before the  $\hat{q}$  measurement.

For universal QC, the ability to measure in a non-Gaussian basis is required [6]. In an optical context, this can be achieved through photon counting. Because the resulting state is no longer Gaussian, such measurements are not incorporated into this formalism.

# E. Graph transformation rules

Here we illustrate the transformation rules described above as actions on the adjacency matrix  $\mathbf{Z}$  into rules transforming the associated graph for several examples. In all cases, the original  $\mathbf{Z}$  is given in block form according to Eq. (3.1), while Eqs. (3.9) and (3.7) provide the transformation laws for local and two-local operations, respectively. We focus on representative local transformations, then the two-local interactions discussed previously, and, finally, quadrature measurements.

# 1. Displacement

The graph rule for displacements in phase space is trivial: Do nothing to the graph. The Gaussian graph only represents the noise properties of the state, which are unaffected by overall displacements.

# 2. Local shear

The easiest nontrivial local operation to represent in this formalism is a local shear in phase space:  $\exp (\frac{i}{2} g\hat{q}^2)$ . The corresponding local symplectic matrix is

$$
\mathbf {S} _ {\mathrm {L G}} = \mathbf {S} _ {\text {s h e a r}} (g) := \left( \begin{array}{l l} 1 & 0 \\ g & 1 \end{array} \right), \tag {3.13}
$$

resulting in the simple transformation

$$
\mathbf {Z} \xrightarrow {\mathbf {S} _ {\text {s h e a r}} (g)} \left( \begin{array}{c c} t + g & \mathbf {r} ^ {\mathrm {T}} \\ \mathbf {r} & \mathbf {W} \end{array} \right), \tag {3.14}
$$

where  $\mathbf{Z}$  is defined in Eq. (3.9). Note that the only edge affected by this transformation is the self-loop on the node experiencing the shear (and note that  $\mathbf{W}$  is not shown):

![](images/f08e0a1f8924598881293fd86b5ececfaf9ed42e7b76b62e5d9e4eef407274bc.jpg)

# 3. Single-mode squeezing

Squeezing (i.e., reducing the variance) in  $\hat{p}$  with squeezing parameter  $r > 0$  is equivalent to squeezing in  $\hat{q}$  with squeezing parameter  $-r$  and is effected by the unitary operator  $\exp [-\frac{i}{2} r(\hat{q}\hat{p} +\hat{p}\hat{q})] = \exp [\frac{1}{2} r(a^{\dagger 2} - a^{2})]$  and represented by the local symplectic matrix

$$
\mathbf {S} _ {\mathrm {L G}} = \mathbf {S} _ {\text {s q u e e z e}} (r) := \left( \begin{array}{c c} e ^ {r} & 0 \\ 0 & e ^ {- r} \end{array} \right) \tag {3.15}
$$

and transforms graphs in a particularly simple way:

$$
\mathbf {Z} \xrightarrow {\mathbf {S} _ {\text {s q u e e z e}} (r)} \left( \begin{array}{c c} e ^ {- 2 r} t & e ^ {- r} \mathrm {r} ^ {\mathrm {T}} \\ e ^ {- r} \mathrm {r} & \mathbf {W} \end{array} \right). \tag {3.16}
$$

Note that this transformation only affects the edges attached to the node being squeezed; there is no effect on the neighborhood

of the affected node (represented by  $\mathbf{W}$ , not shown):

![](images/4333b19ae58fcdda383c0447ce204f13b5c16fdfe9bc8a9b727a77272a7e883c.jpg)

# 4. Phase shift

The transformations above only affect edges attached to the node being acted on (the "active" node). To make a change to the  $\mathbf{W}$ -matrix, however, which represents the rest of the graph, we need something else. A simple operation that accomplishes this goal and has the advantage of being very easy to implement in many experiments is the phase shift (a.k.a. phase delay), which simply rotates the phase plane of the active node by an angle  $\theta$ . The unitary operator is  $\exp \left[-\frac{i}{2}\theta (\hat{q}^2 +\hat{p}^2)\right] = e^{-i\theta /2}\exp (-i\theta \hat{a}^\dagger \hat{a})$ , where the overall phase  $e^{-i\theta /2}$  can be ignored. The corresponding local symplectic matrix is just a rotation matrix:

$$
\mathbf {S} _ {\mathrm {L G}} = \mathbf {S} _ {\text {p h a s e}} (\theta) := \left( \begin{array}{l l} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right). \tag {3.17}
$$

The associated transformation is

$$
\mathbf {Z} \xrightarrow {\mathbf {S} _ {\text {p h a s e}} (\theta)} \left( \begin{array}{c c} \frac {- \sin \theta + t \cos \theta}{\cos \theta + t \sin \theta} & \frac {\mathbf {r} ^ {\mathrm {T}}}{\cos \theta + t \sin \theta} \\ \frac {\mathbf {r}}{\cos \theta + t \sin \theta} & \mathbf {W} - \frac {\sin \theta \mathbf {r r} ^ {\mathrm {T}}}{\cos \theta + t \sin \theta} \end{array} \right). \tag {3.18}
$$

Notice that phase shifts on one node can be used to induce additional links within its neighborhood (consider the case where  $W_{12} = 0$  in what follows; also note that  $c_{\theta} = \cos \theta$  and  $s_{\theta} = \sin \theta$ ):

![](images/52da4cc344e2d450e64383131d433568dc012455fc4ea14a3c3ce1a2f975e2d1.jpg)

Any single-mode Gaussian unitary operation can be represented as a graph transformation by appropriately concatenating the rules for squeezing and phase shifting [15].

At this point it is useful to mention that all of these rules agree with the graph rules derived by Zhang [39] in the limit of  $\operatorname{Im} \mathbf{Z} \to \mathbf{0}$ , but only when the initial and final graphs remain

finite in this limit. For example, the Fourier transform, $^{8}$  which corresponds to the phase shift

$$
\mathbf {F} := \mathbf {S} _ {\text {p h a s e}} \left(- \frac {\pi}{2}\right) = \left( \begin{array}{c c} 0 & - 1 \\ 1 & 0 \end{array} \right), \tag {3.19}
$$

gives

$$
\mathbf {Z} \mapsto \left( \begin{array}{c c} - t ^ {- 1} & - t ^ {- 1} \mathbf {r} ^ {\mathrm {T}} \\ - t ^ {- 1} \mathbf {r} & \mathbf {W} - t ^ {- 1} \mathbf {r r} ^ {\mathrm {T}} \end{array} \right) \tag {3.20}
$$

and is represented as follows:

![](images/44180382597984527198a965f357194fd746c0844c09c26f8d0df8487aa1d4c9.jpg)

This has no corresponding rule in the ideal limit if  $t = 0$ , that is, if the active node has no self-loop, which is the case for most ideal CV cluster states of interest. Nevertheless, applying the Fourier transform twice has a corresponding rule in the ideal limit, even when  $t = 0$ , since  $\mathbf{F}^2 = -\mathbf{I}$ :

$$
\mathbf {Z} \stackrel {\mathbf {F} ^ {2}} {\mapsto} \left( \begin{array}{c c} t & - \mathbf {r} ^ {\mathrm {T}} \\ - \mathbf {r} & \mathbf {W} \end{array} \right). \tag {3.21}
$$

This rule corresponds exactly to Fig. 5 in Ref. [39]. Similarly, the rule for local squeezing corresponds to Fig. 6 in that reference (and is valid for  $t = 0$ ), while Figs. 3 and 4 in that work can also be derived from the rules given here.

# 5. Controlled-Z gate

Similar to the local shear operation discussed above, the controlled-Z gate,  $\hat{C}_Z(g) = \exp (ig\hat{q}_1\hat{q}_2)$ , is the easiest 2LG operation to represent in the graphical formalism. The corresponding symplectic matrix is

$$
\mathbf {S} _ {2 \mathrm {L G}} = \mathbf {S} _ {\mathrm {C} _ {Z}} (g) := \left( \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & g & 1 & 0 \\ g & 0 & 0 & 1 \end{array} \right), \tag {3.22}
$$

resulting in the simple transformation

$$
\mathbf {Z} \xrightarrow {\mathbf {S} _ {\mathrm {C} _ {Z}} (g)} \left( \begin{array}{c c c} T _ {1 1} & T _ {1 2} + g & \mathbf {R} ^ {\mathrm {T}} \\ T _ {2 1} + g & T _ {2 2} & \mathbf {W} \end{array} \right). \tag {3.23}
$$

The graphical representation of this is simply to add  $g$  to the edge weight between the two active nodes:

![](images/e1640d0ab82602642e88d78ede320c76b3ead79a59afaa6725da5743a155ef9b.jpg)

All such gates commute, and thus they can be performed in any order or even simultaneously. Despite this theoretical simplicity, their experimental difficulty [11] suggests developing another rule for a canonical 2LG operation.

# 6. Beamsplitter

The beamsplitter interaction  $\mathbf{S}_{\mathrm{BS}}(\theta)$  defined in Eq. (3.10), which corresponds to the unitary  $\exp [-i\theta (\hat{q}_1\hat{p}_2 - \hat{q}_2\hat{p}_1)] = \exp [-\theta (\hat{a}_1\hat{a}_2^\dagger -\hat{a}_2\hat{a}_1^\dagger)]$  and whose action on  $\mathbf{Z}$  is given by Eq. (3.11), has the following graph transformation rule (also note that  $\mathbf{W}$  is unaffected and that  $c_{\theta} = \cos \theta$  and  $s_\theta = \sin \theta$ ):

![](images/ea7ac68bb77c6826beeb99ca13a4b36b22d35b1f771670d85afc047fbe2a1654.jpg)

A useful special case of the above rule is the 50:50 beamsplitter, for which  $\theta = \frac{\pi}{4}$ :

![](images/bd2ffd61126e4e5fbce49a56d46e8f9ecd57f752fa07288b690307270d00c25a.jpg)

Any multimode Gaussian operation can be represented as a graph transformation by appropriately concatenating the rules for arbitrary beamsplitters, single-mode squeezing, and phase shifts through the Bloch-Messiah decomposition [15].

# 7. Measurement of  $\hat{q}$ ,  $\hat{p}$ , and other quadratures

The rule for projective measurement of  $\hat{q}$  is to delete the node and its links from the graph:

![](images/39e4828764e3a1879f190c7fe3dad332990515216b71743825276f2288f48ea7.jpg)

This is the only measurement rule we need because, as shown in Sec. III D, the rule for measuring quadratures other than  $\hat{q}$  is to phase shift the node to be measured so that a subsequent measurement of  $\hat{q}$  is equivalent to the intended quadrature measurement on the original state. For example, an inverse Fourier transform  $\mathbf{F}^{-1} = \mathbf{S}_{\mathrm{phase}}(\frac{\pi}{2})$  followed by a  $\hat{q}$  measurement implements a  $\hat{p}$  measurement on the original state. The graph rule for this is just a concatenation of the rule for the phase shift followed by node deletion.

Because phase shifts can induce new links in the neighborhood of the shifted node (i.e., it can change  $\mathbf{W}$ ), measurements other than of  $\hat{q}$  will in general preserve links between nodes that were previously mediated by the deleted node. We show a special case of this by measuring  $\hat{p}$  in the previous graph with  $W_{12} = 0$ :

![](images/e4554f7e1024b6582238d08a6faff3772412c5f4aa57e286c9b3a11f90373856.jpg)

Note that since the measured node mediated a connection between the two other nodes, measuring it in  $\hat{p}$  preserved this connection in the form of a new edge connecting those two nodes directly. Also, notice that the strength of this new connection is proportional to both of the weights  $r_{1,2}$  in the original mediated connection. These rules agree with Zhang's rules for quadrature measurements on ideal CV cluster states [42].

# IV. APPLICATIONS

# A. Closest CV cluster state to a given Gaussian pure state

Given the many different ways to make approximate CV cluster states [4,5,14,21-24,29], a useful question to ask is, What is the closest CV cluster state approximated by a given Gaussian pure state? Imagine that you are given a system with a Gaussian graph  $\mathbf{Z}$  and you want to know if you can use it as a CV cluster state for one-way QC. From Sec. II H, we know that  $\mathbf{V}$  is the graph for the ideal CV cluster state approximated by  $\mathbf{Z}$  and that  $\frac{1}{2}\operatorname{tr}\mathbf{U}$  is the approximation error (which vanishes in the ideal case). In contrast, we also know that  $\mathcal{H}$ -graph states have  $\mathbf{V} = \mathbf{0}$  and a diverging  $\frac{1}{2}\operatorname{tr}\mathbf{U}$  in the limit of large squeezing, yet they are useful for CV one-way QC [21-24]. This naive prescription is therefore not enough.

In fact, transforming these  $\mathcal{H}$ -graph states into a useful form requires phase shifting nodes appropriately [21], which, of course, also transforms the graph  $\mathbf{Z} \mapsto \mathbf{Z}'$ . The  $\mathcal{H}$ -graph method, first proposed in Ref. [21], creates approximations to ideal CV cluster states with a bipartite graph. The nodes on a bipartite graph can be colored such that no edge links two nodes of the same color. The prescription from Ref. [21] for using these states requires first performing a Fourier transform (i.e., phase shift by  $-\frac{\pi}{2}$ ) on some of the nodes and then using the resulting state as an ordinary CV cluster state (see Ref. [21] for details). The transformed  $\mathbf{Z}'$  has a nonzero  $\mathbf{V}'$  and a small approximation error (in the limit of large squeezing), which is the basis for the main result in that paper. But is this prescription

the best we can do? Or might there be some other ideal CV cluster state obtained by a different phase-shifting procedure that is better approximated by the original  $\mathcal{H}$ -graph state?

We address this question in the next subsection, but to answer it, we need to generalize our notion of what it means for a Gaussian graph to serve as a CV cluster-state graph. Specifically, we must allow the freedom to phase shift any mode arbitrarily since this operation can be absorbed into the measurement-based protocol to be implemented on the state and is thus simply a redefinition of the quadratures and does not need to be actively implemented. Our task then is to minimize the approximation error  $\frac{1}{2}\operatorname{tr}\mathbf{U}'$  over all possible phase shifts (where the prime indicates the new graph after these phase shifts have been applied). Once such a minimum is obtained, the resulting  $\mathbf{V}'$  is the "closest" ideal CV cluster state approximated by  $\mathbf{Z}'$  and thus also the closest one approximated by the original  $\mathbf{Z}$ .

The details of the calculation are somewhat involved, so we relegate them to Appendix B, choosing to list just the results here. Let

$$
\mathbf {S} _ {\theta} = \left( \begin{array}{l l} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right), \tag {4.1}
$$

where  $\pmb{\theta} = \mathrm{diag}(\theta_1, \dots, \theta_N)$ . This is the symplectic matrix representing the phase shifts  $\theta_j$  to be performed on each node  $j$ . In terms of the original graph  $\mathbf{Z}$ , the new graph is

$$
\mathbf {Z} ^ {\prime} = (- \sin \theta + \cos \theta \mathbf {Z}) (\cos \theta + \sin \theta \mathbf {Z}) ^ {- 1}. \tag {4.2}
$$

A sufficient condition for  $\frac{1}{2}\operatorname{tr}\mathbf{U}'$  to be an extremum (see Appendix B) is that

$$
\left(\operatorname {I m} \mathbf {Z} ^ {\prime 2}\right) _ {j j} = \left(\mathbf {U} ^ {\prime} \mathbf {V} ^ {\prime}\right) _ {j j} = 0 \quad \forall j, \tag {4.3}
$$

in other words, when corresponding rows of  $\mathbf{U}'$  and  $\mathbf{V}'$  are orthogonal. A sufficient condition for such an extremum also to be a local minimum (see Appendix B) is that

$$
\operatorname {I m} \left[ \left(\mathbf {I} + \mathbf {Z} ^ {\prime 2}\right) \circ \mathbf {Z} ^ {\prime} \right] > 0, \tag {4.4}
$$

where  $\circ$  represents the Hadamard (entrywise) product of two matrices. An interesting generalization of this condition is when  $\mathrm{Im}[\mathbf{I} + \mathbf{Z}'^2)\circ \mathbf{Z}']\geqslant 0$ , which is the best one can do when there is a continuous manifold of phases that all (locally) minimize  $\frac{1}{2}\operatorname {tr}\mathbf{U}'$ . We will see an example of this in Sec. IV C when we analyze the two-mode squeezed state.

We would like to stress that these are sufficient conditions for local minima only; some minima may not be able to be found this way, and not all minima found in this way may be global minima. But in certain useful cases (such as those that follow), we can apply these results to provide evidence that we have found the closest CV cluster state (up to phase shifts) for a given graph. With rigorous proofs of optimality left to future work, our purpose here is to illustrate a useful application of this graphical formalism.

# B. Analysis of the  $\mathcal{H}$ -graph method of construction

As shown in Sec. II G, all Gaussian pure states created using the  $\mathcal{H}$ -graph method [21] necessarily satisfy  $\mathbf{Z} = i\mathbf{U} = ie^{-2\alpha \mathbf{G}}$ , where  $\mathbf{G}$  is the  $\mathcal{H}$  graph that defines the multimode squeezing Hamiltonian, Eq. (2.33), that acts on the vacuum, and  $\alpha > 0$  is an overall squeezing parameter. To transform this

state into an approximate CV cluster state, the  $\mathcal{H}$ -graph method prescribes phase shifting particular nodes in accordance with the desired CV cluster-state graph [21]. We thus partition  $\mathbf{Z}$  into blocks as in Eq. (3.1), in accord with the partitioning of nodes to be shifted and nodes to be left alone:

$$
\mathbf {Z} = \left( \begin{array}{l l} i \mathbf {U} _ {1} & i \mathbf {U} _ {2} ^ {\mathrm {T}} \\ i \mathbf {U} _ {2} & i \mathbf {U} _ {3} \end{array} \right). \tag {4.5}
$$

We now perform a Fourier transform  $\mathrm{F}$  on the nodes corresponding to the upper-left block, using Eq. (3.20) for each or applying Eq. (3.7) directly, resulting in

$$
\mathbf {Z} ^ {\prime} = \left( \begin{array}{c c} i \mathbf {U} _ {1} ^ {- 1} & - \mathbf {U} _ {1} ^ {- 1} \mathbf {U} _ {2} ^ {\mathrm {T}} \\ - \mathbf {U} _ {2} \mathbf {U} _ {1} ^ {- 1} & i \mathbf {U} _ {3} - i \mathbf {U} _ {2} \mathbf {U} _ {1} ^ {- 1} \mathbf {U} _ {2} ^ {\mathrm {T}} \end{array} \right). \tag {4.6}
$$

We want to know whether this procedure results in a minimum in the approximation error  $\frac{1}{2}\operatorname{tr}\mathbf{U}'$ . This is difficult in general, but we will do so for a particularly useful case shortly. For the moment, we can prove something weaker but still interesting: this particular choice of phase shifts results in an extremum of  $\frac{1}{2}\operatorname{tr}\mathbf{U}'$ . This is easily seen since every entry in  $\mathbf{Z}'$  is either purely real or purely imaginary. Therefore  $(\mathbf{U}'\mathbf{V}')_{jj} = 0$  for all  $j$ , and thus, by Eq. (4.3),  $\frac{1}{2}\operatorname{tr}\mathbf{U}'$  is an extremum.

In fact, this holds for any set of phase shifts by multiples of  $\frac{\pi}{2}$  on purely imaginary graphs, since the above construction did not depend on any particular node(s) being selected for phase shifting, and shifting by  $\pi$  just applies negative signs, which does not change the real or imaginary nature of the entries. Many of these will result in rather large values of the approximation error, but multiples of  $\frac{\pi}{2}$  mean that these cases are still local extrema. The prescription in Ref. [21] explicitly chooses the nodes to be phase shifted so that the desired ideal CV cluster-state nullifiers vanish in the limit  $\alpha \to \infty$ . What was believed, but not shown explicitly, is that for any finite value of  $\alpha$ , the prescription minimized these variances. While we have still not shown this rigorously in the general case, we have provided additional evidence for this claim by showing that it results in an extremum of the sum of these variances. We are able to say more about particular examples, presented next.

# C. Two-mode squeezed state

The simplest nontrivial example of  $\mathcal{H}$ -graph construction of a CV cluster state is embodied by the two-mode squeezed state, which results from downconversion in a nondegenerate OPO [3,49-52]. This procedure applies the Hamiltonian from Eq. (2.33) with an  $\mathcal{H}$  graph [21]

$$
\mathbf {G} = \left( \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right). \tag {4.7}
$$

Using Eq. (2.32), the state created has

$$
\mathbf {Z} _ {1} = i e ^ {- 2 \alpha \mathbf {G}} = \left( \begin{array}{l l} i \cosh 2 \alpha & - i \sinh 2 \alpha \\ - i \sinh 2 \alpha & i \cosh 2 \alpha \end{array} \right), \tag {4.8}
$$

where  $\alpha > 0$  is an overall squeezing parameter, and the subscript is used because this state is compared below to a canonically generated two-mode CV cluster state. This state is symmetric under exchange of the nodes, so we can choose to Fourier transform either one, either of which, using Eq. (3.20), results in

$$
\mathbf {Z} _ {1} ^ {\prime} = \left( \begin{array}{l l} i \operatorname {s e c h} 2 \alpha & \tanh 2 \alpha \\ \tanh 2 \alpha & i \operatorname {s e c h} 2 \alpha \end{array} \right). \tag {4.9}
$$

This is a two-mode CV cluster state with weight  $\tanh 2\alpha$ , which goes to 1 in the limit  $\alpha \to \infty$ , and approximation error  $\frac{1}{2}\operatorname{tr}\mathbf{U}_1' = \operatorname{sech}2\alpha$ , which vanishes in the same limit. This means that  $\mathbf{Z}_1' \to \mathbf{G}$  in this limit, making trivial the connection between the generated CV cluster state and its generating  $\mathcal{H}$  graph for the two-mode squeezed state. This property is not generic—most  $\mathcal{H}$  graphs generate entirely different CV cluster states [21]—but a particular class of  $\mathcal{H}$  graphs admits this trivial connection. This is discussed further in Sec. IV D.

For finite  $\alpha$ , any combination of possible phase shifts by multiples of  $\frac{\pi}{2}$  (see Sec. IV B) results in an approximation error of either  $\cosh 2\alpha$  or  $\operatorname{sech} 2\alpha$ .  $\mathbf{Z}_1'$  corresponds to the latter—a (local) minimum in the approximation error. Let us try to use Eq. (4.4) to verify this, though:

$$
\operatorname {I m} \left[ \left(\mathbf {I} + \mathbf {Z} _ {1} ^ {\prime 2}\right) \circ \mathbf {Z} _ {1} ^ {\prime} \right] = 2 \operatorname {s e c h} 2 \alpha \tanh  ^ {2} 2 \alpha \binom {1} {1}, \tag {4.10}
$$

which has eigenvalues 0 and 4 sech  $2\alpha \tanh^2 2\alpha$ , and thus only the weaker condition,  $\mathrm{Im}[(\mathbf{I} + \mathbf{Z}_1'^2) \circ \mathbf{Z}_1'] \geqslant 0$ , is satisfied. The 0 eigenvalue in this case corresponds to the fact that any additional phase shift by  $\theta$  on the first node can be completely canceled by an additional phase shift by  $-\theta$  on the second node. This means that there is a one-parameter manifold of phase shifts that all result in  $\mathbf{Z}_1 \mapsto \mathbf{Z}_1'$ , which has approximation error such  $2\alpha$  and which is the minimum value obtainable. Specifically, all phase shifts  $(\theta_1, \theta_2)$  satisfying  $\theta_1 + \theta_2 = -\frac{\pi}{2}$  will result in minimal error as an approximation to an ideal CV cluster state. In addition, a second manifold defined by  $\theta_1 + \theta_2 = +\frac{\pi}{2}$  gives a similar minimum-error approximate CV cluster state but one which has weight  $-\tanh 2\alpha$ .

We can also create a version of this state as a canonical CV cluster state. In this case, using Eq. (2.29) gives

$$
\mathbf {Z} _ {2} = \left( \begin{array}{c c} i e ^ {- 2 r} & 1 \\ 1 & i e ^ {- 2 r} \end{array} \right). \tag {4.11}
$$

Both  $\mathbf{Z}_1^{\prime}$  and  $\mathbf{Z}_2$  are complete graphs on two nodes with self-loops, and while they are identical in the infinite-squeezing limit ( $\alpha \to \infty, r \to \infty$ ), the weightings on each are different for any finite amount of squeezing. While real-weighted ideal CV cluster-state graphs fail to illustrate this, the complex graphical formalism captures the difference.

The importance of this difference comes from the relative efficiency of each method in its use of squeezing resources. It is known that the canonically generated CV cluster states (e.g.,  $\mathbf{Z}_2$ ) are inefficient in this sense because the resulting state has single-mode-squeezed marginals [6,14]. An "efficient" state has  $\langle \hat{q}_j\hat{q}_j\rangle = \langle \hat{p}_j\hat{p}_j\rangle$  and  $\frac{1}{2}\langle \{\hat{q}_j,\hat{p}_j\} \rangle = 0$  for all modes  $j$ , which means that all of the quadrature correlations are between

different systems [56]. Recalling Eq. (2.20) for the covariance matrix in terms of  $\mathbf{Z}$ , these requirements become

$$
\left(\mathbf {U} + \mathbf {V U} ^ {- 1} \mathbf {V} - \mathbf {U} ^ {- 1}\right) _ {j j} = \left(\mathbf {V U} ^ {- 1}\right) _ {j j} = 0 \quad \forall j. \tag {4.12}
$$

This fails for  $\mathbf{Z}_2$  because

$$
\left(\mathbf {U} _ {2} + \mathbf {V} _ {2} \mathbf {U} _ {2} ^ {- 1} \mathbf {V} _ {2} - \mathbf {U} _ {2} ^ {- 1}\right) _ {j j} = e ^ {- 2 r}, \tag {4.13}
$$

which vanishes only in the infinite-squeezing limit  $(r\to \infty)$ . In contrast, Eq. (4.12) does hold for  $\mathbf{Z}_1^{\prime}$ . Thus, the  $\mathcal{H}$ -graph method of constructing a two-mode CV cluster state is efficient in its use of squeezing resources, while the canonical method is not. This fact cannot be seen in the real-weighted graphical formalism, but the complex formalism reveals it.

# D. Bipartite, self-inverse  $\mathcal{H}$  graphs

Note that for the two-mode squeezed state created using the  $\mathcal{H}$ -graph method,  $\mathbf{Z}_1' \to \mathbf{G}$  in the limit  $\alpha \to \infty$  of large squeezing. This is a general feature of  $\mathcal{H}$  graphs that are bipartite and self-inverse [22]. Such graphs include some with square-lattice topology that are useful for universal one-way QC [24]. Recalling Eq. (2.34), when  $\mathbf{G}$  is self-inverse (i.e.,  $\mathbf{G}^2 = \mathbf{I}$ ), the resulting  $\mathcal{H}$ -graph Gaussian pure state is

$$
\mathbf {Z} = i e ^ {- 2 \alpha \mathbf {G}} = i \cosh 2 \alpha \mathbf {I} - i \sinh 2 \alpha \mathbf {G}, \tag {4.14}
$$

In this case, the Gaussian graph  $\mathbf{Z}$  is just a rescaled version of  $\mathbf{G}$  with additional self-loops. When  $\mathbf{G}$  is also bipartite, it can be written as

$$
\mathbf {G} = \left( \begin{array}{c c} \mathbf {0} & \mathbf {G} _ {0} ^ {\mathrm {T}} \\ \mathbf {G} _ {0} & \mathbf {0} \end{array} \right), \tag {4.15}
$$

where  $\mathbf{G}_0$  is square and satisfies  $\mathbf{G}_0^{\mathrm{T}}\mathbf{G}_0 = \mathbf{G}_0\mathbf{G}_0^{\mathrm{T}} = \mathbf{I}$ , giving

$$
\mathbf {Z} = \left( \begin{array}{c c} i \cosh 2 \alpha \mathbf {I} & - i \sinh 2 \alpha \mathbf {G} _ {0} ^ {\mathrm {T}} \\ - i \sinh 2 \alpha \mathbf {G} _ {0} & i \cosh 2 \alpha \mathbf {I} \end{array} \right). \tag {4.16}
$$

Performing a Fourier transform on either set of nodes in the bipartition [21], using Eq. (3.20), gives

$$
\begin{array}{l} \mathbf {Z} ^ {\prime} = \left( \begin{array}{c c} i \operatorname {s e c h} 2 \alpha \mathbf {I} & \tanh 2 \alpha \mathbf {G} _ {0} ^ {\mathrm {T}} \\ \tanh 2 \alpha \mathbf {G} _ {0} & i \operatorname {s e c h} 2 \alpha \mathbf {I} \end{array} \right) \\ = i \operatorname {s e c h} 2 \alpha \mathbf {I} + \tanh 2 \alpha \mathbf {G}, \tag {4.17} \\ \end{array}
$$

which satisfies  $\mathbf{Z}' \to \mathbf{G}$  for large squeezing ( $\alpha \to \infty$ ), corresponding to an ideal CV cluster state with a graph the same as the  $\mathcal{H}$  graph,  $\mathbf{G}$  [22,24]. The two-mode squeezed state from Sec. IV C is the simplest special case of this construction.

We already know from Sec. IV B that phase shifting by multiples of  $\frac{\pi}{2}$  the nodes of a Gaussian pure state created using the  $\mathcal{H}$ -graph method of construction results in approximate CV cluster states with extremal approximation error  $\frac{1}{2}$  tr  $\mathbf{U}$ . In this case, the possible values of this error are

$$
\frac {1}{2} \operatorname {t r} \mathbf {U} = n \operatorname {s e c h} 2 \alpha + \left(N _ {b} - n\right) \cosh 2 \alpha , \tag {4.18}
$$

where  $N_{b}$  is the total number of nodes in one of the bipartitions (equal to half the total number of nodes in the graph). Clearly the minimum of these choices occurs when  $n = N_{b}$ , corresponding (nonuniquely) to the original prescription [21]: Fourier transform all nodes in one of the bipartitions, and

do nothing to those in the other set. This results in  $\frac{1}{2}\operatorname{tr} \mathbf{U} = N_b$  such  $2\alpha$ , which vanishes in the limit  $\alpha \to \infty$ .

Let us try to verify Eq. (4.4) for this choice:

$$
\begin{array}{l} \operatorname {I m} \left[ \left(\mathbf {I} + \mathbf {Z} ^ {\prime 2}\right) \circ \mathbf {Z} ^ {\prime} \right] \\ = \operatorname {I m} [ (2 \tanh  ^ {2} 2 \alpha \mathbf {I} + 2 i \operatorname {s e c h} 2 \alpha \tanh 2 \alpha \mathbf {G}) \\ \left. \circ (i \operatorname {s e c h} 2 \alpha \mathbf {I} + \tanh 2 \alpha \mathbf {G}) \right] \\ = 2 \operatorname {s e c h} 2 \alpha \tanh ^ {2} 2 \alpha \left( \begin{array}{c c} \mathbf {I} & \mathbf {G} _ {0} ^ {\mathrm {T}} \circ \mathbf {G} _ {0} ^ {\mathrm {T}} \\ \mathbf {G} _ {0} \circ \mathbf {G} _ {0} & \mathbf {I} \end{array} \right) \\ = 2 \operatorname {s e c h} 2 \alpha \tanh  ^ {2} 2 \alpha (\mathbf {I} + \mathbf {G}) \circ (\mathbf {I} + \mathbf {G}) \geqslant 0, \tag {4.19} \\ \end{array}
$$

where we have used the Schur product theorem  $(\mathbf{A} \circ \mathbf{B} \geqslant 0$  if  $\mathbf{A}, \mathbf{B} \geqslant 0)$ , and  $\mathbf{I} + \mathbf{G} \geqslant 0$  since  $\mathbf{G}$  is self-inverse. Therefore,  $\operatorname{Im}[(\mathbf{I} + \mathbf{Z}'^2) \circ \mathbf{Z}'] \geqslant 0$ , which we also found independently for the two-mode squeezed state in Sec. IV C. In some cases of interest, like the two-mode squeezed state, there will be a manifold of phase shifts that result in equivalent minimal-error CV cluster states made using a bipartite, self-inverse  $\mathcal{H}$  graph, thus accounting for the vanishing eigenvalue(s) in Eq. (4.19). While this does not rigorously prove that the extremal value of the approximation error in the  $\mathcal{H}$ -graph construction method for self-inverse, bipartite  $\mathcal{H}$  graphs [22,24] is a global minimum (or even, strictly speaking, a local minimum), these calculations suffice to illustrate the usefulness of the complex graphical formalism and suggest further avenues of research in this area.

# E. GHZ state

Also discussed in the literature [21,30,57,58] is the CV Greenberger-Horne-Zeilinger (GHZ) state, which can be made for any number of systems  $N$  using a complete  $\mathcal{H}$  graph with no self-loops:  $\mathbf{G} = \mathbf{I} - \mathbf{J}$ , where  $\mathbf{J}$  is the  $N\times N$  matrix of all 1's. We note that the diagonal of  $\mathbf{G}$  is not fixed for this state, but there are restrictions on it. To obtain a fully squeezed state in the limit  $\alpha \rightarrow \infty$ , an  $\mathcal{H}$  graph must be full rank [21] (i.e., all eigenvalues must be nonzero). To obtain GHZ entanglement, self-loops on the complete graph must be adjusted so that  $\mathbf{G}$  has at least one eigenvalue of each sign [30,57,58]. Since the spectrum of  $\mathbf{J}$  is  $(N,0,\dots ,0)$ , any  $\mathcal{H}$  graph that is of the form  $\beta \mathbf{I} - \mathbf{J}$  with  $\beta >0$  will suffice. We choose a hollow  $\mathbf{G}$  (i.e., zero diagonal, corresponding to  $\beta = 1$ ) for calculational convenience and because it has been studied specifically in the literature [57,58].

Since  $\mathbf{J}^k = N^{k - 1}\mathbf{J}$  for  $k\geqslant 1$  , the Gaussian graph associated with  $\mathbf{G}$  is

$$
\begin{array}{l} \mathbf {Z} = i e ^ {- 2 \alpha} e ^ {2 \alpha \mathbf {J}} = i e ^ {- 2 \alpha} \left(\mathbf {I} + \frac {\mathbf {J}}{N} \sum_ {k = 1} ^ {\infty} \frac {(2 \alpha N) ^ {k}}{k !}\right) \\ = i e ^ {- 2 \alpha} \left(\mathbf {I} + \frac {e ^ {2 \alpha N} - 1}{N} \mathbf {J}\right), \tag {4.20} \\ \end{array}
$$

As prescribed in Ref. [21], we wish to perform a Fourier transform on the first node using Eq. (3.20). To do this, we partition the graph as follows:

$$
\mathbf {Z} = \left( \begin{array}{c c c c c} t & r & r & \dots & r \\ r & W & w & \dots & w \\ r & w & W & \ddots & \vdots \\ \vdots & \vdots & \ddots & \ddots & w \\ r & w & \dots & w & W \end{array} \right), \tag {4.21}
$$

where

$$
\begin{array}{l} t = W = \frac {i e ^ {- 2 \alpha}}{N} (N + e ^ {2 \alpha N} - 1) \\ = \frac {i}{N \epsilon^ {N - 1}} [ 1 + (N - 1) \epsilon^ {N} ], \tag {4.22} \\ \end{array}
$$

$$
\begin{array}{l} r = w = \frac {i e ^ {- 2 \alpha}}{N} \left(e ^ {2 \alpha N} - 1\right) \\ = \frac {i}{N \epsilon^ {N - 1}} [ 1 - \epsilon^ {N} ], \tag {4.23} \\ \end{array}
$$

and where we have defined the small parameter  $\epsilon \coloneqq e^{-2\alpha}$  because we are eventually interested in the limit  $\alpha \to \infty$ . After applying Eq. (3.20), the resulting graph is

$$
\mathbf {Z} ^ {\prime} = \left( \begin{array}{c c c c c} t ^ {\prime} & r ^ {\prime} & r ^ {\prime} & \dots & r ^ {\prime} \\ r ^ {\prime} & W ^ {\prime} & w ^ {\prime} & \dots & w ^ {\prime} \\ r ^ {\prime} & w ^ {\prime} & W ^ {\prime} & \ddots & \vdots \\ \vdots & \vdots & \ddots & \ddots & w ^ {\prime} \\ r ^ {\prime} & w ^ {\prime} & \dots & w ^ {\prime} & W ^ {\prime} \end{array} \right), \tag {4.24}
$$

for which we will evaluate each term exactly, and also, to the lowest nontrivial order in  $\epsilon$ ,

$$
t ^ {\prime} = - \frac {1}{t} = \frac {i N \epsilon^ {N - 1}}{1 + (N - 1) \epsilon^ {N}} \simeq i N \epsilon^ {N - 1}, \tag {4.25}
$$

$$
r ^ {\prime} = - \frac {r}{t} = \frac {- 1 + \epsilon^ {N}}{1 + (N - 1) \epsilon^ {N}} \simeq - 1 + N \epsilon^ {N}, \tag {4.26}
$$

$$
W ^ {\prime} = W - \frac {r ^ {2}}{t} = i \epsilon \frac {2 + (N - 2) \epsilon^ {N}}{1 + (N - 1) \epsilon^ {N}} \simeq i 2 \epsilon , \tag {4.27}
$$

$$
w ^ {\prime} = w - \frac {r ^ {2}}{t} = i \epsilon \frac {1 - \epsilon^ {N}}{1 + (N - 1) \epsilon^ {N}} \simeq i \epsilon . \tag {4.28}
$$

In the infinite-squeezing limit ( $\alpha \to \infty$ , which corresponds to  $\epsilon \to 0$ ), all terms vanish except  $r'$ , resulting in an ideal CV cluster state with a star graph and  $-1$  for all edge weights:

$$
\mathbf {Z} ^ {\prime} \rightarrow \left(\begin{array}{c c c c}0&- 1&\dots&- 1\\- 1&0&\dots&0\\\vdots&\vdots&\ddots&\vdots\\- 1&0&\dots&0\end{array}\right). \tag {4.29}
$$

The phase-shifted node is the center of the star. A similar connection between complete graphs and star graphs is known for qubit cluster states [33,34]. We hope this formalism will be a useful tool in generalizing results like these (for qubits) to the realm of CVs.

That a Gaussian pure state generated from a complete  $\mathcal{H}$  graph corresponds—after a Fourier transform on one of the nodes—to a star-graph CV cluster state in the infinite-squeezing limit is already known [21], but the existing graph transformation rules for ideal CV cluster states [39] do not allow representation of the necessary Fourier transform operation. What is new here—and what this construction illustrates—is a unified presentation that includes approximate CV cluster states and  $\mathcal{H}$  graphs (through the exponential map), plus intermediate Gaussian pure states and the rules for transforming between them, which captures all of the details associated with finite squeezing wholly from within the graphical formalism.

# F. CV cluster states as ground states of a two-body Hamiltonian

Here we derive a (nonunique) Hamiltonian whose ground state is a particular CV cluster state<sup>11</sup> or, more generally, any given Gaussian graph  $\mathbf{Z}$ . The straightforward Hamiltonian to consider is

$$
H [ \mathbf {Z} ] = 2 \hat {\mathbf {a}} _ {\mathbf {Z}} ^ {\mathrm {H}} \hat {\mathbf {a}} _ {\mathbf {Z}}, \tag {4.30}
$$

which satisfies  $H[\mathbf{Z}]|\psi_{\mathbf{Z}}\rangle = 0$  by Eq. (2.35). This two-body Hamiltonian is also positive definite by construction, which means that  $|\psi_{\mathbf{Z}}\rangle$  is its ground state. Instead, however, we use

$$
\begin{array}{l} H [ \mathbf {Z} ] = (\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}) ^ {\mathrm {H}} (\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}) \\ = (\hat {\mathbf {p}} ^ {\mathrm {T}} - \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {Z} ^ {*}) (\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}) \\ = \hat {\mathbf {p}} ^ {\mathrm {T}} \hat {\mathbf {p}} - \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {Z} ^ {*} \hat {\mathbf {p}} - \hat {\mathbf {p}} ^ {\mathrm {T}} \mathbf {Z} \hat {\mathbf {q}} + \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {Z} ^ {*} \mathbf {Z} \hat {\mathbf {q}} \\ = \hat {\mathbf {p}} ^ {T} \hat {\mathbf {p}} - \hat {\mathbf {q}} ^ {T} (- i \mathbf {U} + \mathbf {V}) \hat {\mathbf {p}} - \hat {\mathbf {p}} ^ {T} (i \mathbf {U} + \mathbf {V}) \hat {\mathbf {q}} \\ + \hat {\mathbf {q}} ^ {\mathrm {T}} \left(\mathbf {U} ^ {2} + \mathbf {V} ^ {2} - i \mathbf {U V} + i \mathbf {V U}\right) \hat {\mathbf {q}}. \tag {4.31} \\ \end{array}
$$

This two-body Hamiltonian, too, satisfies  $H[\mathbf{Z}]|\psi_{\mathbf{Z}}\rangle = 0$  by Eq. (2.35), and it is positive definite by construction, which means that  $|\psi_{\mathbf{Z}}\rangle$  is its ground state. Reference [21] proves that any CV cluster state with a bipartite graph is equivalent to an  $\mathcal{H}$ -graph state up to phase shifts of  $-\frac{\pi}{2}$ . Restricting to these graphs simplifies the construction even further:

$$
H [ i \mathbf {U} ] = \hat {\mathbf {p}} ^ {\mathrm {T}} \hat {\mathbf {p}} + i \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {U} \hat {\mathbf {p}} - i \hat {\mathbf {p}} ^ {\mathrm {T}} \mathbf {U} \hat {\mathbf {q}} + \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {U} ^ {2} \hat {\mathbf {q}}. \tag {4.32}
$$

Considering that

$$
\begin{array}{l} i \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {U} \hat {\mathbf {p}} - i \hat {\mathbf {p}} ^ {\mathrm {T}} \mathbf {U} \hat {\mathbf {q}} \\ = i \sum_ {j k} \left(\hat {q} _ {j} U _ {j k} \hat {p} _ {k} - \hat {p} _ {j} U _ {j k} \hat {q} _ {k}\right) \\ = i \sum_ {j k} \left(\hat {q} _ {j} U _ {j k} \hat {p} _ {k} - \hat {p} _ {k} U _ {j k} \hat {q} _ {j}\right) \\ = i \sum_ {j k} [ \hat {q} _ {j}, \hat {p} _ {k} ] U _ {j k} \\ = - \sum_ {j} U _ {j j} = - \operatorname {t r} \mathbf {U} \tag {4.33} \\ \end{array}
$$

is just an overall shift in energy (which can be ignored), we have the result that

$$
H = \hat {\mathbf {p}} ^ {\mathrm {T}} \hat {\mathbf {p}} + \hat {\mathbf {q}} ^ {\mathrm {T}} \mathbf {U} ^ {2} \hat {\mathbf {q}} \tag {4.34}
$$

has an  $\mathcal{H}$ -graph-representable ground state (with  $\mathbf{G} \propto -\log \mathbf{U}$ ). Thus, for any desired CV cluster state with a bipartite graph [21], some Hamiltonian of this form exists that has the desired state as its ground state (up to phase shifts).

# G. Bipartite entanglement

A general  $N$ -mode Gaussian pure state may exhibit some form of multipartite entanglement. In this case, it is useful to consider the entanglement for any bipartite splitting of the state. Given an  $N$ -mode Gaussian pure state, we split the modes into two sets, one with  $n$  and the other with  $m$  modes,  $N = n + m$ . We wish to calculate the entanglement between the two sets.

Since the overall state is pure, we may use the entanglement entropy for this, which is simply the entropy of one of the subsystems with the other traced out. For a Gaussian pure state, the entanglement entropy is a simple function of the symplectic eigenvalues [61] of the covariance matrix corresponding to the nodes in question. The symplectic eigenvalues are similar to ordinary eigenvalues of a matrix, except that a symplectic product is taken between the matrix and its symplectic eigenvectors instead of the ordinary matrix product and the magnitude of the imaginary part is then taken. Thus, while the matrix equation  $\mathbf{M}\mathbf{v}_j = \lambda_j\mathbf{v}_j$  defines the ordinary eigenvalues of matrix  $\mathbf{M}$ , the following equation defines the eigenvalues associated with the symplectic product:

$$
\boldsymbol {\Sigma} \boldsymbol {\Omega} \mathbf {v} _ {j} = \lambda_ {j} \mathbf {v} _ {j}. \tag {4.35}
$$

Note the presence of the symplectic form  $\pmb{\Omega}$  in this relation. Further, note that the matrix  $\pmb{\Sigma}\pmb{\Omega}$  is not Hermitian, since we have  $(\pmb{\Sigma}\pmb{\Omega})^{\dagger} = \pmb{\Omega}^{\mathrm{T}}\pmb{\Sigma} = -\pmb{\Omega}\pmb{\Sigma}$ , but both  $\pmb{\Sigma}\pmb{\Omega}$  and  $\pmb{\Omega}\pmb{\Sigma}$  have the same eigenvalues (since they are related by a similarity transformation). Therefore, for an  $N$ -mode matrix, we obtain  $2N$  imaginary eigenvalues  $\lambda_{j\pm} = \pm i\sigma_{j}$ , which occur in conjugate pairs. The  $N$  symplectic eigenvalues are just the  $\sigma_{j} > 0$ .

We want the symplectic eigenvalues of the reduced density matrix, though, so we have to consider the covariance matrix truncated to the subset of  $n$  modes. Let  $\mathbf{P}$  be a matrix constructed in the following way: Create a diagonal matrix that has a 1 in the diagonal entries corresponding to the nodes of the set to be kept and 0's everywhere else; then, remove the all-0 rows. Also, let  $\bar{\mathbf{P}} = \begin{pmatrix} \mathbf{P} & \mathbf{0} \\ \mathbf{0} & \mathbf{P} \end{pmatrix}$ , which is also not a square matrix. Here,  $\mathbf{P}$  is an  $n \times N$  matrix, and so  $\bar{\mathbf{P}}$  is a  $2n \times 2N$  matrix.

The covariance matrix of the reduced state of  $n$  modes is then  $\tilde{\Sigma} \coloneqq \bar{\mathbf{P}}\boldsymbol{\Sigma}\bar{\mathbf{P}}^{\mathrm{T}}$ , a  $2n \times 2n$  matrix. Keep in mind that this truncated covariance matrix does not have a corresponding graph in our formalism, because it is generally not pure (if it were pure, then the original state would be trivially a product state). Since  $\tilde{\Omega} = \bar{\mathbf{P}}\boldsymbol{\Omega}\bar{\mathbf{P}}^{\mathrm{T}}$  is the symplectic form for the truncated set of modes, we seek the ordinary eigenvalues of  $\bar{\mathbf{P}}\boldsymbol{\Omega}\boldsymbol{\Sigma}\bar{\mathbf{P}}^{\mathrm{T}}$ .

Our goal is to find a simple way to use the graph  $\mathbf{Z}$  to read off the bipartite entanglement entropy across an arbitrary boundary dividing the graph into the two subsets of nodes. In particular, we would like to find an interpretation of the symplectic eigenvalues and, hence, the entanglement in terms of the shape and the weights of the given graph. For a general graph and arbitrary divisions into subsets of  $n$  and  $m$  modes, this interpretation is not so straightforward. However, for specific graphs and bipartite splittings, a simple, instructive connection between the entanglement and the graph can sometimes be found.

A particularly straightforward example is that of the canonical CV cluster states [5]. Canonical CV cluster states are of the form  $\mathbf{Z} = i\epsilon \mathbf{I} + \mathbf{V}$ , where  $\epsilon = e^{-2r}$ . As shown in Fig. 2, the imaginary self-loops represent the initial squeezing of each node, while matrix  $\mathbf{V}$  contains the real weights between neighboring nodes (corresponding to the strength of the  $C_Z$  gates, which also contain squeezing [15]). The covariance matrix for such a state is

$$
\boldsymbol {\Sigma} := \frac {1}{2 \epsilon} \left( \begin{array}{c c} \mathbf {I} & \mathbf {V} \\ \mathbf {V} & \epsilon^ {2} \mathbf {I} + \mathbf {V} ^ {2} \end{array} \right). \tag {4.36}
$$

This means that to obtain the ordinary eigenvalues of  $\bar{\mathbf{P}}\pmb {\Omega}\pmb{\Sigma}\bar{\mathbf{P}}^{\mathrm{T}}$  we need to solve

$$
\begin{array}{l} 0 = \det  \left( \begin{array}{c c} \tilde {\mathbf {V}} - \lambda \mathbf {I} & \epsilon^ {2} \mathbf {I} + \tilde {\mathbf {W}} \\ - \mathbf {I} & - \tilde {\mathbf {V}} - \lambda \mathbf {I} \end{array} \right) \\ = \det (\lambda^ {2} \mathbf {I} - \tilde {\mathbf {V}} ^ {2} + \epsilon^ {2} \mathbf {I} + \tilde {\mathbf {W}}), \tag {4.37} \\ \end{array}
$$

where  $\tilde{\mathbf{V}} = \mathbf{P}\mathbf{V}\mathbf{P}^{\mathrm{T}}$  and  $\tilde{\mathbf{W}} = \mathbf{P}\mathbf{V}^{2}\mathbf{P}^{\mathrm{T}}$ , and the second line follows because the bottom two blocks commute. Note that since  $\mathbf{I} - \mathbf{P}^{\mathrm{T}}\mathbf{P}$  is a projector,  $\tilde{\mathbf{W}} -\tilde{\mathbf{V}}^{2} = \mathbf{P}\mathbf{V}(\mathbf{I} - \mathbf{P}^{\mathrm{T}}\mathbf{P})\mathbf{V}\mathbf{P}^{\mathrm{T}}\geqslant 0$ , and thus we label the eigenvalues of  $\tilde{\mathbf{W}} -\tilde{\mathbf{V}}^{2}$  by  $\nu_{j}^{2}\geqslant 0$ . Equation (4.37) then gives  $\lambda_j^2 +\epsilon^2 = -\nu_j^2$ . The  $2n$  eigenvalues  $\mu_{j\pm}$  of  $\tilde{\pmb{\Omega}}\tilde{\pmb{\Sigma}}$  are therefore given by

$$
\mu_ {j \pm} = \pm \frac {\lambda_ {j}}{2 \epsilon} = \pm \frac {i}{2} \sqrt {1 + \frac {\nu_ {j} ^ {2}}{\epsilon^ {2}}}, \tag {4.38}
$$

which gives us the  $n$  symplectic eigenvalues of  $\tilde{\Sigma}$ :

$$
\sigma_ {j} = \frac {1}{2} \sqrt {1 + \frac {\nu_ {j} ^ {2}}{\epsilon^ {2}}} = \frac {1}{2} \sqrt {1 + e ^ {+ 4 r} \nu_ {j} ^ {2}}. \tag {4.39}
$$

The eigenvalues  $\nu_{j}^{2}$  of  $\tilde{\mathbf{W}} -\tilde{\mathbf{V}}^{2}$  contain the information about the graph in question. In particular, when we consider the bipartite entanglement between any single node  $k$  of the graph and the remaining nodes  $(n = 1,m = N - 1)$ , we have

$$
\tilde {\mathbf {V}} \mapsto \tilde {V} = V _ {k k}, \quad \tilde {\mathbf {W}} \mapsto \tilde {W} = \sum_ {l} V _ {k l} ^ {2}. \tag {4.40}
$$

As a result, we simply have to solve  $\lambda^2 +\epsilon^2 = -\sum_{\{l|l\neq k\}}V_{kl}^2$  leading to a single symplectic eigenvalue:

$$
\sigma = \frac {1}{2} \sqrt {1 + e ^ {+ 4 r} \sum_ {\{l \mid l \neq k \}} V _ {k l} ^ {2}}. \tag {4.41}
$$

In other words, besides the initial squeezing  $r$ , the entanglement between any node  $k$  and the rest of the graph is determined by the number of its neighbors and the strength of

the link with each neighbor. Only those "nodes" of the graph that have no neighbors at all would give  $\sigma = \frac{1}{2}$ , corresponding to a pure reduced state and, hence, no entanglement with the actual nodes of the graph. For any given  $r$ , however, any link with nonzero weight means  $\sigma > \frac{1}{2}$  and, thus, entanglement.

Quantitatively, both an increasing number of neighboring nodes and an increasing strength of the links enhances the entanglement, because the entropy grows with  $\sigma$ , and  $\sigma - \frac{1}{2}$  represents the mean excitation number of the reduced thermal state. For the special case of equal unit weights  $V_{kl} = 1$ , we have  $\sigma = \frac{1}{2}\sqrt{1 + e^{+4r}N_k}$ , where  $N_{k}$  represents the number of neighbors of node  $k$ . Thus, the maximum entanglement obtainable between a single node and the rest of the graph is determined by the maximal number of neighboring nodes, the so-called connectivity  $C := \max_k N_k$ . For constant connectivity, as in a 2D lattice with  $C = 4$ , the entropy will be bounded and does not increase with the size of the lattice. Only for an increasing connectivity do we get higher entropies, and in principle, the entanglement between a single node and the rest of the graph may grow unboundedly with the number of its links. This result is consistent with the bounds on the offline squeezing per node needed to create a canonical CV cluster state of constant connectivity [6].

# V. CONCLUSION

We have generalized weighted graphs for CV cluster states in a natural way to a graphical calculus for all Gaussian pure states. The mathematics behind this generalization is not new [44,45,53,62]. What goes beyond those references is interpreting the matrix formalism of Simon, Sudarshan, and Mukunda [44] as transformations on an undirected, complex-weighted graph. This would be a mathematic triviality if it were not for the fact that applying this graphical interpretation to approximate CV cluster states and letting the overall squeezing go to infinity results in exactly the same graphs as are already being used to represent ideal CV cluster states [4-6,14,21-24]. In addition, the graph transformation rules implied by the formalism immediately generalize all of the existing graph transformation rules [32,39,42] to any Gaussian pure state and limit to these rules in the (unphysical) case of ideal CV cluster states. It is these remarkable facts that make these results important.

This graphical formalism satisfies all five of the essential desired properties outlined in Sec. II B [items (1)-(5)]. We have also made headway on the three optional items listed subsequently [items (i)-(iii)]. Our achievements with the formalism thus far include using it for the following purposes:

(1) Incorporate all details of finite squeezing within the CV cluster-state graph (Sec. II F).  
(2) Distinguish between different approximants to a given ideal CV cluster state at the graphical level (Sec. II F).  
(3) Incorporate  $\mathcal{H}$  graphs [21-24] within the same graphical formalism through the exponential map (Sec. II G).  
(4) Generalize the nullifier formalism [6] to all Gaussian pure states (Sec. II H).  
(5) Use the nullifier formalism to define both an error matrix and a scalar approximation error for an approximate CV cluster state (Sec. II H).

(6) Define matrix and graphical transformation rules for a complete set of simple Gaussian unitary operations and quadrature measurements (Sec. III).  
(7) Define the "closest" ideal CV cluster state to a given Gaussian pure state (Sec. IV A).  
(8) Analyze the optimality of the  $\mathcal{H}$ -graph construction method with respect to this notion (Sec. IV B), including the specific examples of the two-mode squeezed state (Sec. IV C) and a useful subclass of  $\mathcal{H}$  graphs (Sec. IV D).  
(9) Demonstrate generation of a star-graph approximate CV cluster state from an approximate GHZ state made using an  $\mathcal{H}$  graph (Sec. IV E).  
(10) Identify classes of two-body Hamiltonians that have CV cluster states as their ground state (Sec. IV F).  
(11) Quantify bipartite entanglement in terms of the graphical formalism, with the explicit example of canonical CV cluster states (Sec. IV G).

We anticipate that this list will grow over time. Specifically, we expect that the formalism will serve well when considering the propagation and manipulation of quantum information through approximate CV cluster states using homodyne detection and development of computer software for visualizing the effects of Gaussian operations on CV cluster states, as well as other uses not yet discovered.

We conclude with a few words about the prospects of fault-tolerant QC using Gaussian approximate CV cluster states. Recent work [10] has demonstrated that all Gaussian approximants to ideal CV cluster states are inherently faulty when used for one-way QC simply due to the fact that they are finitely squeezed. This has led to suggestions (made in a private communication) that these results forbid a fault-tolerant implementation of this QC paradigm. This is not the case.

That CV cluster states are error-prone has been known since the beginning [5]. The main conclusion that should be drawn from Ref. [10] is that there is no "magic pill" to eliminate the effects of finite squeezing using a simple qubit (or other) encoding scheme. Instead, fault tolerance must be addressed from the very beginning because, unlike qubit cluster states, which remain physical in the limit of zero errors in preparation and use, CV cluster states are unphysical in this limit, since ideal states require infinite energy. This is not in any way a show-stopper, however, and the authors of Ref. [10] go to great lengths to show several possible approaches to error correction that do not fall victim to their no-go theorems. (It would be interesting to apply the matrix-product-state calculations from that paper to noisy qubit cluster states to see if analogous results are obtained in that context, to ensure that we are comparing apples with apples.) Fault tolerance in CV one-way QC remains an important open problem and an active area of research.

Note added in proof. After the completion of this work, new results appeared [63] addressing the question of fault tolerance in CV cluster states with a substantially different conclusion from that of Ref. [10].

# ACKNOWLEDGMENTS

We are grateful for discussions with and assistance from Daniel Gottesman, Rolando Somma, Jon Yard, Yeong-Cherng Liang, Andrew Doherty, and Stephen Bartlett. P.v.L. acknowledges the DFG for financial support through the Emmy Noether program. Research at Perimeter Institute is supported

by the Government of Canada through Industry Canada and by the Province of Ontario through the Ministry of Research & Innovation.

# APPENDIX A: DERIVATION OF THE COMPLEX-WEIGHTED GRAPH REPRESENTATION

Here we derive the connection between a Gaussian pure state and its complex-weighted graph  $\mathbf{Z}$ . There is a vast mathematical literature on the set of all allowable graphs  $\mathbf{Z}$ , known as the Siegel upper half-space. The main results for our purposes can be found in Ref. [53], with more details given in Ref. [44]. An extensive review of the Siegel upper half-space and its connection to the symplectic group can be found in the Ph.D. thesis by Freitas [62] and the references therein.

Definition. The graph corresponding to a Gaussian pure state is  $\mathbf{Z} := \langle \hat{\mathbf{q}}\hat{\mathbf{q}}^{\mathrm{T}}\rangle^{-1}\langle \hat{\mathbf{q}}\hat{\mathbf{p}}^{\mathrm{T}}\rangle$

This graph was defined in Eq. (2.27). We wish to prove several properties of all such graphs.

Theorem. Every graph corresponding to a Gaussian pure state is complex weighted, undirected, and unique and has a positive definite imaginary part.

Proof. Let  $\mathbf{Z}$  be a graph corresponding to a Gaussian pure state. That  $\mathbf{Z}$  is complex weighted and unique is guaranteed by the definition: expectation values of operator-valued matrices result in matrices of complex numbers, corresponding to a complex-weighted graph. It is unique for a given state because expectation values are uniquely determined by the state.

An undirected graph has a symmetric adjacency matrix. To show the symmetry of  $\mathbf{Z}$ , the second line of Eq. (2.27) is useful, and we repeat it here for reference:

$$
\mathbf {Z} = \frac {1}{2} \langle \hat {\mathbf {q}} \hat {\mathbf {q}} ^ {\mathrm {T}} \rangle^ {- 1} (i \mathbf {I} + \langle \{\hat {\mathbf {q}}, \hat {\mathbf {p}} ^ {\mathrm {T}} \} \rangle). \tag {A1}
$$

To prove the symmetry of  $\mathbf{Z}$  we refer to Eq. (2.16), which shows that any Gaussian pure state has a covariance matrix that is  $\frac{1}{2}$  times a symplectic matrix:

$$
2 \boldsymbol {\Sigma} = \mathbf {S} \mathbf {S} ^ {\mathrm {T}} \in \operatorname {S p} (2 N, \mathbb {R}), \tag {A2}
$$

since it is the product of a symplectic matrix  $\mathbf{S}$  and its transpose. While  $\mathbf{S}$  is not unique for a given Gaussian pure state,  $\pmb{\Sigma}$  is, and we partition it as follows:

$$
\boldsymbol {\Sigma} = \frac {1}{2} \left( \begin{array}{l l} \mathbf {A} & \mathbf {B} \\ \mathbf {B} ^ {\mathrm {T}} & \mathbf {D} \end{array} \right). \tag {A3}
$$

Being a covariance matrix,  $\pmb{\Sigma} = \pmb{\Sigma}^{\mathrm{T}} > 0$ . (Being the covariance matrix for a valid quantum state requires more than this [3], but we do not need it.) This implies immediately that  $\mathbf{A} = \mathbf{A}^{\mathrm{T}} > 0$ , and  $\mathbf{D} = \mathbf{D}^{\mathrm{T}} > 0$ . That  $2\pmb{\Sigma}$  is symplectic requires, additionally, that

$$
\begin{array}{l} \left( \begin{array}{c c} \mathbf {0} & \mathbf {I} \\ - \mathbf {I} & \mathbf {0} \end{array} \right) = \boldsymbol {\Omega} = 4 \boldsymbol {\Sigma} \boldsymbol {\Omega} \boldsymbol {\Sigma} \\ = \left( \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {B} ^ {\mathrm {T}} & \mathbf {D} \end{array} \right) \left( \begin{array}{c c} \mathbf {0} & \mathbf {I} \\ - \mathbf {I} & \mathbf {0} \end{array} \right) \left( \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {B} ^ {\mathrm {T}} & \mathbf {D} \end{array} \right) \\ = \left( \begin{array}{c c} \mathbf {A B} ^ {\mathrm {T}} - \mathbf {B A} & \mathbf {A D} - \mathbf {B} ^ {2} \\ (\mathbf {B} ^ {\mathrm {T}}) ^ {2} - \mathbf {D A} & \mathbf {B} ^ {\mathrm {T}} \mathbf {D} - \mathbf {D B} \end{array} \right). \tag {A4} \\ \end{array}
$$

From this we can see immediately that

$$
(\mathbf {B A}) ^ {\mathrm {T}} = \mathbf {B A}, \tag {A5a}
$$

$$
(\mathbf {D B}) ^ {\mathrm {T}} = \mathbf {D B}, \tag {A5b}
$$

$$
\mathbf {A} \mathbf {D} = \mathbf {I} + \mathbf {B} ^ {2}. \tag {A5c}
$$

From the definition of the covariance matrix, we have that  $\langle \hat{\mathbf{q}}\hat{\mathbf{q}}^{\mathrm{T}}\rangle = \mathbf{A}$ , and  $\frac{1}{2}\langle \{\hat{\mathbf{q}},\hat{\mathbf{p}}^{\mathrm{T}}\} \rangle = \mathbf{B}$ . That  $\mathbf{A} = \mathbf{A}^{\mathrm{T}} > 0$  guarantees immediately that  $\operatorname{Im}\mathbf{Z} = \mathbf{A}^{-1}$  exists and is also symmetric and positive definite. The only remaining item to prove is that  $\operatorname{Re}\mathbf{Z} = \mathbf{A}^{-1}\mathbf{B}$  is symmetric. Equation (A5a) gives

$$
\begin{array}{l} (\mathbf {B A}) ^ {\mathrm {T}} = \mathbf {B A} \Longrightarrow \mathbf {A} ^ {- 1} (\mathbf {B A}) ^ {\mathrm {T}} \mathbf {A} ^ {- 1} = \mathbf {A} ^ {- 1} \mathbf {B A A} ^ {- 1} \\ \Longrightarrow (\mathbf {A} ^ {- 1} \mathbf {B}) ^ {\mathrm {T}} = \mathbf {A} ^ {- 1} \mathbf {B}, \tag {A6} \\ \end{array}
$$

since  $\mathbf{A} = \mathbf{A}^{\mathrm{T}}$ . Therefore,  $\mathbf{Z}$  is an undirected graph.

Theorem. Every complex-weighted, undirected graph with a positive-definite imaginary part represents a unique Gaussian pure state (up to an arbitrary overall phase).

Proof. Let  $\mathbf{Z}$  be the graph in question. We will split it up into its real and imaginary parts as usual:  $\mathbf{Z} = i\mathbf{U} + \mathbf{V}$ , where  $\mathbf{U} = \mathbf{U}^{\mathrm{T}} > 0$ , and  $\mathbf{V} = \mathbf{V}^{\mathrm{T}}$ . To find the Gaussian pure state that  $\mathbf{Z}$  represents, we will construct a covariance matrix from it and prove that it satisfies the conditions to be a valid covariance matrix for a Gaussian pure state.

We now define

$$
\boldsymbol {\Sigma} _ {\mathbf {Z}} := \frac {1}{2} \left( \begin{array}{c c} \mathbf {U} ^ {- 1} & \mathbf {U} ^ {- 1} \mathbf {V} \\ \mathbf {V U} ^ {- 1} & \mathbf {U} + \mathbf {V U} ^ {- 1} \mathbf {V} \end{array} \right), \tag {A7}
$$

just as in Eq. (2.19). In this case, though, we need to prove that it is a valid covariance matrix for a Gaussian pure state given the assumptions made about  $\mathbf{Z}$ . A straightforward way to do this is to show that it is the result of conjugation of the ground-state covariance matrix  $\frac{1}{2}\mathbf{I}$  by a symplectic matrix (which necessarily represents a Gaussian unitary operation). We define

$$
\mathbf {S} _ {\mathbf {Z}} := \left( \begin{array}{c c} \mathbf {U} ^ {- 1 / 2} & \mathbf {0} \\ \mathbf {V U} ^ {- 1 / 2} & \mathbf {U} ^ {1 / 2} \end{array} \right), \tag {A8}
$$

paralleling Eq. (2.18). One can verify directly that  $\mathbf{S}_{\mathbf{Z}}\boldsymbol{\Omega}\mathbf{S}_{\mathbf{Z}}^{\mathrm{T}} = \boldsymbol{\Omega}$ , guaranteeing the symplectic nature of  $\mathbf{S}_{\mathbf{Z}}$ . Then we have

$$
\boldsymbol {\Sigma} _ {\mathbf {Z}} = \frac {1}{2} \mathbf {S} _ {\mathbf {Z}} \mathbf {S} _ {\mathbf {Z}} ^ {\mathrm {T}}, \tag {A9}
$$

which shows that  $\mathbf{Z}$  represents a valid Gaussian pure state.

To show uniqueness of the state represented (up to overall phase), we assume that there exists another covariance matrix  $\tilde{\Sigma}_{\mathbf{Z}} \neq \Sigma_{\mathbf{Z}}$  that is represented by  $\mathbf{Z}$ . Recalling Eq. (A5c), which holds for an arbitrary pure-Gaussian-state covariance matrix, we write the blocks of  $\tilde{\Sigma}_{\mathbf{Z}}$  as

$$
\tilde {\boldsymbol {\Sigma}} _ {\mathbf {Z}} = \frac {1}{2} \left( \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {B} ^ {\mathrm {T}} & \mathbf {A} ^ {- 1} + \mathbf {A} ^ {- 1} \mathbf {B} ^ {2} \end{array} \right). \tag {A10}
$$

Using Eq. (A1), the graph representing this state is  $\mathbf{A}^{-1}(i\mathbf{I} + \mathbf{B})$ . By assumption, this must be the same as  $\mathbf{Z} = i\mathbf{U} + \mathbf{V}$  which gives  $\mathbf{A} = \mathbf{U}^{-1}$  and  $\mathbf{B} = \mathbf{U}^{-1}\mathbf{V}$ . Plugging these back into Eq. (A10) shows that  $\tilde{\Sigma}_{\mathbf{Z}} = \Sigma_{\mathbf{Z}}$ , in contradiction with the assumption. Therefore,  $\Sigma_{\mathbf{Z}}$  is unique for a given graph  $\mathbf{Z}$ .

Theorem. The transformation law for graphs representing Gaussian pure states under Gaussian unitary operations is given by Eq. (2.24).

Proof. Since we have a unique way of passing from the covariance matrix for a Gaussian pure state to its graph and back again, our method will be to show the action of an arbitrary symplectic operation on the covariance matrix and then extract the new graph from it. Rather than dealing with the covariance matrix alone, it will be useful instead to consider the combination

$$
\begin{array}{l} \boldsymbol {\Sigma} _ {\mathbf {Z}} - \frac {i}{2} \boldsymbol {\Omega} = \frac {1}{2} \left( \begin{array}{c c} \mathbf {U} ^ {- 1} & \mathbf {U} ^ {- 1} \mathbf {V} - i \mathbf {I} \\ \mathbf {V U} ^ {- 1} + i \mathbf {I} & \mathbf {U} + \mathbf {V U} ^ {- 1} \mathbf {V} \end{array} \right) \\ = \frac {1}{2} \left( \begin{array}{c} \mathbf {I} \\ \mathbf {Z} \end{array} \right) \mathbf {U} ^ {- 1} (\mathbf {I} \quad \mathbf {Z} ^ {*}) \\ = \frac {1}{2} \binom {\mathbf {I}} {\mathbf {Z}} \left[ \frac {1}{2 i} (\mathbf {Z} - \mathbf {Z} ^ {*}) \right] ^ {- 1} (\mathbf {I} \quad \mathbf {Z} ^ {*}) \\ = i \binom {\mathbf {I}} {\mathbf {Z}} \left[ \left(\mathbf {I} \quad \mathbf {Z} ^ {*}\right) \boldsymbol {\Omega} \binom {\mathbf {I}} {\mathbf {Z}} \right] ^ {- 1} \left(\mathbf {I} \quad \mathbf {Z} ^ {*}\right), \tag {A11} \\ \end{array}
$$

and similarly for  $\pmb{\Sigma}_{\mathbf{Z}^{\prime}} - \frac{i}{2}\pmb{\Omega}$ , with  $\mathbf{Z}\mapsto \mathbf{Z}'$ . Equation (2.24) requires that  $\pmb{\Sigma}_{\mathbf{Z}^{\prime}} = \mathbf{S}\pmb{\Sigma}_{\mathbf{Z}}\mathbf{S}^{\mathrm{T}}$ , with

$$
\mathbf {S} = \left( \begin{array}{l l} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right) \tag {A12}
$$

from Eq. (2.23), repeated here for reference. Using the symplectic property of  $\mathbf{S}$  allows us to write

$$
\begin{array}{l} \boldsymbol {\Sigma} _ {\mathbf {Z} ^ {\prime}} - \frac {i}{2} \boldsymbol {\Omega} = \mathbf {S} \left(\boldsymbol {\Sigma} _ {\mathbf {Z}} - \frac {i}{2} \boldsymbol {\Omega}\right) \mathbf {S} ^ {\mathrm {T}} \\ = i \mathbf {S} \binom {\mathbf {I}} {\mathbf {Z}} \left[ (\mathbf {I} \quad \mathbf {Z} ^ {*}) \boldsymbol {\Omega} \binom {\mathbf {I}} {\mathbf {Z}} \right] ^ {- 1} (\mathbf {I} \quad \mathbf {Z} ^ {*}) \mathbf {S} ^ {\mathrm {T}} \\ = i \mathbf {S} \binom {\mathbf {I}} {\mathbf {Z}} \left[ \begin{array}{l l} (\mathbf {I} & \mathbf {Z} ^ {*}) \mathbf {S} ^ {\mathrm {T}} \boldsymbol {\Omega} \mathbf {S} \binom {\mathbf {I}} {\mathbf {Z}} \end{array} \right] ^ {- 1} \left( \begin{array}{l l} \mathbf {I} & \mathbf {Z} ^ {*} \end{array} \right) \mathbf {S} ^ {\mathrm {T}}. \tag {A13} \\ \end{array}
$$

Note that

$$
\mathbf {S} \binom {\mathbf {I}} {\mathbf {Z}} = \binom {\mathbf {A} + \mathbf {B Z}} {\mathbf {C} + \mathbf {D Z}} = \binom {\mathbf {I}} {\tilde {\mathbf {Z}}} (\mathbf {A} + \mathbf {B Z}), \tag {A14}
$$

where  $\tilde{\mathbf{Z}} = (\mathbf{C} + \mathbf{D}\mathbf{Z})(\mathbf{A} + \mathbf{B}\mathbf{Z})^{-1}$ . The fact that  $\operatorname{Im}\mathbf{Z} > 0$  guarantees that the inverse exists (unless  $\mathbf{B} = \mathbf{0}$ , in which case invertibility of  $\mathbf{S}$  guarantees that  $\mathbf{A}^{-1}$  exists). Equation (2.24) then amounts to the claim that  $\mathbf{Z}' = \tilde{\mathbf{Z}}$  and, also, that  $\tilde{\mathbf{Z}}$  satisfies all the requirements for representing a Gaussian pure state (i.e., symmetry and positive-definite imaginary part).

To show the symmetry of  $\tilde{\mathbf{Z}}$ , we use a trick similar to that used in Eq. (A13):

$$
\begin{array}{l} \mathbf {0} = \mathbf {Z} - \mathbf {Z} ^ {\mathrm {T}} = (\mathbf {I} \quad \mathbf {Z} ^ {\mathrm {T}}) \Omega \binom {\mathbf {I}} {\mathbf {Z}} = (\mathbf {I} \quad \mathbf {Z} ^ {\mathrm {T}}) \mathbf {S} ^ {\mathrm {T}} \boldsymbol {\Omega} \mathbf {S} \binom {\mathbf {I}} {\mathbf {Z}} \\ = (\mathbf {A} + \mathbf {B Z}) ^ {\mathrm {T}} (\tilde {\mathbf {Z}} - \tilde {\mathbf {Z}} ^ {\mathrm {T}}) (\mathbf {A} + \mathbf {B Z}). \tag {A15} \\ \end{array}
$$

Since  $(\mathbf{A} + \mathbf{B}\mathbf{Z})$  is invertible,  $\tilde{\mathbf{Z}} = \tilde{\mathbf{Z}}^{\mathrm{T}}$ . Similarly, to show that  $\operatorname{Im}\tilde{\mathbf{Z}} > 0$ , we calculate

$$
\begin{array}{l} \operatorname {I m} \mathbf {Z} = \frac {1}{2 i} (\mathbf {Z} - \mathbf {Z} ^ {*}) = \frac {1}{2 i} (\mathbf {I} \quad \mathbf {Z} ^ {*}) \boldsymbol {\Omega} \left( \begin{array}{c} \mathbf {I} \\ \mathbf {Z} \end{array} \right) \\ = \frac {1}{2 i} (\mathbf {I} \quad \mathbf {Z} ^ {*}) \mathbf {S} ^ {\mathrm {T}} \boldsymbol {\Omega} \mathbf {S} \left( \begin{array}{c} \mathbf {I} \\ \mathbf {Z} \end{array} \right) \\ \end{array}
$$

$$
\begin{array}{l} = \frac {1}{2 i} (\mathbf {A} + \mathbf {B Z}) ^ {\mathrm {H}} (\tilde {\mathbf {Z}} - \tilde {\mathbf {Z}} ^ {*}) (\mathbf {A} + \mathbf {B Z}) \\ = (\mathbf {A} + \mathbf {B Z}) ^ {\mathrm {H}} (\operatorname {I m} \tilde {\mathbf {Z}}) (\mathbf {A} + \mathbf {B Z}). \tag {A16} \\ \end{array}
$$

Inverting this relation verifies that  $(\operatorname{Im} \mathbf{Z} > 0) \Longrightarrow (\operatorname{Im} \tilde{\mathbf{Z}} > 0)$ .

We have shown that  $\tilde{\mathbf{Z}}$  satisfies the requirements for representing a Gaussian pure state. All that is left to show is that  $\mathbf{Z}' = \tilde{\mathbf{Z}}$ . To do this, we first take the conjugate transpose of Eq. (A14), giving

$$
(\mathbf {I} \quad \mathbf {Z} ^ {*}) \mathbf {S} ^ {\mathrm {T}} = (\mathbf {A} ^ {\mathrm {T}} + \mathbf {Z} ^ {*} \mathbf {B} ^ {\mathrm {T}}) (\mathbf {I} \quad \tilde {\mathbf {Z}} ^ {*}). \tag {A17}
$$

Plugging Eqs. (A14) and (A17) into Eq. (A13) and canceling the appropriate factors gives

$$
\boldsymbol {\Sigma} _ {\mathbf {Z} ^ {\prime}} - \frac {i}{2} \boldsymbol {\Omega} = i \binom {\mathbf {I}} {\tilde {\mathbf {Z}}} \left[ \left(\mathbf {I} \quad \tilde {\mathbf {Z}} ^ {*}\right) \boldsymbol {\Omega} \binom {\mathbf {I}} {\tilde {\mathbf {Z}}} \right] ^ {- 1} \left(\mathbf {I} \quad \tilde {\mathbf {Z}} ^ {*}\right). \tag {A18}
$$

Clearly,  $\tilde{\mathbf{Z}}$  appears everywhere that  $\mathbf{Z}'$  should appear. The reader can check that solving this equation for  $\boldsymbol{\Sigma}_{\mathbf{Z}'}$  and extracting its graph  $\mathbf{Z}' = \langle \hat{\mathbf{q}}\hat{\mathbf{q}}^{\mathrm{T}}\rangle^{-1}\langle \hat{\mathbf{q}}\hat{\mathbf{p}}^{\mathrm{T}}\rangle$  does, in fact, show that  $\mathbf{Z}' = \tilde{\mathbf{Z}}$ . Since the graph for a Gaussian state is unique, this verifies Eq. (2.24). This transformation law is called a generalized Möbius transformation, and the interested reader is directed to Ref. [62] for a more in-depth mathematical analysis.

# APPENDIX B: DERIVATION OF THE CLOSEST CV CLUSTER STATE TO A GIVEN GAUSSIAN PURE STATE

There are other matrix models for Gaussian pure states besides the one we are using here. One of these, based on the Siegel disc [62], is useful for these calculations. (We forgo presentation of the entire model, referring the interested reader to Ref. [62] and references therein.) Based on this model, we define

$$
\begin{array}{l} \mathbf {K} := (\mathbf {I} + i \mathbf {Z}) (\mathbf {I} - i \mathbf {Z}) ^ {- 1} \\ = (\mathbf {I} \quad i \mathbf {I}) \binom {\mathbf {I}} {\mathbf {Z}} \left[ (\mathbf {I} \quad - i \mathbf {I}) \binom {\mathbf {I}} {\mathbf {Z}} \right] ^ {- 1}. \tag {B1} \\ \end{array}
$$

We also need the following:

$$
\mathbf {I} + \mathbf {K} = [ (\mathbf {I} - i \mathbf {Z}) + (\mathbf {I} + i \mathbf {Z}) ] (\mathbf {I} - i \mathbf {Z}) ^ {- 1} = 2 (\mathbf {I} - i \mathbf {Z}) ^ {- 1}, \tag {B2}
$$

as well as

$$
\mathbf {I} - i \mathbf {Z} = 2 (\mathbf {I} + \mathbf {K}) ^ {- 1}. \tag {B3}
$$

Note that since  $\mathbf{I} + \mathbf{K}$  is symmetric, so is  $\mathbf{K}$ . We repeat Eq. (4.1) here for reference:

$$
\mathbf {S} _ {\theta} = \left( \begin{array}{c c} \cos \theta & \sin \theta \\ - \sin \theta & \cos \theta \end{array} \right), \tag {B4}
$$

where  $\pmb{\theta} = \mathrm{diag}(\theta_1, \dots, \theta_N)$ . We can derive the transformation law for  $\mathbf{K}$  with respect to these phase shifts [cf. Eq. (A14)]:

$$
\begin{array}{l} \mathbf {K} ^ {\prime} = (\mathbf {I} \quad i \mathbf {I}) \left( \begin{array}{c} \mathbf {I} \\ \mathbf {Z} ^ {\prime} \end{array} \right) \left[ \begin{array}{c c} (\mathbf {I} & - i \mathbf {I}) \binom {\mathbf {I}} {\mathbf {Z} ^ {\prime}} \end{array} \right] ^ {- 1} \\ = (\mathbf {I} \quad i \mathbf {I}) \mathbf {S} _ {\theta} \left( \begin{array}{c} \mathbf {I} \\ \mathbf {Z} \end{array} \right) \left[ \begin{array}{c c} (\mathbf {I} & - i \mathbf {I}) \mathbf {S} _ {\theta} \left( \begin{array}{c} \mathbf {I} \\ \mathbf {Z} \end{array} \right) \end{array} \right] ^ {- 1} \\ \end{array}
$$

$$
\begin{array}{l} = e ^ {- i \theta} (\mathbf {I} \quad i \mathbf {I}) \left( \begin{array}{c} \mathbf {I} \\ \mathbf {Z} \end{array} \right) \left[ \begin{array}{c c} e ^ {i \theta} (\mathbf {I} & - i \mathbf {I}) \binom {\mathbf {I}} {\mathbf {Z}} \end{array} \right] ^ {- 1} \\ = e ^ {- i \theta} \mathbf {K} e ^ {- i \theta}. \tag {B5} \\ \end{array}
$$

An extremum of  $\frac{1}{2}\operatorname {tr}\mathbf{U}^{\prime}$  occurs when  $\partial_j$  tr  $\mathbf{U}' = \mathbf{0}$ , where  $\partial_j\coloneqq \frac{\partial}{\partial\theta_j}$ . Let us calculate the left-hand side:

$$
\begin{array}{l} \partial_ {j} \operatorname {t r} \mathbf {U} ^ {\prime} = \partial_ {j} \operatorname {t r} \left(\mathbf {I} + \mathbf {U} ^ {\prime}\right) = \frac {1}{2} \partial_ {j} \operatorname {t r} \left(\mathbf {I} - i \mathbf {Z} ^ {\prime}\right) + c. c. \\ = \partial_ {j} \operatorname {t r} \left[ \left(\mathbf {I} + \mathbf {K} ^ {\prime}\right) ^ {- 1} \right] + \mathrm {c . c .} \\ = \operatorname {t r} \{- (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 1} [ \partial_ {j} (\mathbf {I} + \mathbf {K} ^ {\prime}) ] (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 1} \} + c. c. \\ = \operatorname {t r} \{- (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 1} (- i) e ^ {- i \theta_ {j}} \mathbf {K} e ^ {- i \theta} (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 1} \} \\ + \operatorname {t r} \{\text {t r a n s p o s e} \} + c. c. \\ = 2 i \operatorname {t r} \left\{\left(\mathbf {I} + \mathbf {K} ^ {\prime}\right) ^ {- 1} e ^ {- i \theta_ {j}} \mathbf {K} e ^ {- i \theta} \left(\mathbf {I} + \mathbf {K} ^ {\prime}\right) ^ {- 1} \right\} + c. c. \\ = 2 i \left[ \mathbf {K} ^ {\prime} \left(\mathbf {I} + \mathbf {K} ^ {\prime}\right) ^ {- 2} \right] _ {j j} + \mathrm {c . c .}, \tag {B6} \\ \end{array}
$$

where c.c. stands for complex conjugate, and all entries of  $\theta_{j}$  are 0 except for the  $(j,j)\mathrm{th}$ , which equals  $\theta_{j}$ . We also need the following:

$$
\begin{array}{l} \mathbf {K} ^ {\prime} (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 2} \\ = (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 1} [ \mathbf {I} - (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 1} ] = (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 1} - (\mathbf {I} + \mathbf {K} ^ {\prime}) ^ {- 2} \\ = \frac {1}{2} (\mathbf {I} - i \mathbf {Z} ^ {\prime}) - \frac {1}{4} (\mathbf {I} - i \mathbf {Z} ^ {\prime}) ^ {2} = \frac {1}{4} (\mathbf {I} + \mathbf {Z} ^ {\prime 2}). \tag {B7} \\ \end{array}
$$

Then

$$
\partial_ {j} \operatorname {t r} \mathbf {U} ^ {\prime} = \frac {i}{2} \left(\mathbf {I} + \mathbf {Z} ^ {\prime 2}\right) _ {j j} + \mathrm {c . c .} = - \operatorname {I m} \left(\mathbf {Z} ^ {\prime 2}\right) _ {j j} = - \left(\mathbf {U} ^ {\prime} \mathbf {V} ^ {\prime}\right) _ {j j}. \tag {B8}
$$

Setting this to 0 for an extremum verifies Eq. (4.3).

To show that we have a minimum rather than just an extremum, the Hessian of  $\operatorname{tr} \mathbf{U}'$  must be positive definite. The Hessian matrix has entries

$$
\begin{array}{l} \partial_ {k} \partial_ {j} \operatorname {t r} \mathbf {U} ^ {\prime} = \frac {i}{2} \partial_ {k} \left(\mathbf {I} + \mathbf {Z} ^ {\prime 2}\right) _ {j j} + \mathrm {c . c .} \\ = \frac {i}{2} \partial_ {k} \left[ \left(\mathbf {I} + i \mathbf {Z} ^ {\prime}\right) \left(\mathbf {I} - i \mathbf {Z} ^ {\prime}\right) \right] _ {j j} + c. c. \tag {B9} \\ \end{array}
$$

In addition to Eq. (B3), we can find another similar relation by inverting Eq. (B1):

$$
\begin{array}{l} \mathbf {I} + \mathbf {K} ^ {- 1} = [ (\mathbf {I} + i \mathbf {Z}) + (\mathbf {I} - i \mathbf {Z}) ] (\mathbf {I} + i \mathbf {Z}) ^ {- 1} \\ = 2 (\mathbf {I} + i \mathbf {Z}) ^ {- 1}, \tag {B10} \\ \end{array}
$$

and thus, also,

$$
\mathbf {I} + i \mathbf {Z} = 2 (\mathbf {I} + \mathbf {K} ^ {- 1}) ^ {- 1}, \tag {B11}
$$

and similarly for the primed matrices. We now define the placeholder matrix:

$$
\mathbf {Q} ^ {\prime} := \left(\mathbf {I} + \mathbf {K} ^ {\prime - 1}\right) \left(\mathbf {I} + \mathbf {K} ^ {\prime}\right) = 2 \mathbf {I} + \mathbf {K} ^ {\prime - 1} + \mathbf {K} ^ {\prime}. \tag {B12}
$$

Note that

$$
\mathbf {I} + \mathbf {Z} ^ {\prime 2} = 4 \mathbf {Q} ^ {\prime - 1}. \tag {B13}
$$

The partial derivatives of  $\mathbf{Q}'$  are given by

$$
\begin{array}{l} \partial_ {k} \mathbf {Q} ^ {\prime} = \partial_ {k} \mathbf {K} ^ {\prime} + \partial_ {k} \mathbf {K} ^ {\prime - 1} = \partial_ {k} \mathbf {K} ^ {\prime} - \mathbf {K} ^ {\prime - 1} (\partial_ {k} \mathbf {K} ^ {\prime}) \mathbf {K} ^ {\prime - 1} \\ = - i \pi_ {k} \left(\mathbf {K} ^ {\prime} - \mathbf {K} ^ {\prime - 1}\right) - i \left(\mathbf {K} ^ {\prime} - \mathbf {K} ^ {\prime - 1}\right) \pi_ {k}, \tag {B14} \\ \end{array}
$$

where the  $(k,k)$ th entry of  $\pi_k$  equals 1, while all others are 0. We can plug these results into Eq. (B9):

$$
\begin{array}{l} \partial_ {k} \partial_ {j} \operatorname {t r} \mathbf {U} ^ {\prime} = 2 i \operatorname {t r} \left[ \boldsymbol {\pi} _ {j} \partial_ {k} \mathbf {Q} ^ {\prime - 1} \right] + c. c. \\ = - 2 i \operatorname {t r} \left[ \boldsymbol {\pi} _ {j} \mathbf {Q} ^ {\prime - 1} \left(\partial_ {k} \mathbf {Q} ^ {\prime}\right) \mathbf {Q} ^ {\prime - 1} \right] + c. c. \\ = - 4 \operatorname {t r} \left[ \boldsymbol {\pi} _ {j} \mathbf {Q} ^ {\prime - 1} \boldsymbol {\pi} _ {k} \left(\mathbf {K} ^ {\prime} - \mathbf {K} ^ {\prime - 1}\right) \mathbf {Q} ^ {\prime - 1} \right] + \mathrm {c . c .} \\ = - 4 \operatorname {t r} \left\{\boldsymbol {\pi} _ {j} \mathbf {Q} ^ {\prime - 1} \boldsymbol {\pi} _ {k} [ (\mathbf {I} + \mathbf {K} ^ {\prime}) \mathbf {Q} ^ {\prime - 1} \right. \\ - \left(\mathbf {I} + \mathbf {K} ^ {\prime - 1}\right) \mathbf {Q} ^ {\prime - 1} ] \} \} + c. c. \\ = - 4 \operatorname {t r} \left\{\boldsymbol {\pi} _ {j} \mathbf {Q} ^ {\prime - 1} \boldsymbol {\pi} _ {k} \left[ \left(\mathbf {I} + \mathbf {K} ^ {\prime - 1}\right) ^ {- 1} \right. \right. \\ - \left(\mathbf {I} + \mathbf {K} ^ {\prime}\right) ^ {- 1} ] \} + c. c. \\ = - 2 \operatorname {t r} \left\{\pi_ {j} \mathbf {Q} ^ {\prime - 1} \boldsymbol {\pi} _ {k} \left[ (\mathbf {I} + i \mathbf {Z} ^ {\prime}) - (\mathbf {I} - i \mathbf {Z} ^ {\prime}) \right] \right\} + c. c. \\ = - 4 i \operatorname {t r} \left(\boldsymbol {\pi} _ {j} \mathbf {Q} ^ {\prime - 1} \boldsymbol {\pi} _ {k} \mathbf {Z} ^ {\prime}\right) + c. c. \\ = 2 \operatorname {I m} \operatorname {t r} \left[ \boldsymbol {\pi} _ {j} \left(\mathbf {I} + \mathbf {Z} ^ {\prime 2}\right) \boldsymbol {\pi} _ {k} \mathbf {Z} ^ {\prime} \right] \\ = 2 \operatorname {I m} \left[ \left(\mathbf {I} + \mathbf {Z} ^ {\prime 2}\right) _ {j k} \mathbf {Z} _ {k j} ^ {\prime} \right] \\ = 2 \operatorname {I m} \left[ \left(\mathbf {I} + \mathbf {Z} ^ {\prime 2}\right) \circ \mathbf {Z} ^ {\prime} \right] _ {j k}, \tag {B15} \\ \end{array}
$$

where  $\circ$  represents the Hadamard (entrywise) product of two matrices. Requiring the matrix with these entries to be positive definite verifies Eq. (4.4).

# APPENDIX C: STABILIZERS FOR GAUSSIAN PURE STATES

To find the stabilizer operators for the finitely squeezed, canonical CV cluster states, we start by constructing the stabilizer of the vacuum state  $|0\rangle$  of a single mode  $\hat{a}_k$  [45]. For the dimensionless quadrature operators  $\hat{q}$  and  $\hat{p}$ , where  $\hat{a} = \frac{1}{\sqrt{2}} (\hat{q} + i \hat{p})$ , we obtain

$$
| 0 \rangle = \exp (\alpha \hat {a} _ {k}) | 0 \rangle = \exp \left[ \frac {\alpha}{\sqrt {2}} (\hat {q} _ {k} + i \hat {p} _ {k}) \right] | 0 \rangle . \tag {C1}
$$

Further, from this we need the stabilizer for a single-mode-squeezed state  $\hat{S} (r_k)|0\rangle$ , with a squeezing parameter  $r_k > 0$  and a  $\hat{q}$ -squeezing operator  $\hat{S} (r_k) = \exp [\frac{i}{2} r_k(\hat{q}_k\hat{p}_k + \hat{p}_k\hat{q}_k)]$ . The stabilizer equation can be written as

$$
\begin{array}{l} \hat {S} (r _ {k}) | 0 \rangle = \hat {S} (r _ {k}) \exp \left[ \frac {\alpha}{\sqrt {2}} (\hat {q} _ {k} + i \hat {p} _ {k}) \right] \hat {S} ^ {\dagger} (r _ {k}) \hat {S} (r _ {k}) | 0 \rangle \\ = \exp \left[ \frac {\alpha}{\sqrt {2}} \left(e ^ {+ r _ {k}} \hat {q} _ {k} + i e ^ {- r _ {k}} \hat {p} _ {k}\right) \right] \hat {S} \left(r _ {k}\right) | 0 \rangle . \tag {C2} \\ \end{array}
$$

In the case of momentum squeezing, with  $\hat{S} (-r_k)$ , we have

$$
\begin{array}{l} \hat {S} (- r _ {k}) | 0 \rangle = \hat {S} (- r _ {k}) \exp \left[ \frac {\alpha}{\sqrt {2}} (\hat {q} _ {k} + i \hat {p} _ {k}) \right] \hat {S} ^ {\dagger} (- r _ {k}) \hat {S} (- r _ {k}) | 0 \rangle \\ = \exp \left[ \frac {\alpha}{\sqrt {2}} \left(e ^ {- r _ {k}} \hat {q} _ {k} + i e ^ {+ r _ {k}} \hat {p} _ {k}\right) \right] \hat {S} (- r _ {k}) | 0 \rangle . \tag {C3} \\ \end{array}
$$

Let us rewrite this as

$$
\exp \left(- \frac {1}{4} \alpha^ {2}\right) \hat {X} _ {k} \left(- \frac {\alpha}{\sqrt {2}} e ^ {+ r _ {k}}\right) \hat {Z} _ {k} \left(- i \frac {\alpha}{\sqrt {2}} e ^ {- r _ {k}}\right), \tag {C4}
$$

formally using the Weyl-Heisenberg shift operators  $\hat{X}(s) = e^{-is\hat{p}}$  and  $\hat{Z}(s) = e^{is\hat{q}}$ . Now we define  $\alpha \coloneqq -\sqrt{2}e^{-r_k}s$  such that the momentum-squeezed stabilizer becomes

$$
\exp \left(- \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \hat {X} _ {k} (s) \hat {Z} _ {k} \left(i e ^ {- 2 r _ {k}} s\right). \tag {C5}
$$

In the limit of infinite  $p$  squeezing ( $r_k \to \infty$ ), this operator approaches  $\hat{X}_k(s)$ , which stabilizes the 0-eigenstate  $|0\rangle_{p_k}$ , with  $\hat{X}_k(s)|0\rangle_{p_k} = |0\rangle_{p_k}$  for all  $s \in \mathbb{R}$ , as expected.

Now we can proceed to create CV cluster states in the canonical way: by pairwise applying the  $C_Z$  gates, indicated as  $\hat{C}_Z^{kl}$  for a link between node  $k$  and node  $l$ . The  $N$  stabilizers of the initial  $N$  momentum-squeezed modes, shown in Eq. (C5), with  $k = 1,2,\dots ,N$ , are then transformed for each interaction with neighbor  $l$  as

$$
\begin{array}{l} \exp \left(- \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \hat {C} _ {Z} ^ {k l} \hat {X} _ {k} (s) \hat {C} _ {Z} ^ {k l \dagger} \hat {C} _ {Z} ^ {k l} \hat {Z} _ {k} (i e ^ {- 2 r _ {k}} s) \hat {C} _ {Z} ^ {k l \dagger} \\ = \exp \left(- \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \hat {X} _ {k} (s) \hat {Z} _ {l} (s) \hat {Z} _ {k} \left(i e ^ {- 2 r _ {k}} s\right). \tag {C6} \\ \end{array}
$$

Eventually, collecting all these interactions, we obtain the  $N$  new stabilizers,

$$
\exp \left(- \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \hat {X} _ {k} (s) \hat {Z} _ {k} (i e ^ {- 2 r _ {k}} s) \prod_ {l \in \mathcal {N} (k)} \hat {Z} _ {l} (s), \tag {C7}
$$

where  $\mathcal{N}(k)$  is the set of neighbors of  $k$ . In the limit of infinite squeezing  $(r_k \to \infty)$ , we get back the well-known ideal CV cluster-state stabilizers for unweighted graphs. However, this time, the above stabilizers also do the job for finite squeezing and uniquely represent the corresponding approximate cluster state. The nullifiers are obtained by taking the log of the stabilizers:

$$
\begin{array}{l} \exp \left(- \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \hat {X} _ {k} (s) \hat {Z} _ {k} (i e ^ {- 2 r _ {k}} s) \prod_ {l \in \mathcal {N} (k)} \hat {Z} _ {l} (s) \\ = \exp \left(- \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \exp \left[ - i s \left(\hat {p} _ {k} - i e ^ {- 2 r _ {k}} \hat {q} _ {k}\right) \right] \\ \times \exp \left(+ \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \prod_ {l \in \mathcal {N} (k)} \exp (i s \hat {q} _ {l}) \\ = \exp \left[ - i s \left(\hat {p} _ {k} - i e ^ {- 2 r _ {k}} \hat {q} _ {k} - \sum_ {l} \hat {q} _ {l}\right) \right], \tag {C8} \\ \end{array}
$$

for all  $k = 1,2,\ldots ,N$  and for all  $s\in \mathbb{R}$ . The nullifiers are therefore

$$
\hat {p} _ {k} - i e ^ {- 2 r _ {k}} \hat {q} _ {k} - \sum_ {l \in \mathcal {N} (k)} \hat {q} _ {l} \quad \forall k. \tag {C9}
$$

This result corresponds to the complex nullifier

$$
(\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}) | \psi_ {\mathbf {Z}} \rangle = \mathbf {0}, \tag {C10}
$$

as expressed in Eq. (2.35), with a complex adjacency matrix  $\mathbf{Z}$  having imaginary diagonal entries  $ie^{-2r_k}$  and the remaining entries being either 0 or 1 depending on the particular CV cluster state with unweighted edges. For example, for two modes this reproduces the result in Eq. (4.11) for a canonical two-mode CV cluster state. More generally, the result corresponds to complex-weighted graphs including self-loops.

Any  $N$ -mode Gaussian pure state can be built from  $N$  squeezed vacua sent through passive linear optics (modulo phase-space displacements) [15]. In terms of stabilizers, this means that, without loss of generality, the stabilizers of  $N$  momentum-squeezed states are transformed as

$$
\begin{array}{l} \exp \left(- \frac {1}{2} e ^ {- 2 r _ {k}} s ^ {2}\right) \hat {U} \hat {X} _ {k} (s) \hat {U} ^ {\dagger} \hat {U} \hat {Z} _ {k} (i e ^ {- 2 r _ {k}} s) \hat {U} ^ {\dagger} \\ = \exp \left[ - i s \left(\hat {p} _ {k} ^ {\prime} - i e ^ {- 2 r _ {k}} \hat {q} _ {k} ^ {\prime}\right) \right], \tag {C11} \\ \end{array}
$$

where  $\hat{p}_k^\prime$  and  $\hat{q}_k^\prime$  are the linearly transformed momentum and position operators, respectively, after the corresponding (inverse) unitary transformation  $\hat{U}$ . Provided this  $\hat{U}$  represents

a Gaussian transformation, the exponent on the right-hand side of Eq. (C11) will always be linear combinations of the generators  $\hat{q}$  and  $\hat{p}$ . This would include the canonical  $C_Z$  interactions, as discussed before. However, now we restrict ourselves to only passive, number-preserving unitaries  $\hat{U}$ , without loss of generality [15]. The canonical case would then require that the squeezing parts of the  $C_Z$  gates be absorbed into the offline momentum squeezers, corresponding to Bloch-Messiah reduction [14].

For the case of a passive linear transformation, we can write  $\hat{\mathbf{a}}' = \mathbf{L}\hat{\mathbf{a}}$ , where  $\mathbf{L} \coloneqq \mathbf{X} + i\mathbf{Y}$  is an  $N \times N$  unitary matrix (with real  $\mathbf{X}$  and  $\mathbf{Y}$ ), and therefore [cf. the last matrix in Eq. (2.17)],

$$
\binom {\hat {\mathbf {q}} ^ {\prime}} {\hat {\mathbf {p}} ^ {\prime}} = \binom {\mathbf {X}} {\mathbf {Y}} \binom {- \mathbf {Y}} {\mathbf {X}} \binom {\hat {\mathbf {q}}} {\hat {\mathbf {p}}}. \tag {C12}
$$

Finally, through Eq. (C11), we arrive at the new stabilizers

$$
\left. \exp \left\{- i s \sum_ {l} \left[ \left(Y _ {k l} - i e ^ {- 2 r _ {k}} X _ {k l}\right) \hat {q} _ {l} + \left(X _ {k l} + i e ^ {- 2 r _ {k}} Y _ {k l}\right) \hat {p} _ {l} \right] \right\}. \right. \tag {C13}
$$

For the nullifiers, we obtain

$$
(\mathbf {A} \hat {\mathbf {p}} - \mathbf {B} \hat {\mathbf {q}}) | \psi_ {\mathbf {Z}} \rangle = \mathbf {0}, \tag {C14}
$$

where

$$
A _ {k l} = X _ {k l} + i e ^ {- 2 r _ {k}} Y _ {k l}, \tag {C15}
$$

$$
- B _ {k l} = Y _ {k l} - i e ^ {- 2 r _ {k}} X _ {k l}, \tag {C16}
$$

which we may rewrite as

$$
\left(\mathbf {A} ^ {- 1} \mathbf {A} \hat {\mathbf {p}} - \mathbf {A} ^ {- 1} \mathbf {B} \hat {\mathbf {q}}\right) | \psi_ {\mathbf {Z}} \rangle = (\hat {\mathbf {p}} - \mathbf {Z} \hat {\mathbf {q}}) | \psi_ {\mathbf {Z}} \rangle = \mathbf {0}, \tag {C17}
$$

with  $\mathbf{Z} \coloneqq \mathbf{A}^{-1}\mathbf{B}$ . This gives us, again, the complex adjacency matrix for an arbitrary pure Gaussian  $N$ -mode state. We note that there are at most  $4N^2$  parameters to determine the stabilizer or nullifier [45]. These, however, are not independent, as  $\mathbf{L}$  must be a unitary matrix, and  $\mathbf{B}$  follows from  $\mathbf{A}$ . A general Gaussian unitary transformation has  $2N^2 + N$  free parameters, without displacements, which is the same number for representing a symplectic transformation from  $\mathrm{Sp}(2N,\mathbb{R})$ . For representing pure Gaussian  $N$ -mode states (modulo displacements), it is enough to apply a general Gaussian unitary transformation to an  $N$ -mode vacuum state, where after Bloch-Messiah reduction [15], the first passive transformation has no effect on the vacuum [14]. Thus,  $N$  real squeezing parameters  $r_k$  and  $N^2$  parameters for the remaining passive

transformation  $\mathbf{L}$  suffice to uniquely determine matrices  $\mathbf{A}$  and  $\mathbf{B}$  and, hence, the state through  $\mathbf{Z}$ .

As an example we refer to the standard two-mode-squeezed state, obtainable by interfering a  $\hat{q}$ -squeezed state with a  $\hat{p}$ -squeezed state at a 50:50 beamsplitter [3,47,48]. Then we have

$$
\mathbf {A} = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} 1 & 1 \\ i e ^ {- 2 r _ {2}} & - i e ^ {- 2 r _ {2}} \end{array} \right), \tag {C18}
$$

$$
\mathbf {B} = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} i e ^ {- 2 r _ {1}} & i e ^ {- 2 r _ {1}} \\ - 1 & 1 \end{array} \right), \tag {C19}
$$

and

$$
\mathbf {A} ^ {- 1} = \frac {1}{\sqrt {2}} \left( \begin{array}{c c} 1 & - i e ^ {+ 2 r _ {2}} \\ 1 & i e ^ {+ 2 r _ {2}} \end{array} \right), \tag {C20}
$$

resulting in the matrix  $\mathbf{Z}_1$  from Eq. (4.8) using equal initial squeezing  $r_1 = r_2 = \alpha$ . Another simple example is the  $N$ -mode vacuum state, for which  $r_k = 0$ ,  $\mathbf{A} = \mathbf{L}$ , and  $\mathbf{B} = i\mathbf{L}$  so that  $\mathbf{Z} = i\mathbf{I}$  for any  $\mathbf{L}$ . The vacuum always remains an uncorrelated graph with only self-loops.

# APPENDIX D: MIXED GAUSSIAN STATES

There is a very simple special case of mixed Gaussian states for which the entire pure-state graph calculus presented in this article follows through as well almost trivially. This special case is usually referred to as the  $N$ -dimensional isotropic oscillator [44]. The covariance matrix for a general mixed Gaussian  $N$ -mode state is given by

$$
\boldsymbol {\Sigma} = \frac {1}{2} \mathbf {S} \binom {\mathbf {K}} {\mathbf {0}} \mathbf {S} ^ {\mathrm {T}}, \tag {D1}
$$

generalizing the expressions from Eq. (2.16), by replacing the  $N$ -mode vacuum/ground state  $\mathbf{I} / 2$  by  $1 / 2$  times the above diagonal matrix with  $\mathbf{K} = \mathrm{diag}(\kappa)$ , where the vector  $\kappa = (\kappa_{1},\dots,\kappa_{N})^{\mathrm{T}}$  contains the symplectic eigenvalues (times 2) of  $\pmb{\Sigma}$ . For pure states, we have  $\mathbf{K} = \mathbf{I}$ .

Now let us assume that all symplectic eigenvalues are equal to  $\kappa$ , corresponding to an  $N$ -mode Gaussian state built from  $N$  thermal states with identical excitation number, replacing the  $N$  initial vacua in Eq. (2.16). Carrying along this one extra parameter  $\kappa$ , we can use our graphical formalism to describe this special case as well. We leave to future work a possible extension of our formalism to general Gaussian mixed states.

[1] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[2] H. J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).  
[3] S. L. Braunstein and P. van Loock, Rev. Mod. Phys. 77, 513 (2005).  
[4] J. Zhang and S. L. Braunstein, Phys. Rev. A 73, 032318 (2006).  
[5] N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, and M. A. Nielsen, Phys. Rev. Lett. 97, 110501 (2006).  
[6] M. Gu, C. Weedbrook, N. C. Menicucci, T. C. Ralph, and P. van Loock, Phys. Rev. A 79, 062318 (2009).

[7] M. A. Nielsen, Phys. Rev. Lett. 93, 040503 (2004).  
[8] D. E. Browne and T. Rudolph, Phys. Rev. Lett. 95, 010501 (2005).  
[9] E. Knill, R. Laflamme, and G. J. Milburn, Nature (London) 409, 46 (2001).  
[10] M. Ohliger, K. Kieling, and J. Eisert, Phys. Rev. A 82, 042336 (2010).  
[11] B. Yurke, J. Opt. Soc. Am. B 2, 732 (1985).  
[12] A. La Porta, R. E. Slusher, and B. Yurke, Phys. Rev. Lett. 62, 28 (1989).  
[13] J. Yoshikawa et al., Phys. Rev. A 76, 060301 (2007).

[14] P. van Loock, C. Weedbrook, and M. Gu, Phys. Rev. A 76, 032321 (2007).  
[15] S. L. Braunstein, Phys. Rev. A 71, 055801 (2005).  
[16] X. Su et al., Phys. Rev. Lett. 98, 070502 (2007).  
[17] M. Yukawa, R. Ukai, P. van Loock, and A. Furusawa, Phys. Rev. A 78, 012301 (2008).  
[18] H. Yonezawa and A. Furusawa, Opt. Spectrosc. (USSR) 108, 288 (2010).  
[19] R. Ukai et al., e-print arXiv:1001.4860 [quant-ph] (2010).  
[20] Y. Miwa, R. Ukai, J. Yoshikawa, R. Filip, P. van Loock, and A. Furusawa, Phys. Rev. A 82, 032305 (2010).  
[21] N. C. Menicucci, S. T. Flammia, H. Zaidi, and O. Pfister, Phys. Rev. A 76, 010302(R) (2007).  
[22] H. Zaidi et al., Laser Phys. 18, 659 (2008).  
[23] N. C. Menicucci, S. T. Flammia, and O. Pfister, Phys. Rev. Lett. 101, 130501 (2008).  
[24] S. T. Flammia, N. C. Menicucci, and O. Pfister, J. Phys. B 42, 114009 (2009).  
[25] R. C. Pooser and O. Pfister, Opt. Lett. 30, 2635 (2005).  
[26] M. Pysher et al., Opt. Lett. 35, 565 (2010).  
[27] M. Pysher et al., Opt. Lett. 34, 256 (2009).  
[28] S. L. W. Midgley, A. S. Bradley, O. Pfister, and M. K. Olsen, e-print arXiv:1002.2019 [quant-ph] (2010).  
[29] N. C. Menicucci, X. Ma, and T. C. Ralph, Phys. Rev. Lett. 104, 250503 (2010).  
[30] O. Pfister, e-print arXiv:quant-ph/0701104 (2007).  
[31] S. T. Flammia and S. Severini, J. Phys. A 42, 065302 (2009).  
[32] J. Zhang, Phys. Rev. A 78, 034301 (2008).  
[33] M. Van den Nest, J. Dehaene, and B. De Moor, Phys. Rev. A 69, 022316 (2004).  
[34] M. Hein, J. Eisert, and H. J. Briegel, Phys. Rev. A 69, 062311 (2004).  
[35] D. Schlingemann, Quantum Inf. Comput. 2, 307 (2002).  
[36] D. Schlingemann, Quantum Inf. Comput. 4, 287 (2004).  
[37] M. B. Elliott, B. Eastin, and C. M. Caves, Phys. Rev. A 77, 042307 (2008).  
[38] M. B. Elliott, B. Eastin, and C. M. Caves, J. Phys. A 43, 025301 (2010).  
[39] J. Zhang, Phys. Rev. A 78, 052307 (2008).

[40] M. Hein et al., in International School of Physics Enrico Fermi, Quantum Computer, Algorithms and Chaos, edited by G. Casati et al., Vol. 162 (IOS Press, Amsterdam, 2006).  
[41] R. Ukai, J. Yoshikawa, N. Iwata, P. van Loock, and A. Furusawa, Phys. Rev. A 81, 032315 (2010).  
[42] J. Zhang, Phys. Rev. A 82, 034303 (2010).  
[43] A. C. Doherty and S. D. Bartlett, Phys. Rev. Lett. 103, 020506 (2009).  
[44] R. Simon, E. C. G. Sudarshan, and N. Mukunda, Phys. Rev. A 37, 3028 (1988).  
[45] S. D. Bartlett et al., Phys. Rev. Lett. 88, 097904 (2002).  
[46] D. Fattal, T. S. Cubitt, Y. Yamamoto, S. Bravyi, and I. L. Chuang, e-print arXiv:quant-ph/0406168 (2004).  
[47] A. Furusawa et al., Science 282, 706 (1998).  
[48] P. van Loock and S. L. Braunstein, Phys. Rev. A 61, 010302 (1999).  
[49] M. D. Reid and P. D. Drummond, Phys. Rev. Lett. 60, 2731 (1988).  
[50] M. D. Reid, Phys. Rev. A 40, 913 (1989).  
[51] P. D. Drummond, M. D. Reid, and I. Below, Phys. Rev. A 41, 3930 (1990).  
[52] Z. Y. Ou, S. F. Pereira, H. J. Kimble, and K. C. Peng, Phys. Rev. Lett. 68, 3663 (1992).  
[53] Arvind et al., Pramana 45, 471 (1995).  
[54] S. Lloyd and S. L. Braunstein, Phys. Rev. Lett. 82, 1784 (1999).  
[55] D. F. Walls and G. J. Milburn, Quantum Optics, 2nd ed. (Springer, Berlin, 2008).  
[56] G. Adesso, Phys. Rev. Lett. 97, 130502 (2006).  
[57] A. S. Bradley et al., Phys. Rev. A 72, 053805 (2005).  
[58] O. Pfister, S. Feng, G. Jennings, R. Pooser, and D. Xie, Phys. Rev. A 70, 020302 (2004).  
[59] P. van Loock and S. L. Braunstein, Phys. Rev. Lett. 84, 3482 (2000).  
[60] L. Aolita, A. J. Roncaglia, A. Ferraro, and A. Acín, Phys. Rev. Lett. 106, 090501 (2011).  
[61] G. Vidal and R. F. Werner, Phys. Rev. A 65, 032314 (2002).  
[62] P. J. Freitas, Ph.D. thesis, University of Illinois, Chicago, 1999.  
[63] H. Cable and D. E. Browne, New J. Phys. 12, 113046 (2010).