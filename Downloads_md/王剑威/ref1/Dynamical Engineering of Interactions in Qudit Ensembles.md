# Dynamical Engineering of Interactions in Qudit Ensembles

Soonwon Choi, $^{1}$  Norman Y. Yao, $^{2}$  and Mikhail D. Lukin $^{1}$

$^{1}$ Department of Physics, Harvard University, Cambridge, Massachusetts 02138, USA

$^{2}$ Department of Physics, University of California Berkeley, Berkeley, California 94720, USA

(Received 11 April 2017; published 3 November 2017)

We propose and analyze a method to engineer effective interactions in an ensemble of  $d$ -level systems (quids) driven by global control fields. In particular, we present (i) a necessary and sufficient condition under which a given interaction can be decoupled, (ii) the existence of a universal sequence that decouples any (cancelable) interaction, and (iii) an efficient algorithm to engineer a target Hamiltonian from an initial Hamiltonian (if possible). We illustrate the potential of this method with two examples. Specifically, we present a 6-pulse sequence that decouples effective spin-1 dipolar interactions and demonstrate that a spin-1 Ising chain can be engineered to study transitions among three distinct symmetry protected topological phases. Our work enables new approaches for the realization of both many-body quantum memories and programmable analog quantum simulators using existing experimental platforms.

DOI: 10.1103/PhysRevLett.119.183603

The controlled manipulation of quantum systems with pulsed coherent fields is important in nearly all branches of quantum science. The techniques associated with dynamical coherent control have a long and storied history, originating in nuclear magnetic resonance (NMR), where periodic sequences of control pulses enable the isolation of nuclear spins from unwanted external noise sources [1]. Over the past few decades, advanced techniques have been developed with goals ranging from frequency-selective decoupling to higher-order error suppression, and applications ranging from metrology to information processing [2-14].

Periodic control pulses can also be used to engineer many-body interactions. In particular, they can enable the realization of driven (Floquet) systems that exhibit phenomena richer than the original system without dynamical control [15-21]. This approach falls under the moniker of average Hamiltonian theory [22], a term prevalent in the context of solid-state NMR, where sequences of spin rotations are used to modify the intrinsic interactions between magnetic dipoles [22,23]. A particularly powerful example is the celebrated WAHUHA pulse sequence [23] which cancels the dipole-dipole interaction between spin-  $1 / 2$  particles and has been extensively utilized in systems ranging from solid-state spin defects to ultracold polar molecules [7,24]. More generally, pulsed periodic driving has enabled the experimental exploration of a variety of exotic many-body quantum phenomena including dynamical phase transitions, quantum chaos, glassy dynamics in disordered systems, and discrete time-crystalline order [25-29]. While the majority of existing pulse sequences are designed to engineer Hamiltonians constructed from spin-  $1 / 2$  or qubitlike systems [30-33], recent experimental progress has opened the door to the manipulation of many-body qudit systems, whose basic degrees of freedom possess  $d$  internal states. Indeed, in platforms ranging from trapped ions and Rydberg atoms to

superconducting qubits and solid-state spin defects, coherent interactions among multiple qubits have already been observed [24,29,34]. This enables the study of quantum many-body qudit systems that can exhibit phenomena qualitatively distinct from their spin-1/2 counterparts, such as generalized Potts model and parafermionic topological phases [35-38]. Generalizing Hamiltonian engineering methods to qudit systems may enable exploration of such unique phenomena with important potential applications in areas such as quantum simulations.

In this Letter, we report two advances toward this goal. First, we present a complete generalization of the WAHUHA pulse sequence for an arbitrary qudit system. We derive a necessary and sufficient condition that diagnoses when generic interactions can be canceled. Moreover, we prove the existence of a universal pulse sequence that decouples any cancelable interaction. This result implies that locally encoded quantum information can be protected even in a strongly interacting qudit ensemble. As an example, we present a novel pulse sequence that decouples spin-1 dipolar interactions. Second, we present an algorithm that determines when a given initial Hamiltonian  $H_0$  can be mapped to a desired final Hamiltonian  $H_f$ , using a predetermined set of global pulses. Such a technique provides a recipe to transform an interacting many-body system into a programmable analog quantum simulator [33]. In this context, we demonstrate that a spin-1 classical Ising chain can be directly mapped to a family of Hamiltonians whose ground states include a variety of symmetry protected topological (SPT) phases. In both cases, we consider an ensemble of  $d$ -level systems with generic pairwise interactions and assume that only global  $SU(d)$  manipulations are available. This setting is ubiquitous and particularly relevant to recent experimental developments in a variety of platforms [24-29,39-42]. We note that in the case where quuds can be independently

addressed and controlled, arbitrary modifications of the underlying interactions are possible [32,33,43-45]; however, such precise individual controls are typically challenging to implement in strongly interacting many-body systems.

We consider an  $N$  qudit system with Hamiltonian,

$$
H = \sum_ {i j} J _ {i j} h _ {i j}, \tag {1}
$$

