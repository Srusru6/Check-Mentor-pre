# Duality of quantum coherence and path distinguishability

Manabendra Nath Bera, $^{1,*}$  Tabish Qureshi, $^{2,\dagger}$  Mohd Asad Siddiqui, $^{2,\ddagger}$  and Arun Kumar Pati $^{1,\S}$ $^{1}$ Quantum Information and Computation Group, Harish-Chandra Research Institute, Allahabad-211019, India  
 $^{2}$ Centre for Theoretical Physics, Jamia Millia Islamia, New Delhi-110025, India  
(Received 17 March 2015; published 22 July 2015)

We derive a generalized wave-particle duality relation for arbitrary multipath quantum interference phenomena. Beyond the conventional notion of the wave nature of a quantum system, i.e., the interference fringe visibility, we introduce a quantifier as the normalized quantum coherence, recently defined in the framework of quantum information theory. To witness the particle nature, we quantify the path distinguishability or the which-path information based on unambiguous quantum state discrimination. Then, the Bohr complementarity principle for multipath quantum interference can be stated as a duality relation between the quantum coherence and the path distinguishability. For two-path interference, the quantum coherence is identical to the interference fringe visibility, and the relation reduces to the well-known complementarity relation. The duality relation continues to hold in the case where mixedness is introduced due to possible decoherence effects.

DOI: 10.1103/PhysRevA.92.012118

PACS number(s): 03.65.Ta, 03.65.Aa, 03.67.Mn

# I. INTRODUCTION

One of the famous yet intriguing features of quantum mechanics is the wave-particle duality. This is often described in terms of Bohr's complementarity principle. It states that the wave aspect and the particle aspect are complementary in nature, in the sense that if an experiment clearly reveals the wave nature, it will completely hide the particle aspect and vice versa [1]. The complementarity principle has been a subject of debate since the time of its inception when Einstein proposed his famous recoiling slit experiment (see, e.g., Ref. [2]).

Since then, attempts have been made to give a quantitative meaning to the complementarity principle, in the context of interference experiments [3-5]. The idea is to investigate how much of each aspect, wave or particle, can be seen at the same time. In the two-path interference experiment, either in a two-slit experiment or in a two-path Mach-Zehnder interferometer, the principle of complementarity is quantitatively represented by the Englert-Greenberger-Yasin (EGY) relation

$$
\mathcal {V} ^ {2} + \mathcal {D} ^ {2} \leqslant 1, \tag {1}
$$

where  $\mathcal{V}$  is the visibility of the interference pattern and  $\mathcal{D}$  is a measure of path distinguishability or which-path information. For two-path interference, the quantum system (quanton) may arrive at the detector along two different paths. If the experimenter determines which path the quanton has traveled through without ambiguity (i.e.,  $\mathcal{D} = 1$ ), then no interference fringes will be seen (i.e.,  $\mathcal{V} = 0$ ). On the other hand, a nonzero ambiguity in the which-path information (i.e.,  $\mathcal{D} \neq 1$ ) of the experimenter may retain a nonvanishing fringe visibility (i.e.,  $\mathcal{V} \neq 0$ ). Thus, the knowledge of which-path information or the path distinguishability limits the interference visibility  $\mathcal{V}$  in an interference experiment, according to the above complementarity relation. This relation has been demonstrated experimentally with atoms [6], nuclear magnetic resonance

[7,8], faint lasers [9], and also with single photons [10]. Further, the complementarity relation has been extended to the more general case of an asymmetric interferometer where only a single output port is considered and this duality holds [11]. Recently, the duality relation has also been investigated in the presence of nonlocality [12] and quantum entanglement [13].

Intuitively, the complementarity relation, between the wave and the particle nature of the quantons, is expected to hold in multipath or multislit experiments too. Several attempts have been made to quantitatively formulate the complementarity principle in multipath experiments [14-17]. However, a derivation of a loophole-free generalized complementarity relation for multislit quantum interference experiment is still demanding. The underlying problem is the absence of exact analytical forms of interference fringe visibility and path distinguishability, which are strictly complementary to each other, for an  $n$ -path quantum interferometer. One may seek to resolve this difficulty by relaxing the conventional signatures of particle and wave natures of the quantons, such as which-path information and fringe visibility. While the fringe visibility is the most used signature of wave nature of the quantum particles, it is certainly not the only one to capture the essence. For example, recently, the wave-particle duality in two-slit experiments has been shown to be equivalent to the entropic uncertainty relation [18], and the wave and particle natures are represented with entropic quantifiers.

In this paper we derive a generalized complementarity relation from such an alternative perspective. In our approach, we quantify the wave nature in terms of quantum coherence, which has been proposed recently in the context of quantum information theory [19]. On the other hand, the particle nature connected to the which-path information or the path distinguishability is quantified by the upper bound of the success probability in the unambiguous quantum state discrimination (UQSD) [20-22]. Remarkably, the quantum coherence and the path distinguishability are truly complementary in nature. That means an increase in quantum coherence is always associated with a decrease in path distinguishability and vice versa. With the proposed quantifiers, we derive a generalized complementarity relation for arbitrary  $n$ -slit scenario for both pure and mixed quantum states. We show that the sum of

