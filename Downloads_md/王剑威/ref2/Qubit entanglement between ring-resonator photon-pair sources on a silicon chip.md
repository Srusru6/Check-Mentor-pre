ARTICLE

Received 30 Mar 2015 | Accepted 27 Jun 2015 | Published 6 Aug 2015

DOI: 10.1038/ncomms8948

OPEN

# Qubit entanglement between ring-resonator photon-pair sources on a silicon chip

J.W. Silverstone $^{1,\star}$ , R. Santagati $^{1,\star}$ , D. Bonneau $^{1}$ , M.J. Strain $^{2}$ , M. Sorel $^{3}$ , J.L. O'Brien $^{1}$  & M.G. Thompson $^{1}$

Entanglement—one of the most delicate phenomena in nature—is an essential resource for quantum information applications. Scalable photonic quantum devices must generate and control qubit entanglement on-chip, where quantum information is naturally encoded in photon path. Here we report a silicon photonic chip that uses resonant-enhanced photon-pair sources, spectral demultiplexers and reconfigurable optics to generate a path-entangled two-qubit state and analyse its entanglement. We show that ring-resonator-based spontaneous four-wave mixing photon-pair sources can be made highly indistinguishable and that their spectral correlations are small. We use on-chip frequency demultiplexers and reconfigurable optics to perform both quantum state tomography and the strict Bell-CHSH test, both of which confirm a high level of on-chip entanglement. This work demonstrates the integration of high-performance components that will be essential for building quantum devices and systems to harness photonic entanglement on the large scale.

<sup>1</sup>Centre for Quantum Photonics, H. H. Wills Physics Laboratory and Department of Electrical and Electronic Engineering, University of Bristol, Merchant Venturers Building, Woodland Road, Bristol BS8 1UB, UK. <sup>2</sup>Institute of Photonics, Department of Physics, University of Strathclyde, Wolfson Centre, 106 Rottenrow East, Glasgow G4 ONW, UK. <sup>3</sup>School of Engineering, University of Glasgow, James Watt South Building, Glasgow G12 8QQ, UK. * These authors contributed equally to this work. Correspondence and requests for materials should be addressed to M.G.T. (email: mark.thompson@bristol.ac.uk).

Quantum entanglement is at the heart of quantum information science: entanglement between photons and the vacuum gives security to quantum communications channels; entanglement between photons passing through a sample enables its super-resolution measurement; and entanglement between qubits provides the tremendous power behind quantum computation $^{1,2}$ . Qubit entanglement is regularly generated in bulk- or fibre-based quantum optical systems by directly using the intrinsic polarization correlations of the photon-pair source $^{3,4}$ , and on-chip using post-selected logic gates $^{5,6}$ . On-chip sources of photon pairs have been recently developed $^{7-10}$ , but rely on nonlinear processes in which all fields—pump, signal and idler—are co-polarized, both due to the increased strength of such processes and due to the difficulty of controlling polarization with integrated optics (with some exceptions $^{11-13}$ ). Since source-based entanglement typically lies in the photonic polarization degree of freedom, on-chip sources of path-qubit entanglement have been scarce.

We present a silicon-on-insulator photonic chip operating in the central telecommunications band, which can generate and analyse the path entanglement produced by two coherently pumped photon-pair sources. As shown in Fig. 1, a pulsed pump laser is launched into two microring photon-pair sources that produce pairs in a superposition between being created in one source or the other. The device reconfigures this superposition, using on-chip demultiplexers and a waveguide crossing, into an entanglement between two photonic path qubits. Finally, these path qubits are analysed using two on-chip Mach-Zehnder interferometers (MZIs). Embedded thermo-optic modulators facilitate electro-optic control and reconfiguration of the device. The pump laser, pump-suppressing filters and detectors are all fibre integrated, off the chip. In this work, we integrate narrowband photon sources, spectral demultiplexers and reconfigurable optics into a single device. We describe and quantify the performance of each of these functionalities, culminating with a precise estimation of the on-chip path-entangled state and a strict test of its entanglement.

# Results

Resonant photon-pair generation. Spontaneous four-wave mixing (SFWM) $^{9,10}$  is an effect of the third-order nonlinear susceptibility  $\chi^{(3)}$  of the medium—the silicon waveguide core. We use SFWM to produce photon pairs on-chip. By convention, the two constituents of each pair are referred to as 'signal' and 'idler' photons, with frequencies  $\nu_{\mathrm{s}}$  and  $\nu_{\mathrm{i}}$ , equally spaced on either side

