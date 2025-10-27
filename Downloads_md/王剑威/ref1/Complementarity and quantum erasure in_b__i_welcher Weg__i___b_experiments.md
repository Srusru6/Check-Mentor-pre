# Complementarity and quantum erasure in welcher Weg experiments

Gunnar Björk* and Anders Karlsson  
Department of Electronics, Royal Institute of Technology (KTH), Electrum 229, 164 40 Kista, Sweden  
(Received 16 October 1997; revised manuscript received 2 July 1998)

We extend the concept of distinguishability and likelihood introduced by Englert in Phys. Rev. Lett. 77, 2154 (1996) to encompass quantum erasure. We delineate the necessary and sufficient condition for obtaining optimal values of distinguishability and erasure. Finally we apply these measures on a gedanken welcher Weg experiment consisting of a coupled atom-photon interferometer. [S1050-2947(98)08311-5]

PACS number(s): 03.65.Bz, 42.50.-p

# I. INTRODUCTION

A fundamental notion of quantum mechanics is that of complementarity. If we know, e.g., the location of an object so it becomes particlelike, then no wavelike behavior, like interference, can be observed, and vice versa. Recently Englert showed a fundamental inequality between the fringe visibility and the distinguishability [1] in a welcher Weg measurement. What is notable with Englert's derivation is that it is logically independent of any uncertainty principle, it relies solely on the unitary transformation of the object and meter states [1-3].

In this paper we discuss the connection between Englert's somewhat abstractly defined distinguishability (see below) and the distinguishability measured by some specific detector. As we shall see below, and Englert points out in his paper, unless one carefully matches ones detector to the state containing the welcher Weg information, one will not be able to extract the full welcher Weg information that is available. We also extend Englert's analysis to include quantum erasure [2,4-7]. Quantum erasure is a procedure where the state in which the welcher Weg information is encoded is manipulated in such a way as to prevent the welcher Weg information from being extracted with the chosen detector. In a quantum erasure experiment this loss of welcher Weg information is traded against the reappearance of the complementary information, i.e., the object interference fringes. (The complementary information is quantified by the visibility of the interference fringes.) This is what sets quantum erasure apart from, e.g., simple additive detector noise, which destroys information without trading it for complementary information.

In previous treatments of quantum erasure, specific schemes have been discussed. Our treatment, on the other hand, is general and clearly spells out what is needed in terms of unitary transformations to do quantum erasure. To delineate the trade-off between welcher Weg information and the visibility we extend the visibility measure to include conditioned visibility. With these concepts we demonstrate the conditions under which it is possible to erase the welcher Weg information contained in the meter state and to what extent this will lead to an improved (conditional) visibility.

Let us consider the schematic setup depicted in Fig. 1.

The object is set up by a 'beam splitter' in a superposition of taking the upper (+) path and the lower (-) path, with associated object states  $\{|+_{n}\rangle\}$  and  $\{|-_{n}\rangle\}$ . The object states  $|+_{n}\rangle$  and  $|+_{p}\rangle$  are orthogonal, both with the object in the (+) path but with the object in different internal states, when  $n \neq p$ . To exemplify, if the object is a two-level atom, the  $|+_{0}\rangle$  state may designate the atom localized to the upper path in its ground state while  $|+_{1}\rangle$  may designate the atom localized to the upper path in its excited state. A meter subsequently interacts with the two object modes under a possibly nonunitary transformation  $\hat{U} = \hat{U}_{+} \otimes \hat{U}_{-}$ , where the fact that the upper and lower object paths are physically separated allows us to factorize  $\hat{U}$  into distinct upper- and lower-path transformations. After the interaction we allow the possibility of a unitary transformation  $\hat{U}_{m}$  that is local to the meter. Subsequently we detect the state of the meter by a detector. We note that it is possible to choose many different kinds of detectors for the meter, so after we have detected in which path the object is in, the meter is, in general, not in any of the detector's associated eigenstates.

In the paragraph above we have introduced the term object and meter as if these terms were unambiguous. In reality this is not the case. What constitutes, e.g., the object is defined by the detectors (not shown in Fig. 1) that need to be inserted in the two paths to measure which path the object took, or to measure the object interference visibility. In theory the detectors may be "sharp," i.e., they will "click" only if a particular state impinges on them.

By defining the object as a particular quantum state, it becomes meaningless to talk about the object and the state of the object as separate entities. According to this definition, if the state of the object changes, the object ceases to exist (the object detector will not "click"). This is in contrast to our everyday notion where most of us think about, e.g., an atom as an object that has a physical existence independent of its

![](images/59ac6f852a9bcefc5ba6ad9bfdd5055f5f3a53610ef031563dc09a125f13ea99.jpg)  
FIG. 1. A schematic setup of a welcher Weg experiment.

