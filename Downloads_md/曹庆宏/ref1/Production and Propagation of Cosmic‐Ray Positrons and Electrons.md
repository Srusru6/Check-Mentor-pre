# PRODUCTION AND PROPAGATION OF COSMIC-RAY POSITRONS AND ELECTRONS

I. V. MOSKALENKO<sup>1</sup> AND A. W. STRONG

Max-Planck-Institut für extraterrestrische Physik, Postfach 1603, 85740 Garching bei München, Germany;

imos@mpe-garching.mpg.de, aws@mpe-garching.mpg.de

Received 1997 June 11; accepted 1997 September 8

# ABSTRACT

We have made a new calculation of the cosmic-ray secondary positron spectrum using a diffusive halo model for Galactic cosmic-ray propagation. The code computes self-consistently the spectra of primary and secondary nucleons, primary electrons, and secondary positrons and electrons. The models are first adjusted to agree with the observed cosmic-ray boron/carbon ratio, and the interstellar proton and helium spectra are then computed; these spectra are used to obtain the source function for the secondary positrons/electrons that are finally propagated with the same model parameters. The primary electron spectrum is evaluated, again using the same model. Fragmentation and energy losses are computed using realistic distributions for the interstellar gas and radiation fields, and diffusive reacceleration is also incorporated. Our study includes a critical reevaluation of the secondary decay calculation for positrons.

The predicted positron fraction is in good agreement with the measurements up to  $10\mathrm{GeV}$ , beyond which the observed flux is higher than that calculated. Since the positron fraction is now measured accurately in the 1-10 GeV range, our primary electron spectrum should be a good estimate of the true interstellar spectrum in this range, of interest for gamma-ray and solar modulation studies. We further show that a harder interstellar nucleon spectrum, similar to that suggested to explain EGRET diffuse Galactic gamma-ray observations above  $1\mathrm{GeV}$ , can reproduce the positron observations above  $10\mathrm{GeV}$  without requiring a primary positron component.

Subject headings: acceleration of particles - cosmic rays - diffusion - elementary particles

Galaxy: halo — gamma rays: theory — ISM: abundances

# 1. INTRODUCTION

Secondary positrons in Galactic cosmic rays are an important diagnostic for models of cosmic-ray propagation and also for solar modulation studies. Recently, several new experiments have provided improved data on both the positron-to-electron ratio and the positron spectrum itself (Barwick et al. 1997; Barbiellini et al. 1996; Golden et al. 1996). These and previous data have mainly been compared with model predictions using leaky box and diffusion models from Protheroe (1982). Since these predictions were made, new information and ideas have contributed to our understanding of cosmic-ray propagation: new measurements of nucleon secondary-to-primary ratios, the energy dependence of the propagation, results from gamma-ray astronomy, and studies of the effects of diffusive reacceleration. For this reason, new calculations of secondary positrons are desirable.

Recently, an extensive computer code for the calculation of Galactic cosmic-ray propagation has been developed (Strong & Moskalenko 1997a), which is a further development of the approach described by Strong & Youssefi (1995) and Strong (1996). Primary and secondary nucleons, primary and secondary electrons, and secondary positrons are included. The basic spatial propagation mechanisms are (momentum-dependent) diffusion and convection, while in momentum space, energy loss and diffusive reacceleration are treated. Fragmentation and energy losses are computed using realistic distributions for the interstellar gas and radiation fields.

The main motivation for developing this code was the prediction of diffuse Galactic gamma rays for comparison

with data from the Compton Gamma Ray Observatory (CGRO) instruments EGRET, COMPTEL, and OSSE. More generally, the idea is to develop a model that self-consistently reproduces observational data of many kinds related to the cosmic-ray origin and propagation: directly via measurements of nuclei, electrons, and positrons and indirectly via gamma rays and synchrotron radiation. These data provide many independent constraints on any model, and our approach is able to take advantage of this since it must be consistent with all types of observation. We emphasize also the use of realistic astrophysical input (e.g., for the gas distribution) as well as theoretical developments (e.g., reacceleration). The code is sufficiently general that new physical effects can be introduced as required. In this paper, we focus on positrons. The secondary positron problem is closely connected with that of gamma rays from  $\pi^0$  decay since the same cosmic-ray nucleons are involved. For this reason, the present application is a natural extension of the original code.

The basic procedure is first to obtain a set of propagation parameters that reproduce the cosmic-ray B/C ratio and the spectrum of primary electrons. The proton and helium spectra are then computed using these parameters, and used to obtain the source function for the secondary positrons and electrons. The secondary positron and electron spectra are then computed using the same propagation model. Note that although the ratio of positrons to electrons is normally used for the comparison with data, it is in fact the positron spectrum itself that is of interest in testing propagation models; however, since the ratio is more easily measured experimentally, we also use it in this work.

Turning the argument around, we note that if we can compute the positron spectrum reliably, then accurate measurements of the positron fraction enable us to determine the true interstellar electron spectrum unless there is signifi

cant charge-sign-dependent solar modulation (for a discussion of the charge-sign dependence, see Clem et al. 1996). This approach also provides an independent test for models of the primary electron spectrum, complementing gamma-ray and synchrotron measurements. Especially around 1 GeV, the positron fraction is now rather accurately known, so the interstellar electron flux at this energy can be determined.

We note that similar calculations of the electron spectrum have been made by Porter & Protheroe (1997) using a (one-dimensional) Monte Carlo approach. They also address the Galactic diffuse gamma-ray spectrum. However, since the main subject of the present paper is positrons, a detailed comparison of our electron and gamma-ray spectra with theirs will be made elsewhere (Strong & Moskalenko 1997b).

# 2.DESCRIPTION OF THE MODELS

The models will be described in full detail elsewhere (Strong & Moskalenko 1997b; see also the information in  $\S 7$ ); here we summarize briefly their basic features. The models are three dimensional, with cylindrical symmetry in the Galaxy, and the basic coordinates are  $(R,z,p)$ , where  $R$  is the Galactocentric radius,  $z$  is the distance from the Galactic plane, and  $p$  is the total particle momentum. The distance from the Sun to the Galactic center is taken to be  $8.5\mathrm{kpc}$ . In the models, the propagation region is bounded by  $R = R_{h}$ ,  $z = z_{h}$  beyond which free escape is assumed. We take  $R_{h} = 30\mathrm{kpc}$ . The case  $z_{h} = 3\mathrm{kpc}$  has been studied since this is consistent with studies of radioactive nuclei (the

$^{10}\mathrm{Be} / \mathrm{Be}$  ratio; Lukasiak et al. 1994) and synchrotron radiation. For a given  $z_{h}$ , the diffusion coefficient as a function of momentum is determined by B/C for the case of no reacceleration; with reacceleration, on the other hand, it is the reacceleration strength (related to the Alfven speed) that is determined by B/C. Reacceleration provides a natural mechanism to reproduce the B/C ratio without an ad hoc form for the diffusion coefficient (Simon & Heinbach 1996; Heinbach & Simon 1995; Seo & Ptuskin 1994; Letaw, Silberberg, & Tsao 1993). The spatial diffusion coefficient for no reacceleration is taken to be  $\beta D_0$  below rigidity  $\rho_0$ ,  $\beta D_0(\rho /\rho_0)^{\delta}$  above rigidity  $\rho_0$ . The spatial diffusion coefficient with reacceleration assumes a Kolmogorov spectrum of weak MHD turbulence so  $D = \beta D_0(\rho /\rho_0)^{\delta}$  with  $\delta = \frac{1}{3}$  for all rigidities. For the case of reacceleration, the momentum-space diffusion coefficient  $D_{pp}$  is related to the spatial coefficient using the formula given by Seo & Ptuskin (1994) (their eq. [9]) and Berezinskii et al. (1990). The main free parameter in this relation is the Alfven speed  $v_{\mathrm{A}}$ . The injection spectrum of nucleons is assumed to be a power law in momentum for the different species,  $dq(p) / dp\propto p^{-\gamma}$  for the injected density, corresponding to an injected flux  $dF(p)/dp\propto \beta p^{-\gamma}$  or  $dF(E_k) / dE_k\propto p^{-\gamma}$  since  $dp / dE_{k} = A / \beta$ , where  $E_{k}$  is the kinetic energy per nucleon,  $\beta = v / c$ . The value of  $\gamma$  can vary with species. The interstellar hydrogen distribution uses information from H I surveys (Gordon & Burton 1976; Cox, Krugel, & Mezger 1986) for the atomic component and CO surveys (Bronfmann et al. 1988) for the molecular hydrogen; we use information on the ionized component also. The helium fraction of the gas is taken to be 0.11. The interstellar radiation field for inverse Compton losses is based on stellar population models and IRAS (Bloemen, Deul, & Thaddeus 1990) and COBE (Boulanger & Desert 1992) analyses; in addition, we include the cosmic micro

