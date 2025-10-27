# OPEN

# High-speed programmable photonic circuits in a cryogenically compatible, visible-near-infrared 200 mm CMOS architecture

Mark Dong $^{1,2}$ , Genevieve Clark $^{1,2}$ , Andrew J. Leenheer $^{3}$ , Matthew Zimmermann $^{1}$ , Daniel Dominguez $^{3}$ , Adrian J. Menssen $^{2}$ , David Heim $^{1}$ , Gerald Gilbert $^{2,4}$ , Dirk Englund $^{2,5}$  and Matt Eichenfield $^{3}$

Recent advances in photonic integrated circuits have enabled a new generation of programmable Mach-Zehnder meshes (MZMs) realized by using cascaded Mach-Zehnder interferometers capable of universal linear-optical transformations on  $N$  input/output optical modes. MZMs serve critical functions in photonic quantum information processing, quantum-enhanced sensor networks, machine learning and other applications. However, MZM implementations reported to date rely on thermo-optic phase shifters, which limit applications due to slow response times and high power consumption. Here we introduce a large-scale MZM platform made in a 200 mm complementary metal-oxide-semiconductor foundry, which uses aluminium nitride piezo-optomechanical actuators coupled to silicon nitride waveguides, enabling low-loss propagation with phase modulation at greater than 100 MHz in the visible-near-infrared wavelengths. Moreover, the vanishingly low hold-power consumption of the piezo-actuators enables these photonic integrated circuits to operate at cryogenic temperatures, paving the way for a fully integrated device architecture for a range of quantum applications.

For many applications proposed for programmable optical systems $^{1-3}$ , the key requirements are (1) large scale; (2) fast response: sub-microsecond for applications in machine learning $^{4-7}$  and quantum control $^{8-11}$ ; and (3) power efficiency to enable operation in the cryogenic environment for integration with superconducting detectors $^{12,13}$  and artificial atoms $^{14-16}$ . Leading Mach-Zehnder mesh (MZM) platforms $^{17}$  consist of cascaded Mach-Zehnder interferometers (MZIs) to perform the general special unitary  $\mathrm{SU}(N)$  group requiring  $N(N - 1)/2$  MZIs (ref.  ${}^{18}$ ), as illustrated in Fig. 1a for a four-mode programmable  $\mathrm{SU}(4)$  in a rectangular mesh arrangement $^{19}$ . To meet the scalability requirement, for even a modest mode count  $N$ , the most demanding technical challenge is reliable manufacturing and a clear path to electronics co-integration. Although presently only modern complementary metal-oxide-semiconductor (CMOS)-compatible VLSI processes offer these capabilities through foundry services, material choices are practically limited to Si (refs.  ${}^{20,21}$ ) and silicon nitride (SiN) technologies $^{22}$ . For the high-bandwidth requirement within these materials, silicon-free carrier modulation $^{23}$  is problematic for MZMs because of the inherently coupled phase and amplitude. Silicon electric-field-induced  $\chi^{(2)}$  (ref.  ${}^{24}$ ) modulators are promising, but they have not been realized at scale and have a restricted operating wavelength power. A recently introduced alternative relies on piezo-optomechanical actuation of SiN waveguides $^{25-28}$ , which in the case of another study $^{25}$  has enabled narrow-band operation up to  $250\mathrm{MHz}$  with SiN waveguides for visible-near-infrared (NIR) operation and high optical power handling. Finally, the energy requirement is incompatible with any thermal modulation schemes, which dissipate an average of  $>800\mathrm{mW}$  for doped  $\mathrm{SiO}_2$  (ref.  ${}^{21}$ ),  $>20\mathrm{mW}$  per modulator for SOI (ref.  ${}^{29}$ ) and  $>40\mathrm{mW}$  per

modulator for SiN (ref. 17). Electrostatic MEMS devices meet the power requirement (promising sub-picowatt hold power)[30,31], but modulation timescales have thus far been limited to the microsecond regime.

Figure 1b summarizes this power-modulation bandwidth trade space for SiN and Si platforms compatible with the scalability requirement mentioned earlier. For a cross-platform comparison, Fig. 1b plots the power dissipated for  $\pi$ -phase shifts as a function of the circuit reconfiguration rate. In the thermal regime, the power dissipated is constant up to the maximum reconfiguration bandwidth, whereas piezo-actuation contains a trade-off between faster programming speeds and power dissipated on chip. The piezo-optomechanical approach offers up to three orders of magnitude improvement in programming time with lower power consumption as that of thermal approach and three to five orders of magnitude improvement in power dissipation at the maximum thermal reconfigurability rate, showing the exceptional suitability of this technology for MZM systems. Motivated by these considerations, we advance our wafer-scale process for SiN photonic integrated circuits (PICs) (Fig. 1c) with phase-only piezo-optomechanical tuners, whose basic design and operation are shown in Fig. 1d,e, through the co-design and development of photonics, electromechanics, electrical and mechanical control systems, and driver software. We combine the best attributes of the different devices discussed in our previous work[25] into a proof-of-principle MZM architecture capable of achieving 20 ns reconfiguration time, on-chip power dissipation per modulator below  $200\mu \mathrm{W}$  when switching on average for every  $1\mu \mathrm{s}$  and  $6\mathrm{nW}$  hold power, operation at  $700 - 780\mathrm{nm}$  with optical transmission up to  $1,550\mathrm{nm}$ , and improved power efficiency at  $5\mathrm{K}$ .

