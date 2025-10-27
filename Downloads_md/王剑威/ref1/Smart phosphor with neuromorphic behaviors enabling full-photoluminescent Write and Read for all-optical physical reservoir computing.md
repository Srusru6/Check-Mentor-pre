# Smart phosphor with neuromorphic behaviors enabling full-photoluminescent Write and Read for all-optical physical reservoir computing

Received: 5 February 2025

Accepted: 28 July 2025

Published online: 13 August 2025

Check for updates

Yifei Zhao  $①$ , Man Li  $②$ , Man Chung Wong  $①$ , Xun Han  $①$ , Feng Guo  $^{1,3}$ , Yuan Liu  $①$ , Xinyue Lao  $①$ , Zhaoying Dang  $^{1,3}$ , Sin-Yi Pang  $①$ , Zehan Wu  $①$ , Shi Ye  $②$  & Jianhua Hao  $①,3,4$

The unprecedented growth in information across diverse media drives an urgent need for multifunctional materials and devices beyond conventional electrical paradigms. This work explores all-optical information processing based on photoluminescence functions using smart phosphor. The developed composite phosphor of mixed-halide perovskite embedded macroporous  $\mathrm{Y}_2\mathrm{O}_3:\mathrm{Eu}^{3+}$  exhibits adaptive photoluminescence variations with neuromorphic characteristics. Theoretical simulations reveal interface-mediated halogen migration processes with progressively evolving energy barriers, underpinning the neuron-like photoluminescence property variations. The system enables full photoluminescence-based Write and Read functionalities for all-optical neuromorphic computing, achieving 4-bit binary sequence discrimination as physical reservoirs. It further demonstrates potential in photoluminescence-based fingerprint authentication with  $94.4\%$  accuracy. This work advances smart phosphor as an alternative approach to neuromorphic computing with optical-stimuli and optical-output. It also opens avenues for designing function-oriented phosphor materials with tailored properties for information science and artificial intelligence applications.

The explosive growth of the Internet of Things has generated unprecedented volumes of data across diverse media, driving an urgent demand for information processing technologies beyond conventional electrical approaches<sup>1,2</sup>. Such demand has accelerated the rapid development of multifunctional materials and devices, particularly those incorporating bio-inspired computing algorithms for enhanced efficiency and adaptability<sup>3-6</sup>. Compared to conventional electrical systems, optical signal processing offers unique advantages such as contactless operations, parallel processing capabilities, and high

information bandwidth $^{7-9}$ . Recent breakthroughs demonstrated that optical computing could achieve complex computations with ultra-low latency and high energy efficiency $^{10,11}$ . Consequently, the emerging multimode computing primarily explores the interplay between electrical and optical modes through four fundamental categories: electrical input-electrical output, optical input-electrical output, electrical input-optical output, and optical input-optical output $^{12}$ . Among these, optoelectronic devices that convert light inputs into electrical signals have achieved widespread practical implementation $^{13-16}$ . The electric-

$^{1}$ Department of Applied Physics, The Hong Kong Polytechnic University, Hong Kong, PR China.  $^{2}$ State Key Laboratory of Luminescent Materials and Devices, Guangdong Provincial Key Laboratory of Fiber Laser Materials and Applied Techniques, South China University of Technology, Guangzhou, PR China.  $^{3}$ The Hong Kong Polytechnic University Shenzhen Research Institute, Shenzhen, PR China.  $^{4}$ Research Centre for Nanoscience and Nanotechnology, The Hong Kong Polytechnic University, Hong Kong, PR China.  $\times$  e-mail: msyes@scut.edu.cn; jh.hao@polyu.edu.hk

field-modulated optical and photoluminescence (PL) response have also exhibited promising potential $^{17-20}$ . However, the development of all-optical devices operating solely through light excitation and PL emission remains largely underexplored.

Phosphors with multimodal luminescence have long been recognized as critical components for information security, sensing, and storage[21-24]. These applications exploit static multiplexity or reversible luminescence variations against external stimuli, giving rise to the concept of smart phosphor[25]. However, there is a pressing need to push the boundaries of these materials beyond simple stimulus-response mechanisms, and to exploit more sophisticated functionalities. Recent advances have revealed synaptic-like characteristics in persistent luminescence (PersL), triplet excitonic emission, and photon-avalanche (PA) upconversion (UC), which stem from excited-state manipulations and subsequent luminescence decay[26-28]. These PL-based functions are limited by continuous post-stimulation decay, lacking an independent and on-demand Read mechanism. While biological systems do not explicitly feature Read operations, practical electronic and photonic devices have incorporated distinct Read functions to enhance data retrieval and streamline computation[29-32]. Existing phosphor systems operate in a Write-only mode that leads to passive signal broadcasting, resulting in compromised security and heightened interference vulnerability. To achieve practical PL-based neuromorphic computing, it is essential to develop dark PL variations that enable distinct Write and non-destructive Read operations, moving beyond the current mechanisms of excited-state manipulations.

In this context, phosphor composites offer a promising solution through tailored design of components and interfacial effects, which enables sophisticated coupling between stimuli and PL tuning[33]. Our previous work has demonstrated this potential by strategically integrating functional components such as ferroelectric nanomaterials, magnetic phases, and porous hosts[34-38]. Building upon these findings, we engineer a smart phosphor system with neuromorphic PL behaviors constructed on mixed-halide perovskite (MHPe) embedded macroporous  $\mathrm{Y}_2\mathrm{O}_3:\mathrm{Eu}^{3+}$  (MYE). MHPe@MYE demonstrates progressively evolved PL properties variations upon light stimuli. Theoretical simulation reveals that halogen migrations at the interface between MHPe and MYE play a crucial role in the adaptive PL variations under light stimuli. The system enables full PL-based Write and Read processes, while spectral investigations demonstrate rich neuromorphic properties that closely mimic biological synaptic behaviors. Leveraging these features, the PL-based neuromorphic computing capabilities of MHPe@MYE are further evaluated. It achieves 4-bit binary sequence discrimination as a physical reservoir based on optical-stimuli and PL-readouts. The system further demonstrates promising potential in Modified National Institute of Standards and Technology (MNIST) handwritten digit and Sokoto Coventry Fingerprint (SOCOFing) recognition with notable  $94.4\%$  accuracy. This work expands smart phosphor to tailored neuromorphic behaviors, which may pave the way toward all-optical neuromorphic platforms that integrate PL functionality for information processing.

# Results

Construction of smart phosphor with neuromorphic behaviors Biological synapse is the fundamental unit of neural information processing, which consists of presynaptic and postsynaptic terminals separated by a synaptic cleft (Fig. 1a). This intricate structure facilitates neurotransmitter-mediated communication, inspiring computational models that emulate synaptic plasticity and adaptability for more efficient information processing $^{39,40}$ . PL-based neuromorphic computing offers potential advantages over electrical and optoelectrical systems including high information bandwidth and visualizable results. However, most existing PL-based neuromorphic systems are constructed upon certain photophysical processes $^{26-28}$ . Their

continuous decay characteristic poses significant challenges in further developments, particularly in terms of parallelism and information security. To better address these challenges, we categorize current PL-based neuromorphic phosphor systems into two types: Decay-type, constructed upon certain photophysics phenomena with synaptic post-stimulation PL signal, leading to passive Write-only operations; Variation-type, exhibit history-dependent PL properties variations in dark states originated from light-induced material reconfigurations, which enables discrete Write and Read operations.

Such integration of Read operation in PL-based systems fundamentally relies on materials whose light-induced property changes can give rise to PL variations with neuromorphic characteristics, together with a non-destructive probing mechanism to read out the current PL state. The potential advantages and importance of developing Read operation in PL-based neuromorphic systems are discussed in Supplementary Note 1, illustrating that the proposed variation-type may align more closely to the requirements for practical PL-based neuromorphic computing.

