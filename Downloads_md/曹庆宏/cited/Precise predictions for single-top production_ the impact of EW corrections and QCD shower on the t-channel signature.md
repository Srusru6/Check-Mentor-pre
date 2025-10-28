# Precise predictions for single-top production: the impact of EW corrections and QCD shower on the  $t$ -channel signature

Rikkert Frederix, $^{a}$  Davide Pagani $^{b}$  and Ioannis Tsinikos $^{b}$

${}^{a}$  Theoretical Particle Physics,Department of Astronomy and Theoretical Physics,Lund University, Sølvegatan 14A,SE-223 62 Lund,Sweden  
${}^{b}$  Technische Universität München, James-Franck-Str. 1, D-85748 Garching, Germany

E-mail: rikkert.frederix@thep.lu.se, davide pagani@tum.de, ioannis.tsinikos@tum.de

ABSTRACT: In this work we calculate and provide precise predictions for the signature that is typically exploited at the LHC for the measurement of  $t$ -channel single-top production: 1 lepton, 1 light jet, 1  $b$ -jet,  $E_T$  and no additional jets or leptons. We apply the cuts that define the fiducial region and we take into account all the contributions to this signature; not only those from resonant  $t$ -channel single-top production. On the one hand, we calculate the complete-NLO corrections, i.e., all NLO effects of QCD and EW origin. On the other hand, we study in detail the impact of a QCD parton shower for the fiducial region we consider. We provide predictions in different approximations at the inclusive level and for several differential distributions. Our study demonstrates the relevance of both EW corrections and shower effects for obtaining precise and reliable theoretical predictions for the single-top-production fiducial region.

KEYWORDS: NLO Computations, QCD Phenomenology

ARXIV EPRINT: 1907.12586

# Contents

# 1 Introduction 1

# 2 Calculational frameworks 3

2.1 Fixed-order complete-NLO predictions 3

2.1.1 Structure of the calculation: underlying resonances and notation 4  
2.1.2 Input parameters 6  
2.1.3 Clustering procedure 7

2.2 Shower effects matched to NLO QCD 8

# 3 Results 9

3.1 Fiducial region 9  
3.2 Fixed order 10

3.2.1 Total cross section 10  
3.2.2 Differential distributions 12

3.3 Shower effects matched to NLO QCD 21

3.3.1 Total cross section 21  
3.3.2 Differential distributions 24

# 4 Conclusions 27

# A Comparisons with previous results and different approximations 29

# 1 Introduction

The electroweak production of top quarks in hadron-hadron collisions can be categorised in three main production channels, which all involve a single top (anti)quark in the final state and a  $Wtb$  interaction vertex. The three different channels can be distinguished according to the virtuality of the  $W$  boson appearing in the Feynman diagrams. If the  $W$  is space-like, the category is called  $t$ -channel, if the  $W$  is instead time-like the category is called  $s$ -channel and in the case of a final-state (on-shell)  $W$  boson we refer to  $tW$  associated production.

At the Large Hadron Collider (LHC) the category with the largest production rate is the  $t$ -channel, with about 225 pb at 13 TeV, of which approximately 135 pb is coming from top production and the rest from anti-top production. Within the SM the interest in single-top production is mainly motivated by the possibility of directly extracting the value of  $|V_{tb}|$  in the CKM matrix element [1-5]. Moreover, in numerous BSM scenarios, single-top production provides a sensitive probe to New Physics effects [6-16], possibly parametrised through dimension-6 operators [14-18]. Indeed, involving the heaviest of the SM particles and EW interactions, this class of processes is of paramount interest for physics beyond-the-SM (BSM).

The total cross section for  $t$ -channel single-top production was first measured at the Tevatron about 10 years ago [19, 20], albeit with large uncertainties. The high-precision data from the LHC allowed not only for a well-established measurement of the total production cross sections, but also for a precise determination of differential distributions at the centre-of-mass energies of 7, 8, and  $13\mathrm{TeV}$  [21-29].

The top quarks decay (predominantly) to a  $W$ -boson and a  $b$ -quark. In order to be able to tag the  $t$ -channel single-top production process experimentally, only leptonic decays of  $W$  bosons are considered. With hadronic  $W$  decays the signature would be indistinguishable from the multi-jet background, which has a cross section that is many orders of magnitude larger than the  $t$ -channel signature. Hence, the typical signature that is analysed involves one  $b$ -jet from the top decay, missing transverse-energy and one high- $p_T$  lepton from the decay of the  $W$ -boson emerging from the top-quark decay, and one additional light jet, which is associated to the light parton present in the LO  $t$ -channel matrix elements.

On the theoretical front, predictions for  $t$ -channel single-top quark production have been known at the NLO accuracy in QCD for quite some time [30-33] in the five flavour scheme (5FS), and for about ten years in the four-flavour scheme (4FS) [34-36]. Much more recently, also the NNLO corrections have been computed [37], also including the decay of the top quark in the narrow width approximation up to the same level of accuracy, but neglecting some interference contributions in the NNLO corrections [38, 39]. The NLO corrections in the electroweak coupling have been computed [40-42] and are found to be small for the inclusive production, but can be significantly enhanced in certain regions of phase space. Going beyond the narrow-width approximation for the top quarks, off-shell effects have been studied at fixed-order perturbation theory in refs. [43-45].

Beyond fixed-order perturbation theory, the all-order analytic resummation of threshold and transverse momentum logarithms have been presented in refs. [46, 47] and ref. [48], respectively. Monte Carlo simulations, in which the NLO single-top production processes have been matched to a parton shower are available in the MC@NLO [45, 49-52], Sherpa [53] and POWHEG [51, 54, 55] frameworks. Within the latter framework, also the consistent inclusion of the single-top plus one-jet NLO matrix elements has been considered through the (extended) MINLO method [56].

The main focus of this paper is to re-visit single-top production in the  $t$ -channel in a suitably defined fiducial region of phase space. The motivation is as follows. Although the categorisation of the three main single-top production channels is well-defined at lowest order in perturbation theory, it breaks down when including higher-order quantum corrections. Indeed, interferences between the  $t$ -channel and the other production modes are non-zero. Also, from an experimental point of view, the virtuality of the  $W$ -boson, which defines the categorisation, is not a direct observable. This, formally, also breaks down the categorisation from an experimental point of view. Therefore, in this work we do not include only  $t$ -channel single-top production into our predictions and simulations. Rather, we include all contributions that produce exactly an electron, a neutrino and exactly a jet-pair, of which only one is  $b$ -tagged, and consider a fiducial region that is dominated by  $t$ -channel single-top production. We calculate all LO terms and all the complete-NLO corrections, i.e., all NLO effects of QCD and EW origin are taken into account. Furthermore,

we study in detail the impact of the parton shower on the predictions for the  $t$ -channel fiducial region.

This paper is organised as follows. In section 2 we describe the two different frameworks used in this work: complete-NLO accuracy at fixed order, in section 2.1, and NLO QCD corrections matched to shower effects, in section 2.2. Then, we present numerical predictions at the inclusive and differential level for several phenomenologically relevant distributions in section 3, for both the aforementioned approximations. Finally, in section 4 we write our conclusions and we summarise our findings. Furthermore, in appendix A we collect comparisons with previous results and among different approximations.

# 2 Calculational frameworks

In this section we describe the two calculational frameworks on which the results presented in section 3 are based. Our main focus is providing precise predictions for  $t$ -channel single-top production with subsequent top-quark leptonic decays. Therefore, we consider the signature

$$
e ^ {+}, 1 \text {l i g h t j e t ,} 1 b - \text {j e t ,} \not E _ {T} \text {a n d n o a d d i t i o n a l j e t s ,} \tag {2.1}
$$

which is exploited in the measurements of  $t$ -channel single-top production at the LHC. As already mentioned in the introduction, on the one hand, we calculate all the fixed-order NLO corrections of QCD and EW origin for the signature (2.1), i.e., the complete-NLO prediction. On the other hand, we match a subset of the complete-NLO predictions to QCD shower effects. The calculation framework for the former approximation is discussed in section 2.1, while for the latter in section 2.2.

In our calculation, with both approximations, we always apply cuts (they are explicitly defined in section 3.1) in order to select the fiducial region that has been considered by the ATLAS collaboration in the measurement of  $t$ -channel single-top production [27]. Other production processes contribute to the signature (2.1) as well and the fiducial region is defined in order to suppress them.

It is important to note that, within our setup, the calculation for a signature similar to (2.1) where a  $\mu^{+}$  is present in the place of the  $e^{+}$  is exactly the same. Thus, the numbers given in this paper can be used also for that signature. On the other hand, in this work we do not consider the case where a  $e^{-}$  (or  $\mu^{-}$ ) is present in the place of the  $e^{+}$ , i.e., the case of  $t$ -channel single-top antiquark production; we expect results to be qualitatively similar.

# 2.1 Fixed-order complete-NLO predictions

In this section we describe the calculation at fixed-order complete-NLO accuracy for the signature (2.1). First, in section 2.1.1 we discuss the different resonances appearing in the different perturbative orders that enter the complete-NLO approximation and we introduce the notation used in this work. Then, in section 2.1.2 we specify the input parameters and finally in section 2.1.3 we describe the clustering procedure that we have adopted in order to ensure infra-red (IR) safety. Numerical results are presented in section 3.2.

The calculation that is described in this section, fixed-order complete-NLO predictions for the signature (2.1), has been performed via the latest version of MAD-

GRAPH5_AMC@NLO [42], which is public. In the MADGRAPH5_AMC@NLO framework [57] infrared singularities are dealt with via the FKS method [58, 59], which is automated in the module MADFKS [52, 60]. The evaluation of one-loop amplitudes is performed by dynamically switching among different types of techniques for integral reduction, i.e., the so called OPP method [61], Laurent-series expansion [62], and tensor integral reduction [63-65]. These techniques have been automated in the module MADLOOP [66], which is employed for generating the amplitudes. We recall that MADLOOP employs the codes CUTTOOLS [67], NINJA [68, 69] and COLLIER [70]. Moreover, it includes an in-house implementation of the OPENLOOPS optimisation [71].

# 2.1.1 Structure of the calculation: underlying resonances and notation

The main process we are interested in is single-top production via  $t$ -channel with the top-quark decaying leptonically. In other words,  $pp \rightarrow tj$ , where  $j$  is a light jet and the top-quark is decaying into  $t \rightarrow e^+ \nu_e b$ . In the 5FS, this process contributes at LO, which is of  $\mathcal{O}(\alpha^4)$ , to the cross section for the signature (2.1). Due to the misidentification of  $b$ -jets as light jets, also  $s$ -channel single-top production contributes at the same order when the top quark decays leptonically. Similarly,  $WZ$  production can contribute when the  $Z$  boson decays into a  $b\bar{b}$  pair. The  $\mathcal{O}(\alpha^4)$  contributions, however, are the formally smallest LO contributions in the expansion in powers of  $\alpha_s$  and  $\alpha$ . Indeed, the signature (2.1) receives also  $\mathcal{O}(\alpha_s^2\alpha^2)$  contributions from tree-level diagrams:  $W+jets$  with leptonic  $W$  decays contributes to the  $\mathcal{O}(\alpha_s^2\alpha^2)$ . Thus, as already mentioned, single-top production is not the only production process contributing to this signature. Furthermore also non-resonant contributions are possible.

In this section we present the calculation of all the contributions to fixed-order complete-NLO predictions for the signature (2.1). Following the notation already used in refs. [42, 72-78], with complete-NLO predictions we denote all the one-loop and real emission corrections of QCD and EW origin. To this purpose we calculate all the  $\mathcal{O}(\alpha_s^m\alpha^{n + 2})$  contributions with  $m,n > 0$  and  $m + n = 2,3$  to

$$
p p \rightarrow \nu_ {e} J J J, \tag {2.2}
$$

where  $J$  is any particle that may potentially enter in a fully-democratic jet, i.e., a jet that is obtained by clustering quarks (including  $b$ -quarks), gluons, photons and leptons. As discussed in refs. [42, 75], this procedure is necessary in order to fully ensure IR safety when dealing with complete-NLO contributions and massless final state. In practice, given the presence of an electronic neutrino, $^{1}$  all the possible final states include a positron and two (three) massless particles.

The different contributions to the total cross section can be denoted as:

$$
\begin{array}{l} \Sigma_ {\mathrm {L O}} ^ {\nu_ {e} J J J} \left(\alpha_ {s}, \alpha\right) = \alpha_ {s} ^ {2} \alpha^ {2} \Sigma_ {4, 0} ^ {\nu_ {e} J J J} + \alpha_ {s} \alpha^ {3} \Sigma_ {4, 1} ^ {\nu_ {e} J J J} + \alpha^ {4} \Sigma_ {4, 2} ^ {\nu_ {e} J J J} \\ \equiv \mathrm {L O} _ {1} + \mathrm {L O} _ {2} + \mathrm {L O} _ {3}, \tag {2.3} \\ \end{array}
$$

$$
\begin{array}{l} \Sigma_ {\mathrm {N L O}} ^ {\nu_ {e} J J J} \left(\alpha_ {s}, \alpha\right) = \alpha_ {s} ^ {3} \alpha^ {2} \Sigma_ {5, 0} ^ {\nu_ {e} J J J} + \alpha_ {s} ^ {2} \alpha^ {3} \Sigma_ {5, 1} ^ {\nu_ {e} J J J} + \alpha_ {s} \alpha^ {4} \Sigma_ {5, 2} ^ {\nu_ {e} J J J} + \alpha^ {5} \Sigma_ {5, 3} ^ {\nu_ {e} J J J} \\ \equiv \mathrm {N L O} _ {1} + \mathrm {N L O} _ {2} + \mathrm {N L O} _ {3} + \mathrm {N L O} _ {4}. \tag {2.4} \\ \end{array}
$$

![](images/e386cf3c15972ae24ef661d66ea46d67568a7ae70f1a819d81fceddde12d2061.jpg)

![](images/084c4ccbcb78ba343fb949260cf698e370c0ac15554249127dbb30ccda678fa1.jpg)

![](images/d78fce5d8f024eb9f36923fb6a8994a2eb538643d6897a9b8480ab53c39ad2b2.jpg)

