# Sensitivity to  $\mathcal{CP}$ -violating effective couplings in the top-Higgs sector

Víctor Miralles, Yvonne Peters, Eleni Vryonidou and Joshua K. Winter

Department of Physics and Astronomy, University of Manchester,

Oxford Road, Manchester M13 9PL, U.K.

E-mail: victor.miralles@manchester.ac.uk, yvonne.peters@manchester.ac.uk,

eleni.vryonidou@manchester.ac.uk, joshua.winter@manchester.ac.uk

ABSTRACT: The observed baryon asymmetry of the Universe requires new sources of charge-parity  $(\mathcal{CP})$  violation beyond those in the Standard Model. In this work, we investigate  $\mathcal{CP}$ -violating effects in the top-Higgs sector using the Standard Model Effective Field Theory (SMEFT) framework. Focusing on top-pair production in association with a Higgs boson and single top-Higgs associated production at the LHC, we study  $\mathcal{CP}$  violation in the top-Higgs Yukawa coupling and other Higgs and top interactions entering these processes. By analysing  $\mathcal{CP}$ -sensitive differential observables and asymmetries, we provide direct constraints on  $\mathcal{CP}$ -violating interactions in the top-Higgs sector. Our analysis demonstrates how combining  $t\bar{t}h$  and  $t\bar{h}j$  production can disentangle the real and imaginary components of the top-Yukawa coupling, offering valuable insights into potential sources of  $\mathcal{CP}$  violation. The sensitivity of these observables to SMEFT operators provides model-independent constraints on the parameter space, advancing the search for new physics in the top-Higgs sector.

KEYWORDS: Anomalous Higgs Couplings, SMEFT

ARXIV EPRINT: 2412.10309

# Contents

1 Introduction 1  
2 Theoretical framework 3

2.1Operator basis 3  
2.2 Computational setup 5

3  $\mathcal{CP}$  -odd effects in differential distributions 6

3.1 Single top-Higgs associated production 7  
3.2 Top-pair production in association with a Higgs boson 10  
3.3 Asymmetries 14

4 Constraints on Wilson coefficients 15

4.1 Experimental observables 15  
4.2 Expected bounds at the LHC and beyond 18

5 Conclusions 22

A SMEFT operator basis 23  
B Additional figures 24

# 1 Introduction

Despite the extraordinary success of the Standard Model (SM) in describing the fundamental interactions, it fails to account for the baryon asymmetry of the Universe. In order to describe baryogenesis, the Sakharov conditions [1] must be satisfied, which imply the existence of new sources of charge-parity  $(\mathcal{CP})$  violation [2, 3]. This has motivated a campaign of searches for  $\mathcal{CP}$  violation both at low energy experiments and at high-energy colliders, such as the Large Hadron Collider (LHC).

Searches for  $\mathcal{CP}$  violation at the LHC rely on the construction of suitable observables, sensitive to the presence of  $\mathcal{CP}$ -violating effects. As direct searches for new particles have not yielded any observations, attention has shifted towards indirect searches. The absence of discovery of any additional beyond the Standard Model (BSM) particle by the LHC suggests the existence of an energy gap among the electroweak (EW) scale and the new physics (NP) scale. In this scenario, the Standard Model Effective Field Theory (SMEFT) constitutes a robust theoretical framework to parametrise deviations from the SM predictions, including those arising from  $\mathcal{CP}$ -violating interactions. When the validity of the SMEFT is guaranteed through a sufficiently large mass gap, we can study the effects of NP in a model-independent way, just assuming that the BSM particles, with a mass well above the EW scale, satisfy the gauge symmetries of the SM.

In this work we investigate the effects of  $\mathcal{CP}$ -violating couplings in the top-Higgs sector, where the direct measurements of the couplings are only accessible at the LHC. The top-Higgs Yukawa coupling can be probed directly through the associated production of a Higgs boson with either a top-antitop quark pair or a single top quark. This class of processes has become accessible at the LHC for the first time, with  $t\bar{t}h$  observed in 2018 [4, 5] and current analyses leading to a bound on the single top-Higgs production [6, 7].

The top-Higgs sector, and in particular its  $\mathcal{CP}$ -violating interactions, can also be accessed indirectly. For instance, the top-Yukawa coupling affects the gluon-fusion Higgs boson production, providing the dominant contribution to this process in the SM. Gluon fusion in association with two jets has been proven to be  $\mathcal{CP}$  sensitive [8-14]. The top-Higgs  $\mathcal{CP}$ -violating component also generates huge contributions to the chromo-electric and electric dipole moment (EDM) of the nucleons — through its contribution to the Weinberg operator [15] and to the Barr-Zee diagrams [16] — as well as to the EDM of the leptons [17-22]. For the former, the uncertainties of the hadronic matrix elements are typically too large to provide competitive bounds. For the latter, the extremely good individual constraints become much looser in a global analysis once several operators affect the same observable, generating blind directions [21]. As such, the more direct LHC searches for the top-Higgs interactions provide crucial and complementary information.

Top-pair production in association with a Higgs boson has been widely explored in the context of extended Higgs sectors and the top-Yukawa  $\mathcal{CP}$  structure [11, 23-48]. Whilst suffering from a significantly smaller cross section, single top-Higgs associated production has been proven to be of particular interest in the search for new physics, due to its sensitivity to an anomalous top-Yukawa coupling and in particular to its sign [29, 31, 37, 40, 43, 49-59]. In this work we aim to comprehensively study both processes, focusing on the classes of differential observables and asymmetries, which can be sensitive to  $\mathcal{CP}$  violation.

In this work, we employ the SMEFT framework since it allows us to systematically capture potential  $\mathcal{CP}$ -violating effects in the top-Higgs sector arising from new physics at a heavy mass scale. By parametrising these effects through dimension-six operators, the SMEFT approach allows us to remain agnostic about the details of any specific UV-complete model while still accounting for all possible deviations from the SM. Although many past analyses have especially focused on the effective top-quark Yukawa coupling, working within the SMEFT provides a more comprehensive exploration of the interplay between this interaction and other  $\mathcal{CP}$ -violating couplings. The  $\mathcal{CP}$ -violating top-Higgs interactions have been studied previously in the context of the SMEFT [21, 25, 59-66]. Distinct from previous studies, our work proposes and analyses a wide array of  $\mathcal{CP}$ -sensitive observables and asymmetries that could be measured at the LHC. In particular, we focus on both top-pair production in association with a Higgs boson and single top-Higgs associated production, incorporating realistic projections for Run 3 and the HL-LHC. This comprehensive approach aims to highlight future ways to improve current constraints on the  $\mathcal{CP}$ -violating parameter space, focusing on the complementarity of multiple channels and the importance of differential measurements.

This work is organised as follows. In section 2 we introduce the operators and describe the computational setup for the processes we consider. In section 3 we present results for various differential observables and in section 4 we perform an analysis to constrain the Wilson coefficients using Run 3 LHC and HL-LHC expected measurements. We conclude in section 5.

# 2 Theoretical framework

# 2.1 Operator basis

In this work we parameterise the effects of BSM physics in terms of effective interactions among the SM particles. The SMEFT Lagrangian takes the form

$$
\mathcal {L} _ {\mathrm {S M E F T}} = \mathcal {L} _ {\mathrm {S M}} + \sum_ {d > 4} \sum_ {i} ^ {N _ {d}} \frac {C _ {i} O _ {i} ^ {(d)}}{\Lambda^ {d - 4}}, \tag {2.1}
$$

where the coefficients  $C_i$ , known as Wilson coefficients (WC), can be related to the physical parameters of BSM extensions, while the operators,  $O_i$ , contain only SM fields.

The first contribution relevant for our work appears at dimension six,  $d = 6$ , i.e.

$$
\mathcal {L} _ {\mathrm {S M E F T}} = \mathcal {L} _ {\mathrm {S M}} + \sum_ {i} \frac {C _ {i} O _ {i}}{\Lambda^ {2}} + \sum_ {i} \frac {\hat {C} _ {i} \hat {O} _ {i} + \mathrm {h . c .}}{\Lambda^ {2}} + \mathcal {O} (\Lambda^ {- 4}), \tag {2.2}
$$

where the non-hermitian operators are marked with a hat. At leading order, the imaginary and real part of the complex WC will generate  $\mathcal{CP}$ -odd and  $\mathcal{CP}$ -even interactions, respectively.

The SMEFT contribution to a physical observable can therefore be written as

$$
X _ {\text {S M E F T}} = X _ {\text {S M}} + \sum_ {i} \frac {C _ {i}}{\Lambda^ {2}} X _ {i} ^ {\text {i n t}} + \sum_ {i j} \frac {C _ {i} C _ {j}}{\Lambda^ {4}} X _ {i j} ^ {\text {q u a d}} + \mathcal {O} \left(\Lambda^ {- 4}\right). \tag {2.3}
$$

The contribution at linear order in the WC originates from the interference of the dimension-six operators with the SM, while the contribution at quadratic order arises from the square of dimension-six operators. The latter contribution is suppressed by the NP scale at the same order as the interference of the SM with dimension-eight operators, which are neglected in this analysis. However, we include results with quadratic terms to examine their impact.

In this work we follow the flavour assumptions of ref. [67], relaxing the assumption of  $\mathcal{CP}$ -conservation in the NP. We follow the conventions of the LHC Top WC [68], defining the covariant derivative as in the dim6top model described in the same reference. Our study focuses on the top-Higgs sector, considering only the  $pp\rightarrow thj$  and  $pp\rightarrow t\bar{t} h$  processes. The leading-order diagrams of these processes in the SM are shown in figures 1 and 2, respectively. Different classes of top-quark operators enter our processes of interest, as will be discussed.

The  $pp \to t\bar{t}h$  process will be modified by the same four-fermion operators as those entering the more precisely measured top-pair production process. With a plethora of measurements of differential distributions as well as asymmetries and spin correlation observables in the  $t\bar{t}$  process, we expect top-pair production to sufficiently constrain these operators and thus we do not consider them further.

Both processes considered are affected by the top-Yukawa coupling,  $\hat{O}_{t\varphi}$ , whilst  $\hat{O}_{tG}$  enters the  $t\bar{th}$  process, and  $\hat{O}_{tW}$  and  $O_{\varphi Q}^{(3)}$  affect the  $thj$  process. Since the  $O_{\varphi Q}^{(3)}$  coefficient receives much stronger constraints from single-top production processes without the production of an additional Higgs boson and is  $\mathcal{CP}$ -even by construction, it is not the focus of this work. Therefore, the relevant two-quark operators for this analysis are  $\{\hat{O}_{t\varphi}, \hat{O}_{tG}, \hat{O}_{tW}\}$ .

![](images/832ef6b05f33197d5d5bb96563dec8ea2919a1940f816cf4637d20db94dcfc9f.jpg)  
Figure 1. Leading-order Feynman diagrams contributing to  $thj$  production at the LHC in the SM for the five flavour scheme.

![](images/e7b50523b03d5a1ea9fa2bd03288d0031be75c45f1d69a427b0e8d26778717ce.jpg)

![](images/9884a6bbaa96800abc20b5417d870007a1c8b6c9727686b7bcf07bd895b5df20.jpg)

![](images/806be1417447072f3335af4a1325bc5fa75f55c2ed5da3d60ff5143a2a36be81.jpg)

![](images/c5d67467be07e875cd6606af2edde99e830cca4fc705f51f0e68cc2d8da85326.jpg)

![](images/569ffc8292dc18a4910fc218baa53b6575a629475e21ab6d44fef02d9d85cb05.jpg)

![](images/db9c7b9b5bdf7d691aad4df1a14593c8c22833e605844cc98120d8b99fc50fe8.jpg)

![](images/b1f6dae03b564187dcd59e541b57a5350a9b7c6a92bcbb0922682e72e550f40d.jpg)

![](images/90b5468905270ef6b8a5aaa4030c9fdd5c5a28e4492f8b8a2aa5056d86459b1e.jpg)  
Figure 2. Leading-order Feynman diagrams contributing to  $t\overline{t}h$  production at the LHC in the SM for the five flavour scheme.

![](images/343e1c05a5c45c16de5a469e121c009f2b9cb2a1c0e0e86a53b5cd12e7f9103b.jpg)

![](images/be1f8c6460beeb2109e91ebb28d8e746775d2549761735a97f37baef662248b0.jpg)

Finally, the purely bosonic operators can, in general, have some effect on LHC processes involving top quarks. We have 3 scalar operators

$$
O _ {\varphi}, O _ {\varphi \square}, O _ {\varphi D},
$$