To actualize this conceptual framework, we develop MHPe@MYE smart phosphor with porous composite structure (Fig. 1b). The rich interfacial interactions within MHPe@MYE enable light-induced PL properties variations and recovery in dark states, giving rise to dynamics PL features (black dot line) and on-demand Read operations (lavender arrows) as illustratively plotted in Fig. 1c. This adaptive variation is primarily attributed to light-induced halogen migration at the interfaces within MHPe@MYE. Fig. 1d presents a flow diagram of the microscopic mechanisms upon high-energy Write, dark recovery, and low-energy Read, corresponding to the frames tagged 1-5 in Fig. 1c. Starting from interfacial regions containing defective MHPe and Br/Cl-anchored MYE surface (Frame 1), the adsorbed halogen species (Br/Cl) would migrate to MHPe under intense Write light stimulation (Frame 2). It results in altered halogen composition and defect passivation of MHPe, consequently modifying its PL properties. Upon removal of the light stimulus, the PL properties gradually recover in dark states due to reverse migration of halogen species (Frame 3). For implementing Read operation, low-energy probing light is employed, which does not induce further PL variation, thus allowing for non-destructive probing of the current PL state (Frame 4). The system could return to its initial state after long-term resting (Frame 5). This reversible process facilitates effective Write and Read operations, underpinning the neuromorphic functionality of MHPe@MYE for PL-based information processing. Meanwhile, the inert  $\mathrm{Eu}^{3+}$  luminescence from MYE host can further serve as a baseline for calibrating the PL readouts.

MHPe@MYE is synthesized following the hard-templated sol-gel procedure $^{37}$ . Aligned with our design, the kinetic PL mapping of MHPe@MYE under continuous  $360~\mathrm{nm}$  laser excitation (Fig. 1e) shows characteristic PL variations featuring a red-shifted and drastically enhanced PL intensity at the green region (cycled by blue dot lines), as well as a steady  $\mathrm{Eu}^{3+}$  peak at around  $613~\mathrm{nm}$  (marked by pink dot lines). The decay process of the PL states can be probed using low-energy Read excitation in non-destructive way (Fig. 1f). Read excitation also reveals the initial PL characteristics featuring a weak peak at  $470~\mathrm{nm}$  from defect-rich and Cl-rich MHPe (Supplementary Fig. 2). Using alternating  $360~\mathrm{nm}$  laser illumination as Write and weak  $365~\mathrm{nm}$  excitation as Read, the PL dynamics of MHPe@MYE are investigated. As shown in Fig. 1g, it shows an enhancing PL intensity upon Write excitations, consistent with the kinetic PL mapping results. Multiple cycles of alternating Write and Read operations reveal consistent recovery endpoints during Read and starting points of subsequent Write processes (marked by green dot lines). Similarly, consistency is observed between orange dot lines marking the end of Write and the start of Read operations. These consistencies confirm equivalent PL states at these critical points, despite different PL intensities during Write and Read conditions. It ensures the foundation for reliable operations in MHPe@MYE artificial synapses.

![](images/37a7c916cf4f9091cf1263ea1d3e44571c9f750c0d9cfc0740391c4a34c4da84.jpg)

![](images/a30277ef50ec4023c11993b42a14ab34ce51d684d363e2da7d313457ea315a55.jpg)

![](images/e9c65bb7e8646351608735cdf3011083a00d2148b7998405854333091074c6ab.jpg)

![](images/8a67b0c50471437b5d82d09e85b8d1a21e4c3ea01ffc78c06744a41338d8d263.jpg)

![](images/dad3801f0553a21da96dc45e93f526daeb562bdfccb27bbe1f6dc6a1c98f14eb.jpg)  
Fig. 1 | PL-based Write and Read mechanisms of MHPe@MYE. a Schematic of a biological synapse. Created in BioRender. Lao, X. (2025) https://BioRender.com/syuovcp. b Schematic illustration of the MHPe@MYE porous structure. Created in BioRender. Lao, X. (2025) https://BioRender.com/at18ev9. c PL properties variation of MHPe@MYE showing PL properties changes during Write and Read operations, with tagged points (1-5) corresponding to specific PL states. d Schematic

![](images/cc67dc12b46a899bf2abccbbe140ec54ec9ec5102ca2a38293d07fb968052135.jpg)  
illustrations of the microscopic mechanisms at points 1-5 in (c). e Time-resolved PL intensity mapping of MHPe@MYE upon continuous  $360\mathrm{nm}$  laser excitation. The tagged area by blue and pink dash line represents PL signal from MHPe and MYE, respectively. (Color bar: blue to red represents 1000 to 30020 in arb. units). f Inert PL dynamics of MHPe@MYE under Read excitation. g PL dynamics featuring both Read and Write processes.

![](images/1beb655de3a22adf69ba50a27e97dc9c5659e1cb6342e7af0e2f487620cda69b.jpg)

To clarify the structural underpinnings of the PL variations in MHPe@MYE, a series of material characterizations are carried out. X-ray diffraction (XRD) analysis confirms the good crystallinity and high phase purity of MHPe@MYE. The phase ratios of the composites are calibrated using XRD refinements, showing a majority of MYE and minor MHPe  $(95.0\%$  v.s.  $5.03\%$ , Supplementary Fig. 3a). Transmission electron microscopy (TEM) and scanning electron microscopy (SEM) reveal the uniform porous structures over the samples (Supplementary Fig. 3b). The corresponding energy dispersive spectrometer (EDS) spectra and element mapping also demonstrate homogeneous distribution of all constituent elements (Supplementary Fig. 3c-j), confirming the formation of extensive interfacial regions that are crucial for the light-induced and dark-recoverable PL variations.

# Theoretical insight on adaptive photoluminescence variation

The PL variation in MHPe@MYE is primarily driven by light-induced interface-controlled halogen migration, leading to composition variations from defective Cl-rich to Br-rich MHPe. While halogen migration under light irradiation is common in hybrid and mixed I/Br halide perovskite systems, it is rare in all-inorganic Cl/Br systems due to their structural robustness[41,42]. Comparison studies show no PL variation observed in CsPb(Br/Cl)₃ (CPBC) polycrystalline films or nanoparticles (refer to Supplementary

Note 2 for details). On the other hand, the halogen migration process in metal-halide perovskites is known to be highly susceptible to surface effects $^{43}$ . Meanwhile, porous materials have demonstrated vast potential in providing interface interactions in luminescent materials $^{38,44}$ . In this context, the porous interface unlocks this otherwise challenging halogen migration in all-inorganic Cl/Br systems, thus prompting a detailed mechanistic investigation.

To this end, DFT simulations are carried out to investigate the role of MHPe@MYE interfaces in the halogen migration process. As demonstrated in Fig. 2a and Supplementary Fig. 5a, the introduction of halogen defects primarily increases the bandgap with increasing Cl content. It does not lead to considerable variation in the band structure of  $\mathrm{CsPbBr_3}$  (CPB), CPBC, or halogen-defective lattices (denoted as  $\upsilon$ -CPB and  $\upsilon$ -CPBC), attributing to the defect tolerance of lead halide perovskites[45]. Meanwhile, the large bandgap  $(4.2\mathrm{eV})$  makes  $\mathrm{Y}_2\mathrm{O}_3$  inert in the PL variation process, and it only provides space to incorporate  $\mathrm{Eu}^{3+}$  dopants and  $^5\mathrm{D}_0\rightarrow^7\mathrm{F}_J$  emission (Supplementary Fig. 5b). Halogen vacancy defects have low formation energies and commonly exist in all-inorganic perovskite crystals[46,47]. On the other hand,  $\mathrm{Y}_2\mathrm{O}_3$  's strong adsorption of Br/Cl can create defect-rich MHPe at the porous channels, as evidenced in previous work[37,38]. The surface energies  $(\gamma)$  of Br/ Cl adsorption on different symmetric sites of  $\mathrm{Y}_2\mathrm{O}_3$  surfaces are then

![](images/89b60d20d709245fb631710cbe6c4d5329869fd6d6be6513094834a15a2db1cb.jpg)

