# Building Gaussian cluster states by linear optics

Peter van Loock, $^{1,*}$  Christian Weedbrook, $^{2}$  and Mile Gu $^{2}$

$^{1}$ National Institute of Informatics, 2-1-2 Hitotsubashi, Chiyoda-ku, Tokyo 101-8430, Japan

$^{2}$ Department of Physics, The University of Queensland, Brisbane, Queensland 4072, Australia

(Received 23 October 2006; revised manuscript received 22 June 2007; published 21 September 2007)

The linear optical creation of Gaussian cluster states, a potential resource for universal quantum computation, is investigated. First, using Bloch-Messiah reduction, we show how to achieve canonical cluster-state generation, otherwise based on pairwise acting quantum nondemolition gates, by off-line squeezers and beam splitters. Moreover, we find that, in terms of squeezing resources, the canonical states are rather wasteful. Hence we propose a systematic way to create a whole family of cluster-type states, including potentially cheaper states. Any given cluster (or graph) state can be realized this way. As an example, we consider a protocol in which a single-mode quantum state propagates through a multiple-rail cluster. Such a redundant encoding may reduce errors due to finite squeezing.

DOI: 10.1103/PhysRevA.76.032321

PACS number(s): 03.67.Lx, 42.50.Dv, 42.25.Hz

# I. INTRODUCTION

The cluster-state model for quantum computation [1] is a conceptually interesting alternative to the more conventional circuit model [2]. Once a suitable multiparty entangled cluster state has been prepared, universal quantum gates can be effected through the cluster via only single-party projective measurements and feedforward. Though originally based upon qubits, the cluster-state model can be also applied to other discrete-variable systems (quids) [3-5] as well as to continuous quantum variables [6].

Linear optics represents one of the most practical approaches to the realization of quantum information protocols, both for discrete-variable (DV) [7] and continuous-variable (CV) implementations [8]. In the DV case, efficient entangling gates cannot be achieved with single photons and linear optics. Nonetheless, probabilistic gates can be applied offline to an entangled multiphoton state that eventually serves as a resource for the online computation [9]. A similar approach uses DV photonic cluster states, leading to a significant reduction in the resource consumption [10,11]. However, the generation of the optical cluster states remains highly probabilistic in this case.

Although up to six-qubit single-photon cluster states have been created via postselection using nonlinear and linear optics [12,13], a possible deterministic, unconditional realization of optical cluster states would be based on continuous variables. Here, the resources are squeezed states of light and the Gaussian cluster states may be created via quadratic quantum nondemolition (QND) interactions [14]. These interactions, however, cannot be realized through beam splitters alone. Additional "online" squeezers are needed for every single link of the cluster state, again rendering the mechanism for cluster generation rather inefficient with current technology. Moreover, the squeezing of the resource states will always be finite, inevitably resulting in errors in the cluster computation. In this paper, we will address both

issues: the avoidance of online squeezing in cluster-state generation and the reduction of finite-squeezing-induced errors in cluster-state computation.

When Gaussian cluster states are to be used for universal quantum computation, continuous-variable homodyne measurements will not be sufficient. Universality in this case requires a nonlinear element, corresponding to an at least cubic interaction in terms of the optical mode operators [15]. In Gaussian cluster-state computation, this nonlinear element can be absorbed into the measurement apparatus in the form of a single non-Gaussian projective measurement [6], for instance, photon number detection. The cluster state itself remains Gaussian, thus representing a potential resource for universal quantum computation. The aim of this work is to propose practical and economical ways to create an arbitrary Gaussian cluster state (or, more generally, an arbitrary Gaussian graph state). Only off-line squeezed resource states, but no additional online squeezing transformations shall be used. Moreover, a certain degree of cluster-type quantum correlations should be obtained from as little offline squeezing as possible.

First, using Bloch-Messiah reduction [16], we will show how to generate a canonical cluster state, as originally defined through QND-type entangling interactions [6,14], by off-line squeezers and beam splitters. As a second step, we consider a whole family of Gaussian cluster-type states, defined via cluster-type quadrature correlations in the infinite-squeezing limit; this family includes the original, canonical cluster states as a special case. We then propose a systematic way on how to build alternative cluster-type states from potentially cheaper squeezing resources (with, on average, lower squeezing levels) than needed for the canonical states.

In the resulting linear-optics schemes, the resource states require correspondingly more squeezing to compensate for the lack of extra squeezing in the beam-splitter network that replaces the QND coupling of the cluster nodes. Nonetheless, the main feature of the canonical QND-made clusters, namely, cluster-type quadrature correlations, can still be achieved. As an example, we consider a cluster-based protocol in which a single-mode quantum state is teleported

through a "multiple-rail cluster" instead of the usual, linear, single-rail cluster. We show that via this multiple-rail encoding, the excess noise in one phase-space variable can be suppressed to an arbitrary extent, provided the redundant encoding is achieved using additional QND gates. However, as the QND gates are not freely available, every additional path of the multiple-rail cluster would require extra squeezing for the generation of the larger clusters. Therefore, we will also discuss a potential application of multiple-rail encoding to the cheaper, linear-optics-made cluster-type states.

The plan of the paper is as follows. First, in Sec. II, we define Gaussian cluster-type states in analogy to qubit cluster states. In Sec. III, we will derive a linear-optics generation scheme for the canonical Gaussian cluster states, as defined in terms of QND interactions. The scheme for canonical cluster-state generation is then extended to a more general linear-optics cluster-creation algorithm. This extension, described in Sec. IV, leads to a set of geometrical vector conditions sufficient for the linear-optics generation of cluster-type states. Finally, in Sec. V, we will discuss the example of a cluster-state protocol using multiple-rail clusters.

# II. CLUSTER-TYPE STATES

We define cluster-type (graph-type) states as those multi-mode Gaussian states for which certain quadrature correlations become perfect in the limit of infinite squeezing,

$$
\left(\hat {p} _ {a} - \sum_ {b \in N _ {a}} \hat {x} _ {b}\right)\rightarrow 0, \quad a \in G. \tag {1}
$$

More precisely, in this limit, the  $N$ -mode graph state becomes a simultaneous zero eigenstate of the  $N$  linear combinations in Eq. (1). Here we use the dimensionless "position" and "momentum" operators  $\hat{x}$  and  $\hat{p}$ , corresponding to the quadratures of an optical mode with annihilation operator  $\hat{a} = \hat{x} + i\hat{p}$ . The modes  $a \in G$  correspond to the vertices of the graph, while the modes  $b \in N_a$  are the nearest neighbors of mode  $a$ .

Perfect correlations uniquely define the corresponding graph state. This definition is analogous to the DV case, where, for qubits, a graph state may be defined via its stabilizer group [17]. For a given graph, the stabilizer group can be generated by a set of operators for which the graph state is a common eigenvector with eigenvalue equal to unity. For qubits, this set corresponds to  $\{\hat{\sigma}_x^{(a)}\Pi_{b\in N_a}\hat{\sigma}_z^{(b)}\}$ , with the usual Pauli operators  $\hat{\sigma}_x^{(a)}$  and  $\hat{\sigma}_z^{(a)}$  for every qubit node  $a$ .

