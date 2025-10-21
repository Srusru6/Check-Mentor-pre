![](images/82401a873e2e06286a68b02da45cf8095dea42d07108b1815d45ea115f32fc92.jpg)

SUBJECT AREAS:

QUANTUM OPTICS

NONLINEAR OPTICS

OPTICAL PHYSICS

QUANTUM PHYSICS

Received 24 September 2012

Accepted

17 October 2012

Published

12 November 2012

Correspondence and requests for materials should be addressed to

N.M. (m.nobuyuki@

lab.ntt.co.jp)

* Current address:

ESPCI ParisTech, 10

rueVauquelin,75005

Paris, France.

† Current address:

Graduate School of

Pure and Applied

Science, University of

Tsukuba, Tsukuba,

Ibaraki 305-8571,

Japan.

# A monolithically integrated polarization entangled photon pair source on a silicon chip

Nobuyuki Matsuda<sup>1,3</sup>, Hanna Le Jeannic<sup>1*</sup>, Hiroshi Fukuda<sup>2,3</sup>, Tai Tsuchizawa<sup>2,3</sup>, William John Munro<sup>1</sup>, Kaoru Shimizu<sup>1</sup>, Koji Yamada<sup>2,3</sup>, Yasuhiro Tokura<sup>1†</sup> & Hiroki Takesue<sup>1</sup>

$^{1}$ NTT Basic Research Laboratories, NTT Corporation, 3-1 Morinosato-Wakamiya, Atsugi, Kanagawa 243-0198, Japan,  $^{2}$ NTT Microsystem Integration Laboratories, NTT Corporation, 3-1 Morinosato-Wakamiya, Atsugi, Kanagawa 243-0198, Japan,  $^{3}$ Nanophotonics Center, NTT Corporation, 3-1 Morinosato-Wakamiya, Atsugi, Kanagawa 243-0198, Japan.

Integrated photonic circuits are one of the most promising platforms for large-scale photonic quantum information systems due to their small physical size and stable interferometers with near-perfect lateral-mode overlaps. Since many quantum information protocols are based on qubits defined by the polarization of photons, we must develop integrated building blocks to generate, manipulate, and measure the polarization-encoded quantum state on a chip. The generation unit is particularly important. Here we show the first integrated polarization-entangled photon pair source on a chip. We have implemented the source as a simple and stable silicon-on-insulator photonic circuit that generates an entangled state with  $91 \pm 2\%$  fidelity. The source is equipped with versatile interfaces for silica-on-silicon or other types of waveguide platforms that accommodate the polarization manipulation and projection devices as well as pump light sources. Therefore, we are ready for the full-scale implementation of photonic quantum information systems on a chip.

Photonic quantum states encoded in polarizations, paths, and times of arrival are excellent qubit candidates. Qubits are the quintessential resource for photonic quantum information processing (QIP), which provides a fundamentally new approach to communication $^{1}$ , metrology $^{2}$ , simulation $^{3-5}$ , and computation $^{6-8}$ . Of these quantum states the polarization-encoded state is a true two-level photonic system, which is easy to manipulate with bulk optics such as waveplates. It is at the heart of many photonic QIP protocols $^{1,4-9}$ .

Integrated quantum photonics, which exploits miniature physical size and stable interferometers with near-perfect lateral-mode overlaps of integrated lightwave circuits, constitutes the future for realizing a scalable photonic QIP system on a chip $^{10,11}$ . Recent experiments on integrated quantum photonics have utilized path-encoded quantum states of photons $^{3,10-13}$ . However, polarization encoding allows us to implement the systems without the need for path duplication, and thus provides the simplest and most compact circuitry. It will also allow us to implement a wealth of the QIP protocols. To accomplish such polarization-encoded QIP systems, it is essential to develop integrated subsystems to generate, manipulate, and measure polarization-encoded quantum states on a single chip. Although the integration of optical circuits makes the handling of polarization states slightly more challenging, Bonneau et al. $^{14}$  and Sansoni et al. $^{15,16}$  recently demonstrated the manipulation and projection of quantum states on a chip by using a lithium niobate (LN) waveguide modulator and low-birefringent silica waveguides, respectively. An integrated single-photon detector on a silicon chip has already been demonstrated $^{17}$ . Therefore the only remaining task is to implement a polarization-entangled photon pair source $^{18,19}$ . The source is an essential component of such polarization-encoded QIP systems as quantum gates $^{7}$ , on-demand single photon sources $^{20}$ , and scalable one-way quantum computation $^{8}$ . Furthermore, path-polarization hybrid integration is also useful as a simulation tool for physical quantum systems $^{4}$ .

Many polarization-entanglement sources have already been realized by means of integrated nonlinear waveguides, from which we can obtain quantum-correlated photon pairs via  $\chi^{(2)}$  or  $\chi^{(3)}$  spontaneous parametric processes $^{19,21-25}$ . Such waveguides generally exhibit a polarization-mode walk-off, which causes the generated polarization entanglement to degrade. To compensate for the longitudinal walk-off, some of the sources required off-chip quantum erasers, namely an additional birefringence crystal, a polarization-dependent delay line, or a polarization-maintained fibre $^{21-23}$ . The others utilized one polarization mode of the nonlinear waveguides to

![](images/3404ca2d30a5998ae4be00300b544c4919fb04148a7f9de30c1f437c53a3aedd.jpg)

