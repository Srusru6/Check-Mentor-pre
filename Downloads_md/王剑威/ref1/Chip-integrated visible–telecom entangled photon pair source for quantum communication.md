# Chip-integrated visible-telecom entangled photon pair source for quantum communication

Xiyuan Lu  $^{1,2\star}$ , Qing Li  $^{1,2}$ , Daron A. Westly $^{1}$ , Gregory Moille $^{1,2}$ , Anshuman Singh  $^{1,2}$ , Vikas Anant $^{3}$  and Kartik Srinivasan  $^{1\star}$

Photon pair sources are fundamental building blocks for quantum entanglement and quantum communication. Recent studies in silicon photonics have documented promising characteristics for photon pair sources within the telecommunications band, including sub-milliwatt optical pump power, high spectral brightness and high photon purity. However, most quantum systems suitable for local operations, such as storage and computation, support optical transitions in the visible or short near-infrared bands. In comparison to telecommunications wavelengths, the higher optical attenuation in silica at such wavelengths limits the length scale over which optical-fibre-based quantum communication between such local nodes can take place. One approach to connect such systems over fibre is through a photon pair source that can bridge the visible and telecom bands, but an appropriate source, which should produce narrow-band photon pairs with a high signal-to-noise ratio, has not yet been developed in an integrated platform. Here, we demonstrate a nanophotonic visible-telecom photon pair source, using high quality factor silicon nitride resonators to generate narrow-band photon pairs with unprecedented purity and brightness, with a coincidence-to-accidental ratio up to  $3,780 \pm 140$  and a detected photon pair flux up to  $(18,400 \pm 1,000)$  pairs  $\mathrm{s}^{-1}$ . We further demonstrate visible-telecom time-energy entanglement and its distribution over a  $20\mathrm{km}$  fibre, far exceeding the fibre length over which purely visible wavelength quantum light sources can be efficiently transmitted. Finally, we show how dispersion engineering of the microresonators enables the connections of different species of trapped atoms/ions, defect centres and quantum dots to the telecommunications bands for future quantum communication systems.

long-distance quantum communication requires resources for the low-loss storage and transmission of quantum information<sup>1,2</sup>. For fibre optic networks, this requirement presents a challenge, in that many systems that are best suited for storage, including trapped ions, neutral atoms and spins in crystals, are connected to photons in the visible or short near-infrared (NIR) bands<sup>3</sup>, where losses in silica fibres are orders of magnitude higher than at telecommunications wavelengths<sup>4</sup>. Although a quantum frequency conversion interface can bridge the spectral gap between the relevant wavelengths<sup>5</sup>, it can be challenging, both in finding appropriate laser sources to connect the input and output wavelengths, and also in limiting added noise photons due to the strong classical pump fields. These challenges are more acute as the local quantum system's operating wavelength decreases and moves further away from the telecommunications band.

A second approach to connecting photonic quantum systems over distance is through suitably engineered entangled photon pair sources. In particular, quantum memories can be remotely entangled via entanglement swapping[6,7], in which photons entangled with the two distant memories propagate towards each other and meet, where they are subjected to a Bell-state measurement. For visible/short-NIR memories, the propagation distance in optical fibre is limited as described above. To overcome this limitation, one can introduce entangled photon pair sources in which one photon is resonant with the memory (that is, at a visible wavelength) and the other is in the telecom band (Fig. 1). Successive entanglement swapping operations can then entangle the memories, with their separation now limited by the propagation distance in optical fibre in the telecom band. Such visible-telecom pair sources might also find use

in related scenarios—for example, Bell inequality violations using nitrogen-vacancy centre spins in diamond<sup>8</sup>.

Existing visible-telecom photon pair sources are in platforms such as periodically poled nonlinear crystals, photonic crystal fibres and millimeter-scale crystalline microresonators. The first two platforms generate broadband photons, so that spectral filtering to achieve the narrow linewidths needed for interaction with local quantum systems must be implemented. Filtering after pair generation comes at the price of a decrease in collection efficiency and signal-to-noise ratio, so incorporation of the nonlinear medium into a macroscopic cavity has been pursued. The crystalline microresonator platform, although promising, currently exhibits a coincidence-to-accidental ratio (CAR) below 20, which can be a constraint in applications. In general, these platforms all lack the potential for scalable fabrication and integration common to the planar systems used in nanophotonics.

A nanophotonic device platform for narrow-linewidth, high-quality visible-telecom photon pairs is the whispering gallery mode microresonator based on silicon photonics<sup>15</sup>. Recent studies have documented promising characteristics for photon pair sources based on spontaneous four-wave mixing (SFWM) in the telecommunications band, including sub-milliwatt optical pump power, high spectral brightness and high photon purity<sup>16-21</sup>, and the potential for large-scale integration<sup>22</sup>. Whereas silicon's narrow bandgap forbids operation below  $1.1\mu \mathrm{m}$ , stoichiometric silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)$  has a much wider bandgap, enabling operation across wavelengths from the near-ultraviolet to the mid-infrared. Such broadband performance has been exploited in octave-spanning optical frequency combs<sup>23-25</sup>, and such microcombs have been operated sub-threshold

![](images/aa13d0dfde8499bb1dfb4c71bba9767094aa6f3c1884b780ef46cbbc491184f0.jpg)  
a

![](images/cc4008d07593014ac7b39cdc929447d323a884b399b1a96c4c412016c54b3cca.jpg)  
b

![](images/e66ec6023064d8ec2f593d4a3ae04e9b669ad6a0acb5be0e113d786793d6fd5a.jpg)  
c  
Fig. 1 | Motivation and scheme for a chip-integrated visible-telecom entangled photon pair source. a, Intended application, where photon pairs generated from a silicon nitride nanophotonic chip (centre) connect the visible and telecommunication bands, to enable a link between a nitrogen-vacancy centre in diamond (left) and the telecom fibre network (right), for example. b, Scheme for cavity-enhanced SFWM. The continuous-wave, classical pump field at frequency  $\omega_{\mathrm{p}}$  generates signal and idler photons at  $\omega_{\mathrm{s}}$  and  $\omega_{\mathrm{i}}$ , respectively, dictated by energy conservation  $2\omega_{\mathrm{p}} = \omega_{\mathrm{s}} + \omega_{\mathrm{i}}$ . The nearest relevant cavity mode frequencies are at  $\hat{\omega}_{\mathrm{p}}, \hat{\omega}_{\mathrm{s}}$  and  $\hat{\omega}_{\mathrm{i}}$ , respectively. Phase-matching of light generated in these optical modes is equivalent to the condition on the cavity azimuthal mode numbers  $m$  that  $2m_{\mathrm{p}} = m_{\mathrm{s}} + m_{\mathrm{i}}$ . c, Examples of local quantum systems with optical transitions in the visible/short NIR band (left), and classification of the telecommunications wavelength bands (right).

