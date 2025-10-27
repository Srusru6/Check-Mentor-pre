# Efficient Verification of Hypergraph States

Huangjun Zhu $^{1,2,3,4,5,*}$  and Masahito Hayashi $^{6,7,8,9}$

$^{1}$ Department of Physics and Center for Field Theory and Particle Physics, Fudan University, Shanghai 200433, China

$^{2}$ State Key Laboratory of Surface Physics, Fudan University, Shanghai 200433, China

<sup>3</sup>Institute for Nanoelectronic Devices and Quantum Computing, Fudan University, Shanghai 200433, China

$^{4}$  Collaborative Innovation Center of Advanced Microstructures, Nanjing 210093, China

$^{5}$  Institute for Theoretical Physics, University of Cologne, Cologne 50937, Germany

<sup>6</sup> Graduate School of Mathematics, Nagoya University, Nagoya 464-8602, Japan

Shenzhen Institute for Quantum Science and Engineering, Southern University of Science and Technology, Shenzhen 518055, China

<sup>8</sup> Center for Quantum Computing, Peng Cheng Laboratory, Shenzhen 518000, China

<sup>9</sup> Centre for Quantum Technologies, National University of Singapore, 3 Science Drive 2, 117542, Singapore

![](images/64c1fe3f9b1d7bb34907c9f04cc3b77b766844a8a2e5e72bbb409c2261ff951c.jpg)

(Received 17 May 2019; revised manuscript received 18 September 2019; published 20 November 2019)

Graph states and hypergraph states are of wide interest in quantum information processing and foundational studies. Efficient verification of these states is a key to various applications. Here we propose a simple method for verifying hypergraph states, which requires only two distinct Pauli measurements for each party, yet its efficiency is comparable to the best strategy based on entangling measurements. For a given state, the overhead is bounded by the chromatic number and degree of the underlying hypergraph. Our protocol is dramatically more efficient than all previous protocols based on local measurements, including tomography and direct-fidelity estimation. It enables the verification of hypergraph states and genuine multipartite entanglement of thousands of qubits. The protocol can also be generalized to the adversarial scenario, while achieving almost the same efficiency. This merit is particularly appealing to demonstrating blind measurement-based quantum computation and quantum supremacy.

DOI: 10.1103/PhysRevApplied.12.054047

# I. INTRODUCTION

Entanglement is the characteristic feature of quantum theory and a key resource in quantum information processing [1,2]. As an archetypal example of quantum states with genuine multipartite entanglement (GME), graph states are of wide interest to (blind) quantum computation [3-9], quantum error correction [10,11], quantum networks [12-14], and foundational studies on nonlocality [15-17]. Hypergraph states [18-22], as a generalization of graph states, are equally useful in these research areas [23-28]. Moreover, certain hypergraph states, like Union Jack states, are universal for measurement-based quantum computation (MBQC) under only Pauli measurements [23,24,27,29], which is impossible for graph states. Furthermore, hypergraph states are attractive for demonstrating quantum supremacy [25,30] among other merits.

The applications of hypergraph states rely crucially on our ability to verify them with local measurements

that are accessible in the lab. However, no efficient method is known so far for verifying general hypergraph states, except for graph states [7-9,14,31,32]. In general, the resource required in traditional tomography increases exponentially with the number of qubits. The same is true for popular alternatives, such as compressed sensing [33] and direct-fidelity estimation (DFE) [34]. Even recent approaches tailored for hypergraph states [25,35] are too prohibitive to apply in practice. The situation is much worse in the adversarial scenario, which is crucial to many tasks in quantum information processing that require high-security conditions, including blind MBQC [6-9,29] and quantum networks [12-14]. In this case, unfortunately, to verify the simplest nontrivial hypergraph states (say of three qubits) already entails an astronomical number of measurements [25,35].

Here we propose a simple and efficient method for verifying general (qubit and qudit) hypergraph states, which requires only two distinct Pauli measurements for each party. To verify an  $n$ -qubit hypergraph state, our protocol requires at most  $m = n$  (potential) measurement settings and  $m\epsilon^{-1}\ln \delta^{-1}$  tests in total, where  $\epsilon$  and  $\delta$  denote the

infidelity and significance level, which characterize the target precision. For a given state,  $m$  can be replaced by the chromatic number or degree of the underlying hypergraph. For many interesting graph states and hypergraph states, including cluster states and Union Jack states, the number of measurement settings and that of tests in total do not increase with the number of qubits. For example, Union Jack states can be verified with only three measurement settings and  $3\epsilon^{-1}\ln \delta^{-1}$  tests in total.

Our protocol for verifying hypergraph states is dramatically more efficient than known candidates, including tomography and DFE [34], as well as recent protocols tailored for hypergraph states [25,35]. It enables efficient verification of hypergraph states of thousands of qubits and is also highly efficient in certifying GME. Moreover, our protocol can be generalized to the adversarial scenario, while retaining almost the same efficiency, in which case the advantage over previous approaches is even more dramatic. For stabilizer states (equivalent to graph states under local Clifford transformations [36,37]), our protocol adapted for the adversarial scenario is also much more efficient than previous protocols applicable to the adversarial scenario. Our proposal is thus particularly appealing to realizing blind MBQC and quantum supremacy.

The rest of this Paper is organized as follows. In Sec. II we review the basic framework of pure-state verification. In Sec. III, we review hypergraphs and hypergraph states in preparation for later study. In Sec. IV we propose a simple and efficient protocol for verifying general hypergraph states in the nonadversarial scenario. In Sec. V we generalize our protocol to the adversarial scenario and discuss an application to demonstrating quantum supremacy. In Sec. VI we provide efficient protocols for certifying GME of hypergraph states based on the above verification protocols. In Sec. VII we generalize our results to qudit hypergraph states. Section VIII summarizes this Paper. To streamline the presentation, a few technical proofs and some additional discussions are relegated to the appendix.

# II. VERIFICATION OF PURE STATES

Consider a device that is supposed to produce the target state  $|\Psi \rangle$  in the Hilbert space  $\mathcal{H}$ . In practice, the device may actually produce  $\sigma_1, \sigma_2, \ldots, \sigma_N$  in  $N$  runs. Now our task is to determine whether the average infidelity  $\bar{\epsilon} = 1 - \left( \sum_{j} \langle \Psi | \sigma_j | \Psi \rangle / N \right)$  of these states with the target state is smaller than a given threshold, say  $\epsilon$ . To achieve this task we can perform two-outcome tests  $\{P_l, 1 - P_l\}$  based on local projective measurements. The test projector  $P_l$  corresponds to passing the test and satisfies the condition  $P_l | \Psi \rangle = |\Psi \rangle$ , so that the target state can pass the test for sure. Suppose the test  $P_l$  is performed with probability  $\mu_l$ , then the passing probability of a general state  $\sigma$  is given by  $\operatorname{tr}(\Omega \sigma)$ , where  $\Omega := \sum_l \mu_l P_l$  is the verification operator and also called a strategy. This probability satisfies the

following equation [31,38]:

$$
\max  _ {\langle \Psi | \sigma | \Psi \rangle \leq 1 - \epsilon} \operatorname {t r} (\Omega \sigma) = 1 - [ 1 - \beta (\Omega) ] \epsilon = 1 - v (\Omega) \epsilon , \tag {1}
$$

where  $\beta (\Omega)$  is the second largest eigenvalue of  $\Omega$ , and  $\nu (\Omega)\coloneqq 1 - \beta (\Omega)$  is the spectral gap.

Equation (1) implies that the probability that all states  $\sigma_{1},\sigma_{2},\ldots ,\sigma_{N}$  pass the tests is at most  $[1 - \nu (\Omega)\bar{\epsilon} ]^{N}$  where  $\bar{\epsilon}$  is the average infidelity. To ensure the condition  $\sum_{j}\langle \Psi |\sigma_{j}|\Psi \rangle /N > 1 - \epsilon$  with significance level  $\delta$  ,the minimum number of tests reads [38,39]

$$
N _ {\mathrm {N A}} (\epsilon , \delta , \Omega) = \left\lceil \frac {1}{\ln [ 1 - v (\Omega) \epsilon ]} \ln \delta \right\rceil \leq \left\lceil \frac {1}{v (\Omega) \epsilon} \ln \frac {1}{\delta} \right\rceil , \tag {2}
$$

where NA means nonadversarial. A similar formula was first derived in Ref. [31] under the assumption that the fidelity  $\langle \Psi |\sigma_j|\Psi \rangle$  either equals 1 for all  $j$  or satisfies  $\langle \Psi |\sigma_j|\Psi \rangle \leq 1 - \epsilon$  for all  $j$ . Here we do not need this assumption.

The verification strategy  $\Omega$  can also be applied to constructing upper and lower bounds for the average fidelity. Suppose all  $\sigma_{j}$  are identical to the state  $\sigma$  and let  $F = \langle \Psi |\sigma |\Psi \rangle$  be the fidelity between  $\sigma$  and the target state  $|\Psi \rangle$ . Then it is easy to derive that

$$
[ 1 - \tau (\Omega) ] F + \tau (\Omega) \leq \operatorname {t r} (\Omega \sigma) \leq v (\Omega) F + \beta (\Omega), \tag {3}
$$

where  $\tau (\Omega)$  is the smallest eigenvalue of  $\Omega$ . As an implication, we have [38]

$$
1 - \operatorname {t r} (\Omega \sigma) \leq \frac {1 - \operatorname {t r} (\Omega \sigma)}{1 - \tau (\Omega)} \leq 1 - F \leq \frac {1 - \operatorname {t r} (\Omega \sigma)}{\nu (\Omega)}. \tag {4}
$$

In this way we can construct an interval in which the infidelity (or fidelity) lies by virtue of the passing probability  $\operatorname{tr}(\Omega \sigma)$ . When  $\sigma_{j}$  varies over different runs, Eqs. (3) and (4) are still applicable if  $F$  and  $\operatorname{tr}(\Omega \sigma)$  are replaced by their averages over all runs.

In the adversarial scenario, the quantum states are prepared by a potentially malicious adversary, as encountered in blind MBQC. Nevertheless, we can still verify pure quantum states efficiently by performing random permutations before applying a verification strategy  $\Omega$  as in the nonadversarial scenario. In this case, the number of required tests is determined in Refs. [38,39]. Surprisingly, by adding the trivial test with a suitable probability, this number is comparable to the counterpart for the nonadversarial scenario, and the overhead is at most three times for high-precision verification. Therefore, to construct an efficient verification protocol for the adversarial scenario, it remains to devise an efficient verification protocol for the nonadversarial scenario.

# III. HYPERGRAPHS AND HYPERGRAPH STATES

# A. Hypergraphs

A hypergraph  $G = (V, E)$  is characterized by a set of vertices  $V = \{1, 2, \dots, n\}$  and a set of hyperedges  $E \subset \mathcal{P}(V)$ , where  $\mathcal{P}(V)$  is the power set of  $V$  [19,20]. The order of a hyperedge is the number of vertices it connects, and the order of a hypergraph is the maximum order of its hyperedges. As examples, Fig. 1 shows the order-3 hypergraphs underlying order-3 cluster states and Union Jack states [23]. A graph is a special hypergraph in which all hyperedges have order 2. Two distinct vertices of  $G$  are adjacent if they are connected by a hyperedge. The degree  $\deg(j)$  of a vertex  $j$  is the number of vertices that are adjacent to it; the degree  $\Delta(G)$  of  $G$  is the maximum vertex degree. A subset of  $V$  is a clique if every two vertices in the set are adjacent. The clique number  $\varpi(G)$  of  $G$  is the maximum number of vertices over all cliques. By contrast, a subset is an independent set if no two vertices are adjacent. The independence number  $\alpha(G)$  of  $G$  is the maximum number of vertices over all independent sets.

A set  $\mathcal{A} = \{A_1, A_2, \ldots, A_m\}$  of independent sets of  $G$  is an independence cover if  $\cup_{l=1}^{m} A_l = V$ . The cover  $\mathcal{A}$  defines a coloring of  $G$  with  $m$  colors when  $\mathcal{A}$  forms a partition of  $V$ , that is, when  $A_l$  are pairwise disjoint (assuming no  $A_l$  is empty). A hypergraph  $G$  is  $m$ -colorable if its vertices can be colored using  $m$  different colors such that adjacent vertices have different colors. A bipartite graph is a two-colorable graph. The chromatic number  $\chi(G)$  is the minimum number of colors in any coloring of  $G$ .

A weighted independence cover  $(\mathcal{A},\mu)$  of  $G$  is a cover together with weights  $\mu_{l}$  for  $A_{l}\in \mathcal{A}$ , where  $\mu_{l}$  form a

![](images/67897753d2c3d7c513928e61f14abbb88f1b3a6327670bb169f7b1d72594df6f.jpg)  
FIG. 1. Examples of hypergraphs and associated hypergraph states. Left plot: one-dimensional (1D) and two-dimensional (2D) order-3 cluster states; every three neighboring vertices on a row or column are connected by an order-3 hyperedge. Right plot: Union Jack states on a chain and a 2D lattice, respectively; the three vertices of each elementary triangle are connected by an order-3 hyperedge [23]. All four hypergraphs are three-colorable as illustrated.

probability distribution. It is closely connected to a fractional coloring [40,41] as explained in Appendix A. The cover strength of  $(\mathcal{A},\mu)$  is defined as

$$
s (\mathscr {A}, \mu) = \min  _ {j \in V} \sum_ {l \mid A _ {l} \ni j} \mu_ {l}. \tag {5}
$$

The independence degree  $\gamma (G)$  of  $G$  is the maximum of  $s(\mathcal{A},\mu)$  over all weighted independence covers of  $G$  namely,

$$
\gamma (G) = \max  _ {(\mathcal {A}, \mu)} s (\mathcal {A}, \mu). \tag {6}
$$

It is also equal to the inverse of the fractional chromatic number  $\chi_f(G)$ , that is,  $\gamma (G) = 1 / \chi_f(G)$  [40,41]. The degrees, clique numbers, independence numbers, chromatic numbers, and independence degrees of common graphs and hypergraphs are shown in Table I. The following well-known proposition clarifies the relations among these hypergraph invariants; see Appendix A for a self-contained proof and additional discussions.

Proposition 1. Any hypergraph  $G = (V, E)$  satisfies

$$
\frac {1}{\Delta (G) + 1} \leq \frac {1}{\chi (G)} \leq \gamma (G) \leq \min  \left\{\frac {\alpha (G)}{| V |}, \frac {1}{\varpi (G)} \right\}. \tag {7}
$$

As an implication of Proposition 1,  $\gamma(G) \geq 1/n$  for any hypergraph of  $n$  vertices since  $\Delta(G) \leq n - 1$  and  $\chi(G) \leq n$ . In addition,  $\gamma(G) = 1/m$  if the hypergraph  $G$  has chromatic number and clique number both equal to  $m$ . In particular,  $\gamma(G)$  can attain the maximum 1 if and only if  $G$  has no nontrivial hyperedges. Here a hyperedge is nontrivial if its order is larger than or equal to 2. Any two-colorable graph  $G$  with at least one nontrivial edge has  $\gamma(G) = 1/2$ . For example,  $\gamma(G) = 1/2$  when  $G$  is a square lattice (or analogs in higher dimensions) or an even cycle;  $\gamma(G) = 1/3$  when  $G$  is a triangular lattice.

# B. Hypergraph states

The Pauli group for a qubit is generated by the two Pauli matrices

$$
X := \left( \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right), \quad Z := \left( \begin{array}{c c} 1 & 0 \\ 0 & - 1 \end{array} \right). \tag {8}
$$

The Pauli matrices for the  $j$ th qubit are indexed by the subscript  $j$ . Given any hypergraph  $G = (V, E)$  with  $n$  vertices, we can construct an  $n$ -qubit hypergraph state  $|G\rangle$ : prepare the state  $|+ \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$  (eigenstate of  $X$  with eigenvalue 1) for each vertex of  $G$  and apply the generalized controlled- $Z$  operation  $CZ_{e}$  on the vertices of each

TABLE I. Degrees  $\Delta (G)$ , clique numbers  $\varpi (G)$ , independence numbers  $\alpha (G)$ , chromatic numbers  $\chi (G)$ , and independence degrees  $\gamma (G)$  of common graphs and hypergraphs of  $n$  vertices. A graph is complete if every two vertices are adjacent. Note that the odd cycle of three vertices is complete. Here we assume that each two-colorable graph has at least one edge, while each three-colorable hypergraph has at least one hyperedge of order 3, as illustrated in Fig. 1.  