wave background. The magnetic field is assumed to have the form  $B_{\perp} = 6e^{-|z| / 5\mathrm{kpc} - \overline{R} /20\mathrm{kpc}}\mu \mathrm{G}$ . This magnetic field model is based on recent observational work (Vallee 1994; Heiles 1996), and our local field of  $4\mu \mathrm{G}$  is consistent with these papers. The  $z$ -variation was chosen to follow studies of radio synchrotron surveys, which suggest a vertical extent of emissivity of several kiloparsecs (Phillips et al. 1981) and hence a comparable extent of both field and electrons. Energy losses for the electrons by ionization, Coulomb interactions, bremsstrahlung, inverse Compton effect, and synchrotron radiation are included. The inverse Compton losses were computed using the Thomson approximation, which is sufficient for our purposes. The Klein-Nishina corrections affect only electrons of energies above  $100\mathrm{GeV}$  interacting with optical photon fields, while we are interested here in electron and positron energies below  $100\mathrm{GeV}$ , and in any case far-infrared photons dominate the interstellar radiation energy density. Energy losses for nucleons by ionization and Coulomb interactions are included following Mannheim & Schlickeiser (1994). The distribution of cosmic-ray sources is chosen to reproduce the cosmic-ray distribution determined by analysis of EGRET gamma-ray data (Strong & Mattox 1996).

First, the primary propagation is computed by giving the primary distribution as a function of  $(R,z,p)$ , then the secondary source function is obtained from the gas density and cross sections, and finally the secondary propagation is computed. The entire calculation is performed with momentum as the kinematic variable, since this greatly facilitates the inclusion of reacceleration. Nucleon spectra are converted to  $dF(E_k) / dE_k$  afterward for comparison with observations.

# 3. MODEL PARAMETERS

Table 1 lists the parameters that were used for the models with and without reacceleration. The cross sections for secondary production from the progenitor  $C$ ,  $N$ ,  $O$  were taken from Webber, Lee, & Gupta (1992), Heinbach & Simon (1995), and references therein. The source relative abundances were taken from Engelmann et al. (1990). The injection spectrum for carbon was taken to be  $dq(p) / dp \propto p^{-2.35}$  for the case of no reacceleration and  $p^{-2.25}$  with reacceleration. These values are consistent with Engelmann et al. (1990), who give an injection index  $2.23 \pm 0.05$ .

Figure 1 shows the predicted and observed B/C ratio for the adopted parameters. We use the Voyager data from Webber et al. (1996). The spectra were modulated to 500 MV, appropriate to the Voyager data, by using the force field approximation (Gleeson & Axford 1968). The agreement is sufficiently good for our purpose of computing the secondary positrons. We can note that below 1 GeV the better fit is given by the reacceleration model (which also has one less free parameter), but this has no effect on the positron calculation. Inclusion of a convective term would be necessary to improve the fit in this region for the no reacceleration case.

The proton and helium spectra are computed as a function of  $(R, z, p)$  by the propagation code. Figure 2 shows the predicted and observed proton and helium spectra. The injection spectrum is adjusted to give a good fit to the locally measured spectrum, normalizing at  $10\mathrm{GeV}$  nucleon $^{-1}$ . For protons, we use the data of Seo et al. (1991, Fig. 10a) based on LEAP and IMP8 balloon measurements, and Mori's (1997) "median" flux (his eq. [3]). For helium,

TABLE1 PARAMETERSOFMODELS  

<table><tr><td rowspan="2">MODEL</td><td rowspan="2">zh(kpc)</td><td rowspan="2">D0(cm2s-1)</td><td rowspan="2">ρ0(MV/c)</td><td rowspan="2">δ</td><td rowspan="2">vA(km s-1)</td><td colspan="3">PROTONS</td><td colspan="3">HELIUM</td></tr><tr><td>γ</td><td>p0a</td><td>I0b</td><td>γ</td><td>p0a</td><td>I0b</td></tr><tr><td>08–005......</td><td>3</td><td>2.0 × 1028</td><td>3.0 × 103</td><td>0.60</td><td>0</td><td>2.15</td><td>104</td><td>3 × 10-6</td><td>2.35</td><td>4 × 104</td><td>4 × 10-8</td></tr><tr><td>08–006......</td><td>3</td><td>4.2 × 1028</td><td>3.0 × 103</td><td>0.33</td><td>20</td><td>2.25</td><td>104</td><td>3 × 10-6</td><td>2.45</td><td>4 × 104</td><td>4 × 10-8</td></tr><tr><td>08–009......</td><td>3</td><td>2.0 × 1028</td><td>3.0 × 103</td><td>0.60</td><td>0</td><td>2.00</td><td>104</td><td>3 × 10-6</td><td>2.00</td><td>4 × 104</td><td>4 × 10-8</td></tr></table>

NOTE. Models 08-005 and 08-009 are without reacceleration; model 08-006 is with reacceleration. The spatial diffusion coefficient for no reacceleration is  $\beta D_0$  below rigidity  $\rho_0$  and  $\beta D_0(\rho /\rho_0)^\delta$  above rigidity  $\rho_0$ . The spatial diffusion coefficient with reacceleration is  $\beta D_0(\rho /\rho_0)^\delta$  for all rigidities. The nucleon injection density spectrum is  $dq(p) / dp\propto p^{-\gamma}$ . The nucleon spectra is normalized to flux  $I_{0}$  at momentum  $p_0$ .  
a In units of MeV/c nucleus-1.  
b In units of  $\mathrm{cm}^{-2}\mathrm{s}^{-1}\mathrm{sr}^{-1}$  (MeV/c nucleus $^{-1}$ ) $^{-1}$ .

we use the data of Engelmann et al. (1985, Fig. 11) (HEAO A3) and the interstellar spectrum given by Seo et al. (1991, Fig. 11a).

For the injection spectra of protons, we find that  $\gamma = 2.15$  reproduces the observed spectra in the case of no reacceleration, and that  $\gamma = 2.25$  reproduces the observed spectra in the case with reacceleration. We find that it is necessary to use slightly steeper (0.2 in the index) injection spectra for helium nuclei (see Table 1) in order to fit the observed spectra in the  $1 - 100\mathrm{GeV}$  range of interest for positron production. The spectra fit up to about  $100\mathrm{GeV}$ , beyond which the helium spectrum without reacceleration becomes too steep and the proton spectrum with reacceleration too flat; these deviations are of no consequence for the positron calculation. Although the nucleons are not the main subject of this study, we note that the reacceleration model reproduces slightly better the observed spectrum below  $10\mathrm{GeV}$  nucleon $^{-1}$ , where the interstellar power law in momentum continues down to  $2\mathrm{GeV}$  nucleon $^{-1}$  before bending over (Seo et al. 1991). The adopted nucleon spectra successfully reproduce the  $100 - 1000\mathrm{MeV}$  gamma-ray intensity from  $\pi^0$  decay (Strong et al. 1996; Strong & Moskalenko 1997a;

![](images/5d147e11bf2ca6759f64cb58199965430d8863987928623ca4f010faf726d7c6.jpg)  
FIG. 1.-B/C ratio. Thick solid line: model with no reacceleration, nucleon injection spectrum index 2.35. Thin solid line: model with reacceleration, nucleon injection spectrum index 2.25. Dashed lines: modulated to  $500\mathrm{MV}$ . The data is from Voyager (Webber et al. 1996).

Strong, Moskalenko, & Schonfelder 1997), so that we are not dependent on the locally measured nucleon spectra for the positron calculation only, but have evidence that it extends throughout the Galaxy. Possible gamma-ray evidence for a flatter nucleon spectrum (Hunter et al. 1997) and the consequences for positrons are addressed in § 6.