(normalized) quantum coherence and path distinguishability in the complementarity relation exactly equals to one for every pure state and is upper bounded by the same in the case of mixed states. Our duality relation then gives a justification to the measure of quantum coherence as it truly brings out the wave nature of the quanton at its heart.

The paper is organized as follows. In Sec. II, we introduce the quantifiers of quantum coherence and unambiguous quantum state discrimination, which quantitatively capture the wave nature and particle nature of the quantum system, respectively. The duality relation, for pure quanton and detector state is derived in Sec. III. Then we generalize the duality relation for mixed states of arbitrary dimension. Finally, we conclude in Sec. IV.

# II. QUANTUM COHERENCE AND UQSD

# A. Quantum coherence

Coherence is a fundamental feature of quantum physics, which signifies the possible superposition between the orthogonal quantum states. Again, it is largely believed that the quantum superposition is the manifestation of wave nature of quantum particles. Thus, the quantum coherence has a strong correspondence with the wave nature of a quantum particle. Though a rigorous study of coherence has been carried out in quantum optics in terms of quasiprobabilities, a generalized quantification of quantum coherence was absent until recently. In Ref. [19], Baumgratz et al., proposed a reliable quantifier of quantum coherence from quantum information theoretic approach. The framework, to quantify coherence, is based on the characterization of the set of incoherent quantum states  $(\mathcal{I})$ . For a given incoherent basis  $\{|i\rangle\}$ , the incoherent states are defined as  $\sigma^{\mathcal{I}} = \sum_{i} p_{i} |i\rangle \langle i| \in \mathcal{I}$ , where  $p_{i}$ s are nonnegative probabilities with  $\sum_{i} p_{i} = 1$ . The incoherent operations are the completely positive trace preserving (CPTP) maps  $\Lambda^{\mathcal{I}}$ , which transform  $\sigma^{\mathcal{I}} \to \Lambda^{\mathcal{I}}(\sigma^{\mathcal{I}}) \in \mathcal{I}$  to an incoherent state, which is, again, diagonal in the incoherent basis. The maximally coherent state of dimension  $n$  is defined as  $|\Psi\rangle = \frac{1}{\sqrt{n}} \sum_{i=1}^{n} |i\rangle$  and the coherence of such state is used as reference to compare the coherence in the other states. For a given incoherent basis, the reliable quantifier of quantum coherence  $\mathcal{C}(\rho)$ , is a function of the state  $\rho$ , and should satisfy [19]: (i)  $\mathcal{C}(\rho) = 0$  if and only if  $\rho \in \mathcal{I}$ , (ii)  $\mathcal{C}(\rho)$  is nonincreasing under incoherent operations, i.e.,  $\mathcal{C}(\rho) \geqslant \mathcal{C}(\Lambda^{\mathcal{I}}\rho)$ , (iii)  $\mathcal{C}(\rho)$  is nonincreasing on an average under selective incoherent measurement, i.e.,  $\mathcal{C}(\rho) \geqslant \sum_{m} q_{m} \mathcal{C}(\rho_{m})$ , where  $\rho_{m} = \frac{1}{q_{m}} K_{m} \rho K_{m}^{\dagger}$ ,  $q_{m} = \mathrm{Tr}(K_{m} \rho K_{m}^{\dagger})$ ,  $K_{m}$ s are the Kraus operators and  $K_{m} \mathcal{I} K_{m}^{\dagger} \subseteq \mathcal{I}$ , (iv)  $\mathcal{C}(\rho)$  is nonincreasing under convex mixing of density matrices, i.e.,  $\mathcal{C}(\sum_{k} q_{k} \rho_{k}) \leqslant \sum_{k} q_{k} \mathcal{C}(\rho_{k})$ . The functions of density matrix that satisfy these properties are relative entropy of coherence,  $l_{1}$  norm of coherence [19], and skew information of coherence [23]. In this work, we shall use  $l_{1}$  norm of coherence to quantify the wave nature of the quantons, defined as

$$
\mathcal {C} (\rho) = \min  _ {\sigma^ {\mathcal {I}} \in \mathcal {I}} \| \rho - \sigma^ {\mathcal {I}} \| _ {l _ {1}}, \tag {2}
$$

where  $\| A \|_{l_1} = \sum_{ij} |A_{ij}|$  and the minimization is carried out over the set of all incoherent states  $\sigma^{\mathcal{I}}$ . It can easily be seen that the minimization is achieved for the  $\sigma^{\mathcal{I}} = \sum_{i} \langle i | \rho | i \rangle |i \rangle \langle i |$

and then the coherence quantitatively becomes the sum of the absolute values of the off-diagonal elements of the density matrix of a system, i.e.,

$$
\mathcal {C} (\rho) = \sum_ {i \neq j} | \rho_ {i j} | \tag {3}
$$

with  $\rho_{ij} = \langle i|\rho |j\rangle$ . Using this measure, we define normalized quantum coherence as

$$
\mathcal {C} (\rho) = \frac {1}{n - 1} \sum_ {i \neq j} | \rho_ {i j} |, \tag {4}
$$

