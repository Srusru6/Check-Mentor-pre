# Observation of topologically enabled unidirectional guided resonances

https://doi.org/10.1038/s41586-020-2181-4

Received: 24 June 2019

Accepted: 22 January 2020

Published online: 22 April 2020

Check for updates

Xuefan Yin $^{1,2}$ , Jicheng Jin $^{3}$ , Marin Soljacic $^{2}$ , Chao Peng $^{1,2\boxtimes}$  & Bo Zhen $^{3}$

Unidirectional radiation is important for various optoelectronic applications, such as lasers, grating couplers and optical antennas. However, almost all existing unidirectional emitters rely on the use of materials or structures that forbid outgoing waves—that is, mirrors, which are often bulky, lossy and difficult to fabricate. Here we theoretically propose and experimentally demonstrate a class of resonances in photonic crystal slabs that radiate only towards one side of the slab, with no mirror placed on the other side. These resonances, which we name 'unidirectional guided resonances', are found to be topological in nature: they emerge when a pair of half-integer topological charges $^{1-3}$  in the polarization field bounce into each other in momentum space. We experimentally demonstrate unidirectional guided resonances in the telecommunication regime by achieving single-side radiative quality factors as high as  $1.6 \times 10^{5}$ . We further demonstrate their topological nature through far-field polarimetry measurements. Our work represents a characteristic example of applying topological principles $^{4,5}$  to control optical fields and could lead to energy-efficient grating couplers and antennas for light detection and ranging.

Topological defects<sup>1</sup>, which are characterized by quantized invariants, offer a general description of many exotic phenomena in real space, such as quantum vortices in superfluids and singular optical beams<sup>3</sup>. It has been recently found that topological defects can also emerge in momentum space, giving rise to interesting effects. One such example is bound states in the continuum<sup>6</sup> (BICs) in photonic crystal slabs: these guided resonances reside inside the continuous spectrum of extended radiating modes, yet counter-intuitively remain spatially confined and maintain infinitely long lifetimes. Since they were initially proposed<sup>7</sup>, BICs have been demonstrated in a variety of wave systems<sup>8-20</sup> and have led to various applications<sup>21,22</sup>. Recently, the topological defect nature of BICs in photonic crystal slabs was discovered: BICs are vortices of polarization major axes in momentum space that carry integer topological charges<sup>2,23-25</sup>. The lack of a continuous definition of polarization at the vortex centre forbids the emission of far-field radiation from BICs. So far, most BICs have been demonstrated in up-down mirror-symmetric structures<sup>11,13,26</sup>, in which the observation of no upward radiation necessitates the absence of downward radiation. On the other hand, the existence of unidirectional guided resonances (UGRs)—resonances that radiate only towards one side of a photonic crystal slab, with no mirror placed on the other side—has not been confirmed so far<sup>27,28</sup>.

Here we theoretically propose and experimentally demonstrate UGRs in photonic crystal slabs that are enabled by topological charges. Specifically, we first split the integer topological charge carried by a BIC into a pair of half-integer topological charges $^{29}$ ; each charge corresponds to a circularly polarized resonance. As the structure is continuously varied, the two half-integer topological charges in the downward radiation keep evolving in momentum space until they bounce into each other and, again, act as an integer charge. At this point, downward radiation from

this resonance is disallowed because its far-field polarization is again undefined—this is the topological origin of UGRs. Because up-down mirror symmetry is broken, the UGRs can still radiate towards the top side, unlike traditional  $\mathrm{BICs}^6$ , making them potentially useful as low-loss grating couplers to efficiently couple light both on and off chips.

# Numerical design and topological interpretation

As a specific example, we consider a one-dimensional periodic photonic crystal slab in which infinitely long bars with gaps of width  $w = 358$  nm are defined in a 500-nm-thick silicon layer with refractive index of  $n = 3.48$  at a periodicity of  $a = 772$  nm (Fig. 1a-d). Both the top and bottom silica cladding layers ( $n = 1.46$ ) are assumed to be semi-inferently thick. When the sidewalls of the bars are vertical ( $\theta = 90^\circ$ ; Fig. 1b), the photonic crystal slab is up-down and left-right symmetric, and a BIC is found on a transverse electric (TE)-like band (TE1) along the  $k_x$  axis off the normal direction at  $k_x a / (2\pi) = 0.176$ . In this up-down-symmetric structure, the radiative decay rate of a mode towards the top ( $\gamma_{\mathrm{c}}$ ; orange) of the photonic crystal slab is always the same as that towards the bottom ( $\gamma_{\mathrm{b}}$ ; blue), and both rates are reduced to 0 at the BIC (middle panels, Fig. 1b). Fundamentally, this BIC is a topological defect in the far-field polarization major axes that carries an integer topological charge of  $q = 1$ , defined as:

$$
q = \oint_ {C} \mathrm {d} \mathbf {k} \cdot \nabla_ {\mathbf {k}} \phi (\mathbf {k}) \tag {1}
$$

Here  $\phi (\mathbf{k})$  is the angle between polarization major axis and the  $x$  axis and  $\mathbf{k}$  is the in-plane wave vector.  $C$  is a yellow closed path in Fig. 1b, which goes around the BIC in the counter-clockwise direction.

![](images/56bbd74e2fb8ee5c28e5443b1847e6b3df9ed2c3bcc9b81620aaabd1fdf11bce.jpg)  
a

![](images/aa0fbd68f2201adc58ff93137b158d3bc6afb3c677bca4ca73cfd25d27e18e30.jpg)

![](images/89e745906eadcb86df07f0407d3b76b36bf8d6a4a55f6d4ca8ecf6a6b9d1a685.jpg)  
b

![](images/28557fbf3afb7a759dd932e47f5027c400b28000ef0cf9bc13b822ef96e8041b.jpg)  
C

![](images/a69c72f2d30485431da18bc18e52de5031ab051e14c341c964affd7c13a4ffe6.jpg)  
d

![](images/d6bb39754aaa13f249744090456cefaec060bc0ea4fed42dcf3d7f5dd8cb1e04.jpg)  
e  
Fig.1|UGRs and their topological nature. a, Schematic of a photonic crystal slab supporting a unidirectional guided resonance (UGR). When the sidewall is vertical, a BIC is found on a TE band, labelled by red circles in the right panels.  $Q_{\mathrm{r}}$  accounts for radiative loss towards both top and bottom,  $Q_{\mathrm{r}} = \omega / (\gamma_{\mathrm{t}} + \gamma_{\mathrm{b}})$ . b, When the sidewall is vertical, radiative losses from resonances towards the top ( $\gamma_{\mathrm{t}}$ ; orange line) are equal to those towards the bottom ( $\gamma_{\mathrm{b}}$ ; blue line) owing to up-down symmetry, and both reduce to 0 at the BIC. The polarization major axes wind around the BIC and have a topological charge of  $q = 1$ . c, When the sidewall is tilted from the vertical direction, the  $q = 1$  topological charge splits into a pair of half charges ( $q = 1/2$ ) with opposite helicities, LCP (red) and RCP (green). d, When the sidewall angle  $\theta$  changes to  $75^{\circ}$ , a UGR is achieved: radiation towards the bottom is eliminated ( $\gamma_{\mathrm{b}} = 0$ ) while radiation emitted towards the top ( $\gamma_{\mathrm{t}}$ ) remains finite. e, Trajectories traced by the two half charges (red and green) in momentum space as  $\theta$  is varied.

