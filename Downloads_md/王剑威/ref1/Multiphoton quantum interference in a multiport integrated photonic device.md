ARTICLE

Received 3 Sep 2012 | Accepted 30 Nov 2012 | Published 15 Jan 2013

DOI: 10.1038/ncomms2349

# Multiphoton quantum interference in a multiport integrated photonic device

Benjamin J. Metcalf $^{1,\ast}$ , Nicholas Thomas-Peter $^{1,\ast}$ , Justin B. Spring $^{1}$ , Dmytro Kundys $^{2}$ , Matthew A. Broome $^{3}$ , Peter C. Humphreys $^{1}$ , Xian-Min Jin $^{1,4}$ , Marco Barbieri $^{1}$ , W. Steven Kolthammer $^{1}$ , James C. Gates $^{2}$ , Brian J. Smith $^{1}$ , Nathan K. Langford $^{5}$ , Peter G.R. Smith $^{2}$  & Ian A. Walmsley $^{1}$

Increasing the complexity of quantum photonic devices is essential for many optical information processing applications to reach a regime beyond what can be classically simulated, and integrated photonics has emerged as a leading platform for achieving this. Here we demonstrate three-photon quantum operation of an integrated device containing three coupled interferometers, eight spatial modes and many classical and nonclassical interferences. This represents a critical advance over previous complexities and the first on-chip nonclassical interference with more than two photonic inputs. We introduce a new scheme to verify quantum behaviour, using classically characterised device elements and hierarchies of photon correlation functions. We accurately predict the device's quantum behaviour and show operation inconsistent with both classical and bi-separable quantum models. Such methods for verifying multiphoton quantum behaviour are vital for achieving increased circuit complexity. Our experiment paves the way for the next generation of integrated photonic quantum simulation and computing devices.

Realizing quantum-enhanced information processors for tasks such as simulation and computation demands experimental systems of sufficient complexity that their dynamics cannot be efficiently determined using classical processors. Reaching this regime in practice, however, remains a critical open challenge. Integrated quantum optics provides great promise for enabling photonic experiments, which are otherwise generally limited to relatively small-scale experiments, to reach this new regime of complexity. Chip-based fabrication enables sophisticated networks involving multiple interfering pathways in a compact and stable physical architecture, and pioneering work has shown the viability of this approach for the manipulation of the quantum properties of photons $^{1-10}$ . To date, experiments have demonstrated up to three-photon higher-order terms from a single non-linear photon source being coupled into the two input modes of a single interferometer $^{11}$ , or alternatively, two-photon correlations in up to 21 waveguide modes $^{5,12}$ . Building a photonic system capable of truly outperforming classical processors, however, can only be achieved by simultaneously increasing the number of modes and interference nodes in the circuit and the number of photons distributed among them. Being able to demonstrate such multiphoton interference on this scalable platform opens the way for investigations of genuinely multipartite features, as required for a broad array of quantum simulators $^{13}$ , quantum error-correction $^{14}$  and exploration of the regime beyond the classically computable $^{15}$ .

There are two key outstanding challenges associated with this task of scaling up integrated photonic circuits to these larger systems. First, photon loss exponentially limits the complexity achievable in a quantum circuit, both in terms of the number of circuit elements and the number of photons that can be used effectively. In integrated photonics, significant losses arise from interfacing the circuit with both sources and detectors and become more pronounced with increased photon numbers[16,17]. Ultimately, losses are fundamentally limited by the intrinsic optical properties of the medium and these clearly scale with the circuit size. Second, the monolithic nature of integrated architectures means it is also difficult to verify that the chip meets the design specification. In particular, it is not possible in general to access individual components in situ using the external input and output ports, nor is it always possible to configure ancillary access ports for injecting probe states or performing detection locally. On the other hand, existing process tomography techniques for verifying the quantum operation of a full chip[18,19] become impracticable once it becomes sufficiently complex. Instead, other simpler ways to measure the chip's transformation are required.

In this work, we demonstrate a critical advance in the complexity of quantum-integrated photonic devices by simultaneously increasing the number of photons and the number of spatial modes used. Using a circuit in which three photons are distributed over eight modes and three coupled interferometers[20-22], we certify quantum operation beyond both the classical limit and what can be achieved with two photons using a hierarchy of higher-order photon correlation functions. As part of this, we also provide the first on-chip demonstration of a Hong-Ou-Mandel-type interference effect with three individual input photons. We further show that a critical step in verifying the correct quantum operation was characterizing the operating parameters of individual circuit components, and we introduce a simple loss-insensitive method to achieve this using classical light scattered from the device in the transverse direction. In this paper, we verify three-photon interactions that achieve a complexity sufficient to realise a next generation of on-chip quantum information protocols such as cluster-state generation and teleportation.