where  $n$  is the dimensionality of the Hilbert space. Hereafter we call normalized coherence as coherence, for simplicity. In what follows, we shall show that the coherence captures the wave nature of a quanton in a multipath quantum interference scenario.

# B. Unambiguous quantum state discrimination

Quantum state discrimination has various important applications in quantum information theory [20-22]. In the quantum state discrimination, the task is to find out which state an experimenter has in her possession to the best of her ability [20]. In quantum mechanics the existence of nonorthogonal states adds further difficulties to the problem, in addition to the statistical mixing of the quantum states. The commonly used strategies to discriminate nonorthogonal states can be divided in two broader classes, those are the ambiguous [20] and the unambiguous [24] quantum state discrimination. In ambiguous state discrimination, one always has an answer but with a probability of being wrong and the task is to minimize this probability. On the other hand, in unambiguous state discrimination, one is guaranteed to never be wrong, but sometimes may have a nonanswer, that is to say one does not know. In this case the task is to minimize the probability of a nonanswer. The unambiguous state discrimination is particularly interesting for the cases where the states analyzed are mixed [25]. However, in what follows, we shall stick to UQSD for pure states as it suffices for our analysis.

UQSD was first formulated for unambiguously discriminating between two nonorthogonal states [24]. Consider a state that could be either  $|d_1\rangle$  or  $|d_2\rangle$ , with equal probability. The probability with which one can tell for sure which of the two states is the given one is bounded by [24]

$$
P _ {2} \leqslant 1 - | \langle d _ {1} | d _ {2} \rangle |. \tag {5}
$$

One can also precisely specify the condition in which the success probability is

$$
P _ {2} = 1 - | \langle d _ {1} | d _ {2} \rangle |, \tag {6}
$$

which is the so-called Ivanovic-Dieks-Peres (IDP) limit. The two states,  $|d_1\rangle$  and  $|d_2\rangle$ , cannot be unambiguously discriminated with a probability larger than the IDP limit, even in principle. This shows that the IDP limit sets a fundamental limit to distinguish two nonorthogonal states  $|d_1\rangle$  and  $|d_2\rangle$ .

UQSD was later generalized to  $n$  nonorthogonal states [26]. Consider a quantum state prepared in one of the  $n$  states  $|d_1\rangle, \ldots, |d_n\rangle$  in an  $n$ -dimensional Hilbert space with corresponding probabilities  $p_1, \ldots, p_n$ . The states are in

general nonorthogonal. To find out which of the  $n$  states the given state is, one needs to perform one or more quantum measurements. The upper bound for the success probability of unambiguous discrimination among the  $n$  quantum states is given by [26]

$$
P _ {n} \leqslant 1 - \frac {1}{n - 1} \sum_ {i \neq j} \sqrt {p _ {i} p _ {j}} | \langle d _ {i} | d _ {j} \rangle |. \tag {7}
$$

Clearly, for orthogonal quantum states, there exists a quantum measurement strategy for which the success probability of UQSD reaches maximum to 1. For nonorthogonal states, there may exist a measurement strategy for which the success probability of UQSD is

$$
P _ {n} = 1 - \frac {1}{n - 1} \sum_ {i \neq j} \sqrt {p _ {i} p _ {j}} | \langle d _ {i} | d _ {j} \rangle |. \tag {8}
$$

However, since the above does not represent the optimal success probability, this upper bound may, in general, not be achievable. In the next section, we shall use this upper bound of the success probability for UQSD as a measure of which-path information and that in turn can witness the particle nature of the quanton.

# III. COMPLEMENTARITY OF COHERENCE AND PATH DistinguISHABILITY

# A. Duality relation for pure quantum and detector states

Let us now consider the case of an  $n$ -slit quantum interference with pure quantons. In  $n$ -slit interference, if  $|\psi_i\rangle$  is the possible state of the quanton if it takes the  $i$ th slit or  $i$ th path, then the state of the quanton after crossing the slit can be described solely in terms of  $|\psi_i\rangle$ , and it may be treated as a basis state. Thus the state of the quanton can be represented in terms of  $n$  basis states  $\{|\psi_1\rangle, |\psi_2\rangle, \ldots, |\psi_n\rangle\}$ , where each of the states represents each slit or path.

$$
| \Psi \rangle = c _ {1} | \psi_ {1} \rangle + c _ {2} | \psi_ {2} \rangle + \dots + c _ {n} | \psi_ {n} \rangle , \tag {9}
$$

and  $c_{i}$  is the amplitude of taking the  $i$ th path. In an interference experiment, if one wants to know which of the  $n$  slits the quanton passes through, or which of the  $n$  paths does the quanton take, one needs to perform a quantum measurement. In quantum measurements, according to von Neumann, the first process is to let a detector interact with a quanton and get entangled with it [27]. Then, the quantum measurements may be performed on the detector state to infer about the properties of the quanton. In general, the controlled unitary operations are used to correlate the quanton and detector in an interference experiment. For a quanton state  $|\Psi \rangle$  and controlled unitary interaction  $U(|\psi_i\rangle |0_d\rangle)\mapsto |\psi_i\rangle |d_i\rangle$ , where  $|0_d\rangle$  is the initial detector state, the combined quanton-detector state becomes

