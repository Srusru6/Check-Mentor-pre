# Lepton-mediated electroweak baryogenesis, gravitational waves and the  $4\tau$  final state at the collider

# Ke-Pan Xie

Center for Theoretical Physics, Department of Physics and Astronomy, Seoul National University, Seoul 08826, Korea

E-mail: kpxie@snu.ac.kr

ABSTRACT: An electroweak baryogenesis (EWBG) mechanism mediated by  $\tau$  lepton transport is proposed. We extend the Standard Model with a real singlet scalar  $S$  to trigger the strong first-order electroweak phase transition (SFOEWPT), and with a set of leptophilic dimension-5 operators to provide sufficient CP violating source. We demonstrate this model is able to generate the observed baryon asymmetry of the universe. This scenario is experimentally testable via either the SFOEWPT gravitational wave signals at the next-generation space-based detectors, or the  $pp\rightarrow h^{*}\rightarrow SS\rightarrow 4\tau$  process (where  $h^*$  is an off-shell Higgs) at the hadron colliders. A detailed collider simulation shows that a considerable fraction of parameter space can be probed at the HL-LHC, while almost the whole parameter space allowed by EWBG can be reached by the 27 TeV HE-LHC.

KEYWORDS: Beyond Standard Model, Cosmology of Theories beyond the SM, Thermal Field Theory

ARXIV EPRINT: 2011.04821

# Contents

1 Introduction 1  
2 Lepton-mediated EwBG 2

2.1 SFOEWPT and GWs 2  
2.2 Transport equations and the generation of BAU 6

3 Collider search: the  $4\tau$  final state 9  
4 Conclusion 12

A The complete one-loop scalar potential 13  
B Coefficients in the Boltzmann equations 14

# 1 Introduction

Cosmological observations show that there is an imbalance between the abundance of matter and antimatter in our universe. This is also known as the baryon asymmetry of the universe (BAU), which can be described by the baryon-to-entropy ratio [1]

$$
\eta_ {B} \equiv \frac {n _ {B}}{s} = [ 0. 8 2 \sim 0. 9 4 ] \times 1 0 ^ {- 1 0}. \tag {1.1}
$$

Creating the BAU requires three Sakharov conditions [2-4]: i) baryon number violation, ii) C and CP violation, and iii) departure from equilibrium. The Standard Model (SM) satisfies the first condition [via the electroweak (EW) sphaleron] but fails in the last two: the CP violating (CPV) phase [from the CKM matrix] is too tiny, and the SM EW phase transition (EWPT) is a smooth crossover [5]. Therefore, the observed BAU is a clear evidence for physics beyond the SM (BSM).

There have been a lot of BSM mechanisms explaining BAU [6], and this paper will focus on EW baryogenesis (EWBG) [7-9]. In EWBG, the out-of-equilibrium environment is provided by a strong first-order EWPT (SFOEWPT), during which bubbles containing EW broken phase nucleate and expand in the EW symmetric background. The CPV source on the bubble wall seeds a net density for the left-handed fermions in front of the wall when the particles collide with the bubbles. This "chiral asymmetry" then diffuses into the EW symmetric phase where it is converted to a baryon asymmetry by the EW sphaleron process. The net baryon number is swept into the expanding bubbles and then frozen, because the EW sphaleron is strongly suppressed inside the bubble. The bubbles eventually fill up the whole universe, completing the SFOEWPT and leaving the observed BAU. EWBG is an attractive scenario as it typically involves BSM physics around TeV

scale, thus can be tested at current or future colliders [10]. In addition, the phase transition gravitational waves (GWs) might be detectable at the future space-based detectors [11].

Most literatures focus on EwBG mediated by quark transport, in particular by top transport since the large top Yukawa ( $y_{t} \approx 1$ ) enhances the CPV source and hence the BAU [12-14] (for recent studies see [15-21]).<sup>1</sup> However, the top-mediated EwBG is not as efficient as expected, due to three reasons summarized in ref. [25] as follows. First, because of the strong QCD interaction with the plasma, the diffusion of quark chiral asymmetry to the EW symmetric phase is inefficient [26]. Second, the CPV in top sector has been stringently constrained by the electron electric dipole moment (EDM) experiments [27].<sup>2</sup> Third, the top Yukawa as well as the strong sphaleron process tend to washout the chiral asymmetry, significantly decreasing the generated BAU [30, 31].

Those three disadvantages may be overcome in a lepton-mediated EWBG [25]: first, leptons are easier to diffuse in the plasma [26]; second, the EDM constraints for muon and tau are much weaker [32]; third, the leptons are free from the washout effect of strong sphaleron. Therefore, even though the CPV source from the lepton sector is typically smaller than that from the top sector (for example the tau Yukawa  $y_{\tau} \approx 0.01 \ll y_t$ ), a lepton-mediated EWBG is still possible to account for the observed BAU. Indeed, refs. [33-37] have shown that a successful  $\tau$ -mediated EWBG can be realized, if  $y_{\tau}$  is enhanced in BSM models. Recently, refs. [25, 38] study the CPV source from SM EFT dimension-6 operators, and point out that even a SM-like  $y_{\tau}$  is able to realize EWBG. $^{3}$

In this work, we propose a novel  $\tau$ -mediated EwBG model based on the real singlet scalar extension of SM (xSM). The CPV source comes from the leptophilic dimension-5 operator  $(1 / \Lambda)S\bar{\ell}_L H\tau_R$ , with  $\Lambda$  being the cutoff scale,  $S$  the singlet,  $H = \left(G^{+},(h + iG^{0}) / \sqrt{2}\right)^{T}$  the Higgs doublet,  $\ell_{L} = (\nu_{\tau L},\tau_{L})^{T}$  the third generation lepton doublet and  $\tau_{R}$  the right-handed tau. We will show that such a model can explain today's BAU with a SM-like  $y_{\tau}$  in section 2, where we also discuss the possibility of detecting the phase transition GWs at the future space-based detectors. Section 3 is devoted to collider phenomenology, in which we demonstrate our scenario can be efficiently probed by the  $pp\to h^{*}\to SS\to \tau^{+}\tau^{-}\tau^{+}\tau^{-}$  process at the LHC and future 27 TeV HE-LHC. Finally, we conclude in section 4.

# 2 Lepton-mediated EWBG

# 2.1 SFOEWPT and GWs

The SFOEWPT of xSM has been extensively studied [41-51], and we needn't to repeat all those results here. For simplicity, we assume the following tree level potential

$$
V _ {0} = \mu_ {H} ^ {2} | H | ^ {2} + \frac {\mu_ {S} ^ {2}}{2} S ^ {2} + \lambda_ {H} | H | ^ {4} + \frac {\lambda_ {S}}{4} S ^ {4} + \lambda_ {H S} | H | ^ {2} S ^ {2}, \tag {2.1}
$$

which is symmetric under the  $\mathbb{Z}_2$  transformation  $S\rightarrow -S$ . Under the unitary gauge,

$$
V _ {0} = \frac {\mu_ {H} ^ {2}}{2} h ^ {2} + \frac {\mu_ {S} ^ {2}}{2} S ^ {2} + \frac {\lambda_ {H}}{4} h ^ {4} + \frac {\lambda_ {S}}{4} S ^ {4} + \frac {\lambda_ {H S}}{2} h ^ {2} S ^ {2}. \tag {2.2}
$$

The bounded below condition for this potential is  $\lambda_H > 0$ ,  $\lambda_S > 0$ , and  $\sqrt{\lambda_H\lambda_S} + \lambda_{HS} > 0$ . We are interested in the parameter space with [52]

$$
\mu_ {H} ^ {2} <   0, \quad \mu_ {S} ^ {2} <   0, \quad \lambda_ {H} \mu_ {S} ^ {2} > \lambda_ {H S} \mu_ {H} ^ {2}, \quad \lambda_ {S} \mu_ {H} ^ {2} > \lambda_ {H S} \mu_ {S} ^ {2}, \quad - \frac {\mu_ {H} ^ {4}}{\lambda_ {H}} <   - \frac {\mu_ {S} ^ {4}}{\lambda_ {S}}, \qquad (2. 3)
$$

in which  $V_{0}$  has two local minima  $(v,0)$  and  $(0,w)$  with

$$
v = \sqrt {- \mu_ {H} ^ {2} / \lambda_ {H}}, w = \sqrt {- \mu_ {S} ^ {2} / \lambda_ {S}}, (2. 4)
$$

and the former is the global minimum, i.e. the vacuum. Expanding potential around the vacuum gives physical masses of the scalars

$$
M _ {h} ^ {2} = - 2 \mu_ {H} ^ {2}, \quad M _ {S} ^ {2} = \mu_ {S} ^ {2} + \lambda_ {H S} v ^ {2}. \tag {2.5}
$$

In other words, the measured values  $M_{h} = 125\mathrm{GeV}$  and  $v = 246\mathrm{GeV}$  have fixed  $\mu_H^2$  and  $\lambda_{H}$ , and we only have three free parameters in eq. (2.2).

At one-loop level,  $V_{0}$  becomes

$$
V _ {1} = V _ {0} + V _ {\mathrm {C W}} + V _ {\mathrm {C T}}, \tag {2.6}
$$

where  $V_{\mathrm{CW}}$  is the Coleman-Weinberg potential, and  $V_{\mathrm{CT}}$  is the counter term. At finite temperature, the scalar potential receives thermal corrections,

$$
V _ {T} = V _ {1} + \tilde {V} _ {T} + V _ {\text {d a i s y}}, \tag {2.7}
$$

where  $\tilde{V}_T$  is the one-loop thermal integral correction, while  $V_{\mathrm{daisy}}$  is the daisy resummation term. The detailed expressions for  $V_{\mathrm{CW}}$ ,  $V_{\mathrm{CT}}$ ,  $\tilde{V}_T$  and  $V_{\mathrm{daisy}}$  are given in appendix A. Taking only the leading  $T^2$  terms [53],  $V_T$  can be approximated as

$$
V _ {T} \approx \frac {1}{2} \left(\mu_ {H} ^ {2} + c _ {H} T ^ {2}\right) h ^ {2} + \frac {1}{2} \left(\mu_ {S} ^ {2} + c _ {S} T ^ {2}\right) S ^ {2} + \frac {\lambda_ {H}}{4} S ^ {4} + \frac {\lambda_ {S}}{4} S ^ {4} + \frac {\lambda_ {H S}}{2} h ^ {2} S ^ {2}, \tag {2.8}
$$