where  $h_{ij}$  represents a homogeneous two-qudit interaction between  $i$  and  $j$ , and the scalars  $J_{ij}$  fully characterize the geometry, range and strength of the interactions. Hamiltonian evolution is interspersed with a rapid and repeated sequence of  $k$  pulses, denoted  $P_i$ . More specifically, each pulse is followed by free evolution under  $H$  for a duration  $\tau_i$ . Assuming that the manipulations are sufficiently fast, one can rewrite the (Floquet) unitary evolution over one such  $k$  cycle as

$$
U (T) = e ^ {- i H \tau_ {k}} P _ {k} \dots e ^ {- i H \tau_ {2}} P _ {2} e ^ {- i H \tau_ {1}} P _ {1}, \tag {2}
$$

where  $T = \sum_{i=1}^{k} \tau_i$  is the total time duration of the cycle. At integer multiples of the driving period  $T$ , the time evolution is captured by an effective Hamiltonian  $H_{\mathrm{eff}}$ , defined by  $U(T) = \exp(-iH_{\mathrm{eff}}T)$ .

In the case of both dynamical decoupling and Hamiltonian engineering, the key idea is to design a finite pulse sequence such that  $H_{\mathrm{eff}}$  approximates a desired target Hamiltonian. Defining  $U_{i} \equiv P_{i}P_{i - 1}\dots P_{2}P_{1}$  and  $U_0 \equiv \mathbb{I}$ , one can rewrite Eq. (2) as

$$
U (T) = e ^ {- i \bar {H} _ {k} \tau_ {k}} \dots e ^ {- i \bar {H} _ {2} \tau_ {2}} e ^ {- i \bar {H} _ {1} \tau_ {1}}, \tag {3}
$$

where  $\bar{H}_i = U_i^\dagger HU_i$  [46]. By moving into this so-called toggling frame [22], the pulsed unitary dynamics [Eq. (2)] can be described by continuous evolution under a time-dependent Hamiltonian. Recently, it has been shown that  $H_{\mathrm{eff}}$  can be approximated by a controlled Magnus expansion in the high frequency limit, leading to an effective Hamiltonian description valid up to exponentially long times [47-50]. In particular, for a driving frequency,  $\omega = 2\pi /T$ , that is large compared to local energy scales  $\sim J$ ,  $H_{\mathrm{eff}} \simeq \sum_{q=0}^{q*}(J/\omega)^q H_{\mathrm{eff}}^{(q)}$ , where  $H_{\mathrm{eff}}^{(q)}$  denotes the qth order term while  $q*$  is the maximum order beyond which heating effects become non-negligible. Here, we assume a rapid pulse sequence satisfying  $\omega \gg J$  and focus on the leading order effective Hamiltonian,

$$
H _ {\text {e f f}} \approx H _ {\text {e f f}} ^ {(0)} = \sum_ {i} \frac {\tau_ {i}}{T} \bar {H} _ {i}. \tag {4}
$$

Once a desired pulse sequence is found, one can always symmetrize it such that the next order correction  $H_{\mathrm{eff}}^{(1)}$  also vanishes, leaving only a strongly suppressed second order ( $q \geq 2$ ) contribution [51]. From the linearity of Eq. (4), we only need to consider a single term  $h_{ij}$  and hence omit the qudit indices below.

Consistent with the control available in many-body quudit systems, we focus on the case where one can only apply global single-qudit rotations, i.e.,  $P_{i} = p_{i}^{\otimes N}$  for some  $p_i\in SU(d)$ . To represent the interactions, we use a trace orthonormal operator basis  $\{\lambda_{\mu}\}$  with  $\mathrm{tr}[\lambda_\mu \lambda_\nu ] = 2\delta_{\mu \nu}$ . In this basis, the most general two-qudit interaction can be written as

$$
h = \sum_ {\mu \nu} C _ {\mu \nu} \lambda_ {\mu} \otimes \lambda_ {\nu}. \tag {5}
$$

Hermicity and the exchange symmetry imply that  $C$  is a real symmetric  $m \times m$  matrix with  $m = d^2 - 1$ . For a given  $h$ , the matrix  $C$  can be explicitly obtained using  $C_{\mu \nu} = \mathrm{tr}[h\lambda_{\mu} \otimes \lambda_{\nu}] / 4$ .

Interaction decoupling.—We now derive a necessary and sufficient condition for the full decoupling of an interacting qudit Hamiltonian.

Theorem 1. For a given two-qudit interaction  $h$ , there exists a finite sequence  $\{p_i\} \subset SU(d)$ , or, equivalently,  $\{u_i\} \subset SU(d)$ , and  $\{\tau_i\} \subset \mathbb{R}^+$ , such that  $h_{\mathrm{eff}} = \sum_i(\tau_i / T)(u_i^\dagger \otimes u_i^\dagger)h(u_i \otimes u_i) = 0$  if and only if the  $C$  matrix of  $h$  is traceless, i.e.,  $\operatorname{tr}[C] = \sum_{\mu}\operatorname{tr}[h\lambda_{\mu} \otimes \lambda_{\mu}] / 4 = 0$ .

Proof. For convenience we work with interactions represented as  $C$  matrices, whose transformation under a unitary rotation  $u_{i} \otimes u_{i}$  is given by