For the primary electrons, an injection index of 2.1 below  $10\mathrm{GeV}$ , steepening to 2.4 above  $10\mathrm{GeV}$ , was found to reproduce the observed spectrum up to  $30\mathrm{GeV}$  and is consistent with gamma-ray and synchrotron radiation studies (Strong & Moskalenko 1997a). At higher energies, a further steepening is required, but this is not of consequence here. The flux normalization was chosen to fit direct measurements and the positron ratio as described in  $\S 5$ :  $I_{e}(E) = 3.2 \times 10^{-8} \mathrm{~cm}^{-2} \mathrm{~s}^{-1} \mathrm{sr}^{-1} \mathrm{MeV}^{-1}$  at  $9\mathrm{GeV}$ .

# 4. PRODUCTION OF SECONDARY POSITRONS AND ELECTRONS

The production of positrons in collisions of cosmic-ray protons with protons of the interstellar medium has been discussed in detail in numerous studies (e.g., Stecker 1970; Orth & Buffington 1976; Protheroe 1982; Dermer 1986a, 1986b; Murphy, Dermer, & Ramaty 1987; and references therein). The muons created through decays of secondary pions and kaons are fully polarized, which results in electron/positron decay asymmetry, which in turn causes a difference in their production spectra. In the early papers (Orth & Buffington 1976), the muon decay asymmetry was treated identically for positrons and electrons (our paper:  $\xi = -1$  in eq. [C1]), which leads to almost a factor 2 lower positron production at high energies. Subsequent papers appear to have repeated this mistake (e.g., Protheroe 1982). The difference in  $\mu^{+}$  and  $\mu^{-}$ decay asymmetry as applied to positron and electron production was noted by Dermer (1986a), but no attempts to improve the predicted cosmicray positron spectrum seem to have been made. Additionally, the energy spectra of positrons produced in collisions of isotropic monoenergetic protons with protons at rest calculated by Murphy et al. (1987), although in general agreement with our calculations, still differ in detail. In particular, they agree better with our calculations using an isotropic distribution of positrons in the muon rest system. Since positron/electron production and propagation in the Galaxy is among the hot topics of cosmic-ray physics, we give explicitly our formulae for the positron/ electron production spectrum (see appendices).

The energy spectra of positrons ( $\xi = 1$  in eq. [C1]) and electrons ( $\xi = -1$ ) from the decay of  $\pi^{\pm}$ ,  $K^{\pm}$  mesons produced in collisions of isotropic monoenergetic protons with

![](images/76bfedbcd0de93f8d4c753da103046dc195e1e740bcfd3b1ee88e0ddbb3e2de8.jpg)  
FIG. 2.-Left panel: spectra of protons. Thick solid line: model with no reacceleration, injection spectrum index 2.15. Thin solid line: model with reacceleration, injection spectrum index 2.25. Dashed line: "interstellar" (Seo et al. 1991). Dash-dotted line: Mori (1997) median spectrum. Right panel: spectra of helium. Thick solid line: model with no reacceleration, injection spectrum index 2.35. Thin solid line: model with reacceleration, injection spectrum index 2.45. Dashed line: "interstellar" (Seo et al. 1991). Dash-dotted line: Engelmann et al. (1985).

![](images/b6b8f4190e0e7a127ae8d6d20c5371ec1921d26fae66084b3f056f719add6541.jpg)

protons at rest are shown in Figure 3 for several values of the kinetic energy of protons. For comparison, we show the spectra of positrons that are calculated assuming an isotropic distribution in the muon rest system,  $\xi = 0$ , and also

using  $\xi = -1$ ; the latter corresponds to the formula used by Orth & Buffington (1976). Remarkably, the latter one produces more positrons at maximum (around 30 MeV) compared with the correct positron spectrum, while it gives

![](images/0d997e9fce5388a59a690c99c8f366b5a22fec4799c7043fe5972530e9e21680.jpg)  
FIG. 3.-Left panel: the solid lines show the energy spectra of positrons from the decay of  $\pi^{+}$ ,  $K^{+}$  produced in collisions of isotropic monoenergetic protons with protons at rest for various proton kinetic energies (from bottom to top):  $\epsilon_{p} - m_{p} = 0.316$ , 0.383, 0.464, 0.562, 0.681, 1.0, 1.78, 3.16, 10.0, and 100.0 GeV ( $\xi = 1$ , eq. [C1]). The dashed lines show the spectra calculated assuming an isotropic distribution of  $e^{+}$  in the muon rest system ( $\xi = 0$ ) for some proton kinetic energies only. The dotted lines show the spectra calculated for  $\xi = -1$ , corresponding to the distribution used by Orth & Buffington (1976, their eq. [D9]). Right panel: energy spectra of electrons from the decay of  $\pi^{-}$ ,  $K^{-}$  produced in collisions of isotropic monoenergetic protons with protons at rest for several proton kinetic energies (from bottom to top): 1.0, 1.21, 1.47, 2.15, 3.16, 4.64, 10.0, 21.5, 46.4, and 100.0 GeV ( $\xi = -1$ ).

![](images/9f19b26531e5a68b766355bbe962d93663ba1053eeae85e74ae59589149fcc6b.jpg)

![](images/b20ab87a159c8bb31c54879970715db6a488a7a8dc64a15bbd4244e1d995a07c.jpg)  
FIG. 4.—Illustration of the effect of the different positron distributions in the muon rest system. The thick solid lines show the production spectrum of secondary positrons and electrons per hydrogen atom for the cosmic-ray proton spectrum given by Mori (1997). The positron spectrum with no kaon contribution is shown by the dash-dotted line. The dashed line shows the spectrum calculated assuming an isotropic distribution of  $e^{+}$  in the muon rest system ( $\xi = 0$ ); the dotted line shows the spectrum calculated for  $\xi = -1$ . The thin solid line with hatched regions shows the positron production rate by cosmic rays in the interstellar medium (including the contribution of He nuclei) from Protheroe (1982).

half the positron yield at high energies. The curve corresponding to the isotropic distribution lies exactly in between the two others.

The effect is also clearly seen when integrating over the spectrum of cosmic-ray protons (Fig. 4), where we adopted for illustration the spectrum by Mori (1997), in units of  $\mathrm{cm}^{-2}\mathrm{s}^{-1}\mathrm{GeV}^{-1}:J_{p} = 1.67p_{p}^{-2.7}[1 + (2.5\mathrm{GeV} / c)^{2} / p_{p}^{2}]^{-1 / 2}$  below  $100\mathrm{GeV}$  and  $J_{p} = 6.65\times 10^{-6}(\epsilon_{p} / 100\mathrm{GeV})^{-2.75}$  above  $100\mathrm{GeV}$ . The difference in the positron production spectra for the  $\xi = 1$  and  $\xi = -1$  cases reaches a factor 1.6 above  $\sim 0.2\mathrm{GeV}$ . It supports the conclusion made by Orth & Buffington (1976) that the neglect of the muon decay asymmetry can result in a  $25\%$  error in the positron production spectrum, but curiously the inclusion of the correct kinematics leads to an increase of the positron yield at high energies, just the reverse of their inference. The effect of kaon decay is of minor importance. We included only the most important channel,  $K^{\pm}\rightarrow \mu^{\pm} + \nu_{\mu}$ ; the others would contribute at the few percent level. A comparison with the positron production rate from Protheroe (1982) illustrates the statement above: it generally agrees with our calculations for the case  $\xi = -1$ , also taking into account that his calculations include a contribution of He nuclei in cosmic rays and interstellar matter. Our curves are shown for pure pp-interactions, while inclusion of He would give a factor of  $\approx 1.4$  increase (e.g., Dermer 1986b). Some discrepancy could be connected with uncertainties in the extrapolation of the inclusive cross section used by Protheroe at high energies and the interaction dynamics. The uncertainty at low energies (hatched area) is due to uncertainty in the demodulation of the proton spectrum.

