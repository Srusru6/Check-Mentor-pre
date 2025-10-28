# Search for an invisible scalar in  $t\bar{t}$  final states at the LHC

Duarte Azevedo, $^{a,b}$  Rodrigo Capucha, $^{c}$  Pedro Chaves, $^{d}$  João Bravo Martins, $^{c}$  Antonio Onofre $^{d}$  and Rui Santos $^{c,e}$

$^{a}$ Institute for Theoretical Physics, Karlsruhe Institute of Technology, Wolfgang-Gaede-Str. 1, 76128 Karlsruhe, Germany

$^{b}$ Institute for Astroparticle Physics, Karlsruhe Institute of Technology, Hermann-von-Helmholtz-Platz 1, 76344 Eggenstein-Leopoldshafen, Germany

$^{c}$ Centro de Física Teórica e Computacional, Faculdade de Ciências, Universidade de Lisboa, Campo Grande, Edificio C8 1749-016 Lisboa, Portugal

$^{d}$ Centro de Física da Universidade do Minho e Universidade do Porto (CF-UM-UP), Universidade do Minho, 4710-057 Braga, Portugal

$^{e}$ ISEL — Instituto Superior de Engenharia de Lisboa, Instituto Politécnico de Lisboa, 1959-007 Lisboa, Portugal

E-mail: duarte.azevedo@kit.edu, rscapucha@fc.ul.pt, pshalo06@gmail.com, joaobravomartins24@hotmail.com, antonio.onofre@cern.ch, rasantos@fc.ul.pt

ABSTRACT: We use the current  $t\bar{t}$  experimental analysis to look for Dark Matter (DM) particles hidden in the final state. We present a phenomenological study where we successfully perform the reconstruction of a  $t\bar{t}$  system in the presence of a scalar mediator  $Y_{0}$ , that couples to both Standard Model (SM) and to DM particles. We use a MadGraph5_aMC@NLO simplified DM model, where signal samples of  $pp \rightarrow t\bar{t}Y_{0}$  are generated at the Large Hadron Collider (LHC) with both Charge-Parity (CP) -even and CP-odd couplings of  $Y_{0}$  to the top quarks. Different mass scales for the  $Y_{0}$  mediator are considered, from the low mass region ( $\sim 0\mathrm{GeV}$ ) to masses close to the Higgs boson mass (125 GeV). The dileptonic final states of the  $t\bar{t}$  system were used in our analysis. The reconstruction of the  $t\bar{t}$  system is done with a kinematic fit, without reconstructing the mediator. All relevant SM backgrounds for the dileptonic  $t\bar{t}$  search at the LHC are considered. Furthermore, CP angular observables were used to probe the CP-nature of the coupling between the mediator and top-quarks, which allowed to set confidence level (CL) limits for those Yukawa couplings as a function of the mediator mass.

KEYWORDS: Dark Matter at Colliders, New Light Particles

ARXIV EPRINT: 2308.00819

# Contents

1 Introduction 1  
2 The DM Lagrangian 2  
3 Event generation and simulation 3  
4 Event selection and kinematic reconstruction 4  
5 Results and discussion 8  
6 Conclusions 11

# 1 Introduction

Evidence for the existence of dark matter (DM) provided by astrophysical observations, be it from gravitational lensing effects [1-4], galactic rotational velocity curves [5] or from other measurements like the collision of clusters of galaxies (Bullet Cluster) [6], is by now overwhelming. However, the nature of this non-luminous matter remains unknown in spite of decades of intensive searches in a vast array of experiments. From the observations, we can hypothesise that if DM is actually composed of particles, they only interact very weakly with the Standard Model (SM). Since SM neutrinos have been mostly ruled out as possible DM candidates, due to cosmological constraints [7], this suggests the possible existence of a "dark sector" composed of particles beyond the SM. Attempts at direct and indirect detection of the myriad of particles proposed from extending the SM with such a sector (such as weakly interacting massive particles and axions, among many others) have, so far, provided no definitive results favouring any particular hypotheses [8, 9].

DM searches at colliders have focused on mono-events, such as mono-jet, mono-Higgs among others [10-12]. There are also bounds on the portal couplings from the invisible branching ratio of the 125 GeV Higgs [13, 14]. Searches for DM particles produced alongside a  $t\bar{t}$  pair and single top quark events have also been performed in the past [15-18] mostly using variables such as missing energy as a discriminator, with no attempt to reconstruct the kinematics of the top quarks. Searches using the  $t\bar{t}$  analysis to look for DM were performed considering as signal the productions of stop squarks with masses just above the top quark. The stops would then decay to a top and a nearly massless LSP [19-21]. Our study is also designed to look for DM particles hidden in the current on-going searches and analysis, but with a signal that comes directly from  $t\bar{t}$  plus an invisible particle. Let us consider as an example the case of  $t\bar{t}$  production in the di-leptonic channel. The question we want to answer is: if a very light DM particle would be produced alongside the  $t\bar{t}$  pair would we see any difference in any distributions? If no differences are found, could the analysis

already performed be used to limit the couplings of DM particles for very light invisible particles? One should note that from the point of view of high energy collider physics we are really exploring the case of a zero DM mass particle which means that we are spanning DM masses from the scenarios of ultra-light particles to a few GeV in mass. That is, for LHC energies, masses below about 1 GeV are for all practical purposes equal to zero. Still we will also show how the  $t\bar{t}$  analysis performs in the case of a 125 GeV scalar.

In order to implement our idea we consider a new mediator that couples to both DM and to the SM particles. We study the possibility of using previous mainstream experimental analysis of  $pp \rightarrow t\bar{t}$  in the di-leptonic channel to gauge the impact of a spin-0 DM mediator ( $J^{\mathrm{CP}} = 0^{\pm}$ ) in the associated production process  $t\bar{t} Y_0$ . The analysis is performed within the description of simplified models of DM production at the LHC, where the DM mediator ( $Y_0$ ) couples to the top-quarks proportionally to the top mass. The results are presented as a function of the modifier of this new Yukawa coupling. This is a convenient approach, as the LHC can explore a large spectrum of DM mediator masses and coupling strengths, allowing to access the CP-nature of these mediators, in case they exist even as mixed CP states.

This paper is organised as follows: the simplified DM model, the relevant parameters and the angular observables we used, are presented in section 2. The event generation and simulation are described in section 3 and, in section 4, the event selection and kinematic reconstruction are discussed. Our results are presented in section 5 and the main conclusions are described in section 6.

# 2 The DM Lagrangian

