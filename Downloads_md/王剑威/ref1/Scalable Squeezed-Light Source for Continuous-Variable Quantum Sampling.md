# Scalable Squeezed-Light Source for Continuous-Variable Quantum Sampling

Z. Vernon, $^{1}$ * N. Quesada, $^{1}$  M. Liscidini, $^{2,3}$  B. Morrison, $^{1}$  M. Menotti, $^{1}$  K. Tan, $^{1}$  and J.E. Sipe $^{4}$

$^{1}$ Xanadu, Toronto, Ontario M5G 2C8, Canada

$^{2}$ Dipartimento di Fisica, Università degli studi di Pavia, Via Bassi 6, Pavia 27100, Italy

<sup>3</sup> Impact Centre, University of Toronto, 411-112 College St., Toronto, Ontario M5G 1L6, Canada

$^{4}$  Department of Physics, University of Toronto, 60 St. George Street, Toronto, Ontario M5S 1A7, Canada

![](images/9caa922b3c59204494ab8ccfd97970895e048d50b39b0386e19b4af931a388af.jpg)

(Received 13 July 2018; revised manuscript received 31 October 2019; published 10 December 2019)

We propose a squeezed-light source meeting the stringent requirements of continuous-variable quantum sampling. Using the time-dependent effective second-order nonlinear interaction induced by a strong driving beam in the presence of the  $\chi_{3}$  response in a microresonator, our approach is compatible with established nanophotonic platforms. With typical realistic parameters, squeezed states with a mean photon number of 10 or higher can be generated in a single consistent temporal mode at repetition rates of over  $100\mathrm{MHz}$ . Over  $15\mathrm{dB}$  of squeezing is expected in existing ultralow-loss platforms.

DOI: 10.1103/PhysRevApplied.12.064024

# I. INTRODUCTION

Squeezed light is an essential resource for quantum information processing over continuous variables (CVs) [1]. Since the first measurements of small levels of squeezing were reported in the 1980s using hot atomic gases [2] and then in optical fibers [3], a number of techniques for its generation and control have been developed [4]. Dominant among these techniques are those using parametric fluorescence in  $\chi_{2}$  crystals [5] and those exploiting the Kerr effect on short pulses in optical fibers [6]. Both these techniques and others have enjoyed intensive development for achieving large squeezing levels [7], low-frequency sideband squeezing [8], and a tailored spatiotemporal-mode structure [9]. These efforts have had a marked impact on squeezing-enhanced metrology [10], quantum computation [11], simulation [12], and mesoscopic quantum optics [9].

Most recently, an especially promising avenue toward realizing practically useful CV quantum computation has emerged based on sampling in the Fock basis from multimode entangled Gaussian states [13]. This paradigm of Gaussian boson sampling has been shown to accommodate the embedding of a wide array of graph-structured problems, such as the identification of dense subgraphs [14] and perfect matchings [15] and measures of graph similarity [16], as well as the difficult problems in computational chemistry of estimating Franck-Condon factors [12] (crucial for calculating the vibronic spectra of molecules) and predicting molecular-docking configurations [17]. Aside from the practical utility of

these applications, Gaussian boson sampling is appealing for its compatibility with existing architectures for CV quantum information processing: squeezed states with modest squeezing levels (5–10 dB), low-loss linear optics, and high-efficiency photon-number-resolving detectors [18,19] are sufficient to build such a sampling machine.

While all of these elements have been demonstrated individually, a key challenge remains in designing a squeezed-light source that meets the stringent requirements demanded by a large-scale Gaussian boson sampling device or, indeed, any realistic CV quantum information processing machine. As is apparent from its history, squeezing is nearly ubiquitous across platforms for nonlinear optics; most physically realizable nonlinear-optical Hamiltonians can be used to generate some squeezing in certain regimes. But the mere ability to generate squeezing is insufficient and to date no squeezed-light source able to deliver all the features needed by practically useful CV quantum computation and simulation machines has yet been proposed. These key features are:

(i) Scalability: the ease with which many tens or hundreds of identical mutually coherent and stabilized squeezed-light sources can be integrated on one monolithic platform.  
(ii) Single-mode operation: the capability of producing squeezed light in a single spatiotemporal mode, consistent across multiple sources and a wide range of squeezing levels, obviating the need for bulky and lossy mode-selective elements.  
(iii) Squeezing levels sufficient to enable a genuine quantum advantage in computation [20], simulation [12], and sampling [13].

(iv) Compatibility with single-photon and photon-number-resolving detection [21], which are highly sensitive to noise from residual pump or spuriously generated light and require squeezed light without bright classical mean fields.

Requirements (ii) and (iii) can be succinctly stated in mathematical terms: an ideal source provides an output quantum state of the form  $e^{(r/2)a^2 - \mathrm{H.c.}}|\mathrm{vac}\rangle$ , with the squeezing factor  $r$  being reliably tunable and in which  $a$  is the annihilation operator for a single well-defined spatiotemporal mode, the characteristics of which do not vary over the tuning range of  $r$ . This feature is crucial, since most CV quantum sampling applications rely on interference between squeezed sources with different squeezing levels, requiring the temporal-mode shape to be fixed across multiple sources and power levels. Such a requirement is problematic, since the standard techniques used to select a well-defined temporal mode for photon-counting measurements, based on precise time-of-arrival statistics of photons incident on single-photon detectors, cannot be used in applications such as Gaussian boson sampling due to the slow response of available photon-number-resolving detection systems [18]. Also, while substantial effort [9] has gone into strategies to develop true single-mode squeezing in  $\chi_2$ -based systems, they suffer from spatial-mode engineering issues [22]. Further, if low-index-contrast waveguide platforms are employed, they cannot be scaled to large integrated systems with many modes, due to poor transverse modal confinement, which prevents the monolithic integration of high-depth linear-optical networks.

Existing work on integrated squeezed-light sources has generally focused on such low-index-contrast systems, typically using periodically poled lithium niobate. Two such identical sources were recently integrated alongside a linear-optical network for entanglement generation and local oscillator mixing [23] and an all-fiber integrated squeezed source has also been demonstrated [24]. In high-index-contrast nanophotonic systems, bright twin beams have been generated from a silicon-nitride optical parametric oscillator driven above threshold [25,26]. While useful for quantum metrology, such twin beams cannot be used in a photon-counting context, as they come with high levels of excess noise, as well as bright classical mean fields that would saturate any such detectors. Hoff et al. [27] suggested that a single resonance in a silicon-nitride ring could be used to generate degenerate squeezing using self-phase modulation. However, making such a source compatible with photon counting would require more than 100 dB of pump suppression within a few hundred megahertz of the squeezed signal, which is not practically feasible. Furthermore, thermorefractive effects [28,29] would add considerable excess noise, destroying squeezing over most of the mode [30]. Very recently, however, multiple

resonances in silicon-nitride rings driven below threshold have been used to generate approximately 4 dB (on-chip) of broadband nondegenerate and highly multimode quadrature squeezed vacuum [31], measured using both homodyne detection and photon-number-resolving detectors. These results indicate the promise of such a device for satisfying requirements (i), (iii), and (iv).

In this work, we propose a scalable squeezed-light source that comprehensively satisfies all the requirements (i)-(iv). We focus in particular on metrics relevant to near-term demonstrations of Gaussian boson sampling and its practical-use cases but we emphasize that our device offers substantial advantages over existing systems for many other CV quantum tasks, including squeezing-enhanced metrology protocols such as optical phase tracking [32] and gravitational wave detection [33]. To satisfy the scalability requirements, we turn to existing integrated nanophotonic platforms based on high-index-contrast waveguides having a third-order nonlinear-optical response, permitting the monolithic integration of nonlinear quantum light sources with high-depth programmable linear-optical circuits. A number of recent demonstrations have proven the ability of such platforms to accommodate very complex quantum photonic devices, incorporating multiple quantum light sources, filters, and large linear-optical networks [34,35] on a single chip. This progress has done much to justify increased optimism about the prospects of nanophotonic integrated quantum-computation devices [36,37].

Our device is based on the effective second-order nonlinear interaction induced by a strong continuous-wave (cw) coherent driving field in the presence of the  $\chi_{3}$  response of an integrated nanophotonic resonator [38]; this strategy has recently been used with silicon-nitride microrings to enable strong nonlinear coupling of resonant optical modes [39]. Combined with the resonance enhancement and tight transverse mode confinement provided by modern nanophotonic microresonators, this interaction can enable highly efficient parametric fluorescence when pumped by a secondary weaker field [40]. Crucially, our device provides robust control over the spatiotemporal-mode structure of the generated squeezed light. This allows the generation of true single-mode squeezed states in a single, well-defined, and well-behaved temporal mode at high repetition rates, consistent across a wide range of squeezing levels appropriate for CV quantum sampling. We focus on platforms that are available with present-day commercially available fabrication technology and assess the performance of our device based on currently achievable parameters.

