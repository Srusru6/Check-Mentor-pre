# Complementarity in the double-slit experiment: Quantum nonseparability and a quantitative statement of Bohr's principle

William K. Wootters and Wojciech H. Zurek

Center for Theoretical Physics and Center for Statistical Mechanics,

The University of Texas at Austin, Austin, Texas 78712

(Received 10 July 1978)

A detailed analysis of Einstein's version of the double-slit experiment, in which one tries to observe both wave and particle properties of light, is performed. Quantum nonseparability appears in the derivation of the interference pattern, which proves to be surprisingly sharp even when the trajectories of the photons have been determined with fairly high accuracy. An information-theoretic approach to this problem leads to a quantitative formulation of Bohr's complementarity principle for the case of the double-slit experiment. A practically realizable version of this experiment, to which the above analysis applies, is proposed.

# I. INTRODUCTION

In Einstein's version of the double-slit experiment, one can retain a surprisingly strong interference pattern by not insisting on a  $100\%$  reliable determination of the slit through which each photon passes. The analysis leading us to this conclusion involves the following considerations. The plate which receives the kick from each photon can either be stopped and its position measured, or released and its momentum measured. These two options give us two ways of subdividing the original ensemble of photons: (1) according to the measured position of the plate, and (2) according to the measured momentum of the plate. In case (1) each subensemble produces a perfect but differently shifted interference pattern. In case (2) each subensemble produces a smeared out pattern, but also gives us some information about the photons' paths. We will thus be led to study the following questions. Does our choice of what to measure affect the total interference pattern? Do we not violate the complementarity principle by measuring both the fringes and the kick? Can this kind of experiment be performed in practice?

A monochromatic wave passing through the familiar apparatus shown in Fig. 1 will produce a perfect interference pattern on plate 3. This kind of experiment was used by Young to demonstrate the wave nature of light, and by Davisson and Germer to demonstrate the wave nature of electrons. How does one reconcile this result with the fact that these same photons or electrons also have distinctly particlelike features, such as being individually detectable? For if they are indeed particles, then each one should go through a definite slit, and we should see a sum of single-slit diffraction patterns, rather than the observed interference pattern. This apparent

contradiction has served as an archetypal example of the wave-particle duality encountered in the microworld. As stated by Feynman, the double-slit experiment is a phenomenon "which has in it the heart of quantum mechanics; in reality it contains the only mystery" of the theory.3

The traditional resolution of this problem, consistent with the rest of quantum mechanics, states that unless we actually measure the path of each photon (for definiteness let us restrict our attention to photons; similar arguments apply to any other particle), we have no right to maintain that any given photon actually follows a definite path. Indeed, according to this view, if we were to succeed in measuring the path of each photon, then the interference pattern would be destroyed. Thus, we can observe either the wave properties or the particle properties of light, but not both simultaneously.

At the Fifth Solvay Congress at Brussels, Einstein devised a modification of the double-slit experiment by which he hoped to show the inconsistency of quantum mechanics. He considered an experiment in which the first screen (Fig. 1) is free to move up or down. Photons deflected toward a given slit always impart a characteristic momentum to screen 1. Thus, Einstein hoped that by measuring the momentum imparted one could determine the path of each photon without disturbing the interference pattern. If that were the case, then the complementarity principle would be proven false.

Bohr, in his defense of the consistency of quantum mechanics, pointed out that in order to deduce the slit through which the photon will pass from a knowledge of the final momentum of screen 1, one would also have to know the initial momentum of screen 1 to within an uncertainty  $\Delta p = (s / L)p = (h / \lambda)\times (s / L)(\lambda$  is the wavelength of the light), since this is the difference between the momenta

![](images/15cb3adc4089799f4fa128a750256ba484f37b6b38557198d6db06d538e1f9ad.jpg)  
FIG. 1. Path determination in the double-slit experiment, as proposed by Einstein (Ref. 2).

transferred by photons following the two possible paths to the final screen. But then the Heisenberg uncertainty principle requires that the initial position of screen 1 be uncertain by at least  $\Delta x\sim h / \Delta p = \lambda s / L$ . This is exactly what is needed to wash out the interference pattern, since this  $\Delta x$  is the spacing between fringes. In this way Bohr succeeded in defending the consistency of quantum mechanics.

The purpose of this paper is to examine Bohr's idea in detail; that is, we will find out exactly what interference pattern is produced when we attempt to determine the slit through which each photon passes. To do this, we shall represent the plate as a quantum-mechanical harmonic oscillator. The photon and the plate, having once interacted, become nonseparable parts of a single quantum-mechanical system. This forces us to consider the effect of our measurement of the plate on the photon wave function, and, consequently, on the interference pattern produced by these photons.

In the next section we shall derive the interference pattern attenuated as a result of our measurements on the position of the plate. There we shall also obtain the distribution of momentum of plate 1 associated with the relevant photons, that is, those which contribute to the image on the photographic plate.

In Sec. III we shall find what partial interference patterns correspond to ensembles of photons correlated to definite final momenta of the first plate. We shall also show that although these partial interference patterns depend on the measurements performed on the first plate, the total interference pattern (the sum of the partial interference patterns) is always the same.

In Sec. IV we shall find an analogy between this situation and the celebrated Einstein-Rosen-Podolsky paradox.

Section V discusses in terms of Shannon's theory

the information one can obtain about the slit through which the photon passed. The complementarity principle is stated in terms of an inequality, which sets the limit on the amount of retrievable information about the photons' paths (photon-particle) for an assumed sharpness of the interference pattern (photon-wave). A practically realizable version of Einstein's double-slit experiment is discussed in Appendix A. Appendix B gives details of the proof of the inequality derived in Sec. V.

# II. APPROXIMATE PATH-DETERMINATION

Let us now analyze in more detail the experiment described in Sec. I. Assuming that the Heisenberg uncertainty principle holds, let us ask exactly to what extent the interference pattern is smeared out if we insist on determining the path of each photon with a given accuracy. In the spirit of Bohr's rebuttal, we will represent screen 1 by a quantum-mechanical wave function.

The harmonic-oscillator wave function is a natural choice, since it satisfies (in its lowest-energy state) the equality

$$
\Delta x \Delta p = \hbar / 2,
$$

