# Entropic framework for wave-particle duality in multipath interferometers

Patrick J. Coles*

Institute for Quantum Computing and Department of Physics and Astronomy, University of Waterloo,

Waterloo, Ontario N2L3G1, Canada

(Received 12 January 2016; published 9 June 2016)

An interferometer—no matter how clever the design—cannot reveal both the wave and the particle behavior of a quantum system. This fundamental idea has been captured by inequalities, so-called wave-particle duality relations (WPDRs), that upper bound the sum of the fringe visibility (wave behavior) and path distinguishability (particle behavior). Another fundamental idea is Heisenberg's uncertainty principle, stating that some pairs of observables cannot be known simultaneously. Recent work has unified these two principles for two-path interferometers. Here we extend this unification to  $n$ -path interferometers, showing that WPDRs correspond to a modern formulation of the uncertainty principle stated in terms of entropies. Furthermore, our unification provides a framework for solving an outstanding problem of how to formulate universally valid WPDRs for interferometers with more than two paths, and we employ this framework to derive some novel WPDRs.

DOI: 10.1103/PhysRevA.93.062111

# I. INTRODUCTION

Photons [1], electrons [2], neutrons [3], and even large organic molecules [4] have been shown experimentally to exhibit the behavior of both waves and particles. However, one cannot simultaneously see both behaviors; an apparatus that reveals the particle behavior cannot see the wave behavior, and vice versa. This fundamental principle of quantum mechanics is known as wave-particle duality (WPD) and is closely related to Bohr's complementarity principle [5,6].

Quantitative statements about WPD, so-called wave-particle duality relations (WPDRs), aim to upper bound the sum of the wave behavior and the particle behavior for a given interferometer. A well-known formulation given by Englert [7] and Jaeger, Shimony, and Vaidman [8] considered the two-path Mach-Zehnder interferometer (MZI) for single photons (see Fig. 1, which shows more generally the  $n$ -path MZI). They quantified wave and particle behavior, respectively, by the fringe visibility  $\mathcal{V}$  and path distinguishability  $\mathcal{D}$  (see below for definitions) and proved that

$$
\mathcal {V} ^ {2} + \mathcal {D} ^ {2} \leqslant 1. \tag {1}
$$

This relation says that full wave behavior  $(\mathcal{V} = 1)$  implies no particle behavior  $(\mathcal{D} = 0)$ , and vice versa, and also bounds the intermediate case of partial behavior. Many more complicated interferometry setups have been considered, leading to a vast number of WPDRs [9-23].

It has been debated [7,16,24-29] whether WPD is related to another fundamental principle: Heisenberg's uncertainty principle [30]. For example, the seminal paper Ref. [7] argued that the two principles are distinct. The uncertainty principle states that there exist pairs of observables, like position and momentum, that cannot be simultaneously known or jointly measured, and many quantitative statements of it have been formulated. Historically, these uncertainty relations employed the standard deviation as the uncertainty measure, but later they evolved into a more robust formulation in terms of entropies, i.e., entropic uncertainty relations (EURs). We

refer the reader to Ref. [31] for a review of EURs and their applications to information-processing tasks such as cryptography.

Interestingly, several recent works [16,28,29] demonstrated that the two principles are connected. References [28,29] connected (1) to the standard-deviation-based uncertainty relation, while Ref. [16] showed that (1) is actually an EUR. Hence, these works effectively unified two fundamental principles of quantum mechanics.

However, a skeptic could argue that two-path interferometers are very special, and perhaps the equivalence between the two principles does not extend to arbitrary interferometers. This motivates our current work, where we unify the two principles for general  $n$ -path interferometers. In particular, we extend the result from Ref. [16], which found that (1) is essentially the uncertainty relation for the min- and max-entropies, i.e., the relation used to prove the security of quantum key distribution [32].

Furthermore, we exploit our aforementioned unification to provide a general framework for WPD in  $n$ -path interferometers. Such a framework has been lacking in the literature. On one hand, Durr [20] proved a WDPR for the  $n$ -path MZI involving an operational measure of wave behavior, but at the cost of using a less operational measure of particle behavior. On the other hand, Refs. [21-23] recently proved WPDRs for this same scenario using operational measures of particle behavior, but at the cost of replacing visibility with coherence—a less operational measure of wave behavior. Here, we remedy this situation with measures of particle and wave behavior that are operational, experimentally friendly, and intuitive.

Our main conceptual results are as follows. We find a novel generalization of (1) that extends the trade-off between wave and particle behavior to  $n$ -path interferometers. Likewise, we extend other WPDRs from the literature to the  $n$ -path case, namely, one treating quantum erasure [10] and one treating asymmetric input and output beam splitters [13]. The key point is that we derive these novel WPDRs directly from the uncertainty relation for the min- and max-entropies, which we henceforth abbreviate MMEUR. We argue that our WPDRs and many others in the literature

![](images/380c47cd8d7e7889c880df4971eb515804c0fb889086110470a474f2542fdcb6.jpg)

![](images/5c24630710fa28a0f88ae3fde93566ed92355ca3f2c0616a91ee548cd888d19d.jpg)  
FIG. 1. (a)  $n$ -path interferometer for single photons. A source injects a photon into an optical fiber. The photon approaches a fiber coupler,  $\mathsf{FC}_1$ , which allows the photon to leak into the other  $n - 1$  fibers, creating a superposition of which-path states. Then the photon interacts with some environment  $E$ , which may obtain some information, e.g., about the photon's path. Then a phase shift is applied to each arm ( $\phi_z$  to the  $z$ th arm), and the arms are brought together again at a second fiber coupler,  $\mathsf{FC}_2$ . Finally, the photon is detected at some detector. (b) Guessing-game view of WPD. We think of "particles" as having a well-defined location, so the particle game asks the experimenter to guess (given access to a subsystem  $E_1$  of  $E$ ) which path the photon will take inside the interferometer. We think of "waves" as exhibiting interference—with the most extreme interference pattern corresponding to only one detector clicking all the time and no interference corresponding to a uniform distribution over all detectors. Hence the wave game asks the experimenter to guess (given access to a subsystem  $E_2$  of  $E$  and given the freedom to adjust the phases  $\{\phi_z\}$ ) which detector will click. WPDRs give quantitative trade-offs for the probabilities of winning these two games.

![](images/f5037ff963171d4cb8cbd4cd9d9f46a82213074a8d0ee191b0705e9303d29b5b.jpg)

are special cases of a single, generic WPDR [Eq. (10)] that is explicitly an EUR. In this sense we unify WPDRs with EURs.

The above conceptual insights come from some abstract, technical results that may be useful in other contexts. Namely, we find a new connection between the max-entropy and the guessing probability, which leads to a new uncertainty relation for the guessing probability. We first present these technical results and then move on to a discussion of wave-particle duality in Sec. III. Finally, we compare our approach to the literature in Sec. VII.

# II. ABSTRACT RESULTS

The min- and max-entropies for a classical-quantum state  $\rho_{XB} = \sum_x p_x|x\rangle \langle x|\otimes \rho_B^x$  are defined by [33]

$$
H _ {\min } (X \mid B) := - \log p _ {\text {g u e s s}} (X \mid B), \tag {2}
$$

$$
H _ {\max } (X \mid B) := \log p _ {\sec r} (X \mid B). \tag {3}
$$

Here,

$$
p _ {\text {g u e s s}} (X | B) := \max  _ {\{\mathbb {M} _ {x} \}} \sum_ {x} p _ {x} \operatorname {T r} \left(\mathbb {M} _ {x} \rho_ {B} ^ {x}\right) \tag {4}
$$

is the probability of guessing  $X$  correctly given the outcome of the optimal POVM (positive operator-valued measure) measurement  $\{\mathbb{M}_x\}$  on system  $B$ , and

$$
p _ {\text {s e c r}} (X \mid B) := \max  _ {\sigma_ {B}} \mathsf {F} \left(\rho_ {X B}, \mathbb {1} \otimes \sigma_ {B}\right) \tag {5}
$$

quantifies the secrecy of  $X$  from  $B$ , as measured by the fidelity  $\mathsf{F}$  of  $\rho_{XB}$  to an uncorrelated state, where the maximization in Eq. (5) is over all density operators on  $B$ . Here, the fidelity is  $\mathsf{F}(\rho ,\sigma)\coloneqq (\mathrm{Tr}\sqrt{\sqrt{\rho}}\sigma \sqrt{\rho})^2$ .

The min-entropy is employed in quantum key distribution to quantify how well the eavesdropper can guess the secret key. Interestingly we find that the max-entropy is also connected to the guessing probability, with  $d = |X|$ ,

$$
\begin{array}{l} H _ {\max } (X | B) \\ \leqslant \log \left(1 + \sqrt {(d - 1) ^ {2} - (d p _ {\text {g u e s s}} (X | B) - 1) ^ {2}}\right), \tag {6} \\ \end{array}
$$