<table><tr><td>Hypergraphs G</td><td>Δ(G)</td><td>ω(G)</td><td>α(G)</td><td>χ(G)</td><td>γ(G)</td></tr><tr><td>Square lattice</td><td>4</td><td>2</td><td>⌊n/2⌋</td><td>2</td><td>1/2</td></tr><tr><td>Cubic lattice in dimension k</td><td>2k</td><td>2</td><td>⌊n/2⌋</td><td>2</td><td>1/2</td></tr><tr><td>Triangular lattice</td><td>6</td><td>3</td><td>≥ n/3</td><td>3</td><td>1/3</td></tr><tr><td>Even cycle</td><td>2</td><td>2</td><td>n/2</td><td>2</td><td>1/2</td></tr><tr><td>Odd cycle (n ≥ 5)</td><td>2</td><td>2</td><td>(n-1)/2</td><td>3</td><td>(n-1)/(2n)</td></tr><tr><td>Complete graph</td><td>n-1</td><td>n</td><td>1</td><td>n</td><td>1/n</td></tr><tr><td>Two-colorable graph</td><td>...</td><td>2</td><td>≥ n/2</td><td>2</td><td>1/2</td></tr><tr><td>Three-colorable hypergraph</td><td>...</td><td>3</td><td>≥ n/3</td><td>3</td><td>1/3</td></tr></table>

hyperedge  $e\in E$  [19,20], that is,

$$
| G \rangle = \left(\prod_ {e \in E} C Z _ {e}\right) | + \rangle^ {\otimes n}. \tag {9}
$$

Here  $CZ_{e} = \bigotimes_{j\in e}1_{j} - 2\bigotimes_{j\in e}|1\rangle \langle 1|_{j}$ , which acts trivially on the Hilbert space associated with vertices in  $V\setminus e$ . When the hyperedge  $e$  is empty,  $CZ_{e}$  is equal to the minus identity  $-1$  by convention. When  $e$  contains a single vertex,  $CZ_{e}$  reduces to the Pauli operator  $Z$  on the vertex, which is local. When  $e$  contains two vertices,  $CZ_{e}$  is the familiar controlled-  $Z$  operation.

Alternatively, the hypergraph state  $|G\rangle$  is the unique eigenstate (up to a global phase factor) with eigenvalue 1 of the following  $n$  commuting (nonlocal) stabilizer operators [19,20],

$$
K _ {j} = X _ {j} \otimes \prod_ {e \in E | e \ni j} C Z _ {e \backslash \{j \}}, \quad j = 1, 2, \dots , n. \tag {10}
$$

This alternative characterization plays a key role in the verification of hypergraph states.

The order of a hypergraph state is defined as the order of the underlying hypergraph; similar convention applies to many other graph theoretic quantities, such as the degree, clique number, (fractional) chromatic number, independence number, and independence degree. For example,  $\gamma(G) = 1/2$  for graph states  $|G\rangle$  associated with nontrivial two-colorable graphs (with at least one edge), including cluster states (of any dimension);  $\gamma(G) = 1/3$  for hypergraph states  $|G\rangle$  associated with nontrivial three-colorable hypergraphs (with at least one hyperedge of order 3): including order-3 cluster states (of any dimension) and Union Jack states; cf. Table I.

Hypergraph states enjoy a number of appealing merits. For example, hypergraph states of connected hypergraphs are genuinely multipartite entangled (GME) [19]. Certain hypergraph states, including Union Jack states shown in Fig. 1, are universal for MBQC under only

Pauli measurements [23,24,27], which is impossible for graph states. What is more appealing, hypergraph states are found recently that are universal for MBQC under only  $X$  and  $Z$  measurements [29]. In addition, certain hypergraph states possess symmetry-protected topological orders, which are a focus of ongoing research [23,24,28]. Furthermore, hypergraph states are attractive for demonstrating quantum supremacy [25,30]. When  $G$  is an ordinary graph,  $|G\rangle$  reduces to a graph state. All stabilizer states are equivalent to graph states under local Clifford transformations (LC) [36,37]. Meanwhile, Calderbank-Shor-Steane states are equivalent to graph states associated with two-colorable graphs, and vice versa [42].

# IV. EFFICIENT VERIFICATION OF HYPERGRAPH STATES

# A. Construction of tests for hypergraph states

Let  $G = (V, E)$  be a hypergraph with  $n$  vertices and  $|G\rangle$  the associated hypergraph state. Given any nonempty independent set  $A$  of  $G$ , we can devise a test for  $|G\rangle$  based on two types of Pauli measurements. The test consists in measuring  $X_{j}$  for  $j \in A$  and measuring  $Z_{k}$  for  $k \in \overline{A}$ , where  $\overline{A} := V \setminus A$  is the complement of  $A$  in  $V$ . The measurement outcome on the  $a$ th qubit for  $a = 1,2,\ldots,n$  can be written as  $(-1)^{o_a}$ , where the Boolean variable  $o_{a}$  is either 0 or 1. Since  $A$  is an independent set,  $X_{j}$  and  $Z_{k}$  commute with  $K_{i}$  for all  $i,j \in A$  and  $k \in \overline{A}$ . The joint eigenstate of  $X_{j}$  and  $Z_{k}$  corresponding to the outcome  $\{o_{a}\}$  is an eigenstate of  $K_{i}$  with eigenvalue  $(-1)^{t_i}$ , where

$$
t _ {i} = o _ {i} + \sum_ {e \in E | e \ni i} \left(\prod_ {k \in e, k \neq i} o _ {k}\right). \tag {11}
$$

Here it is understood that  $\prod_{k\in e,k\neq i}o_k = 1$  if  $e = \{i\}$

Now we set the criterion that the test is passed if and only if  $(-1)^{i_i} = 1$  for all  $i\in A$ , then the test effectively measures all the stabilizer operators  $K_{i}$  for  $i\in A$ . The

projector onto the pass eigenspace reads

$$
P _ {A} = \prod_ {i \in A} \frac {1 + K _ {i}}{2}. \tag {12}
$$

A quantum state  $\rho$  can always pass the test if and only if it is stabilized by  $K_{i}$  for all  $i\in A$ , which holds for the target state  $|G\rangle$ . The rank of the test projector  $P_A$  reads

$$
\operatorname {r a n k} \left(P _ {A}\right) = \operatorname {t r} \left(P _ {A}\right) = 2 ^ {n - | A |}, \tag {13}
$$

where  $|A|$  denotes the cardinality of the set  $A$ ; the larger  $|A|$  is, the smaller  $\mathrm{rank}(P_A)$  is. In view of this observation, it is beneficial to choose large independent sets for constructing test projectors for the hypergraph state  $|G\rangle$ . Incidentally, the cardinality  $|A|$  is upper bounded by the independence number  $\alpha(G)$ . Suppose  $G$  has at least one nontrivial hyperedge or edge; then  $\alpha(G) \leq n - 1$ , which implies that  $\mathrm{rank}(P_A) \geq 2$ . So at least two distinct tests are necessary to verify  $|G\rangle$  as expected.

Denote by  $\mathcal{N}(A)$  the neighborhood of  $A$  in the graph  $G$ , that is, the set of vertices in  $G$  that are adjacent to at least one vertex in  $A$ . Since  $A$  is an independent set,  $\mathcal{N}(A)$  and  $A$  are disjoint, that is,  $\mathcal{N}(A) \subset \overline{A}$ . The complement  $\overline{A}$  used in constructing the test  $P_A$  above can be replaced by  $\mathcal{N}(A)$  because Eq. (11) only involves measurement outcomes associated with vertices in the set  $A \cup \mathcal{N}(A)$ . In other words,  $Z$  measurements associated with vertices in  $\overline{A} \setminus \mathcal{N}(A)$  are redundant. Meanwhile, the independent set  $A$  can be enlarged when  $A \cup \mathcal{N}(A)$  is a proper subset of the vertex set  $V$  of  $G$ . Conversely, if  $A \cup \mathcal{N}(A) = V$ , then  $\mathcal{N}(A) = \overline{A}$ , so that  $A$  cannot be contained in any larger independent set.

# B. The cover protocol

Let  $\mathcal{A} = \{A_1, A_2, \ldots, A_m\}$  be an independence cover of  $G$  that is composed of  $m$  nonempty independent sets, then we can devise a verification protocol for  $|G\rangle$  with  $m$  distinct tests. For each independent set  $A_l$ , we can construct a test with the test projector  $P_l = \prod_{i \in A_l} ((1 + K_i) / 2)$  according to Eq. (12). A state can pass all  $m$  tests if and only if it is stabilized by  $K_i$  for all  $i \in \cup_{l=1}^{m} A_l = V$ . So only the target state  $|G\rangle$  can pass all tests with certainty as desired. This verification protocol is referred to as the cover protocol (or fractional coloring protocol) since it is determined by an independence cover (or a fractional coloring). When  $G$  is connected, the hypergraph state  $|G\rangle$  is GME, so each party requires at least two projective measurements to verify  $|G\rangle$  [38]. The cover protocol requires only two Pauli measurements for each party and is thus the most economical with regard to the number of measurement settings for each party.

Suppose the test  $P_{l}$  (associated with the independent set  $A_{l}$ ) is applied with probability  $\mu_{l}$ . Then the cover protocol is characterized by the weighted independence cover

$(\mathcal{A}, \mu)$ . Its efficiency is determined by the spectral gap of the verification operator

$$
\Omega (\mathcal {A}, \mu) = \sum_ {l = 1} \mu_ {l} P _ {l} = \sum_ {l} \mu_ {l} \prod_ {i \in A _ {l}} \frac {1 + K _ {i}}{2}. \tag {14}
$$

Note that the common eigenbasis of  $K_{i}$  for  $i\in V$  also forms an eigenbasis of  $\Omega (\mathcal{A},\mu)$ . Each eigenstate  $|\Psi_x\rangle$  in this basis is specified by an  $n$ -bit string  $x\in \{0,1\} ^n$  and satisfies the equation  $K_{i}|\Psi_{x}\rangle = (-1)^{x_{i}}|\Psi_{x}\rangle$ . The corresponding eigenvalue of  $\Omega (\mathcal{A},\mu)$  reads

$$
\lambda_ {x} = \sum_ {l \mid \operatorname {s u p p} (x) \subset \bar {A} _ {l}} \mu_ {l}, \tag {15}
$$

where  $\operatorname{supp}(x) \coloneqq \{i | x_i \neq 0\}$ . To attain the second largest eigenvalue of  $\Omega(\mathcal{A}, \mu)$ , it suffices to consider the case in which  $x$  has only one bit equal to 1, which means

$$
\beta (\Omega (\mathcal {A}, \mu)) = \max  _ {i \in V} \sum_ {l \mid \bar {A} _ {l} \ni i} \mu_ {l}. \tag {16}
$$

Similarly, the smallest eigenvalue of  $\Omega (\mathcal{A},\mu)$  is attained when all bits of  $x$  are equal to 1, in which case we have  $\lambda_{x} = 0$ , given that all independent sets  $A_{l}$  are nonempty. So the verification operator  $\Omega (\mathcal{A},\mu)$  is always singular. These observations confirm the following theorem.

Theorem 1.-The spectral gap and the smallest eigenvalue of the cover protocol read

$$
v (\Omega (\mathcal {A}, \mu)) = s (\mathcal {A}, \mu), \quad \tau (\Omega (\mathcal {A}, \mu)) = 0, \tag {17}
$$

$$
\max  _ {(\mathcal {A}, \mu)} v (\Omega (\mathcal {A}, \mu)) = \gamma (G) = \left[ \chi_ {f} (G) \right] ^ {- 1}. \tag {18}
$$

When the independent sets  $A_{1}, A_{2}, \ldots, A_{m}$  are pairwise disjoint,  $\mathcal{A}$  defines a coloring of  $G$ , in which case the protocol  $(\mathcal{A}, \mu)$  is also called a coloring protocol. Each test of the coloring protocol is associated with a color:  $X$  measurement is performed on all qubits associated with a given color, while  $Z$  measurement is performed on other qubits. The number of distinct tests equals the number of colors. For example, the Union Jack state shown in Fig. 1 can be verified using a coloring protocol composed of three distinct tests. The spectral gap of the resulting verification operator  $\Omega(\mathcal{A}, \mu)$  reads

$$
v (\Omega (\mathcal {A}, \mu)) = \min  _ {l} \mu_ {l} \leq | \mathcal {A} | ^ {- 1} \leq \chi (G) ^ {- 1}. \tag {19}
$$

Here the first inequality is saturated if and only if all weights  $\mu_l$  are equal; the second one is saturated if and only if  $|\mathcal{A}| = \chi(G)$ , so that the coloring  $\mathcal{A}$  is optimal

(cf. Appendix A). In view of this observation, by a coloring protocol, we assume that all weights  $\mu_l$  are equal, that is, all distinct tests are performed with the same probability. Then the coloring protocol  $(\mathcal{A}, \mu)$  is also denoted by  $\mathcal{A}$ . Here we emphasize that it is not necessary to compute  $\gamma(G)$  or  $\chi(G)$  to apply a cover or coloring protocol. In practice, a good coloring can be found using the Dsatur algorithm [43], for example.

Theorem 1 reveals operational meanings of the cover strength, independence degree, and fractional chromatic number in verifying a hypergraph state. Given a cover protocol  $(\mathcal{A},\mu)$ , to verify  $|G\rangle$  within infidelity  $\epsilon$  and significance level  $\delta$ , the minimum number of tests is

$$
N = \left\lceil \frac {\ln \delta}{\ln [ 1 - s (\mathcal {A} , \mu) \epsilon ]} \right\rceil \leq \left\lceil \frac {\ln \delta^ {- 1}}{s (\mathcal {A} , \mu) \epsilon} \right\rceil \tag {20}
$$

by Eq. (2). This number is minimized when the cover  $(\mathcal{A},\mu)$  is optimal, so that  $s(\mathcal{A},\mu) = \gamma (G) = 1 / \chi_f(G)$  and

$$
N = \left\lceil \frac {\ln \delta}{\ln [ 1 - \gamma (G) \epsilon ]} \right\rceil \leq \left\lceil \frac {\ln \delta^ {- 1}}{\gamma (G) \epsilon} \right\rceil = \left\lceil \frac {\chi_ {f} (G) \ln \delta^ {- 1}}{\epsilon} \right\rceil . \tag {21}
$$

According to Proposition 1, we have

$$
N \leq \left\lceil \frac {\chi (G)}{\epsilon} \ln \frac {1}{\delta} \right\rceil \leq \left\lceil \frac {\Delta (G) + 1}{\epsilon} \ln \frac {1}{\delta} \right\rceil \leq \left\lceil \frac {n}{\epsilon} \ln \frac {1}{\delta} \right\rceil . \tag {22}
$$

Here the first upper bound can be achieved by an optimal coloring protocol; the second one can be achieved by a coloring with  $\Delta(G) + 1$  colors.

Although, in general, it is not easy to find an optimal coloring of the hypergraph  $G$ , it is easy to find a coloring with  $m \leq \Delta(G) + 1$  colors by virtue of a simple greedy

algorithm as presented in the proof of Proposition 1; cf. Ref. [43]. If we apply a coloring protocol with  $m$  colors, then the spectral gap of the verification operator reads  $\nu(\Omega) = 1/m$ , so the minimum number of tests is given by

$$
N = \left\lceil \frac {\ln \delta}{\ln \left(1 - m ^ {- 1} \epsilon\right)} \right\rceil \leq \left\lceil \frac {m \ln \delta^ {- 1}}{\epsilon} \right\rceil . \tag {23}
$$

The above analysis shows that any hypergraph state  $|G\rangle$  can be verified with at most  $m = \Delta (G) + 1$  measurement settings in which each party performs either  $X$  or  $Z$  measurement. Note that  $m$  is upper bounded by the number  $n$  of qubits. The total number of tests is only  $\lceil m\epsilon^{-1}\ln \delta^{-1} \rceil$  and is at most  $m$  times as large as the number for the best protocol based on entangling measurements. The cover protocol for verifying hypergraph states is dramatically more efficient than previous protocols [25,34], as illustrated in Fig. 2 and discussed in detail in Appendix C. Consider the protocol of Ref. [25] for example, both the number of measurement settings and the total number of tests increase exponentially with  $\Delta (G)$ ; in addition, the number of tests scales as  $1 / \epsilon^2$  instead of  $1 / \epsilon$ .

For many interesting hypergraph states, the chromatic numbers do not grow with the qubit number. So the number of measurement settings and the total number of tests required by the coloring protocol are independent of the number of qubits, which is the same as the best protocol based on entangling measurements. For example, two measurement settings and  $\lceil 2\epsilon^{-1}\ln \delta^{-1}\rceil$  tests are sufficient for graph states of two-colorable graphs (equivalent to Calderbank-Shor-Steane states [42]), including GHZ states, cluster states (of arbitrary dimensions), tree graph states, and graph states associated with even cycles. Three settings and  $\lceil 3\epsilon^{-1}\ln \delta^{-1}\rceil$  tests are sufficient for order-3 cluster states and Union Jack states (cf. Fig. 1).

Incidentally, the cover or coloring protocol can also be applied to constructing upper and lower bounds for the

![](images/a8cc67420cdf73a977d2122443411e702499b6d489461ecaf0fc10d6c5c17d33.jpg)  
FIG. 2. Resource costs for verifying hypergraph states in the nonadversarial scenario. Left plot: 1D order-3 cluster states; right plot: Union Jack states on a chain. Here  $n$  is the number of qubits, and  $N$  is the (expected) number of tests required to verify the state within infidelity  $\epsilon = 0.01$  and significance level  $\delta = 0.05$ . In the case of the Morimae, Takeuchi, and Hayashi (MTH) protocol proposed in Ref. [25], only a lower bound for  $N$  is given. The lines are guides for the eye. Our cover protocol dramatically outperforms DFE [34] and the MTH protocol (cf. Appendix C).

