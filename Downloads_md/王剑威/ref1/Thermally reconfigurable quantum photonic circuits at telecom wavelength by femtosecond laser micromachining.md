# ORIGINAL ARTICLE

# Thermally reconfigurable quantum photonic circuits at telecom wavelength by femtosecond laser micromachining

Fulvio Flamini<sup>1</sup>, Lorenzo Magrini<sup>1</sup>, Adil S Rab<sup>1</sup>, Nicolò Spagnolo<sup>1</sup>, Vincenzo D'Ambrosio<sup>1</sup>, Paolo Mataloni<sup>1</sup>, Fabio Sciarrino<sup>1</sup>, Tommaso Zandrini<sup>2,3</sup>, Andrea Crespi<sup>2,3</sup>, Roberta Ramponi<sup>2,3</sup> and Roberto Osellame<sup>2,3</sup>

The importance of integrated quantum photonics in the telecom band is based on the possibility of interfacing with the optical network infrastructure that was developed for classical communications. In this framework, femtosecond laser-written integrated photonic circuits, which have already been assessed for use in quantum information experiments in the 800-nm wavelength range, have great potential. In fact, these circuits, being written in glass, can be perfectly mode-matched at telecom wavelength to the in/out coupling fibers, which is a key requirement for a low-loss processing node in future quantum optical networks. In addition, for several applications, quantum photonic devices must be dynamically reconfigurable. Here, we experimentally demonstrate the high performance of femtosecond laser-written photonic circuits for use in quantum experiments in the telecom band, and we demonstrate the use of thermal shifters, which were also fabricated using the same femtosecond laser, to accurately tune such circuits. State-of-the-art manipulation of single- and two-photon states is demonstrated, with fringe visibilities greater than  $95\%$ . The results of this work open the way to the realization of reconfigurable quantum photonic circuits based on this technological platform.

Light: Science & Applications (2015) 4, e354; doi:10.1038/Isa.2015.127; published online 20 November 2015

Keywords: femtosecond laser micromachining; integrated quantum photonics; thermal shifters; tunable optical circuits

# INTRODUCTION

The inherent advantages of using photons to encode information in computing applications $^{1-4}$  and to implement future quantum networks $^{5,6}$  have recently drawn increasing attention to the field of quantum optics. In particular, significant progress has been made recently in the use of integrated photonic circuits as a stable and compact platform for producing quantum optical devices $^{7-11}$ . Among the different fabrication technologies used to produce integrated optical circuits, the femtosecond laser writing technique is rapidly attaining a relevant role because of its several advantages $^{8,12,13}$ . In fact, this maskless technique allows one to rapidly prototype high-quality photonic circuits in glass with a very fast optimization loop; this technique is also a cost-effective process. This technique produces low birefringence waveguides, which are required for the polarization encoding of single photons $^{14-16}$ , and has unique three-dimensional capabilities that enable unprecedented device layouts $^{17-19}$ . Using this technology for devices operating in the telecom band can add further advantages because the insertion losses of these devices in an optical fiber network are very low, due to the almost perfect mode matching and the reduced propagation losses $^{20,21}$ . The quality of photonic circuits written via femtosecond lasers has been proven by the demonstration of several classical devices in glass as waveguide amplifiers, lasers, broadband couplers, and demultiplexers $^{22-25}$ , as well as the writing of electro-optic modulators in

crystals $^{26,27}$ . Although this fabrication technology has been widely used to produce quantum devices in the 800-nm wavelength range, no investigation on the performances of these devices at telecom wavelengths in the quantum regime has been performed.

For future application of integrated photonic devices to quantum information processing, a very important feature is the reconfigurability of such devices[9,11,28-33]. This capability could bring a two-fold advantage: on the one hand, reconfigurability is very useful when compensating for errors due to fabrication tolerances; on the other hand, reconfigurability allows one to implement several quantum protocols that require changing the functionality of the circuit dynamically. In the first case, a static compensation is necessary; in the second case, the required device reconfiguration rate is rather low due to the currently limited brightness of multiphoton sources, which lead to the requirement of long measurement times. Thus, thermal tuning is considered a convenient choice because of its simple implementation and its stability. In fact, thermal shifters are widely used in several integrated photonic platforms, which range from silicon photonics to silica-on-silicon[9,11,28-30]; however, they have never been used in femtosecond laser-written circuits.

In this work, we report the fabrication, characterization, and application of a reconfigurable integrated photonic circuit for quantum information at telecom wavelengths. Femtosecond laser micromachining is used to inscribe waveguide Mach-Zehnder

interferometers in a glass chip and to pattern gold resistive heaters on the chip surface. A reliable modeling of the thermal tuning process is reported, and a full experimental characterization of the response of the interferometers is performed by injecting coherent light and monitoring the output. Moreover, tunable Hong-Ou-Mandel (HOM) interference and super-resolved fringes based on N00N states are successfully demonstrated with two-photon input states.

# MATERIALS AND METHODS

# Fabrication of the integrated device