In our study, we used the simplified DM model DMsimp [22] where, besides the scalar  $Y_{0}$  boson, we also have a dark sector that couples only to  $Y_{0}$ . In our paper, we will remain agnostic to the latter, focusing solely on the interaction between the  $Y_{0}$  DM mediator to the SM content. In particular, we will assume Yukawa couplings proportional to the mass of the respective SM particle and hence dedicate ourselves exclusively to top quarks. The Lagrangian density can thus be simplified and written as follows

$$
\mathcal {L} _ {\mathrm {S M}} ^ {Y _ {0}} = \frac {y _ {3 3} ^ {t}}{\sqrt {2}} \bar {t} \left(g _ {u _ {3 3}} ^ {S} + i g _ {u _ {3 3}} ^ {P} \gamma^ {5}\right) t Y _ {0}, \tag {2.1}
$$

where the  $g_{u_{33}}^{S / P}$  are the CP-even/-odd couplings of the DM mediator  $(Y_0)$  to top quarks, respectively. They are normalized to the SM Yukawa couplings,  $y_{ii}^f = \sqrt{2} m_f / v$ . The scalar hypothesis  $(\mathrm{CP} = +1)$  is given by setting  $g_{u_{33}}^S = 1$  and  $g_{u_{33}}^P = 0$  and for the pseudo-scalar scenario  $(\mathrm{CP} = -1)$  we set  $g_{u_{33}}^S = 0$  and  $g_{u_{33}}^P = 1$ . When both  $g_{u_{33}}^{S / P} \neq 0$ , the interaction has both CP-even and -odd components and is thus CP-violating.

Note that eq. (2.1) is valid for any extension of the SM that has a CP-violating scalar sector, provided CP-violation does not have origin in a dark sector [23]. The specific extension will determine the mixing between the SM Higgs and all other charge zero scalars and consequently will allow us to write the  $g$  couplings as a function of the mixing angles. It can happen that in some cases the LHC bounds stemming from the measurement of the SM Higgs couplings result in stronger constraints than the ones obtained in this work.

However, our model independent approach allows to obtain bounds for all such extensions, some of which will most certainly have weaker bounds.

Our goal is to explore how angular distributions of SM particles may help probing the dark sector, by looking into the expected changes of these observables in the presence of this DM mediator. Several CP-observables have been proposed in the literature to probe the CP-nature of the coupling of top quarks to the Higgs boson at the LHC or future colliders, using mainly the  $ttH$  channel [24-54]. The vast majority of these variables are only sensitive to the square terms  $(g_{u_{33}}^{S})^{2}$  and  $(g_{u_{33}}^{P})^{2}$  that appear in the cross section of the interaction described by equation (2.1).

After looking in detail at several possible observables, we concluded that the most effective ones are the azimuthal angle difference  $\Delta \phi_{\ell -\ell +}$  of the charged leptons that come from the decay of top quarks, and the  $b_{4}$  variable evaluated in the laboratory frame (LAB),  $b_{4} = (p_{t}^{z}.p_{\bar{t}}^{z}) / (|\vec{p}_{t}|.\| \vec{p}_{\bar{t}}|)$ , where the  $z$ -direction corresponds to the beam direction, and  $\vec{p}_{t(\bar{t})}$  and  $p_{t(\bar{t})}^z$  correspond to the total and z-component of the top (anti-top) quark momentum measured in the LAB frame, respectively. It is worth noting that the  $b_{4}$  variable depends on the  $t$  and  $\bar{t}$  polar angles,  $\theta_t$  and  $\theta_{\bar{t}}$  respectively, with respect to the  $z$ -direction, and can be expressed as  $b_{4} = \cos \theta_{t}\times \cos \theta_{\bar{t}}$ . In order to evaluate this variable, the kinematic reconstruction of the  $t\bar{t}$  system needs to be accomplished. This will be discussed in the next sections.

We conclude this section with a comment about the relation between the total cross section  $pp \rightarrow t\bar{t}Y_0$  in the case of a scalar and of a pseudoscalar. This will be important later as the bounds on the scalar and on the pseudoscalar couplings are heavily dependent on the difference between the corresponding cross sections. The difference between the two cross sections was discussed in [15, 55]. There is a detailed discussion in [15] where it is argued that a spin-0 state with a mass well below all relevant energy scales can be treated as a parton radiated off the final state particles. Contrary to the pseudoscalar, the fragmentation function of the scalar has a soft singularity proportional to  $1 / x$  when the light scalar is radiated off top quarks. This particular feature expains the difference between the two cross section for very light particles.

# 3 Event generation and simulation

LHC-like signal and background events were generated with MadGraph5_aMC@NLO [56], with a centre-of-mass energy of  $13\mathrm{TeV}$ . The DM simplified model, DMsimp [22],<sup>1</sup> was used to generate  $pp \rightarrow t\bar{t}Y_0$  signal events, at Leading Order (LO). The pure scalar and pseudo-scalar signals were generated by setting the respective couplings as mentioned in the previous section (following the Lagrangian density in equation (2.1)). The mass of the DM mediator was set to  $m_{Y_0} = 0,1,10$  and  $125\mathrm{GeV}$ , and the top quark mass to  $m_t = 172.5\mathrm{GeV}$ . Only the dileptonic final state of the  $t\bar{t}$  system was considered ( $t\bar{t} \rightarrow bW^{+}\bar{b}W^{-} \rightarrow b\ell^{+}\nu_{\ell}\bar{\ell}\ell^{-}\bar{\nu}_{\ell}$ ), with the DM mediator forced not to decay, although if we allow the DM mediator to decay to mostly DM particles, the analysis and subsequent results do not change. Backgrounds from SM  $t\bar{t}$  (plus up to 3 jets),  $t\bar{t}V$  (plus up to 1 jet),  $t\bar{t}H$ , single top quark production ( $t-$ ,  $s-$ )

![](images/c88cf60ce681e6c4de03564a6c680e1cb04a5800057d22a5bb2389fadc29f719.jpg)  
Figure 1. Normalized TMVA input variable distributions for correct combinations (labeled as signal, in blue) and wrong combinations (labeled as background, in red), for a DM  $J^{P} = 0^{+}$  mediator. The  $\Delta R$  between the  $\ell^{+}$  and the  $b$ -jet from the  $t$  decay, is shown on the left plot. The corresponding  $\Delta \Phi$  distribution can be seen on the right.

![](images/3fec3c6aed29bf2b46d584f25ed9cfaed7b9d2fbcef9e7d9c7147a6b77ba778c.jpg)

