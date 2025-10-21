# Robustness of Coherence: An Operational and Observable Measure of Quantum Coherence

Carmine Napoli, $^{1,2}$  Thomas R. Bromley, $^{2}$  Marco Cianciaruso, $^{1,2}$  Marco Piani, $^{3}$  Nathaniel Johnston, $^{4}$  and Gerardo Adesso $^{2}$

$^{1}$ Dipartimento di Fisica "E. R. Caianiello", Università degli Studi di Salerno, Via Giovanni Paolo II, I-84084 Fisciano (SA), Italy and INFN Sezione di Napoli, Gruppo Collegato di Salerno, Italy

$^{2}$ School of Mathematical Sciences, The University of Nottingham, University Park, Nottingham NG7 2RD, United Kingdom

$^{3}$ SUPA and Department of Physics, University of Strathclyde, Glasgow G4 0NG, United Kingdom

$^{4}$ Department of Mathematics and Computer Science, Mount Allison University, Sackville, New Brunswick E4L 1E2, Canada (Received 20 January 2016; published 12 April 2016)

Quantifying coherence is an essential endeavor for both quantum foundations and quantum technologies. Here, the robustness of coherence is defined and proven to be a full monotone in the context of the recently introduced resource theories of quantum coherence. The measure is shown to be observable, as it can be recast as the expectation value of a coherence witness operator for any quantum state. The robustness of coherence is evaluated analytically on relevant classes of states, and an efficient semidefinite program that computes it on general states is given. An operational interpretation is finally provided: the robustness of coherence quantifies the advantage enabled by a quantum state in a phase discrimination task.

DOI: 10.1103/PhysRevLett.116.150502

Nearly one century old, quantum mechanics is now livelier than ever. Fundamental experiments have just demonstrated, beyond any major loophole, that quantum correlations are incompatible with a local realistic interpretation [1-3]. Moreover, the realization that quantum properties can be harnessed for practical applications [4] is presently fuelling a heated international race [5] to deploy quantum technologies [6]. This is no coincidence: the improved comprehension of fundamental quantum properties and our increased ability to exploit them go hand in hand.

The most essential feature signifying quantumness in a single system and underpinning all forms of quantum correlations in composite systems [7-9] is quantum coherence, namely, the possibility of creating superpositions of a set of orthogonal states. Revealing quantum coherence in the state of a natural or man-made system earmarks its behavior as genuinely nonclassical [10,11]. Its degree of coherence may quantify the capability of such an object for quantum-enhanced applications [12,13], ranging from cryptography [14] to metrology [15] and thermodynamics [16,17]. It is thus imperative to accomplish a rigorous operational characterization of quantum coherence.

Recently, various approaches have been put forward to develop a resource theory of coherence [12,13,18-27]. These partly follow from, and complement, earlier studies on resource theories of asymmetry [18,28-33], of which coherence may be seen as a special instance [20,34]. A resource theory is defined by the notions of free states (i.e., those not containing the resource, and assumed available at no cost) and free operations (i.e., those one is restricted to, and that cannot transform free states into resource states)

[35,36]. Fixing a reference basis (based on physical arguments [37]), which we can identify as the computational basis  $\{|j\rangle\}_{j=0}^{d-1}$  for a  $d$ -dimensional system, the convex set  $\mathcal{I}$  of free states in any resource theory of coherence is given by the incoherent states diagonal in the reference basis  $\delta = \sum_{j=0}^{d-1} \delta_j |j\rangle \langle j|$ . Any state  $\rho$  can be reduced to an incoherent one by a full dephasing operation  $\Delta$ , which maps  $\rho$  into its diagonal part  $\Delta(\rho) = \sum_{j=0}^{d-1} |j\rangle \langle j|\rho|j\rangle \langle j|$  in the reference basis.

Different authors have however considered different options in analyzing limitations on the processing of coherence (see also Refs. [38,39]). We mention the following alternative choices of free operations, in order of inclusion: incoherence preserving operations [12]  $\supset$  incoherent operations [13]  $\supset$  strictly incoherent operations [40]  $\supset$  translationally invariant operations [20]  $\supset$  genuinely incoherent operations [27]. By incoherence preserving operations we refer to the maximal set of quantum channels  $\Lambda^M$ , which map incoherent states into incoherent states [12], i.e.,  $\Lambda^M(\delta) \in \mathcal{I}$  for any  $\delta \in \mathcal{I}$ . Incoherent operations are instead those quantum channels  $\Lambda^I$  that admit one operator-sum decomposition  $\Lambda^I(\rho) = \sum_l K_l \rho K_l^\dagger$  with all incoherence preserving Kraus operators  $\{K_l\}$  [13]. Strictly incoherent operations  $\Lambda^S$  are a subset of incoherent operations whose incoherence preserving Kraus operators  $\{K_l\}$  further obey  $\langle j|K_l\rho K_l^\dagger |j\rangle = \langle j|K_l\Delta(\rho)K_l^\dagger |j\rangle \quad \forall j,l$ , meaning that they can neither create nor use coherence [19,40]. More restrictively, genuinely incoherent operations  $\Lambda^G$  [27] (also known as generalized incoherent measurements [40]) are those that leave every incoherent state invariant,  $\Lambda^G(\delta) = \delta$  [27]; their

