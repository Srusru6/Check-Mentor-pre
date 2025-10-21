# PHYSICS

# Integrated photonic platform for quantum information with continuous variables

Francesco Lenzini $^{1,2}$ , Jiri Janousek $^{3,4}$ , Oliver Thearle $^{3,4}$ , Matteo Villa $^{1}$ , Ben Haylock $^{1}$ , Sachin Kasture $^{1}$ , Liang Cui $^{5}$ , Hoang-Phuong Phan $^{6,7}$ , Dzung Viet Dao $^{6,7}$ , Hidehiro Yonezawa $^{8}$ , Ping Koy Lam $^{4}$ , Elanor H. Huntington $^{3}$ , Mirko Lobino $^{1,6*}$

Integrated quantum photonics provides a scalable platform for the generation, manipulation, and detection of optical quantum states by confining light inside miniaturized waveguide circuits. Here, we show the generation, manipulation, and interferometric stage of homodyne detection of nonclassical light on a single device, a key step toward a fully integrated approach to quantum information with continuous variables. We use a dynamically reconfigurable lithium niobate waveguide network to generate and characterize squeezed vacuum and two-mode entangled states, key resources for several quantum communication and computing protocols. We measure a squeezing level of  $-1.38 \pm 0.04$  dB and demonstrate entanglement by verifying an inseparability criterion  $I = 0.77 \pm 0.02 < 1$ . Our platform can implement all the processes required for optical quantum technology, and its high nonlinearity and fast reconfigurability make it ideal for the realization of quantum computation with time encoded continuous-variable cluster states.

Copyright © 2018 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original U.S. Government Works. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC).

# INTRODUCTION

Integrated quantum photonics (1) has emerged as the ideal platform for the implementation of optical quantum computation (2), communication (3, 4), and sensing protocols (5). By confining light inside miniaturized waveguide circuits, it is possible to generate quantum states of light (6-9), interfere them over waveguide networks (10, 11), and detect them with integrated detectors (12). Integration of these three key operations establishes the stability and scalability of this technology, enabling continuous increase in the complexity and capabilities of these devices (13, 14).

Optical quantum information is most commonly encoded in one of the discrete degrees of freedom [or discrete variables (DVs)] of single photons such as polarization (15) or path (2). This approach enables operations with near-unity gate fidelity (16) but is currently limited by the lack of on-demand single-photon sources and deterministic two-photon quantum gates. The encoding of information on operators that are continuous variables (CVs), such as quadrature amplitudes, offers the advantages of deterministic generation of quantum states and operation at the expense of a higher tendency to imperfect gate fidelities (17). This approach has been demonstrated in several fields, including secure quantum communication (18), quantum-enhanced sensing (19), and quantum information processing (20). Hybrid approaches combining the benefits of DV and CV systems have also been proposed and experimentally demonstrated (21).

While integrated optics provides great stability and scalability to all types of encoding, in CV schemes, it also greatly simplifies the configuration of current experimental setups, replacing phase-locked cavities for generation of squeezed light with single-pass waveguides (6, 22). It also eliminates the need for mode-cleaning cavities for homodyne detection owing to the nearly perfect overlap between optical modes in guiding structures (23-25).

Furthermore, the possibility of achieving broadband generation bandwidths in a single-pass squeezeer (26) and performing fast-switching operations with electrooptically tunable waveguides (15, 27) makes integrated optics an attractive platform for the implementation of frequency (28, 29) or time-multiplexed encoding (30, 31) and fast feedforward operations needed for CV measurement-based quantum computing (32).

Here, we demonstrate a nonlinear and reconfigurable integrated device that generates, actively manipulates, and performs the interferometric stage of homodyne detection on nonclassical light fields. The device is formed by two integrated sources of squeezed vacuum, electrooptically tunable phase shifters, and beam splitters where squeezed vacua can interfere and be characterized. Complemented with photon number-resolving detectors or non-Gaussian ancilla inputs (17), this architecture can enable non-Gaussian operations for universal quantum information processing or hybridization with DV systems (21).

<sup>1</sup>Centre for Quantum Computation and Communication Technology and Centre for Quantum Dynamics, Griffith University, Brisbane, QLD 4111, Australia. <sup>2</sup>Institute of Physics, University of Muenster, 48149 Muenster, Germany. <sup>3</sup>Centre for Quantum Computation and Communication Technology and Research School of Engineering, The Australian National University, Canberra, ACT 2601, Australia. <sup>4</sup>Centre for Quantum Computation and Communication Technology and Department of Quantum Science, Research School of Physics and Engineering, The Australian National University, Canberra, ACT 2601, Australia. <sup>5</sup>College of Precision Instrument and Opto-electronics Engineering, Tianjin University, Tianjin 300072, China. <sup>6</sup>Queensland Micro and Nanotechnology Centre, Griffith University, Brisbane, QLD 4111, Australia. <sup>7</sup>School of Engineering and Built Environment, Griffith University, Brisbane, QLD 4111, Australia. <sup>8</sup>Centre for Quantum Computation & Communication Technology and School of Engineering and Information Technology, The University of New South Wales, Canberra, ACT 2600, Australia.

*Corresponding author. Email: m.lobino@griffith.edu.au

# RESULTS

Figure 1 shows a schematic of the integrated chip and the experimental setup. The device is made of a network of six waveguides patterned on a z-cut lithium niobate substrate by reverse proton exchange (33) (see Materials and Methods for details on the fabrication process).

Two periodically poled waveguides, phase matched approximately  $1550~\mathrm{nm}$ , are used to generate two squeezed vacuum states, which are interfered on a reconfigurable directional coupler (DC1) for the generation of a two-mode CV entangled state (17). Both waveguides have a 2-cm interaction length, extrapolated from the  $0.5\mathrm{-nm}$  full width at half maximum (FWHM) of the second harmonic generation (SHG) efficiency as a function of the pump wavelength (Fig. 2A). This interaction

![](images/975c8c283dda6e13dbf540558ae24991d0fca4c2970f55d84641a7fff13bd96c.jpg)  
Fig. 1. Configuration of the chip and experimental setup. Periodically poled waveguides (1, 2) are the nonclassical light sources. The squeezed vacuum states are manipulated in a reconfigurable directional coupler (DC1) for the generation of two separable squeezed states or a two-mode CV entangled state. DC2 and DC3 are used to separate the pump at  $\sim 777$  nm from the signal at  $\sim 1554$  nm. The rest of the network ( $\phi_{\mathrm{LO1}}$ ,  $\phi_{\mathrm{LO2}}$ , DC4, and DC5) is made of the reconfigurable phase shifters and couplers of the two homodyne detectors.