and  $Wt$ -channels),  $W / Z$  (plus up to 4 jets),  $W(Z)b\bar{b}$  (plus up to 2 jets) and  $WW,ZZ,WZ$  diboson processes were also generated using MadGraph5_aMC@NLO at LO. Following event generation and hadronization by PYTHIA [57], all signal and background events went through a fast simulation of a typical LHC detector performed by Delphes [58], using the default ATLAS detector cards. Further details on the event generation and detector simulation can be found in [48]. The analysis of signal and background events is performed within the MadAnalysis5 [59] framework.

# 4 Event selection and kinematic reconstruction

Events are selected by requiring the jets and leptons reconstructed by Delphes to have their pseudo-rapidity $^2$ $\eta < 2.5$  and transverse momenta  $p_T > 20\mathrm{GeV}$ . Only events with two jets and two isolated leptons of opposite charge are accepted. To avoid contamination from the  $Z +$  jets background, we require the invariant mass of the two lepton system to fulfil  $|m_{\ell +\ell^{-}} - m_Z| > 10\mathrm{GeV}$ . Further details on the event selection criteria can be found in [49].

In the reconstruction of the  $t\bar{t}$  system, we assume the reconstructed leptons are the ones from the W decays, originated in the top quark decays. We then need to assign the reconstructed jets to the correct b-quarks from the associated top quarks. In order to avoid mismatches, once two jets are present in the final state, we use multivariate statistical methods from the Toolkit for Multivariate Data Analysis, TMVA [60], to find the right pairing of jets and leptons.

To that effect we use several distributions (which already include hadronization and shower effects), where right and wrong combinations are compared. A wrong combination happens whenever a jet not originating from a top decay is assigned to its corresponding

![](images/0032c028b1a676c947207ce0fb9f9c555da34640c60cbd614e9e81651c5ebd97.jpg)  
Figure 2. Normalized TMVA input variable distributions for correct combinations (labeled as signal, in blue) and wrong combinations (labeled as background, in red), for a DM  $J^{P} = 0^{+}$  mediator. The  $\Delta \theta$  between the  $\ell^{+}$  and the  $b$ -jet from the  $t$  decay is shown on the left and the lepton plus  $b$ -jet mass difference is shown on the right.

![](images/27f36d3459c1f9424f67be256b7f26cc6e01c74a7857b33ab026b50a423b6e0e.jpg)

b-quark. Right (labelled as Signal, in blue) and wrong (labelled as Background, in red) combinations are represented in figures 1 and 2, for the  $\Delta R$ , $^3$ $\Delta \Phi$  and  $\Delta \theta$  between the  $\ell^{+}$ lepton and the jet from the hadronization of the  $b$ -quark (originated in the  $t$  decay and labelled as  $b_{t}$ ). Similar distributions were also obtained for the  $\ell^{-}$ lepton, and used to optimize finding the right combination. Clear differences between the wrong and right combinations are visible in all distributions shown. The invariant mass difference between the pairs  $(b_{t},l^{+})$  and  $(\bar{b}_{\bar{t}},l^{-})$  is also shown in figure 2, for the right and wrong combinations. Several multivariate statistical methods were then trained by TMVA, using right and wrong combinations distributions for training and testing. All individual distributions were combined into a single discriminant classifier for each one of the methods. In figure 3 (left), we show the Receiver Operating Characteristic (ROC) curve for the  $Y_{0}$  scalar  $(J^{P} = 0^{+})$  and pseudo-scalar  $(J^{P} = 0^{-})$  mediators in the top and bottom plots, respectively. From the ROC curves we can see that the best method is a Boosted Decision Tree with Gradient boost (BDTG). The corresponding classifier outputs are shown in figure 3 (right), for scalar and pseudo-scalar DM mediators in the top and bottom plots, respectively. From the comparison between both cases, we can see that the scalar mediator is more challenging, with a slightly worse ROC curve. For this reason, from this point on, all results shown originate directly from the scalar mediator analysis, since this case represents the most conservative scenario.

![](images/5ba76e0c344d2204bb6d48b57d9279278fa8ba1db1e6c597072ce17ed74279f3.jpg)

![](images/d53e8684b18b5fd4a0ece4f5d04b7efa40b176db3f3dd9c9a662a653b89da716.jpg)

![](images/a1291ab8110befb9f4f5a97ea9ba6f07482883eb4210bf7d443dbec8058a404e.jpg)  
Figure 3. Background rejection versus signal acceptance (ROC curve) for different multi-variate methods are compared, for the  $J^{P} = 0^{+}$  mediator (top left). The distribution of the best classifier (BDTG) is also shown (top right). The equivalent plots for the case of the  $J^{P} = 0^{-}$  mediator, are shown in the bottom plots.

![](images/c2ca5bde95fe10dc29996388480da92db0d8561c4f9f5811d49b01cea1fb2867.jpg)

To reconstruct the 3-momentum of the undetected neutrinos from the top quark decays, we impose the following energy-momentum conservation conditions to events,

$$
(p _ {\nu} + p _ {\ell^ {+}}) ^ {2} = m _ {W} ^ {2},
$$

$$
\left(p _ {\bar {\nu}} + p _ {\ell^ {-}}\right) ^ {2} = m _ {W} ^ {2},
$$

$$
\left(p _ {W ^ {+}} + p _ {b}\right) ^ {2} = m _ {t} ^ {2}, \tag {4.1}
$$

$$
\left(p _ {W ^ {-}} + p _ {\bar {b}}\right) ^ {2} = m _ {\bar {t}} ^ {2},
$$

$$
p _ {\nu} ^ {x} + p _ {\bar {\nu}} ^ {x} = \not E ^ {x},
$$

$$
p _ {\nu} ^ {y} + p _ {\bar {\nu}} ^ {y} = \not E ^ {y},
$$

where  $p_{\varsigma}\left(p_{\varsigma}^{\kappa}\right)$  represents the four-momentum of particle  $\varsigma$  (its projection along the  $\kappa$ -axis). In the first four equations mass constraints are imposed, where neutrinos and charged leptons are assumed to reconstruct the masses of the  $W$  bosons they originated from which, when combined with the right jet, should reconstruct the correspondent top quark masses. We also consider (last two equations) the total missing transverse energy is wholly accounted for by the neutrinos. In this approximation, we are assuming the DM mediator contribution

![](images/302d9cb1f0d42e2f71192745aa92df683291e36a1d08ef3d882ba8e09d31c2f1.jpg)

![](images/9ac455cd4fb3b2f53318083decab211ec1e06f796e8f20ca699274d04b01ae37.jpg)

![](images/08ef752a0dc3989e76b8c9f0519e31fc82484877398ce46b43fffd8772837c35.jpg)  
Figure 4. Two-Dimensional distributions of  $t\bar{t}Y_{0^{+}}$ events: generator-level transverse momentum versus reconstructed transverse momentum for several particles (neutrino, top left;  $t$ , top right;  $t\bar{t}$  system, bottom left;  $\mathrm{W}^{+}$ boson, bottom right), for the massless DM mediator.