The fabrication process of the reconfigurable devices consists of three steps: fabrication of the three-dimensional waveguide circuits by femtosecond laser writing, deposition of a gold layer on the surface of the sample, and patterning of the surface metallic layer (again realized with femtosecond laser pulses) to define the resistor shape (Figure 1). Waveguides are fabricated in Corning EAGLE2000 alumino-borosilicate glass substrate using a Yb:KYW cavity-dumped mode-locked laser oscillator, that produces pulses at a wavelength of  $1030\mathrm{nm}$ , a duration of 300 fs, and a repetition rate of  $1\mathrm{MHz}$ . To inscribe the waveguides, pulses with  $330\mathrm{nJ}$  of energy per pulse were focused by a  $50\times$  objective  $(\mathrm{NA} = 0.6)$ , while the substrate was translated at a translation speed of  $20\mathrm{mm~s^{-1}}$  (three-axes translation stage, Aerotech ANT). The fabricated waveguides yield single-mode operation at  $1550\mathrm{nm}$ , with a mode diameter  $(1/e^{2})$  of approximately  $13.5\mu \mathrm{m}$  and propagation losses of approximately  $0.6\mathrm{dB~cm^{-1}}$ . Such a mode size enables coupling losses to standard single-mode telecom fibers of  $0.2\mathrm{dB}$  per facet (retrieved from the overlap integral of the measured mode-intensity profiles for waveguides and fibers $^{34}$ ).

The interferometers are composed of two cascaded directional couplers, inscribed at a  $70~\mu \mathrm{m}$  depth below the substrate surface, in which the two waveguides are brought as close as  $14~\mu \mathrm{m}$  for a length of  $200~\mu \mathrm{m}$  to achieve a balanced splitting ratio. Between the couplers, the waveguides are straight and separated by  $1.02\mathrm{mm}$  for a 12-mm-long segment. Such straight segments have different depths in the two arms: one is brought up to a depth of  $25~{\mu\mathrm{m}}$  such that it is closer to the surface where resistors are placed, and the other is brought down to a depth of  $115~{\mu\mathrm{m}}$ . Curved waveguide segments consist of sinusoidal bends, with a minimum curvature radius of  $60~\mathrm{mm}$ . The overall length of the chip is  $45~\mathrm{mm}$ ; the thickness is  $1\mathrm{mm}$ . This geometry for the interferometers, which presents two quite long and well-separated straight segments in the central part, was chosen to facilitate the characterization of thermal diffusion effects and model the operation of the thermal shifter, as described in the section on "Results and discussion". Much more compact devices could be realized by choosing a smaller separation between the waveguides in the central part and by minimizing the length of the straight segments. Ablation lines were also machined on the substrate surface immediately following the waveguide inscription to serve as alignment markers for the following processes.

A 50-nm-thick gold layer was deposited on the substrate surface using a sputter coater (Cressington 108auto). The resistor pattern was defined by laser ablation, focusing on the sample surface the same femtosecond laser beam used for waveguide inscription. Here,  $100\mathrm{-nJ}$  pulses were used, with a translation speed of  $1\mathrm{mm~s^{-1}}$ . Each laser scan produces a  $2.7\mathrm{-}\mu \mathrm{m}$ -wide ablation line in the gold layer, with negligible damage of the glass surface. To safely isolate each resistor from the neighboring ones, nine successive scans, spaced by  $0.5\mu \mathrm{m}$ , were performed. Six rectangular resistors ( $0.3\mathrm{mm}$  wide and  $20\mathrm{mm}$  long) were inscribed on the sample surface, terminating with the larger

![](images/0e0b0c7dd25674964eb9fe7cec21c4f9900631ccc450d77538a629b461553e2d.jpg)

![](images/c1bc55e962b46b1a13fe46a8f934918269b7d2c3a047375303f10dd24226126e.jpg)  
Figure 1 Femtosecond laser microfabrication process. (a) Direct writing of Mach-Zehnder interferometers in the bulk of a borosilicate slide. (b) After gold coating the sample top surface, the resistors are patterned by ablation using the same femtosecond laser. Accurate alignment  $(\sim 1\mu \mathrm{m})$  between the resistors and the Mach-Zehnder arms is achieved by using the reference markers inscribed on the glass surface together with the interferometers.

areas that were used to facilitate the electric connection to external circuits. Each resistor is placed just above one interferometer's arm. Some of the fabricated interferometers had two resistors that were placed above each of the two arms; other interferometers were inscribed at different distances from the resistors to allow a wider experimental investigation on the influence of the heaters on interferometers under different geometric conditions.

The resistance of the fabricated heaters was measured to have an average value of  $67\Omega$  for the resistor and  $13\Omega$  for the plates and connections. The chip was mounted on an aluminum base  $(4.5\mathrm{cm}\times 6\mathrm{cm}\times 1\mathrm{cm})$ , which served as a thermostat to stabilize the boundary temperature during the device operation.

# Characterization setup

The fabricated devices were first characterized with classical light input. For this purpose, light from a tunable laser source (Santec MLS-2000), set at a wavelength of  $1550\mathrm{nm}$ , was injected in the chosen device input by a standard telecom fiber. The output light from the chip was collected by a 0.65 NA objective. For static measurements,

