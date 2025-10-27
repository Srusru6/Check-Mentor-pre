PAPER • OPEN ACCESS

# XENONnT and LUX-ZEPLIN constraints on DSNB-boosted dark matter

To cite this article: Valentina De Romeri et al JCAP03(2024)028

View the article online for updates and enhancements.

# You may also like

- A next-generation liquid xenon observatory for dark matter and neutrino physics  
J Aalbers, S S AbdusSalam, K Abe et al.  
- Constraints on light dark matter effective operators from the LUX-ZEPLIN experiment  
Wen-Na Yang, Mai Qiao and Yu-Feng Zhou  
- Energy-dependent boosted dark matter from diffuse supernova neutrino background  
Anirban Das, Tim Herbermann, Manibrata Sen et al.

# XENONnT and LUX-ZEPLIN constraints on DSNB-boosted dark matter

Valentina De Romeri  $^{a}$ , Anirban Majumdar  $^{b}$ , Dimitrios K. Papoulias  $^{c}$  and Rahul Srivastava  $^{d}$

$^{a}$ Instituto de Física Corpuscular (CSIC-Universitat de València),  
Parc Cientific UV C/ Catedratico Jose Beltrán 2, Paterna E-46980, Valencia, Spain  
$^{b}$ Department of Physics, Indian Institute of Science Education and Research Bhopal,

Bhopal Bypass Road, Bhauri, Bhopal 462066, India

$^{c}$ Department of Physics, National and Kapodistrian University of Athens,

Zografou Campus, Athens GR-15772, Greece

E-mail: deromeri@ific.uv.es, anirban19@iiserb.ac.in,

dkpapoulias@phys.uoa.gr, rahul@iserb.ac.in

ABSTRACT: We consider a scenario in which dark matter particles are accelerated to semi-relativistic velocities through their scattering with the Diffuse Supernova Neutrino Background. Such a subdominant, but more energetic dark matter component can be then detected via its scattering on the electrons and nucleons inside direct detection experiments. This opens up the possibility to probe the sub-GeV mass range, a region of parameter space that is usually not accessible at such facilities. We analyze current data from the XENONnT and LUX-ZEPLIN experiments and we obtain novel constraints on the scattering cross sections of sub-GeV boosted dark matter with both nucleons and electrons. We also highlight the importance of carefully taking into account Earth's attenuation effects as well as the finite nuclear size into the analysis. By comparing our results to other existing constraints, we show that these effects lead to improved and more robust constraints.

KEYWORDS: dark matter detectors, dark matter simulations, supernova neutrinos, supernovas

ARXIV EPRINT: 2309.04117

# Contents

1 Introduction 1  
2 Theoretical estimate of the DSNB flux 3  
3 The DSNB-boosted dark matter flux 4

3.1 Attenuation effects 6

4 Dark matter signal at underground detectors 9

4.1 LZ analysis 11  
4.2 XENONnT analysis 12

5 Results 12  
6 Conclusions 16

A Geometry of an underground detector's location 17  
B Geophysical properties of Earth 18  
C Energy loss experienced by the DSNB-boosted DM due to scattering inside Earth 18  
D Behavior of the exclusion regions in the low DM mass regime 20  
E Overview of the gauged  $\mathrm{U}(1)_{B_1 - 3L_e}$  extension 21

# 1 Introduction

It is estimated that  $85\%$  of the matter content of the Universe is in the form of a hypothetical kind of matter, dubbed dark matter (DM) [1]. One of the biggest mysteries in contemporary physics and astronomy is to understand its microscopic nature. However, since DM does not interact with photons and interacts very "weakly" with ordinary matter, it proves challenging to detect it. On the other hand, DM gravitational effects on visible matter allow us to infer its existence despite its elusiveness. One of the most compelling solutions to the DM puzzle assumes it to be in the form of some unknown particle [2], thus calling for an extension of the Standard Model (SM). Several strategies, including direct and indirect detection experiments and collider searches, have been developed to try to detect it [3, 4]. Although a conclusive finding of DM has not been achieved yet, these searches have imposed very tight constraints on its potential properties. As part of the continuous effort to understand this enigmatic component, new experiments, and observations are being carried out.

The possibility that DM has been produced thermally in the early Universe and that its abundance is determined by thermal freeze-out has motivated numerous large direct detection

(DD) experiments, which aim at observing the scattering of a DM particle off a target in a deep underground detector. These experiments have experienced an increasingly, decades-long progress which has brought them into the multi-ton era [5]. Current most-sensitive constraints in the high-mass regime include those set by liquid xenon (LXe) experiments like LUX-ZEPLIN (LZ) [6, 7], XENONnT [8, 9], XENON1T [10], PandaX-II [11] and LUX [12], together with measurements on liquid argon (LAr) detectors like DEAP-360 [13] and DarkSide-50 [14] and the solid-state cryogenic detector of SuperCDMS [15].

We are interested in the results recently released by two DD experiments, XENONnT [8] and LZ [7]. Both experiments use state-of-the-art LXe detectors that aim at observing low-energy electron and nuclear recoils induced by DM scattering. Being one of the most sensitive DM DD experiments at present, XENONnT [16, 17], installed at the Gran Sasso National Laboratories in Italy, is the upgrade phase of XENON1T [10]. Thanks to its larger active target mass, superior photon detection mechanism, and extremely low background, XENONnT is an order of magnitude more sensitive to weakly-interacting DM particles than its predecessor. The recently released XENONnT data correspond to a total exposure of 1.16 tonne×years [8]. The LZ experiment [18], located at the Sanford Underground Research Facility in South Dakota, is a detector centered on a dual-phase time projection chamber, also filled with LXe. The recently available LZ data correspond to an exposure of 5.5 tonne×60 days [7]. The LZ collaboration has reported results from a blind search for DM particles and established the current strongest constraint for masses above 9 GeV, testing a cross section as small as  $6 \times 10^{-48} \mathrm{~cm}^2$  at a DM mass of 30 GeV.

Both XENONnT and LZ, as most of other DD experiments, have best sensitivities to electroweak-scale DM with masses around 10–100 GeV. Below the GeV scale, their sensitivity drops dramatically, as the electron and nuclear recoil energy becomes smaller and eventually falls below the detector threshold. Normally, recoil events in the LZ experiment cannot be observed for non-relativistic sub-GeV DM traveling at velocities  $v \sim 10^{-3}$ . However, an energetic sub-GeV DM particle may generate a substantial signal. One possibility that has been put forward to explore sub-GeV DM is that of boosted DM (BDM). Such a BDM would contribute as a subdominant component of the total DM flux, but would nonetheless enhance the mass reach of DD experiments, allowing to explore the sub-GeV range. This idea has first been proposed considering DM boosting from the scattering with energetic galactic cosmic rays [19, 20] and has been extensively discussed in the literature, see for instance [21–36]. More recently, the possibility that DM is boosted through its scattering with neutrinos has also been envisaged, either considering cosmic neutrinos [37], solar neutrinos [38], neutrinos from primordial black holes evaporation [39–42], supernova neutrinos [43, 44] or the diffuse supernova neutrino background (DSNB) [45, 46]. Other possibilities leading to BDM include blazar-boosted DM [47], boosted DM from phantom dark energy [48], confined cosmic rays in starburst galaxies [49], models with semi-annihilating DM [50–52] or models with a multi-component DM sector [53–56].

In this work, we investigate the possibility that the DM in the Milky Way halo is boosted to semi-relativistic velocities, via its scattering on the DSNB [57, 58]. The DSNB is a cumulative and isotropic flux of MeV neutrinos of all flavors produced from core-collapse supernovae explosions along the whole history of the Universe. While not yet observed, the DSNB is an irreducible background, expected to be within the reach of near-future

experiments. Even though less energetic than cosmic rays, it seems reasonable to assume possible interactions of local DM with this isotropic neutrino background. By employing XENONnT and LZ latest data releases [7, 8], we derive stringent constraints on both DM-electron and DM-nucleon scattering cross sections in the sub-GeV range, thus providing complementary results to the standard analyses offered by the two collaborations [7, 9]. We highlight and pay special attention to the Earth's attenuation effects, that, as we will show, play an important role in the region of interest of the parameter space. Additionally, we also take into account nuclear effects which further improve the sensitivity and robustness of our analysis. DSNB-boosted DM had previously been considered in ref. [45] as a possible explanation to an excess of electron recoil events in the low energy region, now disappeared, observed by XENON1T [59]. Ref. [46] also set limits on DSNB-boosted DM scattering off electrons using XENON1T and Super-Kamiokande data. Here we improve upon these previous results by presenting for the first time constraints on DSNB-boosted DM, from the most recent XENONnT and LZ data, for both nuclear and electron scattering.

The remainder of this paper is organized as follows. Section 2 provides a discussion on theoretical predictions for the DSNB flux. Section 3 explains how sub-GeV non-relativistic DM particles in the Milky Way halo can attain semi-relativistic speeds due to interactions with DSNB neutrinos, and highlights the importance of Earth's attenuation effects as well as the nuclear form factors. In section 4, we delve into the simulation of the DSNB-boosted DM-induced signal predicted for the XENONnT and LZ detectors. Our results are presented in section 5, while we finally provide our concluding remarks in section 6.

# 2 Theoretical estimate of the DSNB flux

Right after the first star formation event, the Universe has been surrounded by an isotropic flux of MeV-energy neutrinos and antineutrinos of all flavors, produced from all supernovae events from the core-collapse explosions of huge stars throughout the Universe. The theoretical prediction for the differential DSNB flux, per neutrino flavor  $\alpha$ , can be estimated as [57, 60-62]

$$
\frac {d \Phi_ {\nu_ {\alpha}} ^ {\mathrm {D S N B}}}{d E _ {\nu}} = \int_ {0} ^ {\mathrm {z} _ {\max }} d \mathrm {z} \frac {R _ {\mathrm {C C S N}} (\mathrm {z})}{H (\mathrm {z})} \left. \mathcal {F} _ {\nu_ {\alpha}} \left(E _ {\nu_ {\alpha}}\right) \right| _ {E _ {\nu} = E _ {\nu} ^ {s} (1 + \mathrm {z})}, \tag {2.1}
$$

$E_{\nu}^{s}$  being the neutrino energy at the source. The integral is performed over the redshift parameter,  $\mathbf{z}$ , and we take the maximum redshift at which star-formation occurs as  $\mathrm{z}_{\mathrm{max}} \sim 6$ . Moreover,  $H(z)$  is the Hubble function determined from the Friedmann equation as

$$
H (\mathrm {z}) = H _ {0} \sqrt {\Omega_ {M} (1 + \mathrm {z}) ^ {3} + \Omega_ {\Lambda} (1 + \mathrm {z}) ^ {3 (1 + w)} + (1 - \Omega_ {M} - \Omega_ {\Lambda}) (1 + \mathrm {z}) ^ {2}}, \qquad (2. 2)
$$

where  $H_0 = 67.45 \, \mathrm{km} \, \mathrm{s}^{-1} \, \mathrm{Mpc}^{-1}$  is the Hubble constant [1, 63],  $\Omega_M = 0.315 \pm 0.007$  and  $\Omega_{\Lambda} = 0.685 \pm 0.007$  denote the matter and vacuum contributions to the present-Universal energy density, while the best current measurement for the equation-of-state parameter for the dark energy is  $w = -1.028 \pm 0.031$  [1]. The DSNB flux further depends upon the rate of Core-Collapse Supernovae (CCSN), which reads [61]

$$
R _ {\mathrm {C C S N}} (\mathrm {z}) = \dot {\rho} _ {*} (\mathrm {z}) \frac {\int_ {8} ^ {5 0} \psi (M) d M}{\int_ {0 . 1} ^ {1 0 0} M \psi (M) d M}, \tag {2.3}
$$

where  $\psi (M)$  is the initial mass function (IMF) of stars, indicating the star density within a certain mass range. For our analysis we have assumed the IMF to be a power-law distribution,  $\psi (M)\propto M^{-2.35}$  according to [64]. The redshift evolution of the co-moving cosmic starformation rate,  $\dot{\rho}_{*}(\mathrm{z})$ , can be modelled as [60, 65]

$$
\dot {\rho} _ {*} (\mathrm {z}) = \dot {\rho} _ {0} \left[ (1 + \mathrm {z}) ^ {- 1 0 a} + \left(\frac {1 + \mathrm {z}}{B}\right) ^ {- 1 0 b} + \left(\frac {1 + \mathrm {z}}{C}\right) ^ {- 1 0 c} \right] ^ {- 0. 1}, \tag {2.4}
$$

where the overall normalization factor is  $\dot{\rho}_0 = 0.0178_{-0.0036}^{+0.0035}M_\odot\mathrm{yr}^{-1}\mathrm{Mpc}^{-3}$  [61]. The constants  $B$ , and  $C$  are expressed as [60, 65]:

$$
B = \left(1 + \mathrm {z _ {1}}\right) ^ {1 - \frac {a}{b}}, (2. 5 \mathrm {a})
$$

$$
C = \left(1 + z _ {1}\right) ^ {\frac {b - a}{c}} \left(1 + z _ {2}\right) ^ {1 - \frac {b}{c}}, \tag {2.5b}
$$

where  $\mathbf{z}_1 = 1$ , and  $\mathbf{z}_2 = 4$  represent the redshift breaks, while  $a$ ,  $b$  and  $c$  denote the logarithmic slopes for the low, intermediate, and high redshift ranges. An analytical fit to data from different astronomical surveys [60, 65] gives

$$
\{a, b, c \} = \left\{3. 4 \pm 0. 2, - 0. 3 \pm 0. 2, - 3. 5 \pm 1 \right\}.
$$

Finally, a non-degenerate Fermi-Dirac distribution is used to parametrize the flavor-dependent neutrino spectra released by a CCSN event [57, 61]

