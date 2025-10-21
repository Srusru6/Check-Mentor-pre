ARTICLE

Received 14 May 2014 | Accepted 11 Nov 2014 | Published 19 Dec 2014

DOI: 10.1038/ncomms6814

# Equivalence of wave-particle duality to entropic uncertainty

Patrick J. Coles<sup>1,2</sup>, Jedrzej Kaniewski<sup>1,3</sup> & Stephanie Wehner<sup>1,3</sup>

Interferometers capture a basic mystery of quantum mechanics: a single particle can exhibit wave behaviour, yet that wave behaviour disappears when one tries to determine the particle's path inside the interferometer. This idea has been formulated quantitatively as an inequality, for example, by Englert and Jaeger, Shimony and Vaidman, which upper bounds the sum of the interference visibility and the path distinguishability. Such wave-particle duality relations (WPDRs) are often thought to be conceptually inequivalent to Heisenberg's uncertainty principle, although this has been debated. Here we show that WPDRs correspond precisely to a modern formulation of the uncertainty principle in terms of entropies, namely, the min- and max-entropies. This observation unifies two fundamental concepts in quantum mechanics. Furthermore, it leads to a robust framework for deriving novel WPDRs by applying entropic uncertainty relations to interferometric models. As an illustration, we derive a novel relation that captures the coherence in a quantum beam splitter.

When Feynman discussed the two-path interferometer in his famous lectures<sup>1</sup>, he noted that quantum systems (quantons) display the behaviour of both waves and particles and that there is a sort of competition between seeing the wave behaviour versus the particle behaviour. That is, when the observer tries harder to figure out which path of the interferometer the quanton takes, the wave-like interference becomes less visible. This trade-off is commonly called wave-particle duality (WPD). Feynman further noted that this is 'a phenomenon which is impossible... to explain in any classical way, and which has in it the heart of quantum mechanics. In reality, it contains the only mystery [of quantum mechanics].'

Many quantitative statements of this idea, so-called WPD relations (WPDRs), have been formulated[2-13]. Such relations typically consider the Mach-Zehnder interferometer (MZI) for single photons, see Fig. 1. For example, a well-known formulation proven independently by Englert[2] and Jaeger et al.[3] quantifies the wave behaviour by fringe visibility,  $\mathcal{V}$ , and particle behaviour by the distinguishability of the photon's path,  $\mathcal{D}$ . (See below for precise definitions; the idea is that 'waves' have a definite phase, while 'particles' have a definite location, hence  $\mathcal{V}$  and  $\mathcal{D}$ , respectively, quantify how definite the phase and location are inside the interferometer.) They found the trade-off:

$$
\mathcal {D} ^ {2} + \mathcal {V} ^ {2} \leq 1 \tag {1}
$$

which implies  $\mathcal{V} = 0$  when  $\mathcal{D} = 1$  (full particle behaviour means no wave behaviour) and vice versa, and also treats the intermediate case of partial distinguishability.

It has been debated, particularly around the mid-1990s $^{14-16}$ , whether the WPD principle, closely related to Bohr's complementarity principle $^{17}$ , is equivalent to another fundamental quantum idea with no classical analogue: Heisenberg's uncertainty principle $^{18}$ . The latter states that there are certain pairs of observables, such as position and momentum or two orthogonal components of spin angular momentum, which cannot simultaneously be known or jointly measured. Likewise, there are many quantitative statements of this idea, known as uncertainty relations (URs; see, for example,

![](images/1820e21dbc99b766564489131d416b8efb53a082f1bf013f54fc522e913fc6ad.jpg)  
Figure 1 | MZI for single photons. Passing through the first beam splitter (BS) creates a superposition of which-path states,  $|0\rangle$  and  $|1\rangle$ , at time  $t_1$ , then the system interacts with an environment  $E = E_1E_2$ . Finally, at time  $t_2$ , a phase shift  $\phi$  is applied to the lower arm and the two beams are recombined on a second beam splitter. (While this is the typical setup, our framework also allows  $E$  to play a more general role, for example, being correlated to the photon before it enters the MZI.) Our complementary guessing game proceeds as follows. In one game (coloured red), Alice tries to guess which of the two paths the photon took given that she has access to a portion of  $E$  denoted  $E_1$ , which could be, for example, a gas of atoms whose internal states record information about the presence of a photon. In the other game (coloured blue), one of two phases,  $\phi = \phi_0$  or  $\phi = \phi_0 + \pi$ , is randomly applied to the lower interferometer arm and Alice tries to guess  $\phi$  given that she has access to a different portion of  $E$  denoted  $E_2$ , which could be, for example, the photon's polarization. We argue that WPDRs impose fundamental trade-offs on Alice's ability to win these two games.

refs 19-29), and modern formulations typically use entropy instead of s.d. as the uncertainty measure, so-called entropic uncertainty relations (EURs) $^{24}$ . This is because the s.d. formulation suffers from trivial bounds when applied to finite-dimensional systems $^{21}$ , whereas the entropic formulation not only fixes this weakness but also implies the s.d. relation $^{22}$  and has relevance to information-processing tasks.

At present, the debate regarding wave-particle duality and uncertainty remains unresolved, to our knowledge. Yet, Feynman's quote seems to suggest a belief that quantum mechanics has but one mystery and not two separate ones. In this article, we confirm this belief by showing a quantitative connection between URs and WPDRs, demonstrating that URs and WPDRs capture the same underlying physics; see also refs 30,31 for some partial progress along these lines. This may come as a surprise, since Englert<sup>2</sup> originally argued that equation (1) does not make use of Heisenberg's uncertainty relation in any form'. To be fair, the UR that we show is equivalent to equation (1) was not known at the time of Englert's paper, and was only recently discovered<sup>25-29</sup>. Specifically, we will consider EURs, where the particular entropies that are relevant to equation (1) are the so-called min- and max-entropies used in cryptography<sup>32</sup>.

In what follows, we provide a general framework for deriving and discussing WPDRs—a framework that is ultimately based on the entropic uncertainty principle. We illustrate our framework by showing that several different WPDRs from the literature are in fact particular examples of EURs. Making this connection not only unifies two fundamental concepts in quantum mechanics, but also implies that novel WPDRs can be derived simply by applying already-proven EURs. Indeed, we use our framework to derive a novel WPDR for an exotic scenario involving a 'quantum beam splitter'33-36, where testing our WPDR would allow the experimenter to verify the beam splitter's quantum coherence (see equation (17)).

We emphasize that the framework provided by EURs is highly robust and entropies have well-characterized statistical meanings. Note that current approaches to deriving WPDRs often involve brute force calculation of the quantities one aims to bound; there is no general, elegant method currently in use. Our approach simply involves judicial application of the relevant UR. Moreover, we emphasize that URs can be applied to interferometers in two different ways. One involves preparation uncertainty, which says that a quantum state cannot be prepared having low uncertainty for two complementary observables, and it turns out that this is the principle relevant to the original presentation of equation (1) in ref. 2. The other involves measurement uncertainty, which says that two complementary observables cannot be jointly measured[7,31], and we discuss why this principle is actually what was tested in some recent interferometry experiments[34,37].

# Results

