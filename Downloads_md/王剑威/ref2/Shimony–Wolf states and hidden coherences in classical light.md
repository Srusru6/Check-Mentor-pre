# Shimony-Wolf states and hidden coherences in classical light

J.H. Eberly

To cite this article: J.H. Eberly (2015): Shimony-Wolf states and hidden coherences in classical light, Contemporary Physics, DOI: 10.1080/00107514.2015.1080949

To link to this article: http://dx.doi.org/10.1080/00107514.2015.1080949

![](images/421336e0cbc0ebbaa623319218ebda6007a5da2e1466203a31caf8a8eee4a9c1.jpg)

Published online: 21 Sep 2015.

![](images/72b352f00abc8a2fc6f5f3b376150c5cc949fc513e5fc9f68dfc60ae7ad553ce.jpg)

Submit your article to this journal

![](images/5f7b837215e9ade56a7cd70e4d4b2d7bd6fdc701d19593d39a9fc697b5c92f38.jpg)

Article views: 23

![](images/17fb45259e28f47f22e9418baa14ef3f16e2940fbd347eddc69e53fa792c42bb.jpg)

View related articles

![](images/022ba88e36dc1dfd2b7b2e1c5822fe2f5321fb25ff234407576d1d34d46e93ba.jpg)

View Crossmark data

# Shimony-Wolf states and hidden coherences in classical light

J.H. Eberly*

Center for Coherence and Quantum Optics and the Department of Physics & Astronomy, University of Rochester, Rochester, NY, USA

(Received 6 July 2015; accepted 3 August 2015)

The classical theory of polarisation coherence is briefly summarised and then extended. The extension is motivated by the recognition that the traditional theory of two-point coherence provides only what we identify as 'diagonal' correlation functions and their associated two-point coherence matrices. It is pointed out that a wider focus is possible when taking account of the three-sector vector space underlying all two-point coherences in classical optics. This reveals the possibility of observing a new type of 'off-diagonal' correlations that arise when the correlation functions under investigation are associated with points in two distinct vector spaces, pairs of points that are not analogous to the pairs of space points or time points that underlie traditional measures of spatial and temporal coherence. Quantum theory has experience with correlations engaging such 'cross-sector' coherences, for example in tests of Bell inequalities, and the quantum formulations are shown to be easily adopted by classical theory without incorporating quantum features in the optical signals. The familiar theory of classical coherence that is associated with the pioneering work of Emil Wolf is extended in conformance with three criteria advanced by Abner Shimony to obtain formulas for correlation functions and for the Bell measure  $S$  of coherence. Values of  $S$  greater than the standard upper limit  $S = 2$  are predicted for certain classical Shimony-Wolf fields, indicating strong cross-sector coherence, but only when standard measures of coherence such as degree of polarisation  $\mathcal{P}$  are minimised. Experimental results confirming the predictions for cross-sector coherence are exhibited.

Keywords: classical coherence theory of light; correlation vector space; cross-sector correlation; entanglement in classical light

# 1. Where did coherence come from?

The concept of coherence, as applied to light, is a remarkably recent invention, given the subtle observations made on light as early as the 1600s and 1700s. Among these were observations of interference and diffraction, for example by Grimaldi and Boyle and Hooke, and the discovery of polarisation by Christiaan Huygens. Polarisation became a controllable property of light around 1800 when Etienne Malus found that it can be created by reflection. However, convincing explanations for these phenomena were lacking before the advances that followed Thomas Young's report in 1801 announcing the principle of wave interference. In the same period, Augustin Fresnel famously won the Paris Academy's prize in 1818 with a theory of diffraction, combining Huygens' wave construction with Young's interference principle. At almost the same time, a paradigm-shifting moment occurred when the answer was found by Young to the puzzling observation of Fresnel with Dominique Arago that a combination of orthogonal polarisations cannot interfere. Young realised that this amounted to a startling discovery: light waves are transverse not longitudinal. The latter had been universally taken for granted.

By the 1850s, James Clerk Maxwell's equations of electromagnetism gave the first complete theory for light. It

allowed a light wave to be described as a propagating vector electromagnetic field. Slightly earlier, George Stokes had categorised the familiar types of light polarisation – linear, circular and elliptical – and described methods for detecting the types individually. He also invented a new optical measure, the degree of polarisation, to quantify the extent to which a light field shows only partial polarisation. This meant that no clear separation could be observed between contributions to the light intensity from different orientations of the polarisation vector. For this, there was no satisfactory analysis. At the same time, there was also no satisfactory theory of spectrum, i.e. of light with a continuous distribution of frequencies rather than distinct monochromatic components. This is when a defined concept of coherence gradually began to emerge as something new. The incomplete understanding of coherence at that time can be compared with the earlier vague understanding of imperfect light interference that was current before Young's quantitative interference principle was announced.

It is worth recalling how straightforwardly puzzling it is that a vector field can show less than perfect polarisation. To see this, consider the expression for the electric field of an arbitrary light wave, where  $\hat{x}$  and  $\hat{y}$  are unit vectors transverse to propagation, nominally the  $z$  direction:

$$
\vec {E} = \hat {x} E _ {x} (t) + \hat {y} E _ {y} (t). \tag {1}
$$

For simplicity, in the following equations, we'll take the component amplitudes and polarisation vectors of an optical field to be real, but the consequences to be developed will not depend on that restriction. If  $E_{x}$  and  $E_{y}$  can be known, as (1) implies, then the field cannot be anything but perfectly polarised in an exactly known direction  $\hat{u}$ . This means that it can be rewritten much more simply as

$$
\vec {E} = \hat {u} F (t), \tag {2}
$$

where  $\hat{u}$  is a specific unit vector obtained from the original  $\hat{x} -\hat{y}$  pair by rotation. It is determined just by the presumed knowable values of  $E_{x}$  and  $E_{y}$ :

$$
\begin{array}{l} u _ {x} = E _ {x} / F, \quad u _ {y} = E _ {y} / F \\ F (t) = \sqrt {E _ {x} ^ {2} (t) + E _ {y} ^ {2} (t)}. \tag {3} \\ \end{array}
$$

Thus, an observation of incomplete polarisation disproves the existence of a direction  $\hat{u}$ . In effect, this denies the presence of perfectly knowable components  $E_{x}$  and  $E_{y}$ . In other words, incomplete polarisation implies that the field components have indeterministic and uncorrelated values. One reaches the same conclusion if the field has a fixed amplitude and it is the polarisation vectors that are reorienting randomly as an orthogonal pair in the transverse plane. $^{1}$

Beginning around 1890, serious attention began to be given to questions arising from a number of domains in which indeterminism was seen to be present. A question of significance for mathematicians was attached to practical problems in various fields of science and technology where there was no satisfactory way to define the spread of frequencies present in a non-deterministic signal. Especially troubling was the meaning of spectrum for a signal that is continuing to run forever in an irregular but unending way, in a practical sense non-diverging but also non-converging, and technically called 'stationary'. This means that the statistical randomness underlying a stationary signal eliminates any significance for an original time moment. This in turn allows a nominal initial time to be shifted as convenient, so a general correlation coefficient can be expressed as a function of a single variable, the time difference of its signal's arguments:

$$
C \left(t _ {1}, t _ {2}\right) \equiv \langle S \left(t _ {1}\right) S \left(t _ {2}\right) \rangle = \langle S (0) S \left(t _ {2} - t _ {1}\right) \rangle . \tag {4}
$$