and 12 involving gauge bosons for which we have 6  $\mathcal{CP}$ -even operators

$$
O _ {G}, O _ {W}, O _ {\varphi G}, O _ {\varphi W}, O _ {\varphi B}, O _ {\varphi W B},
$$

plus their anti-symmetric counterparts

$$
O _ {\widetilde {G}}, O _ {\widetilde {W}}, O _ {\varphi \widetilde {G}}, O _ {\varphi \widetilde {W}}, O _ {\varphi \widetilde {B}}, O _ {\varphi \widetilde {W} B},
$$

which are  $\mathcal{CP}$ -odd by construction.

The operators  $O_G$  and  $O_{\widetilde{G}}$ , besides generating a relevant contribution for  $t\bar{t}h$ , can be stringently constrained by multi-jet data at quadratic order [69, 70]. The three scalar operators, while generating some subleading effects, are all  $\mathcal{CP}$ -even and are expected to be constrained by other Higgs processes and electroweak precision observables, given that they modify the Higgs kinetic terms (hence affecting its decays), the Higgs self-coupling as well

as the effective weak mixing angle. Therefore, we do not consider them further, leaving the relevant bosonic operators for our processes as  $\{O_{\varphi G}, O_{\varphi \widetilde{G}}, O_{\varphi W}, O_{\varphi \widetilde{W}}\}$ .

In summary, the set of operators considered will be

$$
\{O _ {\varphi G}, O _ {\varphi \widetilde {G}}, O _ {\varphi W}, O _ {\varphi \widetilde {W}}, \hat {O} _ {t \varphi}, \hat {O} _ {t G}, \hat {O} _ {t W} \},
$$

whose definition can be found in appendix A. This set of operators contains four bosonic operators that are Hermitian and three two-fermion operators that are non-Hermitian. Hence, we have in total 10 degrees of freedom

$$
\{C _ {\varphi G}, C _ {\varphi \widetilde {G}}, C _ {\varphi W}, C _ {\varphi \widetilde {W}}, C _ {t \varphi}, C _ {t \varphi} ^ {I}, C _ {t G}, C _ {t G} ^ {I}, C _ {t W}, C _ {t W} ^ {I} \},
$$

where all the coefficients are real and the ones corresponding to the imaginary part of a WC are represented with a super index  $I$ . Therefore, our analysis will contain a total of five WC introducing  $\mathcal{CP}$ -violating effects in the Higgs sector

$$
\{C _ {\varphi \widetilde {G}}, C _ {\varphi \widetilde {W}}, C _ {t \varphi} ^ {I}, C _ {t G} ^ {I}, C _ {t W} ^ {I} \},
$$

and five  $\mathcal{CP}$ -conserving WC

$$
\{C _ {\varphi G}, C _ {\varphi W}, C _ {t \varphi}, C _ {t G}, C _ {t W} \}.
$$

The effects of  $\hat{O}_{t\varphi}$  can also be interpreted using an effective parametrisation of the top-Higgs coupling. The relation between the effective Yukawa couplings and the WC of  $\hat{O}_{t\varphi}$  is given by

$$
\mathcal {L} _ {h \bar {t} t} = - \frac {m _ {t}}{v} \bar {t} (\kappa \cos \alpha + i \gamma_ {5} \kappa \sin \alpha) t h,
$$

$$
\kappa \cos \alpha = 1 - \frac {v ^ {3}}{\sqrt {2} m _ {t}} \frac {C _ {t \varphi}}{\Lambda^ {2}}, \quad \kappa \sin \alpha = - \frac {v ^ {3}}{\sqrt {2} m _ {t}} \frac {C _ {t \varphi} ^ {I}}{\Lambda^ {2}}. (2. 4)
$$

# 2.2 Computational setup

The dependence of the observables considered on the WCs is obtained at leading-order using MadGraph5_aMC@NLO [71]. We use the model SMEFTsim3.0² [72] that implements the SMEFT in MadGraph5_aMC@NLO through the Universal FeynRules Output (UFO) format [73, 74]. Therefore, our parametrisation will be obtained at LO for all the NP effects. However, we have scaled the EFT contributions by the inclusive SM  $k$ -factor of the relevant process. As benchmark SM predictions we take the values quoted in ref. [6] ( $\sigma_{thj}^{\mathrm{SM}} = 84.8\mathrm{fb}$  and  $\sigma_{tth}^{\mathrm{SM}} = 499.8\mathrm{fb}$ ), from which we obtain a  $k$ -factor of 1.51 and 1.24 for the single top-Higgs associated production and the top-pair production in association with a Higgs boson, respectively. Details about the values of the parameters and cuts used can be found in table 1.³

Incoming protons are modelled with the nn231o1 parton distribution function, with dynamic renormalisation and factorisation scales chosen as the default of MadEvent, which

Table 1. Parameters required for event generation in MadGraph5_aMC@NLO, using the SMEFTsim3.0 model. The lepton cuts are applied to the electrons/positrons from the  $W^{\pm}$  decay, while the jet cuts are applied to the b-jets originating from top-quark decay as well as to the final-state jets in the case of single-top production.  

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>\( \Lambda \)</td><td>1000 GeV</td></tr><tr><td>top quark mass</td><td>172 GeV</td></tr><tr><td>Higgs boson mass</td><td>125 GeV</td></tr><tr><td>top resonance width</td><td>1.508336 GeV</td></tr><tr><td>Higgs resonance width</td><td>4.07 · 10-3GeV</td></tr><tr><td>Minimum jet \( p^T \)</td><td>20 GeV</td></tr><tr><td>Minimum charged lepton \( p^T \)</td><td>4 GeV</td></tr><tr><td>Maximum jet \( |\eta| \)</td><td>5</td></tr><tr><td>Maximum charged lepton \( |\eta| \)</td><td>5</td></tr><tr><td>Maximum jet PDG flavour</td><td>5</td></tr></table>

uses the central transverse mass after applying a  $k_{T}$ -clustering algorithm on the event [75], in a five flavour scheme. In the single top-Higgs production process, events with top- or antitop-quarks in the final state are both considered, as well as the s- and t-channel, though the s-channel provides only subleading contribution to the cross section.

Outgoing top-quarks are decayed in MadSpin [76] and the Higgs boson is left undecayed. Since leptons from top-quark decays are most sensitive in their kinematics to top-quark polarisation and top-pair spin correlations,  $W^{\pm}$  bosons from top-quarks are decayed to electrons,  $t \rightarrow bW^{+}, W^{+} \rightarrow e^{+}\nu_{e}$ .

The contributions from the SMEFT operators have only been considered in the production,  $pp \rightarrow thj$  or  $pp \rightarrow t\bar{t}h$ , with top-quark decays assumed to obey the SM predictions. While the impact of higher-dimensional operators in the decay has been shown to be relevant in other channels [77], these effects are found to be irrelevant in our case. To validate this approach, we have explored the effects of inserting  $C_{tW}$  and  $C_{tW}^{I}$  in the decay, obtaining effects smaller than  $5\%$  for values of  $C_{tW}^{(I)} / \Lambda^2$  as large as  $10\mathrm{TeV}^{-2}$ . Given this minimal impact, we focus on the contributions of SMEFT operators only in the production. Note that there are also other production channels that can be relevant as a probe of the  $\mathcal{CP}$ -violating interactions in the top-Higgs sector, e.g.  $pp \rightarrow thW$ . However, significant interference of this channel with  $t\bar{t}h$  [55] complicates both the experimental extraction of the signal and the theoretical interpretation in a SMEFT framework. Therefore, we decided not to include this process in our exploratory analysis.

# 3  $\mathcal{CP}$ -odd effects in differential distributions

The total cross sections are  $\mathcal{CP}$ -even observables by construction. Although these observables are still sensitive to  $\mathcal{CP}$ -odd couplings at quadratic order, the sensitivity to them would benefit from a differential analysis. In the following, we propose and describe some manifestly  $\mathcal{CP}$ -odd observables which are sensitive to  $\mathcal{CP}$ -odd couplings at linear order for single and pair top-Higgs associated production.

# 3.1 Single top-Higgs associated production

We start by considering the  $thj$  process. Since  $thj$  is not sensitive to the gluonic operators, it will only be sensitive to four out of the seven operators considered in this work:  $\left\{\hat{O}_{t\varphi},\hat{O}_{tW},O_{\varphi W},O_{\varphi \widetilde{W}}\right\}$ .

Triple products. There are several angular observables that have been proven to be sensitive to the  $\mathcal{CP}$ -odd couplings at the linear level. A promising set of observables are the triple products of the momenta of the final particles and/or the initial partons [66]. In this work, we have considered the triple product of the 3-momenta of the final particles in the laboratory frame, as well as the triple product of the 3-momenta of the beam axis, the (anti-)top quark, and the final jet in the Higgs rest frame,

$$
\hat {p} _ {h} \cdot \left(\hat {p} _ {t} \times \hat {p} _ {j}\right), \quad \hat {z} \cdot \left(\hat {p} _ {t} \times \hat {p} _ {j}\right), \tag {3.1}
$$

where  $\hat{z}$ ,  $\hat{p}_h$ ,  $\hat{p}_t$ , and  $\hat{p}_j$  are unit vectors in the direction of beam axis, outgoing Higgs boson, (anti-)top quark, and jet, respectively. The former observable measures the cosine of the angle between the Higgs boson and the perpendicular direction to the plane formed by the (anti-)top quark and the jet in the laboratory frame, while the latter measures the cosine of the angle between the beam axis and that same plane in the Higgs rest frame. The differential distributions for these triple products are presented in figure 3 for all relevant degrees of freedom at linear and quadratic order in comparison with the SM prediction. As we aim to compare the shape of these distributions, we normalise them in such a way that the absolute value of the area of the distributions is equal to the one of the SM. As shown in figure 3, these triple products are symmetric for all  $\mathcal{CP}$ -even contributions (i.e., the SM and the interference of the  $\mathcal{CP}$ -even degrees of freedom with the SM) and demonstrate a clear separation of positive and negative weights for  $C_{t\varphi}^I$ ,  $C_{tW}^I$ , and  $C_{\varphi \widetilde{W}}$ . This behaviour allows us to use the triple products to define asymmetries sensitive to the  $\mathcal{CP}$ -odd couplings, as demonstrated in section 3.3.

Although asymmetries are clearly the best option for  $C_{t\varphi}^{I}$  and  $C_{\varphi \widetilde{W}}$ , the situation differs for  $C_{tW}^{I}$ , where the distribution changes sign three times, reducing the sensitivity of the asymmetries. In this case, a binned distribution would achieve better sensitivity, provided the binning is chosen such as to avoid cancellations between positive and negative contributions.

Finally, in figure 3 we can also see how the sensitivity of  $C_{\varphi \widetilde{W}}$  is around a factor 10 higher than the one of the Yukawa,  $C_{t\varphi}^{I}$ , which will be discussed in more detail in section 3.3.

Polarisation angles. Another set of observables that are sensitive to the  $\mathcal{CP}$ -odd couplings are those accessing the top-quark polarisation. In single-top production, the top-quark polarisation is accessible via the angular distribution of its decay products. In the top-quark rest frame, the differential cross section can be written as

$$
\frac {1}{\sigma} \frac {d \sigma}{d \cos \theta_ {i} ^ {x}} = \frac {1}{2} \left(1 + a _ {i} P \cos \theta_ {i} ^ {x}\right), \tag {3.2}
$$

where  $P$  is the top-quark polarisation;  $a_{i}$  is the so-called spin analysing power, which quantifies the effect of the top-quark spin on a given decay product, with  $a_{e} = 1$  at leading order;  $\theta_{i}^{x}$  is

![](images/1eda0d766a4202d0910ee0e866a2a2eba015e25e38a2417a0d857a564f455866.jpg)  
(a)

![](images/168515906562ce68a49379ffd47d398d0f584652a966bea74f151dc22dae1a60.jpg)  
(b)

![](images/42526d7f21be6b0653fe590fefba237c250482deb6562f2973bd8f5255b78a66.jpg)  
(c)

![](images/2bf0901ff39fb315941939c130cbd4e099980571f0cfe525f2420c3cffa27f11.jpg)  
(d)

![](images/fce87e1098bb03c2e9ab1dea7c607434e98335f0a70602ac131974866877be0e.jpg)  
(e)