$$
| \Psi \rangle = c _ {1} | \psi_ {1} \rangle \otimes | d _ {1} \rangle + c _ {2} | \psi_ {2} \rangle \otimes | d _ {2} \rangle + \dots , c _ {n} | \psi_ {n} \rangle \otimes | d _ {n} \rangle , \tag {10}
$$

where  $|d_i\rangle$  is the state of the which-path detector if the quanton went through the  $i$ th path, and  $\sum_{i = 1}^{n}|c_{i}|^{2} = 1$ . For simplicity, we consider the detector states  $\{|d_i\rangle\}$  to be normalized, but not necessarily orthogonal. Now, if one tries to acquire knowledge about which path the quanton took, it shall reduce the coherence of the quanton. The left out coherence present

in the quanton will correspond to the coherence of the reduced density matrix of the quanton, where the latter is given by

$$
\rho_ {s} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} c _ {i} c _ {j} ^ {*} \langle d _ {j} | d _ {i} \rangle | \psi_ {i} \rangle \langle \psi_ {j} | \tag {11}
$$

after tracing over the detector states. For a given interferometric setup the set  $\{|\psi_i\rangle \}$  forms the incoherent basis. The coherence can now be calculated for the particle using the reduced density matrix given above, as

$$
\begin{array}{l} \mathcal {C} = \frac {1}{n - 1} \sum_ {i \neq j} | \langle \psi_ {i} | \rho_ {s} | \psi_ {j} \rangle | \\ = \frac {1}{n - 1} \sum_ {i \neq j} | c _ {i} | | c _ {j} | | \langle d _ {j} | d _ {i} \rangle |. \tag {12} \\ \end{array}
$$

It is interesting to note that if the detector states  $\{|d_i\rangle \}$  form a mutually orthogonal basis, the reduced system states become diagonal in the incoherent basis and hence, have vanishing coherence. This implies that, in this situation, the wave nature of the quanton cannot be seen. However, the situation will be different if the detector states are not mutually orthogonal to each other and in the reduced density matrix, the off-diagonal elements will not necessarily be vanishing. Thus, the wave aspect of the quanton will acquire nonzero value as the quantum coherence is nonvanishing. However, the coherence of the quanton will be certainly reduced more than that of the original state before the measurement interaction was turned on.

Now, let us focus on the problem of path distinguishability or which-path information, which is attributed to the particle nature of the quantons. Since, through the controlled unitary interaction, each of the paths is marked with a detector state  $|d_i\rangle$ , the path distinguishability is equivalent to discriminating the detector states. In other words, if the quanton passes through the  $i$ th path, the resulting the detector states becomes  $|d_i\rangle$  with the probability  $|c_i|^2$ . Now distinguishing all these detector states  $\{|d_i\rangle\}$  with the corresponding probabilities  $\{|c_i|^2\}$  is equivalent to distinguishing the paths the quanton chooses in the interferometric setup. If the detector states  $\{|d_i\rangle\}$  are mutually orthogonal, then the states can be distinguished with unit probability. In this case we will know which path the system has taken with certainty. However, the interesting case appears when  $\{|d_i\rangle\}$  are not mutually orthogonal and in that case we have partial knowledge about which-path information. In general, the best strategy to distinguish between nonorthogonal states is unambiguous quantum state discrimination (UQSD) [24,28,29]. In UQSD, the success probability with which nonorthogonal pure states can be unambiguously distinguished depends on the measurement strategies employed. One would like to know which strategy yields the maximum success probability. The optimal success probability of unambiguously distinguishing between  $n$  nonorthogonal states is not known. However, the success probability in the UQSD between the detector states  $\{|d_i\rangle\}$  with corresponding probabilities  $\{|c_i|^2\}$  is bounded by [26]

$$
P _ {n} \leqslant 1 - \frac {1}{n - 1} \sum_ {i \neq j} | c _ {i} | | c _ {j} | | \langle d _ {i} | d _ {j} \rangle |. \tag {13}
$$

Note that the probabilities  $|c_i|^2$  are decided by the initial superposition in the quantum state. The upper bound given by (13) may not be achievable in practice in many situations. However, it can still serve as a measure of the degree to which the  $n$  states are distinguishable, namely the  $n$  states cannot be distinguished with a probability larger than that given by the upper bound of (13). Here we define the path distinguishability  $\mathcal{D}_Q$  as the upper bound of the success probability with which the  $n$  paths of the particle can be distinguished without any error. The subscript  $Q$  is added to differentiate it from the  $\mathcal{D}$  used in Ref. [5] and elsewhere in the literature. This is just the upper bound of the success probability with which the states  $\{|d_i\rangle\}$  can be unambiguously discriminated, which is the saturation limit of (13). Thus, the path distinguishability, for  $n$ -path interference, can be defined as

$$
\mathcal {D} _ {Q} := 1 - \frac {1}{n - 1} \sum_ {i \neq j} | c _ {i} | | c _ {j} | | \langle d _ {i} | d _ {j} \rangle |. \tag {14}
$$

