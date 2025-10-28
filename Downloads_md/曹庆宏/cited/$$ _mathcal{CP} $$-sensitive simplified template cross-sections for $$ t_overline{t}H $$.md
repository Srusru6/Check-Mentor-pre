# $\mathcal{CP}$ -sensitive simplified template cross-sections for  $t\bar{t}H$

Henning Bahl<sup>1</sup>,<sup>a</sup> Alberto Carnelli<sup>1</sup>,<sup>b</sup> Frédéric Déliot<sup>1</sup>,<sup>b</sup> Elina Fuchs<sup>1</sup>,<sup>c,d</sup> Anastasia Kotsokechagia<sup>1</sup>,<sup>b</sup> Tanguy Lucas Marsault<sup>1</sup>,<sup>b</sup> Marco Menen<sup>1</sup>,<sup>c,d</sup> Laurent Schoeffel<sup>1</sup> and Matthias Saimpert<sup>1</sup>

$^{a}$ Institut für Theoretische Physik, Universität Heidelberg, Philosophenweg 16, 61920 Heidelberg, Germany  
bUniversité Paris-Saclay, CEA, Département de Physique des Particules, 91191, Gif-sur-Yvette, France  
$^{c}$ Institut für Theoretische Physik, Leibniz Universität Hannover, Appelstraße 2, 30167 Hannover, Germany  
$^{d}$ Physikalisch-Technische Bundesanstalt, Bundesallee 100, 38116 Braunschweig, Germany

E-mail: bahl@thphys.uni-heidelberg.de, alberto.carnelli@cea.fr, frederic.deliot@cern.ch, elina.fuchs@cern.ch, anastasia.kotsokechagia@cern.ch, marsault.tanguy@cea.fr, marco.menen@itp.uni-hannover.de, laurent.schoeffel@cea.fr, matthias.saimpert@cea.fr

ABSTRACT: The  $\mathcal{CP}$  structure of the Higgs boson is a fundamental property which has not yet been constrained with high precision.  $\mathcal{CP}$  violation in the Yukawa coupling between the Higgs boson and top quark pair can be probed directly at the Large Hadron Collider by measuring top-quark-associated Higgs production. Multivariate analysis techniques commonly developed so far by the experiments are designed for a specific signal model and, therefore, complicate reinterpretations and statistical combinations. With this motivation in mind, we propose a  $\mathcal{CP}$ -sensitive extension of the simplified template cross-section (STXS) framework. Considering multiple Higgs decay channels, we perform an in-depth comparison of  $\mathcal{CP}$ -sensitive observables and combinations thereof. Our resulting proposal is to extend the existing binning in the transverse momentum of the Higgs boson  $p_{T,H}$  by either the pseudorapidity difference of the two top-quarks  $\Delta \eta_{t\bar{t}}$ , or a variable that is based on the top quark momenta, namely  $b_{2}$  or the Collins-Soper angle  $|\cos \theta^{*}|$ . We demonstrate that this variable selection provides close to optimal sensitivity to the  $\mathcal{CP}$  mixture in the top Yukawa coupling for an integrated luminosity of  $300\mathrm{fb^{-1}}$ , by comparing it to the results of a multivariate analysis. Our results also suggest a benefit of the two-dimensional STXS extension at  $3000\mathrm{fb^{-1}}$ .

KEYWORDS: CP Violation, Higgs Properties

ARXIV EPRINT: 2406.03950

# Contents

# 1 Introduction 1

# 2 CP-sensitive observables in  $ttH$  events 4

2.1 Event generation 4  
2.2 Observable definition 5  
2.3 Distributions at the parton-level 7

# 3 Evaluation of the observable performance 7

3.1 Detector effects and selection efficiency 7  
3.2 Significance computation 11

# 4 Results 13

4.1 Results with default binning 13  
4.2 Final results with optimised binning 14  
4.3 Comparison to a multivariate analysis 16  
4.4 Expected exclusion limits 19

# 5 Extending the STXS framework 20

5.1 Further background considerations 21  
5.2 Proposal for  $t\bar{t} H$  STXS extension 24

# 6 Conclusion 26

# A Supplementary parton-level distributions for  $t\bar{t} H$  27

A.1 Higgs boson rest frame 27  
A.2  $t\bar{t}$  rest frame 29  
A.3  $t\bar{t} H$  rest frame 30  
A.4 Impact of the  $\eta$  cut 31

# B Full two-dimensional significance tables 32

# 1 Introduction

The Standard Model (SM) of particle physics does not contain sufficient  $\mathcal{CP}$  violation to explain the observed baryon asymmetry of the Universe (BAU) [1, 2]. Therefore, new sources of  $\mathcal{CP}$  violation are needed and the search for corresponding  $\mathcal{CP}$ -violating interactions is an important target for searches beyond the SM (BSM) at the LHC.

The investigation of the Higgs sector is especially important in this context. First, the  $\mathcal{CP}$  structure of the Higgs couplings is still comparably unexplored. Second, the BAU can be linked to the Higgs sector via the mechanism of electroweak baryogenesis [3] (for reviews, see e.g. [4-8]). While the  $\mathcal{CP}$  structure of the Higgs couplings to massive gauge bosons is

already relatively tightly constrained [9-18], the test of the  $\mathcal{CP}$  structure of the Higgs-fermion interactions at the LHC only started recently [16, 19-25]. Moreover, most BSM theories predict a larger amount of  $\mathcal{CP}$  violation in the Yukawa couplings than in the interactions with massive vector bosons, since the latter are loop-suppressed.

The top-Yukawa coupling has a special relevance because of its large size. It can be parameterized in the following way in the Higgs Characterization Model [26],

$$
\mathcal {L} _ {\mathrm {t o p - Y u k}} = \frac {y _ {t} ^ {\mathrm {S M}} g _ {t}}{\sqrt {2}} \bar {t} (\cos \alpha_ {t} + i \gamma_ {5} \sin \alpha_ {t}) t H, (1. 1)
$$

where  $y_{t}^{\mathrm{SM}}$  is the SM top-Yukawa coupling,  $g_{t}$  is the (real) modifier of the strength of the top-Yukawa coupling, and  $\alpha_{t}$  is the  $\mathcal{CP}$ -mixing angle. The SM corresponds to  $g_{t} = 1$ ,  $\alpha_{t} = 0$ . Equivalently, this interaction can be parameterized in terms of a  $\mathcal{CP}$ -even and a  $\mathcal{CP}$ -odd coupling,  $c_{t} \equiv g_{t} \cos \alpha_{t}$  and  $\tilde{c}_{t} \equiv g_{t} \sin \alpha_{t}$ , respectively.

In an EFT framework (e.g. the SM effective field theory), this gauge-invariant modification is generated by the operator  $(\Phi^{\dagger}\Phi)Q_{L}u_{R}\tilde{\Phi}$  (where  $\Phi$  is the Higgs doublet,  $Q_{L}$  is the left-handed quark doublet, and  $u_{R}$  is the right-handed up-type quark singlet) and the coefficients  $y_{t}^{\mathrm{SM}}g_{t}\cos \alpha_{t}$  and  $y_{t}^{\mathrm{SM}}g_{t}\sin \alpha_{t}$  in eq. (1.1) can be related to the real and imaginary parts of the corresponding Wilson coefficient (see e.g. [27, 28]).<sup>1</sup>

This general coupling structure can be probed at the LHC but also via measurements of electric dipole moments (EDMs) of particles like the electron or the neutron, for which so far only upper bounds exist [29, 30]. If one assumes that the first-generation Yukawa couplings do not deviate from their SM predictions, these EDM bounds put strong constraints on the  $\mathcal{CP}$ -odd part of the top-Yukawa coupling, constraining  $\tilde{c}_t \lesssim 10^{-3}$  at the  $90\%$  CL [27, 31, 32]; this translates into  $\alpha_t \lesssim 0.06^\circ$  for  $g_t = 1$ . Since the first-generation Yukawa couplings are only very weakly constrained [33-43], this assumption, however, does not necessarily hold, resulting in relaxed EDM bounds. Therefore, it is crucial to measure the  $\mathcal{CP}$  properties of the top-Yukawa coupling directly, i.e. without a strong dependence on the other Yukawa couplings. This can be achieved at the LHC where the measurement of distinct production and decay channels provides access to specific couplings, whereas the measured value of an EDM results from the sum over all  $\mathcal{CP}$ -violating contributions.

Bounds on the  $\mathcal{CP}$  structure of the top-Yukawa interaction at the LHC can be derived from rate measurements [27, 32, 44-58]. In this case, the most stringent constraints arise from Higgs production via gluon fusion when the Higgs boson decays to two photons (constraining  $\alpha_{t} \lesssim 28^{\circ}$  at the  $95\%$  CL assuming that  $g_{t} = 1$  [58]). These constraints are, however, highly model-dependent since other particles also contribute to the respective loop diagrams. A more direct probe is top-associated Higgs production (consisting of the three sub-channels  $t\bar{t}H$ ,  $tHq$ , and  $tWH$ ). Top-associated Higgs production can be used to constrain the  $\mathcal{CP}$  properties of the top-Yukawa coupling via rate measurements (constraining  $\alpha_{t} \lesssim 72^{\circ}$  at the  $95\%$  CL [56] assuming that  $g_{t} = 1$ ), kinematic distributions, and  $\mathcal{CP}$ -odd observables. While rate measurements are again model-dependent (e.g., the Higgs-gluon coupling contributes to

top-associated Higgs production at next-to-leading order),  $\mathcal{CP}$ -odd observables in principle offer a way to unambiguously probe  $\mathcal{CP}$ . For top-associated Higgs production, they are, however, very difficult to measure due to the necessity of reconstructing the polarization of the top quark [59-65]. Specifically, in hadronic decays, it requires to differentiate between up- and down-type quarks. While this might change during the high-luminosity phase of the LHC, at the moment they certainly only provide little sensitivity for testing the  $\mathcal{CP}$  character of the top-Yukawa interaction. On the other hand, kinematic distributions of  $\mathcal{CP}$ -even observables offer a good compromise between the  $\mathcal{CP}$ -odd observables and rate measurements. After the observation of top-associated Higgs production in 2018 [66, 67], the additional data collected and to be collected at the LHC allows now for differential measurements even for this comparably rare process, making it a promising way to probe  $\mathcal{CP}$  during over the next few years.

Kinematic information can be best exploited using multivariate analysis techniques (see e.g. [63, 68-70]) or the matrix element method (see e.g. [71-75]). These methods have been used by the experimental collaborations to put constraints on  $\alpha_{t}$ , constraining at the  $95\%$  CL  $\alpha_{t} \lesssim 43^{\circ}$  (ATLAS using the  $H \to \gamma \gamma$  channel [20]; in addition, see also the currently less sensitive  $H \to b\bar{b}$  channel in [25]) and  $\alpha_{t} \lesssim 45^{\circ}$  (CMS using  $H \to \gamma \gamma, 4\ell, \tau\tau$  [16, 19, 22, 23])² assuming that  $g_{t} = 1$ . For an overview of future prospects, see [76]. These techniques are typically tailored to specific Higgs decay channels, detector environments, and background assumptions. Moreover, they are designed for specific signal models and intrinsically depend on the assumptions about the other couplings involved. As a consequence, the combination of different decay channels (see e.g. [22, 23]) and across experiments is non-trivial. The usage of such approaches also makes the reinterpretation of the analyses difficult, as it usually requires the signal efficiency as a function of the final discriminating algorithm output score. To mitigate such issues — before providing likelihoods encoding all relevant dependencies becomes feasible —, the simplified template cross-section (STXS) framework [77-80] has been established. This study, focusing on  $\mathcal{CP}$ -sensitive but  $\mathcal{CP}$ -even observables, aims to enhance the  $\mathcal{CP}$  sensitivity of this framework for  $t\bar{t}H$  production by taking the interplay of two variables into account. As a complementary example, also for Drell-Yan production, double-and triple-differential distributions have recently been found to yield a higher sensitivity to SMEFT operators compared to a finer binning in a single variable [81].

We start in section 2 with a comparison of the kinematic shapes of various  $\mathcal{CP}$ -sensitive observables evaluated in different reference frames building upon existing proposals in the literature [47, 49, 51, 52, 63-65, 69, 71, 73, 74, 82-87]. In section 3, we evaluate how these observables could be impacted by detector effects using a simplified model and describe how their performance is evaluated. In section 4, we perform a sensitivity study based on one- and two-dimensional distributions, optimize the binning of the most sensitive observables assuming  $300\mathrm{fb}^{-1}$  of data (which should correspond to the available LHC dataset by the end of 2025), and compare the outcome to a multivariate analysis based on a boosted decision tree (BDT). Based on these findings, we make a proposal for a  $\mathcal{CP}$ -sensitive extension of the latest version of the STXS framework (v1.2) in section 5. It also includes a qualitative discussion about the Higgs and non-Higgs backgrounds and a comparison between the expected  $\mathcal{CP}$  sensitivity of the STXS framework v1.2 and our proposed extension. We present conclusions in section 6.

# 2  $\mathcal{CP}$ -sensitive observables in  $t\bar{t}H$  events

The  $t\bar{t}H$  production process possesses many final state particles and therefore also numerous kinematic observables. In experimental analyses targeting  $\mathcal{CP}$  violation in the top-Yukawa coupling, a number of such observables have been used already (see e.g. [25]). These are, however, only optimized for a specific channel and selection. In this work, we aim to find observables that are optimal to use in the context of an STXS extension and should therefore be independent of the analysis details.

We describe the generation of the  $t\bar{t}H$  events used in this study in section 2.1. We then introduce an extended number of kinematic observables in various rest frames in section 2.2. The parton level distributions of these observables are shown in section 2.3.

# 2.1 Event generation

We generate parton-level events for the  $pp \rightarrow t\bar{t}H$  process at a center-of-mass energy of  $\sqrt{s} = 13$  TeV using the event generator MadGraph5_aMC@NLO [88] (version 3.3.2) and the NNPDF23_lo_as_0130_qed PDF set [89]. The renormalization and factorization scales are set to  $1/2 \cdot (2m_t + m_H)$ . Events are generated using the "Higgs Characterization" (HC) UFO model [26] for  $g_t = 1$  and two different values for the  $\mathcal{CP}$  phase  $\alpha_t$ :  $0^\circ$  (pure scalar, corresponding to the SM) and  $90^\circ$  (pure  $\mathcal{CP}$ -odd case). All simulated samples were generated at leading order (LO) and include one million events each.