![](images/f1fa010770d5e164e329dcc094eda84a4c2716dff51a0dc02459d559902dcd8e.jpg)

to the missing transverse energy to be negligible (as well as its  $z$ -axis component) when compared to the neutrinos contribution. In order to find the best solution for each event, the top quark and  $W$  boson mass values, used by the fit, were sampled 500 times from 2-dimensional probability distribution functions  $(p.d.f.s)$  obtained from parton level (with shower effects)  $t\bar{t}Y_0$  signal events (see [49], for more details). The neutrinos four-momenta are obtained from solving the set of equations (4.1), above. If a solution is found, new mass values are tried around the found value (up to 6 times), to check if neighbour mass points can indeed provide a better fit overall. Due to the quadratic form of the mass equations, multiple solutions may exist for a single event. We chose the solution that provides the highest value of the likelihood  $(L)$  constructed using parton level (with shower effects) distributions, in particular the  $p.d.f.s$  for the transverse momenta of the neutrinos, top quarks and  $t\bar{t}$  system,  $P(p_{T_\nu})$ ,  $P(p_{T_\bar{\nu}})$ ,  $P(p_{T_t})$ ,  $P(p_{T_{\bar{t}}})$  and  $P(p_{T_{tt}})$ , respectively. This

likelihood is defined according to

$$
L \propto \frac {1}{p _ {T _ {\nu}} p _ {T _ {\bar {\nu}}}} P \left(p _ {T _ {\nu}}\right) P \left(p _ {T _ {\bar {\nu}}}\right) P \left(p _ {T _ {t}}\right) P \left(p _ {T _ {\bar {t}}}\right) P \left(p _ {T _ {t \bar {t}}}\right), \tag {4.2}
$$

where the normalization factor  $1 / p_{T_\nu}p_{T_\bar{\nu}}$  is applied to account for the energy losses due to radiation emission and effects from detector resolutions which will increase the reconstructed neutrino 4-momentum. This factor compensates for values of neutrino  $p_T$  which are too extreme by giving less weight to those solutions. If no solution is found, the event is discarded. For a scalar (pseudo-scalar) DM mediator mass of  $0\mathrm{GeV}$ , we found that  $75\%$ $(72\%)$  of all events were correctly reconstructed, a number that matches quite well typical SM  $t\bar{t}$  analyses where such kinematic reconstruction is attempted.

In figure 4, we show the 2-dimensional  $p_T$  distributions of the neutrino (top left), top quark (top right),  $tt$  system (bottom left) and  $W^{+}$  boson (bottom right), after kinematic reconstruction. We can see that the parton level (with shower effects) and the reconstructed kinematics are highly correlated for all particles or systems of particles. This implies that, after experimental effects are taken into account, it is still possible to reconstruct the  $tt$  system without even trying to reconstruct the invisible DM mediator. This point is quite important since it opens up the possibility of studying the changes in angular distributions of  $tt$  systems in the presence of a new invisible particle.

# 5 Results and discussion

In figure 5, we show the  $b_{4}$  (left) and  $\Delta \phi_{\ell + \ell^{-}}$  (right) distributions after event selection and kinematic reconstruction, for a reference luminosity of  $100 \, \mathrm{fb}^{-1}$ . All SM backgrounds:  $t\bar{t}$  ( $t\bar{t} c\bar{c}$  and  $t\bar{t} +$  light jets),  $t\bar{t} b\bar{b}$ ,  $t\bar{t} V$ ,  $t\bar{t} H$ , single top quark production ( $t-$ ,  $s-$  and  $Wt$ -channels),  $W / Z +$  jets, and diboson ( $WW, ZZ, WZ$ ) events are represented. The  $t\bar{t} Y_{0}$  scalar and pseudo-scalar signals, with  $m_{Y_0} = 0 \, \mathrm{GeV}$ , are shown as well, scaled by factors of 2 and 500 respectively, for convenience. As expected, the main SM background contribution is the  $t\bar{t}$  due to its similarity with the signal final state topology. All other backgrounds are essentially residual to the overall SM background contribution. Differences in the shapes of the background distributions can also be noticed when compared with the signals. For instance, in the  $b_{4}$  distribution and for the scalar signal (in brown), events tend to populate positive values more than negative values. This behaviour is inverted for the pseudo-scalar case (in orange). For the  $\Delta \phi_{\ell + \ell^{-}}$  distribution (which is symmetric around zero), the scalar and pseudo-scalar signals populate differently its extreme regions. For completeness, we show in figure 6 the missing transverse energy ( $E_T$ ) distribution, which shows a quite similar behaviour to the SM background one, for both the CP-even and CP-odd signals. This means that missing  $E_T$  is not a good discriminating variable for this process which is a very important point to make in an analysis for a process with DM in the final state.

The  $b_{4}$  and  $\Delta \phi_{\ell + \ell^{-}}$  distributions were then used to set confidence level limits (CLs) on the exclusion of the SM with a new CP-mixed massless DM mediator particle,  $Y_{0}$ , assuming the SM hypothesis as the null hypothesis (Scenario 1). The result is shown in figure 7, for an integrated luminosity corresponding roughly to the RUN 2 luminosity plus the contribution

![](images/f1ea981679711eefe76492f73e886cad7a4c1f6322ea144fcf52762030990316.jpg)  
Figure 5. The  $b_{4}$  (left) and  $\Delta \phi_{\ell + \ell^{-}}$  (right) distributions for scalar and pseudo-scalar signals (dashed curves) together with the SM processes (full lines) with dileptonic final states, are represented after event selection and kinematic reconstruction (exp), for a reference luminosity of  $100\mathrm{fb}^{-1}$ . Scaling factors are applied to the scalar and pseudo-scalar signals for convenience.

![](images/558c4109187a125f8f8219467ed31603c0d3dbe17a347679e1bae78f9f48a15c.jpg)

![](images/8cd1ac7f10239e37a391ca59a6513a4b7cc99a84dc6adc41cdd625ad7823700b.jpg)  
Figure 6. Missing transverse energy  $(E_T)$  distributions for scalar and pseudo-scalar signals (dashed curves) together with the SM processes (full lines) with dileptonic final states, are represented after event selection and kinematic reconstruction (exp), for a reference luminosity of  $100\mathrm{fb}^{-1}$ . Scaling factors are applied to the scalar and pseudo-scalar signals for convenience.