![](images/b8d7b1b2947ca07f00d983f98ba035153fc6325d7866c795a8b990279de067b0.jpg)  
Figure 1 | A monolithically integrated polarization-entanglement source. (a) The source, fabricated on a silicon-on-insulator substrate, consists of a silicon-wire-based  $90^{\circ}$  polarization rotator sandwiched by two nonlinear silicon wire waveguides. The device generates the polarization entanglement as a superposition of the two events shown in (b). The figure is not to scale for clarity.

avoid the walk-off, by using additional fibre-optic circuits for polarization steering $^{24-26}$ . Therefore, there have been no fully integrated polarization entanglement sources that generate photon pairs entangled inside the chip; nevertheless the feature is necessary for a practical integrated QIP system. To achieve the future, Bragg-reflection-based AlGaAs waveguides were carefully designed for the monolithic polarization entanglement source with the walk off eliminated $^{27,28}$ . On the other hand, current optical communication technologies require sophisticated polarization diversity technologies $^{29,30}$ , which potentially solve the problem of integrating the polarization entanglement source.

In this work, we experimentally demonstrate the first polarization entanglement source that is fully integrated as a silicon photonic circuit. We compensate for the polarization-dependent walk-off simply by designing the device to be symmetric as regards the polarization degree with respect to the device midpoint, with the help of a polarization manipulation technology for telecommunication devices. The symmetric structure is also useful for the stable generation of maximally entangled states, in the presence of waveguide loss. Our source is not based on a post-selection scheme[22], so creates no spurious photons that limit the application of the source[21]. Furthermore, the device is equipped with a spot-size converter (SSC), which is an interface with silica or other types of quantum waveguide circuits for a fully integrated QIP system on a chip.

# Results

Device design and building blocks. Our source (Fig. 1a), which is based on a simple and single-path configuration, consists of two silicon-wire-waveguide photon pair sources $^{31,32}$  connected by an ultra-small silicon-wire polarization rotator $^{33}$ . Both silicon wire waveguides are  $400~\mathrm{nm}$  wide,  $200~\mathrm{nm}$  high and  $1.5~\mathrm{mm}$  long. The silicon polarization rotator has an off-axis double core structure. The inner core is a silicon photonic wire with a  $200\mathrm{-nm}$ -square cross section, which is embedded in a  $\mathrm{SiO_xN_y}$  outer core with an  $840\mathrm{-nm}$ -square cross section. The silicon wire waveguides and the silicon polarization rotator are connected by  $10 - \mu \mathrm{m}$ -long tapered silicon wires. The over- and under-cladding of the silicon wire waveguides and the silicon polarization rotator are made of  $\mathrm{SiO_2}$  (not shown). The device is equipped with SSCs with tapered silicon cores at their ends $^{34}$ . In this work, the SSCs provide efficient coupling between the silicon wire waveguides and external optics. As we discuss later in detail, the SSC can be an interface between our source and silica-on-silicon or other types of waveguide platforms $^{35}$  for the integrated polarization-encoded QIP system.

In a silicon wire waveguide, a correlated pair of signal and idler photons are created via  $\chi^{(3)}$  spontaneous four-wave mixing (FWM) following the annihilation of two pump photons[31,32]. The spontaneous FWM in the silicon wire waveguide is useful for the efficient creation of photon pairs, thanks to the high  $\chi^{(3)}$  nonlinearity of silicon in the telecom band (more than 100 times higher than that of silica) and the lateral confinement of light in a region less than a wavelength in size. The Raman photons created in the single-crystalline silicon core can be spectrally separated from the signal and the idler photons to reduce potential noise[31,32]. Moreover, the pump and the photon pair have similar frequencies in the spontaneous FWM process, so the longitudinal walk off between involved photons becomes much smaller than those in the  $\chi^{(2)}$  process[19]. Thanks to these features we can obtain highly pure photon pairs from a silicon wire waveguide with a length of few millimetres with a high efficiency.

In the silicon wire waveguide, TE-polarized photon pairs are efficiently generated by a TE-polarized pump field. Figure 2a shows spectra of the idler-to-signal conversion efficiency (extracted from the data shown in Supplementary Fig. S1 online) via the stimulated FWM for cases where the pump, signal, and idler fields are all TE-like (i.e., horizontally polarized) and TM-like (i.e., vertically polarized) (see Methods for details). The efficiency is proportional to the photon-pair production rate in spontaneous  $\mathrm{FWM}^{32}$ . The notably high FWM efficiency and its large bandwidth under the all-TE condition are originating from strong field confinement in the core (Supplementary Fig. S2 online) and the near-zero-dispersion property of the TE mode in the telecom band (Supplementary Fig. S3 online). Thus, we can regard our silicon wire waveguide as a photon pair source that operates only in the TE mode. In the present work, we utilize this polarization-dependent feature to build a polarization entanglement source.