![](images/b1f80612ef5537419e9ce3a9b2e82bbc738545dc275ce76afd27b45f0059d812.jpg)

![](images/e31bf1364cc941a66c7ad922a7dfb1bafa7d30cffc700170208b25594c876850.jpg)  
Fig. 1 | High-speed, visible-wavelength and cryogenic-compatible PICs. a, Schematic of a four-mode programmable circuit consisting of cascaded MZIs for SU(4) operations. b, Trade space diagram of the power-reconfiguration rate for other CMOS-compatible photonic technologies and our piezo-actuated photonics. c, Microscopy images of a fully processed  $200\mathrm{mm}$  wafer with insets showing the zoomed-in view of a reticle and a  $4\times 4$  MZM. d, Three-dimensional concept art of an MZI with piezo-optomechanical phase shifters. e, Cross-sectional diagram of our phase shifter, illustrating how an applied voltage across the piezo results in strain imparted to the optical waveguide.

![](images/72b4706f1ed4097763dc630decf0e859f15cc94fefd9ca2d987e7f6bef8d4dd8.jpg)

![](images/4e0d2a935d5cd224c4b20d0423fb2f393a318dea74ef5ba176c903c4ff360411.jpg)

![](images/520b6bb6205f5161b14153f27d6f1d9550f7d6227436b9a684e1ab1356fba25e.jpg)

# Results

Device fabrication, design and theory of operation. Our devices are designed and fabricated on a  $200\mathrm{mm}$  wafer following an improved process flow based on our previous work[25]. The optical layer consists of a 300-nm-thick SiN layer in a silicon dioxide cladding, located on top of aluminium nitride (AlN) piezoelectric actuators with functionality for selective release and metal routing; Supplementary Section 1 provides additional fabrication details. This process enables high-speed and broadband active modulators. Specifically, Fig. 2a shows a full MZI with strain-actuated phase shifters both internal and external to the directional couplers, as indicated by the unfolded layout in Fig. 1d. Each arm of the internal phase shifter contains an optical-path-length-matched piezo-actuated segment (imparting a phase  $\Theta_{1,2}$ ) and same for the external phase shifter (imparting a phase  $\Phi_{1,2}$ ). Each phase shifter consists of a 400-nm-width SiN waveguide passing through an adiabatic taper, expanding to a width of  $5\mu \mathrm{m}$  for improved strain transfer[25], propagating for a distance of  $1.1\mathrm{mm}$ , and then through a second adiabatic taper back down to a 400-nm-wide single-mode turn. This loop repeats nine times, as shown in Fig. 2b, for a total path length of  $\sim 1\mathrm{cm}$  per phase shifter. The cross section shown in Fig. 2c,d reveals a slightly undercut  $10 - \mu \mathrm{m}$ -wide pillar around the oxide-clad  $5 - \mu \mathrm{m}$ -wide SiN waveguide and AlN actuators. Applying a potential difference across AlN transfers strain to the waveguide (a finite element simulation is shown in Fig. 2e), imparting a shift in the refractive index predominantly due to the strain-optic effect[32] in addition to moving boundary effects[33].

When applying a potential difference, the strain imparts phase change  $\Delta \theta$  to the optical mode for a given length  $L$  of the phase shifter as follows:

$$
\Delta \theta = (2 \pi / \lambda) (\Delta n _ {\mathrm {e f f}} L + n _ {\mathrm {e f f}} \Delta L), \tag {1}
$$

where  $\lambda$  is the free-space wavelength,  $n_{\mathrm{eff}}$  is the static effective mode index,  $\Delta L$  is the strain-induced path-length change in the phase shifter and  $\Delta n_{\mathrm{eff}}$  is the total effective strain-induced change in the refractive index:

$$
\Delta n _ {\text {e f f}} = \Delta n _ {\text {e f f}, \varepsilon} + \Delta n _ {\text {e f f , w g}}, \tag {2}
$$

$$
\Delta n _ {\text {e f f}, \varepsilon} = - p _ {1 1} \left(n _ {\text {e f f}} ^ {3} / 2\right) \varepsilon_ {x x}, \tag {3}
$$

which includes contributions from strain-optic  $(\Delta n_{\mathrm{eff},\varepsilon})$  effects and moving boundary  $(\Delta n_{\mathrm{eff,wg}})$  that contributes to waveguide modal dispersion. Here  $p_{11}$  is the diagonal component of the strain-optic coefficient for SiN, and  $\varepsilon_{xx}$  is the tensile strain component in the horizontal  $(x)$  direction parallel to the substrate surface (Fig. 2e). We estimate the strain values transferred to the SiN from a finite element model using approximate values of AlN piezoelectric coupling coefficients[25], layer-stack geometries and material properties, indicating that the dominant strain is tensile in the horizontal  $(x)$  direction and of magnitude  $\varepsilon_{xx} \approx 1.5 \times 10^{-6}$  per volt applied. The change in effective index due to strain (as shown in equation (3))