Kraus operators are all incoherence preserving in all possible operator-sum decompositions. In between the last two sets are translationally invariant operations, introduced within the resource theory of asymmetry [18,20]: specialized to coherence (i.e., asymmetry with respect to time translations generated by a Hamiltonian  $H$  diagonal in the reference basis  $\{|j\rangle\}$ ), translationally invariant operations  $\Lambda^T$  are defined by the condition  $e^{-iHt}\Lambda^T(\rho)e^{iHt} = \Lambda^T(e^{-iHt}\rho e^{iHt})$  for any  $\rho$  and any real  $t$ .

Several quantities have been proposed accordingly as candidate measures of quantum coherence, respecting the physical requirements of monotonicity under (some of) the sets of operations introduced above [12,13,18-22, 25-27,30,33,37,41]. A canonical measure that complies with all the aforementioned resource theories is the relative entropy of coherence [12,13,18,30], which for a state  $\rho$  takes the simple form  $\mathcal{C}_S(\rho) = \mathcal{S}(\Delta (\rho)) - \mathcal{S}(\rho)$ , where  $\mathcal{S}(\rho) = -\mathrm{Tr}[\rho \log_2\rho ]$  is the von Neumann entropy. This measure can be interpreted as the optimal rate at which maximally coherent states that can be distilled by incoherent operations  $\Lambda^I$  in the asymptotic limit of many copies of  $\rho$  [25]; however, its experimental determination requires full state tomography, which can be unfeasible for large systems. More accessible measures of relevance for quantum metrology [15], such as the Wigner-Yanase skew information and the quantum Fisher information [33,41], are monotone under translationally invariant operations but not under the larger set of incoherent operations [20], which may put into question their broader status as coherence quantifiers. In general, despite recent progress, there remains a shortage of rigorous and physically intuitive bona fide measures of coherence endowed with direct operational interpretations.

In this Letter we fill this gap by introducing the robustness of coherence. As the name suggests, it quantifies the minimal mixing required to destroy all the coherence in a quantum state—an already operational definition, inspired by similar concepts previously investigated for entanglement, steering-type correlations, nonlocality, and other resources [36, 42-45]. We prove that such a measure is a full monotone in all possible resource theories of coherence. The measure is furthermore computable (exactly in relevant cases, and numerically in general via a simple semidefinite program [46]) and observable: it can be recast as the expectation value of a witness operator for any quantum state. This makes it very appealing for experimental investigations, e.g., in condensed matter and biological contexts [10,11,47]. We then show that the measure admits a direct operational interpretation: it quantifies the advantage enabled by a quantum state, compared to any incoherent state, in a phase discrimination task. We further discuss the generalization of these results to the case of asymmetry in a companion paper [34], which also contains detailed proofs for some technical results of this Letter.

Let  $\mathcal{D}(\mathbb{C}^d)$  be the convex set of density operators acting on a  $d$ -dimensional Hilbert space, and let  $\mathcal{I}\subset \mathcal{D}(\mathbb{C}^d)$  be the subset of incoherent states. We define the robustness of coherence (ROC) of a quantum state  $\rho \in \mathcal{D}(\mathbb{C}^d)$  as

$$
\mathcal {C} _ {\mathcal {R}} (\rho) = \min  _ {\tau \in \mathcal {D} \left(\mathbb {C} ^ {d}\right)} \left\{s \geq 0 \left| \frac {\rho + s \tau}{1 + s} =: \delta \in \mathcal {I} \right. \right\}, \tag {1}
$$

that is, the minimum weight of another state  $\tau$  such that its convex mixture with  $\rho$  yields an incoherent state  $\delta$ . The concept is illustrated in Fig. 1 for a qubit  $(d = 2)$ . If we denote by  $\tau^{\star}$  and  $\delta^{\star}$  the states achieving the minimum in Eq. (1), then

$$
\rho = \left[ 1 + \mathcal {C} _ {\mathcal {R}} (\rho) \right] \delta^ {*} - \mathcal {C} _ {\mathcal {R}} (\rho) \tau^ {*} \tag {2}
$$

is said to realize an optimal pseudomixture for  $\rho$ . Notice that it is necessary in Eq. (1) to let  $\tau$  be an arbitrary state: if one restricted  $\tau$  to be incoherent, then the minimum  $s$  would diverge for any state  $\rho$  with nonzero coherence, henceforth resulting totally uninformative. This contrasts with the case of entanglement, for which the original robustness was defined in terms of pseudomixtures with separable states [42], and only later extended to pseudomixtures with arbitrary states [43].

We now prove that the ROC is a bona fide measure of coherence. First of all, it is seen by definition that

$$
\mathcal {C} _ {\mathcal {R}} (\rho) \geq 0 \quad \text {a n d} \quad \mathcal {C} _ {\mathcal {R}} (\rho) = 0 \Leftrightarrow \rho \in \mathcal {I}. \tag {3}
$$

