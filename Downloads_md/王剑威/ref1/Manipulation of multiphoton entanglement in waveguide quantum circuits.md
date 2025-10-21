# Manipulation of multiphoton entanglement in waveguide quantum circuits

Jonathan C. F. Matthews\*, Alberto Politi\*, André Stefanov† and Jeremy L. O'Brien*

On-chip integrated photonic circuits are crucial to further progress towards quantum technologies and in the science of quantum optics. Here we report precise control of single photon states and multiphoton entanglement directly on-chip. We manipulate the state of path-encoded qubits using integrated optical phase control based on resistive elements, observing an interference contrast of  $98.2 \pm 0.3\%$ . We demonstrate integrated quantum metrology by observing interference fringes with two- and four-photon entangled states generated in a waveguide circuit, with respective interference contrasts of  $97.2 \pm 0.4\%$  and  $92 \pm 4\%$ , sufficient to beat the standard quantum limit. Finally, we demonstrate a reconfigurable circuit that continuously and accurately tunes the degree of quantum interference, yielding a maximum visibility of  $98.2 \pm 0.9\%$ . These results open up adaptive and fully reconfigurable photonic quantum circuits not just for single photons, but for all quantum states of light.

Controlling quantum systems is not only a fundamental scientific endeavour, but also holds promise for profound new technologies<sup>1-3</sup>. Quantum photonics already provides enhanced communication security<sup>3-7</sup>; it has demonstrated increased precision by beating the standard quantum limit in metrology<sup>8-11</sup> and the diffraction limit in lithography<sup>12,13</sup>, it holds great promise for quantum computation<sup>14,15</sup>, and it continues to advance fundamental quantum science. The recent demonstrations of integrated quantum circuits<sup>16-18</sup> are key steps towards these new technologies and for further progress in fundamental science applications.

Technologies based on harnessing quantum-mechanical phenomena require methods to precisely prepare and control the state of quantum systems. Manipulation of a path-encoded qubit—a single photon in an arbitrary superposition of two optical paths, which is the natural encoding for waveguides[16,17]—requires control of the relative phase  $\phi$  between the two optical paths and the amplitude in each path.

The integrated waveguide device shown schematically in Fig. 1a applies the unitary operation  $U_{\mathrm{MZ}} = U_{\mathrm{DC}}e^{i\phi \sigma_{\mathrm{Z}} / 2}U_{\mathrm{DC}}$ : each  $50\%$  splitting ratio (reflectivity  $\eta = 0.5$ ) directional coupler implements  $U_{\mathrm{DC}} = ie^{-i\pi \sigma_{\mathrm{Z}} / 4}He^{-i\pi \sigma_{\mathrm{Z}} / 4}$ , which transforms the logical qubit states according to  $U_{\mathrm{DC}}|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$  and  $U_{\mathrm{DC}}|1\rangle = \frac{1}{\sqrt{2}}(i|0\rangle + |1\rangle)$ , where the Hadamard gate  $H = (\sigma_{\mathrm{X}} + \sigma_{\mathrm{Z}}) / \sqrt{2}$  and  $\{\sigma_{\mathrm{X}}, \sigma_{\mathrm{Y}}, \sigma_{\mathrm{Z}}\}$  are the single-qubit Pauli operators, while control over the relative optical phase  $\phi$  between the two optical paths implements the phase gate  $e^{i\phi \sigma_{\mathrm{Z}} / 2}$ . A single-photon input into mode  $a$  is transformed into a superposition across modes  $c$  and  $d$ :

$$
\left| \right. 1 \left. \right\rangle_ {a} | 0 \rangle_ {b} \rightarrow \frac {1}{\sqrt {2}} \left( \right.\left| \right. 1 \left. \right\rangle_ {c} | 0 \rangle_ {d} + i | 0 \rangle_ {c} | 1 \rangle_ {d}\left. \right) \tag {1}
$$

(a single-photon input into mode  $b$  is transformed into the same superposition but with a relative  $\pi$  phase shift). The relative optical phase is then controlled by the parameter  $\phi$ , so that