of the pump frequency  $\nu_{\mathrm{p}}$ ; we will refer to the higher-energy photon as the signal (that is,  $\nu_{\mathrm{s}} > \nu_{\mathrm{p}} > \nu_{\mathrm{i}}$ ). SFWM acts to annihilate two photons from the (degenerate) pump and create the signal and idler at new frequencies via the phenomenological Hamiltonian  $\hat{H} \propto a_{\mathrm{i}}^{\dagger}a_{\mathrm{p}}^{2}a_{\mathrm{s}}^{\dagger} + a_{\mathrm{i}}a_{\mathrm{p}}^{\dagger 2}a_{\mathrm{s}}$ . Each SFWM event conserves the energy and momentum of the input photons. In our experiment, SFWM occurs in the optical cavities formed by two microring resonators, which modify the density of states of the parametric fluorescence, and structure the spectrum of these photon pairs into bright fluorescent peaks around the cavity resonances[14,15]. This structure differs from the characteristic flat, broad spectrum of straight-waveguide-based sources, which is shaped by momentum conservation alone.

We pumped on resonance with the cavity at  $\nu_{\mathrm{p}}$  and collected signal and idler photons from adjacent cavity resonances, one free spectral range over, at  $\nu_{\mathrm{s,i}} = \nu_{\mathrm{p}} \pm 800\mathrm{GHz}$ . The cavity linewidth was  $21\mathrm{GHz}$ . Source resonances cause the highlighted dips in the transmission spectrum of Fig. 2a; the peaks in that spectrum are due to the signal-idler demultiplexers, discussed later. Our pump laser produced 10.8-ps pulses, with a  $40\mathrm{GHz}$  linewidth, at a rate of  $51\mathrm{MHz}$ . Since SFWM takes in two pump photons, its efficiency scales quadratically with pump power for low squeezing values. However, due to the strong two-photon absorption of silicon in the near-infrared, this quadratic scaling only holds at low power, before two-photon absorption starts to dominate[16]. In our measurements, an average pump power of  $150\mu \mathrm{W}$  (253 mW peak) was delivered, leading to generation probabilities of 0.06 and 0.09 pairs per pulse for the two sources. System losses reduced these at-source generation rates to around 30 measured coincidences per second, with a coincidence-to-accidental ratio of around 10. Hereafter, all results are derived from net coincidence data, with accidental coincidences subtracted. An imbalance in efficiency between the top and bottom sources was somewhat compensated by the measured  $54\%$  reflectivity of the first coupler, leading to a source balance of  $\beta = 43\%$ .

Quantum interference. Interference between photons from different sources requires those photons to be indistinguishable in all degrees of freedom, but spectral indistinguishability poses a particular challenge. We refer to this spectral indistinguishability as the overlap,  $\sigma$ , which runs from  $\sigma = 0$  for fully distinguishable photon pairs to  $\sigma = 1$  for indistinguishable ones. We explored the overlap between the two microring sources by configuring the device to interfere the signal-idler superposition on the 'idler' interferometer of Fig. 1, which was configured as a beam

![](images/d4639216b75b707651b6721fa95ee757bdf7187900b37fe41b830c4d420d823a.jpg)  
Figure 1 | Schematic layout of the device. A picosecond pump pulse is coupled into the silicon chip where it generates a superposition of photon pairs via spontaneous four-wave mixing. This superposition is separated into signal (blue) and idler (red) path qubits, which are analysed by two MZIs. Thermo-optic phase shifters are shown in yellow. Photons at the output are separated from residual pump by fibre wavelength-division multiplexers (not shown) and collected by single-photon detectors.

![](images/b0ba29172a66b118184e6b855b708adbae6950468d171da3b5c6e1606061e77a.jpg)

![](images/0373b9bce5bf2753f16d28d0176f98fb29bd0d919f3140d90fb9a4ff9bf7aa3f.jpg)

![](images/493f013c6975d3af89d9abb42c0a307971dba6adc3df4abcf41f8d323fa948a0.jpg)  
Figure 2 | Spectral characteristics of the experiment. (a) Spectral layout of source (dips) and demultiplexer (peaks) resonances in the central telecommunications band. Source-free spectral range is  $800\mathrm{GHz}$ , to match the 200-GHz International Telecommunication Union (ITU) grid. (b) Two-photon fringe visibility measured as a function of top-to-bottom source detuning, as the top resonances were scanned over the stationary bottom resonances. Left inset: diagram describing top (t)-source resonance sweeping across fixed bottom (b)-source resonance. Right inset: representative two-photon fringe corresponding to peak visibility value (circled). Residual detuned visibility is due to the interference between resonant and non-resonant pairs. Error bars represent three standard errors of each sinusoidal regression. Shaded region on fit represents one s.d. in visibility. Measured joint spectral density profiles for the top (c) and bottom (d) microring sources. (e) Calculated joint spectral density, based on measured linear resonator parameters.

splitter. We then swept one source resonance over the other (see Methods). In this way, we could observe two-photon fringes analogous to those in ref. 7, and measure changes in the quality of the quantum interference as the two sources were tuned.

The fringe visibility as a function of source detuning is plotted in Fig. 2b. Accounting for source imbalance, and multi-pair

