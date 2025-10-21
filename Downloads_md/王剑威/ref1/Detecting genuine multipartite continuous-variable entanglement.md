# Detecting genuine multipartite continuous-variable entanglement

Peter van Loock<sup>1</sup> and Akira Furusawa<sup>2</sup>  
<sup>1</sup>Quantum Information Theory Group, Zentrum für Moderne Optik, Universität Erlangen-Nürnberg, 91058 Erlangen, Germany  
<sup>2</sup>Department of Applied Physics, University of Tokyo, Tokyo 113-8656, Japan  
(Received 27 December 2002; published 29 May 2003)

We derive necessary conditions in terms of the variances of position and momentum linear combinations for all kinds of separability of a multiparty multimode continuous-variable state. Their violations can be sufficient for genuine multipartite entanglement, provided the combinations contain both conjugate variables of all modes. Hence, a complete state determination, for example, by detecting the entire correlation matrix of a Gaussian state, is not needed.

DOI: 10.1103/PhysRevA.67.052315

PACS number(s): 03.67.-a, 42.50.Dv

# I. INTRODUCTION

Quantum entanglement shared by two parties enhances their capabilities to communicate. In principle, it allows them to convey quantum information reliably through a classical channel (quantum teleportation [1]), to double the amount of classical information transmittable through a classical channel (quantum dense coding [2]), or to prepare at a distance states from nonorthogonal bases for secure communication (quantum key distribution [3-5]). These entanglement-assisted communication schemes are extendible to an arbitrary number of parties sharing multipartite entanglement. For instance, a sender may transfer quantum information through classical channels to several receivers as reliably as allowed by optimal cloning (telecloning [6]), or the parties may share quantum (or classical) information retrievable only when all parties cooperate (quantum secret sharing [7]). A more recent proposal that exploits the multiparty quantum correlations of multipartite entangled states is the so-called Byzantine agreement protocol [8]. In general, the presence of entanglement is verified through the success of a quantum protocol that would fail otherwise (e.g., quantum teleportation). Such an operational criterion is only sufficient for entanglement, and failure does not necessarily rule out its presence. In an experimental realization, however, before running through an entire entanglement-based protocol, it is desirable first to confirm that the generation of sophisticated multiparty entangled states has succeeded. The aim of this paper is to provide a simple but unambiguous experimental test to check for a particular kind of genuinely multipartite entangled states, namely, those described by continuous variables (CV), and produced with squeezed light and linear optics.

Work in the direction of generating tripartite CV entanglement has been carried out already by sending one half of a two-mode two-party entangled state through an extra beam splitter with a coherent state or a vacuum state at its second input port [9,10]. The resulting three-mode state was a side product of the Bell measurement for the teleportation of coherent states using a preshared symmetric two-mode squeezed state [9]. Its tripartite entanglement was not further investigated in this experiment. In another experiment, reported recently [10], the two-mode state was asymmetric, corresponding to two independently squeezed states com

bined at an asymmetric  $1:2$  beam splitter. The output threemode state after an additional symmetric beam splitter was then similar to the states proposed in Ref. [11].

Quantum communication, or more general quantum information with CV has attracted a lot of interest due to the relative simplicity and high efficiency in the generation, manipulation, and detection of optical CV states. Although recent results suggest that these assets of Gaussian CV operations (phase shifting, beam splitting, homodyne detections, phase-space displacements, and squeezing) are not extendible to more advanced quantum protocols such as entanglement distillation [12-14], the simple and efficient CV approach still seems promising for many tasks and might be suitable for others too when combined with discrete-variable (DV) strategies. On the other hand, potential linear-optics implementations of quantum protocols solely based on DV utilizing single photons are restricted by No-Go results such as the impossibility of a complete distinction between the four Bell states [15]. In order to perform such a Bell measurement near perfectly with linear optics, one has to employ complicated entangled states of many auxiliary photons [16]. In contrast, a Bell and also a Greenberger-Horne-Zeilinger (GHZ) state analyzer can be easily constructed in the CV setting using only beam splitters and homodyne detectors [17-19].

How may one now verify experimentally the presence of entanglement without implementing a full quantum protocol? We are here, particularly, concerned about the experimental verification of genuinely multipartite entangled states where none of the parties is separable from any other party (in terms of the separability properties of the total density matrix). In general, theoretical tests might be as well applicable to the experimental verification. For instance, the violation of inequalities imposed by local realism confirms the presence of entanglement. Proving genuine multipartite entanglement, however, requires stronger violations [20] than those determined by the commonly used Mermin-Klyshko  $N$ -party inequalities [21,22]. Moreover, in any case, violations of Bell-type inequalities using the Gaussian CV entangled states with always positive Wigner functions must rely on observables other than the quadratures (i.e., position and momentum). Photon number parity may serve as an appropriate dichotomic variable to reveal the nonlocality of the CV entangled states [23]. This applies to the two-party two-

mode EPR-like [23] and to the  $N$ -party  $N$ -mode GHZ-like CV states [24]. Such an approach, however, is not very feasible due to its need for detectors resolving large photon numbers.

The negative partial transpose (NPT) criterion [25] is necessary and sufficient for the bipartite inseparability of  $(2 \times 2)$ -dimensional,  $(2 \times 3)$ -dimensional [26], and  $(1 \times N)$ -mode Gaussian states [27,28]. A complete experimental determination of the state in question would also enable an NPT check. In general, any theoretical test is applicable when the experimentalist has full information about the quantum state after measurements on an ensemble of identically prepared states (e.g., by quantum tomography [29]). Such a direct verification of entanglement via a complete state measurement is in general very demanding to the experimentalist, in particular, when the state to be determined is a potentially multiparty entangled multimode state.

# II. GAUSSIAN STATES

The multiparty entanglement criteria that we will derive here do not rely on the assumption of Gaussian states. However, the states commonly produced in the laboratory are indeed Gaussian and the theoretical classification of different types of multipartite entanglement becomes simpler for Gaussian states [30].

Since the entanglement properties of a multimode, multiparty state are invariant under local phase-space displacements, the multimode states may have zero mean and their Wigner function is of the form

$$
W (\xi) = \frac {1}{(2 \pi) ^ {N} \sqrt {\det V ^ {(N)}}} \exp \left\{- \frac {1}{2} \xi [ V ^ {(N)} ] ^ {- 1} \xi^ {T} \right\}, \tag {1}
$$

with the  $2N$ -dimensional vector  $\xi$  having the quadrature pairs of all  $N$  modes as its components,

$$
\xi = \left(x _ {1}, p _ {1}, x _ {2}, p _ {2}, \dots , x _ {N}, p _ {N}\right),
$$

$$
\hat {\xi} = \left(\hat {x} _ {1}, \hat {p} _ {1}, \hat {x} _ {2}, \hat {p} _ {2}, \dots , \hat {x} _ {N}, \hat {p} _ {N}\right), \tag {2}
$$

and with the  $2N \times 2N$  correlation matrix  $V^{(N)}$  having as its elements the second moments symmetrized according to the Weyl correspondence [31],

$$
\begin{array}{l} \operatorname {T r} \left[ \hat {\rho} \left(\Delta \hat {\xi} _ {i} \Delta \hat {\xi} _ {j} + \Delta \hat {\xi} _ {j} \Delta \hat {\xi} _ {i}\right) / 2 \right] = \left\langle \left(\hat {\xi} _ {i} \hat {\xi} _ {j} + \hat {\xi} _ {j} \hat {\xi} _ {i}\right) / 2 \right\rangle \\ = \int W (\xi) \xi_ {i} \xi_ {j} d ^ {2 N} \xi \\ = V _ {i j} ^ {(N)}, \tag {3} \\ \end{array}
$$

where  $\Delta \hat{\xi}_i = \hat{\xi}_i - \langle \hat{\xi}_i\rangle = \hat{\xi}_i$  for zero mean values. Note that the correlation matrix of any physical state must be real, symmetric, positive, and must obey the commutation relation [27,28],

$$
\left[ \hat {\xi} _ {k}, \hat {\xi} _ {l} \right] = \frac {i}{2} \Lambda_ {k l}, \quad k, l = 1, 2, 3, \dots , 2 N, \tag {4}
$$

with the  $2N \times 2N$  matrix  $\Lambda$  having the  $2 \times 2$  matrix  $J$  as diagonal entry for each quadrature pair, for example, for  $N = 2$ ,

$$
\Lambda = \left( \begin{array}{c c} J & 0 \\ 0 & J \end{array} \right), \quad J = \left( \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right). \tag {5}
$$

A direct consequence of this commutation relation and the non-negativity of the density operator  $\hat{\rho}$  is the  $N$ -mode uncertainty relation [27,28],

$$
V ^ {(N)} - \frac {i}{4} \Lambda \geqslant 0. \tag {6}
$$

Note that this condition is equivalent to  $V^{(N)} + i\Lambda /4 \geqslant 0$  by complex conjugation. As for the direct verification of entanglement via a complete state measurement, for the Gaussian CV states, the complete measurement of an  $N$ -party,  $N$ -mode quantum state is accomplished by determining the  $2N \times 2N$  second-moment correlation matrix. This corresponds to  $N(1 + 2N)$  independent entries taking into account the symmetry of the correlation matrix. Kim et al. [32] recently demonstrated how to determine all these entries in the two-party, two-mode case using beam splitters and homodyne detectors. Joint homodyne detections of the two modes yield the intermode correlations such as  $\langle \hat{x}_1\hat{x}_2\rangle -\langle \hat{x}_1\rangle \langle \hat{x}_2\rangle$ ,  $\langle \hat{x}_1\hat{p}_2\rangle -\langle \hat{x}_1\rangle \langle \hat{p}_2\rangle$ , etc. Determining the local intramode correlations such as  $\langle \hat{x}_1\hat{p}_1 + \hat{p}_1\hat{x}_1\rangle /2 - \langle \hat{x}_1\rangle \langle \hat{p}_1\rangle$  is more subtle and requires additional beam splitters and homodyne detections (or, alternatively, heterodyne detections). Once the  $4 \times 4$  two-mode correlation matrix is known, the NPT criterion can be applied as a necessary and sufficient condition for bipartite Gaussian two-mode inseparability (where NPT corresponds to a sign change of all the momentum variables with positions unchanged [27]). In fact, the entanglement can also be quantified for a given correlation matrix [32,33]. For three-party three-mode Gaussian states, one may pursue a similar strategy. After measuring the 21 independent entries of the correlation matrix (for example, by extending the scheme of Kim et al. [32] to the three-mode case), the necessary and sufficient criteria by Giedke et al. [30] can be applied. Let us examine the separability properties of (in particular, three-party, three-mode) Gaussian states in more detail.

# III. SEPARABILITY PROPERTIES OF GAUSSIAN STATES

The criteria by Giedke et al. [30] determine to which of five possible classes of fully and partially separable, and fully inseparable states a three-party, three-mode Gaussian state belongs. Hence, genuine tripartite entanglement if present can be unambiguously identified. The classification is mainly based on the NPT criterion for CV states. Transposition is a positive map that corresponds in phase space to a sign change of all momentum variables,  $\xi^T\rightarrow \Gamma \xi^T = (x_1$ $-p_{1},x_{2}, - p_{2},\dots ,x_{N}, - p_{N})^{T}$  [27]. In terms of the correlation matrix, we have then  $V^{(N)}\to \Gamma V^{(N)}\Gamma$  . Since transposition is not a completely positive map, its partial application

