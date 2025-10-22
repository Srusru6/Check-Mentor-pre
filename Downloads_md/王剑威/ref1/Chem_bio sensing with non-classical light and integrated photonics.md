# Analyst

Accepted Manuscript

This article can be cited before page numbers have been issued, to do this please use: J. Haas, M. Schwartz, U. Rengstl, M. Jetter, P. Michler and B. Mizaikoff, Analyst, 2017, DOI: 10.1039/C7AN01011G.

![](images/5d14f5d5b1dfda216894f87a2be85c3ee0811d22cc44c60ff7688ab0ef77f30f.jpg)

This is an Accepted Manuscript, which has been through the Royal Society of Chemistry peer review process and has been accepted for publication.

Accepted Manuscripts are published online shortly after acceptance, before technical editing, formatting and proof reading. Using this free service, authors can make their results available to the community, in citable form, before we publish the edited article. We will replace this Accepted Manuscript with the edited and formatted Advance Article as soon as it is available.

You can find more information about Accepted Manuscripts in the author guidelines.

Please note that technical editing may introduce minor changes to the text and/or graphics, which may alter content. The journal's standard Terms & Conditions and the ethical guidelines, outlined in our author and reviewer resource centre, still apply. In no event shall the Royal Society of Chemistry be held responsible for any errors or omissions in this Accepted Manuscript or any consequences arising from the use of any information it contains.

# Analyst

# MINI REVIEW

RECEIVED 00TH JANUARY 20XX,

# Chem/Bio Sensing with Non-Classical Light and Integrated Photonics

J. Haas<sup>a</sup>, M. Schwartz<sup>b</sup>, U. Rengstl<sup>b</sup>, M. Jetter<sup>b</sup>, P. Michler<sup>b, *</sup>, and B. Mizaikoff<sup>a, *</sup>

Accepted 00th January 20xx

DOI: 10.1039/x0xx00000x

www.rsc.org/

Modern quantum technology currently experiences extensive advances in applicability in communications, cryptography, computing, metrology and lithography. Harnessing this technology platform for chem/bio sensing scenarios is an appealing opportunity enabling ultra-sensitive detection schemes. This is further facilitated by the progress in fabrication, miniaturization and integration of visible and infrared quantum photonics. Especially, the combination of efficient single-photon sources together with waveguiding/sensing structures, serving as active optical transducer, as well as advanced detector materials is promising integrated quantum photonic chem/bio sensors. Besides the intrinsic molecular selectivity and non-destructive character of visible and infrared light based sensing schemes, chem/bio sensors taking advantage of non-classical light sources promise sensitivities beyond the standard quantum limit. In the present review, recent achievements towards on-chip chem/bio quantum photonic sensing platforms based on N00N states are discussed along with appropriate recognition chemistries, facilitating the detection of relevant (bio)analytes at ultra-trace concentration levels. After evaluating recent developments in this field, a perspective for a potentially promising sensor testbed is discussed for reaching integrated quantum sensing with two fiber-coupled GaAs chips together with semiconductor quantum dots serving as single-photon sources.

# INTRODUCTION

Interferometry is a fundamental measurement technique not limited to applications in chemistry, but has rather successfully been used in a variety of scientific fields. A typical measurement setup is a balanced Mach-Zehnder interferometer comprising two 50:50 beam splitters (BS), which can be used as a sensing instrument, e.g., for (bio)molecules (see Fig. 1a)). Coherent light incident on the first BS will be split between both arms of the interferometer, and constructive or destructive interference will occur at the output ports of the second BS depending on the potential phase shift  $\Delta \varphi$  induced in one arm of the interferometer. This measurable shift can be caused e.g. by light propagation through an area in contact with (bio)molecules, since their presence affects the effective refractive index of the guided photons. The precision of the phase measurement for a classical light source is restricted by the standard quantum limit (SQL) as  $\Delta \Phi_{SQL} = 1/\sqrt{N}$ , with  $N$  as the number of used photons.

![](images/d970ce35aec09c61b022f0f87bb39dd5754491da0532ad2cc12b315f69dcde57.jpg)

![](images/3ba7bdeb6acdbf07b82eb20919fd0aaa4cd7af58a584995c312faf15960ad665.jpg)  
Fig. 1 a) Exemplary realizations of Mach-Zender interferometers (MZI). In 1, beam paths illustrate light split at a first beam splitter (BS1), and then fed into the two arms of the interferometer. After reflection at two mirrors the beam paths are interfered at a second beam splitter (BS2) after a phase shift  $(\Delta \varphi)$  had been introduced within one of the beam paths. A schematic design of an on-chip MZI realization is shown in 2. Waveguides route the light, and evanescent field couplers (BS1 and BS2) act as substitutes for bulk beam splitters. b) Schematic description of the Hong-Ou-Mandel (HOM) effect. At a 50:50 beam-splitter, two identical photons - one at each input port - arrive at the same time. In 1 and 2, one photon is transmitted and the other one is reflected. In 3 and 4, both photons either are reflected or transmitted. Only 1 and 2 are possible, if perfectly aligned quantum mechanical interference occurs, as 3 and 4 interfere destructively.

![](images/766dc2b78555d1f53da55204f705234ad515039212cf9a2b611cdc0d3872fa0c.jpg)

![](images/20c3980e2ea5976a28f25a301925bed0b462b00d4ebd6c96abf17cb94d5be7bd.jpg)

Of particular interest to chem/bio sensor applications is the fact that photons in non-classical N00N states, which will be explained below, in principle allow quantum interferometric sensing

# MINIREVIEW

strategies with an error of the phase estimation of  $\Delta \Phi_{HL} = 1 / N$ , i.e., the Heisenberg limit (HL) (Fig. 2). This precision is only limited by the quantum mechanical law of uncertainty, if imperfections of the measurement system such as losses are neglected<sup>1,2</sup>.

![](images/2c5543dc6a1da70aa237d836f7e21fafa9612f203c81d082bbee91a07f7cd9b9.jpg)  
Fig. 2: Comparison between the standard quantum limit (SQL) and the Heisenberg limit (HL) with respect to the distinguishable phase shift  $\Delta \varphi$  and the number of probing photons.

By reducing the value of the phase precision below  $\Delta \Phi_{SQL}$ , the regime of super-sensitivity is reached. Without the usage of NOON-states or other entangled states, sensing beyond the SQL is also possible by using squeezed states. These are non-classical coherent states, whereby the amplitude-phase-uncertainty of light is squeezed. This is enabled by increasing the uncertainty in one quadrature, while reducing it in the other. For example, phasesqueezed states were successfully used to increase the sensitivity of gravitational wave detectors  $^{3,4}$ . The disadvantage of squeezed light is its rather complex generation, which typically relies on non-linear schemes such as parametric down-conversion or four-wave-mixing. These schemes are probabilistic, and thus require high pumping powers, which need to be filtered prior to sending the probing signal into the sensing area. Therefore, these schemes are currently mainly realized using highly elaborate experimental setups, and bulk optics  $^{5-8}$ .

If the sensing scenario is constrained by the power incident at the sample, as frequently the case for chemical or biological samples, it is necessary to create a probing signal with accordingly low classical background. This circumstance favours N00N states as the fundamental mechanism for generating non-classical light. N00N states are maximally path-entangled N photon states written as  $|\psi_{N00N}\rangle = \frac{1}{\sqrt{2}}\big(|N,0\rangle_{A,B} + |0,N\rangle_{A,B}\big)$ , in which N photons are in a superposition state. Hence, all photons are either in state A and none in state B or vice versa. A two-photon N00N state (i.e., a 2002 state) may be created by taking advantage of the Hong-Ou-Mandel (HOM) effect. There, the interference of two indistinguishable photons at a 50:50 beam splitter is utilized with both photons in a superposition state in either of the beam paths. Hence, the probability of both photons leaving the beam splitter at different outputs cancel each other out (see Fig. 1b)).<sup>9,10</sup> Indistinguishable implies that the photons are equal in each property including energy, polarization, and wave-packet form.

Using an interferometric sensing scheme (see Fig. 1a) where one light path experiences a phase shift  $\Delta \varphi$  with respect to the other path, the state is transformed to  $\frac{1}{\sqrt{2}}\big(|2,0\rangle +e^{i2\varphi}|0,2\rangle \big)$ , since the phase shift in the sensing area of the two-photon NOON-state is twice that of a single photon (i.e., two times  $\varphi$ ). The signal is

