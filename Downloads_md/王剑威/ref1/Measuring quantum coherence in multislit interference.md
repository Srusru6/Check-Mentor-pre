# Measuring quantum coherence in multislit interference

Tania Paul* and Tabish Qureshi†

Centre for Theoretical Physics, Jamia Millia Islamia, New Delhi-110025, India

(Received 6 February 2017; published 10 April 2017)

A quantitative measure of quantum coherence was recently introduced in the context of quantum information theory. This measure has also been propounded as a good quantifier of the wave nature of quantum objects. However, actually measuring coherence in an experiment is still considered a challenge. A procedure for measuring coherence in a multislit interference is proposed here. It can be used for experimentally testing duality relations for interference experiments involving more than two slits.

DOI: 10.1103/PhysRevA.95.042110

# I. INTRODUCTION

Wave-particle duality is a very interesting and intriguing aspect of quantum theory. Bohr argued that the wave and particle aspects of quantum objects, which we shall call quantons, are complementary in nature, in the sense that if an experiment exposes the wave nature, it will completely hide the particle aspect and vice versa [1]. Einstein had proposed his famous recoiling slit experiment (see, e.g., Ref. [2]) in order to refute the complementarity principle. It was later realized that wave and particle aspects could be revealed simultaneously, although to a quantitatively limited extent. Wave-particle duality is now understood as a constraint on the quantitative measures of the wave and particle natures, namely, duality relations for interference experiments [3-5]. Englert had proved a duality relation for a two-path interference, which is an inequality involving a distinguishability  $\mathcal{D}$  and fringe visibility  $\mathcal{V}$ :

$$
\mathcal {D} ^ {2} + \mathcal {V} ^ {2} \leqslant 1. \tag {1}
$$

Distinguishability is a measure which assumes the presence of a device which is capable of determining which of the two slits, or two paths, the quanton went through. If the device determines which path the quanton has traveled through without any error (i.e.,  $\mathcal{D} = 1$ ), then no interference fringes will appear at the detector (i.e.,  $\mathcal{V} = 0$ ). On the other hand, if there is an ambiguity in the which-path information (i.e.,  $\mathcal{D} \neq 1$ ), the quanton will show a reduced fringe visibility (i.e.,  $\mathcal{V} \neq 0$ ). The duality relation (1) was also experimentally verified [6]. Wave-particle duality in two-slit experiments has also been connected to things like entropic uncertainty relations [7] and the dichotomy between symmetry and asymmetry [8].

Wave-particle duality is expected to hold even when a quanton goes through more than two slits or paths. Several attempts were made to formulate a similar duality relation for the case of multipath experiments [9-13], without a completely satisfactory duality relation. The issue of wave-particle duality in multipath experiments has also been probed in the framework of entropic uncertainty [14]. For the particular case of three-slit interference, a new duality relation was recently derived [15], where the wave nature was characterized by the conventional fringe visibility or contrast, but the particle nature

was characterized by a new distinguishability  $\mathcal{D}_Q$  which is based on unambiguous quantum state discrimination (UQSD) [16-20]. The duality relation, for three-slit interference, has the form [15]

$$
\mathcal {D} _ {\mathcal {Q}} + \frac {2 \mathcal {V}}{3 - \mathcal {V}} \leqslant 1. \tag {2}
$$

If one uses this definition of distinguishability, one gets a different form of two-slit duality relation [15]:

$$
\mathcal {D} _ {\mathcal {Q}} + \mathcal {V} \leqslant 1. \tag {3}
$$

Although different in form, the above relation is completely equivalent to (1).

The form of the above two duality relations is different. This means that a universal duality relation for multislit interference, involving fringe visibility, is probably not possible. A new measure of wave nature could probably make a universal duality relation possible. Coherence in optics has long been thought to be representative of wave properties, and it has also been connected to distinguishability of paths [21]. However, a good quantitative measure of quantum coherence was missing.

Recently a measure of coherence was introduced, which is just the sum of the absolute values of the off-diagonal elements of the density matrix of a system, namely,  $\sum_{i\neq j}|\rho_{ij}|$ , with  $\rho_{i,j} = \langle i|\rho |j\rangle$  [22]. This measure is basis dependent, as it should be, and has the minimum value zero, for a diagonal density matrix. However, there is no well-defined upper limit to this measure, as it depends on the dimensionality of the Hilbert space of the system. Using this measure, a normalized quantity called coherence was very recently introduced [23]:

$$
\mathcal {C} = \frac {1}{n - 1} \sum_ {i \neq j} | \rho_ {i j} |, \tag {4}
$$