to a subsystem only may yield an unphysical state when the subsystem was entangled to other subsystems. Expressing partial transposition of a bipartite Gaussian system by  $\Gamma_{a} \equiv \Gamma \oplus 1$  (where  $A \oplus B$  means the block-diagonal matrix with the matrices  $A$  and  $B$  as diagonal "entries," and  $A$  and  $B$  are, respectively,  $2N \times 2N$  and  $2M \times 2M$  square matrices applicable to  $N$  modes at  $a$ 's side and  $M$  modes at  $b$ 's side), the condition that the partially transposed Gaussian state described by  $\Gamma_{a} V^{(N + M)} \Gamma_{a}$  is unphysical [see Eq. (6)],  $\Gamma_{a} V^{(N + M)} \Gamma_{a} \neq \frac{i}{4} \Lambda$ , is sufficient for the inseparability between  $a$  and  $b$  [27,28]. For the Gaussian states with  $N = 1$  and an arbitrary  $M$ , this condition is necessary and sufficient [28]. The simplest example where the condition is no longer necessary for inseparability involves two modes at each side,  $N = M = 2$ . In this case, states with positive partial transpose (bound entangled Gaussian states) exist [28]. For the general bipartite  $N \times M$  case, there is also a necessary and sufficient condition: the correlation matrix  $V^{(N + M)}$  corresponds to a separable state if and only if (iff) a pair of correlation matrices  $V_{a}^{(N)}$  and  $V_{b}^{(M)}$  exists such that  $V^{(N + M)} \geqslant V_{a}^{(N)} \oplus V_{b}^{(M)}$  [28]. Since it is, in general, hard to find such a pair of correlation matrices  $V_{a}^{(N)}$  and  $V_{b}^{(M)}$  for a separable state or to prove the nonexistence of such a pair for an inseparable state, this criterion is not very practical. A more practical solution was provided in Ref. [34]. The operational criteria there, computable and testable via a finite number of iterations, are entirely independent of the NPT criterion. They rely on a nonlinear map between the correlation matrices rather than a linear one such as the partial transposition, and in contrast to the NPT criterion, they witness also the inseparability of bound entangled states. Thus, the separability problem for bipartite Gaussian states with arbitrarily many modes at each side is completely solved. For three-party three-mode Gaussian states, the only partially separable forms are those with a bipartite splitting of  $1 \times 2$  modes. Hence, already the NPT criterion is necessary and sufficient.

The classification of tripartite three-mode Gaussian states [30],

$$
\text {c l a s s} \quad \bar {V} _ {1} ^ {(3)} \neq \frac {i}{4} \Lambda , \bar {V} _ {2} ^ {(3)} \neq \frac {i}{4} \Lambda , \bar {V} _ {3} ^ {(3)} \neq \frac {i}{4} \Lambda ,
$$

$$
\text {c l a s s} \quad \bar {V} _ {k} ^ {(3)} \geqslant \frac {i}{4} \Lambda , \bar {V} _ {m} ^ {(3)} \neq \frac {i}{4} \Lambda , \bar {V} _ {n} ^ {(3)} \neq \frac {i}{4} \Lambda ,
$$

$$
\text {c l a s s} \quad \bar {V} _ {k} ^ {(3)} \geqslant \frac {i}{4} \Lambda , \bar {V} _ {m} ^ {(3)} \geqslant \frac {i}{4} \Lambda , \bar {V} _ {n} ^ {(3)} \neq \frac {i}{4} \Lambda ,
$$

$$
\text {c l a s s} 4 \text {o r} 5: \quad \bar {V} _ {1} ^ {(3)} \geqslant \frac {i}{4} \Lambda , \bar {V} _ {2} ^ {(3)} \geqslant \frac {i}{4} \Lambda , \bar {V} _ {3} ^ {(3)} \geqslant \frac {i}{4} \Lambda , \tag {7}
$$

is solely based on the NPT criterion, where  $\bar{V}_j^{(3)}\equiv \Gamma_jV^{(3)}\Gamma_j$  denotes the partial transposition with respect to one mode  $j$ . In classes 2 and 3, any permutation of modes  $(k,m,n)$  must be considered. Class 1 corresponds to the fully inseparable

states. Class 5 contains the fully separable states. A Gaussian state described by  $V^{(3)}$  is fully separable iff one-mode correlation matrices  $V_{1}^{(1)}, V_{2}^{(1)}$ , and  $V_{3}^{(1)}$  exist such that  $V^{(3)} \geqslant V_{1}^{(1)} \oplus V_{2}^{(1)} \oplus V_{3}^{(1)}$ . In general, fully separable quantum states can be written as a mixture of tripartite product states,  $\Sigma_{i}\eta_{i}\hat{\rho}_{i,1} \otimes \hat{\rho}_{i,2} \otimes \hat{\rho}_{i,3}$ . In class 2, we have the one-mode biseparable states, where only one particular mode is separable from the remaining pair of modes. This means in the Gaussian case that only for one particular mode  $k$ ,  $V^{(3)} \geqslant V_{k}^{(1)} \oplus V_{mn}^{(2)}$  with some two-mode correlation matrix  $V_{mn}^{(2)}$  and one-mode correlation matrix  $V_{k}^{(1)}$ . In general, such a state can be written as  $\Sigma_{i}\eta_{i}\hat{\rho}_{i,k} \otimes \hat{\rho}_{i,mn}$  for one mode  $k$ . Class 3 contains those states where two, but not three, bipartite splittings are possible, i.e., two different modes  $k$  and  $m$  are separable from the remaining pair of modes (two-mode biseparable states). The states of class 4 (three-mode biseparable states) can be written as a mixture of products between any mode 1, 2, or 3 and the remaining pair of modes, but not as a mixture of three-mode product states. Obviously, classes 4 and 5 are not distinguishable via the NPT criterion. An additional criterion for this distinction of class 4 and 5 Gaussian states is given in Ref. [30], deciding whether one-mode correlation matrices  $V_{1}^{(1)}, V_{2}^{(1)}$ , and  $V_{3}^{(1)}$  exist such that  $V^{(3)} \geqslant V_{1}^{(1)} \oplus V_{2}^{(1)} \oplus V_{3}^{(1)}$ . For the identification of genuinely tripartite entangled Gaussian states, only class 1 has to be distinguished from the rest. Hence, the NPT criterion alone suffices.

What about more than three parties and modes? Even for only four parties and modes, the separability issue becomes more subtle. The one-mode bipartite splittings,  $\Sigma_{i}\eta_{i}\hat{\rho}_{i,klm}\otimes \hat{\rho}_{i,n}$ , can be tested and possibly ruled out via the NPT criterion with respect to any mode  $n$ . In the Gaussian language, if  $\bar{V}_n^{(4)}\neq \frac{i}{4}\Lambda$  for any  $n$ , the state cannot be written in the above form. Since we consider here the bipartite splitting of  $1\times 3$  modes, the NPT condition is necessary and sufficient for the Gaussian states. However, also a state of the form  $\Sigma_{i}\eta_{i}\hat{\rho}_{i,kl}\otimes \hat{\rho}_{i,mn}$  leads to negative partial transpose with respect to any of the four modes when the two pairs  $(k,l)$  and  $(m,n)$  are each entangled. Thus, NPT with respect to any individual mode is necessary but not sufficient for genuine four-party entanglement. One has to consider also the partial transposition with respect to any pair of modes. For this  $2\times 2$  mode case, however, we know that entangled Gaussian states with positive partial transpose exist [28], but the NPT criterion is still sufficient for the inseparability between any two pairs. As for a necessary and sufficient condition, one can use those from Ref. [34]. In any case, in order to confirm genuine four-party or even  $N$ -party entanglement, one has to rule out any possible partially separable form. In principle, this can be done by considering all possible bipartite splittings (or groupings) and applying either the NPT criterion or the stronger operational criteria from Ref. [34]. Although a full theoretical characterization including criteria for entanglement classification has not been considered yet for more than three parties and modes, the presence of genu

ine multipartite entanglement can be confirmed, once the complete  $2N\times 2N$  correlation matrix is given.

Rather than detecting all the entries of the correlation matrix, we are aiming here at a simple check based on only a few measurements, preferably efficient homodyne detections. Even for larger numbers of parties, this check should remain simple. Though it may not yield full information (e.g., the complete correlation matrix) about the quantum state of interest, it should still unambiguously verify the presence of genuine multipartite entanglement. This check may prove the presence of entanglement indirectly through measurements after transforming the relevant state first into an appropriate form via linear optics.

# IV. DETECTING ENTANGLEMENT: BIPARTITE CASE

In the two-party, two-mode case, the necessary separability condition for any CV state [35]

$$
\left. \right.\left\langle\left[ \Delta \left(\hat {x} _ {1} - \hat {x} _ {2}\right)\right] ^ {2} \right\rangle + \left\langle\left[ \Delta \left(\hat {p} _ {1} + \hat {p} _ {2}\right)\right] ^ {2} \right\rangle \geqslant 2 \left|\left\langle\left[ \hat {x}, \hat {p} \right]\right\rangle\right|, \tag {8}
$$

can be tested, for example, with a single beam splitter. The position and momentum variables  $\hat{x}_l$  and  $\hat{p}_l$  (units free with  $\hbar = \frac{1}{2}$ , i.e.,  $[\hat{x}_l,\hat{p}_k] = i\delta_{lk} / 2$ ) correspond to the quadratures of two electromagnetic modes, i.e., the real and imaginary parts of the annihilation operators of the two modes:  $\hat{a}_l = \hat{x}_l + i\hat{p}_l$ . The beam splitter provides the suitable quadrature combinations for the positions and momenta, simultaneously detectable at the two output ports. Without beam splitter, just by measuring first both positions and subtracting them electronically, and in a second step, detecting both momenta and combining these electronically [36], a more direct test of the two-party condition is possible. However, instead of a simultaneous detection of the relevant combinations, it requires switching the two local oscillator phases from position to momentum measurements. For an ensemble of identically prepared states, this sequence of detections would still enable the application of the two-party condition. Note that the violation of Eq. (8) is only sufficient for inseparability, i.e., there are (even Gaussian) CV entangled states that satisfy Eq. (8). Any Gaussian CV state, however, can be transformed via local operations into a standard form, and the presence of entanglement would then always yield a violation [35] (alternatively, one may modify the inequality and leave the Gaussian state unchanged to obtain a necessary and sufficient condition [37]). The point is that the entanglement of states already in this standard form (such as two-mode squeezed states) can, in principle, always (for any nonzero squeezing) be verified experimentally by checking Eq. (8). A full determination of the correlation matrix, including elements such as  $\langle \hat{x}_1\hat{p}_2\rangle -\langle \hat{x}_1\rangle \langle \hat{p}_2\rangle$  which do not appear in the expressions of Eq. (8), is not required. Measuring these elements may also confirm that the state is in standard form

(when they are zero) and hence render the condition, Eq. (8), necessary and sufficient for separability. In any case, it would also enable quantification of the entanglement [32,33].

The combinations in condition, Eq. (8), are exactly those detected in a CV Bell measurement of modes 1 and 2 [17]. Thus, the verification of nonmaximum two-mode CV entanglement may rely on measurements of observables that are detected for the projection onto the maximally entangled CV basis of two modes. Now, we investigate the  $N$ -party,  $N$ -mode case in this respect.

# V. THE CV GHZ BASIS

Let us introduce the maximally entangled states

$$
\begin{array}{l} \left| \Psi \left(v, u _ {1}, u _ {2}, \dots , u _ {N - 1}\right) \right\rangle = \frac {1}{\sqrt {\pi}} \int_ {- \infty} ^ {\infty} d x e ^ {2 i v x} | x \rangle \otimes | x - u _ {1} \rangle \\ \otimes \left| x - u _ {1} - u _ {2} \right\rangle \otimes \dots \otimes \left| x - u _ {1} \right. \\ - u _ {2} - \dots - u _ {N - 1} \rangle . \tag {9} \\ \end{array}
$$