thus minimizing the cost (disturbance of photon's phase due to  $\Delta x$ ) of obtaining information about the photon's momentum with an error  $\Delta p$ . Both in the position  $(x)$  and wave-vector  $(k)$  representation it is given by a Gaussian:

$$
\psi (x) = \pi^ {- 1 / 4} a ^ {- 1 / 2} \exp (- x ^ {2} / 2 a ^ {2}), \quad \Delta x ^ {2} = a ^ {2} / 2, \tag {1}
$$

$$
\phi (k) = \pi^ {- 1 / 4} a ^ {1 / 2} \exp (- a ^ {2} k ^ {2} / 2), \quad \Delta k ^ {2} = 1 / (2 a ^ {2}),
$$

where  $k = p / \hbar$  is the  $x$  component of the wave vector of plate 1. [One sees that  $(\Delta x)(\Delta k) = \frac{1}{2}$ , the minimal irreducible demand of the uncertainty principle.]

The object of this section is to calculate the interference pattern one obtains when plate 1 has this wave function. But first we need to state the assumptions we will be making regarding the photon wave function in a single slit experiment. Let us consider for example the wave function at plate 3 of photons which have passed through slit A, slit B being closed for the time being. This wave function is

$$
\mu_ {A} (\xi) = f (\xi) \exp \left\{i (2 \pi / \lambda) \left[ L ^ {2} + (\xi - s / 2) ^ {2} \right] ^ {1 / 2} \right\},
$$

where  $f$  is a slowly varying envelope function whose presence is due to the fact that the slit is not infinitesimally narrow. For an ordinary slit,  $f$  would be the usual diffraction pattern. Moreover, one could also consider a slit containing one or another type of lens, and this would lead to a different envelope function. For ex-

ample, the process of apodization can be used to smooth out the diffraction pattern.12 In any case, all we ask is that there be a region  $|\xi| < \xi_0$  in which  $f(\xi)$  is essentially constant. We will then restrict our attention to a section of plate 3 where  $|\xi| < \xi_0$  and  $|\xi| \ll L$ . There the wave function can be approximated by

$$
\mu_ {A} (\xi) = f (0) e ^ {i \alpha (\xi)} e ^ {i k _ {0} \xi},
$$

where  $\alpha (\xi) = (2\pi /L)[L^2 +(s^2 /8) + (\xi^2 /2)]$  and  $k_{0}$

$\mathbf{\Phi} = (\pi s) / (L\lambda)$  . Similarly, the wave function for photons coming only from slit B is

$$
\mu_ {B} (\xi) = f (0) e ^ {i \alpha (\xi)} e ^ {- i k _ {0} \xi}.
$$

When we superimpose these two wave functions, the common factor  $e^{i\alpha(t)}$  does not contribute to the interference pattern. We will therefore omit this factor throughout the rest of this paper.

Finally, coming back to the double-slit experiment, since we have abandoned the usual normalization in considering only a part of plate 3, our convention will be to let the average of the interference pattern over one period be 1.

Just after each photon passes, we can measure exactly either the position or momentum of plate 1. Let us assume for now that we measure the position, and let us calculate the resulting interference pattern. In this case we know exactly where each photon starts its journey to plate 3. All photons starting at the same place  $x$  form a subensemble whose contribution  $I_{x}(\xi)$  to the total interference pattern is perfect, but shifted by an amount  $\Delta \xi = -x$ :

$$
I _ {x} (\xi) = 1 + \cos 2 k _ {0} (\xi + x),
$$

where  $k_{0} = \pi s / (\mathcal{L}\lambda)$ , and  $s$  and  $L$  are defined in Fig. 1. The number of photons in the subensemble characterized by the position  $x$  is proportional to  $|\psi (x)|^2$ . Therefore, the total interference pattern  $\mathfrak{F}(\xi)$  is just the sum of all the contributions from the various subensembles, weighted by  $|\psi (x)|^2$ :

$$
\mathfrak {F} (\xi) \propto \int d x | \psi (x) | ^ {2} I _ {x} (\xi) = 1 + e ^ {- k _ {0} ^ {2} a ^ {2}} \cos 2 k _ {0} \xi . \tag {2}
$$

This is our smeared-out interference pattern. Now how much can we determine about the paths of the photons using the same experimental arrangement, if we choose to measure the momentum of screen 1 rather than its position? Clearly the only photons which concern us are those which succeed in arriving at the final screen. Therefore, we will record only the momenta imparted by these photons. From the geometry of the apparatus we see that for these photons there are only two possible values of the wave vector imparted to screen 1, namely,  $\pm \pi s / (L\lambda) = \pm k_0$

(We have assumed here that  $a \ll s \ll L$ , and that all photons arrive at screen 1 with no initial momentum in the  $x$  direction.) The measured momentum of screen 1, however, will not be confined to these two values, even if our measurements are exact. As before, the uncertainty comes from the fact that the initial momentum of the plate is not definite, but rather has a distribution given by  $|\phi(k)|^2$ . If the plate has initial wave vector  $\pmb{k}$ , then its final wave vector  $\kappa$  (after the plate has collided with one of the photons under consideration) can have either of the two values  $\kappa = k \pm k_0$ . The total recorded distribution  $\mathfrak{D}(\kappa)$  of wave numbers of the plate will be the sum of all the partial distributions  $D_{k}(\kappa)$ , weighted by  $|\phi(k)|^2$ :

$$
\begin{array}{l} D _ {k} (\kappa) = \frac {1}{2} \left[ \delta \left(\kappa - k + k _ {0}\right) + \delta \left(\kappa - k - k _ {0}\right) \right], \\ \mathfrak {D} (\kappa) = \int d k | \phi (k) | ^ {2} D _ {k} (\kappa) \tag {3} \\ = \left[ a / \left(2 \pi^ {1 / 2}\right) \right] \left\{\exp \left[ - a ^ {2} \left(\kappa + k _ {0}\right) ^ {2} \right] \right. \\ + \exp \left[ - a ^ {2} \left(\kappa - k _ {0}\right) ^ {2} \right] \}. \\ \end{array}
$$

It is convenient to define a dimensionless "smudging parameter"  $u = ak_{0}$ . From Eq. (2) it is clear that this is the parameter characterizing the suppression of the interference pattern. It is also a measure of the uncertainty of our determination of the path of each photon. To clarify these points, let us choose a particular value of  $u$ , namely,  $u = 0.4769$ . If we use this value of  $u$  to calculate the interference pattern according to Eq. (2), and the distribution of measured momenta according to Eq. (3), then the results are those shown in Fig. 2.

If the measured momentum is positive, then we will guess that the photon passed through slit A; if it is negative, then we will guess that the photon passed through slit B. Clearly some of our guesses will be wrong—there are photons that have positive values of measured momentum even though their actual momentum was negative and they went through slit B. The fraction of photons which misbehave in this way equals the fraction  $F(u)$  of our guesses which are wrong. This fraction is just the ratio of the area under the "tails" of the Gaussians (that is, the parts lying on the wrong side of  $\kappa = 0$ ) to the total area under  $\mathfrak{D}(\kappa)$ :

$$
\begin{array}{l} F (u) = \left(a / \pi^ {1 / 2}\right) \int_ {- \infty} ^ {0} \exp \left[ - a ^ {2} \left(\kappa - k _ {0}\right) ^ {2} \right] d \kappa \\ = \left(1 / \pi^ {1 / 2}\right) \int_ {u} ^ {\infty} e ^ {- \eta^ {2}} d \eta \\ = \frac {1}{2} [ 1 - \operatorname {e r f} (u) ]. \\ \end{array}
$$

![](images/810b48fdf024f876acde954c4edc344fa65db4db15d6b69910dfd338a074728c.jpg)

![](images/92031463b59cff22a406918877501daab1f1ea4951a22c09db07e8ff86938be5.jpg)  
FIG. 2. Results of the approximate momentum measurement in the double-slit experiment, for the smudging parameter  $u = 0.4796$ . (a) Distributions of measured momenta. (b) The corresponding total interference patterns.

Our particular value of  $u$  was chosen so that  $F(u) = 0.25$ . That is, out of four guesses, one is usually wrong. Thus, we have done a fairly good (but not perfect) job of determining the path of each photon, and therefore we might expect an almost completely obliterated interference pattern. But in fact this is not true. Figure 2(b) shows that we still get an almost perfect interference pattern; the crest-to-valley ratio  $R(u)$  of intensities is  $R(u) = [1 + \exp(-u^2)] / [1 - \exp(-u^2)] = 8.8$  for our value of  $u$ . Have we not then succeeded in observing both particlelike and wave-like properties of the same photons?

One will no doubt object: The interference pattern  $\mathfrak{F}(\xi)$  was calculated for an experiment in which the position of screen 1 was measured. The path determination depended on the wave vector  $k$  of the photon inferred from the measured momentum of the screen 1. But these two measurements cannot both be performed for the same photons, and so Figs. 2(a) and 2(b) do not refer to the same experiment. Hence, in accord with the Copenhagen interpretation of quantum mechanics, there is no paradox. The complementarity principle does not prevent photons from behaving once as waves and once as particles. It only states that the same photon should not reveal this "split personality" in the same experiment.

The above objection is certainly valid. However, we shall see in the next section that even when we perform the momentum measurements on screen 1, obtaining information about the slit each photon chooses, the same total interference pattern  $\mathfrak{F}(\xi)$  forms on the photosensitive screen 3. That is, Figs. 2(a) and 2(b) describe the outcome of the same hypothetical experiment.

# III. CORRELATION BETWEEN THE MEASURED MOMENTUM AND THE CORRESPONDING INTERFERENCE PATTERN

In this section we will analyze the experiment in which the momentum of screen 1 is measured rather than the position. From each momentum measurement we will infer the relative probabilities of the photon's passing through one slit or the other. In practice, we cannot actually perform this momentum measurement with the necessary accuracy. However, as is shown in Appendix A, one can perform an experiment which will give the desired probabilities. The analysis in this section is sufficiently general to be applicable to the experiment considered in Appendix A.

In our experiment (Fig. 1), photons entering the apparatus change the momentum of screen 1. Then some of them pass through the slits in plate 2, as announced by a flash of light emitted by a scintillator on plate 3. We wait for these scintillations, and immediately record the momentum of plate 1 and the position of the scintillation. That is, our record contains for each photon two numbers: the measured position on plate 3 and the measured momentum. Of course, we can obtain from this record both the interference pattern  $\mathfrak{F}(\xi)$  and the distribution  $\mathfrak{D}(\kappa)$  of measured photon momenta. Indeed, these two distributions could have been obtained directly, without keeping a photon-by-photon record. The fact that each scintillation is actually associated with a definite kick to plate 1 can have no effect on the shapes of  $\mathfrak{F}(\xi)$  and  $\mathfrak{D}(\xi)$ . Given that we do have a photon-by-photon record, we find  $\mathfrak{F}(\xi)$  simply by counting all the photons that landed in the interval  $\xi - \xi + d\xi$ .  $\mathfrak{D}(\kappa)$  is clearly constructed in an analogous manner.

But a new question which we have not considered so far comes to our attention. We can look for the distribution of scintillations arising only from those photons which have been associated with a definite measured momentum  $\kappa$  of the plate 1. What kind of interference pattern will these photons produce? The first thing to notice is that these partial interference patterns  $i_{\kappa}(\xi)$  cannot be independent of  $\kappa$ ; that is, they cannot all have the shape of the total interference pattern. For

if we consider only the photons with a high-enough  $\kappa$ , we could improve indefinitely our chances of a correct determination of their paths; that is, by increasing  $\kappa$  we would be able to tell with as small a margin of error as we wish through which of the two slits the photon has passed. In this way we would be able to get around Bohr's resolution of the double-slit paradox.

Therefore, a correlation between  $\kappa$  -the measured value of the plate's momentum-and  $i_{\kappa}(\xi)$  -the partial interference pattern-seems inescapable. To find out the shape of  $i_{\kappa}(\xi)$  , let us consider the fraction of error  $f(\kappa)$  defined as the ratio of the probability of the photon's passing through slit A to the probability of passing through slit B,

$$
\begin{array}{l} f (\kappa) = p _ {A} / p _ {B} \\ = \exp \left[ - a ^ {2} \left(k + k _ {0}\right) ^ {2} \right] / \exp \left[ - a ^ {2} \left(k - k _ {0}\right) ^ {2} \right]. \tag {4} \\ \end{array}
$$

Here  $p_A$  and  $p_B$  are defined by this formula together with the relation  $p_A + p_B = 1$ . This ratio  $f(\kappa)$  clearly represents the uncertainty in our knowledge about the two possibilities from which the photon can choose.

The same situation and identical error ratio appear when we consider a double-slit experiment in which the two slits have different areas. The uncertainty ratio  $f$  will in this case be expressed by the ratio of the two areas. In this situation the interference pattern can be immediately written:

$$
i _ {f} (\kappa) = 1 + 2 p _ {A} ^ {1 / 2} p _ {B} ^ {1 / 2} \cos 2 k _ {0} \xi . \tag {5}
$$

It is natural to expect that if our correlation measurement is characterized by the same value of  $f$  as this unequal-double-slit experiment, then it should yield the same interference pattern. Therefore,

$$
i _ {\kappa} (\xi) = 1 + 2 p _ {A} ^ {1 / 2} (\kappa) p _ {B} ^ {1 / 2} (\kappa) \cos 2 k _ {0} \xi . \tag {6}
$$

These formulas (5) and (6) are certainly compatible with quantum mechanics and with the uncertainty and complementarity principles. What do they predict for a definite value of  $f$ ? For instance, let us take  $f = \frac{99}{1}$ ; that is, out of 100 photons we expect 99 of them to pass through the more likely slit. An accuracy of  $99\%$  is certainly high, and one would expect that such a measurement should destroy the interference pattern. But a straightforward calculation shows that the crest-to-valley ratio  $R$  given by  $R = (1 + 2p_A^{1/2}p_B^{1/2}) / (1 - 2p_A^{1/2}p_B^{1/2})$  equals approximately  $\frac{3}{2}$ . Despite the fact that we know with  $99\%$  certainty the paths of the photons, they still have strong wavelike properties. In a sense we have localized the cause of what appeared to be a violation of the

![](images/fe45ee53ccd13a7d273888e6099f51ee1c72e312d2f30a0ed42c3d1c3861a5f4.jpg)

![](images/876c1573b4233caf05e598980925e385d9630794fbe7cde591df5007317163d4.jpg)  
FIG. 3. Partial-interference patterns  $i_{\kappa}(\xi)$  corresponding to the different measured momenta  $\kappa$  and the resulting total interference pattern  $\mathfrak{F}(\xi)$ , according to formula (7).

complementarity principle.

To make sure that our present reasoning is consistent and that our apparent paradox survives the objection raised at the end of Sec. I, let us add up all the partial interference patterns, all the differently smudged-out contributions. According to Eqs. (3) and (5), each of them can be written as

$$
\begin{array}{l} i _ {\kappa} (\xi) = 1 + \frac {2 \exp \left[ - a ^ {2} \left(\kappa^ {2} + k _ {0} ^ {2}\right) \right]}{\exp \left[ - a ^ {2} \left(\kappa - k _ {0}\right) ^ {2} \right] + \exp \left[ - a ^ {2} \left(\kappa + k _ {0}\right) ^ {2} \right]} \\ \times \cos 2 k _ {0} \xi . \\ \end{array}
$$

Weighting them by  $\mathfrak{D}(\kappa)$  and adding them together, as represented in Fig. 3, we obtain

$$
\begin{array}{l} \mathfrak {F} (\xi) = \int \mathfrak {D} (\kappa) i _ {\kappa} (\xi) d \kappa \\ = 1 + e ^ {- a ^ {2} k _ {0} \xi^ {2}} \cos 2 k _ {0} \xi . \tag {7} \\ \end{array}
$$

This is exactly what we obtained previously [Eq. (1)] by adding perfect, but shifted, interference patterns. This way of obtaining the total interference pattern is illustrated symbolically in Fig. 3.

# IV. EINSTEIN-ROSEN-PODOLSKY "PARADOX" IN THE DOUBLE-SLIT EXPERIMENT

Let us recall the two possible measurements one can perform using the experimental set-up of Fig. 1: (1) Measure the position of screen 1-

get perfect but shifted partial interference patterns. (2) Measure the momentum of screen 1—get smeared out but centered partial interference patterns.

Notice that in both cases the measurement on screen 1 is performed after the photon has interacted with it. How does the photon know in which partial interference pattern to fall? How can it know what we decided to measure when it is already separated from the plate by a large distance?

There is no doubt that our choice affects the wave function of the photon: (1) If we measure plate 1 to have position  $x$ , the photon arrives at plate 3 in the state

$$
\mu_ {x} (\xi) \propto e ^ {i k _ {0} (\xi + x)} + e ^ {- i k _ {0} (\xi + x)}. \tag {8a}
$$

(2) If we measure plate 1 to have momentum  $\kappa$ , the photon arrives at plate 3 in the state

$$
\nu_ {\kappa} (\xi) \propto p _ {A} ^ {1 / 2} (\kappa) e ^ {i k _ {0} \xi} + p _ {B} ^ {1 / 2} (\kappa) e ^ {- i k _ {0} \xi}. \tag {8b}
$$

This effect of our measurement on the photon's wave function can be understood in the following way. After the photon has interacted with plate 1, it no longer has an individual wave function;

here is only the state  $\Psi$  of the combined system

plate 1 + photon). This combined state can be expanded in terms of any complete set of orthogonal states of plate 1. For example, if  $\sigma_{x}$  is the eigenstate of position of plate 1 corresponding to the eigenvalue  $x$ , we can always write the combined state as