![](images/eb2915151891c5701170e10c7859e6a5996079356af7e8cf17fb533e463714f2.jpg)  
Figure 7. CLs for the exclusion of the SM with a massless DM mediator,  $Y_{0}$ , with mixed scalar and pseudo-scalar couplings with the top quarks, against the SM as null hypothesis, for the  $\Delta \phi$  between the charged leptons,  $\Delta \phi_{\ell +\ell^{-}}$  (left), and  $b_{4}$  (right) observables. Limits are shown for a luminosity of  $L = 200\mathrm{fb}^{-1}$ .

![](images/6490692dae4a1b823b95ece4e5e67a3219e9f6a0a1eb8ece91228aa016fd330b.jpg)

Table 1. Exclusion limits for the  $t\bar{t}Y_0$  CP-couplings for fixed luminosities of  $200\mathrm{fb}^{-1}$  and  $3000\mathrm{fb}^{-1}$  of the SM plus  $Y_0$ , assuming the SM as the null hypothesis. The limits are shown at confidence levels of  $68\%$  and  $95\%$ , for the  $\Delta \phi_{l + l - }$  variable.  

<table><tr><td colspan="2">Exclusion Limits from Δφl+l-</td><td colspan="2">L = 200 fb-1(68% CL) (95% CL)</td><td colspan="2">L = 3000 fb-1(68% CL) (95% CL)</td></tr><tr><td>mY0= 0 GeV</td><td>gSu33∈gPu33∈</td><td>[-0.067, +0.067] [-0.91, +0.91]</td><td>[-0.125, +0.125] [-1.71, +1.71]</td><td>[-0.022, +0.022] [-0.44, +0.44]</td><td>[-0.052, +0.052] [-0.85, +0.85]</td></tr></table>

from the first year of RUN 3, i.e.,  $L \sim 200\mathrm{fb}^{-1}$ . The CL limits are shown as contour plots in the  $(g_{u_{33}}^{S}, g_{u_{33}}^{P})$  2D plane. It is clear that the CLs are identical for both observables, in this scenario.

The CLs are also evaluated, for Scenario 1, for the full luminosity expected at the end of the High-Luminosity phase of the LHC (HL-LHC), for  $L = 3000\mathrm{fb}^{-1}$ , using the  $\Delta \phi_{\ell +\ell -}$  distribution. The resulting  $68\%$  and  $95\%$  exclusion limits, for both luminosity values, are in table 1. For  $L = 3000\mathrm{fb}^{-1}$ , we observe a substantial improvement by factors of 2 to 3, on the exclusion limits. Quite similar results where obtained when using a simple counting experiment. This leads us to conclude that the observable choice has little to no impact on the exclusion limits in this scenario and the DM mediator production cross section is, in itself, the dominant factor.

For completeness, an alternative scenario was considered (Scenario 2), where we assumed as null hypothesis the SM plus a pure CP-even DM mediator of mass  $0\mathrm{GeV}$ . The main goal of this scenario is to quantify how well could the mixed state be excluded from a pure CP-even mediator, in case of a discovery. This scenario was explored by using the  $\Delta \phi_{\ell +\ell -}$  distribution as well as the simple counting experiment used above for Scenario 1. The results are shown in figure 8. Here, however, the difference between both distributions is quite clear, i.e., the  $68\%$  CLs are much worse in the latter case. This indicates that, in Scenario 2, in contrast with Scenario 1, the chosen observable will have an important

![](images/d0de5d56f26b80c84ca7552d78b530337833aabc77994c47adc8bd7b3622a7a4.jpg)  
Figure 8. CLs for the exclusion of the SM with a massless DM mediator,  $Y_0$ , with mixed scalar and pseudo-scalar couplings with the top quarks, against the SM plus a pure scalar DM mediator, for the  $\Delta \phi$  between the charged leptons (left). For completeness, the results for a simple event counting experiment (one Bin) is also shown (right). Limits are represented for a luminosity of  $L = 200\mathrm{fb}^{-1}$ .

![](images/34f259b39cfe0f47276ba53befd136093802911065cdbede64ad97abe331a106.jpg)

impact on the exclusion limits. This also means that angular observables can indeed help on studying the CP-nature of DM mediators upon discovery.

Lastly, to extend our results to a massive  $Y_{0}$  produced together with pairs of top quarks, additional signal events were generated with mediator masses  $(m_{Y_0})$  set to 1, 10 and 125 GeV. The selection criteria and reconstruction procedure described in section 4 were the same. The resulting  $\Delta \phi_{\ell +\ell^{-}}$  distributions were then used to set CLs, in both Scenarios 1 and 2, for a luminosity of  $200\mathrm{fb}^{-1}$  and  $3000\mathrm{fb}^{-1}$  as before. The exclusion limits are depicted for all masses in figure 9, for  $L = 3000\mathrm{fb}^{-1}$ . The respective  $68\%$  and  $95\%$  exclusion limits for Scenario 1 are shown in table 2, for both  $L = 200\mathrm{fb}^{-1}$  and  $L = 3000\mathrm{fb}^{-1}$ . As expected, exclusion limits worsen as masses increase in both Scenarios, since the  $ttY_{0}$  production cross section decreases for heavier  $Y_{0}$  masses, and improve with increasing luminosity values. Also, notice that the observable choice having a very small impact on the exclusion limits in Scenario 1 is true only for smaller DM mediator masses, where the  $Y_{0}$  production cross section is the dominant factor contributing to the exclusion limits.

# 6 Conclusions

In this work we have explored the idea of using on-going searches and measurements, such as the analysis that leads to the measurement of the  $t\bar{t}$  production cross section at the LHC, to look for hidden DM particles in the final states. To that end, we present a new approach to fully reconstruct the kinematics of the  $t\bar{t}$  system present in  $t\bar{t}Y_{0}$  events produced at the LHC. Our study was performed within the context of simplified models of DM production at colliders. In this kinematic reconstruction, the missing transverse energy was fully attributed to the undetected neutrinos and no attempt to reconstruct the invisible DM mediator was tried. The approximations used in our work appear to be valid in a wider range of the DM mediator mass (starting at  $m_{Y_0} = 0 \mathrm{GeV}$ ), according to the resulting correlations between the generated and reconstructed kinematics. An example of these correlations is shown in figure 4 for the  $m_{Y_0} = 0 \mathrm{GeV}$  case. Moreover, we have checked that

![](images/b441875c71947e53b7b9dc72e74d6a64debafec6519f56ba6b9856446e899a0f.jpg)

![](images/cc1ff9aa1feff5eb3f6d632a8f7cfe0bba6e93bbbe1ec31f25f8830b37013aef.jpg)

![](images/f585caf647318414c9999fc88eb8f19a7aff492af06673464924f49b08a38358.jpg)