Since  $\int_{-\infty}^{\infty} dx |x\rangle \langle x| = 1$  and  $\langle x|x' \rangle = \delta(x - x')$ , they form a complete,

$$
\begin{array}{l} \int_ {- \infty} ^ {\infty} d v d u _ {1} d u _ {2} \dots d u _ {N - 1} \\ \times \left| \Psi \left(v, u _ {1}, u _ {2}, \dots , u _ {N - 1}\right) \right\rangle \\ \times \left\langle \Psi \left(v, u _ {1}, u _ {2}, \dots , u _ {N - 1}\right) \right| = 1 ^ {\otimes N}, \tag {10} \\ \end{array}
$$

and orthogonal,

$$
\begin{array}{l} \left\langle \Psi (v, u _ {1}, u _ {2}, \dots , u _ {N - 1}) \mid \Psi \left(v ^ {\prime}, u _ {1} ^ {\prime}, u _ {2} ^ {\prime}, \dots , u _ {N - 1} ^ {\prime}\right) \right\rangle \\ = \delta \left(v - v ^ {\prime}\right) \delta \left(u _ {1} - u _ {1} ^ {\prime}\right) \delta \left(u _ {2} - u _ {2} ^ {\prime}\right) \dots \delta \left(u _ {N - 1} - u _ {N - 1} ^ {\prime}\right), \tag {11} \\ \end{array}
$$

set of basis states for  $N$  modes. In a "CV GHZ state analyzer," determining the quantities  $v \equiv p_1 + p_2 + \dots + p_N$ ,  $u_1 \equiv x_1 - x_2$ ,  $u_2 \equiv x_2 - x_3$ , ..., and  $u_{N-1} \equiv x_{N-1} - x_N$  means projecting onto the basis  $\{|\Psi(v, u_1, u_2, \ldots, u_{N-1})\}$ . This can be accomplished with a sequence of beam splitters and homodyne detections [18,19]. Inferring from the two-party case, we may conjecture that the  $N$  quadrature combinations given by  $v, u_1, u_2, \ldots, u_{N-1}$  provide a sufficient set of observables for the verification of (possibly genuine)  $N$ -party entanglement. Just as for two parties, the variances of these quantities could then also be determined by combining the results of direct  $x$  and  $p$  measurements electronically. It was shown in Refs. [18,19] that conditions for genuine multipartite entanglement can be derived based on the above  $N$  combinations and additional assumptions such as the purity and the total symmetry of the state in question. Later, we derive a set of  $N-1$  conditions for these  $N$  combinations sufficient for the presence of genuine multipartite entanglement. This set is well suited for the experimental confirmation of the genuine multiparty entanglement of CV GHZ-type states. No extra assumptions about the state are needed in order to close the loophole of partial separability. First, we discuss now

what the structure of simple experimental criteria for multipartite CV entanglement might be.

# VI. DETECTING ENTANGLEMENT: TRIPARTITE CASE

Let us consider three parties and modes. The goal is to extend the simple two-party, two-mode entanglement check to a simple test for genuine three-party, three-mode entanglement. The criteria are to be expressed in terms of the variances of quadrature linear combinations for the modes involved. Defining

$$
\hat {u} \equiv h _ {1} \hat {x} _ {1} + h _ {2} \hat {x} _ {2} + h _ {3} \hat {x} _ {3}, \quad \hat {v} \equiv g _ {1} \hat {p} _ {1} + g _ {2} \hat {p} _ {2} + g _ {3} \hat {p} _ {3}, \tag {12}
$$

a fairly general ansatz is

$$
\left\langle \left(\Delta \hat {u}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {v}\right) ^ {2} \right\rangle_ {\rho} \geqslant f \left(h _ {1}, h _ {2}, h _ {3}, g _ {1}, g _ {2}, g _ {3}\right), \tag {13}
$$

as a potential necessary condition for an at least partially separable state. The position and momentum variables  $\hat{x}_l$  and  $\hat{p}_l$  are the quadratures of the three electromagnetic modes. The  $h_l$  and  $g_{l}$  are arbitrary real parameters. We will prove the following statement(s) for (at least partially) separable states:

$$
\begin{array}{l} \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, k m} \otimes \hat {\rho} _ {i, n} \\ \Rightarrow f \left(h _ {1}, h _ {2}, h _ {3}, g _ {1}, g _ {2}, g _ {3}\right) (14) \\ = \left(\left| h _ {n} g _ {n} \right| + \left| h _ {k} g _ {k} + h _ {m} g _ {m} \right|\right) / 2. (15) \\ \end{array}
$$

Here,  $\hat{\rho}_{i,km} \otimes \hat{\rho}_{i,n}$  indicates that the three-party density operator is a mixture of states  $i$  where parties (modes)  $k$  and  $m$  may be entangled or not, but party  $n$  is not entangled with the rest, and  $(k,m,n)$  is any triple of  $(1,2,3)$ . Hence, also the fully separable state is included in the above statements. In fact, for the fully separable state, we have

$$
\begin{array}{l} \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1} \otimes \hat {\rho} _ {i, 2} \otimes \hat {\rho} _ {i, 3} \\ \Rightarrow f \left(h _ {1}, h _ {2}, h _ {3}, g _ {1}, g _ {2}, g _ {3}\right) (16) \\ = \left(\left| h _ {1} g _ {1} \right| + \left| h _ {2} g _ {2} \right| + \left| h _ {3} g _ {3} \right|\right) / 2, (17) \\ \end{array}
$$

which is always greater than or equal to any of the boundaries in Eq. (15). For the proof, let us assume that the relevant state can be written as in Eq. (14). For the combinations in Eq. (12), we find

$$
\begin{array}{l} \left\langle \left(\Delta \hat {u}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {v}\right) ^ {2} \right\rangle_ {\rho} = \sum_ {i} \eta_ {i} \left(\left\langle \hat {u} ^ {2} \right\rangle_ {i} + \left\langle \hat {v} ^ {2} \right\rangle_ {i}\right) - \left\langle \hat {u} \right\rangle_ {\rho} ^ {2} - \left\langle \hat {v} \right\rangle_ {\rho} ^ {2} \\ = \sum_ {i} \eta_ {i} [ h _ {k} ^ {2} \langle \hat {x} _ {k} ^ {2} \rangle_ {i} + h _ {m} ^ {2} \langle \hat {x} _ {m} ^ {2} \rangle_ {i} + h _ {n} ^ {2} \langle \hat {x} _ {n} ^ {2} \rangle_ {i} + g _ {k} ^ {2} \langle \hat {p} _ {k} ^ {2} \rangle_ {i} + g _ {m} ^ {2} \langle \hat {p} _ {m} ^ {2} \rangle_ {i} + g _ {n} ^ {2} \langle \hat {p} _ {n} ^ {2} \rangle_ {i} + 2 (h _ {k} h _ {m} \langle \hat {x} _ {k} \hat {x} _ {m} \rangle_ {i} + h _ {k} h _ {n} \langle \hat {x} _ {k} \hat {x} _ {n} \rangle_ {i} \\ + h _ {m} h _ {n} \langle \hat {x} _ {m} \hat {x} _ {n} \rangle_ {i}) + 2 (g _ {k} g _ {m} \langle \hat {p} _ {k} \hat {p} _ {m} \rangle_ {i} + g _ {k} g _ {n} \langle \hat {p} _ {k} \hat {p} _ {n} \rangle_ {i} + g _ {m} g _ {n} \langle \hat {p} _ {m} \hat {p} _ {n} \rangle_ {i}) ] - \langle \hat {u} \rangle_ {\rho} ^ {2} - \langle \hat {v} \rangle_ {\rho} ^ {2} \\ = \sum_ {i} \eta_ {i} \left[ h _ {k} ^ {2} \langle (\Delta \hat {x} _ {k}) ^ {2} \rangle_ {i} + h _ {m} ^ {2} \langle (\Delta \hat {x} _ {m}) ^ {2} \rangle_ {i} + h _ {n} ^ {2} \langle (\Delta \hat {x} _ {n}) ^ {2} \rangle_ {i} + g _ {k} ^ {2} \langle (\Delta \hat {p} _ {k}) ^ {2} \rangle_ {i} + g _ {m} ^ {2} \langle (\Delta \hat {p} _ {m}) ^ {2} \rangle_ {i} + g _ {n} ^ {2} \langle (\Delta \hat {p} _ {n}) ^ {2} \rangle_ {i} \right. \\ + 2 h _ {k} h _ {m} \left(\left\langle \hat {x} _ {k} \hat {x} _ {m} \right\rangle_ {i} - \left\langle \hat {x} _ {k} \right\rangle_ {i} \left\langle \hat {x} _ {m} \right\rangle_ {i}\right) + 2 h _ {k} h _ {n} \left(\left\langle \hat {x} _ {k} \hat {x} _ {n} \right\rangle_ {i} - \left\langle \hat {x} _ {k} \right\rangle_ {i} \left\langle \hat {x} _ {n} \right\rangle_ {i}\right) + 2 h _ {m} h _ {n} \left(\left\langle \hat {x} _ {m} \hat {x} _ {n} \right\rangle_ {i} - \left\langle \hat {x} _ {m} \right\rangle_ {i} \left\langle \hat {x} _ {n} \right\rangle_ {i}\right) \\ + 2 g _ {k} g _ {m} (\langle \hat {p} _ {k} \hat {p} _ {m} \rangle_ {i} - \langle \hat {p} _ {k} \rangle_ {i} \langle \hat {p} _ {m} \rangle_ {i}) + 2 g _ {k} g _ {n} (\langle \hat {p} _ {k} \hat {p} _ {m} \rangle_ {i} - \langle \hat {p} _ {k} \rangle_ {i} \langle \hat {p} _ {m} \rangle_ {i}) + 2 g _ {m} g _ {n} (\langle \hat {p} _ {m} \hat {p} _ {n} \rangle_ {i} - \langle \hat {p} _ {m} \rangle_ {i} \langle \hat {p} _ {n} \rangle_ {i}) ] \\ + \sum_ {i} \eta_ {i} \left\langle \hat {u} \right\rangle_ {i} ^ {2} - \left(\sum_ {i} \eta_ {i} \left\langle \hat {u} \right\rangle_ {i}\right) ^ {2} + \sum_ {i} \eta_ {i} \left\langle \hat {v} \right\rangle_ {i} ^ {2} - \left(\sum_ {i} \eta_ {i} \left\langle \hat {v} \right\rangle_ {i}\right) ^ {2}, \tag {18} \\ \end{array}
$$

where  $\langle \dots \rangle_{i}$  means the average in the state  $\hat{\rho}_{i,km} \otimes \hat{\rho}_{i,n}$ . Note that in the derivation, so far we have not used the particular form in Eq. (14) yet. Exploiting this form of the state, we obtain  $\langle \hat{x}_k\hat{x}_n\rangle_i = \langle \hat{x}_k\rangle_i\langle \hat{x}_n\rangle_i$ ,  $\langle \hat{x}_m\hat{x}_n\rangle_i = \langle \hat{x}_m\rangle_i\langle \hat{x}_n\rangle_i$  and similarly for the terms involving  $p$ . Because modes  $k$  and  $m$  may be entangled in the states  $i$ , we cannot replace  $\langle \hat{x}_k\hat{x}_m\rangle_i$  by  $\langle \hat{x}_k\rangle_i\langle \hat{x}_m\rangle_i$ , etc. By applying the Cauchy-Schwarz inequality as in the two-party derivation of Ref. [35],  $\Sigma_iP_i\langle \hat{u}\rangle_i^2 \geqslant (\Sigma_iP_i|\langle \hat{u}\rangle_i|)^2$ , we see that the last line in Eq. (18) is bounded below by zero. Hence in order to prove  $\langle (\Delta \hat{u})^2\rangle_\rho + \langle (\Delta \hat{v})^2\rangle_\rho \geqslant (|h_ng_n| + |h_kg_k + h_mg_m|)/2$ , it re

