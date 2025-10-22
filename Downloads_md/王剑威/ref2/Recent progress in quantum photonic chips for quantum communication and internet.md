REVIEW ARTICLE

Open Access

# Recent progress in quantum photonic chips for quantum communication and internet

Wei Luo $^{1}$ , Lin Cao $^{1}$ , Yuzhi Shi $^{2\boxtimes}$ , Lingxiao Wan $^{1}$ , Hui Zhang $^{1}$ , Shuyi Li $^{1}$ , Guanyu Chen $^{1}$ , Yuan Li $^{1}$ , Sijin Li $^{1}$ , Yunxiang Wang $^{3}$ , Shihai Sun $^{4}$ , Muhammad Faeyz Karim $^{1\boxtimes}$ , Hong Cai $^{5\boxtimes}$ , Leong Chuan Kwek $^{1,6,7\boxtimes}$  and Ai Qun Liu $^{1\boxtimes}$

# Abstract

Recent years have witnessed significant progress in quantum communication and quantum internet with the emerging quantum photonic chips, whose characteristics of scalability, stability, and low cost, flourish and open up new possibilities in miniaturized footprints. Here, we provide an overview of the advances in quantum photonic chips for quantum communication, beginning with a summary of the prevalent photonic integrated fabrication platforms and key components for integrated quantum communication systems. We then discuss a range of quantum communication applications, such as quantum key distribution and quantum teleportation. Finally, the review culminates with a perspective on challenges towards high-performance chip-based quantum communication, as well as a glimpse into future opportunities for integrated quantum networks.

# Introduction

Quantum communication, which applies the principles of quantum mechanics for quantum information transmission, enables fundamental improvements to security, computing, sensing, and metrology. This realm encapsulates a vast variety of technologies and applications ranging from state-of-the-art laboratory experiments to commercial reality. The best-known example is quantum key distribution (QKD) $^{1,2}$ . The basic idea of QKD is to use the quantum states of photons to share secret keys between two distant parties. The quantum no-cloning theorem endows the two communicating users with the ability to detect any eavesdropper trying to gain knowledge of the key $^{3,4}$ . Since security is based on the laws of quantum physics rather than computational complexity, QKD is recognized as a desired solution to address the

ever-increasing threat raised by emergent quantum computing hardware and algorithms.

Despite the controversy surrounding its practical security, QKD is leading the way to real-world applications. For example, fiber-based and satellite-to-ground QKD experiments have been demonstrated over  $800\mathrm{km}$  in ultra-low-loss optical fiber and  $2000\mathrm{km}$  in free space, respectively. The maximal secure key rate for a single channel has been pushed to more than  $110\mathrm{Mbit/s}^8$ . A number of field-test QKD networks have been established in Europe, Japan, China, UK, and so forth. Furthermore, the security of practical QKD systems was intensively studied to overcome the current technical limitations. Post-quantum cryptography has been combined with QKD to achieve short-term security of authentication and long-term security of keys.

Beyond QKD, quantum teleportation has attracted extensive attention, which exploits quantum entanglement for transferring fragile quantum information in an effectively unhackable manner[19-21]. Based on this, quantum networks can be conducted to connect various quantum devices, enabling unparalleled capabilities that are provably unattainable using only classical information

Correspondence: Yuzhi Shi (yzshi@tongji.edu.cn) or Muhammad Faeyz Karim (faeyz@ntu.edu.sg) or Hong Cai (caih@ime.a-star.edu.sg) or Leong Chuan Kwek (kwekleongchuan@nus.edu.sg) or Ai Qun Liu (eaqliu@ntu.edu.sg)  
<sup>1</sup>Quantum Science and Engineering Centre (QSec), Nanyang Technological University, Singapore 639798, Singapore  
<sup>2</sup>Institute of Precision Optical Engineering, School of Physics Science and Engineering, Tongji University, 200092 Shanghai, China  
Full list of author information is available at the end of the article

techniques $^{22,23}$ . Quantum secure direct communication (QSDC) $^{24-26}$ , another important branch of quantum communication, has also provided opportunities for secure data transferring. This technique has been evolving quickly in recent years $^{27-33}$ , enabling users to directly transmit confidential information over secure quantum channels without sharing encryption keys. For instance, a QSDC network has been demonstrated with 15 clients $^{32}$ . Combined with post-quantum cryptography, a QSDC network with end-to-end security can be constructed using existing technologies $^{33}$ .

Conventional quantum communication systems are typically built using discrete optical devices. Generally, these devices are separately assembled with optical glasses (e.g., fused quartz and silica) and optical crystals (e.g., calcite, beta barium borate and lithium niobate) and connected via free space or optical fibers. Although it is convenient to optimize individual elements to fit with the strict requirements such as ultra-low loss, high efficiency, fast speed and high fidelity in quantum information applications, interconnects and packaging have always posed significant reliability and cost challenges for traditional discrete optical designs, especially when dealing with large-scale networks linking hundreds of thousands of users. For instance, high mechanical and thermal stabilities are required to mitigate space and phase misalignment over time due to environmental stresses and temperature variations, which are yet difficult to achieve in a complex discrete optical system by global stabilization. Therefore, current bulky systems composed of discrete optical components may struggle to meet the growing demand for higher volume transmission capability, manifesting great merits of chip-scale quantum communication systems[34].

Quantum photonic chips are an ideal platform for new generation of quantum technology[35]. In addition to miniaturization, two advantages over discrete optical systems, i.e., scalability and stability are prominent. Scalability is enabled because the chips, with all their components, are printed as a unit by lithography rather than being constructed one component at a time. Stability is achieved as the circuits built on a robust and compact solid-state platform can minimize deviations due to vibrations or temperature variations. These two advantages are critical for achieving the level of integration and performance required for quantum information processing and highly efficient quantum communication. Moreover, quantum photonic chips have a strong potential for low-cost production. While the initial cost of fabricating the required photomasks is high, the average cost per chip can be greatly reduced through mass production.

After decades of effort, photonic integration has been realized in all aspects of individual quantum communication systems, including photon sources, encoding and

decoding photonic circuits, and detectors $^{34,35}$ . In principle, integrated photonic chips can combine many desirable characteristics, such as efficiency, cost-effectiveness, scalability, flexibility and performance, that are required for quantum communication applications. Such characteristics, along with wafer-scale fabrication processes, make chip-based quantum communication systems a compelling platform for the future of quantum technologies.

In this review, we focus on the latest advances in implementing quantum communication on quantum photonic chips. We begin by discussing state-of-the-art integration platforms used for quantum photonics, summarizing their specific features and criteria that determine their suitability for quantum communication applications. Next, we examine the key elements of a chip-based quantum communication system, namely integrated photon sources, reconfigurable passive and active elements for manipulation of quantum states, and integrated single-photon and homodyne detectors. We then review progress in realizing on-chip systems for practical quantum communication implementations, including QKD and entanglement-based protocols such as entanglement distribution and quantum teleportation. Finally, we conclude by discussing the remaining challenges and prospects in this field.

# Key technologies for quantum photonic chips

Photonic integration opens the path towards miniaturized quantum communication systems with increasing complexity and enhanced functionality. Figure 1 provides an overview of the three aspects of integrated quantum communication: photonic materials platforms for large-scale integration $^{36-38}$ , quantum photonic components such as quantum light sources $^{39}$ , high-speed modulators $^{40}$  and highly efficient photodetectors $^{41}$ , and typical applications in QKD $^{42,43}$  and quantum teleportation $^{44}$ . Since the materials, preparation processes and structural designs employed in photonic integration are considerably different from those used in discrete systems, essential photonic components in chip-level configurations must be redesigned and optimized for specific quantum information applications. The relevant technical studies are summarized in this section, covering quantum light sources, encoding and decoding elements, quantum detectors and packaging techniques for integrated photonic systems.

Figure 2 highlights key milestones in the development of integrated quantum communication. Early attempts in this field can be traced back to the integration of photon sources using periodically poled lithium niobate waveguides $^{45}$  and interferometers using silica-on-silicon planar lightwave circuits (PLCs) $^{46-49}$ . The high efficiency and temperature-stabilized operation of these integrated

![](images/223cb18c01b7fe5cb58506e12abdc8019a05190aaee62ec9abd66618c538d10f.jpg)  
Fig. 1 Overview of quantum photonic chips for quantum communication. The research scope covers photonic materials platforms for large-scale integration $^{36-38}$ , quantum photonic components such as quantum light sources $^{39}$ , high-speed modulators $^{40}$ , and highly efficient photodetectors $^{41}$ , as well as typical applications in QKD $^{42,43}$  and quantum teleportation $^{44}$ . Panels reproduced with permission from: ref.  ${}^{36}$ , Springer Nature Ltd; ref.  ${}^{37}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); ref.  ${}^{38}$ , AIP Publishing LLC; ref.  ${}^{39}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); ref.  ${}^{40}$ , Springer Nature Ltd; ref.  ${}^{41}$ , under a Creative Commons licence (http://creativecommons.org/licenses/by-nc-nd/3.0/); ref.  ${}^{42}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); ref.  ${}^{43}$ , Springer Nature Ltd; ref.  ${}^{44}$ , Springer Nature Ltd

elements demonstrated their inherent suitability over discrete, bulky components. Subsequently, many other materials were explored, and significant progress was made in on-chip generation, manipulation, and detection of quantum states of light for quantum communication and other quantum information applications.

Prevailing materials platforms for chip-based quantum communication implementations include silica waveguides (silica-on-silicon and laser-written silica waveguides), silicon-on-insulator (SOI), silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)$ , lithium niobate (LN), gallium arsenide (GaAs), indium phosphide (InP) and silicon oxynitride  $(\mathrm{SiO}_x\mathrm{N}_y)^{34,35,50}$ . Table 1

summarizes the state of the art of these monolithic platforms, indicating their advantages and disadvantages in terms of waveguiding properties, available active components, and compatibility with related technologies. For example, SOI provides a great refractive-index contrast for high-density integration, strong optical nonlinearity for nonclassical state generation, and excellent compatibility with advanced CMOS (complementary metal-oxide-semiconductor) processes that have been widely employed in the semiconductor industry. However, the lack of lasing capability makes it challenging to fully integrate all the required components of a quantum communication

![](images/2d591356e05e029c5bd5dafa71cae3771fd0baed28fd3a01f9d71f30e0cce2fb.jpg)  
- On-chip quantum interferometer for quantum cryptography

![](images/e2db21e05f1e0e48c56d53ef3adc228fd1abdb73d2f0db409d99d857d763cfa5.jpg)

![](images/50b663a1cd420d0f1bdb62377e92b99c00fd9d1b364920c5df56e123da6ec177.jpg)  
Chip-to-chip quantum teleportation

![](images/805a678c638b7b642b74f162c346df6138d523fac97d30c973290e9bef83ad02.jpg)  
- Chip-based discrete-variable quantum key distribution (DV-QKD)  
- Chip-based measurement-device-independent (MDI) QKD

![](images/1b058bc0a4e784cfdd2517c5989898f8fb1a0baaba980d898f6dc37ea1c0785e.jpg)  
Quantum teleportation on a photonic chip

![](images/1d61080f92458ae17eff150c103f1f55affa518241ab5ad9c8edf57faced1e5a.jpg)  
Fig. 2 Timeline of advances in quantum photonic chips for quantum communication. The key milestones include the first demonstrations of the on-chip quantum interferometer for quantum cryptography $^{46}$ , quantum teleportation on a photonic chip $^{90}$ , chip-based DV-QKD $^{42}$ , CV-QKD $^{43}$  and MDI-QKD $^{81,94,96}$ , and chip-to-chip quantum teleportation $^{44}$ . Panels reproduced with permission from: ref.  ${}^{46}$ , Institution of Electrical Engineers; ref.  ${}^{90}$ , Springer Nature Ltd; ref.  ${}^{42}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); ref.  ${}^{43}$ , Springer Nature Ltd; ref.  ${}^{44}$ , Springer Nature Ltd  
- Chip-based continuous-variable (CV) QKD

system. III-V semiconductor platforms (GaAs, InP, etc.) allow for monolithic system integration, yet coming at the expense of higher cost and lower integration level. The inevitable weaknesses of each material and its fabrication process indicate that no single platform can provide all the desired features for quantum communication applications. A viable solution is a hybrid integration that aims to combine the advantages of different platforms[50]. Such efforts have been made to realize heterogeneous quantum photonic devices like integrated superconducting nanowire single-photon detectors (SNSPDs)[41] and integrated lasers for weak coherent pulse generation[51]. Other important technologies including semiconductor quantum dots (QDs) interfaced with photonic nanostructures[52] and diamond-on-insulator[53,54] have also emerged as competitive platforms for on-chip implementation of quantum communication.

# Quantum light sources

A photon source that generates designated quantum states of light is a key element of a quantum optical system. In general, single-photon states and entangled photon states are required in the architecture of quantum communication networks<sup>16</sup>, which can be obtained either deterministically using single-photon emitters or probabilistically using parametric nonlinear processes.

QDs are considered one of the most promising candidates for the on-demand generation of single photons or

