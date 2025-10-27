sible without the devoted effort of the personnel of the Orbiting Geophysical Observatory office at the Goddard Space Flight Center and at TRW.

*Research supported in part under National Aeronautics and Space Administration Contract No. NAS 5-9096 and Grant No. NGR 14-001-005.

†Present address: Department of Physics, The University of Arizona, Tucson, Ariz.

$\ddagger$ Also Department of Physics.

$^{1}$ K. P. Beuermann, C. J. Rice, E. C. Stone, and R. E. Vogt, Phys. Rev. Letters 22, 412 (1969).  
$^{2}$ J. L'Heureux and P. Meyer, Can. J. Phys. 46, S892 (1968).  
$^{3}$ J. Rockstroh and W. R. Webber, University of Minnesota Publication No. CR-126, 1969.  
4G. M. Simnett and F. B. McDonald, Goddard Space Flight Center Report No. X-611-68-450, 1968 (to be published).  
5W.R.Webber，J.Geophys.Res.73，4905(1968).  
$^{6}$ P. B. Abraham, K. A. Brunstein, and T. L. Cline, Phys. Rev. 150, 1088 (1966).

# PROPOSED EXPERIMENT TO TEST LOCAL HIDDEN-VARIABLE THEORIES*

John F. Clausert†

Department of Physics, Columbia University, New York, New York 10027

and

Michael A. Horne

Department of Physics, Boston University, Boston, Massachusetts 02215

and

Abner Shimony

Departments of Philosophy and Physics, Boston University, Boston, Massachusetts 02215

and

Richard A. Holt

Department of Physics, Harvard University, Cambridge, Massachusetts 02138

(Received 4 August 1969)

A theorem of Bell, proving that certain predictions of quantum mechanics are inconsistent with the entire family of local hidden-variable theories, is generalized so as to apply to realizable experiments. A proposed extension of the experiment of Kocher and Commins, on the polarization correlation of a pair of optical photons, will provide a decisive test between quantum mechanics and local hidden-variable theories.

Einstein, Podolsky, and Rosen (EPR) in a classic paper presented a paradox which led them to infer that quantum mechanics is not a complete theory. They concluded that the quantum mechanical description of a physical system should be supplemented by postulating the existence of "hidden variables," the specification of which would predetermine the result of measuring any observable of the system. They believed the predictions of quantum mechanics to be correct, but only as consequences of statistical distributions of the hidden variables. Bohr argued in reply that no paradox can be derived from the assumption of completeness if one recognizes that quantum mechanics concerns only the interaction of microsystems with experimental apparatus and not their intrinsic character.

There is an extensive literature purporting to prove the inconsistency of hidden-variable theories with the statistical predictions of quantum mechanics. These proofs, though mathematically valid, rest upon physically unrealistic postulates. $^3$  Bell $^4$  succeeded in replacing these postulates by a physically reasonable condition of locality. He showed that in a Gedankenexperiment of Bohm $^5$  (a variant of that of EPR) no local hidden-variable theory can reproduce all of the statistical predictions of quantum mechanics. This result is somewhat ironical in view of Einstein's convictions $^6$  that quantum mechanical predictions concerning spatially separated systems are incompatible with his conditions for locality unless hidden variables exist.

Bell's theorem has profound implications in that it points to a decisive experimental test of the entire family of local hidden-variable theories. The aim of this paper is to propose explicitly such an

experiment. For this purpose, we first present a generalization of Bell's theorem which applies to realizable experiments. Second, we indicate that neither of the experimental realizations<sup>7</sup> of Bohm's Gedankenexperiment has produced evidence against local hidden-variable theories, even though the results of both are compatible with quantum mechanical predictions. Third, we show that a simple extension of one of these experiments can provide a decisive test.

Generalization of Bell's theorem.-Consider an ensemble of correlated pairs of particles moving so that one enters apparatus  $\mathbf{I}_a$  and the other apparatus  $\mathbf{II}_b$ , where  $a$  and  $b$  are adjustable apparatus parameters. In each apparatus a particle must select one of two channels labeled +1 and -1. Let the results of these selections be represented by  $A(a)$  and  $B(b)$ , each of which equals  $\pm 1$  according as the first or second channel is selected.