$$
\Psi = \int d x c _ {x} \mu_ {x} \otimes \sigma_ {x}, \tag {9a}
$$

where the photon states  $\mu_{x}$  are all normalized but not necessarily orthogonal, and  $|c_x|^2$  is the probability distribution of the plate's position  $x$ . Alternatively, we can use the set of eigenstates of momentum of plate 1,  $\{\tau_{\kappa}\}$ , as our basis, in which case  $\Psi$  is written as

$$
\Psi = \int d \kappa d _ {\kappa} \nu_ {\kappa} \otimes \tau_ {\kappa}. \tag {9b}
$$

Thus, each plate eigenstate  $(\sigma_{x}$  or  $\tau_{\kappa})$  has its corresponding photon state. When we measure the plate's position and obtain the value  $x$ , the photon is forced into the state  $\mu_{x}$ , and similarly for momentum. In this way our choice affects the wave function of the photon.

Our object now is to identify the various quantities which appear in Eqs. (9), and thus to check that this idea of the combined state is consistent with the analysis of the previous sections. For definiteness we will write  $\Psi$  as a function of the positions of plate 1 and the photon, to which we assign the symbols “ $z$ ” and “ $\xi$ ” respectively (“ $x$ ”

is reserved as a lable for eigenfunctions; hence the necessity of introducing "  $z ^ { \prime \prime } )$  .According to our previous analysis,  $\mu_{x}$  and  $\nu_{\kappa}$  should be given by Eqs. (8), and the other quantities in Eqs. (9) should be interpreted as follows:

$$
\begin{array}{l} c _ {x} = \psi (x) = \frac {1}{\pi^ {1 / 4} a ^ {1 / 2}} e ^ {- x ^ {2} / 2 a ^ {2}} [ \text {s e e E q . (1)} ], \\ \sigma_ {x} (z) = \delta (z - x), \\ d _ {\kappa} = \mathbb {D} ^ {1 / 2} (\kappa) [ \text {s e e E q . (3)} ], \\ \tau_ {\kappa} (z) = e ^ {i \kappa z}. \\ \end{array}
$$

Inserting these identifications into Eqs. (9), we obtain the following expressions for  $\Psi$ :

According to Eq. (9a),

$$
\begin{array}{l} \Psi = \frac {1}{2 ^ {1 / 2} a ^ {1 / 2} \pi^ {1 / 4}} \int d x e ^ {- x ^ {2} / 2 a ^ {2}} \left[ e ^ {i k _ {0} (\xi + x)} + e ^ {- i k _ {0} (\xi + x)} \right] \\ \times \delta (z - x); \tag {10a} \\ \end{array}
$$

according to Eq. (9b),

$$
\begin{array}{l} \Psi = \frac {a}{2 \pi^ {1 / 4}} \int d \kappa \mathfrak {D} ^ {1 / 2} (\kappa) \left[ p _ {A} ^ {1 / 2} (\kappa) e ^ {i k _ {0} \xi} + p _ {B} ^ {1 / 2} (\kappa) e ^ {- i k _ {0} \xi} \right] \\ \times e ^ {i \kappa z}, \tag {10b} \\ \end{array}
$$

where the constant factors have been chosen so that  $\Psi$  conforms to our normalization convention; i.e.,  $\int dz|\Psi|^2$  is a function of  $\xi$  whose average value is 1. One can verify that these two expressions for the combined wave function are indeed equal. This is in fact the real justification for our identification of  $\nu_{\kappa}$  [Eq. (8b)] as the wave function of photons corresponding to plate momentum  $\kappa$ , and hence also for our expression (6) for the partial interference pattern.

In Secs. II and III we found that although our choice of what to measure (about plate 1) does affect the photon's wave function, it does not affect the total interference pattern. From the point of view of the present section, this result is seen quite easily. The total interference pattern is

$$
f (\xi) = \int d z | \Psi (z, \xi) | ^ {2},
$$

which is independent of any measurements made on plate 1.

The situation described here and the analysis outlined above are essentially the same as in the Einstein-Podolsky-Rosen "paradox."4,5,6 There too what we choose to measure on one system affects the wave-function of another system far away. But the final distribution of measured values of the far away system is again independent of our choice. Thus in discussing Einstein's

double-slit experiment we have encountered the classic nonseparability feature of quantum mechanics.7

To make sure that the analogy is complete, one may consider a situation where the photon is first localized on screen 3, and the position (or

momentum) of screen 1 is measured only afterwards. In that case the wave function of the photon is simply  $\delta (\xi -\xi_0)$ . It is readily seen that the total wave function  $\Psi (z,\xi)$  can be decomposed into a wave function of a photon localized at  $\xi_0$  and a wave function describing plate 1:

$$
\Psi (z, \xi) = \int d \xi_ {0} \left\{\delta (\xi - \xi_ {0}) \right\} \otimes \left\{(2 a) ^ {- 1 / 2} \pi^ {- 1 / 4} \exp (- z ^ {2} / (2 a ^ {2})) \left[ \exp (i k _ {0} (\xi_ {0} + z)) + \exp (- i k _ {0} (\xi_ {0} + z)) \right] \right\}.
$$

From this expression a wave function, and, consequently, a corresponding probability distribution correlated to an ensemble of photons landing at the given coordinate value  $\xi_0$  can be obtained.

That is, the measurement can be first performed either on the plate 1 or on the photon, and the obtained information will allow us to determine what is the probability distribution of the other, yet unmeasured part of an inseparable system.

# V. INFORMATION AND THE COMPLEMENTARITY PRINCIPLE

In the preceding sections we have presented a result which, although not paradoxical, was nevertheless surprising (that is, that one can make a fairly precise determination of the slit through which each photon comes with only a slight disturbance of the interference pattern). It is worthwhile to notice that the two limiting cases of Einstein's version of the double-slit experiment do not surprise us at all. These are the cases in which the smudging parameter  $u$  takes the values zero (no determination is made of the path of the photon) and infinity (each photon's path is determined completely). As we can see from Eq. (1), in the former case the interference pattern is perfect, while in the latter case it is completely washed out. This result has been known for so long that we have learned how to talk about it, and it is therefore no longer surprising.