![](images/625241c197b1ef56322a8b3c1c79fc4f0e8f061aa9d5255f97070dd48e200552.jpg)  
Figure 3. Triple product of final state particles (left) and of the beam, top and jet directions in the Higgs rest frame (right), for the operators  $\hat{O}_{t\varphi}$  (top),  $\hat{O}_{tW}$  (middle) and  $O_{\varphi W / \widetilde{W}}$  (bottom). SMEFT predictions are scaled to match the SM curve area, and we show the multiplicative factor used in parenthesis in the label of each curve.  
(f)

![](images/42f017e14861cd4d52e7d4fe13066addd8a9df409f22290ac810915f298d4abf.jpg)  
(a)

![](images/3ea0f2bdcbe096c830b3ba5c3964c1d9c0ed459f00e5845796f12df532be3c60.jpg)  
(b)

![](images/718a60e66591ba0537760bef6f4fa0cd3a79d49584b9f96b82a754dba7323aa2.jpg)  
(c)

![](images/0492f8bea56a7dca45d8c5073a058861f3cbf4fa3137410998eef8187da30389.jpg)  
(d)

![](images/6c6f4bb20ec2a2a3d9b09692e386c54e66e5c53eeef1e4b2b41e2af6e419fc9f.jpg)  
(e)

![](images/185170902235899e05b8b55764b37d4db4ace3c797bbafa510f801659a9d731b.jpg)  
(f)

![](images/81375cef3e65b6ad9aa9200c1d1099f2a944550c831393999d0b9b7554233fd9.jpg)  
(g)

![](images/62499880451b0d56f77f2ed7a55dfb80bd293c8208a821cc7a391f56b4ddd96a.jpg)  
(h)

![](images/0085b6e1686f6b9b6935809e199c25c480747fc2b3435c18ae3a01cb52338a28.jpg)  
Figure 4. Differential cross sections of  $\cos \theta_{e}$  for the polarisation angles  $\theta_e^j$ ,  $\theta_e^y$ ,  $\theta_e^s$  (from top to bottom), for the operators  $\hat{O}_{t\varphi}$  (left),  $\hat{O}_{tW}$  (middle) and  $O_{\varphi W / \widetilde{W}}$  (right). SMEFT predictions are scaled to match the SM curve area, and we show the multiplicative factor used in parenthesis in the label of each curve.  
(i)

the angle of the decay product  $i$  relative to the axis  $x$ . Following the work of refs. [50, 77], we define the electron polarisation angles,  $\theta_i^x$ , relative to the axes

$$
\hat {j} = \hat {p} _ {j}, \quad \hat {y} = \frac {\hat {p} _ {j} \times \hat {z}}{| \hat {p} _ {j} \times \hat {z} |}, \quad \hat {s} = \frac {\hat {p} _ {j} \times \hat {p} _ {h}}{| \hat {p} _ {j} \times \hat {p} _ {h} |}, \tag {3.3}
$$

in the top-quark rest frame. The polarisation angles can therefore be simply extracted by taking the scalar product of the electron unit 3-momentum with these axes. Given that we consider both top- and antitop-quark production,  $\cos \theta_{e}^{j}$  is a  $\mathcal{CP}$ -even observable. However,  $\cos \theta_{e}^{y}$  and  $\cos \theta_{e}^{s}$  are, by construction,  $\mathcal{CP}$ -odd.

The impact of the higher-dimensional operators on the defined polarisation angles is shown in figure 4. We first note that for the  $\mathcal{CP}$ -even angle the  $\mathcal{CP}$ -odd operators only contribute at the quadratic level, whilst for the  $\mathcal{CP}$ -odd observables, as expected, only the interference of the SM with the  $\mathcal{CP}$ -odd operators gives an odd distribution.

The distributions of  $\cos \theta_e^j$  (figure 4(a)-(c)) indicate that, in the SM, the lepton from the top-quark decay is preferentially produced in the direction of the spectator quark — opposing the top quark momentum ( $P < 0$ ). While the differential interference is consistent with zero for  $\mathcal{CP}$ -odd contributions, the quadratic amplitude distribution of  $\hat{O}_{tW}$  shows an inversion of the top-quark polarisation, relative to the SM. Additionally, the introduction of modified top-Higgs vertices reduces the degree of top-quark polarisation, which also experiences a sign inversion for a  $\mathcal{CP}$ -odd top-Yukawa coupling.

The  $\mathcal{CP}$ -even modified  $hWW$  vertex introduced by  $O_{\varphi W}$  leaves the top-quark polarisation close to unchanged. Small differential asymmetries in  $\cos \theta_e^y$  and  $\cos \theta_e^s$  are seen for the analogous  $\mathcal{CP}$ -odd operator, but these are not as pronounced as those observed with the triple productions at parton-level.

In the SM, and for modified  $\mathcal{CP}$ -even amplitudes (including all quadratic amplitudes from  $\mathcal{CP}$ -odd operators), the lepton direction is invariant along the  $\hat{y}$ - and  $\hat{s}$ -axes, as demonstrated in figures 4(d)-(i). However, the interference of  $\mathcal{CP}$ -odd effective couplings introduces a preferential direction of the charged lepton momentum along each of these axes. The coefficients  $C_{t\varphi}^{I}, C_{tW}^{I}$  and  $C_{\varphi W}$  determine whether leptons are produced preferentially in the forward or backward direction, and the linear dependence allows for the definition of a dedicated  $\mathcal{CP}$ -odd asymmetry about  $\cos \theta_e = 0$ , as shown in section 3.3.

# 3.2 Top-pair production in association with a Higgs boson

Top-pair production in association with a Higgs boson has been widely explored in the context of the top-Yukawa coupling  $\mathcal{CP}$  structure. In this analysis we will review the corresponding observables and explore whether  $\mathcal{CP}$ -odd effects in other interactions can play an important role in this process. At parton-level, from an EFT perspective, many observables rely on quadratic contributions to constrain the  $\mathcal{CP}$ -odd operators. Alternative approaches involve the construction of manifestly  $\mathcal{CP}$ -odd observables that can probe the  $\mathcal{CP}$ -odd interference directly at linear order [26, 34, 41, 42, 44, 46], or the use of machine learning techniques [41, 78-85]. In this work, we focus on the construction of  $\mathcal{CP}$ -sensitive observables sensitive to our subset of WCs.

The sensitivity of this process to operators involving  $W$  bosons is suppressed by the electroweak coupling. However, since we have considered the effects of the operator  $\hat{O}_{tW}$  in  $thj$  production, we also include it in  $t\bar{th}$  for completeness. In fact, due to the large uncertainties in

![](images/6e602029a6e93ea5451a54a8923f1e08e8cc3538334a9bbac0c561b70eab0e21.jpg)  
(a)

![](images/df8064b0677fd768f186d1d0c454e516bf4e5c68fa14e0b98fd31b13d7382ae0.jpg)  
(b)

![](images/f22ea8d65285037f71738d3ed9880c6f82fb3ecc70b66245fe88eec8ffa21f73.jpg)  
(c)

![](images/f975ff8b69b297586fed9d496c1f82394d746e0b1fca757552f28640b2ba114d.jpg)  
Figure 5. Differential cross sections of  $\Delta \phi_{tt}^{(\eta \downarrow)}$ , for the operators  $\hat{O}_{t\varphi}$  (top left),  $O_{\varphi G / \widetilde{G}}$  (top right),  $\hat{O}_{tG}$  (bottom left) and  $\hat{O}_{tW}$  (right left). SMEFT predictions are scaled to match the SM curve area, and we show the multiplicative factor used in parenthesis in the label of each curve.  
(d)

$thj$  measurements, the constraints on  $\hat{O}_{tW}$  are found to be stronger from  $t\bar{t}h$  production [86], as discussed in section 4.2. Other operators, such as  $\hat{O}_{tZ}$ , which could generate effects similar to  $\hat{O}_{tW}$  in  $t\bar{t}h$  production, are omitted because they do not contribute to  $thj$ , and their impact on  $t\bar{t}h$  is minimal. Furthermore, these operators can be more effectively constrained from other LHC processes [87-92]. Therefore, for the observables built from top-pair production in association with a Higgs boson, we have considered the effects of only five out of the seven operators considered:  $\{\hat{O}_{t\varphi}, \hat{O}_{tG}, \hat{O}_{tW}, O_{\varphi G}, O_{\varphi \widetilde{G}}\}$ .

Top-quark level observables. The two-fermion operators generate identical kinematics for the top and antitop quarks. This ensures that, given the subset of operators considered

here, angular observables constructed from top-quark four-momenta, ordered by their pseudorapidities, are invariant under charge conjugation while retaining their parity dependence. Therefore, these observables can be sensitive to the  $\mathcal{CP}$ -odd couplings at linear order.

In this work, we have considered the pseudorapidity-ordered azimuthal angular separation between the top quarks,  $\Delta \phi_{tt}^{\eta \downarrow} = (\phi(t_1) - \phi(t_2):\eta(t_1) > \eta(t_2))$ . This distribution is  $\mathcal{CP}$ -odd by construction and, as can be seen in figure 5, it can be used to discriminate the  $\mathcal{CP}$ -odd effects of  $\hat{O}_{tW}$ ,  $\hat{O}_{tG}$  and  $O_{\varphi \widetilde{G}}$  by constructing an asymmetry observable with its distribution. However, the sensitivity to the  $\mathcal{CP}$ -odd effects of  $\hat{O}_{t\varphi}$  is significantly smaller, making it less effective for probing this operator.

In the context of extended Higgs sectors, various observables have been proposed to discriminate non-SM top-Yukawa couplings [23]. The well-known  $b_{2}$  and  $b_{4}$  observables are  $\mathcal{CP}$ -even, but the quadratic effects of the  $\mathcal{CP}$ -odd couplings generate different shapes on their distributions. They are defined as [23]

$$
b _ {2} = \left(\hat {p} _ {t} \times \hat {z}\right) \cdot \left(\hat {p} _ {\bar {t}} \times \hat {z}\right) = \sin \theta_ {t} \sin \theta_ {\bar {t}} \cos \Delta \phi_ {t \bar {t}}, \tag {3.4}
$$

$$
b _ {4} = \left(\hat {p} _ {t} \cdot \hat {z}\right) \left(\hat {p} _ {\bar {t}} \cdot \hat {z}\right) = \cos \theta_ {t} \cos \theta_ {\bar {t}}, \tag {3.5}
$$

where  $\hat{z}$ ,  $\hat{p}_t$  and  $\hat{p}_{\bar{t}}$  represent the 3-momentum of the beam axis, the top quark and the antitop quark, respectively. In our analysis we have included  $b_{4}$  measured in the lab frame since is the one more sensitive to  $\mathcal{CP}$ -odd interactions, as shown in the ATLAS search for  $\mathcal{CP}$ -odd Higgs bosons [93]. The observable  $b_{2}$  is highly correlated with  $b_{4}$  and is therefore not included in our analysis. The dependence of  $b_{2}$  and  $b_{4}$  on the WC considered can be found in figure 14 of appendix B.

Decay level observables. Besides the parton-level observables, several particle-level observables can be defined to exploit additional information in the leptonic and semi-leptonic decays of the  $t\bar{t}$  pair to probe top-quark spin correlations and thus the interactions entering the production of the top quarks. One promising observable is the azimuthal separation of the charged lepton pair in the  $t\bar{t}$  rest frame,  $\Delta \phi_{ll}^{t\bar{t}}$ , which has been proven to be sensitive to the  $\mathcal{CP}$ -phase of an anomalous top-Yukawa coupling [46]. In this work, instead, we have used the pseudorapidity-ordered azimuthal angular separation between the final electrons in the lab frame,  $\Delta \phi_{ee}^{\eta \downarrow}$ . The advantage of this observable is that it does not depend on the explicit reconstruction of the  $t\bar{t}$  system, which is challenging when both top quarks decay to leptons, due to the presence of multiple neutrinos in the final state. Additionally, we have considered the triple product of the normalised 3-momenta of the top quark, the final electron, and the positron,  $^4\hat{p}_t\cdot (\hat{p}_{e^-}\times \hat{p}_{e^+})$ , and the cosine of the angle formed by the final electron and positron scaled by the sign of the previous triple product,  $\mathrm{sgn}\left[\hat{p}_t\cdot (\hat{p}_{e^-}\times \hat{p}_{e^+})\right]\hat{p}_{e^-}\cdot \hat{p}_{e^+}$ , both in the  $t\bar{t}$  rest frame. All three observables are sensitive to the  $\mathcal{CP}$ -odd couplings at linear level, as illustrated in figure 6. Furthermore, these particle-level observables show much better sensitivity to the  $\mathcal{CP}$ -odd effects of  $\hat{O}_{t\varphi}$  due to the availability of additional spin information at particle-level.