where

$$
c _ {H} = \frac {3 g ^ {2} + g ^ {\prime 2}}{1 6} + \frac {y _ {t} ^ {2}}{4} + \frac {\lambda_ {H}}{2} + \frac {\lambda_ {H S}}{1 2}, \quad c _ {S} = \frac {\lambda_ {S}}{4} + \frac {\lambda_ {H S}}{3}, \tag {2.9}
$$

with  $g^{(t)}$  and  $y_{t}$  being the EW gauge couplings and top Yukawa, respectively.

The thermal potential in eq. (2.8) can realize a two-step phase transition in which a second-order phase transition first occurs along the  $S$ -axis, and then a first-order EWPT happens through the vacuum decay between the  $S$ - and  $h$ -axes, i.e.

$$
\left(\langle h \rangle = 0, \langle S \rangle = 0\right) \xrightarrow [ \text {s t e p} ]{\text {F i r s t}} \left(\langle h \rangle = 0, \langle S \rangle \neq 0\right) \xrightarrow [ \text {s t e p} ]{\text {S e c o n d}} \left(\langle h \rangle \neq 0, \langle S \rangle = 0\right), \tag {2.10}
$$

as the temperature decreases. For the first step, if there were an exact  $\mathbb{Z}_2$  symmetry for  $S$  in  $V_{T}$ , then the probability of transition to  $+S$  and  $-S$  directions would be equal, leaving

the domain wall problem. To avoid this issue, we assume a small  $\mathbb{Z}_2$ -breaking is present, such that the transition along the  $+S$  direction is energetically preferred [29].

The second step is a first-order EWPT, whose necessary condition is two degenerate vacua separated by a barrier at the critical temperature  $T_{c}$ . For the polynomial potential in eq. (2.8), this condition is equivalent to [52]

$$
\frac {c _ {S}}{c _ {H}} <   \frac {\mu_ {S} ^ {2}}{\mu_ {H} ^ {2}} <   \frac {\sqrt {\lambda_ {S}}}{\sqrt {\lambda_ {H}}} <   \frac {\lambda_ {H S}}{\lambda_ {H}}. \tag {2.11}
$$

The sufficient condition for a first-order EWPT is the onset of nucleation, which is resolved from the equality of vacuum decay rate and the universe expansion rate at the nucleation temperature  $T_{n}$ ,

$$
T _ {n} ^ {4} e ^ {- S _ {3} \left(T _ {n}\right) / T _ {n}} \approx H ^ {4} \left(T _ {n}\right), \tag {2.12}
$$

with  $S_{3}(T)$  being the Euclidean action of the  $O(3)$ -symmetric bounce solution [54], and  $H(T)$  the Hubble constant. For a radiation-dominated universe, eq. (2.12) is approximately

$$
\frac {S _ {3} (T _ {n})}{T _ {n}} \sim 1 4 0. \tag {2.13}
$$

for a  $T_{n}$  around the EW scale [55]. For the EW sphaleron process to be suppressed inside the bubble, we further require [56, 57]

$$
v _ {n} / T _ {n} \gtrsim 1, \tag {2.14}
$$

which is the definition for a strong transition, namely a SFOEWPT.

For a numerical study, we adopt the complete one-loop potential eq. (2.7) as the input. Using eq. (2.5), we choose the three free parameter of the scalar potential as  $M_S$ ,  $\lambda_{HS}$  and  $\lambda_S$ . For a fixed  $\lambda_S$ , we scan over  $M_S$  and  $\lambda_{HS}$  and derive the SFOEWPT parameter space by solving eq. (2.12) with the CosmoTransitions package [58] and checking eq. (2.13). The results are shown as shaded regions in figure 1. We found that the shape of those regions match the analytical condition in eq. (2.11) very well. This is because in the two-step phase transition paradigm, the SFOEWPT is induced by the tree level potential barrier dominated by the  $\lambda_{HS}h^2 S^2 /2$  term in the potential, thus a leading  $T^2$  analysis already provides very good approximation. Due to the same reason, a sizable  $\lambda_{HS}$  is needed for a successful SFOEWPT. The correlation between SFOEWPT and the  $\lambda_{HS}$  parameter provides an excellent channel for probing our mechanism at the collider, as will be shown in section 3.

A SFOEWPT in the early universe may show detectable cosmological signals today, as the phase transition GWs typically peak around millihertz, within the sensitive region of a few next-generation space-based detectors, such as LISA [59], BBO [60], TianQin [61, 62], Taiji [63, 64] and DECIGO [65, 66]. GWs are produced by three sources: bubble collision, sound waves and turbulence. For a SFOEWPT with a non-luminal terminal bubble velocity, the bubble collision contribution is negligible and the GWs are dominated by sound waves [67]. The GW spectrum today is described by

$$
\Omega_ {\mathrm {G W}} (f) = \frac {1}{\rho_ {c}} \frac {\rho_ {\mathrm {G W}}}{d \ln f}, \tag {2.15}
$$

![](images/4aab3220bf31af247cf96256c4060a4712f929e7382a5c6a766cc282e0697c9b.jpg)  
Figure 1. Left: parameter space allowed by a successful SFOEWPT. The colored shaded regions are for individual  $\lambda_S$  values, except the light blue shaded area is for the non-perturbative region that  $\lambda_S > 4\pi$ . The colored scatter points are the parameter regions that are detectable at the LISA. For  $\lambda_S = 8$ , to avoid the plot to be too messy we omit the general SFOEWPT region and only show the LISA detectable points. The star-symbols highlight the two BPs in eq. (2.19). Right: the GW spectrum for the two BPs selected from the left panel.

![](images/8443357b758588e759efa8f0c1a825211b8ee344401db2a28ef6cc9c278fe914.jpg)

where  $f$  is the frequency,  $\rho_{\mathrm{GW}}$  is the GW energy density and  $\rho_{c}$  is the critical energy density of the present universe. For a given SFOEWPT, eq. (2.15) can be expressed as numerical functions of the following three physical parameters [68-70]:

1.  $v_{b}$ , the wall velocity of the expanding bubbles.  
2.  $\alpha$ , the ratio of the SFOEWPT latent heat to the cosmic radiative energy density

$$
\alpha = \frac {1}{\rho_ {R} \left(T _ {n}\right)} \left(- \Delta V _ {T} + T \frac {\partial \Delta V _ {T}}{\partial T}\right) \bigg | _ {T _ {n}}, \tag {2.16}
$$

where  $\rho_{R}(T_{n}) = \pi^{2}g(T_{n})T_{n}^{4} / 30$  with  $g(T_{n})$  being the number of relativistic degrees of freedom, and  $\Delta V_{T}$  is the free energy difference between the true and false vaca.

3.  $\beta / H$ , the inverse ratio of the time scale of the SFOEWPT and the universe expansion,

$$
\beta / H = T _ {n} \frac {d}{d T} \left(\frac {S _ {3} (T)}{T}\right) \Big | _ {T _ {n}}. \tag {2.17}
$$

In general,  $\beta / H$  is related to the duration of the SFOEWPT hence the peak frequency of the GWs, while  $\alpha$  is relevant to the signal strength.

We obtain the GWs spectrum using the formulae from the references mentioned above, with the energy budget from ref. [71]. The bubble velocity is adopted as  $v_{b} = 0.6$  as a benchmark. Strictly speaking, the  $\alpha$  and  $\beta / H$  parameters should be calculated at the percolation temperature  $T_{p}$  [67, 73-76]; however the supercooling effect in our scenario is not strong - we have checked that  $\alpha \lesssim 1$  for our parameter space - thus  $T_{p} \approx T_{n}$  is a

good approximation. We have taken into account the suppression factor  $H\tau_{\mathrm{sw}}$  for the sound wave contribution due to the shortness of its duration compared to the Hubble time [67]. For the detectability of GWs signals we take the LISA as an example and evaluate the signal-to-noise-ratio (SNR) [69]

$$
\mathrm {S N R} = \sqrt {\mathcal {T} \int_ {f _ {\operatorname* {m i n}}} ^ {f _ {\operatorname* {m a x}}} d f \left(\frac {\Omega_ {\mathrm {G W}} (f)}{\Omega_ {\mathrm {L I S A}} (f)}\right) ^ {2}}, \tag {2.18}
$$

with  $\Omega_{\mathrm{LISA}}$  being the sensitive curve of the LISA detector [69], and  $\mathcal{T} = 9.46\times 10^{7}$  s the data-taking duration [70]. With  $\mathrm{SNR} = 10$  as the detectable threshold, we find that for a fixed  $\lambda_{S}$ , there is a narrow band in the  $M_S - \lambda_{HS}$  plane that can be probed by the LISA, as shown in the left panel of figure 1. Fixing  $\lambda_{S} = 1$ , we choose two benchmark points (BPs) as

$$
\mathrm {B P} 1: \quad M _ {S} = 1 0 0 \mathrm {G e V}, \quad \lambda_ {H S} = 0. 4 6; \quad \alpha = 0. 1 3, \quad \beta / H = 4 0 6,
$$

$$
\mathrm {B P 2}: \quad M _ {S} = 2 0 0 \mathrm {G e V}, \quad \lambda_ {H S} = 0. 8 8; \quad \alpha = 0. 0 5, \quad \beta / H = 1 0 9, \tag {2.19}
$$

and plot their GW spectra in the right panel of figure 1 as an illustration.

# 2.2 Transport equations and the generation of BAU

Consider a SFOEWPT triggered by the vacuum decay  $(0, w_{n}) \rightarrow (v_{n}, 0)$  at  $T_{n}$ . Since EWBG happens in the vicinity of the bubble wall, it's convenient to work in the wall rest frame. Under the planar wall approximation, the scalars can be treated as background fields  $\hat{h}$  and  $\hat{S}$  that depend only on the spatial distance  $z$  from the center of wall. Assuming  $z \to \pm \infty$  is the broken/symmetric phase, the scalar backgrounds can be parametrized as