entangled photon pairs by virtue of the deterministic nature of their emission characteristics $^{55}$ . In particular, the small footprint and compatibility with semiconductor technology make them appealing for on-chip integration $^{56}$ . For single-photon generation, purity, extraction efficiency, and photon indistinguishability of  $99.1\%$ ,  $66\%$ ,  $98.5\%$  and  $99.7\%$ ,  $65\%$ ,  $99.6\%$  have been achieved in a single InAs/GaAs self-assembled QD (Fig. 3a) $^{57}$  and an InGaAs QD (Fig. 3b) $^{58}$ , respectively. However, these micropillar-based QD single-photon sources present difficulty in waveguide integration due to their out-of-plane emission feature. Alternatively, QDs can be embedded in photonic crystal waveguides (Fig. 3c) $^{59}$  or heterogeneous waveguide structures $^{60}$  for highly efficient coupling with waveguides. Entangled photon pairs can also be obtained using the biexciton-exciton cascaded radiative processes in QDs $^{61-63}$ . By deterministically embedding GaAs QDs in broadband photonic nanostructures, an entangled photon pair source was demonstrated with a pair collection probability of 0.65, entanglement fidelity of 0.88, and indistinguishability of 0.901 and 0.903 (Fig. 3d) $^{64}$ . In addition to QDs, several other solid-state quantum emitters, such as color centers in diamond $^{53,54}$ , silicon carbide $^{65}$ , carbon nanotubes $^{66}$ , and defects in two-dimensional materials $^{67,68}$ , have also been investigated and shown great potential for on-chip generation of single photons or entangled photon pairs.

Table 1 Specifications of the state of the art of monolithic integrated photonic platforms  

<table><tr><td></td><td>Silica waveguides235</td><td>Silicon-on-insulator37,235</td><td>Silicon nitride236</td><td>Lithium niobate on insulator237</td><td>Gallium arsenide238</td><td>Indium phosphide38</td><td>Silicon oxynitride239,240</td></tr><tr><td>Refractive index contrast</td><td>Low</td><td>High</td><td>Moderate</td><td>Moderate</td><td>Low</td><td>Low</td><td>Low, tunable</td></tr><tr><td>Losses</td><td>Ultralow</td><td>Moderate linear loss, High two-photon absorption</td><td>Low linear loss, low two-photon absorption</td><td>Moderate</td><td>Moderate</td><td>Moderate</td><td>Low linear loss, low two-photon absorption</td></tr><tr><td>Nonlinear index</td><td>Weak χ3</td><td>Strong χ3</td><td>Strong χ3</td><td>Strong χ2</td><td>Strong χ2</td><td>Strong χ2</td><td>Moderate χ3</td></tr><tr><td>Laser</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Yes</td><td>Yes</td><td>N/A</td></tr><tr><td>Modulator</td><td>Low speed</td><td>High speed</td><td>Low speed</td><td>High speed</td><td>High speed</td><td>High speed</td><td>Low speed</td></tr><tr><td>Detector</td><td>N/A</td><td>Ge, High speed</td><td>N/A</td><td>N/A</td><td>High speed</td><td>High speed</td><td>N/A</td></tr><tr><td>Mode matching with optical fibers</td><td>Excellent</td><td>Poor</td><td>Moderate</td><td>Moderate</td><td>Poor</td><td>Poor</td><td>Moderate</td></tr><tr><td>CMOS compatibility</td><td>N/A</td><td>Excellent</td><td>Good</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Good</td></tr></table>

N/A not applicable

Integrated probabilistic quantum light sources typically take advantage of spontaneous four-wave mixing (SFWM) or spontaneous parametric down-conversion (SPDC) in optical waveguides or other photonic structures (e.g., micro-disk and ring resonators, and photonic crystals). Due to the tight confinement of light, these nonlinear parametric processes are greatly enhanced on a chip, enabling efficient generation of high-quality photon states in miniaturized configurations. In SFWM, two pump photons are annihilated to produce a pair of signal and idler photons, where the frequencies of the pump  $(\omega_{\mathrm{p1}},\omega_{\mathrm{p2}})$ , signal  $(\omega_{\mathrm{s}})$  and idler  $(\omega_{\mathrm{i}})$  must obey  $\omega_{\mathrm{p1}} + \omega_{\mathrm{p2}} = \omega_{\mathrm{s}} + \omega_{\mathrm{i}}$  to conserve the energy. Single-photon or entangled photon sources based on this four-photon process have been demonstrated in platforms with third-order nonlinearity, such as  $\mathrm{Si}^{69}$ ,  $\mathrm{SiO}_2$  (Fig. 4a)<sup>70</sup>, and  $\mathrm{Si}_3\mathrm{N}_4$  (Fig. 4b)<sup>71</sup>. In SPDC, one pump photon is split into a pair of signal and idler photons, where the frequencies of the pump  $(\omega_{\mathrm{p}})$ , signal  $(\omega_{\mathrm{s}})$ , and idler  $(\omega_{\mathrm{i}})$  must also satisfy  $\omega_{\mathrm{p}} = \omega_{\mathrm{s}} + \omega_{\mathrm{i}}$ . Photon sources based on this three-photon process have been implemented in platforms with second-order nonlinearity, such as periodically poled LN waveguide circuits (Fig. 4c)<sup>72</sup> and a III-V semiconductor chip<sup>73</sup>. The major issues for these photon sources are that they produce photons non-deterministically and the generation rates are limited by the fundamental trade-off between brightness and multi-photon probability. Multiplexing techniques offer a promising way to solve the problems<sup>39,74-77</sup>. For instance, an integrated spatially multiplexed heralded single-photon source (HSPS) achieved  $62.4\%$  and  $63.1\%$  enhancement to the single photon generation probability for two separately pumped sources and two sources pumped through a common input, respectively<sup>74</sup>. Further improvement in efficiency requires better delay lines with ultra-low loss and miniaturized footprint, and faster switches with faster electronics to synchronize the operations<sup>77</sup>.

In a practical quantum communication system, single-photon sources and entangled photon sources are not always required. According to the decoy-state protocol $^{78-80}$ , weak coherent pulses can be used as a credible alternative to single-photon states for most prepare-and-measure QKD applications. As such, integrated photon sources can be achieved simply by attenuating the coherent pulses produced by on-chip lasers. Such photon sources have already been demonstrated in several chip-based QKD systems $^{42,51,81}$ .

# Reconfigurable quantum photonic components

Manipulation of quantum states of light is essential for the processing of quantum information in quantum communication, which can be readily implemented by using off-the-shelf passive and active components of integrated photonics. In a typical quantum communication system, photons are generally handled in polarization, phase, spatial, spectral, and temporal domains. Thus,

![](images/60d39778618f20e45e8bf60219515cfddd9294b67678d4954d42c34f87cf5816.jpg)  
a  
Fig. 3 On-chip QD photon sources. a An illustration of a single InAs/GaAs self-assembled QD embedded in a  $2.5\text{-}\mu \mathrm{m}$  diameter micropillar cavity $^{57}$ . b Schematic of an InGaAs QD coupled to a micropillar that is connected to a surrounding circular frame by four one-dimensional wires $^{58}$ . c A single QD embedded in a photonic crystal waveguide $^{59}$ . A large portion of emitted single photons is channeled with near-unity probability into the waveguide mode. d An illustration of a circular Bragg resonator on a highly efficient broadband reflector with a single GaAs QD emitting entangled photon pairs $^{64}$ . Panels reproduced with permission from: a ref. $^{57}$ , APS; b ref. $^{58}$ , Springer Nature Ltd; c ref. $^{59}$ , APS; d ref. $^{64}$ , Springer Nature Ltd

![](images/295e65772970fcc686b91a12d223663a0f08620ec362cae7a3d4035ee73a4cbb.jpg)  
b

![](images/06e32d9b6a65213e96a680179d42b9b8a3a51fe9480216dcb6fb6ebc2f1f76d0.jpg)  
C

![](images/d115d5cd17af547762c4a088bc32a772a58a607311610f34b7e146a4ebd2e163.jpg)  
d

![](images/6e5c44de94cc4002ebae869c0317b956ec3ee9dea1f86bd7f3e544890adf0485.jpg)  
a

![](images/1bacaeebc01a9418ead59fa63df204cd94ed3a5e0dda34e968ca077ee2ecd2a6.jpg)  
b  
Fig. 4 Different types of chip-based parametric photon sources. a Array of spontaneous four-wave mixing (SFWM) heralded single-photon sources (HSPSs) $^{70}$ . A series of straight waveguides are fabricated via UV-laser writing in a germanium-doped silica-on-silicon photonic chip, each of which constitutes its own HSPS. b A nanophotonic visible-telecom SFWM photon-pair source using high-quality factor silicon nitride resonators to generate narrow-band photon pairs with unprecedented purity and brightness $^{71}$ . c A spontaneous parametric down-conversion (SPDC) entangled photon source based on a LN photonic chip with a periodically poled section $^{72}$ . Panels reproduced with permission from: a ref. $^{70}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); b ref. $^{71}$ , Springer Nature Ltd; c ref. $^{72}$ , APS

![](images/9fcda8b8ca9f0e817c2fb35646100be458d1e13beaf47429448282fb297c44f9.jpg)  
c

it requires building blocks that can influence these degrees of freedom of the photons, such as polarization splitters/rotators (Fig. 5a) $^{82}$ , phase shifters (Fig. 5b) $^{83}$ , intensity modulators (Fig. 5c) $^{84}$ , directional couplers (Fig. 5d) $^{85}$ , multi-mode interferometers (MMI) (Fig. 5e) $^{86}$ , ring resonators (Fig. 5f) $^{87}$ , and delay lines (Fig. 5g) $^{88}$ . In particular, phase shifters can be realized via the thermo-optic effect for low-speed applications $^{83,89}$  and the Pockels electro-optic effect for high-speed applications $^{40,84}$ . Such devices have been demonstrated in a variety of integrated platforms, e.g., an ultraviolet-written silica-on-silicon photonic chip for quantum teleportation with thermo-optic phase shifters $^{90}$ , a GaAs quantum photonic circuit with tunable Mach-Zehnder interferometer (MZI) relying on the Pockels effect $^{91}$ , a reprogrammable linear optical circuit comprising an array of 30 silica-on-silicon waveguide directional couplers with 30 thermo-optic phase shifters (Fig. 5h) $^{92}$ , and a large-scale silicon photonics

quantum circuit integrating 16 SFWM photon-pair sources, 93 thermo-optical phase shifters and 122 MMI beam splitters $^{93}$ . On-chip modulators based on free-carrier dispersion effect $^{43,94}$  or quantum-confined Stark effect $^{81}$  can also be utilized for pulse generation and qubit encoding with frequencies up to GHz. For polarization-encoding protocols, modulators based on polarization rotators and polarization beam splitters have been designed and demonstrated for the generation of BB84 polarization states $^{94-96}$ .

Besides aforementioned elements, additional integrated components are required for optical connection between quantum photonic chips and optical fibers. One-dimensional grating couplers and off-plane coupling can be used when there is only one input or output polarization<sup>97</sup>. Otherwise, edge couplers like inverted tapers for butt coupling can be adopted instead in the case of more polarizations and wider spectral range<sup>98</sup>. Moreover, two-

![](images/eeac266c6fb5257bed27fff66c3d7ce284328dc287507009d09858d03d8cff21.jpg)  
a

![](images/5f31ad167b8030d39fc4088111ac9ecf6bf30448b737b2a71546a04f55c4fb26.jpg)  
b

![](images/8122d91a553da40471c3b82a259000287153e001b225058783c8e52d7ba61b06.jpg)  
C

![](images/e98a3fac5edea1d7a0180360492b08106147fb501c8ff793a14d64fa9b19a57a.jpg)  
d

![](images/8aab4cfcc15b26cb25e19d4f6168853b84e46a090a5c20066d7902881d94817c.jpg)  
e

![](images/51d47e180dd90e278daa80605a093459ca8667c9bac0d34f7b36d102c6a6bc36.jpg)  
f

![](images/c3eeadc014cbebd19262a4644b4394743565d44dbd24eb3f8f187bcfc80b85b1.jpg)  
g