![](images/4b05a4a48f6d8d11c788879a6dc139fca200b168b2d1f47035072a9b61acd7b2.jpg)  
(a)

![](images/d911f4fa7c5a772c3eec0f6005cc925c02a305f7410c17c3d1772dbd8ccf795a.jpg)  
(b)

![](images/311b07b6e3bc7bb32adc7b4ec5cf8eabb812bd6bf922c66d27013e162ad60eb3.jpg)  
(c)

![](images/e72884032195d361f1a2827fb0c21e637baad0bbf35ee99b5b95f01bbd0234b9.jpg)  
(d)

![](images/bbfc0789d22e9eb4870346a2bd06d4d3d649b482825f6a850d8a2dbc2da40297.jpg)  
(e)

![](images/aaca38b361b78666289b77ee7cf2b19d196d6d003307507bb701ce4983856749.jpg)  
(f)

![](images/f756cfcd7780ffe1298fb1e4383880af1269567364b31b65cbc31534553f32a4.jpg)  
(g)

![](images/16d456d838388018da17abb6da828d70cb5a275f955a743d86931b271c58b36a.jpg)  
(h)

![](images/4c0ba3f81ac7419aa5bb96f9802295c72b98e4367024cefd25f6c87afceb5067.jpg)  
(i)

![](images/cfba5504c7054b2bc21aec3d91814a47b62a0ac779a8b47d36fc8cd263792257.jpg)  
(j)

![](images/b5bfee587d10035733378667cad9022009d0c39ad054db9c366fe367d18fd28c.jpg)  
(k)

![](images/5073acc056214205ef15b799edf5c90d291afa34ac92b793e4b910e6c873d649.jpg)  
Figure 6. Differential cross sections of the observables  $\Delta \phi_{ee}^{\eta \downarrow}$  (lab),  $\hat{p}_t \cdot (\hat{p}_{e^-} \times \hat{p}_{e^+})$  and  $\operatorname{sgn}[\hat{p}_t \cdot (\hat{p}_{e^-} \times \hat{p}_{e^+})] \hat{p}_{e^-} \cdot \hat{p}_{e^+}$  (in the  $t\bar{t}$  rest frame), for the operators  $\hat{O}_{t\varphi}$  (top),  $O_{\varphi G / \widetilde{G}}$  (centre top),  $\hat{O}_{tG}$  (centre bottom) and  $\hat{O}_{\mathrm{WG}}$  (bottom). SMEFT predictions are scaled to match the SM curve area, and we show the multiplicative factor used in parenthesis in the label of each curve.  
(1)

Experimentally the pseudorapidity-ordered angular separation among the charged leptons,  $\Delta \phi_{ee}^{\eta \downarrow}$ , is easily accessible since it can be constructed directly from the direction of the lepton pair in the lab frame. Furthermore, and despite the limited information used from the full event, the asymmetry built from  $\Delta \phi_{ee}^{\eta \downarrow}$  has a sensitivity comparable in magnitude to that from observables requiring full event reconstruction, as we will see in section 3.3. Nevertheless, the triple product  $\hat{p}_t \cdot (\hat{p}_{e^-} \times \hat{p}_{e^+})$ , which requires full event reconstruction, is the one providing the best separation of positive and negative weights for an anomalous top-Yukawa  $\mathcal{CP}$ -phase.

# 3.3 Asymmetries

To maximise the linear sensitivity to the  $\mathcal{CP}$ -odd couplings, we have defined asymmetries for the  $\mathcal{CP}$ -odd observables presented in sections 3.1 and 3.2. For a given observable  $X$ , the associated asymmetry is defined as

$$
A (X, x, c) = \frac {\sigma (X > x , c) - \sigma (X <   x , c)}{\sigma (X > x , c) + \sigma (X <   x , c)} \equiv \frac {\Delta (X , x , c)}{\sigma (c)}, \tag {3.6}
$$

where  $\sigma(c)$  is the SMEFT cross section — dependent on the value of the coefficient,  $c$  — and  $\sigma(X > x, c)$  and  $\sigma(X < x, c)$  are the fiducial rates in each of the phase-space regions, defined by the cut-off value,  $x$ , typically taken to be zero.

Interference and quadratic contributions, parameterised as

$$
A (X, x, c) = \frac {\Delta^ {s m} (X , x) + C \Delta^ {\text {i n t}} (X , x) + C ^ {2} \Delta^ {\text {q u a d}} (X , x)}{\sigma (C)}, \tag {3.7}
$$

$$
\Delta^ {i} (X, x) = \sigma^ {i} (X > x) - \sigma^ {i} (X <   x),
$$

are obtained for the subset of WCs considered in this work. Note that all of them except for the asymmetry constructed with  $\cos \theta_e^j$  in  $thj$  will only have a linear contribution in the numerator, given that they are  $\mathcal{CP}$ -odd by construction. Apart from the enhanced sensitivity to  $\mathcal{CP}$ -odd effects, any asymmetry observable benefits from a significant cancellation of systematic uncertainties and thus offers better prospects in the identification of new physics effects.

The asymmetries in  $thj$  production are shown in figure 7. The asymmetry most sensitive to  $O_{\varphi \widetilde{W}}$  and  $\hat{O}_{t\varphi}$  is the one built from the triple product of outgoing partons, with enhanced sensitivity to  $O_{\varphi \widetilde{W}}$ . Nevertheless, this same asymmetry becomes irrelevant for  $\hat{O}_{tW}$ , as the triple product distribution switches sign three times (as shown in figure 3(c)) diminishing any contribution to the asymmetry. Indeed, for this case measuring the binned distribution would be more suitable. For the observables considered in this work the best sensitivity to the  $\mathcal{CP}$ -odd couplings of  $\hat{O}_{tW}$  at linear order is obtained by the  $\mathcal{CP}$ -odd polarisation angular distributions ( $\cos \theta_e^y$  and  $\cos \theta_e^s$ ). Among the two  $\mathcal{CP}$ -odd polarisation angular distributions, the one constructed from  $\cos \theta_e^s$  exhibits stronger effects from  $O_{\varphi \widetilde{W}}$  and  $\hat{O}_{t\varphi}$ . In contrast, the asymmetry extracted from  $\cos \theta_e^y$  shows only mild effects from these operators. Finally, the asymmetry built from the  $\mathcal{CP}$ -even polarisation angular distribution ( $\cos \theta_e^j$ ) shows, as expected, only quadratic dependencies, with particular sensitivity to  $\hat{O}_{tW}$ .

The corresponding asymmetries in  $t\bar{t}h$  production are shown in figure 8. In this case the particle-level pseudorapidity-ordered azimuthal separation,  $\Delta \phi_{ee}^{\eta \downarrow}$ , clearly outperforms its parton-level counterpart,  $\Delta \phi_{tt}^{\eta \downarrow}$ . It shows significant sensitivity to  $\hat{O}_{t\varphi}$  and  $\hat{O}_{tW}$  (unlike the parton-level case) and provides similar sensitivity for  $\hat{O}_{tG}$  and  $O_{\widetilde{\varphi G}}$  as the parton-level case. However, the most sensitive asymmetry, except for  $\hat{O}_{tW}$ , is the one constructed from the triple product of the final charged leptons and the top-quark 3-momentum,  $\hat{p}_t\cdot (\hat{p}_{e^-}\times \hat{p}_{e^+})\big|^{t\bar{t}}$

![](images/55efcef094b20ba2b617895b2cbe89378ff004a366b76ef257995edd544191e6.jpg)  
(a)

![](images/b2a6239880b9a8dfc50b10b0b00063cf81d50dec81d1acd6933d13a2218b71a0.jpg)  
(b)

![](images/2d310f9e5c9c61dd55562de846d5c4e0e846eceb6d949efc7c937adfb0aac3e3.jpg)  
(c)

![](images/a75c7aa60160a3e8494b9a63ff115a4b5e13a85a6566ce9d19a6054211401696.jpg)  
Figure 7. Asymmetries in SMEFT  $thj$  production, constructed from the observables  $\hat{p}_h \cdot (\hat{p}_t \times \hat{p}_j)$ ,  $\cos \theta_e^y$  and  $\cos \theta_e^s$  (red, blue and green curves, respectively). The asymmetries as a function of Wilson coefficient values are shown for the operators  $\hat{O}_{t\varphi}, \hat{O}_{tW}, O_{\varphi \widetilde{W}}$  ((a) to (c)). For better visibility, panel (d) shows the asymmetry  $A(\cos \theta_e^j, 0)$  for these three operators separately (red, blue and green curves, respectively). The shaded bands represent the estimation of the theoretical uncertainties obtained varying the renormalisation and factorisation scales by a factor 2 and 1/2. The ranges of the WC in the plots are chosen to be within the values allowed by our prospects on LHC data.  
(d)

which requires full reconstruction of the top-quark momentum. A relevant intermediate approach is the asymmetry built from the cosine of the final charged leptons and the sign of this triple product,  $\mathrm{sgn}[\hat{p}_t\cdot (\hat{p}_{e^-}\times \hat{p}_{e^+})](\hat{p}_{e^-}\cdot \hat{p}_{e^+})|^{\bar{t}}$ . In this case, only the reconstruction of the sign of the triple product is required. It outperforms the sensitivity of  $\Delta \phi_{ee}^{\eta \downarrow}$  for  $O_{\varphi G}$  and demonstrates comparable sensitivity for  $\hat{O}_{tG}$ ,  $\hat{O}_{tW}$  and,  $\hat{O}_{t\varphi}$ .

Overall, the asymmetries for  $thj$  can range from  $5\%$  to  $10\%$ , while those for  $t\bar{t}h$  typically fall between  $3\%$  and  $6\%$ , for WC values within the ranges currently allowed by LHC data, as discussed in the next section. Although these values are non-negligible, the experimental uncertainties in these channels are often considerable, potentially compromising their impact on the global fit. This impact will be explored in detail in the next section.

# 4 Constraints on Wilson coefficients

# 4.1 Experimental observables

In order to establish the experimental sensitivity to the relevant Wilson coefficients, we will perform a toy fit, using current data as well as future projections for the HL-LHC. The

![](images/aed5c595f1b6cf119f27b367d4dda6fb3f917c8b51f64500240c7f991a24a681.jpg)  
(a)

![](images/b8cb7a57206fd3b96d05819e7bc4b0305777d571e21d4287574ca567203d0572.jpg)  
(b)

![](images/f5eb1e1f01b24ec9a74b6daf92ca57200c7523081ea64eab02dd213989ca78e9.jpg)  
(c)

![](images/792899365799661bf3f9b9900bf52b944bbb34f0857f9481627e846050e163c4.jpg)  
Figure 8. Asymmetries in SMEFT  $t\bar{t}h$  production, constructed from the observables pseudorapidity-ordered  $\Delta \phi_{tt}^{(\eta \downarrow)}$ , pseudorapidity-ordered  $\Delta \phi_{ee}^{\eta \downarrow}$ ,  $\hat{p}_t \cdot (\hat{p}_{e^-} \times \hat{p}_{e^+})|^{t\bar{t}}$  and  $\mathrm{sgn}[\hat{p}_t \cdot (\hat{p}_{e^-} \times \hat{p}_{e^+})](\hat{p}_{e^-} \cdot \hat{p}_{e^+})|^{t\bar{t}}$  (yellow, red, blue and green curves, respectively). The asymmetries as a function of the coefficient value are shown for the  $(\mathcal{CP}$ -odd part of the) operators  $\hat{O}_{t\varphi}$ ,  $\hat{O}_{tG}$ ,  $O_{\varphi \widetilde{G}}$ , and  $\hat{O}_{tW}$  ((a) to (d)). The shaded bands represent the estimation of the theoretical uncertainties obtained varying the renormalisation and factorisation scales by a factor 2 and  $1/2$ . The ranges of the WC in the plots are chosen to be within the values allowed by our prospects on LHC data.  
(d)

observables considered, with the appropriate binning, can be found in table 2. Besides the observables constructed to be sensitive to  $\mathcal{CP}$ -odd operators at linear order, there are other differential measurements that can be useful to constrain our subset of operators. In particular, in this work we have also considered the angular separations between outgoing partons, defined as  $\Delta R = \sqrt{(\Delta\phi)^2 + (\Delta\eta)^2}$ , and some invariant mass distributions. In order to determine their constraining power, we have estimated their experimental uncertainties at the LHC Run 3 and in the future phase of the high luminosity LHC (HL-LHC).

