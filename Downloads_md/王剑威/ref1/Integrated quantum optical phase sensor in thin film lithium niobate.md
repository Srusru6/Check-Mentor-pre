# Integrated quantum optical phase sensor in thin film lithium niobate

Received: 24 February 2023

Accepted: 19 April 2023

Published online: 08 June 2023

Check for updates

Hubert S. Stokowski  $①$ , Timothy P. McKenna  $^2$ , Taewon Park  $^{1,3}$ , Alexander Y. Hwang  $^1$ , Devin J. Dean  $①$ , Oguz Tolga Celik  $^{1,3}$ , Vahid Ansari  $①$ , Martin M. Fejer  $^1$  & Amir H. Safavi-Naeini  $①$

The quantum noise of light, attributed to the random arrival time of photons from a coherent light source, fundamentally limits optical phase sensors. An engineered source of squeezed states suppresses this noise and allows phase detection sensitivity beyond the quantum noise limit (QNL). We need ways to use quantum light within deployable quantum sensors. Here we present a photonic integrated circuit in thin-film lithium niobate that meets these requirements. We use the second-order nonlinearity to produce a squeezed state at the same frequency as the pump light and realize circuit control and sensing with electro-optics. Using 26.2 milliwatts of optical power, we measure  $(2.7 \pm 0.2)\%$  squeezing and apply it to increase the signal-to-noise ratio of phase measurement. We anticipate that photonic systems like this, which operate with low power and integrate all of the needed functionality on a single die, will open new opportunities for quantum optical sensing.

Squeezed states of light exhibit fluctuations in their quadrature amplitude below that of the quantum vacuum<sup>1</sup>. This property makes them indispensable resources for increasing the sensitivity of optical measurements. In interferometry with classical light, signal-to-noise-ratio scales as  $\sqrt{N}$  with the total number of detected photons  $N$ . As a result, the imprecision in determining the optical phase, or phase sensitivity, follows  $1 / \sqrt{N}$ , referred to as the quantum noise limit (QNL). In this case, the signal-to-noise-ratio (SNR) is limited by photon shot noise. To increase the SNR within the confines of the QNL, we must increase  $N$  by using more optical power or extending the measurement time. These approaches are often undesirable or impossible due to technical or fundamental limitations. Intriguingly, the QNL can be overcome by injecting squeezed states of light into the dark port of the interferometer<sup>2</sup>. Ultimately, this approach may lead to a truly quantum-limited Heisenberg scaling  $1 / N$  of sensitivity<sup>2-4</sup>. Over the past forty years, impressive efforts have been put into designing squeezed light sources and integrating them into gravitational wave detectors. These detectors now routinely obtain quantum-enhanced sensitivity exceeding  $2\mathrm{dB}^{5,6}$ . Similar ideas were also extended into other laboratory demonstrations, e.g., in distributed phase sensing<sup>7</sup> and enhanced signal-to-noise-ratio in biological sensing<sup>8</sup> and microscopy<sup>9</sup>.

We aim to demonstrate an integrated quantum optical sensor that generates and uses squeezed light to perform measurements beyond the QNL. Our sensor moves much of the functionality often implemented on the optical table—e.g., generating pump light, locking phases, and implementing an interferometer, onto the chip itself. We use thin-film lithium niobate  $(\mathrm{LN})^{10}$  to achieve all of the functions in a monolithic circuit. In the last few years, integrated thin-film LN devices have demonstrated efficient light generation covering wavelengths from mid-infrared to blue[11-14], optical parametric oscillators[15,16], dispersion engineering[17-19], EO modulation, tuning[20,21], and frequency combs[22]. This article combines nearly all of the aforementioned capabilities in a single LN chip and demonstrates an integrated quantum sensor. We leverage the strongest electro-optic coefficient of LN  $(r_{33} = 31~\mathrm{pm / V})^{23}$  to actively control the power and phase of light within a photonic integrated circuit (PIC) and interface it with periodically poled LN (PPLN) waveguides that support efficient nonlinear processes. The strong second-order optical nonlinear coefficient  $\chi^{(2)}$ , accompanied by quasi-phase-matching in PPLN, allows us to achieve efficient second harmonic generation (SHG) and squeezed light generation through optical parametric amplification (OPA).

$^{1}$ Department of Applied Physics and Ginzton Laboratory, Stanford University, Stanford, CA 94305, USA.  $^{2}$ Physics & Informatics Laboratories, NTT Research, Inc., Sunnyvale, CA 94085, USA.  $^{3}$ Department of Electrical Engineering, Stanford University, Stanford, CA 94305, USA. e-mail: safavi@stanford.edu

In the degenerate parametric amplification process, photons are generated in pairs with a fixed phase relationship through the interaction  $\hat{H}_1\propto (\hat{a}^2 +\hat{a}^{\dagger 2})$  . The resulting state of the light is squeezed. Following the first demonstration of a squeezed light source by parametric down-conversion (PDC) in an optical cavity24, numerous other approaches, including single-pass PDC25,26, semiconductor lasers, optical fibers, atomic ensembles1, and ponderomotive squeezing with mechanical oscillators27 have successfully demonstrated varied amounts of squeezed light. Optical materials with intrinsic second- or third-order nonlinearities may be the most versatile integrated sensors approach. Recent demonstrations of integrated photonic circuits in silicon nitride28-30 proton-exchanged LN31, and thin-film LN32,33 have shown that low power and scalable sources of quantum light are possible.

Here, we focus on integrating these developments into a complex photonic circuit that can be used as a cost-effective and self-contained sensor. Because of this goal, we limit the optical power to the typical range of a commercial diode laser. Our goal, like those of the first integrated analog electronic circuits, is to demonstrate a path towards a deployable technology as opposed to realizing record-breaking performance. From a photonic system perspective, the squeezed source is only one part of a larger optical sensor. Combining emerging squeezed light sources with more complex PICs is a promising avenue for developing deployable optical sensors with quantum-enhanced sensitivity. So far, achieving sub-shot-noise sensitivity in optical metrology has required complex setups with multiple modulators, lasers, and optical cavities. This has limited the domain of quantum optical sensing to experiments with high complexity[5,6,9] that can address only a few of the possible application spaces—even for experiments that use new integrated quantum light sources. Our work

combines emerging squeezed light sources with a complex PIC to realize a nearly complete on-chip quantum sensor, thus opening a promising avenue for deployable optical sensors with quantum-enhanced sensitivity.

# Results

In this work, we use the X-cut thin film of lithium niobate on an insulator (LNOI) platform to build a sensor with an integrated source of squeezed light for quantum-enhanced measurement. Figure 1a outlines a scheme of the PIC implemented in our chip with three major components—input tunable beam splitter, squeezeer, and signal interferometer. We pattern eight such PICs in a single chip, which we show on a microscope picture in Fig. 1b. We design the squeezeer to generate a sub-shot noise state of light at the same frequency as the pump light, enabling interference with the local oscillator (LO) extracted from the original beam. Active EO circuitry controls interferometers and the LO phase, which enables using the system for both squeezing characterization and quantum measurement. Using lensed SMF-28 fiber, we interface our device with an off-the-shelf, ultra-low noise DBR laser and operate the system in CW mode at  $1544\mathrm{nm}$ . The output ports of the beam splitter out-couple light into two lensed multimode fibers, which we connect to a balanced photoreceiver off-chip. Both the laser $^{34,35}$  and detectors $^{36}$  can be further integrated with the PIC to increase the system efficiency and improve the squeezing visibility.

# Device design

The squeezeer subsystem comprises two PPLN waveguides and a series of directional couplers for spectral filtering. We design the waveguide geometry to maximize the nonlinear normalized efficiency (see Methods for details). Fundamental harmonic (FH) light first enters a

![](images/37ec01d98c4a14913f83247efe7c1bc4a66b60f746e1e2328e5dcf92b8d0b129.jpg)  
Fig. 1 | Squeezing and quantum-enhanced measurement PIC. a Schematic of a photonic integrated circuit for squeezing and quantum-enhanced measurement. Light from an external, integrated laser is polarization-controlled and coupled through a cleaved facet. The PIC splits light into two paths at the tunable beam splitter: the squeezeer pump and the local oscillator. The two beams are recombined at the signal interferometer to perform a quantum-enhanced measurement of a small RF signal. The signal interferometer also serves as a 50/50 beam splitter for squeezing characterization in BHD. Light is detected off-chip with a balanced photoreceiver connected to the chip with two lensed multimode fibers. Sum and difference signals provide feedback for locking output splitting ratio and LO power level. The setup contains an additional variable optical attenuator (VOA) just after the laser in the shot noise calibration measurements but is omitted for the  
squeezing measurements to reduce insertion loss. b Microscope picture of a chip with eight PICs, the red rectangle highlights a single device, blue outlines a single signal interferometer. A large-scale gold cross-pattern covers the entire chip to prevent stray light from interfering with guided modes. c Microscope picture of an MZI serving as a signal interferometer. The asymmetric design provides phase modulation to one of the arms of the interferometer through gold electrodes routed to an RF probe. The light blue lines in b and c correspond to optical waveguides; gold structures are elements of the EO-tuning circuitry. FPC fiber polarization controller, SHG second harmonic generation, OPA optical parametric amplification, BHD balanced homodyne detection, AWG arbitrary waveform generator.