The path distinguishability can take values between 0 and 1. For all mutually orthogonal detector states  $\{|d_i\rangle \}$ , one has  $\mathcal{D}_Q = 1$ .

Now with the quantum coherence left in the reduced quanton state in Eq. (12) and the path distinguishability, defined in Eq. (14), we get a general  $n$ -slit duality relation, for arbitrary pure quantons, as

$$
\mathcal {C} + \mathcal {D} _ {Q} = 1. \tag {15}
$$

Using the  $\mathcal{C}$  and  $\mathcal{D}_Q$  as the quantifiers of the wave and the particle nature of the quanton, respectively, Eq. (15) puts a bound on how much of wave nature and particle nature a system can display at the same time. This can be treated as a quantitative statement of Bohr's principle for  $n$ -path interference using the measures of quantum coherence and path distinguishability. Note, the  $\mathcal{C}$  and  $\mathcal{D}_Q$  are truly complementary in nature where an increase in one results in a decrease in the other.

# 1. Two-slit interference

In a two-path interference with equally probable paths we have  $|c_{1}| = |c_{2}| = \frac{1}{\sqrt{2}}$ , and hence the path distinguishability becomes  $\mathcal{D}_Q = 1 - |\langle d_1|d_2\rangle|$ , which, interestingly, is just the IDP limit. The coherence in (12) reduces to

$$
\mathcal {C} = | \langle d _ {1} | d _ {2} \rangle |. \tag {16}
$$

However, for a double-slit experiment, the interference visibility, defined as  $\mathcal{V} \equiv \frac{I_{\mathrm{max}} - I_{\mathrm{min}}}{I_{\mathrm{max}} + I_{\mathrm{min}}}$ , where  $I_{\mathrm{max}}$  and  $I_{\mathrm{min}}$  represent the maximum and minimum intensity in neighboring fringes, respectively, is just  $\mathcal{V} = |\langle d_1|d_2\rangle|$  [2]. Therefore, the fringe visibility is just equal to the coherence  $\mathcal{C}$ . The duality relation (15) now becomes

$$
\mathcal {V} + \mathcal {D} _ {Q} = 1. \tag {17}
$$

In a practical scenario there may be other factors that reduce the visibility of fringes in interference experiments. So in the general case, the above relation will be an inequality saturating to equality. This inequality has been derived before [30], and is completely equivalent to the EGY duality relation (1) with the recognition that  $\mathcal{D}_Q = 1 - \sqrt{1 - \mathcal{D}^2}$  [30]. Therefore, for

the two-slit case the new duality relation (15) reduces to the EGY relation (1).

# 2. Three-slit interference

For the three-slit interference, the path-distinguishability becomes  $\mathcal{D}_Q = 1 - (|c_1||c_2||\langle d_1|d_2\rangle | + |c_2||c_3||\langle d_2|d_3\rangle | + |c_1||c_3||\langle d_1|d_3\rangle |)$ , and the coherence reduces to

$$
\mathcal {C} = | c 1 | | c 2 | | \langle d 1 | d 2 \rangle | + | c 2 | | c 3 | | \langle d 2 | d 3 \rangle | + | c 1 | | c 3 | | \langle d 1 | d 3 \rangle |. \tag {18}
$$

This coherence can be shown to be related to the ideal interference visibility by the relation [30]

$$
\mathcal {C} = \frac {2 \mathcal {V}}{3 - \mathcal {V}}. \tag {19}
$$

The duality relation reduces to

$$
\mathcal {D} _ {\mathcal {Q}} + \frac {2 \mathcal {V}}{3 - \mathcal {V}} = 1, \tag {20}
$$

which is exactly the same as the duality relation derived for the three-slit interference [30]. One should of course realize that in a nonideal situation the fringe visibility will be reduced and the above relation will be an inequality. Thus, for the three-slit case, the new duality relation reduces to an earlier relation derived independently.

# B. Generalization of duality relation for mixed states

We now extend the preceding analysis to the situations where a certain amount of mixedness is introduced in the density matrix of the quantum state, say  $\rho = \sum_{ij}\rho_{ij}|\psi_i\rangle \langle \psi_j|$ . This may happen if the quantum system is exposed to environment. Interference experiments have been carried out with large molecules, where the interaction with the environment, although minimized, is not fully avoided [31,32]. In a scenario where the initial detector state is chosen to be pure, the combined density matrix of the quanton and the path detector after the controlled unitary (the measurement interaction) may be written as

$$
\rho_ {s d} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \rho_ {i j} | \psi_ {i} \rangle \langle \psi_ {j} | \otimes | d _ {i} \rangle \langle d _ {j} |, \tag {21}
$$

where the quanton state becomes entangled with the detector. Note that the combined state is also mixed since the initial quanton state is mixed. As in the pure state scenario, the wavenature in the postinteraction quanton state can be quantified with the quantum coherence present in the reduced quanton state. By tracing out over the path-detector states in (21), one gets the reduced density matrix for the quanton

$$
\rho_ {s} = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \rho_ {i j} | \psi_ {i} \rangle \langle \psi_ {j} | \langle d _ {j} | d _ {i} \rangle . \tag {22}
$$

