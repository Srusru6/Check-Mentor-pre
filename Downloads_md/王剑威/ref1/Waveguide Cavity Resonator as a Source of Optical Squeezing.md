# Waveguide Cavity Resonator as a Source of Optical Squeezing

M. Stefszky, R. Ricken, C. Eigner, V. Quiring, H. Herrmann, and C. Silberhorn  
Integrated Quantum Optics, Applied Physics, University of Paderborn, Warburger Strasse 100, 33098 Paderborn, Germany  
(Received 10 February 2017; revised manuscript received 3 April 2017; published 27 April 2017)

We present the generation of continuous-wave optical squeezing from a titanium-in-diffused lithium niobate waveguide resonator. We directly measure  $2.9 \pm 0.1$  dB of single-mode squeezing, which equates to a produced level of  $4.9 \pm 0.1$  dB after accounting for detection losses. This device showcases the current capabilities of this waveguide architecture and precipitates more complicated integrated continuous-wave quantum devices in the continuous-variable regime.

DOI: 10.1103/PhysRevApplied.7.044026

# I. INTRODUCTION

The utility of quantum states of light is continually increasing as the production, manipulation, and detection of these states improve. For example, such states have been used in gravitational-wave detectors to improve their sensitivity [1-3], while quantum-key-distribution schemes have been demonstrated over useful distances [4] and are now sold as readily available commercial products. Concurrently, progress towards quantum computing and quantum-information processing in both the continuous-variable (CV) and discrete-variable regimes is constantly continuing [5-7].

As these technologies continue to develop, the need for devices that are reproducible, integrable, intrinsically stable, compact, and efficient becomes ever more critical. Integrated devices, boasting many of these properties, have shown substantial improvements in recent years [7,8]. Devices have recently been constructed that combine state generation and manipulation in a single chip [9,10]. Additionally, waveguide devices have recently been used to create more complicated states such as a two-photon quantum-mechanical many-body entangled state and photon-triplet states [11,12]. Integrated devices do not come without additional challenges, however, and one has to address issues such as internal mode overlap, increased losses, photorefractive effects, and the spatial mode overlap between devices and fibers.

Until very recently, most of the attention in integrated quantum optics was directed towards discrete-variable quantum optics [7,9]. However, CV quantum optics more easily achieves deterministic, unconditional operation, and it is therefore better suited to, or provides alternative solutions to, many tasks. CV quantum optics has been used, for example, to improve spectroscopy [13], metrology [2,3], and sensing [14,15] via quantum enhancement.

The foundation of CV quantum optics is optical squeezing. Traditionally, the strongest levels of squeezing have been produced in second-order processes in bulk resonators [16-18]. By contrast, the vast majority of research has been

directed towards single-pass pulsed systems [19-22]. Pulsed systems are used for their intense peak powers, which helps to overcome the large losses that waveguide systems have traditionally exhibited. Only recently has a fully fiber-integrated squeezed light source and detection scheme been demonstrated [23]. In other works, efficient and complicated manipulation of continuous-variable squeezing has been demonstrated in a silica-on-silicon chip [24], and the generation of twin-beam squeezing has been demonstrated in both silicon nitride [25] and whispering-gallery-mode resonators [26].

Resonators have the advantage that they allow one to tailor the trade-off between squeezing bandwidth and magnitude for any particular application. Furthermore, they allow for the production of strong continuous-wave squeezing, the magnitude of which is limited in single-pass configurations due to power limitations [23,27]. The downside to resonators is twofold: in most circumstances, they require active stabilization and they are generally highly sensitive to intracavity losses. These issues are more pronounced in integrated devices because their losses are typically quite high, and photorefractive and/or photothermal effects will limit device stability at high powers.