PPLN waveguide designed to phase match a second harmonic generation process using periodic poling with a period of around  $3.7\mu \mathrm{m}$ . Tight mode confinement and strong second-order optical nonlinear coefficient of LNOI yield highly efficient SHG. Next, we filter out the residual FH by passing the light through three directional couplers. By design, each directional coupler transfers the majority of FH while keeping the second harmonic (SH) light in the original waveguide; hence the structure acts as a dichroic beam splitter. The SH light then loops back to another PPLN waveguide, realizing a phase-sensitive OPA of the quadrature fluctuations at the FH frequency, squeezing one quadrature and anti-squeezing the other. The amount of squeezing generated in this structure is given by:

$$
\frac {\left\langle \delta \hat {Y} ^ {2} \right\rangle}{\left\langle \delta \hat {Y} _ {\mathrm {v a c}} ^ {2} \right\rangle} = \exp \left(- 2 L \sqrt {\eta P _ {\mathrm {i n}}} \tanh  \left(L \sqrt {\eta P _ {\mathrm {i n}}}\right)\right), \tag {1}
$$

where  $\langle \delta \hat{Y}^2\rangle$  is the variance of the quadrature squeezed with respect to vacuum  $\langle \delta \hat{Y}_{\mathrm{vac}}^2\rangle ,L$  is the length of the poled waveguides,  $\eta$  is the normalized nonlinear conversion efficiency<sup>11</sup>, and  $P_{\mathrm{in}}$  is the telecom pump power (see Methods for details). Finally, the SH light is filtered out using the same directional coupler design, and the squeezed state propagates to the signal interferometer at the output of the PIC. We route the light filtered out after the SHG and OPA sections to the chip facet and use them as monitor ports.

Active EO circuitry controls optical power splitting and the LO phase within the PIC. The tunable beam splitter at the input and the signal interferometer at the output are both intensity modulators. Both consist of a Mach-Zehnder interferometer (MZI) with a phase modulator in one arm. The former is typically DC-biased at phase  $\phi_{1}$  either close to zero, to direct most of the input light into the squeezeer, or set to  $\pi$ , to send most of the light into the LO and characterize shot noise. The latter MZI, shown in Fig. 1c, is always locked with a DC bias to make the power at the two outputs equal for a balanced homodyne detection (BHD) measurement. We use the same phase modulator design for quadrature selection in the squeezeer path through  $\phi_{\mathrm{LO}}$  control. In addition to DC bias, we apply RF tones to the LO phase modulator and the signal interferometer. The RF phase modulation on the LO serves as voltage-to-phase calibration and quantifies the light leakage in the squeezeer  $\sqrt{\varepsilon} = \alpha_{\mathrm{Leakage}} / \alpha_{\mathrm{LO}}$ , while the RF phase modulation imposed on the signal interferometer forms the signal we measure. The mentioned leakage occurs only when a significant amount of power pumps the squeezeer subsystem. There is no leakage during the shot noise calibration since there is no light in the squeezing path.

# Subsystem characterization

We calibrate the shot noise level by routing all the optical power to the local oscillator path. For this purpose, we bias the tunable beam splitter at the input with a DC voltage bias of  $47\mathrm{V}$ . In this configuration, we use the local oscillator to probe the vacuum state sent to the opposing port of the signal interferometer. For the BHD measurement, we lock the signal interferometer to a splitting ratio of 50:50. We achieve this by controlling the difference between the intensity of two outputs and locking its DC part to zero. Next, we step the power of the input laser using an external variable optical attenuator (VOA), such that the power in the local oscillator waveguide varies between 0 and  $8.8\mathrm{mW}$  and record the RF spectra of the balanced homodyne detector, as shown in Fig. 2a. Finally, we integrate the noise power and plot it against the LO power in Fig. 2b, observing a linear dependence as expected from a shot noise-limited measurement. Note that the linearity of our measurement implies that there is no excess intensity noise from the laser. Hence, we measure only shot noise and can use it as a reference for further squeezing measurements. The mean squared error of the linear fit defines our uncertainty of the shot noise

![](images/8f039aa57f7d5c355ecd8884d649d45ded6c5c4dfc12651d334f139788fbc613.jpg)  
a

![](images/7f9755e92e66a09b30ae06c962e9de888c793ed69c96ddaf428cc0075ee08933.jpg)  
Frequency (MHz)  
Fig. 2 | PIC subsystems characterization. a Shot-noise power spectral density for different LO powers on the chip. We characterize our setup to find LO power yielding signals about 10 dB above the electronic noise floor. b Integrated noise from Fig. 2a vs. LO power follows a perfect linear trend, proving that the system is limited by shot noise at the target LO power of  $7.84\mathrm{mW}$ . c Example SHG phase-matching curve, deviation from ideal sinc² shape results from small geometry variation along the waveguide length. d Measured on-chip SHG peak power vs. FH pump power. Linear fit yields normalized efficiency of the nonlinear process of about  $1000\%/\left(\mathrm{W} \cdot \mathrm{cm}^{2}\right)$ . The inset shows an SHG microscope image of high-quality periodic poling of the thin-film lithium niobate. We pattern waveguides in the area where poling extends through the entire thickness of the LN film.

![](images/6eb44e546f14154bf234633ac73e6b766e6b97b01e7fb7f3e3131ad724872963.jpg)  
b

![](images/6760cfec029e860301f87e3d83569509c9756ecb565a1a2c80afa97e1e168c9b.jpg)  
LO Power (mW)

measurement. Based on the shot noise calibration, we choose LO power for the squeezing experiments at around  $7.84\mathrm{mW}$ , where the optical shot noise dominates our detection. We highlight this operating point in Fig. 2b. Note that the noise and LO power are recorded simultaneously, and the detector noise determines the uncertainty of the LO power below a relative deviation of  $3\times 10^{-5}$ .

The squeezeer relies on the performance of the periodically poled waveguides in the SHG and OPA sections. We characterize our periodic poling by measuring the quasi-phase-matching transfer function of a diagnostic waveguide patterned adjacent to our SHG and OPA segments such that it passes through the same poling region (see Methods for measurement details). An example QPM transfer function is shown in Fig. 2c. This measurement gives us the SHG response decoupled from the rest of the PIC components. Because the SHG and OPA take advantage of the same nonlinearity and poled waveguides are identical, we can directly use the nonlinear efficiency obtained in the SHG measurements to benchmark the OPA performance. Note that the diagnostic waveguide is  $8.1\mathrm{mm}$  long, whereas the one in the primary device is  $10\mathrm{mm}$  long. Given the significant length of the fabricated waveguide, nonuniformities distort the ideal sinc² shape of the nonlinear transfer function³⁷ and reduce the peak nonlinear efficiency. We measure the intensity of generated SH light as a function of pump power controlled by external VOA. In Fig. 2d, we plot data and linear fit to extract a maximum normalized efficiency of about  $1000\%/(W \cdot cm^2)$ , lower than the simulated  $4000\%/(W \cdot cm^2)$  for an ideal poled structure. We use this number further to estimate the amount of parametric amplification and the expected squeezing level. Because of the non-uniformities, the quadratic scaling of the efficiency with length is not exact. However, we neglect this because the length difference between the test and device waveguides is small. The inset of Fig. 2d shows a

![](images/af1414122359d5a7852592af7a1e40c11f51379b5a2aa812305a9fcf722f50bf.jpg)  
Fig. 3 | Squeezing and quantum-enhanced detection. a Power spectral density for maximum squeezing (orange line) and maximum anti-squeezing (blue line), collected while pumping the squeezeer with  $18.4\mathrm{mW}$  of FH. The black line provides a shot noise measurement reference. We highlight two RF peaks resulting from modulation of the LO phase shifter (blue highlighted area) and signal interferometer (orange highlighted area). b Local oscillator calibration peak power vs. DC bias voltage of the phase shifter. The solid line indicates the fit line, from which we find  $V_{\pi} = 28.6\mathrm{V}$  and light leakage into the squeezing path  $\varepsilon \approx 4.0\%$ . c Integrated noise power as a function of the LO phase (calibrated in Fig. 3b). The gray-dashed area represents the characteristic sub-shot noise behavior of a squeezed state. Misalignment of the squeezed state and LO phases is caused by the path length

![](images/a3c9897431c92ff7b129e3ea9729f98eae4ecc4606fb8fced77ece6b8cb0ac69.jpg)