In the following section, we lay out the theoretical tools used to calculate the output of the proposed device. In Sec. III, we then use these tools to calculate second-order field moments of the device output. In Sec. IV, we apply this to study a realistic system, as well as one with the best-reported specifications, before concluding in Sec. V.

# II. HAMILTONIAN AND FIELDS

An overview of the structure is illustrated in Fig. 1(a). We consider a high-finesse microresonator coupled to a channel waveguide; for definiteness, we display a microring resonator geometry, although our theory and conclusions apply equally well to other types of microresonators. The ring accommodates a set of discrete resonant modes  $J$ , with annihilation operators  $b_{J}$ . In this work, we focus on three key modes of interest: a drive mode  $D$ , a signal mode  $S$ , and a pump mode  $P$ . The intraresonator Hamiltonian arising from the linear and third-order nonlinear response that connects these three modes is [27,41]

$$
\begin{array}{l} H _ {\mathrm {r e s}} = \sum_ {J} \hbar \omega_ {J} b _ {J} ^ {\dagger} b _ {J} - \hbar \Lambda \left(b _ {D} b _ {P} b _ {S} ^ {\dagger} b _ {S} ^ {\dagger} + \mathrm {H . c .}\right) \\ - \frac {\hbar \Lambda}{2} \sum_ {J} b _ {J} ^ {\dagger} b _ {J} ^ {\dagger} b _ {J} b _ {J} \\ - 2 \hbar \Lambda \left(b _ {D} ^ {\dagger} b _ {D} \left(b _ {S} ^ {\dagger} b _ {S} + b _ {P} ^ {\dagger} b _ {P}\right) + b _ {P} ^ {\dagger} b _ {P} b _ {S} ^ {\dagger} b _ {S}\right) + H _ {X}, \tag {1} \\ \end{array}
$$

where  $\omega_{J}$  is the resonant frequency of mode  $J$  and  $\Lambda$  is a constant related to the resonator geometry and third-order nonlinearity; for a microring,  $\Lambda \approx \hbar \omega_{S}v_{g}^{2}\gamma_{\mathrm{NL}} / (2L)$  [27], in which  $v_{g}$  is the group velocity,  $L$  is the resonator length, and  $\gamma_{\mathrm{NL}}$  is the waveguide nonlinear parameter. In general, such a resonator accommodates many more than the three modes of interest; the couplings of these extra modes to the  $D,S,$  and  $P$  modes are contained in  $H_{X}$ , which we will examine shortly. While it is immediately clear from the form of this four-wave mixing Hamiltonian that squeezing can be generated, it is not obvious if or how it can be used to build a source that satisfies the additional requirements discussed previously, which are related to deeper features of the system dynamics that appear at the high pump powers needed to generate strong squeezing [42].

We restrict our analysis to the case in which the  $D$  mode is driven by a strong coherent cw beam, yielding a large amplitude  $\overline{\beta}_D e^{-i\omega Dt}$  in that mode, with  $\overline{\beta}_D$  constant; for convenience, we also take  $\overline{\beta}_D$  to be real, which defines the phase reference for all other complex quantities. The first nonlinear term in Eq. (1) can then be written as  $-\hbar \Lambda_2^{\mathrm{eff}}(t)b_Pb_S^\dagger b_S^\dagger +\mathrm{H.c.}$ , in which  $\Lambda_2^{\mathrm{eff}}(t)\equiv \Lambda \overline{\beta}_D e^{-i\omega Dt}$ . This coupling Hamiltonian is analogous to that of a degenerate spontaneous parametric down-conversion (SPDC)-like interaction driven by a time-dependent effective second-order nonlinearity with strength  $|\Lambda_2^{\mathrm{eff}}|$ , which here has a tunable magnitude determined by the resonator's intrinsic nonlinearity and the driving amplitude. The time dependence of this effective nonlinearity is contained entirely in its phase, which varies at an optical frequency and enables an effective theoretical picture to be

![](images/8c61fb883ac2e011a681b07e3ad2f45929c2820c38faae09806bb8c344cbec40.jpg)

![](images/9be85b106b37232d0aacb919d34a0eeaad575ca8c0cbd89982dc5164259c6723.jpg)  
FIG. 1. (a) A microring resonator side-coupled to a channel waveguide. (b) Tuning the resonance condition for parametric fluorescence via self- and cross-phase-modulation. (c) A virtual-level diagram for dual-pumped spontaneous four-wave mixing (SFWM); the strong cw drive beam mediates an effective second-order parametric nonlinearity  $\chi_2^{\mathrm{eff}}$ .

![](images/783d9a046f483f1894734f69ac66a249b431734eeb92583a1ae54ad639a0088e.jpg)

used in which a field in the  $P$  mode can drive parametric fluorescence into the  $S$  mode.

As illustrated in Fig. 1(c), in the presence of this effective second-order nonlinearity, a weaker coherent pump pulse in the  $P$  mode produces photon pairs via parametric fluorescence into the  $S$  mode. However, unlike SPDC, here  $2\omega_{S} \neq \omega_{P}$ , for part of the energy is supplied by the drive field (i.e.,  $2\omega_{S} = \omega_{P} + \omega_{D}$ ). This technique of using a strong cw pump in conjunction with the intrinsic  $\chi_{3}$  response to induce an effective time-dependent second-order interaction in an integrated microresonator has recently been implemented experimentally on a silicon-nitride nanophotonic platform in the context of strong nonlinear mode coupling, giving rise to effective second-order up-conversion with an extremely large conversion efficiency [39]. A similar dual-pump scheme on a nanophotonic platform has been used to drive optical parametric oscillation [43,44] and produce degenerate photon pairs [45,46].

The second nonlinear term in Eq. (1) corresponds to self-phase modulation (SPM) of each mode and the third to cross-phase-modulation (XPM) between the three modes of interest. For the regime under consideration, in which the  $D$  mode is driven by a strong cw beam, the  $P$  mode by a much weaker cw or pulsed field, and in which the  $S$  mode never accommodates a large mean photon number (i.e., well below any thresholds for parametric oscillation), we may neglect the effects of SPM and XPM due to photons in the  $P$  and  $S$  modes [41]. The effects of SPM and XPM

are then completely encapsulated by static shifts in the effective resonance frequencies  $\omega_{J}$  due to the large cw driving amplitude in the  $D$  mode. The resonator Hamiltonian (1) under these circumstances can thus be well represented by

$$
\begin{array}{l} H _ {\mathrm {r e s}} \rightarrow \sum_ {J} \hbar \omega_ {J} b _ {J} ^ {\dagger} b _ {J} - 2 \hbar \Lambda | \beta_ {P} (t) | ^ {2} b _ {S} ^ {\dagger} b _ {S} \\ - \hbar | \Lambda_ {2} ^ {\mathrm {e f f}} | \left(\beta_ {P} (t) b _ {S} ^ {\dagger} b _ {S} ^ {\dagger} + \mathrm {H . c .}\right) + H _ {X}, \tag {2} \\ \end{array}
$$

where  $\beta_{P}(t) = e^{-i(\omega_{D} + \omega_{P})t}\overline{\beta}_{P}(t)$ , with  $\overline{\beta}_P(t)$  the (slowly varying) envelope of the intraresonator pulse amplitude in the  $P$  mode, which we treat in the usual way as a classical coherent field and in which the resonant frequencies  $\omega_{J}$  are now understood to contain (drive-power-dependent) corrections from the XPM-induced red shift due to the strong driving field. Though, ultimately, we will confine ourselves to a regime in which the pump amplitude  $\beta_{P}(t)$  is sufficiently weak to have little effect on the  $S$  mode from XPM, here we have retained the corresponding term to verify that fact in our calculations.