In principle, the HC model allows generating events at next-to-leading order (NLO) in QCD. Within this model, if the top-quark mass is treated as finite (as needed for  $ttH$  production), it, however, does not allow considering a non-zero effective Higgs-gluon interaction (generated by BSM particles), which would affect  $ttH$  production at NLO in  $\alpha_{s}$ . As discussed in section 1, for a zero BSM Higgs-gluon coupling, Higgs production via gluon fusion allows setting much stronger (indirect) constraints on the  $\mathcal{CP}$  character of the top-Yukawa coupling with respect to top-associated Higgs production. Since we are interested in a scenario in which  $ttH$  provides the leading constraints on the  $\mathcal{CP}$  nature of the top-Yukawa coupling and this scenario cannot be generated with the HC model at NLO, we, therefore, generate all events at LO (see also the discussion in [56]). Moreover, as discussed in [56, 84], the NLO correction to the  $ttH$  total cross-section depends only very weakly on the  $\mathcal{CP}$  character of the top-Yukawa coupling. Similarly, this observation still holds for kinematic distributions. Hence, a simple scaling factor of 1.14 [84] is used as NLO correction in the following.

Since only  $\mathcal{CP}$ -even observables are considered in this study, signal yields for mixed- $\mathcal{CP}$  scenarios are computed by combining the yields from the SM and the pure  $\mathcal{CP}$ -odd samples. The following formula is used:

$$
N \left(g _ {t}, \alpha_ {t}\right) = g _ {t} ^ {2} \left[ N _ {\mathrm {S M}} \cos^ {2} \alpha_ {t} + N _ {\mathrm {o d d}} \sin^ {2} \alpha_ {t} \right], \tag {2.1}
$$

where  $N(g_{t},\alpha_{t})$  is the expected yield for the signal corresponding to the parameters  $(g_{t},\alpha_{t})$ , with  $N_{\mathrm{SM}} = N(1,0)$  and  $N_{\mathrm{odd}} = N(1,90^{\circ})$ . The yields for  $\alpha_{t} = 35^{\circ}$  and  $\alpha_{t} = 45^{\circ}$  obtained from eq. (2.1) were validated against the yields obtained from dedicated samples generated with these  $\alpha_{t}$  values and an agreement within  $1\%$  was obtained.

The SM background processes discussed in section 5.1, i.e.  $tt\bar{\gamma}\gamma$ ,  $t\bar{t}W$  and  $t\bar{t}bb$ , were generated using a similar setup. These samples are used at the parton level only and without any additional selection nor corrections applied. We checked that showering the events with Pythia8 [90] has only a small impact on the resulting distributions shown in section 5.1. Half a million events are generated at LO for each process using the NNPDF23_lo_as_0130_qed PDF set [89] and the renormalization and factorization scales were set to the sum of the transverse mass of all the final state particles divided by a factor of two (corresponding to dynamical_scale_choice = 3 in MadGraph5_aMC@NLO).

# 2.2 Observable definition

We consider a right-handed coordinate system with its origin at the nominal interaction point (IP). In the laboratory frame, see figure 1, top-left, the  $z$ -axis is defined along the beam axis, and  $\pmb{n}$  denotes the associated unit vector. The  $x$ -axis points from the IP to the centre of the LHC ring, and the  $y$ -axis points upwards. Cylindrical coordinates  $(r,\phi)$  are used in the transverse  $(x,y)$  plane,  $\phi$  being the azimuthal angle around the  $z$ -axis. The pseudorapidity is defined in terms of the polar angle  $\theta$  as  $\eta = -\ln \tan (\theta /2)$ . Four-momenta are denoted by  $p$  and their corresponding three-momenta are denoted by  $\pmb{p}$ . The magnitudes of the components of the three-momenta in the transverse plane and along the  $x$  and  $z$ -axes are labeled as  $p_{\mathrm{T}}$ ,  $p^x$  and  $p^z$ , respectively. The subscripts  $t$ ,  $\bar{t}$ ,  $H$ ,  $p_1$  and  $p_2$  in the labels indicate to which particle they refer to, i.e. top quark  $(t)$ , anti-top quark  $(\bar{t})$ , Higgs boson  $(H)$  or the colliding protons  $(p_1,p_2)$ . We consider four possible reference frames for the computation of the observables:

- the laboratory frame (lab frame),  
- the  $\bar{t\bar{t}}$  rest frame, where  $\pmb{p}_{t} + \pmb{p}_{\bar{t}} = \mathbf{0}$  ( $\bar{t\bar{t}}$  frame),  
the  $H$  rest frame, where  $\pmb{p}_H = \mathbf{0}$  ( $H$  frame),  
- the  $t\bar{t}H$  rest frame, where  $\pmb{p}_t + \pmb{p}_{\bar{t}} + \pmb{p}_H = \mathbf{0}$  ( $t\bar{t}H$  frame).

To unambiguously define these frames, we start in the lab frame. To move to the frame  $X$  (defined by  $\pmb{p}_X = \mathbf{0}$ , where  $X = H$ ,  $t\bar{t}$ ,  $t\bar{t}H$ ), we first apply a rotation around the  $z$ -axis such that  $\pmb{p}_{T,X}$  is parallel to the  $x$ -axis, see figure 1, left. Then, a boost along the transverse direction is performed such that  $\pmb{p}_{T,X} = 0$ . Finally, a boost along the longitudinal direction ensures that  $\pmb{p}_X = 0$ . These last two steps are illustrated in figure 1, right. In the resulting coordinate system, the proton momenta lie in the  $x - z$  plane and both form the same angle with the  $z$ -axis.

The  $\mathcal{CP}$ -sensitive observables considered in this work are summarised in table 1. All of these are  $\mathcal{CP}$ -even observables. We analyse them in all applicable rest frames listed above. Any new observable candidate for the extended STXS framework should be defined for all  $t\bar{t}H$  events, regardless of the Higgs boson and top quark pair decay mode. Therefore, in the following, we consider that the Higgs boson, the top quark and anti-top quark are reconstructed experimentally such that their momenta are accessible. In practice, we compute the observables listed in table 1 at the parton level and apply specific acceptance and smearing factors to mimic detector effects, as described in section 3.1. Note that, given the considered

![](images/f5892f9c050b38be5fb335793e65339880867aefdcba74c4cda7f0aea6afe901.jpg)  
Figure 1. Sketch illustrating the rest frame definition adopted in this work. The rest frame  $X$  is shown here, defined by  $\pmb{p}_X = \mathbf{0}$ , where  $X = H$ ,  $t\bar{t}$ ,  $t\bar{t}H$ .

Table 1. Overview of the  $\mathcal{CP}$ -sensitive observables considered in this work, including their definition, the rest frames in which they are analysed, and references where they are discussed in more detail.  

<table><tr><td>observable</td><td>definition</td><td>frame</td><td>reference</td></tr><tr><td>pT,H</td><td>-</td><td>lab, tbar,tbarH</td><td>-</td></tr><tr><td>Δηtbar</td><td>|ηt - ηbar|</td><td>lab, H, tbarH</td><td>-</td></tr><tr><td>Δφtbar</td><td>|φt - φbar|</td><td>lab, H, tbarH</td><td>-</td></tr><tr><td>mtbar</td><td>(pt + pbar)2</td><td>frame-invariant</td><td>-</td></tr><tr><td>mtbarH</td><td>(pt + pbar + pH)2</td><td>frame-invariant</td><td>-</td></tr><tr><td>|cos θ*|</td><td>|pt·n| / |pt| · |n|</td><td>ttbar</td><td>[74, 91]</td></tr><tr><td>b1</td><td>( pt × n) · ( pt × n) / PT,tpT,bar</td><td>all</td><td>[82]</td></tr><tr><td>b2</td><td>( pt × n) · ( pt × n) / |pt| |pt|</td><td>all</td><td>[82]</td></tr><tr><td>b3</td><td>px/PT,tpT,bar</td><td>all</td><td>[82]</td></tr><tr><td>b4</td><td>pz/ |pt| |pbar</td><td>all</td><td>[82]</td></tr><tr><td>φC</td><td>arccos{ | (pp1 × pp2) · (pt × pbar)| / |pp1 × pp2| |pt × pbar|}</td><td>H</td><td>[87]</td></tr></table>

rest frames, none of the observables listed in table 1 requires a distinction between the top and the anti-top quark, which would be very challenging experimentally.

# 2.3 Distributions at the parton-level

The distributions of the observables defined in section 2.2 which will be discussed further in this work are shown in this section, while the others, which were found to have a lower sensitivity, are shown in appendix A. As a baseline cut to mimic the ATLAS and CMS tracker acceptance [92, 93], all particles are required to satisfy  $|\eta| < 2.0$ . The Higgs boson, top and anti-top quarks being massive particles, no minimum  $p_{\mathrm{T}}$  cut is applied.

The distributions of the Higgs  $p_{\mathrm{T}}$ , azimuthal angle difference and pseudorapidity difference between the top and anti-top quarks in the laboratory frame are shown in figure 2, together with the invariant mass of the  $tt$  pair, which is frame-invariant. The distributions of the  $b_{1}$ ,  $b_{2}$ ,  $b_{3}$  and  $b_{4}$  observables in the laboratory frame are shown in figure 3, while the distributions of the  $\phi_C$  angle in the Higgs boson frame and the cosine of the scattering angle with respect to the direction of the proton beams in the  $tt$  frame (  $|\cos \theta^{*}|$ , the so-called Collins-Soper angle) are shown in figure 4.

Large shape differences are observed between the SM and the pure  $\mathcal{CP}$ -odd scenario, whereas the shape differences between the SM and  $\mathcal{CP}$  models closer to the current experimental limit ( $\alpha_{t} = 45^{\circ}$  or  $35^{\circ}$ ) are much reduced, yet visible. Larger tails at high (low) value are observed in case of the presence of a  $\mathcal{CP}$ -odd component for  $p_{T,H}$ ,  $\Delta \eta_{t\bar{t}}$ ,  $m_{t\bar{t}}$ ,  $b_{1}$ ,  $b_{2}$ ,  $b_{3}$  and  $|\cos \theta^{*}|$  ( $b_{4}$ ,  $\phi_{C}$  and  $\Delta \phi_{t\bar{t}}$ ).

The effect from the  $|\eta| < 2.0$  cut on the top and anti-top quarks is particularly visible in the  $\Delta \eta_{t\bar{t}}$  distribution, which consequently has a sharp cut-off at  $\Delta \eta_{t\bar{t}} = 4$ . The impact of this cut is also clearly visible on the  $\phi_C$  angle and  $\cos \theta^*$  distributions, as it breaks the approximate, accidental flat distribution observed for these two observables in the SM by depleting the  $\phi_C < \pi / 4$  and  $|\cos \theta^*| > \cos(\pi / 4)$  regions. A comparison of the distributions of these variables before and after the cut on  $\eta$  can be found in appendix A.4. Let us also note here the large peak in the  $b_1$  observable distribution in the laboratory frame between the lower bound value of -1 and -0.9 that occurs irrespective of the  $\mathcal{CP}$  hypothesis, but is more pronounced for lower  $\alpha_t$ .

# 3 Evaluation of the observable performance

This section focuses on quantifying the discriminating power of each observable to distinguish between a mixed  $\mathcal{CP}$  state of the top-Yukawa coupling and the SM case. With the goal of extending the STXS framework in mind, we examine specifically the three channels explored so far in the experimental  $t\bar{t}H$  analyses at the LHC. We discuss in section 3.1 the limitations in resolution and reconstruction of the top quarks and Higgs boson in each channel, while the formula used for performance evaluation is explained in section 3.2.

# 3.1 Detector effects and selection efficiency

The  $t\bar{t}H$  process at the LHC has been studied so far through three main experimental channels. The first two channels target  $H \to \gamma \gamma$  and  $H \to b\bar{b}$  decays and will be labeled  $t\bar{t}H(\to \gamma \gamma)$  and  $t\bar{t}H(\to bb)$  in the following, while the third channel selects events with multiple leptons in the final state and will be labeled  $t\bar{t}H$  (multilep.). The latest experimental

![](images/8fcc3267d665b81013956f48062566d7d0de5f1f885e4ec37cb54ff90a18bc78.jpg)

![](images/056e9f33d95016d27eb954138e999b25ef524d875b9384c863e14a8e2e09b8f1.jpg)

![](images/5f8314a847800d2671233c748a9add499f21b9538f2233e1a92494dd0ae58321.jpg)

![](images/1df9e88da1bcc226e4621099d9d0c0ef7170a1198ef0d5d8f136deac6e53eb56.jpg)  
Figure 2. Distributions of the (top, left) Higgs  $p_{\mathrm{T}}$ , (top, right) pseudorapidity difference and (bottom, left) azimuthal angle difference between the  $t\bar{t}$  pair in the laboratory frame, as well as (bottom, right) the invariant mass of the  $t\bar{t}$  pair, which is frame-invariant.  $t\bar{t}H$  events generated at parton-level with  $g_{t} = 1$  and various values of  $\mathcal{CP}$  phase  $\alpha_{t}$  are considered following the event generation described in section 2.1. All distributions are normalised to unity.

![](images/7eb3de714a3bb44d3f16ab1fd6ed1fb56af984afcc1aa34a860867aa244ff0c0.jpg)

results from the ATLAS and CMS collaborations for each of these channels are available in [16, 19, 20, 22, 23, 25]. In order to compare the performance of the various observables defined in section 2 in discriminating the top-Yukawa  $\mathcal{CP}$  properties in a meaningful way, it is necessary to account for the limited efficiency of the event selection performed in experimental data analyses as well as the finite resolution and acceptance of the detectors. The  $t\bar{t}H(\rightarrow \gamma \gamma)$ ,  $t\bar{t}H(\rightarrow bb)$  and  $t\bar{t}H(\text{multilep.})$  channels differ widely in terms of final state objects and cross-section times branching ratio; taking into account these detector and acceptance effects is highly non-trivial, hence a simplified approach is adopted in this work. We use the  $t\bar{t}H$  samples described in section 2.1 as a starting point. Relevant decay branching ratios (Higgs, top quark) are taken from the SM, while the limited efficiency of the event selection and acceptance of the detectors are extracted per channel from ATLAS and/or CMS published results (as quoted in the text) and applied as event weights. Finite resolution effects are also extracted per channel from ATLAS and/or CMS published results and accounted for by smearing the four momenta of the Higgs boson and the top and anti-top quarks. All the input parameters to our model are shown in table 2, while more details are given below.