![](images/6da8720067f345b67572b866c53b5bc2ac7fb46ab9e566c8113625cf1b38873c.jpg)

![](images/e6665f36249a19c11ea97947eae0d59a7d10dd789643b9def7f742900716a79f.jpg)  
Fig. 2 | Theoretical insights into the adaptive halogen migration behaviors of MHPe@MYE. a Electronic band structure of perfect CPB, perfect CPBC, and  $\nu$ -CPBC. The green, red, and blue regions indicate the projected contributions from Pb-, Br-, and Cl-orbitals, respectively. The dot line cycles the emergent shallow defect level. b Illustrative scheme of the adsorption site of Br/Cl on  $\mathrm{Y}_2\mathrm{O}_3$  surface

![](images/2d6ab39d2750d74868d9cf355b1834a176539ec85f645c5b46b0fc9842856f0e.jpg)  
and c the corresponding  $\gamma$ . d CCD diagram of Br- and Cl-adsorption on  $\mathrm{Y}_2\mathrm{O}_3$  surface, where red and blue region indicates electron accumulation and depletion, respectively. e Schematic illustration of Br migration pathway from MYE-surface adsorption and interface to subsurface and inner CPBC (or CPB) lattice. f The NEB energy landscape of the migration processes in CPBC and CPB.

![](images/8fdb4687977ba29a6f4727dec1293be28f9828add573470859d41702f14fc9bd.jpg)

![](images/8070501298972a823cbbb687b7ec8637b61f712e02227fd535894b6a5dfd1641.jpg)

compared (Fig. 2b). It shows that values of Br-adsorbed models are always larger than the corresponding Cl counterparts (Fig. 2c), indicative of the comparably unstable Br adsorption. The charge density difference (CDD) diagrams of halogen-adsorbed  $\mathrm{Y}_2\mathrm{O}_3$  also demonstrate the stronger charge interactions between Y and Cl rather than Br as compared in Fig. 2d, attributing to the higher electronegativity of Cl (3.0 vs. 2.8 for Br) and smaller ionic radius (1.81 Å vs. 1.96 Å).

Next, the interface-controlled halogen migration process is investigated from anchored Br/Cl on the MYE surface to the surface site of MHPe, and finally into the deeper MHPe lattice by the nudged elastic band (NEB) method. The model featuring an interface between  $\mathrm{Y}_2\mathrm{O}_3$  and CPBC is illustrated in Fig. 2e. First, we examine Br migration into a CPBC lattice and calculated the migration energy barriers at each layer (Fig. 2f). Detaching from the surfacial sites of  $\mathrm{Y}_2\mathrm{O}_3$ , Br needs to overcome a small energy barrier of  $1.0\mathrm{eV}$  to reach the surface of MHPe. This process mirrors the initial stage of empirical PL variations, where Br can detach from  $\mathrm{Y}_2\mathrm{O}_3$  and migrate to the surface of defect-rich MHPe upon illumination. Since surface defects and their passivation are pivotal in determining the quantum efficiency of halide perovskites, this process would lead to enhanced luminescence intensity[48,49]. Further penetration of Br into CPBC faces substantially higher barriers (3.9 eV and 7.0 eV for subsurface and inner layers,

respectively). Meanwhile, as the Br migration process proceeds, the halide composition of MHPe also evolves, potentially altering the migration energy barrier. The model of Br migration from  $\mathrm{Y}_2\mathrm{O}_3$  surface into the CPB lattice is then investigated, which ideally coincides with the final stage of empirical PL variations with dominated green light emission from CPB. Compared to the CPBC case, the interface barrier of Br migration decreases to only  $0.71\mathrm{eV}$ , with subsequent energy barriers also decreasing to  $2.7\mathrm{eV}$  and  $4.5\mathrm{eV}$ , respectively. This result marks an accelerated Br migration as the Br composition of MHPe increases, explaining the experimentally observed adaptive PL properties evolution with halogen composition. On the other hand, Cl migration faces higher barriers, consistent with dominant green CPB emission during PL evolution. In contrast, bulk CPB shows a higher Br migration barrier (2.3 eV, Supplementary Fig. 6), highlighting the critical role of MHPe@MYE interfaces in enabling adaptive PL changes with neuromorphic behaviors.

# Neuromorphic behaviors in photoluminescence variations

Building upon the theoretically adaptive halogen migration behaviors of MHPe@MYE, the neuromorphic properties of MHPe@MYE are then studied through PL dynamics using programmed light pulses as excitation sources. Fig. 3a illustrates the synaptic PL behavior of

![](images/a47ffcc3bce2abeff0b940d84f19a66d093e59cc782d5a30bd0acd046c9eb62e.jpg)

![](images/ba82816e4d38f004bea2a4570a2c482f2431e6f80adf4c07a39626b8c6ec9958.jpg)  
Fig. 3 | Neuromorphic behaviors in the PL variation process of MHPe@MYE. a PL dynamics of MHPe (upper) featuring Write PL variation and Read dark recovery process, and the PL dynamics of  $\mathrm{Eu}^{3+}$  in MYE (lower) during the same process using programmed  $365\mathrm{nm}$  LED as excitation light spikes. b Stimuli-dependent synaptic behaviors of MHPe@MYE under different spike parameters o  $\lambda_{\mathrm{em}}, \lambda_{\mathrm{ex}}, I_{\mathrm{ex}}$  and f. Error bars are s.d. from four measurements. cx-dependent LTM features of MHPe@MYE, error bars represent s.d. of five measurements. Inset

![](images/0cc359f2ef82dfec6a64aac67ed432f6f18f0f57c32efd00f74c6372cf352397.jpg)  
shows the definitions of  $N_{n}, N_{t}, N_{x}, I_{t}$ , and  $I_{x}$  in the PL dynamics (e.g.,  $x = 30 \, \text{s}$ ). d Fitting curve of PPF indices of MHPe@MYE with s.d. error bars from four measurements. e PL dynamics during formation of STP and LTP. Inset shows the reproducibility of STP (blue) and LTP (red) at the early stages of PL dynamics. f PL dynamics during the decay of STP and LTP, and the corresponding fitting curves. Inset displays s.d. statistical analyses of the fitted time constants across eight measurements.

![](images/1cbe40cf1aaf0a59c8eabb120c3a6f34dadfe968578f651709116863555c2ccd.jpg)

![](images/1542b683c9995b8e1d84d707881629ad6b715f371c16975377a9de6b8fb926b5.jpg)

![](images/136cc6ac4d3924fa0aedb11cf653eedf87ba96891f3fbbbe4fcf87929ec3050f.jpg)

MHPe@MYE by monitoring emissions at  $510\mathrm{nm}$  (MHPe) and  $613\mathrm{nm}$  (MYE). A  $365\mathrm{nm}$  LED powered by an arbitrary waveform generator (AWG) setting at  $2\mathrm{Hz}$  is used as excitation sources. The initial stage requires 85 high-energy Write excitation pulses  $(-161.15\mu \mathrm{W}\cdot \mathrm{cm}^{-2})$  to reach the upper threshold (blue line). The subsequent dark recovery process is monitored using low-energy probing pulses  $(\sim7.96\mu \mathrm{W}\cdot \mathrm{cm}^{-2})$ . The lower threshold (lavender line) is reached within time periods equivalent to 72 Read pulses. Notably, subsequent cycles show adaptive responses, with the second round requiring only 36 Write pulses to reach the upper threshold but 90 Read pulses to recover. This indicates MHPe@MYE's ability to memorize recent excitations, accelerating PL variation while slowing recovery. This effect becomes more pronounced in the third round, with 32 Write and 112 Read pulses, whereas it slightly diminishes after a 1-min interval in the fourth round (51 Write and 89 Read). This behavior mirrors the experience-dependent plasticity in biological synapses, where prior stimulation history influences system responses. In sharp contrast, the  $\mathrm{Eu}^{3+}$  emission from MYE exhibits constant binary On/Off states dictated solely by excitation power without neuromorphic features. The coexisting neuromorphic and inert PL behaviors within the MHPe@MYE system serve as an internal reference. To further characterize these neuromorphic properties, detailed investigations into PL variation process are conducted in search of specific biological phenomena and metrics.