For the desired process to be phase matched in the simple ring system shown in Fig. 1(a), the drive and pump resonances must be separated from the signal resonance by an equal number of mode orders; similarly, to maximize the efficiency of the process, the resonant frequencies of the three resonances must be close to evenly spaced. Absent any driving fields, material and modal dispersion in the resonator will give rise to a detuning  $\Delta_{\mathrm{res}} = \omega_P + \omega_D - 2\omega_S$  away from this condition. As the driving beam power is increased to "dress" the ring with an effective  $\chi_2(t)$ , each resonant mode will experience a red shift in frequency due to SPM and XPM (in addition to a global thermal shift that is nearly the same for all three modes and therefore may be neglected). Since the detuning  $\Delta_{\mathrm{XPM}}$  from XPM is twice as large as the detuning  $\Delta_{\mathrm{SPM}}$  from SPM, this effect can be used to counteract normal dispersion: for a particular drive power and dispersion, the net detuning  $\Delta_{\mathrm{net}} = \Delta_{\mathrm{res}} + \Delta_{\mathrm{SPM}} - \Delta_{\mathrm{XPM}} = \Delta_{\mathrm{res}} - \Delta_{\mathrm{SPM}}$  for the three modes can be reduced to zero, as illustrated in Fig. 1(b). Thus the driving power can be used to tune the three phase-matched resonances into an equally spaced frequency configuration.

A typical microresonator system accommodates many hundreds or even thousands of resonances. The term  $H_{X}$

in Eq. (2) contains the corresponding contributions to the Hamiltonian and their couplings to the three modes of interest. Below any thresholds for optical-parametric-oscillator (OPO) and comb generation and operating in a regime in which cascaded four-wave mixing is negligible, there are two dominant unwanted couplings relevant to the device performance. One gives rise to unwanted SFWM, leading to the generation of spurious photons in the  $S$  mode; another gives rise to Bragg-scattering four-wave mixing, leading to an additional source of loss on the squeezed state generated in the  $S$  mode [47,48]. Both of these processes should be suppressed to yield a pure low-noise squeezed output. This can be accomplished by designing the structure such that the auxiliary resonances involved in their dynamics are absent or sufficiently detuned; many strategies have been demonstrated to selectively suppress or control the position of these resonances [49,50]. More detail on these effects and strategies to eliminate them can be found in Appendix A.

# III. DYNAMICS AND MOMENTS

We now turn to calculating the properties of the squeezed output from the  $S$  mode for a system appropriately designed to suppress unwanted processes, following a cavity input-output formalism appropriate for microresonators [41]. We consider a single-channel system like that shown in Fig. 1(a), for which we introduce Heisenberg-picture input- and output-field operators  $\psi_{S,\mathrm{in}}(t)$  and  $\psi_{S,\mathrm{out}}(t)$ , as well as field operators  $\phi_{S,\mathrm{in}}(t)$  and  $\phi_{S,\mathrm{out}}(t)$  for the scattering modes that couple to the resonator modes due to the presence of loss. Here, all time-dependent quantities are understood to be slowly varying, i.e., their fast optical dependence at  $\omega_{S}$  has been removed; we also move into a rotating wave frame evolving as  $e^{-i(\Delta_{\mathrm{net}} / 2)t}$ , taking into account a possible net detuning of the three resonances from the ideal evenly spaced configuration. The equation of motion for the resonator-mode annihilation operator in this frame is then given by

$$
\frac {d}{d t} \binom {b _ {S} (t)} {b _ {S} ^ {\dagger} (t)} = M (t) \binom {b _ {S} (t)} {b _ {S} ^ {\dagger} (t)} + \mathbf {d} _ {\mathrm {i n}} (t), \tag {3}
$$

with the coupling matrix

$$
M (t) = - \bar {\Gamma} _ {S} I _ {2} + \left( \begin{array}{c c} i \left(\frac {\Delta_ {\mathrm {n e t}}}{2} + 2 \Lambda | \bar {\beta} _ {P} (t) | ^ {2}\right) & g (t) \\ g ^ {*} (t) & - i \left(\frac {\Delta_ {\mathrm {n e t}}}{2} + 2 \Lambda | \bar {\beta} _ {P} (t) | ^ {2}\right) \end{array} \right), \tag {4}
$$

in which  $I_{2}$  is the  $2 \times 2$  identity matrix, and input vacuum fluctuations

$$
\mathbf {d} _ {\text {i n}} (t) = \left( \begin{array}{c} - i \gamma_ {S} ^ {*} \psi_ {S, \text {i n}} (t) - i \mu_ {S} ^ {*} \phi_ {S, \text {i n}} (t) \\ i \gamma_ {S} \psi_ {S, \text {i n}} ^ {\dagger} (t) + i \mu_ {S} \phi_ {S, \text {i n}} ^ {\dagger} (t) \end{array} \right). \tag {5}
$$

Here, the function  $g(t) \equiv 2i\Lambda \overline{\beta}_D \overline{\beta}_P(t)$  describes the time-dependent nonlinearity in the resonator and  $\overline{\Gamma}_S = \Gamma_S + M_S$  is the total damping rate of the resonator  $S$  mode, to which both scattering loss [with associated rate  $M_S = |\mu_S|^2 / (2v_g)$ ] and the resonator-channel coupling [with associated rate  $\Gamma_S = |\gamma_S|^2 / (2v_g)$ ] contribute. These are related to the full loaded quality factor  $Q_S = \omega_S / (2\overline{\Gamma}_S)$  and the escape efficiency  $\eta_S^{\mathrm{esc}} = \Gamma_S / \overline{\Gamma}_S$ .

The output field in the channel is given by

$$
\psi_ {S, \text {o u t}} (t) = \psi_ {S, \text {i n}} (t) - i \left(\gamma_ {S} / v _ {g}\right) b _ {S} (t). \tag {6}
$$

Thus a solution for  $b_{S}(t)$  enables the calculation of all properties of the output. For the linearized dynamics of Eq. (3), it is straightforward to construct a Green function for the system response: a solution is given by

$$
\left(b _ {S} (t), b _ {S} ^ {\dagger} (t)\right) ^ {T} = \int_ {- \infty} ^ {t} d t ^ {\prime} G (t, t ^ {\prime}) \mathbf {d} _ {\mathrm {i n}} (t ^ {\prime}), \tag {7}
$$

where the  $2 \times 2$  matrix Green function  $G$  satisfies  $G(t, t) = I_2$  for all  $t$  and

$$
\frac {d G \left(t , t ^ {\prime}\right)}{d t} = M (t) G \left(t, t ^ {\prime}\right) \tag {8}
$$

for  $t > t'$ . This equation can be solved numerically; the properties of all system outputs can then be expressed in terms of the four components of  $G(t, t')$ . In addition to the static system parameters (quality factor, coupling ratios, etc.), the function  $g(t)$  also must be specified; this can be calculated by numerically integrating the associated nonlinear equation of motion for the pulsed mode, given by

$$
\frac {d \bar {\beta} _ {P} (t)}{d t} = (- \bar {\Gamma} _ {P} + i \Lambda | \bar {\beta} _ {P} (t) | ^ {2}) \bar {\beta} _ {P} (t) - i \gamma_ {P} ^ {*} \alpha_ {P, \mathrm {i n}} (t), \quad (9)
$$

where  $\alpha_{P,\mathrm{in}}$  is the input pump-pulse profile in the channel, normalized such that the energy in the pulse  $\mathcal{E}_P = \hbar \omega_P v_g \int_{-\infty}^{\infty} dt |\alpha_{P,\mathrm{in}}(t)|^2$ . With the drive-mode amplitude  $\overline{\beta}_D$  and the nonlinear strength  $\Lambda$ ,  $g(t)$  is determined; for a resonant drive beam  $\overline{\beta}_D = 2\sqrt{P_D Q_D \eta_D^{\mathrm{esc}} / (\hbar \omega_D^2)}$ , in which  $P_D$  is the input drive power in the channel,  $Q_D$  is the full loaded quality factor of the drive resonance, and  $\eta_D^{\mathrm{esc}}$  is the corresponding escape efficiency.

Since the dynamics of the system are linear in the mode operators, for a vacuum input in the  $S$  mode, the output must correspond to a Gaussian state with zero mean in all

quadratures. Thus all properties of the system output can be expressed in terms of the second-order moments

$$
N (t, t ^ {\prime}) = v _ {g} \left\langle \psi_ {S, \text {o u t}} ^ {\dagger} (t) \psi_ {S, \text {o u t}} (t ^ {\prime}) \right\rangle \tag {10}
$$

and

$$
M (t, t ^ {\prime}) = v _ {g} \langle \psi_ {S, \text {o u t}} (t) \psi_ {S, \text {o u t}} (t ^ {\prime}) \rangle . \tag {11}
$$