events, we compute the maximum visibility as  $96.0\%$  (when  $\sigma = 1$ ; see Supplementary Methods for details). When the sources were tuned, we observed a near-maximum peak visibility of  $95.8 \pm 2.1\%$ , corresponding to an overlap of  $\sigma = 0.99 \pm 0.04$  (Supplementary Figs 3 and 4). When the two sources were detuned completely, the visibility reached a floor of  $37\%$ . This is

residual interference between broadband photon pairs produced in the non-resonant parts of the interferometer, and the single remaining resonant source. Its visibility indicates that the spectral brightness of the bus waveguide was  $1\%$  of that of the tuned microring. Since all subsequent measurements were performed through the on-chip demultiplexers, this waveguide-generated flux did not greatly affect our statistics. These data show that the two microring sources could be made indistinguishable, and exhibited brightness that dominated the background SFWM occurring in the rest of the interferometer.

The interference peak (Fig. 2b) has a Gaussian shape, indicating an inhomogeneous broadening of the SFWM emission. Its width indicates a photon linewidth of  $28.6\mathrm{GHz}$ , somewhat broader than the cold cavity linewidth  $(21.0\mathrm{GHz})$ . Intra-cavity nonlinear effects<sup>17-19</sup> could cause this broadening.

Joint spectra. High-purity photon-pair sources—for heralded- or multi-photon experiments—require that, given the frequency of the signal photon, we gain minimal information about the frequency of the idler photon and vice versa—their frequency states are separable. By pumping the source cavities with spectrally broad pulses, we relax the energy and momentum requirements of the SFWM process. The emitted signal and idler photons then naturally and independently take on the structure of the cavity enhancement, which has been predicted to improve their spectral separability[20]. To quantify this separability, we measured the signal-idler joint spectral density (JSD) using the stimulated emission tomography method of ref. 21.

Measured JSD profiles are shown in Fig. 2c,d, for the top and bottom microring sources showing an overlap of  $\sigma = 0.962$ . They exhibit a residual spectral entanglement (and corresponding multi-mode squeezing) with the number of modes quantified by the Schmidt number  $K$ , where  $1 / K$  would be the visibility of a triggered Hong-Ou-Mandel interference dip. We measured  $K > 1.19$  for the top source and  $K > 1.17$  for the bottom source, where  $K = 1$  represents perfect two-mode squeezing and spectral separability. These values represent lower bounds on  $K$  because our measurements only give information on the magnitude of the joint spectral amplitude, not the phase. The SFWM inside each source resonator can be understood from its bright-light transmission spectrum. This model also takes in the pump lineshape, and the waveguide dispersion and gives as output the theoretical JSD of Fig. 2e (model details are provided in Supplementary Methods). The result of this model is convolved with a Gaussian on the signal arm, to reflect the limited resolution of our spectrometer (see Methods). The measured linewidth is somewhat broader than our model's prediction, but it matches the broadening we observed in the interference measurement. In straight-waveguide source designs, spectral separability is only achievable by inserting a narrow spectral filter after the pair-generation process[7,11,22], which necessarily reduces the source brightness. For bright heralded photon-pair sources, a naturally uncorrelated joint spectrum—like those we have shown—is desirable.

Demultiplexing and state preparation. Each pair is produced in a superposition of being generated in the top and bottom microring sources simultaneously, since we pump with only enough power to produce one photon pair and there is a fixed phase relationship between the two microrings. This pair superposition is then converted into an entanglement between two qubits, each composed of a single signal or idler photon in one or another of two waveguide paths. The signal and idler photons are separated by on-chip demultiplexers, formed by double-bus microring resonators[23]. They exhibited a selectivity of  $22\mathrm{dB}$ , a bandwidth of  $35\mathrm{GHz}$ , a free spectral range of  $640\mathrm{GHz}$  and a loss

that was negligible compared with the system loss. They were designed to select the signal photon, while maximally rejecting the idler (see peaks in Fig. 2b). Finally, the frequency-demultiplexed waveguides are rearranged to group the signal and idler paths together. Written in the form of a density matrix and in terms of the experimental parameters  $\beta$ ,  $\sigma$  and  $\Theta$ , the resulting qubit-basis state is

$$
\begin{array}{l} \hat {\rho} _ {\mathrm {t h}} = | 0 0 \rangle \langle 0 0 | \cdot \beta + \\ \left| 1 1 \right\rangle \langle 1 1 | \cdot (1 - \beta) + \\ | 0 0 \rangle \langle 1 1 | \cdot e ^ {- i \Theta} \sqrt {\beta} \sqrt {1 - \beta} \cdot \sigma + \tag {1} \\ \left| 1 1 \right\rangle \langle 0 0 | \cdot e ^ {+ i \Theta} \sqrt {\beta} \sqrt {1 - \beta} \cdot \sigma^ {*} \\ \end{array}
$$