Suppose now that a statistical correlation of  $A(a)$  and  $B(b)$  is due to information carried by and localized within each particle, and that at some time in the past the particles constituting one pair were in contact and communication regarding this information. The information, which emphatically is not quantum mechanical, is part of the content of a set of hidden variables, denoted collectively by  $\lambda$ . The results of the two selections are then to be deterministic functions  $A(a, \lambda)$  and  $B(b, \lambda)$ . Locality reasonably requires  $A(a, \lambda)$  to be independent of the parameter  $b$  and  $B(b, \lambda)$  to be likewise independent of  $a$ , since the two selections may occur at an arbitrarily great distance from each other. Finally, since the pair of particles is generally emitted by a source in a manner physically independent of the adjustable parameters  $a$  and  $b$ , we assume that the normalized probability distribution  $\rho(\lambda)$  characterizing the ensemble is independent of  $a$  and  $b$ .

Defining the correlation function  $P(a, b) \equiv \int_{\Gamma} A(a, \lambda) B(b, \lambda) \rho(\lambda) d\lambda$ , where  $\Gamma$  is the total  $\lambda$  space, we have

$$
\begin{array}{l} \left| P (a, b) - P (a, c) \right| \leqslant \int_ {\Gamma} | A (a, \lambda) B (b, \lambda) - A (a, \lambda) B (c, \lambda) | \rho (\lambda) d \lambda = \int_ {\Gamma} | A (a, \lambda) B (b, \lambda) | [ 1 - B (b, \lambda) B (c, \lambda) ] \rho (\lambda) d \lambda \\ = \int_ {\Gamma} [ 1 - B (b, \lambda) B (c, \lambda) ] \rho (\lambda) d \lambda = 1 - \int_ {\Gamma} B (b, \lambda) B (c, \lambda) \rho (\lambda) d \lambda . \\ \end{array}
$$