![](images/edd2bdb7836daeddab2e2dff99c9541753f8b26ad30802105be641afd1b5c986.jpg)  
Fig. 2 | Design of piezo-actuated modulators. a, Microscopy photo of an MZI with labelled SiN waveguides, metal routing (M1), phase shifters and directional couplers. b, Model of a phase shifter with labelled optical input/output, waveguide taper and actuation regions with finite element simulations of the  $400\mathrm{nm}$  and  $5 - \mu \mathrm{m}$ -wide waveguide transverse-electric (TE) modes. c, Schematic of the cross section of a phase shifter with materials labelled as shown. d, Scanning electron microscopy image of the cross section of the fabricated device, where the waveguides (purple), AlN (blue) and metal routing (white) are labelled. e, Finite element simulation of the first mechanical eigenfrequency at  $253\mathrm{MHz}$  with the plotted displacement exaggerated for visibility.

is a signed quantity depending on the direction of induced strain, meaning opposite strains produced by a negative applied voltage produce an opposite-shift effective index. This effect allows for a push-pull or differential operation<sup>34</sup> of the phase shifts  $\Theta_{1,2}, \Phi_{1,2} \in [-\pi/2, \pi/2]$  in Fig. 2a for an applied  $V_s \in [-V_\pi/2, V_\pi/2]$ , defined as the potential relative to ground with  $V_\pi$  being the required voltage for a  $\pi$  phase shift.

Room-temperature operation. Figure 3 summarizes the modulator performance at room temperature (300 K). Figure 3a,b shows the operation across a broadband range of wavelengths (700–780 nm). The plots shown here take advantage of the push-pull operation for optical loss balance (typical insertion loss of  $-3.5\mathrm{dB}$  at  $737\mathrm{nm}$ ; Supplementary Section 2 provides the loss characterization details) of the phase shifters by applying opposite-polarity voltages to each arm. We estimate  $V_{\pi}L$  from the sinusoidal fits, yielding values from  $50\mathrm{V}\cdot \mathrm{cm}$  ( $700\mathrm{nm}$ ) to  $65\mathrm{V}\cdot \mathrm{cm}$  ( $780\mathrm{nm}$ ) in the push-pull configuration or a corresponding  $V_{\pi}L$  in the range of  $100 - 130\mathrm{Vcm}$  per phase shifter. We attribute the variance in  $V_{\pi}L$  to material and waveguide dispersion. From Fig. 3a, we observe an inherent static phase shift in our MZIs. This shift does not highly depend on the wavelength and is a result of local stress and refractive-index differences seen by the two arms of the MZI due to fabrication. We note that the peak of the MZI's cross-port transmission (Fig. 3a) depends on the splitting ratios of our passive directional couplers and decreases as the wavelength increases, thus moving further away from the 50:50 point. An improved  $2\times 2\times 2$  MZI design[35,36] in conjunction with wavelength-tolerant directional couplers[37] would enable full tunability across the range of wavelengths tested.

Time-resolved measurements shown in Fig. 3c-e indicate short rise and fall times of  $\sim 5$  ns. Figure 3c plots the transmission when averaging over 16 square-wave voltage pulses applied through an arbitrary waveform generator (AWG), indicating a fall time of

5ns. As shown in Fig. 3d, the modulator follows a Gaussian pulse with a full-width at half-maximum of 15ns. We do not observe substantial hysteresis during active modulation, estimating a  $< 1\%$  deviation from single-shot traces limited by detector noise and stability of our measurement setup. Figure 3f plots the small-signal frequency-resolved modulator response, indicating a  $-3\mathrm{dB}$  cutoff at  $\nu_{\mathrm{3dB}} = 120\mathrm{MHz}$ . This cutoff is consistent with the RC time constant during measurement, consisting of the device capacitance of  $17\mathrm{pF}$  and series resistance of  $\sim 80\Omega$  arising from the voltage source and on-chip routing metal. We attribute the peak at  $241\mathrm{MHz}$  to the fundamental mechanical resonance, which is  $253\mathrm{MHz}$  as per our finite element model (Fig. 2e). The shape of the peak exhibits a characteristic resonance and anti-resonance feature typical of mechanical resonators[38,39]. We note that the AWG used for these tests does not produce the full  $20\mathrm{V}$  swing across its entire bandwidth  $(500\mathrm{MHz})$ , which accounts for the distorted Gaussian envelope and atypical falling edge shown in Fig. 3d,e, respectively. The contrast in these measurements is low, as this device is optimized for cryogenic operation, as described later.

Cryogenic operation at  $5\mathrm{K}$ . We performed the cryogenic characterization in a  $4\mathrm{K}$  closed-cycle cryostat (Montana Instruments). Using a fibre array and radio-frequency probe mounted on nanopositioners inside the cryostat (Supplementary Section 5), we applied various voltage waveforms. The transmission curves in Fig. 4 show no degradation in the switching operation, with an overall similar performance at a base temperature of  $5\mathrm{K}$  (Fig. 4a,b) compared with room temperature. Figure 4c indicates an extinction of approximately  $30\mathrm{dB}$ . We remark that compared with Fig. 3a, the static phase offset shown in Fig. 4c shifts due to differences in thermal contraction and stress-optic effects in the two MZI arms at cryogenic temperatures. Figure 4d plots a time trace when holding  $V_{s} = 20\mathrm{V}$ , indicating very stable open-loop operation ( $<0.5\%$  drift)

![](images/008f5442016731f61eca4d5583b39421cdf68c02e5a6718aba16656afd8364b9.jpg)