In order to obtain an analogous set of operators for continuous variables, one can start with every optical mode, representing the vertices of the graph, in an infinitely squeezed zero-momentum eigenstate  $|p = 0\rangle$ . This initial state  $|p = 0\rangle^{\otimes N}$  is stabilized by the set  $\{\hat{X}_a(s_a)\}$ , with the Weyl-Heisenberg (WH) operator  $\hat{X}(s) \equiv e^{-2i\hat{s}\hat{p}}$ ,  $s \in \mathbf{R}$ , describing position displacements. Using the canonical generation of CV cluster states in terms of QND-type (continuous-variable  $C_Z$  [6]) gates,  $e^{2i\hat{x} \otimes \hat{x}}$ , pairwise acting upon the input modes  $|p = 0\rangle$ , the stabilizer group of the resulting graph is generated by the set  $\{\hat{X}_a(s_a)\Pi_{b \in N_a}\hat{Z}_b(s_a)\}$ , with the momentum displacement

ment WH operator  $\hat{Z}(t) \equiv e^{2it\hat{x}}$ ,  $t \in \mathbf{R}$ . This set can be rewritten as

$$
\hat {X} _ {a} \left(s _ {a}\right) \prod_ {b \in N _ {a}} \hat {Z} _ {b} \left(s _ {a}\right) = e ^ {- 2 i s _ {a} \hat {p} _ {a}} \prod_ {b \in N _ {a}} e ^ {2 i s _ {a} \hat {x} _ {b}} = e ^ {- 2 i s _ {a} \left(\hat {p} _ {a} - \Sigma_ {b \in N _ {a}} \hat {x} _ {b}\right)}. \tag {2}
$$

Now applying the stabilizer condition to a given graph state  $|G\rangle$ ,

$$
e ^ {- 2 i s _ {a} \left(\hat {p} _ {a} - \sum_ {b \in N _ {a}} \hat {x} _ {b}\right)} | G \rangle = | G \rangle \quad \forall s _ {a} \in \mathbf {R}, \forall a \in G, \tag {3}
$$

immediately leads to the definition in Eq. (1). This definition covers all Gaussian states which, in the infinite-squeezing limit, become zero eigenstates of all those quadrature combinations that generate the stabilizer group of the corresponding graph. Here, the zero eigenstates are the representatives for a given graph. More generally, one may define CV graph states as common eigenstates of the corresponding quadrature combinations. This definition means that the variance of the quadrature combinations vanishes in the limit of infinite squeezing,  $\mathrm{Var}(\hat{p}_a - \Sigma_{b\in N_a}\hat{x}_b)\to 0$ ,  $a\in G$ .

# III. CANONICAL CLUSTER STATES VIA LINEAR OPTICS

The canonical way to build CV cluster states would be to send a number of single-mode squeezed states through a corresponding network of QND gates [6,14]. Each individual QND gate could be realized via two beam splitters and a pair of online squeezers [16]. However, by including the initial single-mode squeezers into the QND network, the resulting total circuit corresponds to a big quadratic Hamiltonian applied to a number of vacuum modes. This total transformation can be decomposed into a linear-optics circuit followed by single-mode squeezers and a second linear-optics circuit [16], where the first linear-optics circuit has no effect on the vacuum modes. Eventually one has just one linear circuit applied to a number of single-mode squeezed states; in principle, this works for any cluster (or graph) state. Let us explain this in a little more detail.

The canonical generation of CV cluster states [14] from momentum-squeezed vacuum modes via QND-type interactions can be described by  $\hat{x}_a^\prime = \hat{x}_a$  and  $\hat{p}_a^\prime = \hat{p}_a + \Sigma_{b\in N_a}\hat{x}_b$ , where  $\hat{x}_a = e^{+r}\hat{x}_a^{(0)}$  and  $\hat{p}_a = e^{-r}\hat{p}_a^{(0)},\forall a\in G$ , with vacuum modes labeled by superscript (0). Note that, according to Eq. (1), the canonical cluster states become perfectly correlated for  $r\rightarrow \infty$ . Now we have the following linear Bogoliubov (LUBO) transformation:

$$
\begin{array}{l} \hat {a} _ {a} ^ {\prime} = \hat {x} _ {a} ^ {\prime} + i \hat {p} _ {a} ^ {\prime} = \hat {x} _ {a} + i \left(\hat {p} _ {a} + \sum_ {b \in N _ {a}} \hat {x} _ {b}\right) \\ = e ^ {+ r} \hat {x} _ {a} ^ {(0)} + i \left(e ^ {- r} \hat {p} _ {a} ^ {(0)} + \sum_ {b \in \mathcal {N} _ {a}} e ^ {+ r} \hat {x} _ {b} ^ {(0)}\right) \\ \stackrel {!} {=} \sum_ {l \in G} A _ {a l} \hat {a} _ {l} ^ {(0)} + B _ {a l} \hat {a} _ {l} ^ {(0) \dagger} \\ = \sum_ {l \in G} (A _ {a l} + B _ {a l}) \hat {x} _ {l} ^ {(0)} + i (A _ {a l} - B _ {a l}) \hat {p} _ {l} ^ {(0)}, \quad (4) \\ \end{array}
$$

using  $\hat{a}_l^{(0)} = \hat{x}_l^{(0)} + i\hat{p}_l^{(0)}$ . From this we can extract the LUBO

matrix elements for canonical cluster generation,

$$
A _ {a a} = \cosh r, \quad B _ {a a} = \sinh r,
$$

$$
A _ {a b} = B _ {a b} = (i / 2) e ^ {+ r}, \quad \forall b \in N _ {a},
$$

$$
A _ {a l} = B _ {a l} = 0, \quad \forall l \notin N _ {a} (l \neq a). \tag {5}
$$

Note that the input modes of this LUBO transformation are vacuum modes instead of the squeezed input modes of the QND network. This is crucial in order to eliminate the first linear-optics circuit in the decomposition of the LUBO transformation into beam splitters and squeezers, as we describe now.

Let us decompose the LUBO transformation of Eq. (5) into a linear-optics circuit  $V^{\dagger}$ , a set of single-mode squeezers, and another linear-optics circuit  $U$  [16]. This is achieved by exploiting that  $AA^{\dagger}$  and  $BB^{\dagger}$  are Hermitian and commute, and hence can be simultaneously diagonalized in the same basis described by a unitary matrix  $U$ . Similarly,  $(B^{\dagger}B)^T$  and  $A^{\dagger}A$  shall be simultaneously diagonalized through the unitary matrix  $V$ . In addition, using the singular value decomposition for  $A$  and  $B$ , we have to satisfy

$$
V = A ^ {\dagger} U A _ {D} ^ {- 1} = B ^ {T} U ^ {*} B _ {D} ^ {- 1}, \tag {6}
$$

$$
U = A V A _ {D} ^ {- 1} = B V ^ {*} B _ {D} ^ {- 1}, \tag {7}
$$

for the unitary matrices  $U$  and  $V$ . Here  $A_D^2$  is the diagonalized version of  $AA^\dagger$  and  $A^\dagger A$ ; similarly, we use  $B_D^2$  for  $BB^\dagger$  and  $(B^\dagger B)^T$ . Here, for example, Eq. (6) leads to the matrix elements