$$
\frac {1}{\sqrt {2}} \left(| 1 \rangle_ {c} | 0 \rangle_ {d} + i | 0 \rangle_ {c} | 1 \rangle_ {d}\right)\rightarrow \frac {1}{\sqrt {2}} \left(| 1 \rangle_ {c} | 0 \rangle_ {d} + i e ^ {i \phi} | 0 \rangle_ {c} | 1 \rangle_ {d}\right) \tag {2}
$$

![](images/b3407b99844d29d61925b2459a2736b1aa15b7d0d44feac3ca6b0e7b2aa0a4bf.jpg)  
a

b  
![](images/042ff8f1f58dc64b1087542fd41e249f57bfb582096e1962aaff1cc7a410357e.jpg)  
c, The simulated intensity profile of the guided single mode in the silica waveguides at a wavelength of  $780\mathrm{nm}$ .

![](images/d579fc60e682187fc51de4c801b41e20740bba3a6cba8352bbdcc3a3e9c65beb.jpg)  
Figure 1 | Manipulating quantum states of light on a chip. a, Schematic of a waveguide circuit with the relative optical phase  $\phi$  controlled by applying a voltage  $V$  across the contact pads  $p_1$  and  $p_2$  (not to scale). b, Illustration of the cross-section of one waveguide located beneath a resistive heater.  
C

before the two modes are recombined at the second  $\eta = 0.5$  coupler. This is of course a quantum mechanical description of a Mach-Zehnder (MZ) interferometer operating at the single photon level—something that is well understood in terms of bright coherent light. The device shown in Fig. 1a can also be used to manipulate the phase of multiphoton, entangled states of light.

Two additional relative phase controllers before and after this device would enable arbitrary one-qubit unitary operations $^{19}$ , including state preparation and measurement. First note the relations  $\sigma_{X}e^{i\phi \sigma_{Z} / 2} = e^{-i\phi \sigma_{Z} / 2}\sigma_{X}$  and  $U_{\mathrm{MZ}} = ie^{i\phi \sigma_{\mathrm{Y}} / 2}\sigma_{\mathrm{X}}$ . For some real  $\phi_1, \phi_2, \phi_3$ , arbitrary qubit operations can be decomposed as  $U_{\mathrm{arb}} = e^{i\phi_3\sigma_{Z} / 2}e^{i\phi_2\sigma_{\mathrm{Y}} / 2}e^{i\phi_1\sigma_{Z} / 2}$ ; arbitrary qubit preparation from the logical basis is applied by  $U_{\mathrm{prep}} = e^{i\phi_3\sigma_Z / 2}e^{i\phi_2\sigma_Y / 2}$ .

![](images/7507b2574eeffd3b5ca69a84445d11399cd86b1664160babcbbac34899602052.jpg)  
Figure 2 | Multiphoton state preparation. Pulsed, coherent  $390\mathrm{nm}$  light pumps a Type-I nonlinear bismuth borate  $\mathrm{BiB}_3\mathrm{O}_6$  (BiBO) crystal for spontaneous parametric down-conversion. Depending on the average pump power, we produce two- and four-photon states of  $780\mathrm{nm}$  degenerate photons in two paths. (See Methods for further details.) SHG, second harmonic generation; IF, interference filter; DM, dichroic mirror; PMF, polarization maintaining fibre; SPDC, spontaneous parametric down-conversion.

The inverse (or time-reversed) operation  $U_{\mathrm{prep}}^{\dagger}$  provides arbitrary projective measurement<sup>1</sup>. By combining several such devices across  $N$  waveguides, it is possible to realize any arbitrary  $N$ -mode unitary operator<sup>19</sup>.

We begin by demonstrating a device that implements  $U_{\mathrm{MZ}}$ , in which the phase shift  $\phi$  is controlled by the voltage applied to a lithographically defined resistive heater. We then use this device to manipulate one-, two- and four-photon entangled states relevant to quantum metrology. Finally, we demonstrate how such a device can be used to realize a reconfigurable photonic quantum circuit.

# Results