Suppose that for some  $b'$  and  $b$  we have  $P(b', b) = 1 - \delta$ , where  $0 \leqslant \delta \leqslant 1$ . Experimentally interesting cases will have  $\delta$  close to but not equal to zero. Here we avoid Bell's experimentally unrealistic restriction that for some pair of parameters  $b'$  and  $b$  there is perfect correlation (i.e.,  $\delta = 0$ ). Dividing  $\Gamma$  into two regions  $\Gamma_{+}$  and  $\Gamma_{-}$  such that  $\Gamma_{\pm} = \{\lambda | A(b', \lambda) = \pm B(b, \lambda)\}$ , we have  $\int_{\Gamma_{-}} \rho(\lambda) d\lambda = \frac{1}{2} \delta$ . Hence,

$$
\begin{array}{l} \int_ {\Gamma} B (b, \lambda) B (c, \lambda) \rho (\lambda) d \lambda = \int_ {\Gamma} A (b ^ {\prime}, \lambda) B (c, \lambda) \rho (\lambda) d \lambda - 2 \int A (b ^ {\prime}, \lambda) B (c, \lambda) \rho (\lambda) d \lambda \\ \geqslant P \left(b ^ {\prime}, c\right) - 2 \int_ {\Gamma_ {-}} \left| A \left(b ^ {\prime}, \lambda\right) B (c, \lambda) \right| \rho (\lambda) d \lambda = P \left(b ^ {\prime}, c\right) - \delta , \\ \end{array}
$$

and therefore

$$
\left| P (a, b) - P (a, c) \right| \leqslant 2 - P \left(b ^ {\prime}, b\right) - P \left(b ^ {\prime}, c\right). \tag {1a}
$$

In the experiment proposed below  $P(a, b)$  depends only on the parameter difference  $b - a$ . Defining  $\alpha \equiv b - a$ ,  $\beta \equiv c - b$ , and  $\gamma \equiv b - b'$ , we have

$$
\left| P (\alpha) - P (\alpha + \beta) \right| \leqslant 2 - P (\gamma) - P (\beta + \gamma). \tag {1b}
$$

In principle entire measuring devices, each consisting of a filter followed by a detector, could be used for \( \mathbf{I}_a \) and \( \mathbf{II}_b \), and the values \( \pm 1 \) of \( A(a) \) and \( B(b) \) would denote detection or nondetection of the particles. Inequalities (1) would then apply directly to experimental counting rates. Unfortunately, if the particles are optical photons (as in the experiment proposed below) no practical tests of (1) can presently be performed in this way, because available photoelectric efficiencies are rather small. We shall therefore henceforth interpret \( A(a) = \pm 1 \) and \( B(b) = \pm 1 \) to mean emergence or nonemergence of the photons from the respective filters. Also the filters will be taken to be linear polarization filters, and \( a \) and \( b \) will represent their orientations. It will be convenient to introduce an exceptional value \( \infty \) of the parameter \( a \) (and likewise of \( b \)) to represent the removal of a polarizer; clearly, \( A(\infty) \) and \( B(\infty) \) necessarily equal \( +1 \). Since \( P(a,b) \) is an emergence correlation function, in order to derive an experimental prediction from (1) an additional assumption must be made: that if a pair of photons emerges from \( \mathbf{I}_a, \mathbf{II}_b \) the probability of their joint detection is independent of \( a \) and \( b \). Then if the flux into \( \mathbf{I}_a, \mathbf{II}_b \) is a constant independent of \( a \) and \( b \), the rate of coincidence detection \( R(a,b) \) will be proportional to \( w[A(a)_+,B(b)_+] \), where \( w[A(a)_\pm,B(b)_\pm] \) is the probability that \( A(a) = \pm 1 \) and \( B(b) = \pm 1 \). Letting \( R_0 = R(\infty,

$\infty)$ ,  $R_{1}(a) = R(a, \infty)$ , and  $R_{2}(b) = R(\infty, b)$ , making use of the evident formulas

$$
P (a, b) = w [ A (a) _ {+}, B (b) _ {+} ] - w [ A (a) _ {+}, B (b) _ {-} ] - w [ A (a) _ {-}, B (b) _ {+} ] + w [ A (a) _ {-}, B (b) _ {-} ]
$$

and

$$
w [ A (a) _ {+}, B (\infty) _ {+} ] = w [ A (a) _ {+}, B (b) _ {+} ] + w [ A (a) _ {+}, B (b) _ {-} ],
$$

and of similar formulas for  $w[A(\infty)_+, B(b)_+]$  and  $w[A(\infty)_+, B(\infty)_+]$ , we obtain

$$
P (a, b) = \frac {4 R (a , b)}{R _ {0}} - \frac {2 R _ {1} (a)}{R _ {0}} - \frac {2 R _ {2} (b)}{R _ {0}} + 1.
$$

We can now express (1) in terms of experimental quantities, namely coincidence rates with both polarizers in, and with one and then the other removed. If  $R_{1}(a)$  and  $R_{2}(b)$  are found experimentally to be constants  $R_{1}$  and  $R_{2}$ , the result is

$$
\left| R (a, b) - R (a, c) \right| + R \left(b ^ {\prime}, b\right) + R \left(b ^ {\prime}, c\right) - R _ {1} - R _ {2} \leqslant 0. \tag {2a}
$$

In the special case in which  $P(a, b) = P(a - b)$ , (2a) becomes

$$
\left| R (\alpha) - R (\alpha + \beta) \right| + R (\gamma) + R (\beta + \gamma) - R _ {1} - R _ {2} \leqslant 0. \tag {2b}
$$

Existing experimental results. -Bohm's Gedankenexperiment, involving correlated spin- $\frac{1}{2}$  particles, has not been performed, nor does it appear to be easily realizable. Two related experiments have been performed on polarization correlation of photons. Wu and Shaknov (WS)<sup>7</sup> examined polarization correlation of 0.5-MeV  $\gamma$  rays emitted during positronium annihilation.<sup>9</sup> Although the polarization state of the pair is suitable for our purposes, their high energy requires the use of Compton polarimeters. Thus, instead of directly examining the polarization correlation, WS examined the polarization-dependent joint distribution for Compton scattering of the pair. Inequality (2) cannot be immediately applied to such a scattering experiment because neither photon is forced to make a binary decision. However, a suitable binary result may be imposed by partitioning the scattering sphere into two arbitrary regions, denoted, respectively, by  $\pm 1$ , and by letting the adjustable parameter  $a$  (or  $b$ ) designate the particular mode of partitioning. But as one can see<sup>10</sup> by examining the joint scattering distribution,<sup>11</sup> no such partitioning can yield a correlation in violation of (2). The essential difficulty is that the direction of Compton scattering of a photon is a statistically weak index of its linear polarization.

The other experiment, that of Kocher and Commins (KC),<sup>7</sup> involved polarization correlation of photon pairs emitted in the  $6^{1}S_{0}\rightarrow 4^{1}P_{1}\rightarrow 4^{1}S_{0}$  cascade of calcium. Since the two photons are in the visible, filters of the Polaroid type could be used. The photons impinged normally upon a pair of these polarizers whose planes were parallel, and the polarization correlation was measured with standard coincidence techniques. With this arrangement inequality (2b) is applicable upon assumption of a local hidden-variable theory. However, the data obtained by KC do not suffice to test (2b), because their polarizers were not highly efficient and were placed only in the relative orientations  $0^{\circ}$  and  $90^{\circ}$ .

Proposed experiment. A decisive test can be obtained by modifying the KC experiment to include observations at two appropriate relative orientations of the polarizers, and also with one and then the other removed. For realizable apparatus, quantum mechanics predicts violation of inequality (2b).

Define  $\epsilon_{M}^{i}$  as the efficiency of the polarizer  $i$  ( $i = \mathbf{I}, \mathbf{II}$ ) for light polarized parallel to the polarizer axis and  $\epsilon_{m}^{i}$  as that for light perpendicularly polarized. Consider a point source and filter-detector assemblies, each of which gathers the photons emitted into a cone of half-angle  $\theta$ . Then for a  $J = 0 \rightarrow J = 1 \rightarrow J = 0$  electric-dipole cascade (0-1-0) the quantum mechanical predictions for the counting rates are<sup>10</sup>

$$
\begin{array}{l} R (\varphi) / R _ {0} = \frac {1}{4} \left(\epsilon_ {M} ^ {\mathrm {I I}} + \epsilon_ {m} ^ {\mathrm {I}}\right) \left(\epsilon_ {M} ^ {\mathrm {I I}} + \epsilon_ {m} ^ {\mathrm {I I}}\right) + \frac {1}{4} \left(\epsilon_ {M} ^ {\mathrm {I}} - \epsilon_ {m} ^ {\mathrm {I}}\right) \left(\epsilon_ {M} ^ {\mathrm {I I}} - \epsilon_ {m} ^ {\mathrm {I I}}\right) F _ {\mathbf {1}} (\theta) \cos 2 \varphi , \\ R _ {1} / R _ {0} = \frac {1}{2} \left(\epsilon_ {M} ^ {\mathrm {I}} + \epsilon_ {m} ^ {\mathrm {I}}\right), \quad R _ {2} / R _ {0} = \frac {1}{2} \left(\epsilon_ {M} ^ {\mathrm {I I}} + \epsilon_ {m} ^ {\mathrm {I I}}\right). \tag {3} \\ \end{array}
$$

Here  $\varphi$  is the angle between the polarizer axes,

$$
\boldsymbol {F} _ {1} (\theta) = 2 \boldsymbol {G} _ {1} ^ {2} (\theta) \left[ \boldsymbol {G} _ {2} ^ {2} (\theta) + \frac {1}{2} \boldsymbol {G} _ {3} ^ {2} (\theta) \right] ^ {- 1},
$$

and

$$
G _ {1} (\theta) = \frac {1}{4} \left(\frac {4}{3} - \cos \theta + \sin^ {2} \theta - \frac {1}{3} \cos^ {3} \theta\right), \quad G _ {2} (\theta) = \frac {2}{3} - \frac {1}{3} \left(\sin^ {2} \theta + 2\right) \cos \theta , \quad G _ {3} (\theta) = \frac {4}{3} - \cos \theta - \frac {1}{3} \cos^ {3} \theta .
$$

The predictions for a 0-1-1 electric-dipole cascade (and for a 1-1-0, provided the initial statistical state of the atom is isotropic) are obtained from (3) upon replacing  $F_{1}(\theta)$  with  $-F_{2}(\theta)$  where

$$
F _ {2} (\theta) = 2 G _ {1} ^ {2} (\theta) \left[ 2 G _ {2} (\theta) G _ {3} (\theta) + \frac {1}{2} G _ {3} ^ {2} (\theta) \right] ^ {- 1}.
$$

For sufficiently efficient polarizers one easily sees that there exist sets of relative orientations for which the quantum mechanical counting rates violate Inequality (2b). The greatest violation always occurs at  $\alpha = 22.5^{\circ}$ ,  $\beta = 45^{\circ}$ , and  $\gamma = 157.5^{\circ}$  for the 0-1-0 cascade and at  $\alpha = 67.5^{\circ}$ ,  $\beta = 135^{\circ}$ , and  $\gamma = 112.5^{\circ}$  for the 0-1-1 cascade. Note that in each case the four angles  $\alpha$ ,  $\alpha + \beta$ ,  $\gamma$ , and  $\beta + \gamma$  which occur in Inequality (2b) characterize only two distinct relative orientations of the polarizers, namely  $22.5^{\circ}$  and  $67.5^{\circ}$ .

In an actual experiment  $F_{j}(\theta)$  is less than 1, because of finite half-angle  $\theta$ , and  $\epsilon_{M}$  is never unity. Assuming the use of calcite polarizers (for which  $\epsilon_{m} \approx 10^{-5}$ ), taking  $\epsilon_{M}^{\mathrm{I}} = \epsilon_{M}^{\mathrm{II}} = \epsilon_{M}$  for simplicity, and using the above choices for  $\alpha$ ,  $\beta$ , and  $\gamma$ , we find that for either type of cascade, the condition for violation of Inequality (2b) is

$$
\sqrt {2} F _ {j} (\theta) + 1 > 2 / \epsilon_ {M}. \tag {4}
$$

This is the essential requirement on the design of a decisive experiment. For given  $F_{j}(\theta)$ , (4)

![](images/7473608657573434437889abd47eb3fb03bd9169b43738551a6ace2c24212108.jpg)  
FIG. 1. Upper limits on detector half-angle  $\theta$  as a function of polarizer efficiency  $\epsilon_{M}$ . To test for hidden-variable theories, the experiment must be performed in the region below the appropriate curve—the upper curve for a 0-1-0 cascade, the lower for a 0-1-1.

implies a lower limit on  $\epsilon_{M}$ , and vice versa. Since both  $F_{1}(\theta)$  and  $F_{2}(\theta)$  are monotonically decreasing functions, a lower limit on  $F_{j}(\theta)$  implies an upper limit on  $\theta$ . Condition (4) and numerical evaluation of  $F_{1}(\theta)$  and  $F_{2}(\theta)$  lead to the curves shown in Fig. 1, from which one can directly read combinations of  $\theta$  and  $\epsilon_{M}$  suitable for a decisive experiment. The experiment can be performed with uncoated calcite polarizers ( $\epsilon_{M} \approx 0.92$ ); however, if the polarizers have antireflection coatings ( $\epsilon_{M} \approx 0.95$ ), a larger  $\theta$  and hence a larger counting rate can be achieved.

The authors gratefully acknowledge helpful discussions with Y. Aharonov, M. Jammer, L. Kasday, D. Nartonis, C. Papaliolios, F. Pipkin, D. Pritchard, J. L. Snider, H. Stein, and C. R. Willis.

vert hidden-variable emergence rates into quantum mechanical counting rates.

It has been shown by D. Bohm and Y. Aharonov, Phys. Rev. 108, 1070 (1957), that the WS experiment is a decisive refutation of a hypothesis studied by W. H.

Furry, Phys. Rev. 49, 393, 476 (1936).

10For details see M.A.Horne,thesis,Boston University,1969 (unpublished).

11The distribution is given in H. S. Snyder, S. Pasternack, and J. Hornbostel, Phys. Rev. 73, 440 (1948).

$\Xi$  RESONANCES IN  $K^{-}p \to \Xi \pi K$  AT 2.87 GeV/c*

S. Apsell, N. Barash-Schmidt, L. Kirsch, and P. Schmidt  
artment of Physics, Brandeis University, Waltham, Massachusetts 02154

and

C. Y. Chang, R. J. Hemingway, B. V. Khoury, A. R. Stottlemyer, H. Whiteside, $\dagger$  and G. B. Yodh  
Department of Physics and Astronomy, University of Maryland, College Park, Maryland 20742

and

M. Goldberg, K. Jaeger, C. McCarthy, B. Meadows, and G. C. Moneti‡  
Department of Physics, Syracuse University, Syracuse, New York 13210

and

J. Bartley, R. M. Dowd, J. Schneps, and G. Wolsky

Department of Physics, Tufts University, Medford, Massachusetts 02155 (Received 25 August 1969)

Evidence is presented for four  $\Xi$  resonances in the reaction  $K^{-}p\rightarrow \Xi^{-}\pi^{+}K^{0}$ . In addition to the well known  $\Xi (1530)$ , significant structures are observed in the  $\Xi \pi$  system at masses of 1630, 1800, and 1960 MeV, although the latter two are not statistically distinguishable from a single broad structure at 1950 MeV. No significant enhancements at these masses are observed in the  $\Xi^{-}\pi^{0}K^{+}$ final state.

$\Xi$  resonances are produced with relatively small cross sections, cannot be studied in formation experiments, and have complex decay topologies. For these reasons, only large bubble-chamber exposures have yielded significant information bearing on the existence and properties of these particles. This experiment, designed for the study of  $\Xi$  resonances below a mass of  $2\mathrm{GeV}$ , involves  $10^{6}$  pictures of  $K^{-}p$  interactions at 2.87 GeV/c taken at the Brookhaven National Laboratory 31-in. bubble chamber at the alternating-gradient synchrotron. $^{1}$  The equivalent of 24 events/ $\mu\mathrm{b}$  has been accumulated to date. In this Letter, we report on  $\Xi\pi$  mass spectra observed in the reactions

$$
K ^ {-} p \rightarrow \Xi^ {-} \pi^ {+} K ^ {0}, \tag {1}
$$

$$
K ^ {-} p \rightarrow \Xi^ {-} \pi^ {0} K ^ {+}. \tag {2}
$$

For this study, all film was scanned twice for events with at least two visible decays of strange particles. Those events with one or more successful kinematic fits (confidence level  $\geqslant 0.1\%$  were inspected for consistency with observed ionizations. A total of 635 events achieved a unique

fit to Reaction (1), while 265 events fit Reaction (2) uniquely. The 94 events fitting both reactions<sup>2</sup> have been apportioned to each with a weight of 0.5.

The Dalitz plot for Reaction (1), shown in Fig. 1, shows strong production of  $\Xi^0$  (1530) and

![](images/bfd8e1e81b901ce687bf524adad016b9dac5f703047b929cc4f4e43b05daddd5.jpg)

![](images/a3d0568589cc0e36bcb4ebc1a756e150a9fc9684efd5d3dc86306d98753d87e0.jpg)  
FIG. 1. Dalitz plot for the reaction  $K^{-}p \rightarrow \Xi^{-}\pi^{+}K^{0}$  with  $M^2 (\Xi^{-}\pi^{+})$  and  $M^2 (K^0\pi^+)$  projections.

![](images/c304020eaa26840405a2fed35c9c0d1becc12d7de1a6d6afb3ee30f37e51dce6.jpg)