$$
\begin{array}{l} V _ {a l} = \left[ U _ {a l} \cosh r - (i / 2) e ^ {+ r} \sum_ {b \in N _ {a}} U _ {b l} \right] / \sqrt {\lambda_ {l} ^ {A}} \\ = \left[ U _ {a l} ^ {*} \sinh r + (i / 2) e ^ {+ r} \sum_ {b \in N _ {a}} U _ {b l} ^ {*} \right] / \sqrt {\lambda_ {l} ^ {B}}, \tag {8} \\ \end{array}
$$

where  $\sqrt{\lambda_l^A}$  are the singular values of  $A$  and similarly for  $B$ . The singular values will determine the strength of the single-mode squeezers. By rewriting Eq. (8) in terms of the real and imaginary parts of  $U_{al}$ , we obtain

$$
\operatorname {I m} U _ {a l} - C _ {l} (r) \sum_ {b \in N _ {a}} \operatorname {R e} U _ {b l} = 0, \quad \forall a, l \in G, \tag {9}
$$

with

$$
\operatorname {R e} U _ {a l} \left[ D _ {l} (r) - M _ {N _ {a}} \right] - \sum_ {b \in N _ {a}} \sum_ {k \in N _ {b}, k \neq a} \operatorname {R e} U _ {k l} = 0, \tag {10}
$$

where

$$
C _ {l} (r) \equiv \frac {\frac {e ^ {+ r}}{2} \left(\sqrt {\lambda_ {l} ^ {A}} + \sqrt {\lambda_ {l} ^ {B}}\right)}{\sqrt {\lambda_ {l} ^ {A}} \sinh r + \sqrt {\lambda_ {l} ^ {B}} \cosh r}, \tag {11}
$$

$D_{l}(r)\equiv (\lambda_{l}^{B}\cosh^{2}r - \lambda_{l}^{A}\sinh^{2}r) / [e^{+2r}(\lambda_{l}^{A} - \lambda_{l}^{B}) / 4],$  and  $\operatorname {Re}U_{al}\equiv \operatorname {Re}(U_{al})$  , etc.;  $M_{N_a}$  represents the number of nearest neighbors of mode  $a$  . The double sum in Eq. (10) sums over all second neighbors of mode  $a$  (including multiple counting of identical neighbors of the nearest neighbors of mode  $a$

![](images/3e8cdb04098677e1b2a8b9ddfa9cf13f5328288d5e7d57543d4cc5f7ef0b0cf8.jpg)  
a)

![](images/450e586da7bdf4d2564687b4400784317964923d35ede105bdf9aa3e68ab399f.jpg)  
c)  
d)

![](images/32ffc1c5d585195729e202d242b67c5d17a51e078ed1280b0fd601d4291a5691.jpg)  
b)

![](images/32f57e94213ee0955f13eb9d400a8f3cfc9af22119d65da51fcf7cdddc55b28c.jpg)  
FIG. 1. Different generation schemes for a canonical two-mode cluster state. The input modes are always vacuum modes: (a) canonical generation via QND interaction; (b) QND gate replaced by a beam splitter (BS), two on-line squeezers, and another beam splitter [16]; (c) generation of a standard two-mode squeezed state (via two squeezers and a beam splitter) plus two local squeezers [18]; (d) simplest generation scheme with the QND gate replaced by a beam splitter.

Equation (9) can be incorporated into the column vectors of  $U$ ,

$$
\vec {u} _ {l} \equiv \left( \begin{array}{c} \alpha_ {1 l} + i C _ {l} (r) \sum_ {b \in N _ {1}} \alpha_ {b l} \\ \alpha_ {2 l} + i C _ {l} (r) \sum_ {b \in N _ {2}} \alpha_ {b l} \\ \dots \\ \alpha_ {N l} + i C _ {l} (r) \sum_ {b \in N _ {N}} \alpha_ {b l} \end{array} \right), \tag {12}
$$

using  $\mathrm{Re}U_{kl}\equiv \alpha_{kl}$ , with the constraints of Eq. (10), and  $\Sigma_l(\vec{u}_l)_k(\vec{u}_l)_{k'}^* = \delta_{kk'}$  for unitarity. These conditions automatically satisfy  $A = UA_{D}V^{\dagger}$  and  $B = UB_{D}V^{T}$ , where the diagonal matrices  $A_{D}$  and  $B_{D}$  contain the corresponding singular values. Thus, we effectively constructed a linear-optics circuit  $U$  that exactly outputs the canonical cluster states when applied to the off-line squeezed input modes with squeezed quadratures

$$
\hat {x} _ {l} = (\sqrt {\lambda_ {l} ^ {A}} + \sqrt {\lambda_ {l} ^ {B}}) \hat {x} _ {l} ^ {(0)} \equiv e ^ {+ R _ {l}} \hat {x} _ {l} ^ {(0)},
$$

$$
\hat {p} _ {l} = \left(\sqrt {\lambda_ {l} ^ {A}} - \sqrt {\lambda_ {l} ^ {B}}\right) \hat {p} _ {l} ^ {(0)} \equiv e ^ {- R _ {l}} \hat {p} _ {l} ^ {(0)}. \tag {13}
$$

The vacuum modes  $\hat{a}_l^{(0)} = \hat{x}_l^{(0)} + i\hat{p}_l^{(0)}$  are "redefined" vacuum modes after the first linear-optics circuit  $V^{\dagger}$  that has no effect.

Let us consider the example of the canonical two-mode cluster state. It corresponds to two momentum-squeezed modes (squeezed by  $r$ ) coupled through a quadratic QND gate  $e^{2i\hat{x}\otimes \hat{x}}$  [see Fig. 1(a)]. In this case, we have  $\lambda_l^A \equiv \cosh^2 r + e^{+2r} / 4$ ,  $\lambda_l^B \equiv \sinh^2 r + e^{+2r} / 4$ ,  $C_1(r) = C_2(r) \equiv C^{-1}(r)$ , and  $D_l(r) \equiv 1$ . Thus, in the equivalent linear-optics scheme [Fig. 1(d)], two equally squeezed modes, corresponding to Eqs. (13) with  $l = 1,2$ , are combined at a beam splitter described by  $U$  with column vectors as in Eq. (12),  $l = 1,2$ ,  $N = 2$ ; the constraints in Eq. (10) are always satisfied.

A possible solution for  $U$ , choosing  $\alpha_{12} = \alpha_{21} = 0$ , is

$$
U = \frac {1}{\sqrt {1 + C ^ {2} (r)}} \left( \begin{array}{c c} C (r) & i \\ i & C (r) \end{array} \right). \tag {14}
$$

Each input mode is momentum squeezed with  $R_{l} = \ln (\sqrt{\lambda_{l}^{A}} +\sqrt{\lambda_{l}^{B}})\equiv R$ . For  $r = 0$ , we obtain  $\lambda_l^A\equiv 5 / 4$  and  $\lambda_l^B\equiv 1 / 4$ , and thus  $R = \ln [(1 + \sqrt{5}) / 2]$ . This is the residual squeezing coming from the QND gate, which is now additionally applied offline before the beam splitter. Note that the QND gate here is not simply replaced by a beam splitter followed by two single-mode squeezers and another beam splitter [16], all together applied to two initial squeezed states [Fig. 1(b)]. Instead, the circuit is further simplified, and only one pair of squeezers followed by one beam splitter operation act upon initial vacuum modes.