![](images/dc8af2a5caedc7c8fd27c41951c6964f1cb4deb5ebe8709c919e573706fffb47.jpg)

![](images/c4cba7dcfe88c7dcd5c4a66a2406e96d8437e29b5c59103f74af9a50cb0b4bbd.jpg)  
Figure 9. CLs for the exclusion of the SM with a massive DM mediator,  $Y_{0}$  ( $m_{Y_{0}} = 1$ , 10 and  $125\mathrm{GeV}$  in the top, middle, and bottom rows, respectively), with mixed scalar and pseudo-scalar couplings, against the SM as null hypothesis (left), for the  $\Delta \phi$  between the charged leptons. For completeness, the corresponding CL for the exclusion of the SM plus a mixed DM mediator against the SM plus a pure scalar DM mediator is also shown for  $\Delta \phi$  (right). Limits are shown for a luminosity corresponding to the full HL-LHC luminosity ( $L = 3000\mathrm{fb^{-1}}$ ).

![](images/91314284b7a20e13ceaa1863b12fd59785a8cb23511b92eb259dc570acd35a5b.jpg)

Table 2. Exclusion limits for the  $t\bar{t}Y_0$  CP-couplings for fixed luminosities of  $200\mathrm{fb^{-1}}$  and  $3000\mathrm{fb^{-1}}$  of the SM plus  $Y_0$ , assuming the SM as null hypothesis, for  $Y_0$  masses of  $1\mathrm{GeV}$  (top),  $10\mathrm{GeV}$  (middle) and  $125\mathrm{GeV}$  (bottom). The limits are shown at confidence levels of  $68\%$  and  $95\%$ , for the  $\Delta \phi_{l+l-}$  variable.  

<table><tr><td colspan="2">Exclusion Limits from Δφl+l-</td><td>L=200 fb-1(68% CL)</td><td>(95% CL)</td><td>L=3000 fb-1(68% CL)</td><td>(95% CL)</td></tr><tr><td rowspan="2">mY0=1 GeV</td><td>gSu33∈</td><td>[-0.073, +0.073]</td><td>[-0.142, +0.142]</td><td>[-0.038, +0.038]</td><td>[-0.068, +0.068]</td></tr><tr><td>gPu33∈</td><td>[-0.89, +0.89]</td><td>[-1.65, +1.65]</td><td>[-0.43, +0.43]</td><td>[-0.83, +0.83]</td></tr><tr><td rowspan="2">mY0=10 GeV</td><td>gSu33∈</td><td>[-0.198, +0.198]</td><td>[-0.368, +0.372]</td><td>[-0.098, +0.098]</td><td>[-0.188, +0.188]</td></tr><tr><td>gPu33∈</td><td>[-0.87, +0.87]</td><td>[-1.65, +1.65]</td><td>[-0.44, +0.44]</td><td>[-0.83, +0.83]</td></tr><tr><td rowspan="2">mY0=125 GeV</td><td>gSu33∈</td><td>[-0.328, +0.322]</td><td>[-0.608, +0.612]</td><td>[-0.162, +0.162]</td><td>[-0.308, +0.308]</td></tr><tr><td>gPu33∈</td><td>[-1.48, +1.49]</td><td>[-2.77, +2.78]</td><td>[-0.75, +0.75]</td><td>[-1.41, +1.41]</td></tr></table>

the pairing of the  $b$ -jets and charged leptons originated from the same parent top quark decay was very well achieved using several angular distributions and dedicated multivariate statistical methods.

We have analyzed a significant number of angular observables, from which two of them were selected to illustrate our findings, the  $\Delta \phi_{\ell + \ell^{-}}$  and  $b_4$  distributions. These observables were shown to be sensitive not only to DM mediators with different mass scales, but also with different CP-natures, in what concerns their couplings to heavy SM particles. These distributions were then used to set exclusion limits assuming the SM as the null hypothesis, for a luminosity of  $200\mathrm{fb}^{-1}$  and  $3000\mathrm{fb}^{-1}$ , corresponding to the full luminosity of the High-Luminosity Phase of the LHC (HL-LHC). We also considered a benchmark scenario that takes into account, as null hypothesis, the SM plus a pure scalar DM mediator, in order to check how sensitive the analysis is to a possible CP-mixed nature of the DM mediator. We observe that, in the former case, the  $95\%$  CL limits using the  $\Delta \phi_{\ell + \ell^{-}}$  angular distribution were  $g_{u_{33}}^S \in [-0.125, 0.125]$  and  $g_{u_{33}}^P \in [-1.71, 1.71]$  for a luminosity of  $200\mathrm{fb}^{-1}$ , and  $g_{u_{33}}^S \in [-0.052, 0.052]$  and  $g_{u_{33}}^P \in [-0.85, 0.85]$  for a luminosity of  $3000\mathrm{fb}^{-1}$ . We have also checked that a simple counting experiment can provide similar exclusion limits. In the second case, we observed that the use of angular distributions can improve the exclusion limits for the pseudo-scalar coupling by at least a factor of two, if we want to understand the CP-nature of the DM mediator couplings to SM particles. Finally, we extended our study to the case of a massive DM mediator with  $m_{Y_0}$  set to 1, 10 and  $125\mathrm{GeV}$ . We observed that the exclusion limits set from the  $\Delta \phi_{\ell + \ell^{-}}$  distributions got worse for increasing  $Y_0$  masses, since the  $ttY_0$  cross section decreases in that case.

# Acknowledgments

R.C. and R.S. are partially supported by the Portuguese Foundation for Science and Technology (FCT) under Contracts no. UIDB/00618/2020, UIDP/00618/2020, CERN/FISPAR/0025/2021 CERN/FIS-PAR/0010/2021 and CERN/FIS-PAR/0021/2021. R.C. is