![](images/2deb918ba9413e1c5d63f9491aa74eab68e792dbb5a4461c8fa1a3ed24ed0249.jpg)  
Figure 1. Selection of Feynman diagrams contributing to the signature (2.1). The upper-left diagram contributes to  $\mathrm{NLO}_1$  and  $\mathrm{NLO}_2$  ( $W+$  jets), the upper-central diagram to  $\mathrm{NLO}_4$  (single-top resonant), and the upper-right diagram also to  $\mathrm{NLO}_4$  (non-resonant). The lower-left diagram is a typical  $s$ -channel single-top production diagram, with an extra gluon, while the lower-right diagram can be considered  $\bar{t} W^{+}$ -associated production, both contributing to  $\mathrm{NLO}_3$ .

![](images/3a89d73cac4804f115b7635ee75023d2fc34c48b8488ca825b2dabad0b563654.jpg)

Single-top production via  $s$ - and  $t$ -channel enters at  $\mathrm{LO}_3$  and the corresponding NLO QCD and EW corrections are part of the  $\mathrm{NLO}_3$  (e.g. bottom-left diagram in figure 1) and  $\mathrm{NLO}_4$  (e.g. top-central diagram in figure 1), respectively. The same applies to  $WZ$  production.  $W+$  jets contributes at LO to the  $\mathrm{LO}_1$  and the corresponding NLO QCD and EW corrections are part of the  $\mathrm{NLO}_1$  and  $\mathrm{NLO}_2$  (e.g. top-left diagram in figure 1), respectively. Moreover, including NLO corrections, also  $tW$ -associated production can contribute to the signature (2.1). Indeed, due to the top-quark decay, two  $W$  bosons are present: if one of them decays hadronically and the other one leptonically, LO contributions from  $tW$ ,  $\bar{t}W$  (e.g. bottom-right diagram in figure 1) and  $WW + b_{\mathrm{jet}}$  production enter the  $\mathrm{NLO}_3$  and  $\mathrm{NLO}_4$ . This pattern is summarised in table 1. We remark that besides these production processes, all the off-shell and non-resonant effects (e.g. top-right diagram in figure 1) are exactly taken into account.

In the following, in order to simplify the notation, we will also refer to the perturbative orders  $\mathrm{LO}_3$ ,  $\mathrm{NLO}_3$  and  $\mathrm{NLO}_4$  as "Single-Top", while the remaining perturbative orders  $\mathrm{LO}_1$ ,  $\mathrm{LO}_2$ ,  $\mathrm{NLO}_1$  and  $\mathrm{NLO}_2$  will be also referred as  $W+$  jets. In particular,

$$
\mathrm {L O} = \mathrm {L O} _ {3},
$$

$$
\text {S i n g l e - T o p} \longrightarrow \quad \mathrm {N L O Q C D} = \mathrm {L O} _ {3} + \mathrm {N L O} _ {3},
$$

$$
\mathrm {N L O Q C D} + \mathrm {E W} = \mathrm {L O} _ {3} + \mathrm {N L O} _ {3} + \mathrm {N L O} _ {4}, \tag {2.5}
$$

$$
\mathrm {L O} = \mathrm {L O} _ {1} (+ \mathrm {L O} _ {2}),
$$

$$
W + \text {j e t s} \longrightarrow \quad \mathrm {N L O Q C D} = \mathrm {L O} _ {1} + \mathrm {N L O} _ {1},
$$

$$
\mathrm {N L O Q C D} + \mathrm {E W} = \mathrm {L O} _ {1} + \mathrm {N L O} _ {1} + \mathrm {N L O} _ {2},
$$

where  $\mathrm{LO}_2$  has been put in parentheses since it is numerically zero when the signature (2.1) is considered.

Table 1. Intermediate resonances contributing to the various perturbative orders that enter the calculation.  

<table><tr><td>Perturbative order</td><td>Resonant processes</td></tr><tr><td>LO1 (αs2α2)</td><td>W + 2 jets</td></tr><tr><td>LO2 (αsα3)</td><td>-</td></tr><tr><td>LO3 (α4)</td><td>single-top (t- and s-ch.), WZ</td></tr><tr><td>NLO1 (αs3α2)</td><td>W + 2 jets</td></tr><tr><td>NLO2 (α2α3)</td><td>W + 2 jets</td></tr><tr><td>NLO3 (αsα4)</td><td>single-top (t- and s-ch.), WZ, tW, tW and WW + b-jet</td></tr><tr><td>NLO4 (α5)</td><td>single-top (t- and s-ch.), WZ, tW, tW and WW + b-jet</td></tr></table>

It is worth to note that going beyond NLO for  $pp \rightarrow \nu_{e}JJJ$  production, in particular at  $\mathcal{O}(\alpha_s^3\alpha^3)$ , top-quark pair production with semi-leptonic decays is present and also contributes to the signature (2.1). Moreover, it represents the largest contribution to the background in the searches for  $t$ -channel single-top production, see e.g. ref. [27]. This contribution appears only beyond the formal accuracy of our calculation and therefore it is not entering our results. However, it has to be taken into account for a correct estimate of the background.

# 2.1.2 Input parameters

In order to perform the calculation, given the presence of intermediate resonances, we use the complex-mass scheme. We use as input parameters for the EW sector  $G_{\mu}$ ,  $m_Z$  and  $m_W$  and we accordingly perform the renormalisation in the  $G_{\mu}$ -scheme. The results of section 3.2 are obtained with the following masses and widths for the input parameters of the complex mass scheme<sup>2</sup>

$$
m _ {Z} = 9 1. 1 8 7 6 \mathrm {G e V}, m _ {W} = 8 0. 3 8 5 \mathrm {G e V}, m _ {H} = 1 2 5 \mathrm {G e V}, m _ {\mathrm {t}} = 1 7 3. 3 4 \mathrm {G e V}, (2. 6)
$$

$$
\Gamma_ {Z} = 2. 4 9 5 5 \mathrm {G e V}, \quad \Gamma_ {W} = 2. 0 8 9 7 \mathrm {G e V}, \quad \Gamma_ {H} = 4. 0 7 \mathrm {M e V}, \quad \Gamma_ {\mathrm {t}} = 1. 3 6 9 1 8 \mathrm {G e V}. \tag {2.7}
$$

In our calculation, the width of the Higgs boson is necessary only for regulating the integrable singularity of the  $s$ -channel Higgs boson that can be present in one-loop diagrams.

The value of  $G_{\mu}$  is set equal to

$$
G _ {\mu} = 1. 1 6 6 3 9 \times 1 0 ^ {- 5} \mathrm {G e V} ^ {- 2}, \tag {2.8}
$$

and the CKM matrix is set equal to the  $3 \times 3$  identity matrix. We renormalise QCD interactions in the  $\overline{\mathrm{MS}}$  scheme and, as already mentioned, we use the 5FS. $^3$  We set the

renormalisation and factorisation scales to  $\mu_{R} = \mu_{F} = H_{T} / 2$ , where  $H_{T}$  is the scalar sum of the transverse momenta of all the final-state particles, which are all massless. As PDF set we use LUXQED17_plusPdf4LHC15_NNLO_100 [80, 81], which includes a photon member and  $\alpha_{s}(m_{Z}) = 0.118$ . Scale uncertainties are evaluated via the standard 9-point independent variations of the factorisation and renormalisation scales.

# 2.1.3 Clustering procedure

Since we perform a fixed-order NLO computation, at most two particles can be clustered together to generate signature (2.1). Therefore, in order to ensure IR safety we perform the following procedure. First of all we perform a QED clustering among leptons and photons, where  $\Delta R = \sqrt{(\Delta\eta)^2 + (\Delta\phi)^2}$  is the distance among two particles and the clustering parameter is set to  $\Delta R^{\mathrm{QED}} = 0.1$ . In practice, we apply the anti- $k_{T}$  clustering algorithm with  $p_{T,\min}^{\mathrm{QED}} = 0$  GeV. If only a single particle is present within a radius  $\Delta R = \Delta R^{\mathrm{QED}}$ , we do not cluster this particle with any other. Otherwise, in order to be IR safe, if the distance between two particles is  $\Delta R < \Delta R^{\mathrm{QED}}$  we follow this procedure:

- If they are two photons, they are not clustered.  
- If they are one photon and one lepton with flavour  $f$ , they are clustered and defined as a lepton with flavour  $f$ .  
- If they are an opposite-sign same-flavour (OSSF) lepton pair, they are clustered and defined as a photon.  
- If they are two leptons which are not OSSF, they are not clustered.

After this clustering procedure we can already reject events with three or more QED particles (leptons or photons). Indeed, leptons will not enter the QCD clustering and in order to obtain the signature (2.1) we need at least a  $\nu_{e}$ , a  $b$  or  $\bar{b}$  and a positron. Therefore, four QED particles among four/five particles in the final state are not possible. Three would be in principle possible in the case of a positron and two photons, which in turn would lead to a light jet via the QCD clustering procedure discussed in the next paragraph. However, the process  $pp\rightarrow e^{+}\nu_{e}b\gamma \gamma$  is not possible due to flavour.

Then, we proceed with the standard QCD clustering for quarks, gluons and photons in order to define QCD jets. Since we will perform the calculation for the fiducial region defined in ref. [27], which is also explicitly reported in section 3.1, we use the anti- $k_{T}$  clustering algorithm with parameters  $\Delta R^{\mathrm{QCD}} = 0.4$  and  $p_{T,\min}^{\mathrm{QCD}} = 30\mathrm{GeV}$ . Only jets that contain a  $b$  quark or antiquark and have pseudorapidity  $|\eta (j)| < 2.5$  are identified as  $b$ -jet with a  $100\%$  tagging efficiency. Note that in the case of  $|\eta (j)| > 2.5$  or if a  $b\bar{b}$  pair is present, the jet is considered as a light jet. The latter condition is needed to ensure IR safety in the 5FS.

# 2.2 Shower effects matched to NLO QCD

In this section we describe the calculation of the contributions for Single-Top and  $W+$  jets productions to the signature (2.1), at NLO QCD accuracy and including QCD shower effects. Numerical results are presented later in section 3.3.

First of all, it is important to note that at the moment the theoretical knowledge for a consistent matching of NLO QCD and EW effects to (QCD) shower effects is not yet available for processes involving QCD interactions at LO. The first attempts in this direction have been performed in refs. [84, 86, 87]. However, the approach pursued in these works applies only to the cases where EW effects are dominated by purely weak effects, in particular electroweak Sudakov logarithms. As we will explain in section 3.2, this is not the case for the calculation performed in this work, both at the inclusive and differential level. In particular, in our calculation QED effects cannot be neglected due to the effective jet veto from the definition of the signature (2.1). Moreover, as we will see in section 3.3, QCD shower effects are large and so an analogous feature is expected, although at a smaller extent, also for EW corrections, which for these observables are mainly of QED origin.

In this work therefore we consider only NLO QCD corrections to separately Single-Top and  $W+$  jets production and we match them to QCD parton-shower effects. On the other hand, it is important to note that while such a calculation can be straightforwardly performed for the case of  $W+$  jets via public tools, in the case of Single-Top the situation is much more complex. Indeed, NLO QCD corrections to Single-Top correspond to the  $\mathrm{NLO}_3$  contribution. The  $\mathrm{NLO}_3$  involves both "genuine" QCD corrections on top of  $\mathrm{LO}_3$ , the LO in Single-Top, but also "genuine" EW corrections on top of  $\mathrm{LO}_2$ . Indeed the  $\mathrm{LO}_2$  for the full process (2.2) is not vanishing, and therefore the IR structure of the  $\mathrm{NLO}_3$  does involve QED singularities on top of the  $\mathrm{LO}_2$ .

On the other hand, as also shown later in section 3.2, the  $\mathrm{LO}_2$  contribution is exactly zero when the signature (2.1) is considered. Therefore, QED soft and collinear singularities are not involved in the  $\mathrm{NLO}_3$  calculation for the signature (2.1); soft and collinear enhanced contributions in the  $\mathrm{NLO}_3$  are only of QCD origin. For this reason, NLO QCD corrections can be matched to the QCD parton shower following the standard approaches [88, 89]. On the other hand, since as we said  $\mathrm{NLO}_3$  in (2.2) involves QED singularities on top of the  $\mathrm{LO}_2$ , for the shower simulation we actually consider the process

$$
p p \rightarrow \nu_ {e} b J J + p p \rightarrow \nu_ {e} \bar {b} J J, \tag {2.9}
$$

forcing one of the parton in the final state to be a bottom quark or antiquark. In this way, partonic channels that would be divergent due to QED interactions but that do not contribute to the signature (2.1) are discarded from the beginning. We remind the reader that, in order to preserve IR safety, this approach cannot be pursued for the entire complete-NLO calculation described in section 2.1.1 and results in section 3.2, and in general for other processes [42].

Results based on this approximation are presented in section 3.3 and are based on the same input parameters, scale definitions and PDFs listed in section 2.1.2. Only two differences are present. First, photon-induced contributions have been ignored, but their contribution is negligible. Second, when a  $b\bar{b}$  pair is clustered within a jet, this jet is tagged as a  $b$ -jet, at variance with the fixed-order calculation where it is instead tagged as a light jet.

It is important to note that at LO (where the IR-safety problem cannot be present) in Single-Top numerical differences between the syntaxes (2.2) and (2.9) are completely negligible; also when showering the events. Indeed, at  $\mathrm{LO}_3J$  cannot be a gluon that the shower will subsequently split into a  $b\bar{b}$  pair. Moreover, we have explicitly verified that also tagging a clustered  $b\bar{b}$  pair as a light jet the NLO QCD predictions including shower effects are in general not affected above the percent level. Among all the plots presented in section 3.3, only for the  $m(e^{+}j_{b})$  distribution above  $150\mathrm{GeV}$  differences of order  $5\%$  are observed.

In the case of  $W +$  jets production, tagging a clustered  $b\bar{b}$  pair as a light jet has instead a non-negligible impact. We have verified that this reduces the NLO QCD predictions including shower effects by  $\sim 10\%$  at the inclusive level. Nevertheless, in experimental analyses this procedure is typically not employed and a  $b$ -jet can contain more than a  $b$ -hadron.

# 3 Results

# 3.1 Fiducial region

In order to isolate the contribution to the signature (2.1) and select the fiducial region for  $t$ -channel single-top production we perform the following procedure at the analysis level, adopting the cuts from ref. [27].

