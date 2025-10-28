# CP-violation, asymmetries and interferences in  $t\bar{t}\phi$

Duarte Azevedo, $^{a,b}$  Rodrigo Capucha, $^{c}$  Antonio Onofre $^{d}$  and Rui Santos $^{e,e}$

$^{a}$  Institute for Theoretical Physics, Karlsruhe Institute of Technology, 76128 Karlsruhe, Germany  
$^{b}$ Institute for Astroparticle Physics, Karlsruhe Institute of Technology, 76344 Karlsruhe, Germany  
<sup>c</sup>Centro de Física Teórica e Computacional, Faculdade de Ciências, Universidade de Lisboa, Campo Grande, Edifácio C8 1749-016 Lisboa, Portugal  
$^{d}$ Departamento de Física, Universidade do Minho, 4710-057 Braga, Portugal  
$^{e}$ ISEL — Instituto Superior de Engenharia de Lisboa, Instituto Politécnico de Lisboa 1959-007 Lisboa, Portugal

E-mail: duarte.azevedo@kit.edu, rscapucha@fc.ul.pt, antonio.onofre@cern.ch, rasantos@fc.ul.pt

ABSTRACT: In this paper, we use the associated production of top-quark pairs  $(tt)$  with a generic scalar boson  $(\phi)$  at the LHC  $(pp\rightarrow tt\bar{\phi})$  to explore the sensitivity of a large set of observables to the sign of the CP mixing angle  $(\alpha)$ , present in the coupling between the scalar boson and the top quarks. The mass of the scalar boson is set to  $m_{\phi} = 125\mathrm{GeV}$  (the Standard Model Higgs boson mass) and its coupling to top-quarks is varied such that  $\alpha = 0^{\circ}$ ,  $22.5^{\circ}$ ,  $45.0^{\circ}$ ,  $67.5^{\circ}$ ,  $90.0^{\circ}$ ,  $135.0^{\circ}$  and  $180.0^{\circ}$ . Dileptonic final states of the  $t\bar{t}\phi$  system are used  $(pp\rightarrow b\ell^{+}\nu_{\ell}\bar{b}\ell^{-}\bar{\nu}_{\ell}b\bar{b})$ , where the scalar boson is expected to decay according to  $\phi \rightarrow b\bar{b}$ . A new method to reconstruct the scalar mass, originally designed for the low mass regime is used, improving the resolution of the Higgs mass by roughly a factor of two. A full phenomenological analysis is performed using Standard Model (SM) background and signal events generated with MadGraph5_aMC@NLO, in turn reconstructed using a kinematical fit. The most sensitive CP-observables are selected to compute Confidence Level (CL) limits as a function of the sign of the top quark Yukawa couplings to the  $\phi$  boson. We also explore the sensitivity to interference terms using differential distributions and angular asymmetries. Given the significant difference between the pure scalar  $(\sigma_{0^{+}})$  and pure pseudo-scalar  $(\sigma_{0^{-}})$  production cross section values, it is unlikely the  $t\bar{t}\phi$  channel alone will be sensitive to the sign of the CP-mixing angle or interference terms, even at the end of the LHC. Using the  $b_2^{t\bar{t}\phi}$  and  $b_4^{t\bar{t}\phi}$  variables, exclusion limits at  $95\%$  CL for the CP-even and CP-odd components

of the top quark Yukawa couplings are expected to be set to  $\tilde{\kappa} \in [-0.698, +0.698]$  and  $|\kappa| \in [0.878, 1.04]$ , respectively, at the end of the High Luminosity phase of the LHC (HL-LHC) by using the dileptonic decay channel alone.

KEYWORDS: CP Violation, Multi-Higgs Models

ARXIV EPRINT: 2208.04271

# Contents

1 Introduction 1  
2 CP-observables 3  
3 Differential cross sections and interference term 5  
4 Event generation, selection and kinematic reconstruction 7  
5 Results and discussion 10  
6 Conclusions 18

# 1 Introduction

As first discussed by Sakharov [1], new sources of CP-violation are needed to explain the matter anti-matter asymmetry observed in the Universe. The CP-nature of the 125 GeV Higgs boson needs to be scrutinised and the study of its couplings to fermions and gauge bosons at the Large Hadron Collider (LHC) and future colliders is of the utmost importance. The observation of any deviation from the CP number predicted by the Standard Model (SM) would open doors to extended scalar sectors which easily provide new sources of CP-violation. Therefore, the search for Beyond the Standard Model (BSM) physics, particularly in the Higgs Yukawa couplings, should be a primary target of the next LHC run.

It is ever more likely that the Higgs boson discovered 10 years ago [2, 3] by the ATLAS and CMS collaborations has couplings to the remaining SM particles that resemble very much the ones predicted by the SM. It was already settled experimentally that the  $125\mathrm{GeV}$  Higgs is not a pure pseudoscalar state with a  $99\%$  confidence level (CL). However, it is also well-known that a significant CP-odd component is still possible even in very simple extensions of the SM as is the case of the CP-violating version of the two-Higgs doublet model (2HDM). Usually referred to as C2HDM [4-17], it has been used extensively as a benchmark model in many phenomenological studies. In particular, it was shown that in the C2HDM the CP-odd component of the Yukawa couplings can be varied independently for up-type quarks, down-type quarks and leptons [14]. This in turn means that a dedicated study for each fermion type is needed. The ratio between the CP-even and the CP-odd component of the Yukawa couplings can in principle be probed at tree-level both in the production and decays of these scalars. However, the proposals that were actually turned into experimental analysis are only the ones for the top quark [18-21], in the  $\bar{t} t\phi$  production channel and for the tau lepton [22-26] in the decay channel. ATLAS and CMS have studied the CP-nature of the  $125\mathrm{GeV}$  Higgs boson in these two channels. With the two photon final state channel of a Higgs boson produced in association with top quarks,  $pp\rightarrow \bar{t} t(H\rightarrow \gamma \gamma)$ ,

ATLAS and CMS [27, 28] excluded the pure CP-odd hypothesis at  $3.9\sigma$  and obtained a  $95\%$  CL observed (expected) exclusion upper limit for the CP mixing angle of  $43^{\circ}$ $(63^{\circ})$ . The first measurement of the tau lepton CP mixing angle was performed by CMS [29] using  $\sqrt{s} = 13\mathrm{TeV}$  data with an integrated luminosity of  $137\mathrm{fb}^{-1}$ . The measurement yielded a CP mixing angle of  $4^{\circ} \pm 17^{\circ}$ , and an observed (expected) exclusion upper limit of  $36^{\circ}$ $(55^{\circ})$ .

Besides the top-quark and tau-lepton Yukawa couplings, the only theoretical studies available for the remaining fermions are for the b-quark. The direct observation via the production mode  $pp \rightarrow \bar{b} b\phi$  was discussed in [30, 31] showing that it will be extremely hard to repeat what was done successfully for the top quark. As for the b-quark decays, the authors of [32] discussed the prospects for probing the CP structure in the  $\bar{b} b\phi$  and  $\bar{c} c\phi$  vertices by measuring the heavy-quark polarization from the hadronization to the lightest flavoured baryons  $(\Lambda_q)$ , which preserves the original quark spin in the infinite-mass limit because it decays weakly. They showed that only at a future muon collider would we have some chance of having sensitivity to those vertices. The study of the  $\bar{b} b\phi$  using kinematic shapes was performed in [33]. Note that contrary to CP-violation in the Yukawa couplings which is a tree-level process, even for a simple model like the C2HDM, CP-violation in the gauge couplings is a higher order process that has to be measured indirectly. Just considering as an example the most general  $W^{+}W^{-}\phi$  vertex it was shown in [34], using the C2HDM as benchmark, that even at the high luminosity stage of the LHC it will be very unlikely to have sensitivity to the CP-violating operator of the  $W^{+}W^{-}\phi$  vertex.

The different possible approaches for probing CP-violating couplings from loop processes involving gauge bosons was recently discussed in [35]. It was also examined in detail the origing of CP violation in the Lagrangian: Yukawa couplings stems from P-violation while CP violation coming from C violation has its origin in the scalar sector. In the latter scenario, probing CP violation would imply resourcing to a combination of three decays that would only make sense if new scalars were found. Finally, very recently it was shown in [36] that attention must be paid to both NLO corrections and off-shell effects because they play an important role in the observables that are used to determine the CP nature of the Higgs in its Yukawa couplings.

In this paper, we use the associated production of top-quark pairs with a generic scalar boson at the LHC ( $pp \rightarrow t\bar{t}\phi$ ) to explore the sensitivity of a large set of observables to the sign of the CP-odd component (reflected on the values of the mixing angle  $\alpha$ ), present in the coupling between the scalar boson and the top quarks. Over the years we have not only proposed a number of new variables to probe CP-violation in this channel but we have also tested the most relevant ones present in the literature. $^1$  With this knowledge we have now combined these variables in order to extract the best possible limit on the CP-odd component of the scalar. Although previous papers have discussed how to probe the sign of the CP-odd component of the Yukawa coupling via the mixing angle  $\alpha$  [39-41] a proper analysis at detector level with the main backgrounds included was never performed. Therefore, we will present for the first time a study that include all available variables in