From these moments, we can extract all measurable quantities; full details are provided in Appendix B. For our purposes, we are primarily concerned with those aspects of the system output that are relevant for applications in CV quantum sampling: the efficiency (the degree of squeezing as a function of the drive and pump-pulse powers), the purity (limited by scattering losses), and the temporal-mode structure. The latter can be assessed by calculating the Schmidt number  $K$  of the output field, which quantifies the number of excited output modes and ideally equals unity for single-temporal-mode squeezed states. It is also important to assess the full complex temporal-mode shape of the generated squeezed light, to ensure that is benign (i.e., does not suffer from a complicated and erratic phase or envelope function) and consistent across a wide range of squeezing levels. This last point is crucial for CV quantum-sampling applications, for which squeezed states with different squeezing levels must interfere.

# IV. DEVICE ANALYSIS

We examine a system with realistic device parameters, well below the best-reported values, which are routinely achievable in modern silicon-nitride microring resonators [51]. We consider a device optimized for a cw drive input power of  $200\mathrm{mW}$  at the phase-matching point that yields  $\Delta_{\mathrm{net}} = 0$  and we include the effects of time-dependent self-phase modulation and cross-phase-modulation from the pump pulse. In Fig. 2(a), we show the squeezing performance for a structure with a  $400 - \mu \mathrm{m}$  round-trip length,  $\omega_{S} = 2\pi \times 193\mathrm{THz}$ , a nonlinear parameter  $\gamma_{\mathrm{NL}} = 1(\mathrm{Wm})^{-1}$ , a group velocity  $v_{g} = c / 1.7$ , and an intrinsic quality factor of  $2\times 10^{6}$  for all three resonances, with escape efficiencies of 0.5 (critically coupled) for the drive mode  $D$ , 0.9 for the  $S$  mode, and 0.98 for the pump mode  $P$ ; the corresponding loaded quality factors are then  $1\times 10^{6}$ ,  $2\times 10^{5}$ , and  $4\times 10^{4}$ , respectively. The sequence coupling ratios are chosen to maximize the circulating power in the  $D$  mode, to ensure good escape efficiency for the generated photons in the  $S$  mode, and to allow large-bandwidth pulses into the  $P$  mode, which are necessary to achieve a low Schmidt number [52,53]. Independent control over the escape efficiencies can be realized by suitable coupler design [54]. We note that the maximum operating repetition rate is limited by the  $S-$  and  $P$ -mode inverse dwelling times. For the device that we consider here, the  $S$  mode has

![](images/d7820cc26859d32617ccafb152333f9165e2bd58065fc0f2114a9f7590d629a5.jpg)

![](images/00f717002c467dc5a9f000aa0aa531fefad46b8727b2f06e88bfd284df435f27.jpg)  
FIG. 2. The system performance for a device with realistic parameters (details in text). (a) The variance relative to vacuum of the squeezed quadrature (bottom solid curve) and the antisqueezed quadrature (top solid curve) for the dominant mode. The dashed curve shows the variance of the antisqueezed quadrature for an ideal pure state; some excess antisqueezing is evident from the finite escape efficiency. (b) The mean photon number of the first ten Schmidt modes as a function of the pulse energy; the dominant mode (top curve) consistently lies about  $100 \times$  above the next-largest mode. (c) The intensity (virtually identical solid curves) and phase (dashed curves) of the temporal-mode profile for the squeezed pulses generated for five pulse energies spanning  $1 - 100\mathrm{pJ}$ . The intensity profile is virtually unchanged across this range; the phases show only very small progressive deviations due to cross-phase-modulation from the pulsed pump as the energy is increased. (d) The Schmidt number is consistently close to unity across a wide range of pump-pulse energies and squeezing levels. (e) The fidelity between the dominant complex temporal-mode profile at varying pulse energies and that at the lowest pulse energy. Only very slight degradation of this fidelity is predicted, primarily due to the slight phase variations shown in (c). More details of how these quantities are extracted from the output moments can be found in Appendix B.

![](images/0012c716d54e3136763b4dba032f02de731e3a5049b71db986e3d3e180bd5dcc.jpg)

![](images/eae862b44d4ccc9379f6cbaa95d8a35d3626dba15d9e81af8478bc37baf65cec.jpg)

![](images/145f60b61d5550ceffe93fd432dffbe430565c399d7e0812269c7027051aeff8.jpg)

the longer dwelling time of  $\overline{\Gamma}_S^{-1} \approx 300$  ps, enabling pump repetition rates in the  $100\mathrm{MHz}$  range to be used while allowing ample time for the fields to ring down between pulses.

The fundamental limit to squeezing attainable in this system is set by the  $S$ -mode escape efficiency, which in this case limits the output to  $-10\log (1 - \eta_S^{\mathrm{esc}}) = 10$  dB of squeezing. As is evident from Fig. 2(a), the system can readily approach loss-limited performance, with nearly  $10~\mathrm{dB}$  of squeezing realized for a Gaussian pump pulse having energy  $100\mathrm{pJ}$  and an intensity full-width-at-half-maximum duration set to one tenth of the  $S$ -mode dwelling time. This level of squeezing is precisely the desired operational point for many CV quantum-sampling protocols, which typically call for squeezed states with about  $8\mathrm{dB}$  of squeezing at the input, corresponding to a mean photon number before losses of about one [13]. As is the case with any realistic squeezed-light source, the losses (i.e., the finite escape efficiency) of our device necessitate an output with a higher mean photon number for a fixed level of squeezing; this is reflected by the commensurately higher mean photon number in the dominant temporal mode of the device output [see Fig. 2(b)]. Furthermore, as shown in Fig. 2(c), the system produces clean single-temporal-mode squeezed pulses of roughly 1-ns duration, with negligible variation in their pulse profiles across a wide tuning range of squeezing levels. The Schmidt number and the fidelity of the generated temporal mode at high input energies with that at low input energies both remain

very close to unity [Figs. 2(d) and 2(e)]. The purity  $p = (V_{\max} V_{\min})^{-1/2}$  [55]—where  $V_{\max}$  and  $V_{\min}$  the maximal and minimal quadrature variances—of the generated Gaussian state for a fixed desired squeezing level is determined entirely by the escape efficiency. The behavior of the purity as a function of target squeezing is plotted in Fig. 3 for a device with  $\eta_S^{\mathrm{esc}} = 0.9$ ; this behavior would be identical for any resonator-based parametric squeezed-light source with the same escape efficiency. We note that, as demonstrated experimentally by Cernansky et al. [30], the singly

![](images/9345fbb221c36f15f8be8d2a986f6e2949288c9782c42cbc71ef2e5fb55e3e87.jpg)  
FIG. 3. The purity of the generated Gaussian state as a function of the target squeezing level for a device with  $90\%$  escape efficiency.

resonant microresonator squeezeer design proposed by Hoff et al. [27] suffers from strong nonparametrically generated noise contributions and therefore generates states with much lower purity than those from our proposed device.

As for most resonator-based parametric squeezed-light sources, the purity for our proposed device is limited by losses, which are quantified by the resonator escape efficiency. The impact of subunity purity depends very strongly on the application. For example, squeezing-enhanced gravitational wave detectors [33] require low levels of excess antisqueezing and therefore high purity since the finite phase precision of such devices mixes noise from the antisqueezed quadrature into the measured quadrature and limits the effective quantum enhancement available [56]. On the other hand, high-fidelity CV teleportation experiments (for which very high phase precision can be achieved) can tolerate lower purity, provided that the level of squeezing remains high, since it is the variance of the squeezed quadrature that determines the teleportation fidelity. The role of state purity in applications that can be realized with Gaussian boson sampling is an open question. It has been studied recently [57] in the context of the classical simulability of such a machine in asymptotic limits where the system losses grow with the system size, as would be the case for lossy linear optical networks into which squeezing is injected. However, no analysis is available that definitively addresses how subunity state purity would affect an actual device of fixed size, designed to target a specific application of CV quantum sampling. Nevertheless, since in all cases losses degrade the degree of quantum correlations and coherence available in such a system and since losses are a critical factor in the closely related context of conventional (single-photon-based) boson sampling [58], we expect state purity to be an important metric with which proposed squeezed-light sources should be assessed. Since high escape efficiencies can readily be achieved in integrated microresonators, in this metric our device should compare well with existing nonintegrated approaches, such as bulk  $\chi_{2}$  OPOs.

