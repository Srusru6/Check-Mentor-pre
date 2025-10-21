# Large-scale integration of artificial atoms in hybrid photonic circuits

https://doi.org/10.1038/s41586-020-2441-3

Received: 13 October 2019

Accepted: 2 April 2020

Published online: 8 July 2020

Check for updates

Noel H. Wan $^{1,4\text{※}}$ , Tsung-Ju Lu $^{1,4\text{※}}$ , Kevin C. Chen $^{1}$ , Michael P. Walsh $^{1}$ , Matthew E. Trusheim $^{1}$ , Lorenzo De Santis $^{1}$ , Eric A. Bersin $^{1}$ , Isaac B. Harris $^{1}$ , Sara L. Mouradian $^{1,3}$ , Ian R. Christen $^{1}$ , Edward S. Bielejec $^{2}$  & Dirk Englund $^{1\text{※}}$

A central challenge in developing quantum computers and long-range quantum networks is the distribution of entanglement across many individually controllable qubits<sup>1</sup>. Colour centres in diamond have emerged as leading solid-state 'artificial atom' qubits<sup>2,3</sup> because they enable on-demand remote entanglement<sup>4</sup>, coherent control of over ten ancillae qubits with minute-long coherence times<sup>5</sup> and memory-enhanced quantum communication<sup>6</sup>. A critical next step is to integrate large numbers of artificial atoms with photonic architectures to enable large-scale quantum information processing systems. So far, these efforts have been stymied by qubit inhomogeneities, low device yield and complex device requirements. Here we introduce a process for the high-yield heterogeneous integration of 'quantum microchiplets'-diamond waveguide arrays containing highly coherent colour centres-on a photonic integrated circuit (PIC). We use this process to realize a 128-channel, defect-free array of germanium-vacancy and silicon-vacancy colour centres in an aluminium nitride PIC. Photoluminescence spectroscopy reveals long-term, stable and narrow average optical linewidths of 54 megahertz (146 megahertz) for germanium-vacancy (silicon-vacancy) emitters, close to the lifetime-limited linewidth of 32 megahertz (93 megahertz). We show that inhomogeneities of individual colour centre optical transitions can be compensated in situ by integrated tuning over 50 gigahertz without linewidth degradation. The ability to assemble large numbers of nearly indistinguishable and tunable artificial atoms into phase-stable PICs marks a key step towards multiplexed quantum repeaters<sup>7,8</sup> and general-purpose quantum processors<sup>9-12</sup>.

Artificial atom qubits in diamond combine spin clusters with minute-scale coherence times $^{5}$  and efficient spin-photon interfaces $^{2}$ , making them attractive for processing and distributing quantum information $^{1,3}$ . In particular, proposed quantum repeaters for long-range, high-speed quantum networks will require hundreds or more memory qubits $^{1,7}$ , whereas error-corrected quantum computing may require millions or more $^{9-12}$ . However, a critical barrier to large-scale quantum information processing is the low device yield of functional qubit systems. Furthermore, although individual spin-photon interfaces can now achieve excellent performance, the lack of active chip-integrated photonic components and wafer-scale, single-crystal diamond currently limit the scalability of monolithic diamond quantum-information-processing architectures. A promising method to alleviate these constraints is heterogeneous integration, which is increasingly used in advanced microelectronics to assemble separately fabricated subcomponents into a single, multifunctional chip. Such hybrid fabrication has also recently been used to integrate photonic integrated circuits (PICs) with quantum modules, including quantum dot single-photon sources $^{13-15}$ , superconducting nanowire

single-photon detectors (SNSPDs) $^{16}$  and nitrogen-vacancy (NV) centre diamond waveguides $^{17}$ . However, these demonstrations assembled components one by one, which presents a formidable scaling challenge, and they did not provide for spectral alignment of artificial atoms. Here we introduce a 'quantum microchiplet' (QMC) framework that greatly improves the yield and accuracy of heterogeneously integrated nanoscopic devices. Specifically, this assembly process enables the construction of a 128-channel photonic integrated artificial atom chip containing diamond quantum emitters with high coupling efficiencies, optical coherences near the lifetime limit and tunable optical frequencies to compensate for spectral inhomogeneities on chip.

Figure 1 illustrates the heterogeneous integration process. The multichip module consists of a waveguide layer in single-crystal aluminium nitride (AlN) for low-loss photonics $^{18}$ , microchiplet sockets to optically interface with separately fabricated diamond QMCs and electrical layers for controlling colour centre transitions. This PIC platform is compatible with additional components, such as on-chip electro-optic modulators $^{19}$  and SNSPDs $^{16,20}$ , for photon switching and photon detection in a quantum photonic chip.

<sup>1</sup>Research Laboratory of Electronics, MIT, Cambridge, MA, USA. <sup>2</sup>Sandia National Laboratories, Albuquerque, NM, USA. <sup>3</sup>Present address: University of California Berkeley, Berkeley, CA, USA.  
4These authors contributed equally: Noel H. Wan, Tsung-Ju Lu. e-mail: noelwan@mit.edu; tsungjul@mit.edu; englund@mit.edu

![](images/b6d6b20b12032f7d9b21231464eec2d961d27c14a3993a730c1ea7b37c10204b.jpg)  
Fig. 1|Scalable integration of artificial atoms with photonics. The separate fabrication of subcomponents before their final assembly maximizes the yield, size and performance of the hybrid emitter-photonics chip. A pick-and-place

![](images/d969ac7292600f2268a49f5c85f9622edb0a8284f0d9097aed05f4e4002d2aae.jpg)

![](images/2d75a0eb2d59bbe1641fb5f09814f330426f54c1c1ef0e78815a34bff46cb679.jpg)  
method transfers pre-screened QMCs from their parent diamond chip into a socket containing efficient photonic interfaces, as well as electrical wires for controlling colour centres.

The large optical transparency of the QMC and PIC materials make them compatible with a variety of quantum emitters. Here we consider the negatively charged germanium-vacancy (GeV) and silicon-vacancy (SiV) centres in diamond with zero-phonon line transitions at  $602\mathrm{nm}$  and  $737\mathrm{nm}$ , respectively, because of their stable optical and spin properties[21-25]. The process begins with focused ion beam (FIB) implantation of  $\mathrm{Ge^{+}}$  and  $\mathrm{Si^{+}}$  into a 1-  $\mu \mathrm{m}$ -pitch square array in a single-crystal diamond substrate, followed by high-temperature annealing (Methods). This

process generates spots of tightly localized GeV centres (depth of about  $74~\mathrm{nm}$ , vertical straggle of about  $12\mathrm{nm}$  and lateral full-width at half-maximum (FWHM) distribution of about  $40\mathrm{nm}$ ) and SiV centres (about  $113\mathrm{nm}$ , about  $19\mathrm{nm}$  and about  $50\mathrm{nm}$ , respectively), which we then located and mapped relative to prefabricated alignment markers by photoluminescence microscopy. We fabricated the QMCs over the emitter arrays using a combination of electron-beam lithography (EBL) and quasi-isotropic etching[26,27]. Figure 2a shows a scanning electron

![](images/bbf9469ac25ed5dfef9ddb3984c943dad7575bac9883793114bdf5c7ce34a404.jpg)

![](images/82b3ebdfa4f7d97e9b1ad3d5b6646242c1bfcd1815f25b0e07a5f184d48ef075.jpg)

Fig.2|Fabrication and integration of QMC with integrated photonics.  
![](images/432c9afffdd14fe93b284468c17d7050e6f745224e483c30392ba34003247f4e.jpg)  
a, SEM overview of the parent diamond chip containing over 500 microchiplets for heterogeneous integration. b, A16-channel QMC. c, An 8-channel QMC with varying mechanical beam rigidity. d, Photoluminescence map of GeV centres

![](images/0ae1e3676e61cb9e0db32589cf4bca2cd79f9ad36c0308da9ddca46168c06629.jpg)

