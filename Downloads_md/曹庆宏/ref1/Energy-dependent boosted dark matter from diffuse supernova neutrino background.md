PAPER • OPEN ACCESS

# Energy-dependent boosted dark matter from diffuse supernova neutrino background

To cite this article: Anirban Das et al JCAP07(2024)045

View the article online for updates and enhancements.

# You may also like

- Probing P- and CP-violation in dark matter interactions  
Riccardo Catena, Joakim Hagel and Carlos E. Yaguna  
- The Large Magellanic Cloud: expanding the low-mass parameter space of dark matter direct detection  
Javier Reynoso-Cordova, Nassim  
Bozorgnia and Marie-Cécile Piro  
- Constraints on the Velocity Dispersion of Dark Matter from Cosmology and New Bounds on Scattering from the Cosmic Dawn  
Iván Rodríguez-Montoya, Vladimir Avila-Reese, Abdel Pérez-Lorenzana et al.

# Energy-dependent boosted dark matter from diffuse supernova neutrino background

Anirban Das  $^{a}$ , Tim Herbermann  $^{b}$ , Manibrata Sen  $^{b}$  and Volodymyr Takhistov  $^{c,d,e,f}$

$^{a}$ Center for Theoretical Physics, Department of Physics & Astronomy, Seoul National University, Seoul 08826, South Korea  
${}^{b}$  Max-Planck-Institut für Kernphysik, Saupfercheckweg 1,69117 Heidelberg,Germany  
$^{c}$ International Center for Quantum-field Measurement Systems for Studies of the Universe and Particles (QUP), KEK, 1-1 Oho, Tsukuba, Ibaraki 305-0801, Japan  
$^{d}$ Theory Center, Institute of Particle and Nuclear Studies, High Energy Accelerator Research Organization (KEK), Tsukuba 305-0801, Japan  
<sup>e</sup>Graduate University for Advanced Studies (SOKENDAI), 1-1 Oho, Tsukuba, Ibaraki 305-0801, Japan  
$^{f}$ Kavli Institute for the Physics and Mathematics of the Universe (WPI), The University of Tokyo Institutes for Advanced Study, The University of Tokyo, Kashiwa, Chiba 277-8583, Japan

E-mail: anirbandas@snu.ac.kr, tim.berermann@mpi-hd.mpg.de, manibrata.sen@mpi-hd.mpg.de, vtakhist@post.kek.jp

ABSTRACT: Diffuse neutrinos from past supernovae in the Universe present us with a unique opportunity to test dark matter (DM) interactions. These neutrinos can scatter and boost the DM particles in the Milky Way halo to relativistic energies allowing us to detect them in terrestrial laboratories. Focusing on generic models of DM-neutrino and electron interactions, mediated by a vector or a scalar boson, we implement energy-dependent scattering cross-sections and perform detailed numerical analysis of DM attenuation due to electron scattering in-medium while propagating towards terrestrial experiments. We set new limits on DM-neutrino and electron interactions for DM with masses in the range  $\sim (0.1, 10^4)$  MeV, using recent data from XENONnT, LUX-ZEPLIN, and PandaX-4T direct detection experiments. We demonstrate that consideration of energy-dependent cross-sections for DM interactions can significantly affect constraints previously derived under the assumption of constant cross-sections, modifying them by multiple orders of magnitude.

KEYWORDS: dark matter theory, supernova neutrinos, core-collapse supernovae, dark matter experiments

ARXIV EPRINT: 2403.15367

# Contents

1 Introduction 1  
2 Diffuse supernova neutrino background 3

3 Dark matter-lepton interactions 4

3.1 Vector mediated dark matter-lepton interaction 5  
3.2 Scalar mediated dark matter-lepton interaction 6

4 Boosted dark matter 8

4.1 Attenuation 9

5 Results 11

5.1 Impact of Lorentz structure on upscattering and attenuation 11  
5.2 Expected electron recoil event rates 12  
5.3 Statistical analysis 13

6 Summary and conclusions 16

# 1 Introduction

Dark matter (DM) constitutes about  $\sim 85\%$  of all matter in the Universe. However, despite decades of searches, its nature remains mysterious (see e.g. [1] for review). Traditional direct DM detection experiments, which constitute a cornerstone of DM exploration, have aimed at searching for energy deposits from Galactic halo DM interactions with nucleons (see e.g. [2] for an overview). Recent results from experiments like XENON [3], LUX-Zepelin (LZ) [4, 5] and PandaX [6] continue to further push this frontier. However, scattering with electrons can provide unique opportunities for DM exploration, particularly for sub-GeV low-mass DM which would be kinematically challenging to detect with nuclear scattering. DM-electron scattering has already been adopted as a target for a multitude of experiments, including XENONnT [7], DAMIC [8], SENSEI [9] and SuperCDMS [10] and is expected to become a central avenue for future direct DM detection studies [11].

Neutrinos are ubiquitously abundant in the Universe, originating from diverse sources such as primordial plasma and astrophysical transients. This provides us with unique opportunities to explore possible neutrino-DM interactions. Scattering of energetic neutrinos with slow-moving cold DM particles within the Milky Way halo can upscatter the latter to relativistic energies. Such boosted DM (BDM) would manifest in distinct experimental signatures and offer new means of detection [12-15]. One motivated class of DM models to explore within this context is leptophilic DM [16-23], where the DM interacts exclusively with neutrinos as well as charged leptons of the Standard Model (SM). Furthermore, these interactions facilitate DM scattering off free leptons encountered on their journey towards Earth. We note that analogous boosting of DM can also be achieved in the context of hadrophilic DM models

due to energetic hadronic interactions of DM with cosmic rays, which has been extensively explored [13, 24-43]. Such DM interactions enable probing lighter sub-GeV DM masses with nucleon scattering by overcoming kinematic thresholds which impede cold non-relativistic DM searches in conventional noble element detectors [44].

In this paper, we revisit the boosting of light DM by neutrinos contributing to the diffuse supernova neutrino background (DSNB) from historic supernovae events [13] and expand the analysis in many aspects. An explosive core-collapse supernova (CCSN) loses a major fraction of its energy through neutrino emission. This was confirmed by detection of neutrinos [45, 46] from SN1987A that exploded in the Large Magellanic Cloud, which also spearheaded the era of multimeterger astronomy. Such neutrinos follow an approximate thermal distribution with energies  $E \sim \mathcal{O}(10)$  MeV. Accumulation of neutrinos from all the previous CCSNe in the history of our Universe contributes to the persistent flux of DSNB, also known as supernova relic neutrino background (see e.g. [47, 48] for review). Detection of the DSNB is a prime target of current as well as forthcoming neutrino experiments, including Super-Kamiokande (SK) [49], Hyper-Kamiokande (HK) [50], Jiangmen Underground Neutrino Observatory (JUNO) [51], and Deep Underground Neutrino Experiment (DUNE) [52]. At present, the most stringent upper limit on the DSNB flux, set by SK, remains a few times higher than typical theoretical predictions [49, 53]. Enrichment with gadolinium (Gd) has significantly enhanced SK's sensitivity, potentially leading to the possibility of detection of the DSNB within the next few years [54-56]. Furthermore, other future experiments such as Theia [57], as well as those relying on coherent elastic neutrino-nucleus scattering for detection [58-60], also exhibit promising capabilities for DSNB detection. The anticipated discovery of the DSNB also facilitates exploration of new physics beyond the SM [13, 35, 61-67].

Previously, DSNB-boosted DM was analysed by some of the present authors while focusing on scenarios where DM interacts with leptons through a heavy mediator [13]. Here, we instead consider DM interactions mediated by a scalar or a vector boson of a varied mass. This not only broadens the scope of considered DM models but has crucial implications for the resulting constraints, as the energy dependence of the cross-section changes drastically for a light mediator compared to a heavy one. As we shall demonstrate, our results have significant qualitative dependence on the considered mediator mass. Further, our analysis enables the translation of the existing experimental constraints into new constraints for different DM models.

Furthermore, the interactions with SM constituents lead to in-medium attenuation of the boosted DM flux incoming towards terrestrial experiments (see e.g. [27, 28, 68-73] within the context of other scenarios). We improve upon results of previous DSNB-boosted DM study [13], by some of the present authors, by including the effects of DM flux attenuation due to interactions with the electrons in the atmosphere and the Earth, using a full numerical treatment. A step in this direction was recently taken in ref. [39], considering a simplified analytical treatment of attenuation. However, the simplifying assumptions used to obtain results from such an analytical approach are not valid when the boosted DM has kinetic energy comparable to the electron mass, particularly relevant for DM with low masses. Instead, in this work, we relax this assumption and numerically solve for the mean energy loss effects due to attenuation in the approximation of negligible DM deflection and discuss the impact on boosted DM flux.

Focusing on resulting signatures within large underground direct DM detection experiments, $^{1}$  such as XENONnT [3], LUX-ZEPLIN (LZ) [5] and PandaX-4T [6], we show that attenuation plays an important role for a broad parameter space of interest in the DM mass versus cross-section plane. We find that due to attenuation, the constraints change significantly when the full energy dependence of scattering cross-sections is taken into account. The primary impact of attenuation in the Earth's crust is the downgrading of the energy of traversing DM particles. Attenuation effects are especially pronounced when the mediator is light, resulting in a shift of the resulting constraints from terrestrial experiments towards lower DM masses.

The paper is organized as follows. In section 2 and section 3 we describe the DSNB flux and DM-lepton interaction models, respectively. In section 4, we discuss the upscattering and attenuation of DM and our numerical method to compute it. In section 5 we discuss our results. We conclude in section 6.