For applications requiring very high squeezing levels, such as CV teleportation and cluster-state-based CV quantum computation [20,59], we note that existing ultralow-loss platforms [60] in principle permit the signal resonance escape efficiency to be further optimized while maintaining an acceptable generation efficiency. For our system modified to yield intrinsic quality factors of  $10^{7}$  with  $\eta_{D}^{\mathrm{esc}} = 0.5$ ,  $\eta_{S}^{\mathrm{esc}} = 0.99$ ,  $\eta_{P}^{\mathrm{esc}} = 0.999$ , thereby lowering the effective losses while maintaining respective high loaded quality factors of  $5\times 10^{6}$ ,  $1\times 10^{5}$ , and  $1\times 10^{4}$  and so retaining comparable generation efficiency, it would be possible to realize  $15~\mathrm{dB}$  of squeezing with only a few decibels of excess antisqueezing arising from the subunity escape efficiency. This level of squeezing is comparable to the current experimentally demonstrated record [7].

The engineering of such highly overcoupled resonators is very challenging, but we use this example to highlight how already-demonstrated material parameters and corresponding intrinsic quality factors open such possibilities for extremely high-performance sources. Furthermore, very recently [61], the threshold squeezing required for fault-tolerant CV cluster-state-based quantum computation has been shown to be less than  $10\mathrm{dB}$ ; a device with a more manageable signal-mode escape efficiency of  $\eta_S^{\mathrm{esc}} = 0.9$  as considered in detail in this section, could readily provide this.

To compare the performance of our device with that of Hoff et al. [27], we note that both systems operate using the same underlying material nonlinearity and resonator structure and therefore exhibit similar generation efficiency performance as a function of the pump power, quality factors, and coupling ratios. However, even setting aside the excess noise issues and the presence of a bright copropagating pump that affect the device of Hoff et al. [27], we emphasize that attaining single-temporal-mode operation using a single pulsed pump would be very difficult. The crucial feature in our scheme that allows single-mode squeezed light to be generated in a consistent temporal mode across a wide tuning range is the use of a strong cw drive beam in conjunction with a weak pulsed pump. This avoids time-dependent XPM effects on the squeezed mode, which strongly affect the temporal-mode structure of the generated light. In addition, the use of a single resonance for the pump and squeezed light, as proposed by Hoff et al. [27], prevents the independent engineering of the quality factors that is required for the pulsed-pump resonance to admit pulses with bandwidths exceeding that of the signal-mode resonance.

# V. CONCLUSION

We introduce an integrated nanophotonic device, compatible with current available fabrication technology, and demonstrate that it is capable of producing squeezed light satisfying the strict requirements of CV quantum computation and simulation tasks. We present a strategy for device design and pumping that allows substantial squeezing at modest input powers in a single spatiotemporal mode, the properties of which do not significantly vary as the squeezing level is tuned. This solves a number of key issues hindering progress in CV quantum technology and especially in quantum sampling. We therefore expect our strategy to be of considerable utility for a wide range of CV quantum information processing applications.

# ACKNOWLEDGMENTS

We acknowledge support from the Ontario Centres of Excellence and the Natural Sciences and Engineering Research Council.

# APPENDIX A: UNWANTED NONLINEAR EFFECTS

A typical microresonator system accommodates many hundreds or even thousands of resonances. The term  $H_{X}$  in Eq. (1) of the main text contains the corresponding contributions to the Hamiltonian of these resonances and of their couplings to the three modes of interest. Below any thresholds for OPO and comb generation and operating in a regime where cascaded four-wave mixing is negligible, there are two dominant unwanted couplings relevant to the device performance: those that give rise to unwanted SFWM, leading to the generation of spurious photons in the  $S$  mode [41], and those that give rise to Bragg-scattering four-wave mixing (BS-FWM), leading to an additional source of loss on the squeezed state generated in the  $S$  mode [47]. These effects arise from terms of the form  $b_{D}b_{D}b_{S}^{\dagger}b_{X1}^{\dagger}$  and  $b_{P}b_{P}b_{S}^{\dagger}b_{X2}^{\dagger}$  (unwanted SFWM) and  $b_{D}b_{P}^{\dagger}b_{S}b_{X1}^{\dagger}$  and  $b_{D}^{\dagger}b_{P}b_{S}b_{X2}^{\dagger}$  (unwanted BS-FWM), where  $b_{X1}$  and  $b_{X2}$  are annihilation operators for unwanted modes  $X1$  and  $X2$ .

Such processes effectively entangle the  $X1$  and  $X2$  modes with the  $S$  mode, corrupting the purity of the  $S$ -mode output state. Though both normal dispersion and the effects of SPM or XPM from the strong drive act to counteract this effect by increasing the corresponding net detuning for these processes, in general, for simple single-resonator devices with realistic parameters, this is not sufficient to suppress the unwanted processes to a level appropriate for CV quantum sampling, in which highly pure Gaussian states are desirable.

To see this, we first estimate the strength of the SFWM process associated with the generation of photons at  $\omega_{S}$  and  $\omega_{X2}$ . Similar considerations apply for the pump field and pair generation at  $\omega_{S}$  and  $\omega_{X1}$ . However, the noise arising from the driving field is expected to be several orders of magnitude larger, since SFWM scales quadratically with the power of the generating field.

The intensity of SFWM involving the modes at  $\omega_{X2}$ ,  $\omega_{S}$ , and  $\omega_{D}$  depends on the relative position of the corresponding resonances. In this case, SPM and XPM lead to a relative detuning:

$$
\delta = \left(\omega_ {D} - \omega_ {X _ {2}}\right) - \left(\omega_ {S} - \omega_ {D}\right) = - \frac {3 c}{\omega_ {D} n _ {\text {e f f}}} \gamma_ {\mathrm {N L}} \frac {v _ {g} Q}{2 \pi R} P _ {D}, \tag {A1}
$$

where  $n_{\mathrm{eff}}$  is the mode effective index,  $\gamma_{\mathrm{NL}}$  is the waveguide nonlinear parameter, and  $P_D$  is the input power at  $\omega_D$ . Finally,  $v_g$  is the group velocity,  $Q$  is the resonator quality factor, and  $R$  is the ring radius.

In the presence of a detuning  $\delta$  and in the limit of a small pair generation rate, the average number of generated pairs is reduced according to

$$
| \beta_ {\delta} | ^ {2} = | \beta_ {0} | ^ {2} \frac {\Delta^ {2}}{\delta^ {2} + \Delta^ {2}},
$$

where  $|\beta_0|^2$  is the average number of pairs in the case of equally spaced resonances (i.e.,  $\delta = 0$ ) and  $\Delta$  is the resonance line width, which for simplicity we assume to be the same for all the three resonances involved in the process.

Considering only the noise contribution coming from unwanted SFWM, the signal-to-noise ratio  $(R_{\mathrm{SN}})$  can be defined as

$$
R _ {\mathrm {S N}} = \frac {| \beta_ {\mathrm {S}} | ^ {2}}{| \beta_ {\mathrm {S} , \mathrm {X} _ {2}} | ^ {2}},
$$

where  $|\beta_{\mathrm{S}}|^2$  and  $|\beta_{\mathrm{S,X_2}}|^2$  are the average number of pairs generated in the signal mode and by the unwanted SFWM associated with the driving field, respectively. This leads to

$$
R _ {\mathrm {S N}} = \frac {\left| \beta_ {\mathrm {S}} \right| ^ {2}}{\left| \beta_ {\mathrm {S} , \mathrm {X} _ {2}} \right| ^ {2}} \approx \frac {P _ {P}}{P _ {D}} \left(1 + \frac {\delta^ {2}}{\Delta^ {2}}\right), \tag {A2}
$$

where  $P_{P}$  is the pump-field power. As expected, in the absence of detuning, i.e., when all the resonances at  $\omega_{X_2}$ ,  $\omega_{D}$ ,  $\omega_{S}$ , and  $\omega_{P}$  are equally spaced, the  $R_{\mathrm{SN}}$  would be essentially proportional to  $P_{P} / P_{D}$ . However, due to the presence of SPM or XPM, the unwanted SFWM process is suppressed by the detuning. We can rewrite Eq. (A2) by explicitly taking into account the dependence on the structure parameters using Eq. (A1):

$$
R _ {\mathrm {S N}} \approx \frac {P _ {P}}{P _ {D}} \left(1 + \xi^ {2} \frac {Q ^ {4}}{R ^ {2}} P _ {D} ^ {2}\right), \tag {A3}
$$

where

$$
\xi = \frac {3 c ^ {2} \gamma_ {\mathrm {N L}}}{2 \pi \omega^ {2} n _ {\mathrm {e f f}} n _ {\mathrm {g}}} \tag {A4}
$$

is a constant that depends on the nonlinearity and dispersion of the waveguide.

