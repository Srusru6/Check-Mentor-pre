# Off-shell single-top-quark production in the Standard Model Effective Field Theory

Tobias Neumann $^{a,b}$  and Zack Sullivan $^{a}$

$^{a}$ Department of Physics, Illinois Institute of Technology, 3101 S. Dearborn St., Chicago, IL 60616, U.S.A.  
${}^{b}$  Fermilab,

P.O. Box 500, Batavia, IL 60510, U.S.A.

E-mail: tneumann@fnal.gov, zack.sullivan@iit.edu

ABSTRACT: We present a fully differential and spin-dependent  $t$ -channel single-top-quark calculation at next-to-leading order (NLO) in QCD including off-shell effects by using the complex mass scheme in the Standard Model (SM) and in the Standard Model Effective Field Theory (SMEFT). We include all relevant SMEFT operators at  $1 / \Lambda^2$  that contribute at NLO in QCD for a fully consistent comparison to the SM at NLO. In addition, we include chirality flipping operators that do not interfere with the SM amplitude and contribute only at  $1 / \Lambda^4$  with a massless  $b$ -quark. Such higher order effects are usually captured by considering anomalous right-handed Wtb and left-handed Wtb tensor couplings. Despite their formal suppression in the SMEFT, they describe an important class of models for new physics. Our calculation and analysis framework is publicly available in MCFM.

KEYWORDS: QCD Phenomenology, NLO Computations

ARXIV EPRINT: 1903.11023

# Contents

1 Introduction 1  
2 Setup and calculation 5

2.1 Technical implementation and checks 9  
2.2 Implementation in MCFM-8.3 13

3 Phenomenology 14

3.1 Off-shell and  $W$  reconstruction effects in the Standard Model 15  
3.2 Angular observables in the top-quark rest frame 17  
3.3 SMEFT contributions 20

4 Conclusions 25  
A Additional figures 27

# 1 Introduction

Large statistics data samples from experiments at the CERN Large Hadron Collider (LHC) provide the opportunity to extract precision information about the Standard Model (SM), and to look for small deviations due to new physics that enters at energy scales beyond direct experimental reach.  $t$ -channel single-top-quark production provides a unique window onto this physics, and has been well-measured by both the ATLAS [1-4] and CMS [5-8] Collaborations at the  $\sqrt{S} = 7,8$  and  $13\mathrm{TeV}$  runs. While the Collaborations refine these measurements to extract limits on phenomenologically motivated physics beyond the Standard Model (BSM) [9-13], the theoretical models they use for comparison are not generally as precise as the data they are fitting. This paper describes next-to-leading order (NLO) QCD calculations of  $t$ -channel single-top-quark production including off-shell effects that improve both the SM and Standard Model Effective Field Theory (SMEFT) predictions of fully differential and spin-dependent observables.

$t$ -channel single-top-quark production probes many aspects of the SM. Measurement of the cross section provides direct access to the square of the CKM matrix element  $V_{tb}$  [14, 15]. The  $V - A$  nature of the production and decay vertices are probed by spin correlations [16, 17]. Kinematic distributions, such as the lineshape of the  $b$ -lepton invariant mass  $m_{bl}$  from the top quark decay products, allow for extraction of the top quark mass at the LHC [8, 18].

This process is also a stringent test on the consistency of parton distribution function (PDF) fits at different orders, and it directly tests the analytic framework of improved perturbation theory. Resummation of large logarithms of the top quark mass to the bottom

quark mass leads directly to the introduction a  $b$ -quark PDFs [14]. Through NLO in QCD the process becomes one of double deep inelastic scattering (DDIS) with two independent scales, where the leading order (LO) process is  $qb \rightarrow q't$  scattering [14]. Because DIS data is used to extract the PDFs, when DDIS scale choices are made, the inclusive  $t$ -channel cross sections computed at different perturbative orders should be approximately the same. A primary motivation for improving the SM calculation is that this analytic constraint is strongly violated by recent PDF sets [19]. Once this issue is resolved, this process could provide insight into PDF transverse momentum dependence [20].

While improving our understanding of SM physics, precision calculations of single-top-quark production and decay establish a baseline for controlling the backgrounds to BSM physics. The final state of the  $t$ -channel process is  $W + b + \mathrm{light}$  jets, where the  $W$  can decay to a lepton plus missing energy, and hence is a background to most new physics models. Deviations in inclusive cross sections or kinematic distributions are expected in a large class of BSM physics [21]. The spin correlations are especially sensitive to new physics [22], and a number of observables have been developed in refs. [23-26] that are separately sensitive to new physics contributions in the production and decay vertices of the top-quark, respectively.

In the rest of this section we briefly review the state of SM  $t$ -channel single-top-quark calculations, explain our focus on the SMEFT as an extension of the SM, and summarize what we add to the SMEFT calculations. In section 2 we describe our setup and the calculation. We specify the list of SMEFT operators that we use, as well as our conventions and normalizations. Furthermore, we describe the steps that we perform to compute and simplify the amplitudes and provide a list of checks that we have performed. A primary goal of this study is to allow for a direct improvement of experimental analyses, and we describe our publicly available implementation in MCFM and how to use it. In section 3 we study off-shell and  $W$ -boson/neutrino reconstruction effects in the SM. We define angular observables in the top-quark rest frame that are sensitive to SMEFT contributions. We then study the impact of off-shell effects to these distributions, and the effect of higher order contributions from QCD and stability of the SMEFT.

Towards precise  $t$ -channel single-top-quark predictions. The precision of single-top-quark calculations has largely coincided with the attempts to discover, and later precisely measure, the  $t$ -channel cross section. Early results focused on the inclusive NLO cross section with stable on-shell top quarks [14, 27, 28]. Once experimental backgrounds were better understood, differential calculations were performed [29-31] with a stable top quark, and the results were used to improve LO kinematics in showering Monte Carlo programs.

The next step consisted of including the leptonic decay for an on-shell top quark, preserving full spin correlations, and including separate NLO corrections in production and decay [32-34]. The on-shell approximation relies on the assumption that off-shell effects are expected to be small of the order  $\Gamma_t / m_t$  inclusively, where  $\Gamma_t$  is the top-quark decay width, and  $m_t$  is its mass. This allows for a significant simplification of the analytical expressions at the cost of little error for the inclusive observables used in discovery.

Since the production of the top-quark proceeds through a  $b$ -quark, one can distinguish between calculations that either assume an intrinsic proton  $b$ -quark content (five-flavor scheme), or not (four-flavor scheme). In the latter case, and with a non-zero  $b$ -quark mass, predictions were first calculated in the stable top-quark approximation at NLO [35, 36], and then with a decaying on-shell top quark, retaining spin correlations [37]. This is implemented in MCFM [38]. To this point, all calculations were performed in the on-shell approximation.

Off-shell effects generally play a role when one considers differential distributions. A prime example is the top-quark invariant mass distribution, where the region above the resonance is severely underpopulated in the on-shell approximation. It only receives a tiny contribution when QCD radiation before the top-quark's decay is clustered with the final state  $b$ -jet. The inclusion of off-shell effects was handled for example in an effective field theory approach [39-42], which is valid only close to the resonance. The first gauge invariant calculation valid also in the far off-shell region was performed [43, 44] in the complex mass scheme [45-48], and this is the approach we follow.

Other calculations include an attempt to improve on fixed order matching by adding parton shower effects through implementations in MC@NLO for on-shell and off-shell single top production [44, 49] and in POWHEG-BOX for on-shell production [50]. Analytical resummation has also been performed on top of the on-shell approximated fixed order result [51-57]. Finally, in recent years results at NNLO in QCD have been published for stable on-shell and for decaying top-quarks [58-61], but these numerical results currently differ by the size of their NNLO correction terms.

The primary goal of this study is to provide a public implementation in MCFM of a fully differential spin-dependent prediction for  $t$ -channel single-top-quark production and semi-leptonic decay at NLO including the off-shell effects of initial-final state QCD interference and of non-resonant interferences. We demonstrate in section 3 that, after cuts, off-shell effects produce significant shifts in some key experimental observables. Additionally, we identify kinematic regions and spin observables that are highly sensitive to the cancellation of soft radiation in production and decay. We show that this sensitivity can be hidden by the on-shell approximation, and thus such regions should be avoided in analyses relying on fixed order predictions.

New physics in single-top-quark production and decay. Deviations from the SM are frequently modeled using anomalous couplings (see for example refs. [62-67]) because they often map directly to experimental observables. Most recent studies of BSM physics in the single-top-quark sector by ATLAS [12, 13] and CMS [9-11] use this approach. For a recent single-top-quark overview focusing on measurements of anomalous contributions we refer the reader to ref. [68]. Without a UV completion, however, it can be difficult to systematically incorporate and renormalize higher order perturbative corrections. It can also be challenging to compare limits obtained in one experimental data set with limits obtained from other experiments or data sets since there is neither a systematic power counting scheme, nor a definite basis of the modifying structures [69] (see also the discussion in ref. [70]).

In this paper we take a more systematic approach and parameterize potentially small deviations in terms of an effective field theory (EFT) that obeys well-established SM symmetries. A classification of all relevant dimension six operators has been developed in refs. [71, 72], and goes under the name Standard Model Effective Field Theory (SMEFT), see also [69]. Calculations in the EFT and SMEFT have been performed in abundance at LO, and we can only cite an excerpt of results, see for example refs. [63, 73-81]. Within the EFT framework, limits obtained on operators can be compared directly with limits obtained from  $B$ -meson decays [82, 83], for example.

To consistently include NLO effects one needs to determine the renormalization and anomalous dimension matrix of the SMEFT operators. This framework has been fully developed in a series of publications [84-86]. See also ref. [87] for a working group report regarding the importance of NLO corrections of the SMEFT. Studies including NLO QCD effects for an on-shell top quark have been performed over the years [88-91], and recently also for an off-shell top quark [92], but with a limited set of operators.

The most complete treatment of the SMEFT in single-top-quark calculations so far has been in ref. [92]. The authors consider a limited set of three operators contributing as interference to the SM at LO in QCD, but neglect the operators that begin contributing at NLO in QCD and operators that do not interfere with the SM. Their calculation is also performed in the complex mass scheme, and includes the effect of parton showers. They study different approximations for top-quark decay in the MadGraph5 framework using MadSpin. To estimate uncertainties they consider additional effects at  $\mathcal{O}(1 / \Lambda^4)$  that come from squared  $1 / \Lambda^2$  contributions and from double operator insertions.

We consider six operators that contribute at NLO in QCD at  $1 / \Lambda^2$  at the amplitude level that are relevant for  $t$ -channel production and decay. In addition, we consider a limited set of two color singlet four-fermion operators with the helicity structure  $(\bar{L} L)(\bar{L} L)$  and  $(\bar{R} R)(\bar{R} R)$  that are relevant for matching to  $W'$  analyses. We ignore the corresponding color-octet operators, and  $(\bar{L} L)(\bar{R} R)$ ,  $(\bar{L} R)(\bar{L} R)$ , and  $(\bar{L} R)(\bar{R} L)$  operators which each have color singlet and octet contributions. We also ignore four-fermion operators involving the neutrino and positron. In practice these later operators would only be relevant for  $s$ -channel experimental measurements.

Depending on whether the SMEFT amplitudes interfere with the SM, one obtains effects of order  $1 / \Lambda^2$  or  $1 / \Lambda^4$  at the cross-section level, respectively. We do not include effects of  $1 / \Lambda^4$  at the amplitude level since these would require a classification of dimension eight operators for a consistent renormalization at NLO. Our  $1 / \Lambda^4$  effects at the cross-section level thus come from "squared" amplitudes of order  $1 / \Lambda^2$  and constitute only partial effects in view of missing double insertions and dimension eight operators.

The partial higher order effects we include firstly allow estimating higher order effects for those operators that already enter at  $1 / \Lambda^2$  as an interference with the SM. Secondly, they allow for a quantification of those operators' effects that only enter as "squared" contributions. These are usually neglected in EFT studies, but would be present in the anomalous couplings picture. They can be relevant as higher order effects to the  $1 / \Lambda^2$  contributions, or under certain model assumptions on the operator content.

In our study we consider a set of eight operators and all of them are treated fully consistently at NLO in QCD. Four of them contribute at  $1 / \Lambda^2$  at the cross-section level, and four of them only enter at  $1 / \Lambda^4$ . Two of the newly considered operators here only begin to enter at NLO through gluon radiation and are required for a consistent NLO evaluation since they mix under renormalization. Note that while the  $1 / \Lambda^4$  contributions are partial in the SMEFT expansion, they are still computed consistently at NLO in QCD. All contributions are implemented including off-shell top quark effects in the complex mass scheme with a massless  $b$ -quark in the five-flavor scheme. We do not include all-order effects of parton shower or resummation.

In section 2 we describe the full set of operators, their relationship to anomalous couplings studies, and technical details of our calculation. We show in section 3 that some commonly recommended spin-correlation observables [23-26] that are sensitive to these operators are relatively stable to off-shell effects and QCD radiation, while others are highly sensitive to soft radiation effects that are not apparent in the on-shell calculations.

# 2 Setup and calculation

The calculations in this study are performed in the SM and in the SMEFT framework. The SMEFT is constructed by building higher dimensional operators that respect SM symmetries out of SM fields. It systematically extends the SM Lagrangian as a power series in  $1 / \Lambda$ , where  $\Lambda$  is the scale of new physics where the EFT description breaks down.

$$
\mathcal {L} _ {\text {S M E F T}} = \sum_ {i} \frac {C _ {i}}{\Lambda^ {2}} Q _ {i} + \text {H . c .}, \tag {2.1}
$$