to generate high-dimensional, frequency-bin entangled photon pairs in the telecom band[26,27]. Similar dispersion-engineered  $\mathrm{Si}_3\mathrm{N}_4$  microresonators have been used to achieve efficient single-photon-level frequency conversion interfaces between the  $980\mathrm{nm}$  and  $1,550\mathrm{nm}$  bands[28]. Here, we demonstrate a family of visible/short NIR-telecom photon pair sources using the  $\mathrm{Si}_3\mathrm{N}_4$  microresonator platform. In particular, we show that it is possible to overcome the primary challenge in the development of such sources, which is in achieving phase- and frequency-matching of narrow-band modes over a spectral separation of  $>250\mathrm{THz}$ . Our source produces narrowband visible-telecom photon pairs with an unprecedented CAR of  $3,780\pm 140$  at an on-chip pair flux of  $(1,200\pm 300)$  pairs  $\mathrm{s}^{-1}$  and an unprecedented detected photon pair flux of  $(18,400\pm 1,000)$  pairs  $\mathrm{s}^{-1}$  with a CAR of  $26.8\pm 0.1$ . Moreover, we demonstrate time-energy entanglement of the pairs with a visibility of  $(82.7\pm 0.2)\%$ . We further distribute the entanglement over a distance  $>20\mathrm{km}$  in optical fibre, far exceeding what would be possible for purely visible quantum sources, with a visibility of  $(58\pm 1)\%$ . We also experimentally show that the visible photons can be shifted from  $630\mathrm{nm}$  to  $810\mathrm{nm}$  by varying the pump wavelength and microring width. Our demonstration of a chip-integrated visible-telecom photon pair source emitting bright, pure and narrow-linewidth photons has the

potential to serve as an important resource in connecting quantum memories with telecommunication networks.

# System design

The device is a  $\mathrm{Si}_3\mathrm{N}_4$  microring resonator with a lower silicon dioxide  $(\mathrm{SiO}_2)$  cladding and a top air cladding.  $\mathrm{Si}_3\mathrm{N}_4$  microrings support high quality factor (Q) whispering-gallery modes, which combine a long photon lifetime with localization into a small effective volume (V). This leads to a large optical intensity (that is,  $I\sim Q / V$ ), which is critical for the SFWM efficiency[29,30]—that is, in reducing pump power and excess noise. Moreover, the broad transparency window of  $\mathrm{Si}_3\mathrm{N}_4 / \mathrm{SiO}_2$ , and the ability to compensate for material dispersion through waveguide dispersion, are critical to engineering visible-telecom photon pair sources. We outline the basic design procedure in this section.

Unlike the linear momentum conservation criterion in a waveguide  $(\Delta \beta = 0$ , where  $\beta$  is the propagation constant), phase-matching of the azimuthal momentum is required in a microring. As the electromagnetic field of a whispering gallery mode has an azimuthal dependence that scales as  $\exp (im\phi)$ , where  $\phi$  is the azimuthal angle and  $m$  is the mode number, phase-matching becomes a mode number matching criterion  $(\Delta m = 0)$ . For degenerately pumped

SFWM, the criterion is  $2m_{\mathrm{p}} - m_{\mathrm{s}} - m_{\mathrm{i}} = 0$  where  $m_{\mathrm{p}} / m_{\mathrm{s}} / m_{\mathrm{i}}$  are the azimuthal mode numbers for the pump/signal/idler modes. Next, assuming an appropriate set of modes is found to satisfy this requirement, the energy conservation condition imposed by SFWM  $(2\omega_{\mathrm{p}} - \omega_{\mathrm{s}} - \omega_{\mathrm{i}} = 0)$  must involve pump/signal/idler fields  $(\omega_{\mathrm{p}} / \omega_{\mathrm{s}} / \omega_{\mathrm{i}})$  that are resonant with the corresponding cavity modes  $(\hat{\omega}_{\mathrm{p}} / \hat{\omega}_{\mathrm{s}} / \hat{\omega}_{\mathrm{i}})$ , with a maximum frequency mismatch dictated by the  $Q$  of the corresponding cavity mode; for example,  $\delta \omega_{\mathrm{p,s,i}} = |\omega_{\mathrm{p,s,i}} - \hat{\omega}_{\mathrm{p,s,i}}| \lesssim \hat{\omega}_{\mathrm{p,s,i}} / 2Q_{\mathrm{p,s,i}}$ . It represents a major challenge to fabricate nanophotonic devices that match frequencies separated over hundreds of terahertz with an accuracy within a cavity linewidth (approximately 1 GHz for a loaded  $Q$  of  $10^{5}$ ).

Most demonstrated microresonator-based SFWM devices have not required extensive dispersion engineering, largely because the frequency separation between the pump, signal and idler has been relatively small (for example, all lie within the telecommunications C-band) $^{15}$ . In such a scenario, mode number matching is trivially satisfied by signal and idler modes whose azimuthal orders are separated from the pump by an equal number, so that  $m_{\mathrm{s}} - m_{\mathrm{p}} = m_{\mathrm{p}} - m_{\mathrm{i}}$ . Frequency matching of these modes is satisfied in a resonator with sufficiently low dispersion over the spectral window of interest, and does not present a major difficulty if the overall spectral window is small enough.

In contrast, our SFWM process is distinguished by the large frequency separation between the optical modes, corresponding to over one hundred free spectral ranges (FSRs), which is greater than the scan range of any single laser. This makes counting of mode number offsets, to find the conditions for which  $m_{\mathrm{s}} - m_{\mathrm{p}} = m_{\mathrm{p}} - m_{\mathrm{i}}$ , very difficult. We instead identify the absolute azimuthal numbers of the targeted modes ( $m_{\mathrm{s}}, m_{\mathrm{p}}$  and  $m_{\mathrm{i}}$ ), using a novel method described in the section 'Mode identification' below.

The mode identification procedure, together with dispersion engineering to ensure that the targeted modes adequately satisfy frequency matching for the desired SFWM process (discussed below in the section 'Dispersion design'), enables the generation of visible-telecom photon pairs within the ring resonator. However, for the overall chip to be a bright and power-efficient photon pair generator, the coupling into and out of the resonator via access waveguides must also be optimized. As described in the section 'Coupling design', we use an add-drop geometry, together with the ability to cut off long-wavelength modes in one of the waveguides as a result of its asymmetric cladding (top air cladding, bottom  $\mathrm{SiO}_2$  cladding) to separate the generated visible and telecom photons into different output waveguides.