![](images/e89806a5fee796bcc410c1d023874db9e884c0871c40b77415887e1b432a044c.jpg)  
Figure 1 | Schematic of the single photon source and multiport waveguide circuit. We generate two pairs of single photons by spontaneous parametric down conversion in two non-linear crystals (potassium dihydrogen phosphate, KDP), driven by a frequency doubled (second-harmonic generation, SHG) femtosecond laser (Ti:saphh) - see methods. The circuit consists of eight modes labelled  $a$  to  $h$ , 10 beam splitters labelled  $\eta_{1}$  to  $\eta_{10}$ , and three variable phase shifters labelled  $\phi_{1}$  to  $\phi_{3}$ . Single photons are launched into a subset of  $b$  to  $g$  and the output of each mode was monitored by a single-photon detector. The ancillary modes  $a$  and  $h$  were not accessible for coupling.

# Results

How to verify quantum operation. The multiport waveguide circuit used in these experiments consists of three-coupled Mach-Zehnder interferometers spanning eight spatial modes, with phase control inside the interferometers implemented by thermo-optic phase shifters (see Fig. 1 and Methods for a detailed description of the experimental apparatus). Our main aim is to show genuinely quantum operation of the circuit in a context that demonstrates its full complexity in terms of simultaneously increased number of independent input photons and number of interacting modes and interferometers. To do this, we inject individual single photon states into one mode of each of the interferometers (modes  $c$ ,  $d$  and  $f$ ) and measure the visibility of three-photon nonclassical interference at different combinations of output ports. If the observed visibility is stronger than that predicted when the single-photon inputs are replaced with classical light, this acts as a witness to the desired quantum behaviour.

To calculate the predicted classical bounds, we must assume that the circuit itself operates completely coherently (unitary operation), so we first characterise the circuit using an element-wise, loss-tolerant approach with classical input states, in the process avoiding any need for resource-intensive quantum process tomography. We confirm the reliability of our characterisation by first observing two-photon quantum interference and comparing its behaviour with both a classical and a quantum model: the former is clearly inconsistent with the experimental results, while the latter shows good agreement. Finally, extending this method, we show that the observed three-photon interference measurements exclude with high confidence levels both the classical model, as well as quantum models involving bi-separable states. The nature of the observed three-photon interferences, combined with the known topology of the circuit relative to the input photons, suggest that the results cannot be explained by using a simplified or restricted subsection of the illustrated circuit. This implies that the experiment utilises the full available complexity of the circuit.

Multiphoton integrated-optics experiments set stringent demands on performance with regard to photon loss $^{16,17}$ . Particular care needs to be taken to optimise all experimental efficiencies, especially in experiments utilising down-conversion photon sources, such as this one, to minimise higher-order noise terms $^{23}$ . In order to demonstrate high-brightness multiphoton states 'on-chip', we have combined a range of technical solutions for optimising the loss properties, including efficient pair-source heralding, optimal coupling of six-channel fiber arrays to the chip and use of a low-loss integrated platform (see Methods). These measures enabled us to go beyond the state-of-the-art and for the first-time realise on-chip three-photon interference allowing the exploration of interesting multipartite phenomena on an interferometrically stable and scalable platform.

Characterising circuit operation. The three coupled interferometers in our waveguide circuit, fabricated by UV direct-write technology on a silica-on-silicon substrate<sup>2</sup>, involve 10 beam splitters and three thermo-optic phase shifters, a circuit which has only previously been realised directly in a simplified polarisation-based encoding with bulk optics<sup>20-22</sup>. Temperature control by means of a thermo-electric Peltier element maintained stable beam splitting ratios and phase offsets over many weeks. Individually characterising these parameters permits us to simulate the required multiphoton interference visibilities.

We measured the beam splitter reflectivities,  $\eta_{1}$  to  $\eta_{10}$ , by sending continuous-wave laser light through each splitter in turn and calculating the reflectivity using a ratiometric analysis, which is independent of coupling and transmission losses[17]. This technique uses four measurements for each beam splitter, coupling light in turn into each input port and recording the power at each output port. Because of the complex circuit topology, it is not generally possible to independently access the input and output modes, so instead, light scattered out of the chip surface was used to measure the output powers. The ratiometric calculation is insensitive to different scattering efficiencies in the same way as to different interface coupling efficiencies. Figure 2a,b show a typical example, with  $100\mathrm{mW}$  of laser light coupled into the chip (note that splitters 4 and 7 only had one available input, as modes  $a$  and  $h$  were not accessible for coupling, see Fig. 1). The input polarization was adjusted to maximize the amount of the transverse scatter, which was imaged using a charge-coupled device with a highly linear response. Integrating over a specified region then provides the required intensity measurements (Fig. 2c).

For each Mach-Zehnder interferometer, we characterised the phase by considering the interferometer as an effective beam splitter with a reflectivity determined by the phase shift and the reflectivities of the four relevant beam splitters (see Supplementary Methods for details). This was again characterised using the ratiometric technique. Adjusting the voltage across the thermo-optic element varies the effective reflectivity, as shown in Fig. 2d. Fitting these data then provide both an estimate of the zero-voltage phase of the interferometer, and an independent consistency test of the four beam splitter reflectivities, which define each interferometer. These checks agreed within the measurement uncertainty.