$$
\hat {h} (z) = \frac {v _ {n}}{2} \left(1 + \tanh  \frac {z}{L _ {w}}\right), \quad \hat {S} (z) = \frac {w _ {n}}{2} \left(1 - \tanh  \frac {z}{L _ {w}}\right), \tag {2.20}
$$

with  $L_{w}$  being the wall thickness.

To realize another necessary condition for EwBG, i.e. the CP violation, we shall assume the singlet has the following leptophilic interactions with the SM fields via dimension-5 operators,

$$
\mathcal {L} _ {5} = \sum_ {i, j} \frac {c _ {i j}}{\Lambda} S \bar {\ell} _ {L} ^ {i} H e _ {R} ^ {j} + \text {h . c .}, \tag {2.21}
$$

where  $i$ ,  $j$  are generation indices,  $c_{ij}$  are the (complex) Wilson coefficients, and  $\Lambda$  is the cutoff scale of EFT. For simplicity, we assume the Willson coefficients are flavor-diagonal, i.e.  $c_{ij} = \mathrm{diag}\{c_e,c_\mu ,c_\tau \}$ . During a SFOEWPT, the effective mass of a lepton reads

$$
\bar {m} _ {i} (z) = \frac {y _ {i}}{\sqrt {2}} \hat {h} (z) + \frac {c _ {i}}{\sqrt {2} \Lambda} \hat {h} (z) \hat {S} (z), \tag {2.22}
$$

where  $i = e, \mu, \tau$ , and  $y_{i} = \sqrt{2} M_{i} / v$  is the SM Yukawa coupling, with  $M_{i}$  being the physical lepton mass at zero temperature. Since the effective mass is space-dependent, the complex phase of  $c_{i}$  cannot be globally rotated away, resulting in physical CPV effects.

The Yukawa couplings for the first and second generation leptons are too small to generate a considerable CPV source [25], thus we neglect them and focus on the  $\tau$  lepton. In this case, the magnitude of  $c_{\tau}$  can be absorbed into the definition of  $\Lambda$ , and we can rewrite the relevant part of eq. (2.21) as

$$
\mathcal {L} _ {5} \supset \frac {e ^ {i \phi_ {\tau}}}{\Lambda_ {\tau}} S \bar {\ell} _ {L} H \tau_ {R} + \text {h . c .}, \tag {2.23}
$$

such that  $\phi_{\tau}$  is a pure CPV phase. Note that this operator is rather weakly constrained by the EDM experiments, especially in our scenario that  $V_{0}$  is  $\mathbb{Z}_2$  symmetric and  $\langle S\rangle = 0$  so that there is no tree level  $h - S$  mixing at zero temperature.

In the plasma, the  $\tau$  leptons participate in gauge, Yukawa, helicity-flipping and EW sphaleron interactions. We deal with those interactions following the standard two-step approach: in the first step we derive the generation and diffusion of the (lepton) chiral asymmetry by solving the Boltzmann equations of the "fast processes", and then in the second step the chiral asymmetry is converted into a baryon asymmetry via the EW sphaleron. Here EW sphaleron is the "slow process" and all other interactions are treated as "fast".

First we establish and solve the Boltzmann equations. Denoting the net particle density (i.e. the number density difference between particle and antiparticle) for left-handed third generation leptons, right-handed taus, and the Higgs bosons as  $\ell = n_{\nu_{\tau_L}} + n_{\tau_L}$ ,  $\tau = n_{\tau_R}$  and  $h = n_{G^+} + n_{H^0}$ , respectively, the transport equations read [25]

$$
v _ {w} \ell^ {\prime} - D _ {\ell} \ell^ {\prime \prime} = \Gamma_ {M} \left(\frac {\tau}{k _ {\tau}} - \frac {\ell}{k _ {\ell}}\right) + \Gamma_ {Y} \left(\frac {\tau}{k _ {\tau}} - \frac {\ell}{k _ {\ell}} + \frac {h}{k _ {h}}\right) - S _ {\tau},
$$

$$
v _ {w} \tau^ {\prime} - D _ {\tau} \tau^ {\prime \prime} = - \Gamma_ {M} \left(\frac {\tau}{k _ {\tau}} - \frac {\ell}{k _ {\ell}}\right) - \Gamma_ {Y} \left(\frac {\tau}{k _ {\tau}} - \frac {\ell}{k _ {\ell}} + \frac {h}{k _ {h}}\right) + S _ {\tau}, \tag {2.24}
$$

where  $\ell$ ,  $\tau$  and  $h$  are functions of the spatial coordinate  $z$ , and “/” represents the  $d/dz$  operation.  $v_{w} \in (0,1)$  is the bubble wall velocity with respect to the plasma just in front of the wall. Note that  $v_{w}$  can differ from  $v_{b}$  defined in section 2.1, which is relative wall velocity to the plasma at infinite distance [78].  $D_{\ell} = 100/T_{n}$  and  $D_{\tau} = 380/T_{n}$  are respectively the diffusion constants for left- and right-handed leptons (note that they are much bigger than quark diffusion constant  $D_{q} = 6/T_{n}$ ) [33].  $\Gamma_{M}$  and  $\Gamma_{Y}$  denote the helicity-flipping and Yukawa rates, respectively, and their detail definitions as well as the temperature-dependent coefficients  $k_{i}$  are given in appendix B. The EW gauge interactions are not written in eq. (2.24) because they are treated as in equilibrium, so that the two components of the same  $\mathrm{SU}(2)_L$  doublet share a common chemical potential.  $S_{\tau}$  is the CPV source given by the closed time path method [79]

$$
S _ {\tau} = \frac {v _ {w}}{\pi^ {2}} \mathrm {I m} \left[ \bar {m} _ {\tau} ^ {\prime} m _ {\tau} ^ {*} \right] J _ {\tau}, \tag {2.25}
$$

where  $\bar{m}_{\tau}$  is the  $z$ -dependent effective mass in eq. (2.22), while  $J_{\tau}$  is a numerical factor whose expression is presented in appendix B. Eq. (2.25) clearly reveals that the number density difference between  $\ell_{L}$  and  $\bar{\ell}_L$  is sourced by the space-dependent imaginary part of

the effective mass (namely the physical CPV phase) when the  $\tau$  leptons are passing across the bubble wall.

There are three unknown functions  $\ell$ ,  $\tau$  and  $h$  in eq. (2.24), but only two equations (for leptons). To solve the equations self-consistently we need one more equation about  $h$ . However, the transport equation of  $h$  involves the heavy quarks such as top and bottom, because they interact strongly with the Higgs. As a result, a complete treatment for lepton transport should also include the equations for quarks as well. Thanks to the small lepton Yukawa couplings, the impact of  $h$  on lepton transport is negligible, hence we can reasonably approximate  $h \approx 0$  and avoid the complexity of the quark transport equations. In addition, the diffusion constant for left- and right-handed leptons can be approximated as the same, i.e.  $D_{\ell} \approx D_{\tau} \approx 100 / T_{n}$ , which provides a relation  $\ell = -\tau$  and therefore eq. (2.24) is simplified into a single ordinary differential equation about  $\ell$

$$
- D _ {\ell} \ell^ {\prime \prime} + v _ {w} \ell^ {\prime} + \left(\Gamma_ {M} + \Gamma_ {Y}\right) \left(\frac {1}{k _ {\ell}} + \frac {1}{k _ {\tau}}\right) \ell = - S _ {\tau}, \tag {2.26}
$$

which can be solved either semi-analytically or numerically. Ref. [25] has shown that eq. (2.26) is a very good approximation to the complete treatment which takes into account  $D_{\ell} \neq D_{\tau}$  and the heavy quark transport.

By numerically solving eq. (2.26), we get the non-zero chiral asymmetry  $\ell$ . This asymmetry is then converted into a baryon-to-entropy ratio [25]

$$
\eta_ {B} = \frac {n _ {B}}{s} = - \frac {3 \Gamma_ {\mathrm {w s}}}{2 s D _ {q} \alpha_ {+}} \int_ {- \infty} ^ {0} d z \ell (z) \exp \{- \alpha_ {-} z \}, \tag {2.27}
$$

where  $D_{q} = 6 / T_{n}$  is the quark diffusion constant [33],  $\Gamma_{\mathrm{ws}} = 6\kappa \alpha_W^5 T_n$  is the EW sphaleron rate with  $\kappa \approx 18$  [80], and

$$
\alpha_ {\pm} = \frac {v _ {w} \pm \sqrt {1 5 D _ {q} \Gamma_ {\mathrm {w s}} + v _ {w} ^ {2}}}{2 D _ {q}}. \tag {2.28}
$$

The integration region of eq. (2.27) is limited within the EW symmetric phase where the EW sphaleron is active. The generated baryon number survives until today, becoming the observed BAU. Note that the dimension-5 operator in eq. (2.23) is odd under the  $\mathbb{Z}_2$  transformation, so does the CPV source  $S_{\tau}$  in eq. (2.25). Consequently, if there were an exact  $\mathbb{Z}_2$  for  $S$  in the potential, the  $+S$  and  $-S$  transitions equally distributed in different patches of the universe finally give a zero net BAU on average. This consideration gives another motivation for the small  $\mathbb{Z}_2$ -breaking term [29].

For illustration, we consider the two SFOEWPT BPs in eq. (2.19) of section 2.1. Their SFOEWPT profiles are

$$
\mathrm {B P} 1: \quad T _ {n} = 6 4. 4 4 \mathrm {G e V}, \quad v _ {n} = 2 3 9. 0 6 \mathrm {G e V}, \quad w _ {n} = 1 3 2. 1 3 \mathrm {G e V};
$$

$$
\mathrm {B P 2}: \quad T _ {n} = 9 4. 3 2 \mathrm {G e V}, \quad v _ {n} = 2 2 0. 5 5 \mathrm {G e V}, \quad w _ {n} = 1 0 8. 9 7 \mathrm {G e V}, \tag {2.29}
$$

and we take the wall thickness  $L_{w} = 15 / T_{n}$  according to ref. [81]. The two BPs are fed into the Boltzmann equation (2.26) to get the chiral asymmetry and then we use eq. (2.27) to evaluate the BAU. The CPV phase and cutoff scale are chosen to be  $\phi_{\tau} = 0.02$  and