In this paper, we present results from a titanium-in-diffused lithium niobate waveguide resonator source of single-mode squeezed light that produces high levels of continuous-wave squeezing, on a par with the best squeezing produced in waveguides from any system. The strong levels of squeezing that are generated precipitates the development of more-complicated CV integrated quantum-optics devices. Further improvements to increase the performance and utility of the device are discussed.

# II. THE DEVICE

Waveguides are fabricated in  $Z$ -cut  $\mathrm{LiNbO_3}$  by an in-diffusion of lithographically patterned  $7 - \mu \mathrm{m}$ -wide, 80-nm-thick titanium strips. The diffusion is performed at  $1060^{\circ}\mathrm{C}$  for  $9\mathrm{h}$  in an oxygen flow at atmospheric pressure. In a subsequent lithography step, an insulating

photoresist pattern is defined which is used for field-assisted periodic domain inversion. We choose a poling period of approximately  $16.9\mu \mathrm{m}$  to achieve the desired type-0 quasiphase matching, where all interacting fields are in the TM polarization, at approximately  $170^{\circ}\mathrm{C}$ . The sample is then annealed at  $300^{\circ}\mathrm{C}$  for  $2\mathrm{h}$  to reduce stress at the periodically poled domain walls. This waveguide architecture is chosen because of the ability to produce extremely low-loss waveguides (0.02 dB/cm at  $1550~\mathrm{nm}$ ) [28]. Additionally, lithium niobate is suitable for a fully integrated architecture because of the ability to incorporate additional devices such as wavelength demultiplexers [10] and electro-optic modulators. An 80-mm sample is produced which is cut into a number of smaller pieces that are used for squeezing, second-harmonic production, and local-oscillator shaping.

The end-face coating, deposited in house, which is used as the output of the device has a reflectivity of  $77 \pm 1\%$  at the fundamental wavelength, chosen to optimize the escape efficiency,  $\eta_{\mathrm{esc}} = 81 \pm 1\%$ , while keeping the threshold power at a reasonable level,  $P_{\mathrm{th}} \approx 100 \mathrm{mW}$ . A low threshold power is particularly important for this type of waveguide because photorefractive effects will limit the device performance at high pump powers [29,30]. The other surface has a high-reflectivity (HR) coating at the fundamental, and both faces are antireflecting at the second harmonic. By looking at the transmitted and reflected power from the cavity (far from phase matching) both on and off resonance [31], we are able to determine the reflectivity of the HR coating  $(R = 99.0 \pm 0.1)$  and the intracavity loss  $(0.13 \pm 0.01 \mathrm{~dB/cm})$ , which are consistent with expected values for this sample and from which the escape efficiency and other cavity properties are determined.

The cavity length is stabilized using only a standard temperature feedback scheme, one that does not sense the cavity-resonance condition. A two-stage oven is used in which a larger thermal mass is heated to temperatures of around  $160^{\circ}\mathrm{C}$  using a resistive heating cartridge and fast fine-tuning is achieved via a thermoelectric device. The entire setup is then enclosed in boxes, resulting in a system that is able to hold cavity resonance after initial thermalization for time scales lasting up to hours, which equates to a temperature stability on the millikelvin scale. This high operating temperature is chosen in order to reduce the effect of photorefraction.

# III. EXPERIMENTAL SETUP

The experimental layout is shown in Fig. 1. A  $1550\mathrm{-nm}$  Rio Grande laser system provides up to  $1\mathrm{W}$  of laser power. The power can be distributed between the local-oscillator arm and the second-harmonic stage using a Faraday isolator and half-wave plate combination. The light that passes through the Faraday isolator is frequency modulated at  $25\mathrm{MHz}$  before entering the SHG cavity. SHG is achieved in a waveguide resonator that is essentially a copy of the

