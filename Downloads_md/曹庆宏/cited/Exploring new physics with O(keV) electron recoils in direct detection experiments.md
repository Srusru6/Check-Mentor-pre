# Exploring new physics with O(keV) electron recoils in direct detection experiments

Itay M. Bloch, $^{a}$  Andrea Caputo, $^{b}$  Rouven Essig, $^{c}$  Diego Redigolo, $^{d,e,f}$  Mukul Sholapurkar $^{c}$  and Tomer Volansky $^{a}$

$^{a}$ School of Physics and Astronomy, Tel-Aviv University, Tel-Aviv 69978, Israel  
$^{b}$  Instituto de Física Corpuscular, Universidad de Valencia and CSIC, Edificio Institutos Investigación, Catedratico Jose Beltran 2, Paterna, 46980 Spain  
$^{c}$ C.N. Yang Institute for Theoretical Physics, Stony Brook University, Stony Brook, NY 11794, U.S.A.  
$^d$  CERN, Theory Division, CH-1211 Geneva 23, Switzerland  
eINFN Sezione di Firenze, Via G. Sansone 1, I-50019 Sesto Fiorentino, Italy  
$^{f}$ Department of Physics and Astronomy, University of Florence, Sesto Fiorentino Florence, Italy

E-mail: itay.bloch.m@gmail.com, andrea.caputo@uv.es, rouven.essig@stonybrook.edu, d.redigolo@gmail.com, mukul.sholapurkar@stonybrook.edu, tomerv@post.tau.ac.il

ABSTRACT: Motivated by the recent XENON1T results, we explore various new physics models that can be discovered through searches for electron recoils in  $\mathcal{O}(\mathrm{keV})$ -threshold direct-detection experiments. First, we consider the absorption of axion-like particles, dark photons, and scalars, either as dark matter relics or being produced directly in the Sun. In the latter case, we find that keV mass bosons produced in the Sun provide an adequate fit to the data but are excluded by stellar cooling constraints. We address this tension by introducing a novel Chameleon-like axion model, which can explain the excess while evading the stellar bounds. We find that absorption of bosonic dark matter provides a viable explanation for the excess only if the dark matter is a dark photon or an axion. In the latter case, photophobic axion couplings are necessary to avoid X-ray constraints. Second, we analyze models of dark matter-electron scattering to determine which models might explain the excess. Standard scattering of dark matter with electrons is generically in conflict with data from lower-threshold experiments. Momentum-dependent interactions with a heavy mediator can fit the data with dark matter mass heavier than a GeV but are generically in

tension with collider constraints. Next, we consider dark matter consisting of two (or more) states that have a small mass splitting. The exothermic (down)scattering of the heavier state to the lighter state can fit the data for keV mass splittings. Finally, we consider a subcomponent of dark matter that is accelerated by scattering off cosmic rays, finding that dark matter interacting though an  $\mathcal{O}(100\mathrm{keV})$ -mass mediator can fit the data. The cross sections required in this scenario are, however, typically challenged by complementary probes of the light mediator. Throughout our study, we implement an unbinned Monte Carlo analysis and use an improved energy reconstruction of the XENON1T events.

KEYWORDS: Beyond Standard Model, Cosmology of Theories beyond the SM

ARXIV EPRINT: 2006.14521

# Contents

1 Introduction 1  
2 Models and summary 3

3 XENON1T 7

3.1 Energy reconstruction method 7  
3.2 Statistical method 9

4 Absorption 11

4.1 Axion-like particles 12

4.1.1 ALP dark matter 14  
4.1.2 Solar ALPs 17

4.2 The scalar 19

4.2.1 Scalar dark matter 20  
4.2.2 Solar scalar 21

4.3 The dark photon 22

4.3.1 Dark photon dark matter 24  
4.3.2 Solar dark photon 25

5 Chameleon-like ALPs: circumventing the stellar cooling bounds 26  
6 Dark matter-electron scattering 30

6.1 Standard DM-electron scattering 30  
6.2 Exothermic dark matter and electron recoils 37

6.2.1 Exothermic dark matter-electron scattering: kinematics and best-fit regions 38  
6.2.2 Exothermic dark matter-electron scattering: relic abundance for concrete models 42

7 Accelerated dark matter 46

# 1 Introduction

The quest to identify the particle nature of dark matter (DM) by detecting DM in terrestrial experiments has been ongoing for more than three decades. Despite numerous searches at direct-detection, indirect-detection, and collider experiments, no convincing signal for DM has been found to date. Given the profound implications for our understanding of the DM particle's properties if we were to find it in the laboratory, any claim for a possible DM signal in one of these experiments deserves to be studied carefully.

The XENON1T collaboration has recently observed an unexplained excess of electronic recoil events with an energy of  $\mathcal{O}(\mathrm{keV})$  [1]. While the most likely explanation is a neglected background source or a statistical fluctuation, the possibility that the excess could be the first sign of new physics (not necessarily even a sign of DM) is intriguing. The excess of events does not appear in the traditional search for nuclear recoils from elastic DM-nucleus scattering. Rather, it appears as an excess in a search for electron recoils (ER). The XENON1T search has an exposure of  $2.36\times 10^{5}\mathrm{kg}$  - day in the  $1 - 30\mathrm{keV}$  energy range. The background rate is reported to be  $76\pm 2$  events/tonne year keV implying a total of  $\sim 1476$  background events. An excess of 53 events has been observed at the  $1 - 7\mathrm{keV}$  low energy region (corresponding to roughly a  $3\sigma$  excess), with the excess mainly located in the 2-keV and 3-keV energy bins.

In this paper, we explore several possibilities for the origin of this signal. We will focus mostly on the possibility that the origin is attributable to DM, but will also consider bosonic particles (pseudo-scalar, scalar and vector) produced in the Sun, which do not necessarily have to be a DM component. We discuss in the context of the XENON1T excess several models previously considered in the literature:  $\mathcal{O}(\mathrm{keV})$  bosonic DM that is absorbed by an electron in the xenon atom [2-9], bosonic DM that is emitted from the Sun [10-14], and DM scattering off electrons in xenon [15-19]. For the absorption of bosonic DM, we show that only the dark photon or a "photophobic" axion-like particle can fit the XENON1T hint. For light bosons produced in the Sun, bosons with a mass near  $1\mathrm{keV}$  provide a better fit to the XENON1T data than massless bosons. The tension with star cooling constraints can be ameliorated in models where the shape of the scalar potential is substantially modified in dense environments (for a similar effect see e.g. [20-27]). Here we present a model in which a pseudo-scalar is produced in the Sun and explains the XENON1T excess, but a density-dependent coupling between the pseudo-scalar and electrons avoids stellar cooling bounds.

We also discuss, DM-electron scattering with different form factors, "exothermic" DM scattering off electrons (for previous work focused on nuclear scattering see [28, 29] and focused on electron scattering see [30]), and cosmic-ray accelerated DM that here interacts with electrons through an intermediate-mass mediator (for previous work focused on heavy mediators or light mediators interacting with nuclei see [31-34]; see also [35]). These models deserve further study in future dedicated papers, but we provide their salient features focusing on the XENON1T excess.

This paper is organized as follows. In section 2, we describe the requirements that new physics needs to satisfy in order to explain the XENON1T excess, and also detail the models that we will discuss. In section 3, we describe important features of the XENON1T data, our method for reconstructing the energy, and our statistical analysis. In section 4, we focus on the absorption of bosonic particles that are either (non-relativistic) DM particles in our halo or emitted from the Sun. Section 5 investigates how a density-dependent potential can be used to circumvent the stellar cooling bound. In section 6, we discuss DM-electron scattering, reviewing the "standard" case and then focusing on multi-component DM with small mass splittings. We will see that "exothermic" DM scattering off electrons has a rich phenomenology. Section 7 considers a subdominant DM component that is accelerated by scattering off cosmic rays.

# 2 Models and summary

The XENON1T excess motivates us to consider various known as well as novel new physics scenarios, focused mostly, but not solely, on DM models that can be discovered via a high-threshold  $(\gtrsim \mathrm{keV})$  ER searches. We first summarize the relevant features of the excess and then identify possible mechanisms that may explain it.

The following considerations are important when studying a prospective new physics signal:

- The excess events have an energy of  $2 - 3\mathrm{keV}$ . The measured spectrum suggests that a potential signal should contribute to more than a single bin. However, the finite energy resolution of the experiment makes this (statistically weak) observation less sharp, allowing for rather narrow spectra to provide a reasonable fit. The  $1\mathrm{keV}$  bin and the bins with energies  $\geq 4\mathrm{keV}$  are approximately consistent with background expectations. See figure 4 left.  
- Low-threshold direct-detection experiments searching for electron recoils provide additional constraints on any signal that also produces sub-keV electron recoils [16, 18, 36-46]. For energies of order 100's of eV, the XENON1T S2-only analysis is especially constraining [44].  
- Numerous direct-detection experiments place stringent constraints on any accompanying nuclear recoil signal (for a recent compilation of low-mass DM limits on nuclear interactions see [47]). Models that predict such a signal must evade these bounds.  
- New physics that couples to electrons is constrained by various collider and beam-dump experiments (see [48] for a compilation), as well as from astrophysical observations, such as the cooling of the Sun [49, 50], White Dwarfs (WD) [51-54], Red Giants (RG) [55-57], Horizontal Branch (HB) stars [58], and Supernovae (SN) [59].

Prospective models that could produce the observed excess and satisfy its features can be separated into models that predict an absorption signal (section 4 and section 5) and those that predict a scattering signal (section 6 and section 7). We consider several scenarios:

1. Absorption. We will consider the case that an electron absorbs a bosonic particle: pseudo-scalar (axion), a scalar, or a vector. The boson may be either non-relativistic or relativistic. The former may occur if the particle constitutes a component of the DM; in this case the ER spectrum is peaked at the mass of the DM, and can fit the data only due to the experiment's finite energy resolution. We find that a vector and a pseudo-scalar can explain the XENON1T excess, while a scalar is in conflict with stellar cooling constraints. Next, light bosons may be produced in the Sun, which has a temperature of around  $2\mathrm{keV}$ . A non-zero mass around  $1.5 - 2.5\mathrm{keV}$  depending on the production mechanism could also cut the solar emission kinematically, providing the best fit to the data. However, for bosons produced in the Sun strong constraints arise from stellar cooling, strongly disfavoring the couplings needed to explain the XENON1T excess for the vanilla axion and dark photon models.

2. Chameleons. The stellar cooling constraints on light bosons may be evaded if the couplings of SM particles to the corresponding bosons are screened inside high-density or high-temperature stellar objects. Such chameleon-like particles have a rich phenomenology and can revive the Solar explanation of the XENON1T hint.

3. DM scattering. The DM-electron scattering rate depends on the momentum-transfer-dependent atomic form-factor. This steeply-falling function is highly suppressed for momenta  $q \gg 1 / a_0 = \alpha_{\mathrm{EM}} m_e$ , where  $a_0$  is the Bohr radius,  $\alpha_{\mathrm{EM}}$  is the fine structure constant and  $m_e$  is the electron's mass. As a consequence, DM scattering through a light mediator or a velocity-independent heavy mediator predict a steeply rising spectrum at sub-keV energies and are thus disfavored.

4. Velocity-suppressed DM scattering. Models that exhibit velocity- or momentum-dependent heavy-particle-mediated DM-electron scattering are allowed by experimental data at lower energies and provide an adequate fit to the XENON1T excess. However, such models are likely in tension with collider bounds on new particles that generate this operator [60, 61].

5. Exothermic DM. An unsuppressed high-energy spectrum from DM-electron scattering may stem from an exothermic scattering of DM off electrons, the result of DM consisting of two or more states whose masses are slightly split by an amount denoted as  $\delta$ . The atomic form factor, together with the scattering kinematics, imply a rather narrow electron recoil spectrum that is peaked near  $|\delta|$  for a wide DM mass range and can explain the XENON1T excess for  $|\delta| \sim \mathcal{O}(\mathrm{keV})$ . The spectrum can be broadened if the DM-electron interaction increases with increasing momentum transfer  $q$ , if there are three or more DM states whose mass is split by different amounts of  $\mathcal{O}(\mathrm{keV})$ , or if the DM mass is well below the GeV-scale.

6. Accelerated DM. A small subcomponent of DM may be accelerated through its interactions in the Sun [42, 43] or with Cosmic Rays (CRs) [31-33]. While we find that the component accelerated from the Sun cannot explain the XENON1T excess without being in conflict with lower-threshold direct-detection searches, we find that CR scattering of DM with non-trivial momentum-dependent form factor can address the XENON1T excess while evading other direct-detection constraints. However, in the scenario we consider here, direct constraints on the mediator exclude robustly this explanation.

In figure 1, we summarize the goodness-of-fit of the various absorption scenarios discussed above to the XENON1T measurement. We see that the bosonic DM scenarios (red curve) can fit the data well with a predicted mass of  $m_{X} = 2.5 \mathrm{keV}$  and coupling to electrons. Among these, the scalar DM case is excluded by stellar constraints while the dark photon and the axion are good explanation of the XENON1T excess. In the latter case the anomalous axion coupling to photon should be set to zero to avoid X-rays constraints.

In all the solar cases, the addition of a non zero mass ameliorates the fit by cutting off the spectrum kinematically, in better agreement with the  $1\mathrm{keV}$  bin being consistent with

![](images/52b08573e0b3311acde561aa11cf6843b0ab64502e2e01a04196a9db9618e47d.jpg)  
Figure 1. Summary of the absorption scenarios considered here, with their p-value as a function of the mass. We show in dark red all the cases of bosonic DM: axion-like particles in section 4.1.1, light scalars in section 4.2.1 and dark photon in section 4.3.1. We also discuss all the solar scenarios: in green axion-like particles discussed in section 4.1.2, in blue light scalars in section 4.2.2 and in orange dark photon in section 4.3.2.

the background prediction. For pure electron coupling the axion explanation is disfavored compared to the scalar or the dark photon. The reason is that the peaks in the spectrum of the axion ABC production [50] are not observed in the data. If the solar production happens through the Primakoff process [58] the scalar provides a very good fit of the data while the axion explanation is disfavored. As we will discuss, the reason can be traced back to the different energy dependences of the axion and scalar absorption rates in xenon. The scalar rate grows fast at low energies for very light masses but a good fit can be obtained for a scalar mass of  $m_{\phi} = 1.9 \mathrm{keV}$ , which cuts the sharp rise towards low energies and hence generates a bump between 2 and  $3 \mathrm{keV}$ . On the other hand, the axion absorption rate is suppressed at low energies and the resulting spectrum is too flat at energies above  $3 \mathrm{keV}$  to provide a good fit to the excess, independently of the mass of the axion. Therefore, fitting to a massive axion consistently tends to prefer a very light, even massless, axion.

In figure 2, we summarize the goodness-of-fit of the different scattering scenarios presented above. First, we notice that elastic scattering cannot explain the XENON1T hint for  $F(q) \propto q^{n}$  form factors with  $n \leq 0$ , since the electron recoil spectrum rises at low energy, in tension with complementary direct-detection experiments at lower energy thresholds. However, for  $F(q) \propto q^{n}$  with  $n > 0$  the spectrum falls fast enough towards lower energies and provides an adequate fit to the XENON1T data.

Second, we show that exothermic scattering can fit well the data when the heavy and light DM states are split in mass by a few keV. Once the splitting is marginalized to the best fit value, the p-value is essentially independent of the DM mass as long as it

![](images/9278637bcc1aaf2d187eb2641a2651ce35d204729d14c1aefa80c370a7626986.jpg)  
Figure 2. We show in green momentum suppressed DM-electron scattering with form factors  $F(q) \propto q$  (dark green) and  $F(q) \propto q^2$  (light green) discussed in section 6.1. We show accelerated DM by cosmic rays scattering for fixed mass ratios between the DM and the mediator  $m_{\phi} / m_{\chi} = 1 / 4$  (dark red) and  $m_{\phi} / m_{\chi} = 1 / 15$  (light red), where  $\phi$  can be a scalar or a vector with scalar interactions on the SM side and axial interactions on the DM side. This is discussed in section 7. We also include different scenarios for exothermic scattering: light mediator  $F(q) \propto 1 / q^2$  (purple), heavy mediator  $F(q) \propto 1$  (dark blue), and momentum suppressed form factors  $F(q) \propto q$  (cyan) discussed section 6.2. The splitting  $|\delta|$  between the heavy state and the light state in the dark sector is marginalized to minimize the p-value for  $|\delta| < 4.9 \mathrm{keV}$  (as discussed in the text, this range of splittings may not capture the entire possible parameter space, and should thus be treated with caution). The dashed lines have fixed  $|\delta| = 2.5 \mathrm{keV}$ , which implies a lower bound on the DM mass.

is heavier than the splitting itself. The spectrum is peaked near  $2\mathrm{keV}$  and fits well the data, without being trivially excluded by complementary direct detection experiments. In concrete models, the rich phenomenology of these DM scenario could provide other handles of testing them at beam dump experiments or in nuclear recoil. We also show that for a fixed splitting, a lower bound on the DM mass can be derived, which varies depending on the nature of the form factor.

Third, we discuss accelerated DM by scattering with cosmic rays. In such a case, the challenge is again to find a scenario where the accelerated spectrum falls sufficiently rapidly at energies lower than  $2\mathrm{keV}$ . We achieve this by considering axial-scalar interactions between the accelerated DM and the SM, mediated by a light new mediator with mass around  $100\mathrm{keV}$ . Just as other models of accelerated DM, this scenario is likely to be challenged by other observation probes. We leave a more in-depth study of this scenario for future work.

We now present our data analysis framework, before discussing each of these model scenarios in detail.

# 3 XENON1T

In this section, we review the relevant aspects of the XENON1T experimental apparatus and the electron recoil analysis, with a focus on describing our treatment of the energy reconstruction and statistical analysis that is used throughout this work.

# 3.1 Energy reconstruction method

The experiment utilizes a dual-phase xenon Time Projection Chamber [44, 62-71], to search for weakly interacting particles. When one of the xenon atoms in the Liquid Xenon (LXe) phase recoils or is ionized due to a collision, photons are emitted and detected by photomultiplier tubes (PMTs). This signal is called the prompt scintillation signal (S1). In addition to the photons emitted close to the interaction point, ionized electrons drift inside the detector due to an external electric field. When the electrons reach the Gaseous Xenon layer (GXe) at the top of the detector, they are extracted across the liquid-gas interface, collide with xenon atoms, and produce a proportional scintillation light, known as the S2 signal, which is also measured by the PMTs.

The ratio of S2/S1 provides a handle that enables one to differentiate between Nuclear Recoil (NR) and ER events. Further information about a given event can be inferred by its location inside the PMTs, the time difference between the arrival of the S1 and S2 signals, and the S1 and S2 signal shapes. This complementary information is taken into account in the analysis by the XENON1T collaboration, however, it is not publicly available. When the XENON1T collaboration reports their data, they use the corrected S1 (cS1) and corrected S2 (cS2), which takes into account this additional information.

In their analysis of the Science Run 1 (SR1) data, the XENON1T collaboration provides a scatter plot of  $(\mathrm{cS1},\mathrm{cS2_b})$  (the 'b' subscript signifies that only the PMTs at the bottom of the detector were used for the S2 reconstruction). Rather than using their reconstructed keV-binned energy spectrum, we will use the data from this scatter plot to reconstruct the energies for each event. We do this, since the keV-binned data results in a loss of information, as the XENON1T detector resolution is as low as  $\sim 0.3\mathrm{keV}$  [71] at their analysis threshold  $\sim \mathrm{keV}$ . In order to reconstruct the energies, we use the procedures laid out by the XENON1T collaboration in [69] (which uses detector modeling techniques created by the NEST collaboration [72], and with additional data taken from [73, 74]), which allows us to simulate the detector response and the effects of reconstructing the signal. We use a Monte Carlo (MC) simulation to determine how an ER with a given energy is distributed on the  $(\mathrm{cS1},\mathrm{cS2_b})$  plane, and use a maximum likelihood estimator to find the energy of the event. Below, we refer to this way of reconstructing the energy as "our method", even though it is based on information provided in previous XENON1T papers; we do so to differentiate it from the way the energy was reconstructed by the XENON1T collaboration in their ER analysis paper [1], where they simply use

$$
E _ {\text {r e c o n s t r u c t e d}} ^ {\mathrm {X E N O N 1 T}} = \left(\frac {c S _ {1}}{g _ {1}} + \frac {c S 2 _ {b}}{g _ {2}}\right) W, \tag {3.1}
$$

where  $g_{1} = 0.142$  and  $g_{2} = 11.4$  are the probabilities for one photon to be detected as a photo-electron in the PMT and the charge amplification factor, respectively, and the mean

![](images/a113ce99c66be775cfb46f7f1e30469ca8f9bec12a2d34e02d1ef67c277456c3.jpg)  
Figure 3. Observed events by the XENON1T collaboration [1] in the (cS1,cS2b) plane, for events they tagged as having an energy  $\leq 9\mathrm{keV}$ . The colors of the points correspond to the difference in the reconstructed energy (in units of the energy resolution) between our energy reconstruction calculation and the simplified equation used by XENON1T (eq. (3.1)). The energy resolution is estimated using our energy reconstruction calculation. The gray dashed lines show constant energy lines using the simplified energy reconstruction given in eq. (3.1). In blue is the expectation value for the energy interval [keV, 9keV]. The black points are more than  $2\sigma$  away from this expectation value, and we did not sample the parameter space finely enough with our MC to reliably reconstruct their energy; for these points, we assume simply that their energy is given by eq. (3.1).

energy to produce a detectable quanta is  $W = 13.8$  eV. For additional discussion of the possible problems with this simplified energy reconstruction formula, see [75].

In figure 3, we reproduce the (cS1,cS2b) scatter plot for events tagged in [1] to have an energy below  $9\mathrm{keV}$  (above this energy, the resolution is  $\sim \mathrm{keV}$  so the binning leads to only marginal information loss; moreover, the excess is concentrated below this energy, so we will not be concerned with events at higher energies). The color of the points shows the difference between the energy reconstructed by our method and the simplified formula used in [1], eq. (3.1). The colored points on the plot are in units of the energy resolution, calculated with our method (see below). Due to the finite size of our MC sample, large numerical errors may occur in rare cases where the calculated likelihood for the reconstructed energy of a given event is small ( $\leq 5\%$  C.L.) for all energies. To avoid such errors, in those cases we use the simplified reconstruction method, eq. (3.1).

We show in figure 4 (left) our calculation of the keV-wide binned energy spectrum and compare it with the XENON1T spectrum. The two spectra are nearly identical. This provides confidence in our energy reconstruction method, and allows us to use the full unbinned energy information for our new physics analyses below. We also include in this plot the background model from [1].

For the formula eq. (3.1) to be the best estimator for the energy, the variables cS1 and  $c\mathrm{S2}_b$  should be anti-correlated. While this has been validated for high energies, preliminary measurements appear to suggest that there is only a weak anti-correlation for low energies.

![](images/4407a6fa1b9a5105f996eabd7b279d04e6a5c33e53bba5904b45f60e7452d834.jpg)  
Figure 4. Left: Comparison of the naive spectrum reconstructed, and the one by the MC, for energies below  $9\mathrm{keV}$ . In blue is the background model from [1]. While the biggest disagreement, at the lowest-energy bin, seems to be a  $\geq 1\sigma$  disagreement, we note that this is misleading, as many of the points were reconstructed on the edge of the bin causing small differences to be magnified. An overall good agreement between our MC method and the one used by the XENON1T collaboration is observed, enabling us to use the full unbinned energy information throughout this paper. As an aside, we also note that our binned energy spectrum does not have the same monotonically decreasing spectrum in the  $\sim 5 - - 10\mathrm{keV}$  energy bins. Right: Energy resolution estimated from our MC (black points), a fit to these MC data ( $\sigma_{E}[\mathrm{keV}] = -0.21 + 0.39\sqrt{E}$ , red line), and the energy resolution estimated by the XENON1T collaboration in [1] ( $\sigma_{E}[\mathrm{keV}] = 0.3171\sqrt{E} +0.0015E$  [keV], blue line).

![](images/fe9cca32cb6288f75385de9134cf44b50f52ac59eb250be22528d75ae6fbe595.jpg)

In particular, this can be seen from measurements of the  $^{37}\mathrm{Ar}$  line at  $2.83\mathrm{keV}$  presented in [73]. Our MC simulation of  $2.8\mathrm{keV}$  events (assuming a uniform distribution in  $z$ ) agrees well with the contours in the (cS1, cS2b) plane for the  $^{37}\mathrm{Ar}$  data found in [73]: our agreement is better than  $\lesssim 3\%$  for the central value, and we can find even better agreement if we change the simulation parameters slightly from those given by the XENON1T collaboration in [69] within their error margins. Our simulation also agrees well with the observed weak correlation between cS1 and cS2b. This provides further confidence in our energy reconstruction method, especially at the  $\mathcal{O}(\mathrm{keV})$  energies relevant for the excess events. Figure 4 (right) shows the energy resolution estimated from our MC (black points), a fit to these MC data (red line), and the energy resolution estimated in [1] (blue line). As can be seen, the energy resolution estimated from the MC is slightly better than that used in [1]. As the actual smearing of appears to be not entirely symmetric, an asymmetric resolution might provide an even more accurate description than the symmetric one used here (see also ref. [75]), however, this does not appear to change of the results significantly.

# 3.2 Statistical method

For our analyses, we use a likelihood ratio test, with unbinned likelihoods. For each signal model,  $s$ , that depends on parameters  $\theta_{s}$ , we find the likelihood of the signal+background

hypothesis for the data as a function of the model parameters,

$$
\mathcal {L} (s + b) = \frac {e ^ {- \mu_ {s} - \mu_ {b}}}{n !} \prod_ {i = 1} ^ {n} \frac {d (N _ {s} + N _ {b})}{d E} (E _ {i} | \theta_ {s}), \tag {3.2}
$$

