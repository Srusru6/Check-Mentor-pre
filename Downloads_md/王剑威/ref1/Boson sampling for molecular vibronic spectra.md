# Boson sampling for molecular vibronic spectra

Joonsuk Huh*, Gian Giacomo Guerreschi, Borja Peropadre, Jarrod R. McClean and Alán Aspuru-Guzik*

Controllable quantum devices open novel directions to both quantum computation and quantum simulation. Recently, a problem known as boson sampling has been shown to provide a pathway for solving a computationally intractable problem without the need for a full quantum computer, instead using a linear optics quantum set-up. In this work, we propose a modification of boson sampling for the purpose of quantum simulation. In particular, we show that, by means of squeezed states of light coupled to a boson sampling optical network, one can generate molecular vibronic spectra, a problem for which no efficient classical algorithm is currently known. We provide a general framework for carrying out these simulations via unitary quantum optical transformations and supply specific molecular examples for future experimental realization.

Quantum mechanics allows the storage and manipulation of information in ways that are not possible according to classical physics. At a glance, it appears evident that the set of operations characterizing a quantum computer is strictly larger than the operations possible in a classical hardware. This speculation is at the basis of quantum speedups that have been achieved for oracular and search problems<sup>1,2</sup>. Particularly significant is the exponential speedup achieved for the prime factorization of large numbers<sup>3</sup>, a problem for which no efficient classical algorithm is currently known. Another attractive area for quantum computers is quantum simulation<sup>4-9</sup>, in which it has been shown recently that the dynamics of chemical reactions<sup>10</sup> as well as the molecular electronic structure<sup>11</sup> are attractive applications for quantum devices. For all these instances, the realization of a quantum computer would challenge the extended Church-Turing thesis (ECT), which claims that a Turing machine can efficiently simulate any physically realizable system, and even disprove it if prime factorization was finally demonstrated to be not efficiently solvable on classical machines.

At the same time, the realization of a full-scale quantum computer is a very demanding technological challenge, even if it is not forbidden by fundamental physics. This fact motivated the search for intermediate quantum hardware that could efficiently solve specific computational problems believed to be intractable with classical machines, without being capable of universal quantum computation. Recently, Aaronson and Arkhipov found that sampling the distribution of photons at the output of a linear photonic network is expected (modulo a few conjectures) to be computationally inefficient for any classical computer, because it requires the evaluation of many matrix permanents<sup>12</sup>. On the contrary, this task is naturally simulated by indistinguishable photons injected as the input of a photonic network (see the pictorial description of boson sampling in Fig. 1a). Although several groups have already realized small-scale versions of boson sampling<sup>13-16</sup>, to challenge the ECT one also has to demonstrate the scalability of the experimental architecture<sup>17,18</sup>.

Although boson sampling will probably play a major role in the debate around the ECT, it also appears as a somewhat artificial problem in which we ask a classical computer to predict the behaviour of a quantum machine (under certain working conditions) and then compare its efficiency with the direct operation of the

machine itself. In this work, we present a connection between boson sampling and the calculation of molecular vibronic (vibrational and electronic) spectra related to molecular processes such as absorption, emission, photoelectron and resonance Raman spectroscopy (see Table 1)[19-24]. These molecular spectroscopies are fundamental probes for molecular properties; for example, the corresponding vibronic transitions involve two electronic states and one can extract the molecular structural and force-field changes from the spectra. In particular, the linear absorption spectra of molecules determine important properties, such as their performance as solar cells[25] or as dyes, for either biological labels or industrial processes[26]. The prediction of the linear absorption of molecules is computationally challenging, especially when complicated vibrational features (see, for example, Dierksen and Grimm[27] and Hayes et al.[28]) make the spectra very rich. Moreover, photoelectron spectroscopy is a useful tool to study the ionized states of molecules. The ionizing process is important in chemistry and biology; for example, the photodamage of deoxyribonucleic acid molecules is fatal to life. We show a photoelectron spectrum of thymine[29] (the experimental spectrum is also given later in Fig. 4) as an example of the current state of the art.

We propose a new simulation scheme that provides a second, chemically relevant reason to realize boson sampling machines. It replaces the direct calculation of Franck-Condon (FC) factors, including Duschinsky mode mixing $^{30}$ , that represent a computationally difficult problem for which various strategies have been developed in the vibronic spectroscopy community (see, for example, Ruhoff et al. $^{22}$ , Jankowiak et al. $^{23}$  and Santoro et al. $^{24}$ ) with a simple sampling procedure from a quantum photonic device. In particular, we show that the quantum simulation, and hence the calculation of Franck-Condon profiles (FCPs) that lie at the heart of linear spectroscopy, can be efficiently performed on a boson sampling machine simply by modifying the input state. This connection provides a scientific and industrially relevant problem with a physical and chemical meaning that is well separated from the simulation of linear quantum optical networks. A complementary approach for the quantum simulation of molecular vibrations in quantum optics using a time-domain approach was introduced recently (A. Laing, personal communication).

![](images/a49c0983987ae818341010358b1c116bb22ca69aa5a60af8bdfe3ec65f7dcacb.jpg)  
Figure 1 | Pictorial description of boson sampling and molecular vibronic spectroscopy. a, Boson sampling consists of sampling the output distribution of photons obtained from quantum interference inside a linear quantum optical network. b, Vibronic spectroscopy uses coherent light to excite electronically an ensemble of identical molecules and measures the re-emitted (or scattered) radiation to infer the vibrational spectrum of the molecule. We show in this work how the fundamental physical process that underlies b is formally equivalent to situation a, together with a step to prepare a nonlinear step.

![](images/dbe38db4839168fe9a009b5a6e209266f7aea14e4f868d64c542f1881faa4f02.jpg)

# Results