![](images/569476f3ca9ab54953a1f11757173875aaf10ac5c9af5c7c3215b49dd3d29e03.jpg)

![](images/ca3375a99c04370bb99589be024c4cce9370c8ef33ffe6fc97d1ea8671af2502.jpg)

![](images/db1fa84659f57119088bcc88409db9c000c8b8102d30809317f50710daa18ff6.jpg)  
Fig. 3 | MZI modulator characterization at 300 K. a, Cross-port power transmission coefficient of several wavelengths versus differential driving voltage of the MZI. b, Extracted phase shifts from sinusoidal fits at the same wavelengths. c, Photodiode response at 737 nm with a 5 MHz, 20 V peak-to-peak (pk-pk) square wave applied. d, Photodiode output with 15 ns full-width at half-maximum, 20 V pk-pk Gaussian pulse applied. e, Zoomed-in view of the falling edge of 5 MHz square in c, showing a fall time of  $\sim 5$  ns. f, Normalized modulator response for a 3 V sinusoidal signal showing mechanical resonance at 241 MHz.

![](images/1167f9eaaa3a5d08f6b9da5025443dd9f42fe4a63f7b4fdf9e4b591e9b810c4d.jpg)

![](images/48f72151c37e6ada366aca63d983d7298c0f6b27401135094270c82ffc9e7f46.jpg)

![](images/1d75b3d4d8519ef8480a1cf92f4543ea9384545bcd65af086c73c3e06e5b8d3b.jpg)  
Fig. 4 | Cryogenic operation of the modulator at  $5\mathrm{K}$  at  $737\mathrm{nm}$  wavelength. a, A 16-sample averaged photodiode response for a  $5\mathrm{MHz}$ ,  $20\mathrm{V}$  pk-pk square-wave driving signal. b, Zoomed-in falling edge of the square wave, showing the same  $-5\mathrm{ns}$  fall time as that at room temperature. c, Direct current sweep of a single phase shifter in our modulator, showing the maximum extinction ratio of  $-30\mathrm{dB}$ . d, Stability of our modulator held at  $5\mathrm{K}$  and constant  $20\mathrm{V}$ , showing  $<0.5\%$  drift of the MZI set point over several minutes.

![](images/aa5a6d9f2c464f3f9389e68b530a0559764e04272b524813b3be92da45d0811e.jpg)

![](images/dac8353a98d77459ee0ff9b25cddde5ebbc0c082190c322b1257ea475aac894f.jpg)

![](images/4bd3c5dd09ff64f6611be98c2c3c47b6ae3a58b481b7f7db82cc692dbb0f7cb7.jpg)

on the timescale of minutes. The corresponding hold power of  $2\mathrm{nW}$  is nearly eight orders of magnitude smaller than the cooling power  $(90\mathrm{mW})$  of the Montana cryostat. This low power consumption is a critical benefit, as even state-of-the-art thermal SiN waveguide modulators (Fig. 1b) would easily overwhelm the cryostat's cooling power. We note that the actual extinction ratio of the modulator is larger than  $30\mathrm{dB}$ ; however, limited volume in the cryostat prevented the use of differential driving (as demonstrated at room temperature) and limited the phase change to approximately  $\pi /2$  rather than  $\pi$ .

$4 \times 4$  programmable interferometer. Having characterized the MZIs, we now consider a proof-of-principle SU(4) programmable unitary transformation, which consists of  $N(N - 1)/2 = 6$  MZIs. The MZM is fully programmable, where all the phase shifters are computer controlled (Supplementary Section 3).

Figure 5 summarizes the MZM characterization. After a basic voltage calibration, we run voltage sweeps across all the six MZIs, producing internal phase-shifter transmissions as shown in Fig. 5d. The optical input and output combinations (Fig. 5c) here for

each plotted MZI show maximum power differences on actuation; a full dataset of all the 12 phase shifters is shown in Supplementary Section 4. Figure 5d plots the transmission of output port 3 on actuating 'MZI3', which indicates an optical extinction ratio in excess of  $40\mathrm{dB}$ . The total loss through the MZM ranges from  $-14$  to  $-21\mathrm{dB}$  at  $737\mathrm{nm}$ , depending on the optical path taken, primarily due to waveguide bending losses in the phase shifters, which could be completely eliminated with an unfolded implementation or larger-radii waveguide bends. We confirm that our MZM maintains the  $100\mathrm{MHz}$  bandwidth as demonstrated in single MZI devices by applying a  $10\mathrm{V}$ ,  $100\mathrm{MHz}$  sinusoid to the internal phase shifter of MZI2 and monitor the optical outputs 5 and 6 with a laser coupled through optical input 3. We utilize a lock-in detection scheme on the output photodiodes to extract the signal at  $100\mathrm{MHz}$  (Fig. 5e,f) for both channels and a relative phase offset of  $0.59\pi$ ; the small deviation from  $\pi/2$  is likely due to the  $125\mathrm{MHz}$  bandwidth of the photodiode being close to the driving frequency.

Although the results shown in Fig. 5 demonstrate the program-mability of our MZM as a single packaged device, voltage-handling limitations of our on-chip vias (see Discussion below) currently

![](images/c90e5b5599bb0b1cbe966d93e386e61066f0aa1cbfbd5238936af8b1f35d67e1.jpg)  
a