![](images/83f705fa3d66d2e95e8ab016218de52edc14bd1d51f8596b63b8612362b790a2.jpg)  
h  
Fig. 5 Typical integrated components on quantum photonic chips. a Schematics of a polarization splitter/rotator and the evolution of its mode profile $^{82}$ . b Optical micrograph and perspective view of a thermo-optic phase shifter in silicon $^{83}$ . c Schematic of a high-bandwidth electro-optic modulator, where an unpatterned LN thin film is bonded to a Mach-Zehnder interferometer fabricated in Si $^{84}$ . d Schematic of a directional coupler with a thin layer of  $\mathrm{Ge}_2\mathrm{Sb}_2\mathrm{Te}_5$  (GST) $^{85}$ . e Schematic of a  $4\times 4$  multi-mode interferometer $^{86}$ . f Schematic of a hybrid quantum photonic circuit integrated with an on-chip tunable ring resonator filter $^{87}$ . g Schematic of a silicon photonic waveguide spiral delay line $^{88}$ . (h) A six-mode universal linear-optic device that was realized in a fully re-programmable silica chip $^{92}$ . Panels reproduced with permission from: a ref.  ${}^{82}$ , The Optical Society; b ref.  ${}^{83}$ , The Optical Society; c ref.  ${}^{84}$ , The Optical Society; d ref.  ${}^{85}$ , American Chemical Society; e ref.  ${}^{86}$ , under a Creative Commons licence (http://creativecommons.org/licenses/by-nc-nd/3.0/); f ref.  ${}^{87}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); g ref.  ${}^{88}$ , Chinese Laser Press; h ref.  ${}^{92}$ , AAAS

dimensional grating coupler supporting multipolarization operation has been demonstrated to convert path-encoded qubits to polarization-encoded qubits that are more adapted for propagation in optical fibers $^{99,100}$ .

# Single-photon detectors (SPDs) and homodyne detectors

Efficient single-photon detection is of great importance to quantum communication applications. In particular, fully integrated SPDs are highly desirable because interfacing with off-chip detectors will lead to unavoidable coupling losses. Recently, an integrated waveguide-coupled Ge-on-Si lateral avalanche photodiode has been demonstrated for single-photon detection with efficiency of  $5.27\%$  at  $1310\mathrm{nm}$  and a dark count rate of  $534\mathrm{kHz}$  at  $80\mathrm{K}$  (Fig. 6a) $^{101}$ . However, such single-photon avalanche photodiodes are often plagued with too many dark counts at high efficiencies. As an alternative, SNSPDs offer significantly lower dark noise with higher detection efficiency, reduced timing jitter, as well as photon-number resolving (PNR) capability. Waveguide-integrated SNSPDs have been reported in platforms of GaAs $^{102}$ , Si $^{41}$ ,  $\mathrm{Si}_3\mathrm{N}_4$ ^{103,104}, LN $^{105}$ , etc., among

which the traveling wave SNSPDs embedded on Si waveguides have achieved detection efficiency up to  $91\%$  and a dark count rate down to  $50\mathrm{Hz}$  (Fig. 6b) $^{41}$ , and on-chip compatibility of reconfigurable components with SNSPDs was demonstrated at cryogenic temperatures $^{104,105}$ . Waveguide PNR detectors are possible by patterning multiple wires in series (Fig. 6c) $^{106}$ . In addition to direct deposition, large-scale integration of SNSPDs fabricated on silicon nitride membrane with silicon and aluminum nitride waveguides was enabled by using the pick-and-place technique (Fig. 6d) $^{107}$ . Moreover, transition-edge sensor (TES) detectors were implemented in a waveguide configuration for the PNR detection with a resolution of up to five photons $^{108,109}$ .

The balanced homodyne detector (or balanced zero-beat detector), which has been widely exploited in continuous-variable (CV) quantum information applications, is another crucial detection element for quantum measurement. Recent developments have significantly improved the performance of integrated homodyne detectors, enabling enhanced levels of compact size, good

![](images/b457add9f1780564da69f73f3e0de13ddadf1509b8c10e107e01f552329203eb.jpg)  
a

![](images/a1cb388fe6da51d864ed1c7a1437942f19e5b0302b9ed5efa4b2fc1d707f05df.jpg)  
b

![](images/096d4b19941289bff61bf78081930cc9aeab4929f5ab328c37afe4a5093b8b29.jpg)  
C

![](images/c17f0dba52cea2ffb4ed32259c22ec453199776f1e9f7a47af40800886367a94.jpg)  
d  
Fig. 6 Overview of on-chip single-photon detector (SPD) and homodyne detector. a Angled scanning electron microscope image of a waveguide-coupled Ge-on-Si lateral single-photon avalanche photodiode with oxide cladding removed $^{101}$ . b A NbN nanowire traveling wave SNSPD atop a silicon waveguide with detection efficiency up to  $91\%^{41}$ . c A waveguide photon-number resolving (PNR) SNSPD consisting of four wires in series with a resistance  $(R_{\mathrm{p}})$  in parallel to each wire $^{106}$ . d Membrane transfer of a hairpin-shaped NbN SNSPD onto a photonic waveguide for on-chip detection of non-classical light $^{107}$ . e A silicon-based homodyne detector with a thermo-optical phase shifter, two Mach-Zehnder modulators and two photodiodes, interfaced to a customized transimpedance amplifier by wire bonding $^{114}$ . Panels reproduced with permission from: a ref.  ${}^{101}$ , The Optical Society; b ref.  ${}^{41}$ , under a Creative Commons licence (http://creativecommons.org/licenses/by-nc-nd/3.0/); c ref.  ${}^{106}$ , AIP Publishing LLC; d ref.  ${}^{107}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); e ref.  ${}^{114}$ , The Optical Society

![](images/449040f5aafb105091b3a039b6eb50fc1752fa24414f81bbb542de4389a4072f.jpg)  
e

stability, broad bandwidth, low noise, and a high degree of common-mode rejection. As an illustration, a homodyne detector with 150-MHz bandwidth and 11-dB clearance was monolithically integrated onto a silicon photonics chip $^{110}$ . However, discrete amplification electronics greatly increase the device footprint. To reduce the size and total capacitance, wire bonding was utilized to integrate the germanium-on-silicon homodyne detector chip with the amplifier chip $^{111}$ , which resulted in a 3-dB bandwidth of  $1.7\mathrm{GHz}$  and a shot-noise limited bandwidth of up to  $9\mathrm{GHz}$ . A similar approach has also been applied to construct chip-level InGaAs homodyne detectors comprising low-parasitic photodiodes and low-noise high-speed transimpedance amplifiers $^{112,113}$ . Although it is convenient to adopt commercial telecom transimpedance amplifiers, they will typically bring suboptimal electrical noise. Co-design and integration of a homodyne detector with a customized transimpedance amplifier can efficiently reduce the noise and significantly boost the performance, allowing for a 20-GHz shot-noise-limited bandwidth and a quantum shot noise clearance of up to 28 dB (Fig. 6e) $^{114}$ .

# Chip packaging and system integration

While bare quantum photonic chips can be characterized using a probe station, they must be packaged into durable modules to develop working prototype devices<sup>115</sup>. To this end, numerous processes have been proposed to package quantum photonic chips into compact systems for real-world applications.

Generally, photonic packaging involves a range of techniques and technical competencies needed to make the optical, electrical, mechanical, and thermal connections between a photonic chip and the off-chip components in a photonic module[116-118]. Fiber-to-chip coupling is one of the best-known aspects. The main challenge associated with coupling between an optical fiber and a typical waveguide on the chip is the large difference between their mode-field diameters (MFDs)[119]. For example, the MFD at  $1550\mathrm{nm}$  is  $\sim 10\mu \mathrm{m}$  in telecom single-mode fiber (SMF), while the cross-section of the corresponding strip silicon waveguide is usually only  $220\times 450\mathrm{nm}$ . This mismatch can be mitigated by using configurations that efficiently extract the mode from waveguide[97], such as inverted-taper edge couplers

![](images/84b2425df3ed41e5667a78386a23e736a9d9fd0d49d71dd57bc98b8f7e9a6cc3.jpg)  
a

![](images/5b8e1b7ca5042e3d57d591f1efdf3b5f4aa0e5afea761d5e07d84944ba94c35e.jpg)  
b

![](images/f619efaeb7d6730843bf0b1e06c4823f27440b14f5d5884ab2fb70ab6732908a.jpg)  
C

![](images/1aab27a7f4b7b5e46dfe9c59d66a7bf5e3b0f60d41ec2dd45a699a83c4c4deb0.jpg)  
Fig. 7 Instances of chip packaging and integration. a Schematic of a bilayer LN inverse taper coupled with a lensed optical fiber $^{121}$ . b Schematic of a  $\mathrm{Si}_3\mathrm{N}_4$  on-SOI dual-level grating coupler interfaced with a single-mode fiber $^{123}$ . c Photograph of a quantum photonic processor packaged with PCBs, fiber arrays and thermoelectric cooler $^{127}$ . d Photograph of an assembled multi-chip module that provides connectivity between one photonic integrated circuit (IC) and four electronic ICs via silicon interposer $^{128}$ . Panels reproduced with permission from: a ref.  ${}^{121}$ , The Optical Society; b ref.  ${}^{123}$ , The Optical Society; c ref.  ${}^{127}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); d ref.  ${}^{128}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/)  
d

interfaced with lensed SMF fibers (Fig. 7a) $^{120,121}$  or ultra-high numerical aperture fibers $^{122}$ , and grating couplers interfaced with SMF fibers (Fig. 7b) $^{119,123}$ . For the approach harnessing grating couplers, coupling efficiency up to  $81.3\%$ $(-0.9\mathrm{dB})$  can be achieved in a 260-nm-thick SOI platform without the need for a back reflector or overlayer $^{124}$ . Additionally, efficiencies over  $90\%$  have been experimentally demonstrated using edge couplers fabricated on 200-mm SOI wafers $^{125}$ . An alternative approach for cost-effective and panel-level packaging is the evanescent coupling scheme, which has been reported to have a coupling loss of approximately 1 dB at a wavelength of  $1550\mathrm{nm}^{126}$ .

To access the electrical components on quantum photonic chips, electronic packaging is required to route signals from electronic drivers, amplifiers, and other control circuitry. This is often achieved by interfacing with dedicated printed circuit boards (PCBs) (Fig. 7c) $^{127}$ . The connection between PCBs and the bond-pads on the chip is usually made using wire-bonds. When a very large number of electrical connections or precise sub-nanosecond control on multiple channels is needed, 2.5-dimensional or 3-dimensional integration with customized electronic integrated circuits (EICs) may be utilized (Fig. 7d) $^{115,128}$ . This integration can be achieved using either solder-ball-

bump or copper-pillar-bump interconnects, providing a robust electrical, mechanical, and thermal interface for the photonic chips $^{129,130}$ .

Global thermal stabilization of quantum photonic devices is essential for prototypes that require high accuracy and repeatability or for field tests where seasonal temperature swings are common. This can be achieved using passive cooling techniques or a thermoelectric cooler (TEC). The added global stability from the TEC allows for more efficient and better reproducibility in the local temperature tuning of individual photonic elements (e.g., micro-ring resonators, thermo-optic phase shifters, etc.) on the chip $^{115}$ . Additionally, liquid cooling can be installed to further increase the cooling capacity of the system $^{127}$ .

# Quantum secure communication systems

As the most developed quantum secure communication technology, QKD based on bulk or fiber optic components has already been used in banks and governments to provide high-level security for data transmission. Nevertheless, wider applications require QKD systems that are more robust, compact, and can be mass manufactured at a lower cost. In the previous section, we have summarized a variety of studies targeting integrated devices for the realization of miniaturized and cost-effective quantum

Table 2 Degree of integration for typical integrated QKD implementations  

<table><tr><td>Reference</td><td>Platform</td><td>Protocol</td><td>QRNG</td><td>Source</td><td>Encoding</td><td>Decoding</td><td>Detector</td></tr><tr><td rowspan="3">Sibson, P. et al. (2017)42</td><td rowspan="3">InP, SiOxNy</td><td>BB84</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>COW</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DPS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Paraiso, T. K. et al. (2019)153</td><td rowspan="2">InP</td><td>DPS</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>BB84</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">Paraiso, T. K. et al. (2021)154</td><td rowspan="2">InP, Si</td><td>Modified</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>BB84</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ma, C. et al. (2016)95</td><td>Si</td><td>BB84</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td rowspan="2">Sibson, P. et al. (2017)155</td><td rowspan="2">Si, SiOxNy</td><td>COW</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>BB84</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Bunandar, D. et al. (2018)157</td><td>Si</td><td>BB84</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Avesani, M. et al. (2021)158</td><td>Si</td><td>BB84</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Geng, W. et al. (2019)159</td><td>Si</td><td>BB84</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td rowspan="2">Dai, J. et al. (2020)160</td><td rowspan="2">Si</td><td>COW</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>DPS</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ding, Y. et al. (2017)162</td><td>Si</td><td>HD-QKD</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Semenenko, H. et al. (2020)81</td><td>InP</td><td>MDI-QKD</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Wei, K. et al. (2020)94</td><td>Si</td><td>MDI-QKD</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Cao, L. et al. (2020)96</td><td>Si</td><td>MDI-QKD</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Zheng, X. et al. (2021)165</td><td>Si, NbN</td><td>MDI-QKD</td><td>No</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Zhang, G. et al. (2019)43</td><td>Si</td><td>CV-QKD</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

COW coherent one way, DPS differential phase shift, HD-QKD high-dimensional QKD

communication. In this section, recent efforts towards fully chip-based QKD platform are described from a system-level view. As an overview, the degree of integration for typical integrated QKD implementations is listed in Table 2. Further comprehensive reviews of the QKD protocols can be found in the refs. $^{16,17,131,132}$ .

# Quantum random number generators (QRNGs)

The security of encryption is determined by the quality or unpredictability of keys, implying that a truly random number generator is an essential part of a quantum secure communication system. Although pseudo-random numbers are simple to create, their inherent deterministic behavior prevents them from being regarded as truly unpredictable. QRNGs have thus been developed to produce truly random numbers with characteristics of unpredictability, irreproducibility, and unbiasedness, which are guaranteed by the basic principle of quantum physics<sup>133</sup>.

The most commonly used protocols for QRNGs include the quantum phase fluctuation scheme $^{134-138}$  and vacuum state scheme $^{139-144}$ . These schemes can easily achieve random bit rates up to Gbps by employing photodetectors instead of single-photon detectors. In addition to real