![](images/2495921ccf3f33187a09fdedf3c6502bc1e9e8276894b53f5d7c8b71453fc7ba.jpg)  
difference between the two paths. The green highlighted area represents the model, including squeezeer leakage, detection efficiency, and normalized efficiency. The uncertainty of the normalized efficiency and phase sets the model bounds. d Quantum-enhanced measurement scheme-squeezed state feeds into a dark port of the MZI along with the LO entering the bright port. Phase modulation applied in one of the arms can be detected with enhanced SNR compared to a classical measurement. e Measurement of a small RF tone with noise floor suppressed with squeezing. We align the LO phase with maximum squeezing by DC tuning and measure the RF power spectrum through a BHD. For a  $-83\mathrm{dBm}$  modulation, we observe about  $(3.7\pm 1.0)\%$  improvement of the SNR compared to a shot-noise-limited measurement.

![](images/ea068ebd741abf54f11634952964cf55298b19efd6a9acc54ffd677ca1e66a1d.jpg)

![](images/e203d72fbc87eb8015c6cf70c97c719b4853c6c85f6957211445f8559affd7fe.jpg)

second harmonic microscope image of periodic poling used in the fabrication process. Black stripes on the sides of the picture are metal finger electrodes, and light gray shapes stretching between them correspond to inverted crystal domains.

# Squeezing and quantum-enhanced sensing

We characterize squeezing by directing most of the laser light into the squeezeer and holding the LO power constant. We drive the squeezeer subsystem with  $18.4\mathrm{mW}$  of optical power. Given the calibrated normalized efficiency, we estimate SH power at around  $3.4\mathrm{mW}$  to generate about  $(1.5\pm 0.1)$  dB of squeezing on the chip. We perform a BHD measurement to verify this by beating the squeezed state with the local oscillator at the signal interferometer. We lock the phase shift within the output interferometer such that the DC part of the difference signal is zero. At the same time, we lock the input beam splitter to keep the sum of photodiode readouts at a constant value, ensuring the LO power is fixed at around  $(7.84\pm 0.03)$  mW. We follow this locking scheme to work around the slow phase drift observed in EO devices[38,39]. A simple procedure that periodically updates the voltage at the input beam splitter and signal interferometer at a low frequency (around  $1\mathrm{Hz}$ ) is sufficient. Finally, we measure the power spectral density, as shown in Fig. 3a, and reference it to the shot noise measurement (black line). We perform this measurement as a function of the LO phase, controlled through a DC voltage applied to a phase shifter in the LO path. Blue and orange traces in Fig. 3a correspond to the maximum antisqueezing and maximum squeezing, respectively. In addition to probing broadband noise, we introduce two RF signals corresponding to peaks at 72 and  $60\mathrm{MHz}$ . The former originates from an RF signal applied to the LO phase shifter, which we highlight in blue, and the latter corresponds to a tone on the signal interferometer, which we highlight in orange.

We verify the phase-sensitive nature of the generated squeezed light by stepping the LO phase shifter bias. Due to a small power leakage of the FH in the squeezeer path,  $\varepsilon$ , we can observe the RF peak introduced at the LO phase shifter at  $72\mathrm{MHz}$ . This signal is proportional to  $\varepsilon \sin^2 (V_{DC} / V_{\pi} \cdot \pi)$  (see Methods for details). By fitting the peak power as a function of LO bias voltage in Fig. 3b, we establish the power leakage ratio  $\varepsilon$  at around  $(4.0 \pm 1.0)\%$ , which we use to estimate the filter extinction ratio at around  $18\mathrm{dB}$  (see Methods for details on filter design and characterization). This amount of leakage enables us to find the relative phase between the LO and squeezed state. Note that a single phase shifter on the LO allows us to set any relative phase between the squeezed light and the LO. Consequently, we can characterize the squeezed state or align the phases to only sample the sub-shot noise quadrature in the quantum-enhanced measurement. The observed amount of leakage does not significantly impact the squeezing visibility in our system (see Methods for details). Using the fit, we also find the half-wave voltage of our LO to be  $28.6 \pm 0.3\mathrm{~V}$  and convert the DC bias to phase. The half-wave voltage agrees with our design (see Methods for details). In the squeezing measurement, in Fig. 3c, we plot the integrated noise floor over the measurement bandwidth vs. calibrated LO phase, excluding the two RF peaks and a small, broad feature between 67 and  $72\mathrm{MHz}$ . Plotted noise is normalized to shot noise, in which uncertainty is smaller than the width of the line. Moreover, we continuously monitor the stability of the DC optical power readout on both detectors to ensure that the LO power is constant. The relative deviation of the LO power during the squeezing measurement is below  $0.3\%$ , which allows us to detect changes to the noise on the order of several percent (see Methods for details). We see expected periodic behavior, where the minimum and maximum correspond to probing squeezed and anti-squeezed field quadratures, respectively. Instead of performing fast phase sweeps, we maintain the LO phase at each tuning point for roughly  $13\mathrm{~s}$  and obtain

![](images/52f771414a3e6b134c3b909eac9c2d3f9bae7697fe887d00b6665bd49e8d319e.jpg)  
Fig. 4 | Device fabrication procedure. a We start with a  $500\mathrm{nm}$  thin-film LN on an insulator. b For periodic poling of the LN film, we use chromium electrodes deposited on a  $100\mathrm{nm}$  silica insulation layer. Next, we apply a high-voltage pulse to invert crystal domains. c Chromium electrodes and silica layer are removed after poling using chromium etchant and buffered oxide etchant. d Waveguides are  
patterned using electron beam lithography and argon ion milling. e We pattern a bottom layer of gold directly on LN to increase the electric field within the waveguide region. f Wavegues are covered with around  $700\mathrm{nm}$  of silica. g We open vias in the cladding to provide electrical contact to the buried electrodes. h We pattern the top layer of gold to connect our devices to the external probe.

the full RF spectrum. This highlights the stability of our system, a necessary ingredient for a stable and metrologically useful source of squeezed light. We measure  $(2.7 \pm 0.2$  (stat)  $\pm 0.3$  (syst))% of squeezing and  $(12.3 \pm 0.2$  (stat)  $\pm 0.3$  (syst))% of anti-squeezing.

Limited squeezing visibility and squeezing/anti-squeezing asymmetry result from the detection chain efficiency of  $20\%$  (see Methods for more details) and squeezeer leakage  $\varepsilon \approx 4\%$ . Accounting for these factors, we expect the level of squeezing on-chip to be around  $(1.5 \pm 0.1)$  dB, which agrees with our estimation based on the normalized efficiency. The detection chain loss consists mainly of the fiber-chip coupling with contributions from the small waveguide propagation loss and non-ideal quantum efficiency of the photodiodes. The fiber-chip coupling is also a limiting factor in the available optical pump power. Total detection chain efficiency can improve by up to  $\approx 80\%$  by reducing optical loss. This improvement will increase the amount of squeezing generated on the chip (due to higher available optical power) and squeezing visibility (due to suppressed loss of detection). Implementing straightforward PIC layout improvements to reduce the propagation loss, improved fiber-to-chip coupling[40-42], and higher quantum efficiency photodiodes can result in an achievable  $4.5\mathrm{dB}$  squeezing or SNR improvement by  $280\%$  using the same off-the-shelf integrated laser. See the Methods section for more details on the loss in the current device and the path toward loss reduction.

Finally, we use the signal interferometer to perform a quantum-enhanced measurement of an RF signal. The classical approach to increasing SNR is by using more optical power. However, this strategy is limited –increasing optical power in electro-optic-modulators causes a series of parasitic effects related to the second- and third-order nonlinearity. Especially the photorefractive effect can cause instability of electro-optic modulators. Moreover, photodetectors suffer from saturation and nonlinearity, and can be damaged with large optical power. Using the additional power to generate squeezing offers an alternative. In this case, the chip configuration is the same as in the squeezing measurement; most light pumps the squeezezer, and the LO power is fixed at  $(7.84 \pm 0.03) \mathrm{mW}$ . We use the signal interferometer to perform a quantum-enhanced measurement by injecting squeezed state into its dark port, as shown in Fig. 3d. Based on our squeezing calibration, we set the LO phase to align with the maximum observed squeezing and perform the measurement. For that purpose, we apply a small RF tone to the output interferometer electrode. We set the RF amplitude to  $-83 \mathrm{~dBm}$ , corresponding to the root-mean-square voltage of  $15.8 \mu \mathrm{V}$  at  $60 \mathrm{MHz}$ . This signal can be detected in the BHD measurement, as shown in Fig. 3e, and it is not sensitive to the LO phase, which is set before the light enters the output interferometer. As a result, the measurement noise floor is reduced with respect to the

shot noise and results in about  $(3.7\pm 1.0)\%$  SNR improvement. This data was taken at a different time than the LO phase sweep dataset shown in Fig. 3c, and so we attribute the slightly higher level of observed squeezing to slightly different experimental conditions. The uncertainty on the SNR improvement is also more significant than the squeezing measurement since it comes from just one dataset, as opposed to the entire LO phase sweep.