![](images/0ca7aa8cc038e05f82405554167af2ed492d8377d4d18372a6f3a49b7847598d.jpg)

![](images/4a0ce8bcbb9ebd6687554afce02b3958bc5d0ee1b798620f0a5738eec0228e8a.jpg)

![](images/b46ab29e67cda74bd8383cb0c3f7006049d2cca607af8150021dfd81faf41410.jpg)  
Fig. 2. Generation and homodyne detection of squeezed vacuum states. (A) Measured normalized SHG efficiencies  $P_{2\omega} / P_{\omega}^{2}$  for waveguide 1 (blue points) and waveguide 2 (red points) at  $T = 125^{\circ}\mathrm{C}$  and relative theoretical fit (solid lines). Pump and second harmonic powers are corrected for Fresnel losses at the output facet and propagation losses (see Materials and Methods). The FWHM of the fit  $\mathrm{sinc}^2$  are  $\simeq 0.5$  nm, consistent with a  $\simeq 2$ -cm interaction length. The waveguides have the same normalized conversion efficiency  $\simeq 370\% W^{-1}$  at  $\lambda = 1554.45$  nm. Measurements are performed in the undepleted pump regime, where the SHG power increases quadratically with pump power. The reported SHG efficiencies have a  $\pm 10\%$  relative uncertainty, which is introduced by the error in the power calibration of the used power meters. (B) SR of DC1 (top image) and voltage applied to the LO phase shifters (bottom image) as a function of time. SR measurement is performed by injecting a 1550-nm beam into waveguide 2 and measuring the power at the first output with a photodiode. DC1 electrode is driven with a square wave with 1-kHz frequency and  $\pm 16$ -V amplitude. Distortion of the square signal is due to the limited bandwidth of the voltage amplifier. (C) Noise trace measured from HD1 for a 154-mW pump power. Pump power is measured at the output of the device and corrected for Fresnel losses at the output facet and propagation losses inside the waveguides. Noise variance is calculated on time intervals of 4-μs duration and averaged over 40 sequential traces. Sampling rate is 50 MSPS (mega-sample-per-second). (D) Measured squeezing and antisqueezing levels as a function of pump power for waveguide 1 (blue squares) and waveguide 2 (red circles). Solid lines are the fits made with the function of Eq. 1. Error on the measured noise levels is  $\pm 0.04$  dB. Pump powers are measured at the output of the device and corrected for Fresnel losses at the output facet and propagation losses inside the waveguides. Pump wavelength is  $\lambda_{\mathrm{p}} = 1554.55 / 2$  nm for waveguide 1 and  $\lambda_{\mathrm{p}} = 1554.35 / 2$  nm for waveguide 2.

![](images/805e9d68e2c6bd9ec7f5892a13d5aa0f4fd7f9c2bbc130ab461ee627bc704ac4.jpg)

length corresponds to a 96-nm FWHM bandwidth for the generated squeezed light.

Two directional couplers (DC2 and DC3), designed with a splitting ratio (SR) of 1 (all power coupled into the adjacent waveguide) at  $1550~\mathrm{nm}$ , separate the generated quantum states from the pump beams, which remain confined in the initial waveguides due to the smaller mode field diameter. Balanced homodyne detection is per

formed by mixing the generated signals with two local oscillator (LO) beams in two tunable directional couplers (DC4 and DC5). Electrodes patterned on top of the waveguides are used to scan the phase of the LOs and to tune the SRs of the directional couplers (27). LO phases  $\phi_{\mathrm{LO1}}$  and  $\phi_{\mathrm{LO2}}$  are scanned by  $2\pi$  when a  $\pm 10$ -V waveform is applied (see Fig. 2, B and C), while the SRs of the reconfigurable couplers can be reduced from their no voltage values down to  $\sim 0.005$  with an applied voltage

in the  $\pm 20\mathrm{-V}$  range (see Materials and Methods). The SRs of DC4 and DC5 are tuned at around 0.5 for balanced homodyne detection.

Two-mode CV entanglement is generated by interfering orthogonal squeezed vacuum states from the two periodically poled waveguides on DC1 with an SR tuned at 0.5. Separable squeezed vacuum states are created when the SR of DC1 is set as close as possible to zero (0.005) for implementing the identity operation. Because of imperfections in the waveguide fabrication process, the SRs of DC2 and DC3 were found equal to 0.80 and 0.86, respectively, reducing, in this way, the maximum amount of measurable squeezing. In future implementations, the performance of the filters could be improved by patterning the electrodes with alternating phase mismatch (34) to allow tuning the SR in the full 0 to 1 range.

The master laser is an amplified cavity diode laser, based on a gain chip (35), and tunable in the  $1550\mathrm{-nm}$  wavelength range. The pump beam is obtained by frequency doubling part of the master laser power with a periodically poled potassium titanyl phosphate (PPKTP) crystal in a single-resonant cavity (see Materials and Methods), with the remaining power used as LOs. All the beams are coupled into the chip using a custom-made V-groove array with two central fibers that are single mode at  $775~\mathrm{nm}$  while the remaining fibers are single mode at  $1550~\mathrm{nm}$ . All the output modes are collected by a single lens antireflection (AR) coated at  $1550~\mathrm{nm}$  with  $8\mathrm{-mm}$  focal length and a numerical aperture of 0.5, separated at a large distance from the chip, and sent to a pair of homodyne detectors (HD1 and HD2) with  $99\%$  quantum efficiencies (QEs) by the use of free-space optics. A power meter is used to monitor the power of the pump beams collected from the two central outputs. Electronic filtering is used to select a wide side band from 4 to  $35\mathrm{MHz}$ , which is measured in the time domain with a digital oscilloscope. For generation of CV entanglement, the relative phase of the two pump beams is controlled in free space with a piezoelectric mirror and

the power of the pumps is balanced by the use of free-space optics at the output of the SHG cavity. The second and fifth inputs of the device were unused in this experiment, but in the future may be used to implement displacement operations (17, 21).