However, the canonical two-mode cluster state is rather wasteful in terms of squeezing resources. The most economical two-mode entangled state would be a standard two-mode squeezed state (TMSS) built from two single-mode squeezed states with a 50/50 beam splitter. Like any pure Gaussian two-mode state [18], also the canonical two-mode cluster state can be obtained from a TMSS via local Gaussian transformations, including local squeezers [Fig. 1(c)].

Comparing resources, for example, an excess noise of one vacuum unit in the quadrature correlations  $\hat{p}_1 - \hat{x}_2$  and  $\hat{p}_2 - \hat{x}_1$  can be achieved with a TMSS built from two 3 dB squeezed states (see next section). The canonical two-mode cluster state with these correlations  $(r = 0)$ , would require two  $4.18\mathrm{dB}$  squeezed states combined at the asymmetric beam splitter in Eq. (14). In general, the canonical  $N$ -mode cluster states are always biased in  $x$  and  $p$  [19],  $\langle \hat{x}_a^2\rangle = e^{+2r}\neq \langle \hat{p}_a^2\rangle = e^{-2r} + M_{N_a}e^{+2r}$ , unnecessarily requiring extra local squeezing to achieve a certain degree of correlations and entanglement; they cannot be obtained from  $N$ -mode pure Gaussian states in standard form [20] without the use of local squeezers. In the following, we shall consider a whole family of states producible via linear optics and exhibiting cluster-type correlations. This family will include states cheaper than the canonical cluster states.

# IV. GENERAL CLUSTER-TYPE STATES VIA LINEAR OPTICS

In order to create states with correlations as in Eq. (1) via linear optics, we consider  $p$ -squeezed input modes  $\hat{a}_l = e^{+R_l}\hat{x}_l^{(0)} + ie^{-R_l}\hat{p}_l^{(0)}$ , and a general linear-optics transformation  $\hat{a}_k' = \Sigma_l U_{kl} \hat{a}_l$ , with a unitary matrix  $U$ . From this we obtain the output quadrature operators

$$
\hat {x} _ {k} ^ {\prime} = \sum_ {l} \left(\mathrm {R e} U _ {k l} e ^ {+ R _ {l}} \hat {x} _ {l} ^ {(0)} - \mathrm {I m} U _ {k l} e ^ {- R _ {l}} \hat {p} _ {l} ^ {(0)}\right),
$$

$$
\hat {p} _ {k} ^ {\prime} = \sum_ {l} \left(\operatorname {I m} U _ {k l} e ^ {+ R _ {l}} \hat {x} _ {l} ^ {(0)} + \operatorname {R e} U _ {k l} e ^ {- R _ {l}} \hat {p} _ {l} ^ {(0)}\right), \tag {15}
$$

where  $\hat{a}_k' = \hat{x}_k' + i\hat{p}_k'$ . In order to satisfy the condition in Eq. (1), we assume the large noise terms (those proportional to  $e^{+R_l}$ ) cancel such that

$$
\sum_ {l} \operatorname {I m} U _ {a l} e ^ {+ R _ {l}} \hat {x} _ {l} ^ {(0)} - \sum_ {b \in N _ {a}} \sum_ {l} \operatorname {R e} U _ {b l} e ^ {+ R _ {l}} \hat {x} _ {l} ^ {(0)} = 0, \tag {16}
$$

$\forall a \in G$ . This is possible if and only if

$$
\operatorname {I m} U _ {a l} - \sum_ {b \in N _ {a}} \operatorname {R e} U _ {b l} = 0, \quad \forall a, l \in G. \tag {17}
$$

After inserting these conditions into the excess noise terms (those that vanish for infinite squeezing  $R_{l} \to \infty$ ), we find that each quadrature combination of Eq. (1), labeled by  $a$  for a given graph  $G$ , becomes

$$
\begin{array}{l} \hat {p} _ {a} ^ {G} - \sum_ {b \in N _ {a}} \hat {x} _ {b} ^ {G} = \sum_ {l} \operatorname {R e} U _ {a l} (1 + M _ {N _ {a}}) e ^ {- R _ {l}} \hat {p} _ {l} ^ {(0)} \\ + \sum_ {l} \sum_ {b \in N _ {a}} \sum_ {k \in N _ {b}, k \neq a} \operatorname {R e} U _ {k l} e ^ {- R _ {l}} \hat {p} _ {l} ^ {(0)}. \tag {18} \\ \end{array}
$$

The corresponding excess noise variance for a quadrature combination  $a$  can then be written as

$$
\sum_ {l} \left[ \operatorname {R e} U _ {a l} \left(1 + M _ {N _ {a}}\right) + \sum_ {b \in N _ {a}} \sum_ {k \in N _ {b}, k \neq a} \operatorname {R e} U _ {k l} \right] ^ {2} e ^ {- 2 R _ {l}}, \tag {19}
$$

times one unit of vacuum quadrature noise (1/4 in our scales) which we omit in the following. These excess noises will lead to the errors in the cluster computation [6]. Let us consider two-mode cluster-type states.

Look at the simple circuit described by

$$
U = \left( \begin{array}{l l} 1 & 0 \\ 0 & i \end{array} \right) \left( \begin{array}{c c} \frac {1}{\sqrt {2}} & \frac {1}{\sqrt {2}} \\ \frac {1}{\sqrt {2}} & - \frac {1}{\sqrt {2}} \end{array} \right) \left( \begin{array}{l l} 1 & 0 \\ 0 & i \end{array} \right) = \left( \begin{array}{c c} \frac {1}{\sqrt {2}} & \frac {i}{\sqrt {2}} \\ \frac {i}{\sqrt {2}} & \frac {1}{\sqrt {2}} \end{array} \right), \tag {20}
$$

applied to two momentum-squeezed modes. The circuit is a 50/50 beam splitter with Fourier transforms of mode 2 before and after the beam splitter. It clearly satisfies the conditions in Eq. (17),

$$
\operatorname {I m} U _ {1 1} = \operatorname {R e} U _ {2 1}, \quad \operatorname {I m} U _ {1 2} = \operatorname {R e} U _ {2 2},
$$

$$
\operatorname {I m} U _ {2 1} = \operatorname {R e} U _ {1 1}, \quad \operatorname {I m} U _ {2 2} = \operatorname {R e} U _ {1 2}. \tag {21}
$$

The resulting state is the standard TMSS up to a local Fourier transform of mode 2. No extra local squeezers are needed to obtain this cluster-type state from standard two-mode entanglement. According to Eq. (19), the excess noises in the cluster-type correlations are  $2e^{-2R_1}$  in  $\hat{p}_1 - \hat{x}_2$  and  $2e^{-2R_2}$  in  $\hat{p}_2 - \hat{x}_1$ , corresponding to the optimal entanglement for a given input squeezing  $R_1 = R_2$ . Note that the solutions in Eqs. (20) and (14) coincide for  $r\to \infty$  when  $C(r)\rightarrow 1$ .

We can now recast the conditions in Eq. (17) in terms of a set of geometrical vector conditions. Incorporating Eq. (17) into the column vectors of  $U$  leads to

$$
\vec {u} _ {l} \equiv \left( \begin{array}{c} \alpha_ {1 l} + i \sum_ {b \in N _ {1}} \alpha_ {b l} \\ \alpha_ {2 l} + i \sum_ {b \in N _ {2}} \alpha_ {b l} \\ \dots \\ \alpha_ {N l} + i \sum_ {b \in N _ {N}} \alpha_ {b l} \end{array} \right), \tag {22}
$$