Our calculations of the interstellar  $e^{\pm}$  spectra include the contribution to  $\pi^{\pm}$  production from the channels  $p + \mathrm{He}, \alpha + \mathrm{H},$  and  $\alpha + \mathrm{He}$ . For collisions involving nuclei with atomic numbers  $A > 1$ , the corresponding cross section is multiplied by a factor  $(A_1^{3/8} + A_2^{3/8} - 1)^2$  (Orth & Buffington 1976; Dermer 1986a), while the energy per nucleon is still the kinematic variable.

# 5. INTERSTELLAR POSITRON AND ELECTRON SPECTRA

Figure 5 shows the computed secondary positron and electron spectra for the cases with and without reacceleration. The primary electron spectrum and the total electron  $+$  positron spectrum are also shown. Above a few GeV where solar modulation is small, the agreement with the absolute positron measurements is good within the large experimental errors. Unfortunately, there are few absolute measurements of the positron spectrum, and we have to rely mainly on the positron fraction for comparison. First, in Figure 6, we show the results plotted as the positron fraction using the total electron spectrum from Protheroe (1982). Next, Figure 7 shows the positron fraction, but using our computed interstellar primary electron spectrum. None of the computed positron spectra or positron fractions are seriously in conflict with the observations. Between 1 and  $10\mathrm{GeV}$ , the agreement is very good and the measured data rather precise. Above  $10\mathrm{GeV}$ , there appears to be an excess above the predicted ratio, although the observational errors are larger. Below a few GeV, solar modulation will shift the points to lower energy, but the implications for modulation models are beyond the scope of this paper.

$\varepsilon^2 I$  , MeV cm-2 sr-1 s-1

![](images/a05101d8173eb393d38fbe1dff244e58ebd7d22366e4bbcfc62d375788981f88.jpg)

$\varepsilon^2 I$  , MeV cm-2 sr-1 s-1

![](images/f049b85814ec257ec5b9b1a8c08a0ee87e513a2cd8d29a6bd5a6391bda1f18f0.jpg)  
FIG. 5.-Spectra of secondary positrons and electrons and of primary electrons. Top panel: model with no reacceleration (08-005). The electron injection spectrum indices are 2.1 and 2.4 below and above  $10\mathrm{GeV}$ , respectively. Upper curves: primary electrons and primary + secondary electrons and positrons. Lower curves: secondary positrons and electrons. Lower dash-dotted line: Protheroe (1982) leaky box prediction. Electron data: Buffington, Orth, & Smoot (1975), Golden et al. (1984, 1994), Taira et al. (1993), Ulysses (Ferrando et al. 1996). Upper dash-dotted line: Protheroe (1982). Positron data: Fanselow et al. (1969), Buffington et al. (1975), Golden et al. (1987, 1994). Bottom panel: same, but for the model with reacceleration (08-006).

$$
e ^ {+} / (e ^ {+} + e ^ {-})
$$

![](images/e64688e75a8e8b7a2b4025c7bbc89632d5263e4f0e4db4cff011ed10d4ff68ed.jpg)

$$
e ^ {+} / (e ^ {+} + e ^ {-})
$$

![](images/f1946d2046ccd34017d66a4077435f8a576840b7d8598fd0cbaf1ea045026d88.jpg)  
FIG. 6.—Top panel: positron fraction for model with no reacceleration. The positron spectrum is divided by the electron spectrum used by Protheroe (1982). Dot-dashed line: positron fraction from Protheroe (1982): leaky box (dash-dotted), diffusion (dashed). The collection of the experimental data is taken from Barwick et al. (1997). Bottom panel: same positron fraction for model with reacceleration.

$$
e ^ {+} / (e ^ {+} + e ^ {-})
$$

![](images/13cafcfcb34e2e4ea1420dec3ff6cd6d0569e401656335949327bbc546769bf9.jpg)

$$
e ^ {+} / \left(e ^ {+} + e ^ {-}\right)
$$

![](images/e3584c3865f5989c9b496319311c8ade4df92321303ae75547a386cd42861301.jpg)  
FIG. 7.—Top panel: positron fraction for model with no reacceleration. The positron spectrum is divided by the electron spectrum computed in the propagation model. The data and other curves are the same as in Fig. 6. Bottom panel: same positron fraction for model with reacceleration.

![](images/b47539d43154f552f7ed86de7e2ad5141b6dacd643b6f5736e787d8a9f2c41e8.jpg)

$$
e ^ {+} / (e ^ {+} + e ^ {-})
$$

![](images/2f65586a78fe6ffe9886cfc6878f70b7ffff72add9fb69ae607878bb800e2376.jpg)  
FIG. 8. Top panel: spectrum of protons for a "flat" injection spectrum. Thick solid line: model with no reacceleration (08-009); injection spectrum index 2.0. The other spectra are the same as in Fig. 2. Bottom panel: positron fraction for this nucleon spectrum. The data are the same as in Fig. 6.

Reacceleration produces a more peaked positron spectrum, with the peak positron fraction around 600 MeV compared with 400 MeV without reacceleration. Although the better fit to the positron fraction is given by the model without reacceleration (Fig. 6), this depends critically on the measured electron spectrum that is not known to sufficient accuracy to allow a distinction between the models on this basis. While our nonreacceleration electron spectrum is compatible with Galactic gamma rays from 1 to 1000 MeV and radio synchrotron data down to 38 MHz (Strong & Moskalenko 1997a; Strong et al. 1997), the reacceleration spectrum may not be consistent with such data. In any case, it will be possible to put critical constraints on electron reacceleration by using gamma-ray and radio data, and this will be investigated in future work (Strong & Moskalenko 1997b). Note that Protheroe (1982) uses a radio-based electron spectrum below 1 GeV, but this is increasingly uncertain at lower energies due to free-free absorption of radio emission.

Our positron spectrum without reacceleration is steeper than that computed by Protheroe (1982); ours is a factor 2 higher at  $1\mathrm{GeV}$  and is about equal to his at  $10\mathrm{GeV}$ . A factor of 2 and part of the steeper slope can be traced to a difference in the production function (see Fig. 4), and the remaining difference must be attributed to many details in the different propagation models (diffusion coefficient, halo size, gas density, radiation fields, three-dimensional vs. one-dimensional models). Taking these reasons into account, the calculations are consistent, and it is gratifying that the difference is relatively small. However, the new calculations are able to benefit from better knowledge of the nucleon spectrum and of cosmic-ray propagation.

Above 10 GeV, the predicted positron flux appears too low, and the agreement is not better than for Protheroe (1982). This would be a hint for primary positrons or a harder interstellar nucleon spectrum (see § 6) than is observed locally, and it emphasizes the importance of accurate positron measurements in this range. At energies below 1 GeV where solar modulation is large, our interstellar positron spectrum should provide a good basis for modulation studies.

As promised in § 1, we can use these results to turn the argument around and draw conclusions about the interstellar electron spectrum using the calculated secondary positrons and the measured positron fraction. In Figure 7, we divide the computed positrons by the modeled primary electron spectrum plus the secondary  $e^{\pm}$ ; the agreement with the measured positron fraction shows that either of the modeled primary electron spectra (Fig. 5) are acceptable in the range 0.1–10 GeV. They are consistent with the direct measurements of the primary spectrum. The model without reacceleration, however, is lower by a factor of about 2 than that required to fit the COMPTEL and EGRET gamma-ray spectrum (see Strong & Moskalenko 1997a); nevertheless, an intermediate spectrum would be consistent with both positrons and gamma rays within the uncertainties of each. The model with reacceleration may not be compatible with gamma-ray and radio data, as mentioned above.

# 6. A HARDER INTERSTELLAR NUCLEON SPECTRUM?

The fit to the positron fraction above 10 GeV could be improved by an ad hoc steepening of the electron spectrum,