The coherence can now be calculated as

$$
\begin{array}{l} \mathcal {C} = \frac {1}{n - 1} \sum_ {i \neq j} | \langle \psi_ {i} | \rho_ {s} | \psi_ {j} \rangle | \\ = \frac {1}{n - 1} \sum_ {i \neq j} | \rho_ {i j} | | \langle d _ {j} | d _ {i} \rangle |. \tag {23} \\ \end{array}
$$

Note that, before the interaction between quantum and detector, the coherence is  $\mathcal{C} = \frac{1}{n - 1}\sum_{i\neq j}|\rho_{ij}|,$  which is reduced after the interaction due to the factors  $|\langle d_j|d_i\rangle |\leqslant 1$

Again the particle nature of the quantons can be expressed, quantitatively, by the path-distinguishability or which-path information. That requires nothing but how well an experimenter can distinguish between the detector states  $\{|d_i\rangle\}$  with the corresponding probabilities  $\{\rho_{ii}\}$ , where the probabilities are determined by the initial quantum state. One may carry out UQSD on the state  $|d_i\rangle$  as before. Since a state  $|d_i\rangle$  appears with a probability  $\rho_{ii}$ , the path distinguishability for  $n$ -path interference, which is the upper bound of success probability in UQSD, in the mixed case, can be written as

$$
\mathcal {D} _ {Q} = 1 - \frac {1}{n - 1} \sum_ {i \neq j} \sqrt {\rho_ {i i} \rho_ {j j}} | \langle d _ {i} | d _ {j} \rangle |. \tag {24}
$$

For a given quantum state, the path distinguishability and the quantum coherence of the quanton depend on the choice of initial state of the which-path detector and the measurement interaction. Now from (23) and (24), we get

$$
\mathcal {C} + \mathcal {D} _ {Q} + \frac {1}{n - 1} \sum_ {i \neq j} \left(\sqrt {\rho_ {i i} \rho_ {j j}} - | \rho_ {i j} |\right) | \langle d _ {j} | d _ {i} \rangle | = 1. \tag {25}
$$

Since every principal  $2 \times 2$  submatrix of (21) is positive semidefinite [33], we have

$$
\sqrt {\rho_ {i i} \rho_ {j j}} - | \rho_ {i j} | \geqslant 0 \tag {26}
$$

for arbitrary  $i$  and  $j$ . This in turn implies that  $\frac{1}{n - 1}\sum_{i\neq j}(\sqrt{\rho_{ii}\rho_{jj}} -|\rho_{ij}|)|\langle d_j|d_i\rangle |\geqslant 0$ . The equality holds only for the initial pure quantum systems. Thus, (25) leads to the following duality relation between the quantum coherence and the path distinguishability, which are the quantifiers of the wave nature and particle nature of a quanton respectively, given by

$$
\mathcal {C} + \mathcal {D} _ {Q} \leqslant 1. \tag {27}
$$

The above is the generalized version of (15) and applicable for any mixed quantum state. One can easily see that in an experiment where the mutual overlap between the detector states are simultaneously increased or decreased these two quantities become truly complementary in nature. Therefore, an increase in the path distinguishability inevitably reduces the quantum coherence in the quantum state, and vice versa.

Our analysis can further be extended in the case where one has the initial detector in a mixed state, as well. For the controlled-unitary operation as the measurement interaction  $U = \sum_{i} |\psi_i\rangle \langle \psi_i| \otimes U_i$  and initial detector state  $\rho_d$ , the combined quantum-detector state after the interaction becomes

$$
\rho_ {s d} = \sum_ {i j} \rho_ {i j} | \psi_ {i} \rangle \langle \psi_ {j} | \otimes U _ {i} \rho_ {d} U _ {i} ^ {\dagger}. \tag {28}
$$

If the measurement interaction leads to mutually orthogonal detector states, then  $\mathrm{Tr}(U_i\rho_dU_i^\dagger U_j\rho_dU_j^\dagger) = 0$  for  $\forall i\neq j$ . In such situation, one may easily see that  $\mathrm{Tr}(U_i\rho_dU_j^\dagger) = 0$ , for  $\forall i\neq j$ , holds. The reduced quantum state after the interaction

can be written as

$$
\rho_ {s} ^ {\prime} = \sum_ {i, j} ^ {n} \rho_ {i j} \operatorname {T r} \left(U _ {i} \rho_ {d} U _ {j} ^ {\dagger}\right) | \psi_ {i} \rangle \langle \psi_ {j} |. \tag {29}
$$

Clearly, for a good measurement interaction for which  $\mathrm{Tr}(U_i\rho_dU_j^\dagger) = 0$  for  $\forall i\neq j$ , the quantum state reduces to an incoherent state and thus the wave nature becomes absent. On the other hand if the  $\mathrm{Tr}(U_i\rho_dU_j^\dagger)\neq 0$ , there remains nonvanishing quantum coherence in the reduced quantum state, as

$$
\mathcal {C} ^ {\prime} = \frac {1}{n - 1} \sum_ {i \neq j} | \rho_ {i j} \operatorname {T r} \left(U _ {i} \rho_ {d} U _ {j} ^ {\dagger}\right) |. \tag {30}
$$