# Discussion

Complex quantum photonic integrated circuits, like the one presented in this work, extend the reach of quantum technologies into new domains. The integration allows us to generate quantum light and leverage its properties within the same circuit, enabling more stable and lower power operation. These critical advantages point toward new classes of mobile and deployable sensors that are natively "quantum-compatible". In the work we present here, we benchmark a sensor by detecting voltage signals imparted as phase upon an optical field. Many other interferometric measurements are today limited by shot noise. These measurements, including refractive index sensing, optomechanical force, acceleration $^{43}$ , and mass sensing $^{44}$ , will directly benefit from integrating the quantum apparatus, as demonstrated here. Moreover, squeezing and squeezed light are crucial elements of numerous quantum sensing, communications $^{45}$ , and computing protocols $^{46,47}$ . Quantum PICs, such as those shown here, are promising and scalable approaches for building these systems.

# Methods

# Fabrication

We fabricate our device with X-cut thin-film LNOI (lithium niobate on insulator, NanoLN), following the procedure outlined in Fig. 4. The material stack consists of  $500\mathrm{nm}$  of lithium niobate bonded to a  $2\mu \mathrm{m}$ -thick silica layer on top of a silicon handle wafer, as shown in Fig. 4a. Fabrication starts with poling the thin-film. In the first step (Fig. 4b), we pattern Cr electrodes on an insulating layer of  $100\mathrm{nmSiO}_2$  using electron beam lithography (JEOL 6300-FS,  $100\mathrm{-kV}$ ) and the liftoff process. The poling period is around  $3.7\mu \mathrm{m}$ , and we design it for phasematching between our waveguide's 1550 and  $775\mathrm{nm}$  modes. Next, we apply high-voltage pulses to flip crystal domains[16,48]. After poling, we remove the electrodes with chromium etchant and buffered oxide etchant (Fig. 4b).

The photonic circuit is patterned with a FOX-16 mask and electron beam lithography and transferred to the LN layer with an argon ion mill (Fig. 4d). The etch depth is  $300\mathrm{nm}$ , and the waveguide width is  $1.2\mu \mathrm{m}$ .

Metal electrodes for EO tuning are patterned with the same process as the poling electrodes but made out of  $100\mathrm{nm}$  gold (Fig. 4e).

![](images/57a56090fa0830f587dcbad4c5817551300686fa72075d982a803575e146b0d8.jpg)

![](images/8c5dfbab829394177d3837d4cbdbe0f94f7999a7614da024eafb081cce05e929.jpg)  
Fig. 5 | Design of the waveguide and electro-optic modulator. a Geometry of the nonlinear LN waveguide. The ridge waveguide width is  $w = 1.2 \mu \mathrm{m}$ , and its height is  $h = 300 \mathrm{~nm}$ . Slab thickness is  $s = 200 \mathrm{~nm}$ . Waveguides are periodically poled with period  $\Lambda = 3.7 \mu \mathrm{m}$  and covered with  $\mathrm{SiO}_2$  cladding of thickness  $c = 700 \mathrm{~nm}$ . b Effective indices of waveguide modes as a function of wavelength. The fundamental TE mode is highlighted in orange. The dispersion-induced phase velocity

The bottom layer of electrodes and waveguides are covered with  $\mathrm{SiO}_2$  deposited with a high-density plasma process (Fig. 4f) $^{49}$ . To provide electrical contact to the buried electrodes, we pattern vias by standard  $\mathrm{SiO}_2$  etch with fluorine chemistry and photolithography (Fig. 4g). Finally, we pattern a top metal layer with the electron beam. This layer provides access to the buried electrodes with an external probe and consists of  $200\mathrm{nm}$  of gold and a  $10\mathrm{nm}$  chromium adhesion layer (Fig. 4h).

In the final step, we prepare the chip facets for light coupling by stealth dicing with a DISCO DFL7340 laser saw<sup>17</sup>. High-energy optical pulses are focused on the substrate to create an array of damage sites. They act as nucleation sites for crack propagation, resulting in a uniform and smooth cleave.

# Waveguide design

We design the waveguide geometry to maximize the normalized nonlinear efficiency for the SHG pumped at  $1540\mathrm{nm}$  and OPA pumped at  $770\mathrm{nm}$ . We find a geometry that results in the normalized efficiency of around  $\eta \approx 4000\% /(\mathrm{Wcm}^2)$ . We show the waveguide schematic in Fig. 5a, the ridge width is  $1.2\mu \mathrm{m}$ , height is  $300\mathrm{nm}$ , and slab thickness is  $200\mathrm{nm}$ . We clad the waveguide with around  $700\mathrm{nm}$  of silicon dioxide. For the chosen geometry, we calculate the phase velocity mismatch between 770 and  $1540\mathrm{nm}$  light and compensate for it with periodic poling. Figure 5b shows the effective index of all the supported waveguide modes as a function of wavelength. The difference between the effective index at FH and SH defines poling period  $\Lambda = \lambda_{SH} / \Delta n$ .

# Electro-optic simulation

We design the geometry of our electro-optic devices to provide phasetuning functionality without introducing excess loss to the quantum state of light. We model our system using a finite-element mode solver

![](images/aff9fdb06ca04f3ab100147081c23a327038b3ef6289d1347f996f56aba1d5e2.jpg)

![](images/062afad25ba3202ac68ac9b3394100c0f64f5704b6875f4156c1e098f181c0e4.jpg)  
mismatch is compensated through poling with a period proportional to  $\Delta n_{\mathrm{eff}}$ . c Eigenmode solver solution for the fundamental TE mode in the presence of a static electric field. White arrows indicate the direction of the applied bias field. d Half-wave voltage-length product and metal-induced propagation loss as a function of the waveguide-electrode gap. The dashed line corresponds to the geometry described in the main text with a waveguide-electrode gap of  $1.6\mu \mathrm{m}$

(COMSOL). We first define the electric field-dependent refractive index<sup>23</sup> as:

$$
n _ {\mathrm {o}} ^ {\prime} = n _ {\mathrm {o}} - \frac {1}{2} r _ {1 3} n _ {\mathrm {o}} ^ {3} E _ {\mathrm {z}} \tag {2}
$$

$$
n _ {\mathrm {e}} ^ {\prime} = n _ {\mathrm {e}} - \frac {1}{2} r _ {3 3} n _ {\mathrm {e}} ^ {3} E _ {z}. \tag {3}
$$

The elements of the electro-optic tensor  $r_{33} = 31 \, \mathrm{pm/V}$  and  $r_{13} = 10 \, \mathrm{pm/V}$  modify ordinary and extraordinary indices of the crystal as a result of the static field. We solve for the static electric field and follow with eigenmode analysis in the system with a modified refractive index, as shown in Fig. 5c.

We find the half-wave-voltage-length product from the relationship between the effective index and applied voltage  $V_{\pi}L = \lambda /(\partial n_{\mathrm{eff}} / \partial V)$ . We plot the expected values along with the propagation loss from metal proximity in Fig. 5d. In the device described in the main text, we use a waveguide-electrode gap of  $1.6~{\mu\mathrm{m}}$  and an electrode length of  $2.5\mathrm{mm}$ . We expect the half-wave voltage in this geometry to be around  $30\mathrm{V}$ , which agrees with the value measured in the experiment. This gap size allows us to keep the propagation loss induced by the metal below  $0.05\mathrm{dB / cm}$ , which is negligible compared to the measured loss resulting from fabrication imperfections around  $0.7\mathrm{dB / cm}$ .

# Experimental setup

We characterize fabricated PICs in two different setup configurations, one for BHD and one for SHG characterization. In both cases, the chip temperature is controlled with a thermistor (Thorlabs TH10K) and thermo-electric cooler (Thorlabs TECF2S, MTD41STE, MTDEVAL1). We

![](images/c0dd56ad03d6314316fd80f2a1a682b103034f19cc76f0e809b2e2ed80989deb.jpg)

![](images/ad6b24fe94b3be56b54be2ec8cdb0e9eb965c1e746f86402361f20d86dda22b0.jpg)  
Fig. 6 | Balanced homodyne detection stability. a Absolute power measured on two photodetectors in the balanced homodyne setup during a single LO phase sweep squeezing measurement. b The same data is normalized to the average optical power per detector. The standard deviation of the normalized power is below  $0.3\%$ .

operate our device at  $45^{\circ}\mathrm{C}$  to maximize SHG intensity at the low noise laser operating wavelength.