with  $\Sigma_l(\vec{u}_l)_k(\vec{u}_l)_{k'}^* = \delta_{kk'}$  for unitarity, and again  $\operatorname{Re} U_{kl} \equiv \alpha_{kl}$ . Using this formalism, for any given graph state, one obtains a set of geometrical conditions for  $N$  real vectors  $\vec{\alpha}_k^T \equiv (\alpha_{k1}, \alpha_{k2}, \ldots, \alpha_{kN})$ . For instance, a linear four-mode cluster state has

$$
\vec {\alpha} _ {1} \vec {\alpha} _ {3} = \vec {\alpha} _ {2} \vec {\alpha} _ {4} = - 1 / 5,
$$

$$
\vec {a} _ {1} \vec {a} _ {2} = \vec {a} _ {1} \vec {a} _ {4} = \vec {a} _ {2} \vec {a} _ {3} = \vec {a} _ {3} \vec {a} _ {4} = 0,
$$

$$
\left\| \vec {\alpha} _ {1} \right\| = \left\| \vec {\alpha} _ {4} \right\| = 3 / 5, \quad \left\| \vec {\alpha} _ {2} \right\| = \left\| \vec {\alpha} _ {3} \right\| = 2 / 5, \tag {23}
$$

achievable, for example, with

$$
\vec {\alpha} _ {1} ^ {T} = (1 / \sqrt {2}, 1 / \sqrt {1 0}, 0, 0),
$$

$$
\vec {\alpha} _ {2} ^ {T} = (0, 0, - 2 / \sqrt {1 0}, 0),
$$

$$
\vec {\alpha} _ {3} ^ {T} = (0, - 2 / \sqrt {1 0}, 0, 0),
$$

$$
\vec {\alpha} _ {4} ^ {T} = (0, 0, 1 / \sqrt {1 0}, - 1 / \sqrt {2}). \tag {24}
$$

This, together with Eq. (22), where we set  $N = 4$ , defines a possible solution  $U$ .

In general, any four-mode transformation  $U$  can be decomposed into a network of  $4(4 - 1) / 2 = 6$  beam splitters [21]. However, for the linear four-mode cluster, there is a minimal decomposition of  $U$  into a network of only three beam splitters,

$$
U = F _ {4} S _ {1 2} F _ {1} ^ {\dagger} B _ {3 4} ^ {+} (1 / \sqrt {2}) B _ {1 2} ^ {+} (- 1 / \sqrt {2}) B _ {2 3} ^ {-} (1 / \sqrt {5}) F _ {3} ^ {\dagger} F _ {4} ^ {\dagger}. \tag {25}
$$

Here,  $F_{k}$  (Fourier transform of mode  $k$ ) is the four-mode identity matrix  $I_{4}$  except  $(F_{k})_{kk} = i$ ,  $B_{kl}^{\pm}(t)$  (beam splitter transformation of modes  $k$  and  $l$ ) equals  $I_{4}$  except  $(B_{kl}^{\pm})_{kk} = t$ ,  $(B_{kl}^{\pm})_{kl} = \sqrt{1 - t^{2}}$ ,  $(B_{kl}^{\pm})_{lk} = \pm \sqrt{1 - t^{2}}$ , and  $(B_{kl}^{\pm})_{ll} = \mp t$ , and the matrix  $S_{12}$  swaps modes 1 and 2.

Similarly, one can find linear-optics solutions for other cluster-type states (Fig. 2), including T-shape and cross-shape clusters, exhibiting "GHZ-type" correlations [22] up to local Fourier transforms. The example of a nonlinear six-mode cluster in Fig. 2(a) (a potential resource for two-mode evolutions) leads to two orthogonal subspaces  $\{\vec{\alpha}_k,\vec{\alpha}_l,\vec{\alpha}_m\}$  with  $\{k,l,m\} = \{1,3,5\}$  and  $\{k,l,m\} = \{6,4,2\}$ , where

$$
\vec {\alpha} _ {k} \vec {\alpha} _ {l} = - 3 / 1 0, \quad \vec {\alpha} _ {k} \vec {\alpha} _ {m} = \vec {\alpha} _ {l} \vec {\alpha} _ {m} = - 1 / 1 0,
$$

$$
\left\| \vec {\alpha} _ {k} \right\| = \left\| \vec {\alpha} _ {l} \right\| = 7 / 1 0, \quad \left\| \vec {\alpha} _ {m} \right\| = 3 / 1 0. \tag {26}
$$

A possible solution is

$$
\vec {\alpha} _ {1} ^ {T} = (1 / \sqrt {5}, 1 / \sqrt {2}, 0, 0, 0, 0),
$$

![](images/343149ba0e247ebd1af4c1af820dbbe7e0578db7c1f5428915c694af29532a9a.jpg)  
a)

![](images/c54306f2ccf578350f19264fba3242970e83832124644c61a9f7a8f04140fe97.jpg)  
FIG. 2. (Color online) Examples of cluster-type states produc-ible via linear optics; each optical mode or cluster node  $a$  is represented by a vector  $\vec{\alpha}_a$  (see text): (a) linear four-mode cluster, nonlinear six-mode cluster; (b) "EPR/GHZ-type" [22] clusters: linear two- and three-mode clusters, T-shape, and cross-shape clusters.  
b)

$$
\vec {\alpha} _ {2} ^ {T} = (0, 0, 0, - 1 / \sqrt {2 0}, 0, 1 / 2),
$$

$$
\vec {\alpha} _ {3} ^ {T} = (1 / \sqrt {5}, - 1 / \sqrt {2}, 0, 0, 0, 0),
$$

$$
\vec {\alpha} _ {4} ^ {T} = (0, 0, 0, 1 / \sqrt {5}, 1 / \sqrt {2}, 0),
$$

$$
\vec {\alpha} _ {5} ^ {T} = (- 1 / \sqrt {2 0}, 0, 1 / 2, 0, 0, 0),
$$

$$
\vec {\alpha} _ {6} ^ {T} = (0, 0, 0, 1 / \sqrt {5}, - 1 / \sqrt {2}, 0). \tag {27}
$$

In general, using the geometrical conditions for  $N$ $N$ -dimensional vectors, solutions can be recursively constructed for any graph state: start with  $\vec{\alpha}_1^T = (\alpha_{11},0,0,\dots)$  determined by the norm  $\| \vec{\alpha}_1\|$ , then  $\vec{\alpha}_2^T = (\alpha_{21},\alpha_{22},0,\dots)$  given by the overlap  $\vec{\alpha}_1\vec{\alpha}_2$  and the norm  $\| \vec{\alpha}_2\|$ ,  $\vec{\alpha}_3^T = (\alpha_{31},\alpha_{32},\alpha_{33},\dots)$  via  $\vec{\alpha}_1\vec{\alpha}_3$ ,  $\vec{\alpha}_2\vec{\alpha}_3$ , and  $\| \vec{\alpha}_3\|$ , etc. Let us discuss another example in the following section.

# V. EXAMPLE: REDUNDANT ENCODING FOR ERROR FILTRATION

As an application of our approach, we consider cluster states based on a redundant encoding ("multiple-rail encoding"). We will argue that under certain circumstances, this could be useful for error filtration in a Gaussian cluster computation protocol [6]. For this purpose, we discuss the propagation of a single-mode quantum state through a multiple-rail cluster. We can then analyze the effect of this kind of encoding on the excess noise of the teleported state and hence on the fidelity of the state transmission through the cluster.