For an initial detector state, let  $\rho_{d} = \sum_{k}r_{k}|d_{k}\rangle \langle d_{k}|$  be the spectral decomposition. Then, we have  $|\rho_{ij}\mathrm{Tr}(U_i\rho_dU_j^\dagger)| = |\rho_{ij}\sum_kr_k\langle d_{ki}|d_{kj}\rangle |\leqslant \sum_kr_k|\langle d_{ki}|d_{kj}\rangle ||\rho_{ij}|$ , where we denote  $U_{i}|d_{k}\rangle = |d_{ki}\rangle$ . Thus we are lead to

$$
\mathcal {C} ^ {\prime} \leqslant \frac {1}{n - 1} \sum_ {k} r _ {k} \sum_ {i \neq j} | \rho_ {i j} | | \langle d _ {k i} | d _ {k j} \rangle |. \tag {31}
$$

Now for a given initial detector state  $|d_k\rangle$ , the success probability of UQSD for the ensemble  $\{\rho_{ii},|d_{ki}\rangle \}$  is bounded by  $\mathcal{D}_Q^k = 1 - \frac{1}{n - 1}\sum_{i\neq j}\sqrt{\rho_{ii}\rho_{jj}} |\langle d_{ki}|d_{kj}\rangle |$ , which represents the path distinguishability. Then, for the initial detector state  $\rho_d = \sum_k r_k|d_k\rangle \langle d_k|$ , the path distinguishability can be computed by averaging over the individual  $\mathcal{D}_Q^k$ s, i.e.,

$$
\begin{array}{l} \mathcal {D} _ {Q} ^ {\prime} = \sum_ {k} r _ {k} \mathcal {D} _ {Q} ^ {k} \\ = 1 - \frac {1}{n - 1} \sum_ {k} r _ {k} \sum_ {i \neq j} \sqrt {\rho_ {i i} \rho_ {j j}} | \langle d _ {k i} | d _ {k j} \rangle |. \tag {32} \\ \end{array}
$$

Now, using Eqs. (26), (31), and (32), we arrive at the most general duality relation

$$
\mathcal {C} ^ {\prime} + \mathcal {D} _ {Q} ^ {\prime} \leqslant 1. \tag {33}
$$

Thus, Eqs. (15), (27), and (33) constitute the central results in our paper. It is important to note that, for initial mixed quantum and mixed detector states, a generalized complementarity relation holds, where the particle and wave natures are quantified via path distinguishability based on UQSD and the quantum coherence, respectively.

# IV. CONCLUSIONS

In this paper, we have introduced a generalized duality relation for arbitrary dimensional multislit quantum interference experiments. To delineate the wave nature of the quanton, which passes through the interferometer, we define normalized quantum coherence based on the recently introduced quantifier of quantum coherence in the framework of quantum information theory [19]. Since, both the interference and quantum coherence rely on quantum superposition of the quantum states, we claim that the proposed measure of (normalized) quantum coherence can be a quantifier of the wave nature of the quanton, instead of a traditional quantifier based on the interference fringe visibility. The

particle nature of a quanton is associated with the which-path information acquired through the detection process, i.e., which-path detection. In this work, we quantify the which-path information or path distinguishability by identifying it with the upper bound of success probability in unambiguous quantum state discrimination [20-22,26] of the detector states, after the path detectors are placed and the measurement interaction is turned on. Based on the normalized quantum coherence and the path distinguishability as the quantifiers the wave and particle natures of a quanton, respectively, we derive a duality relation, which is a quantitative statement of Bohr's principle of complementarity. For two-path and three-path interference we have related quantum coherence to the fringe visibility and recovered the corresponding known duality relations. Furthermore, we show that, in cases where decoherence may

introduce some mixedness in the density matrix of the quanton as well as in the detector, the duality relation continues to hold. We hope that our results will have fundamental implications in understanding the quantum complementarity, in particular, the wave nature of a quantum system in terms of quantum coherence.

# ACKNOWLEDGMENTS

The authors thank A. K. Rajagopal for many fruitful discussions. M.N.B. gratefully acknowledges the support provided by the Centre for Theoretical Physics, Jamia Millia Islamia, New Delhi, during his visit, where this work was initiated. M.A.S. thanks the University Grants Commission, India for financial support.