time output speed, the module size is also a key parameter of QRNG for practical applications. The emerging technology of integrated quantum photonics has exhibited considerable benefits in terms of size reduction. Recently, numerous integrated QRNG implementations have been demonstrated, leveraging various integration technologies with different levels of complexity. Utilizing multiplexed detectors, a QRNG based on  $\mathrm{LiNbO_3}$  platform $^{144}$  has reached a real-time rate of 3.08 Gbps, while a quantum entropy source has been constructed in an InP platform $^{145}$ . Since SOI platform has a higher integration density and superior technical maturity compared with III-V systems, QRNG implementations have also been reported on SOI platform by measuring phase fluctuations (Fig. 8a) $^{146}$  and vacuum state $^{110}$ , respectively. However, it is worth noting that germanium photodiodes on SOI experience a significant dark current, which degrades the performance of on-chip QRNGs and needs careful optimization for mitigation. Alternatively, an integrated QRNG based on InGaAs photodiodes was constructed with a real-time output rate of 18.8 Gbps by virtue of a high bandwidth trans-impedance amplifier hybrid packaged with an SOI chip (Fig. 8b) $^{112}$ . Another

![](images/298f081ecb306a868d7697d195728ec03f3d6273f3b04bbbfb518c08cc756f60.jpg)  
a

![](images/20b6a650446cd400512d9464df819e29ad004c14e1718b28a1f7cf9f2e4ed700.jpg)  
Fig. 8 Integrated quantum random number generators (QRNGs). a A QRNG by measuring phase fluctuations from a laser diode with an SOI chip $^{146}$ . b A hybrid integrated QRNG with InGaAs photodiodes packaged on a SOI chip $^{112}$ . Panels reproduced with permission from: a ref.  ${}^{146}$ , Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); b ref.  ${}^{112}$ , AIP Publishing LLC  
b

integrated QRNG has been demonstrated based on a parallel array of independent single-photon avalanche diodes, homogeneously illuminated by a direct-current-biased light-emitting diode and co-integrated with logic circuits for postprocessing $^{147}$ . The real-time bit rate of the CMOS-based QRNG could reach up to 400 Mbps. Recently, through custom co-design of opto-electronic integrated circuits and side-information reduction by digital filtering, a record generation rate of 100 Gbps has been reported using an SOI photonic chip co-packaged with a GaAs transimpedance amplifier circuit $^{148}$ .

# DV-QKD systems

In typical QKD implementations, secret keys are encoded in discrete variables (DVs), such as the polarization or phase of photons. A prominent example of such DV-QKD protocols is decoy-state  $\mathrm{BB84}^{78-80}$ , which has been widely adopted in state-of-the-art commercial applications. According to the protocols, light sources, modulators, single-photon detectors, and essential passive optical components constitute the main framework of a DV-QKD system. Photonic integration of these elements began with the asymmetric PLC MZIs for differential-phase-shift QKD experiments[46-49]. The on-chip interferometers showed much more precise and stable operation for phase decoding compared to their fiber-based counterpart. Afterward, a series of compact QKD devices were demonstrated. For example, a miniaturized QKD transmitter was fabricated with a similar size to an electro-optic modulator, which incorporated a distributed feedback laser and a modulator[149]. The small-scale transmitter can produce 1550-nm weak-coherent pulses encoded in BB84 polarization states with decoy states. Then, a client consisting of an on-chip  $\mathrm{LiNbO}_3$  polarization rotator was realized for client-server reference-frame-independent QKD[150]. The client integrated into a handheld device received dim laser pulses from a QKD server, and then attenuated and encoded each pulse with a

qubit of information for return transmission to the server. In addition, the design and evaluation of a handheld QKD transmitter module were put forward based on an integrated optics architecture with an effective size of  $25\mathrm{mm}\times 2\mathrm{mm}\times 1\mathrm{mm}^{151}$ . In the module, four vertical-cavity surface-emitting lasers coupled to four micropolarizers fabricated by focused ion beam milling were used to generate polarization qubits. The qubits were combined with a waveguide array fabricated in borosilicate glass for ensuring spatial overlap.

The devices previously discussed show the viability and feasibility of partially integrated QKD systems. Nevertheless, fully chip-based systems are essential for enhanced performance, miniaturization, and increased functionality necessary in practical deployments. A QKD system was demonstrated with a high degree of integration (Fig. 9a) $^{42}$ . The transmitter module on an InP chip and the receiver module on a  $\mathrm{SiO}_x\mathrm{N}_y$  chip was integrated by using components and manufacturing processes from the telecommunication industry. The InP transmitter monolithically incorporated a tunable laser, optical interferometers, electro-optic phase modulators and a p-i-n photodiode, while the  $\mathrm{SiO}_x\mathrm{N}_y$  receiver consisted of thermooptic phase shifters and a reconfigurable delay line that interfaced with off-chip single photon detectors. The reconfigurability of the devices enabled the implementation of multiple protocols, including BB84, coherent one-way, and differential phase shift, with clock rates up to  $1.7\mathrm{GHz}$ , a quantum bit error rate (QBER) as low as  $0.88\%$ , and estimated secret key rates up to 568 kbps for an emulated  $20\mathrm{km}$  fiber link. Recently, the data rate of the chip-based system has been increased through wavelength division multiplexing (WDM) $^{152}$ . Such WDM-QKD system was implemented using two InP transmitters and a single  $\mathrm{SiO}_x\mathrm{N}_y$  receiver with on-chip asymmetric MZI filters for wavelength demultiplexing. The combined WDM channels doubled the secret key rate to  $1.11\mathrm{Mbit/s}$  over a  $20\mathrm{km}$  emulated fiber. The aforementioned implementations of

![](images/ab469bc2f9ed660e4b893c71e6dcfcabf72252a6831a97fa686d02e8ef3a5c79.jpg)  
Fig. 9 Chip-based QKD systems with hybrid materials platform. a A chip-to-chip system with a  $2 \times 6 \mathrm{~mm}^2$  integrated indium phosphide (InP) transmitter and a  $2 \times 32 \mathrm{~mm}^2$  silicon oxynitride ( $\mathrm{SiO}_x\mathrm{N}_y$ ) photonic receiver circuit for GHz clock rate, reconfigurable, multi-protocol QKD[42]. b A modulator-free QKD transmitter chip consisting of two cascaded high-bandwidth distributed feedback lasers and one variable optical attenuator[153]. Panels reproduced with permission from: a ref.[42], under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); b ref.[153], under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/)

![](images/f7cf836f0d4149898a66fb6460fb1d8b15ae88b6ec68022a2c06543045382992.jpg)

![](images/1f6a7c786cb772b0740ef3516f891fbada62894d13fa33d63fb3ff1bc132c1e7.jpg)  
a

![](images/3d059e8153a28dc8c0f098187e1c6e7598df4699f3ac72ee8b2b85ee91fd8eeb.jpg)  
b  
Fig. 10 Silicon photonic chips for multiple QKD protocols. a A Si transmitter for polarization-encoded QKD, consisting of a microring pulse generator, a microring intensity modulator, four variable optical attenuators, and a polarization controller $^{95}$ . b Integrated silicon photonic transmitters to perform multiple QKD protocols, including coherent-one-way, polarization encoded BB84 and time-bin encoded BB84 $^{155}$ . c Field test of intercity QKD over a 43-km dark fiber link using a silicon photonic polarization encoder $^{157}$ . Panels reproduced with permission from: a ref.  ${}^{95}$ , The Optical Society; b ref.  ${}^{155}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); c ref.  ${}^{157}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/)

![](images/64ddfed5b23f60d244a94657e0f0da7223bd3abf9fe889d3ce358803f3b43fa6.jpg)  
C

chip-based QKD systems relied on integrated modulators. In fact, a modulator-free QKD transmitter chip can be realized based on the direct phase modulation approach recently introduced in bulk optics transmitters. Using the modulator-free chip, secure key rates of 270 and 400 kbps at  $20\mathrm{dB}$  attenuation were achieved for the decoy state BB84 and distributed phase shift protocols, respectively (Fig. 9b) $^{153}$ . Recently, an entirely standalone QKD system has been developed based on InP photonic integrated circuits assembled into compact modules $^{154}$ . This system integrates the quantum transmitter, receiver, and QRNG chips, enabling quantum random number generation and key distribution at gigahertz clock rates.

Silicon photonics is another attractive platform suitable for fully chip-based QKD systems. Although integrating light sources and SPDs remains challenging, several proof-of-principle demonstrations of Si-based QKD

devices have been reported in recent years. One early work showcased a Si optical transmitter for polarization-encoded QKD (Fig. 10a) $^{95}$ . The chip incorporated a pulse generator, intensity modulator, variable optical attenuator, and polarization modulator in a  $1.3\mathrm{mm} \times 3\mathrm{mm}$  die area and executed the BB84 protocol with a QBER of  $5.4\%$  and an asymptotic secure key rate of  $0.95\mathrm{kbps}$  over a  $5\mathrm{-km}$  fiber link. Meanwhile, three implementations of high-speed low-error QKD with silicon photonic devices were demonstrated (Fig. 10b) $^{155}$ . Employing a combination of thermo-optic phase modulators alongside high-bandwidth carrier-depletion modulators, they attained estimated asymptotic secret key rates of up to  $916\mathrm{kbps}$  and QBERs as low as  $1.01\%$  over  $20\mathrm{km}$  of fiber. Furthermore, a silicon photonic transceiver circuit was constructed, capable of generating the four BB84 states with  $>30\mathrm{dB}$  polarization extinction ratios and gigabit-per

![](images/d0353eac8ac38bf4ebb4c8befae7223a7c1005d054c4a841af87ee4db317bb61.jpg)  
a

![](images/ffc918025ca01884f2e6a1e20ce12e110a6e14b7efb596b951172cef1f1bd21c.jpg)  
b

![](images/cb196b3e7239a04597ed314ac354c3514f3ebf3c2c904a71615d446025c7cb02.jpg)  
c  
Fig. 11 Different chip-based quantum communication systems for advanced QKD protocols. a Silicon-photonic-integrated circuit for noise-tolerant high-dimensional  $\mathsf{QKD}^{162}$ . b InP transmitter chips used to generate the time-bin encoded BB84 weak coherent states for MDI-QKD $^{81}$ . c A packaged silicon photonic MDI-QKD transmitter chip soldered to a compact control board $^{94}$ . d A silicon photonic chip-based MDI-QKD system comprising two transmitter chips and one server chip interfaced with off-chip SPDs $^{96}$ . Panels reproduced with permission from: a ref.  ${ }^{162}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); b ref.  ${ }^{81}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); c ref.  ${ }^{94}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); d ref.  ${ }^{96}$ , APS

![](images/e9dcac6e5037e221b493a64bdb3ecf972db673b3a4029c26491c1bb7e7f5d31d.jpg)  
d

second modulation speed $^{156}$ . On this basis, polarization-encoded QKD field tests were demonstrated using a similar silicon photonic encoder (Fig. 10c) $^{157}$ . The systems achieved composable secret key rates of 1.039 Mbps in a local test (on a 103.6-m fiber with a total emulated loss of 9.2 dB) and 157 kbps in an intercity metropolitan test (on a 43-km fiber with 16.4 dB loss). In addition, other demonstrations using silicon photonics have also been reported, including an integrated state encoder for free-space daylight  $\mathrm{QKD}^{158}$ , a silicon photonic QKD transceiver based on time-bin protocol $^{159}$ , a silicon photonic transmitter for high-speed distributed-phase-reference  $\mathrm{QKD}^{160}$  and an integrated QKD receiver for multiple users $^{161}$ .

Recently, implementations of advanced QKD protocols with chip-based systems have garnered more interest, as these protocols would greatly benefit from photonic integration. A noise-tolerant high-dimensional QKD protocol based on space division multiplexing in multicore fiber was demonstrated using silicon photonic integrated circuits (Fig. 11a) $^{162}$ . These circuits provided a much more efficient way to create high-dimensional quantum states, enabling low and stable QBER well below both the coherent attack and individual attack limits. Moreover, measurement-device-independent (MDI) QKD, which eliminates all side channel loopholes in detection, is well-suited for a chip-based client-server scenario, where clients hold low-cost photonic chips, and

the server, acting as an untrusted node, incorporates the most expensive elements that can be shared among multiple users. The feasibility of using integrated photonics for MDI-QKD was demonstrated in two independent studies with the InP platform $^{163}$  and the Si/III-V hybrid platform $^{51}$ , respectively. In these studies, Hong-Ou-Mandel interference, the key component of MDI-QKD, was performed between weak coherent states from the chips. High visibilities of  $46.5 \pm 0.8\%$  and  $46 \pm 2\%$  were observed with two InP transmitters $^{163}$  and two III-V on silicon waveguide integrated lasers $^{51}$ , respectively. Subsequently, five research groups implemented chip-based MDI-QKD systems: a star-topology quantum access network with an integrated server was built for MDI-QKD $^{164}$ ; secure key exchange up to  $200\mathrm{km}$  was presented using monolithically integrated InP transmitters (Fig. 11b) $^{81}$ ; a 1.25-GHz MDI-QKD system was reported with two silicon photonic transmitters (Fig. 11c) $^{94}$ ; an all-chip-based MDI-QKD system including two client chips and one server chip was demonstrated using silicon photonics (Fig. 11d) $^{96}$ ; and a fully integrated relay server for MDI-QKD was realized based on a heterogeneous superconducting-silicon-photonic chip $^{165}$ .