![](images/89dc6babb27bb99307e86bbdb3e77f4e5f6f423e7ec9c60387c3ea16af6b2aff.jpg)  
(bright spots) in a 16-channel QMC. e, Photoluminescence map of SiV centres (bright spots) in a defect-free 8-channel QMC. f, An AlN-on-sapphire integrated photonics module that interfaces with the diamond QMC placed in the chiplet socket. g, Close-up SEM of the diamond QMC and AlN photonic interfaces.

![](images/dc80bf119cc4f646acfc2c513104b38347ac5004ee69cf4e9f68ba7d677c17af.jpg)

![](images/49afa4d601c597f1a7d3685a2d41e77aecd8c16e051ae52a016eb231a6bcd6d6.jpg)

![](images/92cd09210512eba27eaa8c2bec7251e361490811e6b102ae3279072a05987082.jpg)

![](images/504224d7d3770e997037d714259f5d6536c752f950d78fc10b203347f50d09fd.jpg)  
Fig. 3 | Integrated quantum photonics with colour centres. a, Experimental setup in a 4-K cryostat showing the input and output optical interfaces (1), (2) and (3). b, Energy level and spectrum of a GeV centre, where g, e,  $\Delta_{\mathrm{g}}$  and  $\Delta_{\mathrm{e}}$  denote the ground state, excited state, ground-state splitting and excited-state splitting, respectively. Resonant excitation probed transition C, which is the brightest and narrowest line. c, Optical image of sixteen QMC-populated microchiplet sockets containing GeV or SiV centres. The 'unsuccessful'

microscope (SEM) image of various suspended chiplets containing 8- or 16-channel waveguide arrays connected by diamond 'trusses', as seen in the close-up SEM images in Fig. 2b, c and Fig. 2g, respectively. Structurally, much larger arrays are fabricable and integrable: we successfully transferred QMCs with as many as 64 waveguide components (Methods). Despite a misalignment between the FIB mask and the QMC patterns, the photoluminescence scans showed that  $39\%$  of the 8-channel QMCs are 'defect free' (that is, they have one or more stable colour centre per waveguide) as shown in Fig. 2e (Methods). The defect-free yield of the 16-channel QMCs was lower as these are more susceptible to misalignment, so we did not use them in this study. With improvements in FIB alignment and lithography, as well as targeted fabrication over pre-localized single emitters, an even higher yield should be possible in future work (Methods).

modules indicate failed QMC placements. Ch., channel. d, Autocorrelation measurements of a single GeV in channel 41 under off-resonant 2-mW, 532-nm excitation (left) and under resonant excitation at 602 nm (middle), and autocorrelation measurement of a single SiV in channel 65 under resonant excitation at 737 nm (right). e, Waveguide-coupled single photons from every integrated GeV and SiV channel in the PIC. The error bars indicate fit uncertainties at the 1s.d. level.

Figure 2f shows one of 20 micro-chiplet sockets connecting 8 input and 8 output waveguide arrays to an 8-channel QMC. We fabricated this PIC on a wafer of single-crystal AlN on a sapphire substrate using EBL and chlorine reactive ion etching $^{18}$  (Methods). AlN on sapphire is a suitable platform for linear and nonlinear quantum photonics because of its large bandgap (about  $6.2\mathrm{eV}$ ), high material nonlinearities $^{19,28-30}$  and low narrowband background fluorescence in the spectrum  $(600 - 760\mathrm{nm})$  of GeV and SiV centres $^{18}$ . Using piezo-controlled micromanipulators, we transferred QMCs into the microchiplet sockets with a placement success rate of  $90\%$ . The diamond waveguides (width  $340\mathrm{nm}$  and height  $200\mathrm{nm}$ ) transfer light into the AlN waveguides (width  $800\mathrm{nm}$  and height  $200\mathrm{nm}$ ) through inverse tapered sections with a simulated efficiency of  $97\%$  ( $98\%$ ) at a wavelength of  $602\mathrm{nm}$  ( $737\mathrm{nm}$ ) (Methods). The SEM image of an assembled device in Fig. 2g shows a transverse

![](images/29dddf1823d0c25c394d6680c8acd7e49ae556fafcce45baf1d8fbc5e3908913.jpg)

![](images/676cd88c2b2901f8aba7f27bd541fc8f10477858b6e9cd5bbb8e26f99f39d5dc.jpg)

![](images/acf68b387f8fdb09382d7e946acf4d975835b7bbb63c083c5319cc8101320982.jpg)

![](images/d21824cd55939ca50980db831d74e7615c49de9d6be717fdb45e2030002a54b2.jpg)

Fig. 4 | Defect-free arrays of optically coherent and efficient  
waveguide-coupled emitters.a, PLE spectrum (FWHM linewidth  
![](images/11cf734d938a34084255754e84a0eebaa1e2e830792874147ba8859a8f7b023c.jpg)  
(orange curve,  $\Gamma = 35(15)\mathrm{MHz}$ ). The red curve shows the PLE spectrum ( $\Gamma = 40(5)\mathrm{MHz}$ ). d, PLE spectra of GeV centres in each waveguide (WG) of a characteristic 8-channel GeV QMC, with a mean  $\pm$  standard deviation linewidth of  $\Gamma = 54 \pm 24\mathrm{MHz}$ . e, PLE spectra of SiVs in an 8-channel SiV QMC, with  $\Gamma = 146 \pm 20\mathrm{MHz}$ . We interpret the two lines in channel 69 as PLE spectra from two distinct SiV centres ( $g^{(2)}(0) = 0.69(7)$  under off-resonant excitation, not shown).  
$\Gamma = 37(3)\mathrm{MHz}$ , indicated by the arrows) of a single GeV in channel 41 with all-fibre excitation and detection of the phonon sideband (PSB) fluorescence routed on-chip via (1). b, Excitation via (2) and fluorescence detection via (1). This geometry allows GeV resonance fluorescence detection at least 18 dB above background, without spectral, temporal or polarization filtering. c, In transmission, a single GeV centre causes coherent extinction of  $\Delta T / T = 38(9)\%$

placement error of  $38 \pm 16$  nm. For such typical errors, simulations indicate a drop in coupling efficiency by  $10\%$  or  $0.46$  dB. We find that the transfer of the QMCs is substantially easier than for individual waveguides due to their rigidity and many alignment features. The successful transfer of 16 defect-free chiplets results in a 128-channel photonically integrated quantum emitter chip, as characterized below.

We performed experiments in a closed-cycle cryostat with a base temperature below  $4\mathrm{K}$ , as illustrated in Fig. 3a. The optical fibre labelled (1) couples pump light (fluorescence) to (from) the QMC via the AlN waveguides. A microscope objective also provides optical access to the QMC, for example, to a colour centre (optical interface labelled (2)) or a scattering site (labelled (3)). Figure 3b shows the energy level and emission spectrum of a single GeV when pumped through (2) and collected through (1). Off-resonant excitation using 532-nm light with off-chip pump filtering in this configuration enables the rapid identification of single emitters (indicated by a photon intensity autocorrelation function  $g^{(2)}(0) < 0.5$ ). The left panel in Fig. 3d shows a typical photon antibunching  $(g^{(2)}(0) = 0.19(7))$  from a single GeV centre (channel 41) pumped near saturation, without background or detector jitter correction. Under the resonant excitation at  $602\mathrm{nm}$  of transition C (Fig. 3b) of the zero-phonon line (ZPL), the photon purity improves to  $g^{(2)}(0) = 0.06(2)$  (middle panel in Fig. 3d). Similarly, in channel 65, we measured antibunched photons with  $g^{(2)}(0) = 0.05(3)$  from a single SiV centre under resonant excitation at  $737\mathrm{nm}$  (right panel in Fig. 3d). In all 128 integrated waveguides, shown in Fig. 3c, we identified single GeV

and SiV emitters using top excitation (through (2)) and fibre-coupled waveguide collection (through (1)). Their photon statistics are summarized in Fig. 3e.