where  $n$  is the dimensionality of the Hilbert space. This quantity can assume value between 0 and 1 and can be a measure of wave nature just like fringe visibility. Here  $\rho_{ij}$  are the matrix elements of the density operator of the system, in the basis formed by the set of  $n$  orthogonal states, which correspond to the quanton passing through the  $n$  different slits. Based on this new measure of wave nature, the following duality relation for  $n$ -slit interference was obtained [23]:

$$
\mathcal {D} _ {\mathcal {Q}} + \mathcal {C} \leqslant 1. \tag {5}
$$

Here  $\mathcal{D}_Q$  is a path distinguishability based on UQSD. The above is a universal duality relation for  $n$ -slit interference. It

can be shown to reduce to (1) and (2) for two- and three-slit interference, respectively.

However, a shortcoming of the above relation is that it is not clear if  $\mathcal{C}$  can be measured in an experiment. While the fringe visibility can be experimentally measured to quantify the wave nature in (1) and (2),  $\mathcal{C}$  appears to be just a theoretical construct. The ability to measure quantum coherence is a much-sought-after objective and has received research attention [24,25]. In this paper we show that  $\mathcal{C}$  can actually be measured in a multislit interference experiment.

# II. MULTISLIT INTERFERENCE AND WAVE NATURE

# A. Interference visibility

Let us first look at the case of a  $n$ -slit quantum interference with quantons, without any which-path detection. In  $n$ -slit interference, if  $|\psi_i\rangle$  is the amplitude of the quanton to go through the  $i$ th slit, then the state of the quanton, after passing through the slit, can be described as sum of all possible amplitudes, i.e.,  $|\psi_i\rangle$ , to go through different slits. Since the slits are well separated, the states  $|\psi_i\rangle$  should be orthogonal to each other. We may choose  $|\psi_i\rangle$  to be normalized, and associate a weight factor with it, which determines the probability of the quanton to go through a particular slit:

$$
\left| \Psi_ {0} \right\rangle = c _ {1} \left| \psi_ {1} \right\rangle + c _ {2} \left| \psi_ {2} \right\rangle + \dots , c _ {n} \left| \psi_ {n} \right\rangle . \tag {6}
$$

The probability of the particle to go through, e.g., the  $k$ th slit is given by  $|c_k|^2$  and  $\sum_{i=1}^{n} |c_i|^2 = 1$ . Since the states  $\{|\psi_i\rangle\}$  are orthonormal, they can be assumed to form basis states to describe the quanton after it has passed through the slits.

The interference on the screen is described by the probability density of particle hitting the screen at particular position  $|\langle x|\Psi_0\rangle |^2$ . The expression for the pattern on the screen will have the following general form:

$$
\left| \langle x | \Psi_ {0} \rangle \right| ^ {2} = \sum_ {i = 1} ^ {n} \left| c _ {i} \right| ^ {2} \left| \langle x | \psi_ {i} \rangle \right| ^ {2} + \sum_ {j \neq k} c _ {j} ^ {*} c _ {k} \langle x | \psi_ {k} \rangle \langle \psi_ {j} | x \rangle . \tag {7}
$$

The first term just represents the sum of patterns formed by the quanton coming out of individual slits, without any interference. The second term represents the interference between the amplitudes of the quanton coming out of the  $j$ th and  $k$ th slits, summed over all  $js$  and  $ks$ . One would notice here that the multislit interference pattern consists of all possible two-slit terms ( $j \neq k$ ). There are no three- or multiple-slit terms, which is a direct consequence of the Born rule. This aspect of interference has been used to test Born rule in three-slit interference experiments [26].

Now, if one wants to find out which slit the particle went through, one has to have some kind of path-detecting device in place. Without going into the details of what kind of device one may use, we just consider certain fundamental aspects of what such a detection should involve. According to von Neumann, in a quantum measurement, the first process should be to let the detector interact with the quanton and get entangled with it [27]. This involves building up of correlations between the quanton and the path detector. The necessary condition for a quantum measurement of which slit the quanton went through is satisfied when each  $|\psi_i\rangle$  gets correlated with certain state of the path detector  $|d_i\rangle$ . The combined quanton-detector state,

in such a situation, assumes the following entangled form:

$$
| \Psi \rangle = c _ {1} | \psi_ {1} \rangle | d _ {1} \rangle + c _ {2} | \psi_ {2} \rangle | d _ {2} \rangle + \dots , c _ {n} | \psi_ {n} \rangle | d _ {n} \rangle , \tag {8}
$$