[1] N. Bohr, Nature (London) 121, 580 (1928).  
[2] T. Qureshi and R. Vathsan, Quanta 2, 58 (2013).  
[3] W. K. Wootters and W. H. Zurek, Phys. Rev. D 19, 473 (1979).  
[4] D. M. Greenberger and A. Yasin, Phys. Lett. A 128, 391 (1988).  
[5] B.-G. Englert, Phys. Rev. Lett. 77, 2154 (1996).  
[6] S. Durr, T. Nonn, and G. Rempe, Phys. Rev. Lett. 81, 5705 (1998).  
[7] X. Peng, X. Zhu, X. Fang, M. Feng, M. Liu, and K. Gao, J. Phys. A: Math. Gen. 36, 2555 (2003).  
[8] X. Peng, X. Zhu, D. Suter, J. Du, M. Liu, and K. Gao, Phys. Rev. A 72, 052109 (2005).  
[9] P. D. D. Schwindt, P. G. Kwiat, and B.-G. Englert, Phys. Rev. A 60, 4285 (1999).  
[10] V. Jacques, E. Wu, F. Grosshans, F. Treussart, P. Grangier, A. Aspect, and J.-F. Roch, Phys. Rev. Lett. 100, 220402 (2008).  
[11] L. Li, N.-L. Liu, and S. X. Yu, Phys. Rev. A 85, 054101 (2012).  
[12] A. Peruzzo, P. Shadbolt, N. Brunner, S. Popescu, and J. L. O'Brien, Science 338, 634 (2012).  
[13] M. Jakob and J. A. Bergou, Optics Communications 283, 827 (2010); F. Kaiser, T. Coudreau, P. Milman, D. B. Ostrowsky, and S. Tanzilli, Science 338, 637 (2012); K. Banaszek, P. Horodecki, M. Karpinski, and C. Radzewicz, Nat. Comm. 4, 2594 (2013); J. Prabhu Tej, A. R. Usha Devi, H. S. Karthik, Sudha, and A. K. Rajagopal, Phys. Rev. A 89, 062116 (2014).  
[14] G. Jaeger, A. Shimony, and L. Vaidman, Phys. Rev. A 51, 54 (1995).  
[15] S. Durr, Phys. Rev. A 64, 042113 (2001).  
[16] G. Bimonte and R. Musto, Phys. Rev. A 67, 066101 (2003).  
[17] B.-G. Englert, Int. J. Quantum. Inform. 6, 129 (2008).  
[18] P. J. Coles, J. Kaniewski, and S. Wehner, Nat. Comm. 5, 5814 (2014).  
[19] T. Baumgratz, M. Cramer, and M. B. Plenio, Phys. Rev. Lett. 113, 140401 (2014).  
[20] C. W. Helstrom, Quantum Detection and Estimation Theory (Academic Press, New York, 1976); C. A. Fuchs, Ph.D. thesis,

University of New Mexico, 1996 (unpublished); arXiv:quant-ph/9601020; A. Chefles, Contemp. Phys. 41, 401 (2000).  
[21] J. A. Bergou, J. Phys.: Conf. Ser. 84, 012001 (2007); G. Waldherr, A. C. Dada, P. Neumann, F. Jelezko, E. Andersson, and J. Wrachtrup, Phys. Rev. Lett. 109, 180501 (2012); M. Agnew, E. Bolduc, K. J. Resch, S. Franke-Arnold, and J. Leach, ibid. 113, 020501 (2014); J. Bae and L.-C. Kwek, J. Phys. A: Math. Theor. 48, 083001 (2015).  
[22] L.-M. Duan and G.-C. Guo, Phys. Rev. Lett. 80, 4999 (1998); A. Chefles, Phys. Rev. A 64, 062305 (2001); 69, 050307(R) (2004); A. K. Pati, P. Parashar, and P. Agrawal, ibid. 72, 012329 (2005).  
[23] D. Girolami, Phys. Rev. Lett. 113, 170401 (2014).  
[24] I. D. Ivanovic, Phys. Lett. A 123, 257 (1987); D. Dieks, ibid. 126, 303 (1988); A. Peres, ibid. 128, 19 (1988).  
[25] T. Rudolph, R. W. Spekkens, and P. S. Turner, Phys. Rev. A 68, 010301(R) (2003); P. Raynal, N. Lütkenhaus, and S. J. van Enk, ibid. 68, 022308 (2003); Y. C. Eldar, M. Stojnic, and B. Hassibi, ibid. 69, 062318 (2004); U. Herzog and J. A. Bergou, ibid. 71, 050301(R) (2005); Ph. Raynal and N. Lütkenhaus, ibid. 72, 022342 (2005); U. Herzog, ibid. 75, 052309 (2007).  
[26] S. Zhang, Y. Feng, X. Sun, and M. Ying, Phys. Rev. A 64, 062103 (2001); D. Qiu, Phys. Lett. A 303, 140 (2002).  
[27] J. von Neumann, Mathematical Foundations of Quantum Mechanics (Princeton University Press, Princeton, 1955).  
[28] G. Jaeger and A. Shimony, Phys. Lett. A 197, 83 (1995).  
[29] J. A. Bergou, U. Herzog, and M. Hillary, Lect. Notes Phys. 649, 417 (2004).  
[30] M. A. Siddiqui and T. Qureshi, arXiv:1405.5721.  
[31] M. Arndt, O. Nairz, J. Vos-Andreae, C. Keller, G. van der Zouw, and A. Zeilinger, Nature (London) 401, 680 (1999).  
[32] B. Brezger, L. Hackermüller, S. Utenthaler, J. Petschinka, M. Arndt, and A. Zeilinger, Phys. Rev. Lett. 88, 100404 (2002).  
[33] R. A. Horn and C. R. Johnson, Matrix Analysis (Cambridge University Press, Cambridge, 1985), p. 398.