additionally supported by FCT Grant No. 2020.08221.BD. A.O. is partially supported by FCT, under the Contract CERN/FIS-PAR/0037/2021. D.A. is supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) under grant 396021762 - TRR 257.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] H. Hoekstra, H. Yee and M. Gladders, Current status of weak gravitational lensing, New Astron. Rev. 46 (2002) 767 [astro-ph/0205205] [INSPIRE].  
[2] L.V.E. Koopmans and T. Treu, The structure and dynamics of luminous and dark matter in the early-type lens galaxy of 0047-281 at  $z = 0.485$ , Astrophys. J. 583 (2003) 606 [astro-ph/0205281] [INSPIRE].  
[3] R.B. Metcalf, L.A. Moustakas, A.J. Bunker and I.R. Parry, Spectroscopic gravitational lensing and limits on the dark matter substructure in  $Q2237 + 0305$ , Astrophys. J. 607 (2004) 43 [astro-ph/0309738] [INSPIRE].  
[4] L.A. Moustakas and R.B. Metcalf, Detecting dark matter substructure spectroscopically in strong gravitational lenses, Mon. Not. Roy. Astron. Soc. 339 (2003) 607 [astro-ph/0206176] [INSPIRE].  
[5] V.C. Rubin and W.K. Ford Jr., Rotation of the Andromeda Nebula from a Spectroscopic Survey of Emission Regions, Astrophys. J. 159 (1970) 379 [INSPIRE].  
[6] D. Clowe, A. Gonzalez and M. Markevitch, Weak lensing mass reconstruction of the interacting cluster 1E0657-558: Direct evidence for the existence of dark matter, Astrophys. J. 604 (2004) 596 [astro-ph/0312273] [INSPIRE].  
[7] C. Weinheimer, Laboratory limits on neutrino masses, Springer Tracts Mod. Phys. 190 (2003) 25 [INSPIRE].  
[8] L.J. Rosenberg and K.A. van Bibber, Searches for invisible axions, Phys. Rept. 325 (2000) 1 [INSPIRE].  
[9] M. Schumann, Direct Detection of WIMP Dark Matter: Concepts and Status, J. Phys. G 46 (2019) 103003 [arXiv:1903.03026] [INSPIRE].  
[10] ATLAS collaboration, Search for new phenomena in mono-  $X$  final states using pp collision data collected in Run-2 by the ATLAS experiment at the LHC, PoS ICHEP2020 (2021) 658 [INSPIRE].  
[11] CMS collaboration, Search for Dark Matter with mono- $X$  Signatures in CMS, PoS ICHEP2022 (2022) 260 [INSPIRE].  
[12] ATLAS collaboration, Combination of searches for invisible decays of the Higgs boson using  $139fb^{-1}$  of proton-proton collision data at  $s = 13$  TeV collected with the ATLAS experiment, Phys. Lett. B 842 (2023) 137963 [arXiv:2301.10731] [INSPIRE].  
[13] T. Biekötter and M. Pierre, Higgs-boson visible and invisible constraints on hidden sectors, Eur. Phys. J. C 82 (2022) 1026 [arXiv:2208.05505] [INSPIRE].

[14] CMS collaboration, Searches for Higgs boson rare and invisible decays at CMS, PoS ICHEP2020 (2021) 070 [INSPIRE].  
[15] U. Haisch, P. Pani and G. Polesello, Determining the CP nature of spin-0 mediators in associated production of dark matter and  $\bar{t} \bar{t}$  pairs, JHEP 02 (2017) 131 [arXiv:1611.09841] [INSPIRE].  
[16] U. Haisch and G. Polesello, Searching for production of dark matter in association with top quarks at the LHC, JHEP 02 (2019) 029 [arXiv:1812.00694] [INSPIRE].  
[17] J. Hermann and M. Worek, The impact of top-quark modelling on the exclusion limits in  $t\bar{t} + DM$  searches at the LHC, Eur. Phys. J. C 81 (2021) 1029 [arXiv:2108.01089] [INSPIRE].  
[18] U. Haisch, G. Polesello and S. Schulte, Searching for pseudo Nambu-Goldstone boson dark matter production in association with top quarks, JHEP 09 (2021) 206 [arXiv:2107.12389] [INSPIRE].  
[19] Z. Han, A. Katz, D. Krohn and M. Reece, (Light) Stop Signs, JHEP 08 (2012) 083 [arXiv:1205.5808] [INSPIRE].  
[20] C. Brust, A. Katz and R. Sundrum, SUSY Stops at a Bump, JHEP 08 (2012) 059 [arXiv:1206.2353] [INSPIRE].  
[21] Z. Han and A. Katz, Stealth Stops and Spin Correlation: A Snowmass White Paper, in the proceedings of the Snowmass 2013, Minneapolis, U.S.A., July 29 - August 06 (2013) [arXiv:1310.0356] [INSPIRE].  
[22] M. Backović et al., Higher-order QCD predictions for dark matter production at the LHC in simplified models with s-channel mediators, Eur. Phys. J. C 75 (2015) 1.  
[23] D. Azevedo et al., CP in the dark, JHEP 11 (2018) 091 [arXiv:1807.10322] [INSPIRE].  
[24] W. Bernreuther and A. Brandenburg, Tracing CP violation in the production of top quark pairs by multiple TeV proton proton collisions, Phys. Rev. D 49 (1994) 4481 [hep-ph/9312210] [INSPIRE].  
[25] J.F. Gunion and X.-G. He, Determining the CP nature of a neutral Higgs boson at the LHC, Phys. Rev. Lett. 76 (1996) 4468 [hep-ph/9602226] [INSPIRE].  
[26] P.S. Bhupal Dev et al., Determining the CP properties of the Higgs boson, Phys. Rev. Lett. 100 (2008) 051801 [arXiv:0707.2878] [INSPIRE].  
[27] R. Frederix et al., Scalar and pseudoscalar Higgs production in association with a top-antitop pair, Phys. Lett. B 701 (2011) 427 [arXiv:1104.5613] [INSPIRE].  
[28] J. Ellis, D.S. Hwang, K. Sakurai and M. Takeuchi, Disentangling Higgs-Top Couplings in Associated Production, JHEP 04 (2014) 004 [arXiv:1312.5736] [INSPIRE].  
[29] S. Khatibi and M. Mohammadi Najafabadi, Exploring the Anomalous Higgs-top Couplings, Phys. Rev. D 90 (2014) 074014 [arXiv:1409.6553] [INSPIRE].  
[30] F. Demartin et al., Higgs characterisation at NLO in QCD: CP properties of the top-quark Yukawa interaction, Eur. Phys. J. C 74 (2014) 3065 [arXiv:1407.5089] [INSPIRE].  
[31] A. Kobakhidze, L. Wu and J. Yue, Anomalous Top-Higgs Couplings and Top Polarisation in Single Top and Higgs Associated Production at the LHC, JHEP 10 (2014) 100 [arXiv:1406.1961] [INSPIRE].

