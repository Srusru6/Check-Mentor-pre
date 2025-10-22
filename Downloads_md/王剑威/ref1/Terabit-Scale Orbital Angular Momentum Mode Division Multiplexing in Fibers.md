# Terabit-Scale Orbital Angular Momentum Mode Division Multiplexing in Fibers

Nenad Bozinovic, $^{1*}$  Yang Yue, $^{2*}$  Yongxiong Ren, $^{2}$  Moshe Tur, $^{3}$  Poul Kristensen, $^{4}$  Hao Huang, $^{2}$  Alan E. Willner, $^{2\dagger}$  Siddharth Ramachandran $^{1\dagger}$

Internet data traffic capacity is rapidly reaching limits imposed by optical fiber nonlinear effects. Having almost exhausted available degrees of freedom to orthogonally multiplex data, the possibility is now being explored of using spatial modes of fibers to enhance data capacity. We demonstrate the viability of using the orbital angular momentum (OAM) of light to create orthogonal, spatially distinct streams of data-transmitting channels that are multiplexed in a single fiber. Over 1.1 kilometers of a specially designed optical fiber that minimizes mode coupling, we achieved 400-gigabits-per-second data transmission using four angular momentum modes at a single wavelength, and 1.6 terabits per second using two OAM modes over 10 wavelengths. These demonstrations suggest that OAM could provide an additional degree of freedom for data multiplexing in future fiber networks.

The data-carrying capacity of single-mode optical fibers has increased by four orders of magnitude in the past three decades (1), primarily because of multiplexing techniques that use wavelength, amplitude, phase, and polarization of light to encode information (Fig. 1A). As

$^{1}$ Department of Electrical and Computer Engineering and Photonics Center, Boston University, Boston, MA 02215, USA.  $^{2}$ Department of Electrical Engineering, University of Southern California, Los Angeles, CA 90089, USA.  $^{3}$ School of Electrical Engineering, Tel Aviv University, 69978 Tel Aviv, Israel.  $^{4}$ OFS-Fitel, 2605 Brøndby, Denmark.

*These authors contributed equally to this work. †Corresponding author. E-mail: sidr@bu.edu (S.R.); willner@ usc.edu (A.E.W.)

the capacity of the current optical fiber systems reaches limits imposed by nonlinear effects (2), the possibility of spatial-division-multiplexing methods by use of multicore (3) and multimode (4) fibers has emerged to address the forthcoming capacity crunch. Although multicore fibers potentially require more complex manufacturing than do circularly symmetric multimode fibers, conventional multimode fibers suffer from mode coupling caused by random perturbations in fibers or incomplete mode-conversion (5). Methods that have been developed to address the problem of mode coupling so far have been dependent on computationally intensive digital signal processing (DSP) algorithms, and have been based either on

adaptive optics feedback (6) or complex multiple-input multiple-output (MIMO) methodologies (4).

We show a method that offers a means of increasing network throughput without using complex DSP algorithms, but instead by using fiber modes that carry orbital angular momentum (OAM). As one of the most fundamental physical quantities in classical and quantum electrodynamics, OAM of light has initiated widespread interest in many areas, including optical tweezers, atom manipulation, and optical communications (7). Photons that carry OAM have a helical phase of electric field proportional to  $\exp (i\ell \phi)$ , where  $\ell$  is topological charge, and  $\phi$  is the azimuthal angle (7). Several classical (8) and quantum (9) communications experiments have exploited the inherent orthogonality of OAM modes in free space by multiplexing information in this additional degree of freedom, increasing the capacity of free-space communications links. In fibers, however, OAM beams were considered to be completely unstable owing to mode coupling, and only short-length fiber propagation, without data transmission, has been demonstrated (10-14).

The OAM mode-division multiplexing (OAM-MDM) concept used here is illustrated in Fig. 1B and is based on multiplexing two fundamental fiber modes of opposite spins (circular polarizations), with the two OAM fiber modes of opposite topological charges  $\ell = \pm 1$ . The three key enablers for our demonstration are (i) a multiplexing setup, comprising spatial light modulators (SLMs) and conventional free-space optics (conceptually illustrated in Fig. 1, C and D), that enabled  $< -21$  dB of multiplexing crosstalk; (ii) a circularly symmetric specialty fiber fabricated on a commercial manufacturing setup that minimized mode coupling, leading to  $< -10$  dB of crosstalk