where the balance  $\beta$  describes the relative brightness of the two sources, the overlap  $\sigma$  quantifies their spectral indistinguishability and  $\Theta$  accumulates the intrinsic total phase between the two qubits. We define a photon in the top (bottom) waveguide of each qubit to be a logical  $|0\rangle$  ( $|1\rangle$ ), and the first (second) qubit of each pair to be the signal (idler). For example,  $|00\rangle \langle 00|\beta$  describes both qubits having a photon in the top mode with probability  $\beta$ . Experimentally, we can control the balance  $\beta$  by adjusting the tuning of the filters (at the expense of spectral overlap); we control the overlap  $\sigma$  by tuning the two microring sources. If the flux from the two sources is balanced ( $\beta = 1/2$ ) and the source joint spectra overlap perfectly ( $\sigma = 1$ ) then  $\hat{\rho}_{\mathrm{th}}$  is in the family of maximally entangled Bell states. If  $\beta \in \{0,1\}$  then  $\hat{\rho}_{\mathrm{th}}$  is separable; if  $\sigma = 0$  then  $\hat{\rho}_{\mathrm{th}}$  is mixed. A detailed state evolution and a short discussion on the origin of entanglement in this device can be found in the Supplementary Discussion.

On-chip entanglement analysis. The on-chip state was manipulated and measured using integrated single-qubit analysis MZIs. These interferometers, shown in Fig. 1, implemented  $\hat{R}_z$  and  $\hat{R}_y$  rotations by angles  $\theta_{\mathrm{SZ}}$ ,  $\theta_{\mathrm{IZ}}$ ,  $\theta_{\mathrm{SY}}$  and  $\theta_{\mathrm{IY}}$  on the signal (S) and idler (I) qubits, respectively. These rotations facilitated single-qubit measurements on the generated two-qubit state. Photons from the two qubits were counted using coincidences between two  $25\%$  -efficient avalanche photodiodes, gated on each laser pulse.

A well-known test of quantum non-locality, as well as an indicator of the entanglement present in a quantum state $^{24}$ , is based on the reformulation of Bell's original inequality due to Clauser, Horne, Shimony and Holt (CHSH) $^{25}$ . In this test, a parameter  $S$  is evaluated $^{26}$ , which indicates the presence of non-locality: if  $S > 2$ , the state is non-local; if  $S = 2\sqrt{2}$  the state is maximally entangled.

We can explicitly calculate the  $S$ , which results from  $\hat{\rho}_{\mathrm{th}}$  of equation (1), to quantify how the violation depends on the balance and source overlap (see Supplementary Methods):

$$
S = \sqrt {2} (1 + 2 \sigma \sqrt {\beta} \sqrt {1 - \beta}) \tag {2}
$$

which reaches the maximum violation of  $2\sqrt{2}$  when  $\sigma = 1$  and  $\beta = 1/2$ , and decreases as the overlap and balance deviate from these values. Equation (2) is plotted as a heat map in Fig. 3a showing the level of entanglement indicated by each of our measurements (i-iv).

One manifestation of the entanglement present in our on-chip state (equation (1)) is the presence of the non-local phase factor  $\Theta$ . As a result of this factor,  $\dot{R}_z$  rotations applied to each qubit cannot be observed independently: each equally contributes to the total phase of the state  $\Theta$ . To demonstrate this, we configured the signal and idler  $\dot{R}_y$  rotations to mix the two modes of each qubit ( $\theta_{\mathrm{SY}} = \theta_{\mathrm{IY}} = \pi /2$ ), then manipulated both  $\theta_{\mathrm{SZ}}$  and  $\theta_{\mathrm{IZ}}$  and observed coincidence fringes with an entangled phase

![](images/27df49fc62028d651c3e46b2f75c1cb9896db8b47b24aa71309d2a38a2576a26.jpg)

![](images/2d7e45024278b9478375894f3d3e42ffa0531c309b70999d9dee943a0358ec62.jpg)  
Figure 3 | Summary of measurements in the context of Bell-CHSH inequality violation. (a) Map showing violation  $S$  as a function of source balance  $\beta$  and overlap  $\sigma$ , with listing of measurement results overlaid. When  $S > 2$ , the measurement correlations are consistent with a non-local, entangled state. By measuring: (i) the brightness of each source, we can estimate the balance  $\beta$ ; (ii) the quantum state via quantum state tomography, we can estimate both the balance  $\beta$  and the overlap  $\sigma$ ; (iii) correlated fringes, we obtain a value for the violation  $S(\beta, \sigma)$ ; and (iv) the overlap between measured joint spectra gives  $\sigma$ . The measurement of  $\sigma$  in (iv) naturally excludes multi-photon contamination, while the other measurements (i-iii) necessarily include it and result in lower values of  $\sigma$  as a consequence. (b) Fringes generated by  $\hat{R}_z$  rotations on signal and idler qubits allowing a direct measurement of CHSH  $S$  parameter (denoted measurement (iii) in part a).

$\Theta = \theta_{\mathrm{SZ}} + \theta_{\mathrm{IZ}}$  shown in Fig. 3b. These fringes have a mean visibility of  $94.7 \pm 1.0\%$  that is consistent with a strong CHSH violation of  $S = 2.686 \pm 0.026$ . This value of  $S$  violates the inequality by  $83\%$  and by 26 s.d.