![](images/1bcd85fa13eb77410fd5aeeecb9eb17b3c17d560b6e2ddac4d2059b9d164f1d0.jpg)

![](images/20ed058bb52542b4236c5117ecef8f046b874c8c63e9b90caf07ac40ebda09cd.jpg)

![](images/155720030bcdc5a6e544a5d685bb6f8a99c8fb198f2260142bb24fa6088f448e.jpg)

![](images/c70c3cec8f028c1fc5258b5b5e25219a0acada39206233c29134dad8a5d041bf.jpg)  
Figure 3. Distributions of the  $b_{1}$ ,  $b_{2}$ ,  $b_{3}$  and  $b_{4}$  observables in the laboratory frame.  $t\bar{t}H$  events generated at parton-level with  $g_{t} = 1$  and various values of  $\mathcal{CP}$  phase  $\alpha_{t}$  are considered following the event generation described in section 2.1. All distributions are normalised to unity.

![](images/80e72f910a754e142f5c338a0f1ba152b7326738bfe3a4c8c34c6812a68702e6.jpg)

![](images/d0a14d23885ce37a00d174e81bf06f88e4d0d5189342db61fa310e5be97be39f.jpg)

![](images/8bbee8fc507322aee844711c29f33e41be312f77c40b983fc23dba04ab33468e.jpg)  
Figure 4. Distributions of (left) the  $\phi_C$  and (right) the  $|\cos \theta^*|$  observables in the Higgs and  $t\bar{t}H$  events generated at parton-level with  $g_t = 1$  and various values of  $\mathcal{CP}$  phase  $\alpha_t$  are considered following the event generation described in section 2.1. All distributions are normalised to unity.

![](images/b1b1d53906467baf3f5543aed450a1d233a200ee128a9e66342d7cf960ccdcb0.jpg)

The  $t\bar{t}H(\rightarrow \gamma \gamma)$  channel provides the smallest cross-section times branching ratio, but the best signal-over-background ratio due to the excellent detector resolution on the reconstructed Higgs mass. If any, all high- $p_{\mathrm{T}}$  neutrinos can be assumed to originate from the top or anti-top decays, which eases the  $t\bar{t}$  pair reconstruction. Following the  $t\bar{t}H$  event yields in signal-enriched regions provided in [20], we scale the  $t\bar{t}H$  yields at the parton-level by the branching ratio of  $H \rightarrow \gamma \gamma$  in the SM times the acceptance and selection efficiency of the  $t\bar{t}H$  sample for different  $\alpha_{t}$  values. For  $H \rightarrow \gamma \gamma$ , it ranges between 0.25 and 0.32, corresponding to  $\alpha_{t} = 0^{\circ}$  and  $\alpha_{t} = 90^{\circ}$ , respectively. The Higgs boson and top/anti-top quark transverse momenta are smeared using a Gaussian distribution with a width of 4 and 40 GeV, respectively, while the pseudo-rapidity of the top/anti-top quark is smeared by 0.5. These last numbers were tuned to match the ATLAS photon energy resolution [94] and the top quark mass distribution published in [20].

The  $ttH(\rightarrow bb)$  channel provides the highest cross-section times branching ratio, but the lowest signal-over-background ratio due to the large background originating from  $tt$  pairs produced in association with  $b$ -quarks and the comparatively poor detector energy resolution on jet measurements with respect to photons. Similarly to  $ttH(\rightarrow \gamma \gamma)$ , if any, all high- $p_{\mathrm{T}}$  neutrinos shall originate from the top or anti-top decays. However, jets originating from  $b$ -hadrons can come from either the Higgs boson decay or the top/anti-top decays, making the top/anti-top reconstruction more challenging with respect to  $ttH(\rightarrow \gamma \gamma)$ . Following the  $ttH$  event yields in signal-enriched regions provided in [25], we apply on top of the  $H(\rightarrow bb)$  SM branching ratio a scaling factor ranging from 0.005 to 0.0065 depending on the  $\mathcal{CP}$  hypothesis (the extreme values corresponding to  $\alpha_{t} = 0^{\circ}$  and  $\alpha_{t} = 90^{\circ}$ , respectively) to the  $ttH$  yields at the parton-level. The Higgs boson and top/anti-top quark transverse momenta are smeared using a Gaussian distribution with a width of 80 and 70 GeV, respectively, while the pseudo-rapidity of the top/anti-top quark is smeared by 0.8 and the azimuth angle by  $20^{\circ}$ . The smearing parameters were tuned to match the Higgs boson candidate mass distribution shown in [95] and the top reconstruction performance described in [96, 97].

Finally, the  $ttH$  (multilep.) channel lies in between the  $t\bar{t} H(\rightarrow \gamma \gamma)$  and  $ttH(\rightarrow bb)$  channels in terms of cross-section times branching ratio and signal-over-background ratio. A large number of combinations of top, anti-top quarks and Higgs boson decays lead to multi-lepton final states. In this work, we adopt a simplified approach by considering only the two most sensitive experimental sub-channels, which include the final states with two electrons or muons with the same sign or at least three electrons or muons. The resulting branching ratio is  $6.79\cdot 10^{-2}$  and we obtain the  $t\bar{t} H$  event yields from signal-enriched regions provided in [23]. Based on these yields, we apply to the branching ratio an additional acceptance and efficiency factor ranging from 0.036 to 0.042 depending on the  $\mathcal{CP}$  hypothesis (the extreme values corresponding to  $\alpha_{t} = 0^{\circ}$  and  $\alpha_{t} = 90^{\circ}$ , respectively). The smearing parameters are the same as the ones considered for the  $t\bar{t} H(\rightarrow bb)$  channel, except for the Higgs  $p_{\mathrm{T}}$  which is smeared by a larger value of  $120\mathrm{GeV}$  instead of  $80\mathrm{GeV}$ . Indeed, despite the lack of published experimental data, we anticipate lower performance in the Higgs boson reconstruction due to the multiple high- $p_{\mathrm{T}}$  neutrinos in these events, which can typically originate from either the Higgs or the top/anti-top decays.

Table 2. Summary of the input parameters to the simplified model used to emulate the detector effects and the analysis selection efficiency in each experimental channel. The first block (from top to bottom) shows the scaling factors accounting for the branching ratio, the second block shows the scaling factors accounting for the limited acceptance of the detector and the limited efficiency of the analysis selection, while the third and fourth blocks show the Gaussian smearing factors applied on the Higgs boson and top/anti-top momenta and the final  $tt\bar{H}$  event yields obtained for an integrated luminosity of  $300\mathrm{fb}^{-1}$ , respectively. As a reminder, all cross-sections are obtained directly from MadGraph5_aMC@NLO to which a k-factor of 1.14 is applied to correct for NLO effects.  

<table><tr><td></td><td>ttH(→γγ)</td><td>ttH(multilep.)</td><td>ttH(→bb)</td></tr><tr><td>BR</td><td>2.27·10-3</td><td>6.79·10-2</td><td>5.81·10-1</td></tr><tr><td colspan="4">Acceptance/efficiency scaling factors</td></tr><tr><td>αt=0°</td><td>2.5·10-1</td><td>3.6·10-2</td><td>5.0·10-3</td></tr><tr><td>αt=35°</td><td>2.5·10-1</td><td>3.6·10-2</td><td>5.2·10-3</td></tr><tr><td>αt=45°</td><td>2.7·10-1</td><td>3.8·10-2</td><td>5.4·10-3</td></tr><tr><td>αt=90°</td><td>3.2·10-1</td><td>4.2·10-2</td><td>6.5·10-3</td></tr><tr><td colspan="4">Smearing factors</td></tr><tr><td>ΔpT,H [GeV]</td><td>4</td><td>120</td><td>80</td></tr><tr><td>ΔpT,t [GeV]</td><td>40</td><td>70</td><td>70</td></tr><tr><td>Δηt</td><td>0.5</td><td>0.8</td><td>0.8</td></tr><tr><td>Δφt [°]</td><td>-</td><td>20</td><td>20</td></tr><tr><td colspan="4">Final ttH event yields at 300 fb-1</td></tr><tr><td>αt=0°</td><td>86</td><td>372</td><td>442</td></tr><tr><td>αt=35°</td><td>70</td><td>302</td><td>373</td></tr><tr><td>αt=45°</td><td>67</td><td>281</td><td>341</td></tr><tr><td>αt=90°</td><td>47</td><td>185</td><td>245</td></tr></table>

# 3.2 Significance computation

In order to quantify the sensitivity of the various observables discussed in section 2 to  $\mathcal{CP}$  violation in the top-Yukawa coupling, we assume to have at our disposal the measurement of the corresponding  $t\bar{t} H$  distributions in each experimental channel. The scaling and smearing factors described in the previous section are applied to  $t\bar{t} H$  events generated at the parton level to emulate detector effects and obtain realistic yields.

The sensitivity of an observable to a given BSM model is evaluated by computing a significance  $S$ . This significance reflects the discriminating power to reject the BSM hypothesis (parameterized by  $g_{t},\alpha_{t}$ ) against the null hypothesis of  $g_{t} = 1$ ,  $\alpha_{t} = 0$  (corresponding to

the SM). Formally, it is defined as the sum in quadrature of the significance computed in each bin of the observable,  $(S_{i})_{i = 1\dots N_{\mathrm{bins}}}$ . The observed  $t\bar{t} H$  event yields are assumed to match the central SM predictions. If we make the additional assumption that they are Poisson distributed and not impacted by additional sources of uncertainty, the  $S_{i}$  can then be evaluated using the Wilk's theorem:

$$
S _ {i} = \sqrt {- 2 \left(n _ {i} \ln \frac {m _ {i}}{n _ {i}} + n _ {i} - m _ {i}\right)}, \tag {3.1}
$$

where  $n_i$  and  $m_i$  are the numbers of events in the  $i$ th bin of the observable as predicted by the SM and the BSM model under consideration, respectively. Accordingly, the significance  $S$  results as

$$
S = \sqrt {\sum_ {i = 1} ^ {N _ {\mathrm {b i n s}}} S _ {i} ^ {2}} = \sqrt {- 2 \sum_ {i = 1} ^ {N _ {\mathrm {b i n s}}} \left(n _ {i} \ln \frac {m _ {i}}{n _ {i}} + n _ {i} - m _ {i}\right)}. (3. 2)
$$

In the following, all bins with  $n_i < 2$  are merged with their neighbouring bins until the merged bin contains more than two events, starting with left neighbours, to ensure the validity of Wilk's theorem for significance evaluations. We checked that the significance values are stable within a few percent if  $n_i < 5$  is used instead.

The previous equations rely on two important assumptions, first that the measured  $ttH$  event yields are Poisson distributed and second that they are not impacted by additional sources of uncertainty. In reality, non- $ttH$  events are expected to enter the measurement selection such that

$$
n _ {i} = n _ {i} ^ {\mathrm {d a t a}} - n _ {i} ^ {\mathrm {b k g}}, \tag {3.3}
$$

where  $n_i^{\mathrm{data}}$  and  $n_i^{\mathrm{bkg}}$  are the number of observed data events and the number of predicted non- $t\bar{t}H$  events in the  $i$ th bin, respectively. The evaluation of  $n_i^{\mathrm{bkg}}$  is part of the experimental analysis work. It is impacted by systematic uncertainties related to the detector calibration and physics modelling. Therefore the assumptions used to derive eqs. (3.1) and (3.2) are valid only in the limit of high signal over background ratio  $(S / B)$ , i.e.  $n_i / n_i^{\mathrm{bkg}} \gg 1$ . To take account of these deviations from our initial assumptions, the eqs. (3.1) and (3.2) are corrected in the following way [98]:

$$
S _ {i} = \sqrt {- 2 \left(n _ {i} \ln \frac {m _ {i} \left(n _ {i} + \sigma_ {i} ^ {2}\right)}{n _ {i} ^ {2} + m _ {i} \sigma_ {i} ^ {2}} - \frac {n _ {i} ^ {2}}{\sigma_ {i} ^ {2}} \ln \left[ 1 + \frac {\sigma_ {i} ^ {2} \left(m _ {i} - n _ {i}\right)}{n _ {i} \left(n _ {i} + \sigma_ {i} ^ {2}\right)} \right]\right)}, \tag {3.4}
$$

$$
S = \sqrt {- 2 \sum_ {i = 1} ^ {N _ {\mathrm {b i n s}}} \left(n _ {i} \ln \left[ \frac {m _ {i} \left(n _ {i} + \sigma_ {i} ^ {2}\right)}{n _ {i} ^ {2} + m _ {i} \sigma_ {i} ^ {2}} \right] - \frac {n _ {i} ^ {2}}{\sigma_ {i} ^ {2}} \ln \left[ 1 + \frac {\sigma_ {i} ^ {2} \left(m _ {i} - n _ {i}\right)}{n _ {i} \left(n _ {i} + \sigma_ {i} ^ {2}\right)} \right]\right)}, \tag {3.5}
$$

where  $\sigma_{i}$  is a newly introduced term corresponding to an extra uncertainty in  $n_i$ . It is computed as the sum in quadrature of two terms,

$$
\sigma_ {i} ^ {2} = \left(\sigma_ {i} ^ {\mathrm {s t a t}}\right) ^ {2} + \left(\sigma_ {i} ^ {\mathrm {s y s t}}\right) ^ {2}. \tag {3.6}
$$

The first term,  $\sigma_{i}^{\mathrm{stat}}$ , accounts for the additional Poisson-like uncertainty originating from the fact that  $n_{i}^{\mathrm{bkg}} \neq 0$  and can be approximated by  $\sqrt{n_{i}^{\mathrm{bkg}}}$ . The  $(n_{i}^{\mathrm{bkg}})_{i=1\dots N_{\mathrm{bins}}}$  largely