Voltage-controlled phase shift. Waveguide devices, as illustrated in the cross-section in Fig. 1b, were fabricated on a 4-inch silicon wafer (material I), onto which a  $16 - \mu \mathrm{m}$  layer of thermally grown undoped silica was deposited as a buffer to form the lower cladding of the waveguides (II). A  $3.5 - \mu \mathrm{m}$  layer of silica doped with germanium and boron oxides was then deposited by flame hydrolysis; the material of this layer constitutes the core of the stucture and was patterned into  $3.5 - \mu \mathrm{m}$ -wide waveguides using standard optical lithographic techniques (III). The  $16 - \mu \mathrm{m}$  upper cladding (IV) was composed of phosphorus and boron-doped silica with a refractive index matched to that of the buffer. Simulations indicated single-mode operation at  $780\mathrm{nm}$ , as shown in Fig. 1c. A final metal layer was lithographically patterned on top of the devices to form resistive elements  $(R)$  and the metal connections and contact pads  $(p_1$  and  $p_2)$  shown in Fig. 1a.

When a voltage was applied between  $p_1$  and  $p_2$ , the current in  $R$  generated heat, which dissipated into the device and locally raised the temperature  $T$  of the core and cladding material of the waveguide section directly below. To a first approximation, the change in refractive index  $n$  of silica is given[20] by  $\mathrm{dn} / \mathrm{dT} = 1 \times 10^{-5} / \mathrm{K}$  (independent of compositional variation), which in turn alters the mode group index of the light confined in the waveguide beneath  $R$ . The devices were designed to enable a continuously variable phase shift  $\phi \in [-\pi /2,\pi /2]$  and operate at room temperature. A consequence of the miniature and monolithic structure of the chip is that no strict global temperature control of the device is required for stability (see Supplementary Information).

The voltage-controlled phase inside the waveguide circuit, shown schematically in Fig. 1a, was determined by a nonlinear relation  $\phi (V)$ , which we calibrated using a two-photon interference effect

![](images/4b6baeacf9707252b9b22c9bcd79bb48427e690b7c69c103defecb2b0292fb11.jpg)  
Figure 3 | Calibration of voltage-controlled phase shift. The two-photon interference pattern generated from simultaneous detection of a single photon at both outputs  $g$  and  $h$  as the voltage applied across the device was varied between 0 and 5 V. Error bars are given by Poissonian statistics. Inset: plot of the phase-voltage relationship determined from this calibration.

(see Supplementary Information): ideally, the maximally path entangled state of two photons

$$
\frac {1}{\sqrt {2}} \left(| 2 \rangle_ {c} | 0 \rangle_ {d} + | 0 \rangle_ {c} | 2 \rangle_ {d}\right) \tag {3}
$$

is generated inside the device $^{21-27}$  on inputting the state  $|1\rangle_a|1\rangle_b$ , which we produced using the setup shown in Fig. 2. After the phase shift this entangled state is transformed to  $\frac{1}{\sqrt{2}}(|2\rangle_e|0\rangle_f + e^{i2\phi}|0\rangle_e|2\rangle_f)$ . Figure 3 shows the results of this calibration, in which the rate of simultaneous detection of two photons at outputs  $g$  and  $h$  is plotted as a function of the applied voltage  $V$  across  $p_1$  and  $p_2$ . The phase voltage relationship was verified to be a polynomial function of the form

$$
\phi (V) = \alpha + \beta V ^ {2} + \gamma V ^ {3} + \delta V ^ {4} \tag {4}
$$

where the parameters were found by means of best-fit (see Supplementary Information); the resulting relationship is plotted in the inset of Fig. 3. In comparison to simply using one-photon 'classical' interference, this 'quantum calibration' harnesses the reduced de Broglie wavelength $^{4-6}$  of two-photon interference $^{21-27}$  to wider sample the pattern of phase-dependent interference, thereby giving greater precision in the  $\phi(V)$  calibration. This approach is particularly useful because the range of  $\phi$  we could implement was limited by the maximum voltage that can be applied across the electrodes. The phase shift was found to be stable on a timescale of several hours (see Supplementary Information).

Multiphoton entangled state manipulation. Having obtained  $\phi (V)$ , we were able to analyse the sinusoidal interference pattern arising from single-photon detections at outputs  $g$  and  $h$  when launching single photons into input  $a$  and controlling  $\phi (V)$ . Ideally, the probability of detecting photons varies as