Quantum state tomography. For any quantum system the total accessible information of its quantum state is encoded in its density matrix  $\hat{\rho}_{\mathrm{ex}}$ . Quantum state tomography[27] is the process of experimentally estimating  $\hat{\rho}_{\mathrm{ex}}$  based on a series of measurements. We made an over-complete set[28] of 36 measurements on the state using the on-chip interferometers, and used the results to estimate  $\hat{\rho}_{\mathrm{ex}}$ . See the Methods and Supplementary Methods for details. We produced a series of on-chip states—those that were separable, mixed and entangled—by using different configurations of source and filter tuning. Manipulating both the source balance  $(\beta)$  and frequency overlap  $(\sigma)$ , we observed changes in the resulting state in agreement with the predictions of equation (1).

To compare a measured state  $\hat{\rho}_{\mathrm{ex}}$  with an expected state  $\hat{\rho}_{\mathrm{th}}$ , we use the fidelity  $F$  evaluated as

$$
F = \operatorname {T r} \left(\sqrt {\sqrt {\hat {\rho} _ {\mathrm {t h}}} \cdot \hat {\rho} _ {\mathrm {e x}} \cdot \sqrt {\hat {\rho} _ {\mathrm {t h}}}}\right) ^ {2}, \tag {3}
$$

where the matrix square root is defined as  $\sqrt{\hat{\rho}}\cdot \sqrt{\hat{\rho}} = \hat{\rho}$ . The fidelity runs from 0 to 1:  $F = 1$  if the states are identical, while  $F = 0$  if they are orthogonal. We used  $F$  to gauge the ability of our device to prepare particular states, comparing each measured state with the prediction of equation (1). The results for each measurement are listed in Fig. 4, beside each measured state.

In the first measurement we tuned only the top source and filter and detuned the bottom filter, effectively setting  $\beta = 1$ . We estimated the state shown in Fig. 4a, which exhibits a peak in the pure  $|00\rangle$  component, as expected (a similar result was obtained with the top filter detuned, with  $92 \pm 1\%$  fidelity, see Supplementary Fig. 1). Next, we tuned both filters to match each source, but did not tune the two sources to overlap, effectively setting  $\beta = 1/2$  and  $\sigma = 0$ . We observed amplitude in both the  $|00\rangle$  and  $|11\rangle$  components, but without coherence terms ( $|00\rangle\langle11|$  and  $|11\rangle\langle00|$ ), as shown in Fig. 4b. As predicted by equation (1) this is due to a lack of spectral overlap between photons produced in the top and bottom sources, and the resulting lack of interference at the analysis interferometers. Indeed, the estimated state is mixed with a purity of  $0.49 \pm 0.01$  (with 0.5 expected). Owing to the lack of coherence, we were able to use the filter lineshapes to balance the source brightness, achieving  $\beta = 0.49$ . Finally, we tuned all four microrings to overlap and measured the highly entangled state of Fig. 4c, in which both sources are producing mutually coherent photons.

We evaluated the Bell-CHSH  $S$  parameter for the above entangled state (Fig. 4c) and found  $S = 2.692 \pm 0.018$ . This value violates the inequality by  $83\%$  and by 38 s.d., and is in excellent agreement with our estimation based on correlated fringes (Fig. 3b).

# Discussion

We have demonstrated bright and spectrally separable photon-pair sources, phase-stable frequency-selective elements and passive and active optics integrated on a silicon chip, and used

![](images/3dbf4e0b564fa85bb2046512764098f2bbae4e5038d201d878f9517371f98cf0.jpg)

![](images/3230d67164f3e866ef8e27f467de631d8920710732d843adbeaac563e4a906e0.jpg)

![](images/a4cfe40c52482fa39447ab67772c934629730e18c89003a7416fd4c0639ba349.jpg)  
Figure 4 | On-chip states for various device configurations, estimated using integrated analysis interferometers. Measured states are enlarged at left, with target states and corresponding fidelity (as defined in text) at right. State corresponding to (a) top source only (with bottom source detuned), (b) both sources tuned but not overlapped, showing mixed state, and (c) both sources tuned and overlapped, showing path-qubit entanglement.

them together to generate and analyse path-qubit entanglement at optical frequencies compatible with existing telecommunications networks. We used stimulated emission tomography $^{21}$  to provide evidence that the silicon microring source can produce spectrally uncorrelated photons—making this structure a promising candidate for future multi-pair experiments on silicon chips. Moreover, we were able to overlap two such microrings to a high degree, obtaining high-visibility quantum interference between them, despite their well-documented nonlinear dynamics $^{17,29}$ . We showed how the on-chip state strongly violates the Bell-CHSH inequality—a strict test of entanglement—and confirmed this experimentally in several different ways, including by on-chip quantum state tomography. That such a high degree of entanglement is generated and preserved by this device indicates the high performance of its constituent parts.