both outputs of the interferometer were simultaneously monitored using two photodiode heads of a Coherent LabMaster Ultima power meter, and the driving voltage to the resistors was provided by a TDK-Lambda Zup 6-66 stabilized power supply. Both the optical power meter and the voltage supply were computer controlled, which allowed for the complete automation of the voltage scans used to characterize the static thermal response of the interferometers. The same setup was used for the stability measurement. In contrast, to measure the dynamic step response, the resistor was driven by a function generator (Textronix CFG 280). An InGaAs photodiode (Thorlabs PDB410C) was used as the detector and was connected to an oscilloscope (Tektronix DPO 2024B); a single output of the interferometer was monitored for this measurement.

For the characterization with quantum light, couples of horizontally polarized identical photons were generated at a wavelength of  $1550\mathrm{nm}$  via spontaneous parametric down-conversion (SPDC) in a Type-I bismuth borate (BiBO) biaxial crystal[31] (Figure 2a). The crystal was pumped by 160-fs laser pulses at a repetition rate of  $76\mathrm{MHz}$ , from a Ti:Sapphire oscillator  $(775\mathrm{nm}$  wavelength), with the possibility to switch to CW mode. Typical detected count rates were approximately  $16\mathrm{kHz}$  for singles and  $0.5\mathrm{kHz}$  for coincidences in the pulsed regime, with an incident average power of  $600\mathrm{mW}$ , and they were approximately  $17\mathrm{kHz}$  for singles and  $2\mathrm{kHz}$  for coincidences in CW mode, with an incident power of  $900\mathrm{mW}$ . Longpass (LPF) and bandpass (BPF,  $8.8\mathrm{nm}$  bandwidth centered at  $1550\mathrm{nm}$ ) interference filters were used in each of the SPDC modes to perform a narrow wavelength selection prior to injection into single-mode fibers for spatial selection. A pair of delay lines (Figure 2; each equipped with a set of waveplates) was used for path synchronization and polarization compensation.

Input and output coupling to the chip was performed using a pair of fiber arrays, each of which was mounted onto a micrometric rototranslational stage.

Detection was performed by a pair of InGaAs/InP single-photon avalanche detectors (ID210 by ID Quantique). Coincidences were counted by an external electronic board, connected to a computer for data analysis. The details of the detectors operation are reported in Supplementary Note 1.

The indistinguishability of the down-converted photons was tested by performing HOM interference measurements $^{35}$  in a symmetric 50/50 single-mode fiber beam-splitter, in both the pulsed and CW regimes. Raw visibility values were  $\mathcal{V}_{HOM}^{(1,1)} = 0.967 \pm 0.002$  in the CW regime at an incident power of  $800~\mathrm{mW}$  and  $\mathcal{V}_{HOM}^{(1,1)} = 0.923 \pm 0.004$  in the pulsed regime at an average incident power of  $200~\mathrm{mW}$  ( $\mathcal{V}_{HOM}^{(1,1)} = 0.986 \pm 0.002$  and  $\mathcal{V}_{HOM}^{(1,1)} = 0.994 \pm 0.006$  by correcting for the accidental coincidences in CW and pulsed mode, respectively), comparable to what has been observed in the literature $^{31,36}$ . The visibility  $\mathcal{V}_{HOM}^{(i,j)}$  is defined as  $\mathcal{V}_{HOM}^{(i,j)} = \left(N_{clas}^{(i,j)} - N_{quan}^{(i,j)}\right) / N_{clas}^{(i,j)}$ , where  $N_{clas}^{(i,j)}$  and  $N_{quan}^{(i,j)}$  is the number of detected coincidences for distinguishable photons and indistinguishable photons, respectively. The superscript  $(i,j)$  denotes the number of photons  $i$  and  $j$  measured on the output modes of the device.

# RESULTS AND DISCUSSION

# Device operation

A relative phase delay is induced between the arms of the interferometer by the temperature increase caused by the resistive heater. Given the linearity of the heat equation, which governs the heat diffusion from the resistor in the glass, the temperature variation in a certain point of the glass is proportional to the dissipated power  $\mathcal{P}$

(Supplementary Note 2). The temperature-induced refractive index variation in the glass is also linear, at least in the limited temperature operation range considered in this study. Thus, the induced phase difference between the arms  $\phi = \varphi_{1} - \varphi_{2}$  is linear with  $\mathcal{P}$ .

Considering a single resistor acting on a single interferometer, for coherent light injected in one input, interference fringes can be observed by monitoring the intensity of either one of the two outputs, as follows:

$$
I _ {o u t} = \frac {I _ {t o t}}{2} [ 1 + \mathcal {V} \cos \phi ] = \frac {I _ {t o t}}{2} [ 1 + \mathcal {V} \cos (\Phi_ {0} + \alpha \mathcal {P}) ] \tag {1}
$$

where  $I_{tot}$  is the sum of the intensities on the two outputs,  $\mathcal{V}$  is the fringe visibility, and  $\varPhi_0$  is a phase term present in the interferometer when no power is applied to the heater and  $\alpha$  is a constant that depends on all the geometric, thermal, and optical properties of the interferometers. The fringe visibility is influenced by several factors, such as the degree of coherence of the input light, the splitting ratio of the directional couplers comprising the interferometers and the differential losses in the two arms. In addition, in the case of ohmic resistive heaters, as in our study, one can write  $\mathcal{P} = \Delta \mathcal{V}^2 /\mathcal{R}$ , where  $\Delta V$  is the imposed voltage on the resistor and  $\mathcal{R}$  is the resistance value. Note that the phase depends on  $\mathcal{P}$  but is independent of the absolute values of the temperatures involved, i.e., the thermal drifts of the environment do not affect the interferometer behavior.

