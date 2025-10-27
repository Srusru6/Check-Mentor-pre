PAPER

# Blazar-boosted dark matter at Super-Kamiokande

To cite this article: Alessandro Granelli et al JCAP07(2022)013

View the article online for updates and enhancements.

# You may also like

XENONnT and LUX-ZEPLIN constraints on DSNB-boosted dark matter Valentina De Romeri, Anirban Majumdar, Dimitrios K. Papoulias et al.  
- Simultaneous detection of boosted dark matter and neutrinos from the semiannihilation at DUNE Mayumi Aoki and Takashi Toma  
- Boosted self-interacting dark matter in a multi-component dark matter model Mayumi Aoki and Takashi Toma

# Blazar-boosted dark matter at Super-Kamiokande

Alessandro Granelli, Piero Ullio and Jin-Wei Wang

Scuola Internazionale Superiore di Studi Avanzati (SISSA), via Bonomea 265, 34136 Trieste, Italy

Istituto Nazionale di Fisica Nucleare (INFN), Sezione di Trieste, via Valerio 2, 34127 Trieste, Italy

Institute for Fundamental Physics of the Universe (IFPU), via Beirut 2, 34151 Trieste, Italy

E-mail: agranell@sissa.it, ullio@sissa.it, jinwwang@sissa.it

Received February 22, 2022

Revised April 27, 2022

Accepted June 2, 2022

Published July 7, 2022

Abstract. Dark matter particles near the center of a blazar, after being accelerated by the elastic collisions with relativistic electrons and protons in the blazar jet, can be energetic enough to trigger detectable signals at terrestrial detectors. In this work, focusing on the blazars TXS  $0506 + 056$  and BL Lacertae, we derive novel limits on the cross section of the elastic scattering between dark matter and electrons by means of the available Super-Kamiokande data. Thanks to the large blazar-boosted dark matter flux, the limit on the dark matter-electron scattering cross section for dark matter masses below  $100\mathrm{MeV}$  can be as low as  $\sim 10^{-38}\mathrm{cm}^2$ , that is orders of magnitude stronger than the analogous results from galactic cosmic rays.

Keywords: dark matter theory, dark matter experiments, active galactic nuclei

ArXiv ePrint: 2202.07598

# Contents

1 Introduction 1  
2 Blazar jet spectrum 2

3 Dark matter profile and flux from blazars 4

3.1 Dark matter density profile 4  
3.2 Blazar-boosted dark matter flux 6

4 Constraints on dark matter-electron scattering cross section 7

4.1 Data selection and analysis 7  
4.2 Bounds on scattering cross section 10

5 Conclusion 12

# 1 Introduction

The existence of dark matter (DM) has been established by solid astrophysical and cosmological observations, while its particle nature is still unknown [1, 2]. Assuming that DM has incredibly feeble interaction with ordinary matter, direct DM detection experiments (e.g. XENON1T [3, 4], PandaX-II [5]) are promising in detecting DM scatterings with target nuclei. However, for DM masses below  $\sim 1\mathrm{GeV}$ , the typical kinetic energy of DM in the local halo is not enough to imprint a recoil energy above the threshold of  $\sim 1\mathrm{keV}$ , thus leading to a rapid decrease in detection sensitivity. Nevertheless, DM in this mass region may still be energetic enough to trigger detectable electronic recoils thanks to a lower threshold ( $\sim 0.186\mathrm{keV}$  [6]), thus opening an alternative way to explore sub-GeV DM [6, 7]. Still, the search for DM interacting with electrons in direct detection setups inevitably faces the same problem for DM masses below  $\sim 10\mathrm{MeV}$  [6, 7].

In the past few years, to circumvent the limitations of light DM direct detection, some scenarios with "boosted" DM populations have been proposed [8-11]. For instance, in ref. [12] the authors put forward a novel idea for which DM particles in the local halo are accelerated via elastic collisions with galactic high-energy cosmic rays (CRs). This small but inevitable component of DM (dubbed CRDM) possesses enough energy to set constraints on the DM-proton interaction cross section  $(\sigma_{\chi p})$  for sub-GeV DM. Another similar study on CRDM-electron scattering at Super-Kamiokande (Super-K) can be found in refs. [13-15], where stringent constraints on DM-electron scattering cross section  $(\sigma_{\chi e})$  for DM masses down to  $\sim 1\mathrm{keV}$  are presented ( $\sigma_{\chi e} \lesssim 10^{-33}\mathrm{cm}^2$ ).

Recently, a new DM acceleration mechanism at blazars, referred to as Blazar-Boosted DM (BBDM), has been suggested [16]. Through the scatterings with high-energy protons in the jet of a blazar, DM particles can be boosted up to high velocities. Moreover, the existence of a supermassive Black Hole (BH) at the blazar center may provide a dense DM population [17]. The combination of these two distinguished characteristics makes blazars ideal DM boosters, that can induce a DM flux at Earth much stronger than that from galactic CRs. In ref. [16] the authors focused on the blazars TXS 0506+056 and BL Lacertae

and derived the corresponding constraints on  $\sigma_{\chi p}$  from the results of direct DM detectors (e.g. XENON1T [4]), as well as neutrino detectors (e.g. MiniBooNE [18] and Borexino [19]).

For the sake of simplicity, the authors of ref. [16] ignored the scattering between DM and electrons. However, it is actually intriguing to analyse the influence of DM-electron scattering for the following reasons. Firstly, the observations of the photon Spectral Energy Distribution (SED) of blazars clearly reveal two peaks, one in the infrared/X-ray bands and the other at  $\gamma$ -ray frequencies [20]. Different SED models agree that the low-energy peak is due to the synchrotron emission of electrons [21-27], suggesting that the electron component of the blazar jets is essential (see, e.g., [28] for a recent SED model review). Secondly, it provides a possible way to study the characteristics of blazar jet models and the nature of DM by searching for DM-electron recoil signals at ground detectors. Based on ref. [16], in this work we investigate the framework of BBDM from the blazars TXS 0506+056 and BL Lacertae. We activate the effects of  $\sigma_{\chi e}$  and calculate the corresponding constraints from Super-K observations. In particular, since the flux of BBDM can be much larger and extend to much higher energies than that of CRDM [16], we expect that more stringent constraints on  $\sigma_{\chi e}$  can be derived from Super-K results [13].

This work is organized as follows. In section 2 we compute the jet spectrum for the two blazars under consideration. In section 3, we calculate the DM density profile and estimate the BBDM flux. We devote section 4 to the computation of the constraints at Super-K and summarise our results in section 5.

# 2 Blazar jet spectrum