**Framework.** We argue that a natural and powerful way to think of wave-particle duality is in terms of guessing games, and one's ability to win such games is quantified by entropic quantities. Specifically, we consider complementary guessing games, where Alice is asked to guess one of two complementary observables—a modern paradigm for discussing the uncertainty principle. In the MZI, see Fig. 1, this corresponds to either guessing which path the photon took or which phase was applied inside the interferometer. The which-path and which-phase observables are complementary and hence the uncertainty principle gives a fundamental restriction stating that Alice cannot be able to guess both observables.

Our framework treats this complementary guessing game for binary interferometers. By binary, we mean any interferometer where there are only two interfering paths, that is, all other paths

are classically distinguishable (from each other and from the two interfering paths). In addition to the MZI, this includes as special cases, for example, the Franson interferometer $^{38}$  (see Fig. 2) and the double-slit interferometer (see Fig. 3). Note that binary interferometers go beyond interferometers with two physical paths. For example, in the Franson interferometer, there are four possible paths but post-selecting on coincidence counts discards two of these paths, which are irrelevant to the interference anyway.

Now we link wave and particle behaviour to knowledge of complementary observables. In the case of particle behaviour, the intuition is that particles have a well-defined spatial location, hence 'particleteness' should be connected to knowledge of the path inside interferometer. For binary interferometers, there may be more than two physical paths, but only two of these are interfering. Hence, we only consider the two-dimensional (2D) subspace associated with the two which-path states of interest, denoted  $|0\rangle$  and  $|1\rangle$ . This subspace can be thought of as an effective qubit, denoted  $Q$ , and the standard basis of this qubit:

$$
\text {w h i c h p a t h}: \quad Z = \{\left| 0 \right\rangle , \left| 1 \right\rangle \} \tag {2}
$$

corresponds precisely to the which-path observable. For example, in the double slit (Fig. 3),  $|0\rangle$  and  $|1\rangle$  are the pure states that one would obtain at the slit exit from blocking the bottom and top slits, respectively.

Wave behaviour is traditionally associated with having a large amplitude of intensity oscillations at the interferometer output. Indeed, this has been quantified by the so-called fringe visibility,

![](images/ee25f276babf62be7f43f1316712fbd30f14bb7d7f704162ec3916d697139340.jpg)  
Figure 2 | Franson interferometer for entangled photons. In this interferometer, the 'quanton' consists of two photons. That is, a source produces time-energy entangled photons that each head separately towards a MZI that contains a long arm (depicted with extra loops) and a short arm. A simple model considers the 4D Hilbert space associated with the four possible paths:  $|SS\rangle$ ,  $|SL\rangle$ ,  $|LS\rangle$  and  $|LL\rangle$  with  $S =$  short path and  $L =$  long path. Two of these dimensions are post-selected away by considering only coincidence counts, that is, the photons arriving at the same time is inconsistent with the  $|SL\rangle$  and  $|LS\rangle$  paths. The remaining paths,  $|0\rangle = |SS\rangle$  and  $|1\rangle = |LL\rangle$ , are indistinguishable in the special case of perfect visibility and they produce interference fringes as one varies  $\phi = \phi_A + \phi_B$ . Namely, the intensity of coincidence counts at detector pair  $(D_0^A, D_0^B)$  oscillates with  $\phi$ . Interaction with an environment system, or making the beam splitters asymmetric, may allow one to partially distinguish between  $|SS\rangle$  and  $|LL\rangle$ , and our entropic uncertainty framework can be applied to derive a trade-off, for example, of the form of equation (1). This trade-off captures the idea that Alice can either guess which path ( $|SS\rangle$  versus  $|LL\rangle$ ) or which phase ( $\phi = \phi_0$  versus  $\phi = \phi_0 + \pi$ ), but she cannot do both (even if she extracts information from other systems  $E_1$  and  $E_2$ ).

see equation (7), but to apply the uncertainty principle we need to relate wave behaviour to an observable inside the interferometer. Classical waves (for example, water waves) are often modelled as having a well-defined phase and being spatially delocalized. The analogue in our context corresponds to the quantum being in a equally weighted superposition of which-path states. Hence, eigenstates of the 'wave observable' should live in the  $XY$  plane of the Bloch sphere, so we consider observables on qubit  $Q$  (the interfering subspace) of the form

$$
\text {w h i c h p h a s e :} \quad W = \left\{\left| w _ {\pm} \right\rangle \right\},
$$

$$
\left| w _ {\pm} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 \right\rangle \pm e ^ {i \phi_ {0}} \left| 1 \right\rangle\right). \tag {3}
$$

In terms of the guessing game, guessing the value of the wave (or which-phase) observable corresponds to guessing whether a phase of  $\phi = \phi_0$  or  $\phi = \phi_0 + \pi$  was applied inside the interferometer (see, for example, Fig. 1). While  $\phi_0$  is a generic phase, its precise value will be singled out by the particular experimental setup. When the experimenter measures fringe visibility, this corresponds to varying  $\phi_0$  to find the largest intensity contrast, and mathematically we model this by minimizing the uncertainty within the XY plane, see the second of equations (4).

Entropic view. Our entropic view associates a kind of behaviour with the availability of a kind of information, or lack of

![](images/7e52c68a515805192132823ce55927e56b739f4de94f239bd1b591bca103d411.jpg)  
Figure 3 | Double-slit interferometer for arbitrary quantum particles.

The first guessing game (coloured red) involves Alice guessing which slit the quanton goes through, given that she can measure a system  $E_{1}$  that has interacted with, and hence may contain information about, the quanton. In the second game (coloured blue), Bob randomly chooses the source's vertical coordinate, and Alice tries to guess where the source was located, given some other system  $E_{2}$  and given where the quanton was finally detected. Note that the source's location determines the relative phase between the which-slit states,  $|0\rangle$  and  $|1\rangle$ , and we assume that Bob chooses one of two possible locations such that the relative phase is either 0 or  $\pi$ . Here, the state  $|0\rangle$  ( $|1\rangle$ ) is defined as the pure state at the slit exit that one would obtain from blocking the bottom (top) slit. Our framework provides a WPDR that constrains Alice's ability to win these complementary games. Furthermore, one can reinterpret the probability to win the second game, for the case where  $E_{2}$  is trivial, in terms of the traditional fringe visibility. The latter quantifies the amplitude of intensity oscillations as one varies the detector location  $y$ . Note that varying  $y$  changes the relative path lengths from the slits to the detector and hence is analogous to applying a relative phase  $\phi$  between the two paths. (This assumes that the envelope function (dashed curve) associated with the interference pattern is flat over the range of  $y$  values considered, which is often the case when  $L$  is very large.) So, the double-slit fringe visibility is equivalent to the notion captured by  $\mathcal{V}$  in equation (7), where the detector is spatially fixed but a phase is varied, and we relate  $\mathcal{V}$  to our entropic measure of wave behaviour in the Methods section.

behaviour with missing information, as follows:

lack of particle behaviour:  $H_{\min}(Z|E_1)$

$$
\text {l a c k} \quad \min  _ {W \in X Y} H _ {\max } (W \mid E _ {2}) \tag {4}
$$

