# Proposal for a Quantum Delayed-Choice Experiment

Radu Ionicioiu $^{1,2,3}$  and Daniel R. Terno $^{4,5}$

<sup>1</sup>Centre for Quantum Science and Technology, Macquarie University, Sydney New South Wales 2109, Australia

$^{2}$ Institute for Quantum Computing, University of Waterloo, Waterloo, Ontario N2L 3G1, Canada

$^{3}$ Department of Applied Mathematics, University of Waterloo, Waterloo, Ontario N2L 3G1, Canada

$^{4}$ Department of Physics & Astronomy, Macquarie University, Sydney New South Wales 2109, Australia

$^{5}$ Centre for Quantum Technologies, National University of Singapore, Singapore 117543

(Received 29 March 2011; published 2 December 2011)

Gedanken experiments help to reconcile our classical intuition with quantum mechanics and nowadays are routinely performed in the laboratory. An important open question is the quantum behavior of the controlling devices in such experiments. We propose a framework to analyze quantum-controlled experiments and illustrate it by discussing a quantum version of Wheeler's delayed-choice experiment. Using a quantum control has several consequences. First, it enables us to measure complementary phenomena with a single experimental setup, pointing to a redefinition of complementarity principle. Second, it allows us to prove there are no consistent hidden-variable theories having "particle" and "wave" as realistic properties. Finally, it shows that a photon can have a morphing behavior between particle and wave. The framework can be extended to other experiments (e.g., Bell inequality).

DOI: 10.1103/PhysRevLett.107.230406

PACS numbers: 03.65.Ta, 03.65.Ud, 03.67.-a

Wave-particle duality, a quintessential property of quantum systems, defies our classical intuition. In the context of the double-slit experiment, duality played a central role in the famous Bohr—Einstein debate and prompted Bohr to formulate the complementarity principle [1]: "the study of complementary phenomena demands mutually exclusive experimental arrangements." Classical concepts like particle or wave (as in "wave-particle duality") do not translate perfectly into the quantum language. For example, although we observe interference (a definite wavelike behavior), the pattern is produced click-by-click, in a discrete, particlelike manner [2]. Notwithstanding this ambiguity, and with this proviso, we adopt as operational definition of "wave" or "particle" to stand for "ability" or "inability" to produce interference [3].

A good illustration of wave-particle complementarity is given by a Mach-Zehnder interferometer (MZI), Fig. 1. A photon is first split by beam splitter  $\mathrm{BS}_1$ , travels inside an interferometer with a tunable phase shifter  $\varphi$ , and is finally recombined (or not) at a second beam splitter  $\mathrm{BS}_2$  before detection. If the second beam splitter is present we observe interference fringes, indicating the photon behaved as a wave, traveling both arms of the MZI. If  $\mathrm{BS}_2$  is absent, we randomly register, with probability  $\frac{1}{2}$ , a click in only one of the two detectors, concluding that the photon travelled along a single arm, showing particle properties.

This contradictory behavior prompted Wheeler to formulate the delayed-choice experiment [4-8]. In Wheeler's delayed-choice experiment one randomly chooses whether or not to insert the second beam splitter when the photon is already inside the interferometer and before it reaches  $\mathrm{BS}_2$  [Fig. 1(a)]. The rationale behind the delayed choice is to avoid a possible causal link between the experimental

setup and photon's behavior: the photon should not "know" beforehand if it has to behave like a particle or like a wave. The choice of inserting or removing  $\mathrm{BS}_2$  is classically controlled by a random number generator.

In this article we examine what happens if we replace this classical control with a quantum device. This enables us to extend Wheeler's gedanken experiment to a quantum delayed choice. Quantum elements in various experimental

![](images/3ff1c5e3ea570eaefe0f229f8626e9da348de8846caedc197196434996f25c5c.jpg)  
(c)

![](images/f04f6b86763b6f412a0e3d4064c82662d55544599f3fa7224c64e50cf3786a18.jpg)