The device was first configured for generation and homodyne detection of squeezed vacuum states. The SR of DC1 was set to the minimum value of 0.005, and the phases of LO beams were scanned by approximately  $2\pi$  with a ramp function (see Fig. 2B). To prevent the accumulation of surface charge due to the application of a DC offset, the three directional couplers were modulated by a square function with equal positive and negative amplitudes and a  $1\mathrm{-kHz}$  frequency. Postprocessing on the acquired signal was used to select a 0.4-ms time window centered around the applied square waves for every modulation period. Characterization was carried out by injecting a pump beam into each periodically poled waveguide at a time and measuring the resulting noise levels on the adjacent homodyne detectors. Because of the high operational temperature  $(T = 125^{\circ}\mathrm{C})$  the coupled pump power inside the waveguides can be increased up to  $\simeq 160~\mathrm{mW}$  without any evidence of photorefractive damage.

Figure 2C shows the noise trace from HD1, corresponding to a maximum measured squeezing (antisqueezing) level  $\langle \Delta^2\hat{X}^{-}\rangle = -1.38\pm 0.04\mathrm{dB}$ $(\langle \Delta^{2}\hat{X}^{+}\rangle = 1.98\pm 0.04$  dB) for a pump power  $P = 154~\mathrm{mW}$ . After correcting for  $13\%$  Fresnel losses, which could be eliminated with an AR coating on the output facet, and inefficiencies of the filter  $(\mathrm{SR} = 0.80)$ , we estimate that  $-2.15\pm 0.04$  dB of squeezing is generated in our device. The squeezing and antisqueezing levels measured for both waveguides as a function of pump power are shown in Fig. 2D. The points are fitted using the function (17)

$$
\left\langle \Delta^ {2} \hat {X} ^ {\pm} \right\rangle = \eta e ^ {\pm 2 \mu \sqrt {P}} + 1 - \eta \tag {1}
$$

![](images/184a156720f20f4ae69f1c8d45b09d1bf4155b9a0f8f6f962ffc3fd011be35c0.jpg)

![](images/6562387e825504f724c5d3429be03626b674b80c994dcc3f93e7d1970e487ba2.jpg)

![](images/6a46614b7383a46a24f2bb5f14dbbf40be9ea3c1384cf583365b09c16f69825b.jpg)  
Fig. 3. Generation and characterization of CV entanglement. (A) SR of DC1 (top image) and voltage applied to phase shifters  $\phi_{\mathrm{LO1}}$  (green trace, bottom image) and  $\phi_{\mathrm{LO2}}$  (red trace, bottom image) as a function of time. SR measurement is performed by injecting a 1550-nm beam into waveguide 2 and measuring the power at the first output with a photodiode. DC1 electrode is driven with a square wave at 1-kHz frequency and  $\pm 5.5\text{-V}$  amplitude. Scanning frequency is 1 kHz for  $\phi_{\mathrm{LO1}}$  and 10 kHz for  $\phi_{\mathrm{LO2}}$ . (B) Noise levels measured from HD1 (blue trace) and HD2 (red trace) when the pump beams are in phase. (C) Noise levels measured from HD1 (blue trace) and HD2 (red trace) when the pump beams are out of phase. (D) Noise levels of summed quadratures  $\langle \Delta^2 (\hat{X}_1 + \hat{X}_2)\rangle$  (green trace) and subtracted quadratures  $\langle \Delta^2 (\hat{X}_1 - \hat{X}_2)\rangle$  (red trace) when the pump beams are out of phase. Noise variance is calculated on time intervals of 2.5-μs duration and averaged over 10 sequential traces. Sampling time is 20 ns. Measurements are performed with two pump beams with  $P = 122\mathrm{mW}$  and  $\lambda_{\mathrm{P}} = 1554.45 / 2\mathrm{nm}$ .

![](images/b69fe55acd7bad273f9415187386d5358370d2c4ee47bd89eccd3ba1db78cc0b.jpg)

where  $\eta$  is the overall detection efficiency. Results of the fit give  $\mu_{1} = 0.030 \pm 0.001 \, \mathrm{mW}^{-1/2}$ ,  $\mu_{2} = 0.027 \pm 0.001 \, \mathrm{mW}^{-1/2}$ ,  $\eta_{1} = 0.52 \pm 0.02$ , and  $\eta_{2} = 0.54 \pm 0.02$ , against estimated  $\eta_{1} = 0.55$  and  $\eta_{2} = 0.6$  for  $0.14 \, \mathrm{dB/cm}$  propagation losses (see Materials and Methods). We note that  $\eta_{1}$  is found compatible within the  $95\%$  confidence interval, with the estimated value. For waveguide 2, the extra  $0.06$  inefficiency is likely introduced by imperfections in the waveguides along the path of the generated signals. We note that the values of  $\mu_{1}$  and  $\mu_{2}$  calculated from the fits are approximately three times smaller than the one reported in (24) using a similar technology. However the waveguide used in this reference has a longer interaction length ( $4 \, \mathrm{cm}$ ) and higher propagation losses ( $\simeq 0.4 \, \mathrm{dB/cm}$ ), which would significantly lower the generated squeezing level in a monolithically integrated network.

Next, the device was configured for the generation and characterization of CV entanglement between the two spatial modes after DC1. The SR of DC1 was set to 0.50, and the phases of the two LO beams were scanned by approximately  $\pi$  at  $1\mathrm{kHz}$  for  $\phi_{\mathrm{LO1}}$  and  $10\mathrm{kHz}$  for  $\phi_{\mathrm{LO2}}$  (see Fig. 3A). The phase of pump 1 was scanned simultaneously by approximately  $2\pi$  at a much lower speed  $(50\mathrm{Hz})$  using a piezoelectric mirror (see Fig. 1). Entanglement was verified using the inseparability criterion for Gaussian states (36)

$$
I = \sqrt {\min  \left[ \left\langle \Delta^ {2} \left(\hat {X} _ {1} ^ {+} \pm \hat {X} _ {2} ^ {+}\right) \right\rangle \right] \times \min  \left[ \left\langle \Delta^ {2} \left(\hat {X} _ {1} ^ {-} \pm \hat {X} _ {2} ^ {-}\right) \right\rangle \right]} <   1 \tag {2}
$$

where we use the product form of (36), and  $X^{-}$  and  $X^{+}$  are, respectively, squeezed and antisqueezed quadratures when the pump beams have a  $\pi$  phase shift. The homodyne detection bases used for the measurement of  $\hat{X}_1^{\pm}$  and  $\hat{X}_2^{\pm}$  are determined from the positions of the squeezed and antisqueezed quadratures when the pump beams are in phase.