# CV-QKD systems

In addition to DV-QKD, several QKD protocols $^{166-168}$  have been proposed to encode key information into continuous variables, such as the values of the quadrature components of the quantized electromagnetic field. A major technical difference is that CV-QKD implementation requires only homodyne detectors, rather than the dedicated SPDs used in DV-QKD. This feature eliminates the need for an additional cryogenic system and dramatically simplifies the detection setup. Consequently, CV-QKD is naturally suitable for photonic integration and compatible with chip-based coherent detection schemes that have been used in classical high-bandwidth communication systems. Indeed, a silicon photonic transceiver design was proposed comprising all major CV-QKD components as well as complete subsystems $^{169}$ ; the feasibility of a homodyne detector integrated onto a photonic chip was demonstrated for measuring quantum states and generating random numbers $^{110}$ . Recently, a stable and miniaturized system was implemented for CV-QKD, compatible with existing fiber communication infrastructure by integrating all optical components (except the laser source) on a silicon photonic chip (Fig. 12a) $^{43}$ . The proof-of-principle characterization demonstrated that the system was capable of producing a secret key rate of  $0.14\mathrm{kbps}$  (under collective attack) over a simulated distance of  $100\mathrm{km}$  in fiber. The performance of chip-based CV-QKD systems can be improved by further optimizing the detection module. As a possible illustration, a high-speed homodyne detector was realized by

interfacing CMOS-compatible silicon and germanium-on-silicon nanophotonics with silicon-germanium integrated amplification electronics (Fig. 12b) $^{111}$ . The detector has a 3-dB bandwidth of  $1.7\mathrm{GHz}$ , a shot-noise limited to  $9\mathrm{GHz}$ , and requires only a miniaturized footprint of  $0.84\mathrm{mm}^2$ .

# Entanglement distribution and quantum teleportation systems

Quantum teleportation has been demonstrated with many platforms ranging from superconducting qubits, trapped atoms, nitrogen-vacancy centers, to continuous variable states and so forth $^{170}$ . Among these implementations, photonic qubit is one of the most promising candidates to build the quantum channel in a quantum network since it is robust in a noisy environment and easy to manipulate at room temperature $^{23}$ . Moreover, it can tolerate longer propagation distances with minimal disturbance from the surroundings. So far, photonic quantum teleportation has been implemented experimentally in many ways including free space and fiber systems $^{170}$ .

When quantum teleportation was first experimentally verified, qubits were encoded in the polarization of photons generated from a BBO crystal in a free-space system on an optical table[20]. Later, the record for free-space teleportation was pushed up to over  $1400\mathrm{km}$  between the Micius satellite and a ground station[171]. This achievement paved the way for an interconnected quantum network globally. However, considering the challenges of beam divergence, pointing, and collection for free-space teleportation, optical fiber systems are more promising for cost-effective metropolitan quantum networks. Currently, the longest fiber-based teleportation distance achieved is  $102\mathrm{km}^{172}$ .

One of the main challenges in photonic qubit teleportation is that the theoretical efficiency of Bell state measurement is limited to only  $50\%$  when using linear optics. To overcome this limitation, the continuous variable optical mode can be adopted as an alternative for realizing fully deterministic state teleportation. This approach has already been demonstrated over a 6-km fiber channel[173]. However, its fidelity still needs to be improved, as this scheme is sensitive to channel loss. For other types of material qubits, a record distance of  $21\mathrm{m}$  has been achieved using trapped atom systems[174].

As quantum teleportation continues to make strides toward real-world applications, the importance of integration as a key technology has become increasingly evident. In a future quantum network, it will be possible to embed a teleportation chip into stationary hardware (e.g., relays in the station) or mobile hardware (e.g., drones $^{175}$ ) to transform these devices into lightweight and compact quantum nodes. This would enable remote access to quantum equipment for sharing quantum information or unlocking

![](images/c8b56b05dd6cb40a1017b5654a4c884e8da60aba3b8751cefcda697dd349ed7d.jpg)

![](images/4154d093e4ec12008f4f9276ff57c880f5da4769d88fbc417b793803bf02b1fc.jpg)  
Fig. 12 Integrated circuits for continuous variable (CV) QKD and high-speed homodyne detection. a An integrated silicon photonic chip platform for CV-QKD, consisting of a transmitter for signal modulation and multiplexing and a receiver for signal demultiplexing and homodyne detection $^{43}$ . b A silicon photonic homodyne detector interfaced with integrated electronics for 9-GHz measurement of squeezed light $^{111}$ . Panels reproduced with permission from: a ref. $^{43}$ , Springer Nature Ltd; b ref. $^{111}$ , Springer Nature Ltd

greater computational power. Such advancements have been made possible owing to the ability to generate and manipulate entangled photon pairs in different degrees of freedom on chip $^{176}$ , such as the path-encoded entangled states in MZIs $^{93}$ , polarization-encoded entangled states by engineering birefringent structures $^{177}$ , and time-bin entangled states in Franson interferometers $^{178}$ .

The first on-chip teleportation (Fig. 13a) was reported with off-chip photon source and achieved a fidelity of 0.89, although it was performed within a single chip $^{90}$ . Recent technological progress in integrated quantum photonics has enabled the implementation of entanglement-based quantum communication protocols beyond a single chip. The first chip-to-chip entanglement distribution was demonstrated with all key components monolithically integrated on silicon photonic chips (Fig. 13b) $^{100}$ . On-chip entangled Bell states were generated, and one qubit was distributed to another silicon chip by converting on-chip path-encoded states and in-fiber polarization states via the two-dimensional grating couplers. Furthermore, more integrated quantum circuits

with on-chip sources have realized inter-chip teleportation with a fidelity of 0.88 (Fig. 13c) $^{44}$ . This chip-scale demonstration of photonic qubit production, processing, and transmission shows a promising way for the distributed quantum information processing internet. Moreover, entangled photon pairs across the visible-telecom range were demonstrated on a  $\mathrm{Si}_3\mathrm{N}_4$  chip with a delicately engineered micro-ring resonator and further distributed over  $20\mathrm{km}^{71}$ . High photon number purity and brightness were achieved with low pump consumption of hundreds of microwatts. Importantly, it provides an entangling link between visible-band photons that can interface with quantum memories and telecom-band photons that feature low-loss transmission in optical fibers.

# Challenges and perspectives

In this review, the rapid advances in chip-based quantum communication relying on the development of integrated quantum photonics are discussed. Photonic integration not only provides a solid strategy for the miniaturization and scaling of quantum communication

![](images/a63f6cadc1069d418b25cb526aab58b50db07efc1039f188287b8396296fea35.jpg)  
a

![](images/01d7d9e7199f034747c374e8a1a3a37af71d113856d8d7bd4a3a39c0f10e9361.jpg)  
b

![](images/ce4450c094eba0ca3eef8e27984004598875f11549af9de27ef9482b54d426d6.jpg)  
C  
Fig. 13 Chip-based quantum teleportation and entanglement distribution systems. a Scheme of an on-chip quantum teleportation experiment in a silica-on-silicon integrated chip $^{90}$ . b Silicon photonic circuit diagram for a chip-to-chip entanglement distribution experiment $^{100}$ . c Photonic circuit diagram for a chip-to-chip quantum teleportation experiment $^{44}$ . Panels reproduced with permission from: a ref.  ${}^{90}$ , Springer Nature Ltd; b ref.  ${}^{100}$ , The Optical Society; c ref.  ${}^{44}$ , Springer Nature Ltd

systems but also fosters practical applications of quantum communication and paves the way for future quantum communication networks and the quantum internet.

Although considerable progress has been achieved, the field of chip-based quantum communication is still in its early stages and naturally faces many challenges. On the component side, on-chip elements used in quantum communication require more stringent specifications than those used in classical optical communication to ensure high fidelity and prevent decoherence of quantum states during the process of preparation, manipulation, transmission, and detection. Hence, the exploration of components with suitable characteristics is crucial. For example, high-key-rate QKD calls for modulators that can operate at high clock rates while maintaining an acceptable extinction ratio for low crosstalk between different quantum states. However, this demand cannot always be satisfied by conventional Si-based modulators because carrier injection or carrier depletion techniques induce non-ideal loss characteristics. Fortunately, recent progress in ultra-high extinction  $(>65\mathrm{dB})$  Si modulators based on a cascaded MZI structure[179] and  $\mathrm{LN}^{180}$ ,  $\mathrm{Si - LN}^{40}$ , and Si-barium titanate[181] modulators based on the electro-optical Pockels effect provides possible solutions to this problem.

On the system side, fully integrated quantum communication systems with photon sources, photonic circuits, and detectors have not yet been realized. The difficulties in achieving full integration are due to two challenges: (i) the first challenge is that no monolithic platform can

provide all the desired features for quantum communication applications. Hybrid integration, as discussed in the section "Key technologies for quantum photonic chips", could be a viable solution to address this problem. However, the technique is still under development and requires more effort to achieve the final goal. Fortunately, a detailed roadmap for realizing future large-scale hybrid integrated quantum photonic systems has been summarized[50]; (ii) the second challenge is that different parts of an integrated quantum system may work in different conditions. For example, QD single-photon sources and single-photon detectors usually operate at cryogenic temperatures. In contrast, conventional integrated modulators and thermo-optic phase shifters are designed for room temperature applications and cannot function properly under these extreme conditions. Photon manipulation at cryogenic temperatures has thus become a crucial factor for fully integrated systems. Recently, an integrated cryogenic Si-barium titanate modulator[182] and microelectromechanical photonic circuits interfaced with SNSPDs on the same chip[104] have been demonstrated, removing major roadblocks for the realization of cryogenic-compatible systems. Furthermore, at a practical level, targeting truly useful systems with potential for industrial development will require the integration of both optics and electronics. A recent demonstration has shown the feasibility of integrating photonics with silicon nanoelectronics to construct complete systems on a chip for quantum communication[183].

On the security side, chip-based quantum communication faces potential loophole threats due to the specific imperfections of integrated photonic devices. For instance, phase- and polarization-dependent losses are significant problems in quantum photonic chips that, if unchecked, could lead to an overestimation of the secret key rate, compromising the security of QKD systems. To solve these problems, a post-selection scheme has recently been proposed that provides a high key generation rate even in the presence of severe phase- and polarization-dependent losses[184]. A decoy-state BB84 QKD experiment considering polarization-dependent loss exploited the proposal and successfully distributed secure key bits over fiber links up to  $75\mathrm{km}^{185}$ . Additionally, the security loopholes originating from the plasma dispersion effect of free carriers[186] and the integrated electrical control circuit of the transmitter[187] have been revealed and analyzed in chip-based CV-QKD systems. Since there are still doubts about practical QKD implementations from government organizations like the National Security Agency (NSA) of the USA and the National Cyber Security Centre (NCSC) of the UK, further studies with comprehensive security analysis are needed to close the gap between theoretical models and practical integrated quantum communication systems.

Beyond prepare-and-measure QKD, entanglement-based QKD is another promising application for future chip-based QKD systems. This has become possible since time-bin entangled states were generated in GaAs $^{188}$ , Si $^{189}$  and  $\mathrm{Si}_3\mathrm{N}_4^{71,178}$  chips, and the chip-to-chip entanglement distribution $^{100}$  and quantum teleportation $^{44}$  were demonstrated between two programmable Si chips. Combined with recent experimental progress $^{190-192}$ , integrated photonics provide a viable way for the realization of compact entanglement-based systems that support device-independent QKD over kilometer-scale distances. In addition, QSDC can also utilize the great potential of quantum photonic chips in developing practical QSDC systems and networks as the protocol share a similar setup with QKD $^{27,31,32}$ .

Currently, on-chip quantum teleportation is mostly based on posterior and passive protocols. Future work may include implementing feed-forward control by upgrading a quantum communication system from passive to active so that the receiver can apply conditional unitary operation in real-time to reconstruct quantum states. Furthermore, long-distance entanglement distribution and quantum teleportation and large-scale implementations of quantum networks rely on quantum memories and quantum relays[22,193]. For example, quantum memories in quantum nodes can generate entanglement between distant parties and therefore extend the communication distance. However, the experimental development of integrated quantum memory is still in its

infancy. There is still much work to be done to achieve integrated quantum relays in the telecom band that are compatible with fiber-based long-distance quantum communication systems.

For practical applications of quantum communication, the loss and decoherence in transferring photons between different chips, either through optical fiber or free space, can greatly limit the fidelity of the network. Several solutions have been proposed to address the problem originating from optical coupling. For instance, edge coupling via a tapered silicon waveguide surrounded by a  $\mathrm{SiO}_2$  cladding cantilever structure was utilized, shrinking the coupling loss to  $1.3\mathrm{dB / facet}^{194,195}$ . By engineering the effective refractive index of the waveguides, subwavelength waveguide grating-based edge couplings could achieve coupling efficiencies as high as  $0.32\mathrm{dB / facet}$ $(93\%)^{196}$ . For the packaging process of multiport coupling, methods using intermediate mode transformation stages waveguide such as ribbon layers[197], photonic wire bonding[198], and 3D printing free-form lenses and mirrors[199] were employed to reduce coupling loss. However, the edge coupling strategy is frequently constrained by the effective modal refractive index and mode-size mismatch between the waveguide and fiber due to fabrication or alignment deviation. The technique using evanescent coupling between tapered waveguides and single-sided conical tapered fibers could overcome this shortage and produce highly effective coupling up to  $0.13\mathrm{dB / facet}$ $(97\%)^{200}$ .

