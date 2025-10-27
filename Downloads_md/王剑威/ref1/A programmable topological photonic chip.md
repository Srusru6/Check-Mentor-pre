# A programmable topological photonic chip

Received: 31 July 2023

Accepted: 19 April 2024

Published online: 22 May 2024

![](images/2a9d28639d2086a922442069344275a17aebaeaa30cae0be9ba71219fc7ed427.jpg)

Check for updates

Tianxiang Dai  $^{1,8}$ , Anqi Ma  $^{1,8}$ , Jun Mao  $^{1,8}$ , Yutian Ao  $^{2,3}$ , Xinyu Jia  $^{1}$ , Yun Zheng  $^{1}$ , Chonghao Zhai  $^{1}$ , Yan Yang  $^{4}$ , Zhihua Li  $^{4}$ , Bo Tang  $^{4}$ , Jun Luo  $^{4}$ , Baile Zhang  $^{2,3}$ , Xiaoyong Hu  $^{1,5,6,7}$ , Qihuang Gong  $^{1,5,6,7}$  & Jianwei Wang  $^{1,5,6,7}$

Controlling topological phases of light allows the observation of abundant topological phenomena and the development of robust photonic devices. The prospect of more sophisticated control with topological photonic devices for practical implementations requires high-level programmmability. Here we demonstrate a fully programmable topological photonic chip with large-scale integration of silicon photonic nanocircuits and microresonators. Photonic artificial atoms and their interactions in our compound system can be individually addressed and controlled, allowing the arbitrary adjustment of structural parameters and geometrical configurations for the observation of dynamic topological phase transitions and diverse photonic topological insulators. Individual programming of artificial atoms on the generic chip enables the comprehensive statistical characterization of topological robustness against relatively weak disorders, and counterintuitive topological Anderson phase transitions induced by strong disorders. This generic topological photonic chip can be rapidly reprogrammed to implement multifunctionalities, providing a flexible and versatile platform for applications across fundamental science and topological technologies.

Topological insulators (TIs) have garnered significant interest because of the abundant physical mechanisms underlying non-trivial bands and potential applications of topological boundary modes<sup>1</sup>. Since the discovery of the quantum Hall effect<sup>2</sup>, the intricate diagrams of topological phases have developed as a sprawling tree with intertwined branches, encompassing dimensionality<sup>3</sup>, symmetry<sup>4</sup>, non-Hermiticity<sup>5</sup> and defects<sup>6</sup>. One leap recently happened when topology met photonics<sup>7-10</sup>. Photonic systems provide numerous advantages for topological physics and technologies, such as noise-free environment, few constraints on lattice geometry, large diversity of optical materials, high controllability of optical devices and widely adoptable nonlinear optical effects<sup>8-11</sup>. Topological photonics, initially proposed as an

extension of topological materials in optical artificial structures, is emerging as an independent field and is revolutionizing optical science and technologies. For examples, integer quantum Hall  $\mathrm{TIs}^{12-14}$ , quantum spin Hall  $\mathrm{TIs}^{15,16}$ , Floquet  $\mathrm{TIs}^{17,18}$ , non-Hermitian  $\mathrm{TIs}^{19,20}$  and many other interesting topological phenomena have been observed in various photonic systems. Practical topological photonic devices—for example, topological optical delay lines $^{13}$ , topological lasers $^{21,22}$  and topological single-photon $^{23,24}$  and entangled-photon sources $^{25,26}$ —have been intensively developed and explored.

These observations of topological effects and demonstrations of topological devices are reported on a large variety of optical devices with specifically designed periodic structures or geometries. It is

essential to flexibly and precisely control topological phases of light in programmable topological photonic devices at the levels of both fundamental and applied science. First, the dynamics of topological phase transition (TPT) relies on strong reconfiguring of structural parameters of the devices. Topological invariants persist until bands cross so that a marked altering of parameters is required. In typical measurements, TPTs are observed in several different devices, or a joint multivariate effort may even be necessary[27-29]. Though TPTs can be enabled by globally tailoring the devices with an adoption of nonlinear effects[20,30,31] or mechanical displacement[32], portrayal of TPTs using more direct and accurate approaches is demanded. Individually programming each artificial atom as well as the atom-atom interactions may represent the ultimate control of the system. This however remains challenging in many natural and artificial topological systems, and also in photonics. Second, most previous observations of topological phenomena rely on static analysis of single or several samples. Comprehensively certificating topological robustness by statistical measurements, and probing interesting statistical topological phenomena such as topological Anderson insulators (TAIs)[33-35] and amorphous  $\mathrm{TIs}$ [36,37], requires the ability to individually programme artificial atoms and their interactions to control disorder. Fabricating a large number of samples with precisely controlled disorder for such statistical analysis is impractical. Third, as topology in matter derives from the collective behaviour of atoms in the lattice, the lattice geometry determines the interrelationships between neighbouring atoms and the overall topological properties. The topology of bands varies in dimensions[3], and lattices with various geometries also give different symmetries[4], resulting in TIs in different classes. Previous investigations of TIs in diverse lattices however rely on completely different samples, which necessitates custom design and fabrication of samples.

Programmable photonic integrated circuits $^{38-40}$  across a broad spectrum of advanced optical waveguide materials have been recognized as highly controllable, dynamic and scalable platforms. These are impactful in the realms of both fundamental science and practical applications, including telecommunication and interconnection $^{41,42}$ , optical information processing $^{43,44}$ , light detection and ranging $^{45,46}$  and quantum information processing and communication $^{47-49}$ . Unlike conventional linear-optical circuits that allow merely forward operations of classical $^{43,44,50}$  and quantum $^{47,48,51}$  states of light, a new variety of recirculating photonic networks $^{52-54}$  that allow both forward and backward operations of light has been proposed and demonstrated, marking a departure from previous models. These recirculating photonic circuits intrinsically integrate two types of key photonic component--interferometers and resonators, hence serving as a genetic platform for photonic classical and quantum science technologies. In particular, these systems may even support the emulation of rich topological physics in quantum materials in a fully programmable manner.