The jets of blazars can be well described by the "blob geometry" [29]: electrons and protons move isotropically in the blob frame with a power-law energy distribution, and, in the BH center-of-mass rest frame (also observer's frame), the blob itself moves along the jet axis with speed  $\beta_{B}$ . The corresponding Lorentz boost factor reads  $\Gamma_{B} \equiv (1 - \beta_{B}^{2})^{-1/2}$ . The misalignment angle between the jet axis and the observer's line-of-sight, hereafter denoted by  $\theta_{\mathrm{LOS}}$ , is usually of few degrees. The desired jet spectrum in the observer's frame can be derived from a Lorentz boost transformation and can be expressed as (see ref. [16] for a detailed derivation)

$$
\frac {d \Gamma_ {j}}{d T _ {j} d \Omega} = \frac {1}{4 \pi} c _ {j} \left(1 + \frac {T _ {j}}{m _ {j}}\right) ^ {- \alpha_ {j}} \frac {\beta_ {j} \left(1 - \beta_ {j} \beta_ {B} \mu\right) ^ {- \alpha_ {j}} \Gamma_ {B} ^ {- \alpha_ {j}}}{\sqrt {\left(1 - \beta_ {j} \beta_ {B} \mu\right) ^ {2} - \left(1 - \beta_ {j} ^ {2}\right) \left(1 - \beta_ {B} ^ {2}\right)}}, \tag {2.1}
$$

where the subscript  $j \in \{e, p\}$  refers either to electrons or protons with masses  $m_e \simeq 0.511 \mathrm{MeV}$  and  $m_p \simeq 0.938 \mathrm{GeV}$ , respectively,  $\alpha_j$  is the spectral power index,  $T_j$  and  $\beta_j = \left[1 - m_j^2 / (T_j + m_j)^2\right]^{1/2}$  are respectively the kinetic energy and speed of the particle,  $c_j$  is the normalisation constant that can be computed from the luminosity  $L_j$  (see further in eq. (2.2) and (2.3)),  $\mu$  is the cosine of the angle between the particle's direction of motion and the jet axis.

The relevant (Lepto-)Hadronic SED model parameters of TXS 0506+056 [30] and BL Lacertae [27] are summarized in table 1. The quantities  $\gamma_{\mathrm{min},j}^{\prime}$  and  $\gamma_{\mathrm{max},j}^{\prime}$  are the minimal and maximal Lorentz boost factors in the blob frame, while  $\mathcal{D} = [\Gamma_B(1 - \beta_B\cos \theta_{\mathrm{LOS}})]^{-1}$  is the Doppler factor. In practice, two different assumptions are commonly used in the blazar jet model fitting,  $\mathcal{D} = \Gamma_B$  or  $\mathcal{D} = 2\Gamma_B$ . For the first assumption,  $\theta_{\mathrm{LOS}}$  can be solved by using the definition of  $\mathcal{D}$ , while for the second assumption,  $\theta_{\mathrm{LOS}}$  is set to zero. In the same table,

Table 1. The model parameters for the blazars TXS  $0506 + 056$  (Lepto-Hadronic) [30] and BL Lacertae (Hadronic) [27] used in our calculations. The quantities flagged with a star  $(^{\star})$  correspond to mean values computed from the ranges given in the second column of table 1 of the erratum of ref. [30].<sup>a</sup> In the model fitting, the assumption of  $\mathcal{D} = 2\Gamma_B(\Gamma_B)$  is used for TXS  $0506 + 056$  (BL Lacertae). The resulting values of the normalisation constants  $c_{e,p}$ , as well as the redshift  $z$  [31, 32], luminosity distance  $d_L$ , and BH mass  $M_{\mathrm{BH}}$  [33, 34] for the two considered sources are also reported.  

<table><tr><td colspan="3">(Lepto-)Hadronic Model Parameters</td></tr><tr><td>Parameter (unit)</td><td>TXS 0506+056</td><td>BL Lacertae</td></tr><tr><td>z</td><td>0.337</td><td>0.069</td></tr><tr><td>dL (Mpc)</td><td>1835.4</td><td>322.7</td></tr><tr><td>MBH (M⊙)</td><td>3.09 × 108</td><td>8.65 × 107</td></tr><tr><td>D</td><td>40*</td><td>15</td></tr><tr><td>ΓB</td><td>20</td><td>15</td></tr><tr><td>θLOS (°)</td><td>0</td><td>3.82</td></tr><tr><td>αp</td><td>2.0</td><td>2.4</td></tr><tr><td>αe</td><td>2.0</td><td>3.5</td></tr><tr><td>γ′min,p</td><td>1.0</td><td>1.0</td></tr><tr><td>γ′max,p</td><td>5.5 × 107*</td><td>1.9 × 109</td></tr><tr><td>γ′min,e</td><td>500</td><td>700</td></tr><tr><td>γ′max,e</td><td>1.3 × 104*</td><td>1.5 × 104</td></tr><tr><td>Lp (erg/s)</td><td>2.55 × 1048*</td><td>9.8 × 1048</td></tr><tr><td>Le (erg/s)</td><td>1.32 × 1044*</td><td>8.7 × 1042</td></tr><tr><td>cp (s-1sr-1GeV-1)</td><td>2.54 × 1047</td><td>1.24 × 1049</td></tr><tr><td>ce (s-1sr-1GeV-1)</td><td>2.42 × 1050</td><td>2.59 × 1054</td></tr></table>

<sup>a</sup> Considering that these two sample blazars are BL Lac-type, which means their luminosity is time-dependent, we will briefly discuss how this can affect our final results in section 4.2.

the other relevant parameters of the considered blazars are also given, including the redshift  $z$  [31, 32], the luminosity distance  $d_{L}$ , and central BH mass  $M_{\mathrm{BH}}$  [33, 34], together with the specific values of the normalisation constant  $c_{j}$  appearing in eq. (2.1), that can be fixed via the relation [16, 35]

$$
L _ {j} = \int d \Omega \int d T _ {j} (T _ {j} + m _ {j}) \frac {d \Gamma_ {j}}{d T _ {j} d \Omega} = c _ {j} m _ {j} ^ {2} \Gamma_ {B} ^ {2} \int_ {\gamma_ {\min , j} ^ {\prime}} ^ {\gamma_ {\max , j} ^ {\prime}} d \gamma_ {j} ^ {\prime} (\gamma_ {j} ^ {\prime}) ^ {1 - \alpha_ {j}}, \qquad (2. 2)
$$

giving

$$
c _ {j} = \frac {L _ {j}}{m _ {j} ^ {2} \Gamma_ {B} ^ {2}} \times \left\{ \begin{array}{l l} (2 - \alpha_ {j}) / \left[ (\gamma_ {\max , j} ^ {\prime}) ^ {2 - \alpha_ {j}} - (\gamma_ {\min , j} ^ {\prime}) ^ {2 - \alpha_ {j}} \right] & \text {i f} \alpha_ {j} \neq 2; \\ 1 / \log \left(\gamma_ {\max , j} ^ {\prime} / \gamma_ {\min , j} ^ {\prime}\right) & \text {i f} \alpha_ {j} = 2. \end{array} \right. \tag {2.3}
$$

We note that  $\gamma_{\mathrm{min},e}^{\prime}\gg \Gamma_{B}$  for both sources, namely, the electrons are ultra-relativistic in the blob frame and remain so in the observer's frame. Therefore, we decide to adopt the approximation  $\beta_{e}\approx 1$

# 3 Dark matter profile and flux from blazars

# 3.1 Dark matter density profile

The adiabatic growth of a BH in the central region of a DM halo is expected to focus the distribution of DM particles, giving rise to a very dense spike. The idea was originally suggested by Gondolo and Silk [17] discussing the case for the BH at the center of the Milky Way (MW). Implementing angular momentum and radial action as adiabatic invariants, it was shown that an ergodic, self-gravitating, single power-law spherical DM profile  $\rho(r) \propto r^{-\gamma}$  is turned into a sensibly steeper profile [17]:

$$
\rho^ {\prime} (r) \propto r ^ {- \alpha} \quad \text {w i t h} \alpha = \frac {9 - 2 \gamma}{4 - \gamma}. \tag {3.1}
$$

Such process has, in particular, dramatic phenomenological implications for DM that can annihilate in pairs into Standard Model particles, since it would imply that the region around the MW BH is an extremely bright source for indirect DM detection signals. The effect can be so large that the pair annihilation itself may deplete the central DM density: considering this effect as a continuous loss since the time of the BH formation, and ignoring any replenishing from the surrounding environment, there is a maximum surviving DM density  $\rho_{\mathrm{core}} \simeq m_{\chi} / (\langle \sigma v \rangle_0 t_{\mathrm{BH}})$ , with  $\langle \sigma v \rangle_0$  being the DM annihilation cross section times relative velocity and  $t_{\mathrm{BH}}$  the BH lifetime. The DM profile would then take the final form [17]

$$
\rho_ {\mathrm {D M}} (r) = \frac {\rho^ {\prime} (r) \rho_ {\mathrm {c o r e}}}{\rho^ {\prime} (r) + \rho_ {\mathrm {c o r e}}}. \tag {3.2}
$$

Given its profound impact on thermal Weakly Interacting Massive Particles (WIMPs), the MW BH spike has been very closely scrutinized, discussing both the validity and implications of the assumptions leading to the spike formation, as well as effects possibly impacting on the spike after the formation. For instance, in ref. [36] it was shown that, if the dynamical time for DM particles is not much shorter than the BH formation time, going away from the adiabatic growth assumption to the opposite limit of BH appearing instantaneously, then the DM profile is much less focused. With an initial Navarro-Frenk-White (NFW) profile [37], for which  $\gamma = 1$ , this results in a profile with  $\alpha = 4/3$  rather than one with the slope  $\alpha = 7/3$  has predicted in eq. (3.1). Spherical symmetry is also crucial in the process, and its violation, e.g., by hierarchical mergers onto the central BH may lead to depletion of the central spike [36, 38] down to a weak power  $\alpha = 1/2$ . The authors of ref. [39] argued instead that the presence of an inner stellar cluster around the MW BH would relax, independently of the initial conditions, the DM spike into a "minicusp" with  $\alpha = 3/2$ ; this effect was included in the numerical model of ref. [40] which resulted in a less severe spike depletion.

In the cases under study, we are actually not in the position of describing the DM spikes around the BHs at the center of the considered blazars in terms of initial conditions prior the BHs' formations and up to their present configurations. We are forced to refer to a simplified model, encompassing however uncertainties mentioned above. In most of our results we will consider an initial NFW profile as modified within the Gondolo and Silk scenario according to eq. (3.1); to fix the normalisation condition for  $\rho'(r)$ , as in ref. [16], we consider the region within which the BH is expected to dominate the potential well even after the spike formation and set (in analogy to results in ref. [36])

$$
\int_ {4 R _ {S}} ^ {1 0 ^ {5} R _ {S}} 4 \pi r ^ {2} \rho^ {\prime} (r) d r \simeq M _ {\mathrm {B H}}, \tag {3.3}
$$

where  $R_{S}$  is the Schwarzschild radius of the central BH; DM particles within  $4R_{S}$  are captured by the BH, while  $10^{5}R_{S}$  is also the typical radius relevant for BH mass estimations [35]. At the same time, we include a DM depletion effect, which, for simplicity, is parameterised in terms of a DM pair annihilation rate and the expression in eq. (3.2). We will refer to three benchmark points (BMPs) [16]:

BMP1)  $\langle \sigma v\rangle_0 = 0$ , so that  $\rho_{\mathrm{core}}\rightarrow +\infty$  and  $\rho_{\mathrm{DM}} = \rho^{\prime}$ ;

BMP2)  $\langle \sigma v\rangle_0 = 10^{-28}\mathrm{cm}^3\mathrm{s}^{-1}$  and  $t_\mathrm{BH} = 10^9$  yr;