The ATLAS and CMS collaborations of the LHC have published measurements of the  $t\bar{th}$  cross section [94-98] and the  $\mathcal{CP}$  properties of the top-Yukawa coupling using  $t\bar{th}$  and  $th$  events [93, 94, 97, 98]. Despite the lack of a direct observation of single top-Higgs associated production to date, upper bounds on the total rate are placed by both collaborations[94, 96, 99]. In order to estimate the expected statistical uncertainty at the

Table 2. Binning for the differential distributions of the considered observables.  $\mathcal{CP}$ -odd observables and  $\cos \theta_{e}^{j}$  are interpreted as asymmetries, with the exception of the  $thj$  observable  $\hat{z} \cdot \hat{p}_t \times \hat{p}_j|^h$ .  

<table><tr><td></td><td>thj obs.</td><td>binning</td></tr><tr><td rowspan="4">CP-odd</td><td>\(\hat{z}\cdot \hat{p}_t\times \hat{p}_j|_h\)</td><td>[-1,-0.1,0,0.1,1]</td></tr><tr><td>\(\hat{p}_h\cdot \hat{p}_t\times \hat{p}_j\)</td><td rowspan="4">Asymmetry about 0</td></tr><tr><td>\(\cos \theta_e^y\)</td></tr><tr><td>\(\cos \theta_e^s\)</td></tr><tr><td rowspan="3">CP-even</td><td>\(\cos \theta_e^j\)</td></tr><tr><td>\(\Delta R(ht)\)</td><td>[0,π,8]</td></tr><tr><td>\(M(ht)[GeV]\)</td><td>[200,340,424,620,1600]</td></tr></table>

<table><tr><td></td><td>tth obs.</td><td>binning</td></tr><tr><td rowspan="4">CP-odd</td><td>Δφη↓</td><td rowspan="4">Asymmetry about 0</td></tr><tr><td>Δφee↓</td></tr><tr><td>ˆpt·ˆpe- ×ˆpe+|tt</td></tr><tr><td>[Sgn]ˆpe- ·ˆpe+|tt</td></tr><tr><td rowspan="2">CP-even</td><td>M(htτ) [GeV]</td><td>[450,655,860,1270,2500]</td></tr><tr><td>b4lab</td><td>[-1,-0.5,0,0.5,1]</td></tr></table>

LHC for our binned distributions, we have assumed the same acceptance and efficiency as the one obtained by the ATLAS collaboration for the inclusive cross section shown in figure 2 of ref. [6]. In particular we take as reference

$$
\sigma_ {t t h} = 3 6 9. 6 \pm 8 6. 0 _ {\mathrm {s t a t .}} \pm 8 4. 4 _ {\mathrm {s y s t .}} \mathrm {f b}, \qquad \sigma_ {\mathrm {t h j}} = 5 6 0. 6 \pm 2 7 2. 3 _ {\mathrm {s t a t .}} \pm 2 0 1. 7 _ {\mathrm {s y s t .}} \mathrm {f b}.
$$

Using these numbers together with the quoted SM predictions ( $\sigma_{t\bar{t}h} = 499.8\mathrm{fb}$  and  $\sigma_{thj} = 84.8\mathrm{fb}$ ) we find that 480 and 8.2 events per million of  $t\bar{t}h$  and  $thj$  are properly reconstructed, respectively. For the systematic uncertainty we have simply assumed the same relative uncertainty as in the inclusive cross section. The LHC limits that we present are our prospects after full Run 3, so a total integrated luminosity of  $300\mathrm{fb}^{-1}$  has been assumed and, therefore, the statistical uncertainty has been scaled accordingly, leaving the systematic uncertainties at their current value. Finally, for the prospects of the HL-LHC we have assumed that, besides the appropriate scaling of the statistical uncertainty with the luminosity, the systematic uncertainties will be reduced by a factor of two by the operation time of the HL-LHC.

Since we are combining observables coming from the same processes, it is crucial to determine their correlations. To obtain the correlations among the statistical uncertainties, we have assumed SM distributions<sup>7</sup> and that bins with different events are completely uncorrelated. Thus, any correlation would arise from the events shared among the different binned observables. The systematic uncertainties are assumed to be  $50\%$  correlated among the different bins.<sup>8</sup>

The statistical correlation matrix among the observables considered is shown in figure 9, in addition to the correlation with the total cross section. In general we observe small correlations of the asymmetries built from  $\mathcal{CP}$ -odd observables, with several relevant exceptions.

In the case of  $thj$  observables, the asymmetry of the triple product of the final particles in the lab frame is considerably correlated with the triple product of the beam axis, the (anti-)top quark and the jet in the Higgs rest frame. This correlation is expected since both quantities are defined relative to the plane formed by the final top-quark and jet. The other highly correlated asymmetries in this process are the ones defined with respect to the angles

![](images/516d1e0bc6815278df704a4f5210c70f60834400541ff3e11bcb92d26988e6a5.jpg)  
Figure 9. Correlation matrices among the statistical uncertainties of the observables considered. In the left panel we show the correlation among the observables of the  $thj$  channel and in the right panel the one for the observables of the  $t\bar{t}h$  channel. The entries smaller than  $5 \text{‰}$  have been set to zero.

![](images/94ee799e876b73a5b1b0613c9f2be1b12e1dbd7b5c6054015e10ae46a7c2974b.jpg)

$\theta_{e}^{y}$  and  $\theta_{e}^{s}$ , which are highly correlated (33%) since both measure projections of the electron direction of flight onto the plane normal to the jet momentum. Regarding the correlation among  $\mathcal{CP}$ -even quantities, it is worth noting the correlation among  $\Delta R(ht)$  and  $M(ht)$ . In this case, low and high invariant masses are preferentially associated to angular separations smaller and larger than  $\pi$ , respectively.

Concerning the  $t\bar{t}h$  observables, we see a strong anti-correlation of the asymmetry of  $\hat{p}_t \cdot (\hat{p}_{e^-} \times \hat{p}_{e^+})|^{t\bar{t}}$  and  $\mathrm{sgn}[\hat{p}_t \cdot (\hat{p}_{e^-} \times \hat{p}_{e^+})](\hat{p}_{e^-} \cdot \hat{p}_{e^+})|^{t\bar{t}}$ , which is expected given that the former is proportional to the sine of the angle formed between the final charged leptons and the latter is proportional to the cosine of that same angle. With respect to the  $\mathcal{CP}$ -even observables, the lower bins of the invariant mass,  $M(ht\bar{t})$ , are more correlated with the higher bins of  $b_4^{\mathrm{lab}}$ .

# 4.2 Expected bounds at the LHC and beyond

Using the experimental information presented in the previous section, summarised in table 2, we perform a fit of the 10 degrees of freedom of our analysis:

$$
\{C _ {\varphi G}, C _ {\varphi \widetilde {G}}, C _ {\varphi W}, C _ {\varphi \widetilde {W}}, C _ {t \varphi}, C _ {t \varphi} ^ {I}, C _ {t G}, C _ {t G} ^ {I}, C _ {t W}, C _ {t W} ^ {I} \}.
$$

The fits are performed using the open source code HEPfit [100] to which we have added the parametrisations of the observables considered in terms of the WC at linear and quadratic order. This code has previously been widely used to perform fits on the SM [101], specific SM extensions [102-104] and the SMEFT [88, 91, 105]. Given that we are considering observables that have not been measured yet, we have set the central values to the SM predictions and estimated their uncertainties as described in the previous section.

In figure 10 we show the expected constraints on the subset of WC considered from a linear and quadratic fit at the LHC Run 3 and at the HL-LHC. The shadowed bars represent the marginalised limits for each WC obtained from the global fit, where all the coefficients have been varied at the same time. The solid bars, however, represent the individual limits

![](images/9960be06ff2558bd4bcf309e0c8382ae328bf1c4ca5d1dbb628ca44566860afa.jpg)  
Figure 10. Expected ranges at a  $95\%$  probability for the WC considered in this work. The shadowed (solid) bars represent the marginalised (individual) limits. In green we show the limits expected for the LHC Run 3 and in red those for the HL-LHC.

obtained by performing a fit of one coefficient at a time. The difference between individual and marginalised fits is greater in the linear fit, where strong correlations (and cancellations) occur. There are some cases in which the individual linear fits provide better constraints than the quadratic one due to the appearance of several modes in the quadratic case but, in general, the quadratic fit provides much better constraints than the linear case.

Indeed, we observe a huge dependence of the fit results on the quadratic terms, even in the HL-LHC. This shows that the precision expected on measuring these observables at the HL-LHC does not seem to be enough to make the proposed asymmetries have a relevant impact on the fit, given that the asymmetries only enter at linear order in the  $\mathcal{CP}$ -odd couplings. Therefore, even though the asymmetries are essential to constrain the  $\mathcal{CP}$ -odd couplings at linear order, the effect of the linear terms is sub-leading compared to higher-order effects considering the precision that we will reach in the near/mid future. In general, one should consider the validity of the EFT when the quadratic pieces dominate, given that those terms are generally expected to be much more suppressed than the linear ones by the NP scale. In the case of the  $\mathcal{CP}$ -odd couplings, however, the suppression of the linear terms in the  $\mathcal{CP}$ -even observables is well justified due to the absence of  $\mathcal{CP}$  violation in the SM, making it natural for the quadratics to dominate. The difference between the individual constraints of the linear and quadratic fit of the  $\mathcal{CP}$ -even coupling of  $O_{t\varphi}$  (the operator on which we focus within this work) is negligible, showing a well perturbative behaviour in this case. This is not the case for the other WC but there are other observables sensitive to those that could be added to specifically constrain them [79, 106-108]. The aim of this work is not providing a global analysis of the  $\mathcal{CP}$ -odd couplings of the full SMEFT but to study the possible constraints on the effective top quark Yukawa, being also aware of the possible effects

![](images/b45981c509b41ddaeb3b1cb9f2b15389f2754fa0874016dbfea611df93a4d1cf.jpg)  
Figure 11. Sensitivity of different observables for the  $\mathcal{CP}$ -even WC represented in terms of the allowed ranges at  $95\%$  probability, fitting one operator at a time with only one observable.

of other operators. It is worth noting that the dominance of quadratic terms in our global fit of dimension-six operators suggests that certain dimension-eight operators, whose leading contribution is suppressed by the NP scale at the same order as quadratic dimension-six terms, could influence the global analysis. This may be particularly relevant for the  $\mathcal{CP}$ -odd couplings, which are primarily constrained by  $\mathcal{CP}$ -even observables and contribute to these observables at the same order as the leading dimension-eight contributions, which were not considered in this analysis. Therefore, some caution is warranted when considering these limits.

The breakdown of the sensitivity to the  $\mathcal{CP}$ -odd couplings for the observables of table 2 is shown in figure 11. In this figure we can see how the observables in  $t\bar{th}$  dominate the constraints on  $C_{t\varphi}^{I}$  thanks to the higher precision of this measurement. In general, the asymmetries provide limits around an order of magnitude worse than the  $\mathcal{CP}$ -even observables. Although  $b_{4}$  is the observable most sensitive to  $C_{t\varphi}^{I}$ , the figure also shows that the differential mass distribution provides similar sensitivity.

As mentioned in section 2, we can also reinterpret the constraints in terms of an effective Yukawa coupling which can be related to the WC  $C_{t\varphi}^{(I)}$ , as shown in eq. (2.4). In figure 12 we show the results of a fit including only the effective Yukawa couplings. The constraints at  $95\%$  probability are given in table 3. The results are compatible with those of a recent ATLAS study [93]. We observe that the limits on the real part of the Yukawa coupling could be improved from LHC Run 3 to HL-LHC by a factor 2 and the imaginary part by a factor 1.5.

In figure 13 we can see the impact of each set of observables on the  $\kappa$  sin  $\alpha -\kappa$  cos  $\alpha$  plane for the LHC Run 3 and the HL-LHC. The first remarkable feature is that, even though the differential cross section of  $t\bar{t} h$  in  $M(ht\bar{t})$  is one of the most sensitive observables, it is crucial to add the measurement of the differential cross section of  $thj$  in  $M(ht)$  in order to remove the degeneracy on the  $\kappa$  sin  $\alpha -\kappa$  cos  $\alpha$  plane at  $95\%$  probability. The inclusion of

![](images/c040778bc0ade1cac92a1fcdd0faa3f46f4e37ee91666f5bf5f1fab623a52bd3.jpg)  
Figure 12. Expected ranges of the effective Yukawa couplings at the LHC Run 3 and at the HL-LHC.