mains to be shown that for any  $i$  [recall that the mixture in Eq. (14) is a convex sum with  $\Sigma_{i}\eta_{i} = 1$ ],

$$
\begin{array}{l} h _ {k} ^ {2} \left\langle \left(\Delta \hat {x} _ {k}\right) ^ {2} \right\rangle_ {i} + h _ {m} ^ {2} \left\langle \left(\Delta \hat {x} _ {m}\right) ^ {2} \right\rangle_ {i} + h _ {n} ^ {2} \left\langle \left(\Delta \hat {x} _ {n}\right) ^ {2} \right\rangle_ {i} + g _ {k} ^ {2} \left\langle \left(\Delta \hat {p} _ {k}\right) ^ {2} \right\rangle_ {i} \\ + g _ {m} ^ {2} \left\langle \left(\Delta \hat {p} _ {m}\right) ^ {2} \right\rangle_ {i} + g _ {n} ^ {2} \left\langle \left(\Delta \hat {p} _ {n}\right) ^ {2} \right\rangle_ {i} + 2 h _ {k} h _ {m} \left(\left\langle \hat {x} _ {k} \hat {x} _ {m} \right\rangle_ {i} \right. \\ - \left\langle \hat {x} _ {k} \right\rangle_ {i} \left\langle \hat {x} _ {m} \right\rangle_ {i}) + 2 g _ {k} g _ {m} \left(\left\langle \hat {p} _ {k} \hat {p} _ {m} \right\rangle_ {i} - \left\langle \hat {p} _ {k} \right\rangle_ {i} \left\langle \hat {p} _ {m} \right\rangle_ {i}\right) \\ \geqslant \left(\left| h _ {n} g _ {n} \right| + \left| h _ {k} g _ {k} + h _ {m} g _ {m} \right|\right) / 2. \tag {19} \\ \end{array}
$$

By rewriting the left-hand side of Eq. (19) in terms of variances only, indeed we find

$$
\begin{array}{l} h _ {n} ^ {2} \left\langle \left(\Delta \hat {x} _ {n}\right) ^ {2} \right\rangle_ {i} + g _ {n} ^ {2} \left\langle \left(\Delta \hat {p} _ {n}\right) ^ {2} \right\rangle_ {i} + \left\langle \left[ \Delta \left(h _ {k} \hat {x} _ {k} + h _ {m} \hat {x} _ {m}\right) \right] ^ {2} \right\rangle_ {i} \\ + \left\langle \left[ \Delta \left(g _ {k} \hat {p} _ {k} + g _ {m} \hat {p} _ {m}\right) \right] ^ {2} \right\rangle_ {i} \\ \geqslant \left| \left\langle \left[ h _ {n} \hat {x} _ {n}, g _ {n} \hat {p} _ {n} \right] \right\rangle \right| + \left| \left\langle \left[ h _ {k} \hat {x} _ {k} + h _ {m} \hat {x} _ {m}, g _ {k} \hat {p} _ {k} + g _ {m} \hat {p} _ {m} \right] \right\rangle \right| \\ = \left(\left| h _ {n} g _ {n} \right| + \left| h _ {k} g _ {k} + h _ {m} g _ {m} \right|\right) / 2, \tag {20} \\ \end{array}
$$

using the sum uncertainty relation  $\langle (\Delta \hat{A})^2\rangle +\langle (\Delta \hat{B})^2\rangle$ $\geqslant |\langle [\hat{A},\hat{B} ]\rangle |$  and  $[\hat{x}_l,\hat{p}_j] = i\delta_{lj} / 2$  . Hence, the statements in Eq. (15) with Eq. (14) are proven for all permutations of  $(k,m,n) = (1,2,3)$  . The inequalities, Eq. (13) with Eq. (15) and Eq. (14), represent necessary conditions for all kinds of (partial) separability in a tripartite three-mode state. One may then prove the presence of genuine tripartite entanglement through violations of these inequalities, thus ruling out any (partially) separable form. Whether there are really three different conditions required for the verification, depends on the choice of the coefficients  $h_l$  and  $g_{l}$  in the linear combinations. For a particular choice, some of the conditions may coincide. For example, consider  $h_1 = g_1 = 1$  and  $g_{2} = g_{3}$ $= -h_{2} = -h_{3} = 1 / \sqrt{2}$  in Eq. (12). In this case, the boundaries in Eq. (15) become identical for  $(k,m,n) = (1,2,3)$  and  $(k,m,n) = (3,1,2)$ $f(h_{1},h_{2},h_{3},g_{1},g_{2},g_{3}) = 1 / 2$  . The boundary of Eq. (15) is even larger when  $(k,m,n) = (2,3,1)$ $f(h_{1},h_{2},h_{3},g_{1},g_{2},g_{3}) = 1$  , equivalent to that for a fully separable state in Eq. (16) with Eq. (17). Hence the violation of a single condition,

$$
\begin{array}{l} \left. \left\langle \{\Delta [ \hat {x} _ {1} - (\hat {x} _ {2} + \hat {x} _ {3}) / \sqrt {2} ] \} ^ {2} \right\rangle_ {\rho} + \left\langle \{\Delta [ \hat {p} _ {1} + (\hat {p} _ {2} + \hat {p} _ {3}) / \sqrt {2} ] \} ^ {2} \right\rangle_ {\rho} \right. \\ \geqslant 1 / 2, \tag {21} \\ \end{array}
$$

is already sufficient for genuine tripartite entanglement. These particular combinations are not only significant for the reason that they yield nonzero boundaries for all kinds of separable states. Moreover, their commutator vanishes,

$$
[ \hat {x} _ {1} - (\hat {x} _ {2} + \hat {x} _ {3}) / \sqrt {2}, \hat {p} _ {1} + (\hat {p} _ {2} + \hat {p} _ {3}) / \sqrt {2} ] = 0, \tag {22}
$$

allowing for arbitrarily good violations of Eq. (21) and, in principle, the existence of a simultaneous eigenstate of these two combinations. Such a state corresponds to the three-mode state obtainable by splitting one half of an infinitely squeezed two-mode squeezed (EPR) state at a 50:50 beam splitter. The EPR correlations,  $\hat{x}_1 - \hat{x}_2\rightarrow 0$  and  $\hat{p}_1 + \hat{p}_2\rightarrow 0$  are then transformed into the three-mode correlations  $\hat{x}_1 - (\hat{x}_2' + \hat{x}_3') / \sqrt{2}\rightarrow 0$  and  $\hat{p}_1 + (\hat{p}_2' + \hat{p}_3') / \sqrt{2}\rightarrow 0$ . Let us turn to an arbitrary number of parties (modes) now.

# VII. DETECTING ENTANGLEMENT: MULTIPARTITE CASE

Inferring from the discussion of the preceding section, the recipe for verifying the genuine multipartite entanglement between arbitrarily many parties and modes is the following. First, measure both quadratures  $x$  and  $p$  of all modes involved and combine them in an appropriate linear combina-

tion. The variances of these combinations may then yield violations of conditions necessary for partial separability. Appropriate combinations are those where the total variances for all partially separable states have nonzero lower bounds and where the commutators of the combinations vanish. As for the derivation of the corresponding entanglement criteria, we employ the following steps.

(1) Select a distinct pair of modes  $(m,n)$ .  
(2) Choose appropriate linear combinations of the quadratures in order to rule out all possible separable splittings between this pair of modes in the convex sum of the total density operator.  
(3) Consider different pairs  $(m,n)$  to negate all partial separabilities; if necessary add further conditions involving other linear combinations.

Below it will become clear that step (2) can be performed simply by using the appropriate bipartite combinations,  $\hat{x}_m - \hat{x}_n$  and  $\hat{p}_m + \hat{p}_n$ , i.e., by taking all  $h_l = g_l = 0$  except  $h_m = g_m = 1$  and  $h_n = -g_n = -1$  in the general combinations,

$$
\hat {u} \equiv h _ {1} \hat {x} _ {1} + h _ {2} \hat {x} _ {2} + \dots + h _ {N} \hat {x} _ {N},
$$

$$
\hat {v} \equiv g _ {1} \hat {p} _ {1} + g _ {2} \hat {p} _ {2} + \dots + g _ {N} \hat {p} _ {N}. \tag {23}
$$

The boundaries of the total variance conditions are then identical for any pair  $(m,n)$  separable in the convex sum, namely,  $f(h_{l},g_{l})\equiv 1$  in

$$
\left\langle \left(\Delta \hat {u}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {v}\right) ^ {2} \right\rangle_ {\rho} \geqslant f \left(h _ {1}, h _ {2}, \dots , h _ {N}, g _ {1}, g _ {2}, \dots , g _ {N}\right). \tag {24}
$$

However, in general, one obtains better multiparty conditions when linear combinations for the quadratures of more than only two modes are used. Through such multimode combinations, the potential multimode correlations are taken into account. Before giving an example, let us first derive the general  $N$ -party bounds in the condition given in Eq. (24). For any partially separable form, the total density operator can be written as

$$
\hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, k _ {r}, \dots , m} \otimes \hat {\rho} _ {i, k _ {s}, \dots , n}, \tag {25}
$$

with a distinct pair of "separable modes"  $(m,n)$  and the other modes  $k_{r}\neq k_{s}$ . For the combinations in Eq. (23), we find now