depend on the analysis design and the observable considered and therefore are in general not trivial to evaluate in the context of this work. Though we note that they are connected to the  $S / B$  in each bin such that  $\sigma_{i}^{\mathrm{stat}} = \sqrt{\frac{n_{i}}{S / B}}$ . The  $S / B$  typically varies bin-by-bin in the experimental data analyses, however, a single value per channel is considered here for simplification, taken from the typical values observed in the  $t\bar{t}H$ -enriched regions defined in the corresponding ATLAS and CMS analyses [20, 23, 25].  $S / B = 1$ , 0.4, and 0.1 is assumed in the  $t\bar{t}H(\rightarrow \gamma \gamma)$ ,  $t\bar{t}H(\mathrm{multilep.})$ , and  $t\bar{t}H(\rightarrow bb)$  channels, respectively. The validity of this simplifying assumption depends on the shape differences between signal and background for the observables under consideration, which will be discussed further in section 5.1.

The second term,  $\sigma_{i}^{\mathrm{syst}}$ , accounts for the systematic uncertainty in  $n_i^{\mathrm{bkg}}$ . We define it so that it contains the uncertainty in the shape of the non- $t\bar{t}H$  events. We take  $\sigma_{i}^{\mathrm{syst}} = n_i \cdot 0.2$  [0.5] for the  $t\bar{t}H$  (multilep.)  $[t\bar{t}H(\rightarrow bb)]$  channel, following [23, 25], while  $\sigma_{i}^{\mathrm{syst}} = 0$  is assumed for the  $t\bar{t}H(\rightarrow \gamma \gamma)$  channel as this channel is typically dominated by statistical uncertainties [20]. The last source of uncertainty to take into account is the uncertainty in the overall background normalisation. It is significant in the  $t\bar{t}H(\rightarrow bb)$  and  $t\bar{t}H$  (multilep.) channels only. For these two channels, we decided to account for it by rescaling the total BSM  $t\bar{t}H$  event yield to match the total SM  $t\bar{t}H$  event yields prior to the computation of the significance. This way no discrimination power is obtained from differences in the total rate between SM and BSM in these two channels. In practice, the  $m_i$  are replaced in eqs. (3.4) and (3.5) by  $m_i'$ , which corresponds to the number of events in the  $i$ th bin of the observable as predicted by the BSM model under consideration rescaled so that  $\sum_{i=1}^{N_{\mathrm{bins}}} m_i' = \sum_{i=1}^{N_{\mathrm{bins}}} n_i$ .

# 4 Results

We present results for a luminosity of  $300\mathrm{fb}^{-1}$ , targeting the end of LHC Run-3. Since the current experimental limits exclude values of  $g_{t} = 1$ ,  $\alpha_{t} \gtrsim 43^{\circ}$  at the  $95\%$  CL using  $139\mathrm{fb}^{-1}$  [20], we choose  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  as a benchmark. In section 4.1, we calculate the significance for all the observables mentioned in section 2.2 as well as for the associated two-dimensional observable combinations. This is done with a fixed number of evenly spaced bins. In section 4.2, we optimize the binning individually for the most promising variables based on the combined significance of the three experimental channels. We compare our findings to a multivariate approach in section 4.3. Finally, we show in section 4.4 the expected sensitivity in the full two-dimensional  $(g_{t},\alpha_{t})$  parameter plane.

# 4.1 Results with default binning

We first evaluate the sensitivity of each observable separately starting from a default binning of 14 evenly distributed bins. In addition, we evaluate the sensitivity of the combination of two observables starting from a two-dimensional binning of  $6 \times 6$  evenly distributed bins. These (not yet optimised) binnings were chosen to maximise the number of bins to avoid losing valuable kinematic shape information while populating most of the bins with at least a few events. The bin merging method described in the previous section is then applied to guarantee at least two SM  $t\bar{t}H$  events per bin. In total, 31 different observables (and their combinations) are considered across the four different rest frames defined in section 2.2.

While the results for all 465 different combinations can be found in appendix B, we focus in the following on the most promising observables and related combinations.

The sensitivity of  $p_{\mathrm{T},H}$  and  $\Delta \phi_{t\bar{t}}$  in the laboratory frame to a BSM signal corresponding to  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  is shown in figure 5 for an integrated luminosity of  $300\mathrm{fb^{-1}}$ , separately (emphasized column) and in combination with a second observable (other columns). The significance in each channel as well as the combined significance are shown. The  $p_{\mathrm{T},H}$  observable was chosen to be displayed here as it shows high sensitivity and corresponds to the observable used in the STXS binning v1.2 [77-80], while  $\Delta \phi_{t\bar{t}}$  was chosen to be displayed here as it provides the best significance both when considered alone and when combined with certain observables.

The sensitivity of the  $t\bar{t}H(\rightarrow \gamma \gamma)$  channel largely comes from the difference in terms of total event rate between the SM and BSM hypotheses, and therefore does not depend strongly on the choice of observable. On the other hand, the other channels suffer from a larger background and a less precise event reconstruction, such that no discrimination from the total event rate was considered (see section 3.2). Hence, the choice of the best observable for the combined three channels is mostly driven by the expected performance in the  $t\bar{t}H(\rightarrow bb)$  and  $t\bar{t}H(\text{multilep.})$  channels. The highest significance is obtained when combining  $\Delta \phi_{t\bar{t}}$  with  $b_4$  in the lab frame and reaches  $S = 1.91$ . The best combinations involving  $p_{T,H}$  reach significances ranging from 1.82 to 1.87, and are obtained with  $\Delta \phi_{t\bar{t}}, b_1$ , and  $b_2$  in the lab frame, as well as  $\Delta \eta_{t\bar{t}}, |\cos \theta^*|$ , and  $b_2$  in the  $t\bar{t}$  frame.

While  $p_{T,H}$  alone yields a significance considerably weaker than the best combinations, the difference between the 1D  $\Delta \phi_{t\bar{t}}$  result, the best 2D combinations involving  $p_{T,H}$  and any 2D combination involving  $\Delta \phi_{t\bar{t}}$  is smaller. This result brings some flexibility in the final choice of observables. Since the  $t\bar{t}H$  process is split into  $p_{T,H}$  bins in the current STXS binning, we favour for practical reasons a reduced set of observables which reach the highest significances when paired with  $p_{T,H}$ . For comparison, we also show in figure 5 the best combinations involving  $\Delta \phi_{t\bar{t}}$ . As we will see, given the small difference to the combinations with  $\Delta \phi_{t\bar{t}}$ , we understand our chosen combinations with  $p_{T,H}$  as close to optimal.

# 4.2 Final results with optimised binning

We now optimize the binning of the observables preselected in the previous section for an integrated luminosity of  $300\mathrm{fb}^{-1}$ . In combination with  $p_{T,H}$ , the  $b_{2}$  variable yields the same significance in the lab and  $t\bar{t}$  frame. Taking into account that  $p_{T,H}$  is given in the lab frame, we will consider the  $b_{2}$  observable only in the lab frame in the following. For practical reasons, we follow the STXS v1.2 framework for the Higgs transverse momentum, which specifies the following six bins:

$$
\cdot p _ {T, H}: [ 0, 6 0, 1 2 0, 2 0 0, 3 0 0, 4 5 0, + \infty ] (\mathrm {G e V})
$$

For the remaining five observables, i.e.  $\Delta \phi_{t\bar{t}}$ ,  $b_{1}$ , and  $b_{2}$  in the lab frame, as well as  $\Delta \eta_{t\bar{t}}$  and  $|\cos \theta^{*}|$  in the  $t\bar{t}$  frame, we define six bins as well such that the less populated regions in the tails of the distributions get wider bins:

![](images/9ce7efe3abc6a0fb3312be8cdbc6ace270f4e9ce1021d1909ba4a6bd7fe5be19.jpg)

![](images/29cefbded67a0d5631c80a1ed296eab233109cdb65596b634e3ded4d81fbebfd.jpg)  
Figure 5. Significances evaluated from the (top)  $p_{\mathrm{T},H}$  and (bottom)  $\Delta \phi_{t\bar{t}}$  distributions in the laboratory frame for a BSM signal corresponding to  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$ . The emphasised column shows the significance obtained from the one-dimensional distribution while the others show the significances obtained when combining with a second observable. The significances are shown per experimental channel and after their statistical combinations.

-  $\Delta \phi_{tt}^{\mathrm{lab}}$ :  $[0, \pi/4, \pi/2, 2\pi/3, 5\pi/6, 11\pi/12, \pi]$  (rad.),  
-  $b_1^{\mathrm{lab}}$ : [-1, -0.95, -0.8, -0.2, 0.3, 0.8, 1.0],  
-  $b_2^{\mathrm{lab}}$ :  $[-1, -0.6, -0.4, -0.2, 0., 0.3, 1.0]$ ,  
-  $\Delta \eta_{tt}^{t\bar{t}}$ : [0, 0.5, 1, 1.5, 2, 3, 5],  
$\mid \cos \theta^{*}\mid$  .. [0, 0.2, 0.4, 0.55, 0.7, 0.85, 1].

The normalized distributions of these observables for  $\alpha_{t} = 0^{\circ}$  and  $35^{\circ}$  are shown in figures 6 and 7. The distributions are shown for each observable at the parton level and for the various experimental channels including the smearing factors discussed in section 3.1. The significances obtained for each preselected observable in a two-dimensional combination with  $p_{T,H}$  using the optimized binning are shown in figure 8. The same table considering combinations with  $\Delta \phi_{t\bar{t}}$  is also displayed.

We observe that the optimised binning using just 6 bins almost reproduces the significance based on the default binning after bin merging in the case of the 1D distributions of either  $p_{T,H}$  or  $\Delta \phi_{\bar{t}\bar{t}}$ . For the case of the 2D distributions, the optimised binning yields a very similar performance as the default binning, with an improvement typically at the few-percent level. The similarity of the significances obtained in the default and the optimised binning also indicates a robustness of the method of 2D distributions against the choice of the binning as long as one makes sure that each bin is populated by at least a few events. Therefore we consider the optimised binning as validated and will from now on refer to significances computed from these exclusively.

# 4.3 Comparison to a multivariate analysis

In this section, we compare the significance obtained from the two-dimensional distributions reported in the previous section to the one obtained from the output of a multivariate analysis algorithm trained on the full set of observables<sup>6</sup> introduced in section 2. We assume that such a multivariate analysis is able to make better use of the provided kinematic information of the observables and therefore outperforms the practical usage of only two observables. In the following, we use this comparison to a multivariate analysis to estimate the loss of sensitivity due to the usage of only two physically-motivated observables.

We implement a Boosted Decision Tree (BDT) based on the XGBoost algorithm [99]. The goal of the BDT is to distinguish a signal characterized by  $\alpha_{t} \neq 0$  from the  $\alpha_{t} = 0$  hypothesis. Separate trainings are performed for the three  $t\bar{t}H$  channels. The scaling factors and smearings described in table 2 are applied to  $t\bar{t}H$  events generated at the parton level to emulate detector effects and obtain realistic yields in each channel. The SM  $t\bar{t}H$  sample is used as 'background' and the  $g_{t} = 1$ ,  $\alpha_{t} = 90^{\circ}$  sample is used as 'signal' in the training as this choice leads to the best performance in the full parameter space [100]. To leverage the statistics of the entire dataset, we employ a  $k$ -fold strategy [101] with  $k = 5$ .  $80\%$  of the dataset is dedicated to training, while the remaining  $20\%$  serves as testing subset. This operation is repeated five times to test the full dataset. The performance of the BDT is evaluated by computing the significance from the BDT output score based on eqs. (3.4) and (3.5).

The output BDT score distributions for the SM scenario and the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  signal sample in each  $t\bar{t}H$  channel are shown in figure 9. The bin merging method described in section 3.2 is applied to guarantee at least two SM  $t\bar{t}H$  events per bin. The significance values computed from these distributions are summarized and compared to the best significance values obtained from two-dimensional distributions in table 3. As expected, the significances obtained from the BDT are higher, but only to a limited extent ( $\sim 10\%$  for  $H \to \gamma \gamma$ ,  $\sim 17\%$  for  $H \to$  multilep. and  $\sim 25\%$  for  $H \to b\bar{b}$ ), with a combined significance reaching 2.21 compared to 1.91 for the two-dimensional method. The improvement in sensitivity of the BDT is larger for the  $t\bar{t}H$  (multilep.) and  $t\bar{t}H(\to b\bar{b})$  channels, as these channels select more  $t\bar{t}H$  events (see table 2) and therefore allow better use of kinematic shape information. We conclude that the approach taken so far consisting of using two-dimensional distributions

![](images/7e623f305f13d8a29b608c8684fd8aea8ee30c3c0a8ac31bcb55a1919acd8f4c.jpg)

![](images/304b59e52beb775fa6fb95d998885c845f993d933640e69adeb07b01b110e3df.jpg)

![](images/3fc21bba6d95bbab70f8f29049a88ac618268b935af7784515040a3b2e9c674d.jpg)

![](images/8c01d28e59328b923a84f2b47308d5f4753ccac4714ca3e732ea2b2f2dc3a488.jpg)  
Figure 6. Distributions (from top to bottom) of  $p_{T,H}$ ,  $\Delta \phi_{t\bar{t}}$ ,  $b_{1}$  and  $b_{2}$  in the lab frame with optimised binning. Each canvas is split into four panels, from left to right the following distributions are shown: parton-level and smeared distributions for the  $ttH(\rightarrow \gamma \gamma)$ ,  $ttH(\mathrm{multilep.})$ , and  $ttH(\rightarrow bb)$  channels. The SM distributions are represented as solid black lines, while the distributions for  $\alpha_{t} = 35^{\circ}$  are shown as dashed orange lines.

![](images/f97b17485a3b94a83922c2d1de33797ad7b8369f1cd9fafc6c59fb51340e4cc9.jpg)