![](images/8efa9ac9d4ddb4271e4e908bed51a49351513a3c8d906f621830044f910b901f.jpg)  
Fig. 1. The OAM-MDM principle. (A) OAM may be considered as an orthogonal degree of freedom for data multiplexing. (B) Simplified OAM-MDM setup: four modes with distinct values of OAM  $(\ell)$  and spin (or circular polarization, s) are multiplexed into a specialty fiber, transmitted for  $1.1\mathrm{km}$ , demultiplexed, and analyzed at the output by using BER testers and cameras. (C) OAM conversion of  $\ell = 0\rightarrow 1$  is achieved by using spiral phase patterns (SPPs) (the spiral pattern has opposite helicity for the  $\ell = 0\rightarrow 1$  case). (D) Spin conversion to  $s = \pm 1$  is implemented with a quarter wave plate (QWP) whose fast axis is oriented  $\pm 45^{\circ}$  with respect to the input (linear) polarization.

![](images/b690852625d22600c4f113dfbef21949f9ad5f9d333c58d6c383a61456d26a27.jpg)

![](images/c40e53d6704881a7b6978b59f2746a9b5dfea55f8a152e5fda5bb85acc1be45a.jpg)

among modes after  $1.1\mathrm{km}$  of propagation; and (iii) a demultiplexing setup that enabled sorting of the modes with high purity at the output by using free-space polarization and OAM sorters. The detailed experimental setup is available in fig. S1 (15).

Conventional single-mode fibers (SMFs) support propagation of two distinct, degenerate polarization states of the fundamental mode  $(LP_{01}^{\pm})$ , designated by their spin  $s = \pm 1$ . The few-mode fiber that we use ("vortex fiber") additionally supports the first-order antisymmetric modes: one transverse magnetic mode  $(TM_{01})$ , two  $OAM^{\pm}$  modes (denoted by their  $\ell = \pm 1$  topological charge), and one transverse electric  $(TE_{01})$  mode ("0" and "1" in the subscript "01" refer to azimuthal and radial indices, respectively, denoting the number of nulls in the electric field in the two orthogonal directions). However, unlike traditional few-mode fibers, the vortex fiber was designed to lift the near-degeneracy between the desired  $OAM^{\pm}$  and parasitic  $TM_{01}$  and  $TE_{01}$ , hence minimizing modal crosstalk between them (16). Thus, this fiber yields two new degenerate states  $(OAM^{\pm})$  in addition to the conventional degenerate  $LP_{01}^{\pm}$  modes.

The index profile of our vortex fiber (Fig. 2, A and B) has a characteristic high-index ring that serves to lift the debilitating near-degeneracy between the desired  $OAM^{\pm}$  and parasitic  $TM_{01}$  and  $TE_{01}$  responsible for mode coupling in conventional fibers (5). Effective index differences  $(\Delta n_{eff})$  of the first-order modes with respect to the  $LP_{01}^{\pm}$  modes were numerically calculated and compared with the experimentally measured values (Fig. 2C). In the vortex fiber, the  $OAM^{\pm}$  states are separated from the  $LP_{01}^{\pm}$  states by  $\Delta n_{eff} \approx 3 \times 10^{-3}$  (at  $1550~\mathrm{nm}$ ) and from the parasitic  $TE_{01}$  and  $TM_{01}$  states by  $\Delta n_{eff} \approx 1.6 \times 10^{-3}$ . These values of  $\Delta n_{eff}$  are larger than those in polarization-maintaining fibers that preserve distinct polarization modes and, by analogy, indicate that all distinct modes in the vortex fiber should be resistant to distributed mode coupling (16). This is in contrast to conventional fibers and hence indicative of the fact that OAM modes would be preserved in these vortex fibers. The degenerate pair of  $OAM^{\pm}$  states inevitably mix into each other because of fiber birefringence (13). However, this coupling can be compensated for by

using a fiber polarization controller (we achieve  $-20\mathrm{dB}$  of crosstalk between the two  $OAM^{\pm}$  states at the output of the 1.1-km bare-fiber spool). Polarization controller feedback-based correction techniques are commonly used in conventional polarization-division multiplexed systems (17).