The silicon polarization rotator was originally developed as a polarization-diversity integrated optical component for photonic networks $^{30}$ . The off-axis double core structure of the silicon polarization rotator exhibits two orthogonal eigenmodes, which have different effective refractive indices and eigen-axes tilted at  $45^{\circ}$  to the normal with respect to the silicon substrate (Fig. 2b). The birefringence in the eigenmodes provides an integrated waveplate, causing the polarization plane to rotate by an amount that depends on the length of the rotator. The insertion loss of the silicon polarization rotator was estimated to be approximately  $1\mathrm{dB}^{33}$ . We investigated the polarization rotation angle at the rotator  $\theta_{\mathrm{SPR}}$  (see Methods). Figure 2c shows the light transmission properties of the reference 3-mm silicon wire waveguide and the polarization entanglement source that includes a  $30 - \mu \mathrm{m}$ -long silicon polarization rotator as a function of an additional output polarizer angle. A  $\theta_{\mathrm{SPR}}$  value of 86.7  $\pm 0.1^{\circ}$  was obtained (from a fitting) with a fringe visibility  $V$  of 0.99  $\pm 0.01$ , while the reference silicon wire waveguide exhibited a small

![](images/55f0a825495e8fcb6fe7d6f39025020d6c123326a7dfde92e20c8761e80ed05f.jpg)

![](images/250cdcabe7d52d8725d90c40ca1662d00b26d60d04c05e26053399999a85787f.jpg)

![](images/7e97033930cd1c39d85d6e7f1f00c6cc99ad7d069077ce99a1895bd9c905dcfd.jpg)

![](images/5e1b7ecfb9d3a6c6c8dc58cf0d70162ff81ae2e6281e17a27d08e55d2968aee1.jpg)  
Figure 2 | Property of each building block of the polarization-entanglement source. (a) Polarization dependence of the FWM efficiency in a silicon wire waveguide investigated with a stimulated FWM experiment. The idler-to-signal conversion efficiency is plotted as a function of pump-to-signal detuning. The values are normalized with respect to the TE-FWM efficiency at zero detuning. (b) The two eigenmodes in the silicon polarization rotator (simulated with a mode solver) with effective refractive indices  $n_{\mathrm{eff}}$ . (c) Measured transmittance of the silicon polarization rotator (red) and the reference silicon wire waveguide (black) with TE-polarized incident light as a function of output polarizer angle. The solid curves represent sinusoidal fittings.

initial offset of  $-0.4 \pm 0.3^{\circ}$  with  $V = 0.98 \pm 0.01$ . Thus, a polarization rotation angle of almost  $90^{\circ}$  was obtained with the high polarization extinction ratio.

Operating principle of the device for the stable single-chip generation of polarization-entangled photons. We use a pump beam

with  $+45^{\circ}$  (D) linear polarization, which is a 1:1 combination of the TE and TM modes in the silicon wire waveguides (Fig. 1). In the first silicon wire waveguide (SWW1), the TE component of the pump creates a photon pair in the  $|\mathrm{TE,TE}\rangle_{\mathrm{s,i}}$  state, which the silicon polarization rotator rotates to the  $|\mathrm{TM,TM}\rangle_{\mathrm{s,i}}$  state as a result of a  $90^{\circ}$  polarization rotation. Here the subscripts denote the frequency modes of the signal and idler photons. At the same time, the silicon polarization rotator rotates the TM component of the pump field to provide it with TE polarization, and the second silicon wire waveguide (SWW2) creates other  $|\mathrm{TE,TE}\rangle_{\mathrm{s,i}}$  photons. Since we cannot distinguish whether the pair was generated in SWW1 or SWW2, we obtain the maximally polarization-entangled state:

$$
| \psi \rangle = (| \mathrm {T E}, \mathrm {T E} \rangle_ {\mathbf {s}, \mathbf {i}} + e ^ {- i \phi} | \mathrm {T M}, \mathrm {T M} \rangle_ {\mathbf {s}, \mathbf {i}}) / \sqrt {2}, \tag {1}
$$

at the output of the polarization-entanglement source. It should be noted that our scheme is post-selection-free and thereby creates no spurious photons. Here the relative phase difference  $\phi$  depends on the length difference  $\Delta L$  between SWW1 and SWW2. Strong birefringence in a silicon wire waveguide causes significant polarization-mode dispersion of photonic wave packets. In our silicon wire waveguide the estimated polarization-mode dispersion is  $5\mathrm{ps} / \mathrm{mm}$ , which is comparable to the typical width of a biphoton wave packet obtained from a silicon wire waveguide[31,32]. However, since the polarization-entanglement source is designed to be symmetric as regards the polarization states with respect to the midpoint of the device, the polarization-mode dispersion of the pump pulses and photon pairs are cancelled out if  $\Delta L = 0$ . The  $\Delta L$  fabrication error is less than  $1\mu \mathrm{m}$ , which corresponds to a negligible walk off of less than 10 fs. Therefore, our polarization-entanglement source requires no additional component outside the chip to compensate for the temporal distinguishability of the biphoton wave packets caused by polarization-mode dispersion as in the earlier polarization-entanglement sources[21-23].