but this would then disagree with the direct electron measurements that are rather reliable in this range. Another possibility that we find interesting is to adopt harder interstellar proton and helium spectra. Figure 8 shows the proton spectrum and positron fraction for an injection spectral index  $\gamma = 2.0$  (model 08-009, no reacceleration). The primary electron normalization for this case was adjusted to  $I_{e}(E) = 3.44\times 10^{-8}\mathrm{cm}^{-2}\mathrm{s}^{-1}\mathrm{sr}^{-1}\mathrm{MeV}^{-1}$  at 9 GeV to obtain the best overall fit. This model reproduces the positron fraction well over the whole range; in particular, the data above 10 GeV from the recent HEAT balloon experiment (Barwick et al. 1997) are fitted (note that the higher positron fractions from earlier experiments can probably be attributed to the difficulty of distinguishing positrons from protons). The ambient proton spectral index after propagation is about 2.6 in this model, compared with the directly measured value of 2.75. This is especially interesting in view of the independent result from EGRET diffuse Galactic gamma-ray data (Hunter et al. 1997) that the gamma-ray spectrum above 1 GeV is harder than expected for the locally measured nucleon spectrum (Mori 1997; Gralewicz et al. 1997). Mori (1997) finds that an ambient spectral index of 2.41-2.55 is required to fit the gamma-ray spectrum, which is consistent with that required for the positrons. Thus, our result can be viewed as adding some support to the "hard nucleon spectrum" interpretation of the gamma-ray results, and for the idea that the Galactic interstellar proton and helium spectra are harder than those measured in the heliosphere. However, since this situation is a priori unlikely in conventional models of cosmic-ray propagation and from cosmic-ray anisotropy arguments, it remains an interesting possibility that deserves further investigation and independent tests. If correct, it would explain the positron data without the requirement for a source of primary positrons.

# 7. CONCLUSIONS

We have carried out a new computation of the secondary positron and primary electron spectra in a self-consistent model of propagation that includes nucleons. The model is more realistic than previous leaky box-type calculations and incorporates a wider range of astrophysical input. We have shown that the positron fraction is consistent with measurements up to  $10\mathrm{GeV}$ , beyond which some excess is apparent. We have also shown that it is possible to reverse the normal argumentation in order to constrain the interstellar electron spectrum on the basis of the measured positron fraction and the computed positron spectrum. The resulting interstellar electron spectrum for  $1 - 10\mathrm{GeV}$  is consistent with that from direct measurements. A harder interstellar nucleon spectrum allows the positron fraction to be fitted above  $10\mathrm{GeV}$  and would also explain the high-energy, diffuse Galactic gamma-ray spectrum; thus, two independent lines of evidence point to a flatter nucleon spectrum than that directly measured, so that this possibility has to be taken seriously and further consequences examined. At energies below  $1\mathrm{GeV}$ , our calculated positron spectrum will be of interest for studies of cosmic-ray modulation in the heliosphere.

More details, including the software and data sets, can be found on the World Wide Web.

# APPENDIX A

# SPECTRA OF SECONDARIES FROM  $pp$ -COLLISIONS

The production spectrum of secondary gamma rays, electrons, and positrons can be obtained if one knows the distributions of pions  $F_{\pi}(\epsilon_{\pi}, \epsilon_{p})$  and kaons  $F_{K}(\epsilon_{K}, \epsilon_{p})$  from a collision of a proton of energy  $\epsilon_{p}$ , and the distribution of secondaries  $F_{s}(\epsilon_{s}, \epsilon_{\pi, K})$  from the decay of a pion/kaon of energy  $\epsilon_{\pi, K}$ :

$$
j _ {s} \left(\epsilon_ {s}\right) = n _ {\mathrm {H}} \sum_ {i = \pi , K} \int_ {\epsilon_ {p} \min } ^ {\infty} d \epsilon_ {p} J _ {p} \left(\epsilon_ {p}\right) \left\langle \eta \sigma_ {i} \left(\epsilon_ {p}\right) \right\rangle \int_ {\epsilon_ {i} \min  \left(\epsilon_ {s}\right)} ^ {\epsilon_ {i} \max  \left(\epsilon_ {p}\right)} d \epsilon_ {i} F _ {s} \left(\epsilon_ {s}, \epsilon_ {i}\right) F _ {i} \left(\epsilon_ {i}, \epsilon_ {p}\right), \tag {A1}
$$

where  $n_{\mathrm{H}}$  is the atomic hydrogen number density,  $J_{p}(\epsilon_{p})$  is the proton flux, and  $\langle \eta \sigma_{\pi ,K}(\epsilon_p)\rangle$  is the inclusive cross section of pion/kaon production (a convenient parameterization for different channels is given by Badhwar, Stephens, & Golden 1977 and Dermer 1986a). The minimum proton energy  $\epsilon_p^{\mathrm{min}}$  that contributes to the production of a meson with energy  $\epsilon_i^{\mathrm{min}}$  and the maximal energy of the produced meson  $\epsilon_i^{\mathrm{max}}(\epsilon_p)$  can be easily derived from kinematical considerations, e.g., by equating  $\sqrt{s} = [2m_p(\epsilon_p + m_p)]^{1 / 2} = (m_X^2 +\epsilon_i^{*2} - m_i^2)^{1 / 2} + \epsilon_i^*$ , where  $s$  is the square of the total energy in the center-of-mass system (CMS),  $m_X$  depends on the reaction channel, and  $\epsilon_i^*$  is the CMS energy of the produced meson (connected with the laboratory system energy  $\epsilon_{i}$  via the Lorentz transformation). The minimum meson energy that contributes to the production of a secondary with energy  $\epsilon_s$  is given by  $\epsilon_{\pi^0}^{\mathrm{min}}(\epsilon_\gamma) = \epsilon_\gamma +m_{\pi^0} / (4\epsilon_\gamma)$  for gamma rays;  $\epsilon_{\pi^{\pm},K^{\pm}}^{\mathrm{min}} = m_{\pi^{\pm},K^{\pm}}$  for  $\epsilon_e\leq E\equiv \frac{1}{2} m_\mu \gamma_\mu '(1 + \beta_\mu ')$  and  $\epsilon_{\pi^{\pm},K^{\pm}}^{\mathrm{min}}(\epsilon_e) = \frac{1}{2} m_{\pi ,K}(\epsilon_e / E + E / \epsilon_e)$  if  $\epsilon_e > E$ , where  $\gamma_{\mu}^{\prime}$  and  $\beta_{\mu}^{\prime}$  are the muon Lorentz factor and speed in the meson rest system, respectively (see below).

# APPENDIX B

# PION PRODUCTION IN  $pp$ -COLLISIONS

We consider pion production in  $pp$ -collisions following a method developed by Dermer (1986a, 1986b), which combines isobaric (Stecker 1970) and scaling (Badhwar et al. 1977; Stephens & Badhwar 1981) models of the reaction. The isobaric model was shown to work well at low energies, while at high energies the relevant model is based on scaling arguments. In the transition region, we join the models with a linear connection in the regime between 3 and 7 GeV. The contribution of the  $pp \rightarrow \pi^{+}d$  channel is included separately.

# B1. STECKER'S MODEL

Assuming that the outgoing  $\Delta$ -isobar of mass  $m_{\Delta}$  travels along the initial direction of the colliding protons in the CMS and decays isotropically, the distribution of the  $\pi$ 's in the laboratory system (LS) is

$$
\left. \right. f _ {\pi} \left(\epsilon_ {\pi}, \epsilon_ {p}; m _ {\Delta}\right) = \frac {1}{4 m _ {\pi} \gamma_ {\pi} ^ {\prime} \beta_ {\pi} ^ {\prime}} \left\{\frac {1}{\gamma_ {\Delta} ^ {+} \beta_ {\Delta} ^ {+}} H \left[ \gamma_ {\pi}; \gamma_ {\Delta} ^ {+} \gamma_ {\pi} ^ {\prime} \left(1 - \beta_ {\Delta} ^ {+} \beta_ {\pi} ^ {\prime}\right), \gamma_ {\Delta} ^ {+} \gamma_ {\pi} ^ {\prime} \left(1 + \beta_ {\Delta} ^ {+} \beta_ {\pi} ^ {\prime}\right)\right] + \frac {1}{\gamma_ {\Delta} ^ {-} \beta_ {\Delta} ^ {-}} H \left[ \gamma_ {\pi}; \gamma_ {\Delta} ^ {-} \gamma_ {\pi} ^ {\prime} \left(1 - \beta_ {\Delta} ^ {-} \beta_ {\pi} ^ {\prime}\right), \gamma_ {\Delta} ^ {-} \gamma_ {\pi} ^ {\prime} \left(1 + \beta_ {\Delta} ^ {-} \beta_ {\pi} ^ {\prime}\right)\right]\right\}, \tag {B1}
$$