![](images/c548caf68564924fe79b0186e48391311ab871e68c8a76c612e59172db2980de.jpg)  
FIG. 1 (color online). (a) In the classical delayed-choice experiment the second beam splitter is inserted or removed randomly after the photon is already inside the interferometer. (b) The equivalent quantum network. An ancilla (red line), initially prepared in the state  $| + \rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$  then measured, acts as a quantum random number generator (QRNG). (c) Delayed choice with a quantum beam splitter. The classical control (red double line) after the measurement of the ancilla in (b) is equivalent to a quantum control before the measurement; the second beam splitter  $\mathrm{BS}_2$  is now in superposition of present and absent, equivalent to a controlled-Hadamard  $C(H)$  gate. (d) We bias the QRNG by preparing the ancilla in an arbitrary state  $\cos \alpha |0\rangle + \sin \alpha |1\rangle$ .

![](images/f25e26a5414e36ec6824496898f3a662decd9ce42f9e72a1dcd0b51104affb03.jpg)  
(d)

set ups were proposed in the past [9]. In order to understand the transition from a classical to a quantum controlling element it is insightful to reframe the delayed-choice experiment in terms of quantum networks [10,11]. A quantum network model enables us to analyze the gedanken experiment at a higher level of abstraction and to understand the information flow between different subsystems. The delayed-choice experiment is equivalent to the quantum network in Fig. 1(b), where Hadamard gates  $H$  play the role of beam splitters; we call the top (black) line the photon and the bottom (red) line the ancilla. The quantum random number generator is modeled by an ancilla prepared in the equal-superposition state  $|+ \rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ , then measured; the result of this measurement (0 or 1) controls if  $\mathrm{BS}_2$  is inserted or not. The classical control after the measurement of the ancilla in Fig. 1(b) is equivalent to a quantum control before the measurement of the ancilla, Fig. 1(c). This seemingly innocuous observation radically changes the setup and has two profound implications. First, since now we have a quantum beam splitter in superposition of being present or absent, the interferometer is in a superposition of being closed or open. Following Wheeler's interpretation of the experiment [5], this forces the photon to be in a superposition of particle and wave at the same time.

Second, and more important, a quantum control allows us to reverse the temporal order of the measurements. We can now detect the photon before the ancilla, i.e., before choosing if the interferometer is open or closed. This implies that we can choose if the photon behaves as a particle or as a wave after it has been already detected (postselection). Consequently, this avoids the experimentally demanding requirement of an ultrafast switch necessary in the classical delayed-choice experiment [8]. A quantum control thus allows us to explore a regime outside the classical realm: in any classically controlled experiment the choice of inserting or not the second beam splitter has to be made before the photon is detected. Since the photon and the ancilla interact at the  $C(H)$  gate, the ancilla is always prepared before the photon reaches  $\mathrm{BS}_2$ .

In Fig. 1(c), the photon-ancilla system starts in the state  $|00\rangle$  and at the end of the network the final state is

$$
| \psi \rangle = \frac {1}{\sqrt {2}} (| \text {p a r t i c l e} \rangle | 0 \rangle + | \text {w a v e} \rangle | 1 \rangle), \tag {1}
$$

where the wave functions  $|\mathrm{particle}\rangle = \frac{1}{\sqrt{2}} (|0\rangle +e^{i\varphi}|1\rangle)$  and  $|\mathrm{wave}\rangle = e^{i\varphi /2}(\cos \frac{\varphi}{2} |0\rangle -i\sin \frac{\varphi}{2} |1\rangle)$  describe particle and wave behavior, respectively. The two states are in general not orthogonal  $\langle \mathrm{particle}|\mathrm{wave}\rangle = \frac{1}{\sqrt{2}}\cos \varphi$  , except for  $\varphi = \pm \pi /2$  Equation (1) implies that if the ancilla is measured to be  $|0\rangle (|1\rangle)$  , the interferometer is open (closed) and the photon behaves like a particle (wave). The interference pattern measured by the photon detector  $D_0$  is  $I_0(\varphi) = \mathrm{Tr}(\rho_1|0\rangle \langle 0|)$  with  $\rho_{1} = \mathrm{Tr}_{2}|\psi \rangle \langle \psi | =$