Figure 3 (B to D) shows the results of the measurements for a  $122\mathrm{-mW}$  pump power coupled in each waveguide, close to the maximum attainable power with our setup. When the pump beams are in phase (Fig. 3B), the device generates two separable squeezed states with similar squeezing and antisqueezing levels,  $\langle \Delta^2\hat{X}_1^- \rangle = -1.16 \pm 0.06$  dB  $(\langle \Delta^2\hat{X}_1^+ \rangle = 1.71 \pm 0.06$  dB) for HD1 and  $\langle \Delta^2\hat{X}_2^- \rangle = -1.11 \pm 0.06$  dB  $(\langle \Delta^2\hat{X}_2^+ \rangle = 1.65 \pm 0.06$  dB) for HD2. When the pump beams have a  $\pi$  relative phase (Fig. 3C), as expected for an entangled state, we observed phase-independent and constant noise levels  $\langle \Delta^2\hat{X}_1 \rangle = 0.53 \pm 0.20$  dB for HD1 and  $\langle \Delta^2\hat{X}_2 \rangle = 0.54 \pm 0.20$  dB for HD2. Conversely, variance of summed and subtracted quadratures (green and red traces in Fig. 3D) shows a phase-sensitive behavior with correlations below the equivalent shot-noise level resulting from the combination of the two homodyne currents (see Materials and Methods). From the data of Fig. 3D, we calculated  $\min[\langle \Delta^2(\hat{X}_1^+ \pm \hat{X}_2^+)\rangle] = -1.19 \pm 0.12$  dB and  $\min[\langle \Delta^2(\hat{X}_1^- \pm \hat{X}_2^-)\rangle] = -1.07 \pm 0.12$  dB corresponding to  $I = 0.77 \pm 0.02 < 1$ , which satisfies the inseparability criterion by 11 SEs.

# DISCUSSION

In conclusion, we demonstrated the generation, manipulation, and characterization of nonclassical quantum states of light in a monolithically integrated device. We have shown the reconfigurability of our technology by generating squeezed vacua and CV quadrature entanglement in two separate spatial modes. The device was fabricated using the reverse proton exchange technique, which enables propagation losses as low as  $0.1\mathrm{dB / cm}$ , a crucial parameter for the implementation of high-fidelity CV quantum optics protocols (17). We

calculated that using a pulsed laser and reducing the average pump power, which is the main parameter responsible for photorefractive damage (22), our fabrication technology could reach  $\sim 7$  dB of squeezing with a  $500\mathrm{-mW}$  peak power and a  $4\mathrm{-cm}$  interaction length.

Another important feature of our chip technology is the possibility of fast light manipulation. While in our implementation, the modulation of the electrodes was kept at low frequencies ( $\leq 10\mathrm{kHz}$ ) to avoid the introduction of unwanted amplitude noise in the measured side-band interval (4 to  $35\mathrm{MHz}$ ), in the future it will be of interest to use high-bandwidth homodyne detectors to raise this modulation speed and demonstrate fast-switching operations in the gigahertz regime for measurement-based quantum computation.

Another important feature of proton-exchanged waveguides is the high coupling efficiency, around  $90\%$ , with optical fibers (33). This property is important in quantum communication applications, which may require the use of two separate chips for the generation and detection of light that are connected via optical fiber links.

Furthermore, recently developed low-loss, high-confinement ridge waveguides in lithium niobate (37) can potentially generate more than  $10\mathrm{dB}$  of squeezing with this same material, enabling CV entanglement with a noise reduction comparable to state-of-the-art experiments performed with bulk optical parametric oscillators (38). The use of these waveguides can also provide a technology with a footprint similar to the silicon-on-insulator platform, which would enable integration of more functionalities, such as a SHG stage (22), on the same chip.

# MATERIALS AND METHODS

# Fabrication of the chip

Waveguides were fabricated with a  $1.85\text{-}\mu \mathrm{m}$  proton exchange depth followed by annealing for 8 hours at  $328^{\circ}\mathrm{C}$  and reverse proton exchange for 10 hours at the same temperature. Inputs of the periodically poled waveguides were designed with a channel width of  $2.5\mu \mathrm{m}$  to get nearly single-mode operation at  $775~\mathrm{nm}$  and inject efficiently the pump beam into the fundamental mode of the waveguides. Channel width at the beginning of the poling region was increased to  $8\mu \mathrm{m}$  with a  $7\mathrm{-mm}$  adiabatic taper to work in a noncritical condition for quasi-phase matching (39). After the poling region, the channel widths were decreased to  $6\mu \mathrm{m}$  with a second adiabatic taper of  $1.5\mathrm{mm}$  in length to get single-mode operation at  $1550~\mathrm{nm}$ . S-bends were designed with a sinusoidal function and a minimum bend radius of  $40~\mathrm{mm}$ . Separation between waveguide centers at the input and the output of the device was set to  $127\mu \mathrm{m}$  to match the standard pitch of fiber V-groove arrays. To prevent back reflections into the waveguides and cavity effects inside the chip, the output facet was polished at  $8^{\circ}$ . Total length of the chip was  $62~\mathrm{mm}$ . Light was coupled into the HDs using bulk optical elements to avoid the coupling losses with a second fiber array. In future implementations, the deposition of an AR coating on the output facet would enable polishing the chip at a  $0^{\circ}$  angle and reduction of the Fresnel losses.

The poling pattern was generated by standard electric field poling with a period  $\Lambda = 16.12\mu \mathrm{m}$  and a 50:50 duty cycle. After poling and waveguide fabrication, aluminum electrodes were realized on a  $200\mathrm{-nm}$ -thick  $\mathrm{SiO}_2$  buffer layer to prevent optical absorption from the metal. Aluminum thickness was  $250~\mathrm{nm}$ , while electrodes were patterned using electron beam lithography and wet etching.

Directional couplers were designed with separation between waveguide centers of  $11.3\mu \mathrm{m}$  for DC1, DC4, and DC5, and  $10.6\mu \mathrm{m}$  for DC2