The apparent paradox of our present example clearly arises from the fact that we are considering an intermediate situation in which one obtains some information about the photons' paths, and still retains an interference pattern having some degree of clarity. The problem is that we lack a good way of talking about such a situation, and we have no simple rule which tells us what to expect. The aim of this section is to fill this gap. We will find that information theory

provides a good language for dealing with an imprecise path determination, and this will lead us naturally to a rule which defines the extent to which the two complementary aspects of light (wave and particle) may be manifested simultaneously.

Intuitively, one expects that if the interference pattern has a certain sharpness of definition, then there must be some limit on the amount of information which could have been obtained regarding through which slit each photon passed. What we wish to do here is simply to make this statement more precise. For this we need a way to quantify "information." We will use the measure of information discovered by Shannon, which has all the mathematical properties one usually requires of information, and which has been fruitfully applied to a wide variety of problems, including quantum mechanics itself. Its most general definition is the following: If a system can be in one of  $N$  possible states, but if we know only the probabilities  $p_i$  of its being in each state  $i$ , then the amount of information we lack about the system is the positive number

$$
H = - \sum_ {i = 1} ^ {N} p _ {i} \ln p _ {i}.
$$

In our experiment we can consider each photon as a system with two possible states (in the above sense): passing through slit A and passing through slit B. If we determine the probabilities of these two paths to be  $p_A$  and  $p_B$  (where  $p_A + p_B = 1$ ), then the information we lack about the path of that photon is