When one of the sidewalls is tilted away from the vertical direction  $(\theta = 81^{\circ}$ ; Fig. 1c), the photonic crystal slab is no longer up-down symmetric, and  $\gamma_{\mathrm{t}}$  and  $\gamma_{\mathrm{b}}$  are no longer simply related. No BIC exists in this structure any more; the radiative decay rate towards the top or the bottom  $(\gamma_{\mathrm{t,b}})$  never reaches 0 (middle panel). On the other hand, the total winding of the polarization major axes remains  $+2\pi$  because the winding number is a conserved quantity. Consequently, the integer charge  $q = 1$  is split into two half-integer charges of  $q = 1/2$ , each being

![](images/960d985fac27cf5132b8dc52db130ec4c349cc426a53eafaefd7793268cbb91b.jpg)  
a

![](images/ea6c38a36afec1ce4ec57e0b6a7c090eb6afbc45ef9e31f3a02f09ceecbaefa3.jpg)  
b

![](images/ae27f0523d0a547ecf5006095812a3723a4670d64f3a0599ebc535cbb2adb5be.jpg)  
Fig. 2 | Numerical confirmation of a UGR. a, Unit cell design of a photonic crystal slab supporting a UGR that only radiates towards the top, as shown in its mode profile  $(E_{y})$ . a.u., arbitrary units. b, c, Colour map (b) and line cut (c) showing that the asymmetry ratio between upward and downward radiative loss,  $\eta = \gamma_{\mathrm{t}} / \gamma_{\mathrm{b}}$ , diverges to infinity at the UGR. The polarization major axes (arrows) show a  $+2\pi$  winding around the UGR, which is consistent with Fig. 1d.  
C

a circularly polarized resonance (bottom panel). The two half-integer charges are related to each other by the  $y$ -mirror symmetry of the structure, which also guarantees that these two circularly polarized resonances are opposite in helicity: left-handed circularly polarized (LCP) for one (red) and right-handed circularly polarized (RCP) for the other (green).

When the sidewall is further tilted, the two half-integer charges in the downward radiation keep moving in momentum space, following the trajectories shown in Fig. 1e: red for LCP and green for RCP. Neither of the radiative decay rates  $(\gamma_{\mathrm{t,b}})$  is reduced to 0 until  $\theta$  is decreased to  $75^{\circ}$  (Fig. 1d), where the LCP and RCP trajectories meet on the  $k_{x}$  axis. At this point, any downward radiation needs to be both LCP and RCP at the same time, which can never be satisfied. As a result, this guided resonance cannot have any downward radiation, even without a mirror on the bottom—this is what we call a UGR. From the viewpoint of topology, UGRs can be understood as the merging point between two half-integer charges, where they act like an integer charge, forbidding any radiative loss. This topological interpretation agrees with our numerical simulation results, where  $\gamma_{\mathrm{b}}$  reaches 0 whereas  $\gamma_{\mathrm{t}}$  remains finite (middle panel of Fig. 1d). We note that the lack of certain symmetries in our structure (both  $C_2$  and up-down mirror) is crucial to achieve UGRs; see Supplementary Information sections 1-3 for more details.

Next, we present our UGR design (Fig. 2a). The photonic crystal slab consists of a periodic array of one-dimensional bars defined in a 500-nm-thick silicon-on-insulator wafer at a periodicity of  $a = 825\mathrm{nm}$  (left panel). The top cladding material is air and the bottom cladding is  $\mathrm{SiO}_2$ . The sidewalls are tilted to specific angles,  $\theta_{\mathrm{L}} = 79^{\circ}$  and  $\theta_{\mathrm{R}} = 75^{\circ}$ , to achieve a UGR: as shown in the  $E_{y}$  mode profile (right panel), the downward radiation  $\gamma_{\mathrm{b}}$  is considerably lower, by more than 70 dB, than the upward radiation  $\gamma_{\mathrm{r}}$ . The asymmetry ratio between upward and downward radiation intensity,  $\eta = \gamma_{\mathrm{c}} / \gamma_{\mathrm{b}}$ , is calculated for different  $k$  points (colour map, Fig. 2b), where the extremely bright spot marks the location of the UGR at  $k_{x}a / (2\pi) = 0.0854$ . A line-cut of the colour map along the  $k_{x}$  axis shows the asymmetry ratio  $\eta$  diverging into infinity, which is the characteristic feature of unidirectional radiation (Fig. 2c).

![](images/a55f111164e112a18a142e1b6f090f166be3afeace3474a9f544fd7a3c2d0509.jpg)  
a

![](images/6a1cf15611f00c21fbd165bc80202e7b8d515f3aeb26be182bd22381d31c0f74.jpg)  
b

![](images/97eedf929f7f2529b94e6b9193d8417ab96dab923a5e2415db8d8d2a156f3009.jpg)  
C  
Fig. 3 | Fabricated sample and experimental setup. a, b Scanning electron microscope images of the fabricated photonic crystal sample from tilted (a) and side (b) views. c, Schematic of the setup used to independently measure  
the upward and downward radiation intensities from the guided resonances in the photonic crystal sample. L, lens; Obj, objective; RFP, rear focal plane; PD, photodetector; POL, polarizer; BS, beam splitter; 4f, relay 4f optical system.

Overlaid on the colour map in Fig. 2b is the plot of the polarization major axes for the downward far-field radiation from nearby resonances. An integer winding of the polarization major axes,  $q = 1$ , is observed around the UGR, which is consistent with the topological interpretation presented in Fig. 1d.

# Sample fabrication and experimental setup

To verify our theoretical findings, we fabricate photonic crystal samples with UGRs using plasma-enhanced chemical vapour deposition, electron-beam lithography and reactive ion etching (RIE) processes. The scanning electron microscope images are shown in Fig. 3a, b. Briefly, a thermal  $\mathrm{SiO}_2$  layer with a thickness of approximately  $110\mathrm{nm}$  is first deposited on the wafer as the hard mask. Unlike standard RIE processes that use horizontal substrates, our sample is placed on a wedged substrate that allows us to etch the silicon layer at a slanted angle; as a result, high-quality air gaps with tilted sidewalls are achieved (Fig. 3b). Because of the shadowing effect, the angles of the left and right sidewalls are not identical:  $\theta_{\mathrm{L}} = 79^{\circ}$  and  $\theta_{\mathrm{R}} = 75^{\circ}$ . The width of the air gap,  $w$ , is swept from  $320\mathrm{nm}$  to  $340\mathrm{nm}$  to best capture the UGR design at  $w = 331\mathrm{nm}$ . See Methods for more details about the fabrication.

