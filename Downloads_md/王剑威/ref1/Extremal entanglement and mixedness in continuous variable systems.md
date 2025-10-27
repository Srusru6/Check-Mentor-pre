# Extremal entanglement and mixedness in continuous variable systems

Gerardo Adesso, Alessio Serafini, and Fabrizio Illuminati  
Dipartimento di Fisica "E. R. Caianiello," Università di Salerno, INFM UdR di Salerno, INFN Sezione di Napoli, Gruppo Collegato di Salerno, Via S. Allende, 84081 Baronissi (SA), Italy  
(Received 27 February 2004; revised manuscript received 10 May 2004; published 25 August 2004)

We investigate the relationship between mixedness and entanglement for Gaussian states of continuous variable systems. We introduce generalized entropies based on Schatten  $p$  norms to quantify the mixedness of a state and derive their explicit expressions in terms of symplectic spectra. We compare the hierarchies of mixedness provided by such measures with the one provided by the purity (defined as  $\operatorname{tr} \varrho^2$  for the state  $\varrho$ ) for generic  $n$ -mode states. We then review the analysis proving the existence of both maximally and minimally entangled states at given global and marginal purities, with the entanglement quantified by the logarithmic negativity. Based on these results, we extend such an analysis to generalized entropies, introducing and fully characterizing maximally and minimally entangled states for given global and local generalized entropies. We compare the different roles played by the purity and by the generalized  $p$  entropies in quantifying the entanglement and the mixedness of continuous variable systems. We introduce the concept of average logarithmic negativity, showing that it allows a reliable quantitative estimate of continuous variable entanglement by direct measurements of global and marginal generalized  $p$  entropies.

DOI: 10.1103/PhysRevA.70.022318

PACS number(s): 03.67.Mn, 03.65.Ud

# I. INTRODUCTION

The degree of entanglement (i.e., the contents in quantum correlations) as well as the degree of mixedness (i.e., the "amount" by which a state fails to be pure) are among the crucial features of quantum states from the point of view of quantum information theory. Indeed, the search for proper analytical ways to quantify such features for general (mixed) quantum states cannot be yet considered accomplished. In view of such considerations, it is clear that a full understanding of the relationships between the quantum correlations contained in a bipartite state and the global and local (i.e., referring to the reduced states of the two subsystems) degrees of mixedness of the state would be desirable. In particular, it would be a relevant step towards clarification of the nature of quantum correlations and, possibly, of the distinction between quantum and classical correlations of mixed states, which remains an open issue [1]. A simple question one can raise in such a context is the investigation of the properties of extremely entangled states for a given degree of mixedness.

Let us mention that, as for two-qubit systems, the notion of maximally entangled states at fixed mixedness (MEMS) was originally introduced by Ishizaka and Hiroshima [2]. The discovery of such states spurred several theoretical works [3], aimed at exploring the relations between different measures of entanglement and mixedness [4] (strictly related to the question of the ordering of these different measures [5]). Moreover, maximally entangled states for given local (or "marginal") mixednesses have been recently introduced and analyzed in detail in the context of qubit systems [6]. On the experimental side, much attention has been devoted to exploring the two-qubit Hilbert space in optical settings [7], while the experimental realization of MEMS has been recently demonstrated [8].

Because of the great current interest in continuous variable (CV) quantum information [9-12], the extension of such

analyses to infinite-dimensional systems is highly desirable. In the present work, we introduce and study in detail extremely entangled mixed Gaussian states of infinite-dimensional Hilbert spaces for fixed global and marginal generalized entropies, significantly generalizing the results derived earlier in Ref. [13], where the existence of maximally and minimally entangled mixed Gaussian states at given global and marginal purities was first discovered. In the present paper we will make use of a hierarchy of generalized entropies, based on the Schatten  $p$  norms, to quantify mixedness and characterize extremal entanglement in CV systems and investigate several related subjects, like the ordering of such different entropic measures and the relations between Einstein-Podolsky-Rosen (EPR) correlations and symplectic spectra. The crucial starting point of our analysis is the observation that the existence of infinitely entangled states [14,15] prevents maximally entangled Gaussian states from being defined as states with maximal, finite, logarithmic negativity, even at fixed global mixedness [16]. However, we will show that fixing the global and local mixednesses allows us to define unambiguously both maximally and minimally entangled mixed Gaussian states. This relevant and somehow surprising result—there is no analog of Gaussian minimally entangled states in finite-dimensional systems—turns out to have an experimental interest as well [13,17].

The paper is structured as follows. In Sec. II we briefly review the basic notation and the general properties of Gaussian states. In Sec. III we introduce the hierarchy of generalized Schatten  $p$  norms and entropies, and we extensively discuss the problem of the ordering of different entropic measures for states with an arbitrary number of modes. In Sec. IV we review the state of the art on the existing, computable measures of entanglement for two-mode Gaussian states, while in Sec. V we present a heuristic argument relating EPR correlations to symplectic spectra. In Sec. VI we introduce a parametrization of two-mode Gaussian states in terms of symplectic invariants endowed with a direct

physical interpretation. Exploiting these results, in Sec. VII we define maximally and minimally entangled states for given global and marginal purities and present some experimental situations in which these states occur. In Sec. VIII we generalize the concept of extremal entanglement in CV systems by introducing maximally and minimally entangled states for given global and local generalized entropies of arbitrary order, and we present an extensive study of their properties. We find out, somehow surprisingly, that maximally and minimally entangled states can interchange their roles for certain ranges of values of the global and marginal  $p$  entropies; moreover, we observe that with increasing  $p$  the generalized entropies, while carrying in general less information on a quantum state, provide a more accurate quantification of its entanglement. In Sec. IX we introduce and study the concept of "average logarithmic negativity," showing that this quantity provides an excellent quantitative estimate of CV entanglement based only on the knowledge of global and local entropies. Finally, in Sec. X we summarize our results and discuss future perspectives.

# II. GAUSSIAN STATES: GENERAL OVERVIEW

Let us consider a CV system, described by an Hilbert space  $\mathcal{H} = \otimes_{i=1}^{n}\mathcal{H}_{i}$  resulting from the tensor product of the infinite-dimensional Fock spaces  $\mathcal{H}_{i}$ 's. Let  $a_{i}$  be the annihilation operator acting on  $\mathcal{H}_{i}$ , and  $\hat{x}_{i} = (a_{i} + a_{i}^{\dagger})$  and  $\hat{p}_{i} = (a_{i} - a_{i}^{\dagger}) / i$  be the related quadrature phase operators. The corresponding phase space variables will be denoted by  $x_{i}$  and  $p_{i}$ . Let us group together the operators  $\hat{x}_{i}$  and  $\hat{p}_{i}$  in a vector of operators  $\hat{X} = (\hat{x}_{1},\hat{p}_{1},\dots,\hat{x}_{n},\hat{p}_{n})$ . The canonical commutation relations for the  $\hat{X}_{i}$ 's are encoded in the symplectic form  $\Omega$ :

$$
[ \hat {X} _ {i}, \hat {X} _ {j} ] = 2 i \Omega_ {i j},
$$

$$
\text {w i t h} \quad \boldsymbol {\Omega} \equiv \underset {i = 1} {\overset {n} {\oplus}} \boldsymbol {\omega}, \quad \boldsymbol {\omega} \equiv \left( \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right).
$$

The set of Gaussian states is, by definition, the set of states with Gaussian characteristic functions and quasiprobability distributions. Therefore a Gaussian state  $\varrho$  is completely characterized by its first and second statistical moments, which form, respectively, the vector of first moments  $\bar{X} \equiv (\langle \hat{X}_1\rangle ,\langle \hat{X}_1\rangle ,\dots ,\langle \hat{X}_n\rangle ,\langle \hat{X}_n\rangle)$  and the covariance matrix of elements  $\pmb{\sigma}$ :

$$
\sigma_ {i j} \equiv \frac {1}{2} \left\langle \hat {X} _ {i} \hat {X} _ {j} + \hat {X} _ {j} \hat {X} _ {i} \right\rangle - \left\langle \hat {X} _ {i} \right\rangle \left\langle \hat {X} _ {j} \right\rangle , \tag {1}
$$

where, for any observable  $\hat{o}$ , the expectation value  $\langle \hat{o} \rangle \equiv \mathrm{Tr}(\varrho \hat{o})$ . First statistical moments can be arbitrarily adjusted by local unitary operations, which cannot affect any property related to entanglement or mixedness. Therefore they will be unimportant to our aims and we will set them to 0 in the following, without any loss of generality. Throughout the paper,  $\sigma$  will stand for the covariance matrix of the Gaussian state  $\varrho$ .

Let us now consider the hermitian operator  $\hat{y} = Y\hat{X}^T$ , where  $Y \in \mathbb{R}^{2n}$  is an arbitrary real  $2n$ -dimensional row vector. Posi-

tivity of  $\varrho$  imposes  $\mathrm{Tr}(\varrho \hat{y}^2) \geqslant 0$ , which can be simply recast in terms of second moments as  $Y\tau Y^{T} \geqslant 0$ , with  $\tau_{ij} = \langle \hat{X}_i\hat{X}_j\rangle$ . From this relation, exploiting the canonical commutation relations and recalling definition (1) and the arbitrarity of  $Y$ , the Heisenberg uncertainty principle can be recast in the form

$$
\boldsymbol {\sigma} + i \boldsymbol {\Omega} \geqslant 0. \tag {2}
$$

Inequality (2) is the necessary and sufficient constraint  $\sigma$  has to fulfill to be a bona fide covariance matrix [18,19]. We mention that such a constraint implies  $\sigma \geqslant 0$ .

In the following, we will make use of the Wigner quasiprobability representation  $W(x_{i},p_{i})$  defined, for any density matrix, as the Fourier transform of the symmetrically ordered characteristic function [20]. In Wigner phase-space picture, the tensor product  $\mathcal{H} = \otimes \mathcal{H}_i$  of the Hilbert spaces  $\mathcal{H}_i$ 's of the  $n$  modes results in the direct sum  $\Gamma = \oplus \Gamma_i$  of the phase spaces  $\Gamma_i$ 's. In general, as a consequence of the Stone-von Neumann theorem, any symplectic transformation acting on the phase space  $\Gamma$  corresponds to a unitary operator acting on the Hilbert space  $\mathcal{H}$ , through the so-called metaplectic representation. Such a unitary operator is generated by terms of the second order in the field operators [19]. In what follows we will refer to a transformation  $S_{l} = \oplus S_{i}$  with each  $S_{i} \in Sp_{(2,\mathbb{R})}$  acting on  $\Gamma_i$ , as to a "local symplectic operation." The corresponding unitary transformation is the "local unitary transformation"  $U_{l} = \otimes U_{i}$ , with each  $U_{i}$  acting on  $\mathcal{H}_i$ .

The Wigner function of a Gaussian state can be written as follows in terms of phase space quadrature variables:

$$
W (X) = \frac {\mathrm {e} ^ {- X \boldsymbol {\sigma} ^ {- 1} X ^ {T} / 2}}{\pi \sqrt {\operatorname {D e t} \boldsymbol {\sigma}}}, \tag {3}
$$

where  $X$  stands for the vector  $(x_{1},p_{1},\dots,x_{n},p_{n})\in \Gamma$

Finally let us recall that, due to Williamson theorem [21], the covariance matrix of an  $n$ -mode Gaussian state can always be written as [18]

$$
\boldsymbol {\sigma} = S ^ {T} \boldsymbol {\nu} S, \tag {4}
$$

where  $S\in Sp_{(2n,\mathbb{R})}$  and  $\pmb{\nu}$  is the covariance matrix,

$$
\boldsymbol {\nu} = \operatorname {d i a g} \left(\nu_ {1}, \nu_ {1}, \dots , \nu_ {n}, \nu_ {n}\right), \tag {5}
$$

corresponding to a tensor product of thermal states with diagonal density matrix  $\varrho^{\otimes}$  given by

$$
Q ^ {\otimes} = \otimes_ {i} \frac {2}{\nu_ {i} + 1} \sum_ {k = 0} ^ {\infty} \left(\frac {\nu_ {i} - 1}{\nu_ {i} + 1}\right) | k \rangle_ {i i} \langle k |, \tag {6}
$$

$\left|k\right\rangle_{i}$  being the  $k$ th number state of the Fock space  $\mathcal{H}_i$ . The dual (Hilbert-space) formulation of Eq. (4) then reads  $\varrho = U^{\dagger}\varrho^{\otimes}U$ , for some unitary  $U$ .

The quantities  $\nu_{i}$ 's form the symplectic spectrum of the covariance matrix  $\pmb{\sigma}$  and can be computed as the eigenvalues of the matrix  $|i\pmb{\Omega}\pmb{\sigma}|$ . Such eigenvalues are in fact invariant under the action of symplectic transformations on the matrix  $\pmb{\sigma}$ .

The symplectic eigenvalues  $\nu_{i}$  encode essential information on the Gaussian state  $\pmb{\sigma}$  and provide powerful, simple ways to express its fundamental properties. For instance, let

us consider the Heisenberg uncertainty relation (2). Since  $S$  is symplectic, one has  $S^{-17}\pmb {\Omega}S^{-1} = \pmb{\Omega}$ , so that inequality (2) is equivalent to  $\pmb {\nu} + i\pmb {\Omega}\geqslant 0$ . In terms of the symplectic eigenvalues  $\nu_{i}$  the uncertainty relation then simply reads

$$
\nu_ {i} \geqslant 1. \tag {7}
$$

We can, without loss of generality, rearrange the modes of an  $n$ -mode state such that the corresponding symplectic eigenvalues are sorted in ascending order:

$$
\nu_ {1} \leqslant \nu_ {2} \leqslant \dots \leqslant \nu_ {n - 1} \leqslant \nu_ {n}.
$$