As already mentioned in section 2.1.3 jets are clustered via the anti- $k_{T}$  algorithm with parameters  $\Delta R^{\mathrm{QCD}} = 0.4$  and  $p_{T,\mathrm{min}}^{\mathrm{QCD}} = 30\mathrm{GeV}$ . Also, only jets that contain a  $b$  quark or antiquark and have pseudorapidity  $|\eta (j)| < 2.5$  are identified as  $b$ -jets; in the case of  $|\eta (j)| > 2.5$  a jet is always considered as a light jet. We also remind the reader that in the case of the fixed-order results, if a  $b\bar{b}$  pair is clustered, the corresponding jet is always considered as a light jet for IR safety. When we perform the calculation including shower effects this requirement is not necessary and therefore we consider such a jet a  $b$ -jet, still only if  $|\eta (j)| < 2.5$ . As already mentioned, we explicitly verified that this choice, being preferable because it is much closer to a realistic experimental procedure, has a negligible impact on the Single-Top results presented in this work.

After having defined jets (and dressed leptons), we define the fiducial region according to (2.1), i.e., by requiring exactly one light jet  $(j_{l})$ , one  $b$ -jet  $(j_{b})$ , a positron and missing transverse-energy. In particularly, following ref. [27], these cuts are applied:

- exactly one lepton:  $|\eta(\ell)| < 2.5$  and  $p_T(\ell) > 25\mathrm{GeV}$  and identified as a positron,  
- exactly one light jet:  $|\eta(j_l)| < 4.5$  and  $p_T(j_l) > 30\mathrm{GeV}$ ,  
- exactly one  $b$ -jet:  $|\eta(j_b)| < 2.5$  and  $p_T(j_b) > 30 \, \mathrm{GeV}$ ,  
- missing transverse-energy:  $\mathcal{E}_T > 30\mathrm{GeV}$

- positron and jets separation:  $\Delta R(e^{+},\ell) > 0.4$  
- positron and  $b$ -jet system:  $m(e^{+}j_{b}) < 160\mathrm{GeV}$

where  $\mathcal{E}_T\equiv p_T(\nu_e)$

The requirement of exactly two jets of which one being a light jet and one being a  $b$ -jet is suppressing the relative contribution of all the resonant processes besides the  $t$ -channel single top. Indeed,  $s$ -channel single top typically leads to two  $b$ -jets and  $tW$  associate production to three jets. Also,  $WZ$  and  $W +$  jets production mostly lead to 2  $b$ -jets or 2 light jets.

# 3.2 Fixed order

In this section we present and discuss fixed-order results at complete-NLO accuracy for the total cross section and the differential distributions at 13 TeV; we consider the signature (2.1) in the fiducial region defined in section 3.1. As summarised in (2.5), we will refer to the perturbative orders  $\mathrm{LO}_3$ ,  $\mathrm{NLO}_3$  and  $\mathrm{NLO}_4$  as "Single-Top", while the remaining perturbative orders  $\mathrm{LO}_1$ ,  $\mathrm{LO}_2$ ,  $\mathrm{NLO}_1$  and  $\mathrm{NLO}_2$  will be referred as "W+jets".

One should bear in mind that although the fiducial region has been designed for enhancing the relative contribution of  $t$ -channel single-top,  $s$ -channel single-top and  $tW$  contributions are still present and are not negligible. Numerical results on the relative impact of these other production channels and their dependence on the cuts are presented in appendix A. Furthermore, considering directly the signature (2.1), the different processes cannot be separated in a gauge-invariant way at NLO and also non-resonant contributions are present, which also cannot be excluded for the same motivation. For this reason we have not subtracted the  $s$ -channel single-top and  $tW$  contributions from the Single-Top predictions (cf., the lower two diagrams in figure 1).

We remind the reader that NLO (and also NNLO) QCD corrections to  $t$ -channel single-top with leptonic top decays have already been calculated in a similar fiducial region in refs. [38, 39]. However, this calculation is based on the narrow-width approximation for the top decay, therefore non-resonant effects, and  $s$ -channel and  $tW$  contributions are not taken into account. In appendix A we perform a detailed comparison with the results in refs. [38, 39], showing how these effects can have an impact and motivating the features that are found in the results presented in this section, especially at the differential level.

# 3.2.1 Total cross section

In table 2 we present predictions for the signature (2.1) in the fiducial region defined in section 3.1. For different accuracies, we provide the results for the central value of the factorisation and renormalisation scale together with the associated scale uncertainties. $^{6}$  We also show the relative size of QCD and EW corrections for the central values of the scales. As can be seen, for Single-Top, the NLO QCD cross section  $(\mathrm{LO}_3 + \mathrm{NLO}_3)$  is much smaller than the corresponding LO  $(\mathrm{LO}_3)$  prediction; the QCD  $K$ -factor is  $\sim 0.6$ . This

<table><tr><td>Single-Top</td><td>cross section</td></tr><tr><td>LO</td><td>4.623(1) +0.415(+9.0%) -0.533(-11.5%) pb</td></tr><tr><td>NLO QCD</td><td>2.762(6) +0.226(+8.2%) -0.240(-8.7%) pb</td></tr><tr><td>NLO QCD+EW</td><td>2.676(6) +0.229(+8.6%) -0.236(-8.8%) pb</td></tr><tr><td>(NLO QCD)/LO</td><td>0.60(1)</td></tr><tr><td>(NLO QCD+EW)/(NLO QCD)</td><td>0.97(1)</td></tr></table>

Table 2. Various fixed-order cross sections (in pb), including their scale uncertainty, for the signature (2.1) within the fiducial region defined in section 3.1 for the Single-Top process (top table) and the  $W+$  jets process (bottom table). The ratios (last two lines of both tables) are computed for the central values of the corresponding predictions.  

<table><tr><td>W+jets</td><td>cross section</td></tr><tr><td>LO</td><td>0.7656(6)^{+0.3002(+39.2%)}_{-0.2265(-29.6%)} pb</td></tr><tr><td>NLO QCD</td><td>1.612(3)^{+0.323(+20.1%)}_{-0.309(-19.2%)} pb</td></tr><tr><td>NLO QCD+EW</td><td>1.597(3)^{+0.318(+19.9%)}_{-0.305(-19.1%)} pb</td></tr><tr><td>(NLO QCD)/LO</td><td>2.11(1)</td></tr><tr><td>(NLO QCD+EW)/(NLO QCD)</td><td>0.99(1)</td></tr></table>

reduction is due to the requirement of exactly two jets; vetoing extra jets the QCD radiation is suppressed, yielding a negative correction. For the same reason, scale uncertainties do not strongly decrease moving from LO to NLO QCD accuracy and they are  $\sim 8\%$  for the latter. However, in section 3.3 we will see that taking into account shower effects, and therefore the multiple emissions of partons, NLO QCD corrections do significantly decrease scale uncertainties (cf. table 3). Also, we will show that, unlike the fixed-order case, including shower effects LO and NLO QCD scale-uncertainty estimates are compatible. Moreover, we will compare NLO QCD predictions with or without shower effects and we will show they are compatible, at the inclusive level. Thus, although scale uncertainties are larger at fixed order, NLO corrections are still sensible and reliable, with the exception of specific phase-space regions that we will specify in section 3.3.

The impact of NLO EW corrections  $(\mathrm{NLO}_4)$  on the NLO QCD prediction is sizeable; it reduces the cross section by  $-3\%$ . Even though this is within the scale uncertainties, the latter are significantly reduced by shower effects. Therefore, for a correct comparison between theory predictions and experimental measurements EW effects have to be taken into account.

In table 2, we also show results for  $W +$  jets, i.e., the contributions from the remaining perturbative orders  $\mathrm{LO}_1$ ,  $\mathrm{LO}_2$ ,  $\mathrm{NLO}_1$  and  $\mathrm{NLO}_2$ . The NLO QCD cross section  $(\mathrm{LO}_1 + \mathrm{NLO}_1)$  is much larger than the corresponding LO  $(\mathrm{LO}_1)$  prediction; the QCD  $K$ -factor is  $\sim 2.1$ . Unlike the case of Single-Top, the requirement of exactly two jets does not

lead to negative corrections. This pattern is unusual for a NLO QCD calculation with a requirement of an exclusive number of jets, i.e., applying a jet-veto. However, in this process real QCD radiation can convert LO events that would not contribute to the signature (2.1) in events that do contribute. For example,  $e^{+}\nu_{e}gg$  final states, which are present at LO, do not contribute to the signature (2.1). On the other hand, real QCD radiation can convert them via the  $g\rightarrow b\bar{b}$  splitting into a  $e^{+}\nu_{e}gb\bar{b}$  final state, which can contribute to the signature (2.1). Moreover, the LO  $e^{+}\nu_{e}gg$  final state has a much larger cross section than the  $e^{+}\nu_{e}bq$  one, which does contribute to the signature (2.1) at LO. Hence, the NLO QCD contributions increase the central value of the LO cross section by more than a factor 2.

At variance with Single-Top predictions, scale uncertainties decrease moving from LO  $(\sim +40\%)$  to NLO QCD  $(\sim +20\%)$  accuracy. However, despite this reduction, they are larger than in the case of Single-Top, due to the higher powers of  $\alpha_{s}$  factorising the LO prediction. On the other hand, similarly to the case of Single-Top, LO and NLO QCD predictions do not overlap. We will show in section 3.3 that including shower effects NLO QCD scale uncertainties are strongly reduced and are compatible with the fixed-order case.

The impact of NLO EW corrections  $(\mathrm{NLO}_2)$  on the NLO QCD prediction is instead negligible at the inclusive level; it reduces the cross section by  $-1.0\%$ , i.e., NLO EW corrections are much smaller than scale uncertainties. The  $\mathrm{LO}_2$  is instead exactly equal to zero. Indeed, although the process (2.2), i.e., with fully democratic jets, involves non-vanishing contributions to the  $\mathrm{LO}_2$ , by requiring a  $b$ -jet in the analysis they all vanish.

# 3.2.2 Differential distributions

We move now to differential distributions. Similarly to the inclusive case, we separate results for Single-Top and  $W+$  jets predictions, but one should bear in mind that both refer to the same final state. We provide at the end also a direct comparison at differential level for Single-Top and  $W+$  jets predictions.

In figures 2 and 3 we show predictions for several quantities, taking into account the cuts of section 3.1 that define the fiducial region. All plots display results for Single-Top contributions at LO, NLO QCD and NLO  $\mathrm{QCD + EW}$  accuracy. In the first inset we show both LO (black) and NLO QCD (red) predictions including scale uncertainties normalised to the central value of the LO; the latter is the QCD  $K$ -factor. In the second inset we show again the NLO QCD scale uncertainties, but now normalised to the central NLO value, and also the (NLO  $\mathrm{QCD + EW}$ )/(NLO QCD) ratio. In figure 2 we display the predictions for the transverse momentum of the light jet  $(j_{l})$ , the  $b$ -jet  $(j_{b})$  and the reconstructed momentum of the top-quark  $p_{T}(t^{\mathrm{rec}})$ . We show also the pseudorapidity for the light jet and the  $b$ -jet, and the rapidity for the reconstructed top. In figure 3 we instead show the predictions for the quantities  $m(t)$ ,  $m(t^{\mathrm{rec}})$ ,  $m(e^{+}j_{b})$ ,  $\cos(\theta_{e^{+}j_{l}}^{t})$  and  $\cos(\theta_{j_{b}j_{l}}^{t})$ , which we define in the following. The quantity  $m(t)$  is the invariant mass of the positron, the  $b$ -jet and the momentum of the neutrino and therefore, although it cannot be directly measured, corresponds to the true momentum of the would-be top-quark. On the contrary,  $m(t^{\mathrm{rec}})$  is the same quantity, but with the momentum of the neutrino extracted from the value of  $\mathcal{E}_{T}$  assuming the  $W$  boson being on-shell. In practice, one has to solve the quadratic equation  $m_W^2 = 2p_{e^+} \cdot p_{\nu_e}$

for  $p_{\nu_e}^z$  assuming  $\mathcal{E}_T = p_T(\nu_e)$ . The same procedure is used also for the determination of  $p_T(t^{\mathrm{rec}})$ . The quantity  $m(e^{+}j_{b})$  is the invariant mass of the positron and  $b$ -jet, which is exploited for the measurement of  $m_t$ . Indeed, at LO and assuming the top-quark and the  $W$  boson on-shell,  $m(e^{+}j_{b})$  has an end-point for  $m(e^{+}j_{b}) = \sqrt{m_{t}^{2} - m_{W}^{2}} \sim 154\mathrm{GeV}$ . For this reason in figure 3 we show this distribution both in a wide range (central-left plot) and close to the aforementioned end-point (central-right plot). The quantities  $\cos (\theta_{e^{+}j_{l}}^{t})$  and  $\cos (\theta_{jb j_l}^t)$  are the cosine of the angle between the positron and the light jet and of the angle between the  $b$ -jet and light jet in the top-quark rest-frame, respectively [91]. Via these angular distributions it is possible to gain information on the top-quark polarisation along the direction of the spectator light jet  $(j_{l})$  that is present in the  $t$ -channel production. The positron angular distribution  $\cos (\theta_{e^{+}j_{l}}^{t})$  carries the higher spin-analysing power (degree of correlation) with the top-quark spin. Thanks to the dependence on the top-quark spin and polarisation these distributions are sensitive to new physics [10-13, 16].

Consistently with the result at the inclusive level, differential QCD  $K$ -factors of plots in figure 2 are in general substantially smaller than one. Especially, the  $p_T(j_l)$  and  $p_T(j_b)$  distributions exhibit very large and negative corrections in the tail; they are  $\sim -70\%$  at  $200\mathrm{GeV}$  and well outside the LO scale uncertainty. This feature is induced by the requirement of exactly two jets, and clearly shows the necessity of resumming large QCD Sudakov logarithms in this phase-space region. As we will see in section 3.3 this effect is counterbalanced by QCD shower effects (cf. upper-left plot in figure 9). The QCD  $K$ -factor is instead very different for  $\eta(j_l)$  and  $\eta(j_b)$ ; it is very flat for  $\eta(j_b)$  while  $\eta(j_l)$  shows a bump centred around  $\eta(j_l) = 0$ . As discussed in appendix A, this effect is due to the large contribution from  $tW^{-}$ production entering via NLO QCD corrections. Moreover,  $\bar{t}W^{+}$ is also contributing, increasing even more this effect. Indeed, in  $\bar{t}W^{+}$ production the  $W^{+}$ boson can decay into  $e^{+}\nu_{e}$ , while the top can decay hadronically, contributing in total to the signature (2.1) (see e.g. bottom-right diagram of figure 1). Considering EW corrections, for both  $\eta$  and  $p_T$  distributions of the light and  $b$ -jets, the shape of the (NLO QCD+EW)/(NLO QCD) ratio is very similar to the one of the corresponding QCD  $K$ -factor. In particular, for  $p_T(j_l)(p_T(j_b)) \sim 200\mathrm{GeV}$ , EW corrections further reduce the NLO QCD predictions by  $\sim 20(30)\%$ . Also, EW corrections similarly to QCD corrections do not lead to large effects for central light jets. The  $p_T$  and  $\eta$  distributions for the reconstructed top-quark have features very similar to the case of the  $b$ -jet, besides the region  $p_T(t^{\mathrm{rec}}) \leq 80\mathrm{GeV}$ . In all the aforementioned cases the NLO EW corrections are within the NLO QCD scale uncertainties. On the other hand, as already mentioned, shower effects significantly decrease scale uncertainties as discussed in section 3.3.2 (cf. figure 9).