where  $\mathcal{Q}_i$  denote dimension six operators, we add Hermitian conjugates (H.c.) for non-Hermitian operators with complex Wilson coefficients  $C_i$ , and we add Hermitian operators (without H.c.) with real Wilson coefficients  $C_i$ .

The SMEFT picture we consider in this paper contrasts with the phenomenological approach of anomalous couplings, which modify the  $Wtb$  vertex as follows:

$$
- \frac {g _ {W}}{\sqrt {2}} \bar {b} \gamma^ {\mu} \left(V _ {L} P _ {L} + V _ {R} P _ {R}\right) t W _ {\mu} ^ {-} - \frac {g _ {W}}{\sqrt {2}} \bar {b} \frac {i \sigma^ {\mu \nu} q _ {\nu}}{m _ {W}} \left(g _ {L} P _ {L} + g _ {R} P _ {R}\right) t W _ {\mu} ^ {-} + \text {H . c .}, \tag {2.2}
$$

where in the SM  $V_{L} = V_{tb}^{*}$ ,  $V_{R} = g_{L} = g_{R} = 0$ , and the  $W$ -boson momentum  $q$  is chosen to be incoming. The pictures are connected at tree level, where the anomalous couplings vertices are generated by SMEFT operators and can be directly mapped to them [63, 64]. The relations between the anomalous couplings and our operator Wilson coefficients (defined further below) are

$$
\delta V _ {L} = \mathcal {C} _ {\varphi q} ^ {(3. 3 3)} \frac {m _ {t} ^ {2}}{\Lambda^ {2}}, \text {w h e r e} V _ {L} = 1 + \delta V _ {L}, \tag {2.3}
$$

$$
V _ {R} = \mathcal {C} _ {\varphi u d} ^ {3 3} * \frac {m _ {t} ^ {2}}{\Lambda^ {2}}, \tag {2.4}
$$

$$
g _ {L} = - 4 \frac {m _ {W} m _ {t}}{\Lambda^ {2}} \cdot \mathcal {C} _ {d W} ^ {3 3}, \tag {2.5}
$$

$$
g _ {R} = - 4 \frac {m _ {W} m _ {t}}{\Lambda^ {2}} \cdot \mathcal {C} _ {u W} ^ {3 3} ^ {*}, \tag {2.6}
$$

where  $m_W$  is the  $W$ -boson mass, and  $m_W = \frac{1}{2} g_W v$  has been used to derive this equivalence. Note that the minus sign for  $g_L$  and  $g_R$  is different from the literature. It depends on the choice of treating the momentum  $q_\nu$  in eq. (2.2) as incoming or outgoing and the sign convention in the covariant derivative. We treat all momenta as incoming in this study and adopt the sign convention from the SMEFT literature (see further below).

When considering the leading  $1 / \Lambda^2$  contributions from dimension six operators to single top observables, only  $V_{L}$  and  $g_{R}$  contribute as interference to the SM amplitude. The contributions generated by  $V_{R}$  and  $g_{L}$  flip a  $b$ -quark chirality and do not interfere with the SM amplitude for a massless  $b$ -quark. As such, in the SMEFT they only enter at order  $1 / \Lambda^4$  as "squared" contributions from non-SM helicity amplitudes. Operator double insertions would contribute to the amplitudes at the same order, where renormalization requires the inclusion of dimension eight operators and a determination of their anomalous dimension matrix. Dimension eight operators are beyond the scope of this study, and so we do not include them or any double insertions.