$$
P _ {g} = 1 - P _ {h} = \frac {1}{2} [ 1 - \cos (\phi) ] \tag {5}
$$

yielding sinusoidal interference fringes with a period of  $2\pi$ . The observed fringes (Fig. 4a) show a high contrast  $C = (N_{\mathrm{max}} - N_{\mathrm{min}}) / (N_{\mathrm{max}} + N_{\mathrm{min}})$  of  $C = 0.982 \pm 0.003$ . From this contrast, and assuming no mixture or complex phase is introduced, it is possible to calculate the average fidelity  $F$  between the realized and ideal output state  $U_{\mathrm{MZ}}|0\rangle = \cos(\phi/2)|0\rangle + i\sin(\phi/2)|1\rangle$ . Averaging over the range  $\phi \in [-\pi/2, \pi/2]$  we find  $\bar{F} = 0.99984 \pm 0.00004$ .

![](images/b847492336d1024dff2ce3d59e5951f6cb25989d15af3c81ee8e120542396bf1.jpg)

![](images/918cac3de26a21a2f18f999a94ffe4760d0fce6b163d076b3b0ab3eda819d888.jpg)  
Figure 5 | A reconfigurable quantum circuit. Visibility of the Hong-Ou-Mandel experiment performed using the integrated MZ interferometer as a continuously variable beamsplitter with effective reflectivity  $\eta = \sin^2 (\phi /2)$ . The solid line is a theoretical fit that includes a small phase offset and a small amount of mode mismatch as the only two free parameters that modify equations (10) and (11). Error bars are given by confidence intervals on the best-fit parameter. Left inset: High-visibility two-photon interference. Right inset: Low-visibility two-photon interference. Both inset plots are displayed as a plot of two-photon rate versus the relative optical delay between the interfering photons and fitted with a function that takes into account the non-Gaussian shape of the interference filter used in the experiment. Error bars for each inset are given by Poissonian statistics.

![](images/8b762689c956fdddcd32a5ff2b06a8b2325527629d1c2a42cf50d767c7bee93e.jpg)  
Figure 4 | Integrated quantum metrology. a, One-photon count rates at the outputs  $g$  (blue triangles, dotted fit) and  $h$  (black squares, solid fit) as the phase  $\phi(V)$  is varied on inputting the one-photon state  $|1\rangle_a|0\rangle_b$ . b, Two-photon coincidental detection rate between the outputs  $g$  and  $h$  when inputting the two-photon state  $|1\rangle_a|1\rangle_b$  and varying the phase  $\phi(V)$ . c, Four-photon coincidental detection rate of the output state  $|3\rangle_g|1\rangle_h$  when inputting the four-photon state  $|2\rangle_a|2\rangle_b$ . Error bars are given by Poissonian statistics.

These devices also enable us to manipulate and analyse multiphoton entangled states. For example, the state (3) should ideally be transformed according to  $\frac{1}{\sqrt{2}}(|2\rangle_e|0\rangle_f + e^{2i\phi}|0\rangle_e|2\rangle_f)$ . To confirm the correct on-chip control of this entangled state, simultaneous detection of a single photon at each output  $g$  and  $h$  was recorded as a function of  $\phi$ ; this ideally yields a  $\lambda / 2$  interference fringe described by

$$
P _ {g, h} = \frac {1}{2} (1 + \cos 2 \phi) \tag {6}
$$

with period  $\pi$ -half the period of the one-photon interference fringes. The two-photon interference fringe shown in Fig. 4b plots the measured simultaneous detection rate as a function of  $\phi$ . The contrast is  $C = 0.972 \pm 0.004$ , which is greater than the threshold  $C_{\mathrm{th}} = 1 / \sqrt{2}$  required to beat the standard quantum limit[28], as described below. Note that although a two-photon interference fringe was used to calibrate the phase shift, this calibration is not

![](images/758330053e7b63f442d5348d230e3c8fe5d9f72bcdaa2a281b2e3910dd64bb3f.jpg)

required to claim a  $\lambda /2$  interference fringe; this is simply confirmed by comparison with the one-photon fringe, which can be done even without calibrating the phase.