where  $E_{i}$  are the reconstructed energies,  $n$  is the number of observed events,  $dN_{b} / dE$  ( $dN_{s} / dE$ ) is the background spectrum (signal spectrum), and  $\mu_{b} = \int dN_{b} / dE$  ( $\mu_{s} = dN_{s} / dE$ ) are the total expected background (signal) events. We maximize the likelihood to find the best fit points. In order to estimate the significance and quality of our fits, we assume the asymptotic formulas found in [76]; we therefore assume that twice the log-likelihood-ratio of the signal+background hypothesis compared to the background-only hypothesis is distributed according to a  $\chi^2$  distribution, with the number of degrees of freedom set equal to the number of model parameters,

$$
\mathrm {p - v a l u e} = Q \left(\frac {\# \mathrm {D . O . F .}}{2}, \log \left(\frac {\mathcal {L} (\hat {s} + b)}{\mathcal {L} (b)}\right)\right), \tag {3.3}
$$

where  $\mathcal{L}(\hat{s} + b) (\mathcal{L}(b))$  is the likelihood of the best fit for the signal+background (background-only) hypothesis. #D.O.F is the number of degrees of freedom for the signal hypothesis, and  $Q$  is the regularized incomplete gamma function (one minus the p-value gives the cumulative distribution function for the  $\chi_{\# \mathrm{D.O.F.}}^2$  distribution).

To ease interpreting the  $p$ -value of an excess, we also present the more commonly used significance<sup>2</sup>

$$
\text {S i g n i f i c a n c e} = \sqrt {2} \operatorname {e r f c} ^ {- 1} (\mathrm {p} - \text {v a l u e}). \tag {3.4}
$$

Where  $\operatorname{erfc}^{-1}$  is the inverse function to the complementary error function.

When presenting later 2D plots with  $1 - \sigma$  and  $2 - \sigma$  bands (see e.g. figure 6 left, for an example parameter space for the ALP DM hypothesis), each point on the graph is treated as an independent hypothesis (i.e. with a given coupling, mass, etc.). At such graphs, the  $1 - \sigma$  ( $2 - \sigma$ ) band presents the points that are  $1 - \sigma$  ( $2 - \sigma$ ) away from the best fit point on that graph (i.e. not necessarily the best fit point in general).

In each of the following sections, we describe how to derive the spectrum of events. The measured spectrum will be modified by detector response effects. In particular, for a given theoretically predicted signal, we modify the spectrum by the effective exposure,  $\mathcal{E}(\omega)$ , of the xenon detector. We then smear the resulting spectrum by a gaussian with the resolution presented by the red line in figure 4 (right), and then calculate the likelihood. The effective exposure models the non-flat efficiency, and should in fact be applied during the MC stage, as it directly relates to the S1 signal, and not the energy. However, for simplicity, we have applied it as described in the text. Small variations on our methods yield changes only for signal models with a large rate at the  $1 - 2\mathrm{keV}$  bin where the efficiency is not flat, and even for such models, the effect is not significant.

In our analysis, we will ignore any contribution to the background from, e.g., tritium decays (see e.g. [1, 77]) and  $^{37}\mathrm{Ar}$  (see e.g. [75]). We will also ignore the look-elsewhere

effect which is important for determining the global significance of a particular model [78]. While a formal calculation of the global significances for each model is beyond the scope of this work (see ref. [78] for a thorough discussion), we briefly discuss here what we expect the importance of the look elsewhere effect to be for each of the models considered in this paper.

For both standard DM-e scattering models considered here, as well as for the CR-accelerated DM presented, the look-elsewhere-effect is expected to be non-important. For the case of particles produced in the Sun, the look-elsewhere will have a mild importance, since changing the mass of the particle can lead to peaks in the signal spectrum at different energies, and yet the range of possible masses is limited by roughly the temperature of the solar core. For the case of the DM absorption, the look-elsewhere effect is expected to possibly be important, since it corresponds to the classical case of a highly-localized signal. Indeed, the reported local significance by the XENON1T collaboration is  $4\sigma$ , while the reported global one is  $3\sigma$  [1]. For the case of exothermic-DM, the multi-dimensional parameter space can greatly affect both the location and width of the signal spectrum, and it is thus expected for the look-elsewhere to have the most drastic effect for these models.

# 4 Absorption

We consider first models of bosonic DM, confronting them with the XENON1T measurement. Three cases are considered: pseudo-scalar (axion), scalar, and vector bosons. For each we explore the non-relativistic case, in which the boson constitutes the DM, and the relativistic case, for which the boson is produced in the Sun.

In the case of bosonic DM, the rate of events in the XENON1T detector per unit energy is

$$
\frac {d R _ {\mathrm {a b s}} ^ {\mathrm {D M}}}{d \omega} = \Phi^ {\mathrm {D M}} \sigma_ {\mathrm {a b s}} ^ {I} (\omega) \delta (\omega - m _ {I}), \tag {4.1}
$$

where the energy,  $\omega$ , is kinematically constrained to equal the DM mass (ignoring small non-relativistic corrections of order the DM energy), and is then smeared to account for the detector resolution as described in section 3. The total number of events in the relevant XENON1T energy window is then obtained by convolving the above rate with the effective exposure  $\mathcal{E}(\omega)$  reproduced in section 3 and integrating over energy.

The DM flux,  $\Phi^{\mathrm{DM}}$ , is the same for all bosons, and depends only on the DM relic density,  $\rho_{\chi}$ , and the mass of the light boson

$$
\Phi^ {\mathrm {D M}} = 1. 2 \times 1 0 ^ {1 3} \mathrm {c m} ^ {- 2} \mathrm {s e c} ^ {- 1} \left(\frac {\rho_ {\chi}}{0 . 4 \mathrm {G e V} \mathrm {c m} ^ {- 3}}\right) \left(\frac {\mathrm {k e V}}{m _ {I}}\right) \left(\frac {v}{1 0 ^ {- 3}}\right). (4. 2)
$$

The absorption cross section,  $\sigma_{\mathrm{abs}}^I$ , depends, however, on the interaction of a given light boson  $I$  with the bounded electrons in the liquid xenon. Here we consider three cases: (i) ALP DM absorption via the axioelectric effect ( $I = AE$ ; section 4.1), (ii) scalar absorption via the scalar-electric effect ( $I = SE$ ; section 4.2), and (iii) dark photon DM absorption via the photoelectric effect ( $I = PE$ ; section 4.3).

![](images/4d7e7a7544ff89198cdc66b3c301f57b92a25bf3a9a9ac27cf04b09c07ca14c4.jpg)  
Figure 5. Solar flux spectra for the axion production from ABC processes [50] (blue) and Primakoff production [58] (yellow), for scalars from bremsstrahlung [11, 14] (green), and for dark photons (red). On the left, we assume a massless boson, while on the right we included the kinematical threshold due to a finite boson mass, fixed to the best fit point for each case. To highlight the spectral features, the plots are normalized such that the total integrated flux in the energy window of interest for XENON1T,  $\omega \in [1,10]\mathrm{keV}$  equals  $1\mathrm{event} / \mathrm{cm}^2 /\mathrm{s}$ .

![](images/8c98ba69e9e0c03e76d80076dc1611502b0dd39841b0109c14feebbe9a850144.jpg)

For light bosons produced in the Sun, the differential event rate per unit energy can be written as

$$
\frac {d R _ {\mathrm {a b s}} ^ {\mathrm {S u n}}}{d \omega} = \frac {d \Phi_ {I} ^ {\mathrm {S u n}}}{d \omega} \sigma_ {\mathrm {a b s}} ^ {I} (\omega), \tag {4.3}
$$

where the differential solar flux  $d\Phi_I^{\mathrm{Sun}} / d\omega$  depends on the production mechanisms of the light bosons  $I$  inside the Sun's environment and needs to be treated case by case. Below we discuss solar axions in section 4.1.2, solar scalars in section 4.2.2 and solar dark photons in section 4.3.2. In figure 5, we show the relevant solar fluxes that are important for the derivation of the predicted signal's spectrum for the different cases.

# 4.1 Axion-like particles

We consider an axion-like particle (ALP) of arbitrary mass  $m_{a}$  that couples to photons and electrons,

$$
\mathcal {L} _ {\mathrm {A L P}} = \frac {g _ {a \gamma \gamma}}{4} a F _ {\mu \nu} \tilde {F} ^ {\mu \nu} + \frac {g _ {a e e}}{2 m _ {e}} \partial_ {\mu} a \bar {e} \gamma^ {\mu} \gamma_ {5} e. \tag {4.4}
$$

The ALP can be absorbed inside the detector material leading to a ionization signal. The cross section for this so called axio-electric (AE) effect [3-5, 79] can be written as [8]

$$
\sigma_ {\mathrm {A E}} (\omega_ {a}) = \sigma_ {\mathrm {P E}} (\omega_ {a}) \frac {3 g _ {a e e} ^ {2}}{1 6 \pi \alpha_ {\mathrm {E M}} v _ {a}} \frac {\omega_ {a} ^ {2}}{m _ {e} ^ {2}} \left(1 - \frac {1}{3} v _ {a} ^ {2 / 3}\right), \tag {4.5}
$$

where  $\omega_{a} = \sqrt{m_{a}^{2} + k_{a}^{2}}$  is the energy of the ALP and  $v_{a}$  is its velocity. We take the photoelectric cross section,  $\sigma_{\mathrm{PE}}(\omega_a)$ , from [80], which agrees reasonably well with experimental

data above  $30\mathrm{eV}$ . The above formula is approximate, and chosen to correctly reproduce the results obtained in the non-relativistic limit,  $v_{a} \ll 1$ , and in the relativistic limit,  $v_{a} \rightarrow 1$ .

In what follows, we will derive the XENON1T best-fit regions for  $g_{aee}$  as a function of the ALP mass. Theoretically, however,  $g_{aee}$  is often related to  $g_{a\gamma \gamma}$  and for the ALP DM case, X-rays measurements can then be used to exclude part of the parameter space. It is therefore interesting to understand the theoretical relation between the two couplings, which will allow us to identify viable ALP models. As we shall see below, three conclusions can be drawn:

1. Fitting the data with QCD axion DM requires a high degree of fine tuning of its ultraviolet (UV) couplings to electrons and the UV anomaly with respect to electromagnetism.  
2. More general ALP DM requires suppressed couplings to photons in the UV, which typically implies a non-anomalous global symmetry with respect to QED.  
3. Standard solar ALPs could be the QCD axion but are excluded by stellar constraints, motivating chameleon-like ALPs to be discussed in section 5.

To understand these statements, let us briefly discuss the origin for  $g_{aee}$  and  $g_{a\gamma \gamma}$ . The parametrization of eq. (4.4) can be mapped to concrete models where the pseudo-Nambu-Goldstone boson (pNGb) of a spontaneously broken global symmetry couples to the photons and electrons. An arbitrarily small mass  $m_{a}$  can be introduced as a soft breaking of the pNGb shift symmetry. More explicitly, we can write

$$
g _ {a \gamma \gamma} = \frac {\alpha_ {\mathrm {E M}}}{2 \pi f _ {a}} E _ {\text {e f f}}, \quad g _ {a e e} = \frac {m _ {e}}{f _ {a}} C _ {\text {e f f}}, \tag {4.6}
$$

where  $f_{a}$  is the ALP decay constant and  $E_{\mathrm{eff}}$  parametrizes the effective coupling to photons, which is related to the UV parameters through

$$
E _ {\text {e f f}} = E _ {\mathrm {U V}} + C _ {\mathrm {U V}} \mathcal {A} (x). \tag {4.7}
$$

Here  $C_{\mathrm{UV}}$  is the UV coupling of the axion to electrons, while  $E_{\mathrm{UV}}$  is the UV anomaly with respect to electromagnetism, which is model dependent.  $\mathcal{A}(x)$  parametrizes the electron loop function,  $\mathcal{A}(x) = x\arctan^2\frac{1}{\sqrt{x - 1}} - 1$  with  $x = 4m_e^2 / m_a^2 - i\epsilon$  which decouples as  $m_a^2 / m_e^2$  for  $m_a \ll m_e$ . This feature can be traced back to the fact that in the presence of a purely derivative coupling to electrons, only the effective operator  $\partial^2 aF\tilde{F}$  is generated below the electron threshold [81]. If  $E_{\mathrm{UV}}$  is non-zero, the electron coupling is modified by the running contribution induced by the photon coupling [82]. At low energies, one finds

$$
C _ {\mathrm {e f f}} = C _ {\mathrm {U V}} + \frac {3 \alpha_ {\mathrm {E M}} ^ {2}}{4 \pi^ {2}} E _ {\mathrm {U V}} \log \left(\frac {f _ {a}}{m _ {e}}\right). \tag {4.8}
$$

For the QCD axion, the coupling to the gluon field strength gives further contributions to the effective photon and electron couplings generated by the mixing of the axion with the QCD mesons below the confinement scale [83],

$$
E _ {\mathrm {e f f}} \xrightarrow {\mathrm {Q C D}} E _ {\mathrm {e f f}} - 1. 9 2, \quad C _ {\mathrm {e f f}} \xrightarrow {\mathrm {Q C D}} C _ {\mathrm {e f f}} - \frac {2}{3} \frac {4 m _ {d} + m _ {u}}{m _ {u} + m _ {d}} \log \frac {\Lambda_ {\mathrm {Q C D}}}{m _ {e}}. \tag {4.9}
$$

The strong X-ray limits on  $E_{\mathrm{eff}}$  together with the  $\mathcal{O}(1)$  contribution from QCD explains why QCD axion DM must be tuned to address the anomaly.

Various axion models have been studied, where the different hierarchies between the electron and photon couplings are realized:

- DFSZ models, where naturally  $C_{\mathrm{UV}} \sim E_{\mathrm{UV}} \sim \mathcal{O}(1)$  [84, 85].  
- KSVZ models, where  $C_{\mathrm{UV}} = 0$ , and the electron coupling is only generated from the photon coupling via the running [86, 87].  
- Photophobic models where  $E_{\mathrm{UV}} = 0$  and the electron coupling dominates the phenomenology. See [88] for a general discussion of photophobic ALPs and the Majoron [89, 90] as a particularly motivated example of this coupling structure.

Of the above, and in the absence of tuning, only the Photophobic ALPs can fit the XENON1T hint without being excluded, if they are DM.

# 4.1.1 ALP dark matter

If the ALP is DM, the axio-electric effect should be treated in the non-relativistic limit with  $E \simeq m_{a}$ , and thus the energy absorbed by the bounded electron in the detector is equal to the axion mass. Consequently, in order to explain the XENON1T signal the ALP masses must be around  $m_{a} \sim 1$  keV. The predicted spectrum is a narrow peak around the ALP mass, with the observed signal spreading into several bins from detector resolution effects that smear the predicted signal, as shown in figure 6 (right).

The  $1\sigma$  and  $2\sigma$  bands of our likelihood fit is shown in red in figure 6 (left), where the best fit point is

$$
m _ {a} = 2. 5 \mathrm {k e V}, \quad g _ {a e e} = 4 \times 1 0 ^ {- 1 4}, \quad 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 1 5. 7, \tag {4.10}
$$

which corresponds to a  $3.5\sigma$  local significance. The number of signal events is given by,

$$
R _ {\mathrm {A E}} = 3 3 \left(\frac {\rho_ {\mathrm {D M}}}{0 . 4 \mathrm {G e V} \mathrm {c m} ^ {- 3}}\right) \left(\frac {m _ {a}}{2 . 5 \mathrm {k e V}}\right) \left(\frac {g _ {a e e} ^ {2}}{4 . \times 1 0 ^ {- 1 4}}\right) \left(\frac {\mathcal {E}}{2 0 0 \mathrm {t o n n e - d a y}}\right), \tag {4.11}
$$

where we used that  $\sigma_{\mathrm{PE}} = 1133\mathrm{cm}^2 /\mathrm{gram}$  and the effective XENON1T exposure,  $\mathcal{E}(E)$  evaluated at the best fit mass. The predicted coupling to electrons fixes the decay constant to be  $f_{a} / C_{\mathrm{eff}}\simeq 10^{10}\mathrm{GeV}$  shown on the right y-axis. We further show constraints from white dwarfs [52] (dark blue) and red giants [55, 56] (light blue) cooling as well as terrestrial limits from PandaX [44, 91] (light green) and the XENON1T S2-only analysis [44] (darker green).

If the coupling to photons is non-vanishing, the ALP DM with the desired range of masses and decay constants is severely challenged by its large decay rate into di-photons,

$$
\Gamma_ {\gamma \gamma} = \frac {g _ {a \gamma \gamma} ^ {2}}{1 6 \pi} m _ {a} ^ {3}. \tag {4.12}
$$

Imposing that the ALP is stable on timescales of our Universe we get

$$
\text {A L P} \quad \text {s t a b i l i t y :} \quad \frac {E _ {\text {e f f}}}{C _ {\text {e f f}}} \lesssim 2 3 \left(\frac {2 . 5 \mathrm {k e V}}{m _ {a}}\right) ^ {3 / 2} \left(\frac {4 . \times 1 0 ^ {- 1 4}}{g _ {a e e}}\right), \tag {4.13}
$$

![](images/f02937b45d5e96dcdbb76b8d73b91b7e139f37369ce51be5d4049dbe912dbb49.jpg)  
Figure 6. Left: Allowed parameter space for ALP dark matter in the  $(m_a, g_{aee})$  plane. The ALP decay constant is plotted on the right y-axis. The red star is our best fit point in eq. (4.10) and the dark red regions are the  $1\sigma$  and  $2\sigma$  regions. In blue, we show the bounds from star cooling of red giants [55, 56] and white dwarfs [52], and in green the current direct detection constraints from Xenon1T and PandaX [44, 91]. The gray dotted contours show the X-rays constraints from XQC [92, 93] for different values of  $E_{\mathrm{UV}}$ , the shaded region on the top right is excluded by XQC even for  $E_{\mathrm{UV}} = 0$ . We also show the weaker bound obtained from CXB [94]. Dashed brown contours show the initial misalignment necessary to get the right DM relic abundance for  $C_{\mathrm{eff}} = 1$ . For completeness we show in yellow the cooling hint  $2\sigma$  band adapted from [53]. Right: Signal shape for the best fit point in eq. (4.10). The black dots are the XENON1T data, the gray shaded region is the expected background, the blue solid/dashed line is the signal shape after/before smearing and the blue shaded region is the resulting signal plus background distribution.

![](images/fa60ead5c13a567adaf364805b459774ff502a52171131522ed8d05ec1be77fe.jpg)

which gives already an upper bound on the coupling to photons in order for our best fit point to be stable. Even stronger constraints on the diphoton width come from observations of the cosmic X-ray background (CXB) [94]. The best fit ALP is predicted to produce monochromatic photon-lines at frequency

$$
\nu_ {a} = 3 \times 1 0 ^ {1 7} \mathrm {H z} \left(\frac {m _ {a}}{2 . 5 \mathrm {k e V}}\right). \tag {4.14}
$$

A very conservative bound can be extracted by requiring the intensity of the photon line to be less than the measured CXB background at that frequency, which is  $\nu_{a}I_{\nu_{a}}\simeq (2.3\pm 0.2)\times 10^{-11}\mathrm{Wm}^{-2}\mathrm{rad}^{-1}$ . Using this procedure, we find

$$
\text {C X B b o u n d :} \quad \frac {E _ {\text {e f f}}}{C _ {\text {e f f}}} \lesssim 1 \times 1 0 ^ {- 3} \left(\frac {2 . 5 \mathrm {k e V}}{m _ {a}}\right) ^ {3 / 2} \left(\frac {4 \times 1 0 ^ {- 1 4}}{g _ {a e e}}\right). \tag {4.15}
$$

This bound is very similar to the one obtained in [95] and could be substantially improved by looking at individual sources and performing background subtraction. For instance we consider the bounds obtained in [92, 93] using the X-ray microcalorimeters in the XQC

rocket. Using these bounds we find for the best fit value

$$
\text {X Q C b o u n d :} \quad \frac {E _ {\mathrm {e f f}}}{C _ {\mathrm {e f f}}} \lesssim 1. 6 \times 1 0 ^ {- 4} \left(\frac {2 . 5 \mathrm {k e V}}{m _ {a}}\right) ^ {3 / 2} \left(\frac {4 \times 1 0 ^ {- 1 4}}{g _ {a e e}}\right). \tag {4.16}
$$

On the left of figure 6, we illustrate this limit with dashed gray lines for different values of  $E_{\mathrm{UV}}$ . Interestingly, the X-ray bounds discussed so far can exclude a portion of the ALP parameter space even if  $E_{\mathrm{UV}} = 0$ , due to the irreducible one-loop contribution to the photon coupling in eq. (4.7). The bound from CXB and the one from the XQC rocket are shown as shaded gray regions in figure 6 left. Future X-ray missions like Athena [96], as well as new techniques like line intensity mapping [97, 98], will further improve the X-ray bound in eq. (4.16) and could become important to test the ALP DM interpretation of the Xenon1T excess. In figure 6 we show that at the moment, even the more optimistic Athena prospects derived in [97] are not enough to test the region of parameter space explaining the Xenon1T excess if  $E_{\mathrm{UV}} = 0$ .

It is interesting to ask what are the conditions for an ALP DM addressing the anomaly to have the observed DM relic abundance. If one considers a generic axion-like particle with a non-dynamical mass  $m_{a}$ , the correct relic abundance can be generated in the region of interest via the misalignment mechanism [95, 99-101]

$$
\Omega_ {a} h ^ {2} = 0. 0 1 \left(\frac {m _ {a}}{\mathrm {k e V}}\right) ^ {1 / 2} \left(\frac {4 \times 1 0 ^ {- 1 4}}{g _ {a e e}}\right) ^ {2} \left(\frac {9 0}{g _ {*}}\right) ^ {1 / 4} C _ {\text {e f f}} ^ {2} \theta_ {0} ^ {2}. \tag {4.17}
$$

On the left of figure 6, we show in dotted brown lines two  $\mathcal{O}(1)$  values for the misalignment angle,  $\theta_0$ , for which the observed DM relic abundance is obtained with  $C_{\mathrm{eff}} = 1$ . We conclude that the standard misalignment mechanism, with no tuning of the ALP initial condition can address the ALP DM relic density in the region of interest as long as  $C_{\mathrm{eff}}$  can be made sufficiently large.

All in all, we showed that a very small  $E_{\mathrm{UV}}$  value is needed to explain the XENON1T anomaly, disfavoring most existing ALP models, and in particular the QCD axion, and hinting towards photophobic ALPs. Last, we comment on a particularly interesting example of photophobic ALP: the Majoron. In this case electron coupling are generated at loop level together with LFV couplings, after right-handed neutrinos are integrated out. A first consequence of this framework is that the XENON1T signal is correlated with future signals in  $\mu^{+} \rightarrow e^{+}a$  and  $\mu^{+} \rightarrow e^{+}\gamma a$  that could be seen at future high intensity muon facilities like MEGII and Mu3e (see [59] for further details). Depending on the actual seesaw scale one could further explore the parameter space of this model by looking at  $\mu \rightarrow e\gamma$  at MEGII [90]. Another interesting consequence is that since  $C_{\mathrm{eff}} \sim 1 / 16\pi^2$ , non-minimal production mechanisms are required to enhance the Majoron relic abundance beyond the misalignment contribution [102, 103].

# 4.1.2 Solar ALPs

ALPs can also be produced in the Sun through processes involving the electron and photon couplings of eq. (4.4). Here we study solar production, not making any assumptions on the ALPs relic density. We consider both the relativistic case,  $m_{a} \ll T_{\odot}$ , for which the energy absorbed by the bounded electrons is independent of the ALP's mass, as well as the non-relativistic case,  $m_{a} \gtrsim T_{\odot}$ , in which the spectrum is significantly modified, improving the fit to the XENON1T data. See figure 5 for the different spectra with a massless (relativistic) and massive (non-relativistic) ALPs.

Two production mechanisms are of interest: (i) the "ABC" processes: atomic recombination and de-excitation, bremsstrahlung, and Compton scattering, all depending on the value of  $g_{aee}$  [50]. (ii) The Primakoff process [58], which is the conversion of photons into axions in the electromagnetic fields of the electrons and ions making up the solar plasma. This is the dominant production mechanism in the energy range relevant for XENON1T, which depends on  $g_{a\gamma \gamma}$ .

We discuss photophobic ALPs where both production and absorption are controlled by  $g_{aee}$ , so that the total signal rate scales as

$$
R _ {\mathrm {s o l a r}} ^ {\gamma - \text {p h o b i c}} = 6 1 \left(\frac {\Phi_ {\mathrm {A B C} , \mathrm {X e}}}{2 . 5 \times 1 0 ^ {1 2} \mathrm {c m} ^ {- 2} \mathrm {s e c} ^ {- 1}}\right) \left(\frac {g _ {a e e}}{3 . 4 \times 1 0 ^ {- 1 2}}\right) ^ {4} \left(\frac {\mathcal {E}}{2 0 0 \mathrm {t o n n e - d a y}}\right). \tag {4.18}
$$

Here  $\Phi_{\mathrm{ABC, Xe}}$  is the integrated ABC flux in the energy window that is relevant for the XENON1T experiment, calculated for  $m_{a} = 1.3\mathrm{keV}$ . We also consider photophilic ALP models, where the ALP coupling to photons contributes substantially to the production, while the ALP coupling to the electrons controls the absorption rate. Here one finds

$$
R _ {\text {s o l a r}} ^ {\gamma - \text {p h i l i c}} = 4 8 \left(\frac {\Phi_ {\mathrm {P} , \mathrm {X e}}}{1 . 6 \times 1 0 ^ {1 4} \mathrm {c m} ^ {- 2} \sec^ {- 1}}\right) \left(\frac {g _ {a e e}}{1 0 ^ {- 1 3}}\right) ^ {2} \left(\frac {g _ {a \gamma \gamma}}{4 . 3 \times 1 0 ^ {- 9} \mathrm {G e V} ^ {- 1}}\right) ^ {2} \left(\frac {\mathcal {E}}{2 0 0 \text {t o n n e - d a y}}\right), \tag {4.19}
$$

where  $\Phi_{\mathrm{P,Xe}}$  is the integrated Primakoff flux, once again, in the energy window that is relevant for the XENON1T experiment, and with a massless ALP. We find that for the energy range of interest  $(\omega \gtrsim \mathrm{keV})$ , the ABC productions are subdominant for  $g_{aee} / g_{a\gamma \gamma}\lesssim 16\mathrm{MeV}$ , or equivalently,  $E_{\mathrm{eff}}\gtrsim 27C_{\mathrm{eff}}$ . This is satisfied in many standard QCD axion models (see also [104] for an explicit model where  $E_{\mathrm{eff}}$  takes on very large values).

The best fit points in these scenarios are

$$
\gamma \mathrm {- p h o b i c :} m _ {a} = 1. 3 \mathrm {k e V}, g _ {a e e} = 3. 4 \times 1 0 ^ {- 1 2}, 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 1 1. 5, (4. 2 0)
$$

$$
\gamma \text {- p h i l i c}: \quad m _ {a} = 0, \quad g _ {a \gamma \gamma} g _ {a e e} = 4. 3 \times 1 0 ^ {- 2 2} \mathrm {G e V} ^ {- 1}, \quad 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 6. 9, \tag {4.21}
$$

corresponding to  $3\sigma$  and  $2.1\sigma$  local significance respectively. The spectrum for the two cases is shown on the top of figure 7. The peaked structure of these signals is due to the convolution of the solar fluxes with the detector smearing and efficiency, suggesting that in principle, one may be able to differentiate between the two solar production mechanisms with more data.

First, we discuss the case of a strong prior on a massless ALP. This prior can be justified as a theory bias, given that QCD axion models will typically predict an axion

![](images/482ccc492e2eb516a02704408b7fb768f9a504e6dee799cfa7c95dd5606e9f5b.jpg)  
Figure 7. Predicted spectrum for the solar production of a photophobic axion with a best-fit value of  $m_{a} = 1.3$  keV (left) and a photophilic axion with a massless axion as the best fit model (right). The dashed and solid lines show the signal spectrum before and after detector smearing effects, respectively. The measured XENON1T data is shown as black dots, while the gray-shaded region is the expected binned background, and the blue-shaded region is the predicted binned signal.

![](images/11d0c88a01741389aa11cee9aaa63892d5c780afb8859da7f8f48efd47738575.jpg)

mass of  $m_{a} = 5.70 \mu \mathrm{eV} \times (10^{12} \mathrm{GeV} / f_{a})$  [83], unless non-trivial dynamics modifies the behavior of QCD at high energies. The solar production of a massless photophobic axion does not reproduce well the spectral shape of the data. The reason can be traced back to figure 5 where one can clearly see that the ABC production does not shut off fast enough below  $2.5 \mathrm{keV}$ , leaving an excess signal in the lowest energy bin. On the other hand, the massless photophilic model provides the best-fit one parameter model. The significance of the one parameter fit is  $2.6\sigma$ , obviously larger than the one in eq. (4.21) where the ALP mass was left as a free parameter.

Second, we comment on the case of a massive ALP. The ABC production fit can be sensibly improved by introducing an ALP mass of  $1.3\mathrm{keV}$  shutting of kinematically the solar flux to ameliorate the agreement with the  $1\mathrm{keV}$  bin. This is clearly shown in figure 7 left. We checked that introducing a mass does not ameliorate the Primakoff fit. Comparing eq. (4.20) and (4.21) we conclude that ABC production provides a slightly better fit to the data than Primakoff after a mass for the ALP is introduced.

The parameter space for the solar production of the photophilic and photophobic axions is shown in figure 8. On the left plot, we show in red the photophilic  $1\sigma$  and  $2\sigma$  best-fit regions in the  $g_{a\gamma \gamma}g_{aee}$  versus  $m_a$  plane. As mentioned above, the best-fit value lies outside the plot at  $m_a = 0$ . Stellar cooling constraints [10, 52, 55, 56] are shown in blue. For the same model with the best-fit value  $m_a = 0$ , the middle plot shows constraints in the  $g_{a\gamma \gamma} - g_{aee}$  plane. The  $1\sigma$  and  $2\sigma$  best fit regions are shown in red, white dwarf (WD), horizontal branch (HB), and sun cooling limits are marked with dashed-blue lines, and limits form CAST are shown in orange. We also show the predicted model lines for

![](images/109f378b6c3eca52477ca7289cc418171c93c38001d69bc8d8989ef1e75ad332.jpg)  
Figure 8. Left:  $1\sigma$  and  $2\sigma$  best-fit regions (red) for the photophilic solar axion scenario. The best fit point corresponds to the  $m_{a} = 0$  case and lies outside the plot. White dwarfs (WD) [52], red giants (RG) [55, 56], horizontal branch stars (HB) [58] and Sun [10] stellar cooling constraints on  $g_{ee}$  are shown by the blue-shaded regions in combination with the bound on  $g_{a\gamma \gamma}$  from HB stars [105], the Sun basin bound on  $g_{aee}$  [106] is shown in green in combination with HB stars. Different assumptions about the gravitational ejection timescale distinguish the shaded region and the dashed green line. Middle:  $1\sigma$  and  $2\sigma$  best-fit regions as in the left plot (red) for the best-fit massless photophilic solar axion model, but here shown in the  $g_{a\gamma \gamma} - g_{aee}$  plane. Stellar cooling constraints are indicated with dashed blue lines, while limits from CAST [107] are shaded in orange; arrows point to regions that are allowed. The theoretical axion model lines are shown in the bottom-right part of the plot. Right: Same as the left plot, but for the photophobic solar axion model. The red star indicates the best fit point in this case.

![](images/4e8fd5d29e2fff1bf755edb4a269d0203b1307099796617483445b3dafe2a423.jpg)

![](images/c2027c6b356e83da57e4d08418f9d4a740522f6107e03e1576ba0b5e9c222144.jpg)

the DFSZ and KSVZ axion models. Finally, on the right plot we show the  $1\sigma$  and  $2\sigma$  best-fit regions for the photophobic case in red and the stellar constraints in blue. We conclude that for all cases, the solar axion explanation to the XENON1T anomaly is in severe tension with stellar cooling constraints. In section 5, we discuss briefly a possible mechanism to circumvent these bounds.

# 4.2 The scalar

Consider now a scalar,  $\phi$ , that couples to photons and electrons

$$
\mathcal {L} _ {\text {s c a l a r}} = \frac {g _ {\phi \gamma \gamma}}{4} \phi F _ {\mu \nu} F ^ {\mu \nu} + g _ {\phi e e} \phi \bar {e} e. \tag {4.22}
$$

The cross section for scalar-electric (SE) effect can be written in terms of the photoelectric one as [14, 108]

$$
\sigma_ {\mathrm {S E}} (\omega_ {\phi}) = \sigma_ {\mathrm {P E}} (\omega_ {\phi}) \frac {g _ {\phi e e} ^ {2}}{4 \pi \alpha_ {\mathrm {E M}} v _ {\phi}} \left(\frac {k _ {\phi}}{\omega_ {\phi}}\right) ^ {2}, \tag {4.23}
$$

where  $\omega_{\phi} = \sqrt{m_{\phi}^2 + k_{\phi}^2}$  is the energy of the scalar  $\phi$ ,  $v_{\phi}$  its velocity, and  $\sigma_{\mathrm{PE}}(\omega_{\phi})$  is again the photoelectric cross section already used in eq. (4.5). Notice that in the case of scalar DM, the expression above leads to a suppression of the absorption rate of  $v_{\mathrm{DM}}^2\simeq 10^{-6}$ .

The parametrization of eq. (4.22) can be mapped to concrete models. Two particularly motivated scenarios are (i) a light SM singlet mixing with the SM Higgs doublet, and (ii)

the dilaton from a spontaneously broken conformal-invariance. Below we briefly review these models, pointing to the distinct nature of their photon and electron couplings.

A singlet obtaining a VEV would generically mix with the Higgs through the quartic  $\lambda_{\phi H}\phi^2 H^\dagger H$ . The mixing can be written in terms of the ratio of the Higgs and the singlet VEVs,  $\sin \theta = v / f$ , and the final couplings of the singlet to photons and electrons are generated once the mixing is resolved [109-111]

$$
g _ {\phi \gamma \gamma} = \sin \theta \frac {\alpha_ {\mathrm {E M}}}{2 \pi v} \kappa_ {\phi \gamma \gamma} ^ {\mathrm {S M}}, \qquad g _ {\phi e e} = \sin \theta \frac {m _ {e}}{v}. (4. 2 4)
$$

Here  $\kappa_{\phi \gamma \gamma}^{\mathrm{SM}} \simeq 11 / 3 + \mathcal{O}(m_{\phi} / m_{e})^{2}$  is the asymptotic value of the SM loop functions from  $W$ 's and Standard Model fermions for  $m_{\phi} \ll m_{e}$ , and we fixed the coupling of the Higgs to electrons to be  $y_{e} = m_{e} / v$ , ignoring possible deviations from its predicted SM value. In this simple framework, the ratio between the photon and the electron coupling is fixed to  $g_{\phi \gamma \gamma} m_{e} / g_{\phi ee} = 4.2 \cdot 10^{-3}$ , and a large coupling to nucleons is also generated from the couplings of the Higgs to gluons.

Conversely, if the scalar in eq. (4.22) is a dilaton, its coupling to the SM are more model dependent and controlled by the infrared (IR) trace anomaly contributions induced by direct UV couplings between the CFT and the SM. In this framework, the dilaton mixing with the Higgs can be arbitrarily suppressed [112], and the prediction of eq. (4.24) are changed. In particular, for a dilaton, one can entertain the possibility of a loop-suppressed photon coupling, which decouples as  $m_{\phi} / m_{e}$ . Thus, analogously to the ALP case, we consider two possibilities:

- The Higgs-mixing scenario, where the ratio of the relative strength of photon and electron couplings is fixed.  
- The photophobic dilaton scenario, where  $g_{\phi \gamma \gamma}$  is suppressed as  $m_{\phi} / m_{e}$  and the electron coupling dominates the phenomenology.

# 4.2.1 Scalar dark matter

As in the ALP case, the absorption spectrum of the scalar is sharply peaked around its mass, as can be seen in the spectrum plotted for the best-fit scalar DM model on the right of figure 9, with values,

$$
m _ {a} = 2. 5 \mathrm {k e V}, g _ {\phi e e} = 1. 7 \times 1 0 ^ {- 1 3}, 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 1 5. 7. (4. 2 5)
$$

The number of signal events is given by

$$
R _ {\mathrm {A E}} = 3 3 \left(\frac {\rho_ {\mathrm {D M}}}{0 . 4 \mathrm {G e V} / \mathrm {c m} ^ {3}}\right) \left(\frac {m _ {a}}{2 . 5 \mathrm {k e V}}\right) \left(\frac {g _ {\phi e e} ^ {2}}{1 . 7 \times 1 0 ^ {- 1 3}}\right) \left(\frac {\mathcal {E} (2 . 2 \mathrm {k e V})}{2 0 0 \mathrm {t o n n e - d a y}}\right). \tag {4.26}
$$

The predicted coupling to electrons corresponds to a mixing angle with the Higgs of order  $\sin \theta \simeq 2.1 \times 10^{-7}$ . On the left of figure 9, we show in red the  $1\sigma$  and  $2\sigma$  best-fit regions for the scalar DM case in the  $g_{\phi ee} - m_{\phi}$  plane. On the right y-axis, we map  $g_{\phi ee}$  to the mixing angle for the doublet-singlet model, eq. (4.24). Regions excluded by RG

![](images/684cefe3bd0c66cdc36242fc5aa0be20bbc5dcff75cd8d06a2e46ebb3b8c0f22.jpg)  
Figure 9. Left: Allowed parameter space for scalar dark matter in the  $(m_a, g_{aee})$  plane. The red star is our best fit point in eq. (4.10) and the dark red regions are the  $1\sigma$  and 2 sigma regions around it. In blue we show the bounds from star cooling of red giants and horizontal branch stars [108] and in green the present direct detection constraints from Xenon1T and PandaX [44, 91]. Right: Signal shape for the best fit point in eq. (4.25). black dots are the Xenon1T data. The gray shaded region is the expected background, the blue line is the signal shape and the blue shaded region is the resulting signal plus background distribution.

![](images/a030e39c682c505c530736029a82160d21975fcbbb8afffdeeac6dbf6d78bd05.jpg)

cooling constraints [55, 56] are shown in light blue, while the exclusion regions due to the XENON1T S2-only analysis [44] and PandaX-II analysis [91] are shown in dark and light green, respectively. As one can see from figure 9 the scalar DM cannot explain the XENON1T excess because of the large suppression of its absorption rate compared to the ALP case.

# 4.2.2 Solar scalar

Much like ALPs, light scalars can be produced in the Sun, whether or not they constitute DM. For a photophobic scalar, the production in the Sun is dominated by electron-nucleus scalar-bremsstrahlung  $N + e \rightarrow N + e + \phi$ . The rate can be obtained through the rescaling of the regular photon-bremsstrahlung by the ratio of the matrix elements squared. Doing so we find

$$
\frac {\Gamma (N + e \rightarrow N + e + \phi)}{\Gamma (N + e \rightarrow N + e + \gamma)} = \frac {g _ {\phi e e} ^ {2}}{4 \pi \alpha_ {\mathrm {E M}}}. \tag {4.27}
$$

The above agrees numerically with the one given in [50]. Similarly, a photophilic scalar is produced via the Primakoff process, with a rate similar to that of the ALP. The predicted fluxes are shown in figure 5.

We fit both the photophilic and photophobic scalar to the XENON1T data. We find the best-fit points

$$
\gamma \text {- p h o b i c :} m _ {\phi} = 1. 9 \mathrm {k e V}, g _ {\phi e e} = 2. 1 \times 1 0 ^ {- 1 4}, 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 1 8, \tag {4.28}
$$

$$
\gamma \text {- p h i l i c :} m _ {\phi} = 1. 1 \mathrm {k e V}, g _ {\phi \gamma \gamma} g _ {\phi e e} = 4. 2 \times 1 0 ^ {- 2 4}, 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 1 3. 7, \tag {4.29}
$$

![](images/8782a444a7cce745512e3fd73b377c1167214859362def7e2039787414eb3689.jpg)  
Figure 10. Predicted spectrum for the solar production of a photophobic scalar with a best-fit value of  $m_{\phi} = 2.$  keV (left) and photophilic scalar with a best fit value  $m_{\phi} = 1.1$  keV (right). The dashed and solid lines show the signal spectrum before and after detector smearing effects respective. The measured XENON1T data is shown as black dots while the gray-shaded region is the expected binned background and blue-shaded region is the predicted binned signal.

![](images/c6e9958755bb8c75ba91c377a55522e45c884a4bb403197e320df44a902b4356.jpg)

for which we show with dashed and solid blue lines the predicted spectrum before and after smearing respectively in figure 10. As before, the gray region shows the expected binned background while the blue fillings show the binned contribution of the signals. The XENON1T data are shown in black.

In figure 11, we show in red the  $1\sigma$  and  $2\sigma$  best-fit regions of the solar production of a photophilic (left) and photophobic (right) scalars. In both cases, only a massive scalar can explain the XENON1T anomaly. This is in contrast to the photophilic ALP case for which the massless ALP provided the best fit. The reason for this can be traced back to the rapidly falling absorption rate at high energies, eq. (4.23). This implies a soft spectrum, which must be cut off at production through kinematic effects from a massive particle. For the photophilic case, combined stellar cooling constraints are shown in blue while those are shown separately for the photophobic scalar.

# 4.3 The dark photon

As the final absorption scenario of this section, let us consider the dark photon  $A'$ , a massive gauge boson of a broken (dark) gauge group  $\mathrm{U}(1)'$ . The dark photon may couple to ordinary matter via its kinetic mixing with the visible photon [113]. Much as in the previous sections, we consider the absorption of a dark photon DM and the production of a dark photon in the Sun as explanations to the XENON1T anomaly.

The relevant interactions are

$$
\mathcal {L} = - \frac {1}{4} F ^ {\prime \mu \nu} F _ {\mu \nu} ^ {\prime} - \frac {\epsilon}{2} F ^ {\mu \nu} F _ {\mu \nu} ^ {\prime} + \frac {1}{2} m _ {A ^ {\prime}} ^ {2} A ^ {\prime \mu} A _ {\mu} ^ {\prime} + e A _ {\mu} \bar {e} \gamma_ {\mu} e, \tag {4.30}
$$

![](images/bbbd844812eb6c4f1b996ff8fd405dff94322a3274151a262eacfb73bc461851.jpg)  
Figure 11. Left:  $1\sigma$  and  $2\sigma$  best-fit regions (red) for the photophilic solar scalar (left) and photophobic solar scalar (right) scenarios. Red giants (RG) [55, 56], and horizontal branch (HB) [10, 108] stellar cooling constraints are shown by the blue-shaded regions. The red stars indicate the best fit points in both cases. In contrast to a photophilic ALP, the scalar must be massive in order to explain the data, due to its sharply rising absorption rate at low energy.

![](images/6c5d81c2eaa08745f05e19d337f747c933031ba6ea80a5f5920b06d36638b6bd.jpg)

where  $m_{A'}$  is the mass of the dark photon,  $F^{\mu \nu}$  and  $F'^{\mu \nu}$  are the photon and dark photon field strength respectively, and  $\epsilon$  is the kinetic-mixing parameter. After the kinetic terms are diagonalized, the dark photon couples to the electron vector current with a coupling strength  $\epsilon e$ , and the dark-photon absorption cross-section can be related to the SM photoelectric cross section by a simple rescaling,

$$
\sigma_ {\mathrm {D P}} (E) = \epsilon^ {2} \cdot \sigma_ {\mathrm {P E}} (E). \tag {4.31}
$$

Inside a medium, the propagation of electromagnetic fields is determined by the polarization tensor  $\Pi^{\mu \nu} = e^{2}\langle J_{EM}^{\mu},J_{EM}^{\nu}\rangle$ , which can be decomposed into longitudinal and transverse components as,

$$
\Pi^ {\mu \nu} = \Pi_ {T} \sum_ {i = 1, 2} \epsilon_ {i} ^ {T \mu} \epsilon_ {i} ^ {T \nu} + \Pi_ {L} \epsilon^ {L \mu} \epsilon^ {L \nu}, \tag {4.32}
$$

where  $\epsilon^{L,T}$  are the polarization vectors. In general, in-medium effects should be accounted for in order to correctly compute the dark photon absorption rate. We implement these effects following the discussion in [11, 114]. For dark photon DM with mass near  $1\mathrm{keV}$ , we find that the absorption is dominated by the transverse modes, and the inclusion of the longitudinal ones modifies the rate by less than  $10\%$ .

For  $m_{A'}$  larger than the typical solar plasma frequency  $\omega_{\odot}^{pl} \simeq 0.3 \, \mathrm{keV}$ , the production of dark photons in the Sun is dominated by the transverse modes at energies  $\omega \sim \mathrm{keV}$ . In such a case the flux at the Earth is found to be [11]

$$
\frac {d \Phi_ {T}}{d \omega} = \frac {1}{4 \pi R ^ {2}} \int_ {0} ^ {R _ {\odot}} 4 \pi r ^ {2} d r \frac {1}{\pi^ {2}} \frac {\omega \sqrt {\omega^ {2} - m _ {A ^ {\prime}} ^ {2}}}{\exp \omega / T - 1} \epsilon^ {2} \Gamma_ {T}, \tag {4.33}
$$

![](images/509de9bfd28fc5cb87177fe85aa3364beeff90f8aa3bcd750e780504063995d3.jpg)  
Dark Photon (Stuckelberg)- Dark Matter

![](images/af79b7bbfa65c314bccc0288570ed20917511ec356019a3c3e2b24c5a1fc8e70.jpg)  
Figure 12. Left: The  $1\sigma$  and  $2\sigma$  best-fit regions (red) for dark photon DM with a Stuckelberg mass. Light and darker blue represent the RG and HB cooling limits, respectively, and the light green region is excluded due to the XENON1T S2-only analysis [44]. The dashed blue line delimits the  $2\sigma$  region which can also explain the anomalous cooling of HB stars [115, 116]. Right: An example of the predicted spectrum for dark photon DM using the best-fit value  $m_{A'} = 2.5\mathrm{keV}$ . The dashed and solid lines show the signal spectrum before and after detector smearing effects, respectively. The measured XENON1T data is shown as black dots, while the gray-shaded region is the expected binned background. The blue-shaded region is the predicted binned signal.  
Dark Photon Dark Matter

where the interaction rate  $\Gamma_T$  is dominated by free-free absorption and Compton scattering. At lower masses, the behavior of the flux from the Sun depends crucially on the nature of the dark photon mass [114]. For a non-dynamical Stuckelberg mass, the dark and visible sectors decouple in the  $m_{A'} \rightarrow 0$  limit for an on-shell  $A'$ . As a consequence, the rate of production/absorption of the transverse modes falls off as  $(m_{A'} / T)^4$ , where  $T$  is the Sun's temperature. Adding a Stuckelberg mass to the dark photon will then cut off the solar flux around  $\omega \simeq m_{A'}$  as shown in figure 5. Conversely, if the dark photon's mass is generated through the VEV of a dark Higgs, then the ratio between the dark photon mass and the dark Higgs mass is controlled by the ratio of the Higgs quartic and the dark gauge coupling  $m_{h'} / m_{A'} \sim \sqrt{\lambda} / e'$ . For  $m_h \sim m_{A'}$  the production/absorption of a dynamical dark photon therefore goes predominantly through the radial component in the  $m_{A'} \rightarrow 0$  limit [4]. This case shares many features with the absorption scenarios discussed so far, and we will not discuss it here for the sake of brevity.

# 4.3.1 Dark photon dark matter

If the dark photon plays the role of DM, its predicted absorption spectrum in the XENON1T detector is very similar to the other bosonic DM cases discussed in the previous subsections. On the right panel of figure 12, we show an example for the best-fit model,

$$
m _ {A ^ {\prime}} = 2. 5 \mathrm {k e V}, \quad \epsilon = 5. 8 \times 1 0 ^ {- 1 6}, \quad 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 1 5. 7, \tag {4.34}
$$

for which the number of signal events is given by

$$
R _ {\mathrm {P E}} = 3 3 \left(\frac {\rho_ {\mathrm {D M}}}{0 . 4 \mathrm {G e V} / \mathrm {c m} ^ {3}}\right) \left(\frac {m _ {a}}{2 . 5 \mathrm {k e V}}\right) \left(\frac {\epsilon}{5 . 7 \times 1 0 ^ {- 1 6}}\right) \left(\frac {\mathcal {E} (2 . 2 \mathrm {k e V})}{2 0 0 \mathrm {t o n} / \mathrm {d a y}}\right). \tag {4.35}
$$

Dashed and solid lines represent the unsmeared and smeared spectrum, respectively. We see that, as with the axion and scalar, the spectral shape is peaked around the dark photon mass, and detector resolution allows for a reasonable fit to data. As in previous plots, the expected binned background is shown in the figure in gray, while the binned signal is shown in blue. The XENON1T data is presented with black dots.

On the left plot of figure 12, we show in red the  $1\sigma$  and  $2\sigma$  best-fit regions for dark photon DM with a Stuckelberg mass. In light and darker blue, we show the RG and HB cooling limits respectively and in light green, the constraint from the XENON1T S2-only analysis [44]. We learn that the explanation of the XENON1T anomaly with dark photon DM is viable.

Finally, two remarks are in order. First, a major advantage of dark photon DM compared to the ALP and scalar cases is that the decay rate of a keV dark photon into SM particles is extremely suppressed [4]. The only decay channel allowed kinematically is  $A' \rightarrow 3\gamma$ , which is induced by dimension eight operators generated at one loop from the electron coupling. The width of this process is suppressed by  $\sim \alpha^5\epsilon^2 (m_{A'} / m_e)^8$ , and the dark photon explanation to the XENON1T anomaly is safely outside any bound from decaying DM. Second, the misalignment mechanism, which comfortably explains the scalar-and axion-DM relic densities, fails to generate the observed dark photon abundance unless a non-minimal coupling of the dark field-strength to gravity is taken into account [95, 117]. The contribution from inflationary fluctuations explored in ref. [118] explains the DM relic abundance relating directly the scale of inflation with the dark photon mass

$$
H _ {I} = 8 \times 1 0 ^ {1 1} \mathrm {G e V} \left(\frac {2 . 5 \mathrm {k e V}}{m _ {A ^ {\prime}}}\right) ^ {1 / 4} \tag {4.36}
$$

Lower scales of inflation can be achieved by producing the dark photon with other non-minimal mechanisms [119-122]. In particular, the mechanism in [119] can accommodate the correct DM abundance for a keV dark photon by postulating a coupling  $\phi F' \tilde{F}'$  between the inflaton,  $\phi$  and the dark photon. In principle the different inflationary production mechanisms of dark photon DM could be distinguished by looking at the detailed features of the matter power spectrum at short scales.

# 4.3.2 Solar dark photon

For a Stuckelberg dark photon produced in the Sun, the best fit point is

$$
m _ {A ^ {\prime}} = 2. 2 \mathrm {k e V}, \quad \epsilon = 2. 3 \times 1 0 ^ {- 1 3}, \quad 2 \log (\mathcal {L} (S + B) / \mathcal {L} (B)) = 1 7. 3. \tag {4.37}
$$

As for the case of the scalar, the presence of a mass cuts off the low-energy flux to reduce the signal yield in the lower XENON1T bins. The unsmeared and smeared spectrum, together with the binned background, signal, and data is shown in figure 13 (right). In the left plot, we show the best fit region for the model, together with the HB and RG stellar cooling bounds. We learn that as for the scalar and ALP, the best-fit regime is robustly excluded by the astrophysical bounds.

![](images/375feb36936d96bc0225fe796a199425de2585810ef7beeedc2ef7980481795c.jpg)  
Figure 13. Left: The 1- and  $2-\sigma$  best-fit regions (red) for a dark photon with a Stuckelberg mass produced in the sun. Blue regions represent the Sun [13, 116], RG and HB [55, 56] cooling limits. The red star indicates the best fit point. Right: An example of the predicted spectrum for the solar dark photon using the best-fit value  $m_{A'} = 2.3\mathrm{keV}$ . The dashed and solid lines show the signal spectrum before and after detector smearing effects respective. The measured XENON1T data is shown as black dots while the gray-shaded and blue-shaded regions are the expected binned background and signal respectively.

![](images/1c735d0f48f7b74a769020aa810301bebe27ed888a2265f1a245067565a75507.jpg)

# 5 Chameleon-like ALPs: circumventing the stellar cooling bounds

As discussed in the previous section, particles produced in the Sun are excluded as an explanation for the XENON1T anomaly due to stringent stellar cooling constraints. These constraints arise from the energy loss induced by the emission of light bosons in the star environment. In principle, the constraints can be evaded if the properties of these particles depend on the environment, thereby allowing for a suppressed production in stars. Such Chameleon-like particles have been studied extensively in a broader context, for example in order to evade fifth-force constraints or play the role of dark energy (see e.g. [20, 123]), but also for the particular case of ALPs [21-27].

Here we focus on the specific case of chameleon-like ALPs (cALPs). While most previous work has focused on suppressing the axion-photon couplings in stars, we choose to study the suppression of the axion-electron coupling, which is sufficient to open up the parameter space for solar ALP models that predict either only the latter or both couplings (see figure 8). Below we entertain a simple novel model of this kind, leaving a more general framework as well as possible generalizations for future work.

For the axion-electron coupling,  $g_{aee}$ , four stellar cooling bounds may need to be addressed: RG, WD, HB stars, and Sun cooling. The resulting bounds on the ALP electron couplings are summarized in table 1. Among the four, the solar cooling bound is the least constraining and does not exclude the ALP explanation of the XENON1T anomaly (see for

Table 1. Summary of the bounds on the electron coupling  $g_{aee}$  from star cooling with the rough value of the density at the core. The bounds reported here ignore the systematic uncertainties on the stellar modelling and should be taken as benchmark values exemplifying the power of the stellar cooling constraints.  

<table><tr><td>Star</td><td>gaeee bound</td><td>ρcore(MeV4)</td><td>Tcore(keV)</td><td>Ref.</td></tr><tr><td>RG</td><td>4.3 × 10-13</td><td>4.3</td><td>8.6</td><td>[55-57]</td></tr><tr><td>WD</td><td>2.8 × 10-13</td><td>7.7</td><td>0.8</td><td>[51-54]</td></tr><tr><td>HB</td><td>9.5 × 10-13</td><td>4.3 × 10-2</td><td>8.6</td><td>[58]</td></tr><tr><td>Sun</td><td>2.4 × 10-11</td><td>6.7 × 10-4</td><td>1.3</td><td>[49, 50]</td></tr></table>

instance figure 8). The HB bound is in marginal tension with the XENON1T explanation if one accounts for the potentially large systematical uncertainties.

For this reason, we focus here mostly on evading the RG and WD bounds. The energy losses in RG and WD are dominated by the production of light bosons in the highly degenerate core, where the central density is of order  $\rho_{\mathrm{WD,RG}} \sim \mathrm{MeV}^4$ , roughly four orders of magnitude larger than the core density of the Sun (see table 1). Therefore, a model that suppresses production only in high density stars while keeping it unaltered in low density ones may evade RG and WD constraints and, at the same time, leave the ALP production in the Sun unchanged. To illustrate this point, we now discuss a simple model for which production in high-density objects is suppressed. A more thorough study of the constraints, as well as a UV-completion of this model, is left for future work.

Consider a complex Standard Model (SM) singlet,  $S$ , charged under a Peccei-Quinn (PQ) symmetry [124] and a real SM-singlet  $X$ . The two fields are odd under the same  $\mathbb{Z}_2$ , and  $X$  couples to density. Below a given cutoff scale,  $M$ , we assume that the following  $\mathbb{Z}_2$ -invariant interactions are generated

$$
\mathcal {L} \supset c _ {e e} \frac {X S}{M ^ {2}} m _ {e} e _ {L} e _ {R} + \frac {1}{2} \left(\frac {\rho}{M ^ {2}} - m _ {X} ^ {2}\right) X ^ {2} + \frac {1}{4} \lambda_ {X} X ^ {4} + V (S) + \text {c . c .}. \tag {5.1}
$$

The interaction term with the electrons can be induced in a Froggatt-Nielsen construction [125], where the SM electrons carry charges under the same  $\mathrm{U}(1)_{\mathrm{PQ}}$  that rotates the complex singlet  $S$ . Ensuring that under that symmetry  $[e_L] + [e_R] + 1 = 0$ , allows the operator above while forbidding unwanted others (we normalize the singlet charge to be  $[S] = 1$ ). The cut-off scale in such a construction would correspond to the scale of the vector like-fermions required to generate this interaction [126, 127]. For simplicity, we consider the theory below the Higgs mass scale, ignoring further complications that might arise above it.

The potential  $V(S)$  is such that  $S$  develops a VEV,  $S = \frac{1}{\sqrt{2}} (f_a + s)e^{ia / f_a}$ , where  $s$  is the massive singlet with mass  $m_{s} = \sqrt{\lambda_{s}} f_{a}$  and  $a$  is the ALP, which is massless up to the addition of operators breaking the  $\mathrm{U}(1)_{PQ}$  explicitly. For  $m_S \gg m_X$ , we can neglect the  $s$  dynamics and write the effective coupling of the ALP to the electrons

$$
g _ {a e e} ^ {2} = c _ {e e} ^ {2} \frac {m _ {e} ^ {2}}{M ^ {2}} \left(\frac {\rho - M ^ {2} m _ {X} ^ {2}}{\lambda_ {X} M ^ {4}}\right) \Theta (- \rho + M ^ {2} m _ {X} ^ {2}), \tag {5.2}
$$

![](images/364ea2e37cfaab85e3ede3c42b120be48d10fe2254434847b53bb7f67a7523de.jpg)  
Figure 14. Left: Allowed parameter space for chameleon-like ALPs in the  $(m_X, M)$  plane. In the white region defined in eq. (5.3) RG, WD and HB are shut off while the Sun production is unchanged. In the orange and blue either one or the other requirement is not satisfied. The maximal cutoff scale  $M_{\mathrm{max}}$  depends on the chameleon quartic coupling  $\lambda_{X}$  as in eq. (5.6). The dotted magenta contours show different values of  $M_{\mathrm{max}}$  for different choices of  $\lambda_{X}$ . The smallness of the chameleon quartic can be taken as a measure of the fine tuning of the model. The dashed dark magenta line shows  $M_{\mathrm{max}}$  evaluated at the maximal quartic  $\lambda_{X}^{\mathrm{max}}$  allowed by star cooling bounds (we fix  $\lambda_S = 1$ ) once the ALP coupling to electrons  $g_{aee}$  is fixed at its best fit point. A lower quartic  $\lambda_{X}$  will allow for a higher cutoff scale. Right: Parameter space of the chameleon ALP produced in the Sun. The star cooling bounds from HB, WD and HB stars summarized in table 1 are circumvented by the chameleon mechanism for all the parameter space shown in the left panel. The dark red regions are the  $1\sigma$  and  $2\sigma$  band around the best fit point in eq. (4.28) for unsuppressed Sun flux ( $S = 1$ ) and for a suppressed Sun flux ( $S = 10^{-2}$ ). In green we show the bounds from Sun basins [106] for  $S = 1$  and  $S = 10^{-2}$ . As we can see, suppressing the sun flux extends the parameter space of the model as discussed in the text. The shaded blue band is excluded by Sun cooling.

![](images/f4b60dc8e1bdd3cfedf21ba3d676ab8382baf8d43cbfb379aae1f4819bf98c5a.jpg)

where  $\rho$  is the matter density and  $\Theta (x) = 0$  if  $x < 0$  and 1 otherwise. The second term in eq. (5.1) expresses nothing more than the idea discussed in [128]: at low densities,  $X$  has a negative mass, obtaining a VEV. Conversely, at high densities, its squared mass is positive, and the  $\mathbb{Z}_2$  symmetry is restored. As shown in eq. (5.2), for  $\rho \gtrsim M^2 m_X^2$  one finds  $\langle X\rangle = 0$ , and the coupling of the ALP,  $a$ , to electrons vanishes, shutting down its production in stars.

Several conditions limit the parameter space of the example above:

- First, in accordance with the discussion above

$$
\rho_ {\odot , \text {c o r e}} \lesssim m _ {X} ^ {2} M ^ {2} \lesssim \rho_ {\mathrm {W D}, \mathrm {R G}, \mathrm {H B}} \tag {5.3}
$$

if we want to avoid WD, RG, or HB constraints while keeping the Sun flux unsuppressed. The allowed parameter space in the  $(m_X,M)$  plane is shown in the white band of figure 14.

- Second, the quartic  $\lambda_{SX}X^{2}|S|^{2}$  was omitted from eq. (5.1) even though it is allowed by all symmetries. When  $S$  obtains a VEV, such a quartic induces a new mass term for  $X$  that could destroy the density-dependent VEV of  $X$ . To avoid this, we require  $\lambda_{SX}f_a^2 \lesssim m_X^2$ . Independently of its bare value, this quartic will be generated at one loop via the electrons. Putting all together we get an upper bound on the VEV of  $S$ ,

$$
f _ {a} \lesssim 2 4. 6 \mathrm {M e V} \left(\frac {1}{c _ {e e}}\right) \left(\frac {\rho_ {\mathrm {c o r e}}}{1 \mathrm {M e V} ^ {4}}\right). \tag {5.4}
$$

- Third we want to fit still the XENON1T hint with the cALP. Using as a benchmark the solar ALP best-fit model in eq. (4.20), we get

$$
c _ {e e} = 5 \times 1 0 ^ {- 1 2} \lambda_ {X} ^ {1 / 2} \left(\frac {g _ {a e e}}{2 . 6 \times 1 0 ^ {- 1 2}}\right) \left(\frac {M}{\mathrm {M e V}}\right) ^ {3} \left(\frac {\mathrm {M e V}}{\rho_ {\mathrm {c o r e}}}\right) ^ {1 / 2}. \tag {5.5}
$$

Requiring  $c_{ee} \lesssim 1$  to comply with perturbativity, we get an upper bound on the cutoff scale  $M$

$$
M \lesssim M _ {\max } \equiv 6 \mathrm {G e V} \left(\frac {\rho_ {\text {c o r e}}}{1 \mathrm {M e V}}\right) ^ {1 / 6} \left(\frac {1}{\lambda_ {X}}\right) ^ {1 / 6}. \tag {5.6}
$$

- Finally, we need to avoid the phenomenological constraints on  $X$ . In the limit  $m_{s} \gtrsim m_{X}$  the coupling of the chameleon field  $X$  to electrons  $g_{Xee} = \langle S \rangle m_{e} c_{ee} / M^{2}$  is enhanced compared to the one of the ALP and is bounded from below by

$$
g _ {X e e} \gtrsim g _ {X e e} ^ {\min } \equiv g _ {a e e} \left(\frac {\lambda_ {X}}{\lambda_ {S}}\right) ^ {1 / 2}. \tag {5.7}
$$

A conservative bound on the parameter space can be obtained by requiring  $g_{Xee}^{\mathrm{min}}$  to satisfy the stellar cooling constraints [108]. Setting  $g_{aee}$  to the XENON1T best fit and setting  $\lambda_S = 1$ , we get the maximal value of  $\lambda_X^{\mathrm{max}}$  allowed by stellar cooling constraints. In the mass range  $10^{-4}\mathrm{keV} \lesssim m_X \lesssim 10\mathrm{keV}$  the RG bounds are the most stringent, and we find,

$$
\lambda_ {X} \lesssim \lambda_ {X} ^ {\max } \equiv 7 \times 1 0 ^ {- 8} \left(\frac {2 . 6 \times 1 0 ^ {- 1 2}}{g _ {a e e}}\right) ^ {2} \left(\frac {g _ {X e e}}{6 . 7 \times 1 0 ^ {- 1 6}}\right) ^ {2} \left(\frac {\lambda_ {S}}{1}\right). \tag {5.8}
$$

The above reveals a hierarchy between the quartic of the PQ-breaking field  $\lambda_{S}$ , and that of the chameleon,  $\lambda_{X}$ , needed in order to make this model phenomenologically viable. This hierarchy might be difficult to realize quantum mechanically. For instance, three loop contributions to the singlet and chameleon quartics induced by their electron couplings, will act to make them both of the same order. Higher chameleon masses weaken the phenomenological bounds, allowing for a milder hierarchy between the couplings, but at the price of lowering the cut-off scale  $M$  as in dictated by eq. (5.3).

In summary, cALPs could avoid stellar cooling bounds. As shown in figure 14 right, the stellar cooling from dense stars can be circumvented if a new light scalar  $X$  controls

the coupling of the ALP to matter. If chameleon-like scalar  $X$  lies in the mass vs cut-off range shown in figure 14 left, its potential is modified by density dependent effects. In the simplest construction, the chameleon-like scalar can be light and the cut-off of the theory can be arranged to be sufficiently high if a hierarchy between the quartic of the PQ radial mode and the quartic of the chameleon is arranged as shown in figure 14 left.

Our cALP construction is still challenged by the Sun basins constraint pointed out in [106]. A possibility to relax this constraint, which we do not pursue here, is to suppress the solar production in order to relax stellar cooling bounds with respect to direct detection (see ref. [23] for a first discussion of such a possibility). Indeed, for a given suppression factor,  $\epsilon_{p} \ll 1$ , in the solar production of ALPs, the solar flux scales as  $\epsilon_{p} g_{aee}^{2}$ , while the solar detection rate scales as  $\epsilon_{p} g_{aee}^{4}$ . Increasing  $g_{aee}$ , while keeping the detection rate fixed, implies a relative suppression in the solar cooling bound, which scales as  $\epsilon_{p}^{1/2}$ . Achieving this suppression requires extra fine-tuning in the model presented here but could play an important role in generalizing cALPs to the case of light scalars and dark photons.

# 6 Dark matter-electron scattering

If DM interacts with electrons, it can scatter off the electrons in the target material and produce an electron recoil signal [15]. Due to the distinctive kinematics of this process, the electron recoil signal for "standard" DM-electron scattering peaks at recoil energies well below the keV energies needed to explain the XENON1T data; this standard process is thus in conflict with lower threshold direct-detection searches. However, we will investigate here whether other scenarios can explain the XENON1T data: exothermic scattering off electrons as well as DM-electron interactions that increase as a function of the momentum transfer (up to some cutoff scale). We will find that exothermic scattering off electrons work well, and momentum-dependent interactions also provide a potential explanation of the XENON1T excess.

# 6.1 Standard DM-electron scattering

We begin by reviewing the standard DM-electron scattering kinematics and formalism discussed in [15, 17], before discussing momentum-dependent and exothermic interactions. Consider a DM particle with mass  $m_{\chi}$  and initial velocity  $\mathbf{v}$ , which scatters off a bound electron, transferring a momentum  $\mathbf{q}$  to the electron. Energy conservation of the DM-atom system gives,

$$
\Delta E _ {e} + \frac {| m _ {\chi} \mathbf {v} - \mathbf {q} | ^ {2}}{2 m _ {\chi}} + \frac {q ^ {2}}{2 m _ {N}} = \frac {1}{2} m _ {\chi} v ^ {2}, (6. 1)
$$

where  $\Delta E_{e}$  is the energy transferred to the electron and  $m_N$  is the mass of the nucleus. This can be written as

$$
\Delta E _ {e} = \mathbf {q} \cdot \mathbf {v} - \frac {q ^ {2}}{2 \mu_ {\chi N}}. \tag {6.2}
$$

As the initial electron is in a bound state, it can have arbitrary momentum, and hence the momentum transfer  $\mathbf{q}$  could take any value. The maximum energy that can be deposited

is then found by maximizing the above equation with respect to  $q$ , and we get

$$
\Delta E _ {e} \lesssim \frac {1}{2} \mu_ {\chi N} v ^ {2}. \tag {6.3}
$$

For  $m_{\chi} \ll m_N$ ,  $\mu_{\chi N} \simeq m_{\chi}$ , and almost the entire kinetic energy of the incoming DM particle can be transferred to the electron. Since the typical DM halo velocity is  $v \sim 10^{-3}$ , a DM particle with mass of a few GeV can in principle produce a  $\mathcal{O}(\mathrm{keV})$  electron recoil. However, for DM with masses above the MeV scale, the typical momentum-transfer scale is set by the electron's momentum, given by  $q_{\mathrm{typ}} \sim Z_{\mathrm{eff}} \alpha m_e \sim Z_{\mathrm{eff}} \times 4 \mathrm{keV}$ , where  $Z_{\mathrm{eff}}$  is the effective charge seen by the electron. From eq. (6.2) (neglecting the second term, which is usually small),  $\Delta E_e \sim 10^{-3} q_{\mathrm{typ}} \sim Z_{\mathrm{eff}} \times$  few eV. While higher momentum transfers are possible, they are dramatically suppressed, since it is unlikely for the electron to have a momentum that is much higher than the typical momentum.

We can see this behavior in more detail by calculating the atomic form factor  $f_{1\rightarrow 2}(\mathbf{q})$  which captures the transition from state 1 to state 2,

$$
f _ {1 \rightarrow 2} (\mathbf {q}) = \int d ^ {3} x \psi_ {2} ^ {*} (\mathbf {x}) \psi_ {1} (\mathbf {x}) e ^ {i \mathbf {q} \cdot \mathbf {x}}, \tag {6.4}
$$

where  $\psi_{1}(\mathbf{x})$  ( $\psi_{2}(\mathbf{x})$ ) is the initial bound-state (final-state) electron wavefunction. There are various methods to calculate the wave functions. We here consider three different approaches for calculating the form factors:

- First, we follow [16], taking the initial bound-state wave functions from [129] and numerically solving the Schrödinger equation with a central potential that reproduces the bound state wavefunctions for the outgoing wave functions. We will refer to this scheme of form factors as the 'Non-relativistic' form factors as these do not take into account the relativistic corrections important at high momenta.  
- Another simple approximation for calculating the form factors without taking into account the relativistic corrections is to consider the outgoing wavefunctions as plane waves. We also consider this approach here and call the form factors so obtained as the 'Plane Wave' form factors. In this approach, we also do not subtract the identity operator from the operator  $e^{i\mathbf{q}\cdot \mathbf{x}}$ ; our 'Plane Wave' form factors will therefore not be correctly behaved for  $q \lesssim \mathcal{O}(\mathrm{keV})$ , since the outgoing wave functions are not orthogonal to the bound state wave functions. This issue ends up not affecting our results by much, since DM-electron scattering does not typically sample the atomic form factor at  $q \lesssim \mathcal{O}(\mathrm{keV})$ . Also, within this scheme, the form factors are multiplied by a Fermi factor (see below).  
- Finally, it is important to include the relativistic corrections for high  $q$ . We use the available atomic form factors with relativistic corrections computed in [130], calling them the 'Relativistic' form factors. These form factors are given for  $q \geq 100\mathrm{keV}$ .

In the left panel of figure 15, we plot the non-relativistic form factors  $|f_{nl} \to \Delta E_e - E_{nl}(\mathbf{q})|^2$  for different initial electron shells  $\{\mathrm{n,l}\}$  of the xenon atom and for two different values of

![](images/a430eee16c10eaaeced037740aad51d6ed405529ef7c3781f39086c52b3238a1.jpg)  
Figure 15. Left: Non-relativistic form factors for DM-electron scattering in xenon for the indicated electron shells for  $\Delta E_{e} = 1.5\mathrm{keV}$  (solid lines) and  $\Delta E_{e} = 8\mathrm{keV}$  (dashed lines), where  $\Delta E_{e}$  is the entire deposited energy. Right: Non-relativistic (solid lines), Plane Wave without Fermi factor (dashed lines) and Relativistic form factors (dot-dashed lines) for  $\Delta E_{e} = 3\mathrm{keV}$ .

![](images/c780f3b180e7a82c40cd81a1536c9052c4022ee53ff1cab805cd37361d0e93af.jpg)

$\Delta E_{e}$ . This corresponds to different final outgoing electron energies  $\Delta E_{e} - E_{nl}$ , where  $E_{nl}$  is the binding energy of the shell  $\{\mathrm{n},\mathrm{l}\}$ . We see that the form factor drops sharply for  $q \gtrsim \alpha m_{e}$ . For every shell, the peak also shifts to higher  $q$  for higher  $\Delta E_{e}$ . In order for an electron in any shell to give  $\Delta E_{e} \gtrsim 1\mathrm{keV}$ , we need  $q \gtrsim \mathrm{MeV}$  (see eq. (6.2)). This is possible, but highly suppressed.

In the right panel of figure 15, we compare the three different form factor schemes considered in this paper at a fixed value of  $\Delta E_{e} = 3\mathrm{keV}$ . We see that for  $q \gtrsim 500\mathrm{keV}$ , the relativistic corrections start becoming important. We also see that for  $q \gtrsim 200\mathrm{keV}$ , the plane wave calculation underestimates the form factor, justifying the inclusion of the Fermi factor in the calculation of the scattering rates (see below).

We can now write the cross section for the scattering rate as [15, 17]

$$
\sigma v _ {1 \rightarrow 2} = \frac {\bar {\sigma} _ {e}}{\mu_ {\chi e} ^ {2}} \int \frac {d ^ {3} q}{4 \pi} \delta \left(\Delta E _ {e} + \frac {q ^ {2}}{2 \mu_ {\chi N}} - \mathbf {q} \cdot \mathbf {v}\right) | F _ {\mathrm {D M}} (q) | ^ {2} | f _ {1 \rightarrow 2} (\mathbf {q}) | ^ {2}, \tag {6.5}
$$

where  $|F_{\mathrm{DM}}(q)|^2$  is the DM-electron interaction form factor and  $\overline{\sigma}_e$  is the reference DM-electron cross section defined as

$$
\overline {{| \mathcal {M} _ {\text {f r e e}} (\mathbf {q}) | ^ {2}}} \equiv \overline {{| \mathcal {M} _ {\text {f r e e}} (\alpha m _ {e}) | ^ {2}}} \times | F _ {\mathrm {D M}} (q) | ^ {2} \tag {6.6}
$$

$$
\bar {\sigma} _ {e} \equiv \frac {\mu_ {\chi e} ^ {2} | | \mathcal {M} _ {\mathrm {f r e e}} (\alpha m _ {e}) | ^ {2} |}{1 6 \pi m _ {\chi} ^ {2} m _ {e} ^ {2}}, \tag {6.7}
$$

where  $\overline{|\mathcal{M}_{\mathrm{free}}(\alpha m_e)|^2}$  is the absolute value squared of the matrix element describing the elastic scattering between DM and a free electron. While using the plane wave form factors,

we also include a Fermi factor in the scattering rate given by,

$$
F _ {\mathrm {f e r m i}} (\Delta E _ {e}, Z _ {\mathrm {e f f}}) = \frac {2 \pi \zeta}{1 - e ^ {- 2 \pi \zeta}}, \tag {6.8}
$$

with  $\zeta = Z_{\mathrm{eff}}\alpha \sqrt{\frac{m_e}{2E_e}}$ . We take  $Z_{\mathrm{eff}} = \{12.4, 14.2, 21.9, 25.0, 26.2, 39.9, 35.7, 35.6, 49.8, 39.8, 52.9\}$  for the shells  $\{5\mathrm{p}, 5\mathrm{s}, 4\mathrm{d}, 4\mathrm{p}, 4\mathrm{s}, 3\mathrm{d}, 3\mathrm{p}, 3\mathrm{s}, 2\mathrm{p}, 2\mathrm{s}, 1\mathrm{s}\}$  [131, 132]. The differential scattering rate will then be given by,

$$
\begin{array}{l} \frac {d R}{d \Delta E _ {e}} = \frac {\bar {\sigma} _ {e}}{8 \mu_ {\chi e} ^ {2}} \sum_ {n, l} \left(\Delta E _ {e} - E _ {n l}\right) ^ {- 1} \frac {\rho_ {\chi}}{m _ {\chi}} \tag {6.9} \\ \times \int q d q | F _ {\mathrm {D M}} (q) | ^ {2} | f _ {n l \to (\Delta E _ {e} - E _ {n l})} (\mathbf {q}) | ^ {2} \eta (v _ {\min} (q, \Delta E _ {e})), \\ \end{array}
$$

where we sum over all the occupied initial shells  $\{n,l\}$  with respective binding energies  $E_{nl}$ . The  $\eta (v_{\mathrm{min}})$  is defined by,

$$
\eta (v _ {\mathrm {m i n}}) = \int \frac {d ^ {3} v}{v} g _ {\chi} (v) \Theta (v - v _ {\mathrm {m i n}}), \tag {6.10}
$$

where  $v_{\mathrm{min}}$  is given by,

$$
v _ {\mathrm {m i n}} = \frac {\Delta E _ {e}}{q} + \frac {q}{2 m _ {\chi}}, \tag {6.11}
$$

and

$$
g _ {\chi} \left(\mathbf {v} _ {\chi}\right) \propto e ^ {- \frac {\left| \mathbf {v} _ {\chi} + \mathbf {v} _ {\mathrm {E}} \right| ^ {2}}{v _ {0} ^ {2}}} \Theta \left(v _ {\mathrm {e s c}} - \left| \mathbf {v} _ {\chi} + \mathbf {v} _ {\mathrm {E}} \right|\right), \tag {6.12}
$$

(normalized as  $\int d^3 v g_\chi(\mathbf{v}) = 1$ ) where  $\mathbf{v}_\chi$  is the DM velocity in the Earth frame, and  $\mathbf{v}_{\mathrm{E}}$  is the Earth's velocity in the galactic rest frame. We take a peak velocity of  $v_0 = 220~\mathrm{km / s}$ , an average Earth velocity of  $v_{\mathrm{E}} = 240~\mathrm{km / s}$ , and a galactic escape velocity of  $v_{\mathrm{esc}} = 544~\mathrm{km / s}$ . We set  $\rho_\chi = 0.4~\mathrm{GeV} / \mathrm{cm}^3$ .

The DM form factor depends on the precise DM-electron interaction, but we will consider

$$
F _ {\mathrm {D M}} = 1 \quad \text {“ h e a v y ” m e d i a t o r} \tag {6.13}
$$

$$
F _ {\mathrm {D M}} = \left(\frac {\alpha m _ {e}}{q}\right) ^ {2} \quad \text {l i g h t ” m e d i a t o r} \tag {6.14}
$$

$$
F _ {\mathrm {D M}} = \left(\frac {q}{\alpha m _ {e}}\right) \quad q \text {d e p e n d e n t} \tag {6.15}
$$

$$
F _ {\mathrm {D M}} = \left(\frac {q}{\alpha m _ {e}}\right) ^ {2} \quad q ^ {2} \text {- d e p e n d e n t “ h e a v y ” m e d i a t o r ,} \tag {6.16}
$$

where "heavy" and "light" refer to the mass of the mediator, which is respectively above or below the typical momentum transfer. The resulting differential DM-electron scattering rates for  $m_{\chi} = 10 \mathrm{GeV}$  are shown in figure 16 for  $\overline{\sigma}_e = 10^{-40} \mathrm{cm}^2$ .

For standard DM-electron scattering, we calculate the rates using plane wave atomic form factors and also using the relativistic form factors. We show both spectra in figure 16. We see that the relativistic corrections (dotted lines) predict a larger signal rate in the

![](images/eb27596eeb0e9cbe9d21aa9c0ec1eab8d04555260e50aa579a997519dba7596b.jpg)  
Figure 16. Electron recoil spectra for standard DM-electron scattering for  $m_{\chi} = 10 \, \mathrm{GeV}$  and  $\overline{\sigma}_e = 10^{-40} \, \mathrm{cm}^2$  for four different DM form factors. Solid lines show results calculated with plane waves as outgoing electron wave functions while the dotted lines include relativistic effects using results from [130]. See text for details.

region relevant for explaining the XENON1T excess than that predicted with plane wave form factors (solid lines).

We now briefly describe the different DM form factors, focusing first on their ability to fit the XENON1T excess without being in conflict with other direct detection experiments and then commenting on possible complementary probes related to the new physics scale encoded in the cutoff of the operators generating the DM-electron interaction.

"Heavy" a and light mediator. Due to the steep rise at low energy, the spectra for  $F_{\mathrm{DM}} \propto 1$  and especially  $F_{\mathrm{DM}} \propto 1 / q^2$  are unable to explain the XENON1T signal without being in dramatic conflict with lower-threshold direct-detection searches from, e.g., XENON1T (S2-only analysis) [44] (for heavy mediators) and SENSEI [45] (light mediators).

$q$ -dependent "heavy" mediator. A  $q$ -dependent form factor  $F_{\mathrm{DM}} = q / \alpha m_e$  does provide a reasonable fit to the XENON1T excess. The best-fit point is given by

$$
m _ {\chi} \gtrsim 9 0 \mathrm {G e V}, \quad \overline {{\sigma}} _ {e} = 2. 6 \times 1 0 ^ {- 4 5} \mathrm {c m} ^ {2} \times \left(\frac {m _ {\chi}}{1 \mathrm {G e V}}\right), \quad 2 \log (\mathcal {L} _ {S + B} / \mathcal {L} _ {B}) = 7. 3, \quad (6. 1 7)
$$

and the resulting spectrum is shown in figure 17 right. In figure 17 left we show the  $1\sigma$  and  $2\sigma$  regions in the  $\overline{\sigma}_e$  versus  $m_{\chi}$  parameter space. We include also a rough estimate of the signal yield of the S2-only analysis [44]. We consider two bins: (0.2, 0.5) keV and (0.5, 1) keV. We avoid considering the S2-only analysis above 1 keV to ensure that the dataset is completely independent from the one used to fit the signal. We impose a conservative bound by requiring a signal yield of less than 22 events in the (0.2, 0.5) keV bin, as well as less than 5 events in the (0.5, 1) keV bin. We see that the best-fit regions for the  $q$ -dependent heavy mediators are not constrained from the lower-threshold S2-only analysis.

![](images/dfc8e9b4302b8318ed37a689fa4e1c094810de25185c062ea52cea4d2d03783b.jpg)  
Figure 17. Left: Allowed parameter space for DM-electron scattering through a  $q$ -dependent heavy mediator, with  $F_{\mathrm{DM}} = q / \alpha m_e$ . The dark red regions are the  $1\sigma$  and  $2\sigma$  regions fitting the XENON1T excess. The green shaded region shows the current bound from the XENON1T only analysis based on S2 only. Dashed cyan lines show the scales at which the operator in eq. (6.18) is generated to obtain the corresponding cross section. Right: Signal shape for the best fit point in eq. (6.17). The black dots are the XENON1T data, the gray shaded region is the expected background, the blue line is the signal shape after smearing, and the blue shaded region is the resulting signal plus background distribution.

![](images/fc35180ac317d16ff3e3a1d12a09b67e0d7f9468fc3b0bf7baf2f889ddb78a65.jpg)

A  $q$ -dependent form factor is predicted, for example, by the dimension six operator,

$$
\frac {y _ {e} y _ {D} i \bar {\chi} \gamma_ {5} \chi \bar {e} e}{\Lambda_ {F} ^ {2}}, \tag {6.18}
$$

where  $\chi$  is the fermionic DM and the scalar-pseudoscalar interaction is induced by a heavy scalar which admits a spin dependent interaction with the DM. In the same plot we present contours of the cutoff scale divided by the square-root of the mediator-electron  $(y_{e})$  and mediator-DM  $(y_{D})$  couplings. Even by assuming  $y_{D}$  to be at its perturbativity bound and taking the coupling of the mediator to electrons or be order one, the required cutoff  $\Lambda_F$  of the effective operator in eq. (6.18) implies new physics below the GeV scale. This is likely to be excluded by collider bounds from electron-positron machines [60]. A possible way to raise the cut-off scale would be to consider a scalar DM  $\phi$  interacting with electron through the dimension five operator,

$$
\frac {y _ {e} y _ {D} \phi^ {*} \phi \bar {e} \gamma_ {5} e}{\Lambda_ {S}}, \tag {6.19}
$$

which leads to a  $q$ -dependent cross section, where the scalar DM interacts with the electron spin. The reduced dimensionality of this operator could help pushing the cut-off up to hundreds of GeVs thereby allowing a UV completion consistent with collider constraints and electron EDMs. However, a correct treatment of the spin-dependent interactions for the bounded electrons inside the xenon atom is necessary to correctly compute the DM-e cross section. We leave this interesting issue for future investigations.

![](images/f43930c758d1091528d3312704cab3b21922397a8cd787742917241a3d3ee315.jpg)  
Figure 18. Left: Allowed parameter space for DM-electron scattering through a  $q$ -dependent heavy mediator, with  $F_{\mathrm{DM}} = (q / \alpha m_e)^2$ . The dark red regions are the  $1\sigma$  and  $2\sigma$  bands of our fit to the XENON1T data. The green shaded region shows the current XENON1T bound from the S2 only analysis. Right: Signal shape for the best fit point in eq. (6.20). The black dots are the XENON1T data, the gray shaded region is the expected background, the blue line is the signal shape after smearing, and the blue shaded region is the resulting signal plus background distribution.

![](images/91368ec8db7d234da26a232e4fbe181a97e6bf7a0947668d8693d7ccdfc6b034.jpg)

$q^2$ -dependent "heavy" mediator. Last, we show in figure 18 the allowed parameter and best fit regions to the XENON1T data for the DM form factor  $F_{\mathrm{DM}} = (q / \alpha m_e)^2$  together with the bound from the XENON1T S2-only analysis [44]. The best fit point is given by

$$
m _ {\chi} = 1 1 \mathrm {G e V}, \quad \overline {{\sigma}} _ {e} = 6. 0 \times 1 0 ^ {- 5 0} \mathrm {c m} ^ {2}, \quad 2 \log (\mathcal {L} _ {S + B} / \mathcal {L} _ {B}) = 1 2. 3, \qquad (6. 2 0)
$$

and the resulting spectrum is shown in figure 18 right. As it is evident by comparing this result with the previous one for a  $q$ -dependent form factor, a stronger momentum dependence improves the XENON1T fit substantially.

A  $q^2$ -dependent form factor could be generated by operators such as

$$
\frac {y _ {e} y _ {D} \partial_ {\mu} \left(\phi^ {*} \phi\right) \partial^ {\mu} (\bar {e} e)}{\Lambda_ {S} ^ {3}}, \tag {6.21}
$$

and

$$
\frac {y _ {e} y _ {D} \bar {\chi} \gamma_ {5} \chi \bar {e} \gamma_ {5} e}{\Lambda_ {F} ^ {2}}, \tag {6.22}
$$

where again  $\phi$  is a scalar DM while  $\chi$  is a fermionic DM. The operator in eq. (6.21) could be obtained from the dimension six "derivative" Higgs portal  $\partial_{\mu}(\phi^{*}\phi)\partial_{\mu}(H^{\dagger}H) / \Lambda^{2}$  after the Higgs is integrated out. This will lead to an extra suppression of the Wilson coefficient proportional to  $m_e / m_h$  [133] if  $\Lambda \sim \Lambda_S \sim m_h$ . A very low cut-off scale,  $\Lambda_S$ , is then required to get a cross section in the ballpark of the one required by our fit of the XENON1T data, making this example not viable phenomenologically. The second operator in eq. (6.22) can

be obtained by integrating out a heavy axion coupled to fermionic DM and electrons. The expected cut-off for the range of cross section and DM masses of interest is always lower than  $1\mathrm{GeV}$  and hence in tension with colliders constraints. As mentioned earlier, a more in depth analysis should be performed in order to correctly account for the spin dependence on the electronic side.

We now turn our attention to exothermic DM, which can provide an even better fit to the XENON1T excess, and also has several interesting features that deserve further study.

# 6.2 Exothermic dark matter and electron recoils

DM could consist of two or more approximately degenerate particles, see e.g. [28, 29, 134-139]. We consider two states,  $\chi_{1}$  and  $\chi_{2}$ , with masses  $m_{\chi_1}$  and  $m_{\chi_2} = m_{\chi_1} + \delta$ , respectively, with  $|\delta| \ll m_{\chi_1}, m_{\chi_2}$ . For example,  $\chi_{1}$  and  $\chi_{2}$  could be two Majorana fermions that originated from a Dirac fermion that is charged under a new U(1) gauge symmetry; if there are mass terms for the Dirac fermion that break the U(1) symmetry, it is possible to split them into the two Majorana fermions, with the gauge boson coupling off-diagonally to  $\chi_{1}$  and  $\chi_{2}$ . Similarly, one can consider two real scalars that originated from a complex scalar. In what follows, we will always take  $\chi_{1}$  to be the incoming state, which then scatters off ordinary matter and converts to  $\chi_{2}$  (which in our notation is always the outgoing state). The scenario where  $\chi_{2}$  is heavier than  $\chi_{1}$  is often called "inelastic" DM [134] ( $\delta > 0$ ), while the scenario where  $\chi_{1}$  is heavier than  $\chi_{2}$  is often called "exothermic" DM ( $\delta < 0$ ); in the context of direct-detection experiments, the latter was previously discussed for DM-nuclear scattering in [28, 29] and for DM-electron scattering in [30].

The relic abundance of the two states depends on the precise model. In the minimal scenario above and for  $|\delta|$  sufficiently small (typically  $\lesssim 2m_e$ ), the lifetime of the heavier state for decays via the (off-shell) mediator into the lighter state plus two neutrinos, or for decays into the lighter state plus three photons, is easily much longer than the age of the universe [137, 138]. However, the fractional abundance of the heavier state after freeze-out in the early universe will depend sensitively on the precise DM-mediator interaction strength and the DM and mediator masses [137, 138]. For sub-GeV DM, the abundance of the heavier state will typically be small. However, even a small fractional abundance of the heavier state can leave dramatic signals in direct-detection experiments, since, as we will see, the mass splitting  $|\delta|$  can be entirely converted into kinetic energy of the electron when scattering off of it in a target material. The exothermic scenario allows all relic particles in the halo to scatter, while the inelastic up-scatter of the lighter to the heavier state will be highly suppressed for  $|\delta| \gg 10$ 's of eV.

We focus here on exothermic scattering, since it is able to explain the XENON1T excess. In section 6.2.1, we discuss the kinematics and also provide best-fit regions to the XENON1T excess that are independent of the precise relic abundance of the heavier state, before considering concrete models in section 6.2.2.

# 6.2.1 Exothermic dark matter-electron scattering: kinematics and best-fit regions

We assume that the incoming DM particle,  $\chi_{1}$ , transfers momentum  $\mathbf{q}$  to the target electron and converts to the lighter (outgoing) state,  $\chi_{2}$ . In contrast to eq. (6.2), the energy-conservation equation now reads

$$
\Delta E _ {e} + \frac {\left| m _ {\chi_ {1}} \mathbf {v} - \mathbf {q} \right| ^ {2}}{2 m _ {\chi_ {2}}} + \frac {q ^ {2}}{2 m _ {N}} + m _ {\chi_ {2}} = \frac {1}{2} m _ {\chi_ {1}} v ^ {2} + m _ {\chi_ {1}}, \tag {6.23}
$$

where  $\Delta E_{e}$  is again the energy transferred to the electron. Assuming a small mass-splitting compared to the mass scale of the DM i.e.  $|\delta |\ll m_{\chi_1}\sim m_{\chi_2}$ , we can simplify this as,

$$
\Delta E _ {e} = \mathbf {q} \cdot \mathbf {v} - \frac {q ^ {2}}{2 m _ {\chi_ {2} , N}} - \delta . \tag {6.24}
$$

In contrast to the "standard" DM-electron scattering discussed above ( $\delta = 0$ ) (and in contrast also with exothermic nuclear scattering, see below),  $\Delta E_{e}$  can be well above the "typical" energy transfers of  $\Delta E_{e} \sim 10^{-3} q_{\mathrm{typ}} \sim Z_{\mathrm{eff}} \times$  few eV applicable for  $\delta = 0$ . In particular, for  $\delta \sim \mathcal{O}(-\mathrm{keV})$ , the electron recoil spectrum will be peaked at  $\mathcal{O}(\mathrm{keV})$ , and can explain the XENON1T excess. Below, since  $m_{\chi_1} \sim m_{\chi_2}$ , we will often simply denote the DM mass as  $m_{\chi}$ . Also, for the calculation of exothermic DM-electron scattering, we consider non-relativistic atomic form factors.

The differential scattering rate is given by

$$
\begin{array}{l} \frac {d R}{d \Delta E _ {e}} = \frac {\bar {\sigma} _ {e}}{8 \mu_ {\chi e} ^ {2}} \sum_ {n, l} \left(\Delta E _ {e} - E _ {n l}\right) ^ {- 1} \frac {\rho_ {\chi 1}}{m _ {\chi 1}} \tag {6.25} \\ \times \int q d q | F _ {\mathrm {D M}} (q) | ^ {2} | f _ {n l \rightarrow \Delta E _ {e} - E _ {n l}} (\mathbf {q}) | ^ {2} \eta (v _ {\mathrm {m i n}} (q, \Delta E _ {e})), \\ \end{array}
$$

where the minimum velocity to scatter is given by

$$
v _ {\min } = \left| \frac {\Delta E _ {e} + \delta}{q} + \frac {q}{2 \mu_ {\chi 2 , N}} \right|. \tag {6.26}
$$

As there is an upper bound of  $v_{\mathrm{max}} = v_{\mathrm{esc}} + v_{\mathrm{E}}$  on the DM halo velocity, we get upper and lower bounds on the allowed values of  $q$  for a given  $m_{\chi}$  and a fixed  $\Delta E_{e}$ ,

$$
q _ {\min } = \operatorname {s i g n} \left(\Delta E _ {e} + \delta\right) m _ {\chi} v _ {\max } \left(1 - \sqrt {1 - \frac {\left(\Delta E _ {e} + \delta\right)}{\frac {1}{2} m _ {\chi} v _ {\max } ^ {2}}}\right), \tag {6.27}
$$

$$
q _ {\mathrm {m a x}} = m _ {\chi} v _ {\mathrm {m a x}} \left(1 + \sqrt {1 - \frac {(\Delta E _ {e} + \delta)}{\frac {1}{2} m _ {\chi} v _ {\mathrm {m a x}} ^ {2}}}\right). \tag {6.28}
$$

For DM scattering off electrons through a light mediator  $[F_{\mathrm{DM}} = (\alpha m_e / q)^2]$ , the scattering rate diverges at low  $q$ ; this was not a problem for the case  $\delta = 0$ , since requiring a sizable value for  $\Delta E$  also forces  $q$  to be sizable. However, as we will discuss, this is not true anymore for exothermic scattering: a sizable  $\Delta E$  can be obtained even for very small  $q$ . To remove the resulting divergence in this case, we will consider that the light mediator is

a light dark photon, which couples to electric charge. At low  $q$ , Thomas-Fermi screening will then naturally regulate the divergence. We implement Thomas-Fermi screening as discussed in [140, 141], using a Thomas-Fermi radius (called  $a'$  in [141]) from [142].

Consider first DM masses of  $\mathcal{O}(\mathrm{GeV})$ . From eq. (6.28), we see that the value of  $q_{\mathrm{max}}$  is near  $m_{\chi}v_{\mathrm{max}} \sim \mathcal{O}(\mathrm{MeV})$ , which is much higher than  $q_{\mathrm{typ}}$ . Thus, the recoil spectrum in  $\Delta E_e$  depends on the behavior of  $q_{\mathrm{min}}$  as a function of  $\Delta E_e$ . From eq. (6.27), we see that, for  $\delta = 0$  and  $\Delta E_e \sim \mathcal{O}(\mathrm{keV})$ ,  $q_{\mathrm{min}} \gg q_{\mathrm{typ}}$  and therefore the integral over  $q$  misses the peak of the form-factor, leading to strongly suppressed scattering rates (as discussed above). However, for  $\delta \sim \mathcal{O}(-\mathrm{keV})$ , we see that  $q_{\mathrm{min}} = 0$  when  $\Delta E_e = |\delta|$ . For  $\Delta E_e$  smaller or larger than  $|\delta|$ ,  $q_{\mathrm{min}}$  increases and the available phase space decreases again, thus giving a suppression in the rate. Hence, for  $m_{\chi} \sim \mathcal{O}(\mathrm{GeV})$  and  $\delta \sim \mathcal{O}(-\mathrm{keV})$ , we get a sharp peak in the spectrum at  $\Delta E_e \sim |\delta|$ .

In figure 19, the solid lines show spectra for  $m_{\chi} = 1$  GeV for  $\delta = -2.5$  keV (left) and  $\delta = -4$  keV (right) for  $f_{\chi_1}\overline{\sigma}_e = 10^{-40}$  cm² and for three different form factors. Here the fractional abundance of the incoming DM particle,  $\chi_1$ , is  $f_{\chi_1} = \frac{n_{\chi_1}}{n_{\chi_1} + n_{\chi_2}}$ , with  $n_{\chi_1}(n_{\chi_2})$  being the number density of  $\chi_1(\chi_2)$ . We see that the spectrum is sharply peaked at  $|\delta|$  and is reminiscent of a DM absorption signal, which provides an adequate fit to the XENON1T excess.

We next consider  $m_{\chi} \sim \mathcal{O}(\mathrm{MeV})$ , showing the resulting spectra in figure 19, where the dashed lines show spectra for  $m_{\chi} = 1$  MeV for  $\delta = -2.5$  keV (left) and  $\delta = -4$  keV (right), both for incoming DM mass fraction  $f_{\chi_1}\overline{\sigma}_e = 10^{-40}$  cm² and for three different form factors. The spectrum has a wide peak, wider than for heavier exothermic DM and wider than a DM absorption signal, which (for the larger value of  $|\delta|$ ) provides a very good fit to the XENON1T data.

We can understand the shape of the spectra for  $m_{\chi} \sim \mathcal{O}(\mathrm{MeV})$  as follows. If  $\delta \sim \mathcal{O}(-\mathrm{keV})$ ,  $q_{\mathrm{min}} = 0$  at  $\Delta E_e = |\delta|$ . However,  $q_{\mathrm{max}}$  is now only a few keV, and we see from figure 15 that the  $q_{\mathrm{typ}}$  for  $\Delta E_e \sim \mathcal{O}(\mathrm{keV})$  is higher. Note that for such small  $m_{\chi}$ , there is barely any kinetic energy in the DM to give recoil energies larger than  $|\delta|$ , which is already around keV. So the spectrum sharply cuts off above  $\Delta E_e \sim |\delta|$ . For  $F_{\mathrm{DM}} \propto 1/q^2$ , the spectrum is peaked roughly at  $\Delta E \sim |\delta|$  (due to the enhancement of the integrand of eq. (6.25) at  $q \to 0$ ). However, for  $F_{\mathrm{DM}} \propto 1$  and  $F_{\mathrm{DM}} \propto q$ , the peak (for a fixed  $|\delta|$ ) occurs at energies less than  $|\delta|$ . The reason is that for  $\Delta E_e < |\delta|$ , both  $q_{\mathrm{min}}$  and  $q_{\mathrm{max}}$  increase, and at some  $\Delta E_e$  below  $|\delta|$ , the allowed values of  $q$  cross the peak of the form factor. Hence, we see a peak in the spectrum for  $\Delta E_e$  below  $|\delta|$ . Moreover, the spectrum is not as sharply peaked as it is for heavier DM, since for heavier DM the allowed values of the momentum transfer are always  $q \sim \mathcal{O}(\mathrm{keV}) \sim q_{\mathrm{typ}}$ . In order to have the spectrum peak near 2.5 keV (which gives a good fit to the XENON1T data), one then needs larger values of  $|\delta|$ . However, for  $|\delta| \gtrsim 4.9\mathrm{keV}$ , the 2s- and 2p-shells can also be excited, leading to additional peaks in the spectrum. The precise spectrum thus depends sensitively on the DM mass and splitting. In our parameter scans below, we do not attempt to cover the entire (sub-)MeV-scale DM parameter space.

In figure 20, we show the  $1\sigma$  and  $2\sigma$  best-fit regions that explain the XENON1T excess for a heavy mediator ( $F_{\mathrm{DM}} = 1$ ) in the  $\delta - m_{\chi_1}$  plane (left) and the  $\overline{\sigma}_{e} - m_{\chi_1}$  plane (middle).

![](images/cf01ae937d66492b859b5fd9464a5ba2d438ef964fdc94433000f9a15c1d873e.jpg)  
Figure 19. Differential recoil spectra for "exothermic" DM, in which a heavy incoming DM state,  $\chi_{1}$ , scatters off an electron and converts to a lighter (outgoing) DM state,  $\chi_{2}$ , which is lighter by  $\delta = -2.5\mathrm{keV}$  (left) and  $\delta = -4\mathrm{keV}$  (right). We show  $m_{\chi_1} = 1$  GeV (solid) and  $m_{\chi_1} = 1$  MeV (dashed). We consider three DM form factors,  $F_{\mathrm{DM}} = 1$  (blue),  $F_{\mathrm{DM}} = (\alpha m_e / q)^2$  (orange), and  $F_{\mathrm{DM}} = (q / \alpha m_e)$  (green).

![](images/e5c51a045287278de3492217ef78074e4fc6c59446164ea6f89dd7892af01aad.jpg)

![](images/37bb86013b2b7e7a684072c90012934c4d5e6a6e263844d958765a3a435335dd.jpg)  
Figure 20. The  $1\sigma$  and  $2\sigma$  best-fit regions that explain the XENON1T excess for exothermic DM and a heavy mediator  $(F_{\mathrm{DM}} = 1)$  in the  $f_{\chi_1}\overline{\sigma}_e$  versus  $\delta$  plane for  $m_{\chi} = 30\mathrm{MeV}$ $(f_{\chi_1} = \frac{n_{\chi_1}}{n_{\chi_1} + n_{\chi_2}})$  (left), and in the  $f_{\chi_1}\overline{\sigma}_e$  versus  $m_{\chi}$  plane for  $|\delta| = 2.5\mathrm{keV}$  (middle). In the right plot, we show an example of the predicted spectrum for the best-fit value with  $|\delta| \leq 4.9\mathrm{keV}$  in eq. (6.29). The dashed and solid lines show the signal spectrum before and after detector smearing effects, respectively. The measured XENON1T data is shown as black dots while the gray-shaded and blue-shaded regions are the expected binned background and signal respectively.

![](images/764882f68cf6a2ec1ee46c483e3725cb9fb18ff85d0142850213f20d42071c71.jpg)

![](images/abbd7b6c1cde6d08424feb203d2f047248b4fcfcd4bff9e0f2f1dd5915f8fe09.jpg)

![](images/ac927117ae03227b33b0ada321e78bde6e797df17960ef9c179f212539518884.jpg)  
Figure 21. The  $1\sigma$  and  $2\sigma$  best-fit regions that explain the XENON1T excess for exothermic DM and a light mediator  $(F_{\mathrm{DM}} = (\alpha m_e / q)^2))$  in the  $f_{\chi_1}\overline{\sigma}_e$  versus  $\delta$  plane for  $m_{\chi} = 0.55\mathrm{MeV}$ $(f_{\chi_1} = \frac{n_{\chi_1}}{n_{\chi_1} + n_{\chi_2}})$  (left), and in the  $f_{\chi_1}\overline{\sigma}_e$  versus  $m_{\chi}$  plane for  $|\delta | = 2.5\mathrm{keV}$  (middle). The blue-shaded region has not been included in our scan because the second xenon shells would be excited (see text for details). In the right plot, we show an example of the predicted spectrum for the best-fit value with  $|\delta |\leq 4.9~\mathrm{keV}$  from eq. (6.30). The dashed and solid lines show the signal spectrum before and after detector smearing effects, respectively. The measured XENON1T data is shown as black dots while the gray-shaded and blue-shaded regions are the expected binned background and signal respectively.

![](images/91a52448bab4936fe55615808fe10037c6ef43609898000885eefc1a109f17e7.jpg)

![](images/b5b050f54b2475e02911ba028845ee69c5cca0b0728e4e79cd8a209034e67133.jpg)

We see that the best-fit point (with  $|\delta| \leq 4.9\mathrm{keV}$ ) is given by

$$
m _ {\chi} \simeq 3 0 \mathrm {M e V}, \quad | \delta | \simeq 2. 6 \mathrm {k e V}, \quad f _ {\chi_ {1}} \bar {\sigma} _ {e} \simeq 2. 3 \times 1 0 ^ {- 4 6} \mathrm {c m} ^ {2}, \quad 2 \log \left(\mathcal {L} _ {S + B} / \mathcal {L} _ {B}\right) \simeq 1 5. 7. \tag {6.29}
$$

In the right plot, we show how the signal at the best-fit point compares with the XENON1T data and background model. In figure 21, we show the corresponding plots for a light mediator  $(F_{\mathrm{DM}}\propto 1 / q^2)$ . Here the best-fit point is given by

$$
m _ {\chi} \simeq 0. 5 5 \mathrm {M e V}, \quad | \delta | \simeq 4. 9 \mathrm {k e V}, \quad f _ {\chi 1} \bar {\sigma} _ {e} \simeq 1. 3 \times 1 0 ^ {- 4 3} \mathrm {c m} ^ {2}, \quad 2 \log \left(\mathcal {L} _ {S + B} / \mathcal {L} _ {B}\right) \simeq 1 6. 7. \tag {6.30}
$$

Finally, in figure 22, we show the corresponding plots for a  $q$ -dependent heavy mediator  $(F_{\mathrm{DM}} \propto q)$ ; here the best-fit point is given by

$$
m _ {\chi} \simeq 7 8 0 \mathrm {M e V}, \quad | \delta | \simeq 2. 5 \mathrm {k e V}, \quad f _ {\chi_ {1}} \bar {\sigma} _ {e} \simeq 1. 2 \times 1 0 ^ {- 4 7} \mathrm {c m} ^ {2}, \quad 2 \log \left(\mathcal {L} _ {S + B} / \mathcal {L} _ {B}\right) \simeq 1 5. 8. \tag {6.31}
$$

We see that exothermic DM can explain well the observed XENON1T ER spectrum.

We now make a few comments:

- The inclusion of relativistic corrections when calculating the atomic form factors is not essential for exothermic scattering, since  $q$  is not forced to be large to obtain a large  $\Delta E_{e}$  and the form factors typically peak at values of  $q$  below which relativistic corrections become important. We therefore neglect relativistic corrections in our calculations.  
- While  $m_{\chi} \sim 1$  GeV provides an adequate fit to the XENON1T excess, one can obtain an even better fit for heavy DM by imagining that DM consists of three or more states.

For example, for three states  $\chi_1$ ,  $\chi_2$ , and  $\chi_3$ , with mass splitting  $\delta_{21} \equiv m_{\chi_2} - m_{\chi_1}$ ,  $\delta_{31} \equiv m_{\chi_3} - m_{\chi_1}$ , and  $\delta_{32} \equiv m_{\chi_3} - m_{\chi_2}$ , with  $\delta_{21}$ ,  $\delta_{31}$ ,  $\delta_{32}$  all negative, the electron recoil spectrum would show up to three peaks. Of course, the actual size of the various peaks will depend sensitively on the relic abundances of the three DM states, and hence depend sensitively on the model parameters.

- If the DM couples also to nuclei (for example, if the mediator is a dark photon), DM could scatter exothermically off nuclei. We can contrast the kinematics for exothermic DM scattering off electrons with the kinematics for exothermic DM scattering off nuclei. For exothermic scattering off nuclei, the mean recoil energy is  $\langle E_R\rangle \sim \frac{|\delta|\mu_{\chi_1,N}}{m_N}$  where  $m_N$  is the mass of the nucleus and  $\mu_{\chi_1,N}$  is the reduced mass of  $\chi_1$  and the nucleus; the spread in energy around the mean recoil energy is given by  $\Delta E_R \sim \frac{\mu_{\chi_1,N}}{m_N}\sqrt{8|\delta|\mu_{\chi_1,N}v^2}$  [28, 29]. For  $\chi_1$  scattering off a xenon atom, with  $m_{\chi_1} \sim 1\mathrm{GeV}$  and  $\delta \sim 1\mathrm{keV}$ ,  $\langle E_R\rangle \sim 8\mathrm{eV}$ , while the typical spread in energy around the mean recoil energy for the same parameters and a DM velocity of  $v \sim 10^{-3}$  is  $\Delta E_R \sim 21\mathrm{eV}$ . This is below the XENON1T and many other experimental thresholds, although not below the threshold achieved by CRESST-III; we will discuss this further in section 6.2.2.  
- It is possible to obtain electron recoils from the Migdal effect when DM scatters exothermically off nuclei; this could lead to additional constraints, which requires a careful study that we leave to future work.  
- As mentioned above, the fractional abundance of the heavier state after freeze-out in the early universe will depend sensitively on the precise DM-mediator interaction strength and the DM and mediator masses. Moreover, in a concrete model there will typically also be other constraints from searches at beam dumps, fixed-target experiments, and colliders. We investigate two concrete models in section 6.2.2.

# 6.2.2 Exothermic dark matter-electron scattering: relic abundance for concrete models

In the case of exothermic DM, it is of crucial importance to calculate the relic abundance of the heavier state after freeze-out in the early Universe. We consider the case where the standard freeze-out is dominated by the annihilations into SM fermions  $\chi_{1}\chi_{2} \leftrightarrow f\bar{f}$ . After the dark states freeze out from the SM bath, they continue to be in chemical equilibrium and scatter with each other,  $\chi_{2}\chi_{2} \leftrightarrow \chi_{1}\chi_{1}$ , driving the relative abundance to the equilibrium value

$$
f ^ {*} \equiv n _ {\chi_ {2}} / n _ {\chi_ {1}} \simeq e ^ {- | \delta | / T _ {\chi} ^ {*}}, \tag {6.32}
$$

where  $T_{\chi^*}$  is the temperature of the dark sector at which the DM-DM scattering decouples [134, 137, 138]. If  $T_{\chi^*}$  is much lower than the mass splitting  $|\delta|$ , the relative fraction of the excited states will be exponentially suppressed. In what follows, we compute the temperature of chemical decoupling  $T_{\chi^*}$  in two explicit simple models of exothermic DM. $^4$

![](images/1167caecda16f63ae258e0abbd373c925d9c2cedb2898b687664701c68711c03.jpg)  
Figure 22. The  $1\sigma$  and  $2\sigma$  best-fit regions that explain the XENON1T excess for exothermic DM and a momentum-dependent heavy mediator ( $F_{\mathrm{DM}} = (q / \alpha m_e)$ ) in the  $f_{\chi_1}\overline{\sigma}_e$  versus  $\delta$  plane for  $m_{\chi} = 780\mathrm{MeV}$  ( $f_{\chi_1} = \frac{n_{\chi_1}}{n_{\chi_1} + n_{\chi_2}}$ ) (left), and in the  $f_{\chi_1}\overline{\sigma}_e$  versus  $m_{\chi}$  plane for  $|\delta| = 2.5\mathrm{keV}$  (middle). In the right plot, we show an example of the predicted spectrum for the best-fit value with  $|\delta| \leq 4.9\mathrm{keV}$  from eq. (6.31). The dashed and solid lines show the signal spectrum before and after detector smearing effects, respectively. The measured XENON1T data is shown as black dots while the gray-shaded and blue-shaded regions are the expected binned background and signal respectively.

![](images/3222ce1c8f090b5a62de38186f751a5e471a3b537f18bfe90613df7e027a69fa.jpg)

![](images/86c862cd896b1e587901e254e119ca0e3cc827e2d824fd2168497422477aa92e.jpg)

We study models where the coupling between the SM and the DM sector arises via the kinetic mixing of the dark photon with the SM photon. We discuss both the cases of a complex scalar DM and a pseudo-Dirac fermion DM, which have very similar parametrical dependence on the physical quantities up to numerical factors. The cosmology of the pseudo-Dirac DM and its implications for the XENON1T excess have been recently considered in [143, 144]. Our treatment of the cosmology here agrees with the one first presented in [143]. For the cosmology of the scalar case, we follow a similar treatment, obtaining results that agree with [145]. The final allowed parameter space compatible with the XENON1T excess will be somewhat different than the previous analyses because of our improved statistical analysis of the XENON1T data and a different treatment of the atomic form factors.

The interaction Lagrangian between the SM and the dark sector reads

$$
\mathcal {L} \supset g _ {D} A ^ {\prime \mu} J _ {\mu} ^ {\mathrm {D M}} + \frac {\epsilon}{2} F _ {\mu \nu} F ^ {\prime \mu \nu}, \tag {6.33}
$$

where  $F_{\mu \nu}^{\prime}$  is the field strength of the dark U(1),  $g_{D} \equiv \sqrt{4\pi\alpha_{D}}$  is the dark photon coupling, and  $J_{\mu}^{\mathrm{DM}}$  the dark matter current given by

$$
\text {s c a l a r D M :} J _ {\mu} ^ {\mathrm {D M}} = - i \left(\phi \partial_ {\mu} \phi^ {*}\right) = \chi_ {1} \partial_ {\mu} \chi_ {2} - \chi_ {2} \partial_ {\mu} \chi_ {1}, \tag {6.34}
$$

$$
\text {f e r m i o n i c D M :} \quad J _ {\mu} ^ {\mathrm {D M}} = - i \left(\bar {\psi} \gamma_ {\mu} \psi\right) = - i \left(\chi_ {1} ^ {\dagger} \bar {\sigma} _ {\mu} \chi_ {2} - \chi_ {2} ^ {\dagger} \bar {\sigma} _ {\mu} \chi_ {1}\right), \tag {6.35}
$$

where we write the complex scalar current in terms of the real scalar components  $\phi = (\chi_1 + i\chi_2) / \sqrt{2}$  and the Dirac fermionic current in terms of its Weyl components  $\bar{\psi} = (\chi_{2},\chi_{1}^{\dagger})$

The mass terms in the two models can be written as

$$
\text {s c a l a r D M :} \quad \mathcal {L} _ {m} = m ^ {2} \phi^ {*} \phi + y _ {D} ^ {2} H _ {D} ^ {2} \phi^ {2} + \mathrm {h . c}, \tag {6.36}
$$

$$
\text {f e r m i o n i c D M :} \quad \mathcal {L} _ {m} = m \bar {\psi} \psi + y _ {D} H _ {D} \psi^ {2} + \mathrm {h . c}, \tag {6.37}
$$

where the VEV of the dark Higgs  $H_{D}$  breaks the  $\mathrm{U}(1)$  in the dark sector, generating a mass splitting between  $\chi_{1}$  and  $\chi_{2}$

$$
\mathrm {s c a l a r D M :} \quad \delta \simeq \frac {y _ {D} ^ {2} \langle H _ {D} \rangle^ {2}}{m}, \qquad \mathrm {f e r m i o n D M :} \quad \delta \simeq y _ {D} \langle H _ {D} \rangle . \qquad (6. 3 8)
$$

The splitting can be easily suppressed compared to the mass  $m$ . As long as  $y_{D}$  is small enough, the mass of the dark Higgs can be made arbitrarily heavy and, hence, will be neglected in the rest of our discussion.

The freeze out of the  $\chi_{1}\chi_{2} \leftrightarrow f\bar{f}$  interactions fixes the total number density of dark sector states  $n_{\chi_1} + n_{\chi_2} \simeq n_{\chi_1}$ . This can be chosen to match the DM abundance today if  $y = \alpha_D \epsilon^2 (m_\chi / m_{A'})^4$  is fixed as a function of the DM mass. In the limit  $m_A' \gtrsim m_{\chi_1} \gtrsim m_e$ , we find roughly

$$
\text {s c a l a r D M :} y \sim 1 0 ^ {- 8} \left(\frac {m _ {\chi_ {1}}}{1 0 0 \mathrm {M e V}}\right) ^ {2}, \tag {6.39}
$$

$$
\text {f e r m i o n i c D M :} y \sim 1 0 ^ {- 1 0} \left(\frac {m _ {\chi_ {1}}}{1 0 0 \mathrm {M e V}}\right) ^ {2}. \tag {6.40}
$$

The precise relation dependence of  $y$  on the DM mass needs to be extracted numerically [146] (see also [17, 147]).

The compute the relative abundance of  $n_{\chi_2} / n_{\chi_1}$ , we need to consider the rate of the process  $\chi_2\chi_2 \leftrightarrow \chi_1\chi_1$

$$
\Gamma_ {\chi_ {2} \chi_ {2} \leftrightarrow \chi_ {1} \chi_ {1}} = e ^ {- | \delta | / T _ {\chi}} n _ {\chi_ {1}} \langle \sigma_ {\chi_ {2} \chi_ {2} \leftrightarrow \chi_ {1} \chi_ {1}} v \rangle , \tag {6.41}
$$

where the thermally averaged scattering cross section reads

$$
\langle \sigma_ {\chi_ {2} \chi_ {2} \leftrightarrow \chi_ {1} \chi_ {1}} v \rangle \simeq \frac {1 6 \kappa \sqrt {2} \pi \alpha_ {D} ^ {2} m _ {\chi} ^ {3 / 2}}{m _ {A ^ {\prime}} ^ {4}} \max  \left(2 T _ {\chi} / \pi , \delta\right) ^ {1 / 2}, \tag {6.42}
$$

and we introduce the numerical coefficient  $\kappa = (1,1 / 4)$  to distinguish the scalar and fermionic cases. This formula agrees with the results of [143] and [145] in the fermionic and scalar case, respectively. The dependence on  $\delta$  arises from the threshold velocity for the scattering process, and in most of the parameter space of interest  $|\delta |\gtrsim 2T / \pi$ . The chemical decoupling temperature  $T_{\chi}^{*}$  is then defined as  $\Gamma_{\chi_1\chi_2}(T_\chi^*)\simeq H(T_\chi^*)$ .

In figure 23, we show in red the  $1\sigma$  and  $2\sigma$  best-fit regions for the case of a heavy dark photon mediator with mass  $m_{A'} = 3m_{\chi}$  and  $\alpha_{D} = 0.5$  ( $\alpha_{D} = 2$ ) for the fermion (scalar) case. The required electronic interaction cross section  $\bar{\sigma}_{e}$ , defined in eq. (6.5), needs to be larger for lower DM masses because the fraction of primordial excited states rapidly decreases for lower DM mass. Indeed, the rate of de-excitation scales as  $\Gamma_{\chi_1\chi_2} \sim m_{\chi}^{-7/2}$ , which then implies  $f^* \sim m_{\chi}^{7/2}$ .

![](images/8071136c16fc4277e20fdbe2a6a9b31f65dd5d5548bbb0e8a8c87549c69c0815.jpg)  
Figure 23. The red regions indicate the  $1\sigma$  and  $2\sigma$  best-fit regions for exothermic DM in which the DM states consist of two scalars (left) or two fermions (right) that are split in mass by an amount  $\delta = 2.5\mathrm{keV}$ , and interact through a dark photon mediator with mass  $m_{A'} = 3m_{\chi}$  and coupling  $\alpha_{D} = 2$  (left) and  $m_{A'} = 3m_{\chi}$  and  $\alpha_{D} = 0.5$  (right). The XENON1T signal is produced from the heavy state (down)scattering to the lighter state. We show also the bounds on accelerator-based searches: in blue the bound from the NA64 experiments [148], in dark orange the BABAR constraint [61, 149], in purple the bound from LSND [150, 151], in cyan the bound from E137 [152]. The dotted light-red line shows the reach of LDMX [153], while the dotted dark-red line shows the reach of Belle-II [61, 154]. The light green shaded region is the bound from the heavy state scattering exothermically off nuclei in CRESST-III [155, 156]. We also show the limit from self interaction (dotted red vertical line) [157] and from CMB distortion due to energy injection (dark yellow) for the fermionic case [158, 159]. Dotted black vertical lines indicate the fractional relic abundance,  $f^{*}$ , of the excited state.

![](images/35026cf887f5e63d0bbad7e2626d9e5c8f98c86d70fd97304f572b5bea83c664.jpg)

In the fermionic model, for values of the cross section that explain the XENON1T excess it is easy to get the correct DM relic abundance for perturbative values of  $\alpha_{D}$ . This result is in agreement with previous analysis [143, 144]. Conversely, in the scalar case, fitting the XENON1T excess pushes the parameter space with the relic abundance to values for  $\alpha_{D}$  that are at the boundary of perturbativity [160]. Alternatively, one could explore a region of parameter space where the DM mass is almost degenerate with the dark photon mass, and resonant effects enhance the annihilation cross section [161]. Of course, this is a specific feature of the simple models presented here and adding further annihilation channels within the dark sector could open the parameter space substantially at the price of a less minimal model.

In figure 23, we show the accelerator constraints on the dark photon decaying "invisibly" to DM: the BABAR constraint from a monophoton search  $e^{+}e^{-}\rightarrow \gamma A^{\prime}$  [61, 149] (dark orange solid line), from an electron-beam-dump missing-energy search induced by dark photon bremsstrahlung (to DM) at NA64 [148] (blue solid line), and the projections from LDMX [153] and Belle-II [61, 154]. We show the bound on a DM beam produced in

high-intensity beam dump experiments such as E137 [152] or neutrino experiments such as LSND [150, 151]. We display the self-interaction constraints (dotted red vertical line) [157]  $\sigma_{\mathrm{SI}} / m_{\chi} \lesssim 10 \mathrm{~cm}^2 / \mathrm{g}$ ; in this case, the relevant scattering cross section is the elastic scattering of the light state with itself, which is loop-suppressed. This bound is relevant only at low masses and reads  $\alpha_D \lesssim 0.06 \left( \mathrm{MeV} / m_{\chi} \right)^{1/2} \left( m_{A'} / 10 \mathrm{MeV} \right)^2$  [146, 162].

In the fermionic case, important constraints can be derived from CMB distortion due to energy injection (dark yellow) [158, 159]. In fact, residual co-annihilations into SM states can reionize hydrogen and distort the high- $\ell$  CMB power spectrum. Planck observations limit the cross section for annihilation to electromagnetic final state to be  $f^{*}\sigma v \lesssim \mathrm{pb} \times \left(m_{\chi} / 60\mathrm{GeV}\right)$ , which gives a bound on  $\bar{\sigma}_{e}$  as

$$
\bar {\sigma} _ {e} \lesssim \frac {\mathrm {p b}}{f ^ {*}} \Big (\frac {\mu_ {\chi e}}{m _ {\chi}} \Big) ^ {2} \Big (\frac {m _ {\chi}}{6 0 \mathrm {G e V}} \Big). \tag {6.43}
$$

For the scalar case instead, the CMB bounds are weakened, because the co-annihilation to leptonic final states is p-wave suppressed.

Last, we include direct detection bounds on DM inelastic scattering off nuclei. The most relevant searches here are from CRESST-III, which obtained a very low energy threshold of  $19.7\mathrm{eV}$  in [163] and  $30.1\mathrm{eV}$  in [155, 156]. Since the exposure is on the order of gram-hours in [163] and of order  $\mathrm{kg}$ -days in [155, 156], we calculate only the bound from [155, 156]. To derive this bound, we reproduce Yellin's optimum interval method [164], which is the method used by the CRESST collaboration for their own bounds. More details about the recasting of low-threshold nuclear recoil bounds for different DM models will be given elsewhere [165].

# 7 Accelerated dark matter

A fraction of DM could be accelerated to high velocities, producing an energetic DM flux that impinges on the Earth [31-33, 42, 43, 166]. Such an accelerated component may then be detected with experiments such as XENON1T, allowing for sensitivity to very light DM, which otherwise cannot be probed without sub-keV threshold experiments. Specifically, two distinct mechanisms have been suggested. In the first, DM interacts with the solar interior to produce a significantly harder spectrum [42, 43]. However, for standard DM with  $F_{\mathrm{DM}} = 1$ , the resulting flux ends at around  $2\mathrm{keV}$ , thereby naively disfavoring a simple fit to the XENON1T data. A second energetic DM flux is generated through interactions with cosmic rays (CRs) [31-33]. This was used to derive world-leading limits on DM-electron couplings for DM in the eV to few keV mass range using the Super-K experiment [167].

Naively, DM acceleration from CRs cannot address the XENON1T anomaly either, for the following reason. For the previously studied DM-electron interactions with trivial form factor  $(F_{\mathrm{DM}} = 1)$ , the predicted accelerated DM spectrum does not vary by more than an order of magnitude between keV and  $100\mathrm{MeV}$ . However, the Super-K analysis uses 176 kt-years of data (with a  $\sim 100\mathrm{MeV}$  threshold), about five orders of magnitude larger than the 0.65 tonne-year exposure available in XENON1T. Consequently, any signal at XENON1T would be naively excluded by Super-K.

The above argument does not hold for a DM interacting with electrons via a light mediator. Indeed, in such a case, both the produced flux and scattering rate predict a steeply falling spectrum towards higher energies, thereby easily compensating for the relative low exposure of XENON1T with its significantly lower threshold. However, experiments with lower thresholds may then be more constraining. We now study this possibility in detail.

We consider DM that interacts solely with electrons via a light mediator. In order to fit the XENON1T anomaly, the mediator mass must be i) lighter than a few MeV or else the benefit of having a low-threshold experiment in comparison to the Super-K experiment is lost ii) heavier than roughly  $1\mathrm{keV}$  in order to not overshoot the XENON1T energy bins (see figure 4 left) and evade the constraints from the S2-only analysis of XENON1T [44]. In this mass range, and for the range of electron couplings we consider, the mediator coupling to the SM model ends up being excluded by complementary searches for the light mediator (see e.g. [168] for a summary). We expect this feature to be quite generic in all the models of DM accelerated by cosmic rays. A complementary study to this scenario with significantly lighter mediator masses is upcoming [35].

The DM flux obtained from interactions with CRs is given by,

$$
\frac {d \Phi_ {\chi}}{d \mathcal {E} _ {\chi}} = \int d \mathcal {E} _ {e} \frac {d \Phi_ {\chi}}{d \mathcal {E} _ {e}} \frac {1}{\mathcal {E} _ {\chi} ^ {\max} (\mathcal {E} _ {e})} \Theta \left[ \mathcal {E} _ {\chi} ^ {\max} (\mathcal {E} _ {e}) - \mathcal {E} _ {\chi} \right], \tag {7.1}
$$

where  $\mathcal{E}_{\chi}$  and  $\mathcal{E}_{\mathrm{e}}$  are the DM's and CR-electrons' kinetic energy,

$$
\mathcal {E} _ {\chi} ^ {\max } = \frac {2 m _ {\chi} (\mathcal {E} _ {e} ^ {2} + 2 m _ {e} \mathcal {E} _ {e})}{(m _ {e} + m _ {\chi}) ^ {2} + 2 m _ {\chi} \mathcal {E} _ {e}}, \tag {7.2}
$$

and

$$
\frac {d \Phi_ {\chi}}{d \mathcal {E} _ {e}} = \int \frac {d \Omega}{4 \pi} \int_ {l. o. s.} d l \bar {\sigma} _ {\chi e} | F _ {\mathrm {D M}} (q) | ^ {2} \frac {\rho_ {\chi}}{m _ {\chi}} \frac {d \Phi_ {e}}{d \mathcal {E} _ {e}}. \tag {7.3}
$$

Here  $\sigma_{\chi e}$  is the DM-electron (momentum-dependent) cross-section,  $\rho_{\chi}$  is the DM density profile, taken to be an NFW profile [169] with a scale radius of  $r_s = 20$  kpc, a local density of  $\rho_{\odot} = 0.4\mathrm{GeV / cm^3}$ , and  $d\Phi_e / d\mathcal{E}_e$  is the CR-electron flux.

In order to derive limits from the low threshold ( $\sim 150\mathrm{eV}$ ) S2-only XENON1T analysis, one crucially needs to know the CR flux down to  $\mathcal{O}(\mathrm{keV})$  energies. However, measurements only provide the spectrum down to MeV energies [170] and therefore an extrapolation must be used. Strictly speaking, this implies that systematic uncertainties hinder the possibility of using the S2-analysis to exclude the CR-accelerated DM solution. In what follows, we thus simply assume that the CR flux drops to zero below MeV energies.

The model discussed here has three independent parameters: the DM mass,  $m_{\chi}$ , the mediator mass,  $m_{\phi}$ , and the DM-electron cross-section,  $\bar{\sigma}_{e}$ . In figure 24, we show the predicted accelerated DM flux (top) and expected electron spectra induced by the accelerated DM flux in xenon (bottom) for three different values of  $m_{\phi}$  and for two different form factors, fixing  $m_{\chi} = 1$  MeV and  $\bar{\sigma}_{e} = 10^{-40}\mathrm{cm}^{2}$ :

- The left panels of figure 24 with  $|F_{\mathrm{DM}}(q)|^2 \propto q^2 / (q^2 + m_\phi^2)^2$  corresponds to a scalar-pseudoscalar or vector-pseudovector interaction, where the spin-dependent interaction is on the DM side so that the mediator has scalar or vector coupling to the SM.

![](images/b0942131e3d238c4fb3eca2d7419339a229072c6f69deab69ea64aeaa011b0ec.jpg)

![](images/a5e2ea3b2ddc2173e32cbe18bf593ccd5d19055ab6de6eb08937eb855afb71a8.jpg)

![](images/cf14da1911a418ff65a22e7c5dd884bb8fbe18a012b4a66a5b24965ce199a3f4.jpg)  
Figure 24. Top: Accelerated dark matter flux due to interactions with cosmic ray electrons. The flux is shown for two different DM form factors:  $|F_{\mathrm{DM}}(q)|^2 \propto q^2 / (q^2 + m_\phi^2)^2$  (left) and  $|F_{\mathrm{DM}}(q)|^2 \propto 1 / (q^2 + m_\phi^2)^2$  (right). The three different solid colored lines show the flux for varying values of the mediator mass,  $m_\phi = 1$  eV (blue),  $m_\phi = 100$  keV (orange), and  $m_\phi = 100$  GeV (green). In these plots the DM mass is set to 1 MeV and the DM-electron cross-section is taken to be  $\bar{\sigma}_e = 10^{-30}$  cm $^2$ . The black dashed lines indicate the energy thresholds for the Super-K and XENON1T experiments. Bottom: Electron recoil spectra from cosmic ray accelerated DM flux for  $|F_{\mathrm{DM}}(q)|^2 \propto q^2 / (q^2 + m_\phi^2)^2$  (left) and  $|F_{\mathrm{DM}}(q)|^2 \propto 1 / (q^2 + m_\phi^2)^2$  (right). Three different values of the mediator mass,  $m_\phi = 1$  eV (blue),  $m_\phi = 100$  keV (orange), and  $m_\phi = 100$  GeV (green) are shown. The DM mass is fixed as  $m_\chi = 1$  MeV, and the DM-electron cross section is taken to be  $10^{-30}$  cm $^2$ . As discussed in the text, only the  $|F_{\mathrm{DM}}(q)|^2 \propto q^2 / (q^2 + m_\phi^2)^2$  with an intermediate mediator mass can viably address the XENON1T data.

![](images/80dd218f5661a49d4689f40250062bff538195385c0bee7bd6e493e310c41735.jpg)

![](images/41dca7a0e38edd804c852d18ea087f53424bca9277ac2209ad7c32aa73623b26.jpg)  
Figure 25. Left: The  $1\sigma$  and  $2\sigma$  best-fit regions (red) for cosmic-ray accelerated DM that interacts with electrons via a form factor  $|F_{\mathrm{DM}}(q)|^2 \propto q^2 / (q^2 + m_\phi^2)^2$ . Exclusion regions due to the XENON1T S2-only analysis are shown by the light green-shaded region, while the limits from the Super-K data [33] are shown in darker shaded green. Various complementary constraints strongly bound the light-mediator coupling to electrons. To illustrate this, in the middle plot we show the best fit region for the mediator-electron coupling  $y_e$  as a function of the mediator mass,  $m_\phi$ . The blue region is excluded by HB cooling [108], while in the orange region the mediator thermalizes before electron decoupling, and may therefore suffer from (model-dependent) limits on  $N_{\mathrm{eff}}$ . The magenta shaded regions is excluded by the  $(g - 2)$  measurement of the electron [171, 172], and the region at higher  $y_e$  is excluded by collider constraints from monophoton searches [61, 173]. Right: The signal spectral shape for the best fit point for this model. The black dots are the XENON1T data, the gray shaded region is the expected background, the blue solid line is the signal shape after detector smearing, and the blue dotted line is the signal before smearing. The blue shaded region is the resulting signal plus background distribution.

![](images/1675b264e043ddf2ac12e9997ee1965de48d1843f7a6679175c05a618a66cf64.jpg)

![](images/40a9bb740cd520dd9d91f7486410b093e8bd64229b884b1a670a2579df889383.jpg)

As expected, for lighter mediator masses, the DM flux peaks at lower energies. From the bottom left panel of figure 24, we see that when choosing appropriate mediator masses, we can get a decreasing spectrum at lower energies below the mediator mass for  $|F_{\mathrm{DM}}(q)|^2 \propto q^2 / m_\phi^4$ , and at higher energies compared to the mediator mass, where the suppression  $|F_{\mathrm{DM}}(q)|^2 \propto 1 / q^2$  enhances the suppression from the atomic form factor.

- The right panel of figure 24 with  $|F_{\mathrm{DM}}(q)|^2 \propto 1 / (q^2 + m_\phi^2)^2$  corresponds to a scalar-scalar or vector-vector interaction, which can be obtained by the exchange of a leptophilic scalar or a dark photon mixing with the SM photon. Here the predicted spectrum does not flatten out at low energies, and thus we find it to be excluded by the XENON1T S2-only analysis [44].

We perform a wide scan of the accelerated DM parameter space for different DM masses and mediator masses. The best fit point we find is

$$
m _ {\chi} = 0. 4 \mathrm {M e V}, m _ {\phi} / m _ {\chi} = 4, \overline {{\sigma}} _ {e} = 6. 6 \times 1 0 ^ {- 3 2} \mathrm {c m} ^ {2}, 2 \log (\mathcal {L} _ {S + B} / \mathcal {L} _ {B}) = 1 2. 1, (7. 4)
$$

and in figure 25 (right) we show its expected signal. The dashed and solid blue lines show the unsmeared and detector-smeared spectra. The gray region is the expected binned

background, while the blue shaded regions show the contribution of the binned signal. For simplicity, we fix  $m_{\phi} = m_{\chi} / 4$ , and we explore the parameter space as a function of the DM mass. Our conclusions do not depend much on this choice. In figure 25 (left), we show the corresponding  $1\sigma$  and  $2\sigma$  best-fit regions in red and the best fit point in eq. (7.4) as a red star. In agreement with the previous discussion, we see how in this setup the best-fit region lies close to the boundary of the region excluded by the XENON1T S2-only analysis [44], and the Super-K experiment [33] gives an upper bound on the DM mass (which is related to the mediator mass).

Since the mediator mass must be small enough for the spectrum to be suppressed at high energies, the relevant parameter space is subject to severe constraints that we illustrate in the middle of figure 25. We plot the mediator coupling to electrons,  $y_{e}$ , as a function of the mediator mass, fixing  $y_{D}$  to the maximal value allowed by unitarity. We include stellar cooling constraints from HB stars [108], the electron  $g - 2$  [171, 172] constraints, and a line that shows the coupling required for the mediator  $\phi$  to thermalize before electron decoupling. This region is likely to be subject to (model-dependent) BBN constraints [174]. At higher mediator masses, the required coupling to electrons is so high to be robustly excluded by direct production of the light mediator at colliders through  $e^{+}e^{-}\rightarrow \gamma \phi$  [61, 173]. In summary, it seems that this explanation of the XENON1T excess is robustly excluded.

Before closing, a remark is in order. In deriving the limits above, we used nonrelativistic form factors for the DM-electron interactions. Corrections that arise in the relativistic limit can be found in [130]. To understand why it is justified to neglect relativistic corrections, we note that a DM with mass around  $1\mathrm{MeV}$  must be accelerated to velocities above  $\sim 0.03c$ . Using eq. (6.11) and since  $E_{e}\simeq \mathrm{keV}$ , one finds  $q\gtrsim 30\mathrm{keV}$ . Since the atomic and DM form factors both dominate at low  $q$ , this justifies neglecting the relativistic corrections, which become important only at significantly higher values of  $q$ .

# Acknowledgments

We thank T. Bringmann, R. Budnik, H. Kim, H. Liu, P. Meade, G. Perez, J. Pradler, G. Rossi, F. Sala, Y. Soreq, L. Ubaldi, and N. Weiner for useful discussions. We also thank G. Alonso-Alvarez, L. Calibbi, F. Ertas, J. Huang, J. Jaeckel, F. Kahlhoefer, G. Marquez-Tavares, P. Panci, E. Salvioni, M. Szydagis, L.J. Thormaehlen, K. Van Tilburg for many useful feedbacks on the draft. IB is grateful for the support of the Alexander Zaks Scholarship, The Buchmann Scholarship, and the Azrieli Foundation. AC acknowledges support from the "Generalitat Valenciana" (Spain) through the "plan GenT" program (CIDEGENT/2018/019), as well as national grants FPA2014-57816-P, FPA2017- 85985-P. RE and MS are supported in part by DoE Grant DE-SC0017938 and Simons Investigator in Physics Award 623940. TV is supported by the Israel Science Foundation-NSFC (grant No. 2522/17), by the Binational Science Foundation (grant No. 2016153) and by the European Research Council (ERC) under the EU Horizon 2020 Programme (ERC-CoG-2015 - Proposal n. 682676 LDMThExp).

Note added. While this work was in progress, [115, 145, 175-194] appeared. A number of these papers have partial overlap with the study presented here. Another model that could explain the excess is [195].

Open Access. This article is distributed under the terms of the Creative Commons Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in any medium, provided the original author(s) and source are credited.

# References

[1] XENON collaboration, Excess electronic recoil events in XENON1T, Phys. Rev. D 102 (2020) 072004 [arXiv:2006.09721] [INSPIRE].  
[2] S. Dimopoulos, G.D. Starkman and B.W. Lynn, Atomic Enhancements in the Detection of Weakly Interacting Particles, Phys. Lett. B 168 (1986) 145 [INSPIRE].  
[3] F.T. Avignone et al., Laboratory Limits on Solar Axions From an Ultralow Background Germanium Spectrometer, Phys. Rev. D 35 (1987) 2752 [INSPIRE].  
[4] M. Pospelov, A. Ritz and M.B. Voloshin, Bosonic super-WIMPs as keV-scale dark matter, Phys. Rev. D 78 (2008) 115012 [arXiv:0807.3279] [INSPIRE].  
[5] A. Derevianko, V.A. Dzuba, V.V. Flambaum and M. Pospelov, *Axio-electric effect*, Phys. Rev. D 82 (2010) 065006 [arXiv:1007.1833] [INSPIRE].  
[6] K. Arisaka et al., Expected Sensitivity to Galactic/Solar Axions and Bosonic Super-WIMPs based on the Axio-electric Effect in Liquid Xenon Dark Matter Detectors, Astropart. Phys. 44 (2013) 59 [arXiv:1209.3810] [INSPIRE].  
[7] H. An, M. Pospelov and J. Pradler, Dark Matter Detectors as Dark Photon Helioscopes, Phys. Rev. Lett. 111 (2013) 041302 [arXiv:1304.3461] [INSPIRE].  
[8] I.M. Bloch, R. Essig, K. Tobioka, T. Volansky and T.-T. Yu, Searching for Dark Absorption with Direct Detection Experiments, JHEP 06 (2017) 087 [arXiv:1608.02123] [INSPIRE].  
[9] Y. Hochberg, T. Lin and K.M. Zurek, Absorption of light dark matter in semiconductors, Phys. Rev. D 95 (2017) 023013 [arXiv:1608.01994] [INSPIRE].  
[10] G.G. Raffelt, *Stars as laboratories for fundamental physics*, Chicago University Press, U.S.A. (1996), http://wwwth.mpp.mpg.de/members/raffelt/mypapers/199613.pdf.  
[11] J. Redondo, Helioscope Bounds on Hidden Sector Photons, JCAP 07 (2008) 008 [arXiv:0801.1527] [INSPIRE].  
[12] H. An, M. Pospelov, J. Pradler and A. Ritz, Direct Detection Constraints on Dark Photon Dark Matter, Phys. Lett. B 747 (2015) 331 [arXiv:1412.8378] [INSPIRE].  
[13] J. Redondo and G. Raffelt, Solar constraints on hidden photons re-visited, JCAP 08 (2013) 034 [arXiv:1305.2920] [INSPIRE].  
[14] R. Budnik, O. Davidi, H. Kim, G. Perez and N. Priel, Searching for a solar relaxation scalar particle with XENON1T and LUX, Phys. Rev. D 100 (2019) 095021 [arXiv:1909.02568] [INSPIRE].  
[15] R. Essig, J. Mardon and T. Volansky, Direct Detection of Sub-GeV Dark Matter, Phys. Rev. D 85 (2012) 076007 [arXiv:1108.5383] [INSPIRE].

[16] R. Essig, A. Manalaysay, J. Mardon, P. Sorensen and T. Volansky, First Direct Detection Limits on sub-GeV Dark Matter from XENON10, Phys. Rev. Lett. 109 (2012) 021301 [arXiv:1206.2644] [INSPIRE].  
[17] R. Essig, M. Fernandez-Serra, J. Mardon, A. Soto, T. Volansky and T.-T. Yu, Direct Detection of sub-GeV Dark Matter with Semiconductor Targets, JHEP 05 (2016) 046 [arXiv:1509.01598] [INSPIRE].  
[18] R. Essig, T. Volansky and T.-T. Yu, New Constraints and Prospects for sub-GeV Dark Matter Scattering off Electrons in Xenon, Phys. Rev. D 96 (2017) 043017 [arXiv:1703.00910] [INSPIRE].  
[19] J. Kopp, V. Niro, T. Schwetz and J. Zupan, DAMA/LIBRA and leptonically interacting Dark Matter, Phys. Rev. D 80 (2009) 083502 [arXiv:0907.3159] [INSPIRE].  
[20] J. Khoury and A. Weltman, Chameleon fields:Awaiting surprises for tests of gravity in space, Phys. Rev. Lett. 93 (2004) 171104 [astro-ph/0309300] [INSPIRE].  
[21] E. Masso and J. Redondo, Evading astrophysical constraints on axion-like particles, JCAP 09 (2005) 015 [hep-ph/0504202] [INSPIRE].  
[22] E. Masso and J. Redondo, Compatibility of CAST search with axion-like interpretation of PVLAS results, Phys. Rev. Lett. 97 (2006) 151802 [hep-ph/0606163] [INSPIRE].  
[23] J. Jaeckel, E. Masso, J. Redondo, A. Ringwald and F. Takahashi, The need for purely laboratory-based axion-like particle searches, Phys. Rev. D 75 (2007) 013004 [hep-ph/0610203] [INSPIRE].  
[24] A.K. Ganguly, P. Jain, S. Mandal and S. Stokes, Self Interacting Dark Matter in the Solar System, Phys. Rev. D 76 (2007) 025026 [hep-ph/0611006] [INSPIRE].  
[25] J.E. Kim, PVLAS experiment, star cooling and BBN constraints: Possible interpretation with temperature dependent gauge symmetry breaking, Phys. Rev. D 76 (2007) 051701 [arXiv:0704.3310] [INSPIRE].  
[26] P. Brax, C. van de Bruck and A.-C. Davis, Compatibility of the chameleon-field model with fifth-force experiments, cosmology, and PVLAS and CAST results, Phys. Rev. Lett. 99 (2007) 121103 [hep-ph/0703243] [INSPIRE].  
[27] J. Redondo, Can the PVLAS particle be compatible with the astrophysical bounds?, Ph.D. Thesis, Barcelona, Autonoma U., (2007) [arXiv:0807.4329] [INSPIRE].  
[28] R. Essig, J. Kaplan, P. Schuster and N. Toro, On the Origin of Light Dark Matter Species, arXiv:1004.0691 [INSPIRE].  
[29] P.W. Graham, R. Harnik, S. Rajendran and P. Saraswat, Exothermic Dark Matter, Phys. Rev. D 82 (2010) 063512 [arXiv:1004.0937] [INSPIRE].  
[30] N. Bernal, X. Chu and J. Pradler, Simply split strongly interacting massive particles, Phys. Rev. D 95 (2017) 115023 [arXiv:1702.04906] [INSPIRE].  
[31] T. Bringmann and M. Pospelov, Novel direct detection constraints on light dark matter, Phys. Rev. Lett. 122 (2019) 171801 [arXiv:1810.10543] [INSPIRE].  
[32] Y. Ema, F. Sala and R. Sato, Light Dark Matter at Neutrino Experiments, Phys. Rev. Lett. 122 (2019) 181802 [arXiv:1811.00520] [INSPIRE].  
[33] C. Cappiello and J.F. Beacom, *Strong New Limits on Light Dark Matter from Neutrino Experiments*, Phys. Rev. D 100 (2019) 103011 [arXiv:1906.11283] [INSPIRE].

[34] K. Bondarenko, A. Boyarsky, T. Bringmann, M. Hufnagel, K. Schmidt-Hoberg and A. Sokolenko, Direct detection and complementary constraints for sub-GeV dark matter, JHEP 03 (2020) 118 [arXiv:1909.08632] [INSPIRE].  
[35] T. Bringmann, R. Budnik, T. Emken and R. Essig, in progress.  
[36] DARKSIDE collaboration, Constraints on Sub-GeV Dark-Matter-Electron Scattering from the DarkSide-50 Experiment, Phys. Rev. Lett. 121 (2018) 111303 [arXiv:1802.06998] [INSPIRE].  
[37] SENSEI collaboration, Single-electron and single-photon sensitivity with a silicon Skipper CCD, Phys. Rev. Lett. 119 (2017) 131802 [arXiv:1706.00028] [INSPIRE].  
[38] SENSEI collaboration, SENSEI: Direct-Detection Constraints on Sub-GeV Dark Matter from a Shallow Underground Run Using a Prototype Skipper-CCD, Phys. Rev. Lett. 122 (2019) 161801 [arXiv:1901.10478] [INSPIRE].  
[39] SENSEI collaboration, SENSEI: First Direct-Detection Constraints on sub-GeV Dark Matter from a Surface Run, Phys. Rev. Lett. 121 (2018) 061803 [arXiv:1804.00088] [INSPIRE].  
[40] R.K. Romani et al., Thermal detection of single  $e-h$  pairs in a biased silicon crystal detector, Appl. Phys. Lett. 112 (2018) 043501 [arXiv:1710.09335] [INSPIRE].  
[41] SUPERCDMS collaboration, First Dark Matter Constraints from a SuperCDMS Single-Charge Sensitive Detector, Phys. Rev. Lett. 121 (2018) 051301 [Erratum ibid. 122 (2019) 069901] [arXiv:1804.10697] [INSPIRE].  
[42] H. An, M. Pospelov, J. Pradler and A. Ritz, Directly Detecting MeV-scale Dark Matter via Solar Reflection, Phys. Rev. Lett. 120 (2018) 141801 [Erratum ibid. 121 (2018) 259903] [arXiv:1708.03642] [INSPIRE].  
[43] T. Emken, C. Kouvaris and N.G. Nielsen, The Sun as a sub-GeV Dark Matter Accelerator, Phys. Rev. D 97 (2018) 063007 [arXiv:1709.06573] [INSPIRE].  
[44] XENON collaboration, Light Dark Matter Search with Ionization Signals in XENON1T, Phys. Rev. Lett. 123 (2019) 251801 [arXiv:1907.11485] [INSPIRE].  
[45] SENSEI collaboration, SENSEI: Direct-Detection Results on sub-GeV Dark Matter from a New Skipper-CCD, Phys. Rev. Lett. 125 (2020) 171802 [arXiv:2004.11378] [INSPIRE].  
[46] SUPERCDMS collaboration, Constraints on low-mass, relic dark matter candidates from a surface-operated SuperCDMS single-charge sensitive detector, Phys. Rev. D 102 (2020) 091101 [arXiv:2005.14067] [INSPIRE].  
[47] R. Essig, J. Pradler, M. Sholapurkar and T.-T. Yu, Relation between the Migdal Effect and Dark Matter-Electron Scattering in Isolated Atoms and Semiconductors, Phys. Rev. Lett. 124 (2020) 021801 [arXiv:1908.10881] [INSPIRE].  
[48] M. Battaglieri et al., US Cosmic Visions: New Ideas in Dark Matter 2017: Community Report, in U.S. Cosmic Visions: New Ideas in Dark Matter, (2017) [arXiv:1707.04591] [INSPIRE].  
[49] P. Gondolo and G.G. Raffelt, Solar neutrino limit on axions and keV-mass bosons, Phys. Rev. D 79 (2009) 107301 [arXiv:0807.2926] [INSPIRE].  
[50] J. Redondo, Solar axion flux from the axion-electron coupling, JCAP 12 (2013) 008 [arXiv:1310.0823] [INSPIRE].

[51] G.G. Raffelt, Axion Constraints From White Dwarf Cooling Times, Phys. Lett. B 166 (1986) 402 [INSPIRE].  
[52] M.M. Miller Bertolami, B.E. Melendez, L.G. Althaus and J. Isern, Revisiting the axion bounds from the Galactic white dwarf luminosity function, JCAP 10 (2014) 069 [arXiv:1406.7712] [INSPIRE].  
[53] M. Giannotti, I.G. Irastorza, J. Redondo, A. Ringwald and K. Saikawa, Stellar Recipes for Axion Hunters, JCAP 10 (2017) 010 [arXiv:1708.02111] [INSPIRE].  
[54] A.H. Córsico, L.G. Althaus, M.M. Miller Bertolami and S.O. Kepler, Pulsating white dwarfs: new insights, *Astron. Astrophys. Rev.* 27 (2019) 7 [arXiv:1907.00115] [INSPIRE].  
[55] G. Raffelt and A. Weiss, Red giant bound on the axion-electron coupling revisited, Phys. Rev. D 51 (1995) 1495 [hep-ph/9410205] [INSPIRE].  
[56] N. Viaux et al., Neutrino and axion bounds from the globular cluster M5 (NGC 5904), Phys. Rev. Lett. 111 (2013) 231301 [arXiv:1311.1669] [INSPIRE].  
[57] O. Straniero, I. Dominguez, M. Giannotti and A. Mirizzi, Axion-electron coupling from the RGB tip of Globular Clusters, in 13th Patras Workshop on Axions, WIMPs and WISPs, pp. 172-176, 2018, DOI [arXiv:1802.10357] [INSPIRE].  
[58] G.G. Raffelt, Astrophysical axion bounds diminished by screening effects, Phys. Rev. D 33 (1986) 897 [INSPIRE].  
[59] L. Calibbi, D. Redigolo, R. Ziegler and J. Zupan, Looking forward to Lepton-flavor-violating ALPs, arXiv:2006.04795 [INSPIRE].  
[60] P.J. Fox, R. Harnik, J. Kopp and Y. Tsai, LEP Shines Light on Dark Matter, Phys. Rev. D 84 (2011) 014028 [arXiv:1103.0240] [INSPIRE].  
[61] R. Essig, J. Mardon, M. Papucci, T. Volansky and Y.-M. Zhong, Constraining Light Dark Matter with Low-Energy  $e^{+}e^{-}$  Colliders, JHEP 11 (2013) 167 [arXiv:1309.5084] [INSPIRE].  
[62] B.A. Dolgoshein, V.N. Lebedenko and B.U. Rodionov, New Method of Registration of Ionizing-particle Tracks in Condensed Matter, JETP Lett. 11 (1970) 351.  
[63] G.J. Alner et al., First limits on WIMP nuclear recoil signals in ZEPLIN-II: A two phase xenon detector for dark matter detection, Astrophys. 28 (2007) 287 [astro-ph/0701858] [INSPIRE].  
[64] XENON collaboration, First Dark Matter Search Results from the XENON1T Experiment, Phys. Rev. Lett. 119 (2017) 181301 [arXiv:1705.06655] [INSPIRE].  
[65] XENON collaboration, The XENON1T Dark Matter Experiment, Eur. Phys. J. C 77 (2017) 881 [arXiv:1708.07051] [INSPIRE].  
[66] XENON collaboration, Dark Matter Search Results from a One Ton-Year Exposure of XENON1T, Phys. Rev. Lett. 121 (2018) 111302 [arXiv:1805.12562] [INSPIRE].  
[67] XENON collaboration, First results on the scalar WIMP-pion coupling, using the XENON1T experiment, Phys. Rev. Lett. 122 (2019) 071301 [arXiv:1811.12482] [INSPIRE].  
[68] XENON collaboration, Constraining the spin-dependent WIMP-nucleon cross sections with XENON1T, Phys. Rev. Lett. 122 (2019) 141301 [arXiv:1902.03234] [INSPIRE].

[69] XENON collaboration, XENON1T dark matter data analysis: Signal and background models and statistical inference, Phys. Rev. D 99 (2019) 112009 [arXiv:1902.11297] [INSPIRE].  
[70] XENON collaboration, Search for Light Dark Matter Interactions Enhanced by the Migdal Effect or Bremsstrahlung in XENON1T, Phys. Rev. Lett. 123 (2019) 241803 [arXiv:1907.12771] [INSPIRE].  
[71] XENON collaboration, Energy resolution and linearity of XENON1T in the MeV energy range, Eur. Phys. J. C 80 (2020) 785 [arXiv:2003.03825] [INSPIRE].  
[72] M. Szydagis et al., NEST: A Comprehensive Model for Scintillation Yield in Liquid Xenon, 2011 JINST 6 P10002 [arXiv:1106.1613] [INSPIRE].  
[73] XENON1T collaboration, Search for Axions and Axion-Like Particles with XENON1T, XENON Technical Meeting, May 12-14, 2020, https://indico.cern.ch/event/923834/contributions/3913983/attachments/2064918/3465213/zoomaxion_2606_Galloway.pdf.  
[74] XENON collaboration, XENON1T Dark Matter Data Analysis: Signal Reconstruction, Calibration and Event Selection, Phys. Rev. D 100 (2019) 052014 [arXiv:1906.04717] [INSPIRE].  
[75] M. Szydagis, C. Levy, G.M. Blockinger, A. Kamaha, N. Parveen and G.R.C. Rischbieter, Investigating the XENON1T low-energy electronic recoil excess using NEST, Phys. Rev. D 103 (2021) 012002 [arXiv:2007.00528] [INSPIRE].  
[76] G. Cowan, K. Cranmer, E. Gross and O. Vitells, Asymptotic formulae for likelihood-based tests of new physics, Eur. Phys. J. C 71 (2011) 1554 [Erratum ibid. 73 (2013) 2501] [arXiv:1007.1727] [INSPIRE].  
[77] A.E. Robinson, XENON1T observes tritium, arXiv:2006.13278 [INSPIRE].  
[78] O. Vitells and E. Gross, Estimating the significance of a signal in a multi-dimensional search, *Astropart. Phys.* **35** (2011) 230 [arXiv:1105.4355] [INSPIRE].  
[79] S. Dimopoulos, J.A. Frieman, B.W. Lynn and G.D. Starkman, Axiorecombination: A New Mechanism for Stellar Axion Production, Phys. Lett. B 179 (1986) 223 [INSPIRE].  
[80] B.L. Henke, E.M. Gullikson and J.C. Davis, X-Ray Interactions: Photoabsorption, Scattering, Transmission, and Reflection at  $E = 50 - 30,000\mathrm{eV}$ ,  $Z = 1 - 92$ , Atom. Data Nucl. Data Tabl. 54 (1993) 181.  
[81] K. Nakayama, F. Takahashi and T.T. Yanagida, Anomaly-free flavor models for Nambu-Goldstone bosons and the 3.5keV X-ray line signal, Phys. Lett. B 734 (2014) 178 [arXiv:1403.7390] [INSPIRE].  
[82] S. Chang and K. Choi, Hadronic axion window and the big bang nucleosynthesis, Phys. Lett. B 316 (1993) 51 [hep-ph/9306216] [INSPIRE].  
[83] G. Grilli di Cortona, E. Hardy, J. Pardo Vega and G. Villadoro, The QCD axiom, precisely, JHEP 01 (2016) 034 [arXiv:1511.02867] [INSPIRE].  
[84] A.R. Zhitnitsky, On Possible Suppression of the Axion Hadron Interactions (in Russian), Sov. J. Nucl. Phys. 31 (1980) 260 [INSPIRE].  
[85] M. Dine, W. Fischler and M. Srednicki, A Simple Solution to the Strong CP Problem with a Harmless Axion, Phys. Lett. B 104 (1981) 199 [INSPIRE].

[86] J.E. Kim, Weak Interaction Singlet and Strong CP Invariance, Phys. Rev. Lett. 43 (1979) 103 [INSPIRE].  
[87] M.A. Shifman, A.I. Vainshtein and V.I. Zakharov, Can Confinement Ensure Natural CP Invariance of Strong Interactions?, Nucl. Phys. B 166 (1980) 493 [INSPIRE].  
[88] N. Craig, A. Hook and S. Kasko, The Photophobic ALP, JHEP 09 (2018) 028 [arXiv:1805.06538] [INSPIRE].  
[89] A. Ibarra, E. Molinaro and S.T. Petcov, Low Energy Signatures of the TeV Scale See-Saw Mechanism, Phys. Rev. D 84 (2011) 013005 [arXiv:1103.6217] [INSPIRE].  
[90] J. Heeck and H.H. Patel, Majoron at two loops, Phys. Rev. D 100 (2019) 095015 [arXiv:1909.02029] [INSPIRE].  
[91] PANDAX collaboration, Limits on Axion Couplings from the First 80 Days of Data of the PandaX-II Experiment, Phys. Rev. Lett. 119 (2017) 181806 [arXiv:1707.07921] [INSPIRE].  
[92] A. Boyarsky, J.W. den Herder, A. Neronov and O. Ruchayskiy, Search for the light dark matter with an X-ray spectrometer, Astrophys. 28 (2007) 303 [astro-ph/0612219] [INSPIRE].  
[93] XQC collaboration, Searching for keV Sterile Neutrino Dark Matter with X-ray Microcalorimeter Sounding Rockets, Astrophys. J. 814 (2015) 82 [arXiv:1506.05519] [INSPIRE].  
[94] R. Hill, K.W. Masui and D. Scott, The Spectrum of the Universe, Appl. Spectrosc. 72 (2018) 663 [arXiv:1802.03694] [INSPIRE].  
[95] P. Arias, D. Cadamuro, M. Goodsell, J. Jaeckel, J. Redondo and A. Ringwald, WISPy Cold Dark Matter, JCAP 06 (2012) 013 [arXiv:1201.5902] [INSPIRE].  
[96] D. Barret et al., *Athena+: The first Deep Universe X-ray Observatory*, arXiv:1310.3814 [INSPIRE].  
[97] A. Caputo, M. Regis and M. Taoso, Searching for Sterile Neutrino with X-ray Intensity Mapping, JCAP 03 (2020) 001 [arXiv:1911.09120] [INSPIRE].  
[98] C. Creque-Sarbinowski and M. Kamionkowski, Searching for Decaying and Annihilating Dark Matter with Line Intensity Mapping, Phys. Rev. D 98 (2018) 063524 [arXiv:1806.11119] [INSPIRE].  
[99] J. Preskill, M.B. Wise and F. Wilczek, Cosmology of the Invisible Axion, Phys. Lett. B 120 (1983) 127 [INSPIRE].  
[100] L.F. Abbott and P. Sikivie, A Cosmological Bound on the Invisible Axion, Phys. Lett. B 120 (1983) 133 [INSPIRE].  
[101] M. Dine and W. Fischler, The Not So Harmless Axion, Phys. Lett. B 120 (1983) 137 [INSPIRE].  
[102] A. Hook, G. Marques-Tavares and Y. Tsai, *Scalers Gliding through an Expanding Universe*, Phys. Rev. Lett. **124** (2020) 211801 [arXiv:1912.08817] [INSPIRE].  
[103] A. Arvanitaki, S. Dimopoulos, M. Galanis, L. Lehner, J.O. Thompson and K. Van Tilburg, Large-misalignment mechanism for the formation of compact axion structures: Signatures from the QCD axion to fuzzy dark matter, Phys. Rev. D 101 (2020) 083014 [arXiv:1909.11665] [INSPIRE].

[104] M. Farina, D. Pappadopulo, F. Rompineve and A. Tesi, The photo-philic QCD axion, JHEP 01 (2017) 095 [arXiv:1611.09855] [INSPIRE].  
[105] A. Ayala, I. Dominguez, M. Giannotti, A. Mirizzi and O. Straniero, Revisiting the bound on axion-photon coupling from Globular Clusters, Phys. Rev. Lett. 113 (2014) 191302 [arXiv:1406.6053] [INSPIRE].  
[106] K. Van Tilburg, Stellar Basins of Gravitationally Bound Particles, arXiv:2006.12431 [INSPIRE].  
[107] CAST collaboration, New CAST Limit on the Axion-Photon Interaction, Nature Phys. 13 (2017) 584 [arXiv:1705.02290] [INSPIRE].  
[108] E. Hardy and R. Lasenby, Stellar cooling bounds on new light particles: plasma mixing effects, JHEP 02 (2017) 033 [arXiv:1611.05852] [INSPIRE].  
[109] D. Carmi, A. Falkowski, E. Kuflik and T. Volansky, Interpreting LHC Higgs Results from Natural New Physics Perspective, JHEP 07 (2012) 136 [arXiv:1202.3144] [INSPIRE].  
[110] D. Carmi, A. Falkowski, E. Kuflik and T. Volansky, Interpreting the 125 GeV Higgs, Nuovo Cim. C 035 (2012) 315 [arXiv:1206.4201] [INSPIRE].  
[111] J.D. Clarke, R. Foot and R.R. Volkas, Phenomenology of a very light scalar (100 MeV <  $m_h < 10$  GeV) mixing with the SM Higgs, JHEP 02 (2014) 123 [arXiv:1310.8042] [INSPIRE].  
[112] Z. Chacko and R.K. Mishra, *Effective Theory of a Light Dilaton*, Phys. Rev. D **87** (2013) 115006 [arXiv:1209.3022] [INSPIRE].  
[113] B. Holdom, Two U(1)'s and Epsilon Charge Shifts, Phys. Lett. B 166 (1986) 196 [INSPIRE].  
[114] H. An, M. Pospelov and J. Pradler, New stellar constraints on dark photons, Phys. Lett. B 725 (2013) 190 [arXiv:1302.3884] [INSPIRE].  
[115] G. Alonso-Álvarez, F. Ertas, J. Jaeckel, F. Kahlhoefer and L.J. Thormaehlen, Hidden Photon Dark Matter in the Light of XENON1T and Stellar Cooling, JCAP 11 (2020) 029 [arXiv:2006.11243] [INSPIRE].  
[116] M. Giannotti, I. Irastorza, J. Redondo and A. Ringwald, Cool WISP's for stellar cooling excesses, JCAP 05 (2016) 057 [arXiv:1512.08108] [INSPIRE].  
[117] G. Alonso-Álvarez, T. Hugle and J. Jaeckel, Misalignment & Co.: (Pseudo-)scalar and vector dark matter with curvature couplings, JCAP 02 (2020) 014 [arXiv:1905.09836] [INSPIRE].  
[118] P.W. Graham, J. Mardon and S. Rajendran, Vector Dark Matter from Inflationary Fluctuations, Phys. Rev. D 93 (2016) 103520 [arXiv:1504.02102] [INSPIRE].  
[119] M. Bastero-Gil, J. Santiago, L. Ubaldi and R. Vega-Morales, Vector dark matter production at the end of inflation, JCAP 04 (2019) 015 [arXiv:1810.07208] [INSPIRE].  
[120] P. Agrawal, N. Kitajima, M. Reece, T. Sekiguchi and F. Takahashi, *Relic Abundance of Dark Photon Dark Matter*, Phys. Lett. B 801 (2020) 135136 [arXiv:1810.07188] [INSPIRE].  
[121] R.T. Co, A. Pierce, Z. Zhang and Y. Zhao, Dark Photon Dark Matter Produced by Axion Oscillations, Phys. Rev. D 99 (2019) 075002 [arXiv:1810.07196] [INSPIRE].  
[122] J.A. Dror, K. Harigaya and V. Narayan, Parametric Resonance Production of Ultralight Vector Dark Matter, Phys. Rev. D 99 (2019) 035036 [arXiv:1810.07195] [INSPIRE].

[123] J. Khoury, Chameleon Field Theories, Class. Quant. Grav. 30 (2013) 214004 [arXiv:1306.4326] [INSPIRE].  
[124] R.D. Peccei and H.R. Quinn, CP Conservation in the Presence of Instantons, Phys. Rev. Lett. 38 (1977) 1440 [INSPIRE].  
[125] C.D. Froggatt and H.B. Nielsen, *Hierarchy of Quark Masses*, Cabibbo Angles and CP-violation, Nucl. Phys. B 147 (1979) 277 [INSPIRE].  
[126] M. Leurer, Y. Nir and N. Seiberg, Mass matrix models, Nucl. Phys. B 398 (1993) 319 [hep-ph/9212278] [INSPIRE].  
[127] L. Calibbi, Z. Lalak, S. Pokorski and R. Ziegler, The Messenger Sector of SUSY Flavour Models and Radiative Breaking of Flavour Universality, JHEP 06 (2012) 018 [arXiv:1203.1489] [INSPIRE].  
[128] K. Hinterbichler and J. Khoury, Symmetron Fields: Screening Long-Range Forces Through Local Symmetry Restoration, Phys. Rev. Lett. 104 (2010) 231301 [arXiv:1001.4525] [INSPIRE].  
[129] C. Bunge, J. Barrientos and A. Bunge, Roothaan-Hartree-Fock Ground-State Atomic Wave Functions: Slater-Type Orbital Expansions and Expectation Values for  $Z = 2-54$ , Atom. Data Nucl. Data Tabl. 53 (1993) 113.  
[130] B.M. Roberts, V.A. Dzuba, V.V. Flambaum, M. Pospelov and Y.V. Stadnik, Dark matter scattering on electrons: Accurate calculations of atomic excitations and implications for the DAMA signal, Phys. Rev. D 93 (2016) 115037 [arXiv:1604.04559] [INSPIRE].  
[131] E. Clementi and D.L. Raimondi, Atomic Screening Constants from SCF Functions, J. Chem. Phys. 38 (1963) 2686.  
[132] E. Clementi, D.L. Raimondi and W.P. Reinhardt, Atomic Screening Constants from SCF Functions. II. Atoms with 37 to 86 Electrons, J. Chem. Phys. 47 (1967) 1300.  
[133] R. Balkin, M. Ruhdorfer, E. Salvioni and A. Weiler, Dark matter shifts away from direct detection, JCAP 11 (2018) 050 [arXiv:1809.09106] [INSPIRE].  
[134] D. Tucker-Smith and N. Weiner, Inelastic dark matter, Phys. Rev. D 64 (2001) 043502 [hep-ph/0101138] [INSPIRE].  
[135] D.P. Finkbeiner and N. Weiner, Exciting Dark Matter and the INTEGRAL/SPI 511 keV signal, Phys. Rev. D 76 (2007) 083519 [astro-ph/0702587] [INSPIRE].  
[136] N. Arkani-Hamed, D.P. Finkbeiner, T.R. Slatyer and N. Weiner, A Theory of Dark Matter, Phys. Rev. D 79 (2009) 015014 [arXiv:0810.0713] [INSPIRE].  
[137] D.P. Finkbeiner, T.R. Slatyer, N. Weiner and I. Yavin, PAMELA, DAMA, INTEGRAL and Signatures of Metastable Excited WIMPs, JCAP 09 (2009) 037 [arXiv:0903.1037] [INSPIRE].  
[138] B. Batell, M. Pospelov and A. Ritz, Direct Detection of Multi-component Secluded WIMPs, Phys. Rev. D 79 (2009) 115019 [arXiv:0903.3396] [INSPIRE].  
[139] R.F. Lang and N. Weiner, Peaked Signals from Dark Matter Velocity Structures in Direct Detection Experiments, JCAP 06 (2010) 032 [arXiv:1003.3664] [INSPIRE].  
[140] T. Emken, R. Essig, C. Kouvaris and M. Sholapurkar, Direct Detection of Strongly Interacting Sub-GeV Dark Matter via Electron Recoils, JCAP 09 (2019) 070 [arXiv:1905.06348] [INSPIRE].

[141] T. Emken, Dark Matter in the Earth and the Sun — Simulating Underground Scatterings for the Direct Detection of Low-Mass Dark Matter, Ph.D. thesis, Southern Denmark University, CP3-Origins, (2019), arXiv:1906.07541 [INSPIRE].  
[142] Y.-S. Tsai, *Pair Production and Bremsstrahlung of Charged Leptons*, Rev. Mod. Phys. **46** (1974) 815 [Erratum ibid. **49** (1977) 421] [INSPIRE].  
[143] M. Baryakhtar, A. Berlin, H. Liu and N. Weiner, Electromagnetic Signals of Inelastic Dark Matter Scattering, arXiv:2006.13918 [INSPIRE].  
[144] J. Bramante and N. Song, Electric But Not Eclectic: Thermal Relic Dark Matter for the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 161805 [arXiv:2006.14089] [INSPIRE].  
[145] K. Harigaya, Y. Nakai and M. Suzuki, Inelastic Dark Matter Electron Scattering and the XENON1T Excess, Phys. Lett. B 809 (2020) 135729 [arXiv:2006.11938] [INSPIRE].  
[146] E. Izaguirre, G. Krnjaic, P. Schuster and N. Toro, Analyzing the Discovery Potential for Light Dark Matter, Phys. Rev. Lett. 115 (2015) 251301 [arXiv:1505.00011] [INSPIRE].  
[147] C. Boehm and P. Fayet, Scalar dark matter candidates, Nucl. Phys. B 683 (2004) 219 [hep-ph/0305261] [INSPIRE].  
[148] D. Banerjee et al., Dark matter search in missing energy events with NA64, Phys. Rev. Lett. 123 (2019) 121801 [arXiv:1906.00176] [INSPIRE].  
[149] BABAR collaboration, Search for Invisible Decays of a Dark Photon Produced in  $e^+ e^-$  Collisions at BaBar, Phys. Rev. Lett. 119 (2017) 131804 [arXiv:1702.03327] [INSPIRE].  
[150] P. deNiverville, M. Pospelov and A. Ritz, Observing a light dark matter beam with neutrino experiments, Phys. Rev. D 84 (2011) 075020 [arXiv:1107.4580] [INSPIRE].  
[151] B. Batell, M. Pospelov and A. Ritz, Exploring Portals to a Hidden Sector Through Fixed Targets, Phys. Rev. D 80 (2009) 095024 [arXiv:0906.5614] [INSPIRE].  
[152] B. Batell, R. Essig and Z. Surujon, *Strong Constraints on Sub-GeV Dark Sectors from SLAC Beam Dump E137*, Phys. Rev. Lett. 113 (2014) 171802 [arXiv:1406.2698] [INSPIRE].  
[153] A. Berlin, N. Blinov, G. Krunjaic, P. Schuster and N. Toro, Dark Matter, Millicharges, Axion and Scalar Particles, Gauge Bosons, and Other New Physics with LDMX, Phys. Rev. D 99 (2019) 075001 [arXiv:1807.01730] [INSPIRE].  
[154] BELLE II, Dark sector searches at BaBar and Belle and outlook for Belle II, Talk by C. Hearty, US Cosmic Visions, March 23, 2017, https://indico.fnal.gov/event/13702/contributions/21158/attachments/13740/17506/Dark sector_BaBar_Belle_II_Hearty.pdf.  
[155] CRESST collaboration, First results from the CRESST-III low-mass dark matter program, Phys. Rev. D 100 (2019) 102002 [arXiv:1904.00498] [INSPIRE].  
[156] CRESST collaboration, Description of CRESST-III Data, arXiv:1905.07335 [INSPIRE].  
[157] S. Tulin and H.-B. Yu, Dark Matter Self-interactions and Small Scale Structure, Phys. Rept. 730 (2018) 1 [arXiv:1705.02358] [INSPIRE].  
[158] M.S. Madhavacheril, N. Sehgal and T.R. Slatyer, Current Dark Matter Annihilation Constraints from CMB and Low-Redshift Data, Phys. Rev. D 89 (2014) 103508 [arXiv:1310.3815] [INSPIRE].  
[159] PLANCK collaboration, Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641 (2020) A6 [arXiv:1807.06209] [INSPIRE].

[160] H. Davoudiasl and W.J. Marciano, Running of the U(1) coupling in the dark sector, Phys. Rev. D 92 (2015) 035008 [arXiv:1502.07383] [INSPIRE].  
[161] J.L. Feng and J. Smolinsky, Impact of a resonance on thermal targets for invisible dark photon searches, Phys. Rev. D 96 (2017) 095022 [arXiv:1707.03835] [INSPIRE].  
[162] K. Schutz and T.R. Slatyer, Self-Scattering for Dark Matter with an Excited State, JCAP 01 (2015) 021 [arXiv:1409.2867] [INSPIRE].  
[163] CRESST collaboration, Results on MeV-scale dark matter from a gram-scale cryogenic calorimeter operated above ground, Eur. Phys. J. C 77 (2017) 637 [arXiv:1707.06749] [INSPIRE].  
[164] S. Yellin, Finding an upper limit in the presence of unknown background, Phys. Rev. D 66 (2002) 032005 [physics/0203002] [INSPIRE].  
[165] I. Bloch, R. Essig, D. Redigolo, M. Sholapurkar, T.-T. Yu and T. Volansky, to appear.  
[166] W. Yin, Highly-boosted dark matter and cutoff for cosmic-ray neutrinos through neutrino portal, EPJ Web Conf. 208 (2019) 04003 [arXiv:1809.08610] [INSPIRE].  
[167] SUPER-KAMIOKANDE collaboration, Supernova Relic Neutrino Search at Super-Kamiokande, Phys. Rev. D 85 (2012) 052007 [arXiv:1111.5031] [INSPIRE].  
[168] S. Knapen, T. Lin and K.M. Zurek, Light Dark Matter: Models and Constraints, Phys. Rev. D 96 (2017) 115021 [arXiv:1709.07882] [INSPIRE].  
[169] J.F. Navarro, C.S. Frenk and S.D.M. White, A universal density profile from hierarchical clustering, Astrophys. J. 490 (1997) 493 [astro-ph/9611107] [INSPIRE].  
[170] M.J. Boschini et al., HelMod in the works: from direct observations to the local interstellar spectrum of cosmic-ray electrons, Astrophys. J. 854 (2018) 94 [arXiv:1801.04059] [INSPIRE].  
[171] Y.-S. Liu, D. McKeen and G.A. Miller, Electrophobic Scalar Boson and Muonic Puzzles, Phys. Rev. Lett. 117 (2016) 101801 [arXiv:1605.04612] [INSPIRE].  
[172] Y.-S. Liu, D. McKeen and G.A. Miller, Validity of the Weizsacker-Williams approximation and the analysis of beam dump experiments: Production of a new scalar boson, Phys. Rev. D 95 (2017) 036010 [arXiv:1609.06781] [INSPIRE].  
[173] BABAR collaboration, Search for a Dark Photon in  $e^{+}e^{-}$  Collisions at BaBar, Phys. Rev. Lett. 113 (2014) 201801 [arXiv:1406.2980] [INSPIRE].  
[174] C. Boehm, M.J. Dolan and C. McCabe, A Lower Bound on the Mass of Cold Thermal Dark Matter from Planck, JCAP 08 (2013) 041 [arXiv:1303.6270] [INSPIRE].  
[175] F. Takahashi, M. Yamada and W. Yin, XENON1T Excess from Anomaly-Free Axionlike Dark Matter and Its Implications for Stellar Cooling Anomaly, Phys. Rev. Lett. 125 (2020) 161801 [arXiv:2006.10035] [INSPIRE].  
[176] K. Kannike, M. Raidal, H. Veermäe, A. Strumia and D. Teresi, Dark Matter and the XENON1T electron recoil excess, Phys. Rev. D 102 (2020) 095002 [arXiv:2006.10735] [INSPIRE].  
[177] C. Boehm, D.G. Cerdeno, M. Fairbairn, P.A.N. Machado and A.C. Vincent, Light new physics in XENON1T, Phys. Rev. D 102 (2020) 115013 [arXiv:2006.11250] [INSPIRE].  
[178] B. Fornal, P. Sandick, J. Shu, M. Su and Y. Zhao, Boosted Dark Matter Interpretation of the XENON1T Excess, Phys. Rev. Lett. 125 (2020) 161804 [arXiv:2006.11264] [INSPIRE].

[179] L. Su, W. Wang, L. Wu, J.M. Yang and B. Zhu, Atmospheric Dark Matter and Xenon1T Excess, Phys. Rev. D 102 (2020) 115028 [arXiv:2006.11837] [INSPIRE].  
[180] A. Bally, S. Jana and A. Trautner, Neutrino self-interactions and XENON1T electron recoil excess, Phys. Rev. Lett. 125 (2020) 161802 [arXiv:2006.11919] [INSPIRE].  
[181] M. Du, J. Liang, Z. Liu, V.Q. Tran and Y. Xue, On-shell mediator dark matter models and the Xenon1T anomaly, Chin. Phys. C 45 (2021) 013114 [arXiv:2006.11949] [INSPIRE].  
[182] G. Choi, M. Suzuki and T.T. Yanagida, XENON1T Anomaly and its Implication for Decaying Warm Dark Matter, Phys. Lett. B 811 (2020) 135976 [arXiv:2006.12348] [INSPIRE].  
[183] Y. Chen, M.-Y. Cui, J. Shu, X. Xue, G. Yuan and Q. Yuan, Sun Heated MeV-scale Dark Matter and the XENON1T Electron recoil Excess, arXiv:2006.12447 [INSPIRE].  
[184] D. Aristizabal Sierra, V. De Romeri, L.J. Flores and D.K. Papoulias, Light vector mediators facing XENON1T data, Phys. Lett. B 809 (2020) 135681 [arXiv:2006.12457] [INSPIRE].  
[185] N.F. Bell, J.B. Dent, B. Dutta, S. Ghosh, J. Kumar and J.L. Newstead, Explaining the XENON1T excess with Luminous Dark Matter, Phys. Rev. Lett. 125 (2020) 161803 [arXiv:2006.12461] [INSPIRE].  
[186] G. Paz, A.A. Petrov, M. Tammaro and J. Zupan, Shining dark matter in Xenon1T, arXiv:2006.12462 [INSPIRE].  
[187] L. Di Luzio, M. Fedele, M. Giannotti, F. Mescia and E. Nardi, Solar axions cannot explain the XENON1T excess, Phys. Rev. Lett. 125 (2020) 131804 [arXiv:2006.12487] [INSPIRE].  
[188] J. Buch, M.A. Buen-Abad, J. Fan and J.S.C. Leung, Galactic Origin of Relativistic Bosons and XENON1T Excess, JCAP 10 (2020) 051 [arXiv:2006.12488] [INSPIRE].  
[189] U.K. Dey, T.N. Maity and T.S. Ray, Prospects of Migdal Effect in the Explanation of XENON1T Electron recoil Excess, Phys. Lett. B 811 (2020) 135900 [arXiv:2006.12529] [INSPIRE].  
[190] Q.-H. Cao, R. Ding and Q.-F. Xiang, Exploring for sub-MeV Boosted Dark Matter from Xenon Electron Direct Detection, arXiv:2006.12767 [INSPIRE].  
[191] A.N. Khan, Can Nonstandard Neutrino Interactions explain the XENON1T spectral excess?, Phys. Lett. B 809 (2020) 135782 [arXiv:2006.12887] [INSPIRE].  
[192] K. Nakayama and Y. Tang, Gravitational Production of Hidden Photon Dark Matter in Light of the XENON1T Excess, Phys. Lett. B 811 (2020) 135977 [arXiv:2006.13159] [INSPIRE].  
[193] R. Primulando, J. Julio and P. Uttayarat, *Collision Constraints on a Dark Matter Interpretation of the XENON1T Excess*, Eur. Phys. J. C **80** (2020) 1084 [arXiv:2006.13161] [INSPIRE].  
[194] H.M. Lee, Exothermic dark matter for XENON1T excess, JHEP 01 (2021) 019 [arXiv:2006.13183] [INSPIRE].  
[195] J. Smirnov and J.F. Beacom, New Freezeout Mechanism for Strongly Interacting Dark Matter, Phys. Rev. Lett. 125 (2020) 131301 [arXiv:2002.04038] [INSPIRE].