![](images/ec0832c3badf7ae81a2a22ca5ebc783d0e0e09338b8f6a57488a0697ce296fcd.jpg)

average infidelity between the states prepared and the target hypergraph state  $|G\rangle$ . Suppose all states  $\sigma_{j}$  prepared in different runs are identical to  $\sigma$ . If we apply the optimal cover protocol, then the spectral gap of the verification operator reads  $\nu(\Omega) = \gamma(G) = 1 / \chi_{f}(G)$ . According to Eq. (4), the infidelity between  $\sigma$  and  $|G\rangle$  satisfies

$$
1 - \operatorname {t r} (\Omega \sigma) \leq 1 - \langle G | \sigma | G \rangle \leq \chi_ {f} (G) [ 1 - \operatorname {t r} (\Omega \sigma) ]. \tag {24}
$$

If instead a coloring protocol with  $m$  colors is applied, then  $\nu (\Omega) = 1 / m$ , so that

$$
1 - \operatorname {t r} (\Omega \sigma) \leq 1 - \langle G | \sigma | G \rangle \leq m [ 1 - \operatorname {t r} (\Omega \sigma) ]. \tag {25}
$$

In general, if  $\sigma_{j}$  are not identical with each other, the above conclusions still hold if  $\langle G|\sigma |G\rangle$  and  $\mathrm{tr}(\Omega \sigma)$  are replaced by their averages over all runs.

# V. VERIFICATION OF HYPERGRAPH STATES IN THE ADVERSARIAL SCENARIO

# A. Cover protocol for the adversarial scenario

Thanks to a general recipe proposed in Refs. [38,39], the cover protocol can also be applied to the adversarial scenario, which is very important to many tasks in quantum information processing that demand high-security requirements, such as blind MBQC. Let  $\Omega = \Omega (\mathcal{A},\mu)$  be the verification operator associated with the cover protocol  $(\mathcal{A},\mu)$ , then  $\nu (\Omega) = s(\mathcal{A},\mu)$  and  $\tau (\Omega) = 0$  according to Theorem 1. By Ref. [38], the number of tests required by  $\Omega$  to verify  $|G\rangle$  within infidelity  $\epsilon$  and significance level  $\delta$  in the adversarial scenario satisfies

$$
\left. \right. \min  \left\{\left\lceil \frac {1 - \delta}{v (\Omega) \delta \epsilon} \right\rceil , \left\lceil \frac {1}{\delta \epsilon} - 1 \right\rceil \right\} \leq N \leq \left\lceil \frac {1 - \delta}{v (\Omega) \delta \epsilon} \right\rceil . \tag {26}
$$

For the optimal coloring protocol with  $\nu (\Omega) = 1 / \chi (G)$ , we have

$$
N \leq \left\lceil \frac {\chi (G) (1 - \delta)}{\delta \epsilon} \right\rceil \leq \left\lceil \frac {\Delta (G) + 1}{\delta \epsilon} \right\rceil \leq \left\lceil \frac {n}{\delta \epsilon} \right\rceil . \tag {27}
$$

If in addition  $G$  is two-colorable, then  $\nu(\Omega) = 1/2$  and the lower bound in Eq. (26) is saturated according to Ref. [38]. The cover protocol adapted to the adversarial scenario is much more efficient than all previous protocols for verifying hypergraph states known in the literature. Nevertheless, the scaling of  $N$  with  $\delta$  is suboptimal because the verification operator  $\Omega(\mathcal{A}, \mu)$  is singular.

# B. Hedged cover protocol

To improve the scaling behavior of the number of required tests with  $\delta$ , here we propose a hedged cover protocol  $(\mathcal{A}, \mu)_p$ , which is characterized by the verification

operator

$$
\Omega_ {p} = (1 - p) \Omega + p, \tag {28}
$$

with  $\Omega = \Omega (\mathcal{A},\mu)$ . It can be realized by performing  $\Omega$  with probability  $1 - p$  and the trivial test (the test projector is the identity) with probability  $p$ . The name "hedged cover protocol" reflects the fact that the trivial test is introduced to hedge the influence of small eigenvalues of the verification operator  $\Omega$  of the cover protocol. The second largest and smallest eigenvalues of  $\Omega_p$  read

$$
\beta_ {p} = (1 - p) \beta + p = 1 - v + p v, \quad \tau_ {p} = p, \tag {29}
$$

where  $\beta$  is the second largest eigenvalue of  $\Omega$ . The protocol  $(\mathcal{A}, \mu)_p$  is also called a hedged coloring protocol and denoted by  $\mathcal{A}_p$  when  $\mathcal{A}$  denotes a coloring and all  $\mu_l$  are equal.

According to Refs. [38,39], to verify  $|G\rangle$  within infidelity  $\epsilon$  and significance level  $\delta$  in the adversarial scenario, the number of tests required by the strategy  $\Omega_p$  (with  $p > 0$ ) satisfies

$$
N <   \frac {h (p , v) \ln (F \delta) ^ {- 1}}{\epsilon}, \tag {30}
$$

where  $\nu = s(\mathcal{A},\mu),F = 1 - \epsilon$  , and

$$
h (p, v) = \left[ \min  \left\{\beta_ {p} \ln \beta_ {p} ^ {- 1}, p \ln p ^ {- 1} \right\} \right] ^ {- 1}. \tag {31}
$$

To achieve high efficiency, the value of  $p$  can be chosen as follows according to Refs. [38,39]:

$$
p _ {*} (\nu) = \min  \left\{p > 0 | p \ln p ^ {- 1} \geq \beta_ {p} \ln \beta_ {p} ^ {- 1} \right\}. \tag {32}
$$

With this choice, the hedged cover protocol  $(\mathcal{A},\mu)_p$  is also denoted by  $(\mathcal{A},\mu)_{*}$ ; similarly, the hedged coloring protocol  $\mathcal{A}_p$  is denoted by  $\mathcal{A}_{*}$ . By virtue of the hedged cover protocol  $(\mathcal{A},\mu)_{*}$ , that is,  $(\mathcal{A},\mu)_p$  with  $p = p_{*}(\nu)$ , the number of tests in Eq. (26) can be reduced to [38,39]

$$
\begin{array}{l} N = \left\lfloor \frac {h _ {*} (\nu) \ln (F \delta) ^ {- 1}}{\epsilon} \right\rfloor \leq \frac {\ln (F \delta) ^ {- 1}}{(1 - \nu + e ^ {- 1} \nu^ {2}) \nu \epsilon} \\ \leq \frac {(1 + \mathrm {e} \nu - \nu) \ln (F \delta) ^ {- 1}}{\nu \epsilon} \leq \frac {\mathrm {e} \ln (F \delta) ^ {- 1}}{\nu \epsilon}, \tag {33} \\ \end{array}
$$

where  $\nu = s(\mathcal{A},\mu),F = 1 - \epsilon$

$$
h _ {*} (\nu) = h \left(p _ {*} (\nu), \nu\right) = - \left[ p _ {*} (\nu) \ln p _ {*} (\nu) \right] ^ {- 1}, \tag {34}
$$

and  $e$  is the base of the natural logarithm.

Alternatively, we can choose  $p = \nu / \mathrm{e}$  to construct an efficient hedged cover protocol [38,39]. It turns out that the three upper bounds in Eq. (33) still apply if the hedged

cover protocol  $(\mathcal{A},\mu)_*$  is replaced by  $(\mathcal{A},\mu)_p$  with  $p = \nu/\mathrm{e}$ , that is,

$$
\begin{array}{l} N \leq \frac {\ln (F \delta) ^ {- 1}}{(1 - v + e ^ {- 1} v ^ {2}) v \epsilon} \leq \frac {(1 + e v - v) \ln (F \delta) ^ {- 1}}{v \epsilon} \\ \leq \frac {\mathrm {e} \ln (F \delta) ^ {- 1}}{\nu \epsilon}. \tag {35} \\ \end{array}
$$

If  $\mathcal{A}$  is a coloring protocol with  $m$  colors, then the spectral gap reads  $\nu = 1 / m$ , and the number of tests required by the hedged coloring protocol  $\mathcal{A}_{*}$  is given by Eq. (33) with  $\nu = 1 / m$ , that is,

$$
N = \left\lfloor \frac {h _ {*} (1 / m) \ln (F \delta) ^ {- 1}}{\epsilon} \right\rfloor \leq \frac {(m + \mathrm {e} - 1) \ln (F \delta) ^ {- 1}}{\epsilon}. \tag {36}
$$

If the coloring is optimal, then we have  $m = \chi (G)$  and  $\nu = 1 / \chi (G)$ , so that

$$
\begin{array}{l} N = \left\lfloor \frac {h _ {*} (1 / \chi (G)) \ln (F \delta) ^ {- 1}}{\epsilon} \right\rfloor \leq \frac {\left[ \chi (G) + e - 1 \right] \ln (F \delta) ^ {- 1}}{\epsilon} \\ \leq \frac {\left[ \Delta (G) + \mathrm {e} \right] \ln (F \delta) ^ {- 1}}{\epsilon} \leq \frac {(n + \mathrm {e} - 1) \ln (F \delta) ^ {- 1}}{\epsilon}. \tag {37} \\ \end{array}
$$

Again, the upper bound in Eq. (36) and the last three bounds in Eq. (37) still apply if the hedged coloring protocol  $\mathcal{A}_{*}$  is replaced by  $\mathcal{A}_p$  with  $p = \nu/\mathrm{e}$ . According to the above results, the hedged cover (or coloring) protocol can achieve the same optimal scaling behavior in the number  $N$  of tests with  $\epsilon^{-1}$  and  $\delta^{-1}$  as the counterpart in the nonadversarial scenario; cf. Eq. (22). For high-precision verification, the overhead is at most three times, and is even negligible when  $\chi(G)$  is large. Therefore, all the conclusions on the cover protocol presented in Sec. IV B can easily be adapted to the adversarial scenario.

To illustrate the advantage of our approach, suppose we want to verify a general  $n$ -qubit hypergraph state within infidelity  $\epsilon$  and significance level  $\delta = \epsilon$  in the adversarial scenario. The protocol in a recent Paper, Ref. [35], requires at least  $(2\ln 2)n^{3}\epsilon^{-18}$  tests [applicable when  $4n\epsilon \leq 1$ , cf. Eq. (C38) in Appendix C]. By contrast, our coloring protocol requires at most  $\lceil n\epsilon^{-2}\rceil$  tests by Eq. (26), note that  $\nu (\Omega)\geq 1 / n$  for any coloring protocol. The hedged coloring protocol requires about  $n\epsilon^{-1}\ln \epsilon^{-1}$  tests if  $n,\epsilon^{-1}\gg 1$ . When  $\delta = \epsilon = 1 / (4n)$  and the hypergraph is three-colorable, the protocol in Ref. [35] requires at least  $9.5\times 10^{10}n^{21}$  tests, which is astronomical. By contrast, the optimal cover or coloring protocol with  $\nu (\Omega) = \gamma (G) = 1 / \chi (G) = 1 / 3$  requires at most  $12n(4n - 1)$  tests by Eq. (26), which outperforms Ref. [35] by at least 18 orders of magnitude even when  $n = 3$ , and the advantage increases rapidly with  $n$ , as illustrated in Fig. 3. The hedged

![](images/95a3ff7f4254fbf0120022bd26c441610f1d9c382b486e1878a30ab0a1e19e36.jpg)  
FIG. 3. Resource costs for verifying three-colorable hypergraph states in the adversarial scenario. Here  $n$  is the number of qubits, and  $N$  is the number of tests required to verify the state within infidelity  $\epsilon = 1/(4n)$  and significance level  $\delta = 1/(4n)$ . The lines are guides for the eye. Our cover protocol (Cover) and hedged cover protocol (HCover) outperform the Takeuchi and Morimae (TM) protocol proposed in Ref. [35] by at least 18 orders of magnitude.

cover or coloring protocol can further reduce the number to  $\left\lfloor 16.3n\ln (16n^2 /(4n - 1))\right\rfloor$  by Eq. (37), given the inequality  $h_{*}(\nu = 1 / 3) < 4.052$ , which can be verified by straightforward numerical calculation.

# C. Application to demonstrating quantum supremacy

Our protocols for verifying hypergraph states are instrumental to demonstrating quantum supremacy. Recently, on the basis of a plausible complexity theoretic assumption, Bremner, Montanaro, and Shepherd demonstrated the average case hardness of sampling from probability distributions from instantaneous quantum polytime circuits [30] (Theorem 6 there). Their work implies the hardness of sampling from probability distributions resulting from  $X$  measurements on random order-3 hypergraph states such that the error in  $\ell_1$  norm is bounded by  $1/192$ .

To guarantee that the error in  $\ell_1$  norm is bounded by  $1 / 192$  so as to demonstrate quantum supremacy, it suffices to ensure that the trace distance between the hypergraph state generated and the ideal target state is bounded by  $1 / 192$ . Note that the trace distance  $D_{\mathrm{tr}}(\rho_1,\rho_2)$  between two quantum states  $\rho_{1},\rho_{2}$  and the fidelity  $F(\rho_{1},\rho_{2})$  satisfies

$$
1 - \sqrt {F \left(\rho_ {1} , \rho_ {2}\right)} \leq D _ {\mathrm {t r}} \left(\rho_ {1}, \rho_ {2}\right) \leq \sqrt {1 - F \left(\rho_ {1} , \rho_ {2}\right)}, \tag {38}
$$

where the upper bound is saturated when  $\rho_{1}$  and  $\rho_{2}$  are pure [44] (our definition of the fidelity is the square of the counterpart in Ref. [44]). To demonstrate quantum supremacy, we need to verify the hypergraph state within infidelity  $\epsilon = 1 / 192^{2}$  and a given significance level  $\delta$ . If  $\delta = \epsilon$ , then the number of tests required by the protocol in Ref. [35] is more than  $2 \times 10^{82}n^{3}$  [applicable when  $4n\epsilon \leq 1$ , cf. Eq. (C38)]. By contrast, our hedged coloring

protocol requires only about  $4 \times 10^{5}n$  tests according to Eq. (36) and is thus dramatically more efficient.

# VI. CERTIFICATION OF GENUINE MULTIPARTITE ENTANGLEMENT

Here we show that the cover protocol and the hedged cover protocol are surprisingly efficient in certifying GME of hypergraph states, although it is not necessarily optimized for this purpose. Recall that a multipartite pure state is GME if it is not biseparable, that is, if it cannot be written as a tensor product of two pure states. A mixed state is GME if it cannot be expressed as a convex mixture of biseparable states [2].

# A. Nonadversarial scenario

Theorem 2. Let  $G$  be a connected order- $k$  hypergraph and  $|G\rangle$  the corresponding hypergraph state. If a state  $\rho$  satisfies  $\langle G|\rho |G\rangle >1 - 2^{1 - k}$ , then  $\rho$  is GME.

This theorem was proved in Ref. [45]; see Appendix B for an independent proof. Note that the conclusion is independent of the number  $n$  of qubits. Theorem 2 is known much earlier when  $|G\rangle$  is a graph state associated with a connected graph, in which case  $\rho$  is GME if its fidelity with  $|G\rangle$  is larger than one half [2,46,47]. In general, to certify the GME of the hypergraph state  $|G\rangle$  with significance level  $\delta$ , we need to guarantee the fidelity  $\langle G|\rho |G\rangle >1 - 2^{1 - k}$  with significance level  $\delta$ . Given a verification strategy  $\Omega$ , then it suffices to perform

$$
N = \left\lceil \frac {1}{\ln \left[ 1 - 2 ^ {1 - k} v (\Omega) \right]} \ln \delta \right\rceil \leq \left\lceil \frac {2 ^ {k - 1}}{v (\Omega)} \ln \delta^ {- 1} \right\rceil \tag {39}
$$

tests according to Eq. (2) with  $\epsilon = 2^{1 - k}$ .

If  $\Omega$  corresponds to the cover protocol  $(\mathcal{A},\mu)$ , then  $\nu (\Omega)$  is equal to the cover strength  $s(\mathcal{A},\mu)$  according to Theorem 1. If we choose the optimal cover protocol, then  $\nu (\Omega)$  is equal to the independence degree  $\gamma (G)$ , so the number of tests reduces to

$$
\begin{array}{l} N = \left\lceil \frac {1}{\ln [ 1 - 2 ^ {1 - k} \gamma (G) ]} \ln \delta \right\rceil \leq \left\lceil 2 ^ {k - 1} \chi (G) \ln \delta^ {- 1} \right\rceil \\ \leq \left\lceil 2 ^ {k - 1} [ \Delta (G) + 1 ] \ln \delta^ {- 1} \right\rceil \leq \left\lceil 2 ^ {k - 1} n \ln \delta^ {- 1} \right\rceil , \tag {40} \\ \end{array}
$$