BMP3)  $\langle \sigma v\rangle_0 = 3\times 10^{-26}\mathrm{cm}^3\mathrm{s}^{-1}$  and  $t_\mathrm{BH} = 10^9$  yr.

The third benchmark with  $\langle \sigma v\rangle_0 = 3\times 10^{-26}\mathrm{cm}^3\mathrm{s}^{-1}$  corresponds nominally to the case of DM thermal relics, a regime however which is rather unlikely for the DM masses and interaction strengths considered in our analysis; it also drives, for most of the DM masses of our interest, to a DM core profile  $\rho_{\mathrm{core}}$  extending to larger radii with respect to the inner region considered in eq. (3.3). The case with  $\langle \sigma v\rangle_0 = 0$  would be appropriate, e.g., for asymmetric DM models [41-43], and corresponds more in general to scenarios in which no significant spike depletion effects are expected. The second benchmark stands in between.

The relevant quantity to derive the flux of BBDM is the DM line-of-sight integral  $\Sigma_{\mathrm{DM}}$  (see section 3.2), which is defined as [16]

$$
\Sigma_ {\mathrm {D M}} (r) \equiv \int_ {4 R _ {S}} ^ {r} \rho_ {\mathrm {D M}} (r ^ {\prime}) d r ^ {\prime}. \tag {3.4}
$$

Given that  $\Sigma_{\mathrm{DM}}(r)$  tends to a constant value for  $r \gtrsim 10$  pc [16] for the mass range of interest, we can factor the effects of the DM profile into  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}} \equiv \Sigma_{\mathrm{DM}}(r \simeq 10$  pc). In the left panel of figure 1 we show the behaviour of  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}} / m_{\chi}$  against  $m_{\chi}$  for TXS 0506+056 (purple) and BL Lacertae (green). For BMP1 (solid lines),  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}}$  is determined by the properties of the BH ( $\rho'(r)$ ) and independent of  $m_{\chi}$ , while for BMP2 (dashed lines) and BMP3 (dotted lines) the dominant contribution to  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}}$  comes from the core region where  $\rho_{\mathrm{core}} \propto m_{\chi}$ . In the right panel of figure 1, we illustrate the relationship between  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}} / m_{\chi}$  and  $\alpha$  for different BMPs, setting  $m_{\chi} = 10$  MeV (for different masses the plot is scaled). The solid vertical grey line marks the considered case of a Gondolo and Silk spike with slope  $\alpha = 7/3$  (i.e.  $\gamma = 1$ ). It is evident that a smaller choice of  $\alpha$  corresponds to an intermediate situation between the already considered cases. In the same plot we also depict how departures from an initial NFW profile, in connection to baryonic feedback models (see, e.g., [44-46]), would change the Gondolo and Silk scenario; two different initial conditions with  $\gamma = 0$  ( $\alpha = 9/4$ ) and  $\gamma = 2$  ( $\alpha = 5/2$ ) are marked by dotted vertical lines. It is clear from the figure that the variation of the initial slope in the range  $0 \leq \gamma \leq 2$  would only mildly affect the quantity  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}} / m_{\chi}$  for BMP1 by factors of few, while leaving the BMP2 and BMP3 cases roughly invariant.

![](images/010b36d6bde82640026822d2fce269e9ce6b6da8fefe8718490b59ba40b58713.jpg)  
Figure 1. The quantity  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}} / m_{\chi}$  as a function of  $m_{\chi}$  (left panel) and the slope  $\alpha$  (right panel) for BL Lacertae (green) and TXS 0506+056 (purple). The solid, dashed and dotted curves correspond to BMP1, BMP2 and BMP3, respectively. Note that the results shown in the right panel are obtained for  $m_{\chi} = 10\mathrm{MeV}$ . The vertical grey lines correspond, from left to right, to the cases of Gondolo and Silk spikes from initial profiles with  $\gamma = 0, 1$  (NFW) and 2, see eq. (3.1).

![](images/ae39c228246712f3f48250624f6e97e635f014ebd4fbf94b1523b01b31796cf9.jpg)

# 3.2 Blazar-boosted dark matter flux

Through elastic collisions, the relativistic electrons and protons in the jet of a blazar can speed up the neighbouring DM particles. Assuming an isotropic differential scattering cross section, the BBDM flux at Earth can be expressed as [16]

$$
\frac {d \Phi_ {\chi}}{d T _ {\chi}} = \frac {\sum_ {\mathrm {D M}} ^ {\mathrm {t o t}}}{2 \pi m _ {\chi} d _ {L} ^ {2}} \sum_ {j = e, p} \widetilde {\sigma} _ {\chi j} \int_ {0} ^ {2 \pi} d \phi_ {s} \int_ {T _ {j} ^ {\mathrm {m i n}} (T _ {\chi}, \phi_ {s})} ^ {T _ {j} ^ {\mathrm {m a x}} (T _ {\chi}, \phi_ {s})} \frac {d T _ {j}}{T _ {\chi} ^ {\mathrm {m a x}} (T _ {j})} \frac {d \Gamma_ {j}}{d T _ {j} d \Omega}, \qquad (3. 5)
$$

where we have summed over the contributions from electrons and protons. The angle  $\phi_s$  is the azimuth with respect to the line-of-sight, while the quantity  $T_{\chi}^{\mathrm{max}}$  is the maximal kinetic energy DM can have after the scattering, i.e. [12, 16, 47]

$$
T _ {\chi} ^ {\max } \left(T _ {j}\right) = \frac {T _ {j} ^ {2} + 2 m _ {j} T _ {j}}{T _ {j} + \left(m _ {j} + m _ {\chi}\right) ^ {2} / \left(2 m _ {\chi}\right)}. \tag {3.6}
$$