the literature and that also discusses the interference terms. The Higgs boson mass is set to  $m_{\phi} = 125 \, \mathrm{GeV}$  and dileptonic final states of the  $t\bar{t}\phi$  system are used ( $pp \to b\ell^{+}\nu_{\ell}\bar{b}\ell^{-}\bar{\nu}_{\ell}b\bar{b}$ ), with  $\phi \to b\bar{b}$ . A new method to reconstruct the scalar mass, originally designed for the low mass regime is used, improving the resolution of the Higgs mass by roughly a factor of two [31]. A full phenomenological analysis is performed using SM background and signal events generated with MadGraph5_aMC@NLO, in turn reconstructed using a kinematical fit.

The paper is organized as follows. The different CP-observables are presented in section 2. The differential production cross sections for the various CP signals and the interference terms, are discussed in section 3. The event generation, selection and kinematic reconstruction are presented in section 4 and the results are analysed in section 5. Our main conclusions are presented in section 6.

# 2 CP-observables

The most general top quark-Higgs interaction can be parameterized as

$$
\mathcal {L} = \kappa_ {t} y _ {t} \bar {t} (\cos \alpha + i \gamma_ {5} \sin \alpha) t \phi = y _ {t} \bar {t} (\kappa + i \gamma_ {5} \tilde {\kappa}) t \phi , \tag {2.1}
$$

where the real parameter  $\kappa_{t}$  describes the magnitude of the coupling strength with respect to the SM and  $\alpha$  is the CP-mixing angle. The last part of the previous expression is another parameterization of the same coupling, the mapping between them given by  $\kappa = \kappa_{t}\cos \alpha$  and  $\tilde{\kappa} = \kappa_{t}\sin \alpha$ . For the SM hypothesis, i.e. the CP-even case ( $\phi = H$ ), we fix  $\kappa_{t} = 1$  and  $\alpha = 0^{\circ}$ . Alternatively, for the CP-odd case ( $\phi = A$ ), we consider  $\alpha = 90.0^{\circ}$ . The Yukawa coupling strength of the top quark to the SM-Higgs boson is given by  $y_{t} = \sqrt{2} m_{t} / v$ , proportional to the top quark mass ( $m_{t}$ ) and the electroweak vacuum expectation value  $v$ .

Several CP-observables have been proposed and discussed in the literature to probe the CP-nature of the top-Higgs couplings at the LHC or future colliders, using mainly the  $t\bar{t}\phi$  production channel [18-21, 31, 39-65]. These observables can be sensitive to the nature of the coupling but also allow discrimination of scalar boson signals from irreducible backgrounds at the LHC. Moreover, it has been shown that some of these observables can be used to explore the CP nature of Higgs bosons with masses ranging from 12 GeV to 500 GeV [31, 60]. The vast majority of these variables are only sensitive to the square terms  $\kappa^2$  and  $\tilde{\kappa}^2$  that appear in the cross section of the interaction described in eq. (2.1), missing the interference term between the CP-even and CP-odd couplings (proportional to  $\kappa \tilde{\kappa}$ ). We define these observables as CP-even, as they are invariant under a CP-transformation and, in particular, they are not sensitive to the relative sign of the CP-phase  $\alpha$ . In this paper, from all variables considered, we show results for only a few most sensitive CP-even variables like the  $b_2^{t\bar{t}\phi}$  and  $b_4^{t\bar{t}\phi}$  defined in the  $t\bar{t}\phi$  centre-of-mass (CM) frame [58] according to

$$
b _ {2} ^ {t \bar {t} \phi} = (\vec {p _ {t}} \times \hat {k} _ {z}). (\vec {p _ {\bar {t}}} \times \hat {k} _ {z}) / (| \vec {p _ {t}} |. | \vec {p _ {\bar {t}}} |) \quad \text {a n d} \quad b _ {4} ^ {t \bar {t} \phi} = (p _ {\tilde {t}} ^ {z}. p _ {\tilde {t}} ^ {z}) / (| \vec {p _ {t}} |. | \vec {p _ {\bar {t}}} |) \tag {2.2}
$$

where  $\vec{p}_{t(\bar{t})}$  and  $p_{t(\bar{t})}^z$ , correspond to the total and  $z$ -component of the top (anti-top) quark momentum measured in the  $t\bar{t}\phi$  centre-of-mass system. The beam line direction defines the unit vector  $\hat{k}_z$ . It is worth noting that  $b_2^{t\bar{t}\phi}$  and  $b_4^{t\bar{t}\phi}$  have a natural physics interpretation

Table 1. Asymmetries for the  $t\bar{t}\phi$  signal as a function of the mixing angle  $\alpha$ , as well as for the dominant background  $t\bar{t}b\bar{b}$  at NLO+Shower (without any cuts), are shown for several observables. Significant differences between the asymmetries for the pure scalar  $(\alpha = 0.0^{\circ})$  and pseudo-scalar  $(\alpha = 90.0^{\circ})$  cases are observed for several asymmetries.  

<table><tr><td rowspan="2">Asymmetries</td><td rowspan="2">xc</td><td colspan="8">MadGraph5 @ NLO+Shower (no cuts applied) tbarφ signal mixing angle α (deg.)</td></tr><tr><td>0.0°</td><td>22.5°</td><td>45.0°</td><td>67.5°</td><td>90.0°</td><td>135.0°</td><td>180.0°</td><td>tbarbbar</td></tr><tr><td>Ac[b2tbarφ]</td><td>-0.30</td><td>-0.35</td><td>-0.31</td><td>-0.15</td><td>+0.15</td><td>+0.34</td><td>-0.14</td><td>-0.36</td><td>-0.17</td></tr><tr><td>Ac[b4tbarφ]</td><td>-0.50</td><td>+0.41</td><td>+0.37</td><td>+0.22</td><td>-0.04</td><td>-0.22</td><td>+0.22</td><td>+0.41</td><td>+0.33</td></tr><tr><td>Ac[sin(θφtbarφ) * sin(θbarτ)]</td><td>+0.70</td><td>-0.27</td><td>-0.26</td><td>-0.20</td><td>-0.09</td><td>-0.03</td><td>-0.20</td><td>-0.27</td><td>-0.56</td></tr><tr><td>Ac[sin(θφtbarφ) * sin(θbarbbar)]</td><td>+0.60</td><td>+0.05</td><td>+0.05</td><td>+0.07</td><td>+0.09</td><td>+0.11</td><td>+0.06</td><td>+0.05</td><td>-0.38</td></tr><tr><td>(seq. boost)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

since they only consider the information of the transverse  $p_{t(\bar{t})}^T$  (in  $b_2^{t\bar{t}\phi}$ ) and longitudinal  $p_{t(\bar{t})}^z$  (in  $b_4^{t\bar{t}\phi}$ ) components of the  $t(\bar{t})$  momentum, measured in the  $t\bar{t}\phi$  system, normalized to the  $t(\bar{t})$  total momentum. As these components depend on the  $t$  and  $\bar{t}$  polar angles with respect to the  $z$ -direction,  $\theta_t$  and  $\theta_{\bar{t}}$ , and on the azimuthal angle difference between the top quarks  $\Delta \phi_{t\bar{t}}$ , they can simply be expressed as  $b_{2} = \cos \Delta \phi_{t\bar{t}}\times \sin \theta_{t}\times \sin \theta_{\bar{t}}$  and  $b_{4} = \cos \theta_{t}\times \cos \theta_{\bar{t}}$ , i.e. as a function of angular distributions alone. Furthermore, we will consider two additional variables

$$
\sin \left(\theta_ {\phi} ^ {t \bar {t} \phi}\right) * \sin \left(\theta_ {\bar {t}} ^ {t \bar {t}}\right), \quad \sin \left(\theta_ {\phi} ^ {t \bar {t} \phi}\right) * \sin \left(\theta_ {\bar {b} _ {\bar {t}}} ^ {\bar {t}}\right) (\text {s e q . b o o s t}), \tag {2.3}
$$

where  $\theta_{Y}^{X}$  is the angle between the direction of the  $Y$  system 3-momentum (in the rest frame of  $X$ ) with respect to the momentum direction of the  $X$  system (in the rest frame of its parent system), as defined in [20, 21]. Angular asymmetries associated to each one of the observables in eqs. (2.2) and (2.3), are defined following [20],

$$
A _ {c} [ Z ] = \frac {\sigma (Z > x _ {c}) - \sigma (Z <   x _ {c})}{\sigma (Z > x _ {c}) + \sigma (Z <   x _ {c})}, \tag {2.4}
$$

where  $\sigma (Z > x_{c})$  and  $\sigma (Z < x_{c})$  correspond to the total cross section for each observable  $(Z)$ , above and below a specific cut-off value  $x_{c}$ , respectively. The cut-off values for each observable are chosen to be the ones where the difference between the respective asymmetries for the CP-even against the CP-odd case are largest. In table 1, the cut-off values  $(x_{c})$  are shown for each observable together with the asymmetry values at next-to-leading order (NLO) with parton shower effects. This is given for the CP-even ( $\alpha = 0.0^{\circ}$ ), CP-odd ( $\alpha = 90.0^{\circ}$ ) and mixed cases without any cuts. For completeness, the dominant background  $t\bar{t} b\bar{b}$  is also shown. The  $b_{2}^{t\bar{t}\phi}$  and  $b_{4}^{t\bar{t}\phi}$  variables show the strongest variation of asymmetry values as a function of the mixing angle, hence making these observables particularly sensitive to the absolute value of the mixing angle.

Contrary to CP-even observables, CP-odd variables are sensitive to the sign of  $\alpha$  since the interference term may contribute to the total differential cross section. One can show