Boson sampling and vibronic transitions. Boson sampling considers the input of  $N$  photons into  $M$  optical modes. This quantum space can be described through a Fock basis that counts the number of photons distributed in each mode. We denote such states by  $|n_1, n_2, \dots, n_M\rangle = |\mathbf{n}\rangle$ , where  $n_j$  corresponds to the number of photons in the  $j$ th mode and we have the constraint  $\sum_{j} n_j = N$ . These photons are sent through an optical network whose action is characterized by the unitary operation  $\hat{U}$ . Any input state  $|\phi_{\mathrm{in}}\rangle$  is related to the corresponding output state  $|\phi_{\mathrm{out}}\rangle$

through the relation:

$$
\left| \phi_ {\text {o u t}} \right\rangle = \hat {U} \left| \phi_ {\text {i n}} \right\rangle \tag {1}
$$

Considering linear quantum optical set-ups poses a restriction on the transformation  $\hat{U}$  that is constrained to represent a multimode rotation. We denote such a rotation as  $\hat{R}_U$  because its action is characterized by the  $M\times M$  unitary matrix  $U$  via the expression:

$$
\hat {\mathbf {a}} ^ {\prime \dagger} = \hat {R} _ {U} ^ {\dagger} \hat {\mathbf {a}} ^ {\dagger} \hat {R} _ {U} = U \hat {\mathbf {a}} ^ {\dagger} \tag {2}
$$

For notational simplicity, we introduce the column vectors of boson-creation operators  $\hat{\mathbf{a}}^{\dagger} = (\hat{a}_{1}^{\dagger},\dots,\hat{a}_{M}^{\dagger})^{t}$  and transformed boson-creation operators  $\hat{\mathbf{a}}^{\prime \dagger} = (\hat{a}_{1}^{\prime \dagger},\dots,\hat{a}_{M}^{\prime \dagger})^{t}$ , and adopt a shorthand notation<sup>31</sup> for the operator action on  $\hat{\mathbf{a}}^{\dagger}$ , that is  $\hat{A}\hat{\mathbf{a}}^{\dagger}\hat{B} = (\hat{A}\hat{a}_{1}^{\dagger}\hat{B},\dots,\hat{A}\hat{a}_{M}^{\dagger}\hat{B})^{t}$ .

Given this set-up, the problem is to compute both the transition probability between input and output states in the Fock basis expressed by the quantity:

$$
P _ {\mathbf {n m}} = \left| \langle \mathbf {m} | \hat {R} _ {U} | \mathbf {n} \rangle \right| ^ {2} \tag {3}
$$

where  $|\mathbf{n}\rangle$  is the input state and  $|\mathbf{m}\rangle$  the desired state in output, and, perhaps more importantly, which output states  $|\mathbf{m}\rangle$  will significantly contribute to the total distribution. As the total number of photons and the number of modes increase, the probability distribution of output states becomes hard to predict and sample from with classical computers, but it can be measured directly with linear optics devices. In particular, each transition probability,  $P_{\mathrm{nm}}$ , is proportional to the permanent of a different submatrix of  $U$  (refs 12,32).

We observe two facts: first, that the calculation of matrix permanents is a computationally hard problem for many classes of matrices belonging to the complexity class  $\# P$  (ref. 12) and, second, that the space of  $N$  photons in  $M$  optical modes is isomorphic to the space of  $N$  molecular vibrational quanta (phonons) in  $M$  vibrational modes. The latter connection suggests that the dynamics of vibrational modes is computationally difficult, at least in some instances. Moreover, as we will show, the computation of spectra requires sampling from a distribution of an

Table1 | A comparison of boson sampling and the computation of vibronic transitions.  

<table><tr><td></td><td>Boson sampling</td><td>Vibronic transitions</td></tr><tr><td>Harmonic oscillators</td><td>q1(ω) q2(ω) q1(ω) q2(ω)</td><td>q1(ω1) q2(ω2) q2(ω2) q1(ω1)</td></tr><tr><td>Linear transform</td><td>ˆt′ = Uˆt</td><td>ˆt′ = 1/2 (J - (J′)−1)ˆt + 1/2 (J + (J′)−1)ˆt + 1/√2 δ</td></tr><tr><td>Unitary operators</td><td>Rotation</td><td>Displacement, squeezing and rotation</td></tr><tr><td>Particle to simulate</td><td>Photon</td><td>Phonon</td></tr><tr><td>Particle in simulator</td><td>Photon</td><td>Photon</td></tr><tr><td>Outcome of simulation</td><td>|Permanent|2</td><td>FCP (spectrum)</td></tr></table>

The QHOs in the first row show the corresponding two-dimensional normal coordinates  $(q_{k}$  and  $q_{k}^{\prime}$  for input and output states, respectively) and their respective harmonic frequencies  $(\omega_{k}^{\prime}$  and  $\omega_{k}^{\prime})$  . The two sets of QHOs in boson sampling are rotated with respect to each other such that the linear relation with the rotation matrix  $U$  of the boson-creation operators are given in the second row. The two sets of QHOs in vibronic transitions are displaced, distorted (frequency changes) and rotated with respect to each other. d is a displacement vector of the QHOs. The boson-creation operator  $(\hat{a}^{\dagger})$  of the output state is now given as a linear combination of the boson-annihilation (a) and -creation  $(\hat{a}^{\dagger})$  operators of the input state with the dimensionless displacement vector 8. A matrix J characterizes the rotation and squeezing operations during a vibronic transition. This scenario applies only when  $U$  is a real matrix.

![](images/604f68aaba917db0ea66c0e8b1b341244354317371a0da36bbbda579a9dfbbc5.jpg)  
Figure 2 | Boson sampling apparatus for vibronic spectra. a, The boson sampling apparatus modified according to a direct implementation of equation (9). b, The boson sampling apparatus modified according to equation (11). Here the difference with the usual set-ups for the typical boson sampling problem is confined to the preparation process of the input state. For simplification,  $\hat{D} = \hat{D}_{J^{-1}\delta / \sqrt{2}}$ . Green and red boxes after the first unitary operations represent the prepared initial states, which are identified as squeezed vacuum and squeezed coherent states, respectively. The wavy yellow lines that enter the interferometer represent the preoperative initial states, which are vacuum states in this figure. They could be non-vacuum states for the proposed extension of the theory.