measured by recombining both paths at another beam splitter, and a single photon detector at each output port. Unlike classical interferometric schemes where the measurement of the signal intensity at the output ports is sufficient, quantum interference using N00N states results in a phase-shift-dependent oscillation of the coincidence rate of the single photons at the two output ports. This oscillation can be measured by determining the correlation signal of the two corresponding outputs.

As the 2002 state received a doubled phase shift compared to a single photon, the oscillation rate is twice the classical expected intensity oscillation rate. Consequently, super-resolution, i.e., a faster oscillation than the classical intensity oscillation is readily achieved. Using an N-photon NOON state would therefore result in a  $\cos (N\varphi)$  correlation signal  $^{11-13}$ ; yet, the generation of NOON states with  $N > 2$  is highly nontrivial.

Super-resolution itself can also be achieved without quantum interference  $^{14}$ . However, one can distinguish between quantum and classical input states by the degree of visibility of superresolution fringes, as depicted in Fig. 3. It is important to note that quantum interference alone is not sufficient for sensing beyond classical limits. For each particular sensing system, losses and photon generation efficiencies must be taken into account to determine whether improved performance is achieved or not. This leads to the introduction of a new threshold  $(C_{\mathrm{SIL}})$ , which can be calculated via the standard interferometric limit (SIL) as:  $C_{\mathrm{SIL}} = 1 / \sqrt{\varepsilon_p(\varepsilon_i\varepsilon_d)^{N - 1}N}$ , with the generation efficiency  $\varepsilon_{p}$  of the NOON state, interferometer transmissivity  $\varepsilon_{i}$ , and detection efficiency  $\varepsilon_{d}$  of the photons. Only if the contrast of the super-resolution fringes (see Fig. 3) is higher than this threshold, classical performance criteria may be surpassed, and super-sensitivity is reached. The contrast is defined as  $C = (I_{Max} - I_{Min}) / (I_{Max} + I_{Min})$  with the minimal  $(I_{Min})$  and the maximal  $(I_{Max})$  signal of the oscillation. This in turn is determined by the degree of indistinguishability of the photons, which is specified by the interference visibility V, and the degree of the classical mode overlap of the beam paths of the entire optical chem/bio sensing setup. Surpassing the SIL is a highly challenging demand, since, e.g., for a 2002 state a precision of  $C_{\mathrm{SIL}} = 0.96$  is required, if state-of-the-art indistinguishable single-photon sources and single-photon detectors are used  $^{16}$ . This implies that V needs to be  $\approx 0.96$ .

It is important to note that higher N00N states are more sensitive to losses  $(\varepsilon_{i}$  and  $\varepsilon_d)$ , as directly evident considering the equation of  $C_{SIL}$  above. This is due to the fact that the absorption of only one photon destroys the entire N00N state due to the collapse of the wave function. Consequently, the highest usable N00N state depends on the achievable  $C_{SIL}$  of the experiment.

If NOON states are generated with individual QDs instead of a single QD, the condition of indistinguishable photons is not sufficient anymore for achieving the required emission characteristics. Instead, the photons need to be additionally transform-limited, i.e., any effect of uncorrelated charge noise in vicinity of the QDs needs to be suppressed. This again is highly challenging, however, has been overcome and realized in recent studies operating near the ideal limit.[17] Today, the experimental realization of two-photon interference from two remote QDs is under extensive investigation, and has achieved state-of-the-art visibilities of  $\approx 50\%$ .[18]

Nevertheless, this is clearly on a path towards realization in the near future, if existing photonic technologies are smartly combined.

![](images/503094744a83d5336d480b740910474680cb7adeb66da5d97dbd7da144f621a2.jpg)  
Fig. 3: Simulated coincidences rates at the output ports of a perfectly aligned MZI using a single-photon source at each input port plotted in dependence of the phase shift in one interferometer arm for pure distinguishable (i.e., no quantum interference and just classical interference, respectively; visibility  $V = 0$ ), pure indistinguishable (i.e., maximal quantum interference; visibility  $V = 1$ ), and partially indistinguishable (i.e.,  $V = 0.5$ ) photons.  $V = 0$  and  $V = 0.5$  do not exhibit super-sensitivity despite revealing super-resolution.

A requirement for the integration of such quantum technologies into suitable real-world sensing devices is a scalable system. Hence, one needs to consider on-chip integration of all required elements for quantum sensing. Moreover, using integrated optics has the appealing benefit of providing a stable system platform enabling applications outside specialized laboratory environments. As scalability and on-chip integration are currently investigated for quantum computing, and both schemes, i.e., NOON sensing and quantum computation may be realized using linear optics with single photons, the integration of NOON state based sensing directly benefits from advances in integrated quantum computing $^{19-21}$ . Therefore, a NOON state based concept for achieving supersensitivity via two fiber-coupled on-chip platforms is discussed devising a prospective sensing platform enabling chem/bio diagnostic schemes. Prior to considering the operation and conceptualization of the required on-chip components, the required properties for the suggested III-V semiconductor quantum dots serving as single photon sources are discussed $^{22}$ , as well as the overall sensing concept for chem/bio sensing with NOON states and integrated infrared photonics.

# GENERATION OF PATH-ENTANGLED PHOTONS VIA QUANTUM DOTS

A key element for quantum photonics is the coherent generation of single photons and entangled photons  $^{23,24}$ . To date, entangled photon pairs, suitable for NOON states, are mostly generated by spontaneous parametric down conversion (SPDC) or four-wave mixing  $^{25-28}$ . However, these schemes require external optical pumping sources with high output power, and the emitted photons exhibit a Poissonian distribution, i.e., these sources may not be used as on-demand single-photon sources in a straightforward way. However, they can be used as heralded single-photon sources, i.e., if one photon of an entangled photon pair is detected, the

occurrence of the second one is certain. This renders such sources also suitable for NOON state generation. Hence, a variety of generation schemes including the measurement of super-phase-resolution have been realized  $^{29-32}$ . Besides the realization of entangled two-photon systems, entangled four-photon interference beyond the SQL has been demonstrated  $^{11}$ . Recently, even higher NOON states (i.e.,  $N = 5$ ) have been realized by mixing quantum and classical light  $^{33}$ . However, for on-chip usage of these sources, and for studying samples with low optical damage threshold, radiation incidence of the rather strong pump lasers has to be efficiently suppressed, which remains challenging for on-chip implementations  $^{34}$ . Similar challenges are encountered when using squeezed coherent states, where the usage of additional off-chip filters is commonly necessary  $^{35}$ . Another limitation of the direct production of NOON states via SPDC is the decreasing probability for the creation of high photon states, and the necessity of post-selection to filter NOON states with lower N.

In this context, semiconductor quantum dots (QD) have been introduced as a versatile alternative for deliberately producing entangled photons  $^{36-42}$ . Semiconductor quantum dots are only a few nanometers in diameter, and are usually grown on a semiconductor substrate. They can be used as bright and efficient on-demand single-photon and entangled photon sources with narrow emission bandwidths up to transform-limited photons in the bandwidth range of a few hundred MHz  $^{17}$ , and a photon generation rate at the high MHz up to GHz range  $^{43}$ . This renders QDs particularly suitable for on-chip quantum sensing schemes.

Most recently, phase super-resolution with NOON states generated by QD-based on-demand single photon sources has been shown  $^{32}$ , as well as super-sensitivity  $^{16}$ . The brightness of the source is an essential criterion for building an efficient device, whereas the state-of-the-art extraction efficiency for a quantum dot source in a cavity reaches approx.  $80\%$ $^{44-46}$ . Further important properties are the indistinguishability and coherence of the generated single photons to achieve a quantum interference with high visibility. High visibilities even  $>99\%$ , have been reported for QDs  $^{45,47,48}$ . In combination with a high performance cavity for a high photon extraction efficiency, indistinguishable photons with total generation efficiencies up to  $64\%$  have been demonstrated  $^{45}$ . A high generation efficiency is a prerequisite for sensing beyond classical limits with higher NOON states  $(N > 2)$ , which are currently limited by non-deterministic generation schemes.

A limiting factor for the creation of multi-photon entangled states is potential dephasing of a QD state, and emission wavelength fluctuations due to an unstable environment, which limits the achievable quantum interference visibility. Hence, resonant excitation is the only suitable excitation scheme, since incoherent phonon-assisted relaxation may be avoided, if excitation and emission wavelength are similar  $^{49,50}$ . In addition, cryogenic temperatures (approx. 4 K) are needed to prevent phonon-assisted linewidth broadening. However, this would not be sufficeitn for chem/bio sensing beyond classical limits. Moreover, transform-limited photons are required, as discussed in the introduction of this review.