where  $H[x;a,b] = 1$  if  $a\leq x\leq b$  and  $= 0$  otherwise,  $\epsilon_{\pi}$  is the pion energy, and  $\epsilon_{p}$  is the LS energy of the colliding proton. The Lorentz factors of the forward (plus sign) and backward (minus sign) moving isobars in the LS are  $\gamma_{\Delta}^{\pm} = \gamma_{c}\gamma_{\Delta}^{*}(1\pm \beta_{c}\beta_{\Delta}^{*})$  where  $\gamma_c = \sqrt{s} /2m_p$  is the Lorentz factor of the CMS in the LS, and  $\gamma_{\Delta}^{*} = (s + m_{\Delta}^{2} - m_{p}^{2}) / 2\sqrt{s} m_{\Delta}$  is the Lorentz factor of the isobar in the CMS. The pion Lorentz factor in the rest frame of the  $\Delta$  -isobar is  $\gamma_{\pi}^{\prime} = (m_{\Delta}^{2} + m_{\pi}^{2} - m_{p}^{2}) / 2m_{\Delta}m_{\pi}$ .

Integration over the isobar mass spectrum (Breit-Wigner distribution) yields the distribution of pions:

$$
F _ {\pi} \left(\epsilon_ {\pi}, \epsilon_ {p}\right) = \Gamma \left[ \tan^ {- 1} \left(\frac {\sqrt {s} - m _ {p} - m _ {\Delta} ^ {0}}{\Gamma}\right) - \tan^ {- 1} \left(\frac {m _ {p} + m _ {\pi} - m _ {\Delta} ^ {0}}{\Gamma}\right) \right] ^ {- 1} \times \int_ {m _ {p} + m _ {\pi}} ^ {\sqrt {s} - m _ {p}} d m _ {\Delta} \frac {f _ {\pi} \left(\epsilon_ {\pi} , \epsilon_ {p} ; m _ {\Delta}\right)}{\left(m _ {\Delta} - m _ {\Delta} ^ {0}\right) ^ {2} + \Gamma^ {2}}, \tag {B2}
$$

where  $m_{\Delta}^{0}$  is the average mass of the  $\Delta$ -isobar, and  $\Gamma$  is the width of the Breit-Wigner distribution (note that  $\Gamma$  here is a factor of 2 higher than the value usually given in particle data tables).

# B2. SCALING MODEL

The Lorentz invariant cross sections for charged and neutral pion production in  $pp$ -collisions inferred from experimental data at  $\epsilon_p \gtrsim 13.5$  GeV are given by Badhwar et al. (1977) and Stephens & Badhwar (1981):

$$
\epsilon_ {\pi} \frac {d ^ {3} \sigma}{d ^ {3} p _ {\pi}} = A G _ {\pi} \left(\epsilon_ {p}\right) \left(1 - \tilde {x} _ {\pi}\right) ^ {Q} \exp \left[ - B p _ {\perp / \left(1 + 4 m _ {p} ^ {2} / s\right)} \right], \tag {B3}
$$

where

$$
G _ {\pi \pm} \left(\epsilon_ {p}\right) = \left(1 + 4 m _ {p} ^ {2} / s\right) ^ {- R}, \tag {B4}
$$

$$
G _ {\pi 0} (\epsilon_ {p}) = \left(1 + 2 3 \epsilon_ {p} ^ {- 2. 6}\right) \left(1 - 4 m _ {p} ^ {2} / s\right) ^ {R}, \tag {B5}
$$

$$
Q = \left(C _ {1} - C _ {2} p _ {\perp} + C _ {3} p _ {\perp} ^ {2}\right) / \sqrt {1 + 4 m _ {p} ^ {2} / s}, \tag {B6}
$$

$$
\tilde {x} _ {\pi} = \sqrt {x _ {\parallel} ^ {*} + (4 / s) \left(p _ {\perp} ^ {2} + m _ {\pi} ^ {2}\right)}, \tag {B7}
$$

$$
x _ {\parallel} ^ {*} = \frac {2 m _ {\pi} \sqrt {s} \gamma_ {c} \gamma_ {\pi} \left(\beta_ {\pi} \cos \theta - \beta_ {c}\right)}{\left[ \left(s - m _ {\pi} ^ {2} - m _ {X} ^ {2}\right) ^ {2} - 4 m _ {\pi} ^ {2} m _ {X} ^ {2} \right] ^ {1 / 2}}, \tag {B8}
$$

$\theta$  is the pion LS polar angle,  $A, B, C_{1,2,3}$ , and  $R$  are positive constants, and  $m_X$  depends on the reaction channel:  $m_X = 2m_p$  for reaction  $pp \to \pi^0 X$ ,  $m_X = m_p + m_n$  for  $pp \to \pi^+ X$ ,  $m_X = 2m_p + m_n$  for  $pp \to \pi^- X$ ,  $m_X = m_p + m_n$  for  $pp \to K^+ X$ , and  $m_X = 2m_p + m_k$  for  $pp \to K^- X$ .

The LS energy distribution of pions can be obtained by integration over the LS polar angle:

$$
F _ {\pi} \left(\epsilon_ {\pi}, \epsilon_ {p}\right) = \frac {2 \pi p _ {\pi}}{\left\langle \eta \sigma_ {\pi} \left(\epsilon_ {p}\right) \right\rangle_ {\mathrm {s m}}} \int_ {\cos \theta_ {\max }} ^ {1} d \cos \theta \left(\epsilon_ {\pi} \frac {d ^ {3} \sigma}{d ^ {3} p _ {\pi}}\right), \tag {B9}
$$

where, provided  $-1\leq \cos \theta_{\mathrm{max}}\leq 1$

$$
\cos \theta_ {\max } = \frac {1}{\beta_ {c} \gamma_ {c} p _ {\pi}} \left(\gamma_ {c} \epsilon_ {\pi} - \frac {s - m _ {X} ^ {2} + m _ {\pi} ^ {2}}{2 \sqrt {s}}\right), \tag {B10}
$$

and  $\langle \eta \sigma_{\pi}(\epsilon_p)\rangle_{\mathrm{sm}}$  is the inclusive cross section of pion production in the scaling model.

The charged kaon production is of minor importance in comparison with pion production. The parameters of the Lorentz invariant cross section

$$
\epsilon_ {K} \frac {d ^ {3} \sigma}{d ^ {3} p _ {K}} = A \left(1 - \tilde {x} _ {K}\right) ^ {C} \exp (- B p _ {\perp}) \tag {B11}
$$

are given by Badhwar et al. (1977). The two main decay modes are  $K^{\pm} \rightarrow \mu \nu_{\mu}$  (63.5%) and  $K^{\pm} \rightarrow \pi^{0}\pi^{\pm}$  (21.2%); other modes, with three particles in the final state, contribute at a level of a few percent (Particle Data Group 1990, p. VI.11).

# APPENDIX C

# PION DECAY

The muons from the decay of charged pions are created fully polarized, which results in  $e^{\pm}$  decay asymmetry. The secondary electron/positron distribution in the muon rest system, assuming a massless electron/positron, is given by (Particle Data Group 1990, p. VI.11)

$$
f _ {\xi} ^ {\prime} \left(\epsilon_ {e} ^ {\prime}, \cos \theta^ {\prime}\right) = \frac {8 \epsilon_ {e} ^ {\prime 2}}{m _ {\mu} ^ {3}} \left[ 3 - 4 \frac {\epsilon^ {\prime}}{m _ {\mu}} - \xi \cos \theta^ {\prime} \left(1 - 4 \frac {\epsilon^ {\prime}}{m _ {\mu}}\right) \right], \tag {C1}
$$

where  $\xi = \pm 1$  for  $e^{\pm}$ ,  $\xi = 0$  for the isotropic distribution, and  $\epsilon_{e}^{\prime}$  and  $\theta^{\prime}$  are the electron/positron energy in the muon rest system and polar angle, respectively.

In the LS, the electron/positron distribution is

$$
f _ {\xi} \left(\boldsymbol {\epsilon} _ {e}, \boldsymbol {\epsilon} _ {\mu}\right) = \int_ {\cos \theta_ {L}} ^ {1} d \cos \theta f _ {\xi} ^ {\prime} \left(\boldsymbol {\epsilon} _ {e} ^ {\prime}, \cos \theta^ {\prime}\right) J \left(\frac {\boldsymbol {\epsilon} _ {e} ^ {\prime} , \cos \theta^ {\prime}}{\boldsymbol {\epsilon} _ {e} , \cos \theta}\right), \tag {C2}
$$