While formally suppressed in SMEFT, the couplings  $V_{R}$  and  $g_{L}$  are relevant for the study of new charged vector currents ( $W'$  bosons) or scalars ( $H^{\pm}$  bosons) [93-95] and are strongly constrained experimentally despite their suppression. This is possible due to the strong spin correlations in single-top-quark production, and a large set of observables highly sensitive to SM deviations.

To maintain a direct coupling to experiment, we follow a hybrid approach. In the first part we include all dimension six SMEFT operators that are relevant at NLO in QCD, and enter at order  $1 / \Lambda^2$  at the cross-section level. This allows for a fully consistent evaluation of SMEFT effects and comparison of Wilson coefficients extracted from different experiments when higher order effects can be neglected.

In an enhanced mode we include all contributions of order  $1 / \Lambda^2$  in the amplitudes from dimension six operators of the SMEFT. The additional operator contributions do not interfere with the SM and contribute only as the operator insertions squared, or in interference with other SMEFT contributions. This leads to  $1 / \Lambda^4$  effects at the cross-section level. This enhancement serves two purposes. It allows for a NLO QCD mapping to anomalous coupling studies under the assumption that dimension eight operators can be ignored. And it allows for a systematic determination of whether a given observable is sensitive to higher-order corrections in the EFT. If one wishes to obtain consistent limits on Wilson coefficients and compare them with other sources, one should not be sensitive to  $1 / \Lambda^2$  and  $1 / \Lambda^4$  contributions at the same time. For that purpose one can run the analysis using only the  $1 / \Lambda^2$  contributions and then compare with results obtained when including the partial  $1 / \Lambda^4$  contributions.

SMEFT operators. As shown in eq. (2.1), all operators  $\mathcal{Q}$  come with a Wilson coefficient  $C$  and a power of  $1 / \Lambda^2$ . The operators that contribute at  $1 / \Lambda^2$  in NLO QCD as interference to the SM amplitude are

$$
\mathcal {Q} _ {\varphi q} ^ {(3, 3 3)} = \frac {1}{2} y _ {t} ^ {2} \left(\varphi^ {\dagger} i D _ {\mu} ^ {I} \varphi\right) \left(\bar {Q} _ {L} \gamma^ {\mu} \tau^ {I} Q _ {L}\right), \tag {2.7}
$$

$$
\mathcal {Q} _ {u W} ^ {3 3} = y _ {t} g _ {W} (\bar {Q} _ {L} \sigma^ {\mu \nu} \tau^ {I} t) \tilde {\varphi} W _ {\mu \nu} ^ {I}, \tag {2.8}
$$

$$
\mathcal {Q} _ {u G} ^ {3 3} = y _ {t} g _ {s} \left(\bar {Q} _ {L} \sigma^ {\mu \nu} T ^ {A} t\right) \tilde {\varphi} G _ {\mu \nu} ^ {A}, \tag {2.9}
$$

$$
\mathcal {Q} _ {4 L} = \mathcal {Q} _ {q q} ^ {(3, 1 1 3 3)} = (\bar {q} _ {L} \gamma_ {\mu} \tau^ {I} q _ {L}) (\bar {Q} _ {L} \gamma^ {\mu} \tau^ {I} Q _ {L}), \tag {2.10}
$$

where  $Q_{L}$  is the third generation left handed SU(2) doublet  $(t_{L}, b_{L})$  and  $q_{L}$  the first generation doublet  $(u_{L}, d_{L})$ . Here  $y_{t} = m_{t}\sqrt{2}/v$  is the real-valued top-quark Yukawa coupling,  $g_{W}$  is the electroweak coupling, and  $g_{s}$  is the strong coupling. The operators  $\mathcal{Q}_{\varphi q}^{(3,33)}$  and  $\mathcal{Q}_{4L}$  are Hermitian, have real Wilson coefficients, and no Hermitian conjugate is added to the sum in eq. (2.1). We also add the second generation operator  $\mathcal{Q}_{qq}^{(3,2233)}$  with the same real Wilson coefficient. The operator  $\mathcal{Q}_{uG}^{33}$  modifies the  $\bar{t}tg$  Feynman rule vertex and enters only at NLO in QCD.

Our notation, sign conventions, and operator basis follows that of the SMEFT literature in refs. [72, 84-86]. This sign convention is different from the one used in other  $t$ -channel single-top-quark SMEFT studies [73, 74, 88, 90, 92]. Both conventions exist in FeynRules model files [96]. We use a plus sign for minimal coupling in the covariant derivative  $D_{\mu} = \partial_{\mu} + igX_{\mu}$  for gauge fields  $X$  and a corresponding minus sign in the gauge field strength tensor  $X_{\mu \nu} = \partial_{\mu}X_{\mu} + \partial_{\nu}X_{\mu} - gX_{\mu}X_{\nu}$  consistent with SMEFTsim package [97], whereas the dim6top package [81] uses the opposite convention.

At  $1 / \Lambda^4$  there are additional dimension six operators

$$
\mathcal {Q} _ {\varphi u d} ^ {3 3} = y _ {t} ^ {2} \left(\tilde {\varphi} ^ {\dagger} i D _ {\mu} \varphi\right) \left(\bar {t} \gamma^ {\mu} b\right), \tag {2.11}
$$

$$
\mathcal {Q} _ {d W} ^ {3 3} = y _ {t} g _ {W} \left(\bar {Q} _ {L} \sigma^ {\mu \nu} \tau^ {I} b\right) \Phi W _ {\mu \nu} ^ {I}, \tag {2.12}
$$

$$
\mathcal {Q} _ {d G} ^ {3 3} = y _ {T} g _ {s} \left(\bar {Q} _ {L} \sigma^ {\mu \nu} T ^ {A} b\right) \Phi G _ {\mu} ^ {A} \nu , \tag {2.13}
$$

$$
\mathcal {Q} _ {4 R} = \mathcal {Q} _ {u d} ^ {(1, 1 3 3 1)} + \mathcal {Q} _ {u d} ^ {(1, 3 1 1 3)} = (\bar {d} \gamma_ {\mu} u) (\bar {t} \gamma^ {\mu} b) + (\bar {u} \gamma_ {\mu} d) (\bar {b} \gamma^ {\mu} t), \tag {2.14}
$$

where the third operator  $\mathcal{Q}_{dG}^{33}$  only contributes at NLO in QCD and modifies the  $\bar{bbg}$  vertex. For the Hermitian operator  $\mathcal{Q}_{4R}$  no Hermitian conjugate is added to the sum in eq. (2.1), and we also add the corresponding second generation operator with the same Wilson coefficient.

Operator mixing and running. The operator pair  $\mathcal{Q}_{uW}^{33}$ ,  $\mathcal{Q}_{uG}^{33}$  has nonzero anomalous dimension and mixes according to

$$
\mu_ {X} \frac {\mathrm {d}}{\mathrm {d} \mu_ {X}} \left( \begin{array}{c} \mathcal {Q} _ {u G} ^ {3 3} \\ \mathcal {Q} _ {u W} ^ {3 3} \end{array} \right) = \frac {\alpha_ {s}}{4 \pi} C _ {F} \left( \begin{array}{c c} 1 & 0 \\ 2 & 2 \end{array} \right) \left( \begin{array}{c} \mathcal {Q} _ {u G} ^ {3 3} \\ \mathcal {Q} _ {u W} ^ {3 3} \end{array} \right), \tag {2.15}
$$

where  $\mu_{X}$  is a renormalization scale that is independent of the QCD renormalization scale. The pair  $\mathcal{Q}_{dW}^{33},\mathcal{Q}_{dG}^{33}$  mixes analogously under renormalization [86].

We renormalize the Wilson coefficients in the  $\overline{\mathrm{MS}}$  scheme following  $C_i^{\mathrm{bare}} = Z_{ij}C_j(\mu)$  where

$$
Z _ {i j} = 1 + \frac {\alpha_ {s}}{4 \pi} \frac {\gamma_ {i j}}{2 \epsilon}.
$$

A factor of  $(4\pi)^{\epsilon} / \Gamma (1 - \epsilon)$  is absorbed into the definition of  $\alpha_{s}$  and from here on we define  $a_{s}\equiv \alpha_{s} / (4\pi)$ . We set the renormalization point of the Wilson coefficients to the same value as the QCD renormalization point, as both contributions are probed at the same scale. The effect of the running of  $C_i$  has been studied in refs. [88, 90] and can be used to evolve the Wilson coefficients to the scale  $\Lambda$  or to some lower scale for comparisons.

We renormalize the top-quark mass and wavefunction in the complex mass scheme with complex mass on-shell conditions. The SM renormalization constants receive additional contributions from  $\mathcal{Q}_{uG}^{33}$ . We confirm the SMEFT mass and wavefunction renormalization constants in ref. [88] by computing the top-quark 1PI self energy with complex mass on-shell renormalization conditions and find

$$
\mu_ {0} = \left(1 + a _ {s} \delta_ {m}\right) \mu_ {t}, \tag {2.16}
$$

$$
\delta_ {m} = \left(\frac {\mu^ {2}}{\mu_ {t} ^ {2}}\right) ^ {\epsilon} C _ {F} \left(- \frac {3}{\epsilon} - 4 + \Re \mathfrak {C} _ {u G} ^ {3 3} \frac {m _ {t} \mu_ {t}}{\Lambda^ {2}} C _ {F} \left(\frac {1 2}{\epsilon} + 4\right)\right), \tag {2.17}
$$

$$
Z _ {\Psi} = \left(1 + a _ {s} \delta Z _ {\Psi}\right), \tag {2.18}
$$

$$
\begin{array}{l} \delta Z _ {\Psi} = \left(\frac {\mu^ {2}}{\mu_ {t} ^ {2}}\right) ^ {\epsilon} C _ {F} \left(- \frac {3}{\epsilon} - 4 + \Re \mathfrak {C} _ {u G} ^ {3 3} \frac {m _ {t} \mu_ {t}}{\Lambda^ {2}} C _ {F} \left(\frac {6}{\epsilon} + 2\right) \right. \\ \left. + \Im \mathfrak {m} \mathcal {C} _ {u G} ^ {3 3} \frac {m _ {t} \mu_ {t}}{\Lambda^ {2}} C _ {F} i \gamma_ {5} \left(\frac {6}{\epsilon} + 2\right)\right). \tag {2.19} \\ \end{array}
$$

Here  $\mu_t^2 = m_t^2 - i\Gamma_t m_t$  is the squared complex top-quark mass. One power of  $m_t$  is part of the operator normalization and is kept real. Note that in ref. [88] the covariant derivative is defined with a different sign convention which flips the sign of the Wilson coefficient  $\mathcal{C}_{uG}^{33}$  relative to our results.

Special care has to be taken for  $\mathfrak{Im}\mathcal{C}_{uG}^{33}$ , which receives a wavefunction renormalization contribution proportional to  $\gamma_{5}$ . We obtain it by adding an additional counterterm to the top-quark 1PI self energy proportional to  $\gamma_{5}$  and demanding that the propagator keeps its tree-level form throughout higher orders. For the  $\gamma_{5}$  contribution this is analogous to the SM on-shell condition of having residue  $i$  for the renormalized propagator.

Note: because we are examining an off-shell top quark, the non-resonant diagrams include contributions from  $\bar{b} bA$  and  $\bar{b} bZ$  vertices, where  $A$  is the photon field. The corresponding SM Feynman rules receive contributions from  $\mathcal{Q}_{dW}^{33}$  in the SMEFT and renormalize the gluon contributions from  $\mathcal{Q}_{dG}^{33}$  at NLO. In this case also the operator  $\mathcal{Q}_{dB}^{33} = y_t g_B(\bar{Q}\sigma^{\mu \nu}b)\Phi B_{\mu \nu}$  must be included to renormalize  $\mathcal{Q}_{dG}^{33}$ . The anomalous dimension matrix follows the operator renormalization group running

$$
\mu_ {X} \frac {\mathrm {d}}{\mathrm {d} \mu_ {X}} \left( \begin{array}{c} \mathcal {O} _ {d G} ^ {3 3} \\ \mathcal {O} _ {d W} ^ {3 3} \\ \mathcal {O} _ {d B} ^ {3 3} \end{array} \right) = \frac {\alpha_ {s}}{4 \pi} C _ {F} \left( \begin{array}{c c c} 1 & 0 & 0 \\ 2 & 2 & 0 \\ - 2 / 3 & 0 & 2 \end{array} \right) \left( \begin{array}{c} \mathcal {O} _ {d G} ^ {3 3} \\ \mathcal {O} _ {d W} ^ {3 3} \\ \mathcal {O} _ {d B} ^ {3 3} \end{array} \right). \tag {2.20}
$$

![](images/720fb81972a20dc9407a0de56d129b693d58b452715eb5260ce35bfff5989692.jpg)  
(a) Resonant.

![](images/f4a0ae32a59488ced5c4eccf47544f74c8d2c6bf6c6e0b1dc0f3d2594095224f.jpg)  
Figure 1. Sample Feynman diagrams of resonant and non-resonant contributions at LO.  
(b) Non-resonant.

![](images/ce3c159cd416e953e38d62529a495641626a70476456fab40cd1b86c9330dc01.jpg)  
(c) Non-resonant.

We include this operator  $\mathcal{Q}_{dB}^{33}$  only for the renormalization of  $\mathcal{Q}_{dB}^{33}$  and set its Wilson coefficient to zero afterwards, since it only contributes to the non-resonant amplitudes.

# 2.1 Technical implementation and checks

We consider the process  $u(p_1) + b(p_2) \to \nu(p_3) + e^+(p_4) + b(p_5) + d(p_6)$  at NLO in QCD in the complex mass scheme including off-shell interference effects and non-resonant contributions required by gauge invariance. The complex mass scheme introduces a squared complex top-quark mass  $\mu_t^2 = m_t^2 - im_t\Gamma_t$  to the otherwise real valued top-quark mass in the Lagrangian. We also work in the five-flavor scheme and set  $m_b = 0$ . We compute all results at the amplitude level in the spinor helicity formalism in the 't Hooft-Veltman scheme and avoid any ambiguities related to  $\gamma_5$  in dimensional regularization and thus treat it in the naive dimensional regularization approach.

To obtain a gauge invariant result with an off-shell top quark, requires the inclusion of both resonant and non-resonant contributions. We include all such contributions and show a partial sample of the diagrams in figures 1, 2 and 3. In addition to QCD corrections, we allow for exactly one SMEFT operator insertion in each diagram (at positions denoted by the crossed circles in figure 3). We do not include the  $W + 2$  jets contributions that have a gluon exchange at tree level. These diagrams are separately gauge invariant, do not interfere with our contributions through NLO, and are considered a background that can be computed fully independently.

Apart from gluon radiation, in the SM and throughout NLO only two helicity amplitudes contribute. The first amplitude only encompasses left-handed particles and a right-handed positron. Its predominant contribution is from the resonant diagrams, which are purely left-handed charged current mediated. It also receives non-resonant contributions from  $Z$ -boson and photon exchanges. The second amplitude with flipped  $b$ -quark helicities comes purely from non-resonant pieces. When SMEFT operators are added, one has additional helicity amplitudes where either one of the  $b$ -quark helicities is flipped

![](images/4982c2527171842fbba6170a40d125734e41d67e7b40f96d8122481cfa82bb3c.jpg)  
(a) Non-resonant SMEFT.

![](images/b11383805cda351132714b2daa6cecc7c36310f0c50e53ae5c62e38c482216de.jpg)  
(b) Off-shell resonant.

![](images/0e4c35b4897b2c8ebbe38a0810d00e0c7d8ad4a06c691e8d902d203dc39d638f.jpg)  
Figure 2. (a) Example non-resonant contribution in the SMEFT at LO. (b) One-loop resonant diagram with production-decay interference.  
(a) Production.  
Figure 3. NLO virtual contribution to the (a) production vertex, (b) decay vertex, or (c) top-quark self-energy. Each crossed circle represents a possible SMEFT operator insertion.

![](images/eb1def561aead201e63f086b7ad1254b7f3c50c8a7ba1187d3a4f538dd037f87.jpg)  
(b) Decay.

![](images/5ca27928020fd606acf042ca4da5f9048043b0b0eace3eac200b833753596d28.jpg)  
(c) Self-energy.

$(\mathcal{Q}_{\varphi ud}^{33}, \mathcal{Q}_{dW}^{33}, \mathcal{Q}_{dG}^{33})$ , or the helicities of the light quark line are flipped together with the initial-state  $b$ -quark helicity  $(\mathcal{Q}_{4R})$ .

The one-loop amplitudes we want to compute and simplify have large tensor ranks that are further increased with the SMEFT contributions. Their evaluation with a standard framework like FeynCalc [98, 99] and Passarino-Veltman reduction, for example, would be prohibitively difficult due to the size of resulting and intermediate expressions. We instead develop our own setup in Mathematica [100] which performs the tensor reduction with dimensional shift relations [101]. We implement the dimensionally shifted integrals with increased propagator powers in terms of standard one-loop master integrals by means of integration by parts reduction performed with Kira [102]. The scalar one-loop integrals are evaluated with QCDLoop 2.0 [103, 104]. The few necessary Feynman diagrams are generated with QGRAF [105] and translated into initial FORM [106] code with DIANA [107] to output Mathematica code. Feynman rules are generated using LANHEP [108-111] and checked by-hand, as well as compared with refs. [112, 113]. We make use of the Mathematica packages S@M [114] and FeynCalc [98, 99] for debugging purposes. The simplification of large expressions is accelerated enormously with the multivariate polynomial greatest

common divisor implementation in Fermat [115], and it is used through an interface to Mathematica [116].

A major part of our calculation involves the reduction of spinor (helicity) chains to a set of basis structures, as outlined in ref. [46], where the elements of the minimal set are referred to as "standard matrix elements." We extended these reduction prescriptions to spinor chains of type left-right  $\langle \dots \rangle$  and right-left  $[\dots ]$ , which appear in our SMEFT contributions. In principle, a reduction to one spinor master structure is possible for the SM helicity amplitudes [46]; and a reduction to two master structures can be performed for the amplitudes with one flipped  $b$ -quark helicity (left-right and right-left types). In practice, we balance the number of structures we use against the number of terms produced when we express the coefficients in terms of kinematic invariants.

We begin by reducing all spinor combinations to a set of 59 structures. To achieve a full reduction to two master structures one can directly write down a set of 58 linearly independent equations in terms of nine Lorentz-invariants [46]. The use of Lorentz-invariants to parameterize the kinematics enforces one additional Gram determinant constraint [117], which leaves 57 independent equations. This system of equations is highly complicated, but can be solved with the aid of Kira [102, 118] for example. The resulting expressions are huge and do not directly to lead to simplifications when inserted in the amplitudes. Instead we follow the suggestion of ref. [46], and perform the reduction using only equations that do not introduce additional denominator structures. For example, we express the SM amplitude with left-handed  $b$ -quarks and contributions from  $\mathcal{Q}_{\varphi q}^{(3,33)}$ ,  $\mathcal{Q}_{uW}^{33}$ ,  $\mathcal{Q}_{uG}^{33}$ ,  $\mathcal{Q}_{4L}$  to the same helicity configuration in terms of five spinor chains. We reduce to a larger basis set for the amplitudes with flipped quark helicities, since the equations would either introduce additional complicated denominator structures, or do not lead to simpler final results.

Both resonant and non-resonant contributions contain box diagrams that naively lead to huge expressions. While expressing the results in terms of scalar box integrals in six dimensions removes some of the cancellations between the box and triangle diagrams, we do not use a basis that lends itself to simple expressions for the loop amplitudes. In order to deal with leftover spurious cancellations that eventually will impair numerical stability we implement a simple rescaling scheme stability control mechanism.

This stability control works as follows: for each phase space point we evaluate our matrix elements twice — in double precision, and again in double precision where all dimensionful quantities are rescaled by a constant. Taking into account the dimensionality of the matrix element, we then divide out the constant and check how many digits agree to get an estimate for the numerical precision of the result. We find that for precision runs the integration eventually focuses its sampling on numerically unstable points and the integration becomes unstable. If the stability check fails with less than four digits precision left, we reevaluate them using the QD library [119], which implements twice the precision of IEEE doubles (approximately 32 decimal digits) using two double precision variables. This is faster than an evaluation with full IEEE quad precision and allows for Fortran compilers without such quad precision support.

We directly compute all amplitudes for single-top-quark production. The matrix elements for single-top-antiquark production are obtained by crossing the single-top-quark

matrix elements after applying a CP transformation. After the CP transformation one crosses the light quarks and reidentifies electron and neutrino particle labels to obtain the single-top-antiquark result. The CP transformation itself introduces sign flips for the imaginary parts of the Wilson coefficients, which we take into account, but leaves the other parts unaffected since we assume  $V_{tb}$  is real.

In order to maintain a connection to PDF fits, we implement the use of double deep inelastic scattering (DDIS) scales [14] in MCFM. We label the DIS momentum transfer between the light-quark line and the  $b$ -quark line as  $Q^2 = -q^2$ . We then set the renormalization and factorization scales for the light-quark line to  $\mu^2 = Q^2$ , and for the  $b$ -quark line  $\mu^2 = Q^2 + m_t^2$ . The implementation of DDIS scales at NLO is a non-trivial effort, since light line and heavy line corrections have to be handled separately, and Catani-Seymour dipole contributions have also to be accounted for with the right scales.

As part of our calculation we compute the decay width  $t \to Wb$  at NLO including the SMEFT operators, with an on-shell  $W$ -boson and a massless  $b$ -quark. This is consistent with the complex mass scheme at NLO. We follow the steps of ref. [33] to perform the necessary real emission phase space integrals. In addition to the integrals listed in ref. [33] table I, we find that three additional finite phase space integrals  $\langle y\rangle$ ,  $\langle z\rangle$  and  $\langle yz\rangle$  are necessary. We compute these using the Mathematica package HypExp [120].

Crosschecks. We compute Feynman rules in the SM and the SMEFT with both LANHEP and by hand, ensuring proper relative signs with the help of ref. [113]. Our SMEFT Feynman rules agree with those in ref. [112]. The relative signs between  $\mathcal{Q}_{uW}^{33}$  and  $\mathcal{Q}_{uG}^{33}$ , and  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  are fixed by the anomalous dimension matrix in ref. [86], and we agree with this through our operator renormalization.

We compared our results analytically to the SMEFT tree level matrix elements printed in ref. [73], eq. (27). We also compared our results with the SMEFT NLO decay width results in eq. (120) of ref. [88] as well as with the mass and wavefunction renormalization constants. We fully agree with all those results when taking into account the different sign convention used in the covariant derivative for the SMEFT operator definition.

Using our anomalous couplings parametrization in eq. (2.2) with the  $W$ -boson momentum defined to be incoming, we find a global sign difference for  $\mathcal{Q}_{uW}^{33}$  and  $\mathcal{Q}_{dW}^{33}$  when comparing our results against the Protos code [63, 76]. This difference is explained by the different momentum convention in Protos, where the momentum is outgoing. We do agree on the relative signs between real and imaginary parts, so this difference is indeed purely a global sign of  $\mathcal{Q}_{uW}^{33}$  and  $\mathcal{Q}_{dW}^{33}$ .

Another check on our signs that eliminates a consistency problem with defining momenta as incoming or outgoing in the Feynman rules is as follows. The needed Feynman rules in off-shell single top production at NLO from  $\mathcal{Q}_{uW}^{33}$  and  $\mathcal{Q}_{uG}^{33}$ ,  $\mathcal{Q}_{dG}^{33}$  all have a linear momentum dependence, and one might argue that a sign difference can appear be because we define particle momenta as incoming. However, because we are considering off-shell effects, we must introduce the operator  $\mathcal{Q}_{dW}^{33}$ , which adds an additional contribution from the momentum independent  $W^{+}W^{-}\bar{b} b$  vertex. The relative sign between this contribution and the contributions from  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  at NLO is set by the cancellation between the

poles for UV renormalization and IR subtraction. As we are overall consistent with the signs in ref. [112], this fixes the signs of both  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$ . Since  $\mathcal{Q}_{uW}^{33}$  and  $\mathcal{Q}_{uG}^{33}$  have the same structure and mixing, it also fixes their signs. This is the first calculation to include the operators  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  at NLO (in the off-shell process), so this check is new.

We explicitly checked QCD gauge invariance for our amplitudes — analytically for pole terms and numerically for finite pieces. We note that all amplitudes contributing to  $\mathcal{Q}_{uG}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  are separately gauge invariant. As part of our setup we reproduce the SM NLO decay width, which is calculated in detail in refs. [33, 121]. We extensively compare our off-shell SM calculation to on-shell results for compatibility. We check the proper cancellation of poles between real and virtual corrections by checking independence of the  $\alpha$  parameter in the MCFM Catani-Seymour dipole implementation [122-124] to the permille level. We also check that all infrared singular limits of the real emission amplitude are approached correctly as predicted by the Catani-Seymour dipole terms.

# 2.2 Implementation in MCFM-8.3

Our results are implemented in the upcoming release version 8.3 of MCFM. Here we describe the user-visible modifications of MCFM. The code allows one to directly and easily reproduce the plots in the following phenomenology section. We implement  $b$  tagging, top-quark and  $W$  reconstruction, as well as preconfigured histograms for the most common observables in the SMEFT and spin correlation studies. Our implementation provides an easy analysis framework to perform further studies.

Dynamical double deep inelastic scattering scales can be consistently used at NLO by setting dynamicscale to 'DDIS' and scale=facscale to 1d0. In this way the momentum transfer along the  $W$ -boson  $Q^2$  is used as the scale for the light-quark-line corrections  $\mu^2 = Q^2$ , and  $\mu^2 = Q^2 + m_t^2$  for the heavy-quark-line corrections. These scales are also consistently used for the non-resonant contributions, with QCD corrections on the  $ud$ -quark line, and separate QCD corrections on the bottom-quark line.

The new block "Single top SMEFT, nproc=164,169" in the input file governs the inclusion of SMEFT operators and corresponding orders. The scale of new physics  $\Lambda$  can be separately set, and has a default value of  $1000\mathrm{GeV}$ . The flag enable 1/lambda4 enables the  $1/\Lambda^4$  contributions, where operators  $\mathcal{Q}_{\varphi ud}^{33}, \mathcal{Q}_{dW}^{33}, \mathcal{Q}_{dG}^{33}$  and  $\mathcal{Q}_{4R}$  can contribute for the first time. For the non-Hermitian operators we allow complex Wilson coefficients. We also have a flag to disable the pure SM contribution, leaving only contributions from SMEFT operators either interfered with the SM amplitudes or as squared contributions at  $1/\Lambda^4$ . This can be used to directly and quickly extract kinematical distributions and the magnitudes of pure SMEFT contributions.

To allow for easier comparisons with previous anomalous couplings results, and possibly estimate further higher order effects, we allow for an anomalous couplings mode at LO by enabling the corresponding flag. The relations between our operators and the anomalous couplings are the same as in eqs. (2.3), (2.4), (2.5) and (2.6).

The analysis/plotting routine is contained in the file 'src/User/nplotter_ktopanom.f', where all observables presented in this study are implemented, and the  $W$ -boson/neutrino reconstruction is implemented and can be

Table 1. Applied cuts at a center of momentum energy  $\sqrt{s} = 13\mathrm{TeV}$ ,  $m_t^{\mathrm{O.S.}} = 173\mathrm{GeV}$ ,  $\mu_X = \mu_R = \mu_F$  set to DDIS scales. W-boson and top-quark reconstruction are as described in the text.  

<table><tr><td>Jets</td><td>pT,jet &gt; 30 GeV, |ηjet| &lt; 4.5, Rjet = 0.4</td></tr><tr><td>Lepton</td><td>at least one b-jet and one non-b-jet (spectator)</td></tr><tr><td>Neutrino</td><td>plT &gt; 25 GeV, |ηl| &lt; 2.5</td></tr><tr><td></td><td>ptν &gt; 30 GeV</td></tr></table>

switched on or off. With this one can directly reproduce all the phenomenological results in this study.

# 3 Phenomenology

In this section we examine kinematic distributions in off-shell single-top-quark production and decay in both the SM and the SMEFT. We begin by examining the effects of a  $W$ -boson / neutrino reconstruction on the top-quark reconstruction. We then study a set of angular observables in the top-quark rest frame for the SM before we focus our attention on SMEFT contributions. We address the importance of unique NLO perturbative corrections to the SMEFT contributions compared to using LO predictions with SM  $K$ -factors. We also show the behavior of the operators  $\mathcal{Q}_{uG}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  that only enter at NLO and are shown here for the first time for the full process.

Our set of cuts is given in table 1. We require at least one  $b$ -jet and one non- $b$ -jet, but also allow for a third jet of either kind. We refer to the leading non- $b$ -jet as the spectator jet. On top of these cuts, experimental anomalous couplings studies in  $t$ -channel production select exactly two jets and have further cuts on the rapidities of the  $b$  and spectator jet [9-13]. We find that these additional cuts decrease the acceptance, but do not alter any of our conclusions here.

Our default choice of renormalization and factorization scales for the off-shell results are the DDIS scales, where for the light-quark line the momentum transfer  $Q^2$  to the  $b$ -quark line is used,  $\mu^2 = Q^2$ , and for the  $b$ -quark line  $\mu^2 = Q^2 + m_t^2$ . It has been shown that the DDIS scales lead to small perturbative corrections in inclusive observables [14, 30]. We confirm that the difference between using a fixed scale  $\mu^2 = m_t^2$  and the DDIS scales is tiny for most NLO accurate observables, even differentially. For LO observables like the subleading  $b$  or subleading light quark jet transverse momentum, which only enter through the real emission, the scale choices lead to significant differences.

We note that in on-shell results, we use the fixed scale  $m_{t}$  which is used throughout the literature. While a comparison between off-shell results with DDIS scales and on-shell results with  $m_{t}$  as a scale is not on precisely equal footing, we consider the DDIS scales to be an improvement over the current calculations that do not allow for this natural scale choice. While the DDIS paradigm formally breaks down at NNLO in QCD, interference between the light- and heavy-quark lines is expected to be small [58, 60]. In addition, there

remains an analytic relationship to DIS in PDF fits [19] that is directly constrained by the consistency of the calculation of DDIS.

We use CT14 parton distribution functions (PDFs) [125] at the corresponding perturbative orders with a value of  $\alpha_{s}^{\mathrm{NLO}}(m_{Z}) = 0.118$  at NLO, and at  $\alpha_{s}^{\mathrm{LO}}(m_{Z}) = 0.13$  at LO. The CKM matrix is chosen to be diagonal and all other parameters have recent PDG values as implemented in MCFM-8.3. The top-quark width is evaluated at the corresponding perturbative order for  $t\rightarrow Wb$  at the fixed scale  $m_t$  and takes into account the SMEFT contributions at LO and NLO.

# 3.1 Off-shell and  $W$ -reconstruction effects in the Standard Model

It is well known that in fixed order perturbation theory colored resonances are sensitive to soft radiation [126]. At higher orders in perturbation theory soft and collinear parton configurations between virtual corrections and real emission corrections cancel in the singular limit. However, configurations approaching the soft/collinear limits are still present. In our case, the top-quark is reconstructed from a reconstructed  $b$ -jet and  $W$ -boson. Depending on whether such radiation configurations get clustered with the  $b$ -jet, and whether the radiation is produced before the resonance or in its decay, one can observe a mass enhancement or diminution.

Assuming the top-quark is in the on-shell approximation, the cancellation between virtual corrections and real emission is pinched to the phase space with an on-shell reconstructed top-quark. Having an off-shell top quark makes the approach of the cancellation explicit, with large positive and negative contributions around  $\simeq m_t \pm \Gamma_t$ . To obtain a smooth invariant mass distribution near the peak one can either choose a larger binning with radius  $\simeq \Gamma_t$  or include all-order effects through parton shower or resummation.

A further complication is that experimental analyses have to use a reconstruction scheme for the leptonically decaying  $W$ -boson. The neutrino's transverse component can be derived by requiring the event's transverse momentum to be vanishing. On the other hand, the longitudinal component is completely unknown and needs to be reconstructed. This reconstruction induces a smearing, not just of the  $W$ -boson, but also of the reconstructed top quark. We follow the most recent ATLAS study on anomalous coupling contributions [12] and reconstruct the neutrino's four-vector by requiring that the invariant mass of the neutrino-electron system in the top-quark decay equals the on-shell  $W$ -boson mass. With this condition one has either two real solutions or two complex solutions for the neutrino's longitudinal component. In the former case the solution closer to zero is taken. For the latter case of complex solutions, the neutrino's transverse component is rescaled by 0.9 until a real and positive solution is found.

As a result of the neutrino reconstruction the reconstructed top-quark invariant mass distribution gets smeared, and the aforementioned problem is somewhat ameliorated, although not fully removed. We show this in figure 4, where we compare the reconstructed top-quark invariant mass distribution using the full neutrino four momentum to using the reconstructed neutrino (smeared). For comparison the on-shell distributions are also shown. The full off-shell result receives large negative (not shown on the logarithmic scale) and positive contributions close to the resonance. These are smeared by using the recon

![](images/41bf558233e2e0dc92d6002355c9d0b213c5700c26d34da1c926edca1cca43eb.jpg)  
Figure 4. Reconstructed top-quark mass distribution for an on-shell and off-shell top quark at NLO. The full result denotes reconstruction through the full  $W$ -boson and  $b$ -jet four vectors. The "W rec." lines denote the reconstruction of the neutrino's longitudinal component.

structured neutrino, but one can still see a noticeable dip just below  $m_{t}$ . These off-shell effects in comparison to the on-shell approximation are well known [41-43].

We note that the previous off-shell SM calculation in the complex mass scheme in ref. [43] with an on-shell  $W$ -boson seems to obtain a smooth  $m_{t}$  distribution with 1 GeV bins without applying any smearing procedures. This behavior could be due to the way the  $W$ -boson is handled, leading to a smoothing effect, although no indication of how to treat the  $W$ -boson decay is given in their study. It is also conceivable that since the affected region is not well-defined in fixed order perturbation theory, their use of a different subtraction procedure leads to a differently distributed result there.

The off-shell effects we consider are important for experimental observables. In figure 5 we show the positron transverse momentum distribution, which is sensitive to soft QCD radiation corrections only through the recoil of the  $W$  boson. The off-shell distribution is up to  $\sim 15\%$  harder at  $300\mathrm{GeV}$  compared to the on-shell result, while corrections at low  $p_T$  are at the few percent level. The  $K$ -factor  $(\sigma_{\mathrm{NLO}} / \sigma_{\mathrm{LO}})$  in an on-shell calculation and the  $K$ -factor in the off-shell calculation differ by at most a few percent. Similar corrections can be seen in the leading  $b$ -jet transverse momentum distribution in figure 6. There, off-shell effects at NLO are about  $5 - 10\%$  in the tail. The ratio of the  $K$ -factors for the off-shell and on-shell production is not flat, and shows deviations with up to  $\sim 10\%$ .

Deviations in the distributions of these top-quark decay products will have a significant effect on LHC measurements of the top-quark mass. To avoid neutrino reconstruction uncertainties, it is common practice to fit the top-quark mass based on the line shape of the  $b$ -jet/lepton invariant mass  $m_{bl}$  [8, 18]. In figure 7 we observe that off-shell effects lead to a large  $\sim 20\%$  shift in the  $m_{bl}$  line shape close to the kinematic endpoint. In a template

![](images/705206506fc1c0d3b81e64b8c371b285ca1bfa07eba00d527514077584d2a206.jpg)  
Figure 5. Positron transverse momentum distributions for the top-quark on-shell approximation and for the off-shell top quark at LO and NLO. The lower panel shows the ratio of the NLO/LO  $K$ -factors from the off-shell and on-shell results.

fit this effect is similar to a few GeV shift in the top-quark mass, though the difference might be partially ameliorated by further final state showering.

# 3.2 Angular observables in the top-quark rest frame

Apart from common kinematical distributions like transverse momenta, rapidities and invariant masses,  $t$ -channel single-top-quark analyses are characterized by their use of angular distributions. In particular, the angle between the leading non- $b$  jet and the lepton from the top-quark decay is strongly correlated in the top-quark rest frame [16, 17], and this is used in part to identify the  $t$ -channel state [31]. Any modification (other than scaling) of the production or decay vertices is expected to be observed as a modification of one or more angular observables [23, 24]. While most of the angles are well-behaved under the inclusion of off-shell effects from fixed order perturbation theory, we find that one angle is highly unstable to soft radiation.

The first set of angles we examine is sensitive to operators that modify the production of the top quark. A coordinate system is established by using the direction of the spectator quark  $\vec{p}_j$  in the top-quark rest frame to define a corresponding axis  $\hat{z}$ . A second axis  $\hat{y}$  is defined by the direction orthogonal to the plane made by the spectator quark and the initial-state light-quark, while the third axis  $\hat{x}$  is defined by requiring the coordinate system to be right-handed [24]. The direction of the initial-state quark is taken to be that of the

![](images/5c2b44211ffa3811c3843922c0805d6cc0c9f2ef35c47a08c5ffa2689d5fd741.jpg)  
Figure 6. Leading  $b$ -jet transverse momentum distributions for the top-quark on-shell approximation and for the off-shell top quark at LO and NLO. The lower panel shows the ratio of the NLO/LO  $K$ -factors from the off-shell and on-shell results.

![](images/9a42479889b3cd9d79bca384fb6f2d3a92f8719e9208dc10f7c8b1ed7ab1432e.jpg)  
Figure 7. Invariant mass of the positron plus leading  $b$ -jet system for the top-quark on-shell approximation and for the off-shell top quark at LO and NLO. The lower panel shows the ratio of the ratio of the NLO/LO  $K$ -factors from the off-shell and on-shell results.

proton beam that shares the same sign of rapidity as that of the spectator jet.

$$
\hat {z} = \frac {\vec {p _ {j}}}{| \vec {p _ {j}} |}, \quad \hat {y} = \frac {\vec {p _ {j}} \times \vec {p _ {q}}}{| \vec {p _ {j}} \times \vec {p _ {q}} |}, \quad \hat {x} = \hat {y} \times \hat {z}. (3. 1)
$$

We refer to angles of the lepton in the top-quark rest frame with respect to these axes as  $\cos \theta_{l,x}$ ,  $\cos \theta_{l,y}$ ,  $\cos \theta_{l,z}$ .

The second coordinate system we consider is sensitive to the decay vertex, and starts with the direction  $\vec{q}$  of the  $W$ -boson in the top-quark rest frame as one axis  $\hat{q}$ . The second axis  $\hat{N}$  is orthogonal to the plane defined by  $\hat{q}$  and the top-quark spin direction, as implemented by the spectator quark direction  $\vec{s}_t$  in the top-quark rest frame. The last axis  $\hat{T}$  is again defined by the right-handedness of the coordinate system [23]:

$$
\hat {q} = \frac {\vec {q}}{| \vec {q} |}, \quad \hat {N} = \frac {\vec {s} _ {t} \times \vec {q}}{| \vec {s} _ {t} \times \vec {q} |}, \quad \hat {T} = \hat {q} \times \hat {N}. (3. 2)
$$

From this basis we construct the angles between the lepton in the  $W$ -boson rest frame with respect to these three axes. We refer to them as  $\cos \theta_l^*$  for the angle with respect to the  $\hat{q}$  axis, and  $\cos \theta_l^N$ ,  $\cos \theta_l^T$  with respect to  $\hat{N}$  and  $\hat{T}$ , respectively. In addition to the angles described here, one can find angles between the  $\hat{N}$  and  $\hat{T}$  axes, and projections of the lepton in the  $W$  boson rest frame onto the  $\hat{N} -\hat{T}$  plane being used in analyses. We have examined those projection angles, but do not find interesting results regarding the SMEFT contributions.

Discussion of angular observables. First we note that neutrino reconstruction has a noticeable impact on most of the observables in the top-quark rest frame. This is expected as the top-quark rest frame has a direct dependence on the neutrino four-momentum. Since the reconstruction procedure we use is based on an experimental algorithm described in section 3.1, we do not comment further on angular differences due to other reconstruction procedures. Both on-shell and off-shell results that follow use a reconstructed neutrino.

It was previously observed [31] that, after cuts, going from LO to NLO had little effect on the SM angular distributions used to measure  $t$ -channel single-top-quark production. When comparing off-shell distributions to on-shell results, this similarity in most angular distributions is maintained. For example, for  $\cos \theta_{l,x}$  the  $K$ -factor ratio is  $\simeq 0.97 - 0.98$  and flat within  $1 - 2\%$  of integration noise. In the SM, off-shell effects have rather uniform impact. With one notable exception, the largest deviations in shape we find are  $\sim 10\%$  in  $\cos \theta_{l,y}$  and  $\cos \theta_l^*$  which are modestly relevant when considering backgrounds to SMEFT operators. For completeness we include corresponding plots with  $K$ -factor ratios in figures 14, 15, 16, 17 and 18 in appendix A.

One angular distribution that is currently used in experimental analyses [13] demands further discussion. The angular distribution of  $\cos \theta_l^N$  becomes unphysical at NLO for an off-shell top quark in fixed order perturbation theory, see figure 8. This is because the top-quark invariant mass distribution is not well-defined close to the resonance, where soft radiation from production and decay cancels. It turns out that the angle  $\cos \theta_l^N$  is highly sensitive to this cancellation and the cross section prediction becomes negative for  $\cos \theta_l^N \gtrsim 0$ , which is compensated by an according increase for  $\cos \theta_l^N \lesssim 0$ .

![](images/4c3da41165d5b314acaea2c2f00293585582a4f266d66cd3cf30905e76b821aa.jpg)  
Figure 8. Angular distribution  $\cos \theta_l^N$  at LO and NLO for an on-shell and off-shell top quark. The NLO off-shell result becomes unphysical and indicates a strong sensitivity to the cancellation of soft radiation.

When using this observable at LO or with the on-shell approximation one seemingly does not have this issue, since no negative cross section is observed. But the intrinsic sensitivity to the cancellation of soft radiation in this angle is merely hidden. Effects from resummation and parton showers can change the distribution drastically. As such we do not recommend to use this angle for precision studies in the SM and the SMEFT. One must be especially careful in the latter case, as SMEFT operators can modify gluon radiation. A resummation or parton shower without taking into account the SMEFT operators might lead to incorrect conclusions or limits.

# 3.3 SMEFT contributions

We now turn our attention to modifications of the angular distributions by SMEFT operators in the off-shell NLO QCD calculation. We distinguish how SMEFT operators modify the distributions compared to SM NLO effects. We also discuss the importance of higher order corrections in the EFT for the consistent extraction of limits on SMEFT Wilson coefficients. Operators that begin to enter at  $1 / \Lambda^2$  receive corrections at order  $1 / \Lambda^4$ . To obtain universal results one needs to make sure that these higher order EFT corrections are small.

We limit ourselves to some representative examples here, as a detailed study of all operators and their effects on all observables used in single-top studies is beyond the scope of this paper. Additional observables can easily and quickly be predicted with our published code. We only show off-shell results here and present  $K$ -factors for them, if applicable. We do not display  $\mathcal{Q}_{\varphi q}^{(3,33)}$  in our plots since this operator is just a rescaling of the SM results with an effective modification of  $V_{tb}$ . We consider the case where just one Wilson coefficient is non-zero and choose Wilson coefficients of one or  $i$ , with a scale  $\Lambda = 1000\mathrm{GeV}$ . This choice is not very important here, except for the consideration of higher order effects

$1 / \Lambda^4$ . Otherwise, our presentation of the pure (SM subtracted) and normalized SMEFT contributions divides out the Wilson coefficient.

NLO and  $1 / \Lambda^4$  effects. We start with a discussion of higher order effects in QCD and in the SMEFT. It has already been pointed out in ref. [92] that inclusively the  $K$ -factors for the SMEFT contributions are different from the SM  $K$ -factor broadly by  $10 - 25\%$  depending on the operator combination. We show below that differentially this worsens somewhat. For the actual distributions used to constrain BSM physics, NLO QCD corrections to the SMEFT operators are essential.

We begin with one of the most important operators  $\mathcal{Q}_{uW}^{33}$ , that leads to the richest phenomenological structure. In figure 9 we show the pure SMEFT contribution (with the SM contribution subtracted) at LO and NLO in QCD to get an impression of the perturbative corrections. We also include effects of order  $1 / \Lambda^2$  and additionally of order  $1 / \Lambda^4$  to show the impact of higher order EFT corrections. In the top panel the absolute corrections are shown and in the bottom panel we show  $K\equiv \mathrm{NLO / LO}$  as a representation of the perturbative corrections. For comparison we have also included the  $K$ -factor for the SM contribution itself in black.

The  $K$ -factor for the SMEFT contribution is not flat, and unique NLO QCD corrections are indeed important, especially for the region of  $\cos \theta_{l,x} \simeq -1$ . The impact of the  $1 / \Lambda^4$  corrections on the  $K$ -factor is moderate in size, apart from the first bins. This effect reduces for a smaller Wilson coefficient or a larger scale  $\Lambda$ , but might have to be considered depending on the analysis. Differentially the corrections are an important effect to consider, but the size of the contributions at  $\cos \theta_{l,x} \simeq -1$  are small in comparison to the other regions. We show the same operator contributions for  $\cos \theta_{l,y}$  in figure 10. Generally NLO corrections are sizable differentially and important to correctly capture the shapes.

The imaginary part of  $\mathcal{Q}_{uW}^{33}$ . While for most of the  $1 / \Lambda^2$  contributions with Wilson coefficients of one, the higher order EFT effects seem to be moderate, this is not the case for the imaginary part of  $\mathcal{Q}_{uW}^{33}$ 's Wilson coefficient,  $\Im \mathfrak{m}\mathcal{C}_{uW}^{33}$ . It is claimed in the literature that the imaginary part of  $\mathcal{Q}_{uW}^{33}$  does not contribute at  $1 / \Lambda^2$  [92]. We do not find this to be true (with our set of cuts). For the stable-top approximation one indeed does not have enough linearly independent four-vectors contracted with the Levi-Civita tensor, so the contribution vanishes [127], but this no longer holds for a decaying top-quark. The Wilson coefficient  $\Im \mathfrak{m}\mathcal{C}_{uW}^{33}$  enters the composite observable  $\delta_{-}$  [127-129] as measured for example by ATLAS [130].

While inclusively the operator contribution for  $\mathfrak{Im}\mathcal{C}_{uW}^{33} = 1$  and  $\Lambda = 1000\mathrm{GeV}$  is tiny at  $1 / \Lambda^2$ , this is not true differentially. At LO the  $1 / \Lambda^4$  contributions are small, but they are not flat, and the NLO contribution is neither small nor flat. We display these issues in figure 11 and figure 12. Figure 11 shows with the  $\cos \theta_{l,x}$  distribution that inclusively the contribution from  $\mathfrak{Im}\mathcal{C}_{uW}^{33}$  is small at LO, but it is large at NLO QCD with a complex angular structure. The  $\cos \theta_{l,y}$  distribution in figure 12 shows that differentially in  $\cos \theta_{l,y}$  at NLO,  $\mathfrak{Im}\mathcal{C}_{uW}^{33}$  leads to large contributions, where large negative contributions for  $\cos \theta_{l,y} < 0$  cancel with positive contributions in  $\cos \theta_{l,y} > 0$  inclusively, but will strongly modify the

![](images/d12edfb04019eca6b481308e5bae57307ab1d9ef0b88ba9f6058ffec3004ab96.jpg)  
Figure 9. Distribution of  $\cos \theta_{l,x}$  for the pure SMEFT contribution with  $\Re \mathcal{C}_{uW}^{33} = 1$ ,  $\Lambda = 1000\mathrm{GeV}$ . Shown are results at LO and NLO in QCD and at  $1 / \Lambda^2$  in the SMEFT as well as with higher order effects  $1 / \Lambda^4$ .

![](images/bc95a71a3dfa72aac6be3083994799ab945058fb6fdf7f015baa6f0f31fbffc0.jpg)  
Figure 10. Distribution of  $\cos \theta_{l,y}$  for the pure SMEFT contribution with  $\Re \mathcal{C}_{uW}^{33} = 1$ ,  $\Lambda = 1000\mathrm{GeV}$ . Shown are results at LO and NLO in QCD and at  $1 / \Lambda^2$  in the SMEFT as well as with higher order effects  $1 / \Lambda^4$ .

![](images/1c24d5f05f26d4afa4d8c54212d269bb33f4df5240f63f8e30b86034e18b7ded.jpg)  
Figure 11. Distribution of  $\cos \theta_{l,x}$  for the pure SMEFT contribution with  $\mathfrak{Im}\mathcal{C}_{uW}^{33} = 1$ ,  $\Lambda = 1000\mathrm{GeV}$ . Shown are results at LO and NLO in QCD and at  $1 / \Lambda^2$  in the SMEFT as well as higher order effects  $1 / \Lambda^4$ .

![](images/adae2d6eb0cf5187e54eca0df9dd13e8e5bd2a9c8920e11472326f8487a80884.jpg)  
Figure 12. Distribution of  $\cos \theta_{l,y}$  for the pure SMEFT contribution with  $\mathfrak{Im}\mathcal{C}_{uW}^{33} = 1$ ,  $\Lambda = 1000\mathrm{GeV}$ . Shown are results at LO and NLO in QCD and at  $1 / \Lambda^2$  in the SMEFT as well as higher order effects  $1 / \Lambda^4$ .

SM result. Interestingly the shift in  $\cos \theta_{l,y}$  here is similar in shape and size to the shift seen in figure 15 when going from an on-shell approximation to the full off-shell result in the SM.

![](images/40cc365b1d4e7fe251617cbb5aedb3551631f41fc1806fcde9649423067aadca.jpg)  
Figure 13. To itself and to the SM normalized SMEFT contributions to the cos  $\theta_{l,x}$  distribution at NLO in QCD. Results are presented for the real and imaginary parts of  $\mathcal{C}_{uW}^{33}$  and  $\mathcal{C}_{uG}^{33}$  as well as for the four quark operator  $\mathcal{C}_{4L}$ .

The sensitivity to  $1 / \Lambda^2$  contributing SMEFT operators. One way to present the sensitivity of the angular observables to the various operators is to show normalized distributions where the SM contributions are divided out. As previous we compute the SMEFT contribution  $\sigma^{\mathrm{EFT}}$ , but now we also normalize these distributions to themselves and divide by the normalized SM distribution. In this way one can see the shape difference of the SMEFT contribution with respect to the SM. Since shape differences in differential distributions result in the highest discriminating power, operators with stronger shape differentials can be constrained better. In short, what we show in the following for a differential distribution with respect to the variable  $x$  is

$$
\left(\frac {1}{\sigma^ {\mathrm {E F T}}} \cdot \frac {\Delta \sigma^ {\mathrm {E F T}}}{\Delta x}\right) \Bigg / \left(\frac {1}{\sigma^ {\mathrm {S M}}} \cdot \frac {\Delta \sigma^ {\mathrm {S M}}}{\Delta x}\right), (3. 3)
$$

where  $\sigma^{\mathrm{EFT}}$  is the SM subtracted pure SMEFT contribution,  $\sigma = \sigma^{\mathrm{EFT}} + \sigma^{\mathrm{SM}}$ .

In figure 13 we show the resulting shapes for the real and imaginary parts of the Wilson coefficients for the operators  $\mathcal{Q}_{uW}^{33}$  and  $\mathcal{Q}_{uG}^{33}$  and the four quark operator  $\mathcal{Q}_{4L}$ . Note that the operator  $\mathcal{Q}_{uG}^{33}$  has no LO contribution since it only enters at NLO. Generally  $\mathfrak{Im}\mathcal{C}_{uW}^{33}$  and  $\mathfrak{Im}\mathcal{C}_{uG}^{33}$  have the largest shape differentials. Arriving at precise limits on Wilson coefficients is thus strongly influenced by unique NLO contributions. The corresponding distributions for the angles  $\cos\theta_{l,y}$ ,  $\cos\theta_{l,z}$  and  $\cos\theta_{l}^{*}$  as well as  $\cos\theta_{l}^{T}$  are in included in appendix A in figures 19, 20, 21 and 22 for completeness, and are maximally sensitive to the imaginary parts of the operators.

The sensitivity to  $1 / \Lambda^4$  contributing SMEFT operators. We treat operators that enter at  $1 / \Lambda^4$  as leading order in the SMEFT in the sense that we do not consider possible

mixing with dimension eight operators that appear at NLO in QCD. We include these operators to allow for a mapping onto the right-handed anomalous coupling experimental limits, such as arise in  $W'$  models [22, 93, 94]. These operators do not interfere with the SM amplitude.

We present self-normalized angular distributions that are divided by the SM angular distribution shape for the operators  $\mathcal{Q}_{\varphi ud}^{33}$ ,  $\mathcal{Q}_{dW}^{33}$ ,  $\mathcal{Q}_{dG}^{33}$  and  $\mathcal{Q}_{4R}$  in figures 23, 24, 25, 26 and 27 in appendix A. The cross sections only depend on the modulus squared of the Wilson coefficients  $|C_i|^2$ . Operators like  $\mathcal{Q}_{\varphi ud}^{33}$  that act like a right-handed Wtb coupling predictably create a strong  $\cos \theta_{l,z}$  dependence that can be distinguished from the four-fermion operator  $\mathcal{Q}_{4R}$  by comparing to  $\cos \theta_{l,y}$ .

# 4 Conclusions

In this study we present for the first time a full  $2 \rightarrow 4$  off-shell calculation of  $t$ -channel single-top-quark production at NLO in QCD, taking into account the decay of the  $W$ -boson at the amplitude level. We use the complex mass scheme to gauge-invariantly include such off-shell effects in both the SM, and in the SMEFT framework. We include all relevant dimension six operators that affect the  $Wtb$  vertex at NLO in QCD.

We examine off-shell effects in the SM and find significant differences with respect to the on-shell approximation. We also consider effects due to the reconstruction of the  $W$ -boson and neutrino coincident with the off-shell effects. While sensitivity of the reconstructed top-quark invariant mass distribution near its peak due to soft radiation is expected for an off-shell top quark; we point out for the first time how this carries through to certain angular distributions used by experimental analyses. In particular, we find that the  $\cos \theta_l^N$  distribution used by some analyses, which is constructed in the top-quark rest frame, becomes unphysical when off-shell effects are included. This problem is hidden in the on-shell calculations. Without a resummation of soft radiation in the on-shell region, we cannot recommend the use of this observable for precision studies.

Our results move beyond the common LO SMEFT picture and allow for a fully consistent SMEFT evaluation at  $1 / \Lambda^2$ , as well as partial corrections from  $1 / \Lambda^4$  operators in order to compare to the anomalous couplings picture. We show that NLO QCD effects to the SMEFT contributions can be large in angular distributions, and in general are not captured by a rescaling with SM  $K$ -factors. In addition, the operators  $\mathcal{Q}_{uG}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  are included for the first time in the full process at NLO. These operators only begin to enter at NLO in QCD, and are important for consistent NLO limits on Wilson coefficients.

We present an extensive list of checks of our amplitudes, and we successfully compare several SM and SMEFT terms at LO and NLO with results from the literature. We are able to identify the correct relative signs of all pieces of our calculation through checks of gauge-invariance, and UV and IR finiteness. Because of the asymmetric nature of limits for positive and negative SMEFT operators that arise in the NLO calculations, it is imperative for experimental analyses to clearly state which sign convention is used for both minimal coupling in the SM and for the SMEFT.

While we present the most complete fixed-order perturbative calculation of the SMEFT operators, a dedicated study of parton shower effects to observables used for SMEFT studies would be useful. Parton shower effects are included in ref. [92], but they do not discuss their impact on the fixed order results. Some observables, like the top-quark invariant mass distribution clearly need to include all-order effects. Our study is also performed with a massless bottom quark, but bottom-quark mass effects could become interesting at future precision levels.

Our implementation is publicly available in MCFM-8.3 and includes preconfigured plotting routines to reproduce all distributions in this study. It is our goal to allow for easy, yet precise and refined determination of observables in the SM and better constraints on SMEFT operators.

# Acknowledgments

We thank Stefan Dittmaier for helpful comments on the reduction to spinor chain master structures, John Campbell for invaluable continuous discussion, Bogdan Dobrescu for useful discussion on model interpretation of the EFT operators, Claudius Krause for helpful discussion about the SMEFT, and Mario Prausa for help on interpreting Fermat output. We would also like to thank Cen Zhang for helping to track down the sign discrepancy we stated in the preprint of this study to a different sign convention used in parts of the literature. Feynman diagrams were generated with TikZ-Feynman [131].

This work was supported by the U.S. Department of Energy under award No. DE-SC0008347. This document was prepared using the resources of the Fermi National Accelerator Laboratory (Fermilab), a U.S. Department of Energy, Office of Science, HEP User Facility. Fermilab is managed by Fermi Research Alliance, LLC (FRA), acting under Contract No. DE-AC02-07CH11359.

# A Additional figures

![](images/67a2003f53cebdaabb2389aef8c19800105463145e80bb8d4454117116856a1d.jpg)  
Figure 14. Distribution of  $\cos \theta_{l,x}$  at NLO in the on-shell approximation and for an off-shell top quark. The lower panel shows the ratio of the off-shell and on-shell  $K$ -factors. Note the range of the  $y$ -axis, which does not start at zero.

![](images/4e4ebb117e09e200776a6ff1942c3d3a72cdeebd4c0c264c726df95dafca9fae.jpg)  
Figure 15. Distribution of  $\cos \theta_{l,y}$  at NLO in the on-shell approximation and for an off-shell top quark. The lower panel shows the ratio of the off-shell and on-shell  $K$ -factors. Note the range of the  $y$ -axis, which does not start at zero.

![](images/aeba1cbc33b654d5f00fcf00bfae97988301c138a2566cdb102526621b03fc65.jpg)  
Figure 16. Distribution of  $\cos \theta_{l,z}$  at NLO in the on-shell approximation and for an off-shell top quark. The lower panel shows the ratio of the off-shell and on-shell  $K$ -factors. Note the range of the  $y$ -axis, which does not start at zero.

![](images/f955ebf1954226d141e24e6e95f3b3e0c6bcffe962318a2b5c60c2175c1b498d.jpg)  
Figure 17. Distribution of  $\cos \theta_l^T$  at NLO in the on-shell approximation and for an off-shell top quark. The lower panel shows the ratio of the off-shell and on-shell  $K$ -factors. Note the range of the  $y$ -axis, which does not start at zero.

![](images/4f714a595cb16fa534fa962a885c818886096b05d7570d9025203af6004ed58e.jpg)  
Figure 18. Distribution of  $\cos \theta_l^*$  at NLO in the on-shell approximation and for an off-shell top quark. The lower panel shows the ratio of the off-shell and on-shell  $K$ -factors. Note the range of the  $y$ -axis, which does not start at zero.

![](images/43c65fa4cbdb4b9d3c69c8b4b721b497cbea6a2c896b60d2fe1a5f635d687a65.jpg)  
Figure 19. To itself and to the SM normalized SMEFT contributions to the cos  $\theta_{l,x}$  distribution at NLO in QCD. Results are presented for the real and imaginary parts of  $\mathcal{C}_{uW}^{33}$  and  $\mathcal{C}_{uG}^{33}$  as well as for the four quark operator  $\mathcal{C}_{4L}$ .

![](images/d9389914a2f4980f5c342afe3c9402f06e9117eb7fb3a9df7ad747ee44ee93c4.jpg)  
Figure 20. To itself and to the SM normalized SMEFT contributions to the cos  $\theta_{l,y}$  distribution at NLO in QCD. Results are presented for the real and imaginary parts of  $\mathcal{C}_{uW}^{33}$  and  $\mathcal{C}_{uG}^{33}$  as well as for the four quark operator  $\mathcal{C}_{4L}$ .

![](images/5a819b93796418dd4e64e2ae85c1aa2f8531ac0753019555410abb6583d470b7.jpg)  
Figure 21. To itself and to the SM normalized SMEFT contributions to the  $\cos \theta_l^T$  distribution at NLO in QCD. Results are presented for the real and imaginary parts of  $\mathcal{C}_{uW}^{33}$  and  $\mathcal{C}_{uG}^{33}$  as well as for the four quark operator  $\mathcal{C}_{4L}$ .

![](images/487c9dbecdfb867d3857199be5fcd18799930305c1791a9915b1e445ddc90b75.jpg)  
Figure 22. To itself and to the SM normalized SMEFT contributions to the  $\cos \theta_l^*$  distribution at NLO in QCD. Results are presented for the real and imaginary parts of  $\mathcal{C}_{uW}^{33}$  and  $\mathcal{C}_{uG}^{33}$  as well as for the four quark operator  $\mathcal{C}_{4L}$ .

![](images/db7601437319da6b0724e3d7a40d50de5f6b39c614eec6e72d7ef1209294994d.jpg)  
Figure 23. To itself and to the SM normalized SMEFT contributions to the cos  $\theta_{l,x}$  distribution at NLO in QCD. Results are presented for  $\mathcal{Q}_{\varphi ud}^{33}$ ,  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  as well as for the four quark operator  $\mathcal{Q}_{4R}$ .

![](images/34cb87382f7712c274129fd009c0f621ab93f4e089ba2b24b8c92270551ae4ac.jpg)  
Figure 24. To itself and to the SM normalized SMEFT contributions to the cos  $\theta_{l,y}$  distribution at NLO in QCD. Results are presented for  $\mathcal{Q}_{\varphi ud}^{33}$ ,  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  as well as for the four quark operator  $\mathcal{Q}_{4R}$ .

![](images/4b7abdcac6935e77eb594c7ab2f8b734c43fe270d8d75b4c535c2fc142744ac4.jpg)  
Figure 25. To itself and to the SM normalized SMEFT contributions to the cos  $\theta_{l,z}$  distribution at NLO in QCD. Results are presented for  $\mathcal{Q}_{\varphi ud}^{33}$ ,  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  as well as for the four quark operator  $\mathcal{Q}_{4R}$ .

![](images/38b2790944ac1c4351b5a8fdc9d7f99581481aad607bfb2728334ee3e807d3dc.jpg)  
Figure 26. To itself and to the SM normalized SMEFT contributions to the  $\cos \theta_l^T$  distribution at NLO in QCD. Results are presented for  $\mathcal{Q}_{\varphi ud}^{33}$ ,  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  as well as for the four quark operator  $\mathcal{Q}_{4R}$ .

![](images/f485bfe7c1dccb5d1779ceff155c2f8d727b8b2330bbe09ba1234307770ca639.jpg)  
Figure 27. To itself and to the SM normalized SMEFT contributions to the  $\cos \theta_l^*$  distribution at NLO in QCD. Results are presented for  $\mathcal{Q}_{\varphi ud}^{33}$ ,  $\mathcal{Q}_{dW}^{33}$  and  $\mathcal{Q}_{dG}^{33}$  as well as for the four quark operator  $\mathcal{Q}_{4R}$ .

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] ATLAS collaboration, Measurement of the t-channel single top-quark production cross section in pp collisions at  $\sqrt{s} = 7$  TeV with the ATLAS detector, Phys. Lett. B 717 (2012) 330 [arXiv:1205.3130] [INSPIRE].  
[2] ATLAS collaboration, Comprehensive measurements of t-channel single top-quark production cross sections at  $\sqrt{s} = 7$  TeV with the ATLAS detector, Phys. Rev. D 90 (2014) 112006 [arXiv:1406.7844] [INSPIRE].  
[3] ATLAS collaboration, Measurement of the inclusive cross-sections of single top-quark and top-antiquark t-channel production in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, JHEP 04 (2017) 086 [arXiv:1609.03920] [INSPIRE].  
[4] ATLAS collaboration, Fiducial, total and differential cross-section measurements of t-channel single top-quark production in pp collisions at 8 TeV using data collected by the ATLAS detector, Eur. Phys. J. C 77 (2017) 531 [arXiv:1702.02859] [INSPIRE].  
[5] CMS collaboration, Measurement of the t-channel single top quark production cross section in pp collisions at  $\sqrt{s} = 7$  TeV, Phys. Rev. Lett. 107 (2011) 091802 [arXiv:1106.3052] [INSPIRE].  
[6] CMS collaboration, Measurement of the single-top-quark  $t$ -channel cross section in pp collisions at  $\sqrt{s} = 7$  TeV, JHEP 12 (2012) 035 [arXiv:1209.4533] [INSPIRE].  
[7] CMS collaboration, Cross section measurement of t-channel single top quark production in pp collisions at  $\sqrt{s} = 13$  TeV, Phys. Lett. B 772 (2017) 752 [arXiv:1610.00678] [INSPIRE].  
[8] CMS collaboration, Measurement of the top quark mass using single top quark events in proton-proton collisions at  $\sqrt{s} = 8$  TeV, Eur. Phys. J. C **77** (2017) 354 [arXiv:1703.02530] [INSPIRE].  
[9] CMS collaboration, Measurement of the t-channel single-top-quark production cross section and of the  $|V_{tb}|$  CKM matrix element in pp collisions at  $\sqrt{s} = 8$  TeV, JHEP 06 (2014) 090 [arXiv:1403.7366] [INSPIRE].  
[10] CMS collaboration, Measurement of top quark polarisation in  $t$ -channel single top quark production, JHEP 04 (2016) 073 [arXiv:1511.02138] [INSPIRE].  
[11] CMS collaboration, Search for anomalous Wtb couplings and flavour-changing neutral currents in t-channel single top quark production in pp collisions at  $\sqrt{s} = 7$  and 8 TeV, JHEP 02 (2017) 028 [arXiv:1610.03545] [INSPIRE].  
[12] ATLAS collaboration, Analysis of the Wtb vertex from the measurement of triple-differential angular decay rates of single top quarks produced in the t-channel at  $\sqrt{s} = 8$  TeV with the ATLAS detector, JHEP 12 (2017) 017 [arXiv:1707.05393] [INSPIRE].  
[13] ATLAS collaboration, Probing the Wtb vertex structure in t-channel single-top-quark production and decay in pp collisions at  $\sqrt{s} = 8$  TeV with the ATLAS detector, JHEP 04 (2017) 124 [arXiv:1702.08309] [INSPIRE].  
[14] T. Stelzer, Z. Sullivan and S. Willenbrock, Single top quark production via W-gluon fusion at next-to-leading order, Phys. Rev. D 56 (1997) 5919 [hep-ph/9705398] [INSPIRE].  
[15] ATLAS and CMS collaborations, Combinations of single-top-quark production cross-section measurements and  $|f_{\mathrm{LV}}V_{tb}|$  determinations at  $\sqrt{s} = 7$  and 8 TeV with the ATLAS and CMS experiments, JHEP 05 (2019) 088 [arXiv:1902.07158] [INSPIRE].