To demonstrate UGRs, the upward and downward radiative decay rates from our fabricated samples are independently characterized using the experimental setup schematically shown in Fig. 3c. A tunable telecommunication laser in the  $\mathrm{C + L}$  band is first sent through a polarizer in the  $x$  direction before it is focused by a lens (L1) onto the rear focal plane of an infinity-corrected objective lens. To achieve on-resonance coupling, the incident angle is tuned for each excitation wavelength  $\lambda$  by moving L1 in the  $x - y$  plane, exciting a resonance in the sample. Each excited resonance radiates towards the top (bottom) according to its radiative decay rate  $\gamma_{\mathrm{t}}(\gamma_{\mathrm{b}})$  into this channel. Upward (downward) far-field radiation from this resonance is then collected by the confocal setup shown on the right (left), marked with a orange (blue) dashed box, where the beam is shrunk by 0.67 times through a 4f system to best fit the camera. This on-resonance excitation scheme is similar to previously reported results[30,31]. See Methods for more details on the experimental setup.

# Experimental results

As an example, the experimental comparison between upward and downward radiation from a resonance at  $\lambda = 1,551\mathrm{nm}$  is shown in Fig.4a.

Here, the excitation laser is on resonance with a mode on the  $k_{y}$  axis at  $k_{y}a / (2\pi) = 0.01$ . Momentum space is labelled with respect to the known numerical aperture of the objectives (NA = 0.26), shown as white circles. The characteristic feature of the UGR - marked by a white arrow on the  $k_{x}$  axis - is qualitatively shown in the comparison between the two figures: for resonances near the white arrow, the downward radiation  $(X', Y', Z')$  is always much weaker than the upward radiation  $(X, Y, Z)$ . On the other hand, for resonances far from the UGRs (for example, to the left of the  $k_{y}$  axis), the upward and downward radiation are comparable. We note that although UGRs radiate only towards a single side (top), their in-plane propagation is not immune to back-scattering from fabrication disorder such as the chiral edge states in a Chern insulator, because our structure is reciprocal.

A more quantitative demonstration of the UGRs is achieved by measuring the up-down asymmetry ratio  $\eta = \gamma_{\mathrm{t}} / \gamma_{\mathrm{b}}$  of the resonances. Two movable pinholes (not shown in Fig. 3c) with diameters of  $300\mu \mathrm{m}$  are placed at the image planes of the rear focal planes of the objectives to select specific  $k$  points. Three examples are shown in Fig. 4b, where upward  $(X,Y,Z)$  and downward  $(X^{\prime},Y^{\prime},Z^{\prime})$  radiation intensities are measured by two photodetectors as the excitation wavelength scans through the three resonances. As expected, all measured spectra exhibit symmetric Lorentzian features<sup>30</sup>: the excitation efficiency reaches its maximum when the excitation is on resonance, which happens at  $\lambda = 1,553.7\mathrm{nm}$ ,  $1,551.2\mathrm{nm}$  and  $1,549.4\mathrm{nm}$ . Accordingly, both the central wavelengths and the total quality factors of the resonances can be extracted by fitting the experimental results. By repeating this procedure for all resonances along the  $X - Z$  line, we achieve good agreement between experiments (red crosses) and numerical simulation (blue line, Fig. 4c).

We further measure the downward radiative decay rate of the resonances,  $\gamma_{\mathrm{b}} = \omega /Q_{\mathrm{b}}$  and show that it is reduced to 0 at the UGR. Here,  $\omega$  is the resonance frequency and  $Q_{\mathrm{b}}$  is the radiative quality factor that accounts only for the downward radiation. In practice, the observed total loss  $\gamma_{\mathrm{tot}} = \omega /Q_{\mathrm{tot}}$  is composed of non-radiative loss  $\gamma_{\mathrm{non - rad}} = \omega /Q_{\mathrm{non - rad}}$  (including absorption, scattering, and lateral leakage), as well as radiative losses towards the top and bottom:

$$
\gamma_ {\mathrm {t o t}} = \gamma_ {\mathrm {n o n - r a d}} + \gamma_ {\mathrm {t}} + \gamma_ {\mathrm {b}} \tag {2}
$$

Because these resonances are close in momentum space and share similar mode profiles, it is reasonable to assume that they share a similar non-radiative quality factor, which is found to be  $Q_{\mathrm{non - rad}} = 2,080$  through

![](images/c402cb178ceb89cb77581ac1b84a58433a10bcdb217b8f7c90565e4e58ae0673.jpg)  
Fig. 4 | Observation of UGRs. a, Upward and downward radiation intensities from resonances under an excitation wavelength of  $1,551\mathrm{nm}$ . In the vicinity of the UGR on the  $k_{x}$  axis, marked by a white arrow, the downward radiation intensities  $(X', Y', Z')$  are considerably suppressed compared to the upward

![](images/2112a19290c6a55b938ac04b5e30437708860322868de6fbe2b6c41bc4b58356.jpg)  
radiation  $(X,Y,Z)$ . b, Upward and downward radiation intensities from the resonances as the excitation wavelength scans from 1,535 nm to 1,565 nm. c, d, Experimental results (red crosses) of the band structure (c) and  $Q_{\mathrm{b}}(\mathbf{d})$  showing good agreement with the simulation results (blue lines).

![](images/2ea575df26ba7af8a342475f4b8b55a73d97765502607cc7c82100ce76da2380.jpg)

![](images/eec29511674de67430ed882f9528f78a28678c5a15be6d60758db280a9e36124.jpg)

numerical fitting (see Methods for details). Upward and downward radiative decay rates can be further separated based on the measured asymmetry ratio  $\eta = \gamma_{\mathrm{t}} / \gamma_{\mathrm{b}}$  (see Extended Data Fig. 3 for measurement results of  $\eta$ ). Experimentally extracted  $Q_{\mathrm{b}}$  values are presented in Fig. 4c as red crosses, showing good agreement with the numerical simulation results (blue line). In particular, the fact that the bottom radiation  $\gamma_{\mathrm{b}}$  is reduced to almost 0 at  $k_{x}a / (2\pi) = 0.088$  proves the existence of UGR.

To demonstrate the topological nature of UGRs, we perform polarimetry measurements $^{31}$  on a series of five samples with slightly different widths  $w$ . For each sample, we experimentally locate the two half-integer charges in momentum space (symbols in Fig. 5a), which show good agreement with the simulation results (dashed lines). See Methods for more experimental details of the polarimetry measurements. The perfect design with a UGR is marked with an arrow. As shown, when  $w$  increases from  $0.399a$  (marked by inverted triangles) to  $0.403a$  (diamonds), the two half-integer charges switch positions.

![](images/b341c3d571501ee92bf057465b1d380b8ac2b857c315d73b21cf2ec7c140f018.jpg)  
Fig. 5 | Observation of the topological nature of UGRs. a, Experimentally measured trajectories of half-integer charges from five samples with different widths  $w$  (symbols), showing good agreement with simulation results (dashed lines). b, c, The LCP and RCP resonances switch positions as  $w$  increases from  $0.4a$  (b) to  $0.403a$  (c), with the merging point being the UGR. The colour map shows the measured ellipticity of the downward radiation fields.

This switching behaviour is further confirmed by measuring the ellipticity  $\rho$  of the far-field polarization: when  $w$  increases from 0.4a (Fig. 5b) to 0.403a (Fig. 5c), the LCP (RCP) resonance, shown in red (green), moves from the top (bottom) to the bottom (top) half of the momentum space. Taken together, these experimental results confirm our topological interpretation shown in Fig. 1d: UGRs arise when two half-integer charges with opposite helicities bounce into each other in momentum space.

To summarize, we present a type of resonance, which we call UGR, that radiates only towards the top of a photonic crystal slab, even without a bottom mirror. We experimentally demonstrate their existence by showing that the downward radiation field vanishes. Through polarimetry measurements, we further demonstrate the topological nature of these resonances as the merging point between half-integer topological charges. Owing to their unique properties, UGRs could be used as energy-efficient grating couplers (see Methods for discussion) with further applications in photonic-crystal surface-emitting lasers, light detection and ranging antennas.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-020-2181-4.

1. Mermin, N. D. The topological theory of defects in ordered media. Rev. Mod. Phys. 51, 591-648 (1979).  
2. Zhen, B., Hsu, C.W., Lu, L., Stone, A. D. & Soljačić, M. Topological nature of optical bound states in the continuum. Phys. Rev. Lett. 113, 257401 (2014).  
3. Gbur, G. J. Singular Optics (CRC Press, 2016).  
4. Lu, L., Joannopoulos, J. D. & Soljai, M. Topological photonics. Nat. Photon. 8, 821-829 (2014).  
5. Ozawa, T. et al. Topological photonics. Rev. Mod. Phys. 91, 015006 (2019).  
6. Hsu, C.W., Zhen, B., Stone, A.D., Joannopoulos, J.D. & Soljacic, M. Bound states in the continuum. Nat. Rev. Mater. 1, 16048 (2016).  
7. von Neuman, J. & Wigner, E. Über merkwürdige diskrete Eigenwerte. Über das Verhalten von Eigenwerten bei adiabatischen Prozessen. Phys. Z. 30, 467-470 (1929).  
8. Friedrich, H. & Wintgen, D. Interfering resonances and bound states in the continuum. Phys. Rev. A 32, 3231-3242 (1985).

9. Fan, S. & Joannopoulos, J. D. Analysis of guided resonances in photonic crystal slabs. Phys. Rev. B 65, 235112 (2002).  
10. Plotnik, Y. et al. Experimental observation of optical bound states in the continuum. Phys. Rev. Lett. 107, 183901 (2011).  
11. Hsu, C. W. et al. Observation of trapped light within the radiation continuum. Nature 499, 188-191 (2013).  
12. Corrielli, G., Della Valle, G., Crespi, A., Osellame, R. & Longhi, S. Observation of surface states with algebraic localization. Phys. Rev. Lett. 111, 220403 (2013).  
13. Kodigala, A. et al. Lasing action from photonic bound states in continuum. Nature 541, 196-199 (2017).  
14. Gomis-Bresco, J., Artigas, D. & Torner, L. Anisotropy-induced photonic bound states in the continuum. Nat. Photon. 11, 232-236 (2017).  
15. Molina, M. I., Miroshnichenko, A. E. & Kivshar, Y. S. Surface bound states in the continuum. Phys. Rev. Lett. 108, 070401 (2012).  
16. Carletti, L., Koshelev, K., De Angelis, C. & Kivshar, Y. Giant nonlinear response at the nanoscale driven by bound states in the continuum. Phys. Rev. Lett. 121, 033903 (2018).  
17. Monticone, F. & Alu, A. Embedded photonic eigenvalues in 3D nanostructures. Phys. Rev. Lett. 112, 213903 (2014).  
18. Liu, Z. et al. High-Q quasibound states in the continuum for nonlinear metasurfaces. Phys. Rev. Lett. 123, 253901 (2019).  
19. Lim, T. C. & Farnell, G. W. Character of pseudo surface waves on anisotropic crystals. J. Acoust. Soc. Am. 45, 845-851 (1969).  
20. Cobelli, P. J., Pagneux, V., Maurel, A. & Petitjeans, P. Experimental observation of trapped modes in a water wave channel. Europhys. Lett. 88, 20006 (2009).  
21. Hirose, K. et al. Watt-class high-power, high-beam-quality photonic-crystal lasers. Nat. Photon. 8, 406 (2014).

22. Chow, E., Grot, A., Mirkarimi, L. W., Sigalias, M. & Girolami, G. Ultracompact biochemical sensor built with two-dimensional photonic crystal microcavity. Opt. Lett. 29, 1093-1095 (2004).  
23. Bulgakov, E. N. & Maksimov, D. N. Topological bound states in the continuum in arrays of dielectric spheres. Phys. Rev. Lett. 118, 267401 (2017).  
24. Zhang, Y. et al. Observation of polarization vortices in momentum space. Phys. Rev. Lett. 120, 186103 (2018).  
25. Doeleman, H. M., Monticone, F., den Hollander, W., Andrea, A. & Koenderink, A. F. Experimental observation of a polarization vortex at an optical bound state in the continuum. Nat. Photon. 12, 397-401 (2018).  
26. Yang, Y., Peng, C., Liang, Y., Li, Z. & Noda, S. Analytical perspective for bound states in the continuum in photonic crystal slabs. Phys. Rev. Lett. 113, 037401 (2014).  
27. Zhou, H. et al. Perfect single-sided radiation and absorption without mirrors. Optica 3, 1079-1086 (2016).  
28. Wang, K. X., Yu, Z., Sandhu, S. & Fan, S. Fundamental bounds on decay rates in asymmetric single-mode optical resonators. Opt. Lett. 38, 100-102 (2013).  
29. Liu, W. et al. Circularly polarized states spawning from bound states in the continuum. Phys. Rev. Lett. 123, 116104 (2019).  
30. Jin, J. et al. Topologically enabled ultrahigh-Q guided resonances robust to out-of-plane scattering. Nature 574, 501-504 (2019).  
31. Zhou, H. et al. Observation of bulk Fermi arc and polarization half charge from paired exceptional points. Science 359, 1009-1012 (2018).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2020

# Article

# Methods

# Numerical simulation details

All simulations are performed using the COMSOL Multiphysics 5.2 'Radio Frequency' module in the frequency domain. Two-dimensional models (in the  $x - y$  plane) are created to simulate one-dimensional photonic crystal slabs with perfectly matching layers along the  $y$  direction. Periodic (Floquet) boundary conditions are applied in the  $x$  direction. The meshing resolution is set to adequately capture resonances with  $Q$  values of up to  $10^{9}$ . The eigenvalue solver is used to calculate the band structures and quality factors. To calculate the asymmetric radiation ratios  $\eta$ , two surface probes—one above and one below the structure—are used to calculate the radiative fields towards both sides.

# Sample fabrication

The sample is fabricated on a single-side polished silicon-on-insulator wafer with a silicon layer thickness of  $500\mathrm{nm}$ , a silica layer of  $2\mu \mathrm{m}$  and a silicon substrate of  $\sim 725\mu \mathrm{m}$ . The step-by-step fabrication process is illustrated in Extended Data Fig. 1a. The wafer is first cleaved into  $1\mathrm{cm} \times 1\mathrm{cm}$  chips and cleaned. The photonic crystal pattern is then defined using electron-beam lithography. A  $110\mathrm{-nm}$ -thick  $\mathrm{SiO}_2$  film is thermally deposited using plasma-enhanced chemical vapour deposition as the hard mask. A layer of ZEP520A photo-resist (340 nm thick) is spin-coated on the  $\mathrm{SiO}_2$  layer. The photonic crystal patterns are defined in the photo-resist layer (Elionix FLS-125), which is then developed using o-xylene ( $>95\%$ ). The chip is then placed on a customized wedged holder made of  $\mathrm{Al}_{2}\mathrm{O}_{3}$  with a slanted angle of  $26^{\circ}$  for RIE. The photonic crystal patterns are first transferred onto the  $\mathrm{SiO}_2$  hard mask using  $\mathrm{CF}_4$ , and are then transferred onto Si using  $\mathrm{Cl}_2$  gas. The residue hard mask is removed using BHF wet etching. Finally, the bottom side is treated with chemical-mechanical polishing for the measurements of the bottom radiation fields. The size of the sample is  $500\mu \mathrm{m} \times 500\mu \mathrm{m}$ . Owing to the shadowing effect, the tilt angles of the two sidewalls are not identical, as illustrated in Extended Data Fig. 1b. To best capture the UGR design at  $w = 331\mathrm{nm}$ , the width of the air gap is varied from  $320\mathrm{nm}$  to  $340\mathrm{nm}$ .

# Measurement of asymmetry ratio  $\eta$  and single-side quality factors

As illustrated in Extended Data Fig. 2, a  $x$ -polarized tunable telecommunication laser (Santec TSL-550, C+L band) is sent through a chopper for lock-in detection and is focused by a lens (L1) onto the rear focal plane of the objective to define the excitation angle. Two identical arms are used to measure the two radiation fields from the top and the bottom. In each arm, a two-stage 4f system is used to adjust the magnification ratio. After passing through an orthogonal polarizer in the  $y$  direction, the radiation field is collected using a photodetector and a camera. To measure radiation fields from resonances from a specific  $k$  point, two movable pin holes with diameters of  $300~{\mu\mathrm{m}}$  are placed at the Fourier planes to select the desired  $k$  point. Upward and downward radiation fields go through two identical pin holes and are then measured using two identical photodetectors (PDA10DT-EC). Each photodetector is connected to a lock-in amplifier (SRS SR830). A flip mirror is used to switch between the camera that images the light-scattering patterns and the photodetector.

A 'cross-polarization filtering' technique is used to suppress unwanted reflections, similarly to some previous works[32,33]. Specifically, unwanted reflections (caused by lenses or other optical surfaces) mostly maintain the incident polarization, whereas most radiation fields from guided resonances do not. By placing two orthogonal polarizers in the optical path along the  $x$  axis (for excitation) and  $y$  axis (for observation), unwanted reflection is greatly suppressed. This setup also transforms typical asymmetric Fano lineshapes into nearly symmetric Lorentzian lineshapes. An 'on-resonance pumping' technique is also used in the setup, similarly to previous works[34]. As the photonic

crystal structure shows little dispersion along  $k_{y}$  but strong dispersion along  $k_{x}$ , the scattering patterns are almost straight lines parallel to the  $x$  axis.

The central wavelengths (Fig. 4c) and total quality factors ( $Q_{\mathrm{tot}}$ ; Extended Data Fig. 3a) of the guided resonances are extracted by numerically fitting the measured spectra; examples are shown in Fig. 4b. As both upward and downward radiation fields are measured in our setup, the ratio between upward and downward decay rate,  $\eta$ , is achieved directly. The observed total quality factor  $Q_{\mathrm{tot}}$  includes contributions from: (1) non-radiative losses due to material absorption, scattering from surface roughness and in-plane lateral leakage and (2) radiative losses due to upward and downward radiation. This relationship can be written as:

$$
\frac {1}{Q _ {\text {t o t}}} = \frac {1}{Q _ {\text {n o n - r a d}}} + \frac {1}{Q _ {\mathrm {r}}} \tag {3}
$$

The radiative losses can be further separated into top and bottom channels:  $1 / Q_{\mathrm{r}} = 1 / Q_{\mathrm{t}} + 1 / Q_{\mathrm{b}}$ . As shown in Extended Data Fig. 3a, by comparing the measured  $Q_{\mathrm{tot}}$  (blue crosses) to the calculated radiative quality factors from an ideal unidirectional design (red line),  $Q_{\mathrm{non - rad}} = 2,080$  is extracted. By design,  $Q_{\mathrm{non - rad}}$  is much larger than  $Q_{\mathrm{r}}$  (200 to 600), so the energy loss is dominated by radiation. Furthermore, the simulation results from disordered designs (green circles) are presented as a reference, where the air-gap locations and widths fluctuate with a standard deviation of  $1\mathrm{nm}$ . Using the measured asymmetry ratio  $\eta = \gamma_{\mathrm{t}} / \gamma_{\mathrm{b}} = Q_{\mathrm{b}} / Q_{\mathrm{t}}$ , equation (3) can be written as

$$
\frac {1}{Q _ {\mathrm {t o t}}} = \frac {1}{Q _ {\mathrm {n o n - r a d}}} + \frac {\eta + 1}{Q _ {\mathrm {b}}} \tag {4}
$$

Using this relationship, the single-side quality factors  $Q_{\mathrm{b}}$  can be calculated accordingly.

# Polarimetry measurement setup

To demonstrate the topological nature of UGRs, we perform polarimetry measurements on the downward radiation fields. The experimental setup is schematically shown in Extended Data Fig. 4. Unlike the previous setup, which uses a continuous-wave tunable laser, this setup uses a broadband amplified spontaneous emission light source with a centre wavelength of  $1,550\mathrm{nm}$ , a bandwidth of  $40\mathrm{nm}$  and an output power of  $10\mathrm{dBm}$ . The incident light excites the sample along the  $k_{y}$  axis, and the incident angle is varied between  $-1.3^{\circ}$  and  $1.3^{\circ}$  at a step size of  $0.3^{\circ}$ , which is controlled by lens L1. Owing to the broad bandwidth of the excitation, all resonances at a given incident angle are excited.

A standard polarimetry measurement is then performed on the scattered light to determine the polarization state of each resonance. Specifically, the scattered light intensity is measured after passing through six configurations of a polarizer and a quarter-wave plate (QWP): (1) no QWP, polarizer oriented along the  $x$  axis; (2) no QWP, polarizer along the  $y$  axis; (3) no QWP, polarizer at  $45^{\circ}$  with respect to the  $x$  axis; (4) no QWP, polarizer at  $135^{\circ}$  with respect to the  $x$  axis; (5) QWP fast axis at  $45^{\circ}$  with respect to the  $x$  axis, polarizer along the  $y$  axis; (6) QWP fast axis at  $135^{\circ}$  with respect to the  $x$  axis, polarizer along the  $y$  axis. This set of measurements allows us to fully reconstruct the polarization state of each resonance<sup>35</sup> through the Stokes parameters:

$$
S _ {0} = \left| E _ {x} \right| ^ {2} + \left| E _ {y} \right| ^ {2}
$$

$$
S _ {1} = \left| E _ {y} \right| ^ {2} - \left| E _ {x} \right| ^ {2} \tag {5}
$$

$$
S _ {2} = 2 \left| E _ {y} E _ {x} \right| \cos (\Delta \delta)
$$

$$
S _ {3} = 2 \left| E _ {y} E _ {x} \right| \sin (\Delta \delta)
$$

Here,  $\mathbf{E} = E_{x}\mathrm{e}^{\mathrm{i}\omega t}\hat{\mathbf{e}}_{x} + E_{y}\mathrm{e}^{\mathrm{i}\omega t + \Delta \delta}\hat{\mathbf{e}}_{y}$ . Specifically, the ellipticity  $\rho = S_3 / S_0$  is maximized (+1) or minimized (-1) when  $|E_x| = |E_y|$  and  $\Delta \delta = \pm \pi /2$ , which correspond to the LCP and RCP resonances, respectively. This allows us to locate the half-integer topological charges  $q = \pm 1 / 2$  in momentum space by measuring the maximum and minimum ellipticity  $\rho$  of the scattered light.

The ellipticity measurement results for five samples are shown in Extended Data Fig. 5. All samples share the same design, except for the air-gap width  $w$ , which varies between  $0.399a$  (Extended Data Fig. 5a) and  $0.403a$  (Extended Data Fig. 5e). As  $w/a$  is varied, the two half-integer charges (with opposite ellipticities) approach and bounce into each other before they move apart. The transition point corresponds to the UGR design, which is confirmed by the switching of the ellipticity before and after the transition; namely, LCP (RCP) is initially in the top (bottom) half plane, as in Extended Data Fig. 5a, and moves to the bottom (top) at the end, as in Extended Data Fig. 5e. These experimental results are in good agreement with the simulation results (Supplementary Fig. 4) and with our topological interpretation presented in Fig. 1e.

# Robustness of the UGRs to fabrication errors

In practice, fabricated samples inevitably deviate from their designs because of fabrication errors or imperfections. Here we analyse the factors limiting the performance of UGRs in realistic samples. The periodicity of photonic crystal is limited by the accuracy of the electron-beam lithography; however, this is often not the limiting factor. In comparison, it is more challenging to fabricate the air gaps (both width and tilt angles) exactly as designed, owing to the accuracy of the etching processes. First, we assume that the fabricated sample deviates steadily from the ideal design ( $a = 825 \mathrm{~nm}$ ,  $w = 352 \mathrm{~nm}$ ,  $\theta_{\mathrm{L}} = 79^{\circ}$ ,  $\theta_{\mathrm{R}} = 75^{\circ}$ ) in terms of (1) air-gap width,  $\Delta w = \pm 2.5 \mathrm{~nm}$  and (2) sidewall angle,  $\Delta \theta = \pm 1^{\circ}$ . The simulation results in Extended Data Fig. 6a, b confirm that when the parameters are slightly different from the ideal design, the asymmetry ratio remains high, as expected. Furthermore, owing to the topological nature of UGRs, a fixed deviation in one parameter can be compensated by another parameter to restore the perfect elimination of downward radiation fields. For example, as shown in Extended Data Fig. 6c, a change of  $\Delta \theta = -1^{\circ}$  in the etching angle can be compensated by changing the air-gap width from  $w = 352 \mathrm{~nm}$  to  $w = 365 \mathrm{~nm}$ , where the UGR is restored.

Meanwhile, random fluctuations are also inevitable in fabricated samples and they induce scattering losses and lower the asymmetry ratios. In this part of the analysis, we assume that the tilted angles are fixed while the air-gap locations and widths fluctuate randomly from the ideal design with a standard deviation of  $1\mathrm{nm}$ , which is estimated from the scanning electron microscope images. The average  $Q_{\mathrm{tot}}$  and asymmetry ratios for disordered samples are obtained from simulations, which are compared with the ideal design and the experimental results, as shown in Extended Data Fig. 3b.  $Q_{\mathrm{tot}}$  drops owing to scattering losses. The asymmetry ratio is reduced to approximately 50 dB at its peak (from 70 dB) but remains higher than 35 dB in the vicinity of the UGR, demonstrating that our design is robust to fabrication errors and uncertainties. The 'cross-polarization filtering' technique also allows us to measure the asymmetry ratio for any  $k$  points. As confirmed by simulation and experimental results (Extended Data Fig. 7), the asymmetry ratios remain higher than 35 dB as the excitation deviates from  $k_y = 0$  to  $k_ya / (2\pi) = 0.06$ . This provides a  $6^{\circ}$  tolerance in the polishing angle of the angled fibre couplers, which is reasonable in practice.

# Prospects of using UGRs as grating couplers

Highly directional radiation is desirable in on-chip optoelectronic devices such as lasers, LIDAR antennas and grating couplers. Although grating couplers having been studied extensively, their performances are still not optimal, with one major challenge arising from unwanted

downward radiation losses towards the handle wafer side $^{36,37}$ . Several mechanisms have been proposed to achieve highly directional radiation, including non-resonant blazed gratings and resonance-based dual-layer gratings. Some relevant works $^{36,38-44}$  are listed in Extended Data Table1 for a comparison with our work, which is based on topology. The measured asymmetry ratio reaches a maximum of 27.7 dB; namely,  $99.8\%$  of the radiation field is upward and  $0.2\%$  is downward (Extended Data Fig. 8). Near the UGR, strong suppression of the downward radiation is achieved across a reasonably broad bandwidth: over  $90\%$  of the upward radiation energy is maintained within a 26 nm bandwidth from 1,536 nm to 1,562 nm, as shown in Extended Data Fig. 8a. Furthermore, we achieve robust suppression of downward radiation at different out-coupling angles between  $5^{\circ}$  and  $11^{\circ}$ , as shown in Extended Data Fig. 8b. Although we have not fully characterized the fibre-to-waveguide losses for our design, the UGRs that we demonstrate here naturally eliminate downward radiation and provide a practical and effective method to suppress downward radiative losses.

# Data availability

The datasets generated and analysed during the current study are available from the corresponding author upon request.

32. Wang, Z. et al. Mode splitting in high-index-contrast grating with mini-scale finite size. Opt. Lett. 41, 3872-3875 (2016).  
33. Lv, J. et al. Demonstration of a thermo-optic phase shifter by utilizing high-Q resonance in high-index-contrast grating. Opt. Lett. 43, 827-830 (2018).  
34. Regan, E. C. et al. Direct imaging of isofrequency contours in photonic structures. Sci. Adv. 2, e1601591 (2016).  
35. McMaster, W. H. Polarization and the stokes parameters. Am. J. Phys. 22, 351-362 (1954).  
36. Notaros, J. et al. Ultra-efficient CMOS fiber-to-chip grating couplers. In Optical Fiber Communications Conf. Exhibit. 1-3 (IEEE, 2016).  
37. Wade, M. T. et al. 75% efficient wide bandwidth grating couplers in a 45 nm microelectronics cmos process. In IEEE Optical Interconnects Conf. 46-47 (IEEE, 2015).  
38. Wang, B., Jiang, J. & Nordin, G. P. Compact slanted grating couplers. Opt. Express 12, 3313-3326 (2004).  
39. Li, M. & Sheard, S. J. Waveguide couplers using parallelogramic-shaped blazed gratings. Opt. Commun. 109, 239-245 (1994).  
40. Hagberg, M., Eriksson, N. & Larsson, A. Investigation of high-efficiency surface-emitting lasers with blazed grating outcouplers. IEEE J. Quantum Electron. 32, 1596-1605 (1996).  
41. Eriksson, N., Hagberg, M. & Larsson, A. Highly directional grating outcouplers with tailorable radiation characteristics. IEEE J. Quantum Electron. 32, 1038-1047 (1996)  
42. Notaros, J. & Popovi, M. A. Band-structure approach to synthesis of grating couplers with ultra-high coupling efficiency and directivity. In Optical Fiber Communications Conf. Exhibit, 1-3 (IEEE, 2015).  
43. Michaels, A. & Yablonsovitch, E. Inverse design of near unity efficiency perfectly vertical grating couplers. Opt. Express 26, 4766-4779 (2018).  
44. Dai, M. et al. Highly efficient and perfectly vertical chip-to-fiber dual-layer grating coupler. Opt. Express 23, 1691-1698 (2015).

Acknowledgements We thank L. He for discussion, V. Yoshioka for reading the manuscript and Z. Zhang for helping to conduct the experiments. C.P. was supported by the National Natural Science Foundation of China under grant number 61922004. J.J. and B.Z. were sponsored by the US Army Research Office under grant number W91NF-19-1-0087. The simulations were supported by the High-performance Computing Platform of Peking University. The project was partially supported by AFRL contract FA8650-16-D-5403 and MIT Lincoln Laboratory contract 7000371273, as well as by the Army Research Office, and was accomplished under Cooperative Agreement number W91NF-18-2-0048. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the Army Research Office or the US Government. The US Government is authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation herein.

Author contributions All authors contributed substantially to this work. X.Y., C.P. and B.Z. wrote the manuscript with contributions from all authors. M.S., C.P. and B.Z. supervised the project.

Competing interests The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41586-020-2181-4.  
Correspondence and requests for materials should be addressed to C.P.  
Peer review information Nature thanks Yuri Kivshar, Mikael Rechtsman and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.  
Reprints and permissions information is available at http://www.nature.com/reprints.

![](images/2f317dede56e18d508dd62310153e89b14645f214a8c2e2eda6c81dc29232f63.jpg)  
a)

![](images/82d14532333f8431e3f0fb59a08ed4bc10b0a1a0292213c0f27f0ef544b8a3f0.jpg)  
Wafer preparation

![](images/4daa7f3be14df3d24ac130b4f0e19e8d4aa5e7954c0125fca9026577c62274aa.jpg)  
PECVD deposit

![](images/934cd22d897b6c549637d4ee2b2283d79eda09794216100de37c41a7503e9c42.jpg)

![](images/551e54b6ccdfb8f241346188da9db2c4f98193aea9502846bb07cd8778714887.jpg)  
Spin-coat resist

![](images/ea4a0b9bce68c09e38862b039d34f5882eb0e61832f9f49110af1ed863c9d476.jpg)  
EBL exposure

![](images/0ab4e0bda7d1a421144b13464a473828186a7e20cd34b091cea08fc9aaafcec1.jpg)  
CF4 RIE etch

![](images/ae5ae34c4b2ffd5f1d24c6ed90baa2345601bc07db4a593194bf9f7684bf020b.jpg)

![](images/a603dd6969d50aadfd2d233dd7b233b83033e6be19dcf43118c12b6e040ccc2a.jpg)  
Cl2 RIE etch

![](images/3048f7583d9288aa6e40731d770b42be40e111a0b8786eb4afcdea4cbdff1f12.jpg)  
BHF wet etch

![](images/67bed5c8e7d94bafaffdd90e315d14ef4fe93f7bbbf996ec2425f3d693aab94a.jpg)

![](images/ec5ee870f6394e8577b817e9977fa826d9096583872b07a908927677d1097f78.jpg)  
CMP mirror-finish

![](images/25ce0ab296acc09269d905d3d3ff1c7009df464a44188232e7b53446e64a9a5a.jpg)  
resist  
SiO2

![](images/dcc49733fbc12018e3766305087926369d024a0d790b80d2d6fd7e1e3fd9994b.jpg)

![](images/dc6bdbc6ce62493bb83efa26e594bcd8c480980d0081165fc88f59c3aa78c5d7.jpg)  
Extended Data Fig.1|Sample fabrication.a, Step-by-step flow chart of the fabrication process.b, Schematics of the customized RIE process. EBL, electron-beam lithography; PECVD, plasma-enhanced chemical vapour deposition; CMP, chemical-mechanical polishing.  
Si

![](images/8c1a85aa56605e5825551c4cab14cb55ed97afe0246cc83a59d1ed3d92519d25.jpg)  
b)  
Ion bombardment