Demonstrating quantum operation and circuit complexity. Having characterised the individual circuit elements classically, we now investigate the operation of the circuit using quantum input light. We generated three individual input photons from two spectrally factorable down-conversion pair sources, using both photons from one pair and using the other as a heralded single photon (see Fig. 1 and Methods for details). Detecting all four photons in this way to give four-fold coincidence measurements reduces the effects of noise terms.

We first study the quantum interference from two-photon inputs to confirm our classical device characterisation and our single photon indistinguishability. In these experiments, we injected photons into two of the selected input modes:  $cf$ ,  $cd$  or  $df$  (corresponding to regions I, II and III in Fig. 3a). We then measured interference visibilities for all possible coincidence outcomes by varying the timing of one photon using an off-chip optical delay stage (for example, Fig. 3d,e), and compared the observed values to the quantum (boxes) and classical (triangles) predictions (see Fig. 3a). The expected quantum visibilities were calculated directly from the quantum output state predicted by the classically characterised circuit unitary adjusted for the independently measured fidelity between photon pairs (see Supplementary Methods). The corresponding classical visibilities were calculated by replacing the input Fock states with phase-averaged coherent states (see Methods).

A  $\chi^2$ -test verifies that these data are consistent with the quantum predictions while in strong disagreement with classical theory[24]. The likelihood for observing a set of interference visibilities is calculated given measurement uncertainties in the observed interference visibilities and the underlying circuit parameters (see Methods). The residuals from quantum theory (Fig. 3c) give a reduced  $\chi_r^2 = 0.9$ ; a value at least this large will occur with probability  $P(\chi_r^2 \geq 0.9) = 0.5$ . By contrast, the residuals from classical theory (Fig. 3b) give  $\chi_r^2 = 23$  corresponding to  $P(\chi_r^2 \geq 23) < 10^{-16}$ . Furthermore, the ultimate classical visibility limit of  $1/2$  is expected and observed to be exceeded by output mode combinations  $de$ ,  $cd$  and  $dg$ .

The three experiments each used a different pair-wise combination of the three chosen input photons, allowing the different input photons to be tested individually against each of the other two. In all three cases, the experiments are in good agreement with the expected quantum results. This suggests that our element-wise characterisation technique is a good predictor of device performance and shows that each of the three-photon quantum states has a good fidelity with the other two, a critical factor for observing genuine three-photon interference (see Supplementary Methods).

To demonstrate the complexity of the quantum circuit, we study the higher-order nonclassical interference, which arises when the three coupled interferometers are all operating simultaneously and in parallel, each injected with quantum light at the input. We observe this via the (heralded) three-photon coincidence counts (for example, Fig. 4d,e), with three individual input photons coupled into modes  $c$ ,  $d$  and  $f$ . Again detecting the fourth photon enabled discrimination between downconversion events with one photon in each spatial mode  $\left( \left|111\right\rangle_{\mathrm{cdf}} \right)$  from equally likely unwanted noise events with two photons in each of only two input modes  $\left( \left|022\right\rangle_{\mathrm{cdf}} \right)$ . After setting the temporal delay between input modes  $c$  and  $f$  to maximize their two-photon interference, we varied the delay for input mode  $d$  while simultaneously monitoring the eight three-fold coincidence combinations described in Fig. 4a. We observed average four-photon coincidence rates of around  $16\mathrm{mHz}$  and measured the heralded three-folds continuously for  $294\mathrm{h}$ , iterating a full scan of the temporal delays each minute. This method averages out long-term systematic effects, such as drifts in the chip coupling efficiencies and photon source performance[25], and allows an accurate calculation of the statistical error in the counts.

As in the two-photon experiments, the observed three-photon quantum interference visibilities agree with quantum predictions based on the individually characterised circuit elements and are completely inconsistent with the equivalent classical predictions (Fig. 4b,c). The quantum prediction gives  $\chi_{\mathrm{r}}^{2} = 1.5$  with  $P(\chi_{\mathrm{r}}^{2}\geq 1.5) = 0.2$ , whereas the classical prediction gives  $\chi_{\mathrm{r}}^{2} = 6$  with  $P(\chi_{\mathrm{r}}^{2}\geq 6) < 10^{-8}$ . Moreover, using a global optimisation

![](images/9ea98bf64e1e3dff267d471c226e4969e84d1ade6bf0930d74241d99d885f359.jpg)

![](images/e9e71b8173c811e404824ac3edb100c122677cb42c9fa622f9c514ce51a97952.jpg)

![](images/c5541067020c0285cd8a83224939a4511067508850bf03e7980d6d4284fe1867.jpg)  
Figure 2 | Classical characterisation of integrated circuit elements. (a,b) Charge-coupled device (CCD) images of light scattered in the transverse direction from the waveguide when light is coupled into the bottom (a) and top (b) input of a beam splitter. Red arrows denote the direction of propagation of the light. The white box denotes the integration region at the output for the ratiometric analysis. (c) The integrated intensity is used as part of a ratiometric analysis to determine  $\eta_{8} = 0.55 \pm 0.02$ . (d) Interference fringe produced by scanning  $\phi_{1}$ . The parameter values obtained from the theoretical fit (red line) include the zero-voltage phase offset.