where the proof is given in Appendix A.

For any tripartite state  $\rho_{AB_1B_2}$  and for two orthonormal bases,  $\mathbb{X} = \{|\mathbb{X}_x\rangle \langle \mathbb{X}_x|\}$  and  $\mathbb{Y} = \{|\mathbb{Y}_y\rangle \langle \mathbb{Y}_y|\}$  on  $\mathcal{H}_A$ , whose measurement gives rise to random variables  $X$  and  $Y$ , the MMEUR [34] states that

$$
H _ {\min } \left(X \mid B _ {1}\right) + H _ {\max } \left(Y \mid B _ {2}\right) \geqslant \log (1 / c), \tag {7}
$$

where  $c \coloneqq \max_{x,y} |\langle \mathbb{X}_x | \mathbb{Y}_y \rangle|^2$ . Inserting (2) and (6) into (7) gives a novel uncertainty relation for  $p_{\mathrm{guess}}$ ,

$$
\frac {p _ {\text {g u e s s}} \left(X \mid B _ {1}\right)}{c} - \sqrt {(d - 1) ^ {2} - (d p _ {\text {g u e s s}} \left(Y \mid B _ {2}\right) - 1) ^ {2}} \leqslant 1, \tag {8}
$$

with  $d = |X| = |Y| = \dim (\mathcal{H}_A)$ . In the extreme case of mutually unbiased bases (MUBs) we have  $c = 1 / d$ , and (8) simplifies to a symmetric-looking relation,

$$
\mathcal {D} \left(X \mid B _ {1}\right) ^ {2} + \mathcal {D} \left(Y \mid B _ {2}\right) ^ {2} \leqslant 1, \tag {9}
$$

where  $\mathcal{D}(X|B) \coloneqq (d p_{\mathrm{guess}}(X|B) - 1) / (d - 1)$  is a measure of distinguishability with a range between 0 and 1. This concludes our abstract results, and we now move on to discuss WPD.

# III. GENERIC WPDR

# A.  $n$ -path interferometer

Henceforth we consider an  $n$ -path interferometer. For example, Fig. 1 shows a source injecting a photon into a fiber optic, which then approaches a fiber coupler,  $\mathsf{FC}_1$ , creating a superposition of which-path states inside the interferometer. The photon then interacts with an environment  $E = E_{1}E_{2}$  which (for generality) we allow to be a bipartite system composed of subsystems  $E_{1}$  and  $E_{2}$ . Each path receives a phase shift  $\phi_z$ , with  $\vec{\phi} \coloneqq \{\phi_z\}$  denoting the set of all phases. Finally, the paths are recombined with a fiber coupler  $\mathsf{FC}_2$  and the photon is detected at a detector.

# B. Guessing-game view

We argue that the MMEUR provides a robust, operational framework for discussing WPD, particularly due to the above connection with the guessing probability. Indeed, one can think of WPD operationally as a statement that one cannot build an interferometer that allows one to win two complementary guessing games. Namely, as shown in Fig. 1(b), we consider a "particle game" and a "wave game." The particle game asks the experimenter to guess which path the photon takes inside the interferometer, and the experimenter is given access to subsystem  $E_{1}$  to help win the particle game. The wave game asks the experimenter to guess which detector will click at the interferometer output. To help win the wave game, the experimenter is given access to  $E_{2}$  and, furthermore, is allowed to vary the phases  $\vec{\phi}$ . WPDRs are essentially quantitative restrictions on one's ability to win both the particle and the wave guessing games.

To treat this general situation we state a generic WPDR. We quantify (lack of) particle and wave behavior by

lack of particle behavior:  $H_{\mathrm{min}}(Z|E_1)$

lack of wave behavior:  $\min_{\mathbb{W}\in \mathcal{M}_{\mathbb{Z}}}H_{\max}(W|E_2)$

where  $Z$  is the which-path random variable, which we associate with the standard basis  $\mathbb{Z} = \{|z\rangle \langle z|\}$  of an  $n$ -dimensional Hilbert space  $\mathcal{H}_S$ ,  $W$  is the random variable associated with basis  $\mathbb{W}$  of  $\mathcal{H}_S$ , and  $\mathcal{M}_{\mathbb{Z}}$  is the set of all orthonormal bases that are mutually unbiased to  $\mathbb{Z}$ . We formulate our generic WPDR as

$$
H _ {\min } (Z \mid E _ {1}) + \min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } (W \mid E _ {2}) \geqslant \log n, \tag {10}
$$

which states that, for an  $n$ -path interferometer for single quantons (i.e., quantum particles such as photons), the sum of the ignorances about the particle and wave behaviors is at least  $\log n$  bits of information. Of course, (10) is explicitly an EUR, a special case of (7). But by applying the above argument used to derive (9), Eq. (10) can be rearranged into the standard form for WPDRs, involving an upper bound on the sum of the squares of particle and wave terms. Furthermore, we now proceed to show that (10) encompasses several WPDRs in the literature and leads to novel WPDRs.

# IV. TWO PATHS

First, let us consider Eq. (1) for the two-path MZI, a special case of Fig. 1, where there is only a single relative phase  $\phi$  applied between the two arms of the interferometer, i.e.,  $\bar{\phi} = \{0,\phi\}$ . The path distinguishability quantifies how well one can guess which path the photon takes, given the outcome of the optimal measurement on the environment  $E$  (e.g.,  $E$  could be the photon's polarization), and is defined by

$$
\mathcal {D} = 2 p _ {\text {g u e s s}} (Z | E) - 1. \tag {11}
$$

The fringe visibility  $\mathcal{V}$  quantifies oscillations, as one varies the phase  $\phi$ , in the probability of detecting the photon at a given detector. Let  $C \in \{1,2\}$  denote the random variable referring to which detector clicks at the interferometer output. Then  $\mathcal{V}$

is defined by

$$
\mathcal {V} = \frac {p _ {C = 1} ^ {\max} - p _ {C = 1} ^ {\min}}{p _ {C = 1} ^ {\max} + p _ {C = 1} ^ {\min}}, \tag {12}
$$

where  $p_{C=1}^{\max} = \max_{\vec{\phi}}(p_{C=1})$ ,  $p_{C=1}^{\min} = \min_{\vec{\phi}}(p_{C=1})$ , and  $p_{C=1}$  is the probability that  $C = 1$ , i.e., that detector  $D_1$  clicks. Reference [16] showed that  $\mathcal{D}$  and  $\mathcal{V}$  are, respectively, connected to the min- and max-entropies as follows:

$$
H _ {\min } (Z \mid E) = - \log \frac {1 + \mathcal {D}}{2}, \tag {13}
$$

$$
\min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } (W) = \log \left(1 + \sqrt {1 - \mathcal {V} ^ {2}}\right). \tag {14}
$$

One can plug these identities into the EUR,

$$
H _ {\min } (Z | E) + \min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } (W) \geqslant 1, \tag {15}
$$

to show that (1) is equivalent to (15). Note that (15) is a special case of (10), corresponding to  $E_1 = E$ ,  $n = 2$ , and  $E_2$  being a trivial system.

# V. OUR WPDR FOR  $n$  PATHS

To extend the above connection to the  $n$ -path MZI, we must address the question of how to generalize  $\mathcal{D}$  and  $\mathcal{V}$ . The seminal paper by Jaeger et al. [8] proposed that the appropriate generalization of  $\mathcal{D}$  to  $n$  paths is

$$
\mathcal {D} = \frac {n p _ {\text {g u e s s}} (Z | E) - 1}{n - 1}, \tag {16}
$$

which reduces to (11) for  $n = 2$ .

The more difficult task is to generalize  $\mathcal{V}$ . Naively, one might just try to directly use the formula in Eq. (12), in which case we denote the quantity  $\widetilde{\mathcal{V}}$ . However, this approach fails. As the following example illustrates,  $\widetilde{\mathcal{V}}$  does not satisfy a strong trade-off with  $\mathcal{D}$ , for large  $n$ .

Example 1. Consider the  $n$ -path MZI in Fig. 1. Suppose  $\mathsf{FC}_2$  induces the unitary transformation  $F^{\dagger}$ , where  $F = \sum_{z,z'}(\omega^{-zz'} / \sqrt{n})|z\rangle \langle z'|$  is the Fourier matrix with  $\omega = e^{2\pi i / n}$ . Suppose the photon's state inside the interferometer is

$$
\begin{array}{l} | \psi \rangle = \sum_ {x \neq n} \frac {1}{\sqrt {n - 1}} | \mathbb {X} _ {x} \rangle (17) \\ = \sqrt {\frac {n - 1}{n}} \left(| n \rangle - \frac {1}{n - 1} \sum_ {z \neq n} | z \rangle\right), (18) \\ \end{array}
$$