$$
\begin{array}{l} \sum_ {\mu \nu} C _ {\mu \nu} \lambda_ {\mu} \otimes \lambda_ {\nu} \mapsto \sum_ {\mu \nu} C _ {\mu \nu} \left(u _ {i} ^ {\dagger} \lambda_ {\mu} u _ {i}\right) \otimes \left(u _ {i} ^ {\dagger} \lambda_ {\nu} u _ {i}\right) (6) \\ \equiv \sum_ {\mu \nu} C _ {\mu \nu} ^ {(i)} \lambda_ {\mu} \otimes \lambda_ {\nu}, (7) \\ \end{array}
$$

where the coefficients  $C_{\mu \nu}^{(i)}$  are defined by the equality above. More specifically, two matrices  $C^{(i)}$  and  $C$  are related by the transformation  $C^{(i)} = (O^i)^T CO^i$ , where  $O_{\nu/\nu}^i \equiv \frac{1}{2}\mathrm{tr}[\lambda_\nu u_i^\dagger \lambda_{\nu'}u_i]$ . Taking into account the full sequence of unitary pulses yields the  $C$  matrix for the effective Hamiltonian as

$$
C _ {\text {e f f}} = \sum_ {i} \alpha_ {i} (O ^ {i}) ^ {T} C O ^ {i}. \tag {8}
$$

where  $\alpha_{i} = \tau_{i} / T$  characterizes the relative time scale of the various intermediary free evolutions. Intuitively, Eq. (8) demonstrates that the effective interaction is simply given by a weighted average of "rotated" versions of the original interaction. Indeed, it can be easily shown that  $O^i$  is a real orthogonal matrix.

First, one immediately sees that the trace of  $C$  is preserved. Thus, it is necessary for the original  $C$  matrix to be traceless in order for the effective Hamiltonian to be fully decoupled. Second, this also naturally suggests a decomposition of a general interaction into two components: an isotropic part with nonzero trace and a traceless anisotropic part. Since  $C$  is a real-symmetric matrix, there exists only one linearly independent isotropic component, which is proportional to the identity matrix. The corresponding two-qudit interaction

is  $h_{\mathrm{iso}} \propto \sum_{\mu} \lambda_{\mu} \otimes \lambda_{\mu}$ . Equation (8) shows that any isotropic interaction cannot be modified by global pulses as it is invariant under  $SU(d)$  rotations.

To prove sufficiency, we construct a pulse sequence that explicitly cancels any interaction  $(C_{\mathrm{eff}} = 0)$  given that the interaction is purely anisotropic. The design principle of this "universal decoupling" sequence is simple: find a finite set of  $\{u_i\}$ , where the corresponding  $\{O^i\}$  are distributed among all possible rotations such that their weighted average vanishes; this strategy is reminiscent of unitary 2-designs, but here, we have one additional control knob, corresponding to the choices of  $\alpha_{i}$ . Interestingly, a very related problem has been already studied in quantum information science. In Ref. [57], Dur et al. introduce a depolarization superoperator  $\mathcal{D}$  that acts on a density matrix  $\rho$  of a two-qudit system

$$
\mathcal {D} (\rho) = A _ {d} \frac {\operatorname {t r} [ A _ {d} \rho ]}{\operatorname {t r} [ A _ {d} ]} + S _ {d} \frac {\operatorname {t r} [ S _ {d} \rho ]}{\operatorname {t r} [ S _ {d} ]}, \tag {9}
$$

where  $S_{d}(A_{d})$  is the projector onto even(odd) eigenspace of the exchange operator  $\Pi_{d} = \sum_{i,j=1}^{d} |ij\rangle \langle ji|$ , i.e.,  $A_{d} = (\mathbb{I} - \Pi_{d}) / 2$  and  $S_{d} = 1 - A_{d} = (\mathbb{I} + \Pi_{d}) / 2$ . It is shown, by explicit construction, that  $\mathcal{D}(\cdot)$  can be implemented by a finite sequence of probabilistic bilocal operations,  $\sum_{i=1}^{k} p_{i}(v_{i}^{\dagger} \otimes v_{i}^{\dagger}) \rho(v_{i} \otimes v_{i}) = \mathcal{D}(\rho)$ , where  $\{p_{i}\}$  is a probability distribution and  $\{v_{i}\} \subset SU(d)$ . Here, we reinterpret the superoperator as a dynamical decoupling sequence via the mapping:  $p_{i} \to \alpha_{i}$  and  $v_{i} \to u_{i}$ . To show that this is a universal decoupling sequence, we demonstrate that for an arbitrary interaction  $h$ ,  $\mathrm{tr}[S_d h] = -\mathrm{tr}[A_d h] = \mathrm{tr}[C]$ ; thus,  $\mathrm{tr}[C] = 0$  implies  $\mathcal{D}(h) = 0$ . The proof is simple: for  $h$  acting on qubits  $A$  and  $B$ ,

$$
\begin{array}{l} \operatorname {t r} \left[ h \Pi_ {d} \right] = \sum_ {\mu \nu i j} C _ {\mu \nu} \operatorname {t r} \left[ \lambda_ {\mu} ^ {A} \otimes \lambda_ {\nu} ^ {B} | i j \rangle \langle j i | \right] (10) \\ = \sum_ {\mu \nu i j} C _ {\mu \nu} \left\langle j _ {A} \mid \lambda_ {\mu} ^ {A} \mid i _ {A} \right\rangle \left\langle i _ {B} \mid \lambda_ {\nu} ^ {B} \mid j _ {B} \right\rangle (11) \\ = \sum_ {\mu \nu} C _ {\mu \nu} \operatorname {t r} \left[ \lambda_ {\mu} \lambda_ {\nu} \right] = 2 \operatorname {t r} [ C ], (12) \\ \end{array}
$$

where we have explicitly dropped the qudit indices and the tensor product [Eq. (12)] to emphasize that  $\lambda_{\mu (\nu)}$  are matrices. Finally, noting that  $\mathrm{tr}[h] = \sum_{\mu \nu}\mathrm{tr}[\lambda_\mu^A\otimes \lambda_\nu^B ] = 0$  we obtain  $\mathrm{tr}[S_d h] = -\mathrm{tr}[A_d h] = \mathrm{tr}[h\Pi_d] / 2 = \mathrm{tr}[C]$ , which completes the proof of Theorem 1.

Hamiltonian engineering.-The previous case of interaction decoupling can be viewed as a specific example of a more general question: given an initial set of interactions  $h_0$ , a target Hamiltonian  $h_f$  and a finite set of available unitaries  $\mathcal{U}$ , is there a pulse sequence such that  $\sum_{i} (\tau_i / T)(u_i^\dagger \otimes u_i^\dagger) h_0(u_i \otimes u_i) = \beta h_f$  for a constant  $\beta > 0$ ? If so, is there an efficient algorithm to construct the desired pulse sequence? In what follows we describe such an algorithm.

Let us begin by rewriting  $h_0$  and  $h_f$  in their corresponding  $C$  matrices  $C_0$  and  $C_f$ . We denote the strengths of their isotropic components as  $s_0 = \mathrm{tr}[C_0]$  and  $s_f = \mathrm{tr}[C_f]$ . As previously discussed, if only one of their  $C$  is traceless,  $h_0$  cannot be mapped to  $h_f$  since the isotropic components can never be decoupled by any pulse sequence. We will now divide our analysis into two cases: (i)  $s_0 = s_f = 0$  and (ii)  $s_0, s_f \neq 0$  (Fig. 1).

Case (i) [Fig. 1(a)]: Our strategy is to cancel the portion of the interaction that is orthogonal to  $C_f$  while maximizing the strength of the remaining piece. To illustrate this idea more clearly, we introduce a vector representation of interactions

$$
(\vec {w}) _ {a} \equiv \operatorname {t r} [ C \eta_ {a} ] / 2, \tag {13}
$$

using a matrix basis  $\{\eta_{a}\}$  of dimension  $m = d^{2} - 1$ . In this representation, Eq. (8) becomes  $\vec{w}_{\mathrm{eff}} = \sum_{i}\alpha_{i}M^{i}\vec{w}$  with  $M_{ab}^{i}\equiv \frac{1}{2}\mathrm{tr}[\eta_{a}(O^{i})^{T}\eta_{b}O^{i}]$ . Our objective is to maximize  $\vec{w}_{\mathrm{eff}}\cdot \vec{w}_f$  while satisfying  $\vec{w}_{\mathrm{eff}}\cdot P_{\perp} = 0$ , where  $\vec{w}_q$  ( $q\in \{0,f\}$ ) is the vector representation of  $C_q$  and  $P_{\perp}$  is the projector on to a space that is orthogonal to  $\vec{w}_f$ , i.e.,  $(P_{\perp})_{ab} = \delta_{ab} - (\vec{w}_f)_a(\vec{w}_f)_b / |\vec{w}_f|^2$ . Interestingly, this task can naturally be cast into the canonical form of linear programming, i.e., maximize  $\sum_{i}\alpha_{i}\vec{w}_{f}\cdot M^{i}\vec{w}_{0}$  with respect to  $\{\alpha_i\}$  under constraints  $\sum \alpha_{i}P_{\perp}M^{i}\vec{w}_{0} = 0$ ,  $\sum \alpha_{i} = 1$ , and  $\alpha_{i}\geq 0$  [58].

Case (ii) [Fig. 1(b)]: In this case, the contributions from the isotropic components cannot be ignored, and they fix the rescaling parameter,  $\beta = s_0 / s_f$ . Thus, one has to not only engineer the "shape" of the anisotropic interaction but also adjust its strength to match with the fixed  $\beta$ . Now our strategy is to decompose the given interaction into

![](images/74d8472c09c0c88fd57797e72612410b54510710a8f3c8a21153bcd4f6b69420.jpg)  
(a) Purely anisotropic

![](images/eb5081dda22870421ccaafaf438e40bc379d60d52a9060cf97be482e5271a8c4.jpg)  
(b)  
FIG. 1. Schematic diagram of interaction engineering. Black solid, red dotted, and blue dashed lines indicate full interactions, isotropic components, and anisotropic components, respectively. Dotted arrows represent applications of the dynamical decoupling sequence. (a) When both source and target interactions are purely anisotropic ( $s_0 = s_f = 0$ ), one directly maps interactions. (b) For interactions with both isotropic and anisotropic components, one engineers only the anisotropic component and matches the relative strength by canceling some fraction.

three pieces: an isotropic part, a fraction of the anisotropic part to be modified, and the remaining portion to be canceled. To this end, one is searching for two pulse sequences,  $\mathcal{P}_1 = (\{\tau_i^1\}, \{u_i^1\})$ , which maps  $\bar{C}_0 \mapsto \beta^*\bar{C}_f$  and  $\mathcal{P}_2 = (\{\tau_i^2\}, \{u_i^2\})$ , which cancels  $\bar{C}_0 \mapsto 0$ . Here,  $\bar{C}_q$  ( $q \in \{0, f\}$ ) is the anisotropic component of  $C_q$  and  $\beta^*$  is the maximum possible strength. As before, one can use linear programming to efficiently find these sequences. If both maps are possible and the engineered interaction strength is sufficiently strong  $\beta^* \geq \beta$ , one can concatenate two sequences to form  $\mathcal{P}_3 = (\{\beta/\beta^*\} \tau_i^1, (1 - \beta/\beta^*) \tau_i^2$ ,  $\{u_i^1, u_i^2\}$ ), which maps  $C_0 \mapsto \beta C_f$ .

Decoupling spin-1 dipolar interactions. We now turn to two examples. First, we present a 6-pulse sequence that decouples effective dipole-dipole interactions  $H_{d} = \sum J_{ij}h_{ij}^{d}$  in an ensemble of spin-1 particles (states  $\{|\pm 1\rangle ,|0\rangle \}$ ) with anharmonic level spacings [39],

$$
\begin{array}{l} h ^ {d} = \sum_ {a = 1} ^ {2} \left(X _ {a} \otimes X _ {a} + Y _ {a} \otimes Y _ {a}\right) \\ - \left(Z _ {1} + Z _ {2}\right) \otimes \left(Z _ {1} + Z _ {2}\right), \tag {14} \\ \end{array}
$$

where  $X_{a}$ ,  $Y_{a}$ , and  $Z_{a}$  are Pauli matrices associated with two different transitions,  $|0\rangle \leftrightarrow | + 1\rangle (a = 1)$  and  $|0\rangle \leftrightarrow |-1\rangle (a = 2)$ , of a single spin-1 particle [see Fig. 2(a)] [51]. Such a Hamiltonian is ubiquitous in quantum optical systems and arises in the context of ultracold polar molecules, NV centers, and quadrupolar nuclear spins [11,24,29]. While the solution for the analogous question in dipolar spin-1/2 systems has been known for a half-century (e.g., WAHUHA), the spin-1 problem remains an open question.

Motivated by typical experimental constraints, we assume that the available manipulations are limited to a set of composite pulses constructed from up to four  $\pm \pi$  or  $\pm (\pi /2)$  pulses between any of the three transitions with two different phases [Fig. 2(a)]. Using a linear programming algorithm, we find an explicit decoupling sequence using only 6 pulses  $\{P_1,\dots P_6\}$  with equal time durations  $\tau_{i} = T / 6$  as depicted in Fig. 2(b). Explicit expressions for these pulses are provided in the Supplemental Material [51]. In order to test our sequence, we simulate the dynamics of  $N = 6$  spin-1 particles with random interaction strengths  $J_{ij}\in [-J,J]$  between every pair. We compute the Floquet unitary  $U_{T}\equiv P_{6}e^{-iH_{d}T / 6}P_{5}\dots P_{1}e^{-iH_{d}T / 6}$  and generate stroboscopic time evolution via  $(U_T)^n$  with  $n\in \mathbb{Z}$ . We introduce the fidelity  $\mathcal{F}(nT)\equiv |\mathrm{tr}[(U_T)^n ] / D|^2$  where  $D = 3^{N}$  is the dimension of the Hilbert space. Since  $\mathcal{F}(t) = 1$  if and only if the evolution corresponds to the identity, the decay of  $\mathcal{F}$  serves as a conservative measure for the performance of our decoupling sequence.

Figure 2(c) depicts  $\mathcal{F}(t)$  for various values of  $T$ , demonstrating that the evolution remains trivial up to

![](images/3fb401269ff92e3e51701c86a5749fcfece09a46f70963b27f925d04404e76d4.jpg)  
(a)

![](images/0ea3929b700e41121b75918299214e5a1156c6353a3f81771c833b2335263d4d.jpg)  
(c)

![](images/cd778404f84aa9316ae31b9686e69dfb50e98aa0a61dced772b6a5c97b5cca94.jpg)  
(b)

![](images/d639e33f826fbb2c407c641df848b96929e396ff0251b8204256d2e7d436e2e1.jpg)  
(d)

![](images/d4fa309f717ecdd63bea81d4860e928ee6f017d3990a623e7531200bcbb9507c.jpg)  
FIG. 2. (a) Level diagram for an anharmonic three level system. (b) Decoupling sequence for spin-1 dipolar interactions. Pulse durations are indicated by rotation angles, and phase choices are color coded. (c) Numerical simulations of decoupling dipolar interactions among  $N = 6$  spin-1 particles. Black solid line indicates  $\mathcal{F}(t)$  in the absence of the pulse sequence. Blue, red, and yellow solid lines correspond to  $\mathcal{F}(t)$  under a decoupling sequence with  $1 / JT = 3,5,10$ , respectively. Dashed lines are for symmetrized sequences. (d) Two generators  $\{a,x\}$  of the symmetry group  $A_4$ . (e) Phase diagram. Three SPT phases (I, II, and III) are distinguished by the transformation of ground state wave functions under the action of  $a \in A_4$ . The colored area indicates the domain of  $(p,q)$  that can be engineered from Ising interactions. Blue dot indicates the AKLT point  $(p,q) = (1/3,0)$ .  
(e)

$\sim 10 / J$  for  $JT < 1$ . Once a given decoupling sequence is found, one can always symmetrize it to further suppress the leading order correction in Magnus expansion [51]. In our case, such a sequence involves 10 pulses within the period  $2T$ . As shown in Fig. 2(c), the symmetrized sequence significantly suppresses the interaction for time scales up to  $\sim 100 / J$ .

Engineering SPT Hamiltonians. As a second example, we show that a spin-1 chain with nearest neighbor Ising interactions can be directly mapped to a family of SPT Hamiltonians [51]. More specifically, given a basic Ising interaction  $H_{I} = \sum_{i}S_{i}^{z}S_{i + 1}^{z}$ , one can engineer a two-parameter family of Hamiltonians  $H(p,q) = H_{1} + pH_{2} + qH_{3}$  with

$$
H _ {1} = \sum_ {i} \vec {S} _ {i} \cdot \vec {S} _ {i + 1}, \quad H _ {2} = \sum_ {i} (\vec {S} _ {i} \cdot \vec {S} _ {i + 1}) ^ {2},
$$

$$
H _ {3} = \sum_ {i} \sum_ {(a, b, c) \in S _ {3}} \left(S _ {i} ^ {a} S _ {i} ^ {b} S _ {i + 1} ^ {c} + S _ {i} ^ {a} S _ {i + 1} ^ {b} S _ {i + 1} ^ {c}\right),
$$

where  $p, q \in \mathbb{R}$ ,  $\vec{S}_i = (S_i^x, S_i^y, S_i^z)$  is the spin-1 vector operator, and  $\sum_{(a,b,c) \in S_3}$  indicates the summation over all permutations of  $(x,y,z)$ . The symmetries of the Hamiltonian include lattice translation, the bond-centered inversion, and a global internal symmetry  $A_4$ , which is the symmetry group of a tetrahedron [see Fig. 2(d)]. All possible SPT phases protected by these symmetries are explicitly enumerated in Ref. [59].

When  $p = 1/3$  and  $q = 0$ , the Hamiltonian reduces to the celebrated Affleck-Kennedy-Lieb-Tasaki (AKLT) model, whose ground state is exactly solvable and exhibits nontrivial topological edge degrees of freedom [60]. As  $(p,q)$  deviates from this solvable point, phase transitions arise among three distinct regions, I, II, and III, as indicated in the numerically obtained phase diagram in Fig. 2(e) [51]. The ground states in the three phases respect all the symmetries while they are distinguished by the complex  $U(1)$  phase that the state picks upon a  $120^{\circ}$  rotation  $a \in A_4$  of underlying spins [51]. Using our algorithm, we find that  $H(p,q)$  with  $2|q| \leq p \leq 2 - 2|q|$  can be engineered from  $H_I$  [Fig. 2(e)]. The strength of  $H(p,q)$  is set to  $1/(3+p)$  by isotropic components, and the range of  $(p,q)$  is limited by the maximum possible strength of the engineered anisotropic components [51].

Discussions.-We now consider the dominant operational imperfections which may arise during our protocol. First, periodic driving pulses may cause heating in the many-body system, eventually leading to a featureless infinite temperature state [61-63]. As discussed earlier, such energy absorption is irrelevant until exponentially long times  $t^* \sim \exp [O(1 / \bar{J} T)]$ , where  $\bar{J} \equiv \max_{i,j} J_{ij} \| h_{ij} \|$ . A second natural concern is that our method is based upon engineering the low order Magnus Hamiltonian  $H_{\mathrm{eff}}^{(0)}$  which provides only an approximate description of the full many-body dynamics. However, for gapped Hamiltonians, higher order terms are strongly suppressed so long as  $\bar{J} T \ll 1$ , and the phase should remain stable. Third, in the presence of weak coupling to a bath, our protocol can enhance qudit sensitivity to external noise at harmonics of  $1 / T$  [6,10,13]. However, this extra sensitivity can be mitigated if the control pulses are significantly faster than the bandwidth of noise spectrum. In a similar vein, the limited strength of control pulses also imposes additional practical constraints for any experimental implementation; in certain cases, further numerical optimization may help to solve these practical issues [2,8,12].

Interestingly, the decoupling of interactions may result in dynamical quantum phase transitions for isolated, weakly disordered systems [64]. In such cases, the interplay of weak disorder, suppressed interactions, and an exponentially slow heating rate can lead to many-body localization, where initial state memories survive for extremely long times. Harnessing these effects may enable the coherent manipulation and storage of quantum information in an interacting many-body system [65,66].

The authors would like to thank E. Rosenfeld, H. Zhou, J. Choi, V. Khemani, A. Prakash, J. Haah, A. Gorshkov, Y. Moon, and J. Taylor for useful discussions. This work was supported through NSF, CUA, the Vannevar Bush Faculty Fellowship from ONR, AFOSR MURI and Moore Foundation. S.C. is supported by the Kwanjeong Educational Foundation.

[1] E. L. Hahn, Phys. Rev. 80, 580 (1950).  
[2] G. S. Uhrig, Phys. Rev. Lett. 98, 100504 (2007).  
[3] G. de Lange, Z. H. Wang, D. Riste, V. V. Dobrovitski, and R. Hanson, Science 330, 60 (2010).  
[4] W.-J. Kuo and D.A. Lidar, Phys. Rev. A 84, 042329 (2011).  
[5] L. Jiang and A. Imambekov, Phys. Rev. A 84, 060302 (2011).  
[6] J. Bylander, S. Gustavsson, F. Yan, F. Yoshihara, K. Harrabi, G. Fitch, D. G. Cory, Y. Nakamura, J.-S. Tsai, and W. D. Oliver, Nat. Phys. 7, 565 (2011).  
[7] P. C. Maurer, G. Kucsko, C. Latta, L. Jiang, N. Y. Yao, S. D. Bennett, F. Pastawski, D. Hunger, N. Chisholm, M. Markham, D. J. Twitchen, J. I. Cirac, and M. D. Lukin, Science 336, 1283 (2012).  
[8] G. A. Paz-Silva and D. A. Lidar, Sci. Rep. 3, 1530 (2013).  
[9] E.M. Kessler, P. Komar, M. Bishop, L. Jiang, A.S. Sorensen, J. Ye, and M.D. Lukin, Phys. Rev. Lett. 112, 190403 (2014).  
[10] I. Lovchinsky, A. O. Sushkov, E. Urbach, N. P. de Leon, S. Choi, K. De Greve, R. Evans, R. Gertner, E. Bersin, C. Müller, L. McGuinness, F. Jelezko, R. L. Walsworth, H. Park, and M. D. Lukin, Science 351, 836 (2016).  
[11] I. Lovchinsky, J. D. Sanchez-Yamagishi, E. K. Urbach, S. Choi, S. Fang, T. I. Andersen, K. Watanabe, T. Taniguchi, A. Bylinskii, E. Kaxiras, P. Kim, H. Park, and M. D. Lukin, Science 355, 503 (2017).  
[12] D. G. Lucarelli, arXiv:1611.00188.  
[13] V.M. Frey, S. Mavadia, L. M. Norris, and W. de Ferranti, arXiv:1704.02050.  
[14] A. Ajoy, U. Bissbort, D. Poletti, and P. Cappellaro, arXiv:1710.03987.  
[15] N. H. Lindner, G. Refael, and V. Galitski, Nat. Phys. 7, 490 (2011).  
[16] L. Jiang, T. Kitagawa, J. Alicea, A. R. Akhmerov, D. Pekker, G. Refael, J. I. Cirac, E. Demler, M. D. Lukin, and P. Zoller, Phys. Rev. Lett. 106, 220402 (2011).  
[17] T. Iadecola, L. H. Santos, and C. Chamon, Phys. Rev. B 92, 125107 (2015).  
[18] V. Khemani, A. Lazarides, R. Moessner, and S. L. Sondhi, Phys. Rev. Lett. 116, 250401 (2016).  
[19] D. V. Else, B. Bauer, and C. Nayak, Phys. Rev. Lett. 117, 090402 (2016).  
[20] C. W. von Keyserlingk, V. Khemani, and S. L. Sondhi, Phys. Rev. B 94, 085112 (2016).  
[21] N. Y. Yao, A. C. Potter, I.-D. Potirniche, and A. Vishwanath, Phys. Rev. Lett. 118, 030401 (2017).  
[22] U. Haeberlen and J. S. Waugh, Phys. Rev. 175, 453 (1968).  
[23] J. S. Waugh, L. M. Huber, and U. Haeberlen, Phys. Rev. Lett. 20, 180 (1968).

[24] B. Yan, S. A. Moses, B. Gadway, J. P. Covey, K. R. A. Hazzard, A. M. Rey, D. S. Jin, and J. Ye, Nature (London) 501, 521 (2013).  
[25] G. A. Álvarez, D. Suter, and R. Kaiser, Science 349, 846 (2015).  
[26] M. Gärttner, J. G. Bohnet, A. Safavi-Naini, M. L. Wall, J. J. Bollinger, and A. M. Rey, Nat. Phys. 13, 781 (2017).  
[27] K.X. Wei, C. Ramanathan, and P. Cappellaro, arXiv: 1612.05249v1.  
[28] J. Zhang, P.W. Hess, A. Kyprianidis, P. Becker, A. Lee, J. Smith, G. Pagano, I.D. Potirniche, A.C. Potter, A. Vishwanath, N.Y. Yao, and C. Monroe, Nature (London) 543, 217 (2017).  
[29] S. Choi, J. Choi, R. Landig, G. Kucsko, H. Zhou, J. Isoya, F. Jelezko, S. Onoda, H. Sumiya, V. Khemani, C. von Keyserlingk, N. Y. Yao, E. A. Demler, and M. D. Lukin, Nature (London) 543, 221 (2017).  
[30] A. Brinkmann and M. Edén, J. Chem. Phys. 120, 11726 (2004).  
[31] A. Ajoy and P. Cappellaro, Phys. Rev. Lett. 110, 220503 (2013).  
[32] H. Frydrych, G. Alber, and P. Bažant, Phys. Rev. A 89, 022320 (2014).  
[33] D. Hayes, S. T. Flammia, and M. J. Biercuk, New J. Phys. 16, 083027 (2014).  
[34] C. Senko, P. Richerme, J. Smith, A. Lee, I. Cohen, A. Retzker, and C. Monroe, Phys. Rev. X 5, 021026 (2015).  
[35] R. B. Potts and C. Domb, Math. Proc. Cambridge Philos. Soc. 48, 106 (1952).  
[36] D. A. Huse, Phys. Rev. B 24, 5180 (1981).  
[37] F. D. M. Haldane, Phys. Rev. Lett. 50, 1153 (1983).  
[38] P. Fendley, J. Stat. Mech. (2012) P11020.  
[39] G. Kucsko, S. Choi, J. Choi, P.C. Maurer, H. Sumiya, S. Onoda, J. Isoya, F. Jelezko, E. Demler, N. Y. Yao, and M. D. Lukin, arXiv:1609.08216.  
[40] H. Labuhn, D. Barredo, S. Ravets, S. de Leseleuc, T. Macri, T. Lahaye, and A. Browaeks, Nature (London) 534, 667 (2016).  
[41] J. Zeiher, J.-y. Choi, A. Rubio-Abadal, T. Pohl, R. van Bijnen, I. Bloch, and C. Gross, arXiv:1705.08372.  
[42] H. Bernien, S. Schwartz, A. Keesling, H. Levine, A. Omran, H. Pichler, S. Choi, A. S. Zibrov, M. Endres, M. Greiner, V. Vuletic, and M. D. Lukin, arXiv:1707.04344.  
[43] M. Rotteler and P. Wocjan, IEEE Trans. Inf. Theory 52, 4171 (2006).  
[44] M. Stollsteimer and G. Mahler, Phys. Rev. A 64, 052301 (2001).

[45] M. A. Nielsen, M. J. Bremner, J. L. Dodd, A. M. Childs, and C. M. Dawson, Phys. Rev. A 66, 022317 (2002).  
[46] We assume that  $U_{k} = \mathbb{I}$  by appropriately setting either  $P_{1}$  or  $P_{k}$ .  
[47] D. A. Abanin, W. De Roeck, W. W. Ho, and F. Huveneers, Phys. Rev. B 95, 014112 (2017).  
[48] D. Abanin, W. De Roeck, F. Huveneers, and W. W. Ho, Commun. Math. Phys. 354, 809 (2017).  
[49] T. Mori, T. Kuwahara, and K. Saito, Phys. Rev. Lett. 116, 120401 (2016).  
[50] T. Kuwahara, T. Mori, and K. Saito, Ann. Phys. (Amsterdam) 367, 96 (2016).  
[51] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.119.183603 for a detailed description of the exemplary pulse sequence that cancels spin-1 dipolar interactions and for the numerical method used to compute the phase boundary of Fig. 2(e). The Supplemental Material includes Refs. [51-55].  
[52] X. Chen, Z.-C. Gu, and X.-G. Wen, Phys. Rev. B 83, 035107 (2011).  
[53] X. Chen, Z.-C. Gu, and X.-G. Wen, Phys. Rev. B 84, 235128 (2011).  
[54] N. Schuch, D. Perez-Garcia, and I. Cirac, Phys. Rev. B 84, 165139 (2011).  
[55] F. Pollmann and A. M. Turner, Phys. Rev. B 86, 125441 (2012).  
[56] G. Vidal, Phys. Rev. Lett. 98, 070201 (2007).  
[57] W. Dür, J. I. Cirac, M. Lewenstein, and D. Bruß, Phys. Rev. A 61, 062313 (2000).  
[58] D. Bertsimas, J. N. Tsitsiklis, and J. Tsitsiklis, Introduction to Linear Optimization (Athena Scientific Series in Optimization and Neural Computation, 6) (Athena Scientific, Nashua, 1997).  
[59] A. Prakash, C. G. West, and T. C. Wei, Phys. Rev. B 94, 045136 (2016).  
[60] I. Affleck, T. Kennedy, E. H. Lieb, and H. Tasaki, Phys. Rev. Lett. 59, 799 (1987).  
[61] L. D'Alessio and M. Rigol, Phys. Rev. X 4, 041048 (2014).  
[62] A. Lazarides, A. Das, and R. Moessner, Phys. Rev. E 90, 012110 (2014).  
[63] P. Ponte, A. Chandran, Z. Papić, and D. A. Abanin, Ann. Phys. (Amsterdam) 353, 196 (2015).  
[64] S. Choi, D. A. Abanin, and M. D. Lukin, arXiv:1703.03809v1.  
[65] S. Choi, N. Y. Yao, S. Gopalakrishnan, and M. D. Lukin, arXiv:1508.06992v1.  
[66] N. Y. Yao, C. R. Laumann, and A. Vishwanath, arXiv: 1508.06995v1.