The response of the fabricated interferometers was experimentally characterized as a function of the heat dissipated by the different resistors. For this purpose, laser light was fiber-coupled to one input of each interferometer, and the optical power from both outputs was measured while varying the voltage across the resistor; this process allowed us to fit for each interferometer the relevant parameters,  $\alpha$ ,  $\varPhi_0$ , and  $\nu$ , in Equation (1). Figure 3 shows the normalized output intensity,  $\bar{I} = I_{out} / I_{tot}$ , for the interferometer as a function of the power dissipated by a resistor placed directly above its shallower arm. A best fit of Equation (1) yields  $\alpha = 13.43$  rad W $^{-1}$  and  $\varPhi_0 = 0.837$  rad, and the fringe visibility is  $\nu = 0.964 \pm 0.003$ . The good agreement between the fitting curve and the experimental points confirms the linearity of the differential phase  $\phi$  with the dissipated power, as theoretically discussed above. Although the Mach-Zehnder interferometer is nominally balanced, we observe a value of  $\varPhi_0 \neq 0$ . This observation can be explained by the fact that the two arms of the interferometer are written at different depths in the glass substrate. In fact, small variations in the spherical aberrations of the writing beam are responsible for a slightly different refractive index change being induced in the two arms, thus resulting in the  $\varPhi_0$  phase bias.

The experimental calibration previously discussed is necessary to retrieve the precise  $\alpha$  and  $\varPhi_0$  values for a given device; however, it may also be desirable to develop simple models to estimate a priori the thermal response of the interferometers, at least for a certain standard circuit geometry. In fact, such models would greatly facilitate the design of more complex reconfigurable circuits. Below, we discuss a simple analytical model that is applicable to our circuit layout.

Assuming a wire-like heater and neglecting power dissipation from the top surface of the glass (air is an insulator), a logarithmic decay law for the temperature as a function of the distance from the heater can be easily determined (see Supplementary Note 2). The latter approximates well the temperature distribution around the resistor, as confirmed by comparison with a numerical simulation of the heat diffusion (Supplementary Fig. S1). Within this simplified model, an analytic expression for  $\alpha$  in Equation (1) can be

![](images/9fa04f2f35c35f71d467b35a70825eba00a9c00a05f98ee18dab258ed9500f08.jpg)  
a

![](images/e6d7d07d8ecee3107610e9857e09c4f2da9e311f73f4088a19b2793d9dd1279c.jpg)  
b

![](images/66aa041f8123b1933385f8b4ca895516ea9ed044bacb16e850e3af7514851930.jpg)  
C

![](images/491ca9f79c283d1b35dcbcdd455304e40cdae5bc1dda046984015dd01c60739f.jpg)  
Figure 2 Setup for device characterization with quantum light in the telecom band. (a) Schematic of the two-photon source adopted in the experiment: pairs of photons are emitted in two different spatial modes and injected into single-mode fibers. L, lens (50 cm focal length); P, pinhole; BiBO, bismuth borate crystal; BPF, band pass filter; LPF, long pass filter; PBS, polarizing beam splitter; WPs, wave plates for polarization compensation. (b) The generated photons are injected in spatial delay lines for temporal synchronization and propagate through a set of waveplates for polarization compensation. (c) Single-mode fiber arrays (SMFA) are used to inject the photons in both of the interferometer's inputs and to collect photons from both output modes. (d) Schematic of the integrated tunable Mach-Zehnder interferometer. The phase  $\phi$  in the interferometer is controlled by tuning the driving voltage on the resistive heating plate placed on the chip surface.  
d

derived, given the distances  $\rho_{1}$  and  $\rho_{2}$  of the interferometer's arms from the heater:

$$
\alpha = \frac {2 n _ {T}}{\lambda} \frac {1}{\kappa} \frac {L _ {\text {a r m}}}{L _ {\text {w i r e}}} \ln \frac {\rho_ {1}}{\rho_ {2}} \tag {2}
$$

where  $\kappa$  is the thermal conductivity of the glass substrate,  $n_{T}$  is its thermo-optic coefficient,  $\lambda$  is the wavelength,  $L_{arm}$  is the length of the straight segments in the interferometer's arms, and  $L_{wire}$  is the length of the wire-like heater. The  $\alpha$  coefficients were experimentally characterized for different couples of interferometers and resistors and had different ratios of  $\rho_{1}$  over  $\rho_{2}$ . Equation (2) was found to predict the experimental values with an average accuracy of  $10\%$  (see Supplementary Fig. S2). Thus, this simple model can be used as a robust approximation for designing circuits and estimating the influence of the wire-like resistive heaters on interferometers that are placed at different distances from the heaters.

In the case of the use of several resistive heaters (and several interferometers) on the same substrate, cross-talk among the heaters is possible for each interferometer due to the combined effects of the different heaters. However, from the linearity of the heat equation, one can easily infer the phase  $\phi$  induced on a single interferometer as:

$$
\phi = \varphi_ {1} - \varphi_ {2} = \Phi_ {0} + \sum_ {i} \alpha_ {i} \mathcal {P} _ {i} \tag {3}
$$

where  $\mathcal{P}_i$  is the dissipated powers from the different resistors. Note that the interferometer is influenced in principle by all of the heaters but with different constants, depending on the geometric configuration. Of course,  $\alpha_{i}$  for distant heaters is expected to be negligible. However, the influence of each heater to each interferometer could be characterized independently (thus characterizing the various  $\alpha_{i}$ ), and the combined behavior could be predicted simply by adding the different contributions. This modeling approach was confirmed experimentally by measuring the output of an interferometer under the action of two heaters, one placed above its shallower arm and one placed above its deeper arm (see Supplementary Fig. S3). This showed that the response can be accurately predicted, even in the case of strong cross-talk among the different heaters on the same interferometer.

The operation of multiple heaters on the same chip is also not a problem from the heat sinking point of view; in fact, the power that must be dissipated is rather low because a  $2\pi$  phase shift in a single interferometer is achieved with only 0.5 W (Figure 3). In addition, the circuit reconfiguration, even for a repeated number of times, does not affect the alignment between the chip and the input optical fibers. In fact, the induced temperature variations are on the order of ten degrees Celsius and are localized around the heater; thus, they do not induce significant deformation of the whole chip.

In applications such as quantum optics experiments, where measurements may take from several minutes to several hours or days, operational stability is crucial for a reconfigurable circuit. The operation of the interferometer was monitored for  $10\mathrm{h}$  under constant voltage driving conditions, imposing a phase of approximately  $\pi /2$  where the sensitivity to variations in voltage is maximum (Supplementary Fig. S4): the observed phase fluctuations were smaller

![](images/b6da668c9f8f9c7679e14c8ab3795b21c030b913d84cc1b137c1c29773440dce.jpg)  
Figure 3 Experimental characterization of the interferometer operation with classical light at a wavelength of  $1550\mathrm{nm}$ . The transmission of the interferometer in the cross-arm is plotted as a function of the thermal power dissipated by the resistor. The best fit of the data with the function reported in Equation (1) is also shown as a solid line.

![](images/e6d6bb3068f4fa03de52079510da95c06dc3cb2e7ea7d50477a2c70cc8ba58b9.jpg)  
Figure 5 HOM interference experiment for input state  $|1,1\rangle$  at  $\Delta V\simeq 1.97\mathrm{V}\left(\phi \sim \frac{\pi}{2}\right)$ . Blue points: coincidences for output (1, 1). Green points: coincidences of output (0, 2). Solid lines: best fit of the measured data. Horizontal lines: levels for the contribution of accidental coincidences. The error bars are given by Poissonian statistics.

![](images/af7e0a39876ae4d1873fe6ea350350e50bddea4ff7af2af831f871b732894e05.jpg)  
Figure 4 (a) Experimental measurement of a single-photon fringe pattern for input mode 1 and output mode 2 as a function of the dissipated power. Points: normalized counts. Solid red curve: best fit of the measured data with a sinusoidal function. Horizontal red line: estimated contribution of accidental coincidences. (b) Experimental fringe pattern for a two-photon input  $[1,1)$  as a function of the dissipated power. Blue points: normalized coincidences of the output  $(1,1)$ , with one photon for each output port; the statistics of the recorded data was  $\sim 1200$  coincidences for the fringe maximum in  $120\mathrm{s}$ . Green points: normalized coincidences of the output  $(0,2)$ , with two photons on output port 2; the statistics of the recorded data was  $\sim 600$  coincidences for the fringe maximum in  $180\mathrm{s}$ . Both fringes show twice the periodicity of single-photon ones (dashed red curve). Solid lines: best fit of the measured data with a sinusoidal function. Horizontal blue and green lines: estimated contribution of accidental coincidences. The error bars are given by Poissonian statistics.

than 0.01 rad, with no evidence of drifts. Finally, the response of the device to a voltage step was also characterized (Supplementary Fig. S5), which revealed a rise time of  $\sim 0.9$  s (10%–90% of the variation). This result indicates that the circuit is completely settled to a new configuration within a few seconds.

# Two-photon interference

The overall action  $U^{theo}$  of an ideal Mach-Zehnder interferometer on the input-output modes  $b_{i}^{\dagger} = \sum_{j}U_{i,j}^{theo}a_{j}^{\dagger}$ , being  $a_{i}^{\dagger}$  and  $b_{i}^{\dagger}$  the field operators for the input and output modes, respectively, is described by:

$$
U ^ {t h e o} = \left( \begin{array}{c c} \sin \phi & \cos \phi \\ \cos \phi & - \sin \phi \end{array} \right) \tag {4}
$$

where the global phase factor  $t e^{-t\phi /2}$  is removed.

![](images/47dfc74aa5ab086940b59caed4c47aac3e2c13125a92e181a64cca4abe7abec0.jpg)