We move now to the discussion of plots in figure 3. The  $m(t)$  distribution receives enormous corrections from QCD manifesting also as very large scale uncertainties that nevertheless do not overlap with the LO ones. This effect is induced by real radiation from the bottom quark which is not clustered into the  $b$ -jet and therefore leads to the migration of events from the LO peak  $m(t) \simeq m_t$  to smaller values. Moreover, this effect is

![](images/02331bc765ccc82910e8f8fc9ad515e88af4750c2e2d34b81c4bc093378d83a9.jpg)

![](images/b9cb9801989fb67f7e4236ce82e912de8c791730602140c70852cb4e7d4a3e89.jpg)

![](images/bc029c33fd4ddecfb501dc3ba8af8e53fa404f14b2d9f6249102931514b5e9c4.jpg)

![](images/fa862eb2429ab0bdcd28a764ca22e512b5a354c3e932c70c2d60d4f5c39b8755.jpg)

![](images/83ef8125de33e8112a53d2f9f3244ac05831b1ccd184a7e6db859ad8477f82ac.jpg)  
Figure 2. LO, NLO QCD and NLO QCD+EW predictions for the transverse momentum (left) and rapidity (right) distributions of the light jet (top),  $b$ -jet (central) and reconstructed-top (bottom) for the Single-Top process.

![](images/e500ebe4170747aeb550303ba89a3505f979d5bdd362b49bd8bcaeabc5a73209.jpg)

![](images/7583e4f6b413fae998c10a5e8677831c89bf7e6c7fbf8813917b46a0e3aa6d6a.jpg)

![](images/eb83b9bfb17b9f6f8b37e53273267ef20555950d32d4da3e359c8904ce21d7a1.jpg)

![](images/c617107b9e0c8135481c0e456bc13fc15daf830f9fc26bdc2ea63f7c7e68f6c3.jpg)

![](images/1f1f7534adda4818ba9da5cffddf0634e069cb61c5e50484dca7abd8857d1e45.jpg)

![](images/dfbe506f0149786b252ebd51e210eed4a3a453b02341f57dbedaa03c1b9458a6.jpg)  
Figure 3. LO, NLO QCD and NLO QCD+EW predictions for the top-quark invariant mass (top) at the truth level (left) and reconstructed (right), positron and  $b$ -jet system invariant mass distribution (central) in a large (left) and small range (right), and spin-correlation observables (bottom) for the Single-Top process.

![](images/d9f203f1e411fda2db7755f7f91fd435fa21cc3a8d89437717087d43fecc671e.jpg)

further enhanced by the requirement of exactly one  $b$ -jet and one light jet. Indeed, at NLO QCD, often these two jets corresponds to the  $b$  quark and the unclustered gluon emitted by it, with instead the light-jet from  $t$ -channel production ( $tj_l$ ) being actually forward and undetected. Thus, the shape of the NLO QCD prediction and the QCD  $K$ -factor of  $m(t)$  strongly depend on the veto and the clustering radius  $\Delta R^{\mathrm{QCD}}$ . As a further check, we have investigated the effect of a jet veto on  $m(t)$  for  $pp \rightarrow W^{+}bW^{-}\bar{b}$  production at NLO QCD accuracy. While without jet veto we find results qualitatively in very good agreement with the case of  $m(t)$  for a top quark with leptonic decays discussed in ref. [92], a veto on additional QCD radiation strongly affects the distribution and moves the position of the peak as in figure 3. The very large  $K$ -factor at  $m(t) < m_t$  is induced by the migration of events from the peak to the off-shell region.

The situation is a bit different for the case of  $m(t^{\mathrm{rec}})$ . NLO QCD scale uncertainties are not as large as in the  $m(t)$  case and, especially, we do not see the very large  $K$ -factor at  $m(t^{\mathrm{rec}}) < m_t$ , which we observe at  $m(t) < m_t$ . Regardless of the value of  $m(t)$ , most of the events are associated to an on-shell  $W$ , but nonetheless for a small fraction of them the reconstructed value of the longitudinal component of the neutrino momentum is different to the true value. This fraction is anyway sufficiently large to lead to a much flatter LO distribution for  $m(t^{\mathrm{rec}})$  w.r.t.  $m(t)$ ; this effect is due to events with  $m(t) \simeq m_t$  and  $|m(t^{\mathrm{rec}}) - m_t| \gg \Gamma_t$ , which are a small fraction w.r.t. the generic events with  $m(t) \simeq m_t$ , but not w.r.t. those with  $m(t) \simeq m(t^{\mathrm{rec}})$ . When NLO QCD corrections are calculated, the migration effects from the peak of  $m(t^{\mathrm{rec}})$  is then much smaller, and therefore we do not observe large  $K$ -factors for  $m(t^{\mathrm{rec}}) < m_t$ . Although smaller in size, a similar effect is observed also for EW corrections, which for both  $m(t)$  and  $m(t^{\mathrm{rec}})$  are within the NLO QCD scale uncertainties.

The  $m(e^{+}j_{b})$  distribution (central-left plot) receives also very large negative QCD corrections due to the jet veto, besides the last bin where only events originating from a off-shell top-quark and/or  $W$  boson can contribute at LO. We zoom the last two bins in the central-right plot, where this effect can be seen even better in proximity to the value  $m(e^{+}j_{b}) = \sqrt{m_{t}^{2} - m_{W}^{2}}\sim 154\mathrm{GeV}$ . Electroweak corrections start being rather flat at  $\sim -2\%$  in the  $m(e^{+}j_{b}) < 100\mathrm{GeV}$  range. They increase in absolute value reaching a relative size of  $\sim -10\%$  for  $m(e^{+}j_{b})\sim 140\mathrm{GeV}$  and then quickly decrease up to the cut  $m(e^{+}j_{b}) = 160\mathrm{GeV}$ . Also for this observable parton-shower effects are expected to be non-negligible. Finally, we discuss the  $\cos (\theta_{e^{+}j_{l}}^{t})$  and  $\cos (\theta_{j_b j_l}^t)$  normalised distributions, for which scale uncertainties are calculated via the envelope of the 9-point variation correlated in the numerator and the denominator. For values  $\cos (\theta_{e^{+}j_l}^t) < -0.5$ , QCD corrections are positive and large (reaching a factor of  $\sim 5$ ) and they are further increased by EW corrections, which are instead negligible over the rest of the phase space. On the contrary, in the case of the  $\cos (\theta_{j_b j_l}^t)$  normalised distribution, EW corrections are negligible and QCD corrections are at most  $\sim 15\%$  in absolute value.

Summarising, the plots in figures 2 and 3 clearly show that EW effects are sizeable, although within the NLO QCD scale uncertainties, and that in very specific phase-space regions (the tails of the  $p_T(j_l)$  and  $p_T(j_b)$  distributions, the peak of the  $m(t)$  and  $m(t^{\mathrm{rec}})$

and the  $m(e^{+}j_{b})$  bin around the  $\sqrt{m_t^2 - m_W^2}\sim 154\mathrm{GeV}$  region) QCD effects are not under control at fixed order; NLO QCD and LO scale-uncertainty bands do not in general overlap. Precisely for this reason, in section 3.3 we analyse the impact of shower effects, which as anticipated reduce the impact of NLO QCD corrections and also the associated scale uncertainties.

In figure 4 we show predictions at LO, NLO QCD and NLO QCD+EW accuracy for  $W +$  jets. The layout of the plots is the same of those in figures 2 and 3 and we have shown only the distributions that have already been considered for the case of Single-Top and that show non-flat effects from either NLO QCD or NLO EW corrections, i.e.,  $\eta (j_{l})$ ,  $p_{T}(j_{b})$ ,  $m(t)$ ,  $m(e^{+}j_{b})$  in the large range,  $\cos (\theta_{e^{+}j_{l}}^{t})$  and  $\cos (\theta_{j_b j_l}^t)$ . For all these observables, also in the  $W +$  jets case, NLO QCD scale uncertainties are large and are not compatible with the LO ones.

At variance with Single-Top, the light-jet and the  $b$ -jet distributions have a very different shape in the case of  $W+$  jets contribution to the signature (2.1). Therefore, the fact that all jets with  $|\eta| > 2.5$  are tagged as light jets has a strong impact on the  $\eta(j_l)$  distribution (top-left plot). Indeed, especially in the (NLO QCD)/LO ratio, this distribution shows a very different behaviour for  $|\eta(j_l)| < 2.5$  and  $|\eta(j_l)| > 2.5$ . The NLO EW corrections are instead rather flat. Moving to  $p_T(j_b)$  (top-right plot), the impact of NLO QCD corrections on this distribution is very different from the Single-Top case. At small  $p_T(j_b)$  values the QCD  $K$ -factor is almost equal to 3 and becomes much smaller than 1 at large  $p_T(j_b)$ . Therefore, also in the case of  $W+$  jets shower effects are expected to be relevant. Results at the inclusive level including QCD shower effects are presented in section 3.3.1 for  $W+$  jets. NLO EW corrections exhibit a negative growth for large  $p_T$  values due to the jet veto, but for this observable are smaller in absolute value than in the case of Single-Top, reaching at most  $-5\%$  in the tail. The  $m(t)$  distribution and the corresponding NLO QCD corrections (center-left plot) are very flat in the range considered, since no top-resonance is present. However, the (NLO QCD+EW)/(NLO QCD) ratio is non-flat around  $m(t) \sim m_t$ , with the typical shape induced by a resonance and has a  $+10\%$  impact for  $m(t) \lesssim m_t$ . This effects is induced by interferences among real emission diagrams of  $\mathcal{O}(\alpha_s^{3/2}\alpha)$  and  $\mathcal{O}(\alpha_s^{1/2}\alpha^{3/2})$ , where the latter order contains diagrams with  $s$ -channel top-quark propagators and therefore induces this effect. On the other hand, in the case of  $m(t^{\mathrm{rec}})$  we have checked that the non-flat effect is reduced a lot, being at most  $2\%$ .

For all the three remaining distributions in figure 4, NLO EW corrections are small and flat w.r.t. the NLO QCD predictions, while the QCD  $K$ -factor is not flat. Since top-quark resonances are not present at LO or NLO QCD, the shape of the  $m(e^{+}j_{b})$  distribution is completely different from the Single-Top case and consequently also the QCD  $K$ -factor, which is positive over the full  $m(e^{+}j_{b})$  range considered and ranges form  $\sim 3$  at  $m(e^{+}j_{b}) = 20\mathrm{GeV}$  to  $\sim 1.5$  at  $m(e^{+}j_{b}) = 160\mathrm{GeV}$ . The same argument applies also to the  $\cos (\theta_{e + j_l}^t)$  and  $\cos (\theta_{j_bj_l}^t)$  distribution. On the other hand, while in the case of  $\cos (\theta_{e + j_l}^t)$  the QCD  $K$ -factor monotonically decreases from 1.2 at  $\cos (\theta_{e + j_l}^t) = -1$  to 0.8 at  $\cos (\theta_{e + j_l}^t) = 1$ , in the case of  $\cos (\theta_{j_bj_l}^t)$  it monotonically grows from 0.7 at  $\cos (\theta_{j_bj_l}^t) = -1$  to 3 at  $\cos (\theta_{j_bj_l}^t) = 1$  using our binning.

![](images/0bcf2870360a95f364d5f886bdb7c3b4c3850953e81925ecc9cf78078110a93b.jpg)

![](images/a687b100d334fa1bc531b0540565e71672fffe01cb0caa736f7553f84237c53d.jpg)

![](images/cbe24e1fb1890d011dc821c4bc46d88bf2558fa223919fbf4c7b39e3614356d3.jpg)

![](images/ef94edfb578cb00fb74e5f8106065e8880e4afe80e66a228396d7421df6d66f8.jpg)

![](images/2ee41ceef02571e94369be40fa9c74bd2381e64099605c528bec470178307594.jpg)  
Figure 4. LO, NLO QCD and NLO QCD+EW predictions for the observables from figures 2 and 3 that show non-flat effects from either NLO QCD or NLO EW corrections for the  $W+$  jets process.

![](images/32306456911f86c5adbc9b64b7ae33357ff36416796f0e49b8f054a64cda5afb.jpg)

![](images/7b0ccb760908bb3815720fcd711639912bf3293bad89b1adbdbaaa46391a5359.jpg)

![](images/7ffe0eac9f03de36deaad52af2fba6c2d9a51b13b8806c4366f9f4f209ea6094.jpg)

![](images/3c511ef9507eae5b3a54249c7d9a8e2ad6bbd63ba1002e6bfd5b4d232e5031d2.jpg)

![](images/c9ed102245915779bb152660c05e039aabe99f4b3ab7b2beeef27949c4e8bb62.jpg)

![](images/43e4d2933e968d0799c9b94a1dab5c338ed8685d551b681e5093324c44ce241f.jpg)  
Figure 5. Comparison between Single-Top and  $W+$  jets predictions at NLO QCD+EW accuracy for the same observables considered in figure 2.

![](images/346dc6304253e568d066de545ab4c9f225e18a3fa9dfd47d26ebe5ecb84d67bc.jpg)

Finally, in figures 5 and 6 we plot the predictions at NLO QCD+EW accuracy for Single-Top and  $W+jets$  for the same distributions considered in figures 2 and 3, respectively, and we show in the inset of each plot their ratio (Single-Top)/(W+jets), including scale uncertainties. In this case we do not normalise the  $\cos(\theta_{e+j_l}^t)$  and  $\cos(\theta_{j_b j_l}^t)$  distributions. At the inclusive level (Single-Top)/(W+jets)~1.7, but several distributions show a very strong kinematic dependence for this quantity. As expected, in the case of  $m(t)$  in the range shown in figures 6 the (Single-Top)/(W+jets) ratio is much larger than at the