We used slow thermo-optic modulators to tune and configure the device. In our experiments, the required seconds of detector integration per reconfiguration meant this slowness posed no problem, however. Focussed efforts on thermo-optic modulation have achieved bandwidths up to  $1\mathrm{MHz}$  (refs 30,31). In any event, the thermo-optic coefficient decreases dramatically at low

temperatures $^{32}$ ; an entirely new approach will be required if superconducting detectors are also to be integrated $^{33,34}$ .

By assembling and characterizing a path-entangled Bell state on-chip, we have shown that silicon photonics, with its inherently mature and scalable manufacturing process, can prepare and manipulate delicate quantum entanglement. The narrow-band photon-pair sources and spectral demultiplexers, demonstrated here, will be useful tools for engineering future photonic quantum devices and systems.

# Methods

Apparatus. Pump pulses were generated by a passively mode-locked fibre laser (PriTel), with a 10.8-ps duration and a 51-MHz repetition rate. These pulses were cleaned by a silica arrayed-waveguide grating with 200-GHz channel spacing,  $\sim 120\mathrm{-GHz}$  channel width and an extinction  $>100$  dB (Opneti). Pump light was coupled onto, and signal and idler photons were coupled off of the chip via piezo-aligned lensed fibres with a  $2.5\text{-}\mu \mathrm{m}$  spot size  $(e^{-2}$ , OZ Optics). Remaining pump was removed from signal and idler channels by two more arrayed-waveguide gratings. Signal and idler photons were detected by two InGaAs geiger-mode avalanche photodiodes with  $25\%$  nominal detection efficiency, gated to each pump pulse (ID Quantique ID210). Photon coincidences were integrated for between 10 and 30 s per measurement.

The device's eight thermo-optic phase shifters were controlled by a bank of amplified 12-bit digital-to-analog converters, controlled by computer, delivering up to  $30\mathrm{mW}$  to each phase shifter. The overall temperature of the device was actively controlled using a Peltier module. Device footprint was reduced by the use of a common ground line. Electrical cross-talk due to this shared ground was mitigated using off-chip feedback.

Device fabrication. The device was fabricated on a silicon-on-insulator wafer with a  $220\mathrm{-nm}$  silicon slab and a  $2 - \mu \mathrm{m}$  buried oxide layer. The waveguides were  $500\mathrm{nm}$  wide and were patterned using direct-write electron beam lithography into a hydrogen silsesquioxane resist layer, used as a hard mask for the reactive ion etching of the silicon slab. These structures were subsequently coated with a  $900\mathrm{-nm}$  silica layer. Phase shifters were based on resistive heaters, patterned atop the silica layer using a lift-off technique on a  $50\mathrm{-nm}$  nickel-chromium film. Electrical traces connecting the heater elements were similarly patterned in a  $200\mathrm{-nm}$  gold layer. An optical micrograph of the fabricated device is shown in Supplementary Fig. 5.

All waveguide-waveguide couplers were fabricated as evanescent field (directional) couplers with  $300\mathrm{-nm}$  gaps. Losses were minimized at waveguide crossings via tapered sections, and fibre-to-chip coupling was achieved using inverse silicon tapers embedded in  $2\times 1.5\mathrm{-m}^2$  SU8 polymer waveguides.

Source overlap measurement. To obtain the data of Fig. 2b, we spectrally swept the top microring source resonance across the bottom one, while interfering the generated pairs on the bottom MZI (denoted  $\hat{R}_y(\theta_{\mathrm{IY}})$  in Fig. 1). To allow both signal and idler photons to reach the bottom MZI, we detuned both filter microrings, such that they were effectively removed from the light path, and both signal and idler photons were reflected downwards. To allow interference to occur on the bottom MZI, we configured it as a simple beam splitter by setting  $\theta_{\mathrm{IY}} = \pi /2$ . We then measured coincidences across the bottom two output ports of the device (labelled  $|0\rangle_i$  and  $|1\rangle_i$  in Fig. 1) while at the same time varying  $\theta_{\mathrm{IZ}}$  to form fringes. We fit these fringes sinusoidally to extract the visibility of each, and these visibility data are plotted in Fig. 2b.

Projector calibration. The rotations  $\hat{R}_y(\theta_{\mathrm{SY}})$ ,  $\hat{R}_y(\theta_{\mathrm{IY}})$ ,  $\hat{R}_z(\theta_{\mathrm{SZ}})$  and  $\hat{R}_z(\theta_{\mathrm{IZ}})$  were used to analyse the states generated on-chip. To do so, we calibrated the phase-voltage relationship of each phase shifter independently. We injected laser light into the device and recorded the output intensity  $I$  from each interferometer as a function of the phases, obtaining  $I(\theta_{\mathrm{SY}},\theta_{\mathrm{SZ}})$  and  $I(\theta_{\mathrm{IY}},\theta_{\mathrm{IZ}})$ . We fit the data with a model of the double interferometer (which included the first on-chip coupler), yielding the various coupler reflectivities and phase-voltage relationships. These data and models are plotted in Supplementary Fig. 2. Since we were unable to determine the absolute values of  $\theta_{\mathrm{SZ}}$  and  $\theta_{\mathrm{IZ}}$ , we defined these phases relatively. We used the resulting models to control the on-chip phase shifters as required by each part of the experiment.