$$
\begin{array}{l} \left\langle \left(\Delta \hat {u}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {v}\right) ^ {2} \right\rangle_ {\rho} = \sum_ {i} \eta_ {i} \left(\left\langle \hat {u} ^ {2} \right\rangle_ {i} + \left\langle \hat {v} ^ {2} \right\rangle_ {i}\right) - \left\langle \hat {u} \right\rangle_ {\rho} ^ {2} - \left\langle \hat {v} \right\rangle_ {\rho} ^ {2} \\ = \sum_ {i} \eta_ {i} \left[ h _ {m} ^ {2} \langle \hat {x} _ {m} ^ {2} \rangle_ {i} + h _ {n} ^ {2} \langle \hat {x} _ {n} ^ {2} \rangle_ {i} + \sum_ {j = 1} ^ {N - 2} h _ {k _ {j}} ^ {2} \langle \hat {x} _ {k _ {j}} ^ {2} \rangle_ {i} + g _ {m} ^ {2} \langle \hat {p} _ {m} ^ {2} \rangle_ {i} + g _ {n} ^ {2} \langle \hat {p} _ {n} ^ {2} \rangle_ {i} + \sum_ {j = 1} ^ {N - 2} g _ {k _ {j}} ^ {2} \langle \hat {p} _ {k _ {j}} ^ {2} \rangle_ {i} \right. \\ + \sum_ {j \neq j ^ {\prime} = 1} ^ {N - 2} \left(h _ {k _ {j}} h _ {k _ {j ^ {\prime}}} \langle \hat {x} _ {k _ {j}} \hat {x} _ {k _ {j ^ {\prime}}} \rangle_ {i} + g _ {k _ {j}} g _ {k _ {j ^ {\prime}}} \langle \hat {p} _ {k _ {j}} \hat {p} _ {k _ {j ^ {\prime}}} \rangle_ {i}\right) + 2 \sum_ {j = 1} ^ {N - 2} \left(h _ {k _ {j}} h _ {m} \langle \hat {x} _ {k _ {j}} \hat {x} _ {m} \rangle_ {i} + h _ {k _ {j}} h _ {n} \langle \hat {x} _ {k _ {j}} \hat {x} _ {n} \rangle_ {i} \right. \\ \left. \left. + g _ {k _ {j}} g _ {m} \langle \hat {p} _ {k _ {j}} \hat {p} _ {m} \rangle_ {i} + g _ {k _ {j}} g _ {n} \langle \hat {p} _ {k _ {j}} \hat {p} _ {n} \rangle_ {i}\right) + 2 \left(h _ {m} h _ {n} \langle \hat {x} _ {m} \hat {x} _ {n} \rangle_ {i} + g _ {m} g _ {n} \langle \hat {p} _ {m} \hat {p} _ {n} \rangle_ {i}\right) \right] - \langle \hat {u} \rangle_ {\rho} ^ {2} - \langle \hat {v} \rangle_ {\rho} ^ {2} \\ = \sum_ {i} \eta_ {i} \left\{h _ {m} ^ {2} \left\langle \left(\Delta \hat {x} _ {m}\right) ^ {2} \right\rangle_ {i} + h _ {n} ^ {2} \left\langle \left(\Delta \hat {x} _ {n}\right) ^ {2} \right\rangle_ {i} + g _ {m} ^ {2} \left\langle \left(\Delta \hat {p} _ {m}\right) ^ {2} \right\rangle_ {i} + g _ {n} ^ {2} \left\langle \left(\Delta \hat {p} _ {n}\right) ^ {2} \right\rangle_ {i} + \sum_ {j = 1} ^ {N - 2} \left(h _ {k _ {j}} ^ {2} \left\langle \left(\Delta \hat {x} _ {k _ {j}}\right) ^ {2} \right\rangle_ {i} \right. \right. \\ + g _ {k _ {j}} ^ {2} \langle (\Delta \hat {p} _ {k _ {j}}) ^ {2} \rangle_ {i}) + \sum_ {r \neq r ^ {\prime}} [ h _ {k _ {r}} h _ {k _ {r ^ {\prime}}} (\langle \hat {x} _ {k _ {r}} \hat {x} _ {k _ {r ^ {\prime}}} \rangle_ {i} - \langle \hat {x} _ {k _ {r}} \rangle_ {i} \langle \hat {x} _ {k _ {r ^ {\prime}}} \rangle_ {i}) + g _ {k _ {r}} g _ {k _ {r ^ {\prime}}} (\langle \hat {p} _ {k _ {r}} \hat {p} _ {k _ {r ^ {\prime}}} \rangle_ {i} - \langle \hat {p} _ {k _ {r}} \rangle_ {i} \langle \hat {p} _ {k _ {r ^ {\prime}}} \rangle_ {i}) ] \\ + \sum_ {s \neq s ^ {\prime}} \left[ h _ {k _ {s}} h _ {k _ {s} ^ {\prime}} \left(\left\langle \hat {x} _ {k _ {s}} \hat {x} _ {k _ {s} ^ {\prime}} \right\rangle_ {i} - \left\langle \hat {x} _ {k _ {s}} \right\rangle_ {i} \left\langle \hat {x} _ {k _ {s} ^ {\prime}} \right\rangle_ {i}\right) + g _ {k _ {s}} g _ {k _ {s} ^ {\prime}} \left(\left\langle \hat {p} _ {k _ {s}} \hat {p} _ {k _ {s} ^ {\prime}} \right\rangle_ {i} - \left\langle \hat {p} _ {k _ {s}} \right\rangle_ {i} \left\langle \hat {p} _ {k _ {s} ^ {\prime}} \right\rangle_ {i}\right) \right] \\ + 2 \sum_ {r} \left[ h _ {k _ {r}} h _ {m} (\langle \hat {x} _ {k _ {r}} \hat {x} _ {m} \rangle_ {i} - \langle \hat {x} _ {k _ {r}} \rangle_ {i} \langle \hat {x} _ {m} \rangle_ {i}) + g _ {k _ {r}} g _ {m} (\langle \hat {p} _ {k _ {r}} \hat {p} _ {m} \rangle_ {i} - \langle \hat {p} _ {k _ {r}} \rangle_ {i} \langle \hat {p} _ {m} \rangle_ {i}) \right] \\ + 2 \sum_ {s} \left. \left[ h _ {k _ {s}} h _ {n} \left(\left\langle \hat {x} _ {k _ {s}} \hat {x} _ {n} \right\rangle_ {i} - \left\langle \hat {x} _ {k _ {s}} \right\rangle_ {i} \left\langle \hat {x} _ {n} \right\rangle_ {i}\right) + g _ {k _ {s}} g _ {n} \left(\left\langle \hat {p} _ {k _ {s}} \hat {p} _ {n} \right\rangle_ {i} - \left\langle \hat {p} _ {k _ {s}} \right\rangle_ {i} \left\langle \hat {p} _ {n} \right\rangle_ {i}\right) \right] \right\} \\ + \sum_ {i} \eta_ {i} \langle \hat {u} \rangle_ {i} ^ {2} - \left(\sum_ {i} \eta_ {i} \langle \hat {u} \rangle_ {i}\right) ^ {2} + \sum_ {i} \eta_ {i} \langle \hat {v} \rangle_ {i} ^ {2} - \left(\sum_ {i} \eta_ {i} \langle \hat {v} \rangle_ {i}\right) ^ {2}. \tag {26} \\ \end{array}
$$

For the last equality, we exploited Eq. (25), namely, modes  $k_{r}$  through  $m$  are separable from modes  $k_{s}$  through  $n$  in the convex sum of the total density operator. Similar to the three-party case, we can now apply the Cauchy-Schwarz inequality to the last line of Eq. (26) and express the remaining terms by variances only. This leads for any  $i$  to

$$
\begin{array}{l} \left\langle \left[ \Delta \left(h _ {m} \hat {x} _ {m} + \sum_ {r} h _ {k _ {r}} \hat {x} _ {k _ {r}}\right) \right] ^ {2} \right\rangle_ {i} + \left\langle \left[ \Delta \left(g _ {m} \hat {p} _ {m} + \sum_ {r} g _ {k _ {r}} \hat {p} _ {k _ {r}}\right) \right] ^ {2} \right\rangle_ {i} \\ \left. + \left\langle \left[ \Delta \left(h _ {n} \hat {x} _ {n} + \sum_ {s} h _ {k _ {s}} \hat {x} _ {k _ {s}}\right) \right] ^ {2} \right\rangle_ {i} + \left\langle \left[ \Delta \left(g _ {n} \hat {p} _ {n} + \sum_ {s} g _ {k _ {s}} \hat {p} _ {k _ {s}}\right) \right] ^ {2} \right\rangle_ {i} \right. \\ \geqslant \left| \left\langle \left[ h _ {m} \hat {x} _ {m} + \sum_ {r} h _ {k _ {r}} \hat {x} _ {k _ {r}}, g _ {m} \hat {p} _ {m} + \sum_ {r} g _ {k _ {r}} \hat {p} _ {k _ {r}} \right] \right\rangle \right| + \left| \left\langle \left[ h _ {n} \hat {x} _ {n} + \sum_ {s} h _ {k _ {s}} \hat {x} _ {k _ {s}}, g _ {n} \hat {p} _ {n} + \sum_ {s} g _ {k _ {s}} \hat {p} _ {k _ {s}} \right] \right\rangle \right|, \tag {27} \\ \end{array}
$$

using again the sum uncertainty relation  $\langle (\Delta \hat{A})^2\rangle +\langle (\Delta \hat{B})^2\rangle \geqslant |\langle [\hat{A},\hat{B} ]\rangle |$  . Thus, by evaluating the commutators with  $[\hat{x}_l,\hat{p}_j] = i\delta_{lj} / 2$  , we obtain for the total variance

$$
\begin{array}{l} \left\langle \left(\Delta \hat {u}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {v}\right) ^ {2} \right\rangle_ {\rho} \geqslant \frac {1}{2} \left(\left| h _ {m} g _ {m} + \sum_ {r} h _ {k _ {r}} g _ {k _ {r}} \right| + \right| h _ {n} g _ {n} \\ \left. + \sum_ {s} h _ {k _ {s}} g _ {k _ {s}} \right|. \tag {28} \\ \end{array}
$$

Any additional splitting of the parties in the states

$i,\quad \hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,k_{r},\dots ,m}\otimes \dots \otimes \hat{\rho}_{i,k_{r^{\prime}}}\otimes \hat{\rho}_{i,k_{s},\dots ,n}\otimes \dots \otimes \hat{\rho}_{i,k_{s^{\prime}}},$  would in general make the bound larger, eventually yielding the bound for the fully separable state,  $\Sigma_j|h_jg_j| / 2(j$ $= 1,\ldots ,N)$

As mentioned previously, the well-known bipartite combinations applied to modes  $(m,n)$ ,  $\hat{x}_m - \hat{x}_n$  and  $\hat{p}_m + \hat{p}_n$ , mean all  $h_l = g_l = 0$  except  $h_m = g_m = 1$  and  $h_n = -g_n = -1$  in Eq. (28) and hence  $\langle (\Delta \hat{u})^2\rangle_{\rho} + \langle (\Delta \hat{v})^2\rangle_{\rho} \geqslant 1$ .

As for a simple example, we may extend that from the preceding section to  $N$  modes and set  $h_1 = g_1 = 1$  and

![](images/d73dc89f26fdb76bba98704d05434328e9aaa0b88fc2408262cba747094f88d6.jpg)  
FIG. 1. Verification of genuine tripartite CV entanglement.  $x$  measurements: directly detecting the  $x$  quadratures of all three modes and electronically combining them in an appropriate way. The three-mode tripartite entangled state of modes 1, 2, and 3 in this figure is produced with three squeezers and two beam splitters (the star denotes a 1:2 BS).

$g_{2} = g_{3} = \dots = g_{N} = -h_{2} = -h_{3} = \dots = -h_{N} = 1 / \sqrt{N - 1}$  Without loss of generality, we choose  $m = 1$  and obtain for a state of the form given in Eq. (25),

$$
\left\langle \left(\Delta \hat {u}\right) ^ {2} \right\rangle_ {\rho} + \left\langle \left(\Delta \hat {v}\right) ^ {2} \right\rangle_ {\rho} \geqslant \frac {1}{2} \left(\left| 1 - \frac {M _ {r}}{N - 1} \right| + \left| \frac {1 + M _ {s}}{N - 1} \right|\right), \tag {29}
$$

where  $M_r$  is the number of modes potentially entangled with mode  $m = 1$  in the convex sum and  $M_s$  is the number of modes potentially entangled with mode  $n$  in the convex sum. Apart from the fully inseparable case  $M_r = N - 1$ , the boundary in Eq. (29) is always greater than zero, allowing for an ultimate nonzero bound for all kinds of partial separability. Since  $[\hat{u},\hat{v}] = 0$ , genuine  $N$ -party entanglement can be verified when  $\langle (\Delta \hat{u})^2\rangle_{\rho} + \langle (\Delta \hat{v})^2\rangle_{\rho}$  is sufficiently close to zero. The ultimate (smallest) bound is given by the state with the maximum number of modes  $M_r$  inseparable from mode  $m = 1$  in the convex sum,  $M_r = N - 2$ , and hence  $M_s = 0$ . This bound is then  $1 / (N - 1)$ . If none of the modes is inseparable from mode  $m = 1$ ,  $M_r = 0$  and  $M_s = N - 2$ , the boundary becomes simply that of a fully separable state, namely 1. Thus, again the violation of a single condition,