and DC3. The lengths of the directional couplers were  $6.1\mathrm{mm}$  for DC1 and  $3.5\mathrm{mm}$  for DC2, DC3, DC4, and DC5. For DC2 and DC3, we chose a smaller center-to-center separation to achieve an SR of 1 while minimizing the length of the couplers. Electrodes (12 mm long) act as phase shifters on the LO arms. At a zero applied voltage, the SRs of the reconfigurable couplers were 0.72 for DC1, 0.85 for DC4, and 0.75 for DC5. Application of a voltage to the electrodes induced a mismatch between the propagation constants of the coupled waveguides, which reduced the SR of the DCs. For this reason, both positive and negative voltages reduced the SRs below their zero-voltage values. Application of a square modulation with positive and negative amplitudes resulted in typical traces such as the one reported in Fig. 2B.

The isolation of the pump beams from the homodyne detectors was achieved by DC2 and DC3 and a dichroic mirror after the chip for a total of 40-dB isolation. Furthermore, since the output facet of the chip was angled polished, pump and signal beams were refracted in slightly different directions, and only  $1550\mathrm{-nm}$  light gets coupled into the HDs. During the experiments, the shot-noise level was measured while blocking the pump beam with a chopper.

To prevent photorefractive damage, the chip was bonded with an ultraviolet curing glue to a custom-made aluminum oven and heated at  $125^{\circ}\mathrm{C}$ . Photorefractive effect must be avoided because it can locally change phase-matching wavelength of the waveguide and reduce the interaction length of the down conversion process, thus reducing the maximum attainable level of squeezing in our device. Two printed circuit boards with SubMiniature version A connectors were mounted on the sides of the oven and wire bonded to the electrodes to control the voltage applied to phase shifters and directional couplers.

# Propagation losses

Transmission of the waveguides at the signal wavelength was tested on the second and fifth waveguides and at the pump wavelength on the two central inputs. Transmission of the device corrected for Fresnel losses was found equal to  $61\%$  at  $1550~\mathrm{nm}$  and to  $40\%$  at  $775~\mathrm{nm}$ . From the numerical calculation of the mode overlap between waveguides and single-mode fibers (33), we estimated  $0.14\mathrm{-dB / cm}$  propagation losses at the signal wavelength and  $0.55\mathrm{-dB / cm}$  propagation losses at the pump wavelength. Propagation losses at the signal wavelength were not directly measurable from the central inputs, since  $1550\mathrm{-nm}$  beams were only weakly guided in the first tapered section of the periodically poled waveguides.

# Detection efficiencies

Estimation of the detection efficiencies  $\eta_{1}$  and  $\eta_{2}$  from Eq. 1 takes into account  $0.14\mathrm{-dB / cm}$  propagation losses calculated from the center of the periodically poled waveguides, a  $0.5\%$  loss introduced by the first directional coupler,  $20\%$  (for waveguide 1) and  $14\%$  (for waveguide 2) losses introduced by the pump filters DC2 and DC3,  $13\%$  Fresnel losses at the output facet, a  $99\%$  QE, and a 17-dB shot-noise clearance measured for a 4-mW LO power.

# Shot-noise levels

To evaluate the shot-noise levels, we used a motorized optical chopper blocking periodically the power of the pump beams. For each data acquisition, the shot-noise variance was calculated on five time windows with 0.4-ms duration. SE in the evaluation of the shot-noise levels was estimated equal to  $\pm 0.025$  dB and added to all the uncertainties reported in the paper.

# Driving voltage

The electrodes on the chip were driven by three dual-channel arbitrary waveform generators. The waveform generators were operated in burst mode with a common trigger generated by a photodiode at the output of the optical chopper. Phase shifters, DC5, and DC1 (for generation of CV entanglement), required voltages in the  $\pm 10\mathrm{-V}$  range and were driven directly by the waveform generators. DC4 and DC1 (for generation and homodyne detection of squeezed vacuum) required voltages of  $\pm 18$  and  $\pm 16\mathrm{V}$ , respectively, generated with two voltage amplifiers. Low-pass filters from DC to  $1.9\mathrm{MHz}$  were used to suppress unwanted amplitude noise introduced by the driving voltage in the measured side bands.

# Squeezing and antisqueezing levels

Squeezing and antisqueezing levels were evaluated by fitting each noise trace with the function

$$
\langle \Delta^ {2} \hat {X} \rangle = \langle \Delta^ {2} \hat {X} ^ {+} \rangle \cos^ {2} (a t + \phi) + \langle \Delta^ {2} \hat {X} ^ {-} \rangle \sin^ {2} (a t + \phi)
$$

where  $t$  is the acquisition time and  $a$  and  $\phi$  are fitting parameters. Uncertainties reported in the paper are the SEs in the evaluation of the coefficients calculated by the least squares fitting procedure.

# Inseparability criterion

Variance of summed and subtracted quadratures was calculated from the photocurrents  $i_{1}$  and  $i_{2}$  measured from the two homodyne detectors as<sup>17</sup>

$$
\langle \Delta^ {2} (\hat {X} _ {1} \pm \hat {X} _ {2}) \rangle = \left\langle \Delta^ {2} \left(\frac {i _ {1}}{\sqrt {2 \langle \Delta^ {2} \hat {X} _ {\mathrm {S N 1}} \rangle}} \pm \frac {i _ {2}}{\sqrt {2 \langle \Delta^ {2} \hat {X} _ {\mathrm {S N 2}} \rangle}}\right) \right\rangle
$$

where  $\langle \Delta^2\hat{X}_{\mathrm{SN1}}\rangle$  and  $\langle \Delta^2\hat{X}_{\mathrm{SN2}}\rangle$  are the shot-noise levels of the two homodyne detectors. Noise variances,  $\langle \Delta^{2}(\hat{X}_{1}^{+}\pm \hat{X}_{2}^{+})\rangle$  and  $\langle \Delta^2 (\hat{X}_1^- \pm \hat{X}_2^-)\rangle$  were calculated by averaging four points centered around the squeezed and antisqueezed quadrature positions  $X_{1}^{+}$ $X_{2}^{+}$  and  $X_{1}^{-},X_{2}^{-}$ . SE in the evaluation of the noise levels was estimated as

$$
\mathrm {S E} = \frac {\sigma_ {X _ {1 , 2}}}{\sqrt {4}}
$$