![](images/e10a4c172c4dff7fb9a84b0e2e29a17f1a1f72bb076880aa0f98e6c03282d9cc.jpg)

![](images/30fcf09142dd9267f20a4296e05b5133d84b74f55536e39e196b93c0add60eb7.jpg)  
Figure 3 | Two-photon interference. (a) Experimentally measured two-photon interference visibilities (red circles) are compared against the quantum (clear boxes) and classical (blue triangles) predictions. Regions I, II and III contain experiments using input modes  $cf$ ,  $cd$  and  $df$ , respectively. The errors shown on the simulated quantum and classical visibilities were calculated by Monte-Carlo simulation (see Supplementary Methods); errors on the classical visibilities are smaller than the marker size because of the decrease in sensitivity of classical interference to the measured circuit parameters. (b,c) The residuals between the measurements and the calculated classical and quantum visibilities. (d,e) Example two-fold coincidence counts between output channels  $dg$  and  $fg$  when two photons are input into modes  $df$  and the optical delay of mode  $d$  is varied. The shaded area shows the uncertainty in the determined visibility.

![](images/9a12c59b5de786cab54b24392210ea524fd5056381d0d998911e5a02f9dfdc3d.jpg)

![](images/08e6a9e309ae101637a743bedb9d4dffe651409f387e85b0c896b6b765366cc8.jpg)

![](images/595d9cfe6fc2605ee4b47d920a83af53296d521cd72e958195b2f3f5196c4be5.jpg)

![](images/0949f4b10a4431f3a512e83cf66fa7a9d6405848956fb04655903b31d2fc0642.jpg)

routine, we determined the maximum classical interference visibility for any possible circuit parameters with this circuit topology to be 0.59 (see Supplementary Methods). This ultimate limit is exceeded by more that one s.d. by output channel combination cdf. Furthermore, a  $\chi^2$ -test shows that the circuit parameters, which result from this optimisation are strongly inconsistent with our measured values  $P(\chi_{\mathrm{r}}^2 \geq 4.4) = 10^{-8}$ . Thus,

only the full quantum explanation can plausibly account for the higher observed visibilities. We note that Fig. 4a includes all measured three-fold coincidence combinations, including several that occur very rarely and which therefore lead to large error bars in the measured visibility. Nevertheless, including all observed data in our analysis, we can exclude classical models with extremely high confidence, despite the low-count rates in some channels.

![](images/3a30e77fdf9c7428a1a0c7e5503220d3e66272f68d94e1c8336c7c62ed0bcc26.jpg)  
Figure 4 | Three-photon interference. (a) The experimentally recorded three-photon interference visibilities (red circles) are compared against the predicted quantum (clear boxes) and classical (blue triangles) results as in Fig. 3. The errors shown on the simulated quantum and classical visibilities were calculated by Monte-Carlo simulation (see Supplementary Methods); errors on the classical visibilities are smaller than the marker size because of the decrease in sensitivity of classical interference to the measured circuit parameters. (b,c) The residuals between the measurements and the calculated classical and quantum visibilities. (d,e) Example four-fold coincidence counts of output channels cdf and bdg when the input photon in mode  $d$  is temporally delayed. The shaded area shows the uncertainty in the determined visibility.

![](images/e274df55f5580ada03e4b4bbd8b3445c746fb5f8f96b990fac1b002e0448ffb2.jpg)

![](images/a9763b165d9f19c960f80e439f3280419ff17a7e292782ab883596646055f57f.jpg)

Finally, to verify that the observed interference results from a quantum interaction of all three photons and is not explainable via a bi-separable interaction only, we also simulated the expected quantum visibilities when one of the three photons remains completely distinguishable from the other two at all temporal delays. These quantum bi-separable explanations are also inconsistent with the data, predicting at most a likelihood of  $P < 10^{-8}$  for the observed interference signature.

# Discussion

These results demonstrate genuinely multipartite quantum operation in a next-generation integrated circuit that provides a critical new level of complexity in integrated quantum photonics. The measurements simultaneously accessed three coupled interferometers, with classical interference at three circuit nodes and nonclassical interference at five circuit nodes. This experiment also represents the first observation of chip-based, multipartite nonclassical interference, which relies on more than two individual photonic inputs. By moving beyond these previous two-photon, two-mode experiments, our work has demonstrated the challenges lying ahead for integrated quantum photonic experiments. We have proposed viable solutions in order to reach a level of complexity necessary for the exploration of interesting multipartite effects for the first time on the integrated photonics platform.