Second, the ROC is convex, which is a desirable (although not a fundamental) property for a coherence quantifier [13]. The proof mirrors the one for the robustness of entanglement [42]. Let  $\rho_{1}$  and  $\rho_{2}$  be two states, and write for each the optimal pseudomixture  $\rho_{k} = [1 + \mathcal{C}_{\mathcal{R}}(\rho_{k})]\delta_{k}^{\star} - \mathcal{C}_{\mathcal{R}}(\rho_{k})\tau_{k}^{\star}$ $(k = 1,2)$ . Taking the convex combination  $\rho = p\rho_{1} + (1 - p)\rho_{2}$  with  $0\leq p\leq 1$ , notice that a pseudomixture  $\rho = (1 + s)\delta -s\tau$  can be written with  $\delta = \{p[1 + \mathcal{C}_{\mathcal{R}}(\rho_1)]\delta_1^\star +$ $(1 - p)[1 + \mathcal{C}_{\mathcal{R}}(\rho_2)]\delta_2^\star \} /(1 + s)\in \mathcal{I},\quad \tau = [p\mathcal{C}_{\mathcal{R}}(\rho_1)\tau_1^\star +$ $(1 - p)\mathcal{C}_{\mathcal{R}}(\rho_2)\tau_2^\star ] / s$  and  $s = p\mathcal{C}_{\mathcal{R}}(\rho_1) + (1 - p)\mathcal{C}_{\mathcal{R}}(\rho_2)$ . By definition,  $\mathcal{C}_{\mathcal{R}}(\rho)\leq s$ , which proves convexity,

$$
\mathcal {C} _ {\mathcal {R}} \left(p \rho_ {1} + (1 - p) \rho_ {2}\right) \leq p \mathcal {C} _ {\mathcal {R}} (\rho_ {1}) + (1 - p) \mathcal {C} _ {\mathcal {R}} (\rho_ {2}). \tag {4}
$$

