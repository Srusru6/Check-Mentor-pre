rspa.royalsocietypublishing.org

![](images/ef672db281ffc062abc4bb31a7583e34674df8081c9d47ab813b22428f344668.jpg)

Check for updates

# Research

Cite this article: Biswas T, Garcia Diaz M, Winter A. 2017 Interferometric visibility and coherence. Proc. R. Soc. A 473: 20170170. http://dx.doi.org/10.1098/rspa.2017.0170

Received: 10 March 2017

Accepted: 23 June 2017

# Subject Areas:

quantum physics

# Keywords:

quantum coherence, interferometer, visibility

# Author for correspondence:

Andreas Winter

e-mail: andreas.winter@uab.cat

# Interferometric visibility and coherence

Tanmoy Biswas<sup>1</sup>, María García Díaz<sup>2</sup> and

Andreas Winter2,3

$^{1}$ Department of Physical Sciences, IISER Kolkata, Mohanpur 741246, West Bengal, India  
$^{2}$ Departament de Física: Grup d'Informação Quántica, Universitat Autònoma de Barcelona, 08193 Bellaterra (Barcelona), Spain  
$^{3}$ ICREA—Institución Catalana de Recerca i Estudis Avançats, Pg. Lluis Companys, 23, 08001 Barcelona, Spain

ID AW,0000-0001-6344-4870