![](images/dcb1c77645a92828e1eb5799cd5b0e3aab9c40927305bdb46467ed8bf9b9563a.jpg)  
Figure 7. Distributions of (top)  $\Delta \eta_{tt}$  in the  $t\bar{t}$  frame and (bottom)  $|\cos \theta^{*}|$  with optimized binning. Each canvas is split into four panels, from left to right the following distributions are shown: parton level and smeared distributions for the  $t\bar{t} H(\rightarrow \gamma \gamma)$ ,  $t\bar{t} H$  (multilep.), and  $t\bar{t} H(\rightarrow b\bar{b})$  channels, respectively. The SM distributions are represented as solid black lines, while the distributions for  $\alpha_{t} = 35^{\circ}$  are shown as dashed orange lines.

![](images/5ec72077d5e7dd06bc0f0af67e64a35c8d9979d6f90e39fff7d50dc4d7b35ff3.jpg)  
Figure 8. Significances evaluated from the (left)  $p_{\mathrm{T},H}$  and (right)  $\Delta \phi_{t\bar{t}}$  distributions in the lab frame for a BSM signal corresponding to  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$ . The emphasised column shows the significance obtained from the one-dimensional distribution while the others show the significance obtained when combining with a second observable. All observables are considered in their optimised binning. The significances are shown per experimental channel and after their statistical combinations.

![](images/7820cb1e10c37b3f63158889b6e82f4eeb5bad55251495c4455ffd392a1cfa8a.jpg)

![](images/b9aae9c4be5e469065a8062cc7b3945ee5a34c174ee23c24e8c25f0ace2aa166.jpg)  
Figure 9. Distributions of the output BDT score for the (left)  $t\bar{t}H(\rightarrow \gamma \gamma)$ , (center)  $t\bar{t}H$  (multilep.), and (right)  $t\bar{t}H(\rightarrow bb)$  channels, evaluated for the (black) SM and (orange)  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  sample.

Table 3. Significance obtained from the output BDT score distributions and best significance obtained from two-dimensional distributions in section 4.2.  

<table><tr><td>Channel</td><td>Significance (BDT)</td><td>Significance (2D)</td></tr><tr><td>ttH(→γγ)</td><td>1.75</td><td>1.57</td></tr><tr><td>ttH(multilep.)</td><td>1.17</td><td>0.94</td></tr><tr><td>ttH(→bb)</td><td>0.69</td><td>0.55</td></tr><tr><td>Combined</td><td>2.21</td><td>1.91</td></tr></table>

to probe  $\mathcal{CP}$  violation in the top-Yukawa coupling is sufficient to reach a close-to-optimal sensitivity with  $300\mathrm{fb}^{-1}$  of data, especially since the combined sensitivity is driven by the statistically limited  $H\rightarrow \gamma \gamma$  channel.

# 4.4 Expected exclusion limits

Only results for  $\alpha_{t} = 35^{\circ}$  and  $g_{t} = 1$  have been presented so far. In this section, we show and discuss the expected exclusion limits at the  $95\%$  confidence-level (using the Gaussian limit, i.e.  $S = 1.96$ ) in the full  $(\alpha_{t}, g_{t})$  plane for an integrated luminosity of  $300\mathrm{fb}^{-1}$ . The significance at any given point of the parameter space is computed based on the distribution of the observables under consideration for both the SM and BSM cases, where the BSM  $t\bar{t}H$  yields are obtained from eq. (2.1). The resulting two-dimensional contours are shown for each  $t\bar{t}H$  channel as well as their statistical combination in figure 10. The contours for the  $t\bar{t}H$  (multilep.) and  $t\bar{t}H(\rightarrow bb)$  channels are not closed at high values of  $g_{t}$ , which is due to the fact that any discrimination power arising from differences in the total rate between SM and BSM is neglected in these two channels (see section 3.2).

In the current STXS  $p_{T,H}$  setup (i.e.,  $p_{T,H}$  as the single discriminating variable with 6 bins), the discriminating power between SM and BSM hypotheses in the  $ttH(\rightarrow \gamma \gamma)$  channel

originates mainly from differences in the total event rate (see section 4.1). This channel almost entirely drives the sensitivity and allows to constrain  $|\alpha_t| \lesssim 43^\circ$  for  $g_t = 1$ , while the combination of the three channels improves the constraint marginally to  $|\alpha_t| \lesssim 41^\circ$  for  $g_t = 1$ . In this scenario, the  $ttH(\rightarrow bb)$  channel contribution to the combined sensitivity in the entire parameter space is rather small. The  $ttH$  (multilep.) channel contributes to the combined sensitivity more strongly for  $g_t > 1$ , where higher  $ttH$  yields are expected such that a higher discrimination power from the  $p_{T,H}$  kinematic shape is obtained. In this region, an improvement up to  $36\%$  is observed in the combined limit on  $|\alpha_t|$  due to  $ttH$  (multilep.), obtained for  $g_t = 1.27$ .

If the current STXS  $p_{T,H}$  setup is extended by splitting further  $t\bar{t}H$  events according to their  $|\cos \theta^{*}|$  value, the combined limit at  $g_{t} = 1$  is improved by  $12\%$  to reach  $|\alpha_{t}| \lesssim 36^{\circ}$ . The best improvement of the combined limit on  $|\alpha_{t}|$  over the  $t\bar{t}H(\rightarrow \gamma \gamma)$  standalone limit is  $40\%$  and is reached at  $g_{t} = 1.24$ . The improvement originates mainly from the improved sensitivity of the  $t\bar{t}H(\mathrm{multilep.})$  channel, although the sensitivity of the  $t\bar{t}H(\rightarrow bb)$  channel is also significantly improved and contributes to the combination. In this scenario, a higher sensitivity from the  $t\bar{t}H(\mathrm{multilep.})$  is expected with respect to the  $t\bar{t}H(\rightarrow \gamma \gamma)$  channel for  $1.10 < g_{t} < 1.31$ . We obtain comparable results when combining  $p_{T}^{H}$  with one of the other promising candidates identified in the previous sections, i.e.  $\Delta \phi_{t\bar{t}}$ ,  $b_{1}$  or  $b_{2}$  in the lab frame.

figure 10 also shows the exclusion contours for  $\Delta \phi_{t\bar{t}}$  instead of  $p_{T,H}$  as single variable, as well as for the two-dimensional binning of  $\Delta \phi_{t\bar{t}}$  and  $|\cos \theta^{*}|$ , which was among the best combinations not involving  $p_{T,H}$  identified in section 4.1. As expected from figure 8, the  $\Delta \phi_{t\bar{t}}$  observable alone performs better than  $p_{T,H}$  alone mainly due to its higher level of kinematic shape discrimination, which leads to an increased sensitivity in the  $t\bar{t}H$  (multilep.) and  $t\bar{t}H(\rightarrow bb)$  channels. Regarding the two-dimensional observable combination ( $\Delta \phi_{t\bar{t}}, |\cos \theta^{*}|$ ), the picture is qualitatively very similar to the  $(p_{T,H}, |\cos \theta^{*}|)$  case and compatible limits are found after statistical combinations of the three channels ( $|\alpha_t| \lesssim 36^\circ$  for  $g_t = 1$ ).

Finally we show in figure 10 the exclusion contours resulting from the significance computed from the output BDT score described in section 4.3. Since the BDT inputs include the full set of observables shown in table 1, we expect it to outperform our two-dimensional approach. Still, only a slight improvement over the limits obtained from simple two-dimensional variable combinations is observed overall. In particular, the expected limit of  $|\alpha_t| \lesssim 33^\circ$  for  $g_t = 1$  from the BDT is close to the corresponding result obtained from the  $(p_{T,H},|\cos \theta^*|)$  distribution.

To summarize, we found comparable performance between the best  $p_{T,H}$ -based and  $\Delta \phi_{t\bar{t}}$  based two-dimensional variable combinations and the output from a multivariate analysis based on the full set of observables shown in table 1.

# 5 Extending the STXS framework

The additional data from the ongoing Run 3 of the LHC is expected to increase the size of the proton-proton dataset of the ATLAS and CMS collaborations from  $140\mathrm{fb}^{-1}$  to about  $300\mathrm{fb}^{-1}$ . The increased statistics will open the possibility to extract more precise information from the  $t\bar{t}H$  kinematic shapes. As of now, the sensitivity to the  $\mathcal{CP}$  nature of the top-Yukawa coupling is largely driven by the  $t\bar{t}H(\rightarrow \gamma \gamma)$  channel. However, based on our results, we

![](images/15e40f8d029f4a48eecb89745e264dc493d5c03723bd289badeadee667a66bc5.jpg)

![](images/ff98ddfb0271c8d405d0cff199844cc6630f3280bd0d6103cb135200e6c465b1.jpg)

![](images/83988433671dfe1b642d4aa6cb92a345c3284fd5980fb4cb9a2aef4395525a29.jpg)

![](images/aeba348c5fcfbf4d6dce5f43eba46fa0a7582f9d1b4b779b336ffa9711b17535.jpg)  
Figure 10. Expected limits at the  $95\%$  confidence level in the  $(\alpha_{t},g_{t})$  plane for  $\mathcal{L} = 300\mathrm{fb}^{-1}$  when considering (upper left) the current  $p_{T,H}$  STXS setup and (upper right) the  $\Delta \phi_{tt}^{\mathrm{lab}}$  observable alone. On the second row, the results from the two-dimensional observables  $(p_{T,H},|\cos \theta^{*}|)$  and  $(\Delta \phi_{tt}^{\mathrm{lab}},|\cos \theta^{*}|)$  are shown. The expected limits obtained from the BDT output score described in section 4.3 are also shown for comparison.

![](images/a5f1e4fd89ceb1a6a8047d4e47bc1f49e6c8aeacd316e406363bfd0b11d70df2.jpg)

![](images/e985d3d6b893eaef2aef2ca0d915857dc2d4bcdea61dc8c03eced0b1c50a9286.jpg)

expect a significant increase in sensitivity of the  $t\bar{t}H$  (multilep.) and  $t\bar{t}H(\rightarrow bb)$  channels by the end of Run 3. If confirmed, the statistical combination of the various  $t\bar{t}H$  channels will become key to constrain further the  $\mathcal{CP}$  nature of the top-Yukawa coupling over the next few years. We propose in section 5.1 a qualitative discussion regarding the validity of our background assumptions used to evaluate the significance for the best candidate observables. This allows us to reduce further our list of candidates and to formulate our final proposal for a  $\mathcal{CP}$ -sensitive STXS extension in section 5.2.

# 5.1 Further background considerations

The significance computation used to evaluate the sensitivity of each observable combination relies on some assumptions which were discussed in section 3.2. In particular, a constant signal  $(t\bar{t}H)$  over background (non- $t\bar{t}H$ ) ratio is assumed throughout all the bins considered in our study and  $S/B = 1$ , 0.4, and 0.1 are assumed in the  $t\bar{t}H(\rightarrow \gamma\gamma)$ ,  $t\bar{t}H(\text{multilep.})$ , and  $t\bar{t}H(\rightarrow bb)$  channels, respectively. These values are based on typical values observed in the corresponding ATLAS and CMS analyses. Qualitatively, this assumption should be

conservative under the condition that the background shape is not peaking around the highest significance bins, which we propose to verify here.

# Higgs background processes.

We start with a short discussion of Higgs background processes, i.e. mainly  $tHq$  and  $tWH$  events in which a second top quark could be wrongly reconstructed. In the SM, the cross-sections of the  $tHq$  and  $tWH$  processes are comparably low with respect to  $t\bar{t}H$ , with  $\sigma_{\mathrm{SM}}^{tHq} / \sigma_{\mathrm{SM}}^{t\bar{t}H} \approx 0.15$  and  $\sigma_{\mathrm{SM}}^{tWH} / \sigma_{\mathrm{SM}}^{t\bar{t}H} \approx 0.03$ . Both Higgs background processes become more important for higher fractions of  $\mathcal{CP}$ -odd top-Yukawa coupling, however, at  $(g_t, \alpha_t) = (1, 35^\circ)$ , we still find  $\sigma^{tHq} / \sigma^{t\bar{t}H} \approx 0.24$  and  $\sigma^{tWH} / \sigma^{t\bar{t}H} \approx 0.05$ . Given the low cross-sections in the parameter space of interest and the additional yield reduction expected from the analysis selection, we conclude that the  $tHq$  and  $tWH$  processes can only play a minor role in the measurement of the  $t\bar{t}H$  kinematic distributions and therefore satisfy the assumptions made in section 3.2.

# Non-Higgs background processes.

We discuss here the most relevant non-Higgs background process in each channel:  $t\bar{t}\gamma \gamma$  for the  $H \to \gamma \gamma$  channel,  $t\bar{t}W$  for the multi-lepton channel, and  $t\bar{t}b\bar{b}$  for the  $H \to b\bar{b}$  channel, for which samples were generated at the parton-level based on the setup described in section 2.1. For each background process, we assume that the non-top-quark particles are misidentified as a Higgs boson to compute the observables introduced in section 2. In practice, we implement this by setting  $p_{H} = p_{\gamma \gamma}$  for  $t\bar{t}\gamma \gamma$ ,  $p_{H} = p_{W}$  for  $t\bar{t}W$ , and  $p_{H} = p_{b\bar{b}}$  for  $t\bar{t}b\bar{b}$ . Following these assignments, we show in figure 11 the  $t\bar{t}\gamma \gamma$ ,  $t\bar{t}W$  and  $t\bar{t}b\bar{b}$  distributions for the various observables selected in section 4. We also show in the same figure the combined significance obtained in each bin for the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  sample. This gives us a qualitative estimate of whether our  $S/B$  assumptions about the background uncertainties from section 3.2 are conservative or not. If the non-Higgs backgrounds for a specific variable peaks in the bin which mainly drives the sensitivity, we consider this variable's sensitivity to be possibly inflated in section 4 and discard it in the final proposal. The parton-level non-Higgs background distributions were cross-checked against distributions obtained from the same samples but after parton shower (using Pythia8 [90]) and while minor shape differences are present, the conclusions below remain unchanged.