We used a previously developed mode-purity characterization technique that analyzes spatial intensity variations at the fiber output arising from intermodal interference in order to study the effects of distributed mode coupling (13). Relative mode powers as a function of a fiber length (iteratively measured via cutback) is shown in Fig. 2D for the case of high-purity  $(>21\mathrm{dB})$ $OAM^{+}$  mode excitation at  $1550~\mathrm{nm}$  After  $1.1\mathrm{km}$  of propagation of the desired OAM modes, less than  $-10\mathrm{dB}$  of the input power leaked into the  $LP_{01}^{\pm}$  and the parasitic  $TM_{01}$  and  $TE_{01}$  modes. The relative mode powers are also measured in time (Fig. 2E), indicating temporal stability on the order of hours, although polarization controller adjustments were necessary for longer periods of time.

Having confirmed the capability of the fiber to carry individual OAM states over long distances

![](images/3500b99eb93b0bf5ef778dcead0019f777c239dd3177daa330d6a8c49bd699ab.jpg)  
A

![](images/4e7d18e2979059e5df4564b95b9fcc59892a26b8cdb66a4d20495c0d4e551639.jpg)  
E  
B  
C

![](images/fb2dabdb014aa412ea837527f297a8a6f40f91c3518d4cab88e1656d1adbf677.jpg)

![](images/a04a604b7fa5735e235f1fc57eec9a86c00dd9269945f812a31052221b9f6f66.jpg)  
D  
F  
Fig. 2. Vortex fiber characteristics. (A) Microscope image of the vortex fiber facet. (B) Measured fiber refractive index and numerically calculated mode profiles. (C) Measured (open circles) and numerically calculated (solid lines) effective index differences  $(\Delta n_{eff})$  of the first-order modes— $TE_{01}$ ,  $OAM$ , and  $TM_{01}$ —with respect to the fundamental mode  $(LP_{01})$ ; large  $\Delta n_{eff}$  between modes lowers mode-coupling distortions. (D) Measured modal power ratios as

![](images/f094b9c8ba8b75447309c348809fc6bcdc7607a664e77ec9cb207b379f73e900.jpg)  
a function of fiber length for the case of  $OAM^{+}$  mode excitation at 1550 nm (OAM power refers to combined  $OAM^{+}$  and  $OAM^{-}$  mode powers, and  $LP_{01}$  refers to combined powers of the two  $LP_{01}^{\pm}$  states). (E) Relative mode powers with respect to time, showing the temporal stability of the  $OAM$  modes. (F) Table of vortex fiber properties at 1550 nm, including numerically calculated effective area and dispersion and experimentally measured loss.

<table><tr><td>@1550nm</td><td>neff</td><td>Aeff(μm2)</td><td>D (ps/nm-km)</td><td>Loss (dB/km)</td></tr><tr><td>LP01</td><td>1.451</td><td>82</td><td>2.0</td><td>1.3</td></tr><tr><td>OAM</td><td>1.448</td><td>88</td><td>0.6</td><td>1.6</td></tr></table>

with low mode-coupling, we investigate the prospects of multiplexing four guided modes—namely, the two  $LP_{01}^{\pm}$  and the two  $OAM^{\pm}$  modes—and using them as four distinct channels for OAM-MDM data transmission. We used a commercial SLM and free-space optics for OAM mode generation and multiplexing (Fig. 1, B and C, and fig. S1). The detailed alignment procedure is available in (15).

After  $1.1\mathrm{km}$  of propagation, the vortex fiber output is imaged onto a camera when only one channel is enabled at a time. Examples of images from the  $LP_{01}^{\pm}$  and  $OAM^{+}$  channels are shown in Fig. 3, A and B (images from all four channels are available in fig. S2). To reveal the transverse phase of the  $OAM^{\pm}$  channel outputs, interference with an expanded Gaussian beam reference was recorded (Fig. 3, C and D), with the vortex fiber polarization controller adjusted to yield  $\approx -20$  dB  $OAM^{\pm}$  crosstalk. The spiral interference patterns clearly indicate that the  $OAM^{+}(OAM^{-})$  state was obtained at the output in the case when the individual  $OAM^{+}(OAM^{-})$  mode was sent at the channel input.

With all four channels enabled simultaneously, the demuxing system sorts the modes according to their OAM  $(l)$  and spin  $(s)$  values, using another SLM and a combination of a quarterwave plate and a polarizer, respectively (15). In the example of the  $OAM^{+}$  channel, the resulting output maps back into a conventional Gaussian-shaped beam with a planar phase (Fig. 3, E and F), which we can now route to a coherent receiver by