![](images/cb97a3b9cf791ea80e34b61d7df24d317f8b4a57386a4b2f77d610440ab7f9ae.jpg)

![](images/33bf4662c3e6245c14fc38f124f4f2bdd8a08d3c8c53e3bcfeb299ec17eba21f.jpg)

![](images/1931fb3ae35e99ab4bfe658efcf72d7eb37f9daf65f8189342f96056aad8a736.jpg)

![](images/8685a6f41b1eb19451bddc0c880718bcac2bb708db36d4c6b60670585e59a621.jpg)

![](images/39dc75d2dcbf0c289c1ff93de0abf28a67a3d0843a1d84ad74718e385f5c34ab.jpg)  
Figure 6. Comparison between Single-Top and  $W+$  jets predictions at NLO QCD+EW accuracy for the same observables considered in figure 3.

![](images/3fc55aeb73db0e3c72b37403089b625fe6d14f2b4029b83de0d2cc728dbe29d9.jpg)

inclusive level, however, this feature is strongly reduced for the experimental observable  $m(t^{\mathrm{rec}})$ . Non-negligible effects are also present for the remaining distributions. Notably, (Single-Top)/(W+jets) reduces to almost 1 for  $m(e^{+}j_{b})$  in the region around the endpoint  $m(e^{+}j_{b}) = \sqrt{m_{t}^{2} - m_{W}^{2}} \sim 154\mathrm{GeV}$ .

The case of  $\eta(j_l)$  is somehow special. As can be seen in figure 5, the ratio (Single-Top)/(W+jets) strongly increases moving from the central to the peripheral region. This is particularly interesting for two reasons. First, the Single-Top  $\eta(j_l)$  distribution is rather flat, so cutting the central region the decrease of the total cross section is not dramatic.

Second, as discussed in detail in appendix A, the  $tW$  contamination to the fiducial region we are considering is mainly affecting the central region of the  $\eta (j_l)$  distribution. Therefore, applying a veto on central light jets may at the same time improve the sensitivity to Single-Top production and also reduce the contamination from  $tW$ , leading to a measurement closer to the true  $t$ -channel single-top production. We have also verified that  $t\bar{t}$  production, which is the main background in the measurements of  $t$ -channel single-top production via the signature (2.1), has much more central distribution for  $\eta (j_l)$  too.

The reader should note also that in figures 5 and 6 scale uncertainties are associated to the NLO QCD+EW predictions, unlike in the plots of figures 2-4, which display NLO QCD scale uncertainties. As can be seen, in the case of Single-Top, the relative size of the NLO QCD+EW scale uncertainties is a bit larger than the NLO QCD ones in specific phase-space regions. The main reason is that when NLO EW are large and negative, for example at large  $p_T(j_l)$  and  $p_T(j_b)$ , the central value is reduced and therefore the relative size of the scale uncertainties increases.

# 3.3 Shower effects matched to NLO QCD

In this section we provide numerical results at NLO QCD accuracy including shower effects for the signature (2.1) within the cuts specified in section 3.1. Details on the calculational framework are described in section 2.2. In section 3.3.1 we present the inclusive results for separately  $W+$  jets and Single-Top production. In section 3.3.2 we show and comment on differential distributions for Single-Top case only.

# 3.3.1 Total cross section

We start discussing the case of Single-Top production and then we move to the  $W+$  jets case. In table 3 we compare LO and NLO results for Single-Top production including shower effects, denoted respectively as LOPS QCD and NLOPS QCD, together with the corresponding results at fixed-order. In the same table we also show three different ratios in order to separately display the impact of shower effects and NLO corrections. As can be seen, the LOPS QCD result is much smaller than the LO one, the shower effects reduce the cross section by a factor 0.64. This effect is due to the jet veto, i.e., the request that there are at most two jets. We remind the reader that for this reason results strongly depend on the  $R^{\mathrm{QCD}}$  and  $p_{t,\min}^{\mathrm{QCD}}$ . On the other hand, once the shower effects are taken into account, NLO effects have a no impact at inclusive level with the ratio being at 1.00 and the NLOPS QCD result is higher by a factor of 1.08 w.r.t. the NLO QCD one. At variance with the fixed-order case (see table 2), NLO effects do reduce the scale uncertainty, which moves form  $+8.2\%$  to  $+3.3\%$ . This result is important for two reasons. First, it shows that if the actual experimental fiducial region is considered, parton-shower effects (or possibly analytic jet-veto resummation) are necessary in order to reduce theory uncertainties for Single-Top predictions. It is not even clear if NNLO QCD effects would reduce the scale uncertainties or anyway would be useful for estimating the theory error. Indeed, although in ref. [39] a reduction of scale uncertainties is progressively observed moving from LO to NLO and then to NNLO accuracy, this reduction is very sensitive to the definition of the fiducial region (which is different in ref. [39] and in this work), see also appendix A. Also, in ref. [39] it

Table 3. Total cross section and scale uncertainty in various QCD approximations for the signature (2.1) from Single-Top production within the fiducial region defined in section 3.1. The ratios are computed from the central values of their corresponding predictions.  

<table><tr><td>Single-Top</td><td>cross section</td></tr><tr><td>LO</td><td>4.623(1) +0.415(+9.0%) -0.533(-11.5%) pb</td></tr><tr><td>LOPS QCD</td><td>2.968(3) +0.28(+9.3%) -0.35(-11.9%) pb</td></tr><tr><td>NLO QCD</td><td>2.762(6) +0.226(+8.2%) -0.240(-8.7%) pb</td></tr><tr><td>NLOPS QCD</td><td>2.974(9) +0.098(+3.3%) -0.098(-3.3%) pb</td></tr><tr><td>(NLOPS QCD)/(LOPS QCD)</td><td>1.00(1)</td></tr><tr><td>(LOPS QCD)/LO</td><td>0.64(1)</td></tr><tr><td>(NLOPS QCD)/(NLO QCD)</td><td>1.08(1)</td></tr></table>

was pointed out that LO, NLO and even NNLO QCD uncertainty bands do not overlap. Second, NLO electroweak corrections at fixed order reduces the NLO QCD corrections by  $\sim -3\%$ , i.e., their impact is at the same level with the scale uncertainty at NLOPS QCD. Summarising, both QCD shower and EW fixed-order effects are important in order to further improve the precision of predictions for the fiducial region. However, these two results cannot be directly combined, being the latter based on a fixed-order computation for a process where shower effects are very large. The technology for matching NLO EW, and more in general complete-NLO, calculations to shower effects would be very useful for the calculation studied here. We summarise in the plot in figure 7 the results obtained for the total cross section within the fiducial region, including the scale uncertainties, for different approximations discussed in this section and in section 3.2.1.

Using the same layout of table 3 and figure 7 we show predictions at fixed order and including shower effects for  $W+$  jets production in table 4 and figure 8. At variance with the Single-Top case, the LOPS QCD result is larger than the LO one; the shower effects increase the central value of the cross section by a factor 1.78. Although the jet veto (at most two jets) is present, the additional radiation induced by the shower splits part of the final-state gluons into  $b\bar{b}$  pairs, converting events with two light jets into events with one  $b$ -jet and one light jet, which in turn contribute to the signature (2.1). Therefore, as explained in more details in section 3.2.1, the real radiation leads to an increase of the cross section, even though a jet veto is present. Matching the shower simulation to NLO QCD corrections, and therefore improving the simulation of hard real radiation, further increases the cross section by a factor 1.31. In this case the central value of the NLOPS QCD result is higher by a factor of 1.11 w.r.t. the NLO QCD one.

For  $W +$  jets the jet veto induced by the signature (2.1) is not leading to negative corrections, but nevertheless is preventing fixed-order calculations to substantially improve the scale uncertainties moving from LO to NLO. However, like in Single-Top, taking into account shower effects, NLO corrections do reduce the scale uncertainty, which moves from  $+31.1\%$  at LOPS to  $+5.1\%$  at NLOPS QCD. Therefore, also for  $W +$  jets contributions to

![](images/33bc50aadc561fb87e430fb1dfce3e486dfe041a7072320894cc6728cd84c42c.jpg)  
Figure 7. Single-Top cross section and their uncertainty from scale dependence in the fiducial region in various approximations. Corresponding numbers are listed in tables 2 and 3.

Table 4. Total cross sections and their uncertainty from scale dependence in various QCD approximations for the signature (2.1) from  $W+$  jets within the fiducial region defined in section 3.1. The ratios are computed for the central values of the corresponding predictions.  

<table><tr><td>W+jets</td><td>cross section</td></tr><tr><td>LO</td><td>0.7656(6)+0.3002(+39.2%) -0.2265(-29.6%) pb</td></tr><tr><td>LOPS QCD</td><td>1.36(2)+0.42(+31.1%) -0.32(-23.6%) pb</td></tr><tr><td>NLO QCD</td><td>1.612(3)+0.323(+20.1%) -0.309(-19.2%) pb</td></tr><tr><td>NLOPS QCD</td><td>1.79(5)+0.09(+5.1%) -0.18(-10.3%) pb</td></tr><tr><td>(NLOPS QCD)/(LOPS QCD)</td><td>1.31(4)</td></tr><tr><td>(LOPS QCD)/LO</td><td>1.78(3)</td></tr><tr><td>(NLOPS QCD)/(NLO QCD)</td><td>1.11(3)</td></tr></table>

the signature (2.1), parton-shower effects (or possibly analytic jet-veto resummation) are necessary in order to reduce theory uncertainties. On the other hand, the impact of NLO EW corrections on top of NLO QCD predictions is much smaller ( $\sim 1\%$  at the inclusive level) than the scale uncertainty even at NLOPS QCD accuracy. Given the results that we have found at the inclusive and differential level for NLO EW corrections (see section 3.2), in the case of the  $W+$  jets contribution to the signature (2.1), the impact of EW corrections is negligible and their combination with showered effects is not so relevant as in the case of Single-Top.

![](images/70eac9d9dcd4e768f2cee57e9a46f9a1da2f4cd3fffc3257b901eef2b1fb4c5b.jpg)  
Figure 8.  $W+$  jets cross sections and their uncertainties from scale dependence in the fiducial region in different approximations. Corresponding numbers are listed in tables 2 and 4.

# 3.3.2 Differential distributions

We move now to differential distributions for Single-Top production. In figures 9 and 10 we show the NLOPS QCD predictions for the observables already considered in figures 2 and 3. In the main panel we show the central value for NLO QCD and NLOPS QCD predictions, while in the first inset we compare their scale uncertainties normalised to the central value of the NLO QCD prediction. Since the NLOPS QCD scale uncertainties are much smaller than the corresponding NLO QCD ones, it is interesting to compare them with the size of the NLO EW corrections, which on the other hand can be computed at the moment only at fixed order (see discussion in section 2.2). For this reason, in the second inset we show the NLOPS QCD scale uncertainty band normalised to its central value together with the  $(\mathrm{NLOQCD + EW}) / (\mathrm{NLOQCD})$  ratio already shown in figures 9 and 10. In other words, in such a way, we can directly compare the scale uncertainty at NLOPS QCD accuracy with the impact of NLO EW corrections on top of the corresponding fixed-order calculation.

As at the inclusive level, NLOPS QCD scale uncertainties are in general smaller than the NLO QCD ones and are roughly of the same size as the NLO EW corrections in absolute value. However, shower effects are largely enhanced in many regions of the phase space and especially the NLOPS QCD and NLO QCD predictions can be incompatible at the differential level. In the tails of the  $p_T$  distributions for the light-jet, the  $b$ -jet and the reconstructed top-quark, scale-uncertainty bands are much smaller when shower effects are taken into account and especially they are clearly outside the corresponding NLO QCD scale-uncertainty bands. Moreover, in all the three cases, EW corrections are also much larger than the NLOPS QCD scale uncertainties. The corresponding (pseudo)rapidity

![](images/cbab8cdb1b5bd6b04a39928d3ae4a50fb6cac5122c3b1bd1ae519b541fae10e5.jpg)

![](images/4ef9eb1e28b11839602afe1da3d86127481648886bd7bf88bbfdeb8a6fcf1031.jpg)

![](images/0a83555ef2163ddfc5468620cffba6b400264a2ca49cf9f56f398cf8531cbd8f.jpg)

![](images/98c93eedd9d9cde361d08d91936c3bae56634d3f41f1684931c003cbfeb1b87e.jpg)

![](images/8c461754c32735dbc55ce1240a5683a07ebc076584dbccc75b8b1321c0700e16.jpg)  
Figure 9. Predictions at NLO(PS) QCD accuracy for the same observables considered in figure 2 for the Single-Top process. Note that the second inset shows the ratio of the NLO QCD+EW over the NLO QCD process, but with the relative uncertainty from the NLOPS QCD superimposed on the latter.

![](images/d8139f3bdb6243b60522db202559fd22d5ae0ff5193a920d5760539c25972389.jpg)

![](images/5bcee3c7eb90a0e72c4c4408bcf84bff06279b259b690078bc577e9d313c1428.jpg)

![](images/c63fb3b42f638d96da12e9f63e08a7293886f4e31edc6aeb9a855873a12bf484.jpg)

![](images/bc76f35c2db1fa71fc34339ff13d5f2bc5e66500de42900e81f7581c6740a2d7.jpg)

![](images/29279e3cf5f905ce8cad0fae9e22f02a2ee43513a1178b33ae942fe7449183c2.jpg)

![](images/2f5be6bb856bad7c732ee95d8bcde7c8267cf4a13c8d0c1527ea3e3273f4de2f.jpg)  
Figure 10. Predictions at NLO(PS) QCD accuracy for the same observables considered in figure 3 for the Single-Top process. Note that the second inset shows the ratio of the NLO QCD+EW over the NLO QCD process, but with the relative uncertainty from the NLOPS QCD superimposed on the latter.

![](images/78ee150c8c43746cfbb1e46a21a151c921e8643b205332bceb53cf1475d79e54.jpg)

distributions instead show compatible results at NLO QCD and NLOPS QCD accuracies, with anyway the latter with smaller scale uncertainties. For these distributions, electroweak corrections are negative and, in absolute value, as large as the scale uncertainties at NLOPS QCD, with the exception of the central region for  $\eta (j_l)$ .

