LETTER | MAY 24 2022

# High-performance silicon photonic filters based on all-passive tenth-order adiabatic elliptical-microrings

Dajian Liu  $①$  ; Jianghao He; Yuluan Xiang; Yang Xu  $①$  ; Daoxin Dai  $①$

![](images/eff61b3d4e0a5f695d01a3fc364e4294e6b650e4d660293497b6aab868f0cbc0.jpg)

Check for updates

APL Photonics 7, 051303 (2022)

https://doi.org/10.1063/5.0085332

![](images/5246b59db65a00c8c7c4618ea4276d0ed1a0db33575a8b319fd4570e08900073.jpg)  
View Online

![](images/fca5e5a6774ebdeb69d5986f69df6dbb2c9ae81f84a322b881719eb877ce5cbc.jpg)  
Export Citation

# Articles You May Be Interested In

High-bandwidth  $\mathrm{Si} / \mathrm{In}_2\mathrm{O}_3$  hybrid plasmonic waveguide modulator

APL Photonics (May 2022)

Polymer microring resonators fabricated by nanoimprint technique

J. Vac. Sci. Technol. B (December 2002)

All optically tunable wavelength-selective reflector consisting of coupled polymeric microring resonators

Appl. Phys. Lett. (December 2005)

![](images/229a2a92476e57baaa1d31eed8b4d4a3eb16c0380ce7b16170b47a5c9efb8126.jpg)

THE MATERIALS SCIENCE MANUFACTURER

# Now Invent.

![](images/f736374d4b2974a7465304f00b0f5f875e1c8521a864f219458431b68f821040.jpg)

![](images/3ba7a2633110023c613e13e2601de2d91d04336547996c9574a5f3b49619abb9.jpg)

![](images/b9f5a7d0b8decd178b88feef9cb4eafad02b1f19ebc4c69a6d623e8e5810d8e3.jpg)

![](images/b7022b6ccdaabb6659799b158d52810af89edf41f897128644acd932e690d198.jpg)

# High-performance silicon photonic filters based on all-passive tenth-order adiabatic elliptical-microrings

Cite as: APL Photon. 7, 051303 (2022); doi: 10.1063/5.0085332

Submitted: 15 January 2022 · Accepted: 5 May 2022

Published Online: 24 May 2022

![](images/b71f3bbd6bc31d5277383efcfce7bc0229f1bfbeef922f95a559f5ffae6ea810.jpg)  
View Online

![](images/2333a626adae6f8849d04977cf9e8218e015b666108bcf993ce8eb51ef5c2a58.jpg)  
Export Citation

![](images/8bda15148322b26ee297a64640ecfa0a479c9a8830a182114fbe8875578478a2.jpg)  
CrossMark

Dajian Liu, $^{1,2}$  Jianghao He, $^{1}$  Yuluan Xiang, $^{1}$  Yang Xu, $^{2}$  and Daoxin Dai $^{1,3,a)}$

# AFFILIATIONS

$^{1}$ State Key Laboratory for Modern Optical Instrumentation, Centre for Optical and Electromagnetic Research, College of Optical Science and Engineering, International Research Center for Advanced Photonics, Zhejiang University, Zijingang Campus, Hangzhou 310058, China  
$^{2}$ ZJU-Hangzhou Global Scientific and Technological Innovation Center, Hangzhou 311200, China  
$^{3}$ Ningbo Research Institute, Zhejiang University, Ningbo 315100, China

$^{a)}$ Author to whom correspondence should be addressed: dxdai@zju.edu.cn

# ABSTRACT

Ultra-compact silicon photonic filters with box-like responses and high extinction ratios are proposed and demonstrated by introducing tenth-order adiabatic elliptical-microrings (AEMs) with bent directional couplers. For the AEMs, the waveguides in the non-coupling regions are wide and have a minimal bending radius, while the waveguides in the coupling regions are narrowed and have a maximal bending radius. The present silicon photonic filters based on tenth-order AEMs show a free spectral range as large as  $37~\mathrm{nm}$  for the first time. Even fabricated with commercial complementary metal-oxide-semiconductor-compatible  $248~\mathrm{nm}$  deep-ultraviolet lithography processes, the present devices show high performances with excess losses as low as  $\sim 1$  dB and extinction ratios as high as  $>60$  dB. More importantly, the present silicon photonic filters work very well all-passively without any thermal control for calibration.