The  $\Delta \phi_{t\bar{t}}$  and  $b_{1}$  distributions in the lab frame show the same behaviour, with a clear peak at one end of the distribution in both the background distributions and the significance. The peak is particularly pronounced for the  $t\bar{t}\gamma \gamma$  background and has the same location as the peak in the significance. Consequently, the sensitivity of these observables may be overestimated in our results shown in section 4 and they are excluded from the final shortlist. The distribution of  $b_{2}$  in the lab frame has a peak of the background in the third bin, which is, however, not the bin dominating the total significance. For the  $\Delta \eta_{t\bar{t}}$  and  $|\cos \theta^{*}|$  distributions in the  $t\bar{t}$  frame, the sensitivity as well as the background distributions are relatively flat across the full range. Therefore we expect our sensitivity estimates to be more robust for these three last observables, which are the final ones selected.

![](images/92748a8807cd80ac2a63c9d617e5e78b4d1fd4fb498276912a180624381a19c1.jpg)

![](images/fa5e6d7689265c19e8d4ba75cf983c59b8239a0679b17b7cb27f1ceafc787502.jpg)

![](images/d987f63f8c15e12bb178d2c1ac2f492beec1f366a1a1f32551b93c06a7e19dd7.jpg)

![](images/dcf00d87d669a7f5d9fae6a5ec9ea1081bb7b1f0b70b1d16e2a00a682cc70798.jpg)

![](images/eceb5daf164ab8fe122308524eb40e5755f060d3aa300d12544713d7477b13fb.jpg)

![](images/363c04c95261f9e42619482cdecc7708bfc9fe3a688c9a90c80c55a34ae3bb61.jpg)  
Figure 11. Distributions of the (top, left) azimuthal angle difference between the  $t\bar{t}$  pair, (top, right)  $b_{1}$  observable, and (center, left)  $b_{2}$  observable in the lab frame, and distribution of the (center, right) pseudorapidity difference between the  $t\bar{t}$  pair and (bottom)  $|\cos \theta^{*}|$  observable in the  $t\bar{t}$  frame. The distributions for SM  $t\bar{t}\gamma \gamma$ ,  $t\bar{t}W$  and  $t\bar{t}b\bar{b}$  events are shown in each upper panel plot. The observables are reconstructed by setting  $p_{H} = p_{\gamma \gamma}$  for  $t\bar{t}\gamma \gamma$ ,  $p_{H} = p_{W}$  for  $t\bar{t}W$ , and  $p_{H} = p_{b\bar{b}}$  for  $t\bar{t}b\bar{b}$ . The events are generated at the parton-level following the setup described in section 2.1. All distributions are normalised to unity. We also show in each case the per-bin combined significance obtained for the  $t\bar{t}H$  sample at  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  in a lower panel plot.

![](images/9b5fb464defbd270fd521ca5e7ce4980e55680e7473ac89aaf9fef19d2af4329.jpg)  
Figure 12. Proposal for an extension of the current STXS binning for the  $t\bar{t}H$  production mode. Each bin in  $p_{T,H}$  is further split in bins of either  $b_2^{\mathrm{lab}}$ ,  $\Delta \eta_{tt}^{t\bar{t}}$ , or  $|\cos \theta^{*}|$ .

# 5.2 Proposal for  $t\bar{t}H$  STXS extension

The findings of our analysis are the following, considering as a benchmark the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  sample with  $300\mathrm{fb^{-1}}$  of data:

- The combination of  $p_{T,H}$  with  $\Delta \phi_{tt}^{\mathrm{lab}}$ ,  $b_1^{\mathrm{lab}}$ ,  $b_2^{\mathrm{lab}}$ ,  $\Delta \eta_{tt}^{t\overline{t}}$ , or  $|\cos \theta^*|$  feature compatible sensitivity within 5% of the best combination. We favour combinations with  $p_{T,H}$  due to the existing STXS binning.  
- When using the existing STXS binning in  $p_{T,H}$  (6 bins) adding any second observable composed of 6 bins with optimized boundaries, the two-dimensional combinations including  $p_{T,H}$  listed above yield compatible sensitivity.  
- If we compare these results with the sensitivity that we obtain from a multivariate analysis trained on all the observables introduced in section 2, a limited gain of  $16\%$  is found when using the multivariate analysis (after combining all channels).  
- A qualitative comparison of the main non-Higgs background shapes with respect to the significance in each of the tested bins shows that  $\Delta \phi_{tt}^{\mathrm{lab}}$  and  $b_1^{\mathrm{lab}}$  are disfavored. This leads to the exclusion of the respective combinations with  $p_{T,H}$ .  
- The final shortlist of candidate observables to be combined with  $p_{T,H}$  include  $b_2^{\mathrm{lab}}$ ,  $\Delta \eta_{tt}^{t\overline{t}}$  and  $|\cos \theta^{*}|$ . Our analysis provides no support to favour one over another.

Based on these findings, our final proposal is to extend the current STXS binning by a second dimension that could either be  $b_{2}^{\mathrm{lab}}, \Delta \eta_{tt}^{t\overline{t}}$ , or  $|\cos \theta^{*}|$ , as illustrated in figure 12.

![](images/9e4999a47cfd098db13f5b25bc17a05945c54fb374126cc6e638826c1efa0d3f.jpg)

![](images/23ae32c8a11653ec633faaba3982a815021a0833a906ca2ecf27dd34b63395a2.jpg)  
Figure 13. Constraints in the  $(g_t, \alpha_t)$  plane for (blue)  $\mathcal{L} = 300\mathrm{fb}^{-1}$  and (red)  $\mathcal{L} = 3000\mathrm{fb}^{-1}$  at the  $95\%$  CL using the one-dimensional  $p_{T,H}$  distribution — evaluated using 6 (dotted line) and 36 (dashed line) bins — as well as the two-dimensional  $(p_{T,H}, |\cos \theta^*|)$  distributions (solid line,  $6 \times 6$  bins). The contour for  $\mathcal{L} = 3000\mathrm{fb}^{-1}$  is shown alone on the right-hand side and together with the  $\mathcal{L} = 300\mathrm{fb}^{-1}$  contour on the left-hand side for better comparison.

![](images/648f42d7604533b5f4934ba5062b5d368e845365108ab3e6b88789dcdf137a31.jpg)

To further support our proposal, we show in figure 13 a comparison of the expected two-dimensional limits in the  $(g_{t},\alpha_{t})$  parameter space that we obtain from the current STXS binning for  $t\bar{t} H$  production, a finer one-dimensional binning including 36 bins, and our proposal taking the example of  $|\cos \theta^{*}|$  as the second observable. This comparison is shown for  $300\mathrm{fb}^{-1}$  and  $3000\mathrm{fb}^{-1}$  (without any other modification in the analysis). Although the  $3000\mathrm{fb}^{-1}$  scenario may be conservative as the moderate increase of center-of-mass energy from  $\sqrt{s} = 13\mathrm{TeV}$  to  $14\mathrm{TeV}$ , improved acceptance and potential systematic uncertainty reduction are not taken into account, it still shows that our proposal allows to improve the sensitivity of the STXS measurement in the longer term. The sensitivity improvement from the introduction of a second observable due to the improved kinematic shape discrimination with higher number of  $t\bar{t} H$  events goes up to  $+33\%$ $(+28\%)$ , reached at  $g_{t} = 1.24$  (1.08) for  $300\mathrm{fb}^{-1}$ $(3000\mathrm{fb}^{-1})$  of data. On the other hand, the introduction of more  $p_{T,H}$  bins lead to lower sensitivity improvements, going up to  $+24\%$ $(+15\%)$ , reached at  $g_{t} = 1.26$  (1.10) for  $300\mathrm{fb}^{-1}$ $(3000\mathrm{fb}^{-1})$  of data. $^{8}$

Our proposal for the extension of the STXS framework assumes a common definition of the top quark. This definition should guarantee the possibility to calculate higher-order loop corrections in a well-defined way. A pseudo-top-quark definition has already been worked out

in the context of the LHC Top Working Group [102]. We leave a study of the applicability of this definition to the  $t\bar{t}H$  process for future work.

# 6 Conclusion

$\mathcal{CP}$  violation in the Higgs sector is a possibility with far-reaching phenomenological and cosmological consequences such as for electroweak baryogenesis, which should be thoroughly explored. In this work, we focused on constraining the  $\mathcal{CP}$  structure of the top-Yukawa coupling via top-associated Higgs production. While multivariate analysis techniques allow to best exploit the experimental data, measurements of one- or two-dimensional contributions allow for a clearer reinterpretation of the data and an easier combination of different Higgs decay channels and across experiments. With this motivation, we have studied in this paper which combinations of observables are most sensitive to the  $\mathcal{CP}$  nature of the top-Yukawa coupling.

Our study considers eleven observables (in various reference frames) already identified as being  $\mathcal{CP}$ -sensitive in the literature. For the comparison of their performance, we investigated the three most important experimental channels measured at the LHC: the channel when the Higgs boson decays into two photons, the channel where the Higgs boson decays into a bottom quark and antiquark, and the  $t\bar{t}H$  events leading to multi-lepton final states. For each of these channels, we included detection effects and selection efficiencies to mimic the data efficiency and resolution from the experimental analysis results. Based on the resulting distributions, we evaluated the sensitivity of each (combination of) observable(s) to distinguish between a mixed  $\mathcal{CP}$  state of the top-Yukawa coupling and the SM case via the computation of significances based on a benchmark signal corresponding to  $g_{t} = 1$  and  $\alpha_{t} = 35^{\circ}$  and  $300\mathrm{fb}^{-1}$  of data. The best sensitivity is found for combinations of observables with the azimuthal angle difference between the top quarks,  $\Delta \phi_{t\bar{t}}$ , while combinations with the Higgs transverse momentum,  $p_{T,H}$ , show comparable performance.

With an extension of the current STXS v1.2 binning in  $p_{T,H}$  in mind, we selected five observables which have the highest sensitivity in combination with  $p_{T,H}$ :  $\Delta \phi_{t\bar{t}}$ ,  $b_1$  and  $b_2$  in the laboratory frame, and  $\Delta \eta_{t\bar{t}}$  and  $|\cos \theta^*|$  in the  $t\bar{t}$  frame (see section 2 for exact definitions). For these observables, we optimized the binning for the final sensitivity comparison with six bins per observable to match the number of bins used in the current STXS  $p_{T,H}$  binning. We found that all five observables show very similar performance when used in combination with  $p_{T,H}$ . As a comparison, we also trained a boosted decision tree with all variables considered in our study. Overall, we found that for  $300\mathrm{fb}^{-1}$  of data, the exclusion limits are only slightly improved with the multivariate approach over our best two-dimensional combinations of observables.

For the final selection of an observable combination, we also qualitatively investigated the behaviour of the various non-Higgs backgrounds. For  $\Delta \phi_{t\bar{t}}$  and  $b_{1}$ , we found enhanced backgrounds in the bins which are most sensitive to the  $\mathcal{CP}$  nature of the top-Yukawa interactions, which make these observables less favorable. This is not the case for  $\Delta \eta_{t\bar{t}}$ ,  $|\cos \theta^{*}|$ , and  $b_{2}$ . Their two-dimensional combinations with  $p_{T,H}$  constitute our final proposal for a  $\mathcal{CP}$ -sensitive STXS extension. Their sensitivities are very similar and the best choice likely depends on more specific analysis details not considered in this work. Finally, we

compared the expected limits in the  $(g_t, \alpha_t)$  plane obtained with the current STXS binning, an extended one-dimensional  $p_{T,H}$  binning, and our proposal. Both with  $300\mathrm{fb}^{-1}$  and  $3000\mathrm{fb}^{-1}$  of data, our proposal of two-dimensional binning exceeds the sensitivity of the other alternative STXS binning scenarios.

It is important to note that all the proposed STXS extensions in this work require the reconstruction of both top quarks per event. Therefore, a thorough discussion within the community is needed to agree beforehand on a common top-quark definition.

# Acknowledgments

We thank Sarah Heim and Frank Tackmann for helpful discussions. This work was supported by ANR PIA funding: ANR-20-IDEES-0002. H.B. acknowledges support from the Alexander von Humboldt foundation. E.F. and M.M. acknowledge funding via Germany's Excellence Strategy - EXC-2123 QuantumFrontiers - 390837967. E.F. also thanks the CERN TH Department for support during the initial phase of this project.

# A Supplementary parton-level distributions for  $t\bar{t} H$

# A.1 Higgs boson rest frame

The supplementary kinematic distributions for observables defined in the Higgs boson rest frame are shown in figure 14.

![](images/dcdd22e6e33959f33cd3ba00e1f89ee58ae6d237b445896a3be34b6167f04127.jpg)

![](images/caeb4b8e594708925ab68f2e1f7e51aaecdb256e8cde6d373482005f7202e555.jpg)

![](images/842094cf5935274f91a37987e59401a75c3b627a5723f17a03d80a5afd84ea95.jpg)

![](images/f5413164d18b5ffcce702633c4101c7908d7bb615640975fcfe74a1ed2818cd7.jpg)

![](images/236b15c1e5ee9039ef025fd705a7330fc9511e0c34d0f85459c2aa43adf6af3f.jpg)

![](images/659d0c08540f40ca8d1c9081d48a150000206096cfb58302e500f1efdbc89d67.jpg)  
Figure 14. Distributions of the observables defined in section 2 in the Higgs boson rest frame.  $ttH$  events generated at parton-level with  $g_{t} = 1$  and various values of  $\mathcal{CP}$  phase  $\alpha_{t}$  are considered following the event generation described in section 2.1. All distributions are normalised to unity.

![](images/84393a0cf2e3f376acacb46e23e4d91922130a88e4d1ee1bc979e8ed94821afa.jpg)

# A.2  $t\bar{t}$  rest frame

The supplementary kinematic distributions for observables defined in the  $t\bar{t}$  rest frame are shown in figure 15.

![](images/92ace679a1ae39b93e0adf4f49211214745d36b112b566ca4337386dbbab50fa.jpg)  
$\alpha_{t} = \begin{array}{ccccccccc}\hline & 0^{\circ} & 35^{\circ} & 45^{\circ} & 90^{\circ}\\ \hline \end{array}$

![](images/0a144518f0bbf628047339edfa39107def824870904d599a0cca700c33af7fe6.jpg)

![](images/a891735b291ee52fbcec14e7fea7a92b0fe6c15c23792d958689eaa0496d6f22.jpg)

![](images/c45609bf85c25faa9d7657010330f13ad7b6fbd93b2c2dd63b8104d4f6671a81.jpg)

