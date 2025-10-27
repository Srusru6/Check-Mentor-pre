# EFT approach of inelastic dark matter for Xenon electron recoil detection

To cite this article: Hong-Jian He et al JCAP01(2021)042

View the article online for updates and enhancements.

# You may also like

- A next-generation liquid xenon observatory for dark matter and neutrino physics  
J Aalbers, S S AbdusSalam, K Abe et al.  
Prospect of dark matter searches in split SUSY models Nobuchika Okada and Hieu Minh Tran  
- Convolutional neural networks for direct detection of dark matter
Charanjit K Khosa, Lucy Mars, Joel Richards et al.

# EFT approach of inelastic dark matter for Xenon electron recoil detection

Hong-Jian He, $^{a,b,c}$  Yu-Chen Wang $^{b}$  and Jiaming Zheng $^{a}$

${}^{a}$  Tsung-Dao Lee Institute & School of Physics and Astronomy,

Key Laboratory for Particle Astrophysics and Cosmology (MOE),

Shanghai Key Laboratory for Particle Physics and Cosmology,

Shanghai Jiao Tong University, Shanghai 200240, China

$^{b}$ Institute of Modern Physics and Department of Physics, Tsinghua University,

Beijing 100084, China

${}^{c}$  Center for High Energy Physics, Peking University,

Beijing 100871, China

E-mail: hjhe@sjtu.edu.cn, wang-yc15@mails.tsinghua.edu.cn,

zhengjm3@sjtu.edu.cn

Received July 14, 2020

Revised September 10, 2020

Accepted November 27, 2020

Published January 21, 2021

Abstract. Measuring dark matter (DM) signals via electron recoil provides an important means for direct detection of light DM particles. The recent XENON1T anomaly with electron recoil energy around  $E_{R} = (2 - 3)\mathrm{keV}$  can be naturally explained by DM inelastic scattering which injects energy to the recoiled electrons and gives a narrow peak structure in the recoil spectrum. We present an effective field theory (EFT) approach to exothermic inelastic DM signals for the Xenon electron recoil detection. For relatively heavy mediator, we fairly formulate the DM-lepton interactions by effective contact operators with two DM fields  $(X,X^{\prime})$  and two leptons. Using the XENON1T data, we fit the electron recoil spectrum and constrain the allowed scalar DM mass-splitting as  $2.1\mathrm{keV} < \Delta m < 3.3\mathrm{keV}$  (95% C.L.), with the best fit  $\Delta m = 2.8\mathrm{keV}$ . We analyze the relic abundance produced by such effective DM-electron contact interaction. To provide both the DM relic abundance and the XENON1T excess, we derive new constraints on the DM mass and the UV cutoff scale of DM effective interactions. Finally, we study possible UV completions for the effective DM-lepton contact interactions.

Keywords: dark matter theory, particle physics - cosmology connection, dark matter experiments

ArXiv ePrint: 2007.04963

# Contents

1 Introduction 1  
2 EFT analysis of inelastic dark matter and Xenon electron recoil 2

2.1 Realizing minimal inelastic dark matter 2  
2.2 EFT analysis of inelastic DM for Xenon electron recoil 5

3 Constraints from DM relic abundance and decays 9  
4 UV completion for effective DM-lepton interactions 14

4.1 Mediation by second Higgs doublet 14  
4.2 Mediation by vector-like heavy leptons 14  
4.3 UV completion for vector-type contact operator 15

5 Conclusions 17  
A Independent operators for DM-lepton interactions 18

# 1 Introduction

With the tremendous experimental efforts of searching dark matter (DM) particles ranging from the underground up to the sky over the past thirty years, the dark matter physics is expected to be approaching an exciting turning point. Among various ground-based experiments, measuring the DM signal via electron recoil provides an important means for directly detecting light DM particles. The XENON collaboration [1] has newly announced an excess of events with low electron recoil energy around  $E_{R} = (2 - 3)\mathrm{keV}$  [2]. The XENON1T detector recorded 285 events over the range  $E_{R} = (1 - 7)\mathrm{keV}$ , in which the expected background events are  $232\pm 15$  [2]. This leads to a  $3.5\sigma$  excess above the expected backgrounds. Such an anomaly may be attributed to possible tritium  $\beta$  decays in the backgrounds [2, 3] or by new physics beyond the Standard Model (SM). In the latter case, the XENON collaboration also pointed out two simple possibilities [2]: (i) solar neutrinos with a large magnetic dipole moment [4-6] and (ii) solar axions [7-9] absorbed by the recoiled electrons. However, both explanations have severe tension with stellar cooling constraints [10] such as those from the white dwarfs and globular clusters. Absorption of other light DM particles [11-14], such as axion-like particles or dark photons can also give rise to a narrow peak signal at low recoil energy.

Another class of explanations for the excess have focused on the scattering between DM and electrons in XENON1T. But, for an elastic DM-electron scattering process, it was found [15] that the DM particle  $X$  has to be as fast as  $0.05c$  with mass  $m_X \gtrsim 0.1\mathrm{MeV}$  in order to produce the desired electron recoil energy of  $O(\mathrm{keV})$ , where  $c$  denotes the light velocity. This is an order of magnitude faster than the local escape velocity  $v_{\mathrm{esc}} \sim 10^{-3}c$  from the Milky Way. There are related attempts to realize such a boosted DM component for explaining the XENON1T excess [16-22]. Various other attempts also newly appeared [14, 23-32, 32-55].

In this work, we investigate an attractive resolution that the electron recoil is induced by inelastic scattering<sup>1</sup> of a heavier DM component  $X'$  to a lighter component  $X$ . The exothermic inelastic DM scattering was studied before for the DM scattering with nuclei as an explanation to the DAMA/LIBRA excess [56-58]. For the present study, we fit the XENON1T data and find that the inelastic DM-electron scattering leads to a narrow peak in the recoil spectrum for the DM mass-splitting  $\Delta m\simeq (2.1 - 3.3)\mathrm{keV}$ , which is consistent with the XENON1T excess. This also means that its crossing channel will generate the DM annihilation  $XX^{\prime}\rightarrow e^{-}e^{+}$ . We present an effective field theory (EFT) approach to inelastic DM signals for the Xenon electron recoil detection. For relatively heavy mediator, we can fairly formulate the DM-electron interactions by effective contact operators with two DM fields  $(X,X^{\prime})$  and two electrons. We demonstrate that the DM relic abundance can be determined by the freeze-out of this annihilation process. We compute the lifetime of the heavier DM component and find that it can be much longer than the age of the Universe due to the small mass-splitting required to explain the XENON1T excess.

The paper is organized as follows. In section 2, we present the gauge-invariant effective operators of dimension-6 which realize exothermic inelastic scattering between the DM and electrons. We analyze the contributions of these operators to the electron recoil spectrum and fit them with the XENON1T data. With this we identify the allowed parameter space for the inelastic DM. In section 3, we study the contributions of the inelastic DM to the relic abundance and derive the constraints. We further analyze the lifetime of the heavier DM component  $X^{\prime}$  and other constraints by the collider experiments. In section 4, we discuss three possible UV completions of these effective operators. Finally, we conclude in section 5. Appendix A presents a proof of the independent operators for the DM-lepton interactions which are used for the current EFT approach.

# 2 EFT analysis of inelastic dark matter and Xenon electron recoil

In this section, we study the inelastic DM as a resolution to the XENON1T anomaly. We present an effective field theory (EFT) approach to inelastic DM signals for the Xenon electron recoil detection. For relatively heavy mediator, we formulate the DM-electron interactions by effective contact operators with two DM fields  $(X,X^{\prime})$  and two electrons. Then we analyze the predicted electron recoil energy spectrum and identify the allowed parameter space by fitting the XENON1T data and imposing the bound from CMB measurements of the DM relic abundance.

# 2.1 Realizing minimal inelastic dark matter