where  $H_{\mathrm{min}}$  and  $H_{\mathrm{max}}$  are the min- and max-entropies, defined below in equations (6), which are commonly used in quantum information theory,  $Z$  is the which-path observable in equation (2),  $W$  is the which-phase observable in equation (3) (whose uncertainty we optimize over the XY plane of the Bloch sphere) and  $E_1$  and  $E_2$  are some other quantum systems that contain information, and measuring these systems may help to reveal the behaviour (for example,  $E_1$  could be a which-path detector and  $E_2$  could be the quantum's internal degree of freedom). Note that we use the same symbols ( $Z$ ,  $W$  and so on) for the observables as for the random variables they give rise to. Full behaviour (no behaviour) of some kind corresponds to the associated entropy in equations (4) being zero (one). We formulate our general WPDR as

$$
H _ {\min } \left(Z \mid E _ {1}\right) + \min  _ {W \in X Y} H _ {\max } \left(W \mid E _ {2}\right) \geq 1. \tag {5}
$$

This states that, for a binary interferometer, the sum of the ignorances about the particle and wave behaviours is lower bounded by 1 (that is, 1 bit). Equation (5) constrains Alice's ability to win the complementary guessing game described above. If measuring  $E_{1}$  allows her to guess the quanton's path, that is, the min-entropy in the first of equations (4) is small, then, even if she measures  $E_{2}$ , she still will not be able to guess the quanton's phase, that is, the max-entropy in the second of equations (4) will be large (and vice versa).

To be clear, equation (5) is explicitly an EUR, and it has been exploited to prove the security of quantum cryptography $^{39}$ . The usefulness of equation (5) for cryptography is due to the clear operational meanings of the min- and max-entropies $^{32}$ , which naturally express the monogamy of correlations as they give the distances to being uncorrelated  $(H_{\mathrm{max}})$  and being perfectly correlated  $(H_{\mathrm{min}})$ . One can replace these entropies with the von Neumann entropy in equation (5) and the relation still holds; however, the min- and max-entropies give more refined statements about information processing since they are also applicable to finite numbers of experiments. From ref. 32, the precise definitions of these entropies, for a generic classical-quantum state  $\rho_{XB}$ , are

$$
H _ {\min } (X \mid B) = - \log p _ {\text {g u e s s}} (X \mid B),
$$

$$
H _ {\max } (X \mid B) = \log p _ {\operatorname {s e c r}} (X \mid B), \tag {6}
$$

where all logarithms are base 2 in this article. Here,  $p_{\mathrm{guess}}(X|B)$  denotes the probability for the experimenter to guess  $X$  correctly with the optimal strategy, that is, with the optimally helpful measurement on system  $B$ . Also,  $p_{\mathrm{secr}}(X|B) = \max_{\sigma_B} F(\rho_{XB}, \mathbb{1} \otimes \sigma_B)^2$  quantifies the secrecy of  $X$  from  $B$ , as measured by the fidelity  $F$  of  $\rho_{XB}$  to a state that is completely uncorrelated.

The fact that equation (5) can be thought of as a WPDR, and furthermore that it encompasses the majority of WPDRs found in the literature for binary interferometers, is our main result.

# Discussion

To illustrate this, we consider the celebrated MZI, shown in Fig. 1, since most literature WPDRs have been formulated for this interferometer. In the simplest case, one sends in a single photon towards a  $50/50$  (that is, symmetric) beam splitter,  $\mathrm{BS}_1$ , which results in the state  $| + \rangle = (|0\rangle + |1\rangle)/\sqrt{2}$ , then a phase  $\phi$  is applied to the lower arm giving the state  $(|0\rangle + e^{i\phi} |1\rangle)/\sqrt{2}$ . Finally, the two paths are recombined on a second  $50/50$  beam

splitter  $\mathrm{BS}_2$  and the output modes are detected by detectors  $D_0$  and  $D_{1}$ . Fringe visibility is then defined as

$$
\text {f r i n g e v i s i b i l i t y}: \mathcal {V} := \frac {p _ {\max } ^ {D _ {0}} - p _ {\min } ^ {D _ {0}}}{p _ {\max } ^ {D _ {0}} + p _ {\min } ^ {D _ {0}}}, \tag {7}
$$

where  $p^{D_0}$  is the probability for the photon to be detected at  $D_0$ ;  $p_{\max}^{D_0} = \max_{\phi} p^{D_0}$  maximizes this probability over  $\phi$ , whereas  $p_{\min}^{D_0} = \min_{\phi} p^{D_0}$ . In this trivial example, one has  $\mathcal{V} = 1$ . However, many more complicated situations, for which the analysis is more interesting, have been considered in the extensive literature; we now illustrate how these situations fall under the umbrella of our framework with some examples.

As a warm-up, we begin with the simplest known WPDR, the predictability-visibility trade-off. Predictability  $\mathcal{P}$  quantifies the prior knowledge, given the experimental setup, about which path the photon will take inside the interferometer. More precisely,  $\mathcal{P} = 2p_{\mathrm{guess}}(Z) - 1$ , where  $p_{\mathrm{guess}}(Z)$  is the probability of correctly guessing  $Z$ . Non-trivial predictability is typically obtained by choosing  $\mathrm{BS}_1$  to be asymmetric. In such situations, the following bound holds<sup>4,5</sup>:

$$
\mathcal {P} ^ {2} + \mathcal {V} ^ {2} \leq 1. \tag {8}
$$

This particularly simple example is a special case of Robertson's UR involving s.d.  $^{30,31,40,41}$ . However, ref. 41 argues that equation (8) is inequivalent to a family of EURs where the same (Renyi) entropy is used for both uncertainty terms, hence one gets the impression that entropic uncertainty is different from wave-particle duality. On the other hand, ref. 41 did not consider the EUR involving the min- and max-entropies. For some probability distribution  $P = \{p_j\}$ , the unconditional min- and max-entropies are given by  $H_{\min}(P) = -\log \max_j p_j$  and  $H_{\max}(P) = 2\log \sum \sqrt{p_j}$ . We find that equation (8) is equivalent to

$$
{ } ^ { j } H _ { \operatorname* { m i n } } ( Z ) + \min  _ { W \in X Y } H _ { \operatorname* { m a x } } ( W ) \geq 1 , \tag {9}
$$

which is an EUR proved in the seminal paper by Maassen and Uffink $^{23}$ , and corresponds to  $E_{1}$  and  $E_{2}$  in equation (5) being trivial. The entropies in equation (9) are evaluated for the state at any time while the photon is inside the interferometer. It is straightforward to see that  $H_{\mathrm{min}}(Z) = -\log \frac{1 + \mathcal{P}}{2}$  and in Methods we prove that

$$
\min  _ {W \in X Y} H _ {\max } (W) = \log \left(1 + \sqrt {1 - \mathcal {V} ^ {2}}\right). \tag {10}
$$

Plugging these relations into equation (9) gives equation (8).

Let us move on to a more general and more interesting scenario where, in addition to prior which-path knowledge, one may obtain further knowledge during the experiment due to the interaction of the photon with some environment  $F$ , which may act as a which-way detector. Most generally, the interaction is given by a completely positive trace preserving map  $\mathcal{E}$ , with the input system being  $Q$  at time  $t_1$  and output systems being  $Q$  and  $F$  at time  $t_2$ , see Fig. 1. The final state is  $\rho_{QF}^{(2)} = \mathcal{E}(\rho_Q^{(1)})$ , where the superscripts (1) and (2) indicate the states at times  $t_1$  and  $t_2$ . We do not require  $\mathcal{E}$  to have any special form to derive our WPDR, so our treatment is general.

The path distinguishability is defined by  $\mathcal{D} = 2p_{\mathrm{guess}}(Z|F) - 1$  where  $p_{\mathrm{guess}}(Z|F)$  is the probability for correctly guessing the photon's path  $Z$  at time  $t_2$  given that the experimenter performs the optimally helpful measurement on  $F$ . We find that equation (1) is equivalent to

$$
H _ {\min } (Z \mid F) + \min  _ {W \in X Y} H _ {\max } (W) \geq 1, \tag {11}
$$

where the entropy terms are evaluated for the state  $\rho_{OP}^{(2)}$ , which corresponds to  $E_1 = F$  and  $E_2$  being trivial in equation (5). First, it is obvious from the operational meaning of the conditional min

entropy in the first of equations (6) that we have  $H_{\min}(Z|F) = -\log \frac{1 + \mathcal{D}}{2}$ , and second we use our result equation (10) to rewrite equation (11) as equation (1). As emphasized in ref. 2, we note that equation (1) and its entropic form equation (11) do not require  $\mathrm{BS}_1$  to be symmetric. Hence,  $\mathcal{D}$  accounts for both the prior  $Z$  knowledge associated with the asymmetry of  $\mathrm{BS}_1$  as well as the  $Z$  information gained from  $F$ .

The above analysis shows that equations (1) and (8) correspond to applying the preparation UR at time  $t_2$  (just before the photon reaches  $\mathrm{BS}_2$ ). Preparation uncertainty restricts one's ability to predict the outcomes of future measurements of complementary observables. Thus, to experimentally measure  $\mathcal{P}$  or more generally  $\mathcal{D}$ , the experimenter removes  $\mathrm{BS}_2$  and sees how well he/she can guess which detector clicks, see Fig. 4a. Of course, to then measure  $\mathcal{V}$ , the experimenter reinserts  $\mathrm{BS}_2$  to close the interferometer. We emphasize that this procedure falls into the general framework of preparation uncertainty.

On the other hand, URs can be applied in a conceptually different way. Instead of two complementary output measurements and a fixed input state, consider a fixed output measurement and two complementary sets of input states. Namely, consider the input ensembles from equations (2) and (3), now labelled as  $Z_{i} = \{|0\rangle ,|1\rangle \}$  and  $W_{i} = \{|w\pm \rangle \}$ , where  $i$  stands for 'input', to indicate the physical scenario of a sender inputting states into a channel. Imagine this as a retrodictive guessing game, where Bob controls the input and Alice has control over both  $F$  and the detectors. Bob chooses one of the ensembles and flips a coin to determine which state from the ensemble he will send, and Alice's goal is to guess Bob's coin flip outcome. Assuming  $\mathrm{BS}_1$  is 50/50, the two  $Z_{i}$  states are generated by Bob blocking the opposite arm of the interferometer, as in Fig. 4b, while the  $W_{i}$  states are generated by applying a phase (either  $\phi_0$  or  $\phi_0 + \pi$ ) to the lower arm.

It may not be common knowledge that this scenario leads to a different class of WPDRs, therefore we illustrate the difference in Fig. 4. For clarity, we refer to  $\mathcal{D}$  introduced above as output distinguishability, whereas in the present scenario we use the symbol  $\mathcal{D}_i$  and call this quantity input distinguishability, defined by

$$
\mathcal {D} _ {i} = 2 p _ {\text {g u e s s}} \left(Z _ {i} \mid F\right) _ {D _ {0}} - 1, \tag {12}
$$

![](images/105e438150817a95f9f0ccdbb3481598060cd2c898a7cf8c9f22da1ea0d7882e.jpg)

![](images/6a59565683a27120681c1186eb477a43abdc0ec6decaa4855d6e227a7e53d7d1.jpg)  
Figure 4 | Path prediction versus path retrodiction, in the MZI. (a) In the predictive scenario, the second beam splitter is removed and Alice tries to guess which detector will click. (b) In the retrodictive scenario, a blocker is randomly inserted into one of the interferometer arms and Alice tries to guess which arm was blocked (given the knowledge of which detector clicked).

where  $p_{\mathrm{guess}}(Z_i|F)_{D_0}$  is Alice's probability to correctly guess Bob's  $Z_i$  state given that she has access to  $F$  and she knows that detector  $D_0$  clicked at the output. Likewise, we define the notion of input visibility  $\mathcal{V}_i$  via:

$$
\mathcal {V} _ {i} = \max  _ {W \in X Y} \left[ 2 p _ {\text {g u e s s}} \left(W _ {i}\right) _ {D _ {0}} - 1 \right], \tag {13}
$$

which quantifies how well Alice can determine  $W_{i}$  given that she knows  $D_{0}$  clicked.

Now the uncertainty principle says there is a trade-off: if Alice can guess the  $Z_{i}$  states well, then she cannot guess the  $W_{i}$  states well and vice versa. In other words, Alice's measurement apparatus, the apparatus to the right of the dashed line labelled  $t_1$  in Fig. 1, cannot jointly measure Bob's  $Z$  and  $W$  observables. EURs involving von Neumann entropy have previously been applied to the joint measurement scenario[27,42], we do the same for the min- and max-entropies to obtain (see Methods for details)

$$
\mathcal {D} _ {i} ^ {2} + \mathcal {V} _ {i} ^ {2} \leq 1, \tag {14}
$$

which can now be applied to a variety of situations.

As an interesting application of equation (14), we consider the scenario proposed in ref. 33 and implemented in refs 34-36, where the photon's polarization  $P$  acts as a control system to determine whether or not  $\mathrm{BS}_2$  appears in the photon's path and hence whether the interferometer is open or closed, see Fig. 5. Since  $P$  can be prepared in an arbitrary input state  $\rho_P^{(2)}$ , such as a superposition, this effectively means that  $\mathrm{BS}_2$  is a 'quantum beam splitter', that is, it can be in a quantum superposition of being absent or present. The interaction coupling  $P$  to  $Q$  is modelled as a controlled unitary as in Fig. 5. In this case, the two visibilities are equivalent (see Methods)

$$
\mathcal {V} _ {i} = \mathcal {V} = 2 | \kappa | \sqrt {R (1 - R)} \langle V | \rho_ {P} ^ {(2)} | V \rangle , \tag {15}
$$

where we assume the dynamics are path preserving, that is,  $\mathcal{E}_Q(|0\rangle\langle 0|) = |0\rangle\langle 0|$  and  $\mathcal{E}_Q(|1\rangle\langle 1|) = |1\rangle\langle 1|$ , where  $\mathcal{E}_Q = \mathrm{Tr}_F \circ \mathcal{E}$  is the reduced channel on  $Q$ , which implies that  $\mathcal{E}_Q(|0\rangle\langle 1|) = \kappa |0\rangle\langle 1|$ , that is, off-diagonal elements get scaled

![](images/70d28908e55d4d3eea2aeb1a174895051750544dfffe07fb23599333a98c1425.jpg)

![](images/c9b2910ef56bede35cfc9ae4e96aa87df999ef954a82aa362a94c0cd3ddc6636.jpg)  
Figure 5 | Quantum beam splitter in the MZI. In this scenario, the second beam splitter is in a superposition of 'absent' and 'present', as determined by the polarization state  $\rho_{P}^{(2)}$  at time  $t_2$ . The quantum beam splitter (QBS) can be modelled as a controlled unitary,

$U_{PQ} = |H\rangle \langle H|_P\otimes \mathbb{1}_Q + |V\rangle \langle V|_P\otimes U(R)$ , where  $U(R)$  is the unitary on  $Q$  associated with an asymmetric beam splitter with reflection probability  $R$ . Polarization-resolving detectors (PBS = polarizing beam splitter) on the output modes help to reveal the 'quantumness' of the QBS.

by a complex number  $\kappa$  with  $|\kappa| \leq 1$ . In equation (15),  $\mathcal{V}$  is evaluated for any pure state input  $\rho_{Q}^{(1)}$  from the  $XY$  plane of the Bloch sphere (for example,  $|+\rangle$ ). Now we apply equation (14) to this scenario and use equation (15) to obtain:

$$
\mathcal {D} _ {i} ^ {2} + \mathcal {V} ^ {2} \leq 1, \tag {16}
$$

which extends a recent result in ref. 13 to the case where  $F$  is nontrivial. This general treatment includes the special case where  $\rho_{P}^{(2)} = |V\rangle \langle V|$ , corresponding to a closed interferometer with an asymmetric  $\mathrm{BS}_2$ . Ref. 37 experimentally tested this special case. However, ref. 37 did not remark that their experiment actually tested a relation different from equation (1), namely, they tested a special case of equation (16).

Similarly, ref. 34 tested equation (16) rather than equation (1), but they allowed  $\rho_{P}^{(2)}$  to be in a superposition. At first sight, this seems to test the WPDR in the case of a quantum beam splitter (QBS), but it turns out that neither the visibility  $\mathcal{V}$  nor the distinguishability  $\mathcal{D}_i$  depends on the phase coherence in  $\rho_P^{(2)}$  and hence the data could be simulated by a classical mixture of  $\mathrm{BS}_2$  being absent or present. Nevertheless, our framework provides a WPDR that captures the coherence in  $\rho_P^{(2)}$ , by conditioning on the polarization  $P$  at the interferometer output (see Methods). For example, defining the polarization-enhanced distinguishability,  $\mathcal{D}_i^P = 2p_{\mathrm{guess}}(Z_i|FP)_{D_0} - 1$ , which corresponds to choosing  $E_{1} = FP$ , we obtain the novel WPDR:

$$
\left(\mathcal {D} _ {i} ^ {p}\right) ^ {2} + \mathcal {V} ^ {2} \leq 1, \tag {17}
$$

which captures the beam splitter's coherence (see Supplementary Note 4 for elaboration) and could be tested with the set-up in ref. 34.

The above examples use the environment solely to enhance the particle behaviour. To give a corresponding example for wave behaviour, that is, where system  $E_{2}$  in equation (5) is non-trivial, the main result in ref. 11 is a WPDR for the case when the environment  $F$  is measured (after it has interacted with the quanton) and the resulting information is used to enhance the fringe visibility. This scenario is called quantum erasure, since the goal is to erase the which-path information stored in the environment to recover full visibility. This falls under our framework by taking  $E_{2}$  to be the classical output of the measurement on the environment. For elaboration, see Supplementary Note 3, where we also cast the main results of ref. 10 (Supplementary Note 2) and ref. 12 (Supplementary Note 3) within our framework.

In summary, we have unified the wave-particle duality principle and the entropic uncertainty principle, showing that WPDRs are EURs in disguise. We leave it for future work to extend this connection to multiple interference pathways<sup>6</sup>. The framework presented here can be applied universally to binary interferometers. Our framework makes it clear how to formulate novel WPDRs by simply applying known EURs to novel interferometer models, and these new WPDRs will likely inspire new interferometry experiments. We note that all of our relations also hold if one replaces both min- and max-entropies with the well-known von Neumann entropy. Alternatively, one can use smooth entropies<sup>29,39</sup>, and the resulting smooth WPDRs may find application in the security analysis of interferometric quantum key distribution<sup>43</sup>, which often exploits the Franson set-up (Fig. 2).

# Methods

Outline. We emphasize that our treatment, in what follows, will be for a generic binary interferometer. We will first discuss our general treatment, then we will specialize to the predictive and retrodictive scenarios (see Fig. 4).

Origin of general WPDR. It is known that the min- and max-entropies satisfy the UR<sup>29</sup>:

$$
H _ {\min } \left(Z \mid E _ {1}\right) + H _ {\max } \left(W \mid E _ {2}\right) \geq 1, \tag {18}
$$

for any tripartite state  $\rho_{AE_1E_2}$ , where  $A$  is a qubit and  $Z$  and  $W$  are mutually unbiased bases on  $A$ . Noting that the which-path and which-path observables in equations (2) and (3) are mutually unbiased (for all  $\phi_0$  in equation (3), that is, for all  $W$  in the  $XY$  plane) gives our general WPDR in equation (5).

Complementary guessing game. The operational interpretation of equation (5) in terms of the complementary guessing game described, for example, in Figs 1-3 can be seen clearly as follows. While the min-entropy is related to the guessing probability via the first of equations (6), we establish a similar relation for the max-entropy. First, we prove (see Supplementary Note 1) that for a general classical-quantum state  $\rho_{XB} = \sum |j\rangle \langle j|\otimes \sigma_B^j$ , where  $X$  is binary,

$$
H _ {\max } (X \mid B) = \log \left(1 + 2 \left\| \sqrt {\sigma_ {B} ^ {0}} \sqrt {\sigma_ {B} ^ {1}} \right\| _ {1}\right), \tag {19}
$$

where the 1-norm is  $\| M\| _1 = \mathrm{Tr}\sqrt{M^\dagger M}$ . Next we show (in Supplementary Note 1), for any positive semi-definite operators  $M$  and  $N$ ,

$$
\left\| M - N \right\| _ {1} ^ {2} + 4 \left\| \sqrt {M} \sqrt {N} \right\| _ {1} ^ {2} \leq (\operatorname {T r} M + \operatorname {T r} N) ^ {2}. \tag {20}
$$

Combining equation 20 with equation (19), and using the well-known formula  $\left\| \sigma_B^0 -\sigma_B^1\right\| _1 = 2p_{\mathrm{guess}}(X|B) - 1$  gives

$$
H _ {\max } (X \mid B) \leq \log \left(1 + \sqrt {1 - \left(2 p _ {\text {g u e s s}} (X \mid B) - 1\right) ^ {2}}\right). \tag {21}
$$

Now one can define generic measures of particle and wave behaviour directly in terms of the guessing probabilities:

$$
\mathcal {D} _ {g} = 2 p _ {\text {g u e s s}} \left(Z \mid E _ {1}\right) - 1, \tag {22}
$$

$$
\mathcal {V} _ {g} = \max  _ {W \in X Y} \left[ 2 p _ {\text {g u s s}} (W | E _ {2}) - 1 \right] \tag {23}
$$

for some arbitrary quantum systems  $E_{1}$  and  $E_{2}$ , and rearrange equation (5) into the traditional form for WPDRs:

$$
\mathcal {D} _ {g} ^ {2} + \mathcal {V} _ {g} ^ {2} \leq 1. \tag {24}
$$

This operationally motivated relation, which follows directly from equation (5), clearly imposes a restriction on Alice's ability to win the complementary guessing game, since  $\mathcal{D}_g$  and  $\mathcal{V}_g$  are defined in terms of the winning probabilities. Below we show that  $\mathcal{V}_g$  becomes the fringe visibility when  $E_2$  is discarded.

Predictive WPDRs. We now elaborate on our framework for deriving predictive WPDRs. Let us denote the quantum's spatial degree of freedom as  $S$ , which includes the previously mentioned  $Q$  as a subspace. At time  $t_2$  (see, for example, Fig. 1)—the time just before a phase  $\phi$  is applied and the interferometer is closed— $S$  and its environment  $E$  are in some state  $\rho_{SE}^{(2)}$ , where again  $E = E_1E_2$  is a generic bipartite system. The preparation is arbitrary, that is, we need not specify what happened at earlier times, such as what the system's state was at time  $t_1$  (before the interaction between  $S$  and  $E$ ). While in general a binary interferometer may have more than two paths, all but two of these are non-interfering (by definition), hence we only consider the 2D subspace associated with the two which-path states of interest, denoted  $|0\rangle$  and  $|1\rangle$ . This subspace, defined by the projector  $\Pi = |0\rangle \langle 0| + |1\rangle \langle 1|$ , can be thought of as an effective qubit system  $Q$ . (Note that  $Q = S$  in the MZI.) Without loss of generality, we project the state  $\rho_{SE}^{(2)}$  onto this subspace and denote the resulting (renormalized) state as

$$
\rho_ {Q E} ^ {(2)} = (\Pi \otimes \mathbb {1}) \rho_ {S E} ^ {(2)} (\Pi \otimes \mathbb {1}) / \operatorname {T r} \left(\Pi \rho_ {S} ^ {(2)}\right). \tag {25}
$$

Experimentally, this corresponds to post-selecting on the interfering portion of the data. To derive predictive WPDRs, we apply equation (5) to the state  $\rho_{QE}^{(2)}$  in equation (25), where we associate the subsystems  $E_{1}$  and  $E_{2}$  of  $E$  with the particle and wave terms, respectively.

For example, this approach gives the WPDRs discussed in ref. 2, equations (1) and (8). To show this, we must prove equation (10), which relates our entropic measure of wave behaviour in the second of equations (4) to fringe visibility, and we now do this for generic binary interferometers. We remark that one can take equation (7) as a generic definition for fringe visibility, where the label  $D_0$  is arbitrary, that is, it corresponds to some arbitrary detector. For generic binary interferometers, there is a phase shift  $\phi$  applied just after time  $t_2$ , as depicted in Fig. 1. Let  $U_{\phi} = |0\rangle \langle 0| + e^{i\phi}|1\rangle \langle 1|$  denote the unitary associated with this phase shift, and note that we only need to specify the action of  $U_{\phi}$  on the  $Q$  subspace since the state  $\rho_{OE}^{(2)}$  lives in this subspace.

Finally, the quanton is detected somewhere, that is, system  $S$  is measured and a detector  $D_0$  clicks. This measurement is a positive operator-valued measure (POVM)  $C = \{C_0, C_1, \ldots\}$  on the larger space, system  $S$  rather than the subspace  $Q$  (for example, think of the double-slit case, where the detection screen performs a position measurement on  $S$ ). We associate the POVM element  $C_0$  with the event of

detector  $D_0$  clicking. To prove equation (10), we need to restrict the form of  $C_0$ . We show that equation (10) holds so long as  $C_0$  is unbiased with respect to the which-path basis  $Z$  on the subspace  $Q$ . Fortunately, this condition is satisfied for all three types of interferometers in Figs 1, 2 and 3. More precisely, it is satisfied for the MZI provided  $\mathrm{BS}_2$  is 50/50, for the Franson case provided both  $\mathrm{BS}_2$  (the second beam splitters in Fig. 2) are 50/50 and for the double slit for some limiting choice of experimental parameters such as large  $L$  in Fig. 3. We now state a general lemma that applies to all of these interferometers.

Lemma 1: Consider a binary interferometer where  $\bar{C}_0 = \Pi C_0\Pi$  denotes the projection of POVM element  $C_0$  onto the interfering subspace  $(Q)$ . Suppose  $\bar{C}_0$  is proportional to a projector projecting onto a state from the  $XY$  plane of the Bloch sphere of  $Q$ , that is,

$$
\tilde {C} _ {0} = q \left| w _ {+} \right\rangle \left\langle w _ {+} \right| \tag {26}
$$

for some  $0 < q \leq 1$ , where  $|w_{+}\rangle$  is given by equation (3) for some arbitrary phase  $\phi_0$ , then it follows that

$$
\min  _ {W \in X Y} H _ {\max } (W) = \log \left(1 + \sqrt {1 - \mathcal {V} ^ {2}}\right), \tag {27}
$$

where  $\mathcal{V}$  is given by equation (7) and  $H_{\mathrm{max}}(W)$  is evaluated for the state  $\rho_Q^{(2)} = \mathrm{Tr}_E\Bigl (\rho_{QE}^{(2)}\Bigr)$ .

Proof: In what follows, it should be understood that probabilities and expectation values are evaluated for the state  $\rho_Q^{(2)}$ . Suppose that  $\bar{W}$  is optimal in the sense that  $\max_{W\in XY}\mathrm{Pr}(w_{+}) = \mathrm{Pr}(\tilde{w}_{+})$ , where  $\mathrm{Pr}(w_{\pm}) = \langle w_{\pm}|\rho_Q^{(2)}|w_{\pm}\rangle$ , then we have

$$
\min  _ {W \in X Y} H _ {\max } (W) = \log \left(1 + \sqrt {1 - \left\langle \sigma_ {\bar {W}} \right\rangle^ {2}}\right), \tag {28}
$$

where we denote Pauli operators by  $\sigma_{W} = |w_{+}\rangle \langle w_{+}| - |w_{-}\rangle \langle w_{-}|$  and  $\langle \sigma_{\tilde{W}}\rangle = \operatorname *{Pr}(\tilde{w}_{+}) - \operatorname *{Pr}(\tilde{w}_{-})$

The probability for  $D_0$  to click is

$$
p ^ {D _ {0}} = \operatorname {T r} \left(C _ {0} U _ {\phi} \rho_ {Q} ^ {(2)} U _ {\phi} ^ {\dagger}\right) = \operatorname {T r} \left(U _ {\phi} ^ {\dagger} \tilde {C} _ {0} U _ {\phi} \rho_ {Q} ^ {(2)}\right) \tag {29}
$$

and maximizing this over  $\phi$  gives

$$
p _ {\max } ^ {D _ {0}} = q \max  _ {W \in X Y} \Pr \left(w _ {+}\right) = q \Pr \left(\bar {w} _ {+}\right). \tag {30}
$$

Now, due to the geometry of the Bloch sphere, we have  $p_{\mathrm{min}}^{D_0} = \operatorname*{Pr}(\tilde{w}_-)$ . Thus,  $p_{\mathrm{max}}^{D_0} + p_{\mathrm{min}}^{D_0} = q$  and  $p_{\mathrm{max}}^{D_0} - p_{\mathrm{min}}^{D_0} = q\langle \sigma_{\tilde{W}}\rangle$ . This gives  $\mathcal{V} = \langle \sigma_{\tilde{W}}\rangle$ , completing the proof.

Retrodictive WPDRs. While we saw that the predictive approach allowed for any preparation but required complementary output measurements, the opposite is true in the retrodictive case, that is, the form of the output measurement is arbitrary while we require complementary preparations. The input ensembles  $Z_{i} = \{|0\rangle\}, |1\rangle \}$  and  $W_{i} = \{|w_{+}\rangle, |w_{-}\rangle \}$  can be generated by performing the relevant measurements on a reference qubit  $Q'$  that is initially entangled to the quanton  $S$ . Associating state ensembles with measurements on a reference system is a useful trick, for example, for deriving equation (14). Thus, at time  $t_1$  (just after the quanton enters the interferometer; see Fig. 1) we introduce a qubit  $Q'$  that is maximally entangled to the interfering subspace  $(Q)$  of  $S$ , denoted by the state  $\overline{\rho}_{QS}^{(1)} = |\Phi \rangle \langle \Phi |$  with  $|\Phi \rangle = (|00\rangle + |11\rangle) / \sqrt{2}$ . The dynamics after time  $t_1$  is modelled as a quantum operation  $\mathcal{A}$ , defined in ref. 44 as a completely positive, trace non-increasing map that maps  $S \rightarrow E_1E_2$ . The output of  $\mathcal{A}$  does not contain  $S$  because the quanton is eventually detected by a detector, at which point we no longer need a quantum description of the quanton's spatial degree of freedom; we only care where it was detected. The map  $\mathcal{A}$  corresponds to a particular detection event; for concreteness say that detector  $D_0$  clicking is the associated event. The probability for this event is the trace of the state after the action of  $\mathcal{A}$ , and renormalizing gives the final state