The interference fringe shown in Fig. 4b arises from the two-photon maximally path entangled state that is an equal superposition of  $N$  photons in one mode and  $N$  photons in another mode:  $|N\rangle |0\rangle + |0\rangle |N\rangle$  (ref. 29). Such a state evolves under a  $\phi$  phase shift in the second mode to  $|N\rangle |0\rangle + e^{iN\phi} |0\rangle |N\rangle$  and can in principle be used to estimate an unknown phase  $\phi$  with a sensitivity  $\Delta \phi = 1 / N$ , better than the standard quantum limit  $\Delta \phi = 1 / \sqrt{N}$  (the limit attainable with classical schemes). By inputting the four-photon state  $|2\rangle_{a}|2\rangle_{b}$ , nonclassical interference at the first directional coupler ideally produces the state [6,28,30]

$$
\sqrt {\frac {3}{4}} \left(| 4 \rangle_ {c} | 0 \rangle_ {d} + | 0 \rangle_ {c} | 4 \rangle_ {d}\right) / \sqrt {2} + \frac {1}{\sqrt {4}} | 2 \rangle_ {c} | 2 \rangle_ {d} \tag {7}
$$

At the second directional coupler, quantum interference means that only the  $|4\rangle |0\rangle +|0\rangle |4\rangle$  part of this state gives rise to  $|3\rangle_{g}|1\rangle_{h}$  and  $|1\rangle_{g}|3\rangle_{h}$  in the output state of the interferometer. By varying the phase  $\phi$  in the interferometer, the probability of detecting either of the states  $|3\rangle_{g}|1\rangle_{h}$  or  $|1\rangle_{g}|3\rangle_{h}$  is given by

$$
P _ {3 g, h} = P _ {g, 3 h} = \frac {3}{8} (1 - \cos 4 \phi) \tag {8}
$$

and yields a  $\lambda / 4$  interference fringe with period  $\pi / 2$ . We measured the four-photon interference fringe shown in Fig. 4c, which plots the rate of simultaneous detection of four photons corresponding to the state  $|3\rangle_g|1\rangle_h$  (by cascading three detectors using  $1 \times 2$  fibre-beamsplitters at the output  $g$ ) against the phase  $\phi$ . The contrast of this four-photon interference is  $C = 0.92 \pm 0.04$ , which is greater than the threshold to beat the standard quantum limit[28].

Reconfigurable quantum circuits. Quantum interference of photons<sup>31</sup> at a directional coupler (or beamsplitter) lies at the

heart of the multiphoton interference fringes shown in Fig. 4 and is the crucial underlying physical process in linear optical networks for quantum-information science. The reflectivity  $\eta$  of a coupler determines the degree of quantum interference, thereby making  $\eta$  the critical parameter for quantum operation. The directional couplers in the device shown schematically in Fig. 1 were lithographically set to  $\eta = 1/2$ . More general photonic circuits, including optical entangling logic gates[14,16,32,33], are composed of a number of different reflectivity couplers, whereas adaptive schemes whose function depends on the input state, such as Fock state filters[34-36], make use of devices equivalent to a single coupler with variable  $\eta$ . Reconfigurable photonic circuits, including routing of photons, can be realized by combining such variable  $\eta$  devices. By controlling the phase  $\phi$  within our devices, we implement the unitary operation

$$
U _ {\mathrm {M Z}} \doteq \left( \begin{array}{c c} \sin (\phi / 2) & \cos (\phi / 2) \\ \cos (\phi / 2) & - \sin (\phi / 2) \end{array} \right) \tag {9}
$$

acting on the two input waveguides $^{19}$ . This operation is equivalent to a single coupler with variable reflectivity

$$
\eta = \sin^ {2} \frac {\phi}{2} \tag {10}
$$

We performed multiple quantum interference experiments $^{31}$  in which two photons were launched into inputs  $a$  and  $b$  of the device. While scanning through the relative arrival time with an off-chip optical delay, we measured the rate of simultaneous detection of a single photon at both outputs  $g$  and  $h$ . Each experiment resulted in a quantum interference 'dip' in this rate of simultaneous photon detection, centred around zero delay (see insets to Fig. 5). The depth of such a dip indicates the degree of quantum interference, which can be quantified by the visibility  $V = (N_{\mathrm{max}} - N_{\mathrm{min}}) / N_{\mathrm{max}}$ . Ideally,