[16] G. Mahlon and S.J. Parke, Improved spin basis for angular correlation studies in single top quark production at the Tevatron, Phys. Rev. D 55 (1997) 7249 [hep-ph/9611367] [INSPIRE].  
[17] G. Mahlon and S.J. Parke, *Single top quark production at the LHC: understanding spin*, Phys. Lett. B **476** (2000) 323 [hep-ph/9912458] [INSPIRE].  
[18] ATLAS collaboration, Measurement of the top quark mass in topologies enhanced with single top quarks produced in the  $t$ -channel at  $\sqrt{s} = 8$  TeV using the ATLAS experiment, in Proceedings,  $7^{\text{th}}$  International Workshop on Top Quark Physics (TOP2014), Cannes, France, 28 September-3 October 2014 [arXiv:1411.3879] [INSPIRE].  
[19] Z. Sullivan, Are PDFs still consistent with Tevatron data?, EPJ Web Conf. 172 (2018) 03008 [arXiv:1711.04018] [INSPIRE].  
[20] N.A. Abdulov, H. Jung, A.V. Lipatov, G.I. Lykasov and M.A. Malyshev, Employing RHIC and LHC data to determine the transverse momentum dependent gluon density in a proton, Phys. Rev. D 98 (2018) 054010 [arXiv:1806.06739] [INSPIRE].  
[21] T.M.P. Tait and C.P. Yuan, The phenomenology of single top quark production at the Fermilab Tevatron, hep-ph/9710372 [INSPIRE].  
[22] T.M.P. Tait and C.P. Yuan, Single top quark production as a window to physics beyond the Standard Model, Phys. Rev. D 63 (2000) 014018 [hep-ph/0007298] [INSPIRE].  
[23] J.A. Aguilar-Saavedra and J. Bernabeu, W polarization beyond helicity fractions in top quark decays, Nucl. Phys. B 840 (2010) 349 [arXiv:1005.5382] [INSPIRE].  
[24] J.A. Aguilar-Saavedra and S. Amor Dos Santos, New directions for top quark polarization in the t-channel process, Phys. Rev. D 89 (2014) 114009 [arXiv:1404.1585] [INSPIRE].  
[25] J.A. Aguilar-Saavedra and J. Bernabeu, Breaking down the entire  $W$  boson spin observables from its decay, Phys. Rev. D 93 (2016) 011301 [arXiv:1508.04592] [INSPIRE].  
[26] J.A. Aguilar-Saavedra, J. Boudreau, C. Escobar and J. Mueller, The fully differential top decay distribution, Eur. Phys. J. C 77 (2017) 200 [arXiv:1702.03297] [INSPIRE].  
[27] G. Bordes and B. van Eijk, Calculating QCD corrections to single top production in hadronic interactions, Nucl. Phys. B 435 (1995) 23 [INSPIRE].  
[28] P. Kant et al., HatHor for single top-quark production: updated predictions and uncertainty estimates for single top-quark production in hadronic collisions, Comput. Phys. Commun. 191 (2015) 74 [arXiv:1406.4403] [INSPIRE].  
[29] B.W. Harris, E. Laenen, L. Phaf, Z. Sullivan and S. Weinzierl, The fully differential single top quark cross-section in next to leading order QCD, Phys. Rev. D 66 (2002) 054024 [hep-ph/0207055] [INSPIRE].  
[30] Z. Sullivan, Understanding single-top-quark production and jets at hadron colliders, Phys. Rev. D 70 (2004) 114012 [hep-ph/0408049] [INSPIRE].  
[31] Z. Sullivan, Angular correlations in single-top-quark and Wjj production at next-to-leading order, Phys. Rev. D 72 (2005) 094034 [hep-ph/0510224] [INSPIRE].  
[32] Q.-H. Cao and C.P. Yuan, Single top quark production and decay at next-to-leading order in hadron collision, Phys. Rev. D 71 (2005) 054022 [hep-ph/0408180] [INSPIRE].  
[33] J.M. Campbell, R.K. Ellis and F. Tramontano, *Single top production and decay at next-to-leading order*, Phys. Rev. D **70** (2004) 094012 [hep-ph/0408158] [INSPIRE].