As another factor that drives the compact integration of optical components, quantum computing on integrated photonic chips has also attracted much attention in recent years. There are two types of optical models $^{201}$ : specific quantum computing models $^{202,203}$  (e.g., boson sampling), and universal quantum computing models $^{204-209}$  (e.g., one-way or measurement-based). For specific quantum computation, a variety of photonic systems were demonstrated using quantum photonic chips $^{210-217}$ , enabling a natural and effective implementation of boson sampling. Gaussian boson sampling $^{218,219}$ , which can dramatically enhance the sampling rate with the adoption of squeezed light sources, was performed for the calculation of molecular vibronic spectra on a Si chip $^{217}$  (up to 8 photons) and a SiN chip $^{216}$  (up to 18 photons). Recently, quantum computational advantage has been delivered by photonic Gaussian boson sampling processors $^{220,221}$ , paving the path for further development of integrated specific quantum computers with potential applications including graph optimization $^{222}$ , complex molecular spectra $^{223}$ , molecular docking $^{224}$ , quantum chemistry $^{225}$ , etc. For universal quantum computation, a number of major functionalities have been demonstrated with on-chip photonic components, such as controlled-NOT gate and its heralding version $^{92,226}$ , and compiled Shor's

factorization $^{227}$ . Moreover, both architectural and technological efforts have been dedicated to photonic one-way quantum computation. This approach employs cluster states and sequential single-qubit measurement to perform universal quantum algorithms $^{205,207,228}$  and can be greatly enhanced by implementing resource state generation and fusion operation natively $^{229-231}$ . The relevant circuit implementations include programmable four-photon graph states on a Si chip $^{232}$ , path-polarization hyperentangled and cluster states on a  $\mathrm{SiO}_2$  chip $^{233}$  and programmable eight-qubit graph states on a Si chip $^{234}$ .

In conclusion, quantum photonic chips have rapidly matured to become a versatile platform that proves to be invaluable in the development of cutting-edge quantum communication technologies. This review delves into the advancements achieved in this particular field. Considering the remarkable outcomes, it is anticipated that photonic integration will eventually assume a crucial role in building various quantum networks and potentially a global quantum internet, reshaping the landscape of future communication methodologies.

# Acknowledgements

This work was supported by the Singapore Ministry of Education (MOE) Tier 3 grant (MOE2017-T3-1-001), NRF grant (MOH-000926), A*STAR research grant (SERC-A18A5b0056) and PUB Singapore's National Water Agency grant (PUB-1804-0082).

# Author details

<sup>1</sup>Quantum Science and Engineering Centre (QSec), Nanyang Technological University, Singapore 639798, Singapore. <sup>2</sup>Institute of Precision Optical Engineering, School of Physics Science and Engineering, Tongji University, 200092 Shanghai, China. <sup>3</sup>School of Optoelectronic Science and Engineering, University of Electronic Science and Technology of China, 610054 Chengdu, China. <sup>4</sup>School of Electronics and Communication Engineering, Sun Yat-Sen University, 518100 Shenzhen, Guangdong, China. <sup>5</sup>Institute of Microelectronics, A*STAR (Agency for Science, Technology and Research), Singapore 138634, Singapore. <sup>6</sup>Centre for Quantum Technologies, National University of Singapore, 3 Science Drive 2, Singapore 117543, Singapore. <sup>7</sup>National Institute of Education, Nanyang Technological University, Singapore 637616, Singapore

# Competing interests

The authors declare no competing interests.

Received: 7 August 2022 Revised: 27 April 2023 Accepted: 28 April 2023  
Published online: 14 July 2023

# References

1. Bennett, C. H. & Brassard, G. Quantum cryptography: public key distribution and coin tossing. Proc. International Conference on Computers, Systems & Signal Processing 175-179 (IEEE, Bangalore, 1984).  
2. Bennett, C. H. et al. Experimental quantum cryptography. J. Cryptol. 5, 3-28 (1992).  
3. Shor, P. W. & Preskill, J. Simple proof of security of the BB84 quantum key distribution protocol. Phys. Rev. Lett. 85, 441-444 (2000).  
4. Gisin, N. et al. Quantum cryptography. Rev. Mod. Phys. 74, 145-195 (2002).  
5. Xu, F. H. et al. Secure quantum key distribution with realistic devices. Rev. Mod. Phys. 92, 025002 (2020).  
6. Wang, S. et al. Twin-field quantum key distribution over 830-km fibre. Nat. Photonics 16, 154-161 (2022).

7. Chen, Y. A. et al. An integrated space-to-ground quantum communication network over 4,600 kilometres. Nature 589, 214-219 (2021).  
8. Li, W. et al. High-rate quantum key distribution exceeding  $110\mathrm{Mb}\mathrm{s}^{-1}$ . Nat. Photonics 17, 416-421 (2023).  
9. Peev, M. et al. The SECOQC quantum key distribution network in Vienna. N. J. Phys. 11, 075001 (2009).  
10. Stucki, D. et al. Long-term performance of the SwissQuantum quantum key distribution network in a field environment. N. J. Phys. 13, 123001 (2011).  
11. Avesani, M. et al. Deployment-ready quantum key distribution over a classical network infrastructure in Padua. J. Lightwave Technol. 40, 1658-1663 (2022).  
12. Sasaki, M. et al. Field test of quantum key distribution in the Tokyo QKD network. Opt. Express 19, 10387-10409 (2011).  
13. Chen, T. Y. et al. Field test of a practical secure communication network with decoy-state quantum cryptography. Opt. Express 17, 6540-6549 (2009).  
14. Wang, S. et al. Field and long-term demonstration of a wide area quantum key distribution network. Opt. Express 22, 21739-21756 (2014).  
15. Dynes, J. F. et al. Cambridge quantum network. npj Quantum Inf. 5, 101 (2019).  
16. Scarani, V. et al. The security of practical quantum key distribution. Rev. Mod. Phys. 81, 1301-1350 (2009).  
17. Diamanti, E. et al. Practical challenges in quantum key distribution. npj Quantum Inf. 2, 16025 (2016).  
18. Wang, L. J. et al. Experimental authentication of quantum key distribution with post-quantum cryptography. npj Quantum Inf. 7, 67 (2021).  
19. Bennett, C. H. et al. Teleporting an unknown quantum state via dual classical and Einstein-Podolsky-Rosen channels. Phys. Rev. Lett. 70, 1895-1899 (1993).  
20. Bouwmeester, D. et al. Experimental quantum teleportation. Nature 390, 575-579 (1997).  
21. Furusawa, A. et al. Unconditional quantum teleportation. Science 282, 706-709 (1998).  
22. Wehner, S., Elkouss, D. & Hanson, R. Quantum internet: a vision for the road ahead. Science 362, eaam9288 (2018).  
23. Kimble, H. J. The quantum internet. Nature 453, 1023-1030 (2008).  
24. Long, G. L. & Liu, X. S. Theoretically efficient high-capacity quantum-key-distribution scheme. Phys. Rev. A 65, 032302 (2002).  
25. Deng, F. G., Long, G. L. & Liu, X. S. Two-step quantum direct communication protocol using the Einstein-Podolsky-Rosen pair block. Phys. Rev. A 68, 042317 (2003).  
26. Deng, F. G. & Long, G. L. Secure direct communication with a quantum onetime pad. Phys. Rev. A 69, 052319 (2004).  
27. Hu, J. Y. et al. Experimental quantum secure direct communication with single photons. Light Sci. Appl. 5, e16144 (2016).  
28. Zhang, W. et al. Quantum secure direct communication with quantum memory. Phys. Rev. Lett. 118, 220501 (2017).  
29. Zhu, F. et al. Experimental long-distance quantum secure direct communication. Sci. Bull. 62, 1519-1524 (2017).  
30. Qi, R. Y. et al. Implementation and security analysis of practical quantum secure direct communication. Light Sci. Appl. 8, 22 (2019).  
31. Zhang, H. R. et al. Realization of quantum secure direct communication over  $100\mathrm{km}$  fiber with time-bin and phase quantum states. Light Sci. Appl. 11, 83 (2022).  
32. Qi, Z. T. et al. A 15-user quantum secure direct communication network. Light Sci. Appl. 10, 183 (2021).  
33. Long, G. L. et al. An evolutionary pathway for the quantum internet relying on secure classical repeaters. IEEE Netw. 36, 82-88 (2022).  
34. Orieux, A. & Diamanti, E. Recent advances on integrated quantum communications. J. Opt. 18, 083002 (2016).  
35. Wang, J. W. et al. Integrated photonic quantum technologies. Nat. Photonics 14, 273-284 (2020).  
36. Matthews, J. C. F. et al. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nat. Photonics 3, 346-350 (2009).  
37. Siew, S. Y. et al. Review of silicon photonics technology and platform development. J. Lightwave Technol. 39, 4374-4389 (2021).  
38. Smit, M., Williams, K. & van der Tol, J. Past, present, and future of InP-based photonic integration. APL Photonics 4, 050901 (2019).  
39. Joshi, C. et al. Frequency multiplexing for quasi-deterministic heralded single-photon sources. Nat. Commun. 9, 847 (2018).  
40. He, M. B. et al. High-performance hybrid silicon and lithium niobate Mach-Zehnder modulators for 100 Gbit s $^{-1}$  and beyond. Nat. Photonics 13, 359-364 (2019).

41. Pernice, W. H. P. et al. High-speed and high-efficiency travelling wave single-photon detectors embedded in nanophotonic circuits. Nat. Commun. 3, 1325 (2012).  
42. Sibson, P. et al. Chip-based quantum key distribution. Nat. Commun. 8, 13984 (2017).  
43. Zhang, G. et al. An integrated silicon photonic chip platform for continuous-variable quantum key distribution. Nat. Photonics 13, 839-842 (2019).  
44. Llewellyn, D. et al. Chip-to-chip quantum teleportation and multi-photon entanglement in silicon. Nat. Phys. 16, 148-153 (2020).  
45. Tanzilli, S. et al. PPLN waveguide for quantum communication. Eur. Phys. J. D. - At, Mol., Opt. Plasma Phys. 18, 155-160 (2002).  
46. Bonfrate, G. et al. Asymmetric Mach-Zehnder germano-silicate channel waveguide interferometers for quantum cryptography systems. *Electron. Lett.* 37, 846-847 (2001).  
47. Honjo, T., Inoue, K. & Takahashi, H. Differential-phase-shift quantum key distribution experiment with a planar light-wave circuit Mach-Zehnder interferometer. Opt. Lett. 29, 2797-2799 (2004).  
48. Takesue, H. et al. Differential phase shift quantum key distribution experiment over 105 km fibre. N. J. Phys. 7, 232 (2005).  
49. Diamanti, E. et al. 100 km differential phase shift quantum key distribution experiment with low jitter up-conversion detectors. Opt. Express 14, 13073-13082 (2006).  
50. Elshaari, A. W. et al. Hybrid integrated quantum photonic circuits. Nat. Photonics 14, 285-298 (2020).  
51. Agnesi, C. et al. Hong-Ou-Mandel interference between independent III-V on silicon waveguide integrated lasers. Opt. Lett. 44, 271-274 (2019).  
52. Lodahl, P., Mahmoodian, S. & Stobbe, S. Interfacing single photons and single quantum dots with photonic nanostructures. Rev. Mod. Phys. 87, 347-400 (2015).  
53. Schröder, T. et al. Quantum nanophotonics in diamond [Invited]. J. Opt. Soc. Am. B 33, B65-B83 (2016).  
54. Lenzini, F. et al. Diamond as a platform for integrated quantum photonics. Adv. Quantum Technol. 1, 1800061 (2018).  
55. Senellart, P., Solomon, G. & White, A. High-performance semiconductor quantum-dot single-photon sources. Nat. Nanotechnol. 12, 1026-1039 (2017).  
56. Orieux, A. et al. Semiconductor devices for entangled photon pair generation: a review. Rep. Prog. Phys. 80, 076001 (2017).  
57. Ding, X. et al. On-demand single photons with high extraction efficiency and near-unity indistinguishability from a resonantly driven quantum dot in a micropillar. Phys. Rev. Lett. 116, 020401 (2016).  
58. Somaschi, N. et al. Near-optimal single-photon sources in the solid state. Nat. Photonics 10, 340-345 (2016).  
59. Arcari, M. et al. Near-unity coupling efficiency of a quantum emitter to a photonic crystal waveguide. Phys. Rev. Lett. 113, 093603 (2014).  
60. Davanco, M. et al. Heterogeneous integration for on-chip quantum photonic circuits with single quantum dot devices. Nat. Commun. 8, 889 (2017).  
61. Benson, O. et al. Regulated and entangled photons from a single quantum dot. Phys. Rev. Lett. 84, 2513-2516 (2000).  
62. Müller, M. et al. On-demand generation of indistinguishable polarization-entangled photon pairs. Nat. Photonics 8, 224-228 (2014).  
63. Chung, T. H. et al. Selective carrier injection into patterned arrays of pyramidal quantum dots for entangled photon light-emitting diodes. Nat. Photonics 10, 782-787 (2016).  
64. Liu, J. et al. A solid-state source of strongly entangled photon pairs with high brightness and indistinguishability. Nat. Nanotechnol. 14, 586-593 (2019).  
65. Castelletto, S. et al. A silicon carbide room-temperature single-photon source. Nat. Mater. 13, 151-156 (2014).  
66. Hogele, A. et al. Photon antibunching in the photoluminescence spectra of a single carbon nanotube. Phys. Rev. Lett. 100, 217401 (2008).  
67. He, Y. M. et al. Single quantum emitters in monolayer semiconductors. Nat. Nanotechnol. 10, 497-502 (2015).  
68. Kim, S. et al. Integrated on chip platform with quantum emitters in layered materials. Adv. Opt. Mater. 7, 1901132 (2019).  
69. Engin, E. et al. Photon pair generation in a silicon micro-ring resonator with reverse bias enhancement. Opt. Express 21, 27826-27834 (2013).  
70. Spring, J. B. et al. Chip-based array of near-identical, pure, heralded single-photon sources. Optica 4, 90-96 (2017).  
71. Lu, X. Y. et al. Chip-integrated visible-telecom entangled photon pair source for quantum communication. Nat. Phys. 15, 373-381 (2019).