Since on-demand creation of single photons requires pulsed excitation, the combination of resonant and pulsed excitation for coherent optical control of the QD state is essential  $^{51}$ .

# REQUIREMENTS FOR CHEM/BIO SENSING

# MINIREVIEW

From a materials perspective, on-chip sensing remains dominated by silicon-based processing techniques, which have readily matured due to ubiquitous microelectronics and silicon photonics. Consequently, on-chip integrated photonics usually takes advantage of the integration of, e.g., vertical-emitting resonant-cavity light emitting diode and laser structures on silicon substrates facilitating room temperature operation, integration with microelectronic circuitry and CMOS-compatible optical transducers. Hence, this material basis ideally lends itself for chem/bio sensing applications $^{52-54}$ . In contrast, using III-V semiconductors as material platform allows the straightforward integration of quantum dots serving as single-photon sources, which is highly nontrivial for the silicon platform.

To date, quantum dot-based on-chip light sources, which are suitable to produce highly coherent photons require operation at cryogenic temperatures, as mentioned before. This is in stark contrast to chem/bio sensing strategies, which are unfeasible at these temperatures. Therefore, the combination of a 'light source chip' (LSC) with a 'chem/bio sensing chip' (CBSC), with the latter operating at ambient conditions and connected via optical fibers is a straightforward strategy derived from state-of-the-art technologies.

Using these concepts, interferometric sensing schemes can be realized via a 50:50 beam splitter on each chip, i.e., the LSC and the CBSC (Fig. 4 a)). In this case, a two-photon NOON state is prepared on the LSC and transferred via fibers to the CBSC. Alternatively, the entire MZI setup may be realized on the CBSC, while the LSC solely acts as fiber-coupled single-photon source (Fig. 4b)). The latter approach renders quantum interference independent of phase fluctuations caused by the fibers, e.g., by temperature variations. Both approaches result in a MZI configuration with the cryogenically cooled LSC providing single photons from waveguide integrated quantum dots, and the on-chip preparation of two-photon NOON states that are directed to the MZI arms of the CBSC operating at ambient conditions.

Since this modular concept entails that each chip can be independently designed, maximum flexibility for optimizing the light source, sensing, and detection architecture is ensured. Hence, such sensing systems could be tailored and optimized to a wide range of chem/bio sensing scenarios.

The testbed displayed in Fig. 4 would only create 2002 states, and is therefore only able to beat the SQL of a balanced MZI by a factor of  $1 / \sqrt{2}$ , which could also be achieved using an unbalanced MZI with a coherent input state, and additional power propagating within the reference arm. To beat the SQL of an unbalanced MZI, the LSC may take advantage of scalable NOON state generators, as for example proposed by Lee et al. and Kok et al. These schemes rely on linear optics with single-photon sources, 50:50 beam splitters, and detectors to herald the creation of the desired NOON states. Thus, the scalability of such NOON state sensing scheme is comparable with the scalability of quantum photonic circuits applied in quantum computing, and may therefore benefit from current advances in this field. Furthermore, such schemes directly benefit from triggered single photon generation via QDs, as this allows the simultaneous creation of several single photons inside a circuit in contrast to the Poissonian distribution of probabilistic schemes such as SPDC and FWM.

An advantage of N00N sensing vs. quantum computing is the inherent sensitivity for low photon counts (i.e., qubit) of  $\mathrm{N} \geq 3$ , which

is much easier to realize compared to a full scale quantum computer  $^{57}$ . For example, a 4004 state can be created using only two sources of N=3 Fock states  $|3\rangle$ , and a composer stage. The two  $|3\rangle$  states can be created in a heralded manner using three single photon sources, two 50:50 beam splitters, and two detectors each. The composing stage converts these two  $|3\rangle$  states into a heralded N=4 NOON state using only four 50:50 beam splitters, and two heralding detectors. Further stacking of this scheme would allow the creation of even higher heralded NOON states  $^{56}$ .

The success probability of the 4004 state generation discussed above is rather low at 3/2048, as expected for the probabilistic creation scheme necessary for high N00N states. However, as the constraint relevant in N00N sensing is the power incident at the sample, all non-N00N components at the output of the LSC chip, which are heralded in this scheme could be simply filtered using an on-chip optical switch, as routinely realized using MZIs in silicon-based telecommunication applications[58,59]. Hewnce, the proposed structure can be considered a fundamental future testbed of chem/bio sensing schemes using non-classical light even entailing opportunities for scalability to higher N00N state sensing devices.

![](images/e4f9f9e5340d6afd602dd9f3e6020fe1c4d57311af71f4bb0a1e0886ce4c7026.jpg)  
Fig. 4 a) Conceptual design of a two-chip assembly comprising a light source chip (LSC), and a chem/bio sensing chip (CBSC). Entangled photons are generated by the excitation of quantum dots embedded within the waveguide arms of the LSC at cryogenic conditions (4 K), e.g. via laser light, and propagate to the first beam splitter. Fiberoptics (i.e., as shown) or free space optics can be used to feed these photons from the cryogenically cooled compartment to the CBSC, operated at ambient temperatures, which provides similar waveguiding structures. A 'sensing window' enables interaction of the photons at one arm with analyte molecules

# Analyst

present at the surface of the waveguide, which act as the phase-changing transducer via evanescent field interactions. The output arms of this MZI structure are connected to a single-photon detector system that is either integrated on-chip or - again - optically coupled via fibers. Sensing and reference arm are both covered with a protective layer such as  $\mathrm{SiO}_2$ . b) Conceptual design of a Mach-Zehnder interferometric sensing chip with increased phase stability comprising all components of the MZI architecture integrated onto a single-chip (CBSC), and a fiber-coupled quantum light source chip (LSC) operated at cryogenic conditions.

# ON-CHIP INTEGRATION

To date, comparatively complex optical systems have been used for generating N00N states and recent studies have shown that such states can be generated via photon sources integrated into waveguide circuits  $^{60,61}$ . Silverstone et al.  $^{60}$  have shown a silicon-on-insulator (SOI) device combining two four-wave mixing sources into an interferometer with a reconfigurable phase shifter and quantum interference visibilities of up to  $100\%$ .

Also, an on-chip waveguide circuit equal to an universal three qubit gate was shown on silica  $^{21}$ . However, as discussed before there is no straightforward strategy for integrating on-demand single-photon sources on a silicon chip. The GaAs platform, on the other hand, enables the direct integration of quantum dots as single-photon sources, albeit with the drawback of higher propagation losses inside the waveguide structures in comparison to silicon waveguides  $^{62}$ .

A main advantage of on-chip integration derives from the maturity and flexibility of microfabrication and semiconductor processing technologies including, e.g., (deep) UV photolithography, e-beam lithography, focused ion beam (FIB) micromachining, as well as wet and dry etching protocols (e.g., reactive ion etching (RIE), inductively coupled plasma etching, etc.). Hence, a wide spectrum of processing strategies is available for optimizing complex photonic devicesranging from prototyping for single-device fabrication to batch fabrication schemes with a considerable potential of cost-per-device reduction. Recently, integrated semiconductor devices demonstrating on-chip triggered single-photon generation, waveguiding, and beam splitter operation have been realized  $^{63}$  and may also be capable of generating path-entangled photons in the near future  $^{18,20,63}$ . Furthermore, the generation of path-entangled photons on a GaAs chip was already demonstrated  $^{64}$ .

Fig. 5 shows an on-chip beam splitter realized as an evanescent field coupler. InGaAs quantum dots are embedded into a GaAs single-mode waveguide core and can be optically excited. Subsequently, resonant fluorescence is guided alongside the waveguide structure towards a logical structure, e.g., a beamsplitter. Single-mode operation is crucial, since otherwise two-photon interference, and therefore the generation of NOON states, would be impossible, as the propagation of photons in distinguishable modes prohibits the Hong-Ou-Mandel effect and potential sensitivity enhancements disappear [15]. The coupling efficiency from a quantum dot in a waveguide can be as high as  $95\%$  for a free standing structure [18].

![](images/98451cf82ab63175d55684536d9e684b9b2032e9c146ced093af7d0a51a0331b.jpg)  
Fig. 5 a) Scanning electron microscope (SEM) image of an on-chip beam splitter with an evanescent field coupler. b) Cross-section of InGaAs quantum dots embedded into a GaAs waveguide. c) Simulated mode profile of guided radiation at  $\lambda = 892$  nm. Reprinted from  $^{19}$  with the permission of AIP Publishing.

![](images/a2030d08b4e4d0e4b658db94a1a2675a03a1a60f299b3ed1fdc62c88a11ac883.jpg)