Next we investigated the optical coherence of a GeV centre using all-fibre spectroscopy. Figure 4a shows the photoluminescence excitation (PLE) spectrum of the channel-41 GeV as we scanned a resonant laser across its ZPL (transition C) with both excitation and detection through the fibre interface (1). Despite the presence of another emitter spectrally detuned by  $50\mathrm{GHz}$  in the same waveguide, resonant excitation allows the selective addressing and readout of single emitters. The measured linewidth of  $\Gamma = \Gamma_0 + 2\Gamma_{\mathrm{d}} = 37(3)\mathrm{MHz}$  (values in parentheses indicate one standard deviation throughout this work), where  $\Gamma_{\mathrm{d}}$  is the pure dephasing rate of the emitter, is near the lifetime limit  $\Gamma_0 = 1 / 2\pi \tau = 24(2)\mathrm{MHz}$ , as obtained from the excited-state lifetime  $\tau$  (Methods).

The PIC geometry also enables the direct detection of ZPL resonance fluorescence without any spectral, temporal or polarization filtering, even under resonant excitation. Figure 4b shows the resonance fluorescence obtained for top excitation (through (2)) and waveguide collection without filtering in the detection via (1). By polarizing the pump electric field along the waveguide axis to minimize excitation of the transverse electric waveguide mode, this cross-excitation/detection configuration achieves a ZPL intensity 18 dB above the background, comparable to free-space diamond entanglement experiments using cross-polarization and time-gated detection $^{31}$ .

![](images/14db8d20d707c984b6dcb01a4235c5f5074bc49832a6e9af5b9cec6cffd9c818.jpg)  
Fig. 5 | Controlling the optical transitions of colour centres on a PIC. a, We applied a d.c. bias between the metal layer Au1 on diamond and metal Au2 on the substrate to electrostatically actuate the QMC. b, SEM image of the device. In this experiment, we investigated the optical response of emitters 1A, 1B and 2

![](images/f78ba3fa747758afa66e2058f773c735c72e30db553375114b9406974ed8840a.jpg)

![](images/c6edcc37bb2a45c3ad3bbd8e68322f6956462f0de49077c872890d0a739480c6.jpg)

According to finite-difference time-domain (FDTD) simulations, an ideal emitter in the optimal configuration has a spontaneous emission coupling efficiency of  $\beta = 0.8$  into the diamond waveguide. Experimentally, we measured this efficiency by measuring the transmission of a laser field through a single GeV centre (Fig. 4c). By injecting a laser field through (3) and monitoring the transmission  $T$  via (1), we observed an extinction of  $1 - T = 0.38(9)$  when on resonance with the GeV centre. This extinction places a lower bound of the emitter-waveguide cooperativity at  $C = 0.27(10)$  and  $\beta = 0.21(6)$ . By accounting for residual line broadening and for the ZPL emission fraction (about 0.6), the dipole-waveguide coupling efficiency is at least 0.55(18); see Methods for other factors that reduce  $\beta$ .

The excellent coherence of the GeV centre in channel 41 is not unique. Figure 4d reports the linewidths of every channel in a characteristic 8-channel GeV diamond chiplet, all measured through the on-chip routing of fluorescence into an optical fibre. We find a mean  $\pm$  standard deviation normalized linewidth of  $T / T_0 = 1.7 \pm 0.7$ , with GeV channels 41, 45 and 48 exhibiting lifetime-limited values of 1.0(2), 0.9(1) and 1.0(2), respectively. From these measurements, we also obtained the inhomogeneous ZPL transition frequency distribution of 85 GHz. In these PLE measurements, we averaged each spectrum over about 5 min (5,000 experiments), demonstrating the emitters' long-term stability after heterogeneous integration. Similarly, as shown in Fig. 4e, we also find uniformly narrow lines from SiV centres across a QMC, with linewidths within a factor of  $T / T_0 = 1.6 \pm 0.2$  from SiV centres in bulk diamond $^{32}$ , and with an inhomogeneous frequency distribution of 30 GHz.

To overcome the inhomogeneous spread in transition frequencies, we implemented a strain-tuning scheme using the electrical layers in our PIC. The fabricated device (Fig. 5a, b) uses a QMC that consists of waveguides with different lengths and beam rigidities (Extended Data Fig. 5). Strain is applied by a capacitive actuator consisting of one gold electrode (Au1) on the QMC layer, separated transversely by  $1.5\mu \mathrm{m}$  from a gold ground plane (Au2) on the sapphire substrate. A bias voltage deforms the waveguide so the associated strain modifies the orbital structures and the optical transitions of embedded colour centres[33-35]. This device geometry enables tuning ranges up to  $100\mathrm{GHz}$ , which is larger than the inhomogeneous distribution and only limited by stiction between the QMC and the substrate (Methods). Owing to differences in dipole positions and orientations, we can spectrally overlap the optical transitions of, for example, emitters 1A and 1B in one waveguide at a bias of  $24.5\mathrm{V}$ , as shown in Fig. 5c. Alternatively, they can also be selectively aligned with that of emitter 2, initially detuned by about  $10\mathrm{GHz}$  in another waveguide channel, at distinct voltages. During strain tuning, we did not observe degradation in the linewidths in PLE scans lasting  $3\mathrm{min}$  (Extended Data Fig. 8); this long-term stability remained within  $150\mathrm{MHz}$  over  $3\mathrm{h}$  of continuous measurement without feedback and unchanged up to a tuning of about  $6.8\mathrm{GHz}$  (Extended Data Fig. 9).

Although not demonstrated here, an array of electrodes could provide closed-loop tuning<sup>35</sup> on each waveguide-coupled emitter

to strain. c, Intra-waveguide emitter 1A and emitter 1B overlap spectrally at  $24.5\mathrm{V}$ . Inter-waveguide overlapping between emitter 2 and emitter 1A (1B) occurs at  $2\mathrm{V}(12\mathrm{V})$ . Error bars for emitter 1A and emitter 2 are smaller than the data points.

to generate indistinguishable photons for Hong-Ou-Mandel interference $^{36}$  using on-chip beamsplitters. On the basis of the emitter linewidths measured here over minutes without feedback, we estimate high-visibility interference of 0.9(0.8) for stable GeV (SiV) emitters such as those in channel 41 (69) and a visibility of  $0.58 \pm 0.24$  ( $0.63 \pm 0.07$ ) when averaging over all emitters in Fig. 4d, e. The optical coherence and photon indistinguishability, which is critical for entangling operations, can be improved, for example, through the Purcell effect by coupling to photonic cavities $^{37}$ .

The large-scale integration of artificial atoms with photonics extends to a wide range of nanophotonic devices, in particular, high-quality-factor diamond photonic crystal cavities $^{26,27,38}$  and other optically active spins $^{2}$  such as NV centres $^{17,31}$ , emerging diamond group-IV quantum memories $^{39}$ , quantum dots $^{40}$  and rare-earth ion dopants $^{41,42}$ . The advances reported in this work should therefore encourage further integration of photonic and electronic components for large-scale quantum-information-processing applications such as multiplexed quantum repeaters or modular quantum computers based on solid-state spins $^{7-12,31,43}$ . Key components have already been individually demonstrated, including photonic switch arrays and beamsplitter meshes $^{44-46}$  for reconfigurable qubit connectivity and heralded spin entanglement, AlN-based high-speed electro-optic modulators $^{19}$  and SNSPDs $^{20}$ , and custom complementary metal-oxide-semiconductor electronics $^{47,48}$  for colour centre spin control and low-latency processing. As PIC applications ranging from optical communications $^{49}$  to phased-array light detection and ranging $^{50}$  to machine learning accelerators $^{44}$  are pushing systems beyond thousands of optical components, the high-yield integration with arrays of high-quality artificial atoms provides a basis to extend these scaling gains to quantum information processing with spins and photons.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-020-2441-3.

1. Wehner, S., Elkouss, D. & Hanson, R. Quantum internet: a vision for the road ahead. Science 362, eaam9288 (2018).  
2. Awschalom, D. D., Hanson, R., Wrachtrup, J. & Zhou, B. B. Quantum technologies with optically interfaced solid-state spins. Nat. Photon. 12, 516-527 (2018).  
3. Atature, M., Englund, D., Vamivakas, N., Lee, S.-Y. & Wrachtrup, J. Material platforms for spin-based photonic quantum technologies. Nat. Rev. Mater. 3, 38-51 (2018).  
4. Humphreys, P. C. et al. Deterministic delivery of remote entanglement on a quantum network. Nature 558, 268-273 (2018); correction 562, E2 (2018).  
5. Bradley, C. E. et al. A ten-qubit solid-state spin register with quantum memory up to one minute. Phys. Rev. X 9, 031045 (2019).  
6. Bhaskar, M. K. et al. Experimental demonstration of memory-enhanced quantum communication. Nature 580, 60-64 (2020).