![](images/c2809072c5da8439a9e6f81385d5d1023b2dcb9942ba5e9d5598e164eb6f95f6.jpg)  
Extended Data Fig.2 | Experimental setup used to measure the asymmetry ratio  $\eta$ . The setup is capable of both near- and far-field measurements. The focal lengths of lenses L2, L3, L4 and L5 are  $150\mathrm{mm}$ ,  $100\mathrm{mm}$ ,  $75\mathrm{mm}$  and  $75\mathrm{mm}$ ,  
respectively. RFP, rear focal plane; PD, photodetector; Obj, objective; Pol, polarizer; Amp, amplifier; BS, beam splitter. N1 and N2 denote the movable lenses used to achieve near-field imaging.

![](images/4ffae3974fa814f7cf7e3c720f4585cf926c8c13e7761ec480822aa77906293d.jpg)  
a)  
Ideal Disordered  $\times$  Experiment  
Extended Data Fig. 3 | Experimental and simulation results for disordered samples. a, Experimentally extracted  $Q_{\mathrm{tot}}$  (blue) compared with simulation results for samples with (green) and without (red) disorder. b, Measured asymmetry ratio  $\eta$  (blue) compared with simulation results for samples with (green) and without (red) disorder.

![](images/1440f66c803825bdeafa3b0a1d8a9282abd3540ce6becb8de4a796645083f599.jpg)  
b)