In the case of SiN ring resonators, one can take  $\xi = 10^{-14}\mathrm{mW}^{-1}$ ,  $Q = 10^{6}$ ,  $R = 10^{-4}$  m,  $P_{D} = 2\times 10^{-1}W$ , and  $P_{P} = 10^{-3}W$ , which leads to

$$
R _ {\mathrm {S N}} \approx 2.
$$

This value suggests that, in general, the resonance detuning determined by SPM or XPM is not sufficient to neglect the effect of unwanted pairs generated by the driving field via degenerate SFWM.

Care must therefore be taken to further corrupt the efficiency of the unwanted process, either by detuning or removing altogether the associated resonances  $X1$  and  $X2$ . Many strategies exist to accomplish this without significantly compromising other aspects of device performance: one particularly promising possibility is to couple to the primary resonator two auxiliary resonators with different free spectral ranges, which can be used to selectively split and severely detune the  $X1$  and  $X2$  resonances from their

default frequencies [49]. Another strategy involves using a Mach-Zehnder interferometer-based coupler to independently modify the quality factors of the resonances; the efficiency of processes involving the unwanted  $X1$  and  $X2$  modes can be strongly degraded by reducing their associated quality factors. Alternatively, if a more sophisticated coupled resonator system is used to obviate the need for strong dispersion and the associated free spectral ranges are chosen to be incommensurate, the unwanted resonances will be absent, strongly suppressing unwanted four-wave mixing effects.

# APPENDIX B:TEMPORAL-MODE DECOMPOSITION

In this appendix, we analyze how, from the second-order moments of the channel fields, one can obtain the quantum state of systems that produce Gaussian states of zero mean in all quadratures and calculate any measurable quantity related to the device output. We start by noting that the intraresonator dynamics are linear in the quantum operators within our assumptions and thus, since the initial quantum state is vacuum, the state is at all times Gaussian [62], i.e., it is described by a mean displacement

$$
\langle \psi_ {S, \text {o u t}} (t) \rangle , \tag {B1}
$$

and the two-point correlation functions

$$
N (t, t ^ {\prime}) = v _ {S} \left\langle \psi_ {S, \text {o u t}} ^ {\dagger} (t) \psi_ {S, \text {o u t}} \left(t ^ {\prime}\right) \right\rangle , \tag {B2}
$$

$$
M \left(t, t ^ {\prime}\right) = v _ {S} \left\langle \psi_ {S, \text {o u t}} (t) \psi_ {S, \text {o u t}} \left(t ^ {\prime}\right) \right\rangle . \tag {B3}
$$

For our system, we can always guarantee that  $\langle \psi_{S,\mathrm{out}}(t)\rangle = 0$  and thus for the rest of this appendix we focus on  $M(t,t^{\prime})$  and  $N(t,t^{\prime})$ . Furthermore, note that  $N$  is Hermitian and  $M$  is symmetric:

$$
N \left(t, t ^ {\prime}\right) = N \left(t ^ {\prime}, t\right) ^ {*} \quad \text {a n d} \quad M \left(t, t ^ {\prime}\right) = M \left(t ^ {\prime}, t\right). \tag {B4}
$$

In the absence of intrinsic losses, i.e., assuming that any photon created inside the resonator can only leak into the waveguide at rate  $\Gamma_{S}$ , we know that the quantum state of the waveguide is pure once the resonator-mode populations have decayed. If this were not the case, there would be some entanglement between the mode  $S$  in the resonator and the mode  $S$  in the waveguide and thus the resonator could not be in the vacuum state. Knowing this, we can use Williamson's theorem and the Bloch-Messiah decomposition [62] to write a joint decomposition of the second-order moments,

$$
N (t, t ^ {\prime}; \Gamma_ {S}) _ {\text {p u r e}} = \sum_ {\lambda} \sinh \left(r _ {\lambda}\right) ^ {2} f _ {\lambda} (t) f _ {\lambda} ^ {*} \left(t ^ {\prime}\right), \tag {B5}
$$

$$
M \left(t, t ^ {\prime}; \Gamma_ {S}\right) _ {\text {p u r e}} = \sum_ {\lambda} \frac {\sinh \left(2 r _ {\lambda}\right)}{2} f _ {\lambda} ^ {*} (t) f _ {\lambda} ^ {*} \left(t ^ {\prime}\right), \tag {B6}
$$

where the set of functions  $f_{\lambda}(t)$  are orthonormal and complete:

$$
\int d t f _ {\lambda} (t) f _ {\lambda^ {\prime}} ^ {*} (t) = \delta_ {\lambda , \lambda^ {\prime}}, \tag {B7}
$$

$$
\sum_ {\lambda} f _ {\lambda} (t) f _ {\lambda} ^ {*} \left(t ^ {\prime}\right) = \delta \left(t - t ^ {\prime}\right). \tag {B8}
$$

We use the subscript "pure" to indicate that these moments come from a pure state and we explicitly write the dependence on the overall decay rate  $\Gamma_{S}$  into the waveguide. For pure states, there is a certain degree of redundancy, since if one has just the  $N$  moment, one can obtain the set  $\{f_{\lambda}(t)\}$  and the mean photon numbers  $\sinh^2 (r_\lambda)$  via a simple eigendecomposition. Alternatively, if one has the  $M$  moment, one can obtain the set  $\{f_{\lambda}(t)\}$  and the quantities  $\sinh (2r_{\lambda}) / 2$  via a Takagi-Autonne decomposition [63]. For our purposes, we use the eigendecomposition of  $N$  but also verify consistency using the Takagi-Autonne decomposition, as implemented in STRAWBERRY FIELDS [64]. Note that, in practice, one knows the correlators on a grid of points and then for a sufficiently dense grid estimates the decompositions in Eq. (B5) (cf. Appendix B of Ref. [65]). Having the functions  $f_{\lambda}(t)$  and the coefficients  $r_{\lambda}$ , one can write the ket describing the state of the electromagnetic field of the waveguide as

$$
| \Psi \rangle = \bigotimes_ {\lambda} S \left(r _ {\lambda}, A _ {\lambda}\right) | \text {v a c} \rangle , \tag {B9}
$$

$$
S \left(r _ {\lambda}, A _ {\lambda}\right) = \exp \left(\frac {r _ {\lambda}}{2} \left[ A _ {\lambda} ^ {2} - A _ {\lambda} ^ {\dagger 2} \right]\right), \tag {B10}
$$

$$
A _ {\lambda} = \int d t \psi_ {S, \text {o u t}} (t) f _ {\lambda} ^ {*} (t). \tag {B11}
$$

Now let us consider the case in which photons from the ring can be scattered into modes different from the ones in the waveguide, e.g., scattering modes that contribute to loss of photons from the resonator. The treatment of such losses into an undesired channel has been dealt with by, e.g., Vernon and Sipe [41]. The system is now described by several decay rates:  $\Gamma_{S}$ , the decay rate into the waveguide;  $M_S$ , the scattering loss decay rate; and  $\overline{\Gamma}_S = \Gamma_S + M_S$ , the total decay rate. For our correlation functions, it is easily seen that in the case of loss, the moments associated with this mixed state are related to the moments of a pure state as in Eq. (B5), where all the photons go into a fictitious waveguide (with modes corresponding to the physical channel and the bundle of scattering modes) at

rate  $\overline{\Gamma}_S$  , by

$$
N _ {\text {m i x e d}} (t, t ^ {\prime}) = \eta_ {S} ^ {\mathrm {e s c}} N _ {\text {p u r e}} (t, t ^ {\prime}; \bar {\Gamma} _ {S}), \tag {B12}
$$

$$
M _ {\text {m i x e d}} (t, t ^ {\prime}) = \eta_ {S} ^ {\text {e s c}} M _ {\text {p u r e}} (t, t ^ {\prime}; \bar {\Gamma} _ {S}), \tag {B13}
$$

where  $\eta_S^{\mathrm{esc}} = \Gamma_S / \overline{\Gamma}_S$  is the escape efficiency into the waveguide channel, i.e., the ratio of the decay rate into the physical waveguide to the overall decay rate into all channels (including the waveguide). If there is only decay into the waveguide, we have  $\eta_{\mathrm{esc}} = 1$ ,  $\Gamma_S = \overline{\Gamma}_S$  and recover the pure-state case discussed previously.

The moments in Eq. (B12) are also the moments characterizing the state  $|\Psi \rangle$  after being sent through a loss channel where the (energy) transmission is precisely  $\eta_S^{\mathrm{esc}}$ . Note that a squeezed state with squeezing parameter  $r$  subjected to loss by transmission amount  $\eta$  has the same density matrix as a thermal state with mean photon number