coupling into an SMF. This enables a quantitative measure of mode purity by observing channel output power versus time (Fig. 3G), which reveals how much power leaked into other channels (crosstalk), as well as how much power leaked out-and-back, during fiber propagation, into an individual channel [multi-path interference (MPI)] (18, 19). MPI is a fundamental property arising from fiber design, whereas crosstalk depends on both the fiber and the multiplexing (or demultiplexing) setup design. Both crosstalk and MPI increase bit error rate (BER) in the absence of MIMO corrective algorithms (measured values for all the modes are given in Fig. 3E).

We have demonstrated OAM-MDM data transmission feasibility of the system described above by sending 50-GBaud, quadrature-phase-shift-keyed (QPSK) data at a single wavelength and over four mode channels (Fig. 4A) (15, 20). BERs were measured for two cases: when only one channel was used for data transmission (single-channel case) and when all four channels were simultaneously populated with distinct (decorrelated) data streams (all-channels case). In the single-channel case, the largest received power penalty for achieving a BER of  $3.8 \times 10^{-3}$  [the threshold BER level at which forward-error-correction (FEC) algorithms ensure error-free data transmission] is  $2.5\mathrm{dB}$ , mainly due to MPI. In the all-channel case, this largest power penalty increased to  $4.1\mathrm{dB}$ , mainly due to crosstalk. In the latter case, a total transmission capacity at 400 Gbit/s below the FEC limit is achieved.

In addition to the single-wavelength demonstration, we used wavelength-division multiplexing (WDM) to further extend the capacity of our system (Fig. 4C) (20). Recall that we used a conventional polarization controller to achieve  $\approx -20$  dB crosstalk between the  $OAM^{\pm}$  modes. However, optimizing our system to yield two orthogonal, pure  $OAM^{\pm}$  states at one wavelength implies that at other wavelengths, the  $OAM^{\pm}$  states will, to a certain extent, couple with each other. A more advanced transmitter with individual wavelength channel polarization control could, in principle, be used to mitigate this effect. In addition, extraneous contributory factors such as the wavelength dependence of the SLM and other free-space optical components can also affect the crosstalk. For these reasons, only two OAM modes and 10 WDM channels (from 1546.64 to  $1553.88\mathrm{nm}$ ) were chosen for our WDM experiment (Fig. 4D, boxed region, which illustrates wavelengths at which crosstalk was low) (15). Reduction to two modes allowed us to choose a more complex modulation format (16-quadrature amplitude modulation) for data transmission, yielding higher spectral efficiency, albeit at a lower baud rate of 20 GBAud. Although the BER of the two modes varied somewhat because of crosstalk (Fig. 4E), transmission of 20 channels (OAM-MDM and WDM) resulted in a total transmission capacity of  $1.6\mathrm{Tb / s}$  under the FEC limit.

Our results indicate that simple, low-complexity DSP coherent detection methods can be used to achieve OAM-MDM in fibers. Our demonstration

![](images/20df4c7228d98b858c17ec493ca28e662ef4a54264442e3656f31ce3a02f2670.jpg)  
B

![](images/ec1ea3b1436856ca8cf7199fac77ec50a62b2d36999ebe8ab58884bb33ab7a78.jpg)  
D

![](images/2c740a3e3ecaf37ee21b48318a289b28c249130a32a3f7b675270f4e9ff7465c.jpg)  
$O A M^{+}$  after demux

![](images/1932e7c648461ba47133a439ec79b6da7190dc7981e63743d473b98774383907.jpg)

![](images/bd08fcb7937804a5689ed24633c9c409781a82c8a0e714b1aca77b3cc683b817.jpg)  
F

![](images/619f255560c9a485ad3b1d9164ae0f81d00871c3bff806c7dced7f6640ade803.jpg)  
Fig. 3. Transmission channel characterization. (A and B) Intensity of  $LP_{01}^{\pm}$  and  $OAM^{+}$  channel outputs (collimated). (C and D) Interference patterns between an expanded Gaussian beam reference and the  $OAM^{+}$  and  $OAM^{-}$  channel outputs, respectively. The handedness of the spiral is indicative of the OAM value ( $l = +1$  or -1) carried by each beam. Clear spiral images are also indicative of high mode purity. (E and F) Intensity and phase of the  $OAM^{+}$  channel output after demulti-  
plexing. All images taken when only one channel is enabled at a time. (G) Example of the  $LP_{01}^{\pm}$  channel power drift (attributed to crosstalk and free-space optics) and power fluctuations (due to MPI). (Inset) Illustration of crosstalk and MPI mechanisms; mode A can couple into mode B, producing crosstalk, but a certain amount of the power can couple back into mode A, interfering with the original signal and producing MPI. (H) Table of measured values for crosstalk and MPI for all four modes.