In biological neurons, synaptic plasticity allows a synapse to adjust its synaptic weight (SW) in response to stimuli. In PL-based artificial systems, SW can be quantified by comparing the PL intensity before and after excitation spikes, and the SW variation trends under

different stimulus conditions reflect the stimuli-dependent synaptic behaviors. Our study investigates these behaviors across varying spike parameters specifically based on PL features, including emission wavelength  $(\lambda_{\mathrm{em}})$ , excitation wavelength  $(\lambda_{\mathrm{ex}})$ , excitation intensity  $(I_{\mathrm{ex}})$  and frequency  $(f)$ . The results are summarized in Fig. 3b, with raw spectral data displayed in Supplementary Figs. 7-10. Taking the  $\lambda_{\mathrm{em}}$  series as a reference, when monitoring shorter wavelengths (470-490 nm), SW grows rapidly within 20 spikes but saturates at small values, which is due to the red-shifting wavelength at initial stages. The largest SW is observed at  $500\mathrm{nm}$ , with longer wavelengths showing slower evolution and smaller SW. These trends highlight the diverse synaptic behaviors across different  $\lambda_{\mathrm{em}}$ . Notably, as shown in Supplementary Fig. 7, after 45 s intervals, fewer spikes are required for MHPe@MYE to reach the same SW values, attributed to the history-dependent adaptive behavior of MHPe@MYE. Similarly diverse synaptic evolution trends can be observed in the  $I_{\mathrm{ex}}$  series. As demonstrated in Supplementary Fig. 9, the SW values and variation speeds decrease monotonically as  $I_{\mathrm{ex}}$  decreases, whereas the accelerated recovery behavior persists after resting periods. When  $I_{\mathrm{ex}}$  is further reduced to  $-33.12~\mu \mathrm{W}\cdot \mathrm{cm}^{-2}$ , approaching the energy density of Read  $(-7.96~\mu \mathrm{W}\cdot \mathrm{cm}^{-2})$ , PL variations can no longer be observed. The dependence of SW is similarly studied when varying other parameters of excitation spikes  $(f,\lambda_{\mathrm{ex}})$ , showing that higher SW correlates with shorter  $\lambda_{\mathrm{ex}}$  and higher  $f$ . Reproducibility of such stimuli-dependent synaptic behaviors are examined across four measurements with tolerable standard deviation (s.d.). These rich and adjustable neuromorphic behaviors through multiple spiking parameters enhance the information bandwidth and offer flexibility in designing PL-based

neuromorphic systems, such as the potential task-adaptive parameters tunning<sup>50</sup>. Moreover, this ability to sustain neuromorphic characteristics after resting periods is similar to the long-term memory (LTM) phenomena.

LTM behavior represents a sustained synaptic strength modulation over extended periods, driven by mechanisms like receptor activation and  $\mathrm{Ca^{2+}}$  influx that stabilize experience-dependent memory in biological origins[51]. As shown in Fig. 3c, we observe analogous LTM behavior in MHPe@MYE from the recovery and recalling processes from a highly potentiated PL states after various resting time (denoted as  $x$ ). The inset spectrum demonstrates how LTM behaviors are quantified by comparing  $N_{t}$ ,  $N_{n}$ , and  $N_{x}$ , as defined in Supplementary Note 3. Statistical analysis of five independent measurements confirms high consistency, as evidenced by the minimal error bars in Fig. 3c (raw data in Supplementary Fig. 11). It demonstrates that a smaller  $x$  leads to a higher  $I_{x}$  and fewer  $N_{x}$  required to arouse the same  $I_{t}$  again, indicating good preservation (smaller  $N_{n}$ ) and fast recalling (smaller  $N_{x}$ ) of memory after short periods. As  $x$  prolongs,  $N_{n}$  and  $N_{x}$  become larger and move close to pristine  $N_{t}$  (indicated by gray arrows in Fig. 3c), mimicking the gradual fading (lager  $N_{n}$ ) and hard recalling (larger  $N_{x}$ ) of memory after long intervals. When resting intervals exceed a critical duration ( $\sim 180$  s), the system loses its retained state (Supplementary Fig. 12), analogous to biological forgetting processes. The above behaviors replicate the LTM effects by PL manners, indicating the intriguing long-term neuromorphic behaviors of MHPe@MYE.

On the other hand, pair-pulse facilitation (PPF) is a pivotal indicator for determining the short-term functions of neuromorphic behaviors. It occurs when two consecutive identical pre-synaptic stimuli are applied, leading to a progressively enhanced postsynaptic response. Here, the PPF is measured at higher excitation energy  $(365\mathrm{nm}, -668.78\mu \mathrm{W}\cdot \mathrm{cm}^{-2})$  while  $\lambda_{\mathrm{em}}$  is set at  $500\mathrm{nm}$  for they exhibit faster adaptation during the early stages. PPF index can be defined as the PL intensity ratios between two paired pulse excitation at time interval  $\Delta t$  (Supplementary Fig. 13). Supplementary Table 1 gives a comprehensive benchmark of PPF behavior in a wide spectrum of synaptic devices. MHPe@MYE exhibits  $-181\%$  PPF index measured at  $\Delta t = 0.1\mathrm{s}$ , which is a modest value among existing reports. PPF index typically exhibits a bi-exponential decay relationship against pulse interval  $(\Delta t)$  regardless of the input/output modes[14,52-54]:

$$
\text {P P F} = \mathrm {C} _ {0} + \mathrm {C} _ {1} \exp \left(- \frac {\Delta t}{\tau_ {1}}\right) + \mathrm {C} _ {2} \exp \left(- \frac {\Delta t}{\tau_ {2}}\right) \tag {1}
$$

where  $C_0$  is a constant,  $C_1$  and  $C_2$  represent the initial facilitation degrees of the two phases, and  $\tau_1$  and  $\tau_2$  are the characteristic relaxation times for the fast and slow phases, respectively. Supplementary Fig. 13 presents the measured PPF values at different time intervals, and the resultant fitting curve is shown in Fig. 3d. The fitted  $\tau_1$  and  $\tau_2$  values are 0.205 and 5.04 s (adjusted  $R^2 \approx 0.99$ ), respectively. The two decay channels are indicative of the fast and slow relaxation phases of PPF: the short  $\tau_1$  value enables immediate signal amplification, while the longer  $\tau_2$  value reflects a more gradual change in facilitation for sustained memory over extended periods. This dual-phase relaxation behavior closely mimics the dynamic response of synaptic facilitation, where both fast and slow processes contribute to the complex temporal and adaptive signal processing.

In biological systems, short-term plasticity (STP) and long-term plasticity (LTP) represent fundamental mechanism underlying learning and memory formation. STP functions as a dynamic filter for temporal information processing and working memory, whereas LTP facilitates the consolidation of significant information into long-term memory via sustained synaptic enhancement[55]. MHPe@MYE can also emulate STP and LTP behaviors in PL-based manner, and the distinct decay processes can be monitored by Read operations. As shown in Fig. 3e, the PL states of MHPe@MYE can be categorized into STP with fewer Write

spikes (blue) and LTP with more spikes (red). The variation trends of both LTP and STP demonstrate good reproducibility across eight different measurements. Decay time constants can be acquired from the decay curves (Fig. 3f) of STP and LTP, respectively, by fitting the biexponential decay function:

$$
y = y _ {0} + \mathrm {A} _ {1} \exp \left(- \frac {\Delta t}{\tau_ {1}}\right) + \mathrm {A} _ {2} \exp \left(- \frac {\Delta t}{\tau_ {2}}\right) \tag {2}
$$