For the DM-proton cross section we assume:

$$
\widetilde {\sigma} _ {\chi p} = \sigma_ {\chi p} G ^ {2} (2 m _ {\chi} T _ {\chi} / \Lambda_ {p} ^ {2}), \tag {3.7}
$$

where  $\sigma_{\chi p}$  is the zero-momentum transfer DM-proton cross section and the form factor  $G(x^{2})\equiv 1 / (1 + x^{2})^{2}$  accounts for the internal structure of the proton, with  $\Lambda_p\simeq 0.77$  GeV [12]. There is no need for a form factor in the case of DM interaction with free electrons, thus  $\widetilde{\sigma}_{\chi e}\equiv \sigma_{\chi e}.$

If  $\theta_{\mathrm{LOS}} = 0$ , the system is symmetric around the line-of-sight and the integration over  $\phi_s$  appearing in eq. (2.1) is trivial. This is the case for the blazar TXS  $0506 + 056$  in the considered Lepto-Hadronic SED model (see table 1). If instead the jet is inclined with respect to the line-of-sight, the computation is complicated by the geometry, with the interval of integration and the jet spectrum depending, in general, on  $\phi_s$ . However, in the case of protons the situation is less involved as they can have arbitrary small energy in the blob frame ( $\gamma_{\mathrm{min},p}^{\prime} = 1$ ). Thus, the lower limit of integration for protons coincides with the minimal kinetic energy required for the scattering, namely

$$
T _ {p} ^ {\mathrm {m i n}} (T _ {\chi}) = \left(\frac {T _ {\chi}}{2} - m _ {p}\right) \left[ 1 \pm \sqrt {1 + \frac {(m _ {p} + m _ {\chi}) ^ {2}}{(T _ {\chi} - 2 m _ {p}) ^ {2}} \frac {2 T _ {\chi}}{m _ {\chi}}} \right]. \tag {3.8}
$$

where the  $+(-)$  applies for  $T_{\chi} \geq 2m_p$  ( $T_{\chi} < 2m_p$ ). Also, given that  $\gamma_{\max,p}^{\prime} \gg 1$  and that the proton spectrum is strongly attenuated at high energies, the integral over  $T_{p}$  in eq. (2.1) shows only mild dependency on the upper extreme of integration  $T_{p}^{\mathrm{max}}$ , which we therefore set at  $10^{7}\mathrm{GeV}$  with no appreciable loss of accuracy. Conversely, the electron case is more subtle and the extremes of integration result as solutions of kinematical constraints combined with other energy availability conditions (refer to ref. [16] for more details on the kinematics).