$$
\bar {n} = \frac {1}{2} \sqrt {\cosh^ {2} (r) - (1 - 2 \eta) ^ {2} \sinh^ {2} (r)} - \frac {1}{2}, \tag {B14}
$$

and then squeezed by the amount [66]

$$
r ^ {\prime} = \frac {1}{4} \log \left(\frac {\eta e ^ {2 r} + 1 - \eta}{\eta e ^ {- 2 r} + 1 - \eta}\right). \tag {B15}
$$

Using this equivalence, we write the density matrix of the state when scattering into unmeasured modes is present as

$$
\rho = \bigotimes_ {\lambda} S \left(r _ {\lambda} ^ {\prime}, A _ {\lambda}\right) \left\{\rho_ {\lambda} \left(\bar {n} _ {\lambda}\right) \right\} S ^ {\dagger} \left(r _ {\lambda} ^ {\prime}, A _ {\lambda}\right), \tag {B16}
$$

where  $\rho_{\lambda}$  is a thermal state in the mode with temporal profile  $\lambda$  and with mean occupation number  $\bar{n}_{\lambda}$  given by Eq. (B14) with  $\eta = \eta_{\mathrm{esc}}$  and  $r = r_{\lambda}$ . Likewise,  $r_{\lambda}^{\prime}$  is given in Eq. (B15) with the same substitutions.

[1] S. L. Braunstein and P. Van Loock, Quantum information with continuous variables, Rev. Mod. Phys. 77, 513 (2005).  
[2] R. Slusher, L. Hollberg, B. Yurke, J. Mertz, and J. Valley, Observation of Squeezed States Generated by Four-Wave Mixing in an Optical Cavity, Phys. Rev. Lett. 55, 2409 (1985).  
[3] R. Shelby, M. Levenson, S. Perlmutter, R. DeVoe, and D. Walls, Broad-Band Parametric Deamplification of Quantum Noise in an Optical Fiber, Phys. Rev. Lett. 57, 691 (1986).  
[4] U. L. Andersen, T. Gehring, C. Marquardt, and G. Leuchs, 30 years of squeezed light generation, Phys. Scr. 91, 053001 (2016).  
[5] L.-A. Wu, H. Kimble, J. Hall, and H. Wu, Generation of Squeezed States by Parametric Down Conversion, Phys. Rev. Lett. 57, 2520 (1986).

[6] C. Silberhorn, P. K. Lam, O. Weiss, F. König, N. Korolkova, and G. Leuchs, Generation of Continuous Variable Einstein-Podolsky-Rosen Entanglement via the Kerr Nonlinearity in an Optical Fiber, Phys. Rev. Lett. 86, 4267 (2001).  
[7] H. Vahlbruch, M. Mehmet, K. Danzmann, and R. Schnabel, Detection of 15 dB Squeezed States of Light and Their Application for the Absolute Calibration of Photoelectric Quantum Efficiency, Phys. Rev. Lett. 117, 110801 (2016).  
[8] K. McKenzie, N. Grosse, W. P. Bowen, S. E. Whitcomb, M. B. Gray, D. E. McClelland, and P. K. Lam, Squeezing in the Audio Gravitational-Wave Detection Band, Phys. Rev. Lett. 93, 161105 (2004).  
[9] G. Harder, T. J. Bartley, A. E. Lita, S. W. Nam, T. Gerrits, and C. Silberhorn, Single-Mode Parametric-Down-Conversion States with 50 Photons as a Source for Mesoscopic Quantum Optics, Phys. Rev. Lett. 116, 143601 (2016).  
[10] C. M. Caves, Quantum-mechanical noise in an interferometer, Phys. Rev. D 23, 1693 (1981).  
[11] S. Lloyd and S. L. Braunstein, Quantum Computation over Continuous Variables, Phys. Rev. Lett. 82, 1784 (1999).  
[12] J. Huh, G. G. Guerreschi, B. Peropadre, J. R. McClean, and A. Aspuru-Guzik, Boson sampling for molecular vibronic spectra, Nat. Photonics 9, 615 (2015).  
[13] C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, and I. Jex, Gaussian Boson Sampling, Phys. Rev. Lett. 119, 170501 (2017).  
[14] J. M. Arrazola and T. R. Bromley, Using Gaussian Boson Sampling to Find Dense Subgraphs, Phys. Rev. Lett. 121, 030503 (2018).  
[15] K. Brádler, P.-L. Dallaire-Demers, P. Rebentrost, D. Su, and C. Weedbrook, Gaussian boson sampling for perfect matchings of arbitrary graphs, Phys. Rev. A 98, 032310 (2018).  
[16] M. Schuld, K. Brádler, R. Israel, D. Su, and B. Gupt, A quantum hardware-induced graph kernel based on Gaussian boson sampling, arXiv:1905.12646 (2019).  
[17] L. Banchi, M. Fingerhuth, T. Babej, and J. M. Arrazola, Molecular docking with Gaussian boson sampling, arXiv:1902.00462 (2019).  
[18] A. E. Lita, A. J. Miller, and S. W. Nam, Counting near-infrared single-photon with  $95\%$  efficiency, Opt. Express 16, 3032 (2008).  
[19] T. Gerrits, N. Thomas-Peter, J. C. Gates, A. E. Lita, B. J. Metcalf, B. Calkins, N. A. Tomlin, A. E. Fox, A. L. Linares, J. B. Spring, N. K. Langford, R. P. Mirin, P. G. R. Smith, I. A. Walmsley, and S. W. Nam, On-chip, photon-number-resolving, telecommunication-band detectors for scalable photonic information processing, Phys. Rev. A 84, 060301 (2011).  
[20] N. C. Menicucci, Fault-Tolerant Measurement-Based Quantum Computing with Continuous-Variable Cluster States, Phys. Rev. Lett. 112, 120504 (2014).  
[21] F. Marsili, V. B. Verma, J. A. Stern, S. Harrington, A. E. Lita, T. Gerrits, I. Vayshenker, B. Baek, M. D. Shaw, R. P. Mirin, and S. W. Nam, Detecting single infrared photons with  $93\%$  system efficiency, Nat. Photonics 7, 210 (2013).  
[22] W. R. Clements, J. J. Renema, A. Eckstein, A. A. Valido, A. Lita, T. Gerrits, S. W. Nam, W. S. Kolthammer, J. Huh, and I. A. Walmsley, Approximating vibronic spectroscopy

with imperfect quantum optics, J. Phys. B: At., Mol. Opt. Phys. 51, 245503 (2018).  
[23] F. Lenzini, J. Janousek, O. Thearle, M. Villa, B. Haylock, S. Kasture, L. Cui, H.-P. Phan, D. V. Dao, H. Yonezawa, P. K. Lam, E. H. Huntington, and M. Lobino, Integrated photonic platform for quantum information with continuous variables, Sci. Adv. 4, eaat9331 (2018).  
[24] F. Kaiser, B. Fedrici, A. Zavatta, V. D'Auria, and S. Tanzilli, A fully guided-wave squeezing experiment for fiber quantum networks, Optica 3, 362 (2016).  
[25] A. Dutt, K. Luke, S. Manipatruni, A. L. Gaeta, P. Nussenzweig, and M. Lipson, On-Chip Optical Squeezing, Phys. Rev. Appl. 3, 044005 (2015).  
[26] A. Dutt, S. Miller, K. Luke, J. Cardenas, A. L. Gaeta, P. Nussenzveig, and M. Lipson, Tunable squeezing using coupled ring resonators on a silicon nitride chip, Opt. Lett. 41, 223 (2016).  
[27] U. B. Hoff, B. M. Nielsen, and U. L. Andersen, Integrated source of broadband quadrature squeezed light, Opt. Express 23, 12013 (2015).  
[28] N. Le Thomas, A. Dhakal, A. Raza, F. Peyskens, and R. Baets, Impact of fundamental thermodynamic fluctuations on light propagating in photonic waveguides made of amorphous materials, Optica 5, 328 (2018).  
[29] G. Huang, E. Lucas, J. Liu, A. S. Raja, G. Lihachev, M. L. Gorodetsky, N. J. Engelsen, and T. J. Kippenberg, Thermorefractive noise in silicon-nitride microresonators, Phys. Rev. A 99, 061801 (2019).  
[30] R. Cernansky and A. Politi, Nanophotonic source of broadband quadrature squeezing, arXiv:1904.07283 (2019).  
[31] V. Vaidya, B. Morrison, L. Helt, R. Shahrokhshahi, D. Mahler, M. Collins, K. Tan, J. Lavoie, A. Repingon, M. Menotti, N. Quesada, R. C. Pooser, A. E. Lita, T. Gerrits, S. W. Nam, and Z. Vernon, Broadband quadrature-squeezed vacuum and nonclassical photon number correlations from a nanophotonic device, arXiv:1904.07833 (2019).  
[32] H. Yonezawa, D. Nakane, T. A. Wheatley, K. Iwasawa, S. Takeda, H. Arao, K. Ohki, K. Tsumura, D. W. Berry, T. C. Ralph, H. M. Wiseman, E. H. Huntington, and A. Furusawa, Quantum-enhanced optical-phase tracking, Science 337, 1514 (2012).  
[33] LIGO Scientific Collaboration, Enhanced sensitivity of the LIGO gravitational wave detector by using squeezed states of light, Nat. Photonics 7, 613 (2013).  
[34] X. Qiang, X. Zhou, J. Wang, C. M. Wilkes, T. Loke, S. O'Gara, L. Kling, G. D. Marshall, R. Santagati, T. C. Ralph, J. B. Wang, J. L. O'Brien, M. G. Thompson, and J. C. F. Matthews, Large-scale silicon quantum photonics implementing arbitrary two-qubit processing, Nat. Photonics 12, 534 (2018).  
[35] N. C. Harris, G. R. Steinbrecher, M. Prabhu, Y. Lahini, J. Mower, D. Bunandar, C. Chen, F. N. Wong, T. Baehr-Jones, M. Hochberg, S. Lloyd, and D. Englund, Quantum transport simulations in a programmable nanophotonic processor, Nat. Photonics 11, 447 (2017).  
[36] J. W. Silverstone, D. Bonneau, J. L. O'Brien, and M. G. Thompson, Silicon quantum photonics, IEEE J. Sel. Top. Quantum Electron. 22, 390 (2016).  
[37] T. Rudolph, Why I am optimistic about the silicon-photonic route to quantum computing, APL Photonics 2, 030901 (2017).