where  $|\mathbb{X}_x\rangle = F|x\rangle$ . From (18), one can see that  $p_{\mathrm{guess}}(Z) = (n - 1) / n$  and hence  $\mathcal{D} = (n - 2) / (n - 1)$ . So  $\mathcal{D}\rightarrow 1$  in the limit of large  $n$ . Also,  $\widetilde{\nu} = 1$ , since  $p_{C = 1}^{\max} > 0$  from (17), and  $p_{C = 1}^{\min} = 0$  since choosing  $\phi_z = \omega^z$  sets  $p_{C = 1} = 0$ . Hence, for large  $n$ , one cannot formulate a nontrivial trade-off relation between  $\mathcal{D}$  and  $\widetilde{\nu}$ .

While directly using (12) fails, we seek to rewrite (12) in a form that naturally generalizes to  $n$  paths. Assuming that  $\mathsf{FC}_2$  is symmetric (i.e., a photon with a well-defined path inside the interferometer has an equal chance of going into each of the output modes), note that for  $n = 2$ ,

$$
\mathcal {V} = 2 p _ {\text {g u e s s}} ^ {\max } (C) - 1, \tag {19}
$$

where  $p_{\mathrm{guess}}^{\mathrm{max}}(C) \coloneqq \max_{\vec{\phi}} p_{\mathrm{guess}}(C)$ . Hence, for arbitrary  $n$ , we propose the following formula:

$$
\mathcal {V} := \frac {n p _ {\text {g u e s s}} ^ {\max } (C) - 1}{n - 1}. \tag {20}
$$

Note the similarity between (20) and (16). We emphasize that (20) captures the intuitive notion of interference visibility, since  $p_{\mathrm{guess}}^{\mathrm{max}}(C)$  quantifies the spatial contrast of intensity at the interferometer output.

With these definitions we state the following result.

Theorem 1. For the  $n$ -path MZI in Fig. 1, where  $\mathsf{FC}_1$  is arbitrary while  $\mathsf{FC}_2$  is symmetric, the generalization of Eq. (1) holds:

$$
\mathcal {V} ^ {2} + \mathcal {D} ^ {2} \leqslant 1, \tag {21}
$$

where  $\mathcal{V}$  and  $\mathcal{D}$  are defined in Eqs. (20) and (16), respectively. Furthermore, (21) can be seen as a special case of the entropic uncertainty relation in Eq. (10).

Proof. The proof notes that (13) generalize to

$$
H _ {\min } (Z \mid E) = - \log \left(\frac {1 + (n - 1) \mathcal {D}}{n}\right), \tag {22}
$$

while (14) generalizes with the inequality

$$
\min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } (W) \leqslant \log (1 + (n - 1) \sqrt {1 - \mathcal {V} ^ {2}}), \tag {23}
$$

where (23) follows from (6), noting that

$$
\max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} p _ {\text {g u e s s}} (W) = p _ {\text {g u e s s}} ^ {\max } (C). \tag {24}
$$

Inserting (22) and (23) into (10), while setting  $E_{2}$  to be trivial and  $E_{1} = E$ , and rearranging gives (21).

# VI. EXTENSIONS OF OUR WPDR

# A. Asymmetric couplers

The restriction in Theorem 1 that  $\mathsf{FC}_2$  is symmetric can be relaxed, and a relation of the form of (21) can be obtained for the case where both  $\mathsf{FC}_1$  and  $\mathsf{FC}_2$  are possibly asymmetric. However, the price to pay is that one needs slightly more complicated definitions of visibility and distinguishability, where one postselects on a particular detection event. This point was first highlighted in Ref. [13] for the two-path MZI. Here we extend the WPDR in Ref. [13] to the  $n$ -path MZI, proving the relation (see Appendix B for the proof and further discussion)

$$
\mathcal {V} _ {1} ^ {2} + \mathcal {D} _ {1} ^ {2} \leqslant 1, \tag {25}
$$

where we define

$$
\mathcal {V} _ {1} := \frac {p _ {C = 1} ^ {\max } - p _ {C = 1} ^ {\mathrm {d e c}}}{(n - 1) p _ {C = 1} ^ {\mathrm {d e c}}}, \quad \mathcal {D} _ {1} := \frac {n p _ {\text {g u e s s}} (Z | E , C = 1) - 1}{n - 1}. \tag {26}
$$

Here,  $\mathcal{D}_1$  is the path distinguishability conditioned on the event  $C = 1$ . Also,  $p_{C=1}^{\mathrm{dec}}$  denotes the probability that detector  $D_1$  will click when the system's density matrix has been diagonalized (i.e., decohered) in the which-path basis. Note that  $\mathcal{V}_1$  quantifies the degree to which adjusting the phases  $\vec{\phi}$  can increase the probability  $p_{C=1}$  of detecting the photon at detector  $D_1$ , beyond the baseline value  $p_{C=1}^{\mathrm{dec}}$  associated

with no coherence. So it quantifies the effect of the applied phases on the final detection probability. Interestingly, the formula for  $\nu_{1}$  somewhat resembles the standard definition for visibility in Eq. (12) and, in fact, reduces to (12) for  $n = 2$ .

# B. Quantum erasure

Finally, we show that (10) also provides a natural framework for a scenario called quantum erasure (see, e.g., [1] for an experimental implementation), which aims to enhance the visibility by erasing the which-path information stored in the environment. Reference [10] presented a WPDR for quantum erasure in two-path interferometers. Here we generalize their relation to the  $n$ -path case.

In quantum erasure, after the system  $S$  interacts with an environment  $E$ , the experimenter performs a POVM measurement  $\mathbb{Y} = \{\mathbb{Y}_y\}$  on  $E$ . This gives rise to subensembles associated with the different measurement outcomes  $y$ , and one can define the distinguishability and visibility for the  $y$ th subensemble, which we, respectively, denote  $\mathcal{D}(\mathbb{Y}_y)$  and  $\mathcal{V}(\mathbb{Y}_y)$ . Averaging over all  $y$  gives

$$
\mathcal {D} (\mathbb {Y}) := \sum_ {y} p _ {y} \mathcal {D} (\mathbb {Y} _ {y}) \quad \text {a n d} \quad \mathcal {V} (\mathbb {Y}) := \sum_ {y} p _ {y} \mathcal {V} (\mathbb {Y} _ {y}), \tag {27}
$$

where  $p_y$  is the probability of outcome  $y$ . Our result for quantum erasure is that, for the  $n$ -path MZI in Fig. 1, it holds for any choice of  $\mathbb{Y}$  that (see Appendix C for proof)

$$
\mathcal {V} (\mathbb {Y}) ^ {2} + \mathcal {D} (\mathbb {Y}) ^ {2} \leqslant 1. \tag {28}
$$

Note that (28) generalizes and implies our WPDR in Eq. (21). One can recover (21) from (28) by noting that  $\mathcal{V} \leqslant \mathcal{V}(\mathbb{Y})$  and by choosing  $\mathbb{Y}$  to optimize the distinguishability, since  $\max_{\mathbb{Y}} \mathcal{D}(\mathbb{Y}) = \mathcal{D}$ . Alternatively, one can choose  $\mathbb{Y}$  to maximize  $\mathcal{V}(\mathbb{Y})$ , in which case (28) provides a fundamental limit on the recoverable visibility in a quantum erasure experiment.

We show (see Appendix C) that (28) follows from a relation of the form

$$
H _ {\min } (Z | Y) + \min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } (W | Y) \geqslant \log n, \tag {29}
$$

where  $Y$  is the classical register that stores the outcome of the  $\mathbb{Y}$  measurement on  $E$ . Note that (29) is a special case of (10) where  $E_1 = Y$  and  $E_2 = Y'$ , with  $Y'$  a copy of  $Y$  (which has the same information content as  $Y$  and, hence, can be replaced by  $Y$  in the entropy term).

# VII. DISCUSSION OF THE LITERATURE

The first WPDR for  $n$ -path interferometers was given by Durr [20]. Durr exploited the fact that the purity function  $\mathrm{Tr}\rho^2$  can be broken down into two terms,

$$
\sum_ {z} \rho_ {z z} ^ {2} + \sum_ {z, z ^ {\prime} \neq z} | \rho_ {z z ^ {\prime}} | ^ {2} = \operatorname {T r} \rho^ {2}, \tag {30}
$$