![](images/d41925277ab18bd7bd083e55865c614fe2b27a5e0bb8a599e0f0c542b45fdbf2.jpg)  
Figure 2. Left: the chiral asymmetry  $\ell(z) \equiv n_{\ell}(z) - n_{\bar{\ell}}(z)$  solved from the transport equation (2.26). Right: the BAU as a function of wall velocity  $v_w$ . The gray band represents the BBN fitted result of  $\eta_B$ . The CPV phase is  $\phi_{\tau} = 0.02$  for both panels.

![](images/837e799d3f132664b04cbc69f8cfeb67f27fa3f52fb7b77a9d642272d0f89b05.jpg)

$\Lambda_{\tau} = 10 \mathrm{TeV},^{6}$  respectively. The chiral asymmetry  $\ell(z) \equiv n_{\ell}(z) - n_{\bar{\ell}}(z)$  is shown in the left panel of figure 2, where we can recognize that the asymmetry is generated on the bubble wall, and then diffuses to both the EW symmetric and broken phases. Only the chiral asymmetry in the symmetric phase is responsible for generating BAU, and we plot the resultant BAU as a function of  $v_{w}$  in the right panel of figure 2. The observed BAU is shown in gray band and we find it can be achieved for  $v_{w} \sim 0.01$  or 0.1 in the figure, where  $\phi_{\tau} = 0.02$  is fixed. Since  $\phi_{\tau}$  is actually a free parameter, we conclude that our mechanism can explain the BAU within a vast parameter space of  $\phi_{\tau}$  and  $v_{w}$ .

# 3 Collider search: the  $4\tau$  final state

Complementary to the space-based GW detectors, the terrestrial collider experiments also serve as a powerful probe for the SFOEWPT by either measuring the Higgs potential shape or directly detecting the relevant BSM physics around TeV scale [82-90]. In this section we assess the possibility of detecting the lepton-mediated EWBG at the 14 TeV LHC and the 27 TeV HE-LHC [91]. At the collider, the real singlet in the xSM can be probed by the resonant or non-resonant di-Higgs production, the modified Higgs-fermion or Higgs-gauge couplings, etc. However, most of the proposed channels require the mixing between  $S$  and  $h$ . If unfortunately the  $S - h$  mixing is negligible, e.g. in the scenario considered in section 2.1 that  $S$  has an approximate  $\mathbb{Z}_2$  symmetry in the potential and  $\langle S\rangle |_{T = 0} = 0$ , then it would be very challenging to test the SFOEWPT at the collider [92, 93]. However,

![](images/03488a717210b0854c81321c1b13c50b54350139bcd76ab6f31de0b921881e9c.jpg)  
Figure 3. Production rates of  $pp \rightarrow h^* \rightarrow SS \rightarrow \tau^+ \tau^- \tau^+ \tau^-$  at the 14 TeV LHC and 27 TeV HE-LHC. We have assumed  $\lambda_{HS} = 0.5$  and  $\mathrm{Br}(S \rightarrow \tau^+ \tau^-) = 100\%$ .

in our scenario, there exists the following process at a  $pp$  collider,

$$
g g \rightarrow h ^ {*} \rightarrow S S \rightarrow \tau^ {+} \tau^ {-} \tau^ {+} \tau^ {-}, \tag {3.1}
$$

i.e. the pair production of  $S$  through an off-shell Higgs (mediated by the  $\lambda_{HS}v hS^2 \subset \lambda_{HS}|H|^2 S^2$  vertex), followed by the  $S \to \tau^{+}\tau^{-}$ decay (mediated by the dimension-5 operator  $(c_{\tau} / \Lambda_{\tau})S\bar{\ell}_{L}H\tau_{R}$ ). This robust channel is present even in the absence of a  $h - S$  mixing. Since the  $\lambda_{HS}$  coupling is required by a SFOEWPT, while the dimension-5 operator is required by the CPV, both two necessary ingredients of our model is tested by the single process in eq. (3.1).

The cross sections of eq. (3.1) are shown as functions of  $M_S$  in figure 3, where we have set  $\lambda_{HS} = 0.5$  and assumed  $S$  decays exclusively to  $\tau^{+}\tau^{-}$ . Note that the production rate is proportional to  $\lambda_{HS}^2$ , thus this channel is sensitive to the SFOEWPT parameter space, which requires a sizable  $\lambda_{HS}$  (see the left panel of figure 1). The decay branching ratio for a  $\tau$  lepton is  $\sim 35\%$  and  $\sim 65\%$  for leptonic and hadronic channels, respectively. The leptonic decay yields a charged lepton  $(e^{\pm}$  or  $\mu^{\pm}$ ) and missing transverse momentum, while the hadronic decay typically results in a  $\tau$ -jet [94]. Therefore, the  $4\tau$  final state can be categorized into the following final states directly available at the detector:

$$
4 \tau_ {j} (17.9 \%), \quad 1 \ell 3 \tau_ {j} (38.4 \%), \quad 2 \ell 2 \tau_ {j} (31.1 \%), \quad 3 \ell 1 \tau_ {j} (11.1 \%), \quad 4 \ell (1.5 \%), \tag{3.2}
$$

where  $\ell$  denotes the charged leptons  $e^{\pm}$  and  $\mu^{\pm}$ ,  $\tau_{j}$  denotes the  $\tau$ -jets, and the numbers in the brackets are the corresponding probabilities. We find that the  $1\ell 3\tau_{j}$  and  $2\ell 2\tau_{j}$  channels are hopefully to be probed, as they enjoy considerable cross section fractions and have charged leptons to trigger the events. While the  $2\ell 2\tau_{j}$  final state is searched at the LHC in supersymmetry-relevant experiments [95], the  $1\ell 3\tau_{j}$  final state has not yet been dedicatedly searched at the LHC.

In this work, we focus on the  $1\ell 3\tau_{j}$  channel, whose main backgrounds are the SM  $W^{\pm} +$  jets,  $Z +$  jets,  $t\bar{t}$ ,  $W^{\pm}\tau^{+}\tau^{-}j$ ,  $\tau^{+}\tau^{-}+$  jets and  $\tau^{+}\tau^{-}\tau^{+}\tau^{-}$  processes. We perform

Table 1. Cut flows for backgrounds and the two signal BPs at the 14 TeV LHC and 27 TeV HE-LHC. The two signal BPs are from eq. (2.19) in section 2.1.  

<table><tr><td>Unit: fb</td><td>Signal BP1</td><td>Signal BP2</td><td>W±+jets</td><td>Z+jets</td><td>tt̅</td><td>W±τ+τ-j</td><td>τ+τ-+jets</td><td>τ+τ-τ+τ-</td></tr><tr><td colspan="9">14 TeV LHC</td></tr><tr><td>Before</td><td>12.3</td><td>1.19</td><td>1.45×106</td><td>6.18×105</td><td>1.21×105</td><td>129</td><td>1.49×105</td><td>7.15</td></tr><tr><td>Cut I</td><td>1.76</td><td>0.352</td><td>2.43×105</td><td>5.91×104</td><td>6.73×104</td><td>34.5</td><td>6.35×103</td><td>0.511</td></tr><tr><td>Cut II</td><td>0.0733</td><td>0.0269</td><td>0.832</td><td>3.28</td><td>3.41</td><td>0.152</td><td>0.841</td><td>0.0378</td></tr><tr><td>Cut III</td><td>0.0661</td><td>0.0245</td><td>0.681</td><td>2.64</td><td>0.243</td><td>0.134</td><td>0.762</td><td>0.0356</td></tr><tr><td colspan="9">27 TeV HE-LHC</td></tr><tr><td>Before</td><td>42.7</td><td>5.30</td><td>4.10×106</td><td>1.59×106</td><td>1.06×106</td><td>321</td><td>3.34×105</td><td>13.4</td></tr><tr><td>Cut I</td><td>6.74</td><td>1.64</td><td>6.66×105</td><td>1.69×105</td><td>5.55×105</td><td>95.8</td><td>1.72×104</td><td>1.19</td></tr><tr><td>Cut II</td><td>0.267</td><td>0.115</td><td>2.54</td><td>13.9</td><td>45.7</td><td>0.369</td><td>2.23</td><td>0.0724</td></tr><tr><td>Cut III</td><td>0.245</td><td>0.103</td><td>2.05</td><td>10.9</td><td>9.14</td><td>0.315</td><td>1.87</td><td>0.0635</td></tr></table>

a collider simulation using the packages FeynRules [96] (to write the UFO model file [97] for our scenario), MadGraph5_aMC@NLO [98] (to generate parton level events for signal and backgrounds) and Pythia8 [99] and Delphes [100] (for parton shower and fast detector simulation, respectively). The  $W^{\pm} +$  jets,  $Z +$  jets and  $\tau^{+}\tau^{-} +$  jets backgrounds are realized by matching  $W^{\pm}jjj$  to  $W^{\pm}jj$  process, matching  $Zjj$  to  $Zj$  process, matching  $\tau^{+}\tau^{-}jj$  to  $\tau^{+}\tau^{-}j$  process, respectively. The  $tt$  is also matched to  $+1$  jet final state. The inclusive decay of  $\tau$  lepton is implemented by the Pythia8 package.

To suppress the backgrounds, we apply the following cuts to the events:

1. Exactly 1 charged lepton with  $p_T^\ell > 25$  GeV and  $|\eta_\ell| < 2.5$ , and at least 3 jets with  $p_T^j > 20$  GeV and  $|\eta_j| < 5$ .  
2. At least 3  $\tau$ -tagged jets. The tagging and mistag rates for a  $\tau$ -jet are set to be  $60\%$  and  $1\%$ , respectively.  
3. Veto any event with  $b$ -tagged jets. The  $b$ -tagging efficiency is chosen as  $77\%$ , and the mistag rate for  $c$  and other light quarks are  $17\%$  and  $0.75\%$ , respectively [101].

The cut flows for the backgrounds and the two signal BPs are listed in table 1. We can see that the requirement of three  $\tau$ -jets significantly suppresses the backgrounds, while the  $b$ -veto cut works very well in reducing the  $t\bar{t}$  background.

Given the cut flow data, now we can derive the signal significance for a given set of  $(M_S,\lambda_{HS})$  and integrated luminosity  $\mathcal{L}$ :