Integrated waveguides generally exhibit linear propagation loss, which reduces number of pairs created in SWW1, can cause the imbalance between the two terms in the entangled state. However, our configuration automatically equalizes the two amplitudes and thus provides a maximally entangled state. This is because the reduction of the pairs created in SWW1 resulting from the waveguide loss in SWW2 is equivalent to the reduction of the pairs to be created in SWW2 owing to the loss of the TM component of the input pump pulses. We denote the light transmittance of each silicon wire waveguide for the TM mode and the transmittance of the silicon polarization rotator as  $\mu_{\mathrm{TM}}$  and  $\mu_{\mathrm{SPR}}$ , respectively. The photon pairs created in SWW1 by TE-polarized pump pulses suffer from extra loss in the silicon polarization rotator and SWW2 compared with the pairs created in SWW2. Hence, the output photon pair rate decreases by  $(\mu_{\mathrm{TM}}\mu_{\mathrm{SPR}})^2$ . On the other hand, the intensity of the TM-polarized component of the pump pulses decreases by  $\mu_{\mathrm{TM}}\mu_{\mathrm{SPR}}$  in the SWW1 and the silicon polarization rotator. Thus, the pair production rate decreases by  $(\mu_{\mathrm{TM}}\mu_{\mathrm{SPR}})^2$ , which corresponds to the total transmittance of the other pair. Therefore, the two terms in the  $|\psi\rangle$  state are automatically balanced. Note that this effect is not available with the  $\chi^{(2)}$ -based parametric process where the pair production rate is proportional to the pump power[18,19].

Observation of polarization-entangled photon pairs. We have created polarization-entangled photon pairs using optical pulses with a temporal width of 80 ps and a repetition rate of  $100\mathrm{MHz}$  in the experimental set-up shown in Fig. 3 (see Methods for details). The detected coincidence rate  $N_{\mathrm{cc}}$  and the coincidence over accidental ratio (CAR) of the photon pairs generated with the setup were  $103.9\mathrm{Hz}$  and 54.7, respectively, for the reference silicon wire waveguide with a projection basis of  $\left|\mathrm{TE},\mathrm{TE}\right\rangle_{\mathrm{s,i}}$  and a pump peak power  $P_{\mathrm{peak}}$  of  $69~\mathrm{mW}$ . Given the device length of  $3\mathrm{mm}$  and the overall photon detection efficiency of  $-15\mathrm{dB}$  (per channel), the pair

![](images/dbac217e053b014983a569e25d405438e2fb76cd13c7ffd1d7aa93be5b27a383.jpg)  
Figure 3 | Experimental set-up for measuring the polarization entanglement. IM, intensity modulator; EDFA, erbium-doped fibre amplifier; P, polarizer; H, half-wave plate; Q, quarter-wave plate; SSC, spot-size converter; APD, InGaAs avalanche photodiode; TIA, time-interval analyser. Dashed line shows free-space optical path. Blue lines show electrical connection. Note that all the wave plates are free space bulk optics embedded in collimation benches.

creation efficiency at the chip end was estimated to be 0.14 pairs/ pulse/GHz/W²/cm², which is comparable to the efficiency of 0.2 pairs/pulse/GHz/W²/cm² in conventional silicon wire waveguides fabricated without a SiOₙNₚ deposition process³². At the same time, our polarization-entanglement source emitted photon pairs with Ncc = 39.0 Hz and CAR = 57.9 with a |TE,TE\rangle s,i basis and Ncc = 40.2 Hz and CAR = 42.2 at |TM,TM\rangle s,i, at Ppeak of 128 mW. The slightly degraded CAR of the TM pairs compared with that of TE pairs is because the TM pairs (generated in SWW1) suffered additional loss in the silicon polarization rotator and SWW2.

We performed quantum state tomography on the generated photon pairs by carrying out a correlation measurement of 16 polarization combinations that were selected based on the angles of the four wave plates in the polarization projection units<sup>36</sup>. The reconstructed density matrix with the maximum-likelihood estimation for the reference silicon wire waveguide  $\rho_{\mathrm{ref}}$  and for the polarization-entanglement source  $\rho_{\mathrm{ent}}$  (with measurement times of 60 and  $120~\mathrm{s}$ ) are shown in Fig. 4a and b, respectively, as their real and imaginary parts, and absolute values of each element. Note that these results included statistical accidental coincidence counts.  $\rho_{\mathrm{ref}}$  shows that the reference waveguide generated  $|\mathrm{TE,TE}\rangle_{s,i}$  pairs as expected. For the state  $|\psi \rangle$  we obtain a density matrix written as

$$
\begin{array}{l} \rho = \sum | \psi \rangle \langle \psi | = \frac {1}{2} (| \mathrm {T E}, \mathrm {T E} \rangle \langle \mathrm {T E}, \mathrm {T E} | + e ^ {i \phi} | \mathrm {T E}, \mathrm {T E} \rangle \langle \mathrm {T M}, \mathrm {T M} |) \tag {2} \\ + e ^ {- i \phi} | \mathrm {T M}, \mathrm {T M} \rangle \langle \mathrm {T E}, \mathrm {T E} | + | \mathrm {T M}, \mathrm {T M} \rangle \langle \mathrm {T M}, \mathrm {T M} |) \\ \end{array}
$$

if the generated state is purely  $|\psi \rangle$ . The off-diagonal terms, which represent the state purity, vanish if the biphoton is in a mixed state. Therefore, the state amplitudes (absolute values) close to 0.5 at the off-diagonal corners of the obtained  $\rho_{\mathrm{ent}}$  represent the high state purity. We obtained a high purity value of  $0.93 \pm 0.02$ .