Fig. 6 exemplarily shows the field distribution within a GaAs on  $\mathrm{Al}_{50}\mathrm{Ga}_{50}\mathrm{As}$  waveguide architecture at a wavelength of  $900\mathrm{nm}$  indicating single-mode guiding at an effective refractive index of 3.39 and providing an evanescent field extending approx.  $100\mathrm{nm}$  into the adjacent optically rarer medium, which defines the photon/sample interaction range. Especially for the generation of higher N00N states by using extended optical circuits, decoherence has to be efficiently minimized [65] and parasitic losses at structural defects or imperfections have to be limited [66]. Furthermore, only systems, which sufficiently suppress all macroscopic sources of noise including vibrations, Brownian motion or environmental sources of noise are suitable for operating at quantum noise limits. In the context of on-chip integration, the monolithic incorporation of suitable detectors, which are capable of single-photon detection directly at or within the waveguide structure, is preferable to avoid coupling losses and increase the overall optical circuit integration. Possible concepts based on superconductive nanowires have been presented lately [67-70]. Such detectors are characterized by low jitter, polarization sensitivity, fast response times and high quantum efficiencies. Nevertheless, although room temperature superconductivity is anticipated to be within reach [71], room temperature operation of such detectors, which are usually operated at liquid helium temperatures is currently out of reach. Hence, instead of requiring additional fiber coupling back into another cryostate, alternative detection schemes based on HgCdTe avalanche photodetector diodes (MCT-APTs) are potential candidates to bypass this challenge and already provide up to  $90\%$  quantum efficiency at operating temperatures up to  $210\mathrm{K}$ , which is achievable using thermoelectrical cooling [72-74].

![](images/b13b9011fe6e56089fd29aedc03245580171e6199717f686b4d3caefebf1ab90.jpg)  
Fig. 6 Normalized electric field distribution within a straight GaAs waveguide on an  $\mathrm{Al}_{50}\mathrm{Ga}_{50}\mathrm{As}$  buffer layer at a wavelength of  $900\mathrm{nm}$ .

# CHIP-TO-CHIP COUPLING

Since the coherent preparation of path-entangled photons via on-chip quantum dot light sources requires cooling to the temperature of liquid helium (i.e.,  $4\mathrm{K}$ ), the emitted radiation must be efficiently propagated to the outside of the cryogenically cooled environment for chem/bio sensing at ambient conditions, which is commonly realized via optical fibers. However, the coupling of a LSC to the fiber-optic waveguide and from the other end of the fiber to a CBSC must be realized using efficient fiber-to-chip coupling strategies as coupling losses affect  $\varepsilon_{i}$  of the  $C_{SIL}$ . Common coupling techniques derived from silicon photonics include butt coupling via V-grooves, tapered fibers, and tapered on-chip waveguides (i.e., tapered at the edge of the chip) facilitating efficient fiber-to-chip coupling<sup>75</sup>. While evanescent coupling of tapered fibers to single-mode waveguides is a useful concept (i.e., up to  $97\%$  coupling efficiency<sup>74</sup>), aggravated optical alignment limits the practical benefits of such concepts for rapid prototyping. V-grooves may enable self-alignment of fibers with on-chip waveguide structures.

Since mode-matched waveguiding is crucial for maintaining the quantum states of the propagating radiation, mode-matched coupling with high coupling efficiencies must be considered. This is achieved via appropriate tapers of the fiber and the on-chip waveguide structure designed towards mode conservation. Furthermore, a spectral window can be selected in the NIR around  $900\mathrm{nm}$  where the absorption of biomolecules is negligible, and thus, contributes only minor losses. GaAs-based semiconductor chips are readily structured by photolithographic patterning and subsequent etching using, e.g.,  $\mathrm{HBr / Br_2}$  wet chemical etching. However, such protocols are limited in the achievable resolution by the applied wavelength during photolithography and the isotropic nature of wet chemical etching. Alternatively, single-mode waveguides are more precisely defined using e-beam lithography for patterning and dry etching via, e.g., RIE with  $\mathrm{SiCl}_4 / \mathrm{Ar}$  for structuring.

# CHEM/BIO SENSING VIA ON-CHIP STRUCTURES

Chem/bio sensing chips utilizing MOVPE-grown GaAs/AlGaAs waveguide structures have readily demonstrated ultra-sensitive

evanescent field sensing capabilities in the mid-infrared (MIR; 3-15  $\mu$ m) $^{76,77}$ . In addition, these waveguide structures have already been evolved into long-wavelength Mach-Zehnder interferometers (MZI) facilitating chem/bio sensing and providing optimized chip-integrated sensing platforms in combination with quantum cascade lasers $^{77-79}$ .

Interferometric chem/bio sensing may be realized via different optical configurations, as mentioned above. Classical as well as non-classical arrangements comprise Michelson, Sagnac, Fabry-Pérot  $^{80}$  or MZI schemes, which are commonly realized via conventional bulk optics  $^{81,82}$ . MZIs are intrinsically most suitable for integration into on-chip photonic circuits and have been demonstrated useful for sensing strategies using classical light in the visible, NIR and MIR spectral window  $^{78,83-85}$ . Major differences are that one-port-based designs achieve beam splitting via Y-branching, while two-port-based designs depend on evanescent field coupling  $^{86}$  or multimode interference couplers.

MZIs are readily designed for two or more wavelength demultiplexing via single MZIs and cascaded setups or may even comprise non-linear optical elements, e.g., Kerr lenses  $^{87}$  for intensity splitting or as optical switches. Thermo-optical, electro-optical or all-optical operation has been shown for altering the refractive index at high speed of such devices  $^{88}$ .

The fundamental signal generating process in a classical MZI used in a chem/bio sensing scenario relies on simple wave interference. Laser-light at a wavelength of  $\lambda$  and an intensity of  $I_0$  is divided into two equal beams propagating along two waveguide arms leading to interference when recombined.

An active sensing area defined via the sensing window of a length  $L$  along one of the interferometer arms will result in a variation of the effective refractive index  $n_{\mathrm{eff}}$  via interactions between the deposited chem/bio molecules and the evanescent light-field. Hence, within this area a phase difference  $\Delta \varphi$  between the photons travelling in the sensor arm (S) vs. the photons traveling in the reference arm (R) is induced. Upon reuniting these two beams on the second beam splitter of the MZI a changing interference pattern is generated. The theoretical description of the detectable light intensity  $I$  measured on one output port is given by the interference equation  $I = \frac{1}{2} I_0 \left[ 1 + \cos \left( L \cdot 2\pi \frac{\Delta n_{\mathrm{eff}}}{\lambda} \right) \right]$ . The phase difference is given by  $\Delta \varphi = L \cdot 2\pi \frac{\Delta n_{\mathrm{eff}}}{\lambda}$ . As evident from the interference equation, complete constructive interference is achieved for integer multiples of  $\lambda$ , whereas complete destructive interference appears for odd integer multiples of  $\lambda / 2$ .

The interaction path length  $L$  must be precisely controlled to ensure a reliable phase estimation. As shown in Fig. 7 a), an elongation of the interaction path length  $L$  decreases the oscillation period of the MZI light output across a certain range of the analyte media refractive index, and likewise increases the accompanying phase shift of the sensing vs. the reference arm. This enables a more precise evaluation of changes of the effective refractive index and therefore, the discrimination of minute concentration changes resulting in lower limits of detection for chem/bio sensing schemes<sup>89</sup>. Since a well-defined interaction path length is essential for deriving quantitative analytical signals, the active sensing region along the sampling arm of the MZI (S) should be photolithographically defined by protecting the entire chip excluding the active sensing region with  $\mathrm{SiO}_2$ , SU-8, PMMA or any other material that is compatible (i.e., non-absorbing) at the

# Analyst

operation wavelength of the MZI. This is of importance for MZIs operating in the NIR and MIR spectral window, as a wide variety of commonly used protective materials (e.g., polymers) strongly absorb in these wavelength windows.

Such classical, optical lab-on-chip concepts using silicon photonics for biosensing and operating in the visible spectral regime have been shown by the research groups of Huang  $^{90}$ , Lechuga  $^{91-94}$ , and Toccafondo  $^{95}$ . These sensors are based on the phase estimation via slow, yet highly controlled changes of the refractive index of analyte solutions within microfluidic channels and allow the direct correlation of phase shifts with analyte concentrations without prior knowledge on the actual refractive index.