![](images/1823b86366b58cf3404c87ea8f0268fe5e972f926a047610e5ae123f7b2477c4.jpg)

extremely large number of permanents, identical to the problem of boson sampling. Thus, even in instances where the individual permanents may be easy to approximate, the overall sampling problem may not be tractable<sup>12</sup>. However, unlike boson sampling, a simple rotation of the modes is not sufficient to reproduce vibronic spectra (see the first row of Table 1) and additional effects need to be taken into account. We now detail these important additional effects.

An electronic transition of a molecule induces nuclear structural and force changes at the new electronic state. This defines a new set of vibrational modes that are displaced, distorted (hence showing a frequency change) and rotated with respect to the vibrational modes of the ground electronic state (see Table 1, first row and second column). Within the harmonic approximation of the electronic energy surfaces and the assumption of a coordinate-independent electronic transition moment (the Condon approximation), the vibronic transition profiles can be obtained by the overlap integral of the two  $M$ -dimensional quantum harmonic oscillator (QHO) eigenstates (FC integral), where  $M = 3M_{\mathrm{atom}} - 6(5)$  for nonlinear (linear) molecules with  $M_{\mathrm{atom}}$  atoms.

To describe these effects and compute vibronic profiles, Duschinsky $^{30}$  proposed a linear relation between the initial (mass-weighted) normal coordinates  $(\mathbf{q})$  and the final coordinates  $(\mathbf{q}^{\prime})$ , which reads:

$$
\mathbf {q} ^ {\prime} = U \mathbf {q} + \mathbf {d} \tag {4}
$$

where  $U$  is the Duschinsky rotation (real) matrix $^{23,33}$  and  $\mathbf{d}$  is the displacement (real) vector responsible for the molecular structural changes along the normal coordinates (see the first row of Table 1 for a comparison between the Duschinsky relation and the boson sampling problem). Observe that all the matrices and vectors associated with the electronic excitation of a molecule are real matrices and real vectors, a fact used to simplify all the expressions reported below. The two sets of QHOs are related by the Duschinsky relation,

which can be expressed in terms of a modification of the ladder operators $^{21}$  as given by:

$$
\hat {\mathbf {a}} ^ {\prime \dagger} = \frac {1}{2} (J - (J ^ {t}) ^ {- 1}) \hat {\mathbf {a}} + \frac {1}{2} (J + (J ^ {t}) ^ {- 1}) \hat {\mathbf {a}} ^ {\dagger} + \frac {1}{\sqrt {2}} \boldsymbol {\delta} \tag {5}
$$

with  $J$  and  $\delta$  defined as:

$$
J = \Omega^ {\prime} U \Omega^ {- 1}, \boldsymbol {\delta} = \hbar^ {(- 1 / 2)} \Omega^ {\prime} \mathbf {d} \tag {6}
$$

$$
\Omega^ {\prime} = \operatorname {d i a g} \left(\sqrt {\omega_ {1} ^ {\prime}}, \dots , \sqrt {\omega_ {N} ^ {\prime}}\right), \Omega = \operatorname {d i a g} \left(\sqrt {\omega_ {1}}, \dots , \sqrt {\omega_ {N}}\right)
$$

The notation 'diag' denotes a diagonal matrix, and  $\{\omega_k^{\prime}\}$  and  $\{\omega_l\}$  are the harmonic angular frequencies of the final and initial states. The major differences of equation (5) from the boson sampling problem  $(\hat{\mathbf{a}}^{\prime \dagger} = U\hat{\mathbf{a}}^{\dagger})$  are the appearance of the annihilation operators  $\hat{\mathbf{a}}$  and the displacement vector  $\delta$ . The annihilation operators appear in equation (5) to account for the distinct frequencies of the QHOs. Doktorov et al.20 analysed the linear transformation in equation (5) with a set of unitary operators. The linear transform in equation (5) can be written as  $\hat{\mathbf{a}}^{\prime \dagger} = \hat{U}_{\mathrm{Dok}}^{\dagger}\hat{\mathbf{a}}^{\dagger}\hat{U}_{\mathrm{Dok}}$  where the Doktorov transformation  $\hat{U}_{\mathrm{Dok}}$  is:

$$
\hat {U} _ {\mathrm {D o k}} = \hat {D} _ {\delta / \sqrt {2}} \hat {S} _ {\Omega^ {\prime}} ^ {\dagger} \hat {R} _ {U} \hat {S} _ {\Omega} \tag {7}
$$