$\frac{1}{2}(|\mathrm{particle}\rangle \langle \mathrm{particle}| + |\mathrm{wave}\rangle \langle \mathrm{wave}|)$  the reduced density matrix of the photon. The visibility of the interference pattern is  $\mathcal{V} = (I_{\mathrm{max}} - I_{\mathrm{min}}) / (I_{\mathrm{max}} + I_{\mathrm{min}})$ , where the min/max values are calculated with respect to  $\varphi$ . If the interferometer is closed, the photon shows a wavelike behavior with  $I_w(\varphi) = \cos^2\frac{\varphi}{2}$  and visibility  $\mathcal{V} = 1$ . For an open interferometer the photon behaves like a particle and  $I_p(\varphi) = \frac{1}{2}$ , resulting in  $\mathcal{V} = 0$ . For the entangled state (1) the result is

$$
I _ {0} (\varphi) = \frac {1}{2} \left[ I _ {p} (\varphi) + I _ {w} (\varphi) \right] = \frac {1}{2} + \frac {1}{4} \cos \varphi . \tag {2}
$$

Without correlating the photon data with the ancilla we observe an interference pattern with reduced visibility  $\mathcal{V} = \frac{1}{2}$ : the photon has a mixed behavior between a particle and a wave. On the other hand, if we do correlate the photon with the ancilla we observe either a perfect wave-like behavior (ancilla  $|1\rangle$ ) or a particlelike one (ancilla  $|0\rangle$ ). Contrary to Bohr's opinion, we do not have to change the experimental setup in order to measure complementary properties—we can measure both properties in a single experiment, provided that a component of the apparatus is a quantum object in a superposition state. The behavior is postselected by the experimenter after the photon has been detected, by correlating the data with the appropriate value of the ancilla [12].

The photon in state  $|\psi \rangle$  exhibits both wave and particle behavior with equal probability. It is insightful to generalize this result to an arbitrary superposition. We achieve this by preparing the ancilla in the state  $\cos \alpha |0\rangle +\sin \alpha |1\rangle$  before interacting with the photon [Fig. 1(d)]. In the classical setup [Fig. 1(a)] this choice corresponds to a biased random number generator which outputs 0 with probability  $\cos^2\alpha$ . The final state becomes

$$
\left| \psi^ {\prime} \right\rangle = \cos \alpha | \text {p a r t i c l e} \rangle | 0 \rangle + \sin \alpha | \text {w a v e} \rangle | 1 \rangle \tag {3}
$$

and the photon detector  $D_0$  now measures

$$
I _ {0} (\varphi , \alpha) = I _ {p} (\varphi) \cos^ {2} \alpha + I _ {w} (\varphi) \sin^ {2} \alpha \tag {4}
$$

with the corresponding visibility  $\mathcal{V} = \sin^2\alpha$ . Thus, by varying  $\alpha$  we have the ability to modify continuously the interference pattern—we have a morphing behavior between a particle at  $\alpha = 0$  and a wave at  $\alpha = \pi /2$  (Fig. 2).

This continuously varying behavior (morphing) raises questions about the classical picture of a photon as either a particle or a wave. A quantum beam splitter transcends the "particle-or-wave" dichotomy and enables preparation of the photon in a superposition of both. For example, by measuring the ancilla controlling the beam splitter in the  $|\pm \rangle$  basis, the photon state becomes  $\cos \alpha |\mathrm{particle}\rangle \pm$ $\sin \alpha |\mathrm{wave}\rangle$ , a superposition without a classical analog.

The introduction of a quantum control (i.e., quantum beam splitter) allows us to answer an important question: Can a hidden-variable (HV) theory, in which particle and wave are realistic properties, explain the delayed-choice experiment? Such a model should satisfy two conditions:

![](images/d32c1545a9e8a9d9dcf67b1126c4cfd12996a7c633a63f1ec266a6869009a593.jpg)  
FIG. 2 (color online). Morphing behavior between particle  $(\alpha = 0)$  and wave  $(\alpha = \pi /2)$

(i) it should reproduce the quantum mechanical (QM) statistics, and (ii) for a given photon the property of being a particle or a wave is intrinsic, i.e., does not change during its lifetime. The second condition is very important, since it selects from the existing HV theories [13] reproducing the QM statistics those models having meaningful notions of particle and wave. Moreover, a quantum control potentially introduces new routes for causal influence, making the HV analysis [13] more subtle. In the basis  $a\otimes b =$  00, 01, 10, 11) the statistics for the joint measurements of the photon  $a$  and ancilla  $b$  in the state (3) is

