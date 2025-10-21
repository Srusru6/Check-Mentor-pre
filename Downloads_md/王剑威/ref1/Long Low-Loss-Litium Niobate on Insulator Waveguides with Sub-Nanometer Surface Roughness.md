Article

# Long Low-Loss-Lithium Niobate on Insulator Waveguides with Sub-Nanometer Surface Roughness

Rongbo Wu  $^{1,2,\dagger}$ , Min Wang  $^{3,4,\dagger}$ , Jian Xu  $^{3,4}$ , Jia Qi  $^{1,2}$ , Wei Chu  $^{1,4}$ , Zhiwei Fang  $^{3,4}$ , Jianhao Zhang  $^{1,2}$ , Junxia Zhou  $^{3,4}$ , Lingling Qiao  $^{1}$ , Zhifang Chai  $^{3,4}$ , Jintian Lin  $^{1}$  and Ya Cheng  $^{1,3,4,5,*}$

$^{1}$  State Key Laboratory of High Field Laser Physics, Shanghai Institute of Optics and Fine Mechanics, Chinese Academy of Sciences, Shanghai 201800, China; rbwu@siom.ac.cn (R.W.); qijia@siom.ac.cn (J.Q.); chuwei@siom.ac.cn (W.C.); jhzhang@siom.ac.cn (J.Z.); qiaolingling@siom.ac.cn (L.Q.); jintianlin@siom.ac.cn (J.L.)  
2 University of Chinese Academy of Sciences, Beijing 100049, China  
3 State Key Laboratory of Precision Spectroscopy, East China Normal University, Shanghai 200062, China; mwang@phy.ecnu.edu.cn (M.W.); jxu@phy.ecnu.edu.cn (J.X.); zwfang@phy.ecnu.edu.cn (Z.F.); 52180920026@stu.ecnu.edu.cn (J.Z.); zfchai@phy.ecnu.edu.cn (Z.C.)  
4 XXL—The Extreme Optoelectromechanics Laboratory, School of Physics and Materials Science, East China Normal University, Shanghai 200241, China  
5 Collaborative Innovation Center of Extreme Optics, Shanxi University, Taiyuan 030006, Shanxi, China  
* Correspondence: ya.cheng@siom.ac.cn  
These authors contributed equally to this paper.

Received: 5 October 2018; Accepted: 2 November 2018; Published: 6 November 2018

![](images/b3e1e3cfa9138dc5f66661636ae9577d4d157d1ac51c331b12f20d6fe889e1bc.jpg)

check for updates

Abstract: In this paper, we develop a technique for realizing multi-centimeter-long lithium niobate on insulator (LNOI) waveguides with a propagation loss as low as  $0.027\mathrm{dB / cm}$ . Our technique relies on patterning a chromium thin film coated on the top surface of LNOI into a hard mask with a femtosecond laser followed by chemo-mechanical polishing for structuring the LNOI into the waveguides. The surface roughness on the waveguides was determined with an atomic force microscope to be  $0.452\mathrm{nm}$ . The approach is compatible with other surface patterning technologies, such as optical and electron beam lithographies or laser direct writing, enabling high-throughput manufacturing of large-scale LNOI-based photonic integrated circuits.

Keywords: lithium niobate; waveguide; photonic integrated circuit; propagation loss; optical lithography; chemo-mechanical polishing

# 1. Introduction

Photonic integrated circuits (PICs) have shown the potential for use in complex information processing systems employing both quantum and classical light sources [1,2]. To increase computational efficiency and reconfigurability, PIC-based optical computers/calculators must have low propagation loss, fast tunability, and efficient optical interfacing. Currently, several materials have been utilized to construct large-scale PICs, including silicon and some semiconductor materials [3-6], fused silica [7,8], and bulk lithium niobate (LN) [9,10]. The advantage of silicon-based PICs is the high refractive index of silicon that enables the fabrication of compact light circuits with strong confinement and tight bends. In addition, the lithographic technology for high precision patterning of silicon and semiconductors is mature. However, silicon-based PICs intrinsically suffer from a relatively high propagation loss and a transmission window prohibitive for visible and shorter wavelengths. PICs can be built on fused silica and bulk LN crystals by local modification of the refractive index via either illumination of light or ion doping. Unfortunately, the refractive index increases achieved using these approaches are