$$
\text {S i g n i f i c a n c e} = \frac {\sigma_ {S} \epsilon_ {S}}{\sqrt {\sigma_ {B} \epsilon_ {B}}} \sqrt {\mathscr {L}}, \tag {3.3}
$$

where  $\sigma_{S,B}$  and  $\epsilon_{S,B}$  denote the cross sections and cut efficiencies for signal and total background, respectively. We define the significance equal to  $5\sigma$  and  $2\sigma$  as the experimental

![](images/0cc18b0433c4da846c35fd67b6b672d1cff862dc008465e8105ed84e41d4d932.jpg)  
Figure 4. Probing the SFOEWPT parameter space at the LHC and HE-LHC. The left and right panels show the  $5\sigma$  discovery and  $2\sigma$  exclusion limits, respectively. The gray shaded region labeled as "SFOEWPT" is derived by varying  $\lambda_{S} \in (0, 4\pi)$ .

![](images/e816530442e9bd3881c011737a05fafc9baaa1cc9bd17e7ac16025bea0ea9c51.jpg)

discovery and exclusion limits of the collider at a given integrated luminosity, respectively. Note that the collider phenomenology is irrelevant to the singlet quartic coupling  $\lambda_{S}$ , while the SFOEWPT parameter space depends on  $\lambda_{S}$ , see the left panel of figure 1. In figure 4, we obtain the whole SFOEWPT parameter space at the  $\lambda_{HS} - M_S$  plane by varying  $\lambda_{S}$  from 0 to the non-perturbative limit  $4\pi$ , and taking the envelop of the SFOEWPT regions. The expected reach of different collider setups is shown in the figure with solid or dashed lines with different colors. We can see that those reach curves have similar shapes with the SFOEWPT parameter space (gray shaded region), because both the  $gg \rightarrow h^* \rightarrow SS$  process and the SFOEWPT prefer a large  $\lambda_{HS}$ . A considerable fraction of the SFOEWPT space can be probed at the HL-LHC (namely the LHC with an integrated luminosity of 3 ab $^{-1}$ ), while almost all the SFOEWPT parameter space can be covered by the 27 HE-LHC with an integrated luminosity of 15 ab $^{-1}$ .

Note that the results in figure 4 are for the  $1\ell 3\tau_{j}$  channel only. We have also checked that the  $2\ell 2\tau_{j}$  channel shows a similar reach by using the backgrounds simulated in ref. [95]. Therefore, the combination of those two channels can provide an even better probe for our mechanism. Finally, we emphasize that the collider phenomenology presented in this section is mainly determined by the existence of the dimension-5 operator  $(c_{\tau} / \Lambda_{\tau})S\bar{\ell}_{L}H\tau_{R}$ , but not sensitive to its CPV phase. If in the future we really detected an excess in the  $4\tau$  channel, then a further analysis should be performed to reveal its CP structure.

# 4 Conclusion

In this article, we have proposed a novel EwBG mechanism mediated by  $\tau$  lepton transport. The SM is extended with a real singlet to trigger the SFOEWPT and with a set of dimension-5 operators to get sufficient CPV source. For simplicity, we assume a scalar potential that is symmetric under  $S\rightarrow -S$  at tree level, and demonstrate that it is able to realize the SFOEWPT with the real scalar mass at  $\mathcal{O}(100\mathrm{GeV})$ . By establishing and

solving the Boltzmann equations, we have shown that this model is able to account for current BAU using the  $\tau$ -mediated EwBG.

Our model is testable in current or near-future experiments. On one hand, the phase transition GWs can be probed by the near-future space-based detectors (e.g. LISA); on the other hand, the pair production of singlets via the off-shell Higgs leads to distinguishable  $4\tau$  final state at hadron colliders such as LHC and HE-LHC. This  $pp \rightarrow h^{*} \rightarrow SS \rightarrow \tau^{+}\tau^{-}\tau^{+}\tau^{-}$  process is a characteristic channel of our mechanism, as the production of  $S$  pair is induced by the  $\lambda_{HS}$  term which is required by the SFOEWPT, while the decay of  $S$  is induced by the dimension-5 operator which is needed for CPV. A detailed collider simulation shows that the EWBG parameter space can be efficiently explored through the  $1\ell 3\tau_{j}$  channel.

# Acknowledgments

I am grateful to Ligong Bian, Peisi Huang and Zhen Liu for the useful discussions. I also thank Huai-Ke Guo for the discussion about the sound wave period of GWs. This work is supported by the Grant Korea NRF-2019R1C1C1010050.

# A The complete one-loop scalar potential

The one-loop Coleman Weinberg potential in  $\overline{\mathrm{MS}}$  scheme is

$$
V _ {\mathrm {C W}} = \sum_ {j} n _ {j} \frac {m _ {j} ^ {4}}{6 4 \pi^ {2}} \left(\ln \frac {m _ {j} ^ {2}}{\mu^ {2}} - C _ {j}\right), \tag {A.1}
$$

where the subscript  $j$  runs over all particles of the model, and he field-dependent masses are

$$
m _ {h} ^ {2} = \mu_ {H} ^ {2} + 3 \lambda_ {H} h ^ {2} + \lambda_ {H S} S ^ {2}, m _ {S} ^ {2} = \mu_ {S} ^ {2} + 3 \lambda_ {S} S ^ {2} + \lambda_ {H S} h ^ {2}, m _ {h S} ^ {2} = 2 \lambda_ {H S} h S,
$$

$$
m _ {G ^ {\pm , 0}} ^ {2} = \mu_ {H} ^ {2} + \lambda_ {H} h ^ {2} + \lambda_ {H S} S ^ {2}, \tag {A.2}
$$

for the scalars (where  $G^{\pm,0}$  denote the Goldstone modes of the Higgs doublet) and

$$
m _ {W} ^ {2} = \frac {g ^ {2}}{4} h ^ {2}, \quad m _ {Z} ^ {2} = \frac {g ^ {2} + g ^ {\prime 2}}{4} h ^ {2}, \quad m _ {t} ^ {2} = \frac {y _ {t} ^ {2}}{2} h ^ {2}. \tag {A.3}
$$

for the gauge bosons and the top quark. The numerical factors are

$$
\left\{ \begin{array}{l l} n _ {j} = 1, & C _ {j} = 3 / 2, \quad \text {f o r s c a l a r f i e l d s}; \\ n _ {j} = 3, & C _ {j} = 5 / 6, \quad \text {f o r v e c t o r f i e l d s}; \\ n _ {j} = - 4 N _ {c}, & C _ {j} = 3 / 2, \quad \text {f o r D i r a c f e r m i o n s}, \end{array} \right. \tag {A.4}
$$

where  $N_{c}$  is the color number, which is 3 for a quark and 1 for a lepton. For our numerical study, the renormalization scale is chosen as the top mass, i.e.  $\mu = M_t = 173.2\mathrm{GeV}$ .

The counter term is defined as

$$
V _ {\mathrm {C T}} = \frac {\delta \mu_ {H} ^ {2}}{2} h ^ {2} + \frac {\delta \mu_ {S} ^ {2}}{2} S ^ {2} + \frac {\delta \lambda_ {H}}{4} h ^ {4} + \frac {\delta \lambda_ {S}}{4} S ^ {4} + \frac {\delta \lambda_ {H S}}{2} h ^ {2} S ^ {2}. \tag {A.5}
$$

We choose the following renormalization conditions,

$$
\left. \left(V _ {\mathrm {C W}} + V _ {\mathrm {C T}}\right) \right| _ {(0, w)} = 0, \quad \left. \frac {\partial \left(V _ {\mathrm {C W}} + V _ {\mathrm {C T}}\right)}{\partial h} \right| _ {(v, 0)} = \left. \frac {\partial \left(V _ {\mathrm {C W}} + V _ {\mathrm {C T}}\right)}{\partial S} \right| _ {(0, w)} = 0,
$$

$$
\left. \frac {\partial^ {2} \left(V _ {\mathrm {C W}} + V _ {\mathrm {C T}}\right)}{\partial h ^ {2}} \right| _ {(v, 0)} = \left. \frac {\partial^ {2} \left(V _ {\mathrm {C W}} + V _ {\mathrm {C T}}\right)}{\partial S ^ {2}} \right| _ {(v, 0)} = 0, \tag {A.6}
$$

to determine the coefficients in eq. (A.5), such that the tree-level relations in eq. (2.4) and eq. (2.5) still hold at one-loop level.

The thermal integral correction is

$$
\tilde {V} _ {T} = \sum_ {j} n _ {j} \frac {T ^ {4}}{2 \pi^ {2}} J _ {j} \left(\frac {m _ {j} ^ {2}}{T ^ {2}}\right), \tag {A.7}
$$

where  $j$  again runs over all particles and  $m_j$  again is the field-dependent mass given in last subsection. The thermal integral are

$$
J _ {B / F} (y) = \int_ {0} ^ {\infty} x ^ {2} d x \ln \left(1 \mp e ^ {- \sqrt {x ^ {2} + y}}\right), \tag {A.8}
$$

where  $B / F$  is for bosons/fermions. Finally, the daisy resummation term is

$$
V _ {\text {d a i s y}} = - \sum_ {j ^ {\prime}} \frac {T}{1 2 \pi} \left[ \left(m _ {j ^ {\prime}} ^ {T}\right) ^ {3} - m _ {j ^ {\prime}} ^ {3} \right], \tag {A.9}
$$

where  $j'$  runs over the scalars and longitudinal modes of the vector bosons, and  $m_{j'}^T$  is the Debye mass whose expression can be found in refs. [43, 102].

For  $m_j^2 /T^2\lesssim 2$  , the thermal integrals can be approximated as

$$
\frac {T ^ {4}}{2 \pi^ {2}} J _ {B} \left(\frac {m _ {j} ^ {2}}{T ^ {2}}\right) \approx \frac {T ^ {2}}{2 4} m _ {j} ^ {2}, \quad \frac {T ^ {4}}{2 \pi^ {2}} J _ {F} \left(\frac {m _ {j} ^ {2}}{T ^ {2}}\right) \approx - \frac {T ^ {2}}{4 8} m _ {j} ^ {2}. \tag {A.10}
$$

Using this expansion, and ignoring the Coleman-Weinberg potential, the counter terms and the daisy resummation, we can get the leading  $T^2$  approximation for  $V_T$ , i.e. eq. (2.8).