As regards the degree of entanglement, we estimate the fully entangled fraction  $F(\rho) = \max_{\Psi} \langle \Psi | \rho | \Psi \rangle$ , where the maximum is taken over all maximally entangled states  $|\Psi \rangle$ , i.e., over  $|\Psi \rangle = U_s \otimes U_i \left[ \frac{1}{\sqrt{2}} \left( |TE, TE\rangle_{S,i} + |TM, TM\rangle_{S,i} \right) \right]$ , where  $U_s$  and  $U_i$  are unitary transformations on the signal and idler modes<sup>37,38</sup>. Therefore, we can create any maximally entangled state (including Bell states) from a state  $\rho$  with  $F(\rho) = 1$  by employing linear optics such as wave plates. In accordance with the procedure described in ref [38], we obtained  $F(\rho_{\mathrm{ref}})$  as  $0.51 \pm 0.02$ , which is on the bound of the classical states of

![](images/8a2f67ffc6b12bddfab2ea90321071e3870873bca49240a596c653d1154bcce0.jpg)

![](images/96fce6aacc2a91eb58cb40cb016577de668de1cd3e3c06950cb5bca9320f5279.jpg)  
Figure 4 | The real and the imaginary parts of the reconstructed density matrices for the two-photon polarization states generated from (a) the reference silicon wire waveguide and (b) the polarization entanglement source. The absolute values of the elements are also displayed to show the amplitudes on off-diagonal elements. H and V represent the TE and TM bases, respectively.

$F(\rho) = 0.5$ . Thus, the single straight silicon wire waveguide created no entanglement. At the same time, for the polarization-entanglement source we obtained  $F(\rho_{\mathrm{ent}}) = 0.91 \pm 0.02$ . The  $F(\rho_{\mathrm{ent}})$  value is much greater than  $1 / \sqrt{2} \sim 0.71$ , implying that the generated state can violate the Clauser-Horne-Shimony-Holt inequality<sup>39</sup>. In addition, the concurrence (an alternate measure of entanglement) was obtained as  $0.88 \pm 0.02$ . Hence, we successfully generated photon pairs with a high degree of polarization entanglement from the chip.

# Discussion

The imperfection of  $F(\rho_{\mathrm{ent}})$  value is considered to be mainly due to the wavelength-dependent polarization rotation at the SSCs and at the silicon polarization rotator (see Supplementary for details). The unexpected polarization rotation at the SSCs might be due to a fabrication error (e.g., a slight geometric horizontal offset between the axes of the inverse-taper silicon wire and the second core at the SSCs). Regarding the silicon polarization rotator, in principle, the retardation dispersion is  $\varDelta\theta_{\mathrm{SPR}}/\varDelta\lambda=0.2^{\circ}/\mathrm{nm}^{33}$ , which is as small as usual bulk zero-order half wave plates<sup>40</sup>. This small dispersion is

because the silicon polarization rotator is also a zero-order rotator. Therefore, by solving practical fabrication issues (such as the semicircular shape of the  $\mathrm{SiO_xN_y}$  second core $^{33}$ ) we could provide a better silicon polarization rotator with almost perfect polarization rotation.

To summarize, we have demonstrated a monolithically integrated polarization entangled photon pair source. The device requires no additional off-chip components and thus is the first complete subsystem of an integrated polarization entanglement source. To achieve full-scale QIP system, a polarization entanglement source must be capable of integration with quantum circuits consisting of manipulation and projection devices for polarization-encoded states on the same chip. Furthermore, it is argued that the polarization entanglement source should also be equipped with an electrically driven pump laser integrated on the same chip for further system stability[41]. These criteria seem to be formidable at first glance; however, our source can be integrated with any of them. The silica SSC interface allows hybrid integration with silica-on-silicon waveguides[35], which already accommodates a polarization controller[42], a polarization beam splitter[16,43], and even a pump laser diode[44]. Although a rectangular-core silica waveguide generally exhibits a strain that makes the waveguide birefringent[16], such birefringence can be eliminated[43] or tuned with voltage-controlled heaters[45]; the birefringence compensation technology is useful for, e.g., selecting output entangled states on a chip by tuning the phase difference  $\phi$  in the state  $|\psi\rangle$ . Furthermore, the silica waveguides can be integrated with high-speed LN-based modulators[14] by means of silica-LN hybrid integration technology[46]. Of course our silicon-wire-based device can be directly connected with silicon-wire-based quantum circuits[13]. Integrated single-photon detectors on a silicon chip are also ready with a markedly high quantum efficiency[17]. Therefore, our monolithic polarization-entangled photon pair source helps pave the way to the full-scale implementation of photonic QIP system using the polarization degree of freedom.

# Methods

Device fabrication. Our device was fabricated on a silicon-on-insulator wafer with a  $200\mathrm{-nm}$ -thick silicon layer and a  $3 - \mu \mathrm{m}$ -thick buried  $\mathrm{SiO_2}$  layer. The silicon wire waveguides were  $400~\mathrm{nm}$  wide. The  $30 - \mu \mathrm{m}$ -long and  $200\mathrm{-nm}$ -wide silicon wire for the rotator was adiabatically connected by  $10 - \mu \mathrm{m}$ -long silicon tapers. For efficient coupling between the device and the external fibres, we equipped both ends of the device with SSCs. The silicon wire waveguides and SSCs were fabricated by electron beam lithography and electron cyclotron resonance plasma etching. An 840-nm-thick silicon oxynitride film with a refractive index of 1.60 was deposited by plasma-enhanced chemical vapour deposition and the second core of the silicon polarization rotator was formed by reactive ion etching with fluoride gas. The measured propagation losses of our device were 2.2 and  $1.7~\mathrm{dB / cm}$  for the TE and TM modes, respectively.