The setup for BHD measurements is shown in Fig. 1a. For squeezing and quantum-enhanced measurements, we use an ultra-low noise, integrated DFB laser with an emission wavelength of around  $1544\mathrm{nm}$  (Thorlabs ULN15PC). The laser is followed by a high extinction ratio fiber isolator (Thorlabs IOT-G-1550A) and a fiber polarization controller. We introduce an additional variable optical attenuator (HP 8156A) for the shot noise measurement to control the laser power. Then, we couple light to the chip with a lensed SMF-28 fiber (OZ Optics). We collect light into a balanced photoreceiver (Thorlabs PDB425C with RF output conversion gain  $1.25\times 10^{5}\mathrm{V / W})$  using multimode fibers lensed (in-house) and mounted on a v-groove chip with a pitch matching the PIC output waveguide separation. We collect RF spectra with an electronic spectrum analyzer (Rohde & Schwarz FSW26) with a resolution bandwidth set to  $60\mathrm{kHz}$ . Tap ports for FH and SH light filtered within the squeezezer subsystem are collected into another lensed multimode fiber, separated by a combination of a 50/50 splitter and optical edge pass filters, and monitored with photodiodes: Newport 1623 Nanosecond Photodetector for FH and Thorlabs APD440A for SH. Electro-optic components on the chip are controlled with DC voltage supplied with three TTi PLH250-P sources. LO phase modulator and the signal interferometer receive RF signal from an arbitrary waveform generator (Rigol DG4102). We mix RF signals and DC bias with bias-tees  $(\mathrm{ZFBT - 4R2G + })$  and connect to the chip with a triple ground-signal-ground (GSG) probe. We estimate the total insertion loss of RF input at  $1.22\mathrm{dB}$  by combining the loss of two SMA cables (FLC-4FT-SMSM+), DC block (Inmet 8039), and the bias-tee.

We evaluate the system's stability during balanced homodyne measurements based on the DC readout of the individual photodiodes of the balanced detector. We convert the readouts to optical power and plot it for the squeezing measurement dataset in Fig. 6a. Figure 6b shows the same dataset normalized to the mean power of each channel in the BHD. The standard deviation of the relative power is below  $0.3\%$ , which allows us to detect small changes to the noise power on the order of a few percent. We also use the DC readouts from the

homodyne detector to normalize the data plotted in the main part of the article.

For the second harmonic characterization, we reconfigure the setup to work with a continuously tunable c-band laser (Santec TSL-550, 1480–1630 nm) passing through a variable optical attenuator (HP 8156A). Next, we tap off  $5\%$  of the light for power calibration using a power meter (Newport 918D-IR-OD3R) and pass the light through a polarization controller. Light couples to the chip through an SMF-28 lensed fiber and is collected by the same kind of fiber at the output facet. Then, we out-couple light into free space and split with a  $1000\mathrm{nm}$  short-pass dichroic mirror (Thorlabs DMSP1000) and filter to avoid cross-talk. Finally, we measure light intensity with avalanche photodiodes (Thorlabs APD410A and Thorlabs APD410). We use variable optical attenuators before APDs to prevent saturation and increase the dynamic range of our measurement (HP 8156A and Thorlabs FW102C).

# Squeeze performance

The integrated squeezeer proposed in the main text takes advantage of the second-order nonlinearity in LN waveguides. In this system, both SHG and OPA can be described with coupled-mode equations for the degenerate three-wave mixing process $^{23}$ :

$$
\frac {\partial}{\partial z} A (z) = - i \sqrt {\eta} B (z) A ^ {*} (z) e ^ {- i \Delta k z}, \tag {4}
$$

$$
\frac {\partial}{\partial z} B (z) = - i \sqrt {\eta} A ^ {2} (z) e ^ {i \Delta k z}. \tag {5}
$$

where  $A(z)$  and  $B(z)$  are amplitudes of the FH and SH modes with frequency relationship  $2\omega_{A} = \omega_{B}$ .  $\eta$  corresponds to normalized efficiency,  $\Delta k = 2k_{A} - k_{B}$  is the phase mismatch between FH and SH modes, which we compensate for with periodic poling. We solve these equations to obtain the magnitude of the power normalized amplitude of the generated SHG, assuming perfect phasematching:

$$
| B (z) | = | A (0) | \tanh  (\sqrt {\eta} | A (0) | z). \tag {6}
$$

In the squeezeer subsystem, FH light is filtered out after pumping the SHG, and the SH stays in the waveguide to generate squeezing through OPA. To find the amount of squeezing generated, we will first define field quadratures for the FH mode as follows:

$$
X = \frac {A + A ^ {*}}{2}, \tag {7}
$$

$$
Y = i \frac {A - A ^ {*}}{2}. \tag {8}
$$

Next, we can use equation (4) to find the evolution of the field quadratures  $X$  and  $Y$  along the waveguide length as follows:

$$
\begin{array}{l} \partial_ {z} (A (z) + A ^ {*} (z)) = - i \sqrt {\eta} (B (z) A (z) ^ {*} - B (z) ^ {*} A (z)) \tag {9} \\ = \sqrt {\eta} | B (z) | \left(A (z) + A (z) ^ {*}\right). \\ \end{array}
$$

In the last line, we have chosen to set the phase of  $B(z)$  to  $-\pi / 2$ . Performing a similar calculation for the time evolution of the Y quadrature, we arrive at:

$$
\partial_ {z} X = \sqrt {\eta} | B (z) | X, \tag {10}
$$

$$
\partial_ {z} \mathrm {Y} = - \sqrt {\eta} | B (z) | \mathrm {Y}. \tag {11}
$$

Solving these equations yields:

$$
\mathrm {X} = \mathrm {X} (0) \exp (\sqrt {\eta} | B (z) | z), \tag {12}
$$

$$
Y = Y (0) \exp (- \sqrt {\eta} | B (z) | z). \tag {13}
$$

It is clear that the Y quadrature is deamplified while the X quadrature is amplified. This amplification and deamplification process, when applied to shot-noise-limited light, leads to anti-squeezing and squeezing of the quadrature fluctuations. In other words, the variance for quadrature operators under the action of amplification/deamplification is given by:

$$
\left\langle \delta \hat {\mathbf {X}} ^ {2} \right\rangle = \exp \left(2 \sqrt {\eta} | B (z) | z\right) \left\langle \delta \hat {\mathbf {X}} _ {0} ^ {2} \right\rangle , \tag {14}
$$

$$
\left\langle \delta \hat {\mathbf {Y}} ^ {2} \right\rangle = \exp \left(- 2 \sqrt {\eta} | B (z) | z\right) \left\langle \delta \hat {\mathbf {Y}} _ {0} ^ {2} \right\rangle , \tag {15}
$$

where  $\langle \delta \hat{\mathbf{X}}_0^2\rangle$  and  $\langle \delta \hat{\mathbf{Y}}_0^2\rangle$  are variances of the quantum state entering the OPA. In the proposed PPLN squeezeer subsystem of length  $L$ , combining equations (6) and (15) defines squeezing as:

$$
\frac {\left\langle \delta \hat {Y} ^ {2} \right\rangle}{\left\langle \delta \hat {Y} _ {0} ^ {2} \right\rangle} = \exp \left(- 2 L \sqrt {\eta P _ {\mathrm {i n}}} \tanh  \left(L \sqrt {\eta P _ {\mathrm {i n}}}\right)\right). \tag {16}
$$

# Coherent leakage into the squeezeer and LO phase calibration

In our system, we observe non-perfect filtering of the squeezezer subsection pump at the fundamental frequency. This results from the limited extinction ratio of the filter used on the chip to separate FH from SH after the SHG section. This section explains how we quantify this leakage and use it to calibrate the local oscillator phase.

Our model consists of a tunable beam splitter with two inputs (LO and squeezeer output) and two outputs (BHD ports). We calculate a result of a phase modulation imposed on the LO arm on the BHD measurement result, depending on the leakage level. The input state of the system is:

$$
\left[ \begin{array}{l} A _ {i n} ^ {(1)} \\ A _ {i n} ^ {(2)} \end{array} \right] = \left[ \begin{array}{c} \sqrt {\varepsilon} \alpha_ {\mathrm {L O}} (t) + \hat {\boldsymbol {a}} \\ \alpha_ {\mathrm {L O}} (t) e ^ {i \phi_ {\mathrm {L O}}} e ^ {i \phi_ {\mathrm {M}} (t)} + \hat {\boldsymbol {v}} \end{array} \right]. \tag {17}
$$

Here,  $\varepsilon$  is the power ratio of the coherent leakage to the LO,  $\phi_{\mathrm{LO}}$  is the LO phase with respect to the signal in the squeezeer path,  $\phi_{\mathrm{M}}$  is the RF phase modulation,  $\hat{a}$  and  $\hat{\nu}$  represent quantum fluctuations in the squeezeer and LO paths, respectively. We solve the beam splitter matrix equation:

$$
\left[ \begin{array}{l} A _ {o u t} ^ {(1)} \\ A _ {o u t} ^ {(2)} \end{array} \right] = \left[ \begin{array}{c c} \sin \left(\phi_ {2} / 2\right) & \cos \left(\phi_ {2} / 2\right) \\ \cos \left(\phi_ {2} / 2\right) & - \sin \left(\phi_ {2} / 2\right) \end{array} \right] \left[ \begin{array}{l} A _ {i n} ^ {(1)} \\ A _ {i n} ^ {(2)} \end{array} \right] \tag {18}
$$

to find the BHD signal generated. This model is equivalent to the signal interferometer described in the main text. For no power leakage, it is biased such that the phase is around  $\phi_{2} = \pi / 2$  but  $\varepsilon \neq 0$  results in an imbalance that we have to compensate for.

We solve for the output port amplitudes and use them to find the BHD differential signal defined as  $P_{\mathrm{BH}} = |A_{out}^{(1)}|^2 - |A_{out}^{(2)}|^2$ . The result is

given by:

$$
\begin{array}{l} P _ {\mathrm {B H}} = \cos \left(\phi_ {2}\right) \left| \alpha_ {\mathrm {L O}} \right| ^ {2} (1 - \varepsilon) + 2 \sin \left(\phi_ {2}\right) \sqrt {\varepsilon} \left| \alpha_ {\mathrm {L O}} \right| ^ {2} \cos \left(\phi_ {\mathrm {L O}}\right) \\ + \cos (\phi_ {2}) [ \alpha_ {\mathrm {L O}} e ^ {i \phi_ {\mathrm {L O}}} \hat {v} ^ {\dagger} - \sqrt {\varepsilon} \alpha_ {\mathrm {L O}} \hat {a} ^ {\dagger} + h. c ] \tag {19} \\ + \sin \left(\phi_ {2}\right) \left[ \alpha_ {\mathrm {L O}} e ^ {i \phi_ {\mathrm {L O}}} \hat {a} ^ {\dagger} + \sqrt {\varepsilon} \alpha_ {\mathrm {L O}} \hat {v} ^ {\dagger} + h. c \right] \\ \end{array}
$$

We separate equation (19) into DC and AC parts. The former defines the locking condition:

$$
\cos \left(\phi_ {2}\right) (1 - \varepsilon) + 2 \sin \left(\phi_ {2}\right) \sqrt {\varepsilon} \cos \left(\phi_ {\mathrm {L O}}\right) = 0, \tag {20}
$$

which is solvable analytically:

$$
\phi_ {2} = \pm \arccos  \left[ \pm \frac {2 \sqrt {\varepsilon} \cos \left(\phi_ {\mathrm {L O}}\right)}{\sqrt {4 \varepsilon \cos^ {2} \left(\phi_ {\mathrm {L O}}\right) + \varepsilon^ {2} - 2 \varepsilon + 1}} \right]. \tag {21}
$$

In addition to locking, we use the DC term to calibrate the LO phase and directly measure the leakage  $\varepsilon$ . For this purpose, we introduce a periodic modulation to the LO phase shift, such that  $\phi_{\mathrm{LO}} = \phi_{\mathrm{LO}} + \phi_{\mathrm{M}}(t) = \phi_{\mathrm{LO}} + \pi V_{\mathrm{p - p}} / (2V_{\pi})\sin (\Omega t)$ .  $\Omega$  is the modulation frequency (here set to  $72\mathrm{MHz}$ ),  $V_{\pi}$  is the half-wave voltage, and  $V_{\mathrm{p - p}}$  is the peak-to-peak modulation voltage. We focus on the DC part of the equation (19), apply a standard Taylor series expansion to the phase modulation term, and write the resulting signal in the frequency domain at the peak frequency of the modulation:

$$
P _ {\mathrm {R F}} (\Omega) = \frac {2 \varepsilon R ^ {2} P _ {\mathrm {L O}} ^ {2}}{Z} \left(\frac {\pi}{2}\right) ^ {3} \frac {V _ {\mathrm {p - p}}}{V _ {\pi}} \sin^ {2} \left(\frac {V _ {\mathrm {D C}}}{V _ {\pi}} \pi\right), \tag {22}
$$

$V_{\mathrm{DC}}$  is the DC voltage bias at the LO phase shifter. Signal strength depends on the local oscillator power  $P_{\mathrm{LO}}$ , detection responsivity  $R$ , the impedance of the detector  $Z$ , and the leakage  $\varepsilon$ . We fit equation (22) in the main text to find  $\varepsilon$  and  $V_{\pi}$ .

# Impact of leakage on the squeezing visibility

The AC part of the equation (19) probes both the noise of the prepared quantum state and the noise of the LO. It results in the noise measured in the main text:

$$
\begin{array}{l} P _ {\mathrm {B H}} ^ {(\mathrm {A C})} = \cos (\phi_ {2}) [ \alpha_ {\mathrm {L O}} e ^ {i \phi_ {\mathrm {L O}}} \hat {v} ^ {\dagger} - \sqrt {\varepsilon} \alpha_ {\mathrm {L O}} \hat {a} ^ {\dagger} + h. c ] \\ + \sin (\phi_ {2}) [ \alpha_ {\mathrm {L O}} e ^ {i \phi_ {\mathrm {L O}}} \hat {a} ^ {\dagger} + \sqrt {\varepsilon} \alpha_ {\mathrm {L O}} \hat {v} ^ {\dagger} + h. c ]. \\ \end{array}
$$

(23)

Note that it reduces to the usual BHD expression for  $\varepsilon = 0$  and  $\phi_{2} = \pi /2$ . Our experiment introduces two modifications to the classical BHD picture. One is the leakage  $\varepsilon \neq 0$ , which results in probing the local oscillator noise  $\hat{v}$ , in addition to measuring the squeezed state  $\hat{a}$ . The other modification is varying the splitting ratio of the output beam splitter  $\phi_2\neq \pi /2$ . This adds a term proportional to  $\cos (\phi_2)$ , resulting in changing the measured noise characteristics. As a result, measured squeezing can be reduced. This section explains how the power leakage  $\varepsilon$  impacts observable squeezing. We first rewrite the equation (23) with the quadrature operators for the squeezing and LO paths  $\hat{a} = \delta \hat{\mathbf{X}} - i\delta \hat{\mathbf{Y}}$  and  $\hat{v} = \delta \hat{\mathrm{X}}_{\mathrm{LO}} - i\delta \hat{\mathrm{Y}}_{\mathrm{LO}}$ :

$$
\begin{array}{l} P _ {\text {D I F F}} ^ {(\mathrm {A C})} = 2 \sin (\phi_ {2}) | \alpha_ {\mathrm {L O}} | \\ \times \left[ \cos \left(\phi_ {\mathrm {L O}}\right) \delta \hat {\mathrm {X}} - \sin \left(\phi_ {\mathrm {L O}}\right) \delta \hat {\mathrm {Y}} + 2 \sqrt {\varepsilon} \delta \hat {\mathrm {X}} _ {\mathrm {L O}}. \right] \tag {24} \\ + 2 \cos (\phi_ {2}) | \alpha_ {\mathrm {L O}} | \\ \times \left[ \cos \left(\phi_ {\mathrm {L O}}\right) \delta \hat {\mathrm {X}} _ {\mathrm {L O}} - \sin \left(\phi_ {\mathrm {L O}}\right) \delta \hat {\mathrm {Y}} _ {\mathrm {L O}} - 2 \sqrt {\varepsilon} \delta \hat {\mathrm {X}} \right] \\ \end{array}
$$

This is an expected result for the BHD applied toward phase-sensitive probing of the quadratures of a squeezed state with an additional term that probes the noise of the LO. We assume the LO noise to be phase-

![](images/1a6bba2eb0cfe907a8beac6caf8c7dcdabaa93c57de8a1422013c68b4411db22.jpg)  
Fig. 7 | Effect of coherent leakage on squeezing visibility. We calculate the expected noise assuming  $1.5\mathrm{dB}$  squeezing and anti-squeezing and coherent leakage in the squeezeer subsystem. The noise values correspond to the values on the chip (excluding fiber-to-chip coupling efficiency) and are normalized to the shot noise. We plot the noise as a function of the local oscillator phase for three different values of coherent leakage  $\varepsilon = 0.01, 0.1,$  and  $0.5$  ( $\sqrt{\varepsilon} = \alpha_{\mathrm{Leakage}} / \alpha_{\mathrm{LO}}$ ).

insensitive and shot-noise-limited. The signal variance is proportional to the power measured by the spectrum analyzer and given by equation (25). We use this result as a model for our squeezing measurement in the main text.