# Dispersion design

The core of the device is a high-  $Q$ $\mathrm{Si}_3\mathrm{N}_4$  microring with three key parameters:  $\mathrm{Si}_3\mathrm{N}_4$  film thickness, ring width and ring radius. The dispersion of the optical modes in the device is fully determined by these three parameters, given ellipsometric measurements of the wavelength-dependent refractive index of the  $\mathrm{Si}_3\mathrm{N}_4$  and  $\mathrm{SiO}_2$  layers. We first carry out a waveguide simulation with the first two parameters to estimate the frequency mismatch, as shown in Fig. 2a. The frequency mismatch is calculated by the finite-element method as  $\Delta \omega = [(n_{\mathrm{s}}\omega_{\mathrm{s}} + n_{\mathrm{i}}\omega_{\mathrm{i}}) / (2n_{\mathrm{p}})] - \omega_{\mathrm{p}}$ , where  $n_{\mathrm{s}}, n_{\mathrm{i}}$  and  $n_{\mathrm{i}}$  are the effective indices at the frequencies  $\omega_{\mathrm{s}}, \omega_{\mathrm{p}}$  and  $\omega_{\mathrm{i}}$  (corresponding wavelengths of  $668.4\mathrm{nm}$ ,  $934.0\mathrm{nm}$  and  $1,550.0\mathrm{nm}$ , respectively, for signal, pump and idler modes). For a device with a larger thickness, the ring width needs to be smaller for the geometric dispersion to compensate the material dispersion. At a  $\mathrm{Si}_3\mathrm{N}_4$  thickness of  $500\mathrm{nm}$ , the targeted ring width is about  $1,200\mathrm{nm}$ . We then run full simulations for the  $\mathrm{Si}_3\mathrm{N}_4$  microring with a radius of  $25\mu \mathrm{m}$  to find the optical modes around the targeted wavelengths, which have mode numbers of 443, 303 and 163, respectively. These mode numbers satisfy  $2m_{\mathrm{p}} = m_{\mathrm{s}} + m_{\mathrm{i}}$ , and their corresponding resonances are close to the targeted frequencies (within one FSR). The ring simulation shows

that the pump mode has a small group velocity dispersion (GVD) at the geometry of interest in the inset of Fig. 2b. The frequency mismatches of the targeted modes  $\Delta \omega = \omega_{\mathrm{p}} - (\omega_{\mathrm{s}} + \omega_{\mathrm{i}}) / 2$  are calculated and plotted in Fig. 2b, where the bending effect yields additional geometric dispersion that offsets the targeted geometry from that determined from waveguide simulations in Fig. 2a. For a device thickness of  $500\mathrm{nm}$ , the targeted ring width is around  $1,140\mathrm{nm}$ .

# Coupling design

The wide spectral separation of the SFWM process in this work also poses a challenge for the resonator-waveguide coupling design. To couple visible, pump and telecom modes efficiently, we employ two waveguides that separate the coupling tasks with the scheme shown in Fig. 2c. A scanning electron microscope (SEM) image of the device is presented in Fig. 2d. The top pulley waveguide is wrapped around the microring to provide the extra interaction length needed to couple the pump and visible modes efficiently at the same time. This waveguide has a width of  $560\mathrm{nm}$ , which supports single-mode operation for the pump mode, and is cut off for the telecom mode, a consequence of the asymmetric cladding (above a certain wavelength, not even a fundamental mode is guaranteed). Figure 2e shows the calculated coupling  $Q$  (using the coupled mode theory approach[28,31]) of this pulley waveguide for the pump and signal modes, as a function of coupling gap and for a coupling length of  $33\mu \mathrm{m}$ . For gaps between  $200\mathrm{nm}$  to  $250\mathrm{nm}$ , the pump mode is close to critically coupled and the signal mode is slightly over-coupled for intrinsic  $Q$  values around one million. The bottom straight waveguide (Fig. 2d) is used to out-couple the telecom mode and has a width of  $1,120\mathrm{nm}$ . This width supports single-mode operation at telecom wavelengths, and as shown in Fig. 2f, the coupling gap for the straight waveguide can be tuned to couple the telecom mode only, while not coupling pump and signal modes (they are severely undercoupled), for optical modes with intrinsic  $Q$  values around one million.

# Mode identification

The dispersion design presented in the previous sections is targeted to specific mode numbers and cavity frequencies. Such unambiguous knowledge of optical mode numbers is absent in traditional transmission measurements of whispering gallery mode resonators. Here, we employ a method of mode splitting to identify the mode numbers $^{32}$ , by introducing a sinusoidal modulation of the form  $\delta r = \alpha \cos (n\phi)$  to the inside boundary of the microring (Fig. 3a, b). When the modulation index  $n$  does not line up with the azimuthal order  $m$  of the optical mode (bottom panel of Fig. 3a,  $n \neq 2m$ ), the perturbation is not in phase with the optical mode, and thus any reflection induced by the perturbation does not coherently build up. Therefore, in this case, the optical mode (both clockwise and anticlockwise) remains unperturbed. In contrast, when the modulation index lines up with the azimuthal order of the optical mode so that  $n = 2m$ , the phase degeneracy is removed and the clockwise and anticlockwise optical modes are renormalized into two modes (top panel of Fig. 3a). One mode is located near the outside of the modulation and has a higher frequency, while the other mode is located near the inside of the modulation and has a lower frequency. This splitting in frequency is proportional to the modulation amplitude. At a modulation amplitude of  $50\mathrm{nm}$  (Fig. 3b), the frequency splitting is much larger than the cavity linewidth and is therefore visible in the transmission spectra. Thus, by changing the modulation period, the optical mode numbers can be identified, as shown in Fig. 3c for modes in the signal, pump and idler bands. The  $Q$  values of modes in the ring-width-modulated resonators are still reasonably high ( $Q > 10^{5}$ ), so that one could envisage using this approach to split modes that are some small number of FSRs away from the targeted ones, enabling their mode identification. However, as we would like to use as high  $Q$  resonances as possible for pair generation, we instead use the mode splitting approach on test devices that

![](images/67704cbfbfd5633118655c34f8316f86845af4a767eea33f885d3dad8f38921a.jpg)

![](images/f3bf2677b168f9e0091741dad085cdccb9f633a205e80dfd65153254db165228.jpg)

![](images/2f9ba877c9ae63a7337e8fdd29a60906c477ea136fcd4d5c79245f07571f51fc.jpg)

![](images/8d01da39f315946db09bb3ad9348599a078dd6bdb8bf21ad54157a9ad34542b8.jpg)