With our conventions, any initial vibronic state  $|\phi_{\mathrm{in}}\rangle$  is transformed into  $|\phi_{\mathrm{out}}\rangle = \hat{U}_{\mathrm{Dok}}|\phi_{\mathrm{in}}\rangle$ . The Doktorov transformation is composed, in order of application, of (single mode) squeezing  $\hat{S}_{\Omega}$ , rotation  $\hat{R}_U$ , squeezing  $\hat{S}_{\Omega'}^\dagger$  and coherent state displacement  $\hat{D}_{\delta/\sqrt{2}}$  operators. The specific form of the unitary operators is given in Ma and Phodes<sup>31</sup> and also in Methods. Unlike the usual boson sampling case, the total number of phonons is not conserved in the scattering process.

The transition probability  $(|\langle \mathbf{m}|\hat{U}_{\mathrm{Dok}}|\mathbf{n}\rangle |^2)$  is called the FC factor, and through sampling many FC factors one obtains at each given vibrational transition frequency  $(\omega_{\mathrm{vib}})$  the FCP. Explicitly, the FCP at  $0\mathrm{K}$  is obtained with the initial vacuum state  $|\mathbf{0}\rangle$  as:

$$
\operatorname {F C P} \left(\omega_ {\mathrm {v i b}}\right) = \sum_ {\mathbf {m}} ^ {\infty} \left| \langle \mathbf {m} | \hat {U} _ {\mathrm {D o k}} | \mathbf {0} \rangle \right| ^ {2} \delta \left(\omega_ {\mathrm {v i b}} - \sum_ {k} ^ {N} \omega_ {k} ^ {\prime} m _ {k}\right) \tag {8}
$$

the best-known classical algorithm to compute FCP scales combinatorially in the size of the system. We provide a more thorough discussion of the complexity aspects in Methods.

We summarize the comparison between the boson sampling and the vibronic transition in Table 1 and proceed to show how to simulate the molecular vibronic spectra by sampling photons from a modified boson sampling device.

Boson sampling for FC factors. If all the phonon frequencies are identical and there is no displacement, the Duschinsky relation (equation (5)) can be directly reduced to the original boson sampling problem (equation (2)) when it applies to input Fock states of the form discussed in the original boson sampling $^{12}$ . For these molecules, a specific initial Fock state would correspond to the vibronic spectra of molecules in a well-defined initial vibrational state. Therefore, the Duschinsky relation can be considered as a generalized boson sampling problem (see Lund et al. $^{34}$ ) that involves not only rotation, but also displacement and squeezing operations. In this section, we modify boson sampling to simulate the FCP in the Duschinksy relation. We assume that the initial state corresponds to the vibrational ground state (mathematically, a vacuum state), which means that the FCP is produced at  $0\mathrm{K}$ .

Our proposal can be extended to vibronic profiles at a finite temperature by preparing various initial states with a probability

that corresponds to their Boltzmann factor $^{33,35}$ . A detailed finite-temperature experimental proposal is outside the scope of this paper. We can interpret some of the additional operators in the Duschinsky relation as part of the state-preparation process of the input state for boson sampling. To this end, we move the position of the displacement operator in  $\hat{U}_{\mathrm{Dok}}$  (equation (7)) from the left end to the right end by rotating the corresponding displacement parameter vector, that is:

$$
\hat {U} _ {\mathrm {D o k}} = \hat {S} _ {\Omega^ {\prime}} ^ {\dagger} \hat {R} _ {U} \hat {S} _ {\Omega} \hat {D} _ {J ^ {- 1} \delta / \sqrt {2}} \tag {9}
$$

The FC optical apparatus can be set up according to  $\hat{U}_{\mathrm{Dok}}$  in equation (9). As shown in Fig. 2a, the photons are prepared as squeezed coherent states or squeezed vacuum states, which correspond to the displaced modes and non-displaced modes, respectively. Thus, the input state to the boson sampling optical network is  $|\psi\rangle = \hat{S}_{\Omega} \hat{D}_{J^{-1}\delta/\sqrt{2}} |\mathbf{0}\rangle = \hat{S}_{\Omega} \left| \frac{1}{\sqrt{2}} J^{-1}\delta \right\rangle$ . As depicted in Fig. 2a, the prepared initial state  $|\psi\rangle$  passes through the boson sampling photon scatterer  $\hat{R}_U$  and then the output photons undergo the second squeezing operation  $\hat{S}_{\Omega}^{\dagger}$ . Finally, photocounters detect the output Fock states. The resulting probability can be resolved in its transition frequency  $(\omega_{\mathrm{vib}} = \sum_k^N \omega_k' m_k)$  to yield the FCPs from the boson sampling statistics. Here,  $\omega_k'$  represents the phonon frequency and not the input photon frequency. We do not assign different frequencies to different modes for the corresponding phonon modes; however, that the phonon-mode frequencies are different is taken into account by parameters of the state-preparation process and of the optical network.

In practice, the second squeezing operation is difficult to realize in optical set-ups as one needs a nonlinear interaction in situations that may involve only a limited number of photons. For this reason, instead of performing such an operation directly, as described in Fig. 2a, we propose to compress the two squeezing operations into a single one. We can achieve this goal by means of the singular value decomposition of the matrix  $J$  in equation (6),

$$
J = C _ {\mathrm {L}} \Sigma C _ {R} ^ {t} \tag {10}
$$

where  $C_{\mathrm{L}}$  and  $C_{\mathrm{R}}$  are real unitary matrices and  $\Sigma$  is a diagonal matrix composed of square roots of the eigenvalues of  $J^t J$ . As a result, the Doktorov operator can be rewritten as:

$$
\hat {U} _ {\mathrm {D o k}} = \hat {R} _ {C _ {\mathrm {L}}} \hat {S} _ {\Sigma} ^ {\dagger} \hat {R} _ {C _ {\mathrm {R}}} ^ {\dagger} \hat {D} _ {\frac {1}{\sqrt {2}} J ^ {- 1} \delta} \tag {11}
$$

The computation of the  $\hat{U}_{\mathrm{Dok}}$  operator and the transformation require  $\mathcal{O}(M^3)$  operations which remain feasible even when  $M$  exceeds several thousand.

At this point, the Doktorov operator is composed of two rotations, one squeezing operator and one displacement operator. The input state  $|\phi \rangle$  to the boson sampling optical network is prepared by applying the displacement, rotation and squeezing operators sequentially, that is:

$$
\begin{array}{l} | \phi \rangle = \hat {S} _ {\Sigma} ^ {\dagger} \hat {R} _ {C _ {\mathrm {R}}} ^ {\dagger} \hat {D} _ {J ^ {- 1} \delta / \sqrt {2}} | \mathbf {0} \rangle \tag {12} \\ = \hat {S} _ {\Sigma} ^ {\dagger} | \frac {1}{\sqrt {2}} C _ {\mathbb {R}} ^ {t} J ^ {- 1} \boldsymbol {\delta} \rangle \\ \end{array}
$$

As one can see from direct inspection,  $|\phi \rangle$  is a squeezed coherent state. The only remaining task is to pass the prepared input state through the boson sampling optical network, which is characterized by the rotation matrix  $C_{\mathrm{L}}$  for  $\hat{R}_{C_{\mathrm{L}}}$ . This simplified optical apparatus is depicted in Fig. 2b. Now, the problem is identical to boson sampling with squeezed coherent states as input<sup>34,36,37</sup>. Boson sampling with inputs different from Fock states, for example with coherent states or squeezed vacuum states, have been proposed

![](images/68b0acb8c06a4c8aab1c937f3dbdfb8a9eef92ecae37a54330f7e9008398ffab.jpg)  
Figure 3 | FCP (black sticks) of formic acid  $(1^{1}\mathbf{A}^{\prime}\rightarrow 1^{2}\mathbf{A}^{\prime})$  for a symmetry block  $\mathbf{a}^{\prime}$ . The red curve is taken from the experimental spectrum in Leach et al.40

and analysed in the context of the study of computational complexity in Lund et al.34, Rahimi-Keshari et al.36 and Olson et al.37 The algorithm for computing FCPs from a boson sampling set-up and its scaling behaviour are described in Methods.

Examples. We present two examples of computation of FCPs for molecules. In particular, we propose to simulate the photoelectron spectra of formic acid  $(\mathrm{CH}_2\mathrm{O}_2)$  and thymine  $(\mathrm{C}_5\mathrm{H}_6\mathrm{N}_2\mathrm{O}_2)$ . The photoelectron spectroscopy involves the molecular electronic transition from a neutral state to a cationic state. The spectral profile can be obtained by computing the corresponding FC factors[23]. The molecular parameters for the calculations are reproduced from the Supplementary Material of Jankowiak et al.[23] The FCPs are calculated with the vibronic structure program hotFCHT[23,38,39]. Parameters for the corresponding boson sampling experimental set-up are given in the Supplementary Information.

Formic acid represents a small system for testing the quantum simulation with relatively small optical set-ups. The calculated FCPs for formic acid are presented in Fig. 3 as black sticks, with a bin size  $\Delta_{\mathrm{vib}} = 1\mathrm{cm}^{-1}$ . The red curve in Fig. 3 is taken from the experimental spectrum in Leach et al.40 and includes the effects of line broadening. A table for the probabilities with respect to the corresponding quantum numbers and the vibrational transition frequencies is given in the Supplementary Information for a direct verification with boson sampling experiments. Additionally, we simulated the results of what would be expected in a boson sampling simulation of formic acid, and present these in the Supplementary Information. This simulation is done by stochastically sampling the known probability distribution for the output modes and performing the analysis according to equation (8) and the algorithm in Methods. The results from this simulation indicate that relatively few samples are needed from the device to resolve the overall shape of the spectrum, which supports the experimental feasibility of the approach.

The important FC factors  $(\geq 0.01)$  in Fig. 3 require at most three photons per mode (see the Supplementary Information). Current photon counters are able to distinguish up to a few photon numbers  $(\leq 3)$  per mode<sup>41</sup>. The (single mode) squeezing parameters for formic acid are given as  $\ln (\Sigma)$  (ref. 31), that is:

$$
\ln (\Sigma) = \operatorname {d i a g} (0. 1 0, 0. 0 7, 0. 0 2, - 0. 0 6, - 0. 0 8, - 0. 1 1, - 0. 1 9) \tag {13}
$$

The squeezing parameters are between  $-0.2$  and  $0.1$ . These parameters are related to the frequency ratio between the initial and final frequencies. The experimental implementation of boson

![](images/b8b48e8795efc4ff3a39483c388aed15a1f549a6d503353dd14aee4fc41d6152.jpg)  
Figure 4 | FCP (black sticks) of thymine  $(1^{1}\mathsf{A}^{\prime}\rightarrow 1^{2}\mathsf{A}^{\prime \prime})$ . The red curve, whose FCP is shifted to be compared clearly, is taken from the experimental spectrum in Choi et al.[29]

sampling for vibronic spectra would rely on experimental squeezing-operation techniques. At present, multiple experimental proposals for arbitrary squeezing operations on coherent states have been proposed. For example, phase-intensive optical amplification $^{42}$ , ancillary squeezed vacuum $^{43}$  and a dynamic squeezing operation $^{44}$  are all potentially promising.

We present here an FCP of thymine as a more experimentally challenging example for vibronic boson sampling. The calculated FCP of thymine is given as black sticks in Fig. 4. The details can be found in Jankowiak et al.[23] and also in the Supplementary Information.

# Discussion

Boson sampling may be one of the first experimentally accessible systems that challenges the computational power of classical computers. However, to our knowledge there has not been any proposal on its use for simulation purposes. In this work, we develop a connection between molecular vibronic spectra and boson sampling that allows the calculation of FCPs with quantum optical networks.

First, such a connection suggests that computing the dynamics of vibrational systems must be a computationally difficult task for some systems. We show that a modification of the input state of a boson sampling device enables the computation of complex molecular spectra in a way that includes effects beyond simple vibrational dynamics. This allows one to generate the molecular vibronic spectrum by shining light in boson sampling optical networks rather than on real molecules, and opens new possibilities for studying molecules that are hard to isolate in a lab setting and too big to simulate on a classical computer.

It is worth addressing a few points regarding the complexity of the classical computation that we propose to substitute, especially in relation to analogous results demonstrated for the original boson sampling problem. On the one hand, the set-up that we consider includes additional operations, namely squeezing and displacement, with the consequence of enlarging the output distributions that it can generate. On the other hand, the hardness proof by Aaronson and Arkhipov<sup>12</sup> relies on a few conditions that concern the optical network. First, the matrix that describes such networks should be randomly distributed according to the Haar measure; second, the relation  $M = \mathcal{O}(N^2)$  is required for the original boson sampling problem to avoid boson collisions in the output modes. Although there is no reason to believe that the Duschinsky rotation matrix is randomly distributed according to the Haar measure, it has both positive and negative entries<sup>12,45</sup>, and the combinatorial scaling of all known classical methods for sampling the output of such matrices (approximate and exact) suggests they fall under the currently unknown necessary (as

opposed to sufficient) conditions for hardness of sampling. Moreover, in contrast to the original boson sampling, alternative implementations with squeezed coherent states preserve hardness as they present mean photon numbers different from unity $^{34,36,37}$ .

To motivate experimental realizations, we present two small molecules with a  $C_s$  point-group symmetry. Exploiting the molecular symmetry makes the classical computation of the FCP easier, but molecules often have no symmetry, especially in the case of large molecules. Testing small systems represents an important step that precedes the application of boson sampling to the molecular vibronic spectroscopy of large systems whose calculation with classical computers is expected to be hard. Our work can be extended in various directions, for example, the quantum simulation that we propose can be generalized to vibronic profiles at finite temperature[33,35] by exploiting thermal coherent states[36] or one can consider the modification of boson sampling experiments to include non-Condon[35] and anharmonic effects[46]. Finally, we envision that experimental molecular spectra may be used as a reference to provide partial certification of large quantum devices beyond classical simulation capabilities.

# Methods

Methods and any associated references are available in the online version of the paper.

Received 5 January 2015; accepted 17 July 2015; published online 24 August 2015

# References

1. Deutsch, D. & Jozsa, R. Rapid solution of problems by quantum computation. Proc. R. Soc. Lond. A 439, 553-558 (1992).  
2. Grover, L. K. Quantum mechanics helps in searching for a needle in a haystack. Phys. Rev. Lett. 79, 325-328 (1997).  
3. Shor, P. W. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM Rev. 41, 303-332 (1999).  
4. Georgescu, I. M., Ashhab, S. & Nori, F. Quantum simulation. Rev. Mod. Phys. 86, 153-185 (2014).  
5. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nature Phys. 8, 285-291 (2012).  
6. Bloch, I., Dalibard, J. & Nascimbène, S. Quantum simulations with ultracold quantum gases. Nature Phys. 8, 267-276 (2012).  
7. Blatt, R. & Roos, C. F. Quantum simulations with trapped ions. Nature Phys. 8, 277-284 (2012).  
8. Lloyd, S. Universal quantum simulators. Science 273, 1073-1077 (1996).  
9. Aspuru-Guzik, A., Dutoi, A. D., Love, P. J. & Head-Gordon, M. Simulated quantum computation of molecular energies. Science 309, 1704-1707 (2005).  
10. Kassal, I., Whitfield, J. D., Perdomo-Ortiz, A., Yung, M.-H. & Aspuru-Guzik, A. Simulating chemistry using quantum computers. Ann. Rev. Phys. Chem. 62, 185-207 (2011).  
11. Babbush, R., McClean, J., Wecker, D., Aspuru-Guzik, A. & Wiebe, N. Chemical basis of Trotter-Suzuki errors in quantum chemistry simulation. Phys. Rev. A 91, 022311 (2015).  
12. Aaronson, S. & Arkhipov, A. in Proceedings of the 43rd Annual ACM Symposium on Theory of Computing (eds Fortnow, L. & Vadhan, S.) 333-342 (ACM, 2011).  
13. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
14. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
15. Crespi, A. et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nature Photon. 7, 545-549 (2013).  
16. Tillmann, M. et al. Experimental boson sampling. Nature Photon. 7, 540-544 (2013).  
17. Shchesnovich, V. S. Conditions for an experimental boson-sampling computer to disprove the extended Church-Turing thesis. Preprint at http://arxiv.org/abs/1403.4459v6 (2014).  
18. Rohde, P. P., Motes, K. R., Knott, P. A. & Munro, W. J. Will boson-sampling ever disprove the extended Church-Turing thesis? Preprint at http://arxiv.org/abs/1401.2199v2 (2014).  
19. Sharp, T. E. & Rosenstock, H. M. Franck-Condon factors for polyatomic molecules. J. Chem. Phys. 41, 3453-3463 (1964).  
20. Doktorov, E. V., Malkin, I. A. & Man'ko, V. I. Dynamical symmetry of vibronic transitions in polyatomic molecules and the Franck-Condon principle. J. Mol. Spectrosc. 64, 302-326 (1977).

21. Malmqvist, P.-Å. & Forsberg, N. Franck-Condon factors for multidimensional harmonic oscillators. Chem. Phys. 228, 227-240 (1998).  
22. Ruhoff, P. T. & Ratner, M. A. Algorithm for computing Franck-Condon overlap integrals. Int. J. Quantum Chem. 77, 383-392 (2000).  
23. Jankowiak, H.-C., Stuber, J. L. & Berger, R. Vibronic transitions in large molecular systems: rigorous prescreening conditions for Franck-Condon factors. J. Chem. Phys. 127, 234101 (2007).  
24. Santoro, F., Lami, A., Improta, R. & Barone, V. Effective method to compute vibrationally resolved optical spectra of large molecules at finite temperature in the gas phase and in solution. J. Chem. Phys. 126, 184102 (2007).  
25. Hachmann, J. et al. The Harvard Clean Energy Project: large-scale computational screening and design of organic photovoltaics on the world community grid. J. Phys. Chem. Lett. 2, 2241-2251 (2011).  
26. Gross, M. et al. Improving the performance of doped  $\pi$ -conjugated polymers for use in organic light-emitting diodes. Nature 405, 661-665 (2000).  
27. Dierksen, M. & Grimme, S. The vibronic structure of electronic absorption spectra of large molecules: a time-dependent density functional study on the influence of 'exact' Hartree-Fock exchange. J. Phys. Chem. A 108, 10225-10237 (2004).  
28. Hayes, D., Wen, J., Panitchayangkoon, G., Blankenship, R. E. & Engel, G. S. Robustness of electronic coherence in the Fenna-Matthews-Ohson complex to vibronic and structural modifications. Faraday Discuss. 150, 459-469 (2011).  
29. Choi, K.-W., Lee, J.-H. & Kim, S. K. Ionization spectroscopy of DNA base: vacuum-ultraviolet mass-analyzed threshold ionization spectroscopy of jet-cooled thymine. J. Am. Chem. Soc. 127, 15674-15675 (2005).  
30. Duschinsky, F. The importance of the electron spectrum in multiatomic molecules. Concerning the Franck-Condon principle. Acta Physicochim. URSS 7, 551-566 (1937).  
31. Ma, X. & Phodes, W. Multimode squeeze operators and squeezed states. Phys. Rev. A 41, 4625-4631 (1990).  
32. Scheel, S. Permanents in linear optical networks. Preprint at http://arxiv.org/abs/quant-ph/0406127 (2004).  
33. Huh, J. Unified Description of Vibronic Transitions with Coherent States. PhD thesis, Goethe Univ. Frankfurt (2011).  
34. Lund, A. P. et al. Boson sampling from a Gaussian state. Phys. Rev. Lett. 113, 100502 (2014).  
35. Santoro, F., Lami, A., Improta, R., Bloino, J. & Barone, V. Effective method for the computation of optical spectra of large molecules at finite temperature including the Duschinsky and Herzberg-Teller effect: the  $Q_{x}$  band of porphyrin as a case study. J. Chem. Phys. 128, 224311 (2008).  
36. Rahimi-Keshari, S., Lund, A. P. & Ralph, T. C. What can quantum optics say about complexity theory? Preprint at http://arxiv.org/abs/1408.3712v1 (2014).  
37. Olson, J. P., Seshadreesan, K. P., Motes, K. R., Rohde, P. P. & Dowling, J. P. Sampling arbitrary photon-added or photon-subtracted squeezed states is in the same complexity class as boson sampling. Phys. Rev. A 91, 022317 (2015).  
38. Berger, R. & Klessinger, M. Algorithms for exact counting of energy levels of spectroscopic transitions at different temperatures. J. Comput. Chem. 18, 1312-1319 (1997).

39. Berger, R., Fischer, C. & Klessinger, M. Calculation of the vibronic fine structure in electronic spectra at higher temperatures. 1. Benzene and pyrazine. J. Phys. Chem. 102, 7157-7176 (1998).  
40. Leach, S. et al. He I photoelectron spectroscopy of four isotopologues of formic acid: HCOOH, HCOOD, DCOOH and DCOOD. Chem. Phys. 286, 15-43 (2003).  
41. Carolan, J. et al. On the experimental verification of quantum complexity in linear optics. Nature Photon. 8, 621-626 (2014).  
42. Josse, V., Sabuncu, M., Cerf, N., Leuchs, G. & Andersen, U. Universal optical amplification without nonlinearity. Phys. Rev. Lett. 96, 163602 (2006).  
43. Yoshikawa, J.-I. et al. Demonstration of deterministic and high fidelity squeezing of quantum information. Phys. Rev. A 76, 060301(R) (2007).  
44. Miwa, Y. et al. Exploring a new regime for processing optical qubits: squeezing and unsqueezing single photons. Phys. Rev. Lett. 113, 013601 (2014).  
45. Jerrum, M., Sinclair, A. & Vigoda, E. A polynomial-time approximation algorithm for the permanent of a matrix with nonnegative entries. J. ACM 51, 671-697 (2004).  
46. Huh, J., Neff, M., Rauhut, G. & Berger, R. Franck-Condon profiles in photodetachment-photoelectron spectra of  $\mathrm{HS}_2^-$  and  $\mathrm{DS}_2^-$  based on vibrational configuration interaction wavefunctions. Mol. Phys. 108, 409-423 (2010).

# Acknowledgements

We thank R. Berger for permission to use the vibronic structure program hotFCHT for our research. J.H. and A.A.-G. acknowledge a Defense Threat Reduction Agency grant HDTRA1-10-1-0046 and the Air Force Office of Scientific Research grant FA9550-12-1-0046. J.R.M. is supported by the Department of Energy Computational Science Graduate Fellowship under grant number DE-FG02-97ER25308. G.G.G. and A.A.-G. acknowledge support from Natural Sciences Foundation (NSF) Grant No. CHE-1152291. B.P. and A.A.-G. acknowledge support from the Science and Technology Center for Integrated Quantum Materials, NSF Grant No. DMR-1231319. Furthermore, A.A.-G. is grateful for support from the Defense Advanced Research Projects Agency grant N66001-10-1-4063, and the Corning Foundation for their generous support.

# Author contributions

J.H., G.G.G. and A.A.-G. conceived and designed the experiments. J.H. and G.G.G. performed the simulations. J.H., G.G.G., B.P. and J.R.M. contributed materials and/or analysis tools. J.H., G.G.G., B.P., J.R.M. and A.A.-G. worked on the theory, analysed the data and wrote the paper.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to J.H. and A.A.G.

# Competing financial interests

The authors declare no competing financial interests.

# Methods

Algorithm and scaling. Although no formal proof of the complexity of computing FCPs exists, we describe an observed computational effort for current algorithms and typical (molecular) problem instances. As the molecular system size and temperature increase, the evaluation of the FCP with classical computers becomes practically intractable (see Jankowiak et al.[23] and Santoro et al.[24]). The size and temperature effects make the resulting spectrum very congested because of the increase of the density of states. Already, the enumeration of the states that contribute to each point of the frequency grid  $(\omega_{\mathrm{vib}})$  is an issue for evaluating the FCP. That is, one needs to find all sets of  $\mathbf{m}$  that satisfy  $\omega_{\mathrm{vib}} = \sum_{k}^{N}\omega_{k}^{\prime}m_{k}$  at  $0\mathrm{K}$ . To address this issue requires an algorithm to count the vibrational states and determine its limitation with respect to the system size (see, for example, Berger and Klessinger[38]). The calculation of FC integrals  $(\langle \mathbf{m}|\hat{U}_{\mathrm{Dok}}|\mathbf{n}\rangle)$  (see the Supplementary Information for the detailed expression)) is equivalent to the evaluation of multivariate Hermite polynomials at the origin[33,47,48]. Indeed, Huh[33] showed that it can be evaluated by an algorithm developed for multivariate normal moments[49]. Kan[49] exploited a collective variable to calculate the moments of the distribution, and obtained an algorithm that requires

$$
\left(1 + \left[ \frac {1}{2} \left(\sum_ {k} \left(n _ {k} + m _ {k}\right)\right) \right]\right) \prod_ {k} \left(n _ {k} + 1\right) \left(m _ {k} + 1\right)
$$

terms, where  $[x]$  is a rounded integer of  $x$ . This number is much smaller than the number of terms from a brute-force evaluation of Wick's formula, which corresponds to  $(\sum_{k}(n_{k} + m_{k}) - 1)!!$  (ref. 49), where a similar analysis was done for the squeezed vacuum state input problem in boson sampling<sup>36</sup>. However, the computation with Kan's algorithm<sup>49</sup> is still likely to be a hard problem.

Here we describe explicitly the algorithm for computing FCPs given a boson sampling set-up and analyse the computational cost of resolving FCPs with this setup. As in the rest of the work we limit ourselves to the case of  $0\mathrm{K}$  with the generalization to finite temperature being the subject of future work.

The goal is to resolve the function  $\mathrm{FCP}(\omega_{\mathrm{vib}})$  in equation (8) to a fixed precision  $\epsilon_{\mathrm{FCP}}$  in the function value at a fixed resolution  $\Delta_{\mathrm{vib}}$  in the value of  $\omega_{\mathrm{vib}}$ . We also take as input values the number of vibrational modes  $M$ , final vibrational frequencies  $\{\omega_k^{\prime}\}$  and a maximum frequency of interest  $\omega_{\mathrm{max}}$ .

Consider the FCP on the interval  $[0, \bar{\omega}_{\mathrm{max}}]$  and discretize this interval uniformly at a resolution of  $\Delta_{\mathrm{vib}}$ . The algorithm proceeds as follows. Prepare the state  $|\phi\rangle$ , and pass it into the boson sampling set-up. Measure at the output modes the photon numbers  $\{m_k\}$  in each mode. Locate the discrete bin of the FCP that is non-zero and corresponds to the measurement values of  $\{m_k\}$ , and increment its value by one. Repeat the experiment until the estimated statistical error of the average values in each discrete bin of FCP is below the desired threshold  $\epsilon_{\mathrm{FCP}}$ . Denote the total number of samples taken as  $N_{\mathrm{Samp}}$ .

To assess the algorithm, we rewrite it as a stochastic sampling problem over a probability distribution given by the boson sampling device. We observe that  $P_{\mathbf{m}|\phi} = |\langle \mathbf{m}|\hat{U} |\phi \rangle |^2$  is a normalized probability distribution, and the one naturally sampled at unit cost by a boson sampling device. As such, an FCP at a given frequency is equivalent to the average value of  $f(\mathbf{m}) = \delta (\omega_{\mathrm{vib}} - \sum_k^M\omega_k^* m_k)$  over the probability distribution  $P$ , which we denote  $\langle f\rangle_P$ . By simply computing the average of  $N_{\mathrm{samp}}$  independent samples  $|\mathbf{s}_i\rangle$  taken from the device, that is:

$$
\operatorname {F C P} = \left\langle f \right\rangle_ {P} \approx \frac {1}{N _ {\text {S a m p}}} \sum_ {i = 1} ^ {N _ {\text {S a m p}}} f (\mathbf {s} _ {i}), \tag {14}
$$

one obtains an estimate of the FCP. By the central limit theorem, the number of samples required to reach a desired precision  $\epsilon_{\mathrm{FCP}}$  scales as  $\mathrm{var}(f) / \epsilon_{\mathrm{FCP}}^2$ . As the Kronecker delta function is constrained to have a value of either 0 or 1, the variance of  $f$  in this case can be bounded by 1, and the number of expected samples to converge FCP for a given frequency may be bounded by a constant dictated by the fixed precision  $\epsilon_{\mathrm{FCP}}$ . Also, this constant bound is an upper bound on the number of required samples, and some distributions and experiments will require far fewer samples. For example, distributions with a small number of peaks (at the resolution determined by  $\Delta_{\mathrm{vib}}$ ) may converge extremely rapidly.

Unitary transformations. The specific form of the unitary operators that appear in the Doktorov transformation as reported in equation (7) is given by [31]

$$
\hat {D} _ {\delta / \sqrt {2}} ^ {\dagger} \hat {\mathbf {a}} ^ {\dagger} \hat {D} _ {\delta / \sqrt {2}} = \hat {\mathbf {a}} ^ {\dagger} + \frac {1}{\sqrt {2}} \boldsymbol {\delta} \tag {15}
$$

$$
\hat {S} _ {\Omega^ {\prime}} \hat {\mathbf {a}} ^ {\dagger} \hat {S} _ {\Omega^ {\prime}} ^ {\dagger} = \frac {1}{2} \left(\Omega^ {\prime} + \Omega^ {\prime - 1}\right) \hat {\mathbf {a}} ^ {\dagger} + \frac {1}{2} \left(\Omega^ {\prime} - \Omega^ {\prime - 1}\right) \hat {\mathbf {a}} \tag {16}
$$

$$
\hat {S} _ {\Omega} ^ {\dagger} \hat {\mathbf {a}} ^ {\dagger} \hat {S} _ {\Omega} = \frac {1}{2} (\Omega + \Omega^ {- 1}) \hat {\mathbf {a}} ^ {\dagger} - \frac {1}{2} (\Omega - \Omega^ {- 1}) \hat {\mathbf {a}} \tag {17}
$$

# References

47. Huh, J. & Berger, R. Application of time-independent cumulant expansion to calculation of Franck-Condon profiles for large molecular systems. Faraday Discuss. 150, 363-373 (2011).  
48. Huh, J. & Berger, R. Coherent state-based generating function approach for Franck-Condon transitions and beyond. J. Phys. Conf. Ser. 380, 012019 (2012).  
49. Kan, R. From moments of sum to moments of product. J. Multivariate Anal. 99, 542-554 (2008).