We develop a practical method to verify successful operation of the device: a loss-independent technique to classically characterise individual circuit parameters and two-photon interference to verify device performance understood by simulations. Using a parameterised characterisation allows identification of poorly fabricated components and freedom to separately simulate individual circuit subsections, such as on-chip state preparation, manipulation and measurement. Having techniques that successfully predict device performance will be critical as experimental capacities continue to improve, making this demonstration an important step forward. An alternative scheme has recently been introduced for inferring the overall unitary transformation implemented by a device from a series of classical interference experiments using only the nominal input and output ports[26-28]. Although this does not give access to individual components, it may be useful for cases where only the operation of the device as a whole is of concern.

In this paper, we highlight the often-unacknowledged fact that minimising losses will be critical for scaling up integrated circuits to the regime where they can no longer be simulated using classical processors. An array of ongoing work seeks to do so by integrating $^{29-32}$  and synchronising $^{33}$  quantum light sources, as well as developing high-efficiency integrated detectors $^{34,35}$ . We have shown how it is already possible to overcome losses and perform on-chip experiments requiring three-photon quantum interference.

Increasing the complexity of integrated photonic devices requires not only an increased number of discrete optical modes but also complex multiphoton quantum interference across all of these modes. By moving beyond previous two-photon experiments, our work has demonstrated the challenges lying ahead for integrated quantum photonic experiments, and proposed viable solutions in order to reach a level of complexity comparable with other architectures. This work has already verified the multiphoton interference necessary for the first nontrivial tests of recently proposed boson sampling problems[15,36,37]. It also provides the first demonstration of quantum operation of a chip, which is sufficiently complex to allow a range of advanced quantum information protocols, such as teleportation and cluster-state generation, to be realised on an integrated platform.

# Methods

Device fabrication. The waveguide circuit used in this work was fabricated by use of UV direct-write technology on a silica-on-silicon substrate (See Supplementary Fig. S1 and (ref. 2)). The individual waveguides were written by focusing a continuous-wave UV laser  $(244\mathrm{nm}$  wavelength) onto the chip, which is subsequently moved transversely to the surface normal with computer-interfaced 2D motion control. The UV-writing process enables creation of beam splitters (X couplers) by crossing waveguides at different angles[38]. These are much smaller than traditional directional couplers, which helps to reduce the effect of propagation loss in more complex circuits. The effective beam splitter reflectivity of these X couplers is primarily governed by the intersection angle of the guides, which reduces sensitivity to wavelength, polarisation and temperature fluctuations making them extremely stable over the long experimental durations in this work. The characterised beam splitter values are presented in Supplementary Fig. S2. The thermo-optic phase shifters utilise a small NiCr electrode  $(0.35\times 50\mu \mathrm{m}\times 2.5\mathrm{mm},$ $0.85\mathrm{kOhm}$  electrical resistance) deposited directly over one of the waveguides through which a current can be passed. The temperature-stabilised passive stability of the interferometers with the phase-shifters set to a constant voltage was measured to be  $<  1^{\circ}$  over  $24\mathrm{h}$

High-brightness multiphoton states on-chip. An 80-MHz Ti:sapphire oscillator (Mai-Tai, Spectra Physics) produces 100 fs pulses at  $830\mathrm{nm}$  (2.6 W average power),

which are upconverted to  $700\mathrm{mW}$  of  $415\mathrm{nm}$  light in a  $700 - \mu \mathrm{m}\beta \mathrm{-BaB_2O_4}$  (BBO) crystal cut for type-I second-harmonic generation. This blue light is split on a 50:50 beam splitter and used to pump two  $8\mathrm{mm}$ -long AR-coated potassium dihydrogen phosphate crystals phase-matched for degenerate type-II collinear parametric down-conversion (See Supplementary Fig. S3). We optimise the collection optics and spatial mode-matching to achieve a coincidence count rate of  $160\mathrm{kHz}$  on each crystal with a raw heralding efficiency of  $28 - 30\%$  without any filters. The source is designed to be spectrally factorable[39], which improves the heralding efficiency we can achieve when interference filters (Semrock,  $\Delta \lambda = 3\mathrm{nm}$ ) are used to match the bandwidths of the broad and narrowband daughter photons. With the filters in place we achieve a four-photon coincidence rate of  $20\mathrm{Hz}$  and two-photon fidelities of 0.98 (narrowband-narrowband) and 0.92 (narrowband-broadband)—see Supplementary Methods.

Three of the photons were coupled into polarisation-maintaining fibers and launched into the waveguide circuit using a butt-coupled polarisation-maintaining v-groove array. Index matching oil is applied between the fiber array and the chip to reduce reflection losses and a 6-axis piezo-controlled alignment stage provides all the degrees of freedom necessary to achieve optimal simultaneous coupling into all six input modes. The piezo-driven axes were operated in closed-loop mode to maintain this coupling throughout the experiment. An identical set-up is used on the output to a achieve maximal coupling from the chip into the single-photon counting modules. A home-built FPGA-based logic unit records all desired coincidence counts simultaneously.