where  $\sigma_{X_{1,2}}$  is the SD of the noise traces measured on each homodyne detector. Because of the finite  $\phi_{\mathrm{LO2}}$  scanning speed, the squeezed  $(X_1^-,X_2^-)$  and antisqueezed  $(X_1^+,X_2^+)$  quadrature positions cannot be measured at exactly the same time on the two HDs. For this reason, the quadratures  $X_{1}^{-},X_{1}^{+}$  used for the calculation of the inseparability criterion have an offset of  $-0.09$  and  $-0.10$  rad, respectively, from the squeezed and antisqueezed quadrature positions determined when the pump beams are in phase. We point out that the two quadratures are orthogonal within an offset, which is smaller than the error in the quadrature positions (±0.02 rad) determined by fitting the data of Fig. 2B. Thus, the measured data still satisfy the inseparability criterion, which is generally valid for any set of orthogonal quadratures.

We further note that for an EPR (Einstein-Podolsky-Rosen) state, the inseparability criterion is not only satisfied for squeezed and antisqueezed quadratures, but for several sets of rotated orthogonal

quadratures. For instance, if  $\langle \Delta^2 (\hat{X}_1^+ +\hat{X}_2^+)\rangle$  and  $\langle \Delta^2 (\hat{X}_{1 - } - \hat{X}_{2 - })\rangle$  display correlations below the shot-noise levels, the same will hold for

$$
\hat {X} _ {1} = \hat {X} _ {1} ^ {-} \cos (\theta) + \hat {X} _ {1} ^ {+} \sin (\theta)
$$

$$
\hat {P} _ {1} = - \hat {X} _ {1} ^ {-} \sin (\theta) + \hat {X} _ {1} ^ {+} \cos (\theta)
$$

$$
\hat {X} _ {2} = \hat {X} _ {2} ^ {-} \cos (- \theta) + X _ {2} ^ {+} \sin (- \theta)
$$

$$
\hat {P} _ {2} = - \hat {X} _ {2} ^ {-} \sin (- \theta) + \hat {X} _ {2} ^ {+} \cos (- \theta)
$$

This explains why the data reported in Fig. 3D show correlations below the shot-noise level for several measurement bases.

# Balanced homodyne detection

Balanced homodyne detection provides a phase-sensitive measurement of a quantum state. To find the variance of an arbitrary frequency dependant quadrature operator  $\hat{X}_{\mathrm{sig}}^{\phi}$  of the signal field, we interfered the signal beam on a 50/50 beamsplitter (BS) with a bright LO beam with a relative phase  $\phi$ . The outputs from the BS were coupled to a pair of photodetectors, and the difference of the photocurrents was recorded. Assuming that the power of LO is much higher than that of the signal beam, the effect of LO is to rotate the coherent amplitudes of the two BS outputs, allowing measurement of an arbitrary state quadrature.

To achieve a calibrated quadrature measurement of the variance of the input state  $V_{\mathrm{sig}}^{\phi}$ , we measured the variance of the difference of the BS photocurrents  $V_{\mathrm{diff}}$  and blocked the input state (but not the LO beam). In this case, it is a vacuum state entering the BS input port, and hence we can normalize the variance by assigning  $V_{\mathrm{sig|blocked}} = 1$  for any  $\phi$  and any side-band frequency. The ratio of the variances with the input signal unblocked and blocked provided a calibrated measurement of  $V_{\mathrm{sig}}^{\phi}$ , i.e.,  $V_{\mathrm{dif|unblocked}} / V_{\mathrm{dif|blocked}} = V_{\mathrm{sig}}^{\phi}$ , where the relative phase between the signal and LO beam defines the measured quadrature. A review of this topic can be found in (40).

# Homodyne detectors

The homodyne detectors (40) used in this experiment used two matched photodetectors with custom-ordered photodiodes from Laser Components with efficiencies of  $>99\%$  and dark currents of  $>20~\mathrm{pA}$ . Each photodetector was in a dual amplifier configuration. The first stage used a dc-coupled transimpedance amplifier to amplify the photocurrent using the op-amp AD829, with a transimpedance gain of 3000. The signal was then split in two using a resistor network for ac- and dc-coupled channels, which may decrease the overall measured signal but does not introduce extra noise. The side bands containing the measurements were present in the ac signal, and the dc signal was used to monitor the detector. The ac path was filtered with a passive high-pass filter with a corner frequency of  $100\mathrm{kHz}$  and then amplified with a gain of 20 using another AD829. The dc-coupled signal was amplified and used for monitoring. The noise floor of the ac-coupled signals from each detector in a homodyne detector was matched using the compensation capacitor on the transimpedance amplifier. The ac signals were matched in phase using cable lengths and then subtracted to get the homodyne signal. While not really flexible, this solution represents a more broadband alternative to electronic phase shifters. The 3-dB bandwidth of the homodyne detectors was measured to be  $21\mathrm{MHz}$ , and with a LO power of  $4\mathrm{mW}$ , they achieved a dark noise clearance of  $17\mathrm{dB}$  below shot noise.

# SHG cavity

The SHG cavity is a free-space bow-tie configuration using a PPKTP nonlinear crystal. The cavity consisted of two high-reflectivity (HR) concave mirrors at  $1550\mathrm{nm}$  with a radius of curvature  $= 50~\mathrm{mm}$  and two plane mirrors. The first plane mirror, input coupler (IC), was a partially reflecting mirror at  $1550\mathrm{nm}$ , and the second was an HR steering mirror attached to a piezo actuator. The cavity was locked on resonance using Pound-Drever-Hall technique. All mirrors were AR coated at the SHG wavelength. The cavity formed a beam waist of radius of approximately  $27\mu \mathrm{m}$  between the two concave mirrors, where a  $15\mathrm{-mm}$ -long PPKTP crystal was aligned. This configuration maximized the nonlinear conversion as detailed by the Boyd-Kleinman theory. The PPKTP crystal was housed in an oven and temperature stabilized around the optimum phase-matching temperature of  $40^{\circ}\mathrm{C}$  using a Peltier element. Both faces of the crystal were wedged and AR coated at both wavelengths to minimize an intracavity parasitic interference. One watt of fundamental optical power was injected through IC into the cavity and converted into the SHG wavelength with  $80\%$  efficiency. The SHG field exited the system through one of the concave mirrors and was subsequently coupled into an optical fiber.

# REFERENCES AND NOTES