For the present study, we construct a minimal dark sector for inelastic DM, including two light real scalar DM fields  $X$  and  $X'$ , with masses around  $m_{X}, m_{X'} = O(\mathrm{GeV}) \gg m_{e}$  and a small mass-difference  $\Delta m \equiv m_{X'} - m_{X} = O(2-3)\mathrm{keV}$ . In our EFT construction, the DM fields  $(X, X')$  are the SM singlets and odd under a  $\mathbb{Z}_2$  parity, and their interactions with SM fields are realized via gauge-invariant effective operators of dimension-6. These include the contact quartic interactions between  $(X, X')$  and lepton pairs relevant to the current study. Depending on the type of the bilinear lepton fields in the quartic interaction, we may assign

both  $(X, X')$  as  $P$ -even real scalars or one of them as  $P$ -odd pseudo-scalar. In the latter case,  $(X, X')$  can combine to form a complex singlet scalar such as  $\widehat{X} = (X' + \mathrm{i}X) / \sqrt{2}$  (for  $X$  being  $P$ -odd) or  $\widehat{X} = (X + \mathrm{i}X') / \sqrt{2}$  (for  $X'$  being  $P$ -odd).

In the present study, we will consider the following inelastic scattering process of the DM with electrons,

$$
e ^ {-} + X ^ {\prime} \longleftrightarrow e ^ {-} + X. \tag {2.1}
$$

For the typical local DM velocity, it is known [15] that the recoil energy of an elastic scattering between the DM and electron is too low to explain the event excess in the electron recoil energy spectrum around (2-3)keV as newly observed by XENON1T [1]. Thus, we only consider the inelastic channel (2.1) for analyzing the xenon electron recoil detection. If a large proportion of the DM is made of  $X^{\prime}$ , then its exothermic inelastic scattering  $e^{-} + X^{\prime}\rightarrow e^{-} + X$  releases an amount of energy  $\sim \Delta m$  to the kinetic energy of the final states. In the case of  $m_{X},m_{X^{\prime}}\gg m_{e}$ , most of these released energy goes into the kinetic energy of the scattered electron and produces a narrow peak in the electron recoil energy  $E_{R}\sim \Delta m$ . The reverse process  $e^{-} + X\to e^{-} + X^{\prime}$  is kinematically suppressed because the local DM particles in average are too slow to overcome the energy barrier.

Related to the scattering process (2.1), we note that the heavier DM particle  $X'$  has the following decay channel induced by an electron-loop,

$$
X ^ {\prime} \rightarrow X + (\mathrm {p h o t o n s}). \tag {2.2}
$$

This is the dominant decay channel if  $X$  and  $X'$  do not couple directly to light neutrinos. The number of photons emitted in the decay products depends on details of the DM-electron interaction and the spin of the DM particles. This process is extremely suppressed kinematically because of the small mass-splitting  $\Delta m \ll m_X$ . The lifetime of  $X'$  can be much beyond the age of the Universe, as we will show later.

This inelastic DM sector can be realized consistently in the early Universe. The DM particles were originally in chemical equilibrium with electrons/positrons through the annihilation,

$$
e ^ {+} + e ^ {-} \longleftrightarrow X + X ^ {\prime}. \tag {2.3}
$$

As the Universe cools down, the above scattering became inefficient when  $T \lesssim m_X$  and the dark matter relic density  $n_{X} + n_{X^{\prime}}$  is determined by the usual freeze-out mechanism. But, the scattering process (2.1) and its counterpart with positron are still operative because of the large  $e^{\pm}$  abundance. These keep  $n_{X} = n_{X^{\prime}}$  for  $T \gg \Delta m$ . The process  $X^{\prime}X^{\prime} \leftrightarrow XX$  also maintains chemical equilibrium between  $X$  and  $X^{\prime}$ . But, it is mainly controlled by the quartic coupling  $X^{2}X^{\prime 2}$  and we assume it decouples earlier than DM scattering with  $e^{\pm}$ . The electron kinetically decouples from  $X$  and  $X^{\prime}$  at a temperature  $T_{D} \approx m_{e} \gg \Delta m$ . Since then the density ratio of  $X$  and  $X^{\prime}$  has been frozen as  $n_{X} = n_{X^{\prime}}$ . So only half of the DM particles ( $X^{\prime}$ ) can contribute to the event excess in the electron recoil energy spectrum observed by the XENON1T experiment.

In the following, we quantitatively compute the contribution of our inelastic DM to the electron recoil energy spectrum of XENON1T. We present an EFT formulation for the DM-lepton interactions by considering the parameter space with the mediator mass much larger than the energy scale of the DM-electron scattering and the lepton mass, i.e.,  $M_{\mathrm{md}}^2 \gg q_t^2$ ,  $m_{\ell}^2$  where  $M_{\mathrm{md}}$  denotes the mediator mass,  $m_{\ell}$  the lepton mass, and  $q_{t}$  the 4-momentum transfer between the DM and electron. In this case the DM-lepton interaction reduces to an effective contact operator. This is a reasonable EFT setup since the freeze-out of the DM density and

the DM-electron scattering in XENON1T detector both occur at energy scales much below  $O(\mathrm{GeV})$  which we will identify as the mass scale of our inelastic DM. We may also consider the case with the mediator mass above the electroweak symmetry breaking scale. Thus, integrating out the mediator field, we can write down the following effective Lagrangian for the DM-lepton interactions:

$$
\mathcal {L} _ {(6)} = \sum_ {j} \frac {c _ {j}}{\tilde {\Lambda} ^ {2}} \mathcal {O} _ {j} = \sum_ {j} \frac {\operatorname {s i g n} \left(c _ {j}\right)}{\Lambda_ {j} ^ {2}} \mathcal {O} _ {j}, \tag {2.4}
$$

where each dimensionless coefficient  $c_{j}$  is the product of mediator couplings with the DM and with the leptons and has possible signs  $\mathrm{sign}(c_{j}) = \pm$ . In the current notation,  $c_{j}$  can be defined as a real coupling before specifying the form of the corresponding operator  $\mathcal{O}_j$ . The UV cutoff scale  $\tilde{\Lambda}$  equals the mediator mass,  $\tilde{\Lambda} = M_{\mathrm{med}}$ , and we can define the corresponding effective UV cutoff scale  $\Lambda_{j} = \tilde{\Lambda} /|c_{j}|^{1 / 2}$  for each operator  $\mathcal{O}_j$ . In the effective Lagrangian (2.5), we have the following  $\mathrm{SU}(2)_L\otimes \mathrm{U}(1)_Y$  gauge-invariant and  $CP$ -conserving dimension-6 effective operators for the DM-lepton interactions,

$$
\mathcal {O} _ {S j} = (\bar {L} H \ell_ {R}) [ X ^ {\prime} X, X ^ {2}, X ^ {\prime 2} ] + \mathrm {h . c .}, \tag {2.5a}
$$

$$
\mathcal {O} _ {V L} = (\bar {L} \gamma^ {\mu} L) \left(X ^ {\prime} \partial_ {\mu} X - X \partial_ {\mu} X ^ {\prime}\right), \tag {2.5b}
$$

$$
\mathcal {O} _ {V R} = (\bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R}) (X ^ {\prime} \partial_ {\mu} X - X \partial_ {\mu} X ^ {\prime}), \tag {2.5c}
$$

where  $H$  denotes the SM Higgs doublet with its vacuum expectation value  $(\mathrm{VEV})\langle H\rangle = (0,v)^T$ ,  $L = (\nu_{L},\ell_{L})^{T}$  is the left-handed lepton-doublet, and  $\ell = e,\mu ,\tau .^2$  For the vector-type interactions (2.5b)-(2.5c), we assign one of the scalars  $(X,X^{\prime})$  as  $P$  -odd and the other one as  $P$  -even, so the operators  $\mathcal{O}_{VL}$  and  $\mathcal{O}_{VR}$  conserve  $CP$ . We consider the scalar-type interactions (2.5a) and the vector-type interactions (2.5b)-(2.5c) as motivated by two different types of the underlying UV theories, so we will take them as two independent effective model-setup for our present study and analyze them separately. In the broken phase, the scalar-type operators (2.5a) provide the following dimension-5 operators relevant to DM-lepton interactions,

$$
\mathcal {O} _ {S j} ^ {(5)} = v (\bar {\ell} \ell) X ^ {\prime} X, v (\bar {\ell} \ell) X ^ {2}, v (\bar {\ell} \ell) X ^ {\prime 2}. \tag {2.6}
$$

For the vector-type operators (2.5b)-(2.5c), we find that they give the same contributions to the DM scattering and annihilation amplitudes. We also note that for  $\mathcal{O}_{VL}$  and  $\mathcal{O}_{VR}$ , the asymmetric combination  $(X' \partial_{\mu} X - X \partial_{\mu} X')$  is unique because the vector-type operators with the other combination  $(X' \partial_{\mu} X + X \partial_{\mu} X') = \partial_{\mu}(XX')$  can be converted to terms suppressed by the leptonic Yukawa couplings of the SM, or, to terms with additional gauge fields which are irrelevant to the current study. Besides, in eqs. (2.5b)-(2.5c), we could consider the operators with their DM part replaced by the bilinear fields  $X \partial_{\mu} X (\propto \partial_{\mu} X^2)$  or  $X' \partial_{\mu} X' (\propto \partial_{\mu} X'^2)$ . But by the same reasoning, we can convert such operators to terms suppressed by the SM leptonic Yukawa couplings, or, to terms with additional gauge fields. Finally, we note that there is another dimension-6 operator involving  $\mathrm{U}(1)_Y$  gauge field strength  $B^{\mu \nu}$  and the DM fields,  $B^{\mu \nu} \partial_{\mu} X \partial_{\nu} X'$ . Again it can be converted to operators suppressed by the SM leptonic Yukawa couplings. The details of the proof are presented in appendix A. We will further discuss the possible UV completions of the above effective operators in section 4.

# 2.2 EFT analysis of inelastic DM for Xenon electron recoil

In this subsection, we use the generic effective DM-electron interactions (2.5)-(2.6) to analyze the electron recoil energy spectrum and compare it with the new measurement of XENON1T [2]. We will demonstrate that the effective interactions (2.5)-(2.6) can realize the inelastic DM scattering  $X^{\prime}e^{-}\rightarrow Xe^{-}$  and neatly explain the observed XENON1T anomaly.

For the current situation, we note that the DM masses  $(m_X, m_{X'})$ , their mass-splitting  $(\Delta m)$ , and the electron mass  $(m_e)$  should obey the relation  $\Delta m \ll m_e \ll m_X$ . In natural units, we have the local DM velocity  $v_{\mathrm{DM}} \sim 10^{-3}$  and typical atomic electron velocity  $v_e \sim \alpha \sim 10^{-2}$  where  $\alpha$  is the fine structure constant. So we have the velocity relation  $v_{\mathrm{DM}} \ll v_e \ll 1$ . Thus, for the inelastic scattering  $X' e^- \rightarrow X e^-$ , we can express the electron recoil energy to the leading order of  $(v_{\mathrm{DM}}, v_e)$  and  $(\Delta m, m_e)$ ,

$$
E _ {R} \simeq \Delta m \left(1 - \frac {v _ {\mathrm {D M}}}{v _ {e}} \cos \theta_ {e}\right), (2. 7)
$$

where  $\theta_{e}$  is the scattering angle between the moving directions of the final and initial state electrons. In deriving the above formula, we have chosen the initial state electron and  $X^{\prime}$  to move in parallel for simplicity of demonstration, but the following analysis does not rely on this choice. Because  $v_{\mathrm{DM}} \ll v_{e}$ , eq. (2.7) shows that the recoil energy spectrum has to exhibit a narrow peak around  $E_{R} \approx \Delta m$ , which will be further spread by detector resolution.

To analyze the electron recoil energy spectrum at XENON1T induced by the inelastic DM scattering, we use the systematic treatment of [59]-[62]. We parameterize the  $X^{\prime}e$  scattering cross section as  $\sigma_{Xe}(q) = \overline{\sigma}_e|F_X(q)|^2$ , where  $q\equiv |\vec{q} |$  is the size of transferred 3-momentum, and  $\overline{\sigma}_{e}\equiv \sigma_{Xe}(q = 0)$  is the scattering cross section evaluated at  $q = 0$ . The function  $F_{X}(q)$  is the DM form factor that captures the  $q$  dependence of the cross section. We consider the DM mass range  $m_{X}\gg m_{e}$ . For the inelastic scattering  $X^{\prime}e^{-}\rightarrow Xe^{-}$  induced by scalar-type contact interaction  $\mathcal{O}_{S1}^{(5)}$  in eq. (2.6), we derive

$$
\overline {{\sigma}} _ {e} ^ {S} = \frac {m _ {e} ^ {2} v ^ {2}}{4 \pi \Lambda_ {S} ^ {4} m _ {X} ^ {2}}, (2. 8 \mathrm {a})
$$

$$
| F _ {X} ^ {S} (q) | ^ {2} = \frac {m _ {e} ^ {2} + q ^ {2} / 4}{m _ {e} ^ {2}}, \tag {2.8b}
$$

where  $\Lambda_{S}$  is the effective cutoff scale associated with the operator  $\mathcal{O}_{S1}$  and  $\mathcal{O}_{S1}^{(5)}$ . For vector-type contact interaction  $\mathcal{O}_{VL}$  or  $\mathcal{O}_{VR}$  in eqs. (2.5b)-(2.5c), we denote the associated cutoff scale as  $\Lambda_{V}$  and deduce the following,

$$
\overline {{\sigma}} _ {e} ^ {V} = \frac {m _ {e} ^ {2}}{4 \pi \Lambda_ {V} ^ {4}}, (2. 9 \mathrm {a})
$$

$$
| F _ {X} ^ {V} (q) | ^ {2} = \frac {m _ {e} ^ {2} - q ^ {2} / 2}{m _ {e} ^ {2}}. (2. 9 \mathrm {b})
$$

Then, the velocity-averaged differential cross section is given by

$$
\frac {\mathrm {d} \langle \sigma_ {X e} v _ {\mathrm {D M}} \rangle}{\mathrm {d} E _ {R}} = \frac {\overline {{\sigma}} _ {e}}{2 m _ {e}} \int \mathrm {d} v _ {\mathrm {D M}} \frac {f (v _ {\mathrm {D M}})}{v _ {\mathrm {D M}}} \int_ {q _ {-}} ^ {q _ {+}} \mathrm {d} q a _ {0} ^ {2} q | F _ {X} (q) | ^ {2} K (E _ {R}, q), \tag {2.10}
$$

where  $f(v_{\mathrm{DM}})$  is the local DM velocity distribution function, normalized to  $\int \mathrm{d}v_{\mathrm{DM}}f(v_{\mathrm{DM}}) = 1$ . We take  $f(v_{\mathrm{DM}})$  as a pseudo-Maxwellian distribution,

$$
f (v) = N _ {0} v ^ {2} \exp \left[ - (v - v _ {\mathrm {m e a n}}) ^ {2} / (2 v _ {\mathrm {r m s}} ^ {2}) \right], \tag {2.11}
$$

where  $N_0$  is the normalization factor,  $v_{\mathrm{mean}}$  denotes the average velocity  $v_{\mathrm{mean}} = 0.77 \times 10^{-3}$ , and  $v_{\mathrm{rms}}$  is the local DM velocity dispersion  $v_{\mathrm{rms}} = 0.73 \times 10^{-3}$  [61]. In the above eq. (2.10),  $a_0 = 1 / (m_e\alpha)$  is the Bohr radius, while  $K(E,q)$  is the atomic excitation factor. We input  $K(E,q)$  from figure 7 of [62] with  $E_R = 2\mathrm{keV}$ . Most of our signal events have a recoil energy around  $E_R \sim \Delta m = (2 - 3)\mathrm{keV}$ . For  $E_R = (1 - 5)\mathrm{keV}$ , the scattering happens dominantly with electrons in the 3s shell [60]. The function  $K(E,q)$  is independent of  $E$  before it reaches the threshold of the next quantum energy level. So we can approximate  $K(E,q) \simeq K(\Delta m,q) \simeq K(2\mathrm{keV},q)$  for the calculation. The upper and lower limits of the  $q$  integration ( $q_{-} \leqslant q \leqslant q_{+}$ ) is determined by the range which obeys the energy-momentum conservation,

$$
q ^ {2} - 2 q m _ {X} v _ {\mathrm {D M}} \cos \eta + 2 m _ {X} (E _ {R} - \Delta m) = 0, \tag {2.12}
$$

for any  $\eta$ , where  $\eta$  is the angle between the momentum-transfer  $\vec{q}$  and the momentum  $\vec{p}_i$  of the incident DM particle  $X'$ . Thus, we have

$$
\frac {q _ {\pm}}{m _ {X}} = \left| v _ {i} \pm \sqrt {v _ {i} ^ {2} - 2 \left(\frac {E _ {R} - \Delta m}{m _ {X}}\right)} \right|. (2. 1 3)
$$

The electron recoil energy spectrum of the scattering events is given by

$$
\frac {\mathrm {d} N}{\mathrm {d} E _ {R}} \simeq \frac {\mathrm {d} \langle \sigma_ {X e} v _ {\mathrm {D M}} \rangle}{\mathrm {d} E _ {R}} \frac {\rho_ {\mathrm {D M}}}{2 m _ {X ^ {\prime}}} N _ {T} \Delta t, \tag {2.14}
$$

where the product  $N_{T}\Delta t\simeq 4.2\times 10^{27} / \mathrm{ton}\times 0.65\mathrm{ton}\cdot \mathrm{yr}$ , which gives the number of atoms  $N_{T}$  times the total exposure time  $\Delta t$  for the Science Run-1 (SR1) [2]. The local DM density is  $\rho_{\mathrm{DM}}\simeq 0.3\mathrm{GeV / cm}^3$ . We have used the condition that the heavier component  $X^{\prime}$  makes up half of the dark matter relics. We further incorporate the detector energy resolution  $\sigma_{d} = 0.5\mathrm{keV}$  [1] into the recoil spectrum by convolving it with a normal distribution  $G(E,\sigma_d)$ . The efficiency function  $\eta (E)$  of the XENON1T detector is given by figure 2 of ref. [2]. Thus, we estimate the detected recoil energy spectrum as follows,

$$
\frac {\mathrm {d} N _ {\mathrm {D T}}}{\mathrm {d} E _ {R}} = \eta (E _ {R}) \int \mathrm {d} E ^ {\prime} G (E _ {R} - E ^ {\prime}, \sigma_ {d}) \frac {\mathrm {d} N (E ^ {\prime})}{\mathrm {d} E ^ {\prime}}. \tag {2.15}
$$

In the above formulation, we have three key quantities for describing the DM-electron inelastic scattering: the DM mass  $m_{X}$ , the DM mass-splitting  $\Delta m$ , and the inelastic scattering cross section at  $q^{2} = 0$ , which is  $\sigma_{Xe}(q^{2} = 0) = \overline{\sigma}_{e}$ . From eqs. (2.8)-(2.9), we see that in the expression of the inelastic cross section  $\sigma_{Xe}$ , the part  $\overline{\sigma}_{e}$  contains all the information of the DM-electron interactions, especially the effective DM-electron coupling  $\Lambda_S^{-1}$  or  $\Lambda_V^{-1}$  as defined in the dimension-6 effective operators (2.4)-(2.6). Also, the kinematic function  $F_{X}^{S}(q)$  or  $F_{X}^{V}(q)$  just extracts the  $q^{2}$ -dependence of the inelastic cross section  $\sigma_{Xe}$ , and practically  $F_{X}^{S,V}(q) \simeq 1$  holds well for the relevant region of the  $q$ -integration (2.10). This is because the atomic excitation function  $K(E,q)$  takes its peak value at  $q \approx 0.04\mathrm{MeV} \ll m_e$  and falls off rapidly as  $q$  deviates from this peak position. Hence, we can make a fairly model-independent fit of the inelastic DM parameters ( $m_X, \Delta m, \overline{\sigma}_e$ ) with the XENON1T data.

With these, we present our fitting results in figure 1. Plot-(b) shows the  $\chi^2$  fit for  $\Delta m$ , which gives the best fit of the DM mass-splitting  $\Delta m = 2.8\mathrm{keV}$ , and the allowed ranges:  $\Delta m = 2.8_{-0.3}^{+0.2}\mathrm{keV}$  (68% C.L.) and  $2.1\mathrm{keV} < \Delta m < 3.3\mathrm{keV}$  (95% C.L.). In Plot-(a), we present the allowed parameter space in the  $m_X - \overline{\sigma}_e$  plane by fixing the DM mass-splitting to

![](images/77c4ccbf72deeefd098195a8a0d136b173129d42aaed89f76aa061b78b4fa6b7.jpg)  
Figure 1. Fitting inelastic DM with XENON1T data. The fit is performed by varying the parameters  $(m_X, \Delta m, \overline{\sigma}_e)$  simultaneously. Plot-(a) presents the allowed parameter space in the  $m_X - \overline{\sigma}_e$  plane for setting the DM mass-splitting to its best fit  $\Delta m = 2.8\mathrm{keV}$ , where the red and pink contours give the  $68\%$  C.L. and  $95\%$  C.L. limits, respectively. The black solid curve in the middle of the contours correspond to the best fit of  $(m_X, \overline{\sigma}_e)$ . Plot-(b) shows the  $\chi^2$  fit for  $\Delta m$ , which gives the best fit of  $\Delta m = 2.8\mathrm{keV}$ , and the allowed ranges of  $\Delta m = 2.8_{-0.3}^{+0.2}\mathrm{keV}$  ( $68\%$  C.L.) and  $2.1\mathrm{keV} < \Delta m < 3.3\mathrm{keV}$  ( $95\%$  C.L.).

![](images/a58e66527d1e37b064a73251569a41806f7deacd883b0ce3e3514298249c89b7.jpg)

its best fit  $\Delta m = 2.8\mathrm{keV}$ , where the red and pink contours correspond to the  $68\%$  C.L. and  $95\%$  C.L. limits, respectively. The black solid curve in the middle of the contours corresponds to the best fit of  $(m_X,\overline{\sigma}_e)$ . As we will show, given the general contour of  $(m_X,\overline{\sigma}_e)$  in figure 1(a), we can further derive new bounds on the cutoff scale  $\Lambda$  versus the DM mass  $m_{X}$  for each given type of contact DM-electron interactions.

Inspecting eqs. (2.10) and (2.14), we observe that the information of the DM dynamics enters the recoil spectrum via the ratio  $\overline{\sigma}_e / m_{X'}$  (or equivalently,  $\overline{\sigma}_e / m_X$ ) for a given DM mass-splitting  $\Delta m$ . The integral upper/lower limits  $q_{\pm}$  [cf. eq. (2.13)] also have dependence on  $m_X$ , but we find that this effect is rather weak and practically negligible for the final result. In figure 2, we present the smeared electron recoil energy spectrum for the sample input of cross-section/mass ratio  $\overline{\sigma}_e / m_X = 8.8 \times 10^{-44} \mathrm{~cm}^2/\mathrm{GeV}$ , which corresponds to the best fit of figure 1(a). As will be shown below, this input satisfies the constraint of the DM relic abundance. The data points with error bars correspond to the new measurement by the XENON1T collaboration and the black solid curve shows the background contribution in the XENON1T detector, which are taken from ref. [2].

With our generic EFT formulation of the inelastic DM, we have computed the electron recoil energy spectrum for different DM mass-splittings  $\Delta m = (2.5, 2.8, 3.0)\mathrm{keV}$ , which are plotted as (blue, red, green) dashed curves in figure 2. We sum these DM signal contributions with the backgrounds (black solid curve) respectively, and plot them as the (green, red, blue) solid curves in the same figure. It shows that the case of  $\Delta m = 2.8\mathrm{keV}$  (red solid curve) gives the best fit to the recoil spectrum measured by XENON1T. Also, comparing the (blue, red, green) solid curves with different  $\Delta m$  values, we see that varying the  $\Delta m$  value has little effect on the height and width of the recoil peak, but it does shifts the peak position in  $E_{R}$ . We see that even after including the detector energy resolution the recoil peak still reamins quite narrow, so the peak position in  $E_{R}$  is fairly constrained by the XENON1T data.

![](images/98da9e3f6b73be293732c56a65dd58e9a9d0a80def378cff1d2f5ea9b14c59e6.jpg)  
Figure 2. Prediction of inelastic DM for the electron recoil energy spectrum and the XENON1T data. The data points with error bars correspond to the new measurement of XENON1T [2], and the black solid curve shows the background contribution. The (green, red, blue) solid curves include the inelastic DM contributions with the DM mass-splitting  $\Delta m = (2.5, 2.8, 3.0)\mathrm{keV}$ , respectively, while the dashed (green, red, blue) curves correspond to the inelastic DM contributions alone. We have input a sample cross-section/mass ratio  $\overline{\sigma}_e / m_X = 8.8\times 10^{-44}\mathrm{cm}^2 /\mathrm{GeV}$ , which corresponds to the best fit of figure 1(a).

Next, we can apply the general fit of figure 1(a) to the case of the scalar-type DM-electron interaction (2.6) and to the case of the vector-type DM-electron (2.5b)-(2.5c), respectively. With the fit of figure 1(a), we can derive the allowed parameter space in the  $m_X - \Lambda_S$  plane for the scalar-type DM-electron interaction, and in the  $m_X - \Lambda_V$  plane for the vector-type DM-electron interaction. This is practically equivalent to making a direct fit of XENON1T data (under  $\Delta m = 2.8\mathrm{keV}$ ) in the  $m_X - \Lambda_S$  plane and in the  $m_X - \Lambda_V$  plane, respectively.

We present our findings in figure 3. In plot-(a), we fit with the XENON1T data and show the allowed parameter region in the  $m_{X} - \Lambda_{S}$  plane for the case of scalar-type DM-electron interaction under  $\Delta m = 2.8\mathrm{keV}$ . The black curve represents the best fit value, and the red and pink bands give the allowed parameter space at  $68\%$  C.L. and  $95\%$  C.L., respectively. This parameter region is largely independent of the DM mass-splitting  $\Delta m$ , as indicated by figure 2 which shows the recoil spectrum for different  $\Delta m$  values under the same input ratio of  $\overline{\sigma}_{e} / m_{X}$ . In parallel, we further present in plot-(b) the allowed parameter region in the  $m_{X} - \Lambda_{V}$  plane for the case of vector-type DM-electron interaction under  $\Delta m = 2.8\mathrm{keV}$ . The  $68\%$  and  $95\%$  confidence limits of the XENON1T data on the parameter space are marked by the red and pink colors, respectively. In figure 3, we also presented the constraints from the CMB measurements on the DM relic density as the blue and green curves which we will derive and discuss in the next section.

Finally, for the convenience of analysis, we present a compact formula for computing the total number of DM signal events in the XENON1T experiment. We define the following

![](images/cdf5b3362942723ce1f3cc4d7d77d451c94ea910195771ce6d5f563df92c11c9.jpg)  
Figure 3. Bounds of XENON1T data on the parameter space  $m_X - \Lambda$  of inelastic DM. Plot-(a) presents the bounds in the  $m_X - \Lambda_S$  plane (under  $\Delta m = 2.8\mathrm{keV}$ ) for the scalar-type DM-electron interaction at the 68% C.L. (red region) and 95% C.L. (pink region). Plot-(a) depicts the bounds in the  $m_X - \Lambda_S$  plane (with  $\Delta m = 2.8\mathrm{keV}$ ) for the vector-type DM-electron interaction at 68% C.L. (red region) and 95% C.L. (pink region). In each plot, the constraints by the CMB measurements of the DM relic density are also shown as blue and green curves, which are discussed in section 3.

![](images/fcbafd5d2f4382c257d52e2b40cbd2946074c1e9d7a68be4a6853fbcc134e8c9.jpg)

ratio which is mainly independent of the model-parameters  $(\Delta m, m_X, \Lambda)$ ,

$$
\xi \equiv \int \mathrm {d} E _ {R} \eta (E _ {R}) \frac {1}{\bar {\sigma} _ {e}} \frac {\mathrm {d} \langle \sigma_ {X e} v _ {\mathrm {D M}} \rangle}{\mathrm {d} E _ {R}}, \tag {2.16}
$$

where  $\eta (E)$  is the detector efficiency function. The only dependence of  $\xi$  on  $(\Delta m, m_X)$  comes from the upper/ lower limits  $q_{\pm}$  of the integration (2.10). We have shown in figure 2 that varying  $\Delta m$  will mainly shift the position of the recoil energy peak, but has little effect on the height of the spectrum. We have also checked numerically that the ratio  $\xi$  only changes by about  $4\%$  when the DM mass  $m_X$  varies within (0.1-10) GeV and the mass-splitting varies within  $\Delta m = (2 - 3)\mathrm{keV}$ . As a benchmark point, we obtain  $\xi_0 = 1.62$  for  $\Delta m = 2.8\mathrm{keV}$  and  $m_X = 1\mathrm{GeV}$ . Then, we derive the total number of excess events beyond the backgrounds,

$$
\begin{array}{l} N _ {\mathrm {t o t}} \simeq \xi_ {0} \bar {\sigma} _ {e} \frac {\rho_ {\mathrm {D M}}}{2 m _ {X}} N _ {T} \Delta t \\ \simeq 5 0 \times \frac {\bar {\sigma} _ {e}}{8 \times 1 0 ^ {- 4 4} \mathrm {c m} ^ {2}} \frac {\rho_ {\mathrm {D M}}}{0 . 3 \mathrm {G e V / c m} ^ {3}} \frac {\mathrm {G e V}}{m _ {X}} \frac {N _ {T}}{4 . 2 \times 1 0 ^ {2 7} / \mathrm {t o n}} \frac {\Delta t}{0 . 6 5 \mathrm {t o n y r}}. (2. 1 7) \\ \end{array}
$$

# 3 Constraints from DM relic abundance and decays

In this section, we compute the relic abundance for the inelastic DM and analyze the constraints on the DM parameter space by following the conventional DM freeze-out mechanism [63, 64]. We also derive constraint on the DM self-interactions. Then, we show that the lifetime of the heavier DM component  $X'$  can be much longer than the age of the Universe.

With the DM-lepton contact interactions, we can compute the DM annihilation cross sections of  $XX^{\prime},X^{\prime}X^{\prime},XX\to \ell^{+}\ell^{-}$  with  $\ell = e,\mu ,\tau$  for the scalar-type contact interactions (2.6) and the vector-type contact interactions (2.5b)-(2.5c). For instance, the

scalar-type operator  $\mathcal{O}_S$  contributes to the annihilation cross section of  $XX^{\prime}\rightarrow \ell^{+}\ell^{-}$  for  $m_{X},m_{\ell}\gg \Delta m$

$$
\sigma_ {\mathrm {a n n}} ^ {S} \simeq \frac {v ^ {2}}{8 \pi \Lambda_ {S} ^ {4}} \sqrt {\frac {s}{s - 4 m _ {X} ^ {2}}} \left(1 - \frac {4 m _ {\ell} ^ {2}}{s}\right) ^ {3 / 2}, (3. 1)
$$

while the vector-type operator  $\mathcal{O}_{VL}$  or  $\mathcal{O}_{VR}$  contributes to the annihilation cross section,

$$
\sigma_ {\mathrm {a n n}} ^ {V} \simeq \frac {s - m _ {\ell} ^ {2}}{2 4 \pi \Lambda_ {V} ^ {4}} \sqrt {\left(1 - \frac {4 m _ {\ell} ^ {2}}{s}\right) \left(1 - \frac {4 m _ {X} ^ {2}}{s}\right)}. (3. 2)
$$

The same formulas also hold for other initial states  $XX$  and  $X^{\prime}X^{\prime}$ . But for the vector-type operators (2.5b)-(2.5c), the initial state contains  $XX^{\prime}$  only. Similar type of annihilation processes were considered in the literature [65]. Then, we further derive the thermal averaged annihilation cross section of  $XX^{\prime} \rightarrow \ell^{+}\ell^{-}$  at the freeze-out temperature  $T_{f}$ ,

$$
\langle \sigma_ {\mathrm {a n n}} ^ {S} v _ {\mathrm {D M 0}} \rangle \simeq \frac {v ^ {2}}{4 \pi \Lambda_ {S} ^ {4}} \left(1 - \frac {m _ {\ell} ^ {2}}{m _ {X} ^ {2}}\right) ^ {3 / 2}, (3. 3 \mathrm {a})
$$

$$
\langle \sigma_ {\mathrm {a n n}} ^ {V} v _ {\mathrm {D M 0}} \rangle \simeq \frac {m _ {X} ^ {2}}{2 \pi x _ {f} \Lambda_ {V} ^ {4}} \sqrt {1 - \frac {m _ {\ell} ^ {2}}{m _ {X} ^ {2}}} \left(1 - \frac {m _ {\ell} ^ {2}}{4 m _ {X} ^ {2}}\right), (3. 3 \mathrm {b})
$$

where  $v_{\mathrm{DM0}}$  is the DM velocity around the freeze-out epoch and  $x_{f} = m_{X} / T_{f} \simeq 18$ . In the above formulas we only keep the lowest order of  $x_{f}^{-1}$ . For computing the DM relic density, we have determined the freeze-out temperature and  $x_{f}$  numerically. Following the analysis of the conventional freeze-out mechanism, we parameterize  $\sigma_{\mathrm{ann}} v_{\mathrm{DM0}} \simeq a_{0} + a_{1} x_{f}^{-1}$ , then the total relic density of  $X$  and  $X'$  is given by

$$
\Omega_ {\mathrm {D M}} h ^ {2} \simeq 2. 1 \times 1 0 ^ {9} \mathrm {G e V} ^ {- 1} \left(\frac {T _ {0}}{2 . 7 2 5 \mathrm {K}}\right) ^ {3} \frac {x _ {f}}{M _ {\mathrm {P l}} \sqrt {g _ {*} (T _ {f})} \left(a _ {0} + a _ {1} x _ {f} ^ {- 1} / 2\right)}, \tag {3.4}
$$

where  $M_{\mathrm{Pl}}$  denotes the reduced Planck mass and  $T_{f}$  is the freeze-out temperature. We will determine  $T_{f}$  and  $x_{f}$  numerically. The temperature  $T_{0} \simeq 2.725\mathrm{K}$  is the current CMB temperature [66] and  $g_{*}(T_{f})$  is the effective degrees of freedom at the DM freeze-out.

Using the CMB measurement of the current DM relic density  $\Omega_{\mathrm{DM}}h^{2} = 0.120\pm 0.001$  [75], we can derive strong constraints on the cutoff scales  $\Lambda_S$  and  $\Lambda_V$  for the scalar-type and vector-type DM interactions. We present the bounds on  $\Lambda_S$  in figure 3(a) and the bounds on  $\Lambda_V$  in figure 3(b), where in each plot the blue curve depicts the bound from the annihilation channel  $XX^{\prime}\rightarrow e^{+}e^{-}$  and the green curve corresponds to the bound from all relevant annihilation channels including the initial states  $(XX^{\prime},X^{\prime}X^{\prime},XX)$  and the final states  $(e^{+}e^{-},\mu^{+}\mu^{-},\tau^{+}\tau^{-})$ . Note that for vector-type contact interaction,  $XX^{\prime}$  is the only possible initial state. To derive the green curve in each plot, we have chosen a common cutoff scale for all the relevant operators in eq. (2.6) or eqs. (2.5b)(2.5c). Figure 3 shows that combining the DM relic density bound with the bound by fitting the XENON1T anomaly, we can constrain the DM parameter space  $(m_X,\Lambda)$  into rather narrow regions. For the case of scalar-type contact interactions, the relic density bounds in figure 3(a) are fairly flat, so the cutoff scale  $\Lambda_S$  is almost fully fixed. In summary, we obtain the following bounds on the

DM mass and the cutoff scale of the effective DM contact interactions,

Scalar-type:  $(m_X, \Lambda_S) = (1.22\mathrm{GeV}, 1.11\mathrm{TeV})$ , (Best Fit);

$$
(1.02 \mathrm{GeV}, 1.110 \mathrm{TeV}) <   (m_{X}, \Lambda_{S}) <   (1.90 \mathrm{GeV}, 1.113 \mathrm{TeV}), \quad (95 \% \mathrm{C.L.}); \tag{3.5}
$$

Vector-type:  $(m_X,\Lambda_V) = (2.95\mathrm{GeV},74.8\mathrm{GeV})$  , (Best Fit);

$$
(2.48 \mathrm{GeV}, 68.2 \mathrm{GeV}) <   (m_{X},\Lambda_{V}) <   (4.51 \mathrm{GeV},92.9 \mathrm{GeV}), \quad (95 \% \mathrm{C.L.}). \tag{3.6}
$$

It shows that the bound on the vector-type cutoff scale  $\Lambda_V$  is much lower than the bound on the scalar-type cutoff scale  $\Lambda_S$ . The reason is because the vector-type cross sections are much smaller than that of the scalar-type due to the relative suppression factor  $m_X^2 / v^2 = O(10^{-4})$  as shown in eqs. (2.8)-(2.9) and eqs. (3.3a)-(3.3b), where  $v \simeq 174\mathrm{GeV}$  is the Higgs VEV. We also note that the cutoff scale  $\Lambda$  in the effective operator is connected to the heavy mediator mass  $M_{\mathrm{md}}$  via  $\Lambda = M_{\mathrm{md}} / \sqrt{\tilde{g}_X\tilde{g}_\ell}$ , where  $\tilde{g}_X$  denotes the mediator coupling to the DM and  $\tilde{g}_\ell$  the mediator coupling to the leptons. Thus, we can deduce  $\Lambda \gg M_{\mathrm{md}}$  (when  $\tilde{g}_X\tilde{g}_\ell \ll 1$ ), or,  $\Lambda \lesssim M_{\mathrm{md}}$  (when  $\tilde{g}_X\tilde{g}_\ell \gtrsim 1$ ).

The DM mass ranges in eqs. (3.5)-(3.6) are small enough, so the DM particles can be produced at the  $e^{+}e^{-}$  colliders [68-71]. In the following, we summarize the current constraints by the LEP and BaBar experiments from [68, 70].<sup>3</sup> Note that the validity of the EFT requires  $M_{\mathrm{md}}^2 \gg (2m_X)^2$ . Thus, for the simplicity of discussion, we consider the case where the mediator mass is heavier than  $10\mathrm{GeV}$ , which is also about the center of mass energy of BaBar experiment. For the scalar-type operator  $\mathcal{O}_S$ , eq. (3.5) gives a sizable cutoff scale  $\Lambda_S \simeq 1.1\mathrm{TeV}$ , which is much above the current collider search limits of a few hundred GeV [68, 70]. The mediator in the UV completed model could receive additional constraints, as we will discuss in sections 4.1-4.2. On the other hand, for the vector-type operator  $\mathcal{O}_V$ , eq. (3.6) gives a quite low cutoff scale  $\Lambda_V \simeq (68 - 93)\mathrm{GeV}$ . In the case of  $\tilde{g}_X\tilde{g}_\ell \ll 1$ , we have  $M_{\mathrm{md}} \ll \Lambda_V$  and thus the mediator can be produced on-shell at the LEP. The mediator contributes constructively to the cross section of the lepton-pair production process  $e^{+}e^{-} \rightarrow \ell^{+}\ell^{-}$ . This places a constraint  $\sqrt{4\pi s} / \tilde{g}_\ell > 13.2\mathrm{TeV}$  ( $95\%$  C.L.)<sup>4</sup> for the mediator having universal coupling to all the leptons, or,  $\sqrt{4\pi s} / \tilde{g}_\ell > 8.6\mathrm{TeV}$  for the mediator having coupling to electrons only [67], where  $\sqrt{s} \simeq 200\mathrm{GeV}$  is the LEP collider energy. This corresponds to  $\tilde{g}_\ell \lesssim 0.054$  (0.082) for the case of universal coupling (electron coupling only), and in turn it imposes  $\tilde{g}_X^2 \gg \tilde{g}_\ell^2$  for the low cut-off scale required by eq. (3.6) and  $M_{\mathrm{md}} \gtrsim 10\mathrm{GeV}$ . In this case, the mediator decays predominantly into the DM particles<sup>5</sup> and is constrained by the mono-photon searches at LEP-2. Since the width of the mediator scales as  $\Gamma_{\mathrm{md}} \propto \tilde{g}_X^2 M_{\mathrm{md}}$  and the mono-photon cross section scales as  $\sigma \propto \tilde{g}_\ell^2 \tilde{g}_X^2 M_{\mathrm{md}} / (\Gamma_{\mathrm{md}} s) \propto \tilde{g}_\ell^2 / s$  for  $s \gg M_{\mathrm{md}}^2$ , the mono-photon searches only constrain  $\tilde{g}_\ell$  and is independent of  $M_{\mathrm{md}}$  in the mass range of interest. Ref. [70] extracted such a bound from the result of ref. [68] and sets  $\tilde{g}_\ell \lesssim 0.023$ , or in terms of the cutoff scale, we can derive

$$
\Lambda_ {V} \gtrsim 5 2 \mathrm {G e V} \times \left(\frac {\sqrt {4 \pi}}{\tilde {g} _ {X}}\right) ^ {\frac {1}{2}} \left(\frac {M _ {\mathrm {m d}}}{1 5 \mathrm {G e V}}\right), \tag {3.7}
$$

which is consistent with our bound (3.6) within limited parameter space. On the other hand, the constraint on the off-shell vector mediator by the Bar measurement sets a bound

$\Lambda_V \gtrsim 30\mathrm{GeV}$  [70] for  $m_X \lesssim 3\mathrm{GeV}$ . The constraint becomes weaker for heavier DM due to the limited center of mass energy. As the next generation B-factory, the upcoming Belle-II experiment [72] is expected to further probe a much larger  $\Lambda_V$ . For the ideal case where the systematic errors are negligible, the Belle-II measurement can probe up to  $\Lambda_V \simeq 92\mathrm{GeV}$  [70], and thus it could help to either confirm or rule out our EFT formulation of the vector-type inelastic DM as a viable resolution to the XENON1T anomaly.

After the annihilation processes  $XX^{\prime},X^{\prime}X^{\prime},XX\to \ell^{+}\ell^{-}$  decouple, the total number of the DM particles  $X$  and  $X^{\prime}$  is fixed. But, the conversion between  $X$  and  $X^{\prime}$  is still efficient due to the scattering process  $e^{\pm}X^{\prime}\leftrightarrow e^{\pm}X$ . We may estimate the kinetic decoupling temperature of this process. We note that for  $T\lesssim m_e$ , the scattering cross sections  $\bar{\sigma}_e^S$  and  $\bar{\sigma}_e^V$  are already given by eqs. (2.8)-(2.9). Thus, this decoupling happens when the following condition is realized,

$$
\bar {\sigma} _ {e} ^ {S, V} n _ {e \pm} \simeq H, \tag {3.8}
$$

where  $n_{e^{\pm}} \simeq 4\zeta(3)T^{3}/\pi^{2}$  is the number density of  $e^{\pm}$ , and  $H \simeq \sqrt{\frac{g_{*}\pi^{2}}{90}\frac{T^{2}}{M_{\mathrm{Pl}}}}$  is the Hubble rate. For the parameter space of  $(m_X, \Lambda_S)$  or  $(m_X, \Lambda_V)$  which realizes both the observed DM relic density and XENON1T signal excess, we find that this conversion process freezes out at a temperature  $T \simeq 0.7\mathrm{MeV} \gg \Delta m$ , very close to the temperature when the  $e^{\pm}$  density gets depleted.

We note that the quartic interactions of the scalar DM contain a term  $\tilde{\lambda} X^2 X'^2$  which induces the annihilation process  $X'X' \leftrightarrow XX$ . This converts the two types of DM particles into each other and gives the following annihilation cross section,

$$
\sigma \left[ X ^ {\prime} X ^ {\prime} X X \right] \simeq \frac {\tilde {\lambda} ^ {2}}{6 4 \pi m _ {X} ^ {2}}. \tag {3.9}
$$

After  $e^{\pm}$  decouple from the dark sector, the temperature of the dark matter drops quickly as  $a(t)^{-2}$ , with  $a(t)$  being the expansion scale factor of the Universe. The DM temperature then falls below keV in a very short time and an active annihilation  $X'X' \rightarrow XX$  would deplete the  $X'$  density. Since the quartic scalar self-interaction  $\tilde{\lambda} X^{2}X'^{2}$  is generally independent of the DM-electron interactions, we may properly set the scalar coupling  $\tilde{\lambda}$  such that the annihilation  $X'X' \rightarrow XX$  freezes out before the electrons decouple. The decoupling is realized by the condition

$$
\sigma \left[ X ^ {\prime} X ^ {\prime} X X \right] \times v _ {\mathrm {D M} _ {0}} n _ {\mathrm {D M}} \simeq H, \tag {3.10}
$$

where the DM has kinetic energy  $\frac{1}{2} m_X v_{\mathrm{DM}_0}^2 \approx \frac{3}{2} T$ . For the temperature  $T \ll m_X$ , we have  $n_{\mathrm{DM}} \approx \frac{\pi^2}{15} \frac{\Omega_{\mathrm{DM}}}{\Omega_{\mathrm{M}}} \frac{T_{\mathrm{eq}}}{m_X} T^3$ , where  $T_{\mathrm{eq}}$  is the temperature at the matter-radiation equality; and  $\Omega_{\mathrm{DM}}$  and  $\Omega_{\mathrm{M}}$  are the normalized present-day DM density and total matter density, respectively. By requiring the annihilation  $X'X' \rightarrow XX$  to freeze out before  $T \approx 1 \mathrm{MeV}$  we deduce an upper bound on the DM self-coupling  $\tilde{\lambda} \lesssim 0.03$ . After  $e^{\pm}$  decouple, the ratio between the particle number densities of  $X$  and  $X'$  is frozen as  $n_X = n_{X'} = \frac{1}{2} n_{\mathrm{DM}}$ , consistent with the setup throughout our formulation.

Next, we further estimate the lifetime of the heavier dark matter component  $X'$ . There are two possible decay channels,  $X' \rightarrow X\gamma\gamma$  and  $X' \rightarrow X\nu\bar{\nu}$ . The decay rate is generally suppressed by the small DM mass-splitting  $\Delta m$  which determines the energy scales of outgoing photons or neutrinos. If  $X$  and  $X'$  couple to electrons through the contact interaction  $\mathcal{O}_S$  or  $\mathcal{O}_{VR}$ , then  $X'$  decays dominantly into two photons  $X' \rightarrow X\gamma\gamma$  through one-loop diagram

with electron in the loop. If  $X$  and  $X'$  couple to electrons through the contact interaction  $\mathcal{O}_{VL}$  instead, then  $X'$  will decay dominantly via invisible channels  $X' \to X\nu \bar{\nu}$  at tree level.

For the scalar-type interaction  $\mathcal{O}_S$ , we compute the one-loop diagram for  $X' \to X\gamma \gamma$  and obtain the decay width:

$$
\Gamma_ {X ^ {\prime}} ^ {S} \simeq \frac {\alpha^ {2}}{7 5 6 0 \pi^ {5}} \frac {\Delta m ^ {7} v ^ {2}}{m _ {e} ^ {2} m _ {X} ^ {2} \Lambda_ {S} ^ {4}}. (3. 1 1)
$$

Here the electron triangle-loop has some similarity with the SM Higgs decay into di-photon  $(h\rightarrow \gamma \gamma)$  via fermion triangle-loop [76, 77]. Taking the sample inputs of  $m_{X}\approx 1$  GeV and  $\Lambda_S\approx 1$  TeV for satisfying the constraints by the DM relic density and the XENON1T measurement, we find the  $X^{\prime}$  lifetime as  $\tau_{X^{\prime}} = O(10^{18})\mathrm{yr}$ , which is 8 orders of magnitude longer than the age of the present Universe ( $\sim 10^{10}\mathrm{yr}$ ). So it is far beyond any current constraints for the decaying dark matter. Besides, we note that for the scalar-type interaction  $\mathcal{O}_S$ , the invisible decay channel  $X^{\prime}\rightarrow X\nu \bar{\nu}$  could occur via one-loop  $W$ -exchange triangle-loop. But its decay width is expected to be highly suppressed by extra factors of  $(m_{\nu}^{2}m_{e}^{2}) / M_{W}^{4}$  due to chirality-flips and thus fully negligible.

For the vector-type interaction  $\mathcal{O}_{VR}$ , we compute its contribution to the decay width of  $X' \rightarrow X\gamma\gamma$ , and obtain to the leading order of  $\Delta m$ ,

$$
\Gamma_ {X ^ {\prime}} ^ {V R} \simeq \frac {\alpha^ {2}}{7 5 6 0 \pi^ {5}} \frac {\Delta m ^ {9}}{m _ {e} ^ {4} \Lambda_ {V} ^ {4}}. (3. 1 2)
$$

This loop result is consistent with that of [78] when comparable. From the above formula, we deduce the  $X'$  lifetime  $\tau_{X'}^{VR} = O(10^{23})$  yr for  $\Lambda_V \sim 100\mathrm{GeV}$ . This is again far beyond the age of the Universe. For the vector-type interaction  $\mathcal{O}_{VR}$ , we may further consider the invisible decay channel  $X' \rightarrow X\nu \bar{\nu}$  via  $W$ -exchange triangle-loop. But we find that the  $X'$  decay width is highly suppressed by an extra chirality-flip factor of  $m_e^4 / M_W^4$ , so it is fully negligible.

Then, for the vector-type interaction  $\mathcal{O}_{VL}$ , we see that  $X^{\prime}$  will decay predominantly via the invisible channel  $X^{\prime} \to X\nu \bar{\nu}$  at tree level. We can derive its decay rate,

$$
\Gamma_ {X ^ {\prime}} ^ {V L} = \frac {1}{1 2 0 \pi^ {3}} \frac {\Delta m ^ {5}}{\Lambda_ {V L} ^ {4}}. (3. 1 3)
$$

By requiring the  $X^{\prime}$  decay lifetime larger than the age of the present Universe (about  $1.38 \times 10^{10} \mathrm{yr}$ ) and inputting the fitted range of DM mass-splitting  $2.1 \mathrm{keV} < \Delta m < 3.3 \mathrm{keV}$  ( $95\%$  C.L.) from figure 1(b), we derive the lower bound on the cutoff scale  $\Lambda_V > (291 - 512) \mathrm{GeV}$ . Comparing this with the allowed range given in figure 3(b), we find that this is excluded by both the DM relic density measurement and the current XENON1T data. Hence, the vector-type interaction  $\mathcal{O}_{VL}$  cannot provide a viable inelastic DM resolution.

Finally, we note that the effective DM-electron interactions can also induce new decay channels of the SM gauge bosons  $W / Z$  and the Higgs boson  $h^0$  with  $X$  and  $X'$  in the decay products. But, such decays are realized by either attaching the effective DM-electron quartic vertex to an electron loop or to an out-going electron line in the Feynman diagram. In both cases, the corresponding decay width and branching fraction are suppressed by an extra factor of  $(1 / 16\pi^2)^2 \lesssim 10^{-4}$ , either from the loop factor or from the phase space of two additional DM particles in the final state. Hence such effects are far below the current experimental sensitivity [79].

# 4 UV completion for effective DM-lepton interactions

In this section, we study possible UV completions for the effective DM-lepton interactions  $\mathcal{O}_S$  and  $\mathcal{O}_{VR}$  as illustration. In the first model, the effective DM-lepton interactions are mediated by an extra heavy Higgs doublet. In the second model, the interactions are mediated by extra vector-like heavy leptons. In the third model, the interactions are mediated by a new gauge boson that couples to the leptons and DM. We also note that whenever a light singlet scalar DM is coupled to the Higgs sector, there are Higgs portal terms such as  $\lambda_{XH}X^2 |H|^2$ ,  $\lambda_{X'H}X'^2|H|^2$  and  $\lambda_{XX'H}XX'|H|^2$ . These interactions will induce invisible decays of the SM Higgs boson, so their couplings are constrained by the Higgs boson measurements at the LHC,  $\lambda_{XH}, \lambda_{X'H}, \lambda_{XX'H} \lesssim 10^{-2}$  [81-83].

# 4.1 Mediation by second Higgs doublet

In this model, we couple the real scalar DM fields  $X$  and  $X^{\prime}$  to a two-Higgs-doublet model (2HDM) [80]. The relevant terms in the Lagrangian are

$$
\mathcal {L} \supset y _ {j} ^ {\prime} \bar {L} _ {j} H _ {2} \ell_ {j R} + \lambda_ {1 2} ^ {\prime} X X ^ {\prime} H _ {2} ^ {\dagger} H _ {1} + \mathrm {h . c .}, \tag {4.1}
$$

where  $H_{1}$  and  $H_{2}$  are two Higgs doublets, and lepton  $\ell_{j} = e,\mu ,\tau$ . For convenience, we may arrange the Higgs potential such that  $H_{1}$  is a SM-like Higgs doublet with the full VEV  $\langle H_1\rangle = (0,v)^T$ , and  $H_{2}$  is a heavy Higgs doublet with vanishing VEV  $\langle H_2\rangle = (0,0)^T$ . This means that  $H_{2}$  is irrelevant to fermion mass-generation, so its Yukawa couplings such as  $y_{\ell}^{\prime}$  can be very different from the leptonic Yukawa coupling  $y_{\ell} = m_{\ell} / v$  in the SM. As before, we assign  $X$  and  $X^{\prime}$  to be odd under an exact  $\mathbb{Z}_2$  symmetry which ensures the DM stability, while all other fields are  $\mathbb{Z}_2$  even. For  $H_{2}$  being a heavy Higgs doublet, we can integrate it out and induce the following effective operator at low energies,

$$
\mathcal {O} = \frac {y _ {j} ^ {\prime} \lambda_ {1 2} ^ {\prime}}{M _ {H _ {2}} ^ {2}} \bar {L} _ {j} H _ {1} \ell_ {j R} X X ^ {\prime} + \mathrm {h . c .} \tag {4.2}
$$

The just gives the effective dimension-6 operator  $\mathcal{O}_S$  in eq. (2.5a) with the cutoff scale  $\Lambda_S = M_{H_2} / \sqrt{|y_j'\lambda_{12}'|}$ . This can also induce a contribution to the DM self-interaction term  $\delta \tilde{\lambda} X^2 X'^2$  with  $\delta \tilde{\lambda} = \lambda_{12}'^2 v^2 /M_{H_2}^2$ . To generate the observed relic density and explain the XENON1T excess, we require  $\Lambda_S\simeq 1.1$  TeV as in eq. (3.5). For  $y_e'\lambda_{12}' = O(1)$ , this requires that the second Higgs doublet has a mass  $M_{H_2} = O(1)$  TeV.

# 4.2 Mediation by vector-like heavy leptons

In this subsection, we consider the second model where the effective interaction is mediated by a new generation of vector-like heavy leptons. The setup has some similarity to the lepton portal DM model [84-87], but it contains both vector-like fermion singlets and doublets as the mediators, which have mixings induced by Higgs VEV via Yukawa-type interactions. If coupled to the muon, such extra mixed vector-like leptons can also be a potential resolution to the muon  $g_{\mu} - 2$  [88]. This model contains the following new terms beyond the SM Lagrangian,

$$
\Delta \mathcal {L} = \left[ y _ {X} \bar {L} _ {j} \Psi X + y _ {X ^ {\prime}} \bar {f} \ell_ {j R} X ^ {\prime} + y ^ {\prime} \bar {\Psi} H f + \mathrm {h . c .} \right] + M _ {f} \bar {f} f + M _ {\Psi} \bar {\Psi} \Psi , (4. 3)
$$

where the Dirac fermion  $\Psi$  is an  $\mathrm{SU}(2)_L$  doublet with hypercharge  $Y_{\Psi} = -\frac{1}{2}$ , and Dirac fermion  $f$  is a weak singlet with hypercharge  $Y_{f} = -1$ . Both the fermions  $\Psi$  and  $f$  are  $\mathbb{Z}_2$  odd, just like the DM  $X$  and  $X'$ . We also set a small coupling for the terms  $y_X' \bar{L}_j \Psi X'$  and  $y_{X'}' \bar{f} \ell_{jR} X$ . If  $y_X'$  and  $y_{X'}'$  are as large as  $y_X$  and  $y_{X'}$ , the electron anomalous magnetic moment  $g_e - 2$  would receive an unacceptably large correction. In this case, the annihilation cross section  $\sigma_0 \sim 10^{-9} \mathrm{GeV}^{-2}$  is required for the DM relic density and can be related to  $\Delta(g_e - 2) \sim \frac{m_e}{16\pi^2} \sqrt{2\pi \sigma_0} \sim 10^{-10}$  [88]. Thus, we suppress the couplings for  $y_X' \bar{L}_j \Psi X'$  and  $y_{X'}' \bar{f} \ell_{jR} X'$  in this model setup. Although these two terms could be generated by one-loop diagrams in connection to the leptons, they are suppressed by the small SM lepton Yukawa couplings  $y_{\ell j}$ . To see this explicitly, we note that in the limit of setting the couplings  $y_{\ell j}, y_X', y_{X'}' = 0$ , the Lagrangian (4.3) is invariant under a discrete  $\mathbb{Z}_2'$  symmetry:  $\Psi \rightarrow -\Psi$ ,  $X \rightarrow -X$ ,  $\ell_{jR} \rightarrow -\ell_{jR}$ , and  $f \rightarrow -f$ . This symmetry is broken by the SM lepton Yukawa couplings  $y_{\ell j}$ . Hence, the loop-generated couplings  $y_X'$  and  $y_{X'}'$  are proportional to  $y_{\ell j}$ .

Integrating out the heavy vector-like fermions  $\Psi$  and  $f$ , we obtain the following gauge-invariant dimension-6 effective operator,

$$
\mathcal {O} = \frac {y _ {X} y _ {X ^ {\prime}} y ^ {\prime}}{M _ {\Psi} M _ {f}} \bar {L} _ {j} H \ell_ {j R} X X ^ {\prime} + \mathrm {h . c .} \tag {4.4}
$$

This is just the scalar-type operator  $\mathcal{O}_S$  given in eq. (2.5a), with the cutoff scale  $\Lambda_S = \left[M_{\Psi}M_f / (y_Xy_{X'}y')\right]^{1 / 2}$ . From our analysis in section 3, we find  $\Lambda_S \approx 1.1\mathrm{TeV}$  in order to realize the observed relic density and explain the XENON1T signal excess. For  $y_{X}y_{X^{\prime}}y^{\prime} \lesssim 1$  and  $M_{\Psi} \approx M_{f}$ , this suggests  $M_{\Psi}, M_{f} \gtrsim 1.1\mathrm{TeV}$ , which is above the current collider limit of  $900\mathrm{GeV}$  for the vector-like leptons [88, 89].

# 4.3 UV completion for vector-type contact operator

In this subsection, we provide a UV completion for the vector-type effective operator  $\mathcal{O}_{VR}$  in eq. (2.5c). We introduce an extra dark  $\mathrm{U}(1)_X$  gauge group with gauge boson  $A_{\mu}^{\prime}$  and two complex scalar singlets  $S$  and  $S^{\prime}$ . The electroweak symmetry is spontaneously broken by the SM-like Higgs doublet  $H$  with  $\mathrm{VEV}\langle H\rangle = (0,v_h)^T$ . The dark  $\mathrm{U}(1)_X$  gauge group is broken at the TeV scale by the singlet scalar field  $S$  with  $\mathrm{VEV}\langle S\rangle = v_S / \sqrt{2}$ . We present the anomaly-free particle content and group assignments in table 1.

We can write down the relevant new Lagrangian terms as follows,

$$
\begin{array}{l} \Delta \mathcal {L} = \bar {\ell} _ {R} \mathbf {i} \not D \ell_ {R} + | D ^ {\mu} \widehat {X} | ^ {2} - m _ {\widehat {X}} ^ {2} | \widehat {X} | ^ {2} - \lambda_ {\widehat {X} S} | S | ^ {2} | \widehat {X} | ^ {2} - \lambda_ {\widehat {X} H} | H | ^ {2} | \widehat {X} | ^ {2} \\ + | D ^ {\mu} S | ^ {2} + | D ^ {\mu} S ^ {\prime} | ^ {2} + \mu_ {S} ^ {2} | S | ^ {2} - \lambda_ {S} | S | ^ {4} - M _ {S ^ {\prime}} ^ {2} | S ^ {\prime} | ^ {2} - \lambda_ {S ^ {\prime}} | S ^ {\prime} | ^ {4} \\ - \lambda_ {S S ^ {\prime}} | S | ^ {2} | S ^ {\prime} | ^ {2} + \left(\tilde {\lambda} _ {S S ^ {\prime}} S ^ {\prime} S ^ {3} + \tilde {\lambda} _ {\hat {X} S ^ {\prime}} S ^ {\prime 2} \hat {X} ^ {2} + \mathrm {h . c .}\right) - \left(y _ {S} \nu_ {R} ^ {T} S \nu_ {R} + \mathrm {h . c .}\right) + \dots , \tag {4.5} \\ \end{array}
$$

where we have suppressed the fermion family indices for simplicity of notations. In the above, we consider that all the scalar couplings respect CP symmetry and are thus real. We note that the VEV of the singlet  $S$  can generate TeV-scale Majorana masses for the right-handed neutrinos,  $M_R = \sqrt{2} y_S v_S = O(0.5)\mathrm{TeV}$ , for the sample inputs of the scalar VEV  $v_S = O(100)\mathrm{GeV}$  and the Yukawa coupling  $y_S = O(3)$ . Then, we can generate the light neutrino masses through a TeV scale seesaw mechanism,

$$
m _ {\nu} = \frac {y _ {\nu} ^ {2} v _ {h} ^ {2}}{M _ {R}}. (4. 6)
$$

Table 1. Particle content and group assignments of the UV completion model for the vector-type contact operator  $\mathcal{O}_{VR}$ . Here  $Q_{L_j}$  and  $L_j$  denote the left-handed weak doublet of the SM quarks and leptons, respectively, and the subscript  $j$  is the fermion family index of the SM.  

<table><tr><td>Group</td><td>QjL</td><td>ujR</td><td>djR</td><td>Lj</td><td>ℓjR</td><td>νR</td><td>H</td><td>S</td><td>S&#x27;</td><td>X̂</td></tr><tr><td>SU(2)L</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td></tr><tr><td>U(1)Y</td><td>1/6</td><td>2/3</td><td>-1/3</td><td>-1/2</td><td>-1</td><td>0</td><td>1/2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>U(1)X</td><td>0</td><td>1/2</td><td>-1/2</td><td>0</td><td>-1/2</td><td>1/2</td><td>1/2</td><td>-1</td><td>3</td><td>-3</td></tr><tr><td>Z2</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>+</td><td>-</td></tr></table>

We consider that the  $\nu_{R}$  Yukawa couplings with the Higgs and lepton doublets to be  $y_{\nu} = O(y_{e})$ , where  $y_{e} \simeq 3 \times 10^{-6}$  denotes the electron Yukawa coupling in the standard model (SM). Thus, we find that eq. (4.6) provides the light neutrino masses  $m_{\nu} = O(0.1)\mathrm{eV}$ , which are consistent with the neutrino oscillation data.

For the singlet  $S'$  having a large positive mass  $M_{S'} = O(10)\mathrm{TeV}$ , we can minimize the scalar potential of eq. (4.5) for  $S'$  and realize a naturally small VEV  $\langle S' \rangle \equiv v_{S'} / \sqrt{2}$  as follows,

$$
v _ {S ^ {\prime}} \simeq \frac {\tilde {\lambda} _ {S S ^ {\prime}} v _ {S} ^ {3}}{2 M _ {S ^ {\prime}} ^ {2}}, \tag {4.7}
$$

where we have ignored the tiny ratios in the denominator (relative to the large mass term  $M_{S'}^2$ ),  $\lambda_{SS'}v_S^2 / M_{S'}^2 \ll 1$  and  $\lambda_{S'}v_{S'}^2 / M_{S'}^2 \simeq \frac{1}{4}\lambda_{S'}\tilde{\lambda}_{SS'}^2(v_S / M_{S'})^6 \ll 1$ , for  $\lambda_{SS'}, \tilde{\lambda}_{SS'} = O(10^{-1})$  and  $\lambda_{S'} \lesssim O(1)$ . From eq. (4.7) and taking the sample inputs  $M_{S'} = O(3)\mathrm{TeV}$ ,  $v_S = O(100)\mathrm{GeV}$  and  $\tilde{\lambda}_{SS'} = O(10^{-1})$ , we deduce a small  $S'$  VEV,  $v_{S'} = O(\mathrm{MeV})$ .

The complex singlet  $\widehat{X} = (X + \mathrm{i}X^{\prime}) / \sqrt{2}$  contains the DM components  $X$  and  $X^{\prime}$ , which are stabilized by the  $\mathbb{Z}_2$  parity defined in table 1. The  $(X,X^{\prime})$  mass-splitting is generated by a quartic term  $\tilde{\lambda}_{\widehat{X} S^{\prime}}S^{\prime 2}\widehat{X}^{2} + \mathrm{h.c.}$ , as shown in eq. (4.5). For the setup in eq. (4.5), we derive the mass-splitting of  $(X,X^{\prime})$  after the spontaneous symmetry breaking,

$$
m _ {X} ^ {2} = m _ {\widehat {X}} ^ {2} + \left(\frac {\lambda_ {\widehat {X} S} v _ {S} ^ {2}}{2} + \lambda_ {\widehat {X} H} v _ {H} ^ {2} - \tilde {\lambda} _ {\widehat {X} S ^ {\prime}} v _ {S ^ {\prime}} ^ {2}\right) + \dots , \tag {4.8a}
$$

$$
m _ {X ^ {\prime}} ^ {2} = m _ {\widehat {X}} ^ {2} + \left(\frac {\lambda_ {\widehat {X} S} v _ {S} ^ {2}}{2} + \lambda_ {\widehat {X} H} v _ {H} ^ {2} + \tilde {\lambda} _ {\widehat {X} S ^ {\prime}} v _ {S ^ {\prime}} ^ {2}\right) + \dots . (4. 8 \mathrm {b})
$$

We can realize  $m_X^2, m_{X'}^2 = O(m_{\widehat{X}}^2)$  by setting the mixed quartic couplings  $\lambda_{\widehat{X}S}, \lambda_{\widehat{X}H} = 0$  at the tree-level. From eq. (4.8), we derive the DM mass-splitting,

$$
\frac {m _ {X ^ {\prime}} - m _ {X}}{m _ {X}} = \frac {\tilde {\lambda} _ {\widehat {X} S ^ {\prime}} v _ {S ^ {\prime}} ^ {2}}{m _ {X} ^ {2}}. (4. 9)
$$

Below eq. (4.7), we obtained the sample value of the singlet scalar VEV  $v_{S'} = O(\mathrm{MeV})$ . With the inputs  $m_X = O(\mathrm{GeV})$  and  $\hat{\lambda}_{\widehat{X} S'} = O(1)$ , we can further derive the desired DM mass-splitting  $\Delta m = O(\mathrm{keV})$  from eq. (4.9).

The  $\mathrm{U}(1)_X$  gauge boson  $A_{\mu}^{\prime}$  acquires a mass after spontaneous gauge symmetry breaking. For the case of  $g_{X}\ll g,g^{\prime}$ , we have

$$
M _ {A ^ {\prime}} ^ {2} \approx g _ {X} ^ {2} v _ {S} ^ {2}, \tag {4.10}
$$

where  $g$ ,  $g'$  and  $g_{X}$  are the gauge couplings of  $\mathrm{SU}(2)_L$ ,  $\mathrm{U}(1)_Y$  and  $\mathrm{U}(1)_X$ , respectively. Integrating out the massive gauge field  $A_{\mu}'$ , we derive the dimension-6 effective operator  $\mathcal{O}_{VR}$  in eq. (2.5c) with a cut-off scale:

$$
\Lambda_ {V R} = \sqrt {\frac {2}{3}} \frac {M _ {A ^ {\prime}}}{g _ {X}}. (4. 1 1)
$$

We note that the DM particle in this model not only induces the effective operator  $\mathcal{O}_{VR}$ , but also couples to right-handed quarks. This opens up new DM annihilation channels in the early universe. Thus, the constraint set by the DM relic density in section 3 is inapplicable to this model while the constraint by the XENON1T data in section 2.2 remains valid. Since the Higgs doublet is charged under  $\mathrm{U}(1)_X$ , the model is further constrained by electroweak precision tests. We will explore the experimental tests of this model and related phenomenology elsewhere. A fully realistic UV completion model including GeV scale inelastic DM and dark photon mediator is presented in our new work [91].

# 5 Conclusions

Probing the dark matter (DM) signals via electron recoil provides an important means for direct detection of light DM particles. In this work, we explored an attractive resolution of the newly reported XENON1T anomaly via exothermic inelastic scattering between the DM particles and electrons. In this scenario, the dark matter sector contains two components  $X$  and  $X'$  with a small mass-splitting  $\Delta m = m_{X'} - m_X$  close to the recoil energy of the excess events. The inelastic scattering of the heavy component  $X'$  with electrons de-excites it to the lighter state  $X$ , releasing the energy to the recoiled electrons.

In section 2, we presented an effective field theory (EFT) approach to inelastic DM signals for the Xenon electron recoil detection. For relatively heavy mediator, we formulated the DM-lepton interactions by gauge-invariant effective contact operators of dimension-6 which contains two DM fields  $(X,X^{\prime})$  and two leptons, as given in eqs. (2.5)-(2.6). Then, we computed the electron recoil energy spectrum and fitted the XENON1T data. We found that the DM mass-splitting falls into the range  $\Delta m = (2.1 - 3.3)\mathrm{keV}$  at  $95\%$  C.L., with the best fit  $\Delta m = 2.8\mathrm{keV}$ , which is shown in figure 1 and figure 2.

In section 3, we analyzed the relic abundance for the inelastic DM. The DM particles were in kinetic and chemical equilibrium in the early Universe. The DM relic abundance is determined by the conventional freeze-out mechanism. The conversion between the heavier and lighter DM states was maintained by their scattering with  $e^{\pm}$  in the plasma. The conversion became inefficient at  $T \approx 1 \mathrm{MeV}$  and the proportion of the two DM components was frozen at  $n_{X} \simeq n_{X'}$ . We derived constraint on the DM self-interactions  $\tilde{\lambda} X^{2}X'^{2}$  to ensure that the DM annihilation  $X'X' \rightarrow XX$  froze out before the  $e^{\pm}$  decoupled. We also found that the decay of the heavier component  $X'$  is severely suppressed by the small DM mass-splitting  $\Delta m$ , so its lifetime is much longer than the age of the Universe. This means that the DM inelastic scattering  $X'e^{-} \rightarrow Xe^{-}$  still happens in the Universe today. We further identified the viable parameter space to realize the observed DM relic abundance and the XENON1T recoil energy spectrum, as shown in figure 3 and eqs. (3.5)-(3.6).

Finally, in section 4 we presented three plausible UV completions for the effective operators (2.5)-(2.6). The first model is given in section 4.1, which is a 2HDM extension with an extra heavy Higgs doublet as the mediator to induce the scalar-type DM-lepton interactions. The second model is shown in section 4.2. It contains extra vector-like heavy leptons as mediators to generate scalar-type DM-lepton interactions. We presented the third model in

section 4.3, in which the DM-lepton interactions are mediated by the new gauge boson  $A_{\mu}^{\prime}$  of a dark  $\mathrm{U}(1)_X$  gauge group. This gauge group is spontaneously broken at  $100\mathrm{GeV}$  scale and a low scale seesaw mechanism is realized for mass-generation of light neutrinos. At low energies, the dark gauge boson exchange can induce the vector-type DM-lepton interactions.

We stress that our generic EFT approach in sections 2-3 has provided a valuable approach for studying the inelastic DM and its implications for the Xenon electron recoil detection. With this approach, we identified new viable parameter space of the inelastic DM as in figures 1-3, and realized the inelastic DM via attractive UV-completion models in section 4. These will be further tested via the electron recoil measurements by the next-generation DM detectors, including the upcoming experiments of PandaX-4T [92], LZ [93], and XENONnT [94, 95].

# A Independent operators for DM-lepton interactions

In this appendix, we show that the effective operators in eq. (2.5) are the general gauge-invariant dimension-6 operators which are relevant for studying the inelastic DM-electron scattering. Here we focus on the operators including the DM bilinear fields of  $X$  and  $X^{\prime}$ ,

$$
\mathcal {O} _ {S} = \left(\bar {L} H \ell_ {R}\right) \left(X X ^ {\prime}\right) + \text {h . c .}, \tag {A.1a}
$$

$$
\mathcal {O} _ {V L} = (\bar {L} \gamma^ {\mu} L) (X ^ {\prime} \partial_ {\mu} X - X \partial_ {\mu} X ^ {\prime}), \tag {A.1b}
$$

$$
\mathcal {O} _ {V R} = (\bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R}) (X ^ {\prime} \partial_ {\mu} X - X \partial_ {\mu} X ^ {\prime}). \qquad \mathrm {(A . 1 c)}
$$

We show that the other relevant operators can be reexpressed in terms of this set of operators.

In general, we may also write down the following dimension-6 operators,

$$
(\bar {L} \mathrm {i} D L) \left(X X ^ {\prime}\right), \tag {A.2a}
$$

$$
\left(\bar {\ell} _ {R} \mathbf {i} D / \ell_ {R}\right) \left(X X ^ {\prime}\right), \tag {A.2b}
$$

$$
\left(\bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R}\right) \left(X ^ {\prime} \partial_ {\mu} X + X \partial_ {\mu} X ^ {\prime}\right), \tag {A.2c}
$$

$$
\left(\bar {L} \gamma^ {\mu} L\right) \left(X ^ {\prime} \partial_ {\mu} X + X \partial_ {\mu} X ^ {\prime}\right), \tag {A.2d}
$$

$$
B ^ {\mu \nu} \partial_ {\mu} X \partial_ {\nu} X ^ {\prime}, \tag {A.2e}
$$

where  $D^{\mu}$  is the covariant derivative and  $B_{\mu \nu}$  is the field strength tensor of the hypercharge gauge group  $\mathrm{U}(1)_Y$ . For the operators (A.2a) and (A.2b), they can be converted to the form of eq. (A.1a) with additional suppression by the small leptonic Yukawa coupling  $y_{\ell}$  after applying the equations of motions (EOM),

$$
\mathrm {i} \not D L = y _ {\ell} H \ell_ {R} + \dots , \tag {A.3a}
$$

$$
\mathrm {i} \not D \ell_ {R} = y _ {\ell} H ^ {\dagger} L + \dots . \tag {A.3b}
$$

Hence, the contributions of the operators (A.2a)-(A.2b) are negligible for our current study.

For eq. (A.2c), we note that up to integration by part, a total derivative term in the Lagrangian gives vanishing contribution and leads to the following:

$$
0 = \partial_ {\mu} (\bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R} X X ^ {\prime}) = \partial_ {\mu} (\bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R}) (X X ^ {\prime}) + (\bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R}) (X ^ {\prime} \partial_ {\mu} X + X \partial_ {\mu} X ^ {\prime}). \qquad \mathrm {(A . 4)}
$$