Details of stimulated FWM experiment. In the stimulated FWM experiment designed to show the discrepancy between the FWM efficiencies of the TE and TM polarizations, we used two independent wavelength-tuneable cw lasers as a pump and a signal source. The pump beam was modulated into a pulse train (500-ps full-width half maximum, 40-MHz repetition rate) with an LN intensity modulator. The pump and signal beams were combined by a 50/50 directional coupler, and then copolarized in either the TE or TM mode by the half-wave plate in the free-space focusing module, which coupled the light into a straight silicon waveguide with a length  $L$  of  $3\mathrm{mm}$  that was used as a reference. They were then corrected from the waveguide output with a lensed fibre, and the overall output spectrum was measured directly with an optical spectrum analyzer (OSA) with a spectral resolution of  $0.05\mathrm{nm}$ . The observed FWM spectrum is shown as a density plot in supplementary Fig. S1. Here the signal wavelength was scanned across the telecom band to change the pump-signal detuning, while the pump wavelength was fixed at  $1551.1\mathrm{nm}$ . The pump and the signal powers coupled to the waveguide were  $90\mathrm{mW}$  (peak) and  $3.0\mathrm{mW}$ , respectively. The data in Fig. 2a were extracted from the data in Fig. S1. Here the stimulated FWM efficiency, which is the ratio of the output idler power to the output signal power, is approximated as  $\eta = (\gamma P_{\mathrm{peak}}L)^2$  in the vicinity of zero pump-signal detuning; the nonlinear constant  $\gamma = (2\pi n_2) / (\lambda_{\mathrm{p}}A_{\mathrm{eff}})$ , where  $n_2$  is the nonlinear refractive index of the material,  $\lambda_{\mathrm{p}}$  is the pump wavelength.  $A_{\mathrm{eff}}$  is the polarization-dependent effective mode area, which mainly determines the discrepancy between the  $\eta$  values in the TE and TM modes. The calculated  $A_{\mathrm{eff}}$  ratio between the TE and TM modes is 0.2, corresponding to an  $\eta$  ratio of  $0.2^2 (-14\mathrm{dB})$ , which approximately explains the experimental value of  $-17\mathrm{dB}$ .

Evaluating the performance of the silicon polarization rotator. In Fig. 3, IM consists of an electro-absorption modulator and an LN intensity modulator, which modulated a continuous beam from the light source ( $\lambda_{\mathrm{p}} = 1551.1 \mathrm{~nm}$ ) into a train of pump pulses. The pulses were amplified by an erbium-doped fibre amplifier, filtered to eliminate the amplified spontaneous emission noise, and then launched into the polarization-entanglement source. The input polarization state was set by using a free-space focusing module that contained a collimation lens followed by a polarizer, a half-wave plate, and a high-NA focusing lens. Here the coupling efficiency with the chip was  $-2 \mathrm{~dB}$ .

To evaluate the polarization rotation angle of the silicon polarization rotator, we set the input half-wave plate angle at  $0^{\circ}$  so that the input state was in the TE mode. We also used a similar free-space focusing module but with an embedded polarizer to collect and analyse the SOP of the output field. Figure 2b is the measured transmittance as a function of the output polarizer angle.

Experimental details of the polarization entanglement generation. For the polarization-entanglement generation, we set the half-wave plate in the input focusing module at  $+22.5^{\circ}$  so that the pump pulses were D polarized. Then the output field from the device including entangled photons was collected by a lensed fibre with an outcoupling efficiency of  $-2$  dB. Then, the light was introduced into the WDM filter, which suppressed the residual pump field (with an isolation of more than 130 dB) and separated the signal and idler photons into different fibre channels. Each output port has a centre wavelength of  $1546.4\mathrm{nm}$  (s) and  $1556.0\mathrm{nm}$  (i) with a channel bandwidth of  $0.14\mathrm{nm}$  (18 GHz). Then, the photons passed through fibre birefringence compensators (a half wave plate sandwiched by two quarter wave plates) and subsequently polarization analysers, each of which consisted of a half and a quarter wave plate, and a polarizer. Finally, the photons were received by InGaAs single photon detectors (id210, id Quantique) that operated at a gate frequency of  $100\mathrm{MHz}$  synchronous with the pump's repetition rate. The quantum efficiency, gate width, the dark count rate, and the dead time of the detectors were  $20\%$ ,  $1\mathrm{ns}$ ,  $10^{-5}/$  gate, and  $5.0~\mu \mathrm{s}$ , respectively. The overall photon detection efficiency was  $-15$  dB per channel, which consisted of the collection efficiency of the created photons  $(-8\mathrm{dB})$  and the quantum efficiency of each detector  $(-7\mathrm{dB})$ . The detection signals from the two detectors were input into the time interval analyser (TIA) for coincidence measurements.

Each wave plate of the birefringence compensators was set so that the polarization basis at the device output corresponded to the basis of the polarization analyser. To accomplish this, we used an erbium-doped fibre amplifier emitting an amplified-spontaneous-emission source in the TE mode at the input. Then, we set the angles of the wave plates in the birefringence compensators so that the minimum and maximum transmittance through the polarization analysers were obtained with appropriate basis sets.