![](images/fe7bce5df7f81fdbb9e08d54a7df348754baf42ced6daddbf0a45587488ff1f7.jpg)  
Fig. 2 | Dispersion/coupling engineering essential for the chip-integrated visible-telecom photon source. a,b, Simulation of the device dispersion engineering for phase and frequency matching, where frequency mismatch  $(\Delta \omega = \omega_{\mathrm{p}} - (\omega_{\mathrm{s}} + \omega_{\mathrm{t}}) / 2)$  is plotted for phase-matched pump, signal and idler mode sets  $(2m_{\mathrm{p}} = m_{\mathrm{s}} + m_{\mathrm{t}})$ , as a function of ring waveguide width (x axis) and thickness  $t$  (different displayed curves). The simulation in a is based on a model in which straight waveguide dispersion (no bending effect) is used and the wavelengths are fixed to be 668.375 nm, 934.000 nm and 1,550.000 nm for signal, pump and idler, respectively. The simulation in b is based on a full model in which the ring dispersion is used. The mode numbers are fixed to be 443, 303 and 163 for the signal, pump and idler modes, respectively. The inset of b shows the GVD of a microring with a 500 nm thickness and a 1,150 nm ring width. c-f, An appropriate design of waveguide-resonator coupling is required to ensure that pump/generated photons are efficiently injected/ extracted from the resonator. c, Waveguide-resonator coupling scheme. d, Scanning electron microscope images show a fabricated device with a pulley waveguide on the top, for injecting the 930 nm band pump and extracting the 660 nm band signal, and a straight waveguide on the bottom, for extracting the 1,550 nm band idler. e,f, Simulation of the coupling Q factors of the pulley waveguide (e) and straight waveguide (f) for the pump/signal and pump/signal/idler (the pulley waveguide does not support a mode at the idler wavelength).

![](images/ba8002ab11c76f84e42808c78701545e9f3f61c9910b2fccf071bfb0e5e3236f.jpg)

are fabricated on the same chip as the devices in which we generate photon pairs. The good reproducibility of device fabrication across a chip ensures that these test mode splitting devices have spectra that are well-matched to the photon pair generation devices.

# Phase/frequency matching

Through the mode number identification process, it is straightforward to find the targeted modes and calculate their frequency mismatch. Figure 4a shows the normalized cavity transmission for

a fabricated device in the signal, pump and idler bands, respectively. The frequency mismatch of various configurations that satisfy mode number matching is shown in Fig. 4b. The targeted optical modes, shaded in Fig. 4a, have azimuthal mode numbers  $m_{\mathrm{s}} = 443$ ,  $m_{\mathrm{p}} = 303$  and  $m_{\mathrm{i}} = 163$ . The wavelengths of the modes, measured by a waveneter with an accuracy of  $0.1\mathrm{pm}$ , are  $668.3789\mathrm{nm}$ ,  $933.6211\mathrm{nm}$  and  $1,547.8960\mathrm{nm}$ . The loaded Qs of the three modes, shown in Fig. 4c, are  $(1.52\pm 0.02)\times 10^{5}$ ,  $(1.04\pm 0.02)\times 10^{6}$  and  $(1.93\pm 0.04)\times 10^{5}$ , corresponding to loaded cavity linewidths of

![](images/6d675d63b13fc831d671ae48d72932173b39c6665a2752f03403b5b4294d9abd.jpg)  
a

![](images/e38dab47031b4a7226b91abc8b4e6a97d1ff8e3920c9ab1ff8dbe939bb5f485c.jpg)  
b

![](images/aa1a48cbf0359951e03855c079a54fb891543c99f09ad7478cef1b06d185ac50.jpg)  
c

![](images/a822877534422b0f994e05a86672a4ab6dc749f53e4f610898e0cca0861da734.jpg)

![](images/00340573758902d9bfbf1365886593760c888807b80801792400d04c272c29ab.jpg)

![](images/c68e913ce94e07db5cb33f7bf16f5cfbe5ccc0a8534e8f5e17ed1acb13f1b97a.jpg)

![](images/9fc8e0878f00032fab525ca60b49d1d867674b3d4f91778bb55817f36f67d44a.jpg)

![](images/9295c4767eff33ee71dd240bf1be798b31c9cd3fbf5f7242c430f18da15b8c3a.jpg)

![](images/64a3283423781b760cc469d70270a70fce310b932d0aac98b95435b6e6085d0f.jpg)  
Fig. 3 | Mode splitting technique is employed to identify the exact mode numbers for phase matching. a, Principle of azimuthal mode number identification by mode splitting. The colour maps show top views of the dominant electric field component (in the radial direction) for microring optical modes with azimuthal mode number  $m = 4$  (top) and  $m = 5$  (bottom), with red/blue representing positive/negative values of the field. The mode splitting is created by periodic modulation of the inside boundary of the microring, of the form  $\delta r = \alpha \cos(n\phi)$ . When the modulation index  $n$  is in phase with the azimuthal order of the mode  $m$  (top), so that  $n = 2m$ , frequency splitting occurs. When  $n \neq 2m$ , the optical modes are unperturbed (bottom). b, Zoomed-in SEM images of the mode splitting devices in the signal (left), pump (centre) and telecom (right) bands, in which an inner modulation amplitude  $\alpha = 50$  nm is applied. The approximate modulation period in the three cases is  $170$  nm,  $250$  nm and  $460$  nm, respectively. c, Measured transmission spectra from  $\mathrm{Si}_3\mathrm{N}_4$  microrings fabricated with the inner boundary modulation, in the signal (visible), pump (930 nm) and telecom bands, shown in red, green and blue, respectively, where the modulation has been varied across the spectra to target the labelled mode numbers. Insets in the left panels are zoomed-in views to show the mode splitting more clearly.

![](images/010329e3957c589dffdea8d677cd8de4522e1d65753ac8d5c26a50c924dbf405.jpg)

![](images/7abe1b081ed814cefd08148cca8bf33a61e2ed0bcb647e440b0f14d5219ba41a.jpg)

$(2.95 \pm 0.04) \mathrm{GHz}$ ,  $(0.31 \pm 0.01) \mathrm{GHz}$  and  $(1.00 \pm 0.02) \mathrm{GHz}$ , respectively. The uncertainties indicate  $95\%$  confidence intervals for nonlinear least-squares fits of the cavity resonances to Lorentzian lineshapes. The frequency mismatch of the targeted modes  $(\Delta \omega = \omega_{\mathrm{p}} - (\omega_{\mathrm{s}} + \omega_{\mathrm{i}}) / 2)$  is only  $(0.16 \pm 0.04) \mathrm{GHz}$  (coloured by red in Fig. 4b), which is smaller than the cavity linewidths. Thus both

phase and frequency matching are satisfied and the targeted SFWM process is permitted.