![](images/82528b483e642030df2d04b405024cf4b1675d711b5e2fd19fd3122d83fe06ee.jpg)  
G

H  

<table><tr><td></td><td>OAM+</td><td>OAM-</td><td>LP01+</td><td>LP01-</td></tr><tr><td>Cross-talk (dB)</td><td>-14.8</td><td>-15.5</td><td>-16.1</td><td>-15.2</td></tr><tr><td>MPI (dB)</td><td>-44</td><td>-43</td><td>-41</td><td>-41</td></tr></table>

1 wavelength, 4 modes,  $50 \times 2$  Gb/s QPSK

![](images/c28f2f3365a4d9a6663c79b89410c1e0bf44470a744cb2f02479c6a67754b142.jpg)  
A  
Laser Source

![](images/3d505e01ffd5a0d3077526c1a2c3d7f65f73ddcb61633078e0550efaf5ad58f3.jpg)  
Generation of OAM Beams

![](images/c9dcdf20aa49071ed0bad3187b0ddbb7fdf6fcb8e220594f61da3f75f0f5b172.jpg)  
B  
Fig. 4. Data-transmission experiments. (A) Block diagram of  $50 \times 2$  Gbaud QPSK signal transmission over a single wavelength carrying four modes in the vortex fiber. (B) Measured BER as a function of received power for the single-channel (SC) and all-channels (AC) transmission case. (C) Block diagram

10 wavelengths, 2 modes,  $20 \times 4$  Gb/s 16-QAM

![](images/fe15ab1c962e518c6263561664e2230390b63204f0fb8ee73f83a1bca200cb66.jpg)  
C  
WDM Source

![](images/e4c947718fff4a61fbacb9c066f2901cb5a1aca63eb1aa17db7e1868340d27e1.jpg)  
16-QAM Generation

![](images/a9589e515192f3d48bf5aea4c84fb49cc005f114d452c08d7d879c6a2d8b05e0.jpg)  
Generation of OAM Beams

![](images/565dbc5d4626f463482568666b977663fb0a6af2dde64569f38ea84433b4f47f.jpg)  
D  
E

![](images/acb4fc2d2345d3b0684a363edf51b223685fa4c909c516559cedc3808ac1fac6.jpg)  
of  $20 \times 4$  Gbaud 16-QAM signal transmission over 10 wavelengths carrying two modes in the vortex fiber. (D) Measured crosstalk between  $OAM^{\pm}$  modes as a function of wavelength. (E) BER as a function of wavelength for  $OAM^{\pm}$  modes in the WDM system.

used no computationally intensive DSP corrective algorithms, such as MIMO. Furthermore, because our OAM-MDM scheme primarily required that the vortex fiber we used enabled mode-coupling-free propagation of OAM modes, we expect this scheme to be scalable in number of modes, and thus data capacity, given recent developments on fiber designs that may be able to support propagation of multiple OAM modes with  $\ell >> 1$  (22). Because our primary goal is that of demonstrating the viability of fiber-based data transmission of independent OAM modes, we used conventional, commercial components (SLMs and wave retarders) forMUXing and demuxing, which are inherently lossy as the number of OAM modes is scaled. Recent demonstrations of theoretically lossless OAM muxing devices, based on waveguides (23) or free-space optics (24), indicate that the required component technology is concurrently developing to enable realistic deployments of scalable networks based on OAM-MDM.

# References and Notes

1. R. Essiambre, R. Tkach, Proc. IEEE 100, 1035 (2012).  
2. D. J. Richardson, Science 330, 327 (2010).  
3. J. Sakaguchi et al., J. Lightwave Technol. 30, 658 (2012).  
4. R. Ryf et al., J. Lightwave Technol. 30, 521 (2012).