Third, and most importantly, the ROC is nonincreasing under all the sets of operations used in resource theories of coherence. We prove in fact a general form of monotonicity under incoherence preserving (sub)channels. Let  $\{\Gamma_l\}_{l=1}^m$  be an instrument, i.e., a set of  $m$  (sub)channels [completely

![](images/031a672d1b5042d04a4169929b28e90f2a0f1895afec5d1aba92041a25d974fd.jpg)  
FIG. 1. Robustness of coherence  $\mathcal{C}_{\mathcal{R}}(\rho)$  for a single qubit state  $\rho = \frac{1}{2} (\mathbb{1} + \vec{r}\cdot \vec{\sigma})$ , where  $\vec{r}$  is the Bloch vector and  $\vec{\sigma}$  is the vector of Pauli matrices. Incoherent states span the thick vertical  $r_3$  axis. The optimization in Eq. (1) is fulfilled by an equatorial pure state  $\tau^{\star}$  as depicted, resulting in  $\mathcal{C}_{\mathcal{R}}(\rho) = (r_1^2 +r_2^2)^{\frac{1}{2}} = 2|\rho_{01}|$ .

positive maps whose sum  $\sum_{l=1}^{m} \Gamma_{l}(\rho) =: \Lambda(\rho)$  defines a trace preserving channel  $\Lambda$ , mapping any incoherent state  $\delta \in \mathcal{I}$  into another (un)normalized incoherent state  $\Gamma_{l}(\delta)$ . For any  $\rho$ , we have then

$$
\mathcal {C} _ {\mathcal {R}} (\rho) \geq \sum_ {l = 1} ^ {m} \operatorname {T r} \left[ \Gamma_ {l} (\rho) \right] \mathcal {C} _ {\mathcal {R}} \left(\frac {\Gamma_ {l} (\rho)}{\operatorname {T r} \left[ \Gamma_ {l} (\rho) \right]}\right). \tag {5}
$$

The proof can be easily sketched (see Ref. [34] for more details). Take the optimal pseudomixture for  $\rho$  given by Eq. (2) and apply the (sub)channel  $\Gamma_{l}$  to both sides,  $\Gamma_{l}(\rho) = [1 + \mathcal{C}_{\mathcal{R}}(\rho)]\Gamma_{l}(\delta^{\star}) - \mathcal{C}_{\mathcal{R}}(\rho)\Gamma_{l}(\tau^{\star})$ . Since  $\Gamma_{l}(\delta^{\star}) / \mathrm{Tr}[\Gamma_{l}(\delta^{\star})]$  is still incoherent, definition (1) implies  $\mathcal{C}_{\mathcal{R}}(\Gamma_{l}(\rho) / \mathrm{Tr}[\Gamma_{l}(\rho)]) \leq \mathcal{C}_{\mathcal{R}}(\rho) \{\mathrm{Tr}[\Gamma_{l}(\tau^{\star})] / \mathrm{Tr}[\Gamma_{l}(\rho)]\}$ . Then,  $\sum_{l} \mathrm{Tr}[\Gamma_{l}(\rho)] \mathcal{C}_{\mathcal{R}}(\Gamma_{l}(\rho) / \mathrm{Tr}[\Gamma_{l}(\rho)]) \leq \sum_{l} \mathrm{Tr}[\Gamma_{l}(\rho)] \mathcal{C}_{\mathcal{R}}(\rho) \times \{\mathrm{Tr}[\Gamma_{l}(\tau^{\star})] / \mathrm{Tr}[\Gamma_{l}(\rho)]\} = \mathcal{C}_{\mathcal{R}}(\rho) \sum_{l} \mathrm{Tr}[\Gamma_{l}(\tau^{\star})] = \mathcal{C}_{\mathcal{R}}(\rho)$ , concluding the proof. In the case  $m = 1$ , Eq. (5) proves that the ROC cannot increase, on average, under the maximal set of incoherence preserving operations  $\{\Lambda^{M}\}$  [12]. For  $m \geq 1$ , if one identifies each  $\Gamma_{l}$  with a Kraus operator  $K_{l}$  (obeying  $\sum_{l=1}^{m} K_{l}^{\dagger} K_{l} = 1$ ), then Eq. (5) proves monotonicity of the ROC under selective incoherent operations  $\{\Lambda^{I}\}$ , flagged as property C2b in Ref. [13], which is typically a rather demanding requirement in resource theories. Overall, Eq. (5) establishes the ROC as a full monotone with respect to all possible formulations of the theory of coherence.

We now show that the ROC has also the desirable properties of computability and accessibility. Inspired by entanglement witnesses [7,48], which are very useful tools to detect inseparability in the laboratory [49], we introduce the notion of coherence witnesses. A Hermitian operator  $W$  satisfies  $\Delta(W) \geq 0$  if and only if  $\mathrm{Tr}[\delta W] = \mathrm{Tr}[\delta \Delta(W)] \geq 0$  for all incoherent states  $\delta \in \mathcal{I}$ ; we call any such an observable  $W$  a coherence witness, because finding  $\mathrm{Tr}[\rho W] < 0$  reveals coherence in the state  $\rho$  [50]. We find that the expectation value of any witness  $W$ , obeying the further constraint  $W \leq \mathbb{1}$ , provides a quantitative lower bound to the ROC [34]

$$
\max  \{0, - \operatorname {T r} [ \rho W ] \} \leq \mathcal {C} _ {\mathcal {R}} (\rho), \quad \forall W \text {s u c h t h a t} \tag {6}
$$

$$
\Delta (W) \geq 0 \quad \text {a n d} \quad W \leq \mathbb {1}. \tag {7}
$$

Importantly, given any state  $\rho$ , there always exists an optimal witness  $W^{\star}$ , characterized in particular by  $\Delta(W^{\star}) = 0$ , that saturates inequality (6). In other words, the ROC is an observable quantity, given by the expectation value of a suitable (state-dependent) witness operator for any quantum state  $\rho$ . Finding such an optimal witness, hence determining  $\mathcal{C}_{\mathcal{R}}(\rho)$  as defined in Eq. (1), can be then recast [34] as a simple semidefinite program (SDP) [51] (significantly more efficient than the convex optimization one for the robustness of entanglement [52]):

$$
\text {m a x i m i z e} - \operatorname {T r} [ W \rho ] \text {s u b j e c t t o E q . (7)}. \tag {8}
$$

For the convenience of the reader, we release the MATLAB [53] code that makes use of the free cvx package [54,55] to evaluate the ROC, as Supplemental Material [46].

These results reveal that one can readily estimate the ROC from below in the laboratory, by measuring any

observable  $W$  obeying the constraints in Eq. (7), with no need for full tomography of the state  $\rho$ . This may be particularly valuable for witnessing coherence effects in biological domains, e.g., energy transport phenomena in light-harvesting systems [10,11,47,56]. However, given a state  $\rho$ , the lower bound of Eq. (6) can vanish for non-optimized choices of  $W$ . Typically, one needs some knowledge on the form of  $\rho$  to determine the optimal witness  $W^{\star}$ ; a similar issue is encountered in entanglement detection [49]. Nonetheless, Eqs. (6) and (7) imply that, for any set of observables  $\{O_i\}$ ,  $i = 1,\dots,k$ , experimentally measured with expectation values  $o_{i} = \mathrm{Tr}[O_{i}\rho ]$ , and not necessarily tailored to the measurement of ROC, one can consider coherence witnesses of the form  $W = \sum_{i = 1}^{k}c_{i}O_{i} + m\mathbb{1}$ , for  $c_{1},\ldots ,c_{k},m\in \mathbb{R}$ , and obtain a lower bound to the ROC by the SDP [34] (code available [46])

$$
\text {m a x i m i z e} - \left(\sum_ {i = 1} ^ {k} c _ {i} o _ {i} + m\right)
$$

$$
\text {s u b j e c t} \Delta \left(\sum_ {i = 1} ^ {k} c _ {i} O _ {i} + m \mathbb {1}\right) \geq 0,
$$

$$
\sum_ {i = 1} ^ {k} c _ {i} O _ {i} + m \mathbb {1} \leq \mathbb {1}.
$$

One can even make potentially better use of available experimental data, by exactly estimating the minimal ROC compatible with the data; this can also be cast as a SDP [34,46].

Accessible faithful lower bounds to the ROC can be given too, noting that  $W_{2} = [\Delta (\rho) - \rho ] / \| \Delta (\rho)\|_{\infty}$  obeys Eq. (7), so that

$$
\mathcal {C} _ {\mathcal {R}} (\rho) \geq \frac {\| \rho - \Delta (\rho) \| _ {2} ^ {2}}{\| \Delta (\rho) \| _ {\infty}} \geq \frac {\| \rho - \Delta (\rho) \| _ {2} ^ {2}}{\| \Delta (\rho) \| _ {2}} \geq \| \rho - \Delta (\rho) ] \| _ {2} ^ {2}, \tag {9}
$$

since  $\mathrm{Tr}[(\Delta (\rho) - \rho)\rho ] = \mathrm{Tr}[\Delta (\rho)^2 ] - \mathrm{Tr}[\rho^2 ] = \| \rho -\Delta (\rho)\| _2^2$  Here,  $\| \cdot \| _2$  is the 2-norm, and  $\| \cdot \|_{\infty}$  is the operator norm. The quantity on the rightmost side of Eq. (9) is (i) nonzero on all but incoherent states, (ii) itself a monotone under genuinely incoherent operations  $\Lambda^{G}$  [27], but not under the larger sets of incoherent operations [13], and (iii) accessible via the measurement of the purities  $\mathrm{Tr}[\rho^2 ]$  and  $\mathrm{Tr}[\Delta (\rho)^2 ]$  [notably, the same holds for the tighter second-to-last bound in Eq. (9)]. The latter two quantities can be measured directly on two copies of the state  $\rho$  (assumed unknown) as  $\mathrm{Tr}[\rho^{\otimes 2}V]$  and  $\mathrm{Tr}[\rho^{\otimes 2}\Delta^{\otimes 2}(V)]$  , respectively, with  $V$  being the swap operator [41,57], defined by its action  $V|\psi \rangle |\phi \rangle =$ $|\phi \rangle |\psi \rangle$  , for all  $|\psi \rangle ,|\phi \rangle \in \mathbb{C}^d$