usually in the order of  $10^{-3}$  to  $10^{-2}$ , resulting in large PICs footprints being required for minimizing the bending loss. Most importantly, the typical propagation losses of waveguides in state-of-the-art PICs are typically in the order of  $10^{-1}$  dB/cm or higher, which ultimately limits the performance of PIC-based optical computers.

A revolutionary approach for building high-performance PICs has been emerging, enabled by the successful application of high quality lithium niobate on insulator (LNOI) nanophotonic structures. The first experimental proof of this approach was provided by first patterning the LNOI into the designated geometries using a femtosecond laser. The draft structures obtained after the femtosecond laser patterning, which has a relatively high sidewall roughness in the order of tens of nanometers, were then polished with a focused ion beam (FIB) milling to smoothen the sidewall [11]. This concept was soon incorporated into other lithographic technologies, such as optical lithography and electron beam writing (EBW), for defining the planar patterns on LNOI substrates followed by reactive ion etching to complete the nanostructuring of the LNOI [12,13]. The initial focus was mainly on optical microresonators [11-21], and other devices (such as waveguides and photonic crystals [22-28]) appeared shortly, taking advantage of the high surface smoothness of the sidewalls as a result of the ion dry etching. So far, the propagation loss in the LNOI waveguides has reached 0.04 dB/cm, highlighting their potential for use in large-scale PIC applications [29].

Notably, the ion etching step, which is necessary for achieving high quality sidewalls on LNOI nanophotonic structures, leaves a low but non-negligible surface roughness that is difficult to completely remove [29]. Moreover, the use of FIB or EBW in the patterning of LNOI makes the approach impractical for fabricating large-scale PICs due to their low throughputs and limited range of motion. Recently, we developed a technique for fabricating high-quality optical microresonators on LNOI with a quality factor above  $10^{7}$  [30]. Since this technique does not involve an ion beam etching process, surface smoothness beyond that allowed by ion beam etching can be readily achieved, and the footprint sizes of PICs can be increased by patterning the LNOI photonic structures with either laser direct writing or optical lithography. Here, we experimentally show that we are able to realize 10-cm-long LNOI waveguides with a propagation loss of  $0.027\mathrm{dB / cm}$ , which benefited from the low surface roughness of  $0.452\mathrm{nm}$  measured with an atomic force microscope (AFM). The low loss waveguides can be essential building blocks for light modulation, beam delivery and manipulation, nonlinear optics, and optical signal processing.

# 2. Materials and Methods

A commercially available X-cut LNOI wafer fabricated by ion slicing (NANOLN, Jinan Jingzheng Electronics Co., Ltd., Jinan, Shandong, China) was chosen in our experiment as the material upon which the LNOI waveguides were produced [31]. The LN thin film had a thickness of  $400\mathrm{nm}$  and was bonded to a  $\mathrm{SiO}_2$  layer  $2 - \mu \mathrm{m}$ -thick, which was grown on a LN substrate. The fabrication procedures are schematically illustrated in Figure 1, including (1) deposition of a thin layer of chromium (Cr) with a thickness of  $600\mathrm{nm}$  on LNOI by magnetron sputtering and (2) patterning of the Cr film using femtosecond laser ablation. It is critical to carefully choose the pulse energy of the femtosecond laser to ensure the complete removal of the Cr film without damaging the LNOI underneath, which is enabled by the unique characteristics of the interaction of femtosecond laser pulses with various types of materials [32]. More details on the laser parameters can be found in Wu, R., et al. [30] To produce a tightly focused spot  $\sim 1\mu \mathrm{m}$  in diameter, a  $100\times$  objective lens (M Plan Apo NIR, Mitutoyo Corporation, Kawasaki, Kanagawa, Japan) with a numerical aperture (NA) of 0.7 was used in our experiment. Femtosecond laser direct writing was conducted by translating the LNOI sample with a computer-controlled XY motion stage (ABL15020WB and ABL15020, Aerotech Inc., Pittsburgh, PA, USA, translation resolution  $\sim 100\mathrm{nm}$ ). The focus of the laser beam was controlled in the Z direction using another one-dimensional stage with a translation resolution of  $100\mathrm{nm}$  (ANT130-110-L-ZS, Aerotech Inc., Pittsburgh, PA, USA) on which the objective lens was installed. A charged coupled device (CCD) was installed above the objective lens for monitoring the fabrication