![](images/f11c1af983bbcb5e2182512cf06da02cb6b84c194eb0ecf9310012cee838ce77.jpg)  
FIG. 1. Experimental schematic of the squeezezer setup. RIO denotes Rio Grande laser system; CS, coupling stage; HWP, half-wave plate; PD, photodetector; BD, beam dump; PZT, piezoelectric transducer; FI, Faraday isolator; EOM, electro-optic modulator; PBS, polarizing beam splitter; BS, beam splitter; FM, flipper mirror; WG, waveguide; DM, dichroic mirror; SHG, second-harmonic waveguide resonator; MR, dielectric mirror; and SQZ, squeezezer waveguide resonator.

squeezeer. Up to  $40\mathrm{mW}$  of second-harmonic power is stably produced by the second-harmonic cavity with a pump power of approximately  $60~\mathrm{mW}$ . The cavity-resonance condition is locked using a Pound-Drever-Hall scheme [32]. The aforementioned frequency modulation passes through the cavity and is detected by a photodetector after a dichroic mirror. This photocurrent is then fed into a Toptica DigiLock system, wherein an error signal is produced that is fed back to the frequency of the laser.

The generated second-harmonic power is coupled to the squeezeer cavity after passing through a number of dichroic mirrors and a Faraday isolator for the second harmonic. This field makes a single pass of the cavity, producing squeezing in the waveguide cavity mode. Detection of the squeezed field produced is then achieved via standard homodyne detection. The detector itself consists of two Hamamatsu G12180 photodiodes (with a quantum efficiency of approximately  $88\%$ ) in a current subtraction setup [16] with fine-tuning of the subtraction achieved via a half-wave plate in the local-oscillator arm, which varies the splitting ratio on a 50:50 beam splitter. Common-mode rejection of up to 50 dB is seen when a 100-kHz modulation is applied to the laser. Linearity of the measured shot-noise level is observed with local oscillator powers from 2 to 16 mW. Dark noise clearance of approximately 11 dB is seen with a 2-mW local oscillator.

In order to optimize the spatial overlap between the squeezed field and the local oscillator (LO), the LO is transmitted through a waveguide (cut from the same large sample as the squeezeer and the SHG resonator) whose temperature is allowed to drift at room temperature, far from phase matching. Using this method, we are able to achieve a visibility between the local oscillator and the squeezed fields of up to  $97\%$ . Visibility is measured with the use of a flipper mirror before the SHG cavity, used to direct this power through the on-resonance squeezeer, after which it interferes with the local oscillator. The visibility achieved during the presented data run of  $95 \pm 1\%$ , combined with the propagation efficiency,  $\eta_{p} = 92 \pm 2\%$ , and the aforementioned detector efficiency, results in an expected total detection efficiency of  $73 \pm 3\%$ .

# IV. RESULTS AND DISCUSSION

To characterize the performance of the waveguide resonator, we first investigate the nonlinear gain of the device. The gain of the device (assuming that the nonlinear gain is real) can be described by [33]

$$
G = \frac {\left(1 \pm \sqrt {P / P _ {\mathrm {t h}}}\right) ^ {2}}{\left(1 - P / P _ {\mathrm {t h}}\right) ^ {2}}, \tag {1}
$$

where  $G$  is the (below-threshold) parametric gain, defined as the ratio between the fundamental power exiting the cavity with gain and the power exiting the cavity without gain. The pump power is given by  $P$ , and the threshold pump field power  $P_{\mathrm{th}}$ .

A beam splitter in the LO path (shown in Fig. 1) provides a weak seed field that enters the device together with the second-harmonic pump. A piezoelectric transducer (PZT) in the seed beam is used to scan the phase between the two fields, such that amplification and deamplification of the seed can be observed. After traversing the dichroic mirrors and the Faraday isolator, the  $40\mathrm{-mW}$  SH power produced by the SHG cavity is reduced to approximately  $23\mathrm{mW}$ , measured directly in front of the squeezeer cavity. The SHG power is limited to around  $40\mathrm{mW}$  because the cavity lock becomes unstable when producing more than  $50\mathrm{mW}$  of SH. The reason for this behavior is not currently known and may be due to photorefraction or limits in the electronics. A half-wave plate before the Faraday isolator allows one to vary the amount of power entering the squeezeer. The observed gains as the pump power is varied are shown in Fig. 2.