For chem/bio sensing concepts based on non-classical light, the measurement concept must be adapted, since coincidence rates have to be recorded rather than output intensities, thereby resulting in a necessity for single-photon detectors to demonstrate quantum mechanical interference. Considering a NOON state  $\frac{1}{\sqrt{2}}\big(|2,0\rangle_{A,B} + |0,2\rangle_{A,B}\big)$  were all photons in path B acquire a phase shift of  $\Delta \varphi$  due to a sensing area, which results in  $\frac{1}{\sqrt{2}}\big(|2,0\rangle_{A,B} + e^{i2\Delta \varphi}|0,2\rangle_{A,B}\big)$ . If this state is send onto a beam splitter with input ports A and B and the two-fold coincidence  $C_2$  is measured at one output port,  $C_2 = \frac{1}{2} +\frac{1}{2}\cos \left(L\cdot 2\cdot 2\pi \frac{\Delta n_{eff}}{\lambda}\right)$  is achieved in the ideal case ( $V_{HOM} = 1$ ). This implies that the coincidence rate oscillates two times faster than the measured intensity in the classical case. For a NOON state with  $N = 3$ , the three-fold coincidence rate oscillates three times faster and so on (Fig. 7 b). As already pointed out in the introduction, this faster oscillation itself is no proof for super-sensitivity, rather than the contrast of the super-resolution fringes  $^{16}$ . A chem/bio sensing scenario exhibiting super-sensitivity is potentially reaching the Heisenberg limit at ideal conditions, and therefore may be finally outperforming the SQL  $^{96-98}$

![](images/5487be529d486c4a071b97112340686147ab24ddf76df2f2eb2b3a7beaec716a.jpg)

![](images/6121ed3b6a7646cdf1ee2f42a2a35441a94c8d071c041e146798c8bd01c25d27.jpg)  
Fig. 7 a) Calculated MZI signal for GaAs  $(n_{\mathrm{eff}} = 3.39)$  waveguides at a wavelength of  $900~\mathrm{nm}$  for different lengths of the active sensing region along the sampling arm (S) of the MZI illustrating the oscillation for  $\mathsf{L} = 1$  mm (blue) vs.  $\mathsf{L} = 100\mu \mathsf{m}$  (red). b) Calculated MZI coincidence count output signal for the system shown in A) at  $\mathsf{L} = 100\mu \mathsf{m}$  along with the expected acceleration of the signal oscillation for entangled systems  $(N = 1, N = 2, N = 4)$ .

Commonly, detection limits of refractive-index-based sensors are given in fractions of refractive index units (RIU) that can be discriminated. Typical values of  $10^{-7}$  RIU $^{94}$ , which refer to analyte concentrations down to the pg mL $^{-1}$  scale are already reached with optical sensor devices using classical light.

However, with an interferometric scheme reaching supersensitivity improvements are anticipated for measurements at low intensity, i.e., at a few-photon level. In addition, utilizing quantum states enables significant sensitivity enhancements of such sensors, while preserving device dimensions and radiation intensity at the sample, e.g., when studying photosensitive analytes. From the definition of the standard quantum limit, it is evident that the precision of the phase may be arbitrarily small by just increasing the power. Therefore, analytical measurements using N00N states are mainly relevant, if the optical power is or has to be limited, e.g., considering a damage threshold of the sample.

As an example, proteins have been probed via an opto-fluidic device by Crespy et al. (Fig. 8) using entangled photons at a wavelength of  $785~\mathrm{nm}$ , which were created via parametric down conversion in a nonlinear bismuth borate  $\mathrm{BiB}_3\mathrm{O}_6$  (BiBO) crystal. However, the standard quantum limit was not surpassed in these experiments[99,100].

![](images/4a1569f8200ba8d75dbe7c7fc98ebb145d4a031177db4e0988f541de241ce650.jpg)

![](images/1d11948301c20b25d2c09016b00615ce7c9030f37f1a97367657f4b2aeb5d68e.jpg)  
Fig. 8 a) and b) schematic setup, c) and d) images of an opto-fluidic assembly for analyzing the concentration of proteins via entangled photons, as presented by Crespy et al. Reprinted with permission from © 2012 American Institute of Physics.

![](images/cb6052ee3f76fa2d995affacf23f64b962ed6b6ffa01b3f6d76711dddd2b7bd0.jpg)

![](images/5400acb9d6070d09e1a779d8105b3e217cbaa124cca7548b6d3fad7a61926c3a.jpg)

# WAVEGUIDE SURFACE MODIFICATION FOR CHEM/BIO SENSING

Sensing of biomolecules usually requires exceptional sensitivity. For example, direct access to the aggregation state of proteins is of utmost importance for almost any kind of neurodegenerative disease, which are commonly associated with the accumulation, secondary structure changes, and/or aggregation of specific biomarker proteins. Some examples include prion proteins, which give rise to the Creutzfeld-Jacob syndrome (a.k.a., mad cow disease) or  $\alpha$ -synuclein, which is gaining relevance as a potential biomarker for Parkinson's disease  $^{101-106}$ . Next to the intracellular accumulation of  $\alpha$ -synuclein inside Lewy bodies and Lewy neurites in the brain, which may only be accessed post mortem, this protein has been detected - albeit at very low concentrations (i.e., few ng/L) - within the cerebrospinal fluid (CSF) of patients, and has since been associated with the disease status. Hence, the development of ultra-sensitive and ideally label-free detection schemes for analyzing secondary structure changes and/or aggregation states of such proteins in CSF within minute sample volumes (i.e., few  $\mu$ L) and at extremely low concentrations is among the most demanded assay strategies in early neurodegenerative disease detection, disease progression monitoring, and potentially for accompanying therapy strategies  $^{107-110}$ .

For interferometric sensing of biomolecules such as proteins via N00N states, inorganic semiconductor materials including, e.g., GaAs serving as the waveguide must be efficiently decorated with a chem/bio sensing architecture at the surface, which ensures target-specific changes of the refractive index. In addition, appropriate analyte capture for achieving the anticipated sensitivity via a combination of quantum sensing principles and analyte enrichment for the detection of such biomarkers at relevant concentrations in biofluids is demanded. Finally, degradation of the transducer surface and accompanying leakage of potentially toxic degradation products needs to be avoided via appropriate coating strategies.

For GaAs, different surface immobilization/modification routes (Fig. 9) have been described in literature  $^{111}$ . Self-assembled monolayers (SAMs) based on short organic thiolates  $^{112,113}$  or long chained polymers  $^{85}$  have been applied to protect GaAs surfaces, and for immobilizing molecular recognition motifs such as aptamers.

![](images/f75b86c2d7caba54fdde654bc0e632c49db0491872812f1d460a43e94cc56b54.jpg)  
Fig. 9 Schematic work flow for immobilizing a biomolecular recognition scheme at the surface of an interferometer arm acting as the active 'sensing window' via a microfluidic architecture at the CBSC. a-b) Oxide removal step. b-c) Immobilization of the molecular recognition layer, e.g., via thiol attachment chemistry (i.e., self-assembly processes). c-d) Measurement of the actual target analyte via the recognition/capture layer (interacting radiation is indicated with red arrows). After analyte recognition/capture, the sensor surface may be regenerated to the states a), b), or c) depending on the applied chemistry. For clarity and comprehensibility, the actual top surface of the flow cell enclosing the microfluidic channel is not shown.

As an alternative for surface protection, atomic layer deposition (ALD) has recently been applied to establish thin layers of, e.g.,  $\mathrm{Al}_{2}\mathrm{O}_{3}$  on GaAs  $^{114}$ . However, GaAs substrates require oxide removal steps prior to any surface modification and subsequent suppression of oxide regrowth during further surface modification steps. Hence, fully integrated CBSCs comprising structured waveguides covered with protective coatings and microfluidic channels are useful for both in-situ surface modification and subsequent liquid phase sensing.

# CONCLUSIONS

Given recent progress in the practical utility of non-classical light for quantum sensing, viable strategies and challenges towards quantum interferometric sensing schemes for ultra-sensitive chem/bio sensing scenarios, providing analytical signals beyond the standard quantum limit need to be debated. The development of waveguide-embedded quantum dots serving as on demand single-photon source to produce entangled photons facilitates on-chip integration of the entire optical circuitry required for such sensing schemes. Consequently, efficient generation, coupling, propagation, and detection of coherent quantum states, as already shown for bulk optics, may be entirely replaced by on-chip photonics. Therefore, III-V semiconductors represents a platform were the integration of quantum dots is directly possible.

For achieving these goals, and since quantum dots as non-classical light sources still require operation at cryogenic temperatures, separation into a cooled light source chip (LSC) and a chem/bio sensing chip (CBSC) is a promising strategy. Combining these chips via fiber-optic coupling essentially yields Mach-Zehnder-type interferometer structures facilitating chem/bio sensing via quantum