Quantum state tomography. We used the on-chip rotations to implement an informationally over-complete $^{35}$  set of 36 projective measurements on two qubits, to reconstruct  $\hat{\rho}_{\mathrm{ex}}$ . Each measurement projected each of the two qubits onto one of the six states:  $|0\rangle$ ,  $|1\rangle$ ,  $|+ \rangle$ ,  $| - \rangle$ ,  $| + i \rangle$  or  $| - i \rangle$ . We then performed a multidimensional search for the two-qubit state  $\hat{\rho}_{\mathrm{th}}$ , which could best explain the measurement outcomes, based on a constrained least squares estimator. The

problem is defined as:

$$
\hat {\rho} _ {\mathrm {t h}} = \arg \min  _ {\hat {\rho}} \left\{\sum_ {i} \left| P _ {\mathrm {e x}} (i) - P _ {\hat {\rho}} (i) \right| ^ {2} \right\} \tag {4}
$$

where  $\hat{\rho}$  is the density matrix generated internally by the search algorithm, with the condition that it is physical: that is, hermitian, positive semi-definite and with trace one.  $P_{\mathrm{ex}}(i)$  is the  $i^{\mathrm{th}}$  experimental probability estimate and  $P_{\rho}(i)$  is the corresponding computed result based on the application of the  $i^{\mathrm{th}}$  projector to  $\hat{\rho}$ .

Experimental uncertainty per count was measured using residuals from a number of coincidence fringes. This was used to estimate the uncertainty on each  $P_{\mathrm{ex}}(i)$ . A Monte-Carlo method was then used to sample 500 reconstructions around the measured values  $P_{\mathrm{ex}}(i)$ , and the uncertainty in each tomographic parameter (fidelity,  $S$ , etc.) was estimated from the distribution of these reconstructions.

Joint spectral density measurement. In obtaining the data of Figs 2c and 2d, we followed closely the prescription of Liscidini et al.[21] and the method of Eckstein et al.[36]. We tuned each ring separately and pumped them as detailed in the main text. A narrow linewidth seed laser was swept across one resonance of each ring, and the stimulated four-wave mixing was collected by a spectrometer. The seed field was provided by an amplified tuneable laser with  $10\mathrm{kHz}$  linewidth (Photonetics Tunics Plus). We reduced the launched seed power until no evidence of seed-induced optical bi-stability remained. The stimulated four-wave mixing signal was collected by an optical spectrum analyser with a 6-GHz resolution (Anritsu MS9740A).

# References

1. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
2. Horodecki, R., Horodecki, M. & Horodecki, K. Quantum entanglement. Rev. Mod. Phys. 81, 865-942 (2009).  
3. Xing-Can Y. et al. Observation of eight-photon entanglement. Nat. Photonics 6, 225-228 (2012).  
4. Bell, B. A. et al. Experimental characterization of universal one-way quantum computing. New J. Phys. 15, 053030 (2013).  
5. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
6. Shadbolt, P. J. et al. Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit. Nat. Photonics 6, 45-49 (2012).  
7. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photonics 8, 104-108 (2014).  
8. Collins, M. J. et al. Integrated spatial multiplexing of heralded single photon sources. Nat. Commun. 4, 2582 (2013).  
9. Sharping, J. E. et al. Generation of correlated photons in nanoscale silicon waveguides. Opt. Express 14, 12388-12393 (2006).  
10. Lin, Q. & Agrawal, G. P. Silicon waveguides for creating quantum-correlated photon pairs. Opt. Lett. 31, 3140-3142 (2006).  
11. Matsuda, N. et al. A monolithically integrated polarization entangled photon pair source on a silicon chip. Sci. Rep. 2, 817 (2012).  
12. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nat. Commun. 2, 566 (2011).  
13. Olislager, L. et al. Silicon-on-insulator integrated source of polarization-entangled photons. Opt. Lett. 38, 1960-1962 (2013).  
14. Azzini, S. et al. Ultra-low power generation of twin photons in a compact silicon ring resonator. Opt. Express 20, 23100-23107 (2012).  
15. Wakabayashi, R. et al. Time-bin entangled photon pair generation from Si micro-ring resonator. Opt. Express 23, 1103-1113 (2015).  
16. Husko, C. A., Clark, A. S., Collins, M. J. & De Rossi, A. Multi-photon absorption limits to heralded single photon sources. Sci. Rep. 3, 3087 (2013).  
17. Pernice, W. H. P., Schuck, C., Li, M. & Tang, H. X. Carrier and thermal dynamics of silicon photonic resonators at cryogenic temperatures. Opt. Express 19, 3290-3296 (2011).  
18. Pernice, W. H. P., Li, M. & Tang, H. X. Time-domain measurement of optical transport in silicon micro-ring resonators. Opt. Express 18, 18438-18452 (2010).  
19. Priem, G. et al. Optical bistability and pulsating behaviour in Silicon-On-Insulator ring resonator structures. Opt. Express 13, 9623-9628 (2005).  
20. Helt, L. G., Sipe, J. E., Yang, Z. & Liscidini, M. Spontaneous four-wave mixing in microring resonators. Opt. Lett. 35, 3006-3008 (2010).  
21. Liscidini, M. & Sipe, J. E. Stimulated emission tomography. Phys. Rev. Lett. 111, 193602 (2013).  
22. Harada, K. et al. Indistinguishable photon pair generation using two independent silicon wire waveguides. New J. Phys. 13, 065005 (2011).