In this work, we report a highly programmable topological photonic chip. The chip has generically integrated a lattice of large-scale silicon photonic nanowaveguide circuits and microring resonators, and is fabricated using complementary metal-oxide-semiconductor processes. When we consider each ring as an artificial atom, our photonic chip can be regarded as an artificial lattice that allows arbitrary individual control of atoms as well as the coupling strength and hopping phase between atoms. The generic chip can be rapidly reprogrammed to implement different functionalities: for example, to dynamically transform topological phases of Floquet TIs, observe statistical topological phenomena (statistical analysis of topological robustness and topological Anderson phase transitions) and realize a diverse class of TIs with various lattices (for example, one-dimensional (1D) Su-Schrieffer-Heeger TIs, and two-dimensional Floquet TIs in square and honeycomb lattices). Our work prototypes a flexible, versatile and instantly reprogrammable topological photonic platform.

Figure 1 illustrates an overall concept. The photonic topological insulating chip is devised on a two-dimensional lattice of

coupled-microring resonators and nanophotonic circuits, as shown in Fig. 1a. Our topological chip is based on recirculating photonic circuits with unique capabilities of operating light states both forwards and backwards $^{52-54}$ . One microring emulates one atom, a Mach-Zehnder interferometer (MZI) emulates tunable atom-atom interaction and the photonic chip emulates the artificial atom lattice. In experiment, we use a square lattice of six unit cells by six unit cells, embedding a total of 96 microrings with identical perimeters of  $1,234.4 \mu \mathrm{m}$ , each of which has an intrinsic quality factor of the order of  $10^{5}$ . The propagation loss of the silicon nanowaveguides is  $2.4 \mathrm{~dB} \mathrm{~cm}^{-1}$ . As shown in Fig. 1e, the resonance of each microring can be individually controlled, and the coupling between microrings (both strength and phase) can be arbitrarily controlled by MZIs with an ultrahigh extinction ratio of about  $50 \mathrm{~dB}$  and ultralow loss of about  $0.07 \mathrm{~dB}$ . Each phase shifter is thermo-optically driven by  $30 \mathrm{mW}$  power for  $2 \pi$  modulation, and accessed by electronic routing circuits. Characteristics of microrings and interferometers such as loss and crosstalk are provided in Supplementary Notes 2.1 and 2.2. The device operates at the wavelength of  $1,525 \mathrm{~nm}$ . The device properties (for example, loss and power consumption) fall within the average range for silicon photonic technologies at this wavelength. From the technological perspective, the demonstration of the topological chip is the result of fabrication, controlling and packaging of large-scale photonic circuits, and the completeness of measurements. One fabricated and packaged chip is shown in Fig. 1b-d. The high-level controllability and programmability of the generic photonic chip enable sophisticated implementations of dynamic TPTs, statistical topological processes and diverse topological lattices (Fig. 1g). As an initial test of the flexible and fast programmability of the generic chip, Fig. 1f shows imaged field distributions of '@PKU' symbols, and Supplementary Video 1 shows real-time modulations of the letters 'HELLO'.

We first report arbitrary controls of the band structure of Floquet TIs in the three-particle model, which has been proposed to study non-Hermiticity in Floquet TIs $^{55}$ . The famous Floquet theory provides an effective temporal approach for TIs with no need to truly break time-reversal symmetry $^{18,56}$ . Demonstrating the full modulation capability requires comprehensive controls of structural parameters, which remain experimentally exclusive. A zoom-in view of a three-ring unit is shown in Fig. 2a and the real structure is shown in Fig. 1d. By reconfiguring four parameters on the coupling strength  $(\theta_{1-4})$  and five parameters on the phase  $(\varphi_{\mathrm{L1-L4}}$  and  $\varphi_{\mathrm{s}})$  in a three-ring unit cell, arbitrary topology in the three-band structure can be constructed on the basis of the Floquet band theory. We experimentally characterize two types of Floquet TPT, which are driven by the coupling strength  $(\theta)$  and resonant phase  $(\varphi_{\mathrm{s}})$ , respectively.

For  $\theta$ -driven TPTs, simultaneously tuning all coupling parameters  $\theta_{1-4} = \theta$  and across the TPT critical point ( $\theta = 2\arcsin(\sqrt{2} - 1) \approx 0.272\pi$ ), the bandgaps close and reopen, resulting in disappearance of the topological edge modes (indicated by  $\mathbf{1}$  in Fig. 2b) and the phase transition at bandgap  $\mathbf{1}$  from a topological phase to a trivial phase. The topologically invariant winding number ( $\mathcal{W}$ ) is used to explicitly portray the topology (that is,  $\mathcal{W} = 1$  for the non-trivial phase, while  $\mathcal{W} = 0$  for the trivial phase). Topological invariants are also intuitively reflected in transport properties. Figure 2b shows the theoretical and experimental transmission spectra with a fine tuning of  $\theta$  from 0 to  $\pi$  (that is, transmittance of MZIs from 1 to 0). The flat and high-transmission regimes (outlined by dashed lines) indicate topological edge modes in one free spectral range (FSR). One FSR corresponds to one  $2\pi / T$  period in quasienergy  $\epsilon$ , where  $T$  is the period of Floquet evolution. Figure 2c,d shows two measured spectra before and after the TPT point, corresponding to the calculated projected bands plotted in Fig. 2e,f. At certain typical points in the spectra, real-space distributions of electromagnetic fields are imaged using an infrared camera (see examples in Fig. 2g-j). Figure 2g,h records light distributions before and after TPTs, while Fig. 2i displays an always existing