As expected, the case of  $m(t)$  is extreme, especially for the region  $m(t) \gtrsim m_t$  where NLOPS QCD predictions are larger and far outside the NLO QCD ones. Also the region  $m(t) < m_t$  is strongly affected, with scale uncertainties very much reduced and decreasing the prediction to the lower edge of the NLO QCD scale-uncertainty band. In other words, the QCD parton shower has an opposite effect w.r.t. NLO QCD corrections on top of LO, and therefore it flattens the distribution. Again, this distribution is strongly affected by the  $R^{\mathrm{QCD}}$  and  $p_{t,\min}^{\mathrm{QCD}}$  parameters. Around the peak, EW corrections are much larger than NLOPS QCD scale uncertainties and in minor extent also in the region  $m(t) < m_t$ . However, similarly to the QCD case, the QED shower is expected to reduce these effects, which also strongly depend on the parameter  $R^{\mathrm{QED}}$  for the clustering of photons with leptons. In the case of  $m(t^{\mathrm{rec}})$  we observe the same features, but in a milder way. Similarly to the fixed-order case, the realistic  $m(t^{\mathrm{rec}})$  observable is flatter than the purely theoretical quantity  $m(t)$  and therefore migration effects from the peak are less severe.

The  $m(e^{+}j_{b})$  distribution shows effects similar to those at the inclusive level, with the exception of the phase-space region close to the end-point  $m(e^{+}j_{b}) = \sqrt{m_{t}^{2} - m_{W}^{2}}\sim 154\mathrm{GeV}$ , see central-left and -right plots of figure 10. Indeed, in most of the phase space the corrections from parton showering are small and positive, but significantly reduce the NLO QCD scale uncertainties. However, close to the end-point, the corrections increase to a maximum of  $\sim 25\%$  at  $m(e^{+}j_{b})\simeq 140\mathrm{GeV}$ ; once we exceed the  $m(e^{+}j_{b})\simeq 150\mathrm{GeV}$  and enter the off-shell region the shower effects reduce very fast. Hence, the parton shower partially compensates the large fixed-order NLO QCD corrections, and introduces non-trivial alterations to the shape of the  $m(e^{+}j_{b})$  distribution close to the end-point. A similar dynamics is also present for the region  $\cos (\theta_{e^{+}j_{l}}^{t}) < - 0.5$ , where the shower effects reduce the NLO QCD prediction by up to  $20\%$ . In the rest of this distribution, the shower effects are small, except for the final bin, where the corrections are large and positive. In the case of  $\cos (\theta_{j_b j_l}^t)$ , shower effects are small, similarly to the NLO corrections at fixed order, with at most  $\sim 10\%$  effects. This observable therefore turns out to be very stable under radiative corrections.

# 4 Conclusions

In this work we have calculated and provided precise predictions for the signature (2.1), which belongs to the class of those exploited at the LHC for the measurement of  $t$ -channel single-top production. All the results presented in the main text of the paper have been obtained by applying the cuts that are listed in section 3.1, defining the fiducial region.

First, we have calculated the complete-NLO predictions, i.e., all NLO effects of QCD and EW origin, for the signature (2.1). We have shown that also other resonant processes contribute at this accuracy and we provided predictions at the inclusive and differential level for all the perturbative orders entering the complete-NLO results. According to the

underlying resonance structure (see table 1) we have denoted the orders  $\mathrm{LO}_1$ ,  $\mathrm{LO}_2$ ,  $\mathrm{NLO}_1$  and  $\mathrm{NLO}_2$  as  $W+$  jets and  $\mathrm{LO}_3$ ,  $\mathrm{NLO}_3$  and  $\mathrm{NLO}_4$  as Single-Top (see also eq. (2.5)). The latter does include also contributions from the  $s$ -channel single-top,  $tW^{-}/\bar{t}W^{+}$  and  $WZ$  production, which we have not subtracted since we directly provide predictions for the signature (2.1).

Second, for both Single-Top and  $W+$  jets production we have calculated LO and NLO QCD predictions matched to parton-shower effects. As discussed in section 2.2, the necessary technology for matching NLO QCD+EW predictions to shower effects, and possibly including also photon emissions in the shower, is not yet available. However our study clearly shows that it is desirable and, for particular observables, necessary in order to obtain precise and reliable predictions.

Here, we summarise our main findings. At the inclusive level NLO EW corrections to Single-Top production are of order  $-3\%$  w.r.t. the NLO QCD prediction, which reduces the LO cross section by  $\sim 40\%$  and scale uncertainties (only) from  $\sim \pm 10\%$  at LO to  $\sim \pm 8\%$  at NLO QCD. This effect is due to the presence of the jet-veto imposed by the signature (2.1). However, once parton-shower effects are taken into account, NLOPS QCD predictions reduce scale uncertainties to  $\sim \pm 3\%$  and increase the fixed-order NLO QCD prediction by  $8\%$ . Notably, NLO EW corrections are in absolute value of the same order as QCD scale uncertainties when parton-shower effects are included. We have also found that the impact of QCD corrections strongly depends on the cuts applied and in general on the definition of the fiducial region. Moreover, as documented in appendix A, the contributions from  $s$ -channel and  $tW^{-} / \bar{t} W^{+}$ production are sizeable also in the fiducial region.

At the differential level, both EW and QCD effects can be enormous and consequently also the effect from parton showering is very large. For instance, for values of  $p_T \sim 250\mathrm{GeV}$ , for both the light- and  $b$ -jet, NLO QCD corrections reduce the LO prediction by  $80\%$  and similar effects are present for the reconstructed top-quark mass close to the  $m_t$  value. Moreover, in these phase-space regions, scale uncertainties are of order  $\sim \pm 50\%$  at NLO QCD, and even larger at NLO QCD+EW. However, shower effects reduce them to the order of  $\sim \pm 3\%$ , as at the inclusive level, and shift the predictions outside the scale-uncertainty band of NLO QCD predictions at fixed-order. The NLO EW corrections are also in general much larger than the percent level; in the case  $p_T(j_b) \sim 250\mathrm{GeV}$  they are of the order of  $-50\%$  w.r.t. the NLO QCD prediction. Therefore, since the origin of the enhancement is also in this case the jet veto, the multiple emission of photons and QCD partons via EW interactions is also expected to have a non-negligible impact in these specific phase-space regions. Also, NLO EW corrections are in general larger, or at least as large as, the NLOPS QCD scale uncertainty in absolute value over the full phase space. Last but not least, it is also important to remember that the opening of new resonating channels at NLO induces important distortions on distributions, such as the pseudorapidity of the light jet.

In the case of  $W +$  jets the situation is different. At the inclusive level, NLO EW corrections are of order  $-1\%$  w.r.t. the NLO QCD prediction, which increases the LO cross section by a factor  $\sim 2.1$  and reduces the scale uncertainty from  $\sim_{-30\%}^{+40\%}$  at LO to  $\sim \pm 20\%$  at NLO QCD. The increase due to the NLO QCD corrections is quite surprising, given

the presence of the jet veto. However, as explained in the text, NLO QCD corrections induce  $g \rightarrow b\bar{b}$  splittings that lead to the migration of LO contributions inside the signature (2.1). Once parton-shower effects are taken into account, NLOPS QCD predictions reduce scale uncertainties to  $\sim_{-10\%}^{+5\%}$  and increase the fixed-order NLO QCD prediction by 11%. Therefore, at variance with the Single-Top case, NLO EW corrections are in absolute value much smaller than QCD scale uncertainties also including parton-shower effects. At the differential level, both NLO QCD and EW corrections are mostly flat for the observable we considered. On the other hand, few exceptions are present and include, e.g., the distribution of the rapidity of the light jet and the  $p_T$  of the  $b$ -jet at small values.

In conclusion, our study demonstrates the relevance of both EW corrections and shower effects for obtaining precise and reliable theoretical predictions for the single-top-production fiducial region. Therefore, in this context, the possibility of performing NLO QCD+EW corrections matched with QCD and QED shower simulations would be desirable. Finally, from the experimental side, we also suggest to study the possibility of applying a veto on central light jets in order to increase the Signal/Backgrounds ratio. Indeed such a cut suppresses much more the contributions of  $W +$  jets,  $tW^{-} / \bar{t} W^{+}$  production and also  $\bar{t}\bar{t}$  production, which is the main background in the measurement of  $t$ -channel single top production, than the contribution from  $t$ -channel single-top itself.

# Acknowledgments

This work has been supported in part by the Alexander von Humboldt Foundation, in the framework of the Sofja Kovalevskaja Award Project "Event Simulation for the Large Hadron Collider at High Precision". D.P. has been also supported by the Deutsche Forschungsgemeinschaft (DFG) through the Collaborative Research Centre SFB1258. R.F. is supported in part by the Swedish Research Council under contract number 2016-05996.

# A Comparisons with previous results and different approximations

The purpose of this appendix is twofold. First, we want to compare our NLO QCD results for Single-Top production and decay with those presented in the literature, in particular the NLO results from refs. [38] and [39]. These calculations used different input parameters $^{8}$  and applied different cuts than those specified in section 3.1. Moreover, these calculations are performed employing a different approximation. Indeed, not only for the NNLO but also in the NLO case, only factorisable corrections in the narrow-width approximation for the  $t$ -channel  $pp \rightarrow tj_l$  production with the subsequent leptonic top-quark decay are taken into account; non-factorisable corrections, non-resonant contributions, and the contributions from  $s$ -channel and  $tW$  to the full final state have been ignored. Second, we want to explore the effects of the different cuts of the fiducial region for the signature (2.1). For this purpose we start from the case of  $pp \rightarrow tj_l$  production and we progressively take into account the  $t \rightarrow Wb$  and  $W \rightarrow e^{+} \nu_{e}$  decay and the effects of the cuts, directly comparing the obtained results with those of refs. [38] and [39] for the same final state. We show results

![](images/23000bf432881807336f203b3f9e943e9b000d61832b2dacf07fed340653af0d.jpg)

![](images/5042b941f354dc3a3aa76ff55b4977b1e4966e7d063902dc6116469e1210fbc1.jpg)

![](images/99825b2fe4be8455a4cd5382027f37cdeb5d31925ff6fbaade784ebe01904fa0.jpg)  
Figure 11. Differential distributions for the process  $pp \to t j_{l}$  at LO and NLO QCD accuracy. They can be compared with figures 20 and 22 (bottom-left plots) of ref. [39].

![](images/bc11092842328c3afa96de79e81d3a0fa48d7ec9a9037c1b35afc1bc641b36be.jpg)

at the total cross-section level and for the light- and  $b$ -jets distributions. It is important to bear in mind that none of the aforementioned approximations are well-defined if we want to take into account EW corrections as done in section 3.2 — here we are comparing only fixed-order QCD effects.

At the production level,  $pp \rightarrow tj_l$ , we find perfect agreement both at LO and NLO accuracy with the settings of ref. [39], where no  $p_T$  cut for the jet (clustered with  $\Delta R_j = 0.5$  and anti-  $k_{T}$  algorithm) is set. Clearly, in order to obtain the agreement, we have excluded  $s$ -channel single-top contributions by excluding any diagram with a  $W$  boson in the  $s$ -channel. We also perform a comparison at the differential level for the leading jet, which accordingly to ref. [39] can be either a light or  $b$ -jet.

In the top plots of figure 11 we show LO and NLO contributions as well the  $K$ -factor for the transverse momentum and the rapidity of the hardest jet. Comparing these plots with the distributions in figures 20 and 22 of ref. [39] we find a very good agreement. The lower plots show the case of the light jet (which is always identified with the hardest jet only at LO). From the comparison of upper and lower plots we understand that  $b$ -jets emerging from real emissions are more central than the light jet.

Table 5. Comparison between the two approximations (A and B) described in the text, at the cross section level. The LO  $tW$  process contributes to the NLO QCD in the approximation B. At NLO we use  $\Gamma_t^{\mathrm{NLO}}$ .  

<table><tr><td>Order</td><td>Ref. [39] [pb]</td><td>A [pb]</td><td>B [pb]</td><td>tW [pb]</td><td>s-channel [pb]</td></tr><tr><td>LO (ΓtNLO)</td><td>-</td><td>157.88(1)+8.1%-10.2%</td><td>163.96(2)+7.8%-10.0%</td><td>-</td><td>5.15(2)+2.6%-3.4%</td></tr><tr><td>LO (ΓtLO)</td><td>144.5+8.1%-10%</td><td>144.3(4)+8.1%-10.3%</td><td>150.7(4)+7.8%-9.9%</td><td>-</td><td>4.73(2)+2.6%-3.4%</td></tr><tr><td>NLO QCD</td><td>138.8+2.9%-1.7%</td><td>137.8(3)+3.3%-1.7%</td><td>160.5(1)+2.4%-2.3%</td><td>19.1(1)+16.5%-15.9%</td><td>-</td></tr></table>

We move now to the process  $pp \to W^{+}bj_{l}$ . In this case, in order to be close to the calculation in ref. [39], we use two different approximations.

- Approximation A: we remove all diagrams with  $W$ ,  $Z$  and/or photon  $s$ -channel propagators.  
- Approximation B: we remove all diagrams with  $Z$  and/or photon (but not  $W$ ) propagators.

In practice, the former does not include any single-top  $s$ -channel or  $tW$  contribution, but it includes non-resonant effects with no intermediate top quarks already at LO. The latter instead involves only contributions from resonant diagrams at LO, which on the other hand includes also  $s$ -channel single-top contributions. Similarly,  $tW$  contributions are present at NLO. For the comparison with the results in ref. [39] we calculate the LO contribution from  $pp \rightarrow W^{+}bjj$ , with a  $W^{-}$  and a top-quark in  $s$ -channel propagators, i.e., the  $tW$  contribution with top-quark leptonic and  $W^{-}$  hadronic decays. Also, we calculate the LO contribution from  $s$ -channel single top ( $pp \rightarrow W^{+}b\bar{b}$  vetoing any  $Z$  or photon in the diagrams). Since in the Approximation A initial-state collinear QED divergencies from  $b \rightarrow b\gamma$  splittings are already present at the LO, we use the generation cuts at the matrix-element level  $\Delta R_{j} > 0.5$ ,  $p_{T}(j) > 5\mathrm{GeV}$ .

In table 5 we display the numerical results for the calculations we have just described and we compare with the results from ref. [39], which on the other hand are still at the purely production level  $pp \rightarrow t j_{\ell}$ . However, although we apply some technical cuts on the jets, we can still perform a qualitative comparison between results from table 5 and Approximations A and B, being  $\mathrm{Br}(t \rightarrow Wb) \simeq 1$ . More important is the use of a consistent value of  $\Gamma_{t}$ , which is very different at LO and NLO.