We see that the experimental data agree very well with the theory. The fit indicates that the system has a threshold power (here defined as the power incident on the waveguide) of approximately  $135\mathrm{mW}$ . Unfortunately, this

![](images/fc54c8af67252ebd5dbe04a15e6f328249b7e28f3ce4e9170b50ea3a1c12fa07.jpg)  
FIG. 2. Parametric amplification and deamplification of a weak seed field as the pump power is varied. The pump power is defined as the power incident on the waveguide. The fit (the dashed red line) is made with a threshold power of  $135\mathrm{mW}$ . Error bars are shown for data points with uncertainties larger than the marker size.

number is not an accurate value for the true threshold power of the resonator itself because the waveguide is multimode at  $775~\mathrm{nm}$ . It is, therefore, very difficult to determine the exact amount of power in the fundamental mode, which is the only mode that couples with the squeezed field for the given phase-matching conditions.

The seed field is then blocked, leading to the production of vacuum squeezing. We expect the detected noise variances for the squeezed and antisqueezed quadratures  $V_{\pm}$  to follow the standard (non-pump-depleted) theory [33],

$$
V _ {\pm} = 1 \mp \eta_ {\mathrm {e s c}} \eta_ {\mathrm {d e t}} \frac {4 \sqrt {P / P _ {\mathrm {t h}}}}{\left(1 \pm \sqrt {P / P _ {\mathrm {t h}}}\right) ^ {2}}, \tag {2}
$$

where the escape efficiency is given by  $\eta_{\mathrm{esc}} = \left[\left(\gamma_a^{\mathrm{coup}}\right) / \gamma_a^{\mathrm{tot}}\right]$ , and  $\eta_{\mathrm{det}}$  represents the total detection efficiency (propagation, photodetector, and homodyne detector efficiencies). The cavity decay rates are defined using  $\sum \gamma_{a}^{i} = (1 - \sqrt{R_{i}}) / \tau$ , where  $R_{i}$  represents the equivalent power reflectivities for each loss source and  $\tau$  is the round-trip time of the resonator. It has been assumed that the sideband measurement frequency is well within the bandwidth of the cavity and that phase fluctuations can be neglected [34].

The quadrature measured by the homodyne is varied by scanning the phase of the local oscillator using the same PZT as before. This scanning of the phase allows one to measure the squeezing and antisqueezing. In order to more accurately measure the levels of squeezing, the phase scan is turned off and the phase is allowed to drift. The (dark-noise-corrected) results, relative to the shot noise (averaged 20 times), are shown in Fig. 3. With the maximum pump power,  $2.9 \pm 0.1$  dB of squeezing and  $6.0 \pm 0.1$  dB of antisqueezing is observed. A fit to these parameters shows that these results are consistent with a total state loss of  $58\%$ . Removing the measured escape efficiency from this value reveals

![](images/ff335da009dd6258570a364c45fbd85f2eaf8dc5575afa3aca9439354981cf5a.jpg)  
FIG. 3. Measured noise variances of the shot noise (blue line), scanned squeezing (red line), and drifting squeezing (black line). The shot noise is averaged 20 times. The resolution bandwidth is  $20\mathrm{kHz}$  and the video bandwidth is  $10\mathrm{Hz}$  for all traces. Dark noise is approximately  $12\mathrm{dB}$  below shot noise. All data are corrected for dark noise.

![](images/d6537d6c4e5efd845cb94290dabe3e5662e03d3bfd185eede525280d62e5d48f.jpg)  
FIG. 4. Measured squeezing and antisqueezing levels as the pump power is varied. The red (dashed) trace is a fit including detection losses and the black (solid) trace shows the squeezing and antisqueezing levels exiting the device, calculated by correcting for detection losses. Error bars are shown for points where the error is greater than the marker size.