$$
\begin{array}{l} \left\langle \left\{\Delta \left[ \hat {x} _ {1} - \left(\hat {x} _ {2} + \hat {x} _ {3} + \dots + \hat {x} _ {N}\right) / \sqrt {N - 1} \right] \right\} ^ {2} \right\rangle_ {\rho} \\ + \left\langle \left\{\Delta \left[ \hat {p} _ {1} + \left(\hat {p} _ {2} + \hat {p} _ {3} + \dots + \hat {p} _ {N}\right) / \sqrt {N - 1} \right] \right\} ^ {2} \right\rangle_ {\rho} \\ \geqslant 1 / (N - 1), \tag {30} \\ \end{array}
$$

is sufficient for genuine  $N$ -partite entanglement. As an example for the violation of the ultimate bound for genuine  $N$ -party entanglement, consider the  $N$ -mode state that

![](images/269ece7b1f938a78cee054bbb13bdf7bfd929bdc8e68ac7ca17aefc852375e4f.jpg)  
FIG. 2. Verification of genuine tripartite CV entanglement.  $p$  measurements: directly detecting the  $p$  quadratures of all three modes and electronically combining them in an appropriate way. The three-mode tripartite entangled state of modes 1, 2, and 3 in this figure is produced with three squeezers and two beam splitters. The parameters  $g_{i}$  are the "gains" from the conditions in Eq. (37) which can be chosen optimally (see the text later).

emerges after symmetrically splitting one half of an infinitely squeezed two-mode squeezed state by  $N - 2$  beam splitters. The output state is a simultaneous eigenstate of  $\hat{u}$  and  $\hat{v}$ . In this case, the EPR correlations,  $\hat{x}_1 - \hat{x}_2 \rightarrow 0$  and  $\hat{p}_1 + \hat{p}_2 \rightarrow 0$ , are transformed into the  $N$ -mode correlations  $\hat{x}_1 - (\hat{x}_2' + \hat{x}_3' + \dots + \hat{x}_N') / \sqrt{N - 1} \rightarrow 0$  and  $\hat{p}_1 + (\hat{p}_2' + \hat{p}_3' + \dots + \hat{p}_N') / \sqrt{N - 1} \rightarrow 0$ . As a further example, we will now discuss the CV GHZ-type states with quadrature correlations analogous to those of DV GHZ states.

# VIII. EXAMPLE: CV GHZ-TYPE STATES

We consider a family of genuinely  $N$ -party entangled states. The members of this family are those states that emerge from a particular sequence of  $N - 1$  phase-free beam splitters (" $N$  splitter") with  $N$  squeezed state inputs [11]. By choosing the squeezing direction of one distinct input mode orthogonal to that of the remaining input modes (mode 1 squeezed in  $p$  and the other modes squeezed in  $x$ , as shown in Figs. 1 and 2 for  $N = 3$ ) and the degree of squeezing by  $r_1$  of mode 1 potentially different from that of the other modes (which are equally squeezed by  $r_2$ ) [39], the output states have the following properties [18,19]. These are pure  $N$ -mode states, totally symmetric under interchange of modes, and retain the Gaussian character of the input states. Hence, they are entirely described by their second-moment correlation matrix

$$
V ^ {(N)} = \frac {1}{4} \left( \begin{array}{c c c c c c c} a & 0 & c & 0 & c & 0 & \dots \\ 0 & b & 0 & d & 0 & d & \dots \\ c & 0 & a & 0 & c & 0 & \dots \\ 0 & d & 0 & b & 0 & d & \dots \\ c & 0 & c & 0 & a & 0 & \dots \\ 0 & d & 0 & d & 0 & b & \dots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \end{array} \right), \tag {31}
$$

where

$$
\begin{array}{l} a = \frac {1}{N} e ^ {+ 2 r _ {1}} + \frac {N - 1}{N} e ^ {- 2 r _ {2}}, \\ b = \frac {1}{N} e ^ {- 2 r _ {1}} + \frac {N - 1}{N} e ^ {+ 2 r _ {2}}, \\ c = \frac {1}{N} \left(e ^ {+ 2 r _ {1}} - e ^ {- 2 r _ {2}}\right), \\ d = \frac {1}{N} \left(e ^ {- 2 r _ {1}} - e ^ {+ 2 r _ {2}}\right). \tag {32} \\ \end{array}
$$

For squeezed vacuum inputs, the multimode output states have zero mean and their Wigner function is of the form given in Eq. (1). The particularly simple form of the correlation matrix in Eq. (31) is, in addition to the general correlation matrix properties, symmetric with respect to all modes and contains no intermode or intramode  $x - p$  correlations (hence, only four parameters  $a$ ,  $b$ ,  $c$ , and  $d$  are needed to determine the matrix). However, the states of this form are, in general, biased with respect to  $x$  and  $p$  ( $a \neq b$ ). Only for a particular relation between the squeezing values  $(r_1, r_2)$  [18,19],

$$
e ^ {\pm 2 r _ {1}} = (N - 1) \sinh 2 r _ {2} \left[ \sqrt {1 + \frac {1}{(N - 1) ^ {2} \sinh^ {2} 2 r _ {2}}} \pm 1 \right], \tag {33}
$$

the states are unbiased (all diagonal entries of the correlation matrix being equal), thus having minimum energy at a given degree of entanglement or, in other words, maximum entanglement for a given mean photon number [39]. The other  $N$ -mode states of the family can be converted into the minimum-energy state via local squeezing operations [18,19,39]. Only for  $N = 2$ , we obtain  $r = r_1 = r_2$ . In this case, the matrix  $V^{(N)}$  reduces to that of a two-mode squeezed state which is the maximally entangled state of two modes at a given mean energy with the correlation matrix entries  $a = b = \cosh 2r$  and  $c = \sinh 2r = -d$ . For general  $N$ , the first squincer with  $r_1$  and the  $N - 1$  remaining squeezers with  $r_2$  have different squeezing. In the limit of large squeezing  $(\sinh 2r_2 \approx e^{+2r_2 / 2})$ , we obtain approximately [18,19]

$$
e ^ {+ 2 r _ {1}} \approx (N - 1) e ^ {+ 2 r _ {2}}. \tag {34}
$$

For the whole family of  $N$ -party  $N$ -mode states with the correlation matrix in Eq. (31), the quadrature combinations relevant for detecting genuine multiparty entanglement are [11,18,19]

$$
\begin{array}{l} \left\langle \left[ \Delta \left(\hat {x} _ {m} - \hat {x} _ {n}\right) \right] ^ {2} \right\rangle = e ^ {- 2 r _ {2}} / 2, \\ \left\langle \left[ \Delta \left(\hat {p} _ {m} + \hat {p} _ {n} + g ^ {(N)} \sum_ {j \neq m, n} ^ {N} \hat {p} _ {j}\right) \right] ^ {2} \right\rangle \\ = \frac {\left[ 2 + (N - 2) g ^ {(N)} \right] ^ {2}}{4 N} e ^ {- 2 r _ {1}} \\ + \frac {\left(g ^ {(N)} - 1\right) ^ {2} (N - 2)}{2 N} e ^ {+ 2 r _ {2}}. \tag {35} \\ \end{array}
$$

The total variances are then optimized (minimized) for

$$
g _ {\text {o p t}} ^ {(N)} = \frac {e ^ {+ 2 r _ {2}} - e ^ {- 2 r _ {1}}}{e ^ {+ 2 r _ {2}} + \frac {N - 2}{2} e ^ {- 2 r _ {1}}}. \tag {36}
$$

In the limit of infinite squeezing,  $r_1,r_2\to \infty$  , the above correlations correspond to a simultaneous eigenstate of the relative positions and the total momentum such as the CV GHZ states in Eq. (9).

Let us now examine how to experimentally verify the genuine multipartite entanglement of the CV GHZ-type states (in any case, it may be verified in an operational way by doing quantum teleportation between every pair of parties with the help of the remaining party [11]). Due to experimental imperfections, we may assume that the entanglement of slightly degraded approximate versions of the states, generated according to a scheme as in Figs. 1 and 2, is to be verified. We start again with only three parties and modes. For a simple check, look at the following set of inequalities:

$$
\begin{array}{l} I \left\langle \left[ \Delta (\hat {x} _ {1} - \hat {x} _ {2}) \right] ^ {2} \right\rangle + \left\langle \left[ \Delta (\hat {p} _ {1} + \hat {p} _ {2} + g _ {3} \hat {p} _ {3}) \right] ^ {2} \right\rangle \geqslant 1, \\ \left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left.\left. \hat {x} _ {2} - \hat {x} _ {3}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2}\right)\right] ^ {2} \right\rangle \geqslant 1, \\ \left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left. \right.\left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left. \right.\left. \right.\left. \right.\left. \right.\left.\left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left.\left.\left.\left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left.\left.\left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left.\left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {2}\right) + \left.\left. \hat {x} _ {1} - \hat {x} _ {3}\right) ] ^ {\prime 2}\right) + 1 .}}\right) + 1 .\right) + 1 .\right) + 1 .\right) + 1 .\right) + 1 .\right) + 1 .\right) + 1 . \\ \end{array}
$$

On the left-hand side (lhs) of condition I we have  $h_1 = -h_2 = g_1 = g_2 = 1$  and  $h_3 = 0$ , and hence the boundary for the total variance in Eq. (13) with Eq. (15) and Eq. (14) becomes 1 for  $(k, m, n) = (3, 1, 2)$  and  $(k, m, n) = (2, 3, 1)$ , but zero for  $(k, m, n) = (1, 2, 3)$ . Similarly, using the left-hand side of condition II where  $h_2 = -h_3 = g_2 = g_3 = 1$  and  $h_1 = 0$ , the boundary is 1 for  $(k, m, n) = (1, 2, 3)$  and  $(k, m, n) = (3, 1, 2)$ , but zero for  $(k, m, n) = (2, 3, 1)$ . Finally, the lhs of condition III with  $h_1 = -h_3 = g_1 = g_3 = 1$  and  $h_2 = 0$  corresponds to a boundary of 1 for  $(k, m, n) = (1, 2, 3)$  and  $(k, m, n) = (2, 3, 1)$ , but zero for  $(k, m, n) = (3, 1, 2)$ . Thus, the following statements for (at least partially) separable states hold,

$$
\hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 2} \otimes \hat {\rho} _ {i, 3}, \Rightarrow \mathrm {I I} \text {a n d} \mathrm {I I I},
$$

$$
\hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 3} \otimes \hat {\rho} _ {i, 2} \Rightarrow I a n d I I,
$$

$$
\hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 2 3} \otimes \hat {\rho} _ {i, 1} \quad \Rightarrow \mathrm {I} \text {a n d I I I}. \tag {38}
$$

The conditions in Eq. (37) are necessary for different kinds of partial separability. As a result, the violation of any pair of inequalities in Eq. (37) is sufficient for genuine three-party three-mode entanglement. Violating only one condition in Eq. (37) (for example, condition I) means that the total density operator cannot be written in two of the three forms in Eq. (38) (for example, neither in the form  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,13}\otimes \hat{\rho}_{i,2}$  nor in the form  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,23}\otimes \hat{\rho}_{i,1})$ . Using the classification of Ref. [30], the classes 3 [two-mode biseparable states expressible in two of the three forms in Eq. (38)], 4 [three-mode biseparable states expressible in all of the three forms in Eq. (38)], and 5 [fully separable states describable by Eq. (16)] are then ruled out. The forms of the classes 1 (fully inseparable states) and 2 [one-mode biseparable states expressible in one of the three forms in Eq. (38)] remain both possible. In our example with the violation of condition I, the state might be genuinely tripartite entangled or of the partially separable form  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,12}\otimes \hat{\rho}_{i,3}$ . Eventually, the violation of a second inequality in Eq. (37) (for instance, condition II) negates also the only remaining partially separable form (e.g.,  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,12}\otimes \hat{\rho}_{i,3}$ ), thus proving the full inseparability of the state [40]. Note that even though pure and totally symmetric multiparty entangled states are always genuinely multipartite entangled [18,19], asymmetric pure or mixed entangled three-mode states (e.g., from class 2 in Ref. [30], the product state of a bipartite entangled two-mode squeezed state and a vacuum state) and symmetric mixed entangled three-mode states (like the example for the three-mode biseparable class, class 4, given in Ref. [30]) do not automatically exhibit genuine tripartite entanglement. Due to the violation of two conditions in Eq. (37), the two loop-holes of partial separability, mixedness and/or asymmetry, are ruled out.