The consistent use of  $\Gamma_{t}$  is necessary for achieving the agreement at LO. Indeed, in ref. [39] the LO value of  $\Gamma_{t}$  is used for LO calculations, while in the NLO calculations the NLO value is used. Moreover, moving from the approximation A to B, there is a  $\sim 5\%$  increase at LO due to the  $s$ -channel inclusion. At NLO QCD, also the  $tW$  production is included and since at this point there are no cuts designed for  $t$ -channel single top, their effect cannot be ignored. At LO, the best agreement with the results of ref. [39] is achieved with the Approximation A, which does not include the  $s$ -channel. Similarly a good agreement is present for the value of the Approximation B subtracting the  $s$ -channel contribution. In both cases, the usage of  $\Gamma_{t}^{\mathrm{LO}}$  is crucial. At the NLO level the Approximation A, but also

![](images/9435fdc2bcd402b952a76b976d0e21ee7313b8f83e72de69ae5978f246e00d91.jpg)

![](images/3d7c38b77658e9341393cc0b35bfd64f40190719b9590a9e98850a1bf654ecf6.jpg)

![](images/b221ae1e7cc97c93a9025027f6006b51dc157179255f4056a38e58b4d7de7d17.jpg)  
Figure 12. The LO and NLO QCD predictions for the  $p_T(j_l)$  and  $\eta (j_{l})$  distributions for the process  $pp\to tj_l(t\to Wb)$  using Approximations A (left) and B (right).

![](images/88f65d6d74bce9d639d73ed834b5edda13386b2b378ed2a004bd577d46775d87.jpg)

the Approximation B subtracting the  $s$ -channel and  $tW$  contributions have a qualitatively good agreement with ref. [39].

We also show in figure 12 a comparison between the approximation A (left) and B (right) for the  $p_T$  (top) and the  $\eta$  (bottom) distributions of the (leading) light jet. The inclusion of the  $s$ -channel single-top and the  $tW$  production flattens the  $K$ -factor of the  $p_T$  distribution and completely changes the shape of the  $\eta$  distribution. The reason is that for both these two additional contributions the leading light jet is more central. So although we have considered only light jets, we see a similar effect to the one observed for the upper-right plot of figure 11.

Then we compare Approximations A and B after applying part of the fiducial-region cuts of section 3.1. Specifically,

- light jet:  $|\eta (j_{l})| < 5$ ,  $\Delta R > 0.5$ ,  $p_{T}(j_{l}) > 40\mathrm{GeV}$  
-  $b$ -jet:  $|\eta(j_b)| < 2.4$ ,  $\Delta R > 0.5$ ,  $p_T(j_b) > 40 \, \mathrm{GeV}$ ,  
- event veto: require exactly two jets of which exactly one is a  $b$ -jet.

Table 6. Comparison between approximations A and B applying subsequent jet vetoes.  

<table><tr><td>Vetoes</td><td>Order</td><td>A [pb]</td><td>B [pb]</td><td>tW [pb]</td><td>s-channel [pb]</td></tr><tr><td rowspan="2">No jet veto</td><td>LO</td><td>157.2(2)-8.1%</td><td>163.8(1)-7.8%</td><td>-</td><td>5.17(2)-2.6%</td></tr><tr><td>NLO QCD</td><td>131(2)-10.3%</td><td>159(1)-10.0%</td><td>-</td><td>-</td></tr><tr><td rowspan="2">nj=2, nb&gt;1</td><td>LO</td><td>74.9(1)-7.6%</td><td>79.2(2)-7.4%</td><td>-</td><td>2.83(2)+2.0%</td></tr><tr><td>NLO QCD</td><td>47.7(6)-9.8%</td><td>59.3(6)-9.6%</td><td>-</td><td>-</td></tr><tr><td rowspan="2">nj=2, nb=1</td><td>LO</td><td>74.8(1)-7.6%</td><td>77.0(1)-7.3%</td><td>-</td><td>0.676(9)+0.9%</td></tr><tr><td>NLO QCD</td><td>41.8(4)-8.4%</td><td>52.9(9)-4.0%</td><td>-</td><td>-</td></tr></table>

These cuts are expected to reduce the  $s$ -channel single-top and the  $tW$  contributions. Especially, the last requirement suppresses the  $s$ -channel single-top, because this channel typically leads to two  $b$ -jets at LO, and the  $tW$  because mostly leads to three jets.

In table 6 we show numerical results applying the aforementioned cuts without requirements on the number of  $(b-)$  jets and then progressively asking exactly two jets and at least one  $b$ -jet and then exactly one  $b$ -jet. The first row of the table actually differs with results of table 5 only for the definition of the jets; the results are qualitative identical. On the contrary, both in the second and third line NLO corrections are negative and therefore reduce the value of the total cross section. Moreover, scale uncertainties are much larger at NLO as compared to no jet veto, especially for Approximation A. This comparison clearly shows that vetoing extra jets leads to larger scale uncertainties. Also, these vetoes strongly suppress the  $s$ -channel contribution, but leave a non-negligible contribution from  $tW$  production; it is  $17\%$  of the results with Approximation B and accounts for most of the difference with the approximation A.

We also show distributions corresponding to the case of the last row of table 6. In figure 13 we show the  $p_T$  (top plots) and  $\eta$  (bottom plots) distributions of the leading light jet. The shape of the  $K$ -factors for the  $p_T$  is similar but this is not the case for the  $\eta$  distribution. This implies that despite being in the fiducial region there are still some contributions with central leading light-jet, which clearly are not related to  $t$ -channel single-top production. Based on the results of table 6, we can conclude that they mostly originate from the  $tW$  production.

Moving to the case where also the  $W \to e^{+} \nu_{e}$  decay is included, we clearly cannot use the Approximation A. We compared the results obtained with the Approximation B with the results in ref. [39], where decays and cuts on decay products are taken into account. Taking into account that non-resonant effects are not present and that they use different scales for the production and the decay, we found again good agreement ( $\sim 2\%$  difference) after subtracting the LO  $s$ -channel single-top contribution and the contribution from  $tW$  production, which represents in total  $\sim 20\%$  of the results in the Approximation B. At the differential level we observe the same features of figure 13. Notably, similarly to ref. [39], we observe also here a reduction of the scale uncertainties moving from LO to NLO, which instead we do not see in the case of Single-Top in table 2, where different cuts have been

![](images/f89c7874616465bbd889279e14976a7ee88698e3eabbe330d8a8283162a140d9.jpg)

![](images/0dbe528ba8c5e7c835938bb80b8e3ac8d5bf3a5a2f03e0037d614afc267e70ef.jpg)

![](images/a54ac9dfb1ac8ab6b8ca121e149bc17d8061653318b81a097f9844e57ddeec0d.jpg)  
Figure 13. Same as figure 12, but applying part of the fiducial-region cuts (see text for details).

![](images/f7e1b51534650cfd363dd7f4412940cbdaececba442b2a57c3f866352715108b.jpg)

used. Therefore, the behaviour of the scale uncertainties is very sensitive to the definition of the fiducial region. Moreover, in ref. [39] it was pointed out that LO, NLO and even NNLO QCD uncertainty bands do not overlap. This comes with no surprise since we have shown in this paper that QCD shower effects are important.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] J. Alwall et al., Is  $V(_{tb}) \simeq 1?$ , Eur. Phys. J. C 49 (2007) 791 [hep-ph/0607115] [INSPIRE].  
[2] H. Lacker et al., Model-independent extraction of  $|V_{tq}|$  matrix elements from top-quark measurements at hadron colliders, Eur. Phys. J. C 72 (2012) 2048 [arXiv:1202.4694] [INSPIRE].  
[3] Q.-H. Cao, B. Yan, J.-H. Yu and C. Zhang, A General Analysis of Wtb anomalous Couplings, Chin. Phys. C 41 (2017) 063101 [arXiv:1504.03785] [INSPIRE].  
[4] E. Alvarez, L. Da Rold, M. Estevez and J.F. Kamenik, Measuring  $|V_{td}|$  at the LHC, Phys. Rev. D 97 (2018) 033002 [arXiv:1709.07887] [INSPIRE].

[5] ATLAS and CMS collaborations, Combinations of single-top-quark production cross-section measurements and  $|f_{\mathrm{LV}}V_{tb}|$  determinations at  $\sqrt{s} = 7$  and 8 TeV with the ATLAS and CMS experiments, JHEP 05 (2019) 088 [arXiv:1902.07158] [INSPIRE].  
[6] T.M.P. Tait and C.P. Yuan, Single top quark production as a window to physics beyond the standard model, Phys. Rev. D 63 (2000) 014018 [hep-ph/0007298] [INSPIRE].  
[7] D. Atwood, S. Bar-Shalom, G. Eilam and A. Soni,  $CP$  violation in top physics, Phys. Rept. 347 (2001) 1 [hep-ph/0006032] [INSPIRE].  
[8] E. Drueke, J. Nutter, R. Schwienhorst, N. Vignaroli, D.G.E. Walker and J.-H. Yu, *Single Top Production as a Probe of Heavy Resonances*, Phys. Rev. D **91** (2015) 054020 [arXiv:1409.7607] [INSPIRE].  
[9] J.A. Aguilar-Saavedra, C. Degrande and S. Khatibi, Single top polarisation as a window to new physics, Phys. Lett. B 769 (2017) 498 [arXiv:1701.05900] [INSPIRE].  
[10] A. Arhrib and A. Jueid, tbW Anomalous Couplings in the Two Higgs Doublet Model, JHEP 08 (2016) 082 [arXiv:1606.05270] [INSPIRE].  
[11] A. Jueid, Probing anomalous Wtb couplings at the LHC in single  $t$ -channel top quark production, Phys. Rev. D 98 (2018) 053006 [arXiv:1805.07763] [INSPIRE].  
[12] A. Arhrib, A. Jueid and S. Moretti, Top quark polarization as a probe of charged Higgs bosons, Phys. Rev. D 98 (2018) 115006 [arXiv:1807.11306] [INSPIRE].  
[13] A. Arhrib, A. Jueid and S. Moretti, Searching for Heavy Charged Higgs Bosons through Top Quark Polarization, arXiv:1903.11489 [INSPIRE].  
[14] Q.-H. Cao, J. Wudka and C.P. Yuan, Search for new physics via single top production at the LHC, Phys. Lett. B 658 (2007) 50 [arXiv:0704.2809] [INSPIRE].  
[15] C. Zhang, *Single Top Production at Next-to-Leading Order in the Standard Model Effective Field Theory*, Phys. Rev. Lett. **116** (2016) 162002 [arXiv:1601.06163] [INSPIRE].  
[16] M. de Beurs, E. Laenen, M. Vreeswijk and E. Vryonidou, Effective operators in t-channel single top production and decay, Eur. Phys. J. C 78 (2018) 919 [arXiv:1807.03576] [INSPIRE].  
[17] N.P. Hartland et al., A Monte Carlo global analysis of the Standard Model Effective Field Theory: the top quark sector, JHEP 04 (2019) 100 [arXiv:1901.05965] [INSPIRE].  
[18] T. Neumann and Z.E. Sullivan, Off-Shell Single-Top-Quark Production in the Standard Model Effective Field Theory, JHEP 06 (2019) 022 [arXiv:1903.11023] [INSPIRE].  
[19] D0 collaboration, Observation of Single Top Quark Production, Phys. Rev. Lett. 103 (2009) 092001 [arXiv:0903.0850] [INSPIRE].  
[20] CDF collaboration, First Observation of Electroweak Single Top Quark Production, Phys. Rev. Lett. 103 (2009) 092002 [arXiv:0903.0885] [INSPIRE].  
[21] CMS collaboration, Measurement of the t-channel single top quark production cross section in pp collisions at  $\sqrt{s} = 7$  TeV, Phys. Rev. Lett. 107 (2011) 091802 [arXiv:1106.3052] [INSPIRE].  
[22] ATLAS collaboration, Measurement of the  $t$ -channel single top-quark production cross section in pp collisions at  $\sqrt{s} = 7$  TeV with the ATLAS detector, Phys. Lett. B 717 (2012) 330 [arXiv:1205.3130] [INSPIRE].  
[23] CMS collaboration, Measurement of the Single-Top-Quark t-Channel Cross Section in pp Collisions at  $\sqrt{s} = 7$  TeV, JHEP 12 (2012) 035 [arXiv:1209.4533] [INSPIRE].