process. The laser power was chosen to ensure the complete removal of the Cr thin film while keeping the LNOI underneath the Cr film intact. The patterned Cr disk served as a hard mask in the subsequent CM polishing.

![](images/4f9ff29b9df8c841544dc5af56768ab42cadc584620aa9ea3e3ed5a2f5af8f49.jpg)

![](images/1dbfce2ea71406e4dccb80d5904e7fe88425d6a2edd1806195d9e9cdfa5762a2.jpg)

![](images/36cbf1c50936351319252732e52c1a76221c572efe513eea6d28a6e46a2758e3.jpg)

![](images/b48a6775dadf4906b811c59872204e99bc9a914f582f5995972e49fb0bcd1320.jpg)

![](images/aa1524807bd96e767520b93cbda0bb34841ebe6fc5335f15ffe781db9f0c2ced.jpg)

![](images/6ed7a244d7444aef7473a4d481b064cf2b89caf5e44e4eeef59fe1a23ae7a5cd.jpg)

![](images/4ca9a44642972e4704adbe63acecda384da049a139ffcd4bb876c67331cb073c.jpg)  
Figure 1. (a-d) Flow-chart of fabrication of lithium niobate on insulator (LNOI) waveguide and (e) schematic diagram of chemo-mechanical polishing (CMP).

The CM polishing was carried out using a wafer polishing machine (NUIPOL802, Hefei Kejing Materials Technology Co., Ltd., Hefei, Anhui, China). More details on CM polishing can also be found in Wu, R, et al. [30]. Note that the Cr film has a higher hardness than the LNOI, so LNOI would be completely removed by CM polishing, unless it is protected by a Cr mask. Finally, the Cr mask was removed by immersing the fabricated sample in a Cr etching solution (Chromium etchant, Alfa Aesar GmbH, Haverhill, MA, USA) for  $10\mathrm{min}$ . All the procedures up to this stage were the same as those used for fabricating a high-Q microresonator, as described by Wu, R., et al. [30], For fabricating low-loss waveguides, the sample underwent an additional CM polishing at a relatively low pressure with a shorter polishing duration to improve the smoothness of the upper surface of LN waveguide, as illustrated in Figure 1d.

To characterize the propagation loss in the LNOI waveguide, we constructed a whispering gallery ring resonator through which the propagation loss of the LNOI waveguide was determined using  $\alpha = 2\pi n_{eff} / (Q\lambda)$ , where  $\alpha$  is the attenuation coefficient,  $n_{eff}$  the effective refractive index,  $Q$  the quality factor of the ring resonator, and  $\lambda$  is the wavelength of the light beam. Both  $n_{eff}$  and the  $Q$ -factor were determined from the transmission spectrum of microring resonator. The experimental setup for measuring the  $Q$  factor of the ring resonator is schematically shown in Figure 2. The light produced by a tunable laser (LTB-6728, Newport Corporation, Santa Clara, CA, USA) was coupled to a curved LNOI waveguide whose geometric parameters, including the thickness and width, were the same as that of the LNOI ring, determined with the use of a fiber lens. The exiting light was collected using a  $20\times$  objective lens (MPlanFL N, Olympus Corporation, Tokyo, Japan) into a detector (Model 1811, Newport Corporation, Santa Clara, CA, USA). The bend of the upper waveguide was intentionally introduced for preventing the stray light from the fiber laser from entering the objective lens located in front of the detector. The polarization direction of the light was adjusted with a fiber polarization controller. The curved waveguide was coupled to the LNOI ring resonator via evanescent coupling. Specifically, by carefully adjusting the distance between the coupling waveguide and the microring resonator, we were able to achieve the coupling condition crucial for obtaining an accurate intrinsic  $Q$  factor of the ring resonator. We fabricated five microrings and the measured optical losses were close