5. D. Marcuse, Appl. Opt. 23, 1082 (1984).  
6. J. Carpenter, B. C. Thomsen, T. D. Wilkinson, Degenerate mode-group division multiplexing, J. Lightwave Technol. 30, 3946 (2012).  
7. D. Andrews, Structured Light and Its Applications (Academic Press, New York, 2008).  
8. J. Wang et al., Nat. Photonics 6, 488 (2012).  
9. S. Gröblacher, T. Jennewein, A. Vaziri, G. Weihs, A. Zeilinger, New J. Phys. 8, 75 (2006).  
10. D. McGloin, N. B. Simpson, M. J. Padgett, Appl. Opt. 37, 469 (1998).  
11. P. Z. Dashti, F. Alhassen, H. P. Lee, Phys. Rev. Lett. 96, 043604 (2006).  
12. N. Bozinovic, P. Kristensen, S. Ramachandran, in Frontiers in Optics 2011/Laser Science XXVII, OSA Technical Digest (online) (Optical Society of America, 2011), paper LW3; available at http://dx.doi.org/10.1364/LS.2011.LWL3.  
13. N. Bozinovic, S. Golowich, P. Kristensen, S. Ramachandran, Opt. Lett. 37, 2451 (2012).  
14. G. K. L. Wong et al., Science 337, 446 (2012).  
15. Materials and methods are available as supplementary materials on Science Online.  
16. S. Ramachandran, P. Kristensen, M. F. Yan, Opt. Lett. 34, 2525 (2009).  
17. H. Sunnerud, C. Xie, M. Karlsson, R. Samuelsson, P. A. Andrekson, J. Lightwave Technol. 20, 368 (2002).  
18. S. Ramachandran, J. W. Nicholson, S. Ghalmi, M. F. Yan, IEEE Photon. Technol. Lett. 15, 1171 (2003).  
19. S. Ramachandran, S. Ghalmi, J. Bromage, S. Chandrasekhar, L. L. Buhl, IEEE Photon. Technol. Lett. 17, 238 (2005).

20. N. Bozinovic et al., in European Conference and Exhibition on Optical Communication, OSA Technical Digest (online), (Optical Society of America, 2013), paper Th.3.C.6; available at http://dx.doi.org/10.1364/ECEOC.2012.Th.3.C.6.  
21. Y. Yue et al., in Conference on Optical Fiber Communications, OSA Technical Digest, paper OTh4G.2 (Optical Society of America, Washington, DC, 2013).  
22. P. Gregg et al., in Conference on Lasers and Electro-Optics 2013, OSA Technical Digest (online) (Optical Society of America, 2013), paper Ctu2K.2.  
23. T. Su et al., Opt. Express 20, 9396 (2012).  
24. G. C. Berkhout, M. P. Lavery, J. Courtial, M. W. Beijersbergen, M. J. Padgett, Phys. Rev. Lett. 105, 153601 (2010).

Acknowledgments: We thank S. Golowich, P. Gregg, and P. Steinurzel for insightful discussions and M. V. Pedersen for the numerical waveguide simulation tool. This work was funded by the Defense Advanced Research Projects Agency-InPho program. M.T. acknowledges support from the Chief Scientist Office of the Israeli Ministry of Industry, Trade and Labor within the "Tera Santa" consortium. All data related to the experiments described in this manuscript are recorded in laboratory notebooks of members in S.R.'s group, and all associated digital data are stored on networked computers at Boston University, whose contents are archived daily.

# Supplementary Materials

www.sciencemag.org/cgi/content/full/340/6140/1545/DC1

Materials and Methods

Figs. S1 to S6

15 March 2013; accepted 29 May 2013

10.1126/science.1237861

# Terabit-Scale Orbital Angular Momentum Mode Division Multiplexing in Fibers

Nenad Bozinovic, Yang Yue, Yongxiong Ren, Moshe Tur, Poul Kristensen, Hao Huang, Alan E. Willner and Siddharth Ramachandran

Science 340 (6140), 1545-1548.

DOI: 10.1126/science.1237861

# A Twist on the Capacity Crunch

The rate at which data can be transmitted down optic fibers is approaching a limit because of nonlinear optical effects. Multiplexing allows data to be encoded in different modes of light such as polarization, wavelength, amplitude, and phase and to be sent down the fibers in parallel. Optical angular momentum (OAM) can provide another degree of freedom whereby the photons are given a well-defined twist or helicity. Bozinovic et al. (p. 1545) were able to transmit high-bandwidth data using OAM modes in long lengths of optical fibers, thus providing a possible route to get yet more capacity through optic fiber networks.

# ARTICLE TOOLS

http://science.sciencemag.org/content/340/6140/1545

# SUPPLEMENTARY MATERIALS

http://science.sciencemag.org/content/suppl/2013/06/26/340.6140.1545.DC1

# RELATED CONTENT

http://science.sciencemag.org/content/sci/340/6140/1513.full

# REFERENCES

This article cites 18 articles, 2 of which you can access for free http://science.sciencemag.org/content/340/6140/1545#BIBL

# PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service