[24] CMS collaboration, Measurement of the t-channel single-top-quark production cross section and of the  $|V_{tb}|$  CKM matrix element in pp collisions at  $\sqrt{s} = 8$  TeV, JHEP 06 (2014) 090 [arXiv:1403.7366] [INSPIRE].  
[25] ATLAS collaboration, Comprehensive measurements of t-channel single top-quark production cross sections at  $\sqrt{s} = 7$  TeV with the ATLAS detector, Phys. Rev. D 90 (2014) 112006 [arXiv:1406.7844] [INSPIRE].  
[26] ATLAS collaboration, Measurement of the inclusive cross-sections of single top-quark and top-antiquark  $t$ -channel production in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, JHEP 04 (2017) 086 [arXiv:1609.03920] [INSPIRE].  
[27] ATLAS collaboration, Fiducial, total and differential cross-section measurements of t-channel single top-quark production in pp collisions at 8 TeV using data collected by the ATLAS detector, Eur. Phys. J. C 77 (2017) 531 [arXiv:1702.02859] [INSPIRE].  
[28] CMS collaboration, Measurement of the single top quark and antiquark production cross sections in the  $t$  channel and their ratio in proton-proton collisions at  $\sqrt{s} = 13$  TeV, arXiv:1812.10514 [INSPIRE].  
[29] CMS collaboration, Measurement of differential cross sections and charge ratios for  $t$ -channel single top quark production at 13 TeV, CMS-PAS-TOP-17-023.  
[30] B.W. Harris, E. Laenen, L. Phaf, Z. Sullivan and S. Weinzierl, The Fully Differential Single Top Quark Cross-Section in Next to Leading Order QCD, Phys. Rev. D 66 (2002) 054024 [hep-ph/0207055] [INSPIRE].  
[31] J.M. Campbell, R.K. Ellis and F. Tramontano, *Single top production and decay at next-to-leading order*, Phys. Rev. D **70** (2004) 094012 [hep-ph/0408158] [INSPIRE].  
[32] Q.-H. Cao, R. Schwienhorst, J.A. Benitez, R. Brock and C.P. Yuan, Next-to-leading order corrections to single top quark production and decay at the Tevatron: 2.  $t^{-}$  channel process, Phys. Rev. D 72 (2005) 094027 [hep-ph/0504230] [INSPIRE].  
[33] S. Mölbitz, L.D. Ninh and P. Uwer, Next-to-leading order QCD corrections for single top-quark production in association with two jets, arXiv:1906.05555 [INSPIRE].  
[34] J.M. Campbell, R. Frederix, F. Maltoni and F. Tramontano, Next-to-Leading-Order Predictions for t-Channel Single-Top Production at Hadron Colliders, Phys. Rev. Lett. 102 (2009) 182003 [arXiv:0903.0005] [INSPIRE].  
[35] J.M. Campbell, R. Frederix, F. Maltoni and F. Tramontano, NLO predictions for t-channel production of single top and fourth generation quarks at hadron colliders, JHEP 10 (2009) 042 [arXiv:0907.3933] [INSPIRE].  
[36] J.M. Campbell and R.K. Ellis, Top-Quark Processes at NLO in Production and Decay, J. Phys. G 42 (2015) 015005 [arXiv:1204.1513] [INSPIRE].  
[37] M. Brucherseifer, F. Caola and K. Melnikov, On the NNLO QCD corrections to single-top production at the LHC, Phys. Lett. B 736 (2014) 58 [arXiv:1404.7116] [INSPIRE].  
[38] E.L. Berger, J. Gao, C.P. Yuan and H.X. Zhu, NNLO QCD Corrections to t-channel Single Top-Quark Production and Decay, Phys. Rev. D 94 (2016) 071501 [arXiv:1606.08463] [INSPIRE].  
[39] E.L. Berger, J. Gao and H.X. Zhu, Differential Distributions for t-channel Single Top-Quark Production and Decay at Next-to-Next-to-Leading Order in QCD, JHEP 11 (2017) 158 [arXiv:1708.09405] [INSPIRE].

[40] M. Beccaria et al., A Complete one-loop calculation of electroweak supersymmetric effects in t-channel single top production at CERN LHC, Phys. Rev. D 77 (2008) 113018 [arXiv:0802.1994] [INSPIRE].  
[41] D. Bardin, S. Bondarenko, L. Kalinovskaya, V. Kolesnikov and W. von Schlippe, Electroweak Radiative Corrections to Single-top Production, Eur. Phys. J. C 71 (2011) 1533 [arXiv:1008.1859] [INSPIRE].  
[42] R. Frederix, S. Frixione, V. Hirschi, D. Pagani, H.S. Shao and M. Zaro, The automation of next-to-leading order electroweak calculations, JHEP 07 (2018) 185 [arXiv:1804.10017] [INSPIRE].  
[43] P. Falgari, P. Mellor and A. Signer, Production-decay interferences at NLO in QCD for t-channel single-top production, Phys. Rev. D 82 (2010) 054028 [arXiv:1007.0893] [INSPIRE].  
[44] P. Falgari, F. Giannuzzi, P. Mellor and A. Signer, Off-shell effects for t-channel and s-channel single-top production at NLO in QCD, Phys. Rev. D 83 (2011) 094013 [arXiv:1102.5267] [INSPIRE].  
[45] A.S. Papanastasiou, R. Frederix, S. Frixione, V. Hirschi and F. Maltoni, Single-top t-channel production with off-shell and non-resonant effects, Phys. Lett. B 726 (2013) 223 [arXiv:1305.7088] [INSPIRE].  
[46] J. Wang, C.S. Li, H.X. Zhu and J.J. Zhang, Factorization and resummation of t-channel single top quark production, arXiv:1010.4509 [INSPIRE].  
[47] N. Kidonakis, Next-to-  $n e x t$ -to-leading-order collinear and soft gluon corrections for  $t$ -channel single top quark production, Phys. Rev. D 83 (2011) 091503 [arXiv:1103.2792] [INSPIRE].  
[48] Q.-H. Cao, P. Sun, B. Yan, C.P. Yuan and F. Yuan, Transverse Momentum Resummation for t-channel single top quark production at the LHC, Phys. Rev. D 98 (2018) 054032 [arXiv:1801.09656] [INSPIRE].  
[49] S. Frixione, E. Laenen, P. Motylinski and B.R. Webber, Single-top production in MC@NLO, JHEP 03 (2006) 092 [hep-ph/0512250] [INSPIRE].  
[50] S. Frixione, E. Laenen, P. Motylinski, B.R. Webber and C.D. White, *Single-top hadroproduction in association with a W boson*, JHEP 07 (2008) 029 [arXiv:0805.3067] [INSPIRE].  
[51] R. Frederix, E. Re and P. Torrielli, Single-top t-channel hadroproduction in the four-flavour scheme with POWHEG and aMC@NLO, JHEP 09 (2012) 130 [arXiv:1207.5391] [INSPIRE].  
[52] R. Frederix, S. Frixione, A.S. Papanastasiou, S. Prestel and P. Torrielli, Off-shell single-top production at NLO matched to parton showers, JHEP 06 (2016) 027 [arXiv:1603.01178] [INSPIRE].  
[53] E. Bothmann, F. Krauss and M. Schönherr, *Single top-quark production with SHERPA*, Eur. Phys. J. C **78** (2018) 220 [arXiv:1711.02568] [INSPIRE].  
[54] S. Alioli, P. Nason, C. Oleari and E. Re, NLO single-top production matched with shower in POWHEG: s- and t-channel contributions, JHEP 09 (2009) 111 [Erratum ibid. 02 (2010) 011] [arXiv:0907.4076] [INSPIRE].  
[55] T. Jezo and P. Nason, On the Treatment of Resonances in Next-to-Leading Order Calculations Matched to a Parton Shower, JHEP 12 (2015) 065 [arXiv:1509.09071] [INSPIRE].

[56] S. Carrazza, R. Frederix, K. Hamilton and G. Zanderighi, MINLO t-channel single-top plus jet, JHEP 09 (2018) 108 [arXiv:1805.09855] [INSPIRE].  
[57] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[58] S. Frixione, Z. Kunszt and A. Signer, Three jet cross-sections to next-to-leading order, Nucl. Phys. B 467 (1996) 399 [hep-ph/9512328] [INSPIRE].  
[59] S. Frixione, A General approach to jet cross-sections in QCD, Nucl. Phys. B 507 (1997) 295 [hep-ph/9706545] [INSPIRE].  
[60] R. Frederix, S. Frixione, F. Maltoni and T. Stelzer, Automation of next-to-leading order computations in QCD: The FKS subtraction, JHEP 10 (2009) 003 [arXiv:0908.4272] [INSPIRE].  
[61] G. Ossola, C.G. Papadopoulos and R. Pittau, Reducing full one-loop amplitudes to scalar integrals at the integrand level, Nucl. Phys. B 763 (2007) 147 [hep-ph/0609007] [INSPIRE].  
[62] P. Mastrolia, E. Mirabella and T. Peraro, Integrand reduction of one-loop scattering amplitudes through Laurent series expansion, JHEP 06 (2012) 095 [Erratum ibid. 11 (2012) 128] [arXiv:1203.0291] [INSPIRE].  
[63] G. Passarino and M.J.G. Veltman, One Loop Corrections for  $e^{+}e^{-}$  Annihilation Into  $\mu^{+}\mu^{-}$  in the Weinberg Model, Nucl. Phys. B 160 (1979) 151 [INSPIRE].  
[64] A.I. Davydychev, A Simple formula for reducing Feynman diagrams to scalar integrals, Phys. Lett. B 263 (1991) 107 [INSPIRE].  
[65] A. Denner and S. Dittmaier, Reduction schemes for one-loop tensor integrals, Nucl. Phys. B 734 (2006) 62 [hep-ph/0509141] [INSPIRE].  
[66] V. Hirschi, R. Frederix, S. Frixione, M.V. Garzelli, F. Maltoni and R. Pittau, Automation of one-loop QCD corrections, JHEP 05 (2011) 044 [arXiv:1103.0621] [INSPIRE].  
[67] G. Ossola, C.G. Papadopoulos and R. Pittau, CutTools: A Program implementing the OPP reduction method to compute one-loop amplitudes, JHEP 03 (2008) 042 [arXiv:0711.3596] [INSPIRE].  
[68] T. Peraro, *Ninja: Automated Integrand Reduction via Laurent Expansion for One-Loop Amplitudes*, Comput. Phys. Commun. **185** (2014) 2771 [arXiv:1403.1229] [INSPIRE].  
[69] V. Hirschi and T. Peraro, Tensor integrand reduction via Laurent expansion, JHEP 06 (2016) 060 [arXiv:1604.01363] [INSPIRE].  
[70] A. Denner, S. Dittmaier and L. Hofer, Collier: a fortran-based Complex One-Loop LLibrary in Extended Regularizations, Comput. Phys. Commun. 212 (2017) 220 [arXiv:1604.06792] [INSPIRE].  
[71] F. Cascioli, P. Maierhofer and S. Pozzorini, Scattering Amplitudes with Open Loops, Phys. Rev. Lett. 108 (2012) 111601 [arXiv:1111.5206] [INSPIRE].  
[72] S. Frixione, V. Hirschi, D. Pagani, H.S. Shao and M. Zaro, Weak corrections to Higgs hadroproduction in association with a top-quark pair, JHEP 09 (2014) 065 [arXiv:1407.0823] [INSPIRE].  
[73] S. Frixione, V. Hirschi, D. Pagani, H.S. Shao and M. Zaro, Electroweak and QCD corrections to top-pair hadroproduction in association with heavy bosons, JHEP 06 (2015) 184 [arXiv:1504.03446] [INSPIRE].

[74] D. Pagani, I. Tsinikos and M. Zaro, The impact of the photon PDF and electroweak corrections on  $t\bar{t}$  distributions, Eur. Phys. J. C 76 (2016) 479 [arXiv:1606.01915] [INSPIRE].  
[75] R. Frederix, S. Frixione, V. Hirschi, D. Pagani, H.-S. Shao and M. Zaro, The complete NLO corrections to dijet hadroproduction, JHEP 04 (2017) 076 [arXiv:1612.06548] [INSPIRE].  
[76] M. Czakon, D. Heymes, A. Mitov, D. Pagani, I. Tsinikos and M. Zaro, Top-pair production at the LHC through NNLO QCD and NLO EW, JHEP 10 (2017) 186 [arXiv:1705.04105] [INSPIRE].  
[77] R. Frederix, D. Pagani and M. Zaro, Large NLO corrections in  $t\bar{t}W^{\pm}$  and  $t\bar{t}t\bar{t}$  had reproduction from supposedly subleading EW contributions, JHEP 02 (2018) 031 [arXiv:1711.02116] [INSPIRE].  
[78] A. Broggio, A. Ferroglia, R. Frederix, D. Pagani, B.D. Pecjak and I. Tsinikos, Top-quark pair hadroproduction in association with a heavy boson at NLO+NNLL including EW corrections, JHEP 08 (2019) 039 [arXiv:1907.04343] [INSPIRE].  
[79] V. Bertone, S. Carrazza, D. Pagani and M. Zaro, On the Impact of Lepton PDFs, JHEP 11 (2015) 194 [arXiv:1508.07002] [INSPIRE].  
[80] A. Manohar, P. Nason, G.P. Salam and G. Zanderighi, How bright is the proton? A precise determination of the photon parton distribution function, Phys. Rev. Lett. 117 (2016) 242002 [arXiv:1607.04266] [INSPIRE].  
[81] A.V. Manohar, P. Nason, G.P. Salam and G. Zanderighi, The Photon Content of the Proton, JHEP 12 (2017) 046 [arXiv:1708.01256] [INSPIRE].  
[82] L. Barze, G. Montagna, P. Nason, O. Nicrosini and F. Piccinini, Implementation of electroweak corrections in the POWHEG BOX: single W production, JHEP 04 (2012) 037 [arXiv:1202.0465] [INSPIRE].  
[83] L. Barze, G. Montagna, P. Nason, O. Nicosini, F. Piccinini and A. Vicini, Neutral current Drell-Yan with combined QCD and electroweak corrections in the POWHEG BOX, Eur. Phys. J. C 73 (2013) 2474 [arXiv:1302.4606] [INSPIRE].  
[84] F. Granata, J.M. Lindert, C. Oleari and S. Pozzorini, NLO QCD+EW predictions for HV and HV +jet production including parton-shower effects, JHEP 09 (2017) 012 [arXiv:1706.03522] [INSPIRE].  
[85] M. Chiesa, A. Denner, J.-N. Lang and M. Pellen, An event generator for same-sign W-boson scattering at the LHC including electroweak corrections, arXiv:1906.01863 [INSPIRE].  
[86] S. Kallweit, J.M. Lindert, P. Maierhofer, S. Pozzorini and M. Schönherr, NLO QCD+EW predictions for  $V +$  jets including off-shell vector-boson decays and multijet merging, JHEP 04 (2016) 021 [arXiv:1511.08692] [INSPIRE].  
[87] C. Gütschow, J.M. Lindert and M. Schönherr, Multi-jet merged top-pair production including electroweak corrections, Eur. Phys. J. C 78 (2018) 317 [arXiv:1803.00950] [INSPIRE].  
[88] S. Frixione and B.R. Webber, Matching NLO QCD computations and parton shower simulations, JHEP 06 (2002) 029 [hep-ph/0204244] [INSPIRE].  
[89] S. Frixione, P. Nason and C. Oleari, Matching NLO QCD computations with Parton Shower simulations: the POWHEG method, JHEP 11 (2007) 070 [arXiv:0709.2092] [INSPIRE].  
[90] CMS collaboration, Cross section measurement of t-channel single top quark production in pp collisions at  $\sqrt{s} = 13$  TeV, Phys. Lett. B 772 (2017) 752 [arXiv:1610.00678] [INSPIRE].

[91] S. Frixione, E. Laenen, P. Motylinski and B.R. Webber, Angular correlations of lepton pairs from vector boson and top quark decays in Monte Carlo simulations, JHEP 04 (2007) 081 [hep-ph/0702198] [INSPIRE].  
[92] A. Denner and M. Pellen, Off-shell production of top-antitop pairs in the lepton+jets channel at NLO QCD, JHEP 02 (2018) 013 [arXiv:1711.10359] [INSPIRE].