where  $\cos \theta_{L} = \max \left[-1, (1 - m_{\mu} / 2\epsilon_{e}\gamma_{\mu}) / \beta_{\mu}\right]$ ,  $\gamma_{\mu}$  and  $\beta_{\mu}$  are the muon Lorentz factor and speed in LS, respectively,  $J$  is the Jacobian

$$
J \left(\frac {\epsilon_ {e} ^ {\prime} , \cos \theta^ {\prime}}{\epsilon_ {e} , \cos \theta}\right) = \frac {\epsilon_ {e}}{\epsilon_ {e} ^ {\prime}} = \frac {1}{\gamma_ {\mu} \left(1 - \beta_ {\mu} \cos \theta\right)}, \tag {C3}
$$

and

$$
\boldsymbol {\epsilon} _ {e} ^ {\prime} = \boldsymbol {\epsilon} _ {e} \gamma_ {\mu} \left(1 - \beta_ {\mu} \cos \theta\right), \quad \cos \theta^ {\prime} = \frac {\cos \theta - \beta_ {\mu}}{1 - \beta_ {\mu} \cos \theta}. \tag {C4}
$$

The LS distribution of  $\mu^{\pm}$  from the  $\pi^{\pm}$  decay is

$$
f _ {\mu} \left(\epsilon_ {\mu}, \epsilon_ {\pi}\right) = \frac {1}{2 m _ {\mu} \gamma_ {\pi} \beta_ {\pi} \gamma_ {\mu} ^ {\prime} \beta_ {\mu} ^ {\prime}}, m _ {\mu} \gamma_ {\mu} ^ {-} \leq \epsilon_ {\mu} \leq m _ {\mu} \gamma_ {\mu} ^ {+}, \tag {C5}
$$

where  $\epsilon_{\mu}$  is the muon LS energy,  $\gamma_{\mu}^{\pm} = \gamma_{\pi}\gamma_{\mu}'(1\pm \beta_{\pi}\beta_{\mu}')$  and  $\gamma_{\mu}'\approx 0.2714$  are the muon Lorentz factor and speed in the pion rest system, respectively, and  $\gamma_{\pi}$  and  $\beta_{\pi}$  are the pion Lorentz factor and speed in the LS, respectively. Therefore, the LS distribution of  $e^{\pm}$  from the decay of pion with Lorentz factor  $\gamma_{\pi}$  is given by

$$
F _ {\xi} \left(\epsilon_ {e}, \epsilon_ {\pi}\right) = \frac {1}{m _ {\mu} \gamma_ {\pi} \beta_ {\pi} \gamma_ {\mu} ^ {\prime} \beta_ {\mu} ^ {\prime}} \left\{ \begin{array}{l l} X _ {\xi} \left(\gamma_ {\mu} ^ {+}\right) - X _ {\xi} \left(\gamma_ {\mu} ^ {-}\right), & 0 \leq \epsilon_ {e} \leq m _ {\mu} / 2 \gamma_ {\mu} ^ {+} \left(1 + \beta_ {\mu} ^ {+}\right), \\ X _ {\xi} \left(\gamma_ {1}\right) - X _ {\xi} \left(\gamma_ {\mu} ^ {-}\right) + Y _ {\xi} \left(\gamma_ {\mu} ^ {+}\right) - Y _ {\xi} \left(\gamma_ {1}\right), & m _ {\mu} / 2 \gamma_ {\mu} ^ {+} \left(1 + \beta_ {\mu} ^ {+}\right) \leq \epsilon_ {e} \leq m _ {\mu} / 2 \gamma_ {\mu} ^ {-} \left(1 + \beta_ {\mu} ^ {-}\right), \\ Y _ {\xi} \left(\gamma_ {\mu} ^ {+}\right) - Y _ {\xi} \left(\gamma_ {\mu} ^ {-}\right), & m _ {\mu} / 2 \gamma_ {\mu} ^ {-} \left(1 + \beta_ {\mu} ^ {-}\right) \leq \epsilon_ {e} \leq m _ {\mu} / 2 \gamma_ {\mu} ^ {-} \left(1 - \beta_ {\mu} ^ {-}\right), \\ Y _ {\xi} \left(\gamma_ {\mu} ^ {+}\right) - Y _ {\xi} \left(\gamma_ {1}\right), & m _ {\mu} / 2 \gamma_ {\mu} ^ {-} \left(1 - \beta_ {\mu} ^ {-}\right) \leq \epsilon_ {e} \leq m _ {\mu} / 2 \gamma_ {\mu} ^ {+} \left(1 - \beta_ {\mu} ^ {+}\right), \end{array} \right. \tag {C6}
$$

where  $\gamma_{1} = \epsilon_{e} / m_{\mu} + m_{\mu} / 4\epsilon_{e}$ , and

$$
X _ {\xi} (\gamma) = \frac {m _ {\mu}}{2} \int^ {\gamma} d \gamma_ {\mu} \int_ {- 1} ^ {1} d \cos \theta f _ {\xi} ^ {\prime} \left(\epsilon_ {e} ^ {\prime}, \cos \theta^ {\prime}\right) J \left(\frac {\epsilon_ {e} ^ {\prime} , \cos \theta^ {\prime}}{\epsilon_ {e} , \cos \theta}\right),
$$

$$
Y _ {\xi} (\gamma) = \frac {m _ {\mu}}{2} \int^ {\gamma} d \gamma_ {\mu} \int_ {1 / \beta_ {\mu} (1 - m _ {\mu} / 2 \epsilon_ {e} \gamma_ {\mu})} ^ {1} d \cos \theta f _ {\xi} ^ {\prime} \left(\epsilon_ {e} ^ {\prime}, \cos \theta^ {\prime}\right) J \left(\frac {\epsilon_ {e} ^ {\prime} , \cos \theta^ {\prime}}{\epsilon_ {e} , \cos \theta}\right). \tag {C7}
$$

After the integration, one can obtain

$$
X _ {\pm} (\gamma) = \frac {4}{9} \left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {2} \left\{\frac {\epsilon_ {e}}{m _ {\mu}} \left[ - 3 2 \gamma^ {3} (1 \pm \beta) + \gamma (2 4 \pm 3 2 \beta) \right] + \gamma^ {2} (2 7 \pm 9 \beta) \mp 9 \ln [ \gamma (1 + \beta) ] \right\}, \tag {C8}
$$

$$
X _ {0} (\gamma) = \left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {2} \left[ \left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) \left(- \frac {1 2 8}{9} \gamma^ {3} + \frac {3 2}{3} \gamma\right) + 1 2 \gamma^ {2} \right], \tag {C9}
$$

$$
Y _ {+} (\gamma) = \frac {1}{1 2} \left\{\left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {3} \left[ 1 6 \ln \left(\frac {\gamma + 1}{\gamma - 1}\right) - 6 4 \gamma (1 - \beta) \right] + \left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {2} \left[ 4 8 \gamma^ {2} (1 - \beta) + 2 4 \ln \left(\frac {\beta}{1 + \beta}\right) \right] - 2 \ln (\gamma \beta) + 1 0 \ln [ \gamma (1 + \beta) ] \right\}, \tag {C10}
$$

$$
\begin{array}{l} Y _ {-} (\gamma) = \frac {1}{3 6} \left\{\left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {3} \left[ - 5 1 2 \gamma^ {3} (1 - \beta) + \gamma (5 7 6 - 3 2 0 \beta) - 4 8 \ln \left(\frac {\gamma + 1}{\gamma - 1}\right) \right] \right. \\ \left. + \left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {2} \left[ 2 8 8 \gamma^ {2} (1 - \beta) - 7 2 \ln \left(\frac {\beta}{1 + \beta}\right) \right] + 6 \ln (\gamma \beta) + 3 0 \ln [ \gamma (1 + \beta) ] \right\}. \tag {C11} \\ \end{array}
$$