If we set the small leptonic Yukawa coupling  $y_{\ell} = 0$ , then the lepton chirality is conserved at tree level and thus  $\partial_{\mu}(\bar{\ell}_R\gamma^\mu \ell_R) = 0$ . Hence, including the leptonic Yukawa couplings only

leads to a term suppressed by  $y_{\ell}$ . To see this explicitly, we apply the EOM (A.3a) and obtain  $\partial_{\mu}(\bar{\ell}_R\gamma^\mu \ell_R) = y_\ell \bar{\ell}_R H^\dagger L + \mathrm{h.c.} + \dots$ . Thus, we arrive at

$$
(\bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R}) (X ^ {\prime} \partial_ {\mu} X + X \partial_ {\mu} X ^ {\prime}) = y _ {\ell} (\bar {\ell} _ {R} H ^ {\dagger} L) (X X ^ {\prime}) + \mathrm {h . c .} + \dots , \qquad \qquad \mathrm {(A . 5)}
$$

which again reduces to the form of eq. (A.1a), but suppressed by the small leptonic Yukawa coupling  $y_{\ell}$ . The exactly same reasoning holds for the operator (A.2d).

For eq. (A.2e), the following total derivative term gives vanishing contribution up to integration by part and leads to,

$$
0 = \partial_ {\mu} \left[ B ^ {\mu \nu} (X \partial_ {\nu} X ^ {\prime}) \right] = (\partial_ {\mu} B ^ {\mu \nu}) (X \partial_ {\nu} X ^ {\prime}) + B ^ {\mu \nu} (\partial_ {\mu} X \partial_ {\nu} X ^ {\prime}), \tag {A.6}
$$