Effectively stationary signals occur in all scientific fields and include earth tremors, ocean waves, radio noise and white light.

Then, in the first half of the twentieth century, mathematically sound treatments of spectra of stationary signals were given separately by Norbert Wiener and Aleksander Khintchine using different approaches. This development reoriented all subsequent analyses of indeterministic signals away from the Fourier transform of the signal itself (strictly not defined for a non-convergent signal) to the Fourier transform of the signal's correlation functions. In the case of an

![](images/229f8dfd34ffb4a838822a68882ecacb042a82a5f0739cdc0631fbb72a222500.jpg)  
Figure 1. Set-up for a generic two-point correlation experiment. The point  $P$  receives two signals and registers the intensity of the combined signal. The experimenter can control differences in the signals arising from source positions, signal polarisations and relative time delay. From [1] with permission.

indeterministic signal  $S(t)$  this meant:

$$
\begin{array}{l} s p e c t r u m \quad \nrightarrow \quad \int S (t) e ^ {i \omega t} d t (\text {u n d e f i n e d}) \\ \rightarrow \int \langle S (0) S (t) \rangle e ^ {i \omega t} d t \quad (\text {w e l l d e f i n e d}), \tag {5} \\ \end{array}
$$

where the angular brackets can have more than one interpretation, but always represent an average over an underlying distribution of signals. In Wiener's case, the distribution was understood to be a sufficiently long-time record of the indeterministic signal itself, implying a time average. In Khintchine's case, the average was abstract and based on an imaginary ensemble of complete realisations of the signal. If the signal is ergodic, as is normally the case for natural signals, there is no difference.

A quantitative measure for coherence in the time domain can be obtained by considering the correlation function as the Fourier inverse of (5). As it indicates, the existence of a spectrum means coherence in the time domain, where one can understand coherence in the sense of the fidelity of a signal, measured by the length of time that the correlation coefficient  $C(t_{1},t_{2})$  remains faithful to its earlier value  $C(t_{1},t_{1})$ . Obviously,  $\langle |S(t_1) - S(t_2)|^2\rangle \geq 0$ , so  $2|\langle S(t_1)S(t_2)\rangle |\leq \langle S^2 (t_1)\rangle +\langle S^2 (t_2)\rangle$ , and for stationary signals  $\langle S^2 (t_1)\rangle = \langle S^2 (t_2)\rangle$ , so the ratio

$$
\frac {2 | \langle S (t _ {1}) S (t _ {2}) \rangle |}{\langle S ^ {2} (t _ {1}) \rangle + \langle S ^ {2} (t _ {2}) \rangle} \rightarrow \frac {| \langle S (0) S (t) \rangle |}{\langle S ^ {2} (0) \rangle} = \frac {| C (0 , t) |}{C (0 , 0)} \tag {6}
$$

lies between 0 and 1 and serves as a particularly simple quantitative measure of fidelity.

Spatial coherence also exists, of course, and one can define the wave vector spectrum as the Fourier transform of the space correlation coefficient  $\langle S(0)S(r)\rangle$ , where spatial stationarity has been assumed, and  $r = r_2 - r_1$  is a spatial displacement. The domain of detection over which signals from two sources can give rise to observable interference defines coherence area. In Figure 1, this is the range over which the point  $P$  can be moved without appreciably

altering the coherence of the detected combined signal. Following the breakthroughs by Wiener and Khintchine, spatial coherence was identified and studied by P.H. van Cittert and Fritz Zernike, and the concept of partial coherence as a joint space-time construct became reasonable.

# 2. Where coherence theory has led us

In the mid-1950s, slightly more than 100 years after Maxwell and Stokes, the developments triggered by Wiener and Khintchine were creatively applied to optics by Emil Wolf [2-4], who pioneered a formal theory of partial coherence applicable to spectrum as well as to polarisation. As Wolf has indicated [5], an enormous advantage attaches to a theory of optics based on correlation functions instead of the signals themselves. Then optics becomes freed from reliance on the fields. These oscillate much too rapidly for direct detection and the slower evolution of correlations is what is registered in any event when the field is observed via intensity. Wolf's theory of partial optical coherence has been organised and presented in a wide variety of monographs and texts in a number of closely related ways, sometimes with slightly varying definitions of the degree of coherence.

Here, we intend to present a different organisation that exposes categories of optical coherence that are typically overlooked, and suggests that truly 'off-diagonal' coherences have been neglected and should be included. All of the correlation coefficients to be mentioned will be accessible via intensity measurements of a composite vector optical field that we can call a 'three-sector' field [6]. That is, each field has three independent elements, usually called degrees of freedom, that are exhibited in polarisation direction, spatial modes and temporal variation. The most general lowest order correlation function will depend on pairs of each, which can be schematically indicated by

$$
C (1, 2) = \langle E \left(p _ {1}, r _ {1}, t _ {1}\right) E \left(p _ {2}, r _ {2}, t _ {2}\right) \rangle , \tag {7}
$$

where the space vectors  $\vec{r}$  have been reduced to scalars  $r$  for simplicity.

The preceding section summarises the usual theory of temporal and spatial coherences as examined by correlations of a two-point field vector. The temporal correlation coefficient ignores polarisation direction and spatial location (implicitly fixing  $p_1 = p_2 = p$  and  $r_1 = r_2 = r$ ), and the spatial correlation coefficient ignores polarisation and time by fixing them similarly. These yield the familiar results:

$$
\begin{array}{r l}C _ {t i m e} (t _ {1}, t _ {2})&= \langle \hat {p} \cdot \vec {E} (r, t _ {1}) \hat {p} \cdot \vec {E} (r, t _ {2}) \rangle\\&\rightarrow \langle E (t _ {1}) E (t _ {2}) \rangle\end{array}\tag {8}
$$

$$
\begin{array}{r l}C _ {s p a c e} (r _ {1}, r _ {2})&= \langle \hat {p} \cdot \vec {E} (r _ {1}, t) \hat {p} \cdot \vec {E} (r _ {2}, t) \rangle\\&\rightarrow \langle E (r _ {1}) E (r _ {2}) \rangle .\end{array}\tag {9}
$$

The same is true of correlation in 'polarization space', where position and time are not mentioned. Independent

polarisation possibilities, say  $\hat{p}_1$  and  $\hat{p}_2$ , are analogous to the independent  $t_1$  and  $t_2$  possibilities in the temporal correlation, and the conventional choice is to use the orthogonal  $\hat{x}$  and  $\hat{y}$ , to obtain:

$$
\begin{array}{l} C _ {p o l z n.} (x, y) = \langle \hat {x} \cdot \vec {E} (r, t) \hat {y} \cdot \vec {E} (r, t) \rangle \\ \rightarrow \langle E _ {x} E _ {y} \rangle . \tag {10} \\ \end{array}
$$

By definition, the degrees of freedom of the field (temporal function, spatial mode, and polarisation direction) are independent of each other. Each defines an independent vector space and each degree of freedom has its own notion of basis vectors and scalar product and orthogonality and completeness. These are elementary for the polarisation space, which is only two dimensional, with unit basis vectors  $\hat{x}$  and  $\hat{y}$ , where  $\hat{x} \cdot \hat{x} = \hat{y} \cdot \hat{y} = 1$  and  $\hat{x} \cdot \hat{y} = 0$ . To describe the continuum of locational space (the  $r$  dependence) we have complete sets of mode functions,  $G_{n}(r)$ , in terms of which all other space functions can be expanded, and scalar product is an integration over the  $r$  domain.