$$
p (a, b) = \left(\frac {1}{2} \cos^ {2} \alpha , \sin^ {2} \alpha \cos^ {2} \frac {\varphi}{2}, \frac {1}{2} \cos^ {2} \alpha , \sin^ {2} \alpha \sin^ {2} \frac {\varphi}{2}\right). \tag {5}
$$

We show that there is no satisfactory HV model reproducing the statistics  $p(a, b)$  and in which particle and waves are realistic properties. One can assume that the source randomly emits, with some probability, particle- or wave-like photons. However, in order to have the statistics  $p(a, b)$  these "photons" show an inconsistent behavior: in an open interferometer waves obey a particle statistics and in a closed interferometer particles behave like waves, showing interference. Consequently, the properties wave and particle become meaningless.

Proof: We assume the photon has an extra degree of freedom  $\lambda$  (the hidden variable) corresponding to a particlelike  $(\lambda = \mathsf{p})$  or a wavelike  $(\lambda = \mathsf{w})$  behavior. We also assume the standard conditions for probability distributions; for all variables  $i, j$  we have: (i)  $p(i) = \sum_{j} p(i, j)$  (marginals) and (ii)  $p(i, j) = p(i|j)p(j) = p(j|i)p(i)$  (conditionals).

In this HV model the probability distribution  $p(a, b)$  is the marginal of a distribution involving the hidden-variable  $\lambda$ , namely  $p(a, b) = \sum_{\lambda} p(a, b, \lambda)$ , with  $p(a, b, \lambda)$  unknown. We decompose this probability as  $p(a, b, \lambda) = p(a | b, \lambda) p(b | \lambda) p(\lambda)$ , by replacing the seven parameters

$p(a, b, \lambda)$  with another seven functions (the probabilities in the right-hand side have four, two and, respectively, one free parameter). This decomposition is appealing as the new functions are physically intuitive, unlike  $p(a, b, \lambda)$ . Thus we have

$$
p (a, b) = \sum_ {\lambda} p (a | b, \lambda) p (b | \lambda) p (\lambda). \tag {6}
$$

Two of the conditional distributions  $p(a|b, \lambda)$  are constrained by the expectation of how particles (waves) behave in open (closed) interferometers. Consistent with our previous definition, a particle in an open interferometer  $(b = 0)$  has the statistics

$$
p (a \mid b = 0, \lambda = \mathfrak {p}) = (\frac {1}{2}, \frac {1}{2}), \tag {7}
$$

whereas a wave in a closed MZI  $(b = 1)$  shows interference,

$$
p (a \mid b = 1, \lambda = w) = \left(\cos^ {2} \frac {\varphi}{2}, \sin^ {2} \frac {\varphi}{2}\right). \tag {8}
$$

The other two conditional probabilities specify the behavior of a wave  $(\lambda = \mathsf{w})$  in an open  $(b = 0)$  interferometer and of a particle  $(\lambda = \mathsf{p})$  in a closed  $(b = 1)$  one. We denote these two unknown distributions by  $x$  and  $y$ , respectively

$$
p (a \mid b = 0, \lambda = \mathsf {w}) = (x, 1 - x),
$$

$$
p (a \mid b = 1, \lambda = \mathfrak {p}) = (y, 1 - y).
$$

The probability distribution of the ancilla  $p(b)$  is obtained from Eq. (5) as the marginal of  $p(a, b)$

$$
p (b) = \left(\cos^ {2} \alpha , \sin^ {2} \alpha\right). \tag {9}
$$

By freely choosing  $\alpha$  at the preparation stage we modify  $p(b)$ , a fact which will prove crucial later.

For  $\lambda$  we assume that the source randomly emits particle- or wavelike photons with probability  $f$  and  $1 - f$ , respectively:

$$
p (\lambda) = (f, 1 - f).
$$

The remaining two variables are the conditional probability distributions of the ancilla  $b$  and the hidden variable  $\lambda$ :

$$
p (b | \lambda = \mathsf {p}) = (z, 1 - z), \qquad p (b | \lambda = \mathsf {w}) = (\nu , 1 - \nu),
$$

satisfying the consistency condition  $p(b) = \sum_{\lambda} p(b|\lambda)p(\lambda)$ . From Eqs. (5) and (6) with the constraints (7) and (8) we obtain