We plot in figure 2 the flux of BBDM computed numerically for the blazars TXS  $0506 + 056$  (left panel) and BL Lacertae (right panel). The solid and dashed lines are obtained for  $m_{\chi} = 1\mathrm{keV}$  and  $1\mathrm{MeV}$ , respectively. Note that all these results are derived by setting  $\sigma_{\chi p} = \sigma_{\chi e} = 10^{-30}\mathrm{cm}^2$ . For clarity, we have separated the contributions from protons (red) and electrons (blue). To underline the effects of the inclination angle, we also show the results of BBDM flux after artificially setting  $\theta_{\mathrm{LOS}} = 0$  for BL Lacertae (thinner lines). In the figure, the BBDM flux from electrons stop at  $T_{\chi}^{\max}(T_e = \overline{T}_e)\simeq 265.5\mathrm{GeV}$  for TXS  $0506 + 056$  and  $114.9\mathrm{GeV}$  ( $229.6\mathrm{GeV}$  if  $\theta_{\mathrm{LOS}}$  is set to zero) for BL Lacertae, with  $\overline{T}_e\simeq m_e[\gamma_{\max ,e}'\Gamma_B^{-1}(1 - \beta_B\cos \theta_{\mathrm{LOS}})^{-1} - 1]$  being the maximal kinetic energy of electrons along the line-of-sight. Moreover, it is clear from the plot that the BBDM flux from protons is much larger than that from electrons, even for the same cross section (i.e.  $\sigma_{\chi p} = \sigma_{\chi e}$ ), due to the fact that  $L_{p}\gg L_{e}$  in the SED models under consideration.

# 4 Constraints on dark matter-electron scattering cross section

# 4.1 Data selection and analysis

Recently, Super-K has performed a search for CRDM in its "electron elastic scatter-like" event with electron recoil energy  $T_{e} > 100 \mathrm{MeV}$  [13-15]. Due to the large volume (22.5 kt in fiducial volume) and long exposure time (2628.1 days), Super-K is an ideal detector to search for DM-electron scattering signals. In the analysis of ref. [13], because of the strong energy dependence of the atmospheric neutrino background, three energy bins were considered, namely  $0.1 < T_{e} / \mathrm{GeV} < 1.33$  (Bin1),  $1.33 < T_{e} / \mathrm{GeV} < 20$  (Bin2), and  $20 < T_{e} / \mathrm{GeV} < 10^{3}$  (Bin3). For each bin, the authors of ref. [13] give the total number of data events ( $N_{\mathrm{Data}}$ ), the Monte Carlo simulated atmospheric neutrino background ( $N_{\mathrm{Bkg}}$ ) and the signal efficiency ( $\epsilon_{\mathrm{sig}}$ ), as well as the spatial distribution of the events.

A BBDM particle can hit an electron in the Super-K water tank and imprint a detectable signal. We treat the electrons in the detector as free and at rest in the observer's frame. According to figure 2, the BBDM spectrum can extend to high-energy scales, so that we can expect the scattered electron in the detector to be strongly forward. Moreover, both TXS

![](images/0fce95245023d65cf950e7525873654e72f04c19bc6f34410c65744c29d745ad.jpg)  
Figure 2. The expected flux of BBDM from TXS  $0506 + 056$  (left panel) and BL Lacertae (right panel). The red (blue) curves represent the contribution from protons (electrons), while the solid and dashed curves correspond to  $m_{\chi} = 1\mathrm{keV}$  and  $1\mathrm{MeV}$ , respectively. For BL Lacertae, the thinner blue curves are obtained by artificially setting  $\theta_{\mathrm{LOS}} = 0$ . The truncation of the electron-induced BBDM flux is caused by electron energy limitations (see the text for further details). Note that all these results are derived for  $\sigma_{\chi p} = \sigma_{\chi e} = 10^{-30}\mathrm{cm}^2$  and BMP1 parameters.

![](images/432fff4fbd5d4a7063afa99799f0c60ed4715d91ba721cd333b09c778d4c6f16.jpg)

$0506 + 056$  and BL Lacertae can be treated as point sources. Therefore, by selecting signals from a proper "searching cone" in the direction of the source, we can get rid of most of the background and obtain a higher sensitivity.

After the collision, the probability distribution of the cosine of the scattering angle for the electron  $(\mu_{e})$  in the observer's frame can be expressed as (more detailed derivations can be found in ref. [16])

$$
P (\mu_ {e}; T _ {\chi}) = \frac {2 \mu_ {e} \gamma_ {\mathrm {c . m .}} ^ {2} (T _ {\chi}) \Theta (1 - \mu_ {e})}{[ \mu_ {e} ^ {2} + \gamma_ {\mathrm {c . m .}} ^ {2} (T _ {\chi}) (1 - \mu_ {e} ^ {2}) ] ^ {2}}, \tag {4.1}
$$

where

$$
\gamma_ {\mathrm {c . m .}} ^ {2} (T _ {\chi}) \equiv \frac {(T _ {\chi} + m _ {\chi} + m _ {e}) ^ {2}}{(m _ {\chi} + m _ {e}) ^ {2} + 2 m _ {e} T _ {\chi}} \tag {4.2}
$$

is the squared Lorentz boost factor of the center-of-mass and the Heaviside theta function  $\Theta$  ensures that  $0 \leq \mu_{e} \leq 1$ . From eqs. (4.1) and (4.2) follow that the larger  $T_{\chi}$  is, the more forward the motion of electron ( $\mu_{e} \rightarrow 1$ ) will be. For Bin1 and Bin2, a conservative half-opening angle of the searching cone ( $\delta$ ) can be derived by imposing

$$
P \left(\mu_ {e} > \cos \delta ; T _ {\chi} ^ {\min } \left(T _ {e} = T _ {l} ^ {\min }\right)\right) \gtrsim 0. 9 5, \tag {4.3}
$$

where  $T_{\chi}^{\mathrm{min}}(T_e)$  is defined as in eq. (3.8) with the substitutions  $\chi \rightarrow e$  and  $p \rightarrow \chi$ , and  $(l, T_l^{\mathrm{min}} / \mathrm{GeV}) \in \{(\mathrm{Bin1}, 0.1), (\mathrm{Bin2}, 1.33)\}$ . Note that  $\gamma_{\mathrm{c.m.}}^2 \left( T_{\chi} = T_{\chi}^{\mathrm{min}}(T_e) \right) = 1 + T_e / (2m_e)$  and, consequently, eq. (4.3) is independent of  $m_{\chi}$ . For the third energy bin, given the limit of angular resolution of the detector, we simply set  $\delta = 5^\circ$  [13]. The number of expected background in each cone  $(N_{\mathrm{Bkg}}^{\delta})$  can be estimated by assuming an isotropic distribution [13, 14], while the corresponding number of data events inside each cone from TXS 0506+056 and BL Lacertae  $(N_{\mathrm{TXS}}^{\delta}$  and  $N_{\mathrm{BL}}^{\delta}$ ) can be counted directly. We depict in figure 3 the spatial distribution of data events that followed the data selection of ref. [13] together with the optimal searching cones around the two blazars.

![](images/47343fb975b650857d709d809969913ae6454fa0cb4d2d230f872e675946f66d.jpg)

![](images/4fe41a344503f9564d00823dc306a5f82541e9d14f59e9b096a73adffe89f372.jpg)

![](images/36a3e2f361c53cc08bcfdd6d5a1961f32e18f6a582f9468ca878632a999a2c2a.jpg)  
Figure 3. The spatial distribution of the Super-K data events in Bin1 (top-left panel), Bin2 (top-right panel), and Bin3 (bottom panel) [13]. The positions of TXS  $0506 + 056$  (TXS) and BL Lacertae (BL) are marked with an orange and a blue star, respectively. As a landmark, the position of the Galactic Center (GC) is also identified (red diamond). The yellow (blue) regions around TXS (BL) represent the corresponding searching cones (see the text for further clarifications).

Table 2. A summary of our data analysis that follows ref. [13]. Three bins are considered according to the electron recoil energy, namely Bin1, Bin2 and Bin3. For each bin, we adopt different half-opening angles  $(\delta)$  of the searching cone based on eq. (4.3) and Super-K angular resolution. Using the Poisson method, the  $95\%$  C.L. upper limits on the number of events from TXS  $0506 + 056$  ( $N_{\mathrm{TXS}}$ ) and BL Lacertae ( $N_{\mathrm{BL}}$ ) can be derived. See the text for further details.  

<table><tr><td colspan="4">Sensitivity of Super-Kamiokande</td></tr><tr><td></td><td>Bin1</td><td>Bin2</td><td>Bin3</td></tr><tr><td>Te(GeV)</td><td>(0.1, 1.33)</td><td>(1.33, 20)</td><td>(20, 103)</td></tr><tr><td>NData</td><td>4042</td><td>658</td><td>3</td></tr><tr><td>NBkg</td><td>3992.9</td><td>772.6</td><td>7.4</td></tr><tr><td>εsig</td><td>93.0%</td><td>91.3%</td><td>81.1%</td></tr><tr><td>δ</td><td>24°</td><td>7°</td><td>5°</td></tr><tr><td>NTXSδ</td><td>169</td><td>2</td><td>0</td></tr><tr><td>NBLδ</td><td>167</td><td>4</td><td>0</td></tr><tr><td>NBkgδ</td><td>172.6</td><td>2.88</td><td>0.014</td></tr><tr><td>NTXS (95% C.L.)</td><td>19.39</td><td>3.42</td><td>2.98</td></tr><tr><td>NBL (95% C.L.)</td><td>17.27</td><td>6.27</td><td>2.98</td></tr></table>

Using the standard Poisson method [49], we derived the  $95\%$  Confidence Level (C.L.) upper limits on the event number from TXS 0506+056 ( $N_{\mathrm{TXS}}$ ) and BL Lacertae ( $N_{\mathrm{BL}}$ ). All the results of the data analysis have been condensed in table 2.

# 4.2 Bounds on scattering cross section

The number of BBDM-induced electron recoil events at Super-K can be expressed as

$$
N _ {e} ^ {\mathrm {D M}} \simeq N _ {e} \sigma_ {\chi e} t _ {\mathrm {o b s}} \int_ {T _ {\mathrm {e x p}} ^ {\mathrm {m i n}}} ^ {T _ {\mathrm {e x p}} ^ {\mathrm {m a x}}} d T _ {e} \int_ {T _ {\chi} ^ {\mathrm {m i n}} (T _ {e})} ^ {+ \infty} \frac {d T _ {\chi}}{T _ {e} ^ {\mathrm {m a x}} (T _ {\chi})} \frac {d \Phi_ {\chi} ^ {z}}{d T _ {\chi}}, \tag {4.4}
$$

where  $N_{e} = 7.5 \times 10^{33}$  is the total number of electrons in the Super-K water reservoir [13],  $t_{\mathrm{obs}} = 2628.1$  days is the exposure time,  $\left[T_{\mathrm{exp}}^{\mathrm{min}}, T_{\mathrm{exp}}^{\mathrm{max}}\right]$  is the energy range of each bin and  $d\Phi_{\chi}^{z} / dT_{\chi}$  is the BBDM flux at detector. The corresponding constraints on  $\sigma_{\chi e}$  from TXS 0506+056 (BL Lacertae) can be obtained by imposing

$$
N _ {e} ^ {\mathrm {D M}} \times \epsilon_ {\mathrm {s i g}} <   N _ {\mathrm {T X S}} \left(N _ {\mathrm {B L}}\right). \tag {4.5}
$$

For large enough  $\sigma_{\chi p}$  and/or  $\sigma_{\chi e}$ , the DM flux will be attenuated by the scatterings with nuclei and/or electrons in the crust of the Earth and render a "blind spot" at detectors [16, 50-53]. If one ignores the form factor, the corresponding upper bound for  $\sigma_{\chi p}(\sigma_{\chi e})$  at XENON1T (Super-K) is about  $3.0\times 10^{-28}\mathrm{cm}^2$  ( $2.0\times 10^{-28}\mathrm{cm}^2$ ) [14, 16]. However, a recent study shows that, after the form factor is properly taken into account, the exclusion upper bound for  $\sigma_{\chi p}$  can be increased at least by four orders of magnitude [54]. Therefore, given such large values, we decide to ignore the upper constraints in our analysis. Concerning the lower exclusion limits, the Earth's attenuation effects can be safely neglected because of the extreme smallness of  $\sigma_{\chi p}$  and  $\sigma_{\chi e}$  ( $\sigma_{\chi p}\lesssim 10^{-35}\mathrm{cm}^2$  [16] and  $\sigma_{\chi e}\lesssim 10^{-33}\mathrm{cm}^2$  [13]), meaning that we can safely replace  $d\Phi_{\chi}^{z} / dT_{\chi}$  in eq. (4.4) with  $d\Phi_{\chi} / dT_{\chi}$  given in eq. (3.5).

For our results, we first fix  $\sigma_{\chi p}$  at the corresponding lower exclusion values given in ref. [16] for BMP1 and BMP2, respectively. Therefore, there are only two free parameters,  $\sigma_{\chi e}$  and  $m_{\chi}$ . Combining eqs. (4.4) and (4.5) we derive the  $95\%$  C.L. limits on  $\sigma_{\chi e}$  from Super-K results. However, it is worth noting that the limitations on  $\sigma_{\chi e}$  we obtain in this case are the most optimistic results, because we have actually selected the maximal possible value of  $\sigma_{\chi p}$ . At the end of this section, we will discuss how different choices of  $\sigma_{\chi p}$  would influence our final results.

In table 3, we report the constraints on the logarithm of the DM-electron cross section  $(\log_{10}[\sigma_{\chi e} / \mathrm{cm}^2])$  from the two considered blazars with BMP1 parameters, for different energy bins and various DM masses. We find that, for different  $m_{\chi}$ , the most stringent limits on  $\sigma_{\chi e}$  may come from different bins. Hence, more stringent limits can be obtained by performing a combined analysis. We then show in the left and right panels of figure 4 the results for TXS  $0506 + 056$  and BL Lacertae, respectively. The solid line corresponds to BMP1, while the dashed and dotted lines represent the results for BMP2 and BMP3, respectively. For each considered blazar, the differences between these lines arise only from  $\Sigma_{\mathrm{DM}}^{\mathrm{tot}} / m_{\chi}$  (see figure 1). Compared to the results of CRDM, the BBDM constraints are more stringent by orders of magnitude, depending on the DM mass and the parameters of the benchmark point. Besides, the boundary values of  $\sigma_{\chi e}$  we have obtained are much smaller than the ones adopted for  $\sigma_{\chi p}$ , meaning that the BBDM flux at Super-K is dominated by the contribution from the protons in the blazars' jets.

On the other hand, assuming crossing symmetry, one can relate the scattering cross section to that of the annihilation/production processes and consider the relevant bounds. For instance, the Big Bang Nucleosynthesis (BBN) could constrain the parameter space for DM masses less than  $\mathcal{O}(1)\mathrm{MeV}$  [55, 56], although the precise bound is rather model dependent. From figure 4 we find that, after including the BBN bound, the previous boundaries from,

Table 3. The constraints on the DM-electron scattering cross section in the form  $\log_{10}[\sigma_{\chi e}/\mathrm{cm}^2]$  for different source, energy bin and DM mass. Note that all these results are derived for the parameters of BMP1. Also, for  $m_{\chi}/\mathrm{GeV} = \{10^{-6}, 10^{-4}, 10^{-2}\}$ , the corresponding lower boundary values of  $\sigma_{\chi p}$  are  $\log_{10}[\sigma_{\chi p}/\mathrm{cm}^2] = \{-34.80, -34.20, -32.29\}$  and  $\{-35.67, -35.36-34.09\}$  for TXS 0506+056 and BL Lacertae, respectively.  

<table><tr><td colspan="5">Constraints on DM-electron Cross Section</td></tr><tr><td rowspan="2">Source</td><td rowspan="2">Te(GeV)</td><td colspan="3">mχ(GeV)</td></tr><tr><td>10-6</td><td>10-4</td><td>10-2</td></tr><tr><td rowspan="3">BL Lacertae</td><td>(0.1, 1.33)</td><td>-38.35</td><td>-38.05</td><td>-37.39</td></tr><tr><td>(1.33, 20)</td><td>-38.00</td><td>-37.70</td><td>-37.84</td></tr><tr><td>(20, 103)</td><td>-37.49</td><td>-37.07</td><td>-35.87</td></tr><tr><td rowspan="3">TXS 0506+056</td><td>(0.1, 1.33)</td><td>-37.48</td><td>-36.95</td><td>-35.67</td></tr><tr><td>(1.33, 20)</td><td>-37.67</td><td>-37.26</td><td>-35.68</td></tr><tr><td>(20, 103)</td><td>-37.15</td><td>-36.62</td><td>-35.49</td></tr></table>

![](images/b5cb65d5723a3089a367d0896080b6589d1fb8bab829ad8a8ba5b2774bcbea23.jpg)  
Figure 4. The constraints on DM-electron scattering cross section imposed by Super-K [13]. The left panel is for TXS  $0506 + 056$ , while the right panel for BL Lacertae. The solid, dashed, and dotted purple lines correspond to BMP1, BMP2, and BMP3, respectively. For comparison, the constrains from CRDM [14, 15], XENON1T [6], SENSEI [58], Solar Reflection [57], and BBN [55, 56] are included.

![](images/c852b391a9ac2e2a46aa4f6bd8fa4a07ad4103ca4d9c598962d7e3b0edea7112.jpg)

e.g., CRDM [14] and Solar Reflection [57], are almost, if not all, excluded, whereas our results for BMP1 (as well as any intermediate case between BMP1 and BMP2) still cover an important region of the parameter space in the  $1 \lesssim m_{\chi} / \mathrm{MeV} \lesssim 30$  range.

As we have emphasized in section 2, the luminosities of TXS  $0506 + 056$  and BL Lacertae vary over time. Therefore, during the entire exposure period of Super-K, both  $L_{p}$  and  $L_{e}$  are not constant. However, we estimate that smaller values for  $L_{p}$  and  $L_{e}$  would not affect too much our results. For instance, since the boundary values of  $\sigma_{\chi p} \propto L_{p}^{-1/2}$  [16] and  $\sigma_{\chi e} \propto (L_{p}\sigma_{\chi p})^{-1} \propto L_{p}^{-1/2}$ , if  $L_{p}$  and  $L_{e}$  are reduced by two orders of magnitude simultaneously, the lower exclusion limits for  $\sigma_{\chi p}$  and  $\sigma_{\chi e}$  would increase by a factor of 10.

In figure 5 we show how the lower exclusion limit on  $\sigma_{\chi e}$  changes for different values of  $\sigma_{\chi p}$ . The left (right) panel corresponds to TXS  $0506 + 056$  (BL Lacertae). In the two plots, we show the curves for  $m_{\chi} = 10^{-8}\mathrm{GeV}$  (red),  $10^{-5}\mathrm{GeV}$  (green), and  $10^{-2}\mathrm{GeV}$  (blue), for

![](images/e4ceef2f5960ed88831009635dc1ce6bbb88c5b1877e114a65ae99fa18654c43.jpg)  
Figure 5. The relationship between  $\sigma_{\chi p}$  and  $\sigma_{\chi e}$  for TXS  $0506 + 056$  (left panel) and BL Lacertae (right panel). Different colours correspond to different DM masses, namely  $10^{-5}\mathrm{GeV}$  (purple) and  $10^{-2}\mathrm{GeV}$  (blue). The solid, dashed, and dotted lines represent BMP1, BMP2, and BMP3, respectively. The dot-dashed horizontal lines indicate the lower boundary values of  $\sigma_{\chi e}$  given by CRDM (see figure 4).

![](images/f5a866d3f0e4236f302ed1ff5ed7f6c8a2dfea314aaa5179a8186f3ec35f2c99.jpg)

both BMP1 (solid lines) and BMP2 (dashed lines). We find that, for small values of  $\sigma_{\chi p}$  (say  $\sigma_{\chi p} \lesssim 10^{-38} \mathrm{~cm}^2$ ), the exclusion boundaries of  $\sigma_{\chi e}$  tend to constant values, which means that in this case the BBDM flux at Super-K would only come from the electron contribution, and can be regarded as the most conservative limits on the DM-electron cross section from BBDM. Note that the "vanishing"  $\sigma_{\chi p}$  scenario would be analogous to the case of purely leptonic SED model, for which the contribution from protons is naturally suppressed. For comparison, we indicate with horizontal dot-dashed lines the lower constraints on  $\sigma_{\chi e}$  from CRDM (see figure 4).

# 5 Conclusion

The highly powerful jets emitted from the center, together with the large amount of DM present in their surroundings, make blazars ideal DM boosters. Based on ref. [16], we have included the DM-electron interaction and derived the corresponding constraints on  $\sigma_{\chi e}$  by making use of the available experimental results of Super-K. In our analysis, two blazars have been considered, namely TXS  $0506 + 056$  and BL Lacertae. Combining the spatial distribution of electron recoil data with the blazars' positions, we have conducted a refined analysis by setting a proper searching cone for different energy bins and derived the  $95\%$  C.L. constraints on the DM-electron cross section with the standard Poisson method (see figure 4). Compared with the previous results from galactic CRs, the limits on  $\sigma_{\chi e}$  from BBDM has improved by orders of magnitude, depending mainly on  $m_{\chi}$  and the parameters relevant to the DM density profile. Besides, in view of future neutrino detectors such as Hyper-Kamiokande [59] and DUNE [60] (see also ref. [61]), our results could be further improved.

For future prospects, it could be interesting to do a more refined analysis (improving, e.g., the size of the searching cone and/or the time correlation) through the combination of neutrino detectors data with the observations of blazars from telescopes, such as Fermi-LAT [62] and/or the planned Cherenkov Telescope Array project [63]. This, in principle, could enable us to select events from the right blazar at the optimal time, e.g. during a blazar flare when the luminosity is enhanced, in analogy to the multi-messenger approach used to

correlate the flaring of TXS  $0506 + 056$  with the first detection of cosmic neutrinos by IceCube Neutrino Observatory [64-67]. Furthermore, we expect that a statistical analysis extended to the full population of blazars would minimize the dependence on both model uncertainties and blazar selection, leading eventually to an enhancement of our results. Finally, studying possible BBDM signals could allow to extrapolate more information on the SED jet models of blazars and/or the nature of DM.

# Acknowledgments

The authors wish to thank Serguey T. Petcov for thoughtful discussions and suggestions. This work was supported by the research grant "The Dark Universe: A Synergic Multi-messenger Approach" number 2017X7X85K under the program PRIN 2017 funded by the The Italian Ministry of Education, University and Research (MIUR), and by the European Union's Horizon 2020 research and innovation program under the Marie Skłodowska-Curie grant agreement No 860881-HIDDeN.

# References

[1] G. Bertone, D. Hooper and J. Silk, Particle dark matter: evidence, candidates and constraints, Phys. Rept. 405 (2005) 279 [hep-ph/0404175] [INSPIRE].  
[2] PLANCK collaboration, Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [Erratum ibid. 652 (2021) C4] [arXiv:1807.06209] [INSPIRE].  
[3] XENON1T collaboration, The XENON1T dark matter search experiment, Springer Proc. Phys. 148 (2013) 93 [arXiv:1206.6288] [INSPIRE].  
[4] XENON collaboration, The XENON1T dark matter experiment, Eur. Phys. J. C 77 (2017) 881 [arXiv:1708.07051] [INSPIRE].  
[5] PANDAX-II collaboration, Dark matter results from 54-ton-day exposure of PandaX-II experiment, Phys. Rev. Lett. 119 (2017) 181302 [arXiv:1708.06917] [INSPIRE].  
[6] XENON collaboration, Light dark matter search with ionization signals in XENON1T, Phys. Rev. Lett. 123 (2019) 251801 [arXiv:1907.11485] [INSPIRE].  
[7] PANDAX-II collaboration, Search for light dark matter-electron scatterings in the PandaX-II experiment, Phys. Rev. Lett. 126 (2021) 211803 [arXiv:2101.07479] [INSPIRE].  
[8] K. Agashe, Y. Cui, L. Necib and J. Thaler, (In)direct detection of boosted dark matter, JCAP 10 (2014) 062 [arXiv:1405.7370] [INSPIRE].  
[9] C. Kouvaris, Probing light dark matter via evaporation from the sun, Phys. Rev. D 92 (2015) 075001 [arXiv:1506.04316] [INSPIRE].  
[10] H. An, M. Pospelov, J. Pradler and A. Ritz, Directly detecting MeV-scale dark matter via solar reflection, Phys. Rev. Lett. 120 (2018) 141801 [Erratum ibid. 121 (2018) 259903] [arXiv:1708.03642] [INSPIRE].  
[11] T. Emken, C. Kouvaris and N.G. Nielsen, The sun as a sub-GeV dark matter accelerator, Phys. Rev. D 97 (2018) 063007 [arXiv:1709.06573] [INSPIRE].  
[12] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[13] SUPER-KAMIOKANDE collaboration, Search for boosted dark matter interacting with electrons in Super-Kamiokande, Phys. Rev. Lett. 120 (2018) 221301 [arXiv:1711.05278] [INSPIRE].

[14] Y. Ema, F. Sala and R. Sato, Light dark matter at neutrino experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[15] C.V. Cappiello and J.F. Beacom, *Strong new limits on light dark matter from neutrino experiments*, Phys. Rev. D 100 (2019) 103011 [Erratum ibid. 104 (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[16] J.-W. Wang, A. Granelli and P. Ullio, Direct detection constraints on blazar-boosted dark matter, Phys. Rev. Lett. 128 (2022) 221104 [arXiv:2111.13644] [INSPIRE].  
[17] P. Gondolo and J. Silk, Dark matter annihilation at the galactic center, Phys. Rev. Lett. 83 (1999) 1719 [astro-ph/9906391] [INSPIRE].  
[18] MINIBOONE collaboration, The MiniBoONE detector, Nucl. Instrum. Meth. A 599 (2009) 28 [arXiv:0806.4201] [INSPIRE].  
[19] BOREXINO collaboration, Science and technology of BOREXINO: a real time detector for low-energy solar neutrinos, Astropart. Phys. 16 (2002) 205 [hep-ex/0012030] [INSPIRE].  
[20] A.A. Abdo et al., The spectral energy distribution of Fermi bright blazars, Astrophys. J. 716 (2010) 30 [arXiv:0912.2040] [INSPIRE].  
[21] L. Maraschi, G. Ghisellini and A. Celotti, A jet model for the gamma-ray emitting blazar 3C 279, Astrophys. J. Lett. 397 (1992) L5 [INSPIRE].  
[22] K. Mannheim, The proton blazar, Astron. Astrophys. 269 (1993) 67 [astro-ph/9302006] [INSPIRE].  
[23] S.D. Bloom and A.P. Marscher, An analysis of the synchrotron self-Compton model for the multi-wave band spectra of blazars, Astrophys. J. 461 (1996) 657 [INSPIRE].  
[24] A. Mücke and R.J. Protheroe, A proton synchrotron blazar model for flaring in Markarian 501, Astrophys. Phys. 15 (2001) 121 [astro-ph/0004052] [INSPIRE].  
[25] A. Celotti and G. Ghisellini, The power of blazar jets, Mon. Not. Roy. Astron. Soc. 385 (2008) 283 [arXiv:0711.4112] [INSPIRE].  
[26] G. Ghisellini, F. Tavecchio, L. Foschini, G. Ghirlanda, L. Maraschi and A. Celotti, General physical properties of bright Fermi blazars, Mon. Not. Roy. Astron. Soc. 402 (2010) 497 [arXiv:0909.0932] [INSPIRE].  
[27] M. Böttcher, A. Reimer, K. Sweeney and A. Prakash, Leptonic and hadronic modeling of Fermi-detected blazars, Astrophys. J. 768 (2013) 54 [arXiv:1304.0605] [INSPIRE].  
[28] M. Cerruti, Leptonic and hadronic radiative processes in supermassive-black-hole jets, *Galaxies* 8 (2020) 72 [arXiv:2012.13302] [INSPIRE].  
[29] C.D. Dermer and G. Menon, High energy radiation from black holes: gamma rays, cosmic rays and neutrinos, Princeton University Press, Princeton, NJ, U.S.A. (2009).  
[30] M. Cerruti, A. Zech, C. Boisson, G. Emery, S. Inoue and J.-P. Lenain, Leptohadronic single-zone models for the electromagnetic and neutrino emission of TXS 0506 + 056, Mon. Not. Roy. Astron. Soc. 483 (2019) L12 [Erratum ibid. 502 (2021) L21] [arXiv:1807.04335] [INSPIRE].  
[31] J.B. Oke and J.E. Gunn, The distance of BL Lacertae, Astrophys. J. 189 (1974) L5.  
[32] S. Paiano, R. Falomo, A. Treves and R. Scarpa, The redshift of the BL Lac object TXS 0506 + 056, Astrophys. J. Lett. 854 (2018) L32 [arXiv:1802.01939] [INSPIRE].  
[33] L. Titarchuk and E. Seifina, BL Lacertae: X-ray spectral evolution and a black-hole mass estimate, Astron. Astrophys. 602 (2017) A113 [arXiv:1704.04552] [INSPIRE].

[34] P. Padovani, F. Oikonomou, M. Petropoulou, P. Giommi and E. Resconi, TXS 0506 + 056, the first cosmic neutrino source, is not a BL Lac, Mon. Not. Roy. Astron. Soc. 484 (2019) L104 [arXiv:1901.06998] [INSPIRE].  
[35] M. Gorchtein, S. Profumo and L. Ubaldi, Probing dark matter with AGN jets, Phys. Rev. D 82 (2010) 083514 [Erratum ibid. 84 (2011) 069903] [arXiv:1008.2230] [INSPIRE].  
[36] P. Ullio, H. Zhao and M. Kamionkowski, A dark matter spike at the galactic center?, Phys. Rev. D 64 (2001) 043504 [astro-ph/0101481] [INSPIRE].  
[37] J.F. Navarro, C.S. Frenk and S.D.M. White, A universal density profile from hierarchical clustering, Astrophys. J. 490 (1997) 493 [astro-ph/9611107] [INSPIRE].  
[38] D. Merritt, M. Milosavljevic, L. Verde and R. Jimenez, Dark matter spikes and annihilation radiation from the galactic center, Phys. Rev. Lett. 88 (2002) 191301 [astro-ph/0201376] [INSPIRE].  
[39] O.Y. Gnedin and J.R. Primack, Dark matter profile in the galactic center, Phys. Rev. Lett. 93 (2004) 061302 [astro-ph/0308385] [INSPIRE].  
[40] G. Bertone and D. Merritt, Time-dependent models for dark matter at the galactic center, Phys. Rev. D 72 (2005) 103502 [astro-ph/0501555] [INSPIRE].  
[41] D.E. Kaplan, M.A. Luty and K.M. Zurek, Asymmetric dark matter, Phys. Rev. D 79 (2009) 115016 [arXiv:0901.4117] [INSPIRE].  
[42] K. Petraki and R.R. Volkas, Review of asymmetric dark matter, Int. J. Mod. Phys. A 28 (2013) 1330028 [arXiv:1305.4939] [INSPIRE].  
[43] K.M. Zurek, Asymmetric dark matter: theories, signatures, and constraints, Phys. Rept. 537 (2014) 91 [arXiv:1308.0338] [INSPIRE].  
[44] D. Martizzi, R. Teyssier and B. Moore, Cusp-core transformations induced by AGN feedback in the progenitors of cluster galaxies, Mon. Not. Roy. Astron. Soc. 432 (2013) 1947 [arXiv:1211.2648] [INSPIRE].  
[45] A. Di Cintio, C.B. Brook, A.A. Dutton, A.V. Maccio, G.S. Stinson and A. Knebe, *A mass-dependent density profile for dark matter haloes including the influence of galaxy formation*, Mon. Not. Roy. Astron. Soc. 441 (2014) 2986 [arXiv:1404.5959] [INSPIRE].  
[46] O. Sameie et al., The central densities of milky way-mass galaxies in cold and self-interacting dark matter models, Mon. Not. Roy. Astron. Soc. 507 (2021) 720 [arXiv:2102.12480] [INSPIRE].  
[47] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse direct detection: cosmic ray scattering with light dark matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[48] K. Bondarenko, A. Boyarsky, T. Bringmann, M. Hufnagel, K. Schmidt-Hoberg and A. Sokolenko, Direct detection and complementary constraints for sub-GeV dark matter, JHEP 03 (2020) 118 [arXiv:1909.08632] [INSPIRE].  
[49] PARTICLE DATA GROUP collaboration, Review of particle physics, PTEP 2020 (2020) 083C01 [INSPIRE].  
[50] G.D. Starkman, A. Gould, R. Esmailzadeh and S. Dimopoulos, Opening the window on strongly interacting dark matter, Phys. Rev. D 41 (1990) 3594 [INSPIRE].  
[51] G.D. Mack, J.F. Beacom and G. Bertone, Towards closing the window on strongly interacting dark matter: far-reaching constraints from earth's heat flow, Phys. Rev. D 76 (2007) 043523 [arXiv:0705.4298] [INSPIRE].  
[52] D. Hooper and S.D. McDermott, Robust constraints and novel gamma-ray signatures of dark matter that interacts strongly with nucleons, Phys. Rev. D 97 (2018) 115006 [arXiv:1802.03025] [INSPIRE].

[53] T. Emken and C. Kouvaris, How blind are underground and surface detectors to strongly interacting dark matter?, Phys. Rev. D 97 (2018) 115047 [arXiv:1802.04764] [INSPIRE].  
[54] C. Xia, Y.-H. Xu and Y.-F. Zhou, Production and attenuation of cosmic-ray boosted dark matter, JCAP 02 (2022) 028 [arXiv:2111.05559] [INSPIRE].  
[55] G. Krnjaic and S.D. McDermott, Implications of BBN bounds for cosmic ray upscattered dark matter, Phys. Rev. D 101 (2020) 123022 [arXiv:1908.00007] [INSPIRE].  
[56] P.F. Depta, M. Hufnagel, K. Schmidt-Hoberg and S. Wild, BBN constraints on the annihilation of MeV-scale dark matter, JCAP 04 (2019) 029 [arXiv:1901.06944] [INSPIRE].  
[57] H. An, M. Pospelov, J. Pradler and A. Ritz, Directly detecting MeV-scale dark matter via solar reflection, Phys. Rev. Lett. 120 (2018) 141801 [Erratum ibid. 121 (2018) 259903] [arXiv:1708.03642] [INSPIRE].  
[58] SENSEI collaboration, SENSEI: direct-detection results on sub-GeV dark matter from a new skipper-CCD, Phys. Rev. Lett. 125 (2020) 171802 [arXiv:2004.11378] [INSPIRE].  
[59] HYPER-KAMIOKANDE collaboration, Hyper-Kamiokande design report, arXiv:1805.04163 [INSPIRE].  
[60] DUNE collaboration, Long-Baseline Neutrino Facility (LBNF) and Deep Underground Neutrino Experiment (DUNE). Conceptual design report, volume 2: the physics program for DUNE at LBNF, arXiv:1512.06148 [INSPIRE].  
[61] L. Necib, J. Moon, T. Wongjirad and J.M. Conrad, Boosted dark matter at neutrino experiments, Phys. Rev. D 95 (2017) 075018 [arXiv:1610.03486] [INSPIRE].  
[62] FERMI-LAT collaboration, The Large Area Telescope on the Fermi gamma-ray space telescope mission, Astrophys. J. 697 (2009) 1071 [arXiv:0902.1089] [INSPIRE].  
[63] P. Goldoni et al., Optical spectroscopy of blazars for the Cherenkov Telescope Array, Astron. Astrophys. 650 (2021) A106 [arXiv:2012.05176] [INSPIRE].  
[64] ICECUBE, FERMI-LAT, MAGIC, AGILE, ASAS-SN, HAWC, H.E.S.S., INTEGRAL, KANATA, KISO, KAPTEYN, LIVERPOOL TELESCOPE, SUBARU, SWIFT NUSTAR, VERITAS and VLA/17B-403 collaborations, Multimessenger observations of a flaring blazar coincident with high-energy neutrino IceCube-170922A, Science 361 (2018) eaat1378 [arXiv:1807.08816] [INSPIRE].  
[65] ICECUBE collaboration, Neutrino emission from the direction of the blazar TXS 0506 + 056 prior to the IceCube-170922A alert, Science 361 (2018) 147 [arXiv:1807.08794] [INSPIRE].  
[66] P. Padovani et al., Dissecting the region around IceCube-170922A: the blazar TXS 0506 + 056 as the first cosmic neutrino source, Mon. Not. Roy. Astron. Soc. 480 (2018) 192 [arXiv:1807.04461] [INSPIRE].  
[67] K. Murase, F. Oikonomou and M. Petropoulou, *Blazar flares as an origin of high-energy cosmic neutrinos?, Astrophys. J. 865 (2018) 124 [arXiv:1807.04748] [INSPIRE].