# B Coefficients in the Boltzmann equations

In this appendix we list the definitions of the coefficients exist in the transport equation eq. (2.24). The  $k_{i}$  coefficients are given by [28, 103]

$$
k _ {i} = \tilde {k} _ {i} \frac {c _ {B / F}}{\pi^ {2}} \int_ {a _ {i}} ^ {\infty} d x \frac {x e ^ {x}}{(e ^ {x} \mp 1) ^ {2}} \sqrt {x ^ {2} - a _ {i} ^ {2}}, \tag {B.1}
$$

where the upper/ lower sign is for bosons/fermions,  $c_{B / F} = 3$  or 6 for bosons/fermions,  $\tilde{k}_i$  is the physical degrees of freedom in a multiplet ( $\tilde{k}_h = 4$ ,  $\tilde{k}_{\ell} = 2$  and  $\tilde{k}_{\tau} = 1$  in our scenario),

and  $a_{i} = \sqrt{\mathrm{Re}[\delta m_{i}^{2}(T_{n})] / T_{n}}$ , with the real part of the thermal masses being [104]

$$
\mathrm {R e} [ \delta m _ {h} ^ {2} (T) ] = \left[ \frac {3}{1 6} g ^ {2} + \frac {1}{1 6} g ^ {\prime 2} + \frac {1}{1 2} \sum_ {j} \left(y _ {e ^ {j}} ^ {2} + 3 y _ {u ^ {j}} ^ {2} + 3 y _ {d ^ {j}} ^ {2}\right) \right] T ^ {2},
$$

$$
\mathrm {R e} [ \delta m _ {\ell} ^ {2} (T) ] = \left(\frac {3}{3 2} g ^ {2} + \frac {1}{3 2} g ^ {\prime 2} + \frac {1}{1 6} y _ {\tau} ^ {2}\right) T ^ {2},
$$

$$
\operatorname {R e} \left[ \delta m _ {\tau} ^ {2} (T) \right] = \left(\frac {1}{8} g ^ {\prime 2} + \frac {1}{8} y _ {\tau} ^ {2}\right) T ^ {2}. \tag {B.2}
$$

The interactions rates in eq. (2.24) are [103]

$$
\begin{array}{l} \Gamma_ {M} = \frac {3}{\pi^ {2} T _ {n} ^ {3}} | \bar {m} _ {\tau} | ^ {2} \int_ {0} ^ {\infty} \frac {k ^ {2} d k}{\omega_ {L} \omega_ {R}} \times \\ \mathrm {I m} \left[ \frac {h _ {F} (\epsilon_ {R}) + h _ {F} (\epsilon_ {L})}{\epsilon_ {R} + \epsilon_ {L}} \left(\epsilon_ {L} \epsilon_ {R} + k ^ {2}\right) - \frac {h _ {F} (\epsilon_ {R} ^ {*}) + h _ {F} (\epsilon_ {L})}{\epsilon_ {R} ^ {*} - \epsilon_ {L}} \left(\epsilon_ {L} \epsilon_ {R} ^ {*} - k ^ {2}\right) \right], \quad \mathrm {(B . 3)} \\ \end{array}
$$

and

$$
\begin{array}{l} \Gamma_ {Y} = \frac {3 y _ {\tau} ^ {2}}{4 \pi^ {3} T _ {n} ^ {2}} (m _ {h} ^ {2} - m _ {\ell} ^ {2} - m _ {\tau} ^ {2}) \int_ {m _ {\tau}} ^ {\infty} d \omega_ {R} h _ {F} (\omega_ {R}) \ln \left(\frac {e ^ {\omega_ {R} / T _ {n}} + e ^ {\omega_ {-} / T _ {n}}}{e ^ {\omega_ {R} / T _ {n}} + e ^ {\omega_ {+} / T _ {n}}} \frac {e ^ {\omega_ {+} / T _ {n}} - 1}{e ^ {\omega_ {-} / T _ {n}} - 1}\right) \\ + \frac {1 . 2 0 2}{6 \pi^ {3}} g _ {s} ^ {2} y _ {\tau} ^ {2} T _ {n} \ln \left(\frac {8 T _ {n} ^ {2}}{m _ {\ell} ^ {2}}\right), \tag {B.4} \\ \end{array}
$$

where  $\bar{m}_{\tau}$  is the effective mass in eq. (2.22),  $m_{\ell, \tau, h}^{2}$  are short for the thermal masses in eq. (B.2), and

$$
\begin{array}{l} \omega_ {\pm} = \frac {1}{2 m _ {\tau} ^ {2}} \Big [ \omega_ {R} | m _ {h} ^ {2} + m _ {\tau} ^ {2} - m _ {\ell} ^ {2} | \\ \left. \pm \sqrt {(\omega_ {R} ^ {2} - m _ {\tau} ^ {2}) (m _ {\tau} ^ {2} - (m _ {\ell} + m _ {h}) ^ {2}) (m _ {\tau} ^ {2} - (m _ {\ell} - m _ {h}) ^ {2})} \right]. \qquad (\mathrm {B . 5}) \\ \end{array}
$$

The  $\omega_{R / L}$  and  $\epsilon_{R / L}$  functions are

$$
\omega_ {R / L} (\mathbf {k}) = \sqrt {| \mathbf {k} | ^ {2} + \operatorname {R e} [ \delta m _ {\tau / \ell} ^ {2} (T) ]}, \quad \epsilon_ {R / L} (\mathbf {k}) = \omega_ {R / L} (\mathbf {k}) - i \Gamma_ {\tau}, \tag {B.6}
$$

where  $\Gamma_{\tau} \approx 0.002T_{n}$  [105]. The  $n_F$  and  $h_F$  functions are

$$
n _ {F} \left(k _ {0}\right) = \frac {1}{e ^ {k _ {0} / T _ {n}} + 1}, \quad h _ {F} \left(k _ {0}\right) = \frac {e ^ {k _ {0} / T _ {n}}}{\left(e ^ {k _ {0} / T _ {n}} + 1\right) ^ {2}}. \tag {B.7}
$$

Finally, the factor  $J_{\tau}$  in the CPV source of eq. (2.25) is given by [79, 103, 106]

$$
J _ {\tau} = \int_ {0} ^ {\infty} \frac {d ^ {2} d k}{\omega_ {L} \omega_ {R}} \mathrm {I m} \left[ \frac {n _ {F} (\epsilon_ {L}) - n _ {F} (\epsilon_ {R} ^ {*})}{(\epsilon_ {L} - \epsilon_ {R} ^ {*}) ^ {2}} (\epsilon_ {L} \epsilon_ {R} ^ {*} - k ^ {2}) + \frac {n _ {F} (\epsilon_ {L}) + n _ {F} (\epsilon_ {R})}{(\epsilon_ {L} + \epsilon_ {R}) ^ {2}} (\epsilon_ {L} \epsilon_ {R} + k ^ {2}) \right]. \qquad (B. 8)
$$

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] PARTICLE DATA GROUP collaboration, Review of Particle Physics, Phys. Rev. D 98 (2018) 030001 [INSPIRE].  
[2] A.D. Sakharov, Violation of CP Invariance, C asymmetry, and baryon asymmetry of the universe, Sov. Phys. Usp. 34 (1991) 392 [INSPIRE].  
[3] V. Kuzmin, Cp violation and baryon asymmetry of the universe, Pisma Zh. Eksp. Teor. Fiz. 12 (1970) 335.  
[4] A.Y. Ignatiev, N.V. Krasnikov, V.A. Kuzmin and A.N. Tavkhelidze, Universal CP Noninvariant Superweak Interaction and Baryon Asymmetry of the Universe, Phys. Lett. B 76 (1978) 436 [INSPIRE].  
[5] K. Rummukainen, M. Tsypin, K. Kajantie, M. Laine and M.E. Shaposhnikov, The Universality class of the electroweak theory, Nucl. Phys. B 532 (1998) 283 [hep-lat/9805013] [INSPIRE].  
[6] D. Bödeker and W. Buchmüller, Baryogenesis from the weak scale to the GUT scale, arXiv:2009.07294 [INSPIRE].  
[7] D.E. Morrissey and M.J. Ramsey-Musolf, Electroweak baryogenesis, New J. Phys. 14 (2012) 125003 [arXiv:1206.2942] [INSPIRE].  
[8] J.M. Cline, Baryogenesis, in Les Houches Summer School — Session 86: Particle Physics and Cosmology: The Fabric of Spacetime, (2006) [hep-ph/0609145] [INSPIRE].  
[9] M. Trodden, Electroweak baryogenesis, Rev. Mod. Phys. 71 (1999) 1463 [hep-ph/9803479] [INSPIRE].  
[10] N. Arkani-Hamed, T. Han, M. Mangano and L.-T. Wang, Physics opportunities of a 100 TeV proton-proton collider, Phys. Rept. 652 (2016) 1 [arXiv:1511.06495] [INSPIRE].  
[11] A. Mazumdar and G. White, Review of cosmic phase transitions: their significance and experimental signatures, Rept. Prog. Phys. 82 (2019) 076901 [arXiv:1811.01948] [INSPIRE].  
[12] M. Joyce, T. Prokopec and N. Turok, Electroweak baryogenesis from a classical force, Phys. Rev. Lett. 75 (1995) 1695 [Erratum ibid. 75 (1995) 3375] [hep-ph/9408339] [INSPIRE].  
[13] M. Joyce, T. Prokopec and N. Turok, Nonlocal electroweak baryogenesis. Part 2: The Classical regime, Phys. Rev. D 53 (1996) 2958 [hep-ph/9410282] [INSPIRE].  
[14] L. Fromme and S.J. Huber, Top transport in electroweak baryogenesis, JHEP 03 (2007) 049 [hep-ph/0604159] [INSPIRE].  
[15] M. Jiang, L. Bian, W. Huang and J. Shu, Impact of a complex singlet: Electroweak baryogenesis and dark matter, Phys. Rev. D 93 (2016) 065032 [arXiv:1502.07574] [INSPIRE].  
[16] S. Bruggisser, B. Von Harling, O. Matsedonskyi and G. Servant, Baryon Asymmetry from a Composite Higgs Boson, Phys. Rev. Lett. 121 (2018) 131801 [arXiv:1803.08546] [INSPIRE].  
[17] W. Chao and Y. Liu, CP violation in the top-assisted electroweak baryogenesis, arXiv:1910.09303 [INSPIRE].