7. Muralidharan, S. et al. Optimal architectures for long distance quantum communication. Sci. Rep. 6, 20463 (2016).  
8. Lo Piparo, N., Munro, W. J. & Nemoto, K. Quantum multiplexing. Phys. Rev. A 99, 022337 (2019).  
9. Nemoto, K. et al. Photonic architecture for scalable quantum information processing in diamond. Phys. Rev. X 4, 031022 (2014).  
10. Monroe, C. et al. Large-scale modular quantum-computer architecture with atomic memory and photonic interconnects. Phys. Rev. A 89, 022317 (2014).  
11. Nickerson, N. H., Fitzsimons, J. F. & Benjamin, S. C. Freely scalable quantum technologies using cells of 5-to-50 qubits with very lossy and noisy photonic links. Phys. Rev. X 4, 041041 (2014).  
12. Choi, H., Pant, M., Guha, S. & Englund, D. Percollation-based architecture for cluster state creation using photon-mediated entanglement between atomic memories. npj Quantum Inf. 5, 104 (2019).  
13. Kim, J.-H. et al. Hybrid integration of solid-state quantum emitters on a silicon photonic chip. Nano Lett. 17, 7394-7400 (2017).  
14. Elshaari, A. W. et al. On-chip single photon filtering and multiplexing in hybrid quantum photonic circuits. Nat. Commun. 8, 379 (2017).  
15. Osada, A. et al. Strongly coupled single-quantum-dot-cavity system integrated on a CMOS-processed silicon photonic chip. Phys. Rev. Appl. 11, 024071 (2019).  
16. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).  
17. Mouradian, S. L. et al. Scalable integration of long-lived quantum memories into a photonic circuit. Phys. Rev. X 5, 031009 (2015).  
18. Lu, T.-J. et al. Aluminum nitride integrated photonics platform for the ultraviolet to visible spectrum. Opt. Express 26, 11147-11160 (2018).  
19. Xiong, C., Pernice, W. H. P. & Tang, H. X. Low-loss, silicon integrated, aluminum nitride photonic circuits and their use for electro-optic signal processing. Nano Lett. 12, 3562-3568 (2012).  
20. Zhu, D. et al. Superconducting nanowire single-photon detector on aluminum nitride. In Conference on Lasers and Electro-Optics FTu4C.1 (Optical Society of America, 2016).  
21. Sukachev, D. D. et al. Silicon-vacancy spin qubit in diamond: a quantum memory exceeding 10 ms with single-shot state readout. Phys. Rev. Lett. 119, 223602 (2017).  
22. Bhaskar, M. K. et al. Quantum nonlinear optics with a germanium-vacancy color center in a nanoscale diamond waveguide. Phys. Rev. Lett. 118, 223603 (2017).  
23. Becker, J. N. & Becher, C. Coherence properties and quantum control of silicon vacancy color centers in diamond. Phys. Status Solidi A 214, 1770170 (2017).  
24. Siyushev, P. et al. Optical and microwave control of germanium-vacancy center spins in diamond. Phys. Rev. B 96, 081201(R) (2017).  
25. Nguyen, C. T. et al. Quantum network nodes based on diamond qubits with an efficient nanophotonic interface. Phys. Rev. Lett. 123, 183602 (2019).  
26. Mouradian, S., Wan, N. H., Schröder, T. & Englund, D. Rectangular photonic crystal nanobeam cavities in bulk diamond. Appl. Phys. Lett. 111, 021103 (2017).  
27. Wan, N. H., Mouradian, S. & Englund, D. Two-dimensional photonic crystal slab nanocavities on bulk single-crystal diamond. Appl. Phys. Lett. 112, 141102 (2018).  
28. Lueng, C. M., Chan, H. L. W., Surya, C. & Choy, C. L. Piezoelectric coefficient of aluminum nitride and gallium nitride. J. Appl. Phys. 88, 5360-5363 (2000).  
29. Guo, X., Zou, C.-L., Jung, H. & Tang, H. X. On-chip strong coupling and efficient frequency conversion between telecom and visible optical modes. Phys. Rev. Lett. 117, 123902 (2016).

30. Jung, H., Xiong, C., Fong, K. Y., Zhang, X. & Tang, H. X. Optical frequency comb generation from aluminum nitride microring resonator. Opt. Lett. 38, 2810-2813 (2013).  
31. Bernien, H. et al. Heralded entanglement between solid-state qubits separated by three metres. Nature 497, 86-90 (2013).  
32. Rogers, L. J. et al. Multiple intrinsically identical single-photon emitters in the solid state. Nat. Commun. 5, 4739 (2014).  
33. Meesala, S. et al. Strain engineering of the silicon-vacancy center in diamond. Phys. Rev. B 97, 205444 (2018).  
34. Maity, S. et al. Spectral alignment of single-photon emitters in diamond using strain gradient. Phys. Rev. Appl. 10, 024050 (2018).  
35. Machielse, B. et al. Quantum interference of electromechanically stabilized emitters in nanophotonic devices. Phys. Rev. X 9, 031022 (2019).  
36. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
37. Grange, T. et al. Reducing phonon-induced decoherence in solid-state single-photon sources with cavity quantum electrodynamics. Phys. Rev. Lett. 118, 253602 (2017).  
38. Mouradian, S. L. & Englund, D. A tunable waveguide-coupled cavity design for scalable interfaces to solid-state quantum emitters. *APL Photon.* 2, 046103 (2017).  
39. Bradac, C., Gao, W., Forneris, J., Trusheim, M. E. & Aharonovich, I. Quantum nanophotonics with group IV defects in diamond. Nat. Commun. 10, 5625 (2019); correction 11, 360 (2020).  
40. Lodahl, P., Mahmoodian, S. & Stobbe, S. Interfacing single photons and single quantum dots with photonic nanostructures. Rev. Mod. Phys. 87, 347-400 (2015).  
41. Zhong, T. et al. Optically addressing single rare-earth ions in a nanophotonic cavity. Phys. Rev. Lett. 121, 183603 (2018).  
42. Dibos, A. M., Raha, M., Phenicie, C. M. & Thompson, J. D. Atomic source of single photons in the telecom band. Phys. Rev. Lett. 120, 243601 (2018).  
43. Bersin, E. et al. Individual control and readout of qubits in a sub-diffraction volume. npj Quantum Inf. 5, 38 (2019).  
44. Harris, N. C. et al. Linear programmable nanophotonic processors. Optica 5, 1623-1631 (2018).  
45. Taballione, C. et al.  $8 \times 8$  reconfigurable quantum photonic processor based on silicon nitride waveguides. Opt. Express 27, 26842-26857 (2019).  
46. Seok, T. J., Quack, N., Han, S., Muller, R. S. & Wu, M. C. Large-scale broadband digital silicon photonic switches with vertical adiabatic couplers. Optica 3, 64-70 (2016).  
47. Kim, D. et al. A CMOS-integrated quantum sensor based on nitrogen-vacancy centres. Nat. Electron. 2, 284-289 (2019).  
48. Patra, B. et al. Cryo-CMOS circuits and systems for quantum computing applications. IEEE J. Solid-State Circuits 53, 309-321 (2018).  
49. Atabaki, A. H. et al. Integrating photonics with silicon nanoelectronics for the next generation of systems on a chip. Nature 556, 349-354 (2018); 560, E4 (2018).  
50. Sun, J., Timurdogan, E., Yaacobi, A., Hosseini, E. S. & Watts, M. R. Large-scale nanophotonic phased array. Nature 493, 195-199 (2013).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2020

# Article

# Methods

# Ion implantation