# Analyst

interferometric sensing. It is anticipated that integrated photonics will particularly benefit the on-demand generation of entangled states/N00N-states, efficient light guiding, and fiber-optic coupling. Thereby, decoherence may be minimized while efficient optical signal transduction via the evanescent field emanating at the sensing arm surface of such MZI structures is enabled. Finally, a variety of relevant chem/bio sensing scenarios such as label-free rare biomarker detection in biofluids may benefit from the yet unprecedented sensitivity promised by optical sensing platforms smartly combining non-classical light with advanced molecular recognition motifs. Consequently, sophisticated quantum sensing schemes utilizing integrated photonics may yield a new generation of cost effective and robust chem/bio sensing platforms contributing to the recent trends in precision medicine by revolutionizing point-of-care (POC) and personalized biodiagnostics.

# ACKNOWLEDGEMENTS

This study has in part been funded by the European Union's Seventh Framework Programme managed by REA Research Executive Agency http://ec.europa.eu/rea (FP7/2007-2013) under Grant Agreement No. 314018 FP7-SME-2012-SME (MYCOSPEC). Furthermore, the authors gratefully acknowledge partial support by the Kompetenznetz Funktionelle Nanostrukturten Baden Württemberg, Germany, and by the Center for Integrated Quantum Science and Technology (IQST), Ulm University, University of Stuttgart, and MPI for Solid State Research, Germany. Furthermore, the Focused Ion Beam Center UUIm supported by the FEI Company (Eindhoven, The Netherlands), the German Science Foundation (INST40/385-F1UG), and the Struktur- und Innovationsfonds Baden-Württemberg are thanked.

# REFERENCES

1 M. Zwierz, C. A. Pérez-Delgado and P. Kok, Phys. Rev. A, 2012, 85, 42112.  
2 R. Demkowicz-Dobrzanski, U. Dorner, B. J. Smith, J. S. Lundeen, W. Wasilewski, K. Banaszek and I. A. Walmsley, Phys. Rev. A, 2009, 80, 13825.  
3 E. Oelker, G. Mansell, M. Tse, J. Miller, F. Matichard, L. Barsotti, P. Fritschel, D. E. McClelland, M. Evans and N. Mavalvala, Optica, 2016, 3, 682-685.  
4 The LIGO Scientific Collaboration, Nat. Photonics, 2013, 7, 613-619.  
5 L. Pezzé and A. Smerzi, Phys. Rev. Lett., 2008, 100, 73601.  
6 M. A. Taylor, J. Janousek, V. Daria, J. Knittel, B. Hage, H.-A. Bachor and W. P. Bowen, Nat. Photonics, 2012, 7, 299.  
7 K. Goda, O. Miyakawa, E. E. Mikhailov, S. Saraf, R. Adhikari, K. McKenzie, R. Ward, S. Vass, A. J. Weinstein and N. Mavalvala, Nat. Phys., 2008, 4, 472-476.  
8 R. Schnabel, Nat. Phys., 2008, 4, 440-441.  
9 M. A. Taylor and W. P. Bowen, Phys. Rep., 2016, 615, 1-59.  
10 J.P.Dowling,Contemp.Phys.,2008,49,125-143.

11 T. Nagata, R. Okamoto, J. L. O'brien, K. Sasaki and S. Takeuchi, Science, 2007, 316, 726-729.  
12 V. Giovannetti, S. Lloyd and L. Maccone, Nat. Photonics, 2011, 5, 222-229.  
13 M. W. Mitchell, J. S. Lundeen and a M. Steinberg, Nature, 2004, 429, 161-164.  
14 K. J. Resch, K. L. Pregnell, R. Prevedel, a. Gilchrist, G. J. Pryde, J. L. O'Brien and a. G. White, Phys. Rev. Lett., 2007, 98, 2-5.  
15 N. Thomas-Peter, B. J. Smith, A. Datta, L. Zhang, U. Dorner and I. A. Walmsley, Phys. Rev. Lett., 2011, 107, 113603.  
16 M. Müller, H. Vural, C. Schneider, A. Rastelli, O. G. Schmidt, S. Hofling and P. Michler, Phys. Rev. Lett., 2017, 118, 257402.  
17 A. V Kuhlmann, J. H. Prechtel, J. Houel, D. Reuter, A. D. Wieck and R. J. Warburton, Nat. Commun., 2015, 6, 8204.  
18 M. N. Makhonin, J. E. Dixon, R. J. Coles, B. Royall, I. J. Luxmoore, E. Clarke, M. Hugues, M. S. Skolnick and A. M. Fox, Nano Lett., 2014, 14, 6997-7002.  
19 U. Rengstl, M. Schwartz, T. Herzog, F. Hargart, M. Paul, S. L. Portalupi, M. Jetter and P. Michler, Appl. Phys. Lett., 2015, 107, 21101.  
20 N. Prtljaga, R. J. Coles, J. O'Hara, B. Royall, E. Clarke, A. M. Fox and M. S. Skolnick, Appl. Phys. Lett., 2014, 104, 231107.  
21 J. Carolan, C. Harrold, C. Sparrow, E. Martin-Lopez, N. J. Russell, J. W. Silverstone, P. J. Shadbolt, N. Matsuda, M. Oguma, M. Itoh, G. D. Marshall, M. G. Thompson, J. C. F. Matthews, T. Hashimoto, J. L. O'Brien and A. Laing, Science, 2015, 349, 711-716.  
22 P. Michler, A. Kiraz, C. Becher, W. V Schoenfeld, P. M. Petroff, L. Zhang, E. He and A. Imamoglu, Science, 2000, 290, 2282-2285.  
23 A. Scherer, B. C. Sanders and W. Tittel, Opt. Express, 2011, 19, 3004-3018.  
24 N. Gisin, G. Ribordy, W. Tittel and H. Zbinden, Rev. Mod. Phys., 2002, 74, 145-195.  
25 D. Drassani, S. Azzini, M. Liscidini, M. Galli, M. J. Strain, M. Sorel, J. E. Sipe and D. Bajoni, Optica, 2015, 2, 88-94.  
26 P. G. Kwiat, K. Mattle, H. Weinfurter and A. Zeilinger, Phys. Rev. Lett., 1995, 75, 4337-4341.  
27 R.M.Camacho,Opt.Express,2012,20,21977.  
28 S. Barz, G. Cronenberg, A. Zeilinger and P. Walther, Nat. Photonics, 2010, 4, 553-556.  
29 M. W. Mitchell, J. S. Lundeen and A. M. Steinberg, Nature, 2004, 429, 161.  
30 D. Bouwmeester, Nature, 2004, 429, 139-141.  
31 P. Walther, J.-W. Pan, M. Aspelmeyer, R. Ursin, S. Gasparoni and A. Zeilinger, Nature, 2004, 429, 158-161.  
32 A. J. Bennett, J. P. Lee, D. J. P. Ellis, T. Meany, E. Murray, F. F. Floether, J. P. Griffiths, I. Farrer, D. A. Ritchie and A. J. Shields, Sci. Adv., 2016, 2, e1501256-e1501256.

# MINIREVIEW