[34] R. Schwienhorst, C.P. Yuan, C. Mueller and Q.-H. Cao, Single top quark production and decay in the t-channel at next-to-leading order at the LHC, Phys. Rev. D 83 (2011) 034019 [arXiv:1012.5132] [INSPIRE].  
[35] J.M. Campbell, R. Frederix, F. Maltoni and F. Tramontano, Next-to-leading-order predictions for t-channel single-top production at hadron colliders, Phys. Rev. Lett. 102 (2009) 182003 [arXiv:0903.0005] [INSPIRE].  
[36] J.M. Campbell, R. Frederix, F. Maltoni and F. Tramontano, NLO predictions for t-channel production of single top and fourth generation quarks at hadron colliders, JHEP 10 (2009) 042 [arXiv:0907.3933] [INSPIRE].  
[37] J.M. Campbell and R.K. Ellis, Top-quark processes at NLO in production and decay, J. Phys. G 42 (2015) 015005 [arXiv:1204.1513] [INSPIRE].  
[38] J.M. Campbell and R.K. Ellis, MCFM for the Tevatron and the LHC, Nucl. Phys. Proc. Suppl. 205-206 (2010) 10 [arXiv:1007.3492] [INSPIRE].  
[39] R. Pittau, Final state QCD corrections to off-shell single top production in hadron collisions, Phys. Lett. B 386 (1996) 397 [hep-ph/9603265] [INSPIRE].  
[40] M. Beneke, A.P. Chapovsky, A. Signer and G. Zanderighi, *Effective theory calculation of resonant high-energy scattering*, Nucl. Phys. B 686 (2004) 205 [hep-ph/0401002] [INSPIRE].  
[41] P. Falgari, F. Giannuzzi, P. Mellor and A. Signer, Off-shell effects for t-channel and s-channel single-top production at NLO in QCD, Phys. Rev. D 83 (2011) 094013 [arXiv:1102.5267] [INSPIRE].  
[42] P. Falgari, P. Mellor and A. Signer, Production-decay interferences at NLO in QCD for t-channel single-top production, Phys. Rev. D 82 (2010) 054028 [arXiv:1007.0893] [INSPIRE].  
[43] A.S. Papanastasiou, R. Frederix, S. Frixione, V. Hirschi and F. Maltoni, Single-top t-channel production with off-shell and non-resonant effects, Phys. Lett. B 726 (2013) 223 [arXiv:1305.7088] [INSPIRE].  
[44] R. Frederix, S. Frixione, A.S. Papanastasiou, S. Prestel and P. Torrielli, Off-shell single-top production at NLO matched to parton showers, JHEP 06 (2016) 027 [arXiv:1603.01178] [INSPIRE].  
[45] A. Denner, S. Dittmaier, M. Roth and D. Wackeroth, Predictions for all processes  $e^{+}e^{-}\rightarrow 4$  fermions  $+\gamma$ , Nucl. Phys. B 560 (1999) 33 [hep-ph/9904472] [INSPIRE].  
[46] A. Denner, S. Dittmaier, M. Roth and L.H. Wieders, Electroweak corrections to charged-current  $e^{+}e^{-} \rightarrow 4$  fermion processes: technical details and further results, Nucl. Phys. B 724 (2005) 247 [Erratum ibid. B 854 (2012) 504] [hep-ph/0505042] [INSPIRE].  
[47] A. Denner and S. Dittmaier, The complex-mass scheme for perturbative calculations with unstable particles, Nucl. Phys. Proc. Suppl. 160 (2006) 22 [hep-ph/0605312] [INSPIRE].  
[48] A. Denner and J.-N. Lang, The complex-mass scheme and unitarity in perturbative quantum field theory, Eur. Phys. J. C 75 (2015) 377 [arXiv:1406.6280] [INSPIRE].  
[49] S. Frixione, E. Laenen, P. Motylinski and B.R. Webber, Single-top production in MC@NLO, JHEP 03 (2006) 092 [hep-ph/0512250] [INSPIRE].