© 2022 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution (CC BY) license (http://creativecommons.org/licenses/by/4.0/). https://doi.org/10.1063/5.0085332

Benefiting from the complementary metal-oxide-semiconductor (CMOS) infrastructure enabling the fabrication of photonic integrated circuits on the silicon-on-insulator (SOI) platform, silicon photonics is gradually expanding to many emerging applications, such as optical interconnection, nonlinear optics, LiDAR, and quantum integrated optics. Silicon photonic filters are often used for spectrum manipulation in various optical systems and have attracted intensive attention as one of the main functional devices of integrated photonics. It becomes very critical to develop compact high-performance optical filters with a low excess loss, a high extinction ratio (ER), and a box-like response. For example, a high-ER optical filter can be used potentially for pump removing in silicon quantum photonics.

Currently, various photonic filters have been demonstrated successfully by using Mach-Zehnder interferometers (MZIs), Bragg

gratings, and microring resonators (MRRs) as well as their cascaded structures. $^{5,6,8-26}$  Among them, high-order MRRs $^{10-26}$  have been one of the most attractive options due to their footprint compactness and functional versatility. However, for high-order MRRs based on silicon photonic waveguides with an ultra-high refractive index contrast, a big challenge is the high sensitivity of the effective index to random nanometer-scale dimensional variation introduced by the fabrication imperfection, which introduces significant resonance wavelength misalignment for the MRRs. To overcome this drawback, the introduction of individual thermal-tuning for all microring elements is one of the most common methods for wavelength alignment. $^{14-20}$  Unfortunately, this greatly increases device power consumption, the device size, as well as circuit complexity. Another approach is to introduce more advanced processing and manufacturing technology, such as using  $193~\mathrm{nm}$  ArF-immersion lithography. $^{12}$  However, this increases the fabrication cost, and

currently, most silicon photonic foundries do not have such advanced equipment yet.

In this Letter, we demonstrate a high-performance silicon photonic filter by using tenth-order adiabatic elliptical-microrings (AEMs) with a free spectral range (FSR) as large as  $37~\mathrm{nm}$  for the first time. For these AEMs, both the radius and the width of the ring waveguide are varied adiabatically, which can provide not only a sufficient coupling as desired but also a compact size with low propagation loss. Previously, we realized excellent silicon photonic filters based on second-, third-, and fourth-order AEMs by using E-beam lithography processes.[21] Generally, when the cascaded rings have a higher order, one has a more box-like spectral response with higher ERs and higher roll-off rates, as shown in Fig. 1. On the other hand, the performance does not improve notably when further increasing the order from 10 to even more. Therefore, in this Letter, we focus on the silicon photonic filters based on tenth-order AEMs. In this case, the wavelength alignment for these ten AEMs in cascade is very critical. Remarkably, the present tenth-order AEM photonic filters on silicon are realized successfully with high performances by using low-cost standard foundry processes. For the realized AEM photonic filters, the measured ER is as high as  $\sim 60$  dB, while the size of a single AEM is as compact as  $5.6\times 4.6\mu \mathrm{m}^2$ , enabling a very large FSR of  $37~\mathrm{nm}$ , which is the largest one among those tenth-order MRRs reported to date. Since the present AEM is the most compact one among the reported high-order MRRs to the best of our knowledge, the footprint compactness greatly helps minimize the random variation of the resonance wavelengths of these AEMs. In addition, the widened waveguide and the relatively large gap for the AEMs ensure the fabrication robustness. Benefiting from the advantages of CMOS compatibility in fabrication and integration, it has great potential for on-chip high-ER photonic filtering applications.

Figure 2(a) shows a three-dimensional (3D) view of the present tenth-order AEM photonic filter. Here, both the radius and the width of the ring waveguide for the AEMs are varied adiabatically. The waveguides in the non-coupling regions are widened and have a minimized bending radius. The wider waveguide improves the tolerance of the ring because the effective index is less sensitive to the width variation. Furthermore, bent directional couplers (DCs) are introduced to help strengthen the coupling between the access waveguide and the adjacent AEM even when choosing a relatively large gap width according to the requirements of the fabrication processes. In addition, the waveguides in the coupling regions are relatively narrow and have a maximal bending radius. As a result,

![](images/8753072e06d31df9056c99f41068dd584e5efcda87b4890807ed35cb64a9fdef.jpg)  
FIG. 1. Calculated spectral responses with different orders.

![](images/630c3f01584f650045a9c3c9a95ebc9bb77a1b4bce075b42656b6ef6be85d196.jpg)

![](images/2642f6464b3fe9dffc39bee0b764d7f04a659216d7958e2acb730b81e6e194fe.jpg)  
FIG. 2. Schematic configurations of the present silicon photonic filter by using tenth-order AEMs. (a) 3D view. (b) Partial view and main parameters.

the gaps in the coupling regions can be relatively large, which helps ensure the full filling of the silica upper-cladding. With the introduction of AEMs and bent coupling structures, one can achieve very compact resonators with low excess losses and sufficient coupling even when ten AEMs are cascaded. This helps minimize the phase error due to the fabrication imperfection, and thus, one might not need to tune and calibrate all the resonators individually, which greatly reduces the structural complexity and footprints.

As an example, here, silicon-on-insulator (SOI) waveguides with a  $220\mathrm{nm}$  thick top-silicon layer and a  $2\mu \mathrm{m}$  thick oxide buffer layer are chosen. The operation wavelength is around  $1550~\mathrm{nm}$ , and the corresponding refractive indices of silicon and silica are  $n_{\mathrm{Si}} = 3.476$  and  $n_{\mathrm{SiO2}} = 1.455$ , respectively. The devices were designed for transverse-electric (TE) polarization. The design of the AEMs is mainly determined by the half lengths  $(L_{\mathrm{a}}$  and  $L_{\mathrm{b}})$  and the widths  $(w_{\mathrm{a}}$  and  $w_{\mathrm{b}})$  at the major/minor axes, as shown in Fig. 2(b). Here, we choose  $(L_{\mathrm{a}}, L_{\mathrm{b}}) = (2.8, 2.3)\mu \mathrm{m}$  and  $(w_{\mathrm{a}}, w_{\mathrm{b}}) = (0.4, 0.65)\mu \mathrm{m}$  according to the design rules in our previous work.[21] More details for the design of a single AEM can be found in our previous work.[21] To implement a box-like response at the drop port, the power coupling coefficients of all the 11 couplers are chosen as  $\kappa_{1} = \kappa_{11} = 0.25$ ,  $\kappa_{2} = \kappa_{10} = 0.046$ ,  $\kappa_{3} = \kappa_{9} = 0.025$ ,  $\kappa_{4} = \kappa_{8} = 0.025$ ,  $\kappa_{5} = \kappa_{7} = 0.025$ , and  $\kappa_{6} = 0.022$ , respectively, where  $\kappa_{i}$  is the power coupling ratios of the ith coupler of the tenth-order AEM. According to the simulation results of the bent DC and inter-AEM couplers, we choose the geometrical parameters as follows: The width of the access waveguide is  $w_{\mathrm{access}} = 0.36\mu \mathrm{m}$ , the coupling angle is  $\alpha = 80^{\circ}$ , and the widths of the minimal gap between two waveguides in the coupling region are chosen as  $w_{\mathrm{gap1}} = w_{\mathrm{gap11}} = 0.18\mu \mathrm{m}$ ,  $w_{\mathrm{gap2}} = w_{\mathrm{gap10}} = 0.185\mu \mathrm{m}$ ,  $w_{\mathrm{gap3}} = w_{\mathrm{gap9}} = 0.23\mu \mathrm{m}$ ,  $w_{\mathrm{gap4}} = w_{\mathrm{gap8}} = 0.23\mu \mathrm{m}$ ,  $w_{\mathrm{gap5}} = w_{\mathrm{gap7}} = 0.23\mu \mathrm{m}$ , and  $w_{\mathrm{gap6}} = 0.24\mu \mathrm{m}$ .

Figure 3(a) shows the calculated transmission response of the tenth-order AEM designed with these power coupling coefficients by using the transfer matrix method (TMM). From Fig. 3(a), it can

![](images/9da08f984d6478b6106c16919881aae1d50dc20d5ba68f9164791c7c907c5b8c.jpg)  
FIG. 3. (a) Calculated spectral responses of the tenth-order AEM filter by using TMM. (b) Calculated spectral responses for the tenth-order AEM filter when there is a variation  $\Delta w$ . Calculated coupling ratios of (c) the bent DC and (d) the inter-AEM coupler when there is a variation  $\Delta w$ ; here, the variation is assumed to be  $\Delta w = \pm 20$  and  $\pm 40$  nm.

![](images/5cb895df8e97f9a1d68426b47053e95a0794379bfec51cf3a5b78559bc443f53.jpg)

![](images/e05722d454044b1c4a55148595fcc84841d0b557ae5f43ac20f4f96318e9f09a.jpg)

be seen that the designed tenth-order AEM has a box-like response with an ultra-high ER of over 200 dB and an FSR as large as  $37~\mathrm{nm}$ . The excess loss of the designed tenth-order AEMs is about  $0.5\mathrm{dB}$  and the  $3\mathrm{dB}$  bandwidth is about  $3\mathrm{nm}$  around the central wavelength of  $1550~\mathrm{nm}$ , as shown by the red line in Fig. 3(b). While the ER for through port is about  $10\mathrm{dB}$  due to some ripples, which was observed in those high-order MRRs reported previously.[18,19,22] Here, we pay more attention to the spectral response at the drop port, which is the key when the device works as a passband filter for many applications. To give an analysis for the fabrication tolerance, we calculate the power coupling ratios of all the coupling regions by assuming the core width has some deviation of  $\Delta w = \pm 20\mathrm{nm}$  and  $\Delta w = \pm 40\mathrm{nm}$  as shown in Figs. 3(c) and 3(d), respectively. It can be seen that the power coupling ratios for the bent DC and inter-AEM couplers increase when the waveguide becomes narrowed because the narrower waveguide provides weaker mode confinement. For example, when the width of the waveguide is narrowed by  $-20\mathrm{nm}$ , the coupling ratio of the bent DC varies from 0.24 to 0.38, while the coupling ratio for the inter-AEM coupler (i.e., the second and tenth couplers) varies from 0.046 to 0.05. Accordingly, Fig. 3(b) shows the calculated spectral response for the tenth-order AEM by using TMM. It can be seen that a box-like response can be obtained even when  $\Delta w = -20$  and  $-40\mathrm{nm}$ , while the  $3\mathrm{dB}$  bandwidth is widened slightly by 0.3 and  $0.8\mathrm{nm}$ , respectively. On the other hand, for the cases of  $\Delta w = +20$  and  $+40\mathrm{nm}$ , the bandwidth of the tenth-order AEM filter does not change notably, while there are some ripples at the top of the response.

To further verify the spectral response of the designed tenth-order AEM, a 2.5-dimensional variational finite-difference time-domain (FDTD) method was performed, as shown in Fig. 4(a). From

this figure, it can be seen that the designed tenth-order AEM has a box-like response with a high ER of  $\sim 80$  dB (limited by the calculation precision). The excess loss is about 1 dB and the 3 dB bandwidth is  $\sim 3$  nm, which agrees well with the result from the TMM calculation. Figure 4(b) shows the simulated light propagation in the tenth-order AEM when operating at the resonance wavelength of  $1539~\mathrm{nm}$ . It shows that there is no multimode interference observed, indicating that the designed AEM works well with the  $\mathrm{TE_0}$  mode. In addition, we also analyze the fabrication tolerance of the designed AEM by assuming the core width has some variation of  $\Delta w = \pm 20$  and  $\pm 40$  nm by using 2.5 D FDTD, as shown in Fig. 4(c). It shows that a box-like response can be obtained with an ER of  $>60$  dB even when  $\Delta w = \pm 40$  nm. Some ripples are observed at the top of the spectrum, which also agrees well with the calculated results from the TMM method.

The designed tenth-order AEM filters were then fabricated through a CMOS-compatible  $248~\mathrm{nm}$  deep-ultraviolet lithography foundry process (instead of using E-beam lithography) by the commercial MPW (Multi-Project Wafer) from CUMEC (China United Microelectronics Center). Figures 5(a)-5(c) show the microscope images of the fabricated devices. In the experiment, we also fabricated the tenth-order AEMs with  $\Delta w = 0$  and  $\pm 20~\mathrm{nm}$ , which can verify the robustness of the present tenth-order AEM filter, as shown in Fig. 5(a). Here, grating couplers [see Fig. 5(c)] were used for convenient and efficient chip-fiber coupling. Broadband amplified spontaneous emission (ASE) light source and an optical spectrum analyzer (OSA) were used to characterize the fabricated devices. Straight waveguides are also used as the reference for normalization.

Figure 6 shows the measured spectral responses at the drop port for the tenth-order AEM filters. The excess losses for all filters are

![](images/14e177da64732cecfac3793aad30e552fbd15333190ee1535ff8bedab792d4d0.jpg)  
FIG. 4. (a) Calculated spectral response of the designed tenth-order AEM filter. (b) Simulated light propagation in the designed tenth-order AEM at the resonance wavelength of  $\lambda = 1539\mathrm{nm}$ . (c) Simulated transmissions at the drop port of the designed AEMs by assuming that there is some width variation of  $\Delta w = \pm 20$  and  $\pm 40\mathrm{nm}$ .

![](images/72952eea23dbcdc526781d412cd70283572c63d9fd726d6c9a1299148329ac6f.jpg)

![](images/a6fe9f30a5c31c439f53d19f20717a2b321033bdafd3a9b1da80dd99b144739b.jpg)

estimated by normalizing the measured transmissions at the drops of the AEMs with respect to the transmission of a straight waveguide on the same chip. It can be seen that the fabricated AEM filter has box-like responses with low excess losses of  $\sim 1$  dB even without any thermal-tuning or trimming, which is different from those

MRR filters reported previously. $^{17-20}$  The FSR of the AEM is as large as  $\sim 37$  nm due to its compact size of the AEM. The 3 dB bandwidth of the AEM-based filter is about  $3\mathrm{nm}$ , and the ER is over 60 dB. The roll-off rate is about  $70.5~\mathrm{dB / nm}$ , which is much higher than that for low-order MRRs. For example, the roll-off rate of the second-order

![](images/2e934ba02154919a0f3e9f709e4e58cea6098b81db6e2dc867ba79aa258d6344.jpg)  
FIG. 5. (a) Microscope images of the fabricated tenth-order AEM filters with  $\Delta w = 0$  and  $\pm 20\mathrm{nm}$ ; zoom-in view of (b) the tenth-order AEM filter and (c) the grating coupler.

![](images/2020dd94a0d52af46943be38e8e00dd323eba3285be4a2b996f6e4fce01c9ade.jpg)

![](images/4305f8018c90288dee2e1cd0a8fc6b8fc699a2cc7f7d5c04cd5696fbddd1ab66.jpg)

![](images/2f1b184b28caa7982e057ccd505c405eab12a3750aaa3f93bfc997472a700b6f.jpg)  
FIG. 6. Measured spectral responses of the fabricated silicon photonic filters based on the tenth-order AEMs.

AEM is  $\sim 6.8$  dB/nm only.[21] It is possible to achieve an even higher roll-off rate by introducing higher-order AEMs. Figure 7 shows the measured results of the fabricated tenth-order AEM filters with  $\Delta w = 0$  and  $\pm 20$  nm. It shows that one can still obtain box-like spectral responses with a high ER up to 60 dB even when the waveguide widths vary with  $\Delta w = \pm 20$  nm. The bandwidth has some deviation of about  $\mp 0.3$  nm, while the excess loss is still lower than 2 dB. One should note that the ripples of about 2 dB appear when the waveguide is widened by  $+20$  nm, which agrees well with the simulation result as shown in Figs. 3(b) and 4(c). From Figs. 6 and 7, it can

![](images/902e1460c433eb3dde218332ad6f2bed7d370727821c7ba251972b282d86bc75.jpg)  
FIG. 7. Measured spectral responses of the fabricated tenth-order AEM when there is some core-width variation of  $\Delta w = 0$  and  $\pm 20\mathrm{nm}$ . Here, these filters with  $\Delta w = 0$  and  $\pm 20\mathrm{nm}$  have some wavelength shifting.

be seen that the measured spectral responses are gently asymmetric, which is slightly different from the simulated result. This is probably due to the small fabrication deviation in the fabrication, and advanced manufacturing technologies will be helpful.

To characterize the wafer-scale uniformity of the fabrication for the tenth-order AEM filters, we measured all the six chips fabricated by the same MPW processes. Figures 8(a)-8(f) show the normalized measurement results for six chips from the same fabrication batch, respectively. It shows that all chips (except chip No. 6) obtain very similar spectral responses with large ERs over  $60~\mathrm{dB}$ ,

![](images/eda9c52295b8abc1544afc04e59fc1ab93392110a9e610a40c709b85884b1897.jpg)

![](images/ca9bcfcf2dfac607ee1a2f3d52255c1785ea9fd66a9b420106e9d5bef7e945e0.jpg)  
FIG. 8. Measured results of the fabricated tenth-order AEM filters on six chips. (a) Chip No. 1; (b) Chip No. 2; (c) Chip No. 3; (d) Chip No. 4; (e) Chip No. 5; (f) Chip No. 6.

![](images/6fa6a6fe3caa1e0c83ebd827c18df41ce4e4cfa0a9405837b9c7727c17a90c0a.jpg)

![](images/beb8c7b54f1a498ae76250ed0e27cd5b962321e3c2070c63aa400c818b4335aa.jpg)

![](images/91ad1a93fa4f5cb0d2ed58a02e1599d04985bf18431d3f902f7dfbfce9217f3e.jpg)

![](images/0f68adf9c0df02dfc47acaffc489a581b46907254025354639a3195949527140.jpg)

TABLE I. Summary of silicon photonic filters based on MRRs with a high order number of  $\geq  7$  . (Boldface denotes the work in this Letter.)  

<table><tr><td>References</td><td>Order</td><td>FSR (nm)</td><td>BW3dB (nm)</td><td>Loss (dB)</td><td>ER (dB)</td><td>Waveguide</td><td>Unit size (μm2)</td><td>Phase control</td></tr><tr><td>17</td><td>7</td><td>~7.5</td><td>~1.2</td><td>1.5</td><td>&gt;70</td><td>Strip</td><td>32 × 20</td><td>Thermal-tuning</td></tr><tr><td>13</td><td>8</td><td>11.7</td><td>~3</td><td>~8</td><td>~40</td><td>Strip</td><td>16.5 × 13</td><td>All passive</td></tr><tr><td>13</td><td>16</td><td>11.7</td><td>~3.5</td><td>~9</td><td>~42</td><td>Strip</td><td>16.5 × 13</td><td>All passive</td></tr><tr><td>20</td><td>10</td><td>1.2</td><td>~0.17</td><td>~43</td><td>32</td><td>Ridge</td><td>81.6 × 81.6</td><td>Thermal-tuning</td></tr><tr><td>19</td><td>10</td><td>~6</td><td>~0.8</td><td>~5</td><td>50</td><td>Ridge</td><td>40 × 20</td><td>All passive</td></tr><tr><td>18</td><td>14</td><td>8.4</td><td>~0.5</td><td>~7</td><td>73</td><td>Ridge</td><td>22 × 20</td><td>Thermal-tuning</td></tr><tr><td>This work</td><td>10</td><td>37</td><td>~3</td><td>~1</td><td>&gt;60</td><td>Strip</td><td>5.6 × 4.6</td><td>All passive</td></tr></table>

low excess losses of 1-2.5 and 3 dB bandwidths of  $3 - 3.4\mathrm{nm}$ . One should note that there are some deviations of the central wavelength of the tenth-order AEMs among different chips, which is mainly caused by the silicon-core width-variation and the silicon-core thickness-variation of different chips. For example, the central wavelengths of the filters on the six chips (Nos. 1-6) have some difference of  $\sim 6.5\mathrm{nm}$ . On the other hand, the ten AEMs of the same photonic filter have so excellent consistency that the spectral response is very similar to the theoretical simulation result. In this way, one can tune the filter wavelength conveniently by only introducing a micro-heater for all the AEMs instead of individual thermal control for each ring. This avoids the complex wavelength alignment among the rings and, thus, reduces the complexity of the device operation.

Table I gives a summary of silicon photonic filters based on MRRs with a high order number of  $\geq 7$  reported in recent years. It is worth noting that ultra-high order MRR filters have also been reported, including 50th, 100th, and even 235th order.[22-24] However, they often have very large losses and spectral responses with large fluctuations, which is not included in Table I. As shown in Table I, the present tenth-order AEM filters have the largest FSRs (i.e.,  $\sim 37\mathrm{nm}$ ) and very low excess losses of  $\sim 1$  dB. In contrast, most reported ordinary high-order resonators have an FSR of  $\sim 10$  nm or less as well as high excess losses of  $>5$  dB (except Ref. 17). It is also worth noting that the present high-order AEM filters show box-like responses with a high ER of  $>60$  dB even without any thermal-tuning and trimming, which is the highest ER in the all-passive high-order MRRs reported until now. In contrast, most high-order MRR filters reported previously usually need careful calibration for each MRR individually. In contrast, for the present AEM filters, the wavelength tuning can be easily achieved by introducing a single micro-heater. Finally, we also calculate the group delay of the designed tenth-order AEM, as shown in Fig. 9. It can be seen that the calculated group delay is less than 26 ps, which is comparable to those of conventional coupled resonator optical waveguide (CROW) filters reported previously.[13,25,26] As a result, the present AEM filters can work well in high-speed data transmission systems according to the experimental results in Refs. 13, 25, and 26.

In summary, we have proposed and realized a compact and high-ER silicon photonic filter by using tenth-order AEMs in cascade. Both the radius and the width of the AEMs are varied adiabatically, which not only provides sufficient coupling but also compact size with low propagation loss for the micro-resonators. The realized AEM has a compact unit size of  $5.6 \times 4.6 \mu \mathrm{m}$  and a large

![](images/9a7f355c058657fbb109219dc8349a0be64ebc32f62e11492ec461f2d2b8f48f.jpg)  
FIG. 9. Simulated group delay of the designed tenth-order AEM.

FSR of  $37~\mathrm{nm}$ , which is the largest one among those high-order resonators reported previously. The realized high-order AEM filters have shown an ER as high as 60 dB. More interestingly, the AEMs show high consistency even when fabricated with CMOS-compatible foundry processes (instead of using E-beam lithography processes). Therefore, it does not require individual thermal-tuning and careful calibration, which makes it very attractive for many applications.

This work was supported by the National Major Research and Development Program (Grant No. 2018YFB2200200/2018 YFB2200201), the Zhejiang Provincial Major Research and Development Program (Grant No. 2021C01199), the National Science Fund for Distinguished Young Scholars (Grant No. 61725503), the National Natural Science Foundation of China (NSFC) (Grant Nos. 61961146003 and 91950205), the Zhejiang Provincial Natural Science Foundation (Grant Nos. LZ18F050001 and LD19F050001), and the Fundamental Research Funds for the Central Universities. The authors acknowledge the silicon photonics fabrication service from CUMEC in China.

# AUTHOR DECLARATIONS

# Conflict of Interest

The authors declare no conflicts of interest.

# DATA AVAILABILITY

Data sharing is not applicable to this article as no new data were created or analyzed in this study but may be available from the corresponding author upon reasonable request.

# REFERENCES

$^{1}$ D. Dai and J. Bowers, "Silicon-based on-chip multiplexing technologies and devices for Peta-bit optical interconnects," Nanophotonics 3, 283-311 (2014).  
$^{2}$ A. Li and W. Bogaerts, "Reconfigurable nonlinear nonreciprocal transmission in a silicon photonic integrated circuit," Optica 7, 7-14 (2020).  
$^{3}$ K. Y. Yang, J. Skarda, M. Cotrufo, A. Dutt, G. H. Ahn, M. Sawaby, D. Vercruysse, A. Arababian, S. Fan, A. Alú, and J. Vucković, "Inverse-designed non-reciprocal pulse router for chip-based LiDAR," Nat. Photonics 14, 369 (2020).  
$^{4}$ J. Wang, F. Sciarrino, A. Laing, and M. G. Thompson, "Integrated photonic quantum technologies," Nat. Photonics 14, 273-284 (2020).  
5 D. J. Liu, H. N. Xu, Y. Tan, Y. C. Shi, and D. X. Dai, "Silicon photonic filters," Microw Opt. Technol. Lett. 63, 2252-2268 (2021).  
$^{6}$ W. Bogaerts, S. K. Selvaraja, P. Dumon, J. Brouckaert, K. De Vos, D. Van Thourhout, and R. Baets, "Silicon-on-insulator spectral filters fabricated with CMOS technology," IEEE J. Sel. Top. Quantum Electron. 16, 33-44 (2010).  
7J. C. Adcock, J. M. Bao, Y. L. Chi, X. J. Chen, D. Bacco, Q. H. Gong, L. K. Oxenlowe, J. W. Wang, and Y. H. Ding, "Advances in silicon quantum photonics," IEEE J. Sel. Top. Quantum Electron. 27, 6700224 (2021).  
8M. Piekarek, D. Bonneau, S. Miki, T. Yamashita, M. Fujiwara, M. Sasaki, H. Terai, M. G. Tanner, C. M. Natarajan, R. H. Hadfield, J. L. O'Brien, and M. G. Thompson, "High-extinction ratio integrated photonic filters for silicon quantum photonics," Opt. Lett. 42, 815-818 (2017).  
$^{9}$ D. Oser, F. Mazeas, X. Le Roux, D. Perez-Galacho, O. Alibart, S. Tanzilli, L. Labonte, D. Marris-Morini, L. Vivien, E. Casson, and C. Alonso-Ramos, "Coherency-broken Bragg filters: Overcoming on-chip rejection limitations," Laser Photonics Rev. 13, 1800226 (2019).  
$^{10}$ F. Xia, M. Rooks, L. Sekaric, and Y. Vlasov, "Ultra-compact high order ring resonator filters using submicron silicon photonic wires for on-chip optical interconnects," Opt. Express 15, 11934-11941 (2007).  
11 P. Chen, S. Chen, X. Guan, Y. Shi, and D. Dai, "High-order microring resonators with bent couplers for a box-like filter response," Opt. Lett. 39, 6304-6307 (2014).  
$^{12}$ S. D. Shimura, T. Simoyama, M. Seki, N. Yokoyama, M. Ohtsuka, K. Koshino, T. Horikawa, Y. Tanaka, and K. Morito, "Low-loss, flat-topped and spectrally uniform silicon-nanowire-based 5th-order CROW fabricated by ArF-immersion lithography process on a 300-mm SOI wafer," Opt. Express 21, 30163-30174 (2013).  
$^{13}$ F. N. Xia, L. Sekaric, M. O'Boyle, and Y. Vlasov, "Coupled resonator optical waveguides based on silicon-on-insulator photonic wires," Appl. Phys. Lett. 89, 041122 (2006).

$^{14}$ P. Dong, N.-N. Feng, D. Feng, W. Qian, H. Liang, D. C. Lee, B. J. Luff, T. Banwell, A. Agarwal, P. Toliver, R. Menendez, T. K. Woodward, and M. Asghari, "GHz-bandwidth optical filters based on high-order silicon ring resonators," Opt. Express 18, 23784-23789 (2010).  
15 J. C. C. Mak, W. D. Sacher, T. Y. Xue, J. C. Mikkelsen, Z. Yong, and J. K. S. Poon, "Automatic resonance alignment of high-order microring filters," IEEE J. Quantum Electron. 51, 0600411 (2015).  
$^{16}$ J. R. Ong, R. Kumar, and S. Mookherjea, "Ultra-high-contrast and tunable-bandwidth filter using cascaded high-order silicon microring filters," IEEE Photonics Technol. Lett. 25, 1543-1546 (2013).  
17R. Ge and X. Cai, "High-extinction-ratio optical filters based on high-order silicon microring resonators," in 2018 Conference on Lasers and Electro-Optics Pacific Rim (CLEO-PR) (IEEE, 2018).  
$^{18}$ H. Jayatilleka, H. Shoman, L. Chrostowski, and S. Shekhar, "Photoconductive heaters enable control of large-scale silicon photonic ring resonator circuits," Optica 6, 84-91 (2019).  
$^{19}$ X. Luo, J. Song, S. Feng, A. W. Poon, T.-Y. Liow, M. Yu, G.-Q. Lo, and D.-L. Kwong, "Silicon high-order coupled-microring-based electro-optical switches for on-chip optical interconnects," IEEE Photonics Technol. Lett. 24, 821-823 (2012).  
20 L. Xu, J. Hou, H. Tang, Y. Yu, Y. Yu, X. Shu, and X. Zhang, "Silicon-on-insulator-based microwave photonic filter with widely adjustable bandwidth," Photonics Res. 7, 110-115 (2019).  
21 D. Liu, L. Zhang, Y. Tan, and D. Dai, "High-order adiabatic elliptical-microring filter with an ultra-large free-spectral-range," J. Lightwave Technol. 39, 5910-5916 (2021).  
22 S. H. Tao, J. F. Song, Q. Fang, M. B. Yu, G. Q. Lo, and D. L. Kwong, “50th order series-coupled micro-ring resonator,” in 2008 IEEE PhotonicsGlobal@Singapore (IPGC) (IEEE, Singapore, 2008), Vols. 1 and 2, pp. 12-14.  
23F. Xia, L. Sekaric, and Y. Vlasov, "Ultracompact optical buffers on a silicon chip," Nat. Photonics 1, 65-71 (2007).  
24 M. L. Cooper, G. Gupta, M. A. Schneider, W. M. J. Green, S. Assefa, F. Xia, Y. A. Vlasov, and S. Mookherjea, "Statistics of light transport in 235-ring silicon coupled-resonator optical waveguides," Opt. Express 18, 26505-26516 (2010).  
25C. Li, R. Bai, A. Shafik, E. Z. Tabasy, B. Wang, G. Tang, C. Ma, C.-H. Chen, Z. Peng, M. Fiorentino, R. G. Beausoleil, P. Chiang, and S. Palermo, "Silicon photonic transceiver circuits with microring resonator bias-based wavelength stabilization in  $65\mathrm{nm}$  CMOS," IEEE J. Solid-State Circuits 49, 1419-1436 (2014).  
26 P. Dong, J. Lee, Y.-K. Chen, L. L. Buhl, S. Chandrasekhar, J. H. Sinsky, and K. Kim, "Four-channel 100-Gb/s per channel discrete multitone modulation using silicon photonic integrated circuits," J. Lightwave Technol. 34, 79-84 (2016).