We now show that an analytical evaluation of ROC can be obtained for a relevant class of  $d$ -dimensional states. Let  $\rho \in \mathcal{D}(\mathbb{C}^d)$  be a state for which there exists a unitary  $U = \sum_{j}e^{i\phi_{j}}|j\rangle \langle j|$ , belonging to the set of genuinely incoherent operations [27], such that  $(U\rho U^{\dagger})_{kl} = |\rho_{kl}|$ . One has then  $\mathcal{C}_{\mathcal{R}}(\rho) = \mathcal{C}_{\ell_1}(\rho)$  [34], where  $\mathcal{C}_{\ell_1}(\rho) = \sum_{k,l}|\rho_{kl}| - 1 = 2\sum_{k < l}|\rho_{kl}|$  is the  $\ell_1$  norm of coherence

[13]. The class of states for which this equality holds includes, for instance, all one-qubit states ( $d = 2$ , see Fig. 1), all  $d$ -dimensional states with an  $X$ -shaped density matrix [58-60] (which contain in particular Bell diagonal states of two qubits [37,61]), and all pure states  $|\psi \rangle \in \mathbb{C}^d$ . For the latter, writing in general  $|\psi \rangle = \sum_{j=0}^{d-1} \psi_j |j\rangle$ , we get explicitly  $\mathcal{C}_{\mathcal{R}}(|\psi\rangle \langle \psi|) = \mathcal{C}_{\ell_1}(|\psi\rangle \langle \psi|) = (\sum_j |\psi_j|)^2 - 1$  [13].

In particular, maximally coherent states  $|\psi^{+}\rangle$ , characterized by  $|\psi_{j}| = (1 / \sqrt{d})$ $\forall j = 0,\dots,d - 1$ , have  $\mathcal{C}_{\mathcal{R}}(|\psi^{+}\rangle \langle \psi^{+}|) = \mathcal{C}_{\ell_1}(|\psi^{+}\rangle \langle \psi^{+}|) = d - 1$ , which is the maximum possible value for the ROC of any  $d$ -dimensional state. One can show [34] in fact that these are the only states that can reach maximal ROC, which positively settles another requirement recently advocated for bona fide measures of coherence [26].

The equivalence between ROC and the  $\ell_1$  norm of coherence breaks down already in the dimension  $d = 3$ . One can prove however the existence of general upper and lower bounds [34]

$$
(d - 1) ^ {- 1} \mathcal {C} _ {\ell_ {1}} (\rho) \leq \mathcal {C} _ {\mathcal {R}} (\rho) \leq \mathcal {C} _ {\ell_ {1}} (\rho), \forall \rho \in \mathcal {D} (\mathbb {C} ^ {d}). \tag {10}
$$

Both bounds can be tight. Examples of states saturating the upper bound have been provided already (for instance, all pure states). A family of states saturating the lower bound is instead given by  $\rho_{p} = (1 + p)\mathbb{1} / d - p|\psi^{+}\rangle \langle \psi^{+}|$  with  $0\leq p\leq 1 / (d - 1)$ , for which  $\mathcal{C}_{\ell_1}(\rho_p) = p(d - 1)$  and  $\mathcal{C}_{\mathcal{R}}(\rho_p) = p$ . Nonetheless, the lower bound becomes looser for large values of  $\mathcal{C}_{\ell_1}$ , and one finds  $\mathcal{C}_{\mathcal{R}}(\rho)\to d - 1$  for all  $\rho$  such that  $\mathcal{C}_{\ell_1}(\rho)\to d - 1$  [34].

We are finally ready to provide a direct operational interpretation for the ROC in a metrology context. Consider the following phase discrimination (PD) game. Alice prepares a quantum state  $\rho \in \mathcal{D}(\mathbb{C}^d)$ , which then enters a black box. The black box encodes a phase on  $\rho$  by implementing a unitary  $U_{\phi} = \exp(iN\phi)$  with  $N = \sum_{j=0}^{d-1} j|j\rangle \langle j|$  and  $\phi \in \mathbb{R}$ , so that the output state is determined by the action of the unitary channel  $\mathcal{U}_{\phi}(\rho) \coloneqq U_{\phi}\rho U_{\phi}^{\dagger}$ . We can think of  $N$  as a Hamiltonian for the system with an equispaced spectrum, assuming unit spacing without loss of generality. In this way, the reference basis  $\{|j\rangle\}$ , with respect to which coherence is defined and measured, is physically identified by the choice of the Hamiltonian. Suppose one of  $m$  phases  $\{\phi_k\}_{k=0}^{m-1}$  can be applied, each with a prior probability  $p_k$ . Any collection of pairs  $\{(p_k, \phi_k)\}_{k=0}^{m-1} \eqqcolon \Theta$  defines a PD game, where Alice's goal is that of guessing correctly the phase that was actually imprinted on the state. To this end, she performs a generalized measurement with elements  $\{M_k\}$  (satisfying  $M_k \geq 0$ ,  $\sum_k M_k = 1$ ) on the output state  $\mathcal{U}_{\phi}(\rho)$  after the black box. Optimizing over all measurements, the maximal probability of success depends on the game  $\Theta$  and the input state  $\rho$ , and is given by  $p_{\Theta}^{\mathrm{suc}}(\rho) = \max_{\{M_k\}} \sum_k p_k \mathrm{Tr}[U_{\phi_k}\rho U_{\phi_k}^\dagger M_k]$ .