23. Rabus, D. G. Integrated Ring Resonators (Springer, 2007).  
24. Bartkiewicz, K., Horst, B., Lemr, K. & Miranowicz, A. Entanglement estimation from bell inequality violation. Phys. Rev. A 88, 052105 (2013).  
25. Clauser, J. F., Horne, M. A., Shimony, A. & Holt, R. A. Proposed experiment to test local hidden-variable theories. Phys. Rev. Lett. 23, 880-884 (1969).  
26. Aspect, A., Grangier, P. & Roger, G. Experimental realization of Einstein-Podolsky-Rosen-Bohm gedankenexperiment: a new violation of bell's inequalities. Phys. Rev. Lett. 49, 91-94 (1982).  
27. Leonhardt, U. Quantum-state tomography and discrete wigner function. Phys. Rev. Lett. 74, 4101-4105 (1995).  
28. James, D. F. V., Kwiat, P. G., Munro, W. J. & White, A. G. Measurement of qubits. Phys. Rev. A 64, 052312 (2001).  
29. Pelc, J. S. et al. Picosecond all-optical switching in hydrogenated amorphous silicon microring resonators. Opt. Express 22, 3797-3810 (2013).  
30. Atabaki, A. H., Shah Hosseini, E., Eftekhar, A. A., Yegnanarayanan, S. & Adibi, A. Optimization of metallic microheaters for high-speed reconfigurable silicon photonics. Opt. Express 18, 18312-18323 (2010).  
31. Watts, M. R. et al. Adiabatic thermo-optic Mach-Zehnder switch. Opt. Lett. 38, 733-735 (2013).  
32. Komma, J., Schwarz, C., Hofmann, G., Heinert, D. & Nawrodt, R. Thermo-optic coefficient of silicon at  $1550\%$  nm and cryogenic temperatures. Appl. Phys. Lett. 101, 041905 (2012).  
33. Pernice, W. H. P. et al. High-speed and high-efficiency travelling wave single-photon detectors embedded in nanophotonic circuits. Nat. Commun. 3, 1325 (2012).  
34. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).  
35. de Burgh, M. D., Langford, N. K., Doherty, A. C. & Gilchrist, A. Choice of measurement sets in qubit tomography. Phys. Rev. A 78, 052122 (2008).  
36. Eckstein, A. et al. High-resolution spectral characterization of two photon states via classical measurements. *Laser & Phot. Rev* 8, L76-L80 (2014).

# Acknowledgements

We thank John G. Rarity, Peter J. Shadbolt and Anthony Laing for valuable discussions, as well as Luka Milic for his help with the joint spectral density measurements. We also thank the staff of both the James Watt Nanofabrication Centre in Glasgow and the Centre for Nanoscience and Quantum Information in Bristol for their support. We acknowledge the support from the European Research Council through the BBOI project, and from the Department of the Army, US Army Research Office. M.G.T. acknowledges the support from an Engineering and Physical Sciences Research Council (EPSRC, UK) Early Career Fellowship. J.W.S. acknowledges an EPSRC Doctoral Training Account, and a Natural Sciences and Engineering Research Council (Canada) Alexander Graham Bell Canada Graduate Scholarship. J.L.O'B. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies.

# Author contributions

J.W.S. and R.S. contributed equally to this work; J.W.S., R.S., D.B., J.L.O'B. and M.G.T. conceived and designed the experiments; J.W.S. and R.S. analysed the data; M.J.S. and M.S. fabricated the device; J.W.S., R.S. and D.B. performed the experiments; J.W.S., R.S. and M.G.T. wrote the manuscript.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

How to cite this article: Silverstone, J. W. et al. Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat. Commun. 6:7948 doi: 10.1038/ ncomms8948 (2015).

![](images/4552cb4e1f7c50028781dec1fdf3fe03a52577d901647355c2a8ab175ec49c60.jpg)

This work is licensed under a Creative Commons Attribution 4.0 International License. The images or other third party material in this

article are included in the article's Creative Commons license, unless indicated otherwise in the credit line; if the material is not included under the Creative Commons license, users will need to obtain permission from the license holder to reproduce the material. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/