$$
H = - \left(p _ {A} \ln p _ {A} + p _ {B} \ln p _ {B}\right). \tag {11}
$$

As an example, we note that if we know nothing about the path of a photon, that is, if each slit is equally likely, then the amount of information we lack is

$$
H _ {0} = - \left(\frac {1}{2} \ln \frac {1}{2} + \frac {1}{2} \ln \frac {1}{2}\right) = \ln 2.
$$

Now we are ready to formulate the problem.

Suppose we are interested in obtaining an interference pattern with a certain crest-to-valley ratio of intensities, say, 8.8 as in the above example. Notice that there are many ways to make such a pattern. We list a few of them here:

(1) Perform the experiment described in Sec. II, in which the measured momentum of plate 1 is used to judge the path of each photon. In this case we have seen that the paths of some photons will be better determined than the paths of others, depending on the value  $\kappa$  of the measured momentum.

(2) Keep all the plates fixed, but let one of the slits be bigger than the other. We have seen in Sec. III that the resulting pattern will again be partially smeared out, and that the same pattern arises from a subensemble of photons all having the same value of  $\kappa$ . The crucial thing about these experiments is that we cannot differentiate further among the photons. There is only one subensemble (the whole ensemble); each photon gives us the same amount of information; the photons are in a pure state.

(3) Allow some of the photons to pass through one slit only (the other being blocked), making a completely smeared out pattern; then open the other slit, allowing the rest of the photons to interfere perfectly. The sum of the two patterns can be arranged to have the desired crest-to-valley ratio.  
(4) Make no measurement of the photons' paths, but let the slit in plate 1 be of a size comparable to the spacing between fringes, so that the resulting pattern is smudged.

The point is that the amount of information one obtains about the photons' paths varies from one case to another, even though the "summed-up interference pattern" is the same in each case. For example, in case 4 one loses some of the sharpness of the pattern without gaining any information at all.

The question naturally arises: Of all possible methods of generating this particular interference pattern, which one gives us the most information regarding the photons' paths? If we can find this method, then we will have found the limit on the amount of information which can be obtained, given that we insist on a certain sharpness of definition of the pattern. We will then have to admit that no amount of cleverness can produce an experiment in which the information gained exceeds this limit.

We will find that this question is indeed answerable, and that the best method turns out to be experiment (2) above, in which the photons are in a pure state. To see this, we first need to write down a general expression for information which

applies to all the experiments we are considering.

A typical experiment can be described as follows. As in Sec. III, all the photons can be divided into different subensembles, such that the photons of a given subensemble all have the same probability of passing through slit A. In Sec. III we labeled the subensembles by the measured quantity  $\kappa$ , and we called the probabilities of the two paths  $p_A(\kappa)$  and  $p_B(\kappa)$ . In the general case which we are considering now, it will be more convenient simply to label each subensemble by its values of  $p_A$  and  $p_B$ . To simplify the notation let us define  $\gamma = p_A$ , from which it follows that  $p_B = 1 - \gamma$ . For our purpose, each experiment is completely characterized once we specify the fraction of the photons in each subensemble. Therefore, let  $\rho(\gamma)d\gamma$  be the fraction of the photons whose probabilities of going through slit A are between  $\gamma$  and  $\gamma + d\gamma$ .