![](images/d83b23a5d03c6a534f6ab4eb7c3bbdc27720f480364b7731e798a65762c15098.jpg)  
Figure 15. Distributions of the observables defined in section 2 in the  $t\bar{t}$  rest frame.  $t\bar{t}H$  events generated at parton-level with  $g_{t} = 1$  and various values of  $\mathcal{CP}$  phase  $\alpha_{t}$  are considered following the event generation described in section 2.1. All distributions are normalised to unity.

![](images/aad9ed6f021c947400795238802befe0a16129bbf960c4df03d3900a239e1344.jpg)

# A.3  $t\bar{t} H$  rest frame

The supplementary kinematic distributions for observables defined in the  $t\bar{t} H$  rest frame are shown in figure 16.

![](images/1cdcbdce2d492f9d60cc3f77dcfaea613cde75121804353ba9876f921da6873b.jpg)

![](images/bd537db8ff5ab62c4f62d4b397c6504cc4975e8c9b9b0702707eb553d2eb3224.jpg)

![](images/2281d5c5fdcea93a4729e3c05c675323189e6bc5e89a09c8a691cf4d3ae6ea0b.jpg)

![](images/27cb41e75d680fea505c33ad6da9abc5533eb01cca37829f5d91fe3bd0b6b298.jpg)

![](images/d595a89bb17ec2ff1e9a49679b50d7956d60bbebc2e186a984c877fcd5e7d6e6.jpg)

![](images/65909f1067fab0472031fdaa40430a1e2780fd09bfe30c13deca5f10f5a0bdb2.jpg)  
Figure 16. Distributions of the observables defined in section 2 in the  $t\bar{t}H$  rest frame.  $t\bar{t}H$  events generated at parton-level with  $g_{t} = 1$  and various values of  $\mathcal{CP}$  phase  $\alpha_{t}$  are considered following the event generation described in section 2.1. All distributions are normalised to unity.

![](images/ab875364bdbcf50ab5c60bb5cca7dcd38b2a5e358831e6d7d1dcf9ffdf97cf42.jpg)

# A.4 Impact of the  $\eta$  cut

![](images/f71da8e29bf4612c4b15f7431eef041c44bc0a8c8779ce3a360b3af84e393079.jpg)  
$\alpha_{t} = \mathrm{~~\textit~{~0^{\circ}~}\eta~cut~}$  0° no cut 90° no cut

![](images/7375d3225b2444a187acd6188e45898bd88aa64dc1e71735704cf6e7e5f54d83.jpg)  
Figure 17. Distributions of (left) the  $\phi_C$  and (right) the  $|\cos \theta^*|$  observables in the Higgs and  $t\bar{t}$  frame, respectively. The distributions without any cut (solid line) and requiring  $|\eta| < 2$  (dashed line) are shown for the  $\alpha_t = 0^\circ$  and  $90^\circ$  samples. All distributions are normalised to unity.

# B Full two-dimensional significance tables

The full two-dimensional significance tables for the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  sample are shown in figure 18 for the  $ttH(\rightarrow \gamma \gamma)$  channel, in figure 19 for the  $ttH$  (multilep.) channel, and in figure 20 for the  $ttH(\rightarrow bb)$  channel. The combined significances including the three channels are depicted in figure 21.

![](images/d0bc4b9ea06040843c6ad5bb7eeede4d10d59220967c256f189d3f1bce293ce6.jpg)  
Figure 18. Significances of the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  signal for the  $t\bar{t} H(\rightarrow \gamma \gamma)$  channel. The diagonal matrix elements show the significances obtained from single observables with default binning, while the off-diagonal matrix elements show the significances obtained from the combination of two observables. Only half of the histogram is filled to avoid repeating the same information.

![](images/89cf9d6a4ccac9594ec647fc183d23def7a0fd4cd0b6251875d53203b0f651e8.jpg)  
Figure 19. Significances of the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  signal for the  $t\bar{t}H$  (multilep.) channel. The diagonal matrix elements show the significances obtained from single observables with default binning, while the off-diagonal matrix elements show the significances obtained from the combination of two observables. Only half of the histogram is filled to avoid repeating the same information.

![](images/aa553f0877deca49024714f04ebd9a7e447a968c0a0fc3661c1ce071a9b63021.jpg)  
Figure 20. Significances of the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  signal for the  $t\bar{t} H(\rightarrow bb)$  channel. The diagonal matrix elements show the significances obtained from single observables with default binning, while the off-diagonal matrix elements show the significances obtained from the combination of two observables. Only half of the histogram is filled to avoid repeating the same information.

![](images/de633f7c60fd58324b609c299266a5382fae1d505cd376092bf93aaf8e2fb294.jpg)  
Figure 21. Combined significances of the  $g_{t} = 1$ ,  $\alpha_{t} = 35^{\circ}$  signal including the  $ttH(\rightarrow \gamma \gamma)$ ,  $ttH(\mathrm{multilep.})$  and  $ttH(\rightarrow bb)$  channels. The diagonal matrix elements show the significances obtained from single observables with default binning, while the off-diagonal matrix elements show the significances obtained from the combination of two observables. Only half of the histogram is filled to avoid repeating the same information.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] M.B. Gavela, P. Hernandez, J. Orloff and O. Pene, Standard model CP violation and baryon asymmetry, Mod. Phys. Lett. A 9 (1994) 795 [hep-ph/9312215] [INSPIRE].  
[2] P. Huet and E. Sather, Electroweak baryogenesis and standard model CP violation, Phys. Rev. D 51 (1995) 379 [hep-ph/9404302] [INSPIRE].

[3] A.G. Cohen, D.B. Kaplan and A.E. Nelson, Progress in electroweak baryogenesis, Ann. Rev. Nucl. Part. Sci. 43 (1993) 27 [hep-ph/9302210] [INSPIRE].  
[4] M. Trodden, Electroweak baryogenesis, Rev. Mod. Phys. 71 (1999) 1463 [hep-ph/9803479] [INSPIRE].  
[5] J.M. Cline, Baryogenesis, in the proceedings of the Les Houches Summer School - Session 86: Particle Physics and Cosmology: The Fabric of Spacetime, Les Houches, France, July 31 - August 25 (2006) [hep-ph/0609145] [INSPIRE].  
[6] D.E. Morrissey and M.J. Ramsey-Musolf, Electroweak baryogenesis, New J. Phys. 14 (2012) 125003 [arXiv:1206.2942] [INSPIRE].  
[7] G.A. White, A Pedagogical Introduction to Electroweak Baryogenesis [DOI:10.1088/978-1-6817-4457-5] [INSPIRE].  
[8] D. Bodeker and W. Buchmuller, Baryogenesis from the weak scale to the grand unification scale, Rev. Mod. Phys. 93 (2021) 035004 [arXiv:2009.07294] [INSPIRE].  
[9] ATLAS collaboration, Study of the spin and parity of the Higgs boson in diboson decays with the ATLAS detector, Eur. Phys. J. C 75 (2015) 476 [Erratum ibid. 76 (2016) 152] [arXiv:1506.05669] [INSPIRE].  
[10] ATLAS collaboration, Test of CP Invariance in vector-boson fusion production of the Higgs boson using the Optimal Observable method in the ditau decay channel with the ATLAS detector, Eur. Phys. J. C 76 (2016) 658 [arXiv:1602.04516] [INSPIRE].  
[11] CMS collaboration, Constraints on anomalous Higgs boson couplings using production and decay information in the four-lepton final state, Phys. Lett. B 775 (2017) 1 [arXiv:1707.00541] [INSPIRE].  
[12] CMS collaboration, Constraints on anomalous HVV couplings from the production of Higgs bosons decaying to  $\tau$  lepton pairs, Phys. Rev. D 100 (2019) 112002 [arXiv:1903.06973] [INSPIRE].  
[13] CMS collaboration, Measurements of the Higgs boson width and anomalous HVV couplings from on-shell and off-shell production in the four-lepton final state, Phys. Rev. D 99 (2019) 112003 [arXiv:1901.00174] [INSPIRE].  
[14] ATLAS collaboration, Test of CP invariance in vector-boson fusion production of the Higgs boson in the  $H\rightarrow \tau \tau$  channel in proton-proton collisions at  $s = 13\mathrm{TeV}$  with the ATLAS detector, Phys. Lett. B 805 (2020) 135426 [arXiv:2002.05315] [INSPIRE].  
[15] ATLAS collaboration, Constraints on Higgs boson properties using  $WW^{*}(\rightarrow e\nu \mu \nu)jj$  production in 36.1fb $^{-1}$  of  $\sqrt{s} = 13$  TeV pp collisions with the ATLAS detector, Eur. Phys. J. C 82 (2022) 622 [arXiv:2109.13808] [INSPIRE].  
[16] CMS collaboration, Constraints on anomalous Higgs boson couplings to vector bosons and fermions from the production of Higgs bosons using the  $\tau \tau$  final state, Phys. Rev. D 108 (2023) 032013 [arXiv:2205.05120] [INSPIRE].  
[17] ATLAS collaboration, Test of CP Invariance in Higgs Boson Vector-Boson-Fusion Production Using the  $H \to \gamma \gamma$  Channel with the ATLAS Detector, Phys. Rev. Lett. 131 (2023) 061802 [arXiv:2208.02338] [INSPIRE].  
[18] ATLAS collaboration, Test of CP-invariance of the Higgs boson in vector-boson fusion production and in its decay into four leptons, JHEP 05 (2024) 105 [arXiv:2304.09612] [INSPIRE].

[19] CMS collaboration, Measurements of ttH Production and the CP Structure of the Yukawa Interaction between the Higgs Boson and Top Quark in the Diphoton Decay Channel, Phys. Rev. Lett. 125 (2020) 061801 [arXiv:2003.10866] [INSPIRE].  
[20] ATLAS collaboration, CP Properties of Higgs Boson Interactions with Top Quarks in the  $ttH$  and  $tH$  Processes Using  $H \rightarrow \gamma \gamma$  with the ATLAS Detector, Phys. Rev. Lett. 125 (2020) 061802 [arXiv:2004.04545] [INSPIRE].  
[21] CMS collaboration, Analysis of the CP structure of the Yukawa coupling between the Higgs boson and  $\tau$  leptons in proton-proton collisions at  $\sqrt{s} = 13$  TeV, JHEP 06 (2022) 012 [arXiv:2110.04836] [INSPIRE].  
[22] CMS collaboration, Constraints on anomalous Higgs boson couplings to vector bosons and fermions in its production and decay using the four-lepton final state, Phys. Rev. D 104 (2021) 052004 [arXiv:2104.12152] [INSPIRE].  
[23] CMS collaboration, Search for CP violation in ttH and tH production in multilepton channels in proton-proton collisions at  $\sqrt{s} = 13$  TeV, JHEP 07 (2023) 092 [arXiv:2208.02686] [INSPIRE].  
[24] ATLAS collaboration, Measurement of the CP properties of Higgs boson interactions with  $\tau$ -leptons with the ATLAS detector, Eur. Phys. J. C 83 (2023) 563 [arXiv:2212.05833] [INSPIRE].  
[25] ATLAS collaboration, Probing the CP nature of the top-Higgs Yukawa coupling in  $tt^{-}H$  and tH events with  $H\rightarrow bb^{-}$  decays using the ATLAS detector at the LHC, Phys. Lett. B 849 (2024) 138469 [arXiv:2303.05974] [INSPIRE].  
[26] P. Artoisenet et al., A framework for Higgs characterisation, JHEP 11 (2013) 043 [arXiv:1306.6464] [INSPIRE].  
[27] E. Fuchs, M. Losada, Y. Nir and Y. Viernik,  $CP$  violation from  $\tau$ ,  $t$  and  $b$  dimension-6 Yukawa couplings - interplay of baryogenesis, EDM and Higgs physics, JHEP 05 (2020) 056 [arXiv:2003.00099] [INSPIRE].  
[28] S. Aharony Shapira, Current bounds on baryogenesis from complex Yukawa couplings of light fermions, Phys. Rev. D 105 (2022) 095037 [arXiv:2106.05338] [INSPIRE].  
[29] T.S. Roussy et al., An improved bound on the electron's electric dipole moment, Science 381 (2023) adg4084 [arXiv:2212.11841] [INSPIRE].  
[30] C. Abel et al., Measurement of the Permanent Electric Dipole Moment of the Neutron, Phys. Rev. Lett. 124 (2020) 081803 [arXiv:2001.11966] [INSPIRE].  
[31] J. Brod, U. Haisch and J. Zupan, Constraints on CP-violating Higgs couplings to the third generation, JHEP 11 (2013) 180 [arXiv:1310.1385] [INSPIRE].  
[32] J. Brod, J.M. Cornell, D. Skodras and E. Stamou, Global constraints on Yukawa operators in the standard model effective theory, JHEP 08 (2022) 294 [arXiv:2203.03736] [INSPIRE].  
[33] W. Altmannshofer, J. Brod and M. Schmaltz, Experimental constraints on the coupling of the Higgs boson to electrons, JHEP 05 (2015) 125 [arXiv:1503.04830] [INSPIRE].  
[34] ATLAS collaboration, Search for the Higgs boson decays  $H \rightarrow ee$  and  $H \rightarrow e\mu$  in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, Phys. Lett. B 801 (2020) 135148 [arXiv:1909.10235] [INSPIRE].  
[35] Y. Zhou, Constraining the Higgs boson coupling to light quarks in the  $H\rightarrow ZZ$  final states, Phys. Rev. D 93 (2016) 013019 [arXiv:1505.06369] [INSPIRE].