With this notation, the uncertainty relation reduces to  $\nu_{1} \geqslant 1$ . We remark that the full saturation of Heisenberg uncertainty principle can only be achieved by pure  $n$ -mode Gaussian states, for which  $\nu_{i} = 1 \forall i = 1, \dots, n$ . Instead, mixed states such that  $\nu_{i \leqslant k} = 1$  and  $\nu_{i > k} > 1$ , with  $1 \leqslant k \leqslant n$ , only partially saturate the uncertainty principle, with partial saturation becoming weaker with decreasing  $k$ . Such states are minimum uncertainty mixed Gaussian states in the sense that the phase quadrature operators of the first  $k$  modes satisfy the Heisenberg minimal uncertainty, while for the remaining  $n - k$  modes the state indeed contains some additional thermal and/or Schrödinger-like correlations which are responsible for the global mixedness of the state.

# Two-mode states

In the present work we will mainly deal with two-mode Gaussian states. Here, we will thus briefly review their relevant properties and specify some further notations.

The expression of the two-mode covariance matrix  $\pmb{\sigma}$  in terms of the three  $2\times 2$  matrices  $\alpha ,\beta$  and  $\gamma$  will be useful:

$$
\boldsymbol {\sigma} \equiv \left( \begin{array}{c c} \boldsymbol {\alpha} & \gamma \\ \boldsymbol {\gamma} ^ {T} & \boldsymbol {\beta} \end{array} \right). \tag {8}
$$

It is well known that for any two-mode covariance matrix  $\pmb{\sigma}$  there exists a local symplectic operation  $S_{l} = S_{1}\oplus S_{2}$  which takes  $\pmb{\sigma}$  to the so-called standard form  $\pmb{\sigma}_{sf}$  [22,23]:

$$
S _ {l} ^ {T} \boldsymbol {\sigma} S _ {l} = \boldsymbol {\sigma} _ {s f} \equiv \left( \begin{array}{c c c c} a & 0 & c _ {+} & 0 \\ 0 & a & 0 & c _ {-} \\ c _ {+} & 0 & b & 0 \\ 0 & c _ {-} & 0 & b \end{array} \right). \tag {9}
$$

States whose standard form fulfills  $a = b$  are said to be symmetric. Let us recall that any pure state is symmetric and fulfills  $c_{+} = -c_{-} = \sqrt{a^{2} - 1}$ . The correlations  $a, b, c_{+}$ , and  $c_{-}$  are determined by the four local symplectic invariants  $\operatorname{Det}\pmb{\sigma} = (ab - c_{+}^{2})(ab - c_{-}^{2})$ ,  $\operatorname{Det}\pmb{\alpha} = a^{2}$ ,  $\operatorname{Det}\pmb{\beta} = b^{2}$ , and  $\operatorname{Det}\pmb{\gamma} = c_{+}c_{-}$ . Therefore, the standard form corresponding to any covariance matrix is unique.

The uncertainty principle, inequality (2), can be recast as a constraint on the  $Sp_{(4,\mathbb{R})}$  invariants Det  $\pmb{\sigma}$  and  $\Delta (\pmb {\sigma})$ $= \mathrm{Det}\alpha +\mathrm{Det}\beta +2$  Det  $\gamma$

$$
\Delta (\boldsymbol {\sigma}) \leqslant 1 + \operatorname {D e t} \boldsymbol {\sigma}. \tag {10}
$$

Let us mention that, as is evident from Eq. (9), the condition  $\pmb{\sigma} \geqslant 0$  implies

$$
a b - c _ {\mp} ^ {2} \geqslant 0. \tag {11}
$$

The symplectic eigenvalues of a two-mode Gaussian state will be named  $\nu_{-}$  and  $\nu_{+}$ , with  $\nu_{-} \leqslant \nu_{+}$  in general. With such an ordering, the Heisenberg uncertainty relation, Eq. (7), becomes

$$
\nu_ {\mp} \geqslant 1. \tag {12}
$$

Full saturation  $\nu_{-} = \nu_{+} = 1$  yields the standard pure Gaussian states of Heisenberg minimum uncertainty; partial saturation  $\nu_{-} = 1, \nu_{+} > 1$  defines the minimum-uncertainty mixed Gaussian states. A simple expression for the  $\nu_{+}$  can be found in terms of the two  $Sp_{(4,\mathbb{R})}$  invariants [24,25]

$$
2 \nu_ {+} ^ {2} = \Delta (\boldsymbol {\sigma}) \bar {+} \sqrt {\Delta (\boldsymbol {\sigma}) ^ {2} - 4 \operatorname {D e t} \boldsymbol {\sigma}}. \tag {13}
$$

In turn, Eq. (13) yields immediately

$$
\Delta (\boldsymbol {\sigma}) = \nu_ {-} ^ {2} + \nu_ {+} ^ {2}. \tag {14}
$$

A subclass of Gaussian states that will play a relevant role in the following is constituted by the nonsymmetric two-mode squeezed thermal states. Let  $S_{r} = \exp (1 / 2ra_{1}a_{2} - 1 / 2ra_{1}^{\dagger}a_{2}^{\dagger})$  be the two-mode squeezing operator with real squeezing parameter  $r$ , and let  $\varrho_{\nu_i}^{\otimes}$  be a tensor product of thermal states with covariance matrix  $\pmb{\nu}_{\nu_{\mp}} = \mathbb{1}_2\nu_{-}\oplus \mathbb{1}_2\nu_{+}$  where  $\nu_{\mp}$  is, as usual, the symplectic spectrum of the state. Then, a nonsymmetric two-mode squeezed thermal state  $\xi_{\nu_i,r}$  is defined as  $\xi_{\nu_i,r} = S_r\varrho_{\nu_i}^{\otimes}S_r^{\dagger}$ , corresponding to a standard form with

$$
a = \nu_ {-} \cosh^ {2} r + \nu_ {+} \sinh^ {2} r,
$$

$$
b = \nu_ {-} \sinh^ {2} r + \nu_ {+} \cosh^ {2} r,
$$

$$
c _ {\pm} = \pm \frac {\nu_ {-} + \nu_ {+}}{2} \sinh 2 r. \tag {15}
$$

We mention that the peculiar entanglement properties of squeezed nonsymmetric thermal states have been recently analyzed [26]. In the symmetric instance (with  $\nu_{-} = \nu_{+} = \nu$ ) these states reduce to two-mode squeezed thermal states. The covariance matrices of these states are symmetric standard forms with

$$
a = \nu \cosh 2 r, \quad c _ {\pm} = \pm \nu \sinh 2 r. \tag {16}
$$

In the pure case, for which  $\nu = 1$ , one recovers the two-mode squeezed vacua. Notice that such states encompass all the standard forms associated to pure states: any two-mode Gaussian state can be reduced to a squeezed vacuum by means of unitary local operations.

Two-mode squeezed states (both thermal and pure) are endowed with remarkable properties related to entanglement [27-29]. Even the ideal, perfectly correlated original EPR state [30] can be seen indeed as a two-mode squeezed vacuum in the limit of infinite squeezing parameter  $r$ . The dynamical properties of the entanglement and the characterization of the decoherence of such states have been addressed in detail in several works [31]. We will also show, as a by-product of the present work, the peculiar role they play as maximally entangled Gaussian states.

# III. MEASURES OF MIXEDNESS, DEGREE OF COHERENCE, AND ENTROPIC MEASURES

The degree of mixedness of a quantum state  $\varrho$  can be characterized completely by the knowledge of all the associated Schatten  $p$  norms [32]

$$
\left\| \varrho \right\| _ {p} \equiv (\operatorname {T r} | \varrho | ^ {p}) ^ {1 / p} = (\operatorname {T r} \varrho^ {p}) ^ {1 / p}, \quad \text {w i t h} p \geqslant 1. \tag {17}
$$

In particular, the case  $p = 2$  is directly related to the purity  $\mu = \mathrm{Tr} \varrho^2 = (\| \varrho \|_2)^2$  [33]. The  $p$  norms are multiplicative on tensor product states and thus determine a family of "generalized entropies"  $S_p$  [34,35], defined as

$$
S _ {p} = \frac {1 - \operatorname {T r} \varrho^ {p}}{p - 1}, p > 1. \tag {18}
$$

These quantities have been introduced independently by Bastiaans in the context of quantum optics [34] and by Tsallis in the context of statistical mechanics [35]. In the quantum arena, they can be interpreted both as quantifiers of the degree of mixedness of a state  $\varrho$  by the amount of information it lacks and as measures of the overall degree of coherence of the state (the latter meaning was elucidated by Bastiaans in his analysis of the properties of partially coherent light). The quantity  $S_{2} = 1 - \mu \equiv S_{L}$ , conjugate to the purity  $\mu$ , is usually referred to as the linear entropy: it is a particularly important measure of mixedness, essentially because of the simplicity of its analytical expressions, which will become soon manifest. Finally, another important class of entropic measures includes the Rényi entropies [36]

$$
S _ {p} ^ {R} = \frac {\ln \operatorname {T r} \varrho^ {p}}{1 - p}, \quad p > 1. \tag {19}
$$

It can be easily shown that

$$
\lim  _ {p \rightarrow 1 +} S _ {p} = \lim  _ {p \rightarrow 1 +} S _ {p} ^ {R} = - \operatorname {T r} (\varrho \ln \varrho) \equiv S _ {V}, \tag {20}
$$

so that also the Shannon-von Neumann entropy  $S_V$  can be defined in terms of  $p$  norms. The quantity  $S_V$  is additive on tensor product states and provides a further convenient measure of mixedness of the quantum state  $\varrho$ .

It is easily seen that the generalized entropies  $S_{p}$ 's range from 0 for pure states to  $1 / (p - 1)$  for completely mixed states with fully degenerate eigenspectra. Notice that  $S_{V}$  is infinite on infinitely mixed states, while  $S_{L}$  is normalized to 1. We also mention that, in the asymptotic limit of arbitrary large  $p$ , the function  $\mathrm{Tr}\varrho^{p}$  becomes a function only of the largest eigenvalue of  $\varrho$ : more and more information about the state is discarded in such an estimate for the degree of purity; considering  $S_{p}$  in the limit  $p\to \infty$  yields a trivial constant null function, with no information at all about the state under examination. We also note that, for any given quantum state,  $S_{p}$  is a monotonically decreasing function of  $p$ .

Because of their unitarily invariant nature, the generalized purities  $\mathrm{Tr}\varrho^p$  of generic  $n$ -mode Gaussian states can be simply computed in terms of the symplectic eigenvalues  $\nu_{i}$  of  $\sigma$ . In fact, a symplectic transformation acting on  $\sigma$  is embodied by a unitary (trace preserving) operator acting on  $\varrho$ , so that  $\mathrm{Tr}\varrho^p$  can be easily computed on the diagonal state  $\nu$ . One obtains

$$
\operatorname {T r} \varrho^ {p} = \prod_ {i = 1} ^ {n} g _ {p} \left(\nu_ {i}\right), \tag {21}
$$

where

$$
g _ {p} (x) = \frac {2 ^ {p}}{(x + 1) ^ {p} - (x - 1) ^ {p}}.
$$

A first consequence of Eq. (21) is that

$$
\mu (\varrho) = \frac {1}{\prod v _ {i}} = \frac {1}{\sqrt {\operatorname {D e t} \boldsymbol {\sigma}}}. \tag {22}
$$

Regardless of the number of modes, the purity of a Gaussian state is fully determined by the symplectic invariant Det  $\sigma$  alone. A second consequence of Eq. (21) is that, together with Eqs. (18) and (20), it allows for the computation of the von Neumann entropy  $S_V$  of a Gaussian state  $\varrho$ , yielding

$$
S _ {V} (\varrho) = \sum_ {i = 1} ^ {n} f \left(\nu_ {i}\right), \tag {23}
$$

where

$$
f (x) \equiv \frac {x + 1}{2} \ln \left(\frac {x + 1}{2}\right) - \frac {x - 1}{2} \ln \left(\frac {x - 1}{2}\right).
$$

Such an expression for the von Neumann entropy of a Gaussian state was first explicitly given in Ref. [37]. Let us remark that, clearly, the symplectic spectrum of single-mode Gaussian states, which consists of only one eigenvalue  $\nu_{1}$ , is fully determined by the invariant  $\mathrm{Det} \sigma = \nu_{1}^{2}$ . Therefore, all the entropies  $S_{p}$ 's (and  $S_{V}$  as well) are just increasing functions of  $\mathrm{Det} \sigma$  (i.e., of  $S_{L}$ ) and induce the same hierarchy of mixedness on the set of one-mode Gaussian states. This is no longer true for multi mode states, even for the relevant, simple instance of two-mode states.

Here we aim to find extremal values of  $S_{p}$  (for  $p \neq 2$ ) for fixed  $S_{L}$  in the general  $n$ -mode Gaussian instance, in order to quantitatively compare the characterization of mixedness given by the different entropic measures. For simplicity, in calculations we will replace  $S_{L}$  with  $\mu$ . In view of Eqs. (21) and (22), the possible values taken by  $S_{p}$  for a given  $\mu$  are determined by

$$
(p - 1) S _ {p} = 1 - \left(\prod_ {i = 1} ^ {n - 1} g _ {p} \left(s _ {i}\right)\right) g _ {p} \left(\frac {1}{\prod_ {i = 1} ^ {n - 1} s _ {i}}\right), \tag {24}
$$

$$
\text {w i t h} \quad 1 \leqslant s _ {i} \leqslant \frac {1}{\mu \prod_ {i \neq j} s _ {j}}. \tag {25}
$$

The last constraint on the  $n - 1$  real auxiliary parameters  $s_i$  is a consequence of the uncertainty relation (7). We first focus on the instance  $p < 2$ , in which the function  $S_{p}$  is concave with respect to any  $s_i$ , for any value of the  $s_i$ 's. Therefore its minimum with respect to, say,  $s_{n - 1}$  occurs at the boundaries of the domain, for  $s_{n - 1}$  saturating inequality (25). Since  $S_{p}$

takes the same value at the two extrema and exploiting  $g_{p}(1) = 1$ , one has