The errors in the  $F(\rho)$  values obtained with quantum state tomography were estimated using the angular setting uncertainties of the wave plates in the polarization projection units and the Poissonian noise statistics of the obtained coincidence counts. We increased the  $P_{\mathrm{peak}}$  value and the measurement time for the  $\rho_{\mathrm{ent}}$  measurement to obtain good statistics. The obtained total coincidence counts (the sum of the values on the diagonal bases) were  $6.6 \times 10^{3}$  and  $1.0 \times 10^{4}$  for the reference silicon wire waveguide and the entanglement source, respectively. The corresponding pair production rate was estimated to be  $1.1 \times 10^{-3}$  and  $0.8 \times 10^{-3}$  per pulse.

1. Gisin, N., Ribordy, G., Tittel, W. & Zbinden, H. Quantum cryptography. Rev. Mod. Phys. 74, 145-195 (2002).  
2. Giovannetti, V., Lloyd, S. & Maccone, L. Quantum-enhanced measurements: beating the standard quantum limit. Science 19, 1330-1336 (2004).  
3. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500 (2010).  
4. Sansoni, L. et al. Two-particle Bosonic-Fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
5. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nature Physics 8, 285-291 (2012).  
6. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
7. Pittman, T. B., Jacobs, B. C. & Franson, J. D. Probabilistic quantum logic operations using polarization beam splitters. Phys. Rev. A 64, 062311 (2001).  
8. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169-176 (2005).  
9. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
10. Politi, A., Cryan, M., J. rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
11. O'Brien, J. L., Furusawa, A. & Vucovic, Photonic quantum technologies. Nature Photonics 3, 687-695 (2009).  
12. Politi, A. Matthews, J. C. F. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
13. Bonneau, D. et al. Quantum interference and manipulation of entanglement in silicon wire waveguide quantum circuits. New J. Phys. 14, 045003 (2012).  
14. Bonneau, D. et al. Fast path and polarization manipulation of telecom wavelength single photons in lithium niobate waveguide devices. Phys. Rev. Lett. 108, 053601 (2012).  
15. Sansoni, L. et al. Polarization entangled state measurement on a chip. Phys. Rev. Lett. 105, 200503 (2010).

16. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nature Communications 2, 566 (2011).  
17. Pernice, W. et al. High speed and high efficiency travelling wave single-photon detectors embedded in nanophotonic circuits. arXiv:1108.5299.  
18. Kwiat, P. et al., New high-intensity source of polarization-entangled photon pairs. Phys. Rev. Lett. 75, 4337-4341 (1995).  
19. Tanzilli, S. et al. On the genesis and evolution of integrated quantum optics. *Laser Photonics* Rev. 6, 115-143 (2012).  
20. Shapiro, J. H. & Wong, F. N. C. On-demand single-photon generation using a modulator array of parametric downconverters with electro-optic polarization controls. Opt. Lett. 32, 2698-2700 (2007).  
21. Suhara, T., Nakaya, G., Kawashima, J. & Fujimura, M. Quasi-phase-matched waveguide devices for generation of postselection-free polarization entangled twin photons, IEEE Photon. Technol. Lett. 21, 1096-1098 (2009).  
22. Martin, A. et al. A polarization entangled photon-pair source based on a type-II PPLN waveguide emitting at a telecom wavelength. New J. Phys. 12, 103005 (2010).  
23. Thomas, A., Herrmann, H. & Sohler, W. Generation of non-degenerated polarization entangled photon pairs in periodically poled Ti:LiNbO₃ waveguides with interlaced domains. In the proceedings of European Quantum Electronics Conference (EQEC) 2011, paper: ED_P1.  
24. Lim, H. C., Yoshizawa, A., Tsuchida, H. & Kikuchi, K. Stable source of high quality telecom-band polarization-entangled photon-pairs based on a single, pulse-pumped, short PPLN waveguide. Opt. Express 16, 12460–12468 (2008).  
25. Takesue, H. et al. Generation of polarization entangled photon pairs using silicon wire waveguide. Opt. Express 16, 5721-5727 (2008).  
26. Arahira, S., Namekata, N., Kishimoto, T., Yaegashi, H. & Inoue, S. Generation of polarization entangled photon pairs at telecommunication wavelength using cascaded  $\chi^{(2)}$  processes in a periodically poled  $\mathrm{LiNbO_3}$  ridge waveguide. Opt. Express 19, 16032-16043 (2011).  
27. Zhukovsky, S. V. et al. Generation of maximally-polarization-entangled photons on a chip. Phys. Rev. A 85, 013838 (2012).  
28. Kang, D. & Helmy, A. S. Generation of polarization entangled photons using concurrent type-I and type-0 processes in AlGaAs ridge waveguides. Opt. Lett. 37, 1481-1483 (2012).  
29. Nasu, Y., Mizuno, T., Kasahara, R. & Saida, T. Temperature insensitive and ultra wideband silica-based dual polarization optical hybrid for coherent receiver with highly symmetrical interferometer design. Opt. Express 19, B112-B118 (2011).  
30. Fukuda, H. et al. Silicon photonic circuit with polarization diversity. Opt. Express 16, 4872-4880 (2008).  
31. Sharping, J. et al. Generation of correlated photons in nanoscale silicon waveguides. Opt. Express 14, 12388-12393 (2006).  
32. Harada, K.-I. et al. Frequency and polarization characteristics of correlated photon pair generation using a silicon wire waveguide. IEEE J. Sel. Topics Quantum Electron 16, 325-331 (2010).  
33. Fukuda, H. et al. Polarization rotator based on silicon wire waveguides. Opt. Express 16, 2628-2635 (2008).  
34. Shoji, T., Tsuchizawa, T., Watanabe, T., Yamada, K. & Morita, H. Low loss mode size converter from  $0.3\mu \mathrm{m}$  square Si wire waveguides to singlemode fibers. Electron. Lett. 38, 1669-1670 (2002).  
35. Tsuchizawa, T. et al. Monolithic integration of silicon-, germanium-, and silica-based optical devices for telecommunications applications. IEEE J. Sel. Topics Quantum Electron. 17, 516-525 (2011).