[18] S.A.R. Ellis, S. Ipek and G. White, Electroweak Baryogenesis from Temperature-Varying Couplings, JHEP 08 (2019) 002 [arXiv:1905.11994] [INSPIRE].  
[19] S. De Curtis, L. Delle Rose and G. Panico, Composite Dynamics in the Early Universe, JHEP 12 (2019) 149 [arXiv:1909.07894] [INSPIRE].  
[20] J.M. Cline and K. Kainulainen, Electroweak baryogenesis at high bubble wall velocities, Phys. Rev. D 101 (2020) 063525 [arXiv:2001.00568] [INSPIRE].  
[21] K.-P. Xie, L. Bian and Y. Wu, Electroweak baryogenesis and gravitational waves in a composite Higgs model with high dimensional fermion representations, JHEP 12 (2020) 047 [arXiv:2005.13552] [INSPIRE].  
[22] T. Modak and E. Senaha, Electroweak baryogenesis via bottom transport, Phys. Rev. D 99 (2019) 115022 [arXiv:1811.08088] [INSPIRE].  
[23] T. Modak and E. Senaha, Probing Electroweak Baryogenesis induced by extra bottom Yukawa coupling via EDMs and collider signatures, JHEP 11 (2020) 025 [arXiv:2005.09928] [INSPIRE].  
[24] S. Bruggisser, B. Von Harling, O. Matsedonskyi and G. Servant, Electroweak Phase Transition and Baryogenesis in Composite Higgs Models, JHEP 12 (2018) 099 [arXiv:1804.07314] [INSPIRE].  
[25] J. De Vries, M. Postma and J. van de Vis, The role of leptons in electroweak baryogenesis, JHEP 04 (2019) 024 [arXiv:1811.11104] [INSPIRE].  
[26] M. Joyce, T. Prokopec and N. Turok, Efficient electroweak baryogenesis from lepton transport, Phys. Lett. B 338 (1994) 269 [hep-ph/9401352] [INSPIRE].  
[27] V. Cirigliano, W. Dekens, J. de Vries and E. Mereghetti, Constraining the top-Higgs sector of the Standard Model Effective Field Theory, Phys. Rev. D 94 (2016) 034031 [arXiv:1605.04311] [INSPIRE].  
[28] J. de Vries, M. Postma, J. van de Vis and G. White, Electroweak Baryogenesis and the Standard Model Effective Field Theory, JHEP 01 (2018) 089 [arXiv:1710.04061] [INSPIRE].  
[29] J.R. Espinosa, B. Gripaios, T. Konstandin and F. Riva, Electroweak Baryogenesis in Non-minimal Composite Higgs Models, JCAP 01 (2012) 012 [arXiv:1110.2876] [INSPIRE].  
[30] G.F. Giudice and M.E. Shaposhnikov, *Strong sphalerons and electroweak baryogenesis*, Phys. Lett. B 326 (1994) 118 [hep-ph/9311367] [INSPIRE].  
[31] S. Tulin and P. Winslow, Anomalous B meson mixing and baryogenesis, Phys. Rev. D 84 (2011) 034013 [arXiv:1105.2848] [INSPIRE].  
[32] J. Brod, U. Haisch and J. Zupan, Constraints on CP-violating Higgs couplings to the third generation, JHEP 11 (2013) 180 [arXiv:1310.1385] [INSPIRE].  
[33] M. Joyce, T. Prokopec and N. Turok, Nonlocal electroweak baryogenesis. Part 1: Thin wall regime, Phys. Rev. D 53 (1996) 2930 [hep-ph/9410281] [INSPIRE].  
[34] D.J.H. Chung, B. Garbrecht, M.J. Ramsey-Musolf and S. Tulin, Yukawa Interactions and Supersymmetric Electroweak Baryogenesis, Phys. Rev. Lett. 102 (2009) 061301 [arXiv:0808.1144] [INSPIRE].  
[35] D.J.H. Chung, B. Garbrecht, M.J. Ramsey-Musolf and S. Tulin, Lepton-mediated electroweak baryogenesis, Phys. Rev. D 81 (2010) 063506 [arXiv:0905.4509] [INSPIRE].

[36] C.-W. Chiang, K. Fuyuto and E. Senaha, Electroweak Baryogenesis with Lepton Flavor Violation, Phys. Lett. B 762 (2016) 315 [arXiv:1607.07316] [INSPIRE].  
[37] H.-K. Guo, Y.-Y. Li, T. Liu, M. Ramsey-Musolf and J. Shu, Lepton-Flavored Electroweak Baryogenesis, Phys. Rev. D 96 (2017) 115034 [arXiv:1609.09849] [INSPIRE].  
[38] E. Fuchs, M. Losada, Y. Nir and Y. Viernik,  $CP$  violation from  $\tau$ ,  $t$  and  $b$  dimension-6 Yukawa couplings — interplay of baryogenesis, EDM and Higgs physics, JHEP 05 (2020) 056 [arXiv:2003.00099] [INSPIRE].  
[39] E. Fuchs, M. Losada, Y. Nir and Y. Viernik, Implications of the Upper Bound on  $h \to \mu^{+} \mu^{-}$  on the Baryon Asymmetry of the Universe, Phys. Rev. Lett. 124 (2020) 181801 [arXiv:1911.08495] [INSPIRE].  
[40] E. Fernández-Martínez, J. López-Pavón, T. Ota and S. Rosauro-Alcaraz,  $\nu$  electroweak baryogenesis, JHEP 10 (2020) 063 [arXiv:2007.11008] [INSPIRE].  
[41] J. McDonald, Electroweak baryogenesis and dark matter via a gauge singlet scalar, Phys. Lett. B 323 (1994) 339 [INSPIRE].  
[42] S. Profumo, M.J. Ramsey-Musolf and G. Shaughnessy, Singlet Higgs phenomenology and the electroweak phase transition, JHEP 08 (2007) 010 [arXiv:0705.2425] [INSPIRE].  
[43] J.R. Espinosa, T. Konstandin and F. Riva, *Strong Electroweak Phase Transitions in the Standard Model with a Singlet*, Nucl. Phys. B 854 (2012) 592 [arXiv:1107.5441] [INSPIRE].  
[44] J.M. Cline and K. Kainulainen, Electroweak baryogenesis and dark matter from a singlet Higgs, JCAP 01 (2013) 012 [arXiv:1210.4196] [INSPIRE].  
[45] T. Alanne, K. Tuominen and V. Vaskonen, *Strong phase transition, dark matter and vacuum stability from simple hidden sectors*, Nucl. Phys. B 889 (2014) 692 [arXiv:1407.0688] [INSPIRE].  
[46] V. Vaskonen, Electroweak baryogenesis and gravitational waves from a real scalar singlet, Phys. Rev. D 95 (2017) 123515 [arXiv:1611.02073] [INSPIRE].  
[47] F.P. Huang, Z. Qian and M. Zhang, Exploring dynamical CP-violation induced baryogenesis by gravitational waves and colliders, Phys. Rev. D 98 (2018) 015014 [arXiv:1804.06813] [INSPIRE].  
[48] W. Cheng and L. Bian, From inflation to cosmological electroweak phase transition with a complex scalar singlet, Phys. Rev. D 98 (2018) 023524 [arXiv:1801.00662] [INSPIRE].  
[49] T. Alanne, T. Hugle, M. Platscher and K. Schmitz, A fresh look at the gravitational-wave signal from cosmological phase transitions, JHEP 03 (2020) 004 [arXiv:1909.11356] [INSPIRE].  
[50] O. Gould, J. Kozaczuk, L. Niemi, M.J. Ramsey-Musolf, T.V.I. Tenkanen and D.J. Weir, Nonperturbative analysis of the gravitational waves from a first-order electroweak phase transition, Phys. Rev. D 100 (2019) 115024 [arXiv:1903.11604] [INSPIRE].  
[51] M. Carena, Z. Liu and Y. Wang, Electroweak phase transition with spontaneous  $Z_{2}$ -breaking, JHEP 08 (2020) 107 [arXiv:1911.10206] [INSPIRE].  
[52] L. Bian, Y. Wu and K.-P. Xie, Electroweak phase transition with composite Higgs models: calculability, gravitational waves and collider searches, JHEP 12 (2019) 028 [arXiv:1909.02014] [INSPIRE].  
[53] L. Dolan and R. Jackiw, Symmetry Behavior at Finite Temperature, Phys. Rev. D 9 (1974) 3320 [INSPIRE].