Suppose now Alice's input state is incoherent,  $\rho \equiv \delta \in \mathcal{I}$ . Since every unitary channel  $\mathcal{U}_{\phi}$  leaves any such state invariant,  $\mathcal{U}_{\phi}(\delta) = \delta$ , the best strategy for Alice is always to cast the guess  $k^{\mathrm{max}}$  corresponding to the phase with the highest prior probability  $p_{k^{\mathrm{max}}} \coloneqq \max_k p_k$ . This results in an optimal probability of success for any incoherent state given by  $p_{\Theta}^{\mathrm{suc}}(\mathcal{I}) \coloneqq p_{k^{\mathrm{max}}}$ , which can be achieved even without actually probing the channel, just by a fixed guess.

It is clear that, by preparing a coherent state  $\rho \notin \mathcal{I}$ , Alice can expect to do better. What is less obvious yet more remarkable is that the maximum advantage achievable by using  $\rho$  as opposed to any incoherent probe  $\delta$ , in all possible PD games, is quantified exactly by the ROC of  $\rho$ . More precisely [34],

$$
\max  _ {\Theta} \frac {p _ {\Theta} ^ {\text {s u c c}} (\rho)}{p _ {\Theta} ^ {\text {s u c c}} (\mathcal {I})} = 1 + \mathcal {C} _ {\mathcal {R}} (\rho). \tag {11}
$$

The maximum is achieved for the PD game  $\Theta^{\star} \equiv \{(1 / d, 2\pi k / d)\}_{k = 0}^{d - 1}$ . Therefore,  $\mathcal{C}_{\mathcal{R}}(\rho)$  exactly quantifies, in particular, how useful the state  $\rho$  is for reliable decoding and transmission of messages encoded by generalized phase channels  $\rho \mapsto Z^k\rho Z^{\dagger k}$  with  $Z|j\rangle = \exp [i(2\pi /d)j]|j\rangle$ . These channels feature in several quantum information tasks such as quantum error correction [62], cloning [63], and dense coding [64,65]. This suggests a prominent role of coherence, specifically measured by the ROC, in quantum communication.

We notice that one can consider more general channel discrimination (CD) games, where each game is associated with a set of pairs  $\{(p_k,\Lambda_k)\}_{k = 0}^{m - 1} \eqqcolon \Upsilon$  with  $\{\Lambda_k\}$  a set of  $m$  (generally nonunitary) channels. For each CD game  $\Upsilon$ , Alice's goal is still that of discriminating which  $\Lambda_{k}$  gets applied by a black box to an input  $\rho$ , and she succeeds with optimal probability  $p_{\Upsilon}^{\mathrm{succ}}(\rho) = \max_{\{M_k\}}\sum_k p_k\mathrm{Tr}[\Lambda_k(\rho)M_k]$ , where we optimize over measurements similarly as before. By virtue of Eq. (2), for any CD game  $\Upsilon$  it holds that  $p_{\Upsilon}^{\mathrm{succ}}(\rho) \leq [1 + \mathcal{C}_{\mathcal{R}}(\rho)]p_{\Upsilon}^{\mathrm{succ}}(\mathcal{I})$ , where  $p_{\Upsilon}^{\mathrm{succ}}(\mathcal{I})$  is the best probability of success by using as input any incoherent state. In general,  $p_{\Upsilon}^{\mathrm{succ}}(\mathcal{I})$  can be higher than  $p_{k^{\max}}$ , because the channels  $\Lambda_{k}$  may act nontrivially on incoherent states. Nonetheless, if one focuses on a subclass of CD games  $\{\Upsilon^{\star}\} \ni \Theta^{\star}$  containing the PD game  $\Theta^{\star}$ , one gets  $\max_{\Upsilon \in \{\Upsilon^{\star}\}}(p_{\Upsilon}^{\mathrm{succ}}(\rho) / p_{\Upsilon}^{\mathrm{succ}}(\mathcal{I})) = 1 + \mathcal{C}_{\mathcal{R}}(\rho)$ . The ROC  $\mathcal{C}_{\mathcal{R}}(\rho)$  thus quantifies the maximum achievable advantage in any CD task in which the phase channels  $Z^{k}$  are some of the possible channels applied to a probe  $\rho$ . It will be a worthy development to extend this analysis to the scenario of assisted CD games, where the collaboration of a correlated party Bob may further increase Alice's probability of success in the discrimination [66].

We conclude by remarking that the definition (1) can be extended to a more abstract notion of robustness of asymmetry [34], in which the free states (symmetric states) are those invariant under the action of a group [18]. Specifically, given a symmetry group  $\mathsf{G}$  with associated unitary representation  $\{U_g\}_{g\in \mathsf{G}}$  on the Hilbert space  $\mathcal{H}$ , and defining the action of  $U_{g}$  on a state  $\rho \in \mathcal{D}(\mathcal{H})$  as