According to Eq. (7) the information we lack about the path of each photon of the subensemble  $\gamma$  is

$$
H (\gamma) = - \left[ \gamma \ln \gamma + (1 - \gamma) \ln (1 - \gamma) \right].
$$

The total information we lack is the sum of  $H(\gamma)$  over all photons. To obtain the average information  $H$  we lack per photon, we divide this sum by the total number of photons, arriving at the formula

$$
\begin{array}{l} H = \int_ {0} ^ {1} d \gamma \rho (\gamma) H (\gamma) \\ = - \int_ {0} ^ {1} d \gamma \rho (\gamma) [ \gamma \ln \gamma + (1 - \gamma) \ln (1 - \gamma) ]. \tag {12} \\ \end{array}
$$

Now we would also like to write an expression for the interference pattern  $\mathfrak{F}(\xi)$  in terms of the function  $\rho (\gamma)$ . As in Sec. III [Eq. (6)], we again associate with each subensemble  $\gamma$  a partial interference pattern  $i_{\gamma}(\xi)$ , given by

$$
i _ {\gamma} (\xi) \propto 1 + 2 \gamma^ {1 / 2} (1 - \gamma) ^ {1 / 2} \cos 2 k _ {0} \xi .
$$

Notice that we have assumed the best possible  $i_{\gamma}(\xi)$ . One could always be sloppy (as in experiment 4) and obtain a more smudged pattern. Furthermore, we have assumed that all of the contributions  $i_{\gamma}$  from the various subensembles are not shifted relative to each other; that is, they all have their maxima at the same places. For our purpose here, these assumptions entail no loss of generality; we are trying to get as good a pattern as we can in order to investigate the theoretical limit on the amount of information which can be obtained. We now generalize Eq. (7), and find that the total interference pattern is

$$
\mathfrak {F} (\xi) = \int_ {0} ^ {1} d \gamma \rho (\alpha) i _ {\gamma} (\xi) = 1 + S \cos 2 k _ {0} \xi , \tag {13}
$$

where

$$
S \equiv 2 \int_ {0} ^ {1} d \gamma \rho (\gamma) \gamma^ {1 / 2} (1 - \gamma) ^ {1 / 2}. \tag {14}
$$

From Eq. (13) it is clear that the quantity  $S$  is a measure of the sharpness of definition of the interference pattern. In terms of  $S$ , the main problem of this section can now be stated very simply: For a given value of  $S$ , what distribution  $\rho$  minimizes  $H$ , and what is this minimum value of  $H$ ?

Our answer, whose proof is outlined in Appendix B, is that the best  $\rho$  is

$$
\rho_ {0} (\gamma) = \delta (\gamma - \gamma_ {0}), \tag {15}
$$

where  $\gamma_0$  is determined by the chosen sharpness of the interference pattern. In fact, according to Eqs. (13)-(15),

$$
S = 2 \gamma_ {0} ^ {1 / 2} (1 - \gamma_ {0}) ^ {1 / 2},
$$

or, if we solve this for  $\gamma_0$

$$
\gamma_ {0} = \frac {1}{2} [ 1 \pm (1 - S ^ {2}) ^ {1 / 2} ]. \tag {16}
$$

What Eq. (15) says is that if we wish to get as much information as we can about the photons' paths, the best experiment we can do is of the kind exemplified by experiment 2, where all photons have the same probability  $\gamma_0$  of passing through slit A, and are thus in a pure state. (Actually, as is shown in Appendix B, there is a one-parameter family of distributions which are as good as  $\rho_0$ ; they differ from  $\rho_0$  only in that some of the photons have their probabilities  $p_A$  and  $p_B$  reversed.) We have thus answered the first part of our question.

For an interference pattern of given sharpness  $S$ , the amount of information  $H(S)$  one gives up when he uses this "best" method can be found from Eqs. (12) and (15) (and this answers the second part of our question):

$$
H (S) = - \left[ \gamma_ {0} \ln \gamma_ {0} + \left(1 - \gamma_ {0}\right) \ln \left(1 - \gamma_ {0}\right) \right], \tag {17}
$$

where  $\gamma_0$  is given by Eq. (16). The main result of this section is that one must forfeit at least this much information about the photons' paths in order to obtain an interference pattern of sharpness  $S$ . That is,

$$
H \geqslant H (S). \tag {18}
$$

Let us now apply this result to our original experiment (experiment 1), with the smudging parameter  $u$  having the same value as before. The interference pattern is [Eq. (2)]

$$
\begin{array}{l} \mathcal {F} (\xi) = 1 + e ^ {- u ^ {2}} \cos 2 k _ {0} \xi \\ = 1 + (0. 7 9 6) \cos 2 k _ {0} \xi . \tag {19} \\ \end{array}
$$

That is,  $S = 0.796$ . The value of  $H(S)$ , given by

Eqs. (17) and (16), is then  $H(S) = 0.497$ . This number becomes more meaningful if we compare it to the total amount of information  $H_0 = \ln 2$  available about each photon:

$$
H (S) / H _ {0} = 0. 7 1 7.
$$

Thus, according to our result, in order to obtain the interference pattern (19), we must sacrifice at least  $71.7\%$  of the available information regarding the photons' paths.

This is the minimum amount of information we must sacrifice. How much information do we infact give up when we perform Einstein's experiment? The easiest way to answer this is to return to the  $\kappa$  notation. According to Eq. (4), the probability  $p_A(\kappa)$  that a photon in the subensemble  $\kappa$  will pass through slit A is

$$
p _ {A} (\kappa) = \frac {\exp \left[ - a ^ {2} \left(\kappa + k _ {0}\right) ^ {2} \right]}{\exp \left[ - a ^ {2} \left(\kappa + k _ {0}\right) ^ {2} \right] + \exp \left[ - a ^ {2} \left(\kappa - k _ {0}\right) ^ {2} \right]},
$$

and  $p_{B}(\kappa) = 1 - p_{A}(\kappa)$ . The average information we lack per photon is

$$
H = \int_ {- \infty} ^ {\infty} d \kappa \mathfrak {D} (\kappa) \left[ p _ {A} (\kappa) \ln p _ {A} (\kappa) + p _ {B} (\kappa) \ln p _ {B} (\kappa) \right],
$$

where the distribution  $\mathfrak{D}$  of measured momentum  $\kappa$  is given by Eq. (3). Upon evaluating this integral numerically, we find that

$$
H / H _ {0} = 0. 7 2 8.
$$

This is only slightly greater than the minimum value  $H(S) / H_0 = 0.717$ , associated with this interference pattern. Thus, Einstein's experiment gives almost as much information as one could possibly get [which, by the way, is not very much in this case—only  $28.3\%$  (i.e.,  $1 - 71.7\%$ ) of the available information; this is perhaps in better agreement with what we might expect for this interference pattern, as compared to the expression "75% accuracy" which we used earlier]. But the point is that the amount of information one can get is limited by  $H(S)$ .