[32] J. Bramante, A. Delgado and A. Martin, Cornering a hyper Higgs boson: Angular kinematics for boosted Higgs bosons with top pairs, Phys. Rev. D 89 (2014) 093006 [arXiv:1402.5985] [INSPIRE].  
[33] F. Boudjema, R.M. Godbole, D. Guadagnoli and K.A. Mohan, Lab-frame observables for probing the top-Higgs interaction, Phys. Rev. D 92 (2015) 015019 [arXiv:1501.03157] [INSPIRE].  
[34] X.-G. He, G.-N. Li and Y.-J. Zheng, Probing Higgs boson CP Properties with  $t\bar{t}H$  at the LHC and the 100 TeV pp collider, Int. J. Mod. Phys. A 30 (2015) 1550156 [arXiv:1501.00012] [INSPIRE].  
[35] S.P. Amor dos Santos et al., Angular distributions in  $t\bar{t}H(H \to b\bar{b})$  reconstructed events at the LHC, Phys. Rev. D 92 (2015) 034021 [arXiv:1503.07787] [INSPIRE].  
[36] A.V. Gritsan, R. Röntsch, M. Schulze and M. Xiao, Constraining anomalous Higgs boson couplings to the heavy flavor fermions using matrix element techniques, Phys. Rev. D 94 (2016) 055023 [arXiv:1606.03107] [INSPIRE].  
[37] M.J. Dolan, M. Spannowsky, Q. Wang and Z.-H. Yu, Determining the quantum numbers of simplified models in  $t\bar{t}X$  production at the LHC, Phys. Rev. D 94 (2016) 015025 [arXiv:1606.00019] [INSPIRE].  
[38] D. Gonçalves and D. López-Val, Pseudoscalar searches with dileptonic tops and jet substructure, Phys. Rev. D 94 (2016) 095005 [arXiv:1607.08614] [INSPIRE].  
[39] M.R. Buckley and D. Gonçalves, Constraining the Strength and CP Structure of Dark Production at the LHC: the Associated Top-Pair Channel, Phys. Rev. D 93 (2016) 034003 [arXiv:1511.06451] [INSPIRE].  
[40] N. Mileo et al., Pseudoscalar top-Higgs coupling: exploration of CP-odd observables to resolve the sign ambiguity, JHEP 07 (2016) 056 [arXiv:1603.03632] [INSPIRE].  
[41] M.R. Buckley and D. Gonçalves, Boosting the Direct CP Measurement of the Higgs-Top Coupling, Phys. Rev. Lett. 116 (2016) 091801 [arXiv:1507.07926] [INSPIRE].  
[42] S. Amor Dos Santos et al., Probing the CP nature of the Higgs coupling in  $t\bar{t}h$  events at the LHC, Phys. Rev. D 96 (2017) 013004 [arXiv:1704.03565] [INSPIRE].  
[43] D. Gonçalves, K. Kong and J.H. Kim, Probing the top-Higgs Yukawa CP structure in dileptonic  $\bar{t} \bar{t} \bar{h}$  with  $M_2$ -assisted reconstruction, JHEP 06 (2018) 079 [arXiv:1804.05874] [INSPIRE].  
[44] D. Azevedo, A. Onofre, F. Filthaut and R. Gonçalo, CP tests of Higgs couplings in  $t\bar{t}$  semileptonic events at the LHC, Phys. Rev. D 98 (2018) 033004 [arXiv:1711.05292] [INSPIRE].  
[45] J. Li, Z.-G. Si, L. Wu and J. Yue, Central-edge asymmetry as a probe of Higgs-top coupling in t $\bar{t}$ h production at the LHC, Phys. Lett. B 779 (2018) 72 [arXiv:1701.00224] [INSPIRE].  
[46] A. Ferroglia, M.C.N. Fiolhais, E. Gouveia and A. Onofre, Role of the  $t$ th rest frame in direct top-quark Yukawa coupling measurements, Phys. Rev. D 100 (2019) 075034 [arXiv:1909.00490] [INSPIRE].  
[47] D.A. Faroughy, J.F. Kamenik, N. Košnik and A. Smolkovič, Probing the CP nature of the top quark Yukawa at hadron colliders, JHEP 02 (2020) 085 [arXiv:1909.00007] [INSPIRE].  
[48] D. Azevedo, R. Capucha, A. Onofre and R. Santos, Scalar mass dependence of angular variables in  $t\bar{t}\phi$  production, JHEP 06 (2020) 155 [arXiv:2003.09043] [INSPIRE].

[49] D. Azevedo et al., Light Higgs searches in  $t\bar{t}\phi$  production at the LHC, JHEP 04 (2021) 077 [arXiv:2012.10730] [INSPIRE].  
[50] B. Bortolato, J.F. Kamenik, N. Košnik and A. Smolkovič, Optimized probes of CP -odd effects in the tth process at hadron colliders, Nucl. Phys. B 964 (2021) 115328 [arXiv:2006.13110] [INSPIRE].  
[51] Q.-H. Cao, K.-P. Xie, H. Zhang and R. Zhang, A New Observable for Measuring CP Property of Top-Higgs Interaction, Chin. Phys. C 45 (2021) 023117 [arXiv:2008.13442] [INSPIRE].  
[52] D. Gonçalves, J.H. Kim, K. Kong and Y. Wu, Direct Higgs-top CP-phase measurement with  $t\bar{t}h$  at the 14 TeV LHC and 100 TeV FCC, JHEP 01 (2022) 158 [arXiv:2108.01083] [INSPIRE].  
[53] R.K. Barman, D. Gonçalves and F. Kling, Machine learning the Higgs boson-top quark CP phase, Phys. Rev. D 105 (2022) 035023 [arXiv:2110.07635] [INSPIRE].  
[54] D. Azevedo, R. Capucha, A. Onofre and R. Santos,  $CP$ -violation, asymmetries and interferences in  $t\bar{t}\phi$ , JHEP 09 (2022) 246 [arXiv:2208.04271] [INSPIRE].  
[55] M. Backović et al., Higher-order QCD predictions for dark matter production at the LHC in simplified models with s-channel mediators, Eur. Phys. J. C 75 (2015) 482 [arXiv:1508.05327] [INSPIRE].  
[56] J. Alwall et al., MadGraph 5: Going Beyond, JHEP 06 (2011) 128 [arXiv:1106.0522] [INSPIRE].  
[57] T. Sjostrand, S. Mrenna and P.Z. Skands, PYTHIA 6.4 Physics and Manual, JHEP 05 (2006) 026 [hep-ph/0603175] [INSPIRE].  
[58] DELPHES 3 collaboration, DELPHES 3, A modular framework for fast simulation of a generic collider experiment, JHEP 02 (2014) 057 [arXiv:1307.6346] [INSPIRE].  
[59] E. Conte, B. Fuks and G. Serret, MadAnalysis 5, A User-Friendly Framework for Collider Phenomenology, Comput. Phys. Commun. 184 (2013) 222 [arXiv:1206.1599] [INSPIRE].  
[60] A. Hoecker et al., TMVA-toolkit for multivariate data analysis, physics/0703039.