[54] A.D. Linde, Decay of the False Vacuum at Finite Temperature, Nucl. Phys. B 216 (1983) 421 [Erratum ibid. 223 (1983) 544] [INSPIRE].  
[55] M. Quiros, Finite temperature field theory and phase transitions, in ICTP Summer School in High-Energy Physics and Cosmology, pp. 187-259 (1999) [hep-ph/9901312] [INSPIRE].  
[56] G.D. Moore, Measuring the broken phase sphaleron rate nonperturbatively, Phys. Rev. D 59 (1999) 014503 [hep-ph/9805264] [INSPIRE].  
[57] R. Zhou, L. Bian and H.-K. Guo, Connecting the electroweak sphaleron with gravitational waves, Phys. Rev. D 101 (2020) 091903 [arXiv:1910.00234] [INSPIRE].  
[58] C.L. Wainwright, Cosmo Transitions: Computing Cosmological Phase Transition Temperatures and Bubble Profiles with Multiple Fields, Comput. Phys. Commun. 183 (2012) 2006 [arXiv:1109.4189] [INSPIRE].  
[59] LISA collaboration, Laser Interferometer Space Antenna, arXiv:1702.00786 [INSPIRE].  
[60] J. Crowder and N.J. Cornish, Beyond LISA: Exploring future gravitational wave missions, Phys. Rev. D 72 (2005) 083005 [gr-qc/0506015] [INSPIRE].  
[61] TIANQIN collaboration, TianQin: a space-borne gravitational wave detector, Class. Quant. Grav. 33 (2016) 035010 [arXiv:1512.02076] [INSPIRE].  
[62] Y.-M. Hu, J. Mei and J. Luo, Science prospects for space-borne gravitational-wave missions, Natl. Sci. Rev. 4 (2017) 683 [INSPIRE].  
[63] W.-R. Hu and Y.-L. Wu, The Taiji Program in Space for gravitational wave physics and the nature of gravity, Natl. Sci. Rev. 4 (2017) 685 [INSPIRE].  
[64] W.-H. Ruan, Z.-K. Guo, R.-G. Cai and Y.-Z. Zhang, *Taiji program: Gravitational-wave sources*, Int. J. Mod. Phys. A 35 (2020) 2050075 [arXiv:1807.09495] [INSPIRE].  
[65] S. Kawamura et al., The Japanese space gravitational wave antenna: DECIGO, Class. Quant. Grav. 28 (2011) 094011 [INSPIRE].  
[66] S. Kawamura et al., The Japanese space gravitational wave antenna DECIGO, Class. Quant. Grav. 23 (2006) S125 [INSPIRE].  
[67] J. Ellis, M. Lewicki and J.M. No, On the Maximal Strength of a First-Order Electroweak Phase Transition and its Gravitational Wave Signal, JCAP 04 (2019) 003 [arXiv:1809.08242] [INSPIRE].  
[68] C. Grojean and G. Servant, Gravitational Waves from Phase Transitions at the Electroweak Scale and Beyond, Phys. Rev. D 75 (2007) 043507 [hep-ph/0607107] [INSPIRE].  
[69] C. Caprini et al., Science with the space-based interferometer eLISA. II: Gravitational waves from cosmological phase transitions, JCAP 04 (2016) 001 [arXiv:1512.06239] [INSPIRE].  
[70] C. Caprini et al., Detecting gravitational waves from cosmological phase transitions with LISA: an update, JCAP 03 (2020) 024 [arXiv:1910.13125] [INSPIRE].  
[71] J.R. Espinosa, T. Konstandin, J.M. No and G. Servant, Energy Budget of Cosmological First-order Phase Transitions, JCAP 06 (2010) 028 [arXiv:1004.4187] [INSPIRE].  
[72] X. Wang, F.P. Huang and X. Zhang, The energy budget and the gravitational wave spectra beyond the bag model, arXiv:2010.13770 [INSPIRE].  
[73] A. Megevand and S. Ramirez, Bubble nucleation and growth in very strong cosmological phase transitions, Nucl. Phys. B 919 (2017) 74 [arXiv:1611.05853] [INSPIRE].

[74] A. Kobakhidze, C. Lagger, A. Manning and J. Yue, Gravitational waves from a supercooled electroweak phase transition and their detection with pulsar timing arrays, Eur. Phys. J. C 77 (2017) 570 [arXiv:1703.06552] [INSPIRE].  
[75] J. Ellis, M. Lewicki and J.M. No, Gravitational waves from first-order cosmological phase transitions: lifetime of the sound wave source, JCAP 07 (2020) 050 [arXiv:2003.07360] [INSPIRE].  
[76] X. Wang, F.P. Huang and X. Zhang, Phase transition dynamics and gravitational wave spectra of strong first-order phase transition in supercooled universe, JCAP 05 (2020) 045 [arXiv:2003.08892] [INSPIRE].  
[77] H.-K. Guo, K. Sinha, D. Vagie and G. White, Phase Transitions in an Expanding Universe: Stochastic Gravitational Waves in Standard and Non-Standard Histories, JCAP 01 (2021) 001 [arXiv:2007.08537] [INSPIRE].  
[78] J.M. No, Large Gravitational Wave Background Signals in Electroweak Baryogenesis Scenarios, Phys. Rev. D 84 (2011) 124025 [arXiv:1103.2159] [INSPIRE].  
[79] C. Lee, V. Cirigliano and M.J. Ramsey-Musolf, Resonant relaxation in electroweak baryogenesis, Phys. Rev. D 71 (2005) 075010 [hep-ph/0412354] [INSPIRE].  
[80] M. D'Onofrio, K. Rummukainen and A. Tranberg, Sphaleron Rate in the Minimal Standard Model, Phys. Rev. Lett. 113 (2014) 141602 [arXiv:1404.3565] [INSPIRE].  
[81] T. Konstandin, G. Nardini and I. Rues, From Boltzmann equations to steady wall velocities, JCAP 09 (2014) 028 [arXiv:1407.3132] [INSPIRE].  
[82] S. Profumo, M.J. Ramsey-Musolf, C.L. Wainwright and P. Winslow, Singlet-catalyzed electroweak phase transitions and precision Higgs boson studies, Phys. Rev. D 91 (2015) 035018 [arXiv:1407.5342] [INSPIRE].  
[83] Q.-H. Cao, F.P. Huang, K.-P. Xie and X. Zhang, Testing the electroweak phase transition in scalar extension models at lepton colliders, Chin. Phys. C 42 (2018) 023103 [arXiv:1708.04737] [INSPIRE].  
[84] A. Alves, T. Ghosh, H.-K. Guo and K. Sinha, Resonant Di-Higgs Production at Gravitational Wave Benchmarks: A Collider Study using Machine Learning, JHEP 12 (2018) 070 [arXiv:1808.08974] [INSPIRE].  
[85] L. Bian, H.-K. Guo, Y. Wu and R. Zhou, Gravitational wave and collider searches for electroweak symmetry breaking patterns, Phys. Rev. D 101 (2020) 035011 [arXiv:1906.11664] [INSPIRE].  
[86] N. Chen, T. Li, Y. Wu and L. Bian, Complementarity of the future  $e^+e^-$  colliders and gravitational waves in the probe of complex singlet extension to the standard model, Phys. Rev. D 101 (2020) 075047 [arXiv:1911.05579] [INSPIRE].  
[87] P. Huang, A.J. Long and L.-T. Wang, Probing the Electroweak Phase Transition with Higgs Factories and Gravitational Waves, Phys. Rev. D 94 (2016) 075008 [arXiv:1608.06619] [INSPIRE].  
[88] J. Kozaczuk, M.J. Ramsey-Musolf and J. Shelton, *Exotic Higgs boson decays and the electroweak phase transition*, Phys. Rev. D 101 (2020) 115035 [arXiv:1911.10210] [INSPIRE].  
[89] A. Papaefstathiou and G. White, The Electro-Weak Phase Transition at Colliders: Confronting Theoretical Uncertainties and Complementary Channels, arXiv:2010.00597 [INSPIRE].

[90] A. Alves, D. Gonçalves, T. Ghosh, H.-K. Guo and K. Sinha, Di-Higgs Blind Spots in Gravitational Wave Signals, arXiv:2007.15654 [INSPIRE].  
[91] FCC collaboration, HE-LHC: The High-Energy Large Hadron Collider: Future Circular Collider Conceptual Design Report Volume 4, Eur. Phys. J. ST 228 (2019) 1109 [INSPIRE].  
[92] A. Ashoorioon and T. Konstandin, *Strong electroweak phase transitions without collider traces*, JHEP 07 (2009) 086 [arXiv:0904.0353] [INSPIRE].  
[93] D. Curtin, P. Meade and C.-T. Yu, Testing Electroweak Baryogenesis with Future Colliders, JHEP 11 (2014) 127 [arXiv:1409.0005] [INSPIRE].  
[94] G. Bagliesi, Tau tagging at ATLAS and CMS, in 17th Symposium on Hadron Collider Physics 2006 (HCP 2006), 7, 2007 [arXiv:0707.0928] [INSPIRE].  
[95] ATLAS collaboration, Search for supersymmetry in events with four or more leptons in  $\sqrt{s} = 13$  TeV pp collisions with ATLAS, Phys. Rev. D 98 (2018) 032009 [arXiv:1804.03602] [INSPIRE].  
[96] A. Alloul, N.D. Christensen, C. Degrande, C. Duhr and B. Fuks, *FeynRules* 2.0 — A complete toolbox for tree-level phenomenology, *Comput. Phys. Commun.* **185** (2014) 2250 [arXiv:1310.1921] [INSPIRE].  
[97] C. Degrande, C. Duhr, B. Fuks, D. Grellscheid, O. Mattelaer and T. Reiter, UFO — The Universal FeynRules Output, Comput. Phys. Commun. 183 (2012) 1201 [arXiv:1108.2040] [INSPIRE].  
[98] J. Alwall et al., The automated computation of tree-level and next-to-leading order differential cross sections, and their matching to parton shower simulations, JHEP 07 (2014) 079 [arXiv:1405.0301] [INSPIRE].  
[99] T. Sjöstrand, S. Mrenna and P.Z. Skands, A Brief Introduction to PYTHIA 8.1, Comput. Phys. Commun. 178 (2008) 852 [arXiv:0710.3820] [INSPIRE].  
[100] DELPHES 3 collaboration, DELPHES 3, A modular framework for fast simulation of a generic collider experiment, JHEP 02 (2014) 057 [arXiv:1307.6346] [INSPIRE].  
[101] ATLAS collaboration, Search for new phenomena in events with same-charge leptons and b-jets in pp collisions at  $\sqrt{s} = 13$  TeV with the ATLAS detector, JHEP 12 (2018) 039 [arXiv:1807.11883] [INSPIRE].  
[102] M.E. Carrington, The Effective potential at finite temperature in the Standard Model, Phys. Rev. D 45 (1992) 2933 [INSPIRE].  
[103] E. Fuchs, M. Losada, Y. Nir and Y. Viernik, Analytic Techniques for Solving the Transport Equations in Electroweak Baryogenesis, arXiv:2007.06940 [INSPIRE].  
[104] K. Enqvist, A. Rietto and I. Vilja, Baryogenesis and the thermalization rate of stop, Phys. Lett. B 438 (1998) 273 [hep-ph/9710373] [INSPIRE].  
[105] P. Elmfors, K. Enqvist, A. Riotto and I. Vilja, Damping rates in the MSSM and electroweak baryogenesis, Phys. Lett. B 452 (1999) 279 [hep-ph/9809529] [INSPIRE].  
[106] V. Cirigliano, M.J. Ramsey-Musolf, S. Tulin and C. Lee, Yukawa and tri-scalar processes in electroweak baryogenesis, Phys. Rev. D 73 (2006) 115009 [hep-ph/0603058] [INSPIRE].