where  $\rho_{zz'} \coloneqq \langle z|\rho |z'\rangle$ . Since  $\mathrm{Tr}\rho^2 \leqslant 1$ , Eq. (30) gives a WPDR where the first and second terms on the left-hand side are interpreted as measures of particle and wave behavior, respectively. (More precisely, Durr incorporated some

dimension-dependent scaling factors into these terms for normalization purposes.)

Furthermore, Durr generalized the relation in Eq. (30) to the more interesting case where a which-path detector obtains some information inside the interferometer, i.e., the scenario considered in Eq. (1). However, Durr's generalized relation has been critiqued [35-37] due to the fact that it is not saturated for all pure states. Nevertheless, we do not see this as a major issue. Consider that Maassen and Uffink's EUR [38] is not saturated by all pure states. Yet their relation is by far the most famous EUR, and it has inspired countless studies on the topic.

We believe that much more important issues are whether the employed quantitative measures (i) are operational and experimentally friendly and (ii) capture one's intuition about wave and particle behavior. One could argue that Durr was on the right track, in this sense, with his measure of wave behavior, for which he gave an operational interpretation [20]. However, Durr's measure of particle behavior is not as operational or intuitive as the one in Eq. (16), proposed in Ref. [8].

Interestingly, some recent studies [21-23] seem to do the opposite of Durr's. They employ operational measures of particle behavior, e.g., Ref. [22] employs the definition in Eq. (16). But these references replace visibility with a more abstract quantity called coherence. While coherence is an interesting quantity for theorists, it remains to be clarified how it precisely relates to interferometry experiments.

The nice aspect of our approach is that both the wave and the particle terms are operational—both involving the optimal guessing probability. The symmetric nature of the two terms seems quite natural. It leads to a simple guessing-game view of wave-particle duality, as shown in Fig. 1(b).

Furthermore, all of the previous works stop short of considering the case where both the input and the output beam splitters are asymmetric. Indeed the relations derived in Refs. [20-23] do not apply to this situation. The fact that we can treat this situation is a testament to the robustness of our entropic-uncertainty framework.

We remark that, after completion of our work, Renes [39] proved an uncertainty relation that is analogous to (but not exactly the same as) Eq. (9). In some cases Renes's bound is tighter than (9), and in other cases the opposite is true. Interestingly, like us, Renes derived his relation directly from the MMEUR.

# VIII. CONCLUSION

In summary, we have obtained three novel WPDRs for  $n$ -path interferometers, Eqs. (21), (25), and (28), each of which generalizes the famous WPDR of Refs. [7,8]. All of these novel WPDRs follow directly from the MMEUR, combined with our new operational meaning for the max-entropy in Eq. (6). In this sense, wave-particle duality is the entropic uncertainty principle in disguise, and the latter provides a robust framework for formulating the former. We emphasize that our generic WPDR in Eq. (10) can be applied to a variety of interferometric scenarios and, hence, when specialized, will lead to other novel WPDRs.

# ACKNOWLEDGMENTS

The author was funded by Sandia National Laboratories, Office of Naval Research, Industry Canada, an NSERC Discovery Grant, and the Ontario Research Fund.

# APPENDIX A: RELATIONSHIP BETWEEN MAX-ENTROPY AND GUESSING PROBABILITY

Here we prove (6). First, we state a technical lemma involving the  $p$  norm, which is defined by

$$
\| \vec {x} \| _ {p} := \left(\sum_ {j} | x _ {j} | ^ {p}\right) ^ {1 / p} \tag {A1}
$$

for a real vector  $\vec{x} = \{x_j\}$ . In particular, we consider the special cases

$$
\| \vec {x} \| _ {\infty} = \max  _ {j} | x _ {j} |, \tag {A2}
$$

$$
\| \vec {x} \| _ {1 / 2} = \left(\sum_ {j} \sqrt {| x _ {j} |}\right) ^ {2}. \tag {A3}
$$

We remark that  $\| \vec{x}\| _p$  is technically a norm for  $p\geqslant 1$ , while this is not true for  $0 < p < 1$ .

Lemma 2. For a discrete probability distribution  $\vec{q} = \{q_j\}$  over a sample space of size  $d$ , it holds that

$$
\left(\| \vec {q} \| _ {1 / 2} - 1\right) ^ {2} + \left(d \| \vec {q} \| _ {\infty} - 1\right) ^ {2} \leqslant (d - 1) ^ {2}, \tag {A4}
$$

where equality holds if  $d = 2$ .

Proof. The function  $\| \vec{q}\|_{1 / 2}$  is Schur-concave, i.e., it satisfies

$$
\| \vec {q} \| _ {1 / 2} \leqslant \| \vec {r} \| _ {1 / 2} \quad \text {i f} \quad \vec {q} \succ \vec {r}. \tag {A5}
$$

The majorization condition  $\vec{q} \succ \vec{r}$  is defined by

$$
\sum_ {j = 1} ^ {k} q _ {j} \geqslant \sum_ {j = 1} ^ {k} r _ {j} \quad \text {f o r a l l} \quad k \in [ d ], \tag {A6}
$$

where the probabilities are assumed to be listed in descending order, i.e.,  $q_{j} \geqslant q_{l}$  for  $j < l$ , and likewise for  $\vec{r}$ .

Now let us choose

$$
\vec {s} := \left\{q _ {1}, \frac {1 - q _ {1}}{d - 1}, \frac {1 - q _ {1}}{d - 1}, \dots , \frac {1 - q _ {1}}{d - 1} \right\} \tag {A7}
$$

and note that this choice gives  $\vec{q} \succ \vec{s}$ . Hence we have

$$
\| \vec {q} \| _ {1 / 2} \leqslant \| \vec {s} \| _ {1 / 2} = \left(\sqrt {q _ {1}} + \sqrt {(d - 1) (1 - q _ {1})}\right) ^ {2}. \tag {A8}
$$

Now consider the function

$$
f \left(q _ {1}\right) := (d - 1) ^ {2} - \left(d q _ {1} - 1\right) ^ {2} - \left(\| \vec {s} \| _ {1 / 2} - 1\right) ^ {2}. \tag {A9}
$$

We wish to show that  $f(q_{1}) \geqslant 0$ . Note that, using (A8) and the fact that  $\| \vec{q} \|_{\infty} = q_{1}$ , the non-negativity of  $f(q_{1})$  would imply that the desired result, (A4), is true.

The equality of (A4) for  $d = 2$  is easily verified, so in what follows we restrict ourselves to  $d \geqslant 3$ . To show  $f(q_{1}) \geqslant 0$  we write

$$
f \left(q _ {1}\right) = \left(1 - q _ {1}\right) \left(a \left(q _ {1}\right) - b \left(q _ {1}\right)\right), \tag {A10}
$$

where

$$
a \left(q _ {1}\right) := d (d - 2) + d ^ {2} q _ {1}, \tag {A11}
$$

$$
b \left(q _ {1}\right) := \left((d - 2) \sqrt {1 - q _ {1}} + \sqrt {q _ {1} (d - 1)}\right) ^ {2}. \tag {A12}
$$

We just need to verify that  $a(q_1) \geqslant b(q_1)$ . It is straightforward to show that

$$
\max  _ {q _ {1} \in [ 0, 1 ]} b (q _ {1}) = (d - 2) ^ {2} + d - 1, \tag {A13}
$$

and clearly  $a(q_1) \geqslant d(d - 2)$ , so we have

$$
a \left(q _ {1}\right) - b \left(q _ {1}\right) \geqslant d - 3, \tag {A14}
$$

which proves  $f(q_{1}) \geqslant 0$  and hence (A4).

We note that (A4) is equivalent to

$$
H _ {\max } (X) \leqslant \log \left(1 + \sqrt {(d - 1) ^ {2} - (d p _ {\text {g u e s s}} (X) - 1) ^ {2}}\right), \tag {A15}
$$

which is a special case of relation (6), corresponding to a trivial  $B$  system. Now we prove the general case, where  $B$  is nontrivial. For convenience, we restate (6) in the following lemma.

Lemma 3. For a classical-quantum state  $\rho_{XB} = \sum_{x}p_{x}|x\rangle \langle x|\otimes \rho_{B}^{x}$ , where  $d = |X|$ , it holds that

$$
H _ {\max } (X \mid B) \leqslant \log \left(1 + \sqrt {(d - 1) ^ {2} - (d p _ {\text {g u e s s}} (X \mid B) - 1) ^ {2}}\right). \tag {A16}
$$

Proof. In what follows, we use some properties of the min- and max-entropies, and we refer the reader to Ref. [40] for elaboration. For example, the data-processing inequality for the max-entropy implies that

$$
2 ^ {H _ {\max } (X \mid B)} \leqslant 2 ^ {H _ {\max } (X \mid M)}, \tag {A17}
$$

where  $M$  is the classical register produced from measuring POVM  $\mathbb{M} = \{\mathbb{M}_m\}$  in system  $B$ . That is, the right-hand side of (A17) is evaluated for the state

$$
\begin{array}{l} \rho_ {X M} := \sum_ {m} \operatorname {T r} _ {B} (\rho_ {X B} (\mathbb {1} \otimes \mathbb {M} _ {m})) \otimes | m \rangle \langle m | \\ = \sum_ {x, m} \operatorname {T r} \left(p _ {x} \rho_ {B} ^ {x} \mathbb {M} _ {m}\right) | x \rangle \langle x | \otimes | m \rangle \langle m |. \tag {A18} \\ \end{array}
$$

Suppose we choose  $\mathbb{M}$  such that it is the measurement that optimizes the guessing probability, i.e.,

$$
p _ {\text {g u e s s}} (X | B) = \sum_ {x} p _ {x} \operatorname {T r} \left(\mathbb {M} _ {x} \rho_ {B} ^ {x}\right). \tag {A19}
$$

Using properties of the guessing probability, we can write

$$
p _ {\text {g u e s s}} (X | B) = p _ {\text {g u e s s}} (X | M) = \sum_ {m} q _ {m} p _ {\text {g u e s s}} (X | M = m), \tag {A20}
$$

where  $q_{m} \coloneqq \mathrm{Tr}(\rho_{B}\mathbb{M}_{m})$  is the probability of outcome  $M = m$ , and  $p_{\mathrm{guess}}(X|M = m)$  denotes the guessing probability for  $X$  conditioned on outcome  $M = m$ .

From (A17) and the expression for the max-entropy when conditioning on classical information [40], we have

$$
2 ^ {H _ {\max } (X \mid B)} \leqslant \sum_ {m} q _ {m} 2 ^ {H _ {\max } (X \mid M = m)}, \tag {A21}
$$

where  $H_{\mathrm{max}}(X|M = m)$  is the max-entropy of  $X$  conditioned on outcome  $M = m$ . Combining (A21) with (A15) gives

$$
\begin{array}{l} 2 ^ {H _ {\max } (X | B)} - 1 \\ \leqslant \sum_ {m} q _ {m} \sqrt {(d - 1) ^ {2} - (d p _ {\text {g u e s s}} (X | M = m) - 1) ^ {2}} (A22) \\ \leqslant \sqrt {(d - 1) ^ {2} - \sum_ {m} q _ {m} (d p _ {\text {g u e s s}} (X | M = m) - 1) ^ {2}} \quad (\mathrm {A} 2 3) \\ \leqslant \sqrt {(d - 1) ^ {2} - \left(d \sum_ {m} q _ {m} p _ {\text {g u e s s}} (X | M = m) - 1\right) ^ {2}}, (A24) \\ \end{array}
$$

where the second (third) inequality uses the concavity (convexity) of the square root (square) function. Combining (A24) with (A20) proves the desired result.

# APPENDIX B: ASYMMETRIC COUPLERS

Theorem 1 treats the  $n$ -path interferometer in Fig. 1 for the special case where  $\mathsf{FC}_2$  is symmetric, or, in other words, unbiased, with respect to the  $n$  output modes. Here we show that this restriction can be relaxed, and one can derive a WPDR for the general scenario where both  $\mathsf{FC}_1$  and  $\mathsf{FC}_2$  are possibly asymmetric, namely, Eq. (25). Furthermore, we derive (25) from the MMEUR: more specifically, from our generic relation in Eq. (10).

First, let us introduce our notation. Recall that  $S$  denotes the photon's spatial degree of freedom inside the interferometer and  $E$  is the environment. Let  $\rho_{SE}$  denote the bipartite state for  $S$  and  $E$  at a time immediately after these two systems finish interacting inside the interferometer, and denote this time  $t_1$ . As shown in Fig. 1, after time  $t_1$ , the photon receives a phase shift  $\phi_z$  depending on its path, which we can write as the unitary

$$
U _ {\vec {\phi}} := \sum_ {z} e ^ {i \phi_ {z}} | z \rangle \langle z |. \tag {B1}
$$

Then the photon approaches  $\mathsf{FC}_2$ , whose action is given by some unitary matrix  $U_{2}$  applied to  $\mathcal{H}_S$ . Finally, the photon is detected at one of the detectors. Let  $\mathbb{C} := \{\mathbb{C}_c\}_{c=1}^n$  denote the POVM associated with detection at the interferometer output. This POVM gives rise to the random variable  $C$ , which encodes the information about which detector clicks, as noted in the text. For notational simplicity, we lump  $U_{2}$  and  $\mathbb{C}$  together into a single step, and we define the POVM

$$
\tilde {\mathbb {C}} := \left\{\tilde {\mathbb {C}} _ {c} \right\} _ {c = 1} ^ {n}, \quad \text {w i t h} \quad \tilde {\mathbb {C}} _ {c} := U _ {2} ^ {\dagger} \mathbb {C} _ {c} U _ {2}. \tag {B2}
$$

As noted in the text, we need to modify the definitions of distinguishability and visibility in order to formulate a universally valid relation. Let us first consider distinguishability. Consider a game where one tries to guess which path the photon took given that one knows that the photon was detected at a particular detector, say detector  $D_{1}$  (which corresponds to  $C = 1$ ). The guessing probability for this game can be written as  $p_{\mathrm{guess}}(Z|E,C = 1)$ , i.e., the probability of guessing the path  $Z$  given the optimal measurement on the environment

$E$  and given the outcome  $C = 1$ . We define the postselected distinguishability  $\mathcal{D}_1$  as

$$
\mathcal {D} _ {1} := \frac {n p _ {\text {g u e s s}} (Z | E , C = 1) - 1}{n - 1}. \tag {B3}
$$

Moving on to visibility, we define

$$
\mathcal {V} _ {1} := \frac {p _ {C = 1} ^ {\max } - p _ {C = 1} ^ {\mathrm {d e c}}}{(n - 1) p _ {C = 1} ^ {\mathrm {d e c}}}, \tag {B4}
$$

where  $p_{C=1}^{\max} \coloneqq \max_{\vec{\phi}} (p_{C=1})$  is the probability that detector  $D_1$  will click maximized over all phases  $\vec{\phi}$  applied inside the interferometer. Also,  $p_{C=1}^{\mathrm{dec}}$  denotes the probability that detector  $D_1$  will click in the case where the state inside the interferometer is fully decohered, i.e., where all of the which-path information has leaked out to the environment and hence the system's density matrix has been diagonalized in the which-path basis. Mathematically, we can write

$$
p _ {C = 1} ^ {\max } = \max  _ {\vec {\phi}} \operatorname {T r} (U _ {\vec {\phi}}   \rho_ {S}   U _ {\vec {\phi}} ^ {\dagger} \tilde {\mathbb {C}} _ {1}) \quad \text {a n d}
$$

$$
p _ {C = 1} ^ {\mathrm {d e c}} = \operatorname {T r} \left(\sum_ {z} | z \rangle \langle z | \rho_ {S} | z \rangle \langle z | \tilde {\mathbb {C}} _ {1}\right). \tag {B5}
$$

The intuition behind the formula for  $\mathcal{V}_1$  is the following. It quantifies the degree to which adjusting the phases  $\phi$  can increase the probability  $p_{C=1}$  of detecting the photon at detector  $D_1$ , beyond the baseline value  $p_{C=1}^{\mathrm{dec}}$  associated with no coherence. So it quantifies the effect of the applied phases on the final detection probability. One may notice that  $\mathcal{V}_1$  looks somewhat similar to (12), which is the most common way of writing  $\mathcal{V}$  in the two-path case. Indeed, one has  $\mathcal{V}_1 = \mathcal{V}$  in the two-path case, which can be seen using the identity [16]

$$
p _ {C = 1} ^ {\text {d e c}} = \left(p _ {C = 1} ^ {\max } + p _ {C = 1} ^ {\min }\right) / 2, \tag {B6}
$$

which holds in the special case of  $n = 2$ . However, for  $n > 2$ ,  $\mathcal{V}_1$  is generally not equal to the expression in Eq. (12).

We remark that  $\mathcal{D}_1$  and  $\nu_{1}$  can be experimentally measured as follows. The experimenter, whom we call Alice, can insert a variable attenuator into each arm of the interferometer in Fig. 1, such that the attenuator can be seteitherto allow the photon to pass or to block the photon. To measure  $\mathcal{D}_1$ , Alice flips a fair  $n$ -sided classical coin in order to determine which path inside the interferometer to keep open (to allow the photon to pass), while blocking the other  $n - 1$  paths. To compute  $p_{\mathrm{guess}}(Z|E,C = 1)$  Alice employs a second experimenter, named Bob, who tries to guess which path Alice kept open, given that Bob has access to  $E$  and given that he postselects on  $C = 1$  outcomes. In the case of  $\nu_{1}$ , measuring  $p_{C = 1}^{\mathrm{max}}$  is straightforward, while  $p_{C = 1}^{\mathrm{dec}}$  can be measured as follows. Alice once again flips a fair  $n$ -sided classical coin to determine which path inside the interferometer to keep open (while blocking the other  $n - 1$  paths) and then computes  $p_{C = 1}^{\mathrm{dec}}$  as the number of detection events at  $D_{1}$  divided by the total number of detection events.

Reference [13] proved a WPDR for the two-path MZI for the general case where both fiber couplers (or beam splitters in the case of free-space propagation) are asymmetric. We now state the following theorem, which generalizes the WPDR in Ref. [13] to the  $n$ -path MZI.

Theorem 4. For the  $n$ -path MZI in Fig. 1, where  $\mathsf{FC}_1$  and  $\mathsf{FC}_2$  are arbitrary (possibly asymmetric) fiber couplers, it holds that

$$
\mathcal {V} _ {1} ^ {2} + \mathcal {D} _ {1} ^ {2} \leqslant 1. \tag {B7}
$$

Moreover, (B7) is a special case of the MMEUR in Eq. (10).

Proof. The proof simply involves applying (10) to the appropriate density operator.

Consider an isometry  $V$  that produces a copy of the which-path information and stores it in a register  $S'$ , which we can write as a map  $\mathcal{H}_{SE} \to \mathcal{H}_{S'SE}$  given by