$$
V _ {\text {i d e a l}} = \frac {2 \eta (1 - \eta)}{1 - 2 \eta + 2 \eta^ {2}} \tag {11}
$$

The main panel in Fig. 5 plots the quantum interference visibility observed for different values of  $\phi$  and hence  $\eta$ . The insets of Fig. 5 show two examples of the raw data used to generate this curve: (right)  $\phi = -0.49 \pm 0.01$  rad,  $V = 0.129 \pm 0.009$ ; (left)  $\phi = -1.602 \pm 0.01$  rad,  $V = 0.982 \pm 0.009$ . The average relative visibility  $V_{\mathrm{rel}} = V / V_{\mathrm{ideal}}$  for all the data in Fig. 5 is  $\overline{V}_{\mathrm{rel}} = 0.980 \pm 0.003$ .

# Discussion

Integrated optics has been developed primarily by the telecommunications industry for devices that allow high-speed information transmission, including optical switches, wavelength division multiplexers and modulators. Quantum optics appears destined to benefit from existing integrated optics technologies, as well as drive new developments for its own needs. The reconfigurable quantum circuit we demonstrate could be used as the fundamental element to build a large-scale circuit capable of implementing any unitary operation on many waveguides. A thermal-based  $32 \times 32$  waveguide switch has been demonstrated[37]. Implementing an arbitrary unitary on this number of modes would require a comparable number of resistive elements. This is well beyond anything conceivable with bulk optics. The millisecond timescales available with thermal switching are suitable for reconfigurable circuits, for state preparation, quantum measurement, quantum metrology[2] and perhaps even full-scale quantum computing[38]. Other applications demanding fast switching, such as adaptive circuits for quantum control and feedforward, will require subnanosecond switching, which is possible using electro-optic materials such as  $\mathrm{LiNbO}_3$ , used to make modulators operating at tens of gigahertz[39].

In addition to the demonstrations presented here, these devices may be used for other quantum states of light, for the fundamental sciences of quantum optics $^{40-42}$  and quantum information $^{43-46}$ . In particular, phase control will be particularly important for homodyne detection required for phase estimation $^{47}$  and adaptive measurements $^{48}$  with squeezed states of light. Our results point towards adaptive and arbitrarily reconfigurable quantum networks capable of generating, manipulating and characterizing multiphoton states of light with near-unit fidelity. Possible future applications span all of quantum information science from metrology to information processing.

# Methods

Devices. The bend radius of curves in the directional couplers in the waveguide circuit are  $15\mathrm{mm}$  at the tightest curvature, the effective interaction length of each directional coupler is  $2.95\mathrm{mm}$ , and each path within the interferometer is  $9.7\mathrm{mm}$  (defined from the end of the first directional coupler to the beginning of the second directional coupler). The maximum optical path difference with the maximum voltage we apply is  $\sim \lambda / 2$  (that is,  $\sim 390\mathrm{nm}$ ). The physical length of the chip from input facet to output facet is  $26\mathrm{mm}$ .

Multiphoton generation. The experiments reported were conducted using degenerate single-photon pairs at a wavelength of  $780\mathrm{nm}$  produced by means of spontaneous parametric downconversion (SPDC). The nonlinear crystal used was a type-I phase-matched bismuth borate  $\mathrm{BiB}_3\mathrm{O}_6$  (BiBO) pumped by a  $390\mathrm{nm}$  150 fs pulsed laser focused to a waist of  $\omega_0\approx 40~\mu \mathrm{m}$ . The  $390\mathrm{nm}$  pump was prepared using a further BiBO crystal, phase-matched for second harmonic generation (SHG) to double the frequency of a  $780\mathrm{nm}$  mode-locked Ti:sapphire laser focused to a waist of  $\omega_0\approx 40~\mu \mathrm{m}$ ; four successive dichroic mirrors (DM) were used to purify the pump beam spectrally. Degenerate photon pairs were created by the SPDC crystal and passed through  $3\mathrm{nm}$  interference filters (IF), which filtered each photon to a coherence length of  $l_{c} = \lambda^{2} / \Delta \lambda \approx 200~\mu \mathrm{m}$ . The photons were collected into two single-mode polarization maintaining fibers (PMFs) coupled to two diametrically opposite points  $x$  and  $y$  on the SPDC cone. In the case of low average pump power, the state  $|1\rangle_x|1\rangle_y$  was produced with a rate of  $100\mathrm{s}^{-1}$ . On increasing the average pump power, the multiphoton production rate from the downconversion process was no longer negligible such that it is possible to produce two degenerate pairs of photons in the state  $|2\rangle_x|2\rangle_y$ .