note that  $1 / \gamma (G)\leq \chi (G)\leq \Delta (G) + 1\leq n$  according to Proposition 1. For example, we have  $N\leq 3\times 2^{k - 1}\chi (G)$  when  $\delta = 0.05$ . For a given  $\delta$ , the number in Eq. (40) is upper bounded by a constant that is independent of the number of qubits if  $\gamma (G)$ ,  $\chi (G)$ , or  $\Delta (G)$  is bounded. In particular, GME of two-colorable graph states [with  $k = 2$  and  $\gamma (G) = 1 / \chi (G) = 1 / 2]$  can be certified with only  $\lceil \ln \delta /\ln (3 / 4)\rceil$  tests (11 tests when  $\delta = 0.05$ ); for order-3 cluster states and Union Jack states [with  $k = 3$  and  $\gamma (G) = 1 / \chi (G) = 1 / 3]$ , it suffices to perform

$\lceil \ln \delta / \ln (11 / 12) \rceil$  tests (35 tests when  $\delta = 0.05$ ). Incidentally, efficient entanglement (not GME) verification of cluster states was also studied in Ref. [48].

# B. Adversarial scenario

Next, consider certification of GME of hypergraph states in the adversarial scenario. Given the cover protocol  $(\mathcal{A},\mu)$  with verification operator  $\Omega = \Omega (\mathcal{A},\mu)$ , to certify the GME of  $|G\rangle$  with significance level  $\delta$ , the minimal number of required tests satisfies

$$
N \leq \left\lceil \frac {2 ^ {k - 1} (1 - \delta)}{\nu (\Omega) \delta} \right\rceil \tag {41}
$$

according to Eq. (26) with  $\epsilon = 2^{1 - k}$ , where the spectral gap  $\nu (\Omega) = s(\mathcal{A},\mu)$  depends on the specific cover protocol. For example,  $\nu (\Omega) = \gamma (G)$  for the optimal cover protocol and  $\nu (\Omega) = 1 / \chi (G)$  for the optimal coloring protocol. When  $\nu (\Omega)\geq 1 / 2$ , the lower bound in Eq. (26) is saturated, so the number of tests reduces to

$$
N = \min  \left\{\left. \left\lceil \frac {2 ^ {k - 1} (1 - \delta)}{\nu (\Omega) \delta} \right\rceil , \left\lceil \frac {2 ^ {k - 1}}{\delta} - 1 \right\rceil \right\}. \right. \tag {42}
$$

To improve the scaling of  $N$  with  $1 / \delta$ , we can apply the hedged cover protocol  $(\mathcal{A},\mu)_*$  proposed in Sec. V B. Then the number of required tests is given by Eq. (33) with  $\epsilon = 2^{1 - k}$ , that is,

$$
\begin{array}{l} N = \left\lfloor 2 ^ {k - 1} h _ {*} (\nu) \ln (F \delta) ^ {- 1} \right\rfloor \leq \frac {2 ^ {k - 1} \ln (F \delta) ^ {- 1}}{\nu (1 - \nu + e ^ {- 1} \nu^ {2})} \\ \leq \frac {2 ^ {k - 1} (1 + \mathrm {e} \nu - \nu) \ln (F \delta) ^ {- 1}}{\nu} \leq \frac {2 ^ {k - 1} \mathrm {e} \ln (F \delta) ^ {- 1}}{\nu}, \tag {43} \\ \end{array}
$$

where  $\nu = s(\mathcal{A},\mu)$  and  $F = 1 - \epsilon = 1 - 2^{1 - k}$ . If  $\mathcal{A}$  denotes the optimal coloring protocol, then  $\nu = 1 / \chi (G)$ , and the number of tests required by the hedged coloring protocol  $\mathcal{A}_{*}$  satisfies

$$
\begin{array}{l} N \leq 2 ^ {k - 1} [ \chi (G) + e - 1 ] \ln [ (1 - 2 ^ {1 - k}) ^ {- 1} \delta^ {- 1} ] \\ \leq 2 ^ {k - 1} [ \Delta (G) + \mathrm {e} ] \ln [ (1 - 2 ^ {1 - k}) ^ {- 1} \delta^ {- 1} ]. \tag {44} \\ \end{array}
$$

This equation is also applicable if the protocol  $\mathcal{A}_*$  is replaced by  $\mathcal{A}_p$  with  $p = \nu/\mathrm{e}$ . These results are comparable to the counterparts for the nonadversarial scenario presented in Eq. (40), especially when  $k$ ,  $\chi(G)$ , and  $\Delta(G)$  are large. Therefore, GME of hypergraph states can be certified efficiently even in the adversarial scenario as long as the order  $k$  is bounded. For example, GME of two-colorable graph states can be certified in the adversarial scenario with only  $\lfloor 6.44\ln(2/\delta)\rfloor$  tests (23 tests when  $\delta =$

0.05) according to Eq. (43). For order-3 cluster states and Union Jack states, which are three-colorable, it suffices to perform  $\lfloor 16.3\ln (4 / 3\delta)\rfloor$  tests (53 tests when  $\delta = 0.05$ ).

Although detection or certification of GME has been discussed in many works, our approach is appealing for at least four reasons. First, our approach is based on quantum state verification, which can provide more precise information about the state than entanglement detection usually based on witness operators. Such information is crucial to many practical applications, including MBQC. Second, our approach requires much fewer measurement settings and tests than most previous works on the detection of GME. Third, given a significance level, we can determine the number of required tests explicitly, which is not the case for most previous works. Fourth, our approach can be applied to both nonadversarial and adversarial scenarios.

# VII. VERIFICATION OF QUDIT HYPERGRAPH STATES

Most previous verification protocols for hypergraph states only apply to the qubit case [25,35]. Here we show that the cover protocol and hedged cover protocol can also be applied to qudit hypergraph states with minor modifications; in addition, most conclusions on the verification of qubit hypergraph states are still applicable in the qudit case. This merit is particularly appealing to both theoretical studies and practical applications.

# A. Qudit hypergraphs

In the case of qudit, we need to revise the definition of hypergraphs to take into account multiplicities of hyperedges. Now a hypergraph  $G = (V,E,m_{E})$  (also known as multihypergraph in the literature) is characterized by a set of vertices  $V$  and a set of hyperedges  $E\subset \mathcal{P}(V)$  together with multiplicities specified by  $m_E = (m_e)_{e\in E}$ , where  $m_e\in \mathbb{Z}_d$  with  $m_e\neq 0$  and  $\mathbb{Z}_d$  is the ring of integers modulo  $d$  [21,22]. Nevertheless, almost all graph theoretic concepts considered in this work do not depend on the multiplicity vector  $m_E$  and are defined in the same way as in the qubit case. To be specific, these concepts include the order of a hyperedge and the hypergraph, the adjacency relation, the degree of a vertex and the hypergraph, clique and clique number, independent set and independence number, (weighted) independence cover, cover strength, independence degree, and (fractional) chromatic number. Therefore, Proposition 1 and its proof are applicable without any modification.

# B. Qudit hypergraph states

The qudit Pauli group (also known as the Heisenberg-Weyl group) is generated by the following two generalized

Pauli operators:

$$
X = \sum_ {j \in \mathbb {Z} _ {d}} | j + 1 \rangle \langle j |, \quad Z = \sum_ {j \in \mathbb {Z} _ {d}} \omega^ {j} | j \rangle \langle j |, \tag {45}
$$

where  $\omega = \mathrm{e}^{2\pi \mathrm{i} / d}$  is a primitive  $d$ th root of unity. Given any qudit hypergraph  $G = (V,E,m_E)$  with  $n$  vertices, we can construct an  $n$ -qudit hypergraph state  $|G\rangle$  as follows: prepare the quantum state  $|+\rangle \coloneqq (1 / \sqrt{d})\sum_{j\in \mathbb{Z}_d}|j\rangle$  (eigenstate of  $X$  with eigenvalue 1) for each vertex of  $G$  and apply  $m_e$  times the generalized controlled-  $Z$  operation  $CZ_{e}$  on the vertices of each hyperedge  $e$  [21,22], that is,

$$
| G \rangle = \left(\prod_ {e \in E} C Z _ {e} ^ {m _ {e}}\right) | + \rangle^ {\otimes n}. \tag {46}
$$

To simplify the notation, here we only give the expression of  $CZ_{e}$  when  $e = \{1,2,\ldots ,k\}$ , in which case we have

$$
C Z _ {e} := \sum_ {j _ {1}, j _ {2}, \dots , j _ {k} \in \mathbb {Z} _ {d}} \omega^ {j _ {1} j _ {2} \dots j _ {k}} | j _ {1}, j _ {2}, \dots , j _ {k} \rangle \langle j _ {1}, j _ {2}, \dots , j _ {k} |; \tag {47}
$$

the general case is defined analogously.

Alternatively,  $|G\rangle$  is the unique eigenstate (up to a global phase factor) with eigenvalue 1 of the  $n$  commuting (nonlocal) stabilizer operators [21,22]

$$
K _ {j} = X _ {j} \otimes \prod_ {e \in E | e \ni j} C Z _ {e \backslash \{j \}} ^ {m _ {e}}, \quad j = 1, 2, \dots , n. \tag {48}
$$

Note that  $K_{j}^{d} = 1$ , so all eigenvalues of  $K_{j}$  are powers of  $\omega$ . As in the qubit case, graph theoretic concepts pertinent to the hypergraph  $G$  also apply to the corresponding hypergraph state  $|G\rangle$ .

# C. Verification of qudit hypergraph states

The following protocol for verifying qudit hypergraph states is a simple variation of the cover protocol for verifying qubit hypergraph states presented in Sec. IV B.

Let  $G = (V, E, m_E)$  be a qudit hypergraph and  $|G\rangle$  the associated hypergraph state. Choose an independence cover  $\mathcal{A} = \{A_1, A_2, \ldots\}$  of  $G$  and let  $\overline{A}_l := V \setminus A_l$  be the complement of  $A_l$  in  $V$ . Then we can construct a verification protocol with  $|\mathcal{A}|$  distinct tests (measurement settings): the  $l$ th test consists in measuring  $X_j$  for all  $j \in A_l$  and measuring  $Z_k$  for all  $k \in \overline{A}_l$ . By measuring  $X_j$  ( $Z_k$ ) we mean the measurement on the eigenbasis of  $X_j$  ( $Z_k$ ). The measurement outcome on the  $a$ th qubit for  $a = 1, 2, \ldots, n$  can be written as  $\omega^{o_a}$ , where  $o_a \in \mathbb{Z}_d$ . Note that  $X_j$  and  $Z_k$  commute with  $K_i$  for all  $i, j \in A_l$  and  $k \in \overline{A}_l$ . In addition,

the joint eigenstate of  $X_{j}$  and  $Z_{k}$  corresponding to the outcome  $\{o_a\}$  is an eigenstate of  $K_{i}$ , whose eigenvalue is given by  $\omega^{t_i}$  with

$$
t _ {i} = o _ {i} + \sum_ {e \in E | e \ni i} m _ {e} \prod_ {k \in e, k \neq i} o _ {k} \tag {49}
$$

according to Eq. (48). The test is passed if  $\omega^{t_i} = 1$  for all  $i\in A_l$ . The projector onto the pass eigenspace associated with the  $l$ th test reads

$$
P _ {l} = \prod_ {i \in A _ {l}} \left(\frac {1}{d} \sum_ {b \in \mathbb {Z} _ {d}} K _ {i} ^ {b}\right). \tag {50}
$$

A state can pass all tests if and only if it is stabilized by  $K_{i}$  for all  $i \in V$ . So only the target state  $|G\rangle$  can pass all tests with certainty as desired.

Suppose the  $l$ th test  $P_{l}$  (associated with  $A_{l}$ ) is applied with probability  $\mu_{l}$ . The efficiency of the resulting protocol is determined by the spectral gap of the verification operator  $\Omega (\mathcal{A},\mu) = \sum_{l = 1}\mu_lP_l$ . Here the common eigenbasis of  $K_{i}$  for  $i\in V$  also form an eigenbasis of  $\Omega (\mathcal{A},\mu)$ . Each eigenstate  $|\Psi_x\rangle$  in this basis is specified by a string  $x\in \mathbb{Z}_d^n$  and satisfies  $K_{i}|\Psi_{x}\rangle = \omega^{x_{i}}|\Psi_{x}\rangle$ . The corresponding eigenvalue of  $\Omega (\mathcal{A},\mu)$  reads

$$
\lambda_ {x} = \sum_ {l \mid \operatorname {s u p p} (x) \subset \bar {A} _ {l}} \mu_ {l}, \tag {51}
$$

where  $\operatorname{supp}(x) \coloneqq \{i \mid x_i \neq 0\}$ . The second largest eigenvalue of  $\Omega(\mathcal{A}, \mu)$  can be attained when  $x_i = 0$  for all  $i \in V$  except for one of them. So we have

$$
\beta (\Omega (\mathscr {A}, \mu)) = \max  _ {i \in V} \sum_ {l \mid \bar {A} _ {l} \ni i} \mu_ {l}, \tag {52}
$$

$$
v (\Omega (\mathcal {A}, \mu)) = \min  _ {i \in V} \sum_ {l \mid A _ {l} \ni i} \mu_ {l} = s (\mathcal {A}, \mu), \tag {53}
$$

as in the case of qubit hypergraph states. Similarly, the smallest eigenvalue of  $\Omega (\mathcal{A},\mu)$  is attained when all dits of  $x$  are nonzero, in which case we have  $\lambda_{x} = 0$ . Again, the verification operator  $\Omega (\mathcal{A},\mu)$  is always singular.

In addition, the hedged cover protocol can be generalized to quudit hypergraph states according to the same recipe presented in Sec. VB. Moreover, Theorem 1 and Eqs. (19)-(37) are still applicable in the quudit case.

# VIII. SUMMARY

We propose a simple protocol—the cover protocol—for verifying (qubit and qudit) hypergraph states, which requires only two distinct Pauli measurements for each party. This protocol is dramatically more efficient than all previous protocols based on local measurements and

is comparable to the best protocol based on entangling measurements. In general, the overhead is bounded by the chromatic number and degree of the underlying hypergraph. For many interesting hypergraph states, including Union Jack states, the number of required tests is even independent of the number of qubits. Our protocol enables the verification of hypergraph states and GME of thousands of qubits, which is instrumental to many applications in quantum information processing. Moreover, we propose the hedged cover protocol, which can be applied to verify hypergraph states and GME in the adversarial scenario with almost the same efficiency as in the nonadversarial scenario. This protocol is thus particularly appealing to many applications that require high-security conditions, such as blind MBQC and quantum networks.

# ACKNOWLEDGMENTS

We are grateful to a referee for pointing out the relation between the independence degree and fractional chromatic number. H.Z. is grateful to Zhibo Hou and Jiangwei Shang for discussions. This work is supported by the National Natural Science Foundation of China (Grant No. 11875110). H.Z. acknowledges financial support from the Excellence Initiative of the German Federal and State Governments Zukunftskonzept (ZUK 81) and the Deutsche Forschungsgemeinschaft (DFG) in the early stage of this work. M.H. is supported in part by Fund for the Promotion of Joint International Research (Fostering Joint International Research) Grant No. 15KK0007, Japan Society for the Promotion of Science (JSPS) Grant-in-Aid for Scientific Research (A) No. 17H01280, (B) No. 16KT0017, and Kayamori Foundation of Informational Science Advancement.

# Appendix

In this appendix, we prove Proposition 1 and provide additional details on hypergraphs, which are instructive to understanding the verification of hypergraph states. Then we present an independent proof of Theorem 2, which was originally proved in Ref. [45]. Finally, we compare our work with previous works and demonstrate the advantage of our approach.

# APPENDIX A: COVER STRENGTHS AND INDEPENDENCE DEGREES OF HYPERGRAPHS

In this section we prove Proposition 1 and provide additional details on independence degrees and related invariants of hypergraphs. Here we would like to thank an anonymous referee for pointing out that the independence degree is actually equal to the inverse fractional chromatic number [41]. In view of this fact, all conclusions presented here are well known. For the convenience of the readers, nevertheless, we give elementary proofs of

the main conclusions, assuming little background on graph theory.

# 1. Fractional coloring and fractional chromatic number

Let  $G = (V, E)$  be a hypergraph with vertex set  $V$  and hyperedge set  $E$ . Let  $\mathcal{I}$  be the set of all independent sets of  $G$ . A fractional coloring of  $G$  [40,41] is a mapping  $g$  from  $\mathcal{I}$  to nonnegative real numbers such that

$$
\sum_ {A \in \mathcal {I} (G), A \ni j} g (A) \geq 1 \quad \forall j \in V. \tag {A1}
$$

The weight  $w(g)$  of the fractional coloring  $g$  is defined as the sum of  $g(A)$  over all independent sets in  $\mathcal{I}$ , that is,  $w(g) = \sum_{A \in \mathcal{I}} g(A)$ . The fractional chromatic number  $\chi_f(G)$  of  $G$  is the minimum weight over all fractional colorings of  $G$  [41]. Note that there are several equivalent definitions of the fractional chromatic number; here we have chosen the definition that is the most convenient for the current study. The fractional chromatic number would reduce to the usual chromatic number if  $g(A)$  for each  $A \in \mathcal{I}$  could take on only two possible values 0 and 1.