$$
V := \sum_ {z} | z \rangle_ {S ^ {\prime}} \otimes | z \rangle \langle z | _ {S} \otimes \mathbb {1} _ {E}. \tag {B8}
$$

Consider the density operator obtained from applying this isometry to  $\rho_{SE}$ :

$$
\tilde {\rho} _ {S ^ {\prime} S E} := V \rho_ {S E} V ^ {\dagger}. \tag {B9}
$$

We note that  $\tilde{\rho}_{S^{\prime}SE}$  is not actually the physical state; rather it is a mathematical construction that we use to prove the desired result.

Now consider the density operator obtained from postselecting on events where detector  $D_{1}$  clicks (i.e., where  $C = 1$ ). That is, we take the density operator  $\tilde{\rho}_{S^{\prime}SE}$  and we consider its overlap with the POVM element  $\tilde{\mathbb{C}}_1$  associated with the event  $C = 1$ . Applying this postselection to  $\tilde{\rho}_{S^{\prime}SE}$  gives the following density operator:

$$
\widehat {\rho} _ {S ^ {\prime} E} := \frac {\operatorname {T r} _ {S} \left[ \left(\mathbb {1} _ {S ^ {\prime}} \otimes \tilde {\mathbb {C}} _ {1} \otimes \mathbb {1} _ {E}\right) \tilde {\rho} _ {S ^ {\prime} S E} \right]}{\operatorname {T r} \left[ \left(\mathbb {1} _ {S ^ {\prime}} \otimes \tilde {\mathbb {C}} _ {1} \otimes \mathbb {1} _ {E}\right) \tilde {\rho} _ {S ^ {\prime} S E} \right]}. \tag {B10}
$$