$\mathcal{U}_g(\rho) = U_g\rho U_g^\dagger$ , a state  $\sigma \in \mathcal{D}(\mathcal{H})$  is symmetric with respect to  $\mathsf{G}$  if and only if  $\mathcal{U}_g(\sigma) = \sigma$  for all  $g \in \mathsf{G}$ . Denoting by  $\mathcal{S}$  the convex set of all symmetric states, the robustness of asymmetry of a state  $\rho$  is then defined as  $\mathcal{A}_{\mathcal{R}}(\rho) = \min_{\tau \in \mathcal{D}(\mathcal{H})} \{s \geq 0 | (\rho + s\tau) / (1 + s) =: \sigma \in \mathcal{S}\}$ , i.e., as the minimum weight of another state  $\tau$  such that its convex mixture with  $\rho$  yields a symmetric state  $\sigma$ . Then, suitable adaptations of all the properties demonstrated above in Eqs. (3)-(9) carry over to the robustness of asymmetry, including the SDP evaluation and an operational interpretation in the context of channel discrimination games [34]. Coherence can be recovered as a special case of asymmetry with respect to the  $d$ -dimensional representation of the compact group  $\mathsf{U}(1)$ .

The approach pursued in this Letter, based on the generalized notion of robustness, appears accordingly quite versatile to define and validate insightful quantifiers of resources in quantum physics [36] and beyond [35,67], as demonstrated here for the fundamental case of quantum coherence.

This work has received funding from the European Research Council (ERC StG GQCOP, Grant No. 637352), from the European Union's Horizon 2020 research and innovation programme under Marie Skłodowska-Curie Grant Agreement No. 661338 and the Erasmus+Programme. We thank D. Girolami, M. Hall, I. Marvian, M. B. Plenio, A. Streltsov, and J. Vaccaro for useful discussions.

[1] B. Hensen, H. Bernien, A. Drelau, A. Reiserer, N. Kalb, M. Blok, J. Ruitenberg, R. Vermeulen, R. Schouten, C. Abellán, W. Amaya, V. Pruneri, M. W. Mitchell, M. Markham, D. Twitchen, D. Elkouss, S. Wehner, T. Taminiau, and R. Hanson, Nature (London) 526, 682 (2015).  
[2] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015).  
[3] L. K. Shalm et al., Phys. Rev. Lett. 115, 250402 (2015).  
[4] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2010).  
[5] "A little bit, better," The Economist, June 20, 2015, http://www.economist.com/news/science-and-technology/21654566-after-decades-languishing-laboratory-quantum-computers-are-attracting.  
[6] J. P. Dowling and G. J. Milburn, Phil. Trans. R. Soc. A 361, 1655 (2003).  
[7] R. Horodecki, P. Horodecki, M. Horodecki, and K. Horodecki, Rev. Mod. Phys. 81, 865 (2009).  
[8] K. Modi, A. Brodutch, H. Cable, T. Paterek, and V. Vedral, Rev. Mod. Phys. 84, 1655 (2012).  
[9] N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani, and S. Wehner, Rev. Mod. Phys. 86, 419 (2014).  
[10] S. Lloyd, J. Phys. Conf. Ser. 302, 012037 (2011).  
[11] S.F. Huelga and M.B. Plenio, Contemp. Phys. 54, 181 (2013).  
[12] J. Åberg, arXiv:quant-ph/0612146.  
[13] T. Baumgratz, M. Cramer, and M. B. Plenio, Phys. Rev. Lett. 113, 140401 (2014).  
[14] F. Grosshans, G. Van Assche, J. Wenger, R. Brouri, N. J. Cerf, and P. Grangier, Nature (London) 421, 238 (2003).