$$
v (1 - f) \left(x - \frac {1}{2}\right) = 0, \tag {10}
$$

$$
f (1 - z) \left(y - \cos^ {2} \frac {\varphi}{2}\right) = 0, \tag {11}
$$

$$
z f + v (1 - f) - \cos^ {2} \alpha = 0. \tag {12}
$$

As  $\alpha$  is arbitrary, we disregard the cases  $\nu = 0$ ,  $f = 0$ , implying  $\cos^2\alpha = 0$  and  $f = 1$ ,  $z = 1$ , giving  $\cos^2\alpha = 1$ .

Five of the remaining nontrivial solutions have either  $x = \frac{1}{2}$  or  $y = \cos^2\frac{\varphi}{2}$  (or both). The solution  $x = \frac{1}{2}$  means that waves in open interferometers have a particle statistics,  $p(a|b = 0, \lambda = \mathsf{w}) = (\frac{1}{2}, \frac{1}{2})$ . The second solution  $y = \cos^2\frac{\varphi}{2}$  implies that particles in closed interferometers behave like waves,  $p(a|b = 1, \lambda = \mathsf{p}) = (\cos^2\frac{\varphi}{2}, \sin^2\frac{\varphi}{2})$ . None of these solutions is acceptable, as particles and waves show an inconsistent behavior: waves in open interferometers have particle statistics and particles in closed interferometers show interference. The last solution is

$$
\nu = 0, \quad z = 1, \quad f = \cos^ {2} \alpha , \tag {13}
$$

with  $x, y$  undetermined. In other words, the source randomly emits particles and waves with a distribution  $p(\lambda) = (\cos^2\alpha, \sin^2\alpha)$  identical to the probability distribution  $p(b)$  of the ancilla. Moreover, whenever the source emits a particlelike photon the ancilla is found to be 0,  $p(b|\lambda = \mathfrak{p}) = (1,0)$  and the interferometer is open. On the other hand, when it emits a wavelike photon the ancilla is measured as 1,  $p(b|\lambda = \mathsf{w}) = (0,1)$ , so the interferometer is closed. The hidden-variable  $\lambda$  and the ancilla  $b$  are perfectly correlated,  $p(b|\lambda) = \delta_{\lambda \mathsf{p}}\delta_{b0} + \delta_{\lambda \mathsf{w}}\delta_{b1}$ .

The paradox is now revealed: although the hidden variable completely determines the value of the ancilla, the probability distribution  $p(\lambda)$  is identical to  $p(b)$  which is set by the experimenter preparing  $\alpha$ . To explain this, we need to enlarge the HV theory in order to include also the setting  $\alpha$ , resulting in a second-order HV theory (deemed unacceptable by Bell [14]). This invites an induction ad infinitum procedure, in which we introduce a second (and third, etc.) ancilla in order to offset the causality between the source and the preparation of the lower-order ancilla. In this scenario we have a delayed-delayed...-choice experiment all the way down. Occam's razor compels us to cut this infinite chain to the first link. In conclusion, if the hidden-variable  $\lambda$  completely determines  $b$ , then  $\lambda$  itself cannot be determined by the setting  $\alpha$  preparing  $b$ .

To summarize, we have shown that any HV theory that reproduces the QM statistics  $p(a,b)$  and agrees with natural definitions of particle and wave behavior, either assumes wave-particle duality (which was supposed to abolish in the first place) or introduces higher-order HV theories.

The definition of particle (wave) used above is based on the observed statistics in a open (closed) interferometer (7) and (8), as this is the only meaningful possibility in a probabilistic theory as QM. As noted before, from a classical perspective there is still an ontological tension between the observed interference and the detection of individual photons, one by one, by clicks in the detectors.

In conclusion, we proposed and analyzed a quantum version of Wheeler's delayed-choice experiment. This has several important consequences. First, the photon