33 I. Afek, O. Ambar and Y. Silberberg, Science, 2010, 328, 879-881.  
34 N. C. Harris, D. Grassani, A. Simbula, M. Pant, M. Galli, T. Baehr-Jones, M. Hochberg, D. Englund, D. Bajoni and C. Galland, Phys. Rev. X, 2014, 4, 41047.  
35 A. Dutt, K. Luke, S. Manipatruni, L. Gaeta, P. Nussenzveig and M. Lipson, 2015, 4, 1-7.  
36 N. Akopian, N. H. Lindner, E. Poem, Y. Berlatzky, J. Avron, D. Gershoni, B. D. Gerardot and P. M. Petroff, Phys. Rev. Lett., 2006, 96, 130501.  
37 R. J. Young, R. M. Stevenson, P. Atkinson, K. Cooper, D. A. Ritchie and A. J. Shields, New J. Phys., 2006, 8, 29-29.  
38 R. J. Young, R. M. Stevenson, P. Atkinson, K. Cooper, D. a Ritchie and A. J. Shields, in Conference on Lasers and Electro-Optics, 2006, pp. 1-9.  
39 G. Juska, V. Dimastrodonato, L. O. Mereni, A. Gocalinska and E. Pelucchi, Nat. Photonics, 2013, 7, 527-531.  
40 S. Ates, S. M. Ulrich, a. Ulhaq, S. Reitzenstein, a. Löffler, S. Höfling, a. Forchel and P. Michler, Nat. Photonics, 2009, 3, 724-728.  
41 M. Müller, S. Bounouar, K. D. Jönns, M. Glässl and P. Michler, Nat. Photonics, 2014, 8, 224-228.  
42 M. Ghali, K. Ohtani, Y. Ohno and H. Ohno, Nat. Commun., 2012, 3, 661.  
43 F. Hargart, C. a. Kessler, T. Schwarzbäck, E. Koroknay, S. Weidenfeld, M. Jetter and P. Michler, Appl. Phys. Lett., 2013, 102, 11126.  
44 J. Claudon, J. Bleuse, N. S. Malik, M. Bazin, P. Jaffrennou, N. Gregersen, C. Sauvan, P. Lalanne and J.-M. Gérard, Nat. Photon., 2010, 4, 174-177.  
X. Ding, Y. He, Z. C. Duan, N. Gregersen, M. C. Chen, S. Unsleber, S. Maier, C. Schneider, M. Kamp, S. Hofling, C. Y. Lu and J. W. Pan, Phys. Rev. Lett., 2016, 116, 1-6.  
46 O. Gazzano, S. Michaelis de Vasconcellos, C. Arnold, a Nowak, E. Galopin, I. Sagnes, L. Lanco, a Lemaitre and P. Senellart, Nat. Commun., 2013, 4, 1425.  
47 N. Somaschi, V. Giesz, L. De Santis, J. C. Loredo, M. P. Almeida, G. Hornecker, S. L. Portalupi, T. Grange, C. Anton, J. Demory, C. Gomez, I. Sagnes, N. D. L. Kimura, A. Lemaitre, A. Auffeves, A. G. White, L. Lanco and P. Senellart, Nat. Photonics, 2015, 10, 1-6.  
48 S. Unsleber, Y.-M. He, S. Gerhardt, S. Maier, C.-Y. Lu, J.-W. Pan, N. Gregersen, M. Kamp, C. Schneider and S. Höfling, Opt. Express, 2016, 24, 8539.  
49 Y.-M. He, Y. He, Y.-J. Wei, D. Wu, M. Atature, C. Schneider, S. Hofling, M. Kamp, C.-Y. Lu and J.-W. Pan, Nat. Nanotechnol., 2013, 8, 213-7.  
50 S. Ates, S. M. Ulrich, S. Reitzenstein, A. Löffler, A. Forchel and P. Michler, Phys. Rev. Lett., 2009, 103, 167402.  
51 H. Kamada, H. Gotoh, J. Temmyo, T. Takagahara and H. Ando, Phys. Rev. Lett., 2001, 87, 246401.  
52 M. Wiesner, W.-M. Schulz, E. A. Angelopoulos, J. N. Burghartz, J.

Werner, M. Oehme, J. Schulze, R. Roßbach, M. Jetter, P. Michler, J. Ihm and H. Cheong, in AIP Conference Proceedings, 2011, vol. 1399, pp. 261-262.  
53 J. J. Lillie, M. A. Thomas, N. M. Jokerst, S. E. Ralph, K. A. Dennis and C. L. Henderson, J. Opt. Soc. Am. B-Optical Phys., 2006, 23, 642-651.  
54 M. Oehme, J. Werner, M. Jutzi, G. Wöhl, E. Kasper and M. Berroth, Thin Solid Films, 2006, 508, 393-395.  
55 H. Lee, P. Kok, N. J. Cerf and J. P. Dowling, Phys. Rev. A, 2002, 65, 1-4.  
56 P. Kok, H. Lee and J. P. Dowling, Phys. Rev. A, 2002, 65, 1-5.  
57 J. Fulconis, O. Alibart, W. J. Wadsworth and J. G. Rarity, New J. Phys., 2007, 9, 1-15.  
58 A. V Rylyakov, C. L. Schow, B. G. Lee, W. M. J. Green, S. Assefa, F. E. Doany, M. Yang, J. Van Campenhout, C. V Jahnes, J. A. Kash and Y. A. Vlasov, IEEE J. Solid-State Circuits, 2012, 47, 345-354.  
59 T. Goh, M. Yasu, K. Hattori, A. Himeno, M. Okuno and Y. Ohmori, J. Light. Technol., 2001, 19, 371-379.  
60 J. W. Silverstone, D. Bonneau, K. Ohira, N. Suzuki, H. Yoshida, N. Iizuka, M. Ezaki, C. M. Natarajan, M. G. Tanner, R. H. Hadfield, V. Zwiller, G. D. Marshall, J. G. rarity, J. L. O'Brien and M. G. Thompson, Nat. Photonics, 2013, 8, 104-108.  
61 S. Kalliakos, Y. Brody, A. J. Bennett, D. J. P. Ellis, J. Skiba-Szymanska, I. Farrer, J. P. Griffiths, D. A. Ritchie and A. J. Shields, Appl. Phys. Lett., 2016, 109, 151112.  
62 J. Cardenas, C. B. Poitras, J. T. Robinson, K. Preston, L. Chen and M. Lipson, Opt. Express, 2009, 17, 4752.  
63 M. Schwartz, U. Rengstl, T. Herzog, M. Paul, J. Kettler, S. L. Portalupi, M. Jetter and P. Michler, Opt. Express, 2016, 24, 3089.  
64 J. Wang, A. Santamato, P. Jiang, D. Bonneau, E. Engin, J. W. Silverstone, M. Lerner, J. Beetz, M. Kamp, S. Hofling, M. G. Tanner, C. M. Natarajan, R. H. Hadfield, S. N. Dorenbos, V. Zwiller, J. L. O'Brien and M. G. Thompson, Opt. Commun., 2014, 327, 49-55.  
65 J. Jeske, J. H. Cole and S. F. Huelga, New J. Phys., 2014, 16, 73039.  
66 T. Caneva, T. Calarco and S. Montangero, New J. Phys., 2012, 14, 93041.  
67 W. H. P. Pernice, C. Schuck, O. Minaeva, M. Li, G. N. Goltsman, A. V. Sergienko and H. X. Tang, Nat. Commun., 2012, 3, 1325.  
68 C. Schuck, W. H. P. Pernice and H. X. Tang, Sci. Rep., 2013, 3, 1893.  
69 J. P. Sprengers, A. Gaggero, D. Sahin, S. Jahanmirinejad, G. Frucci, F. Mattioli, R. Leoni, J. Beetz, M. Lerner, M. Kamp, S. Hofling, R. Sanjines and A. Fiore, Appl. Phys. Lett., 2011, 99, 181110.  
T. Gerrits, N. Thomas-Peter, J. C. Gates, A. E. Lita, B. J. Metcalf, B. Calkins, N. A. Tomlin, A. E. Fox, A. L. Linares, J. B. Spring, N. K. Langford, R. P. Mirin, P. G. R. Smith, I. A. Walmsley and S. W. Nam, Phys. Rev. A - At. Mol. Opt. Phys., 2011, 84, 1-8.  
71 A.W.Sleight,Acc.Chem.Res.,1995,28,103-108.  
72 X. Sun, J. B. Abshire and J. D. Beck, Porc. SPIE, 2014, 9114, 91140K.

# Analyst