For an actual cluster-state computation [6], the simple state transmission through the cluster would become a state transformation (a gate), where the input state is transformed at every measurement step by choosing an appropriate measurement basis. In this case, the distortion of the input state for a finitely squeezed cluster would depend on the particular gate to be realized. Here, for our analysis of noise reduction via redundant encoding, we will only consider the simple case of state transmission through the cluster.

A simple cluster protocol would be to teleport an input mode onto mode 1 of a "diamond state" and from there to mode 4 [Fig. 3(b)]. For simplicity, we assume that the input mode is attached to mode 1 through the QND gate  $e^{2i\hat{x}_{\mathrm{in}}\otimes \hat{x}_1}$

such that  $\hat{p}_1\rightarrow \hat{p}_1 + \hat{x}_{\mathrm{in}}$  and  $\hat{p}_{\mathrm{in}}\rightarrow \hat{p}_{\mathrm{in}} + \hat{x}_1;\hat{x}_1$  and  $\hat{x}_{\mathrm{in}}$  remain unchanged. Now  $p$  measurements of the input mode and modes 1-3 (with results  $s_{\mathrm{in}},s_{1\dots 3}$ ) would transform mode 4 into the input state up to some known corrections and excess noise coming from the imperfect diamond state. After the correction operation  $\hat{F}^{\dagger}\hat{X} (-s_{\mathrm{in}})\hat{F}^{\dagger}\hat{X} (-s_1)\hat{F}^{\dagger}\hat{X} [-(s_2 + s_3) / 2]$ , with an inverse Fourier transform operator  $\hat{F}^{\dagger}$  acting as  $\hat{x}\rightarrow \hat{p}$  and  $\hat{p}\rightarrow -\hat{x}$ , and  $x$  displacements  $\hat{X} (s)$  such that  $\hat{x}\rightarrow \hat{x} +s$ , mode 4 is described by

$$
\hat {x} _ {\mathrm {o u t}} = \hat {x} _ {\mathrm {i n}} + (\hat {p} _ {1} - \hat {x} _ {2} - \hat {x} _ {3}) - (\hat {p} _ {4} - \hat {x} _ {2} - \hat {x} _ {3}),
$$

$$
\hat {p} _ {\text {o u t}} = \hat {p} _ {\text {i n}} - \left(\hat {p} _ {2} - \hat {x} _ {1} - \hat {x} _ {4}\right) / 2 - \left(\hat {p} _ {3} - \hat {x} _ {1} - \hat {x} _ {4}\right) / 2. \tag {28}
$$

Here,  $\hat{p}_{\mathrm{in}}$  and  $\hat{p}_1$  correspond to the momentum operators of the input mode and mode 1 of the diamond state before the QND coupling.

We see that the imperfect teleportation fidelities depend on the correlations of the diamond state, Eq. (1) with Fig. 3(b). Only for infinite squeezing, the unwanted terms in Eq. (28) vanish and the input state appears at the output with unit fidelity. Note that this unit-fidelity transmission can be achieved with any cluster-type state that exhibits the corresponding correlations, Eq. (1) with Fig. 3(b), in the limit of infinite squeezing. Let us now discuss the case of finitely squeezed resource states in more detail. First, we consider QND-made cluster states.

If we had QND gates freely available, we could perform the entire teleportation protocol using these gates, including creation of the diamond state. In this case, the  $\hat{x}$ -excess noise in the teleported mode of Eq. (28) would correspond to  $\mathrm{Var}[(\hat{p}_1 - \hat{x}_2 - \hat{x}_3) - (\hat{p}_4 - \hat{x}_2 - \hat{x}_3)] = \mathrm{Var}[e^{-r}(\hat{p}_1^{(0)} - \hat{p}_4^{(0)})] = 2e^{-2r}$ . (Here, and in what follows, we again omit the factor of  $1/4$  for a quadrature vacuum variance.) The  $\hat{p}$ -excess noise becomes  $\mathrm{Var}[(\hat{p}_2 - \hat{x}_1 - \hat{x}_4)/2 + (\hat{p}_3 - \hat{x}_1 - \hat{x}_4)/2] = \mathrm{Var}[e^{-r}(\hat{p}_2^{(0)} + \hat{p}_3^{(0)})/2] = e^{-2r}/2$ . Let us compare this with a scheme in which the input state is attached to and teleported through a linear three-mode cluster [Fig. 3(a)], with the output quadratures

$$
\hat {x} _ {\mathrm {o u t}} = \hat {x} _ {\mathrm {i n}} + (\hat {p} _ {1} - \hat {x} _ {2}) - (\hat {p} _ {3} - \hat {x} _ {2}),
$$

$$
\hat {p} _ {\text {o u t}} = \hat {p} _ {\text {i n}} - (\hat {p} _ {2} - \hat {x} _ {1} - \hat {x} _ {3}). \tag {29}
$$

Now the excess noises in  $\hat{x}$  and  $\hat{p}$  are, respectively,  $\mathrm{Var}[(\hat{p}_1 - \hat{x}_2) - (\hat{p}_3 - \hat{x}_2)] = \mathrm{Var}[e^{-r}(\hat{p}_1^{(0)} - \hat{p}_3^{(0)})] = 2e^{-2r}$  and  $\mathrm{Var}(\hat{p}_2 - \hat{x}_1 - \hat{x}_3) = \mathrm{Var}[e^{-r}\hat{p}_2^{(0)}] = e^{-2r}$ , for a QND-made linear cluster state.

In comparison to the diamond-based protocol, the excess noise in  $\hat{x}$  is unchanged. However, the  $\hat{p}$ -excess noise is only half as big in the diamond-based scheme compared to the protocol with the linear three-mode cluster. Similarly, multiple paths between modes 1 and  $N$  [Fig. 3(c)] result in a reduction of the  $\hat{p}$  noise,

$$
\begin{array}{l} \operatorname {V a r} \left[ \left(\hat {p} _ {2} - \hat {x} _ {1} - \hat {x} _ {N}\right) / m + \left(\hat {p} _ {3} - \hat {x} _ {1} - \hat {x} _ {N}\right) / m \right. \\ + \dots + \left(\hat {p} _ {N - 1} - \hat {x} _ {1} - \hat {x} _ {N}\right) / m ], \tag {30} \\ \end{array}
$$

![](images/c8bd90a470f74176b701b8db7ecb063a9be06bb6150b0a532821f4ac5edd4078.jpg)  
a)

![](images/bed3bb615f9ff3bcea4b758ecf6032065fcf8c8eb96d4586c7ae0739912f2a9e.jpg)  
b)

![](images/f010779dca1985faf7b7df6aa1967927c5a9125a87872276e34163222ced0668.jpg)  
FIG. 3. (Color online) Error propagation when an input state is attached to and teleported through (a) a linear three-mode cluster; (b) a four-mode diamond cluster; (c) an  $N$ -mode multiple-rail cluster; all clusters can be created by off-line squeezing and linear optics.  
c)

scaling as  $e^{-2r} / m$ , where  $m = N - 2$  is the number of intermediate nodes (number of rails) between mode 1 and the output mode  $N$ . The  $\hat{x}$  noise,