$$
\mathcal {F} _ {\nu_ {\alpha}} (E _ {\nu_ {\alpha}}) = \frac {E _ {\nu} ^ {\mathrm {t o t}}}{6} \frac {1 2 0}{7 \pi^ {4}} \frac {E _ {\nu_ {\alpha}} ^ {2}}{T _ {\nu_ {\alpha}} ^ {4}} \frac {1}{1 + e ^ {E _ {\nu_ {\alpha}} / T _ {\nu_ {\alpha}}}}, \tag {2.6}
$$

where  $E_{\nu}^{\mathrm{tot}} = 3 \times 10^{53} \, \mathrm{erg}$ , represents the total amount of energy released as neutrinos [57], and  $T_{\nu_{\alpha}}$  denotes the temperature of each flavor of neutrinos. In our present study, we consider  $T_{\nu_{e}} = 6.6 \, \mathrm{MeV}$ ,  $T_{\bar{\nu}_{e}} = 7 \, \mathrm{MeV}$ ,  $T_{\nu_{x}} = 10 \, \mathrm{MeV}$  ( $\nu_{x}$  denotes either  $\nu_{\mu}$  or  $\nu_{\tau}$  or their antiparticles), satisfying the upper limit extracted from Super-Kamiokande [66].

We show in figure 1 the predicted DSNB fluxes, for the different neutrino flavors, as a function of the neutrino energy. In the following calculations we will assume an uncertainty of  $40\%$  in the normalization of the DSNB spectra, estimated from uncertainties in the cosmic star-formation rate [60]. This uncertainty on the DSNB fluxes is illustrated by the shaded bands in figure 1.

# 3 The DSNB-boosted dark matter flux

In this section, we discuss how the DM particles in the Milky Way halo get boosted to considerably greater velocities due to their scattering with DSNB neutrinos. We remain agnostic of the specific DM model<sup>2</sup> and for the sake of uniformity in comparing the final results

![](images/816547bb608438a059439bbcab64a3ade92a242c388d0bb6084bdded81062386.jpg)  
Figure 1. Predicted DSNB fluxes for various neutrino flavors ( $\nu_{x}$  denotes either  $\nu_{\mu}$  or  $\nu_{\tau}$  or their antiparticles), as a function of the neutrino energy, estimated from eq. (2.1). The bands illustrate a  $40\%$  error in the normalization uncertainty of the DSNB spectra [60].

we assume the DM to be made of one particle species  $\chi$  that scatters with neutrinos and electrons ( $\sigma_{\nu \chi} = \sigma_{\chi e}$ ) or with neutrinos and nucleons ( $\sigma_{\nu \chi} = \sigma_{\chi n}$ ) with the same cross section, as the benchmark for our analysis. These assumptions can be naturally realized in flavor-dependent gauged U(1) extensions such as  $\mathrm{U}(1)_{B_i - 3L_i}$ ,  $i$  being generation index or  $\mathrm{U}(1)_{B - 3L_i}$  models [68-70] (for an overview of such a model, see appendix E). Furthermore, scenarios deviating from this assumption can be easily accounted for by using the product  $\sqrt{\sigma_{\nu \chi} \sigma_{\chi e}}$  or  $\sqrt{\sigma_{\nu \chi} \sigma_{\chi n}}$  as applicable, see section 5 for further discussion. Before entering into details, it is noteworthy to stress that the initial DM galactic escape velocity is irrelevant [19], as the scattering between  $\chi$  and DSNB neutrinos accelerates the DM to significantly higher velocities.

The DSNB-boosted DM differential flux, induced by its scattering with the DSNB given in eq. (2.1), can be estimated as [45]

$$
\frac {d \Phi_ {\chi}}{d T _ {\chi}} = D _ {\mathrm {h a l o}} \int_ {E _ {\nu} ^ {\mathrm {m i n}}} ^ {E _ {\nu} ^ {\mathrm {m a x}}} d E _ {\nu} \frac {1}{m _ {\chi}} \frac {d \sigma_ {\nu \chi}}{d T _ {\chi}} \frac {d \Phi_ {\nu} ^ {\mathrm {D S N B}}}{d E _ {\nu}}, \tag {3.1}
$$

where  $T_{\chi}$  is the energy transferred to  $\chi$  and  $\frac{d\Phi_{\nu}^{\mathrm{DSNB}}}{dE_{\nu}}$  is the sum over all neutrino flavors of the DSNB flux given in eq. (2.1). The neutrino-DM scattering cross section can be cast in the form

$$
\frac {d \sigma_ {\nu \chi}}{d T _ {\chi}} = \frac {\sigma_ {\nu \chi}}{T _ {\chi} ^ {\max } \left(E _ {\nu}\right)} \Theta \left[ T _ {\chi} ^ {\max } \left(E _ {\nu}\right) - T _ {\chi} \right], \tag {3.2}
$$

where  $m_{\chi}$  denotes the DM mass, while  $\sigma_{\nu \chi}$  controls the strength of the interaction. The maximum transferred energy to which the DM can be boosted for a given neutrino energy  $E_{\nu}$ , is dictated by the kinematics of the process and is incorporated in the Heaviside step function:  $T_{\chi}^{\max}(E_{\nu}) = E_{\nu}^{2} / \left(E_{\nu} + \frac{m_{\chi}}{2}\right)$ . The maximum neutrino energy in our numerical calculations is taken to be  $E_{\nu}^{\max} = 100\mathrm{MeV}$ , while the lower integration limit in eq. (3.1) can

be obtained by inverting the expression for  $T_{\chi}^{\mathrm{max}}$  which gives the minimum neutrino energy required to boost the DM, i.e.  $E_{\nu}^{\mathrm{min}} = \left[T_{\chi} + \sqrt{T_{\chi}^{2} + 2m_{\chi}T_{\chi}}\right] / 2$ .

The  $D$ -factor  $(D_{\mathrm{halo}})$  in eq. (3.1) encodes the DM density distribution within our galactic halo, and it is expressed as the integral of the density profile along the line of sight (l.o.s.)  $\ell$  and over the solid angle  $\Omega$ :

$$
D _ {\mathrm {h a l o}} = \int_ {\Delta \Omega} \frac {d \Omega}{4 \pi} \int_ {0} ^ {\ell_ {\max }} \rho_ {\mathrm {M W}} [ r (\ell , \psi) ] d \ell . \tag {3.3}
$$

Here, we assume a Navarro-Frenk-White (NFW) profile, $^{4}$  defined as [72]

$$
\rho_ {\mathrm {M W}} (r) = \rho_ {\odot} \left[ \frac {r}{r _ {\odot}} \right] ^ {- 1} \left[ \frac {1 + \frac {r _ {\odot}}{r _ {s}}}{1 + \frac {r}{r _ {s}}} \right] ^ {2}, \tag {3.4}
$$

where the scale radius is  $r_s = 20\mathrm{kpc}$  and the local DM density is  $\rho_{\odot} = 0.4\mathrm{GeVcm}^{-3}$ . The galactocentric distance reads

$$
r (l, \psi) = \sqrt {r _ {\odot} ^ {2} - 2 l r _ {\odot} \cos \psi + l ^ {2}}, \tag {3.5}
$$

with  $r_{\odot} = 8.5\mathrm{kpc}$  being the distance between the Earth and the galactic centre and  $\psi$  the angle of view defining the l.o.s.. The upper limit of the l.o.s. integral is given by  $\ell_{\max} = \sqrt{R^2 - r_{\odot}^2\sin^2\psi + r_{\odot}\cos\psi}$ , with the galactic halo virial radius taken to be  $R = 200\mathrm{kpc}$ . Given these values, we hence obtain  $D_{\mathrm{halo}} = 2.22\times 10^{25}\mathrm{MeVcm^{-2}}$  over the whole galactic halo.

# 3.1 Attenuation effects

In this subsection, we will focus our attention on the modifications expected to occur in the energy profile of the DSNB-boosted DM flux during its propagation through the atmosphere and the Earth [19, 26, 73-76]. For sufficiently large interaction cross sections,  $d\sigma_{\chi i} / dT_i$ , the DM particles may lose a significant amount of energy due to their scattering on nuclei ( $i = \mathcal{N}$ ) or electrons ( $i = e$ ), resulting into a sizeable attenuation of the DM flux before reaching the detector. This effect can be accounted for via the energy loss equation [19, 26]

$$
\frac {d T _ {\chi} ^ {z}}{d z} = - n _ {i} \int_ {0} ^ {T _ {i} ^ {\max} (T _ {\chi} ^ {z})} \frac {d \sigma_ {\chi i}}{d T _ {i}} T _ {i} d T _ {i}, \tag {3.6}
$$

where  $T_{i}$  denotes the energy lost by the boosted DM particle in a collision and  $n_i$  is the number density of nucleus species or electrons. Here,  $z$  denotes the distance travelled from the location of the scattering point (inside the atmosphere or the Earth) to the detector. In the most general case, eq. (3.6) relates the initial energy at the top of the atmosphere  $(z = 0)$ ,  $T_{\chi}^{0}$ , with the average kinetic energy,  $T_{\chi}^{z}$ , after travelling a distance  $z$  before reaching the underground detector. In our analysis, we neglect the impact of atmospheric attenuation as it is expected to be negligible compared to Earth's attenuation [26], for the cross sections under consideration. Hence, we take  $z = 0$  at the Earth's surface. Then, the distance  $z$  can be expressed as (see appendix A for more details)

$$
z = - \left(R _ {E} - h _ {d}\right) \cos \theta_ {z} + \sqrt {R _ {E} ^ {2} - \left(R _ {E} - h _ {d}\right) ^ {2} \sin^ {2} \theta_ {z}}, \tag {3.7}
$$

where  $R_{E}$  stands for the radius of the Earth,  $\theta_{z}$  refers to the detector's zenith angle and  $h_{d}$  indicates the depth of the detector's location from the Earth's surface, at the point where the zenith angle is zero. Moreover, for the sake of simplicity, we have adopted a mean average electron density  $n_{e}$  of Earth's most abundant elements between the surface and depth  $z$ ,  $n_{e} = 8 \times 10^{23} \mathrm{~cm}^{-3}$  [20]. In the case of attenuation due to  $\chi$  scattering on nuclei, we have determined the nuclear number density at depth  $z$  through a weighted average of the most abundant elements found in the Earth's crust, mantle, and core, yielding  $n_{\mathcal{N}} = 3.44 \times 10^{22} \mathrm{~cm}^{-3}$  and  $A \approx 33.3$  (for details see appendix B and refs. [73, 77-79]).

The differential cross section for DM-electron or DM-nucleus scattering takes the form

$$
\frac {d \sigma_ {\chi i}}{d T _ {i}} = \frac {\sigma_ {\chi i}}{T _ {i} ^ {\max} (T _ {\chi})}, \quad i = \mathcal {N} \mathrm {o r} e, \tag {3.8}
$$

where the maximum recoil energy that can be lost by  $\chi$  during the attenuation process, is obtained from the kinematics of the process and reads

$$
T _ {i} ^ {\max } (T _ {\chi}) = \frac {2 m _ {i} T _ {\chi} (T _ {\chi} + 2 m _ {\chi})}{(m _ {\chi} + m _ {i}) ^ {2} + 2 m _ {i} T _ {\chi}}, \tag {3.9}
$$

with  $m_{i}$  indicating the nuclear  $(i = \mathcal{N})$  or electron  $(i = e)$  mass. The solution of eq. (3.6) gives the DM energy as a function of the distance and the initial DM energy, i.e.  $T_{\chi}^{z}\equiv T_{\chi}^{z}(T_{\chi}^{0},z)$  with  $z$  depending on the zenith angle and the detector depth as indicated in eq. (3.7). The resulting attenuated DM flux reaching the detector after averaging over angles,  $^5 d\Phi_\chi^z /dT_\chi^z$  is given by the expression

$$
\frac {d \Phi_ {\chi}}{d T _ {\chi} ^ {z}} = \int d \Omega \left. \frac {d ^ {2} \Phi_ {\chi}}{d T _ {\chi} d \Omega} \right| _ {T _ {\chi} ^ {0}} \frac {d T _ {\chi} ^ {0}}{d T _ {\chi} ^ {z}}, \tag {3.10}
$$

where  $\Omega$  is the solid angle.

# 3.1.1 Scattering with electrons

For the case of DM-electron scattering we have  $\sigma_{\chi i} = \sigma_{\chi e}$  in eq. (3.8). In this case eq. (3.6) can be solved analytically. The solution for  $T_{\chi}^{z}$  at a given depth  $z$  can be expressed in terms of the DM energy at the surface,  $T_{\chi}^{0}$ , as

$$
T _ {\chi} ^ {z} \approx \frac {T _ {\chi} ^ {0} e ^ {- z / l _ {E}}}{1 + \frac {T _ {\chi} ^ {0}}{2 m _ {\chi}} \left(1 - e ^ {- z / l _ {E}}\right)}, \tag {3.11}
$$

where  $l_{E}$  represents the mean free path for energy loss, given by  $l_{E}^{-1} = n_{e}\sigma_{\chi e}\frac{2m_{e}m_{\chi}}{(m_{e} + m_{\chi})^{2}}$ . By inverting eq. (3.11) we obtain the expression for  $T_{\chi}^{0}$  as a function of  $T_{\chi}^{z}$  and  $z$ , which reads

$$
T _ {\chi} ^ {0} \approx \frac {2 m _ {\chi} T _ {\chi} ^ {z} e ^ {z / l _ {E}}}{2 m _ {\chi} + T _ {\chi} ^ {z} \left(1 - e ^ {z / l _ {E}}\right)}. \tag {3.12}
$$

As a consequence, the attenuated DM flux given in eq. (3.10) that eventually reaches the detector can be simplified as follows

$$
\frac {d \Phi_ {\chi}}{d T _ {\chi} ^ {z}} \approx \int d \Omega \left. \frac {d ^ {2} \Phi_ {\chi}}{d T _ {\chi} d \Omega} \right| _ {T _ {\chi} ^ {0}} \frac {4 m _ {\chi} ^ {2} e ^ {z / l _ {E}}}{\left[ 2 m _ {\chi} + T _ {\chi} ^ {z} \left(1 - e ^ {z / l _ {E}}\right) \right] ^ {2}}. \tag {3.13}
$$