Predicted visibilities. The simulated visibilities in our interference experiments were calculated by first simulating the complete quantum output state,  $|\psi_{\mathrm{out}}\rangle$  using the characterised circuit unitary,  $\mathbf{U}_{\mathrm{circ}}$  (See Supplementary Methods and Supplementary Figs S4 and S5). The intensity cross-correlation functions at zero and infinite temporal delay were then used to find an interference visibility.

When photons are launched into modes  $\{a_i\}$  of a linear optical circuit the intensity cross-correlation between output modes  $\{b_i\}$  at zero temporal delay is:

$$
\Gamma_ {\left\{b _ {i} \right\}} ^ {(0)} = \left\langle \psi_ {\text {o u t}} ^ {\left\{a _ {i} \right\}} \right| \left(\prod_ {b _ {j}} \hat {\mathrm {I}} _ {b _ {j}}\right) \left| \psi_ {\text {o u t}} ^ {\left\{a _ {i} \right\}} \right\rangle , \tag {1}
$$

where the intensity operator on mode  $i$  is  $\hat{\mathrm{I}}_i = \hat{\mathrm{b}}_i^{\dagger}\hat{\mathrm{b}}_i$ . Suppose the photon in mode  $a_{d}$  undergoes a temporal delay then the total output state is now a classical mixture:

$$
\rho_ {\text {o u t}} = \left| \psi_ {\text {o u t}} ^ {\{a _ {i}, i \neq d \}} \right\rangle \left\langle \psi_ {\text {o u t}} ^ {\{a _ {i}, i \neq d \}} \right| + \left| \psi_ {\text {o u t}} ^ {(a _ {d})} \right\rangle \left\langle \psi_ {\text {o u t}} ^ {(a _ {d})} \right|. \tag {2}
$$

The intensity cross-correlation function at infinite delay is then,

$$
\Gamma_ {\left\{b _ {i} \right\}} ^ {(\infty)} = \operatorname {T r} \left\{\rho_ {\text {o u t}} \prod_ {b _ {i}} \hat {\mathrm {I}} _ {b _ {i}} \right\}, \tag {3}
$$

and the visibility of the interference pattern between the  $n$ th-order output coincidence counts is then given by

$$
V _ {\text {q u a n t}} = \frac {\Gamma_ {\{b _ {i} \}} ^ {(\infty)} - \Gamma_ {\{b _ {i} \}} ^ {(0)}}{\Gamma_ {\{b _ {i} \}} ^ {(\infty)}}. \tag {4}
$$

The corresponding classical visibility of this interference pattern is given by injecting three equal amplitude coherent states of mutually randomised phase into modes  $\{a_i\}$ . This ensures that we mimic independent sources of light, which will have no first-order correlation as required to compare against Hong-Ou-Mandel-type quantum interference. Coherent states represent the classical state, which have the highest interference visibility, ensuring the bound we calculate is an upper limit. The resulting output vector of complex amplitudes is:

$$
\mathbf {e} _ {\text {o u t}} = \mathbf {U} _ {\text {c i r c}} \mathbf {e} _ {\text {i n}} \tag {5}
$$

$$
\mathbf {e} _ {\text {o u t}} = \mathbf {U} _ {\text {c i r c}} \left( \begin{array}{c} e ^ {i \theta_ {1}} \\ \vdots \\ e ^ {i \theta_ {n}} \end{array} \right), \tag {6}
$$

where  $e_{\mathrm{out}}$  is the vector of time-independent electric fields in each of the output modes and similarly for  $e_{\mathrm{in}}$ . The phase-averaged intensity cross-correlation function is then

$$
\Gamma_ {\{b _ {i} \}} ^ {\prime} (0) = \frac {1}{(2 \pi) ^ {n}} \int_ {0} ^ {2 \pi} \dots \int_ {0} ^ {2 \pi} \prod_ {b _ {i}} | \left(\mathbf {e} _ {\text {o u t}}\right) _ {b _ {i}} | ^ {2} d \theta_ {1} \dots d \theta_ {n}. \tag {7}
$$

The classical cross-correlation function at infinite delay is calculated in a similar manner, taking incoherent sums between the delayed and non-delayed

photons,

$$
\Gamma_ {\left\{b _ {i} \right\}} ^ {\prime} (\infty) = \frac {1}{(2 \pi) ^ {n}} \int_ {0} ^ {2 \pi} \dots \int_ {0} ^ {2 \pi} \prod_ {i} \left(\left| \left(\mathbf {e} _ {\text {o u t}} ^ {\left\{a _ {i}, i \neq d \right\}}\right) _ {\mathrm {b} _ {i}} \right| ^ {2} + \left| \left(\mathbf {e} _ {\text {o u t}} ^ {\left(a _ {d}\right)}\right) _ {\mathrm {b} _ {i}} \right| ^ {2}\right) d \theta_ {1} \dots d \theta_ {n}. \tag {8}
$$

From which we calculate the classical interference visibility,