where the right-hand-side contains only two terms and a possible third term vanishes,  $B^{\mu \nu}(X\partial_{\mu}\partial_{\nu}X') = 0$ , because  $B_{\mu \nu}$  is anti-symmetric. The equation of motion for  $B^{\mu}$  reads,

$$
\partial_ {\mu} B ^ {\mu \nu} = - g ^ {\prime} Y _ {\ell_ {R}} \bar {\ell} _ {R} \gamma^ {\nu} \ell_ {R} - g ^ {\prime} Y _ {L} \bar {L} \gamma^ {\nu} L + \dots . \tag {A.7}
$$

Thus, we find that eq. (A.2e) reduces to eqs. (A.1c) and (A.1b),

$$
B ^ {\mu \nu} (\partial_ {\mu} X \partial_ {\nu} X ^ {\prime}) = (X \partial_ {\mu} X ^ {\prime}) \left(g ^ {\prime} Y _ {\ell_ {R}} \bar {\ell} _ {R} \gamma^ {\mu} \ell_ {R} + g ^ {\prime} Y _ {L} \bar {L} \gamma^ {\mu} L\right) + \dots . \qquad \mathrm {(A . 8)}
$$

In summary, the above proof shows that the set of operators in eq. (2.5) are unique for our present EFT study.

# Acknowledgments

This research was supported in part by the National NSF of China (under grants 11835005 and 11675086), by the CAS Center for Excellence in Particle Physics (CCEPP), by the National Key R & D Program of China (No. 2017YFA0402204), by the Key Laboratory for Particle Physics, Astrophysics and Cosmology (Ministry of Education), and by the Office of Science and Technology, Shanghai Municipal Government (No. 16DZ2260200).

# References

[1] XENON collaboration, Energy resolution and linearity of XENON1T in the MeV energy range, Eur. Phys. J. C 80 (2020) 785 [arXiv:2003.03825] [INSPIRE].  
[2] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].  
[3] A.E. Robinson, XENON1T observes tritium, arXiv:2006.13278 [INSPIRE].  
[4] N.F. Bell, V. Cirigliano, M.J. Ramsey-Musolf, P. Vogel and M.B. Wise, How magnetic is the Dirac neutrino?, Phys. Rev. Lett. 95 (2005) 151802 [hep-ph/0504134] [INSPIRE].  
[5] N.F. Bell, M. Gorchtein, M.J. Ramsey-Musolf, P. Vogel and P. Wang, Model independent bounds on magnetic moments of Majorana neutrinos, Phys. Lett. B 642 (2006) 377 [hep-ph/0606248] [INSPIRE].  
[6] BOREXINO collaboration, Limiting neutrino magnetic moments with Borexino Phase-II solar neutrino data, Phys. Rev. D 96 (2017) 091103 [arXiv:1707.09355] [INSPIRE].  
[7] K. van Bibber, P.M. McIntyre, D.E. Morris and G.G. Raffelt, A Practical Laboratory Detector for Solar Axions, Phys. Rev. D 39 (1989) 2089 [INSPIRE].