We now apply (10) to the density operator in Eq. (B10), setting  $E_{2}$  to a trivial system and  $E_{1} = E$ , giving

$$
H _ {\min } \left(Z _ {S ^ {\prime}} | E\right) _ {\widehat {\rho}} + \min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } \left(W _ {S ^ {\prime}}\right) _ {\widehat {\rho}} \geqslant \log n, \tag {B11}
$$

where the  $\widehat{\rho}$  subscripts in Eq. (B11) serve as a reminder that the entropy terms are evaluated for the state in Eq. (B10), and the  $S^{\prime}$  subscripts in Eq. (B11) indicate that the random variables arise from observables in system  $S^{\prime}$ . Noting that  $Z_{S^{\prime}}$  is a copy of the which-path information for system  $S$ , one can see that

$$
\begin{array}{l} H _ {\min } \left(Z _ {S ^ {\prime}} | E\right) _ {\hat {\rho}} = - \log p _ {\text {g u e s s}} \left(Z _ {S ^ {\prime}} | E\right) _ {\hat {\rho}} (B12) \\ = - \log p _ {\text {g u e s s}} \left(Z _ {S} \mid E, C = 1\right) _ {\rho} (B13) \\ = - \log \left(\frac {1 + (n - 1) \mathcal {D} _ {1}}{n}\right), (B14) \\ \end{array}
$$

where we note that (B13) refers to the physical state  $\rho_{SE}$ . Likewise we can relate the max-entropy term in Eq. (B11) to  $\mathcal{V}_1$  as

$$
\min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } \left(W _ {S ^ {\prime}}\right) _ {\hat {\rho}} \leqslant \log \left(1 + (n - 1) \sqrt {1 - \mathcal {V} _ {1} ^ {2}}\right), \tag {B15}
$$

where we elaborate on the proof of (B15) below. Inserting (B14) and (B15) into (B11) and rearranging gives the desired result, (B7).

Equation (B15) is proved as follows. First, using (6) gives

$$
\min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } \left(W _ {S ^ {\prime}}\right) _ {\widehat {\rho}} \leqslant \log \left(1 + (n - 1) \sqrt {1 - \left(\frac {n \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} p _ {\text {g u e s s}} \left(W _ {S ^ {\prime}}\right) _ {\widehat {\rho}} - 1}{n - 1}\right) ^ {2}}\right). \tag {B16}
$$

So it remains only to show that

$$
n \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} p _ {\text {g u e s s}} \left(W _ {S ^ {\prime}}\right) _ {\hat {\rho}} = \frac {p _ {C = 1} ^ {\max }}{p _ {C = 1} ^ {\mathrm {d e c}}}. \tag {B17}
$$

The proof of (B17) goes as follows:

$$
\begin{array}{l} \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} p _ {\text {g u e s s}} \left(W _ {S ^ {\prime}}\right) _ {\hat {\rho}} = \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} p _ {\text {g u e s s}} \left(W _ {S ^ {\prime}} \mid C = 1\right) _ {\tilde {\rho}} (B18) \\ = \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} \max  _ {w} \Pr \left(W _ {S ^ {\prime}} = w \mid C = 1\right) _ {\tilde {\rho}} (B19) \\ = \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} \max  _ {w} \frac {\Pr \left(W _ {S ^ {\prime}} = w , C = 1\right) _ {\tilde {\rho}}}{\Pr (C = 1) _ {\tilde {\rho}}} (B20) \\ = \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} \max  _ {w} \frac {\operatorname {T r} \left(\left(| \mathbb {W} _ {w} \rangle \langle \mathbb {W} _ {w} | \otimes \tilde {\mathbb {C}} _ {1}\right) \tilde {\rho} _ {S ^ {\prime} S}\right)}{\operatorname {T r} \left(\tilde {\mathbb {C}} _ {1} \tilde {\rho} _ {S}\right)} (B21) \\ = \frac {1}{p _ {C = 1} ^ {\mathrm {d e c}}} \max  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} \max  _ {w} \operatorname {T r} \left(\left| \mathbb {W} _ {w} \right\rangle \left(\mathbb {W} _ {w} \right| \otimes \tilde {\mathbb {C}} _ {1}\right) \tilde {\rho} _ {S ^ {\prime} S}) (B22) \\ = \frac {1}{p _ {C = 1} ^ {\mathrm {d e c}}} \max  _ {\left\{\phi_ {z} \right\}} \operatorname {T r} \left(\left(\sum_ {z, z ^ {\prime}} \frac {e ^ {i \left(\phi_ {z} - \phi_ {z ^ {\prime}}\right)}}{n} | z \rangle \langle z ^ {\prime} | \otimes \tilde {\mathbb {C}} _ {1}\right) \tilde {\rho} _ {S ^ {\prime} S}\right) (B23) \\ = \frac {1}{n p _ {C = 1} ^ {\mathrm {d e c}}} \max  _ {\left\{\phi_ {z} \right\}} \operatorname {T r} \left(\left(\sum_ {z, z ^ {\prime}} e ^ {i \left(\phi_ {z} - \phi_ {z ^ {\prime}}\right)} | z \rangle \langle z ^ {\prime} | \otimes \tilde {\mathbb {C}} _ {1}\right) \left(\sum_ {z ^ {\prime \prime}, z ^ {\prime \prime \prime}} \left| z ^ {\prime \prime} \right\rangle \left\langle z ^ {\prime \prime \prime} \right| \otimes \left| z ^ {\prime \prime} \right\rangle \left\langle z ^ {\prime \prime} \right| \rho_ {S} \left| z ^ {\prime \prime \prime} \right\rangle \left\langle z ^ {\prime \prime \prime} \right|\right)\right) (B24) \\ = \frac {1}{n p _ {C = 1} ^ {\mathrm {d e c}}} \max  _ {\left\{\phi_ {z} \right\}} \operatorname {T r} \left(\sum_ {z, z ^ {\prime}} e ^ {i \left(\phi_ {z} - \phi_ {z ^ {\prime}}\right)} \tilde {\mathbb {C}} _ {1} \left| z ^ {\prime} \right\rangle \langle z ^ {\prime} \mid \rho_ {S} | z \rangle \langle z |\right) (B25) \\ = \frac {1}{n p _ {C = 1} ^ {\mathrm {d e c}}} \max  _ {\left\{\phi_ {z} \right\}} \operatorname {T r} \left(\tilde {\mathbb {C}} _ {1} U _ {\vec {\phi}} \rho_ {S} U _ {\vec {\phi}} ^ {\dagger}\right) (B26) \\ = \frac {p _ {C = 1} ^ {\max}}{n p _ {C = 1} ^ {\mathrm {d e c}}}. (B27) \\ \end{array}
$$