![](images/e45ed93618b194fa49acd892a11ec56174f88a7d20201d5e2f4ca9d87b5c4a89.jpg)

![](images/897c92bb5443efad9ccb1dc0b19f0b02c1584360a407aa9431ce214797388ee1.jpg)

![](images/67622dd84317e039dba64d02bfee2a16727f642bb2e8fddf50ba66e6c9ac6e8e.jpg)

![](images/fed1ca7d9f3a9d29cfbe0245e4d0a2f36ae0b7d14a98d9d4c0cbba6334ead358.jpg)

![](images/7d9d84a6bb42a6ea3e2e9cb804c780c29f907878141ce7616028b45d046a3025.jpg)

![](images/bc6686d5ee274c712b78b9a1520f56f971a8684fc6b173758e2441f6d16c8e03.jpg)

![](images/88b45bc4f41f3b0b5bf6a1c41bd1c4aef7695425f84df682eb85c7710daf96cc.jpg)  
Fig. 1 | A fully programmable topological photonic chip. a, Conceptual diagram. It integrates large-scale photonic nanowaveguide circuits and microring resonators. In total, 96 microrings with high quality factors are regularly positioned in a square lattice of six unit cells by six unit cells. All rings (artificial atoms) can be individually controlled by integrated thermo-optical phase shifters (gold parts), achieving arbitrary resonant phases in all rings, phase differences between the two paths of link rings and coupling strength between neighbouring rings. At the boundaries, 24-in-by-24-out ports are connected to the lattice. b, Photograph of a fabricated topological chip. The silicon chip is fabricated using complementary metal-oxide-semiconductor processes and it monolithically integrates 2,712 components in an  $11\mathrm{mm} \times 7\mathrm{mm}$  footprint,

![](images/cfb67a01c2ac6c405b06dbab0e4c04ef065817591bdace513224e81cde26a68b.jpg)  
including 408 low-loss directional couplers, 300 phase shifters with 528 thermal isolators, 48 grating couplers for optical access, 120 tapping ports for light field imaging and 600 electronic access and 708 transmission lines. c, Photograph of a packaged chip. The chip is wire bonded on a multilayer printed circuit board (PCB). External electronic drivers with 600 channels are used to individually control 300 phase shifters. d, Optical microscopy image of a three-ring unit cell. e, Diagrams of reconfigurable optical components, including MZIs and phase shifters. f, Imaging of real-space distributions of electromagnetic field. As an example, the chip is flexibly reprogrammed to display @PKU. g, The generic chip is reprogrammed to implement multifunctionalities: dynamic TPTs, observation of statistical topological phenomena and benchmarking of TIs in various lattices.

![](images/f1a9c94b6a9ac5ed15d70c5214343fc436d90fded7c86b14a817d446249d12ec.jpg)

edge mode at bandgaps ②. In bulk modes, light dissipates into the bulk (Fig. 2j). Topological immunity against structural defects is tested in Fig. 2k, where one cell is removed by adjusting its coupling to the bar state forming a lattice defect. This indicates an unique ability to withstand and tolerate structure defects. Our topological chip could provide fertile ground for studying the critical conditions for the emergence of defect-induced states<sup>6</sup>.

For  $\varphi_{\mathrm{s}}$ -driven TPTs, in typical Floquet TIs, introducing local phase modulations is challenging, owing to the globally consistent Floquet period in the time domain. On our chip, Floquet TPTs also can be realized by finely altering  $\varphi_{\mathrm{s}}$  in all the site rings. In Fig. 3a, by turning  $\varphi_{\mathrm{s}}$  from

0 to  $\pi$ , we continue to reduce the number of non-trivial bandgaps in one FSR from two to one in the  $\varphi_{\mathrm{S}}$ -TPT (when we set  $\theta = 0.4\pi$  and phase in link rings  $\varphi_{\mathrm{L1-L4}} = 0$ ). Band deformations and changes of topological invariants are shown in the calculated band structures. Bandgaps become trivial after the critical point  $\varphi_{\mathrm{S}} = 0.58\pi$ . As there is a  $2\pi$  period on resonant phases, it is expected that the spectrum will return to its original state when  $\varphi_{\mathrm{S}} = 2\pi$ . Consequently, there must be another TPT to regenerate topological edge modes at the forbidden bandgaps when increasing  $\varphi_{\mathrm{S}}$  from  $\pi$  to  $2\pi$ . Figure 3b displays consistent spectra between theory and experiment, showing the disappearance of edge states at bandgaps within  $[0, \pi]$  evolution and the re-emergence of

![](images/9d1fdadba4557641de3da41949c96e403878452292e37280b4b001af46646d91.jpg)  
a

![](images/8783d78b607c3e829570d05e5caf1f5dda90cac0fc5ff5f37eef786e7d6894fb.jpg)  
b

![](images/4ea82b0940bdd26ceb5a613731f61c1105ee225ad43bc753c73b53acb6b89966.jpg)

![](images/d8c22ffaf460b19a02ede92eca1d2f238a71410503362a8dad8b8d0e90c7938e.jpg)  
e

![](images/c295a6a6c4b1dd51177f22d7501b1ae3928a211aef45864b60e3f7d47f1f6ffe.jpg)

![](images/70f5e032b2ff5e65ae746cae4658cbd22291e0021a9e282f6aee861b1f295f12.jpg)

![](images/d20a262069a9a5b56be53703ed2b4179fe959af230dfb1701f08d523138f5b83.jpg)  
Theoretical results are in good agreement with experimental results. Boundary states at bandgaps 1 disappear with a continuous variation of  $\theta$  near the critical point at  $\theta = 0.272\pi$ , while edge modes in bandgaps 2 and 3 exist throughout the entire range of  $\theta$  variation. The attenuation of light for large  $\theta$  in experiment is due to resonant enhancement in rings, which increases the effective optical length and thus the loss. c-f, Measured spectra at  $\theta = 0.1\pi$  (strong coupling, c)