Given any fractional coloring  $g$  of  $G$ , we can construct a weighted independence cover  $(\mathcal{I}, \mu)$  of  $G$  by setting  $\mu(A) = w(g)^{-1} g(A)$ . Here the set  $\mathcal{I}$  appearing in  $(\mathcal{I}, \mu)$  can be replaced by the independence cover  $\{A \in \mathcal{I} | g(A) > 0\}$ . Conversely, given any weighted independence cover  $(\mathcal{A}, \mu)$  of  $G$  with nonzero cover strength  $s(\mathcal{A}, \mu)$ , we can construct a fractional coloring  $g$  of  $G$  by setting

$$
g (A) = \frac {\mu (A)}{s (\mathcal {A} , \mu)}, \quad A \in \mathcal {A}, \tag {A2}
$$

$$
g (A) = 0 \quad \forall A \in (\mathcal {I} \backslash \mathcal {A}). \tag {A3}
$$

Note that  $\mathcal{A}$  can also be replaced by  $\mathcal{I}$  by adding zero components in  $\mu$ ; the resulting weighted independence cover is taken to be identical to the original one. The above discussions establish a one-to-one correspondence between weighted independence covers of  $G$  with nonzero cover strengths and fractional colorings  $g$  which can saturate the inequality in Eq. (A1) for at least one vertex  $j \in V$ . Therefore, the independence degree is equal to the inverse fractional chromatic number [41], that is,

$$
\gamma (G) = \frac {1}{\chi_ {f} (G)}. \tag {A4}
$$

In view of the above observations, every fractional coloring of  $G$  can be applied to construct a cover protocol for verifying the hypergraph state  $|G\rangle$  as presented in the main text; conversely, every cover protocol determines a fractional coloring of  $G$ . So a cover protocol may also be referred to as a fractional coloring protocol.

# 2. Proof of Proposition 1

Here we present an elementary and self-contained proof of Proposition 1. This conclusion is well known; in particular, the inequalities concerning the independence degree can be found in Chapter 3 of Ref. [41] in view of the relation  $\gamma (G) = 1 / \chi_f(G)$  in Eq. (A4). The inequality  $1 / (\Delta (G) + 1)\leq 1 / \chi (G)$  amounts to  $\chi (G)\leq \Delta (G) + 1$  and follows from a well-known greedy algorithm, which produces a coloring of  $G$  with no more than  $\Delta (G) + 1$  colors. The following algorithm is a simplified version of the Dsatur algorithm introduced in Ref. [43]. Let  $v_{1},v_{2},\ldots ,v_{n}$  be the vertices of  $G$  whose degrees are in decreasing order. Use natural numbers to represent colors and assign color 1 to  $v_{1}$ . The colors of other vertices are assigned inductively as follows. Suppose the colors of  $v_{1},v_{2},\ldots ,v_{j - 1}$  for  $j\leq n$  have been assigned. Then the color number of  $v_{j}$  is the smallest natural number that is different from the color numbers of those vertices in the set  $\{v_{1},v_{2},\dots ,v_{j - 1}\}$  that are adjacent to  $v_{j}$ . Since  $v_{j}$  has at most min  $\{\deg (v_j),j - 1\}$  neighbors in this set, where  $\deg (v_j)$  is the degree of  $v_{j}$ , the color number of  $j$  is at most min  $\{\deg (v_j) + 1,j\}$ . Therefore,

$$
\chi (G) \leq \max  _ {j} \min  \left\{\deg \left(v _ {j}\right) + 1, j \right\} \leq \Delta (G) + 1. \tag {A5}
$$

The inequality  $\gamma (G)\geq 1 / \chi (G)$  follows from the observation that any independence cover (or coloring) of  $G$  with  $\chi (G)$  elements and uniform weights has cover strength  $1 / \chi (G)$ . Alternatively, this inequality follows from the relation  $\gamma (G) = 1 / \chi_f(G)$  and the inequality  $\chi_f(G)\leq \chi (G)$  [41].

To prove the inequality  $\gamma (G)\leq \alpha (G) / |V|$ , let  $(\mathcal{A},\mu)$  be an arbitrary independence cover. Then we have

$$
\begin{array}{l} | V | s (\mathscr {A}, \mu) = | V | \min  _ {j \in V} \sum_ {l \mid A _ {l} \ni j} \mu_ {l} \leq \sum_ {j} \sum_ {l \mid A _ {l} \ni j} \mu_ {l} \\ = \sum_ {l} \mu_ {l} \left| A _ {l} \right| \leq \alpha (G) \sum_ {l} \mu_ {l} = \alpha (G), \quad (A 6) \\ \end{array}
$$

which implies that  $\gamma (G)\leq \alpha (G) / |V|$ .

To prove the inequality  $\gamma (G)\leq 1 / \varpi (G)$ , let  $V_{C}$  be a subset of  $\varpi (G)$  vertices in  $V$  that forms a clique. Then

$$
\begin{array}{l} \varpi (G) s (\mathcal {A}, \mu) = \varpi (G) \min  _ {j \in V} \sum_ {l | A _ {l} \ni j} \mu_ {l} \leq \sum_ {j \in V _ {C}} \sum_ {l | A _ {l} \ni j} \mu_ {l} \\ \leq \sum_ {l} \mu_ {l} = 1, \tag {A7} \\ \end{array}
$$

where the second inequality follows from the fact that each independent set  $A_{l}$  can contain at most one vertex in the clique  $V_{C}$ .

# 3. Cover strengths of colorings and minimal covers

Let  $G = (V, E)$  be a hypergraph and  $(\mathcal{A}, \mu)$  a weighted independence cover constructed from a coloring  $\mathcal{A}$ , assuming that no independent set in  $\mathcal{A}$  is empty (note that empty independent sets cannot increase the cover strength). Then each vertex of  $V$  is contained in only one independent set in  $\mathcal{A}$ , which implies that

$$
s (\mathscr {A}, \mu) = \min  _ {l} \mu_ {l} \leq | \mathscr {A} | ^ {- 1} \leq \chi (G) ^ {- 1}. \tag {A8}
$$

Here the first inequality is saturated if and only if all weights  $\mu_l$  are equal, and the second inequality is saturated if and only if the coloring  $\mathcal{A}$  is optimal in the sense that no other coloring of  $G$  requires fewer colors.

Next, let  $(\mathcal{A},\mu)$  be a weighted independence cover of  $G$  constructed from a minimal cover  $\mathcal{A}$ . By "minimal" we mean that any proper subset  $\mathcal{A}'$  of  $\mathcal{A}$  is not a cover of  $G$  because the union of independent sets in  $\mathcal{A}'$  does not coincide with the vertex set  $V$ . In other words, for any  $A_{l}$  in  $\mathcal{A}$ , there exists a vertex  $j\in V$  such that  $j\in A_l$  and  $j\notin A_k$  for all  $k\neq l$ . Therefore,

$$
s (\mathscr {A}, \mu) = \min  _ {l} \mu_ {l} \leq | \mathscr {A} | ^ {- 1} \leq \chi (G) ^ {- 1} \tag {A9}
$$

as in Eq. (A8). Again the first inequality is saturated if and only if all weights  $\mu_l$  are equal; the second inequality is saturated if and only if  $|\mathcal{A}| = \chi(G)$ , in which case an optimal coloring of  $G$  can be constructed from  $\mathcal{A}$  by deleting some vertices in some independent sets if  $\mathcal{A}$  is not yet a coloring.

In view of the above discussion, to maximize the cover strength it is always beneficial to choose uniform weights when  $\mathcal{A}$  is a coloring or minimal independence cover. In addition, the cover strength of any such cover is upper bounded by  $1 / \chi (G)$ , which can be saturated.

# 4. Independence degrees of odd cycles

Let  $C_n$  be a cycle with  $n$  vertices, where  $n$  is an odd integer. According to Proposition 3.1.2 in Ref. [41], the fractional chromatic number of  $C_n$  reads

$$
\chi_ {f} \left(C _ {n}\right) = \frac {2 n}{n - 1}. \tag {A10}
$$

Thanks to Eq. (A4), the independence degree of  $C_n$  is thus given by

$$
\gamma \left(C _ {n}\right) = \frac {n - 1}{2 n} = \frac {1}{2} - \frac {1}{2 n}, \tag {A11}
$$

which increases monotonically with  $n$ . This conclusion indicates that overcomplete covers of some hypergraph  $G$  can have cover strengths larger than  $1 / \chi (G)$  and that the inequality  $\gamma (G)\geq 1 / \chi (G)$  in Proposition 1 is, in general, strict. By contrast, the cover strength of any coloring

or minimal cover of  $C_n$  is upper bounded by  $1/3$  given that  $\chi(C_n) = 3$ . So it is indeed advantageous to consider weighted independence covers (or fractional colorings) beyond usual colorings for some hypergraphs. These observations are of interest to constructing efficient verification protocols for hypergraph states (including graph states in particular) in view of Theorem 1 in the main text.

To prove Eq. (A11), note that  $\alpha(C_n) = (n - 1)/2$ , so that  $\gamma(C_n) \leq (n - 1)/(2n)$  according to Proposition 1. This upper bound can be saturated by the equal-weight cover composed of the  $n$  independent sets

$$
A _ {j} = \{j, j + 2, \dots , j + n - 3 \}, \quad j = 1, 2, \dots , n. \tag {A12}
$$

Here vertex labels  $j$  and  $j + n$  are identified.

# APPENDIX B: PROOF OF THEOREM 2

In this section we present an independent proof of Theorem 2, which was originally proved in Ref. [45]. This theorem is an immediate consequence of Lemmas 2 and 3 presented below. Before stating and proving these auxiliary results, we need to introduce a few additional concepts. Let  $|\Psi \rangle \langle \Psi |$  be an  $n$ -partite pure state of the parties  $V = \{1,2,\dots,n\}$ . For each nonempty proper subset  $A$  of  $V$ , denote by  $\varrho_{A}$  the reduced state of  $|\Psi \rangle \langle \Psi |$  over the parties in  $A$ , that is,  $\varrho_{A} = \mathrm{tr}_{\overline{A}}(|\Psi \rangle \langle \Psi |)$ , where  $\overline{A} = V \setminus A$  is the complement of  $A$  in  $V$ . Define

$$
\kappa (| \Psi \rangle) := \max  _ {A} \| \varrho_ {A} \|, \tag {B1}
$$

where  $\| \varrho_{A}\|$  denotes the operator norm (the largest eigenvalue) of  $\varrho_{A}$  and the maximum is taken over all nonempty proper subsets  $A$  of  $V$ . Note that  $\kappa(|\Psi\rangle)$  is invariant under local unitary transformations. Given a hypergraph  $G$ , define  $\kappa(G) := \kappa(|G\rangle)$ .

Lemmas 1 and 2 below were known previously [2], but here we provide self-contained proofs for completeness.

Lemma 1.-The pure state  $|\Psi \rangle$  is GME if and only if  $\kappa (|\Psi \rangle) < 1$ .

To prove the lemma, it is equivalent to prove the statement that the state  $|\Psi \rangle$  is biseparable if and only if  $\kappa (|\Psi \rangle) = 1$ . If  $\kappa (|\Psi \rangle) = 1$ , then  $|\Psi \rangle$  has a nontrivial reduced state that is pure, which implies that  $|\Psi \rangle$  is biseparable. Conversely, if  $|\Psi \rangle$  is biseparable, then it has a nontrivial reduced state that is pure, which implies that  $\kappa (|\Psi \rangle) = 1$ .

Lemma 2.—Suppose  $|\Psi \rangle$  is GME and a state  $\rho$  satisfies  $\langle \Psi |\rho |\Psi \rangle >\kappa (|\Psi \rangle)$ . Then  $\rho$  is GME.

Suppose  $|\Phi \rangle$  is an arbitrary pure state that is biseparable over the partition  $A$  and  $\overline{A}$ , that is,  $|\Phi \rangle$  has the form

$|\Phi \rangle = |\Phi_A\rangle \otimes |\Phi_{\overline{A}}\rangle$  . Then

$$
| \langle \Psi | \Phi \rangle | ^ {2} \leq \left\langle \Phi_ {A} \mid \varrho_ {A} \mid \Phi_ {A} \right\rangle \leq \| \varrho_ {A} \| \leq \kappa (| \Psi \rangle), \tag {B2}
$$

where  $\varrho_{A}$  is the reduced state of  $|\Psi \rangle \langle \Psi |$  over the parties in  $A$ . If  $\rho$  is not GME, then it is a convex combination of biseparable pure states, so that  $\langle \Psi |\rho |\Psi \rangle \leq \kappa (|\Psi \rangle)$ . Therefore,  $\rho$  is GME whenever  $\langle \Psi |\rho |\Psi \rangle >\kappa (|\Psi \rangle)$ .

Lemma 3. Suppose  $G = (V, E)$  is a connected order- $k$  hypergraph with  $k \geq 2$ . Then  $\kappa(G) \leq 1 - 2^{1 - k}$ .

This lemma is an easy consequence of Lemma 4 below. When  $|G\rangle$  is a connected graph state, Lemma 3 is known much earlier [2,46,47], in which case the bound  $\kappa (G)\leq 1 - 2^{1 - k}$  with  $k = 2$  is always saturated. This conclusion follows from the fact that any nontrivial reduced density matrix of the graph state  $|G\rangle \langle G|$  is proportional to a projector of rank at least 2.

Besides the application in proving Theorem 2, Lemma 3 shows that any order- $k$  hypergraph state  $|G\rangle$  with  $k \geq 2$  and  $\kappa(G) = 1 - 2^{1-k}$  is not equivalent to any order- $k'$  hypergraph state with  $k' < k$  under local unitary transformations.

The bound  $\kappa(G) \leq 1 - 2^{1 - k}$  is saturated if  $G$  contains an order- $k$  leaf. Here a leaf of  $G$  is a vertex that belongs to only one hyperedge with order at least 2. The order of the leaf is the order of this unique hyperedge. In this case  $\|\varrho_A\| = 1 - 2^{1 - k}$  when  $A$  is composed of the leaf. To verify this claim, it suffices to consider the scenario in which  $n = |V| = k$  and  $G$  contains a single hyperedge (which necessarily has order  $k$ ). Now it is straightforward to verify that each single-qubit reduced state of  $|G\rangle$  has two eigenvalues equal to  $1 - 2^{1 - k}$  and  $2^{1 - k}$ , respectively, so the bound  $\kappa(G) \leq 1 - 2^{1 - k}$  is indeed saturated. In particular, the above observation implies that  $\kappa(G) = 1 - 2^{1 - k}$  when  $|G\rangle$  is a 1D order- $k$  cluster state. Straightforward calculations also show that the bound  $\kappa(G) \leq 1 - 2^{1 - k}$  with  $k = 3$  is saturated for 2D order-3 cluster states and Union Jack states for which  $\kappa(G) = 3/4$ .

Lemma 4. Suppose  $G = (V, E)$  is a hypergraph and  $A$  is any nonempty proper subset of  $V$  that is adjacent to  $\overline{A}$ . Let  $\varrho_{A}$  be the reduced state of  $|G\rangle$  over the parties in  $A$ . Then  $\| \varrho_{A} \| \leq 1 - 2^{1 - k}$ , where  $k$  is the maximum order of hyperedges that connect  $A$  and  $\overline{A}$ .

Here two disjoint nonempty subsets  $A$  and  $B$  of the vertex set  $V$  of  $G$  are adjacent if  $E$  contains a hyperedge that connects a vertex in  $A$  and a vertex in  $B$ .

Lemma 4 can be proved by induction. To start with, let  $n = |V|$ ; then  $n \geq k \geq 2$  by assumption. It is straightforward to verify that the lemma holds when  $n = k = 2$ . Suppose the lemma holds for  $2 \leq k \leq n \leq n_0$  with  $n_0 \geq 2$ . We prove that the lemma also holds for  $2 \leq k \leq n = n_0 + 1$ .

It is instructive to note that  $\| \varrho_{A}\|$  does not change if we add or delete hyperedges among vertices in  $A$  or hyperedges among vertices in  $\overline{A}$ . So we may assume that  $G$  has

neither hyperedges among vertices in  $A$  nor hyperedges among vertices in  $\overline{A}$ ; in other words, every hyperedge of  $G$  contains at least one vertex in  $A$  and one vertex in  $\overline{A}$ . Then  $k$  is equal to the order of  $G$ . In addition, we may assume that  $G$  has no isolated vertices. Note that the order of  $G$  does not change if any isolated vertex, say  $j$ , is deleted; meanwhile,  $\varrho_{A}$  does not change after this deletion if  $j \in \overline{A}$ , while  $\| \varrho_{A} \| = \| \varrho_{A \setminus \{j\}} \|$  if  $j \in A$ . Furthermore, we may assume  $|A| \leq n - 2$  without loss of generality given that  $\| \varrho_{A} \| = \| \varrho_{\overline{A}} \|$  and  $n \geq 3$ . By relabeling the parties if necessary, we may assume that  $n \notin A$ , that is,  $n \in \overline{A}$ .