[8] S. Moriyama, A Proposal to search for a monochromatic component of solar axions using Fe-57, Phys. Rev. Lett. 75 (1995) 3222 [hep-ph/9504318] [INSPIRE].  
[9] J. Redondo, Solar axion flux from the axion-electron coupling, JCAP 12 (2013) 008 [arXiv:1310.0823] [INSPIRE].  
[10] L. Di Luzio, M. Fedele, M. Giannotti, F. Mescia and E. Nardi, Solar axions cannot explain the XENON1T excess, Phys. Rev. Lett. 125 (2020) 131804 [arXiv:2006.12487] [INSPIRE].  
[11] F. Takahashi, M. Yamada and W. Yin, XENON1T Excess from Anomaly-Free Axionlike Dark Matter and Its Implications for Stellar Cooling Anomaly, Phys. Rev. Lett. 125 (2020) 161801 [arXiv:2006.10035] [INSPIRE].  
[12] G. Alonso-Álvarez, F. Ertas, J. Jaeckel, F. Kahlhoefer and L.J. Thormaehlen, Hidden Photon Dark Matter in the Light of XENON1T and Stellar Cooling, JCAP 11 (2020) 029 [arXiv:2006.11243] [INSPIRE].  
[13] C. Boehm, D.G. Cerdeno, M. Fairbairn, P.A.N. Machado and A.C. Vincent, *Light new physics in XENON1T*, Phys. Rev. D **102** (2020) 115013 [arXiv:2006.11250] [INSPIRE].  
[14] D. Aristizabal Sierra, V. De Romeri, L.J. Flores and D.K. Papoulias, Light vector mediators facing XENON1T data, Phys. Lett. B 809 (2020) 135681 [arXiv:2006.12457] [INSPIRE].  
[15] K. Kannike, M. Rraidal, H. Veermäe, A. Strumia and D. Teresi, Dark Matter and the XENON1T electron recoil excess, Phys. Rev. D 102 (2020) 095002 [arXiv:2006.10735] [INSPIRE].  
[16] B. Fornal, P. Sandick, J. Shu, M. Su and Y. Zhao, Boosted Dark Matter Interpretation of the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 161804 [arXiv:2006.11264] [INSPIRE].  
[17] L. Su, W. Wang, L. Wu, J.M. Yang and B. Zhu, Atmospheric Dark Matter and Xenon1T Excess, Phys. Rev. D 102 (2020) 115028 [arXiv:2006.11837] [INSPIRE].  
[18] Y. Chen, M.-Y. Cui, J. Shu, X. Xue, G. Yuan and Q. Yuan, Sun Heated MeV-scale Dark Matter and the XENON1T Electron recoil Excess, arXiv:2006.12447 [INSPIRE].  
[19] Q.-H. Cao, R. Ding and Q.-F. Xiang, Exploring for sub-MeV Boosted Dark Matter from Xenon Electron Direct Detection, arXiv:2006.12767 [INSPIRE].  
[20] H. Alhazmi, D. Kim, K. Kong, G. Mohlabeng, J.-C. Park and S. Shin, Implications of the XENON1T Excess on the Dark Matter Interpretation, arXiv:2006.16252 [INSPIRE].  
[21] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, Leptonic New Force and Cosmic-ray Boosted Dark Matter for the XENON1T Excess, Phys. Lett. B 811 (2020) 135863 [arXiv:2006.13910] [INSPIRE].  
[22] S. Chigusa, M. Endo and K. Kohri, Constraints on electron-scattering interpretation of XENON1T excess, JCAP 10 (2020) 035 [arXiv:2007.01663] [INSPIRE].  
[23] J. Smirnov and J.F. Beacom, New Freezeout Mechanism for Strongly Interacting Dark Matter, Phys. Rev. Lett. 125 (2020) 131301 [arXiv:2002.04038] [INSPIRE].  
[24] A. Bally, S. Jana and A. Trautner, Neutrino self-interactions and XENON1T electron recoil excess, Phys. Rev. Lett. 125 (2020) 161802 [arXiv:2006.11919] [INSPIRE].  
[25] M. Du, J. Liang, Z. Liu, V.Q. Tran and Y. Xue, On-shell mediator dark matter models and the Xenon1T anomaly, Chin. Phys. C 45 (2021) 013114 [arXiv:2006.11949] [INSPIRE].  
[26] N.F. Bell, J.B. Dent, B. Dutta, S. Ghosh, J. Kumar and J.L. Newstead, Explaining the XENON1T excess with Luminous Dark Matter, Phys. Rev. Lett. 125 (2020) 161803 [arXiv:2006.12461] [INSPIRE].  
[27] G. Paz, A.A. Petrov, M. Tammaro and J. Zupan, Shining dark matter in Xenon1T, arXiv:2006.12462 [INSPIRE].