72. Jin, H. et al. On-chip generation and manipulation of entangled photons based on reconfigurable lithium-niobate waveguide circuits. Phys. Rev. Lett. 113, 103601 (2014).  
73. Horn, R. et al. Monolithic source of photon pairs. Phys. Rev. Lett. 108, 153605 (2012).  
74. Collins, M. J. et al. Integrated spatial multiplexing of heralded single-photon sources. Nat. Commun. 4, 2582 (2013).  
75. Meany, T. et al. Hybrid photonic circuit for multiplexed heralded single photons. Laser Photonics Rev. 8, L42-L46 (2014).  
76. Kaneda, F. & Kwiat, P. G. High-efficiency single-photon generation via large-scale active time multiplexing. Sci. Adv. 5, eaaw8586 (2019).  
77. Saravi, S., Pertsch, T. & Setzpfandt, F. Lithium niobate on insulator: an emerging platform for integrated quantum photonics. Adv. Opt. Mater. 9, 2100789 (2021).  
78. Hwang, W. Y. Quantum key distribution with high loss: toward global secure communication. Phys. Rev. Lett. 91, 057901 (2003).  
79. Lo, H. K., Ma, X. F. & Chen, K. Decoy state quantum key distribution. Phys. Rev. Lett. 94, 230504 (2005).  
80. Wang, X. B. Beating the photon-number-splitting attack in practical quantum cryptography. Phys. Rev. Lett. 94, 230503 (2005).  
81. Semenenko, H. et al. Chip-based measurement-device-independent quantum key distribution. Optica 7, 238-242 (2020).  
82. Ma, Y. J. et al. Symmetrical polarization splitter/rotator design and application in a polarization insensitive WDM receiver. Opt. Express 23, 16052-16062 (2015).  
83. Harris, N. C. et al. Efficient, compact and low loss thermo-optic phase shifter in silicon. Opt. Express 22, 10487-10493 (2014).  
84. Weigel, P. O. et al. Bonded thin film lithium niobate modulator on a silicon photonics platform exceeding 100 GHz 3-dB electrical modulation bandwidth. Opt. Express 26, 23728-23739 (2018).  
85. Xu, P. P. et al. Low-loss and broadband nonvolatile phase-change directional coupler switches. ACS Photonics 6, 553-557 (2019).  
86. Peruzzo, A. et al. Multimode quantum interference of photons in multiport integrated devices. Nat. Commun. 2, 224 (2011).  
87. Elshaari, A. W. et al. On-chip single photon filtering and multiplexing in hybrid quantum photonic circuits. Nat. Commun. 8, 379 (2017).  
88. Hong, S. H. et al. Ultralow-loss compact silicon photonic waveguide spirals and delay lines. Photonics Res. 10, 1-7 (2022).  
89. Qiang, X. G. et al. Large-scale silicon quantum photonics implementing arbitrary two-qubit processing. Nat. Photonics 12, 534-539 (2018).  
90. Metcalf, B. J. et al. Quantum teleportation on a photonic chip. Nat. Photonics 8, 770-774 (2014).  
91. Wang, J. W. et al. Gallium arsenide (GaAs) quantum photonic waveguide circuits. Opt. Commun. 327, 49-55 (2014).  
92. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
93. Wang, J. W. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
94. Wei, K. J. et al. High-speed measurement-device-independent quantum key distribution with integrated silicon photonics. Phys. Rev. X 10, 031030 (2020).  
95. Ma, C. X. et al. Silicon photonic transmitter for polarization-encoded quantum key distribution. Optica 3, 1274-1278 (2016).  
96. Cao, L. et al. Chip-based measurement-device-independent quantum key distribution using integrated silicon photonic systems. Phys. Rev. Appl. 14, 011001 (2020).  
97. Marchetti, R. et al. Coupling strategies for silicon photonics integrated chips [Invited]. Photonics Res. 7, 201-239 (2019).  
98. Cardenas, J. et al. High coupling efficiency etched facet tapers in silicon waveguides. IEEE Photonics Technol. Lett. 26, 2380-2382 (2014).  
99. Olislager, L. et al. Silicon-on-insulator integrated source of polarization-entangled photons. Opt. Lett. 38, 1960-1962 (2013).  
100. Wang, J. W. et al. Chip-to-chip quantum photonic interconnect by path-polarization interconversion. Optica 3, 407-413 (2016).  
101. Martinez, N. J. D. et al. Single photon detection in a waveguide-coupled Geon-Si lateral avalanche photodiode. Opt. Express 25, 16130-16139 (2017).  
102. Sprengers, J. P. et al. Waveguide superconducting single-photon detectors for integrated quantum photonic circuits. Appl. Phys. Lett. 99, 181110 (2011).  
103. Schuck, C. et al. Quantum interference in heterogeneous superconducting-photonic circuits on a silicon chip. Nat. Commun. 7, 10352 (2016).  
104. Gyger, S. et al. Reconfigurable photonics with on-chip single-photon detectors. Nat. Commun. 12, 1408 (2021).

105. Lomonte, E. et al. Single-photon detection and cyrogenic reconfigurability in lithium niobate nanophotonic circuits. Nat. Commun. 12, 6847 (2021).  
106. Sahin, D. et al. Waveguide photon-number-resolving detectors for quantum photonic integrated circuits. Appl. Phys. Lett. 103, 111116 (2013).  
107. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).  
108. Gerrits, T. et al. On-chip, photon-number-resolving, telecommunication-band detectors for scalable photonic information processing. Phys. Rev. A 84, 060301 (2011).  
109. Hopker, J. P. et al. Towards integrated superconducting detectors on lithium niobate waveguides. Proceedings of SPIE 10358, (eds Soci, C., Agio, M. & Srinivasan K) Quantum Photonic Devices (SPIE, San Diego, 2017).  
110. Raffaelli, F. et al. A homodyne detector integrated onto a photonic chip for measuring quantum states and generating random numbers. Quantum Sci. Technol. 3, 025003 (2018).  
111. Tasker, J. F. et al. Silicon photonics interfaced with integrated electronics for 9 GHz measurement of squeezed light. Nat. Photonics 15, 11-15 (2021).  
112. Bai, B. et al. 18.8 gpbs real-time quantum random number generator with a photonic integrated chip. Appl. Phys. Lett. 118, 264001 (2021).  
113. Milovancev, D. et al. Chip-level GHz capable balanced quantum homodyne receivers. J. Lightwave Technol. 40, 7518-7528 (2022).  
114. Bruynsteen, C. et al. Integrated balanced homodyne photonic-electronic detector for beyond 20 GHz shot-noise-limited measurements. Optica 8, 1146-1152 (2021).  
115. Carroll, L. et al. Photonic packaging: transforming silicon photonic integrated circuits into photonic devices. Appl. Sci. 6, 426 (2016).  
116. Zimmermann, L. et al. Packaging and assembly for integrated photonics—a review of the ePIXpack photonics packaging platform. IEEE J. Sel. Top. Quantum Electron. 17, 645-651 (2011).  
117. O'Brien, P. et al. Packaging of silicon photonic devices. In Silicon Photonics II: Systems and Applications (eds Pavesi, L. & Lockwood, D. J.) 217-236 (Springer, Berlin, 2016).  
118. Lee, J. S. et al. Meeting the electrical, optical, and thermal design challenges of photonic-packaging. IEEE J. Sel. Top. Quantum Electron. 22, 8200209 (2016).  
119. Taillaert, D. et al. Grating couplers for coupling between optical fibers and nanophotonic waveguides. Jpn. J. Appl. Phys. 45, 6071-6077 (2006).  
120. Pu, M. H. et al. Ultra-low-loss inverted taper coupler for silicon-on-insulator ridge waveguide. Opt. Commun. 283, 3678-3682 (2010).  
121. He, L. Y. et al. Low-loss fiber-to-chip interface for lithium niobate photonic integrated circuits. Opt. Lett. 44, 2314-2317 (2019).  
122. Preble, S. F. et al. On-chip quantum interference from a single silicon ring-resonator source. Phys. Rev. Appl. 4, 021001 (2015).  
123. Sacher, W. D. et al. Wide bandwidth and high coupling efficiency  $\mathrm{Si}_3\mathrm{N}_4$  on-SOI dual-level grating coupler. Opt. Express 22, 10938-10947 (2014).  
124. Marchetti, R. et al. High-efficiency grating-couplers: demonstration of a new design strategy. Sci. Rep. 7, 16670 (2017).  
125. Bakir, B. B. et al. Low-loss (<1 dB) and polarization-insensitive edge fiber couplers fabricated on 200-mm silicon-on-insulator wafers. IEEE Photonics Technol. Lett. 22, 739-741 (2010).  
126. Dangel, R. et al. Polymer waveguides for electro-optical integration in data centers and high-performance computers. Opt. Express 23, 4736-4750 (2015).  
127. Taballione, C. et al. A universal fully reconfigurable 12-mode quantum photonic processor. Mater. Quantum Technol. 1, 035002 (2021).  
128. Abrams, N. C. et al. Silicon photonic 2.5D multi-chip module transceiver for high-performance data centers. J. Lightwave Technol. 38, 3346-3357 (2020).  
129. Worhoff, K. et al. Flip-chip assembly for photonic circuits. Proceedings of SPIE 5454, Micro-Optics: Fabrication, Packaging, and Integration 9–20 (SPIE, Strasbourg, 2004).  
130. Zhang, X. R. et al. Copper pillar bump structure optimization for flip chip packaging with Cu/Low-K stack. Proc. 11th International Thermal, Mechanical & Multi-Physics Simulation, and Experiments in Microelectronics and Microsystems. 1-7 (IEEE, Bordeaux, 2010).  
131. Pirandola, S. et al. Advances in quantum cryptography. Adv. Opt. Photonics 12, 1012-1236 (2020).  
132. Kwek, L. C. et al. Chip-based quantum key distribution. AAPPS Bull. 31, 15 (2021).  
133. Stipcevic, M. Quantum random number generators and their applications in cryptography. Proc. SPIE 8375, Advanced Photon Counting Techniques VI. 837504 (eds Itzler, M. A.) (SPIE, Baltimore, 2012).  
134. Williams, C. R. S. et al. Fast physical random number generator using amplified spontaneous emission. Opt. Express 18, 23584-23597 (2010).