that the only non-zero contributions to the interference term comes from the totally antisymmetric tensor product of the form  $\epsilon_{\mu \nu \gamma \rho}p_1^\mu p_2^\nu p_3^\gamma p_4^\rho$  (with  $\epsilon_{1234} = 1$ ), where  $p_i$  ( $i = 1, \dots, 4$ ) represents the four momenta associated with the process [54]. Furthermore, choosing a reference frame where  $p_1^\mu = (E_1, \vec{0})$ ,  $\epsilon_{\mu \nu \gamma \rho}p_1^\mu p_2^\nu p_3^\gamma p_4^\rho$  reduces to a scalar triple product of the form  $E_1\vec{p}_2 \cdot (\vec{p}_3 \times \vec{p}_4)$ , allowing us to construct simpler CP-odd observables [66]. In our paper, we will consider two most sensitive CP-odd observables from previous studies [39, 40], where the tensor products already mentioned are evaluated at the  $t\bar{t}$  CM frame, resulting in a single triple product of the form  $\vec{p}_t \cdot (\vec{p}_{l^+} \times \vec{p}_{l^-})$ . We then define  $\Delta \phi_{ll}$  which is the angle between the two lepton momenta projected onto the plane perpendicular to the  $t$  direction at the centre-of-mass frame of the  $t\bar{t}$  system and

$$
\Delta \phi_ {l l} ^ {t \bar {t}} = \operatorname {s g n} [ \hat {p} _ {t} \cdot (\hat {p} _ {l ^ {+}} \times \hat {p} _ {l ^ {-}}) ] \operatorname {a r c c o s} [ (\hat {p} _ {t} \times \hat {p} _ {l ^ {+}}) \cdot (\hat {p} _ {t} \times \hat {p} _ {l ^ {-}}) ]. \tag {2.5}
$$

Both variables are defined in the  $[- \pi, \pi]$  range. Notice however that there is a relative minus sign between these two definitions since the sign of  $\Delta \phi_{ll}$  is defined as the sign of  $\hat{p}_t \cdot (\hat{p}_{l-} \times \hat{p}_{l+})$ . For additional examples of CP-odd observables see [19, 41, 42, 54, 59, 63, 65].

# 3 Differential cross sections and interference term

The differential production cross section associated to any CP-mixed case of the  $t\bar{t}\phi$  signal can be parameterized as a function of the pure scalar and pure pseudo-scalar differential cross sections, according to

$$
d \sigma_ {t \bar {t} \phi} = \kappa^ {2} d \sigma_ {\mathrm {C P - e v e n}} + \tilde {\kappa} ^ {2} d \sigma_ {\mathrm {C P - o d d}} + \kappa \tilde {\kappa} d \sigma_ {\text {i n t}} \tag {3.1}
$$

where  $d\sigma_{t\bar{t}\phi}, d\sigma_{\mathrm{CP - even}}, d\sigma_{\mathrm{CP - odd}}$  and  $d\sigma_{\mathrm{int}}$  correspond to the signal differential cross sections for the CP-mixed, CP-even, CP-odd and interference terms, respectively. Although the interference terms do not contribute to the total cross section, they can affect the overall shape of the differential distributions for the different CP-observables. One of the most interesting questions we want to address in this paper is to understand the sensitivity of the different CP-observables to the interference terms in  $t\bar{t}\phi$  production at the LHC. By re-arranging the terms in eq. (3.1), it is possible to extract the contribution of the interference terms. This is done by subtracting to the CP-mixed differential cross sections the sum of the CP-even and CP-odd differential cross sections (weighted, respectively, by  $\kappa^2$  and  $\tilde{\kappa}^2$ ) and normalising the differences to  $\kappa \times \tilde{\kappa}$ . In figure 1 we present the interference terms at NLO+Shower effects, for the most sensitive CP-observables (as previously discussed) in  $t\bar{t}\phi$  production at the LHC, for a reference luminosity of  $100\mathrm{fb}^{-1}$ . The different  $t\bar{t}\phi$  signals, with mixing angles set to  $\alpha = 22.5^o, 45.0^o, 67.5^o$  and  $135^o$ , are used to extract the interference terms. From all CP-observables studied, the only ones that show any shape dependence are the ones corresponding to  $\Delta \phi_{ll}^{t\bar{t}}$  and  $\Delta \phi_{ll}$ , defined previously. In order to reduce the uncertainty on the interference terms, for each CP-observable, all generated CP-mixed signals are considered to compute an interference term, and their average (also represented in figure 1) is taken as the interference term for that particular CP-observable. To show that the process of determining the interferences is consistent, a

![](images/84e66f37d2fc391dbb8e3ce23fc67f0ed73e22377a770a26349c1adce38afe27.jpg)

![](images/27bb28d2fd0d7ce5e8a9e44d53f26e59e19f23b034d28a5ece6a2d4bc39f4983.jpg)

![](images/f4946392f32bcee3798ca6209dacc9222d28144e2f94f7ad2165947668e6b344.jpg)

![](images/79666b3de30fbe33917a385e90137d9223f672c7d9774f1eaac20111abbf79c4.jpg)

![](images/99f18b92b450f4032e5826c2decc6b99bcfefa5d829fdcab8f972eb432f59f68.jpg)  
Figure 1. Interference term at NLO+Shower effects for our choice of the best CP-sensitive variables in  $tt\phi$  production at the LHC, for a reference luminosity of  $100\mathrm{fb}^{-1}$ . Different  $tt\phi$  signals, with mixing angles set to  $\alpha = 22.5^o$ ,  $45.0^o$ ,  $67.5^o$  and  $135^o$  are used to extract the interference term.

![](images/b2a6039e9846d82ea5b75cd2aab7344f6a60de61a48ff620e573852219840f95.jpg)

comparison between the CP-mixed signals generated with different mixing angles, and the signals reconstructed using the interference terms, evaluated as described in eq. (3.1), is performed. This comparison is shown in figure 2, where good agreement is observed not only in what concerns the different differential distributions shapes but also the absolute rates expected for the different CP-mixed signals.

# 4 Event generation, selection and kinematic reconstruction

Monte Carlo generation and simulation. LHC-like signal and background events were generated with MadGraph5_aMC@NLO [67] for a centre-of-mass energy of 13 TeV. The Higgs Characterization model HC_NL0_X0 [68] was used to generate  $pp \rightarrow t\bar{t}\phi$  and single  $pp \rightarrow t\phi + jets$  signal events. The CP-even  $(\phi = H)$  and CP-odd  $(\phi = A)$  signals were generated by setting the mixing angle  $(\alpha)$  to  $\alpha = 0^{\circ}$  and  $90^{\circ}$ , respectively, following eq. (2.1), with  $\kappa_{t} = 1$ . Additional signal samples with different mixing angles, i.e.  $\alpha = 22.5^{\circ}$ ,  $45.0^{\circ}$ ,  $67.5^{\circ}$ ,  $135.0^{\circ}$  and  $180.0^{\circ}$ , were also generated. The mass of the scalar was set to  $m_{\phi} = 125\mathrm{GeV}$  in all signal samples. Only  $t\bar{t}\phi$  dileptonic events were considered  $(t\bar{t} \rightarrow bW^{+}\bar{b} W^{-} \rightarrow b\ell^{+}\nu_{\ell}\bar{b}\ell^{-}\bar{\nu}_{\ell})$  and the scalar boson is set to decay to a pair of  $b$ -quarks  $(\phi \rightarrow b\bar{b})$ . Backgrounds from SM  $t\bar{t} + 3$  jets,  $t\bar{t} V +$  jets, single top quark production  $(t-$ ,  $s-$  and  $Wt$ -channels),  $W(Z) + 4$  jets,  $W(Z)b\bar{b} + 2$  jets and  $WW,ZZ,WZ$  diboson processes were also generated using MadGraph5_aMC@NLO. Following event generation and hadronization by PYTHIA [69], all signal and background events were passed through a fast simulation of a typical LHC detector using DELPHES [70]. Further details on the event generation and detector simulation can be found in [31]. The analysis of signal and background events follows using the MadAnalysis5 [71] framework.

Selection and kinematic reconstruction. Events are selected by requiring at least four jets and two opposite charge leptons in the final state, with pseudo-rapidities  $(\eta)$  below 2.5 and transverse momenta  $(p_T)$  above  $20\mathrm{GeV}$ . As was done in [60], we start the kinematic reconstruction by evaluating the mass of the  $\phi$  boson and the jets associated to it. We use the usual invariant mass of pairs of jets (1,2) to evaluate the scalar boson mass,  $m_{\phi}^{\mathrm{inv}} = \sqrt{(p_1 + p_2)^2}$ , as well as a new method that uses the jets polar angles,

$$
m _ {\phi} ^ {(i)} = | \vec {p _ {1}} | \sqrt {2 \frac {\sin \theta_ {1}}{\sin \theta_ {2}} \left[ 1 - \cos \left(\theta_ {1} + \theta_ {2}\right) \right]}, \tag {4.1}
$$