[28] J. Buch, M.A. Buen-Abad, J. Fan and J.S.C. Leung, Galactic Origin of Relativistic Bosons and XENON1T Excess, JCAP 10 (2020) 051 [arXiv:2006.12488] [INSPIRE].  
[29] U.K. Dey, T.N. Maity and T.S. Ray, Prospects of Migdal Effect in the Explanation of XENON1T Electron recoil Excess, Phys. Lett. B 811 (2020) 135900 [arXiv:2006.12529] [INSPIRE].  
[30] A.N. Khan, Can Nonstandard Neutrino Interactions explain the XENON1T spectral excess?, Phys. Lett. B 809 (2020) 135782 [arXiv:2006.12887] [INSPIRE].  
[31] K. Nakayama and Y. Tang, Gravitational Production of Hidden Photon Dark Matter in Light of the XENON1T Excess, Phys. Lett. B 811 (2020) 135977 [arXiv:2006.13159] [INSPIRE].  
[32] H.M. Lee, Exothermic dark matter for XENON1T excess, JHEP 01 (2021) 019 [arXiv:2006.13183] [INSPIRE].  
[33] M. Baryakhtar, A. Berlin, H. Liu and N. Weiner, Electromagnetic Signals of Inelastic Dark Matter Scattering, arXiv:2006.13918 [INSPIRE].  
[34] J. Bramante and N. Song, Electric But Not Eclectic: Thermal Relic Dark Matter for the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 161805 [arXiv:2006.14089] [INSPIRE].  
[35] L. Zu, G.-W. Yuan, L. Feng and Y.-Z. Fan, Mirror Dark Matter and Electronic Recoil Events in XENON1T, arXiv:2006.14577 [INSPIRE].  
[36] I.M. Bloch, A. Caputo, R. Essig, D. Redigolo, M. Sholapurkar and T. Volansky, Exploring New Physics with  $O(keV)$  Electron Recoils in Direct Detection Experiments, arXiv:2006.14521 [INSPIRE].  
[37] M. Lindner, Y. Mambrini, T.B. de Melo and F.S. Queiroz, XENON1T anomaly: A light  $Z^{\prime}$  from a Two Higgs Doublet Model, Phys. Lett. B 811 (2020) 135972 [arXiv:2006.14590] [INSPIRE].  
[38] W. DeRocco, P.W. Graham and S. Rajendran, Exploring the robustness of stellar cooling constraints on light particles, Phys. Rev. D 102 (2020) 075015 [arXiv:2006.15112] [INSPIRE].  
[39] M. Chala and A. Titov, One-loop running of dimension-six Higgs-neutrino operators and implications of a large neutrino dipole moment, JHEP 09 (2020) 188 [arXiv:2006.14596] [INSPIRE].  
[40] C. Gao, J. Liu, L.-T. Wang, X.-P. Wang, W. Xue and Y.-M. Zhong, Reexamining the Solar Axion Explanation for the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 131806 [arXiv:2006.14598] [INSPIRE].  
[41] J.B. Dent, B. Dutta, J.L. Newstead and A. Thompson, Inverse Primakoff Scattering as a Probe of Solar Axions at Liquid Xenon Direct Detection Experiments, Phys. Rev. Lett. 125 (2020) 131805 [arXiv:2006.15118] [INSPIRE].  
[42] P. Ko and Y. Tang, Semi-annihilating  $Z_{3}$  Dark Matter for XENON1T Excess, arXiv:2006.15822 [INSPIRE].  
[43] W. Chao, Y. Gao and M.j. Jin, Pseudo-Dirac Dark Matter in XENON1T, arXiv:2006.16145 [INSPIRE].  
[44] L. Delle Rose, G. Hütsi, C. Marzo and L. Marzola, Impact of loop-induced processes on the boosted dark matter interpretation of the XENON1T excess, arXiv:2006.16078 [INSPIRE].  
[45] B. Bhattacharjee and R. Sengupta, XENON1T Excess: Some Possible Backgrounds, arXiv:2006.16172 [INSPIRE].  
[46] Y. Gao and T. Li, Lepton Number Violating Electron Recoils at XENON1T by the U(1)  $B-L$  Model with Non-Standard Interactions, arXiv:2006.16192 [INSPIRE].  
[47] T. Li, The KSVZ Axion and Pseudo-Nambu-Goldstone Boson Models for the XENON1T Excess, arXiv:2007.00874 [INSPIRE].