Given the match of mode numbers and cavity frequencies as shown in Fig. 4a-c, we now consider the generation of photon pairs. Continuous-wave light from an external cavity diode laser is used to pump the cavity mode at  $933.6\mathrm{nm}$ , and the spectrum of SFWM

![](images/0565ad4f6431854ed5567f3df5d87d987a54b9acff040ca79952ef6240835c3b.jpg)  
a

![](images/641adec9d2e30e19feedbaf2d454d960f8e8f96247fe6730b4af6f18379eb18e.jpg)

![](images/dd86a48a4b9f8e242ba580ea82e459e71a10eb76b7bcf74966c3a7fb2cf690c7.jpg)

![](images/97529919b61d1a7d8be004004d943bfda13435017facf8485a431efaa24af76b.jpg)  
b

![](images/8d8ac446997772c36ce884752d690bb987732083307465a3134529322a403d79.jpg)  
c

![](images/d5c3af997248552c18c2408a959b910c865e3d931f5abe6df751d49b31a75b56.jpg)

![](images/ff41cee3e36e376e20c594744558f4aeb7fed4bc00174be2e1fd0bdf0aff8ccf.jpg)

![](images/d6b41736d8d80ed8c3dda5c00635c314df6b4a1055df8f92b6e0fc89f5ca19bf.jpg)

![](images/dfa6604eb4d2561c553834e8181889f5dffe005bbc7363863d742a9bfc2d80d0.jpg)

![](images/7b3854915a34486054cb0979fa352822962aa112388acd77f064be78cc69e780.jpg)

![](images/e149cd03bcb3f27ff55de544deac005b2b0046409cadbed9a1a5a887fa1f4a9a.jpg)  
d  
Fig. 4 | Visible-telecom photon pairs are generated when both phases and frequencies are matched. a, Transmission spectrum of the microring resonator in the signal (visible), pump (930 nm) and idler (telecom) bands, respectively. The targeted modes for photon pair generation are highlighted, with their azimuthal mode numbers labelled. b, Frequency mismatch  $\Delta \omega = \omega_{\mathrm{p}} - (\omega_{\mathrm{s}} + \omega_{\mathrm{i}}) / 2$ , determined from wavemeter measurements in which the pump mode is fixed ( $m_{\mathrm{p}} = 303$ ) and the signal and idler modes vary in such a way to maintain mode number matching ( $2m_{\mathrm{p}} = m_{\mathrm{s}} + m_{\mathrm{i}}$ ). c, Zoomed-in transmission spectra (top) of the targeted optical modes, with Lorentzian fits in black. Bottom images show cross-sectional views of the simulated dominant electrical field amplitudes (in the radial direction) of each mode, where red/green represent strong/weak amplitudes. d, Schematic depiction of the SFWM process (centre), along with recorded spectra in the visible (left) and telecom (right) bands, measured after edge-pass filters to remove residual pump light, but without narrow-band spectral filtering.

![](images/272ca0ccfd8062c6423d6afe49de136a9347bcca6fbb45cf1319b8a2f123d64b.jpg)

![](images/f99b94fd628bd71a39ca925396205c26e296b5b0c7b2a4a29c25c870d0e9acc3.jpg)

is measured using two grating spectrometers, one to cover the visible wavelength band and the other to cover the telecommunications wavelength band (Fig. 4d). Emission from cavity modes at  $1,547.9\mathrm{nm}$  and  $668.4\mathrm{nm}$  is observed in the spectrometers (spectral resolution is approximately  $100\mathrm{pm}$ ), along with two adjacent sets of pairs. These auxiliary pairs are both matched in mode number, but are weaker in amplitude due to the greater frequency mismatch. For example, the photon pair at  $667.0\mathrm{nm}$  ( $m_{\mathrm{s}} = 444$ ) and  $1,555.2\mathrm{nm}$  ( $m_{\mathrm{i}} = 162$ ) has a frequency mismatch of  $3.86\mathrm{GHz}$ , as shown in Fig. 4b, which is about 10 times larger than that of the brightest pair.

# Photon pair source characterization and comparison

We next use coincidence counting measurements to characterize the quality of the generated photon pairs (Fig. 5a). For coincidence counting, two filters are used to select the targeted spectral channels before single photon detection (see Supplementary Information for details for the experimental set-up). The large spectral separation between pump, signal and idler makes this task straightforward, as the photons can be easily separated by edgepass filters or

broadband demultiplexers. Moreover, the spectra in the signal and idler bands exhibit limited influence from amplified spontaneous emission and Raman noise, which are adjacent to the pump band and do not extend far enough spectrally to strongly influence the pairs. As a result, no broadband noise is observed in either the visible or telecom bands.

Figure 5d presents the pump-power-dependence of the on-chip photon pair flux at the waveguide output and the CAR. The on-chip photon pair flux is inferred from the detected photon pair flux, taking account of the losses in both signal and idler channels (see Supplementary Information for details). At high pump powers, the increase in pair flux is accompanied by a rise in accidental coincidence counts, limiting the achievable CAR values because of the increase in multi-pair generation inherent to spontaneous parametric processes, as well as the generation of noise photons or imperfect spectral rejection of residual pump light. At low pump powers, the decrease in pair flux is accompanied by an almost complete suppression of multi-pair events, so that CAR values are primarily limited by detector dark counts and imperfect filtering. When the pump

![](images/f3f21ffeaa293d2d9dd8bdf161923360e3a80e298f07ce4e1a4370c8ce214081.jpg)  
a

![](images/b88621a83e1e1d161c51cd18023593a04ac889bc660f1b033c8fe7e8f35b72c2.jpg)

![](images/cefe8df7392918f501ac32817ce567fde3a33ace548019cc2f7bfe570b655e2e.jpg)

![](images/2010d38a8f60b4e975016dcccd9e6c7cf5a4269fb1335474303a34cacd037a60.jpg)  
Fig. 5 | Characterizations show state-of-the-art performance for power efficiency and photon purity. a, Experimental scheme for coincidence counting characterizations. SPAD, single-photon avalanche diode; SNSPD, superconducting nanowire single-photon detector. b,c, Coincidence counting traces at pump powers of  $46\mu \mathrm{W}$  and  $146\mu \mathrm{W}$ , respectively. The mean background levels (that is, accidental counting) are normalized to 1. The time bins are 128 ps. d, Pump-power dependence of the visible-telecom photon pair source CAR and on-chip photon pair flux. Error bars are one standard deviation uncertainties. Data points highlighted with colours correspond to coincidence counting traces in b with respective background colours. e, A comparison of the peak CAR values and the raw detected photon pair flux for narrow-band visible-telecom photon pair sources. The open red circles correspond to d and the solid red circles represent data from a separate device with improved telecom-band out-coupling. PPKTP, periodically poled potassium titanyl phosphate; PPLN, periodically poled lithium niobate.