We first measured single-photon fringe patterns by injecting a heralded single photon into input port 1 and measuring the triggered count rate at output port 2 (Figure 4a). The measured raw visibility was  $\mathcal{V} = 0.930 \pm 0.006$  ( $\mathcal{V} = 0.981 \pm 0.007$ , correcting for the accidental coincidences), compatible with the one performed with classical light. We then recorded the interference fringes obtained by injecting two photons into the device in a  $|1,1\rangle$  state, where  $|i,j\rangle$  denotes  $i$  ( $j$ ) photons on input port 1 (2). In this case, after the first beam-splitter, the state evolves into a two-photon N00N state  $\propto (|2,0\rangle - |0,2\rangle)$ . The action of the phase shift changes the state into  $\propto (|2,0\rangle - e^{-i2\phi} |0,2\rangle)$ . The fringe pattern recorded in the twofold coincidences after the recombination in the second beam-splitter, corresponding to the measurement of the  $(1,1)$  output state, led, as expected, to a halved period with respect to the single-photon case. The experimental fringe pattern is shown in Figure 4b. We measured an experimental raw visibility  $\mathcal{V}_{N00N}^{(1,1)} = 0.864 \pm 0.007$  ( $\mathcal{V}_{N00N}^{(1,1)} = 0.913 \pm 0.006$  by subtracting the accidental coincidences), showing the correct operation of the integrated interferometer. The visibility  $\mathcal{V}_{N00N}^{(1,1)}$  is defined as  $\mathcal{V}_{N00N}^{(1,1)} = \left(N_{max}^{(i,j)} - N_{min}^{(i,j)}\right) / \left(N_{max}^{(i,j)} + N_{min}^{(i,j)}\right)$ , where the subscripts refer to the maximum and the minimum number of coincidences measured scanning the phase  $\phi$ .

We then measured the events in which the two photons emerge from the same output port 2 by connecting it to a symmetric  $50/50$  fiber beam-splitter and by collecting two-fold coincidences between the output of the beam-splitter. The results are shown in Figure 4b: the  $(0,2)$  output contribution exhibits the same super-resolved two-fold pattern with opposite relative phase with respect to the  $(1,1)$  contribution. The measured visibility was  $\mathcal{V}_{N00N}^{(0,2)} = 0.882 \pm 0.008$ , which increases to  $\mathcal{V}_{N00N}^{(0,2)} = 0.949 \pm 0.007$  after subtracting the contribution from accidental coincidences.

To assess the non-classicality of the observed super-resolved two-photon interference fringes, we applied a recently proposed criterion $^{37}$  that compares the visibility of the pattern with the visibility that can be achieved using classical light. Though it is possible to obtain fringes oscillating as  $2\phi$  with perfect visibility  $\mathcal{V}^{(1,1)} = 1$  with appropriately tailored classical light measuring the (1,1) output contribution, the maximum achievable visibility for the (0,2) output contribution is

![](images/292d4e28511a2ec9b9defd085b66df64588adf00a34e9453f30aa110b51edff6.jpg)  
a  $\phi \simeq 2.08$

![](images/94cb3749abc1046954580cd8eb36ec7f2e3dcb3f60d13e814018bc9ababe6b62.jpg)

![](images/c1553a8225ac8821ab4d3e66c14bd5f4cbb0c2895e5595332773f5e0c16cfba7.jpg)  
b  $\phi \simeq 3.27$

![](images/1cad6646ec0a51504a11cb623588ea880972bda76efa5ae5e147c9a71f9d655c.jpg)

![](images/d821354602f8360d78c8efb69d8a9ba6def38636d693e42a3be4e60dd4242b8d.jpg)  
c  $\phi \simeq 4.77$

![](images/d142d46b7947c0b2f3b750b0aba6d238bbf5463f3f1acebffa8d93812922cac9.jpg)  
Figure 6 Tomography of the interferometer for different values of the phase  $\phi$ . (a) Tomography for  $\phi \simeq 2.08$ . (b) Tomography for  $\phi \simeq \pi$ , where the interferometer behaves as the identity with an additional (-1) phase factor on mode 2. (c) Tomography for  $\phi \simeq \frac{3\pi}{2}$ : the interferometer behaves as a symmetric 50/50 beam-splitter. (d) Tomography for  $\phi \simeq 2\pi$ : the interferometer behaves as a swap operation, exchanging modes 1 and 2. For each panel: red bars correspond to the reconstructed unitary  $U^{exp}$ , while green bars correspond to the ideal unitary  $U^{theo}$ . Light red bars correspond to the error in the reconstruction process.

![](images/f0bdb801bde1411ffaae9cf3f5b1aff9a7f3e1dabdc0b206faf5b40d9329a0ef.jpg)

![](images/6752ef6b3e9d57273e24ca29d572dc92477defefa3cf3ac6de14376c550b3f8c.jpg)

bounded to  $\mathcal{V}_{cl}^{(0,2)} < 1/3$ . The raw visibility  $\mathcal{V}_{N00N}^{(0,2)}$  measured with two-photon input exceeds the classical bound by more than 68 standard deviations (88 for the corrected value  $\mathcal{V}_{N00N}^{(0,2)}$ ) thus showing the quantumness of the observed effect.