Fig. 2 | Coupling-strength-controlled TPTs in Floquet TIs. a, A three-ring model for Floquet TIs. Using nine parameters in a single unit cell, it fully describes the quasienergy band structure. b, TPTs driven by coupling strength. Transmission spectra as functions of wavelength  $\lambda$  and the parameter  $\theta$  on coupling strength are shown, where  $\theta$  is negatively correlated with the coupling strength and the amplitude transmittance of an MZI is  $\cos(\theta/2)$ . The boundaries of non-trivial bandgaps in one FSR are indicated by purple dashed lines.  
and  $\theta = 0.32\pi$  (weak coupling, d) and their respective calculated band structures (e,f). The windows of edge modes are visually enhanced. g-j, Imaged real-space distributions of electromagnetic field under different points marked in spectra in c,d: TPT from topological edge modes (g) to forbidden bandgaps (h) at bandgap 1, edge modes at bandgaps 2 in weak-coupling regime (i) and randomly  
![](images/99002bb835513bd58d551314557fe79efcad7c8e9e91a63b2e2cb57031dbd999.jpg)  
distributed bulk mode from the non-degenerate bulk bands (j). k, A boundary cell in Floquet topological insulators (FTIs) is removed by adjusting its coupling to the 'bar' state, which forms a lattice defect. High-transmission topological edge modes bypass the hole and present its robustness against atomic vacancies. Note that on the link ring paths we tapped out  $-35$  dB light using diffractive grating couplers for better imaging of light fields, which results in the appearance of regularly distributed bright spots. Noise at the top right arises from light reflection from the input fibre.

edge states at bandgaps  $\mathbf{1}$  within  $[\pi, 2\pi]$  evolution. Interestingly, the seemingly negligible  $2\pi$  phase in site rings in fact leads to a reversal of band structure and a global phase shift to lower quasienergy that corresponds to longer wavelength. That being said, the non-trivial bandgaps  $\mathbf{2}$  and  $\mathbf{3}$  at  $\varphi_{\mathrm{s}} = 0$  correspond to non-trivial bandgaps  $\mathbf{1}$  and  $\mathbf{2}$  at  $\varphi_{\mathrm{s}} = 2\pi$ , respectively.

Robustness, as the most intriguing property of topological edge modes, allows protection of transport immune to imperfections.

As long as the presence of disorder does not interrupt the band structure and the bandgaps remain open, the topological invariants are always constant and light transport along the edge modes is robust. This property has led to many potential applications $^{13,21-26}$ . Previously, single or several samples are fabricated, sometimes together with numerical simulation, to verify topological robustness. By harnessing the individual programmability, we experimentally validate the robustness of topological edge modes by statistical measurements.

![](images/4f66c25c0fd20ce2efcec9be919ff294e5561702c52b06e3358efb207bfd7500.jpg)  
a  
b

![](images/baaf697cc083fe41857035a1adf97bcd3520014b60c5cc507ad5a1401ac01545.jpg)

![](images/36e734d467a314b26b233ed406b1e4b2c15464eb822809f4ce3be6329a154521.jpg)

![](images/8711b3165684eca58b807bb405dc5a62625140d45425a8700bf67c746bb457df.jpg)  
Fig. 3 | Resonant-phase-controlled TPTs and statistical verification of topological robustness. a, Calculated band structures in  $\varphi_{\mathrm{s}}$ -controlled TPT. Starting from the weak coupling regime ( $\theta = 0.4\pi$ ), by increasing  $\varphi_{\mathrm{s}}$  from 0 to  $\pi$ , site rings and link rings become detuned, reaching a maximum detuning at  $\varphi_{\mathrm{s}} = \pi$ . TPT occurs at bandgap ③ when  $\varphi_{\mathrm{s}} = 0.58\pi$ , making it a trivial forbidden bandgap. b, Theoretical and experimental transmission spectra as functions of  $\lambda$  and  $\varphi_{\mathrm{s}}$ . As a global phase shift is introduced by  $\varphi_{\mathrm{s}}$ , TPT occurs at bandgap ①. The mapping of bandgaps changes from  $\{\mathbf{1}, \mathbf{2}, \mathbf{3}\}$  to  $\{\mathbf{3}, \mathbf{1}, \mathbf{2}\}$  after a  $2\pi$  evolution of phase  $\varphi_{\mathrm{s}}$ . c, Calculated projected band structures at  $\varphi_{\mathrm{s}} = 0.8\pi$ , plotted as a reference to demonstrate the robustness of topological edge modes. d,e, Experimental verification of topological robustness with statistical measurements by individually controlling the phase disorders in all rings. The

![](images/5d47e26da121a15f4cdf6c4e7d76a792140284b531e34bef0d5176fd73b9e529.jpg)  
generated random phase obeys the same uniform distribution in the range of  $\delta[-0.5, 0.5]$ . d, A set of 100 samples with uniformly distributed random phases is chosen at  $\delta = 0.1\pi$  in measurement. Measured transmission spectra for the disordered devices are shown as the grey background, and the spectrum for an ideal device without disorder is plotted as a blue line. In the topological edge modes the flat plateaus with high transmission are only slightly influenced, while in all other regimes severe broadening and small dips owing to obstruction from random local modes appear. e, The measured s.d. (normalized) of transmission spectra under different strengths of disorder. Evident windows with low fluctuations correspond exactly to the regimes of topological edge modes.  $\delta$  increases from 0 to  $0.2\pi$  with an interval of  $0.01\pi$ . S.d. is colour coded and the key is provided at the bottom right.