The fitted time constants are larger for LTP ( $\tau_{1} = 6.5\mathrm{s}$ ,  $\tau_{2} = 41\mathrm{s}$ ) than STP ( $\tau_{1} = 1.3\mathrm{s}$ ,  $\tau_{2} = 29\mathrm{s}$ ), with tolerable s.d. error margins as shown in the inset of Fig. 3f. This suggests the capability of MHPe@MYE to emulate enduring synaptic modifications by LTP induction, which allows for sustained potentiation over extended periods compared to STP. Such behavior is consistent with the fundamental principles of synaptic plasticity observed in biological systems.

The reproducibility of MHPe@MYE's neuromorphic properties is further verified through four new batches. The PL properties and structural characteristics of other MHPe@MYE samples demonstrate high batch-to-batch consistency, showing similar porous structure and history-dependent reversible PL properties variations. Supplementary Note 4 presents a detailed comparison based on representative results. It should be emphasized that the PL-based neuromorphic behaviors observed in MHPe@MYE mainly mimic excitatory processes, which capture the essential nature of memory acquisition, reinforcement, and retention $^{56}$ . Biological synapses also exhibit complementary functions like inhibitory behaviors. Achieving bidirectional optical modulation of optical responses remains a technical challenge due to the unidirectional nature of light, and PL-based inhibitory excitation requires further mechanism innovations. Learning from existing optoelectrical devices, recent reports have demonstrated that heterostructural designs can enable both excitatory and inhibitory control of electrical states by optical stimuli $^{14,57,58}$ . Other studies have successfully employed electrical control or combined optalelectrical architectures to realize inhibitory behaviors $^{52,59}$ . These approaches provide valuable insights into further enriching the PL-based neuromorphic functions of smart phosphor, particularly in terms of heterostructure engineering and strategic introduction of secondary physical terminals.

# Physical reservoir computing based on smart phosphor

The above results confirm the intriguing PL-based neuromorphic behaviors of MHPe@MYE, characterized by volatile and nonlinear responses to optical stimuli in ultraviolet (UV) and blue regions. These characteristics align well with the fundamental principles of reservoir computing, including nonlinear signal processing and high-dimensional data projection, which facilitates effective feature extraction and transformation of original dataset before downstream classification $^{60-62}$ . To evaluate the feasibility of MHPe@MYE as PL-based physical reservoir, we design an experimental setup using Write pulses ( $\lambda_{\mathrm{ex}} = 365 \mathrm{~nm}$ ,  $-668.78 \mu \mathrm{W} \cdot \mathrm{cm}^{-2}$ ) as inputs and PL intensities under Read excitation ( $\lambda_{\mathrm{em}} = 500 \mathrm{~nm}$ , read by  $-7.96 \mu \mathrm{W} \cdot \mathrm{cm}^{-2}$ ) as outputs, respectively. The custom measurement setup is depicted in Supplementary Note 5. The input signal encoded 4-bit binary sequences (0000 to 1111) as periodic waveforms controlled by AWG (1 Hz), with 1 represented by an active cycle and 0 by absence. An example waveform for the sequence 1011 is shown in Fig. 4a. The measured Read PL dynamics are shown in Fig. 4b, where all  $16 I_{\mathrm{em}} - t$  curves (from 0000 to 1111) exhibit distinct PL dynamics features with notable reproducibility (Supplementary Fig. 15). The results demonstrate that the PL-based MHPe@MYE physical reservoir exhibits stable fading memory characteristics, where the output PL state depends critically on both the number of excitation pulses and their temporal distributions. This can be

![](images/0c4b64fcf308125b3064f75f8941c94b8ca78e5137e01afee0b1d14b4cb96e1d.jpg)

![](images/194b7bfb0b4806f7b9ff028d104f72f0d4cc0b2bbb93f2aeea9cd06d7a8b0af8.jpg)

![](images/39b6dcc455c5a9f024fcd0f84e8e20b44277bb52b4c58fd94ff59f237d9399b4.jpg)

![](images/107966fcca5bf02b0dba07b4b8fa0d5d61df62829e13275060b5ad1031990905.jpg)

![](images/e7bbd31ff73793c17d15ad407c8e12549ffd51b5c70cedf2725add97bf576dda.jpg)

![](images/a2ed47b7d2f929ab40214c136f8cc129a18790192eebb09fa2293d1b874be971.jpg)

![](images/59fc4c7544063818afd30ac8d89b291a1759c9015987c4b746a7d9ebd87f1423.jpg)

![](images/68d5e6a0b7fad0680b445d1ca8a0fa010e10d2cd30c6cbb8c72f45c34247e79c.jpg)

![](images/de66a3eab5773b953d5a6b3f406e9284808f88e7714ee720a75af454cd8c7399.jpg)  
Fig. 4 | Potential application of MHPe@MYE as all-optical physical reservoir. a Schematic representation of 4-bit binary code 1011 encoding through Write and Read light pulse waveforms. b Characteristic Read PL dynamics of MHPe@MYE of 16 binary sequences, with SMP locations indicated in the inset. c Representations of 1100, 0110, 1110, and 1111 Write waveforms used as binary sequences. d Statistical quantification of PL readout distributions at SMP1 and SMP2 of all 16 binary sequences, demonstrating code-specific PL signatures with small s.d. error margins from eight measurements. e 2D feature space projection of dual-feature PL

![](images/30b1e3fe07b75963e9b03f38cc5a7f1bf854f423e540a2b857bea9a02c0e322b.jpg)  
readouts based on eight measurements, showing effective separation of all 4-bit sequence. f Schematic illustrations of SOCOFing fingerprint data acquisition and preprocessing from UV camera imaging, and light pulse conversion to full-PL-based information processing through the MHPe@MYE physical reservoir. Scheme was created in BioRender. Lao, X. (2025) https://BioRender.com/qgctjin.  
g Software-based offline ANN training of the processed results for distinguishing authentic and counterfeit fingerprints. h Training records of Dev1 and Dev2.

exemplified by sequences 1100 and 0110 (Fig. 4c), though both contain two pulses, their distinct timing sequence induces different PL trajectories. Similarly, sequences with varying pulse counts (1100, 1110, and 1111) also generate distinct PL variations. This nonlinear weighting of excitation spikes enables MHPe@MYE reservoir to map distinct 4-bit sequence to characteristic PL responses. Furthermore, sampling points (SMPs) are discrete time instants at which readouts are sampled from the PL dynamics of MHPe@MYE reservoir, thereby encoding temporal PL responses into static features. As tagged in Fig. 4b, two SMPs are manually assigned based on inter-class separation among 16 PL dynamics. While PL readouts at individual SMP show high reproducibility with minimal s.d. errors among eight experiments, neither could fully differentiate all 4-bit codes due to signal overlaps in the one-dimensional feature space (Fig. 4d). By contrast, plotting paired SMP readouts can transfer the time-resolved waveforms into a

two-dimensional (2D) feature space of PL intensity map (Fig. 4e), where all 16 binary patterns become clearly and reproducibly distinguishable.

To validate the practical utility of MHPe@MYE as physical reservoir, it is first applied to process MNIST dataset for handwritten digit recognition $^{63}$ . The MNIST images are preprocessed into stripes of 4-bit binary codes, with detailed methodology outlined in Supplementary Note 6. To compare different SMP designs, three virtual devices with varying abilities to distinguish 4-bit binary codes are constructed. Dev1 employs two SMPs for dual-feature sampling, ensuring better input code identification according to the well-separated features in Fig. 4e. In contrast, Dev2 and Dev3 use only SMP1 or SMP2 as the readout, respectively. The experimental PL readouts are extracted from Fig. 4d with different SMP configurations, which are then fed into a simple artificial neural network (ANN) for offline software-based

training to evaluate the MNIST recognition accuracy after PL-based physical reservoir computing. As plotted in Supplementary Fig. 17, the training results show that Dev1 can achieve classification accuracy of  $92\%$  within 20 epochs, while Dev2 and Dev3 reach only  $90\%$  and  $87\%$ , respectively. This result highlights that the dual-feature method offers better performance in PL-based physical reservoir computing.