$$
V _ {\text {c l a s s}} = \frac {\Gamma_ {\{b _ {i} \}} ^ {\prime} (\infty) - \Gamma_ {\{b _ {i} \}} ^ {\prime} (0)}{\Gamma_ {\{b _ {i} \}} ^ {\prime} (\infty)}. \tag {9}
$$

$\chi^2$ -test. To estimate the likelihood of observing a particular set of  $m$  interference visibilities  $\nu$ , we construct the probability density function

$$
f (\mathbf {v}) \sim \int \left(\prod_ {i} ^ {n} \exp \left(\frac {- \alpha_ {i} ^ {2}}{2 s _ {i} ^ {2}}\right) \prod_ {i} ^ {m} \exp \left(\frac {- \left(v _ {i} - w _ {i} (\alpha)\right) ^ {2}}{2 \sigma_ {i} ^ {2}}\right)\right) d ^ {n} \alpha , \tag {10}
$$

where  $w_{i}(\alpha)$  is the calculated  $i$ th visibility based on the set on  $n$  circuit parameters  $\alpha$ ,  $\sigma_{i}$  is the measurement s.d. in the observed visibility  $\nu_{i}$ , and  $s_i$  is the measurement s.d. of the characterised circuit parameter  $\alpha_{i}$ . We approximate each  $w_{i}(\alpha)$  to be linear in  $\alpha$ ,

$$
w _ {i} (\alpha) \approx w _ {i} ^ {0} + \sum_ {j} ^ {n} \frac {\partial w _ {i}}{\partial \alpha_ {j}} \alpha_ {j}, \tag {11}
$$

which we verify to be accurate to within 0.02 over the range  $\pm 2s_{j}$ . The resulting multidimensional Gaussian integral yields an analytic solution with an exponent quadratic in visibility residuals. We analyse our data in a basis  $x_{j} = \Sigma_{i}c_{ij}(\nu_{i} - w_{i}^{0})$  so that  $f(x)$  is factorable:

$$
f (\mathbf {x}) \sim \prod_ {i} ^ {m} \exp \left(- \lambda_ {i} x _ {i} ^ {2}\right). \tag {12}
$$

The visibilities  $\mathbf{x}$  are thus statistically independent and a typical  $\chi^2$ -test,  $\chi_r^2 = 1 / m\Sigma_i^m\lambda_ix_i^2$ , can be applied. If we instead errantly assume that the uncertainties in our simulated visibilities are uncorrelated, we calculate a  $\chi^2 \sim 0.3$  lower than that reported for the quantum analysis of our experiments.

# References

1. Politi, A., Cryan, M. J., Parity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
2. Smith, B. J., Kundys, D., Thomas-Peter, N., Smith, P. G. R. & Walmsley, I. A. Phase-controlled integrated photonic quantum circuits. Opt. Express 17, 13516-13525 (2009).  
3. Matthews, J., Politi, A., Stefanov, A. & O'Brien, J. L. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nat. Photon 3, 346-350 (2009).  
4. Politi, A., Matthews, J. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
5. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
6. Marshall, G. et al. Laser written waveguide photonic quantum circuits. Opt. Express 17, 12546-12554 (2009).  
7. Sansoni, L. et al. Polarization Entangled State Measurement on a Chip. Phys. Rev. Lett. 20, 200503 (2010).  
8. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
9. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nat. Commun. 2, 566 (2011).  
10. Shadbolt, P. J. et al. Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit. Nat. Photon 6, 45-49 (2011).  
11. Matthews, J., Politi, A., Bonnaue, D. & O'Brien, J. L. Heralding Two-Photon and Four-Photon Path Entanglement on a Chip. Phys. Rev. Lett. 107, 163602 (2011).  
12. Owens, J. O. et al. Two-photon quantum walks in an elliptical direct-write waveguide array. New J. Phys. 13, 075003 (2011).  
13. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nat. Phys. 8, 285-291 (2012).  
14. Reed, M. D. et al. Realization of three-qubit quantum error correction with superconducting circuits. Nature 482, 382-385 (2012).  
15. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proceedings of the 43rd annual Symposium on Theory of Computing. STOC 333-342 (ACM, New York, USA, 2011).  
16. Thomas-Peter, N. L., Smith, B. J., Dorner, U. & Walmsley, I. A. Real-world Quantum Sensors: Evaluating Resources for Precision Measurement. Phys. Rev. Lett. 107, 113603 (2011).