Here,  $\operatorname{Pr}$  denotes "probability," and (B20) uses the fact that the joint probability for two events  $X = x$  and  $Y = y$  is given by  $\operatorname{Pr}(X = x, Y = y) = \operatorname{Pr}(X = x | Y = y) \operatorname{Pr}(Y = y)$ . Also, (B23) uses the fact that any state  $|\psi\rangle$  that is unbiased to the  $\mathbb{Z}$  basis can be written as  $|\psi\rangle = \sum_{z} (e^{i\phi_z} / \sqrt{n}) |z\rangle$  for some set of phases  $\{\phi_z\}$ . This concludes the proof.

# APPENDIX C: QUANTUM ERASURE

Here we give a proof of (28). As a reminder, we restate this result as follows. Recall that a quantum erasure experiment involves performing a measurement  $\mathbb{Y} = \{\mathbb{Y}_y\}$  on the environment  $E$  and using the measurement outcome to sort the data into subensembles. Let

$$
\mathcal {D} (\mathbb {Y} _ {y}) := \frac {n p _ {\text {g u e s s}} (Z | Y = y) - 1}{n - 1} \quad \text {a n d}
$$

$$
\mathcal {V} (\mathbb {Y} _ {y}) := \frac {n \max  _ {\vec {\phi}} p _ {\text {g u e s s}} (C | Y = y) - 1}{n - 1} \tag {C1}
$$

denote the path distinguishability and fringe visibility, respectively, for the  $y$ th subensemble, i.e., associated with outcome

$y$  of the  $\mathbb{Y}$  measurement. Averaging over all  $y$  gives the quantities

$$
\mathcal {D} (\mathbb {Y}) := \sum_ {y} p _ {y} \mathcal {D} (\mathbb {Y} _ {y}) \quad \text {a n d} \quad \mathcal {V} (\mathbb {Y}) := \sum_ {y} p _ {y} \mathcal {V} (\mathbb {Y} _ {y}), \tag {C2}
$$

where  $p_y$  is the probability of outcome  $y$ . Then we have the following result, which is a generalization of Theorem 1. (We remark that, while the following theorem is stated for the case where  $\mathsf{FC}_2$  is symmetric, this assumption can be relaxed using the approach in Appendix B, where the definitions of visibility and distinguishability are slightly modified.)

Theorem 5. For the  $n$ -path MZI in Fig. 1, where  $\mathsf{FC}_1$  is arbitrary while  $\mathsf{FC}_2$  is symmetric, it holds that

$$
\mathcal {V} (\mathbb {Y}) ^ {2} + \mathcal {D} (\mathbb {Y}) ^ {2} \leqslant 1. \tag {C3}
$$

Proof. A quantum erasure experiment can be separated into three sequential steps, each of which is a CPTP map:

(1) The system  $S$  (i.e., the photon's spatial degree of freedom) interacts with an environment  $E$ , via CPTP map  $\mathcal{E}_{\mathrm{int}}$ .

(2) System  $E$  is measured and the outcome is stored in a register  $Y$ , via CPTP map  $\mathcal{E}_{\mathrm{meas}}$ .  
(3) The experimenter uses this measurement result to enhance the visibility in system  $S$  (i.e., to sort the data point into a subensemble and determine the optimal phase shift for that subensemble). This is modeled as a CPTP map  $\mathcal{E}_{\mathrm{enh}}$  that couples  $Y$  to  $S$ .  
The overall CPTP map  $\mathcal{E}$  is a composition of these three maps:  
$\mathcal{E} = \mathcal{E}_{\mathrm{enh}}\circ \mathcal{E}_{\mathrm{meas}}\circ \mathcal{E}_{\mathrm{int}}$  (C4)  
Suppose the system starts in the state  $\rho_{S}^{(1)}$ , just after it enters the interferometer. The interaction with  $E$  results in the state  $\rho_{SE}^{(2)} \coloneqq \mathcal{E}_{\mathrm{int}}(\rho_{S}^{(1)})$ . Next,  $\mathcal{E}_{\mathrm{meas}}$  performs the measurement  $\mathbb{Y} = \{\mathbb{Y}_y\}$  on system  $E$  and stores the outcome in two (redundant) registers,  $Y$  and  $Y'$ , resulting in the state  
$\rho_{SYY'}^{(3)} \coloneqq \mathcal{E}_{\mathrm{meas}}\bigl (\rho_{SE}^{(2)}\bigr) = \sum_y p_y\rho_{S,y}^{(2)}\otimes |y\rangle \langle y|_Y\otimes |y\rangle \langle y|_{Y'}$  (C5)  
Here, state  $|y\rangle$  corresponds to obtaining outcome  $y$  from measuring  $\mathbb{Y}$ , with the set  $\{|y\rangle\}$  forming an orthonormal basis on the register Hilbert space, and outcome  $y$  leaves system  $S$  in the conditional state  
$\rho_{S,y}^{(2)} = \frac{1}{p_y}\mathrm{Tr}_E\bigl [(\mathbb{1}_S\otimes \mathbb{Y}_y)\rho_{SE}^{(2)}\bigr ],$  with  
$p_{y} = \mathrm{Tr}\bigl [(\mathbb{1}_{S}\otimes \mathbb{Y}_{y})\rho_{SE}^{(2)}\bigr ]$  (C6)  
The point of having two registers ( $Y$  and  $Y'$ ) is that one register will act as system  $E_1$  to be used to enhance the distinguishability—while the other will act as system  $E_2$  to be used to enhance the visibility.  
For each outcome  $y$ , we wish to obtain the full visibility that is available. So we allow the experimenter to choose the optimal set of phase shifts  $\vec{\phi}_y$  for each  $y$ , i.e., let  $\vec{\phi}_y$  achieve the optimization in  $\mathcal{V}(\mathbb{Y}_y)$  as defined in Eq. (C1). In other words, we allow the experimenter, given the outcome  $y$ , to rotate the system  $S$  via a unitary  $U_{\vec{\phi}_y}$  that has the form given in Eq. (B1). Accounting for all possible values of  $y$ , the overall unitary is a controlled unitary  $U_{\mathrm{enh}} := \sum_y U_{\vec{\phi}_y} \otimes |y\rangle \langle y|_Y$ , where  $Y$  acts as the control system. Hence the action of the map that enhances the visibility is  
$\rho_{SYY'}^{(4)} \coloneqq \mathcal{E}_{\mathrm{enh}}\bigl(\rho_{SYY'}^{(3)}\bigr) = U_{\mathrm{enh}}\rho_{SYY'}^{(3)}U_{\mathrm{enh}}^{\dagger}$  
$= \sum_{y}p_{y}\tilde{\rho}_{S,y}^{(2)}\otimes |y\rangle \langle y|_{Y}\otimes |y\rangle \langle y|_{Y^{\prime}}$  ，with  
$\tilde{\rho}_{S,y}^{(2)}:= U_{\vec{\phi}_y}\rho_{S,y}^{(2)}\big(U_{\vec{\phi}_y}\big)^\dagger.$  (C7)

Applying (10) to the state  $\rho_{SYY'}^{(4)}$ , choosing  $E_1 = Y$  and  $E_2 = Y'$ , and noting that  $Y'$  and  $Y$  are identical copies and hence can be interchanged, gives  
$H_{\min}(Z|Y)_{\rho^{(4)}} + \min_{W\in \mathcal{M}_{\mathbb{Z}}}H_{\max}(W|Y)_{\rho^{(4)}}\geqslant \log n,$  (C8)  
where the subscript  $\rho^{(4)}$  emphasizes that the entropy terms are evaluated for the state  $\rho_{SYY'}^{(4)}$ . Equation (C8) is our quantum erasure relation, corresponding to Eq. (29) in the text.  
We note that (C8) can be rewritten as follows. Using the definition of  $\mathcal{D}(\mathbb{Y})$  in Eq. (C2), we have

$$
\begin{array}{l} H _ {\min } (Z | Y) _ {\rho^ {(4)}} = - \log p _ {\text {g u e s s}} (Z | Y) (C9) \\ = - \log \left(\sum_ {y} p _ {y} p _ {\text {g u e s s}} (Z | Y = y)\right) (C10) \\ = \log n - \log ((n - 1) \mathcal {D} (\mathbb {Y}) + 1). (C11) \\ \end{array}
$$

Likewise, the definition of  $\mathcal{V}(\mathbb{Y})$  gives

$$
\begin{array}{l} \min  _ {\mathbb {W} \in \mathcal {M} _ {\mathbb {Z}}} H _ {\max } (W | Y) _ {\rho^ {(4)}} \\ \leqslant H _ {\max } (C | Y) _ {\rho^ {(4)}} (C12) \\ \leqslant \log \left(1 + \sqrt {(n - 1) ^ {2} - (n p _ {\text {g u e s s}} (C | Y) _ {\rho^ {(4)}} - 1) ^ {2}}\right) (C13) \\ = \log (1 + (n - 1) \sqrt {1 - \mathcal {V} (\mathbb {Y}) ^ {2}}). (C14) \\ \end{array}
$$

Here, (C12) uses the fact that  $\mathsf{FC}_2$  is symmetric, and hence the POVM  $\tilde{\mathbb{C}}$  defined in Eq. (B2) corresponds to an orthonormal basis that is mutually unbiased to  $\mathbb{Z}$ , i.e.,  $\tilde{\mathbb{C}} \in \mathcal{M}_{\mathbb{Z}}$ . Equation (C13) uses (6). Equation (C14) uses the fact that the state  $\rho_{SYY'}^{(4)}$  in Eq. (C7) is constructed such that  $p_{\mathrm{guess}}(C|Y = y)$  is optimal, i.e.,

$$
\begin{array}{l} \mathcal {V} (\mathbb {Y}) = \sum_ {y} p _ {y} \mathcal {V} (\mathbb {Y} _ {y}) (C15) \\ = \sum_ {y} p _ {y} \left(\frac {n \max  _ {\bar {\phi}} p _ {\text {g u e s s}} (C \mid Y = y) - 1}{n - 1}\right) (C16) \\ = \sum_ {y} p _ {y} \left(\frac {n p _ {\text {g u e s s}} (C | Y = y) _ {\rho^ {(4)}} - 1}{n - 1}\right). (C17) \\ \end{array}
$$

Inserting the expressions in Eqs. (C11) and (C14) into (C8) and rearranging gives the desired result (C3).

[1] P. D. D. Schwindt, P. G. Kwiat, and B. G. Englert, Quantitative wave-particle duality and nonerasing quantum erasure, Phys. Rev. A 60, 4285 (1999).  
[2] R. Bach, D. Pope, S.-H. Liou, and H. Batelaan, Controlled double-slit electron diffraction, New J. Phys. 15, 033018 (2013).  
[3] D. M. Greenberger and A. Yasin, Simultaneous wave and particle knowledge in a neutron interferometer, Phys. Lett. A 128, 391 (1988).

[4] M. Arndt et al., Wave-particle duality of C(60) molecules, Nature 401, 680 (1999).  
[5] M. O. Scully, B.-G. Englert, and H. Walther, Quantum optical tests of complementarity, Nature 351, 111 (1991).  
[6] N. Bohr, The quantum postulate and the recent development of atomic theory, Nature 121, 580 (1928).  
[7] B. Englert, Fringe Visibility and Which-Way Information: An Inequality, Phys. Rev. Lett. 77, 2154 (1996).

[8] G. Jaeger, A. Shimony, and L. Vaidman, Two interferometric complementarities, Phys. Rev. A 51, 54 (1995).  
[9] W. K. Wootters and W. H. Zurek, Complementarity in the double-slit experiment: Quantum nonseparability and a quantitative statement of Bohr's principle, Phys. Rev. D 19, 473 (1979).  
[10] B.-G. Englert and J. A. Bergou, Quantitative quantum erasure, Opt. Commun. 179, 337 (2000).  
[11] G. M. Bosyk, M. Portesi, F. Holik, and A. Plastino, On the connection between complementarity and uncertainty principles in the Mach-Zehnder interferometric setting, Phys. Scr. 87, 065002 (2013).  
[12] K. Banaszek, P. Horodecki, M. Karpinski, and C. Radzewicz, Quantum mechanical which-way experiment with an internal degree of freedom, Nat. Commun. 4, 2594 (2013).  
[13] L. Li, N. L. Liu, and S. Yu, Duality relations in a two-path interferometer with an asymmetric beam splitter, Phys. Rev. A 85, 054101 (2012).  
[14] T. Qureshi, Quantum twist to complementarity: A duality relation, Prog. Theoret. Exp. Phys. (2013) 041A01.  
[15] J.-H. Huang, S. Wölk, S.-Y. Zhu, and M. S. Zubairy, Higher-order wave-particle duality, Phys. Rev. A 87, 022107 (2013).  
[16] P. J. Coles, J. Kaniewski, and S. Wehner, Equivalence of wave-particle duality to entropic uncertainty, Nat. Commun. 5, 5814 (2014).  
[17] J. A. Vaccaro, Particle-wave duality: A dichotomy between symmetry and asymmetry, Proc. R. Soc. London A 468, 1065 (2012).  
[18] M. A. Siddiqui and T. Qureshi, Three-slit interference: A duality relation, Prog. Theoret. Exp. Phys. (2015) 083A02.  
[19] B.-G. Englert, D. Kaszlikowski, L. C. Kwek, and W. H. Chee, Wave-particle duality in multi-path interferometers: General concepts and three-path interferometers, Int. J. Quantum Inf. 06, 129 (2008).  
[20] S. Durr, Quantitative wave-particle duality in multibeam interferometers, Phys. Rev. A 64, 042113 (2001).  
[21] M. N. Bera, T. Qureshi, M. A. Siddiqui, and A. K. Pati, Duality of quantum coherence and path distinguishability, Phys. Rev. A 92, 012118 (2015).  
[22] E. Bagan, J. A. Bergou, S. S. Cottrell, and M. Hillary, Relations Between Coherence and Path Information, Phys. Rev. Lett. 116, 160406 (2016).

[23] T. Qureshi and M. A. Siddiqui, Wave-particle duality in  $n$ -path interference, arXiv:1605.02849.  
[24] P. Storey, S. Tan, M. Collett, and D. Walls, Path detection and the uncertainty principle, Nature 367, 626 (1994).  
[25] B.-G. Englert, M. O. Scully, and H. Walther, Complementarity and uncertainty, Nature 375, 367 (1995).  
[26] H. Wiseman and F. Harrison, Uncertainty over complementarity? Nature 377, 584 (1995).  
[27] G. Björk, J. Söderholm, and A. Trifonov, Complementarity and the uncertainty relations, Phys. Rev. A 60, 1874 (1999).  
[28] S. Durr and G. Rempe, Can wave-particle duality be based on the uncertainty relation? Am. J. Phys. 68, 1021 (2000).  
[29] P. Busch and C. Shilladay, Complementarity and uncertainty in Mach-Zehnder interferometry and beyond, Phys. Rep. 435, 1 (2006).  
[30] W. Heisenberg, Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik, Z. Phys. 43, 172 (1927).  
[31] P. J. Coles, M. Berta, M. Tomamichel, and S. Wehner, Entropic uncertainty relations and their applications, arXiv:1511.04857.  
[32] M. Tomamichel, C. Ci, W. Lim, N. Gisin, and R. Renner, Tight finite-key analysis for quantum cryptography, Nat. Commun. 3, 634 (2012).  
[33] R. Konig, R. Renner, and C. Schaffner, The operational meaning of min- and max-entropy, IEEE Trans. Inform. Theor. 55, 4337 (2009).  
[34] M. Tomamichel and R. Renner, Uncertainty Relation for Smooth Entropies, Phys. Rev. Lett. 106, 110506 (2011).  
[35] G. Bimonte and R. Musto, Comment on "Quantitative wave-particle duality in multibeam interferometers," Phys. Rev. A 67, 066101 (2003).  
[36] G. Bimonte and R. Musto, On interferometric duality in multibeam experiments, J. Phys. A: Math. Gen. 36, 11481 (2003).  
[37] M. Jakob and J. A. Bergou, Complementarity and entanglement in bipartite qudit systems, Phys. Rev. A 76, 052107 (2007).  
[38] H. Maassen and J. B. M. Uffink, Generalized Entropic Uncertainty Relations, Phys. Rev. Lett. 60, 1103 (1988).  
[39] J. M. Renes, Uncertainty relations and approximate quantum error correction, arXiv:1605.01420.  
[40] M. Tomamichel, A Framework for Non-Asymptotic Quantum Information Theory, Ph.D. thesis, ETH Zurich (2012).