Before closing this discussion let us stress that, as discussed before, our analysis is done for the benchmark  $\sigma_{\nu \chi} = \sigma_{\chi e}$ . Note that the bounds that we will eventually obtain in section 5 will mainly depend on the product  $\sqrt{\sigma_{\nu \chi} \sigma_{\chi e}}$ , which simplifies to  $\sigma_{\chi e}$  under the assumption  $\sigma_{\nu \chi} = \sigma_{\chi e}$ , plus corrections due to the dependence of  $l_{E}$  (see eq. (3.11)) on  $\sigma_{\chi e}$ . We will discuss this in more detail in section 5.

# 3.1.2 Scattering with nuclei: effect of the finite nuclear size

For the case of DM-nucleus scattering we take  $\sigma_{\chi i} = \sigma_{\chi \mathcal{N}}^{\mathrm{SI}}$  in eq. (3.8), where the spin-independent (SI) DM-nucleus elastic scattering cross section is expressed as [80, 81]

$$
\sigma_ {\chi \mathcal {N}} ^ {\mathrm {S I}} (\mathfrak {q} ^ {2}) = \frac {\mu_ {\mathcal {N}} ^ {2}}{\mu_ {n} ^ {2}} A ^ {2} \sigma_ {\chi n} F ^ {2} (\mathfrak {q} ^ {2}), \tag {3.14}
$$

where  $A$  denotes the atomic mass number of the target nuclei,  $\mathfrak{q} = \sqrt{2m_{\mathcal{N}}T_{\mathcal{N}}}$  stands for the three-momentum transfer,  $\sigma_{\chi n}$  is the DM-nucleon SI cross section and  $\mu_{\mathcal{N}}(\mu_n)$  represents the DM-nucleus (DM-nucleon) reduced mass. We again take the benchmark  $\sigma_{\nu \chi} = \sigma_{\chi n}$  for our analysis, but, as mentioned above, our bounds are mainly dependent on  $\sqrt{\sigma_{\nu\chi}\sigma_{\chi n}}$  (see section 5). The SI cross section  $\sigma_{\chi \mathcal{N}}^{\mathrm{SI}}$  is a momentum-dependent quantity due to the presence of the nuclear form factor,  $F(\mathfrak{q}^2)$ , which accounts for the finite nuclear size and has been parametrized by a Helm-type effective form factor [82]. Notice that the energy dependence of the SI cross section prevents us from obtaining an analytical solution for eq. (3.6), unlike the case of DM-electron scattering discussed above, hence we need to solve eq. (3.6) numerically.

The fact that the DM travels through Earth to reach the detectors, leads to attenuation of the flux. In figure 2 we present the angle-averaged DSNB-boosted DM flux for unattenuated and attenuated cases. The results are plotted for the benchmark parameters  $m_{\chi} = 300 \mathrm{MeV}$  and  $\sigma_{\nu \chi} = 10^{-29} \mathrm{~cm}^2$ , assuming a depth of  $h_d = 1.4 \mathrm{~km}$  which corresponds to the underground location of XENONnT. Note that the results remain essentially unchanged for the case of LZ ( $h_d = 1.47 \mathrm{~km}$ ). The solid blue line in figure 2 corresponds to the unattenuated flux. The dashed lines show the attenuated fluxes corresponding to attenuation due to DM-nucleus (orange, dashed) and DM-electron (green, dashed) scattering as a function of the DM energy. For the case of  $\chi - \mathcal{N}$  scattering, the effect of the finite nuclear size is illustrated by comparing the resulting fluxes for two cases: (i) by incorporating the Helm form factor in the calculation (orange, dashed) and (ii) by assuming  $F = 1$  i.e. completely ignoring nuclear physics (orange, dotted).

![](images/a3acac82551ceca28ccdc9b22dd5d76f28fee9862135bb0a440687f0c64dc4d0.jpg)  
Figure 2. The angle-averaged DNSB-boosted DM flux distribution as a function of the DM energy for  $m_{\chi} = 300 \, \mathrm{MeV}$ ,  $\sigma_{\nu \chi} = 10^{-29} \, \mathrm{cm}^2$  and a detector depth of  $h_d = 1.4 \, \mathrm{km}$  for the benchmarks  $\sigma_{\nu \chi} = \sigma_{\chi e}$  and  $\sigma_{\nu \chi} = \sigma_{\chi n}$ . The unattenuated flux is shown by the solid blue line. The attenuated DM flux for the case of DM scattering with electrons (nuclei including Helm-type form factor) inside the Earth is displayed with a green (orange) dashed line. The effect of the nuclear form factor is illustrated by comparing the results assuming a Helm-type form factor (dashed line) and  $F = 1$  (dash-dotted line). See main text for more details.

As can be seen, Earth's attenuation effects shift the peak of the DSNB-boosted DM flux towards lower energies and reduce it up to a factor 2 (3.5) for  $\chi -e$  ( $\chi -\mathcal{N}$ ) scattering. Furthermore, the high-energy endpoint of the differential DSNB-boosted DM flux spectra exhibits a faster decline when finite nuclear size is neglected, as opposed to the case where the finite nuclear size effects are taken into account. The Earth's attenuation and nuclear size effects play a crucial role in the results presented in the remainder of the work (see also appendix C).

Before closing this discussion let us stress that in the present analysis, the calculated attenuated flux is not taking into account additional effects related to the direction of DNSB-boosted DM particles after each scattering process nor the possibility of multiple scatterings. These effects only become relevant when the DM mass and energy are significantly lower than the mass of the nucleus [26, 73] and are important for probing diurnal effects [83].

# 4 Dark matter signal at underground detectors

After reaching the underground detector, the DSNB-boosted DM can scatter off both the electrons and nuclei of the target material, thus inducing both electronic and nuclear recoils. The differential event rate with respect to the recoil energy  $T_{i}$  can be written as [45]

$$
\frac {d R}{d T _ {i}} = t _ {\text {r u n}} N _ {\text {t a r g e t}} ^ {i} \mathcal {A} \int d T _ {\chi} ^ {z} \frac {d \Phi_ {\chi}}{d T _ {\chi} ^ {z}} \frac {\sigma_ {\chi i}}{T _ {i} ^ {\max } \left(T _ {\chi} ^ {z}\right)} \Theta \left[ T _ {i} ^ {\max } \left(T _ {\chi} ^ {z}\right) - T _ {i} \right], \tag {4.1}
$$

where  $t_{\mathrm{run}}$  and  $N_{\mathrm{target}}$  denote the exposure time and number of targets of the detector, respectively, while  $\mathcal{A}$  represents the detection efficiency provided by each experiment. At this

point we should clarify that the detection efficiency is provided either in terms of true  $\mathcal{A}(T_i)$  or reconstructed  $\mathcal{A}(T_i^{\mathrm{reco}})$  recoil energy, hence its explicit dependence has been dropped in eq. (4.1) to avoid confusion. Regarding DM-electron scattering, our calculations incorporate the detection efficiency provided by LZ [6] in terms of true recoil energy  $\mathcal{A}(T_e)$ , while for the case of XENONnT we consider the efficiency provided in ref. [8] in terms of reconstructed recoil energy  $\mathcal{A}(T_e^{\mathrm{reco}})$ . Regarding DM-nucleus scattering, we account for the detection efficiency  $\mathcal{A}(T_{\mathcal{N}})$  provided in terms of true nuclear recoil energy as reported by both LZ [7] and XENONnT [9]. In what follows, we will use the recent data released by XENONnT and LZ collaborations to put constraints on the DM mass and DM-electron/nucleon cross sections.

We first focus on DM-electron scattering, i.e. we calculate the differential event spectrum  $dR / dT_{e}$  given in eq. (4.1) for  $i = e$ . In this case,  $\chi$  particles scatter off electrons in the underground detector with a cross section  $\sigma_{\chi e}$ . The angle-averaged DSNB-boosted DM flux, accounting for the attenuation effects (see section 3.1.1) is given in eq. (3.13). Since very low energy scatterings occur, our calculations take into consideration atomic binding effects which lead to a slight cross section suppression at very low recoil energies. To this purpose, the number of target electrons in eq. (4.1) is expressed as  $N_{\mathrm{target}}^{e} = \frac{m_{\mathrm{det}}N_{A}}{M_{r}}\times Z_{\mathrm{eff}}(T_{e})$  where  $m_{\mathrm{det}}$ ,  $M_{r}$  and  $N_{A}$  represent the detector mass, the molar mass of the target material and the Avogadro's number, respectively. The recoil energy-dependent quantity  $Z_{\mathrm{eff}}(T_e)$  denotes the effective charge of the atomic nucleus that is seen by DM for a given energy deposition  $T_{e}$ . The latter can be approximated by a series of step functions that depend on the single particle binding energy of the ith electron, following the Hartree-Fock calculations of ref. [84].

Turning our attention to the case of DM scattering with nuclei, we calculate the corresponding differential event spectrum  $dR / dT_{\mathcal{N}}$  that follows from eq. (4.1) for  $i = \mathcal{N}$ . For the sake of clarity let us note that in this case, although our calculated event rates refer to DM-nucleus scattering, our results will be always expressed in terms of the fundamental DM-nucleon cross section  $\sigma_{\chi n}$ , instead of the SI DM-nucleus cross section  $\sigma_{\chi \mathcal{N}}^{\mathrm{SI}}$  [see e.g. eq. (3.14)]. In this case the angle-averaged attenuated boosted DM flux has been computed numerically as discussed in section 3.1.2. Since both the LZ and XENONnT collaborations have reported their measured data in terms of electron-recoil spectra, we convert our calculated nuclear recoil spectrum  $dR / dT_{\mathcal{N}}$  into an "electron-equivalent" recoil spectrum, according to the expression

$$
\frac {d R}{d T _ {e}} = \frac {d R}{d T _ {\mathcal {N}}} \frac {1}{\mathcal {Q} _ {f} \left(T _ {\mathcal {N}}\right) + T _ {\mathcal {N}} \frac {d \mathcal {Q} _ {f}}{d T _ {\mathcal {N}}}}, \tag {4.2}
$$

where the quenching factor,  $\mathcal{Q}_f(T_{\mathcal{N}}) = T_e / T_{\mathcal{N}}$ , quantifies the energy loss to heat in the aftermath of a DM-nucleus scattering event. In the present analysis we adopt the standard Lindhard quenching factor [85]. Notice also that for DM-nucleus scattering the effective charge  $Z_{\mathrm{eff}}$  is irrelevant and hence we take  $Z_{\mathrm{eff}} = 1$ .

In the final step we intend to simulate the expected boosted DM signal at the LZ and XENONnT detectors with high reliability. To this purpose we evaluate the reconstructed spectra by assuming a Gaussian smearing function  $\mathcal{G}(T_e^{\mathrm{reco}}, T_e)$  as

$$
\frac {d R}{d T _ {e} ^ {\text {r e c o}}} = \int_ {0} ^ {T _ {e} ^ {\max }} \frac {d R}{d T _ {e}} \left(T _ {e}\right) \mathcal {G} \left(T _ {e} ^ {\text {r e c o}}, T _ {e}\right) d T _ {e}. \tag {4.3}
$$

By following the above method we have verified that our predictions are in excellent agreement with those reported by XENONnT and LZ for both electron and nuclear recoils. First, based on previous work [86], we have calculated the elastic neutrino-electron scattering spectra and found that a total of  $\sim 30$  events are expected for LZ and 76 events (300 events in the full region [1, 140] keV<sub>ee</sub>) for XENONnT, in agreement with refs. [7, 8]. Second, regarding nuclear recoils we have calculated the corresponding coherent elastic neutrino-nucleus scattering (CE<sub>ν</sub>NS) expected events induced by <sup>8</sup>B neutrinos and found 0.16 events for LZ and 0.24 events for XENONnT, in agreement with refs. [7, 9], respectively.

Following these prescriptions, we show in figure 3 the simulated recoil spectra as a function of the electron-equivalent ionization energy, expected at both the LZ and XENONnT detectors. The black points depict the experimental data together with the error bars, when available, $^{8}$  as provided by the collaborations. The blue histograms indicate the background events, also given by the collaborations. The red and green histograms represent the sum of the background and of the simulated number of events, assuming  $m_{\chi} = 300 \mathrm{MeV}$  and two different values of  $\chi$ -nucleon or  $\chi$ -electron scattering cross sections, as indicated in the legend. In the case of the LZ detector, the light brown histogram further represents the  $^{37} \mathrm{Ar}$  background, which originates from cosmogenic activation of the xenon prior to underground deployment, producing short-lived  $^{37} \mathrm{Ar}$  that decayed during the first run [7].

# 4.1 LZ analysis

For the analysis of LZ data, we have performed a spectral analysis using the following Poissonian  $\chi^2$  function [87]

$$
\begin{array}{l} \chi^ {2} (\vec {S}; \alpha , \beta , \delta) = 2 \sum_ {i = 1} ^ {5 1} \left[ R _ {\text {p r e d}} ^ {i} (\vec {S}; \alpha , \beta , \delta) - R _ {\exp} ^ {i} + R _ {\exp} ^ {i} \ln \left(\frac {R _ {\text {e x p}} ^ {i}}{R _ {\text {p r e d}} ^ {i} (\vec {S} ; \alpha , \beta , \delta)}\right) \right] \tag {4.4} \\ + \left(\frac {\alpha}{\sigma_ {\alpha}}\right) ^ {2} + \left(\frac {\beta}{\sigma_ {\beta}}\right) ^ {2} + \left(\frac {\delta}{\sigma_ {\delta}}\right) ^ {2}, \\ \end{array}
$$