$$
(p - 1) \min  _ {s _ {n - 1}} S _ {p} = 1 - \left(\prod_ {i = 1} ^ {n - 2} g _ {p} \left(s _ {i}\right)\right) g _ {p} \left(\frac {1}{\mu \prod_ {i = 1} ^ {n - 2} s _ {i}}\right). \tag {26}
$$

Iterating this procedure for all the  $s_i$ 's leads eventually to the minimum value  $S_{p\min}(\mu)$  of  $S_p$  at given purity  $\mu$ , which simply reads

$$
S _ {p \min } (\mu) = \frac {1 - g _ {p} \left(\frac {1}{\mu}\right)}{p - 1}, \quad p <   2. \tag {27}
$$

For  $p < 2$ , the mixedness of the states with minimal generalized entropies at given purity is therefore concentrated in one quadrature: the symplectic spectrum of such states is partially degenerate, with  $\nu_{1} = \dots = \nu_{n - 1} = 1$  and  $\nu_{n} = 1 / \mu$ .

The maximum value  $S_{p\max}(\mu)$  is achieved by states satisfying the coupled trascendental equations

$$
g _ {p} \left(\frac {1}{\mu \prod s _ {i}}\right) g _ {p} ^ {\prime} (s _ {j}) = \frac {1}{\mu s _ {j} \prod s _ {i}} g _ {p} (s _ {j}) g _ {p} ^ {\prime} \left(\frac {1}{\mu \prod s _ {i}}\right), \tag {28}
$$

where all the products  $\Pi$  run over the index  $i$  from 1 to  $n - 1$  and

$$
g _ {p} ^ {\prime} (x) = \frac {- p 2 ^ {p} \left[ (x + 1) ^ {p - 1} - (x - 1) ^ {p - 1} \right]}{\left[ (x + 1) ^ {p} - (x - 1) ^ {p} \right] ^ {2}}. \tag {29}
$$

It is promptly verified that the above two conditions are fulfilled by states with a completely degenerate symplectic spectrum:  $\nu_{1} = \dots = \nu_{n} = \mu^{-1 / n}$ , yielding

$$
S _ {p \max } (\mu) = \frac {1 - g _ {p} \left(\mu^ {- 1 / n}\right) ^ {n}}{p - 1}, \quad p <   2. \tag {30}
$$

The analysis that we carried out for  $p < 2$  can be straightforwardly extended to the limit  $p \to 1$ , yielding the extremal values of the von Neumann entropy for given purity  $\mu$  of  $n$ -mode Gaussian states. Also in this case the states with maximal  $S_V$  are those with a completely degenerate symplectic spectrum, while the states with minimal  $S_V$  are those with all the mixedness concentrated in one quadrature. The extremal values  $S_{V\min}(\mu)$  and  $S_{V\max}(\mu)$  read

$$
S _ {V \min } (\mu) = f \left(\frac {1}{\mu}\right), \tag {31}
$$

$$
S _ {V \max } (\mu) = n f \left(\mu^ {- 1 / n}\right). \tag {32}
$$

The behaviors of the von Neumann and of the linear entropies for two-mode states are compared in Fig. 1.

The instance  $p > 2$  can be treated in the same way, with the major difference that the function  $S_{p}$  of Eq. (24) is convex with respect to any  $s_{i}$  for any value of the  $s_{i}$ 's. As a consequence we have an inversion of the previous expressions: for  $p > 2$ , the states with minimal  $S_{p\min}(\mu)$  at given purity  $\mu$  are those with a fully distributed symplectic spectrum, with

![](images/e9f946dc40a1c37a26e7fd1720787a6023173a5a47c351b48f65f18699a46390.jpg)  
FIG. 1. Plot of the curves (solid lines) of maximal and minimal von Neumann entropy at given linear entropy for two-mode Gaussian states. The density of states in the plane of entropies is represented as well, by plotting the distribution of 20 000 randomly generated states (dots).

$$
S _ {p \min } (\mu) = \frac {1 - g _ {p} \left(\mu^ {- 1 / n}\right) ^ {n}}{p - 1}, \quad p > 2. \tag {33}
$$

On the other hand, the states with maximal  $S_{p\max}$  at given purity  $\mu$  are those with a spectrum of the kind  $\nu_{1} = \dots = \nu_{n - 1} = 1$  and  $\nu_{n} = 1 / \mu$ . Therefore,

$$
S _ {p \max } (\mu) = \frac {1 - g _ {p} \left(\frac {1}{\mu}\right)}{p - 1}, \quad p > 2. \tag {34}
$$

As shown in Fig. 2, the distance  $\left| S_{p\max} - S_{p\min} \right|$  decreases with increasing  $p$ . This is due to the fact that the quantity  $S_{p}$  carries less information with increasing  $p$ , and the knowledge of  $\mu$  provides a more precise bound on the value of  $S_{p}$ .

# IV. MEASURES OF ENTANGLEMENT

We now review the main aspects of entanglement for CV systems and discuss some of the possible quantifications of quantum correlations for Gaussian states.

The necessary and sufficient separability criterion for a two-mode Gaussian state  $\varrho$  has been shown to be positivity

![](images/3c8e2c7999f51ba4bd8af0e2fe7421180400d97e75681d3f7885134d314cb9ba.jpg)  
FIG. 2. Plot of the absolute difference between the maximal and the minimal values of the generalized entropies  $S_{p}$  at fixed linear entropy  $S_{L}$  for two-mode Gaussian states, as a function of  $p$ . Different curves correspond to different values of the linear entropy:  $S_{L} = 0.8$  (dashed line),  $S_{L} = 0.5$  (solid line), and  $S_{L} = 0.1$  (dash-dotted line).

of the partially transposed state  $\widetilde{\varrho}$  (PPT criterion) [22]. In general, the partial transposition  $\widetilde{\varrho}$  of a bipartite quantum state  $\varrho$  is defined as the result of the transposition performed on only one of the two subsystems in some given basis. Even though the resulting  $\widetilde{\varrho}$  does depend on the choice of the transposed subsystem and on the transposition basis, the statement  $\widetilde{\varrho} \geqslant 0$  is geometric and is invariant under such choices [38]. It can be easily seen from the definition of  $W(X)$  that the action of partial transposition amounts, in phase space, to a mirror reflection of one of the four canonical variables. In terms of  $Sp_{(2,\mathbb{R})} \oplus Sp_{(2,\mathbb{R})}$  invariants, this reduces to a sign flip in Det  $\gamma$ :

$$
\operatorname {D e t} \gamma \stackrel {\varrho \rightarrow \tilde {\varrho}} {\to} - \operatorname {D e t} \gamma .
$$

Therefore the invariant  $\Delta (\pmb {\sigma})$  is changed into  $\widetilde{\Delta} (\pmb {\sigma}) = \Delta (\widetilde{\pmb{\sigma}})$ $= \mathrm{Det}\alpha +\mathrm{Det}\beta -2\mathrm{Det}\gamma .$  Now, the symplectic eigenvalues  $\tilde{\nu}_{+}$  of  $\tilde{\pmb{\sigma}}$  read

$$
\widetilde {\nu} _ {+} = \sqrt {\frac {\widetilde {\Delta} (\boldsymbol {\sigma}) \mp \sqrt {\widetilde {\Delta} (\boldsymbol {\sigma}) ^ {2} - 4 \operatorname {D e t} \boldsymbol {\sigma}}}{2}}. \tag {35}
$$

The PPT criterion thus reduces to a simple inequality that must be satisfied by the smallest symplectic eigenvalue  $\widetilde{\nu}_{-}$  of the partially transposed state:

$$
\tilde {\nu} _ {-} \geqslant 1, \tag {36}
$$

which is equivalent to

$$
\tilde {\Delta} (\boldsymbol {\sigma}) \leqslant \operatorname {D e t} \boldsymbol {\sigma} + 1. \tag {37}
$$

The above inequalities imply  $\operatorname{Det} \gamma = c_{+}c_{-} < 0$  as a necessary condition for a two-mode Gaussian state to be entangled. The quantity  $\widetilde{\nu}_{-}$ encodes all the qualitative characterization of the entanglement for arbitrary (pure or mixed) two-mode Gaussian states. Note that  $\widetilde{\nu}_{-}$ takes a particularly simple form for entangled symmetric states, whose standard form has  $a = b$ :

$$
\tilde {\nu} _ {-} = \sqrt {\left(a - \left| c _ {+} \right|\right) \left(a - \left| c _ {-} \right|\right)}. \tag {38}
$$

Inserting Eqs. (15) into Eq. (37) yields the following condition for a two-mode squeezed thermal state  $\xi_{\nu_i,r}$  to be entangled:

$$
\sinh^ {2} (2 r) > \frac {\left(v _ {+} ^ {2} - 1\right) \left(v _ {-} ^ {2} - 1\right)}{\left(v _ {-} + v _ {+}\right) ^ {2}}. \tag {39}
$$

As for the quantification of entanglement, no fully satisfactory measure is known at present for arbitrary mixed bipartite Gaussian states. However, a quantification of entanglement which can be computed for general Gaussian states is provided by the negativity  $\mathcal{N}$ , first introduced in Ref. [39], later thoroughly discussed and extended in Ref. [24] to CV systems. The negativity of a quantum state  $\varrho$  is defined as

$$
\mathcal {N} (\varrho) = \frac {\left\| \widetilde {\varrho} \right\| _ {1} - 1}{2}, \tag {40}
$$