Table 3. Predicted ranges within  $95\%$  probability for  $\kappa \cos \alpha$  and  $\kappa \sin \alpha$  at LHC Run 3 and at HL-LHC from the fit including only the Yukawa couplings.  

<table><tr><td></td><td>LHC (Run 3)</td><td>HL-LHC</td></tr><tr><td>κ cos α</td><td>[0.61, 1.20]</td><td>[0.80, 1.12]</td></tr><tr><td>κ sin α</td><td>[-0.84, 0.84]</td><td>[-0.64, 0.64]</td></tr></table>

![](images/e72b6073c71ed442652a62b9eb325e2e40cec82d0d558fe312a86f7f8dfe2c66.jpg)  
Figure 13. Constraining effect of the different sets of observables on the effective Yukawa couplings for the LHC Run 3 (left) and the HL-LHC (right). The label "Only  $t\bar{th}$  xsec." refers to a fit in which only the differential cross section of  $t\bar{th}$  with respect to the invariant mass of  $t\bar{th}$  is added. The label "Only xsec." includes also the invariant  $t\bar{h}j$  differential cross section with respect to the invariant mass of the  $th$  system. The label "No Asym." removes the asymmetries of table 2 from the fit. Finally, the label "All Obs." refers to a fit including all the observables defined in table 2.

![](images/15e19b767299a27314115a89a337a8ed4d895d9ec4d10f07f586ee99ef8bc7ef.jpg)

other quadratic observables like  $b_4^{\mathrm{lab}}$ , and differential distributions with respect to  $\Delta R(ht)$  and  $\hat{z} \cdot (\hat{p}_t \times \hat{p}_j)$  as shown in table 2, also help to shrink the allowed region. The asymmetries, however, do not have an effect once compared with the effect of the other observables. A similar behaviour is observed for the HL-LHC although the degeneracy on the  $\kappa \sin \alpha - \kappa \cos \alpha$  is less pronounced than in the LHC case.

# 5 Conclusions

In this work, we have studied the  $\mathcal{CP}$ -violating couplings in the top-Higgs sector using LHC processes. Specifically, we focus on two key processes: top-quark pair production in association with a Higgs boson and single top-Higgs associated production. To conduct a model-independent analysis, we parameterised the NP effects using SMEFT operators. Given our focus on these specific LHC processes, we restricted our analysis to the 10 Wilson coefficients relevant to these interactions:  $\{C_{\varphi G}, C_{\varphi \widetilde{G}}, C_{\varphi W}, C_{\varphi \widetilde{W}}, C_{t\varphi}, C_{t\varphi}^{I}, C_{tG}, C_{tG}^{I}, C_{tW}, C_{tW}^{I}\}$ , with particular emphasis on the top-Yukawa couplings  $\{C_{t\varphi}, C_{t\varphi}^{I}\}$ .

To enhance sensitivity to  $\mathcal{CP}$ -violating operators, we proposed and examined several observables that have been or could eventually be measured by the experimental collaborations. In the case of single top Higgs associated production, we studied several triple products of the momenta of the final and/or initial partons which constitute  $\mathcal{CP}$ -odd observables by construction. Besides these observables we also examined observables sensitive to the top-quark polarisation. These observables are angular distributions of the top-quark decay products, in our case the final electron coming from the decay of the  $W$  produced from the top-quark decay. In the top-pair production in association with a Higgs boson, we studied both parton- and particle-level observables. Besides the well-studied  $\mathcal{CP}$ -even observable  $b_{4}$  we also proposed pure  $\mathcal{CP}$ -odd observables built from the azimuthal separation of the leptons as well as triple products of the final state particles.

We then projected the uncertainties associated with these observables at the final stage of the Run 3 of the LHC and in the HL-LHC, assuming integrated luminosities of  $300\mathrm{fb}^{-1}$  and  $3000\mathrm{fb}^{-1}$ , respectively. We have performed a global fit considering the linear and the linear plus quadratic terms of the SMEFT parametrisation. Given the small number of processes considered, we observe a significant difference between the marginalised and individual limits in the linear global fit due to cancellations among the contributions of the different operators. This is not the case for the quadratic fit, which also provides more stringent constraints, especially for the marginalised constraints. Indeed, we expect the difference between the marginalised and the individual limits to be reduced when adding other observables since in this work we have only considered the observables most relevant to constrain the top-Yukawa couplings from LHC data.

In the quadratic fit, the pure  $\mathcal{CP}$ -odd observables proposed will not be measured with enough precision at the HL-LHC to compete with other  $\mathcal{CP}$ -even observables. However, for the linear case these observables are essential to constrain the  $\mathcal{CP}$ -odd couplings, for which the  $\mathcal{CP}$ -even observables offer no sensitivity at linear order.

Finally, by reinterpreting the SMEFT limits in terms of an effective Yukawa coupling, we anticipate a factor of two improvement in the constraints on the imaginary Yukawa coupling at the HL-LHC compared to the current bounds established by ATLAS [93]. In this analysis,

the combination of  $t\bar{t}h$  and  $thj$  processes — despite the limited precision expected for  $thj$  — is crucial to resolve degeneracies in the parameter space of the real and imaginary Yukawa couplings. Purely  $\mathcal{CP}$ -odd observables, however, are not relevant for this scenario and the constraints come mainly from quadratic terms in  $\mathcal{CP}$ -even observables.

Our work establishes a proof of concept for incorporating  $\mathcal{CP}$ -violating effects in the top-Higgs sector within broader global fits of the SMEFT framework. By integrating this analysis alongside constraints from other high-precision probes, such as flavor, electroweak, and Higgs observables, we can progress toward a more comprehensive and interconnected understanding of  $\mathcal{CP}$  violation in the SMEFT. Notably, the inclusion of low-energy observables, such as lepton EDMs, which were not studied here, could provide further insights for the top-Higgs sector. At present, most global fits within the SMEFT framework assume  $\mathcal{CP}$  conservation in new physics sectors, an assumption that future analyses should reconsider and relax. Additionally, advancements in experimental techniques, including enhanced reconstruction methods and machine learning tools, could significantly improve the precision of the measurements beyond our initial conservative estimates. Such improvements are essential for isolating subtle  $\mathcal{CP}$ -violating signals from background effects, thereby advancing the robustness and reach of  $\mathcal{CP}$  violation studies in the high-luminosity era of the LHC.

# Acknowledgments

V.M. would like to thank Giuseppe Ventura and Valentina Vecchio for valuable discussions during this work. The authors would also like to thank Simone Tentori for spotting a typo in the first version of this draft. The work of V.M. and E.V. is supported by the European Research Council (ERC) under the European Union's Horizon 2020 research and innovation programme (Grant agreement No. 949451) and a Royal Society University Research Fellowship through grant URF/R1/201553. The work of Y.P. and J.W. is supported by the ERC under the European Union's Horizon 2020 research and innovation programme (Grant agreement No. 817719).

# A SMEFT operator basis

The SMEFT operators that we have used in our analysis are defined as

$$
O _ {\varphi G} = \left(\varphi^ {\dagger} \varphi\right) G _ {A} ^ {\mu \nu} G _ {\mu \nu} ^ {A}, \qquad O _ {\varphi \widetilde {G}} = \left(\varphi^ {\dagger} \varphi\right) \widetilde {G} _ {A} ^ {\mu \nu} G _ {\mu \nu} ^ {A},
$$

$$
O _ {\varphi W} = \left(\varphi^ {\dagger} \varphi\right) W _ {I} ^ {\mu \nu} W _ {\mu \nu} ^ {I}, \quad O _ {\varphi \widetilde {W}} = \left(\varphi^ {\dagger} \varphi\right) \widetilde {W} _ {I} ^ {\mu \nu} W _ {\mu \nu} ^ {I}, \tag {A.1}
$$

$$
\hat {O} _ {t \varphi} = (\varphi^ {\dagger} \varphi) \bar {Q} t \tilde {\varphi}, \qquad \hat {O} _ {t G} = g _ {S} (\bar {Q} \sigma^ {\mu \nu} T _ {A} t) \tilde {\varphi} G _ {\mu \nu} ^ {A}, \qquad \hat {O} _ {t W} = i (\bar {Q} \sigma^ {\mu \nu} \tau_ {I} t) \tilde {\varphi} W _ {\mu \nu} ^ {I},
$$

where  $\varphi$  ( $\widetilde{\varphi}$ ) represents the (charge-conjugate) SM Higgs doublet,  $Q$  is the bottom- and top-quark left-handed doublet,  $t$  is the right-handed top-quark,  $G_{A}^{\mu \nu}$  and  $W_{\mu \nu}^{I}$  stand for the  $\mathrm{SU}(3)_C$  and  $\mathrm{SU}(2)_L$  field strength tensors, and  $T_{A}$  and  $\tau_{I}$  are the generators of the  $\mathrm{SU}(3)_C$  and  $\mathrm{SU}(2)_L$  groups, respectively.

The other operators mentioned in the text but not included in the analysis are

$$
O _ {\varphi} = \left(\varphi^ {\dagger} \varphi\right) ^ {3}, \qquad \qquad O _ {\varphi \square} = \left(\varphi^ {\dagger} \varphi\right) \square (\varphi^ {\dagger} \varphi), \qquad \qquad O _ {\varphi D} = \left(\varphi^ {\dagger} D ^ {\mu} \varphi\right) ^ {*} \left(\varphi^ {\dagger} D _ {\mu} \varphi\right),
$$

$$
O _ {G} = f ^ {A B C} G _ {\mu} ^ {A \nu} G _ {\nu} ^ {B \rho} G _ {\rho} ^ {C \mu}, \qquad O _ {W} = \epsilon^ {I J K} W _ {\mu} ^ {I \nu} W _ {\nu} ^ {J \rho} W _ {\rho} ^ {K \mu},
$$

$$
O _ {\widetilde {G}} = f ^ {A B C} \widetilde {G} _ {\mu} ^ {A \nu} G _ {\nu} ^ {B \rho} G _ {\rho} ^ {C \mu}, \quad O _ {\widetilde {W}} = \epsilon^ {I J K} \widetilde {W} _ {\mu} ^ {I \nu} W _ {\nu} ^ {J \rho} W _ {\rho} ^ {K \mu}, \tag {A.2}
$$

$$
O _ {\varphi B} = \left(\varphi^ {\dagger} \varphi\right) B ^ {\mu \nu} B _ {\mu \nu}, \qquad O _ {\varphi W B} = \left(\varphi^ {\dagger} \varphi\right) W _ {I} ^ {\mu \nu} B _ {\mu \nu},
$$

$$
O _ {\varphi \widetilde {B}} = \left(\varphi^ {\dagger} \varphi\right) \widetilde {B} ^ {\mu \nu} B _ {\mu \nu}, \qquad O _ {\varphi \widetilde {W} B} = \left(\varphi^ {\dagger} \varphi\right) \widetilde {W} _ {I} ^ {\mu \nu} B _ {\mu \nu},
$$

with  $f^{ABC}$  and  $\epsilon^{IJK}$  the structure constants of the  $\mathrm{SU}(3)_C$  and  $\mathrm{SU}(2)_L$  groups, respectively.

# B Additional figures

Here we present the dependence on the WC of some additional observables presented in the main text.

![](images/f75e0c1dab344bb4238a3234e5b5329513543a46444de7e3fd7d704bd380f68c.jpg)  
(a)

![](images/2d433e959a8a875c4043dff3c1934e5f887d8b9c9544b1decbd571dc55071769.jpg)  
(b)

![](images/c9f1d2482614a8ada66c5ece65dc4895b4e2cca1a036e84d5ce8ecbc9ba424f4.jpg)  
(c)

![](images/6b2ef5c0f5126a7a6848ac44ddb5cf2b218b2de30ebc8355f2e9c96a67058ffc.jpg)  
(d)

![](images/5559e1b19ebaadd89c00b701e2f8e44b44e92a226dd66fc4c62c7567e7424ff0.jpg)  
(e)

![](images/5cf318ba147a41307b4d4747428229c3a7398433e9f9024c64b3e77897244125.jpg)  
(f)

![](images/a57e5f1b04e9ffe0d380ee7a83869df57eba71f84ca0d2bea418e85e3266b967.jpg)  
(g)

![](images/aa20ddd04164a6e1d140c40386e8ea8f6570a4c69ed39d3a3f52f87bcce71e29.jpg)  
Figure 14. Differential cross sections of the observables  $b_{2}$  (eq. (3.4)) and  $b_{4}$  (eq. (3.5)) for the operators  $\hat{O}_{t\varphi}$  (up),  $O_{\varphi G / \widetilde{G}}$  (centre up),  $\hat{O}_{tG}$  (centre down) and  $\hat{O}_{tW}$  (down).  
(h)