36. James, D. F. V., Kwiat, P. G., Munro, W. J. & White, A. G. Measurement of qubits. Phys Rev. A 64, 052312 (2001).  
37. Modlawska, J. & Grudka, A. Increasing singlet fraction with entanglement swapping. Phys. Rev. A 78, 032321 (2008).  
38. Badziag, P., Horodecki, M., Horodecki, P. & Horodecki, R. Local environment can enhance fidelity of quantum teleportation. Phys. Rev. A 62, 012311 (2000).  
39. Ikuta, R. et al. Wide-band quantum interface for visible-to-telecommunication wavelength conversion. Nature Communications 2, 537 (2011).  
40. Nasu, Y. et al. Reduction of polarization dependence of PLC Mach-Zehnder interferometer over wide wavelength range. J. Lightwave Technol. 27, 4814-4820 (2009).  
41. Horn, R. et al. Monolithic source of photon pairs. Phys. Rev. Lett. 108, 153605 (2012).  
42. Hirabayashi, K. & Amano, C. Liquid-crystal polarization controller arrays on planar lightwave circuits. IEEE Photon. Technol. Lett. 14, 504-506 (2002).  
43. Mizuno, T., Goh, T., Ohyama, T., Hashizume, Y. & Kaneko, A. Integrated in-band OSNR monitor based on planar lightwave circuit, in Proceedings of the ECOC2009, Session 7.2.5 (2009).  
44. Himeno, A., Kato, K. & Miya, T. Silica-based planar lightwave circuits. IEEE J. Sel. Topics Quantum Electron. 4, 913-924 (1998).  
45. Kim, J.-W., Park, S.-H., Chu, W.-S. & Oh, M.-C. Integrated-optic polarization controllers incorporating polymer waveguide birefringence modulators. Opt. Express 20, 12443-12448 (2012).  
46. Yamazaki, H., Yamada, T., Goh, T., Sakamaki, Y. & Kaneko, A. 64QAM modulator with a hybrid configuration of silica PLCs and  $\mathrm{LiNbO_3}$  phase modulators. IEEE Photon. Technol. Lett. 22, 344-346 (2010).

# Acknowledgements

We are grateful to T. Watanabe, K. Azuma, M. Oguma, H. Takahashi, J. L. O'Brien, and S. Itabashi for fruitful discussions. This work was supported in part by a Grant-in-Aid for Scientific Research (No. 22360034) from the Japan Society for the Promotion of Science.

# Author contributions

NM and HL performed the experiments and data analysis. NM developed the device concept. HF, TT and KY designed and fabricated the sample. YT and HT led the project. All authors discussed the results and contributed to the preparation of the manuscript.

# Additional information

Supplementary information accompanies this paper at http://www.nature.com/scientificreports

Competing financial interests: The authors declare no competing financial interests.

License: This work is licensed under a Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit http://creativecommons.org/licenses/by/3.0/

How to cite this article: Matsuda, N. et al. A monolithically integrated polarization entangled photon pair source on a silicon chip. Sci. Rep. 2, 817; DOI:10.1038/srep00817 (2012).

DOI: 10.1038/srep01590

SUBJECT AREAS:

QUANTUM OPTICS

NONLINEAR OPTICS

OPTICAL PHYSICS

QUANTUM PHYSICS

SCIENTIFIC REPORTS:

1:817

DOI: 10.1038/srep00817

(2012)

Published:

12 November 2012

Updated:

5 April 2013

# ERRATUM: A monolithically integrated polarization entangled photon pair source on a silicon chip

Nobuyuki Matsuda, Hanna Le Jeannic, Hiroshi Fukuda, Tai Tsuchizawa, William John Munro, Kaoru Shimizu, Koji Yamada, Yasuhiro Tokura & Hiroki Takesue

Due to a technical error, an incorrect version of Figure. 1 was published in the original Article. The corrected version of the Figure appears below.

![](images/6369be50515b7a0fb3de64e06e1fe71855e22269e0b807f3b692ccc6ab710dc5.jpg)

![](images/ef241695c46764afbf5b189c9dddb2131c4cc07accaa4da11ff3cd2c210869d5.jpg)  
Figure 1 | A monolithically integrated polarization-entanglement source. (a) The source, fabricated on a silicon-on-insulator substrate, consists of a silicon-wire-based  $90^{\circ}$  polarization rotator sandwiched by two nonlinear silicon wire waveguides. The device generates the polarization entanglement as a superposition of the two events shown in (b). The figure is not to scale for clarity.