where  $\widetilde{\varrho}$  is the partially transposed density matrix and  $\| \hat{o}\| _1$ $= \mathrm{Tr}|\hat{o} |$  stands for the Schatten 1-norm (the so-called "trace

norm") of the Hermitian operator  $\hat{o}$ . The quantity  $\mathcal{N}(\varrho)$  is equal to  $|\Sigma_i\lambda_i|$ , the modulus of the sum of the negative eigenvalues of  $\widetilde{\varrho}$ , quantifying the extent to which  $\widetilde{\varrho}$  fails to be positive. Strictly related to  $\mathcal{N}$  is the logarithmic negativity  $E_{\mathcal{N}}$ , defined as  $E_{\mathcal{N}}\equiv \ln \| \widetilde{\varrho}\| _1$ , which constitutes an upper bound to the distillable entanglement of the quantum state  $\varrho$ .

The negativity has been proven to be convex and monotone under local operations and classical communications (LOCC) [40], but fails to be continuous in trace norm on infinite-dimensional Hilbert spaces. However, this problem can be circumvented by restricting to physical states with finite mean energy [14].

We will now show that for any two-mode Gaussian state  $\varrho$  the negativity is a simple decreasing function of  $\widetilde{\nu}_{-}$ , which is thus itself an entanglement monotone. The norm  $\|\cdot\|_{1}$  is unitarily invariant; in particular, it is invariant under global symplectic operations in phase space. Considering the symplectic diagonalization  $\widetilde{\pmb{\nu}} \equiv \mathrm{diag}(\widetilde{\nu}_{-}, \widetilde{\nu}_{-}, \widetilde{\nu}_{+}, \widetilde{\nu}_{+})$  of  $\widetilde{\sigma}$ , this means that  $\mathcal{N}(\varrho) = (\|\widetilde{\pmb{\nu}}\|_{1} - 1)/2$ . Now, because of the multiplicativity of the norm  $\|\cdot\|_{1}$ , we have just to compute the trace of the single-mode thermal-like operator  $\rho_{\widetilde{\nu}_i}^{\otimes}$ :

$$
\rho_ {\widetilde {\nu} _ {i}} ^ {\otimes} = \frac {2}{\widetilde {\nu} _ {i} + 1} \sum_ {k = 0} ^ {\infty} \left(\frac {\widetilde {\nu} _ {i} - 1}{\widetilde {\nu} _ {i} + 1}\right) ^ {k} | k \rangle \langle k |.
$$

Such an operator is obviously normalized for  $\widetilde{\nu}_i\geqslant 1$ , yielding  $\| \rho_{\widetilde{\nu}_i}^{\otimes}\| _1 = 1$  (all eigenvalues are positive). Instead, if  $\widetilde{\nu}_i < 1$ , then  $\| \rho_{\widetilde{\nu}_i}^{\otimes}\| _1 = 1 / \widetilde{\nu}_i$ . The proof is completed by showing that the largest symplectic eigenvalue  $\widetilde{\nu}_{+}$  of  $\widetilde{\sigma}$  fulfills  $\widetilde{\nu}_{+}\geqslant 1$ . This is obviously true for separable states; therefore, we can set  $c_{+}c_{-} < 0$ . With this position, it is easy to show that

$$
\tilde {\nu} _ {+} > \nu_ {-} \geqslant 1.
$$

Thus, we obtain  $\| \rho_{\widetilde{\nu}_{+}}^{\otimes}\|_{1} = 1$  and

$$
\left\| \tilde {\varrho} \right\| _ {1} = \frac {1}{\tilde {\nu} _ {-}} \Rightarrow \mathcal {N} (\varrho) = \max  \left[ 0, \frac {1 - \tilde {\nu} _ {-}}{2 \tilde {\nu} _ {-}} \right], \tag {41}
$$

$$
E _ {\mathcal {N}} (\varrho) = \max  [ 0, - \ln \tilde {\nu} _ {-} ]. \tag {42}
$$

This is a decreasing function of the smallest partially transposed symplectic eigenvalue  $\widetilde{\nu}_{-}$ , quantifying the amount by which inequality (36) is violated. The eigenvalue  $\widetilde{\nu}_{-}$  thus completely qualifies and quantifies the quantum entanglement of a Gaussian state  $\sigma$ . Notice that, in such an instance, this feature holds for nonsymmetric states as well.

We finally mention that, as far as symmetric states are concerned, another measure of entanglement, the entanglement of formation  $E_{F}$  [41], can be actually computed [28]. Since  $E_{F}$  turns out to be, again, a decreasing function of  $\tilde{\nu}_{-}$ , it provides for symmetric states a quantification of entanglement fully equivalent to the one provided by the logarithmic negativity  $E_{\mathcal{N}}$ .

# V. SYMPLECTIC EIGENVALUES AND EPR CORRELATIONS

A deeper insight on the relationship between correlations and the eigenvalue  $\widetilde{\nu}_{-}$  is provided by the following observation, which holds in the symmetric case.

Let us define the EPR correlation  $\xi$  [28,29] of a continuous variable two-mode quantum state as

$$
\xi \equiv \frac {\delta_ {\hat {x} _ {1} - \hat {x} _ {2}} + \delta_ {\hat {p} _ {1} + \hat {p} _ {2}}}{2} = \frac {\operatorname {T r} \boldsymbol {\sigma}}{2} - \sigma_ {1 3} + \sigma_ {2 4}, \tag {43}
$$

where  $\delta_{\hat{o}} = \langle \hat{o}^2\rangle -\langle \hat{o}\rangle^2$  for an operator  $\hat{o}$ . If  $\xi \geqslant 1$ , then the state does not possess nonlocal correlations. The idealized EPR-like state [30] (simultaneous eigenstate of the commuting observables  $\hat{x}_1 - \hat{x}_2$  and  $\hat{p}_1 + \hat{p}_2$ ) has  $\xi = 0$ . As for standard form states, one has

$$
\delta_ {\hat {x} _ {1} - \hat {x} _ {2}} = a + b - 2 c _ {+}, \tag {44}
$$

$$
\delta_ {\hat {p} _ {1} + \hat {p} _ {2}} = a + b + 2 c _ {-}, \tag {45}
$$

$$
\xi = a + b - c _ {+} + c _ {-}. \tag {46}
$$

Notice that  $\xi$  is not by itself a good measure of correlation because, as one can easily verify, it is not invariant under local symplectic operations. In particular, applying local squeezings with parameters  $r_i = \ln v_i$  and local rotations with angles  $\varphi_i$  to a standard form state, we obtain

$$
\xi_ {v _ {i}, \vartheta} = \frac {a}{2} \left(v _ {1} ^ {2} + \frac {1}{v _ {1} ^ {2}}\right) + \frac {b}{2} \left(v _ {2} ^ {2} + \frac {1}{v _ {2} ^ {2}}\right) - \left(c _ {+} v _ {1} v _ {2} - \frac {c _ {-}}{v _ {1} v _ {2}}\right) \cos \vartheta , \tag {47}
$$

with  $\vartheta = \varphi_{1} + \varphi_{2}$ . Now, the quantity

$$
\bar {\xi} \equiv \min  _ {v _ {i}, \vartheta} \xi_ {v _ {i}, \vartheta}
$$

has to be  $Sp_{(2,\mathbb{R})}\oplus Sp_{(2,\mathbb{R})}$  invariant. It corresponds to the maximal amount of EPR correlations which can be distributed in a two-mode Gaussian state by means of local operations. Minimization in terms of  $\vartheta$  is immediate, yielding  $\overline{\xi} = \min_{v_i}\xi_{v_i}$ , with

$$
\xi_ {v _ {i}} = \frac {a}{2} \left(v _ {1} ^ {2} + \frac {1}{v _ {1} ^ {2}}\right) + \frac {b}{2} \left(v _ {2} ^ {2} + \frac {1}{v _ {2} ^ {2}}\right) - \left| c _ {+} v _ {1} v _ {2} - \frac {c _ {-}}{v _ {1} v _ {2}} \right|. \tag {48}
$$

The gradient of such a quantity is null if and only if

$$
a \left(v _ {1} ^ {2} - \frac {1}{v _ {1} ^ {2}}\right) - \left| c _ {+} \right| v _ {1} v _ {2} - \frac {\left| c _ {-} \right|}{v _ {1} v _ {2}} = 0, \tag {49}
$$

$$
b \left(v _ {2} ^ {2} - \frac {1}{v _ {2} ^ {2}}\right) - \left| c _ {+} \right| v _ {1} v _ {2} - \frac {\left| c _ {-} \right|}{v _ {1} v _ {2}} = 0, \tag {50}
$$

where we introduced the position  $c_{+}c_{-} < 0$ , necessary to have entanglement. Equations (49) and (50) can be combined to get

$$
a \left(v _ {1} ^ {2} - \frac {1}{v _ {1} ^ {2}}\right) = b \left(v _ {2} ^ {2} - \frac {1}{v _ {2} ^ {2}}\right). \tag {51}
$$

Restricting to the symmetric  $(a = b)$  entangled  $(\Rightarrow c_{+}c_{-} < 0)$  case, Eq. (51) and the fact that  $v_{i} > 0$  imply  $v_{1} = v_{2}$ . Under such a constraint, minimizing  $\xi_{v_i}$  becomes a trivial matter and yields

$$
\bar {\xi} = 2 \sqrt {\left(a - \left| c _ {+} \right|\right) \left(a - \left| c _ {-} \right|\right)} = 2 \tilde {\nu} _ {-}. \tag {52}
$$

We thus see that the smallest symplectic eigenvalue of the partially transposed state is endowed with a direct physical interpretation: it quantifies the greatest amount of EPR correlations which can be created in a Gaussian state by means of local operations.

As can be easily shown by a numerical analysis, such a simple interpretation is lost for nonsymmetric states. This fact properly exemplifies the difficulties of handling optimization problems in nonsymmetric instances, encountered, e.g., in the computation of the entanglement of formation of such states.

# VI. PARAMETRIZATION OF GAUSSIAN STATES WITH SYMPLECTIC INVARIANTS

Two-mode Gaussian states can be classified according to the values of their four  $Sp_{(2,\mathbb{R})}\oplus Sp_{(2,\mathbb{R})}$  invariants  $a,b,c_{+}$  and  $c_{-}$ , which determine their standard form. It is relevant to provide a reparametrization of standard form states in terms of invariants which admit a direct interpretation for generic Gaussian states. Such invariants will be the global purity  $\mu = \mathrm{Tr}\varrho^2$ , the marginal purities of the reduced states  $\mu_{i} = \mathrm{Tr}_{i}[(\mathrm{Tr}_{j\neq i}\varrho)^{2}]$ , and the  $Sp_{(4,\mathbb{R})}$  invariant  $\Delta$ , whose meaning will become soon clear. For a two-mode Gaussian state one has

$$
\mu_ {1} = \frac {1}{a}, \quad \mu_ {2} = \frac {1}{b}, \tag {53}
$$

$$
\frac {1}{\mu^ {2}} = \operatorname {D e t} \boldsymbol {\sigma} = (a b) ^ {2} - a b \left(c _ {+} ^ {2} + c _ {-} ^ {2}\right) + \left(c _ {+} c _ {-}\right) ^ {2}, \tag {54}
$$

$$
\Delta = a ^ {2} + b ^ {2} + 2 c _ {+} c _ {-}. \tag {55}
$$

Equations (53)-(55) can be inverted to provide the parametrization

$$
a = \frac {1}{\mu_ {1}}, \quad b = \frac {1}{\mu_ {2}}, \tag {56}
$$

$$
c _ {\pm} = \frac {1}{4} \sqrt {\mu_ {1} \mu_ {2} \left[ \left(\Delta - \frac {\left(\mu_ {1} - \mu_ {2}\right) ^ {2}}{\mu_ {1} ^ {2} \mu_ {2} ^ {2}}\right) ^ {2} - \frac {4}{\mu^ {2}} \right]} \pm \epsilon , \tag {57}
$$

with

$$
\epsilon \equiv \frac {1}{4} \sqrt {\frac {[ (\mu_ {1} + \mu_ {2}) ^ {2} - \mu_ {1} ^ {2} \mu_ {2} ^ {2} \Delta ] ^ {2}}{\mu_ {1} ^ {3} \mu_ {2} ^ {3}} - \frac {4 \mu_ {1} \mu_ {2}}{\mu^ {2}}}.
$$

The global and marginal purities range from 0 to 1, constrained by the condition

$$
\mu \geqslant \mu_ {1} \mu_ {2}, \tag {58}
$$

which can be easily shown to be a direct consequence of inequality (11). Notice that inequality (58) entails that no Gaussian less pure than product (LPTP) states exist, at variance with the case of two-qubit systems [6].

The smallest symplectic eigenvalues of the covariance matrix  $\pmb{\sigma}$  and of its partial transpose  $\tilde{\pmb{\sigma}}$  are promptly determined in terms of symplectic invariants

$$
2 \nu_ {-} ^ {2} = \Delta - \sqrt {\Delta^ {2} - \frac {4}{\mu^ {2}}}, \quad 2 \tilde {\nu} _ {-} ^ {2} = \tilde {\Delta} - \sqrt {\tilde {\Delta} ^ {2} - \frac {4}{\mu^ {2}}}, \tag {59}
$$

where  $\widetilde{\Delta} = -\Delta +2 / \mu_1^2 +2 / \mu_2^2$

The parametrization provided by Eqs. (56) and (57) describes physical states if the radicals in Eqs. (57) and (59) exist and the Heisenberg uncertainty principle (7) is satisfied. All these conditions can be combined and recast as upper and lower bounds on the global symplectic invariant  $\Delta$ :

$$
\frac {2}{\mu} + \frac {\left(\mu_ {1} - \mu_ {2}\right) ^ {2}}{\mu_ {1} ^ {2} \mu_ {2} ^ {2}} \leqslant \Delta \leqslant \min  \left\{\frac {\left(\mu_ {1} + \mu_ {2}\right) ^ {2}}{\mu_ {1} ^ {2} \mu_ {2} ^ {2}} - \frac {2}{\mu}, 1 + \frac {1}{\mu^ {2}} \right\}. \tag {60}
$$

Let us investigate the role played by the invariant  $\Delta$  in the characterization of the properties of Gaussian states. To this aim, we just analyze the dependence of the eigenvalue  $\widetilde{\nu}_{-}$  on  $\Delta$ :

$$
\left. \frac {\partial \tilde {\nu} _ {-} ^ {2}}{\partial \Delta} \right| _ {\mu_ {1}, \mu_ {2}, \mu} = \frac {1}{2} \left(\frac {\tilde {\Delta}}{\sqrt {\tilde {\Delta} ^ {2} - \frac {1}{4 \mu^ {2}}}} - 1\right) > 0. \tag {61}
$$

The smallest symplectic eigenvalue of the partially transposed state is strictly monotone in  $\Delta$ . Therefore the entanglement of a generic Gaussian state  $\sigma$  with global purity  $\mu$  and marginal purities  $\mu_{1,2}$  strictly increases with decreasing  $\Delta$ . The invariant  $\Delta$  is thus endowed with a direct physical interpretation: at given global and marginal purities, it determines the amount of entanglement of the state.

Because, due to inequality (60),  $\Delta$  possess both lower and upper bounds, not only maximally but also minimally entangled Gaussian states exist. This elucidates the relations between the entanglement and the purity of two-mode Gaussian states: the entanglement of such states is tightly bound by the amount of global and marginal purities, with only one remaining degree of freedom related to the invariant  $\Delta$ .

# VII. EXTREMAL ENTANGLEMENT AT FIXED GLOBAL AND LOCAL PURITIES

We now aim to characterize extremal (maximally and minimally) entangled Gaussian states for fixed global and marginal purities. As is clear from Eq. (53), the standard form of states with fixed marginal purities always satisfies  $a = 1 / \mu_1, b = 1 / \mu_2$ . Therefore the complete characterization of maximally and minimally entangled states is achieved by specifying the expression of their standard form coefficients  $c_{\mp}$ .

Let us first consider the states saturating the lower bound in Eq. (60), which entails maximal entanglement. They are Gaussian maximally entangled states for fixed global and local purities (GMEMS), admitting the parametrization

$$
c _ {\pm} = \pm \sqrt {\frac {1}{\mu_ {1} \mu_ {2}} - \frac {1}{\mu}}. \tag {62}
$$

It is easily seen that such states belong to the class of asymmetric two-mode squeezed thermal state, with squeezing parameter and symplectic spectrum given by

$$
\tanh 2 r = 2 \left(\mu_ {1} \mu_ {2} - \mu_ {1} ^ {2} \mu_ {2} ^ {2} / \mu\right) ^ {1 / 2} / \left(\mu_ {1} + \mu_ {2}\right), \tag {63}
$$

$$
\nu_ {+} ^ {2} = \frac {1}{\mu} + \frac {\left(\mu_ {1} - \mu_ {2}\right) ^ {2}}{2 \mu_ {1} ^ {2} \mu_ {2} ^ {2}} \neq \frac {\left| \mu_ {1} - \mu_ {2} \right|}{2 \mu_ {1} \mu_ {2}} \sqrt {\frac {\left(\mu_ {1} - \mu_ {2}\right) ^ {2}}{\mu_ {1} ^ {2} \mu_ {2} ^ {2}} + \frac {4}{\mu}}. \tag {64}
$$

In particular, any GMEMS can be written as an entangled two-mode squeezed thermal states [satisfying inequality (39)]. This provides a characterization of two-mode thermal squeezed states as maximally entangled states for given global and marginal purities. We can restate this result as follows: given an initial tensor product of (generally different) thermal states, the unitary operation providing the maximal entanglement for given values of the local purities  $\mu_{i}$ 's is given by a two-mode squeezing, with squeezing parameter determined by Eq. (63). Notice that fixing the values of the local purities is necessary to attain maximal, finite entanglement; in fact, fixing only the value of the global purity  $\mu$  always allows for an arbitrary large logarithmic negativity (as  $\tilde{\nu}_{-}$  goes to 0), achievable by means of two-mode squeezing with arbitrary large squeezing parameter.

Nonsymmetric two-mode thermal squeezed states turn out to be separable in the range

$$
\mu \leqslant \frac {\mu_ {1} \mu_ {2}}{\mu_ {1} + \mu_ {2} - \mu_ {1} \mu_ {2}}. \tag {65}
$$

In such a separable region in the space of purities, no entanglement can occur for states of the form of Eq. (62), while, outside this region, they are properly GMEMS. We remark that, as a consequence, all Gaussian states whose purities fall in the separable region defined by inequality (65) are separable.

We now consider the states that saturate the upper bound in Eq. (60). They determine the class of Gaussian least entangled states for given global and local purities (GLEMS). Violation of inequality (65) implies that

$$
1 + \frac {1}{\mu^ {2}} \leqslant \frac {\left(\mu_ {1} + \mu_ {2}\right) ^ {2}}{\mu_ {1} ^ {2} \mu_ {2} ^ {2}} - \frac {2}{\mu}.
$$

Therefore, outside the separable region, GLEMS fulfill

$$
\Delta = 1 + \frac {1}{\mu^ {2}}. \tag {66}
$$

Equation (66) expresses partial saturation of Heisenberg relation, Eq. (12). Namely, considering the symplectic diagonalization of Gaussian states and Eq. (14), it immediately

follows that the  $Sp_{(4,\mathbb{R})}$  invariant condition (66) is fulfilled if and only if the symplectic spectrum of the state takes the form  $\nu_{-} = 1, \nu_{+} = 1 / \mu$ . We thus find that GLEMS are characterized by a peculiar spectrum, with all the mixedness con

centrated in one "decoupled" quadrature. Moreover, by Eqs. (66) and (12) it follows that GLEMS are minimum-uncertainty mixed Gaussian states. They are determined by the standard form correlation coefficients

$$
c _ {\pm} = \frac {1}{4} \sqrt {\mu_ {1} \mu_ {2} \left[ - \frac {4}{\mu^ {2}} + \left(1 + \frac {1}{\mu^ {2}} - \frac {\left(\mu_ {1} - \mu_ {2}\right) ^ {2}}{\mu_ {1} ^ {2} \mu_ {2} ^ {2}}\right) ^ {2} \right]} \pm \frac {1}{4 \mu} \sqrt {- 4 \mu_ {1} \mu_ {2} + \frac {\left[ (1 + \mu^ {2}) \mu_ {1} ^ {2} \mu_ {2} ^ {2} - \mu^ {2} \left(\mu_ {1} + \mu_ {2}\right) ^ {2} \right] ^ {2}}{\mu^ {2} \mu_ {1} ^ {3} \mu_ {2} ^ {3}}}. \tag {67}
$$

Quite remarkably, following the analysis presented in Sec. III, it turns out that the GLEMS at fixed global and marginal purities are also states of minimal global  $p$  entropy for  $p < 2$  and of maximal global  $p$  entropy for  $p > 2$ .

According to the PPT criterion, GLEMS are separable only if  $\mu \leqslant \mu_1\mu_2 / \sqrt{\mu_1^2 + \mu_2^2 - \mu_1^2\mu_2^2}$ . Therefore, in the range

$$
\frac {\mu_ {1} \mu_ {2}}{\mu_ {1} + \mu_ {2} - \mu_ {1} \mu_ {2}} <   \mu \leqslant \frac {\mu_ {1} \mu_ {2}}{\sqrt {\mu_ {1} ^ {2} + \mu_ {2} ^ {2} - \mu_ {1} ^ {2} \mu_ {2} ^ {2}}}, \tag {68}
$$

both separable and entangled states can be found. Instead, the region

$$
\mu > \frac {\mu_ {1} \mu_ {2}}{\sqrt {\mu_ {1} ^ {2} + \mu_ {2} ^ {2} - \mu_ {1} ^ {2} \mu_ {2} ^ {2}}} \tag {69}
$$

can only accommodate entangled states.

The very narrow region defined by inequality (68) is thus the only region of coexistence of both entangled and separable Gaussian mixed states. We mention that the sufficient condition for entanglement (69), first derived in Ref. [13], has been independently rediscovered in another recent work [17].

The upper and lower inequalities (60) lead to the following further constraint between the global and the local purities:

$$
\mu \leqslant \frac {\mu_ {1} \mu_ {2}}{\mu_ {1} \mu_ {2} + | \mu_ {1} - \mu_ {2} |}. \tag {70}
$$

For purities which saturate inequality (70), one obtains the states of maximal global purity with given marginal purities.

![](images/6b97454da3277c45649a5966e16df7e5157e66eca722011e28a20f6aaeffa39d.jpg)  
FIG. 3. Plot of the maximal logarithmic negativity of Gaussian states for fixed marginal purities. The surface represents GMEMMS, states that saturate inequality (70).

In such an instance GMEMS and GLEMS coincide and we have a unique class of entangled states depending only on the marginal purities  $\mu_{1,2}$ . They are Gaussian maximally entangled states for fixed marginals (GMEMMS). In Fig. 3 the logarithmic negativity of GMEMMS is plotted as a function of  $\mu_{1,2}$ , showing how the maximal entanglement achievable by Gaussian states rapidly decreases with increasing difference of marginal purities, in analogy with finite-dimensional systems [6]. For symmetric states  $(\mu_1 = \mu_2)$  inequality (70) reduces to the trivial bound  $\mu \leqslant 1$  and GMEMMS reduce to pure two-mode squeezed vacua.

The previous necessary or sufficient conditions for entanglement are collected in Table I and allow a graphical display of the behavior of the entanglement of mixed Gaussian states as shown in Fig. 4. These relations classify the properties of separability of all two-mode Gaussian states according to their degree of global and marginal purities.

# Realization of extremely entangled states in experimental settings

As we have seen, GMEMS are two-mode squeezed thermal states, whose general covariance matrix is described by Eqs. (9) and (15). A realistic instance giving rise to such states is provided by the dissipative evolution of an initially pure two-mode squeezed vacuum created, e.g., in a nondegenerate parametric downconversion process. Let us denote by  $\sigma_r$  the covariance matrix of a two-mode squeezed vacuum with squeezing parameter  $r$ , derived from Eqs. (15)

TABLE I. Classification of two-mode Gaussian states and of their properties of separability according to their degrees of global purity  $\mu$  and of marginal purities  $\mu_{1}$  and  $\mu_{2}$ .  

<table><tr><td>Degrees of purity</td><td>Separability</td></tr><tr><td>μ&lt;μ1μ2</td><td>unphysical region</td></tr><tr><td>μ1μ2≤μ≤μ1μ2/(μ1+μ2-μ1μ2)</td><td>separable states</td></tr><tr><td>μ1μ2/(μ1+μ2-μ1μ2)&lt;μ</td><td>coexistence region</td></tr><tr><td>≤μ1μ2/√μ12+μ22-μ12μ2</td><td></td></tr><tr><td>μ1μ2/√μ12+μ22-μ12μ2&lt;μ</td><td>entangled states</td></tr><tr><td>≤μ1μ2/(μ1μ2+|μ1-μ2|)</td><td></td></tr><tr><td>μ&gt;μ1μ2/(μ1μ2+|μ1-μ2|)</td><td>unphysical region</td></tr></table>

![](images/9a20a9b3c006952940c8ca1e422bf70b18457807934fe3dd4ce25aa67df5d617.jpg)  
FIG. 4. Summary of entanglement properties of two-mode (non-symmetric) Gaussian states in the space of marginal purities  $\mu_{1,2}$  ( $x$  and  $y$  axes) and global purity  $\mu$ . In fact, on the  $z$  axis we plot the ratio  $\mu / \mu_1 \mu_2$  to gain a better graphical distinction between the various regions. In this space, all physical states lie between the horizontal plane  $z = 1$  representing product states and the upper limiting surface representing GMEMMS. Separable and entangled states are well separated except for a narrow region of coexistence (depicted in black). Separable states fill the region depicted in dark gray, while in the region containing only entangled states we have depicted the average logarithmic negativity, Eq. (88), growing from white to medium gray. The mathematical relations defining the boundaries between all these regions are collected in Table I. The three-dimensional envelope is cut at  $z = 3.5$ .

with  $\nu_{\mp} = 1$ . The interaction of this initial state with a thermal noise results in the following dynamical map describing the time evolution of the covariance matrix  $\pmb{\sigma}(t)$  [31]:

$$
\boldsymbol {\sigma} (t) = \mathrm {e} ^ {- \Gamma t} \boldsymbol {\sigma} _ {r} + \left(1 - \mathrm {e} ^ {- \Gamma t}\right) \boldsymbol {\sigma} _ {n _ {1}, n _ {2}}, \tag {71}
$$

where  $\Gamma$  is the coupling to the noisy reservoir (equal to the inverse of the damping time) and  $\pmb{\sigma}_{n_1,n_2} = \oplus_{i=1}^{2} n_i \mathbb{1}_2$  is the covariance matrix of the thermal noise. The average number of thermal photons  $n_i$  given by

$$
n _ {i} = \frac {1}{\exp (\hbar \omega_ {i} / k _ {B} T) - 1}
$$

in terms of the frequencies of the modes  $\omega_{i}$  and of the temperature of the reservoir  $T$ . It can be easily verified that the covariance matrix, Eq. (71), defines a two-mode thermal squeezed state, generally nonsymmetric (for  $n_1 \neq n_2$ ). However, notice that the entanglement of such a state cannot persist indefinitely, because after a given time inequality (39) will be violated and the state will evolve into a nonentangled two-mode squeezed thermal state. We also notice that the relevant instance of pure loss  $(n_1 = n_2 = 0)$  allows the realization of symmetric GMEMS.

Concerning the experimental characterization of minimally entangled states, one can envisage several explicit experimental settings for their realization. For instance, let us consider (see Fig. 5) a beam splitter with transmittivity  $\tau = 1 / 2$  (corresponding to a two-mode rotation of angle  $\pi /4$  in phase space). Suppose that a single-mode squeezed state, with covariance matrix  $\pmb{\sigma}_{1r} = \mathrm{diag}\left(\mathrm{e}^{2r},\mathrm{e}^{-2r}\right)$  (like, e.g., the result of a degenerate parametric downconversion in a non

![](images/a87e4d7cec12f86ebd286095fd7bb7f2b1b058f23b946d1e85c0ad5c5eb544cf.jpg)  
FIG. 5. Possible scheme for the generation of Gaussian least-entangled mixed states (GLEMS). A single-mode squeezed state (obtained, for example, by an optical parametric oscillator or amplifier) interferes with a thermal state through a 50:50 beam splitter. The resulting two-mode state is a minimally entangled mixed Gaussian state at given global and marginal purities.

linear crystal), enters in the first input of the beam splitter. Let the other input be an incoherent thermal state produced from a source at equilibrium at a temperature  $T$ . The purity  $\mu$  of such a state can be easily computed in terms of the temperature  $T$  and of the frequency of the thermal mode  $\omega$ :

$$
\mu = \frac {\exp \left(\hbar \omega / k _ {B} T\right) - 1}{\exp \left(\hbar \omega / k _ {B} T\right) + 1}. \tag {72}
$$

The state at the output of the beam splitter will be a correlated two-mode Gaussian state with covariance matrix  $\pmb{\sigma}_{\mathrm{out}}$  which reads

$$
\boldsymbol {\sigma} _ {\mathrm {o u t}} = \frac {1}{2} \left( \begin{array}{c c c c} n + k & 0 & n - k & 0 \\ 0 & n + k ^ {- 1} & 0 & n - k ^ {- 1} \\ n - k & 0 & n + k & 0 \\ 0 & n - k ^ {- 1} & 0 & n + k ^ {- 1} \end{array} \right),
$$

with  $k = \mathrm{e}^{2r}$  and  $n = \mu^{-1}$ . By immediate inspection, the symplectic spectrum of this covariance matrix is  $\nu_{-} = 1$  and  $\nu_{+} = 1 / \mu$ . Therefore the output state is always a state with extremal generalized entropy at a given purity (the state can be seen as the tensor product of a vacuum and of a thermal state, on which one has applied symplectic transformation). Moreover, the state is entangled if

$$
\cosh (2 r) > \frac {\mu^ {2} + 1}{2 \mu} = \frac {\exp \left(2 \hbar \omega / k _ {B} T\right) + 1}{\exp \left(2 \hbar \omega / k _ {B} T\right) - 1}. \tag {73}
$$

Tuning the experimental parameters to meet the above condition, indeed makes the output state of the beam splitter a symmetric GLEMS. It is interesting to observe that nonsymmetric GLEMS can be produced as well by choosing a beam splitter with transmissivity different from 0.5.

# VIII. EXTREMAL ENTANGLEMENT AT FIXED GLOBAL AND LOCAL GENERALIZED ENTROPIES

In this section we introduce a more general characterization of the entanglement of generic two-mode Gaussian states, by exploiting the generalized  $p$  entropies as measures of global and marginal mixedness. For ease of comparison we will carry out this analysis along the same lines followed

in the previous section by studying the explicit behavior of the global invariant  $\Delta$ , directly related to the logarithmic negativity  $E_{\mathcal{N}}$  at fixed global and marginal entropies. This study will clarify the relation between  $\Delta$  and the generalized entropies  $S_{p}$  and the ensuing consequences for the entanglement of Gaussian states.

We begin by observing that the standard form covariance matrix  $\sigma$  of a generic two-mode Gaussian state can be parametrized by the following quantities: the two marginals  $\mu_{1,2}$  (or any other marginal  $S_{p1,2}$  because all the local, single-mode entropies are equivalent for any value of the integer  $p$ ), the global  $p$  entropy  $S_{p}$  (for some chosen value of the integer  $p$ ), and the global symplectic invariant  $\Delta$ . On the other hand, Eqs. (18), (21), and (13) provide an explicit expression for any  $S_{p}$  as a function of  $\mu$  and  $\Delta$ . Such an expression can be exploited to study the behavior of  $\Delta$  as a function of the global purity  $\mu$ , at fixed marginals and global  $S_{p}$  (from now on we will omit the explicit reference to fixed marginals). One has

$$
\left. \frac {\partial \mu}{\partial \Delta} \right| _ {S _ {p}} = - \frac {2}{R ^ {2}} \frac {\partial R}{\partial \Delta} \Bigg | _ {S _ {p}} = \frac {2}{R ^ {2}} \frac {\partial S _ {p} / \partial \Delta | _ {R}}{\partial S _ {p} / \partial R | _ {\Delta}} = \frac {2}{R ^ {2}} \frac {N _ {p} (\Delta , R)}{D _ {p} (\Delta , R)}, \tag {74}
$$

where we have defined the inverse participation ratio

$$
R \equiv \frac {2}{\mu}, \tag {75}
$$

and the remaining quantities  $N_{p}$  and  $D_{p}$  read

$$
\begin{array}{l} N _ {p} (\Delta , R) = \left[ (R + 2 + 2 \sqrt {\Delta + R}) ^ {p - 1} - (R + 2 \right. \\ - 2 \sqrt {\Delta + R}) ^ {p - 1} ] \sqrt {\Delta - R} - \left[ (R - 2 + 2 \sqrt {\Delta - R}) ^ {p - 1} \right. \\ \left. - (R - 2 - 2 \sqrt {\Delta - R}) ^ {p - 1} \right] \sqrt {\Delta + R}, \\ \end{array}
$$

$$
\begin{array}{l} D _ {p} (\Delta , R) = \left[ \left(\sqrt {\Delta + R} + 1\right) (R + 2 + 2 \sqrt {\Delta + R}) ^ {p - 1} + \left(\sqrt {\Delta + R} - 1\right) \right. \\ \times (R + 2 - 2 \sqrt {\Delta + R}) ^ {p - 1} ] \sqrt {\Delta - R} - [ (\sqrt {\Delta - R} + 1) \\ \times (R - 2 - 2 \sqrt {\Delta - R}) ^ {p - 1} + (\sqrt {\Delta - R} - 1) (R - 2 \\ \left. + 2 \sqrt {\Delta - R}\right) ^ {p - 1} ] \sqrt {\Delta + R}. \tag {76} \\ \end{array}
$$

Now, it is easily shown that the ratio  $N_{p}(\Delta, R) / D_{p}(\Delta, R)$  is increasing with increasing  $p$  and has a zero at  $p = 2$  for any  $\Delta, R$ ; in particular, its absolute minimum  $(-1)$  is reached in the limit  $(\Delta \to 2, R \to 2, p \to 1)$ . Thus the derivative, Eq. (74), is negative for  $p < 2$ , null for  $p = 2$  (in this case  $\Delta$  and  $S_{2} = 1 - \mu$  are of course regarded as independent variables), and positive for  $p > 2$ . This implies that, for given marginals, keeping fixed any global  $S_{p}$  for  $p < 2$  the minimum (maximum) value of  $\Delta$  corresponds to the maximum (minimum) value of the global purity  $\mu$ . Instead, by keeping fixed any global  $S_{p}$  for  $p > 2$  the minimum of  $\Delta$  is always attained at the minimum of the global purity  $\mu$ .

This observation allows us to determine rather straightforwardly the states with extremal  $\Delta$ . They are extremely entangled states because, for fixed global and marginal entropies, the logarithmic negativity of a state is determined only by the one remaining independent global symplectic invari

ant, represented by  $\Delta$  in our choice of parametrization. If, for the moment being, we neglect the fixed local purities, then the states with maximal  $\Delta$  are the states with minimal (maximal)  $\mu$  for a given global  $S_{p}$  with  $p < 2$  ( $p > 2$ ) (see Sec. III and Fig. 1). As found in Sec. III, such states are minimum uncertainty two-mode states with mixedness concentrated in one quadrature. We have shown in Sec. VII that they correspond to Gaussian least-entangled mixed states (GLEMS) whose standard form is given by Eq. (67). As can be seen from Eq. (67), these states are consistent with any legitimate physical value of the local invariants  $\mu_{1,2}$ . We therefore conclude that all Gaussian states with maximal  $\Delta$  for any fixed triple of values of global and marginal entropies are GLEMS.

Vice versa one can show that all Gaussian states with minimal  $\Delta$  for any fixed triple of values of global and marginal entropies are Gaussian maximally entangled mixed states (GMEMS). This fact is immediately evident in the symmetric case because the extremal surface in the  $S_{p}$  vs  $S_{L}$  diagrams is always represented by symmetric two-mode squeezed states (symmetric GMEMS). These states are characterized by a degenerate symplectic spectrum and encompass only equal choices of the local invariants:  $\mu_1 = \mu_2$ . In the nonsymmetric case, the given values of the local entropies are different, and the extremal value of  $\Delta$  is further constrained by inequality (60):

$$
\Delta - R \geqslant \frac {\left(\mu_ {1} - \mu_ {2}\right) ^ {2}}{\mu_ {1} ^ {2} \mu_ {2} ^ {2}}. \tag {77}
$$

From Eq. (74) it follows that

$$
\left. \frac {\partial (\Delta - R)}{\partial \Delta} \right| _ {S _ {p}, \mu_ {1, 2}} = 1 + \frac {N _ {p} (\Delta , R)}{D _ {p} (\Delta , R)} \geqslant 0, \tag {78}
$$

because  $N_{p}(\Delta, R) / D_{p}(\Delta, R) > -1$ . Thus,  $\Delta - R$  is an increasing function of  $\Delta$  at fixed  $\mu_{1,2}$  and  $S_{p}$ , and the minimal  $\Delta$  corresponds to the minimum of  $\Delta - R$ , which occurs if inequality (77) is saturated. Therefore, also in the nonsymmetric case, the two-mode Gaussian states with minimal  $\Delta$  at fixed global and marginal entropies are GMEMS.

Summing up, we have shown that GMEMS and GLEMS introduced in the previous section at fixed global and marginal linear entropies, are always extremely entangled Gaussian states, whatever triple of generalized global and marginal entropic measures one chooses to fix. Maximally and minimally entangled states of CV systems are thus very robust with respect to the choice of different measures of mixedness. This is at striking variance with the case of discrete variable systems, where it has been shown that fixing different measures of mixedness yields different classes of maximally entangled states [4].

Furthermore, we will now show that the characterization provided by the generalized entropies leads to some remarkable insight into the behavior of the entanglement of CV systems. The crucial observation is that for a generic  $p$ , the smallest symplectic eigenvalue of the partially transposed covariance matrix, at fixed global and marginal  $p$  entropies, is not in general a monotone function of  $\Delta$ , so that the connection between extremal  $\Delta$  and extremal entanglement turns out to be, in some cases, inverted. In particular, while for

$p < 2$  the GMEMS and GLEMS surfaces tend to be more separated as  $p$  decreases, for  $p > 2$  the two classes of extremely entangled states get closer with increasing  $p$  and, within a particular range of global and marginal entropies, they exchange their role. GMEMS (i.e., states with minimal  $\Delta$ ) become minimally entangled states and GLEMS (i.e., states with maximal  $\Delta$ ) become maximally entangled states. This inversion always occurs for all  $p > 2$ .

To understand this interesting behavior, let us study the dependence of the symplectic eigenvalue  $\widetilde{\nu}_{-}$  on the global invariant  $\Delta$  at fixed marginals and at fixed  $S_{p}$  for a generic  $p$ . Using Maxwell's relations, we can write

$$
\kappa_ {p} \equiv \left. \frac {\partial (2 \widetilde {\nu} _ {-} ^ {2})}{\partial \Delta} \right| _ {S _ {p}} = \left. \frac {\partial (2 \widetilde {\nu} _ {-} ^ {2})}{\partial \Delta} \right| _ {R} - \left. \frac {\partial (2 \widetilde {\nu} _ {-} ^ {2})}{\partial R} \right| _ {\Delta} \frac {\partial S _ {p} / \partial \Delta | _ {R}}{\partial S _ {p} / \partial R | _ {\Delta}}. \tag {79}
$$

Clearly, for  $\kappa_{p} > 0$  GMEMS and GLEMS retain their usual interpretation, whereas for  $\kappa_{p} < 0$  they exchange their role. On the node  $\kappa_{p} = 0$  GMEMS and GLEMS share the same entanglement; i.e., the entanglement of all Gaussian states at  $\kappa_{p} = 0$  is fully determined by the global and marginal  $p$  entropies alone and does not depend any more on  $\Delta$ . Such nodes also exist in the case  $p \leqslant 2$  in two limiting instances: in the special case of GMEMS (states with maximal global purity at fixed marginals) and in the limit of zero marginal purities. We will now show that, besides these two limiting behaviors, a nontrivial node appears for all  $p > 2$ , implying that on the two sides of the node GMEMS and GLEMS indeed exhibit opposite behaviors. Because of Eq. (74),  $\kappa_{p}$  can be written in the form

$$
\kappa_ {p} = \kappa_ {2} - \frac {R}{\sqrt {\tilde {\Delta} ^ {2} - R ^ {2}}} \frac {N _ {p} (\Delta , R)}{D _ {p} (\Delta , R)}, \tag {80}
$$

with  $N_{p}$  and  $D_{p}$  defined by Eq. (76) and

$$
\widetilde {\Delta} = - \Delta + \frac {2}{\mu_ {1} ^ {2}} + \frac {2}{\mu_ {2} ^ {2}},
$$

$$
\kappa_ {2} = - 1 + \frac {\widetilde {\Delta}}{\sqrt {\widetilde {\Delta} ^ {2} - R ^ {2}}}.
$$

The quantity  $\kappa_{p}$  in Eq. (80) is a function of  $p,R,\Delta$ , and of the marginals; since we are looking for the node (where the entanglement is independent of  $\Delta$ ), we can investigate the existence of a nontrivial solution to the equation  $\kappa_{p} = 0$  fixing any value of  $\Delta$ . Let us choose  $\Delta = 1 + R^2 /4$  that saturates the Heisenberg uncertainty relation and is satisfied by GLEMS. With this position, Eq. (80) becomes

$$
\begin{array}{l} \kappa_ {p} (\mu_ {1}, \mu_ {2}, R) = \kappa_ {2} (\mu_ {1}, \mu_ {2}, R) \\ - \frac {R}{\sqrt {\left(2 / \mu_ {1} ^ {2} + 2 / \mu_ {2} ^ {2} - R ^ {2} / 4 - 1\right) ^ {2} - R ^ {2}}} f _ {p} (R). \tag {81} \\ \end{array}
$$

The existence of the node depends then on the behavior of the function

$$
f _ {p} (R) \equiv \frac {2 [ (R + 2) ^ {p - 2} - (R - 2) ^ {p - 2} ]}{(R + 4) (R + 2) ^ {p - 2} - (R - 4) (R - 2) ^ {p - 2}}. \tag {82}
$$

In fact, as we have already pointed out,  $\kappa_{2}$  is always positive, while the function  $f_{p}(R)$  is an increasing function of  $p$  and, in particular, it is negative for  $p < 2$ , null for  $p = 2$ , and positive for  $p > 2$ , reaching its asymptote  $2 / (R + 4)$  in the limit  $p \to \infty$ . This entails that, for  $p \leqslant 2$ ,  $\kappa_{p}$  is always positive, which in turn implies that GMEMS and GLEMS are, respectively, maximally and minimally entangled two-mode states with fixed marginal and global  $p$  entropies in the range  $p \leqslant 2$  (including both von Neumann and linear entropies). On the other hand, for any  $p > 2$  one node can be found solving the equation  $\kappa_{p}(\mu_{1}, \mu_{2}, 2 / \mu) = 0$ . The solutions to this equation can be found analytically for low  $p$  and numerically for any  $p$ . They form a continuum in the space  $\{\mu_{1}, \mu_{2}, \mu\}$  which can be expressed as a surface of general equation  $\mu = \mu_{p}^{\kappa}(\mu_{1}, \mu_{2})$ . Since the fixed variable is  $S_{p}$  and not  $\mu$ , it is convenient to rewrite the equation of this surface in the space  $\varepsilon_{p} \equiv \{\mu_{1}, \mu_{2}, S_{p}\}$ , keeping in mind the relation (34), holding for GLEMS, between  $\mu$  and  $S_{p}$ . In this way the nodal surface  $(\kappa_{p} = 0)$  can be written in the form

$$
S _ {p} = S _ {p} ^ {\kappa} \left(\mu_ {1}, \mu_ {2}\right) \equiv \frac {1 - g _ {p} \left\{\left[ \mu_ {p} ^ {\kappa} \left(\mu_ {1} , \mu_ {2}\right) \right] ^ {- 1} \right\}}{p - 1}. \tag {83}
$$

The entanglement of all Gaussian states whose entropies lie on the surface  $S_{p}^{\kappa}(\mu_{1},\mu_{2})$  is completely determined by the knowledge of  $\mu_1,\mu_2$  , and  $S_{p}$  . The explicit expression of the function  $\mu_p^\kappa (\mu_1,\mu_2)$  depends on  $p$  , but being the global purity of physical states, is constrained by the inequality

$$
\mu_ {1} \mu_ {2} \leqslant \mu_ {p} ^ {\kappa} (\mu_ {1}, \mu_ {2}) \leqslant \frac {\mu_ {1} \mu_ {2}}{\mu_ {1} \mu_ {2} + | \mu_ {1} - \mu_ {2} |}.
$$

The nodal surface of Eq. (83) constitutes a "leaf," with base at the point  $\mu_p^\kappa(0,0) = 0$  and tip at the point  $\mu_p^\kappa(\sqrt{3}/2, \sqrt{3}/2) = 1$ , for any  $p > 2$ ; such a leaf becomes larger and flatter with increasing  $p$  (see Fig. 6). For  $p > 2$ , the function  $f_p(R)$  defined by Eq. (82) is negative but decreasing with increasing  $R$ —that is, with decreasing  $\mu$ . This means that, in the space of entropies  $\varepsilon_p$ , above the leaf  $(S_p > S_p^\kappa)$  GMEMS (GLEMS) are still maximally (minimally) entangled states for fixed global and marginal generalized entropies, while below the leaf they are inverted. Notice also that for  $\mu_{1,2} > \sqrt{3}/2$  no node and so no inversion can occur for any  $p$ . Each point on the leaf-shaped surface of Eq. (83) corresponds to an entire class of infinitely many two-mode Gaussian states (including GMEMS and GLEMS) with the same marginals and the same global  $S_p = S_p^\kappa(\mu_1, \mu_2)$ , which are all equally entangled, since their logarithmic negativity is completely determined by  $\mu_1, \mu_2$ , and  $S_p$ . For the sake of clarity we provide the explicit expressions of  $\mu_p^\kappa(\mu_1, \mu_2)$ , as plotted in Fig. 6 for the cases (a)  $p = 3$  and (b)  $p = 4$ :

$$
\mu_ {3} ^ {\kappa} \left(\mu_ {1}, \mu_ {2}\right) = \left(\frac {6}{3 / \mu_ {1} ^ {2} + 3 / \mu_ {1} ^ {2} - 2}\right) ^ {1 / 2}, \tag {84}
$$

![](images/e395e2dfa10d38299be4f090a5de1f9cb72b97e4109e21769e953cf6ad9ab537.jpg)

![](images/021e09b9dc0e3a2af818199765a7c370bea86255be485b3a27f732a38db5b664.jpg)  
FIG. 6. Plot of the nodal surface which solves the equation  $\kappa_{p} = 0$  with  $\kappa_{p}$  defined by Eq. (80), for (a)  $p = 3$  and (b)  $p = 4$ . The entanglement of Gaussian states that lie on the leaf-shaped surfaces is fully quantified in terms of the marginal purities and the global generalized entropy (a)  $S_{3}$  or (b)  $S_{4}$ . The equations of the surfaces in the space  $\varepsilon_{p} \equiv \{\mu_{1}, \mu_{2}, S_{p}\}$  are given by Eqs. (83)-(85).

$$
\begin{array}{l} \mu_ {4} ^ {\kappa} \left(\mu_ {1}, \mu_ {2}\right) = \sqrt {3} \mu_ {1} \mu_ {2} / \left(\mu_ {1} ^ {2} + \mu_ {2} ^ {2} - 2 \mu_ {1} ^ {2} \mu_ {2} ^ {2} \right. \\ + \sqrt {\left(\mu_ {1} ^ {2} + \mu_ {2} ^ {2}\right) \left(\mu_ {1} ^ {2} + \mu_ {2} ^ {2} - \mu_ {1} ^ {2} \mu_ {2} ^ {2}\right) + \left. \mu_ {1} ^ {4} \mu_ {2} ^ {4}\right) ^ {1 / 2}}. \tag {85} \\ \end{array}
$$

Apart from the relevant "inversion" feature shown by  $p$  entropies for  $p > 2$ , the possibility of an accurate characterization of CV entanglement based on global and marginal entropic measures still holds in the general case for any  $p$ . In particular, the set of all Gaussian states can be again divided, in the space of global and marginal  $S_{p}$ 's, into three main areas: separable, entangled, and coexistence regions. It can be thus very interesting to investigate how the different entropic measures chosen to quantify the degree of global mixedness (all marginal measures are equivalent) behave in classifying the separability properties of Gaussian states. Figure 7 provides a numerical comparison of the different characterizations of entanglement obtained by the use of different  $p$  entropies, with  $p$  ranging from 1 to 4, for symmetric Gaussian states  $(S_{p_1} = S_{p_2} \equiv S_{p_i})$ . The last restriction has been imposed just for ease of graphical display. The following considerations, based on the exact numerical solutions of the transcendental conditions, will take into account nonsymmetric states as well.

The mathematical relations expressing the boundaries between the different regions in Fig. 7 are easily obtained for any  $p$  by starting from the relations holding for  $p = 2$  (see Table I) and by evaluating the corresponding  $S_{p}(\mu_{1,2})$  for each  $\mu (\mu_{1,2})$ . For any physical symmetric state such a calculation yields

$$
0 \leqslant (p - 1) S _ {p} <   1 - g _ {p} \left(\frac {\sqrt {2 - \mu_ {i} ^ {2}}}{\mu_ {i}}\right) \Rightarrow \text {e n t a n g l e d},
$$

$$
\begin{array}{l} 1 - g _ {p} \left(\frac {\sqrt {2 - \mu_ {i} ^ {2}}}{\mu_ {i}}\right) \leqslant (p - 1) S _ {p} <   1 \\ - g _ {p} ^ {2} \left(\sqrt {\frac {2 - \mu_ {i}}{\mu_ {i}}}\right) \Rightarrow \text {c o e x i s t e n c e}, \\ \end{array}
$$

$$
1 - g _ {p} ^ {2} \left(\sqrt {\frac {2 - \mu_ {i}}{\mu_ {i}}}\right) \leqslant (p - 1) S _ {p} \leqslant 1 - g _ {p} ^ {2} \left(\frac {1}{\mu_ {i} ^ {2}}\right) \Rightarrow \text {s e p a r a b l e}. \tag {86}
$$

Equations (86) were obtained exploiting the multiplicativity of  $p$  norms on product states and using Eq. (27) for the lower boundary of the coexistence region (which represents GLEMS becoming entangled) and Eq. (30) for the upper one (which expresses GMEMS becoming separable). Let us mention also that the relation between any local entropic measure  $S_{p_i}$  and the local purity  $\mu_i$  is obtained directly from Eq. (21) and reads

$$
S _ {p _ {i}} = \frac {1 - g _ {p} \left(1 / \mu_ {i}\right)}{p - 1}. \tag {87}
$$

We notice prima facie that, with increasing  $p$ , the entanglement is more sharply qualified in terms of the global and marginal  $p$  entropies. In fact the region of coexistence between separable and entangled states becomes narrower with higher  $p$ . Thus, somehow paradoxically, with increasing  $p$  the entropy  $S_{p}$  provides less information about a quantum state, but at the same time it yields a more accurate characterization and quantification of its entanglement. In the limit  $p\to \infty$  all the physical states collapse to one point at the origin of the axes in the space of generalized entropies, due to the fact that the measure  $S_{\infty}$  is identically zero.

# IX. QUANTIFYING ENTANGLEMENT: THE AVERAGE LOGARITHMIC NEGATIVITY

We have extensively shown that knowledge of the global and marginal generalized  $p$  entropies accurately characterizes the entanglement of Gaussian states, providing strong sufficient or necessary conditions. The present analysis naturally leads us to propose an actual quantification of entanglement, based exclusively on marginal and global entropic measures, enriching and generalizing the approach introduced in Ref. [13].

Outside the separable region, we can formally define the maximal entanglement  $E_{\mathcal{N}\max}(S_{p_{1,2}}, S_p)$  as the logarithmic negativity attained by GMEMS (or GLEMS, below the inversion nodal surface for  $p > 2$ ; see Fig. 6). In a similar way, in the entangled region GLEMS (or GMEMS, below the inversion nodal surface for  $p > 2$ ) achieve the minimal logarithmic negativity  $E_{\mathcal{N}\max}(S_{p_{1,2}}, S_p)$ . The explicit analytical expressions of these quantities are unavailable for any  $p \neq 2$  due to the transcendence of the conditions relating  $S_p$  to the symplectic eigenvalues. The surfaces of maximal and minimal entanglement in the space of the global and local  $S_p$  are plotted in Fig. 8 for symmetric states. In the plane  $S_p = 0$  the upper and lower bounds correctly coincide, since for pure

![](images/d128e90cedc182c3d28c6e1e90ddb6e381f84fe11eef50ea1d2c2aaf925501db.jpg)

![](images/2807c270c81b84522f8d8b77e6a039870aea8dfae1be652622b0f0a5e7a96044.jpg)

![](images/81ab29ef599ac3ebe9a8d584cf956b8fc951b97406ebaa1e4401e4f5822fbbef.jpg)  
FIG. 7. Summary of the entanglement properties for symmetric Gaussian states at fixed global and marginal generalized  $p$  entropies, for (a)  $p = 1$  (von Neumann entropies), (b)  $p = 2$  (linear entropies), (c)  $p = 3$ , and (d)  $p = 4$ . In the entangled region, the average logarithmic negativity  $\overline{E}_{\mathcal{N}}(S_{p_i}, S_p)$ , Eq. (88), is depicted, growing from gray to black. For  $p > 2$  an additional dashed curve is plotted; it represents the nodal line of inversion. Along it the entanglement is fully determined by the knowledge of the global and marginal generalized entropies  $S_{p_i}, S_p$ , and GMEMS and GLEMS are equally entangled. On the left side of the nodal line GMEMS (GLEMS) are maximally (minimally) entangled Gaussian states at fixed  $S_{p_i}, S_p$ . On the right side of the nodal line they are inverted: GMEMS (GLEMS) are minimally (maximally) entangled states. Also notice how the dashed region of coexistence becomes narrower with increasing  $p$ . The equations of all boundary curves can be found in Eq. (86).

![](images/6ce5c1f28c4b095a33496c8d9958ce6282298e5fb48d05554151a156d2ac2c5d.jpg)

states the entanglement is completely quantified by the marginal entropy. For mixed states this is not the case, but as the plot shows, knowledge of the global and marginal entropies strictly bounds the entanglement both from above and from below. For  $p > 2$ , we notice how GMEMS and GLEMS exchange their role beyond a specific curve in the space of  $S_{p}$ 's. The equation of this nodal curve is obtained from the general leaf-shaped nodal surfaces of Eqs. (83)-(85), by imposing the symmetry constraint  $(S_{p_1} = S_{p_2} \equiv S_{p_i})$ . We notice again how the  $S_{p}$ 's with higher  $p$  provide a better characterization of the entanglement, even quantitatively. In fact, the gap between the two extremely entangled surfaces in the  $S_{p}$ 's space becomes smaller with higher  $p$ . Of course the gap is exactly zero all along the nodal line of inversion for  $p > 2$ .

We will now introduce a particularly convenient quantitative estimate of the entanglement based only on the knowl

edge of the global and marginal entropies. Let us define the "average logarithmic negativity"  $\bar{E}_{\mathcal{N}}$  as

$$
\bar {E} _ {\mathcal {N}} \left(S _ {p _ {1, 2}}, S _ {p}\right) \equiv \frac {E _ {\mathcal {N} \max } \left(S _ {p _ {1 , 2}} , S _ {p}\right) + E _ {\mathcal {N} \min } \left(S _ {p _ {1 , 2}} , S _ {p}\right)}{2}. \tag {88}
$$

We will now show that this quantity, fully determined by the global and marginal entropies, provides a reliable quantification of entanglement (logarithmic negativity) for two-mode Gaussian states. To this aim, we define the relative error  $\delta \overline{E}_{\mathcal{N}}$  on  $\overline{E}_{\mathcal{N}}$  as

$$
\delta \bar {E} _ {\mathcal {N}} \left(S _ {p _ {1, 2}}, S _ {p}\right) \equiv \frac {E _ {N \max } \left(S _ {p _ {1 , 2}} , S _ {p}\right) - E _ {N \min } \left(S _ {p _ {1 , 2}} , S _ {p}\right)}{E _ {N \max } \left(S _ {p _ {1 , 2}} , S _ {p}\right) + E _ {N \min } \left(S _ {p _ {1 , 2}} , S _ {p}\right)}. \tag {89}
$$

As Fig. 9 shows, this error decreases exponentially both with

![](images/db1f761441029f305bc6cd1a955eb3576e35c98cb9f6e15bc26061a23358b642.jpg)

![](images/6c9fdd893a443fab184f96b1cda98c4f5b440001c3e0434649816b0a667050a7.jpg)

![](images/7951b1609d732cc2a89e290e828bc95e09c631de40644905995d74fa996c4bf6.jpg)  
FIG. 8. Upper and lower bounds on the logarithmic negativity of symmetric Gaussian states as functions of the global and marginal generalized  $p$  entropies, for (a)  $p = 1$  (von Neumann entropies), (b)  $p = 2$  (linear entropies), (c)  $p = 3$ , and (d)  $p = 4$ . The black (gray) surface represents GMEMS (GLEMS). Notice that for  $p > 2$  GMEMS and GLEMS surfaces intersect along the inversion line (meaning they are equally entangled along that line), and beyond it they interchange their role. The equations of the inversion lines are obtained from Eqs. (83)-(85), with the position  $S_{p_1} = S_{p_2} \equiv S_{p_i}$ .

![](images/6d2335e960563cfbb399a100b8b04290b93cf2e58d18363e55b2ae66b79c6bf1.jpg)

decreasing global entropy and increasing marginal entropies—that is, with increasing entanglement. In general the relative error  $\delta \bar{E}_{\mathcal{N}}$  is "small" for sufficiently entangled states; we will present more precise numerical considerations in the subcase  $p = 2$ . Notice that the decaying rate of the relative error is faster with increasing  $p$ : the average logarithmic negativity turns out to be a better estimate of entanglement with increasing  $p$ . For  $p > 2$ ,  $\delta \bar{E}_{\mathcal{N}}$  is exactly zero on the inversion node; then it becomes finite again and, after reaching a local maximum, it goes asymptotically to zero (see the insets of Fig. 9).

All the above considerations, obtained by an exact numerical analysis, show that the average logarithmic negativity  $\overline{E}_{\mathcal{N}}$  at fixed global and marginal  $p$  entropies is a very good estimate of entanglement in CV systems, whose reliability improves with increasing entanglement and, surprisingly, with increasing order  $p$  of the entropic measures.

# Direct estimate of the entanglement

In the present general framework, a peculiar role is played by the case  $p = 2$  —i.e., by the linear entropy  $S_{L}$  (or, equival

lently, the purity  $\mu$ ). The previous general analysis on the whole range of generalized entropies  $S_{p}$  has remarkably stressed the privileged theoretical role of the instance  $p = 2$  which discriminates between the region in which extremely entangled states are unambiguously characterized and the region in which they can exchange their roles. Moreover, the graphical analysis shows that, in the region where no inversion takes place  $(p \leqslant 2)$ , fixing the global  $S_{2} = 1 - \mu$  yields the most stringent constraints on the logarithmic negativity of the states (see Figs. 7-9). Notice that such constraints, involving no transcendental functions for  $p = 2$ , can be easily handled analytically. A crucial experimental consideration strengthens these theoretical and practical reasons to privilege the role of  $S_{2}$ . In fact,  $S_{2}$  can indeed, assuming some prior knowledge about the state (essentially, its Gaussian character), be measured through conceivable direct methods, in particular by means of single-photon detection schemes [17] or of the upcoming quantum network architectures [42]. No complete homodyne reconstruction of the density matrix is needed in such schemes. Very recently, a first important and promising step in this direction has been realized with the experimental implementation of direct photon detection

![](images/a6f4ec48fb1034ae6be0bc02f950c04398b0f71ceb05ff8733c978c96c9237e9.jpg)

![](images/da68edde1436188b620035bd02b6f027be703885a1fbfb9b95a157a81c0e7bcd.jpg)

![](images/f0753dac7e05167943d0b4a8ef519bae6c4afdc57af192cbe284fac3af039da5.jpg)  
FIG. 9. The relative error  $\delta \overline{E}_{\mathcal{N}}$ , Eq. (89), on the average logarithmic negativity as a function of the ratio  $S_{p_i} / S_p$ , for (a)  $p = 1$ , (b)  $p = 2$ , (c)  $p = 3$ , and (d)  $p = 4$ , plotted at (a)  $S_V = 1$ , (b)  $S_L = 1/2$ , (c)  $S_3 = 1/4$ , and (d)  $S_4 = 1/6$ . Notice how, in general, the error decays exponentially and, in particular, faster with increasing  $p$ . For  $p > 2$ , notice how the error reaches zero on the inversion node (see the insets), then grows and reaches a local maximum before going back to zero asymptotically.

![](images/aa1d9a9399da47fd685d5d326fda27b4bfbc0583f398d3e9aac6bc76076edc9d.jpg)

for the measurement of the squeezing and purity of a single-mode squeezed vacuum with a setup that required only a tunable beam splitter and a single-photon detector [43].

As already anticipated, for  $p = 2$  we can provide analytical expressions for extremal entanglement in the space of global and marginal purities:

$$
\begin{array}{l} E _ {\mathcal {N} \max } (\mu_ {1, 2}, \mu) = - \frac {1}{2} \ln \left[ - \frac {1}{\mu} + \left(\frac {\mu_ {1} + \mu_ {2}}{2 \mu_ {1} ^ {2} \mu_ {2} ^ {2}}\right) \left(\mu_ {1} + \mu_ {2} \right. \right. \\ \left. - \sqrt {(\mu_ {1} + \mu_ {2}) ^ {2} - \frac {4 \mu_ {1} ^ {2} \mu_ {2} ^ {2}}{\mu}}\right) \Bigg ], \tag {90} \\ \end{array}
$$

$$
\begin{array}{l} E _ {\mathcal {N} \min } (\mu_ {1, 2}, \mu) = - \frac {1}{2} \ln \left[ \frac {1}{\mu_ {1} ^ {2}} + \frac {1}{\mu_ {2} ^ {2}} - \frac {1}{2 \mu^ {2}} - \frac {1}{2} \right. \\ \left. - \sqrt {\left(\frac {1}{\mu_ {1} ^ {2}} + \frac {1}{\mu_ {2} ^ {2}} - \frac {1}{2 \mu^ {2}} - \frac {1}{2}\right) ^ {2} - \frac {1}{\mu^ {2}}} \right]. \tag {91} \\ \end{array}
$$

Consequently, both the average logarithmic negativity  $\delta \bar{E}_{\mathcal{N}}$  defined in Eq. (88), and the relative error  $\delta \bar{E}_{\mathcal{N}}$ , given by Eq. (89), can be easily evaluated in terms of the purities. The relative error is plotted in Fig. 9(b) for symmetric states as a function of the ratio  $S_{L_i} / S_L$ . Notice, as already pointed out in the general instance of arbitrary  $p$ , how the error decays exponentially. In particular, it falls below  $5\%$  in the range  $S_L < S_{L_i}$  ( $\mu > \mu_i$ ), which excludes at most very weakly entangled states (states with  $E_{\mathcal{N}} \lesssim 1$  [44]). Let us remark that the accuracy of estimating entanglement by the average loga

rithmic negativity proves even better in the nonsymmetric case  $\mu_1\neq \mu_2$  , essentially because the maximal allowed entanglement decreases with the difference between the marginals, as shown in Fig. 3.

The above analysis proves that the average logarithmic negativity  $\overline{E}_{\mathcal{N}}$  is a reliable estimate of the logarithmic negativity  $E_{\mathcal{N}}$ , improving as the entanglement increases. This allows for an accurate quantification of continuous variable entanglement by knowledge of the global and marginal purities. As we already mentioned, the latter quantities may be in turn amenable to direct experimental determination by exploiting recent single-photon detection proposals or the upcoming technology of quantum networks.

# X. SUMMARY AND CONCLUDING REMARKS

Summarizing, we have pointed out the existence of both maximally and minimally entangled two-mode Gaussian states at fixed local and global generalized  $p$  entropies. The analytical properties of such states have been studied in detail for any value of  $p$ . Remarkably, for  $p \leqslant 2$ , minimally entangled states are minimum uncertainty states, saturating the Heisenberg principle, while maximally entangled states are nonsymmetric two-mode squeezed thermal states. Interestingly, for  $p > 2$  and in specific ranges of the values of the entropic measures, the role of such states is reversed. In particular, for such quantifications of the global and local entropies, two-mode squeezed thermal states, often referred to as continuous variable analog of maximally entangled states, turn out to be minimally entangled.

In the search for the extremely entangled states, we focused on the hierarchy of mixedness induced by  $p$  entropies

on the set of arbitrary multimode states, investigating several related subjects, like the ordering of such different entropic measures and the analytical comparison between the generic  $S_{p}$  (and in particular the von Neumann entropy  $S_{V}$ ) and the linear entropy  $S_{L}$ . Moreover, we have introduced the notion of "average logarithmic negativity" for given global and marginal generalized  $p$  entropies, showing that it provides a reliable estimate of CV entanglement in a wide range of physical parameters.

Our analysis also clarifies the reasons why the linear entropy is a "privileged" measure of mixedness in continuous variable systems. It is naturally normalized between 0 and 1, it offers an accurate qualification and quantification of entanglement of any mixed state while giving significant information about the state itself, and, crucially, is the only entropic measure which could be directly measured in the near future by schemes involving only single-photon detections or the technology of quantum networks, without requiring a full homodyne reconstruction of the state.

More generally, the present analysis shows that some of the canonical measures of entanglement and mixedness in the discrete variable scenario, such as the entanglement of formation and the von Neumann entropy, may not be the best choices for the characterization of mixed states of continuous variable systems. Discontinuous behaviors appear in the limit of infinite dimensions for quantities like the entanglement of formation, even when restricted to the special class of Gaussian states. Entanglement measures such as the logarithmic negativity and informational measures such as the linear entropy and the generalized entropies of higher order provide quantifications which are, in many respects, more satisfactory (both mathematically and physically) in the context of CV systems.

# ACKNOWLEDGMENTS

We thank INFM, INFN, and MIUR under national project PRIN-COFIN 2002 for financial support.

[1] L. Henderson and V. Vedral, Phys. Rev. Lett. 84, 2263 (2000); J. Phys. A 34, 6899 (2001).  
[2] S. Ishizaka and T. Hiroshima, Phys. Rev. A 62, 022310 (2000).  
[3] F. Verstraete, K. Audenaert, and B. De Moor, Phys. Rev. A 64, 012316 (2001); W. J. Munro, D. F. V. James, A. G. White, and P. G. Kwiat, ibid. 64, 030302 (2001).  
[4] T.-C. Wei, K. Nemoto, P. M. Goldbart, P. G. Kwiat, W. J. Munro, and F. Verstraete, Phys. Rev. A 67, 022110 (2003).  
[5] J. Eisert and M. Plenio, J. Mod. Opt. 46, 145 (1999); F. Verstraete, K. Audenaert, J. Dehaene, and B. de Moor, J. Phys. A 34, 10327 (2001).  
[6] G. Adesso, F. Illuminati, and S. De Siena, Phys. Rev. A 68, 062318 (2003).  
[7] A. G. White, D. F. V. James, W. J. Munro, and P. G. Kwiat, Phys. Rev. A 65, 012301 (2002).  
[8] M. Barbieri, F. De Martini, G. Di Nepi, and P. Mataloni, Phys. Rev. Lett. 92, 177901 (2004).  
[9] Quantum Information Theory with Continuous Variables, edited by S. L. Braunstein and A. K. Pati (Kluwer, Dordrecht, 2002).  
[10] H. P. Yuen and A. Kim, Phys. Lett. A 241, 135 (1998); F. Grosshans, G. Van Assche, J. Wenger, R. Brouri, N. J. Cerf, and P. Grangier, Nature (London) 421, 238 (2003).  
[11] A. Furusawa, J. L. Sorensen, S. L. Braunstein, C. A. Fuchs, H. J. Kimble, and E. S. Polzik, Science 282, 706 (1998); T. C. Zhang, K. W. Goh, C. W. Chou, P. Lodahl, and H. J. Kimble, Phys. Rev. A 67, 033802 (2003).  
[12] X. Li, Q. Pan, J. Jing, J. Zhang, C. Xie, and K. Peng, Phys. Rev. Lett. 88, 047904 (2002); J. Mizuno, K. Wakui, A. Furusawa, and M. Sasaki, e-print quant-ph/0402040.  
[13] G. Adesso, A. Serafini, and F. Illuminati, Phys. Rev. Lett. 92, 087901 (2004).  
[14] J. Eisert, C. Simon, and M. B. Plenio, J. Phys. A 35, 3911 (2002).  
[15] M. Keyl, D. Schlingemann, and R. F. Werner, Quantum Inf. Comput. 3, 281 (2003).

[16] We mention that, indeed, the continuous variable analogous of maximally entangled states have been introduced in Ref. [15], by considering singular states of the algebra of bounded operators.  
[17] J. Fiurasek and N. J. Cerf, Phys. Rev. Lett. 93, 063601 (2004).  
[18] R. Simon, E. C. G. Sudarshan, and N. Mukunda, Phys. Rev. A 36, 3868 (1987).  
[19] R. Simon, N. Mukunda, and B. Dutta, Phys. Rev. A 49, 1567 (1994).  
[20] See, e.g., S. M. Barnett and P. M. Radmore, Methods in Theoretical Quantum Optics (Clarendon Press, Oxford, 1997).  
[21] J. Williamson, Am. J. Math. 58, 141 (1936); see also V. I. Arnold, Mathematical Methods of Classical Mechanics (Springer-Verlag, New York, 1978).  
[22] R. Simon, Phys. Rev. Lett. 84, 2726 (2000).  
[23] L.-M. Duan, G. Giedke, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 84, 2722 (2000).  
[24] G. Vidal and R. F. Werner, Phys. Rev. A 65, 032314 (2002).  
[25] A. Serafini, F. Illuminati, and S. De Siena, J. Phys. B 37, L21 (2004).  
[26] L-z. Jiang, e-print quant-ph/0309156.  
[27] S. M. Barnett and S. J. D. Phoenix, Phys. Rev. A 40, 2404 (1989); 44, 535 (1991).  
[28] G. Giedke, M. M. Wolf, O. Krüger, R. F. Werner, and J. I. Cirac, Phys. Rev. Lett. 91, 107901 (2003).  
[29] G. Rigolin and C. O. Escobar, Phys. Rev. A 69, 012307 (2004).  
[30] A. Einstein, B. Podolski, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[31] T. Hiroshima, Phys. Rev. A 63, 022305 (2001); S. Scheel and D.-G. Welsch, ibid. 64, 063811 (2001); A. Serafini, F. Illuminati, M. G. A. Paris, and S. De Siena, ibid. 69, 022318 (2004).  
[32] R. Bathia, Matrix Analysis (Springer-Verlag, Berlin, 1997).  
[33] M. G. A. Paris, F. Illuminati, A. Serafini, and S. De Siena, Phys. Rev. A 68, 012314 (2003).  
[34] M. J. Bastiaans, J. Opt. Soc. Am. A 1, 711 (1984); 3, 1243

(1986); V. V. Dodonov, J. Opt. B: Quantum Semiclassical Opt. 4, S98 (2002).  
[35] C. Tsallis, J. Stat. Phys. 52, 479 (1988).  
[36] A. Rényi, Probability Theory (North-Holland, Amsterdam, 1970).  
[37] A. S. Holevo, M. Sohma, and O. Hirota, Phys. Rev. A 59, 1820 (1999).  
[38] A. Peres, Phys. Rev. Lett. 77, 1413 (1996); R. Horodecki, P. Horodecki, and M. Horodecki, Phys. Lett. A 210, 377 (1996).  
[39] K. Žyczkowski, P. Horodecki, A. Sanpera, and M. Lewenstein, Phys. Rev. A 58, 883 (1998).  
[40] The proof of such properties can be found in Ref. [24] for finite-dimensional Hilbert spaces. Anyway, since the proof essentially relies on the use of the Jordan decomposition, it still holds in infinite dimensions; see also J. Eisert, Ph.D. thesis,

University of Potsdam, 2001.  
[41] C. H. Bennett, D. P. DiVincenzo, J. A. Smolin, and W. K. Wootters, Phys. Rev. A 54, 3824 (1996).  
[42] A. K. Ekert, C. M. Alves, D. K. L. Oi, M. Horodecki, P. Horodecki, and L. C. Kwek, Phys. Rev. Lett. 88, 217901 (2002); R. Filip, Phys. Rev. A 65, 062320 (2002).  
[43] J. Wenger, J. Fiurášek, R. Tualle-Brouri, N. J. Cerf, and Ph. Grangier, e-print quant-ph/0403234.  
[44] It is straightforward to verify that, in the instance of two-mode squeezed thermal (symmetric) states, such a condition corresponds to  $\cosh(2r) \gtrsim \mu^{1/4}$ . This constraint can be easily satisfied with the present experimental technology: even for the quite unfavorable case  $\mu = 0.5$  the squeezing parameter needed is just  $r \simeq 0.3$ .