where  $|d_i\rangle$  is the state of the path detector if the quanton went through the  $i$ th path. For simplicity, we assume the detector states  $\{|d_i\rangle\}$  to be normalized but not necessarily orthogonal. With the path detector added to the interference setup, the pattern of the quantons hitting the screen has the following form:

$$
\begin{array}{l} | \langle x | \Psi_ {0} \rangle | ^ {2} = \sum_ {i = 1} ^ {n} | c _ {i} | ^ {2} | \langle x | \psi_ {i} \rangle | ^ {2} \\ + \sum_ {j \neq k} c _ {j} ^ {*} c _ {k} \langle x | \psi_ {k} \rangle \langle \psi_ {j} | x \rangle \langle d _ {j} | d _ {k} \rangle . \tag {9} \\ \end{array}
$$

While the first term remains unaffected by the introduction of path detector, the second term, which gives rise to interference, is reduced by the factors  $\langle d_j|d_k\rangle$ . In fact, for completely orthogonal path-detector states,  $\langle d_j|d_k\rangle = 0$ , and the interference pattern disappears. So it is clear from this very general analysis that any attempt to gain information, about which slit the quanton went through, affects the interference. In other words, probing the particle nature of the quanton more precisely degrades its wave nature, which is characterized by interference.

In order to quantify the wave nature of the quanton, one needs to quantify the sharpness of the interference pattern. The interference visibility is defined as

$$
\mathcal {V} \equiv \frac {I _ {\max } - I _ {\min }}{I _ {\max } + I _ {\min}}, \tag {10}
$$

where  $I_{\mathrm{max}}, I_{\mathrm{min}}$  are the maximum and minimum intensity, respectively, in some region of the interference pattern. While this visibility works well for two-slit interference experiments, it is not clear whether the same definition suffices for multislit experiments [10-14].

# B. Coherence as a measure of wave nature

Coherence as defined by (4) has been shown to capture the wave aspect of a quanton well. Let us calculate the coherence  $\mathcal{C}$  for the state (8). Since coherence is a property of the quanton alone, we will first trace out the path-detector states, to obtain a reduced density matrix of the quanton. Writing the corresponding density operator for the state (8), and taking a trace over an orthonormal set of path-detector states, it is straightforward to obtain the reduced density operator of the quanton:

$$
\rho_ {r} = \sum_ {k = 1} ^ {n} \sum_ {j = 1} ^ {n} c _ {k} c _ {j} ^ {*} \langle d _ {j} | d _ {k} \rangle | \psi_ {k} \rangle \langle \psi_ {j} |. \tag {11}
$$

Inserting this reduced density in the expression for coherence (4), and using  $\{|\psi_i\rangle \}$  as the basis, one arrives at

$$
\begin{array}{l} \mathcal {C} = \frac {1}{n - 1} \sum_ {k \neq j} | \langle \psi_ {k} | \rho_ {r} | \psi_ {j} \rangle | \\ = \frac {1}{n - 1} \sum_ {k \neq j} | c _ {k} | | c _ {j} | | \langle d _ {j} | d _ {k} \rangle |. \tag {12} \\ \end{array}
$$

Two extreme cases may be worth noting here. If the detector states  $\{|d_i\rangle\}$  are all mutually orthogonal to each other, the coherence  $\mathcal{C}$  is 0. This implies that in this situation, the fringe visibility goes to zero. This is also the case when the interference disappears. On the other extreme, if all the path-detector states  $|d_i\rangle$  are identical, and all  $c_{i}$  are equal to  $\frac{1}{\sqrt{n}}$ , the coherence  $\mathcal{C}$  is equal to 1. This is the special case where there is zero path information about the quanton, and the quanton is equally likely to pass through any of the  $n$  slits. In this situation one gets sharpest interference. For other nonzero values of  $|\langle d_j|d_k\rangle|$ , and different amplitudes of the quanton passing through different slits,  $\mathcal{C}$  will lie between 0 and 1.

Durr suggested that any newly defined visibility should satisfy the following criteria [10]:

(1) It should be possible to give a definition of visibility that is based only on the interference pattern, without explicitly referring to the matrix elements of  $\rho$ .  
(2) It should vary continuously as a function of the matrix elements of  $\rho$ .  
(3) If the system shows no interference, visibility should reach its global minimum.  
(4) If  $\rho$  represents a pure state (i.e.,  $\rho^2 = \rho$ ) and all  $n$  beams are equally populated (i.e., all  $\rho_{jj} = 1 / n$ ), visibility should reach its global maximum.  
(5) Visibility considered as a function in the parameter space  $(\rho_{11},\rho_{12},\ldots ,\rho_{nn})$  should have only global extrema, no local ones.  
(6) Visibility should be independent of our choice of the coordinate system. Coherence, as defined by (12), satisfies Durr's criteria (2) through (6). However, criterion (1) implies that it should be possible to talk of coherence based only on the interference pattern. This point will be addressed in the next section.

# III. MEASURING COHERENCE

# A. Pure quantum-detector state

Next we address the issue of measuring coherence. In order to see how one may try to measure coherence, one has to have an interference pattern. For getting an interference pattern we theoretically analyze the behavior of a quanton passing through  $n$  equally spaced slits. We assume that the quanton is traveling along the  $z$  axis and encounters  $n$  slits, which lie in the  $x - y$  plane, as shown in Fig. 1. The slits are centered at  $x_{j} = j\ell, j = 1,2,3,\ldots,n$ . This means that the distance between any two neighboring slits is  $\ell$ . We also assume that the state that emerges from the  $j$ th slit is a Gaussian along the  $x$  axis, centered at  $x = j\ell$ . The width of the Gaussian is very small and is supposed to be of the order of the width of the slit. Thus the state that emerges from the slits, at time  $t = 0$ , has the following form, in the position basis:

$$
\langle x | \Psi (0) \rangle = A \sum_ {j = 1} ^ {n} c _ {j} \exp \left[ - \frac {(x - j \ell) ^ {2}}{\epsilon^ {2}} \right] | d _ {j} \rangle , \tag {13}
$$

where  $A = (2 / \pi \epsilon^2)^{1 / 4}$ . After traveling a distance  $D$ , in a time  $t$ , the quanton reaches the screen. The time evolution of the Gaussian can be calculated by either assuming the quanton to be particle of mass  $m$ , moving with a momentum

![](images/90edc81b50ae023474c60f83a943857ad39c9f63af2f0c91ef4cb588b4f6c906.jpg)  
FIG. 1. Schematic diagram of an  $n$ -slit interference experiment. A quantum path detector has been added to the setup, which is capable of obtaining information on which slit the particle passed through.

corresponding to a de Broglie wavelength  $\lambda$ , or by assuming it to be a photon of wavelength  $\lambda$  [28]. In both cases, the state of the quanton, at the screen, is given by

$$
\langle x | \Psi (t) \rangle = A _ {t} \sum_ {j = 1} ^ {n} c _ {j} \exp \left[ - \frac {(x - j \ell) ^ {2}}{\epsilon^ {2} + i \lambda D / \pi} \right] | d _ {j} \rangle , \tag {14}
$$

where  $A_{t} = \left[\frac{2}{\pi(\epsilon + i\lambda D / \pi\epsilon)}\right]^{1 / 4}$ .

The probability density of the quanton, hitting the screen at a position  $x$ , can now be calculated as

$$
\begin{array}{l} | \langle x | \Psi (t) \rangle | ^ {2} = | A _ {t} | ^ {2} \sum_ {j = 1} ^ {n} | c _ {j} | ^ {2} \exp \left[ - \frac {2 \epsilon^ {2} (x - j \ell) ^ {2}}{\epsilon^ {4} + (\lambda D / \pi) ^ {2}} \right] \\ + \sum_ {j \neq k} c _ {j} ^ {*} c _ {k} \exp \left[ - \frac {(x - j \ell) ^ {2}}{\epsilon^ {2} - i \lambda D / \pi} \right] \\ \times \exp \left[ - \frac {(x - k \ell) ^ {2}}{\epsilon^ {2} + i \lambda D / \pi} \right] \langle d _ {j} | d _ {k} \rangle . \tag {15} \\ \end{array}
$$

Notice that  $\epsilon$ , being the width of one slit, is very small, and hence  $\epsilon^4$  is negligible in comparison to  $(\lambda D / \pi)^2$ . Also, it is convenient to combine the phases of  $c_{j}$  and  $|d_j\rangle$  as  $c_{j}|d_{j}\rangle = |c_{j}||d_{j}\rangle e^{i\theta_{j}}$ , where  $|d_j\rangle$  is now real. With these assumptions, the above assumes the following form:

$$
\begin{array}{l} \left| \langle x | \Psi (t) \rangle \right| ^ {2} = \left| A _ {t} \right| ^ {2} \sum_ {j = 1} ^ {n} \left| c _ {j} \right| ^ {2} \exp \left[ - \frac {2 \epsilon^ {2} (x - j \ell) ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \\ + \sum_ {j \neq k} | c _ {j} | | c _ {k} | | \langle d _ {j} | d _ {k} \rangle | \exp \left[ - \frac {\epsilon^ {2} f _ {j k} (x)}{(\lambda D / \pi) ^ {2}} \right] \\ \times \cos \left[ \frac {2 \pi x l (k - j)}{\lambda D} + \frac {\ell^ {2} (j ^ {2} - k ^ {2})}{\lambda D} \right. \\ + \left(\theta_ {k} - \theta_ {j}\right) \bigg ], \tag {16} \\ \end{array}
$$

where  $f_{jk}(x) = 2x^{2} - 2x\ell (j + k) + (j^{2} + k^{2})\ell^{2}$ . The expression (16) represents an  $n$ -slit interference pattern in the presence of path detectors. The distance between the primary maxima or the fringe width is given by  $w = \lambda D / \ell$ , which is much larger than the distance between the two slits,  $\ell$ , and also the width of a slit  $\epsilon$ . If the position on the screen  $x$  is on any

maximum away from the one at  $x = 0, j\ell$  is negligible in its comparison. With these things in mind, the probability density of quantons on the screen can be simplified to

$$
\begin{array}{l} | \langle x | \Psi (t) \rangle | ^ {2} = | A _ {t} | ^ {2} \sum_ {j = 1} ^ {n} | c _ {j} | ^ {2} \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \\ + \sum_ {j \neq k} | c _ {j} | | c _ {k} | | \langle d _ {j} | d _ {k} \rangle | \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \\ \times \cos \left[ \frac {2 \pi x l (k - j)}{\lambda D} + \left(\theta_ {k} - \theta_ {j}\right) \right]. \tag {17} \\ \end{array}
$$

For simplicity, we assume all the phases to be the same:  $\theta_{k} - \theta_{j} = 0$ . Notice that for  $x_{m} = m\lambda D / \ell, m = 0,1,2,\ldots$ , the cosine term is 1, irrespective of the values of  $j,k$ . These are the positions of the primary maxima, where the cosine contributions from every pair of slits are 1. There are other positions where cosine terms from some slit pairs are 1, but those from some others are not. Those are the secondary maxima. The maximum intensity at a primary maximum is then given by,  $I_{\mathrm{max}} = |\langle x_m|\Psi (t)\rangle |^2$  and has the form

$$
\begin{array}{l} I _ {\max } = \left| A _ {t} \right| ^ {2} \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \\ \times \left[ \sum_ {j = 1} ^ {n} | c _ {j} | ^ {2} + \sum_ {j \neq k} | c _ {j} | | c _ {k} | | \langle d _ {j} | d _ {k} \rangle | \right]. \tag {18} \\ \end{array}
$$

If the same experiment is performed using incoherent light, instead of coherent light, one has to average over the phases  $\theta_{j},\theta_{k}$  in (17), and that would kill the cosine terms. The intensity, at the same position on the screen as in (18), is then given by

$$
I _ {\mathrm {i n c}} = \left| A _ {t} \right| ^ {2} \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \sum_ {j = 1} ^ {n} \left| c _ {j} \right| ^ {2}. \tag {19}
$$

One may carry out a careful photon-counting experiment with coherent laser light to measure  $I_{\mathrm{max}}$ . A phase randomizer may then be added to the setup and the experiment repeated to measure  $I_{\mathrm{inc}}$ . This procedure would allow one to calculate the following quantity:

$$
\frac {1}{n - 1} \frac {I _ {\max } - I _ {\mathrm {i n c}}}{I _ {\mathrm {i n c}}} = \frac {1}{n - 1} \sum_ {j \neq k} | c _ {j} | | c _ {k} | | \langle d _ {j} | d _ {k} \rangle |, \tag {20}
$$

where  $n$  is the number of slits used in the experiment. Comparing the r.h.s. of the above equation with (12), one finds that it is exactly the same as the coherence  $\mathcal{C}$  for the quanton! So, one can measure the value of coherence in a multislit experiment. Needless to say, since the experiment involves two parts, it is important to make sure that number of photons coming out of the slits remains unchanged. Thus the experimentally measured coherence can be written as

$$
\mathcal {C} _ {\text {e x p t}} = \frac {1}{n - 1} \frac {I _ {\max } - I _ {\mathrm {i n c}}}{I _ {\mathrm {i n c}}}. \tag {21}
$$

In real situations, the interference fringes occur within a Gaussian envelope, and the maxima on either side of the Gaussian peak will be gradually lower in intensity. However, it does not matter which primary maximum is chosen for

measuring the intensity. The procedure makes sure that the Gaussian part cancels out and one gets an expression for coherence (20) independent of the position of the primary maximum. With the measured coherence given by (21),  $\mathcal{C}$  also satisfies Durr's criterion (1) for being a good measure of interference visibility.

# B. Mixed quantum-detector state

In real-life situations, it may happen that the quanton is affected by the environment and can no longer be described by a pure state. In such situations, the state of the quanton and path detector combined may be represented by a mixed state density operator,

$$
\rho_ {m} = \sum_ {j = 1} ^ {n} \sum_ {k = 1} ^ {n} q _ {j k} | \psi_ {j} \rangle \langle \psi_ {k} | \otimes | d _ {j} \rangle \langle d _ {k} |, \tag {22}
$$

where  $q_{jk}$  are complex numbers. In this case, coherence is given by [23]

$$
\mathcal {C} = \frac {1}{n - 1} \sum_ {k \neq j} | q _ {j k} | | \langle d _ {k} | d _ {j} \rangle |. \tag {23}
$$

One can then follow a procedure closely similar to that in the preceding subsection and obtain the reduced density matrix for the quanton at the screen. The diagonal part of the density matrix in the position representation is then given by

$$
\begin{array}{l} \rho_ {m r} (x, x, t) = | A _ {t} | ^ {2} \sum_ {j = 1} ^ {n} | q _ {j j} | \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \\ + \sum_ {j \neq k} | q _ {j k} | | \langle d _ {j} | d _ {k} \rangle | \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \\ \times \cos \left[ \frac {2 \pi x l (k - j)}{\lambda D} + \phi_ {j k} \right], \tag {24} \\ \end{array}
$$

where  $q_{jk}\langle d_j|d_k\rangle = |q_{jk}||\langle d_j|d_k\rangle |e^{i\phi_{jk}}$ . The maximum intensity at a primary maximum is then given by  $I_{\mathrm{max}} = \rho_{mr}(x_m,x_m,t)$ . Again, for incoherent light, random variations in  $\phi_{jk}$  will kill the cosine terms. Experimentally measured coherence is then given by

$$
\mathcal {C} _ {\text {e x p t}} = \frac {1}{n - 1} \frac {I _ {\max } - I _ {\mathrm {i n c}}}{I _ {\mathrm {i n c}}} = \frac {1}{n - 1} \sum_ {j \neq k} | q _ {j k} | | \langle d _ {j} | d _ {k} \rangle |, \tag {25}
$$

which agrees with the theoretical expression for coherence (23).

# C. Coherence of the incoming quantum

In the preceding subsections, we looked at the problem of measuring the coherence of a quanton as it emerges from n slits, and a path detector tries to get information about which of the  $n$  slits the quanton passed through. The coherence of the quanton degrades in the process of path detection. This procedure is well suited for testing wave-particle duality relations. On the other hand, if one is interested in measuring the coherence of the incoming quanton as it enters the slits, the above procedure may not be well suited for the job. One reason is that in the preceding procedure, one needs to change the incoming state

by randomizing the phases at different slits. One may want a measuring procedure where the incoming state is not disturbed. Another reason could be that the phase randomizer may not be easily realizable. We propose another procedure for this particular case.

We assume that we have an  $n$ -slit system and a path detector in place where the path distinguishability is tunable. At the least, it should be switchable between two modes corresponding to (a) making all the paths completely indistinguishable and (b) making all the paths fully distinguishable. We denote the two cases (a) and (b) by  $\parallel$  and  $\perp$ , respectively. First, the intensity at a primary maximum is measured when all  $n$  paths are indistinguishable, i.e.,  $|d_i\rangle$  are all identical and parallel. For a pure quantum state, this intensity can be obtained simply by putting  $|\langle d_j|d_k\rangle | = 1$  for all  $j,k$  in (18), and is given by

$$
I _ {\max } ^ {\parallel} = \left| A _ {t} \right| ^ {2} \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \left[ \sum_ {j = 1} ^ {n} \left| c _ {j} \right| ^ {2} + \sum_ {j \neq k} \left| c _ {j} \right| \left| c _ {k} \right| \right]. \tag {26}
$$

Next the path detector is switched to the mode where all  $n$  paths are fully distinguishable, and the intensity is measured at the same position on the screen as before. This intensity can be obtained simply by putting  $\langle d_j|d_k\rangle = 0$  for all  $j\neq k$  in (18) and is given by

$$
I _ {\max } ^ {\perp} = \left| A _ {t} \right| ^ {2} \exp \left[ - \frac {2 \epsilon^ {2} x ^ {2}}{(\lambda D / \pi) ^ {2}} \right] \sum_ {j = 1} ^ {n} \left| c _ {j} \right| ^ {2}. \tag {27}
$$

Coherence of the incoming quantum can then be measured as

$$
\mathcal {C} _ {\text {e x p t}} ^ {0} = \frac {1}{n - 1} \frac {I _ {\max } ^ {\parallel} - I _ {\max } ^ {\perp}}{I _ {\max } ^ {\perp}} = \frac {1}{n - 1} \sum_ {j \neq k} | c _ {j} | | c _ {k} |. \tag {28}
$$

The right-hand side of the above is the coherence of the incoming quanton, in the basis of the  $n$ -slit paths, unmodified by the path detector. Doing away with the factor  $\frac{1}{n-1}$  in the above gives the unnormalized coherence introduced by Baumgratz et al. [22]. Exactly the same procedure will also work for quantons described by a mixed state.

So, in order to measure the coherence of a beam of light or massive particles, one needs to introduce a  $n$ -slit setup in its path and measure the intensity at a primary maximum, in two different modes of the path detector.

# D. Path distinguishability

For completeness, we briefly discuss the path distinguishability  $\mathcal{D}_Q$  introduced in Ref. [23]. From (8) it is clear that in order to tell which slit the quanton went through, one has to be able to tell which path-detector state out of the set  $\{|d_j\rangle \}$  materialized. If one is interested only in the path detector and is not concerned with what happens to the quanton after passing through the slits, one can write the density operator corresponding to the state (8) and trace out the states of the quanton. The resulting reduced density operator for the path detector is

$$
\rho_ {d} = \sum_ {j = 1} ^ {n} | c _ {j} | ^ {2} | d _ {j} \rangle \langle d _ {j} |. \tag {29}
$$

So, essentially a particular detector state  $|d_k\rangle$  occurs with a probability  $|c_k|^2$ . The only problem is that the states  $\{|d_j\rangle\}$  are not orthogonal to each other, in general. The problem of path detection then boils down to the following. Certain known nonorthogonal states  $|d_k\rangle$  occur at random, one at a time, and which one occurs is not known. One has to tell unambiguously which of the set  $\{|d_j\rangle\}$  is a given state. Our view is that the answer has to be unambiguous, and only then can one claim that the particle has gone through a particular slit. An answer which is ambiguous doesn't serve the purpose.

In general, the best strategy to distinguish between nonorthogonal states is unambiguous quantum state discrimination (UQSD) [16-20]. In UQSD, the maximum probability with which nonorthogonal pure states can be unambiguously distinguished can be calculated [29,30]. The probability of successfully distinguishing between  $n$  nonorthogonal states  $\{|d_j\rangle\}$  via UQSD is bounded by [29,30]

$$
P _ {n} \leqslant 1 - \frac {1}{n - 1} \sum_ {k \neq j} | c _ {k} | | c _ {j} | | \langle d _ {k} | d _ {j} \rangle |. \tag {30}
$$

It should be reiterated that the probabilities  $|c_{j}|^{2}$  are decided by the initial superposition in the quantum state. The path distinguishability  $\mathcal{D}_Q$  can then be defined as the maximum probability with which the  $n$  paths of the particle can be distinguished without any error, and is given here by the upper bound of (30) [23]:

$$
\mathcal {D} _ {Q} \equiv 1 - \frac {1}{n - 1} \sum_ {i \neq j} | c _ {i} | | c _ {j} | | \langle d _ {i} | d _ {j} \rangle |. \tag {31}
$$

The path distinguishability can take values between 0 and 1. For all mutually orthogonal  $\{|d_j\rangle\}$ , one gets  $\mathcal{D}_Q = 1$ . It should be mentioned that that UQSD works for linearly independent states. In the situation where the set  $\{|d_j\rangle\}$  is not linearly independent, UQSD will not work, and one has to employ some other strategy to unambiguously tell, probably in a limited way, which of  $\{|d_j\rangle\}$  states one has obtained. However, one can still continue to use the upper bound given by (30). Of course in this scenario, the bound may not be reachable.

The quantum coherence  $\mathcal{C}$ , given by (12) or (23), and the path distinguishability, given by (31), are bounded by the inequality (5) [23]. In light of the demonstration of experimental measurability of  $\mathcal{C}$ , the inequality (5) can be treated as a general duality relation which works for interference experiments with any number of slits.

# IV. CONCLUSIONS

In conclusion, we have presented a method of experimentally measuring the recently introduced measure of coherence,  $\mathcal{C}$ , in a multislit interference experiment. Coherence  $\mathcal{C}$  had earlier been argued to be a good candidate for quantifying the wave nature of quantons in interference experiments, and a duality relation between  $\mathcal{C}$  and the path distinguishability  $\mathcal{D}_Q$ , based on UQSD, had been proved [23]. Here  $\mathcal{C}$  has been shown to be related to measured intensities in interference experiments, which puts it firmly as a good measure of wave nature of quantons in multislit interference experiments.

Additionally, it makes  $\mathcal{D}_Q + \mathcal{C} \leqslant 1$  a universal wave-particle duality relation, valid for interference experiments with any number of slits.

Apart from the issue of wave-particle duality, a method of measuring the coherence of any given beam of quantons has also been proposed.

# ACKNOWLEDGMENTS

T.P. is thankful to the Centre for Theoretical Physics at Jamia Millia Islamia for providing the facilities of the Centre during the course of this work. The authors thank an anonymous referee for suggesting an extension of the results.

[1] N. Bohr, Nature (London) 121, 580 (1928).  
[2] T. Qureshi and R. Vathsan, Quanta 2, 58 (2013).  
[3] W. K. Wootters and W. H. Zurek, Phys. Rev. D 19, 473 (1979).  
[4] D. M. Greenberger and A. Yasin, Phys. Lett. A 128, 391 (1988).  
[5] B.-G. Englert, Phys. Rev. Lett. 77, 2154 (1996).  
[6] S. Durr, T. Nonn, and G. Rempe, Phys. Rev. Lett. 81, 5705 (1998).  
[7] P. J. Coles, J. Kaniewski, and S. Wehner, Nat. Commun. 5, 5814 (2014).  
[8] J. A. Vaccaro, Proc. R. Soc. A. 468, 1065 (2012).  
[9] G. Jaeger, A. Shimony, and L. Vaidman, Phys. Rev. A 51, 54 (1995).  
[10] S. Durr, Phys. Rev. A 64, 042113 (2001).  
[11] G. Bimonte and R. Musto, Phys. Rev. A 67, 066101 (2003).  
[12] B.-G. Englert, Int. J. Quantum Inform. 6, 129 (2008).  
[13] G. Bimonte and R. Musto, J. Phys. A: Math. Gen. 36, 11481 (2003).  
[14] P. J. Coles, Phys. Rev. A 93, 062111 (2016).  
[15] M. A. Siddiqui and T. Qureshi, Prog. Theor. Exp. Phys. 2015, 083A02 (2015).  
[16] I. D. Ivanovic, Phys. Lett. A 123, 257 (1987).

[17] D. Dieks, Phys. Lett. A 126, 303 (1988).  
[18] A. Peres, Phys. Lett. A 128, 19 (1988).  
[19] G. Jaeger and A. Shimony, Phys. Lett. A 197, 83 (1995).  
[20] J. A. Bergou, U. Herzog, and M. Hillary, in Quantum State Estimation, edited by M. Paris and J. Reháček (Springer, Heidelberg, 2004), pp. 417-465.  
[21] L. Mandel, Opt. Lett. 16, 1882 (1991).  
[22] T. Baumgratz, M. Cramer, and M. B. Plenio, Phys. Rev. Lett. 113, 140401 (2014).  
[23] M. N. Bera, T. Qureshi, M. A. Siddiqui, and A. K. Pati, Phys. Rev. A 92, 012118 (2015).  
[24] M. Narhi, J. Turunen, A. T. Friberg, and G. Genty, Phys. Rev. Lett. 116, 243901 (2016).  
[25] P. Barcik and L. Hudcova, Radioengineering 22, 341 (2013).  
[26] U. Sinha, C. Couteau, T. Jennewein, R. Laflamme, and G. Weihs, Science 329, 418 (2010).  
[27] J. von Neumann, Mathematical Foundations of Quantum Mechanics (Princeton University Press, Princeton, 1955).  
[28] G. Dillon, Eur. Phys. J. Plus 127, 66 (2012).  
[29] S. Zhang, Y. Feng, X. Sun, and M. Ying, Phys. Rev. A 64, 062103 (2001).  
[30] D. Qiu, Phys. Lett. A 303, 140 (2002).