To further validate the capability of PL-based reservoir computing in more complex application scenarios, their potential in UV light-based fingerprint recognition is then explored. While optoelectronic devices are typically employed for processing UV light inputs, our study shows that MHPe@MYE can effectively replicate this process through PL-based manner $^{64-66}$ . The workflow of proposed MHPe@MYE physical reservoir for SOCOFing fingerprint authentication is illustrated in Fig. 4f and described in Supplementary Note 7, as modified from previous reports based on optoelectronic devices $^{64}$ . After optimizing the binarization and resizing parameters of SOCOFing images in Supplementary Figs. 18-20, we select the adaptive thresholding binarization and  $64 \times 64$  resizing pixels due to their good performance in balancing training costs and preservation of features. A similar approach is then used to transform the resized images into 4-bit binary codes (Supplementary Fig. 21a, b), which further modulate the input waveform to MHPe@MYE PL-based physical reservoir. Experimental PL dynamics maps are again extracted as the readouts, and fed into ANN to evaluate the recognition accuracy (Fig. 4g). The training results are plotted in Fig. 4h, showing that the dual-feature method (Dev1) leads to much higher accuracies throughout the training process, and finally reaches  $94.4\%$  after 60 epochs. The results are comparable to optoelectronic neuromorphic devices despite the different information processing modes and algorithms $^{15,16,64,67}$ . In sharp contrast, the result of Dev2 (employing SMP2 only) attains markedly lower accuracy of  $84.2\%$ . The disparity between dual- and single-SMP methods is consistently observed across different resizing strategies as compared in Supplementary Fig. 21c-e. Supplementary Fig. 21f summarizes the accuracy and loss of SOCOFing recognition training process at different resize methods.

The above PL-based physical reservoir concept can be broadly extended to other smart phosphor systems, such as the decay-type PersL phosphors, as exemplified in Supplementary Note 8. Nevertheless, the absence of Read mechanism impedes the effective retrieval of information due to internal and external interferences. Comparative studies reveal that decay-type systems experience notably increased computational costs and decreased accuracy resulting from wrong readouts and feature-loss events, particularly with decay signal overlaps from adjacent units (details in Supplementary Note 9). This marks the importance of achieving distinct Read operations for future developments of PL-based neuromorphic computing.

# Discussion

In conclusion, we present MHPe@MYE smart phosphor with intriguing PL-based neuromorphic characteristics. This work promotes conventional smart phosphor from passive stimuli actuators to active information processors, enabling PL-based all-optical neuromorphic computing. By intentionally establishing distinct Write and Read operations through engineered interfacial interaction, this system overcomes the inherent challenges of previous decay-type Write-only phosphor systems. These improvements are crucial for the advancement of PL-based neuromorphic computing. Its potential in real-world applications is demonstrated through high-accuracy recognition tasks as a physical reservoir, validated using MNIST handwritten number recognition and SOCOFing UV fingerprint authentication. These results underscore the feasibility of phosphor materials in all-optical neuromorphic computing, opening alternative pathways for function-oriented design of phosphor materials for information science.

# Methods

# Materials synthesis

MYE host was first prepared by hard-templated sol-gel synthesis. First, poly(methyl methacrylate) (PMMA) mesosphere ( $\sim 80$  nm in diameter) were prepared by colloidal polymerization. The YE sol was prepared by mixing  $5\mathrm{mmol}$ $\mathrm{Y(NO_3)_3}$  and  $\mathrm{Eu(NO_3)_3}$  in  $25\mathrm{mL}$  deionized water and  $10\mathrm{mmol}$  citric acid at  $80^{\circ}\mathrm{C}$ . Next, stacked hard templates of PMMA were prepared by vacuum filtering, where the YE sol was later infiltrated to immerse into the interval of PMMA templates. The obtained composite was dried at  $60^{\circ}\mathrm{C}$  and calcined at  $400^{\circ}\mathrm{C}$  under an inert atmosphere to discard PMMA. The final calcination was performed at  $1000^{\circ}\mathrm{C}$  in air to form the MYE host. The incorporation of MHPe into MYE uses a DMSO precursor containing  $1\mathrm{mol}\cdot \mathrm{L}^{-1}\mathrm{CsCl}$  and  $0.33\mathrm{mol}\cdot \mathrm{L}^{-1}\mathrm{PbCl}_2$ , and  $0.67\mathrm{mol}\cdot \mathrm{L}^{-1}\mathrm{PbBr}_2$ .  $0.1\mathrm{g}$  of the as-prepared MYE was soaked into the above MHPe precursor for  $1\mathrm{h}$  and washed with DMSO twice to remove the remnant precursor on the outer surfaces. The obtained MYE was heated at  $150^{\circ}\mathrm{C}$  for  $15\mathrm{min}$  to finally obtain MHPe@MYE.

# Materials characterizations

A Rigaku SmartLab 9 kW Advance was utilized for XRD analyses using Cu Kα radiation ( $\lambda = 1.5406\AA$ ) at 40 kV and 200 mA. Refinements of XRD data were performed using GSAS-II software[68]. The TEM images were captured with a Tecnai TF30 transmission electron microscope. A Regulus 8100 (HITACHI) SEM equipped with a Bruker Nano GmbH EDS was used to capture the morphology and investigate the elemental distribution of MHPe@MYE. The PL mapping was recorded using a Nova high-sensitivity fiber spectrometer, while the PL dynamics were recorded by Edinburgh FLS 920 using 360 nm laser, Xeon lamp, AWG-controlled UV and blue LEDs (LED Guhon Optoelectronics) as excitation sources, respectively. An optical power meter (SANWA) was used to calibrate the light intensity of LEDs.

# DFT computation methods

Theoretical simulations were performed based on the density functional theory (DFT) using the generalized gradient approximation (GGA) Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional in the MedeA VASP package $^{69}$ . The plane-wave cutoff energy was set to be  $400\mathrm{eV}$ . A  $3\times 3\times 3$  k-mesh centered at the gamma point was used for investigating the electronic structures of bulk MHPe and  $\mathrm{Y}_2\mathrm{O}_3$ $(\mathrm{Eu}^{3+})$ , while  $3\times 3\times 1$  k-mesh was used for investigating the surface adsorption and interface NEB migration processes. All the structures were allowed to relax until the energy on the atoms was less than  $1.0\times 10^{-5}\mathrm{eV}$  and all the forces on atoms were below  $0.1\mathrm{eV}\cdot \mathring{\mathrm{A}}^{-1}$ .  $\gamma$  of halogen adsorption is calculated by the following equation:

$$
\gamma = \frac {E _ {\text {s l a b}} - N E _ {\text {b u l k}} - E _ {\text {H a l o g e n}}}{2 A} \tag {3}
$$

where  $E_{\mathrm{slab}}$  is the total energy of the halogen-absorbed surface model and  $E_{\mathrm{bulk}}$  is the total energy for the corresponding bulk structure,  $N$  is the supercell number,  $A$  is the area of adsorption surface,  $E_{\mathrm{Halogen}}$  is the chemical reference energy of halogen which is derived from  $\mathrm{Br}_2$  and  $\mathrm{Cl}_2$ , respectively. The CCD diagram  $(\rho_{\mathrm{diff}})$  of halogen absorption on  $\mathrm{Y}_2\mathrm{O}_3$  surface was plotted based on the following equation:

$$
\rho_ {\text {d i f f}} = \rho (\mathrm {Y} _ {2} \mathrm {O} _ {3} - \mathrm {X}) - \rho (\mathrm {Y} _ {2} \mathrm {O} _ {3}) - \rho (\mathrm {X}) \tag {4}
$$