The criteria here are only sufficient for full inseparability and hence genuinely tripartite entangled states may also satisfy all the conditions in Eq. (37) (an example will be mentioned later). On the other hand, note that we did not use the assumption of Gaussian states. The derivation of the conditions relies only on the Cauchy-Schwarz inequality and Heisenberg's (sum) uncertainty relation.

Alternatively, one could simply check the known bipartite separability conditions [35] for pairs of modes, i.e.,  $g_{1} = g_{2} = g_{3} = 0$  in Eq. (37) (or using products of variances [38] instead of sums). Again, the statements of Eq. (38) hold. Hence, two violations again verify genuine tripartite entanglement. However, the significance of the more general conditions in Eq. (37) compared to those with  $g_{1} = g_{2} = g_{3} = 0$  is that for the CV GHZ-type states, as discussed later, the former can always be violated for any degree of multiparty entanglement and the violations can steadily grow from small towards "perfect" (that is all variances of the combi

nations zero) as the three-mode entanglement increases. In contrast, the bipartite conditions with  $g_{1} = g_{2} = g_{3} = 0$  may be violated for bad three-mode entanglement (small squeezing) and satisfied for larger squeezing, thus not always verifying genuine tripartite entanglement, and, in particular, never verifying good genuine tripartite entanglement. Moreover, they might be always violated, but the violations do not attain a significant amount (e.g., three-mode states made from one squeezed state [18,19]). Similarly, using products of variances [38] instead of sums in Eq. (37) with  $g_{1} = g_{2} = g_{3} = 0$ , violations may always occur, but also only to a certain extent [18,19]. In Figs. 1 and 2, it is shown how to apply the tripartite entanglement criteria experimentally using homodyne detectors.

Let us also discuss the conditions for the  $N = 4$  case in more detail. We consider the following set of six inequalities:

I  $\langle [\Delta (\hat{x}_1 - \hat{x}_2)]^2\rangle +\langle [\Delta (\hat{p}_1 + \hat{p}_2 + g_3\hat{p}_3 + g_4\hat{p}_4)]^2\rangle \geqslant 1,$  
II  $\langle [\Delta (\hat{x}_2 - \hat{x}_3)]^2\rangle +\langle [\Delta (g_1\hat{p}_1 + \hat{p}_2 + \hat{p}_3 + g_4\hat{p}_4)]^2\rangle \geqslant 1,$  
III  $\langle [\Delta (\hat{x}_1 - \hat{x}_3)]^2\rangle +\langle [\Delta (\hat{p}_1 + g_2\hat{p}_2 + \hat{p}_3 + g_4\hat{p}_4)]^2\rangle \geqslant 1,$  
IV  $\langle [\Delta (\hat{x}_3 - \hat{x}_4)]^2\rangle +\langle [\Delta (g_1\hat{p}_1 + g_2\hat{p}_2 + \hat{p}_3 + \hat{p}_4)]^2\rangle \geqslant 1,$  
V  $\langle [\Delta (\hat{x}_2 - \hat{x}_4)]^2\rangle +\langle [\Delta (g_1\hat{p}_1 + \hat{p}_2 + g_3\hat{p}_3 + \hat{p}_4)]^2\rangle \geqslant 1,$  
VI  $\langle [\Delta (\hat{x}_1 - \hat{x}_4)]^2\rangle +\langle [\Delta (\hat{p}_1 + g_2\hat{p}_2 + g_3\hat{p}_3 + \hat{p}_4)]^2\rangle \geqslant 1.$  (39)

The position and momentum variables  $\hat{x}_l$  and  $\hat{p}_l$  are the quadratures of four electromagnetic modes this time. The  $g_{l}$  are again arbitrary real parameters. Now the following statements for (at least partially) separable states hold,

$$
\begin{array}{l} \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 2 3} \otimes \hat {\rho} _ {i, 4} \Rightarrow \mathrm {I V}, \mathrm {V}, \text {a n d} \mathrm {V I}, \\ \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 2 4} \otimes \hat {\rho} _ {i, 3} \Rightarrow \mathrm {I I}, \mathrm {I I I}, \text {a n d I V}, \\ \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 3 4} \otimes \hat {\rho} _ {i, 2} \Rightarrow \mathrm {I}, \text {I I , a n d V}, \\ \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 2 3 4} \otimes \hat {\rho} _ {i, 1} \quad \Rightarrow \mathrm {I}, \text {I I I , a n d V I} \tag {40} \\ \end{array}
$$

and

$$
\begin{array}{l} \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 2} \otimes \hat {\rho} _ {i, 3 4} \Rightarrow \mathrm {I I}, \mathrm {I I I}, \mathrm {V}, \text {a n d V I}, \\ \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 3} \otimes \hat {\rho} _ {i, 2 4} \Rightarrow \mathrm {I}, \mathrm {I I}, \mathrm {I V}, \text {a n d} \mathrm {V I}, \\ \hat {\rho} = \sum_ {i} \eta_ {i} \hat {\rho} _ {i, 1 4} \otimes \hat {\rho} _ {i, 2 3} \quad \Rightarrow \mathrm {I}, \text {I I I , I V , a n d V .} \tag {41} \\ \end{array}
$$

Note that again the fully separable state,  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,1}\otimes \hat{\rho}_{i,2}$ $\hat{\rho}_{i,3}\otimes \hat{\rho}_{i,4}$ , is included and as well states such as  $\hat{\rho}$ $= \Sigma_{i}\eta_{i}\hat{\rho}_{i,km}\otimes \hat{\rho}_{i,l}\otimes \hat{\rho}_{i,n}$ . The above statements can be easily confirmed using Eq. (28) for states of the general form given in Eq. (25). The different forms here are  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,klm}\otimes \hat{\rho}_{i,n}$  including  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,kl}\otimes \hat{\rho}_{i,m}\otimes \hat{\rho}_{i,n}$ , and  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,km}\otimes \hat{\rho}_{i,ln}$  including  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,km}\otimes \hat{\rho}_{i,l}\otimes \hat{\rho}_{i,n}$ , with the two modes  $m$  and  $n$  always being separable. For the combinations  $\hat{u} = \hat{x}_m - \hat{x}_n$  and  $\hat{v} = g_k\hat{p}_k + g_l\hat{p}_l + \hat{p}_m + \hat{p}_n$ , the boundary of the total variance is always 1. The statements in Eqs. (40) and (41) become obvious then, by considering all possible pairs of modes  $(m,n)$  of the four modes  $(k,l,m,n)$ . Note that always when the two modes  $(m,n)$  are potentially entangled, the boundary for the total variance drops to zero.

What kind of violations of the six inequalities in Eq. (39) are now sufficient to verify the full inseparability of a four-mode, four-party state? The violations must rule out any of the partially separable forms in Eqs. (40) and (41). Let us, for example, consider violations of the inequalities IV and V. These violations mean that all partially separable forms in Eqs. (40) and (41) are excluded except for the form  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,234}\otimes \hat{\rho}_{i,1}$  in Eq. (40). In order to negate this form as well a further violation is needed. According to Eq. (40), one of the inequalities I, III, or VI should be violated in addition. Here it is important to realize that the conditions IV and V do not involve the  $x$  quadrature of mode 1, but that of all the other modes. The additional test via any one of the conditions I, III, or VI of which all contain both quadratures of mode 1, eventually provides the missing information about mode 1. Hence we learn that three conditions are sufficient here to verify the full inseparability of a four-mode, four-party state. We may choose

$$
\left\langle \left[ \Delta (\hat {x} _ {1} - \hat {x} _ {2}) \right] ^ {2} \right\rangle + \left\langle \left[ \Delta (\hat {p} _ {1} + \hat {p} _ {2} + g _ {3} \hat {p} _ {3} + g _ {4} \hat {p} _ {4}) \right] ^ {2} \right\rangle <   1,
$$

$$
\langle [ \Delta (\hat {x} _ {2} - \hat {x} _ {3}) ] ^ {2} \rangle + \langle [ \Delta (g _ {1} \hat {p} _ {1} + \hat {p} _ {2} + \hat {p} _ {3} + g _ {4} \hat {p} _ {4}) ] ^ {2} \rangle <   1,
$$

$$
\left\langle \left[ \Delta \left(\hat {x} _ {3} - \hat {x} _ {4}\right) \right] ^ {2} \right\rangle + \left\langle \left[ \Delta \left(g _ {1} \hat {p} _ {1} + g _ {2} \hat {p} _ {2} + \hat {p} _ {3} + \hat {p} _ {4}\right) \right] ^ {2} \right\rangle <   1, \tag {42}
$$

which involve both quadratures  $x$  and  $p$  of all four modes. Note that apart from the coefficients  $g_{l}$ , these four combinations correspond to those observables measured in a four-party CV GHZ state analyzer. Correspondingly, for  $N$  parties and modes, we may choose the following  $N - 1$  conditions in terms of effective  $N$  combinations (those of an  $N$ -party  $N$ -mode CV GHZ state analyzer):

$$
\begin{array}{l} \left\langle \left[ \Delta (\hat {x} _ {1} - \hat {x} _ {2}) \right] ^ {2} \right\rangle + \left\langle \left[ \Delta (\hat {p} _ {1} + \hat {p} _ {2} + g _ {3} \hat {p} _ {3} + \dots + g _ {N} \hat {p} _ {N}) \right] ^ {2} \right\rangle <   1, \\ \left\langle \left[ \Delta (\hat {x} _ {2} - \hat {x} _ {3}) \right] ^ {2} \right\rangle \\ + \left\langle \left[ \Delta \left(g _ {1} \hat {p} _ {1} + \hat {p} _ {2} + \hat {p} _ {3} + g _ {4} \hat {p} _ {4} + \dots + g _ {N} \hat {p} _ {N}\right) \right] ^ {2} \right\rangle <   1, \\ \end{array}
$$

： ： ： ： ： ： ：

![](images/b3b44cadae83da7e05469544e83910148c6a45429a60464f7bfa881b4fc19367.jpg)  
FIG. 3. Plot of the left-hand sides (total variance) of the conditions in Eq. (43) for different  $N$ -mode states with quadrature correlations given by Eq. (35) and different numbers of parties  $N = 3$  and  $N = 30$ . The states are those produced with one squeezed state (dotted lines with  $r_2 = 0$  and  $r = r_1$ ), those made from  $N$  equally squeezed states (dashed lines with  $r = r_1 = r_2$ ), and the unbiased minimum-energy states with squeezing  $r_1$  and  $r = r_2$  related as in Eq. (33).

$$
\begin{array}{l} \left\langle \left[ \Delta \left(\hat {x} _ {N - 1} - \hat {x} _ {N}\right) \right] ^ {2} \right\rangle \\ + \left\langle \left[ \Delta \left(g _ {1} \hat {p} _ {1} + g _ {2} \hat {p} _ {2} + \dots + g _ {N - 2} \hat {p} _ {N - 2} + \hat {p} _ {N - 1} + \hat {p} _ {N}\right) \right] ^ {2} \right\rangle \\ <   1. \tag {43} \\ \end{array}
$$