![](images/eadd658f0c2abbc6ccb6308b1fe8db98bebec9a56fc43e57679a772c2fce4b42.jpg)

# Extended Data Fig.4 | Experimental setup used for polarimetry

measurements. An amplified spontaneous emission (ASE) source excites the resonances in the sample. Scattered light is recorded by a camera under six different combinations of a polarizer (Pol) and a QWP. The focal lengths of lenses L2, L3, L4 and L5 are  $150\mathrm{mm}$ ,  $100\mathrm{mm}$ ,  $75\mathrm{mm}$  and  $75\mathrm{mm}$ , respectively.

![](images/d7c8a4664180061184b3dae9e16e32dba8cdb733eb92f6db003ca23816330037.jpg)  
Extended Data Fig. 5 | Experimental observation of the evolution of half-integer charges. a, UGR as the merging point between two half-integer charges. b-f, Measured ellipticity  $\rho$  of the resonances in five samples with

![](images/3b00b1685ead880587cc31edc6f0d3f4c19bd828b43da935df7fb42d2b303eac.jpg)

![](images/e612930c33458b77700550423fe54bf8d842d97b7e722db6ba7186ad44e6f1f0.jpg)  
slightly different air-gap widths  $w$ , ranging from  $w / a = 0.399$  (b) to 0.403 (f). Dark red ( $\rho = 1$ ) and dark green ( $\rho = -1$ ) colours indicate the locations of the LCP and RCP resonances, which are also half-integer topological charges.