![](images/1b0edd0924be107d64ffda98470f0c58ba042a45df23fe31fb1eb3dcc1a48ad5.jpg)  
b

![](images/3e66199d5306f2fec5a7c514d0ae4ec50b186b7663ee1171540a1ee36bb0fbc0.jpg)  
c

![](images/be6c3cd08d752105c26f6195b7d625475b5591059f9153bb41e0f836a288fb97.jpg)  
d

![](images/3d7c34cbb7e3215a3230c682854c4aeec5f7d3ef075ee4d68833ec3787884251.jpg)  
MZ12 (input 3)

![](images/9802c60f4e20fb4c2977c4e72b5d5fe1b94ff74cda25e37ee52f57253fab9ae1.jpg)  
MZI3 (input 3)

![](images/662f1c05b3ccc0c4f10bfaa17b5280aca7eba97f3418947ce7ac0c001f2b4733.jpg)  
Fig. 5 | Proof-of-principle MZM operation at 737 nm. a, Scanning electron microscopy image of the device. b, Photograph of the photonic chip, wire bonds, printed circuit board, and optical input/output for testing. c, Diagram of MZI list and labels for optical input/output; fibre channels 1 and 8 are not connected and channels 2 and 7 are straight-through waveguides for alignment and calibration. d, Actuation of numbered MZI while plotting optical outputs 3 and 4 or 5 and 6; optical inputs used are input 3 for MZIs 2, 3 and 5; input 4 for MZI6; and input 6 for MZI1 and MZI4. The plotted optical power is normalized to the input laser power after accounting for facet coupling losses. e, Measured signal amplitude from fibre outputs 5 and 6 of the  $4 \times 4$  MZM with a  $10\mathrm{V}$ ,  $100\mathrm{MHz}$  driving sinusoid on MZI2. f, Signal amplitude as a function of lock-in phase; integration time for the lock-in measurements is  $4\mathrm{ms}$ .

![](images/a9ba5801df065ce03199cf004cad7cdcaa5fe909b8573ba77602f59ae8f151e0.jpg)

![](images/96b98e42302c5cb1ab0b4d6d63305f3a7860b89e5d704f8258c49591a47873ce.jpg)  
MZ16 (input 4)

![](images/d51a113fbb7e69534068977f33819dbe8c494c32128a6f8cdc9ba619246bdf32.jpg)  
e  
f

![](images/64455e4af8e4d76c8b16c6ea42aafb16fb720f9ff1743af977b88ec694a07833.jpg)

prevent accessing the full scope of SU(4) operations and thus the use of certain calibration procedures $^{34,40,41}$  to discern  $4 \times 4$  matrices or unitary fidelities produced by the chip. However, with expected improvements in overall loss, loss balance between MZIs, and a full  $2\pi$ -phase actuation (enabled by a combination of better via design, fabrication processes, and control electronic systems), we will explore such measurements in future experiments.

# Discussion

We have demonstrated a four-mode programmable interferometer in a  $200\mathrm{mm}$  CMOS foundry. The MZM comprises cryogenically compatible, piezo-optomechanical phase shifters with  $>100\mathrm{MHz}$  bandwidth operating in the visible-NIR wavelengths, which should be immediately applicable to many hybrid photonic architectures<sup>16</sup>, quantum protocols<sup>8,42</sup> and machine-learning algorithms<sup>6</sup>.

Although the devices presented here show promise for universal linear-optic programmable photonics in new performance regimes and application spaces, there are still some non-idealities that will be improved in future work. First, the dominant source of loss in all devices presented is the bends induced by waveguide meanders and directional couplers, measured to be  $-2.7\mathrm{dB}$  of the

-3.5 dB MZI insertion loss (Supplementary Section 2). Waveguide propagation losses  $(-0.39\mathrm{dBcm}^{-1})$  and adiabatic taper losses of  $-0.022 \pm 0.038\mathrm{dB}$  per taper account for the remaining loss of  $-0.8\mathrm{dB}$ . We estimate that implementing less tightly folded versions of the same devices that have fewer bends and tapers would allow us to achieve MZI insertion losses substantially lower than  $-1\mathrm{dB}$ . Second, in these particular devices, small voids in AlN in the vicinity of electrical vias produced metal filamentation that degraded the device breakdown voltage and prevented the application of voltages above  $V_{\mathrm{s}} = 25\mathrm{V}$ . Although we found individual vias in the test structures on the same wafer that allowed  $V_{\mathrm{s}} > 90\mathrm{V}$ , the yield was insufficient for an MZI comprising 90 vias. After a systematic failure analysis and cross-sectional imaging, the process yield improved greatly so that full SU(N) devices appear likely with maximum  $V_{\mathrm{s}} > 90\mathrm{V}$  (Supplementary Section 6). Besides the electrical vias, we have not observed any causes of systematic failure (such as mechanical failure or fatigue) in our devices, likely attributed to the relatively low strain and stress values under operation.

In addition to device performance improvements, design variations and prospects for large-scale photonics remain to be explored. With our current technology and SU(2) device footprint