a total detection efficiency of  $72\%$ , which agrees with the previously determined value for the detection losses of  $73\% \pm 3\%$ .

Finally, the previous measurement from Fig. 3 is repeated a number of times with differing pump powers. Each time the power is varied, the system is given a few minutes to stabilize. After this thermalization time, the cavity resonance is stable over time scales of at least a number of minutes, more than enough time to produce reliable squeezing results. From these traces, the amount of antisqueezing and squeezing are recorded, and they are plotted in Fig. 4 as a function of the pump power incident on the cavity..

We immediately see that the measured squeezing and antisqueezing levels fit the predicted behavior very well, indicating that the prior assumptions are valid and giving confidence in the previously determined losses. The red dashed trace is a fit to the data with the threshold power of the cavity as the only free parameter. The black trace then illustrates the amount of squeezing produced by the cavity (found by removing the detection losses).

The device can be further improved through a number of methods. Certainly, the device can be improved by reducing the losses. Titanium-in-diffused lithium niobate waveguides have been shown to have losses as low as  $0.02\mathrm{dB / cm}$  [28]. Although some of the waveguides on the current sample have losses below  $0.1\mathrm{dB / cm}$ , the nonlinear efficiency or phase-matching temperature at these waveguides is not desirable. A sample with identical mirror coatings, pump power, and nonlinear performance, but reduced losses from 0.13 to  $0.02\mathrm{dB / cm}$ , would produce over  $8\mathrm{dB}$  of squeezing. Further optimization and an increase in the available pump power would allow for the production of yet more squeezing. Although increasing the pump power increases the squeezing, it remains to be

seen at what pump-power levels photorefraction will begin to affect the properties of the squeezed state.

Another improvement to the device would be to ensure long-term stability through active locking of the resonator length. Exploiting the fact that this waveguide technology has desirable electro-optic properties, a phase modulator could be added to this device for this purpose. With the correct locking scheme, a phase modulator will allow for fast locking of the waveguide cavity length, even when producing vacuum squeezing [35].

# V. CONCLUSIONS AND OUTLOOK

In this paper, we present a titanium-in-diffused lithium niobate waveguide resonator that produces up to  $4.9 \pm 0.1$  dB of squeezing. From this state, we are able to directly measure  $2.9 \pm 0.1$  dB of single-mode vacuum squeezing. By increasing pump power, reducing losses and with further resonator optimization, we expect that it will be possible to produce greater than 8 dB of squeezing using this architecture. The addition of an on-chip modulator would also allow for a robust, compact solution to ensuring cavity stability over time. The results presented here show that integrated platforms have now progressed to a stage where it is possible to produce useful levels of squeezing without the need for pulses. These results open up the possibility of using these resources in integrated systems to provide quantum enhancement for various applications.

# ACKNOWLEDGMENTS

The authors acknowledge funding from the DFG (Deutsche Forschungsgemeinschaft) via the Gottfried Wilhelm Leibniz-Preis.

[1] H. Grote, K. Danzmann, K.L. Dooley, R. Schnabel, J. Slutsky, and H. Vahlbruch, First Long-Term Application of Squeezed States of Light in a Gravitational-Wave Observatory, Phys. Rev. Lett. 110, 181101 (2013).  
[2] LIGO Scientific Collaboration, A gravitational wave observatory operating beyond the quantum shot-noise limit, Nat. Phys. 7, 962 (2011).  
[3] J. Aasi et al., Enhanced sensitivity of the LIGO gravitational wave detector using squeezed states of light, Nat. Photonics 7, 613 (2013).  
[4] B. Korzh, C.C.W. Lim, R. Houlmann, N. Gisin, M.J. Li, D. Nolan, B. Sanguinetti, R. Thew, and H. Zbinden, Provably secure and practical quantum key distribution over  $307\mathrm{km}$  of optical fibre, Nat. Photonics 9, 163 (2015).  
[5] N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, and M. A. Nielsen, Universal Quantum Computation with Continuous-Variable Cluster States, Phys. Rev. Lett. 97, 110501 (2006).  
[6] M. Yukawa, R. Ukai, P. van Loock, and A. Furusawa, Experimental generation of four-mode continuous-variable cluster states, Phys. Rev. A 78, 012301 (2008).