where  $R_{\mathrm{exp}}^{i}$  denotes the experimental differential events in the  $i$ th recoil energy bin, as reported in ref. [7], while the predicted differential events contain the DSNB-boosted DM signal, as well as all background components:  $R_{\mathrm{pred}}^{i}(\vec{S};\alpha ,\beta ,\delta) = (1 + \alpha)R_{\mathrm{bkg}}^{i} + (1 + \beta)R_{\mathrm{DSNB-BDM}}^{i}(\vec{S}) + (1 + \delta)R_{37\mathrm{Ar}}^{i}$ . It is worth noting that, in accordance with ref. [88], the  $R_{\mathrm{bkg}}$  spectrum is calculated by eliminating the  $^{37}\mathrm{Ar}$  contributions from the total background provided in ref. [7]. The nuisance parameters  $\{\alpha ,\beta ,\delta \}$  are introduced to incorporate the uncertainty on background, neutrino flux distribution and  $^{37}\mathrm{Ar}$  components with  $\sigma_{\alpha} = 13\%$ ,  $\sigma_{\beta} = 40\%$  [60] and  $\sigma_{\delta} = 100\%$ . For each new physics parameter belonging to  $\vec{S}$  (i.e.  $m_{\chi}$  or  $\sigma_{\chi i}$ ), we have marginalized the  $\chi^2$  function over all nuisance parameters.

![](images/427809f41dea882a645e8e2e52c0d3d43aec5302e004a4751a3888453b45c984.jpg)  
Figure 3. Simulated signal (colored histograms) and experimental data (black points with error bars) as a function of the electron-equivalent ionization energy, for the LZ (left) and XENONnT (right) experiments. The DSNB-boosted DM events have been computed assuming  $m_{\chi} = 300 \mathrm{MeV}$  and different values of scattering cross sections, see the legend. The blue and light brown histograms refer to the background events as provided by the collaborations.

![](images/c7930cc2c6c3b878caf2349d41b897281525c46c6c9f6760064808bb6cd333b8.jpg)

# 4.2 XENONnT analysis

The following Gaussian  $\chi^2$  function is used for the analysis of XENONnT data [87]

$$
\chi^ {2} (\vec {\mathcal {S}}; \beta) = \sum_ {i = 1} ^ {3 0} \left(\frac {R _ {\mathrm {p r e d}} ^ {i} (\vec {\mathcal {S}} ; \beta) - R _ {\mathrm {e x p}} ^ {i}}{\sigma^ {i}}\right) ^ {2} + \left(\frac {\beta}{\sigma_ {\beta}}\right) ^ {2}. \tag {4.5}
$$

Here,  $R_{\mathrm{pred}}^i (\vec{\mathcal{S}};\beta) = (1 + \beta)R_{\mathrm{DSNB - BDM}}^i (\vec{\mathcal{S}}) + B_0^i$ , with  $B_0$  denoting the simulated background mentioned in ref. [8]. The rest of the details are similar to the LZ analysis.

# 5 Results

We present in figure 4 the  $90\%$  C.L. exclusion regions on the DSNB-boosted DM, in the planes  $(m_{\chi},\sigma_{\chi^e})$  and  $(m_{\chi},\sigma_{\chi^n})$ . We consider the case of DM scattering off electrons (left panel) and nuclei (right panel), and show both constraints obtained using LZ (blue) and XENONnT (red) experimental data.

For comparison purposes, we also show limits from other dedicated experiments and studies. In the  $\chi$ -electron scattering channel (left panel), we consider results from DD experiments (gray contour), mainly SENSEI [89], DAMIC [90], EDELWEISS [91], SuperCDMS [92], DarkSide-50 [93], XENON1T [94] and PandaX-II [95]. Additionally, we include constraints from solar reflection [96, 97] (dark yellow) and from Super-Kamiokande [31] (green). Similarly, for the  $\chi$ -nucleus scattering channel (right panel), we take into account results from various experiments and studies. These include again DD experiments (black region) [92, 98-106], together with constraints from the Super-Kamiokande experiment [107, 108] (green) and the XQC rocket experiment [109] (light pink). We further depict cosmological bounds in cyan

![](images/29331bb4f9404201ec4ab2c299178c4209dd5c50c04bfcc064f6c6687b44a02c.jpg)  
Figure 4.  $90\%$  C.L. exclusion regions in the DSNB-boosted DM parameter space, obtained for scattering off electrons, for the benchmark  $\sigma_{\nu \chi} = \sigma_{\chi e}$  (left panel) and nuclei, for the benchmark  $\sigma_{\nu \chi} = \sigma_{\chi n}$  (right). We show results obtained with LZ (blue) and XENONnT (red) data. For comparison purposes, existing limits from other studies are also shown (see main text for details).

![](images/45e792e7c6fd4f6e094d3b5756ffb2fe587de215d4df2f857daed5bc95526ecd.jpg)

(note that they are obtained as a  $95\%$  C.L. exclusion region). Among them, the strongest bounds come from the Lyman-  $\alpha$  forest, but also include constraints from cosmic-microwave-background anisotropy measurements and Milky-Way satellite galaxies [110-115]. We also represent the Big Bang Nucleosynthesis (BBN) limit on the mass of real scalar and Dirac fermion DM [116]. By considering the limits from these experiments, we establish a comprehensive picture of the constraints on the DSNB-boosted DM parameter space. Additionally, let us mention that DM-neutrino interactions are in principle subject to strong cosmological bounds. In particular, Lyman-  $\alpha$  data provide stringent constraints on  $\sigma_{\nu \chi}$  [117, 118], although dependent on several assumptions, including massless neutrinos. A more recent analysis, accounting for neutrino masses, points toward a preference for a non-zero DM-neutrino interaction strength [119] thus providing further motivations for our work.

Finally, we compare our results with recent bounds on sub-GeV cosmic-ray boosted DM (CRDM), also derived using LZ data [30] (light yellow). While many references in the literature have addressed cosmic-ray boosted DM, ref. [30] allows for a direct comparison of our results given that we both analyze the same LZ data set. As can be seen, our constraints obtained assuming a boost from DSNB neutrinos are ruling out a larger region of the parameter space. This is understood since the local interstellar population of cosmic rays is about one order of magnitude less intense compared to the flux of DSNB neutrinos, the latter peaking at lower ( $\sim 10$  MeV) energies, though. Notice also that ref. [30] ignored nuclear-physics corrections, that are rather important for a CRDM-based analysis where a larger momentum transfer is involved (compared to our DSNB-based analysis). The correct inclusion of such effects would drastically modify the CRDM region shown in the plot. Although not shown here, nuclear effects in CRDM studies have been considered by incorporating Helm-type nuclear form factors, for example, in the analysis of XENON1T excess data in refs. [26, 29]. At this point we should note that given that the initial CRDM flux peaks beyond  $100\mathrm{MeV}$  and extends up to GeV energies, a large momentum transfer is involved in the process and it cannot be

realistically accounted for through the inclusion of nuclear form factors. For an appropriate treatment of nuclear structure at such large momentum transfer see ref. [28].

While a significant part of our constraints lie in a region of parameter space already probed by other searches, these results highlight the complementarity and significance of the LZ and XENONnT data in probing the sub-GeV DM parameter space. Also, it is worth mentioning that both these experiments have just started taking data and we are only using their very first data sets obtained with exposure time of only a few months, but still the bounds are already competitive with other bounds. As the statistics of these experiments will increase, their data will play a much more important role in constraining the DSNB-boosted DM parameter space. Moreover, and as mentioned in section 3, let us recall that we present the limits on  $\sigma_{\chi e}$  and  $\sigma_{\chi n}$  under the assumption of  $\sigma_{\nu \chi} = \sigma_{\chi e}$  and  $\sigma_{\nu \chi} = \sigma_{\chi n}$ , respectively. However, note that the lower limit of our closed regions is basically dependent only on  $\sqrt{\sigma_{\chi e}\sigma_{\nu\chi}}$  and  $\sqrt{\sigma_{\chi n}\sigma_{\nu\chi}}$ , respectively, so it can be easily recast into alternative scenarios in which the magnitude of the two cross sections is different. The upper limit of our closed contours though, has a stronger dependence on the attenuation effects and therefore depends on a more complicated combination of  $\sigma_{\chi e,n}$  and  $\sigma_{\nu \chi}$ . As it can be noticed, our exclusion regions have a closed shape, due to the inclusion of attenuation effects (see the discussion below). Large scattering cross sections i.e.  $\sigma_{\chi e} \gtrsim 2 \times 10^{-28} \mathrm{~cm}^2$  ( $\sigma_{\chi n} \gtrsim 8 \times 10^{-28} \mathrm{~cm}^2$ ) for DM scattering off electrons (nucleons) and  $m_{\chi} = 0.1 \mathrm{MeV}$  result into a strong attenuation during the propagation of the DM particles through the Earth and are therefore disfavored.

To understand the shape of our bounds in more detail, we now explore the implications of considering attenuation effects and adopting a realistic nuclear form factor. We examine how these factors influence the exclusion limits on the scattering cross section and DM mass. The energy loss experienced by the DSNB-boosted DM due to its scattering with the Earth's material introduces a significant impact on the derived exclusion limits. Figure 5 illustrates the consequences of considering (blue, closed contour) or neglecting (red exclusion line) attenuation effects for  $\chi - e$  scattering, while figure 6 depicts the same for  $\chi - \mathcal{N}$  scattering. Clearly, attenuation effects impose an upper bound on the exclusion region. Above a certain scattering cross section, energy loss becomes substantial such that the DSNB-boosted DM particles cannot be detected because of severe attenuation. This fact confirms the necessity of properly accounting for Earth's attenuation effects to ensure accurate and robust constraints on the DNSB-boosted DM parameters. Finally, for low DM mass, e.g.  $m_{\chi} \lesssim 1 \mathrm{MeV}$ , we find that the exclusion regions which incorporate attenuation effects (blue contours) are excluding lower cross sections (below  $\sigma_{\chi e} = 10^{-31} \mathrm{~cm}^2$ ) compared to the case where attenuation effects are ignored (red contours) in figure 5. This is expected since in the low-mass region, for a fixed  $m_{\chi}$  the number of events corresponding to the attenuated case is larger compared to the unattenuated one. The reason behind this behavior is twofold: first for low  $m_{\chi}$  the DM flux reaching the detector is larger at low  $T_{\chi}$  when attenuation effects are taken into account in comparison to the unattenuated case. Second, the non-vanishing attenuated DM flux at lower  $T_{\chi}$  is triggering lower recoils  $T_{e}$  in the detector, which due to their inversely proportional dependence on the differential cross section given in eq. (3.8) are eventually leading to an enhancement of the event rates given by eq. (4.1). The same reasoning applies for the case of nuclear recoils, discussed below, but due to kinematics this effect is not visible in figure 6. Further details are given in appendix D.

![](images/aa43c2084a90aa77e1185623e8639e1e0c58d765baf315baa84808b1d1b27925.jpg)  
Figure 5.  $90\%$  C.L. exclusion limits on  $\sigma_{\chi e}$  and  $m_{\chi}$ , obtained including (blue closed contour) or neglecting (red line) attenuation effects due to DM scattering off Earth's elements before reaching the detectors. Left panel shows bounds obtained with XENONnT data, while right panel refers to LZ data.

![](images/2aea75a0f7a8be4a81a4807a6bb4eb68be2453b7503a46c6e5f015e53cad3bd2.jpg)

![](images/32abcc67dac0ab02df817899f77cdf4e1072b44081d661e2c8c0247259db1484.jpg)  
Figure 6.  $90\%$  C.L. exclusion limits on  $\sigma_{\chi n}$  and  $m_{\chi}$ , obtained including (blue closed contour) or neglecting (red line) attenuation effects due to DM scattering off Earth's elements before reaching the detectors. Left panel shows bounds obtained with XENONnT data, while right panel refers to LZ data. Additionally, the impact of the nuclear form factor is shown, with solid lines representing the Helm form factor, and dashed lines obtained assuming  $F = 1$  for both attenuated and unattenuated scenarios.

![](images/907c1f7e6397e6f1f950fffb5321b1c359380cf9e5591b6203938130611d6a4f.jpg)

Furthermore, for the case of  $\chi -\mathcal{N}$  scattering, considering a realistic nuclear form factor [see e.g. eq. (3.14)] introduces visible effects, as illustrated in figure 6. The inclusion of the Helm form factor effectively modifies the energy-loss dynamics compared to the  $F = 1$  scenario. Indeed, the finite nuclear size reduces the differential DM-nucleus cross section given in eq. (3.8), thus leading to a decrease in the energy-loss rate  $dT_{\chi}^{z} / dz$  when a larger momentum transfer is involved i.e. for the high-energy tail of DSNB-boosted DM flux (for an illustration see figure 10 in appendix C). This modification results in a shift of the upper

bound of the exclusion region, allowing for slightly higher  $\sigma_{\chi n}$  values before energy loss renders particles undetectable.

Such an exploration of the interplay between attenuation effects and nuclear-physics considerations leads to a more comprehensive and robust understanding of the complex dynamics governing DSNB-boosted DM scatterings. These insights emphasize the significance of accounting for the latter effects in the accurate interpretation of experimental results, providing insights into the implications of  $\chi-\mathcal{N}$  scattering.

Before closing our discussion we should stress that obtaining large,  $\mathcal{O}(10^{-30})\mathrm{cm}^2$ , DM-nucleon cross sections from conventional DM models is challenging, primarily due to the stringent bounds imposed on mediators coupled to nucleons, as pointed out in [67, 120]. A model-dependent study should be performed to thoroughly address the applicability of our limits. The interested reader is for instance referred to [120], where a sub-GeV DM candidate is presented, dubbed HYPER, that can accommodate large DM-nucleon cross sections. This example presents a promising pathway to reconcile large direct detection cross sections with cosmological and laboratory observations.

# 6 Conclusions

In this work we have revisited the possibility that sub-GeV DM is boosted to semi-relativistic velocities through collisions with the DSNB. Such a very energetic component of the total DM flux, while subdominant, would be detectable at DM DD experiments thus amplifying their experimental reach.