[50] S. Alioli, P. Nason, C. Oleari and E. Re, NLO single-top production matched with shower in POWHEG: s- and t-channel contributions, JHEP 09 (2009) 111 [Erratum ibid. 02 (2010) 011] [arXiv:0907.4076] [INSPIRE].  
[51] N. Kidonakis, Higher-order soft gluon corrections in single top quark production at the LHC, Phys. Rev. D 75 (2007) 071501 [hep-ph/0701080] [INSPIRE].  
[52] J. Wang, C.S. Li, H.X. Zhu and J.J. Zhang, Factorization and resummation of t-channel single top quark production, arXiv:1010.4509 [INSPIRE].  
[53] N. Kidonakis, Next-to- next-to-leading-order collinear and soft gluon corrections for t-channel single top quark production, Phys. Rev. D 83 (2011) 091503 [arXiv:1103.2792] [INSPIRE].  
[54] N. Kidonakis, NNLL threshold resummation for top-pair and single-top production, Phys. Part. Nucl. 45 (2014) 714 [arXiv:1210.7813] [INSPIRE].  
[55] N. Kidonakis, *Single-top transverse-momentum distributions at approximate NNLO*, Phys. Rev. D 93 (2016) 054022 [arXiv:1510.06361] [INSPIRE].  
[56] Q.-H. Cao, P. Sun, B. Yan, C.P. Yuan and F. Yuan, Transverse momentum resummation for t-channel single top quark production at the LHC, Phys. Rev. D 98 (2018) 054032 [arXiv:1801.09656] [INSPIRE].  
[57] Q.-H. Cao, P. Sun, B. Yan, C.P. Yuan and F. Yuan, Soft gluon resummation in t-channel single top quark production at the LHC, arXiv:1902.09336 [INSPIRE].  
[58] M. Brucherseifer, F. Caola and K. Melnikov, On the NNLO QCD corrections to single-top production at the LHC, Phys. Lett. B 736 (2014) 58 [arXiv:1404.7116] [INSPIRE].  
[59] M. Assadsolimani, P. Kant, B. Tausk and P. Uwer, Calculation of two-loop QCD corrections for hadronic single top-quark production in the t-channel, Phys. Rev. D 90 (2014) 114024 [arXiv:1409.3654] [INSPIRE].  
[60] E.L. Berger, J. Gao, C.P. Yuan and H.X. Zhu, NNLO QCD corrections to t-channel single top-quark production and decay, Phys. Rev. D 94 (2016) 071501 [arXiv:1606.08463] [INSPIRE].  
[61] E.L. Berger, J. Gao and H.X. Zhu, Differential distributions for t-channel single top-quark production and decay at next-to-  $n$  -th leading order in QCD, JHEP 11 (2017) 158 [arXiv:1708.09405] [INSPIRE].  
[62] G.L. Kane, G.A. Ladinsky and C.P. Yuan, Using the top quark for testing Standard Model polarization and CP predictions, Phys. Rev. D 45 (1992) 124 [INSPIRE].  
[63] J.A. Aguilar-Saavedra, A minimal set of top anomalous couplings, Nucl. Phys. B 812 (2009) 181 [arXiv:0811.3842] [INSPIRE].  
[64] F. Bach and T. Ohl, Anomalous top couplings at hadron colliders revisited, Phys. Rev. D 86 (2012) 114026 [arXiv:1209.4564] [INSPIRE].  
[65] E. Boos, L. Dudko and T. Ohl, Complete calculations of Wbb and Wbb + jet production at Tevatron and LHC: probing anomalous Wtb couplings in single top production, Eur. Phys. J. C 11 (1999) 473 [hep-ph/9903215] [INSPIRE].  
[66] E.E. Boos, V.E. Bunichev, L.V. Dudko, V.I. Savrin and A.V. Sherstnev, Method for simulating electroweak top-quark production events in the NLO approximation: singleTop event generator, Phys. Atom. Nucl. 69 (2006) 1317 [INSPIRE].