73 H. Mohseni, V. Fathipour and S. J. Jang, SPIE Newsroom, 2014, 2-4.  
74 V. Fathipour, O. G. Memis, Sung Jun Jang, R. L. Brown, I. H. Nia and H. Mohseni, IEEE J. Sel. Top. Quantum Electron., 2014, 20, 65-70.  
75 R. Soref, IEEE J. Sel. Top. Quantum Electron., 2006, 12, 1678-1687.  
76 X. Wang, S.-S. Kim, R. Roßbach, M. Jetter, P. Michler and B. Mizaikoff, Analyst, 2012, 137, 2322-2327.  
77 M. Sieger, J. Haas, M. Jetter, P. Michler, M. Godejohann and B. Mizaikoff, Anal. Chem., 2016, 88, 2558-2562.  
78 M. Sieger, F. Balluff, X. Wang, S. Kim, L. Leidner, G. Gauglitz and B. Mizaikoff, Anal. Chem., 2013, 85, 3050-3052.  
79 M. Sieger and B. Mizaikoff, Photon. Res., 2016, 4, 106-110.  
80 J. H. Jerman and D. J. Clift, in TRANSDUCERS '91: 1991 International Conference on Solid-State Sensors and Actuators. Digest of Technical Papers, IEEE, pp. 372-375.  
81 T. Schubert, N. Haase, H. Kück and R. Gottfried-Gottfried, Sensors And Actuators, 1997, 60, 108-112.  
82 G. B. Lemos, V. Borish, G. D. Cole, S. Ramelow, R. Lapkiewicz and A. Zeilinger, Nature, 2014, 512, 409-412.  
83 C. Charlton, M. Giovannini, J. Faist and B. Mizaikoff, *Anal. Chem.*, 2006, 78, 4224-4227.  
84 B. Mizaikoff, Chem. Soc. Rev., 2013, 42, 8683-99.  
85 L. Leidner, M. Ewald, M. Sieger and B. Mizaikoff, Proc. SPIE, 2013, 8774, 1-15.  
86 J.-R. Chang Chien, C.-C. Liu, C.-J. Wu, P. Y. Wu and C. C. Li, Prog. Electromagn. Res., 2012, 124, 71-83.  
87 B.C.Sanders,Phys.Rev.A,1992,45,6811-6815.  
88 H. S. Jung, J. Opt. Soc. Korea, 2012, 16, 47-52.  
89 W. B. Li, P. N. Segre, R. W. Gammon, J. V. Sengers and M. Lamvik, J. Chem. Phys., 1994, 101, 5058.  
90 M. I. Lapsley, I.-K. Chiang, Y. B. Zheng, X. Ding, X. Mao and T. J. Huang, Lab Chip, 2011, 11, 1795.  
91 K. Zinoviev, L. G. Carrascosa, B. Sep, C. Dom and L. M. Lechuga, Adv. Opt. Technol., 2008, 2008, 1-6.  
92 B. Sepúlveda, J. S. Del Río, M. Moreno, F. J. Blanco, K. Mayora, C. Dominguez and L. M. Lechuga, J. Opt. A Pure Appl. Opt., 2006, 8, S561-S566.  
93 L. M. Lechuga, Proc. SPIE, 2004, 5357, 96-110.  
94 M.-C. Estevez, M. Alvarez and L. M. Lechuga, *Laser Photon. Rev.*, 2012, 6, 463-487.  
95 V. Toccafondo and C. J. Oton, Photon. Res., 2016, 4, 57-60.  
96 A. Kuzmich and L. Mandel, Quantum Semiclassical Opt. J. Eur. Opt. Soc. Part B, 1998, 10, 493-500.  
97 C.M.Caves,Phys.Rev.D1981,23,1693-1708.  
98 M. A. Taylor and W. P. Bowen, Phys. Rep., 2016, 615, 1-59.

99 A. Crespi, M. Lobino, J. C. F. Matthews, A. Politi, C. R. Neal, R. Ramponi, R. Osellame and J. L. O'Brien, Appl. Phys. Lett., 2012, 100, 233704.  
100 A. Crespi, Y. Gu, B. Ngamsom, H. J. W. M. Hoekstra, C. Dongre, M. Pollnau, R. Ramponi, H. H. van den Vlekkert, P. Watts, G. Cerullo and R. Osellame, Lab Chip, 2010, 10, 1167-1173.  
101 A. Nabers, J. Ollesch, J. Schartner, C. Kötting, J. Genius, U. Haußmann, H. Klafki, J. Wiltfang and K. Gerwert, J. Biophotonics, 2015, 1-11.  
102 A. Nabers, J. Ollesch, J. Schartner, C. Kotting, J. Genius, H. Hafermann, H. Klafki, K. Gerwert and J. Wiltfang, Anal. Chem., 2016, 88, 2755-2762.  
103 S. B. Prusiner, A. L. Woerman, D. a. Mordes, J. C. Watts, R. Rampersaud, D. B. Berry, S. Patel, A. Oehler, J. K. Lowe, S. N. Kravitz, D. H. Geschwind, D. V. Glidden, G. M. Halliday, L. T. Middleton, S. M. Gentleman, L. T. Grinberg and K. Giles, Proc. Natl. Acad. Sci., 2015, 201514475.  
104 C.J.R.Dunning,S.George and P.Brundin,Prion,2013,7,92-7.  
105 S. George, N. L. Rey, N. Reichenbach, J. a. Steiner and P. Brundin, Brain Pathol., 2013, 23, 350-357.  
106 L. Breydo, J. W. Wu and V. N. Uversky, Biochim. Biophys. Acta - Mol. Basis Dis., 2012, 1822, 261-285.  
107 P. Wang, W. Bohr, M. Otto, K. M. Danzer and B. Mizaikoff, Anal. Bioanal. Chem., 2015, 407, 4015-4021.  
108 Á. I. López-Lorente and B. Mizaikoff, Anal. Bioanal. Chem., 2016, 2875-2889.  
109 A. Stuendl, M. Kunadt, N. Kruse, C. Bartels, W. Moebius, K. M. Danzer, B. Mollenhauer and A. Schneider, Brain, 2016, 139, 481-494.  
110 K. M. Danzer, S. K. Krebs, M. Wolff, G. Birk and B. Hengerer, J. Neurochem., 2009, 111, 192-203.  
111 C. Kirchner, M. George, B. Stein, W. Parak, H. Gaub and M. Seitz, Bayreuth Polym. Symp. Int. Symp. Funct. Struct. Polym. Mater., 2001, 266-276.  
112 K. Adlkofer and M. Tanaka, Longmuir, 2001, 17, 4267-4273.  
113 K. Adlkofer, M. Tanaka, H. Hillebrandt, G. Wiegand, E. Sackmann, T. Bolom, R. Deutschmann and G. Abstreiter, Appl. Phys. Lett., 2000, 76, 3313-3315.  
114 Y. Xuan, H. C. Lin and P. D. Ye, IEEE Trans. Electron Devices, 2007, 54, 1811-1817.

J. Haas received his M.Sc. in chemistry at Ulm University in 2014. Currently, he is a PhD student in the research group of B. Mizaikoff at the Institute of Analytical and Bioanalytical Chemistry at Ulm University. His research interests include infrared reflection absorption spectroscopy, attenuated total reflection spectroscopy, quantum cascade lasers, thin-film waveguide technology, and on-chip integrated photonics.

# MINIREVIEW

M. Schwartz is a PhD student in the group of P. Michler at the Institute of Halbleiteroptik und Funktionelle Grenzflächen at the University of Stuttgart where he also started his scientific career in 2013 with his Master Thesis. He works in the field of quantum photonics by optical investigations of integrated devices with semiconductor quantum dots as single photon emitters.  
U. Rengstl studied physics at the University of Stuttgart and received his Diploma in 2011. He defended his PhD in 2017 and is currently a researcher in the group of P. Michler at the Institut für Halbleiteroptik und Funktionelle Grenzflächen at the University of Stuttgart. His main research interests are the simulation and fabrication of photonic integrated circuits with semiconductor quantum dots as single-photon emitters for integrated quantum optics.  
M. Jetter graduated in Physics at the University of Stuttgart in 1997 and received his Doctoral Degree (Dr. rer. nat.) in 2003 at the  $4^{\text{th}}$  Physics Institute. In 1998 he joined the Universidad Autonoma de Madrid, Spain, as a scientific guest. Since 2003 he is the head of the epitaxy lab of the  $4^{\text{th}}$  Physics Institute, since 2005 of the Institut für Halbleiteroptik und Funktionelle Grenzflächen, respectively. His main research interests are red emitting VCSEL and VECSEL, MOVPE growth of semiconductor nanostructures and quantum dots, Group III-Nitrides, LEDs, laser diodes quantum dot based single photon emitters and photonic integrated circuits.  
P. Michler got his Physics Diploma and his PhD degree from the University of Stuttgart in 1990 and 1994, respectively. He worked as post-doc at the Max-Planck Institute for Solid State Research in Stuttgart from 1994 to 1995. From 1995 to 1999, he was a research group leader at the University of Bremen and from 1999 until 2000 he spent a one year research stay at the University of California, Santa Barbara. In 2001, he performed his Habilitation at the University of Bremen and he became a professor in 2003 at the University of Stuttgart. Since May 2006, he is the head of the Institute for Semiconductor Optics and Functional Interfaces at the University of Stuttgart, concentrating research on quantum dots, quantum optics, non-classical light sources and semiconductor lasers.  
B. Mizaikoff joined the faculty at Ulm University, Germany, as a Chaired Professor and Director at the Institute of Analytical and Bioanalytical Chemistry in 2007 with prior appointments at the Vienna University of Technology (Austria), and at the Georgia Institute of Technology (USA). His research interests focus on optical chem/bio sensors, tailored (bio)molecular recognition interfaces, molecularly imprinted materials, system miniaturization and integration, and multifunctional (nano)analytical techniques with applications in environmental analysis, process monitoring, and biomedical diagnostics.