Coupling to devices. The photons coupled into PMF were launched into the chip and collected at the outputs using two arrays of eight PMFs, with  $250~\mu \mathrm{m}$  spacing, to match that of the waveguides. The photons were detected using fiber coupled single photon counting modules (SPCMs). The PMF arrays and chip were directly buttcoupled, with index matching fluid, to obtain an overall coupling efficiency of  $\sim 60\%$  through the device (input plus output insertion losses  $\sim 40\%$ ).

# Received 15 January 2009; accepted 23 April 2009; published online 24 May 2009

# References

1. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
2. Giovannetti, V., Lloyd, S. & Maccone, L. Quantum-enhanced measurements: beating the standard quantum limit. Science 306, 1330-1336 (2004).  
3. Gisin, N., Ribordy, G., Tittel, W. & Zbinden. Quantum cryptography. Rev. Mod. Phys. 74, 145-195 (2002).  
4. www.secoqc.net  
5. www.idQuantique.com  
6. www.magiqtech.com  
7. www.smartquantum.com  
8. Mitchell, M. W., Lundeen, J. S. & Steinberg, A. M. Super-resolving phase measurements with a multiphoton entangled state. Nature 429, 161-164 (2004).  
9. Walther, P. et al. de Broglie wavelength of a non-local four-photon state. Nature 429, 158-161 (2004).  
10. Nagata, T., Okamoto, R., O'Brien, J. L., Sasaki, K. & Takeuchi, S. Beating the standard quantum limit with four-entangled photons. Science 316, 726-729 (2007).  
11. Higgins, B. L., Berry, D. W., Bartlett, S. D., Wiseman, H. M. & Pryde, G. J. Entanglement-free Heisenberg-limited phase estimation. Nature 450, 393-396 (2007).  
12. Boto, A. N. et al. Quantum interferometric optical lithography: exploiting entanglement to beat the diffraction limit. Phys. Rev. Lett. 85, 2733-2736 (2000).  
13. Kawabe, Y., Fujiwara, H., Okamoto, R., Sasaki, K. & Takeuchi, S. Quantum interference fringes beating the diffraction limit. Opt. Express 15, 14244-14250 (2007).  
14. Knill, E., Laamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).