to each other (with  $Q$  factors between  $10^{6}$  and  $10^{7}$ ), indicating that the fabrication technique is reliable and reproducible.

![](images/d52a359049ea8166ca660fcb40160d6f28fbecbff8907ef7aad969a778f7b2c4.jpg)  
Figure 2. Schematic of the experimental setup for measuring the  $Q$  factor of the microring resonator. Left inset: Optical micrograph image of the microring resonator coupling with the waveguide, as indicated by the black arrows.

# 3. Results

Figure 3a shows the top-view scanning electron microscope (SEM) images of a LN micro ring resonator with a diameter of  $160~\mu \mathrm{m}$ . The width of the waveguide was  $\sim 3\mu \mathrm{m}$ . The close-up-view SEM of an arc of the ring highlights the high surface smoothness of the CM polished sample. A further atomic force microscope (AFM) inspection, as illustrated in Figure 3c, confirmed that a surface roughness  $Rq$  as low as  $0.452\mathrm{nm}$  was achieved. The same fabrication technique was also used to fabricate a continuous 11-cm-long optical waveguide, as shown by the digital-camera-captured picture in Figure 3d, with details provided in the zoomed optical micrographs in Figure 3e-f. The total time of femtosecond laser ablation for fabricating the 11-cm-long waveguide was  $90\mathrm{min}$ . At this moment, the footprint size of the PICs was only limited by the LNOI wafer size. The LNOI wafer can be made larger without much difficulty [33].

![](images/38f7a37d4c17ca041abe01160599e7eb33af0f64a160dcca0ad3c41ba4c8bbf6.jpg)

![](images/780c23bcc86a4f9f38166366e4e93685a940959991e1e6928f5a109f6526d95a.jpg)

![](images/a763e9de3324ce2bc846bc48007b65bc5b21c26cead167055c47b8bdab69dc41.jpg)

![](images/65c8d8dbe2bc29f0f7539935632a727e6e008e7690039afc81db61aea19955b9.jpg)  
Figure 3. (a) Top-view scanning electron microscope (SEM) image of a lithium niobate (LN) microring resonator; (b) Zoomed view of the ridge of the microring resonator in (a); (c) Atomic force microscope (AFM) image of the ridge; (d) Picture of a chip consisting of an 11-cm-long waveguide captured by digital camera; (e,f) Zoomed images of the waveguides on the chip captured with an optical microscope.

![](images/058adcfdb32fe91111fc348a3a111816496161ddee947ef3f2c270804ed195a3.jpg)

![](images/77748c5f6911f0c9a5aecf5008337081ec0960ea18892b415cba4f1a508277d3.jpg)

The optical loss characterization was performed using whispering-gallery-resonator-loss measurements. The propagation loss  $\alpha$  is related to the  $Q$  factor of the ring resonator. Figure 4a shows the measured transmission spectrum for the wavelength range between 1546 and  $1564\mathrm{nm}$ . The free spectral range (FSR) of the microring resonator was determined to be  $2.71\mathrm{nm}$ , which is consistent with the  $160~{\mu\mathrm{m}}$  diameter of our ring resonator. The resonant lines appeared regularly spaced, indicating that mostly low-order modes exist in the ring resonator. One of the whispering-gallery modes at the resonant wavelength of  $1560.48\mathrm{nm}$  was chosen for the measurement of the loaded  $Q$  factor by fitting with a Lorentz function, which reached  $5.70\times 10^{6}$ , corresponding to an intrinsic  $Q$  factor of  $1.14\times 10^{7}$  in the critical coupling regime as evidenced in Figure 4b. The effective refractive index,  $n_{eff} = \lambda^2 /(2\pi R\cdot FSR)$ , with a ring radius  $R$  of  $80~{\mu\mathrm{m}}$  and wavelength of  $1560.48\mathrm{nm}$ , was calculated to be 1.79, which is in good agreement with our finite-difference time-domain (FDTD) simulation result given in the inset of Figure 4b. Combining the effective refractive index and the  $Q-$  factor obtained from the transmission spectrum, the propagation loss in the microring resonator was calculated to be  $0.027\mathrm{dB / cm}$  using the aforementioned expression  $\alpha = 2\pi n_{eff} / (Q\lambda)$ . This result represents the upper limit of the propagation loss in the LNOI waveguide fabricated using our method.