![](images/cd0b2fa5267cc7edd5f1a93e79858ca795cd7f402b18f352cd56f6eece12f302.jpg)

![](images/343f09e424f7c8c01974ed55c692427a2da596021bd688d9efc517774531c201.jpg)

![](images/fc4c8da2b7a20edf71f76807483e697d9b2dfd8ced542484858bc8cf708577e3.jpg)

![](images/a3bfc6bd7d29897c3492d70eb9658d5a47644209e7b52cd7aa27bdb16044dc6b.jpg)  
a)

![](images/89b19f584e53f0713a96151217783bd98f591924749eeebc97924c766ff5b3b8.jpg)  
b)

![](images/8df4bd2ed156d4b624759bd1d538449820aa0a673e5a1ac3df7e0084946f05f3.jpg)  
c)  
Extended Data Fig. 6 | Robustness of UGRs against parameter variations. a, Device performance when the air-gap widths deviate by  $\pm 2.5\mathrm{nm}$  from the perfect design. b, Device performance when the etching angle deviates by  $\pm 1^{\circ}$  from the perfect design (grey). c, The UGR is restored if the etching angle deviates by  $-1^{\circ}$  from the perfect design and the air-gap width changes to  $w = 365\mathrm{nm}$ .

![](images/e9b0c8c977a790aaaf83022cd7f717c2fe610e439f8a66592522c7f405524822.jpg)