$$
\operatorname {V a r} \left[ \left(\hat {p} _ {1} - \hat {x} _ {2} - \hat {x} _ {3} - \dots - \hat {x} _ {N - 1}\right) - \left(\hat {p} _ {N} - \hat {x} _ {2} - \hat {x} _ {3} - \dots - \hat {x} _ {N - 1}\right) \right], \tag {31}
$$

will remain unchanged. For example, using six 3 dB squeezed resource states for multiple-rail encoding, i.e.,  $m = 4$  and  $e^{-2r} = 1/2$ , we obtain one unit of vacuum excess noise in  $\hat{x}$ , but only 1/8 times a vacuum unit excess noise in  $\hat{p}$  (compared to half a vacuum unit excess noise without multiple-rail encoding). Thus, we conclude that, with QND gates freely available, multiple-rail encoding may reduce errors in cluster computation.

A possible scenario for this would be when the quantum information to be transferred through the cluster is encoded in such a way that it is less sensitive to errors in  $\hat{x}$  than in  $\hat{p}$  and an asymmetric accumulation of errors in phase space would be beneficial. Another possibility is that the experimentalist has access to a highly asymmetric supply of squeezing resources and then uses the largest available squeezing for the end nodes of the multiple-rail cluster (modes 1 and  $N$  whose squeezing occurs in the  $\hat{x}$  quadrature noise). The effect of the smaller squeezing of the remaining modes could then be suppressed in multiple-rail encoding.

The discussion of the preceding paragraphs raises the question whether a similar error filtration can be achieved with multiple-rail graph states built from off-line squeezed states via linear optics. Obviously, the same error reduction (scaling as  $e^{-2r} / m$ ) would occur, when the canonical multiple-rail clusters are created, using our first algorithm based on Bloch-Messiah reduction. However, such a scheme would require higher degrees of squeezing for the cluster generation, increasing with the number of extra rails [23]. The larger squeezing could then as well be used directly in a single-rail scheme and this would trivially achieve smaller excess noise. Therefore, let us consider the more general class of multiple-rail clusters, producible via our vector-based, second algorithm of Sec. IV.

For the diamond cluster state in Fig. 3(b), the vector conditions become  $\vec{\alpha}_1\vec{\alpha}_2 = \vec{\alpha}_1\vec{\alpha}_3 = \vec{\alpha}_2\vec{\alpha}_4 = \vec{\alpha}_3\vec{\alpha}_4 = 0$ ,  $\vec{\alpha}_2\vec{\alpha}_3 = \vec{\alpha}_1\vec{\alpha}_4 = -2/5$ , and  $||\vec{\alpha}_k|| \equiv 3/5$ . This can be satisfied, for example, with

$$
\vec {\alpha} _ {1} ^ {T} = (1 / \sqrt {3}, - 2 / \sqrt {1 5}, 0, 0),
$$

$$
\vec {\alpha} _ {2} ^ {T} = (0, 0, 1 / \sqrt {3}, - 2 / \sqrt {1 5}),
$$

$$
\vec {\alpha} _ {3} ^ {T} = (0, 0, 0, \sqrt {3 / 5}),
$$

$$
\vec {\alpha} _ {4} ^ {T} = (0, \sqrt {3 / 5}, 0, 0). \tag {32}
$$

Together with Eq. (22) for  $N = 4$ , this defines a possible solution  $U$ , realizable through a network of at most six beam splitters [21]. Now we attach an input mode to mode 1 of the linear-optics-made diamond state (using a QND gate) and teleport it through the cluster to mode 4 [Fig. 3(b)]. The teleportation protocol is the same as described above. Hence the output quadratures are again given by Eq. (28). Using Eq. (18) for the diamond graph, we can calculate the excess noise in  $\hat{x}$ ,

$$
\begin{array}{l} \operatorname {V a r} \left[ \left(\hat {p} _ {1} - \hat {x} _ {2} - \hat {x} _ {3}\right) - \left(\hat {p} _ {4} - \hat {x} _ {2} - \hat {x} _ {3}\right) \right] \\ = \operatorname {V a r} \left[ (1 / \sqrt {3}) e ^ {- R _ {1}} \hat {p} _ {1} ^ {(0)} - \sqrt {5 / 3} e ^ {- R _ {2}} \hat {p} _ {2} ^ {(0)} \right] \\ = e ^ {- 2 R _ {1}} / 3 + 5 e ^ {- 2 R _ {2}} / 3 \\ = 2 e ^ {- 2 R}, \tag {33} \\ \end{array}
$$

up to a vacuum unit factor  $1/4$  (again omitted here and in the following). For the last equality, we assumed equal squeezing resources,  $R_{1} = R_{2} \equiv R$ . Note that now the quadrature combinations are no longer uncorrelated,  $\hat{p}_{1} - \hat{x}_{2} - \hat{x}_{3} = \sqrt{3} e^{-R_{1}} \hat{p}_{1}^{(0)}$  and  $\hat{p}_{4} - \hat{x}_{2} - \hat{x}_{3} = (2/\sqrt{3}) e^{-R_{1}} \hat{p}_{1}^{(0)} + \sqrt{5/3} e^{-R_{2}} \hat{p}_{2}^{(0)}$ . Similarly, the excess noise in  $\hat{p}$  becomes

$$
\begin{array}{l} \operatorname {V a r} \left[ \left(\hat {p} _ {2} - \hat {x} _ {1} - \hat {x} _ {4}\right) / 2 + \left(\hat {p} _ {3} - \hat {x} _ {1} - \hat {x} _ {4}\right) / 2 \right] \\ = \operatorname {V a r} \left[ (5 / \sqrt {3}) e ^ {- R _ {3}} \hat {p} _ {3} ^ {(0)} + \sqrt {5 / 3} e ^ {- R _ {4}} \hat {p} _ {4} ^ {(0)} \right] / 4 \\ = (2 5 e ^ {- 2 R _ {3}} / 3 + 5 e ^ {- 2 R _ {4}} / 3) / 4 \\ = 5 e ^ {- 2 R} / 2, \tag {34} \\ \end{array}
$$

for equal squeezing  $R$ . Let us compare this result with the excess noises after state transmission through a general linear-optics-made, single-rail, linear three-mode cluster [Fig. 3(a)],  $N = 3$  and  $m = 1$  [24],

$$
\begin{array}{l} \operatorname {V a r} \left[ \sum_ {l} \left(\alpha_ {1 l} - \alpha_ {3 l}\right) e ^ {- R _ {l}} \hat {p} _ {l} ^ {(0)} \right] = \left(\left\| \vec {\alpha} _ {1} \right\| + \left\| \vec {\alpha} _ {3} \right\| - 2 \vec {\alpha} _ {1} \vec {\alpha} _ {3}\right) e ^ {- 2 R} \\ = 2 e ^ {- 2 R}, \tag {35} \\ \end{array}
$$

and

$$
\mathrm {V a r} \bigg (\sum_ {l} 3 \alpha_ {2 l} e ^ {- R _ {l}} \hat {p} _ {l} ^ {(0)} \bigg) = 9 \| \vec {\alpha} _ {2} \| e ^ {- 2 R} = 3 e ^ {- 2 R},
$$

for  $\hat{x}$  and  $\hat{p}$ , respectively. Here we have used Eqs. (29) and (18), and assumed equal squeezing,  $R_{l} \equiv R$ .