$$
\begin{array}{l} \left\langle \delta P _ {\text {D I F F}} ^ {(\text {A C}), 2} \right\rangle = 4 \left| \alpha_ {\mathrm {L O}} \right| ^ {2} \left[ \cos^ {2} \left(\phi_ {2}\right) \left(\cos^ {2} \left(\phi_ {\mathrm {L O}}\right) \left\langle \delta \hat {\mathrm {X}} _ {\mathrm {L O}} ^ {2} \right\rangle + \sin^ {2} \left(\phi_ {\mathrm {L O}}\right) \left\langle \delta \hat {\mathrm {Y}} _ {\mathrm {L O}} ^ {2} \right\rangle + 4 \varepsilon \left\langle \delta \hat {\mathrm {X}} ^ {2} \right\rangle\right) \right. \\ + \sin^ {2} \left(\phi_ {2}\right) \left(\cos^ {2} \left(\phi_ {\mathrm {L O}}\right) \left\langle \delta \hat {\mathrm {X}} ^ {2} \right\rangle + \sin^ {2} \left(\phi_ {\mathrm {L O}}\right) \left\langle \delta \hat {\mathrm {Y}} ^ {2} \right\rangle + 4 \varepsilon \left\langle \delta \hat {\mathrm {X}} _ {\mathrm {L O}} ^ {2} \right\rangle\right) \\ \left. + 2 \sin \left(2 \phi_ {2}\right) \sqrt {\varepsilon} \cos \left(\phi_ {\mathrm {L O}}\right) \left(\left\langle \delta \hat {\mathrm {X}} _ {\mathrm {L O}} ^ {2} \right\rangle - \left\langle \delta \hat {\mathrm {X}} ^ {2} \right\rangle\right) \right] \tag {25} \\ \end{array}
$$

We illustrate the effects of coherent leakage on squeezing visibility in Fig. 7. We plot the normalized BHD signal using the formula (25) as a function of the local oscillator phase for  $1.5\mathrm{dB}$  of squeezing and anti-squeezing. We assume that the system is locked such that the homodyne detector is balanced, following formula (21) and plot all the values normalized to the shot noise. We plot the results for three squeezeer leakage ratios:  $\varepsilon = 0.01$ , 0.1, and 0.5. The leakage on the order of less than  $10\%$  does not change the squeezing visibility significantly. However, excessive leaks can have a more severe impact. Note that we do not include the fiber-to-chip coupling efficiency in this plot to isolate the leakage effect from the detection loss.

# Effects of loss in the system

The total detection chain efficiency is a major challenge in characterizing squeezed light. This is especially consequential when working with complex PICs like the one described in the main text. In our experiment, the total detection chain efficiency was around  $\zeta \approx 20\%$ , this leads to the reduction of squeezing visibility:

$$
\left[ \frac {\left\langle \delta \hat {Y} ^ {2} \right\rangle}{\left\langle \delta \hat {Y} _ {\mathrm {v a c}} ^ {2} \right\rangle} \right] = \left(\zeta \left[ \frac {\left\langle \delta \hat {Y} ^ {2} \right\rangle}{\left\langle \delta \hat {Y} _ {\mathrm {v a c}} ^ {2} \right\rangle} \right] _ {\text {O n - C h i p}} + (1 - \zeta)\right). \tag {26}
$$

Table 1 | Summary of the sources of loss in the detection chain  

<table><tr><td>Loss source</td><td>Loss (dB)</td><td>Determination</td></tr><tr><td>Waveguide propagation</td><td>0.80</td><td>Q-factor measurement in a ring resonator on the same chip</td></tr><tr><td>Lensed multimode fiber collection</td><td>5.40</td><td>Coupling test to a straight waveguide</td></tr><tr><td>Detector quantum efficiency</td><td>0.80</td><td>Photodetector documentation</td></tr></table>

![](images/0ce5e6949e4366447372d145937e5177d32154c0f35fb9976ea89e50ca0ed5bf.jpg)  
Fig. 8 | Calculated squeezing with reduced loss. We calculate the expected squeezing for the proposed device with reduced detection and laser coupling loss. We assume a total laser coupling loss of  $0.6\mathrm{dB}$  and a total detection loss of  $0.8\mathrm{dB}$ . The blue line corresponds to the expected squeezing after reducing optical loss in the system. The orange line corresponds to the squeezing achievable with the current system, with  $20\%$  detection efficiency. The shaded areas are accessible with the current integrated DFB laser for both cases.

We summarize all the sources of loss that impact reported total detection efficiency in Table 1. In our measurement, the main limitation is a result of the loss at the interface between the chip facet and collection fibers.

Reducing the overall losses in the system is a straightforward way to improve the device's performance. Reducing the fiber-to-chip coupling loss down to  $0.6\mathrm{dB}$  has been established by engineering the waveguide termination[40-42]. Moreover, the propagation loss can be reduced to  $0.2\mathrm{dB}$  by reducing the waveguide length where the squeezed state can experience loss. The quantum efficiency of the detector used in this study can be improved to  $99.5\%$  using commercially available photodiodes. We use these values to estimate potentially achievable squeezing in the proposed device. In this case, the total detection loss is  $0.8\mathrm{dB}$ , and the total insertion loss of the laser is  $0.6\mathrm{dB}$ . Using these values, we plot the expected achievable squeezing with respect to the laser power in Fig. 8. Assuming no squeezeer leakage, we compare the calculated values in a system with reduced loss (blue) to the current system with a total detection efficiency of around  $20\%$  (orange). We estimate that the same integrated DFB laser, as we used in the main text, would facilitate access to the blue-shaded region and result in the maximum squeezing factor of 2.8 at the highest achievable on-chip power of  $96\mathrm{mW}$ .

# Fundamental harmonic filter design and characterization

We designed the FH filter based on a directional waveguide coupler. We calculate the coupling ratio by simulating a cross-section of two adjacent waveguides in a finite-element mode solver (COMSOL). We extract effective indices for the symmetric and anti-symmetric modes, their difference defines the coupling strength. Then, we find the length of the coupler necessary to transfer  $100\%$ . We choose the gap between waveguides to avoid SH light coupling. Our design length is  $380\mu \mathrm{m}$  and the gap between waveguides is  $1\mu \mathrm{m}$ .

Due to the fabrication imperfections and bend contributions to the coupling, the actual devices differ from the ideal design. We verify the filter performance experimentally by including it inside a racetrack resonator with a total length of around  $2\mathrm{mm}$ , as shown in the inset of Fig. 9a. The filter contributes to the intrinsic loss of the cavity and has a clear wavelength dependence. We measure it by sweeping a tuneable laser coupled to a bus waveguide and fitting lorentzians to the cavity modes. Figure 9a shows the measured intrinsic quality factors. Assuming that the propagation loss of the waveguide is constant across our measurement bandwidth of  $1480 - 1620\mathrm{nm}$ , we extract the

![](images/702465671abd00504cb80b0dc83f0a577f15f6dc2bd68a392f906e4b8346bd9c.jpg)

![](images/4c20521dde8b7e4608c90e70a3a529bfce54d0ab542f6f9f6793ace76864024c.jpg)  
Fig. 9 | Fundamental harmonic filter characterization. a Measured intrinsic quality factors of a snail resonator as a function of wavelength. The inset shows resonator design—the characterized filter is a part of the cavity and contributes to the intrinsic loss. b Extracted filter transmission based on the cavity measurements. The filter's transmission at  $1544\mathrm{nm}$  is around  $(8\pm 1)\%$ . Increased loss at around 1535 and  $1610\mathrm{nm}$  results from cavity mode crossing and is unrelated to the filter.

loss contribution from the coupler and plot it in Fig. 9b. The fabricated devices perform best at around  $1585\mathrm{nm}$  and transmit around  $(8\pm 1)\%$  of light at the squeezezer subsystem operation wavelength of  $1544\mathrm{nm}$ . We use three back-to-back filters in the squeezezer subsection and observe a suppression of around  $18\mathrm{dB}$ . The excess leakage can result from fabrication imperfections and stray light coupling into the system. The increased density of waveguides in the squeezing PIC can result in more severe electron beam proximity effects and changes in the coupler dimensions. Stray light can propagate in the slab or insulator layer and be parasitically coupled to the circuit.

# Data availability

The data sets generated during and/or analyzed during this study are available from the corresponding author on request.

# References

1. Andersen, U. L., Gehring, T., Marquardt, C. & Leuchs, G. 30 years of squeezed light generation. Phys. Scr. 91, 053001 (2016).  
2. Caves, C. M., Thorne, K. S., Drever, R. W., Sandberg, V. D. & Zimmermann, M. On the measurement of a weak classical force coupled to a quantum-mechanical oscillator. I. Issues of principle. Rev. Mod. Phys. 52, 341-392 (1980).  
3. Giovannetti, V., Lloyd, S. & Maccone, L. Quantum-enhanced measurements: beating the standard quantum limit. Science 306, 1330-1336 (2004).  
4. Giovannetti, V., Lloyd, S. & Maccone, L. Quantum metrology. Phys. Rev. Lett. 96, 010401 (2006).  
5. Goda, K. et al. A quantum-enhanced prototype gravitational-wave detector. Nat. Phys. 4, 472-476 (2008).  
6. Aasi, J. et al. Enhanced sensitivity of the ligo gravitational wave detector by using squeezed states of light. Nat. Photonics 7, 613-619 (2013).  
7. Guo, X. et al. Distributed quantum sensing in a continuous-variable entangled network. Nat. Phys. 16, 281-284 (2020).  
8. Taylor, M. A. et al. Biological measurement beyond the quantum limit. Nat. Photonics 7, 229-233 (2013).  
9. Casacio, C. A. et al. Quantum-enhanced nonlinear microscopy. Nature 594, 201-206 (2021).  
10. Zhang, M., Wang, C., Cheng, R., Shams-Ansari, A. & Lončar, M. Monolithic ultra-high-q lithium niobate microring resonator. Optica 4, 1536-1537 (2017).