![](images/01c04703f7ff07758c705df30c3d0d5e703a3ab1bf454a03a13ac531ee54ee52.jpg)  
C

![](images/fdd1a6739b5dc1352464a146bdaa9ecfe51546ab26ae6ddcf2beadf82c8b857a.jpg)

Random perturbations on resonant phases with a uniform distribution of  $\delta[-0.5, 0.5]$ , in which the probability density is  $1 / \delta$ , are added to all microrings. We consider a non-trivial device with an initial configuration of  $\varphi_{s} = 0.8\pi$ ; see its band structure in Fig. 3c. A set of 100 samples with precisely controlled disorder at  $\delta = 0.1\pi$  is generated and tested on a single chip. The collections of these statistical measurements (grey lines) are shown in Fig. 3d. The spectrum for an ideal device with no disorder (blue line), in which the topological edge modes in bandgaps are wide and flat high-transmission plateaus, is plotted for comparison. In the presence of disorder, the high-transmittance plateau exhibit only small fluctuations in topological edge modes, but large fluctuations in bulk modes. We then estimate the normalized s.d. of transmittance over 100 samples for different levels of disorder (Fig. 3). With these statistical measurements, the observation of low-noise windows for topological edge modes unambiguously confirms the topological robustness against a certain degree of disorder. Moreover, despite the presence of crosstalk when operating a large-scale photonic chip (Supplementary Note 2.3), such inherent topological robustness provides substantial protection. This chip is inherently protected against crosstalk that may take place in real controls and fabrication disorder that may occur in a clean room.

Despite the superiority of topological transport, strong disorder may lead to marked deformation of bands and even disrupt the band topology, but this does not mean the properties of the original TI will completely disappear. Interestingly, under specific conditions, the unidirectional transport of the boundary states will still occur in the presence of strong disorder or even amorphous structures[33-37]. Exploring order within areas of disorder is the charm of topology, which particularly requires a highly programmable platform with individual controllability. Recently, the emergence of counterintuitive TAls from trivial phases has been successfully observed, by

inducing sufficiently strong areas of disorder in one sample $^{33}$ . Similar to Anderson localization $^{57}$ , topological Anderson insulation is also a statistical phenomenon for waves in disordered lattices. Such statistical measurement and verification of TAls have not been reported in optical systems, to the best of our knowledge. Figure 4b illustrates the random phase distribution in the TAI lattice in the presence of strong disorder. We first consider an ideal lattice in the absence of disorder;  $\theta$  is set as  $0.3\pi$ , constructing one trivial bandgap within one FSR. We are interested here in the bandgaps that used to be forbidden, that is, the dips of blue spectra in Fig. 4c,d. Experiment and simulation results of averaged transmission spectra over 100 samples with different levels of disorder in the resonant phase are reported in Fig. 4c,d, respectively. A peak gradually emerges at the windows of forbidden bandgaps (indicated by the red arrow) as the strength of disorder reaches a sufficiently large value, indicating the occurrence of topological Anderson phase transitions. The emergence of the TAI phase can be portrayed by real-space topological invariants $^{18,58,59}$ . Analogous to the winding number  $\mathcal{W}_{\epsilon}$  in momentum space, the real-space  $\mathcal{W}_{\mathrm{real}}$  related to non-trivial bandgaps approaches unity, while it fluctuates around zero for trivial bandgaps. According to the averaged  $\mathcal{W}_{\mathrm{real}}$  in Supplementary Fig. 23, a non-zero plateau obviously arises from the ordinary zero dip in forbidden bandgaps. Moreover, Fig. 4e shows the imaged real-space field distributions with an increase of disorder, each of which is an overlaid distribution of all 100 samples for better characterization of the dynamics of phase transitions. The TAI boundary modes break free from the localization near the input, and unidirectionally move along boundaries with an exponential decay into the bulk lattice. In contrast, the same measurements were conducted in trivial coupled resonators of optical waveguides (CROW) (Fig. 4f,g inset). The shape of the spectra remains unchanged and no TAI boundary modes are observed, as shown in Fig. 4f,g.

![](images/0d57315f63614ad6bd4feeec1524f70fc5ef2e9acdfa242df73f8aff3100f7ea.jpg)  
a  
Lattice w/o disorder

![](images/0ac26f9ad1ef45821cc82cac605003977fdf393712e9ddb3d6e71d250899ba36.jpg)  
b  
Lattice with strong disorder

![](images/f1b9312cf43b8c4ff82c253cdbc5a1e09cc19801daead474abe8288ed30b5922.jpg)  
C  
TAI boundary mode

![](images/08efefb79516dcf03cccff82e24133121181633616e8e7173aa4aa56e4d7657b.jpg)  
d

![](images/20234d3398d5c82c0f553ba9d250005a0abfd4d112222f131b46c80dd791e3fe.jpg)  
f  
Fig. 4 | Observation of topological Anderson phase transitions with statistical measurements on individually programming the TI with strong disorder. a, Ideal Floquet TI in weak-coupling regime  $(\theta = 0.3\pi)$  with no disorder. All microrings are matched to resonance. There is a forbidden bandgap within one FSR. b, TAI induced by strong disorder. Topological Anderson phase transitions occur at the forbidden bandgaps and connect them with TAI boundary modes. Statistical measurements of the TAI with a large variety of disorder are necessary to observe the topological Anderson phase transitions, which are realized on a single device by individually controlling phase disorder in all rings in our experiment. c,d, Measured (c) and simulated (d) transmission spectra of the TAI with different levels of disorder. For each level of disorder, 100 samples are generated on the chip for statistical measurements, and the mean spectrum is plotted. With an increase of disorder, an intriguing peak