![](images/f5d9fad019103ebd3560327075c27250f016a48811fd2896f427673f948b1563.jpg)  
(a)  
(b)

![](images/dd93ed0bc10a51db2b8e50c7554834f60dda12cebcfb0755631dbddde2da3614.jpg)  
Figure 4. (a) Transmission spectrum of the LN microring resonator; (b) The Lorentz fitting (red curve) reveals a loaded  $Q$  factor of  $5.70 \times 10^{6}$ , corresponding to an intrinsic  $Q$  factor of  $1.14 \times 10^{7}$ . Inset: The optical mode distribution and  $n_{\mathrm{eff}}$  in the ring waveguide calculated using finite-difference time-domain (FDTD) simulation.

# 4. Discussion

The low propagation loss of  $0.027\mathrm{dB / cm}$  was a result of the low surface roughness  $Rq$  of  $0.452\mathrm{nm}$  on the fabricated LNOI waveguides. The surface roughness was improved using our technique in which the LNOI is purely patterned by the chemo-mechanical polishing without any use of ion beam etching [30]. The ion beam etching inherently leaves a small amount of surface roughness on the nearly vertical sidewalls, which is difficult to completely remove by top surface polishing [34,35]. This is the major reason that we were able to obtain a propagation loss lower than the waveguides fabricated by FIB or reactive ion etching. In the current experiment, we used a femtosecond laser to pattern the Cr hard mask. Generally speaking, the sidewall roughness on the Cr mask patterned by femtosecond laser ablation should be higher than the surface roughness of the LNOI photonic structures produced by ion beam etching. However, the sidewall roughness on the Cr mask only transfers to the underneath LNOI near the top surface, thus it can be completely suppressed with an additional polishing process for thinning the LNOI substrate after the removal of the Cr mask (Figure 1d).

Notably, the propagation loss obtained by measuring the  $Q$  factor of the ring resonator may have been underestimated for the straight segments in the LNOI waveguides, as presented in Figure 3d-f, due to a higher radiative loss in the ring resonator. Ultimately, the propagation loss of the LNOI waveguides is limited by the absorption in crystalline LN, which is well known to be in the order of  $\sim 10^{-3}\mathrm{dB / cm}$ . Our measured loss was still one order of magnitude away from the theoretical limit, which could be attributed to several factors, including the radiative loss in the ring resonator and some

unknown contamination on the surface of the LNOI waveguide, as the measurements were all carried out in a low-class clean room, existence of absorptive defects in the LNOI substrate owing to the imperfect crystal growth, and the remaining surface roughness left by the chemo-mechanical polishing process. Thus, to realize LNOI waveguides with propagation losses in the order of  $1 \times 10^{-3} \mathrm{~dB/cm}$ , many refinements should be systematically investigated in the future.

The fabrication resolution of femtosecond laser direct writing is typically in the order of  $1\mu \mathrm{m}$  for inorganic materials such as glass, semiconductors, and metals. However, today's optical lithography can easily achieve sub-micron or even 100-nm-level patterning resolutions. This should be sufficient for fabricating single-mode LNOI waveguides of narrower widths by which PICs, such as Mach-Zender interferometers and polarization convertors, can be built. The mode field of the LNOI waveguides can be tuned by coating them with fused silica for suppressing higher order modes as well as scattering loss due to the reduced contrast of the refractive index between the LNOI waveguide and the cladding environment [36]. With these improvements, the LNOI waveguides will become a major building block for PIC applications.

# 5. Conclusions

In this study, we achieved a propagation loss of  $0.027\mathrm{dB / cm}$  in LNOI waveguides fabricated by combining femtosecond laser micromachining for patterning the Cr mask and chemo-mechanical polishing for transferring the laser-written patterns to the LNOI beneath the Cr mask. By eliminating the low-throughput FIB or EBW process, our technique enables the rapid fabrication of longer low-loss optical waveguides, which are only limited by the range of motion of the air bearing stage and the size of the LNOI wafers. Thus, our approach promotes the fabrication efficiency and reduces the cost of manufacturing LNOI PICs. The waveguides and ring resonators can be adopted for constructing complex PICs, enabling the mass production of LNOI PICs for optical communication and computation applications.