1. S. Tanzilli, A. Martin, F. Kaiser, M. P. de Micheli, O. Alibart, D. B. Ostrowsky, On the genesis and evolution of integrated quantum optics. *Laser Photon. Rev.* 6, 115-143 (2012).  
2. A. Politi, J. C. F. Matthews, J. L. O'Brien, Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
3. P. Zhang, K. Aungskunsiri, E. Martin-Lopez, J. Wabnig, M. Lobino, R. W. Nock, J. Munns, D. Bonneau, P. Jiang, H. W. Li, A. Laing, J. G. rarity, A. O. Niskanen, M. G. Thompson, J. L. O'Brien, Reference-frame-independent quantum-key-distribution server with a telecom tether for an on-chip client. Phys. Rev. Lett. 112, 130501 (2014).  
4. A. Orieux, E. Diamanti, Recent advances on integrated quantum communications. J. Opt. 18, 083002 (2016).  
5. A. Crespi, M. Lobino, J. C. F. Matthews, A. Politi, C. R. Neal, R. Ramponi, R. Osellame, J. L. O'Brien, Measuring protein concentration with entangled photons. Appl. Phys. Lett. 100, 233704 (2012).  
6. M. E. Anderson, M. Beck, M. G. Raymer, J. D. Bierlein, Quadrature squeezing with ultrashort pulses in nonlinear-optical waveguides. Opt. Lett. 20, 620-622 (1995).  
7. H. Jin, F. M. Liu, P. Xu, J. L. Xia, M. L. Zhong, Y. Yuan, J. W. Zhou, Y. X. Gong, W. Wang, S. N. Zhu, On-chip generation and manipulation of entangled photons based on reconfigurable lithium-niobate waveguide circuits. Phys. Rev. Lett. 113, 103601 (2014).  
8. H. Takesue, Y. Tokura, H. Fukuda, T. Tsuchizawa, T. Watanabe, K. Yamada, S.-I. Itabashi, Entanglement generation using silicon wire waveguide. Appl. Phys. Lett. 91, 201108 (2007).  
9. T. Nosaka, B. K. Das, M. Fujimura, T. Suhara, Cross-polarized twin photon generation device using quasi-phase matched  $\mathrm{LiNbO_3}$  waveguide. IEEE Photonics Technol. Lett. 18, 124-126 (2006).  
10. J. W. Silverstone, D. Bonneau, K. Ohira, N. Suzuki, H. Yoshida, N. Iizuka, M. Ezaki, C. M. Natarajan, M. G. Tanner, R. H. Hadfield, V. Zwiller, G. D. Marshall, J. G. Parity, J. L. O'Brien, M. G. Thompson, On-chip quantum interference between silicon photon-pair sources. Nat. Photonics 8, 104-108 (2014).  
11. C. Taballione, T. A. W. Wolterink, J. L. A. Eckstein, B. A. Bell, R. Grootjans, I. Visscher, D. Geskus, C. G. H. Roeloffzen, J. J. Renema, I. A. Walmsley, P. W. H. Pinkse, K.-J. Boller, 8x8 Programmable Quantum Photonic Processor based on Silicon Nitride Waveguides. arXiv:1805.10999 [quant-ph] (2018).  
12. W. H. P. Pernice, C. Schuck, O. Minaeva, M. Li, G. N. Goltzman, A. V. Sergienko, H. X. Tang, High-speed and high-efficiency travelling wave single-photon detectors embedded in nanophotonic circuits. Nat. Commun. 3, 1325 (2012).  
13. J. Carolan, C. Harrold, C. Sparrow, E. Martin-López, N. J. Russell, J. W. Silverstone, P. J. Shadbolt, N. Matsuda, M. Oguma, M. Itoh, G. D. Marshall, M. G. Thompson, J. C. F. Matthews, T. Hashimoto, J. L. O'Brien, A. Laing, Universal linear optics. Science 349, 711-716 (2015).  
14. J. Wang, S. Paesani, Y. Ding, R. Santagati, P. Skrzypczyk, A. Salavrakos, J. Tura, R. Augusiak, L. Mančinska, D. Bacco, D. Bonneau, J. W. Silverstone, Q. Gong, A. Acin, K. Rottwitt, L. K. Oxenlöwe, J. L. O'Brien, A. Laing, M. G. Thompson, Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).

15. D. Bonneau, M. Lobino, P. Jiang, C. M. Natarajan, M. G. Tanner, R. H. Hadfield, S. N. Dorenbos, V. Zwiller, M. G. Thompson, J. L. O'Brien, Fast path and polarization manipulation of telecom wavelength single photons in lithium niobate waveguide devices. Phys. Rev. Lett. 108, 053601 (2012).  
16. A. Laing, A. Peruzzo, A. Politi, M. R. Verde, M. Halder, T. C. Ralph, M. G. Thompson, J. L. O'Brien, High-fidelity operation of quantum photonic circuits. Appl. Phys. Lett. 97, 211109 (2010).  
17. S. L. Braunstein, P. van Loock, Quantum information with continuous variables. Rev. Mod. Phys. 77, 513-577 (2005).  
18. P. Jouguet, S. Kunz-Jacques, A. Leverrier, P. Grangier, E. Diamanti, Experimental demonstration of long-distance continuous-variable quantum key distribution. Nat. Photonics. 7, 378-381 (2013).  
19. The LIGO Scientific Collaboration, Enhanced sensitivity of the LIGO gravitational wave detector by using squeezed states of light. Nat. Photonics 7, 613-619 (2013).  
20. T. Aoki, G. Takahashi, T. Kajiya, J.-I. Yoshikawa, S. L. Braunstein, P. van Loock, A. Furusawa, Quantum error correction beyond qubits. Nat. Phys. 5, 541-546 (2009).  
21. S. Takeda, T. Mizuta, M. Fuwa, P. van Loock, A. Furusawa, Deterministic quantum teleportation of photonic quantum bits by a hybrid technique. Nature 500, 315-318 (2013).  
22. G. S. Kanter, P. Kumar, R. V. Roussev, J. Kurz, K. R. Parameswaran, M. M. Fejer, Squeezing in a  $\mathrm{LiNbO_3}$  integrated optical waveguide circuit. Opt. Express 10, 177-182 (2002).  
23. G. Masada, K. Miyata, A. Politi, T. Hashimoto, J. L. O'Brien, A. Furusawa, Continuous-variable entanglement on a chip. Nat. Photonics. 9, 316-319 (2015).  
24. F. Kaiser, B. Fedrici, A. Zavatta, V. D'Auria, S. Tanzilli, A fully guided-wave squeezing experiment for fiber quantum networks. Optica 3, 362-365 (2016).  
25. F. Raffaelli, G. Ferranti, D. H. Mahler, P. Sibson, J. E. Kennard, A. Santamato, G. Sinclair, D. Bonneau, M. G. Thompson, J. C. F. Matthews, An on-chip homodyne detector for measuring quantum states and generating random numbers. Quantum Sci. Technol. 3, 025003 (2016).  
26. K.-I. Yoshino, T. Aoki, A. Furusawa, Generation of continuous-wave broadband entangled beams using periodically poled lithium niobate waveguides. Appl. Phys. Lett. 90, 041111 (2007).  
27. F. Lenzini, B. Haylock, J. C. Loredo, R. A. Abrahao, N. A. Zakaria, S. Kasture, I. Sagnes, A. Lemaitre, H.-P. Phan, D. V. Dao, P. Senellart, M. P. Almeida, A. G. White, M. Lobino, Active demultiplexing of single photons from a solid-state source. *Laser Photon.* Rev. **11**, 1600297 (2017).  
28. M. Chen, N. C. Menicucci, O. Pfister, Experimental realization of multipartite entanglement of 60 modes of a quantum optical frequency comb. Phys. Rev. Lett. 112, 120505 (2014).  
29. Y. Cai, J. Roslund, G. Ferrini, F. Arzani, X. Xu, C. Fabre, N. Treps, Multimode entanglement in reconfigurable graph states using optical frequency combs. Nat. Commun. 8, 15645 (2017).  
30. N. C. Menicucci, Temporal-mode continuous-variable cluster states using linear optics. Phys. Rev. A 83, 062314 (2011).  
31. S. Yokoyama, R. Ukai, S. C. Armstrong, C. Sornphiphathphong, T. Kaji, S. Suzuki, J.-I. Yoshikawa, H. Yonezawa, N. C. Menicucci, A. Furusawa, Ultra-large-scale continuous-variable cluster states multiplexed in the time domain. Nat. Photonics 7, 982-986 (2013).  
32. N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, M. A. Nielsen, Universal quantum computation with continuous-variable cluster states. Phys. Rev. Lett. 97, 110501 (2006).