where  $\rho (\Upsilon_2\mathrm{O}_3 - \mathrm{X}),\rho (\Upsilon_2\mathrm{O}_3)$ , and  $\rho (\mathbf{X})$  are the charge density of the halogen-adsorbed  $\Upsilon_{2}\mathrm{O}_{3}$ , empty  $\Upsilon_{2}\mathrm{O}_{3}$  surface, and the empty X structure, respectively. The NEB method was employed to investigate the energy barriers by tracing the migration path of halogen from adsorption on the  $\Upsilon_{2}\mathrm{O}_{3}$  surface to surfacial CPBC (or CPB), the subsurface layer, and finally into the inner layers. The atomic positions of  $\Upsilon_{2}\mathrm{O}_{3}$  and the underlying CPBC (or CPB) layer were kept fixed during

the relaxation of the initial and final images. All the DFT computations have been performed with assistance from the VESTA software.

# Software-based training methods of reservoir computing

Python code based on TensorFlow and Keras package was written to evaluate the performance of MHPe@MYE physical reservoir in MNIST and SOCOFing recognition. Readouts of MHPe@MYE physical reservoir were extracted from experimentally acquired PL features, which were fed into software-based ANN for offline evaluation of recognition accuracy. The ANN was trained using the Adam optimizer with sparse categorical cross-entropy as loss function  $(L)$ , which is defined as:

$$
L = - \sum_ {i = 1} ^ {N} y _ {i} \log \left(\widehat {y} _ {i}\right) \tag {5}
$$

where  $N$  is the number of classes,  $y_{i}$  is the true label, and  $\hat{y}_i$  is the predicted probability for class  $i$ . The optimizer updates the weights  $(w)$  at each step  $(t)$  according to:

$$
w _ {t + 1} = w _ {t} - \frac {\eta}{\sqrt {\widehat {v _ {t}}} + \epsilon} \widehat {m _ {t}} \tag {6}
$$

where  $\widehat{m_t}$  and  $\widehat{\nu_t}$  are the bias-corrected first and second moment estimates of the gradients,  $\eta$  is the learning rate, and  $\epsilon$  is a constant for numerical stability.

# Data availability

All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Information or available from the corresponding authors upon request. Source data are provided with this paper.

# Code availability

The custom code used in this study is available from the corresponding authors upon request.

# References

1. Wetzstein, G. et al. Inference in artificial intelligence with deep optics and photonics. Nature 588, 39-47 (2020).  
2. Ren, Q. et al. Optoelectronic devices for in-sensor computing. Adv. Mater. 37, 2407476 (2024).  
3. Mehonic, A. & Kenyon, A. J. Brain-inspired computing needs a master plan. Nature 604, 255-260 (2022).  
4. Cai, H. et al. Brain organoid reservoir computing for artificial intelligence. Nat. Electron. 6, 1032-1039 (2023).  
5. Zhang, W. et al. The development of general-purpose brain-inspired computing. Nat. Electron. 7, 954-965 (2024).  
6. Kudithipudi, D. et al. Neuromorphic computing at scale. Nature 637, 801-812 (2025).  
7. Xu, X. et al. Neuromorphic computing based on wavelength-division multiplexing. IEEE J. Sel. Top. Quant. 29, 7400112 (2023).  
8. Shastri, B. J. et al. Photonics for artificial intelligence and neuromorphic computing. Nat. Photon. 15, 102-114 (2021).  
9. Youngblood, N., Rios Ocampo, C. A., Pernice, W. H. P. & Bhaskaran, H. Integrated optical memristors. Nat. Photon. 17, 561-572 (2023).  
10. Ahmed, S. R. et al. Universal photonic artificial intelligence acceleration. Nature 640, 368-374 (2025).  
11. Hua, S. et al. An integrated large-scale photonic accelerator with ultralow latency. Nature 640, 361-367 (2025).  
12. Li, R. et al. Multimodal artificial synapses for neuromorphic application. Research 7, 0427 (2024).  
13. Wang, J. et al. Technology and integration roadmap for optoelectronic memristor. Adv. Mater. 36, 2307393 (2024).

14. Han, X. et al. Ultrawear light-modulated heterostructure with bidirectional photoresponse for static and dynamic image perception. Nat. Commun. 15, 10430 (2024).  
15. Guo, F. et al. Multifunctional optoelectronic synapse based on ferroelectric Van der Waals heterostructure for emulating the entire human visual system. Adv. Funct. Mater. 32, 2108014 (2022).  
16. Dang, Z. et al. Ferroelectric modulation of  $\mathrm{ReS}_2$ -based multifunctional optoelectronic neuromorphic devices for wavelength-selective artificial visual system. Adv. Funct. Mater. 34, 2400105 (2024).  
17. Wen, Y. et al. Ferroelectric optical memristors enabled by non-volatile electro-optic effect. Adv. Mater. 37, 2417658 (2025).  
18. Zheng, M., Sun, H., Chan, M. K. & Kwok, K. W. Reversible and nonvolatile tuning of photoluminescence response by electric field for reconfigurable luminescent memory devices. Nano Energy 55, 22-28 (2019).  
19. Gong, J. et al. The enhancement of photochromism and luminescence modulation properties of ferroelectric ceramics via chemical and physical strategies. *Laser Photonics* Rev. **16**, 2200170 (2022).  
20. Shan, L. et al. A sensory memory processing system with multi-wavelength synaptic-polychromatic light emission for multi-modal information recognition. Nat. Commun. 14, 2648 (2023).  
21. Du, J. et al. Pushing Trap-controlled persistent luminescence materials toward multi-responsive smart platforms: recent advances, mechanism, and frontier applications. Adv. Mater. 36, 2314083 (2024).  
22. Zhou, X. et al. Interplay of defect levels and rare earth emission centers in multimode luminescent phosphors. Nat. Commun. 13, 7589 (2022).  
23. Zhang, P. et al. High defect tolerance breaking the design limitation of full-spectrum multimodal luminescence materials. Adv. Mater. 37, 2411532 (2024).  
24. Yang, H. et al. Microstrain-stimulated elastico-mechanoluminescence with dual-mode stress sensing. Adv. Mater. 36, 2401296 (2024).  
25. Wong, M.-C., Zhang, Y., Hao, J. Smart phosphors. In Phosphor Handbook (CRC Press, 2022).  
26. Bednarkiewicz, A. et al. All-optical data processing with photon-avalanching nanocrystalline photonic synapse. Adv. Mater. 35, 2304390 (2023).  
27. Bian, H. et al. Multimodal tuning of synaptic plasticity using persistent luminescent memitters. Adv. Mater. 34, 2101895 (2022).  
28. Chen, H. et al. Organic all-photonic artificial synapses enabled by anti-stokes photoluminescence. J. Am. Chem. Soc. 145, 11988-11996 (2023).  
29. Kumar, S., Wang, X., Strachan, J. P., Yang, Y. & Lu, W. D. Dynamical memristors for higher-complexity neuromorphic computing. Nat. Rev. Mater. 7, 575-591 (2022).  
30. Chen, X. et al. Neuromorphic photonic memory devices using ultrafast, non-volatile phase-change materials. Adv. Mater. 35, 2203909 (2023).  
31. Dai, T. et al. A programmable topological photonic chip. Nat. Mater. 23, 928-936 (2024).  
32. Fang, Z. et al. Ultra-low-energy programmable non-volatile silicon photonics based on phase-change materials with graphene heaters. Nat. Nanotech. 17, 842-848 (2022).  
33. Bai, G., Tsang, M.-K. & Hao, J. Luminescent ions in advanced composite materials for multifunctional applications. Adv. Funct. Mater. 26, 6330-6350 (2016).  
34. Wong, M.-C., Chen, L., Tsang, M.-K., Zhang, Y. & Hao, J. Magnetic-induced luminescence from flexible composite laminates by coupling magnetic field to piezophotonic effect. Adv. Mater. 27, 4488-4495 (2015).