Extended Data Fig.7 | Asymmetry ratio for modes near UGRs. Simulated

(left) and measured (right) asymmetry ratios  $\eta$  for resonances close to the UGR in momentum space.

![](images/055e1db473a8b28695f36f3159231956b7170c385867c7262282f3b420445037.jpg)

![](images/a53d8e3287b44dd8a9f62ed2bfdc4c60c3962aea20de64e79f7351f596b254d1.jpg)

# Extended Data Fig. 8 | Prospects of using UGRs as grating couplers.

a, Asymmetry ratio  $n$  between upward and downward radiation intensities for a fixed out-coupling angle of  $9^{\circ}$ . The maximum reaches 27.7 dB near the UGR and remains high (above 10 dB) over a bandwidth of 26 nm. b, Highly directional emission is observed over a wide range of excitation wavelengths and for different out-coupling angles. The fibre-to-waveguide loss is not measured.

Extended Data Table 1 | Comparison of different mechanisms used to achieve highly directional radiation  

<table><tr><td rowspan="2">Mechanism</td><td colspan="2">Asymmetry ratio (dB)</td><td colspan="2">Maximum coupling efficiency (%)</td><td rowspan="2">Ref</td></tr><tr><td>numerical</td><td>experimental1</td><td>numerical</td><td>experimental1,2</td></tr><tr><td>non-resonant blazing effect</td><td>8.7</td><td>×</td><td>80.1</td><td>×</td><td>[38]</td></tr><tr><td>non-resonant blazing effect</td><td>20</td><td>×</td><td>up to 99</td><td>×</td><td>[39]</td></tr><tr><td>non-resonant blazing effect</td><td>20</td><td>&gt;7.96</td><td>up to 99</td><td>86.2</td><td>[40]</td></tr><tr><td>non-resonant blazing effect</td><td>20</td><td>×</td><td>up to 99</td><td>×</td><td>[41]</td></tr><tr><td>dual-layer guided resonance</td><td>20</td><td>&gt;10.6</td><td>95</td><td>92</td><td>[36]</td></tr><tr><td>dual-layer guided resonance</td><td>20</td><td>×</td><td>95</td><td>×</td><td>[42]</td></tr><tr><td>dual-layer guided resonance</td><td>21</td><td>×</td><td>99.2</td><td>×</td><td>[43]</td></tr><tr><td>dual-layer guided resonance</td><td>8.9</td><td>×</td><td>70</td><td>×</td><td>[44]</td></tr><tr><td>UGR</td><td>70</td><td>27.7</td><td>×</td><td>×</td><td>this work</td></tr></table>

Data from refs.  $^{38-44}$  and from this work.  
Lower bound on the measurement value.  
2Not including taper loss.