Data Availability Statement. This article has no associated data or the data will not be deposited.

Code Availability Statement. This article has no associated code or the code will not be deposited.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] A.D. Sakharov, Violation of CP Invariance,  $C$  asymmetry, and baryon asymmetry of the universe, Pisma Zh. Eksp. Teor. Fiz. 5 (1967) 32 [INSPIRE].  
[2] X. Zhang, S.K. Lee, K. Whisnant and B.L. Young, Phenomenology of a nonstandard top quark Yukawa coupling, Phys. Rev. D 50 (1994) 7042 [hep-ph/9407259] [INSPIRE].  
[3] M. Trodden, Electroweak baryogenesis, Rev. Mod. Phys. 71 (1999) 1463 [hep-ph/9803479] [INSPIRE].  
[4] CMS collaboration, Observation of  $t\bar{t}H$  production, Phys. Rev. Lett. 120 (2018) 231801 [arXiv:1804.02610] [INSPIRE].  
[5] ATLAS collaboration, Observation of Higgs boson production in association with a top quark pair at the LHC with the ATLAS detector, Phys. Lett. B 784 (2018) 173 [arXiv:1806.00425] [INSPIRE].  
[6] ATLAS collaboration, A detailed map of Higgs boson interactions by the ATLAS experiment ten years after the discovery, Nature 607 (2022) 52 [Erratum ibid. 612 (2022) E24] [arXiv:2207.00092] [INSPIRE].  
[7] CMS collaboration, Search for CP violation in ttH and tH production in multilepton channels in proton-proton collisions at  $\sqrt{s} = 13$  TeV, JHEP 07 (2023) 092 [arXiv:2208.02686] [INSPIRE].  
[8] G. Klamke and D. Zeppenfeld, Higgs plus two jet production via gluon fusion as a signal at the CERN LHC, JHEP 04 (2007) 052 [hep-ph/0703202] [INSPIRE].  
[9] A. Freitas and P. Schwaller, Higgs CP Properties From Early LHC Data, Phys. Rev. D 87 (2013) 055014 [arXiv:1211.1980] [INSPIRE].  
[10] A. Djouadi and G. Moreau, The couplings of the Higgs boson and its CP properties from fits of the signal strengths and their ratios at the  $7 + 8$  TeV LHC, Eur. Phys. J. C 73 (2013) 2512 [arXiv:1303.6591] [INSPIRE].  
[11] F. Demartin et al., Higgs characterisation at NLO in QCD: CP properties of the top-quark Yukawa interaction, Eur. Phys. J. C 74 (2014) 3065 [arXiv:1407.5089] [INSPIRE].  
[12] C. Englert, P. Galler, A. Pilkington and M. Spannowsky, Approaching robust EFT limits for CP-violation in the Higgs sector, Phys. Rev. D 99 (2019) 095007 [arXiv:1901.05982] [INSPIRE].  
[13] A. Bhardwaj, C. Englert, D. Gonçalves and A. Navarro, Nonlinear CP violation in the top-Higgs sector, Phys. Rev. D 108 (2023) 115006 [arXiv:2308.11722] [INSPIRE].  
[14] H. Bahl, E. Fuchs, M. Hannig and M. Menen, Classifying the CP properties of the ggH coupling in  $H + 2j$  production, SciPost Phys. Core 8 (2025) 006 [arXiv:2309.03146] [INSPIRE].

[15] S. Weinberg, Larger Higgs Exchange Terms in the Neutron Electric Dipole Moment, Phys. Rev. Lett. 63 (1989) 2333 [INSPIRE].  
[16] S.M. Barr and A. Zee, Electric Dipole Moment of the Electron and of the Neutron, Phys. Rev. Lett. 65 (1990) 21 [Erratum ibid. 65 (1990) 2920] [INSPIRE].  
[17] J. Brod, U. Haisch and J. Zupan, Constraints on CP-violating Higgs couplings to the third generation, JHEP 11 (2013) 180 [arXiv:1310.1385] [INSPIRE].  
[18] J. Brod and E. Stamou, Electric dipole moment constraints on CP-violating heavy-quark Yukawas at next-to-leading order, JHEP 07 (2021) 080 [arXiv:1810.12303] [INSPIRE].  
[19] E. Fuchs, M. Losada, Y. Nir and Y. Viernik, CP violation from  $\tau$ ,  $t$  and  $b$  dimension-6 Yukawa couplings-interplay of baryogenesis, EDM and Higgs physics, JHEP 05 (2020) 056 [arXiv:2003.00099] [INSPIRE].  
[20] H. Bahl et al., Constraining the  $\mathcal{CP}$  structure of Higgs-fermion couplings with a global LHC fit, the electron EDM and baryogenesis, Eur. Phys. J. C 82 (2022) 604 [arXiv:2202.11753] [INSPIRE].  
[21] J. Brod, J.M. Cornell, D. Skodras and E. Stamou, Global constraints on Yukawa operators in the standard model effective theory, JHEP 08 (2022) 294 [arXiv:2203.03736] [INSPIRE].  
[22] J. Brod, Z. Polonsky and E. Stamou, A precise electron EDM constraint on CP-odd heavy-quark Yukawas, JHEP 06 (2024) 091 [arXiv:2306.12478] [INSPIRE].  
[23] J.F. Gunion and X.-G. He, Determining the CP nature of a neutral Higgs boson at the LHC, Phys. Rev. Lett. 76 (1996) 4468 [hep-ph/9602226] [INSPIRE].  
[24] X.-G. He, G.-N. Li and Y.-J. Zheng, Probing Higgs boson CP Properties with  $t\bar{t}H$  at the LHC and the 100 TeV pp collider, Int. J. Mod. Phys. A 30 (2015) 1550156 [arXiv:1501.00012] [INSPIRE].  
[25] Y.T. Chien et al., Direct and indirect constraints on CP-violating Higgs-quark and Higgs-gluon interactions, JHEP 02 (2016) 011 [arXiv:1510.00725] [INSPIRE].  
[26] F. Boudjema, R.M. Godbole, D. Guadagnoli and K.A. Mohan, Lab-frame observables for probing the top-Higgs interaction, Phys. Rev. D 92 (2015) 015019 [arXiv:1501.03157] [INSPIRE].  
[27] M.R. Buckley and D. Gonçalves, Boosting the Direct CP Measurement of the Higgs-Top Coupling, Phys. Rev. Lett. 116 (2016) 091801 [arXiv:1507.07926] [INSPIRE].  
[28] S.D. Rindani, P. Sharma and A. Shivaji, Unraveling the CP phase of top-Higgs coupling in associated production at the LHC, Phys. Lett. B 761 (2016) 25 [arXiv:1605.03806] [INSPIRE].  
[29] A.V. Gritsan, R. Röntsch, M. Schulze and M. Xiao, Constraining anomalous Higgs boson couplings to the heavy flavor fermions using matrix element techniques, Phys. Rev. D 94 (2016) 055023 [arXiv:1606.03107] [INSPIRE].  
[30] N. Mileo et al., Pseudoscalar top-Higgs coupling: exploration of CP-odd observables to resolve the sign ambiguity, JHEP 07 (2016) 056 [arXiv:1603.03632] [INSPIRE].  
[31] A. Kobakhidze, N. Liu, L. Wu and J. Yue, Implications of CP-violating Top-Higgs Couplings at LHC and Higgs Factories, Phys. Rev. D 95 (2017) 015016 [arXiv:1610.06676] [INSPIRE].  
[32] Q.-H. Cao, S.-L. Chen and Y. Liu, Probing Higgs Width and Top Quark Yukawa Coupling from  $t\bar{t}H$  and  $t\bar{t}t\bar{t}$  Productions, Phys. Rev. D 95 (2017) 053004 [arXiv:1602.01934] [INSPIRE].  
[33] D. Azevedo, A. Onofre, F. Filthaut and R. Gonçalo, CP tests of Higgs couplings in tth semileptonic events at the LHC, Phys. Rev. D 98 (2018) 033004 [arXiv:1711.05292] [INSPIRE].

[34] D. Gonçalves, K. Kong and J.H. Kim, Probing the top-Higgs Yukawa CP structure in dileptonic  $t\bar{t}h$  with  $M_2$ -assisted reconstruction, JHEP 06 (2018) 079 [arXiv:1804.05874] [INSPIRE].  
[35] W.-S. Hou, M. Kohda and T. Modak, Probing for extra top Yukawa couplings in light of  $t\bar{t}h$  (125) observation, Phys. Rev. D 98 (2018) 075007 [arXiv:1806.06018] [INSPIRE].  
[36] Q.-H. Cao et al., Limiting top quark-Higgs boson interaction and Higgs-boson width from multitop productions, Phys. Rev. D 99 (2019) 113003 [arXiv:1901.04567] [INSPIRE].  
[37] D.A. Faroughy, J.F. Kamenik, N. Košnik and A. Smolkovič, Probing the CP nature of the top quark Yukawa at hadron colliders, JHEP 02 (2020) 085 [arXiv:1909.00007] [INSPIRE].  
[38] B. Bortolato, J.F. Kamenik, N. Košnik and A. Smolkovič, Optimized probes of CP -odd effects in the  $t\overline{t}h$  process at hadron colliders, Nucl. Phys. B 964 (2021) 115328 [arXiv:2006.13110] [INSPIRE].  
[39] Q.-H. Cao, K.-P. Xie, H. Zhang and R. Zhang, A New Observable for Measuring CP Property of Top-Higgs Interaction, Chin. Phys. C 45 (2021) 023117 [arXiv:2008.13442] [INSPIRE].  
[40] H. Bahl et al., Indirect CP probes of the Higgs-top-quark interaction: current LHC constraints and future opportunities, JHEP 11 (2020) 127 [arXiv:2007.08542] [INSPIRE].  
[41] R.K. Barman, D. Gonçalves and F. Kling, Mach. Learn. the Higgs boson-top quark CP phase, Phys. Rev. D 105 (2022) 035023 [arXiv:2110.07635] [INSPIRE].  
[42] D. Gonçalves, J.H. Kim, K. Kong and Y. Wu, Direct Higgs-top CP-phase measurement with  $t\bar{t}h$  at the 14 TeV LHC and 100 TeV FCC, JHEP 01 (2022) 158 [arXiv:2108.01083] [INSPIRE].  
[43] T. Martini, R.-Q. Pan, M. Schulze and M. Xiao, Probing the CP structure of the top quark Yukawa coupling: Loop sensitivity versus on-shell sensitivity, Phys. Rev. D 104 (2021) 055045 [arXiv:2104.04277] [INSPIRE].  
[44] R.K. Barman et al., Directly Probing the CP-structure of the Higgs-Top Yukawa at HL-LHC and Future Colliders, in the proceedings of the Snowmass 2021, Seattle, U.S.A., July 17-26 (2022) [arXiv:2203.08127] [INSPIRE].  
[45] J. Hermann, D. Stremmer and M. Worek,  $\mathcal{CP}$  structure of the top-quark Yukawa interaction: NLO QCD corrections and off-shell effects, JHEP 09 (2022) 138 [arXiv:2205.09983] [INSPIRE].  
[46] D. Azevedo, R. Capucha, A. Onofre and R. Santos,  $CP$ -violation, asymmetries and interferences in  $t\bar{t}\phi$ , JHEP 09 (2022) 246 [arXiv:2208.04271] [INSPIRE].  
[47] H. Bahl et al.,  $\mathcal{CP}$ -sensitive simplified template cross-sections for  $t\bar{t}H$ , JHEP 10 (2024) 214 [arXiv:2406.03950] [INSPIRE].  
[48] F. Maltoni, D. Pagani and S. Tentori, Top-quark pair production as a probe of light top-philic scalars and anomalous Higgs interactions, JHEP 09 (2024) 098 [arXiv:2406.06694] [INSPIRE].  
[49] P. Agrawal, S. Mitra and A. Shivaji, Effect of Anomalous Couplings on the Associated Production of a Single Top Quark and a Higgs Boson at the LHC, JHEP 12 (2013) 077 [arXiv:1211.4362] [INSPIRE].  
[50] J. Ellis, D.S. Hwang, K. Sakurai and M. Takeuchi, Disentangling Higgs-Top Couplings in Associated Production, JHEP 04 (2014) 004 [arXiv:1312.5736] [INSPIRE].  
[51] A. Kobakhidze, L. Wu and J. Yue, Anomalous Top-Higgs Couplings and Top Polarisation in Single Top and Higgs Associated Production at the LHC, JHEP 10 (2014) 100 [arXiv:1406.1961] [INSPIRE].  
[52] J. Yue, Enhanced thj signal at the LHC with  $h \to \gamma \gamma$  decay and  $\mathcal{CP}$ -violating top-Higgs coupling, Phys. Lett. B 744 (2015) 131 [arXiv:1410.2701] [INSPIRE].