# 2 Diffuse supernova neutrino background

CCSNe are among the most energetic and extreme violent events in our Universe. At any given time, the rate of CCSNe in the whole observable Universe can be as large as one per second. It is well established that in a single such explosive transient event, almost  $\sim 99\%$  of the binding energy of the progenitor star is carried away by  $\sim 10^{58}$  emitted neutrinos. Accumulation of these neutrinos from historic CCSNe forms a persistent DSNB flux. The DSNB is isotropic and is composed of  $\mathcal{O}(10)$  MeV energy neutrinos that are as ubiquitous as neutrinos comprising the cosmic neutrino background that is a relic of the Big Bang in the early Universe, only significantly more energetic.

The estimation of the DSNB spectra requires knowledge of the rate of CCSN happening in the Universe,  $R_{\mathrm{CCSN}}(z)$ , where  $z$  is the redshift of occurrence of the CCSN in the past, and the energy spectrum of the neutrinos from individual CCSN,  $F_{\nu}(E')$ . Combining these, the DSNB spectra for a given neutrino flavour can be computed as [47, 75]

$$
\Phi_ {\nu} (E) = \int_ {0} ^ {z _ {\max }} \frac {d z}{H (z)} R _ {\mathrm {C C S N}} (z) F _ {\nu} \left(E ^ {\prime}\right) | _ {E ^ {\prime} = E (1 + z)}, \tag {2.1}
$$

where  $H(z) = H_0\sqrt{\Omega_m(1 + z)^3 + \Omega_\Lambda}$  is the Hubble function with  $H_0 = 67\mathrm{km s^{-1}}\mathrm{Mpc^{-1}}$ ,  $\Omega_{m} = 0.32$ ,  $\Omega_{\Lambda} = 0.68$  in the  $\Lambda$ CDM cosmological model [76]. We take the maximum redshift of star formation to be  $z_{\mathrm{max}} = 6$ . The neutrino emission spectrum  $F(E)$  from a single CCSN can be obtained from a hydrodynamic simulation. Typically, the fluence denoting time-integrated spectra is relevant for the estimation. This is dominated by the cooling phase of the CCSN, and hence the spectrum can approximated to be a Fermi-Dirac distribution [47]

$$
F _ {\nu} (E) = \frac {E _ {\nu} ^ {\mathrm {t o t}}}{6} \frac {1 2 0}{7 \pi^ {4}} \frac {E ^ {2}}{T _ {\nu} ^ {4}} \frac {1}{e ^ {E / T _ {\nu}} + 1}. \tag {2.2}
$$

Here,  $E_{\nu}^{\mathrm{tot}} = 3 \times 10^{53}$  erg is the total emitted neutrino energy and we take for reference input temperatures to be  $T_{\nu_e} = 6.6$  MeV,  $T_{\bar{\nu}_e} = 7$  MeV, and  $T_{\nu_x} = 10$  MeV, where  $\nu_x \equiv \nu_{\mu,\tau}$ .<sup>2</sup>

![](images/91b0e173fbccf6b2a9897fa63f5ab03cda0af3dc8556c184ad3cd6ecdb617d5b.jpg)  
Figure 1. The diffuse supernova neutrino background (DSNB) spectra for  $\nu_{e}$  (blue),  $\bar{\nu}_{e}$  (orange), and  $\nu_{x}$  (green). The width for each flavour denotes the uncertainty from the history of the star-formation rate. We assume the normal ordering for neutrino masses.

Constraints on the allowed values of the temperature have been put from null observations of the DSNB flux by SK [53]. Alternatively, one can also use the  $\alpha$ -fit parameterization of  $F_{\nu}$ , following [78]. We do not expect this to change the qualitative nature of our results.

The CCSN rate can be estimated from the star formation rate (SFR)  $R_{*}(z)$ . To this end, we use the following fitting function from ref. [79],

$$
R _ {\mathrm {C C S N}} (z) = \frac {R _ {0 , \mathrm {S F R}}}{1 4 3} \left[ (1 + z) ^ {- 1 0 \alpha} + \left(\frac {1 + z}{B}\right) ^ {- 1 0 \beta} + \left(\frac {1 + z}{C}\right) ^ {- 1 0 \gamma} \right] ^ {- 1 / 1 0}. \tag {2.3}
$$

Here, the parameters are as follows:  $R_{0,\mathrm{SFR}} = 0.0178\mathrm{yr}^{-1}\mathrm{Mpc}^{-3}$ ,  $\alpha = 3.4$ ,  $\beta = -0.3$ ,  $\gamma = -3.5$ , and  $B = (1 + z_1)^{1 - \alpha / \beta}$ ,  $C = (1 + z_1)^{(\beta - \alpha) / \gamma} \times (1 + z_2)^{1 - \beta / \gamma}$ . For a more recent measurement of the SFR, see [80]. We also neglect contributions from failed SNe [61].

We consider the neutrino spectra from the SN to be processed by adiabatic Mikheyev-Smirnov-Wolfenstein flavour conversions and neglect the effects due to collective oscillations in view of the larger  $\sim 40\%$  uncertainty from CCSN rate [75]. We assume normal mass-ordering for neutrinos, which implies that the  $\nu_{e}$  is mostly associated with the heaviest mass eigenstate  $\nu_{3}$ , and the  $\bar{\nu}_{e}$  with the lightest state,  $\bar{\nu}_{1}$ . The DSNB spectra for different neutrino flavours are shown in figure 1, with the corresponding uncertainty from SFR. We find that the  $\nu_{e}$  spectrum peaks at lower energy, whereas at higher energies, the dominant contribution comes from the non-electron flavour neutrinos —  $\nu_{x}$ . Using this, we will compute the boosted DM spectra at the Earth. In this and what follows, we assume the normal ordering for neutrino masses. The results for inverted ordering will only alter the DSNB spectra slightly and we have checked that this does not affect the overall results for the boosted DM spectra.

# 3 Dark matter-lepton interactions

In this section, we study simple phenomenological models of DM-lepton interactions. Such interactions, responsible for boosting the DM, attenuation, and ultimately detection, can arise in a variety of models of new physics beyond SM, where the DM is coupled to the

SM through some portal interactions. We consider cases where the interactions can be mediated by a vector or a scalar boson.

# 3.1 Vector mediated dark matter-lepton interaction

In the first example, we consider a fermionic singlet Dirac DM  $\chi$  coupled to a massive vector boson  $Z_{\mu}^{\prime}$ . The relevant interaction reads,

$$
\mathcal {L} \supset g _ {e} \bar {e} \gamma^ {\mu} e Z _ {\mu} ^ {\prime} + g _ {\nu} \bar {\nu} \gamma^ {\mu} \nu Z _ {\mu} ^ {\prime} + g _ {\chi} \bar {\chi} \gamma^ {\mu} \chi Z _ {\mu} ^ {\prime}. \tag {3.1}
$$

Under the assumption  $g_{\nu} = g_{e} = g$ , this can be embedded in a UV-complete model. This can happen, for example, if the DM is charged under an additional U(1) symmetry. We do not discuss here further details of a complete model construction. The relevant part of the Lagrangian reads

$$
\mathcal {L} \supset \bar {\chi} (i \partial / - m _ {\chi}) \chi - \frac {1}{4} Z _ {\mu \nu} ^ {\prime} Z ^ {\prime \mu \nu} + \frac {1}{2} m _ {Z ^ {\prime}} ^ {2} Z _ {\mu} ^ {\prime} Z ^ {\prime \mu} + g \bar {L} \gamma_ {\mu} L Z ^ {\prime \mu} + g _ {\chi} \bar {\chi} \gamma_ {\mu} \chi Z ^ {\prime \mu} + \mathrm {h . c .}. \tag {3.2}
$$

Here  $L$  is the SM lepton doublet. This model permits the upscattering of  $\chi$  through the following  $t$ -channel scattering process:  $\nu(p_1) + \chi(p_2) \rightarrow \nu(p_3) + \chi(p_4)$ . The upscattering can be captured by the following averaged matrix amplitude-squared (assuming  $m_\nu = 0$ ),

$$
| M | ^ {2} = \frac {2 g ^ {2} g _ {\chi} ^ {2}}{(t - m _ {Z ^ {\prime}} ^ {2}) ^ {2}} \left[ 2 (m _ {\chi} ^ {2} - s) ^ {2} + 2 s t + t ^ {2} \right]. \tag {3.3}
$$

The corresponding matrix-amplitude squared for direct detection with electrons is given by

$$
| M | ^ {2} = \frac {2 g ^ {2} g _ {\chi} ^ {2}}{(t - m _ {Z ^ {\prime}} ^ {2}) ^ {2}} \left[ 2 (m _ {e} ^ {2} + m _ {\chi} ^ {2} - s) ^ {2} + 2 s t + t ^ {2} \right]. \tag {3.4}
$$

Eq. (3.3) can be used to estimate the energy dependence of DM-neutrino differential cross-section for the vector mediator in terms of the DM kinetic energy  $(T_{\chi})$ . In the heavy mediator limit, we find that

$$
\frac {d \sigma_ {\nu \chi}}{d T _ {\chi}} \propto \left\{ \begin{array}{l l} \frac {m _ {\chi}}{m _ {Z ^ {\prime}} ^ {4}}, & \text {f o r} E _ {\nu} \gg m _ {\chi} \\ \frac {T _ {\chi}}{m _ {Z ^ {\prime}} ^ {4}}, & \text {f o r} m _ {\chi} \gg E _ {\nu}. \end{array} \right. \tag {3.5}
$$

On the other hand, if the mediator is light, the differential cross-section follows,

$$
\frac {d \sigma_ {\nu \chi}}{d T _ {\chi}} \propto \left\{ \begin{array}{l l} \frac {1}{T _ {\chi} ^ {2} m _ {\chi}}, & \text {f o r} E _ {\nu} \gg m _ {\chi} \\ \frac {1}{T _ {\chi} m _ {\chi} ^ {2}}, & \text {f o r} m _ {\chi} \gg E _ {\nu}. \end{array} \right. \tag {3.6}
$$

A similar dependence can be worked out for the DM-electron differential cross-section. We find, in the heavy mediator limit,

$$
\frac {d \sigma_ {e \chi}}{d T _ {e}} \propto \left\{ \begin{array}{l l} \frac {m _ {e}}{m _ {Z ^ {\prime}} ^ {4}}, & \text {f o r} T _ {e} \gg m _ {\chi} \\ \frac {m _ {\chi} m _ {e}}{T _ {\chi} m _ {Z ^ {\prime}} ^ {4}}, & \text {f o r} m _ {\chi} \gg T _ {e}. \end{array} \right. \tag {3.7}
$$

On the other hand, if the mediator is light, we find that

$$
\frac {d \sigma_ {e \chi}}{d T _ {e}} \propto \left\{ \begin{array}{l l} \frac {1}{m _ {e} T _ {\chi} ^ {2}}, & \text {f o r} T _ {e} \gg m _ {\chi} \\ \frac {(m _ {\chi} + m _ {e}) ^ {4}}{T _ {\chi} ^ {3} m _ {e} ^ {3} m _ {\chi}}, & \text {f o r} m _ {\chi} \gg T _ {e}, \end{array} \right. \tag {3.8}
$$

where  $T_{e}$  is the electron recoil kinetic energy.

# 3.2 Scalar mediated dark matter-lepton interaction

The second example considers the DM to be a SM singlet Dirac fermion,  $\chi$ , which can interact with neutrinos and electrons through two scalar mediators,  $\Phi^0$  and  $\Phi^{-}$ . This proceeds through the interaction,

$$
\mathcal {L} \supset g _ {\nu} \bar {\nu} \chi \Phi^ {0} - g _ {e} \bar {e} \chi \Phi^ {-}. \tag {3.9}
$$

Just like the vector model, following  $g_{\nu} = g_{e} = g$ , this can be embedded in a UV-complete model. The SM can be augmented with a new scalar doublet,  $\Phi \in [\Phi^{-}, \Phi^{0}]$ . The corresponding Lagrangian can be written as

$$
\mathcal {L} \supset \bar {\chi} (i \partial / - m _ {\chi}) \chi + \partial_ {\mu} \Phi^ {\dagger} \partial^ {\mu} \Phi + g \bar {L} \Phi \chi - \mu_ {\phi} | \Phi | ^ {2} - \lambda_ {\Phi} | \Phi | ^ {4} - \lambda_ {\Phi H} | H | ^ {2} | \Phi | ^ {2} + h. c., \tag {3.10}
$$

where  $H$  is the SM Higgs field and  $L$  is the SM lepton doublet. The assumption of a dark sector symmetry for  $\chi$  and  $\Phi$  can allow one to set the interaction term  $\bar{L} H\chi$  to zero. For our analysis, we consider scenarios,  $m_{\chi} < m_{\Phi}$ , where  $m_{\phi}^{2} = \mu_{\Phi}^{2} + \lambda_{\Phi H}v_{\mathrm{EW}}^{2}$ .

The matrix amplitude squared for the upscattering of  $\chi$  can be computed as

$$
| M | ^ {2} = \frac {g ^ {4}}{2} \frac {\left(t - m _ {\chi} ^ {2}\right) ^ {2}}{\left(t - m _ {\Phi} ^ {2}\right) ^ {2}}. \tag {3.11}
$$

The same interaction also allows the direct detection of boosted DM through the electron scattering channel. The matrix amplitude-squared for the process is given by

$$
\left| M \right| ^ {2} = g ^ {4} \frac {\left[ \left(m _ {\chi} + m _ {e}\right) ^ {2} - t \right] ^ {2}}{\left(t - m _ {\Phi} ^ {2}\right) ^ {2}}. \tag {3.12}
$$

Note that in the case of  $\chi - e$  scattering, a  $t$ -channel resonance can take place if  $t = m_{\phi}^{2}$  is satisfied. This  $t$ -channel singularity is a generic feature of scattering processes where particles are exchanged at the vertices. This can be interpreted in terms of the stability of one of the particles in the initial and final states [81]. In our study, we will not worry about such singularities as it happens for that region of the parameter space which allows for the electron to decay and hence is ruled out from observations. No such singularities exist for the  $\chi - \nu$  channel due to the requirement of  $m_{\phi} > m_{\chi}$ .

Eq. (3.11) can be used to estimate the energy dependence of DM-neutrino differential cross-section in terms of the DM kinetic energy  $(T_{\chi})$ , relevant for our analysis. In the heavy

mediator limit, we find that

$$
\frac {d \sigma_ {\nu \chi}}{d T _ {\chi}} \propto \left\{ \begin{array}{l l} \frac {m _ {\chi}}{m _ {\Phi} ^ {4}}, & \text {f o r} E _ {\nu} \gg m _ {\chi} \\ \frac {m _ {\chi}}{m _ {\Phi} ^ {4}} \left(1 - \frac {4 m _ {\chi} T _ {\chi}}{m _ {\Phi} ^ {2}}\right), & \text {f o r} m _ {\chi} \gg E _ {\nu}. \end{array} \right. \tag {3.13}
$$

On the other hand, if the mediator is light, the differential cross-section follows,

$$
\frac {d \sigma_ {\nu \chi}}{d T _ {\chi}} \propto \left\{ \begin{array}{l l} \frac {1}{T _ {\chi} ^ {2} m _ {\chi}}, & \text {f o r} E _ {\nu} \gg m _ {\chi} \\ \frac {1}{m _ {\chi} ^ {3}}, & \text {f o r} m _ {\chi} \gg E _ {\nu}. \end{array} \right. \tag {3.14}
$$

A similar dependence can be worked out for the DM-electron differential cross-section. We find, in the heavy mediator limit,

$$
\frac {d \sigma_ {e \chi}}{d T _ {e}} \propto \left\{ \begin{array}{l l} \frac {m _ {e}}{m _ {\Phi} ^ {4}}, & \text {f o r} T _ {e} \gg m _ {\chi} \\ \frac {m _ {\chi} m _ {e}}{T _ {\chi} m _ {\Phi} ^ {4}}, & \text {f o r} m _ {\chi} \gg T _ {e}. \end{array} \right. \tag {3.15}
$$

On the other hand, if the mediator is light, we find that

$$
\frac {d \sigma_ {e \chi}}{d T _ {e}} \propto \left\{ \begin{array}{l l} \frac {1}{m _ {e} (2 T _ {\chi} - m _ {e}) ^ {2}}, & \text {f o r} T _ {e} \gg m _ {\chi} \\ \frac {m _ {\chi} m _ {e}}{T _ {\chi} (m _ {\chi} - m _ {e}) ^ {4}}, & \text {f o r} m _ {\chi} \gg T _ {e}, \end{array} \right. \tag {3.16}
$$

where  $T_{e}$  is the electron kinetic energy.

These dependencies discussed above can be confirmed from figure 2, which compares the differential cross-section as a function of  $T_{\chi}$  between the constant cross-section case and the case with scalar/vector mediators. The left panels focus on DM-neutrino cross-sections, whereas the right panels show DM-electron cross-sections. Previous studies with constant DM cross-sections usually assumed these two cross-sections to be identical. However, it is important to stress that these two cross-sections are different in general, and there is no reason for them to be considered equal unless the underlying model demands it to be. The top and bottom panels are for two different representative values of  $E_{\nu}$  and  $T_{e}$  respectively. For the top left panel, the neutrino energy is fixed to the minimum energy required to boost DM to kinetic energies  $T_{\chi}$ , whereas the bottom left panel shows the plots for a representative value  $E_{\nu} = 10 \mathrm{MeV}$ . Similarly, for the top right panel, we fix the recoil electron energy  $(T_{e})$  to the maximum value that can be achieved upon scattering with BDM of energy  $T_{\chi}$ , whereas for the bottom right panel, we choose  $T_{e} = 5 \mathrm{keV}$ . The limiting behaviour of the differential cross-sections can be qualitatively understood from eqs. (3.5)-(3.8), and eqs. (3.13)-(3.16) respectively.

![](images/43c5d3e97ce75186653a2e341a5710fda3c1facefd0d1be74044d8a5994e0f36.jpg)

![](images/eddc810211d64215591f22ed749a5284db6042d092bb79a1f1bbbdffdb5f9469.jpg)

![](images/b2860650d294156b235a7c3867501ecb10a48436043794e807a6998921484b65.jpg)  
Figure 2. Comparison of the differential cross-section of neutrinos and electrons with DM. We present benchmark point with a mediator mass of  $1\mathrm{MeV}$ ,  $m_{\chi} = 0.1\mathrm{MeV}$  and fix the scalar and gauge couplings such that  $\bar{\sigma}_{e\chi} = 10^{-30}\mathrm{cm}^2$ . Top Left: differential cross-section for the interaction of neutrinos with DM at rest as a function of kinetic energy gained by DM. The neutrino energy is fixed to the minimum energy required to boost DM to kinetic energies  $T_{\chi}$ . Top Right: differential cross-section for scattering of BDM with electrons at rest as a function of BDM kinetic energy. We fix the recoil electron energy to the maximum value that can be achieved upon scattering with BDM of energy  $T_{\chi}$ . Bottom row: same as above but with the incident neutrino energy and electron recoil energy fixed to  $E_{\nu} = 10\mathrm{MeV}$  and  $T_{e} = 5\mathrm{keV}$  respectively.

![](images/cec1af7ab2daa7562a23006f6b96b50f28ba3a2e0686753dbf6ab721aa257037.jpg)

# 4 Boosted dark matter

The neutrinos from the DSNB can scatter off ambient DM particles and transfer a part of their energy, resulting in a fraction of the DM being boosted to high energies. As a result, the DM particles have kinetic energy that significantly exceeds the energy from their virial motion in galactic structures. From kinematic considerations, it follows that for a neutrino hitting a DM particle at rest, the transferred kinetic energy is given by

$$
T _ {\chi} = T _ {\chi} ^ {\max } \left(\frac {1 - \cos \theta}{2}\right), \qquad T _ {\chi} ^ {\max } = \frac {E _ {\nu} ^ {2}}{E _ {\nu} + m _ {\chi} / 2}. \tag {4.1}
$$

Here  $E_{\nu}$  is the neutrino energy and,  $\theta$  is the scattering angle in the centre of momentum frame. The resulting BDM flux in the Milky Way halo is obtained by performing a line-of-sight integral over all possible directions of incoming DM that was upscattered by the DSNB. For

a given DSNB flux spectrum  $d\Phi_{\nu} / dE_{\nu}$ , the flux of boosted DM reads [13, 28, 37, 39]

$$
\frac {d \Phi_ {\chi}}{d T _ {\chi}} = \int \frac {d \Omega}{4 \pi} \int_ {\mathrm {l . o . s .}} d l \int_ {E _ {\nu} ^ {\mathrm {m i n}}} ^ {E _ {\nu} ^ {\mathrm {m a x}}} d E _ {\nu} \frac {\rho_ {\chi} (l)}{m _ {\chi}} \frac {d \Phi_ {\nu}}{d E _ {\nu}} \frac {d \sigma_ {\nu \chi}}{d T _ {\chi}} \equiv D _ {\mathrm {h a l o}} \int_ {E _ {\nu} ^ {\mathrm {m i n}}} ^ {E _ {\nu} ^ {\mathrm {m a x}}} d E _ {\nu} \frac {1}{m _ {\chi}} \frac {d \Phi_ {\nu}}{d E _ {\nu}} \frac {d \sigma_ {\nu \chi}}{d T _ {\chi}}. (4. 2)
$$

In the above equation, we have exploited the factorization of halo dependence and the underlying particle physics. We assume that the DM density in the MW halo  $\rho_{\chi}(r)$  follows a Navarro-Frenk-White (NFW) profile [82]

$$
\rho_ {\chi} (r) = \rho_ {s} \frac {\left(\frac {r}{r _ {s}}\right) ^ {- \gamma}}{1 + \left(\frac {r}{r _ {s}}\right) ^ {\beta - \gamma}}, \tag {4.3}
$$

where  $r$  is the radial distance from the Galactic centre (GC), and  $\beta, \gamma, r_s$  are fitting parameters. Following the NFW profile  $(\beta, \gamma, r_s) = (3, 1, 20\mathrm{kpc})$ , we get  $D_{\mathrm{halo}} = 2.04\times 10^{25}\mathrm{MeVcm}^{-2}$ . The precise value of  $D_{\mathrm{halo}}$  depends on assumptions made on the nature of the DM halo profile. For various choices of the halo following [83], we find that the difference is not more than  $\mathcal{O}(1\%)$ , which agrees with what was found in [39].

# 4.1 Attenuation

On their way to the detector, boosted DM particles can interact with electrons in the atmosphere and the earth and lose energy before reaching the detector site. For sufficiently strong interactions, this can lead to distortion and ultimately attenuation of the differential BDM flux. We model the mean energy loss of a single DM particle travelling through a medium by the energy loss equation (e.g. [27, 28, 69])

$$
\frac {d T _ {\chi}}{d x} (x) = - \sum_ {i} n _ {i} (x) \int_ {0} ^ {T _ {i} ^ {\max }} d T _ {i} T _ {i} \frac {d \sigma_ {i \chi}}{d T _ {i}}. \tag {4.4}
$$

Here we sum over all medium constituents that may participate in the scattering, their respective number densities  $(n_i)$  as a function of distance  $x$ , and integrate over the energy lost in a single interaction. Note that only in the case of elastic scattering,  $T_{i}$  correspond to the recoil energy. In this case, the maximum energy that can be transferred is [28]

$$
T _ {i} ^ {\mathrm {m a x}} = \frac {T _ {\chi} ^ {2} + 2 m _ {\chi} T _ {\chi}}{T _ {\chi} + (m _ {\chi} + m _ {i}) ^ {2} / (2 m _ {\chi})}, \tag {4.5}
$$

where  $m_{i}$  is the mass of the target particle, assumed to be at rest.

Under certain assumptions, eq. (4.4) admits an analytic solution. For  $d\sigma_{i\chi} / dT_i = \sigma_i / T_i^{\max}$  the constant cross-section assumption, the integral can be performed analytically. If we also assume  $T_{\chi} \ll m_{i}$ , we find

$$
\frac {d T _ {\chi}}{d x} = - \frac {1}{2} \sum_ {i} n _ {i} \sigma_ {i} T _ {i} ^ {\max} \approx - \frac {T _ {\chi} ^ {2} + 2 m _ {\chi} T _ {\chi}}{2 m _ {\chi} l}, \quad \mathrm {w h e r e} \quad l ^ {- 1} = \sum_ {i} n _ {i} \sigma_ {i} \frac {2 m _ {i} m _ {\chi}}{(m _ {i} + m _ {\chi}) ^ {2}}. (4. 6)
$$

Solving the resulting ODE yields

$$
T _ {\chi} (x) \equiv T _ {\chi} ^ {x} = T _ {\chi} ^ {0} \frac {e ^ {- x / l}}{1 + \frac {T _ {\chi} ^ {0}}{2 m _ {\chi}} \left(1 - e ^ {- x / l}\right)}, \tag {4.7}
$$

which can also be inverted to find  $T_{\chi}^{0}(T_{\chi}^{x}, x)$ . This allows us to express the attenuated flux at the detector as

$$
\frac {d \Phi_ {\chi}}{d T _ {\chi} ^ {x}} = \int \frac {d \Omega}{4 \pi} \frac {d \Phi_ {\chi} ^ {0}}{d T _ {\chi} ^ {0}} \frac {d T _ {\chi} ^ {0}}{d T _ {\chi} ^ {x}}, \tag {4.8}
$$

where we take into account that BDM flux from different directions travelled a different distance  $x$  through the earth, depending on the angle  $\theta$  of arrival to the detector [28, 39].

The analytic solution is however not suitable for our case for multiple reasons. In the following, we only consider scattering on electrons and assume a constant electron density  $n_e = 8 \times 10^{23} \, \mathrm{cm}^{-3}$  [39]. The models we consider do not assume additional interactions with nucleons for simplicity. Hence any constraints we put are conservative in terms of the estimated energy loss from attenuation, since additional scattering targets make energy loss more efficient.

For typical BDM energies, we do not expect  $T_{\chi} \ll m_e$  to be valid all the time. Moreover, the assumption of a constant cross-section  $(d\sigma_{i\chi} / dT_i = \sigma_i / T_i^{\max})$  is an oversimplification. Depending on the details of the interaction, the probability, and hence the efficiency of mean energy loss, depends on the current mean energy  $T_{\chi}^{x}$ . Thus, different parts of the BDM energy spectrum experience a different energy loss rate, which can ultimately lead to an over or underestimation of detector events compared to the constant cross-section case. This necessitates a numerical solution of eq. (4.4). We describe the procedure below.

The full numerical implementation of the upscattering, boosting, and arrival at the detector follows an instructive sequence of steps. After selecting a specific model, we specify all relevant parameters, e.g., DM mass, mediator mass, couplings, etc. We use eq. (4.2) for a given model to numerically find the unattenuated flux of BDM at earth. To find the attenuated BDM at some detector depth  $h_d$ , we repeatedly solve eq. (4.4) for many different initial energies  $T_0^\chi$ . We find a grid of  $T_{\chi}^{x}(x,T_{\chi}^{0})$  for every point in the parameter space on which we can smoothly interpolate. For any fixed value of  $x$ , we can determine  $T_0^\chi (T_\chi^x)$  and the Jacobian  $\frac{dT_{\chi}^{x}}{dT_{\chi}^{0}} (T_{\chi}^{0}(T_{\chi}^{x},x),x)$  and exploit the relation  $\frac{dT_{\chi}^{x}}{dT_{\chi}^{0}} = \left(\frac{dT_{\chi}^{0}}{dT_{\chi}^{x}}\right)^{-1}$ . The differential flux at the detector site is now given by eq. (4.8), which can also be turned into an integration over  $x$ . For the relation of the angle  $\theta$  to the overburden  $x$ , see [39].

The numerical scheme as described above comes with several technical difficulties. To connect the entire BDM spectrum at the surface to that at the detector site, eq. (4.4) needs to be solved repeatedly even for a single point in parameter space to obtain a reliable grid for interpolation. This requires a stable ODE solution over orders of magnitude in depth and energy for many initial energies which also vary over the dominant range of energies for the BDM flux at the surface. Depending on model parameters, the rate of energy loss also varies by orders of magnitude in a parameter scan for which we have to guarantee the stability of the solver. Moreover, the solution exhibits singular behaviour, i.e., full loss of energy within finite depth. The final result, by virtue of the angular integration in eq. (4.8), depends on very different energy loss regimes and combines singular and non-singular partial solutions.

Although such a solution is expected to be a significant improvement on previous treatments, the resulting BDM fluxes and derived constraints provide only a conservative estimate. Here we work with the assumption of negligible deflection of BDM particles. Our

treatment also neglects multiple scatterings which become important as  $\lambda_{\mathrm{scat}} = (n\sigma)^{-1}$  no longer exceeds the depth of the detector location  $h_d$  by a significant margin.

# 5 Results

For all the following analyses, we set the relevant couplings to be the same, i.e.,  $g_{\nu} = g_{e} = g_{\chi} = g$ . We will comment later on the possibility of relaxing this assumption. To compare with results from the direct detection experiments, we use the effective cross-section

$$
\bar {\sigma} _ {e \chi} = \frac {g ^ {4}}{\pi} \frac {\mu_ {e \chi} ^ {2}}{(q _ {\mathrm {r e f}} ^ {2} + m _ {\mathrm {m e d}} ^ {2}) ^ {2}}, (5. 1)
$$

which can be used to replace couplings in the differential cross-section with the effective cross-section. We follow the conventional definition of  $q_{\mathrm{ref}} = \alpha m_e$ , involving the fine structure constant, to compare with other works. Note that for a variety of models, this gives the correct scale of momentum transfer, for e.g., if we consider an energy-independent cross-section or a vector mediator. However, the scalar model we consider is more subtle. Due to the conversion of particle species by a t-channel exchange, there is a mass splitting of  $\Delta m$  between the incoming and outgoing particles on the same fermion line. Thus, a second mass scale is present in the process. The momentum transfer to overcome this gap may be much larger than the typical transfer naively expected from  $q_{\mathrm{ref}} = \alpha m_e$ . In those circumstances,  $q_{\mathrm{ref}} = \Delta m$  is a more natural definition. However to maintain comparability with previous results we adopt the original definition of  $q_{\mathrm{ref}}$  exclusively. In some cases, this leads to an apparent offset of the scalar cross-section when compared to the constant one. This is a matter of definition and not connected to any physical effects.

# 5.1 Impact of Lorentz structure on upscattering and attenuation

We illustrate the effect of Lorentz structure on DM upscattering and attenuation of the DM flux in figure 3 for two different benchmark points. The resulting BDM spectra are best understood in light of the previous discussion on the energy dependence of the cross-sections. Compared to the constant cross-section case (dashed blue), the inclusion of the underlying Lorentz structure can change the BDM spectra considerably. In particular, upscattering by neutrinos is suppressed for the scalar model (dashed orange) and slightly enhanced for the vector model (dashed green) for the same effective cross-section, as compared to the constant case. This can be seen in the unattenuated BDM spectra for both benchmark points.

Similarly, the energy dependence of DM electron scattering has a strong impact on the attenuation of the BDM flux arriving at the detector, as shown by the solid coloured lines in figure 3. This is due to the behaviour of the energy-dependent cross-sections, as shown in figure 2 and discussed in section 3. For example, we find that for the benchmark point,  $\bar{\sigma}_{e\chi} = 10^{-30}\mathrm{cm}^2$ , mediator  $1\mathrm{MeV}$ , and  $m_{\chi} = 0.1\mathrm{MeV}$ , we find a peak followed by a strong falloff in the BDM spectra for the vector model. This is because, for these values of the parameters, the differential  $e - \chi$  spectra remain almost constant with  $T_{\chi}$  as shown in the bottom right panel of figure 2. As a result, depending on the energy of the BDM, attenuation affects the spectra in a qualitatively different manner, thereby leading to model-dependent BDM fluxes at the detector sites, which cannot be accurately approximated by a constant

![](images/bac71936324c1f19ea96b07dcc5f9bc1bc8ad60bdee6a92e93ed018c461ec260.jpg)  
Figure 3. Attenuated and unattenuated BDM spectra for two benchmark points for the models we consider. For the left plot we assume  $\bar{\sigma}_{e\chi} = 10^{-30}\mathrm{cm}^2$ , mediator 1 MeV, and  $m_{\chi} = 0.5\mathrm{MeV}$ . The right plot shows the spectra for  $\bar{\sigma}_{e\chi} = 10^{-30}\mathrm{cm}^2$ , mediator 1 MeV, and  $m_{\chi} = 0.1\mathrm{MeV}$ . To calculate the attenuated spectrum we employ a detector location at depth  $h_d = 1.4\mathrm{km}$ . The definition of  $\bar{\sigma}_{e\chi}$  is given in eq. (5.1).

![](images/7b7c899a7957f81b9743af76993383ff93ad85c9a4f9b9689a51f9f81ba8e066.jpg)

cross-section. The variation in the final signal event rate in the detector for different models can also be described using similar arguments.

# 5.2 Expected electron recoil event rates

The differential electron recoil event rate is given by

$$
\frac {d R}{d T _ {e}} = N _ {e} \int d T _ {\chi} \frac {d \Phi_ {\chi}}{d T _ {\chi} ^ {z}} \frac {d \sigma_ {e \chi}}{d T _ {e}}. \tag {5.2}
$$

For the number of electron targets in the detector we find  $N_{e} = M_{\mathrm{det}} / m_{\mathrm{Xe}}Z_{\mathrm{eff}}(T_{e})$ , involving the total mass of detector material, the mass of a xenon atom and  $Z_{\mathrm{eff}}(T_e)$  is the general energy-dependent effective charge number seen by a recoiling DM particle. Throughout the analysis, we assume constant  $Z_{\mathrm{eff}}(T_e)\approx 40$ . We take the convolution of the resulting recoil spectrum with a detector-specific resolution function. For all experiments considered this resolution function is Gaussian in shape

$$
I (E _ {R}, T _ {e}) = \frac {1}{\sqrt {2 \pi \sigma (T _ {e}) ^ {2}}} \exp \left(- \frac {(T _ {e} - E _ {R}) ^ {2}}{2 \sigma (T _ {e}) ^ {2}}\right), \tag {5.3}
$$

where  $T_{e}$  is the "true" deposited energy and  $E_{R}$  the observed energy in the detector. We use the detector resolutions (in keV) provided by the respective collaboration, i.e.  $\sigma_{\mathrm{XE}} = 0.31\sqrt{E / \mathrm{keV}} + 0.0037E / \mathrm{keV}$  [84],  $\sigma_{\mathrm{LZ}} = 0.323\times 10^{-1.5}\sqrt{E / \mathrm{keV}}$  [4], and  $\sigma_{\mathrm{PA}} = 0.073 + 0.173E / \mathrm{keV} - 6.5\times 10^{-3}(E / \mathrm{keV})^{2} + 1.1\times 10^{-4}(E / \mathrm{keV})^{3}$  [6] for XENONnT, LZ and PandaX, respectively. The convoluted signal is then multiplied by the respective efficiency function also provided by the collaboration. We show example electron recoil spectra from BDM scattering in three experiments for the constant cross-section case, and a benchmark point for the scalar and the vector model in figure 4, along with the data. In the next subsection, we proceed to perform a statistical analysis of the hypothesis with the experimental data.

![](images/85bd6033c133bcb177b5b6401812f3689a70755b5bb171ff1c395c6be5ba9620.jpg)  
Figure 4. Expected electron recoil event rates in XENONnT (left), LZ (middle), and PandaX (right) with respective experimental background for benchmark point  $\bar{\sigma}_{e\chi} = 10^{-30}\mathrm{cm}^2$ , mediator mass  $1\mathrm{MeV}$  and  $m_{\chi} = 0.5\mathrm{MeV}$ . We show the rates for constant cross-section (blue), vector (green), and scalar (orange) mediator models.

![](images/a627ef8843ecceca1cb2315645f61115fe7afa541bfab55b43ccca8edcd03fc3.jpg)

![](images/229ec59b8e5ad69ad487de299dd76a5ff5092edaf9d5082256ee197c6806b2f4.jpg)

# 5.3 Statistical analysis

To calculate the constraints on the parameter space  $(\bar{\sigma}_{e\chi},m_{\chi})$ , we use the following  $\chi^2$  statistic,

$$
\chi^ {2} = \sum_ {E _ {i}} \frac {\left(R _ {i} ^ {\operatorname* {p r e d}} (E _ {i}) - R _ {i} ^ {\exp} (E _ {i})\right) ^ {2}}{\sigma_ {i} ^ {2} (E _ {i})}, \tag {5.4}
$$

for each of the experiments considered. Here  $R_{i}^{\mathrm{pred}}$  denotes the predicted event rates, which include the DSNB boosted DM contribution as well as the experimental background. For the fixed background, we use what is provided as the best-fit background model for each experiment. Thus, constraints derived from our approach are conservative, since we do not attempt a joint fit of the BDM and the background. Reported event rates from the experimental collaborations are denoted by  $R_{i}^{\mathrm{exp}}$ . The net uncertainty in the model and data is given by

$$
\sigma_ {i} ^ {2} (E _ {i}) = R _ {i} ^ {\mathrm {p r e d}} (E _ {i}) + \sigma_ {\mathrm {D i}} ^ {2} (E _ {i}), \tag {5.5}
$$

where we estimate the event rate uncertainties  $(\sigma_{\mathrm{Di}})$  by combining a Poissonian counting error on the total predicted event rate with the experimental uncertainty from the experiment. For the exclusion contours, we use a  $\chi^2$  difference to the best-fit background model, i.e.  $\Delta \chi^2 = \chi^2 - \chi_{\mathrm{bkg}}^2$  and exclude regions with  $\Delta \chi^2 > 4.61$  at  $90\%$  confidence level (CL).

We present the resulting exclusion regions for the three experiments for the vector and scalar mediators in figure 5 and figure 6 respectively. For reference, we also show constraints assuming a constant cross-section. The differences in these constraints compared to previous studies arise from relaxing the assumptions needed for the approximate analytical solution [39]. The effect of mediator mass dependence on the constraints is found to be pronounced even without attenuation. In the case of a vector mediator, the full energy-dependent cross-section (coloured lines) tends to put stronger constraints than the energy-independent cross-section (black lines). This can be traced back to the enhanced cross-section for both the DM upscattering and interaction in the detector. We find that, in the absence of attenuation, for heavier mediators, the exclusion region is larger, whereas for lighter mediators it shrinks considerably to lower values of  $m_{\chi}$ . The effect of attenuation is two-fold. Firstly, the exclusion region

![](images/c4eddf6b0004048463a6e3e95d589a1e321a9e52ed2e14062e94dd6e00369c87.jpg)

![](images/c93cdc95575b35611ec20b0dd60254a1c464bb1e0784ed4980333e44914d7c68.jpg)

![](images/44c25b21b3e135a0474c6f0bff597bfa4889abff44ec29e0e2e430c6a04edf2c.jpg)  
Figure 5. Constraints on parameter space for the vector mediator model with four values of the mediator mass  $m_{Z^{\prime}} = 0.1$  (yellow), 1 (purple), 10 (orange), and  $100\mathrm{MeV}$  (blue). Coloured regions are excluded at  $90\%$  CL. The constraint assuming a constant cross-section (energy-independent) is shown in black. The dashed lines show the corresponding constraints in the absence of attenuation.

includes an upper limit (ceiling) on the interaction strength due to the complete attenuation of BDM. We note that some of the presented constraints exhibit numerical artifacts at the predicted ceiling edges, the precise position of which is highly sensitive to the DM coupling. These features appear due to finite parameter grid resolution. Secondly, we observe an enhancement of the constraints for lower values of  $m_{\chi}$ . This can be attributed to the down scattering of higher energetic BDM to lower energies more favourable for detection in the experiments.

For scalar-mediated interactions, the shape of the constraints is qualitatively distinct from the vector-mediated interactions. For most of the available parameter space, they tend to be weaker when compared to the constant cross-section case if attenuation is not considered. As the DM mass approaches the mediator mass, constraints become particularly strong. This can be traced to the resonant behaviour of the electron-DM cross-section, cf eq. (3.15), and it further highlights the importance of the underlying Lorentz structure. On the other hand, the effects of attenuation are similar to the vector case with the typical upper limit and enhancement on the lower limit of the constraints. The latter is very pronounced for the scalar mediator case. We do not discuss limits for  $m_{\chi} > m_{\Phi}$ , which would introduce an annihilation channel of DM in the considered model. For this reason, we also do not

![](images/98f06d540f2e7b2857258f104e4fefd204e82917e46cebc1fffcbd52a0a70a53.jpg)

![](images/085290212bb573053c004f5dbebf53b6bad4ee1336ee8351cd74c246c6020425.jpg)

![](images/1ed57fd6e5c68b96bc72a1b9630a580dc6caaa5ae55cab6f80824cb74a67114b.jpg)  
Figure 6. Constraints on the parameter space for the scalar mediator model with two values of the mediator mass  $m_{\Phi} = 10$  (red) and  $100\mathrm{MeV}$  (blue). Coloured regions are excluded at  $90\%$  CL. The constraint assuming a constant cross-section (energy-independent) is shown in black. The dashed lines show the corresponding constraints in the absence of attenuation.

present constraints for even lighter mediator masses. Due to the stability condition they would only cover little parameter space in the mass range we consider.

As expected, the constraints cast by XENONnT and LZ are similar, as they employ a similar technology and are located at an approximately similar depth of  $h_d \simeq 1.4\mathrm{km}$  from the surface. The results from PandaX tend to be slightly weaker compared to LZ and XENONnT. Since the former is located at a greater depth of  $h_d \simeq 2.4\mathrm{km}$ , the attenuation of the BDM flux is stronger. This leads to a weakening of both limits, the attenuation-induced upper limit, as well as the constraints on the lower mass of DM. This is a result of the additional overburden, hence the overall loss of energy of BDM flux will not be locally compensated by overproducing DM with favourable kinetic energies for direct DM detection.

Let us emphasize again that the limits derived in figure 5 and figure 6 assume  $g_{\nu} = g_{e}$ . From a phenomenological point of view, these two couplings can be different and can yield different results for the same scenario. To demonstrate our point, we show in figure 7 the constraints for the specific case of vector mediator of mass  $m_Z' = 10$  MeV for three values of  $g_{\nu} = g_{e}$ ,  $g_{e}/2$ ,  $2g_{e}$  in XENONnT. We find that the lower bound on the exclusion region shifts depending on the value of  $g_{\nu}$ , while the upper limit remains virtually unchanged. This

![](images/398ba6f9e61f8059f3ff4b9bd3a15fe9ee488e05dabf3b21a4b07a4d27bc7c98.jpg)  
Figure 7. The effect of changing neutrino-DM coupling  $g_{\nu}$  relative to  $g_{e}$  on the constraints set by XENONnT. The attenuation ceiling is barely influenced, since the dominant effect of changing  $g_{\nu}$  is changing the overall flux of BDM. The position of the ceiling is mildly sensitive to the overall flux but exponentially sensitive to  $g_{e}$ . The lower limits are dominated by the BDM flux and hence is affected by the change in  $g_{\nu}$ .

is expected since the upper limit is fixed by the attenuation and depends on the value of  $g_{e}$ , whereas changing  $g_{\nu}$  affects the BDM flux.

Finally, we note that the limits we derived in this study are at relatively large DM cross-section values. This is a generic feature of boosted DM models as it requires DM to scatter twice with electrons and neutrinos. These cross-sections are excluded by other astrophysical observations and laboratory experiments [8, 9, 85-87]. We do not display these additional constraints in our figures for clarity. However, a variety of additional constraints in these regions of parameter space require separate analysis since the exact nature of the constraint depends on the energy dependence of the DM-electron scattering cross-section, which has a significant impact on the resulting limits.

# 6 Summary and conclusions

Abundant neutrinos from past SN explosions in the Universe provide a testing ground for DM interactions with leptons. In this study, we analysed boosted DM due to upscattering with energetic neutrinos from the DSNB. Focusing on minimal leptophilic DM models, where DM interacts with neutrinos and electrons through a scalar or a vector boson, we explored attenuation of the DM flux due to in-medium propagation as well as experimental signatures. Previous studies have focused on the simplifying assumption of constant DM interaction cross-sections and an analytic treatment of attenuation. We expand on the treatment of attenuation and discard the analytic treatment of attenuation in favour of a full numerical solution. We find this to be relevant even in the case of constant cross-section. We demonstrated that the inclusion of an energy-dependent cross-section significantly affects the boosted DM flux and the detection prospects.

We analyzed the constraints on boosted DM using recent data from XENONnT, LZ, and PandaX-4T large underground direct DM detection experiments. As expected, the rate of attenuation also depends on the details of the underlying DM model considered, differing considerably from the constant cross-section case. With the effects of attenuation taken into account, we derived constraints on the model parameter space from these direct detection experiments and set new limits on DM neutrino and electron interactions for DM masses in the range  $\sim (0.1, 10^4)$  MeV. By considering the energy dependence of DM interaction cross-sections, we demonstrated that resulting constraints can differ by multiple orders of magnitude compared to those found assuming constant cross-sections. These results showcase the inadequacies of the approximation of a constant cross-section as considered in previous studies.

Our work highlights the significance of the DSNB as an excellent target for probing neutrino-DM interactions. With the doping of the SK experiment with Gd, the expected sensitivity holds promise for DSNB detection in the near future. This discovery would open new avenues in neutrino astronomy. In light of this, our work is timely and sets the ground for further exploration of connections between this omnipresent astrophysical neutrino background and DM.

# Acknowledgments

We thank John Beacom, Shunsaku Horiuchi, Anna Suliga for discussion. We acknowledge the extensive use of FEYNCALC, NUMPY, SCIPY, MATLAB in this work [88-91]. AD gratefully acknowledges the hospitality at APCTP during the program "Dark Matter as a Portal to New Physics". AD was supported by Grant Korea NRF-2019R1C1C1010050. TH acknowledges support from the IMPRS-PTFS. MS acknowledges the hospitality of the Network for Neutrinos, Nuclear Astrophysics, and Symmetries (N3AS) Physics Frontier Center of UC Berkeley where part of this work was carried out. TH and MS would like to thank Paul Frederik Depta for insightful discussions. The work of VT was supported by the World Premier International Research Center Initiative (WPI), MEXT, Japan. VT acknowledges support the JSPS KAKENHI Grant 23K13109.

# References

[1] G.B. Gelmini, The Hunt for Dark Matter, in the proceedings of the Theoretical Advanced Study Institute in Elementary Particle Physics: Journeys Through the Precision Frontier: Amplitudes for Colliders, Boulder, U.S.A., 02-27 June 2014 [DOI:10.1142/9789814678766_0012] [arXiv:1502.01320] [INSPIRE].  
[2] D.S. Akerib et al., Snowmass 2021 Cosmic Frontier Dark Matter Direct Detection to the Neutrino Fog, in the proceedings of the Snowmass 2021, Seattle, U.S.A., 17-26 July 2022 [arXiv:2203.08084] [INSPIRE].  
[3] XENON collaboration, First Dark Matter Search with Nuclear Recoils from the XENONnT Experiment, Phys. Rev. Lett. 131 (2023) 041003 [arXiv:2303.14729] [INSPIRE].  
[4] LZ collaboration, First Dark Matter Search Results from the LUX-ZEPLIN (LZ) Experiment, Phys. Rev. Lett. 131 (2023) 041002 [arXiv:2207.03764] [INSPIRE].

[5] LZ collaboration, Background determination for the LUX-ZEPLIN dark matter experiment, Phys. Rev. D 108 (2023) 012010 [arXiv:2211.17120] [INSPIRE].  
[6] PANDAX collaboration, Search for Light Fermionic Dark Matter Absorption on Electrons in PandaX-4T, Phys. Rev. Lett. 129 (2022) 161804 [arXiv:2206.02339] [INSPIRE].  
[7] XENON collaboration, Search for New Physics in Electronic recoil Data from XENONnT, Phys. Rev. Lett. 129 (2022) 161805 [arXiv:2207.11330] [INSPIRE].  
[8] DAMIC-M collaboration, First Constraints from DAMIC-M on Sub-GeV Dark-Matter Particles Interacting with Electrons, Phys. Rev. Lett. 130 (2023) 171003 [arXiv:2302.02372] [INSPIRE].  
[9] SENSEI collaboration, SENSEI: First Direct-Detection Results on sub-GeV Dark Matter from SENSEI at SNOLAB, arXiv:2312.13342 [INSPIRE].  
[10] SUPERCDMS collaboration, Constraints on low-mass, relic dark matter candidates from a surface-operated SuperCDMS single-charge sensitive detector, Phys. Rev. D 102 (2020) 091101 [arXiv:2005.14067] [INSPIRE].  
[11] R. Essig et al., Snowmass2021 Cosmic Frontier: The landscape of low-threshold dark matter direct detection in the next decade, in the proceedings of the Snowmass 2021, Seattle, U.S.A., 17-26 July 2022 [arXiv:2203.08297] [INSPIRE].  
[12] Y. Zhang, Speeding up dark matter with solar neutrinos, PTEP 2022 (2022) 013B05 [arXiv:2001.00948] [INSPIRE].  
[13] A. Das and M. Sen, Boosted dark matter from diffuse supernova neutrinos, Phys. Rev. D 104 (2021) 075029 [arXiv:2104.00027] [INSPIRE].  
[14] Y.-H. Lin, W.-H. Wu, M.-R. Wu and H.T.-K. Wong, Searching for Afterglow: Light Dark Matter Boosted by Supernova Neutrinos, Phys. Rev. Lett. 130 (2023) 111002 [arXiv:2206.06864] [INSPIRE].  
[15] Y.-H. Lin et al., Signatures of afterglows from light dark matter boosted by supernova neutrinos in current and future large underground detectors, Phys. Rev. D 108 (2023) 083013 [arXiv:2307.03522] [INSPIRE].  
[16] R. Bernabei et al., Investigating electron interacting dark matter, Phys. Rev. D 77 (2008) 023506 [arXiv:0712.0562] [INSPIRE].  
[17] A. Falkowski, J. Juknevich and J. Shelton, Dark Matter Through the Neutrino Portal, arXiv:0908.1790 [INSPIRE].  
[18] P.J. Fox and E. Poppitz, Leptophilic Dark Matter, Phys. Rev. D 79 (2009) 083528 [arXiv:0811.0399] [INSPIRE].  
[19] S. Chang, R. Edezhath, J. Hutchinson and M. Luty, Leptophilic Effective WIMPs, Phys. Rev. D 90 (2014) 015011 [arXiv:1402.7358] [INSPIRE].  
[20] M. Lindner, A. Merle and V. Niro, Enhancing Dark Matter Annihilation into Neutrinos, Phys. Rev. D 82 (2010) 123529 [arXiv:1005.3116] [INSPIRE].  
[21] V. Gonzalez Macias and J. Wudka, *Effective theories for Dark Matter interactions and the neutrino portal paradigm*, JHEP 07 (2015) 161 [arXiv:1506.03825] [INSPIRE].  
[22] M. Blennow et al., Neutrino Portals to Dark Matter, Eur. Phys. J. C 79 (2019) 555 [arXiv:1903.00006] [INSPIRE].  
[23] P. Fileviez Pérez, C. Murgui and A.D. Plascencia, Neutrino-Dark Matter Connections in Gauge Theories, Phys. Rev. D 100 (2019) 035041 [arXiv:1905.06344] [INSPIRE].

[24] F. D'Eramo and J. Thaler, Semi-annihilation of Dark Matter, JHEP 06 (2010) 109 [arXiv:1003.5912] [INSPIRE].  
[25] K. Agashe, Y. Cui, L. Necib and J. Thaler, (In)direct Detection of Boosted Dark Matter, JCAP 10 (2014) 062 [arXiv:1405.7370] [INSPIRE].  
[26] J. Berger, Y. Cui and Y. Zhao, Detecting Boosted Dark Matter from the Sun with Large Volume Neutrino Detectors, JCAP 02 (2015) 005 [arXiv:1410.2246] [INSPIRE].  
[27] Y. Ema, F. Sala and R. Sato, Light Dark Matter at Neutrino Experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[28] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[29] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse Direct Detection: Cosmic Ray Scattering With Light Dark Matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[30] W. Yin, Highly-boosted dark matter and cutoff for cosmic-ray neutrinos through neutrino portal, EPJ Web Conf. 208 (2019) 04003 [arXiv:1809.08610] [INSPIRE].  
[31] K. Kannike et al., Dark Matter and the XENON1T electron recoil excess, Phys. Rev. D 102 (2020) 095002 [arXiv:2006.10735] [INSPIRE].  
[32] B. Fornal et al., Boosted Dark Matter Interpretation of the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 161804 [arXiv:2006.11264] [INSPIRE].  
[33] H. Alhazmi et al., Implications of the XENON1T Excess on the Dark Matter Interpretation, JHEP 05 (2021) 055 [arXiv:2006.16252] [INSPIRE].  
[34] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, *Cosmic-Neutrino-Boosted Dark Matter (νBDM)*, arXiv:2101.11262 [INSPIRE].  
[35] A. Das, Y.F. Perez-Gonzalez and M. Sen, Neutrino secret self-interactions: A booster shot for the cosmic neutrino background, Phys. Rev. D 106 (2022) 095042 [arXiv:2204.11885] [INSPIRE].  
[36] J. Berger et al., Snowmass 2021 White Paper: Cosmogenic Dark Matter and Exotic Particle Searches in Neutrino Experiments, in the proceedings of the Snowmass 2021, Seattle, U.S.A., 17-26 July 2022 [arXiv:2207.02882] [INSPIRE].  
[37] D. Bardhan et al., Bounds on boosted dark matter from direct detection: The role of energy-dependent cross sections, Phys. Rev. D 107 (2023) 015010 [arXiv:2208.09405] [INSPIRE].  
[38] T.N. Maity and R. Laha, Cosmic-ray boosted dark matter in Xe-based direct detection experiments, Eur. Phys. J. C 84 (2024) 117 [arXiv:2210.01815] [INSPIRE].  
[39] V. De Romeri, A. Majumdar, D.K. Papoulias and R. Srivastava, XENONnT and LUX-ZEPLIN constraints on DSNB-boosted dark matter, JCAP 03 (2024) 028 [arXiv:2309.04117] [INSPIRE].  
[40] C. Xia, C.-Y. Xing and Y.-H. Xu, Boosted dark matter from Centaurus A and its detection, JHEP 03 (2024) 076 [arXiv:2401.03772] [INSPIRE].  
[41] A. Guha and J.-C. Park, Constraints on cosmic-ray boosted dark matter with realistic cross section, arXiv:2401.07750 [INSPIRE].  
[42] G. Guo, Y.-L.S. Tsai and M.-R. Wu, Probing cosmic-ray accelerated light dark matter with IceCube, JCAP 10 (2020) 049 [arXiv:2004.03161] [INSPIRE].  
[43] G. Guo, Y.-L.S. Tsai, M.-R. Wu and Q. Yuan, Elastic and Inelastic Scattering of Cosmic-Rays on Sub-GeV Dark Matter, Phys. Rev. D 102 (2020) 103004 [arXiv:2008.12137] [INSPIRE].

[44] G. Elor, R. McGehee and A. Pierce, Maximizing Direct Detection with Highly Interactive Particle Relic Dark Matter, Phys. Rev. Lett. 130 (2023) 031803 [arXiv:2112.03920] [INSPIRE].  
[45] KAMIOKANDE-II collaboration, Observation of a Neutrino Burst from the Supernova SN 1987a, Phys. Rev. Lett. 58 (1987) 1490 [INSPIRE].  
[46] R.M. Bionta et al., Observation of a Neutrino Burst in Coincidence with Supernova SN 1987a in the Large Magellanic Cloud, Phys. Rev. Lett. 58 (1987) 1494 [INSPIRE].  
[47] J.F. Beacom, The Diffuse Supernova Neutrino Background, Ann. Rev. Nucl. Part. Sci. 60 (2010) 439 [arXiv:1004.3311] [INSPIRE].  
[48] S. Ando, N. Ekanger, S. Horiuchi and Y. Koshio, Diffuse neutrino background from past core-collapse supernovae, arXiv:2306.16076 [INSPIRE].  
[49] SUPER-KAMIOKANDE collaboration, Supernova Relic Neutrino Search with Neutron Tagging at Super-Kamiokande-IV, Astropart. Phys. 60 (2015) 41 [arXiv:1311.3738] [INSPIRE].  
[50] HYPER-KAMIOKANDE collaboration, Hyper-Kamiokande Design Report, arXiv:1805.04163 [INSPIRE].  
[51] JUNO collaboration, Neutrino Physics with JUNO, J. Phys. G 43 (2016) 030401 [arXiv:1507.05613] [INSPIRE].  
[52] DUNE collaboration, Deep Underground Neutrino Experiment (DUNE), Far Detector Technical Design Report, Volume II: DUNE Physics, arXiv:2002.03005 [INSPIRE].  
[53] SUPER-KAMIOKANDE collaboration, Diffuse supernova neutrino background search at Super-Kamiokande, Phys. Rev. D 104 (2021) 122002 [arXiv:2109.11174] [INSPIRE].  
[54] SUPER-KAMIOKANDE collaboration, First result of a search for Diffuse Supernova Neutrino Background in SK-Gd experiment, PoS ICRC2023 (2023) 1173 [INSPIRE].  
[55] J.F. Beacom and M.R. Vagins, GADZOOKS! Anti-neutrino spectroscopy with large water Cherenkov detectors, Phys. Rev. Lett. 93 (2004) 171101 [hep-ph/0309300] [INSPIRE].  
[56] SUPER-KAMIOKANDE collaboration, Physics Potential of Super-  $K$  Gd, PoS ICHEP2018 (2019) 008 [INSPIRE].  
[57] THEIA collaboration, THEIA: an advanced optical neutrino detector, Eur. Phys. J. C 80 (2020) 416 [arXiv:1911.03501] [INSPIRE].  
[58] L. Pattavina, N. Ferreiro Iachellini and I. Tamborra, Neutrino observatory based on archaeological lead, Phys. Rev. D 102 (2020) 063001 [arXiv:2004.06936] [INSPIRE].  
[59] A.M. Suliga, J.F. Beacom and I. Tamborra, Towards probing the diffuse supernova neutrino background in all flavors, Phys. Rev. D 105 (2022) 043008 [arXiv:2112.09168] [INSPIRE].  
[60] S. Baum, F. Capozzi and S. Horiuchi, *Rocks, water, and noble liquids: Unfolding the flavor contents of supernova neutrinos*, Phys. Rev. D 106 (2022) 123008 [arXiv:2203.12696] [INSPIRE].  
[61] K. Møller, A.M. Suliga, I. Tamborra and P.B. Denton, Measuring the supernova unknowns at the next-generation neutrino telescopes through the diffuse neutrino background, JCAP 05 (2018) 066 [arXiv:1804.03157] [INSPIRE].  
[62] A. De Gouvêa, I. Martinez-Soler, Y.F. Perez-Gonzalez and M. Sen, Fundamental physics with the diffuse supernova background neutrinos, Phys. Rev. D 102 (2020) 123012 [arXiv:2007.13748] [INSPIRE].

[63] P. Iváñez-Ballesteros and M.C. Volpe, Neutrino nonradiative decay and the diffuse supernova neutrino background, Phys. Rev. D 107 (2023) 023017 [arXiv:2209.12465] [INSPIRE].  
[64] N.F. Bell, M.J. Dolan and S. Robles, Dark matter pollution in the Diffuse Supernova Neutrino Background, JCAP 11 (2022) 060 [arXiv:2205.14123] [INSPIRE].  
[65] A. de Gouvêa, I. Martinez-Soler, Y.F. Perez-Gonzalez and M. Sen, Diffuse supernova neutrino background as a probe of late-time neutrino mass generation, Phys. Rev. D 106 (2022) 103026 [arXiv:2205.01102] [INSPIRE].  
[66] Z. Tabrizi and S. Horiuchi, Flavor Triangle of the Diffuse Supernova Neutrino Background, JCAP 05 (2021) 011 [arXiv:2011.10933] [INSPIRE].  
[67] P. Martínez-Miravé, I. Tamborra and M. Tórtola, The Sun and core-collapse supernovae are leading probes of the neutrino lifetime, JCAP 05 (2024) 002 [arXiv:2402.00116] [INSPIRE].  
[68] P.-K. Hu, A. Kusenko and V. Takhistov, Dark Cosmic Rays, Phys. Lett. B 768 (2017) 18 [arXiv:1611.04599] [INSPIRE].  
[69] J.B. Dent, B. Dutta, J.L. Newstead and I.M. Shoemaker, Bounds on Cosmic Ray-Boosted Dark Matter in Simplified Models and its Corresponding Neutrino-Floor, Phys. Rev. D 101 (2020) 116007 [arXiv:1907.03782] [INSPIRE].  
[70] R. Plestid et al., New Constraints on Millicharged Particles from Cosmic-ray Production, Phys. Rev. D 102 (2020) 115032 [arXiv:2002.11732] [INSPIRE].  
[71] C.A. Arguelles Delgado, K.J. Kelly and V. Muñoz Albornoz, Millicharged particles from the heavens: single- and multiple-scattering signatures, JHEP 11 (2021) 099 [arXiv:2104.13924] [INSPIRE].  
[72] C.A. Arguelles, V. Munoz, I.M. Shoemaker and V. Takhistov, Hadrophilic light dark matter from the atmosphere, Phys. Lett. B 833 (2022) 137363 [arXiv:2203.12630] [INSPIRE].  
[73] C.V. Cappiello, Analytic Approach to Light Dark Matter Propagation, Phys. Rev. Lett. 130 (2023) 221001 [arXiv:2301.07728] [INSPIRE].  
[74] C.V. Cappiello and J.F. Beacom, *Strong New Limits on Light Dark Matter from Neutrino Experiments*, Phys. Rev. D 100 (2019) 103011 [Erratum ibid. 104 (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[75] S. Horiuchi, J.F. Beacom and E. Dwek, The Diffuse Supernova Neutrino Background is detectable in Super-Kamiokande, Phys. Rev. D 79 (2009) 083013 [arXiv:0812.3157] [INSPIRE].  
[76] PLANCK collaboration, Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [Erratum ibid. 652 (2021) C4] [arXiv:1807.06209] [INSPIRE].  
[77] D.A. Newmark and A. Schneider, Sensitivity to supernovae average  $\nu x$  temperature with neutral current interactions in DUNE, Phys. Rev. D 108 (2023) 043005 [arXiv:2304.00035] [INSPIRE].  
[78] M.T. Keil, G.G. Raffelt and H.-T. Janka, Monte Carlo study of supernova neutrino spectra formation, Astrophys. J. 590 (2003) 971 [astro-ph/0208035] [INSPIRE].  
[79] M.D. Kistler, H. Yuksel and A.M. Hopkins, The Cosmic Star Formation Rate from the Faintest Galaxies in the Unobservable Universe, arXiv:1305.1630 [INSPIRE].  
[80] N. Ekanger, S. Horiuchi, H. Nagakura and S. Reitz, Diffuse supernova neutrino background with up-to-date star formation rate measurements and long-term multidimensional supernova simulations, Phys. Rev. D 109 (2024) 023024 [arXiv:2310.15254] [INSPIRE].  
[81] B. Grzadkowski, M. Iglicki and S. Mrówczyński,  $t$ -channel singularities in cosmology and particle physics, Nucl. Phys. B 984 (2022) 115967 [arXiv:2108.01757] [INSPIRE].

[82] J.F. Navarro, C.S. Frenk and S.D.M. White, The structure of cold dark matter halos, Astrophys. J. 462 (1996) 563 [astro-ph/9508025] [INSPIRE].  
[83] K.C.Y. Ng et al., Resolving small-scale dark matter structures using multisource indirect detection, Phys. Rev. D 89 (2014) 083001 [arXiv:1310.1915] [INSPIRE].  
[84] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].  
[85] D.V. Nguyen et al., Observational constraints on dark matter scattering with electrons, Phys. Rev. D 104 (2021) 103521 [arXiv:2107.12380] [INSPIRE].  
[86] M.A. Buen-Abad, R. Essig, D. McKeen and Y.-M. Zhong, Cosmological constraints on dark matter interactions with ordinary matter, Phys. Rept. 961 (2022) 1 [arXiv:2107.12377] [INSPIRE].  
[87] K. Akita and S. Ando, Constraints on dark matter-neutrino scattering from the Milky-Way satellites and subhalo modeling for dark acoustic oscillations, JCAP 11 (2023) 037 [arXiv:2305.01913] [INSPIRE].  
[88] V. Shtabovenko, R. Mertig and F. Orellana, FeynCalc 10: Do multiloop integrals dream of computer codes?, arXiv:2312.14089 [INSPIRE].  
[89] C.R. Harris et al., Array programming with NumPy, Nature 585 (2020) 357 [arXiv:2006.10256] [INSPIRE].  
[90] P. Virtanen et al., SciPy 1.0-Fundamental Algorithms for Scientific Computing in Python, Nature Meth. 17 (2020) 261 [arXiv:1907.10121] [INSPIRE].  
[91] J.D. Hunter, Matplotlib: A 2D Graphics Environment, Comput. Sci. Eng. 9 (2007) 90 [INSPIRE].