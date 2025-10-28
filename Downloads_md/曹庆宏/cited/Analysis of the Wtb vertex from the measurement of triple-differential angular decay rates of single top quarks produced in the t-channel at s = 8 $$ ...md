# Analysis of the Wtb vertex from the measurement of triple-differential angular decay rates of single top quarks produced in the  $t$ -channel at  $\sqrt{s} = 8$  TeV with the ATLAS detector

![](images/df3b149a2a71c8493e4fa184b24bb083372b73673eff9af36013b064a3795b96.jpg)

# The ATLAS collaboration

E-mail: atlas.publications@cern.ch

ABSTRACT: The electroweak production and subsequent decay of single top quarks in the  $t$ -channel is determined by the properties of the Wtb vertex, which can be described by the complex parameters of an effective Lagrangian. An analysis of a triple-differential decay rate in  $t$ -channel production is used to simultaneously determine five generalised helicity fractions and phases, as well as the polarisation of the produced top quark. The complex parameters are then constrained. This analysis is based on  $20.2\mathrm{fb}^{-1}$  of proton-proton collision data at a centre-of-mass energy of 8 TeV collected with the ATLAS detector at the LHC. The fraction of decays containing transversely polarised  $W$  bosons is measured to be  $f_{1} = 0.30 \pm 0.05$ . The phase between amplitudes for transversely and longitudinally polarised  $W$  bosons recoiling against left-handed  $b$ -quarks is measured to be  $\delta_{-} = 0.002\pi_{+0.017\pi}^{+0.016\pi}$ , giving no indication of CP violation. The fractions of longitudinal or transverse  $W$  bosons accompanied by right-handed  $b$ -quarks are also constrained. Based on these measurements, limits are placed at  $95\%$  CL on the ratio of the complex coupling parameters  $\mathrm{Re}[g_{\mathrm{R}} / V_{\mathrm{L}} \in [-0.12, 0.17]$  and  $\mathrm{Im}[g_{\mathrm{R}} / V_{\mathrm{L}} \in [-0.07, 0.06]$ . Constraints are also placed on the ratios  $|V_{\mathrm{R}} / V_{\mathrm{L}}|$  and  $|g_{\mathrm{L}} / V_{\mathrm{L}}|$ . In addition, the polarisation of single top quarks in the  $t$ -channel is constrained to be  $P > 0.72$  (95% CL). None of the above measurements make assumptions about the value of any of the other parameters or couplings and all of them are in agreement with the Standard Model.

KEYWORDS: Electroweak interaction, Hadron-Hadron scattering (experiments), Top physics

ARXIV EPRINT: 1707.05393

# Contents

1 Introduction 1  
2 Triple-differential decay rate of polarised single top quarks 5  
3ATLAS detector 8  
4 Data and simulation samples 9  
5 Event reconstruction 11  
6 Event selection in the signal, control, and validation regions 12  
7 Background estimation and normalisation 14  
8 Event yields and kinematic distributions 17  
9 Analysis of angular distributions 18  
10 Sources of systematic uncertainty 25  
11 Results 28  
12 Conclusion 35  
The ATLAS collaboration 43

# 1 Introduction

The top quark is the heaviest known fundamental particle, making the measurement of its production and decay kinematic properties an important probe of physical processes beyond the Standard Model (SM). Within the SM, the top quark decays predominantly through the electroweak interaction to an on-shell  $W$  boson and a  $b$ -quark. Due to its large mass [1], its lifetime  $\mathcal{O}(10^{-25}\mathrm{s})$  is smaller than its hadronisation time-scale  $\mathcal{O}(10^{-24}\mathrm{s})$ , allowing this quark to be studied as a free quark. Since the top-quark lifetime is also shorter than the depolarisation timescale  $\mathcal{O}(10^{-21}\mathrm{s})$  [2] and the  $W$  boson is produced on-shell in the top-quark decay, the top-quark spin information is directly transferred to its decay products. Comparing angular measurements of the decay products of polarised top quarks with precise SM predictions provides a unique way to study the non-SM couplings in the Wtb vertex [3]. The normalised triple-differential cross-section (to be defined in section 2) is the joint probability distribution in all three of the angles determining the

kinematics of the decay  $t \to Wb$  from a polarised initial state. Its analysis is the most complete investigation of the dynamics of top-quark decay undertaken to date.

At hadron colliders, top quarks are produced predominantly in pairs  $(tt)$  via the flavour-conserving strong interaction, while an alternative process produces single top quarks through the electroweak interaction. Although the  $tt$  production cross-section is larger than that of single-top-quark production, top quarks are produced unpolarised because of parity conservation in quantum chromodynamics (QCD) [4], contrary to what happens for single top quarks. At the Large Hadron Collider (LHC) [5], in proton-proton  $(pp)$  collision data, the  $t$ -channel is the dominant process for producing single top quarks used for the measurements presented in this paper. Figure 1 shows the two representative leading-order (LO) Feynman diagrams for  $t$ -channel single-top-quark production. In these two diagrams, a light-flavour quark  $q$  (i.e.  $u-$  or  $\bar{d}$ -quark) from one of the colliding protons interacts with a  $b$ -quark by exchanging a virtual  $W$  boson, producing a top quark  $t$  and a recoiling light-flavour quark  $q'$ , called the spectator quark. The  $b$ -quark comes either directly from another colliding proton in the five-flavour scheme (5FS) or  $2 \rightarrow 2$  process (a) or from a gluon splitting in the four-flavour scheme<sup>1</sup> (4FS) or  $2 \rightarrow 3$  process (b). In  $pp$  collisions at  $\sqrt{s} = 8$  TeV, the predicted  $t$ -channel production cross-section using the 5FS is  $87.8_{-1.9}^{+3.4}\mathrm{pb}$  [6], calculated at next-to-leading order (NLO) in QCD with resummed next-to next-to-leading logarithmic (NNLL) accuracy, and called approximate next-to next-to-leading order (NNLO) in the following. The calculation assumes a top-quark mass of 172.5 GeV and uses the MSTW2008 NNLO [7, 8] parton distribution function (PDF) set. The uncertainties correspond to the sum in quadrature of the uncertainty obtained from the MSTW2008 NNLO PDF set at the 90% confidence level (CL) and the factorisation and renormalisation scale uncertainties.

As a consequence of the vector-axial (V-A) form of the Wtb vertex in the SM, the spin of single top quarks in  $t$ -channel production is predominantly aligned along the direction of the spectator-quark momentum [9].

Probes of new physics phenomena affecting the production or decay of the top quark can be parameterised with a series of effective couplings at each vertex [10, 11]; in the  $t$ -channel single-top-quark production, both production and decay proceed through the Wtb vertex, and thus are sensitive to the same set of effective couplings.

New physics can be described by an effective Lagrangian,  $\mathcal{L}_{\mathrm{eff}}$ , represented by dimension-five and dimension-six operators in the framework of effective field theory [12, 13]

$$
\mathcal {L} _ {\mathrm {e f f}} = \mathcal {L} _ {\mathrm {S M}} + \frac {1}{\Lambda_ {\mathrm {N P}}} \mathcal {L} _ {5} + \frac {1}{\Lambda_ {\mathrm {N P}} ^ {2}} \mathcal {L} _ {6} + \dots ,
$$

where  $\mathcal{L}_{\mathrm{SM}}$  represents the SM Lagrangian of dimension four,  $\mathcal{L}_5$  and  $\mathcal{L}_6$  represent the contributions from dimension-five and dimension-six operators invariant under the SM gauge symmetry, and  $\Lambda_{\mathrm{NP}}$  is a new physics scale chosen such that higher-dimension operators are sufficiently suppressed by higher powers of  $\Lambda_{\mathrm{NP}}$ . Of the standardised set of operators reported in ref. [12], only four operators, which are dimension six, contribute independently

![](images/c4262b16cd8633e4c98021eefd63798765842fd9ec1695cf30fe98af4db83a8e.jpg)  
(a) 5FS  $(2\rightarrow 2$  process)

![](images/3576818a3de64c35080ecf87f37509d18090815055258e5d8619cf6fbb273dbe.jpg)  
Figure 1. Representative LO Feynman diagrams for  $t$ -channel single-top-quark production and decay. Here  $q$  represents a  $u-$  or  $\bar{d}$ -quark, and  $q'$  represents (a) a  $d-$  or  $\bar{u}$ -quark, respectively, in which the initial  $b$ -quark arises from a sea  $b$ -quark in the 5FS or  $2 \rightarrow 2$  process, or (b) a gluon splitting into a  $b\bar{b}$  pair in the 4FS or  $2 \rightarrow 3$  process.  
(b) 4FS  $(2\rightarrow 3$  process)

to the Wtb vertex at LO, allowing these terms to be analysed separately from the rest of the full set of possible operators. In a general Lorentz-covariant Lagrangian, expressed by refs. [10, 11], corrections to the vertex are absorbed into four non-renormalisable effective complex couplings called anomalous couplings:

$$
\mathcal {L} _ {\mathrm {e f f}} = - \frac {g}{\sqrt {2}} \bar {b} \gamma^ {\mu} \left(V _ {\mathrm {L}} P _ {\mathrm {L}} + V _ {\mathrm {R}} P _ {\mathrm {R}}\right) t W _ {\mu} ^ {-} - \frac {g}{\sqrt {2}} \bar {b} \frac {i \sigma^ {\mu \nu} q _ {\nu}}{m _ {W}} \left(g _ {\mathrm {L}} P _ {\mathrm {L}} + g _ {\mathrm {R}} P _ {\mathrm {R}}\right) t W _ {\mu} ^ {-} + \mathrm {h . c .},
$$

where the four complex effective couplings  $V_{\mathrm{L,R}}$ ,  $g_{\mathrm{L,R}}$  can be identified with the dimension-six operators' Wilson coefficients [14]. Here,  $g$  is the weak coupling constant, and  $m_W$  and  $q_\nu$  are the mass and the four-momentum of the  $W$  boson. The terms  $P_{\mathrm{L,R}} \equiv \left(1 \mp \gamma^5\right) / 2$  are the left- and right-handed projection operators and  $\sigma^{\mu \nu} = i[\gamma^{\mu},\gamma^{\nu}] / 2$ . The terms  $V_{\mathrm{L,R}}$  and  $g_{\mathrm{L,R}}$  are the left- and right-handed vector and tensor complex couplings, respectively. In the SM at LO, all coupling constants vanish, except  $V_{\mathrm{L}} = V_{tb}$ , which is a quark-mixing element in the Cabibbo-Kobayashi-Maskawa (CKM) matrix. Deviations from these values would provide hints of physics beyond the SM, and furthermore, complex values could imply that the top-quark decay has a CP-violating component [15-19].

Indirect constraints on  $V_{\mathrm{L}}$ ,  $V_{\mathrm{R}}$ ,  $g_{\mathrm{L}}$ , and  $g_{\mathrm{R}}$  were obtained [20, 21] from precision measurements of  $B$ -meson decays. These results yield constraints in a six-dimensional space of operator coefficients, where four of them correspond to Wtb couplings. Considering one coefficient at a time results in very tight constraints on a particular combination of  $V_{\mathrm{R}}$  and  $g_{\mathrm{L}}$ , but if several coefficients are allowed to move simultaneously, then individual bounds are not possible. Very tight constraints on CP-violating interactions have been derived from measurements of electric dipole moments [22]. Those constraints also depend on combinations of couplings, and in a global fit [23], cannot constrain Im  $[g_{\mathrm{R}}]$  better than direct measurements, as are presented here. Measurements of the  $W$  boson helicity fractions in top-quark decays [24-28] are sensitive to the magnitude of combinations of anomalous couplings, which are assumed to be purely real, corresponding to the CP-conserving case.

These measurements can only place limits on combinations of couplings, and thus the quoted limits on individual couplings depend on the assumptions made about other couplings while  $V_{\mathrm{L}}$  is fixed to the SM value of one. More stringent limits are set either in these analyses on  $\operatorname{Re}[g_{\mathrm{R}}]$  by considering the measurements of the  $t$ -channel single-top-quark production cross-section [29-31] or by performing a global fit considering the most precise measurements of the  $W$  boson helicity fractions at the LHC combined with measurements of single-top-quark production cross-sections for different centre-of-mass energies at the LHC and Tevatron [32]. Direct searches for anomalous couplings in  $t$ -channel single-top-quark events set limits simultaneously on either both  $\operatorname{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}]$  and  $\operatorname{Im}[g_{\mathrm{R}} / V_{\mathrm{L}}]$  [33, 34], or on pairs of couplings [35]. In both cases, analyses assume SM values for the other anomalous couplings.

The goal of this analysis is to simultaneously constrain the full space of parameters governing the Wtb vertex using the triple-differential angular decay rate of single top quarks produced in the  $t$ -channel as discussed in section 2, in which the  $W$  boson from the top quark subsequently decays leptonically. Conceptually, this is a measurement of each of the anomalous coupling parameters  $V_{\mathrm{L,R}}$  and  $g_{\mathrm{L,R}}$  plus the polarisation  $P$  of the top quark, with a full covariance matrix; however, any likelihood function derived from the triple-differential decay rate possesses invariances and/or parameter space boundaries lying quite near to the SM point. Therefore, contours are presented instead, with only  $\operatorname{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  and  $\operatorname{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  showing approximate elliptical contours and therefore admitting point estimation. The anomalous couplings  $V_{\mathrm{R}}$ ,  $g_{\mathrm{L}}$  and  $g_{\mathrm{R}}$  are allowed to be complex and the measurements shown require no assumptions to be made regarding the other anomalous couplings. The analysis is carried out in a Fourier-dual space of coefficients in an angular expansion [36, 37]. This method is chosen because it permits an analytic deconvolution of detector effects including both resolution and efficiency, while permitting a simultaneous determination of the real and imaginary parts of all of the anomalous couplings at the Wtb vertex, in addition to the polarisation of the top quark produced in the  $t$ -channel.

This paper is organised as follows. Section 2 defines the coordinate system and parameterisation used in the measurement and the triple-differential formalism applied to polarised single top quarks. Section 3 gives a short description of the ATLAS detector, then section 4 describes the data samples as well as the simulated event samples used to predict properties of the  $t$ -channel signal and background processes. Section 5 describes the event reconstruction for the identification of  $t$ -channel events, while section 6 presents the criteria to define the signal region as well as the control and validation regions. The procedures for modelling background processes are reported in section 7. The event yields and angular distributions comparing the predictions and the observed data are shown in section 8. Section 9 describes the efficiency, resolution, and background models used to translate the distribution of true  $t$ -channel signal events to the distribution of reconstructed signal and background events, and how the parameters of the model are estimated. Section 10 quantifies the sources of uncertainty important in this measurement. Section 11 presents the resulting central value and covariance matrix for the model parameters and the ratios  $\mathrm{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  and  $\mathrm{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$ , and the conclusions are given in section 12.

![](images/47e47073b3a9bedaefbc14fc277eb8bf8cac1036e417edb985b03f20294d28b3.jpg)  
Figure 2. Definition of the right-handed coordinate system with  $\hat{x}$ ,  $\hat{y}$ , and  $\hat{z}$  defined as shown from the momentum directions of the  $W$  boson,  $\hat{q} \equiv \hat{z}$ , and the spectator quark,  $\hat{p}_{\mathrm{s}}$  with  $\hat{y} = \hat{p}_{\mathrm{s}} \times \hat{q}$ , in the top-quark rest frame. The angles  $\theta^{*}$  and  $\phi^{*}$  indicate the direction of the lepton momentum,  $\hat{p}_{\ell}^{*}$ , while the angle  $\theta$  indicates the direction of the spectator-quark momentum,  $\hat{p}_{\mathrm{s}}$ , in this coordinate system.

# 2 Triple-differential decay rate of polarised single top quarks

An event-specific coordinate system is defined for analysing the decay of the top quark in its rest frame, using the directions of the spectator quark  $q'$  that recoils against the top quark, the  $W$  boson from the top-quark decay, and the lepton  $\ell$  ( $e, \mu$  or  $\tau$ ) from the  $W$  boson decay, in the final state depicted in figure 2. The  $\hat{z}$ -axis is chosen along the direction of the  $W$  boson momentum,  $\vec{q}$ , or equivalently along the direction opposite to the  $b$ -quark momentum, boosted into the top-quark rest frame,  $\hat{z} \equiv \hat{q} = \vec{q} / |\vec{q}|$ . The reconstruction of the  $W$  boson and top quark is discussed in section 6. As mentioned before, the spin of single top quarks,  $\vec{s}_t$ , in  $t$ -channel production is predominantly aligned along the direction of the spectator-quark momentum,  $\vec{p}_{\mathrm{s}}$ , in the top-quark rest frame,  $\hat{p}_{\mathrm{s}} = \vec{p}_{\mathrm{s}} / |\vec{p}_{\mathrm{s}}|$  [9]. If this quark defines the spin-analysing direction, the degree of polarisation is shown in refs. [3, 38, 39] to be  $P \equiv \hat{p}_{\mathrm{s}} \cdot \vec{s}_t / |\vec{s}_t| \approx 0.9$  at  $\sqrt{s} = 8$  TeV for SM couplings. A three-dimensional right-handed coordinate system is defined from the  $\hat{q} - \hat{p}_{\mathrm{s}}$  plane and the perpendicular direction, with  $\hat{y} = \hat{p}_{\mathrm{s}} \times \hat{q}$  and  $\hat{x} = \hat{y} \times \hat{q}$ . In this coordinate system, the direction of the lepton momentum,  $\vec{p}_{\ell}^{*}$ , in the  $W$  boson rest frame,  $\hat{p}_{\ell}^{*} = \vec{p}_{\ell}^{*} / |\vec{p}_{\ell}^{*}|$ , is specified by the polar angle  $\theta^{*}$  and the azimuthal angle  $\phi^{*}$ . The third angle  $\theta$  is defined as the angle between  $\hat{p}_{\mathrm{s}}$  and  $\hat{q}$ . The angle  $\theta^{*}$  is the same angle used to measure the  $W$  boson helicity fractions in top-quark decays [24-28].

These three angles,  $\theta$ ,  $\theta^{*}$ , and  $\phi^{*}$ , arise as a natural choice for measuring a triple-differential distribution for the decay of the top quark, where the  $W$  boson subsequently

decays leptonically. The  $t \to Wb$  transition is determined by four helicity amplitudes,  $A_{\lambda_W,\lambda_b}$ , where  $\lambda_W$  and  $\lambda_b$  are the helicities of the  $W$  boson and the  $b$ -quark, respectively [36]. For  $\lambda_b = \frac{1}{2}$ , only the  $W$  boson helicities  $\lambda_W = 1,0$  are possible, while for  $\lambda_b = -\frac{1}{2}$ ,  $\lambda_W = -1,0$  are possible. The angular dependence of these transition amplitudes is given in ref. [36]. At LO and neglecting the  $b$ -quark mass, the helicity amplitudes have a simple dependence on the anomalous couplings. Up to a common proportionality constant, the magnitudes can be expressed as

$$
\left| A _ {1, \frac {1}{2}} \right| ^ {2} \propto 2 \left| x _ {W} V _ {\mathrm {R}} - g _ {\mathrm {L}} \right| ^ {2},
$$

$$
\left| A _ {0, \frac {1}{2}} \right| ^ {2} \propto \left| V _ {\mathrm {R}} - x _ {W} g _ {\mathrm {L}} \right| ^ {2},
$$

$$
\left| A _ {- 1, - \frac {1}{2}} \right| ^ {2} \propto 2 \left| x _ {W} V _ {\mathrm {L}} - g _ {\mathrm {R}} \right| ^ {2},
$$

$$
\left| A _ {0, - \frac {1}{2}} \right| ^ {2} \propto \left| V _ {\mathrm {L}} - x _ {W} g _ {\mathrm {R}} \right| ^ {2},
$$

where  $x_{W} = m_{W} / m_{t}$ . The relative phases between  $A_{1,\frac{1}{2}}$  and  $A_{0,\frac{1}{2}}$  and between  $A_{-1, -\frac{1}{2}}$  and  $A_{0, -\frac{1}{2}}$  are determined by the relative phases between  $V_{\mathrm{R}}$  and  $g_{\mathrm{L}}$  and between  $V_{\mathrm{L}}$  and  $g_{\mathrm{R}}$ , respectively.

From the four helicity amplitudes, three fractions can be independently determined. In addition, the interference allows two relative phases between amplitudes to be experimentally determined. These are called the generalised helicity fractions and phases [33, 36]:

-  $f_{1}$ , the fraction of decays containing transversely polarised  $W$  bosons,

$$
f _ {1} = \frac {\left| A _ {1 , \frac {1}{2}} \right| ^ {2} + \left| A _ {- 1 , - \frac {1}{2}} \right| ^ {2}}{\left| A _ {1 , \frac {1}{2}} \right| ^ {2} + \left| A _ {- 1 , - \frac {1}{2}} \right| ^ {2} + \left| A _ {0 , \frac {1}{2}} \right| ^ {2} + \left| A _ {0 , - \frac {1}{2}} \right| ^ {2}},
$$

-  $f_1^+$ , the fraction of  $b$ -quarks that are right-handed in events with transversely polarised  $W$  bosons,

$$
f _ {1} ^ {+} = \frac {\left| A _ {1 , \frac {1}{2}} \right| ^ {2}}{\left| A _ {1 , \frac {1}{2}} \right| ^ {2} + \left| A _ {- 1 , - \frac {1}{2}} \right| ^ {2}},
$$

-  $f_0^+$ , the fraction of  $b$ -quarks that are right-handed in events with longitudinally polarised  $W$  bosons,

$$
f _ {0} ^ {+} = \frac {\left| A _ {0 , \frac {1}{2}} \right| ^ {2}}{\left| A _ {0 , \frac {1}{2}} \right| ^ {2} + \left| A _ {0 , - \frac {1}{2}} \right| ^ {2}},
$$

-  $\delta_{+}$ , the phase between amplitudes for longitudinally polarised and transversely polarised  $W$  bosons recoiling against right-handed  $b$ -quarks,

$$
\delta_ {+} = \arg \left(A _ {1, \frac {1}{2}} A _ {0, \frac {1}{2}} ^ {*}\right),
$$

-  $\delta_{-}$ , the phase between amplitudes for longitudinally polarised and transversely polarised  $W$  bosons recoiling against left-handed  $b$ -quarks,

$$
\delta_ {-} = \arg \left(A _ {- 1, - \frac {1}{2}} A _ {0, - \frac {1}{2}} ^ {*}\right).
$$

The fractions  $f_{1}$  and  $f_{1}^{+}$  are related to the quantities  $F_{\mathrm{R}}$ ,  $F_{0}$ , and  $F_{\mathrm{L}}$  determined by measurements of the  $W$  boson helicity fractions in top-quark decays [24-28], with  $F_{\mathrm{R}} = f_{1}f_{1}^{+}$ ,  $F_{0} = 1 - f_{1}$ , and  $F_{\mathrm{L}} = f_{1}(1 - f_{1}^{+})$ . The fraction  $f_{0}^{+}$  is previously unmeasured.

For convenience in what follows,  $\vec{\alpha}$  is defined as  $\vec{\alpha} \equiv \{f_1, f_1^+, f_0^+, \delta_+, \delta_-\}$ . From these five experimental observables, plus the relationships between the helicity amplitudes and the anomalous couplings, one can obtain constraints on all the couplings simultaneously. Additionally, the top-quark polarisation,  $P$ , is considered separately from  $\vec{\alpha}$  because it depends on the production of the top quark, rather than on its decay.

At LO, the helicity amplitudes, and hence  $\vec{\alpha}$  can be expressed as functions of the couplings and the parton masses [19, 40]. Using SM couplings and  $m_{b} = 4.95\mathrm{GeV}$ ,  $m_{t} = 172.5\mathrm{GeV}$ , and  $m_{W} = 80.399\mathrm{GeV}$  with the derived analytic expressions for  $\vec{\alpha}$ , the expected values are

$$
f _ {1} = 0. 3 0 4, \qquad f _ {1} ^ {+} = 0. 0 0 1, \qquad f _ {0} ^ {+} = 6 \cdot 1 0 ^ {- 5}, \qquad \delta_ {+} = \delta_ {-} = 0. 0.
$$

Calculations at NNLO [41] predict  $f_{1} = 0.311 \pm 0.005$ , and  $f_{1}^{+} = 0.0054 \pm 0.0003$ , where the largest part of the uncertainty in  $f_{1}$  comes from the experimental uncertainty of the top-quark mass, while for  $f_{1}^{+}$  it arises from uncertainties in  $\alpha_{\mathrm{s}}$  and the  $b$ -quark mass. An NNLO prediction does not yet exist for  $f_{0}^{+}$ , but NLO calculations [40] yield a value  $< 0.001$ .

In refs. [36, 37] it is shown that the Jacob-Wick helicity formalism [42, 43] applied to the decay of polarised top quarks in  $t$ -channel production leads to the following expression for the triple-differential decay rate for polarised top quarks in terms of the three angles  $(\theta, \theta^{*}$ , and  $\phi^{*}$ ) and the top-quark polarisation,

$$
\begin{array}{l} \varrho (\theta , \theta^ {*}, \phi^ {*}; P) = \frac {1}{N} \frac {\mathrm {d} ^ {3} N}{\mathrm {d} (\cos \theta) \mathrm {d} \Omega^ {*}} = \frac {1}{8 \pi} \left\{\frac {3}{4} \left| A _ {1, \frac {1}{2}} \right| ^ {2} (1 + P \cos \theta) (1 + \cos \theta^ {*}) ^ {2} \right. \\ + \frac {3}{4} \left| A _ {- 1, - \frac {1}{2}} \right| ^ {2} (1 - P \cos \theta) (1 - \cos \theta^ {*}) ^ {2} \\ + \frac {3}{2} \left(\left| A _ {0, \frac {1}{2}} \right| ^ {2} (1 - P \cos \theta) + \left| A _ {0, - \frac {1}{2}} \right| ^ {2} (1 + P \cos \theta)\right) \sin^ {2} \theta^ {*} \\ - \frac {3 \sqrt {2}}{2} P \sin \theta \sin \theta^ {*} (1 + \cos \theta^ {*}) \mathrm {R e} \left[ e ^ {i \phi^ {*}} A _ {1, \frac {1}{2}} A _ {0, \frac {1}{2}} ^ {*} \right] \\ \left. \right.\left. - \frac {3 \sqrt {2}}{2} P \sin \theta \sin \theta^ {*} (1 - \cos \theta^ {*}) \operatorname {R e} \left[ e ^ {- i \phi^ {*}} A _ {- 1, - \frac {1}{2}} A _ {0, - \frac {1}{2}} ^ {*} \right]\right\} \\ = \sum_ {k = 0} ^ {1} \sum_ {l = 0} ^ {2} \sum_ {m = - k} ^ {k} a _ {k, l, m} M _ {k, l} ^ {m} \left(\theta , \theta^ {*}, \phi^ {*}\right), \tag {2.1} \\ \end{array}
$$

where  $\mathrm{d}\Omega^{*} \equiv \mathrm{d}(\cos \theta^{*})\mathrm{d}\phi^{*}$  (see figure 2). The  $a_{k,l,m}$  represent the angular coefficients to be determined and  $M_{k,l}^{m}(\theta, \theta^{*}, \phi^{*})$  are orthonormal functions over the three angles defined by

the product of two spherical harmonics,  $Y_{k}^{m}(\theta ,0)$  and  $Y_{l}^{m}(\theta^{*},\phi^{*})$ ,

$$
M _ {k, l} ^ {m} (\theta , \theta^ {*}, \phi^ {*}) = \sqrt {2 \pi} Y _ {k} ^ {m} (\theta , 0) Y _ {l} ^ {m} (\theta^ {*}, \phi^ {*}).
$$

The properties of these  $M$ -functions are detailed in ref. [37]. The restriction to  $k \leq 1$  and  $l \leq 2$  in eq. (2.1) is caused by the allowed spin states of the initial- and final-state fermions and the vector boson at the weak vertex.

Only nine of the angular coefficients  $a_{k,l,m}$ , not taking into account  $a_{0,0,0}$ , which is constrained by normalisation  $(|A_{1,\frac{1}{2}}|^2 + |A_{0,\frac{1}{2}}|^2 + |A_{-1, -\frac{1}{2}}|^2 + |A_{0, -\frac{1}{2}}|^2 = 1)$ , are non-zero and can be parameterised in terms of the generalised helicity fractions and phases.

The non-zero angular coefficients  $a_{k,l,m}(\vec{\alpha};P)$  are:

$$
a _ {0, 0, 0} = \frac {1}{\sqrt {8 \pi}}, \tag {2.2}
$$

$$
a _ {0, 1, 0} = \frac {\sqrt {3}}{\sqrt {8 \pi}} f _ {1} \left(f _ {1} ^ {+} - \frac {1}{2}\right),
$$

$$
a _ {0, 2, 0} = \frac {1}{\sqrt {4 0 \pi}} \left(\frac {3}{2} f _ {1} - 1\right),
$$

$$
a _ {1, 0, 0} = + P \frac {1}{\sqrt {2 4 \pi}} \left(f _ {1} (2 f _ {1} ^ {+} - 1) + (1 - f _ {1}) (1 - 2 f _ {0} ^ {+})\right),
$$

$$
a _ {1, 1, 0} = + P \frac {1}{\sqrt {3 2 \pi}} f _ {1},
$$

$$
a _ {1, 2, 0} = + P \frac {1}{\sqrt {4 8 0 \pi}} \left(f _ {1} (2 f _ {1} ^ {+} - 1) - 2 (1 - f _ {1}) (1 - 2 f _ {0} ^ {+})\right),
$$

$$
a _ {1, 1, 1} = (a _ {1, 1, - 1}) ^ {*} = - P \frac {1}{\sqrt {1 6 \pi}} \sqrt {f _ {1} (1 - f _ {1})} \left\{\sqrt {f _ {1} ^ {+} f _ {0} ^ {+}} \mathrm {e} ^ {i \delta_ {+}} + \sqrt {(1 - f _ {1} ^ {+}) (1 - f _ {0} ^ {+})} \mathrm {e} ^ {- i \delta_ {-}} \right\},
$$

$$
a _ {1, 2, 1} = (a _ {1, 2, - 1}) ^ {*} = - P \frac {1}{\sqrt {8 0 \pi}} \sqrt {f _ {1} (1 - f _ {1})} \left\{\sqrt {f _ {1} ^ {+} f _ {0} ^ {+}} \mathrm {e} ^ {i \delta_ {+}} - \sqrt {(1 - f _ {1} ^ {+}) (1 - f _ {0} ^ {+})} \mathrm {e} ^ {- i \delta_ {-}} \right\},
$$

where  $(a_{k,l,m})^*$  represents a complex conjugate. All the other angular coefficients are zero in top-quark decays.

Coefficients of  $M$ -functions can also be determined from data. In section 9, techniques are discussed for measuring those coefficients, how to deconvolve them to obtain the coefficients presented here, and hence the parameters  $\vec{\alpha}$  and  $P$ .

# 3 ATLAS detector

The ATLAS detector [44] consists of a set of sub-detector systems, cylindrical in the central region and planar in the two endcap regions, that covers almost the full solid angle around the interaction point (IP).<sup>2</sup> ATLAS is composed of an inner detector (ID) for tracking close

to the IP, surrounded by a superconducting solenoid providing a 2 T axial magnetic field, electromagnetic (EM) and hadronic calorimeters, and a muon spectrometer (MS). The ID consists of a silicon pixel detector, a silicon micro-strip detector, providing tracking information within pseudorapidity  $|\eta| < 2.5$ , and a straw-tube transition radiation tracker that covers  $|\eta| < 2.0$ . The central EM calorimeter is a lead and liquid-argon (LAr) sampling calorimeter with high granularity, and is divided into a barrel region that covers  $|\eta| < 1.5$  and endcap regions that cover  $1.4 < |\eta| < 3.2$ . A steel/scintillator tile calorimeter provides hadronic energy measurements in the central range of  $|\eta| < 1.7$ . The endcap  $(1.5 < |\eta| < 3.2)$  and forward regions  $(3.1 < |\eta| < 4.9)$  are instrumented with LAr calorimeters for both the EM and hadronic energy measurements. The MS consists of three large superconducting toroid magnets with eight coils each, a system of trigger chambers covering  $|\eta| < 2.4$ , and precision tracking chambers covering  $|\eta| < 2.7$ . The ATLAS detector employs a three-level trigger system [45], used to select events to be recorded for offline analysis. The first-level trigger is hardware-based, implemented in custom-built electronics and it uses a subset of the detector information to reduce the physical event rate from  $40\mathrm{MHz}$  to at most  $75\mathrm{kHz}$ . The second-level trigger and the final event filter, collectively referred to as the high-level trigger (HLT), are software-based and together reduce the event rate to about  $400\mathrm{Hz}$ .

# 4 Data and simulation samples

The analysis is performed using data from  $pp$  collisions delivered by the LHC in 2012 at  $\sqrt{s} = 8\mathrm{TeV}$  and recorded by the ATLAS detector. Stringent detector and data quality requirements were applied, resulting in a data sample corresponding to a total integrated luminosity of  $20.2\mathrm{fb^{-1}}$  [46]. The events were selected by single-lepton<sup>3</sup> triggers [45, 47], imposing at the HLT a threshold of  $24\mathrm{GeV}$  on the transverse energy ( $E_{\mathrm{T}}$ ) of electrons and on the transverse momentum ( $p_{\mathrm{T}}$ ) of muons, along with isolation requirements. To recover efficiency for higher- $p_{\mathrm{T}}$  leptons, the isolated lepton triggers were complemented by triggers without isolation requirements, but with a threshold raised to  $60\mathrm{GeV}$  for electrons and to  $36\mathrm{GeV}$  for muons.

Samples of events generated using Monte Carlo (MC) simulations were produced using different event generators interfaced to various parton showering (PS) and hadronisation generators. Minimum-bias events simulated with the PYTHIA8 generator (ver. 8.1) [48] were overlaid to model the effect of multiple  $pp$  collisions per bunch crossing (pile-up). The distribution of the average number of pile-up interactions in the simulation is reweighted to match the corresponding distribution in data, which has an average of 21 [46]. The events were processed using the same reconstruction and analysis chain as for data events.

Single-top-quark  $t$ -channel events were generated with the NLO PowHEG-Box generator (rev. 2556) [49] with the CT10f4 [50] PDF set, using the 4FS for the matrix-element (ME) calculations [51]. The renormalisation and factorisation scales were set to  $\mu_{\mathrm{R}}^{2} = \mu_{\mathrm{F}}^{2} = 16(m_{b}^{2} + p_{\mathrm{T},b}^{2})$ , where  $m_{b}$  is the mass of the  $b$ -quark and  $p_{\mathrm{T},b}$  is the transverse momentum of the  $b$ -quark from the initial gluon splitting. Top quarks were decayed using

MADSPIN [52], which preserves all spin correlations. Additional  $t$ -channel samples were produced with the LO PROTOS generator (ver. 2.2b) [53] using the CTEQ6L1 PDF set [54] within the 4FS. Thus in addition to a SM sample, samples with anomalous couplings enabled in both the production and the decay vertices were produced using the PROTOS generator, varying simultaneously  $V_{\mathrm{L}}$  with either  $\operatorname{Re}[V_{\mathrm{R}}] \in [0.25, 0.50]$ ,  $\operatorname{Re}[g_{\mathrm{R}}] \in [-0.26, 0.18]$  or  $\operatorname{Im}[g_{\mathrm{R}}] \in [-0.23, 0.23]$ , such that the top-quark width was invariant. The factorisation scale was set to  $\mu_{\mathrm{F}}^{2} = -p_{W}^{2}$  for the spectator quark and  $\mu_{\mathrm{F}}^{2} = p_{b}^{2} + m_{b}^{2}$  for the gluon, where  $p_{W}$  and  $p_{\bar{b}}$  are the three-momenta of the exchanged  $W$  boson and of the  $\bar{b}$ -quark originating from the gluon splitting (the spectator  $\bar{b}$ -quark), respectively. In order to compare different LO generators, another sample of signal events was produced with the multi-leg LO ACERMC generator (ver. 3.8) [55] using the CTEQ6L1 PDF set. This generator incorporates both 4FS and 5FS, featuring an automated procedure to remove the overlap in phase space between the two schemes [56]. The factorisation and renormalisation scales were set to  $\mu_{\mathrm{F}} = \mu_{\mathrm{R}} = m_{t} = 172.5 \mathrm{GeV}$ .

In this analysis, all simulated signal event samples are normalised using the production cross-section mentioned in section 1. Simulation samples produced with PowHEG-Box are used for predicting the acceptance and the template shape of the  $t$ -channel signal. To estimate the efficiency and resolution models, the simulation samples in which parton-level information is well defined, i.e. those produced with either PROTOS or ACERMC, are used.

Samples of simulated events for  $t\bar{t}$  production and electroweak production of single top quarks in the associated  $Wt$  and  $s$ -channel were produced using the NLO PowHEG-Box generator (rev. 2819, rev. 3026) coupled with the CT10 [50] PDF set. The  $t$ - and  $s$ -channel processes do not interfere even at NLO in QCD and are thus well defined with that precision [57]. For  $Wt$  associated production, the diagram removal scheme is used to eliminate overlaps between this process and  $t\bar{t}$  production at NLO. In the  $t\bar{t}$  sample, the resummation damping factor<sup>4</sup>  $h_{\mathrm{damp}}$  was set to the top-quark mass [58]. An additional  $t\bar{t}$  sample with anomalous couplings enabled in the decay vertex was produced using the PROTOS generator (ver. 2.2) coupled with the CTEQ6L1 PDF set. This sample is used to take into account the dependence of  $t\bar{t}$  background upon the value of the anomalous couplings.

For all simulated event samples mentioned above, the PS, hadronisation and underlying event (UE) were added using PYTHIA (ver. 6.426, ver. 6.427) [59] with the Perugia 2011C set of tuned parameters (P2011C tune) [60] and the CTEQ6L1 PDF set. The TAUOLA [61] program and the PHOTOS [62] algorithm were used to properly simulate decays of polarised  $\tau$  leptons including spin correlations and to generate quantum electrodynamics (QED) radiative corrections in decays to account for photon radiation. All these processes were simulated assuming a top-quark mass of  $172.5\mathrm{GeV}$ , and the decay of the top quark was assumed to be  $100\% t\rightarrow Wb$ .

For estimating the  $t$ -channel and  $tt$  generator modelling uncertainties, additional samples were produced using alternative generators or parameter variations. For studying the

top-quark mass dependence, supplementary single-top-quark and  $t\bar{t}$  simulated event samples with different top-quark masses were generated. These topics are further discussed in section 10 and section 11, respectively.

Vector-boson production in association with jets was simulated using the multi-leg LO SHERPA generator (ver. 1.4.1) [63] with its own parameter tune and the CT10 PDF set. Thus,  $W+$  jets and  $Z+$  jets events with up to four additional partons were generated and the contributions of  $W/Z+$  light-jets and  $W/Z+$  heavy-jets ( $W/Z+bb$ ,  $W/Z+cc$ ,  $W/Z+c$ ) were simulated separately. SHERPA was also used to generate the hard process, but also for the PS, hadronisation and the UE, using the CKKW method [64] to remove overlaps between the partonic configurations generated by the ME and by the PS. Samples of diboson events ( $WW$ ,  $WZ$ , and  $ZZ$ ), containing up to three additional partons where at least one of the bosons decays leptonically, were also produced using the SHERPA generator (ver. 1.4.1) with the CT10 PDF set.

All baseline simulated event samples were passed through the full simulation of the ATLAS detector [65] based on the GEANT4 framework [66] while PROTOS simulated event samples and alternative samples used to estimate systematic uncertainties were processed through a faster simulation using the ATLFAST2 framework [67].

# 5 Event reconstruction

Electron candidates are reconstructed from isolated energy deposits in the EM calorimeter associated with ID tracks fulfilling strict quality requirements [68]. These electrons are required to satisfy  $E_{\mathrm{T}} = E_{\mathrm{cluster}} / \sin(\theta_{\mathrm{track}}) > 25 \, \mathrm{GeV}$  and  $|\eta_{\mathrm{cluster}}| < 2.47$ , where  $E_{\mathrm{cluster}}$  and  $\eta_{\mathrm{cluster}}$  denote the energy and the pseudorapidity of the cluster of energy deposits in the EM calorimeter, and  $\theta_{\mathrm{track}}$  denotes the polar angle of the ID track associated with this cluster. Clusters in the EM calorimeter barrel-endcap transition region, corresponding to  $1.37 < |\eta_{\mathrm{cluster}}| < 1.52$ , are excluded. Muon candidates are reconstructed using combined information from the ID tracks and the MS [69]. They are required to have  $p_{\mathrm{T}} > 25 \, \mathrm{GeV}$  and  $|\eta| < 2.5$ . The electron and muon candidates must fulfil additional isolation requirements, as described in ref. [70], in order to reduce contributions from misidentified jets, non-prompt leptons from the decay of heavy-flavour quarks and non-prompt electrons from photon conversions.

Jets are reconstructed using the anti- $k_{t}$  algorithm [71, 72] with a radius parameter of 0.4, using topological clusters of calorimeter energy deposits [73] as inputs to the jet finding. The clusters are calibrated with a local cluster weighting method [73]. The jet energy is further corrected for the effect of multiple  $pp$  interactions. Jets are calibrated using an energy- and  $\eta$ -dependent simulation-based scheme, with in situ corrections based on data [74]. To reject jets from pile-up events, a so-called jet-vertex-fraction (JVF) criterion [75] is applied to the jets with  $p_{\mathrm{T}} < 50 \mathrm{GeV}$  and  $|\eta| < 2.4$ : at least  $50\%$  of the scalar sum of the  $p_{\mathrm{T}}$  of the tracks associated with a jet is required to be from tracks compatible with the primary vertex. $^{5}$  Only events containing reconstructed jets with  $p_{\mathrm{T}} > 30 \mathrm{GeV}$  and

$|\eta| < 4.5$  are considered. The  $p_{\mathrm{T}}$  threshold is raised to  $35\mathrm{GeV}$  for the jets in the calorimeter endcap-forward transition region, corresponding to  $2.7 < |\eta| < 3.5$  [29]. Jets identified as likely to contain  $b$ -hadrons are tagged as  $b$ -jets. The  $b$ -tagging is performed using a neural network (NN) which combines three different algorithms exploiting the properties of a  $b$ -hadron decay in a jet [76]. The  $b$ -tagging algorithm, only applied to jets within the coverage of the ID (i.e.  $|\eta| < 2.5$ ), is optimised to improve the rejection of  $c$ -quark jets, since  $W$  boson production in association with  $c$ -quarks is a major background for the selected final state. The requirement applied to the NN discriminant corresponds to a  $b$ -tagging efficiency of  $50\%$ , with mis-tagging rates of  $3.9\%$  and  $0.07\%$  for  $c$ -quark jets and light-flavour jets ( $u-$ ,  $d-$ ,  $s$ -quark or gluon  $g$ ), respectively, as predicted in simulated  $tt$  events and calibrated with data [77, 78].

The missing transverse momentum, with magnitude  $E_{\mathrm{T}}^{\mathrm{miss}}$ , is reconstructed from the vector sum of energy deposits in the calorimeter projected onto the transverse plane [79]. The energies of all clusters are corrected using the local cluster weighting method. Clusters associated with high-  $p_{\mathrm{T}}$  jets and electrons are further calibrated using their respective energy corrections. In addition, contributions from the  $p_{\mathrm{T}}$  of the selected muons are also included in the calculation. The  $E_{\mathrm{T}}^{\mathrm{miss}}$  is taken as a measurement of the undetectable particles, and is affected by energy losses due to detector inefficiencies and acceptance, and by energy resolution.

# 6 Event selection in the signal, control, and validation regions

The signal event candidates are selected by requiring a single prompt isolated lepton, $^{6}$  significant  $E_{\mathrm{T}}^{\mathrm{miss}}$ , and exactly two jets. All these objects must satisfy the criteria described in section 5, and the  $E_{\mathrm{T}}^{\mathrm{miss}}$  is required to be larger than  $30\mathrm{GeV}$ . One of the jets must be identified as a  $b$ -tagged jet with  $|\eta| < 2.5$  while the second jet, also called the spectator jet, is required to be untagged and produced in the forward direction. Events containing additional jets are vetoed to suppress background from  $t\bar{t}$  production. The spectator  $\bar{b}$ -quark originating from the gluon splitting (4FS), as shown in figure 1(b), can result in an additional  $b$ -tagged jet. This jet is expected to have a softer  $p_{\mathrm{T}}$  spectrum and a broader  $\eta$  distribution than the  $b$ -tagged jet produced in the top-quark decay. It is generally not detected in the experiment and these events pass the event selection. Events are required to contain at least one good primary vertex candidate, and no jets failing to satisfy reconstruction quality criteria. In addition, the transverse mass of the lepton- $E_{\mathrm{T}}^{\mathrm{miss}}$  system,

$$
m _ {\mathrm {T}} (\ell E _ {\mathrm {T}} ^ {\mathrm {m i s s}}) = \sqrt {2 p _ {\mathrm {T}} (\ell) \cdot E _ {\mathrm {T}} ^ {\mathrm {m i s s}} \left[ 1 - \cos \left(\Delta \phi (\ell , E _ {\mathrm {T}} ^ {\mathrm {m i s s}})\right) \right]},
$$

where  $\Delta \phi (\ell ,E_{\mathrm{T}}^{\mathrm{miss}})$  is the difference in azimuthal angle between the lepton momentum and the  $E_{\mathrm{T}}^{\mathrm{miss}}$  direction, is required to be larger than  $50\mathrm{GeV}$  in order to reduce the multijet background contribution. Further reduction of this background is achieved by imposing a requirement on the lepton  $p_{\mathrm{T}}$  to events in which the lepton and leading jet  $(j_{1})$  are

back-to-back [29, 33, 80],

$$
p _ {\mathrm {T}} (\ell) > 4 0 \left(\frac {| \Delta \phi (j _ {1} , \ell) | - 1}{\pi - 1}\right) \mathrm {G e V},
$$

where  $\Delta \phi (j_1,\ell)$  is the difference in azimuthal angle between the lepton momentum and the leading jet. To reduce the dilepton backgrounds, events containing an additional lepton, identified with less stringent criteria (referred to as a loose lepton) and with a  $p_{\mathrm{T}}$  threshold lowered to  $10\mathrm{GeV}$ , are rejected. Finally, two additional requirements are applied in order to remove a mis-modelling between data and prediction seen in the  $W+$  jets control and validation regions, in the  $|\eta|$  distribution of the non- $b$ -jet and in the  $|\Delta \eta|$  distribution between the two required jets:  $|\eta (\mathrm{non - }b\text{-jet})| < 3.6$  and  $|\Delta \eta (\mathrm{non - }b\text{-jet}, b\text{-jet})| < 4.5$ .

The  $W$  boson originating from the decay of the top quark is reconstructed from the momenta of the lepton and the neutrino by imposing four-momentum conservation. Since the neutrino escapes undetected, the  $x$  and  $y$  components of the reconstructed  $E_{\mathrm{T}}^{\mathrm{miss}}$  are assumed to correspond to the  $p_{\mathrm{T}}$  of the neutrino. The unmeasured longitudinal component of the neutrino momentum,  $p_{\nu}^{z}$ , is computed by imposing a  $W$  boson mass constraint on the lepton-neutrino system. A quadratic expression is found for  $p_{\nu}^{z}$ . If there are two real solutions, the solution closer to zero is taken. If the solutions are complex, the assumption of the neutrino being the only contributor to the  $E_{\mathrm{T}}^{\mathrm{miss}}$  is not valid. $^7$  Therefore, the reconstructed  $E_{\mathrm{T}}^{\mathrm{miss}}$  is rescaled, preserving its direction, in order to have physical (real) solutions for  $p_{\nu}^{z}$ . This generally results in two solutions for the rescaled  $E_{\mathrm{T}}^{\mathrm{miss}}$ . If just one solution of the rescaled  $E_{\mathrm{T}}^{\mathrm{miss}}$  is positive, this is chosen. If both are positive, the one closer to the initial  $E_{\mathrm{T}}^{\mathrm{miss}}$  is chosen. The top-quark candidate is then reconstructed by combining the four-momenta of the reconstructed  $W$  boson and the selected  $b$ -tagged jet. Finally, the momenta of the  $W$  boson and spectator jet are boosted into the top-quark rest frame to obtain  $\vec{q}$  and  $\vec{p}_{\mathrm{s}}$ , used to define the coordinate system in figure 2, and the lepton is boosted into the  $W$  boson rest frame to obtain  $\vec{p}_{\ell}^{*}$ .

In addition to this basic event selection, which defines the preselected region, further discrimination between the  $t$ -channel signal events and background events is achieved by applying additional criteria:

- The pseudorapidity of the non- $b$ -tagged jet must satisfy  $|\eta(\text{non}-b\text{-jet})| > 2.0$ , since the spectator jet tends to be produced in the forward region in the  $t$ -channel signature.  
- The scalar sum of the  $p_{\mathrm{T}}$  of all final-state objects (lepton, jets and  $E_{\mathrm{T}}^{\mathrm{miss}}$ ),  $H_{\mathrm{T}}$ , must be larger than 195 GeV, since the  $H_{\mathrm{T}}$  distributions of the backgrounds peak at lower values (in particular for the  $W+$  jets contribution) than the  $t$ -channel signature.  
- The mass of the top quark reconstructed from its decay products,  $m(\ell \nu b)$ , is required to be within 130–200 GeV, to reject background events from processes not involving top quarks.

- The absolute difference in  $\eta$  between the non- $b$ -tagged jet and the  $b$ -jet,  $|\Delta \eta (\text{non}-b\text{-jet}, b\text{-jet})|$ , must be larger than 1.5, to further reduce  $t\bar{t}$  contributions.

These criteria are based on the selection requirements used in ref. [33], re-optimised using MC simulation at  $\sqrt{s} = 8\mathrm{TeV}$  [34]. Thus, these criteria together with the signal preselection define the signal region of this analysis.

The distributions of the four variables used to define the signal region are shown in figure 3 at the preselection stage. The simulated signal and background distributions are scaled to their theoretical predictions except the multijet background, which is estimated using data-driven techniques described in section 7. The  $W+$  jets, top-quark backgrounds and  $t$ -channel distributions are normalised to the results of the maximum-likelihood fit, also described in section 7. In figure 3(a), the well-modelled bump around  $|\eta| = 2.5$  is due to a combination of the JVF requirement, which is applied to jets with  $p_{\mathrm{T}} < 50 \mathrm{GeV}$  and  $|\eta| < 2.4$ , and the increased  $p_{\mathrm{T}}$  requirement on jets in the calorimeter endcap-forward transition region  $(2.7 < |\eta| < 3.5)$ . These two requirements are described in section 5.

To estimate the rates and validate the modelling of the dominant background contributions, the simulated events are compared to the data in three dedicated background-enriched regions:

- A control region dominated by  $t\bar{t}$  events is defined by considering preselected events containing two additional non- $b$ -tagged jets (i.e. four jets are required since just one of them is required to be  $b$ -tagged).  
- A control region enriched in  $W +$  jets events, and dominated by  $W +$  heavy-jets, is defined in order to control the modelling of the background. The events selected in this control region are the ones satisfying the preselection criteria and failing to satisfy any of the four requirements in the selection criteria. The flavour composition of this control region is similar to that of the signal region.  
- A third region is defined as a validation region dominated by  $W+$  jets events to further control the modelling of the shapes of the  $W+$  jets background. Events in this validation region are selected by considering the preselection criteria with a relaxed  $b$ -tagging efficiency requirement of  $80\%$ . In addition, all events satisfying the tighter signal  $b$ -tagging efficiency requirement of  $50\%$  are excluded. This region has much larger enrichment in  $W+$  jets events although the flavour composition differs from that of the signal region.

The two control regions are used to extract the normalisation of  $t\bar{t}$  and  $W+$  jets as described in section 7.

# 7 Background estimation and normalisation

The largest background contributions to single-top-quark  $t$ -channel production arise from  $t\bar{t}$  and  $W+$  jets production. The former is difficult to distinguish from the signal since  $t\bar{t}$  events contain real top quarks in the final state. The  $W+$  jets production contributes to the

![](images/501102c506863a20d25888f01d622217873f1d773ca912860254af225be49ffb.jpg)  
(a)

![](images/bf354bf586b9000c8f74e928b8a8a25ee088841b3c90391658250980b5f0055d.jpg)  
(b)

![](images/c76ee280a596dd897e152e9aa8581a9ca5015ff73c7f26a0e55bbb86020e3830.jpg)  
(c)

![](images/aeddfef5c036934ee1c90a9ee3b1fe34844939e82f0bcfa3eca542ffc69d3e5d.jpg)  
Figure 3. Distributions of (a)  $|\eta(\text{non}-b\text{-jet})|$ , (b) the scalar sum of the  $p_{\mathrm{T}}$  of all final-state objects,  $H_{\mathrm{T}}$ , (c) reconstructed top-quark mass,  $m(\ell \nu b)$ , and (d)  $|\Delta \eta(\text{non}-b\text{-jet}, b\text{-jet})|$  in the signal preselected region for the electron and muon channels merged. The prediction is compared to data, shown as the black points with statistical uncertainties. The multijet background is estimated using data-driven techniques, while contributions from simulated  $W+$  jets, top-quark backgrounds and  $t$ -channel event samples are normalised to the results of a maximum-likelihood fit to event yields in the signal and control regions. The uncertainty bands correspond to the uncertainties due to the size of the simulated event samples added in quadrature with the data-driven normalisation uncertainty of  $70\%$  estimated for the multijet contribution. The lower plots show the ratio of data to prediction in each bin. The regions excluded by the selection criteria are shown by vertical black lines and dashed areas.  
(d)

background if there is a  $b$ -quark in the final state or due to mis-tagging of jets containing other quark flavours. Multijet production via the strong interaction can contribute as well if, in addition to two reconstructed jets, an extra jet is misidentified as an isolated lepton,

or if a non-prompt lepton appears to be isolated (both referred to as fake leptons). Other minor backgrounds originate from single-top-quark  $Wt$ -channel and  $s$ -channel,  $Z+$  jets and diboson production.

For all background processes, except multijet production, the normalisation is initially estimated by using the MC simulation scaled with the theoretical cross-section prediction, and the event distribution modelling is taken from simulation.

The  $t\bar{t}$  events are normalised with the  $t\bar{t}$  production cross-section calculated at NNLO in QCD including resummation of NNLL soft gluon terms with  $\mathrm{Top}++2.0$  [81-86]. Its predicted value is  $253_{-15}^{+13}\mathrm{pb}$  calculated according to ref. [86]. The quoted uncertainty, evaluated according to the PDF4LHC prescription [87], corresponds to the sum in quadrature of the  $\alpha_{\mathrm{S}}$  uncertainty and the PDF uncertainty, calculated from the envelope of the uncertainties at  $68\%$  CL of the MSTW2008 NNLO, CT10 NNLO [88] and NNPDF2.3 5f FFN [89] PDF sets. The associated  $Wt$ -channel events are normalised with the predicted NNLO production cross-section of  $22.4 \pm 1.5\mathrm{pb}$  [90] and the  $s$ -channel production to the predicted NNLO cross-section of  $5.61 \pm 0.22\mathrm{pb}$  [91]. The uncertainties correspond to the sum in quadrature of the uncertainty derived from the MSTW2008 NNLO PDF set at  $90\%$  CL and the scale uncertainties.

The inclusive cross-sections of vector-boson production are calculated to NNLO with the FEWZ program [92] and the MSTW2008 NNLO PDF set, with a theoretical uncertainty of  $4\%$  and  $5\%$  for  $W+$  jets and  $Z+$  jets, respectively. The cross-sections of diboson processes are calculated at NLO using the MCFM program [93], with a theoretical uncertainty of  $5\%$ . For these three background processes the normalisation uncertainty is  $34\%$  each. This is the result of adding in quadrature their theory uncertainty and  $24\%$  per additional jet, accordingly to the Berends-Giele scaling [94].

The normalisation as well as the event modelling of the multijet background is estimated from data using a matrix method [70, 95]. This method allows the derivation of the true composition of the data sample in terms of prompt (real) and fake leptons from its observed composition in terms of tight (signal selection) and loose leptons. An alternative normalisation and modelling based on the mixed data-simulation jet-electron method [29, 70, 96] and the purely data-driven anti-muon selection [70] are also considered. From the comparison of these two models with the results obtained using the matrix method, an overall normalisation uncertainty of  $70\%$  is assigned to the multijet contribution, irrespective of lepton flavour, as done in ref. [34].

The final  $t$ -channel,  $W+$  jets and top-quark background ( $tt$ , associated  $Wt$  and  $s$ -channel) normalisations are estimated through a simultaneous maximum-likelihood fit to the numbers of data events observed in the signal region and the  $tt$  and  $W+$  jets control regions, described in section 6. The likelihood function [96] is given by the product of Poisson probability terms associated with the fitted regions, combined with the product of Gaussian priors to constrain the background rates to their predictions within the associated uncertainties. In the fit, the  $t$ -channel contribution, estimated using PowHEG-Box, is treated as unconstrained. The top-quark background contributions are merged with their relative fractions taken from simulation, and the applied constraint,  $6\%$ , is derived from the combination in quadrature of their cross-section uncertainties. The  $W+$  jets contribution

is constrained to the normalisation uncertainty of  $34\%$  and its flavour composition is taken from simulation. In these three fitted regions the production of a  $W$  boson in association with heavy-flavour jets is the dominant contribution to the  $W+$  jets background, predicted to be around  $95\%$  in each region. The  $Z+$  jets and diboson contributions, which are very low in the signal region (2% of the expected total), are merged and fixed to the predictions. The multijet contribution is kept fixed to its data-driven estimate. The overall normalisation scale factors obtained from the maximum-likelihood fit together with the statistical post-fit uncertainties are found to be  $1.010 \pm 0.005$  and  $1.128 \pm 0.013$  for the top-quark and  $W+$  jets background contributions, respectively, and  $0.909 \pm 0.022$  for the  $t$ -channel signal. The impact on the analysis due to the deviation of these scale factors from unity is negligible and it is taken into account through the  $W+$  jets normalisation uncertainty as discussed in section 10. In the case of the  $W+$  jets validation region, used to validate the shapes of the predicted templates, just an overall scale factor for the  $W+$  jets component is estimated. It is extracted by matching the total predicted event yields to the number of events observed in this validation region. The results are found to be stable when the prior constraints on the top-quark and  $W+$  jets backgrounds are relaxed to  $100\%$  of their predicted cross-section in the signal and control regions.

The overall normalisation scale factors are used to control the modelling of the kinematic and angular variable distributions in the signal, control, and validation regions. In the subsequent steps of the analysis, the overall scaling of the  $t$ -channel prediction is not relevant, since it is taken from background-subtracted data, while the  $W+$  jets and top-quark backgrounds are normalised using these overall scale factors.

# 8 Event yields and kinematic distributions

Table 1 provides the predicted signal and background event yields for the electron and muon channels merged together in the signal, control, and validation regions after scaling to the results of the maximum-likelihood fit to the data. Observed data yields are also shown. The signal-to-background (S/B) ratio is 0.97 in the signal region while  $\lesssim 0.1$  in the control and validation regions.

Figures 4 and 5 show the distributions of the relevant kinematic distributions used to define the signal region in the  $t\bar{t}$  and  $W+$  jets control regions while figure 6 shows the same distributions in the  $W+$  jets validation region. Good overall data-to-prediction agreement is found within the uncertainty band shown in these distributions, which only includes the uncertainty due to the size of the simulation samples and the uncertainty in the normalisation of the multijet background, added in quadrature. Any data-to-prediction disagreement is covered by the  $t\bar{t}$  and/or  $W+$  jets normalisation and modelling uncertainties detailed in section 10. In figure 5(a) and figure 6(a), the origin of the well-modelled bumps around  $|\eta| = 2.5$  is the same as for figure 3(a). In addition, the well-modelled decrease at  $|\eta| = 2$  shown in figure 5(a) is due to the rejected events in the  $W+$  jets control region, which satisfy the signal selection requirement of  $|\eta(\text{non } b-\text{jet})| > 2.0$ .

Table 1. Predicted and observed data event yields are shown for the merged electron and muon channels in the signal,  $tt$  and  $W+$  jets control and validation regions. The multijet background is estimated using data-driven techniques, while contributions from simulated  $W+$  jets, top-quark backgrounds and  $t$ -channel event samples are normalised to the results of a maximum-likelihood fit to event yields in the signal and control regions. The uncertainties shown are statistical only. Individual predictions are rounded to two significant digits of the uncertainty while "Total expected" corresponds to the rounding of the sum of full-precision individual predictions. The expected S/B ratios are also given.  

<table><tr><td>Process</td><td>Signal region</td><td>tbar control region</td><td>W+jets control region</td><td>W+jets validation region</td></tr><tr><td>t-channel</td><td>4395 ± 17</td><td>1688 ± 12</td><td>11601 ± 29</td><td>9306 ± 27</td></tr><tr><td>tbar, Wt, s-channel</td><td>2017 ± 15</td><td>62864 ± 77</td><td>48120 ± 82</td><td>23937 ± 61</td></tr><tr><td>W+heavy-jets</td><td>1910 ± 49</td><td>6898 ± 65</td><td>45410 ± 200</td><td>157260 ± 480</td></tr><tr><td>W+light-jets</td><td>87 ± 31</td><td>218 ± 38</td><td>3110 ± 200</td><td>130900 ± 1000</td></tr><tr><td>Z+jets, diboson</td><td>157 ± 7</td><td>1118 ± 37</td><td>4734 ± 77</td><td>17750 ± 300</td></tr><tr><td>Multijet</td><td>375 ± 13</td><td>862 ± 27</td><td>8910 ± 61</td><td>20140 ± 120</td></tr><tr><td>Total expected</td><td>8941 ± 64</td><td>73650 ± 120</td><td>121890 ± 310</td><td>359300 ± 1200</td></tr><tr><td>Data</td><td>8939</td><td>73662</td><td>121913</td><td>359320</td></tr><tr><td>S/B</td><td>0.97</td><td>0.02</td><td>0.11</td><td>0.03</td></tr></table>

# 9 Analysis of angular distributions

The model introduced in section 2 is based on the angles  $\theta$ ,  $\theta^{*}$  and  $\phi^{*}$ . The distributions of these angular observables, for events satisfying the signal selection criteria, are shown in figure 7. Isolation requirements placed on the leptons influence the shape of these angular distributions. Thus from figure 2 one can see that for  $\cos \theta = -1$ , the spectator jet overlaps with the  $b$ -tagged jet. Similarly, for  $\cos \theta^{*} = -1$ , the lepton overlaps with the  $b$ -tagged jet. Therefore, in both cases, the acceptance is significantly reduced. For  $\cos \theta = +1$ , the acceptance is maximal since the spectator jet and the  $b$ -tagged jet are back-to-back. For  $\cos \theta^{*} = +1$ , although the lepton and the  $b$ -tagged jet are back-to-back, the acceptance is not maximal since the lepton is in the same plane as the spectator jet and therefore it may overlap with this jet. For  $\phi^{*} = 0$ ,  $\pi$  or  $2\pi$ , the lepton is in the same plane as the spectator jet and therefore it may overlap with this jet. This is disfavoured by the isolation criteria, so acceptance reduces in these three regions. Acceptance is maximal for  $\phi^{*} = \pm \pi / 2$ , since the lepton is in a plane perpendicular to the spectator.

Just as the angular distribution for the true signal can be expressed in terms of the angular coefficients,  $a_{k,l,m}$ , of a finite series of orthonormal functions, the reconstructed angular distribution can be expressed as an infinite series of the same functions, similarly to eq. (2.1):

$$
\varrho_ {\mathrm {r}} \left(\theta , \theta^ {*}, \phi^ {*}; \vec {\alpha}, P\right) = \sum_ {\kappa , \lambda , \mu} \mathcal {A} _ {\kappa , \lambda , \mu} (\vec {\alpha}, P) M _ {\kappa , \lambda} ^ {\mu} \left(\theta , \theta^ {*}, \phi^ {*}\right), \tag {9.1}
$$

where  $|\mu |\leq \min (\kappa ,\lambda)$ . Multiplying eq. (9.1) by  $M_{\kappa ,\lambda}^{\mu *}(\theta ,\theta^{*},\phi^{*})$ , integrating, and applying

![](images/5a43b6b716c8af77b564a498f72d14d9c2962a67da196785bccb32ded1c557e6.jpg)  
(a)

![](images/af31e392c02e194a487618a030afa711ffca5791dfdcc0adf174e4874b246c5d.jpg)  
(b)

![](images/3787aa5fc21c3a1f6981dd03424a032dbc4e27c736660126c88ebb485558b30d.jpg)  
(c)

![](images/6886ccc6e199b39b649c07d572e0a3c329470e2e6900d132c175a2e9f54dcc6a.jpg)  
Figure 4. Distributions of (a)  $|\eta(\text{non } b\text{-jet})|$ , (b) the scalar sum of the  $p_{\mathrm{T}}$  of all final-state objects,  $H_{\mathrm{T}}$ , (c) reconstructed top-quark mass,  $m(\ell \nu b)$ , and (d)  $|\Delta \eta(\text{non } b\text{-jet}, b\text{-jet})|$  in the  $t\bar{t}$  control region for the merged electron and muon channels. The multijet background is estimated using data-driven techniques, while contributions from simulated  $W+$  jets, top-quark backgrounds and  $t$ -channel event samples are normalised to the results of a maximum-likelihood fit to event yields in the signal and control regions. The uncertainty bands correspond to the uncertainties due to the size of the simulated event samples added in quadrature with the data-driven normalisation uncertainty of  $70\%$  estimated for the multijet contribution. The lower plots show the ratio of data to prediction in each bin.  
(d)

the orthonormality of the  $M$ -functions, one projects out the angular coefficients, obtaining

$$
\mathcal {A} _ {\kappa , \lambda , \mu} = \int \varrho_ {\mathrm {r}} (\theta , \theta^ {*}, \phi^ {*}; \vec {\alpha}, P) M _ {\kappa , \lambda} ^ {\mu *} (\theta , \theta^ {*}, \phi^ {*}) \mathrm {d} (\cos \theta) \mathrm {d} \Omega^ {*}.
$$

For a discrete set of data that follows  $\varrho_{\mathrm{r}}$ , the angular coefficients can be estimated as the

![](images/7c6cadbc17ce0b04a3ce4662c91a0a386bba7494baff4e535972562f596c4efc.jpg)  
(a)

![](images/0c68dad84bf1480db4335a8cab38db36e2adfb187ae4e64fb02b5876a3f8c259.jpg)  
(b)

![](images/f6aefc417c7499ef1af44a668f001a11caea6003bb3a2ba8c2dc49aef4b27dc1.jpg)  
(c)

![](images/48a9f994a49619a19231d4d7f7e6fb025ec07a27e80badfed84b69eccbc8aeea.jpg)  
Figure 5. Distributions of (a)  $|\eta(\text{non } b\text{-jet})|$ , (b) the scalar sum of the  $p_{\mathrm{T}}$  of all final-state objects,  $H_{\mathrm{T}}$ , (c) reconstructed top-quark mass,  $m(\ell \nu b)$ , and (d)  $|\Delta \eta(\text{non } b\text{-jet}, b\text{-jet})|$  in the  $W+$  jets control region for the merged electron and muon channels. The multijet background is estimated using data-driven techniques, while contributions from simulated  $W+$  jets, top-quark backgrounds and  $t$ -channel event samples are normalised to the results of a maximum-likelihood fit to event yields in the signal and control regions. The uncertainty bands correspond to the uncertainties due to the size of the simulated event samples added in quadrature with the data-driven normalisation uncertainty of  $70\%$  estimated for the multijet contribution. The lower plots show the ratio of data to prediction in each bin.  
(d)

average value of the function over the data:

$$
\mathcal {A} _ {\kappa , \lambda , \mu} = \langle M _ {\kappa , \lambda} ^ {\mu *} (\theta , \theta^ {*}, \phi^ {*}) \rangle ,
$$

similar to a MC estimation of an integral. Experimental values of these coefficients can thus be obtained by taking this average over a set of discrete data for terms up to a maximum  $\kappa$  and  $\lambda$ , determined by the precision of the data. A similar approach to sequential

![](images/f063acaf41ef6211f196006a79d90ca6114e84cc22fbd188ab003f0cc4e48487.jpg)  
(a)

![](images/ee3861181dc8ab691825f5cb545e3d6433baeb518be051ee899e65cd95d76cce.jpg)  
(b)

![](images/cbfdba6a5f44a5fffd76cbcb16c813cacb31b72e1d62ea8c2cbe7575dbea3375.jpg)  
(c)

![](images/10484f307a3a48841b31c7af00884f54e83c685440ce440da365783c8b848edd.jpg)  
Figure 6. Distributions of (a)  $|\eta(\text{non } b\text{-jet})|$ , (b) the scalar sum of the  $p_{\mathrm{T}}$  of all final-state objects,  $H_{\mathrm{T}}$ , (c) reconstructed top-quark mass,  $m(\ell \nu b)$ , and (d)  $|\Delta \eta(\text{non } b\text{-jet}, b\text{-jet})|$  in the  $W+$  jets validation region for the merged electron and muon channels. The multijet background is estimated using data-driven techniques, while contributions from simulated  $W+$  jets, top-quark backgrounds and  $t$ -channel event samples are normalised to the results of a maximum-likelihood fit to event yields in the signal and control regions. The uncertainty bands correspond to the uncertainties due to the size of the simulated event samples added in quadrature with the data-driven normalisation uncertainty of  $70\%$  estimated for the multijet contribution. The lower plots show the ratio of data to prediction in each bin.  
(d)

decays is suggested in ref. [97]. This technique, called orthogonal series density estimation (OSDE) [98], is essentially a Fourier technique to determine moments of the angular distribution. Since  $\mathcal{A}_{\kappa,\lambda,\mu} = \mathcal{A}_{\kappa,\lambda,-\mu}^*$ , the coefficients with  $\mu = 0$  are purely real, while those with  $\mu \neq 0$  can be represented by the real and imaginary components of  $\mathcal{A}_{\kappa,\lambda,|\mu|}$ . These sets of reconstructed and true angular coefficients,  $\mathcal{A}_{\kappa,\lambda,\mu}$  and  $a_{k,l,m}$ , can be represented by

![](images/fb9a73913979f47707a1c0af25126bd42fcb04b2ec345574a04a5f76df2035f9.jpg)  
(a)

![](images/210671cf075988f59f0a584c67734231474085cfc8f0a4c5ff73a6a2a66c963f.jpg)  
(b)

![](images/1c9de13675450d43e3f6001f469de56fc719c04fa967d89c26afdf8dafd392b4.jpg)  
(c)  
Figure 7. Angular distributions of (a)  $\cos \theta$ , (b)  $\cos \theta^{*}$  and (c)  $\phi^{*}$  in the signal region for the electron and muon channels merged, comparing observed data, shown as the black points with statistical uncertainties, to SM signal and background predictions. The multijet background is estimated using data-driven techniques, while contributions from simulated  $W+$  jets, top-quark backgrounds and  $t$ -channel event samples are normalised to the results of a maximum-likelihood fit to event yields in the signal and control regions. The uncertainty bands correspond to the uncertainties due to the size of the simulated event samples added in quadrature with the data-driven normalisation uncertainty of  $70\%$  estimated for the multijet contribution. The lower plots show the ratio of data to prediction in each bin.

two vectors of coefficients,  $\vec{A}$  and  $\vec{a}$ . A covariance matrix,  $\mathbf{C} = \mathrm{Cov}(\vec{A})$ , is also determined using OSDE, in the standard way by averaging products of two  $M$ -functions.

The background's shape and its covariance matrix are determined through an OSDE analysis of a hybrid sample consisting of background events from simulation samples, and selected data events from samples enriched in multijet events as reported in section 7. The

vector of reconstructed and background-subtracted coefficients,  $\vec{\mathcal{A}}^{\prime}$ , is

$$
\vec {\mathcal {A}} ^ {\prime} = \frac {1}{f _ {\mathrm {s}}} \vec {\mathcal {A}} - \left(\frac {1}{f _ {\mathrm {s}}} - 1\right) \vec {\mathcal {A}} _ {b},
$$

where  $\vec{A}_b$  is the vector of coefficients for the background and  $f_{\mathrm{s}}$  is the signal fraction. On the other hand, the covariance matrix  $\mathbf{C}$  is modified to include the contribution from the background,

$$
\mathbf {C} ^ {\prime} = \left(\frac {1}{f _ {\mathrm {s}}}\right) ^ {2} \mathbf {C} + \left(\frac {1}{f _ {\mathrm {s}}} - 1\right) ^ {2} \mathbf {C} _ {\mathrm {b}}, \tag {9.2}
$$

where  $\mathbf{C}'$  and  $\mathbf{C}_{\mathrm{b}}$  are the covariance matrices of the background-subtracted coefficients and the background coefficients alone, respectively. The second term in eq. (9.2) represents a systematic uncertainty in  $\mathbf{C}'$  due to statistical uncertainties in the background estimate.

Detector effects, both efficiency and resolution, are incorporated through a migration matrix that relates true coefficients,  $\vec{a}$ , to reconstructed and background-subtracted coefficients,  $\vec{\mathcal{A}}'$ . This matrix, denoted by  $\mathbf{G}$ , translates all of the nine true coefficients (not counting  $a_{0,0,0}$ ) to the reconstructed coefficients. It is determined from MC samples produced with the PROTOS generator using a Fourier analysis of the joint probability density function of true and reconstructed angles, followed by a transformation to coefficients of a conditional probability density function. The procedure is described in more detail in refs. [36, 37]. In terms of  $\mathbf{G}$ ,

$$
\vec {\mathcal {A}} = \mathbf {G} \cdot \vec {a}. \tag {9.3}
$$

Equation (9.3) cannot be inverted in practice because the matrix  $\mathbf{G}$  has more rows than columns, indicating a situation with more equations than unknown variables. Owing to statistical fluctuations or systematic shifts in the measured quantities, it is possible that they cannot all be satisfied simultaneously. The number of rows can be reduced by considering fewer equations. The higher-order terms in  $\vec{\mathcal{A}}$  and  $\vec{\mathcal{A}}_b$ , of which there are an infinite number, are truncated since they represent high-frequency components bringing little information about the true coefficients. In what follows, a truncation is done at  $\lambda_{\mathrm{max}} = \kappa_{\mathrm{max}} = 2$  (subscript "max" is the maximum index value of a given series). The maximum values of  $k$  and  $l$  are chosen to obtain the optimal statistical uncertainty in physics parameters. With this truncation the number of background-subtracted coefficients is 18.

Since a covariance matrix,  $\mathbf{C}' = \mathrm{Cov}(\vec{\mathcal{A}}')$ , is available, one can minimise the function

$$
\chi^ {2} (\vec {a}) = \left(\vec {\mathcal {A}} ^ {\prime} - \mathbf {G} \cdot \vec {a}\right) ^ {\mathrm {T}} \cdot (\mathbf {C} ^ {\prime}) ^ {- 1} \cdot \left(\vec {\mathcal {A}} ^ {\prime} - \mathbf {G} \cdot \vec {a}\right),
$$

over the vector  $\vec{a}$ . This can be done analytically, and yields the solution

$$
\vec {a} = \mathbf {V} \cdot \mathbf {G} ^ {\mathrm {T}} \cdot \left(\mathbf {C} ^ {\prime}\right) ^ {- 1} \cdot \vec {\mathcal {A}} ^ {\prime}, \tag {9.4}
$$

with

$$
\mathbf {V} = \operatorname {C o v} (\vec {a}) = \left(\mathbf {G} ^ {\mathrm {T}} \cdot \left(\mathbf {C} ^ {\prime}\right) ^ {- 1} \cdot \mathbf {G}\right) ^ {- 1}. \tag {9.5}
$$

The deconvolved coefficients, using a migration matrix derived from simulated SM event samples produced with the PROTOS generator, are shown in figure 8. Correlations between the different coefficients range from nearly zero to almost  $70\%$ . Also shown are the

![](images/964c47e085f806f6cede15d09ab5be52a6323d6664f7a64be548c0c8cb79eea1.jpg)  
Figure 8. Deconvolved angular coefficients from data using the migration matrix from the SM simulation. Data are shown as black points with statistical uncertainties (inner error bar) and statistical and systematic uncertainties added in quadrature (outer error bar), while SM prediction is shown as a red line. In addition, two new physics scenarios, one with  $\delta_{-} = \pi$  and another one with  $f_0^+ = 0.2$ , are also shown as a dotted blue line and dashed green line, respectively. The  $x$ -axis shows the real and imaginary parts of the angular coefficients, where the latter appears in boldface.

SM predictions, obtained from eq. (2.2), using SM values for  $\vec{\alpha}$ , and a PROTOS simulation for the polarisation. Moreover, two new physics scenarios, obtained from PROTOS simulations, are also shown. The scenario with  $\delta_{-} = \pi$  corresponds to a region where  $\mathrm{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}] \approx 0.77$ , allowed by the fit in measurements of  $W$  boson helicity fractions in top-quark decays [24-28]. The scenario with  $f_0^+ = 0.2$  corresponds to a set of couplings  $(|V_{\mathrm{R}} / V_{\mathrm{L}}| \approx 0.65$ , and  $|g_{\mathrm{L}} / V_{\mathrm{L}}| \approx 0.27)$  that are also consistent with measurements of  $W$  boson helicity fractions, but where  $20\%$  of the longitudinal  $W$  bosons are due to right-handed couplings.

The derivation of the migration matrix,  $\mathbf{G}$ , and background model,  $\vec{\mathcal{A}}_b$ , described above, is based on the form of these distributions in MC simulation. For the background model, constructed from the sum of all predicted backgrounds with an appreciable effect on the distribution, this includes events containing top quarks, primarily from  $t\bar{t}$  production, the distribution of which is affected by changing the values of the anomalous couplings. The efficiency and resolution models are averages over all unmeasured distributions in the signal. Variations in the values of anomalous couplings alter those unmeasured distributions, which could lead to a dependence on these couplings for the efficiency and resolution models. For instance,  $t$ -channel single-top-quark production depends on anomalous couplings in both the top-quark production and decay vertices, so varying the couplings alters production-side distributions, such as the  $p_{\mathrm{T}}$  and  $\eta$  distributions of the top or spectator quark. Therefore  $\mathbf{G}$  and  $\vec{\mathcal{A}}_b$  both depend upon  $\vec{\alpha}$ . When evaluating  $\vec{a}$  for different possible values of  $\vec{\alpha}$ , the appropriate values of  $\mathbf{G}(\vec{\alpha})$  and  $\vec{\mathcal{A}}_b(\vec{\alpha})$  must be used. Consequently,  $\vec{a}$  also depends on  $\vec{\alpha}$ .

To interpret the measurement of the coefficients  $\vec{a} (\vec{\alpha})$  as a measurement of the parameters  $\vec{\alpha}$ , the real and imaginary parts of the predicted coefficients  $a_{k,l,m}$  obtained from eq. (2.2) are packed into a vector  $\vec{a}_{\mathrm{th}}$ . The coefficient  $a_{0,0,0}$  is omitted in this procedure because it is constrained by normalisation. Since the number of parameters used to describe the complex coefficients  $\dim (\vec{a}) = 9$  exceeds  $\dim (\vec{\alpha}) = 6$ , an over-constrained system is found. Using  $\vec{a} (\vec{\alpha})$  from eq. (9.4) and  $\mathbf{V}$  from eq. (9.5), an additional  $\chi^2$  contribution is defined as

$$
\chi^ {2} (\vec {\alpha}) = \left(\vec {a} _ {\mathrm {t h}} (\vec {\alpha}) - \vec {a} (\vec {\alpha})\right) ^ {\mathrm {T}} \cdot \mathbf {V} ^ {- 1} \cdot \left(\vec {a} _ {\mathrm {t h}} (\vec {\alpha}) - \vec {a} (\vec {\alpha})\right). \tag {9.6}
$$

The final fit uses the combined likelihood

$$
- 2 \ln \mathcal {L} = \chi^ {2} (\vec {\alpha}) + \chi^ {2} (\vec {a}). \tag {9.7}
$$

Likelihood profiles over the parameters  $\vec{\alpha}$  are computed using a Markov chain MC method [99]. In order to correct for the dependence of  $\mathbf{G}$  on  $\vec{\alpha}$ , the migration matrix is computed on a four-dimensional grid in  $f_{1}, f_{1}^{+}, f_{0}^{+}$ , and  $\delta_{-}$  using Lagrange interpolation between the grid points. Two points are used in  $f_{1}^{+}, f_{0}^{+}$ , while four are used in  $f_{1}$  and  $\delta_{-}$ . The range of interpolation is  $f_{1} \in [0.24, 0.36]$ ,  $f_{1}^{+} \in [0.0, 0.25]$ ,  $f_{0}^{+} \in [0.0, 0.25]$ , and  $\delta_{-} \in [-0.5, 0.5]$ . The background coefficients  $\vec{A}_{b}$  are also corrected for the dependence of the  $t\bar{t}$  background on  $\vec{\alpha}$  in the same manner.

The procedure for deconvolving detector effects has been validated with closure tests, performed using simulation samples produced with the PROTOS and ACERMC generators. The model independence of this procedure has been validated using the various simulation samples with anomalous couplings enabled in both the production and the decay vertices, as mentioned in section 4.

# 10 Sources of systematic uncertainty

Systematic uncertainties are estimated for the angular coefficients  $a_{k,l,m}$ . The systematic uncertainties are better behaved in these angular coefficients than in the parameters  $\vec{\alpha}$ , where they might be close to physical boundaries, e.g.  $f_1^+ = 0$  or  $f_0^+ = 0$ . These systematic uncertainties are used to construct a  $9 \times 9$  covariance matrix including all correlations between different angular coefficients for each uncertainty considered. The full systematic covariance matrix,  $\mathbf{V}_{\mathrm{syst}}$ , is then formed by summing the individual matrices. For evaluating the likelihood including the total uncertainty,  $\mathbf{V}_{\mathrm{syst}}$  is added to the covariance matrix determined from eq. (9.5) before evaluating eq. (9.6).

Unless addressed specifically, the efficiency and resolution models (i.e. migration matrix) in  $t$ -channel events used to estimate the impact of the various sources of uncertainty on the deconvolved measurements are those extracted from the nominal simulation sample produced with the PROTOS generator and SM couplings. The nominal acceptance and template shape of the  $t$ -channel signal is predicted using the PowHEG-Box generator. Various signal and background models are determined from MC simulation samples with either alternative generators or parameters varied by their uncertainty in order to estimate systematic uncertainty from different sources. For each source, a likelihood is constructed

from the resulting background-subtracted-data model, using events generated with varied parameters. The difference is calculated between the central values estimated at the nominal value of a parameter and at the value varied by its uncertainty, or half the difference between central values estimated with the parameter varied up and down by its uncertainty. These differences are used to construct a covariance matrix for each source of systematic uncertainty. The total covariance matrix for the systematic uncertainties and its correlation matrix are found from the sum of the covariance matrices determined for individual uncertainties.

When estimating the impact of the various sources of uncertainty, the variations are propagated in a correlated way to the rates and to the shapes. The variations due to the systematic uncertainties are also propagated in a correlated way to the signal region and to the two control regions used to constrain the top-quark and  $W+$  jets background contributions. For the statistical uncertainties, the variations in the signal and control regions are considered as independent. A set of overall scale factors associated with the top-quark and  $W+$  jets backgrounds and with the signal events are extracted for each source of systematic or statistical variation, through the procedure explained in section 7. The background normalisation is obtained for each systematic uncertainty shift before being subtracted from the observed data. Then the systematic and statistical uncertainties in the fitted normalisation factors are propagated to the measurement.

The sources of systematic uncertainty are split into the following categories:

Detector modelling. The systematic uncertainties in the reconstruction, and energy calibration of electrons and jets and momentum calibration of muons are propagated in the analysis through variations in the modelling of the detector response. Uncertainties related to leptons come from trigger, identification and isolation efficiencies, as well as from the energy or momentum scale and resolution [68, 69]. For jets, the main source of uncertainty is the jet energy scale (JES), evaluated using a combination of in situ techniques [74]. Other jet-related uncertainty sources are the modelling of the energy resolution [100] and reconstruction efficiency [74], the JVF efficiency [75], and the modelling of the tagging efficiencies of  $b$ -quark jets,  $c$ -quark jets and light-quark jets [77, 78]. The uncertainties from the energy or momentum scale and resolution corrections applied to leptons and jets are propagated to the computation of the  $E_{\mathrm{T}}^{\mathrm{miss}}$ . The scale and resolution uncertainties due to soft jets and to contributions of calorimeter energy deposits not associated with any reconstructed objects are also considered independently. For all detector modelling uncertainties, positive and negative uncertainties are estimated separately from the corresponding shifts.

Background normalisation. The uncertainties in the normalisation of the top-quark and  $W+$  jets background processes are determined from the scale factor obtained from the maximum-likelihood fit to data. For the top-quark background processes, the statistical post-fit uncertainty of  $1\%$  in its overall scale factor is considered. For the  $W+$  jets background process, the difference between its nominal overall scale factor and the one estimated when constraining the scale factor of the  $t$ -channel contribution to 1.0 in the maximum-likelihood fit (3%) is considered. For the  $Z+$  jets and diboson processes, a normalisation uncertainty of  $34\%$  is applied to the predictions. For the data-driven normalisation of the

multijet background the uncertainty of  $70\%$  estimated from the comparison of the matrix method estimates with those given by the jet-electron and anti-muon methods is used. The uncertainty in the integrated luminosity is  $1.9\%$  [46] and it is propagated through the normalisation of the simulated background events.

Signal and background modelling. Systematic uncertainties associated with the signal and background modelling are estimated by comparing different generators and by varying parameters in the event generation. The uncertainty in the predicted efficiency and resolution models for the  $t$ -channel single-top-quark process, used to deconvolve reconstructed quantities (from PowHEG-Box interfaced to PYTHIA), is estimated by comparing the nominal PROTOS with ACERMC, both interfaced to PYTHIA. This uncertainty also accounts for the difference between models which consider the 4FS in PROTOS and the 5FS+4FS in ACERMC. The uncertainty in the ME calculation in the simulation of the  $t$ -channel process is estimated in two ways; by comparing PROTOS with PowHEG-Box, both interfaced to PYTHIA, to account for the mis-modelling of an NLO process by a LO generator, and by comparing PowHEG-Box with MG5_AMC@NLO (ver. 2.2.2) [101], both interfaced to HERWIG (ver. 6.5.20.2) [102] using ATLAS underlying event tune 2 (AUET2) [103], to account for modelling differences between NLO generators. For the  $tt$  process, PowHEG-Box is compared with MC@NLO (version 4.06) [104], both also interfaced to HERWIG using the AUET2 tune. The uncertainty in the PS and hadronisation is estimated by comparing PowHEG-Box interfaced with PYTHIA and HERWIG for both the  $t$ -channel and  $tt$  processes. The uncertainty in the amount of radiation is evaluated for the  $t$ -channel and  $tt$  processes by comparing the nominal samples with the PowHEG-Box samples generated with varied factorisation and renormalisation scales (and different values of the  $h_{\mathrm{damp}}$  parameter in the case of the  $tt$  samples), interfaced to PYTHIA with different hadronisation scales or configurations via alternative Perugia sets of tuned parameters (P2012radHi, P2012radLo, P2012mpiHi and P2012loCR) [60]. In this case, the uncertainty is defined by the shift from the nominal measurement. All these signal and background modelling uncertainties are treated as uncorrelated between  $t$ -channel and  $tt$ .

The impact of the flavour composition on the modelling of the  $W+$  jets distributions is determined by propagating an uncertainty of  $50\%$  in the ratio of the  $W + bb$  and  $W + cc$  contributions. As reported in section 8,  $W+$  light-jets events give a small contribution in the signal region and no associated modelling uncertainty is taken into account. An additional shape modelling uncertainty is considered for the  $W+$  jets contribution by applying an event-by-event shape reweighting procedure. This reweighting is derived in the  $W+$  jets validation region from the matching to the data (after subtraction of all processes other than  $W+$  jets) in the distribution of the  $p_{\mathrm{T}}$  of the  $W$  boson.

Systematic uncertainties related to the PDF sets are evaluated for all processes, except for the multijet contribution, in a correlated way. The uncertainty is estimated, following a procedure based on the PDF4LHC prescription [87], by calculating a multidimensional envelope of the uncertainties at  $68\%$  CL of the CT10, MSTW2008 NLO and NNPDF2.3 [89] PDF sets. Additionally, an uncertainty due to possible non-linearities in the polarisation, while not statistically significant, is propagated to the final likelihood contours.

The size of simulation samples. The statistical uncertainty due to the size of simulated background event samples enters through the background coefficients and is estimated during the OSDE analysis of simulated background events. It is evaluated by subtracting, in quadrature, the covariance of the deconvolved coefficients with and without the inclusion of the statistical uncertainties from the background. The statistical uncertainty due to the size of simulated signal event samples enters through the migration matrix and is evaluated by subdividing the simulated signal event samples into 16 equally-sized subsamples. Migration matrices are computed for each subsample, each one being used to deconvolve the full nominal simulation signal sample. From the extracted values for  $\vec{a}$ , a covariance matrix is determined, reflecting the size of the MC samples.

The expected statistical uncertainty due to the size of the data sample is evaluated from pseudoexperiments. The covariance matrix is evaluated for each experiment and the matrices are then averaged. The result is taken to be the expected covariance for the signal. The square root of the diagonal elements are the predicted uncertainties in the coefficients.

Table 2 shows the contribution of each source of systematic uncertainty to the most sensitive helicity parameters and coupling ratios. The total systematic uncertainty is obtained by adding in quadrature all the individual systematic uncertainties and the MC statistics uncertainties. Finally, the total statistical and systematic uncertainty is computed by adding all contributions in quadrature.

The leading systematic uncertainties for  $f_{1}$  come from the jet measurements and the generator modelling. For this parameter, the size of the data sample is also an important source of uncertainty. In the case of  $\delta_{-}$ , the leading systematic uncertainties are jet measurements, the generator modelling and MC sample sizes. The measurement of  $\delta_{-}$  is dominated by the statistical uncertainty in the data. The leading systematic uncertainties for  $\mathrm{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  and  $\mathrm{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  are the same as for  $f_{1}$  and  $\delta_{-}$ , respectively.

# 11 Results

In this section, measurements, limits and distributions obtained from a numerical calculation of the likelihood function (eq. (9.7)) are shown in the space of the generalised helicity fractions and phases  $\vec{\alpha} \equiv \{f_1, f_1^+, f_0^+, \delta_+, \delta_-\}$  and  $P$ , or alternatively of the anomalous couplings  $V_{\mathrm{L,R}}$ ,  $g_{\mathrm{L,R}}$ , and  $P$ . No external constraints or assumptions are imposed on couplings. Values for parameters of interest can be obtained from likelihood profiles, or joint likelihood contours which show the correlations between the extracted parameters.

Likelihood profiles and a joint likelihood contour for the quantities  $f_0^+$  and  $f_1^+$  are shown in figure 9. The  $68\%$  contours represent the total uncertainty in the measurement.

The limit for  $f_0^+$ , i.e. for the fraction of  $b$ -quarks that are right-handed in events with longitudinally polarised  $W$  bosons, is

$$
f _ {0} ^ {+} <   0.041 \quad (68 \% \mathrm {CL}),
$$

$$
f _ {0} ^ {+} <   0.085 \quad (95 \% \mathrm {CL}),
$$

Table 2. Statistical and systematic uncertainties in the measurement of helicity parameters  $f_{1}$  and  $\delta_{-}$ , and of coupling ratios  $\mathrm{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  and  $\mathrm{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$ . Uncertainties from individual sources are estimated separately for shifts up and down, and symmetrised uncertainties  $\sigma(f_{1})$  and  $\sigma(\delta_{-})$ , and  $\sigma(\mathrm{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right])$  and  $\sigma(\mathrm{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right])$  are given. The statistical uncertainty is calculated by evaluating the likelihood including only the covariance matrix,  $\mathbf{V}$ , arising from the data statistics. The total uncertainty is calculated by including  $\mathbf{V}_{\mathrm{syst}}$  in the likelihood calculation as well as  $\mathbf{V}$ . Finally, the total systematic uncertainty is computed by subtracting in quadrature the statistical uncertainty from the total uncertainty.  

<table><tr><td rowspan="2">Source</td><td colspan="2">Helicity parameters</td><td colspan="2">Coupling ratios</td></tr><tr><td>σ(f1)</td><td>σ(δ-) / π</td><td>σ(Re [gR/VL])</td><td>σ(Im [gR/VL])</td></tr><tr><td>Statistical</td><td>0.022</td><td>0.013</td><td>0.030</td><td>0.027</td></tr><tr><td>Jets</td><td>0.029</td><td>0.007</td><td>0.039</td><td>0.009</td></tr><tr><td>Leptons</td><td>0.014</td><td>0.002</td><td>0.017</td><td>&lt; 0.001</td></tr><tr><td>ETmiss</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td>Generator</td><td>0.027</td><td>0.006</td><td>0.030</td><td>0.010</td></tr><tr><td>Parton shower and hadronisation</td><td>0.004</td><td>0.003</td><td>&lt; 0.001</td><td>0.003</td></tr><tr><td>PDF variations</td><td>0.008</td><td>0.004</td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td>Background normalisation</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td>Multijet normalisation</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td>W+jets shape</td><td>0.015</td><td>0.005</td><td>0.007</td><td>0.009</td></tr><tr><td>Luminosity</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td>MC sample sizes</td><td>0.009</td><td>0.006</td><td>&lt; 0.001</td><td>0.013</td></tr><tr><td>Other</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td><td>&lt; 0.001</td></tr><tr><td>Total systematic uncertainty</td><td>0.044</td><td>0.010</td><td>0.061</td><td>0.017</td></tr><tr><td>Total</td><td>0.049</td><td>0.017</td><td>0.068</td><td>0.032</td></tr></table>

compared with the SM expectation of  $f_0^+ = 6 \cdot 10^{-5}$ . The limit for  $f_1^+$ , i.e. for the fraction of transversely polarised  $W$  boson decays that are right-handed, is

$$
f_{1}^{+}<  0.053\quad (68\% \mathrm{CL}),
$$

$$
f_{1}^{+}<  0.120\quad (95\% \mathrm{CL}),
$$

compared with the SM expectation  $f_{1}^{+} = 0.001$ .

The limits obtained for  $f_{1}^{+}$  in this analysis are comparable and complementary to those determined from  $F_{\mathrm{R}}$  [24-28], since  $F_{\mathrm{R}} = f_{1}f_{1}^{+}$ . However, the quantity  $f_{0}^{+}$  is not accessible in measurements of the  $W$  boson helicity fractions, as those analyses extract  $F_{0}$ , which only measures the sum of the contributions of both longitudinal amplitudes. The contributions can only be separated in an analysis with polarised top quarks. Since  $f_{1}^{+}$  and  $f_{0}^{+}$  are found to be very small, there is no sensitivity to the relative phase  $\delta_{+}$ .

![](images/16c082130557a7786db7297b61ca769ec990e76eea48ad46e4262a9574b191b7.jpg)  
(a)  $f_0^+$  (stat. + syst.)

![](images/8dc4903aa87e0b5ad141f232cf1f5f655c2aeb0dadda1a8fc6035309e2321f3e.jpg)  
(b)  $f_{1}^{+}$  (stat. + syst.)

![](images/0c627f3cc1321bdb39dd267c2577cb9f7b2f6cb7a53f38b1daa3a945ae3f22ed.jpg)  
(c)  $f_0^+$  vs.  $f_1^+$  (stat. + syst.)  
Figure 9. The likelihood profiles for the parameters (a)  $f_0^+$  and (b)  $f_1^+$  are shown. The black line indicates the evaluated likelihood in each bin of the profiled variable. The red dashed line, which overlaps the  $y$ -axis, represents the SM expectation. Additionally (c), the joint likelihood profile of  $f_0^+$  as a function of  $f_1^+$  is shown. The red point represents the SM expectation while a black x mark indicates the observed value. Both points overlap with the origin of the  $x$ - and  $y$ -axis. The  $68\%$  and  $95\%$  CL regions are shown in green and yellow, respectively.

The likelihood profile for the top-quark polarisation  $P$  is also obtained and it is shown in figure 10. This leads to the following constraint on the top-quark polarisation:

$$
P > 0.86 \quad (68\% \mathrm{CL}),
$$

$$
P > 0.72 \quad (95\% \mathrm{CL}).
$$

This is compatible with the SM prediction of  $P \approx 0.9$  at  $\sqrt{s} = 8 \mathrm{TeV}$  as computed in refs. [3, 38, 39], and with recent measurements of the top-quark polarisation obtained from asymmetries of angular distributions with additional inputs on the values of the charged-lepton spin analysing power [105] and/or the  $W$  boson helicity fractions [34].

For the parameters for which the analysis obtains point estimates rather than limits, i.e. the fraction  $f_{1}$  and the phase  $\delta_{-}$  as discussed in section 1, likelihood profiles and a joint

![](images/5d0d19e1481448cd102a29ac1bc1b9e38485a48d57d67e64b25751cf01d18131.jpg)  
(a)  $P$  (stat. + syst.)  
Figure 10. The likelihood profile for the top-quark polarisation  $P$  is shown. The black line indicates the evaluated likelihood in each bin of the profiled variable. The red dashed line represents the SM expectation. The  $68\%$  and  $95\%$  CL regions are shown in green and yellow, respectively.

likelihood contour are shown in figure 11. These parameters are measured to be

$$
\begin{array}{l} {f _ {1}} = {0. 2 9 6 _ {- 0. 0 2 3} ^ {+ 0. 0 2 0} \left(\mathrm {s t a t .}\right) _ {- 0. 0 4 6} ^ {+ 0. 0 4 3} \left(\mathrm {s y s t .}\right) = 0. 2 9 6 _ {- 0. 0 5 1} ^ {+ 0. 0 4 8},} \\ \delta_ {-} = 0. 0 0 2 \pi_ {- 0. 0 1 4 \pi} ^ {+ 0. 0 1 3 \pi} (\text {s t a t .}) _ {- 0. 0 1 1 \pi} ^ {+ 0. 0 1 0 \pi} (\text {s y s t .}) = 0. 0 0 2 \pi_ {- 0. 0 1 7 \pi} ^ {+ 0. 0 1 6 \pi}. \\ \end{array}
$$

Correlations between the coefficients of figure 8 are taken into account but do not lead to large correlations between these two parameters. The results are compatible with their SM expectations shown in section 2, and improve on the measurements from double-differential angular decay rates done at  $\sqrt{s} = 7$  TeV by the ATLAS Collaboration [33].

The dependence of the parameters  $f_{1}$  and  $\delta_{-}$  on the top-quark mass is evaluated using  $t$ -channel,  $Wt$ -channel,  $s$ -channel, and  $t\bar{t}$  simulation samples with a range of different top-quark masses. A linear dependence is found, resulting from changes in acceptance at different masses, with a slope of  $-0.005\mathrm{GeV}^{-1}$  for  $f_{1}$  and consistent with zero for  $\delta_{-}$ . The uncertainty due to the top-quark mass dependence is not included in the total systematic uncertainty since it has a negligible impact on the results.

The results for the generalised helicity fractions and phases can be interpreted in terms of anomalous couplings by propagating the statistical and systematic uncertainties. Although a parameterisation of  $P$  in terms of anomalous couplings, obtained from LO MC simulations, exists [106], it is not included in this interpretation. Likelihood profiles and joint likelihood contours for these couplings are shown in figures 12 and 13. The  $68\%$  contours represent the total uncertainty in the measurement. The normalised observables measured in this paper are sensitive to ratios of couplings, which are presented normalised to the dominant coupling in the SM,  $V_{\mathrm{L}}$ . The quantities  $f_1^+$  and  $f_0^+$  depend most strongly on two different combinations of  $V_{\mathrm{R}}$  and  $g_{\mathrm{L}}$ , while the quantities  $f_1(1 - f_1^+)$  and  $\delta_{-}$  depend more strongly on  $V_{\mathrm{L}}$  and  $g_{\mathrm{R}}$ . Since the likelihood is determined in terms of all of these quantities simultaneously, no assumptions need to be imposed on couplings in order to produce these distributions. In each case the measured values are consistent with the SM prediction, i.e.  $V_{\mathrm{R}} = g_{\mathrm{L,R}} = 0$ .

![](images/53ccba2d3f897a47f79692b9f922da3adf3a51ed7d39d18473eb02f11d8bdbf9.jpg)  
(a)  $f_{1}$  (stat. + syst.)

![](images/40080f297fda523ebf25777978d945ac48ad10b04dfae30f142b19c30514239a.jpg)  
(b)  $\delta_{-}$  (stat. + syst.)

![](images/1cd3c68b0974e00a410272649f855139f321a1789779500525060c5af9d41c7c.jpg)  
(c)  $\delta_{-}$  vs  $f_{1}$  (stat. + syst.)  
Figure 11. The likelihood profiles for the parameters (a)  $f_{1}$  and (b)  $\delta_{-}$  are shown. The black line indicates the evaluated likelihood in each bin of the profiled variable. The red dashed line represents the SM expectation. Additionally (c), the joint likelihood contour of  $\delta_{-}$  as a function of  $f_{1}$  is shown. The red point represents the SM expectation while a black x mark indicates the observed value. The 68% and 95% CL regions are shown in green and yellow, respectively.

The bounds obtained on  $V_{\mathrm{R}}$  and  $g_{\mathrm{L}}$  are shown in figure 12. As this analysis yields no constraint on  $\delta_{+}$ , no constraint can be placed on the relative phase between  $V_{\mathrm{R}}$  and  $g_{\mathrm{L}}$ . Thus, only bounds on the magnitudes,

$$
\left| V _ {\mathrm {R}} / V _ {\mathrm {L}} \right| <   0.23 \quad (68 \% \mathrm {CL}),
$$

$$
\left| V _ {\mathrm {R}} / V _ {\mathrm {L}} \right| <   0.37 \quad (95 \% \mathrm {CL}),
$$

and

$$
\left| g _ {\mathrm {L}} / V _ {\mathrm {L}} \right| <   0.19 \quad (68 \% \mathrm {CL}),
$$

$$
\left| g _ {\mathrm {L}} / V _ {\mathrm {L}} \right| <   0.29 \quad (95 \% \mathrm {CL}),
$$

![](images/f432975737e07f4bdca8876b21fa786170167be32857abed7b5c0c5afe3d9a4d.jpg)  
(a)  $|V_{\mathrm{R}} / V_{\mathrm{L}}|$  (stat. + syst.)

![](images/806066a0b7a57c400a43167713c8c74b32b0496724a69e872d7165dd78588cee.jpg)  
(b)  $|g_{\mathrm{L}} / V_{\mathrm{L}}|$  (stat. + syst.)

![](images/217268553e035a32a770118947ba6fcb0e43590acf0765d820770c4d98925df2.jpg)  
(c)  $|g_{\mathrm{L}} / V_{\mathrm{L}}|$  vs.  $|V_{\mathrm{R}} / V_{\mathrm{L}}|$  (stat. + syst.)  
Figure 12. The likelihood profiles for the parameters (a)  $|V_{\mathrm{R}} / V_{\mathrm{L}}|$  and (b)  $|g_{\mathrm{L}} / V_{\mathrm{L}}|$  are shown. The black line indicates the evaluated likelihood in each bin of the profiled variable. The red dashed line, which overlaps the  $y$ -axis, represents the SM expectation. Additionally (c), the joint likelihood contour of  $|g_{\mathrm{L}} / V_{\mathrm{L}}|$  as a function of  $|V_{\mathrm{R}} / V_{\mathrm{L}}|$  is shown. The red point, which overlaps with the origin of the  $x$ - and  $y$ -axis, represents the SM expectation while a black x mark indicates the observed value. The  $68\%$  and  $95\%$  CL regions are shown in green and yellow, respectively.

are obtained. Limits on these quantities have been obtained from  $B$ -meson decays [20], and from measurements of  $W$  boson helicity fractions in top-quark decays [24-28], but all of those measurements can only place limits on combinations of couplings, and thus the quoted limits on individual couplings depend on the assumptions made about other couplings.

The propagation of the uncertainties to the  $(\mathrm{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}], \mathrm{Im}[g_{\mathrm{R}} / V_{\mathrm{L}}])$  space gives

$$
\mathrm {R e} \left[ \frac {g _ {\mathrm {R}}}{V _ {\mathrm {L}}} \right] = 0. 0 0 6 _ {- 0. 0 2 8} ^ {+ 0. 0 3 3} (\mathrm {s t a t .}) _ {- 0. 0 5 9} ^ {+ 0. 0 6 3} (\mathrm {s y s t .}) = 0. 0 0 6 _ {- 0. 0 6 5} ^ {+ 0. 0 7 1},
$$

$$
\mathrm {I m} \left[ \frac {g _ {\mathrm {R}}}{V _ {\mathrm {L}}} \right] = - 0. 0 0 5 \pm 0. 0 2 7 (\mathrm {s t a t .}) _ {- 0. 0 1 2} ^ {+ 0. 0 2 1} (\mathrm {s y s t .}) = - 0. 0 0 5 _ {- 0. 0 3 0} ^ {+ 0. 0 3 4}.
$$

![](images/5dfabefa19a63d5867e9c71f1121fc36f9416d170b34dea6aaa90332b733d253.jpg)  
(a)  $\mathrm{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  (stat. + syst.)

![](images/45a71bfff729a87d689f137111ccbade8f18d7cb5aaa7f1269e42f1827d422d7.jpg)  
(b)  $\operatorname{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  (stat. + syst.)

![](images/b2cad476b84141a8c0e73e4c26e852bbe99dd5379f4e825335df2dec2b210dbd.jpg)  
(c)  $\operatorname{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  vs.  $\operatorname{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  (stat. + syst.)  
Figure 13. The likelihood profiles for the parameters (a)  $\mathrm{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  and (b)  $\mathrm{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  are shown. The black line indicates the evaluated likelihood in each bin of the profiled variable. The red dashed line represents the SM expectation. Additionally (c), the joint likelihood contour of  $\mathrm{Im}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  as a function of  $\mathrm{Re}\left[g_{\mathrm{R}} / V_{\mathrm{L}}\right]$  is shown. The red point represents the SM expectation while a black x mark indicates the observed value. The  $68\%$  and  $95\%$  CL regions are shown in green and yellow, respectively.

A linear dependence is found for the coupling ratios on the top-quark mass, which is evaluated with the top-quark mass-variaged samples mentioned before. A slope of  $0.008\mathrm{GeV}^{-1}$  is found for  $\mathrm{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}]$ , while the slope is consistent with zero for  $\mathrm{Im}[g_{\mathrm{R}} / V_{\mathrm{L}}]$ . Similarly to  $f_{1}$  and  $\delta_{-}$ , the uncertainty due to the top-quark mass dependence is not included in the total systematic uncertainty since it has no significant impact on the results.

Confidence intervals are placed simultaneously on the values of the ratio of the anomalous couplings  $g_{\mathrm{R}}$  and  $V_{\mathrm{L}}$  at  $95\%$  CL,

$$
\operatorname {R e} \left[ \frac {g _ {\mathrm {R}}}{V _ {\mathrm {L}}} \right] \in [ - 0. 1 2, 0. 1 7 ] \quad \text {a n d} \quad \operatorname {I m} \left[ \frac {g _ {\mathrm {R}}}{V _ {\mathrm {L}}} \right] \in [ - 0. 0 7, 0. 0 6 ].
$$

The best constraints on  $\mathrm{Re}[g_{\mathrm{R}}]$  derive from measurements of the  $W$  boson helicity fractions in top-quark pair decays, with  $\mathrm{Re}[g_{\mathrm{R}}] \in [-0.02, 0.06]$  and  $[-0.08, 0.07]$ , both at

$95\%$  CL, from ATLAS at  $\sqrt{s} = 8$  TeV [26] and from CMS at  $\sqrt{s} = 7$  TeV [25], respectively. However, these limits use the measured single-top-quark production cross-section [29, 30] along with the assumption that  $V_{\mathrm{L}} = 1$ ,  $\operatorname{Im}[g_{\mathrm{R}}] = 0$ , and either  $g_{\mathrm{L}} = 0$  or  $V_{\mathrm{R}} = 0$ . Without these assumptions only a circular region in the complex  $g_{\mathrm{R}}$  plane within  $0.0 \lesssim \operatorname{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}] \lesssim 0.8$  can be excluded by  $W$  boson helicity fractions measurements. The measurements presented here require no assumptions in values of the other anomalous couplings, and on their own can exclude large values of  $\operatorname{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}]$ .

Along these lines, from the double-differential angular decay rates in  $t$ -channel single-top-quark events in ATLAS at  $\sqrt{s} = 7\mathrm{TeV}$  [33], confidence intervals are placed simultaneously on the coupling ratios,  $\mathrm{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}] \in [-0.36,0.10]$  and  $\mathrm{Im}[g_{\mathrm{R}} / V_{\mathrm{L}}] \in [-0.17,0.23]$ , at  $95\%$  CL, assuming  $V_{\mathrm{R}} = g_{\mathrm{L}} = 0$ . Furthermore, slightly better limits on the imaginary part of  $g_{\mathrm{R}}$  are set from asymmetries by ATLAS at  $\sqrt{s} = 8\mathrm{TeV}$ , giving  $\mathrm{Im}[g_{\mathrm{R}}] \in [-0.18,0.06]$  [34], at  $95\%$  CL, assuming again  $V_{\mathrm{R}} = g_{\mathrm{L}} = 0$ . The limits presented in this paper improve on both these results and extend current constraints on  $g_{\mathrm{R}}$  to the whole complex plane by simultaneously measuring information about  $\mathrm{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}]$  and  $\mathrm{Im}[g_{\mathrm{R}} / V_{\mathrm{L}}]$ .

# 12 Conclusion

The analysis presented in this paper uses the triple-differential decay rate in electroweak production and subsequent decay of single top quarks to constrain the complex parameters of the effective Lagrangian that describes the properties of the Wtb vertex. An analysis of angular distributions of the decay products of single top quarks produced in the  $t$ -channel constrains these parameters simultaneously. The analysis is based on  $20.2\mathrm{fb}^{-1}$  of  $pp$  collision data at  $\sqrt{s} = 8\mathrm{TeV}$  collected with the ATLAS detector at the LHC. The selected events contain one isolated electron or muon, large  $E_{\mathrm{T}}^{\mathrm{miss}}$ , and exactly two jets, with one of them identified as likely to contain a  $b$ -hadron. A cut-based analysis is used to discriminate the signal events from background, and the electron and muon channels are merged. An OSDE technique is used to perform an angular analysis of the triple-differential decay rate in order to determine six observables simultaneously, i.e. five generalised helicity fractions and phases, as well as the polarisation of the produced top quark. Detector effects are deconvolved from data using Fourier techniques. The fraction  $f_{1}$  of decays containing transversely polarised  $W$  bosons is measured to be  $f_{1} = 0.30 \pm 0.05$ . The phase  $\delta_{-}$  between amplitudes for transversely and longitudinally polarised  $W$  bosons recoiling against left-handed  $b$ -quarks, is measured to be  $\delta_{-} = 0.002\pi_{-0.017\pi}^{+0.016\pi}$ , giving no indication of CP violation. The fractions of transverse and longitudinal  $W$  bosons accompanied by right-handed  $b$ -quarks are also constrained at  $95\%$  CL to  $f_{1}^{+} < 0.120$  and  $f_{0}^{+} < 0.085$ , respectively. The fractions  $f_{1}$  and  $f_{1}^{+}$ are related to the  $W$  boson helicity fractions ( $F_{\mathrm{R}}$ ,  $F_{0}$ , and  $F_{\mathrm{L}}$ ), while the fraction  $f_{0}^{+}$ , which is previously unmeasured, separates  $F_{0}$  into two components involving left- and right-handed  $b$ -quarks. Based on these measurements,  $95\%$  CL intervals are placed on the ratio of the complex coupling parameters  $g_{\mathrm{R}}$  and  $V_{\mathrm{L}}$  such that  $\operatorname{Re}[g_{\mathrm{R}} / V_{\mathrm{L}}] \in [-0.12, 0.17]$  and  $\operatorname{Im}[g_{\mathrm{R}} / V_{\mathrm{L}}] \in [-0.07, 0.06]$ . Constraints at  $95\%$  CL are also placed on the magnitudes of the ratios  $|V_{\mathrm{R}} / V_{\mathrm{L}}| < 0.37$  and  $|g_{\mathrm{L}} / V_{\mathrm{L}}| < 0.29$ , and the

polarisation of single top quarks in the  $t$ -channel is constrained to be  $P > 0.72$  (95% CL). None of the above measurements make assumptions about the value of any of the other parameters or couplings and all of them are in agreement with the SM expectations.

# Acknowledgments

We thank CERN for the very successful operation of the LHC, as well as the support staff from our institutions without whom ATLAS could not be operated efficiently.

We acknowledge the support of ANPCyT, Argentina; YerPhI, Armenia; ARC, Australia; BMWFW and FWF, Austria; ANAS, Azerbaijan; SSTC, Belarus; CNPq and FAPESP, Brazil; NSERC, NRC and CFI, Canada; CERN; CONICYT, Chile; CAS, MOST and NSFC, China; COLCIENCIAS, Colombia; MSMT CR, MPO CR and VSC CR, Czech Republic; DNRF and DNSRC, Denmark; IN2P3-CNRS, CEA-DSM/IRFU, France; SRNSF, Georgia; BMBF, HGF, and MPG, Germany; GSRT, Greece; RGC, Hong Kong SAR, China; ISF, I-CORE and Benoziyo Center, Israel; INFN, Italy; MEXT and JSPS, Japan; CNRST, Morocco; NWO, Netherlands; RCN, Norway; MNiSW and NCN, Poland; FCT, Portugal; MNE/IFA, Romania; MES of Russia and NRC KI, Russian Federation; JINR; MESTD, Serbia; MSSR, Slovakia; ARRS and MIZŠ, Slovenia; DST/NRF, South Africa; MINECO, Spain; SRC and Wallenberg Foundation, Sweden; SERI, SNSF and Cantons of Bern and Geneva, Switzerland; MOST, Taiwan; TAEK, Turkey; STFC, United Kingdom; DOE and NSF, United States of America. In addition, individual groups and members have received support from BCKDF, the Canada Council, CANARIE, CRC, Compute Canada, FQRNT, and the Ontario Innovation Trust, Canada; EPLANET, ERC, ERDF, FP7, Horizon 2020 and Marie Skłodowska-Curie Actions, European Union; Investissements d'Avenir Labex and Idex, ANR, Région Auvergne and Fondation Partager le Savoir, France; DFG and AvH Foundation, Germany; Herakleitos, Thales and Aristeia programmes co-financed by EU-ESF and the Greek NSRF; BSF, GIF and Minerva, Israel; BRF, Norway; CERCA Programme Generalitat de Catalunya, Generalitat Valenciana, Spain; the Royal Society and Leverhulme Trust, United Kingdom.

The crucial computing support from all WLCG partners is acknowledged gratefully, in particular from CERN, the ATLAS Tier-1 facilities at TRIUMF (Canada), NDGF (Denmark, Norway, Sweden), CC-IN2P3 (France), KIT/GridKA (Germany), INFN-CNAF (Italy), NL-T1 (Netherlands), PIC (Spain), ASGC (Taiwan), RAL (UK) and BNL (USA), the Tier-2 facilities worldwide and large non-WLCG resource providers. Major contributors of computing resources are listed in ref. [107].

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] ATLAS, CDF, CMS and D0 collaborations, First combination of Tevatron and LHC measurements of the top-quark mass, arXiv:1403.4427 [INSPIRE].  
[2] I.I.Y. Bigi, Y.L. Dokshitzer, V.A. Khoze, J.H. Kuhn and P.M. Zerwas, Production and Decay Properties of Ultraheavy Quarks, Phys. Lett. B 181 (1986) 157 [INSPIRE].  
[3] M. Jezabek and J.H. Kuhn, V-A tests through leptons from polarized top quarks, Phys. Lett. B 329 (1994) 317 [hep-ph/9403366] [INSPIRE].  
[4] G. Mahlon and S.J. Parke, Angular correlations in top quark pair production and decay at hadron colliders, Phys. Rev. D 53 (1996) 4886 [hep-ph/9512264] [INSPIRE].  
[5] L. Evans and P. Bryant, LHC Machine, 2008 JINST 3 S08001 [INSPIRE].  
[6] N. Kidonakis, Next-to-  $n e x t$ -to-leading-order collinear and soft gluon corrections for  $t$ -channel single top quark production, Phys. Rev. D 83 (2011) 091503 [arXiv:1103.2792] [INSPIRE].  
[7] A.D. Martin, W.J. Stirling, R.S. Thorne and G. Watt, *Parton distributions for the LHC*, Eur. Phys. J. C **63** (2009) 189 [arXiv:0901.0002] [INSPIRE].  
[8] A.D. Martin, W.J. Stirling, R.S. Thorne and G. Watt, Uncertainties on  $\alpha_{s}$  in global PDF analyses and implications for predicted hadronic cross sections, Eur. Phys. J. C 64 (2009) 653 [arXiv:0905.3531] [INSPIRE].  
[9] G. Mahlon and S.J. Parke, Improved spin basis for angular correlation studies in single top quark production at the Tevatron, Phys. Rev. D 55 (1997) 7249 [hep-ph/9611367] [INSPIRE].  
[10] C.S. Li, R.J. Oakes and T.C. Yuan, QCD corrections to  $t \to W^{+}b$ , Phys. Rev. D 43 (1991) 3759 [INSPIRE].  
[11] G.L. Kane, G.A. Ladinsky and C.P. Yuan, Using the Top Quark for Testing Standard Model Polarization and CP Predictions, Phys. Rev. D 45 (1992) 124 [INSPIRE].  
[12] W. Buchmüller and D. Wyler, Effective Lagrangian Analysis of New Interactions and Flavor Conservation, Nucl. Phys. B 268 (1986) 621 [INSPIRE].  
[13] C. Zhang and S. Willenbrock, *Effective-field-theory approach to top-quark production and decay*, Phys. Rev. D 83 (2011) 034006 [arXiv:1008.3869] [INSPIRE].  
[14] K.G. Wilson, Nonlagrangian models of current algebra, Phys. Rev. 179 (1969) 1499 [INSPIRE].  
[15] F. del Aguila and J.A. Aguilar-Saavedra, Precise determination of the Wtb couplings at CERN LHC, Phys. Rev. D 67 (2003) 014009 [hep-ph/0208171] [INSPIRE].  
[16] J.A. Aguilar-Saavedra, J. Carvalho, N.F. Castro, F. Veloso and A. Onofre, Probing anomalous Wtb couplings in top pair decays, Eur. Phys. J. C 50 (2007) 519 [hep-ph/0605190] [INSPIRE].  
[17] J.A. Aguilar-Saavedra, A minimal set of top anomalous couplings, Nucl. Phys. B 812 (2009) 181 [arXiv:0811.3842] [INSPIRE].  
[18] J.A. Aguilar-Saavedra, A Minimal set of top-Higgs anomalous couplings, Nucl. Phys. B 821 (2009) 215 [arXiv:0904.2387] [INSPIRE].  
[19] J.A. Aguilar-Saavedra and J. Bernabéu, W polarization beyond helicity fractions in top quark decays, Nucl. Phys. B 840 (2010) 349 [arXiv:1005.5382] [INSPIRE].

[20] B. Grzadkowski and M. Misiak, Anomalous Wtb coupling effects in the weak radiative  $B$ -meson decay, Phys. Rev. D 78 (2008) 077501 [Erratum ibid. D 84 (2011) 059903] [arXiv:0802.1413] [INSPIRE].  
[21] Q.-H. Cao, B. Yan, J.-H. Yu and C. Zhang, A General Analysis of Wtb anomalous Couplings, Chin. Phys. C 41 (2017) 063101 [arXiv:1504.03785] [INSPIRE].  
[22] V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Is there room for CP-violation in the top-Higgs sector?, Phys. Rev. D 94 (2016) 016002 [arXiv:1603.03049] [INSPIRE].  
[23] V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Constraining the top-Higgs sector of the standard model effective field theory, Phys. Rev. D 94 (2016) 034031 [arXiv:1605.04311] [INSPIRE].  
[24] ATLAS collaboration, Measurement of the W boson polarization in top quark decays with the ATLAS detector, JHEP 06 (2012) 088 [arXiv:1205.2484] [INSPIRE].  
[25] CMS collaboration, Measurement of the W-boson helicity in top-quark decays from  $\bar{t} \bar{t}$  production in lepton+jets events in pp collisions at  $\sqrt{s} = 7$  TeV, JHEP 10 (2013) 167 [arXiv:1308.3879] [INSPIRE].  
[26] ATLAS collaboration, Measurement of the W boson polarisation in  $\bar{t} \bar{t}$  events from pp collisions at  $\sqrt{s} = 8$  TeV in the lepton + jets channel with ATLAS, Eur. Phys. J. C 77 (2017) 264 [arXiv:1612.02577] [INSPIRE].  
[27] CMS collaboration, Measurement of the W boson helicity fractions in the decays of top quark pairs to lepton + jets final states produced in pp collisions at  $\sqrt{s} = 8$  TeV, Phys. Lett. B 762 (2016) 512 [arXiv:1605.09047] [INSPIRE].  
[28] CMS collaboration, Measurement of the  $W$  boson helicity in events with a single reconstructed top quark in pp collisions at  $\sqrt{s} = 8$  TeV, JHEP 01 (2015) 053 [arXiv:1410.1154] [INSPIRE].  
[29] ATLAS collaboration, Comprehensive measurements of t-channel single top-quark production cross sections at  $\sqrt{s} = 7$  TeV with the ATLAS detector, Phys. Rev. D 90 (2014) 112006 [arXiv:1406.7844] [INSPIRE].  
[30] CMS collaboration, Measurement of the single-top-quark  $t$ -channel cross section in pp collisions at  $\sqrt{s} = 7$  TeV, JHEP 12 (2012) 035 [arXiv:1209.4533] [INSPIRE].  
[31] CMS collaboration, Measurement of the t-channel single-top-quark production cross section and of the  $|V_{tb}|$  CKM matrix element in pp collisions at  $\sqrt{s} = 8$  TeV, JHEP 06 (2014) 090 [arXiv:1403.7366] [INSPIRE].  
[32] J.L. Birman, F. Deliot, M.C.N. Fiolhais, A. Onofre and C.M. Pease, New limits on anomalous contributions to the Wtb vertex, Phys. Rev. D 93 (2016) 113021 [arXiv:1605.02679] [INSPIRE].  
[33] ATLAS collaboration, Search for anomalous couplings in the Wtb vertex from the measurement of double differential angular decay rates of single top quarks produced in the  $t$ -channel with the ATLAS detector, JHEP 04 (2016) 023 [arXiv:1510.03764] [INSPIRE].  
[34] ATLAS collaboration, Probing the W tb vertex structure in t-channel single-top-quark production and decay in pp collisions at  $\sqrt{s} = 8$  TeV with the ATLAS detector, JHEP 04 (2017) 124 [arXiv:1702.08309] [INSPIRE].  
[35] CMS collaboration, Search for anomalous Wtb couplings and flavour-changing neutral currents in t-channel single top quark production in pp collisions at  $\sqrt{s} = 7$  and 8 TeV, JHEP 02 (2017) 028 [arXiv:1610.03545] [INSPIRE].

[36] J. Boudreau, C. Escobar, J. Mueller, K. Sapp and J. Su, Single top quark differential decay rate formulae including detector effects, arXiv:1304.5639 [INSPIRE].  
[37] J. Boudreau, C. Escobar, J. Mueller and J. Su, Deconvolving the detector in Fourier space, J. Phys. Conf. Ser. 762 (2016) 012041.  
[38] G. Mahlon and S.J. Parke, *Single top quark production at the LHC: Understanding spin*, Phys. Lett. B **476** (2000) 323 [hep-ph/9912458] [INSPIRE].  
[39] R. Schwienhorst, C.P. Yuan, C. Mueller and Q.-H. Cao, Single top quark production and decay in the t-channel at next-to-leading order at the LHC, Phys. Rev. D 83 (2011) 034019 [arXiv:1012.5132] [INSPIRE].  
[40] M. Fischer, S. Groote, J.G. Korner and M.C. Mauser, Complete angular analysis of polarized top decay at  $O(\alpha_{s})$ , Phys. Rev. D 65 (2002) 054036 [hep-ph/0101322] [INSPIRE].  
[41] A. Czarnecki, J.G. Korner and J.H. Piclum, Helicity fractions of  $W$  bosons from top quark decays at NNLO in QCD, Phys. Rev. D 81 (2010) 111503 [arXiv:1005.2625] [INSPIRE].  
[42] M. Jacob and G.C. Wick, On the general theory of collisions for particles with spin, Annals Phys. 7 (1959) 404 [INSPIRE].  
[43] J.D. Richman, An Experimenter's Guide to the Helicity Formalism, CALT-68-1148 (1984) [INSPIRE].  
[44] ATLAS collaboration, The ATLAS Experiment at the CERN Large Hadron Collider, 2008 JINST 3 S08003 [INSPIRE].  
[45] ATLAS collaboration, The performance of the jet trigger for the ATLAS detector during 2011 data taking, Eur. Phys. J. C 76 (2016) 526 [arXiv:1606.07759] [INSPIRE].  
[46] ATLAS collaboration, Luminosity determination in pp collisions at  $\sqrt{s} = 8$  TeV using the ATLAS detector at the LHC, Eur. Phys. J. C 76 (2016) 653 [arXiv:1608.03953] [INSPIRE].  
[47] ATLAS collaboration, Performance of the ATLAS muon trigger in pp collisions at  $\sqrt{s} = 8$  TeV, Eur. Phys. J. C 75 (2015) 120 [arXiv:1408.3179] [INSPIRE].  
[48] T. Sjöstrand, S. Mrenna and P.Z. Skands, A brief introduction to PYTHIA 8.1, Comput. Phys. Commun. 178 (2008) 852 [arXiv:0710.3820] [INSPIRE].  
[49] S. Frixione, P. Nason and C. Oleari, Matching NLO QCD computations with Parton Shower simulations: the POWHEG method, JHEP 11 (2007) 070 [arXiv:0709.2092] [INSPIRE].  
[50] H.-L. Lai et al., New parton distributions for collider physics, Phys. Rev. D 82 (2010) 074024 [arXiv:1007.2241] [INSPIRE].  
[51] R. Frederix, E. Re and P. Torrielli, Single-top t-channel hadroproduction in the four-flavour scheme with POWHEG and aMC@NLO, JHEP 09 (2012) 130 [arXiv:1207.5391] [INSPIRE].  
[52] P. Artoisenet, R. Frederix, O. Mattelaer and R. Rietkerk, Automatic spin-entangled decays of heavy resonances in Monte Carlo simulations, JHEP 03 (2013) 015 [arXiv:1212.3460] [INSPIRE].  
[53] J.A. Aguilar-Saavedra, *Single top quark production at LHC with anomalous Wtb couplings*, Nucl. Phys. B **804** (2008) 160 [arXiv:0803.3810] [INSPIRE].  
[54] J. Pumplin, D.R. Stump, J. Huston, H.L. Lai, P.M. Nadolsky and W.K. Tung, New generation of parton distributions with uncertainties from global QCD analysis, JHEP 07 (2002) 012 [hep-ph/0201195] [INSPIRE].

[55] B.P. Kersevan and E. Richter-Was, The Monte Carlo event generator AcerMC versions 2.0 to 3.8 with interfaces to PYTHIA 6.4, HERWIG 6.5 and ARIADNE 4.1, Comput. Phys. Commun. 184 (2013) 919 [hep-ph/0405247] [INSPIRE].  
[56] B.P. Kersevan and I. Hinchliffe, A consistent prescription for the production involving massive quarks in hadron collisions, JHEP 09 (2006) 033 [hep-ph/0603068] [INSPIRE].  
[57] S.S.D. Willenbrock and D.A. Dicus, Production of heavy quarks from W gluon fusion, Phys. Rev. D 34 (1986) 155 [INSPIRE].  
[58] ATLAS collaboration, Comparison of Monte Carlo generator predictions to ATLAS measurements of top pair production at 7 TeV, ATL-PHYS-PUB-2015-002 (2015).  
[59] T. Sjöstrand, S. Mrenna and P.Z. Skands, PYTHIA 6.4 physics and manual, JHEP 05 (2006) 026 [hep-ph/0603175] [INSPIRE].  
[60] P.Z. Skands, Tuning Monte Carlo Generators: The Perugia Tunes, Phys. Rev. D 82 (2010) 074018 [arXiv:1005.3457] [INSPIRE].  
[61] S. Jadach, J.H. Kuhn and Z. Was, TAUOLA: a library of Monte Carlo programs to simulate decays of polarized tau leptons, Comput. Phys. Commun. 64 (1990) 275 [INSPIRE].  
[62] P. Golonka and Z. Was, PHOTOS Monte Carlo: a precision tool for QED corrections in  $Z$  and  $W$  decays, Eur. Phys. J. C 45 (2006) 97 [hep-ph/0506026] [INSPIRE].  
[63] T. Gleisberg et al., Event generation with SHERPA 1.1, JHEP 02 (2009) 007 [arXiv:0811.4622] [INSPIRE].  
[64] S. Hoeche, F. Krauss, S. Schumann and F. Siegert, QCD matrix elements and truncated showers, JHEP 05 (2009) 053 [arXiv:0903.1219] [INSPIRE].  
[65] ATLAS collaboration, The ATLAS simulation infrastructure, Eur. Phys. J. C 70 (2010) 823 [arXiv:1005.4568] [INSPIRE].  
[66] GEANT4 collaboration, S. Agostinelli et al., GEANT4: a simulation toolkit, Nucl. Instrum. Meth. A 506 (2003) 250 [INSPIRE].  
[67] E. Richter-Was, D. Froidevaux and L. Poggioli, ATLFAST 2.0 a fast simulation package for ATLAS, ATL-PHYS-98-131 (1998).  
[68] ATLAS collaboration, Electron reconstruction and identification efficiency measurements with the ATLAS detector using the 2011 LHC proton-proton collision data, Eur. Phys. J. C 74 (2014) 2941 [arXiv:1404.2240] [INSPIRE].  
[69] ATLAS collaboration, Measurement of the muon reconstruction performance of the ATLAS detector using 2011 and 2012 LHC proton-proton collision data, Eur. Phys. J. C 74 (2014) 3130 [arXiv:1407.3935] [INSPIRE].  
[70] ATLAS collaboration, Estimation of non-prompt and fake lepton backgrounds in final states with top quarks produced in proton-proton collisions at  $\sqrt{s} = 8$  TeV with the ATLAS detector, ATLAS-CONF-2014-058 (2014).  
[71] M. Cacciari, G.P. Salam and G. Soyez, The anti- $k(t)$  jet clustering algorithm, JHEP 04 (2008) 063 [arXiv:0802.1189] [INSPIRE].  
[72] M. Cacciari, G.P. Salam and G. Soyez, FastJet user manual, Eur. Phys. J. C 72 (2012) 1896 [arXiv:1111.6097] [INSPIRE].  
[73] ATLAS collaboration, Topological cell clustering in the ATLAS calorimeters and its performance in LHC Run 1, Eur. Phys. J. C 77 (2017) 490 [arXiv:1603.02934] [INSPIRE].

[74] ATLAS collaboration, Jet energy measurement and its systematic uncertainty in proton-proton collisions at  $\sqrt{s} = 7$  TeV with the ATLAS detector, Eur. Phys. J. C **75** (2015) 17 [arXiv:1406.0076] [INSPIRE].  
[75] ATLAS collaboration, Performance of pile-up mitigation techniques for jets in pp collisions at  $\sqrt{s} = 8$  TeV using the ATLAS detector, Eur. Phys. J. C 76 (2016) 581 [arXiv:1510.03823] [INSPIRE].  
[76] ATLAS collaboration, Performance of b-jet identification in the ATLAS experiment, 2016 JINST 11 P04008 [arXiv:1512.01094] [INSPIRE].  
[77] ATLAS collaboration, Calibration of the performance of  $b$ -tagging for  $c$  and light-flavour jets in the 2012 ATLAS data, ATLAS-CONF-2014-046 (2014).  
[78] ATLAS collaboration, Calibration of b-tagging using dileptonic top pair events in a combinatorial likelihood approach with the ATLAS experiment, ATLAS-CONF-2014-004 (2014).  
[79] ATLAS collaboration, Performance of Missing Transverse Momentum Reconstruction in ATLAS studied in Proton-Proton Collisions recorded in 2012 at 8 TeV, ATLAS-CONF-2013-082 (2013).  
[80] ATLAS collaboration, Fiducial, total and differential cross-section measurements of t-channel single top-quark production in pp collisions at 8TeV using data collected by the ATLAS detector, Eur. Phys. J. C 77 (2017) 531 [arXiv:1702.02859] [INSPIRE].  
[81] P. Bärnreuther, M. Czakon and A. Mitov, Percent Level Precision Physics at the Tevatron: First Genuine NNLO QCD Corrections to  $q\bar{q} \rightarrow t\bar{t} + X$ , Phys. Rev. Lett. 109 (2012) 132001 [arXiv:1204.5201] [INSPIRE].  
[82] M. Czakon and A. Mitov, Top++: A Program for the Calculation of the Top-Pair Cross-Section at Hadron Colliders, Comput. Phys. Commun. 185 (2014) 2930 [arXiv:1112.5675] [INSPIRE].  
[83] M. Czakon and A. Mitov, NNLO corrections to top-pair production at hadron colliders: the all-fermionic scattering channels, JHEP 12 (2012) 054 [arXiv:1207.0236] [INSPIRE].  
[84] M. Czakon and A. Mitov, NNLO corrections to top pair production at hadron colliders: the quark-gluon reaction, JHEP 01 (2013) 080 [arXiv:1210.6832] [INSPIRE].  
[85] M. Czakon, P. Fiedler and A. Mitov, Total Top-Quark Pair-Production Cross section at Hadron Colliders Through  $O(\alpha_S^4)$ , Phys. Rev. Lett. 110 (2013) 252004 [arXiv:1303.6254] [INSPIRE].  
[86] M. Cacciari, M. Czakon, M. Mangano, A. Mitov and P. Nason, Top-pair production at hadron colliders with next-to-  $n$  ext-to-leading logarithmic soft-gluon resummation, Phys. Lett. B 710 (2012) 612 [arXiv:1111.5869] [INSPIRE].  
[87] M. Botje et al., The PDF4LHC Working Group Interim Recommendations, arXiv:1101.0538 [INSPIRE].  
[88] J. Gao et al., CT10 next-to-  $n e x t$ -to-  $n e x t$ -leading order global analysis of QCD, Phys. Rev. D 89 (2014) 033009 [arXiv:1302.6246] [INSPIRE].  
[89] R.D. Ball et al., Parton distributions with LHC data, Nucl. Phys. B 867 (2013) 244 [arXiv:1207.1303] [INSPIRE].  
[90] N. Kidonakis, Two-loop soft anomalous dimensions for single top quark associated production with a  $W^{-}$  or  $H^{-}$ , Phys. Rev. D 82 (2010) 054018 [arXiv:1005.4451] [INSPIRE].

[91] N. Kidonakis, NNLL resummation for s-channel single top quark production, Phys. Rev. D 81 (2010) 054028 [arXiv:1001.5034] [INSPIRE].  
[92] C. Anastasiou, L.J. Dixon, K. Melnikov and F. Petriello, High precision QCD at hadron colliders: Electroweak gauge boson rapidity distributions at NNLO, Phys. Rev. D 69 (2004) 094008 [hep-ph/0312266] [INSPIRE].  
[93] J.M. Campbell, R.K. Ellis and C. Williams, Vector boson pair production at the LHC, JHEP 07 (2011) 018 [arXiv:1105.0020] [INSPIRE].  
[94] F.A. Berends, H. Kuijf, B. Tausk and W.T. Giele, On the production of a  $W$  and jets at hadron colliders, Nucl. Phys. B 357 (1991) 32 [INSPIRE].  
[95] ATLAS collaboration, Measurement of the top quark pair production cross-section with ATLAS in the single lepton channel, Phys. Lett. B 711 (2012) 244 [arXiv:1201.1889] [INSPIRE].  
[96] ATLAS collaboration, Measurement of the t-channel single top-quark production cross section in pp collisions at  $\sqrt{s} = 7$  TeV with the ATLAS detector, Phys. Lett. B 717 (2012) 330 [arXiv:1205.3130] [INSPIRE].  
[97] P. Bialas, J.G. Korner, M. Krämer and K. Zalewski, Joint angular decay distributions in exclusive weak decays of heavy mesons and baryons, Z. Phys. C 57 (1993) 115 [INSPIRE].  
[98] S.C. Schwartz, Estimation of Probability Density by an Orthogonal Series, Ann. Math. Statist. 38 (1967) 1261.  
[99] S. Brooks, A. Gelman, G. Jones and X.-L. Meng, Handbook of Markov Chain Monte Carlo, Chapman & Hall/CRC Handbooks of Modern Statistical Methods, CRC Press, Boca Raton U.S.A. (2011).  
[100] ATLAS collaboration, Jet energy resolution in proton-proton collisions at  $\sqrt{s} = 7$  TeV recorded in 2010 with the ATLAS detector, Eur. Phys. J. C 73 (2013) 2306 [arXiv:1210.6210] [INSPIRE].  
[101] J. Alwall, R. Frederix, S. Frixione, V. Hirschi, F. Maltoni, O. Mattelaer et al., The automated computation of tree-level and next-to-leading order differential cross sections and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[102] G. Corcella et al., HERWIG 6: An Event generator for hadron emission reactions with interfering gluons (including supersymmetric processes), JHEP 01 (2001) 010 [hep-ph/0011363] [INSPIRE].  
[103] ATLAS collaboration, New ATLAS event generator tunes to 2010 data, ATL-PHYS-PUB-2011-008 (2011).  
[104] S. Frixione and B.R. Webber, Matching NLO QCD computations and parton shower simulations, JHEP 06 (2002) 029 [hep-ph/0204244] [INSPIRE].  
[105] CMS collaboration, Measurement of top quark polarisation in t-channel single top quark production, JHEP 04 (2016) 073 [arXiv:1511.02138] [INSPIRE].  
[106] J.A. Aguilar-Saavedra and S. Amor Dos Santos, New directions for top quark polarization in the  $t$ -channel process, Phys. Rev. D 89 (2014) 114009 [arXiv:1404.1585] [INSPIRE].  
[107] ATLAS collaboration, ATLAS Computing Acknowledgements 2016-2017, ATL-GEN-PUB-2016-002 (2016).

# The ATLAS collaboration

M. Aaboud $^{137d}$ , G. Aad $^{88}$ , B. Abbott $^{115}$ , J. Abdallah $^{8}$ , O. Abdinov $^{12,*}$ , B. Abeloos $^{119}$  
S.H. Abidi $^{161}$ , O.S. AbouZeid $^{139}$ , N.L. Abraham $^{151}$ , H. Abramowicz $^{155}$ , H. Abreu $^{154}$ ,  
R. Abreu $^{118}$ , Y. Abulaiti $^{148a,148b}$ , B.S. Acharya $^{167a,167b,a}$ , S. Adachi $^{157}$ , L. Adamczyk $^{41a}$  
J. Adelman $^{110}$ , M. Adersberger $^{102}$ , T. Adye $^{133}$ , A.A. Affolder $^{139}$ , T. Agatonovic-Jovin $^{14}$  
C. Agheorghiesei $^{28c}$ , J.A. Aguilar-Saavedra $^{128a,128f}$ , S.P. Ahlen $^{24}$ , F. Ahmadov $^{68,b}$  
G. Aielli $^{135a,135b}$ , S. Akatsuka $^{71}$ , H. Akerstedt $^{148a,148b}$ , T.P.A. Åkesson $^{84}$ , E. Akilli $^{52}$  
A.V. Akimov $^{98}$ , G.L. Alberghi $^{22a,22b}$ , J. Albert $^{172}$ , P. Albicocco $^{50}$ , M.J. Alconada Verzini $^{74}$ ,  
M. Aleksa $^{32}$ , I.N. Aleksandrov $^{68}$ , C. Alexa $^{28b}$ , G. Alexander $^{155}$ , T. Alexopoulos $^{10}$ , M. Alhroob $^{115}$  
B. Ali $^{130}$ , M. Aliev $^{76a,76b}$ , G. Alimonti $^{94a}$ , J. Alison $^{33}$ , S.P. Alkire $^{38}$ , B.M.M. Allbrooke $^{151}$ ,  
B.W. Allen $^{118}$ , P.P. Allport $^{19}$ , A. Aloisio $^{106a,106b}$ , A. Alonso $^{39}$ , F. Alonso $^{74}$ , C. Alpigiani $^{140}$  
A.A. Alshehri $^{56}$ , M.I. Alstaty $^{88}$ , B. Alvarez Gonzalez $^{32}$ , D. Álvarez Piqueras $^{170}$  
M.G. Alviggi $^{106a,106b}$ , B.T. Amadio $^{16}$ , Y. Amaral Coutinho $^{26a}$ , C. Amelung $^{25}$ , D. Amidei $^{92}$  
S.P. Amor Dos Santos $^{128a,128c}$ , A. Amorim $^{128a,128b}$ , S. Amoroso $^{32}$ , G. Amundsen $^{25}$ ,  
C. Anastopoulos $^{141}$ , L.S. Ancu $^{52}$ , N. Andari $^{19}$ , T. Andeen $^{11}$ , C.F. Anders $^{60b}$ , J.K. Anders $^{77}$  
K.J. Anderson $^{33}$ , A. Andreazza $^{94a,94b}$ , V. Andrei $^{60a}$ , S. Angelidakis $^{9}$ , I. Angelozzi $^{109}$ ,  
A. Angerami $^{38}$ , A.V. Anisenkov $^{111,c}$ , N. Anjos $^{13}$ , A. Annovi $^{126a,126b}$ , C. Antel $^{60a}$ , M. Antonelli $^{50}$  
A. Antonov<sup>100,*</sup>, D.J. Antrim<sup>166</sup>, F. Anulli<sup>134a</sup>, M. Aoki<sup>69</sup>, L. Aperio Bella<sup>32</sup>, G. Arabidze<sup>93</sup>,  
Y. Arai $^{69}$ , J.P. Araque $^{128a}$ , V. Araujo Ferraz $^{26a}$ , A.T.H. Arce $^{48}$ , R.E. Ardell $^{80}$ , F.A. Arduh $^{74}$ .  
J-F. Arguin $^{97}$ , S. Argyropoulos $^{66}$ , M. Arik $^{20a}$ , A.J. Armbruster $^{32}$ , L.J. Armitage $^{79}$ , O. Arnaez $^{161}$  
H. Arnold $^{51}$ , M. Arratia $^{30}$ , O. Arslan $^{23}$ , A. Artamonov $^{99}$ , G. Artoni $^{122}$ , S. Artz $^{86}$ , S. Asai $^{157}$  
N. Asbah<sup>45</sup>, A. Ashkenazi<sup>155</sup>, L. Asquith<sup>151</sup>, K. Assamagan<sup>27</sup>, R. Astalos<sup>146a</sup>, M. Atkinson<sup>169</sup>,  
N.B. Atlay $^{143}$ , K. Augsten $^{130}$ , G. Avolio $^{32}$ , B. Axen $^{16}$ , M.K. Ayoub $^{119}$ , G. Azuelos $^{97,d}$  
A.E. Baas $^{60a}$ , M.J. Baca $^{19}$ , H. Bachacou $^{138}$ , K. Bachas $^{76a,76b}$ , M. Backes $^{122}$ , M. Backhaus $^{32}$ ,  
P. Bagnaia $^{134a,134b}$ , H. Bahrasemani $^{144}$ , J.T. Baines $^{133}$ , M. Bajic $^{39}$ , O.K. Baker $^{179}$  
E.M. Baldin $^{111,c}$ , P. Balek $^{175}$ , F. Balli $^{138}$ , W.K. Balunas $^{124}$ , E. Banas $^{42}$ , Sw. Banerjee $^{176,e}$  
A.A.E. Bannoura $^{178}$ , L. Barak $^{32}$ , E.L. Barberio $^{91}$ , D. Barberis $^{53a,53b}$ , M. Barbero $^{88}$  
T. Barillari $^{103}$ , M-S Barisits $^{32}$ , J.T. Barkeloo $^{118}$ , T. Barklow $^{145}$ , N. Barlow $^{30}$ , S.L. Barnes $^{36c}$  
B.M. Barnett $^{133}$ , R.M. Barnett $^{16}$ , Z. Barnovska-Blenessy $^{36a}$ , A. Baroncelli $^{136a}$ , G. Barone $^{25}$ ,  
A.J. Barr<sup>122</sup>, L. Barranco Navarro<sup>170</sup>, F. Barreiro<sup>85</sup>, J. Barreiro Guimarães da Costa<sup>35a</sup>,  
R. Bartoldus<sup>145</sup>, A.E. Barton<sup>75</sup>, P. Bartos<sup>146a</sup>, A. Basalaev<sup>125</sup>, A. Bassalat<sup>119,f</sup>, R.L. Bates<sup>56</sup>,  
S.J. Batista $^{161}$ , J.R. Batley $^{30}$ , M. Battaglia $^{139}$ , M. Bauce $^{134a,134b}$ , F. Bauer $^{138}$ , H.S. Bawa $^{145,g}$  
J.B. Beacham<sup>113</sup>, M.D. Beattie<sup>75</sup>, T. Beau<sup>83</sup>, P.H. Beauchemin<sup>165</sup>, P. Bechtle<sup>23</sup>, H.P. Beck<sup>18,h</sup>,  
K. Becker $^{122}$ , M. Becker $^{86}$ , M. Beckingham $^{173}$ , C. Becot $^{112}$ , A.J. Beddall $^{20e}$ , A. Beddall $^{20b}$  
V.A. Bednyakov $^{68}$ , M. Bedognetti $^{109}$ , C.P. Bee $^{150}$ , T.A. Beermann $^{32}$ , M. Begalli $^{26a}$ , M. Begel $^{27}$  
J.K. Behr $^{45}$ , A.S. Bell $^{81}$ , G. Bella $^{155}$ , L. Bellagamba $^{22a}$ , A. Bellerive $^{31}$ , M. Bellomo $^{154}$  
K. Belotskiy<sup>100</sup>, O. Beltramello<sup>32</sup>, N.L. Belyaev<sup>100</sup>, O. Benary<sup>155,*</sup>, D. Benchekroun<sup>137a</sup>,  
M. Bender $^{102}$ , K. Bendtz $^{148a,148b}$ , N. Benekos $^{10}$ , Y. Benhammou $^{155}$ , E. Benhar Noccioli $^{179}$ ,  
J. Benitez $^{66}$ , D.P. Benjamin $^{48}$ , M. Benoit $^{52}$ , J.R. Bensinger $^{25}$ , S. Bentvelsen $^{109}$ , L. Beresford $^{122}$ .  
M. Beretta $^{50}$ , D. Berge $^{109}$ , E. Bergeaas Kuitmann $^{168}$ , N. Berger $^{5}$ , J. Beringer $^{16}$ , S. Berlendis $^{58}$  
N.R. Bernard89, G. Bernardi83, C. Bernius145, F.U. Bernlochner23, T. Berry80, P. Berta131,  
C. Bertella $^{35a}$ , G. Bertoli $^{148a,148b}$ , F. Bertolucci $^{126a,126b}$ , I.A. Bertram $^{75}$ , C. Bertsche $^{45}$ ,  
D. Bertsche $^{115}$ , G.J. Besjes $^{39}$ , O. Bessidskaia Bylund $^{148a,148b}$ , M. Bessner $^{45}$ , N. Besson $^{138}$  
C. Betancourt $^{51}$ , A. Bethani $^{87}$ , S. Bethke $^{103}$ , A.J. Bevan $^{79}$ , J. Beyer $^{103}$ , R.M. Bianchi $^{127}$  
O. Bieberl<sup>102</sup>, D. Biedermann<sup>17</sup>, R. Bielski<sup>87</sup>, N.V. Biesuz<sup>126a,126b</sup>, M. Biglietti<sup>136a</sup>,  
J. Bilbao De Mendizabal $^{52}$ , T.R.V. Billoud $^{97}$ , H. Bilokon $^{50}$ , M. Bindi $^{57}$ , A. Bingul $^{20b}$  
C. Bini $^{134a,134b}$ , S. Biondi $^{22a,22b}$ , T. Bisanz $^{57}$ , C. Bittrich $^{47}$ , D.M. Bjergaard $^{48}$ , C.W. Black $^{152}$

J.E. Black $^{145}$ , K.M. Black $^{24}$ , R.E. Blair $^{6}$ , T. Blazek $^{146a}$ , I. Bloch $^{45}$ , C. Blocker $^{25}$ , A. Blue $^{56}$ ,  
W. Blum $^{86,*}$ , U. Blumenschein $^{79}$ , S. Blunier $^{34a}$ , G.J. Bobbink $^{109}$ , V.S. Bobrovnikov $^{111,c}$  
S.S. Bocchetta $^{84}$ , A. Bocci $^{48}$ , C. Bock $^{102}$ , M. Boehler $^{51}$ , D. Boerner $^{178}$ , D. Bogavac $^{102}$ ,  
A.G. Bogdanchikov<sup>111</sup>, C. Bohm<sup>148a</sup>, V. Boisvert<sup>80</sup>, P. Bokan<sup>168,i</sup>, T. Bold<sup>41a</sup>, A.S. Boldyrev<sup>101</sup>,  
A.E. Bolz $^{60b}$ , M. Bomben $^{83}$ , M. Bona $^{79}$ , M. Boonekamp $^{138}$ , A. Borisov $^{132}$ , G. Borissov $^{75}$  
J. Bortfeldt $^{32}$ , D. Bortolotto $^{122}$ , V. Bortolotto $^{62a,62b,62c}$ , D. Boscherini $^{22a}$ , M. Bosman $^{13}$  
J.D. Bossio Sola $^{29}$ , J. Boudreau $^{127}$ , J. Bouffard $^{2}$ , E.V. Bouhova-Thacker $^{75}$ , D. Boumediene $^{37}$ ,  
C. Boudarios $^{119}$ , S.K. Boutle $^{56}$ , A. Boveia $^{113}$ , J. Boyd $^{32}$ , I.R. Boyko $^{68}$ , J. Bracinik $^{19}$  
A. Brandt $^{8}$ , G. Brandt $^{57}$ , O. Brandt $^{60a}$ , U. Bratzler $^{158}$ , B. Brau $^{89}$ , J.E. Brau $^{118}$  
W.D. Breaden Madden $^{56}$ , K. Brendlinger $^{45}$ , A.J. Brennan $^{91}$ , L. Brenner $^{109}$ , R. Brenner $^{168}$ ,  
S. Bressler $^{175}$ , D.L. Briglin $^{19}$ , T.M. Bristow $^{49}$ , D. Britton $^{56}$ , D. Britzger $^{45}$ , F.M. Brochu $^{30}$  
I. Brock $^{23}$ , R. Brock $^{93}$ , G. Brooijmans $^{38}$ , T. Brooks $^{80}$ , W.K. Brooks $^{34b}$ , J. Brosamer $^{16}$  
E. Brost $^{110}$ , J.H Broughton $^{19}$ , P.A. Bruckman de Renstrom $^{42}$ , D. Bruncko $^{146b}$ , A. Bruni $^{22a}$  
G. Bruni $^{22a}$ , L.S. Bruni $^{109}$ , BH Brunt $^{30}$ , M. Bruschi $^{22a}$ , N. Bruscino $^{23}$ , P. Bryant $^{33}$  
L. Bryngemark $^{45}$ , T. Buanes $^{15}$ , Q. Buat $^{144}$ , P. Buchholz $^{143}$ , A.G. Buckley $^{56}$ , I.A. Budagov $^{68}$ ,  
F. Buehrer $^{51}$ , M.K. Bugge $^{121}$ , O. Bulekov $^{100}$ , D. Bullock $^{8}$ , T.J. Burch $^{110}$ , H. Burckhart $^{32}$  
S. Burdin $^{77}$ , C.D. Burgard $^{51}$ , A.M. Burger $^{5}$ , B. Burghgrave $^{110}$ , K. Burka $^{42}$ , S. Burke $^{133}$  
I. Burmeister $^{46}$ , J.T.P. Burr $^{122}$ , E. Busato $^{37}$ , D. Buscher $^{51}$ , V. Buscher $^{86}$ , P. Bussey $^{56}$  
J.M. Butler $^{24}$ , C.M. Buttar $^{56}$ , J.M. Butterworth $^{81}$ , P. Butti $^{32}$ , W. Buttinger $^{27}$ , A. Buzatu $^{35c}$  
A.R. Buzykaev<sup>111,c</sup>, S. Cabrera Urbán<sup>170</sup>, D. Caforio<sup>130</sup>, V.M. Cairo<sup>40a,40b</sup>, O. Cakir<sup>4a</sup>,  
N. Calace $^{52}$ , P. Calafiura $^{16}$ , A. Calandri $^{88}$ , G. Calderini $^{83}$ , P. Calfayan $^{64}$ , G. Callea $^{40a,40b}$  
L.P. Caloba $^{26a}$ , S. Calvente Lopez $^{85}$ , D. Calvet $^{37}$ , S. Calvet $^{37}$ , T.P. Calvet $^{88}$ , R. Camacho Toro $^{33}$  
S. Camarda $^{32}$ , P. Camarri $^{135a,135b}$ , D. Cameron $^{121}$ , R. Caminal Armadans $^{169}$ , C. Camincher $^{58}$ ,  
S. Campana $^{32}$ , M. Campanelli $^{81}$ , A. Camplani $^{94a,94b}$ , A. Campoverde $^{143}$ , V. Canale $^{106a,106b}$  
M. Cano Bret $^{36c}$ , J. Cantero $^{116}$ , T. Cao $^{155}$ , M.D.M. Capeans Garrido $^{32}$ , I. Caprini $^{28b}$  
M. Caprini $^{28b}$ , M. Capua $^{40a,40b}$ , R.M. Carbone $^{38}$ , R. Cardarelli $^{135a}$ , F. Cardillo $^{51}$ , I. Carli $^{131}$ ,  
T. Carli $^{32}$ , G. Carlino $^{106a}$ , B.T. Carlson $^{127}$ , L. Carminati $^{94a,94b}$ , R.M.D. Carney $^{148a,148b}$  
S. Caron $^{108}$ , E. Carquin $^{34b}$ , S. Carrá $^{94a,94b}$ , G.D. Carrillo-Montoya $^{32}$ , J. Carvalho $^{128a,128c}$  
D. Casadei $^{19}$ , M.P. Casado $^{13,j}$ , M. Casolino $^{13}$ , D.W. Casper $^{166}$ , R. Castelijn $^{109}$ ,  
V. Castillo Gimenez $^{170}$ , N.F. Castro $^{128a,k}$ , A. Catinaccio $^{32}$ , J.R. Catmore $^{121}$ , A. Cattai $^{32}$  
J. Caudron $^{23}$ , V. Cavaliere $^{169}$ , E. Cavallaro $^{13}$ , D. Cavalli $^{94a}$ , M. Cavalli-Sforza $^{13}$ ,  
V. Cavainni $^{126a,126b}$ , E. Celebi $^{20a}$ , F. Ceradini $^{136a,136b}$ , L. Cerda Alberich $^{170}$ , A.S. Cerqueira $^{26b}$  
A. Cerri $^{151}$ , L. Cerrito $^{135a,135b}$ , F. Cerutti $^{16}$ , A. Cervelli $^{18}$ , S.A. Cetin $^{20d}$ , A. Chafaq $^{137a}$  
D. Chakraborty<sup>110</sup>, S.K. Chan<sup>59</sup>, W.S. Chan<sup>109</sup>, Y.L. Chan<sup>62a</sup>, P. Chang<sup>169</sup>, J.D. Chapman<sup>30</sup>,  
D.G. Charlton $^{19}$ , C.C. Chau $^{161}$ , C.A. Chavez Barajas $^{151}$ , S. Che $^{113}$ , S. Cheatham $^{167a,167c}$  
A. Chegwidden $^{93}$ , S. Chekanov $^{6}$ , S.V. Chekulaev $^{163a}$ , G.A. Chelkov $^{68,l}$ , M.A. Chelstowska $^{32}$  
C. Chen $^{67}$ , H. Chen $^{27}$ , S. Chen $^{35b}$ , S. Chen $^{157}$ , X. Chen $^{35c,m}$ , Y. Chen $^{70}$ , H.C. Cheng $^{92}$  
H.J. Cheng $^{35a}$ , A. Cheplakov $^{68}$ , E. Cheremushkina $^{132}$ , R. Cherkoui El Moursli $^{137e}$  
V. Chernyatin $^{27,*}$ , E. Cheu $^{7}$ , K. Cheung $^{63}$ , L. Chevalier $^{138}$ , V. Chiarella $^{50}$ , G. Chiarelli $^{126a,126b}$  
G. Chiodini $^{76a}$ , A.S. Chisholm $^{32}$ , A. Chitan $^{28b}$ , Y.H. Chiu $^{172}$ , M.V. Chizhov $^{68}$ , K. Choi $^{64}$  
A.R. Chomont $^{37}$ , S. Chouridou $^{156}$ , V. Christodoulou $^{81}$ , D. Chromek-Burckhart $^{32}$ , M.C. Chu $^{62a}$  
J. Chudoba $^{129}$ , A.J. Chuinard $^{90}$ , J.J. Chwastowski $^{42}$ , L. Chytka $^{117}$ , A.K. Ciftci $^{4a}$ , D. Cinca $^{46}$  
V. Cindro $^{78}$ , I.A. Cioara $^{23}$ , C. Ciocca $^{22a,22b}$ , A. Ciocio $^{16}$ , F. Ciroitto $^{106a,106b}$ , Z.H. Citron $^{175}$ ,  
M. Citterio $^{94a}$ , M. Ciubancan $^{28b}$ , A. Clark $^{52}$ , B.L. Clark $^{59}$ , M.R. Clark $^{38}$ , P.J. Clark $^{49}$ .  
R.N. Clarke $^{16}$ , C. Clement $^{148a,148b}$ , Y. Coadou $^{88}$ , M. Cobal $^{167a,167c}$ , A. Coccaro $^{52}$ , J. Cochran $^{67}$  
L. Colasurdo $^{108}$ , B. Cole $^{38}$ , A.P. Colijn $^{109}$ , J. Collot $^{58}$ , T. Colombo $^{166}$ , P. Conde Muiño $^{128a,128b}$  
E. Coniavitis $^{51}$ , S.H. Connell $^{147b}$ , I.A. Connelly $^{87}$ , S. Constantinescu $^{28b}$ , G. Conti $^{32}$  
F. Conventi $^{106a,n}$ , M. Cooke $^{16}$ , A.M. Cooper-Sarkar $^{122}$ , F. Cormier $^{171}$ , K.J.R. Cormier $^{161}$ ,

M. Corradi $^{134a,134b}$ , F. Corriveau $^{90,o}$ , A. Cortes-Gonzalez $^{32}$ , G. Cortiana $^{103}$ , G. Costa $^{94a}$  
M.J. Costa $^{170}$ , D. Costanzo $^{141}$ , G. Cottin $^{30}$ , G. Cowan $^{80}$ , B.E. Cox $^{87}$ , K. Cranmer $^{112}$ ,  
S.J. Crawley $^{56}$ , R.A. Creager $^{124}$ , G. Cree $^{31}$ , S. Crépé-Renaudin $^{58}$ , F. Crescioli $^{83}$  
W.A. Cribbs $^{148a,148b}$ , M. Cristinziani $^{23}$ , V. Croft $^{108}$ , G. Crosetti $^{40a,40b}$ , A. Cueto $^{85}$ ,  
T. Cuhadar Donszelmann<sup>141</sup>, A.R. Cukierman<sup>145</sup>, J. Cummings<sup>179</sup>, M. Curatolo<sup>50</sup>, J. Cúth<sup>86</sup>,  
H. Czirr $^{143}$ , P. Czodrowski $^{32}$ , G. D'amen $^{22a,22b}$ , S. D'Auria $^{56}$ , L. D'eramo $^{83}$ , M. D'Onofrio $^{77}$  
M.J. Da Cunha Sargedas De Sousa $^{128a,128b}$ , C. Da Via $^{87}$ , W. Dabrowski $^{41a}$ , T. Dado $^{146a}$ ,  
T. Dai $^{92}$ , O. Dale $^{15}$ , F. Dallaire $^{97}$ , C. Dallapiccola $^{89}$ , M. Dam $^{39}$ , J.R. Dandoy $^{124}$ , M.F. Daneri $^{29}$  
N.P. Dang $^{176}$ , A.C. Daniells $^{19}$ , N.S. Dann $^{87}$ , M. Danninger $^{171}$ , M. Dano Hoffmann $^{138}$ , V. Dao $^{150}$ ,  
G. Darbo $^{53a}$ , S. Darmora $^{8}$ , J. Dassoulas $^{3}$ , A. Dattagupta $^{118}$ , T. Daubney $^{45}$ , W. Davey $^{23}$  
C. David $^{45}$ , T. Davidek $^{131}$ , M. Davies $^{155}$ , D.R. Davis $^{48}$ , P. Davison $^{81}$ , E. Dawe $^{91}$ , I. Dawson $^{141}$  
K. De $^{8}$ , R. de Asmundis $^{106a}$ , A. De Benedetti $^{115}$ , S. De Castro $^{22a,22b}$ , S. De Cecco $^{83}$ ,  
N. De Groot<sup>108</sup>, P. de Jong<sup>109</sup>, H. De la Torre<sup>93</sup>, F. De Lorenzi<sup>67</sup>, A. De Maria<sup>57</sup>,  
D. De Pedis $^{134a}$ , A. De Salvo $^{134a}$ , U. De Sanctis $^{135a,135b}$ , A. De Santo $^{151}$ ,  
K. De Vasconcelos Corga $^{88}$ , J.B. De Vivie De Regie $^{119}$ , W.J. Dearnaley $^{75}$ , R. Debbe $^{27}$  
C. Debenedetti $^{139}$ , D.V. Dedovich $^{68}$ , N. Dehghanian $^{3}$ , I. Deigaard $^{109}$ , M. Del Gaudio $^{40a,40b}$  
J. Del Peso $^{85}$ , T. Del Prete $^{126a,126b}$ , D. Delgove $^{119}$ , F. Deliot $^{138}$ , C.M. Delitzsch $^{52}$ ,  
A. Dell'Acqua $^{32}$ , L. Dell'Asta $^{24}$ , M. Dell'Orso $^{126a,126b}$ , M. Della Pietra $^{106a,106b}$ , D. della Volpe $^{52}$  
M. Delmastro<sup>5</sup>, C. Delseport<sup>119</sup>, P.A. Delsart<sup>58</sup>, D.A. DeMarco<sup>161</sup>, S. Demers<sup>179</sup>, M. Demichev<sup>68</sup>,  
A. Demilly $^{83}$ , S.P. Denisov $^{132}$ , D. Denysiuk $^{138}$ , D. Derendarz $^{42}$ , J.E. Derkaoui $^{137d}$ , F. Derue $^{83}$  
P. Dervan $^{77}$ , K. Desch $^{23}$ , C. Deterre $^{45}$ , K. Dette $^{46}$ , M.R. Devesa $^{29}$ , P.O. Deviveiros $^{32}$  
A. Dewhurst $^{133}$ , S. Dhaliwal $^{25}$ , F.A. Di Bello $^{52}$ , A. Di Ciaccio $^{135a,135b}$ , L. Di Ciaccio $^{5}$ ,  
W.K. Di Clemente $^{124}$ , C. Di Donato $^{106a,106b}$ , A. Di Girolamo $^{32}$ , B. Di Girolamo $^{32}$ ,  
B. Di Micco $^{136a,136b}$ , R. Di Nardo $^{32}$ , K.F. Di Petrillo $^{59}$ , A. Di Simone $^{51}$ , R. Di Sipio $^{161}$ ,  
D. Di Valentino $^{31}$ , C. Diaconu $^{88}$ , M. Diamond $^{161}$ , F.A. Dias $^{39}$ , M.A. Diaz $^{34a}$ , E.B. Diehl $^{92}$ ,  
J. Dietrich $^{17}$ , S. Díez Cornell $^{45}$ , A. Dimitrievska $^{14}$ , J. Dingfelder $^{23}$ , P. Dita $^{28b}$ , S. Dita $^{28b}$  
F. Dittus<sup>32</sup>, F. Djama<sup>88</sup>, T. Djobava<sup>54b</sup>, J.I. Djuvsland<sup>60a</sup>, M.A.B. do Vale<sup>26c</sup>, D. Dobos<sup>32</sup>,  
M. Dobre $^{28b}$ , C. Doglioni $^{84}$ , J. Dolejsi $^{131}$ , Z. Dolezal $^{131}$ , M. Donadelli $^{26d}$ , S. Donati $^{126a,126b}$  
P. Dondero $^{123a,123b}$ , J. Donini $^{37}$ , J. Dopke $^{133}$ , A. Doria $^{106a}$ , M.T. Dova $^{74}$ , A.T. Doyle $^{56}$ ,  
E. Drechsler $^{57}$ , M. Dris $^{10}$ , Y. Du $^{36b}$ , J. Duarte-Campderros $^{155}$ , A. Dubreuil $^{52}$ , E. Duchovni $^{175}$  
G. Duckeck $^{102}$ , A. Ducourthial $^{83}$ , O.A. Ducu $^{97,p}$ , D. Duda $^{109}$ , A. Dudarev $^{32}$ , A. Chr. Dudder $^{86}$  
E.M. Duffield $^{16}$ , L. Duflot $^{119}$ , M. Dührssen $^{32}$ , M. Dumancic $^{175}$ , A.E. Dumitriu $^{28b}$  
A.K. Duncan $^{56}$ , M. Dunford $^{60a}$ , H. Duran Yildiz $^{4a}$ , M. Düren $^{55}$ , A. Durglishvili $^{54b}$  
D. Duschinger $^{47}$ , B. Dutta $^{45}$ , M. Dyndal $^{45}$ , B.S. Dziedzic $^{42}$ , C. Eckardt $^{45}$ , K.M. Ecker $^{103}$  
R.C. Edgar $^{92}$ , T. Eifert $^{32}$ , G. Eigen $^{15}$ , K. Einsweiler $^{16}$ , T. Ekelof $^{168}$ , M. El Kacimi $^{137c}$  
R. El Kosseifi $^{88}$ , V. Ellajosyula $^{88}$ , M. Ellert $^{168}$ , S. Elles $^{5}$ , F. Ellinghaus $^{178}$ , A.A. Elliot $^{172}$  
N. Ellis $^{32}$ , J. Elmsheuser $^{27}$ , M. Elsing $^{32}$ , D. Emeliyanov $^{133}$ , Y. Enari $^{157}$ , O.C. Endner $^{86}$  
J.S. Ennis $^{173}$ , J. Erdmann $^{46}$ , A. Ereditatato $^{18}$ , G. Ernis $^{178}$ , M. Ernst $^{27}$ , S. Errede $^{169}$ .  
M. Escalier<sup>119</sup>, C. Escobar<sup>170</sup>, B. Esposito<sup>50</sup>, O. Estrada Pastor<sup>170</sup>, A.I. Etienvre<sup>138</sup>,  
E. Etzion $^{155}$ , H. Evans $^{64}$ , A. Ezhilov $^{125}$ , M. Ezzi $^{137e}$ , F. Fabbri $^{22a,22b}$ , L. Fabbri $^{22a,22b}$ .  
G. Facini $^{33}$ , R.M. Fakhrutdinov $^{132}$ , S. Falciano $^{134a}$ , R.J. Falla $^{81}$ , J. Faltova $^{32}$ , Y. Fang $^{35a}$  
M. Fanti $^{94a,94b}$ , A. Farbin $^{8}$ , A. Farilla $^{136a}$ , C. Farina $^{127}$ , E.M. Farina $^{123a,123b}$ , T. Farooque $^{93}$ ,  
S. Farrell $^{16}$ , S.M. Farrington $^{173}$ , P. Farthouat $^{32}$ , F. Fassi $^{137e}$ , P. Fassnacht $^{32}$ , D. Fassouliotis $^{9}$  
M. Faucci Giannelli $^{80}$ , A. Favareto $^{53a,53b}$ , W.J. Fawcett $^{122}$ , L. Fayard $^{119}$ , O.L. Fedin $^{125,q}$  
W. Fedorko<sup>171</sup>, S. Feigl<sup>121</sup>, L. Feligioni<sup>88</sup>, C. Feng<sup>36b</sup>, E.J. Feng<sup>32</sup>, H. Feng<sup>92</sup>, M.J. Fenton<sup>56</sup>,  
A.B. Fenyuk<sup>132</sup>, L. Feremenga<sup>8</sup>, P. Fernandez Martinez<sup>170</sup>, S. Fernandez Perez<sup>13</sup>, J. Ferrando<sup>45</sup>  
A. Ferrari $^{168}$ , P. Ferrari $^{109}$ , R. Ferrari $^{123a}$ , D.E. Ferreira de Lima $^{60b}$ , A. Ferrer $^{170}$ , D. Ferrere $^{52}$  
C. Ferretti $^{92}$ , F. Fiedler $^{86}$ , A. Filipcic $^{78}$ , M. Filipuzzi $^{45}$ , F. Filthaut $^{108}$ , M. Fincke-Keeler $^{172}$

K.D. Finelli $^{152}$ , M.C.N. Fiolhais $^{128a,128c,r}$ , L. Fiorini $^{170}$ , A. Fischer $^{2}$ , C. Fischer $^{13}$ , J. Fischer $^{178}$  
W.C. Fisher $^{93}$ , N. Flaschel $^{45}$ , I. Fleck $^{143}$ , P. Fleischmann $^{92}$ , R.R.M. Fletcher $^{124}$ , T. Flick $^{178}$  
B.M. Flierl $^{102}$ , L.R. Flores Castillo $^{62a}$ , M.J. Flowerdew $^{103}$ , G.T. Forcolin $^{87}$ , A. Formica $^{138}$  
F.A. Förster $^{13}$ , A. Forti $^{87}$ , A.G. Foster $^{19}$ , D. Fournier $^{119}$ , H. Fox $^{75}$ , S. Fracchia $^{141}$ ,  
P. Francavilla $^{83}$ , M. Franchini $^{22a,22b}$ , S. Franchino $^{60a}$ , D. Francis $^{32}$ , L. Franconi $^{121}$ ,  
M. Franklin $^{59}$ , M. Frate $^{166}$ , M. Fraternali $^{123a,123b}$ , D. Freeborn $^{81}$ , S.M. Fressard-Batraneanu $^{32}$ ,  
B. Freund $^{97}$ , D. Froidevaux $^{32}$ , J.A. Frost $^{122}$ , C. Fukunaga $^{158}$ , T. Fusayasu $^{104}$ , J. Fuster $^{170}$  
C. Gabaldon $^{58}$ , O. Gabizon $^{154}$ , A. Gabrielli $^{22a,22b}$ , A. Gabrielli $^{16}$ , G.P. Gach $^{41a}$ , S. Gadatsch $^{32}$  
S. Gadomski $^{80}$ , G. Gagliardi $^{53a,53b}$ , L.G. Gagnon $^{97}$ , C. Galea $^{108}$ , B. Galhardo $^{128a,128c}$  
E.J. Gallas<sup>122</sup>, B.J. Gallop<sup>133</sup>, P. Gallus<sup>130</sup>, G. Galster<sup>39</sup>, K.K. Gan<sup>113</sup>, S. Ganguly<sup>37</sup>, Y. Gao<sup>77</sup>,  
Y.S. Gao $^{145,g}$ , F.M. Garay Walls $^{49}$ , C. García $^{170}$ , J.E. García Navarro $^{170}$ , J.A. García Pascual $^{35a}$  
M. Garcia-Sciveres $^{16}$ , R.W. Gardner $^{33}$ , N. Garelli $^{145}$ , V. Garonne $^{121}$ , A. Gascon Bravo $^{45}$ ,  
K. Gasnikova $^{45}$ , C. Gatti $^{50}$ , A. Gaudiello $^{53a,53b}$ , G. Gaudio $^{123a}$ , I.L. Gavrilenko $^{98}$ , C. Gay $^{171}$  
G. Gaycken23, E.N. Gazis10, C.N.P. Gee133, J. Geisen57, M. Geisen86, M.P. Geisler60a,  
K. Gellerstedt $^{148a,148b}$ , C. Gemme $^{53a}$ , M.H. Genest $^{58}$ , C. Geng $^{92}$ , S. Gentile $^{134a,134b}$  
C. Gentsos $^{156}$ , S. George $^{80}$ , D. Gerbaudo $^{13}$ , A. Gershon $^{155}$ , G. Geßner $^{46}$ , S. Ghasemi $^{143}$  
M. Ghneimat $^{23}$ , B. Giacobbe $^{22a}$ , S. Giagu $^{134a,134b}$ , P. Giannetti $^{126a,126b}$ , S.M. Gibson $^{80}$ ,  
M. Gignac $^{171}$ , M. Gilchriese $^{16}$ , D. Gillberg $^{31}$ , G. Gilles $^{178}$ , D.M. Gingrich $^{3,d}$ , N. Giokaris $^{9,*}$ .  
M.P. Giordani $^{167a,167c}$ , F.M. Giorgi $^{22a}$ , P.F. Giraud $^{138}$ , P. Giromini $^{59}$ , D. Giugni $^{94a}$ , F. Giul $^{122}$  
C. Giuliani $^{103}$ , M. Giulini $^{60b}$ , B.K. Gjelsten $^{121}$ , S. Gkaitatzis $^{156}$ , I. Gkialas $^{9,s}$  
E.L. Gkougkousis $^{139}$ , P. Gkountoumis $^{10}$ , L.K. Gladilin $^{101}$ , C. Glasman $^{85}$ , J. Glatzer $^{13}$  
P.C.F. Glaysher $^{45}$ , A. Glazov $^{45}$ , M. Goblirsch-Kolb $^{25}$ , J. Godlewski $^{42}$ , S. Goldfarb $^{91}$ ,  
T. Golling $^{52}$ , D. Golubkov $^{132}$ , A. Gomes $^{128a,128b,128d}$ , R. Gonçalo $^{128a}$ , R. Goncalves Gama $^{26a}$  
J. Goncalves Pinto Firmino Da Costa $^{138}$ , G. Gonella $^{51}$ , L. Gonella $^{19}$ , A. Gongadze $^{68}$  
S. González de la Hoz<sup>170</sup>, S. Gonzalez-Sevilla<sup>52</sup>, L. Goossens<sup>32</sup>, P.A. Gorbounov<sup>99</sup>,  
H.A. Gordon $^{27}$ , I. Gorelov $^{107}$ , B. Gorini $^{32}$ , E. Gorini $^{76a,76b}$ , A. Gorišek $^{78}$ , A.T. Goshaw $^{48}$  
C. Gossling $^{46}$ , M.I. Gostkin $^{68}$ , C.A. Gottardo $^{23}$ , C.R. Goudet $^{119}$ , D. Goujdami $^{137c}$  
A.G. Goussiou<sup>140</sup>, N. Govender<sup>147b,t</sup>, E. Gozani<sup>154</sup>, L. Graber<sup>57</sup>, I. Grabowska-Bold<sup>41a</sup>,  
P.O.J. Gradin<sup>168</sup>, J. Gramling<sup>166</sup>, E. Gramstad<sup>121</sup>, S. Grancagnolo<sup>17</sup>, V. Gratchev<sup>125</sup>,  
P.M. Gravila $^{28f}$ , C. Gray $^{56}$ , H.M. Gray $^{16}$ , Z.D. Greenwood $^{82,u}$ , C. Grefe $^{23}$ , K. Gregersen $^{81}$  
I.M. Gregor $^{45}$ , P. Grenier $^{145}$ , K. Grevtsov $^{5}$ , J. Griffiths $^{8}$ , A.A. Grillo $^{139}$ , K. Grimm $^{75}$  
S. Grinstein $^{13,v}$ , Ph. Gris $^{37}$ , J.-F. Grivaz $^{119}$ , S. Groh $^{86}$ , E. Gross $^{175}$ , J. Grosse-Knetter $^{57}$  
G.C. Grossi $^{82}$ , Z.J. Grout $^{81}$ , A. Grummer $^{107}$ , L. Guan $^{92}$ , W. Guan $^{176}$ , J. Guenther $^{65}$  
F. Guescini $^{163a}$ , D. Guest $^{166}$ , O. Gueta $^{155}$ , B. Gui $^{113}$ , E. Guido $^{53a,53b}$ , T. Guillemin $^{5}$  
S. Guindon $^{2}$ , U. Gul $^{56}$ , C. Gumpert $^{32}$ , J. Guo $^{36c}$ , W. Guo $^{92}$ , Y. Guo $^{36a}$ , R. Gupta $^{43}$  
S. Gupta $^{122}$ , G. Gustavino $^{134a,134b}$ , P. Gutierrez $^{115}$ , N.G. Gutierrez Ortiz $^{81}$ , C. Gutschow $^{81}$  
C. Guyot $^{138}$ , M.P. Guzik $^{41a}$ , C. Gwenlan $^{122}$ , C.B. Gwilliam $^{77}$ , A. Haas $^{112}$ , C. Haber $^{16}$  
H.K. Hadavand<sup>8</sup>, N. Haddad<sup>137e</sup>, A. Hdef<sup>88</sup>, S. Hageböck<sup>23</sup>, M. Hagihara<sup>164</sup>, H. Hakobyan<sup>180,*</sup>,  
M. Haleem $^{45}$ , J. Haley $^{116}$ , G. Halladjian $^{93}$ , G.D. Hallewell $^{88}$ , K. Hamacher $^{178}$ , P. Hamal $^{117}$  
K. Hamano $^{172}$ , A. Hamilton $^{147a}$ , G.N. Hamity $^{141}$ , P.G. Hamnett $^{45}$ , L. Han $^{36a}$ , S. Han $^{35a}$  
K. Hanagaki $^{69, w}$ , K. Hanawa $^{157}$ , M. Hance $^{139}$ , B. Haney $^{124}$ , P. Hanke $^{60a}$ , J.B. Hansen $^{39}$  
J.D. Hansen $^{39}$ , M.C. Hansen $^{23}$ , P.H. Hansen $^{39}$ , K. Hara $^{164}$ , A.S. Hard $^{176}$ , T. Harenberg $^{178}$ ,  
F. Hariri $^{119}$ , S. Harkusha $^{95}$ , R.D. Harrington $^{49}$ , P.F. Harrison $^{173}$ , N.M. Hartmann $^{102}$ ,  
M. Hasegawa $^{70}$ , Y. Hasegawa $^{142}$ , A. Hasib $^{49}$ , S. Hassani $^{138}$ , S. Haug $^{18}$ , R. Hauser $^{93}$ ,  
L. Hauswald $^{47}$ , L.B. Havener $^{38}$ , M. Havranek $^{130}$ , C.M. Hawkes $^{19}$ , R.J. Hawkings $^{32}$ ,  
D. Hayakawa $^{159}$ , D. Hayden $^{93}$ , C.P. Hays $^{122}$ , J.M. Hays $^{79}$ , H.S. Hayward $^{77}$ , S.J. Haywood $^{133}$ ,  
S.J. Head $^{19}$ , T. Heck $^{86}$ , V. Hedberg $^{84}$ , L. Heelan $^{8}$ , K.K. Heidegger $^{51}$ , S. Heim $^{45}$ , T. Heim $^{16}$  
B. Heinemann $^{45,x}$ , J.J. Heinrich $^{102}$ , L. Heinrich $^{112}$ , C. Heinz $^{55}$ , J. Hejbal $^{129}$ , L. Helary $^{32}$

A. Held $^{171}$ , S. Hellman $^{148a,148b}$ , C. Helsens $^{32}$ , R.C.W. Henderson $^{75}$ , Y. Heng $^{176}$  
S. Henkelmann<sup>171</sup>, A.M. Henriques Correia<sup>32</sup>, S. Henrot-Versille<sup>119</sup>, G.H. Herbert<sup>17</sup>, H. Herde<sup>25</sup>,  
V. Herget $^{177}$ , Y. Hernández Jiménez $^{147c}$ , H. Herr $^{86}$ , G. Herten $^{51}$ , R. Hertenberger $^{102}$ ,  
L. Hervas $^{32}$ , T.C. Herwig $^{124}$ , G.G. Hesketh $^{81}$ , N.P. Hessey $^{163a}$ , J.W. Hetherly $^{43}$ , S. Higashino $^{69}$ ,  
E. Higón-Rodriguez $^{170}$ , E. Hill $^{172}$ , J.C. Hill $^{30}$ , K.H. Hiller $^{45}$ , S.J. Hillier $^{19}$ , M. Hilis $^{47}$  
I. Hinchliffe $^{16}$ , M. Hirose $^{51}$ , D. Hirschbuehl $^{178}$ , B. Hiti $^{78}$ , O. Hladik $^{129}$ , X. Hoad $^{49}$ , J. Hobbs $^{150}$  
N. Hod $^{163a}$ , M.C. Hodgkinson $^{141}$ , P. Hodgson $^{141}$ , A. Hoecker $^{32}$ , M.R. Hoeferkamp $^{107}$ ,  
F. Hoenig $^{102}$ , D. Hohn $^{23}$ , T.R. Holmes $^{33}$ , M. Homann $^{46}$ , S. Honda $^{164}$ , T. Honda $^{69}$ , T.M. Hong $^{127}$  
B.H. Hooberman $^{169}$ , W.H. Hopkins $^{118}$ , Y. Horii $^{105}$ , A.J. Horton $^{144}$ , J-Y. Hostachy $^{58}$ , S. Hou $^{153}$ ,  
A. Hoummada $^{137a}$ , J. Howarth $^{87}$ , J. Hoya $^{74}$ , M. Hrabovsky $^{117}$ , J. Hrdinka $^{32}$ , I. Hristova $^{17}$ ,  
J. Hrivnac $^{119}$ , T. Hryn'ova $^{5}$ , A. Hrynevich $^{96}$ , P.J. Hsu $^{63}$ , S.-C. Hsu $^{140}$ , Q. Hu $^{36a}$ , S. Hu $^{36c}$  
Y. Huang $^{35a}$ , Z. Hubacek $^{130}$ , F. Hubaut $^{88}$ , F. Huegging $^{23}$ , T.B. Huffman $^{122}$ , E.W. Hughes $^{38}$  
G. Hughes $^{75}$ , M. Huhtinen $^{32}$ , P. Huo $^{150}$ , N. Huseynov $^{68,b}$ , J. Huston $^{93}$ , J. Huth $^{59}$ , G. Iacobucci $^{52}$ ,  
G. Iakovidis $^{27}$ , I. Ibragimov $^{143}$ , L. Iconomidou-Fayard $^{119}$ , Z. Idrissi $^{137e}$ , P. Iengo $^{32}$  
O. Igonkina $^{109,y}$ , T. Iizawa $^{174}$ , Y. Ikegami $^{69}$ , M. Ikeno $^{69}$ , Y. Ilchenko $^{11,z}$ , D. Iliadis $^{156}$ , N. Ilic $^{145}$ ,  
G. Introzzi $^{123a,123b}$ , P. Ioannou $^{9,*}$ , M. Iodice $^{136a}$ , K. Iordanidou $^{38}$ , V. Ippolito $^{59}$  
M.F. Isacson $^{168}$ , N. Ishijima $^{120}$ , M. Ishino $^{157}$ , M. Ishitsuka $^{159}$ , C. Issever $^{122}$ , S. Istin $^{20a}$ , F. Ito $^{164}$ ,  
J.M. Iturbe Ponce $^{87}$ , R. Iuppa $^{162a,162b}$ , H. Iwasaki $^{69}$ , J.M. Izen $^{44}$ , V. Izzo $^{106a}$ , S. Jabbar $^{3}$ ,  
P. Jackson $^{1}$ , R.M. Jacobs $^{23}$ , V. Jain $^{2}$ , K.B. Jakobi $^{86}$ , K. Jakobs $^{51}$ , S. Jakobsen $^{65}$ ,  
T. Jakoubek $^{129}$ , D.O. Jamin $^{116}$ , D.K. Jana $^{82}$ , R. Jansky $^{52}$ , J. Janssen $^{23}$ , M. Janus $^{57}$  
P.A. Janus $^{41a}$ , G. Jarlskog $^{84}$ , N. Javadov $^{68,b}$ , T. Javurek $^{51}$ , M. Javurkova $^{51}$ , F. Jeanneau $^{138}$  
L. Jeanty $^{16}$ , J. Jejelava $^{54a,aa}$ , A. Jelinskas $^{173}$ , P. Jenni $^{51,ab}$ , C. Jeske $^{173}$ , S. Jézéquel $^{5}$ , H. Ji $^{176}$  
J. Jia $^{150}$ , H. Jiang $^{67}$ , Y. Jiang $^{36a}$ , Z. Jiang $^{145}$ , S. Jiggins $^{81}$ , J. Jimenez Pena $^{170}$ , S. Jin $^{35a}$  
A. Jinaru $^{28b}$ , O. Jinnouchi $^{159}$ , H. Jivan $^{147c}$ , P. Johansson $^{141}$ , K.A. Johns $^{7}$ , C.A. Johnson $^{64}$ ,  
W.J. Johnson $^{140}$ , K. Jon-And $^{148a,148b}$ , R.W.L. Jones $^{75}$ , S.D. Jones $^{151}$ , S. Jones $^{7}$ , T.J. Jones $^{77}$ ,  
J. Jongmanns $^{60a}$ , P.M. Jorge $^{128a,128b}$ , J. Jovicevic $^{163a}$ , X. Ju $^{176}$ , A. Juste Rozas $^{13,v}$  
M.K. Kohler $^{175}$ , A. Kaczmarska $^{42}$ , M. Kado $^{119}$ , H. Kagan $^{113}$ , M. Kagan $^{145}$ , S.J. Kahn $^{88}$ ,  
T. Kaji $^{174}$ , E. Kajomovitz $^{48}$ , C.W. Kalderon $^{84}$ , A. Kaluza $^{86}$ , S. Kama $^{43}$ , A. Kamenshchikov $^{132}$ ,  
N. Kanaya $^{157}$ , L. Kanjin $^{78}$ , V.A. Kantserov $^{100}$ , J. Kanzaki $^{69}$ , B. Kaplan $^{112}$ , L.S. Kaplan $^{176}$  
D. Kar  $^{147\mathrm{c}}$  , K. Karakostas  $^{10}$  , N. Karastathis  $^{10}$  , M.J. Kareem  $^{57}$  , E. Karentzos  $^{10}$  , S.N. Karpov  $^{68}$  
Z.M. Karpova $^{68}$ , K. Karthik $^{112}$ , V. Kartvelishvili $^{75}$ , A.N. Karyukhin $^{132}$ , K. Kasahara $^{164}$ ,  
L. Kashif $^{176}$ , R.D. Kass $^{113}$ , A. Kastanas $^{149}$ , Y. Kataoka $^{157}$ , C. Kato $^{157}$ , A. Katre $^{52}$ , J. Katzy $^{45}$  
K. Kawade $^{70}$ , K. Kawagoe $^{73}$ , T. Kawamoto $^{157}$ , G. Kawamura $^{57}$ , E.F. Kay $^{77}$ , V.F. Kazanin $^{111,c}$  
R. Keeler $^{172}$ , R. Kehoe $^{43}$ , J.S. Keller $^{31}$ , J.J. Kempster $^{80}$ , J Kendrick $^{19}$ , H. Keoshkerian $^{161}$  
O. Kepka $^{129}$ , B.P. Kerševan $^{78}$ , S. Kersten $^{178}$ , R.A. Keyes $^{90}$ , M. Khader $^{169}$ , F. Khalil-zada $^{12}$  
A. Khanov $^{116}$ , A.G. Kharlamov $^{111,c}$ , T. Kharlamova $^{111,c}$ , A. Khodinov $^{160}$ , T.J. Khoo $^{52}$  
V. Khovanskiy $^{99,*}$ , E. Khramov $^{68}$ , J. Khubua $^{54b,ac}$ , S. Kido $^{70}$ , C.R. Kilby $^{80}$ , H.Y. Kim $^{8}$  
S.H. Kim $^{164}$ , Y.K. Kim $^{33}$ , N. Kimura $^{156}$ , O.M. Kind $^{17}$ , B.T. King $^{77}$ , D. Kirchmeier $^{47}$ , J. Kirk $^{133}$  
A.E. Kiryunin $^{103}$ , T. Kishimoto $^{157}$ , D. Kisielewska $^{41a}$ , V. Kitali $^{45}$ , K. Kiuchi $^{164}$ , O. Kiveryk $^{5}$  
E. Kladiva $^{146b}$ , T. Klapdor-Kleingrothaus $^{51}$ , M.H. Klein $^{38}$ , M. Klein $^{77}$ , U. Klein $^{77}$ ,  
K. Kleinknecht $^{86}$ , P. Klimek $^{110}$ , A. Klimentov $^{27}$ , R. Klingenberg $^{46}$ , T. Klingl $^{23}$  
T. Klioutchnikova<sup>32</sup>, E.-E. Kluge<sup>60a</sup>, P. Kluit<sup>109</sup>, S. Kluth<sup>103</sup>, E. Kneringer<sup>65</sup>,  
E.B.F.G. Knoops $^{88}$ , A. Knue $^{103}$ , A. Kobayashi $^{157}$ , D. Kobayashi $^{159}$ , T. Kobayashi $^{157}$  
M. Kobel $^{47}$ , M. Kocian $^{145}$ , P. Kodys $^{131}$ , T. Koffas $^{31}$ , E. Koffeman $^{109}$ , N.M. Kohler $^{103}$ , T. Koi $^{145}$ ,  
M. Kolb $^{60b}$ , I. Koletsou $^{5}$ , A.A. Komar $^{98,*}$ , Y. Komori $^{157}$ , T. Kondo $^{69}$ , N. Kondrashova $^{36c}$  
K. Koneke<sup>51</sup>, A.C. König<sup>108</sup>, T. Kono<sup>69,ad</sup>, R. Konoplich<sup>112,ae</sup>, N. Konstantinidis<sup>81</sup>,  
R. Kopeliansky $^{64}$ , S. Koperny $^{41a}$ , A.K. Kopp $^{51}$ , K. Korcyl $^{42}$ , K. Kordas $^{156}$ , A. Korn $^{81}$  
A.A. Korol<sup>111,c</sup>, I. Korolkov<sup>13</sup>, E.V. Korolkova<sup>141</sup>, O. Kortner<sup>103</sup>, S. Kortner<sup>103</sup>, T. Kosek<sup>131</sup>,

V.V. Kostyukhin $^{23}$ , A. Kotwal $^{48}$ , A. Koulouris $^{10}$ , A. Kourkoumeli-Charalampidi $^{123a,123b}$ ,  
C. Kourkoumelis<sup>9</sup>, E. Kourlitis<sup>141</sup>, V. Kouskoura<sup>27</sup>, A.B. Kowalewska<sup>42</sup>, R. Kowalewski<sup>172</sup>,  
T.Z. Kowalski $^{41a}$ , C. Kozakai $^{157}$ , W. Kozanecki $^{138}$ , A.S. Kozhin $^{132}$ , V.A. Kramarenko $^{101}$ ,  
G. Kramberger $^{78}$ , D. Krasnopevtsev $^{100}$ , M.W. Krasny $^{83}$ , A. Krasznahorkay $^{32}$ , D. Krauss $^{103}$  
J.A. Kremer $^{41a}$ , J. Kretzschmar $^{77}$ , K. Kreutzfeldt $^{55}$ , P. Krieger $^{161}$ , K. Krizka $^{33}$ , K. Kroeninger $^{46}$  
H. Kroha $^{103}$ , J. Kroll $^{129}$ , J. Kroll $^{124}$ , J. Kroseberg $^{23}$ , J. Krstic $^{14}$ , U. Kruchonak $^{68}$ , H. Krüger $^{23}$ ,  
N. Krumnack $^{67}$ , M.C. Kruse $^{48}$ , T. Kubota $^{91}$ , H. Kucuk $^{81}$ , S. Kuday $^{4b}$ , J.T. Kuechler $^{178}$  
S. Kuehn $^{32}$ , A. Kugel $^{60a}$ , F. Kuger $^{177}$ , T. Kuhl $^{45}$ , V. Kukhtin $^{68}$ , R. Kukla $^{88}$ , Y. Kulchitsky $^{95}$ ,  
S. Kuleshov $^{34b}$ , Y.P. Kulinich $^{169}$ , M. Kuna $^{134a,134b}$ , T. Kunigo $^{71}$ , A. Kupco $^{129}$ , T. Kupfer $^{46}$  
O. Kuprash $^{155}$ , H. Kurashige $^{70}$ , L.L. Kurchaninov $^{163a}$ , Y.A. Kurochkin $^{95}$ , M.G. Kurth $^{35a}$  
V. Kus $^{129}$ , E.S. Kuwertz $^{172}$ , M. Kuze $^{159}$ , J. Kvita $^{117}$ , T. Kwan $^{172}$ , D. Kyriazopoulos $^{141}$  
A. La Rosa $^{103}$ , J.L. La Rosa Navarro $^{26d}$ , L. La Rotonda $^{40a,40b}$ , C. Lacasta $^{170}$ , F. Lacava $^{134a,134b}$  
J. Lacey $^{45}$ , H. Lacker $^{17}$ , D. Lacour $^{83}$ , E. Ladygin $^{68}$ , R. Lafaye $^{5}$ , B. Laforge $^{83}$ , T. Lagouri $^{179}$  
S. Lai $^{57}$ , S. Lammers $^{64}$ , W. Lampl $^{7}$ , E. Lancon $^{27}$ , U. Landgraf $^{51}$ , M.P.J. Landon $^{79}$  
M.C. Lanfermann $^{52}$ , V.S. Lang $^{60a}$ , J.C. Lange $^{13}$ , R.J. Langenberg $^{32}$ , A.J. Lankford $^{166}$  
F. Lanni $^{27}$ , K. Lantzsch $^{23}$ , A. Lanza $^{123a}$ , A. Lapertosa $^{53a,53b}$ , S. Laplace $^{83}$ , J.F. Laporte $^{138}$ ,  
T. Lari $^{94a}$ , F. Lasagni Manghi $^{22a,22b}$ , M. Lassnig $^{32}$ , P. Laurelli $^{50}$ , W. Lavrijsen $^{16}$ , A.T. Law $^{139}$  
P. Laycock $^{77}$ , T. Lazovich $^{59}$ , M. Lazzaroni $^{94a,94b}$ , B. Le $^{91}$ , O. Le Dortz $^{83}$ , E. Le Guirriec $^{88}$ ,  
E.P. Le Quilleuc $^{138}$ , M. LeBlanc $^{172}$ , T. LeCompte $^{6}$ , F. Ledroit-Guillon $^{58}$ , C.A. Lee $^{27}$  
G.R. Lee $^{133,af}$ , S.C. Lee $^{153}$ , L. Lee $^{59}$ , B. Lefebvre $^{90}$ , G. Lefebvre $^{83}$ , M. Lefebvre $^{172}$ , F. Legger $^{102}$  
C. Leggett $^{16}$ , A. Lehan $^{77}$ , G. Lehmann Miotto $^{32}$ , X. Lei $^{7}$ , W.A. Leight $^{45}$ , M.A.L. Leite $^{26d}$ ,  
R. Leitner $^{131}$ , D. Lellouch $^{175}$ , B. Lemmer $^{57}$ , K.J.C. Leney $^{81}$ , T. Lenz $^{23}$ , B. Lenzi $^{32}$ , R. Leone $^{7}$ ,  
S. Leone $^{126a,126b}$ , C. Leonidopoulos $^{49}$ , G. Lerner $^{151}$ , C. Leroy $^{97}$ , A.A.J. Lesage $^{138}$ , C.G. Lester $^{30}$ ,  
M. Levchenko $^{125}$ , J. Levêque $^{5}$ , D. Levin $^{92}$ , L.J. Levinson $^{175}$ , M. Levy $^{19}$ , D. Lewis $^{79}$ , B. Li $^{36a,ag}$  
Changqiao Li $^{36a}$ , H. Li $^{150}$ , L. Li $^{36c}$ , Q. Li $^{35a}$ , S. Li $^{48}$ , X. Li $^{36c}$ , Y. Li $^{143}$ , Z. Liang $^{35a}$  
B. Liberti $^{135a}$ , A. Liblong $^{161}$ , K. Lie $^{62c}$ , J. Liebal $^{23}$ , W. Liebig $^{15}$ , A. Limosani $^{152}$ , S.C. Lin $^{182}$  
T.H. Lin $^{86}$ , B.E. Lindquist $^{150}$ , A.E. Lionti $^{52}$ , E. Lipeles $^{124}$ , A. Lipniacka $^{15}$ , M. Lisovyi $^{60b}$  
T.M. Liss $^{169,ah}$ , A. Lister $^{171}$ , A.M. Litke $^{139}$ , B. Liu $^{153,ai}$ , H. Liu $^{92}$ , H. Liu $^{27}$ , J.K.K. Liu $^{122}$  
J. Liu $^{36b}$ , J.B. Liu $^{36a}$ , K. Liu $^{88}$ , L. Liu $^{169}$ , M. Liu $^{36a}$ , Y.L. Liu $^{36a}$ , Y. Liu $^{36a}$ , M. Livan $^{123a,123b}$  
A. Lleres $^{58}$ , J. Llorente Merino $^{35a}$ , S.L. Lloyd $^{79}$ , C.Y. Lo $^{62b}$ , F. Lo Sterzo $^{153}$ ,  
E.M. Lobodzinska $^{45}$ , P. Loch $^{7}$ , F.K. Loebinger $^{87}$ , A. Loesle $^{51}$ , K.M. Loew $^{25}$ , A. Loginov $^{179,*}$  
T. Lohse $^{17}$ , K. Lohwasser $^{141}$ , M. Lokajicek $^{129}$ , B.A. Long $^{24}$ , J.D. Long $^{169}$ , R.E. Long $^{75}$  
L. Longo $^{76a,76b}$ , K.A. Looper $^{113}$ , J.A. Lopez $^{34b}$ , D. Lopez Mateos $^{59}$ , I. Lopez Paz $^{13}$ ,  
A. Lopez Solis $^{83}$ , J. Lorenz $^{102}$ , N. Lorenzo Martinez $^{5}$ , M. Losada $^{21}$ , P.J. Lösel $^{102}$ , X. Lou $^{35a}$  
A. Lounis $^{119}$ , J. Love $^{6}$ , P.A. Love $^{75}$ , H. Lu $^{62a}$ , N. Lu $^{92}$ , Y.J. Lu $^{63}$ , H.J. Lubatti $^{140}$  
C. Luci $^{134a,134b}$ , A. Lucotte $^{58}$ , C. Luedtke $^{51}$ , F. Luehring $^{64}$ , W. Lukas $^{65}$ , L. Luminari $^{134a}$  
O. Lundberg $^{148a,148b}$ , B. Lund-Jensen $^{149}$ , P.M. Luzi $^{83}$ , D. Lynn $^{27}$ , R. Lysak $^{129}$ , E. Lytken $^{84}$ ,  
V. Lyubushkin $^{68}$ , H. Ma $^{27}$ , L.L. Ma $^{36b}$ , Y. Ma $^{36b}$ , G. Maccarrone $^{50}$ , A. Macchiolo $^{103}$ ,  
C.M. Macdonald $^{141}$ , B. Macek $^{78}$ , J. Machado Miguens $^{124,128b}$ , D. Madaffari $^{170}$ , R. Madar $^{37}$  
W.F. Mader $^{47}$ , A. Madsen $^{45}$ , J. Maeda $^{70}$ , S. Maeland $^{15}$ , T. Maeno $^{27}$ , A.S. Maevskiy $^{101}$ ,  
E. Magradze $^{57}$ , J. Mahlstedt $^{109}$ , C. Maiani $^{119}$ , C. Maidantchik $^{26a}$ , A.A. Maier $^{103}$ , T. Maier $^{102}$  
A. Maio $^{128a,128b,128d}$ , O. Majersky $^{146a}$ , S. Majewski $^{118}$ , Y. Makida $^{69}$ , N. Makovec $^{119}$  
B. Malaescu $^{83}$ , Pa. Malecki $^{42}$ , V.P. Maleev $^{125}$ , F. Malek $^{58}$ , U. Mallik $^{66}$ , D. Malon $^{6}$ , C. Malone $^{30}$  
S. Maltezos $^{10}$ , S. Malyukov $^{32}$ , J. Mamuzic $^{170}$ , G. Mancini $^{50}$ , L. Mandelli $^{94a}$ , I. Mandić $^{78}$  
J. Maneira $^{128a,128b}$ , L. Manhaes de Andrade Filho $^{26b}$ , J. Manjarres Ramos $^{47}$ , A. Mann $^{102}$  
A. Manousos<sup>32</sup>, B. Mansoulie<sup>138</sup>, J.D. Mansour<sup>35a</sup>, R. Mantifel<sup>90</sup>, M. Mantoani<sup>57</sup>,  
S. Manzoni $^{94a,94b}$ , L. Mapelli $^{32}$ , G. Marceca $^{29}$ , L. March $^{52}$ , L. Marchese $^{122}$ , G. Marchiori $^{83}$  
M. Marcisovsky $^{129}$ , M. Marjanovic $^{37}$ , D.E. Marley $^{92}$ , F. Marroquim $^{26a}$ , S.P. Marsden $^{87}$ ,

Z. Marshall $^{16}$ , M.U.F Martensson $^{168}$ , S. Marti-Garcia $^{170}$ , C.B. Martin $^{113}$ , T.A. Martin $^{173}$ ,  
V.J. Martin $^{49}$ , B. Martin dit Latour $^{15}$ , M. Martinez $^{13,v}$ , V.I. Martinez Outschoorn $^{169}$  
S. Martin-Haugh $^{133}$ , V.S. Martoiu $^{28b}$ , A.C. Martyniuk $^{81}$ , A. Marzin $^{32}$ , L. Masetti $^{86}$  
T. Mashimo $^{157}$ , R. Mashinistov $^{98}$ , J. Masik $^{87}$ , A.L. Maslennikov $^{111,c}$ , L. Massa $^{135a,135b}$  
P. Mastrandrea $^{5}$ , A. Mastroberardino $^{40a,40b}$ , T. Masubuchi $^{157}$ , P. Mattig $^{178}$ , J. Maurer $^{28b}$  
S.J. Maxfield $^{77}$ , D.A. Maximov $^{111,c}$ , R. Mazini $^{153}$ , I. Maznas $^{156}$ , S.M. Mazza $^{94a,94b}$  
N.C. Mc Fadden $^{107}$ , G. Mc Goldrick $^{161}$ , S.P. Mc Kee $^{92}$ , A. McCarn $^{92}$ , R.L. McCarthy $^{150}$ ,  
T.G. McCarthy $^{103}$ , L.I. Clymont $^{81}$ , E.F. McDonald $^{91}$ , J.A. Mcfayden $^{81}$ , G. Mchedlidze $^{57}$  
S.J. McMahon<sup>133</sup>, P.C. McNamara<sup>91</sup>, R.A. McPherson<sup>172,o</sup>, S. Meehan<sup>140</sup>, T.J. Megy<sup>51</sup>,  
S. Mehlhase $^{102}$ , A. Mehta $^{77}$ , T. Meideck $^{58}$ , K. Meier $^{60a}$ , B. Meirose $^{44}$ , D. Melini $^{170,aj}$  
B.R. Mellado Garcia $^{147c}$ , J.D. Mellenthin $^{57}$ , M. Melo $^{146a}$ , F. Meloni $^{18}$ , S.B. Menary $^{87}$ ,  
L. Meng $^{77}$ , X.T. Meng $^{92}$ , A. Mengarelli $^{22a,22b}$ , S. Menke $^{103}$ , E. Meoni $^{40a,40b}$ , S. Mergelmeyer $^{17}$  
P. Mermod $^{52}$ , L. Merola $^{106a,106b}$ , C. Meroni $^{94a}$ , F.S. Merritt $^{33}$ , A. Messina $^{134a,134b}$ , J. Metcalfe $^{6}$  
A.S. Mete $^{166}$ , C. Meyer $^{124}$ , J-P. Meyer $^{138}$ , J. Meyer $^{109}$ , H. Meyer Zu Theenhausen $^{60a}$ ,  
F. Miano $^{151}$ , R.P. Middleton $^{133}$ , S. Miglioranzi $^{53a,53b}$ , L. Mijović $^{49}$ , G. Mikenberg $^{175}$ ,  
M. Mikestikova $^{129}$ , M. Mikuz $^{78}$ , M. Milesi $^{91}$ , A. Milic $^{161}$ , D.W. Miller $^{33}$ , C. Mills $^{49}$ , A. Milov $^{175}$ ,  
D.A. Milstead $^{148a,148b}$ , A.A. Minaenko $^{132}$ , Y. Minami $^{157}$ , I.A. Minashvili $^{68}$ , A.I. Mincer $^{112}$ ,  
B. Mindur $^{41a}$ , M. Mineev $^{68}$ , Y. Minegishi $^{157}$ , Y. Ming $^{176}$ , L.M. Mir $^{13}$ , K.P. Mistry $^{124}$ ,  
T. Mitani $^{174}$ , J. Mitrevski $^{102}$ , V.A. Mitsou $^{170}$ , A. Miucci $^{18}$ , P.S. Miyagawa $^{141}$ , A. Mizukami $^{69}$  
J.U. Mjörnmark $^{84}$ , T. Mkrchyan $^{180}$ , M. Mlynarikova $^{131}$ , T. Moa $^{148a,148b}$ , K. Mochizuki $^{97}$ ,  
P. Mogg $^{51}$ , S. Mohapatra $^{38}$ , S. Molander $^{148a,148b}$ , R. Moles-Valls $^{23}$ , R. Monden $^{71}$ ,  
M.C. Mondragon $^{93}$ , K. Monig $^{45}$ , J. Monk $^{39}$ , E. Monnier $^{88}$ , A. Montalbano $^{150}$ ,  
J. Montejo Berlingen $^{32}$ , F. Monticelli $^{74}$ , S. Monzani $^{94a,94b}$ , R.W. Moore $^{3}$ , N. Morange $^{119}$  
D. Moreno $^{21}$ , M. Moreno Llacer $^{32}$ , P. Moretti $^{53a}$ , S. Morgenstern $^{32}$ , D. Mori $^{144}$ , T. Mori $^{157}$  
M. Morii $^{59}$ , M. Morinaga $^{157}$ , V. Morisbak $^{121}$ , A.K. Morley $^{152}$ , G. Mornacchi $^{32}$ , J.D. Morris $^{79}$  
L. Morvaj<sup>150</sup>, P. Moschovakos<sup>10</sup>, M. Mosidze<sup>54b</sup>, H.J. Moss<sup>141</sup>, J. Moss<sup>145,ak</sup>, K. Motohashi<sup>159</sup>,  
R. Mount $^{145}$ , E. Mountricha $^{27}$ , E.J.W. Moyse $^{89}$ , S. Muanza $^{88}$ , R.D. Mudd $^{19}$ , F. Mueller $^{103}$  
J. Mueller $^{127}$ , R.S.P. Mueller $^{102}$ , D. Muenstermann $^{75}$ , P. Mullen $^{56}$ , G.A. Mullier $^{18}$ ,  
F.J. Munoz Sanchez $^{87}$ , W.J. Murray $^{173,133}$ , H. Musheghyan $^{32}$ , M. Muškinja $^{78}$  
A.G. Myagkov $^{132,al}$ , M. Myska $^{130}$ , B.P. Nachman $^{16}$ , O. Nackenhorst $^{52}$ , K. Nagai $^{122}$  
R. Nagai $^{69,ad}$ , K. Nagano $^{69}$ , Y. Nagasaka $^{61}$ , K. Nagata $^{164}$ , M. Nagel $^{51}$ , E. Nagy $^{88}$ , A.M. Nairz $^{32}$  
Y. Nakahama $^{105}$ , K. Nakamura $^{69}$ , T. Nakamura $^{157}$ , I. Nakano $^{114}$ , R.F. Naranjo Garcia $^{45}$ ,  
R. Narayan $^{11}$ , D.I. Narrias Villar $^{60a}$ , I. Naryshkin $^{125}$ , T. Naumann $^{45}$ , G. Navarro $^{21}$ , R. Nayyar $^{7}$  
H.A. Neal $^{92}$ , P.Yu. Nechaeva $^{98}$ , T.J. Neep $^{138}$ , A. Negri $^{123a,123b}$ , M. Negrini $^{22a}$ , S. Nektarijevic $^{108}$ ,  
C. Nellist $^{119}$ , A. Nelson $^{166}$ , M.E. Nelson $^{122}$ , S. Nemecek $^{129}$ , P. Nemethy $^{112}$ , M. Nessi $^{32,am}$  
M.S. Neubauer $^{169}$ , M. Neumann $^{178}$ , P.R. Newman $^{19}$ , T.Y. Ng $^{62c}$ , T. Nguyen Manh $^{97}$  
R.B. Nickerson $^{122}$ , R. Nicolaidou $^{138}$ , J. Nielsen $^{139}$ , V. Nikolaenko $^{132,al}$ , I. Nikolic-Audit $^{83}$  
K. Nikolopoulos $^{19}$ , J.K. Nilsen $^{121}$ , P. Nilsson $^{27}$ , Y. Ninomiya $^{157}$ , A. Nisati $^{134a}$ , N. Nishu $^{35c}$  
R. Nisius $^{103}$ , I. Nitsche $^{46}$ , T. Nitta $^{174}$ , T. Nobe $^{157}$ , Y. Noguchi $^{71}$ , M. Nomachi $^{120}$ , I. Nomidis $^{31}$  
M.A. Nomura $^{27}$ , T. Nooney $^{79}$ , M. Nordberg $^{32}$ , N. Norjoharuddeen $^{122}$ , O. Novgorodova $^{47}$  
S. Nowak<sup>103</sup>, M. Nozaki<sup>69</sup>, L. Nozka<sup>117</sup>, K. Ntekas<sup>166</sup>, E. Nurse<sup>81</sup>, F. Nuti<sup>91</sup>, K. O'connor<sup>25</sup>,  
D.C. O'Neil $^{144}$ , A.A. O'Rourke $^{45}$ , V. O'Shea $^{56}$ , F.G. Oakham $^{31,d}$ , H. Oberlack $^{103}$  
T. Obermann $^{23}$ , J. Ocariz $^{83}$ , A. Ochi $^{70}$ , I. Ochoa $^{38}$ , J.P. Ochoa-Ricoux $^{34a}$ , S. Oda $^{73}$ , S. Odaka $^{69}$  
H. Ogren $^{64}$ , A. Oh $^{87}$ , S.H. Oh $^{48}$ , C.C. Ohm $^{16}$ , H. Ohman $^{168}$ , H. Oide $^{53a,53b}$ , H. Okawa $^{164}$ ,  
Y. Okumura $^{157}$ , T. Okuyama $^{69}$ , A. Olariu $^{28b}$ , L.F. Oleiro Seabra $^{128a}$ , S.A. Olivares Pino $^{49}$  
D. Oliveira Damazio $^{27}$ , A. Olszewski $^{42}$ , J. Olszowska $^{42}$ , A. Onofre $^{128a,128e}$ , K. Onogi $^{105}$  
P.U.E. Onyisi<sup>11,z</sup>, M.J. Oreglia<sup>33</sup>, Y. Oren<sup>155</sup>, D. Orestano<sup>136a,136b</sup>, N. Orlando<sup>62b</sup>, R.S. Orr<sup>161</sup>,  
B. Osculati $^{53a,53b,*}$ , R. Ospanov $^{36a}$ , G. Otero y Garzon $^{29}$ , H. Otono $^{73}$ , M. Ouchrif $^{137d}$

F. Ould-Saada<sup>121</sup>, A. Ouraou<sup>138</sup>, K.P. Oussoren<sup>109</sup>, Q. Ouyang<sup>35a</sup>, M. Owen<sup>56</sup>, R.E. Owen<sup>19</sup>,  
V.E. Ozcan $^{20a}$ , N. Ozturk $^{8}$ , K. Pachal $^{144}$ , A. Pacheco Pages $^{13}$ , L. Pacheco Rodriguez $^{138}$ ,  
C. Padilla Aranda $^{13}$ , S. Pagan Griso $^{16}$ , M. Paganini $^{179}$ , F. Paige $^{27}$ , G. Palacino $^{64}$ ,  
S. Palazzo $^{40a,40b}$ , S. Palestini $^{32}$ , M. Palka $^{41b}$ , D. Pallin $^{37}$ , E.St. Panagiotopoulou $^{10}$  
I. Panagoulias<sup>10</sup>, C.E. Pandini<sup>83</sup>, J.G. Panduro Vazquez<sup>80</sup>, P. Pani<sup>32</sup>, S. Panitkin<sup>27</sup>,  
D. Pantea $^{28b}$ , L. Paolozzi $^{52}$ , Th.D. Papadopoulou $^{10}$ , K. Papageorgiou $^{9,s}$ , A. Paramonov $^{6}$  
D. Paredes Hernandez $^{179}$ , A.J. Parker $^{75}$ , M.A. Parker $^{30}$ , K.A. Parker $^{45}$ , F. Parodi $^{53a,53b}$  
J.A. Parsons<sup>38</sup>, U. Parzefall<sup>51</sup>, V.R. Pascuzzi<sup>161</sup>, J.M. Pasner<sup>139</sup>, E. Pasqualucci<sup>134a</sup>,  
S. Passaggio $^{53a}$ , Fr. Pastore $^{80}$ , S. Pataraia $^{178}$ , J.R. Pater $^{87}$ , T. Pauly $^{32}$ , B. Pearson $^{103}$  
S. Pedraza Lopez $^{170}$ , R. Pedro $^{128a,128b}$ , S.V. Peleganchuk $^{111,c}$ , O. Penc $^{129}$ , C. Peng $^{35a}$  
H. Peng $^{36a}$ , J. Penwell $^{64}$ , B.S. Peralva $^{26b}$ , M.M. Perego $^{138}$ , D.V. Perepelitsa $^{27}$ , F. Peri $^{17}$  
L. Perini $^{94a,94b}$ , H. Pernegger $^{32}$ , S. Perrella $^{106a,106b}$ , R. Peschke $^{45}$ , V.D. Peshekhonov $^{68,*}$  
K. Peters $^{45}$ , R.F.Y. Peters $^{87}$ , B.A. Petersen $^{32}$ , T.C. Petersen $^{39}$ , E. Petit $^{58}$ , A. Petridis $^{1}$  
C. Petridou $^{156}$ , P. Petroff $^{119}$ , E. Petrolo $^{134a}$ , M. Petrov $^{122}$ , F. Petrucci $^{136a,136b}$  
N.E. Pettersson $^{89}$ , A. Peyaud $^{138}$ , R. Pezoa $^{34b}$ , F.H. Phillips $^{93}$ , P.W. Phillips $^{133}$ ,  
G. Piacquadio $^{150}$ , E. Pianori $^{173}$ , A. Picazio $^{89}$ , E. Piccaro $^{79}$ , M.A. Pickering $^{122}$ , R. Piegaia $^{29}$  
J.E. Pilcher $^{33}$ , A.D. Pilkington $^{87}$ , A.W.J. Pin $^{87}$ , M. Pinamonti $^{135a,135b}$ , J.L. Pinfold $^{3}$ ,  
H. Pirumov $^{45}$ , M. Pitt $^{175}$ , L. Plazak $^{146a}$ , M.-A. Pleier $^{27}$ , V. Pleskot $^{86}$ , E. Plotnikova $^{68}$  
D. Pluth $^{67}$ , P. Podberezko $^{111}$ , R. Poettgen $^{148a,148b}$ , R. Poggi $^{123a,123b}$ , L. Poggioli $^{119}$ , D. Pohl $^{23}$  
G. Polesello $^{123a}$ , A. Paley $^{45}$ , A. Policicchio $^{40a,40b}$ , R. Polifka $^{32}$ , A. Polini $^{22a}$ , C.S. Pollard $^{56}$ ,  
V. Polychronakos $^{27}$ , K. Pommès $^{32}$ , D. Ponomarenko $^{100}$ , L. Pontecorvo $^{134a}$ , B.G. Pope $^{93}$  
G.A. Popeneciu $^{28d}$ , A. Poppleton $^{32}$ , S. Pospisil $^{130}$ , K. Potamianos $^{16}$ , I.N. Potrap $^{68}$ , C.J. Potter $^{30}$ ,  
G. Poulard $^{32}$ , T. Poulsen $^{84}$ , J. Poveda $^{32}$ , M.E. Pozo Astigarraga $^{32}$ , P. Pralavorio $^{88}$ , A. Pranko $^{16}$  
S. Prell $^{67}$ , D. Price $^{87}$ , L.E. Price $^{6}$ , M. Primavera $^{76a}$ , S. Prince $^{90}$ , N. Proklova $^{100}$ , K. Prokofiev $^{62c}$  
F. Prokoshin $^{34b}$ , S. Protopopescu $^{27}$ , J. Proudfoot $^{6}$ , M. Przybycien $^{41a}$ , A. Puri $^{169}$ , P. Puzo $^{119}$  
J. Qian $^{92}$ , G. Qin $^{56}$ , Y. Qin $^{87}$ , A. Quadt $^{57}$ , M. Queitsch-Maitland $^{45}$ , D. Quilty $^{56}$ , S. Raddum $^{121}$  
V. Radeka $^{27}$ , V. Radescu $^{122}$ , S.K. Radhakrishnan $^{150}$ , P. Radloff $^{118}$ , P. Rados $^{91}$ , F. Ragusa $^{94a,94b}$  
G. Rahal $^{181}$ , J.A. Raine $^{87}$ , S. Rajagopalan $^{27}$ , C. Rangel-Smith $^{168}$ , T. Rashid $^{119}$ , S. Raspopov $^{5}$  
M.G. Ratti $^{94a,94b}$ , D.M. Rauch $^{45}$ , F. Rauscher $^{102}$ , S. Rave $^{86}$ , I. Ravinovich $^{175}$ , J.H. Rawling $^{87}$ ,  
M. Raymond $^{32}$ , A.L. Read $^{121}$ , N.P. Readioff $^{58}$ , M. Reale $^{76a,76b}$ , D.M. Rebuzzi $^{123a,123b}$  
A. Redelbach<sup>177</sup>, G. Redlinger<sup>27</sup>, R. Reece<sup>139</sup>, R.G. Reed<sup>147c</sup>, K. Reeves<sup>44</sup>, L. Rehnisch<sup>17</sup>,  
J. Reichert $^{124}$ , A. Reiss $^{86}$ , C. Rembser $^{32}$ , H. Ren $^{35a}$ , M. Rescigno $^{134a}$ , S. Resconi $^{94a}$  
E.D. Resseguie $^{124}$ , S. Rettie $^{171}$ , E. Reynolds $^{19}$ , O.L. Rezanova $^{111,c}$ , P. Reznicek $^{131}$ , R. Rezvani $^{97}$ ,  
R. Richter $^{103}$ , S. Richter $^{81}$ , E. Richter-Was $^{41b}$ , O. Ricken $^{23}$ , M. Ridel $^{83}$ , P. Rieck $^{103}$  
C.J. Riegel $^{178}$ , J. Rieger $^{57}$ , O. Rifki $^{115}$ , M. Rijssenbeek $^{150}$ , A. Rimoldi $^{123a,123b}$ , M. Rimoldi $^{18}$  
L. Rinaldi $^{22a}$ , G. Ripellino $^{149}$ , B. Ristic $^{32}$ , E. Ritsch $^{32}$ , I. Riu $^{13}$ , F. Rizatdinova $^{116}$ , E. Rizvi $^{79}$ ,  
C. Rizzi $^{13}$ , R.T. Roberts $^{87}$ , S.H. Robertson $^{90,o}$ , A. Robichaud-Veronneau $^{90}$ , D. Robinson $^{30}$  
J.E.M. Robinson $^{45}$ , A. Robson $^{56}$ , E. Rocco $^{86}$ , C. Roda $^{126a,126b}$ , Y. Rodina $^{88,an}$  
S. Rodriguez Bosca<sup>170</sup>, A. Rodriguez Perez<sup>13</sup>, D. Rodriguez Rodriguez<sup>170</sup>, S. Roe<sup>32</sup>,  
C.S. Rogan $^{59}$ , O. Røhne $^{121}$ , J. Roloff $^{59}$ , A. Romaniouk $^{100}$ , M. Romano $^{22a,22b}$  
S.M. Romano Saez $^{37}$ , E. Romero Adam $^{170}$ , N. Rompotis $^{77}$ , M. Ronzani $^{51}$ , L. Roos $^{83}$ ,  
S. Rosati $^{134a}$ , K. Rosbach $^{51}$ , P. Rose $^{139}$ , N.-A. Rosien $^{57}$ , E. Rossi $^{106a,106b}$ , L.P. Rossi $^{53a}$  
J.H.N. Rosten $^{30}$ , R. Rosten $^{140}$ , M. Rotaru $^{28b}$ , I. Roth $^{175}$ , J. Rothberg $^{140}$ , D. Rousseau $^{119}$  
A. Rozanov $^{88}$ , Y. Rozen $^{154}$ , X. Ruan $^{147c}$ , F. Rubbo $^{145}$ , F. Rühr $^{51}$ , A. Ruiz-Martinez $^{31}$  
Z. Rurikova $^{51}$ , N.A. Rusakovich $^{68}$ , H.L. Russell $^{90}$ , J.P. Rutherfoord $^{7}$ , N. Ruthmann $^{32}$  
Y.F. Ryabov $^{125}$ , M. Rybar $^{169}$ , G. Rybkin $^{119}$ , S. Ryu $^{6}$ , A. Ryzhov $^{132}$ , G.F. Rzehorz $^{57}$ ,  
A.F. Saavedra $^{152}$ , G. Sabato $^{109}$ , S. Sacerdoti $^{29}$ , H.F-W. Sadrozinski $^{139}$ , R. Sadykov $^{68}$  
F. Safai Tehrani $^{134a}$ , P. Saha $^{110}$ , M. Sahinsoy $^{60a}$ , M. Saimpert $^{45}$ , M. Saito $^{157}$ , T. Saito $^{157}$ ,

H. Sakamoto $^{157}$ , Y. Sakurai $^{174}$ , G. Salamanna $^{136a,136b}$ , J.E. Salazar Loyola $^{34b}$ , D. Salek $^{109}$  
P.H. Sales De Bruin $^{168}$ , D. Salihagic $^{103}$ , A. Salnikov $^{145}$ , J. Salt $^{170}$ , D. Salvatore $^{40a,40b}$  
F. Salvatore $^{151}$ , A. Salvucci $^{62a,62b,62c}$ , A. Salzburger $^{32}$ , D. Sammel $^{51}$ , D. Sampsonidis $^{156}$ ,  
D. Sampsonidou<sup>156</sup>, J. Sánchez<sup>170</sup>, V. Sanchez Martinez<sup>170</sup>, A. Sanchez Pineda<sup>167a,167c</sup>,  
H. Sandaker $^{121}$ , R.L. Sandbach $^{79}$ , C.O. Sander $^{45}$ , M. Sandhoff $^{178}$ , C. Sandoval $^{21}$ ,  
D.P.C. Sankey $^{133}$ , M. Sannino $^{53a,53b}$ , Y. Sano $^{105}$ , A. Sansoni $^{50}$ , C. Santoni $^{37}$ ,  
R. Santonico $^{135a,135b}$ , H. Santos $^{128a}$ , I. Santoyo Castillo $^{151}$ , A. Saponov $^{68}$ , J.G. Saraiva $^{128a,128d}$  
B. Sarrazin $^{23}$ , O. Sasaki $^{69}$ , K. Sato $^{164}$ , E. Sauvan $^{5}$ , G. Savage $^{80}$ , P. Savard $^{161,d}$ , N. Savic $^{103}$  
C. Sawyer $^{133}$ , L. Sawyer $^{82,u}$ , J. Saxon $^{33}$ , C. Sbarra $^{22a}$ , A. Sbrizzi $^{22a,22b}$ , T. Scanlon $^{81}$  
D.A. Scannicchio $^{166}$ , M. Scarcella $^{152}$ , V. Scarfone $^{40a,40b}$ , J. Schaarschmidt $^{140}$ , P. Schacht $^{7}$  
B.M. Schachtner $^{102}$ , D. Schaefer $^{32}$ , L. Schaefer $^{124}$ , R. Schaefer $^{45}$ , J. Schaeffer $^{86}$ , S. Schaepe $^{23}$  
S. Schaetzel $^{60b}$ , U. Schäfer $^{86}$ , A.C. Schaffer $^{119}$ , D. Schaile $^{102}$ , R.D. Schamberger $^{150}$ , V. Scharf $^{60a}$  
V.A. Schegelsky $^{125}$ , D. Scheirich $^{131}$ , M. Schernau $^{166}$ , C. Schiavi $^{53a,53b}$ , S. Schier $^{139}$  
L.K. Schildgen $^{23}$ , C. Schillo $^{51}$ , M. Schioppa $^{40a,40b}$ , S. Schlenker $^{32}$ , K.R. Schmidt-Sommerfeld $^{103}$ ,  
K. Schmieden $^{32}$ , C. Schmitt $^{86}$ , S. Schmitt $^{45}$ , S. Schmitz $^{86}$ , U. Schnoor $^{51}$ , L. Schoeffel $^{138}$  
A. Schoening $^{60b}$ , B.D. Schoenrock $^{93}$ , E. Schopf $^{23}$ , M. Schott $^{86}$ , J.F.P. Schouwenberg $^{108}$  
J. Schovancova $^{32}$ , S. Schramm $^{52}$ , N. Schuh $^{86}$ , A. Schulte $^{86}$ , M.J. Schultens $^{23}$  
H.-C. Schultz-Coulon $^{60a}$ , H. Schulz $^{17}$ , M. Schumacher $^{51}$ , B.A. Schumm $^{139}$ , Ph. Schune $^{138}$ ,  
A. Schwartzman<sup>145</sup>, T.A. Schwarz<sup>92</sup>, H. Schweiger<sup>87</sup>, Ph. Schwemling<sup>138</sup>, R. Schwienhorst<sup>93</sup>,  
J. Schwindling $^{138}$ , A. Sciandra $^{23}$ , G. Sciolla $^{25}$ , M. Scornajenghi $^{40a,40b}$ , F. Scuri $^{126a,126b}$  
F. Scutti $^{91}$ , J. Searcy $^{92}$ , P. Seema $^{23}$ , S.C. Seidel $^{107}$ , A. Seiden $^{139}$ , J.M. Seixas $^{26a}$ ,  
G. Sekhniaidze $^{106a}$ , K. Sekhon $^{92}$ , S.J. Sekula $^{43}$ , N. Semprini-Cesari $^{22a,22b}$ , S. Senkin $^{37}$  
C. Serfon $^{121}$ , L. Serin $^{119}$ , L. Serkin $^{167a,167b}$ , M. Sessa $^{136a,136b}$ , R. Seuster $^{172}$ , H. Severini $^{115}$  
T. Sfiligoj $^{78}$ , F. Sforza $^{32}$ , A. Sfyrla $^{52}$ , E. Shabalina $^{57}$ , N.W. Shaikh $^{148a,148b}$ , L.Y. Shan $^{35a}$ .  
R. Shang $^{169}$ , J.T. Shank $^{24}$ , M. Shapiro $^{16}$ , P.B. Shatalov $^{99}$ , K. Shaw $^{167a,167b}$ , S.M. Shaw $^{87}$  
A. Shcherbakova $^{148a,148b}$ , C.Y. Shehu $^{151}$ , Y. Shen $^{115}$ , N. Sherafati $^{31}$ , P. Sherwood $^{81}$ , L. Shi $^{153,ao}$  
S. Shimizu $^{70}$ , C.O. Shimmin $^{179}$ , M. Shimojima $^{104}$ , I.P.J. Shipsey $^{122}$ , S. Shirabe $^{73}$  
M. Shiyakova $^{68,ap}$ , J. Shlomi $^{175}$ , A. Shmeleva $^{98}$ , D. Shoaleh Saadi $^{97}$ , M.J. Shochet $^{33}$  
S. Shojai $^{94a}$ , D.R. Shope $^{115}$ , S. Shrestha $^{113}$ , E. Shulga $^{100}$ , M.A. Shupe $^{7}$ , P. Sicho $^{129}$  
A.M. Sickles $^{169}$ , P.E. Sidebo $^{149}$ , E. Sideras Haddad $^{147c}$ , O. Sidiropoulou $^{177}$ , A. Sidoti $^{22a,22b}$  
F. Siegert $^{47}$ , Dj. Sijacki $^{14}$ , J. Silva $^{128a,128d}$ , S.B. Silverstein $^{148a}$ , V. Simak $^{130}$ , Lj. Simic $^{14}$  
S. Simion $^{119}$ , E. Simioni $^{86}$ , B. Simmons $^{81}$ , M. Simon $^{86}$ , P. Sinervo $^{161}$ , N.B. Sinev $^{118}$  
M. Sioli $^{22a,22b}$ , G. Siragusa $^{177}$ , I. Siral $^{92}$ , S.Yu. Sivoklokov $^{101}$ , J. Sjolin $^{148a,148b}$ , M.B. Skinner $^{75}$ ,  
P. Skubic $^{115}$ , M. Slater $^{19}$ , T. Slavicek $^{130}$ , M. Slawinska $^{42}$ , K. Sliwa $^{165}$ , R. Slovak $^{131}$ ,  
V. Smakhtin<sup>175</sup>, B.H. Smart<sup>5</sup>, J. Smiesko<sup>146a</sup>, N. Smirnov<sup>100</sup>, S.Yu. Smirnov<sup>100</sup>, Y. Smirnov<sup>100</sup>,  
L.N. Smirnova $^{101,aq}$ , O. Smirnova $^{84}$ , J.W. Smith $^{57}$ , M.N.K. Smith $^{38}$ , R.W. Smith $^{38}$ ,  
M. Smizanska $^{75}$ , K. Smolek $^{130}$ , A.A. Snesarev $^{98}$ , I.M. Snyder $^{118}$ , S. Snyder $^{27}$ , R. Sobie $^{172,o}$  
F. Socher $^{47}$ , A. Soffer $^{155}$ , D.A. Soh $^{153}$ , G. Sokhrannyi $^{78}$ , C.A. Solans Sanchez $^{32}$ , M. Solar $^{130}$  
E.Yu. Soldatov<sup>100</sup>, U. Soldevila<sup>170</sup>, A.A. Solodkov<sup>132</sup>, A. Soloshenko<sup>68</sup>, O.V. Solovyanov<sup>132</sup>,  
V. Solovyev<sup>125</sup>, P. Sommer<sup>51</sup>, H. Son<sup>165</sup>, A. Sopczak<sup>130</sup>, D. Sosa<sup>60b</sup>, C.L. Sotiropoulou<sup>126a,126b</sup>,  
R. Soualah $^{167a,167c}$ , A.M. Soukharev $^{111,c}$ , D. South $^{45}$ , B.C. Sowden $^{80}$ , S. Spagnolo $^{76a,76b}$ ,  
M. Spalla $^{126a,126b}$ , M. Spangenberg $^{173}$ , F. Spanò $^{80}$ , D. Sperlich $^{17}$ , F. Spettel $^{103}$ , T.M. Spieker $^{60a}$  
R. Spighi $^{22a}$ , G. Spigo $^{32}$ , L.A. Spiller $^{91}$ , M. Spousta $^{131}$ , R.D. St. Denis $^{56,*}$ , A. Stabile $^{94a}$  
R. Stamen $^{60a}$ , S. Stamm $^{17}$ , E. Stanecka $^{42}$ , R.W. Stanek $^{6}$ , C. Stanescu $^{136a}$ , M.M. Stanitzki $^{45}$ ,  
B.S. Stapf $^{109}$ , S. Stapnes $^{121}$ , E.A. Starchenko $^{132}$ , G.H. Stark $^{33}$ , J. Stark $^{58}$ , S.H Stark $^{39}$  
P. Staroba $^{129}$ , P. Starovoitov $^{60a}$ , S. Stärz $^{32}$ , R. Staszewski $^{42}$ , P. Steinberg $^{27}$ , B. Stelzer $^{144}$  
H.J. Stelzer $^{32}$ , O. Stelzer-Chilton $^{163a}$ , H. Stenzel $^{55}$ , G.A. Stewart $^{56}$ , M.C. Stockton $^{118}$ ,  
M. Stoebe $^{90}$ , G. Stoicea $^{28b}$ , P. Stolte $^{57}$ , S. Stonjek $^{103}$ , A.R. Stradling $^{8}$ , A. Straessner $^{47}$

M.E. Stramaglia $^{18}$ , J. Strandberg $^{149}$ , S. Strandberg $^{148a,148b}$ , M. Strauss $^{115}$ , P. Strizenec $^{146b}$ , R. Strohmer $^{177}$ , D.M. Strom $^{118}$ , R. Stroynowski $^{43}$ , A. Strubig $^{108}$ , S.A. Stucci $^{27}$ , B. Stugu $^{15}$ , N.A. Styles $^{45}$ , D. Su $^{145}$ , J. Su $^{127}$ , S. Suchek $^{60a}$ , Y. Sugaya $^{120}$ , M. Suk $^{130}$ , V.V. Sulin $^{98}$ , DMS Sultan $^{162a,162b}$ , S. Sultansoy $^{4c}$ , T. Sumida $^{71}$ , S. Sun $^{59}$ , X. Sun $^{3}$ , K. Suruliz $^{151}$ , C.J.E. Suster $^{152}$ , M.R. Sutton $^{151}$ , S. Suzuki $^{69}$ , M. Svatos $^{129}$ , M. Swiatlowski $^{33}$ , S.P. Swift $^{2}$ ,  
I. Sykora $^{146a}$ , T. Sykora $^{131}$ , D. Ta $^{51}$ , K. Tackmann $^{45}$ , J. Taenzer $^{155}$ , A. Taffard $^{166}$ ,  
R. Tafirout<sup>163a</sup>, N. Taiblum<sup>155</sup>, H. Takai<sup>27</sup>, R. Takashima<sup>72</sup>, E.H. Takasugi<sup>103</sup>, T. Takeshita<sup>142</sup>, Y. Takubo<sup>69</sup>, M. Talby<sup>88</sup>, A.A. Talyshev<sup>111,c</sup>, J. Tanaka<sup>157</sup>, M. Tanaka<sup>159</sup>, R. Tanaka<sup>119</sup>,  
S. Tanaka $^{69}$ , R. Tanioka $^{70}$ , B.B. Tannenwald $^{113}$ , S. Tapia Araya $^{34b}$ , S. Tappprogge $^{86}$ , S. Tarem $^{154}$ , G.F. Tartarelli $^{94a}$ , P. Tas $^{131}$ , M. Tasevsky $^{129}$ , T. Tashiro $^{71}$ , E. Tassi $^{40a,40b}$ ,  
A. Tavares Delgado $^{128a,128b}$ , Y. Tayalati $^{137e}$ , A.C. Taylor $^{107}$ , G.N. Taylor $^{91}$ , P.T.E. Taylor $^{91}$ ,  
W. Taylor $^{163b}$ , P. Teixeira-Dias $^{80}$ , D. Temple $^{144}$ , H. Ten Kate $^{32}$ , P.K. Teng $^{153}$ , J.J. Teoh $^{120}$ ,  
F. Tepel<sup>178</sup>, S. Terada<sup>69</sup>, K. Terashi<sup>157</sup>, J. Terron<sup>85</sup>, S. Terzo<sup>13</sup>, M. Testa<sup>50</sup>, R.J. Teuscher<sup>161,o</sup>,  
T. Theveneaux-Pelzer $^{88}$ , J.P. Thomas $^{19}$ , J. Thomas-Wilsker $^{80}$ , P.D. Thompson $^{19}$ ,  
A.S. Thompson $^{56}$ , L.A. Thomsen $^{179}$ , E. Thomson $^{124}$ , M.J. Tibbetts $^{16}$ , R.E. Ticse Torres $^{88}$ ,  
V.O. Tikhomirov $^{98,ar}$ , Yu.A. Tikhonov $^{111,c}$ , S. Timoshenko $^{100}$ , P. Tipton $^{179}$ , S. Tisserant $^{88}$  
K. Todome $^{159}$ , S. Todorova-Nova $^{5}$ , S. Todt $^{47}$ , J. Tojo $^{73}$ , S. Tokár $^{146a}$ , K. Tokushuku $^{69}$  
E. Tolley $^{59}$ , L. Tomlinson $^{87}$ , M. Tomoto $^{105}$ , L. Tompkins $^{145,as}$ , K. Toms $^{107}$ , B. Tong $^{59}$  
P. Tornambe $^{51}$ , E. Torrence $^{118}$ , H. Torres $^{144}$ , E. Torro Pastor $^{140}$ , J. Toth $^{88,at}$ , F. Touchard $^{88}$  
D.R. Tovey $^{141}$ , C.J. Treado $^{112}$ , T. Trefzger $^{177}$ , F. Tresoldi $^{151}$ , A. Tricoli $^{27}$ , I.M. Trigger $^{163a}$  
S. Trincaz-Duvoid $^{83}$ , M.F. Tripiana $^{13}$ , W. Trischuk $^{161}$ , B. Trocmé $^{58}$ , A. Trofymov $^{45}$ ,  
C. Troncon $^{94a}$ , M. Trottier-McDonald $^{16}$ , M. Sovatelli $^{172}$ , L. Truong $^{167a,167c}$ , M. Trzebinski $^{42}$  
A. Trzupek $^{42}$ , K.W. Tsang $^{62a}$ , J.C-L. Tseng $^{122}$ , P.V. Tsireshka $^{95}$ , G. Tsipolitis $^{10}$  
N. Tsirintanis<sup>9</sup>, S. Tsiskaridze<sup>13</sup>, V. Tsiskaridze<sup>51</sup>, E.G. Tskhadadze<sup>54a</sup>, K.M. Tsui<sup>62a</sup>,  
I.I. Tsukerman $^{99}$ , V. Tsulaia $^{16}$ , S. Tsuno $^{69}$ , D. Tsybychev $^{150}$ , Y. Tu $^{62b}$ , A. Tudorache $^{28b}$  
V. Tudorache $^{28b}$ , T.T. Tulbure $^{28a}$ , A.N. Tuna $^{59}$ , S.A. Tupputi $^{22a,22b}$ , S. Turchikhin $^{68}$ ,  
D. Turgeman $^{175}$ , I. Turk Cakir $^{4b,au}$ , R. Turra $^{94a}$ , P.M. Tuts $^{38}$ , G. Ucchielli $^{22a,22b}$ , I. Ueda $^{69}$  
M. Ughetto $^{148a,148b}$ , F. Ukegawa $^{164}$ , G. Unal $^{32}$ , A. Undrus $^{27}$ , G. Unel $^{166}$ , F.C. Ungaro $^{91}$ ,  
Y. Unno $^{69}$ , C. Unverdorben $^{102}$ , J. Urban $^{146b}$ , P. Urquijo $^{91}$ , P. Urrejola $^{86}$ , G. Usai $^{8}$ , J. Usui $^{69}$  
L. Vacavant $^{88}$ , V. Vacek $^{130}$ , B. Vachon $^{90}$ , A. Vaidya $^{81}$ , C. Valderanis $^{102}$  
E. Valdes Santurio $^{148a,148b}$ , S. Valentinetti $^{22a,22b}$ , A. Valero $^{170}$ , L. Valery $^{13}$ , S. Valkar $^{131}$  
A. Vallier<sup>5</sup>, J.A. Valls Ferrer<sup>170</sup>, W. Van Den Wollenberg<sup>109</sup>, H. van der Graaf<sup>109</sup>  
P. van Gemmeren<sup>6</sup>, J. Van Nieuwkoop<sup>144</sup>, I. van Vulpen<sup>109</sup>, M.C. van Woerden<sup>109</sup>,  
M. Vanadia $^{135a,135b}$ , W. Vandelli $^{32}$ , A. Vaniachine $^{160}$ , P. Vankov $^{109}$ , G. Vardanyan $^{180}$ ,  
R. Vari $^{134a}$ , E.W. Varnes $^{7}$ , C. Varni $^{53a,53b}$ , T. Varol $^{43}$ , D. Varouchas $^{119}$ , A. Vartapetian $^{8}$  
K.E. Varvell $^{152}$ , J.G. Vasquez $^{179}$ , G.A. Vasquez $^{34b}$ , F. Vazeille $^{37}$ , T. Vazquez Schroeder $^{90}$  
J. Veatch $^{57}$ , V. Veeraraghavan $^{7}$ , L.M. Veloc $^{161}$ , F. Veloso $^{128a,128c}$ , S. Veneziano $^{134a}$  
A. Ventura $^{76a,76b}$ , M. Venturi $^{172}$ , N. Venturi $^{32}$ , A. Venturini $^{25}$ , V. Vercesi $^{123a}$  
M. Verducci $^{136a,136b}$ , W. Verkerke $^{109}$ , A.T. Vermeulen $^{109}$ , J.C. Vermeulen $^{109}$ , M.C. Vetterli $^{144,d}$  
N. Viaux Maira $^{34b}$ , O. Viazlo $^{84}$ , I. Vichou $^{169,*}$ , T. Vickey $^{141}$ , O.E. Vickey Boeriu $^{141}$  
G.H.A. Viehhauser<sup>122</sup>, S. Viel<sup>16</sup>, L. Vigani<sup>122</sup>, M. Villa<sup>22a,22b</sup>, M. Villaplana Perez<sup>94a,94b</sup>,  
E. Vilucchi $^{50}$ , M.G. Vincter $^{31}$ , V.B. Vinogradov $^{68}$ , A. Vishwakarma $^{45}$ , C. Vittori $^{22a,22b}$  
I. Vivarelli $^{151}$ , S. Vlachos $^{10}$ , M. Vogel $^{178}$ , P. Vokac $^{130}$ , G. Volpi $^{126a,126b}$ , H. von der Schmitt $^{103}$ ,  
E. von Toerne $^{23}$ , V. Vorobel $^{131}$ , K. Vorovev $^{100}$ , M. Vos $^{170}$ , R. Voss $^{32}$ , J.H. Vossebeld $^{77}$  
N. Vranjes $^{14}$ , M. Vranjes Milosavljevic $^{14}$ , V. Vrba $^{130}$ , M. Vreeswijk $^{109}$ , R. Vuillermet $^{32}$  
I. Vukotic $^{33}$ , P. Wagner $^{23}$ , W. Wagner $^{178}$ , J. Wagner-Kuhr $^{102}$ , H. Wahlberg $^{74}$ , S. Wahrmund $^{47}$  
J. Wakabayashi $^{105}$ , J. Walder $^{75}$ , R. Walker $^{102}$ , W. Walkowiak $^{143}$ , V. Wallangen $^{148a,148b}$  
C. Wang $^{35b}$ , C. Wang $^{36b,av}$ , F. Wang $^{176}$ , H. Wang $^{16}$ , H. Wang $^{3}$ , J. Wang $^{45}$ , J. Wang $^{152}$

Q. Wang $^{115}$ , R. Wang $^{6}$ , S.M. Wang $^{153}$ , T. Wang $^{38}$ , W. Wang $^{153,aw}$ , W. Wang $^{36a}$ , Z. Wang $^{36c}$ ,  
C. Wanotayaroj $^{118}$ , A. Warburton $^{90}$ , C.P. Ward $^{30}$ , D.R. Wardrope $^{81}$ , A. Washbrook $^{49}$ ,  
P.M. Watkins $^{19}$ , A.T. Watson $^{19}$ , M.F. Watson $^{19}$ , G. Watts $^{140}$ , S. Watts $^{87}$ , B.M. Waugh $^{81}$ ,  
A.F. Webb $^{11}$ , S. Webb $^{86}$ , M.S. Weber $^{18}$ , S.W. Weber $^{177}$ , S.A. Weber $^{31}$ , J.S. Webster $^{6}$  
A.R. Weidberg $^{122}$ , B. Weinert $^{64}$ , J. Weingarten $^{57}$ , M. Weirich $^{86}$ , C. Weiser $^{51}$ , H. Weits $^{109}$ ,  
P.S. Wells $^{32}$ , T. Wenaus $^{27}$ , T. Wengler $^{32}$ , S. Wenig $^{32}$ , N. Werner $^{23}$ , M.D. Werner $^{67}$ , P. Werner $^{32}$ ,  
M. Wessels $^{60a}$ , K. Whalen $^{118}$ , N.L. Whallon $^{140}$ , A.M. Wharton $^{75}$ , A.S. White $^{92}$ , A. White $^{8}$  
M.J. White $^{1}$ , R. White $^{34b}$ , D. Whiteson $^{166}$ , B.W. Whitmore $^{75}$ , F.J. Wickens $^{133}$ ,  
W. Wiedenmann<sup>176</sup>, M. Wielers<sup>133</sup>, C. Wiglesworth<sup>39</sup>, L.A.M. Wiik-Fuchs<sup>23</sup>, A. Wildauer<sup>103</sup>,  
F. Wilk $^{87}$ , H.G. Wilkens $^{32}$ , H.H. Williams $^{124}$ , S. Williams $^{109}$ , C. Willis $^{93}$ , S. Willocq $^{89}$ ,  
J.A. Wilson $^{19}$ , I. Wingerter-Seez $^{5}$ , E. Winkels $^{151}$ , F. Winklmeier $^{118}$ , O.J. Winston $^{151}$ ,  
B.T. Winter $^{23}$ , M. Wittgen $^{145}$ , M. Wobisch $^{82,u}$ , T.M.H. Wolf $^{109}$ , R. Wolff $^{88}$ , M.W. Wolter $^{42}$ ,  
H. Wolters $^{128a,128c}$ , V.W.S. Wong $^{171}$ , S.D. Worm $^{19}$ , B.K. Wosiek $^{42}$ , J. Wotschack $^{32}$  
K.W. Wozniak $^{42}$ , M. Wu $^{33}$ , S.L. Wu $^{176}$ , X. Wu $^{52}$ , Y. Wu $^{92}$ , T.R. Wyatt $^{87}$ , B.M. Wynne $^{49}$  
S. Xella $^{39}$ , Z. Xi $^{92}$ , L. Xia $^{35c}$ , D. Xu $^{35a}$ , L. Xu $^{27}$ , T. Xu $^{138}$ , B. Yabsley $^{152}$ , S. Yacoob $^{147a}$  
D. Yamaguchi $^{159}$ , Y. Yamaguchi $^{120}$ , A. Yamamoto $^{69}$ , S. Yamamoto $^{157}$ , T. Yamanaka $^{157}$ ,  
M. Yamatani $^{157}$ , K. Yamauchi $^{105}$ , Y. Yamazaki $^{70}$ , Z. Yan $^{24}$ , H. Yang $^{36c}$ , H. Yang $^{16}$ , Y. Yang $^{153}$  
Z. Yang $^{15}$ , W-M. Yao $^{16}$ , Y.C. Yap $^{83}$ , Y. Yasu $^{69}$ , E. Yatsenko $^{5}$ , K.H. Yau Wong $^{23}$ , J. Ye $^{43}$  
S. Ye $^{27}$ , I. Yeletskikh $^{68}$ , E. Yigitbasi $^{24}$ , E. Yildirim $^{86}$ , K. Yorita $^{174}$ , K. Yoshihara $^{124}$  
C. Young $^{145}$ , C.J.S. Young $^{32}$ , J. Yu $^{8}$ , J. Yu $^{67}$ , S.P.Y. Yuen $^{23}$ , I. Yusuff $^{30,ax}$ , B. Zabinski $^{42}$  
G. Zacharis $^{10}$ , R. Zaidan $^{13}$ , A.M. Zaitsev $^{132,al}$ , N. Zakharchuk $^{45}$ , J. Zalieckas $^{15}$ , A. Zaman $^{150}$  
S. Zambito $^{59}$ , D. Zanzi $^{91}$ , C. Zeitnitz $^{178}$ , G. Zemaityte $^{122}$ , A. Zemla $^{41a}$ , J.C. Zeng $^{169}$ , Q. Zeng $^{145}$ ,  
O. Zenin $^{132}$ , T. Ženis $^{146a}$ , D. Zerwas $^{119}$ , D. Zhang $^{92}$ , F. Zhang $^{176}$ , G. Zhang $^{36a,ay}$ , H. Zhang $^{35b}$  
J. Zhang $^{6}$ , L. Zhang $^{51}$ , L. Zhang $^{36a}$ , M. Zhang $^{169}$ , P. Zhang $^{35b}$ , R. Zhang $^{23}$ , R. Zhang $^{36a,av}$  
X. Zhang $^{36b}$ , Y. Zhang $^{35a}$ , Z. Zhang $^{119}$ , X. Zhao $^{43}$ , Y. Zhao $^{36b,az}$ , Z. Zhao $^{36a}$ , A. Zhemchugov $^{68}$ ,  
B. Zhou $^{92}$ , C. Zhou $^{176}$ , L. Zhou $^{43}$ , M. Zhou $^{35a}$ , M. Zhou $^{150}$ , N. Zhou $^{35c}$ , C.G. Zhu $^{36b}$ , H. Zhu $^{35a}$  
J. Zhu $^{92}$ , Y. Zhu $^{36a}$ , X. Zhuang $^{35a}$ , K. Zhukov $^{98}$ , A. Zibell $^{177}$ , D. Zieminska $^{64}$ , N.I. Zimine $^{68}$  
C. Zimmermann $^{86}$ , S. Zimmermann $^{51}$ , Z. Zinonos $^{103}$ , M. Zinser $^{86}$ , M. Ziolkowski $^{143}$ ,  
L. Živković<sup>14</sup>, G. Zobernig<sup>176</sup>, A. Zoccoli<sup>22a,22b</sup>, R. Zou<sup>33</sup>, M. zur Nedden<sup>17</sup>, L. Zwalinski<sup>32</sup>.

$^{1}$  Department of Physics, University of Adelaide, Adelaide, Australia  
$^{2}$  Physics Department, SUNY Albany, Albany NY, U.S.A.  
$^{3}$  Department of Physics, University of Alberta, Edmonton AB, Canada  
$^{4}$  (a) Department of Physics, Ankara University, Ankara; (b) Istanbul Aydin University, Istanbul; (c) Division of Physics, TOBB University of Economics and Technology, Ankara, Turkey  
5 LAPP, CNRS/IN2P3 and Université Savoie Mont Blanc, Annecy-le-Vieux, France  
$^{6}$  High Energy Physics Division, Argonne National Laboratory, Argonne IL, U.S.A.  
$^{7}$  Department of Physics, University of Arizona, Tucson AZ, U.S.A.  
$^{8}$  Department of Physics, The University of Texas at Arlington, Arlington TX, U.S.A.  
9 Physics Department, National and Kapodistrian University of Athens, Athens, Greece  
$^{10}$  Physics Department, National Technical University of Athens, Zografou, Greece  
$^{11}$  Department of Physics, The University of Texas at Austin, Austin TX, U.S.A.  
$^{12}$  Institute of Physics, Azerbaijan Academy of Sciences, Baku, Azerbaijan  
$^{13}$  Institut de Física d'Altes Energies (IFAE), The Barcelona Institute of Science and Technology, Barcelona, Spain  
$^{14}$  Institute of Physics, University of Belgrade, Belgrade, Serbia  
$^{15}$  Department for Physics and Technology, University of Bergen, Bergen, Norway  
$^{16}$  Physics Division, Lawrence Berkeley National Laboratory and University of California, Berkeley CA, U.S.A.  
$^{17}$  Department of Physics, Humboldt University, Berlin, Germany

18 Albert Einstein Center for Fundamental Physics and Laboratory for High Energy Physics, University of Bern, Bern, Switzerland  
$^{19}$  School of Physics and Astronomy, University of Birmingham, Birmingham, U.K.  
$^{(a)}$  Department of Physics, Bogazici University, Istanbul;  ${}^{(b)}$  Department of Physics Engineering, Gaziantep University, Gaziantep;  ${}^{(d)}$  Istanbul Bilgi University, Faculty of Engineering and Natural Sciences, Istanbul;  ${}^{(e)}$  Bahcesehir University, Faculty of Engineering and Natural Sciences, Istanbul, Turkey  
21 Centro de Investigaciones, Universidad Antonio Narino, Bogota, Colombia  
$^{(a)}$  INFN Sezione di Bologna;  ${}^{(b)}$  Dipartimento di Fisica e Astronomia, Università di Bologna, Bologna, Italy  
23 Physikalisches Institut, University of Bonn, Bonn, Germany  
$^{24}$  Department of Physics, Boston University, Boston MA, U.S.A.  
$^{25}$  Department of Physics, Brandeis University, Waltham MA, U.S.A.  
$^{(a)}$  Universidade Federal do Rio De Janeiro COPPE/EE/IF, Rio de Janeiro;  ${}^{(b)}$  Electrical Circuits Department, Federal University of Juiz de Fora (UFJF), Juiz de Fora;  ${}^{(c)}$  Federal University of Sao Joao del Rei (UFSJ), Sao Joao del Rei;  ${}^{(d)}$  Instituto de Fisica, Universidade de Sao Paulo, Sao Paulo, Brazil  
$^{27}$  Physics Department, Brookhaven National Laboratory, Upton NY, U.S.A.  
$^{(a)}$  Transilvania University of Brasov, Brasov;  ${}^{(b)}$  Horia Hulubei National Institute of Physics and Nuclear Engineering, Bucharest;  ${}^{(c)}$  Department of Physics, Alexandru Ioan Cuza University of Iasi, Iasi;  ${}^{(d)}$  National Institute for Research and Development of Isotopic and Molecular Technologies, Physics Department, Cluj Napoca;  ${}^{(e)}$  University Politehnica Bucharest, Bucharest;  ${}^{(f)}$  West University in Timisoara, Timisoara, Romania  
29 Departamento de Física, Universidad de Buenos Aires, Buenos Aires, Argentina  
30 Cavendish Laboratory, University of Cambridge, Cambridge, U.K.  
$^{31}$  Department of Physics, Carleton University, Ottawa ON, Canada  
32 CERN, Geneva, Switzerland  
33 Enrico Fermi Institute, University of Chicago, Chicago IL, U.S.A.  
$^{(a)}$  Departamento de Física, Pontificia Universidad Católica de Chile, Santiago;  ${}^{(b)}$  Departamento de Física, Universidad Técnica Federico Santa María, Valparaíso, Chile  
$^{(a)}$  Institute of High Energy Physics, Chinese Academy of Sciences, Beijing;  ${}^{(b)}$  Department of Physics, Nanjing University, Jiangsu;  ${}^{(c)}$  Physics Department, Tsinghua University, Beijing 100084, China  
$^{(a)}$  Department of Modern Physics and State Key Laboratory of Particle Detection and Electronics, University of Science and Technology of China, Anhui; (b) School of Physics, Shandong University, Shandong; (c) Department of Physics and Astronomy, Key Laboratory for Particle Physics, Astrophysics and Cosmology, Ministry of Education; Shanghai Key Laboratory for Particle Physics and Cosmology, Shanghai Jiao Tong University, Shanghai (also at PKU-CHEP), China  
37 Université Clermont Auvergne, CNRS/IN2P3, LPC, Clermont-Ferrand, France  
38 Nevis Laboratory, Columbia University, Irvington NY, U.S.A.  
39 Niels Bohr Institute, University of Copenhagen, Kobenhavn, Denmark  
$^{(40)}$  INFN Gruppo Collegato di Cosenza, Laboratori Nazionali di Frascati;  ${}^{(b)}$  Dipartimento di Fisica, Università della Calabria, Rende, Italy  
$^{(a)}$  AGH University of Science and Technology, Faculty of Physics and Applied Computer Science, Krakow;  ${}^{(b)}$  Marian Smoluchowski Institute of Physics, Jagiellonian University, Krakow, Poland  
42 Institute of Nuclear Physics Polish Academy of Sciences, Krakow, Poland  
43 Physics Department, Southern Methodist University, Dallas TX, U.S.A.  
4 Physics Department, University of Texas at Dallas, Richardson TX, U.S.A.  
45 DESY, Hamburg and Zeuthen, Germany  
46 Lehrstuhl für Experimentelle Physik IV, Technische Universität Dortmund, Dortmund, Germany  
47 Institut für Kern- und Teilchenphysik, Technische Universität Dresden, Dresden, Germany  
$^{48}$  Department of Physics, Duke University, Durham NC, U.S.A.

49 SUPA - School of Physics and Astronomy, University of Edinburgh, Edinburgh, U.K.  
50 INFN e Laboratori Nazionali di Frascati, Frascati, Italy  
51 Fakultät für Mathematik und Physik, Albert-Ludwigs-Universität, Freiburg, Germany  
$^{52}$  Departement de Physique Nucleaire et Corpusculaire, Université de Genève, Geneva, Switzerland  
53 (a) INFN Sezione di Genova; (b) Dipartimento di Fisica, Università di Genova, Genova, Italy  
$^{(a)}$  E. Andronikashvili Institute of Physics, Iv. Javakhishvili Tbilisi State University, Tbilisi;  ${}^{(b)}$  High Energy Physics Institute, Tbilisi State University, Tbilisi, Georgia  
55 II Physikalisches Institut, Justus-Liebig-Universität Giessen, Giessen, Germany  
56 SUPA - School of Physics and Astronomy, University of Glasgow, Glasgow, U.K.  
57 II Physikalisches Institut, Georg-August-Universität, Göttingen, Germany  
$^{58}$  Laboratoire de Physique Subatomique et de Cosmologie, Université Grenoble-Alpes, CNRS/IN2P3, Grenoble, France  
$^{59}$  Laboratory for Particle Physics and Cosmology, Harvard University, Cambridge MA, U.S.A.  
$^{(a)}$  Kirchhoff-Institut für Physik, Ruprecht-Karls-Universität Heidelberg, Heidelberg;  ${}^{(b)}$  Physikalisches Institut, Ruprecht-Karls-Universität Heidelberg, Heidelberg, Germany  
$^{61}$  Faculty of Applied Information Science, Hiroshima Institute of Technology, Hiroshima, Japan  
$^{(a)}$  Department of Physics, The Chinese University of Hong Kong, Shatin, N.T., Hong Kong;  $^{(b)}$  Department of Physics, The University of Hong Kong, Hong Kong;  $^{(c)}$  Department of Physics and Institute for Advanced Study, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong, China  
$^{63}$  Department of Physics, National Tsing Hua University, Taiwan, Taiwan  
$^{64}$  Department of Physics, Indiana University, Bloomington IN, U.S.A.  
65 Institut für Astro- und Teilchenphysik, Leopold-Franzens-Universität, Innsbruck, Austria  
66 University of Iowa, Iowa City IA, U.S.A.  
$^{67}$  Department of Physics and Astronomy, Iowa State University, Ames IA, U.S.A.  
$^{68}$  Joint Institute for Nuclear Research, JINR Dubna, Dubna, Russia  
69 KEK, High Energy Accelerator Research Organization, Tsukuba, Japan  
70 Graduate School of Science, Kobe University, Kobe, Japan  
$^{71}$  Faculty of Science, Kyoto University, Kyoto, Japan  
72 Kyoto University of Education, Kyoto, Japan  
$^{73}$  Research Center for Advanced Particle Physics and Department of Physics, Kyushu University, Fukuoka, Japan  
$^{74}$  Instituto de Física La Plata, Universidad Nacional de La Plata and CONICET, La Plata, Argentina  
$^{75}$  Physics Department, Lancaster University, Lancaster, U.K.  
$^{76}$  (a) INFN Sezione di Lecce; (b) Dipartimento di Matematica e Fisica, Università del Salento, Lecce, Italy  
$^{77}$  Oliver Lodge Laboratory, University of Liverpool, Liverpool, U.K.  
$^{78}$  Department of Experimental Particle Physics, Jožef Stefan Institute and Department of Physics, University of Ljubljana, Ljubljana, Slovenia  
$^{79}$  School of Physics and Astronomy, Queen Mary University of London, London, U.K.  
$^{80}$  Department of Physics, Royal Holloway University of London, Surrey, U.K.  
$^{81}$  Department of Physics and Astronomy, University College London, London, U.K.  
82 Louisiana Tech University, Ruston LA, U.S.A.  
$^{83}$  Laboratoire de Physique Nucléaire et de Hautes Energies, UPMC and Université Paris-Diderot and CNRS/IN2P3, Paris, France  
84 Fysiska institutionen, Lund's universitet, Lund, Sweden  
85 Departamento de Fisica Teorica C-15, Universidad Autonoma de Madrid, Madrid, Spain  
86 Institut für Physik, Universität Mainz, Mainz, Germany  
87 School of Physics and Astronomy, University of Manchester, Manchester, U.K.  
88 CPPM, Aix-Marseille Université and CNRS/IN2P3, Marseille, France  
$^{89}$  Department of Physics, University of Massachusetts, Amherst MA, U.S.A.  
$^{90}$  Department of Physics, McGill University, Montreal QC, Canada

91 School of Physics, University of Melbourne, Victoria, Australia  
$^{92}$  Department of Physics, The University of Michigan, Ann Arbor MI, U.S.A.  
$^{93}$  Department of Physics and Astronomy, Michigan State University, East Lansing MI, U.S.A.  
$^{(a)}$  INFN Sezione di Milano;  ${}^{(b)}$  Dipartimento di Fisica, Università di Milano, Milano, Italy  
95 B.I. Stepanov Institute of Physics, National Academy of Sciences of Belarus, Minsk, Republic of Belarus  
$^{96}$  Research Institute for Nuclear Problems of Byelorussian State University, Minsk, Republic of Belarus  
97 Group of Particle Physics, University of Montreal, Montreal QC, Canada  
98 P.N. Lebedev Physical Institute of the Russian Academy of Sciences, Moscow, Russia  
99 Institute for Theoretical and Experimental Physics (ITEP), Moscow, Russia  
100 National Research Nuclear University MEPhI, Moscow, Russia  
101 D.V. Skobeltsyn Institute of Nuclear Physics, M.V. Lomonosov Moscow State University, Moscow, Russia  
102 Fakultät für Physik, Ludwig-Maximilians-Universität München, München, Germany  
103 Max-Planck-Institut für Physik (Werner-Heisenberg-Institut), München, Germany  
104 Nagasaki Institute of Applied Science, Nagasaki, Japan  
105 Graduate School of Science and Kobayashi-Maskawa Institute, Nagoya University, Nagoya, Japan  
106 (a) INFN Sezione di Napoli; (b) Dipartimento di Fisica, Università di Napoli, Napoli, Italy  
$^{107}$  Department of Physics and Astronomy, University of New Mexico, Albuquerque NM, U.S.A.  
$^{108}$  Institute for Mathematics, Astrophysics and Particle Physics, Radboud University Nijmegen/Nikhef, Nijmegen, Netherlands  
109 Nikhef National Institute for Subatomic Physics and University of Amsterdam, Amsterdam, Netherlands  
$^{110}$  Department of Physics, Northern Illinois University, DeKalb IL, U.S.A.  
111 Budker Institute of Nuclear Physics, SB RAS, Novosibirsk, Russia  
$^{112}$  Department of Physics, New York University, New York NY, U.S.A.  
113 Ohio State University, Columbus OH, U.S.A.  
$^{114}$  Faculty of Science, Okayama University, Okayama, Japan  
115 Homer L. Dodge Department of Physics and Astronomy, University of Oklahoma, Norman OK, U.S.A.  
$^{116}$  Department of Physics, Oklahoma State University, Stillwater OK, U.S.A.  
117 Palacky University, RCPTM, Olomouc, Czech Republic  
118 Center for High Energy Physics, University of Oregon, Eugene OR, U.S.A.  
119 LAL, Univ. Paris-Sud, CNRS/IN2P3, Université Paris-Saclay, Orsay, France  
120 Graduate School of Science, Osaka University, Osaka, Japan  
$^{121}$  Department of Physics, University of Oslo, Oslo, Norway  
$^{122}$  Department of Physics, Oxford University, Oxford, U.K.  
123 (a) INFN Sezione di Pavia; (b) Dipartimento di Fisica, Università di Pavia, Pavia, Italy  
$^{124}$  Department of Physics, University of Pennsylvania, Philadelphia PA, U.S.A.  
125 National Research Centre "Kurchatov Institute" B.P.Konstantinov Petersburg Nuclear Physics Institute, St. Petersburg, Russia  
$^{(a)}$  INFN Sezione di Pisa;  ${}^{(b)}$  Dipartimento di Fisica E. Fermi, Università di Pisa, Pisa, Italy  
$^{127}$  Department of Physics and Astronomy, University of Pittsburgh, Pittsburgh PA, U.S.A.  
$^{(a)}$  Laboratório de Instrumentação e Física Experimental de Partículas - LIP, Lisboa;  $^{(b)}$  Faculdade de Ciências, Universidade de Lisboa, Lisboa;  $^{(c)}$  Department of Physics, University of Coimbra, Coimbra;  $^{(d)}$  Centro de Física Nuclear da Universidade de Lisboa, Lisboa;  $^{(e)}$  Departamento de Física, Universidade do Minho, Braga;  $^{(f)}$  Departamento de Física Teorica y del Cosmos and CAFPE, Universidad de Granada, Granada;  $^{(g)}$  Dep Física and CEFITEC of Faculdade de Ciências e Tecnologia, Universidade Nova de Lisboa, Caparica, Portugal  
129 Institute of Physics, Academy of Sciences of the Czech Republic, Praha, Czech Republic  
130Czech Technical University in Prague, Praha, Czech Republic

131 Charles University, Faculty of Mathematics and Physics, Prague, Czech Republic  
132 State Research Center Institute for High Energy Physics (Protvino), NRC KI, Russia  
133 Particle Physics Department, Rutherford Appleton Laboratory, Didcot, U.K.  
134 (a) INFN Sezione di Roma; (b) Dipartimento di Fisica, Sapienza Università di Roma, Roma, Italy  
$^{(a)}$  INFN Sezione di Roma Tor Vergata;  ${}^{(b)}$  Dipartimento di Fisica, Università di Roma Tor Vergata, Roma, Italy  
$^{(a)}$  INFN Sezione di Roma Tre;  ${}^{(b)}$  Dipartimento di Matematica e Fisica, Università Roma Tre, Roma, Italy  
$^{(a)}$  Faculté des Sciences Ain Chock, Réseau Universitaire de Physique des Hautes Energies - Université Hassan II, Casablanca;  $^{(b)}$  Centre National de l'Energie des Sciences Techniques Nucleaires, Rabat;  $^{(c)}$  Faculté des Sciences Semlalia, Université Cadi Ayyad, LPHEA-Marrakech;  
$^{(d)}$  Faculté des Sciences, Université Mohamed Premier and LPTPM, Oujda;  ${}^{(e)}$  Faculté des sciences, Université Mohammed V, Rabat, Morocco  
138 DSM/IRFU (Institut de Recherches sur les Lois Fondamentales de l'Univers), CEA Saclay (Commissariat à l'Energie Atomique et aux Energies Alternatives), Gif-sur-Yvette, France  
139 Santa Cruz Institute for Particle Physics, University of California Santa Cruz, Santa Cruz CA, U.S.A.  
$^{140}$  Department of Physics, University of Washington, Seattle WA, U.S.A.  
$^{141}$  Department of Physics and Astronomy, University of Sheffield, Sheffield, U.K.  
$^{142}$  Department of Physics, Shinshu University, Nagano, Japan  
$^{143}$  Department Physik, Universität Siegen, Siegen, Germany  
$^{144}$  Department of Physics, Simon Fraser University, Burnaby BC, Canada  
145 SLAC National Accelerator Laboratory, Stanford CA, U.S.A.  
$^{(146)}$  (a) Faculty of Mathematics, Physics & Informatics, Comenius University, Bratislava; (b) Department of Subnuclear Physics, Institute of Experimental Physics of the Slovak Academy of Sciences, Kosice, Slovak Republic  
$^{(a)}$  Department of Physics, University of Cape Town, Cape Town;  ${}^{(b)}$  Department of Physics, University of Johannesburg, Johannesburg;  ${}^{(c)}$  School of Physics, University of the Witwatersrand, Johannesburg, South Africa  
$^{(a)}$  Department of Physics, Stockholm University;  ${}^{(b)}$  The Oskar Klein Centre, Stockholm, Sweden  
$^{149}$  Physics Department, Royal Institute of Technology, Stockholm, Sweden  
150 Departments of Physics & Astronomy and Chemistry, Stony Brook University, Stony Brook NY, U.S.A.  
$^{151}$  Department of Physics and Astronomy, University of Sussex, Brighton, U.K.  
152 School of Physics, University of Sydney, Sydney, Australia  
153 Institute of Physics, Academia Sinica, Taipei, Taiwan  
$^{154}$  Department of Physics, Technion: Israel Institute of Technology, Haifa, Israel  
155 Raymond and Beverly Sackler School of Physics and Astronomy, Tel Aviv University, Tel Aviv, Israel  
$^{156}$  Department of Physics, Aristotle University of Thessaloniki, Thessaloniki, Greece  
157 International Center for Elementary Particle Physics and Department of Physics, The University of Tokyo, Tokyo, Japan  
158 Graduate School of Science and Technology, Tokyo Metropolitan University, Tokyo, Japan  
$^{159}$  Department of Physics, Tokyo Institute of Technology, Tokyo, Japan  
160 Tomsk State University, Tomsk, Russia  
$^{161}$  Department of Physics, University of Toronto, Toronto ON, Canada  
162 (a) INFN-TIFPA; (b) University of Trento, Trento, Italy  
$^{(a)}$  TRIUMF, Vancouver BC;  ${}^{(b)}$  Department of Physics and Astronomy, York University, Toronto ON, Canada  
$^{164}$  Faculty of Pure and Applied Sciences, and Center for Integrated Research in Fundamental Science and Engineering, University of Tsukuba, Tsukuba, Japan  
$^{165}$  Department of Physics and Astronomy, Tufts University, Medford MA, U.S.A.

$^{166}$  Department of Physics and Astronomy, University of California Irvine, Irvine CA, U.S.A.

167 (a) INFN Gruppo Collegato di Udine, Sezione di Trieste, Udine; (b) ICTP, Trieste; (c) Dipartimento di Chimica, Fisica e Ambiente, Università di Udine, Udine, Italy

$^{168}$  Department of Physics and Astronomy, University of Uppsala, Uppsala, Sweden

$^{169}$  Department of Physics, University of Illinois, Urbana IL, U.S.A.

170 Instituto de Fisica Corpuscular (IFIC), Centro Mixto Universidad de Valencia - CSIC, Spain

$^{171}$  Department of Physics, University of British Columbia, Vancouver BC, Canada

$^{172}$  Department of Physics and Astronomy, University of Victoria, Victoria BC, Canada

$^{173}$  Department of Physics, University of Warwick, Coventry, U.K.

174 Waseda University, Tokyo, Japan

$^{175}$  Department of Particle Physics, The Weizmann Institute of Science, Rehovot, Israel

$^{176}$  Department of Physics, University of Wisconsin, Madison WI, U.S.A.

177 Fakultät für Physik und Astronomie, Julius-Maximilians-Universität, Würzburg, Germany

178 Fakultät für Mathematik und Naturwissenschaften, Fachgruppe Physik, Bergische Universität Wuppertal, Wuppertal, Germany

$^{179}$  Department of Physics, Yale University, New Haven CT, U.S.A.

180 Yerevan Physics Institute, Yerevan, Armenia

181 Centre de Calcul de l'Institut National de Physique Nucléaire et de Physique des Particules (IN2P3), Villeurbanne, France

$^{182}$  Academia Sinica Grid Computing, Institute of Physics, Academia Sinica, Taipei, Taiwan

${}^{a}$  Also at Department of Physics,King’s College London,London,U.K.  
${}^{b}$  Also at Institute of Physics,Azerbaijan Academy of Sciences,Baku,Azerbaijan  
c Also at Novosibirsk State University, Novosibirsk, Russia  
${}^{d}$  Also at TRIUMF,Vancouver BC,Canada  
e Also at Department of Physics & Astronomy, University of Louisville, Louisville, KY, U.S.A.  
${}^{f}$  Also at Physics Department,An-Najah National University,Nablus,Palestine  
${}^{g}$  Also at Department of Physics,California State University,Fresno CA,U.S.A.  
${}^{h}$  Also at Department of Physics,University of Fribourg,Fribourg,Switzerland  
<sup>1</sup> Also at II Physikalisches Institut, Georg-August-Universität, Göttingen, Germany  
${}^{j}$  Also at Departament de Física de la Universitat Autonoma de Barcelona,Barcelona,Spain  
${}^{k}$  Also at Departamento de Física e Astronomía, Faculdade de Ciencias, Universidade do Porto, Portugal  
<sup>1</sup> Also at Tomsk State University, Tomsk, Russia  
Also at The Collaborative Innovation Center of Quantum Matter (CICQM), Beijing, China  
${}^{n}$  Also at Universita di Napoli Parthenope,Napoli,Italy  
${}^{o}$  Also at Institute of Particle Physics (IPP),Canada  
${}^{p}$  Also at Horia Hulubei National Institute of Physics and Nuclear Engineering, Bucharest, Romania  
$^{q}$  Also at Department of Physics, St. Petersburg State Polytechnical University, St. Petersburg, Russia  
Also at Borough of Manhattan Community College, City University of New York, New York City, U.S.A.  
${}^{s}$  Also at Department of Financial and Management Engineering,University of the Aegean,Chios, Greece  
<sup>t</sup> Also at Centre for High Performance Computing, CSIR Campus, Rosebank, Cape Town, South Africa  
${}^{u}$  Also at Louisiana Tech University,Ruston LA,U.S.A.  
${}^{v}$  Also at Institucio Catalana de Recerca i Estudis Avancats,ICREA,Barcelona,Spain  
${}^{w}$  Also at Graduate School of Science,Osaka University,Osaka,Japan  
${}^{x}$  Also at Fakultät für Mathematik und Physik,Albert-Ludwigs-Universität,Freiburg,Germany  
<sup>9</sup> Also at Institute for Mathematics, Astrophysics and Particle Physics, Radboud University Nijmegen/Nikhef, Nijmegen, Netherlands

$^{z}$  Also at Department of Physics, The University of Texas at Austin, Austin TX, U.S.A.  
${}^{a\mathrm{a}}$  Also at Institute of Theoretical Physics,IIia State University,Tbilisi,Georgia  
${}^{ab}$  Also at CERN,Geneva,Switzerland  
${}^{ac}$  Also at Georgian Technical University (GTU),Tbilisi,Georgia  
$^{a,d}$  Also at Ochadai Academic Production, Ochanomizu University, Tokyo, Japan  
${}^{ae}$  Also at Manhattan College,New York NY,U.S.A.  
<sup>a</sup> Also at Departamento de Física, Pontificia Universidad Católica de Chile, Santiago, Chile  
$^{a g}$  Also at Department of Physics, The University of Michigan, Ann Arbor MI, U.S.A.  
${}^{a\mathrm{h}}$  Also at The City College of New York,New York NY,U.S.A.  
<sup>a</sup> Also at School of Physics, Shandong University, Shandong, China  
$^{a j}$  Also at Departamento de Física Teorica y del Cosmos and CAFPE, Universidad de Granada, Granada, Portugal  
${}^{ak}$  Also at Department of Physics,California State University,Sacramento CA,U.S.A.  
<sup>a</sup> Also at Moscow Institute of Physics and Technology State University, Dolgoprudny, Russia  
<sup>am</sup> Also at Departement de Physique Nucleaire et Corpusculaire, Université de Genève, Geneva, Switzerland  
<sup>a</sup> Also at Institut de Física d'Altes Energies (IFAE), The Barcelona Institute of Science and Technology, Barcelona, Spain  
${}^{a0}$  Also at School of Physics, Sun Yat-sen University, Guangzhou, China  
<sup>a p</sup> Also at Institute for Nuclear Research and Nuclear Energy (INRNE) of the Bulgarian Academy of Sciences, Sofia, Bulgaria  
$^{aq}$  Also at Faculty of Physics, M.V.Lomonosov Moscow State University, Moscow, Russia  
$^{a r}$  Also at National Research Nuclear University MEPhI, Moscow, Russia  
<sup>a</sup> Also at Department of Physics, Stanford University, Stanford CA, U.S.A.  
$^{at}$  Also at Institute for Particle and Nuclear Physics, Wigner Research Centre for Physics, Budapest, Hungary  
<sup>a u</sup> Also at Giresun University, Faculty of Engineering, Turkey  
<sup>a</sup> Also at CPPM, Aix-Marseille Université and CNRS/IN2P3, Marseille, France  
${}^{aw}$  Also at Department of Physics, Nanjing University, Jiangsu, China  
${}^{ax}$  Also at University of Malaya,Department of Physics,Kuala Lumpur,Malaysia  
<sup>a</sup> Also at Institute of Physics, Academia Sinica, Taipei, Taiwan  
$^{a z}$  Also at LAL, Univ. Paris-Sud, CNRS/IN2P3, Université Paris-Saclay, Orsay, France  
* Deceased