17. Thomas-Peter, N. et al. Integrated Photonic Sensing. New J. Phys. 13, 055024 (2011).  
18. O'Brien, J. L. et al. Quantum process tomography of a controlled-not gate. Phys. Rev. Lett. 93, 080502 (2004).  
19. Shabani, A. et al. Efficient measurement of quantum dynamics via compressive sensing. Phys. Rev. Lett. 106, 100401 (2011).  
20. Ralph, T. Scaling of multiple postselected quantum gates in optics. Phys. Rev. A 70, 012312 (2004).  
21. Lanyon, B. P. et al. Experimental demonstration of a compiled version of Shor's algorithm with quantum entanglement. Phys. Rev. Lett. 99, 250505 (2007).  
22. Lu, C.-Y., Browne, D. E., Yang, T. & Pan, J.-W. Demonstration of a compiled version of Shor's quantum factoring algorithm using photonic qubits. Phys. Rev. Lett. 99, 250504 (2007).  
23. Barbieri, M. et al. Parametric downconversion and optical quantum gates: two's company, four's a crowd. J. Mod. Optics 56, 209-214 (2009).  
24. Ghosh, R. & Mandel, L. Observation of nonclassical effects in the interference of two photons. Phys. Rev. Lett. 59, 1903-1905 (1987).  
25. Lanyon, B. P. & Langford, N. K. Experimentally generating and tuning robust entanglement between photonic qubits. New J. Phys. 11, 013008 (2009).  
26. Rahimi-Keshari, S. et al. Robust characterisation of any linear photonic device. Preprint at http://arxiv.org/abs/1210.6463 (2012).  
27. Laing, A. & O'Brien, J. L. Super-stable tomography of any linear optical device. Preprint at http://arxiv.org/abs/1208.2868 (2012).  
28. Meany, T. et al. Non-classical interference in integrated 3D multiports. Opt. Express 20, 26895-26905 (2012).  
29. Xiong, C. et al. Generation of correlated photon pairs in a chalcogenide As2S3 waveguide. App. Phys. Lett. 98, 051101 (2011).  
30. Martin, A. et al. A polarization entangled photon-pair source based on a type-II PPLN waveguide emitting at a telecom wavelength. New J. Phys. 12, 103005 (2010).  
31. Eckstein, A., Christ, A., Mosley, P. J. & Silberhorn, C. Highly efficient single-pass source of pulsed single-mode twin beams of light. Phys. Rev. Lett. 106, 013603 (2011).  
32. Martin, A., Alibart, O., Micheli, M. P. D., Ostrowsky, D. B. & Tanzilli, S. A quantum relay chip based on telecommunication integrated optics technology. New J. Phys. 14, 025002 (2012).  
33. Nunn, J. et al. Enhancing multiphoton rates with quantum memories Preprint at http://arxiv.org/abs/1208.1534 (2012).  
34. Gerrits, T. et al. On-chip, photon-number-resolving, telecommunication-band detectors for scalable photonic information processing. Phys. Rev. A 84, 060301(R) (2011).  
35. Sprengers, J. P. et al. Waveguide superconducting single-photon detectors for integrated quantum photonic circuits. App. Phys. Lett. 99, 181110 (2011).

36. Aaronson, S. A linear-optical proof that the permanent is # P-hard. Proc. R. Soc. A 467, 3393-3405 (2011).  
37. Rohde, P. & Ralph, T. Error tolerance of the boson-sampling model for linear optics quantum computing. Phys. Rev. A 85, 022332 (2012).  
38. Kundys, D. O., Gates, J. C., Dasgupta, S., Gawith, C. & Smith, P. G. R. Use of cross-couplers to decrease size of UV written photonic circuits. Photon. Technol. Lett. IEEE 21, 947-949 (2009).  
39. Mosley, P. J. et al. Heralded generation of ultrafast single photons in pure quantum states. Phys. Rev. Lett. 100, 133601 (2008).

# Acknowledgements

This work was supported by the EPSRC (EP/C51933/01, EP/J008052/1 and EP/C013956/1), the EC project Q-ESSENCE (248095), the Royal Society, the AFOSR EOARD, The Australian Research Council's Federation Fellow program (FF0668810), Centre for Engineered Quantum Systems (CE110001013) and the Centre for Quantum Computation and Communication Technology (CE110001027). J.B.S. acknowledges support from the United States Air Force Institute of Technology. X.-M.J. and N.K.L. are supported by EC Marie Curie Fellowships (PIIF-GA-2011-300820 and PIEF-GA-2010-275103). M.B. is supported by a FASTQUAST ITN Marie Curie fellowship.

# Author contributions

N.T.-P., B.J.M., J.B.S., N.K.L. and I.A.W. all contributed to designing and setting up the experiment. B.J.M. and N.T.-P. performed the experiment. J.B.S. designed the FPGA electronics and helped with data taking. D.K. and J.C.G. fabricated the waveguide device. M.A.B., B.J.M, N.T.-P. and J.B.S. contributed to building the single-photon source. X.-M.J., W.S.K., M.B., P.H., N.K.L., J.B.S., B.J.M. and N.T.-P. all contributed to the analysis of the data. All authors contributed to writing the manuscript. B.J.S, P.G.R.S and I.A.W. conceived the work.

# Additional information

Supplementary Information accompanies this paper at http://www.nature.com/naturecommunications

Competing financial interests: The authors declare no competing financial interests.

Reprints and permissions information is available at http://npg.nature.com/reprintsandpermissions

How to cite this article: Metcalf, B.J. et al. Multiphoton quantum interference in a multiport integrated photonic device. Nat. Commun. 4:1356 doi: 10.1038/ncomms2349 (2013).