(approximately  $1.3\mathrm{mm} \times 0.6\mathrm{mm}$ ), we can conceivably fit  $>500$  components on a single die without any lithographic modifications (such as stitching between reticle fields), enough to make an SU(32) device. Simply lengthening the phase shifters would also allow them to operate at CMOS-level voltages at the cost of actuation bandwidth due to increased device capacitance (a 10-cm-length phase shifter would potentially have  $V_{\pi} \approx 5 - 10\mathrm{V}$  and  $\nu_{3\mathrm{dB}} \approx 12\mathrm{MHz}$ ). Alternatively, strain-concentrating structures or mechanical resonance effects would help shrink our current device size by reducing the required driving voltage. Moreover, high-scandium-concentration  $\mathrm{Sc}_{(1 - x)}\mathrm{Al}_x\mathrm{N}$  has shown a fivefold increase in piezoelectric responsivity[43], promising a further five times reduction in  $V_{\pi}$  or device length.

Finally, the layer stack of our PIC (Supplementary Table 1 and Fig. 2c), which places the optical layers on top, enables many extensions to the platform. The optical layer—on top of all the metal and piezoelectric layers—allows for alternative optical layers to expand the transparency window into the ultraviolet regime[44-46]. Moreover, heterogeneously integrated thin films for either photon generation[14,47,48] and detection[13] or nonlinear interactions[49-52] could be placed directly on top of the optical layer with photons coupling evanescently to the rest of the integrated photonics. The AlN-actuator-based photonic platform is also entirely post-CMOS compatible and therefore can be directly fabricated on fully formed CMOS integrated circuits[53] for direct biasing or control of hybrid systems[54-56]; thus, the architecture presented here can be scaled to both very large photonic circuit sizes and very small photonic circuit pitches without electrical control bottlenecks.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41566-021-00903-x.

Received: 26 May 2021; Accepted: 28 September 2021; Published online: 13 December 2021

# References

1. Bogaerts, W. et al. Programmable photonic circuits. Nature 586, 207-216 (2020).  
2. Harris, N. C. et al. Linear programmable nanophotonic processors. Optica 5, 1623-1631 (2018).  
3. Pérez, D., Gasulla, I., Mahapatra, P. D. & Capmany, J. Principles, fundamentals, and applications of programmable integrated photonics. Adv. Opt. Photon. 12, 709-786 (2020).  
4. Wetzstein, G. et al. Inference in artificial intelligence with deep optics and photonics. Nature 588, 39-47 (2020).  
5. Shen, Y., Harris, N. C., Skirlo, S., Englund, D. & Soljacic, M. Deep learning with coherent nanophotonic circuits. In 2017 IEEE Photonics Society Summer Topical Meeting Series (SUM) 189-190 (IEEE, 2017)https://doi.org/10.1109/ phosst.2017.8012714  
6. Hamerly, R., Bernstein, L., Sludds, A., Soljacic, M. & Englund, D. Large-scale optical neural networks based on photoelectric multiplication. Phys. Rev. X 9, 021032 (2019).  
7. Prabhu, M. et al. Accelerating recurrent Ising machines in photonic integrated circuits. Optica 7, 551-558 (2020).  
8. Levine, H. et al. Parallel implementation of high-fidelity multiqubit gates with neutral atoms. Phys. Rev. Lett. 123, 170503 (2019).  
9. Kielpinski, D., Monroe, C. & Wineland, D. J. Architecture for a large-scale ion-trap quantum computer. Nature 417, 709-711 (2002).  
10. Choi, H., Pant, M., Guha, S. & Englund, D. Percolation-based architecture for cluster state creation using photon-mediated entanglement between atomic memories. npj Quantum Inf. 5, 104 (2019).  
11. Mehta, K. K. et al. Integrated optical addressing of an ion qubit. Nat. Nanotechnol. 11, 1066-1070 (2016).  
12. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).