15. O'Brien, J. L. Optical quantum computing. Science 318, 1567-1570 (2007).  
16. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
17. Marshall, G. D. et al. Laser written waveguide photonic quantum circuits. <http://arxiv.org/abs/0902.4357> (2009).  
18. Clark, A. S. et al. All-optical-fiber polarization-based quantum logic gate. Phys. Rev. A 79, 030303 (2009).  
19. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
20. Kenichi, I. & Yokubun, Y. Encyclopedic Handbook of Integrated Optics (CRC Press, 2006).  
21. Ou, Z. Y., Zou, X. Y., Wang, L. J. & Mandel, L. Experiment on nonclassical fourth-order interference. Phys. Rev. A 42, 2957-2965 (1990).  
22. Rarity, J. G. et al. Two-photon interference in a Mach-Zehnder interferometer. Phys. Rev. Lett. 65, 1348-1351 (1990).  
23. Kuzmich, A. & Mandel, L. Sub-shot-noise interferometric measurements with two-photon states. Quant. Semiclass. Opt. 10, 493-500 (1998).  
24. Fonseca, E. J. S., Monken, C. H. & Pádua, S. Measurement of the de Broglie wavelength of a multiphoton wave packet. Phys. Rev. Lett 82, 2868-2871 (1999).  
25. Edamatsu, K., Shimizu, R. & Itoh, T. Measurement of the photonic de Broglie wavelength of entangled photon pairs generated by spontaneous parametric down-conversion. Phys. Rev. Lett. 89, 213601 (2002).  
26. Eisenberg, H. S., Hodelin, J. F., Khoury, G. & Bouwmeester, D. Multiphoton path entanglement by non-local bunching. Phys. Rev. Lett. 94, 090502 (2005).  
27. Resch, K. J. et al. Time-reversal and super-resolving phase measurements. Phys. Rev. Lett. 98, 223601 (2007).  
28. Okamoto, R. et al. Beating the standard quantum limit: phase super-sensitivity of  $N$ -photon interferometers. New J. Phys. 10, 073033 (2008).  
29. Lee, H., Kok, P. & Dowling, J. P. A quantum Rosetta stone for interferometry. J. Mod. Opt. 49, 2325-2338 (2002).  
30. Steuernagel, O. de Broglie wavelength reduction for a multiphoton wave packet. Phys. Rev. A 65, 033820 (2002).  
31. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
32. O'Brien, J. L., Pryde, G. J., White, A. G., Ralph, T. C. & Branning, D. Demonstration of an all-optical quantum controlled-NOT gate. Nature 426, 264-267 (2003).  
33. Lanyon, B. P. et al. Simplifying quantum logic using higher-dimensional Hilbert spaces Nat. Phys., 5, 134-140 (2009).  
34. Sanaka, K., Resch, K. J. & Zeilinger, A. Filtering out photonic Fock states. Phys. Rev. Lett. 96, 083601 (2006).

35. Resch, K. J. et al. Entanglement generation by Fock-state filtration. Phys. Rev. Lett. 98, 203602 (2007).  
36. Okamoto, R. et al. An entanglement filter. Science 323, 483-485 (2009).  
37. Mino, S. Recent progress on PLC technologies for large-scale integration. Optical Fiber Communication and Optoelectronics Conference, 2007 Asia, 27 (2007).  
38. Kieling, K., Ruddolph, T. & Eisert, J. Percolation, renormalization, and quantum computing with nondeterministic gates. Phys. Rev. Lett. 99, 130501 (2007).  
39. Wooten, E. L. et al. A review of lithium niobate modulators for fiber-optic communications systems. IEEE J. Sel. Top. Quant. Electron. 6, 69-82 (2000).  
40. Lobino, M. et al. Complete characterization of quantum-optical processes. Science 322, 563-566 (2008).  
41. Furusawa, A. et al. Unconditional quantum teleportation. Science 282, 706-709 (1998)  
42. Parigi, V., Zavatta, A., Kim, M. & Bellini, M. Probing quantum commutation rules by addition and subtraction of single photons to/from a light field. Science 317, 1890-1893 (2007).  
43. Braunstein, S. L. & van Loock, P. Quantum information with continuous variables. Rev. Mod. Phys. 77, 513-577 (2005).  
44. Ourjoumtsev, A., Tualle-Brouri, R., Laurat, J. & Grangier, P. Generating optical Schrodinger kittens for quantum information processing. Science 312, 83-86 (2006).  
45. Menicucci, N. C., Flammia, S. T. & Pfister, O. One-way quantum computing in the optical frequency comb. Phys. Rev. Lett. 101, 130501 (2008).  
46. O'Brien, J. L. Quantum computing over the rainbow. Physics 1, 23 (2008).  
47. Pezzé, L., Smerzi, A., Khoury, G., Hodelin, J. F. & Bouwmeester, D. Phase detection at the quantum limit with multiphoton Mach-Zehnder interferometry. Phys. Rev. Lett. 99, 223602 (2007).  
48. Berry, D. W. & Wiseman, H. M. Adaptive phase measurements for narrowband squeezed beams. Phys. Rev. A. 73, 063824 (2006).

# Acknowledgements

We thank A. Laing, T. Nagata, S. Takeuchi and X. Q. Zhou for helpful discussions. This work was supported by IARPA, EPSRC, QIP IRC and the Leverhulme Trust.

# Additional information

Supplementary information accompanies this paper at www.nature.com/naturephotonics. Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/. Correspondence and requests for materials should be addressed to J.L.O'B.