135. Qi, B. et al. High-speed quantum random number generation by measuring phase noise of a single-mode laser. Opt. Lett. 35, 312-314 (2010).  
136. Xu, F. H. et al. Ultrafast quantum random number generation based on quantum phase fluctuations. Opt. Express 20, 12366-12377 (2012).  
137. Nie, Y. Q. et al. The generation of 68 Gbps quantum random number by measuring laser phase fluctuations. Rev. Sci. Instrum. **86**, 063105 (2015).  
138. Liu, J. L. et al. 117 Gbits/s quantum random number generation with simple structure. IEEE Photonics Technol. Lett. 29, 283-286 (2017).  
139. Gabriel, C. et al. A generator for unique quantum random numbers based on vacuum states. Nat. Photonics 4, 711-715 (2010).  
140. Symul, T., Assad, S. M. & Lam, P. K. Real time demonstration of high bitrate quantum random number generation with coherent laser light. Appl. Phys. Lett. 98, 231103 (2011).  
141. Shi, Y. C., Chng, B. & Kurtsiefer, C. Random numbers from vacuum fluctuations. Appl. Phys. Lett. 109, 041101 (2016).  
142. Zheng, Z. Y. et al. 6 Gbps real-time optical quantum random number generator based on vacuum fluctuation. Rev. Sci. Instrum. 90, 043105 (2019).  
143. Zhou, Q. et al. Practical quantum random-number generation based on sampling vacuum fluctuations. Quantum Eng. 1, e8 (2019).  
144. Haylock, B. et al. Multiplexed quantum random number generation. Quantum 3, 141 (2019).  
145. Abellan, C. et al. Quantum entropy source on an InP photonic integrated circuit for random number generation. Optica 3, 989-994 (2016).  
146. Raffaelli, F. et al. Generation of random numbers by measuring phase fluctuations from a laser diode with a silicon-on-insulator chip. Opt. Express 26, 19730-19741 (2018).  
147. Regazzoni, F. et al. A high speed integrated quantum random number generator with on-chip real-time randomness extraction. Preprint at https://doi.org/10.48550/arXiv.2102.06238 (2021).  
148. Bruynsteen, C. et al. 100-Gbit/s Integrated Quantum Random Number Generator Based on Vacuum Fluctuations. PRX Quantum 4, 010330 (2023).  
149. Hughes, R. J. et al. Network-centric quantum communications with application to critical infrastructure protection. Print at https://doi.org/10.48550/arXiv.1305.0305 (2013).  
150. Zhang, P. et al. Reference-frame-independent quantum-key-distribution server with a telecom tether for an on-chip client. Phys. Rev. Lett. 112, 130501 (2014).  
151. Vest, G. et al. Design and evaluation of a handheld quantum key distribution sender module. IEEE J. Sel. Top. Quantum Electron. 21, 6600607 (2015).  
152. Thompson, M. G. Large-scale integrated quantum photonic technologies for communications and computation. Proc. 2019 Optical Fiber Communications Conference. 1-3. (IEEE, San Diego, 2019).  
153. Paraiso, T. K. et al. A modulator-free quantum key distribution transmitter chip. npj Quantum Inf. 5, 42 (2019).  
154. Paraiso, T. K. et al. A photonic integrated quantum secure communication system. Nat. Photonics 15, 850-856 (2021).  
155. Sibson, P. et al. Integrated silicon photonics for high-speed quantum key distribution. Optica 4, 172-177 (2017).  
156. Cai, H. et al. Silicon photonic transceiver circuit for high-speed polarization-based discrete variable quantum key distribution. Opt. Express 25, 12282-12294 (2017).  
157. Bunandar, D. et al. Metropolitan quantum key distribution with silicon photonics. Phys. Rev. X 8, 021009 (2018).  
158. Avesani, M. et al. Full daylight quantum-key-distribution at  $1550\mathrm{nm}$  enabled by integrated silicon photonics. npj Quantum Inf. 7, 93 (2021).  
159. Geng, W. et al. Stable quantum key distribution using a silicon photonic transceiver. Opt. Express 27, 29045-29054 (2019).  
160. Dai, J. C. et al. Pass-block architecture for distributed-phase-reference quantum key distribution using silicon photonics. Opt. Lett. 45, 2014-2017 (2020).  
161. Kong, L. W. et al. Photonic integrated quantum key distribution receiver for multiple users. Opt. Express 28, 18449-18455 (2020).  
162. Ding, Y. H. et al. High-dimensional quantum key distribution based on multicore fiber using silicon photonic integrated circuits. npj Quantum Inf. 3, 25 (2017).  
163. Semenenko, H. et al. Interference between independent photonic integrated devices for quantum key distribution. Opt. Lett. 44, 275-278 (2019).  
164. Wang, C. Y. et al. Integrated measurement server for measurement-device-independent quantum key distribution network. Opt. Express 27, 5982-5989 (2019).

165. Zheng, X. D. et al. Heterogeneously integrated, superconducting silicon-photonic platform for measurement-device-independent quantum key distribution. Adv. Photonics 3, 055002 (2021).  
166. Grosshans, F. & Grangier, P. Continuous variable quantum cryptography using coherent states. Phys. Rev. Lett. 88, 057902 (2002).  
167. Grosshans, F. et al. Quantum key distribution using Gaussian-modulated coherent states. Nature 421, 238-241 (2003).  
168. Weedbrook, C. et al. Gaussian quantum information. Rev. Mod. Phys. 84, 621-669 (2012).  
169. Ziebell, M. et al. Towards on-chip continuous-variable quantum key distribution. Proc. European Conference on Lasers and Electro-Optics—European Quantum Electronics Conference 2015. JSV_4_2 (Optica Publishing Group, Munich, 2015).  
170. Pirandola, S. et al. Advances in quantum teleportation. Nat. Photonics 9, 641-652 (2015).  
171. Ren, J. G. et al. Ground-to-satellite quantum teleportation. Nature 549, 70-73 (2017).  
172. Takesue, H. et al. Quantum teleportation over  $100\mathrm{km}$  of fiber using highly efficient superconducting nanowire single-photon detectors. Optica 2, 832-835 (2015).  
173. Huo, M. R. et al. Deterministic quantum teleportation through fiber channels. Sci. Adv. 4, eaas9401 (2018).  
174. Nölleke, C. et al. Efficient teleportation between remote single-atom quantum memories. Phys. Rev. Lett. 110, 140403 (2013).  
175. Liu, H. Y. et al. Optical-relayed entanglement distribution using drones as mobile nodes. Phys. Rev. Lett. 126, 020503 (2021).  
176. Wang, Q. Q. et al. Chip-based quantum communications. J. Semicond. 42, 091901 (2021).  
177. Corielli, G. et al. Rotated waveplates in integrated waveguide optics. Nat. Commun. 5, 4249 (2014).  
178. Zhang, X. et al. Integrated silicon nitride time-bin entanglement circuits. Opt. Lett. 43, 3469-3472 (2018).  
179. Liu, S. et al. High speed ultra-broadband amplitude modulators with ultra-high extinction  $>65$  dB. Opt. Express 25, 11254-11264 (2017).  
180. Wang, C. et al. Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages. Nature 562, 101-104 (2018).  
181. Abel, S. et al. Large Pockels effect in micro- and nanostructured barium titanate integrated on silicon. Nat. Mater. 18, 42-47 (2019).  
182. Eltes, F. et al. An integrated optical modulator operating at cryogenic temperatures. Nat. Mater. 19, 1164-1168 (2020).  
183. Atabaki, A. H. et al. Integrating photonics with silicon nanoelectronics for the next generation of systems on a chip. Nature 556, 349-354 (2018).  
184. Li, C. Y. et al. Secure quantum communication in the presence of phase- and polarization-dependent loss. Phys. Rev. A 98, 042324 (2018).  
185. Huang, C. F. et al. Experimental secure quantum key distribution in the presence of polarization-dependent loss. Phys. Rev. A 105, 012421 (2022).  
186. Li, L. et al. Practical security of a chip-based continuous-variable quantum-key-distribution system. Phys. Rev. A 103, 032611 (2021).  
187. Zheng, Y. et al. Quantum hacking on an integrated continuous-variable quantum key distribution system via power analysis. Entropy 23, 176 (2021).  
188. Autebert, C. et al. Integrated AlGaAs source of highly indistinguishable and energy-time entangled photons. Optica 3, 143-146 (2016).  
189. Grassani, D. et al. Micrometer-scale integrated silicon source of time-energy entangled photons. Optica 2, 88-94 (2015).  
190. Nadlinger, D. P. et al. Experimental quantum key distribution certified by Bell's theorem. Nature 607, 682-686 (2022).  
191. Zhang, W. et al. A device-independent quantum key distribution system for distant users. Nature 607, 687-691 (2022).  
192. Liu, W. Z. et al. Toward a photonic demonstration of device-independent quantum key distribution. Phys. Rev. Lett. 129, 050502 (2022).  
193. Hermans, S. L. N. et al. Qubit teleportation between non-neighbouring nodes in a quantum network Nature 605, 663-668 (2022).  
194. Jia, L. X. et al. Efficient suspended coupler with loss less than  $-1.4\mathrm{dB}$  between Si-photonic waveguide and cleaved single mode fiber. J. Lightwave Technol. 36, 239-244 (2018).  
195. Fang, Q. et al. Mode-size converter with high coupling efficiency and broad bandwidth. Opt. Express 19, 21588-21594 (2011).  
196. Cheben, P. et al. Broadband polarization independent nanophotonic coupler for silicon waveguides with ultra-high efficiency. Opt. Express 23, 22553-22563 (2015).

197. Barwicz, T. et al. Automated, high-throughput photonic packaging. Opt. Fiber Technol. 44, 24-35 (2018).  
198. Billah, M. R. et al. Hybrid integration of silicon photonics circuits and InP lasers by photonic wire bonding. Optica 5, 876-883 (2018).  
199. Dietrich, P. I. et al. In situ 3D nanoprinting of free-form coupling elements for hybrid photonic integration. Nat. Photonics 12, 241-247 (2018).  
200. Tiecke, T. G. et al. Efficient fiber-optical interface for nanophotonic devices. Optica 2, 70-75 (2015).  
201. Pelucchi, E. et al. The potential and global outlook of integrated photonics for quantum technologies. Nat. Rev. Phys. 4, 194-208 (2022).  
202. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. Proc. 43rd Annual ACM Symposium on Theory of Computing. 333-342 (ACM, San Jose, 2011).  
203. Rohde, P. P. & Ralph, T. C. Error tolerance of the boson-sampling model for linear optics quantum computing. Phys. Rev. A 85, 022332 (2012).  
204. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
205. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
206. Nielsen, M. A. Optical quantum computation using cluster states. Phys. Rev. Lett. 93, 040503 (2004).  
207. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169-176 (2005).  
208. Menicucci, N. C., Flammia, S. T. & Pfister, O. One-way quantum computing in the optical frequency comb. Phys. Rev. Lett. 101, 130501 (2008).  
209. Saggio, V. et al. Experimental quantum speed-up in reinforcement learning agents. Nature 591, 229-233 (2021).  
210. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
211. Broome, M. A. et al. Photonic Boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
212. Tillmann, M. et al. Experimental boson sampling. Nat. Photonics 7, 540-544 (2013).  
213. Crespi, A. et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat. Photonics 7, 545-549 (2013).  
214. Bentivegna, M. et al. Experimental scattershot boson sampling. Sci. Adv. 1, e1400255 (2015).  
215. Wang, H. et al. High-efficiency multiphoton boson sampling. Nat. Photonics 11, 361-365 (2017).  
216. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
217. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019).  
218. Hamilton, C. S. et al. Gaussian Boson sampling. Phys. Rev. Lett. 119, 170501 (2017).  
219. Kruse, R. et al. Detailed study of Gaussian boson sampling. Phys. Rev. A 100, 032326 (2019).  
220. Zhong, H. S. et al. Quantum computational advantage using photons. Science 370, 1460-1463 (2020).  
221. Madsen, L. S. et al. Quantum computational advantage with a programmable photonic processor. Nature 606, 75-81 (2022).  
222. Arrazola, J. M. & Bromley, T. R. Using Gaussian Boson sampling to find dense subgraphs. Phys. Rev. Lett. 121, 030503 (2018).  
223. Quesada, N. Franck-Condon factors by counting perfect matchings of graphs with loops. J. Chem. Phys. 150, 164113 (2019).  
224. Banchi, L. et al. Molecular docking with Gaussian Boson sampling. Sci. Adv. 6, eaax1950 (2020).  
225. Huh, J. & Yung, M. H. Vibronic Boson sampling: generalized Gaussian Boson sampling for molecular vibronic spectra at finite temperature. Sci. Rep. 7, 7462 (2017).  
226. Politi, A. et al. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
227. Politi, A., Matthews, J. C. F. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
228. Bourassa, J. E. et al. Blueprint for a scalable photonic fault-tolerant quantum computer. Quantum 5, 392 (2021).  
229. Rudolph, T. Why I am optimistic about the silicon-photonic route to quantum computing. APL Photonics 2, 030901 (2017).  
230. Browne, D. E. & Rudolph, T. Resource-efficient linear optical quantum computation. Phys. Rev. Lett. 95, 010501 (2005).  
231. Pant, M. et al. Percolation thresholds for photonic quantum computing. Nat. Commun. 10, 1070 (2019).

232. Adcock, J. C. et al. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10, 3528 (2019).  
233. Ciampini, M. A. et al. Path-polarization hyperentangled and cluster states of photons on a chip. Light Sci. Appl. 5, e16064 (2016).  
234. Vigliar, C. et al. Error-protected qubits in a silicon photonic chip. Nat. Phys. 17, 1137-1143 (2021).  
235. Silverstone, J. W. et al. Silicon quantum photonics. IEEE J. Sel. Top. Quantum Electron. 22, 390-402 (2016).  
236. Blumenthal, D. J. et al. Silicon nitride in silicon photonics. Proc. IEEE 106, 2209-2231 (2018).

237. Boes, A. et al. Status and potential of lithium niobate on insulator (LNOI) for photonic integrated circuits. *Laser Photonics* Rev. **12**, 1700256 (2018).  
238. Dietrich, C. P. et al. GaAs integrated quantum photonics: towards compact and multi-functional quantum photonic integrated circuits. *Laser Photonics* Rev. **10**, 870–894 (2016).  
239. Trenti, A. et al. Thermo-optic coefficient and nonlinear refractive index of silicon oxynitride waveguides. AlP Adv. 8, 025311 (2018).  
240. Shi, Y. et al. A review: preparation, performance, and applications of silicon oxynitride film. Micromachines 10, 552 (2019).