![](images/52217b9e02237f707170db1255140de14a107f9e032a3fa0069e466e06e27430.jpg)

power is around  $46\mu \mathrm{W}$ , the CAR value is about  $2,200 \pm 14$  and the photon pair flux is about  $(4,800 \pm 900)$  pairs  $\mathrm{s}^{-1}$ , where the uncertainties are one standard deviation values based on the fluctuation in detected count rates. The highest CAR measured is  $3,780 \pm 140$  at a pair flux of  $(1,200 \pm 300)$  pairs  $\mathrm{s}^{-1}$ . This CAR value is two orders of magnitude higher than those of previously demonstrated visible-telecom photon pair sources based on photonic crystal fibre and millimeter-scale crystalline disks[1]. When the pump power is near  $146\mu \mathrm{W}$ , the CAR value is  $423 \pm 4$  and the on-chip photon pair flux is about  $(62,000 \pm 5,000)$  pairs  $\mathrm{s}^{-1}$ . At pump powers above  $290\mu \mathrm{W}$ , the photon pair flux shows a weaker increase than expected based on the slope of the lower power data, and is due to optical parametric oscillation in the pump band (see Supplementary Information for additional data). This effectively serves as a competing process that results in a reduced conversion efficiency from the pump to visible-telecom photon pairs. Finally, Fig. 5b, c shows normalized coincidence spectra that correspond to two of the aforementioned cases, with CAR values of  $423 \pm 4$  and  $2,200 \pm 14$ , respectively. The asymmetry in the coincidence peak is a result of the difference in photon lifetimes and detector timing jitters in the telecom and visible bands.

To evaluate the performance of our photon pair source among state-of-the-art narrow-band visible-telecom photon pair sources, we compare in Fig. 5e the CAR and the raw detected photon pair flux

of our photon source with the reported values from the literature, which have primarily been created through spontaneous parametric downconversion in second-order nonlinear optical  $(\chi^{(2)})$  media. To achieve the narrow-bandwidth photons required for most quantum memories, researchers have adopted various schemes, including cavity-enhanced systems that incorporate a bulk quasi-phase-matched crystal[12-14], direct spectral filtering of broadband photons generated by a quasi-phase-matched waveguide or bulk crystal[9], and millimetre-scale whispering gallery mode resonators[1]. We see that our source achieves a combination of CAR and pair detection rate that is as good as those that have been previously documented in more mature, macroscopic (non-integrated) systems. In particular, by further optimizing the waveguide-resonator coupling in the telecom band, we have been able to improve on our source performance (solid red data in Fig. 5e) and achieve a detected pair flux up to  $(18,400 \pm 1,000)$  pairs $^{-1}$ , while maintaining high CARs above 27. This substantially outperforms previous work, and has ramifications for practical applications in which pair flux is a dominant consideration.

# Entanglement distribution over distance

To date, long-haul fibre distribution of time-energy entanglement has focused on telecom-band photon pair sources<sup>33</sup>. However, telecom-band photons are not directly accessible for visible/short-NIR quantum memories. Our visible-telecom photon pair source

![](images/a086b9238aaa8424b481aa3f38861855313e4d9da2cfcaed03c4c9c35393e1f2.jpg)

![](images/71a80f4b18713b8dd01dec5108a6cfab854d27d03915c1332b8e2ab9ef5b5fb0.jpg)  
b-g, Constructive (top: b,d,f) and destructive (bottom: c,e,g) interferences for fibre lengths of 20 m (left), 2.5 km (middle) and 20.65 km (right), respectively. The extracted entanglement visibility of each fibre length is listed above b, d and f, respectively.

![](images/877cc1ce5fe4d6e6ad9a3829caf9103587a705e33699e51047d495d4b6e2b1cc.jpg)

![](images/a567d3f747a38251955ae97f53372297898306e9ec3abe4151c1bdce4cb98147.jpg)

![](images/aff24caf9c0cc0ad7eb087439f4dd64ef1339f2ed1b19d79882f167cc7125a0c.jpg)  
Fig. 6 | Visible-telecom time-energy entanglement is generated and then distributed over distance. a, A Franson interferometer, consisting of two unbalanced Mach-Zehnder interferometers (MZIs), one for the visible photons and the other for the telecom photons, is used to verify visible-telecom time-energy entanglement. The cases of both photons taking their respective short path  $(|ss >)$  and both photons taking their respective long path  $(|ll >)$  are indistinguishable, resulting in quantum interference. s and l are used to denote the short and long paths, respectively. The amplitude of the interference depends on the phases of the signal/idler MZIs  $(\varphi_{s} / \varphi_{l})$ . A fibre spool is added to the telecom arm to distribute the entanglement over distance.

![](images/c8e4363ce91d03e9835c0409904487d14f86842ee8f097508ffc87135e656380.jpg)

![](images/628b660b11f9fdfdc37684b180058acac3431f08ab9781109a8e778c81df9426.jpg)

has the potential of directly connecting to quantum memories by visible photons, while distributing the entanglement over distance by telecom photons. In this section we demonstrate visible-telecom entanglement distribution through  $20\mathrm{km}$  fibre, with narrowband photons that are suitable for quantum memories. As a point of comparison, typical single-mode fibre loss in the  $660\mathrm{nm}$  band is  $10\mathrm{dBkm}^{-1}$ , indicating that entanglement distribution over such a fibre length would not be practically feasible for quantum light sources operating purely at visible wavelengths.

Figure 6a shows the experimental scheme for the entanglement distribution. Time-energy entanglement is verified by two unbalanced Mach-Zehnder interferometers (MZIs) with a variable length of telecom fibre included in the telecom path. The path length differences of these two MZIs are identical  $(\sim 2\mathrm{m})$ . The visible MZI is stabilized by a thermal phase shifter and a reference laser locked to a Doppler-free rubidium spectral line. The telecom MZI is stabilized by a fibre phase shifter and a telecom laser which is internally locked to a reference gas cell. Photon pairs have four paths, namely, short-short, long-long, short-long and long-short for visible-telecom channels. In the coincidence spectrum, the centre coincidence peak contains the first two paths, which can interfere with each other, whereas the side peaks correspond to the latter two paths, which show no interference. The amplitude of the interference peak depends on the relative phases of the two MZIs. In the experiment, the telecom MZI is fixed in phase and the visible MZI changes its phase as the phase locking point of the reference laser changes.

The visibility of time-energy entanglement with a  $20\mathrm{m}$  fibre is calculated to be  $(82.7\pm 0.2)\%$  (see Methods for details). For the