[7] A. Goban, C.-L. Huang, S.-P. Yu, J. D. Hood, J. A. Muniz, J. H. Lee, M. J. Martin, A. C. McClung, K. S. Choi, D. E. Chang, O. Painter, and H. J. Kimble, Atom-light interactions in photonic crystals, Nat. Commun. 5, 3808 (2015).  
[8] A. Orieux and E. Diamanti, Recent advances on integrated quantum communications, J. Opt. 18, 083002 (2016).  
[9] J. W. Silverstone, D. Bonneau, K. Ohira, N. Suzuki, H. Yoshida, N. Lizuka, M. Ezaki, C.M. Natarajan, M.G. Tanner, R.H. Hadfield, V. Zwiller, G.D. Marshall, J.G. rarity, J.L. O'Brien, and M.G. Thompson, On-chip quantum interference between silicon photon-pair sources, Nat. Photonics 8, 104 (2014).  
[10] S. Krapick, H. Herrmann, V. Quiring, B. Brecht, H. Suche, and Ch. Silberhorn, An efficient integrated two-color source for heralded single photons, New J. Phys. 15, 033010 (2013).  
[11] R. Kruse, L. Sansoni, S. Brauner, R. Ricken, C. S. Hamilton, I. Jex, and C. Silberhorn, Dual-path source engineering in integrated quantum optics, Phys. Rev. A 92, 053841 (2015).  
[12] S. Krapick, B. Brecht, H. Herrmann, V. Quiring, and C. Silberhorn, On-chip generation of photon-triplet states, Opt. Express 24, 2836 (2016).  
[13] E. S. Polzik, J. C. Carri, and H. J. Kimble, Spectroscopy with Squeezed Light, Phys. Rev. Lett. 68, 3020 (1992).  
[14] A. M. Marino and P. D. Lett, Absolute calibration of photodiodes with bright twin beams, J. Mod. Opt. 58, 328 (2011).  
[15] H. Vahlbruch, M. Mehmet, K. Danzmann, and R. Schnabel, Detection of 15 dB Squeezed States of Light and Their Application for the Absolute Calibration of Photoelectric Quantum Efficiency, Phys. Rev. Lett. 117, 110801 (2016).  
[16] M. S. Stefszky, C. M. Mow-Lowry, S. S. Y. Chua, D. A. Shaddock, B. C. Buchler, H. Vahlbruch, A. Khalaidovski, R. Schnabel, P. K. Lam, and D. E. McClelland, Balanced homodyne detection of optical quantum states at audio-band frequencies and below, Classical Quantum Gravity 29, 145015 (2012).  
[17] M. Mehmet, S. Ast, T. Eberle, S. Steinlechner, H. Vahlbruch, and R. Schnabel, Squeezed light at  $1550~\mathrm{nm}$  with a quantum noise reduction of 12.3 dB, Opt. Express 19, 25763 (2011).  
[18] T. Eberle, S. Steinlechner, J. Bauchrowitz, V. Handchen, H. Vahlbruch, M. Mehmet, H. Müller-Ebhardt, and R. Schnabel, Quantum Enhancement of the Zero-Area Sagnac Interferometer Topology for Gravitational Wave Detection, Phys. Rev. Lett. 104, 251102 (2010).  
[19] M. E. Anderson, M. Beck, M. G. Raymer, and J. D. Bierlein, Quadrature squeezing with ultrashort pulses in nonlinear-optical waveguides, Opt. Lett. 20, 620 (1995).  
[20] Y. Eto, A. Koshio, A. Ohshiro, J. Sakurai, K. Horie, T. Hirano, and M. Sasaki, Efficient homodyne measurment of picosecond squeezed pulses with pulse shaping technique, Opt. Lett. 36, 4653 (2011).