We observe that for the diamond-based scheme, the  $\hat{p}$ -excess noise is slightly suppressed, by a factor of 5/6, compared to the general single-rail scheme; the  $\hat{x}$ -excess noise again remains unchanged. Thus, we still obtain an excess noise reduction, but this reduction is smaller than that for QND-made cluster states. Numerically, we find that for larger multiple-rail clusters with larger numbers of rails  $m$

$= N - 2$  [24], the  $\hat{p}$ -excess noises are  $(21/9)e^{-2R} \approx 2.33e^{-2R}$  ( $m = 3$ ) and  $(9/4)e^{-2R} = 2.25e^{-2R}$  ( $m = 4$ ); the  $\hat{x}$ -excess noises are still unchanged,  $2e^{-2R}$ . We conclude that even using linear-optics-made multiple-rail clusters some error reduction may occur. However, an arbitrarily good noise suppression (in one phase-space variable), as it is possible with QND-based redundant encoding, appears to be unattainable using the general linear-optics scheme of Sec. IV.

# VI. CONCLUSION

In this paper, we derived various protocols for the creation of Gaussian cluster (graph) states via linear optics and offline squeezing. In these schemes, no online squeezers are needed. This is in contrast to protocols in which the QND coupling for every single link of the cluster is simply replaced by two beam splitters and two squeezers.

Our first algorithm, based on Bloch-Messiah reduction, leads to the generation of canonical cluster states, as originally defined in terms of QND interactions. This algorithm works for any cluster (graph) state. Using a second, more general algorithm, expressible in terms of geometrical vector conditions, a whole family of cluster-type states can be produced by linear optics. Again, any graph-type state can be built via this algorithm. The extended family of cluster-type states contains potentially cheaper states (in terms of squeezing resources) compared to the canonical states. The simplest example for the different resource costs is the two-mode cluster state.

Finally, we discussed a cluster-state protocol in which a single-mode quantum state is transmitted through a multiple-rail cluster. As long as the multiple-rail clusters are produced via QND interactions, the redundant encoding of the cluster states results in a reduction of the finite-squeezing-induced excess noise in one phase-space variable (to an arbitrary extent for sufficiently many extra rails); the excess noise in the conjugate variable remains unchanged compared to the single-rail case. The same noise suppression is achieved, when the canonical multiple-rail clusters are created using our first algorithm based on Bloch-Messiah reduction. However, such a scheme would require higher degrees of squeezing for the cluster generation, increasing with the number of extra rails. The larger squeezing could then as well be used directly in a single-rail scheme. When the multiple-rail clusters are produced according to our second algorithm, some error filtration still occurs during the state transmission, but it seems the excess noise (in one phase-space variable) cannot be made arbitrarily small by adding extra rails.

Gaussian continuous-variable cluster states represent a practical, readily available resource for small-scale quantum information processing and quantum computation. This statement even extends to universal quantum computation, provided non-Gaussian measurements are included during the cluster computation. In this paper, we proposed several schemes for the efficient generation of Gaussian cluster-type states. The scheme for the creation of canonical cluster states (first algorithm) is directly applicable to cluster computation, as the resulting states are identical to those originally proposed for cluster computation [6]. The more general, broader

class of cluster-type states (second algorithm) reproduces the quadrature correlations of the canonical states in the limit of infinite squeezing. It should be further investigated whether the whole family of Gaussian cluster states, in the case of finite squeezing, is just as useful for cluster computation as the canonical states. Moreover, more robust and efficient methods are still needed in order to avoid the occurrence of

errors induced by the finite squeezing of the Gaussian cluster states.

# ACKNOWLEDGMENTS

P.v.L. acknowledges the MIC in Japan. C.W. and M.G. thank the Australian Research Council for support.

[1] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[2] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2000).  
[3] D. L. Zhou, B. Zeng, Z. Xu, and C. P. Sun, Phys. Rev. A 68, 062303 (2003).  
[4] Sean Clark, J. Phys. A 39, 2701 (2006).  
[5] William Hall, e-print arXiv:quant-ph/0512130.  
[6] N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, and M. A. Nielsen, Phys. Rev. Lett. 97, 110501 (2006).  
[7] P. Kok, W J. Munro, K. Nemoto, T. C. Ralph, J. P. Dowling, and G. J. Milburn, Rev. Mod. Phys. 79, 135 (2007).  
[8] S. L. Braunstein and P. van Loock, Rev. Mod. Phys. 77, 513 (2005).  
[9] E. Knill, R. Laflamme, and G. J. Milburn, Nature (London) 409, 46 (2001).  
[10] M. A. Nielsen, Phys. Rev. Lett. 93, 040503 (2004).  
[11] D. E. Browne and T. Rudolph, Phys. Rev. Lett. 95, 010501 (2005).  
[12] P. Walther, K. J. Resch, T. Rudolph, E. Schenck, H. Weinfurter, V. Vedral, M. Aspelmeyer, and A. Zeilinger, Nature (London) 434, 169 (2005).  
[13] C.-Y. Lu, X.-Q. Zhou, O. Gühne, W.-B. Gao, J. Zhang, Z.-S. Yuan, A. Goebel, T. Yang, and J.-W. Pan, Nat. Phys. 3, 91 (2007).

[14] J. Zhang and S. L. Braunstein, Phys. Rev. A 73, 032318 (2006).  
[15] S. Lloyd and S. L. Braunstein, Phys. Rev. Lett. 82, 1784 (1999).  
[16] S. L. Braunstein, Phys. Rev. A 71, 055801 (2005).  
[17] M. Hein, J. Eisert, and H. J. Briegel, Phys. Rev. A 69, 062311 (2004).  
[18] L.-M. Duan, G. Giedke, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 84, 2722 (2000).  
[19] W. P. Bowen, P. K. Lam, and T. C. Ralph, J. Mod. Opt. 50, 801 (2003).  
[20] G. Adesso, Phys. Rev. Lett. 97, 130502 (2006).  
[21] M. Reck, A. Zeilinger, H. J. Bernstein, and P. Bertani, Phys. Rev. Lett. 73, 58 (1994).  
[22] P. van Loock and S. L. Braunstein, Phys. Rev. Lett. 84, 3482 (2000).  
[23] Recall that for "truly" QND-made clusters, the excess noise variances and the variances of the input squeezing are described by the same squeezing factor,  $e^{-2r}$ . In contrast, after Bloch-Messiah reduction for canonical cluster generation, the excess noise factors  $e^{-2r}$  no longer reflect the degree of input squeezing (which is described by a different squeezing factor  $e^{-2R}$ , with  $R > r$ ).  
[24] For general  $N$  and  $m = N - 2$ , the vector conditions are  $\vec{\alpha}_1\vec{\alpha}_N = (m - 2m^2) / (4m^2 - 1)$ ,  $\vec{\alpha}_k\vec{\alpha}_l = (2 - 4m) / (4m^2 - 1)$ ,  $(k, l \neq 1, N)$ ,  $\vec{\alpha}_1\vec{\alpha}_k = \vec{\alpha}_N\vec{\alpha}_k = 0$ ,  $\|\vec{\alpha}_1\| = \|\vec{\alpha}_N\| = (2m^2 + m - 1) / (4m^2 - 1)$ , and  $\|\vec{\alpha}_k\| = (4m^2 - 4m + 1) / (4m^2 - 1)$ .