constructive interference (Fig. 6b), the interference peak has a CAR of 32 and both side peaks have a CAR around 8. For the destructive interference (Fig. 6c), the destructive peak has a CAR of 3.6 with the side peak levels showing a similar CAR around 8. The departure from a perfect visibility of  $100\%$  can be attributed to the imperfect balancing of the MZIs, the differences in the delay time, and the phase stabilization. To distribute the entanglement over distance, we pass telecom photons through a fibre of length  $2.5\mathrm{km}$  and  $20.65\mathrm{km}$  respectively, as shown in Fig. 6d-g. The corresponding entanglement visibilities are  $(68\pm 2)\%$  and  $(58\pm 1)\%$ . The degradation of the visibility for longer fibre is probably caused by the phase fluctuation in the fibre spool. Nevertheless, quantum interference is still clearly resolvable with the  $20\mathrm{km}$  fibre spool. For example, as shown in Fig. 6g, the summation of coincidence counts of short-short and long-long paths is smaller than that of either short-long or long-short paths, which clearly shows destructive interference with a visibility over  $50\%$ .

# Discussion

We have demonstrated the ability to engineer on-chip nanophotonic resonators to create photon pair sources with a wide spectral separation between signal and idler, so that one photon is in the visible and the other in the telecom band. We use the  $\mathrm{Si}_3\mathrm{N}_4 / \mathrm{SiO}_2 / \mathrm{Si}$  platform to enable this work, due to its large Kerr nonlinearity, broadband optical transparency, and strong ability to engineer dispersion through geometric (waveguiding and bending) effects. After performing electromagnetic simulations to identify sets of microring resonator modes that can satisfy both phase-matching

(mode number matching) and frequency matching, we use a mode identification technique that allows us to experimentally determine absolute azimuthal mode numbers in fabricated devices, thereby paving the way for the experimental demonstration of photon pair generation. Our photon pair sources generate bright and pure visible-telecom photon pairs with unprecedented CAR values and photon pair flux at sub-milliwatt pump power. We have used our nanophotonic chip source to further demonstrate visible-telecom time-energy entanglement over a  $20\mathrm{km}$  fibre. Finally, as described in detail in the Supplementary Information, we are able to use the same design principles as described in the main text to create a family of pair sources in which the visible wavelength photon can be varied from  $630\mathrm{nm}$  to  $810\mathrm{nm}$ . Through further development, we anticipate that these sources can be used in efforts to link distant quantum systems via entanglement swapping[7,34].

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of data availability and associated accession codes are available at https://doi.org/10.1038/s41567-018-0394-3.

Received: 30 May 2018; Accepted: 3 December 2018  
Published online: 21 January 2019

# References

1. Gisin, N. & Thew, R. Quantum communication. Nat. Photon. 1, 165-171 (2007).  
2. Lvovsky, A. I., Sanders, B. C. & Tittel, W. Optical quantum memory. Nat. Photon. 3, 706-714 (2009).  
3. Simon, C. et al. Quantum memories: A review based on the European integrated project Qubit Applications (QAP). Euro. Phys. J. D 58, 1-22 (2010).  
4. Miya, T., Terunuma, Y., Hosaka, T. & Miyashita, T. Ultimate low-loss single-mode fibre at  $1.55\mu \mathrm{m}$ . *Electron. Lett.* 15, 106-108 (1979).  
5. Raymer, M. G. & Srinivasan, K. Manipulating the color and shape of single photons. Phys. Today 65, 32-37 (2012).  
6. Pan, J.-W., Bouwmeester, D., Weinfurter, H. & Zeilinger, A. Experimental entanglement swapping: entangling photons that never interacted. Phys. Rev. Lett. 80, 3891-3894 (1998).  
7. Halder, M. et al. Entangling independent photons by time measurement. Nat. Phys. 3, 692-695 (2007).  
8. Hensen, B. et al. Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres. Nature 526, 682-686 (2015).  
9. Clausen, C. et al. A source of polarization-entangled photon pairs interfacing quantum memories with telecom photons. New J. Phys. 16, 093058 (2014).  
10. Soller, C. et al. Bridging visible and telecom wavelengths with a single-mode broadband photon pair source. Phys. Rev. A. 81, 031801 (2010).  
11. Schunk, G. et al. Interfacing transitions of different alkali atoms and telecom bands using one narrowband photon pair source. Optica 2, 773-778 (2015).  
12. Fekete, J., Rieländer, D., Cristiani, M. & de Riedmatten, H. Ultranarrow-band photon-pair source compatible with solid state quantum memories and telecommunication networks. Phys. Rev. Lett. 110, 220502 (2013).  
13. Slattery, O., Ma, L., Kuo, P. & Tang, X. Narrow-line width source of greatly non-degenerate photon pairs for quantum repeaters from a short singly resonant cavity. Appl. Phys. B 121, 413-419 (2015).  
14. Rielander, D., Lenhard, A., Mazzera, M. & de Riedmatten, H. Cavity enhanced telecom heralded single photons for spin-wave solid state quantum memories. New J. Phys. 18, 123013 (2016).  
15. Caspani, L. et al. Integrated sources of photon quantum states based on nonlinear optics. Light: Sci. Appl. 6, e17100 (2017).  
16. Jiang, W. C., Lu, X., Zhang, J., Painter, O. & Lin, Q. Silicon-chip source of bright photon pairs. Opt. Express 23, 20884-20904 (2015).  
17. Lu, X., Jiang, W. C., Zhang, J. & Lin, Q. Biphoton statistics of quantum light generated on a silicon chip. ACS Photon. 3, 1626-1636 (2016).