$$
Y _ {0} (\gamma) = \frac {1}{1 8} \left\{\left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {3} [ - 1 2 8 \gamma^ {3} (1 - \beta) + \gamma (9 6 - 3 2 \beta) ] + \left(\frac {\epsilon_ {e}}{m _ {\mu}}\right) ^ {2} 1 0 8 \gamma^ {2} (1 - \beta) + 1 5 \ln [ \gamma (1 + \beta) ] \right\}, \tag {C12}
$$

At large Lorentz factors,  $\gamma \gtrsim 20$ , it is necessary to use the series expansions.

The distribution of gamma rays from  $\pi^0$  decay is given by

$$
F _ {\gamma} \left(\epsilon_ {\gamma}, \epsilon_ {\pi 0}\right) = \frac {2}{p _ {\pi}}, \frac {1}{2} m _ {\pi} \gamma_ {\pi} \left(1 - \beta_ {\pi}\right) \leq \epsilon_ {\gamma} \leq \frac {1}{2} m _ {\pi} \gamma_ {\pi} \left(1 + \beta_ {\pi}\right), \tag {C13}
$$

where the factor of 2 accounts for two photons per decay.

# APPENDIX D

# KAON DECAY

The two main kaon decay modes are  $K^{\pm} \rightarrow \mu \nu_{\mu}$  (63.5%) and  $K^{\pm} \rightarrow \pi^{0}\pi^{\pm}$  (21.2%), and thus they also contribute to the secondary  $e^{\pm}$  spectrum. The first mode is similar to  $\pi^{\pm}$  decay, and all formulas presented in the previous section are valid if one replaces index  $\pi$  with  $K$  and takes appropriate values for  $\gamma_{\mu}'$  and  $\beta_{\mu}'$ .

The charged pion distribution from the two-pion decay of the kaon is

$$
f _ {\pi} \left(\epsilon_ {\pi}, \epsilon_ {K}\right) = \frac {1}{2 m _ {\pi} \gamma_ {K} \beta_ {K} \gamma_ {\pi} ^ {\prime} \beta_ {\pi} ^ {\prime}}, m _ {\pi} \gamma_ {\pi} ^ {-} \leq \epsilon_ {\pi} \leq m _ {\pi} \gamma_ {\pi} ^ {+}, \tag {D1}
$$

where  $\epsilon_{\pi}$  is the pion LS energy,  $\gamma_{\pi}^{\pm} = \gamma_{K}\gamma_{\pi}'(1 \pm \beta_{K}\beta_{\pi}')$ ,  $\gamma_{\pi \pm}'$  and  $\beta_{\pi \pm}' \approx 0.8267$  are the charged pion Lorentz factor and speed in the kaon rest system, respectively, and  $\gamma_{K}$  and  $\beta_{K}$  are the kaon Lorentz factor and speed in the LS, respectively. Therefore, the LS distribution of pions from the reaction  $pp \rightarrow K^{\pm}X$  is given by

$$
F _ {\pi} \left(\epsilon_ {\pi}, \epsilon_ {p}\right) = \frac {\pi m _ {K}}{m _ {\pi} \gamma_ {\pi} ^ {\prime} \beta_ {\pi} ^ {\prime}} \left\langle \eta \sigma_ {K} \left(\epsilon_ {p}\right) \right\rangle^ {- 1} \int_ {\epsilon_ {K} ^ {\min } \left(\epsilon_ {\pi}\right)} ^ {\infty} d \epsilon_ {K} \int_ {\cos \theta_ {\max }} ^ {1} d \cos \theta \left(\epsilon_ {K} \frac {d ^ {3} \sigma}{d ^ {3} p _ {K}}\right), \tag {D2}
$$

where  $\cos \theta_{\max}$  is given by equation (B10) with the replacement of the index  $\pi$  with  $K$ , and  $\epsilon_K^{\min}(\epsilon_\pi)$  can be obtained from the equation  $\gamma_\pi m_K = \gamma_\pi' (\epsilon_K^{\min} + \beta_\pi' p_K^{\min})$ .

# REFERENCES

Badhwar, G. D., Stephens, S. A., & Golden, R. L. 1977, Phys. Rev. D, 15, 820  
Barbiellini, G., et al. 1996, A&A, 309, L15  
Barwick, S. W., et al. 1997, ApJ, 482, L191  
Berezinskii, V. S., Bulanov, S., Dogiel, V., Ginzburg, V., & Ptuskin, V. 1990, Astrophysics of Cosmic Rays (Amsterdam: North-Holland)  
Bloemen,H.,Deul,E.R.,& Thaddeus,P.1990,A&A,233,437  
Boulanger, F., & Desert F. X. 1992, in The Infrared and Submillimetre Sky after COBE, ed. M. Signore & C. Dupraz (Dordrecht: Kluwer), 263  
Bronfmann,L.,et al.1988,ApJ,324,248  
Buffington,A.,Orth,C.D.,& Smoot,G.F.1975,ApJ,199,669  
Clem, J. M., et al. 1996, ApJ, 464, 507  
Cox,P.,Krugel,E.,&Mezger,P.G.1986,A&A,155,380

Dermer, C. D. 1986a, ApJ, 307, 47  
1986b,A&A,157,223  
Engelmann, J. J., et al. 1985, A&A, 148, 12  
1990,A&A,233,96  
Fanselow, J. L., et al. 1969, ApJ, 158, 771  
Ferrando, P., et al. 1996, A&A, 316, 528  
Gleeson,L.J.,&Axford,W.I.1968,ApJ,154,1011  
Golden, R. L., et al. 1984, ApJ, 287, 622  
1987,A&A,188,145  
1994,ApJ,436,769  
1996,ApJ,457,L103  
Gordon,M.A.,&Burton,W.B.1976,ApJ,208,346  
Gralewicz, P., et al. 1997, A&A, 318, 925

Heiles, C. 1996, ApJ, 462, 316  
Heinbach, U., & Simon, M. 1995, ApJ, 441, 209  
Hunter, S. D., et al. 1997, ApJ, 481, 205  
Letaw, J. R., Silberberg, R., & Tsao, C. H. 1993, ApJ, 414, 601  
Lukasiak, A., Ferrando, P., McDonald, F. B., & Webber, W. R. 1994, ApJ, 423, 426  
Mannheim, K., & Schlickeiser, R. 1994, A&A, 286, 983  
Mori, M. 1997, ApJ, 478, 225  
Murphy, R. J., Dermer, C. D., & Ramaty, R. 1987, ApJS, 63, 721  
Orth, C. D., & Buffington, A. 1976, ApJ, 206, 312  
Particle Data Group. 1990, Phys. Lett. B, 239  
Phillipps,S.,et al.1981,A&A,103,405  
Porter, T. A., & Protheroe, R. J. 1997, J. Phys. G: Nucl. Part. Phys., 23, 1765  
Protheroe,R.J.1982,ApJ,254,391  
Seo,E.S.,et al.1991,ApJ,378,763  
Seo,E.S.,&Ptuskin,V.S.1994,ApJ,431,705  
Simon,M.,&Heinbach,U.1996,ApJ,456,519

Stecker,F.W.1970,Ap&SS,6,377  
Stephens, S. A., & Badhwar, G. D. 1981, Ap&SS, 76, 213  
Strong,A.W.1996,SpaceSci.Rev.,76,205  
Strong,A.W.,et al.1996,A&AS,120,C381  
Strong, A. W., & Mattox, J. R. 1996. A&A, 308, L21  
Strong, A. W., & Moskalenko, I. V. 1997a, in AIP Conf. Proc. 410, Fourth Compton Symp., ed. C. D. Dermer, M. S. Strickman, & J. D. Kurfess (New York: AIP), in press  
1997b, in preparation  
Strong, A. W., Moskalenko, I. V., & Schonfelder, V. 1997, 25th Int. Cosmic Ray Conf. (Durban), 4, 257  
Strong, A. W., & Youssefi, G. 1995, 24th Int. Cosmic Ray Conf. (Roma), 3, 48  
Taira, T., et al. 1993, 23d Int. Cosmic Ray Conf. (Calgary), 2, 128  
Vallee,J.P.1994,ApJ,437,179  
Webber, W. R., et al. 1996, ApJ, 457, 435  
Webber, W. R., Lee, M. A., & Gupta, M. 1992, ApJ, 390, 96