quantum state. However, while it may seem "natural" to speak about a two-level atom having a physical existence regardless of whether it is in its excited or its ground state, the picture becomes more ambiguous if we assume that the object is a single photon. In this case subtraction of one energy quanta (the equivalent to the emission of one quanta from an excited atom) would leave the object in the electromagnetic ground state. We believe that few physicists would still think about this zero-point field as the "object" (which was a one-photon state) but in a different state. Hence, from this point of view it is natural to define the object in terms of a particular quantum state (which must be one of the detector's associated eigenstates). Defining the object in terms of a single quantum state the analysis in [1] is sufficient to describe the distinguishability and visibility of any welcher Weg experiment in which all null (= no "click") results are ignored. Note that the same sharp detectors need to be used both to determine which path the object took and to measure the visibility. In both cases null results must be ignored.

However, in practice many detectors are not "sharp," they will have insufficient resolution to distinguish between different states. To exemplify, suppose a slow Rb atom, moving at  $1\mathrm{m / s}$  is "beam-split" and we want to measure which path it took. Furthermore, suppose we chose to define the "object" by measuring the linear momentum of the Rb atom. The presence of the object would be defined by a linear momentum measurement result of  $1.4\times 10^{-22}(\mathrm{kg~m})$  in one of the paths. If the meter consisted of a pulse of photons at 780-nm wavelength (the Rb  $D_{2}$  line), and if for some reason the object-meter interaction leaves the Rb atom in its excited state, then the atom's state will change and so will the atom's linear momentum. The momentum change would be approximately  $\pm 8.5\times 10^{-28}(\mathrm{kg~m})$  (depending on whether the photon copropagates or counterpropagates with the atom), that is, less than 1 part in  $10^{5}$  of the atom's total momentum. Hence, it is unlikely that the detectors will be able to resolve the slight momentum shift. Therefore one of the detectors will click indicating the presence of the object although the Rb atom was in a state orthogonal to its ground state, which was our definition of the object. We see that in this case it is hard to analyze the outcome of the experiment using a theory that defines the object in terms of a particular state. We believe it is still meaningful to talk about the object by taking one path or the other (at least subsequent to a measurement), although the object may be in one of two (orthogonal) internal states. As indicated above we will therefore define the object in terms of two sets of states  $\{|+_{n}\rangle\}$  and  $\{|-_{n}\rangle\}$ , which can be associated with detector clicks from an upper and lower path detector, respectively. Note that, e.g., the electromagnetic ground state may belong to these sets, somewhat contrary to the everyday usage of the term "object." We will discuss this further in Sec. IV. We have already introduced the notation "internal state" to distinguish the respective states within each set from each other. It is our hope that this extension of Englert's work in terms of internal states is helpful to experimentalists that usually do not possess infinitely "sharp" object detectors. Finally we note that throughout the paper we will assume that the meter detector is sharp. The rationale for this assumption is that it is the state of the meter we want to use to be able to predict which path the object will be found in. Therefore, if the

meter detector is unsharp, the whole objective with our analysis, and any associated experiment, will fail. In reality, experiments are usually designed with an intentional asymmetry between the meter and the object to assure that a suitable sharp meter detector can be implemented.

We start the analysis by reiterating Englert's definitions. The preinteraction object is assumed to be described by its density operator  $\hat{\rho}_0$ , where we have assumed that only one of the object internal states is excited. The (a priori) predictability  $P$  of the object being found in the upper or the lower path is

$$
P \equiv | \langle + _ {0} | \hat {\rho} _ {0} | + _ {0} \rangle - \langle - _ {0} | \hat {\rho} _ {0} | - _ {0} \rangle | \equiv | w _ {+} - w _ {-} |, \tag {1}
$$

where  $|+_{0}\rangle$  and  $|-_{0}\rangle$  represent identical internal states with the object in the upper and lower path, respectively. The predictability satisfies  $0 \leqslant P \leqslant 1$ , where  $P = 0$  represents no a priori knowledge of which path the object will be found in and  $P = 1$  represents the case where there is no uncertainty as to which path the object will be found in. The two cases correspond to object 'beam splitters' with transmittivities of  $50\%$  and 0 or  $100\%$ . As demonstrated by Englert, the maximum preinteraction visibility of an object interferometer is  $V_{\mathrm{max}} = (1 - P^2)^{1 / 2}$  and this visibility requires  $\hat{\rho}_0$  to represent a pure state. If one is to predict (or estimate) which path one will find the object one strategy one may use is a Maximum likelihood estimation. This strategy dictates that in every realization one should predict the path with the highest a priori probability. If, e.g.,  $w_{+} > w_{-}$  one should predict that the object will be found in the upper path in every realization. Hence, the likelihood  $L$  of correctly estimating in which path the object will be found is  $L = w_{+} = (w_{+} + w_{-} + w_{+} - w_{-}) / 2 = (1 + P) / 2$ . The last equality follows from the fact that  $\mathrm{Tr}\{\hat{\rho}_0\} = |\langle +_0|\hat{\rho}_0| + _0\rangle +\langle -_0|\hat{\rho}_0| - _0\rangle |\equiv w_+ + w_- = 1$ .

The interaction will in general entangle the object and the meter. Hence, the post-interaction total object and meter density matrix

$$
\hat {\rho} = \hat {U} \hat {\rho} _ {o} \otimes \hat {\rho} _ {D} \hat {U} ^ {\dagger}, \tag {2}
$$

where  $\hat{\rho}_D$  corresponds to the preinteraction density operator of the meter, will in general be nonseparable. Englert defined the (postinteraction) distinguishability  $D$  of the object to be in the upper and lower path as

$$
\begin{array}{l} D = \operatorname {T r} _ {\mathrm {D}} \left\{\left| \sum_ {n} \left(\hat {\rho} _ {+ n} - \hat {\rho} _ {- n}\right) \right| \right\} \leqslant \sum_ {n} D _ {n} \\ \equiv \sum_ {n} \operatorname {T r} _ {\mathrm {D}} \left\{\left| \hat {\rho} _ {+ n} - \hat {\rho} _ {- n} \right| \right\}, \tag {3} \\ \end{array}
$$

where  $|\hat{A}| \equiv \sqrt{\hat{A}^{\dagger}\hat{A}}$  denotes the absolute value of the operator  $\hat{A}$  and the trace is taken over the meter states. The operator  $\hat{\rho}_{+n} \equiv \langle +_n|\hat{\rho} | + _n\rangle$  and correspondingly for  $\hat{\rho}_{-n}$ . The distinguishability is hence the sum of the Hilbert-space distances between the meter density operators conditioned on the respective state  $| + _n\rangle$  and  $| - _n\rangle$  of the object.

We note that Eq. (3) actually differs from that of Englert in two respects. First we have used un-normalized condi-

tioned density operators  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{+n}$ . The reason for this is mainly to simplify subsequent notation. Second, as discussed above, we have allowed for the possibility that the object changes its internal state as a consequence of the interaction with the meter. Keeping with our definition of the object, we therefore sum  $\hat{\rho}_{+n} - \hat{\rho}_{-n}$  over all object internal states. If the object detector is sharp, these states can be separated and a separate distinguishability  $D_{n}$  can be assigned to each subensemble. This will lead to a higher distinguishability except if all  $n$  operators  $(\hat{\rho}_{+n} - \hat{\rho}_{-n})$  are orthogonal, in which case  $D = \Sigma_{n}D_{n}$ . The latter case is ensured if both the object and the meter preinteraction states are pure, the interaction described by  $\hat{U}$  is unitary and (as we have assumed) the meter detector is sharp. In this case identification of the respective  $D_{n}$ 's can be achieved through the outcome of the meter measurement.

The postinteraction likelihood of estimating in which path the object will be found by an optimal measurement is  $L = (1 + D) / 2$ . It is worth noticing that the a priori information about the path the object took is built into  $D$ . For example, if  $\hat{U}$  is the identity operator then

$$
\hat {\rho} _ {\pm n} = \hat {\rho} _ {D} \otimes \left\langle \pm_ {n} \right| \hat {\rho} _ {o} | \pm_ {n} \rangle = \left\{ \begin{array}{l l} 0 & \text {i f} n \neq 0 \\ w _ {\pm} \hat {\rho} _ {D} & \text {i f} n = 0. \end{array} \right. \tag {4}
$$

Hence, in this case,  $D = P$ .

# II. MEASURED DistinguISHABILITY

As stated above, the distinguishability  $D$  defined by Englert is the optimum distinguishability. In general the distinguishability inferred from a measurement will be smaller than  $D$  since the meter detector will not optimally use the Hilbert-space distance between the operators  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$ . It is particularly convenient to express these operators in the complete orthonormal basis associated with the detector,  $\{|\psi_i\rangle\}$ . A measurement of the meter will collapse its state into one of the detector eigenstates. Only if the meter states corresponding to  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  have different (meter) detector statistics is it possible to get any path information from such a measurement. To exemplify, if  $|\psi_0\rangle$  and  $|\psi_1\rangle$  are detector eigenstates, then the states  $|\xi_0\rangle = (|\psi_0\rangle + |\psi_1\rangle) / \sqrt{2}$  and  $|\xi_1\rangle = (|\psi_0\rangle - |\psi_1\rangle) / \sqrt{2}$  are orthogonal, but they are indistinguishable by the detector, since the probability of collapsing  $|\xi_0\rangle$  and  $|\xi_1\rangle$  into e.g.,  $|\psi_0\rangle$  are both equal to 1/2, and the same for  $|\psi_1\rangle$ . If, on the other hand, we chose a detector for which  $|\xi_0\rangle$  and  $|\xi_1\rangle$  were both eigenstates, then we could distinguish perfectly between these states. We see that our choice of detector will influence how well we can read the welcher Weg information in the meter, and as we shall see below the choice of (effective) detector provides the foundation on which quantum erasure schemes are based.

The measured distinguishability  $D_{m}$  is given by

$$
\begin{array}{l} D _ {m} = \sum_ {i} \left| \right.\left\langle \right. \psi_ {i} \left. \right| \hat {U} _ {m} \sum_ {n} \left(\hat {\rho} _ {+ n} - \hat {\rho} _ {- n}\right) \hat {U} _ {m} ^ {\dagger} \mid \psi_ {i} \left. \right\rangle\left. \right| \leqslant \sum_ {n} D _ {m _ {n}} \\ \equiv \sum_ {n} \sum_ {i} | \langle \psi_ {i} | \hat {U} _ {m} (\hat {\rho} _ {+ n} - \hat {\rho} _ {- n}) \hat {U} _ {m} ^ {\dagger} | \psi_ {i} \rangle |, \tag {5} \\ \end{array}
$$

where we have first summed over all internal object states, then allowed for a unitary transformation local to the meter and then finally projected the conditioned summed density matrices of the meter onto the detector eigenstates. The absolute value of this detector outcome probability difference constitutes our measure of how well the which-path information can be read out. (The measured distinguishability is denoted the "knowledge"  $K_W$  by Englert [8], and the equation above can be found implicitly in the definition of the estimation likelihood  $\mathcal{L}_w$  in [1].) We note once more that if the object and the meter preinteraction state is pure, and  $\hat{U}$  is unitary, then  $D_m = \Sigma_n D_{m_n}$ .

We note that  $\hat{\rho}_{+n} - \hat{\rho}_{-n}$  is a Hermitian operator so the diagonal operator coefficients are real valued irrespective of the chosen basis. In Eq. (5) above we have included the unitary transformation of the meter  $\hat{U}_m$ . This transformation will not affect  $D$  (or  $V$ , see below) but it will in general change  $D_m$ . If the total object and meter evolution is unitary, then one can find a unitary operator  $\hat{U}_{mn}$  so that the operator  $\hat{U}_{mn}(\hat{\rho}_{+n} - \hat{\rho}_{-n})\hat{U}_{mn}^{\dagger}$  is strictly diagonal in the detector eigenstate basis. In fact, if the object and meter preinteraction states are pure, and  $\hat{U}$  is unitary, the relation  $\langle \pm_n|\pm_p\rangle = \delta_{np}$  ensures that  $\mathrm{Tr}\{\hat{\rho}_{\pm n}\hat{\rho}_{\pm p}\} = w_{\pm n}^2\delta_{np}$  since quantum numbers are conserved in closed systems. Therefore, in such a case it is always possible to find a unitary transformation  $\hat{U}_m = \hat{U}_{m0}\otimes \hat{U}_{m1}\otimes \dots \otimes \hat{U}_{mn}$  that simultaneously makes all  $n$  operators  $\hat{U}_{mn}(\hat{\rho}_{+n} - \hat{\rho}_{-n})\hat{U}_{mn}^{\dagger}$  diagonal in the detector eigenstate basis. This operator  $\hat{U}_m$  represents the ideal postinteraction unitary transformation of the meter so that the measured distinguishability  $D_m$  equals the distinguishability  $D$ . Alternatively one can incorporate the unitary transformation  $\hat{U}_m$  in the meter detector so that this unitary transformation plus the "bare" detector constitutes an "effective" detector. This optimal "effective detector" is the one that makes all operators  $(\hat{\rho}_{+n} - \hat{\rho}_{-n})$  diagonal when expressed in the "effective" detector eigenstate basis.

It follows from the definitions (3) and (5) that  $D_{m} \leqslant D$  and that the equality holds if and only if  $\hat{U}_{m}(\hat{\rho}_{+n} - \hat{\rho}_{-n})\hat{U}_{m}^{\dagger}$  is diagonal in the detector eigenstate basis for all  $n$ . Under certain conditions (to be derived below) it is also possible to find a different  $\hat{U}_{m}$  so that  $D_{m} = 0$  although  $D$  may be unity. This corresponds to total quantum erasure, the conditioned states of the meter has been projected onto the detector in such a way that the path information encoded on the meter cannot be extracted.

The visibility  $V$  for the setup in Fig. 1 is defined as

$$
\begin{array}{l} V = 2 \left| \sum_ {n} \langle + _ {n} | \operatorname {T r} _ {\mathrm {D}} \{\hat {\rho} \} | - _ {n} \rangle \right| \leqslant \sum_ {n} V _ {n} \\ \equiv \sum_ {n} 2 | \langle + _ {n} | \operatorname {T r} _ {\mathrm {D}} \{\hat {\rho} \} | - _ {n} \rangle |. \tag {6} \\ \end{array}
$$

This definition, too, is contingent on our definition of the object. We sum over all the object internal states since the set of states are defined to be the object. Superficially, the outcome of the meter measurement plays no role. However, if the preinteraction state of the object and meter are pure and

$\hat{U}$  is unitary, the postinteraction state of the meter will allow one to identify the internal state of the object. This will lead to identification of the respective visibilities  $V_{n}$ , which, in general, will result in a higher visibility than if the meter detector outcome is simply ignored (or the meter is not detected at all).

A fundamental inequality Englert implicitly established was

$$
D _ {n} ^ {2} + V _ {n} ^ {2} \leqslant \left(w _ {+ n} + w _ {- n}\right) ^ {2}, \tag {7}
$$

where  $w_{\pm n} = \mathrm{Tr}_{\mathrm{D}}\{\hat{\rho}_{\pm n}\}$  and where the equality sign holds if the total postinteraction state is pure. Summing over the object internal states gives us the inequality

$$
\sum_ {n} D _ {n} ^ {2} + V _ {n} ^ {2} \leqslant \sum_ {n} \left(w _ {+ n} + w _ {- n}\right) ^ {2}; \tag {8}
$$

Eq. (8) reduces to Englert's explicit result if  $w_{\pm n} \neq 0$  for one, and only one, value of  $n$ , since, in this case,

$$
\begin{array}{l} \mathrm {T r} \{\hat {U} \otimes \hat {U} _ {m} \hat {\rho_ {0}} \hat {U} _ {m} ^ {\dagger} \otimes \hat {U} ^ {\dagger} \} = \sum_ {n} (w _ {+ n} + w _ {- n}) = (w _ {+ n} + w _ {- n}) \\ = 1. \tag {9} \\ \end{array}
$$

# III. CONDITIONED VISIBILITY

In the case when  $D = 1$  then Englert's analysis asserts that  $V = 0$ . However, it follows quite naturally to ask if somehow the visibility can be resurrected when simultaneously  $D_{m} = 0$ . To this end we define a conditioned visibility, where the measurement information about the meter state is incorporated in the visibility measurement. The conditioned visibility is defined as

$$
\begin{array}{l} V _ {c} = \sum_ {i} 2 \left| \langle \psi_ {i} | \sum_ {n} \langle + _ {n} | \hat {U} _ {m} \hat {\rho} \hat {U} _ {m} ^ {\dagger} | - _ {n} \rangle | \psi_ {i} \rangle \right| \leqslant \sum_ {n} V _ {c _ {n}} \\ \equiv \sum_ {n} \sum_ {i} 2 | \langle + _ {n} | \otimes \langle \psi_ {i} | \hat {U} _ {m} \hat {\rho} \hat {U} _ {m} ^ {\dagger} | \psi_ {i} \rangle \otimes | - _ {n} \rangle |. \tag {10} \\ \end{array}
$$

Note that in contrast to  $V$ , the conditioned visibility  $V_{c}$  per definition uses the meter detector result and records the visibility of each subensemble ("labeled" by the meter detector eigen-state index  $i$ ) before adding them. It follows from the definition that  $V_{c} \geqslant V$ . This is also quite natural, because this is a type of postinteraction selection of states and such postselection can never degrade the obtained visibility, only improve it. Once again, if the object and the meter preinteraction states are pure and  $\hat{U}$  unitary,  $V_{c} = \Sigma_{n}V_{c_{n}}$  due to quantum number conservation.

The fundamental inequality for measured distinguishability and conditional visibility corresponding to (7) is

$$
\sum_ {n} D _ {m _ {n}} ^ {2} + V _ {c _ {n}} ^ {2} \leqslant \sum_ {n} \left(w _ {+ n} + w _ {- n}\right) ^ {2}. \tag {11}
$$

This is one of the central results in this paper and the proof will be outlined below. The result extends Englert's analysis to the (intentional or nonintentional) quantum erasure re

gim, and makes a natural connection between Englert's somewhat abstractly defined distinguishability  $D$  and that measured in a laboratory,  $D_{m}$  (or the knowledge reaped from the measurement, in Englert's language).

In order to achieve the upper limit of Eq. (11) a necessary but insufficient condition is that the object-meter interaction be unitary. In the following we will treat only this case. To derive the bounds for  $D_{m}$  and  $V_{c}$ , let us first assume that  $\mathrm{Tr}_{\mathrm{D}}\{\hat{\rho}_{+n}\hat{\rho}_{-n}\} = 0$  for some  $n$ , i.e., that  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  are orthogonal. Any unitary transformation will leave the density matrices  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  orthogonal. Specifically, it is possible to find a unitary transformation  $\hat{U}_m$  such that the meter states corresponding to  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  are transformed onto two orthogonal detector eigenstates,  $|\psi_{+n}\rangle$  and  $|\psi_{-n}\rangle$ . Hence, the term in the postinteraction density operator corresponding to the states  $|\pm_n\rangle$  can be expressed

$$
\left. w _ {+ n} \right| + _ {n} \rangle \langle + _ {n} | \otimes | \psi_ {+ n} \rangle \langle \psi_ {+ n} | + w _ {- n} | - _ {n} \rangle \langle - _ {n} | \otimes | \psi_ {- n} \rangle \langle \psi_ {- n} |. \tag {12}
$$

In this basis it becomes clear that  $D_{m_n} = D_n = w_{+n} + w_{-n}$ , and  $V_{c_n} = V_n = 0$ . However, if we rotate the meter state using the only nontrivial two-state unitary operator

$$
\hat {U} _ {m n} \left(\phi_ {n}\right) = \left[ \begin{array}{l l} \cos \left(\phi_ {n}\right) & i \sin \left(\phi_ {n}\right) \\ i \sin \left(\phi_ {n}\right) & \cos \left(\phi_ {n}\right) \end{array} \right], \tag {13}
$$

then it is straightforward to show that

$$
\left| w _ {+ n} - w _ {- n} \right| \leqslant D _ {m _ {n}} \leqslant w _ {+ n} + w _ {- n}, \tag {14}
$$

and

$$
0 \leqslant V _ {c _ {n}} \leqslant 2 \sqrt {w _ {+ n} w _ {- n}}. \tag {15}
$$

All values in the respective ranges can be achieved by a proper choice of rotation angle  $\phi_{n}$ . If  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  are orthogonal for all  $n$  it follows that

$$
\begin{array}{l} \left| w _ {+} - w _ {-} \right| \equiv P \leqslant \sum_ {n} \left| w _ {+ n} - w _ {- n} \right| \leqslant D _ {m} \leqslant \sum_ {n} w _ {+ n} + w _ {- n} \\ = 1 = D. \tag {16} \\ \end{array}
$$

The result is intuitive,  $D_{m}$  cannot be smaller than the a priori predictability  $P$  and cannot exceed the distinguishability  $D$ . Equation (16) also shows that only if  $w_{+n} = w_{-n}$  for all  $n$  is it possible to obtain a complete quantum erasure,  $D_{m} = 0$ . This last condition can be restated as

$$
\operatorname {T r} _ {\mathrm {D}} \left\{\left(\hat {\rho} _ {+ n} - \hat {\rho} _ {- n}\right) \right\} = 0 \quad \forall \quad n \leftrightarrow D _ {m} = 0. \tag {17}
$$

When condition (17) is fulfilled (and  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  are orthogonal for all  $n$ ) then it follows [from an explicit but trivial calculation using Eq. (13)] that  $V_{c} = 1$ . Furthermore, in this case, it can readily be shown that  $\Sigma_{n}D_{m_{n}}^{2} + V_{c_{n}}^{2}$  is independent of the unitary transformation  $\hat{U}_{m}$  and is equal to  $\Sigma_{n}(w_{+n} + w_{-n})^{2}$  for whatever values of  $\phi_{n}$  one chooses.

If  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  are orthogonal, but  $w_{+n} \neq w_{-n}$ , the sum  $\Sigma_n D_{m_n}^2 + V_{c_n}^2$  can still reach the upper limit spelled out by Eq.

(11). This limit is reached when all  $D_{m_n}$  are maximized (and hence, all  $V_{c_n} = 0$ ) by a proper choice of the rotation angles  $\phi_n$ . On the other hand, the minimum value of  $D_{m_n}^2 + V_{c_n}^2$  is given by the expression

$$
\left(w _ {+ n} + w _ {- n}\right) ^ {2} \left(1 6 y _ {n} ^ {4} - 3 2 y _ {n} ^ {3} + 2 0 y _ {n} ^ {2} - 4 y _ {n} + 1\right), \tag {18}
$$

where  $y_{n} = \max [w_{+n}, w_{-n}] / (w_{+n} + w_{-n})$ . Hence, the "worst combined" measurement of  $D_{m_n}^2 + V_{c_n}^2$  will be

$$
\min  \left[ D _ {m _ {n}} ^ {2} + V _ {c _ {n}} ^ {2} \right] = 3 \left(w _ {+ n} + w _ {- n}\right) ^ {2} / 4, \tag {19}
$$

and it will be obtained for the specific choice of relative object internal state probabilities giving  $y = (2 + \sqrt{2}) / 4$  and (assuming that  $w_{+n} > w_{-n}$ )  $\phi_n = \arccos \{[(2 + \sqrt{2}) / 4]^{1/2}\}$ .

Let us now turn over to the case when  $\left|\psi_{+n}\right\rangle$  and  $\left|\psi_{-n}\right\rangle$  are nonorthogonal for some  $n$ . It is then not possible to obtain  $D = 1$ . We define an overlap of the postinteraction conditional meter states as

$$
c _ {n} ^ {2} = \frac {\operatorname {T r} _ {\mathrm {D}} \left\{\hat {\rho} _ {+ n} \hat {\rho} _ {- n} \right\}}{w _ {+ n} w _ {- n}}, \tag {20}
$$

where  $0 \leqslant c_{n} \leqslant 1$ . Using this measure, the bounds for  $D_{m_n}$  and  $V_{c_n}$  are calculated as

$$
\begin{array}{l} \left| w _ {+ n} - w _ {- n} \right| \leqslant D _ {m _ {n}} \leqslant \left[ \left(w _ {+ n} + w _ {- n}\right) ^ {2} - 4 w _ {+ n} w _ {- n} c _ {n} ^ {2} \right] ^ {1 / 2} \\ = D _ {n}, \tag {21} \\ \end{array}
$$

and

$$
V _ {n} = 2 c _ {n} \sqrt {w _ {+ n} w _ {- n}} \leqslant V _ {c _ {n}} \leqslant 2 \sqrt {w _ {+ n} w _ {- n}}. \tag {22}
$$

These relations and Eq. (11) delineate the bounds for quantum erasure measurements. We see that in order to make  $D_{m} = 0$  the relation (17) is sufficient, the respective operators  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  need not be orthogonal. It is also possible to get  $V_{c} = 1$  in the same situation. This makes sense because in order to get maximum visibility every internal state must be split symmetrically between the two paths. On the other hand it is clear that it is not possible to get  $V = 0$  (and hence not  $V_{c} = 0$ ) when any pair  $\hat{\rho}_{+n}$  and  $\hat{\rho}_{-n}$  is simultaneously nonzero and nonorthogonal. This is also obvious, because nonorthogonal conditional meter states will prevent us from localizing the object to any one path with certainty. Therefore the object will remain in a (possibly weak) superposition of being in both paths with subsequent probability amplitude interference as a result.

# IV. A GEDANKEN EXPERIMENT

In the remainder of the paper we apply the formalism outlined above to a specific welcher Weg setup, illustrated in Fig. 2. The object is represented by a two-level atom wave packet, whose trajectory is split by the means of an  $x\pi$  pulse and one  $\pi$  pulse. If the atom initially is in its ground state  $|g\rangle$  then the exact value of  $x$  ( $0 \leqslant x \leqslant 1$ ) determines the splitting-fraction of the atom "beam splitter." The  $x\pi$  pulse prepares the atom in a superposition of the ground and the excited

![](images/c8f54c11d2440c32e6ed9af1f7dbe8a27a7480083d93052842491056f2a71f48.jpg)  
FIG. 2. The proposed experiment. A single-photon optical interferometer (top) probes the path information of an atom (bottom). The right optical beam splitter performs the photon-state rotation corresponding to  $\hat{U}_m$ .

state. Due to the linear momentum of the absorbed photon, the excited-atom wave function will have a superimposed velocity component in the direction transverse to its initial velocity. Therefore, with time, the ground- and excited-state center-of-mass wave functions will separate spatially in the vertical direction (in the figure). The subsequent  $\pi$  pulse will stimulate the excited atom to relax to the ground state and emit a photon (with unity probability), in the process restoring the transverse linear momentum so that the atomic states in path 3 (before the interaction with the meter) and path 4 have identical internal states (the ground state) but are spatially separated.

The photon interferometer in Fig. 2 has one  $50\%$  transmission beam splitter (at left) and one variable transmission beam splitter (at right). A single photon wave packet  $\left|1\right\rangle$  enters this interferometer and is put in an equal superposition of being in the upper and lower photon-interferometer path. The photon will be used to probe the upper atom path to determine which path the atom is in. Specifically, the lower photon-interferometer path mode and the upper atom interferometer path mode will interact under the interaction Hamiltonian  $\hat{H}_i$  during some interaction time  $\tau$ , giving

$$
\hat {U} _ {+} = \exp (- i \hat {H} _ {i} \tau / \hbar) \tag {23}
$$

and

$$
\hat {U} _ {-} = \hat {1}, \tag {24}
$$

where  $\hat{1}$  is the identity operator. In the language used above, the atom, in its ground or excited state, is the object and the photon, in either state  $|1\rangle$  or  $|0\rangle$  is the meter. The meter detector used are photodetectors, so the convenient basis to express the state of the meter is the number basis.

Let us assume that the atom "beam splitter" has a  $50\%$  transmittivity (implying  $x = 1 / 2$ ). Hence  $w_{+} = w_{-} = 1 / 2$ . We denote the total object and meter state by a vector  $\left|1,2,3,4\right\rangle$ , where the state in mode  $i = 1,\dots ,4$  (identified at various places of the measurement setup on Fig. 2) is indicated in the corresponding position in the state vector. The pertinent total object and meter state vector space is spanned by the five vectors  $\left|1,0,g, - \right\rangle$ ,  $\left|0,1,g, - \right\rangle$ ,  $\left|1,0, - g\right\rangle$ ,  $\left|0,1, - g\right\rangle$ , and  $\left|0,0,e, - \right\rangle$ , where 0 and 1 denote a zero- and one-photon states in the mode in question, and  $-,g$ , and  $e$  denote no atom, a ground-state atom, and an excited atom in the mode.

![](images/235b9a5c392e162d2079430aa3d28e7f549670cf1fcdd77f4439de175580c7e5.jpg)  
FIG. 3. Distinguishability and visibility as a function of the  $\hat{U}_m$  rotation angle  $\phi$ . The right beam-splitter transmittivity (in Fig. 2) corresponds to  $\cos^2 (\phi)$ .

Using this basis (in the order indicated) we can represent the total object and meter state as a five-component vector. Using the initial state  $(1,0,0,0,0)$ , the state is transformed to the state  $(1,i,i,-1,0)/2$  after the two beam splitters and the  $\pi$  pulse. The modes 1 (lower photon) and 3 (upper atom) subsequently interact under the (rotating wave) interaction Hamiltonian

$$
\hat {H} _ {i} = \hbar \Omega_ {R} \left(\hat {a} ^ {\dagger} \hat {\sigma} _ {-} + \hat {a} \hat {\sigma} _ {+}\right), \tag {25}
$$

where  $\hat{\sigma}_{-} = |g\rangle \langle e|$ , and  $\hat{\sigma}_{+} = |e\rangle \langle g|$  are the Pauli spin-flip operators,  $\hat{a}$  the photon annihilation operator, and  $\Omega_{R}$  the vacuum Rabi frequency. After an interaction time  $\tau$  the ensuing state becomes  $(\cos (\Omega \tau), i, i, -1, i \sin (\Omega \tau)) / 2$ . We see that when  $\Omega \tau$  is an even multiple of  $\pi$  the state is left unchanged and hence factorizable (this corresponds to a full Rabi cycle). When  $\Omega \tau$  is an odd multiple of  $\pi$  the state of the atom and photon modes are completely entangled, or in the language used above,  $\hat{\rho}_{+0}$  and  $\hat{\rho}_{-0}$  are orthogonal and all other operators  $\hat{\rho}_{\pm n}$  are zero. Computing  $D$  and  $V$  of this state we find that  $D = 1$  and  $V = 0$ . It is therefore possible to determine with certainty in which path the atom will be found. However, this state has  $D_{m} = 0$ , so if the second photon beam splitter has unit (or zero) transmittivity, it is impossible to distinguish the meter states conditioned on the atom in paths 3 and 4, respectively, with the chosen detector. The reason is that the meter states conditioned on the atom in paths 3 and 4 are  $(-|1,0\rangle + i|0,1\rangle) / \sqrt{2}$  and  $i(|1,0\rangle + i|0,1\rangle) / \sqrt{2}$ , respectively. These states are orthogonal but have identical diagonal density-matrix coefficients if expressed in the number-state basis. Therefore they are indistinguishable when measured with a photon-counting detector. However, as discussed above, by a suitable unitary transformation the states can be rotated so that  $\hat{\rho}_{+0} - \hat{\rho}_{-0}$  becomes strictly diagonal in the same basis. In Fig. 3 we have plotted  $D_{m_0} (= D_m)$  and  $V_{c_0} (= V_c)$  as a function of the unitary rotation angle  $\phi$ . The physical interpretation of this angle is that the transmittivity of the second photon beam splitter is  $\cos^2 (\phi)$ . We see that  $D_{m_0}$  and  $V_{c_0}$  vary periodically while  $D_{m_0}^2 + V_{c_0}^2 = 1$ , and is an invariant since  $w_{+0} = w_{-0}$  and  $\hat{\rho}_{+0}$  and  $\hat{\rho}_{-0}$  are orthogonal.

![](images/3097924964cdc2ede83b47447c569b8d613838a7799e499627700564e1d1783e.jpg)  
FIG. 4. Distinguishability and visibility as a function of  $\phi$ .

In Fig. 4 we have plotted the same quantities when the initial atom "beam-splitter" has a transmittivity of  $3/4$  ( $x = 1/6$ ) but everything else is left invariant. In this case  $\hat{\rho}_{+0}$  and  $\hat{\rho}_{-0}$  are still orthogonal, but  $w_{+0} = 3/4 \neq w_{-0} = 1/4$  due to the asymmetry in the atom "beam splitter." We find that in this case too,  $D = 1$  and  $V = 0$ . However, in this case full erasure of the information represented by the entanglement cannot be obtained since  $|w_{+0} - w_{-0}| = 1/2 \leqslant D_m \leqslant w_{+0} + w_{-0} = 1$ , as seen in the figure. Furthermore  $0 \leqslant V_c \leqslant 2\sqrt{w_{+0}w_{-0}} = \sqrt{3}/2 \approx 0.866$ . The unequal a priori path probability of the object always gives us some minimum path information ( $= P$ ). This information prevents the object from displaying full wave characteristics so that the visibility cannot reach unity.

Finally we can look at what happens if we let the atom "beam splitter" have  $50\%$  transmittivity but let  $\Omega \tau$  not be a multiple of  $\pi$ . In Fig. 5 we have used  $\Omega \tau = 5\pi /4$ , leading to the final state  $(-1,i\sqrt{2},i\sqrt{2}, - \sqrt{2}, - i) / (2\sqrt{2})$ . We see that in this case we get two  $\hat{\rho}_{+}$  operators corresponding to the atomic states  $|g\rangle$  and  $|e\rangle$ . If we give the first of these operators the index 0 and the second the index 1, we find that  $w_{+0} = 3 / 8$ ,  $w_{+1} = 1 / 8$ ,  $w_{-0} = 1 / 2$ , and  $w_{-1} = 0$ . In addition  $c_{0} = (\sqrt{2} -1) / \sqrt{6}$ , that is, the two meter states conditioned on the ground state atom in paths 3 and 4 are nonorthogonal. According to Eq. (8) this leads to

$$
\sum_ {n} D _ {n} ^ {2} + V _ {n} ^ {2} \leqslant (7 / 8) ^ {2} + (1 / 8) ^ {2} \approx 0. 7 8 1. \tag {26}
$$

We also find that  $\Sigma_{n}|w_{+n} - w_{-n}| = 0.25\leqslant D_{m}\leqslant \Sigma_{n}[(w_{+n} - w_{-n})^{2} - 4w_{+n}w_{-n}c^{2}]^{1 / 2}\approx 0.988 = D$  The fact that  $\hat{\rho}_{+0}$

![](images/7bdd903dd462293559fb0acf3c7d925d33fa9c357cafa1659b22999a75924358.jpg)  
FIG. 5. Distinguishability and visibility as a function of  $\phi$ .

and  $\hat{\rho}_{-0}$  are nonorthogonal makes it impossible to localize the atom to any one path with absolute certainty. The conditioned visibility will similarly lie in the interval  $2c_{0}\sqrt{w_{+0}w_{-0}} = V\approx 0.146\leqslant V_{c}\leqslant 2\sqrt{w_{+0}w_{-0}}\approx 0.866$ . This is quite clearly confirmed by the figure. Using these numbers it is to be noted that  $D^{2} + V^{2}\approx 0.997 < 1$  for this state.

Before concluding this section we will briefly discuss some theoretical and experimental aspects of the gedanken experiment described above. The gedanken experiment was chosen because of its computational simplicity. Both the object and meter detector outcomes are discrete, which makes the operator algebra simple. The example also demonstrates a nice duality between the object measurement and the meter measurement. To find the particlelike characteristics of the object (collapsing its wave function into one of the two possible paths) the wavelike characteristics of the meter must be used. The meter  $(= \mathrm{photon})$  must interfere in the second 50/50 beam splitter so no meter-path information can be obtained. Conversely, to restore the full object interference visibility, i.e., making the object wavelike, it is necessary to make a particlelike measurement of the meter. That is, we must make a measurement that collapses the meter into one of paths 1 or 2. Note that if neither photodetector clicks, this still represents a meter path measurement (if the photodetectors are ideal) since the state  $|0\rangle$  (somewhat counterintuitively) belongs to our set of states that defines the meter. This outcome will localize the meter to path 1, since, under the assumptions made, the only way of deexciting the meter is by exciting the object. This can only happen if the object and meter simultaneously take the paths 3 and 1, respectively. This conclusion can be experimentally confirmed by correlating the object and the meter outcomes. An ideal such experiment will show a perfect correlation between the non-observation of a photon and the simultaneous detection of an excited atom in path 3.

Of course the experiment works equally well, and can be described by the formalism above, if we designate the photon to be the object and the atom to be the meter. Nature makes no distinction between the object and the meter, and it does not matter which of the object and meter is measured first. The distinction between object and meter is only semantic and is done by the observer.

At present it is difficult to perform the experiment described above. The main difficulty is to control dissipation,

control the interaction time  $\tau$ , and to have object and meter detectors with close to unit detection efficiency and negligible noise for single quanta. However, similar welcher Weg and quantum erasure experiments have recently been performed using Rb atoms and microwave photons [9], which we believe can successfully be analyzed with our general formalism.

We finally note that our gedanken experiment is a perfect example of a case where the loss of visibility when the object's wave function is collapsed into one of the interferometer paths cannot be ascribed to a random momentum kick imparted by the meter. Instead, the loss of visibility is due to a nonlocal momentum transfer to one of the states in the postinteraction entangled object-meter superposition state [10].

# V. CONCLUSION

To conclude, we have extended Englert's analysis to encompass cases when the welcher Weg measurement changes the internal state of the object and the object detector (which defines what constitutes the object) has insufficient resolution to distinguish between the internal states. We have also discussed in detail what information actually becomes available when the meter is measured with a specific detector. We have shown that in general this detector information does not give the entire welcher Weg information encoded in the meter. We have explicitly demonstrated how to transform the conditioned meter states in such a manner as to enable the readout of the full welcher Weg information. We have also delineated the conditions for complete quantum erasure, that is, when the welcher Weg information encoded on the meter can be traded partially or completely for (conditional) object interference, quantified by the interference visibility. We have demonstrated that a complete erasure  $(D_{m} = 0$  while  $D = 1)$  requires a zero a priori predictability but ensures a conditioned visibility of unity.

# ACKNOWLEDGMENTS

The authors thank Professor Göran Lindblad and Professor Ari Laptev at KTH for illuminating discussions, and Professor B.-G. Englert for numerous critical comments. The work was supported by the Swedish Natural Science Research Council and the Swedish Technical Science Research Council.

[1] B.-G. Englert, Phys. Rev. Lett. 77, 2154 (1996).  
[2] M. O. Scully, B.-G. Englert, and H. Walther, Nature (London) 351, 111 (1991).  
[3] S. M. Tan and D. F. Walls, Phys. Rev. A 47, 4663 (1993).  
[4] M. O. Scully and K. Druhl, Phys. Rev. A 25, 2208 (1982).  
[5] M. G. Raymer and S. Yang, J. Mod. Opt. 39, 1221 (1992).  
[6] P. G. Kwiat, A. M. Steinberg, and R. Chiao, Phys. Rev. A 45,

7729 (1992).  
[7] P. G. Kwiat, A. M. Steinberg, and R. Chiao, Phys. Rev. A 49, 61 (1994).  
[8] B.-G. Englert (private communication).  
[9] S. Duerr, T. Nonn, and G. Rempe (unpublished).  
[10] H. M. Wiseman, F. E. Harrison, M. J. Collett, S. M. Tan, D. F. Walls, and R. B. Killip, Phys. Rev. A 56, 55 (1997).