We have analyzed the most recent data from two cutting-edge DM experiments, LZ and XENONnT, and we have obtained stringent constraints on the DSNB-boosted DM parameter space. For the first time, we have considered both electron and nuclear scatterings and obtained bounds on the relevant cross sections and DM mass. These new bounds extend the reach of typical DM DD searches to even lower DM mass ranges, and they are consistent with other searches for cosmic-ray boosted DM. In this regard, we have illustrated that due to the higher intensity of the DSNB flux in comparison to cosmic rays, the former allows to exclude a larger part of the available parameter space. We further point out that in obtaining our results for DM-nuclei scattering we reliably account for corrections due to the finite nuclear size by incorporating a Helm-type nuclear form factor.

Our results hence complement other existing searches for sub-GeV DM. Most of all, they show that even with their very first and limited exposure time data sets, the low-threshold XENONnT and LZ experiments dominate the terrestrial limits on DM-nucleus scattering at very low DM masses, with good complementarity to neutrino experiments like Super-Kamiokande and cosmological observations. Finally we have highlighted the importance of including Earth's attenuation effects in the analysis. In particular, we have demonstrated that they have a strong impact on the upper bound of our derived exclusion regions disfavoring large DM scattering cross sections, namely  $\sigma_{\chi e} \gtrsim 2 \times 10^{-28} \mathrm{~cm}^2$  and  $\sigma_{\chi n} \gtrsim 8 \times 10^{-28} \mathrm{~cm}^2$  for  $m_{\chi} = 0.1 \mathrm{MeV}$ .

In summary our current analysis, by taking into account the Earth's attenuation and finite nuclear size effects, provides accurate and robust constraints on the parameter space of low mass DSNB-boosted DM, using the first data sets of LZ and XENONnT.

![](images/fe78153fac269b5c5bf25189fa6f87def3049a671ca7ef35410563c22783b85e.jpg)  
Figure 7. Geometry of the underground detector's location at a depth  $h_d$  below Earth's surface, and distance  $z$  traveled by DM before detection.

# Acknowledgments

We are grateful to Filippo Sala for useful comments on this manuscript. We acknowledge the use of the high-performance computing facilities offered by the Bhaskara Cluster at IISER Bhopal, which significantly facilitated the completion of this research. VDR acknowledges financial support by the CIDEXG/2022/20 grant (project “D’AMAGAT”) funded by Generalitat Valenciana and by the Spanish grant PID2020-113775GB-I00 (MCIN/AEI/10.13039/501100011033). AM is grateful for the invaluable financial support provided by the Prime Minister Research Fellowship (PMRF), sponsored by the Government of India (PMRF ID: 0401970). The work of DKP was supported by the Hellenic Foundation for Research and Innovation (H.F.R.I.) under the “3rd Call for H.F.R.I. Research Projects to support Post-Doctoral Researchers” (Project Number: 7036). The work of RS has been supported by the SERB, Government of India grant SRG/2020/002303.

# A Geometry of an underground detector's location

In the context of DM detection, the geometry of the detector's underground position plays a pivotal role in assessing the anticipated signal rate and characteristics of the search. We explore the configuration of a detector located at a depth  $h_d$  below the Earth's surface, as depicted in figure 7. $^{10}$  Our primary concern is to determine the distance  $z$  that corresponds to the distance traveled by DM particles between a specific impact point on the Earth's surface ( $I$ ) and the detector ( $D$ ). This distance depends on the zenith angle,  $\theta_z$ , representing

Table 1. Properties of the most abundant elements in the Earth's geosphere. The table presents the main elements found within the Earth's crust, mantle, and core [77, 78]. For each element, the respective mass number  $(A)$ , relative abundance, and nuclear number density  $(n_{\mathcal{N}})$  are provided.  

<table><tr><td>Element</td><td>Mass Number (A)</td><td>Relative Abundance (%)</td><td>nN(cm-3)</td></tr><tr><td>Fe</td><td>55.845</td><td>32.1</td><td>6.11 × 1022</td></tr><tr><td>O</td><td>15.999</td><td>30.1</td><td>3.45 × 1022</td></tr><tr><td>Si</td><td>28.086</td><td>15.1</td><td>1.77 × 1022</td></tr><tr><td>Mg</td><td>24.305</td><td>13.9</td><td>1.17 × 1022</td></tr><tr><td>S</td><td>32.065</td><td>2.9</td><td>2.33 × 1021</td></tr><tr><td>Ca</td><td>40.078</td><td>1.5</td><td>7.94 × 1020</td></tr><tr><td>Al</td><td>26.982</td><td>1.4</td><td>1.09 × 1021</td></tr></table>

the angle between the vertical direction and the line connecting the detector to the chosen point on the Earth's surface.

For the purpose of computing the distance  $z$  we employ the law of cosines within the triangle  $\triangle \mathrm{ODI}$  (see figure 7), leading to the following expression:

$$
\begin{array}{l} R _ {E} ^ {2} = z ^ {2} + \left(R _ {E} - h _ {d}\right) ^ {2} - 2 R _ {E} \left(R _ {E} - h _ {d}\right) \cos \left(\pi - \theta_ {z}\right) \\ \Rightarrow z = - \left(R _ {E} - h _ {d}\right) \cos \theta_ {z} + \sqrt {R _ {E} ^ {2} - \left(R _ {E} - h _ {d}\right) ^ {2} \sin^ {2} \theta_ {z}}. \tag {A.1} \\ \end{array}
$$

By means of this expression, we can precisely determine the distance  $z$  that characterizes the spatial relationship between the position of the detector and the Earth's surface point of interest for a given zenith angle. Understanding this geometric configuration is crucial for a more realistic simulation of the interactions between DM particles and the detector and in predicting potential signals in DM experiments.

# B Geophysical properties of Earth

We model the Earth's interior as a sphere of constant electron and nuclear densities ( $n_e = 8 \times 10^{23} \, \mathrm{cm}^{-3}$  and  $n_{\mathcal{N}} = 3.44 \times 10^{22} \, \mathrm{cm}^{-3}$ ), based on the abundances of the main elements as shown in table 1.

# C Energy loss experienced by the DSNB-boosted DM due to scattering inside Earth

In this appendix we investigate the dependence of the DSNB-boosted DM's underground kinetic energy (here denoted as  $T_{\chi}^{z}$ ) on the distance  $(z)$  and initial value of the DM kinetic energy at Earth's surface  $(T_{\chi}^{0})$ . Such considerations provide essential insights into the impact of attenuation effects within Earth's materials. The left panel of figure 8 illustrates  $T_{\chi}^{z}$  as a function of  $z$ , derived by solving eq. (3.6), while considering different initial values of  $T_{\chi}^{0}$ . This analysis is performed separately for  $\chi - e$  (dashed curves) and  $\chi - \mathcal{N}$  (solid curves) scattering

![](images/50f4f5a702c3270ff379c1a3e34227357a0a6877ee04dcd98c3ab4202d17193f.jpg)  
Figure 8. Left panel:  $T_{\chi}^{z}$  as a function of  $z$  for fixed  $T_{\chi}^{0}$ . Right panel:  $T_{\chi}^{z}$  versus  $T_{\chi}^{0}$  at fixed  $z = 1.4 \, \mathrm{km}$ . We fix  $m_{\chi} = 300 \, \mathrm{MeV}$  and  $\sigma_{\chi e}(\sigma_{\chi n}) = 10^{-29} \, \mathrm{cm}^2$ . Solid lines correspond to DM-nuclei scattering, while dashed lines represent DM-electron scattering.

![](images/18f25850ad1a4bea7c8ea75a56f7782fb2aec53083feb46229b2e8e851fd77ed.jpg)

![](images/114ec11ef1c03b6c42411b5a749b47aeac9c0b46feccd9eff9bda89192b91de0.jpg)  
Figure 9. Contour plot of values of  $T_{\chi}^{z}$  in the  $(z, T_{\chi}^{0})$  plane, for  $m_{\chi} = 300 \mathrm{MeV}$  and  $\sigma_{\chi e}(\sigma_{\chi n}) = 10^{-29} \mathrm{cm}^2$ . The left panel refers to DM-electron scattering, while the right panel refers to DM-nuclei scattering. Both panels depict the variation of  $T_{\chi}^{z}$  across different values of  $T_{\chi}^{0}$  and  $z$ , providing insights into the interplay between these parameters.

![](images/b98eea840c4b397325d8959f51f7d110248bcf458c8fe7b8da2555a0ad732480.jpg)

scenarios. As can be seen, the energy of the DSNB-boosted DM undergoes a rapid decrease for distances larger than  $\sim 1\mathrm{km}$  for  $\chi -\mathcal{N}$  scattering, while in the case of  $\chi -e$  scattering, this substantial energy reduction takes place at distances beyond  $\sim 100\mathrm{km}$ . In the right panel of figure 8, we present  $T_{\chi}^{z}$  as a function of the initial kinetic energy  $T_{\chi}^{0}$ , computed at a fixed depth  $z = 1.4\mathrm{km}$  (typical of DD experiments like XENONnT and LZ), i.e. corresponding to the special case  $\theta_z = 0$  for which  $z = h_d$ . This plot offers a direct comparison of the energy evolution assuming different initial conditions. The intricate interplay between these parameters is further visualized in the contour plot displayed in figure 9, which depicts the variation of  $T_{\chi}^{z}$  across the  $(z,T_{\chi}^{0})$  plane. In all cases, we adopt a representative DSNB-boosted DM particle mass  $m_{\chi} = 300\mathrm{MeV}$  and assume a cross section  $\sigma_{\chi e} = \sigma_{\chi n} = 10^{-29}\mathrm{cm}^2$ .

For the case of  $\chi -\mathcal{N}$  scattering, incorporating finite nuclear size effects through the nuclear form factor becomes particularly relevant. Figure 10 shows the impact of nuclear effects by

![](images/5f96d65c0151b958af84a49a48ded5027f63bf12e72b9f38ab74b6772dcb7edd.jpg)  
Figure 10.  $T_{\chi}^{z}$  as a function of the distance  $z$ , for different initial kinetic energies of DM particles at Earth's surface ( $T_{\chi}^{0}$ ), focusing on  $\chi - \mathcal{N}$  scattering interactions. The DM particle mass and cross section are fixed to  $m_{\chi} = 300 \, \mathrm{MeV}$  and  $\sigma_{\chi n} = 10^{-29} \, \mathrm{cm}^2$ . The depicted results are obtained considering both the Helm form factor (solid lines) and  $F = 1$  (dotted lines).

considering two distinct scenarios in the calculation of the final kinetic energy of DM particles reaching the detector: (i) including a Helm-type nuclear form factor and (ii) completely neglecting nuclear effects, i.e.  $F = 1$ . Notably, the effect driven by nuclear physics becomes evident around  $z = 0.1\mathrm{km}$ . In particular for high-energy DSNB-boosted DM particles, the disparity between the two scenarios becomes substantial. All in all, incorporating nuclear physics effects through the Helm form factor leads to a reduction of the total cross section, resulting in a mitigated energy loss. Remarkably, DSNB-boosted DM particles with kinetic energies exceeding  $100\mathrm{MeV}$  undergo such a marginal energy loss that their energy remains nearly constant at distances around  $z \lesssim 100\mathrm{km}$ .

# D Behavior of the exclusion regions in the low DM mass regime

Here we provide further clarifications regarding the behavior of the exclusion regions observed in figure 5, where the sensitivity of XENONnT and LZ experiments to DM-electron scattering was presented assuming both attenuated and unattenuated DSNB-boosted DM fluxes. For relatively low DM masses  $m_{\chi}$ , the exclusion limit in figure 5 corresponding to DM-electron scattering when attenuation effects are taken into account (blue contours) is extending to lower cross section values compared to the unattenuated case (red contours). As we will explain, this is a direct consequence related to the shape of the energy distribution of DSNB-boosted DM particles reaching the terrestrial detector as well as to the recoil dependence of the differential event rates.

For low values of  $T_{\chi}$  the attenuated flux becomes significantly larger in comparison to the unattenuated one, a behaviour that is more pronounced when the value of  $m_{\chi}$  gets smaller. Moreover, a non-vanishing DM flux at lower values of  $T_{\chi}$  results into detectable signals of lower recoil energies  $T_{e}$ . As explained in the main text, the number of detected events is inversely proportional to  $T_{e}$ , see e.g. eqs. (3.8), (4.1), thus a signal enhancement is expected for lower recoils. As a consequence, the events originating from the attenuated

flux are enhanced in comparison to those coming from the unattenuated flux, affecting the sensitivity in the parameter space of  $(m_{\chi},\sigma_{\chi e})$  accordingly. This is particularly relevant for small values of  $m_{\chi}$  (especially for  $m_{\chi} \lesssim 1\mathrm{MeV}$ ). The opposite behavior occurs for larger values of  $m_{\chi}$  (see the discussion below).

A detailed illustration of these effects is presented in figure 11. Each row from top to bottom corresponds to different values of DM mass  $m_{\chi} = 0.1, 1, 100 \mathrm{MeV}$ , while left and right panels show the differential DSNB-boosted DM flux distribution and the respective differential event rates at XENONnT. $^{11}$  For each case, a comparison is given between the attenuated and unattenuated cases, while the chosen cross section values are allowed by the exclusion limits in figure 5. Results in the left panels of figure 11 demonstrate that the lower the DM mass the larger the attenuated flux becomes in the low  $T_{\chi}$  regime. In the right panels, the corresponding event rates show that the lower the DM mass the larger the enhancement of the events coming from the attenuated flux becomes compared to the unattenuated case. Let us finally note that for  $m_{\chi} = 100 \mathrm{MeV}$ , the unattenuated flux is larger and so is the respective number of events; consequently the exclusion region that corresponds to the unattenuated flux is slightly more constraining at this value of  $m_{\chi}$ .

Before closing, let us stress that the obtained results highlight the intricate nature of direct detection of sub-GeV DM and the importance of considering these factors when interpreting experimental results.

# E Overview of the gauged  $\mathrm{U}(1)_{B_1 - 3L_e}$  extension

In section 5, we have presented our results for the benchmark case  $\sigma_{\nu \chi} = \sigma_{\chi e}$  or  $\sigma_{\nu \chi} = \sigma_{\chi n}$ . This specific choice allows us to derive constraints on DM scattering in a simplified, yet representative manner. However, as explained in section 5, our results can be easily recast into scenarios beyond this benchmark.