[48] O.G. Miranda, D.K. Papoulias, M. Tórtola and J.W.F. Valle, XENON1T signal from transition neutrino magnetic moments, Phys. Lett. B 808 (2020) 135685 [arXiv:2007.01765] [INSPIRE].  
[49] K. Benakli, C. Branchina and G. Lafforgue-Marmet, U(1) mixing and the Weak Gravity Conjecture, Eur. Phys. J. C 80 (2020) 1118 [arXiv:2007.02655] [INSPIRE].  
[50] N. Okada, S. Okada, D. Raut and Q. Shafi, Dark matter  $Z'$  and XENON1T excess from  $\mathrm{U}(1)_X$  extended standard model, Phys. Lett. B 810 (2020) 135785 [arXiv:2007.02898] [INSPIRE].  
[51] J. Davighi, M. McCullough and J. Tooby-Smith, Undulating Dark Matter, JHEP 11 (2020) 120 [arXiv:2007.03662] [INSPIRE].  
[52] K.S. Babu, S. Jana and M. Lindner, Large Neutrino Magnetic Moments in the Light of Recent Experiments, JHEP 10 (2020) 040 [arXiv:2007.04291] [INSPIRE].  
[53] K. Harigaya, Y. Nakai and M. Suzuki, Inelastic Dark Matter Electron Scattering and the XENON1T Excess, Phys. Lett. B 809 (2020) 135729 [arXiv:2006.11938] [INSPIRE].  
[54] H. An and D. Yang, Direct detection of freeze-in inelastic dark matter, arXiv:2006.15672 [INSPIRE].  
[55] S. Baek, J. Kim and P. Ko, XENON1T excess in local  $Z_{2}$  DM models with light dark sector, Phys. Lett. B 810 (2020) 135848 [arXiv:2006.16876] [INSPIRE].  
[56] P.W. Graham, R. Harnik, S. Rajendran and P. Saraswat, Exothermic Dark Matter, Phys. Rev. D 82 (2010) 063512 [arXiv:1004.0937] [INSPIRE].  
[57] G. Barello, S. Chang and C.A. Newby, A Model Independent Approach to Inelastic Dark Matter Scattering, Phys. Rev. D 90 (2014) 094027 [arXiv:1409.0536] [INSPIRE].  
[58] E. Del Nobile, G.B. Gelmini, A. Georgescu and J.-H. Huh, Reevaluation of spin-dependent WIMP-proton interactions as an explanation of the DAMA data, JCAP 08 (2015) 046 [arXiv:1502.07682] [INSPIRE].  
[59] R. Essig, J. Mardon and T. Volansky, Direct Detection of Sub-GeV Dark Matter, Phys. Rev. D 85 (2012) 076007 [arXiv:1108.5383] [INSPIRE].  
[60] B.M. Roberts, V.A. Dzuba, V.V. Flambaum, M. Pospelov and Y.V. Stadnik, Dark matter scattering on electrons: Accurate calculations of atomic excitations and implications for the DAMA signal, Phys. Rev. D 93 (2016) 115037 [arXiv:1604.04559] [INSPIRE].  
[61] K. Freese, M. Lisanti and C. Savage, Colloquium: Annual modulation of dark matter, Rev. Mod. Phys. 85 (2013) 1561 [arXiv:1209.3339] [INSPIRE].  
[62] B.M. Roberts and V.V. Flambaum, *Electron-interacting dark matter: Implications from DAMA/LIBRA-phase2* and prospects for liquid xenon detectors and NaI detectors, Phys. Rev. D 100 (2019) 063017 [arXiv:1904.07127] [INSPIRE].  
[63] P. Gondolo and G. Gelmini, *Cosmic abundances of stable particles: Improved analysis*, Nucl. Phys. B 360 (1991) 145 [INSPIRE].  
[64] M. Srednicki, R. Watkins and K.A. Olive, *Calculations of Relic Densities in the Early Universe*, Nucl. Phys. B 310 (1988) 693 [INSPIRE].  
[65] Z.-H. Yu, J.-M. Zheng, X.-J. Bi, Z. Li, D.-X. Yao and H.-H. Zhang, Constraining the interaction strength between dark matter and visible matter: II. scalar, vector and spin-3/2 dark matter, Nucl. Phys. B 860 (2012) 115 [arXiv:1112.6052] [INSPIRE].  
[66] D.J. Fixsen, The Temperature of the Cosmic Microwave Background, Astrophys. J. 707 (2009) 916 [arXiv:0911.1955] [INSPIRE].  
[67] ALEPH, DELPHI, L3, OPAL and LEP ELECTROWEAK collaborations, Electroweak Measurements in Electron-Positron Collisions at W-Boson-Pair Energies at LEP, Phys. Rept. 532 (2013) 119 [arXiv:1302.3415] [INSPIRE].