[15] V. Giovannetti, S. Lloyd, and L. Maccone, Nat. Photonics 5, 222 (2011).  
[16] M. Lostaglio, D. Jennings, and T. Rudolph, Nat. Commun. 6, 6383 (2015).  
[17] V. Narasimhachar and G. Gour, Nat. Commun. 6, 7689 (2015).  
[18] I. Marvian and R. W. Spekkens, New J. Phys. 15, 033001 (2013).  
[19] F. Levi and F. Mintert, New J. Phys. 16, 033007 (2014).  
[20] I. Marvian, R.W. Spekkens, and P. Zanardi, arXiv: 1510.06474.  
[21] A. Streltsov, U. Singh, H. S. Dhar, M. N. Bera, and G. Adesso, Phys. Rev. Lett. 115, 020403 (2015).  
[22] S. Du, Z. Bai, and Y. Guo, Phys. Rev. A 91, 052120 (2015).  
[23] S. Cheng and M. J. W. Hall, Phys. Rev. A 92, 042101 (2015).  
[24] U. Singh, M. N. Bera, H. S. Dhar, and A. K. Pati, Phys. Rev. A 91, 052115 (2015).  
[25] A. Winter and D. Yang, Phys. Rev. Lett. 116, 120404 (2016).  
[26] Y. Peng, Y. Jiang, and H. Fan, Phys. Rev. A 93, 032326 (2016).  
[27] A. Streltsov, arXiv:1511.08346.  
[28] J. A. Vaccaro, F. Anselmi, and H. M. Wiseman, Int. J. Quantum. Inform. 01, 427 (2003).  
[29] S. D. Bartlett, T. Rudolph, and R. W. Spekkens, Rev. Mod. Phys. 79, 555 (2007).  
[30] J. A. Vaccaro, F. Anselmi, H. M. Wiseman, and K. Jacobs, Phys. Rev. A 77, 032114 (2008).  
[31] G. Gour and R. W. Spekkens, New J. Phys. 10, 033023 (2008).  
[32] G. Gour, I. Marvian, and R. W. Spekkens, Phys. Rev. A 80, 012307 (2009).  
[33] I. Marvian and R.W. Spekkens, Nat. Commun. 5, 3821 (2014).  
[34] M. Piani, M. Cianciaruso, T. R. Bromley, C. Napoli, N. Johnston, and G. Adesso, coordinated paper, Phys. Rev. A, 042107 (2016).  
[35] B. Coecke, T. Fritz, and R. Spekkens, Inf. Comput., doi:10.1016/j.ic.2016.02.008 (2016).  
[36] F.G. S.L. Brandão and G. Gour, Phys. Rev. Lett. 115, 070503 (2015).  
[37] T. R. Bromley, M. Cianciaruso, and G. Adesso, Phys. Rev. Lett. 114, 210401 (2015).  
[38] E. Chitambar and G. Gour, arXiv:1602.06969.  
[39] I. Marvian and R. W. Spekkens, arXiv:1602.08049.  
[40] B. Yadin, J. Ma, D. Girolami, M. Gu, and V. Vedral, arXiv: 1512.02085.  
[41] D. Girolami, Phys. Rev. Lett. 113, 170401 (2014).  
[42] G. Vidal and R. Tarrach, Phys. Rev. A 59, 141 (1999).  
[43] M. Steiner, Phys. Rev. A 67, 054305 (2003).  
[44] M. Piani and J. Watrous, Phys. Rev. Lett. 114, 060404 (2015).  
[45] J. Geller and M. Piani, J. Phys. A 47, 424030 (2014).  
[46] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.116.150502, which contains the MATLAB code to evaluate the ROC for arbitrary quantum states, as well as from experimental data.  
[47] C.-M. Li, N. Lambert, Y.-N. Chen, G.-Y. Chen, and F. Nori, Sci. Rep. 2, 885 (2012).  
[48] J. Eisert, F. G. Brandão, and K. M. Audenaert, New J. Phys. 9, 46 (2007).

[49] O. Gühne and G. Tóth, Phys. Rep. 474, 1 (2009).  
[50] A coherence witness  $W$  could also be defined by  $\Delta(W) = 0$ , but relaxing the latter to  $\Delta(W) \geq 0$  is experimentally friendlier, and sets the scene for a practical verification of coherence.  
[51] L. Vandenberghe and S. Boyd, SIAM Rev. 38, 49 (1996).  
[52] F. G. S. L. Brandão, Phys. Rev. A 72, 022310 (2005).  
[53] MATLAB, version 8.5.0 (R2015a), The MathWorks Inc., Natick, Massachusetts, 2015.  
[54] M. Grant and S. Boyd, cvx: Matlab software for disciplined convex programming, version 2.1, http://cvxr.com/cvx (2014).  
[55] M. Grant and S. Boyd, in *Recent Advances in Learning and Control*, Lecture Notes in Control and Information Sciences, edited by V. Blondel, S. Boyd, and H. Kimura (Springer-Verlag Limited, Berlin, 2008), pp. 95–110; http://stanford.edu/~boyd/graph_dcp.html.  
[56] M. Sarovar, A. Ishizaki, G. R. Fleming, and K. B. Whaley, Nat. Phys. 6, 462 (2010).  
[57] A.K. Ekert, C.M. Alves, D.K.L. Oi, M. Horodecki, P. Horodecki, and L.C. Kwek, Phys. Rev. Lett. 88, 217901 (2002).

[58] S. Vinjanampathy and A.R.P. Rau, Phys. Rev. A 82, 032336 (2010).  
[59] S. M. Hashemi Rafsanjani, M. Huber, C. J. Broadbent, and J. H. Eberly, Phys. Rev. A 86, 062303 (2012).  
[60] Generalized  $X$  states are defined as  $\rho = \sum_{k=0}^{d/2} \rho_k$  if  $d$  is even, and  $\rho = \sum_{k=0}^{\lfloor d/2 \rfloor} \rho_k + \rho_c$  if  $d$  is odd, with  $\rho_k = \rho_{kk}|k\rangle \langle k| + \rho_{k,d-1-k}|k\rangle \langle d-1-k| + \rho_{d-1-k,k}|d-1-k\rangle \langle k| + \rho_{d-1-k,d-1-k}|d-1-k\rangle \langle k|$  and  $\rho_c = \rho_{\lfloor d/2 \rfloor+1} | \lfloor d/2 \rfloor + 1 \rangle \times \langle \lfloor d/2 \rfloor + 1 \rvert$ .  
[61] R. Horodecki and M. Horodecki, Phys. Rev. A 54, 1838 (1996).  
[62] D. Gottesman, Chaos, Solitons Fractals 10, 1749 (1999).  
[63] N.J. Cerf, J. Mod. Opt. 47, 187 (2000).  
[64] T. Hiroshima, J. Phys. A 34, 6907 (2001).  
[65] R. F. Werner, J. Phys. A 34, 7081 (2001).  
[66] E. Chitambar, A. Streltsov, S. Rana, M.N. Bera, G. Adesso, and M. Lewenstein, Phys. Rev. Lett. 116, 070402 (2016).  
[67] L. del Rio, L. Kramer, and R. Renner, arXiv:1511.08818.