![](images/0e798b2786362a63f544adfa77eb06f9c4fff384350bdcb103f78d61e8b30942.jpg)  
g  
that represents the TAI boundary mode (indicated by the red arrow) gradually emerges at the low-transmission dip where the forbidden bandgap used to be in the ideal lattice with no disorder. e, Imaging the dynamic process of topological Anderson phase transitions. Each image is an accumulated field distribution of 100 samples. The phase transition from a forbidden mode to a TAI boundary mode transported along the upper boundary is observed. Simulation results are shown for comparison, and are in good agreement with experimental results. In contrast to random diffusions of bulk modes, the TAI boundary modes propagate along the boundary and rapidly decay into the bulk. f,g, Measured (f) and simulated (g) transmission spectra of a 1D trivial device. The shape of the transmission spectra does not change with increasing disorder, and the low-transmission dip corresponding to the forbidden bandgap remains a dip (indicated by the blue arrow); that is, no phase transition occurred.

![](images/466df3ea8d1ba8ab73370112dbd0bc474e01eb9ce1cb383b0fe311ebec9011b6.jpg)  
e

We further benchmark photonic TIs in various lattice structures. Experimental results for the well known Su-Schrieffer-Heeger 1D TIs are shown in Supplementary Fig. 20. The redundant dimension for the 1D models in a two-dimensional lattice allows observations of the non-Hermitian skin effect in Supplementary Fig. 21, and other unordinary experiments such as non-reciprocity and next-nearest-neighbour coupling are implementable. Moreover, it is also possible to achieve other two-dimensional lattice geometries beyond the inherent square lattice by reprogramming microrings. Figure 5 illustrates an example of equivalent Floquet TIs in the honeycomb lattice. A perfect

correspondence between the measured transmission spectra and simulated projected band structures in the strong-coupling regime  $(\theta = 0.08\pi)$  and weak-coupling regime  $(\theta = 0.24\pi)$  is shown in Fig. 5e-h. When  $\theta$  is larger than  $0.19\pi$ , TPTs occur at the bandgaps across  $\epsilon = \pi /T$  and the flat high-transmission plateau turns into a blocked dip. Distinct real-space field distributions for different modes are shown in Fig. 5b-d, including topological edge modes conducting along the honeycomb boundaries, dissipatively distributed bulk modes and prohibitively forbidden bandgaps. By distinguishing the winding number, we observe phase transitions in a five-bulk-band structure.

![](images/2f271e6160b2408718b754bfac4b28ec8ba690941d725a09d2a0ae519a057cc9.jpg)

![](images/dc183d6de0882612ae13a1f223f0fb7618d2bcfce4e3b471b326d2582f090644.jpg)  
b  
Fig. 5 | Floquet TIs in the honeycomb lattice on reconfiguring the lattice geometry. a, A reconfigured square lattice that is equivalent to the honeycomb lattice. b–d, Measured real-space distributions of light field in different modes: topological edge mode (b), bulk mode (c) and forbidden bandgap (d). e,f, Measured transmission spectrum (e) and calculated projected band (f) when the device works at  $\theta = 0.08\pi$ . There are five bulk bands in one FSR, distinct from

![](images/7a05e39eb6a72a16ac1a7b037b01fc78ec5e55d8a1a041a9116e2e2fb00f4372.jpg)  
C

![](images/01b9d9f1d865aaaae1a145c29f7ee00c20c9ce23de6147120d5601e60e821efc.jpg)

![](images/c45d8f9a8cb83e510fdf8cbba9890ae8954e881ac3c5f641cb5e790e4b28bca1.jpg)

![](images/2456d4390fb26da52db0c8af0f2a7b5c758f0d86e5eb6498483e36adc731451d.jpg)

![](images/c30196ee3ff00497783e80e043f6c41a7ef2cc0aaed3c1ad9c3891c1face4a1e.jpg)

![](images/2552a01283d8c140713ed6c12418c3fd549aee889b6ca7dfa15590669ed6fc89.jpg)  
the three-particle model in a square lattice. The winding numbers  $\mathcal{W}$  in all bulk bandgaps are unity, implying the existence of non-trivial boundary modes.  $\mathbf{g},\mathbf{h}$ , Measured transmission spectrum (g) and calculated projected band (h) when the device works at  $\theta = 0.24\pi$ . When decreasing the coupling strength to the critical point of  $\theta = 0.19\pi$ , TPTs occur at the bandgap across  $\epsilon = \pi /T$ , turning it into a trivial forbidden bandgap ( $\mathcal{W} = 0$ ), while other bandgaps remain non-trivial.

Such multiple non-trivial topological phases in standard honeycomb lattices have been achieved in another recent work $^{60}$ , using chain-driven laser-written waveguides. This effectively validates the correctness and reliability of our programmable topological chip. In addition, the results show that, by reconfiguring the device, a squared mesh-based TI can be equivalently translated into a TI based on the hexagonal mesh $^{53,54}$ . Such topological equivalence is also indicated in a scheme shown in Supplementary Fig. 25.

This work has demonstrated a flexibly and rapidly programmable topological photonic chip. Multifunctionalities are benchmarked by reprogramming the generic chip, including dynamic TPTs, realizations of diverse topological lattices and implementations of statistical measurement of topological processes. Our generic chip could be directly used to discover topological phases of light and understand exotic phenomena. The chip possesses unique backward operations in a large-scale lattice of optical resonators and it may provide an alternative solution for classical $^{38-40}$  and quantum $^{47-49}$  information processing and computing tasks. It could provide flexible hardware to model the lattice of topological materials and predict their physical properties. Such reprogrammability could even allows dynamic simulation of real-world materials, where disorder, inhomogeneity and anisotropy are commonly present. To emulate these complex topological materials and matter, a larger-scale lattice is required. Further scaling of the topological chip is achievable by delicate design of the recirculating photonic circuits and electrical routing circuits. Advanced silicon-based integrated photonic technologies may provide the ultimate solutions for very-large-scale integrated programmable TIs, using heterogeneous integration of different optical materials on silicon $^{61}$  and photonics-electronics packaging or co-integration $^{62}$ . Programmable topological photonic chips may