According to Proposition 7.16 of Ref. [49],

$$
\varrho_ {V \backslash \{n \}} = \frac {1}{2} \left(\left| G _ {0} \right\rangle \left\langle G _ {0} \right| + \left| G _ {1} \right\rangle \left\langle G _ {1} \right|\right), \tag {B3}
$$

where  $G_0, G_1$  are subhypergraphs of  $G$  defined as follows:

$$
G _ {0} = (V \backslash \{n \}, \{e \in E | n \notin e \}),
$$

$$
G _ {1} = (V \backslash \{n \}, \{e \in E \mid n \notin e \} \Delta \{e \backslash \{n \} \mid n \in e \in E \}). \tag {B4}
$$

Here  $A\Delta B$  denotes the symmetric difference of  $A$  and  $B$ , that is,  $(A\cup B)\setminus (A\cap B)$ . Literally,  $G_{0}$  is the subhypergraph of  $G$  obtained by deleting the vertex  $n$  and all the hyperedges containing  $n$ ;  $G_{1}$  is the subhypergraph of  $G$  obtained by deleting the vertex  $n$ , shrinking all the hyperedges containing  $n$ , and then deleting repeated hyperedges.

Let  $B = V \setminus \{n\} \setminus A$ ; note that  $B$  is nonempty due to the assumption  $|A| \leq n - 2$ . In addition,  $A \cup B = V \setminus \{n\}$  is the vertex set of both  $G_0$  and  $G_1$ . Let  $\varrho_0 = \mathrm{tr}_B(|G_0\rangle \langle G_0|)$  and  $\varrho_1 = \mathrm{tr}_B(|G_1\rangle \langle G_1|)$ . Then  $\varrho_A = (\varrho_0 + \varrho_1)/2$  and

$$
\left\| \varrho_ {A} \right\| \leq \frac {1}{2} \left(\left\| \varrho_ {0} \right\| + \left\| \varrho_ {1} \right\|\right). \tag {B5}
$$

If  $A$  is adjacent to  $B$  with respect to both  $G_0$  and  $G_1$ , then the induction hypothesis implies that

$$
\left\| \varrho_ {0} \right\| \leq 1 - 2 ^ {1 - k _ {0}} \leq 1 - 2 ^ {1 - k},
$$

$$
\left\| \varrho_ {1} \right\| \leq 1 - 2 ^ {1 - k _ {1}} \leq 1 - 2 ^ {1 - k}, \tag {B6}
$$

which in turn implies that  $\| \varrho_A\| \leq 1 - 2^{1 - k}$ . Here  $k_{0}$  and  $k_{1}$  denote the orders of  $G_{0}$  and  $G_{1}$ , respectively, which satisfy  $k_{0}, k_{1} \leq k$ .

If  $A$  is not adjacent to  $B$  with respect to  $G_0$ , then  $G_0$  has no hyperedges, which implies that all hyperedges of  $G$  contain the vertex  $n$ . Recall that by assumption  $G$  has neither hyperedges among vertices in  $A$  nor hyperedges among vertices in  $\overline{A}$ . Consequently,  $G_1$  has order at most  $k - 1$ . If, in addition,  $A$  is adjacent to  $B$  with respect to  $G_1$ ,

then  $\| \varrho_1\| \leq 1 - 2^{2 - k}$ , which implies that

$$
\left\| \varrho_ {A} \right\| \leq \frac {1}{2} \left(\left\| \varrho_ {0} \right\| + \left\| \varrho_ {1} \right\|\right) \leq \frac {1}{2} \left(1 + 1 - 2 ^ {2 - k}\right) = 1 - 2 ^ {1 - k}. \tag {B7}
$$

Otherwise, if  $A$  is not adjacent to  $B$  with respect to  $G_{1}$ , then no hyperedge of  $G$  contains any vertex in  $B$ ; in other words, all vertices of  $B$  are isolated with respect to  $G$ , which contradicts our assumption.

It remains to consider the case in which  $A$  is adjacent to  $B$  with respect to  $G_0$ , but not adjacent to  $B$  with respect to  $G_1$ . In view of Eq. (B4), we conclude that  $G_0$  has order at most  $k - 1$  since, otherwise, any order- $k$  hyperedge of  $G_0$  (which necessarily connects  $A$  and  $B$ ) would also be a hyperedge of  $G_1$ . Therefore,

$$
\left\| \varrho_ {A} \right\| \leq \frac {1}{2} \left(\left\| \varrho_ {0} \right\| + \left\| \varrho_ {1} \right\|\right) \leq \frac {1}{2} \left(1 - 2 ^ {2 - k} + 1\right) = 1 - 2 ^ {1 - k}. \tag {B8}
$$

This observation completes the proof of Lemma 4.

# APPENDIX C: COMPARISON WITH PREVIOUS WORKS

In this section we discuss the connections and distinctions between our work and entanglement detection. We then compare our protocols for verifying hypergraph states with a number of previous works, including DFE [34] and Refs. [9,25,31,32,35].

# 1. Quantum state verification and entanglement detection

In the main text, we introduce a simple and efficient protocol for verifying general hypergraph states. Our protocol can also be applied to detecting GME, though it is not necessarily optimized for this purpose. In the literature, there are many works on the detection of entanglement, including GME in particular [2]. The main distinction between state verification and entanglement detection lies in the motivations, which are reflected in the following two questions.

(1) Is the quantum state prepared good enough for a given task, such as quantum computation, quantum communication, or quantum metrology?  
(2) Is the quantum state prepared GME?

The main motivation of the current work is to provide an efficient tool for answering the first question, while most works on entanglement detection focus on the second question directly. Question 2 is definitely interesting in itself since GME is a key resource in quantum information processing and a focus of foundational studies. In addition, demonstrating GME in experiments is usually highly

nontrivial and may serve as a signature of the advance in quantum information science. On the other hand, although there are intimate connections between the two questions, the answer to question 2 is, in general, far from enough for answering question 1, which usually entails high fidelity with the target state. Instead of demonstrating certain quantum signature, eventually, we need to answer more specific and practical questions directly. Crucial to achieving this task is efficient quantum state verification, which is the focus of this work.

In addition, most works on entanglement detection are based on the expectation values of certain witness operators and usually do not discuss the number of tests required to make a conclusion. With the cover protocol, by contrast, we can not only provide more precise information about the quantum state prepared, but also determine the explicit number of tests required. In addition, our approach can be applied to the adversarial scenario, which is appealing to many applications that require high-security conditions.

# 2. Comparison with direct-fidelity estimation Ref. [34]

In this section we compare our cover protocol with DFE introduced by Flammia and Liu [34]. Compared with the cover protocol, DFE can be applied to any pure state and thus has wider applications. The number of measurements required by DFE is smaller than tomography by a factor of  $D = 2^n$ , where  $n$  is the number of qubits. Moreover, this number does not increase with the number of qubits in the case of stabilizer states. From this perspective, DFE is very efficient and very useful. However, DFE has several drawbacks as mentioned below, which limit its applications to hypergraph states and many other states of quantum systems of more than 15 qubits.

(1) To apply DFE it is necessary to sample from the squared characteristic function defined on the discrete phase space of  $2^{2n}$  points. In general, it is not easy to compute and store this function for large quantum systems; also, it is not easy to implement the sampling even if the characteristic function is determined.  
(2) The number of potential measurement settings increases exponentially with the number of qubits even for stabilizer states. The number of actual measurement settings  $\lceil 1 / (\epsilon^2\delta)\rceil$  depends on the target infidelity  $\epsilon$  and significance level  $\delta$ . Specific measurement settings cannot be determined before implementing the protocol. Also, the total number of measurements cannot be determined in advance.  
(3) The average total number of measurements reads

$$
\begin{array}{l} N _ {\mathrm {D F E}} \approx 1 + \frac {1}{\epsilon^ {2} \delta} + \frac {2 g}{D \epsilon^ {2}} \ln (2 / \delta) \\ = 1 + \frac {1}{\epsilon^ {2} \delta} + \frac {2 \tilde {g}}{\epsilon^ {2}} \ln (2 / \delta), \tag {C1} \\ \end{array}
$$

where  $D = 2^n$ ,  $\tilde{g} = g / 2^n$ , and  $g$  is the number of points at which the characteristic function is nonzero [34]. It is known that  $g \geq D$  and the lower bound is saturated if and only if the target state is a stabilizer state. For a generic state  $g \approx D^2$ , so the number of measurements increases exponentially with  $n$ . As we see shortly, the exponential growth is also inevitable for many hypergraph states.

The number  $N_{\mathrm{DFE}}$  in Eq. (C1) can be reduced for a well-conditioned state  $\rho$ , which means either  $|\operatorname{tr}(\rho W_{x,z})| = 0$  or  $|\operatorname{tr}(\rho W_{x,z})| \geq c$  for all Pauli operators  $W_{x,z}$  [cf. Eq. (C4) below], where  $c$  is a positive constant whose inverse is upper bounded by a polynomial of  $n$ . In this case,  $N_{\mathrm{DFE}}$  can be reduced to  $O(\ln(1/\delta)/(c^2\epsilon^2))$ , though the quadratic scaling behavior with  $1/\epsilon$  does not change. However, many hypergraph states are not well conditioned. In addition, no simple way is known for determining whether a generic hypergraph state is well conditioned or not when the number of qubits is large.

To analyze the supports of the characteristic functions of hypergraph states, it is instructive to point out that any hypergraph state is a real equally weighted state and vice versa [19,20]. In other words, any  $n$ -qubit hypergraph state can be written as

$$
| \Psi_ {f} \rangle = 2 ^ {- n / 2} \sum_ {x = 0} ^ {2 ^ {n} - 1} (- 1) ^ {f (x)} | x \rangle , \tag {C2}
$$

where  $x$  is understood as a string in  $\{0,1\}^n$  and  $f$  is a Boolean function from  $\{0,1\}^n$  to  $\{0,1\}$ . For example, the Boolean function corresponding to the hypergraph state  $|G\rangle = \left(\prod_{e\in E}CZ_e\right)|+\rangle^{\otimes n}$  is given by

$$
f (x) = \sum_ {e \in E} \prod_ {j \in e} x _ {j}, \tag {C3}
$$

where the addition is modulo 2. Up to a phase factor, any  $n$ -qubit Pauli operator can be written as

$$
W _ {x, z} := \left(\prod_ {j = 1} ^ {n} X _ {j} ^ {x _ {j}}\right) \left(\prod_ {j = 1} ^ {n} Z _ {j} ^ {z _ {j}}\right), \quad x, z \in \{0, 1 \} ^ {n}, \tag {C4}
$$

where  $X_{j}$  and  $Z_{j}$  are the Pauli  $X$  and  $Z$  operators for the  $j$ th qubit. Here we are mainly interested in the absolute value of the characteristic function, so the overall phase factor does not matter. Calculation shows that

$$
\langle \Psi_ {f} | W _ {x, z} | \Psi_ {f} \rangle = \frac {1}{2 ^ {n}} \sum_ {u = 0} ^ {2 ^ {n} - 1} (- 1) ^ {f (u) + f (u + x)} (- 1) ^ {z \cdot u}, \tag {C5}
$$

where the addition  $u + x$  is modulo 2 and so is the product  $z \cdot u \coloneqq \sum_{j=1}^{n} z_j u_j$ . The cardinality of the support of the

characteristic function reads

$$
g (f) = \left| \left\{(x, z) \in \{0, 1 \} ^ {2 n} | \langle \Psi_ {f} | W _ {x, z} | \Psi_ {f} \rangle \neq 0 \right\} \right|. \tag {C6}
$$

In the rest of this section, we provide several concrete examples of hypergraph states for which  $\tilde{g} = g / 2^n$  increases exponentially with the number  $n$  of qubits, which means  $N_{\mathrm{DFE}}$  increases exponentially with  $n$ . First, consider the special hypergraph with only one hyperedge, which contains all  $n$  vertices. The corresponding Boolean function  $f_{n}$  reads