The non-deterministic time sector of our three-sector vector space has mode functions  $\phi_{m}(t)$  defined via the integral equation

$$
\int C \left(t _ {1}, t _ {2}\right) \phi_ {m} \left(t _ {2}\right) \mathrm {d} t _ {2} = \kappa_ {m} ^ {2} \phi_ {m} \left(t _ {1}\right), \tag {11}
$$

in which the kernel is the time-sector correlation function. The  $\kappa_{m}$  are real and the  $\phi_{m}$  form an orthonormal set in terms of which the temporal functions may be expanded (see below), with random coefficients  $c_{m}$  satisfying  $\langle c_m c_n\rangle = \delta_{mn}$  [7].

The three correlation coefficients (8)-(10), are familiar elements of the theory of partial coherence of light. All of the elements belonging to each coefficient are conveniently displayed as  $2 \times 2$  matrices, each of which deserves the generic name coherence matrix:

$$
C _ {\text {t i m e}} \rightarrow \left[\begin{array}{l}\langle E (t _ {1}) E (t _ {1}) \rangle \langle E (t _ {1}) E (t _ {2}) \rangle\\\langle E (t _ {2}) E (t _ {1}) \rangle \langle E (t _ {2}) E (t _ {2}) \rangle\end{array}\right], \tag {12}
$$

$$
C _ {s p a c e} \rightarrow \left[\begin{array}{l l}\langle E (r _ {1}) E (r _ {1}) \rangle&\langle E (r _ {1}) E (r _ {2}) \rangle\\\langle E (r _ {2}) E (r _ {1}) \rangle&\langle E (r _ {2}) E (r _ {2}) \rangle\end{array}\right], \tag {13}
$$

$$
C _ {p o l z n.} \rightarrow \left[\begin{array}{l l}\langle E _ {x} E _ {x} \rangle&\langle E _ {y} E _ {x} \rangle\\\langle E _ {x} E _ {y} \rangle&\langle E _ {y} E _ {y} \rangle\end{array}\right]. \tag {14}
$$

Texts of optical physics [8] explain that any of the elements of the coherence matrices above are individually physically accessible via intensity measurements. The matrices themselves are said to express what is observable in regard to optical coherence, and in each case, as comparison of (8)-(10) with (12)-(14) indicates, non-zero coherence means a non-zero value of the off-diagonal matrix element.

# 3. New off-diagonal correlations in super-space

We now argue that the view of coherence just expressed is not broad enough. A clue to this is in the arrangement of correlation coefficients into matrices. The odd point is that,

in all cases, there is no rationale for the standard matrix arrangement. That is, no suitable vector space is traditionally identified to support a matrix form, and small inconsistencies have been widely introduced. It is proposed here to begin an expanded organisation of optical coherence theory by first making explicit the vector space underlying all of these coherence matrices, and then to show that, despite conventional interpretations, all of the coherence measures belonging to the standard theory are only measures of a kind of 'diagonal' coherence, and the corresponding 'off-diagonal' coherences have not generally been recognised or measured [6].

The steps to reach the goal just mentioned are not complicated, are in fact trivial, but necessary in order to embrace the full potential for coherence in classical optics. One simply needs to take full advantage of the natural underlying so-called 'correlation super-space'. This is the tensor product of the three different vector spaces defined by the three independent variables at hand (the degrees of freedom of the field): time, space, and polarisation direction. The most general optical field vector in this space relevant to two-point coherences as sketched in (7) is easily written. Two different polarisation directions  $\hat{p}$  are needed, and the space-function and time-function sectors of the super-space are accommodated separately by the infinite sets of temporal modes  $\phi_{m}(t)$  and spatial mode functions  $G_{n}(r)$ , and one obtains:

$$
\vec {E} (p, r, t) = \sum_ {k = 1, 2} \sum_ {m, n} a _ {k, m, n} \hat {p} _ {k} \phi_ {m} (t) G _ {n} (r). \tag {15}
$$

A key observation is that all of the familiar two-point correlation functions displayed in (8)-(10) are tagged by different values of the same degree of freedom, obtained by cancelling (or ignoring) the field's dependence on two other degrees of freedom, and retaining two points that are always in the same vector space. Three different reductions of this kind are exhibited in (8), (9), and (10), in the ways indicated in these three 'two-point reductions':

$$
(p _ {1} r _ {1} t _ {1}) - (p _ {2} r _ {2} t _ {2}) \rightarrow (t _ {1}, t _ {2}), \quad \text {o r}
$$

$$
\left(p _ {1} r _ {1} t _ {1}\right) - \left(p _ {2} r _ {2} t _ {2}\right)\rightarrow \left(r _ {1}, r _ {2}\right), \quad \text {o r}
$$

$$
\left(p _ {1} r _ {1} t _ {1}\right) - \left(p _ {2} r _ {2} t _ {2}\right)\rightarrow \left(p _ {1}, p _ {2}\right). \tag {16}
$$

In this light, we see that the traditional results are what could (should?) be called 'diagonal' correlations, that is, correlations staying within any one particular sector of the entire three-sector correlation super-space.

A new question comes up when considering the  $C$ 's in this way. It seems to have been overlooked previously. The question is how to explore the domain of classical correlations ignored so far, the correlations 'across' divisions in this huge super-space, as indicated by different reductions of the spaces across sector lines. For example, one can at least think about cross coherences implied by reductions different from those in (16):

$$
\begin{array}{l} (p _ {1} r _ {1} t _ {1}) - (p _ {2} r _ {2} t _ {2}) \rightarrow (t; r), \quad \text {o r} \\ (p _ {1} r _ {1} t _ {1}) - (p _ {2} r _ {2} t _ {2}) \rightarrow (r; p), \quad \text {o r} \\ \left(p _ {1} r _ {1} t _ {1}\right) - \left(p _ {2} r _ {2} t _ {2}\right)\rightarrow (p; t). \tag {17} \\ \end{array}
$$

One easily sees in the three-sector field (15) many cross-correlation possibilities. It appears that, for example, cross correlation between a beam's spatial character and its temporal character should be accessible in principle [11]. However, a complication is raised by such cross correlations. In our examples, coherence was a kind of fidelity that depended on a difference between two values of a coordinate location or time or polarisation. In terms of specific experimental set-ups one knows how to interpret off-sets and delays such as  $\Delta r \equiv r_2 - r_1$  and  $\Delta t \equiv t_2 - t_1$ , as well as the angle difference  $\Delta \theta$  between  $\hat{p}_1$  and  $\hat{p}_2$ . But it is initially puzzling what set-up permits a cross-sector experiment correlating  $t$  and  $r$ , or  $t$  and  $p$ .

As an illustration, we choose the  $(t;p)$  type. We will ignore  $r$  by fixing  $r_1 = r_2 = 0$  and take  $t_2 = t_1 \equiv t$ . If the polarisation vectors are resolved into the  $\hat{x}$  and  $\hat{y}$  bases, then the resulting amplitudes are simply the components  $E_x(t)$  and  $E_y(t)$  of the field, and we have effectively returned from (15) to Equation (1):

$$
\vec {E} = \hat {x} E _ {x} (t) + \hat {y} E _ {y} (t), \tag {18}
$$

where only time variation and polarisation direction are considered.