where  $\vec{p}_1$  corresponds to the 3-momentum of jet 1 and  $\theta_{1}(\theta_{2})$  is the polar angle of jet 1 (jet 2), with respect to the direction of flight of the two jet system, assumed to be the scalar boson direction. Eq. (4.1) reflects the momentum conservation of a scalar boson decaying to two jets as represented in figure 3 (left). This method allows the mass measurement to be performed with only the knowledge of the 3-momentum of one jet, together with two polar angles from both jets. As angles tend to be well resolved by the LHC experiments, this method avoids momentum resolution effects from two jets to spoil the mass measurement (as usually happens in an invariant mass calculation), with only one jet momentum being necessary.

![](images/9841f606aac619df6f9f025c020fdecb5ee018005c5a1ba4b61c0e45c7a4ef62.jpg)

![](images/898ad82e797e9cb4be5d5382a9bf2b62ac15217666e400f5f95de276da8d3c7a.jpg)

![](images/2e3b772f5c1309aae5e47eb4cfef9e412aa1e9417ca66fe5e380347cbc35b82f.jpg)

![](images/a8ef7b4588a668f060d79cc87fbb003fbd158329cae09de5157958f6c514a393.jpg)

![](images/861627ac69d86e7a3c59183d73667a89cee1a25c62e31a564fd4322f3705111f.jpg)  
Figure 2. The CP observables reconstructed with the pure CP-even and pure CP-odd signals together with the interference terms at parton level with shower effects (with no cuts applied), for different mixing angles ( $\alpha = 22.5^o$ ,  $45.0^o$ ,  $67.5^o$  and  $135^o$ ), are shown against the corresponding NLO generations. Good agreement between the observables when reconstructed with the interference terms and the parton level distributions is observed.

![](images/2caf419a3d3df922f42611806faf36bcab0d628e1ec517e0d3859120ec3e73a5.jpg)

![](images/d3634c0be722a797c66ad0d46b5230884687fcc69b432b46b45ab4183e4eeeea.jpg)  
Figure 3. (Left) Schematic representation of the  $\phi$  boson decay and angles between the Higgs and its decay products; (right) SM Higgs boson mass distribution after kinematic reconstruction, for  $m_{\phi} = 125\mathrm{GeV}$ . The solid line shows the best invariant Higgs mass from one or two jets i.e.,  $m_{\phi}^{\mathrm{inv}}(1 + 2\mathrm{jets}) = m_{\phi}^{\mathrm{inv}}(1\mathrm{jet})$  or  $m_{\phi}^{\mathrm{inv}}(2\mathrm{jets})$ , and the dashed line represents the best of all methods (best of all) introduced in [60],  $\phi = H$ .

![](images/729361cf77e48b7a085357a10771553b042fad20ae645038bfb6fc69919a30ca.jpg)

For completeness, a one-jet invariant mass reconstruction  $(m_{\phi}^{\mathrm{inv}})$  is also implemented as a possible outcome for the Higgs boson decay, in particular when the decay jets overlap, but this is largely irrelevant in our analysis. From all methods used to evaluate the mass, the one giving the closest result to the Higgs boson mass ( $m_{\phi} = 125\mathrm{GeV}$ ) is chosen. The jets used by this method are associated, by the kinematic reconstruction, to the scalar boson decay partons. In figure 3 (right), we can see that the mass resolution, due to the impact of the new method, improves by roughly a factor two compared with the usual invariant mass measurement. The correct identification of the remaining jets as coming from the top quarks decays, and the reconstruction of the  $t\bar{t}$  system (which includes the neutrinos, the  $W^{\pm}$  bosons and the  $t$  and  $\bar{t}$  quarks), is performed by a kinematic fit detailed in [60].

Events are further selected by accepting the ones with two isolated leptons with opposite charges and invariant mass,  $m_{\ell + \ell^-}$ , outside a window of 10 GeV around the  $Z$  boson mass ( $m_Z = 91 \mathrm{GeV}$ ), to avoid contamination from the  $Z +$  jets background. Only events with at least 3 jets tagged as coming from the hadronization of  $b$ -quarks (labeled as  $b$ -tagged), are accepted. Further details on efficiencies, total number of events and kinematic distributions, can be found in [60].

In table 2, we present the asymmetries for the  $t\bar{t}\phi$  signal as a function of the mixing angle  $\alpha$ , as well as for the dominant background  $t\bar{t}b\bar{b}$  after event selection and kinematic reconstruction. The variable  $x_{c}$  represent the point chosen for the calculation of the asymmetry while  $A_{c}$  is the asymmetry relative to that point. We can see that there are significant differences between the asymmetries for the pure scalar  $(\alpha = 0.0^{\circ})$  and for pseudo-scalar  $(\alpha = 90.0^{\circ})$  scenarios for several asymmetries. As we will show later, an appropriate choice will maximise the difference between the asymmetries from the CP-even and CP-odd pure signal cases.

Table 2. Asymmetries for the  $t\bar{t}\phi$  signal as a function of the mixing angle  $\alpha$ , as well as for the dominant background  $t\bar{t}b\bar{b}$  after event selection and kinematic reconstruction, are shown for several observables. The variable  $x_{c}$  represent the point chosen for the calculation of the asymmetry while  $A_{c}$  is the asymmetry relative to that point. Significant differences between the asymmetries for the pure scalar  $(\alpha = 0.0^{\circ})$  and pseudo-scalar  $(\alpha = 90.0^{\circ})$  cases are observed for several asymmetries.  

<table><tr><td rowspan="3">Asymmetries</td><td rowspan="3">xc</td><td colspan="8">MadGraph5 @ NLO+Shower (after selection and rec.)</td></tr><tr><td colspan="8">tbarφ signal mixing angle α (deg.)</td></tr><tr><td>0.0°</td><td>22.5°</td><td>45.0°</td><td>67.5°</td><td>90.0°</td><td>135.0°</td><td>180.0°</td><td>tbarbbar</td></tr><tr><td>Ac[b2tbarφ]</td><td>-0.30</td><td>-0.12</td><td>-0.11</td><td>-0.01</td><td>+0.16</td><td>+0.24</td><td>-0.01</td><td>-0.13</td><td>-0.03</td></tr><tr><td>Ac[b4tbarφ]</td><td>-0.50</td><td>+0.30</td><td>+0.28</td><td>+0.18</td><td>+0.03</td><td>-0.06</td><td>+0.17</td><td>+0.32</td><td>+0.26</td></tr><tr><td>Ac[sin(θφtbarφ) * sin(θbarτ)]</td><td>+0.70</td><td>-0.26</td><td>-0.26</td><td>-0.24</td><td>-0.22</td><td>-0.19</td><td>-0.25</td><td>-0.25</td><td>-0.37</td></tr><tr><td>Ac[sin(θφtbarφ) * sin(θbarbbar)]</td><td>+0.60</td><td>+0.01</td><td>-0.01</td><td>-0.02</td><td>-0.02</td><td>-0.01</td><td>-0.03</td><td>-0.03</td><td>-0.22</td></tr><tr><td>(seq. boost)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

In figure 4, the differential distributions of the CP-observables are presented, for a reference luminosity of  $100\mathrm{fb}^{-1}$  at the LHC. The  $t\bar{t}\phi$  CP-even and CP-odd signals are scaled by a factor of 7 and 10, respectively, for displaying convenience. Although detector effects are clearly visible as distortions in the distributions shapes, the overall trend of the angular distribution is largely preserved. On the contrary, for the interference terms, evaluated in the same way as previously at parton level, few events are observed in the differential distributions, see figure 5. Although some shapes are still noticeable in the  $\Delta \phi_{ll}^{tt}$  and  $\Delta \phi_{ll}$  angular distributions, given the low number of events in every single bin, it is unlikely that the dileptonic  $t\bar{t}\phi$  analysis will ever be sensitive to this term. Looking for example into  $\Delta \phi_{ll}^{tt}$  (figure 5), we see that the expected number of events in every bin of the interference term is roughly close to half the number expected for the CP-odd signal which, in turn, is half the number of the CP-even case, both showed in figure 4.

# 5 Results and discussion

The differential angular distributions and the asymmetries are used to set confidence levels (CLs) limits on the exclusion of the SM with a contribution from a CP-mixed  $125\mathrm{GeV}$  Higgs boson  $\phi$ , assuming the SM hypothesis as the null hypothesis. The contribution of all SM backgrounds is taken into account and normalized to the LHC luminosity, just like the signal. The CLs limits are computed both for an LHC luminosity of  $L = 200\mathrm{fb}^{-1}$  (corresponding roughly to the RUN 2 luminosity plus the contribution from the first year of RUN 3), and for the full luminosity ( $L = 3000\mathrm{fb}^{-1}$ ) expected at the end of the High-Luminosity phase of the LHC (HL-LHC). The CLs limits are shown as contour plots in the  $(\kappa, \tilde{\kappa})$  2D plane (with  $\kappa = \kappa_{t}\cos \alpha$  and  $\tilde{\kappa} = \kappa_{t}\sin \alpha$ ), which is scanned using steps of 0.1 on the values of  $\kappa$  and  $\tilde{\kappa}$  in the range [-2.0, 2.0] for  $L = 200\mathrm{fb}^{-1}$ , and [-1.5, 1.5], for  $L = 3000\mathrm{fb}^{-1}$ . The calculation of the CLs follows the prescription described in [72, 73].

![](images/45c80629e8fed88eb7755ed3eb2de3f7905032e1fbb14fa09d8ede918dd1f789.jpg)

![](images/7ffb6bf9dc8e664ad2a2b15b89c9cf5e960694c52c1271cf3ebccf96a916486a.jpg)