[67] E. Boos, V. Bunichev, L. Dudko and M. Perfilov, Modeling of anomalous Wtb interactions in single top quark events using subsidiary fields, Int. J. Mod. Phys. A 32 (2016) 1750008 [arXiv:1607.00505] [INSPIRE].  
[68] A. Giammanco and R. Schwienhorst, *Single top-quark production at the Tevatron and the LHC*, Rev. Mod. Phys. **90** (2018) 035001 [arXiv:1710.10699] [INSPIRE].  
[69] C. Degrande et al., Effective field theory: a modern approach to anomalous couplings, Annals Phys. 335 (2013) 21 [arXiv:1205.4231] [INSPIRE].  
[70] D.R. Green, P. Meade and M.-A. Pleier, Multiboson interactions at the LHC, Rev. Mod. Phys. 89 (2017) 035008 [arXiv:1610.07572] [INSPIRE].  
[71] W. Buchmüller and D. Wyler, Effective Lagrangian analysis of new interactions and flavor conservation, Nucl. Phys. B 268 (1986) 621 [INSPIRE].  
[72] B. Grzadkowski, M. Iskrzynski, M. Misiak and J. Rosiek, Dimension-six terms in the Standard Model Lagrangian, JHEP 10 (2010) 085 [arXiv:1008.4884] [INSPIRE].  
[73] C. Zhang and S. Willenbrock, *Effective-field-theory approach to top-quark production and decay*, Phys. Rev. D **83** (2011) 034006 [arXiv:1008.3869] [INSPIRE].  
[74] C. Zhang, N. Greiner and S. Willenbrock, Constraints on non-standard top quark couplings, Phys. Rev. D 86 (2012) 014024 [arXiv:1201.6670] [INSPIRE].  
[75] R. Romero Aguilar, A.O. Bouzas and F. Larios, Limits on the anomalous Wtq couplings, Phys. Rev. D 92 (2015) 114009 [arXiv:1509.06431] [INSPIRE].  
[76] J.A. Aguilar-Saavedra, *Single top quark production at LHC with anomalous Wtb couplings*, Nucl. Phys. B 804 (2008) 160 [arXiv:0803.3810] [INSPIRE].  
[77] Q.-H. Cao and J. Wudka, Search for new physics via single top production at TeV energy  $e\gamma$  colliders, Phys. Rev. D 74 (2006) 094015 [hep-ph/0608331] [INSPIRE].  
[78] Q.-H. Cao, J. Wudka and C.P. Yuan, Search for new physics via single top production at the LHC, Phys. Lett. B 658 (2007) 50 [arXiv:0704.2809] [INSPIRE].  
[79] Q.-H. Cao, B. Yan, J.-H. Yu and C. Zhang, A general analysis of Wtb anomalous couplings, Chin. Phys. C 41 (2017) 063101 [arXiv:1504.03785] [INSPIRE].  
[80] J.A. Aguilar-Saavedra, C. Degrande and S. Khatibi, Single top polarisation as a window to new physics, Phys. Lett. B 769 (2017) 498 [arXiv:1701.05900] [INSPIRE].  
[81] D. Barducci et al., Interpreting top-quark LHC measurements in the Standard-Model effective field theory, arXiv:1802.07237 [INSPIRE].  
[82] B. Grzadkowski and M. Misiak, Anomalous Wtb coupling effects in the weak radiative  $B$ -meson decay, Phys. Rev. D 78 (2008) 077501 [Erratum ibid. D 84 (2011) 059903] [arXiv:0802.1413] [INSPIRE].  
[83] P.J. Fox, Z. Ligeti, M. Papucci, G. Perez and M.D. Schwartz, Deciphering top flavor violation at the LHC with  $B$  factories, Phys. Rev. D 78 (2008) 054008 [arXiv:0704.1482] [INSPIRE].  
[84] E.E. Jenkins, A.V. Manohar and M. Trot, *Renormalization group evolution of the Standard Model dimension six operators I: formalism and  $\lambda$  dependence*, JHEP **10** (2013) 087 [arXiv:1308.2627] [INSPIRE].