18. Grassani, D. et al. Micrometer-scale integrated silicon source of time-energy entangled photons. Optica 2, 88-94 (2015).  
19. Savanier, M., Kumar, R. & Mookherjea, S. Photon pair generation from compact silicon microring resonators using microwatt-level pump powers. Opt. Express 24, 3313-3328 (2016).  
20. Ramelow, S. et al. Silicon-nitride platform for narrowband entangled photon generation. Preprint at https://arXiv.org/abs/1508.04358 (2015).  
21. Jaramillo-Villegas, J. A. et al. Persistent energy-time entanglement covering multiple resonances of an on-chip biphoton frequency comb. Optica 4, 655-658 (2017).  
22. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
23. Okawachi, Y. et al. Octave-spanning frequency comb generation in a silicon nitride chip. Opt. Lett. 36, 3398-3400 (2011).  
24. Li, Q. et al. Stably accessing octave-spanning microresonator frequency combs in the soliton regime. Optica 4, 193-203 (2017).  
25. Karpov, M., Pfeiffer, M. H. P., Liu, J., Lukashchuk, A. & Kippenberg, T. J. Photonic chip-based soliton frequency combs covering the biological imaging window. Nat. Commun. 9, 1146 (2018).  
26. Kues, M. et al. On-chip generation of high-dimensional entangled quantum states and their coherent control. Nature 546, 622-626 (2017).  
27. Imany, P. et al. 50-GHz-spaced comb of high-dimensional frequency-bin entangled photons from an on-chip silicon nitride microresonator. Opt. Express 26, 1825-1840 (2018).  
28. Li, Q., Davanço, M. & Srinivasan, K. Efficient and low-noise single-photon-level frequency conversion interfaces using silicon nanophotonics. Nat. Photon. 10, 406-414 (2016).  
29. Boyd, R. W. Nonlinear Optics (Academic Press, Amsterdam, 2008).  
30. Agrawal, G. P. Nonlinear Fiber Optics (Academic Press, Amsterdam, 2007).  
31. Shah Hosseini, E., Yegnanarayanan, S., Atabaki, A. H., Soltani, M. & Adibi, A. Systematic design and fabrication of high-Q single-mode pulley-coupled planar silicon nitride microdisk resonators at visible wavelengths. Opt. Express 18, 2127-2136 (2010).  
32. Lu, X., Rogers, S., Jiang, W. C. & Lin, Q. Selective engineering of cavity resonance for frequency matching in optical parametric processes. Appl. Phys. Lett. 105, 151104 (2014).  
33. Inagaki, T., Matsuda, N., Tadanaga, O., Asobe, M. & Takesue, H. Entanglement distribution over  $300\mathrm{km}$  of fiber. Opt. Express 21, 23241-23249 (2013).  
34. Sun, Q.-C. et al. Entanglement swapping over  $100\mathrm{km}$  optical fiber with independent entangled photon-pair sources. Optica 4, 1214-1218 (2017).

# Acknowledgements

X.L., Q.L., G.M. and A.S. acknowledge support under the Cooperative Research Agreement between the University of Maryland and NIST-CNST, award number 70NANB10H193.

# Author contributions

X.L. led the design, fabrication and measurement of the entangled photon pair source devices. Q.L., A.S., G.M. and K.S. provided assistance with design and measurement. D.A.W. provided assistance with fabrication and V.A. contributed experimental tools. X.L. and K.S. wrote the manuscript. K.S. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41567-018-0394-3.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to X.L. or K.S.

Journal peer review information: Nature Physics thanks Anthony Laing and other anonymous reviewers for their contribution to the peer review of this work.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2019

# Methods

Device fabrication. The device layout was done with the Nanolithography Toolbox, a free software package developed by the NIST Center for Nanoscale Science and Technology $^{35}$ . The  $\mathrm{Si}_3\mathrm{N}_4$  layer is deposited by low-pressure chemical vapour deposition of a 500-nm-thick  $\mathrm{Si}_3\mathrm{N}_4$  layer on top of a  $3 - \mu \mathrm{m}$ -thick  $\mathrm{SiO}_2$  layer on a  $100\mathrm{mm}$  Si wafer. The wavelength-dependent refractive index and the thickness of the layers are measured using a spectroscopic ellipsometer, with the data fitted to an extended Sellmeier model. The device pattern is created in positive-tone resist by electron-beam lithography. The pattern is then transferred to  $\mathrm{Si}_3\mathrm{N}_4$  by reactive ion etching using a  $\mathrm{CF_4 / CHF_3}$  chemistry. The device is chemically cleaned to remove deposited polymer and remnant resist, and then annealed at  $1,100^{\circ}\mathrm{C}$  in a  $\mathbf{N}_2$  environment for four hours. An oxide lift-off process is performed so that the devices are with air-cladding on top but the input/output waveguides are with oxide-cladding on top. The edge of the chip is then polished for lensed-fibre coupling. After the polishing, the chip is annealed again at  $1,100^{\circ}\mathrm{C}$  in a  $\mathbf{N}_2$  environment for four hours.

In terms of the device reproducibility, the main parameter that affects the device dispersion is the ring thickness, which could be compensated by ring width and pump wavelength. Using ellipsometry and diluted hydrofluoric acid (100:1) etching, we can control the device thickness accurately (within  $5\mathrm{nm}$ ), and the fabricated devices usually have optical modes within two FSR from design in all three bands. For the details of the parameter sensitivities, please refer to Supplementary Section 2.

CAR. The peak CAR values in Fig. 5d are calculated by  $\mathrm{CAR} = (C - A) / A$ , where  $C$  and  $A$  are the overall and accidental coincidence counts extracted from the peak and background of the coincidence counting spectra (Fig. 5e, f), respectively. The one standard deviation uncertainty in CAR  $(\sigma_{\mathrm{CAR}})$  is given by  $\sigma_{\mathrm{CAR}} / \mathrm{CAR} = \sqrt{(\sigma_{\mathrm{C}} / C)^{2} + (\sigma_{A} / A)^{2}} \approx \sigma_{A} / A$ , where  $\sigma_{C}$  and  $\sigma_{A}$  are the one standard deviation uncertainties in the measured overall coincidence counts and accidental coincidence counts, respectively. The above approximation is made possible as  $\sigma_{C} / C \gg \sigma_{A} / A$ .

Entanglement visibility. The entanglement visibility is calculated by the ratios extracted from coincidence spectra in Fig. 6b-g by Visibility  $= (R_{\mathrm{max}} - R_{\mathrm{min}}) / (R_{\mathrm{max}} + R_{\mathrm{min}})$ , where the ratio is defined by  $R = \mathrm{CAR}_{\mathrm{ss},\mathrm{II}}^{\mathrm{int}} / (\mathrm{CAR}_{\mathrm{sl}}^{\mathrm{int}} + \mathrm{CAR}_{\mathrm{ls}}^{\mathrm{int}})$ .  $\mathrm{CAR}^{\mathrm{int}} = (C^{\mathrm{int}} - A^{\mathrm{int}}) / A^{\mathrm{int}}$  is the integrated CAR over a 2 ns window.  $\sigma_{\mathrm{CAR}}^{\mathrm{int}} / \mathrm{CAR}^{\mathrm{int}} \approx \sigma_{A^{\mathrm{int}}} / A^{\mathrm{int}}$ . For a perfect constructive/destructive interference, the ratio would be 2/0 theoretically.

# Data availability

The data that supports the plots within this paper and other findings of this study are available from the corresponding authors upon reasonable request.

# References

35. Coimbatore Balram, K. et al. The nanolithography toolbox. J. Res. Natl Inst. Stand. Technol. 121, 464-475 (2016).