13. Steinhauer, S. et al. NbTiN thin films for superconducting photon detectors on photonic and two-dimensional materials. Appl. Phys. Lett. 116, 171101 (2020).  
14. Wan, N. H. et al. Large-scale integration of artificial atoms in hybrid photonic circuits. Nature 583, 226-231 (2020).  
15. Kim, J.-H., Aghaeimeibodi, S., Carolan, J., Englund, D. & Waks, E. Hybrid integration methods for on-chip quantum photonics. Optica 7, 291-308 (2020).  
16. Elshaari, A. W., Pernice, W., Srinivasan, K., Benson, O. & Zwiller, V. Hybrid integrated quantum photonic circuits. Nat. Photon. 14, 285-298 (2020).  
17. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
18. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
19. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Steven Kolthammer, W. & Walsmley, I. A. Optimal design for universal multiport interferometers. Optica 3, 1460-1465 (2016).  
20. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).  
21. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
22. Taballione, C. et al.  $8 \times 8$  reconfigurable quantum photonic processor based on silicon nitride waveguides. Opt. Express 27, 26842-26857 (2019).  
23. Baehr-Jones, T. et al. Ultralow drive voltage silicon traveling-wave modulator. Opt. Express 20, 12014-12020 (2012).  
24. Chakraborty, U. et al. Cryogenic operation of silicon photonic modulators based on the d.c. Kerr effect. Optica 7, 1385-1390 (2020).  
25. Stanfield, P. R., Leenheer, A. J., Michael, C. P., Sims, R. & Eichenfield, M. CMOS-compatible, piezo-optomechanically tunable photonics for visible wavelengths and cryogenic temperatures. Opt. Express 27, 28588-28605 (2019).  
26. Liu, J. et al. Monolithic piezoelectric control of soliton microcombs. Nature 583, 385-390 (2020).  
27. Tian, H. et al. Hybrid integrated photonics using bulk acoustic resonators. Nat. Commun. 11, 3073 (2020).  
28. Jin, W. et al. Piezoelectric tuning of a suspended silicon nitride ring resonator. In 2017 IEEE Photonics Conference (IPC) 117-118 (IEEE, 2017). https://doi.org/10.1109/ipcon.2017.8116029  
29. Harris, N. C. et al. Efficient, compact and low loss thermo-optic phase shifter in silicon. Opt. Express 22, 10487-10493 (2014).  
30. Errando-Herranz, C. et al. MEMS for photonic integrated circuits. IEEE J. Sel. Topics Quantum Electron. 26, 1-16 (2020).  
31. Gyger, S. et al. Reconfigurable photonics with on-chip single-photon detectors. Nat. Commun. 12, 1408 (2021).  
32. Huang, M. Stress effects on the performance of optical waveguides. Int. J. Solids Struct. 40, 1615-1632 (2003).  
33. Johnson, S. G. et al. Perturbation theory for Maxwell's equations with shifting material boundaries. Phys. Rev. E 65, 066611 (2002).  
34. Miller, D. A. B. Analyzing and generating multimode optical fields using self-configuring networks. Optica 7, 794-801 (2020).  
35. Wang, M., Ribero, A., Xing, Y. & Bogaerts, W. Tolerant, broadband tunable  $2 \times 2$  coupler circuit. Opt. Express 28, 5555-5566 (2020).  
36. Miller, D. A. B. Perfect optics with imperfect components. Optica 2, 747-750 (2015).  
37. Chen, G. F. R. et al. Broadband silicon-on-insulator directional couplers using a combination of straight and curved waveguide sections. Sci. Rep. 7, 7246 (2017).  
38. Neculoiu, D., Bunea, A.-C., Dinescu, A. M. & Farhat, L. A. Band pass filters based on GaN/Si lumped-element SAW resonators operating at frequencies above 5 GHz. IEEE Access 6, 47587-47599 (2018).  
39. Olsson, R. H. et al. A high electromechanical coupling coefficient SH0 Lamb wave lithium niobate micromechanical resonator and a method for fabrication. Sens. Actuator. A Phys. 209, 183-190 (2014).  
40. Rahimi-Keshari, S. et al. Direct characterization of linear-optical networks. Opt. Express 21, 13450-13458 (2013).  
41. Bandyopadhyay, S., Hamerly, R. & Englund, D. Hardware error correction for programmable photonics. Optica 8, 1247-1255 (2021).  
42. Atatoure, M., Englund, D., Vanivakas, N., Lee, S.-Y. & Wrachtrup, J. Material platforms for spin-based photonic quantum technologies. Nat. Rev. Mater. 3, 38-51 (2018).  
43. Teshigahara, A., Hashimoto, K.-Y. & Akiyama, M. Scandium aluminum nitride: highly piezoelectric thin film for RF SAW devices in multi GHz range. In 2012 IEEE International Ultrasonics Symposium 1-5 (IEEE, 2012). https://doi.org/10.1109/ultsym.2012.0481  
44. West, G. N. et al. Low-loss integrated photonics for the blue and ultraviolet regime. APL Photonics 4, 026101 (2019).  
45. Lu, T.-J. et al. Aluminum nitride integrated photonics platform for the ultraviolet to visible spectrum. Opt. Express 26, 11147-11160 (2018).

46. Fan, L., Sun, X., Xiong, C., Schuck, C. & Tang, H. X. Aluminum nitride piezo-acousto-photonic crystal nanocavity with high quality factors. Appl. Phys. Lett. 102, 153507 (2013).  
47. Ellis, D. J. P. et al. Independent indistinguishable quantum light sources on a reconfigurable photonic integrated circuit. Appl. Phys. Lett. 112, 211104 (2018).  
48. Papon, C. et al. Nanomechanical single-photon routing. Optica 6, 524-530 (2019).  
49. Zhu, D. et al. Integrated photonics on thin-film lithium niobate. Adv. Opt. Photon. 13, 242-352 (2021).  
50. Desiatov, B., Shams-Ansari, A., Zhang, M., Wang, C. & Loncar, M. Ultra-low-loss integrated visible photonics using thin-film lithium niobate. Optica 6, 380-384 (2019).  
51. Cai, L. et al. Acousto-optical modulation of thin film lithium niobate waveguide devices. Photon. Res. 7, 1003-1013 (2019).  
52. McKenna, T. P. et al. Cryogenic microwave-to-optical conversion using a triply resonant lithium-niobate-on-sapphire transducer. Optica 7, 1737-1745 (2020).  
53. Wojciechowski, K. E., Olsson, R. H., Tuck, M. R., Roherty-Osmun, E. & Hill, T. A. Single-chip precision oscillators based on multi-frequency, high-Q aluminum nitride MEMS resonators. In TRANSDUCERS 2009-2009 International Solid-State Sensors, Actuators and Microsystems Conference 2126-2130 (IEEE, 2009). https://doi.org/10.1109/sensor.2009.5285626