We finally performed a HOM interference experiment for a voltage set to  $\Delta V \simeq 1.97\mathrm{V}$ , corresponding to  $\varphi \simeq \pi /2$ , where the interferometer behaves as a 50/50 beam-splitter (Figure 5). We measured both the  $(1,1)$  and  $(0,2)$  output contributions as a function of the optical delay between the photons and obtained experimental raw visibilities of  $\mathcal{V}_{HOM}^{(1,1)} = 0.876 \pm 0.010$  and  $\mathcal{V}_{HOM}^{(0,2)} = -0.925 \pm 0.039$ , respectively ( $\mathcal{V}_{HOM}^{(1,1)} = 0.886 \pm 0.010$  and  $\mathcal{V}_{HOM}^{(0,2)} = -0.976 \pm 0.039$  after correcting for the accidental coincidences). We attribute the reduced visibility to a voltage set that differs slightly from the one corresponding to a 50/50 beam-splitter.

# Tomography of the interferometer

To fully characterize the action of the interferometer, we performed the tomography of the corresponding unitary transformation for different values of the phases  $\phi$ . Tomography of the linear transformation can be performed by applying a recently proposed method[38,39] based on single-photon probability measurements or, equivalently, intensity measurements with classical light, and based on two-photon interference HOM experiments. The action of the unitary linear transformations can then be retrieved by applying a suitable analytical[39], numerical[38], or hybrid[12] algorithm.

In Figure 6, we report the results of the tomographic characterization of the device for four different relevant values of the phase. We observed very good agreement between the expected behavior and the measured one. The average gate fidelity  $= \frac{1}{2}\left[Tr[(U^{theo})^\dagger U^{exp}]\right]$ , calculated for 12 different values of  $\phi$ , is  $\bar{F} = 0.998 \pm 0.001$ , thus verifying the quality of the fabrication process.

# CONCLUSIONS

We demonstrated the fabrication using femtosecond laser micromachining of an integrated Mach-Zehnder interferometer at an operating wavelength of  $1550\mathrm{nm}$ , which can be dynamically reconfigured by thermal shifters. Measurements with classical light, single-photons and two-photon states confirmed the correct operation of the device, including the observation of quantum interference fringes corresponding to a two-photon N00N state. A full characterization of the thermal response of the interferometric circuit was also performed; the results were in good agreement with the expected results from the fabrication design. This device represents a possible building block of future reconfigurable quantum circuits operating in the telecom band, thus paving the way for the use of integrated photonic devices to implement large quantum networks.

While this work was being written, the reconfigurable operation of a femtosecond laser-written interferometer at  $800\mathrm{nm}$  wavelength was reported<sup>40</sup>.

# ACKNOWLEDGEMENTS