[38] N. K. Langford, S. Ramelow, R. Prevedel, W. J. Munro, G. J. Milburn, and A. Zeilinger, Efficient quantum computing using coherent photon conversion, Nature 478, 360 (2011).  
[39] S. Ramelow, A. Farsi, Z. Vernon, S. Clemmen, X. Ji, J. Sipe, M. Liscidini, M. Lipson, and A. L. Gaeta, Strong Nonlinear Coupling in a  $\mathrm{Si}_3\mathrm{N}_4$  Ring Resonator, Phys. Rev. Lett. 122, 153906 (2019).  
[40] R. S. Bondurant, P. Kumar, J. H. Shapiro, and M. Maeda, Degenerate four-wave mixing as a possible source of squeezed-state light, Phys. Rev. A 30, 343 (1984).  
[41] Z. Vernon and J. Sipe, Spontaneous four-wave mixing in lossy microring resonators, Phys. Rev. A 91, 053802 (2015).  
[42] N. Quesada and J. Sipe, Time-Ordering Effects in the Generation of Entangled Photons Using Nonlinear Optical Processes, Phys. Rev. Lett. 114, 093903 (2015).  
[43] Y. Okawachi, M. Yu, K. Luke, D. O. Carvalho, S. Ramelow, A. Farsi, M. Lipson, and A. L. Gaeta, Dual-pumped degenerate Kerr oscillator in a silicon nitride microresonator, Opt. Lett. 40, 5267 (2015).  
[44] C. Reimer, M. Kues, L. Caspani, B. Wetzel, P. Roztocki, M. Clerici, Y. Vestin, M. Ferrera, M. Peccianti, A. Pasquazi, B. E. Little, S. T. Chu, D. J. Moss, and R. Morandotti, Cross-polarized photon-pair generation and bichromatically pumped optical parametric oscillation on a chip, Nat. Commun. 6, 8236 (2015).  
[45] J. He, B. A. Bell, A. Casas-Bedoya, Y. Zhang, A. S. Clark, C. Xiong, and B. J. Eggleton, Ultracompact quantum splitter of degenerate photon pairs, Optica 2, 779 (2015).  
[46] Y. Guo, W. Zhang, S. Dong, Y. Huang, and J. Peng, Telecom-band degenerate-frequency photon pair generation in silicon microring cavities, Opt. Lett. 39, 2526 (2014).  
[47] Z. Vernon, M. Liscidini, and J. Sipe, Quantum frequency conversion and strong coupling of photonic modes using four-wave mixing in integrated microresonators, Phys. Rev. A 94, 023810 (2016).  
[48] Q. Li, M. Davanco, and K. Srinivasan, Efficient and low-noise single-photon-level frequency conversion interfaces using silicon nanophotonics, Nat. Photonics 10, 406 (2016).  
[49] C. M. Gentry, X. Zeng, and M. A. Popovic, Tunable coupled-mode dispersion compensation and its application to on-chip resonant four-wave mixing, Opt. Lett. 39, 5689 (2014).  
[50] L. Chen, N. Sherwood-Droz, and M. Lipson, Compact bandwidth-tunable microring resonators, Opt. Lett. 32, 3361 (2007).  
[51] D. J. Moss, R. Morandotti, A. L. Gaeta, and M. Lipson, New CMOS-compatible platforms based on silicon nitride and hydex for nonlinear optics, Nat. Photonics 7, 597 (2013).  
[52] Z. Vernon, M. Menotti, C. Tison, J. Steidle, M. Fanto, P. Thomas, S. Preble, A. Smith, P. Alsing, M. Liscidini, and J. E. Sipe, Truly unentangled photon pairs without spectral filtering, Opt. Lett. 42, 3638 (2017).  
[53] J. Christensen, J. Koefoed, K. Rottwitt, and C. McKinstrie, Engineering spectrally unentangled photon pairs from nonlinear microring resonators by pump manipulation, Opt. Lett. 43, 859 (2018).  
[54] C. Tison, J. Steidle, M. Fanto, Z. Wang, N. Mogent, A. Rizzo, S. Preble, and P. Alsing, Path to increasing

the coincidence efficiency of integrated resonant photon sources, Opt. Express 25, 33088 (2017).  
[55] M. G. Paris, F. Illuminati, A. Serafini, and S. De Siena, Purity of Gaussian states: Measurement schemes and time evolution in noisy channels, Phys. Rev. A 68, 012314 (2003).  
[56] S. Dwyer, et al., Squeezed quadrature fluctuations in a gravitational wave detector using squeezed light, Opt. Express 21, 19047 (2013).  
[57] H. Qi, D. J. Brod, N. Quesada, and R. García-Patrón, Regimes of classical simulability for noisy Gaussian boson sampling, arXiv:1905.12075 (2019).  
[58] H. Wang, W. Li, X. Jiang, Y.-M. He, Y.-H. Li, X. Ding, M.-C. Chen, J. Qin, C.-Z. Peng, C. Schneider, M. Kamp, W. J. Zhang, H. Li, L. X. You, Z. Wang, J. P. Dowling, S. Hofling, C. Y. Lu, and J. W. Pan, Toward Scalable Boson Sampling with Photon Loss, Phys. Rev. Lett. 120, 230502 (2018).  
[59] S. L. Braunstein and H. Kimble, Teleportation of Continuous Quantum Variables, Phys. Rev. Lett. 80, 869 (1998).

[60] D. T. Spencer, J. F. Bauters, M. J. Heck, and J. E. Bowers, Integrated waveguide coupled  $\mathrm{Si}_3\mathrm{N}_4$  resonators in the ultrahigh- $Q$  regime, Optica 1, 153 (2014).  
[61] K. Fukui, A. Tomita, A. Okamoto, and K. Fujii, High-Threshold Fault-Tolerant Quantum Computation with Analog Quantum Error Correction, Phys. Rev. X 8, 021054 (2018).  
[62] A. Serafini, Quantum Continuous Variables: A Primer of Theoretical Methods (CRC Press, Boca Raton, FL, 2017).  
[63] R. A. Horn and C. R. Johnson, Matrix Analysis (Cambridge University Press, New York, NY, 1990).  
[64] N. Killoran, J. Izaac, N. Quesada, V. Bergholm, M. Amy, and C. Weedbrook, STRAWBERRY FIELDS: A software platform for photonic quantum computing, Quantum 3, 129 (2019).  
[65] N. Quesada, Ph.D. thesis, Department of Physics, University of Toronto (Canada), 2015.  
[66] P. Marian and T. A. Marian, Squeezed states with thermal noise. I. Photon-number statistics, Phys. Rev. A 47, 4474 (1993).