Author Contributions: Conceptualization, Y.C.; methodology, Y.C.; software, R.W.; validation, R.W. and M.W.; formal analysis, R.W.; investigation, R.W., M.W., J.Q. and J.X.; resources, R.W., M.W., W.C., Z.F., J.Z. (Jianhao Zhang), J.Z. (Junxia Zhou), L.Q., Z.C. and J.L.; data curation, R.W. and M.W.; writing—original draft preparation, Y.C. and R.W.; writing—review and editing, Y.C., R.W., M.W., J.L. and J.X.; visualization, R.W., J.Q., J.X. and M.W.; supervision, Y.C.; project administration, L.Q. and Z.C.; funding acquisition, Y.C., J.L. and J.X.

Funding: This research was funded by the National Natural Science Foundation of China (Grant Nos. 11734009, 11874375, 61590934, 61635009, 61327902, 61505231, 11604351, 11674340, 61575211, 61675220, 61761136006), the Strategic Priority Research Program of Chinese Academy of Sciences (Grant No. XDB16000000), the Key Research Program of Frontier Sciences, Chinese Academy of Sciences (Grant No. QYZDJ-SSW-SLH010), the Project of Shanghai Committee of Science and Technology (Grant No. 17JC1400400), the Shanghai Rising-Star Program (Grant No. 17QA1404600), and the Shanghai Pujiang Program (Grant No.18PJ1403300).

Conflicts of Interest: The authors declare no conflict of interest.

# References

1. Ladd, T.D.; Jelezko, F.; Laflamme, R.; Nakamura, Y.; Monroe, C.; O'Brien, J.L. Quantum computers. Nature 2010, 464, 45-53. [CrossRef] [PubMed]  
2. Shen, Y.; Harris, N.C.; Skirlo, S.; Prabhu, M.; Baehr-Jones, T.; Hochberg, M.; Sun, X.; Zhao, S.; Larochelle, H.; Englund, D.; et al. Deep learning with coherent nanophotonic circuits. Nat. Photonics 2017, 11, 441. [CrossRef]  
3. Harris Nicholas, C.; Bunandar, D.; Pant, M.; Steinbrecher Greg, R.; Mower, J.; Prabhu, M.; Baehr-Jones, T.; Hochberg, M.; Englund, D. Large-scale quantum photonic circuits in silicon. *Nacnophotonics* 2016, 5, 456-468. [CrossRef]  
4. Dietrich, C.P.; Fiore, A.; Thompson, M.G.; Kamp, M.; Hofling, S. GaAs integrated quantum photonics: Towards compact and multi-functional quantum photonic integrated circuits. *Laser Photonics Rev.* 2016, 10, 870-894. [CrossRef]