These conditions are sufficient to verify the full inseparability (genuine  $N$ -party entanglement) of an  $N$ -party  $N$ -mode state. For an arbitrary  $N$ , the proof relies on the fact that in any partially separable form, we may always select a distinct pair of modes  $(m,n)$  that are separable in the states  $i$  of the convex sum of the density operator. Only exploiting that modes  $m$  and  $n$  are separable, the combinations

$$
\hat {u} = \hat {x} _ {m} - \hat {x} _ {n}, \quad \hat {v} = \sum_ {j = 1} ^ {N - 2} g _ {k j} \hat {p} _ {k j} + \hat {p} _ {m} + \hat {p} _ {n} \tag {44}
$$

always yield a boundary of 1 for the total variance using Eq. (28) for states of the general form given in Eq. (25). By taking the pairs of modes  $(1,2)$ ,  $(2,3)$ , ...,  $(N - 1,N)$  for  $(m,n)$ , all partially separable forms of the total density operator are covered (as demonstrated explicitly for  $N = 4$ ) and hence the  $N - 1$  conditions in Eq. (43) are sufficient for genuine  $N$ -party,  $N$ -mode inseparability.

The left-hand sides of the inequalities in Eq. (43) are shown in Fig. 3 for various CV GHZ-type  $N$ -mode states, differing in the relation between the squeezing  $r_1$  and  $r_2$  [Eqs. (31), (32), and (35)]. Due to the total symmetry of all these states, the left-hand sides of the conditions in Eq. (43) become equal for all conditions (assuming  $g_j \equiv g^{(N)}$ ). Hence, values below the boundary 1, here mean all inequalities in Eq. (43) are satisfied: thus, indicating genuine  $N$ -party entanglement. In all these cases, in Fig. 3, the optimal coefficients  $g_j \equiv g_{\mathrm{opt}}^{(N)}$  from Eq. (36) are used to minimize the total variances of Eq. (35). If  $N = 30$ , only for the unbiased states, the conditions are always met (for any nonzero squeezing,  $r > 0$ ) and the total variances tend to zero for large squeezing. Moreover, for the same squeezing  $r$ , the unbiased states with  $N = 30$  drop below the boundary 1 to a greater extent

than their unbiased tripartite counterparts. In contrast, for the biased states (those with only one squeezeer,  $r_2 = 0$  and  $r = r_1$ , and those with  $N$  equally squeezed states,  $r = r_1 = r_2$ ), the total variances approach or even exceed the boundary 1 as the number of parties grows. The example of the states with  $N$  equal squeezers also demonstrates that there are Gaussian states that are indeed genuinely  $N$ -party entangled, but do not satisfy any of the conditions in Eq. (43). It can be shown, however, taking into account the symmetry and purity of the whole family of  $N$ -mode states (including those with  $N$  equal squeezers) that all these states are genuinely multiparty entangled for any nonzero squeezing [18,19].

Finally, we emphasize that one may use other conditions too for verifying the genuine multipartite entanglement of the CV GHZ-type states. Even a single condition might be again sufficient. For example, consider the combinations  $\hat{u} = 2\hat{x}_1 - (\hat{x}_2 + \hat{x}_3)$  and  $\hat{v} = \hat{p}_1 + \hat{p}_2 + \hat{p}_3$  for three modes. We have  $[\hat{u},\hat{v}] = 0$ , and indeed the GHZ-type three-mode state becomes a simultaneous eigenstate of  $\hat{u}$  and  $\hat{v}$  in the limit of infinite squeezing,  $r_1,r_2\to \infty$ . The boundaries of the total variance for these combinations take on the value 1 when  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,12}\otimes \hat{\rho}_{i,3}$  or  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,13}\otimes \hat{\rho}_{i,2}$ , and the value 2 (corresponding to the fully separable state) when  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,23}\otimes \hat{\rho}_{i,1}$ . Hence  $\langle (\Delta \hat{u})^2\rangle_\rho +\langle (\Delta \hat{v})^2\rangle_\rho < 1$  is sufficient for genuine tripartite entanglement. The number of measurements required, however, remain the same as for the criteria above expressed by  $N - 1$  conditions. In any case, both quadratures of all modes must be detected and combined in an appropriate way.

# IX. CONCLUSIONS

In summary, we proposed experimental criteria to detect genuine multipartite continuous-variable entanglement. These are expressed in terms of the variances of particular combinations of all the quadratures involved. The combinations are measurable with only a few simple homodyne detections. For Gaussian states, it is then not necessary to determine the entire correlation matrix in order to confirm the genuine multipartite entanglement. Furthermore, the conditions here do not rely on the assumption of Gaussian states.

In fact, in the two-party two-mode case, for instance, any state with a correlation matrix corresponding to an entangled Gaussian state is itself entangled, too [28]. An experimental confirmation of the Gaussian character of the state in question is therefore not needed either. Finally, we examined the applicability of the conditions to a particular GHZ-type class of genuinely multiparty entangled states. These states are of the Gaussian form, they are totally symmetric under exchange of modes, and they have zero cross correlations between the  $x$  and the  $p$  quadratures. If they are, in addition, unbiased between the  $x$  and the  $p$  quadratures, they always (for any nonzero entanglement) satisfy the conditions in terms of appropriately chosen linear combinations. In the limit of perfect entanglement, the variances of the combinations tend to zero for the unbiased states, and the conditions are perfectly met.

In an experiment, one normally has approximate a priori knowledge about the state to be analyzed. According to this a priori knowledge, one can then choose appropriate linear combinations to be measured. It would be desirable to know whether there is always, for any given multiparty, multimode state, a single optimal condition to verify its genuine multipartite entanglement and how to constructively derive this condition. Inferring from the results here, such a condition may always exist and the corresponding linear combinations must contain both quadratures of all modes with optimized coefficients  $h_{l}$  and  $g_{l}$ . A possible approach to this question is in terms of so-called entanglement witnesses [26,41]. One may then interpret the inequalities for the total variances as quantum expectation values of Hermitian operators which take on negative values when they witness some kind of partial inseparability.

# ACKNOWLEDGMENTS

P.v.L. is grateful to Masahide Sasaki, Masahiro Takeoka, Marcos Curty, Norbert Lütkenhaus, Geza Giedke, and Samuel Braunstein for useful discussions. He also would like to acknowledge the kind hospitality of the groups at the University of Tokyo and the Communications Research Laboratory (CRL) Tokyo. A.F. acknowledges the financial support of MPHPT and MEXT of Japan. P.v.L. thanks CRL for funding a research visit. He also acknowledges the financial support of the DFG under the Emmy-Noether program.

[1] C.H. Bennett et al., Phys. Rev. Lett. 70, 1895 (1993).  
[2] C.H. Bennett and S.J. Wiesner, Phys. Rev. Lett. 69, 2881 (1992).  
[3] C.H. Bennett and G. Brassard, in Proceedings IEEE International Conference on Computers, Systems and Signal Processing (IEEE Press, Los Alamitos, Calif. 1984), p. 175.  
[4] A.K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[5] C.H. Bennett, G. Brassard, and N.D. Mermin, Phys. Rev. Lett. 68, 557 (1992).  
[6] M. Murao et al., Phys. Rev. A 59, 156 (1999).  
[7] M. Hillary, V. Buzek, and A. Berthiaume, Phys. Rev. A 59, 1829 (1999).

[8] M. Fitzi, N. Gisin, and U. Maurer, Phys. Rev. Lett. 87, 217901 (2001).  
[9] A. Furusawa et al., Science (Washington, DC, U.S.) 282, 706 (1998).  
[10] J. Jing et al., e-print quant-ph/0210132 2002.  
[11] P. van Loock and S.L. Braunstein, Phys. Rev. Lett. 84, 3482 (2000).  
[12] J. Eisert, S. Scheel, and M.B. Plenio, Phys. Rev. Lett. 89, 137903 (2002).  
[13] J. Fiurasek, Phys. Rev. Lett. 89, 137904 (2002).  
[14] G. Giedke and J.I. Cirac, Phys. Rev. A 66, 032316 (2002).  
[15] N. Lütkenhaus, J. Calsamiglia, and K.A. Suominen, Phys. Rev.

A 59, 3295 (1999).  
[16] E. Knill, R. Laflamme, and G.J. Milburn, Nature (London) 409, 46 (2001).  
[17] S.L. Braunstein and H.J. Kimble, Phys. Rev. Lett. 80, 869 (1998).  
[18] P. van Loock, Fortschr. Phys. 50, 12 1177 (2002).  
[19] P. van Loock and S.L. Braunstein, in Quantum Information Theory with Continuous Variables, edited by A.K. Pati and S.L. Braunstein (Kluwer, Dordrecht, 2002).  
[20] M. Seevinck and J. Uffink, Phys. Rev. A 65, 012107 (2001).  
[21] N.D. Mermin, Phys. Rev. Lett. 65, 1838 (1990).  
[22] D.N. Klyshko, Phys. Lett. A 172, 399 (1993); N. Gisin and H. Bechmann-Pasquinucci, ibid. 246, 1 (1998).  
[23] K. Banaszek and K. Wodkiewicz, Phys. Rev. A 58, 4345 (1998).  
[24] P. van Loock and S.L. Braunstein, Phys. Rev. A 63, 022106 (2001).  
[25] A. Peres, Phys. Rev. Lett. 77, 1413 (1996).  
[26] M. Horodecki, P. Horodecki, and R. Horodecki, Phys. Lett. A 223, 1 (1996).  
[27] R. Simon, Phys. Rev. Lett. 84, 2726 (2000).  
[28] R.F. Werner and M.M. Wolf, Phys. Rev. Lett. 86, 3658 (2001).  
[29] U. Leonhardt, Measuring the Quantum State of Light (Cambridge University Press, Cambridge, 1997).  
[30] G. Giedke et al., Phys. Rev. A 64, 052303 (2001).  
[31] H. Weyl, The Theory of Groups and Quantum Mechanics (Dover, New York, 1950).  
[32] M.S. Kim, Jinhyoung Lee, and W.J. Munro, Phys. Rev. A 66, 030301(R) (2002).

[33] G. Vidal and R.F. Werner, Phys. Rev. A 65, 032314 (2002).  
[34] G. Giedke et al., Phys. Rev. Lett. 87, 167904 (2001).  
[35] L.-M. Duan et al., Phys. Rev. Lett. 84, 2722 (2000).  
[36] Akira Furusawa and H.J. Kimble, in Quantum Information Theory with Continuous Variables, edited by A.K. Pati and S.L. Braunstein (Kluwer, Dordrecht, 2002).  
[37] V. Giovannetti et al., Phys. Rev. A 67, 022320 (2003).  
[38] S.M. Tan, Phys. Rev. A 60, 2752 (1999).  
[39] W.P. Bowen, P.K. Lam, and T.C. Ralph, J. Mod. Opt. 50, 801 (2003).  
[40] In fact, the data of the experiment reported in Ref. [10] are also consistent with mixtures of entangled two-mode states and a separable third mode, for example,  $\hat{\rho} = \Sigma_{i}\eta_{i}\hat{\rho}_{i,12}\otimes \hat{\rho}_{i,3}$ . The improvement in the performance of "controlled dense coding" between the two entangled parties due to classical information about one quadrature (say  $\hat{p}_3$ ) of the third mode/party can be explained solely by classical correlations between the third mode and the entangled pair. Although the states produced in Ref. [10] certainly are genuinely tripartite entangled, the experimental verification of this genuine tripartite entanglement is incomplete. The additional measurement required for the complete verification corresponds to the violation of a second inequality, for instance condition II in Eq. (37), involving also the conjugate quadrature (say  $\hat{x}_3$ ) of the third mode. Operationally, this would mean that an additional "controlled dense coding" between a second pair of modes (for example, modes 2 and 3) must be demonstrated.  
[41] B.M. Terhal, Phys. Lett. A 271, 319 (2000).