As we argued in Section 1, if the field is partially polarised, or in the extreme case unpolarised, then either the amplitudes  $E_{x}$  and  $E_{y}$ , or the polarisation vectors  $\hat{x}$  and  $\hat{y}$ , or both, must be indeterministically random. It is difficult to argue, particularly in the fully unpolarised case, that an indeterministically random  $E_{x}(t)$  can correlate with any  $\hat{p}$  value. However, cross-sector correlations, for example of the  $(t;p)$  type, are known in quantum physics. By importing methods to examine cross-sector correlation from quantum mechanics into classical wave theory, we will expand the realm of classical optical coherence.

# 4. Shimony's quantum-like criteria and classical entanglement

The classical fields (15) and (18) obviously fit securely into Wolf's coherence theory, but also fit three quantum-like criteria advanced in 1984 by Abner Shimony [12]. Shimony was addressing methods such as the prescriptions of Clauser, Horne, Shimony and Holt (CHSH) [13] for testing the well-known cross-sector inequalities of John Bell [14-16]. We will see that the CHSH prescription can be adapted to classical cross-sector correlation evaluations.

The criteria that Shimony advanced are embodied in three key features, all of which should be considered, in his words, ... as established parts of physical theory:

(I) In any state of a physical system  $S$ , there are some eventualities which have indefinite truth values.  
(II) If an operation is performed which forces an eventuality with indefinite truth value to achieve definiteness ... the outcome is a matter of chance.  
(III) There are 'entangled systems' (in Schrödinger's phrase) which have the property that they constitute a composite system in a pure state, while neither of them separately is in a pure state.

Here, by eventualities Shimony means measurement outcomes. In effect, to deserve serious attention, he said that every satisfactory description of Nature, i.e. every physical theory, needs to embrace in some way those aspects of natural phenomena that experiments repeatedly show to be completely random.

Shimony's explicit recognition of probabilistic Nature is clearly based on observed micro-properties of quantum systems, but properties available in classical fields as well. It is clear that within the classical optical theory of partial coherence that we have quickly reviewed, Wolf's statistical field (18) has no definite value until it is observed and so satisfies criteria I and II. We have already noted that it cannot be factored as in (2) and thus satisfies entanglement criterion III as well. We will designate as Shimony-Wolf fields or states the classical fields such as (18) that satisfy criteria I-III.

Entanglement is becoming widely understood to be present in classical as well as in quantum physics. One can easily understand entanglement as Schrödinger described it [17]: if a function  $\Psi(x, y)$  of two variables cannot be written as  $f(x)g(y)$ , i.e. with the independent variables  $x$  and  $y$  in factored form, then  $\Psi(x, y)$  is said to be entangled. In his own words, 'What constitutes the entanglement is that  $\Psi$  is not a product of a function of  $x$  and a function of  $y$ . Many treatments of classical optical fields entangled across degrees of freedom, similar to (18) but usually without concern for Shimony's criteria I and II, have already been undertaken. The possibility that classical entanglement is open for experimental observation via optical wave functions was apparently suggested first by Spreeuw in 1998 [18]. This was supported strongly by Ghose and Samal [19] in 2001. An early experimental report by Lee and Thomas [20] came in 2002 and other experimental and theoretical treatments appeared in the following decade [21-29]. Interest in the issues raised by classical entanglement continues to grow. Various different directions of investigation and applications have already been reported in 2015 [30-35].

A further word about entanglement itself may be interesting. Schrödinger was the first to specify the importance of non-factorable joint states and, as is well known, bears the responsibility for giving a technical scientific meaning to the English-language word entanglement. It is not widely appreciated that Schrödinger didn't have to invent

entanglement because it was already 30 years old in the mathematics literature of functional analysis.

Schrodinger acknowledged this by reference to a mathematical-physics textbook in the second footnote of the 1935 paper in which he introduced his famous Cat [17]. His paper was in response to the equally well-known 'EPR' article in which Einstein, Podolsky and Rosen [36] challenged the completeness of quantum mechanics. The backup for Schrodinger's observation was explained in the textbook. It was the work of Erhard Schmidt [37], focused on his theory of integral equations with non-symmetric kernels, an example of which incidentally appears in Equation (11).

# 5. Cross-sector coherence in Shimony-Wolf fields or states

Because of the quantum guide to be followed, we will adopt Dirac-type notation for Shimony-Wolf fields such as (18):  $\vec{E} \rightarrow |\mathbf{E}\rangle$ ,  $\hat{x} \rightarrow |x\rangle$ , etc., and we will use boldface to emphasise the two-sector character of the field and get another way to write (18):

$$
| \mathbf {E} \rangle = | x \rangle \otimes | E _ {x} \rangle + | y \rangle \otimes | E _ {y} \rangle , \tag {19}
$$

where the explicit use of tensor product symbols only emphasises that different vector spaces are included. The same change in notation can also be applied to the more general expression (15) for the field (dropping the tensor symbols hereafter):

$$
\vec {E} (p, r, t) \rightarrow | \mathbf {E} \rangle = \sum_ {k = 1, 2} \sum_ {m, n} a _ {k, m, n} | p _ {k} \rangle | \phi_ {m} \rangle | G _ {n} \rangle . \tag {20}
$$

In any event, nothing becomes quantum mechanical by adopting the new notation.

We next use the Schmidt Theorem [37] to write the unit-normalised classical field  $|\mathbf{e}\rangle \equiv |\mathbf{E}\rangle /\sqrt{\langle\mathbf{E}|\mathbf{E}\rangle}$  as:

$$
| \mathbf {e} \rangle = \kappa_ {1} | u _ {1} \rangle | f _ {1} \rangle + \kappa_ {2} | u _ {2} \rangle | f _ {2} \rangle , \tag {21}
$$

where the  $\kappa$ s are real and one has  $\langle \mathbf{e}|\mathbf{e}\rangle = \kappa_1^2 +\kappa_2^2 = 1$ . The orthogonal polarisation unit vectors  $|u_{1}\rangle$  and  $|u_{2}\rangle$  are merely Schmidt-rotated versions of  $|x\rangle$  and  $|y\rangle$  in the polarisation sector. There are only two (orthogonal)  $|f\rangle$ s that enter because the Schmidt Theorem selects the two that are relevant for combination with  $|x\rangle$  and  $|y\rangle$  to replace  $|E_x\rangle$  and  $|E_y\rangle$ .

To proceed we now follow CHSH. We define a crosssector correlation coefficient  $C(a, b)$  between the polarisation and time-function sectors and then construct the averaged product of specific projection differences:

$$
C (a, b) = \langle \mathbf {e} | \left(Z ^ {u} (a) \otimes Z ^ {f} (b)\right) | \mathbf {e} \rangle . \tag {22}
$$

To pursue the correlation, we have introduced

$$
Z ^ {u} (a) \equiv | u _ {1} ^ {a} \rangle \langle u _ {1} ^ {a} | - | u _ {2} ^ {a} \rangle \langle u _ {2} ^ {a} | \quad a n d
$$

$$
Z ^ {f} (b) \equiv | f _ {1} ^ {b} \rangle \langle f _ {1} ^ {b} | - | f _ {2} ^ {b} \rangle \langle f _ {2} ^ {b} |, \tag {23}
$$

and the  $|u^a\rangle$  s and  $|f^{b}\rangle$  s are further rotations of  $|u_{1}\rangle$  and  $|u_{2}\rangle$  and  $|f_1\rangle$  and  $|f_2\rangle$  through angles  $a$  and  $b$  that are varied in correlation measurements:

$$
\begin{array}{l} \left| u _ {1} ^ {a} \right\rangle = \cos a \left| u _ {1} \right\rangle - \sin a \left| u _ {2} \right\rangle \quad \text {a n d} \\ \left| u _ {2} ^ {a} \right\rangle = \sin a \left| u _ {1} \right\rangle + \cos a \left| u _ {2} \right\rangle , \tag {24} \\ \end{array}
$$

etc. Each  $Z$  is a classical analogue of the  $z$  component of a quantum  $\vec{\sigma}$  operator.  $C(a, b)$  is thus a combination of four joint probabilities:

$$
C (a, b) = P _ {1 1} - P _ {1 2} - P _ {2 1} + P _ {2 2}, \tag {25}
$$

where, for example,

$$
P _ {1 1} (a, b) = \langle \mathbf {e} | \left(| u _ {1} ^ {a} \rangle | f _ {1} ^ {b} \rangle \langle f _ {1} ^ {b} | \langle u _ {1} ^ {a} |\right) | \mathbf {e} \rangle .
$$

One should not be hypnotised by the Dirac notation; all of these quantities are classical and the probabilities  $P_{jk}(a,b)$  with  $j,k = 1,2$  all have roles in classical statistical optics [1,8]. An exact replica of (25) for classical correlation in the  $(p;r)$  sector appears in the report by Kagalwala et al. [28].

The question of interest is the strength of cross-sector coherences. The CHSH procedure proves the inequality  $|S| \leq 2$  for this purpose. This version of a Bell Inequality requires a combination of four correlation coefficients to define  $S$ :

$$
\mathcal {S} = C (a, b) - C \left(a, b ^ {\prime}\right) + C \left(a ^ {\prime}, b\right) + C \left(a ^ {\prime}, b ^ {\prime}\right). \tag {26}
$$

Here  $a$ ,  $a'$ ,  $b$ ,  $b'$  are arbitrary rotation angles in the  $u$  and  $f$  vector spaces. It is understood in the derivation of the CHSH inequality that if  $S \geq 2$  would be found, it would signal a significant strength of correlation, greater than what would be expected classically, although the meaning of 'classical' is not made precise.

# 6. Experimental evaluation

In 1991, Gisin pointed out [38] that any quantum pure state entangled in the same way as Shimony-Wolf pure states, e.g. (20) or (21), will permit sufficiently strong crosssector coherence to violate the CHSH inequality. To replicate Gisin's demonstration only requires independence of vectors in different vector spaces (often termed locality $^3$ ) together with positive probabilities and normed vectors. The only new feature in a classical experiment not appearing in the CHSH description is that  $\langle \mathbf{e}|Z^u (a)|\mathbf{e}\rangle$  and  $\langle \mathbf{e}|Z^{f}(b)|\mathbf{e}\rangle$  both lie anywhere in the continuum between  $-1$  and  $+1$ , rather than taking the discrete values  $\pm 1$  associated with photon-pair detection. That is, one would use a classical light beam so detection would be by power meters not by photon counting.

Recently, a sequence of experimental measurements with a classical non-deterministic Shimony-Wolf wave field have been carried out [32]. The experimental setup used a laser diode operated in the classical multi-mode region below threshold where it produces statistically thermal light. Polarisation tomography was used to characterise the beam.

![](images/55646bb7632eb0137e3a4c8299e5bc61113e72f2c3d4b5c35c36f6f62fd67889.jpg)  
Figure 2. Plots of the correlation functions  $C(a, b)$  obtained by scanning polarisation angle  $a$  and holding angle  $b$  in the function space constant. The invariant cosine function required to violate the Bell inequality is clearly present. From arXiv:1406.3338.

Figure 2 shows  $C(a, b)$  obtained by measuring the joint probabilities  $P_{jk}(a, b)$  for a complete rotation of polariser  $a$ , with different curves corresponding to  $b$  fixed at different values. It is apparent from the near-identity of the curves that, to an excellent approximation, the correlations are a function of the difference in angles, i.e.  $C(a, b) = C(a - b)$ . Using this approach, the maximum value for  $S$  can be found straightforwardly and values were obtained in the range from 2.55 to 2.70, many standard deviations above the critical correlation point  $S = 2$ . There is thus no question that classically as well as quantum mechanically one can detect strong cross-sector coherence.

# 7. Speculations on classical coherences of light

The fact was introduced at the start that incompletely polarised light, in the extreme case completely unpolarised light, demands a theoretical treatment embracing non-determinism. This feature resides in the light wave itself, without a way to assign the randomness either to the orientation of the wave's polarisation unit vectors or to the independent component amplitudes. This makes it initially difficult to conceive that truly 'off-diagonal' coherence requiring correlation between different and independent sectors of the available vector space, e.g.  $(t;p)$  coherence, can be present.

This impression is supported by the CHSH inequality, which posits the impossibility of certain high correlation strengths. These have nevertheless been found to exist in quantum experiments of several types, most often correlations of polarisation of pairs of photons, each one of which is itself unpolarised. How is this possible? In the quantum world, this is trivially possible to explain theoretically although a difficult laboratory challenge to manage, which was successfully done in initially heroic and historically important experiments [39,40], and their subsequent

early counterparts [41-43]. The trivial theoretical explanation is simply that the unpolarised two-photon systems employed in the experiments are pair-wise polarisation-entangled. That is, the CHSH inequality guards against external influences that might induce correlations, but it is blind to the effect of pre-existing structural correlations that are present because of entanglement.

As remarked above, the demonstration by Gisin shows that non-quantum fields of the Shimony-Wolf type are also permitted to be cross-sector coherent enough to violate the inequality. An explicit calculation of the Bell parameter  $S$  is possible and it directly allows strong correlation. For a general partially polarised classical Shimony-Wolf field such as given in (21) one finds:

$$
\begin{array}{l} \mathcal {S} = \cos 2 a (\cos 2 b - \cos 2 b ^ {\prime}) \\ + \cos 2 a ^ {\prime} (\cos 2 b + \cos 2 b ^ {\prime}) \\ + 2 \kappa_ {1} \kappa_ {2} \left\{\sin 2 a \left(\sin 2 b - \sin 2 b ^ {\prime}\right) \right. \\ + \sin 2 a ^ {\prime} (\sin 2 b + \sin 2 b ^ {\prime}) \}. \tag {27} \\ \end{array}
$$

When one of the  $\kappa$ s is zero, the field is not entangled - recall (21) - and in that case  $S \leq 2$  is upheld. However, if the  $\kappa$ s are optimally balanced and equal then the field is maximally classically entangled and (27) gives  $S = 2\sqrt{2}$ , greatly exceeding the CHSH limit. What is apparent is that completely random polarisation orientations and completely random temporal fluctuations show no statistical correlations with anything except with themselves, unless they might be structurally entangled, not existentially separate at all. This is exactly Schrödinger's original remark about states in quantum mechanics, and we see that it applies classically as well as quantum mechanically: a strong cross-sector correlation is the consequence of entanglement. This is obvious once pointed out. As remarked by Zurek [44], cross-sector coherence has all the time been 'hiding in plain sight'.

Going further, one can note a striking contrast, a counterbalancing of coherences. The contrast revealed here is between degree of polarisation  $\mathcal{P}$  on the one hand and crosssector coherence  $S$  on the other. That is, when one  $\kappa$  is zero in (21), the field is transparently factorable and we can have no entanglement. But this brings us all the way back to  $\vec{E} = \hat{u} F$  as in (2) and means  $100\%$  complete polarisation. The opposite limit occurs with maximum  $S$  when  $\kappa_{1} = \kappa_{2}$  and the degree of polarisation  $\mathcal{P} = |\kappa_1^2 -\kappa_2^2 |$  vanishes. This counter-balancing of  $\mathcal{P}$  and  $S$  exposes a wider domain needing further examination, namely the realm of counter-balanced cross-sector 'pair polarizations' of several types. The recent work of De Zela [45] provides a study of different such measures, called by names such as distinguishability, visibility, entanglement, which-way information and predictability all dealing with aspects of duality and complementarity. Interrelationships have been discussed by several authors [46-51].

As a side comment, we first recall that our demonstration of (t;p) coherence employed a restricted form of optical field correlation, in which the  $r$  sector was ignored, just above equation (18). This doesn't mean that there was no  $r$  dependence, but simply that the  $r$  sector was present as a factored part of the entire field state, and could have been represented by any function of  $r$ , in particular any spatial mode function. We also recall that the degree of polarisation could vary from 0 to 1 within the developments described. This combination of facts makes an easy way to see the basis of Wolf's proof [1] that a completely unpolarised beam can be spatially fully coherent.

Going still further, the possibility of mixed-state two-sector coherences is open, but almost completely unexplored. The notion of two-sector coherence has not touched the fact that the light field occupies three (really five) vector spaces. In effect, the general pure state (15) or (20) has been treated as if an uncorrelated sector – the  $r$  sector in our example – could be factored off. However, the most general writing of that field (state) does not support such factoring, and the use of factoring implies that a special experimental set-up has been imagined that permits it. This is the same kind of factoring used historically that leads to our term 'diagonal' as a description of all standard measures of coherence. We now see that the 'off-diagonal' coherence we have introduced here is partially 'diagonal' in a higher dimensional sense. To be fully general in correlating the optical fields or states (15) and (20) to explore two-sector coherences, one should not factor the third sector but trace over it. This will mean that the remaining two-sector state will be mixed, but mixed in at least a four-dimensional rather than two-dimensional way [52].

This is a place where a natural confusion can be dispensed with. Obviously, from the writing in (19) it is clear that  $|\mathbf{E}\rangle = |x\rangle |E_x\rangle +|y\rangle |E_y\rangle$  is a pure state in the quantum sense – it is a bilinear tensor combination of vectors in two distinct Hilbert spaces. One frequently hears the question, how is a pure-state description possible for a classical field that is only partially coherent? The polarisation coherence matrix in (14) is the correct mixed-state, not pure-state, expression of the polarisation character of a partially coherent field, which seems to contradict the use of a pure-state expression in (19).

But there is no contradiction. The Dirac-denoted Shimony-Wolf field (pure state) in (19) can equally well be represented by its corresponding pure-state outer product  $|\mathbf{E}\rangle \langle \mathbf{E}|$  (density matrix when normalised to intensity  $I = \langle \mathbf{E}|\mathbf{E}\rangle$ ), and then the coherence matrix (14) is seen to be just the pure-state field's reduced density matrix, in two-dimensional polarisation space (indices  $xx, xy, yx, yy$ ), obtained by a trace (diagonal sum) of  $|\mathbf{E}\rangle \langle \mathbf{E}|$  over a complete set of orthonormal amplitude functions  $|\phi_m(t)\rangle$  for the components. That is, one easily shows, using  $\sum_{m}|\phi_{m}\rangle \langle \phi_{m}| = 1$  (see [26], Equation (6)), that

$$
\begin{array}{l} T r _ {\text {c o m p o n e n t s}} (| \mathbf {E} \rangle \langle \mathbf {E} |) = \Sigma_ {m} \langle \phi_ {m} | \mathbf {E} \rangle \langle \mathbf {E} | \phi_ {m} \rangle \\ = \Sigma_ {m} [ (| x \rangle \langle \phi_ {m} | E _ {x} \rangle + | y \rangle \langle \phi_ {m} | E _ {y} \rangle) \\ \times \left(\langle x | \langle E _ {x} | \phi_ {m} \rangle + \langle y | \langle E _ {y} | \phi_ {m} \rangle\right) ] \\ = | x \rangle \langle x | \Sigma_ {m} \left\langle E _ {x} \mid \phi_ {m} \right\rangle \left\langle \phi_ {m} \mid E _ {x} \right\rangle \\ + | x \rangle \langle y | \Sigma_ {m} \left\langle E _ {y} \mid \phi_ {m} \right\rangle \left\langle \phi_ {m} \mid E _ {x} \right\rangle + \dots \\ = \Sigma_ {p, q} | p \rangle \langle q | \langle E _ {q} | E _ {p} \rangle , (p, q = x \text {o r} y), \\ = | x \rangle \langle x | \langle E _ {x} | E _ {x} \rangle + | x \rangle \langle y | \langle E _ {y} | E _ {x} \rangle + | y \rangle \langle x | \langle E _ {x} | E _ {y} \rangle \\ + | y \rangle \langle y | \left\langle E _ {y} \mid E _ {y} \right\rangle , \tag {28} \\ \end{array}
$$

and the last line is exactly the coherence matrix in (14).

Incidentally, this derivation of (14) makes clear what defines the rows and columns of the vector space that the matrix lives in. It provides the systematically correct form in this vector space, differing from the conventional ad hoc assignment made in most of the literature.

# 8. Summary

We introduced the classical theory of partial coherence, and mentioned its background in the correlation theory of spectra for statistically random signals. Our examples based on a simplified expression for a typical light field were restricted to completely real fields, but more realistic examples are not conceptually different and don't lead to different conclusions. The three standard coherence matrices of the Wolfian theory were displayed to show their basis in two-point correlation functions, but we pointed out that they are all 'diagonal' correlations. This means that each of the two-point functions engages points chosen from the same sector of the three-sector super-space (i.e. choosing two different values for the same degree-of-freedom variable).

The sectors available for light are the familiar independent degrees of freedom: polarisation direction, spatial mode, and temporal function. For this three-sector space, we used the term correlation super-space to emphasise that its three sectors permit new categories of correlation not present in standard classical theory. They open the possibility for a new type of 'off-diagonal' correlations to be explored, those that correlate different degrees of freedom. The correlation super-space is actually larger than we employed because more spatial degrees of freedom than one are normally incorporated in beam modes. A significant work by Kagalwala et al. [6] was identified as following a similar approach in studying two crossed sectors using polarisation and discretised spatial modes.

We pointed out that many types of cross-sector coherence and their associated correlations, while missing from the standard classical theory of partial coherence, are known with examples in the quantum world. We recalled experimental tests of Bell inequalities to identify the CHSH method for introducing cross-sector correlations into the classical theory. The three criteria named by Shimony needing to be satisfied in making Bell inequality tests were

introduced. One of these criteria is entanglement, and we reviewed the definition of entanglement, including its use by Schrödinger in 1935, and the origin of the concept itself in the analysis of integral equations by Schmidt 30 years earlier, as cited by Schrödinger. Many treatments of entanglement in classical optics that have appeared in the past decade were cited. The importance of all three of Shimony's criteria, and their satisfaction, including entanglement, by the usual field examples in Wolf's theory prompted use of the term Shimony-Wolf field or state for the associated calculations.

Prompted by the quantum methods being followed, we introduced Dirac notation for convenience, but without incorporation of quantum properties. Then, guided by the CHSH specifications, we defined a time-polarisation cross-correlation coefficient  $C(a,b)$  and used the standard CHSH combination of  $C(a,b)$  coefficients to obtain the coherence measure  $S$ . We reviewed the results of recent experiments showing strong cross-sector coherence, confirming that the historically standard classical theory of partial polarisation can allow its coherence domain to be easily extended beyond the familiar 'diagonal' coherences (8)-(10) and their associated matrices. It is clear that the same procedure introduced here to exhibit the  $(t;p)$  cross-coherence can be applied to other 'off-diagonal' coherences. One can expect the counter-balanced signals concerning coexisting kinds of coherence exhibited by  $\mathcal{P}$  and  $S$  to be found for  $(r;p)$  cross coherence as well, while the possibility for a similar reciprocity of measures relevant to the  $(r;t)$  cross coherence remains open [11]. A different further exploration of cross-sector coherences will have to enter the domain where none of the vector-space sectors can be factored, requiring attention to entanglement measures among more than two sectors. Recent progress in this direction may be exploitable [52,53].

# Acknowledgements

It is a great pleasure to acknowledge discussions over many years with Emil Wolf, to thank many colleagues for frank and helpful debates, and to mention Xiao-Feng Qian and Bethany Little particularly for their creative theoretical and experimental contributions that allowed the data shown in Fig. 2 to be obtained.

# Disclosure statement

No potential conflict of interest was reported by the author.

# Funding

Partial financial support has been provided by National Science Foundation [grant number NSF PHY-0855701] and [grant number NSF PHY-1203931].

# Notes

1. Of course one may say that the field simply jumps from one fully polarised state to another so rapidly that no specific polarisation is able to be recorded. But in regard to detection, this is exactly the same as non-deterministic, and a theoretical

description of such a random process has to be effectively stochastic.

2. There are well-known measures of coherence that won't be treated here. One is correlations of higher order, of intensities or other combinations of more than two fields. The quantum theory of coherence based on photon counting raises entirely different considerations [9,10]. We will not enter this domain but recognise its existence by making sure that experimental examinations of classical results to be described below are not dependent on photon-counting detection techniques.  
3. The issue of "locality" often promotes a confusing discussion of tests of Bell inequalities. We accept Shimony's conclusion that what matters in such tests is the independence of the sectors of the joint vector space under examination, as in our polarisation and temporal function spaces. This is logically distinct from the locational separation of detectors that is employed in many experiments on photon pairs to ensure independence (for example, see [39-43]).

# Notes on contributor

Joseph Eberly's areas of active interest include racquetball, bald eagle tracking and the meaning of quantum mechanics. He enjoys introducing first-year undergrads to elements of quantum physics and repeatedly benefits from discovering with PhD students what can be learned about topics such as optical solitons in resonant media, superradiance, cavity QED and quantum revivals, non-diffracting Bessel beams, entanglement sudden death, non-spreading Trojan states of Rydberg electrons, Bell inequalities with classical entanglement and attosecond electron dynamics during multiphoton atomic ionisation. He is currently the Carnegie Professor of Physics and Professor of Optics in the University of Rochester, and has enjoyed times spent in visiting appointments in Warsaw, Boulder, Barcelona, Ulm, Auckland, Louvain, Brisbane, London, Fayetteville, Munich, Stanford and Austin.

# References

[1] E. Wolf, Introduction to the Theory of Coherence and Polarization of Light, Cambridge University Press, 2007. An earlier partial account is given in Phys. Lett. A 312 (2003), p. 263.  
[2] E. Wolf, A macroscopic theory of interference and diffraction of light from finite sources - II. Fields with a spectral range of arbitrary width, Proc. R. Soc. A 230 (1955), p. 246.  
[3] E. Wolf, Reciprocity inequalities, coherence time and bandwidth in signal analysis and optics, Proc. Phys. Soc. 71 (1958), p. 257.  
[4] E. Wolf, Coherence properties of partially polarized electromagnetic radiation, Nuovo Cimento 13 (1959), p. 165.  
[5] The formulation we have followed is closely modeled on M. Born and E. Wolf, Principles of Optics, Chapter 10, 7th ed., Cambridge University Press, Cambridge, 1999, especially Section. 10.3.  
[6] This has been clearly recognized in the detailed analysis of multiple state sectors, in connection with experiments in the space-polarization domain: K.H. Kagalwala, G. DiGiuseppe, A.F. Abouraddy, and B.E.A. Saleh, Bell's measure in classical optical coherence, Nat. Photonics. 7 (2013), p. 72. See also F. Gori, M. Santarsiero, and R. Borghi, Vector mode analysis of a Young interferometer, Opt. Lett. 31 (2006), p. 858.

[7] A complete orthonormal set of time functions directly determined by the random process itself can be obtained as eigenfunctions of the integral equation in which the kernel is the random signal's autocorrelation function M.Kac and J.F.Siegert, An explicit representation of a stationary gaussian process, Ann. Math. Stat. 18 (1947), pp. 438-442, and L. Mandel and E.Wolf, Optical Coherence and Quantum Optics, Chapter 2, Cambridge University Press, 1995.  
[8] For example, see C. Brosseau, Fundamentals of Polarized Light: A Statistical Optics Approach, Wiley, New York, 1998. E.Wolf, Introduction to the Theory of Coherence and Polarization of Light, Cambridge University Press, 2007.  
[9] R.J. Glauber, selected lectures with reprints in Quantum Optics and Electronics, C. DeWitt, ed., Gordon and Breach, New York, 1965. pp. ix-621.  
[10] L. Mandel and E. Wolf, Optical Coherence and Quantum Optics, Chapters 10-14, Cambridge University Press, Cambridge, 1995.  
[11] For example, see an analog Poincaré sphere representation for (t;r) off-diagonal 'polarization' in X.-F. Qian, et al, Transverse mode 'polarization' in optical beams, in Quantum Electronics I, Frontiers in Optics Conference, San Jose, CA, October 20, 2015.  
[12] A. Shimony, Contextual hidden variables theories and Bell's inequalities, Br. J. Philos. Sci. 35 (1984), pp. 25-45. See also A. Shimony, Bell's theorem, in Stanford Encycl. of Philosophy, 2009. Available at http://plato.stanford.edu/ entries/bell-theorem.  
[13] J.F. Clauser, M.A. Horne, A. Shimony, and R.A. Holt, Proposed experiment to test local hidden-variable theories, Phys. Rev. Lett. 23 (1969), p. 880.  
[14] J.F. Clauser and A. Shimony, Bell's theorem – experimental tests and implications, Rep. Prog. Phys. 41 (1978), pp. 1881–1927.  
[15] J.S. Bell, On the Einstein Podolsky Rosen paradox, Physics 1 (1964), pp. 195; J.S. Bell, On the problem of hidden variables in quantum mechanics, Rev. Mod. Phys. 38 (1966), pp. 447-452.  
[16] J.S. Bell, Speakable and Unspeakable in Quantum Mechanics, 2nd ed., Cambridge University Press, Cambridge, 2004, See Essays 4, 7, 16, and 24.  
[17] E. Schrödinger, Discussion of probability relations between separated systems, Proc. Cambridge Philos. Soc. 31 (1935), pp. 555. His reference to the classic mathematical physics text by Courant and Hilbert is key: Methoden der mathematischen Physik, 2nd ed., p. 134.  
[18] R.J.C. Spreeuw, A classical analogy of entanglement, Found. Phys. 28 (1998), pp. 361-374.  
[19] P.Ghose and M.K.Samal, EPR type nonlocality in classical electrodynamics, (2001), arXiv:quant-ph/0111119.  
[20] K.F. Lee and J.E. Thomas, Entanglement with classical fields, Phys. Rev. Lett. 88 (2002), p. 097902.  
[21] K.F. Lee, Observation of bipartite correlations using coherent light for optical communication, Opt. Lett. 34 (2009), p. 1099.  
[22] C.V.S. Borges, M. Hor-Meyll, J.A.O. Huguenin, and A.Z. Khoury, Bell-like Inequality for the spin-orbit separability of a laser beam, Phys. Rev. A 82 (2010), p. 033833.  
[23] M.A. Goldin, D. Francisco, and S. Ledesma, Simulating Bell inequality violations with classical optics encoded qubits, J. Opt. Soc. Am. 27 (2010), p. 779.  
[24] B.N. Simon, S. Simon, F. Gori, M. Santarsiero, R. Borghi, N. Mukunda, and R. Simon, Nonquantum entanglement resolves a basic issue in polarization optics, Phys. Rev. Lett. 104 (2010), pp. 023901. See also M. Sanjay Kumar and R. Simon, Characterization of Mueller matrices in polarization

optics, Opt. Commun. 88 (1992), pp. 464 and A. Aiello and J.P. Woerdman, Role of spatial coherence in polarization tomography, Opt. Lett. 30 (2005), p. 1599.  
[25] C. Gabriel, et al., Entangling different degrees of freedom by quadrature squeezing cylindrically polarized modes, Phys. Rev. Lett. 106 (2011), p. 060502.  
[26] X.F. Qian and J.H. Eberly, Entanglement and classical polarization states, Opt. Lett. 36 (2011), p. 4110. See also T. Setälä, A. Shevchenko, and A. Friberg, Degree of polarization for optical near fields Phys. Rev. E 66 (2002), pp. 016615, and J. Ellis and A. Dogariu, Optical polarimetry of random fields, Phys. Rev. Lett. 95 (2005), p. 203905.  
[27] C. Gabriel, A. Aiello, S. Berg-Johansen, et al., Tools for detecting entanglement between different degrees of freedom in quadrature squeezed cylindrically polarized modes, Eur. Phys. J. D 66 (2012), p. 172.  
[28] K.H. Kagalwala, G. DiGiuseppe, A.F. Abouraddy, and B.E.A. Saleh, Bell's measure in classical optical coherence, Nat. Photonics 7 (2013), p. 72.  
[29] F. Töppel, A. Aiello, C. Marquardt, E. Giacobino, and G. Leuchs, Classical entanglement in polarization metrology, New J. Phys. 16 (2014), p. 073019.  
[30] A. Aiello et al, Quantum-like nonseparable structures in optical beams, New J. Phys. 17 (2015), pp. 043024. See also Annemarie Holleczek, et al. Poincaré sphere representation for classical inseparable Bell-like states of the electromagnetic field, (2010), arXiv:1007.2528.  
[31] Yi Fan Sun, Xinbing Song, Hongwei Qin, et al., Non-local classical optical correlation and implementing analogy of quantum teleportation, Sci. Rep. 5 (2015), p. 9175.  
[32] X.F. Qian, Bethany Little, J.C. Howell, and J.H. Eberly, Shifting the quantum-classical boundary: theory and experiment for statistically classical optical fields, Optica 2 (2015), p. 611.  
[33] S.M. Hashemi, M. Mirhosseini, O.S. Magana-Loaiza, et al., Teleportation via classical entanglement, (2015). arXiv:1504.00697.  
[34] S.Berg-Johansen et al., Classically entangled optical beams for high-speed kinematic sensing, (2015), arXiv:1504.00697.  
[35] B. Stoklasa, L. Motka, and J. Rehacek et al, Experimental violation of a Bell-like inequality with optical vortex beams, (2015), arXiv:1505.06103.  
[36] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47 (1935), p. 777.  
[37] The original paper is: E. Schmidt, Zur Theorie der linearen und nichtlinearen Integralgleichungen. 1. Entwicklung willküriger Funktionen nach Systeme vorgeschriebener, Math. Ann. 63 (1907), p. 433. See, for example, A. Ekert and P.L. Knight, Entangled quantum-systems and the Schmidt decomposition, Am. J. Phys. 63 (1995), p. 415. The Schmidt theorem is the analytic function analog of the singularvalue decomposition theorem for matrices. For background, see M.V. Fedorov and N.I. Miklin, Schmidt modes and entanglement, Contem. Phys. 55 (2014), p. 94.

[38] N. Gisin, Bell's inequality holds for all non-product states, Phys. Lett. A 154 (1991), p. 201.  
[39] S.J. Freedman and J.F. Clauser, Experimental test of local hidden-variable theories, Phys. Rev. Lett. 28 (1972), p. 938.  
[40] A. Aspect, P. Grangier, and G. Roger, Experimental realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment: a new violation of Bell's inequalities, Phys. Rev. Lett. 49 (1982), p. 91. and A. Aspect, J. Dalibard, and G. Roger, Experimental test of Bell's inequalities using time-varying analyzers, Phys. Rev. Lett. 49 (1982), p. 1804.  
[41] E.S. Fry and R.C. Thompson, Experimental test of local hidden-variable theories, Phys. Rev. Lett. 37 (1976), pp. 465-468.  
[42] Z.Y. Ou and L. Mandel, Violation of Bell's inequality and classical probability in a 2-photon correlation experiment, Phys. Rev. Lett. 61 (1988), p. 50.  
[43] Y.-H. Shih and C.O. Alley, New type of Einstein-Podolsky-Rosen-Bohm experiment using pairs of light quanta produced by optical parametric down conversion, Phys. Rev. Lett. 61 (1988), p. 2921.  
[44] W.H.Zurek, in response to a pre-publication description of [29] in the Academia Leopldina Workshop Quantum technologies, München, May 9-10, 2011.  
[45] F. De Zela, Relationship between the degree of polarization, indistinguishability, and entanglement, Phys. Rev. A 89 (2014), p. 013845.  
[46] D.M. Greenberger and A. Yasin, Simultaneous wave and particle knowledge in a neutron interferometer, Phys. Lett. A 128 (1988), p. 391.  
[47] L. Mandel, Coherence and indistinguishability, Opt. Lett. 16 (1991), p. 1882.  
[48] G. Jaeger, M.A. Horne, and A. Shimony, Complementarity of One-particle and Two-particle Interference, Phys. Rev. A 48 (1993), pp. 1023-1027.  
[49] G. Jaeger, A. Shimony, and L. Vaidman, Two interferometric complementarities, Phys. Rev. A 51 (1995), pp. 54-67.  
[50] B.-G. Englert, Fringe visibility and which-way information: an inequality, Phys. Rev. Lett. 77 (1996), p. 2154.  
[51] M. Lahiri, Wave-particle duality and polarization properties of light in single-photon interference experiments, Phys. Rev. A 83 (2011), p. 045803.  
[52] See A. Al-Qasimi, et al., for a study of the role of two-sector mixed-state entanglement following a higher-sector tracing (in preparation).  
[53] See X.-F. Qian, M.A. Alonso, and J.H. Eberly, Entanglement constraints in multi-qubit systems, in Quantum Electronics I, Frontiers in Optics Conference, San Jose, CA, October 20, 2015.