provide one generic platform for fundamental science and topological technologies.

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41563-024-01904-1.

# References

1. Hasan, M. Z. & Kane, C. L. Colloquium: Topological insulators. Rev. Mod. Phys. 82, 3045-3067 (2010).  
2. Klitzing, K. V., Dorda, G. & Pepper, M. New method for high-accuracy determination of the fine-structure constant based on quantized Hall resistance. Phys. Rev. Lett. 45, 494-497 (1980).  
3. Ryu, S., Schnyder, A. P., Furusaki, A. & Ludwig, A. W. Topological insulators and superconductors: tenfold way and dimensional hierarchy. New J. Phys. 12, 065010 (2010).  
4. Slager, R. J., Mesaros, A., Juricic, V. & Zaanen, J. The space group classification of topological band-insulators. Nat. Phys. 9, 98-102 (2013).  
5. Özdemir, S. K., Rotter, S., Nori, F. & Yang, L. Parity-time symmetry and exceptional points in photonics. Nat. Mater. 18, 783-798 (2019).  
6. Lustig, E. et al. Photonic topological insulator induced by a dislocation in three dimensions. Nature 609, 931-935 (2022).  
7. Haldane, F. D. M. & Raghu, S. Possible realization of directional optical waveguides in photonic crystals with broken time-reversal symmetry. Phys. Rev. Lett. 100, 013904 (2008).

8. Lu, L., Joannopoulos, J. D. & Soljacic, M. Topological photonics. Nat. Photon. 8, 821-829 (2014).  
9. Ozawa, T. et al. Topological photonics. Rev. Mod. Phys. 91, 015006 (2019).  
10. Khanikaev, A. B. & Shvets, G. Two-dimensional topological photonics. Nat. Photon. 11, 763-773 (2017).  
11. Slobozhanyuk, A. et al. Three-dimensional all-dielectric photonic topological insulator. Nat. Photon. 11, 130-136 (2017).  
12. Wang, Z., Chong, Y., Joannopoulos, J. D. & Soljačić, M. Observation of unidirectional backscattering-immune topological electromagnetic states. Nature 461, 772-775 (2009).  
13. Hafezi, M., Demler, E. A., Lukin, M. D. & Taylor, J. M. Robust optical delay lines with topological protection. Nat. Phys. 7, 907-912 (2011).  
14. Zilberberg, O. et al. Photonic topological boundary pumping as a probe of 4D quantum Hall physics. Nature 553, 59-62 (2018).  
15. Khanikaev, A. B. et al. Photonic topological insulators. Nat. Mater. 12, 233-239 (2013).  
16. Bliokh, K. Y., Smirnova, D. & Nori, F. Quantum spin Hall effect of light. Science 348, 1448-1451 (2015).  
17. Rechtsman, M. C. et al. Photonic Floquet topological insulators. Nature 496, 196-200 (2013).  
18. Rudner, M. S., Lindner, N. H., Berg, E. & Levin, M. Anomalous edge states and the bulk-edge correspondence for periodically driven two-dimensional systems. Phys. Rev. X 3, 031005 (2013).  
19. Wang, K. et al. Generating arbitrary topological windings of a non-Hermitian band. Science 371, 1240-1245 (2021).  
20. Dai, T. et al. Non-Hermitian topological phase transitions controlled by nonlinearity. Nat. Phys. 20, 101-108 (2024).  
21. Bandres, M. A. et al. Topological insulator laser: experiments. Science 359, eaar4005 (2018).  
22. Zeng, Y. et al. Electrically pumped topological laser with valley edge modes. Nature 578, 246-250 (2020).  
23. Mittal, S., Goldschmidt, E. A. & Hafezi, M. A topological source of quantum light. Nature 561, 502-506 (2018).  
24. Blanco-Redondo, A., Bell, B., Oren, D., Eggleton, B. J. & Segev, M. Topological protection of biphoton states. Science 362, 568-571 (2018).  
25. Mittal, S., Orre, V. V., Goldschmidt, E. A. & Hafezi, M. Tunable quantum interference using a topological source of indistinguishable photon pairs. Nat. Photon. 15, 542-548 (2021).  
26. Dai, T. et al. Topologically protected quantum entanglement emitters. Nat. Photon. 16, 248-257 (2022).  
27. Kudyshev, Z. A., Kildishev, A. V., Boltasseva, A. & Shalaev, V. M. Photonic topological phase transition on demand. Nanophotonics 8, 1349-1356 (2019).  
28. Weidemann, S., Kremer, M., Longhi, S. & Szameit, A. Topological triple phase transition in non-Hermitian Floquet quasicrystals. Nature 601, 354-359 (2022).  
29. Liu, G.-G. et al. Topological Chern vectors in three-dimensional photonic crystals. Nature 609, 925-930 (2022).  
30. Maczewsky, L. J. et al. Nonlinearity-induced photonic topological insulator. Science 370, 701-704 (2020).  
31. Xia, S. et al. Nonlinear tuning of PT symmetry and non-Hermitian topological states. Science 372, 72-76 (2021).  
32. Cheng, X. et al. Robust reconfigurable electromagnetic pathways within a photonic topological insulator. Nat. Mater. 15, 542-548 (2016).  
33. Stützer, S. et al. Photonic topological Anderson insulators. Nature 560, 461-465 (2018).  
34. Li, J., Chu, R. L., Jain, J. K. & Shen, S. Q. Topological Anderson insulator. Phys. Rev. Lett. 102, 136806 (2009).  
35. Meier, E. J. et al. Observation of the topological Anderson insulator in disordered atomic wires. Science 362, 929-933 (2018).