[53] J. Chang, K. Cheung, J.S. Lee and C.-T. Lu, Probing the Top-Yukawa Coupling in Associated Higgs production with a Single Top Quark, JHEP 05 (2014) 062 [arXiv:1403.2053] [INSPIRE].  
[54] F. Demartin, F. Maltoni, K. Mawatari and M. Zaro, Higgs production in association with a single top quark at the LHC, Eur. Phys. J. C 75 (2015) 267 [arXiv:1504.00611] [INSPIRE].  
[55] F. Demartin et al., tWH associated production at the LHC, Eur. Phys. J. C 77 (2017) 34 [arXiv:1607.05862] [INSPIRE].  
[56] M. Kraus, T. Martini, S. Peitzsch and P. Uwer, Exploring BSM Higgs couplings in single top-quark production, arXiv:1908.09100 [INSPIRE].  
[57] R. Patrick, A. Scaffidi and P. Sharma, Top polarisation as a probe of CP-mixing top-Higgs coupling in tjh signals, Phys. Rev. D 101 (2020) 093005 [arXiv:1909.12772] [INSPIRE].  
[58] V. Barger, K. Hagiwara and Y.-J. Zheng, Probing the top Yukawa coupling at the LHC via associated production of single top and Higgs, JHEP 09 (2020) 101 [arXiv:1912.11795] [INSPIRE].  
[59] S. Bhattacharya, S. Biswas, K. Pal and J. Wudka, Associated production of Higgs and single top at the LHC in presence of the SMEFT operators, JHEP 08 (2023) 015 [arXiv:2211.05450] [INSPIRE].  
[60] C. Englert, K. Nordström, K. Sakurai and M. Spannowsky, *Perturbative Higgs CP violation*, unitarity and phenomenology, Phys. Rev. D 95 (2017) 015018 [arXiv:1611.05445] [INSPIRE].  
[61] V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Is there room for CP violation in the top-Higgs sector?, Phys. Rev. D 94 (2016) 016002 [arXiv:1603.03049] [INSPIRE].  
[62] V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Constraining the top-Higgs sector of the Standard Model Effective Field Theory, Phys. Rev. D 94 (2016) 034031 [arXiv:1605.04311] [INSPIRE].  
[63] U. Haisch and A. Hala, Bounds on CP-violating Higgs-gluon interactions: the case of vanishing light-quark Yukawa couplings, JHEP 11 (2019) 117 [arXiv:1909.09373] [INSPIRE].  
[64] V. Cirigliano et al., CP Violation in Higgs-Gauge Interactions: From Tabletop Experiments to the LHC, Phys. Rev. Lett. 123 (2019) 051801 [arXiv:1903.03625] [INSPIRE].  
[65] J. Kley, T. Theil, E. Venturini and A. Weiler, Electric dipole moments at one-loop in the dimension-6 SMEFT, Eur. Phys. J. C 82 (2022) 926 [arXiv:2109.15085] [INSPIRE].  
[66] C. Degrande and J. Touchéque, A reduced basis for CP violation in SMEFT at colliders and its application to diboson production, JHEP 04 (2022) 032 [arXiv:2110.02993] [INSPIRE].  
[67] C. Degrande et al., Automated one-loop computations in the standard model effective field theory, Phys. Rev. D 103 (2021) 096024 [arXiv:2008.11743] [INSPIRE].  
[68] D. Barducci et al., Interpreting top-quark LHC measurements in the standard-model effective field theory, arXiv:1802.07237 [INSPIRE].  
[69] F. Krauss, S. Kuttimalai and T. Plehn, LHC multijet events as a probe for anomalous dimension-six gluon interactions, Phys. Rev. D 95 (2017) 035024 [arXiv:1611.00767] [INSPIRE].  
[70] V. Hirschi, F. Maltoni, I. Tsinikos and E. Vryonidou, Constraining anomalous gluon self-interactions at the LHC: a reappraisal, JHEP 07 (2018) 093 [arXiv:1806.04696] [INSPIRE].  
[71] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections, and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].

[72] I. Brivio, SMEFTsim 3.0 - a practical guide, JHEP 04 (2021) 073 [arXiv:2012.11343] [INSPIRE].  
[73] C. Degrande et al., *UFO - The Universal FeynRules Output*, Comput. Phys. Commun. **183** (2012) 1201 [arXiv:1108.2040] [INSPIRE].  
[74] L. Darmé et al., *UFO 2.0: the 'Universal Feynman Output' format*, Eur. Phys. J. C **83** (2023) 631 [arXiv:2304.09883] [INSPIRE].  
[75] F. Maltoni and T. Stelzer, MadEvent: Automatic event generation with MadGraph, JHEP 02 (2003) 027 [hep-ph/0208156] [INSPIRE].  
[76] P. Artoisenet, R. Frederix, O. Mattelaer and R. Rietkerk, Automatic spin-entangled decays of heavy resonances in Monte Carlo simulations, JHEP 03 (2013) 015 [arXiv:1212.3460] [INSPIRE].  
[77] M. de Beurs, E. Laenen, M. Vreeswijk and E. Vryonidou, Effective operators in t-channel single top production and decay, Eur. Phys. J. C 78 (2018) 919 [arXiv:1807.03576] [INSPIRE].  
[78] J. Ren, L. Wu and J.M. Yang, Unveiling CP property of top-Higgs coupling with graph neural networks at the LHC, Phys. Lett. B 802 (2020) 135198 [arXiv:1901.05627] [INSPIRE].  
[79] A. Bhardwaj, C. Englert, R. Hankache and A.D. Pilkington, Machine-enhanced CP-asymmetries in the Higgs sector, Phys. Lett. B 832 (2022) 137246 [arXiv:2112.05052] [INSPIRE].  
[80] H. Bahl and S. Brass, Constraining  $\mathcal{CP}$ -violation in the Higgs-top-quark interaction using machine-learning-based inference, JHEP 03 (2022) 017 [arXiv:2110.10177] [INSPIRE].  
[81] N.C. Hall et al., Machine-enhanced CP-asymmetries in the electroweak sector, Phys. Rev. D 107 (2023) 016008 [arXiv:2209.05143] [INSPIRE].  
[82] A. Butter et al., Two invertible networks for the matrix element method, SciPost Phys. 15 (2023) 094 [arXiv:2210.00019] [INSPIRE].  
[83] J. Ackerschott et al., Returning CP-observables to the frames they belong, SciPost Phys. 17 (2024) 001 [arXiv:2308.00027] [INSPIRE].  
[84] W. Esmail, A. Hammad, A. Jueid and S. Moretti, Boosting probes of CP violation in the top Yukawa coupling with Deep Learning, arXiv:2405.16499 [INSPIRE].  
[85] A. Hammad and A. Jueid, Progress in  $\mathcal{CP}$  violating top-Higgs coupling at the LHC with Machine Learning, arXiv:2504.11791 [INSPIRE].  
[86] CMS collaboration, Search for new physics using effective field theory in 13 TeV pp collision events that contain a top quark pair and a boosted Z or Higgs boson, Phys. Rev. D 108 (2023) 032008 [arXiv:2208.12837] [INSPIRE].  
[87] I. Brivio et al., O new physics, where art thou? A global search in the top sector, JHEP 02 (2020) 131 [arXiv:1910.03606] [INSPIRE].  
[88] G. Durieux et al., The electro-weak couplings of the top and bottom quarks — Global fit and future prospects, JHEP 12 (2019) 098 [Erratum ibid. 01 (2021) 195] [arXiv:1907.10619] [INSPIRE].  
[89] J. Ellis et al., Top, Higgs, Diboson and Electroweak Fit to the Standard Model Effective Field Theory, JHEP 04 (2021) 279 [arXiv:2012.02779] [INSPIRE].  
[90] SMEFiT collaboration, Combined SMEFT interpretation of Higgs, diboson, and top quark data from the LHC, JHEP 11 (2021) 089 [arXiv:2105.00006] [INSPIRE].

[91] V. Miralles et al., The top quark electro-weak couplings after LHC Run 2, JHEP 02 (2022) 032 [arXiv:2107.13917] [INSPIRE].  
[92] E. Celada et al., Mapping the SMEFT at high-energy colliders: from LEP and the (HL-)LHC to the FCC-ee, JHEP 09 (2024) 091 [arXiv:2404.12809] [INSPIRE].  
[93] ATLAS collaboration, Probing the CP nature of the top-Higgs Yukawa coupling in  $t\bar{t}H$  and  $tH$  events with  $H \rightarrow b\bar{b}$  decays using the ATLAS detector at the LHC, Phys. Lett. B 849 (2024) 138469 [arXiv:2303.05974] [INSPIRE].  
[94] ATLAS collaboration, CP Properties of Higgs Boson Interactions with Top Quarks in the  $ttH$  and  $tH$  Processes Using  $H \rightarrow \gamma \gamma$  with the ATLAS Detector, Phys. Rev. Lett. 125 (2020) 061802 [arXiv:2004.04545] [INSPIRE].  
[95] ATLAS collaboration, Measurement of Higgs boson decay into  $b$ -quarks in associated production with a top-quark pair in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, JHEP 06 (2022) 097 [arXiv:2111.06712] [INSPIRE].  
[96] CMS collaboration, Measurements of Higgs boson production cross sections and couplings in the diphoton decay channel at  $\sqrt{s} = 13$  TeV, JHEP 07 (2021) 027 [arXiv:2103.06956] [INSPIRE].  
[97] CMS collaboration, Constraints on anomalous Higgs boson couplings to vector bosons and fermions in its production and decay using the four-lepton final state, Phys. Rev. D 104 (2021) 052004 [arXiv:2104.12152] [INSPIRE].  
[98] CMS collaboration, Measurement of the  $t\bar{t}H$  and  $tH$  production rates in the  $H \rightarrow b\bar{b}$  decay channel with 138  $fb^{-1}$  of proton-proton collision data at  $\sqrt{s} = 13$  TeV, CMS-PAS-HIG-19-011, CERN, Geneva (2023).  
[99] CMS collaboration, Search for associated production of a Higgs boson and a single top quark in proton-proton collisions at  $\sqrt{s} = 13$  TeV, Phys. Rev. D 99 (2019) 092005 [arXiv:1811.09696] [INSPIRE].  
[100] J. De Blas et al., HEPfit: a code for the combination of indirect and direct constraints on high energy physics models, Eur. Phys. J. C 80 (2020) 456 [arXiv:1910.14012] [INSPIRE].  
[101] J. de Blas et al., Global analysis of electroweak data in the Standard Model, Phys. Rev. D 106 (2022) 033003 [arXiv:2112.07274] [INSPIRE].  
[102] A.M. Coutinho, A. Karan, V. Miralles and A. Pich, Light scalars within the  $\mathcal{CP}$ -conserving Aligned-two-Higgs-doublet model, JHEP 02 (2025) 057 [arXiv:2412.14906] [INSPIRE].  
[103] A. Karan, V. Miralles and A. Pich, Updated global fit of the aligned two-Higgs-doublet model with heavy scalars, Phys. Rev. D 109 (2024) 035012 [arXiv:2307.15419] [INSPIRE].  
[104] O. Eberhardt, V. Miralles and A. Pich, Constraints on coloured scalars from global fits, JHEP 10 (2021) 123 [arXiv:2106.12235] [INSPIRE].  
[105] F. Cornet-Gomez et al., Future collider constraints on top-quark operators, arXiv:2503.11518 [INSPIRE].  
[106] R. Barrué, P. Conde-Muño, V. Dao and R. Santos, Simulation-based inference in the search for CP violation in leptonic WH production, JHEP 04 (2024) 014 [arXiv:2308.02882] [INSPIRE].  
[107] A.N. Rossia and E. Vryonidou, CP-odd effects at NLO in SMEFT WH and ZH production, JHEP 11 (2024) 142 [arXiv:2409.00168] [INSPIRE].  
[108] M.O.A. Thomas and E. Vryonidou, CP violation in loop-induced diboson production, JHEP 03 (2025) 038 [arXiv:2411.00959] [INSPIRE].