35. Wong, M.-C., Chen, L., Bai, G., Huang, L.-B. & Hao, J. Temporal and remote tuning of piezophotonic-effect-induced luminescence and color gamut via modulating magnetic field. Adv. Mater. 29, 1701945 (2017).  
36. Pan, E., Bai, G., Zhou, J., Lei, L. & Xu, S. Exceptional modulation of upconversion and downconversion near-infrared luminescence in Tm/Yb-codoped ferroelectric nanocomposite by nanoscale engineering. Nanoscale 11, 11642-11648 (2019).  
37. Li, M. et al. Understanding the energy barriers of the reversible ion exchange process in CsPbBr $_{1.5}$ Cl $_{1.5}$ @Y $_2$ O $_3$ :Eu $^{3+}$  macroporous composites and their application in anti-counterfeiting codes. ACS Appl. Mater. Interfaces 13, 60362-60372 (2021).  
38. Yang, R. R., Li, M., Zhao, Y. F., Wang, P. & Ye, S. Regulating synthesis and photochromic behavior via interfacial  $\mathrm{Eu}^{3+}/\mathrm{Eu}^{2+}-\mathrm{Pb}^{0}/\mathrm{Pb}^{2+}$  redox of the CsPbCl $_{1.5}$ Br $_{1.5}$ @  $\mathrm{Ca}_{0.9}\mathrm{Eu}_{0.1}\mathrm{MoO}_4$  porous composites. Mater. Today Chem. 23, 100721 (2022).  
39. Ham, D., Park, H., Hwang, S. & Kim, K. Neuromorphic electronics based on copying and pasting the brain. Nat. Electron. 4, 635-644 (2021).  
40. Zhang, W. et al. Neuro-inspired computing chips. Nat. Electron. 3, 371-382 (2020).  
41. Mao, W. et al. Light-induced reversal of ion segregation in mixed-halide perovskites. Nat. Mater. 20, 55-61 (2021).  
42. Zhang, H. et al. Phase segregation due to ion migration in all-inorganic mixed-halide perovskite nanocrystals. Nat. Commun. 10, 1088 (2019).  
43. Biega, R. I. & Leppert, L. Halogen vacancy migration at surfaces of  $\mathrm{CsPbBr}_3$  perovskites: insights from density functional theory. J. Phys. Energy 3, 034017 (2021).  
44. Wang, Y., Yang, R., Zhao, Y., Hong, L. & Ye, S. Lanthanide-containing heteropolyoxomolybdate as precursor to porous complex oxides via polymeric micelle assembly and its heterostructure with carbon dots for anticounterfeiting application. Adv. Opt. Mater. 12, 2302485 (2024).  
45. Kang, J. & Wang, L.-W. High defect tolerance in lead halide perovskite CsPbBr₃. J. Phys. Chem. Lett. 8, 489-493 (2017).  
46. Matheu, R., Vigil, J. A., Crace, E. J. & Karunadasa, H. I. The halogen chemistry of halide perovskites. Trends Chem. 4, 206-219 (2022).  
47. Li, M. et al. Coupling localized laser writing and nonlocal recrystallization in perovskite crystals for reversible multidimensional optical encryption. Adv. Mater. 34, 2201413 (2022).  
48. Yang, D. et al. CsPbBr $_3$  quantum dots 2.0: benzenesulfonic acid equivalent ligand awakens complete purification. Adv. Mater. 31, 1900767 (2019).  
49. Ahmed, G. H. et al. Giant photoluminescence enhancement in  $\mathrm{CsPbCl}_3$  perovskite nanocrystals by simultaneous dual-surface passivation. ACS Energy Lett. 3, 2301-2307 (2018).  
50. Lee, O. et al. Task-adaptive physical reservoir computing. Nat. Mater. 23, 79-87 (2024).  
51. Gu, J. G., Albuquerque, C., Lee, C. J. & MacDermott, A. B. Synaptic strengthening through activation of  $\mathrm{Ca^{2+}}$ -permeable AMPA receptors. Nature 381, 793-796 (1996).  
52. Liu, K. et al. An optoelectronic synapse based on  $\alpha\text{-In}_2\mathrm{Se}_3$  with controllable temporal dynamics for multimode and multiscale reservoir computing. Nat. Electron. 5, 761-773 (2022).  
53. John, R. A. et al. Ionic-electronic halide perovskite memdiodes enabling neuromorphic computing with a second-order complexity. Sci. Adv. 8, eade0072 (2022).  
54. Huang, H. et al. Fully integrated multi-mode optoelectronic memristor array for diversified in-sensor computing. Nat. Nanotechnol. 20, 93-103 (2025).

55. Ohno, T. et al. Short-term plasticity and long-term potentiation mimicked in single inorganic synapses. Nat. Mater. 10, 591-595 (2011).  
56. Rubin, D. C. & Wenzel, A. E. One hundred years of forgetting: a quantitative description of retention. Psychol. Rev. 103, 734-760 (1996).  
57. Yang, R. et al. SnS-facilitated ZnAlSnO-based fully optically modulated artificial synaptic device for image processing. Adv. Funct. Mater. 35, 2414210 (2025).  
58. Yang, R. et al. All-optically controlled artificial synapse based on full oxides for low-power visible neural network computing. Adv. Funct. Mater. 34, 2312444 (2024).  
59. Jiang, H. et al. Simultaneous achieving negative photoconductivity response and volatile resistive switching in  $\mathrm{Cs_2CoCl_4}$  single crystals towards artificial optoelectronic synapse. Light Sci. Appl. 13, 316 (2024).  
60. Cucchi, M., Abreu, S., Ciccone, G., Brunner, D. & Kleemann, H. Hands-on reservoir computing: a tutorial for practical implementation. Neuromorph. Comput. Eng. 2, 032002 (2022).  
61. Liang, X. et al. Physical reservoir computing with emerging electronics. Nat. Electron. 7, 193-206 (2024).  
62. Moon, J. et al. Temporal data classification and forecasting using a memristor-based reservoir computing system. Nat. Electron. 2, 480-487 (2019).  
63. Deng, L. The MNIST database of handwritten digit images for machine learning research [best of the web]. IEEE Sig. Process. Mag. 29, 141-142 (2012).  
64. Zhang, Z. et al. In-sensor reservoir computing system for latent fingerprint recognition with deep ultraviolet photo-synapses and memristor array. Nat. Commun. 13, 6590 (2022).  
65. Guo, J. et al. A flexible PI/graphene heterojunction optoelectronic device modulated by TENG and UV light for neuromorphic vision system. Nano Energy 117, 108928 (2023).  
66. Li, G. et al. Interface-engineered non-volatile visible-blind photodetector for in-sensor computing. Nat. Commun. 16, 57 (2025).  
67. Guo, F. et al. Bio-inspired optoelectronic neuromorphic device based on 2D vdW ferroelectric heterostructure for nonlinearly preprocessing visual information and convolutional operation. Adv. Electron. Mater. 11, 2400528 (2024).  
68. Toby, B. H. & Von Dreele, R. B. GSAS-II: the genesis of a modern open-source all purpose crystallography software package. J. Appl. Crystallogr. 46, 544-549 (2013).  
69. Kresse, G. & Furthmüller, J. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. Comput. Mater. Sci. 6, 15-50 (1996).

# Acknowledgements

This work was supported by a grant from the National Natural Science Foundation of China (No. 52233014, No. 52072126), a fellowship award from the Research Grants Council of Hong Kong (Project No. PolyU SRFS2122-5S02), and PolyU grant (1-CEOH, 1-CD7V).

# Author contributions

Y.Z., S.Y., and J.H. devised the concept. Y.Z. and X.H. designed the experiments. Y.Z. and M.L. synthesized the materials. Y.Z., M.W., F.G., Y.L., X.L., S-Y.P., and Z.D. performed materials characterizations. Y.Z. carried out DFT simulations. Y.Z. and M.W. measured the PL dynamics. Y.Z. conducted software-based ANN training. Y.Z., X.L., and Z.W. visualized the results. Y.Z., X.H., F.G., and M.W. led in drafting original manuscript and all authors have reviewed and commented on it. S.Y. and J.H. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-025-62745-3.

Correspondence and requests for materials should be addressed to Shi Ye or Jianhua Hao.

Peer review information Nature Communications thanks Artur Bednarkiewicz and the other anonymous reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at

http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025