33. F. Lenzini, S. Kasture, B. Haylock, M. Lobino, Anisotropic model for the fabrication of annealed and reverse proton exchanged waveguides in congruent lithium niobate. Opt. Express 23, 1748-1756 (2015).  
34. H. Kogelnik, R. Schmidt, Switched directional couplers with alternating  $\Delta B$ . IEEE J. Quantum Electron. 12, 396-401 (1976).  
35. S. Bennetts, G. D. McDonald, K. S. Hardman, J. E. Debs, C. C. N. Kuhn, J. D. Close, N. P. Robins, External cavity diode lasers with 5kHz linewidth and 200nm tuning range at  $1.55\mu \mathrm{m}$  and methods for linewidth measurement. Opt. Express. 22, 10642-10654 (2014).  
36. W. P. Bowen, R. Schnabel, P. K. Lam, T. C. Ralph, Experimental investigation of criteria for continuous variable entanglement. Phys. Rev. Lett. 90, 043601 (2003).  
37. M. Zhang, C. Wang, R. Cheng, A. Shams-Ansari, M. Loncar, Monolithic ultra-high-Q lithium niobate microring resonator. Optica 4, 1536-1537 (2017).  
38. D. D. Brown, H. Miao, C. Collins, C. Mow-Lowry, D. Tóryra, A. Freise, Broadband sensitivity enhancement of detuned dual-recycled Michelson interferometers with EPR entanglement. Phys. Rev. D. 96, 062003 (2017).  
39. K. R. Parameswaran, R. K. Route, J. R. Kurz, R. V. Roussev, M. M. Fejer, M. Fujimura, Highly efficient second-harmonic generation in buried waveguides formed by annealed and reverse proton exchange in periodically poled lithium niobate. Opt. Lett. 27, 179-181 (2002).  
40. A. I. Lvovsky, M. G. Raymer, Continuous-variable optical quantum-state tomography. Rev. Mod. Phys. 81, 299-332 (2009).

Acknowledgments: We thank N. Robins for lending us the laser. Funding: This work was supported by the Australian Research Council (ARC) Centre of Excellence for Quantum Computation and Communication Technology (CE170100012) and the Griffith University Research Infrastructure Program. B.H. and M.V. are supported by the Australian Government Research Training Program Scholarship. This work was performed in part at the Queensland node of the Australian National Fabrication Facility, a company established under the National Collaborative Research Infrastructure Strategy to provide nano- and microfabrication facilities for Australia's researchers. Author contributions: F.L., J.J., and L.C. performed the experimental measurements. F.L., S.K., B.H., and M.V. designed and fabricated the integrated device. J.J. and O.T. designed and built the SHG cavity and homodyne detectors. H.-P.P. performed the electrode wire bonding. D.V.D., H.Y., P.K.L., E.H.H., and M.L. supervised the project. F.L. and M.L. wrote the manuscript with contributions from all authors. Competing interest: The authors declare that they have no competing interest. Data and materials availability: All data needed to evaluate the conclusions in the paper are present in the paper. Additional data related to this paper may be requested from the authors.

Submitted 19 April 2018

Accepted 7 November 2018

Published 7 December 2018

10.1126/sciadv.aat9331

Citation: F. Lenzini, J. Janousek, O. Thearle, M. Villa, B. Haylock, S. Kasture, L. Cui, H.-P. Phan, D. V. Dao, H. Yonezawa, P. K. Lam, E. H. Huntington, M. Lobino, Integrated photonic platform for quantum information with continuous variables. Sci. Adv. 4, eaat9331 (2018).

# Science Advances

# Integrated photonic platform for quantum information with continuous variables

Francesco Lenzini, Jiri Janousek, Oliver Thearle, Matteo Villa, Ben Haylock, Sachin Kasture, Liang Cui, Hoang-Phuong Phan, Dzung Viet Dao, Hidehiro Yonezawa, Ping Koy Lam, Elanor H. Huntington and Mirko Lobino

Sci Adv 4 (12), eaat9331.

DOI: 10.1126/sciadv.aat9331

# ARTICLE TOOLS

http://advances.sciencemag.org/content/4/12/eaat9331

# REFERENCES

This article cites 39 articles, 3 of which you can access for free http://advances.sciencemag.org/content/4/12/eaat9331#BIBL

# PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service