5. Najafi, F.; Mower, J.; Harris, N.C.; Bellei, F.; Dane, A.; Lee, C.; Hu, X.; Kharel, P.; Marsili, F.; Assefa, S.; et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 2015, 6, 5873. [CrossRef] [PubMed]  
6. Yang, K.Y.; Oh, D.Y.; Lee, S.H.; Yang, Q.-F.; Yi, X.; Shen, B.; Wang, H.; Vahala, K. Bridging ultrahigh-Q devices and photonic circuits. Nat. Photonics 2018, 12, 297-302. [CrossRef]  
7. Qiang, X.; Zhou, X.; Wang, J.; Wilkes, C.M.; Loke, T.; O'Gara, S.; Kling, L.; Marshall, G.D.; Santagati, R.; Ralph, T.C.; et al. Large-scale silicon quantum photonics implementing arbitrary two-qubit processing. Nat. Photonics 2018, 12, 534-539. [CrossRef]  
8. Marshall, G.D.; Politi, A.; Matthews, J.C.F.; Dekker, P.; Ams, M.; Withford, M.J.; O'Brien, J.L. Laser written waveguide photonic quantum circuits. Opt. Express 2009, 17, 12546-12554. [CrossRef] [PubMed]  
9. Sohler, W.; Hu, H.; Ricken, R.; Quiring, V.; Vannahme, C.; Herrmann, H.; Buchter, D.; Reza, S.; Grundkotter, W.; Orlov, S.; et al. Integrated optical devices in lithium niobate. Opt. Photonics News 2008, 19, 24-31. [CrossRef]  
10. Jin, H.; Liu, F.M.; Xu, P.; Xia, J.L.; Zhong, M.L.; Yuan, Y.; Zhou, J.W.; Gong, Y.X.; Wang, W.; Zhu, S.N. On-chip generation and manipulation of entangled photons based on reconfigurable lithium-niobate waveguide circuits. Phys. Rev. Lett. 2014, 113, 103601. [CrossRef] [PubMed]  
11. Lin, J.; Xu, Y.; Fang, Z.; Song, J.; Wang, N.; Qiao, L.; Fang, W.; Cheng, Y. Second harmonic generation in a high-Q lithium niobate microresonator fabricated by femtosecond laser micromachining. arXiv, 2014; arXiv:1405.6473.  
12. Wang, J.; Bo, F.; Wan, S.; Li, W.; Gao, F.; Li, J.; Zhang, G.; Xu, J. High-Q lithium niobate microdisk resonators on a chip for efficient electro-optic modulation. Opt. Express 2015, 23, 23072-23078. [CrossRef] [PubMed]  
13. Wang, C.; Burek, M.J.; Lin, Z.; Atikian, H.A.; Venkataraman, V.; Huang, I.-C.; Stark, P.; Loncar, M. Integrated high quality factor lithium niobate microdisk resonators. Opt. Express 2014, 22, 30924-30933. [CrossRef] [PubMed]  
14. Lin, J.; Xu, Y.; Fang, Z.; Wang, M.; Song, J.; Wang, N.; Qiao, L.; Fang, W.; Cheng, Y. Fabrication of high-Q lithium niobate microresonators using femtosecond laser micromachining. Sci. Rep. 2015, 5, 8072. [CrossRef] [PubMed]  
15. Lin, J.; Xu, Y.; Ni, J.; Wang, M.; Fang, Z.; Qiao, L.; Fang, W.; Cheng, Y. Phase-matched second-harmonic generation in an on-chip  $\mathrm{LiNbO}_3$  microresonator. Phys. Rev. Appl. 2016, 6, 014002. [CrossRef]  
16. Lin, J.; Xu, Y.; Fang, Z.; Wang, M.; Wang, N.; Qiao, L.; Fang, W.; Cheng, Y. Second harmonic generation in a high-Q lithium niobate microresonator fabricated by femtosecond laser micromachining. Sci. China Phys. Mech. Astron. 2015, 58, 114209. [CrossRef]  
17. Hao, Z.; Wang, J.; Ma, S.; Mao, W.; Bo, F.; Gao, F.; Zhang, G.; Xu, J. Sum-frequency generation in on-chip lithium niobate microdisk resonators. Photonics Res. 2017, 5, 623-628. [CrossRef]  
18. Wang, L.; Wang, C.; Wang, J.; Bo, F.; Zhang, M.; Gong, Q.; Lončar, M.; Xiao, Y.-F. High-Q chaotic lithium niobate microdisk cavity. Opt. Lett. 2018, 43, 2917-2920. [CrossRef] [PubMed]  
19. Luo, R.; Jiang, H.; Rogers, S.; Liang, H.; He, Y.; Lin, Q. On-chip second-harmonic generation and broadband parametric down-conversion in a lithium niobate microresonator. Opt. Express 2017, 25, 24531-24539. [CrossRef] [PubMed]  
20. Jiang, W.C.; Lin, Q. Chip-scale cavity optomechanics in lithium niobate. Sci. Rep. 2016, 6, 36920. [CrossRef] [PubMed]  
21. Fang, Z.; Xu, Y.; Wang, M.; Qiao, L.; Lin, J.; Fang, W.; Cheng, Y. Monolithic integration of a lithium niobate microresonator with a free-standing waveguide using femtosecond laser assisted ion beam writing. Sci. Rep. 2017, 7, 45610. [CrossRef] [PubMed]  
22. Liang, H.; Luo, R.; He, Y.; Jiang, H.; Lin, Q. High-quality lithium niobate photonic crystal nanocavities. Optica 2017, 4, 1251-1258. [CrossRef]  
23. Wang, C.; Zhang, M.; Stern, B.; Lipson, M.; Lončar, M. Nanophotonic lithium niobate electro-optic modulators. Opt. Express 2018, 26, 1547-1555. [CrossRef] [PubMed]  
24. Wang, C.; Xiong, X.; Andrade, N.; Venkataraman, V.; Ren, X.-F.; Guo, G.-C.; Loncar, M. Second harmonic generation in nano-structured thin-film lithium niobate waveguides. Opt. Express 2017, 25, 6963-6973. [CrossRef] [PubMed]  
25. Luo, R.; He, Y.; Liang, H.; Li, M.; Lin, Q. Highly tunable efficient second-harmonic generation in a lithium niobate nanophotonic waveguide. Optica 2018, 5, 1006-1011. [CrossRef]