The critical point to be addressed is whether this benchmark choice can be realized in Ultra-Violet (UV) complete models for DM. As we will explain below, the answer is affirmative. This benchmark choice can be realized within the SM by introducing additional scalar and vector leptons and/or quarks and writing down Yukawa interactions for SM fermions and DM. However, for such scalar-mediated scenarios, our benchmark case can be obtained only by requiring a fine-tuning of the Yukawa couplings of the different fermions, which might not be theoretically appealing.

In contrast, extending the SM with a new gauge symmetry and assigning different charges to the fermions provides a more elegant solution. This approach naturally leads to comparable cross sections for DM scattering off different fermions, just by choosing appropriate charges for the fermions, without the need for any fine-tuning. Therefore, while the SM extension with an additional scalar provides a valid framework, the introduction of a new gauge symmetry offers a more compelling and theoretically appealing scenario.

For the reader's convenience in this appendix we provide details regarding the gauged  $\mathrm{U}(1)_{B_1 - 3L_e}$  SM extension (motivated by ref. [69]), which constitutes a framework that can accommodate interactions where the DM scattering cross sections with neutrinos, electrons,

![](images/772589824e4f5569dd7ba2da36421f33ac6c572a7acccfb7108a996aca796862.jpg)

![](images/7373f1c6ff3cc6964c072cb5c5ba3095eff55e32ef921abb92efeb29d65b914f.jpg)

![](images/7f94adc70b312b3d47df45939c7f6f0407a1c6b8e63740201b0879c259635319.jpg)

![](images/e21b8325ac9f5db5e8ad72ec4f9d55268e8f33ce363487fb335802c806ecbba2.jpg)

![](images/0a874627e7d489b32f702d9c90df167a303fcfc9302f33401b6d340bcf541ba7.jpg)  
Figure 11. Left: differential DSNB-boosted DM flux distribution as a function of the DM energy  $(T_{\chi})$  for both attenuated and unattenuated scenarios. Right: simulated differential events for the XENONnT experiment in response to DSNB-boosted DM interactions with electrons, corresponding to both attenuated and unattenuated scenarios. From top to bottom rows the DM mass is fixed at  $m_{\chi} = 0.1, 1$  and  $100\mathrm{MeV}$ , while the corresponding cross section values are obeying the exclusion limits of figure 5 and read  $\sigma_{\chi e} = 6.6\times 10^{-32}, 4.5\times 10^{-31}$  and  $9.9\times 10^{-31}\mathrm{cm}^2$ , respectively.

![](images/d1cd6c0a942ea9ab7ee79203beb4cdc13f84fa9c88f85c588cfe1cb1cf4ce69d.jpg)

Table 2. Matter content and charge assignment of the gauged  $B_{1} - 3L_{e}$  model.  

<table><tr><td>Fields</td><td>SU(3)c⊗ SU(2)L⊗ U(1)Y</td><td>U(1)B1-3Le</td></tr><tr><td>L1 ≈ Le</td><td>(1,2,-1)</td><td>-3</td></tr><tr><td>l1 ≈ eR</td><td>(1,1,-2)</td><td>-3</td></tr><tr><td>νeR</td><td>(1,1,0)</td><td>-3</td></tr><tr><td>Lμ/τ</td><td>(1,2,-1)</td><td>0</td></tr><tr><td>μR/τR</td><td>(1,1,-2)</td><td>0</td></tr><tr><td>νμR/τR</td><td>(1,1,0)</td><td>0</td></tr><tr><td>Q1</td><td>(3,2,1/3)</td><td>1</td></tr><tr><td>u1</td><td>(3,1,4/3)</td><td>1</td></tr><tr><td>d1</td><td>(3,1,-2/3)</td><td>1</td></tr><tr><td>Q2/3</td><td>(3,2,1/3)</td><td>0</td></tr><tr><td>u2/3</td><td>(3,1,4/3)</td><td>0</td></tr><tr><td>d2/3</td><td>(3,1,-2/3)</td><td>0</td></tr><tr><td>H</td><td>(1,2,1)</td><td>0</td></tr><tr><td>φ</td><td>(1,1,0)</td><td>y</td></tr><tr><td>χ</td><td>(1,1,0)</td><td>x</td></tr></table>

and nucleons are comparable. The choice of this particular flavor-dependent gauge extension of the SM is motivated by the desire to achieve comparable DM scattering cross sections with neutrinos, electrons, and nucleons. In DM-electron and DM-nucleon scattering, only one generation of leptons and quarks is involved, respectively. However, in DM-neutrino scattering, all three generations of neutrinos can contribute. Therefore, to ensure comparable cross sections, it becomes necessary to assign charges generation by generation, a feature naturally accommodated in our chosen model. Details are provided below.

The charges of SM quark  $(Q_{i})$  and lepton  $(L_{i})$  doublets as well as the quark and lepton singlets  $(u_{i},d_{i},l_{i})$  and right handed neutrinos  $\nu_{i_R}$ , where  $i = 1,2,3$  denotes the generation index, are given in table 2.

In table 2, in addition to SM fermions, three right-handed neutrinos have been added  $(\nu_{e_R}, \nu_{\mu_R}, \nu_{\tau_R})$ , the inclusion of  $\nu_{e_R}$  being required by anomaly cancellation conditions while the other two are introduced to facilitate neutrino mass generation. Regarding the scalar fields, apart from the SM Higgs doublet  $(H)$ , the singlet field  $(\phi)$  is added for the Spontaneous Symmetry Breaking (SSB) of  $B_1 - 3L_e$  gauge symmetry, while the singlet scalar  $\chi$  serves as the DM candidate. Unlike fermion charges, the scalar charges cannot be fixed by the anomaly cancellation conditions, and thus they are left free. However, their charges can be constrained by additional requirements e.g. DM stability as we will discuss below.

The  $\mathrm{SU}(2)_L\otimes \mathrm{U}(1)_Y\otimes \mathrm{U}(1)_{B_1 - 3L_e}$  invariant Lagrangian of the model is given as follows:

■Fermion-Gauge Sector: The covariant derivative is defined as

$$
D ^ {\mu} = \partial^ {\mu} + i g T ^ {a} W _ {a} ^ {\mu} + i \frac {g ^ {\prime}}{2} Y B ^ {\mu} + i g _ {x} Q _ {B _ {1} - 3 L _ {e}} Z ^ {\prime \mu}, \tag {E.1}
$$

where  $g_{x}$  is the  $\mathrm{U}(1)_{B_1 - 3L_e}$  gauge coupling strength,  $Q_{B_1 - 3L_e}$  are the  $B_{1} - 3L_{e}$  charges of the fields listed in table 2 and  $W_{a}^{\mu}, B^{\mu}, Z^{\prime \mu}$  are the weak, hypercharge, and  $B_{1} - 3L_{e}$  mediators respectively. The  $W_{3}^{\mu}$  and  $B^{\mu}$  fields will further mix to form the photon  $A^{\mu}$  and the  $Z^{\mu}$ . Hence the Lagrangian density in the Fermion-Gauge sector can be written as

$$
\mathscr {L} \subset \sum_ {j = 1} ^ {3} \left(i \bar {Q} _ {j} \gamma_ {\mu} D ^ {\mu} Q _ {j} + i \bar {u} _ {j} \gamma_ {\mu} D ^ {\mu} u _ {j} + i \bar {d} _ {j} \gamma_ {\mu} D ^ {\mu} d _ {j} + i \bar {L} _ {j} \gamma_ {\mu} D ^ {\mu} L _ {j} + i \bar {l} _ {j} \gamma_ {\mu} D ^ {\mu} l _ {j} + i \bar {\nu} _ {j _ {R}} \gamma_ {\mu} D ^ {\mu} \nu_ {j _ {R}}\right).
$$

Gauge Kinetic Sector: The gauge kinetic term is

$$
\mathscr {L} \subset - \frac {1}{4} W _ {a} ^ {\mu \nu} W _ {\mu \nu} ^ {a} - \frac {1}{4} B ^ {\mu \nu} B _ {\mu \nu} - \frac {1}{4} Z ^ {\prime \mu \nu} Z _ {\mu \nu} ^ {\prime}, \tag {E.3}
$$

where  $W_{\mu \nu}^{a}$ ,  $B_{\mu \nu}$ , and  $Z_{\mu \nu}'$  are the field strength tensors corresponding to the gauge groups  $\mathrm{SU}(2)_L$ ,  $\mathrm{U}(1)_Y$ , and  $\mathrm{U}(1)_{B_1 - 3L_e}$  respectively.

Yukawa Sector: The Lagrangian density in the Yukawa sector is given by

$$
\mathcal {L} \subset - Y _ {d} \overline {{Q}} H d - Y _ {u} \overline {{Q}} \tilde {H} u - Y _ {l} \overline {{L}} H l - Y _ {\nu} \overline {{L}} \tilde {H} \nu_ {R} - M _ {R} \overline {{\nu_ {e _ {R} ^ {c}}}} \nu_ {e _ {R}} \phi + \mathrm {h . c .}. \qquad \mathrm {(E . 4)}
$$

In eq. (E.4) we have suppressed the generation indices to avoid cluttering. Note that the SM gauge charges allow also for the term  $\overline{\nu_R^c}\nu_R\chi$ , however, the presence of such a term would lead to the decay of  $\chi$ . This term can be easily forbidden by the  $\mathrm{U}(1)_{B_1 - 3L_e}$  symmetry which implies  $x\neq 0$  and  $x\neq |6|$ .

Scalar Sector: The Lagrangian density in the scalar sector can be expressed as follows

$$
\mathscr {L} \subset (D _ {\mu} H) ^ {\dagger} (D _ {\mu} H) + (D _ {\mu} \phi) ^ {\dagger} (D _ {\mu} \phi) + (D _ {\mu} \chi) ^ {\dagger} (D _ {\mu} \chi) - V (H, \phi , \chi). \tag {E.5}
$$

The potential term  $V(H,\phi ,\chi)$  in (E.5) is given by

$$
\begin{array}{l} V (H, \phi , \chi) = \mu_ {H} ^ {2} H ^ {\dagger} H + \frac {\lambda_ {H}}{2} (H ^ {\dagger} H) ^ {2} + \mu_ {\phi} ^ {2} (\phi^ {\dagger} \phi) + \frac {\lambda_ {\phi}}{2} (\phi^ {\dagger} \phi) ^ {2} + \mu_ {\chi} ^ {2} (\chi^ {\dagger} \chi) + \frac {\lambda_ {\chi}}{2} (\chi^ {\dagger} \chi) ^ {2} \\ + \lambda_ {H \phi} \left(H ^ {\dagger} H\right) \left(\phi^ {\dagger} \phi\right) + \lambda_ {H \chi} \left(H ^ {\dagger} H\right) \left(\chi^ {\dagger} \chi\right) + \lambda_ {\phi \chi} \left(\phi^ {\dagger} \phi\right) \left(\chi^ {\dagger} \chi\right) + \text {h . c .}. \tag {E.6} \\ \end{array}
$$

DM decay terms such as  $(H^{\dagger}H)\chi^{\dagger}\phi$ ,  $(H^{\dagger}H)\chi \phi$ ,  $(\phi^{2})\chi$ ,  $(\phi^{\dagger})^{2}\chi$  etc., can be easily avoided by choosing  $x\neq |y|$ , and  $x\neq 2|y|$  in the potential, eq. (E.6). Additionally, it is worth noting that while  $H$  and  $\phi$  acquire vacuum expectation values (vev) to spontaneously break  $\mathrm{SU}(2)_L\otimes \mathrm{U}(1)_Y\otimes \mathrm{U}(1)_{B_1 - 3L_e}$  symmetry, the DM candidate  $\chi$  does not acquire a vev.

Thus, in summary the  $\mathrm{U}(1)_{B_1 - 3L_e}$  charge  $x$  of the DM  $\chi$  can take any value except  $x = 0$ ,  $x = |6|$ ,  $x = |y|$  and  $x = 2|y|$ .

The cross sections for DM scattering with electrons, nucleons, and neutrinos through  $Z^{\prime}$  mediator can be expressed as follows:

- DM-electron scattering  $(\sigma_{\chi e})$ : DM particles can scatter off electrons in direct-detection experiments through  $Z^{\prime}$  exchange; the DM-electron cross section can be expressed in terms of the coupling [121]

$$
\sigma_ {\chi e} = \frac {3 6 x ^ {2} \mu_ {\chi e} ^ {2} g _ {x} ^ {4}}{\pi m _ {Z ^ {\prime}} ^ {4}}, \tag {E.7}
$$

where  $\mu_{\chi e}$  denotes the DM-electron reduced mass and  $m_{Z^{\prime}}$  the mediator mass.

- DM-nucleon scattering  $(\sigma_{\chi n})$ : similarly the DM-nucleon cross section at zero momentum transfer can be written as [122]

$$
\sigma_ {\chi n} = \frac {3 6 x ^ {2} \mu_ {\chi n} ^ {2} g _ {x} ^ {4}}{\pi m _ {Z ^ {\prime}} ^ {4}}, \tag {E.8}
$$

where  $\mu_{\chi n}$  stands for the DM-nucleon reduced mass.

- Neutrino-DM scattering  $(\sigma_{\nu \chi})$ : finally, the neutrino-DM cross section can be expressed as [123, 124]

$$
\sigma_ {\nu \chi} = \frac {3 6 x ^ {2} E _ {\nu} ^ {2} g _ {x} ^ {4}}{\pi m _ {Z ^ {\prime}} ^ {4}}. \tag {E.9}
$$

Thus, the  $B_{1} - 3L_{e}$  gauge symmetry simultaneously provides a framework for the DM matter extension of SM and naturally leads to our benchmark scenario.

# References