36. Mitchell, N. P., Nash, L. M., Hexner, D., Turner, A. M. & Irvine, W. T. Amorphous topological insulators constructed from random point sets. Nat. Phys. 14, 380-385 (2018).  
37. Jia, Z. et al. Disordered topological graphs enhancing nonlinear phenomena. Sci. Adv. 9, eadf9330 (2023).  
38. Capmany, J. and Pérez, D. Programmable Integrated Photonics (Oxford Univ. Press, 2020).  
39. Bogaerts, W. et al. Programmable photonic circuits. Nature 586, 207-216 (2020).  
40. Lipson, M. The revolution of silicon photonics. Nat. Mater. 21, 974-975 (2022).  
41. Chen, X. et al. The emergence of silicon photonics as a flexible technology platform. Proc. IEEE 106, 2101-2116 (2018).  
42. Smit, M., Williams, K. & van der Tol, J. Past, present, and future of InP-based photonic integration. APL Photon. 4, 050901 (2019).  
43. Shen, Y. et al. Deep learning with coherent nanophotonic circuits. Nat. Photon. 11, 441-446 (2017).  
44. Pai, S. et al. Experimentally realized in situ backpropagation for deep learning in photonic neural networks. Science 380, 398-404 (2023).  
45. Shu, H. et al. Microcomb-driven silicon photonic systems. Nature 605, 457-463 (2022).  
46. Zhang, X., Kwon, K., Henriksson, J., Luo, J. & Wu, M. C. A large-scale microelectromechanical-systems-based silicon photonics LiDAR. Nature 603, 253-258 (2022).  
47. Bao, J. et al. Very-large-scale integrated quantum graph photonics. Nat. Photon. 17, 573-581 (2023).  
48. Zheng, Y. et al. Multichip multidimensional quantum networks with entanglement retrievalability. Science 381, 221-226 (2023).  
49. Wang, J. et al. Integrated photonic quantum technologies. Nat. Photon. 14, 273-284 (2020).  
50. Miller, D. A. B. Self-configuring universal linear optical component. Photon. Res. 1, 1-15 (2013).  
51. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
52. Zhuang, L., Roeloffzen, C. G., Hoekman, M., Boller, K. J. & Lowery, A. J. Programmable photonic signal processor chip for radiofrequency applications. Optica 2, 854-859 (2015).  
53. Pérez, D. et al. Multipurpose silicon photonics signal processor core. Nat. Commun. 8, 636 (2017).  
54. Zand, I. & Bogaerts, W. Effects of coupling and phase imperfections in programmable photonic hexagonal waveguide meshes. Photon. Res. 8, 211-218 (2020).  
55. Li, M., Ni, X., Weiner, M., Alu, A. & Khanikaev, A. B. Topological phases and nonreciprocal edge states in non-Hermitian Floquet insulators. Phys. Rev. B 100, 045423 (2019).  
56. Rudner, M. S. & Lindner, N. H. Band structure engineering and non-equilibrium dynamics in Floquet topological insulators. Nat. Rev. Phys. 2, 229-244 (2020).  
57. Segev, M., Silberberg, Y. & Christodoulides, D. N. Anderson localization of light. Nat. Photon. 7, 197-204 (2013).  
58. Mondragon-Shem, I., Hughes, T. L., Song, J. & Prodan, E. Topological criticality in the chiral-symmetric AllI class at strong disorder. Phys. Rev. Lett. 113, 046802 (2014).  
59. Kitaev, A. Anyons in an exactly solved model and beyond. Ann. Phys. (N. Y.) 321, 2-111 (2006).  
60. Pyrialakos, G. G. et al. Bimorphic Floquet topological insulators. Nat. Mater. 21, 634-639 (2022).  
61. Xiang, C. et al. 3D integration enables ultralow-noise isolator-free lasers in silicon photonics. Nature 620, 78-85 (2023).  
62. Atabaki, A. H. et al. Integrating photonics with silicon nanoelectronics for the next generation of systems on a chip. Nature 556, 349-354 (2018).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this

article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2024

# Data availability

The data that support the findings of this study are available from the corresponding authors upon reasonable request.

# Acknowledgements

We acknowledge support from the National Natural Science Foundation of China (12325410, 61590933, 11734001, 92150302, 11527901, 61904196, 62274179, 62235001), the Innovation Program for Quantum Science and Technology (2021ZD0301500), the National Key R&D Program of China (2019YFA0308702, 2018YFA0704404, 2022YFB2802400), Beijing Natural Science Foundation (Z220008), the Guangdong Major Project of Basic and Applied Basic Research (2020B0301030009) and the Singapore National Research Foundation Competitive Research Program (NRFCRP23-2019-0007).

# Author contributions

T.D. and J.W. conceived the project. T.D., Y.A., X.H. and J.W. designed the devices. T.D., A.M., X.J., Y.Z. and C.Z. implemented the experiment. T.D. and A.M. provided the simulations and performed the theoretical analysis. T.D., A.M., Y.A., B.Z. and J.W. discussed and improved the theoretical results. T.D. designed and established the experimental

set-up. J.M., Y.Y., Z.L., B.T. and J.L. fabricated the device. Q.G. and J.W. managed the project. T.D., A.M. and J.W. wrote the manuscript. All the authors discussed the results and contributed to the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41563-024-01904-1.

Correspondence and requests for materials should be addressed to Tianxiang Dai, Yan Yang, Xiaoyong Hu or Jianwei Wang.

Peer review information Nature Materials thanks Jose Capmany, Alexander Khanikaev and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.