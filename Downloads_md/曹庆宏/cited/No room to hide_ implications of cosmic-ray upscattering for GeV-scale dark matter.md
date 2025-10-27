# No room to hide: implications of cosmic-ray upscattering for GeV-scale dark matter

James Alvey, $^{a}$  Torsten Bringmann $^{b,c}$  and Helena Kolesova $^{d,e}$

<sup>a</sup> GRAPPA Institute, Institute for Theoretical Physics Amsterdam, University of Amsterdam, Science Park 904, 1098 XH Amsterdam, The Netherlands  
$^{b}$ Department of Physics, University of Oslo, Box 1048, N-0316 Oslo, Norway  
c Theoretical Physics Department, CERN, 1211 Geneva 23, Switzerland  
$^d$ Department of Mathematics and Physics, University of Stavanger, 4036 Stavanger, Norway  
$^{e}$ AEC, Institute for Theoretical Physics, University of Bern, Sidlerstrasse 5, CH-3012 Bern, Switzerland

E-mail: j.b.g.alvey@uva.nl, torstenBringmann@fys.uio.no, helena.kolesova@uis.no

ABSTRACT: The irreducible upscattering of cold dark matter by cosmic rays opens up the intriguing possibility of detecting even light dark matter in conventional direct detection experiments or underground neutrino detectors. The mechanism also significantly enhances sensitivity to models with very large nuclear scattering rates, where the atmosphere and rock overburden efficiently stop standard non-relativistic dark matter particles before they could reach the detector. In this article, we demonstrate that cosmic-ray upscattering essentially closes the window for strongly interacting dark matter in the (sub-)GeV mass range. Arriving at this conclusion crucially requires a detailed treatment of both nuclear form factors and inelastic dark matter-nucleus scattering, as well as including the full momentum-transfer dependence of scattering amplitudes. We illustrate the latter point by considering three generic situations where such a momentum-dependence is particularly relevant, namely for interactions dominated by the exchange of light vector or scalar mediators, respectively, and for dark matter particles of finite size. As a final concrete example, we apply our analysis to a putative hexaquark state, which has been suggested as a viable baryonic dark matter candidate. Once again, we find that the updated constraints derived in this work close a significant part of otherwise unconstrained parameter space.

KEYWORDS: Particle Nature of Dark Matter, Cosmic Rays, Models for Dark Matter

ARXIV EPRINT: 2209.03360

# Contents

1 Introduction 1  
2 Cosmic-ray upscattering of dark matter 3  
3 Nuclear form factors 6

3.1 Impact on production 7  
3.2 Impact on attenuation 8

4 Inelastic scattering 10

4.1 Scattering processes and associated energy scales 10  
4.2 Computation of the inelastic cross section for neutrinos 11  
4.3 Mapping to the dark matter case 12

5 Contact interactions and beyond 16

5.1 Constant cross section 17  
5.2 Scalar mediators 19  
5.3 Vector mediators 25  
5.4 Finite-size dark matter 27

6 Hexaquarks: a viable baryonic dark matter candidate? 29  
7 Summary and conclusions 32

# 1 Introduction

The strategies to search for a dark matter (DM) component in the Universe are nowadays extremely varied, targeting many possible gravitational and non-gravitational properties such as the DM mass or standard model (SM) couplings [1]. In astrophysical, cosmological, and laboratory settings, this broadband approach has yet to conclusively reveal any non-gravitational signatures. However, via both indirect and direct searches, the very wide DM model space has been significantly restricted. The focus of this article concerns the reach of the generic class of experiments aiming to directly detect DM through a possible DM-nucleon coupling [2], known as direct detection facilities. Currently, world-leading examples of this setup include e.g. LUX-ZEPLIN (LZ) [3], PandaX-4T [4], and Xenon-1T [5], which set the strongest limits in the DM mass  $m_{\chi}$  vs. spin-independent nuclear coupling  $\sigma_{\mathrm{SI}}$  parameter space.

The sensitivity of a given direct detection experiment is controlled by a number of factors. Firstly, the event rate  $\Gamma_N$  scales with the number of DM particles that have a sufficiently large kinetic energy. Specifically, the DM energy must be large enough to induce a nuclear recoil that can trigger a signal above the detector threshold. Secondly, the rate also scales linearly with the DM-nucleon cross section  $\mathrm{d}\sigma_{\chi N} / \mathrm{d}T_N$ , at least in the above

examples, where  $T_{N}$  is the nuclear recoil energy. Thirdly, as in any count-based experiment, this signal rate should be compared to some background event rate to derive a statistically significant detection threshold. Notably, in direct detection facilities, the background rates are typically extremely low as necessitated by the small expected signal rates, although there are some important exceptions, such as a dedicated CRESST surface run [6].

The standard target for these experiments is the DM in the Galactic halo, which has characteristic velocities of the order  $v_{\chi} \sim 10^{-3}c$  and in any case cannot exceed the Galactic escape velocity  $v_{\mathrm{esc}} \sim 540\mathrm{km / s}$  [7, 8]. For a given DM mass  $m_{\chi}$ , there is hence unavoidably a maximum DM kinetic energy available to excite nuclear recoil signals of the order  $T_{N} \sim m_{\chi}^{2}v_{\mathrm{esc}}^{2} / m_{N}$ . For some DM mass  $m_{\chi}^{\mathrm{min}}$  this recoil energy must fall below the detectable threshold, and the experimental sensitivity drops to zero. For experiments such as Xenon, PandaX and LZ, it is well-known that this cut-off lies around the GeV-scale, corresponding to a detectable threshold in the keV range. As such, even though these detectors have impressive reach — currently down to the level of spin-independent cross sections of  $\sigma_{\mathrm{SI}} \sim 10^{-47}\mathrm{cm}^2$  [3-5], and even approaching the neutrino floor [9, 10] with ongoing searches — there is ample motivation (and hence, in fact, both experimental and theoretical activity) for methods to probe the sub-GeV mass range [11, 12]. This describes the first "window" in which DM can hide — it could just be that DM has a small mass out of the reach of direct detection experiments. There is yet another window at large values of the cross section  $\sigma_{\mathrm{SI}}$ , however, which will be a key focus of this article. This arises due to the fact that if DM interacts too strongly, then it can actually be the case that DM particles are unable to reach the detectors due to the attenuation of the flux in the atmosphere or the rock overburden [13-15]. This typically becomes the main prohibitive factor for cross sections at the level of  $\sigma_{\mathrm{SI}} \gtrsim 10^{-28}\mathrm{cm}^2$  [16].

There have been a number of promising experimental proposals to probe these two open windows. Attempts to extend the sensitivity to DM-nucleus interactions into the sub-GeV realm include searches for Migdal electrons [17, 18] or bremsstrahlung photons [19], accompanied by an intense low-threshold direct detection program in the development of novel detector concepts (for a recent review, see ref. [12]). Cross sections sufficiently large for DM to scatter inside the Earth before reaching underground detectors, on the other hand, can be probed by surface runs of conventional direct detection experiments (like the one performed by the CRESST collaboration [6]), or by targeting the expected diurnal modulation in the signal in this case [20, 21]. As far as this work is concerned, however, we will be interested in the role played by the irreducible astrophysical flux of highly boosted DM that originates from cosmic ray collisions with DM particles in the Galactic halo (CRDM). This was pointed out only relatively recently [22, 23], and subverts the issue of a loss in sensitivity by noting that a sub-dominant component of DM with velocities well above those in the Galactic halo can produce a detectable signal even if it is very light, i.e. for DM masses (well) below  $1\mathrm{GeV}$ . The sub-dominant nature of the flux naturally introduces a trade-off with the interaction rates that can be probed, quantitatively resulting in limits at the level of  $\sigma_{\mathrm{SI}}\sim 10^{-31}\mathrm{cm}^2$  [22]. Interestingly, CRDM does not only probe previously open parameter space at small DM masses but also results in bounds extending into the relevant regime of the second open window described above. After

this initial work pointed out the advantages of considering such a boosting mechanism, a large number of further analyses have addressed various aspects of the production [24-45], attenuation [46, 47], and detection [48-62] of astrophysically boosted DM. For a recent comprehensive (re-)analysis of all of these aspects see, e.g. Xia et al. [63], who stressed in particular that form-factor suppressed attenuation in the overburden seemingly allows us to exclude cross sections much larger than  $\sigma_{\mathrm{SI}} \sim 10^{-28} \mathrm{~cm}^2$ .

This article builds on this literature in three important ways: firstly, we point out that when DM acquires such large energies, inelastic scattering in the rock overburden above detectors such as Xenon-1T will at some point become the dominant attenuation mechanism. As such, to avoid being over-optimistic in terms of how much parameter space is excluded, we show how to include this physical effect in a self-consistent manner and derive the resulting bounds. Secondly, we broaden the applicability of these limits to models that are more realistic for DM with sub-GeV masses, moving beyond simplified contact interactions to interactions mediated by vector or scalar mediators, or DM that has some internal structure. Finally, we argue that with these improvements, and when taking into account fully complementary constraints from cosmology, there is generically no remaining open parameter space left unconstrained for nuclear cross sections exceeding  $10^{-30}\mathrm{cm}^2$ , for DM masses in the entire MeV to GeV range. We demonstrate that possible loopholes to this statement — still allowing an open window at larger cross sections — require a combination of (i) questioning the principal ability of CRESST to probe DM masses down to the published limit of  $m_{\chi} = 140\mathrm{MeV}$  [6] and (ii) choosing a rather narrow range of mediator masses  $m_{\phi} \sim 30\mathrm{MeV}$  (or finite DM extent  $r_{\chi} \sim 10\mathrm{fm}$ ). For our numerical analysis throughout the article, we use the package DarkSUSY [64]. The improved CRDM treatment reported in this work, including also updated cosmic ray fluxes and a more sophisticated use of form factors in the attenuation part, will be included in the next public release of the code.

The rest of the article is organized as follows: we start in section 2 by briefly reviewing the production of CRDM and the attenuation of the subsequent flux on its way to the detector, establishing our notation and setting up the basic formalism that our analysis relies on. In the next two sections, we discuss in more detail how to model nuclear form factors (section 3) and the impact of inelastic scattering (section 4) on the attenuation of the flux. In section 5, we consider a number of generic options for the  $Q^2$ - and  $s$ -dependence of the scattering amplitude that are more realistic than assuming a constant cross section. We complement this in section 6 with the analysis of a specific example, namely a baryonic DM candidate that has been argued to evade traditional direct detection bounds despite its relatively strong interactions with nuclei. We conclude and summarise our results in section 7.

# 2 Cosmic-ray upscattering of dark matter

We describe here, in turn, how initially non-relativistic DM particles in the Galactic halo are up-scattered by cosmic rays (CRs), how the flux of these relativistic CRDM particles is

attenuated before reaching detectors at Earth, and how to compute the resulting elastic scattering rate in direct detection experiments.

Production. The basic mechanism that we consider is the elastic scattering of CR nuclei  $N$ , with a flux of  $d\Phi_N / dT_N$ , on non-relativistic DM particles  $\chi$  in the Galactic halo. For a DM mass  $m_{\chi}$  and density profile  $\rho_{\chi}(\mathbf{r})$ , this induces a relativistic CRDM flux incident on Earth of [22, 46]

$$
\begin{array}{l} \frac {d \Phi_ {\chi}}{d T _ {\chi}} = \int \frac {d \Omega}{4 \pi} \int_ {\text {l . o . s .}} d \ell \frac {\rho_ {\chi}}{m _ {\chi}} \sum_ {N} \int_ {T _ {N} ^ {\min }} ^ {\infty} d T _ {N} \frac {d \sigma_ {\chi N}}{d T _ {\chi}} \frac {d \Phi_ {N}}{d T _ {N}} (2.1) \\ \equiv D _ {\text {e f f}} \frac {\rho_ {\chi} ^ {\text {l o c a l}}}{m _ {\chi}} \sum_ {N} \int_ {T _ {N} ^ {\min }} ^ {\infty} d T _ {N} \frac {d \sigma_ {\chi N}}{d T _ {\chi}} \frac {d \Phi_ {N} ^ {\text {L I S}}}{d T _ {N}}. (2.2) \\ \end{array}
$$

Here  $\mathbf{r}$  denotes the Galactic position, and  $d\sigma_{\chi N} / dT_{\chi}$  is the differential elastic scattering cross section for accelerating a DM particle to a kinetic recoil energy  $T_{\chi}$ . For DM particles initially at rest, this requires a minimal CR energy  $T_N^{\mathrm{min}}$  of