$$
\overline {{\rho}} _ {Q ^ {\prime} E _ {1} E _ {2}} ^ {D _ {0}} = \frac {(\mathcal {I} \otimes \mathcal {A}) (\bar {\rho} _ {Q S} ^ {(1)})}{\operatorname {T r} \left[ (\mathcal {I} \otimes \mathcal {A}) (\bar {\rho} _ {Q S} ^ {(1)}) \right]}. \tag {31}
$$

Our framework applies the UR equation (5) to the state  $\overline{\rho}_{Q'E_1E_2}^{D_0}$  to derive retrodictive WPDRs.

For example, this covers the scenario from the Discussion where  $\mathcal{A}$  involves two sequential steps. First,  $S$  interacts with an environment  $F$  inside the interferometer between times  $t_1$  and  $t_2$ , which corresponds to a channel  $\mathcal{E}$  mapping  $S$  to  $SF$ . Second, the quantum is detected at the interferometer output, say at detector  $D_0$ , modelled as a map  $\mathcal{B}(\cdot) = \mathrm{Tr}_S[C_0(\cdot)]$  acting on  $S$ , where  $C_0$  is the POVM element associated with detector  $D_0$  clicking. Hence, we choose  $\mathcal{A} = \mathcal{B} \circ \mathcal{E}$ . Applying equation (5) to this case while choosing  $E_1 = F$  and  $E_2$  to be trivial gives

$$
H _ {\min } (Z \mid F) _ {\tilde {\rho}} + \min  _ {W \in X Y} H _ {\max } (W) _ {\tilde {\rho}} \geq 1, \tag {32}
$$

where the subscript  $\bar{\rho}$  means evaluating on the state in equation (31). Note that measuring  $Z$  on system  $Q^{\prime}$  corresponds to sending the states  $\{|0\rangle, |1\rangle\}$  with equal probability through the interferometer, and similarly for  $W$  (with an inconsequential complication of taking the transpose of the  $W$  basis states). Realizing this, the first

and second terms in equation (32) map onto  $\mathcal{D}_i$  and  $\mathcal{V}_i$ , respectively:

$$
H _ {\min } (Z \mid F) _ {\bar {p}} = 1 - \log (1 + \mathcal {D} _ {i}), \tag {33}
$$

$$
\min  _ {W \in X Y} H _ {\max } (W) _ {\bar {\rho}} = \log \left(1 + \sqrt {1 - \mathcal {V} _ {i} ^ {2}}\right). \tag {34}
$$

Hence, equation (32) becomes equation (14).

It remains to show that  $\mathcal{V}_i$  appearing in equation (14) can be replaced by  $\mathcal{V}$  for many cases of interest, such as the QBS case. We do this in the following lemma, where the proof is given in Supplementary Note 2 and is similar to the proof of Lemma 1.

Lemma 2: Consider any binary interferometer with an unbiased input, that is, where the state at time  $t_1$  is unbiased with respect to the which-path basis (of the form  $|\psi_Q^{(1)}\rangle = (|0\rangle +e^{i\phi}|1\rangle) / \sqrt{2}$ ). Let  $\mathcal{E}_S = \mathrm{Tr}_F\circ \mathcal{E}$  be the channel describing the quantum's interaction with  $F$  inside the interferometer and let  $\mathcal{G}(\cdot) = \Pi (\cdot)\Pi$  be the map that projects onto the subspace II. Suppose  $\mathcal{E}_S$  is path preserving, that is,  $\mathcal{E}_S(|0\rangle \langle 0|) = |0\rangle \langle 0|$  and  $\mathcal{E}_S(|1\rangle \langle 1|) = |1\rangle \langle 1|$ , and furthermore suppose  $\mathcal{E}_S$  commutes with  $\mathcal{G}$ , then

$$
\min  _ {W \in X Y} H _ {\max } (W) _ {\bar {\rho}} = \log \left(1 + \sqrt {1 - \mathcal {V} ^ {2}}\right), \tag {35}
$$

where  $H_{\mathrm{max}}(W)$  is evaluated for the state  $\bar{\rho}_{Q^{\prime}}^{D_0}$ .

QBS example. Finally, we treat the QBS shown in Fig. 5. (Note that  $S = Q$  in the MZI.) This set-up involves first a quantum channel  $\mathcal{E}$  that describes the interaction of  $S$  with an environment  $F$  between times  $t_1$  and  $t_2$ , followed by another channel associated with the QBS that allows interaction of  $S$  with the polarization  $P$ , followed by a post-selected detection at  $D_0$ . Together, these three steps form a quantum operation  $\mathcal{A}$  that maps  $S \rightarrow FP$ , and hence this falls under our retroductive framework.

To prove equation (17), we apply equation (5) to the state in equation (31) while choosing  $E_{1} = FP$  and  $E_{2}$  to be trivial, giving

$$
H _ {\min } (Z \mid F P) _ {\bar {\rho}} + \max  _ {W \in X Y} H _ {\max } (W) _ {\bar {\rho}} \geq 1. \tag {36}
$$

We then use relations analogous to those in equations (33) and (34), where the former relation now involves conditioning also on the polarization  $P$ . Finally, we note that Lemma 2 applies to the QBS case.

# References

1. Feynman, R. P. Feynman Lectures on Physics (Addison Wesley, 1970).  
2. Englert, B.-G. Fringe visibility and which-way information: an inequality. Phys. Rev. Lett. 77, 2154-2157 (1996).  
3. Jaeger, G., Shimony, A. & Vaidman, L. Two interferometric complementarities. Phys. Rev. A 51, 54-67 (1995).  
4. Wootters, W. K. & Zurek, W. H. Complementarity in the double-slit experiment: quantum nonseparability and a quantitative statement of bohr's principle. Phys. Rev. D 19, 473-484 (1979).  
5. Greenberger, D. M. & Yasin, A. Simultaneous wave and particle knowledge in a neutron interferometer. Phys. Lett. A 128, 391-394 (1988).  
6. Englert, B.-G., Kaszlikowski, D., Kwek, L. C. & Chee, W. H. Wave-particle duality in multi-path interferometers: general concepts and three-path interferometers. Int. J. Quant. Info. 06, 129-157 (2008).  
7. Liu, N.-L., Li, L., Yu, S. & Chen, Z.-B. Duality relation and joint measurement in a Mach-Zehnder interferometer. Phys. Rev. A 79, 052108 (2009).  
8. Huang, J.-H., Wolk, S., Zhu, S.-Y. & Zubairy, M. S. Higher-order wave-particle duality. Phys. Rev. A 87, 022107 (2013).  
9. Qureshi, T. Quantum twist to complementarity: a duality relation. Prog. Theor. Exp. Phys. 2013, 041A01 (2013).  
10. Li, L., Liu, N.-L. & Yu, S. Duality relations in a two-path interferometer with an asymmetric beam splitter. Phys. Rev. A 85, 054101 (2012).  
11. Englert, B.-G. & Bergou, J. A. Quantitative quantum erasure. Opt. Commun. 179, 337-355 (2000).  
12. Banaszek, K., Horodecki, P., Karpinski, M. & Radzewicz, C. Quantum mechanical which-way experiment with an internal degree of freedom. Nat. Commun. 4, 2594 (2013).  
13. Jia, A.-A., Huang, J.-H., Feng, W., Zhang, T.-C. & Zhu, S.-Y. Duality of a single particle with an n-dimensional internal degree of freedom. Chin. Phys. B 23, 30307-30314 (2014).  
14. Englert, B.-G., Scully, M. O. & Walther, H. Complementarity and uncertainty. Nature 375, 367-368 (1995).  
15. Storey, P., Tan, S., Collett, M. & Walls, D. Path detection and the uncertainty principle. Nature 367, 626-628 (1994).  
16. Wiseman, H. & Harrison, F. Uncertainty over complementarity? Nature 377, 584-584 (1995).  
17. Bohr, N. The quantum postulate and the recent development of atomic theory. Nature 121, 580-590 (1928).  
18. Heisenberg, W. Über den anschaulichen Inhalt der quantentheoretischen Kinematik und Mechanik. Z. Phys. 43, 172-198 (1927).

19. Kennard, E. The quantum mechanics of simple types of motion. Z. Phys. 44, 326-352 (1927).  
20. Robertson, H. P. The uncertainty principle. Phys. Rev. 34, 163-164 (1929).  
21. Deutsch, D. Uncertainty in quantum measurements. Phys. Rev. Lett. 50, 631-633 (1983).  
22. Bialynicki-Birula, I. & Mycielski, J. Uncertainty relations for information entropy in wave mechanics. Commun. Math. Phys. 44, 129-132 (1975).  
23. Maassen, H. & Uffink, J. B. M. Generalized entropic uncertainty relations. Phys. Rev. Lett. 60, 1103-1106 (1988).  
24. Wehner, S. & Winter, A. Entropic uncertainty relations - a survey. New J. Phys. 12, 025009 (2010).  
25. Renes, J. M. & Boileau, J.-C. Conjectured strong complementary information tradeoff. Phys. Rev. Lett. 103, 020402 (2009).  
26. Berta, M., Christandl, M., Colbeck, R., Renes, J. M. & Renner, R. The uncertainty principle in the presence of quantum memory. Nat. Phys. 6, 659-662 (2010).  
27. Coles, P. J., Yu, L., Gheorghiu, V. & Griffiths, R. B. Information-theoretic treatment of tripartite systems and quantum channels. Phys. Rev. A 83, 062338 (2011).  
28. Coles, P. J., Colbeck, R., Yu, L. & Zwolak, M. Uncertainty relations from simple entropic properties. Phys. Rev. Lett. 108, 210405 (2012).  
29. Tomamichel, M. & Renner, R. Uncertainty relation for smooth entropies. Phys. Rev. Lett. 106, 110506 (2011).  
30. Durr, S. & Rempe, G. Can wave-particle duality be based on the uncertainty relation? Am. J. Phys. 68, 1021-1024 (2000).  
31. Busch, P. & Shilladay, C. Complementarity and uncertainty in Mach-Zehnder interferometry and beyond. Phys. Rep. 435, 1-31 (2006).  
32. Konig, R., Renner, R. & Schaffner, C. The operational meaning of min- and max-entropy. IEEE Trans. Inf. Theory 55, 4337-4347 (2009).  
33. Ionicioiu, R. & Terno, D. R. Proposal for a quantum delayed-choice experiment. Phys. Rev. Lett. 107, 230406 (2011).  
34. Kaiser, F., Coudreau, T., Milman, P., Ostrowsky, D. B. & Tanzilli, S. Entanglement-enabled delayed-choice experiment. Science 338, 637-640 (2012).  
35. Peruzzo, A., Shadbolt, P., Brunner, N., Popescu, S. & O'Brien, J. L. A quantum delayed-choice experiment. Science 338, 634-637 (2012).  
36. Tang, J.-S., Li, Y.-L., Li, C.-F. & Guo, G.-C. Revisiting Bohr's principle of complementarity with a quantum device. Phys. Rev. A 88, 014103 (2013).  
37. Jacques, V. et al. Delayed-choice test of quantum complementarity with interfering single photons. Phys. Rev. Lett. 100, 220402 (2008).  
38. Franson, J. D. Bell inequality for position and time. Phys. Rev. Lett. 62, 2205-2208 (1989).

39. Tomamichel, M., Lim, C. C. W., Gisin, N. & Renner, R. Tight finite-key analysis for quantum cryptography. Nat. Commun. 3, 634 (2012).  
40. Björk, G., Söderholm, J., Trifonov, A., Tsegaye, T. & Karlsson, A. Complementarity and the uncertainty relations. Phys. Rev. A 60, 1874-1882 (1999).  
41. Bosyk, G. M., Portesi, M., Holik, F. & Plastino, A. On the connection between complementarity and uncertainty principles in the Mach-Zehnder interferometric setting. Phys. Scr. 87, 065002 (2013).  
42. Buscemi, F., Hall, M. J. W., Ozawa, M. & Wilde, M. M. Noise and disturbance in quantum measurements: an information-theoretic approach. Phys. Rev. Lett. 112, 050401 (2014).  
43. Ekert, A. K., Rarity, J. G., Tapster, P. R. & Massimo Palma, G. Practical quantum cryptography based on two-photon interferometry. Phys. Rev. Lett. 69, 1293-1295 (1992).  
44. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information 5th edn (Cambridge Univ. Press, 2000).

# Acknowledgements

We thank B. Englert and S. Tanzilli for helpful correspondence, and acknowledge helpful discussions with M. Woods, M. Tomamichel, C.J. Kwong and L.C. Kwek. We acknowledge funding from the Ministry of Education (MOE) and National Research Foundation Singapore, as well as MOE Tier 3 Grant 'Random numbers from quantum processes' (MOE2012-T3-1-009).

# Author contributions

The main results were developed by all authors. In addition, the following contributions were made P.J.C. conceived the project, analysed the literature and wrote most of the manuscript. J.K. prepared the figures and wrote parts of the Supplementary Information. S.W. provided feedback and revisions.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Coles, P. J. et al. Equivalence of wave-particle duality to entropic uncertainty. Nat. Commun. 5:5814 doi: 10.1038/ncomms6814 (2014).