[68] P.J. Fox, R. Harnik, J. Kopp and Y. Tsai, LEP Shines Light on Dark Matter, Phys. Rev. D 84 (2011) 014028 [arXiv:1103.0240] [INSPIRE].  
[69] R. Primulando, J. Julio and P. Uttayarat, *Collision Constraints on a Dark Matter Interpretation of the XENON1T Excess*, Eur. Phys. J. C 80 (2020) 1084 [arXiv:2006.13161] [INSPIRE].  
[70] R. Essig, J. Mardon, M. Papucci, T. Volansky and Y.-M. Zhong, Constraining Light Dark Matter with Low-Energy  $e^{+}e^{-}$  Colliders, JHEP 11 (2013) 167 [arXiv:1309.5084] [INSPIRE].  
[71] L. Darmé, S.A.R. Ellis and T. You, Light Dark Sectors through the Fermion Portal, JHEP 07 (2020) 053 [arXiv:2001.01490] [INSPIRE].  
[72] BELLE-II collaboration, Belle II Technical Design Report, arXiv:1011.0352 [INSPIRE].  
[73] ATLAS collaboration, Search for Higgs boson decays to beyond-the-Standard-Model light bosons in four-lepton events with the ATLAS detector at  $\sqrt{s} = 13$  TeV, JHEP 06 (2018) 166 [arXiv:1802.03388] [INSPIRE].  
[74] CMS collaboration, Search for an  $L_{\mu} - L_{\tau}$  gauge boson using  $Z \rightarrow 4\mu$  events in proton-proton collisions at  $\sqrt{s} = 13$  TeV, Phys. Lett. B 792 (2019) 345 [arXiv:1808.03684] [INSPIRE].  
[75] PLANCK collaboration, Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [arXiv:1807.06209] [INSPIRE].  
[76] J.R. Ellis, M.K. Gaillard and D.V. Nanopoulos, A Phenomenological Profile of the Higgs Boson, Nucl. Phys. B 106 (1976) 292 [INSPIRE].  
[77] M.A. Shifman, A.I. Vainshtein, M.B. Voloshin and V.I. Zakharov, Low-Energy Theorems for Higgs Boson Couplings to Photons, Sov. J. Nucl. Phys. 30 (1979) 711 [INSPIRE].  
[78] C.B. Jackson, G. Servant, G. Shaughnessy, T.M.P. Tait and M. Taoso, Gamma-ray lines and One-Loop Continuum from s-channel Dark Matter Annihilations, JCAP 07 (2013) 021 [arXiv:1302.1802] [INSPIRE].  
[79] PARTICLE DATA GROUP collaboration, Review of Particle Physics, Phys. Rev. D 98 (2018) 030001 [INSPIRE].  
[80] G.C. Branco, P.M. Ferreira, L. Lavoura, M.N. Rebelo, M. Sher and J.P. Silva, Theory and phenomenology of two-Higgs-doublet models, Phys. Rept. 516 (2012) 1 [arXiv:1106.0034] [INSPIRE].  
[81] M. Escudero, A. Berlin, D. Hooper and M.-X. Lin, Toward (Finally!) Ruling Out Z and Higgs Mediated Dark Matter Models, JCAP 12 (2016) 029 [arXiv:1609.09079] [INSPIRE].  
[82] X.-G. He and J. Tandean, New LUX and PandaX-II Results Illuminating the Simplest Higgs-Portal Dark Matter Models, JHEP 12 (2016) 074 [arXiv:1609.03551] [INSPIRE].  
[83] N. Nagata, K.A. Olive and J. Zheng, Asymmetric Dark Matter Models in SO(10), JCAP 02 (2017) 016 [arXiv:1611.04693] [INSPIRE].  
[84] Y. Bai and J. Berger, Lepton Portal Dark Matter, JHEP 08 (2014) 153 [arXiv:1402.6696] [INSPIRE].  
[85] Q. Yuan et al., Interpretations of the DAMPE electron data, arXiv:1711.10989 [INSPIRE].  
[86] S.-F. Ge, H.-J. He, Y.-C. Wang and Q. Yuan, Probing flavor structure of cosmic ray  $e^{\mp}$  spectrum and implications for dark matter indirect searches, Nucl. Phys. B 959 (2020) 115140 [arXiv:2004.10683] [INSPIRE].  
[87] S.-F. Ge, H.-J. He and Y.-C. Wang, Flavor Structure of the Cosmic-Ray Electron/Positron Excesses at DAMPE, Phys. Lett. B 781 (2018) 88 [arXiv:1712.02744] [INSPIRE].  
[88] J. Kawamura, S. Okawa and Y. Omura, Current status and muon  $g - 2$  explanation of lepton portal dark matter, JHEP 08 (2020) 042 [arXiv:2002.12534] [INSPIRE].

[89] ATLAS collaboration, Search for electroweak production of charginos and sleptons decaying into final states with two leptons and missing transverse momentum in  $\sqrt{s} = 13$  TeV pp collisions using the ATLAS detector, Eur. Phys. J. C 80 (2020) 123 [arXiv:1908.08215] [INSPIRE].  
[90] L. Wang and X.-F. Han, Study of the heavy CP-even Higgs with mass 125 GeV in two-Higgs-doublet models at the LHC and ILC, JHEP 11 (2014) 085 [arXiv:1404.7437] [INSPIRE].  
[91] H.-J. He, Y.-C. Wang and J. Zheng, GeV Scale Inelastic Dark Matter with Dark Photon Mediator via Direct Detection and Cosmological/Laboratory Constraints, arXiv:2012.05891 [INSPIRE].  
[92] PANDAX collaboration, Dark matter direct search sensitivity of the PandaX-4T experiment, Sci. China Phys. Mech. Astron. 62 (2019) 31011 [arXiv:1806.02229] [INSPIRE].  
[93] LZ collaboration, The LUX-ZEPLIN (LZ) Experiment, Nucl. Instrum. Meth. A 953 (2020) 163047 [arXiv:1910.09124] [INSPIRE].  
[94] XENON collaboration, Projected WIMP sensitivity of the XENONnT dark matter experiment, JCAP 11 (2020) 031 [arXiv:2007.08796] [INSPIRE].  
[95] XENON collaboration, Physics reach of the XENON1T dark matter experiment, JCAP 04 (2016) 027 [arXiv:1512.07501] [INSPIRE].