[36] Y. Soreq, H.X. Zhu and J. Zupan, Light quark Yukawa couplings from Higgs kinematics, JHEP 12 (2016) 045 [arXiv:1606.09621] [INSPIRE].  
[37] G. Bonner and H.E. Logan, Constraining the Higgs couplings to up and down quarks using production kinematics at the CERN Large Hadron Collider, arXiv:1608.04376 [INSPIRE].  
[38] F. Yu, Phenomenology of Enhanced Light Quark Yukawa Couplings and the  $W^{\pm}h$  Charge Asymmetry, JHEP 02 (2017) 083 [arXiv:1609.06592] [INSPIRE].  
[39] L. Alasfar, R. Corral Lopez and R. Gröber, Probing Higgs couplings to light quarks via Higgs pair production, JHEP 11 (2019) 088 [arXiv:1909.05279] [INSPIRE].  
[40] J.A. Aguilar-Saavedra, J.M. Cano and J.M. No, More light on Higgs flavor at the LHC: Higgs boson couplings to light quarks through  $h + \gamma$  production, Phys. Rev. D 103 (2021) 095023 [arXiv:2008.12538] [INSPIRE].  
[41] A. Falkowski et al., Light quark Yukawas in triboson final states, JHEP 04 (2021) 023 [arXiv:2011.09551] [INSPIRE].  
[42] N. Vignaroli, Off-Shell Probes of the Higgs Yukawa Couplings: Light Quarks and Charm, Symmetry 14 (2022) 1183 [arXiv:2205.09449] [INSPIRE].  
[43] E. Balzani, R. Gröber and M. Vitti, Light-quark Yukawa couplings from off-shell Higgs production, JHEP 10 (2023) 027 [arXiv:2304.09772] [INSPIRE].  
[44] A. Freitas and P. Schwaller, Higgs CP Properties From Early LHC Data, Phys. Rev. D 87 (2013) 055014 [arXiv:1211.1980] [INSPIRE].  
[45] P. Agrawal, S. Mitra and A. Shivaji, Effect of Anomalous Couplings on the Associated Production of a Single Top Quark and a Higgs Boson at the LHC, JHEP 12 (2013) 077 [arXiv:1211.4362] [INSPIRE].  
[46] A. Djouadi and G. Moreau, The couplings of the Higgs boson and its CP properties from fits of the signal strengths and their ratios at the  $7 + 8$  TeV LHC, Eur. Phys. J. C 73 (2013) 2512 [arXiv:1303.6591] [INSPIRE].  
[47] J. Ellis, D.S. Hwang, K. Sakurai and M. Takeuchi, Disentangling Higgs-Top Couplings in Associated Production, JHEP 04 (2014) 004 [arXiv:1312.5736] [INSPIRE].  
[48] J. Chang, K. Cheung, J.S. Lee and C.-T. Lu, Probing the Top-Yukawa Coupling in Associated Higgs production with a Single Top Quark, JHEP 05 (2014) 062 [arXiv:1403.2053] [INSPIRE].  
[49] X.-G. He, G.-N. Li and Y.-J. Zheng, Probing Higgs boson CP Properties with  $t\bar{t}H$  at the LHC and the 100 TeV pp collider, Int. J. Mod. Phys. A 30 (2015) 1550156 [arXiv:1501.00012] [INSPIRE].  
[50] F. Boudjema, R.M. Godbole, D. Guadagnoli and K.A. Mohan, Lab-frame observables for probing the top-Higgs interaction, Phys. Rev. D 92 (2015) 015019 [arXiv:1501.03157] [INSPIRE].  
[51] F. Demartin, F. Maltoni, K. Mawatari and M. Zaro, Higgs production in association with a single top quark at the LHC, Eur. Phys. J. C 75 (2015) 267 [arXiv:1504.00611] [INSPIRE].  
[52] F. Demartin et al., tWH associated production at the LHC, Eur. Phys. J. C 77 (2017) 34 [arXiv:1607.05862] [INSPIRE].  
[53] A. Kobakhidze, N. Liu, L. Wu and J. Yue, Implications of CP-violating Top-Higgs Couplings at LHC and Higgs Factories, Phys. Rev. D 95 (2017) 015016 [arXiv:1610.06676] [INSPIRE].  
[54] W.-S. Hou, M. Kohda and T. Modak, Probing for extra top Yukawa couplings in light of  $t\bar{t}h(125)$  observation, Phys. Rev. D 98 (2018) 075007 [arXiv:1806.06018] [INSPIRE].

[55] Q.-H. Cao et al., Limiting top quark-Higgs boson interaction and Higgs-boson width from multitop productions, Phys. Rev. D 99 (2019) 113003 [arXiv:1901.04567] [INSPIRE].  
[56] H. Bahl et al., Indirect  $\mathcal{CP}$  probes of the Higgs-top-quark interaction: current LHC constraints and future opportunities, JHEP 11 (2020) 127 [arXiv:2007.08542] [INSPIRE].  
[57] H. Bahl et al., Constraining the  $\mathcal{CP}$  structure of Higgs-fermion couplings with a global LHC fit, the electron EDM and baryogenesis, Eur. Phys. J. C 82 (2022) 604 [arXiv:2202.11753] [INSPIRE].  
[58] H. Bahl, E. Fuchs, M. Hannig and M. Menen, Classifying the CP properties of the ggH coupling in  $H + 2j$  production, arXiv:2309.03146 [INSPIRE].  
[59] N. Mileo et al., Pseudoscalar top-Higgs coupling: exploration of CP-odd observables to resolve the sign ambiguity, JHEP 07 (2016) 056 [arXiv:1603.03632] [INSPIRE].  
[60] D.A. Faroughy, J.F. Kamenik, N. Košnik and A. Smolkovič, Probing the CP nature of the top quark Yukawa at hadron colliders, JHEP 02 (2020) 085 [arXiv:1909.00007] [INSPIRE].  
[61] B. Bortolato, J.F. Kamenik, N. Košnik and A. Smolkovič, Optimized probes of  $CP$ -odd effects in the  $t\overline{t}h$  process at hadron colliders, Nucl. Phys. B 964 (2021) 115328 [arXiv:2006.13110] [INSPIRE].  
[62] D. Gonçalves, J.H. Kim, K. Kong and Y. Wu, Direct Higgs-top CP-phase measurement with  $t\bar{t}h$  at the 14 TeV LHC and 100 TeV FCC, JHEP 01 (2022) 158 [arXiv:2108.01083] [INSPIRE].  
[63] R.K. Barman, D. Gonçalves and F. Kling, Machine learning the Higgs boson-top quark CP phase, Phys. Rev. D 105 (2022) 035023 [arXiv:2110.07635] [INSPIRE].  
[64] D. Azevedo, R. Capucha, A. Onofre and R. Santos,  $CP$ -violation, asymmetries and interferences in  $t\bar{t}\phi$ , JHEP 09 (2022) 246 [arXiv:2208.04271] [INSPIRE].  
[65] J. Ackerschott et al., Returning CP-observables to the frames they belong, SciPost Phys. 17 (2024) 001 [arXiv:2308.00027] [INSPIRE].  
[66] CMS collaboration, Observation of ttH production, Phys. Rev. Lett. 120 (2018) 231801 [arXiv:1804.02610] [INSPIRE].  
[67] ATLAS collaboration, Observation of Higgs boson production in association with a top quark pair at the LHC with the ATLAS detector, Phys. Lett. B 784 (2018) 173 [arXiv:1806.00425] [INSPIRE].  
[68] J. Ren, L. Wu and J.M. Yang, Unveiling CP property of top-Higgs coupling with graph neural networks at the LHC, Phys. Lett. B 802 (2020) 135198 [arXiv:1901.05627] [INSPIRE].  
[69] H. Bahl and S. Brass, Constraining  $\mathcal{CP}$ -violation in the Higgs-top-quark interaction using machine-learning-based inference, JHEP 03 (2022) 017 [arXiv:2110.10177] [INSPIRE].  
[70] W. Esmail, A. Hammad, A. Jueid and S. Moretti, Boosting probes of CP violation in the top Yukawa coupling with Deep Learning, arXiv:2405.16499 [INSPIRE].  
[71] T. Martini, R.-Q. Pan, M. Schulze and M. Xiao, Probing the CP structure of the top quark Yukawa coupling: Loop sensitivity versus on-shell sensitivity, Phys. Rev. D 104 (2021) 055045 [arXiv:2104.04277] [INSPIRE].  
[72] M. Kraus, T. Martini, S. Peitzsch and P. Uwer, Exploring BSM Higgs couplings in single top-quark production, arXiv:1908.09100 [INSPIRE].  
[73] A.V. Gritsan, R. Röntsch, M. Schulze and M. Xiao, Constraining anomalous Higgs boson couplings to the heavy flavor fermions using matrix element techniques, Phys. Rev. D 94 (2016) 055023 [arXiv:1606.03107] [INSPIRE].

[74] D. Gonçalves, K. Kong and J.H. Kim, Probing the top-Higgs Yukawa CP structure in dileptonic  $t\bar{t}h$  with  $M_2$ -assisted reconstruction, JHEP 06 (2018) 079 [arXiv:1804.05874] [INSPIRE].  
[75] A. Butter et al., Two invertible networks for the matrix element method, SciPost Phys. 15 (2023) 094 [arXiv:2210.00019] [INSPIRE].  
[76] A.V. Gritsan et al., Snowmass White Paper: Prospects of CP-violation measurements with the Higgs boson at future experiments, arXiv:2205.07715 [INSPIRE].  
[77] LHC HIGGS CROSS SECTION WORKING GROUP collaboration, Handbook of LHC Higgs Cross Sections: 4. Deciphering the Nature of the Higgs Sector, arXiv:1610.07922 [DOI:10.23731/CYRM-2017-002] [INSPIRE].  
[78] J.R. Andersen et al., Les Houches 2015: Physics at TeV Colliders Standard Model Working Group Report, in the proceedings of the 9th Les Houches Workshop on Physics at TeV Colliders, Les Houches, France, June 01–19 (2015) [arXiv:1605.04692] [INSPIRE].  
[79] N. Berger et al., Simplified Template Cross Sections - Stage 1.1, arXiv:1906.02754 [INSPIRE].  
[80] S. Amoroso et al., Les Houches 2019: Physics at TeV Colliders: Standard Model Working Group Report, in the proceedings of the 11th Les Houches Workshop on Physics at TeV Colliders: PhysTeV Les Houches, Les Houches, France, June 10-28 (2019) [arXiv:2003.01700] [INSPIRE].  
[81] S. Grossi and R. Torre, More variables or more bins? Impact on the EFT interpretation of Drell-Yan measurements, Eur. Phys. J. C 84 (2024) 713 [arXiv:2404.10569] [INSPIRE].  
[82] J.F. Gunion and X.-G. He, Determining the CP nature of a neutral Higgs boson at the LHC, Phys. Rev. Lett. 76 (1996) 4468 [hep-ph/9602226] [INSPIRE].  
[83] J. Yue, Enhanced thj signal at the LHC with  $h \to \gamma \gamma$  decay and  $\mathcal{CP}$ -violating top-Higgs coupling, Phys. Lett. B 744 (2015) 131 [arXiv:1410.2701] [INSPIRE].  
[84] F. Demartin et al., Higgs characterisation at NLO in QCD: CP properties of the top-quark Yukawa interaction, Eur. Phys. J. C 74 (2014) 3065 [arXiv:1407.5089] [INSPIRE].  
[85] M.R. Buckley and D. Goncalves, Boosting the Direct CP Measurement of the Higgs-Top Coupling, Phys. Rev. Lett. 116 (2016) 091801 [arXiv:1507.07926] [INSPIRE].  
[86] D. Azevedo, A. Onofre, F. Filthaut and R. Gonçalo, CP tests of Higgs couplings in  $t$ th semileptonic events at the LHC, Phys. Rev. D 98 (2018) 033004 [arXiv:1711.05292] [INSPIRE].  
[87] Q.-H. Cao, K.-P. Xie, H. Zhang and R. Zhang, A New Observable for Measuring CP Property of Top-Higgs Interaction, Chin. Phys. C 45 (2021) 023117 [arXiv:2008.13442] [INSPIRE].  
[88] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections, and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[89] R.D. Ball et al., Parton distributions with LHC data, Nucl. Phys. B 867 (2013) 244 [arXiv:1207.1303] [INSPIRE].  
[90] T. Sjöstrand et al., An introduction to PYTHIA 8.2, Comput. Phys. Commun. 191 (2015) 159 [arXiv:1410.3012] [INSPIRE].  
[91] J.C. Collins and D.E. Soper, Angular Distribution of Dileptons in High-Energy Hadron Collisions, Phys. Rev. D 16 (1977) 2219 [INSPIRE].  
[92] ATLAS collaboration, The ATLAS Experiment at the CERN Large Hadron Collider, 2008 JINST 3 S08003 [INSPIRE].  
[93] CMS collaboration, The CMS Experiment at the CERN LHC, 2008 JINST 3 S08004 [INSPIRE].

[94] ATLAS collaboration, Electron and photon energy calibration with the ATLAS detector using LHC Run 1 data, Eur. Phys. J. C 74 (2014) 3071 [arXiv:1407.5063] [INSPIRE].  
[95] ATLAS collaboration, Measurement of Higgs boson decay into  $b$ -quarks in associated production with a top-quark pair in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, JHEP 06 (2022) 097 [arXiv:2111.06712] [INSPIRE].  
[96] ATLAS collaboration, Measurement of the charge asymmetry in top quark pair production in pp collisions at  $\sqrt{s} = 7$  TeV using the ATLAS detector, Eur. Phys. J. C 72 (2012) 2039 [arXiv:1203.4211] [INSPIRE].  
[97] ATLAS collaboration, Measurements of top-quark pair differential and double-differential cross-sections in the  $\ell +$  jets channel with pp collisions at  $\sqrt{s} = 13$  TeV using the ATLAS detector, Eur. Phys. J. C 79 (2019) 1028 [Erratum ibid. 80 (2020) 1092] [arXiv:1908.07305] [INSPIRE].  
[98] ATLAS collaboration, Formulae for Estimating Significance, ATL-PHYS-PUB-2020-025, CERN, Geneva (2020).  
[99] T. Chen and C. Guestrin, XGBoost: A Scalable Tree Boosting System, arXiv:1603.02754 [DOI:10.1145/2939672.2939785] [INSPIRE].  
[100] E.M. Metodiev, B. Nachman and J. Thaler, Classification without labels: Learning from mixed samples in high energy physics, JHEP 10 (2017) 174 [arXiv:1708.02949] [INSPIRE].  
[101] S. Raschka, Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning, arXiv:1811.12808.  
[102] LHC working group on Top Quark physics, Particle level objects and pseudo-top-quark definitions, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/ParticleLevelTopDefinitions.