Let us conclude this section with a clear statement of the complementarity principle in the language of information theory, as it applies to the double-slit experiment. The sharpness of the interference pattern can be regarded as a measure of how wavelike the light is, and the amount of information we have obtained about the photons' trajectories can be regarded as a measure of how particlelike it is. Equation (14) can be expressed in words as follows: (Information lost about the photons' paths)  $\geq$  (information  $H(S)$  lost in pure-state experiment giving the same interference pattern).  $H(S)$  [given by Eqs. (17) and (16)] increases monotonically as the sharpness increases. The above inequality is thus a pre

cise statement of the following fact: The more clearly we wish to observe the wave nature of light, the more information we must give up about its particle properties.

# ACKNOWLEDGMENTS

We would like to thank Professor John Archibald Wheeler, who encouraged us to pursue this project, for many stimulating discussions and for reading the manuscript. We would also like to thank Dilip K. Kondepudi for sharing with us some of his ideas on the double-slit experiment.

# APPENDIX A: MULTIPLATE DOUBLE-SLIT EXPERIMENT

As we have discussed in the introduction, Einstein proposed to modify the double-slit experiment in such a way that in principle one should be able to determine through which slit the photon passed. In this appendix we shall propose an arrangement where one would be able to carry out an equivalent experiment in practice

The major difficulty encountered in an attempt to realize Einstein's proposal is the error in the determination of the lateral kick. This measurement may be performed by releasing any of the three screens involved (we do not consider any causality effects in this appendix), and measuring the momentum of the screen after its interaction with the photon. But regardless of the particular screen, the square average momentum of the random, noiselike Brownian motion is larger than the value of the kick we want to determine. For the case where the photographic plate is released Wheeler<sup>13</sup> recently calculated that the resulting fluctuations in the value of the momentum are 12 orders of magnitude larger than the signal itself. We are consequently forced to look for some alternative indicator of the particle path that would replace the momentum kick.

The direction was all that the kick could have told us. Can we determine the direction of the photon in a straightforward manner? To do it we propose the experimental arrangement envisaged in Fig. 4. There, the usual photographic plate is replaced by the set of nontransparent, thin "photoplates" covered with the photographic emulsion on both sides. In such a "multiplate double-slit" experiment, when the photon blackens a grain of sliver bromide on the top (bottom) of one of the photoplates, we expect that it came from the top (bottom) slit. The analysis of the experiment is simplest when the photoplates are occupying the region  $\Delta \xi \ll s$ , that is, when they lie close to the optical axis of the double-slit apparatus. We shall assume that this is true in the

![](images/fb8c1345a26c2d2716efa2525c867f94b643f0e1a8b62cc6f37239556121044e.jpg)  
FIG. 4. Multiplate double-slit experiment.

rest of this section unless otherwise stated.

Let us now consider only those plates in the positions where previously, with the help of the normal photographic plate, maxima and minima of the perfect interference pattern

$$
\mathfrak {F} (\xi) \propto 1 + \cos 2 k _ {0} \xi
$$

were observed. Will the plates placed at  $\xi = 2n\pi / 2k_0$  become dark while the ones at  $\xi = [(2n + 1)\pi] / 2k_0$  remain untouched by the radiation? Shall we recover the perfect interference pattern? If so, quantum mechanics would prove inconsistent: The same photon goes through two slits producing an interference pattern and yet it comes from the top (bottom) slit.

What other outcomes of the experiment are conceivable? Let us examine more carefully the possible fate of photons landing on the photoplates to establish if: (1) The interference pattern may disappear—and all the plates will be “grey.”

(2) The fact that the photon lands on the top (bottom) of the photoplate does not yet allow us to be sure from which slit it came.

While the experiment remains to be done, one really expects (1) to occur. The reason for it in a carefully performed multiplate double-slit experiment is clear enough: The photons coming from two different slits never meet on the same side of the photoplate—they can never interfere. We can conclude this already from the wave optics interpretation, unless the wave representing the

electrical field of the photon can get in some fashion from the bottom slit to the top side of the photoplate.

If this "landing on the wrong side" does occur, then we have the situation described by (2). Physical reasons for that effect can be found in the reflections that direct the ray coming from the top slit to the bottom side of the photoplate [see Fig. 5(a)]. Consequently, the probability of detecting a photon from a certain slit changes accordingly. We can use  $p_A(x)$  as in Sec. III, to denote the probability that a photon from the top slit will arrive at the position  $x$ , where  $x$  is defined in Fig. 5(a). As before, we assume  $p_A(x) + p_B(x) = 1$ . We can also assume that the phases of the photons arriving at the given  $x$  are not randomized through the undergone reflection processes.

With this in mind one does not encounter any difficulties in carrying out an analysis similar to the one performed in Sec. III. The only important change is the different shape of  $p_A(x)$  and  $p_B(x)$ , which is qualitatively shown in Fig. 5(b). What we shall measure here can be described in terms of the partial interference pattern and total interference pattern. For when we record the intensity at a certain position  $x$  on each plate, we sample at a set of discrete points  $\{\xi_i\}$  (which are the positions of the photoplates) the partial interference pattern  $i_x(\xi)$ . As in Sec. III, from the knowledge of  $p_A(x)$  and  $p_B(x)$ , we have

![](images/670eb5ec1a369613942456b853c3ee30dc1e39334e10461fdfca3cbfe92c9460.jpg)

![](images/7c02a8270d13ec45a5d22f74a0dc43a8c9fe8292bee50aff0e1c0125168842d6.jpg)  
FIG. 5. Origin of the residual interference pattern in the multiplate double-slit experiment. (a) The paths of the photons and the resulting interference pattern. (b) Probabilities of arrival from one of the slits as a function of  $x$ .

$$
i _ {x} (\xi) = 1 + p _ {A} ^ {1 / 2} (x) p _ {B} ^ {1 / 2} (x) \cos 2 k _ {0} \xi .
$$

This formula is true since all the photons landing at a certain  $x$  have the identical probabilities  $p_A(x)$  and  $p_B(x)$ , and for that reason constitute one "subensemble" in the sense of Sec. III. Thus, we have succeeded in designing a measurement that gives directly the partial-interference pattern.

To obtain the total interference pattern,  $\mathfrak{F}(\xi)$  we use formula (6):

$$
\mathfrak {F} (\xi) = \int_ {- \infty} ^ {\infty} d x \rho (x) i _ {x} (\xi). \tag {A1}
$$

That is, the total number of grains blackened on the photoplate at a position  $\xi$  gives the value of the total interference pattern  $\mathfrak{F}(\xi)$ . The  $\rho(x)$  used in Eq. (A1) is the weight function proportional to the total number of photons that land at a certain  $x$  and plays the same role as  $\mathfrak{D}(\kappa)$  in formula (6).