This work was supported by the ERC-Starting Grant 3D-QUEST (3D-Quantum Integrated Optical Simulation; grant agreement no. 307783, http://www.3dquest.eu) and by the Marie Curie Initial Training Network PICQUE (Photonic Integrated Compound Quantum Encoding, grant agreement no. 608062, funding Program: FP7-PEOPLE-2013-ITN, http://www.picque.eu).

1 O'Brien JL. Optical quantum computing. Science 2007; 318: 1567-1570.  
2 Walther P, Resch KJ, Rudolph T, Schenck E, Weinfurter H et al. Experimental one-way quantum computing. Nature 2005; 434: 169-176.  
3 Knill E, Laflamme R, Milburn GJ. A scheme for efficient quantum computation with linear optics. Nature 2001; 409: 46-52.  
4 Walmsley IA, Raymer MG. Toward Quantum-information processing with photons. Science 2005; 307: 1733-1734.

5 Duan LM, Lukin MD, Cirac JI, Zoller P. Long-distance quantum communication with atomic ensembles and linear optics. Nature 2001; 414: 413-418.  
6 Kimble HJ. The quantum internet. Nature 2008; 453: 1023-1030.  
7 Politi A, Cryan MJ, Rarity JG, Yu S, O'Brien JL. Silica-on-silicon waveguide quantum circuits. Science 2008; 320: 646-649.  
8 Marshall GD, Politi A, Matthews JCF, Dekker P, Ams M et al. Laser written waveguide photonic quantum circuits. Opt Express 2009; 17: 12546-12554.  
9 Smith BJ, Kundys D, Thomas-Peter N, Smith PGR, Walmsley IA. Phase-controlled integrated photonic quantum circuits. Opt Express 2009; 17: 13516-13525.  
10 Tanzilli S, Martin A, Kaiser F, de Micheli MP, Alibart O et al. On the genesis and evolution of integrated quantum optics. *Laser Photon Rev* 2012; 6: 115-143.  
11 Bonneau D, Engin E, Ohira K, Suzuki N, Yoshida H et al. Quantum interference and manipulation of entanglement in silicon wire waveguide quantum circuits. New J Phys 2012; 14: 045003.  
12 Crespi A, Osellame R, Ramponi R, Giovannetti V, Fazio R et al. Anderson localization of entangled photons in an integrated quantum walk. Nat Photonics 2013; 7: 322-328.  
13 Grafe M, Heilmann R, Perez-Leija A, Keil R, Dreisow F et al. On-chip generation of high-order single-photon W-states. Nat Photonics 2014; 8: 791-795.  
14 Sansoni L, Sciarino F, Vallone G, Mataloni P, Crespi A et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys Rev Lett 2012; 108: 010502.  
15 Heilmann R, Grafe M, Nolte S, Szameit A. Arbitrary photonic wave plate operations on chip: Realizing Hadamard, Pauli-X, and rotation gates for polarisation qubits. Sci Rep 2014; 4: 4118.  
16 Corrielli G, Crespi A, Geremia R, Ramponi R, Sansoni L et al. Rotated waveplates in integrated waveguide optics. Nat Commun 2014; 5: 4249.  
17 Meany T, Delanty M, Gross S, Marshall GD, Steel MJ et al. Non-classical interference in integrated 3D multiports. Opt Express 2012; 20: 26895-26905.  
18 Spagnolo N, Vitelli C, Aparo L, Mataloni P, Sciarrino F et al. Three-photon bosonic coalescence in an integrated tritter. Nat Commun 2013;4: 1606.  
19 Paulios K, Keil R, Fry D, Meinecke JDA, Matthews JC et al. Quantum walks of correlated photon pairs in two-dimensional waveguide arrays. Phys Rev Lett 2014; 112: 143604.  
20 Arriola A, Gross S, Jovanovic N, Charles N, Tuthill PG et al. Low bend loss waveguides enable compact, efficient 3D photonic chips. Opt Express 2013; 21: 2978-2986.  
21 Meany T, Gross S, Jovanovic N, Arriola A, Steel MJ et al. Towards low-loss lightwave circuits for non-classical optics at 800 and  $1550\mathrm{nm}$ . Appl Phys A 2014; 114: 113-118.  
22 Della Valle G, Osellame R, Chiodo N, Taccheo S, Cerullo G et al. C-band waveguide amplifier produced by femtosecond laser writing. Opt Express 2005; 13: 5976-5982.  
23 Osellame R, Della Valle G, Chiodo N, Taccheo S, Laporta P et al. Lasing in femtosecond laser written optical waveguides. Appl Phys A 2008; 93: 17-26.  
24 Chen WJ, Eaton SM, Zhang H, Herman PR. Broadband directional couplers fabricated in bulk glass with high repetition rate femtosecond laser pulses. Opt Express 2008; 16: 11470-11480.  
25 Eaton SM, Chen WJ, Zhang H, Iyer R, Li J et al. Spectral loss characterization of femtosecond laser written waveguides in glass with application to demultiplexing of 1300 and 1550 nm wavelengths. J Lightwave Technol 2009; 27: 1079-1085.

26 Liao Y, Xu J, Cheng Y, Zhou Z, He F et al. Electro-optic integration of embedded electrodes and waveguides in  $\mathrm{LiNbO_3}$  using a femtosecond laser. Opt Lett 2008; 33: 2281-2283.  
27 Horn W, Kroesen S, Herrmann J, Imbrock J, Denz C. Electro-optical tunable waveguide Bragg gratings in lithium niobate induced by femtosecond laser writing. Opt Express 2012; 20: 26922-26928.  
28 Matthews JCF, Politi A, Stefanov A, O'Brien JL. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nat Photonics 2009; 3: 346-350.  
29 Shadbolt PJ, Verde MR, Peruzzo A, Politi A, Laing A et al. Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit. Nat Photonics 2012; 6: 45-49.  
30 Metcalf BJ, Spring JB, Humphreys PC, Thomas-Peter N, Barbieri M et al. Quantum teleportation on a photonic chip. Nat Photonics 2014; 8: 770-774.  
31 Bonneau D, Lobino M, Jiang P, Natarajan CM, Tanner MG et al. Fast path and polarization manipulation of telecom wavelength single photons in lithium niobate waveguide devices. Phys Rev Lett 2012; 108: 053601.  
32 Humphreys PC, Metcalf BJ, Spring JB, Moore M, Salter PS et al. Strain-optic active control for quantum integrated photonics. Opt Express 2014; 22: 21719-21726.  
33 Zhang P, Aungskunsi R, Martin-Lopez E, Wabnig J, Lobino M et al. Reference-frame-independent quantum-key-distribution server with a telecom tether for an on-chip client. Phys Rev Lett 2014; 112: 130501.  
34 Osellame R, Chiodo N, Della Valle G, Taccheo S, Ramponi R et al. Optical waveguide writing with a diode-pumped femtosecond oscillator. Opt Lett 2004; 29: 1900-1902.  
35 Hong CK, Ou ZY, Mandel L. Measurement of subpicosecond time intervals between two photons by interference. Phys Rev Lett 1987; 59: 2044-2046.  
36 Bruno N, Martin A, Thew RT. Generation of tunable wavelength coherent states and heralded single photons for quantum optics applications. Opt Commun 2014; 327: 17-21.  
37 Afek I, Ambar O, Silberberg Y. Classical bound for Mach-Zehnder superresolution. Phys Rev Lett 2010; 104: 123602.  
38 Peruzzo A, Laing A, Politi A, Rudolph T, O'Brien JL. Multimode quantum interference of photons in multiport integrated devices. Nat Commun 2011; 2: 224.  
39 Laing A, O'Brien JL. Super-stable tomography of any linear optical device. 2012; arXiv:1208.2868.  
40 Chaboyer Z, Meany T, Helt LG, Withford MJ, Steel MJ. Tunable quantum interference in a 3D integrated circuit. Sci Rep 2015; 5:9601.

This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 Unported License. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/

Supplementary information for this article can be found on the Light: Science & Applications' website (http://www.nature.com/Isa/).