11. Wang, C. et al. Ultrahigh-efficiency wavelength conversion in nanophotonic periodically poled lithium niobate waveguides. Optica 5, 1438-1441 (2018).  
12. Lu, J., Li, M., Zou, C.-L., Sayem, A. A. & Tang, H. X. Toward  $1\%$  single-photon anharmonicity with periodically poled lithium niobate microring resonators. Optica 7, 1654-1659 (2020).  
13. Mishra, J. et al. Mid-infrared nonlinear optics in thin-film lithium niobate on sapphire. Optica 8, 921-924 (2021).  
14. Park, T. et al. High-efficiency second harmonic generation of blue light on thin-film lithium niobate. Opt. Lett. 47, 2706-2709 (2022).  
15. Lu, J. et al. Ultralow-threshold thin-film lithium niobate optical parametric oscillator. Optica 8, 539-544 (2021).  
16. McKenna, T. P. et al. Ultra-low-power second-order nonlinear optics on a chip. Nat. Commun. 13, 4532 (2022).  
17. Jankowski, M. et al. Ultrabroadband nonlinear optics in nanophotonic periodically poled lithium niobate waveguides. Optica 7, 40-46 (2020).  
18. Jankowski, M., Mishra, J. & Fejer, M. M. Dispersion-engineered  $\chi(2)$  nanophotonics: a flexible tool for nonclassical light. J. Phys. Photonics 3, 042005 (2021).  
19. Mishra, J. et al. Ultra-broadband mid-infrared generation in dispersion-engineered thin-film lithium niobate. Opt. Express 30, 32752-32760 (2022).  
20. Wang, C. et al. Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages. Nature 562, 101-104 (2018).  
21. Celik, O. T. et al. High-bandwidth CMOS-voltage-level electro-optic modulation of 780 nm light in thin-film lithium niobate. Opt. Express 30, 23177-23186 (2022).  
22. Zhang, M. et al. Broadband electro-optic frequency comb generation in a lithium niobate microring resonator. Nature 568, 373-377 (2019).  
23. Boyd, R. W. Nonlinear Optics 3rd edn (Academic Press, 2008).  
24. Wu, L.-A., Kimble, H. J., Hall, J. L. & Wu, H. Generation of squeezed states by parametric down conversion. Phys. Rev. Lett. 57, 2520-2523 (1986).  
25. Kaiser, F., Fedrici, B., Zavatta, A., d'Auria, V. & Tanzilli, S. A fully guided-wave squeezing experiment for fiber quantum networks. Optica 3, 362-365 (2016).  
26. Kashiwazaki, T. et al. Continuous-wave 6-db-squeezed light with 2.5-thz-bandwidth from single-mode PPLN waveguide. APL Photonics 5, 036104 (2020).  
27. Safavi-Naeini, A. H. et al. Squeezed light from a silicon micromechanical resonator. Nature 500, 185-189 (2013).  
28. Dutt, A. et al. On-chip optical squeezing. Phys. Rev. Appl. 3, 044005 (2015).  
29. Vaidya, V. D. et al. Broadband quadrature-squeezed vacuum and nonclassical photon number correlations from a nanophotonic device. Sci. Adv. 6, eaba9186 (2020).  
30. Zhang, Y. et al. Squeezed light from a nanophotonic molecule. Nat. Commun. 12, 2233 (2021).  
31. Lenzini, F. et al. Integrated photonic platform for quantum information with continuous variables. Sci. Adv. 4, eaat9331 (2018).  
32. Chen, P.-K., Briggs, I., Hou, S. & Fan, L. Ultra-broadband quadrature squeezing with thin-film lithium niobate nanophotonics. Opt. Lett. 47, 1506-1509 (2022).  
33. Nehra, R. et al. Few-cycle vacuum squeezing in nanophotonics. Science 377, 1333-1337 (2022).  
34. de Beeck, C. O. et al. III/V-on-lithium niobate amplifiers and lasers. Optica 8, 1288-1289 (2021).  
35. Li, M. et al. Integrated pockels laser. Nat. Commun. 13, 5344 (2022).  
36. Tasker, J. F. et al. Silicon photonics interfaced with integrated electronics for 9 GHz measurement of squeezed light. Nat. Photonics 15, 11-15 (2021).

37. Kuo, P. S. Noncritical phasematching behavior in thin-film lithium niobate frequency converters. Opt. Lett. 47, 54-57 (2021).  
38. Zhu, D. et al. Integrated photonics on thin-film lithium niobate. Adv. Opt. Photonics 13, 242-352 (2021).  
39. Wang, M. et al. Thin-film lithium-niobate modulator with a combined passive bias and thermo-optic bias. Opt. Express 30, 39706-39715 (2022).  
40. He, L. et al. Low-loss fiber-to-chip interface for lithium niobate photonic integrated circuits. Opt. Lett. 44, 2314-2317 (2019).  
41. Hu, C. et al. High-efficient coupler for thin-film lithium niobate waveguide devices. Opt. Express 29, 5397-5406 (2021).  
42. Ying, P. et al. Low-loss edge-coupling thin-film lithium niobate modulator with an efficient phase shifter. Opt. Lett. 46, 1478-1481 (2021).  
43. Krause, A. G., Winger, M., Blasius, T. D., Lin, Q. & Painter, O. A high-resolution microchip optomechanical accelerometer. Nat. Photonics 6, 768-772 (2012).  
44. Hanay, M. S. et al. Single-protein nanomechanical mass spectrometry in real time. Nat. Nanotechnol. 7, 602-608 (2012).  
45. Gehring, T. et al. Implementation of continuous-variable quantum key distribution with composable and one-sided-device-independent security against coherent attacks. Nat. Commun. 6, 8795 (2015).  
46. Zhong, H.-S. et al. Quantum computational advantage using photons. Science 370, 1460-1463 (2020).  
47. Zhong, H.-S. et al. Phase-programmable gaussian boson sampling using stimulated squeezed light. Phys. Rev. Lett. 127, 180502 (2021).  
48. Nagy, J. T. & Reano, R. M. Reducing leakage current during periodic poling of ion-sliced x-cut MgO doped lithium niobate thin films. Opt. Mater. Express 9, 3146-3155 (2019).  
49. Shams-Ansari, A. et al. Reduced material loss in thin-film lithium niobate waveguides. APL Photonics 7, 081301 (2022).

# Acknowledgements

This work was supported in part by the Defense Advanced Research Projects Agency (DARPA) LUMOS program (Grant No. HR0011-20-2-0046, received by A.H.S.-N.) and the DARPA Young Faculty Award (YFA, Grant No. D19AP00040, received by A.H.S.-N.). We also thank NTT Research for their financial and technical support, and the US Department of Energy for their support through Grant No. DE-AC02-76SF00515, received by A.H.S.-N. In addition, the US Air Force Office of Scientific Research provided a MURI grant (Grant No. FA9550-17-1-0002, received by A.H.S.-N.) that supported this research. H.S.S. acknowledges support from the Urbanek Family Fellowship, and V.A. was partially supported by the Stanford Q-Farm Bloch Fellowship Program. This work was also performed at the Stanford Nano Shared Facilities (SNSF), supported by the National Science Foundation under award ECCS-2026822. We also acknowledge the Q-NEXT DOE NQI Center and the David and Lucille Packard Fellowship for their support. D.D.

acknowledges support from the NSF GRFP (No. DGE-1656518). H.S.S. and V.A. thank Kevin Multani, Christopher Sarabalis, and Michael Stefszky for discussions and technical support.

# Author contributions

H.S.S. designed the device. H.S.S., T.P., and A.Y.H. fabricated the device. H.S.S., V.A., T.P.M., and O.T.C. developed the fabrication process. M.M.F. and A.H.S.-N. provided experimental and theoretical support. H.S.S., V.A., T.P., and D.J.D. performed the experiments and analyzed the data. H.S.S., V.A., and A.H.S.-N. wrote the manuscript. H.S.S., V.A., T.P.M., and A.H.S.-N. conceived the experiment, and A.H.S.-N. supervised all efforts.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-023-38246-6.

Correspondence and requests for materials should be addressed to Amir H. Safavi-Naeini.

Peer review information Nature Communications thanks the anonymous reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023