shows a morphing behavior between particle and wave. This further supports the conclusion that particle and wave are not realistic properties but merely reflect how we look at the photon; such behavior is a direct consequence of a quantum beam splitter and cannot be revealed in a classical setup. Second, the classical choice particle vs wave can be made after the photon has been already detected, by correlating the photon data with the measured value of the ancilla (postselection). We have shown that complementary phenomena can be observed with a single experimental setup, provided that a component of the apparatus is a quantum device in a superposition state. Our result suggests a reinterpretation of the complementarity principle—instead of complementarity of experimental setups (Bohr's view) we have complementarity of experimental data. We anticipate quantum controls will play an important role in reassessing other experiments in foundations of quantum mechanics, particularly Bell-inequality tests [15,16].

Discussing the delayed-choice experiment, Wheeler concludes: "In this sense, we have a strange inversion of the normal order of time. We, now, by moving the mirror in or out have an unavoidable effect on what we have a right to say about the already past history of that photon" [5]. We disagree with this interpretation. There is no inversion of the normal order of time—in our case we measure the photon before the ancilla deciding the experimental setup (open or closed interferometer). It is only after we interpret the photon data, by correlating them with the results of the ancilla, that either a particlelike or wavelike behavior emerges: behaviour is in the eye of the observer.

We thank R. Colbeck, A. Leggett, G. Milburn, A. Peruzzo, H. Price, S. Rebić, T. Rudolph, and J. Twamley for comments and discussions. This work was supported by the ARC Centre for Quantum Computer Technology and EC Project QUANTIP 244026.

[1] N. Bohr, in Quantum Theory and Measurement, edited by J.A. Wheeler and W.H. Zurek (Princeton University Press, Princeton, NJ, 1984), pp. 9-49.  
[2] P. Grangier, G. Roger, and A. Aspect, Europhys. Lett. 1, 173 (1986).  
[3] G. Greenstein and A.G. Zajonc, The Quantum Challenge: Modern Research on the Foundations of Quantum Mechanics (Jones and Bartlett, Boston, 1997), Chap. 2.  
[4] J.A. Wheeler, in Mathematical Foundations of Quantum Mechanics, edited by A.R. Marlow (Academic, New York, 1978), pp. 9-48.  
[5] J.A. Wheeler, in Quantum Theory and Measurement, edited by J.A. Wheeler and W.H. Zurek (Princeton University Press, Princeton, NJ, 1984), pp. 182-213.  
[6] A.J. Leggett, in Compendium of Quantum Physics, edited by D. Greenberger, K. Hentschel, and F. Weinert (Springer, Berlin, 2009), pp. 161-166.  
[7] B.-G. Englert, Phys. Rev. Lett. 77, 2154 (1996).  
[8] V. Jacques et al., Science 315, 966 (2007).

[9] W. Marshall, C. Simon, R. Penrose, and D. Bouwmeester, Phys. Rev. Lett. 91, 130401 (2003); D. Kleckner et al., New J. Phys. 10, 095020 (2008); J. Eisert et al., Phys. Rev. Lett. 93, 190402 (2004); A. Bassi, E. Ippoliti, and S.L. Adler, Phys. Rev. Lett. 94, 030401 (2005); T. Rocheleau et al., Nature (London) 463, 72 (2010).  
[10] A. Barenco, D. Deutsch, A. Ekert, and R. Jozsa, Phys. Rev. Lett. 74, 4083 (1995).  
[11] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, U.K., 2000).  
[12] Y.-H. Kim et al., Phys. Rev. Lett. 84, 1 (2000); T.J. Herzog et al., Phys. Rev. Lett. 75, 3034 (1995).

[13] A. Brandenburger and N. Yanofsky, J. Phys. A 41, 425302 (2008); B. J. Hiley, in Compendium of Quantum Physics, edited by D. Greenberger, K. Hentschel, and F. Weinert (Springer, Berlin, 2009), pp. 284-287.  
[14] J.S. Bell, Speakable and Unspeakable in Quantum Mechanics (Cambridge University Press, Cambridge, 1987), p. 154.  
[15] J.S. Bell, Physics 1, 195 (1964); J.F. Clauser, M.A. Horne, A. Shimony, and R.A. Holt, Phys. Rev. Lett. 23, 880 (1969); A. Peres, Found. Phys. 29, 589 (1999).  
[16] A. Aspect, J. Dalibard, and G. Roger, Phys. Rev. Lett. 49, 1804 (1982); M. D. Reid et al., Rev. Mod. Phys. 81, 1727 (2009).