$$
T _ {N} ^ {\mathrm {m i n}} = \left\{ \begin{array}{l l} \left(\frac {T _ {\chi}}{2} - m _ {N}\right) \left[ 1 - \sqrt {1 + \frac {2 T _ {\chi}}{m _ {\chi}} \left(\frac {m _ {N} + m _ {\chi}\right) ^ {2}}{\left(2 m _ {N} - T _ {\chi}\right) ^ {2}}} \right] & \mathrm {f o r} T _ {\chi} <   2 m _ {N} \\ \sqrt {\frac {m _ {N}}{m _ {\chi}}} \left(m _ {N} + m _ {\chi}\right) & \mathrm {f o r} T _ {\chi} = 2 m _ {N} \\ \left(\frac {T _ {\chi}}{2} - m _ {N}\right) \left[ 1 + \sqrt {1 + \frac {2 T _ {\chi}}{m _ {\chi}} \left(\frac {m _ {N} + m _ {\chi}\right) ^ {2}}{\left(2 m _ {N} - T _ {\chi}\right) ^ {2}}} \right] & \mathrm {f o r} T _ {\chi} > 2 m _ {N} \end{array} . \right. (2. 3)
$$

Furthermore, in the second line of eq. (2.2), we have introduced an effective distance  $D_{\mathrm{eff}}$  that allows us to express the CRDM flux in the solar system in terms of the relatively well measured local interstellar CR flux,  $d\Phi_N^{\mathrm{LIS}} / dT_N$ , and the local DM density, for which we adopt  $\rho_{\chi}^{\mathrm{local}} = 0.3\mathrm{GeV/cm}^3$  [65] (noting that our final limits are independent of this choice). The advantage of this parameterisation is that uncertainties deriving from the integration over the volume relevant for CRDM production,  $\int d\Omega \int d\ell$ , are captured in a single phenomenological parameter  $D_{\mathrm{eff}}$ . Indeed, despite the complicated underlying physics, this parameter is surprisingly well constrained, with uncertainties dominated by the vertical extent of the confinement zone of Galactic CRs. In what follows, we will use a fiducial value of  $D_{\mathrm{eff}} = 10\mathrm{kpc}$ . We note that our final limits only depend logarithmically on this quantity, for large interaction rates, or scale as  $D_{\mathrm{eff}}^{-1/2}$  when attenuation in the soil or atmosphere is inefficient, respectively.

When computing the CRDM flux in eq. (2.2), we take into account the four most abundant CR species,  $N = \{p,\mathrm{He},\mathrm{C},\mathrm{O}\}$ , for which high-quality determinations of the local interstellar fluxes exist [68]. The fluxes of heavier nuclei are subject to significant uncertainties for the energies of interest to us, see e.g. the discussion in ref. [69], not least due to apparent discrepancies between AMS-02 data [70-72] and earlier measurements. We also note that the CRDM flux contribution from these heavier elements is strongly form-factor suppressed at large  $T_{\chi}$ , see section 3, and hence anyway not relevant for constraining DM with masses  $m_{\chi} \gtrsim 0.1$  GeV.

Attenuation. On its way to the detector, the CRDM flux given by eq. (2.2) is attenuated due to scattering of the CRDM particles with nuclei in the atmosphere and soil (overburden) above the experimental location. This effect can be well modelled by the energy loss equation

$$
\frac {d T _ {\chi} ^ {z}}{d z} = - \sum_ {N} n _ {N} \int_ {0} ^ {\omega_ {\chi} ^ {\max }} d \omega_ {\chi} \frac {d \sigma_ {\chi N}}{d \omega_ {\chi}} \omega_ {\chi}, \tag {2.4}
$$

which can be used to relate the average kinetic energy at depth  $z$ ,  $T_{\chi}^{z}$ , to an initial energy  $T_{\chi}$  at the top of the atmosphere. Here, the sum runs over the nuclei  $N$  in the overburden, i.e. no longer over the CR species, and  $\omega_{\chi}$  is the energy loss of a DM particle in a single collision. For elastic scattering,  $\omega_{\chi}$  is equal to the nuclear recoil energy  $T_{N}$ . In that case, the maximal energy loss of a DM particle with initial kinetic energy  $T_{\chi}^{z}$  is given by

$$
\omega_ {\chi} ^ {\mathrm {m a x}} = T _ {N} ^ {\mathrm {m a x}} = \frac {2 m _ {N}}{s} \left[ \left(T _ {\chi} ^ {z}\right) ^ {2} + 2 m _ {\chi} T _ {\chi} ^ {z} \right], \tag {2.5}
$$

where

$$
s = \left(m _ {N} + m _ {\chi}\right) ^ {2} + 2 m _ {N} T _ {\chi} ^ {z} \tag {2.6}
$$

is the (squared) CMS energy of the process. For inelastic scattering on the other hand, which we will discuss in more detail in section 4, the energy loss can in principle be as high as  $\omega_{\chi}^{\mathrm{max}} = T_{\chi}^{z}$ . For the purpose of this work we will mostly be interested in the Xenon-1T detector, located at a depth of  $z = 1.4\mathrm{km}$  in the Gran Sasso laboratory. In this case the limestone overburden has a density of  $2.71~\mathrm{g / cm^3}$  [73], mostly consisting of an admixture of  $\mathrm{CaCO_3}$  and  $\mathrm{MgCO_3}$ , and attenuation in the atmosphere can be neglected; in terms of weight percentages the dominant elements are O  $(47.91\%)$ , Ca  $(30.29\%)$ , C  $(11.88\%)$ , Mg  $(5.58\%)$ , Si  $(1.27\%)$ , Al  $(1.03\%)$  and K  $(1.03\%)$  [74]. We note that eq. (2.4) only provides an approximate description of the stopping effect of the overburden, which is nonetheless sufficiently accurate for our purposes. For a detailed comparison of this approach with Monte Carlo simulations of individual particle trajectories, see refs. [16, 63, 75-77]

Detection. The elastic scattering rate of relativistic CRDM particles arriving at underground detectors like the Xenon-1T experiment is given by

$$
\frac {d \Gamma_ {N}}{d T _ {N}} = \int_ {T _ {\chi} ^ {\min }} ^ {\infty} d T _ {\chi} \frac {d \sigma_ {\chi N}}{d T _ {N}} \frac {d \Phi_ {\chi}}{d T _ {\chi}}. \tag {2.7}
$$

Note that the above integral is over the energy of the DM particles before entering the atmosphere. On the other hand, the elastic scattering cross section  $d\sigma_{\chi N} / dT_N$  must still be evaluated at the actual DM energy,  $T_{\chi}^{z}$ , at the detector location, which requires numerically solving eq. (2.4) for  $T_{\chi}^{z}(T_{\chi})$ . The lower bound on the integral then represents the minimal initial CRDM energy that is needed to induce a nuclear recoil of energy  $T_N$  at depth  $z$ , i.e.  $T_{\chi}^{\mathrm{min}} = T_{\chi}(T_{\chi}^{z,\mathrm{min}})$ . This can be obtained by inverting the solution of eq. (2.4), where  $T_{\chi}^{z,\mathrm{min}}$  is given by the right-hand side of eq. (2.3) under the replacement  $(T_{\chi},m_{\chi},m_N)\to (T_N,m_N,m_{\chi})$ . In general, the elastic nuclear scattering cross section  $d\sigma_{\chi N} / dT_N$  is a function of both  $s$  and the (spatial) momentum transfer,

$$
Q ^ {2} = 2 m _ {N} T _ {N}. \tag {2.8}
$$

If the dependence on  $s$  can be neglected or the (dominant) dependence on  $Q^2$  factorizes — as in the case of standard form factors — then the rate in the detector given in eq. (2.7) will have an identical  $Q^2$ -dependence as compared to the corresponding rate expected from the standard population of non-relativistic halo DM. As pointed out in ref. [22], this salient feature makes it possible to directly re-interpret published limits on the latter (conventionally expressed as limits on the scattering cross section with protons) into limits on the former. Otherwise, for an accurate determination of the expected count rate in a given analysis window, one would in principle have to also model the detector response in the evaluation of eq. (2.7) and then infer limits based on the full detector likelihood (e.g. with a tool like DDCalc [78, 79]).

# 3 Nuclear form factors

The target nuclei used in direct detection experiments are typically larger than the de Broglie wavelength of DM with standard Galactic velocities, at least for heavy nuclei, implying that the incoming DM particles only 'see' part of the nucleus. Since the elastic scattering process is fundamentally induced by a coupling between DM and the constituents of these nuclei, this means that it should be suppressed by a nuclear form factor,  $G^2 (Q^2)$ , compared to the naive expectation that the nuclear cross section is merely a coherent sum of the cross sections of all the constituents (for recent pedagogic accounts of conventional direct DM searches, see e.g. refs. [80, 81]). For CRDM, this effect is amplified, given the smaller de Broglie wavelengths associated to the faster moving upscattered DM particles.

These nuclear form factors are essentially Fourier transforms of the number density of nucleons inside the nucleus, usually approximated by the experimentally easier accessible charge density. A common parameterization is the one suggested by Helm [82], which is based on modelling the nucleus as a hard sphere with a Gaussian smearing (in configuration space). For heavy nuclei we follow instead a slightly more accurate approach and implement model-independent form factors [83], based on elastic electron scattering data. Concretely, we implement their Fourier-Bessel (FB) expansion approach, with parameters taken from ref. [84]. For nuclei where the FB parameters are not available, notably Mg and K, we use model-independent Sum of Gaussians (SOG) form factors instead.

For  $Q^2 \gg (0.1\mathrm{GeV})^2$  one starts to resolve the inner structure of the nucleons themselves, which we discuss in more detail in section 4. Let us however briefly mention that in the case of He, this effect is already largely captured by the above description in that we take the SOG form factors from ref. [84] (thus improving on the simple dipole prescription used, e.g., in ref. [22]). For the proton, we adopt the usual dipole nucleon form factor, noting that the nuclear form factor would formally equal unity,

$$
G _ {p} ^ {2} \left(Q ^ {2}\right) = \left(1 + Q ^ {2} / \Lambda_ {p} ^ {2}\right) ^ {- 4}, \tag {3.1}
$$

![](images/862ca058812753a2803a05748d7e81dd1d50cea77327ea84e44898cde9791aed.jpg)  
Figure 1. Left panel. Expected CRDM fluxes for DM masses  $m_{\chi} = 0.001, 0.01, 0.1, 1, 10 \mathrm{GeV}$ , from top to bottom, assuming a constant spin-independent scattering cross section of  $\sigma_{\mathrm{SI}}^{p,n} = 10^{-30} \mathrm{cm}^2$  (solid lines). The effect of inelastic scattering is neglected. Dashed lines show the CRDM fluxes that would result when not taking into account the effect of form factors. Right panel. Black lines indicate the individual contributions to the CRDM flux from scattering on CR  $p$ , He, C and O, for the example of  $m_{\chi} = 100 \mathrm{MeV}$ . Other lines (highlighted only for the  $m_{\chi} = 100 \mathrm{MeV}$  case) show the total flux, as in the left panel.

![](images/c32f649e9fbf2fd4dd63e942474847374ba06e9a2c427de2509676ff4487c9d6.jpg)

with  $\Lambda_p = 0.843\mathrm{GeV}$ . This provides a very good fit to experimental data up to momentum transfers of at least  $Q^2 \sim 1\mathrm{GeV}^2$ , with an agreement of better than  $10\%$  for  $Q^2 \leq 10\mathrm{GeV}^2$  [85, 86]. We note that our final results are highly insensitive to such large momenta.

In the rest of the section, we will briefly describe the impact of nuclear form factors on the CRDM flux and the attenuation of this flux on its way to the detector. In both cases the effect is sizeable, motivating the need for a precise modelling of  $G^{2}(Q^{2})$ .

# 3.1 Impact on production

The solid lines in figure 1 show the expected CRDM flux before attenuation, cf. eq. (2.2), for a range of DM masses. For the purpose of this figure, we have assumed a constant elastic scattering cross section  $\sigma_{\mathrm{SI}}^p = \sigma_{\mathrm{SI}}^n$  on nucleons, i.e. a nuclear cross section given by

$$
\frac {d \sigma_ {\chi N}}{d T _ {\chi}} = \mathcal {C} ^ {2} \times \frac {\sigma_ {\mathrm {S I}} ^ {p}}{T _ {\chi} ^ {\operatorname* {m a x}}} \times G ^ {2} \left(2 T _ {\chi} m _ {\chi}\right). \tag {3.2}
$$

Here,

$$
\mathcal {C} ^ {2} = A ^ {2} \frac {\mu_ {\chi N} ^ {2}}{\mu_ {\chi p} ^ {2}} \tag {3.3}
$$

describes the usual coherent enhancement, in this case proportional to the square of the atomic number  $A$  of nucleus  $N$ . In the rest of the expression,  $\mu_{\chi N}(\mu_{\chi p})$  is the reduced mass of the DM/nucleus (DM/nucleon) system and the maximal DM energy  $T_{\chi}^{\mathrm{max}}$  that can result from a CR nucleus with energy  $T_{N}$  is given by the right-hand side of eq. (2.5) after replacing  $T_{\chi}^{z}\rightarrow T_{N}$  and  $m_{\chi}\leftrightarrow m_{N}$ .

In the left panel of the figure, we show that neglecting nuclear form factors (dashed lines) would lead to a significant overestimate of the CRDM flux at high energies. For  $m_{\chi} \gtrsim 0.1 \mathrm{GeV}$ , the form factor suppression even becomes the dominant effect to determine the overall normalization of the flux, while for lower DM masses, the peak of the distribution is entirely determined by the fact that the CR flux itself peaks at GeV energies. This suppression in the flux leads to a rapid deterioration of CRDM limits. Modelling form factors correctly is thus particularly important for the highest DM masses that can be probed by cosmic-ray upscattering, i.e. for  $m_{\chi} \sim 1 - 10 \mathrm{GeV}$ .

In the right panel of figure 1, the contributions from the individual CR nuclei to the CRDM flux are shown. At low energies the dominant contribution is always from Helium, closely followed by the one from protons. The high-energy part of the CRDM flux, on the other hand, is almost exclusively due to CR protons because the contribution from heavier CR nuclei is heavily form-factor suppressed. In addition, for  $m_{\chi} \gtrsim 1$  GeV, the peak amplitude of the CRDM flux — which typically has the most constraining power in direct detection experiments — is almost exclusively determined by CR  $p$  and He nuclei (see also figure 2 below to better gauge the relevant range of energies after attenuation in the overburden). For lower DM masses, on the other hand, including further high-  $Z$  CR species than those taken into account here could in principle increase the relevant part of the CRDM flux by up to  $\sim 50\%$  [63]. In what follows, we conservatively neglect these contributions, in view of both the larger uncertainties in the underlying CR fluxes and the fact that we are mainly interested in DM masses around the GeV scale.

# 3.2 Impact on attenuation

We now turn our attention to assessing the effect that the form factor suppression has on the attenuation of DM particles on their way to the detector in a direct detection experiment. For concreteness we will again focus on the case of Xenon-1T, where Xe nuclei recoiling with an energy of at least  $T_{\mathrm{Xe}} = 4.9$  keV trigger a detectable signal [5]. In figure 2, we show the minimal initial DM energy that is required to kinematically allow for this, after penetrating through the Gran Sasso rock. In practice this is done by numerically solving eq. (2.4) with DarkSUSY. Dash-dotted lines indicate the result when conservatively assuming that the stopping power in the overburden is as efficient as in the zero-momentum transfer limit (as in ref. [22]), while dashed lines show the effect of adding the additional form factor suppression for high  $Q^2$  (as in refs. [38, 63]). Solid lines, finally, demonstrate the effect of also adding the attenuation power of inelastic scattering events, as described in detail below in section 4.

For small cross sections, attenuation is inefficient and, as expected, the three approaches give the same answer. In this limit, the difference in the required DM energy is entirely due to the well-known kinematic effect, cf. eq. (2.3), that lighter particles require a higher energy to induce a given recoil of much heavier particles (up to a minimum energy of  $T_{\chi} \geq \sqrt{m_{\mathrm{Xe}}T_{\mathrm{Xe}} / 2} = 17.3\mathrm{MeV}$  in the limiting case where  $m_{\chi} \rightarrow 0$ ). Correspondingly, this also means that the CRDM fluxes cannot actually be probed by Xenon-1T for the entire range of  $T_{\chi}$  shown in figure 1; unless  $m_{\chi} \lesssim 10\mathrm{MeV}$ , however, the lowest detectable energy is always smaller than the energy at which the CRDM flux peaks.

![](images/4a03399e092da4f89b008f3a8e362dfe65b84876e11a6d07104e9b923e50c562.jpg)  
Figure 2. Minimal kinetic energy  $T_{\chi}$  that a DM particle must have at the surface of the Earth  $(z = 0)$  in order to trigger a signal in the Xenon-1T experiment, as a function of a (constant) spin-independent scattering cross section  $\sigma_{\mathrm{SI}}^{p,n}$  on nucleons. Different colors correspond to different DM masses, as in figure 1. Dash-dotted lines show the kinetic energies that would be necessary when computing the attenuation in the zero momentum transfer limit. Dashed lines illustrate the effect of adding the expected form factor suppression, cf. section 3, while solid lines show the result of our full treatment, including also inelastic scattering events (discussed in section 4).

For large cross sections, on the other hand, figure 2 shows a pronounced difference between the three approaches: while in the case of a constant cross section (dash-dotted lines) the energy loss equation results in an exponential attenuation, adding form factors (dashed lines) implies that the required initial DM energy only rises as the square root of the scattering cross section in the  $Q^2 = 0$  limit. In fact, we note that this is exactly the behaviour one would expect from eq. (2.4) for a cross section that falls off very rapidly at large momentum transfers. Comparing again to figure 1, this correspondingly enlarged range of kinetic energies that becomes kinematically accessible to Xenon-1T will inevitably lead to significantly larger rates in the detector — which, indeed, is exactly the conclusion reached in refs. [38, 63]. However, such a strong suppression of the physical stopping power of the Gran Sasso rock for a relativistic particle is highly unphysical. As we discuss in the next section, this is simply because the DM particles will start to scatter off the constituent nucleons themselves, albeit not coherently across the whole nucleus. Adding this effect (solid lines), results again in exponential attenuation in the overburden — though only at significantly larger cross sections than what would be expected when adopting a constant cross section for simplicity.

# 4 Inelastic scattering

Our discussion so far has largely neglected the impact of inelastic scattering events of relativistic DM particles incident on nuclei at rest, or vice versa. Physically, the inclusion of inelastic scattering processes is non-negotiable and should be considered in a full treatment. This is because, whilst the form factor suppression described above is the relevant feature in the transition from coherently scattering off the whole nucleus to only parts of it, once the DM or nucleus transfers a sufficiently large amount of energy  $\omega$ , the scattering will probe individual nucleon-, or even quark-level processes. The result is an additional contribution to the total scattering cross section that can easily dominate in the large energy transfer regime. As far as CRDM limits are concerned, the most important effect that the inclusion of inelastic scattering modifies is the attenuation of the flux through the Earth or atmosphere. Not including it, therefore, will lead to an overly optimistic estimate as to the amount of parameter space that is ruled out via this mechanism.<sup>3</sup> Let us note that inelastic scattering of non-relativistic DM, resulting in the excitation of low-lying states in the target nuclei, was previously both studied theoretically [19, 87–89] and searched for experimentally [90–93]. Here we concentrate on different types of inelastic processes that are only accessible to nuclei scattering off high-energy DM particles.

The rest of this section is organised as follows: firstly we give a qualitative description of the most important inelastic scattering processes, such as the excitation of hadronic resonances or quasi-elastic scattering off individual nucleons. Secondly, we explain how we obtain a quantitative estimate of these complicated nuclear interactions by making a direct analogy to the case of neutrino-nucleus scattering. In this regard, we make use of the public code GiBUU [94, 95]. Finally, we will explain how to build this into the formalism described in section 2 in terms of the DM energy loss, see eq. (2.4).

# 4.1 Scattering processes and associated energy scales

There are a number of relevant contributions to scattering cross sections on nuclei that are associated to certain characteristic energies or nuclear length scales. In the highly nonrelativistic limit, as described above, coherently enhanced elastic scattering dominates. At somewhat higher energies, more specifically momentum transfers corresponding to (inverse) length scales smaller than the size of the nucleus, the elastic scattering becomes form factor suppressed — a description which physically assumes a smooth distribution of scattering centres throughout the nucleus. The main characteristic of elastic scattering in both of these regimes is that the energy loss of the incident DM particle is uniquely related to the momentum transfer by  $\omega = Q^2 / (2m_N)$ .

This relation no longer holds for inelastic scattering processes, which are expected to become relevant at even higher energies. For our purposes, these inelastic processes can be broadly split up into three scattering regimes, depending on the energy that is transferred

(see also figure 3 below, as well as a review [96] for the discussion of the analogous situation in the case of neutrino-nucleus scattering):

- Quasi-Elastic Scattering ( $\omega \gtrsim 10^{-2}\mathrm{GeV}$ ). At suitably large energy transfers, the form factor suppression cannot be totally physical. This is because the incident DM particles will probe directly the constituent nucleons, which are inherently not smoothly distributed. Quasi-elastic scattering (QE) dominates for  $10^{-2}\mathrm{GeV} \lesssim \omega \lesssim 1\mathrm{GeV}$ , and describes this situation, i.e. where the dominant scattering is directly off individual protons (and neutrons) inside the nucleus,  $\chi p(n) \rightarrow \chi p(n)$ .  
- Excitation of Hadronic Resonances ( $\omega \gtrsim 0.2\mathrm{GeV}$ ). At higher energies still, DM-nucleon scattering can excite nuclear resonances such as  $\chi p \rightarrow \chi (\Delta \rightarrow p\pi^0)$  etc., leading to a wide variety of hadronic final states. Often, the contribution due to the lowest lying  $\Delta$  resonances (DR) is distinguished from contributions from higher resonances (HR) since the former can be well resolved and starts playing role at considerably smaller transferred energies. In a complicated nucleus such as  $^{16}\mathrm{O}$ , both the QE and resonance contributions to the scattering cross section must be resolved numerically, taking into account effects such as the nuclear potential and spin statistics.  
- Deep Inelastic Scattering ( $\omega \gtrsim 1\mathrm{GeV}$ ). Most DM couplings to nuclei and nucleons result from more fundamental couplings to quarks or gluons. As such, once the energy transfer is large enough to probe the inner structure of the nucleons ( $\omega \gtrsim 1\mathrm{GeV}$ ), then deep inelastic scattering (DIS) of DM with partons inside the nucleons can occur. Again, this should be resolved numerically to give an accurate estimate of the impact at the level of the scattering cross section.

# 4.2 Computation of the inelastic cross section for neutrinos

Due to the complicated nuclear structure of the relevant atomic targets in the Earth, or in the composition of cosmic rays, it is typically not possible to analytically compute all the contributions to DM-nucleus scattering described above. Instead, to estimate their impact on our conclusions and limits, we will make a direct connection with the physics of neutrino-nucleus scattering for which numerical codes — such as GiBUU [94] — are capable of generating the relevant differential cross sections.

In more detail, we draw the analogy between neutral current neutrino-nucleon scattering via processes such as  $\nu p\rightarrow \nu p$  and DM-nucleon scattering. Numerically modelling the neutral current quasi-elastic scattering, resonances and deep inelastic scattering as a function of the energy transferred to the nucleus,  $\omega$ , allows us to understand the relative importance of these processes as a function of the incoming neutrino energy (or DM kinetic energy  $T_{\chi}$ ). Of course, since these codes are tuned for neutrino physics, simply outputting the differential cross sections such as  $\mathrm{d}\sigma_{\nu N} / \mathrm{d}\omega$  is not sufficient. To map the results onto DM, see section 4.3 below for further details, we should re-scale the results so as to respect both the relative interaction strengths and model dependences such as e.g. the mediator mass. In general, we expect this approach to provide a good estimate of the DM-nucleus cross

section (at least) for contact interactions and scattering processes dominated by mediators in the  $t$ -channel.

At the level of implementation, we choose the settings in the GiBUU code described in table 1 (see end of text). Since we are interested in quantifying the effect of inelastic scattering on the attenuation of the CRDM flux as it passes through the Earth, we mostly focus on the total inelastic scattering cross section, i.e. the sum over all the processes described in the previous section. We numerically calculate this for the most abundant nuclei in the Gran Sasso rock,  $N = \{\mathrm{O},\mathrm{Ca},\mathrm{C},\mathrm{Mg},\mathrm{Si},\mathrm{Al},\mathrm{K}\}$ . Fundamentally, inelastic cross sections are expressed in terms of double-differential cross sections like  $\mathrm{d}^2\sigma_{\nu N} / \mathrm{d}Q^2\mathrm{d}\omega$ , since for inelastic scattering  $Q^2$  and  $\omega$  are independent variables. For integrating the energy loss equation, eq. (2.4), however, it suffices to compute

$$
\frac {\mathrm {d} \sigma_ {\nu N}}{\mathrm {d} \omega} \equiv \int_ {Q ^ {2}} \frac {\mathrm {d} ^ {2} \sigma_ {\nu N}}{\mathrm {d} Q ^ {2} \mathrm {d} \omega} \mathrm {d} Q ^ {2}. \tag {4.1}
$$

On the other hand, the full information about the  $Q^2$ -dependence of  $\mathrm{d}^2\sigma_{\nu N} / \mathrm{d}Q^2\mathrm{d}\omega$  provided by GiBUU still remains a highly useful input to our analysis. This is because the double-differential cross sections of the individual inelastic processes turn out to sharply peak at values of  $Q^2$  that have simple relations to  $\omega$ . For example, the peak position for the QE contribution corresponds to the 'elastic' relation (2.8) for nucleons. As described below, this information will be used for setting realistic reference values of  $Q^2$  to capture the model-dependence of the DM cross sections.

# 4.3 Mapping to the dark matter case

Having described the technical details of how we obtain the neutrino-nucleus inelastic cross sections using GiBUU, we now turn our attention to the mapping of these quantities onto DM models. This is a necessary step for two broad reasons:  $(a)$  the interaction strength governing the DM-nucleus interactions is typically very different from the neutrino-nucleus SM value, and  $(b)$  the way the interaction proceeds via e.g. a contact interaction or mediator exchange can lead to substantially different kinematics and non-trivial  $Q^2$ - or  $s$ -dependencies.

The total scattering cross section  $\mathrm{d}\sigma_{\chi N} / \mathrm{d}\omega$  consists of the coherent elastic scattering contribution that we compute analytically for each of the models considered in this work, and the inelastic scattering cross section that we want to estimate based on the GiBUU output:

$$
\begin{array}{l} \frac {\mathrm {d} \sigma_ {\chi N}}{\mathrm {d} \omega} = \left. \frac {\mathrm {d} \sigma_ {\chi N}}{\mathrm {d} \omega} \right| _ {\mathrm {e l}} + \left. \frac {\mathrm {d} \sigma_ {\chi N}}{\mathrm {d} \omega} \right| _ {\mathrm {i n e l}} \\ \equiv \left. \frac {\mathrm {d} \sigma_ {\chi N}}{\mathrm {d} \omega} \right| _ {\text {e l}, Q ^ {2} = 2 \omega m _ {N}} + \sum_ {i} \left. \frac {\mathrm {d} \sigma_ {\mathrm {S I}}}{\mathrm {d} \omega} \right| _ {\text {e l}, Q ^ {2} = Q _ {i, \text {r e f}} ^ {2}} \times I _ {\chi , i} \left(T _ {\chi}, \omega\right). \tag {4.2} \\ \end{array}
$$

Here  $\mathrm{d}\sigma_{\mathrm{SI}} / \mathrm{d}\omega|_{\mathrm{el}}$  is the differential DM-nucleon elastic cross section, excluding nucleon form factors such as the one given in eq. (3.1). The sum runs over the various individual processes,  $i \in (\mathrm{QE}, \mathrm{DR}, \mathrm{HR}, \mathrm{DIS})$ , which all have characteristic reference values of  $Q^2 = Q_{i,\mathrm{ref}}^2(\omega)$  where the respective inelastic cross section peaks. In the second step above, we thus choose to rescale the inelastic scattering events to the elastic scattering off a point-like nucleon. This

rescaling is motivated by the fact that for inelastic contributions like QE, the underlying process is much better described by scattering on individual nucleons than on the entire nucleus. The factor

$$
I _ {\chi , i} \left(T _ {\chi}, \omega\right) \equiv \frac {\mathrm {d} \sigma_ {\chi N} ^ {i} / \mathrm {d} \omega | _ {\text {i n e l}}}{\mathrm {d} \sigma_ {\mathrm {S I}} / \mathrm {d} \omega | _ {\mathrm {e l} , Q ^ {2} = Q _ {i , \text {r e f}} ^ {2}}} \tag {4.3}
$$

thus quantifies the ratio of the inelastic scattering process on a nucleus to the elastic scattering on an individual nucleon.

We now make the simplifying assumption that this ratio is to a certain degree model-independent, based on the expectation that DM should probe the inner structure of nucleons in a similar way as neutrinos do when only neutral current interactions are involved. Physically, indeed, this closely resembles the situation both for contact interactions and  $t$ -channel mediators. The model dependence thus dominantly comes from the structure of the term  $\mathrm{d}\sigma_{\mathrm{SI}} / \mathrm{d}\omega|_{\mathrm{el}}$ , and we approximate

$$
I _ {\chi , i} \left(T _ {\chi}, \omega\right) \approx I _ {\nu , i} \left(E _ {\nu}, \omega\right) \equiv \frac {\mathrm {d} \sigma_ {\nu N} ^ {i} / \mathrm {d} \omega | _ {\text {i n e l}}}{\mathrm {d} \sigma_ {\nu , \mathrm {S I}} ^ {i} / \mathrm {d} \omega | _ {\mathrm {e l}}}. \tag {4.4}
$$

Here, the inelastic neutrino-nucleus cross section  $\mathrm{d}\sigma_{\nu N}^{i} / \mathrm{d}\omega|_{\mathrm{inel}}(E_{\nu},\omega)$  can be obtained using the GiBUU code, as described in section 4.2, and we evaluate it at the incoming DM kinetic energy,  $E_{\nu} = T_{\chi}$ . On the other hand, a possible estimate for the denominator — the elastic neutral current neutrino-nucleon cross section without the form factor — is the average of the proton and neutron cross sections in the  $\omega \rightarrow 0$  limit [96]:

$$
\left. \frac {\mathrm {d} \sigma_ {\nu , \mathrm {S I}} ^ {i}}{\mathrm {d} \omega} \right| _ {\mathrm {e l}} = \frac {1}{2} \sum_ {j = n, p} \frac {m _ {j} G _ {F} ^ {2}}{4 \pi} \left[ \left(g _ {A} \tau_ {3} ^ {j} - \Delta_ {S}\right) ^ {2} + \left(\tau_ {3} ^ {j} - 2 \left(1 + \tau_ {3} ^ {j}\right) \sin^ {2} \theta_ {W}\right) ^ {2} \right]. \tag {4.5}
$$

Here  $\tau_3^p = 1$  and  $\tau_3^n = -1$ ,  $\theta_W$  is the weak mixing angle and  $G_{F}$  is the Fermi constant. The axial vector and strange quark contributions are encoded in the parameters  $\Delta_S \approx -0.15$  (see, e.g., ref. [97] for a discussion) and  $g_A = 1.267$  [98], respectively. Numerically the square bracket evaluates to a factor of  $\sim 2.24$  (2.01) for neutrons (protons). Let us stress, however, that this formula is valid only for energies relevant for inelastic scattering,  $0.1\mathrm{GeV} \lesssim E_\nu \lesssim 10\mathrm{GeV}$ . At much smaller energies, only the valence quarks contribute to the scattering, and we would instead have

$$
\left. \frac {\mathrm {d} \sigma_ {\nu , \mathrm {S I}} ^ {i}}{\mathrm {d} \omega} \right| _ {\text {e l}} = \frac {m _ {n} G _ {F} ^ {2}}{4 \pi} \tag {4.6}
$$

for neutrons, while the scattering on protons is strongly suppressed by a factor of  $Q_W^2 = (1 - 4\sin^2\theta_W)^2 \approx 0.012$ .

It is worth noting that in principle, we could improve the assumption made in eq. (4.4) for the quasi-elastic process, because there is a well-controlled understanding of the analytic QE cross section via the Llewellyn-Smith formalism (see section V of ref. [96]). For clarity, we choose to take a consistent prescription across all inelastic processes, and we have checked that including the full QE cross section would only introduce an additional  $\mathcal{O}(1)$  factor in the DM QE cross section. For the numerical implementation in DarkSUSY, we pre-tabulate

$I_{\nu ,i}$  from  $T_{\chi} = 0.01$  GeV up to energies of  $T_{\chi} = 10$  GeV, with 200 (101) equally log-spaced bins in  $T_{\chi}$ $(\omega)$  and a normalization as given by eq. (4.5), and then interpolate between these values. $^{4}$

We also must choose the reference values for the transferred momentum  $Q_{i,\mathrm{ref}}^2$ , which allows us to account for e.g. mediators that may be much lighter than the electroweak scale. Importantly, each process (quasi-elastic,  $\Delta$ -resonance,...) is expected to have a different characteristic  $Q^{2}$ - $\omega$  dependence that takes into account the relevant binding energies and kinematic scaling. For example, in the case of elastic scattering, the relation  $Q^2 = 2m_N\omega$  holds, whilst for quasi-elastic processes, the relevant scattering component is a nucleon such that the cross section is peaked around  $Q^2 \sim 2\overline{m}\omega$ , where  $\overline{m} \equiv (m_n + m_p) / 2$ . The resonance of a particle with mass  $m_{\mathrm{res}}$  can be accounted for by noting that part of the transferred kinetic energy is used to excite the resonance, such that the cross section peaks around  $Q^2 \sim 2\overline{m} (\omega - (m_{\mathrm{res}} - \overline{m}))$ . We have confirmed these expectations numerically by comparing directly to the doubly-differential cross section extracted from GiBUU. From this numerical comparison we further extract that  $Q^2 \sim 0.6\overline{m} (\omega - \omega_{\mathrm{DIS}})$ , with  $\omega_{\mathrm{DIS}} = 1.0\mathrm{GeV}$ , constitutes a very good fit to the peak location of the DIS cross section. In summary, we take the following reference values across the four inelastic processes:

$$
Q _ {\mathrm {Q E , r e f}} ^ {2} = 2 \overline {{m}} \omega , Q _ {\Delta , \mathrm {r e f}} ^ {2} = 2 \overline {{m}} \left(\omega - \Delta m _ {\Delta}\right)
$$

$$
Q _ {\text {r e s , r e f}} ^ {2} = 2 \bar {m} (\omega - \Delta m _ {\text {r e s}}), \quad Q _ {\text {D I S , r e f}} ^ {2} = 0. 6 \bar {m} (\omega - \omega_ {\text {D I S}}). \tag {4.7}
$$

Here,  $\Delta m_{\Delta} = 0.29\mathrm{GeV}$  is the mass difference between the  $\Delta$  baryon and an average nucleon, and  $\Delta m_{\mathrm{res}} = 0.40\mathrm{GeV}$  is an estimate for the corresponding average mass difference of the higher resonances (we checked that our final limits are insensitive to the exact value taken here).

To illustrate this procedure concretely, we consider the simple case of a contact interaction where, cf. eq. (3.2),  $\mathrm{d}\sigma_{\mathrm{SI}} / \mathrm{d}\omega|_{\mathrm{el.}} = \sigma_{\mathrm{SI}} / \omega^{\max}$  and  $\omega^{\max} = 2\overline{m}(T_{\chi}^{2} + 2\chi T_{\chi}) / ((\overline{m} + m_{\chi})^{2} + 2\overline{m} T_{\chi})$ . The results for the rescaled inelastic cross section (blue) are shown in figure 3 for a DM mass  $m_{\chi} = 1$  GeV incident on a  $^{16}\mathrm{O}$  nucleus. In this figure, we also compare to the coherent elastic contribution (green) and highlight the balance between the relative contributions to the total (integrated) cross section  $\sigma_{\chi N}^{\mathrm{tot}}$ . In particular, we see that above kinetic energies  $T_{\chi} \gtrsim 0.2$  GeV, the inelastic contribution dominates, clearly motivating the necessity of its inclusion. This is consistent with the picture previously

![](images/af8e27f96ac44f96ff570f221e35a5716039b8f5dc9f70d7c4b1deecfb52617e.jpg)

![](images/8a3759d9959691a52b15db68eadb35b0e03d26cdf5abf4642715048cd0a2d5d7.jpg)

![](images/0adca90e82dfeccd6d86fe2aeb8d068406f3457f629349690de1b3bed8fdb4fd.jpg)  
Figure 3. Comparison between the elastic (green, lower energies) and inelastic (blue, higher energies) contributions to the DM-nucleus differential cross section  $\mathrm{d}\sigma_{\chi N} / \mathrm{d}\omega$ , where  $\omega$  is the DM energy loss. This figure shows these contributions for a constant isospin-conserving DM-nucleus cross section, with  $m_{\chi} = 1\mathrm{GeV}$  and  $N = 16\mathrm{O}$ . The small colorbar on the inset of the plots, along with the stated numerical ratio, indicates the balance between elastic and inelastic scattering in terms of the contribution to the integrated cross section  $\sigma_{\chi N}^{\mathrm{tot}}$ .

![](images/4c844e0bd58a8e1818799cc345aebe75190acddcc32f1e6255844cb6438152a5.jpg)

encountered in figure 2, where we could see the impact of inelastic scattering on the energy loss. More concretely, the result lies in some intermediate regime between the  $G(Q^2) = 1$  and  $G(Q^2) \neq 1$  cases, the former/latter leading to conservative/overly optimistic limits respectively. In the next section we will derive the relevant CRDM limits in the  $\sigma_{\mathrm{SI}} - m_{\chi}$  plane for a number of models to make this point quantitatively.

Let us conclude this section by briefly returning to the implicit assumption of isospin-conserving DM interactions that we made above, with  $\sigma_{\mathrm{SI}} = \sigma_{\mathrm{SI}}^p = \sigma_{\mathrm{SI}}^n$ . Interestingly, neutral-

current induced inelastic scatterings between neutrinos and nucleons hardly distinguish between protons and neutrons [96], such that the factor  $I_{\chi,i} \approx I_{\nu,i}$  indeed becomes, by construction, largely independent of the nucleon nature. Naively, one would thus conclude that isospin-violating DM couplings can easily be incorporated in our treatment of inelastic scattering by replacing  $\sigma_{\mathrm{SI}} \rightarrow (1 / A) \times (Z\sigma_{\mathrm{SI}}^p + (A - Z)\sigma_{\mathrm{SI}}^n)$  in eq. (4.2). When doing so, however, it is important to keep in mind that the nucleon cross sections should be evaluated at energies that are relevant for inelastic scattering, not in the highly non-relativistic limit. At these high energies, isospin symmetry is typically largely restored because the nucleon couplings are no longer exclusively determined by the valence quarks, and instead receive corrections from a large number of sea quarks (and, in principle, gluons). As pointed out above, the example of neutrino scattering illustrates this effect very clearly: even though isospin is almost maximally violated at low energies, the effective neutrino couplings to neutrons and protons agree within  $\sim 5\%$  at energies around  $0.1\mathrm{GeV}$ , cf. eqs. (4.5) and (4.6). In practice, however, a possible complication often arises in that the nucleon couplings  $g_{n}$  and  $g_{p}$  are only provided in the highly non-relativistic limit. In that case, an educated guess for  $\sigma_{\mathrm{SI}}$  in the second term of eq. (4.2) is to anyway take the leading order (Born) expression — but to adopt (effective) values for both nucleon couplings that correspond to the maximum of  $|g_{p}|$  and  $|g_{n}|$  in the non-relativistic limit. This induces a model-dependent uncertainty in the normalization of the inelastic contribution that can in principle only be avoided by fully implementing the concrete interaction model in a code like GiBUU. On the other hand, the neutrino example illustrates that this error should generally not be expected to be larger than a factor of  $\sim 2$ , implying that for most applications such a more sophisticated treatment is not warranted.

# 5 Contact interactions and beyond

In sections 3 and 4 we have discussed in detail the  $Q^2$ -dependence that arises due to both form factor suppression and inelastic scattering, as well as the impact this has on the production and attenuation of the CRDM flux. This does not yet take into account, however, the possible angular and energy dependence of the elastic scattering cross section itself. In fact, for (sub-)GeV DM, a significant dependence of this type is actually expected in view of null searches for new light particles at colliders. For example, it has been demonstrated in a recent global analysis [99] that it is impossible to satisfy all relevant constraints simultaneously (even well above GeV DM masses) and at the same time maintain the validity of an effective field theory description at LHC energies.

Of course, this necessarily introduces a model-dependent element to the discussion, and in this section, the aim will be to analyse the most generic situations that can appear when considering models beyond simple contact interactions. Concretely, in section 5.2 we will study the case of a light scalar mediator, a light vector mediator in section 5.3, and the scenario where DM particles have a finite extent in section 5.4. In all these cases, we will re-interpret the published Xenon-1T limits and assess whether there is a remaining unconstrained window of large scattering cross sections for GeV-scale DM. Just before this, however, in section 5.1 we will briefly revisit the (physically less motivated) case of a

![](images/b5455fe305571d33cfe03e680988b24d498db413df1c602824364cbbbf2604e5.jpg)  
Figure 4. Left panel. Limits on a constant spin-independent DM-nucleon scattering cross section as a function of the DM mass, based on a re-interpretation of Xenon-1T limits on non-relativistic DM [5] for the CRDM component studied in this work (solid lines). Dash-dotted lines show the excluded region that results when assuming a constant cross section in the attenuation part (as in ref. [22]). Dashed lines show the effects of adding form factors in the attenuation part, but no inelastic scattering, resulting in limits similar to those derived in ref. [63]. For the latter case, for comparison, we also show the effect of artificially cutting the incoming CRDM flux at the indicated energies. Right panel. Updated CRDM limits (coinciding with the solid lines from the left panel) in comparison to limits from the Lyman-  $\alpha$  forest [100], the Milky Way satellite population [101], gas clouds in the Galactic Centre region [102], the XQC experiment [76, 103], and a recently analysed storage dewar experiment [104, 105]. We also show upper limits on the cross section as published by the CRESST collaboration [6] (solid green lines), based on a surface run of their experiment, along with the maximal cross section where attenuation does not prevent DM from leaving a signal in the detector [16]. Alternative limits are indicated by green dashed [76] and dash-dotted lines [106], based on the assumption of a thermalization efficiency of  $\epsilon_{\mathrm{th}} = 2\%$  and  $\epsilon_{\mathrm{th}} = 1\%$ , respectively, which is significantly worse than the one adopted in the CRESST analysis.

![](images/4c930b2d562faff7c815996afac936078439ec9ff8d087e51b6b4942674091cb.jpg)

constant cross section, which can be viewed as the highly non-relativistic limit of a contact interaction. This will allow us to illustrate how the resulting CRDM constraints compare with established bounds from both surface and astrophysical experiments, as well as provide a more direct comparison with the existing literature.

# 5.1 Constant cross section

For the discussion of a constant cross section, we will again consider the case of spin-independent scattering with isospin conserving nucleon couplings, cf. eq. (3.2). In the left panel of figure 4, we show our improved constraints from a re-interpretation of the Xenon-1T limits in this case. Broadly, these updated and refined CRDM limits cover the mass range up to  $m_{\chi} \lesssim 10 \mathrm{GeV}$  for cross sections  $10^{-31} \mathrm{cm}^2 \lesssim \sigma_{\mathrm{SI}} \lesssim 2 \times 10^{-28} \mathrm{cm}^2$ .

For comparison, we also indicate (with dash-dotted lines) the limits that result when neglecting both form-factor dependence of the cross section and inelastic scatterings in the attenuation part. As expected, this leads to a shape of the excluded region very similar

to that originally derived in ref. [22], where the same simplifying assumptions were made. As a result of our improved treatment of CR fluxes and form factors, however, the limits indicated with dash-dotted lines are overall slightly more stringent than what is reported in that analysis. We find that for very light DM, with  $m_{\chi} \lesssim 10 \mathrm{MeV}$ , this simplistic treatment actually leads to rather realistic limits, the reason being that for highly relativistic particles the typical momentum transfer is always so large that efficient inelastic scattering becomes relevant. For heavier DM masses, on the other hand, this treatment clearly overestimates the stopping power because it neglects the form factor suppression relevant for semi-relativistic DM scattering on nuclei.

Dashed lines furthermore show the effect of adding the form factor suppression during the attenuation in the soil, as done in ref. [63], but still not including inelastic scattering. Clearly, this vastly underestimates the actual attenuation taking place and therefore appears to exclude very large cross sections. In order to gain a better intuitive understanding for the shape and strength of our final limits, finally, we also indicate the effect of neglecting inelastic scattering and instead artificially cutting the CRDM flux (prior to entering the soil) above some given energy. The resulting upper limit on the cross section that can be probed in this fiducial setup strongly suggests that inelastic scattering events very efficiently stop the incident CRDM flux in the overburden as soon as they become relevant compared to elastic scattering events. From figure 4, and well in accordance with the expectations from section 4, this happens at CRDM energies  $T_{\chi} \gtrsim 0.2 \mathrm{GeV}$ .

In the right panel of figure 4 we show our improved constraints from a re-interpretation of the Xenon-1T limits in comparison with complementary limits from direct probes of the DM-nucleon scattering cross section. At small DM masses the dominant constraint results from analysing the distribution of large-scale structures as traced by the Lyman- $\alpha$  forest. This is based on the fact that protons scattering too strongly off DM would accelerate the latter and thereby suppress the matter power spectrum at sub-Mpc scales. Such limits have recently been significantly tightened [100], utilizing state-of-the-art cosmological hydrodynamical simulations of the intergalactic medium at redshifts  $2 \lesssim z \lesssim 6$ . Similar bounds from the CMB (not shown here) are generally weaker by up to three orders of magnitude [100, 107, 108], while the Milky Way satellite population [101] — as inferred from the Dark Energy Survey and PanSTARRS-1 [109] — places bounds that are roughly one order of magnitude weaker. Beyond cosmological bounds, cold gas clouds near the Galactic Center provide an interesting complementary testbed, in particular at high DM masses, where halo DM particles scattering too efficiently on the much colder baryon population would heat up the latter [110]. Here we show updated constraints [102] based on the cloud G357.8-4.7-55, noting that these constraints might be improved by more than one order of magnitude if G1.4-1.8+87 is indeed as cold as  $T \leq 22\mathrm{K}$  (as reported in refs. [111, 112] but disputed in ref. [113]). We also display the limits [76] that result from the ten minutes'

flight of the X-ray Calorimetry Rocket (XQC) [103], based on the observation that ambient DM particles scattering off the silicon nuclei in the quantum calorimeter would deposit (part of) their energy in the process [14, 114, 115]. In deriving these XQC limits, one must take into account that the recoil energy of a silicon nucleus potentially thermalizes much less efficiently in the calorimeter than the  $e^{\pm}$  pairs produced from an incoming X-ray photon, such that a nuclear recoil energy  $T_{N}$  will leave a signal equivalent to a photon with a reduced 'thermal' recoil energy  $T_{T} = \epsilon_{\mathrm{th}} T_{N}$ . Concretely, the limits shown in the plot are based on the very conservative assumption of a thermalization efficiency factor of  $\epsilon_{\mathrm{th}} = 0.02$ .<sup>6</sup>

Furthermore, in order to directly probe sub-GeV DM with very large cross sections, the CRESST collaboration has performed a dedicated surface run of their experiment [6], deliberately avoiding the shielding of the Gran Sasso rock used in the standard run [116]. The result of this search is the exclusion region indicated by the solid green line in figure 4. Here, upper bounds on the cross section correspond to the published limits, obtained under the assumption that any attenuation in the overburden can be neglected. Modelling the effect of attenuation with detailed numerical simulations also results in the exclusion region limited from above [16], coming from the fact that one must have a sufficiently large flux of DM particles at the detector location. In a series of papers, Farrar et al. have claimed that the CRESST thermalization efficiency adopted in the official analysis is too optimistic [76, 105, 106, 117], challenging the general ability of the experiment to probe sub-GeV DM. We indicate the resulting alternatives to the published CRESST limits in the same figure, albeit noting that the underlying assumption of an efficiency as low as  $\epsilon_{\mathrm{th}} \sim 1\%$  is not supported by data or simulations. For example, no indication for such a dramatic loss of efficiency at low energies is observed for neutrons from an AmBe neutron calibration source [118].

To summarise, figure 4 illustrates the fact that the existence of the CRDM component provides an important probe of strongly interacting light DM. In particular, below  $m_{\chi} \lesssim 100 \mathrm{MeV}$ , it restricts parameter space that is otherwise either unconstrained or only testable with cosmological probes (which — at least to some degree — are subject to modelling caveats regarding the Lyman-α forest and the non-linear evolution of density perturbations at small scales; see, e.g., refs. [119, 120]). The CRDM component also leads to highly relevant complementary constraints up to DM masses of a few GeV, especially when noting that these constraints are independent of the thermalization efficiency discussion above.

# 5.2 Scalar mediators

As our first example beyond a constant scattering cross section we consider the case where a new light scalar particle  $\phi$  mediates the interaction between DM and nucleons. We thus

consider the interaction Lagrangian

$$
\mathcal {L} _ {\text {i n t}} = - g _ {\chi} \phi \bar {\chi} \chi - g _ {p} \phi \bar {p} p - g _ {n} \phi \bar {n} n, \tag {5.1}
$$

and assume, for simplicity, isospin conservation ( $g_{p} = g_{n}$ ). At the level of the effective nuclear interaction Lagrangian, the dominant interaction terms with scalar ( $N_0$ ) and fermionic ( $N_{1/2}$ ) nuclei are thus given by<sup>7</sup>

$$
\mathcal {L} _ {\text {i n t}} = - g _ {N} \left(2 m _ {N} N _ {0} N _ {0} + \bar {N} _ {1 / 2} N _ {1 / 2}\right). \tag {5.2}
$$

Here, the dimensionful coupling to scalar nuclei has been normalized such that both terms in the above expression result in the same scattering cross section in the highly non-relativistic limit. In addition, the coupling to individual nucleons is coherently enhanced across the nucleus, resulting in an effective coupling to both scalar and fermionic nuclei given by

$$
g _ {N} ^ {2} = A ^ {2} g _ {p} ^ {2} \times G _ {N} ^ {2} \left(Q ^ {2}\right), \tag {5.3}
$$

where  $G_{N}$  is the same form-factor as in the case of a 'constant' cross section. For the resulting elastic scattering cross section for DM incident on nuclei at rest we find

$$
\frac {d \sigma_ {\chi N}}{d T _ {N}} = \frac {\mathcal {C} ^ {2} \sigma_ {\mathrm {S I}} ^ {\mathrm {N R}}}{T _ {N} ^ {\max }} \frac {m _ {\phi} ^ {4}}{(Q ^ {2} + m _ {\phi} ^ {2}) ^ {2}} \frac {m _ {N} ^ {2} (Q ^ {2} + 4 m _ {\chi} ^ {2})}{4 s \mu_ {\chi N} ^ {2}} \times \left\{ \begin{array}{l l} 1 & \text {f o r s c a l a r N} \\ 1 + \frac {Q ^ {2}}{4 m _ {N} ^ {2}} & \text {f o r f e r m i o n i c N} \end{array} \right\} \times G _ {N} ^ {2} (Q ^ {2}), \tag {5.4}
$$

where  $\mu_{\chi p}$  is the reduced mass of the DM/nucleon system and

$$
\sigma_ {\mathrm {S I}} ^ {\mathrm {N R}} = \frac {g _ {\chi} ^ {2} g _ {p} ^ {2} \mu_ {\chi p} ^ {2}}{\pi m _ {\phi} ^ {4}} \tag {5.5}
$$

is the spin-independent scattering cross section per nucleon in the ultra non-relativistic limit. For reference, the kinematic quantities  $T_N^{\mathrm{max}}$ ,  $s$  and  $Q^2$  are given by eqs. (2.5), (2.6) and (2.8), respectively. For the production part of the process, where CR nuclei collide with DM at rest, one simply has to exchange  $T_N \leftrightarrow T_\chi$  and  $m_{\chi} \leftrightarrow m_{N}$  in these expressions for kinematic variables — but not in the rest of eq. (5.4) — in order to obtain  $d\sigma_{\chi N} / dT_{\chi}$ .

In the left panel of figure 5 we show the resulting CRDM fluxes for this model. For small kinetic energies these fluxes are, as expected, identical to those shown in figure 1 for the case of a constant cross section. This is the regime where  $Q^2 = 2m_{\chi}T_{\chi}$  is smaller than the masses of both the mediator and CR nuclei, such that eq. (5.4) reduces to eq. (3.2). For  $Q^2 \gtrsim m_{\phi}^2$ , on the other hand, the presence of a light mediator clearly suppresses the fluxes. Note that the matrix element also contains a factor of  $(Q^2 + 4m_{\chi}^2)$ , which additionally leads to a flux enhancement for fully relativistic DM particles,  $T_{\chi} \gtrsim 2m_{\chi}$ . In the figure, this latter effect is clearly visible for the case of  $m_{\chi} = 10 \mathrm{MeV}$  and a heavy mediator. In general,

![](images/9aecdf191d7a391a4c5bdc261dc8283e811cd47b57fc6e539d873345d98feb79.jpg)  
Figure 5. Left panel. Solid lines show the CRDM flux before attenuation for a constant interaction cross section, as in figure 1, for DM masses  $m_{\chi} = 10 \mathrm{MeV}$  and  $m_{\chi} = 1 \mathrm{GeV}$ . For comparison we also indicate the corresponding CRDM flux for a scalar mediator, cf. eq. (5.4), with mass  $m_{\phi} = 100 \mathrm{MeV}$  (dash-dotted),  $m_{\phi} = 10 \mathrm{MeV}$  (dashed) and  $m_{\phi} = 1 \mathrm{MeV}$  (dotted), for a cross section (in the non-relativistic limit) of  $\sigma_{\mathrm{SI}}^{\mathrm{NR}} = 10^{-30} \mathrm{cm}^2$ . Right panel. Minimal kinetic energy  $T_{\chi}$  that a DM particle must have, prior to attenuation, in order to trigger a signal in the Xenon-1T experiment. Line styles and colors match those of the left panel. In particular, solid lines show the case of a constant spin-independent scattering cross section and are identical to those displayed in figure 2.

![](images/551755eb89e9b916aeb0ad9c84ca305f94c209bfccaea96d62d22406aec6e849.jpg)

the appearance of such model-dependent features demonstrates the need to use the full matrix element for the relativistic cross section. This is in contrast to the non-relativistic case, where a model-independent rescaling of the cross section by a factor of  $(1 + Q^2 /m_\phi^2)^{-2}$  is usually sufficient to model the effect of a light mediator (see, e.g., refs. [121-123]).

In the right panel of figure 5, we explore the minimal CRDM energy  $T_{\chi}$  that is needed to induce a detectable nuclear recoil. Compared to the situation of a constant scattering cross section (depicted by the solid lines for easy comparison), the attenuation is as expected rather strongly suppressed when light scalar mediators are present (with the exception of the case with  $m_{\chi} = 10 \mathrm{MeV}$  and  $m_{\phi} = 100 \mathrm{MeV}$ , where the cross section is enhanced due to the  $(Q^2 + 4m_{\chi}^2)$  factor in the squared matrix element). In order to understand the qualitative behaviour of  $T_{\chi}^{\mathrm{min}}(z = 0)$  better, we recall from the discussion of figure 2 that there are two generic scaling regimes for solutions of the energy loss equation. Firstly, for cross sections with no or only a mild dependence on the momentum transfer,  $T_{\chi}^{\mathrm{min}}(z = 0)$  grows exponentially with increasing  $\sigma_{\mathrm{SI}}^{\mathrm{NR}}$ . Secondly, in the presence of an effective cutoff in the cross section (like when form factors or light mediators are introduced),  $T_{\chi}^{\mathrm{min}}(z = 0) \propto \sqrt{\sigma_{\mathrm{SI}}^{\mathrm{NR}}}$  for large energies  $T_{\chi}$ . These different regimes are clearly visible in the figure. For the green dot-dashed curve ( $m_{\chi} = 1 \mathrm{GeV}$ ,  $m_{\phi} = 100 \mathrm{MeV}$ ), for example, one observes as expected an initial steep rise at the smallest DM energies — until the form factor and mediator suppression of the cross section cause a scaling with  $\sqrt{\sigma_{\mathrm{SI}}^{\mathrm{NR}}}$  for kinetic energies above a few MeV. At roughly  $T_{\chi} \gtrsim 0.1 \mathrm{GeV}$ , inelastic scattering kicks in,

leading again to an exponential suppression of the flux. For even higher energies, finally, the scattering cross section falls off so rapidly that the required initial DM energy once again only grows as  $\sqrt{\sigma_{\mathrm{SI}}^{\mathrm{NR}}}$ .

Turning our attention to the resulting CRDM limits, it is worth stressing here that  $\sigma_{\mathrm{SI}}^{\mathrm{NR}}$  as introduced in eq. (5.5), is a somewhat artificial object that only describes the cross section for physical processes restricted to  $Q^{2} \lesssim m_{\phi}^{2}$ . In a direct detection experiment like Xenon-1T this is necessarily violated for  $m_{\phi} \lesssim \sqrt{2m_{N}T_{N}^{\mathrm{thr}}} \sim 35\mathrm{MeV}$ , given that  $T_{N}^{\mathrm{thr}} = 4.9\mathrm{keV}$  is the minimal recoil energy needed to generate a signal. A natural consequence of this is that making a straight-forward comparison to the  $\sigma_{\mathrm{SI}}$  appearing in the 'constant cross section' case discussed in section 5.1 is challenging. Instead, the best we can achieve in terms of a meaningful comparison is to define a reference cross section

$$
\tilde {\sigma} _ {\mathrm {X e , S I}} ^ {p} \equiv \sigma_ {\mathrm {S I}} ^ {\mathrm {N R}} \times \frac {m _ {\phi} ^ {4}}{\left(Q _ {\mathrm {X e , r e f}} ^ {2} + m _ {\phi} ^ {2}\right) ^ {2}} \frac {Q _ {\mathrm {X e , r e f}} ^ {2} + 4 m _ {\chi} ^ {2}}{4 m _ {\chi} ^ {2}}, \tag {5.6}
$$

where  $Q_{\mathrm{Xe,ref}} \sim 35 \mathrm{MeV}$ . It follows from eq. (5.4) and eq. (3.2), and the fact that  $s \approx (m_{\chi} + m_N)^2$  for the energies of interest here, that  $\tilde{\sigma}_{\mathrm{Xe,SI}}^p$  should be interpreted as the effective CRDM cross section per nucleon that is dominantly seen in the Xenon-1T analysis window. It is thus this quantity, not the  $\sigma_{\mathrm{SI}}^{\mathrm{NR}}$  from eq. (5.5), that should be compared to the published Xenon-1T limits on the DM-nucleon cross section.

This also allows us to address the question of how the limits on the DM-nucleon coupling coming from the CRDM component compare to the complementary constraints introduced in section 5.1 (cf. the right panel of figure 4). In order to do so, one first needs to realize that all of those limits are derived under the assumption of non-relativistic DM and a constant cross section. In reality, however, they probe very different physical environments and typical momentum transfers. In order to allow for a direct comparison, therefore, they also need to be re-scaled to a common reference cross section. Assuming that the DM energies in eq. (5.4) are non-relativistic, a reported limit on the DM-nucleon cross section  $\sigma_{\mathrm{SI}}^p$  from an experiment probing typical momentum transfers of the order  $Q_{\mathrm{ref}}^2$  would correspond to a cross section of

$$
\tilde {\sigma} _ {\mathrm {X e , S I}} ^ {p} = \sigma_ {\mathrm {S I}} ^ {p} \times \left(\frac {Q _ {\mathrm {r e f}} ^ {2} + m _ {\phi} ^ {2}}{Q _ {\mathrm {X e , r e f}} ^ {2} + m _ {\phi} ^ {2}}\right) ^ {2} \frac {Q _ {\mathrm {X e , r e f}} ^ {2} + 4 m _ {\chi} ^ {2}}{Q _ {\mathrm {r e f}} ^ {2} + 4 m _ {\chi} ^ {2}} \tag {5.7}
$$

in the Xenon-1T detector. As an example, consider the CRESST surface run [6], where a threshold energy of  $\sim 20\mathrm{eV}$  for the sapphire detector would imply  $Q_{\mathrm{ref}}^2 \sim (0.98\mathrm{MeV})^2 / \epsilon_{\mathrm{th}}$ . Similarly, a thermal recoil energy of  $29\mathrm{eV}$  in XQC corresponds to  $Q_{\mathrm{ref}}^2 \sim (8.7\mathrm{MeV})^2$  for the nuclear recoil on Si nuclei (assuming  $\epsilon_{\mathrm{th}} = 0.02$  as for the unscaled limits). Turning to cosmological limits, a baryon velocity of  $v_b^{\mathrm{rms}} \sim 33\mathrm{km/s}$  at the times relevant for the emission of Lyman- $\alpha$  photons [124] implies typical momentum transfers from the Helium nuclei to DM of  $Q_{\mathrm{ref}}^2 \sim 4\mu_{\chi\mathrm{He}}^2 \times 10^{-8}$ . This means that, for the range of DM and mediator masses considered here, the cross section at these times becomes roughly constant and we can approximate  $Q_{\mathrm{ref}}^2 \approx 0$  in eq. (5.7). The same goes for the constraints stemming from the MW satellite abundance, which are sensitive to even lower redshifts and thus smaller momentum transfers [101, 125].

In figure 6 we show a subset of these correspondingly rescaled constraints $^{8}$  — for mediator masses  $m_{\phi} = 1 \mathrm{MeV}$ ,  $10 \mathrm{MeV}$ ,  $100 \mathrm{MeV}$  and  $1 \mathrm{GeV}$  — along with the full CRDM constraints derived here. We also indicate, for comparison, with dotted black lines where non-perturbative couplings would be needed in this model to realize the stated cross section. This line is only visible for the case of  $m_{\phi} = 1 \mathrm{GeV}$ , which demonstrates that it is generically challenging to realize large cross sections without invoking light mediators. The presence of an abundant species with a mass below a few MeV, furthermore, would affect how light elements are produced during big bang nucleosynthesis (BBN). For a  $1 \mathrm{MeV}$  particle with one degree of freedom, like  $\phi$ , this can be formulated as a constraint of  $\tau > 0.43$  s [130] on the lifetime of such a particle. Physically, this constraint derives from freeze-in production of  $\phi$  via the inverse decay process. Since  $\phi \rightarrow \gamma \gamma$  (apart from  $\phi \rightarrow \bar{\nu} \nu$ ) is the only kinematically possible SM decay channel, the translation of this bound to a constraint on the SM coupling  $g_{p}$  is somewhat model-dependent. For concreteness we consider the Higgs portal model, where  $\tau > 1$  s at  $m_{\phi} = 1 \mathrm{MeV}$  corresponds to a squared mixing angle  $\sin^2 \theta = (8.62 \times 10^2 g_p)^2 > 3.8 \times 10^{-4}$  [131]. The area above the dashed line in the top left panel of figure 6 requires either a larger value of  $g_{p}$  than what is given by this bound, or a non-perturbative coupling  $g_{\chi}^2 > 4\pi$ . This confirms the generic expectation that for very light particles BBN constraints are more stringent than those stemming from the CRDM component [46, 132].

Our results demonstrate that in the presence of light mediators the largest DM mass that can be constrained due to CR upscattering is reduced from about  $10\mathrm{GeV}$ , cf. figure 4, to just above  $1\mathrm{GeV}$  (for  $m_{\phi} \sim 1\mathrm{MeV}$ ). This is a direct consequence of the suppressed CRDM production rate discussed above. On the other hand, the reduction of the cross section also implies a smaller attenuation effect, thus closing parameter space at larger cross sections. More importantly, complementary constraints from cosmology and dedicated surface experiments become more stringent in the presence of light mediators, once they are translated to a common reference cross section. To put this in context, let us first recall that in the constant cross section case, figure 4 tells us that cross sections  $\sigma_{\mathrm{SI}} \gtrsim 2 \cdot 10^{-31}\mathrm{cm}^2$  are safely excluded across the entire DM mass range (or  $\sigma_{\mathrm{SI}} \gtrsim 6 \cdot 10^{-31}\mathrm{cm}^2$  when assuming that the thermalization efficiency of CRESST is indeed as low as  $2\%$ ). From figure 6 we infer that these limits can be somewhat weakened for sub-GeV DM, when considering light mediators in the mass range  $10\mathrm{MeV} \lesssim m_{\phi} \lesssim 100\mathrm{MeV}$  (as we will see further down, the situation of a vector mediator is not appreciably different from that of the scalar mediator shown here). Concretely, the upper bound on the cross section now becomes  $\tilde{\sigma}_{\mathrm{SI}} \lesssim 3 \cdot 10^{-31}\mathrm{cm}^2$ ,

<sup>8</sup>Upper bounds on the excluded cross section, due to attenuation effects, cannot simply be rescaled as in eq. (5.7). For the sake of figure 6, we instead adopt a rather simplistic approach [16, 126-128] to estimate these limits by requiring that the most energetic halo DM particles, with an assumed velocity  $v_{\mathrm{max}}$ , can trigger nuclear recoils above the CRESST threshold of  $19.7\mathrm{eV} / \epsilon_{\mathrm{th}}$  after attenuation in the Earth's atmosphere. For the average density and distribution of elements in the atmosphere, we follow ref. [129]. By treating  $v_{\mathrm{max}}$  and the effective height of the atmosphere,  $h_a$ , as free parameters, we can then rather accurately fit the results of more detailed calculations [16, 76] for the case of a constant cross section — with numerical values in reasonable agreement with the physical expectation in such a heuristic approach. Finally, we adopt those values of  $v_{\mathrm{max}}$  and  $h_a$  to derive the corresponding limits for the case of a scalar mediator, as displayed in figure 6.

![](images/83b30d3d33ade8bbd310ca8aa5aafc2cab0bda13c34f1374abd6f7a82045317a.jpg)

![](images/27e329510555e84265c8094c5c27de93a87e11b77d9cd1dca5259e9a63e4492d.jpg)

![](images/4e5200c9613faea7afa0691e2492a933651c636910822bf9476a522e4075482c.jpg)  
Figure 6. Limits on the DM-nucleon scattering cross section evaluated at a reference momentum transfer of  $Q_{\mathrm{Xe,ref}} = 35 \mathrm{MeV}$ , as a function of the DM mass  $m_{\chi}$ . From top left to bottom right, the panels show the case of a scalar mediator with mass  $m_{\phi} = 1 \mathrm{MeV}$ ,  $10 \mathrm{MeV}$ ,  $100 \mathrm{MeV}$  and  $1 \mathrm{GeV}$ . Solid purple lines show the updated CRDM limits studied in this work. We further show limits from the Lyman-  $\alpha$  forest [100], the XQC experiment [76, 103], the CRESST surface run [6, 16] and an alternative analysis of the CRESST limits [76]. All these limits are rescaled to match the situation of a light mediator, as explained in the text. The parameter region above the dotted black line in the bottom right panel requires non-perturbative couplings, while the area above the dotted line in the top left panel is excluded by BBN.

![](images/eca6462d5187bb7ee863aa3a73d1d4a3b4813567877e4c672374595e3cc34dcb.jpg)

independently of the DM and mediator mass. For a  $2\%$  thermalization efficiency of CRESST [76] and a narrow range of mediator masses,  $10\mathrm{MeV}\lesssim m_{\phi}\ll 100\mathrm{MeV}$ , a small window opens up above the maximal cross section that can be probed with CRESST. The reason is the gap between Lyman-  $\alpha$  bounds and the weakened CRESST limits from ref. [76] that is visible in the figure, for  $m_{\phi}\gtrsim 10\mathrm{MeV}$ , and which is closed by the CRDM limits only for mediator masses of  $m_{\phi}\gtrsim 30\mathrm{MeV}$ . Nominally, for  $m_{\chi}\sim 2\mathrm{GeV}$  and  $m_{\phi}\sim 30\mathrm{MeV}$ , this would allow for cross sections as large as  $\tilde{\sigma}_{\mathrm{SI}}\sim 4\cdot 10^{-29}\mathrm{cm}^2$ . In either case, the conclusion remains that CRDM leads to highly complementary limits, and that this relativistic component of the DM flux is in fact crucial for excluding the possibility of very large DM-nucleon interactions.

# 5.3 Vector mediators

We next consider the general case of a massive vector mediator  $V$ , with interactions given by

$$
\mathcal {L} = V _ {\mu} \left(g _ {\chi} \overline {{\chi}} \gamma^ {\mu} \chi + g _ {p} \overline {{p}} \gamma^ {\mu} p + g _ {n} \overline {{n}} \gamma^ {\mu} n\right). \tag {5.8}
$$

We will again assume  $g_{n} = g_{p}$  for simplicity, noting that smaller values of the ratio  $g_{n} / g_{p}$  can lead to significantly smaller cross sections (see, e.g., refs. [123, 133]); in our context this would mostly imply that the attenuation in the overburden becomes less relevant, leading to more stringent constraints. In analogy to eq. (5.2), this implies the following dominant interaction terms with scalar and fermionic nuclei, respectively:

$$
\mathcal {L} _ {\mathrm {i n t}} = - g _ {N} V _ {\mu} \left(i N _ {0} ^ {*} \stackrel {\leftrightarrow} {\partial^ {\mu}} N _ {0} + \overline {{N}} _ {1 / 2} \gamma^ {\mu} N _ {1 / 2}\right), \tag {5.9}
$$

where the effective mediator coupling to nuclei,  $g_{N}$ , is again given by the coherent enhancement stated in eq. (5.3). For the elastic scattering cross section on nuclei we find

$$
\begin{array}{l} \frac {d \sigma_ {\chi N}}{d T _ {N}} = \frac {\mathcal {C} ^ {2} \sigma_ {\mathrm {S I}} ^ {\mathrm {N R}}}{T _ {N} ^ {\operatorname* {m a x}}} \frac {m _ {A} ^ {4}}{(Q ^ {2} + m _ {A} ^ {2}) ^ {2}} \times G _ {N} ^ {2} (Q ^ {2}) \tag {5.10} \\ \times \frac {1}{4 s \mu_ {\chi N} ^ {2}} \left\{ \begin{array}{l l} m _ {\chi} ^ {2} Q ^ {2} - Q ^ {2} s + (s - m _ {N} ^ {2} - m _ {\chi} ^ {2}) ^ {2} & \mathrm {f o r s c a l a r} N \\ \frac {1}{2} Q ^ {4} - Q ^ {2} s + (s - m _ {N} ^ {2} - m _ {\chi} ^ {2}) ^ {2} & \mathrm {f o r f e r m i o n i c} N \end{array} \right.. \\ \end{array}
$$

Here, the cross section in the ultra-nonrelativistic limit,

$$
\sigma_ {\mathrm {S I}} ^ {\mathrm {N R}} = \frac {g _ {\chi} ^ {2} g _ {p} ^ {2} \mu_ {\chi p} ^ {2}}{\pi m _ {A} ^ {4}}, \tag {5.11}
$$

i.e. for  $Q^2 \to 0$  and  $s \to (m_N + m_\chi)^2$ , agrees exactly with the result obtained for the scalar case, as expected. For large energies and momentum transfers, on the other hand, the behaviour is different.

The resulting CRDM fluxes are nonetheless so similar to the scalar case shown in the left panel of figure 5 that we refrain from plotting them separately. Differences do exist, however, for the stopping power in the overburden. In the left panel of figure 7 we therefore show the minimal initial kinetic energy needed by a CRDM particle to induce detectable nuclear recoils in Xenon-1T. Compared to the scalar case, cf. the right panel of figure 5, the attenuation is more efficient for highly relativistic DM particles due to the

![](images/335df3197e6c02fa52211f52ca72afb19aad857b0d34068a4ffe451d07ae4bd1.jpg)  
Figure 7. Left panel. Minimal kinetic energy  $T_{\chi}$  that a DM particle must have, prior to attenuation, in order to trigger a signal in the Xenon-1T experiment for DM nucleus interactions via a vector mediator, as a function of the spin-independent DM-nucleon scattering cross section in the highly non-relativistic limit,  $\sigma_{\mathrm{SI}}^{\mathrm{NR}}$ . Yellow (green) lines indicate a DM mass  $m_{\chi} = 10 \mathrm{MeV}$  ( $m_{\chi} = 1 \mathrm{GeV}$ ), and different line styles correspond to mediator masses  $m_{A} = 1, 10, 100 \mathrm{MeV}$  as indicated. Solid lines show the case of a constant spin-independent scattering cross section and are identical to those displayed in figure 2. Right panel. Constraints on  $\sigma_{\mathrm{SI}}^{\mathrm{NR}}$  as a function of the DM mass  $m_{\chi}$ . Solid purple lines refer to the case of a constant cross section, as in figure 4, while other line styles show the case where the interaction is mediated by a light scalar (red) or vector (green) particle with mass  $m_{\mathrm{med}} = 10 \mathrm{MeV}$  and  $1 \mathrm{GeV}$ , respectively.

![](images/1865874aa6cb9d0aa42fda13fa6b199b3ceef421b12e1dd1cf90514df628b569.jpg)

$s$ -dependence of the terms in the second line of eq. (5.10). As before, the effect of these model-dependent terms from the scattering amplitude is most visible for highly relativistic particles, with small  $m_{\chi}$ , and large mediator masses, where the suppression due to the factor  $(1 + Q^{2} / m_{A}^{2})^{-2}$  is less significant.

In the right panel of figure 7 we compare the final exclusion regions for the situations considered so far, i.e. for a contact interaction, scalar mediators and vector mediators, respectively. For the sake of comparison in one single figure, we plot here the cross section in the ultra-nonrelativistic limit. For an interpretation of these limits in comparison to complementary constraints on DM-nucleon interactions we thus refer to the discussion of figure 6, noting that the rescaling prescriptions for vector and scalar mediators are qualitatively the same. The first thing to take away from figure 7 is that, as expected, the exclusion regions for heavy mediators resemble those obtained for the constant cross section case. The figure further demonstrates that the only significant difference between scalar and vector mediators appears at smaller mediator masses, where the former are somewhat less efficiently stopped in the overburden. It is worth noting, however, that this region of parameter space where the vector and scalar cases differ substantially is nonetheless excluded by Lyman-  $\alpha$  bounds. The general discussion and conclusions from the scalar mediator case explored in the previous subsection thus also applies to interactions mediated by vector particles.

# 5.4 Finite-size dark matter

As a final generic example of a  $Q^2$ -suppressed cross section let us consider the situation where the DM particle itself has a finite size that is larger than its Compton wavelength. Various models of such composite DM have been extensively studied in the literature [134-141]. In fact, ref. [142] even suggests that DM with masses above 1 GeV cannot be point-like for DM-nucleon cross section  $\gtrsim 10^{-25}\mathrm{cm}^2$ . The corresponding scattering cross section then takes the same form as in the point-like case, multiplied by another factor  $|G_{\chi}(Q^{2})|^{2}$  that reflects the spatial extent of  $\chi$  [143-145]. Specifically, just as for nuclear form factors, we have

$$
G _ {\chi} \left(Q ^ {2}\right) = \int d ^ {3} x e ^ {i \mathbf {q} \cdot \mathbf {x}} \rho_ {\chi} (\mathbf {x}), \tag {5.12}
$$

where  $\rho_{\chi}(\mathbf{x})$  is the distribution of the effective charge density that the interaction couples to. For simplicity we will choose a dipole form factor of the form

$$
G _ {\chi} \left(Q ^ {2}\right) = \left(1 + \frac {r _ {\chi} ^ {2}}{1 2} Q ^ {2}\right) ^ {- 2}, \tag {5.13}
$$

with  $r_{\chi}$  being the r.m.s. radius of the DM particle,  $r_{\chi}^{2} = \int d^{3}x\mathbf{x}^{2}\rho_{\chi}(\mathbf{x})$ . We then multiply  $G_{\chi}^{2}(Q^{2})$  with eq. (3.2) in order to obtain  $d\sigma_{\chi N} / dT_N$ , thus describing an effective scalar interaction with the usual coherent enhancement inside the nucleus — but where each of the nucleons only 'sees' some fraction of the entire DM particle.

In a very similar fashion to what happens in the presence of a light mediator  $\phi$ , such a cross section features a sharp suppression for momentum transfers exceeding a 'mass' scale  $m_{\phi} \sim \sqrt{12}/r_{\chi}$ . Sharper than in that case, in fact, as the suppression scales with a power of  $Q^{-8}$  rather than just  $Q^{-4}$ . This is clearly visible in the left panel of figure 8, where we plot the expected CRDM flux for DM with a finite size, for various values of  $m_{\chi}$  and  $r_{\chi}$ . For example, for  $r_{\chi} = 10\mathrm{fm}$ , we have  $\sqrt{12}/r_{\chi} \sim 68\mathrm{MeV}$  and the cutoff indeed appears at only slightly smaller values of  $T_{\chi}$  than in the case of the  $100\mathrm{MeV}$  mediator displayed in figure 5 (for  $m_{\chi} = 1\mathrm{GeV}$ ). The slope above the cutoff, however, is twice as steep — as expected from the  $Q^{-8}$  suppression.

In the right panel of figure 8 we show how the constraints on a constant DM-nucleon cross section weaken when considering the situation where the DM particles themselves have a finite extent. Concretely, for a DM radius of  $r_{\chi} = 1$  fm ( $r_{\chi} = 10$  fm) the maximal DM mass that can be probed decreases from  $\sim 10$  GeV to about  $4.5$  GeV (1.1 GeV). The reduced CRDM flux for extended DM, cf. the left panel of the figure, also visibly weakens the lower bound on the exclusion region. At the same time, attenuation is also less efficient for a given cross section in the non-relativistic limit (inelastic scattering still effectively cuts off the incoming CRDM flux above  $\sim 0.2$  GeV, explaining e.g. the upper, almost horizontal boundary of the exclusion region in the  $r_{\chi} = 10$  fm case). For  $r_{\chi} \gtrsim 1$  fm, this starts to significantly enlarge the excluded region to higher cross sections. On the other hand, it

![](images/51c5dcc8ff2662957f1cc228add5ec18eb77ccbe47b44b2ba6aaf6adaa746a41.jpg)  
Figure 8. Left panel. Solid lines show the CRDM flux before attenuation for a constant interaction cross section, as in figure 1, for DM masses  $m_{\chi} = 10 \mathrm{MeV}$  and  $m_{\chi} = 1 \mathrm{GeV}$ . For comparison we indicate the corresponding CRDM flux for finite size DM, with  $r_{\chi} = 1 \mathrm{fm}$  (dotted) and  $r_{\chi} = 10 \mathrm{fm}$  (dashed), for a cross section of  $\sigma_{\mathrm{SI}}^{\mathrm{NR}} = 10^{-30} \mathrm{cm}^2$ . Right panel. Limits on the spin-independent DM-nucleon cross section, with line styles and colors matching those of the left panel. In particular, solid lines show the case of a constant scattering cross section and are identical to those displayed in the left panel of figure 4.

![](images/375c58d5cb27130d18cfec9101d432006f480c85aacc367f6749f2fcdaf4430a.jpg)

should be noted that for composite DM particles the interaction cross section may not actually continue to drop as  $Q^{-8}$  for very large momentum transfers, as would be implied by eq. (5.13). At some point, instead, inelastic scattering events on the DM constituents will take over, in analogy to what we discussed for nuclei in section 4. This is particularly relevant if the DM constituents are themselves finite in size, in which case the upper boundaries of the exclusion regions shown in figure 8 would be overly optimistic for very large  $r_{\chi}$ .

Similar to the discussion in section 5.2, a comparison of the limits shown in figure 8 with complementary limits requires a re-scaling of  $\sigma_{\mathrm{SI}}$  to a common reference cross section. Due to the strong form factor suppression, this rescaling has an even larger effect than in the light mediator case; concretely, instead of eq. (5.7), the rescaling of reported limits,  $\sigma_{\mathrm{SI}}^p$ , to those relevant for the Xenon-1T detector now takes the form

$$
\tilde {\sigma} _ {\mathrm {X e , S I}} ^ {p} = \sigma_ {\mathrm {S I}} ^ {p} \times \left(\frac {Q _ {\mathrm {r e f}} ^ {2} + 1 2 / r _ {\chi} ^ {2}}{Q _ {\mathrm {X e , r e f}} ^ {2} + 1 2 / r _ {\chi} ^ {2}}\right) ^ {4}. \tag {5.14}
$$

Qualitatively, however, this does not change the lesson learned in the light mediator case: while limits from the CRDM component can be weakened by increasing  $r_{\chi}$ , this will inevitably strengthen complementary bounds from cosmology. As a result, we find once again an absolute upper bound on the cross section of about  $\tilde{\sigma}_{\mathrm{SI}} \sim 3 \cdot 10^{-31} \mathrm{~cm}^2$ , independently of the DM mass and size. Also in this case there is a small loophole to this statement if one is willing to assume that the thermalization efficiency of CRESST is as small as  $2\%$ : when tuning the size of the DM particles to  $r_{\chi} \simeq 10 \mathrm{fm}$ , we find that cross

sections two orders of magnitude larger may in that case be viable for DM masses in a narrow range between around 1 GeV and 2 GeV.

# 6 Hexaquarks: a viable baryonic dark matter candidate?

In section 5 we discussed various generic situations where the amplitude for elastic scattering shows a significant dependence on the momentum transfer, and how this impacts the conclusions about whether a window of large scattering cross sections remains open or not. In this section we complement those more model-independent considerations by taking a closer look at a specific DM candidate in the GeV range, with relatively large nuclear interactions. Concretely, it has been conjectured that a neutral (color-flavor-spin-singlet) bound state of six light quarks  $uuddss$  may exist, and provide a plausible DM candidate that would evade all current constraints despite its baryonic nature [14, 146-149]. In particular, this sexaquark  $S$  (to be distinguished from a generic 6-quark state, often referred to as hexaquark) would form early enough to behave like standard cold DM during both big bang nucleosynthesis and recombination. It would thus not be in conflict with the independent, and rather precise, measurements [150, 151] of the cosmological baryon density during these epochs.

Compared to the H-dibaryon that was suggested earlier [152] and thoroughly studied both theoretically and experimentally (see refs. [153, 154] for reviews), furthermore, the  $S$  should be much more tightly bound, leading to weaker interactions with ordinary baryons and thus evading direct searches. Such a particle would be absolutely stable for  $m_S < m_D + m_e \simeq 1.88\mathrm{GeV}$ , and decay with a lifetime exceeding the age of the Universe for  $m_S \lesssim 2\mathrm{GeV}$  [148]. Determining its expected mass exactly, however, is challenging; lattice simulations, for example, remain somewhat inconclusive (see, e.g., refs. [155-158] where the results for binding energies of the H-dibaryon state range from  $\sim 17\mathrm{MeV}$  to  $\sim 75\mathrm{MeV}$  relying, however, on unrealistically large quark masses). Even if the sexaquark is stable on cosmological timescales, its relic abundance would generally be much smaller than the observed DM abundance if one assumes that its interactions in the early universe are of the order of the strong force [159, 160]. If instead, one postulates much weaker interactions due to the assumed compactness of the sexaquark, thermal equilibrium with the SM heat bath would not be possible to maintain after the QCD phase transition and the correct DM abundance might be achieved — in a region of parameter space claimed to evade all existing constraints [148].

Motivated by this intriguing possibility, for simplicity we will adopt the description of sexaquark interactions from ref. [148], i.e. we model the interaction with nucleons by the exchange of a vector meson. In particular, the relevant interaction terms with the flavour-neutral mixture of  $\phi$  and  $\omega$ , denoted by  $V$ , are given by

$$
\mathcal {L} = V _ {\mu} \left(i g _ {S} S ^ {\dagger} \stackrel {\leftrightarrow} {\partial^ {\mu}} S + g _ {p} \bar {p} \gamma^ {\mu} p + g _ {n} \bar {n} \gamma^ {\mu} n\right), \tag {6.1}
$$

and we adopt the value  $m_V = 1$  GeV used in ref. [148] for our calculations. The value of  $g_{n} = g_{p}\sim 2.6\sqrt{4\pi}$  can be inferred from the literature on the one-boson-exchange model [161]

although  $\mathcal{O}(1)$  uncertainties can be expected here. $^{10}$  The coupling  $g_{S}$  is largely unknown, though simple scaling arguments suggest that

$$
\alpha_ {\mathrm {S N}} \equiv \frac {g _ {S} g _ {p}}{4 \pi} \tag {6.2}
$$

is very roughly of the order of  $\sim 0.1$  [148]. Following that reference, we will treat  $\alpha_{\mathrm{SN}}$  as a free parameter that we will generously vary in the interval  $(10^{-3},10)$ . Importantly however at least in this parameter range — the DM relic abundance is independent of  $\alpha_{\mathrm{SN}}$ . Instead, the final abundance of  $S$  is set by an independent coupling constant  $\tilde{g}$  [148] that describes the (much weaker) sexaquark-breaking interactions within the effective description. This coupling does not directly enter the analysis presented here.

We treat the interaction of  $V$  with nuclei similarly to that in section 5.3, i.e. we describe it by the effective Lagrangian (5.9) with the coherently enhanced, effective coupling  $g_{N}$  given by eq. (5.3). For the elastic scattering cross section on nuclei we thus find

$$
\begin{array}{l} \frac {d \sigma_ {S N}}{d T _ {N}} = \frac {\mathcal {C} ^ {2} \sigma_ {\mathrm {S I}} ^ {\mathrm {N R}}}{T _ {N} ^ {\operatorname* {m a x}}} \frac {m _ {V} ^ {4}}{(Q ^ {2} + m _ {V} ^ {2}) ^ {2}} \times G _ {N} ^ {2} (Q ^ {2}) G _ {V} ^ {2} (Q ^ {2}) \tag {6.3} \\ \times \frac {1}{4 s \mu_ {S N} ^ {2}} \left\{ \begin{array}{l l} \left(s - \frac {1}{2} Q ^ {2} - m _ {N} ^ {2} - m _ {\chi} ^ {2}\right) ^ {2} & \mathrm {f o r s c a l a r} N \\ m _ {N} ^ {2} Q ^ {2} - Q ^ {2} s + (s - m _ {N} ^ {2} - m _ {S} ^ {2}) ^ {2} & \mathrm {f o r f e r m i o n i c} N \end{array} \right.. \\ \end{array}
$$

Here,

$$
\sigma_ {\mathrm {S I}} ^ {\mathrm {N R}} = \frac {1 6 \pi \alpha_ {\mathrm {S N}} ^ {2} \mu_ {S p} ^ {2}}{m _ {V} ^ {4}} \tag {6.4}
$$

is the scattering cross section on nucleons in the non-relativistic limit and  $\mu_{Sp}(\mu_{SN})$  is the reduced mass of the sexaquark-nucleon (nucleus) system.

Compared to the treatment in section 5.3, we introduce an additional form factor  $G_V$  related to the cutoff in the one-boson-exchange models. In this context, exponential cutoffs

$$
G _ {V} (Q ^ {2}) = e ^ {- \frac {Q ^ {2}}{\Lambda_ {V} ^ {2}}} \tag {6.5}
$$

are mostly used and the cutoff mass  $\Lambda_V$  is fitted to data (and can in principle differ for different meson exchange channels). For example, within the fit to data taking into account hyperon-nucleon interactions [161], these cutoff masses were found to range between  $820\mathrm{MeV}$  and  $1270\mathrm{MeV}$ . Since yet lower cutoff masses appear in related literature (e.g., down to  $590\mathrm{MeV}$  in [164]), we generously vary  $\Lambda_V$  between 500 and  $1500\mathrm{MeV}$ . We note that for  $\Lambda_V \gtrsim 1500\mathrm{MeV}$ , CRDM limits become in fact independent of the cutoff scale.

In figure 9 we show the parameter space in the  $\alpha_{\mathrm{SN}}$  vs.  $m_S$  plane where sexaquark DM is excluded because of the irreducible CRDM component. For a better direct comparison, we also indicate the preferred mass range according to ref. [148], along with the complementary limits presented in that analysis. From this figure, it is clear that our new limits close a

![](images/c3f5a5600fcb2f5d3f841b489f6c9bdc33a7da6b0861f3a98e6ce3722ada7aab.jpg)  
Figure 9. Effective sexaquark coupling  $\alpha_{\mathrm{SN}}$  vs. sexaquark mass  $m_S$ . The purple region shows the parameter range that is excluded by the analysis in this work, assuming that sexquarks make up all of the cosmologically observed DM; different line styles correspond, as indicated, to cutoff masses  $\Lambda_V / \mathrm{GeV} \in \{0.5,1,1.5\}$  in the one-boson exchange approximation. All other constraints are, for easier comparison, directly reproduced from figure 10 of ref. [148], conservatively assuming an attractive Yukawa force between  $S$  and nuclei. The thin vertical stripe corresponds to the mass range where, according to that analysis, the sexaquark would be a viable DM candidate without being in conflict with other particle physics observation, in particular the stability of deuterons based on SNO data [165]. The upper end of that mass range may increase from  $1890\mathrm{MeV}$  to up to  $2054\mathrm{MeV}$  if sexaquark DM does not accumulate in the Earth at the level claimed in ref. [166].

significant part of the viable parameter region where sexaquarks could be the dominant DM component — even without taking into account the CRESST results. In particular, we note that the Lyman-  $\alpha$  limits [100] shown in figures 4 and 6 were presented subsequent to the analysis of ref. [148] and are significantly stronger than the CMB limits indicated in figure 9. The apparently open window at  $\alpha_{\mathrm{SN}} \sim 0.3$  is thus also robustly excluded. On the other hand, a small open window remains for  $\alpha_{\mathrm{SN}} \lesssim 4 \cdot 10^{-3}$ . While not being in conflict with the DM abundance, as explained above, we recall that such values of  $\alpha_{\mathrm{SN}}$  are somewhat smaller than intrinsically expected.

Let us, finally, briefly comment on the fact that the DM-nucleon scattering cross section can, strictly speaking, only be calculated perturbatively in the Born limit,  $\alpha_{\mathrm{SN}}\mu_{\chi N}\lesssim m_V$ . Outside this regime, non-relativistic scattering in a Yukawa potential exhibits parametric resonances where the scattering amplitude is significantly enhanced or suppressed. This non-perturbative effect is well-known from the self-scattering of cold DM in the presence of

light mediators [167], and it is the origin of the resonant structure in the complementary limits from ref. [148] that is visible in figure 9. For our CRDM limits, on the other hand, this additional complication does not arise because such non-perturbative corrections are largely irrelevant for relativistic scattering; in fact, already for the typical velocities during the freeze-out process of thermally produced DM,  $v_{\chi} \sim 0.3$ , the impact is strongly suppressed [167]. The CRDM limits are thus also robust w.r.t. underlying model assumptions such as whether the force mediated by the Yukawa potential is attractive or repulsive.

# 7 Summary and conclusions

For sizeable elastic scattering rates between DM and nuclei there is an irreducible relativistic component of the flux of DM particles arriving at Earth. This extends the sensitivity of conventional direct detection experiments both to sub-GeV masses and to scattering cross sections above the limit set by a too efficient attenuation of the DM flux on the way to the detector. While such large scattering cross sections are also constrained by complementary probes from astrophysics and cosmology, it has repeatedly been pointed out that there might be an open window of relatively strongly interacting DM with a mass in the ballpark of  $\sim 1$  GeV.

We find that the CRDM component in the DM flux generically closes this window, under rather minimal assumptions. In order to arrive at this conclusion, we included in our analysis a detailed treatment of the inelastic scattering of DM off nuclei (section 4). We demonstrate that this provides an important additional stopping channel for CRDM particles on their way to direct detection facilities — unlike for non-relativistic DM, where only elastic scattering is relevant. We also investigated the extent to which a possible energy or momentum-transfer dependence of the cross section could weaken our general conclusions. For this purpose, we considered  $i)$  a class of simplified models where the scattering with nuclei is mediated by a light scalar (section 5.2) or vector (section 5.3) particle, as well as  $ii)$  situations where DM particles cannot be described as being point-like (section 5.4). In all these cases, the additional momentum-transfer dependence indeed weakens the limits from direct detection — which however is compensated for by a corresponding strengthening of complementary limits, in particular from cosmology. In combination, these limits stringently constrain the possibility of cross sections larger than a few times  $10^{-31} \mathrm{~cm}^2$ , over a wide range of DM masses. Interestingly, this is largely independent of underlying modelling assumptions such as the mass of new mediator particles or the DM particles' radius.

Finally, an exotic QCD bound state that is produced well before BBN, has repeatedly been put forward as a potential DM candidate. While it is theoretically unclear whether such states could actually exist, adding to significant experimental constraints, it is certainly an intriguing idea to have a 'baryonic' DM candidate that would in fact evade the strong evidence from BBN and CMB against this possibility. However, cosmic-ray upscattering of such particles leads to stringent new constraints that have not previously been pointed out in this context. For the concrete case of stable sexaquark DM, as discussed in section 6, we find that the parameter space giving the correct cosmological abundance is strongly pressured.

Table 1. Settings choices for running GiBUU to study neutral current neutrino scattering. We also enforced a logarithmic binning in the outgoing lepton energy, by changing the variable assignment of dElepton from  $E_{\ell} \rightarrow E_{\ell} + \Delta E_{\ell}$  to  $E_{\ell} \rightarrow (1 + \Delta E_{\ell})E_{\ell}$ .  

<table><tr><td colspan="2">&amp;neutrino_induced</td><td colspan="2">&amp;input</td><td colspan="2">&amp;nl_dSigmadElepton</td></tr><tr><td>process_ID</td><td>3</td><td>eventtype</td><td>5</td><td>enu</td><td>\(T_{\chi}\)</td></tr><tr><td>flavor_ID</td><td>2</td><td>numEnsembles</td><td>100</td><td>elepton</td><td>\(0.005T_{\chi}\)</td></tr><tr><td>nuXsectionMode</td><td>2</td><td>numTimeSteps</td><td>0</td><td>delta_elepton</td><td>\(\Delta E_{\ell}\)</td></tr><tr><td>nuExp</td><td>0</td><td>num_Energies</td><td>50</td><td>&amp;target</td><td></td></tr><tr><td>includeQE</td><td>T/F</td><td>num Runs_sameEnergy</td><td>1</td><td>Target_A</td><td>A</td></tr><tr><td>includeDELTA</td><td>T/F</td><td>delta_T</td><td>0.2</td><td>Target_Z</td><td>Z</td></tr><tr><td>includeRES</td><td>T/F</td><td>localEnsemble</td><td>T</td><td>&amp;initDensity</td><td></td></tr><tr><td>path_To_Input</td><td>/path/to/buuinput</td><td>include1pi</td><td>F</td><td>densitySwitch</td><td>2</td></tr><tr><td>includeDIS</td><td>T/F</td><td colspan="2">&amp;neutrinoAnalysis</td><td>&amp;initPauli</td><td></td></tr><tr><td>2p2hQE</td><td>F</td><td>XSection_analysis</td><td>T</td><td>pauliSwitch</td><td>2</td></tr><tr><td>include2p2hDelta</td><td>F</td><td>detailed_diff_output</td><td>F</td><td></td><td></td></tr><tr><td>include2pi</td><td>F</td><td></td><td></td><td></td><td></td></tr></table>

For the analysis performed in this work we used the numerical tool DarkSUSY [64] to compute CRDM fluxes and limits. In doing so we significantly expanded the general numerical routines provided therein, adding in particular inelastic scattering, the contribution from CRs beyond  $p$  and He, and an updated treatment of nuclear form factors in the context of CRDM attenuation. These updates will be included in the next public release of the code.

# Acknowledgments

We thank Timon Emken and Florian Reindl for enlightening discussions about the thermalization efficiency of the CRESST experiment, and Felix Kahlhoefer for insightful comments on how to map nucleon to nuclear cross sections. We further thank Assumpta Pareño, Gilberto Colangelo and Urs Wiedemann for comments related to the hexaquark state. TB warmly thanks the Albert Einstein Institute in Bern, and the CERN Theoretical Physics Department, for support and hospitality during the preparation of this manuscript. JA is supported through the research program "The Hidden Universe of Weakly Interacting Particles" with project number 680.92.18.03 (NWO Vrije Programma), which is partly financed by the Nederlandse Organisatie voor Wetenschappelijk Onderzoek (Dutch Research Council). HK was supported by the ToppForsk-UiS Grant No. PR-10614 and by the Swiss National Science Foundation (SNSF) under grant 200020B-188712.

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.  $\mathrm{SCOAP}^3$  supports the goals of the International Year of Basic Sciences for Sustainable Development.

# References

[1] G. Bertone, D. Hooper and J. Silk, Particle dark matter: Evidence, candidates and constraints, Phys. Rept. 405 (2005) 279 [hep-ph/0404175] [INSPIRE].  
[2] M.W. Goodman and E. Witten, Detectability of Certain Dark Matter Candidates, Phys. Rev. D 31 (1985) 3059 [INSPIRE].  
[3] LZ collaboration, First Dark Matter Search Results from the LUX-ZEPLIN (LZ) Experiment, arXiv:2207.03764 [INSPIRE].  
[4] PANDAX-4T collaboration, Dark Matter Search Results from the PandaX-4T Commissioning Run, Phys. Rev. Lett. 127 (2021) 261802 [arXiv:2107.13438] [INSPIRE].  
[5] XENON collaboration, Dark Matter Search Results from a One Ton-Year Exposure of XENON1T, Phys. Rev. Lett. 121 (2018) 111302 [arXiv:1805.12562] [INSPIRE].  
[6] CRESST collaboration, Results on MeV-scale dark matter from a gram-scale cryogenic calorimeter operated above ground, Eur. Phys. J. C 77 (2017) 637 [arXiv:1707.06749] [INSPIRE].  
[7] N.W. Evans, C.M. Carollo and P.T. de Zeeuw, Triaxial haloes and particle dark matter detection, Mon. Not. Roy. Astron. Soc. 318 (2000) 1131 [astro-ph/0008156] [INSPIRE].  
[8] N.W. Evans and J.H. An, Distribution function of the dark matter, Phys. Rev. D 73 (2006) 023524 [astro-ph/0511687] [INSPIRE].  
[9] L.E. Strigari, Neutrino Coherent Scattering Rates at Direct Dark Matter Detectors, New J. Phys. 11 (2009) 105011 [arXiv:0903.3630] [INSPIRE].  
[10] C.A.J. O'Hare, New Definition of the Neutrino Floor for Direct Dark Matter Searches, Phys. Rev. Lett. 127 (2021) 251802 [arXiv:2109.03116] [INSPIRE].  
[11] S. Knapen, T. Lin and K.M. Zurek, Light Dark Matter: Models and Constraints, Phys. Rev. D 96 (2017) 115021 [arXiv:1709.07882] [INSPIRE].  
[12] R. Essig et al., Snowmass2021 Cosmic Frontier: The landscape of low-threshold dark matter direct detection in the next decade, in 2022 Snowmass Summer Study, 2022, [arXiv:2203.08297] [INSPIRE].  
[13] G.D. Starkman, A. Gould, R. Esmailzadeh and S. Dimopoulos, Opening the Window on Strongly Interacting Dark Matter, Phys. Rev. D 41 (1990) 3594 [INSPIRE].  
[14] G. Zaharijas and G.R. Farrar, A window in the dark matter exclusion limits, Phys. Rev. D 72 (2005) 083502 [astro-ph/0406531] [INSPIRE].  
[15] G.D. Mack, J.F. Beacom and G. Bertone, Towards Closing the Window on Strongly Interacting Dark Matter: Far-Reaching Constraints from Earth's Heat Flow, Phys. Rev. D 76 (2007) 043523 [arXiv:0705.4298] [INSPIRE].  
[16] T. Emken and C. Kouvaris, How blind are underground and surface detectors to strongly interacting Dark Matter?, Phys. Rev. D 97 (2018) 115047 [arXiv:1802.04764] [INSPIRE].  
[17] M. Ibe, W. Nakano, Y. Shoji and K. Suzuki, Migdal Effect in Dark Matter Direct Detection Experiments, JHEP 03 (2018) 194 [arXiv:1707.07258] [INSPIRE].  
[18] XENON collaboration, Search for Light Dark Matter Interactions Enhanced by the Migdal Effect or Bremsstrahlung in XENON1T, Phys. Rev. Lett. 123 (2019) 241803 [arXiv:1907.12771] [INSPIRE].  
[19] C. Kouvaris and J. Pradler, Probing sub-GeV Dark Matter with conventional detectors, Phys. Rev. Lett. 118 (2017) 031803 [arXiv:1607.01789] [INSPIRE].

[20] J.I. Collar and F.T. Avignone, Diurnal modulation effects in cold dark matter experiments, Phys. Lett. B 275 (1992) 181 [INSPIRE].  
[21] J.I. Collar and F.T. Avignone III, The effect of elastic scattering in the Earth on cold dark matter experiments, Phys. Rev. D 47 (1993) 5238 [INSPIRE].  
[22] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[23] C.V. Cappiello, K.C.Y. Ng and J.F. Beacom, Reverse Direct Detection: Cosmic Ray Scattering With Light Dark Matter, Phys. Rev. D 99 (2019) 063004 [arXiv:1810.07705] [INSPIRE].  
[24] J. Alvey, M. Campos, M. Fairbairn and T. You, Detecting Light Dark Matter via Inelastic Cosmic Ray Collisions, Phys. Rev. Lett. 123 (2019) 261802 [arXiv:1905.05776] [INSPIRE].  
[25] W. DeRocco, P.W. Graham, D. Kasen, G. Marques-Tavares and S. Rajendran, Supernovasignals of light dark matter, Phys. Rev. D 100 (2019) 075018 [arXiv:1905.09284] [INSPIRE].  
[26] J.B. Dent, B. Dutta, J.L. Newstead and I.M. Shoemaker, Bounds on Cosmic Ray-Boosted Dark Matter in Simplified Models and its Corresponding Neutrino-Floor, Phys. Rev. D 101 (2020) 116007 [arXiv:1907.03782] [INSPIRE].  
[27] W. Wang, L. Wu, J.M. Yang, H. Zhou and B. Zhu, *Cosmic ray boosted sub-GeV gravitationally interacting dark matter in direct detection*, JHEP **12** (2020) 072 [Erratum ibid. 02 (2021) 052] [arXiv:1912.09904] [INSPIRE].  
[28] Y. Zhang, Speeding up dark matter with solar neutrinos, PTEP 2022 (2022) 013B05 [arXiv:2001.00948] [INSPIRE].  
[29] R. Plestid, V. Takhistov, Y.-D. Tsai, T. Bringmann, A. Kusenko and M. Pospelov, New Constraints on Millicharged Particles from Cosmic-ray Production, Phys. Rev. D 102 (2020) 115032 [arXiv:2002.11732] [INSPIRE].  
[30] L. Su, W. Wang, L. Wu, J.M. Yang and B. Zhu, Atmospheric Dark Matter and Xenon1T Excess, Phys. Rev. D 102 (2020) 115028 [arXiv:2006.11837] [INSPIRE].  
[31] W. Cho, K.-Y. Choi and S.M. Yoo, Searching for boosted dark matter mediated by a new gauge boson, Phys. Rev. D 102 (2020) 095010 [arXiv:2007.04555] [INSPIRE].  
[32] G. Guo, Y.-L.S. Tsai, M.-R. Wu and Q. Yuan, Elastic and Inelastic Scattering of Cosmic-Rays on Sub-GeV Dark Matter, Phys. Rev. D 102 (2020) 103004 [arXiv:2008.12137] [INSPIRE].  
[33] C. Xia, Y.-H. Xu and Y.-F. Zhou, Constraining light dark matter upscattered by ultrahigh-energy cosmic rays, Nucl. Phys. B 969 (2021) 115470 [arXiv:2009.00353] [INSPIRE].  
[34] J.B. Dent, B. Dutta, J.L. Newstead, I.M. Shoemaker and N.T. Arellano, Present and future status of light dark matter models from cosmic-ray electron upscattering, Phys. Rev. D 103 (2021) 095015 [arXiv:2010.09749] [INSPIRE].  
[35] J.B. Dent et al., Gamma ray signals from cosmic ray scattering on axionlike particles, Phys. Rev. D 104 (2021) 055044 [arXiv:2012.07930] [INSPIRE].  
[36] T. Emken, Solar reflection of light dark matter with heavy mediators, Phys. Rev. D 105 (2022) 063020 [arXiv:2102.12483] [INSPIRE].  
[37] A. Das and M. Sen, Boosted dark matter from diffuse supernova neutrinos, Phys. Rev. D 104 (2021) 075029 [arXiv:2104.00027] [INSPIRE].

[38] N.F. Bell et al., Cosmic-ray upscattered inelastic dark matter, Phys. Rev. D 104 (2021) 076020 [arXiv:2108.00583] [INSPIRE].  
[39] H. An, H. Nie, M. Pospelov, J. Pradler and A. Ritz, Solar reflection of dark matter, Phys. Rev. D 104 (2021) 103026 [arXiv:2108.10332] [INSPIRE].  
[40] J.-C. Feng, X.-W. Kang, C.-T. Lu, Y.-L.S. Tsai and F.-S. Zhang, Revising inelastic dark matter direct detection by including the cosmic ray acceleration, JHEP 04 (2022) 080 [arXiv:2110.08863] [INSPIRE].  
[41] J.-W. Wang, A. Granelli and P. Ullio, Direct Detection Constraints on Blazar-Boosted Dark Matter, Phys. Rev. Lett. 128 (2022) 221104 [arXiv:2111.13644] [INSPIRE].  
[42] A. Granelli, P. Ullio and J.-W. Wang, *Blazar-boosted dark matter at Super-Kamiokande*, JCAP 07 (2022) 013 [arXiv:2202.07598] [INSPIRE].  
[43] L. Darmé, Atmospheric resonant production for light dark sectors, Phys. Rev. D 106 (2022) 055015 [arXiv:2205.09773] [INSPIRE].  
[44] C. Xia, Y.-H. Xu and Y.-F. Zhou, Azimuthal asymmetry in cosmic-ray boosted dark matter flux, arXiv:2206.11454 [INSPIRE].  
[45] D. Bardhan, S. Bhowmick, D. Ghosh, A. Guha and D. Sachdeva, Boosting through the Darkness: Bounds on boosted dark matter from direct detection, arXiv:2208.09405 [INSPIRE].  
[46] K. Bondarenko, A. Boyarsky, T. Bringmann, M. Hufnagel, K. Schmidt-Hoberg and A. Sokolenko, Direct detection and complementary constraints for sub-GeV dark matter, JHEP 03 (2020) 118 [arXiv:1909.08632] [INSPIRE].  
[47] D. McKeen, M. Moore, D.E. Morrissey, M. Pospelov and H. Ramani, Accelerating Earth-bound dark matter, Phys. Rev. D 106 (2022) 035011 [arXiv:2202.08840] [INSPIRE].  
[48] Y. Ema, F. Sala and R. Sato, Light Dark Matter at Neutrino Experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[49] C.V. Cappiello and J.F. Beacom, *Strong New Limits on Light Dark Matter from Neutrino Experiments*, Phys. Rev. D **100** (2019) 103011 [Erratum ibid. **104** (2021) 069901] [arXiv:1906.11283] [INSPIRE].  
[50] J. Berger et al., Prospects for detecting boosted dark matter in DUNE through hadronic interactions, Phys. Rev. D 103 (2021) 095012 [arXiv:1912.05558] [INSPIRE].  
[51] D. Kim, P.A.N. Machado, J.-C. Park and S. Shin, Optimizing Energetic Light Dark Matter Searches in Dark Matter and Neutrino Experiments, JHEP 07 (2020) 057 [arXiv:2003.07369] [INSPIRE].  
[52] G. Guo, Y.-L.S. Tsai and M.-R. Wu, Probing cosmic-ray accelerated light dark matter with IceCube, JCAP 10 (2020) 049 [arXiv:2004.03161] [INSPIRE].  
[53] A. De Roeck, D. Kim, Z.G. Moghaddam, J.-C. Park, S. Shin and L.H. Whitehead, Probing Energetic Light Dark Matter with Multi-Particle Tracks Signatures at DUNE, JHEP 11 (2020) 043 [arXiv:2005.08979] [INSPIRE].  
[54] S.-F. Ge, J. Liu, Q. Yuan and N. Zhou, Diurnal Effect of Sub-GeV Dark Matter Boosted by Cosmic Rays, Phys. Rev. Lett. 126 (2021) 091804 [arXiv:2005.09480] [INSPIRE].  
[55] Q.-H. Cao, R. Ding and Q.-F. Xiang, Searching for sub-MeV boosted dark matter from xenon electron direct detection, Chin. Phys. C 45 (2021) 045002 [arXiv:2006.12767] [INSPIRE].

[56] Y. Jho, J.-C. Park, S.C. Park and P.-Y. Tseng, Leptonic New Force and Cosmic-ray Boosted Dark Matter for the XENON1T Excess, Phys. Lett. B 811 (2020) 135863 [arXiv:2006.13910] [INSPIRE].  
[57] Z.-H. Lei, J. Tang and B.-L. Zhang, Constraints on cosmic-ray boosted dark matter in CDEX-10 *, Chin. Phys. C 46 (2022) 085103 [arXiv:2008.07116] [INSPIRE].  
[58] R. Harnik, R. Plestid, M. Pospelov and H. Ramani, Millicharged cosmic rays and low recoil detectors, Phys. Rev. D 103 (2021) 075029 [arXiv:2010.11190] [INSPIRE].  
[59] Y. Ema, F. Sala and R. Sato, Neutrino experiments probe hadrophilic light dark matter, SciPost Phys. 10 (2021) 072 [arXiv:2011.01939] [INSPIRE].  
[60] J. Bramante, B.J. Kavanagh and N. Raj, Scattering Searches for Dark Matter in Subhalos: Neutron Stars, Cosmic Rays, and Old Rocks, Phys. Rev. Lett. 128 (2022) 231801 [arXiv:2109.04582] [INSPIRE].  
[61] T. Emken, J. Frerick, S. Heeba and F. Kahlhoefer, *Electron recoils from terrestrial upscattering of inelastic dark matter*, Phys. Rev. D 105 (2022) 055023 [arXiv:2112.06930] [INSPIRE].  
[62] PANDAX-II collaboration, Search for Cosmic-Ray Boosted Sub-GeV Dark Matter at the PandaX-II Experiment, Phys. Rev. Lett. 128 (2022) 171801 [arXiv:2112.08957] [INSPIRE].  
[63] C. Xia, Y.-H. Xu and Y.-F. Zhou, Production and attenuation of cosmic-ray boosted dark matter, JCAP 02 (2022) 028 [arXiv:2111.05559] [INSPIRE].  
[64] T. Bringmann, J. Edsjö, P. Gondolo, P. Ullio and L. Bergström, DarkSUSY 6: An Advanced Tool to Compute Dark Matter Properties Numerically, JCAP 07 (2018) 033 [arXiv:1802.03399] [INSPIRE].  
[65] J.I. Read, The Local Dark Matter Density, J. Phys. G 41 (2014) 063101 [arXiv:1404.1938] [INSPIRE].  
[66] J. Einasto, Dark Matter, arXiv:0901.0632 [INSPIRE].  
[67] A.W. Strong and I.V. Moskalenko, Propagation of cosmic-ray nucleons in the galaxy, Astrophys. J. 509 (1998) 212 [astro-ph/9807150] [INSPIRE].  
[68] M.J. Boschini et al., Deciphering the local Interstellar spectra of primary cosmic ray species with HelMod, Astrophys. J. 858 (2018) 61 [arXiv:1804.06956] [INSPIRE].  
[69] M.J. Boschini et al., Inference of the Local Interstellar Spectra of Cosmic-Ray Nuclei  $Z \leq 28$  with the GalProp-HelMod Framework, Astrophys. J. Suppl. 250 (2020) 27 [arXiv:2006.01337] [INSPIRE].  
[70] AMS collaboration, Observation of New Properties of Secondary Cosmic Rays Lithium, Beryllium, and Boron by the Alpha Magnetic Spectrometer on the International Space Station, Phys. Rev. Lett. 120 (2018) 021101 [INSPIRE].  
[71] AMS collaboration, Precision Measurement of Cosmic-Ray Nitrogen and its Primary and Secondary Components with the Alpha Magnetic Spectrometer on the International Space Station, Phys. Rev. Lett. 121 (2018) 051103 [INSPIRE].  
[72] AMS collaboration, Properties of Neon, Magnesium, and Silicon Primary Cosmic Rays Results from the Alpha Magnetic Spectrometer, Phys. Rev. Lett. 124 (2020) 211102 [INSPIRE].  
[73] L. Miramonti, European underground laboratories: An Overview, AIP Conf. Proc. 785 (2005) 3 [hep-ex/0503054] [INSPIRE].  
[74] H. Wulandari, J. Jochum, W. Rau and F. von Feilitzsch, Neutron flux underground revisited, Astropart. Phys. 22 (2004) 313 [hep-ex/0312050] [INSPIRE].

[75] T. Emken and C. Kouvaris, *DaMaSCUS: The Impact of Underground Scatterings on Direct Detection of Light Dark Matter*, JCAP **10** (2017) 031 [arXiv:1706.02249] [INSPIRE].  
[76] M.S. Mahdawi and G.R. Farrar, Constraints on Dark Matter with a moderately large and velocity-dependent DM-nucleon cross-section, JCAP 10 (2018) 007 [arXiv:1804.03073] [INSPIRE].  
[77] T. Emken, Dark Matter in the Earth and the Sun — Simulating Underground Scatterings for the Direct Detection of Low-Mass Dark Matter, Ph.D. thesis, Southern Denmark University, CP3-Origins 2019, arXiv:1906.07541 [INSPIRE].  
[78] GAMBIT DARK MATTER WORKGROUP collaboration, DarkBit: A GAMBIT module for computing dark matter observables and likelihoods, Eur. Phys. J. C 77 (2017) 831 [arXiv:1705.07920] [INSPIRE].  
[79] GAMBIT collaboration, Global analyses of Higgs portal singlet dark matter models using GAMBIT, Eur. Phys. J. C 79 (2019) 38 [arXiv:1808.10465] [INSPIRE].  
[80] E. Del Nobile, The Theory of Direct Dark Matter Detection: A Guide to Computations, arXiv:2104.12785 [INSPIRE].  
[81] J. Cooley, Dark Matter direct detection of classical WIMPs, SciPost Phys. Lect. Notes 55 (2022) 1 [arXiv:2110.02359] [INSPIRE].  
[82] R.H. Helm, Inelastic and Elastic Scattering of 187-Mev Electrons from Selected Even-Even Nuclei, Phys. Rev. 104 (1956) 1466 [INSPIRE].  
[83] G. Duda, A. Kemper and P. Gondolo, Model Independent Form Factors for Spin Independent Neutralino-Nucleon Scattering from Elastic Electron Scattering Data, JCAP 04 (2007) 012 [hep-ph/0608035] [INSPIRE].  
[84] H. De Vries, C.W. De Jager and C. De Vries, Nuclear charge and magnetization density distribution parameters from elastic electron scattering, Atom. Data Nucl. Data Tabl. 36 (1987) 495.  
[85] C.F. Perdrisat, V. Punjabi and M. Vanderhaeghen, *Nucleon Electromagnetic Form Factors*, *Prog. Part. Nucl. Phys.* **59** (2007) 694 [hep-ph/0612014] [INSPIRE].  
[86] V. Punjabi, C.F. Perdrisat, M.K. Jones, E.J. Brash and C.E. Carlson, The Structure of the Nucleon: Elastic Electromagnetic Form Factors, Eur. Phys. J. A 51 (2015) 79 [arXiv:1503.01452] [INSPIRE].  
[87] L. Baudis et al., *Signatures of Dark Matter Scattering Inelastically Off Nuclei*, Phys. Rev. D 88 (2013) 115014 [arXiv:1309.0825] [INSPIRE].  
[88] C. McCabe, Prospects for dark matter detection with inelastic transitions of xenon, JCAP 05 (2016) 033 [arXiv:1512.00460] [INSPIRE].  
[89] M. Hoferichter, P. Klos, J. Menéndez and A. Schwenk, Nuclear structure factors for general spin-independent WIMP-nucleus scattering, Phys. Rev. D 99 (2019) 055031 [arXiv:1812.05617] [INSPIRE].  
[90] XMASS-I collaboration, Search for inelastic WIMP nucleus scattering on  $^{129}$ Xe in data from the XMASS-I experiment, PTEP 2014 (2014) 063C01 [arXiv:1401.4737] [INSPIRE].  
[91] XENON collaboration, Search for WIMP Inelastic Scattering off Xenon Nuclei with XENON100, Phys. Rev. D 96 (2017) 022008 [arXiv:1705.05830] [INSPIRE].  
[92] B. Lehnert et al., Search for Dark Matter Induced Deexcitation of  $^{180}Ta^{\mathrm{m}}$ , Phys. Rev. Lett. 124 (2020) 181802 [arXiv:1911.07865] [INSPIRE].

[93] XENON collaboration, Search for inelastic scattering of WIMP dark matter in XENON1T, Phys. Rev. D 103 (2021) 063028 [arXiv:2011.10431] [INSPIRE].  
[94] O. Buss et al., Transport-theoretical Description of Nuclear Reactions, Phys. Rept. 512 (2012) 1 [arXiv:1106.1344] [INSPIRE].  
[95] https://gibuu.hepforge.org/trac/wiki.  
[96] J.A. Formaggio and G.P. Zeller, From eV to EeV: Neutrino Cross Sections Across Energy Scales, Rev. Mod. Phys. 84 (2012) 1307 [arXiv:1305.7513] [INSPIRE].  
[97] W.M. Alberico et al., Inelastic neutrino and anti-neutrino scattering on nuclei and 'strangeness' of the nucleon, Nucl. Phys. A 623 (1997) 471 [hep-ph/9703415] [INSPIRE].  
[98] PARTICLE DATA GROUP collaboration, Review of Particle Physics, Phys. Lett. B 667 (2008) 1 [INSPIRE].  
[99] GAMBIT collaboration, Thermal WIMPs and the scale of new physics: global fits of Dirac dark matter effective field theories, Eur. Phys. J. C 81 (2021) 992 [arXiv:2106.02056] [INSPIRE].  
[100] K.K. Rogers, C. Dvorkin and H.V. Peiris, Limits on the Light Dark Matter-Proton Cross Section from Cosmic Large-Scale Structure, Phys. Rev. Lett. 128 (2022) 171301 [arXiv:2111.10386] [INSPIRE].  
[101] K. Maamari, V. Gluscevic, K.K. Boddy, E.O. Nadler and R.H. Wechsler, Bounds on velocity-dependent dark matter-proton scattering from Milky Way satellite abundance, Astrophys. J. Lett. 907 (2021) L46 [arXiv:2010.02936] [INSPIRE].  
[102] A. Bhoonah, J. Bramante, F. Elahi and S. Schon, Galactic Center gas clouds and novel bounds on ultralight dark photon, vector portal, strongly interacting, composite, and super-heavy dark matter, Phys. Rev. D 100 (2019) 023001 [arXiv:1812.10919] [INSPIRE].  
[103] D. McCammon et al., A high spectral resolution observation of the soft  $x$ -ray diffuse background with thermal detectors, Astrophys. J. 576 (2002) 188 [astro-ph/0205012] [INSPIRE].  
[104] D.A. Neufeld and D.J. Brach-Neufeld, Dark Matter that Interacts with Baryons: Experimental Limits on the Interaction Cross-section for 27 Atomic Nuclei, and Resultant Constraints on the Particle Properties, Astrophys. J. 877 (2019) 8 [arXiv:1904.01590] [INSPIRE].  
[105] X. Xu and G.R. Farrar, Constraints on GeV Dark Matter interaction with baryons, from a novel Dewar experiment, arXiv:2112.00707 [INSPIRE].  
[106] X. Xu and G.R. Farrar, Resonant Scattering between Dark Matter and Baryons: Revised Direct Detection and CMB Limits, arXiv:2101.00142 [INSPIRE].  
[107] PLANCK collaboration, Planck 2015 results. XI. CMB power spectra, likelihoods, and robustness of parameters, Astron. Astrophys. 594 (2016) A11 [arXiv:1507.02704] [INSPIRE].  
[108] W.L. Xu, C. Dvorkin and A. Chael, Probing sub-GeV Dark Matter-Baryon Scattering with Cosmological Observables, Phys. Rev. D 97 (2018) 103530 [arXiv:1802.06788] [INSPIRE].  
[109] DES collaboration, Milky Way Satellite Census. I. The Observational Selection Function for Milky Way Satellites in DES Y3 and Pan-STARRS DR1, Astrophys. J. 893 (2020) 1 [arXiv:1912.03302] [INSPIRE].  
[110] A. Bhoonah, J. Bramante, F. Elahi and S. Schon, Calorimetric Dark Matter Detection With Galactic Center Gas Clouds, Phys. Rev. Lett. 121 (2018) 131101 [arXiv:1806.06857] [INSPIRE].

[111] N.M. McClure-Griffiths et al., Atomic Hydrogen in a Galactic Center Outflow, Astrophys. J. Lett. 770 (2013) L4 [arXiv:1304.7538] [INSPIRE].  
[112] E.M. Di Teodoro et al., *Blowing in the Milky Way Wind: Neutral Hydrogen Clouds Tracing the Galactic Nuclear Outflow*, Astrophys. J. 855 (2018) 33 [arXiv:1802.02152] [INSPIRE].  
[113] G.R. Farrar, F.J. Lockman, N.M. McClure-Griffiths and D. Wadekar, Comment on the paper "Calorimetric Dark Matter Detection with Galactic Center Gas Clouds", Phys. Rev. Lett. 124 (2020) 029001 [arXiv:1903.12191] [INSPIRE].  
[114] B.D. Wandelt, R. Dave, G.R. Farrar, P.C. McGuire, D.N. Spergel and P.J. Steinhardt, Selfinteracting dark matter, in 4th International Symposium on Sources and Detection of Dark Matter in the Universe (DM 2000), pp. 263-2742000 [astro-ph/0006344] [INSPIRE].  
[115] A.L. Erickcek, P.J. Steinhardt, D. McCammon and P.C. McGuire, Constraints on the Interactions between Dark Matter and Baryons from the X-ray Quantum Calorimetry Experiment, Phys. Rev. D 76 (2007) 042007 [arXiv:0704.0794] [INSPIRE].  
[116] CRESST collaboration, Results on light dark matter particles with a low-threshold CRESST-II detector, Eur. Phys. J. C 76 (2016) 25 [arXiv:1509.01515] [INSPIRE].  
[117] D. Wadekar and G.R. Farrar, Gas-rich dwarf galaxies as a new probe of dark matter interactions with ordinary matter, Phys. Rev. D 103 (2021) 123028 [arXiv:1903.12190] [INSPIRE].  
[118] F. Reindl (CRESST collaboration), personal communication.  
[119] L. Hui, J.P. Ostriker, S. Tremaine and E. Witten, Ultralight scalars as cosmological dark matter, Phys. Rev. D 95 (2017) 043541 [arXiv:1610.08297] [INSPIRE].  
[120] V. Iršić et al., New Constraints on the free-streaming of warm dark matter from intermediate and small scale Lyman-α forest data, Phys. Rev. D 96 (2017) 023522 [arXiv:1702.01764] [INSPIRE].  
[121] S. Chang, A. Pierce and N. Weiner, Momentum Dependent Dark Matter Scattering, JCAP 01 (2010) 006 [arXiv:0908.3192] [INSPIRE].  
[122] N. Fornengo, P. Panci and M. Regis, Long-Range Forces in Direct Dark Matter Searches, Phys. Rev. D 84 (2011) 115002 [arXiv:1108.4661] [INSPIRE].  
[123] M. Kaplinghat, S. Tulin and H.-B. Yu, Direct Detection Portals for Self-interacting Dark Matter, Phys. Rev. D 89 (2014) 035009 [arXiv:1310.7945] [INSPIRE].  
[124] J. Silk, *Cosmic black body radiation and galaxy formation*, Astrophys. J. 151 (1968) 459 [INSPIRE].  
[125] E.O. Nadler, V. Gluscevic, K.K. Boddy and R.H. Wechsler, Constraints on Dark Matter Microphysics from the Milky Way Satellite Population, Astrophys. J. Lett. 878 (2019) 32 [Erratum ibid. 897 (2020) L46] [arXiv:1904.10000] [INSPIRE].  
[126] J.H. Davis, Probing Sub-GeV Mass Strongly Interacting Dark Matter with a Low-Threshold Surface Experiment, Phys. Rev. Lett. 119 (2017) 211302 [arXiv:1708.01484] [INSPIRE].  
[127] C. Kouvaris and I.M. Shoemaker, Daily modulation as a smoking gun of dark matter with significant stopping rate, Phys. Rev. D 90 (2014) 095011 [arXiv:1405.1729] [INSPIRE].  
[128] T. Emken, C. Kouvaris and I.M. Shoemaker, Terrestrial Effects on Dark Matter-Electron Scattering Experiments, Phys. Rev. D 96 (2017) 015018 [arXiv:1702.07750] [INSPIRE].  
[129] U.S. Government Printing Office, U.S. Standard Atmosphere (1976).

[130] P.F. Depta, M. Hufnagel and K. Schmidt-Hoberg, Updated BBN constraints on electromagnetic decays of MeV-scale particles, JCAP 04 (2021) 011 [arXiv:2011.06519] [INSPIRE].  
[131] G. Krnjaic, Probing Light Thermal Dark-Matter With a Higgs Portal Mediator, Phys. Rev. D 94 (2016) 073009 [arXiv:1512.04119] [INSPIRE].  
[132] G. Krnjaic and S.D. McDermott, Implications of BBN Bounds for Cosmic Ray Upscattered Dark Matter, Phys. Rev. D 101 (2020) 123022 [arXiv:1908.00007] [INSPIRE].  
[133] M.T. Frandsen, F. Kahlhoefer, S. Sarkar and K. Schmidt-Hoberg, Direct detection of dark matter in models with a light  $Z'$ , JHEP 09 (2011) 128 [arXiv:1107.2118] [INSPIRE].  
[134] S. Nussinov, Technocosmology: Could A Technibaryon Excess Provide A ‘natural’ Missing Mass Candidate?, Phys. Lett. B 165 (1985) 55 [INSPIRE].  
[135] R.S. Chivukula and T.P. Walker, Technicolor Cosmology, Nucl. Phys. B 329 (1990) 445 [INSPIRE].  
[136] J.M. Cline, Z. Liu, G.D. Moore and W. Xue, Composite strongly interacting dark matter, Phys. Rev. D 90 (2014) 015023 [arXiv:1312.3325] [INSPIRE].  
[137] G. Krnjaic and K. Sigurdson, Big Bang Darkleosynthesis, Phys. Lett. B 751 (2015) 464 [arXiv:1406.1171] [INSPIRE].  
[138] M.B. Wise and Y. Zhang, Yukawa Bound States of a Large Number of Fermions, JHEP 02 (2015) 023 [Erratum ibid. 10 (2015) 165] [arXiv:1411.1772] [INSPIRE].  
[139] E. Hardy, R. Lasenby, J. March-Russell and S.M. West, *Signatures of Large Composite Dark Matter States*, JHEP 07 (2015) 133 [arXiv:1504.05419] [INSPIRE].  
[140] A. Coskuner, D.M. Grabowska, S. Knapen and K.M. Zurek, Direct Detection of Bound States of Asymmetric Dark Matter, Phys. Rev. D 100 (2019) 035025 [arXiv:1812.07573] [INSPIRE].  
[141] R. Contino, A. Mitridate, A. Podo and M. Redi, *Gluequark Dark Matter*, JHEP 02 (2019) 187 [arXiv:1811.06975] [INSPIRE].  
[142] M.C. Digman, C.V. Cappiello, J.F. Beacom, C.M. Hirata and A.H.G. Peter, Not as big as a barn: Upper bounds on dark matter-nucleus cross sections, Phys. Rev. D 100 (2019) 063013 [Erratum ibid. 106 (2022) 089902] [arXiv:1907.10618] [INSPIRE].  
[143] B. Feldstein, A.L. Fitzpatrick and E. Katz, Form Factor Dark Matter, JCAP 01 (2010) 020 [arXiv:0908.2991] [INSPIRE].  
[144] R. Laha and E. Braaten, Direct detection of dark matter in universal bound states, Phys. Rev. D 89 (2014) 103510 [arXiv:1311.6386] [INSPIRE].  
[145] X. Chu, C. Garcia-Cely and H. Murayama, Finite-size dark matter and its effect on small-scale structure, Phys. Rev. Lett. 124 (2020) 041101 [arXiv:1901.00075] [INSPIRE].  
[146] G.R. Farrar, A stable  $H$  dibaryon: Dark matter candidate within QCD?, Int. J. Theor. Phys. 42 (2003) 1211 [INSPIRE].  
[147] G.R. Farrar, Stable Sexaquark, arXiv:1708.08951 [INSPIRE].  
[148] G.R. Farrar, Z. Wang and X. Xu, Dark Matter Particle in QCD, arXiv:2007.10378 [INSPIRE].  
[149] G.R. Farrar, A Stable Sexaquark: Overview and Discovery Strategies, arXiv:2201.01334 [INSPIRE].  
[150] E. Aver, K.A. Olive and E.D. Skillman, The effects of He I λ10830 on helium abundance determinations, JCAP 07 (2015) 011 [arXiv:1503.08146] [INSPIRE].

[151] PLANCK collaboration, Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [Erratum ibid. 652 (2021) C4] [arXiv:1807.06209] [INSPIRE].  
[152] R.L. Jaffe, Perhaps a Stable Dihyperon, Phys. Rev. Lett. 38 (1977) 195 [Erratum ibid. 38 (1977) 617] [INSPIRE].  
[153] T. Sakai, K. Shimizu and K. Yazaki, H dibaryon, Prog. Theor. Phys. Suppl. 137 (2000) 121 [nucl-th/9912063] [INSPIRE].  
[154] H. Clement, On the History of Dibaryons and their Final Observation, Prog. Part. Nucl. Phys. 93 (2017) 195 [arXiv:1610.05591] [INSPIRE].  
[155] NPLQCD collaboration, Evidence for a Bound  $H$ -dibaryon from Lattice QCD, Phys. Rev. Lett. 106 (2011) 162001 [arXiv:1012.3812] [INSPIRE].  
[156] HAL QCD collaboration, Bound H-dibaryon in Flavor SU(3) Limit of Lattice QCD, Phys. Rev. Lett. 106 (2011) 162002 [arXiv:1012.5928] [INSPIRE].  
[157] NPLQCD collaboration, Light Nuclei and Hypernuclei from Quantum Chromodynamics in the Limit of SU(3) Flavor Symmetry, Phys. Rev. D 87 (2013) 034506 [arXiv:1206.5219] [INSPIRE].  
[158] A. Francis, J.R. Green, P.M. Junnarkar, C. Miao, T.D. Rae and H. Wittig, Lattice QCD study of the  $H$  dibaryon using hexaquark and two-baryon interpolators, Phys. Rev. D 99 (2019) 074505 [arXiv:1805.03966] [INSPIRE].  
[159] E.W. Kolb and M.S. Turner, *Dibaryons cannot be the dark matter*, Phys. Rev. D 99 (2019) 063519 [arXiv:1809.06003] [INSPIRE].  
[160] C. Gross, A. Polosa, A. Strumia, A. Urbano and W. Xue, Dark Matter in the Standard Model?, Phys. Rev. D 98 (2018) 063005 [arXiv:1803.10242] [INSPIRE].  
[161] P.M.M. Maessen, T.A. Rijken and J.J. de Swart, Soft Core Baryon Baryon One Boson Exchange Models. 2. Hyperon-Nucleon Potential, Phys. Rev. C 40 (1989) 2226 [INSPIRE].  
[162] M.M. Nagels, T.A. Rijken and Y. Yamamoto, Extended-soft-core baryon-baryon model ESC16. II. Hyperon-nucleon interactions, Phys. Rev. C 99 (2019) 044003 [arXiv:1501.06636] [INSPIRE].  
[163] S. Weinberg, Nuclear forces from chiral Lagrangians, Phys. Lett. B 251 (1990) 288 [INSPIRE].  
[164] V.G.J. Stoks and T.A. Rijken, *Meson-baryon coupling constants from a chiral invariant SU(3) Lagrangian and application to  $N$  N scattering*, Nucl. Phys. A 613 (1997) 311 [nucl-th/9611002] [INSPIRE].  
[165] SNO collaboration, The Sudbury Neutrino Observatory, Nucl. Phys. B 908 (2016) 30 [arXiv:1602.02469] [INSPIRE].  
[166] D.A. Neufeld, G.R. Farrar and C.F. McKee, Dark Matter that Interacts with Baryons: Density Distribution within the Earth and New Constraints on the Interaction Cross-section, Astrophys. J. 866 (2018) 111 [arXiv:1805.08794] [INSPIRE].  
[167] S. Tulin, H.-B. Yu and K.M. Zurek, Beyond Collisionless Dark Matter: Particle Physics Dynamics for Dark Matter Halo Structure, Phys. Rev. D 87 (2013) 115007 [arXiv:1302.3898] [INSPIRE].