54. Patra, B. et al. Cryo-CMOS circuits and systems for quantum computing applications. IEEE J. Solid-State Circuits 53, 309-321 (2018).  
55. Kim, D. et al. A CMOS-integrated quantum sensor based on nitrogen-vacancy centres. Nat. Electron. 2, 284-289 (2019).  
56. Ibrahim, M. I., Foy, C., Englund, D. R. & Han, R. High-scalability CMOS quantum magnetometer with spin-state excitation and detection of diamond color centers. IEEE J. Solid-State Circuits 56, 1001-1014 (2021).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/7f6e48da8043e2653c14d513e4d3d6660a7d0cdcd78a8b559c1b863349f0c61c.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long

as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The MITRE Corporation 2021

# Methods

Hold-power consumption and reconfiguration energy calculations. We first calculate the device capacitance  $C$  and on-chip routing metal resistance  $R_{\mathrm{chip}}$  based on the measured RC roll-off in our frequency response curve, yielding  $C = 17 \mathrm{pF}$  and  $R_{\mathrm{chip}} = 30 \Omega$  in addition to a series voltage source resistance of  $50 \Omega$ . The device leakage resistance based on previous measurements[25] is estimated to be  $500 \mathrm{M} \Omega$  and  $200 \mathrm{G} \Omega$  at 300 and  $5 \mathrm{~K}$ , respectively. The hold power  $P = IV$ , where  $I$  and  $V$  are the leakage current and applied voltage across the device, respectively, is found for two phase shifters holding  $25 \mathrm{~V}$  to maintain a phase shift of  $\pi$ . The reconfiguration energy dissipated on chip is calculated using the formula  $E = (R_{\mathrm{chip}} / R_{\mathrm{tot}}) CV^2$ , where  $R_{\mathrm{tot}}$  is the total series resistance of the circuit including external resistors in the AWG and  $V_s = 50 \mathrm{~V}$ . This equation accounts for two phase shifters with a  $50 \mathrm{~V}$  swing and represents energy dissipated from on-chip resistances from vias and routing metal lines. To reduce on-chip energy dissipation for slower reconfiguration rates,  $R_{\mathrm{tot}}$  is adjusted such that the corner frequency  $1/(2\pi R_{\mathrm{tot}} C)$  matches the current reconfiguration frequency (which is done off chip at the voltage source). This minimizes the on-chip energy dissipation as well as maintaining the necessary reconfiguration rate. The total power dissipated (Fig. 1b) is simply the hold power plus the reconfiguration energy times the reconfiguration rate.

Device characterization. We characterize individual MZI modulators both at room temperature and cryogenic temperature with a  $250 - \mu \mathrm{m}$  -pitch optical fibre array that is coupled through gratings to the on-chip waveguides. We use a  $150 - \mu \mathrm{m}$  -pitch radio-frequency probe (in the ground-signal-ground-signal-ground configuration at room temperature and ground-signal-ground at cryogenic temperature) to apply high-frequency electrical signals.

Digital lock-in amplifier. A time trace of output channels 5 and 6 of the MZM is directly digitized by a high-speed oscilloscope. The time traces are digitally integrated (for  $4\mathrm{ms}$ ) with sinusoids of varying frequencies and phases, whose resulting amplitudes form the data for the plots in Fig. 5e.f. The two photodiodes used for both channels have bandwidths of 125 and  $600\mathrm{MHz}$ . Please see Supplementary Information for more detailed experimental methods.

# Data availability

The data that support the plots and findings within this paper are available from the corresponding authors upon reasonable request.

# Acknowledgements

Major funding for this work is provided by MITRE for the Quantum Moonshot Program. A.J.M. acknowledges support from the Feodor Lynen fellowship, Humboldt Foundation and the DARPA ONISQ program. D.E. acknowledges partial support from Brookhaven National Laboratory, which is supported by the US Department of Energy, Office of Basic Energy Sciences, under contract no. DE-SC0012704 and the NSF RAISE TAQS program. M.E. performed this work, in part, with funding from the Center for Integrated Nanotechnologies, an Office of Science User Facility operated for the US Department of Energy Office of Science. M.D. thanks H. Larocque and M. Heuck for the transmission data at  $1,550\mathrm{nm}$ . M.D. and M.Z. thank MITRE engineers, L. Chan and K. Dauphinais, for their support in designing the MZM experimental setup. M.D. also thanks M. Prabhu, S. Bandyopadhyay, R. Hamerly and C. Errando-Herranz for helpful technical discussions.

# Author contributions

M.D. designed the experimental setups and performed the experiments, with major assistance from G.C. for the cryogenic experiments and M.Z. for the MZM characterization. M.E. conceived the modulator and fabrication architecture and developed the fabrication process with A.J.L. M.E. and A.J.L. supervised the fabrication with assistance from D.D. M.E. and M.D. designed the basic modulators and M.D. laid out the design mask with assistance from G.C., A.J.L. and M.E. on the development of design and process rules. A.J.M. and D.H. assisted in photonic device characterization and design analysis. M.D., D.E. and M.E. conceived the experiment. G.G., D.E. and M.E. supervised the project. The Quantum Moonshot Program is supervised by G.G. All the authors contributed to writing the paper.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41566-021-00903-x.

Correspondence and requests for materials should be addressed to Mark Dong, Gerald Gilbert, Dirk Englund or Matt Eichenfield.

Peer review information Nature Photonics thanks Wim Bogaerts, José Capmany and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.