![](images/20f2cdbb63e472911ccef6db5eeb5180e57c656a4bc8e4c9860ad1d2bd2fa8b6.jpg)

![](images/adb92f8959091f72ca2abb928248f1a2d26c7741e71af0363575a9579805ba2b.jpg)

![](images/1dbfd2e0791d8af5dfd404f015ae11eaf63917ea4fa4aea6334b56f5aa3e9abe.jpg)  
Figure 4. Angular distributions are represented, after event selection and kinematic reconstruction, for several sensitive CP variables, in  $t\bar{t}\phi$  production at the LHC, for a reference luminosity of  $100\mathrm{fb}^{-1}$ . The  $t\bar{t}\phi$  CP-even and CP-odd signals, are scaled by a factor of 7 and 10, respectively, for convenience.

![](images/ecf4384397a104f3bcdaf919eb25d180d384b0fc91967110414d93ff8865d30b.jpg)

![](images/0676b596472e8a0ae7307605df4af68224519b865db45ccdd4aa3293ed867dea.jpg)  
exp)  $\Delta \phi_{\parallel}^{\mathrm{tf}} / \pi$

![](images/2ca8e7fef3936a33ab90d1988a32e8f6c8219ec5e32f32386ed2b7871667b45a.jpg)  
$(\exp)$ $\Delta \phi_{\parallel} / \pi$

![](images/33572c62d2ccfaf459a3ba13bfea97663c724b9a5b5f17c761f653710dcbe575.jpg)  
(exp) b

![](images/f27fcae1ffe122da2174e0e701a9e39296c6adaf29e81d089840e524f1d1fdc1.jpg)  
(exp) b