Extended Data Fig. 1 summarizes the fabrication and integration processes. First, we relieved the strained surface of the single-crystal diamond plate (Element6) by plasma etching the first  $10\mu \mathrm{m}$  of diamond in  $\mathrm{Ar / Cl_2}$ , followed by another  $5\mu \mathrm{m}$  etching in pure oxygen plasma. We used an FIB<sup>51</sup> tool at the Ion Beam Laboratory (Sandia National Laboratories) to implant Ge ions (spot size of about  $35\mathrm{nm} \times 43\mathrm{nm}$ ) and Si ions (spot size of about  $50\mathrm{nm} \times 45\mathrm{nm}$ ) at an effective areal dose of  $2 \times 10^{11} - 6 \times 10^{11}$  ions per  $\mathrm{cm}^2$  and  $4.5 \times 10^{11} - 9 \times 10^{11}$  ions per  $\mathrm{cm}^2$ , respectively. The Ge (Si) ion energy is  $200\mathrm{keV}$  ( $170\mathrm{keV}$ ), which corresponds to an implantation depth of  $74 \pm 12\mathrm{nm}$  ( $113 \pm 19\mathrm{nm}$ ) from stopping and range of ions in matter (SRIM) simulations<sup>52</sup>. After implantation, we annealed the devices at  $1,200^{\circ}\mathrm{C}$  in an ultrahigh vacuum furnace. Finally, we cleaned the diamond in a boiling mixture of 1:1:1 sulfuric acid, nitric acid and perchloric acid.

# Conversion yield of GeV and SiV centres

We analysed the conversion yields of GeV and SiV centres by counting the absence of fluorescent spots in our implantation region (1-μm pitch, square grid) using photoluminescence microscopy. A Poisson distribution  $P(k)$ , with mean number of colour centres  $\lambda$  and number of observed emitters per spot  $k$ , models the stochastic emitter creation process. From the mean  $\lambda = -\log(P(0))$  and our implantation dose, we estimate the conversion yield of GeV (SiV) centres to be about 1.9% (3.2%).

# Registration of emitters using optical localization

We located and mapped the fabricated quantum emitters relative to prefabricated alignment markers using a wide-field and confocal scanning microscope as shown previously[53]. To demonstrate the microchiplet principle in this study, we registered the qubit grid, rather than each emitter's location. In particular, we determined the global displacement of the emitter grid from the implantation process and used this offset in our subsequent electron-beam lithography of QMCs. We anticipate that the targeted placement of devices over pre-localized emitters[53-57] will increase the yield of emitter-coupled QMCs. Such approaches may also be critical for reducing the proximity of nanofabricated surfaces to emitters and for coupling to photonic crystal nanocavities.

# Quantum microchiplet fabrication

After ion implantation and optical registration, we used a quasi-isotropic diamond etching recipe $^{26,27}$  to fabricate suspended QMCs. In particular, we deposited  $180~\mathrm{nm}$  of silicon nitride (SiN) hard mask using plasma-enhanced chemical vapour deposition. We patterned the SiN hard mask using a ZEP-520A electron-beam resist with ESpacer conductive polymer and  $\mathrm{CF_4}$  reactive-ion etching. Subsequently, we used inductively coupled reactive-ion etching to transfer the pattern from SiN into the diamond layer. Following oxygen etching of the diamond, we deposited  $15\mathrm{nm}$  of conformal alumina via atomic layer deposition. After a brief breakthrough etch of alumina, we etched the chip in zero-bias oxygen plasma to isotropically undercut the diamond QMCs. Finally, we removed the SiN and alumina masks in hydrofluoric acid. We again annealed the device at  $1,200^{\circ}\mathrm{C}$  using the above ultrahigh-vacuum, high-temperature annealing recipe, followed by a clean in a boiling mixture of 1:1:1 sulfuric acid, nitric acid and perchloric acid.

# AINphotonics

AlN is a large-bandgap material (about  $6.2\mathrm{eV}$ ) that is suitable for linear optics, nonlinear optics and optomechanics, with an electro-optic coefficient of  $r_{33} = 1\mathrm{pmV}^{-1}$  (ref. [19]), second-order optical nonlinear susceptibility of  $\chi^{(2)} = 4.7\mathrm{pmV}^{-1}$  (ref. [29]), a third-order optical nonlinearity (Kerr) coefficient of  $n_2 \approx 2.5 \times 10^{-15}\mathrm{cm}^2\mathrm{W}^{-1}$  (ref. [30]) and a piezoelectric coefficient of  $d_{33} \approx 5\mathrm{pmV}^{-1}$  (ref. [28]). Here we used a wafer of 200-nm-thick

single-crystal AlN on a sapphire substrate (MSE Supplies, grown by hydride vapour phase epitaxy). Before processing of the AlN PIC, we patterned gold alignment markers to use for alignment between the photonic layer and the metal layers for strain tuning. We defined the AlN photonic circuitry using EBL (ZEP-520A electron-beam resist and ESpacer conductive polymer) and chlorine-based inductively coupled plasma reactive-ion etching[18]. Then, S1813 photoresist served as a protective layer for mechanical edge polishing. We then diced the chip using an automatic dicing saw (DISCO DAD-3240). We polished the chip to produce optical-grade facets for edge coupling (Allied Multi-Prep Polishing System 8). Finally, sonication in  $N$ -methyl-2-pyrrolidone removed the S1813 protective layer and debris caused by dicing and mechanical polishing.

# Metal layers

The fabrication of the metal electrodes and contact pads on top of the PIC substrate immediately followed the patterning of the thin-film AlN and preceded the chip dicing and edge polishing. The PIC substrate metal layer was defined by lift-off of 50-nm Au on top of 5-nm Ti using a single layer of A6 950K poly(methyl methacrylate) electron-beam resist (450 nm thick), which was aligned relative to the AlN PIC with metal alignment markers. Then, the fabrication of the AlN photonic circuitry proceeded to dicing and polishing, followed by integration of the QMC. After pick-and-place transfer of the QMC to the microchiplet socket, we used a targeted electron-beam metal deposition process to place platinum on the periphery of the QMC for electrical connection (FEI Helios NanoLab 600 DualBeam). This process also locked the QMC into place before resist spin-coating. Finally, we defined the metal electrode layer on top of the QMC by lift-off of 15-nm Au on 5-nm Ti using a single layer of A11 950K poly(methyl methacrylate) (2 μm thick).

# Yield of defect-free microchiplets

Using photoluminescence spectroscopy, we investigated the occurrence of defect-free 8-channel QMCs, as summarized in Extended Data Fig. 2. From this histogram, we estimate the probability of creating defect-free QMCs to be  $39\%$ . We note that this success probability depends on a variety of factors, including the alignment accuracy of the FIB implantation, the relative calibration between EBL and FIB, as well as the optical registration process. By deterministically placing each element of the QMC over pre-localized emitters, it should be possible to boost the yield towards unity, allowing hundreds or thousands of quantum channels per chiplet.

# Pick-and-place transfer process

We used piezo-controlled three-axis and rotation stages to align the QMC with the PIC $^{17}$ . In addition to the AlN waveguides, the QMC also rests on top of multiple small AlN pedestals to prevent bowing of the diamond structures and stiction with the underlying sapphire substrate. In the case of an inaccurate placement, both the QMC and socket can be reused simply by picking the QMC and re-attempting the placement process. Experimentally, we have transferred a variety of arrays, ranging from single-channel devices all the way to 64-channel QMCs. We expect computer-controlled placement and self-alignment locking features to improve the transfer rate and to potentially fully automate the process.

# Experimental setup

We used a closed-cycle helium cryostat with a base temperature of  $4\mathrm{K}$  (Montana Instruments) with a top-access microscope objective (Mitutoyo  $100\times$  ULWD, numerical aperture (NA) of 0.55). We used three-axis nanoposition steppers (Attocube ANP-x,z-50) and scanners (Attocube ANS-x,z-50) for edge coupling of optical fibres (lensed fibre with a spot size of  $0.8\mu \mathrm{m}$  at  $633\mathrm{nm}$  or a Nufern UHNA3 fibre) to the PIC. For photoluminescence (PLE) spectroscopy, we filtered the fibre-coupled fluorescence in free space using bandpass filters—Semrock FF01-605/15 (FF01-647/57) for GeV centres and FF01-740/13 (FF01-775/46)