26. Cai, L.; Han, H.; Zhang, S.; Hu, H.; Wang, K. Photonic crystal slab fabricated on the platform of lithium niobate-on-insulator. Opt. Lett. 2014, 39, 2094-2096. [CrossRef] [PubMed]  
27. Diziain, S.; Geiss, R.; Steinert, M.; Schmidt, C.; Chang, W.-K.; Fasold, S.; Füssel, D.; Chen, Y.-H.; Pertsch, T. Self-suspended micro-resonators patterned in Z-cut lithium niobate membranes. Opt. Mater. Express 2015, 5, 2081-2089. [CrossRef]  
28. Krasnokutska, I.; Tambasco, J.-L.J.; Li, X.; Peruzzo, A. Ultra-low loss photonic circuits in lithium niobate on insulator. Opt. Express 2018, 26, 897-904. [CrossRef] [PubMed]  
29. Wolf, R.; Breunig, I.; Zappe, H.; Buse, K. Scattering-loss reduction of ridge waveguides by sidewall polishing. Opt. Express 2018, 26, 19815-19820. [CrossRef] [PubMed]  
30. Wu, R.; Zhang, J.; Yao, N.; Fang, W.; Qiao, L.; Chai, Z.; Lin, J.; Cheng, Y. Lithium niobate micro-disk resonators of quality factors above  $10^{7}$ . Opt. Lett. 2018, 43, 4116-4119. [CrossRef] [PubMed]  
31. Poberaj, G.; Hu, H.; Sohler, W.; Guenter, P. Lithium niobate on insulator (LNOI) for micro-photonics devices. *Laser Photonics Rev.* **2012**, 6, 488–503. [CrossRef]  
32. Sugioka, K.; Cheng, Y. Ultrafast lasers—Reliable tools for advanced materials processing. Light Sci. Appl. 2014, 3, e149. [CrossRef]  
33. Boes, A.; Corcoran, B.; Chang, L.; Bowers, J.; Mitchell, A. Status and potential of lithium niobate on insulator (LNOI) for photonic integrated circuits. *Laser Photonics Rev.* **2018**, 12, 1700256. [CrossRef]  
34. Wolf, R.; Breunig, I.; Zappe, H.; Buse, K. Cascaded second-order optical nonlinearities in on-chip micro rings. Opt. Express 2017, 25, 29927-29933. [CrossRef] [PubMed]  
35. Wolf, R.; Breunig, I.; Zappe, H.; Buse, K. Q-factor enhancement of integrated lithium-niobate-on-insulator ridge waveguide whispering-gallery-mode resonators by surface polishing. In Proceedings of the Laser Resonators, Microresonators, and Beam Control XIX, San Francisco, CA, USA, 20 February 2017; p. 1009002. [CrossRef]  
36. Guarino1, A.; Poberaj, G.; Rezzonico, D.; Degl'Innocenti, R.; Gunter, P. Electro-optically tunable microring resonators in lithium niobate. Nat. Photonics 2007, 1, 407-410. [CrossRef]

![](images/9c67208d33c272daee3694e416e314f98dd2cb48b294e22e71fba95c3a683dd8.jpg)

© 2018 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/).