Recently, the basic concept of quantum coherence (or superposition) has gained a lot of renewed attention, after Baumgratz et al. (Phys. Rev. Lett. 113, 140401. (doi:10.1103/PhysRevLett.113.140401)), following Åberg (http://arxiv.org/abs/quant-ph/0612146), have proposed a resource theoretic approach to quantify it. This has resulted in a large number of papers and preprints exploring various coherence monotones, and debating possible forms for the resource theory. Here, we take the view that the operational foundation of coherence in a state, be it quantum or otherwise wave mechanical, lies in the observation of interference effects. Our approach here is to consider an idealized multi-path interferometer, with a suitable detector, in such a way that the visibility of the interference pattern provides a quantitative expression of the amount of coherence in a given probe state. We present a general framework of deriving coherence measures from visibility, and demonstrate it by analysing several concrete visibility parameters, recovering some known coherence measures and obtaining some new ones.

# 1. Introduction

The physics of constructive and destructive interference of waves, along with the concept of coherence, has been well understood since the nineteenth century. With the advent of quantum mechanics, these studies have assumed a fundamental quality as in quantum theory the superposition principle applies to everything, and the presence of quantum coherence is the basic

hallmark of departure from classical physics. Recently, Baumgratz et al. [1], following Åberg's earlier work [2], have launched a flurry of new activity on coherence by attempting to cast it as a resource theory and introducing a number of tasks and monotones [3,4].

It has, however, remained largely unclear what this resource of 'coherence' is about and how it relates to theories of asymmetry, among others [4]. To make contact with the operational foundations of coherence, we go back to its very definition, the observability of an interference pattern in a suitable experiment. Our present approach is to consider an idealized multi-path interferometer, which receives the state  $\rho$  under consideration at the input. The experimenter is at liberty to put phase plates into each of the paths, and to construct a detector (a general beam splitter with detection of the output beams). The interference pattern, i.e. the response of the fixed detector as a function of the multiple phases, is the signature of coherence: the more it fluctuates, intuitively, the more coherent is the state. The degree of fluctuation, aka visibility, quantifies the strength of interference.

The idea in this paper is that coherence is the potential of a state to yield visible fringes in a suitable experiment. Hence, we propose to optimize the visibility over all possible detectors, to obtain a measure of coherence of the original state. Indeed, we prove that, under mild assumptions, every visibility parameter yields a coherence measure in this way, strongly monotonic under a certain class of incoherence-preserving operations. We illustrate our theory with concrete examples of visibility parameters.

# 2. Interferometers and visibility

Consider a multi-path interferometer, in which a single particle can be in one of  $d$  paths, denoting the spatial variable by orthogonal vectors  $|j\rangle$ ,  $j = 1,\dots,d$ , spanning a  $d$ -dimensional Hilbert space  $\mathcal{H}$ . For the moment, we will ignore any internal degrees of freedom of the particle, and any other spatial degrees, so that the entire Hilbert space describing the system is  $\mathcal{H}$ , and a pure state inside the interferometer can be written as  $|\psi \rangle = \sum_{j}c_{j}|j\rangle$ , and a general mixed state as

$$
\rho = \sum_ {j, k = 1} ^ {d} \rho_ {j k} | j \rangle \langle k |. \tag {2.1}
$$

An interferometric experiment (figure 1) has two distinct components. The first consists of local phase shifts  $\alpha_{j}$  that can be inserted into the paths, implementing a diagonal phase unitary

$$
U (\boldsymbol {\alpha}) = \sum_ {j} \mathrm {e} ^ {\mathrm {i} \alpha_ {j}} | j \rangle \langle j |, \tag {2.2}
$$

so that the state becomes

$$
\rho (\boldsymbol {\alpha}) = U (\boldsymbol {\alpha}) \rho U (\boldsymbol {\alpha}) ^ {\dagger} = \sum_ {j, k = 1} ^ {d} \mathrm {e} ^ {\mathrm {i} \left(\alpha_ {j} - \alpha_ {k}\right)} \rho_ {j k} | j \rangle \langle k |. \tag {2.3}
$$

The second is a detector at the output, often simply fixed as the combination of a symmetric beam splitter with a path measurement, but for us a general POVM  $M = (M_{\omega})$ , with outcomes  $\omega$  from a suitable space  $\Omega$ .

The experimenter, having chosen  $\alpha = (\alpha_{1},\ldots ,\alpha_{d})$ , will observe outcomes  $\omega \in \Omega$  sampled from the Born distribution (the 'interference pattern'):

$$
P _ {M | \rho} (\omega | \alpha) = \operatorname {T r} U (\alpha) \rho U (\alpha) ^ {\dagger} M _ {\omega}. \tag {2.4}
$$

The signature of interference in such an experiment, where  $\rho$  is given and fixed, is that the distribution  $P = P_{M|\rho}$  can vary as a function of the phases  $\alpha_{j}$ . The degree of variability, intuitively, is the visibility of the interference pattern, calling for a visibility functional  $V = V[P]$  on conditional distributions  $P(\omega \mid \alpha)$ .

![](images/34b1ac3539e4a8c3a77e3ef47927e2b57dcca191b5a9c9771e14056903e2af7e.jpg)  
Figure 1. Schematic of a multi-path interferometer: on the left, the input state  $\rho$  (in green), representing the state of a particle on  $d$  paths. Each path can be subjected to a local relative phase  $\alpha_{j}$  (in magenta), after which the particle is detected via a suitable measurement (in violet) that produces an outcome  $\omega$  (in red). (Online version in colour.)

![](images/434074b791edc2b4c2597eac096a4cfb00e69d2c3dcb21640ec5a79188ef2e3d.jpg)  
Figure 2. Mach-Zehnder two-path interferometer. The initial state is  $\rho_0$ , while the state after the interaction with the first beam splitter  $(BS_{1})$  and the first mirror  $(M_{1})$  is  $\rho$  (in green), representing the state of a particle on two paths. Each path can be subjected to a phase  $\alpha_{1}$  and  $\alpha_{2}$ , although only their relative difference  $\alpha = \alpha_{1} - \alpha_{2}$  is physically relevant. After the interaction with the second beam splitter  $(BS_{2})$ , the interference pattern is observed. (Online version in colour.)

While it is always dangerous to make a priori demands, we take it that such a functional has to capture the global property of  $P$  not being constant; i.e. it should be 0 for constant  $P(\cdot |\alpha)$  and positive otherwise. It will also make sense to ask that it is invariant under permutations and shifts of the  $\alpha$ , reflecting the obvious symmetries of the experimental set-up (figure 1). We call a visibility functional  $V[P]$  satisfying these requirements regular. In the discussion of interferometers, specifically in the rich literature on the complementarity between fringe visibility and which-path information [5-9], to cite only the principal ones, the topic of visibility has been addressed repeatedly, and from increasingly general perspectives. In particular, the realization that, for  $d > 2$ , no unique visibility functional seems to exist called for an axiomatic approach to put order into the many ad hoc parameters (cf. [10-12]). We wish to highlight especially Coles' paper [13], which makes an eloquent case for an operational approach, where visibility (as well as which-path information) is expressed as a property of an observable probability distribution, and with which philosophy we feel very much in line.

In the simplest case of the well-known Mach-Zehnder interferometer (figure 2), i.e.  $d = 2$ , we observe interference fringes w.r.t. a relative phase shift: consider the density matrix  $\rho = \rho_{11}|1\rangle\langle 1| + \rho_{22}|2\rangle\langle 2| + \rho_{12}|1\rangle\langle 2| + \rho_{21}|2\rangle\langle 1|$ , the diagonal phase unitary  $U(\alpha) = \mathrm{e}^{\mathrm{i}\alpha_1}|1\rangle\langle 1| + \mathrm{e}^{\mathrm{i}\alpha_2}|2\rangle\langle 2|$ , and a measurement with POVM elements  $|\mu\rangle\langle \mu|$ ,  $|\mu\rangle = \mu_1|1\rangle + \mu_2|2\rangle$ . Now, with  $\alpha = \alpha_1 - \alpha_2$ , and writing  $\rho_{12} = |\rho_{12}|\mathrm{e}^{\mathrm{i}\beta}$ ,  $\bar{\mu}_1\mu_2 = |\mu_1\mu_2|\mathrm{e}^{\mathrm{i}\gamma}$ , the output probability is

$$
P _ {M | \rho} (\mu | \alpha) = \rho_ {1 1} | \mu_ {1} | ^ {2} + \rho_ {2 2} | \mu_ {2} | ^ {2} + 2 | \rho_ {1 2} \mu_ {1} \mu_ {2} | \cos (\alpha + \beta + \gamma), \tag {2.5}
$$

whose fluctuation is essentially characterized by the coefficient  $|\rho_{12}\mu_1\mu_2|$ , and so most analyses conclude this to be the visibility.

# 3. Optimal visibility as a measure of coherence

If we want to treat the state  $\rho$  as a resource, i.e. as a given, of which we are supposed to make the best, it makes sense to optimize the visibility  $V[P_{M|\rho}]$  over all possible measurements. This idea diverges somewhat from laboratory practice in interferometry and from many discussions of visibility versus which-path information duality, where a fixed measurement is used, usually one mixing the paths uniformly (a 50-50 beam splitter in the Mach-Zehnder case, and more generally a transformation acting as a Fourier transform, followed by a channel detector) [7,11,14,15].

However, it is clear that the most beautiful coherent superposition in the state may be rendered invisible by an unsuitable choice of measurements. For instance, consider the qutrit state  $\rho = \frac{1}{3} (|1\rangle + |2\rangle)(|1\rangle + |2\rangle) + \frac{1}{3} |3\rangle \langle 3|$ , under a measurement  $M^{(0)}$  in the basis  $\{|1\rangle, (1 / \sqrt{2})(|2\rangle \pm |3\rangle)\}$ ; evidently, the three outcomes all have probability  $\frac{1}{3}$ , irrespective of the phases in

$$
\rho (\alpha) = \frac {1}{3} (| 1 \rangle + \mathrm {e} ^ {\mathrm {i} \alpha} | 2 \rangle) (\langle 1 | + \mathrm {e} ^ {- \mathrm {i} \alpha} \langle 2 |) + \frac {1}{3} | 3 \rangle \langle 3 |.
$$

Intuitively, we expect the best choice to bring out the coherence in  $\rho$  to be the projective measurement  $M^{(1)}$  in the basis  $\{(1 / \sqrt{2})(|1\rangle \pm |2\rangle),|3\rangle \}$ , for which the detection probabilities are  $(\frac{2}{3}\cos^2 (\alpha /2),\frac{2}{3}\sin^2 (\alpha /2),\frac{1}{3})$ . On the other hand, the standard choice of a symmetric beam splitter results in the Fourier basis  $\{(1 / \sqrt{3})(|1\rangle +\zeta^t |2\rangle +\zeta^{2t}|3\rangle):t = 0,1,2\}$ , where  $\zeta = \mathrm{e}^{2\pi \mathrm{i} / 3}$ , with detection probabilities

$$
\left(\frac {1}{9} + \frac {4}{9} \cos^ {2} \left(\frac {\alpha}{2} - \frac {t \pi}{3}\right): t = 0, 1, 2\right),
$$

which has the same oscillation pattern as  $M^{(1)}$ , but smaller amplitude.

Thus, we are motivated, given a visibility functional  $V[P]$ , to optimize the visibility over all measurements, to get the best out of  $\rho$ . This leads to a number that now depends only on the state,

$$
C _ {V} (\rho) := \sup  _ {M = \left(M _ {\omega}\right)} V \left[ P _ {M | \rho} \right]. \tag {3.1}
$$

The hypothesis that we will explore in the rest of the paper is that this number, for a large class of visibility functionals, is a good indicator of coherence in  $\rho$ .

In an attempt to identify consistent quantifiers of coherent superposition, Baumgratz et al. [1], following Åberg [2], have created a resource theory of coherence, with carefully chosen resource free state (diagonal density operators  $\Delta$ ) and free transformations (the so-called incoherent operations (IO)). A measure that is non-increasing under these operations is called a monotone. Mathematically, incoherent operations are completely positive and trace-preserving linear maps, built from incoherent Kraus operators,  $T(\rho) = \sum_{\lambda} K_{\lambda} \rho K_{\lambda}^{\dagger}$ , where  $K_{\lambda}|j\rangle \propto |k\rangle = |k(\lambda,j)\rangle$  for all computational basis elements  $|j\rangle$ . If both  $K_{\lambda}$  and  $K_{\lambda}^{\dagger}$  are incoherent, it is called strictly incoherent (SIO), and so is a map  $T$  built from strictly incoherent Kraus operators. From this, it is straightforward to see that a Kraus operator is incoherent if and only if it has the form  $K = \sum_{j} c_{j}|k(j)\rangle \langle j|$  with a function  $k(j)$  mapping basis states to basis states; it is strictly incoherent if and only if  $k$  is one-to-one.

A functional  $C(\rho) \geq 0$  is a monotone if  $C(\rho) \geq C(T(\rho))$  under all IO (SIO)  $T$ . It is called a strong monotone if, for an incoherent Kraus decomposition,  $K_{\lambda} \rho K_{\lambda}^{\dagger} \eqqcolon q_{\lambda} \rho_{\lambda}$ ,  $C(\rho) \geq \sum_{\lambda} q_{\lambda} C(\rho_{\lambda})$ . Well-known examples include the  $\ell_1$ -measure of coherence [1], and the relative entropy of coherence [1,2,16]:

$$
C _ {\ell_ {1}} (\rho) = \sum_ {j \neq k} | \rho_ {j k} | \tag {3.2}
$$

and

$$
C _ {r} (\rho) = \min  _ {\sigma \in \Delta} D (\rho \| \sigma) = S (\Delta (\rho)) - S (\rho), \tag {3.3}
$$

with the relative entropy  $D(\rho \parallel \sigma) = \mathrm{Tr}\rho (\log \rho -\log \sigma)$  and the von Neumann entropy  $S(\rho) = -\mathrm{Tr}\rho \log \rho ;\Delta (\rho) = \sum_{j}|j\rangle \langle j|\rho |j\rangle \langle j|$  is the diagonal part of  $\rho$ .

Our first result is a general link between visibility and coherence. We call a visibility functional weakly affine if, for distributions  $P_{i}(\omega \mid \alpha)$ ,  $\omega \in \Omega_{i}$  (assuming w.l.o.g. pairwise disjoint  $\Omega_{i}$ ), and for a probability distribution  $(q_{i})$ , we have  $V[\bar{P}] = \sum_{i} q_{i} V[P_{i}]$ , with the averaged distribution  $\bar{P} = \sum_{i} q_{i} P_{i}$  on  $\Omega = \bigcup_{i} \Omega_{i}$ .

Theorem 3.1. For any regular and weakly affine visibility functional  $V[P]$ ,  $C_V$  is a coherence measure that is strongly monotonic under strictly incoherent operations (SIOs). If  $V$  is convex in  $P$ , then  $C_V$  is convex in  $\rho$ .

Proof. Let an SIO with Kraus operators  $K_{\lambda}$  be given, acting on a state  $\rho$ , so that  $q_{\lambda}\rho_{\lambda} = K_{\lambda}\rho K_{\lambda}^{\dagger}$  defines the probability of the event  $\lambda$  and the post-measurement state. Observe that, because  $K_{\lambda} = \pi_{\lambda}D_{\lambda}$  can be written as a diagonal matrix  $D_{\lambda}$  followed by a permutation  $\pi_{\lambda}$ ,

$$
\begin{array}{l} q _ {\lambda} U (\boldsymbol {\alpha}) \rho_ {\lambda} U (\boldsymbol {\alpha}) ^ {\dagger} = U (\boldsymbol {\alpha}) K _ {\lambda} \rho K _ {\lambda} ^ {\dagger} U (\boldsymbol {\alpha}) ^ {\dagger} \\ = K _ {\lambda} U (\boldsymbol {\beta}) \rho U (\boldsymbol {\beta}) ^ {\dagger} K _ {\lambda} ^ {\dagger}, \\ \end{array}
$$

with  $\beta_{j} = \alpha_{\pi_{\lambda}(j)}$ . This shows that the probability of seeing outcome  $\lambda$  is  $q_{\lambda}$  for all  $\rho (\alpha)$ .

Now choose measurements  $M^{(\lambda)}$  for each  $\rho_{\lambda}$ , taking values  $\omega$  in the disjoint sets  $\Omega_{\lambda}$ , subject to the probability law  $P_{\lambda} = P_{M^{(\lambda)}|\rho_{\lambda}}$  given by

$$
\begin{array}{l} P _ {\lambda} (\omega | \boldsymbol {\alpha}) = \operatorname {T r} U (\boldsymbol {\alpha}) \rho_ {\lambda} U (\boldsymbol {\alpha}) ^ {\dagger} M _ {\omega} ^ {(\lambda)} \\ = \frac {1}{q _ {\lambda}} \operatorname {T r} U (\boldsymbol {\alpha}) K _ {\lambda} \rho K _ {\lambda} ^ {\dagger} U (\boldsymbol {\alpha}) ^ {\dagger} M _ {\omega} ^ {(\lambda)} \\ = \frac {1}{q _ {\lambda}} \operatorname {T r} K _ {\lambda} U (\boldsymbol {\beta}) \rho U (\boldsymbol {\beta}) ^ {\dagger} K _ {\lambda} ^ {\dagger} M _ {\omega} ^ {(\lambda)} \\ = \frac {1}{q _ {\lambda}} \operatorname {T r} U (\boldsymbol {\beta}) \rho U (\boldsymbol {\beta}) ^ {\dagger} K _ {\lambda} ^ {\dagger} M _ {\omega} ^ {(\lambda)} K _ {\lambda}. \\ \end{array}
$$

Introducing the POVM  $\tilde{M} = (K_{\lambda}^{\dagger}M_{\omega}^{(\lambda)}K_{\lambda})_{\lambda ,\omega}$  with outcomes  $(\lambda ,\omega)$ , we can now invoke weak affinity:

$$
\sum_ {\lambda} q _ {\lambda} V \left[ P _ {\lambda} \right] = V \left[ \sum_ {\lambda} q _ {\lambda} P _ {\lambda} \right] = V \left[ P _ {\tilde {M} | \rho} \right] \leq C _ {V} (\rho),
$$

because the measurement  $\tilde{M}$  is eligible for  $\rho$  but may be suboptimal. As the measurements  $M^{(\lambda)}$  can be chosen to maximize the left-hand side, we obtain

$$
\sum_ {\lambda} q _ {\lambda} C _ {V} (\rho_ {\lambda}) \leq C _ {V} (\rho).
$$

For the convexity statement, let  $\rho = \sum_{i}p_{i}\sigma_{i}$  and choose any measurement  $M$  on  $\rho$ . Then,

$$
V \left[ P _ {M | \rho} \right] = V \left[ \sum_ {i} p _ {i} P _ {M | \sigma_ {i}} \right] \leq \sum_ {i} p _ {i} V \left[ P _ {M | \sigma_ {i}} \right] \leq \sum_ {i} p _ {i} C _ {V} (\sigma_ {i}),
$$

and because  $M$  may be chosen to maximize the left-hand side, we find  $C_V(\sum_i p_i \sigma_i) \leq \sum_i p_i C_V(\sigma_i)$ , as claimed.

A couple of remarks are in order: first, there do not seem to be easy conditions for  $C_V$  to be a (strong) coherence monotone under IO, but of course that is something potentially checkable in individual cases. Second, one might wonder in case we merely want to detect coherence, whether there is a universal measurement  $M$  such that if  $\rho$  has coherences, then  $V[P_{M|\rho}]$  is positive. The answer is yes, namely any tomographically complete measurement, as long as  $V[P]$  has the property that it is non-zero on every non-constant  $P$ .

# 4. Examples

We now show that the above theory is not just an abstract construction, by considering several concrete visibility parameters, for which we can evaluate the associated coherence measures, or at least considerably simplify the optimization.

# (a) Largest difference of intensity

The perhaps simplest and most intuitive parameter of visibility for two-outcome measurements  $M = (M_0, M_1 = \mathbb{1} - M_0)$  is the difference between the largest and the smallest value of  $P_{M|\rho}(0|\alpha) = \mathrm{Tr}U(\alpha)\rho U(\alpha)^\dagger M_0$ . To make it suitable for measurements with arbitrary outcome sets, we define

$$
V _ {\max } [ P ] := \sup  _ {\alpha , \beta} \frac {1}{2} \| P (\cdot | \alpha) - P (\cdot | \beta) \| _ {1}. \tag {4.1}
$$

Note that we do not normalize by the sum of the largest and smallest probability, as is customary in discussions of visibility in classical interferometry, where the basic observable quantities are intensities. There, this appears necessary to obtain a dimensionless visibility; here, however, we have the probabilities that are already dimensionless and have an absolute meaning.

Clearly,  $V_{\mathrm{max}}$  is regular and weakly affine, so the corresponding coherence measure  $C_{\mathrm{max}}$  is an SIO monotone. In fact, it is easy to evaluate it, and the result is

$$
\begin{array}{l} C _ {\max } (\rho) = \max  _ {\boldsymbol {\alpha}} \frac {1}{2} \| U (\boldsymbol {\alpha}) \rho U (\boldsymbol {\alpha}) ^ {\dagger} - \rho \| _ {1} \\ = \max  _ {\alpha} \frac {1}{2} \| [ \rho , U (\alpha) ] \| _ {1} \\ = \max  _ {\boldsymbol {\alpha}, M _ {0}} \operatorname {T r} U (\boldsymbol {\alpha}) \rho U (\boldsymbol {\alpha}) ^ {\dagger} M _ {0} - \operatorname {T r} \rho M _ {0}, \tag {4.2} \\ \end{array}
$$

because we can always shift  $\pmb{\beta}$  to  $\mathbf{0}$  by applying  $U(-\pmb{\beta})$ . In particular, the optimal measurement is a two-outcome POVM  $(M_0,M_1 = \mathbb{1} - M_0)$ , and the value is the largest difference in response probability over POVM elements.

We can compare the result with the trace distance measure of coherence,  $C_{\mathrm{Tr}}(\rho) = \min_{\sigma \in \Delta} \frac{1}{2} \| \rho - \sigma \|_1$ , introduced in [1]:  $C_{\mathrm{Tr}}(\rho) \leq C_{\max}(\rho) \leq 2C_{\mathrm{Tr}}(\rho)$ .

Namely, on the one hand, for  $\sigma \in \Delta$ , we have  $\| \rho - \sigma \|_1 = \| U(\alpha) \rho U(\alpha)^\dagger - \sigma \|_1$ , and hence by the triangle inequality,

$$
\| U (\boldsymbol {\alpha}) \rho U (\boldsymbol {\alpha}) ^ {\dagger} - \rho \| _ {1} \leq \| U (\boldsymbol {\alpha}) \rho U (\boldsymbol {\alpha}) ^ {\dagger} - \sigma \| _ {1} + \| \rho - \sigma \| _ {1},
$$

which implies  $C_{\mathrm{max}}(\rho) \leq 2C_{\mathrm{Tr}}(\rho)$ . On the other hand,

$$
\begin{array}{l} C _ {\mathrm {T r}} (\rho) \leq \frac {1}{2} \| \rho - \Delta (\rho) \| _ {1} \\ = \frac {1}{2} \left\| \rho - \int \mathrm {d} \boldsymbol {\alpha} U (\boldsymbol {\alpha}) \rho U (\boldsymbol {\alpha}) ^ {\dagger} \right\| _ {1} \\ \leq \int \mathrm {d} \boldsymbol {\alpha} \frac {1}{2} \| U (\boldsymbol {\alpha}) \rho U (\boldsymbol {\alpha}) ^ {\dagger} - \rho \| _ {1} \leq C _ {\max } (\rho). \\ \end{array}
$$

In the qubit case, it holds that  $C_{\mathrm{max}}(\rho) = 2|\rho_{01}| = C_{\ell_1}(\rho) = 2C_{\mathrm{Tr}}(\rho)$  (see appendix A).

# (b) Estimating equidistributed phases

Inspired by the previous example, we are motivated to consider guessing problems of a more general kind, where we are trying to estimate the true setting of the phases among

several alternatives, based on measurement outcomes. It turns out that a good candidate is the equidistributed set of  $d$  phases  $(2\pi j / d)(1,2,\ldots ,d),j = 1,\ldots ,d,$  and its shifts and permutations:

$$
V _ {\text {g u e s s}} [ P ] := - \frac {1}{d} + \max  _ {\substack {\boldsymbol {\alpha} _ {0}, \pi \in S _ {d} \\ \Omega_ {j} \cap \Omega_ {k} = \emptyset}} \frac {1}{d} \sum_ {j = 1} ^ {d} P (\Omega_ {j} \mid \boldsymbol {\alpha} _ {0} + j h _ {\pi}), \tag{4.3}
$$

where  $h_{\pi} = (2\pi /d)(\pi (1),\pi (2),\ldots ,\pi (d))$  is a generating vector of uniformly accelerating phases (w.r.t. the permutation  $\pi$  of coordinates). This quantity is the bias (excess over  $1 / d$ ) of the optimal strategy to guess the true value of  $j\in \{1,\dots ,d\}$  that defines the phase settings. As defined, this visibility functional is regular and weakly affine, so the corresponding  $C_{\mathrm{guess}}$  is a coherence monotone under SIO. As a matter of fact, it holds [17]

$$
C _ {\text {g u e s s}} (\rho) = - \frac {1}{d} + \max  _ {(M _ {j}) \text {P O V M}} \frac {1}{d} \sum_ {j = 1} ^ {d} \operatorname {T r} \rho \left(\boldsymbol {\alpha} _ {0} + j \boldsymbol {h} _ {\pi}\right) M _ {j} = \frac {1}{d} C _ {\mathrm {R}} (\rho), \tag {4.4}
$$

for any  $\alpha_0$  and any permutation  $\pi$ . Here,  $C_{\mathbb{R}}$  denotes the robustness of coherence, defined via

$$
1 + C _ {\mathrm {R}} (\rho) = \min  \operatorname {T r} \delta \quad \text {s . t .} \delta \geq \rho , \delta \in \Delta , \tag {4.5}
$$

which is known to be an IO monotone [17]. Interestingly, by maximizing the operational visibility proposed in [13, eqn (20)], the same result is obtained (P. J. Coles 2017, personal communication).

In the qubit case, it is well known that the robustness of coherence equals the  $\ell_1$ -measure:  $C_{\mathrm{R}}(\rho) = 2|\rho_{01}| = C_{\ell_1}(\rho)$  [17], and so  $C_{\mathrm{guess}}(\rho) = |\rho_{01}|$  is just half of that.

# (c) Largest sensitivity to phase changes

Looking back at example A, we note that the points of largest and smallest value of the response probability  $I(\pmb{\alpha}) = P_{M|\rho}(0|\pmb{\alpha}) = \mathrm{Tr}U(\pmb{\alpha})\rho U(\pmb{\alpha})^{\dagger}M_0$  to a POVM element  $M_0$  may be quite far apart. By contrast, in many applications of interferometry it is a relatively small phase difference that we want to pick up [18], so we are interested in the largest magnitude of the derivative of  $I(\pmb{\alpha})$ :

$$
V _ {\nabla} [ P ] := \max  _ {\alpha , h} \left| \frac {\partial I}{\partial h} (\alpha) \right|, \tag {4.6}
$$

where  $\alpha$  ranges over all phases, and  $h$  over all direction vectors that are suitably norm bounded. To extend  $V_{\nabla}$  to general measurements, we may include a maximization over all two-outcome coarse grainings. We can easily see that  $V_{\nabla}[P]$  is regular and weakly affine because  $I(\alpha)$  is a well-defined probability distribution over  $\alpha$ .

Now, as  $I(\alpha) = \operatorname{Tr} \rho U(\alpha)^{\dagger} M_0 U(\alpha)$ , its derivative at (w.l.o.g.)  $\mathbf{0}$  in direction  $h$  is given by

$$
\frac {\partial I}{\partial \boldsymbol {h}} (\mathbf {0}) = - \mathrm {i} \operatorname {T r} [ \rho , H ] M _ {0} = - \mathrm {i} \operatorname {T r} \rho [ H, M _ {0} ], \tag {4.7}
$$

where  $H$  is the diagonal Hamiltonian with eigenvalues  $h_j$ ,  $H = \mathrm{diag}(h)$ . Note that the derivative at any other point  $\alpha_0$  is the same, up to conjugating the measurement by  $U(\alpha_0)$ . There are two natural limitations on  $h$ : Geometrically, to obtain the largest gradient of  $I$ , we should consider unit vectors  $h$ , meaning  $\| H \|_2^2 = \operatorname{Tr} H^2 = 1$ ; or taking motivation from the Hamiltonian, we should bound its energy range, meaning  $\| H \|_{\infty} \leq 1$ . We denote these two scenarios by  $p = 2$  and  $\infty$ , giving rise to two coherence measures  $C_{\nabla}^{(p)}$ . From equation (4.7), we directly get

$$
C _ {\nabla} ^ {(p)} (\rho) = \max  \frac {1}{2} \| [ \rho , H ] \| _ {1} \quad \text {s . t .} H \operatorname {d i a g}., \| H \| _ {p} \leq 1. \tag {4.8}
$$

Inspecting this formula, we see that the optimization is convex in  $H$ , hence the maximum is attained on an extremal admissible Hamiltonian. For  $p = 2$ , these have the form  $H = \sum_{j} \epsilon_{j} \sqrt{t_{j}} |j\rangle \langle j|$ ,

with  $\epsilon_{j} = \pm 1$  and  $\sum_{j}t_{j} = 1$ . For  $p = \infty$ , the extremal  $H$  have entries  $\pm 1$  along the diagonal, and so

$$
C _ {\nabla} ^ {(\infty)} (\rho) = \max  _ {S _ {+} \dot {\cup} S _ {-} = [ d ]} 2 \| \Pi_ {+} \rho \Pi_ {-} \| _ {1}, \tag {4.9}
$$

where the maximization over partitions  $S_{+} \dot{\cup} S_{-} = [d]$ , with  $\Pi_{\bullet} = \sum_{j \in S_{\bullet}} |j\rangle \langle j|, \bullet = \pm$ . In both cases, we obtain a strong SIO monotone, due to the evident weak affinity of  $V_{\nabla}$ . From equation (4.2), we see that  $C_{\nabla}^{(\infty)} \leq C_{\max}$ , but equality does not seem to hold in general.

An alternate form of  $C_{\nabla}$  can be obtained by using equation (4.7), and going to the more convenient variable  $B = 2M_0 - \mathbb{1}$  in the above equations. After a few manipulations, we arrive at

$$
C _ {\nabla} ^ {(p)} (\rho) = \max  \operatorname {T r} \rho X \quad \text {s . t .} X \in \mathcal {C} _ {p}, \tag {4.10}
$$

where the maximization is over the set of Hermitian matrices

$$
\mathcal {C} _ {p} = \left\{X = \frac {1}{2 \mathrm {i}} [ H, B ]: H = H ^ {\dagger} \text {d i a g o n a l}, \| H \| _ {p} \leq 1, - \mathbb {1} \leq B \leq \mathbb {1} \right\}.
$$

In this form, it is formally a convex optimization problem, because we may as well go to the convex hull of  $\mathcal{C}_p$ . However, its characterization remains as a beautiful open problem. Indeed, it is easy to see that the elements of  $\mathcal{C}_p$  have zero diagonal and satisfy  $\| X\|_p = (\operatorname{Tr}|X|^p)^{1/p} \leq 1$ , but there may be other constraints.

Once again, the qubit case is very simple (see appendix A):  $C_{\nabla}^{(2)}(\rho) = \sqrt{2} |\rho_{12}|$  and  $C_{\nabla}^{(\infty)}(\rho) = 2|\rho_{12}| = C_{\ell_1}(\rho)$ .

# (d) Largest Fisher information

Considering further the previous example, we realize that finding the largest derivative of the probability  $P(0|\alpha)$ , while strongly motivated by the intuition rooted in intensities, does not necessarily identify the point of strongest statistical sensitivity, which is asking for the largest Fisher information, the natural measure for probability distributions. Looking again at directional estimation of a one-dimensional subfamily  $\alpha = th + \alpha_0$ ,  $t \in \mathbb{R}$ , the Fisher information is given by the expected squared logarithmic derivative of the probability distribution:

$$
\begin{array}{l} \mathcal {F} _ {\boldsymbol {\alpha} _ {0}} (\boldsymbol {h}) = \sum_ {\omega \in \Omega} P (\omega | \boldsymbol {\alpha} _ {0}) \left(\frac {\mathrm {d} \ln P (\omega | \boldsymbol {\alpha})}{\mathrm {d} t} \Big | _ {t = 0}\right) ^ {2} \\ = \sum_ {\omega \in \Omega} \frac {1}{P (\omega | \boldsymbol {\alpha} _ {0})} \left(\left. \frac {\mathrm {d} P (\omega | \boldsymbol {\alpha})}{\mathrm {d} t} \right| _ {t = 0}\right) ^ {2}, \tag {4.11} \\ \end{array}
$$

so we are considering the visibility functional

$$
V _ {\mathrm {F}} [ P ] := \max  _ {\alpha_ {0}, h} \mathcal {F} _ {\alpha_ {0}} (h), \tag {4.12}
$$

where  $\alpha_0$  varies over the whole space of phases, and  $h$  over a suitably bounded set of directions. Clearly,  $V_{\mathrm{F}}$  is regular and weakly affine.

The formula for the Fisher information, optimized over measurements (and  $\alpha_0$ , which w.l.o.g. is 0, by the same reasoning as in previous examples), for estimating  $t \approx 0$  in  $\mathrm{e}^{-\mathrm{i}tH}\rho \mathrm{e}^{\mathrm{i}tH}$  for a given diagonal Hamiltonian  $H = \mathrm{diag}(h)$  and  $\rho = \sum_{j}\lambda_{j}|e_{j}\rangle \langle e_{j}|$  is known [19,20] and given by

$$
\mathcal {F} _ {\text {o p t}} (h) = 2 \sum_ {j k} \frac {\left(\lambda_ {j} - \lambda_ {k}\right) ^ {2}}{\lambda_ {j} + \lambda_ {k}} | \langle e _ {j} | H | e _ {k} \rangle | ^ {2}. \tag {4.13}
$$

As in the previous example on sensitivity, there are two natural domains of diagonal Hamiltonians  $H$  over which to optimize this: Either  $\| H\| _2\leq 1$  or  $\| H\|_{\infty}\leq 1$ , leading to two variants  $C_{\mathrm{F}}^{(2)}(\rho)$  and  $C_{\mathrm{F}}^{(\infty)}(\rho)$  of the coherence measure.

In either case, the optimal choice of  $H$  is extremal subject to the convex constraint, because  $\mathcal{F}$  can easily be seen to be convex in  $H$ . Namely, each term  $|\langle e_j|H|e_k\rangle|$  is convex, hence also its square, and the coefficient in front of it manifestly non-negative. Thus, we obtain

$$
\begin{array}{l} C_{\mathrm{F}}^{(2)}(\rho) = \max_{\substack{\sum_{j}t_{j} = 1\\ \epsilon_{j} = \pm 1}}\sum_{jk}2\frac{(\lambda_{j} - \lambda_{k})^{2}}{\lambda_{j} + \lambda_{k}} \\ \left| \langle e _ {j} | \left(\sum_ {j} \epsilon_ {j} \sqrt {t _ {j}} | j \rangle \langle j | j\right) | e _ {k} \rangle \right| ^ {2} \tag {4.14} \\ \end{array}
$$

and

$$
C _ {\mathrm {F}} ^ {(\infty)} (\rho) = \max  _ {S _ {+}, S _ {-} \subset [ d ]} \sum_ {j k} 2 \frac {\left(\lambda_ {j} - \lambda_ {k}\right) ^ {2}}{\lambda_ {j} + \lambda_ {k}} | \langle e _ {j} | \left(\Pi_ {+} - \Pi_ {-}\right) | e _ {k} \rangle | ^ {2}, \tag {4.15}
$$

where the first maximization is over diagonal Hamiltonians with Hilbert-Schmidt norm 1; the second over partitions  $S_{+} \dot{\cup} S_{-} = [d]$ , with  $\Pi_{\bullet} = \sum_{j \in S_{\bullet}} |j\rangle \langle j|, \bullet = \pm$ , so that  $H = \Pi_{+} - \Pi_{-}$ .

For a qubit state  $\rho$ , it can be verified (see appendix A) that  $C_{\mathrm{F}}^{(2)}(\rho) = 4|\rho_{12}|^2 = C_{\ell_1}(\rho)^2$ ,  $C_{\mathrm{F}}^{(\infty)}(\rho) = 2C_{\ell_1}(\rho)^2$ .

# (e) Largest differential Chernoff bound

We observe that the attainability of the Fisher information presupposes access to many copies of the state and independent measurements, in which setting the Fisher information gives the optimal scaling of the mean squared estimation error with the number of copies. If we allow general collective measurements and at the same time only want to distinguish pairs of nearby states optimally, we are led to the differential Chernoff bound [21]: while the Chernoff bound is defined as  $\xi (\rho ,\sigma) = \sup_{0\leq s\leq 1} - \ln \operatorname {Tr}\rho^s\sigma^{1 - s}$ , for states and probability distributions alike [21,22], it is known that  $(1 / \mathrm{d}t^{2})\mathrm{d}^{2}\xi (P(\cdot |\pmb {\alpha}_{0}),P(\cdot |\pmb {\alpha}_{0} + \mathrm{d}th))\eqqcolon \mathrm{d}_{h}\xi^{2}$  defines the line element of a Riemannian metric on the parameter space. Thus, we let

$$
V _ {\partial \xi} [ P ] := \max  _ {\alpha_ {0}, h} \mathrm {d} _ {h} \xi^ {2}. \tag {4.16}
$$

As  $V_{\partial \xi}$  is regular and weakly affine, we will obtain a strong SIO monotone. Note that this would not work simply fixing a Hamiltonian, as shown in [23,24].

The differential Chernoff bound, optimized over measurements, for distinguishing  $\mathrm{e}^{-\mathrm{i}tH}\rho \mathrm{e}^{\mathrm{i}tH}$  for  $t\approx 0$  from  $\rho$  in the many-copy regime, with a diagonal Hamiltonian  $H$  and  $\rho = \sum_{j}\lambda_{j}|e_{j}\rangle \langle e_{j}|$  is again known [21], and given by  $\mathrm{d}_H\xi^2 = (1 / \mathrm{d}t^2)\mathrm{d}^2\xi (\rho ,\mathrm{e}^{-\mathrm{i}tH}\rho \mathrm{e}^{\mathrm{i}tH})$ , which evaluates to

$$
\begin{array}{l} \mathrm {d} _ {H} \xi^ {2} = \frac {1}{2} \sum_ {j k} \left(\sqrt {\lambda_ {j}} - \sqrt {\lambda_ {k}}\right) ^ {2} | \langle e _ {j} | H | e _ {k} \rangle | ^ {2} \\ = \frac {1}{2} \sum_ {j k} \left(\lambda_ {j} + \lambda_ {k} - 2 \sqrt {\lambda_ {j} \lambda_ {k}}\right) | \langle e _ {j} | H | e _ {k} \rangle | ^ {2} \\ = \operatorname {T r} \rho H ^ {2} - \operatorname {T r} \sqrt {\rho} H \sqrt {\rho} H = - \frac {1}{2} \operatorname {T r} [ \sqrt {\rho}, H ] ^ {2}, \tag {4.17} \\ \end{array}
$$

the latter equalling the Wigner-Yanase skew information,  $I_{\mathrm{WY}}(\rho ,H)$  [25].

As in the previous two examples, there are two natural domains of diagonal Hamiltonians  $H$  over which to optimize this: either  $\|H\|_2 \leq 1$  or  $\|H\|_\infty \leq 1$ , leading to two variants  $C_{\partial \xi}^{(2)}(\rho)$  and  $C_{\partial \xi}^{(\infty)}(\rho)$  of the coherence measure. Again,  $\mathrm{d}_H \xi^2$  is convex in  $H$ , owing to convexity of each term  $|\langle e_j | H | e_k \rangle|^2$ , and  $(\sqrt{\lambda_j} - \sqrt{\lambda_k})^2 \geq 0$ . Consequently, the optimal  $H$  is extremal under the convex norm constraint. For  $p = \infty$ , this means that the maximum is attained on a difference of two diagonal projectors,  $H = \Pi_+ - \Pi_-$ . For  $p = 2$ , however, we can say something even better, using Lieb's

concavity theorem [26], which says that for semidefinite  $H$ , the Wigner-Yanase skew information is convex in  $H^2$ , by writing  $H = \sqrt{H^2}$ . In general, we split  $H = H_{+} - H_{-}$  into positive and negative parts, and find after some straightforward algebra that

$$
I _ {\mathrm {W Y}} (\rho , H) = I _ {\mathrm {W Y}} (\rho , H _ {+}) + I _ {\mathrm {W Y}} (\rho , H _ {-}) - 2 \operatorname {T r} \sqrt {\rho} H _ {+} \sqrt {\rho} H _ {-},
$$

which by Lieb's theorem [26] is jointly convex in  $H_{+}^{2}$  and  $H_{-}^{2}$ . Thus, we find that the optimal  $H_{+}$  and  $H_{-}$  must be proportional to rank-one projectors, resulting in the expression claimed for  $C_{\partial \xi}^{(2)}(\rho)$ .

$$
C _ {\partial \xi} ^ {(2)} (\rho) = \max  _ {j, k, t} I _ {\mathrm {W Y}} \left(\rho , \sqrt {t} | j \rangle \langle j | - \sqrt {1 - t} | k \rangle \langle k |\right) \tag {4.18}
$$

and

$$
\begin{array}{l} C _ {\partial \xi} ^ {(\infty)} (\rho) = \max  _ {S _ {+}, S _ {-} \subset [ d ]} I _ {\mathrm {W Y}} (\rho , \Pi_ {+} - \Pi_ {-}) \\ = \max  _ {S _ {+} \cup S _ {-} = [ d ]} 4 \operatorname {T r} \sqrt {\rho} \Pi_ {+} \sqrt {\rho} \Pi_ {-}, \tag {4.19} \\ \end{array}
$$

where the first maximization is over distinct basis states  $j, k \in [d]$  and  $0 \leq t \leq 1$ ; the second over disjoint subsets  $S_{+}$  and  $S_{-}$  of  $[d]$ , with  $\Pi_{\bullet} = \sum_{j \in S_{\bullet}} |j\rangle \langle j|$ ,  $\bullet = \pm$ .

For a qubit state  $\rho$ , we find (see appendix) that  $C_{\partial \xi}^{(2)}(\rho) = 2|(\sqrt{\rho})_{12}|^2$  and  $C_{\partial \xi}^{(\infty)}(\rho) = 4|(\sqrt{\rho})_{12}|^2$ .

# (f) Largest Shannon information

The previous examples should have prepared us for thinking of visibility as an expression of how much information about  $\alpha$  the output distribution  $P(\cdot |\alpha)$  reveals. So why not take this to the logical conclusion? Noting that  $P$  is a channel from multi-phases  $\alpha$  to outputs  $\omega$ , in the Shannon theoretic sense, we are motivated to define visibility as the Shannon capacity of  $P$ :

$$
V _ {I} [ P ] := C (P) = \sup  _ {\mu} I (\boldsymbol {\alpha}: \omega), \tag {4.20}
$$

where  $\mu$  is a probability measure on the  $\alpha$ , defining a joint distribution  $\mu(\alpha)P(\omega|\alpha)$  of channel inputs and outputs, and  $I(X:Y) = D(\mathbb{P}_{XY} \| \mathbb{P}_X \times \mathbb{P}_Y)$  is the mutual information of two random variables [27]. It can be checked that  $V_I$  is regular and weakly affine. Operationally,  $V_I[P]$  is the largest communication rate that can be transmitted by a sender, who may encode information into the phase settings  $\alpha^{(1)}, \ldots, \alpha^{(n)}$  of asymptotically many interferometers, to a receiver who decodes the correct message with high probability based on the observations  $\omega_1, \ldots, \omega_n$  [27].

To obtain  $C_I(\rho)$ , we then only need to perform a maximization of the Shannon capacity over all measurements:

$$
\begin{array}{l} C _ {I} (\rho) = \sup  _ {(M _ {\omega})} C (P _ {M | \rho}) = \sup  _ {\mu} \sup  _ {(M _ {\omega})} I (\boldsymbol {\alpha}: \omega) \\ = \sup  _ {\mu} I _ {\mathrm {a c c}} \left(\left\{\mu (\boldsymbol {\alpha}), \rho (\boldsymbol {\alpha}) \right\}\right), \tag {4.21} \\ \end{array}
$$

where the latter quantity is known as the accessible information. These optimizations are by no means easy, and are worked out only in some few cases. In any case, theorem 3.1 shows that  $C_I$  is a SIO monotone. This might provide some motivation to try to evaluate  $C_I$  in certain special cases.

However, due to the Holevo bound [28], and the Holevo-Schumacher-Westmoreland theorem [29,30] regarding the capacity of the cq-channel  $\alpha \mapsto \rho(\alpha)$ , we obtain the following:

$$
C _ {I} (\rho) \leq S (\Delta (\rho)) - S (\rho) = C _ {r} (\rho) = \sup  _ {n} \frac {1}{n} C _ {I} \left(\rho^ {\otimes n}\right). \tag {4.22}
$$

Namely, the Holevo bound [28] upper-bounds the accessible information,

$$
\begin{array}{l} I _ {\mathrm {a c c}} (\{\mu (\alpha), \rho (\alpha) \}) \leq \chi (\{\mu (\alpha), \rho (\alpha) \}) \\ := S \left(\int \mu (\mathrm {d} \alpha) \rho (\alpha)\right) - \int \mu (\mathrm {d} \alpha) S (\rho (\alpha)). \\ \end{array}
$$

Here, the second term is always  $S(\rho)$  because the  $\rho(\alpha)$  are unitarily rotated versions of  $\rho$ , and the first term is maximized by the uniform distribution over all phases:

$$
C _ {I} (\rho) \leq S (\Delta (\rho)) - S (\rho) = C _ {r} (\rho), \tag {4.23}
$$

with the well-known relative entropy of coherence [1,2]. Note that the latter is known to be a monotone under IO, and even under the still larger class of maximally incoherent operations (MIOs) [3].

Invoking the Holevo-Schumacher-Westmoreland theorem [29,30] regarding the capacity of the cq-channel  $\alpha \mapsto \rho (\alpha)$ , we get furthermore  $\sup_n(1 / n)C_1(\rho^{\otimes n}) = C_r(\rho)$ .

In the qubit case, the optimization (4.21) seems to be unknown, but we believe that the maximum is attained on the binary ensemble  $\{(\frac{1}{2},\rho_0 = \rho),(\frac{1}{2},\rho_1 = \sigma_z\rho \sigma_z)\}$ , and the measurement in the eigenbasis of  $\rho_0 - \rho_1$ , which would yield  $C_I(\rho) = 1 - H((1\pm 2|\rho_{12}|) / 2)\approx (2 / \ln 2)|\rho_{12}|^2$ . On the other hand,  $C_r(\rho) = H((1\pm \mathrm{Tr}\rho \sigma_Z) / 2) - H((1\pm r) / 2)$ .

# 5. Discussion

Using a simple model of multi-path interferometry and a broad approach to visibility of an experimental set-up of phase modulation and detection, we showed that the concept of coherence of a state can be obtained by optimizing the visibility over detection schemes. We illustrated our approach by analysing specific visibility functionals. The results are clearest in the two-level case, corresponding to Mach-Zehnder interferometers, where we find that the single off-diagonal density matrix element governs almost all visibility and coherence effects. In settings with more paths, as should be expected, there are different inequivalent ways of quantifying visibility and correspondingly many different, incomparable coherence measures.

Our discussion shows that it is possible to link coherence theory, a priori quite an abstract enterprize, to operational notions in the physics of interferometers. We hope that our present approach will be fruitful in the future to develop a firm physical foundation of the resource theory of coherence. As an example of this kind of impact, we highlight theorem 3.1, which shows that visibility-based coherence measures are naturally monotone under strictly incoherent operations (SIOs), while it is an open question whether this holds also under the originally proposed incoherent operations (IOs); this might be construed as favouring SIOs over IOs as the 'correct' class of operations. See also Yadin et al. [31], where it is shown that SIOs are obtained precisely as the class of cctp maps that can be dilated in a specific incoherent way onto an extended system  $\mathcal{H} \otimes \mathcal{S}$ , where the 'internal' or 'spin' degrees of freedom of the particle are thought of as having no incoherence structure, so that in Åberg's framework [2] the incoherent subspaces are  $|j\rangle \otimes \mathcal{S}$ . Namely, a cctp map is strictly incoherent if and only if it can be decomposed into attaching an ancillary state of  $\mathcal{S}$ , followed by an incoherent unitary on the tensor product space, i.e. one mapping the subspaces  $|j\rangle \otimes \mathcal{S}$  into each other, followed by a destructive measurement of  $\mathcal{S}$  with outcomes  $\lambda$ .

Unlike other investigations that have tried to build a similar link between visibility and coherence, we start from visibility parameters as a feature of experimentally accessible data, rather than declaring known coherence measures as 'visibility' [32,33]. Because of this, we think of our approach as operational, in contrast to the cited works whose approach could be characterized as axiomatic. In this respect, we believe that our present work goes some way towards answering the call for an operational justification of coherence as a visibility parameter [13, sec. VII]. It is tempting to conjecture that all the coherence parameters derived from 'reasonable' visibility functionals satisfy duality relations with suitable path information measures such as in the

mentioned works. Whether visibility as conceptualized by us is always dual to a path information or some other parameter is a question we have to leave open at this point. In any case, our analysis of some concrete examples of visibility functionals on interference fringes has bolstered this connection to coherence, resulting in coherence measures that can be related to, and in some cases identified with, previously considered measures.

We also think that the present treatment gives some insight into the relationship between coherence and the resource theory of asymmetry (or reference frames) for the group of time translations (cf. [4]). Namely, looking at Examples C, D and E, each of the resulting coherence measures is obtained by maximizing, over a bounded set of diagonal Hamiltonians, a function given in equations (4.8), (4.13) and (4.17), respectively. It is known that, for a fixed Hamiltonian  $H$ , each of them is an monotone in the resource theory of time asymmetry corresponding to energy conservation; see, for instance, [23] for the latter quantity. Hence, we are led to think of coherence theory as asymmetry theory with a Hamiltonian that has fixed eigenvectors but 'undetermined' eigenvalues. This may go some way towards explaining the characteristic similarities and differences between (time) asymmetry and coherence.

In the analysis, we encountered some interesting mathematical problems, too, among them the characterization of the set of all commutators of norm-bounded diagonal and general Hermitian matrices. Furthermore, we would like to know whether, among the established coherence monotones, we can recover the  $\ell_1$ -measure  $C_{\ell_1}$  [1], or the coherence of formation  $C_f$  [2,16] directly via visibilities? In the light of [32,33], the former would be especially interesting.

Finally, going beyond the single-particle interference of our above theory, the present study suggests multi-particle interference as a natural extension. This will not only provide a framework for the compositions of systems (cf. Åberg [2]), but also bring out the unique quantum features of interference, as opposed to the mere wave-mechanical ones in the single-particle case.

Data accessibility. This article has no additional data.

Authors' contributions. All authors have contributed equally and crucially to the conception of the present paper, the execution of the scientific research and its writing. All authors gave their final approval for publication.

Competing interests. We declare we have no competing interests.

Funding. T.B. is supported by IISER Kolkata and acknowledges the hospitality of the Quantum Information Group (GIQ) at UAB during June-July 2016, when the present work was initiated. M.G.D. is supported by a doctoral studies fellowship of the Fundacion 'la Caixa'. A.W. is supported by the European Commission (STREP 'RAQUEL') and the ERC (Advanced Grant 'IRQUAT'). The authors acknowledge furthermore funding by the Spanish MINECO (grant FIS2013-40627-P), with the support of FEDER funds, and by the Generalitat de Catalunya CIRIT, project 2014-SGR-966.

Acknowledgements. It is our pleasure to thank Emili Bagan, Manabendra Bera, John Calsamiglia and Chang-Shui Yu for discussions on interferometers and visibility, and Patrick Coles for illuminating remarks on an earlier version of the manuscript.

# Appendix A. Qubit examples

# (a)  $C_{\max}$

As only the relative phase  $\alpha = \alpha_{1} - \alpha_{2}$  matters, we see

$$
\rho - U (\pmb {\alpha}) \rho U (\pmb {\alpha}) ^ {\dagger} = \left[ \begin{array}{c c} 0 & (1 - \mathrm {e} ^ {- \mathrm {i} \alpha}) \rho_ {1 2} \\ (1 - \mathrm {e} ^ {+ \mathrm {i} \alpha}) \rho_ {2 1} & 0 \end{array} \right].
$$

Its trace norm clearly is maximized at  $\alpha = \pi$ , showing  $C_{\mathrm{max}}(\rho) = |\rho_{12}| + |\rho_{21}| = C_{\ell_1}(\rho)$ , which for qubits is known to equal  $2C_{\mathrm{Tr}}(\rho)$ .

# (b)  $C_{\nabla}$

For  $p = \infty$ , the only non-trivial choice is  $\varPi_{+} = |1\rangle \langle 1|$  and  $\varPi_{-} = |2\rangle \langle 2|$ , directly resulting in  $C_{\nabla}^{(\infty)} = 2||1\rangle \langle 1|\rho |2\rangle \langle 2||_1 = 2|\rho_{12}|$ .

For  $p = 2$ , we have to consider the Hamiltonian  $H = \sqrt{t} |1\rangle \langle 1| \pm \sqrt{1 - t} |2\rangle \langle 2|$ , yielding

$$
[ \rho , H ] = \left[ \begin{array}{c c} 0 & (- \sqrt {t} \pm \sqrt {1 - t}) \rho_ {1 2} \\ (\sqrt {t} \mp \sqrt {1 - t}) \rho_ {2 1} & 0 \end{array} \right].
$$

Its trace norm is maximized for the negative sign choice and at  $t = \frac{1}{2}$ , and so  $C_{\nabla}^{(2)} = \sqrt{2} |\rho_{12}|$

(c)  $C_F$

The formula for the coherence measure reduces to

$$
C _ {\mathrm {F}} ^ {(p)} (\rho) = \max  2 \frac {(\lambda_ {1} - \lambda_ {2}) ^ {2}}{\lambda_ {1} + \lambda_ {2}} | \langle e _ {1} | H | e _ {2} \rangle | ^ {2},
$$

where the maximization is over  $H \in \operatorname{span}\{\mathbb{1}, \sigma_Z\}$  such that  $\| H \|_p \leq 1$ . Note that  $\lambda_1 + \lambda_2 = 1$  and  $|\langle e_1 | H | e_2 \rangle|^2 = \operatorname{Tr} H |e_1 \rangle \langle e_1 | H |e_2 \rangle \langle e_2 |$ .

This calculation is conveniently done in the Bloch picture, writing  $\rho = \frac{1}{2} (\mathbb{1} + r\cdot \pmb {\sigma})$  with a vector  $r = rr^0$  that we decompose as a product of its length  $r = |r|$  and a unit vector  $r^0$  (with components  $r_x^0,r_y^0$  and  $r_z^0$ ). In this way, the eigenprojectors of  $\rho$  become  $|e_{1,2}\rangle \langle e_{1,2}| = \frac{1}{2} (\mathbb{1}\pm r^0\cdot \pmb {\sigma})$ . In the above maximization, this allows us to identify  $\lambda_1 - \lambda_2 = r$  and  $r^2 = 2\mathrm{Tr}\rho^2 -1$ .

For  $p = \infty$ , we already know that  $H = \sigma_Z$  is optimal, so

$$
\begin{array}{l} C _ {\mathrm {F}} ^ {(\infty)} (\rho) = 2 r ^ {2} \operatorname {T r} \sigma_ {Z} | e _ {1} \rangle \langle e _ {1} | \sigma_ {Z} | e _ {2} \rangle \langle e _ {2} | \\ = 2 r ^ {2} \frac {1}{4} \operatorname {T r} \left(\mathbb {1} - r _ {x} ^ {0} \sigma_ {X} - r _ {y} ^ {0} \sigma_ {Z} + r _ {z} ^ {0} \sigma_ {Z}\right) \\ \cdot \left(\mathbb {1} - r _ {x} ^ {0} \sigma_ {X} - r _ {y} ^ {0} \sigma_ {Z} - r _ {z} ^ {0} \sigma_ {Z}\right) \\ = r ^ {2} \left(1 + \left(r _ {x} ^ {0}\right) ^ {2} + \left(r _ {y} ^ {0}\right) ^ {2} - \left(r _ {z} ^ {0}\right) ^ {2}\right) \\ = 4 (\operatorname {T r} \rho^ {2} - \operatorname {T r} \Delta (\rho) ^ {2}) \\ = 8 | \rho_ {1 2} | ^ {2} = 2 C _ {\ell_ {1}} (\rho) ^ {2}. \\ \end{array}
$$

For  $p = 2$ , the maximization reduces to that of  $2r^2\mathrm{Tr}H|e_1\rangle \langle e_1|H|e_2\rangle \langle e_2|$ , with  $H = \alpha \mathbb{1} + \beta \sigma_Z$  and  $2\alpha^{2} + 2\beta^{2}\leq 1$ . The trace decomposes into four terms; however, the three that contain a  $\alpha \mathbb{1}$  evaluate to 0, leaving  $2\beta^{2}r^{2}\mathrm{Tr}\sigma_{Z}|e_{1}\rangle \langle e_{1}|\sigma_{Z}|e_{2}\rangle \langle e_{2}|$ , which yields (using the optimal choice  $2\beta^{2} = 1$ )  $C_{\mathrm{F}}^{(2)}(\rho) = 2(\mathrm{Tr}\rho^2 -\mathrm{Tr}\Delta (\rho)^2) = C_{\ell_1}(\rho)^2$ .

(d)  $C_{\partial \xi}$

For  $p = \infty$ , the only non-trivial choice is  $\Pi_{+} = |1\rangle \langle 1|$  and  $\Pi_{-} = |2\rangle \langle 2|$ , directly resulting in  $C_{\partial \xi}^{(\infty)} = 4\mathrm{Tr}|1\rangle \langle 1|\sqrt{\rho} |2\rangle \langle 2|_{\sqrt{\rho}} = 4|(\sqrt{\rho})_{12}|^2$ .

For  $p = 2$ , we have to consider the Hamiltonian  $H = \sqrt{t} |1\rangle \langle 1| - \sqrt{1 - t} |2\rangle \langle 2|$ , yielding

$$
[ \sqrt {\rho}, H ] = \left[ \begin{array}{c c} 0 & (- \sqrt {t} - \sqrt {1 - t}) (\sqrt {\rho}) _ {1 2} \\ (\sqrt {t} + \sqrt {1 - t}) (\sqrt {\rho}) _ {2 1} & 0 \end{array} \right].
$$

Thus,  $I_{\mathsf{WY}}(\rho ,H) = (\sqrt{t} +\sqrt{1 - t})^2 |(\sqrt{\rho})_{12}|^2$  , which is maximized at  $t = \frac{1}{2}$  , hence  $C_{\partial \xi}^{(2)} = 2|\langle \sqrt{\rho}\rangle_{12}|^2$

# References

1. Baumgratz T, Cramer M, Plenio MB. 2014 Quantifying coherence. Phys. Rev. Lett. 113, 140401. (doi:10.1103/PhysRevLett.113.140401)  
2. Åberg J. 2006 Quantifying superposition. (http://arxiv.org/abs/0612146)

3. Streltsov A, Adesso G, Plenio MB. 2016 Quantum coherence as a resource. (http://arxiv.org/abs/1609.02439)  
4. Marvian I, Spekkens RW. 2016 How to quantify coherence: distinguishing speakable and unspeakable notions. Phys. Rev. A 94, 052324. (doi:10.1103/PhysRevA.94.052324)  
5. Wootters WK, Zurek WH. 1979 Complementarity in the double-slit experiment: quantum nonseparability and a quantitative statement of Bohr's principle. Phys. Rev. D 19, 473-484. (doi:10.1103/PhysRevD.19.473)  
6. Greenberger DM, Yasin A. 1988 Simultaneous wave and particle knowledge in a neutron interferometer. Phys. Lett. A 128, 391-394. (doi:10.1016/0375-9601(88)90114-4)  
7. Englert B-G. 1996 Fringe visibility and which-way information: an inequality. Phys. Rev. Lett. 77, 2154-2157. (doi:10.1103/PhysRevLett.77.2154)  
8. Jaeger G, Horne MA, Shimony A. 1993 Complementarity of one-particle and two-particle interference. Phys. Rev. A 48, 1023-1027. (doi:10.1103/PhysRevA.48.1023)  
9. Jaeger G, Shimony A, Vaidman L. 1995 Two interferometric complementarities. Phys. Rev. A 51, 54-67. (doi:10.1103/PhysRevA.51.54)  
10. Durr S. 2001 Quantitative wave-particle duality in multibeam interferometers. Phys. Rev. A 64, 042113. (doi:10.1103/PhysRevA.64.042113)  
11. Englert B-G, Kaszlikowski D, Kwek LC, Chee WH. 2008 Wave-particle duality in multipath interferometers: general concepts and three-path interferometers. Int. J. Quantum Inf. 6, 129-157. (doi:10.1142/S021974990803220)  
12. von Prillwitz K, Rudnicki L, Mintert F. 2015 Contrast in multipath interference and quantum coherence. Phys. Rev. A 92, 052114. (doi:10.1103/PhysRevA.92.052114)  
13. Coles PJ. 2016 Entropic framework for wave-particle duality in multipath interferometers. Phys. Rev. A 93, 062111. (doi:10.1103/PhysRevA.93.062111)  
14. Bimonte G, Musto R. 2003 On interferometric duality in multibeam experiments. J. Phys. A: Math. Gen. 36, 11481-11502. (doi:10.1088/0305-4470/36/45/009)  
15. Kaszlikowski D, Kwek LC, Zukowski M, Englert BG. 2003 Information-theoretic approach to single-particle and two-particle interference in multipath interferometers. Phys. Rev. Lett. 91, 037901. (doi:10.1103/PhysRevLett.91.037901)  
16. Winter A, Yang D. 2016 Operational resource theory of coherence. Phys. Rev. Lett. 116, 120404. (doi:10.1103/PhysRevLett.116.120404)  
17. Napoli C, Bromley TR, Cianciaruso M, Piani M, Johnston N, Adesso G. 2016 Robustness of coherence: an operational and observable measure of quantum coherence. Phys. Rev. Lett. 116, 150502. (doi:10.1103/PhysRevLett.116.150502)  
18. Collaboration LIGO. 2013 Enhanced sensitivity of the LIGO gravitational wave detector by using squeezed states of light. Nat. Photon. 7, 613-619. (doi:10.1038/nphoton.2013.177)  
19. Braunstein SL, Caves CM. 1994 Statistical distance and the geometry of quantum states. Phys. Rev. Lett. 72, 3439-3443. (doi:10.1103/PhysRevLett.72.3439)  
20. Paris MGA. 2009 Quantum estimation for quantum technology. Int. J. Quantum Inf. 7, 125-137. (doi:10.1142/S0219749909004839)  
21. Calsamiglia J, Muñoz-Tapia R, Masanes Ll, Acín A, Bagan E. 2008 Quantum Chernoff bound as a measure of distinguishability between density matrices: application to qubit and Gaussian states. Phys. Rev. A 77, 032311. (doi:10.1103/PhysRevA.77.032311)  
22. Chernoff H. 1952 A measure of asymptotic efficiency for tests of a hypothesis based on the sum of observations. Ann. Math. Stat. 23, 493-507. (doi:10.1214/aoms/1177729330)  
23. Girolami D. 2014 Observable measure of quantum coherence in finite dimensional systems. Phys. Rev. Lett. 113, 170401. (doi:10.1103/PhysRevLett.113.170401)  
24. Luo S. 2003 Wigner-Yanase skew information versus Fisher information. Proc. Am. Math. Soc. 132, 885-890. (doi:10.1090/S0002-9939-03-07175-2)  
25. Wigner EP, Yanase MM. 1964 On the positive semi-definite nature of a certain matrix expression. Can. J. Math. 16, 397-406. (doi:10.4153/CJM-1964-041-x)  
26. Lieb EH. 1973 Convex trace functions and the Wigner-Yanase-Dyson conjecture. Adv. Math. 11, 267-288. (doi:10.1016/0001-8708(73)90011-X)  
27. Shannon CE. 1948 A mathematical theory of communication. Bell Syst. Tech. J. 27, 379-423 & 623-656. (doi:10.1002/j.1538-7305.1948.tb01338.x)  
28. Holevo AS. 1973 Bounds for the quantity of information transmitted by a quantum communication channel. Probl. Inform. Transm. 9, 3-11.  
29. Holevo AS. 1998 The capacity of the quantum channel with general signal states. IEEE Trans. Inform. Theory 44, 269-273. (doi:10.1109/18.651037)

30. Schumacher B, Westmoreland MD. 1997 Sending classical information via noisy quantum channels. Phys. Rev. A 56, 131-138. (doi:10.1103/PhysRevA.56.131)  
31. Yadin B, Ma J, Girolami D, Gu M, Vedral V. 2016 Quantum processes which do not use coherence. Phys. Rev. X 6, 041028. (doi:10.1103/PhysRevX.6.041028)  
32. Bera MN, Qureshi T, Siddiqui MA, Pati AK. 2015 Duality of quantum coherence and path distinguishability. Phys. Rev. A 92, 012118. (doi:10.1103/PhysRevA.92.012118)  
33. Bagan E, Bergou JA, Cottrell SS, Hillary M. 2016 Relations between coherence and path information. Phys. Rev. Lett. 116, 160406. (doi:10.1103/PhysRevLett.116.160406)