for SiV centres. We off-resonantly pumped GeV (SiV) using 532-nm (660-nm) lasers. Resonant excitation was achieved using a tunable laser (MSquared SolsTiS with an external mixing module). For PLE, we used acousto-optic modulators to excite GeV centres with a resonant pulse and an optional 532-nm charge repump pulse. For SiV centre experiments, we did not gate the resonant and repump optical pulses. In the resonance fluorescence detection experiment (Fig. 4b), we placed a half-wave plate before channel 2 to minimize laser coupling into the waveguide mode. To measure the excited-state lifetime of single emitters, we used time-correlated single-photon counting (PicoHarp 300) and a pulsed laser source (SuperK, filtered to  $532 \pm 20 \mathrm{~nm}$ ). We fitted the lifetime curves of the emitters in Fig. 4d with biexponential terms to account for fast decay and the slower fluorescence decay time constant. For strain-tuning experiments, we used a programmable voltage source (Keithley 2400) and observed negligible leakage currents (less than  $0.2 \mathrm{nA}$ ) for all applied voltages in this experiment (up to  $35 \mathrm{~V}$ ).

# Spontaneous emission  $\beta$ -factor and dipole coupling with the waveguide mode

The extinction in the resonant transmission spectrum arises from the interference between the scattered and incoming optical fields, and its depth depends on the dipole-waveguide coupling  $\beta = \Gamma_{\mathrm{wg}} / (\Gamma_{\mathrm{wg}} + \Gamma')$ , where  $\Gamma_{\mathrm{wg}}$  is the emission rate into the waveguide mode and  $\Gamma'$  the decay rate into all other channels. For the measurement in Fig. 4c, we first characterized the saturation response of the emitter when excited via (3). At the low-excitation limit, the cooperativity  $C$  can be extracted from  $T \approx (1 - \beta)^2 = (1 + C)^{-2}$ . By also accounting for line broadening of  $2\Gamma_{\mathrm{d}} / \Gamma_0 = 0.33(14)$ , we determined  $\beta$  via  $T = 1 - \frac{(\beta - 2)\beta}{(1 + 2\Gamma_{\mathrm{d}} / \Gamma)(1 + S)}$ , which reduces to the usual expression  $T \approx (1 - \beta)^2$  in the absence of broadening and far from saturation  $S \ll 1$ . In this experiment, we operated at  $S \approx 10^{-2}$  and all errors denote the fit or propagated uncertainties. The discrepancy of the experimental  $\beta = 0.21(6)$  (0.55(18) after correcting for broadening and a ZPL branching ratio of 0.6) with the simulated  $\beta = 0.8$  using the three-dimensional (3D) FDTD method (Lumerical) arises from three possible sources: (1) angular and positional misalignment of the dipole in the waveguide; (2) a finite population in the upper ground state and emission into transition D; and (3) possible non-radiative processes.

# Diamond-PIC coupling

Extended Data Fig. 3a, b shows the normalized electric  $|\mathbf{E}|$  field of 602-nm (737-nm)-wavelength transverse electric light coupling from the diamond waveguide  $(340\mathrm{nm}\times 200\mathrm{nm})$  to the bottom AlN waveguide  $(800\mathrm{nm}\times 200\mathrm{nm})$ , calculated using the 3D FDTD method. The light transfers adiabatically via tapered sections in the diamond waveguide and AlN waveguide. Here the coupling region is  $9\mu \mathrm{m}$  long, with a diamond taper length of  $8\mu \mathrm{m}$  and AlN taper length of  $5\mu \mathrm{m}$ . The top insets show 2D transverse cross-sections of the light propagation. The cross-sections at  $y = -10\mu \mathrm{m}$  and  $y = 1\mu \mathrm{m}$  correspond to the fundamental transverse electric mode of the diamond waveguide and AlN-on-sapphire waveguide, respectively. The cross section at  $y = -5\mu \mathrm{m}$  ( $y = -6\mu \mathrm{m}$ ) is the point where half of the light launched from the diamond waveguide is transferred to the AlN waveguide at 602-nm (737-nm) wavelength. The light from the diamond waveguide couples to the AlN waveguide with  $97\%$  (98%) efficiency at these wavelengths, with all of the light coupling preferentially to the AlN fundamental transverse electric mode and negligible coupling to higher-order modes. This optimized device geometry was determined by optimizing for the coupling efficiency from the fundamental transverse electric mode of the diamond waveguide to the fundamental transverse electric mode of the AlN while sweeping the diamond taper length, the AlN taper length, and the overlap region between the diamond and AlN waveguides. In Fig. 2g, we showed a typical transverse placement error of  $38\pm 16\mathrm{nm}$  for our transfer placement of the QMC to the microchiplet socket; in

simulation, this displacement corresponds to a decrease of the coupling efficiency to  $93\%$  (89%) at 602-nm (737-nm) wavelength. Hence, we have a 0.46-dB tolerance in the coupling efficiency within our transfer placement accuracy. By directly measuring the PIC-diamond-PIC transmission efficiency, we found the interlayer coupling efficiency to be greater than  $34\%$ , which was lower than simulations probably due to scattering at the interfaces and the QMC cross-junctions.

# PIC-fibre coupling

We couple laser and photoluminescence to and from AlN-on-sapphire waveguides using lensed fibres (Nanonics Imaging, SM-630 with spot size  $0.8 \pm 0.3 \mu \mathrm{m}$  and working distance  $4 \pm 1 \mu \mathrm{m}$ ) for cryostat experiments and ultrahigh NA fibres (UNHA3) for room-temperature experiments. Under our single-mode operation at  $602 - 737 \mathrm{~nm}$ , the in-coupling efficiency is the same as the out-coupling efficiency of AlN waveguide to lensed fibre, which we find to be  $51 - 57\%$  using the 3DFDTD method. In practice, the PIC-fibre coupling efficiency, which we find to be about  $11\%$  in our devices, is sensitive to the edge coupler polishing quality. For the high-NA fibre, which is multimode at our wavelengths of interest, we find the numerical out-coupling efficiency to the fundamental fibre mode to be  $25\%$  ( $34\%$ ) at  $602 \mathrm{~nm}$  ( $737 \mathrm{~nm}$ ); there is also  $1\%$  ( $3\%$ ) coupling into higher-order modes.

# System efficiency  $\eta$

Extended Data Fig. 4a shows the response from an idealized emitter system, fitted to  $F = F_{\mathrm{sat}}P / (P_{\mathrm{sat}} + P) + cP$ , where  $P$  is the continuous-wave 532-nm excitation pump power,  $cP$  is the linear background,  $P_{\mathrm{sat}} = 1.2\mathrm{mW}$  is the saturation power,  $F$  is the measured ZPL fluorescence at the detector and  $F_{\mathrm{sat}} = 1.11$  megacounts per second (Mcps). Extended Data Table 1 shows an average saturated count rate of  $0.64 \pm 0.36$  Mcps from an array of GeV waveguides in a QMC. To independently measure the system efficiency at the detector,  $\eta_{\mathrm{system}}$ , we used a pulsed source (SuperK Extreme,  $532 \pm 20$  nm) with a repetition rate of  $26\mathrm{MHz}$ . From the saturation response (Extended Data Fig. 4b), we determined  $F_{\mathrm{sat}} = 0.25\mathrm{Mcps}$  and  $\eta_{\mathrm{system}} = 0.72\%$ . This experimentally determined efficiency is within a factor of five from the independently calculated  $\eta_{\mathrm{system}} = 0.5\beta \eta_{\mathrm{PIC}}\eta_{\mathrm{fibre}}$ $\eta_{\mathrm{setup}} \approx 2.6\%$ , where  $(\beta ,\eta_{\mathrm{PIC}},\eta_{\mathrm{fibre}},\eta_{\mathrm{setup}})\approx (0.55,0.34,0.33,0.58)$  are the dipole-waveguide, diamond-PIC coupling, PIC-fibre coupling and external setup detection efficiencies, respectively. Here the factor of 0.5 accounts for the present configuration in which we collected the photon emission in one direction only. In these saturation experiments at room temperature, we used a lensed fibre with  $2.5 - \mu \mathrm{m}$  spot size at  $1,550~\mathrm{nm}$ , which we find to have  $\eta_{\mathrm{fibre}} \approx 33\%$ . We attribute the discrepancy to the non-unity radiative quantum efficiency of the emitter and deviations in  $\beta ,\eta_{\mathrm{PIC}}$  and  $\eta_{\mathrm{fibre}}$  from independent measurements based on another device. In the next subsection, we outline methods to improve the system efficiency.

# Improving the system efficiency

In our experiments, the uncladded microchip enables the heterogeneous integration of QMC but the mode mismatch between the AlN-on-sapphire waveguide and the lensed (high NA) fibre causes at least 3 dB (5 dB) insertion losses as characterized above. It is possible to improve the mode overlap by cladding the microchip with alumina or with materials with similar refractive indices as the underlying sapphire<sup>18</sup>. In such a scheme, we would taper down the AlN waveguides at the chip facet to better mode-match with the lensed fibre. Our cladded edge coupler design can substantially improve the coupling from the AlN waveguide to the lensed fibre to be  $84\%$  (84%) at 602 nm (737 nm), as well as improve the coupling to high NA fibre to be  $89\%$  (91%) at 602 nm (737 nm), using the present AlN-on-sapphire material and film thickness. In this design, we matched the mode field diameters and reduced the effective refractive index mismatch between the fundamental transverse electric modes at AlN edge coupler facet and the lensed (high NA) fibre focus spot (facet). Owing to the index mismatch, the light

# Article

coupling is limited by Fresnel reflections at the waveguide facet, which can be reduced using an index-matching environment. Finally, on-chip reflectors in diamond can increase the photon collection efficiency by a factor of two, and photonic crystal cavities can boost the emission into the waveguide mode.

# Strain tuning scheme of QMC on PIC

We introduced different optical responses to our emitter QMC by changing the length of their constituent waveguides. Here we used waveguides of length  $20\mu \mathrm{m}$  (type I) and length  $15\mu \mathrm{m}$  (type II). To be compatible with the QMC framework, we included a flexible bridge between type II waveguides and the QMC body (Extended Data Fig. 5a, Fig. 5a). Extended Data Fig. 5b confirms the difference in strain response at  $30\mathrm{V}$  (modelled using COMSOL Multiphysics) between type I and type II waveguides.

# Response of optical transitions to strain

We consider single GeV centres (emitter 1A, emitter 1B, emitter 2) indicated in Extended Data Fig. 5a, Fig. 5a, b. Extended Data Fig. 6 plots the spectral response of the optical transition lines up to an applied voltage of  $30\mathrm{V}$ . From the increasing line splitting of the orbital ground states  $\Delta_{\mathrm{g}}$ , that is, between lines C and D (as well as A and B), we find that emitter 1B is a dipole whose axis lies in the transverse plane<sup>33,34,60</sup> of the waveguide. On the basis of the unidirectional shift of all four lines, emitters 1A and 2 are dipoles oriented in the longitudinal cross-sectional plane of the waveguide<sup>33,34,60</sup>. In particular, the global blueshift of the lines of emitter 1A indicates that it resides in a region with compressive strain (that is, below the neutral axis of the mechanical beam). Conversely, the optical lines of emitter 2 redshifts with applied voltage, indicating that it resides in a region with tensile strain, which is located above the neutral axis of the waveguide. Extended Data Fig. 7 shows the robustness of the strain-tuning mechanism as we repeatedly applied voltages from  $10\mathrm{V}$  to  $26\mathrm{V}$ . Above  $30\mathrm{V}$ , we see over  $100\mathrm{GHz}$  of tuning of the two brightest transitions C and D for emitters 1A and 2; however, we note that in this regime there was hysteresis possibly due to stiction with the underlying gold and substrate about  $150\mathrm{nm}$  and  $200\mathrm{nm}$  away, respectively. Nevertheless, for the purpose here, we were able to spectrally overlap any pair of the three emitters with less than  $25\mathrm{V}$ . Revised electrode, QMC and/or PIC designs in future microchips should be able to extend the spectral shift of individually tunable waveguides. We note that the small 'pull in' voltage in our experiment appears earlier than it does in simulation (over  $250\mathrm{V}$ )—possibly due to the surface conductivity of diamond<sup>60,61</sup>.

# Stability of optical transitions

We investigated the optical stability of an emitter during spectral tuning via strain. Here we monitored a GeV in another chiplet with an identical electrode configuration (the earlier device used for Fig. 5 and Extended Data Figs. 5-7 was no longer available due to an accident). Extended Data Fig. 8 shows the centre frequency shift (bottom) of the ZPL transition and its linewidth (top) as a function of voltage. In these PLE linescans under strain, we averaged each spectrum over 2,000 experiments (about  $3\mathrm{min}$ ) and did not observe substantial degradation in the linewidth. We then tracked the ZPL at various voltage biases under repeated PLE measurements over  $3\mathrm{h}$ . Extended Data Fig. 9 shows the long-term ZPL stability to within  $150\mathrm{MHz}$  for spectral tuning up to  $6.8\mathrm{GHz}$ . At higher tuning ranges, the linewidths were unchanged but there was an increase in spectral diffusion of the centre frequency, probably due to an induced permanent dipole moment that increased susceptibility to charge fluctuations[60,62]. Nevertheless, at a tuning of  $20\mathrm{GHz}$ , the FWHM of the inhomogeneous distribution remained under  $250\mathrm{MHz}$ , which is within a factor of four of the initial linewidths of about  $60\mathrm{MHz}$ .

# Data availability

The datasets generated during and/or analysed during the current study are available from the corresponding author on reasonable request. The data that support the findings of this study are also openly available in figshare at https://doi.org/10.6084/m9.figshare.11874291.

51. Schröder, T. et al. Scalable focused ion beam creation of nearly lifetime-limited single quantum emitters in diamond nanostructures. Nat. Commun. 8, 15376 (2017).  
52. Ziegler, J. F., Ziegler, M. D. & Biersack, J. P. SRIM - the stopping and range of ions in matter (2010). Nucl. Instrum. Methods Phys. Res. B 268, 1818-1823 (2010).  
53. Wan, N. H. et al. Efficient extraction of light from a nitrogen-vacancy center in a diamond parabolic reflector. Nano Lett. 18, 2787-2793 (2018).  
54. Badolato, A. et al. Deterministic coupling of single quantum dots to single nanocavity modes. Science 308, 1158-1161 (2005).  
55. Gazzano, O. et al. Bright solid-state sources of indistinguishable single photons. Nat. Commun. 4, 1425 (2013).  
56. Gschrey, M. et al. In situ electron-beam lithography of deterministic single-quantum-dot mesa-structures using low-temperature cathodoluminescence spectroscopy. Appl. Phys. Lett. 102, 251113 (2013).  
57. Sapienza, L., Davanço, M., Badolato, A. & Srinivasan, K. Nanoscale optical positioning of single quantum dots for bright and pure single-photon emission. Nat. Commun. 6, 7833 (2015).  
58. Thyrestrup, H. et al. Quantum optics with near-l lifetime-limited quantum-dot transitions in a nanophotonic waveguide. Nano Lett. 18, 1801-1806 (2018).  
59. Chang, D. E., Sorensen, A. S., Demler, E. A. & Lukin, M. D. A single-photon transistor using nanoscale surface plasmons. Nat. Phys. 3, 807-812 (2007).  
60. Sohn, Y.-I. et al. Controlling the coherence of a diamond spin qubit through its strain environment. Nat. Commun. 9, 2012 (2018).  
61. Maier, F., Riedel, M., Mantel, B., Ristein, J. & Ley, L. Origin of surface conductivity in diamond. Phys. Rev. Lett. 85, 3472-3475 (2000).  
62. Sipahigil, A. et al. Indistinguishable photons from separated silicon-vacancy centers in diamond. Phys. Rev. Lett. 113, 113602 (2014).

Acknowledgements The focused ion beam implantation work was performed at the Center for Integrated Nanotechnologies, an Office of Science User Facility operated for the US Department of Energy (DOE) Office of Science. Sandia National Laboratories is a multimission laboratory managed and operated by National Technology and Engineering Solutions of Sandia, LLC, a wholly owned subsidiary of Honeywell International, Inc., for the US DOE's National Nuclear Security Administration under contract DE-NA-0003525. The views expressed in the article do not necessarily represent the views of the US DOE or the United States Government. This work made use of the Shared Experimental Facilities supported in part by the MRSEC Program of the National Science Foundation (NSF) under award number DMR - 1419807. We thank D. Perry for providing the focused ion beam implantation at Sandia National Laboratories, and D. Zhu and C. Peng for assistance with wire bonding. N.H.W. acknowledges support from the Army Research Laboratory (ARL) Center for Distributed Quantum Information (CDQI) programme W911NF-15-2-0067. T.-J. L. acknowledges support from the Department of Defense (DOD) National Defense Science and Engineering Graduate Fellowship (NDSEG) as well as the Air Force Research Laboratory RITA programme FA8750-16-2-0141. K.C.C. acknowledges funding support by the NSF Graduate Research Fellowships Program and ARL CDQI. M.P.W. acknowledges support from the NSF Center for Integrated Quantum Materials (CIQM), NSF grant number DMR-1231319. M.T. acknowledges support by an appointment to the Intelligence Community Postdoctoral Research Fellowship Program at the Massachusetts Institute of Technology, administered by the Oak Ridge Institute for Science and Education through an interagency agreement between the US DOE and the Office of the Director of National Intelligence. L.D.S acknowledges support from the Under Secretary of Defense for Research and Engineering administered through the MIT Lincoln Laboratory Technology Office. E.A.B. was supported by a NASA Space Technology Research Fellowship and the NSF Center for Ultracold Atoms (PHY-1734011). I.B.H is supported by the DOE 'Photonics at Thermodynamic Limits' Energy Frontier Research Center under grant DE-SC001940. S.L.M was supported by the NSF EFRI ACQUIRE programme EFMA-1641064. I.R.C. acknowledges funding support from the DOD NDSEG Fellowship, NSF award DMR-1747426, and the NSF EFRI ACQUIRE programme EFMA-1641064. D.E. acknowledges partial support from the MITRE Quantum Moonshot initiative.

Author contributions N.H.W., T.-J.L. and D.E. conceived the experiments and wrote the manuscript. N.H.W. and T.-J.L. fabricated the devices, performed the experiments, and analysed the data, with fabrication assistance from K.C.C. and experimental assistance from M.P.W., M.E.T., L.D.S., E.A.B., I.B.H., S.L.M., and I.R.C. E.S.B. performed ion implantation. D.E. supervised the project. All authors discussed the results and contributed to the manuscript.

Competing interests The authors declare no competing interests.

# Additional information

Correspondence and requests for materials should be addressed to N.H.W., T.-J.L. or D.E. Peer review information Nature thanks Wolfram Pernice, Jennifer Choy and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at http://www.nature.com/reprints.

![](images/978c1f600f90cc0374ba146015ff265bbaf5549ee496d1e773072302f9f80fcf.jpg)

Extended Data Fig.1|Flowchart for large-scale heterogeneous integration. See main text and methods for process descriptions.

# Article

![](images/27492b21137e5063e439349a618e50b68a2db7184b50245e82de9455446e8e44.jpg)  
Extended Data Fig. 2 | Histogram of number of emitter-coupled waveguides within a QMC. The red coloured bar corresponds to the defect-free 8-channel QMCs that were suitable for integration. The orange coloured bars correspond to the QMCs that we did not use in this work.

![](images/8d47b04f965f7732dc30f5b6d5d8742d5dcc660e1920e736c58237efd6b4b87c.jpg)

![](images/80d0e25cdfea689956cd043cbbc0271db0d0f24d7162193d9b31d3121624ee2e.jpg)

![](images/54e7d976ae0fd029589ffc593948bb8ba69f98a800deb9c02ad9f7190340622b.jpg)

![](images/0f63d1fc2b2719925623bfdb7ad2f40fce195f20394adff0456fc4dd6eba0f2d.jpg)

![](images/2cbdbc77e2284e66afbded78cb4ddd9954da5c98d27ca1a287f7fd2fc30e07f7.jpg)

![](images/66f4fe925b8a64070dd4108b5892675b05c13adf2e4a965757150850f1f3daa2.jpg)

![](images/5dc01409702427c07aeb11cac5c528e3e8e8bf545253a4836cda11d335b54ee5.jpg)

![](images/773acd1122e11576c00542dddbb937c13c9eb2c1900a9efb2285d2dff9e707ec.jpg)

![](images/197ee9d81eafcbf228264f80f6c5fa683e4fb6393045d3c35c778b4975517912.jpg)  
Extended Data Fig. 3 | FDTD simulation showing propagation of light from the diamond waveguide into the AlN waveguide. a, For a 602-nm wavelength (corresponding to the GeV colour centre ZPL). b, For a 737-nm wavelength (corresponding to the SiV colour centre ZPL).

![](images/0752a608825a2667924fcaf199deb247fbb755e8708eca938db784ddfd402cec.jpg)  
Extended Data Fig. 4 | Saturation response of a single GeV centre. a, Continuous-wave 532-nm laser excitation b, Pulsed laser excitation at 532 nm with a repetition rate of 26 MHz.

![](images/658dcbe397b93ca016ad1f6e1bce142ce4ade3e4d550f3c710ba11b4567b47d8.jpg)

![](images/ec44ad35bb720c018b09db6a33b98e66ac1445e14874067fbe8a1b95ed75965a.jpg)  
a  
Extended Data Fig. 5 | Scheme for strain-tuning emitters in a PIC platform.  
a, SEM image of type I and type II waveguides considered in this experiment. b,  
Strain distribution along the waveguides and emitters considered in the main  
text (Fig. 5). Horizontal error bars indicate the lateral uncertainty in the position of emitters and vertical error bars indicate the ion implantation straggle.

![](images/f825a8f11778fd64c32fa505f7260c26a997a6f2a3695a31774b236ff427b25c.jpg)  
Extended Data Fig. 6 | Spectral shift of GeV centres in response to strain fields. a-c, Strain response of emitter 1A (a), emitter 1B (b) and emitter 2 (c).

![](images/eb10e4b68d02f946247a00e089202fa7872ccfb25c1434993cd73f10e7bbd77e.jpg)

![](images/13e36f39a0f1b7f09e7fc7db33dd72ed46a6a7d5d72a0a6abf37e0e13c100b4a.jpg)

![](images/010afdcf5cee1671d6e289c6aebb8e3aa5107920a55cc86b268d0f624ffce264.jpg)  
Extended Data Fig. 7 | Spectral shifts for the brightest transitions. Reproducible spectral shifts between  $10\mathrm{V}$  and  $26\mathrm{V}$  for the two brightest transitions C and D for emitter 2.

![](images/0b8aabb72f453870af9e7d4b0423dfa4e854c6554ad7f5530da215d81313ca4a.jpg)  
Extended Data Fig. 8 | Optical properties during strain tuning. Top: PLE linewidths as a function of voltage. Bottom: corresponding frequency shift,  $\Delta \nu$ , of the ZPL transition.

![](images/2af32b2a77dbeb66a71bcd1df3edeb155d88f273c7a2f027b8253b79b4cd5af0.jpg)  
Extended Data Fig. 9 | Stability of the ZPL transition frequency during strain tuning. Each time slice corresponds to a single PLE linewidth measurement averaged over 2,000 experiments (about 3 min).

Article  
Extended Data Table 1 | Saturated count rates from single GeV centres in a QMC  

<table><tr><td>Channel</td><td>41</td><td>42</td><td>43</td><td>44</td><td>45</td><td>46</td><td>47</td><td>48</td></tr><tr><td>Saturated counts x 106cps</td><td>0.20(3)</td><td>0.94(24)</td><td>0.21(7)</td><td>0.80(9)</td><td>0.61(2)</td><td>0.91(13)</td><td>1.11(23)</td><td>0.31(09)</td></tr></table>