![](images/98c261fb5c56b977c9604501f5db0243c02535b5b3b618acd27c35680ce8eb4c.jpg)  
(exp) sin(0f)  $\star$  sin(t

![](images/7ebe2e1200f25475a9a272b10049d42d44e6f52c06996ea92a60e14570e14789.jpg)  
Figure 5. The scalar-pseudoscalar interference term is represented, after event selection and kinematic reconstruction, for several sensitive CP variables, in  $t\bar{t}\phi$  production at the LHC, for a reference luminosity of  $100\mathrm{fb}^{-1}$ . Different  $t\bar{t}\phi$  signals, with mixing angles set to  $\alpha = 22.5^o$ ,  $45.0^o$ ,  $67.5^o$  and  $135^o$  are used to extract the interference term.  
(exp) (seq. boost)  $\sin (\theta_{\phi}^{\mathrm{tfo}})^{*}\sin (\theta_{\overline{b}_{\tau}}^{\overline{t}})$

Exclusion limits from asymmetries. Asymmetries are more interesting to explore during the initial phase of RUN 3 since they do not require the same amount of data as the differential distributions do, to be precisely measured. Whenever a total production cross section measurement is possible for the  $t\bar{t}\phi$  process at RUN 3, the evaluation of an asymmetry, i.e. a two bin measurement, is almost immediately accessible. In figure 6, we have evaluated the CLs limits for the exclusion of the SM null hypothesis, by using the asymmetries introduced in this paper. As can be seen in figure 6, the results obtained at the LHC are competitive with the ones obtained with differential angular distributions and may be performed during an early phase of RUN 3. Moreover the shapes of the  $b_{2}^{\bar{t}\bar{t}\phi}$  and  $b_{4}^{\bar{t}\bar{t}\phi}$  exclusion limits show a particularly different behaviour when compared with the usual  $\kappa^{2}\sigma_{\mathrm{CP - even}} + \tilde{\kappa}^{2}\sigma_{\mathrm{CP - odd}}$  dependence of the exclusions obtained with cross section measurements. This relates to the fact that asymmetries (see eq. (2.4)) of CP-even variables have a generic dependence with the CP-couplings of the form  $A\kappa^{2} + B\tilde{\kappa}^{2}$  but where  $A$  and  $B$  are not necessarily positive anymore. They are defined as

$$
A \propto \int_ {x _ {c}} ^ {+ 1} d \sigma_ {\mathrm {C P - e v e n}} - \int_ {- 1} ^ {x _ {c}} d \sigma_ {\mathrm {C P - e v e n}} \text {a n d} B \propto \int_ {x _ {c}} ^ {+ 1} d \sigma_ {\mathrm {C P - o d d}} - \int_ {- 1} ^ {x _ {c}} d \sigma_ {\mathrm {C P - o d d}}, \tag {5.1}
$$

and their value depends on the particular choice of the cut-off value used to define the asymmetry. An appropriate choice of  $x_{c}$  can render  $A$  and/or  $B$  negative, null or positive. The choice on this paper was to set  $x_{c}$  to maximise the difference between the asymmetries from the CP-even and CP-odd pure signal cases, at parton level (see table 1).

In figure 7 (left), we show the best exclusion limits obtained from the combination of the individual asymmetries in figure 6 where the complementarity amongst the different asymmetries becomes clearly visible.

In order to understand how a given cut-off affects the evaluation of the exclusion limits, a scan varying  $x_{c}$  along the distributions of the four observables, defined in eqs. (2.2) and (2.3) (and shown in figure 6), was performed using 100 different values, uniformly distributed over the range of the angular distributions. It is worth mentioning that the scans, as they use distributions after event selection, kinematic reconstruction, as well a full set of SM backgrounds, allow to find the optimal asymmetry cut-off value for each observable, and get the best exclusion limits with a setup very close to a real LHC experiment, i.e. taking into account the experimental distortions and particular shape of the signals and SM backgrounds. In figure 8, the  $b_4^{t\bar{t}\phi}$  exclusion limits are shown for  $x_{c} = -0.76$  (top-left),  $x_{c} = -0.14$  (top-right) and  $x_{c} = +0.04$  (bottom-left), considering  $k > 0.0$  for simplicity. The shape of the exclusion limits change quite remarkably as a function of  $x_{c}$ . The same behaviour is observed in the other variables. It is possible to make the exclusion limits almost insensitive to the real part of the coupling (for  $x_{c} = -0.14$ ), by allowing in eq. (5.1) the  $k^2$  dependency to essentially vanish ( $A \sim 0$ ). In figure 8 (bottom-right), we show the best combination using  $x_{c}$  set to  $-0.22$ ,  $+0.04$ ,  $+0.89$  and  $+0.15$  for the  $b_2^{t\bar{t}\phi}$ ,  $b_4^{t\bar{t}\phi}$ ,  $\sin(\theta_{\phi}^{t\bar{t}\phi}) * \sin(\theta_{\bar{t}}^{t\bar{t}})$  and  $\sin(\theta_{\phi}^{t\bar{t}\phi}) * \sin(\theta_{\bar{b}_{x}}^{\bar{t}\phi})$  (seq.), respectively.

By comparing the best exclusion limits obtained with the scan in figure 8 (bottom-right) and the limits obtained in figure 7 (left), no significant improvement is observed. Although care should be taken when considering the cut-off values for the evaluation of the

![](images/570d9caeb9bf9be0e5c73bd3a6aafee4ec0899b84b6c22a69b6b9c07b2857d52.jpg)

![](images/3fcc0f69235a0d2cb3eb81bc295592640a7732ca5b9742f08ab7b378a30a17d1.jpg)

![](images/e72556867cba3fbe8e62538697d64a7e2ab54edcf38adc198230a2a07c33fa1f.jpg)  
Figure 6. CLs for the exclusion of the SM with a  $125\mathrm{GeV}$  Higgs boson  $\phi$  with mixed scalar and pseudo-scalar couplings (CP-mixed case), against the SM as null hypothesis. Limits are shown for a luminosity corresponding to the full RUN 2 data and first year of RUN 3 i.e.,  $L = 200\mathrm{fb}^{-1}$ .

![](images/ee694310d0349f177c8e6f8f2484ba8569da4e4ea3110e7a5792e4f273ab9761.jpg)

![](images/0404fad2bc15a2f9917530b8f82e1a62081fbd2cc0deed6b04ed47b96da3f248.jpg)  
Figure 7. The best exclusion limits, from all single asymmetry exclusions, are shown (left), as well as the best exclusion limits from the angular differential distributions (right), for a luminosity corresponding to the full RUN 2 data and first year of RUN 3 i.e.,  $L = 200\mathrm{fb}^{-1}$ .

![](images/4f547dd8e071d50260692ccbccaafbd0cf2be4bc5fa5d2a0c6f0975f7fee699c.jpg)

![](images/61f38874937b4329ff6dbb60d90e0e81e02be2f9d35f8ffa7f87b3370d89259a.jpg)

![](images/7a7b86742a93b42e9ea93b16e2b29b376af5afb7bfc431685d6725bdc3676ed3.jpg)

![](images/672cb62b32e020cdcd2922c4d10e43cb571c1c2350c851326db9ba50afb42281.jpg)  
Figure 8. CLs for the exclusion of the SM with a  $125\mathrm{GeV}$  Higgs boson  $\phi$  with mixed scalar and pseudo-scalar couplings (CP-mixed case), against the SM as null hypothesis, for the  $b_4^{t\overline{t}\phi}$  asymmetry (top- and bottom-left and top-right) and best exclusion limits from all observables (bottom-right). Limits are shown for a luminosity corresponding to the full RUN 2 data and first year of RUN 3 i.e.,  $L = 200\mathrm{fb}^{-1}$  and as a function of different cut-off values applied to  $b_4^{t\overline{t}\phi}$  i.e.,  $x_{c} = -0.76$  (top-left),  $x_{c} = -0.14$  (top-right) and  $x_{c} = +0.04$  (bottom-left).

![](images/c89d2a5083c53d730daa3cbecd2ab4dfe1728103b9abc56bc17d92509e6e0eae.jpg)

individual asymmetries exclusion limits, if several are combined together the dependency with the cut-off is then largely suppressed. The simple approach of defining cut-off values that maximize the difference between the asymmetries for the pure CP-even and CP-odd cases seems appropriate for the analysis strategy. It should be stressed that no systematic uncertainties were considered in these studies and they may change the precision with which asymmetries can be measured. Nevertheless, as asymmetries are expected to be less affected by the systematic uncertainties (as they involve ratios of cross-sections where systematic uncertainties are expected to cancel out), they should be considered in an early phase of the RUN 3 of the LHC, where the signal and background modelling is not yet completely under control, providing similar exclusion limits to differential distributions.

Exclusion limits from differential distributions. When signal and background modelling becomes better understood at RUN 3, differential distributions will play an increasingly relevant role on setting exclusion limits. For comparison we show, in figure 7 (right), the best exclusions limits obtained with the differential angular distributions. An improvement is visible when compared with the asymmetries exclusions, see figure 7 (left). We should bear in mind, however, that the results of differential distributions may degrade once systematic

Table 3. Expected exclusion limits for the  $t\bar{t}\phi$  CP-couplings for a fixed luminosity of  $3000\mathrm{fb}^{-1}$ . The limits are shown for  $68\%$  and  $95\%$  CL, for the variables  $b_{2}^{t\bar{t}\phi}$  and  $b_{4}^{t\bar{t}\phi}$ , at the HL-LHC.  

<table><tr><td colspan="2">L=3000 fb-1</td><td colspan="2">Exclusion Limits from b2tbarphi(68% CL) (95% CL)</td><td colspan="2">Exclusion Limits from b4tbarphi(68% CL) (95% CL)</td></tr><tr><td rowspan="2">mφ=125 GeV</td><td>|κ| ∈</td><td>[0.968, 1.01]</td><td>[0.878, 1.04]</td><td>[0.968, 1.01]</td><td>[0.878, 1.04]</td></tr><tr><td>κ ∈</td><td>[-0.383, +0.383]</td><td>[-0.713, +0.713]</td><td>[-0.368, +0.368]</td><td>[-0.698, +0.698]</td></tr></table>

uncertainties are included. This indeed motivates to explore asymmetries during the early phase of RUN 3, for a new centre-of-mass energy, when a new cross section value for  $t\bar{t}\phi$  will become feasible. Both asymmetries and cross section measurements may be performed simultaneously.

In figure 9, we show the exclusion limits obtained when considering the full luminosity of  $3000\mathrm{fb}^{-1}$  at HL-LHC. The  $b_2^{t\bar{t}\phi}$  (figure 9 top) and  $b_4^{t\bar{t}\phi}$  (figure 9 middle) variables are considered as benchmark observables. In table 3, the corresponding limits are presented at  $68\%$  and  $95\%$  CL. As expected, a significant improvement is observed with respect to the RUN 3 results.

The effect of interference terms on the exclusion limits were also studied at the HL-LHC, considering the  $\Delta \phi_{ll}^{tt}$  angular distribution, see eq. (2.5). Although interference effects are visible for small values of  $k$  (around zero) and large values of  $\tilde{k}$  in figure 9 (bottom), where a slight difference appears in the distribution for positive and negative values of  $\tilde{k}$  (for  $k\sim 0.0$ ), the effect is rather marginal.

This is due to the fact that the interference terms give a rather small contribution to the differential cross section, largely dominated by the CP-even and CP-odd terms. By looking into the  $b_{2}^{t\bar{t}\phi}$  or  $b_{4}^{t\bar{t}\phi}$  exclusion limits, we see that if an exclusion is set to  $|\tilde{k}| \leq 0.85$ , the sensitivity to the interference term vanishes completely, making the test of the interference terms in  $t\bar{t}\phi$  events at the LHC almost impossible even at the HL-LHC.

We can now also compare the expected upper bound on the absolute value of the CP-mixing angle  $|\alpha|$  (see eq. (2.1)) at the end of the HL-LHC (from this channel alone), roughly  $|\alpha| < 40^{\circ}$ , with the 125 GeV Higgs data from rates together with EDMs constraint in UV-complete models. Taking the C2HDM as an example, it was shown in [17] that the data from measurements of cross sections times branching ratios of the 125 GeV Higgs already imposes an indirect bound of roughly  $|\alpha| < 20^{\circ}$  for the CP-mixing angle in the coupling of the SM-like Higgs to top quarks. This comes mainly from the signal strength from gluon fusion production of a Higgs with subsequent decay to the two photon final state. This means that we will most probably not be sensitive to CP-mixing angle of the SM-like Higgs in this model (in its couplings to the top quarks) even with the inclusion of other channels. Note however that in the C2HDM the CP-mixing angles to other quarks and to leptons have to be determined/tested independently and that the number of independent angles depends on the Yukawa model type. On the other hand, this is the dominant channel where this type of CP-violating Yukawa coupling shows at tree-level, allowing for a direct

![](images/0283c0ad53a74ee386a77d5f62d01fd21c0b463d220a87a91696b56347f923cc.jpg)

![](images/4b02059297cc04327ff271c212e9a9608f35ebfedb9795f5d25325d9fb3499de.jpg)

![](images/b3c2bd68de27a2b34f14dbf185c88264d6abe87cda04675248240ebfc76a2023.jpg)  
Figure 9. Expected exclusion limits for the  $t\bar{t}\phi$  CP-couplings for a fixed luminosity of  $3000\mathrm{fb}^{-1}$  and for the  $b_2^{t\bar{t}\phi}$  (top) and  $b_4^{t\bar{t}\phi}$  (middle) variables are shown, at the HL-LHC. The effect of interference effects is also shown (bottom) for the  $\Delta \phi_{ll}^{t\bar{t}}$  angular distribution.

probe which is always a motivated measurement in itself. Furthermore, measurements of values of the CP-mixing angle larger than  $40^{\circ}$  would not only be indication of new physics but would also exclude the C2HDM scenario, inviting for more innovative physics models.

# 6 Conclusions

In this paper we have studied the sensitivity to probe the CP nature of a 125 GeV Higgs boson with CP-even and CP-odd mixed couplings, at the LHC, for luminosities which typically are expected to be within reach during RUN 3 ( $\sim 300\mathrm{fb}^{-1}$ ), up to the High Luminosity phase of the LHC (HL-LHC), with  $3000\mathrm{fb}^{-1}$ . Signal events from  $t\bar{t}\phi$  associated production are searched for, in dileptonic final states. While the  $t\bar{t}$  system decays to two opposite charged leptons, the  $\phi$  boson is expected to decay through the  $\phi \rightarrow b\bar{b}$  channel. A new reconstruction method for the SM Higgs boson mass ( $m_{\phi}$ ) was applied allowing to gain, in terms of mass resolution, roughly a factor of two with respect to previous analysis methods. Without loss of generality, the method can be easily extrapolated to any other two body decays of the Higgs boson like for instance  $\phi \rightarrow \gamma \gamma$ , provided the decay channel is kinematically accessible.

As a result of several years of testing CP-probing variables, four CP-observables,  $b_{2}^{tt\phi}$ ,  $b_{4}^{tt\phi}$ ,  $\sin(\theta_{\phi}^{tt\phi}) * \sin(\theta_{\bar{t}}^{tt})$  and  $\sin(\theta_{\phi}^{tt\phi}) * \sin(\theta_{\bar{b}_{\bar{t}}}^{\bar{t}})$  seq., were constructed and used to set exclusion limits confidence levels (CL) in the 2D  $(\kappa, \tilde{\kappa})$  plane. A signal hypothesis with a 125 GeV Higgs boson  $(\phi)$  with mixed CP states, was studied against the SM scalar Higgs boson (null) hypothesis. The 95% CL exclusion limits in the  $(\kappa, \tilde{\kappa})$  plane are set to  $\tilde{\kappa} \in [-0.698, +0.698]$  and  $|k| \in [0.878, 1.04]$  respectively at the HL-LHC, using only the dileptonic decay channel of the  $pp \to t\bar{t}\phi$  system (with  $\phi \to b\bar{b}$ ). These results are expected to be significantly improved when the semileptonic decays of the  $t\bar{t}\phi$  system are combined on one hand with the remaining decay channels of the top-quarks (W-bosons) and on the other hand with the other decay channels of the 125 GeV Higgs boson.

Exclusion limits are also presented using asymmetries built from the angular CP-observables, for specific choices of the cut-off values  $(x_{c})$  used to define the asymmetries. The optimal values of  $x_{c}$ , i.e., the values that lead to the best exclusion limits when combining the different asymmetries, are studied. The combination of the results allowed to set exclusion limits with asymmetries almost as good as the ones obtained with differential angular distributions. This is particularly appropriated for an early phase of the RUN 3 of the LHC, when background and signal modelling may not yet be fully under control and the statistical size of the collected data sample is still not too large. If all asymmetries are used, the cut-off can be defined by maximising the difference between the pure CP-even and CP-odd cases, at parton level, without loss of sensitivity.

Interference terms (between CP-even and CP-odd components) on the exclusion limits, are also studied at the HL-LHC. Although interference effects are visible for small values of  $k$  (around zero) and large values of  $\tilde{k}$  in the  $(\kappa, \tilde{\kappa})$  plane, the effect is rather small. In particular, if we see that an exclusion limit is set at  $|\tilde{k}| \leq 0.85$ , the sensitivity to the interference term vanishes completely, making the test of the interference terms in  $t\bar{t}\phi$  events at the LHC, unfeasible at HL-LHC.

# Acknowledgments

RC and RS are partially supported by the Portuguese Foundation for Science and Technology (FCT) under Contracts no. UIDB/00618/2020, UIDP/00618/2020, PTDC/FISPAR/31000/2017 and CERN/FIS-PAR/0014/2019. RC is additionally supported by FCT grant 2020.08221.BD. AO is supported by FCT under contracts no. CERN/FISPAR/0029/2019 and CERN/FIS-PAR/0037/2021. DA acknowledges support from the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under grant 396021762 - TRR 257.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.  $\mathrm{SCOAP}^3$  supports the goals of the International Year of Basic Sciences for Sustainable Development.

# References

[1] A.D. Sakharov, Violation of CP Invariance, C asymmetry, and baryon asymmetry of the universe, Pisma Zh. Eksp. Teor. Fiz. 5 (1967) 32 [INSPIRE].  
[2] ATLAS collaboration, Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC, Phys. Lett. B 716 (2012) 1 [arXiv:1207.7214] [INSPIRE].  
[3] CMS collaboration, Observation of a New Boson at a Mass of 125 GeV with the CMS Experiment at the LHC, Phys. Lett. B 716 (2012) 30 [arXiv:1207.7235] [INSPIRE].  
[4] T.D. Lee, A Theory of Spontaneous  $T$  Violation, Phys. Rev. D 8 (1973) 1226 [INSPIRE].  
[5] I.F. Ginzburg, M. Krawczyk and P. Osland, Two Higgs doublet models with CP-violation, in International Workshop on Linear Colliders (LCWS 2002), (2002), pp. 703-706 [hep-ph/0211371] [INSPIRE].  
[6] W. Khater and P. Osland, CP violation in top quark production at the LHC and two Higgs doublet models, Nucl. Phys. B 661 (2003) 209 [hep-ph/0302004] [INSPIRE].  
[7] A.W. El Kaffas, P. Osland and O.M. Ogreid, CP violation, stability and unitarity of the two Higgs doublet model, Nonlin. Phenom. Complex Syst. 10 (2007) 347 [hep-ph/0702097] [INSPIRE].  
[8] B. Grzadkowski and P. Osland, Tempered Two-Higgs-Doublet Model, Phys. Rev. D 82 (2010) 125026 [arXiv:0910.4068] [INSPIRE].  
[9] A. Arhrib, E. Christova, H. Eberl and E. Ginina, CP violation in charged Higgs production and decays in the Complex Two Higgs Doublet Model, JHEP 04 (2011) 089 [arXiv:1011.6560] [INSPIRE].  
[10] A. Barroso, P.M. Ferreira, R. Santos and J.P. Silva, Probing the scalar-pseudoscalar mixing in the 125 GeV Higgs particle with current data, Phys. Rev. D 86 (2012) 015022 [arXiv:1205.4247] [INSPIRE].  
[11] S. Inoue, M.J. Ramsey-Musolf and Y. Zhang, CP-violating phenomenology of flavor conserving two Higgs doublet models, Phys. Rev. D 89 (2014) 115023 [arXiv:1403.4257] [INSPIRE].

[12] K. Cheung, J.S. Lee, E. Senaha and P.-Y. Tseng, Confronting Higginson with Electric Dipole Moments, JHEP 06 (2014) 149 [arXiv:1403.4775] [INSPIRE].  
[13] D. Fontes, J.C. Romão and J.P. Silva,  $h \to Z\gamma$  in the complex two Higgs doublet model, JHEP 12 (2014) 043 [arXiv:1408.2534] [INSPIRE].  
[14] D. Fontes, J.C. Romão, R. Santos and J.P. Silva, Large pseudoscalar Yukawa couplings in the complex 2HDM, JHEP 06 (2015) 060 [arXiv:1502.01720] [INSPIRE].  
[15] C.-Y. Chen, S. Dawson and Y. Zhang, Complementarity of LHC and EDMs for Exploring Higgs CP-violation, JHEP 06 (2015) 056 [arXiv:1503.01114] [INSPIRE].  
[16] M. Mühlleitner, M.O.P. Sampaio, R. Santos and J. Wittbrodt, Phenomenological Comparison of Models with Extended Higgs Sectors, JHEP 08 (2017) 132 [arXiv:1703.07750] [INSPIRE].  
[17] D. Fontes, M. Mühlleitner, J.C. Romão, R. Santos, J.P. Silva and J. Wittbrodt, The C2HDM revisited, JHEP 02 (2018) 073 [arXiv:1711.09419] [INSPIRE].  
[18] J.F. Gunion and X.-G. He, Determining the CP nature of a neutral Higgs boson at the LHC, Phys. Rev. Lett. 76 (1996) 4468 [hep-ph/9602226] [INSPIRE].  
[19] F. Boudjema, R.M. Godbole, D. Guadagnoli and K.A. Mohan, Lab-frame observables for probing the top-Higgs interaction, Phys. Rev. D 92 (2015) 015019 [arXiv:1501.03157] [INSPIRE].  
[20] S.P. Amor dos Santos et al., Angular distributions in  $t\bar{t}H(H \to b\bar{b})$  reconstructed events at the LHC, Phys. Rev. D 92 (2015) 034021 [arXiv:1503.07787] [INSPIRE].  
[21] S. Amor Dos Santos et al., Probing the CP nature of the Higgs coupling in  $t\bar{t}h$  events at the LHC, Phys. Rev. D 96 (2017) 013004 [arXiv:1704.03565] [INSPIRE].  
[22] S. Berge, W. Bernreuther and J. Ziethe, Determining the CP parity of Higgs bosons at the LHC in their tau decay channels, Phys. Rev. Lett. 100 (2008) 171605 [arXiv:0801.2297] [INSPIRE].  
[23] S. Berge and W. Bernreuther, Determining the CP parity of Higgs bosons at the LHC in the tau to 1-prong decay channels, Phys. Lett. B 671 (2009) 470 [arXiv:0812.1910] [INSPIRE].  
[24] S. Berge, W. Bernreuther, B. Niepelt and H. Spiesberger, How to pin down the CP quantum numbers of a Higgs boson in its tau decays at the LHC, Phys. Rev. D 84 (2011) 116003 [arXiv:1108.0670] [INSPIRE].  
[25] S. Berge, W. Bernreuther and S. Kirchner, Determination of the Higgs CP-mixing angle in the tau decay channels at the LHC including the Drell-Yan background, Eur. Phys. J. C 74 (2014) 3164 [arXiv:1408.0798] [INSPIRE].  
[26] S. Berge, W. Bernreuther and S. Kirchner, Prospects of constraining the Higgs boson's CP nature in the tau decay channel at the LHC, Phys. Rev. D 92 (2015) 096012 [arXiv:1510.03850] [INSPIRE].  
[27] CMS collaboration, *Measurements of t $\bar{t}H$  Production and the CP Structure of the Yukawa Interaction between the Higgs Boson and Top Quark in the Diphoton Decay Channel*, Phys. Rev. Lett. **125** (2020) 061801 [arXiv:2003.10866] [INSPIRE].  
[28] ATLAS collaboration, CP Properties of Higgs Boson Interactions with Top Quarks in the  $t\bar{t}H$  and  $tH$  Processes Using  $H \rightarrow \gamma \gamma$  with the ATLAS Detector, Phys. Rev. Lett. 125 (2020) 061802 [arXiv:2004.04545] [INSPIRE].  
[29] CMS collaboration, Analysis of the CP structure of the Yukawa coupling between the Higgs boson and  $\tau$  leptons in proton-proton collisions at  $\sqrt{s} = 13$  TeV, Tech. Rep. CMS-PAS-HIG-20-006 CERN, Geneva (2020).

[30] T. Ghosh, R. Godbole and X. Tata, Determining the spacetime structure of bottom-quark couplings to spin-zero particles, Phys. Rev. D 100 (2019) 015026 [arXiv:1904.09895] [INSPIRE].  
[31] D. Azevedo, R. Capucha, A. Onofre and R. Santos, Scalar mass dependence of angular variables in  $t\bar{t}\phi$  production, JHEP 06 (2020) 155 [arXiv:2003.09043] [INSPIRE].  
[32] R. Alonso, C. Fraser-Taliente, C. Hays and M. Spannowsky, Prospects for direct CP tests of hqq interactions, JHEP 08 (2021) 167 [arXiv:2105.06879] [INSPIRE].  
[33] C. Grojean, A. Paul and Z. Qian, Resurrecting bbh with kinematic shapes, JHEP 04 (2021) 139 [arXiv:2011.13945] [INSPIRE].  
[34] D. Huang, A.P. Morais and R. Santos,  $CP$  violating  $hW^{+}W^{-}$  coupling in the Standard Model and beyond, JHEP 01 (2021) 168 [arXiv:2009.09228] [INSPIRE].  
[35] H.E. Haber, V. Keus and R. Santos,  $P$ -even, CP-violating Signals in Scalar-Mediated Processes, arXiv:2206.09643 [INSPIRE].  
[36] J. Hermann, D. Stremmer and M. Worek,  $\mathcal{CP}$  structure of the top-quark Yukawa interaction: NLO QCD corrections and off-shell effects, arXiv:2205.09983 [INSPIRE].  
[37] A.V. Gritsan, J. Roskes, U. Sarica, M. Schulze, M. Xiao and Y. Zhou, New features in the JHU generator framework: constraining Higgs boson properties from on-shell and off-shell production, Phys. Rev. D 102 (2020) 056022 [arXiv:2002.09888] [INSPIRE].  
[38] A. Bhardwaj, C. Englert, R. Hankache and A.D. Pilkington, Machine-enhanced CP-asymmetries in the Higgs sector, Phys. Lett. B 832 (2022) 137246 [arXiv:2112.05052] [INSPIRE].  
[39] J. Ellis, D.S. Hwang, K. Sakurai and M. Takeuchi, Disentangling Higgs-Top Couplings in Associated Production, JHEP 04 (2014) 004 [arXiv:1312.5736] [INSPIRE].  
[40] D. Gonçalves, K. Kong and J.H. Kim, Probing the top-Higgs Yukawa CP structure in dileptonic  $t\bar{h}$  with  $M_2$ -assisted reconstruction, JHEP 06 (2018) 079 [arXiv:1804.05874] [INSPIRE].  
[41] D. Gonçalves, J.H. Kim, K. Kong and Y. Wu, Direct Higgs-top CP-phase measurement with  $t\bar{t}h$  at the 14 TeV LHC and 100 TeV FCC, JHEP 01 (2022) 158 [arXiv:2108.01083] [INSPIRE].  
[42] W. Bernreuther and A. Brandenburg, Tracing CP-violation in the production of top quark pairs by multiple TeV proton proton collisions, Phys. Rev. D 49 (1994) 4481 [hep-ph/9312210] [INSPIRE].  
[43] P.S. Bhupal Dev, A. Djouadi, R.M. Godbole, M.M. Muhlleitner and S.D. Rindani, Determining the CP properties of the Higgs boson, Phys. Rev. Lett. 100 (2008) 051801 [arXiv:0707.2878] [INSPIRE].  
[44] R. Frederix, S. Frixione, V. Hirschi, F. Maltoni, R. Pittau and P. Torrielli, Scalar and pseudoscalar Higgs production in association with a top-antitop pair, Phys. Lett. B 701 (2011) 427 [arXiv:1104.5613] [INSPIRE].  
[45] S. Khatibi and M. Mohammadi Najafabadi, Exploring the Anomalous Higgs-top Couplings, Phys. Rev. D 90 (2014) 074014 [arXiv:1409.6553] [INSPIRE].  
[46] F. Demartin, F. Maltoni, K. Mawatari, B. Page and M. Zaro, Higgs characterisation at NLO in QCD: CP properties of the top-quark yukawa interaction, Eur. Phys. J. C 74 (2014).  
[47] A. Kobakhidze, L. Wu and J. Yue, Anomalous Top-Higgs Couplings and Top Polarisation in Single Top and Higgs Associated Production at the LHC, JHEP 10 (2014) 100 [arXiv:1406.1961] [INSPIRE].

[48] J. Bramante, A. Delgado and A. Martin, Cornering a hyper Higgs boson: Angular kinematics for boosted Higgs bosons with top pairs, Phys. Rev. D 89 (2014) 093006 [arXiv:1402.5985] [INSPIRE].  
[49] X.-G. He, G.-N. Li and Y.-J. Zheng, Probing Higgs boson CP Properties with  $t\bar{t}H$  at the LHC and the 100 TeV pp collider, Int. J. Mod. Phys. A 30 (2015) 1550156 [arXiv:1501.00012] [INSPIRE].  
[50] A.V. Gritsan, R. Röntsch, M. Schulze and M. Xiao, Constraining anomalous Higgs boson couplings to the heavy flavor fermions using matrix element techniques, Phys. Rev. D 94 (2016) 055023 [arXiv:1606.03107] [INSPIRE].  
[51] M.J. Dolan, M. Spannowsky, Q. Wang and Z.-H. Yu, Determining the quantum numbers of simplified models in  $t\bar{t}X$  production at the LHC, Phys. Rev. D 94 (2016) 015025 [arXiv:1606.00019] [INSPIRE].  
[52] D. Gonçalves and D. López-Val, Pseudoscalar searches with dileptonic tops and jet substructure, Phys. Rev. D 94 (2016) 095005 [arXiv:1607.08614] [INSPIRE].  
[53] M.R. Buckley and D. Gonçalves, Constraining the Strength and CP Structure of Dark Production at the LHC: the Associated Top-Pair Channel, Phys. Rev. D 93 (2016) 034003 [arXiv:1511.06451] [INSPIRE].  
[54] N. Mileo, K. Kiers, A. Szynkman, D. Crane and E. Gegner, Pseudoscalar top-Higgs coupling: exploration of CP-odd observables to resolve the sign ambiguity, JHEP 07 (2016) 056 [arXiv:1603.03632] [INSPIRE].  
[55] M.R. Buckley and D. Gonçalves, Boosting the Direct CP Measurement of the Higgs-Top Coupling, Phys. Rev. Lett. 116 (2016) 091801 [arXiv:1507.07926] [INSPIRE].  
[56] D. Azevedo, A. Onofre, F. Filthaut and R. Gonçalo, CP tests of Higgs couplings in  $t$ th semileptonic events at the LHC, Phys. Rev. D 98 (2018) 033004 [arXiv:1711.05292] [INSPIRE].  
[57] J. Li, Z.-g. Si, L. Wu and J. Yue, Central-edge asymmetry as a probe of Higgs-top coupling in  $t\bar{th}$  production at the LHC, Phys. Lett. B 779 (2018) 72 [arXiv:1701.00224] [INSPIRE].  
[58] A. Ferroglia, M.C.N. Fiolhais, E. Gouveia and A. Onofre, Role of the  $t\bar{t} h$  rest frame in direct top-quark Yukawa coupling measurements, Phys. Rev. D 100 (2019) 075034 [arXiv:1909.00490] [INSPIRE].  
[59] D.A. Faroughy, J.F. Kamenik, N. Košnik and A. Smolkovič, Probing the CP nature of the top quark Yukawa at hadron colliders, JHEP 02 (2020) 085 [arXiv:1909.00007] [INSPIRE].  
[60] D. Azevedo, R. Capucha, E. Gouveia, A. Onofre and R. Santos, Light Higgs searches in  $t\bar{t}\phi$  production at the LHC, JHEP 04 (2021) 077 [arXiv:2012.10730] [INSPIRE].  
[61] H. Bahl et al., Indirect CP probes of the Higgs-top-quark interaction: current LHC constraints and future opportunities, JHEP 11 (2020) 127 [arXiv:2007.08542] [INSPIRE].  
[62] H. Bahl and S. Brass, Constraining  $\mathcal{CP}$ -violation in the Higgs-top-quark interaction using machine-learning-based inference, JHEP 03 (2022) 017 [arXiv:2110.10177] [INSPIRE].  
[63] B. Bortolato, J.F. Kamenik, N. Košnik and A. Smolkovič, Optimized probes of CP-odd effects in the tth process at hadron colliders, Nucl. Phys. B 964 (2021) 115328 [arXiv:2006.13110] [INSPIRE].  
[64] Q.-H. Cao, K.-P. Xie, H. Zhang and R. Zhang, A New Observable for Measuring CP Property of Top-Higgs Interaction, Chin. Phys. C 45 (2021) 023117 [arXiv:2008.13442] [INSPIRE].

[65] R.K. Barman, D. Gonçalves and F. Kling, Machine learning the Higgs boson-top quark CP phase, Phys. Rev. D 105 (2022) 035023 [arXiv:2110.07635] [INSPIRE].  
[66] G. Durieux and Y. Grossman, Probing CP-violation systematically in differential distributions, Phys. Rev. D 92 (2015) 076013 [arXiv:1508.03054] [INSPIRE].  
[67] J. Alwall, M. Herquet, F. Maltoni, O. Mattelaer and T. Stelzer, MadGraph 5: Going Beyond, JHEP 06 (2011) 128 [arXiv:1106.0522] [INSPIRE].  
[68] P. Artoisenet et al., A framework for Higgs characterisation, JHEP 11 (2013) 043 [arXiv:1306.6464] [INSPIRE].  
[69] T. Sjöstrand, S. Mrenna and P.Z. Skands, PYTHIA 6.4 Physics and Manual, JHEP 05 (2006) 026 [hep-ph/0603175] [INSPIRE].  
[70] DELPHES 3 collaboration, DELPHES 3, A modular framework for fast simulation of a generic collider experiment, JHEP 02 (2014) 057 [arXiv:1307.6346] [INSPIRE].  
[71] E. Conte, B. Fuks and G. Serret, MadAnalysis 5, A User-Friendly Framework for Collider Phenomenology, Comput. Phys. Commun. 184 (2013) 222 [arXiv:1206.1599] [INSPIRE].  
[72] A.L. Read, Presentation of search results: The  $CL(s)$  technique, J. Phys. G 28 (2002) 2693 [INSPIRE].  
[73] T. Junk, Confidence level computation for combining searches with small statistics, Nucl. Instrum. Meth. A 434 (1999) 435 [hep-ex/9902006] [INSPIRE].