To show that the discussed proposal is practical and realizable, let us go through the calculations in an example. The separation of photoplates  $\delta$  should not be larger than the distance between the maximum and minimum expected in the interference pattern—in fact it is advantageous to sample the pattern only at these points: This yields for  $\delta$ :

$$
\delta = \pi / k _ {0}.
$$

We have assumed previously that  $\delta / s \ll 1$ . This assumption is not crucial. We have used it solely to ascertain that in the set of photoplates one side of the photoplate can see only one slit. However, even if  $\delta \sim s$ , we can still make sure that this last statement is true by orienting the photoplates so that the plane in which each one of them lies always intercepts the double-slit screen half-way between the two slits. Still, it is easier to do with  $s$  bigger than  $\delta$ .

Taking  $\lambda = 10\mu \mathrm{m}$  (there are lasers which have wavelength of this order), we get for  $L = 100\mathrm{cm}$  and  $s = 5\mathrm{mm}$  the photoplate separation  $\delta = 0.85\mathrm{mm}$ . This is well within reach of experimental possibilities.

We have seen here an experiment that attempts to determine the slit through which each photon passed while trying to retain the interference pattern—the same purpose for which the experiment described in the introduction was designed. However, no data clarifying the Einstein-Podolsky-Rosen paradox as discussed in Sec. IV can be obtained here, since both the path determination and contribution to the interference pattern follow from a single event—photoinduced transition in a silver-bromide grain. Still, our proposal is the only practical version of Einstein's double-slit experiment we are aware of.

# APPENDIX B: OUTLINE OF A PROOF THAT THE PURE STATE MINIMIZES THE LOSS OF INFORMATION

For a given value of  $S$ , what distribution  $\rho$  minimizes  $H$ ? This question can be simplified by the following definitions:

$$
\begin{array}{l} s (\gamma) = \gamma^ {1 / 2} (1 - \dot {\gamma}) ^ {1 / 2}, \\ h (\gamma) = - \left[ \gamma \ln \gamma + (1 - \gamma) \ln (1 - \gamma) \right], \\ \hat {\rho} (\gamma) = \rho (\gamma) + \rho (1 - \gamma), \\ \end{array}
$$

restricted to the interval  $0 \leqslant \gamma \leqslant \frac{1}{2}$ . Then

$$
\begin{array}{l} S = \int_ {0} ^ {1 / 2} d \gamma \hat {\rho} (\gamma) s (\gamma), (B1) \\ H = \int_ {0} ^ {1 / 2} d \gamma \hat {p} (\gamma). (B2) \\ \end{array}
$$

What we wish to show is that the distribution  $\hat{\rho}_0(\gamma) = \delta (\gamma -\gamma_0)$  minimizes  $H$  for a given value of  $S$ . This will imply in particular that the pure state  $\rho_0 = \delta (\gamma -\gamma_0)$  minimizes  $H$ . [So does any other  $\rho$  which gives the same  $\hat{\rho}$ . These other  $\rho$ 's are all of the form

$$
\begin{array}{l} \rho (\gamma) = \alpha \delta (\gamma - \gamma_ {0}) + (1 - \alpha) \delta (\gamma - (1 - \gamma_ {0})), \\ 0 \leqslant \alpha \leqslant 1. ] \\ \end{array}
$$

Step 1. One can prove that  $s$  and  $h$  are monotonically increasing in the interval  $0 \leqslant \gamma \leqslant \frac{1}{2}$ , and that  $s'' / s' \leqslant h'' / h'$  in this interval. (A prime denotes differentiation with respect to  $\gamma$ .)

Step 2. Let us compare the distribution  $\hat{\rho}_0(\gamma) = \delta (\gamma -\gamma_0)$  with the trial distribution  $\hat{\beta}_{1}(\gamma)$  
$= \eta_{1}\delta (\gamma -\gamma_{1}) + \eta_{2}\delta (\gamma -\gamma_{2})$  , in which  $\eta_1 + \bar{\eta}_2 = 1$  , and the parameters are assumed to be adjusted so that both distributions give the same value of  $S$

that is [Eq. (B1)],

$$
s \left(\gamma_ {0}\right) = \eta_ {1} s \left(\gamma_ {1}\right) + \eta_ {2} s \left(\gamma_ {2}\right). \tag {B3}
$$

We will show that  $\hat{\rho}_0$  gives a smaller value of  $H$  than  $\hat{\rho}_1$  does; that is [Eq. (B2)],

$$
h \left(\gamma_ {0}\right) \leqslant \eta_ {1} h \left(\gamma_ {1}\right) + \eta_ {2} h \left(\gamma_ {2}\right). \tag {B4}
$$

To prove this, it is helpful to define  $\overline{h} (\gamma)$  by

$$
\bar {h} (\gamma) = \frac {\left[ s \left(\gamma_ {2}\right) - s \left(\gamma_ {1}\right) \right] h (\gamma) + s \left(\gamma_ {1}\right) h \left(\gamma_ {2}\right) - s \left(\gamma_ {2}\right) h \left(\gamma_ {1}\right)}{h \left(\gamma_ {2}\right) - h \left(\gamma_ {1}\right)}.
$$

The following things are true about  $\overline{h}$ :

(i)  $\overline{h} (\gamma_1) = s(\gamma_1)$  and  $\overline{h} (\gamma_2) = s(\gamma_2)$  
(ii)  $\frac{\overline{h}^{\prime\prime}}{\overline{h}^{\prime}} = \frac{h^{\prime\prime}}{h^{\prime}} \geqslant \frac{s^{\prime\prime}}{s^{\prime}}$  for  $0 \leqslant \gamma \leqslant \frac{1}{2}$ .

(iii) By (i) and Eq. (B3),  $s(\gamma_0) = \eta_1\overline{h} (\gamma_1) + \eta_2\overline{h} (\gamma_2)$ .  
(iv) To prove Eq. (B4), it is sufficient to prove that

$$
\bar {h} \left(\gamma_ {0}\right) \leqslant \eta_ {1} \bar {h} \left(\gamma_ {1}\right) + \eta_ {2} \bar {h} \left(\gamma_ {2}\right).
$$

From (iii) and (iv) it is clear that what we have to prove is that  $\overline{h} (\gamma_0)\leqslant s(\gamma_0)$ . In fact it is not hard to show from properties (i) and (ii) that  $\overline{h} (\gamma)\leqslant s(\gamma)$  for all  $\gamma$  between  $\gamma_{1}$  and  $\gamma_{2}$ , and thus for  $\gamma_0$  in particular.

Step 3. We have seen in Step 2 that the distribution  $\hat{\beta}_0 = \delta (\gamma -\gamma_0)$  is better at minimizing  $H$  than any sum of two  $\delta$  functions. This result can be extended by induction to any sum of  $\pmb{n}$ $\delta$  functions.

Step 4. For the purpose of calculating  $S$  and  $H$ , any distribution can be approximated arbitrarily closely by a sum of  $n \delta$  functions. Therefore, the distribution  $\hat{\beta}_0 = \delta (\gamma -\gamma_0)$  minimizes  $H$  with respect to all possible distributions.