[1] PLANCK collaboration, Planck 2018 results. Part VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [Erratum ibid. 652 (2021) C4] [arXiv:1807.06209] [INSPIRE].  
[2] G. Bertone, D. Hooper and J. Silk, Particle dark matter: Evidence, candidates and constraints, Phys. Rep. 405 (2005) 279 [hep-ph/0404175] [INSPIRE].  
[3] F.S. Queiroz, Dark Matter Overview: Collider, Direct and Indirect Detection Searches, in the proceedings of the 51st Rencontri des Moriond on EW Interactions and Unified Theories, La Thuile, Italy, 12-19 March 2016, ARISF (2016), pp. 427-436 [arXiv:1605.08788] [INSPIRE].  
[4] S.N. Gninenko, D.V. Kirpichnikov and N.V. Krasnikov, Search for Light Dark Matter with accelerator and direct detection experiments: comparison and complementarity of recent results, arXiv:2307.14865 [INSPIRE].  
[5] J. Billard et al., Direct detection of dark matter — APPEC committee report, Rept. Prog. Phys. 85 (2022) 056201 [arXiv:2104.07634] [INSPIRE].  
[6] LZ collaboration, Search for new physics in low-energy electron recoils from the first LZ exposure, Phys. Rev. D 108 (2023) 072006 [arXiv:2307.15753] [INSPIRE].

[7] LZ collaboration, First Dark Matter Search Results from the LUX-ZEPLIN (LZ) Experiment, Phys. Rev. Lett. 131 (2023) 041002 [arXiv:2207.03764] [INSPIRE].  
[8] XENON collaboration, Search for New Physics in Electronic recoil Data from XENONnT, Phys. Rev. Lett. 129 (2022) 161805 [arXiv:2207.11330] [INSPIRE].  
[9] XENON collaboration, First Dark Matter Search with Nuclear Recoils from the XENONnT Experiment, Phys. Rev. Lett. 131 (2023) 041003 [arXiv:2303.14729] [INSPIRE].  
[10] XENON collaboration, Dark Matter Search Results from a One Ton-Year Exposure of XENON1T, Phys. Rev. Lett. 121 (2018) 111302 [arXiv:1805.12562] [INSPIRE].  
[11] PANDAX-II collaboration, Results of dark matter search using the full PandaX-II exposure, Chin. Phys. C 44 (2020) 125001 [arXiv:2007.15469] [INSPIRE].  
[12] LUX collaboration, Results from a search for dark matter in the complete LUX exposure, Phys. Rev. Lett. 118 (2017) 021303 [arXiv:1608.07648] [INSPIRE].  
[13] DEAP collaboration, Search for dark matter with a 231-day exposure of liquid argon using DEAP-3600 at SNOLAB, Phys. Rev. D 100 (2019) 022004 [arXiv:1902.04048] [INSPIRE].  
[14] DARKSIDE collaboration, DarkSide-50 532-day Dark Matter Search with Low-Radioactivity Argon, Phys. Rev. D 98 (2018) 102006 [arXiv:1802.07198] [INSPIRE].  
[15] SUPERCDMS collaboration, Results from the Super Cryogenic Dark Matter Search Experiment at Soudan, Phys. Rev. Lett. 120 (2018) 061802 [arXiv:1708.08869] [INSPIRE].  
[16] XENON collaboration, Physics reach of the XENON1T dark matter experiment, JCAP 04 (2016) 027 [arXiv:1512.07501] [INSPIRE].  
[17] XENON collaboration, Projected WIMP sensitivity of the XENONnT dark matter experiment, JCAP 11 (2020) 031 [arXiv:2007.08796] [INSPIRE].  
[18] LZ collaboration, The LUX-ZEPLIN (LZ) Experiment, Nucl. Instrum. Meth. A 953 (2020) 163047 [arXiv:1910.09124] [INSPIRE].  
[19] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[20] Y. Ema, F. Sala and R. Sato, Light Dark Matter at Neutrino Experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[21] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse Direct Detection: Cosmic Ray Scattering With Light Dark Matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[22] J.B. Dent, B. Dutta, J.L. Newstead and I.M. Shoemaker, Bounds on Cosmic Ray-Boosted Dark Matter in Simplified Models and its Corresponding Neutrino-Floor, Phys. Rev. D 101 (2020) 116007 [arXiv:1907.03782] [INSPIRE].  
[23] J. Alvey, M. Campos, M. Fairbairn and T. You, Detecting Light Dark Matter via Inelastic Cosmic Ray Collisions, Phys. Rev. Lett. 123 (2019) 261802 [arXiv:1905.05776] [INSPIRE].  
[24] Z.-H. Lei, J. Tang and B.-L. Zhang, Constraints on cosmic-ray boosted dark matter in CDEX-10, Chin. Phys. C 46 (2022) 085103 [arXiv:2008.07116] [INSPIRE].  
[25] J.B. Dent, B. Dutta, J.L. Newstead, I.M. Shoemaker and N.T. Arellano, Present and future status of light dark matter models from cosmic-ray electron upscattering, Phys. Rev. D 103 (2021) 095015 [arXiv:2010.09749] [INSPIRE].  
[26] C. Xia, Y.-H. Xu and Y.-F. Zhou, Production and attenuation of cosmic-ray boosted dark matter, JCAP 02 (2022) 028 [arXiv:2111.05559] [INSPIRE].