[85] E.E. Jenkins, A.V. Manohar and M. Trot, *Renormalization group evolution of the Standard Model dimension six operators II: Yukawa dependence*, JHEP 01 (2014) 035 [arXiv:1310.4838] [INSPIRE].  
[86] R. Alonso, E.E. Jenkins, A.V. Manohar and M. Trott, Renormalization group evolution of the Standard Model dimension six operators III: gauge coupling dependence and phenomenology, JHEP 04 (2014) 159 [arXiv:1312.2014] [INSPIRE].  
[87] G. Passarino and M. Trot, The Standard Model effective field theory and next to leading order, arXiv:1610.08356 [INSPIRE].  
[88] C. Zhang, Effective field theory approach to top-quark decay at next-to-leading order in QCD, Phys. Rev. D 90 (2014) 014008 [arXiv:1404.1264] [INSPIRE].  
[89] D. Buarque Franzosi and C. Zhang, Probing the top-quark chromomagnetic dipole moment at next-to-leading order in QCD, Phys. Rev. D 91 (2015) 114010 [arXiv:1503.08841] [INSPIRE].  
[90] C. Zhang, Single top production at next-to-leading order in the Standard Model effective field theory, Phys. Rev. Lett. 116 (2016) 162002 [arXiv:1601.06163] [INSPIRE].  
[91] J. Drobnak, S. Fajfer and J.F. Kamenik, New physics in  $t \rightarrow bW$  decay at next-to-leading order in QCD, Phys. Rev. D 82 (2010) 114008 [arXiv:1010.2402] [INSPIRE].  
[92] M. de Beurs, E. Laenen, M. Vreeswijk and E. Vryonidou, Effective operators in t-channel single top production and decay, Eur. Phys. J. C 78 (2018) 919 [arXiv:1807.03576] [INSPIRE].  
[93] Z. Sullivan, Fully differential  $W'$  production and decay at next-to-leading order in QCD, Phys. Rev. D 66 (2002) 075011 [hep-ph/0207290] [INSPIRE].  
[94] D. Duffy and Z. Sullivan, Model independent reach for  $W'$  bosons at the LHC, Phys. Rev. D 86 (2012) 075018 [arXiv:1208.4858] [INSPIRE].  
[95] E. Druke, J. Nutter, R. Schwienhorst, N. Vignaroli, D.G.E. Walker and J.-H. Yu, Single top production as a probe of heavy resonances, Phys. Rev. D 91 (2015) 054020 [arXiv:1409.7607] [INSPIRE].  
[96] A. Alloul, N.D. Christensen, C. Degrande, C. Duhr and B. Fuks, *FeynRules* 2.0 — a complete toolbox for tree-level phenomenology, *Comput. Phys. Commun.* **185** (2014) 2250 [arXiv:1310.1921] [INSPIRE].  
[97] I. Brivio, Y. Jiang and M. Trot, The SMEFTsim package, theory and tools, JHEP 12 (2017) 070 [arXiv:1709.06492] [INSPIRE].  
[98] R. Mertig, M. Böhm and A. Denner, FEYN CALC: computer algebraic calculation of Feynman amplitudes, Comput. Phys. Commun. 64 (1991) 345 [INSPIRE].  
[99] V. Shtabovenko, R. Mertig and F. Orellana, New developments in FeynCalc 9.0, Comput. Phys. Commun. 207 (2016) 432 [arXiv:1601.01167] [INSPIRE].  
[100] Wolfram Research Inc., *Mathematica*, version 11.2, U.S.A. (2017).  
[101] O.V. Tarasov, Connection between Feynman integrals having different values of the space-time dimension, Phys. Rev. D 54 (1996) 6479 [hep-th/9606018] [INSPIRE].  
[102] P. Maierhöfer, J. Usovitsch and P. Uwer, *Kira — a Feynman integral reduction program*, Comput. Phys. Commun. **230** (2018) 99 [arXiv:1705.05610] [INSPIRE].

[103] R.K. Ellis and G. Zanderighi, Scalar one-loop integrals for QCD, JHEP 02 (2008) 002 [arXiv:0712.1851] [INSPIRE].  
[104] S. Carrazza, R.K. Ellis and G. Zanderighi, QCDLoop: a comprehensive framework for one-loop scalar integrals, Comput. Phys. Commun. 209 (2016) 134 [arXiv:1605.03181] [INSPIRE].  
[105] P. Nogueira, Automatic Feynman graph generation, J. Comput. Phys. 105 (1993) 279 [INSPIRE].  
[106] J.A.M. Vermaseren, New features of FORM, math-ph/0010025 [INSPIRE].  
[107] M. Tentyukov and J. Fleischer, A Feynman diagram analyzer DIANA, Comput. Phys. Commun. 132 (2000) 124 [hep-ph/9904258] [INSPIRE].  
[108] A.V. Semenov, *LanHEP: a package for automatic generation of Feynman rules in gauge models*, hep-ph/9608488 [INSPIRE].  
[109] A.V. Semenov, LanHEP: a package for automatic generation of Feynman rules in field theory. Version 2.0, hep-ph/0208011 [INSPIRE].  
[110] A. Semenov, LanHEP: a package for the automatic generation of Feynman rules in field theory. Version 3.0, Comput. Phys. Commun. 180 (2009) 431 [arXiv:0805.0555] [INSPIRE].  
[111] A. Semenov, *LanHEP: a package for automatic generation of Feynman rules from the Lagrangian*. Version 3.2, Comput. Phys. Commun. **201** (2016) 167 [arXiv:1412.5016] [INSPIRE].  
[112] A. Dedes, W. Materkowska, M. Paraskevas, J. Rosiek and K. Suxho, *Feynman rules for the Standard Model effective field theory in  $R_{\xi}$ -gauges*, JHEP 06 (2017) 143 [arXiv:1704.03888] [INSPIRE].  
[113] J.C. Romao and J.P. Silva, A resource for signs and Feynman diagrams of the Standard Model, Int. J. Mod. Phys. A 27 (2012) 1230025 [arXiv:1209.6213] [INSPIRE].  
[114] D. Maitre and P. Mastrolia,  $S@M$ , a Mathematica implementation of the spinor-helicity formalism, Comput. Phys. Commun. 179 (2008) 501 [arXiv:0710.5559] [INSPIRE].  
[115] R.H. Lewis, Fermat, a computer algebra system for polynomial and matrix computation, http://home.bway.net/lewis/home.html.  
[116] M. Prausa, *Mathematica interface to Fermat*, https://github.com/mprausa/mmaFermat, (2017).  
[117] E. Byckling and K. Kajantie, Particle kinematics, University of Jyvaskyla, Jyvaskyla, Finland (1971).  
[118] P. Maierhöfer and J. Usovitsch, *Kira 1.2 release notes*, arXiv:1812.01491 [INSPIRE].  
[119] Y. Hida, X.S. Li and D.H. Bailey, Quad double computation package, (2003)-(2018).  
[120] T. Huber and D. Maitre, HypExp: a Mathematica package for expanding hypergeometric functions around integer-valued parameters, Comput. Phys. Commun. 175 (2006) 122 [hep-ph/0507094] [INSPIRE].  
[121] M. Jezabek and J.H. Kuhn, QCD corrections to semileptonic decays of heavy quarks, Nucl. Phys. B 314 (1989) 1 [INSPIRE].

[122] S. Catani and M.H. Seymour, A general algorithm for calculating jet cross-sections in NLO QCD, Nucl. Phys. B 485 (1997) 291 [Erratum ibid. B 510 (1998) 503] [hep-ph/9605323] [INSPIRE].  
[123] Z. Nagy and Z. Trócsányi, Next-to-leading order calculation of four jet observables in electron positron annihilation, Phys. Rev. D 59 (1999) 014020 [Erratum ibid. D 62 (2000) 099902] [hep-ph/9806317] [INSPIRE].  
[124] Z. Nagy, Next-to-leading order calculation of three jet observables in hadron hadron collision, Phys. Rev. D 68 (2003) 094002 [hep-ph/0307268] [INSPIRE].  
[125] S. Dulat et al., New parton distribution functions from a global analysis of quantum chromodynamics, Phys. Rev. D 93 (2016) 033006 [arXiv:1506.07443] [INSPIRE].  
[126] A. Aeppli, G.J. van Oldenborgh and D. Wyler, Unstable particles in one loop calculations, Nucl. Phys. B 428 (1994) 126 [hep-ph/9312212] [INSPIRE].  
[127] V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Constraining the top-Higgs sector of the Standard Model effective field theory, Phys. Rev. D 94 (2016) 034031 [arXiv:1605.04311] [INSPIRE].  
[128] J. Boudreau, C. Escobar, J. Mueller, K. Sapp and J. Su, Single top quark differential decay rate formulae including detector effects, arXiv:1304.5639 [INSPIRE].  
[129] S. Alioli, V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Right-handed charged currents in the era of the Large Hadron Collider, JHEP 05 (2017) 086 [arXiv:1703.04751] [INSPIRE].  
[130] ATLAS collaboration, Search for anomalous couplings in the Wtb vertex from the measurement of double differential angular decay rates of single top quarks produced in the t-channel with the ATLAS detector, JHEP 04 (2016) 023 [arXiv:1510.03764] [INSPIRE].  
[131] J. Ellis, TikZ-Feynman: Feynman diagrams with TikZ, Comput. Phys. Commun. 210 (2017) 103 [arXiv:1601.05437] [INSPIRE].