[21] K. Yoshino, T. Aoki, and A. Furusawa, Generation of continuous-wave broadband entangled beams using periodically poled lithium niobate waveguides, Appl. Phys. Lett. 90, 041111 (2007).  
[22] Y. Eto, T. Tajima, Y. Zhang, and T. Hirano, Observation of quadrature squeezing a  $\chi^{(2)}$  nonlinear waveguide using a temporally shaped local oscillator pulse, Opt. Express 16, 10650 (2008).  
[23] F. Kaiser, B. Fedrici, A. Zavatta, V. D'Auria, and S. Tanzilli, A fully guided-wave squeezing experiment for fiber quantum networks, Optica 3, 362 (2016).  
[24] G. Masada, K. Miyata, A. Politi, T. Hashimoto, J. O'Brien, and A. Furusawa, Continuous-variable entanglement on a chip, Nat. Photonics 9, 316 (2015).  
[25] A. Dutt, K. Luke, S. Manipatruni, A.L. Gaeta, P. Nussenzveig, and M. Lipson, On-Chip Optical Squeezing, Phys. Rev. Applied 3, 044005 (2015).  
[26] J. U. Fürst, D. V. Strekalov, D. Elser, A. Aiello, U. L. Andersen, Ch. Marquardt, and G. Leuchs, Quantum Light from a Whispering-Gallery-Mode Disk Resonator, Phys. Rev. Lett. 106, 113901 (2011).  
[27] M. Pysher, R. Bloomer, C.M. Kaleva, T.D. Roberts, P. Battle, and O. Pfister, Broadband amplitude squeezing in a periodically poled  $\mathrm{KTiOPO_4}$  waveguide, Opt. Lett. 34, 256 (2009).  
[28] K.-H. Luo, H. Herrmann, S. Krapick, B. Brecht, R. Ricken, V. Quiring, H. Suche, W. Sohler, and C. Silberhorn, Direct generation of single-longitudinal-mode narrowband photon pairs, New J. Phys. 17, 073039 (2015).  
[29] M. Fontana, K. Chah, M. Aillerie, R. Mouras, and P. Bourson, Optical damage resistance in undoped  $\mathrm{LiNbO_3}$  crystals, Opt. Mater. 16, 111 (2001).  
[30] M. Carrascosa, J. Villaeroel, J. Carnicero, A. Garcia-Cabanes, and J.M. Cabrera, Understanding light intensity thresholds for catastrophic optical damage in  $\mathrm{LiNbO}_3$ , Opt. Express 16, 115 (2008).  
[31] R. Regener and W. Sohler, Loss in low-finesse Ti:  $\mathrm{LiNbO_3}$  optical waveguide resonators, Appl. Phys. B 36, 143 (1985).  
[32] E. D. Black, An introduction to pound-drever-hall laser frequency stabilization, Am. J. Phys. 69, 79 (2001).  
[33] P. K. Lam, T. C. Ralph, B. C. Buchler, D. E. McClelland, H.-A. Bachor, and J. Gao, Optimization and transfer of vacuum squeezing from an optical parametric oscillator, J. Opt. B 1, 469 (1999).  
[34] S. Dwyer et al., Squeezed quadrature fluctuations in a gravitational wave detector using squeezed light, Opt. Express 21, 19047 (2013).  
[35] H. Vahlbruch, S. Chelkowski, B. Hage, A. Franzen, K. Danzmann, and R. Schnabel, Coherent Control of Vacuum Squeezing in the Gravitational-Wave Detection Band, Phys. Rev. Lett. 97, 011101 (2006).