$$
f _ {n} (u) := \prod_ {j = 1} ^ {n} u _ {j} = \left\{ \begin{array}{l l} 1 & u = 1 1 \dots 1, \\ 0 & \text {o t h e r w i s e .} \end{array} \right. \tag {C7}
$$

In this case, we have

$$
\left. 2 ^ {n} \mid \left\langle \Psi_ {f _ {n}} \right| W _ {x, z} \mid \Psi_ {f _ {n}} \right\rangle \mid = \left\{ \begin{array}{l l} 2 ^ {n} & x = z = 0, \\ 2 ^ {n} - 4 & z = 0, x \neq 0, \\ 4 & x \neq 0, z \neq 0, x \cdot z = 0, \\ 0 & x \cdot z = 1, \text {o r} x = 0, z \neq 0, \end{array} \right. \tag {C8}
$$

which implies that

$$
g \left(f _ {n}\right) = 2 ^ {2 n - 1} - 2 ^ {n - 1} + 1, \quad \tilde {g} \approx 2 ^ {n - 1} - 2 ^ {- 1}. \tag {C9}
$$

So the number of measurements in Eq. (C1) reduces to

$$
N _ {\mathrm {D F E}} \approx 1 + \frac {1}{\epsilon^ {2} \delta} + \frac {2 ^ {n} - 1}{\epsilon^ {2}} \ln (2 / \delta), \tag {C10}
$$

which increases exponentially with the number of qubits. By contrast, the number of tests required by our cover protocol is at most  $\lceil (n / \epsilon) \ln(1 / \delta) \rceil$  by Eq. (22) in the main text, which is exponentially smaller than  $N_{\mathrm{DFE}}$ .

As another example, consider the tensor power  $|\Psi_{f_3}\rangle^{\otimes n / 3}$ , which corresponds to the hypergraph state with  $n / 3$  disjoint hyperedges of order 3, assuming that  $n$  is divisible by 3. In this case,

$$
g = g \left(f _ {3}\right) ^ {n / 3} = 2 9 ^ {n / 3} > 3 ^ {n}, \quad \tilde {g} = \frac {2 9 ^ {n / 3}}{2 ^ {n}} > \left(\frac {3}{2}\right) ^ {n}. \tag {C11}
$$

So the number of measurements in Eq. (C1) reduces to

$$
\begin{array}{l} N _ {\mathrm {D F E}} \approx 1 + \frac {1}{\epsilon^ {2} \delta} + \frac {2 \times 2 9 ^ {n / 3}}{2 ^ {n} \epsilon^ {2}} \ln (2 / \delta) \\ > 1 + \frac {1}{\epsilon^ {2} \delta} + \frac {2 \left(\frac {3}{2}\right) ^ {n}}{\epsilon^ {2}} \ln (2 / \delta), \tag {C12} \\ \end{array}
$$

which also increases exponentially with the number of qubits. By contrast, the number of tests required by the

cover protocol is  $\lceil (3 / \epsilon)\ln (1 / \delta)\rceil$ , which is again exponentially smaller than  $N_{\mathrm{DFE}}$ .

Furthermore, numerical calculations show that  $\tilde{g}$  increases exponentially with  $n$  for order-3 cluster states and Union Jack states on a chain or a two-dimensional lattice, so  $N_{\mathrm{DFE}}$  also increases exponentially with  $n$  for these states (cf. Fig. 2 in the main text). The number of tests required by the cover protocol is still  $\lceil (3 / \epsilon)\ln (1 / \delta)\rceil$

# 3. Comparison with Ref. [25]

Recently, Morimae, Takeuchi, and Hayashi [25] introduced a method for verifying hypergraph states in the adversarial scenario. They only considered the case in which all hyperedges have orders at most 3. Although their method may potentially be extended to more general settings, a direct extension of their approach entails exponential increase in the resource overhead with the order of the hypergraph. Even for order-3 hypergraph states, the resource overhead increases exponentially with the number of hyperedges (and thus the degree of the hypergraph). Another drawback of the MTH protocol is that even the target hypergraph state  $|G\rangle$  cannot pass the test with certainty. Consequently, the number of tests required increases quadratically with the inverse infidelity.

More specifically, suppose  $|G\rangle$  is an  $n$ -qubit hypergraph state to be verified. Let  $K_{j}$  be the stabilizer operator corresponding to vertex  $j$  as defined in Eq. (10) in the main text; let  $r_{j}$  be the number of order-3 hyperedges that contain the vertex  $j$ . The MTH verification protocol is composed of  $n$  stabilizer tests. For each stabilizer  $K_{j}$ , MTH devised a test, which requires  $4^{r_{j}}$  potential measurement settings. The total number of potential measurement settings is  $\sum_{j=1}^{n} 4^{r_{j}}$ , which increases exponentially with the number of order-3 hyperedges. MTH also set a criterion such that the probability of a state  $\rho$  to satisfy the criterion is given by

$$
p _ {j} = \frac {1}{2} + \frac {\operatorname {t r} \left(\rho K _ {j}\right)}{2 ^ {r _ {j} + 1}} = \frac {1}{2} + \frac {1 - a _ {j}}{2 ^ {r _ {j} + 1}}, \tag {C13}
$$

where  $a_{j} \coloneqq 1 - \mathrm{tr}(\rho K_{j})$  satisfies  $0 \leq a_{j} \leq 2$ . Although the target state  $|G\rangle$  can attain the maximum probability  $(1/2) + (1/2^{r_{j} + 1})$ , it generally cannot satisfy the criterion with certainty. Suppose the test is performed  $N_{j}$  times, and the criterion is satisfied  $t_{j}$  times. Then the stabilizer test is passed if the frequency  $f_{j} = t_{j} / N_{j}$  satisfies

$$
f _ {j} \geq \frac {1}{2} + \frac {1 - \theta}{2 ^ {r _ {j} + 1}}, \tag {C14}
$$

where  $\theta$  is a small positive constant. The state  $\rho$  is accepted if it can pass all the stabilizer tests. The choice of  $\theta$  needs to guarantee that the target state  $|G\rangle$  can pass all the tests with high probability; meanwhile, any state that has low fidelity with  $|G\rangle$  should fail some test with high probability. When

$a_{j} \geq \theta$ , the probability that  $\rho$  can pass the stabilizer test associated with  $K_{j}$  can be upper bounded as follows:

$$
\begin{array}{l} \Pr \left(f _ {j} \geq \frac {1}{2} + \frac {1 - \theta}{2 ^ {r _ {j} + 1}}\right) = \Pr \left(f _ {j} \geq p _ {j} + \frac {a _ {j} - \theta}{2 ^ {r _ {j} + 1}}\right) \\ \leq \exp \left(- 2 \frac {\left(a _ {j} - \theta\right) ^ {2}}{4 ^ {r _ {j} + 1}} N _ {j}\right), \tag {C15} \\ \end{array}
$$

where the last step follows from the Hoeffding inequality. Similarly, the probability that the target state  $|G\rangle$  passes the test can be lower bounded by virtue of the Hoeffding inequality.

MTH did not give an explicit number of tests needed to verify a hypergraph state within infidelity  $\epsilon$  and significance level  $\delta$ . They considered a related, but different verification problem with a different criterion, which requires about  $nk + m$  tests, where  $k = 2^{2r + 3}n^7$ ,  $m \geq (2\ln 2)n^7k^2$ , and  $r = \max_j r_j$ . In other words, the number of required tests satisfies

$$
\begin{array}{l} n k + m \geq n k + (2 \ln 2) n ^ {7} k ^ {2} \cong (2 \ln 2) n ^ {7} k ^ {2} \\ = (2 ^ {4 r + 7} \ln 2) n ^ {2 1}. \tag {C16} \\ \end{array}
$$

While this number is still polynomial in  $n$  if  $r$  does not increase with  $n$ , it grows rapidly with  $n$ . Actually, it is already astronomical when  $n = 5$  and  $r = 2$  (note that  $r = 8$  for generic Union Jack states on 2D lattices), while any useful MBQC would require more than five qubits. So the MTH protocol is hardly practical. In contrast, the number of tests required by our cover or coloring protocol satisfies

$$
N \leq \left\lceil \frac {\Delta (G) + 1}{\delta \epsilon} \right\rceil \leq \left\lceil \frac {2 r + 1}{\delta \epsilon} \right\rceil \tag {C17}
$$

according to Eq. (27). Note that  $\Delta(G) \leq 2r$  since  $G$  is an order-3 hypergraph state. The upper bound in Eq. (C17) is independent of  $n$ , which shows that our protocol is dramatically more efficient than the MTH protocol. According to Eqs. (36) and (37), the hedged cover or coloring protocol can further reduce the number of tests to

$$
N \leq \frac {\left[ \Delta (G) + \mathrm {e} \right] \ln (F \delta) ^ {- 1}}{\epsilon} \leq \frac {(2 r + \mathrm {e}) \ln (F \delta) ^ {- 1}}{\epsilon}. \tag {C18}
$$

It is natural to ask whether the number of tests can be reduced significantly if the MTH protocol is adapted to the nonadversarial scenario considered in the main text. Here we try to give a rough estimate.

To verify  $|G\rangle$  within infidelity  $\epsilon$  and significance level  $\delta$ , suppose  $1 - \langle G|\rho |G\rangle \geq \epsilon$ , we need to estimate the maximal probability that  $\rho$  can pass all the stabilizer tests and

make sure that this probability is smaller than  $\delta$ , that is,

$$
\prod_ {j} \Pr \left(f _ {j} \geq \frac {1}{2} + \frac {1 - \theta}{2 ^ {r _ {j} + 1}}\right) = \Pr \left(f _ {j} \geq p _ {j} + \frac {a _ {j} - \theta}{2 ^ {r _ {j} + 1}}\right) \leq \delta . \tag {C19}
$$

According to Eq. (C15), it suffices to guarantee that

$$
\prod_ {j \mid a _ {j} \geq \theta} \exp \left(- 2 \frac {\left(a _ {j} - \theta\right) ^ {2}}{4 ^ {r _ {j} + 1}} N _ {j}\right) \leq \delta . \tag {C20}
$$

Note that the infidelity of  $\rho$  with  $|G\rangle$  satisfies

$$
\begin{array}{l} 1 - \langle G | \rho | G \rangle = 1 - \operatorname {t r} \left(\rho \prod_ {j} \frac {K _ {j} + 1}{2}\right) \\ \leq \sum_ {j} \left[ 1 - \operatorname {t r} \left(\rho \frac {K _ {j} + 1}{2}\right) \right] = \frac {1}{2} \sum_ {j} a _ {j}. \tag {C21} \\ \end{array}
$$

The upper bound can be saturated when  $0 \leq \sum_{j} a_{j} \leq 2$ . To see this, for each  $k = 1, 2, \ldots, n$ , let  $|G_{k}\rangle$  be the common eigenstate of  $K_{j}$  for  $j = 1, 2, \ldots, n$  with eigenvalues

$$
K _ {k} | G _ {k} \rangle = - 1, \quad K _ {j} | G _ {k} \rangle = 1, \quad \forall j \neq k. \tag {C22}
$$

Let

$$
\rho = \left(1 - \sum_ {j} \lambda_ {j}\right) | G \rangle \langle G | + \sum_ {j} \lambda_ {j} | G _ {j} \rangle \langle G _ {j} |, \tag {C23}
$$

where  $\lambda_{j} = a_{j} / 2$ . Then we have  $1 - \operatorname{tr}(\rho K_{j}) = 2\lambda_{j} = a_{j}$  and  $1 - \langle G|\rho |G\rangle = \sum_{j}\lambda_{j} = \sum_{j}a_{j} / 2$ , so the bound in Eq. (C21) is saturated.

According to Eq. (C21),  $\sum_{j}a_{j}\geq 2\epsilon$  if the infidelity of  $\rho$  is at least  $\epsilon$ , that is,  $1 - \langle G|\rho |G\geq \epsilon$ . Now we can derive a lower bound for  $\sum_{j}N_{j}$  under the requirement that Eq. (C20) holds whenever  $\sum_{j}a_{j}\geq 2\epsilon$ . To this end, choose

$$
a _ {j} = \frac {2 \epsilon \times 2 ^ {r _ {j}}}{\sum_ {k} 2 ^ {r _ {k}}}, \tag {C24}
$$

then we have  $\sum_{j}a_{j} = 2\epsilon$  . So Eq. (C20) implies that

$$
\exp \left(- \frac {2 \epsilon^ {2} \sum_ {j} N _ {j}}{\left(\sum_ {j} 2 ^ {r _ {j}}\right) ^ {2}}\right) \leq \delta , \tag {C25}
$$

which in turn implies that

$$
N _ {\mathrm {M T H}} = \sum_ {j} N _ {j} \geq \frac {\left(\sum_ {j} 2 ^ {r _ {j}}\right) ^ {2} \ln \delta^ {- 1}}{2 \epsilon^ {2}}. \tag {C26}
$$

If all  $r_j$  are equal to  $r$ , then the MTH protocol requires  $4^r n$  potential measurement settings and at least

$$
N _ {\mathrm {M T H}} \geq \frac {4 ^ {r} n ^ {2} \ln \delta^ {- 1}}{2 \epsilon^ {2}} \tag {C27}
$$

tests. The bounds in the above two equations have much better scaling behavior with  $n$  compared with the bound in Eq. (C16). However, these bounds are already very large for a small value of  $n$  for Union Jack states and many other hypergraph states for which  $r$  is not so small. In general, it is too prohibitive to implement the MTH protocol except for hypergraph states of no more than ten qubits.

A few comments are in order. First, we do not know how tight the bounds in Eqs. (C26) and (C27) are. Nevertheless, these bounds are sufficient for comparing the MTH protocol with our protocol, and it is not so important to derive a tighter bound using more involved analysis. Second, Eq. (C26) is based on Eqs. (C15) and (C21). Note that the bound in Eq. (C21) is tight. The Hoeffding inequality in Eq. (C15) may potentially be improved, thereby reducing  $N_{\mathrm{MTH}}$ . However, this possibility was not considered by MTH. We are not aware of any simple method for improving the Hoeffding inequality either and do not expect a significant improvement even with more sophisticated analysis. In this regard, our protocol is not only much more efficient, but also much easier to implement and to analyze its performance.

In the rest of this section, we consider the performance of the MTH protocol adapted to the nonadversarial scenario for several concrete order-3 hypergraph states. As a start, consider the complete order-3 hypergraph state whose underlying hypergraph contains all possible order-3 hyperedges. In this case, the total number of hyperedges is  $\binom{n}{3} = n(n - 1)(n - 2) / 6$  and  $r_j = r = \binom{n-1}{2} = (n - 1)(n - 2) / 2$  for  $j = 1, 2, \ldots, n$ . Therefore,

$$
N _ {\mathrm {M T H}} \geq \frac {2 ^ {(n - 1) (n - 2)} n ^ {2} \ln \delta^ {- 1}}{2 \epsilon^ {2}}. \tag {C28}
$$

Here both the number of potential measurement settings and the number of tests required by the MTH protocol increase exponentially with the number of qubits. By contrast, our cover protocol requires at most  $n$  potential measurement settings and  $\lceil (n / \epsilon)\ln (1 / \delta)\rceil$  tests according to Eq. (22).

The examples considered in the rest of this section are three colorable, so our cover protocol requires three measurement settings and  $\lceil (3 / \epsilon)\ln (1 / \delta)\rceil$  tests to verify each hypergraph state within infidelity  $\epsilon$  and significance level  $\delta$ . First, consider the tensor power  $|\Psi_{f_3}\rangle^{\otimes n / 3}$  introduced in Appendix C2, assuming that  $n$  is divisible by 3. In this case  $r_j = r = 1$  for all  $j = 1,2,\ldots ,n$ . So Eq. (C27) reduces to

$$
N _ {\mathrm {M T H}} \geq \frac {2 n ^ {2} \ln \delta^ {- 1}}{\epsilon^ {2}}. \tag {C29}
$$

Next, consider order-3 cluster states. In the 1D case, the vertices of the underlying hypergraph are arranged in a chain and labeled by natural numbers; all hyperedges have the form  $\{j,j + 1,j + 2\}$  with  $j\geq 1$  and  $j\leq n - 2$  assuming  $n\geq 3$ . If we use 0,1,2 to denote three colors, then the hypergraph can be colored by assigning vertex  $j$  with the color  $(j\bmod 3)$ . Similar analysis applies to 2D and higher-dimensional lattices. For simplicity, here we focus on the 1D case, which yields

$$
r _ {j} = \left\{ \begin{array}{l l} 1 & n = 3 \text {o r} j = 1 \text {o r} j = n, \\ 2 & n \geq 4, j = 2 \text {o r} j = n - 1, \\ 3 & j \neq 1, 2, n - 1, n. \end{array} \right. \tag {C30}
$$

Therefore,

$$
\sum_ {j} 2 ^ {r _ {j}} = \left\{ \begin{array}{l l} 6 & n = 3, \\ 8 n - 2 0 & n \geq 4, \end{array} \right. \tag {C31}
$$

which implies that

$$
N _ {\mathrm {M T H}} \geq \left\{ \begin{array}{l l} \frac {1 8 \ln \delta^ {- 1}}{\epsilon^ {2}} & n = 3, \\ \frac {8 (2 n - 5) ^ {2} \ln \delta^ {- 1}}{\epsilon^ {2}} & n \geq 4. \end{array} \right. \tag {C32}
$$

Next, consider the Union Jack state on the Union Jack chain; cf. Fig. 1 in the main text. In this case, we have  $r_j = 2$  when  $j$  corresponds to one of the four corners and  $r_j = 4$  otherwise. Therefore,

$$
\sum_ {j} 2 ^ {r _ {j}} = 1 6 n - 4 8, \quad N _ {\mathrm {M T H}} \geq \frac {1 2 8 (n - 3) ^ {2} \ln \delta^ {- 1}}{\epsilon^ {2}}. \tag {C33}
$$

Finally, consider the Union Jack state on the Union Jack lattice with  $\tilde{n} \times \tilde{n}$  cells and  $n = \tilde{n}^2 + (\tilde{n} + 1)^2$  qubits. Calculation shows that

$$
\begin{array}{l} \sum_ {j} 2 ^ {r _ {j}} = 2 ^ {8} (\tilde {n} - 1) ^ {2} + 2 ^ {4} [ \tilde {n} ^ {2} + 4 (\tilde {n} - 1) ] + 2 ^ {2} \times 4 \\ = 1 6 \left(1 7 \tilde {n} ^ {2} - 2 8 \tilde {n} + 1 3\right), \tag {C34} \\ \end{array}
$$

which implies that

$$
N _ {\mathrm {M T H}} \geq \frac {1 2 8 (1 7 \tilde {n} ^ {2} - 2 8 \tilde {n} + 1 3) ^ {2} \ln \delta^ {- 1}}{\epsilon^ {2}}. \tag {C35}
$$

# 4. Comparison with Ref. [9]

Here, in the adversarial setting, we compare our method with the method proposed by Hayashi and Hajdušek (HH) [9], who considered the verification of graph states, but

not hypergraph states. In addition, HH mainly focused on the case in which the graph is three colorable. They mentioned the general case briefly, but did not analyze the performance of their protocol in detail. Since the main focus of Ref. [9] is self-testing, HH do not trust their measurement devices. However, after the verification of their measurement devices, they verify their graph state under the assumption that their measurement devices are trusty.

Suppose  $|G\rangle$  is a graph state associated with the graph  $G$ . When  $G$  is  $m$  colorable, HH (Appendix F of Ref. [9]) proposed the following verification protocol, which consists of  $m$  stabilizer tests. Given a coloring  $\mathcal{A} = \{A_1,A_2,\dots ,A_m\}$  of  $G$  with  $m$  colors, the verifier asks the adversary to prepare  $N + 1$  systems with  $N = mN^{\prime}$ . After a random permutation of the  $N + 1$  systems,  $N$  systems are chosen and divided into  $m$  groups each with  $N^{\prime}$  systems. Then all systems in the  $l$ th group for  $l = 1,2,\ldots ,m$  are subjected to the stabilizer test with  $P_{l}$  [cf. Eq. (12) in the main text] as the projector onto the pass eigenspace. Let  $\sigma$  be the reduced state of the remaining system after all these tests are passed. If the  $l$ th test  $P_{l}$  is passed with significance level  $\delta^{\prime}$ , then one can guarantee that  $\mathrm{tr}[\sigma (1 - P_l)]\leq 1 / \delta '(N' + 1)$ . If all the tests  $P_{1},\ldots ,P_{m}$  are passed, with significance level  $\delta \coloneqq m\delta^{\prime}$ , then one can guarantee that

$$
\begin{array}{l} \epsilon = \operatorname {t r} [ \sigma (1 - | G \rangle \langle G |) ] \leq \sum_ {l = 1} ^ {m} \operatorname {t r} [ \sigma (1 - P _ {l}) ] \\ \leq \sum_ {l = 1} ^ {m} \frac {1}{\delta^ {\prime} \left(N ^ {\prime} + 1\right)} = \frac {m ^ {2}}{\delta (N / m + 1)} \cong \frac {m ^ {3}}{\delta N}. \tag {C36} \\ \end{array}
$$

To verify  $|G\rangle$  within infidelity  $\epsilon$  and significance level  $\delta$  in the adversarial scenario, the HH protocol requires about  $\lceil m^3 /(\delta \epsilon)\rceil$  tests.

Now, we explain how our protocols outperform the HH protocol. If we employ the coloring protocol and randomly choose the  $l$ th measurement setting with probability  $1 / m$ , then the verification operator has spectral gap  $\nu(\Omega) = 1 / m$  according to Theorem 1. If  $N$  tests are passed with significance level  $\delta$ , then we can guarantee that

$$
\epsilon = \operatorname {t r} [ \sigma (1 - | G \rangle \langle G |) ] \leq \frac {m (1 - \delta)}{N \delta} \tag {C37}
$$

according to Refs. [38,39]. So the coloring protocol requires only  $\lceil m(1 - \delta) / (\delta \epsilon) \rceil$  tests to verify  $|G\rangle$  within infidelity  $\epsilon$  and significance level  $\delta$  in the adversarial scenario; cf. Eq. (26) in the main text. This is much more efficient than the HH protocol. Thanks to Eq. (36), the hedged coloring protocol can further reduce the number of tests and achieve the optimal scaling behavior with  $\delta$ . When  $m = 3$  and  $\epsilon = \delta = 0.01$  for example, the HH protocol in Ref. [9] requires 270000 tests, while the hedged coloring protocol requires only 1870 tests, which is smaller by 144 times.

# 5. Comparison with Ref. [35]

Recently, Takeuchi and Morimae [35] introduced a protocol for verifying general hypergraph states whose orders are upper bounded by a constant. Recall that the order of a hypergraph  $G = (V,E)$  is the maximum cardinality of hyperedges in the hyperedge set  $E$ .

Let  $G = (V, E)$  be a hypergraph such that  $2 \leq |e| \leq c$  for all  $e \in E$ , where  $c$  is a positive constant. Let  $k \geq (4n)^7$  and  $m \geq (2\ln 2)n^3 k^{18/7}$  be positive integers. According to Theorem 5 in Ref. [35], to verify the hypergraph state  $|G\rangle$  within infidelity  $\epsilon = k^{-1/7}$  and significance level  $\delta = k^{-1/7}$ , the number of tests required by the TM protocol is given by

$$
\begin{array}{l} N _ {\mathrm {T M}} = m + n k \geq (2 \ln 2) n ^ {3} k ^ {1 8 / 7} + n k > (2 \ln 2) n ^ {3} k ^ {1 8 / 7} \\ = (2 \ln 2) n ^ {3} \epsilon^ {- 1 8}. \tag {C38} \\ \end{array}
$$

Note that the conditions  $k \geq (4n)^{7}$  and  $\epsilon = k^{-1/7}$  imply the inequality  $4n\epsilon \leq 1$ . For example, when  $k = (4n)^{7}$  and  $\epsilon = \delta = k^{-1/7} = 1/(4n)$ , the number of required tests satisfies

$$
\begin{array}{l} N _ {\mathrm {T M}} \geq (2 \ln 2) n ^ {3} (4 n) ^ {1 8} + n (4 n) ^ {7} = (2 ^ {3 7} \ln 2) n ^ {2 1} + 2 ^ {1 4} n ^ {8} \\ > (2 ^ {3 7} \ln 2) n ^ {2 1} > 9. 5 \times 1 0 ^ {1 0} n ^ {2 1}. \tag {C39} \\ \end{array}
$$

Although this number is still polynomial in  $n$ , it is already astronomical in the simplest nontrivial scenario with  $n = 3$ . So it is too prohibitive to apply the TM protocol in any scenario of practical interest. By contrast, the number of tests required by our coloring protocol satisfies

$$
N \leq (1 6 n ^ {2} - 4 n) \chi (G) <   1 6 n ^ {2} \chi (G) \leq 1 6 n ^ {3} \tag {C40}
$$

according to Eq. (27) in the main text, which is dramatically smaller than  $N_{\mathrm{TM}}$ . The hedged coloring protocol can further reduce the number of tests according to Eqs. (36) and (37).

Our protocols are not only much more efficient than the TM protocol, but also much simpler to apply. In particular, the TM protocol relies on adaptive stabilizer tests, while our protocols do not rely on any adaption. In addition, the data processing in the TM protocol is a bit involved, while it is very simple in our protocols. Furthermore, TM did not derive the explicit number of required tests except for restricted choices of the infidelity  $\epsilon$  and significance level  $\delta$ , which makes it difficult to apply their result in many scenarios of practical interest. By contrast, we derive the explicit number of required tests for all valid choices of  $\epsilon$  and  $\delta$ .

# 6. Comparison with Ref. [31]

Recall that graph states are special hypergraph states in which all edges have order 2. It is known that all stabilizer states are equivalent to graph states under local

Clifford transformations [36,37]. Due to their simple structures, stabilizer states can be verified efficiently using Pauli measurements [31,34]. The protocol proposed by Pallister, Linden, and Montanaro (PLM) [31] is particularly efficient with respect to the total number of tests. To be specific, the PLM protocol measures all  $2^{n} - 1$  nontrivial stabilizer operators of  $|G\rangle$  in the Pauli group with equal probability. The resulting verification operator has the form

$$
\Omega_ {\mathrm {P L M}} = | G \rangle \langle G | + \frac {2 ^ {n - 1} - 1}{2 ^ {n} - 1} (1 - | G \rangle \langle G |), \tag {C41}
$$

with

$$
\beta \left(\Omega_ {\mathrm {P L M}}\right) = \frac {2 ^ {n - 1} - 1}{2 ^ {n} - 1}, \quad v \left(\Omega_ {\mathrm {P L M}}\right) = \frac {2 ^ {n - 1}}{2 ^ {n} - 1}. \tag {C42}
$$

To verify  $|G\rangle$  within infidelity  $\epsilon$  and significance level  $\delta$ , this protocol requires about

$$
\lceil 2 ^ {1 - n} (2 ^ {n} - 1) \epsilon^ {- 1} \ln \delta^ {- 1} \rceil \leq \lceil 2 \epsilon^ {- 1} \ln \delta^ {- 1} \rceil \tag {C43}
$$

tests, which is smaller than the number  $\lceil \chi (G)\epsilon^{-1}\ln \delta^{-1}\rceil$  required by our coloring protocol [cf. Eq. (22)]. However, the number of potential measurement settings required by the PLM protocol increases exponentially with the number  $n$  of qubits. When  $n$  is large, this protocol will be impractical if it is costly or time consuming to switch measurement settings. By contrast, our coloring protocol requires at most  $n$  potential measurement settings. In addition, when the chromatic number  $\chi (G)$  of  $G$  is small (in particular, when  $G$  is two colorable), the total number of tests required is comparable to the PLM protocol. Furthermore, the PLM protocol requires  $Y = \mathrm{i}XZ$  measurement because it is necessary to measure all nontrivial stabilizer operators of  $|G\rangle$ , while our protocol requires only  $X$  and  $Z$  measurements.

Incidentally, Ref. [31] introduced another protocol for verifying the graph state  $|G\rangle$  by measuring  $n$  stabilizer generators of  $|G\rangle$  with equal probability. The resulting verification operator  $\Omega$  has spectral gap  $\nu(\Omega) = 1/n$ . This protocol requires  $\lceil n\epsilon^{-1}\ln \delta^{-1} \rceil$  tests in total, which corresponds to the performance of our coloring protocol in the worst case in which the graph is complete (contains all possible edges). In general, the coloring protocol requires much fewer measurement settings and tests in total.

# 7. Comparison with Ref. [32]

Very recently, Takeuchi, Mantri, Morimae, Mizutani, and Fitzsimons (TMMMF) introduced a protocol for verifying graph states with a very small significance level [32]. Given a graph state  $|G\rangle$  of  $n$  qubits, by performing  $N_{\mathrm{TMMMF}} = 2n\lceil (5n^4\ln n) / 32\rceil$  tests, the protocol proposed

in Ref. [32] guarantees that the resultant state  $\sigma$  satisfies

$$
\langle G | \sigma | G \rangle \geq 1 - \frac {2 \sqrt {c} + 1}{n} \tag {C44}
$$

if these tests are passed with significance level  $n^{1 - 5c / 64}$ . Here,  $c$  is a constant that satisfies  $\frac{64}{5} < c < (n - 1)^2 / 4$ .

Next, we consider the performance of the hedged coloring protocol proposed in the main text. Suppose the graph  $G$  is  $m$  colorable and we apply a hedged coloring protocol with  $m$  colors. By Eq. (36), to verify  $|G\rangle$  within infidelity  $\epsilon = (2\sqrt{c} +1) / n$  and significance level  $\delta = n^{1 - 5c / 64}$ , the number of required tests reads

$$
\begin{array}{l} N = \left\lfloor \frac {h _ {*} (1 / m) \ln (F \delta) ^ {- 1}}{\epsilon} \right\rfloor \leq \frac {(m + \mathrm {e} - 1) \ln (F \delta) ^ {- 1}}{\epsilon}, \\ \approx \frac {(m + e - 1) (\frac {5 c}{6 4} - 1) n \ln n}{2 \sqrt {c} + 1} \leq O (n ^ {2} \ln n), \tag {C45} \\ \end{array}
$$

where  $F = 1 - \epsilon$  and the approximation holds as long as  $\epsilon, \delta \ll 1$ . For most graph states of practical interest, the chromatic numbers are upper bounded by a small constant, so  $N = O(n\ln n)$  tests are sufficient. This number is much smaller than  $N_{\mathrm{TMMMF}}$ . Therefore, our hedged coloring protocol is much more efficient than the protocol presented in Ref. [32].

[1] R. Horodecki, P. Horodecki, M. Horodecki, and K. Horodecki, Quantum entanglement, Rev. Mod. Phys. 81, 865 (2009).  
[2] O. Gühne and G. Tóth, Entanglement detection, Phys. Rep. 474, 1 (2009).  
[3] R. Raussendorf and H. J. Briegel, A One-way Quantum Computer, Phys. Rev. Lett. 86, 5188 (2001).  
[4] R. Raussendorf, D. E. Browne, and H. J. Briegel, Measurement-based quantum computation on cluster states, Phys. Rev. A 68, 022312 (2003).  
[5] A. Broadbent, J. Fitzsimons, and E. Kashefi, in Proceedings of the 50th Annual IEEE Symposium on Foundations of Computer Science (IEEE Computer Society, Washington, DC, 2009), p. 517.  
[6] T. Morimae and K. Fujii, Blind quantum computation protocol in which Alice only makes measurements, Phys. Rev. A 87, 050301 (2013).  
[7] M. Hayashi and T. Morimae, Verifiable Measurement-only Blind Quantum Computing with Stabilizer Testing, Phys. Rev. Lett. 115, 220502(R) (2015).  
[8] K. Fujii and M. Hayashi, Verifiable fault tolerance in measurement-based quantum computation, Phys. Rev. A 96, 030301 (2017).  
[9] M. Hayashi and M. Hajdušek, Self-guaranteed measurement-based quantum computation, Phys. Rev. A 97, 052308(R) (2018).  
[10] D. Gottesman, Ph.D. thesis, California Institute of Technology, 1997. Available at http://arxiv.org/abs/quant-ph/9705052.

[11] D. Schlingemann and R. F. Werner, Quantum error-correcting codes associated with graphs, Phys. Rev. A 65, 012308 (2001).  
[12] S. Perseguers, G. J. Lapeyre Jr., D. Cavalcanti, M. Lewenstein, and A. Acin, Distribution of entanglement in large-scale quantum networks, Rep. Prog. Phys. 76, 096001 (2013).  
[13] W. McCutcheon, A. Pappa, B. A. Bell, A. McMillan, A. Chailloux, T. Lawson, M. Mafu, D. Markham, E. Diamanti, I. Kerenidis, J. G. Rarity, and M. S. Tame, Experimental verification of multipartite entanglement in quantum networks, Nat. Commun. 7, 13251 (2016).  
[14] D. Markham and A. Krause, A simple protocol for certifying graph states and applications in quantum networks, (2018), arXiv:1801.05057.  
[15] D. M. Greenberger, M. A. Horne, A. Shimony, and A. Zeilinger, Bell's theorem with out inequalities, Am. J. Phys. 58, 1131 (1990).  
[16] V. Scarani, A. Acin, E. Schenck, and M. Aspelmeyer, Nonlocality of cluster states of qubits, Phys. Rev. A 71, 042325 (2005).  
[17] O. Gühne, G. Toth, P. Hyllus, and H. J. Briegel, Bell Inequalities for Graph States, Phys. Rev. Lett. 95, 120405 (2005).  
[18] C. Kruszynska and B. Kraus, Local entanglability and multipartite entanglement, Phys. Rev. A 79, 052304 (2009).  
[19] R. Qu, J. Wang, Z.-s. Li, and Y.-r. Bao, Encoding hypergraphs into quantum states, Phys. Rev. A 87, 022311 (2013).  
[20] M. Rossi, M. Huber, D. Bruß, and C. Macchiavello, Quantum hypergraph states, New J. Phys. 15, 113022 (2013).  
[21] F. E. S. Steinhoff, C. Ritz, N. I. Miklin, and O. Gühne, Qudit hypergraph states, Phys. Rev. A 95, 052340 (2017).  
[22] F.-L. Xiong, Y.-Z. Zhen, W.-F. Cao, K. Chen, and Z.-B. Chen, Qudit hypergraph states and their properties, Phys. Rev. A 97, 012323 (2018).  
[23] J. Miller and A. Miyake, Hierarchy of universal entanglement in 2D measurement-based quantum computation, npj Quantum Inf. 2, 16036 (2016).  
[24] J. Miller and A. Miyake, Latent Computational Complexity of Symmetry-protected Topological Order with Fractional Symmetry, Phys. Rev. Lett. 120, 170503 (2018).  
[25] T. Morimae, Y. Takeuchi, and M. Hayashi, Verification of hypergraph states, Phys. Rev. A 96, 062321 (2017).  
[26] M. Gachechiladze, C. Budroni, and O. Gühne, Extreme Violation of Local Realism in Quantum Hypergraph States, Phys. Rev. Lett. 116, 070401 (2016).  
[27] M. Gachechiladze, O. Gühne, and A. Miyake, Changing the circuit-depth complexity of measurement-based quantum computation with hypergraph states, Phys. Rev. A 99, 052304 (2019).  
[28] B. Yoshida, Topological phases with generalized global symmetries, Phys. Rev. B 93, 155131 (2016).  
[29] Y. Takeuchi, T. Morimae, and M. Hayashi, Quantum computational universality of hypergraph states with Pauli-X and Z basis measurements, Sci. Rep. 9, 13585 (2019).  
[30] M. J. Bremner, A. Montanaro, and D. J. Shepherd, Average-case Complexity versus Approximate Simulation of Commuting Quantum Computations, Phys. Rev. Lett. 117, 080501 (2016).

[31] S. Pallister, N. Linden, and A. Montanaro, Optimal Verification of Entangled States with Local Measurements, Phys. Rev. Lett. 120, 170502 (2018).  
[32] Y. Takeuchi, A. Mantri, T. Morimae, A. Mizutani, and J. F. Fitzsimons, Resource-efficient verification of quantum computing using Serfling's bound, npj Quantum Inf. 5, 27 (2019).  
[33] D. Gross, Y.-K. Liu, S. T. Flammia, S. Becker, and J. Eisert, Quantum State Tomography via Compressed Sensing, Phys. Rev. Lett. 105, 150401 (2010).  
[34] S. T. Flammia and Y.-K. Liu, Direct Fidelity Estimation from few Pauli Measurements, Phys. Rev. Lett. 106, 230501 (2011).  
[35] Y. Takeuchi and T. Morimae, Verification of Many-qubit States, Phys. Rev. X 8, 021060 (2018).  
[36] D. Schlingemann, Stabilizer codes can be realized as graph codes, Quantum Info. Comput. 2, 307 (2002).  
[37] M. Grassl, A. Klappenecker, and M. Rötteler, in Proceedings of the 2002 IEEE International Symposium on Information Theory (IEEE Information Theory Society, Lausanne, Switzerland, 2002). Available at arXiv:quant-ph/0703112.  
[38] H. Zhu and M. Hayashi, General framework for verifying pure quantum states in the adversarial scenario, Phys. Rev. A (2019).  
[39] H. Zhu and M. Hayashi, Efficient verification of pure quantum states in the adversarial scenario, Phys. Rev. Lett. (2019).

[40] A. J. W. Hilton, R. Rado, and S. H. Scott, A (< 5)-colour theorem for planar graphs, Bull. London Math. Soc. 5, 302 (1973).  
[41] E. R. Scheinerman and D. H. Ullman, *Fractional Graph Theory: A Rational Approach to the Theory of Graphs* (Wiley, New York, 1997).  
[42] K. Chen and H.-K. Lo, Multi-partite quantum cryptographic protocols with noisy GHZ states, Quantum Info. Comput. 7, 689 (2007).  
[43] D. Brélaz, New methods to color the vertices of a graph, Commun. ACM 22, 251 (1979).  
[44] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, UK, 2000).  
[45] M. Ghio, D. Malpetti, M. Rossi, D. Bruß, and C. Macchiavello, Multipartite entanglement detection for hypergraph states, J. Phys. A: Math. Theor. 51, 045302 (2018).  
[46] G. Toth and O. Gühne, Detecting Genuine Multipartite Entanglement with two Local Measurements, Phys. Rev. Lett. 94, 060501 (2005).  
[47] G. Tóth and O. Gühne, Entanglement detection in the stabilizer formalism, Phys. Rev. A 72, 022340 (2005).  
[48] A. Dimić and B. Dakić, Single-copy entanglement detection, npj Quantum Inf. 4, 11 (2018).  
[49] D. W. Lyons, D. J. Upchurch, S. N. Walck, and C. D. Yetter, Local unitary symmetries of hypergraph states, J. Phys. A: Math. Theor. 48, 095301 (2015).