[27] CDEX collaboration, Constraints on sub-GeV dark matter boosted by cosmic rays from the CDEX-10 experiment at the China Jinping Underground Laboratory, Phys. Rev. D 106 (2022) 052008 [arXiv:2201.01704] [INSPIRE].  
[28] J. Alvey, T. Bringmann and H. Kolesova, No room to hide: implications of cosmic-ray upscattering for GeV-scale dark matter, JHEP 01 (2023) 123 [arXiv:2209.03360] [INSPIRE].  
[29] C.A. Arguelles, V. Muñoz, I.M. Shoemaker and V. Takhistov, Hadrophilic light dark matter from the atmosphere, Phys. Lett. B 833 (2022) 137363 [arXiv:2203.12630] [INSPIRE].  
[30] T.N. Maity and R. Laha, *Cosmic-ray boosted dark matter in Xe-based direct detection experiments*, Eur. Phys. J. C 84 (2024) 117 [arXiv:2210.01815] [INSPIRE].  
[31] C.V. Cappiello and J.F. Beacom, *Strong New Limits on Light Dark Matter from Neutrino Experiments*, Phys. Rev. D 100 (2019) 103011 [Erratum ibid. **104** (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[32] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, Leptonic New Force and Cosmic-ray Boosted Dark Matter for the XENON1T Excess, Phys. Lett. B 811 (2020) 135863 [arXiv:2006.13910] [INSPIRE].  
[33] W. Cho, K.-Y. Choi and S.M. Yoo, Searching for boosted dark matter mediated by a new gauge boson, Phys. Rev. D 102 (2020) 095010 [arXiv:2007.04555] [INSPIRE].  
[34] PANDAX-II collaboration, Search for Cosmic-Ray Boosted Sub-GeV Dark Matter at the PandaX-II Experiment, Phys. Rev. Lett. 128 (2022) 171801 [arXiv:2112.08957] [INSPIRE].  
[35] L. Su, L. Wu and B. Zhu, An improved bound on accelerated light dark matter, Sci. China Phys. Mech. Astron. 67 (2024) 221012 [arXiv:2308.02204] [INSPIRE].  
[36] G. Herrera and K. Murase, Probing Light Dark Matter through Cosmic-Ray Cooling in Active Galactic Nuclei, arXiv:2307.09460 [INSPIRE].  
[37] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, *Cosmic-Neutrino-Boosted Dark Matter (νBDM)* arXiv:2101.11262 [INSPIRE].  
[38] Y. Zhang, Speeding up dark matter with solar neutrinos, Prog. Theor. Exp. Phys. 2022 (2022) 013B05 [arXiv:2001.00948] [INSPIRE].  
[39] W. Chao, T. Li and J. Liao, Connecting Primordial Black Hole to boosted sub-GeV Dark Matter through neutrino, arXiv:2108.05608 [INSPIRE].  
[40] R. Calabrese, D.F.G. Fiorillo, G. Miele, S. Morisi and A. Palazzo, Primordial black hole dark matter evaporating on the neutrino floor, Phys. Lett. B 829 (2022) 137050 [arXiv:2106.02492] [INSPIRE].  
[41] R. Calabrese, M. Chianese, D.F.G. Fiorillo and N. Saviano, *Electron scattering of light new particles from evaporating primordial black holes*, Phys. Rev. D 105 (2022) 103024 [arXiv:2203.17093] [INSPIRE].  
[42] T. Li and J. Liao, *Electron-target experiment constraints on light dark matter produced in primordial black hole evaporation*, Phys. Rev. D 106 (2022) 055043 [arXiv:2203.14443] [INSPIRE].  
[43] Y.-H. Lin, W.-H. Wu, M.-R. Wu and H.T.-K. Wong, Searching for Afterglow: Light Dark Matter Boosted by Supernova Neutrinos, Phys. Rev. Lett. 130 (2023) 111002 [arXiv:2206.06864] [INSPIRE].

[44] Y.-H. Lin, T.-H. Tsai, G.-L. Lin, H.T.-K. Wong and M.-R. Wu, *Signatures of afterglows from light dark matter boosted by supernova neutrinos in current and future large underground detectors*, Phys. Rev. D 108 (2023) 083013 [arXiv:2307.03522] [INSPIRE].  
[45] A. Das and M. Sen, Boosted dark matter from diffuse supernova neutrinos, Phys. Rev. D 104 (2021) 075029 [arXiv:2104.00027] [INSPIRE].  
[46] D. Ghosh, A. Guha and D. Sachdeva, Exclusion limits on dark matter-neutrino scattering cross section, Phys. Rev. D 105 (2022) 103029 [arXiv:2110.00025] [INSPIRE].  
[47] S. Bhowmick, D. Ghosh and D. Sachdeva, *Blazar boosted dark matter — direct detection constraints on σeχ: role of energy dependent cross sections*, JCAP 07 (2023) 039 [arXiv:2301.00209] [INSPIRE].  
[48] J.M. Cline, M. Puel and T. Toma, Boosted dark matter from a phantom fluid, Phys. Lett. B 848 (2024) 138377 [arXiv:2308.01333] [INSPIRE].  
[49] A. Ambrosone, M. Chianese, D.F.G. Fiorillo, A. Marinelli and G. Miele, Starburst Galactic Nuclei as Light Dark Matter Laboratories, Phys. Rev. Lett. 131 (2023) 111003 [arXiv:2210.05685] [INSPIRE].  
[50] F. D'Eramo and J. Thaler, Semi-annihilation of Dark Matter, JHEP 06 (2010) 109 [arXiv:1003.5912] [INSPIRE].  
[51] J. Berger, Y. Cui and Y. Zhao, Detecting Boosted Dark Matter from the Sun with Large Volume Neutrino Detectors, JCAP 02 (2015) 005 [arXiv:1410.2246] [INSPIRE].  
[52] T. Toma, Distinctive signals of boosted dark matter from its semiannihilation, Phys. Rev. D 105 (2022) 043007 [arXiv:2109.05911] [INSPIRE].  
[53] K. Agashe, Y. Cui, L. Necib and J. Thaler, (In)direct Detection of Boosted Dark Matter, JCAP 10 (2014) 062 [arXiv:1405.7370] [INSPIRE].  
[54] K. Kong, G. Mohlabeng and J.-C. Park, Boosted dark matter signals uplifted with self-interaction, Phys. Lett. B 743 (2015) 256 [arXiv:1411.6632] [INSPIRE].  
[55] M. Aoki and T. Toma, Boosted Self-interacting Dark Matter in a Multi-component Dark Matter Model, JCAP 10 (2018) 020 [arXiv:1806.09154] [INSPIRE].  
[56] D. Borah, M. Dutta, S. Mahapatra and N. Sahu, Boosted self-interacting dark matter and XENON1T excess, Nucl. Phys. B 979 (2022) 115787 [arXiv:2107.13176] [INSPIRE].  
[57] J.F. Beacom, The Diffuse Supernova Neutrino Background, Annu. Rev. Nucl. Part. Sci. 60 (2010) 439 [arXiv:1004.3311] [INSPIRE].  
[58] C. Lunardini, Diffuse supernova neutrinos at underground laboratories, Astropart. Phys. 79 (2016) 49 [arXiv:1007.3252] [INSPIRE].  
[59] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].  
[60] S. Horiuchi, J.F. Beacom and E. Dwek, The Diffuse Supernova Neutrino Background is detectable in Super-Kamiokande, Phys. Rev. D 79 (2009) 083013 [arXiv:0812.3157] [INSPIRE].  
[61] A. De Gouvêa, I. Martinez-Soler, Y.F. Perez-Gonzalez and M. Sen, Fundamental physics with the diffuse supernova background neutrinos, Phys. Rev. D 102 (2020) 123012 [arXiv:2007.13748] [INSPIRE].  
[62] S. Ando, N. Ekanger, S. Horiuchi and Y. Koshio, Diffuse neutrino background from past core-collapse supernovae, arXiv:2306.16076 [INSPIRE].

[63] PARTICLE DATA collaboration, Review of Particle Physics, Prog. Theor. Exp. Phys. 2022 (2022) 083C01 [INSPIRE].  
[64] E.E. Salpeter, The Luminosity function and stellar evolution, Astrophys. J. 121 (1955) 161 [INSPIRE].  
[65] H. Yuksel, M.D. Kistler, J.F. Beacom and A.M. Hopkins, Revealing the High-Redshift Star Formation Rate with Gamma-Ray Bursts, Astrophys. J. Lett. 683 (2008) L5 [arXiv:0804.4008] [INSPIRE].  
[66] SUPER-KAMIOKANDE collaboration, Supernova Relic Neutrino Search with Neutron Tagging at Super-Kamiokande-IV, Astropart. Phys. 60 (2015) 41 [arXiv:1311.3738] [INSPIRE].  
[67] N.F. Bell, J.L. Newstead and I. Shaukat-Ali, *Cosmic-ray dark matter confronted by constraints on new light mediators*, arXiv:2309.11003 [INSPIRE].  
[68] E. Ma, Gauged  $B - 3L_{\tau}$  and radiative neutrino masses, Phys. Lett. B 433 (1998) 74 [hep-ph/9709474] [INSPIRE].  
[69] C. Bonilla, T. Modak, R. Srivastava and J.W.F. Valle,  $\mathrm{U}(1)_{B_3 - 3L_\mu}$  gauge symmetry as a simple description of  $b\rightarrow s$  anomalies, Phys. Rev. D 98 (2018) 095002 [arXiv:1705.00915] [INSPIRE].  
[70] L.M.G. de la Vega, L.J. Flores, N. Nath and E. Peinado, Complementarity between dark matter direct searches and CEvNS experiments in U(1)' models, JHEP 09 (2021) 146 [arXiv:2107.04037] [INSPIRE].  
[71] K.C.Y. Ng et al., Resolving small-scale dark matter structures using multisource indirect detection, Phys. Rev. D 89 (2014) 083001 [arXiv:1310.1915] [INSPIRE].  
[72] J.F. Navarro, C.S. Frenk and S.D.M. White, A Universal density profile from hierarchical clustering, Astrophys. J. 490 (1997) 493 [astro-ph/9611107] [INSPIRE].  
[73] B.J. Kavanagh, R. Catena and C. Kouvaris, *Signatures of Earth-scattering in the direct detection of Dark Matter*, JCAP 01 (2017) 012 [arXiv:1611.05453] [INSPIRE].  
[74] G.D. Mack, J.F. Beacom and G. Bertone, Towards Closing the Window on Strongly Interacting Dark Matter: Far-Reaching Constraints from Earth's Heat Flow, Phys. Rev. D 76 (2007) 043523 [arXiv:0705.4298] [INSPIRE].  
[75] T. Emken and C. Kouvaris, How blind are underground and surface detectors to strongly interacting Dark Matter?, Phys. Rev. D 97 (2018) 115047 [arXiv:1802.04764] [INSPIRE].  
[76] G.D. Starkman, A. Gould, R. Esmailzadeh and S. Dimopoulos, Opening the Window on Strongly Interacting Dark Matter, Phys. Rev. D 41 (1990) 3594 [INSPIRE].  
[77] J.W. Morgan and E. Anders, Chemical composition of Earth, Venus, and Mercury, Proc. Natl. Acad. Sci. U.S.A. 77 (1980) 6973.  
[78] W.F. McDonough, *Compositional Model for the Earth's Core*, in Treatise on Geochemistry. Volume 2, H.D. Holland and K.K. Turekian eds., Elsevier (2003), pp. 547-568 [DOI:10.1016/b0-08-043751-6/02015-6].  
[79] A.M. Dziewonski and D.L. Anderson, Preliminary reference Earth model, Phys. Earth Planet. Interiors 25 (1981) 297 [INSPIRE].  
[80] J.D. Lewin and P.F. Smith, Review of mathematics, numerical factors, and corrections for dark matter experiments based on elastic nuclear recoil, Astrophys. 6 (1996) 87 [INSPIRE].  
[81] K. Freese, M. Lisanti and C. Savage, Colloquium: Annual modulation of dark matter, Rev. Mod. Phys. 85 (2013) 1561 [arXiv:1209.3339] [INSPIRE].

[82] R.H. Helm, Inelastic and Elastic Scattering of 187 Mev Electrons from Selected Even-Even Nuclei, Phys. Rev. 104 (1956) 1466 [INSPIRE].  
[83] S.-F. Ge, J. Liu, Q. Yuan and N. Zhou, Diurnal Effect of Sub-GeV Dark Matter Boosted by Cosmic Rays, Phys. Rev. Lett. 126 (2021) 091804 [arXiv:2005.09480] [INSPIRE].  
[84] J.-W. Chen, H.-C. Chi, C.-P. Liu and C.-P. Wu, Low-energy electronic recoil in xenon detectors by solar neutrinos, Phys. Lett. B 774 (2017) 656 [arXiv:1610.04177] [INSPIRE].  
[85] J. Lindhard, M. Scharff and H. Schiott, Range concepts and heavy ion searches, Mat. Fys. Medd. K. Dan. Vidensk. Selsk. 33 (1963) 1.  
[86] K.A. ShivaSankar, A. Majumdar, D.K. Papoulias, H. Prajapati and R. Srivastava, Implications of first  $LZ$  and XENONnT results: A comparative study of neutrino properties and light mediators, Phys. Lett. B 839 (2023) 137742 [arXiv:2208.06415] [INSPIRE].  
[87] F.M.L. Almeida Jr., M. Barbi and M.A.B. do Vale, A Proposal for a different chi square function for Poisson distributions, Nucl. Instrum. Meth. A 449 (2000) 383 [hep-ex/9911042] [INSPIRE].  
[88] M. Atzori Corona, W.M. Bonivento, M. Cadeddu, N. Cargioli and F. Dordei, New constraint on neutrino magnetic moment and neutrino millicharge from LUX-ZEPLIN dark matter search results, Phys. Rev. D 107 (2023) 053001 [arXiv:2207.05036] [INSPIRE].  
[89] SENSEI collaboration, SENSEI: Direct-Detection Results on sub-GeV Dark Matter from a New Skipper-CCD, Phys. Rev. Lett. 125 (2020) 171802 [arXiv:2004.11378] [INSPIRE].  
[90] DAMIC collaboration, Constraints on Light Dark Matter Particles Interacting with Electrons from DAMIC at SNOLAB, Phys. Rev. Lett. 123 (2019) 181802 [arXiv:1907.12628] [INSPIRE].  
[91] EDELWEISS collaboration, First germanium-based constraints on sub-MeV Dark Matter with the EDELWEISS experiment, Phys. Rev. Lett. 125 (2020) 141301 [arXiv:2003.01046] [INSPIRE].  
[92] SUPERCDMS collaboration, First Dark Matter Constraints from a SuperCDMS Single-Charge Sensitive Detector, Phys. Rev. Lett. 121 (2018) 051301 [Erratum ibid. 122 (2019) 069901] [arXiv:1804.10697] [INSPIRE].  
[93] DARKSIDE collaboration, Constraints on Sub-GeV Dark-Matter-Electron Scattering from the DarkSide-50 Experiment, Phys. Rev. Lett. 121 (2018) 111303 [arXiv:1802.06998] [INSPIRE].  
[94] XENON collaboration, Light Dark Matter Search with Ionization Signals in XENON1T, Phys. Rev. Lett. 123 (2019) 251801 [arXiv:1907.11485] [INSPIRE].  
[95] PANDAX-II collaboration, Search for Light Dark Matter-Electron Scatterings in the PandaX-II Experiment, Phys. Rev. Lett. 126 (2021) 211803 [arXiv:2101.07479] [INSPIRE].  
[96] H. An, M. Pospelov, J. Pradler and A. Ritz, Directly Detecting MeV-scale Dark Matter via Solar Reflection, Phys. Rev. Lett. 120 (2018) 141801 [Erratum ibid. 121 (2018) 259903] [arXiv:1708.03642] [INSPIRE].  
[97] H. An, H. Nie, M. Pospelov, J. Pradler and A. Ritz, Solar reflection of dark matter, Phys. Rev. D 104 (2021) 103026 [arXiv:2108.10332] [INSPIRE].  
[98] SUPERCDMS collaboration, Search for Low-Mass Weakly Interacting Massive Particles Using Voltage-Assisted Calorimetric Ionization Detection in the SuperCDMS Experiment, Phys. Rev. Lett. 112 (2014) 041302 [arXiv:1309.3259] [INSPIRE].  
[99] DAMIC collaboration, Search for low-mass WIMPs in a  $0.6\mathrm{kg}$  day exposure of the DAMIC experiment at SNOLAB, Phys. Rev. D 94 (2016) 082006 [arXiv:1607.07410] [INSPIRE].

[100] NEWS-G collaboration, First results from the NEWS-G direct dark matter search experiment at the LSM, Astropart. Phys. 97 (2018) 54 [arXiv:1706.04934] [INSPIRE].  
[101] CRESST collaboration, First results from the CRESST-III low-mass dark matter program, Phys. Rev. D 100 (2019) 102002 [arXiv:1904.00498] [INSPIRE].  
[102] CDEX collaboration, Constraints on Spin-Independent Nucleus Scattering with sub-GeV Weakly Interacting Massive Particle Dark Matter from the CDEX-1B Experiment at the China Jinping Underground Laboratory, Phys. Rev. Lett. 123 (2019) 161301 [arXiv:1905.00354] [INSPIRE].  
[103] XENON collaboration, Search for Light Dark Matter Interactions Enhanced by the Migdal Effect or Bremsstrahlung in XENON1T, Phys. Rev. Lett. 123 (2019) 241803 [arXiv:1907.12771] [INSPIRE].  
[104] EDELWEISS collaboration, Searching for low-mass dark matter particles with a massive Ge bolometer operated above-ground, Phys. Rev. D 99 (2019) 082003 [arXiv:1901.03588] [INSPIRE].  
[105] EDELWEISS collaboration, Search for sub-GeV dark matter via the Migdal effect with an EDELWEISS germanium detector with NbSi transition-edge sensors, Phys. Rev. D 106 (2022) 062004 [arXiv:2203.03993] [INSPIRE].  
[106] DARKSIDE collaboration, Search for Dark-Matter-Nucleon Interactions via Migdal Effect with DarkSide-50, Phys. Rev. Lett. 130 (2023) 101001 [arXiv:2207.11967] [INSPIRE].  
[107] Y. Ema, F. Sala and R. Sato, Neutrino experiments probe hadrophilic light dark matter, SciPost Phys. 10 (2021) 072 [arXiv:2011.01939] [INSPIRE].  
[108] SUPER-KAMIOKANDE collaboration, Search for Cosmic-Ray Boosted Sub-GeV Dark Matter Using Recoil Protons at Super-Kamiokande, Phys. Rev. Lett. 130 (2023) 031802 [Erratum ibid. 131 (2023) 159903] [arXiv:2209.14968] [INSPIRE].  
[109] M.S. Mahdawi and G.R. Farrar, Constraints on Dark Matter with a moderately large and velocity-dependent DM-nucleon cross-section, JCAP 10 (2018) 007 [arXiv:1804.03073] [INSPIRE].  
[110] V. Gluscevic and K.K. Boddy, Constraints on Scattering of keV-TeV Dark Matter with Protons in the Early Universe, Phys. Rev. Lett. 121 (2018) 081301 [arXiv:1712.07133] [INSPIRE].  
[111] T.R. Slatyer and C.-L. Wu, Early- Universe constraints on dark matter-baryon scattering and their implications for a global 21 cm signal, Phys. Rev. D 98 (2018) 023013 [arXiv:1803.09734] [INSPIRE].  
[112] W.L. Xu, C. Dvorkin and A. Chael, Probing sub-GeV Dark Matter-Baryon Scattering with Cosmological Observables, Phys. Rev. D 97 (2018) 103530 [arXiv:1802.06788] [INSPIRE].  
[113] E.O. Nadler, V. Gluscevic, K.K. Boddy and R.H. Wechsler, Constraints on Dark Matter Microphysics from the Milky Way Satellite Population, Astrophys. J. Lett. 878 (2019) 32 [Erratum ibid. 897 (2020) L46] [arXiv:1904.10000] [INSPIRE].  
[114] M.A. Buen-Abad, R. Essig, D. McKeen and Y.-M. Zhong, Cosmological constraints on dark matter interactions with ordinary matter, Phys. Rep. 961 (2022) 1 [arXiv:2107.12377] [INSPIRE].  
[115] K.K. Rogers, C. Dvorkin and H.V. Peiris, Limits on the Light Dark Matter-Proton Cross Section from Cosmic Large-Scale Structure, Phys. Rev. Lett. 128 (2022) 171301 [arXiv:2111.10386] [INSPIRE].

[116] G. Krnjaic and S.D. McDermott, Implications of BBN Bounds for Cosmic Ray Upscattered Dark Matter, Phys. Rev. D 101 (2020) 123022 [arXiv:1908.00007] [INSPIRE].  
[117] R.J. Wilkinson, C. Boehm and J. Lesgourgues, Constraining Dark Matter-Neutrino Interactions using the CMB and Large-Scale Structure, JCAP 05 (2014) 011 [arXiv:1401.7597] [INSPIRE].  
[118] K. Akita and S. Ando, Constraints on dark matter-neutrino scattering from the Milky-Way satellites and subhalo modeling for dark acoustic oscillations, JCAP 11 (2023) 037 [arXiv:2305.01913] [INSPIRE].  
[119] D.C. Hooper and M. Lucca, Hints of dark matter-neutrino interactions in Lyman-α data, Phys. Rev. D 105 (2022) 103504 [arXiv:2110.04024] [INSPIRE].  
[120] G. Elor, R. McGehee and A. Pierce, Maximizing Direct Detection with Highly Interactive Particle Relic Dark Matter, Phys. Rev. Lett. 130 (2023) 031803 [arXiv:2112.03920] [INSPIRE].  
[121] R. Essig, M. Fernandez-Serra, J. Mardon, A. Soto, T. Volansky and T.-T. Yu, Direct Detection of sub-GeV Dark Matter with Semiconductor Targets, JHEP 05 (2016) 046 [arXiv:1509.01598] [INSPIRE].  
[122] R. Martinez and F. Ochoa, Spin-independent interferences and spin-dependent interactions with scalar dark matter, JHEP 05 (2016) 113 [arXiv:1512.04128] [INSPIRE].  
[123] A. Olivares-Del Campo, C. Boehm, S. Palomares-Ruiz and S. Pascoli, Dark matter-neutrino interactions through the lens of their cosmological implications, Phys. Rev. D 97 (2018) 075039 [arXiv:1711.05283] [INSPIRE].  
[124] S. Pandey, S. Karmakar and S. Rakshit, Interactions of astrophysical neutrinos with dark matter: a model building perspective, JHEP 01 (2019) 095 [Erratum ibid. 11 (2021) 215] [arXiv:1810.04203] [INSPIRE].