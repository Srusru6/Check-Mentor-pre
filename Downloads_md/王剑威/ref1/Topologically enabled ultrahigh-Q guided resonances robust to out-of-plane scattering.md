# Topologically enabled ultrahigh-Q guided resonances robust to out-of-plane scattering

https://doi.org/10.1038/s41586-019-1664-7

Received: 21 January 2019

Accepted: 26 August 2019

Published online: 23 October 2019

Jicheng Jin $^{1}$ , Xuefan Yin $^{1}$ , Liangfu Ni $^{1}$ , Marin Soljacic $^{2}$ , Bo Zhen $^{3}$  & Chao Peng $^{1,4*}$

Because of their ability to confine light, optical resonators $^{1-3}$  are of great importance to science and technology, but their performance is often limited by out-of-plane-scattering losses caused by inevitable fabrication imperfections $^{4,5}$ . Here we theoretically propose and experimentally demonstrate a class of guided resonances in photonic crystal slabs, in which out-of-plane-scattering losses are strongly suppressed by their topological nature. These resonances arise when multiple bound states in the continuum—each carrying a topological charge $^{6}$ —merge in momentum space and enhance the quality factors  $Q$  of all nearby resonances in the same band. Using such resonances in the telecommunication regime, we experimentally achieve quality factors as high as  $4.9 \times 10^{5}-12$  times higher than those obtained with standard designs—and this enhancement remains robust for all of our samples. Our work paves the way for future explorations of topological photonics in systems with open boundary conditions and for their application to the improvement of optoelectronic devices in photonic integrated circuits.

Topological defects<sup>7</sup> are ubiquitous in the natural world. Examples range from quantum vortices in superfluids to singular optical beams<sup>8</sup>, which are characterized by the non-trivial winding patterns of system parameters (velocity, phase or polarization) in real space. Recently, it was found that unexpected topological defects can also emerge in the momentum space of a crystal and give rise to interesting physical consequences; one such example is the optical bound states in the continuum (BICs). BICs reside inside the continuous spectrum of extended states but counterintuitively remain perfectly localized in space and their lifetimes are theoretically infinitely long. Since their initial proposal<sup>9</sup>, BICs have been observed in a variety of wave systems, including photonic<sup>10-15</sup>, phononic<sup>16</sup> and water waves<sup>17</sup>. Furthermore, they have been used to enhance various applications, such as lasers<sup>13,18</sup> and antennas<sup>19,20</sup>, by providing an out-coupling channel through their surface-emitting nature. In photonic crystal slabs, it has been identified that their fundamental nature is topological; they are essentially topological defects in polarization directions defined in momentum space<sup>6</sup>. In practice<sup>10,21</sup>, the quality factors of such BICs are often much lower than their theoretical prediction of infinity, limited to only about  $10^{4}$ . Aside from other contributing factors, such as material absorption or the finite size of samples, the main limiting factor of the  $Q$  value of BICs is scattering losses caused by fabrication imperfections or disorders—a common problem for many high- $Q$  on-chip resonators<sup>1,2,4,5</sup>.

Here we theoretically propose and experimentally demonstrate on-chip photonic resonances that are much less susceptible to out-of-plane-scattering losses than expected, owing to their unique topological features. We start by showing that resonances with ultrahigh  $Q$  can be achieved by merging multiple BICs. First, we consider a photonic crystal slab (Fig. 1a), in which a square lattice (periodicity  $a = 519.25\mathrm{nm}$ ) of circular air holes (radius  $r = 175\mathrm{nm}$ ) is patterned in silicon (thickness

$h = 600 \mathrm{~nm}$ . With the use of numerical simulations (using the COM-SOL Multiphysics software), we focus on the transverse electric (TE) A band (red line), featuring nine BICs where  $Q$  diverges to infinity (Fig. 1b). The topological nature of the BICs can be understood from the corresponding far-field polarization plots (Fig. 1b, bottom panels), where each BIC appears as a topological defect (vortex) in the polarization long axes[6,19,20,22,23] characterized by an integer topological charge of  $\pm 1$ . Among these nine vortices, one is pinned at the centre of the Brillouin zone owing to symmetry, whereas the locations of the remaining eight can be controlled by varying system parameters such as the periodicity. For example, when  $a$  increases from 519.25 nm to 531.42 nm, the eight off-centre BICs move towards the centre until all nine of them merge into a single BIC with a charge of  $+1$  when  $a = 531.42 \mathrm{~nm}$ . This single BIC persists when  $a$  further increases to 580 nm.

The topological configuration of BICs controls radiative losses of all nearby resonances. Specifically,  $Q$  is shown to decay quadratically  $(Q\propto 1 / k^2)$  with respect to the distance  $k$  (in momentum space) from a single isolated BIC with charge  $\pm 1$ ; however, this scaling changes to  $Q\propto 1 / k^6$  in the configuration in which all nine BICs merge (referred to as 'merging-BIC design' hereafter). A comparison between these two scenarios is shown in Fig. 1c, where the  $Q$  values in a merging-BIC design (red) are always orders of magnitude higher than those in an isolated-BIC design (blue) along all directions in  $k$  space, owing to their fundamentally different scaling properties. This difference in scaling originates from the asymptotic behaviour of  $Q\propto 1 / [k(k + k_{\mathrm{BIC}})(k - k_{\mathrm{BIC}})]^2$  in the regime in which off-centre BICs at  $\pm k_{\mathrm{BIC}}$  and centred BIC coexist, as shown in Fig. 1c (grey lines). In the merging-BIC design,  $k_{\mathrm{BIC}}\rightarrow 0$  and we get  $Q\propto 1 / k^6$ . Further discussion is provided in Supplementary Information sections I and II.

Although simulation results of infinitely large perfect photonic crystals reproduce radiative quality factors, real samples (schematically

![](images/3c3171d6ba161313aa0967f867271638b99a325c57895b466db74f45196286b4.jpg)  
a

![](images/7b4e067b0f55a9feffa8bb2f00c36e8a270682756c9220486789ccc999461c41.jpg)  
b

![](images/b045f5d72cd036e9bdc0e789b33a874c5ccd3c6e9237d431b9d681a4fc341b51.jpg)  
c  
Fig. 1|Suppressing radiation losses by merging multiple topological charges. a, Left, Schematic of a photonic crystal slab and the factors contributing to loss. Right, Simulated band structure. The TE A band is marked with a red line, and  $\omega$  is the normalized resonance frequency. b, Multiple BICs appear on band TE A, where the radiative quality factor  $Q$  diverges. Top, Simulated  $Q$  for various values of the sample periodicity, a. Bottom, far-field polarization plots. When  $a$  is tuned from  $519.25\mathrm{nm}$  (left) to  $580\mathrm{nm}$  (right), nine BICs at  $k_{\mathrm{BIC}}$  with topological charge  $\pm 1$  merge into an isolated BIC with charge  $+1$ . c, Simulated  $Q$  before ( $a = 519.25\mathrm{nm}$ ; grey) and after charges merge at the centre of the Brillouin zone ( $a = 580\mathrm{nm}$ ; blue). The transition ( $a = 531.42\mathrm{nm}$ ; red) corresponds to the merging-BIC configuration, which shows considerably higher quality factors than the isolated-BIC configuration (blue). This is caused by a change to a scaling rule of  $Q \propto 1 / k^6$ , which is observed along both the  $\Gamma - X$  and  $\Gamma - M$  directions. All simulations used the finite-element method in COMSOL.

shown in Fig. 2a) feature some major differences that determine the highest  $Q$  achievable in practice. First, all samples are finite in size; their boundaries introduce fractional orders of the primitive reciprocal lattice in  $k$  space (green dots in Fig. 2a; see Supplementary Information section III for details)[24]. Second, all fabricated samples exhibit disorder and imperfections with both long- and short-range correlations, allowing modes at different  $k$  points to couple to each other. Because of these inevitable coupling terms, modes at different fractional momentum orders are hybridized and all of their loss channels become available to the final resonance[25].

![](images/01afccd512d02ddd95014d9d4f4f0dec8d1002dcbd393d9102eb319ba85c88d6.jpg)  
a

![](images/dcca6fa89c35fd24b946963ce09ba99514594e46d15cc1230bdef256cc72b397.jpg)

![](images/d26fcb6bf5e0c0f9120ca89eaced3a85675da28cd74b229c35f9723cc6680ca6.jpg)  
b

![](images/6687f70f02aa784e38b76196e171a5d87265e037833a0cdcc93f62ef056afa41.jpg)  
d

![](images/5a46231285bbb7035c5b1c9399f4282e0f487e56135e2fb698b54044f31df050.jpg)  
C

![](images/dd41adc4749123f7fcc60cf5adede7f37d6bbba204fa0bca4222f3afbb4b6a51.jpg)  
Fig. 2|Topological protection against scattering losses. a, Schematic of a fabricated photonic crystal sample (solid lines; top), with disorder in the locations and radii of the holes (dashed lines; top). In reciprocal space, fractional orders of momentum (green dots; bottom) are introduced by the supercell.  $N$  is the size of the supercell in increments of the periodicity  $a$  and  $\beta_{N}$  is the minimum step size of the fractional orders of momentum. b, Momentum-energy distribution of the highest-  $Q$  mode in the merging-BIC design for a perfect (top) and a disordered (bottom) structure inside the first Brillouin zone. a.u., arbitrary units. c, Momentum-energy distribution of the radiation field in the disordered merging-BIC (top) and isolated-BIC (bottom) designs. The white circles represent the light cone—the region in the momentum space where guided resonance can couple to the radiation channel, as determined by the structure of the sample. The scattering loss is considerably lower in the merging-BIC sample than in the isolated-BIC sample. d, Schematic of an asymmetric hole (top) acting as a fabrication imperfection, and simulated  $Q$  values near the centre of the Brillouin zone obtained by the application of disorder (bottom). All simulations were performed in a  $15a \times 15a$  supercell ( $N = 15$ ).

![](images/d2b0a08721bbf54b23bc4dffe49e717e5d7d2bd93121080941dd7807942adeeb.jpg)

![](images/83a02720b1b3ef4964dd8b4f2d5ae6c7aa269a3075846d50bc69258bc34dad4f.jpg)

The advantage of our merging-BIC design over an isolated-BIC design is confirmed by simulations (using the COMSOL Multiphysics software) of perturbed  $15 \times 15$  photonic crystal supercells. In a perfect supercell structure without disorder, a BIC with infinite  $Q$  remains at

the centre of the Brillouin zone (Fig. 2b, upper panel). For comparison, perturbations are applied to both the radii  $(\Delta r)$  and positions  $(\Delta x, \Delta y)$  of the holes according to the statistics that best describes our samples (Fig. 3). As expected, each mode in the disordered samples has multiple components in  $k$  space. Furthermore, resonances in a disordered sample with a merging-BIC design have considerably lower radiation fields than those from an isolated-BIC design with the same disorder (Fig. 2c). This result agrees well with Fig. 1b, c: all modes contributing to the final resonance in the merging-BIC sample have much higher  $Q$  values than those in the isolated-BIC case because resonances in the former are much more immune to out-of-plane scattering from disorder than in the latter. Finally, this enhancement of  $Q$  is found to be robust across a range of  $k$  values, as shown in Fig. 2d (bottom panel), by assuming asymmetric holes to represent typical fabrication errors before applying the disorder (see Supplementary Information sections IV and V for details).

To verify our theoretical findings, we fabricate photonic crystal samples with both merging-BIC and isolated-BIC designs using the same electron-beam lithography and inductively coupled plasma etching processes on a 600-nm-thick silicon-on-insulator wafer (see Methods for details). The underlying  $\mathrm{SiO}_2$  layer is then removed to restore the up-down mirror symmetry required for tunable  $\mathrm{BICs}^{6,10}$ . Alternatively, one may use refractive-index-matching liquid or deposition layers instead. The samples are about  $250 \times 250 \mu \mathrm{m}^2$  in size. The periodicity is varied from 530 nm to 580 nm to sample designs with merging and isolated BICs. From the scanning electron microscope images of the samples (Fig. 3a, b), the standard deviations of the hole locations and radii are estimated to be about 5 nm, which is used in the simulations discussed earlier.

A schematic of the experimental setup is shown in Fig. 3c. A tunable telecommunication laser with light in the  $\mathrm{C + L}$  band is first sent through an X-polarizer before the light is focused by a lens (L1) onto the back focal plane of an infinity-corrected objective lens. The incident angle of the laser on the sample is thus controlled by moving L1 on the  $x - y$  plane. Using this confocal setup, reflected and scattered light are also collected by the same objective; they are then magnified 1.67 times through a relay 4f system and imaged on a camera. A Y-polarizer is used to block reflected light (X-polarized) while allowing scattered light to pass (see Methods and Supplementary Information section VI). Under the on-resonance coupling condition, where the

![](images/63ef4db74c8618ccdae4b6ed78cde870dca7749e6f0134bc87ee2d4f69a95704.jpg)  
a

![](images/fd9caa39ee9313d9017976d4b9a13fea1a73a9f0e54fcc676c72807106ebdb49.jpg)  
c

![](images/b6458521cc8a96f3e75f096d5f8f91ea7e8d3efa6b4b169963db2d30cf4d35d7.jpg)  
b  
Fig. 3 | Experimental setup. a, b, Scanning electron microscope images of the fabricated photonic crystal sample; top (a) and side (b) view. c, Schematic of the measurement setup. The blue lines represent the incident light and its direct reflection. The light red region denotes radiation losses induced by scattering from disorder. L, lens. BS, beamsplitter.

photonic crystal sample supports a resonance at the same wavelength as the incident light at that incident angle, isofrequency contours are observed on the camera, similarly to previously reported results $^{22,26}$ . Three examples of isofrequency contours are schematically shown in Fig. 4a as dashed lines.

The  $Q$  values of resonances at different  $k$  points are further characterized using scattered light. Specifically, a movable pinhole (not shown in Fig. 3c) is placed on the image plane of the objective's rear focal plane to specify a  $k$  point. A photodiode connected to a lock-in amplifier is placed behind the pinhole to record the intensity of the scattered light as a function of the wavelength of the tunable laser. As shown in Fig. 4a, when different  $k$  points are selected by the pinhole (X, Y and Z), different scattering spectra are obtained, all exhibiting symmetric Lorentzian features. Similar scattering phenomena have been observed before[26] and can be understood as follows: the intensity of scattered light is governed by the spectral density of states of the sample at that  $k$  point, and is described by a Lorentzian function centred at the resonance frequency, with linewidth determined by the  $Q$  value of the resonance (see Supplementary Information section VII for details).

![](images/1c7e072fe3a72ed927884a16a93796d6626da4a30cd856851bd5f714ec812a15.jpg)  
Fig. 4 | Experimental results. a, Isofrequency contours of the sample at different wavelengths are observed on the camera (right). Three examples are shown as dashed lines. The scattered-light intensity at different points in momentum space (X, Y, Z; left) is further characterized using a photodiode, and is fitted by symmetric Lorentzians as a function of incident wavelength. The

![](images/4480699de2a7303f9961bbb23e7ba0760a7b4ca8329b246e7407e43c08d3bc87.jpg)

![](images/26a4941622aa061c853231cbebfb5b9e0506bb3aeab3f34440f9fb82e994b99f.jpg)  
linewidth is determined by the  $Q$  value of the underlying resonance.  $\mathbf{b},\mathbf{c}$  . The highest  $Q$  observed in the merging-BIC sample is  $4.9\times 10^{5}$  at point W (b), which is more than an order of magnitude larger than that of an isolated-BIC sample constructed with the same fabrication process  $(Q = 4.0\times 10^{4};\mathbf{c})$

![](images/5b2b35923637d54f3e8b1cc2eb1a09857071ac621e6bd9fd49c9875f9afdb6c8.jpg)  
Fig. 5 |12-fold enhancement of  $Q$  via topological protection. a, Dispersion of resonances measured at different points in momentum space (circles), showing good agreement with FEM simulation predictions (dashed lines) along both the  $\Gamma - X$  (top) and  $\Gamma - M$  (bottom) directions. b, An enhancement of  $Q$  by a factor of more than 10 is observed over a wide range in momentum space for the merging-BIC samples (red and blue) compared to the isolated-BIC sample (purple) owing to topological protection.

The  $Q$  values of the resonances are extracted by numerically fitting the scattering spectra with Lorentzian functions. As shown in Fig. 4a,  $Q$  increases from  $2.6 \times 10^{5}$  to  $4.5 \times 10^{5}$  as the observing point moves closer to the centre of the Brillouin zone from X to Z. This agrees well with the simulation results in Fig. 1. The highest  $Q$  observed in the merging-BIC sample is  $4.9 \times 10^{5}$  at point W (Fig. 4b). In comparison, the highest  $Q$  observed in the isolated-BIC sample—fabricated on the same wafer through the same processes as the merging-BIC sample, but with different structural parameters—is limited to only  $4 \times 10^{4}$ , more than an order of magnitude lower (Fig. 4c). This confirms our simulation results in Fig. 2, which indicate that engineering the topological configurations of BICs can substantially suppress scattering losses. Furthermore, this over-ten-fold enhancement of the quality factor is observed to be robust: not only does it appear over a wide range in  $k$  space, as shown in Fig. 5, but a similar level of enhancement is also observed in all merging-BIC samples that we fabricated (see Supplementary Information section VIII for details).

Topological photonics $^{27-29}$  has found tremendous success in suppressing in-plane back-scattering losses by breaking reciprocity. Here we use topology to solve a different class of problems, by suppressing out-of-plane-scattering losses in a reciprocal system. By merging multiple topological charges carried by BICs, we experimentally demonstrate photonic crystal resonances with record-high quality factors of  $Q = 4.9 \times 10^{5}$ , more than an order of magnitude higher than those of ordinary designs. These ultrahigh- $Q$  resonances are potentially useful for chemical or biological sensing $^{30}$  and large-area laser applications $^{18}$ . Furthermore, our high- $Q$  resonances are observed to be robust against fabrication imperfections, and can help to improve the performance of optoelectronic devices using concepts from topological photonics.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-019-1664-7.

1. Biberman, A., Shaw, M. J., Timurdogan, E., Wright, J. B. & Watts, M. R. Ultralow-loss silicon ring resonators. Opt. Lett. 37, 4236-4238 (2012).  
2. Hossein-Zadeh, M. & Vahala, K. J. Free ultra-high-q microtoroid: a tool for designing photonic devices. Opt. Express 15, 166-175 (2007).  
3. Akahane, Y., Asano, T., Song, B.-S. & Noda, S. High-Q photonic nanocavity in a two-dimensional photonic crystal. Nature 425, 944-947 (2003).  
4. Minkov, M., Dharanipathy, U. P., Houdre, R. & Savona, V. Statistics of the disorder-induced losses of high-Q photonic crystal cavities. Opt. Express 21, 28233-28245 (2013).  
5. Ishizaki, K., Okano, M. & Noda, S. Numerical investigation of emission in finite-sized, three-dimensional photonic crystals with structural fluctuations. J. Opt. Soc. Am. B 26, 1157-1161 (2009).  
6. Zhen, B., Hsu, C. W., Lu, L., Stone, A. D. & Soljacic, M. Topological nature of optical bound states in the continuum. Phys. Rev. Lett. 113, 257401 (2014).  
7. Mermin, N. D. The topological theory of defects in ordered media. Rev. Mod. Phys. 51, 591-648 (1979).  
8. Gbur, G. J. Singular Optics (CRC Press, 2016).  
9. von Neumann, J. & Wigner, E. Über merkwürdige diskrete Eigenwerte. Phys. Z. 30, 465-467 (1929).  
10. Hsu, C. W. et al. Observation of trapped light within the radiation continuum. Nature 499, 188-191 (2013).  
11. Plotnik, Y. et al. Experimental observation of optical bound states in the continuum. Phys. Rev. Lett. 107, 183901 (2011).  
12. Fan, S. & Joannopoulos, J. D. Analysis of guided resonances in photonic crystal slabs. Phys. Rev. B 65, 235112 (2002).  
13. Kodigala, A. et al. Lasing action from photonic bound states in continuum. Nature 541, 196-199 (2017).  
14. Gomis-Bresco, J., Artigas, D. & Torner, L. Anisotropy-induced photonic bound states in the continuum. Nat. Photon. 11, 232-236 (2017).  
15. Molina, M. I., Miroshnichenko, A. E. & Kivshar, Y. S. Surface bound states in the continuum. Phys. Rev. Lett. 108, 070401 (2012).  
16. Lim, T. C. & Farnell, G. W. Character of pseudo surface waves on anisotropic crystals. J. Acoust. Soc. Am. 45, 845-851 (1969).  
17. Cobelli, P. J., Pagneux, V., Maurel, A. & Petitjeans, P. Experimental observation of trapped modes in a water wave channel. EPL 88, 20006 (2009).  
18. Hirose, K. et al. Watt-class high-power, high-beam-quality photonic-crystal lasers. Nat. Photon. 8, 406-411 (2014).  
19. Kitamura, K., Sakai, K., Takayama, N., Nishimoto, M. & Noda, S. Focusing properties of vector vortex beams emitted by photonic-crystal lasers. Opt. Lett. 37, 2421-2423 (2012).  
20. Iwahashi, S. et al. Higher-order vector beams produced by photonic-crystal lasers. Opt. Express 19, 11963-11968 (2011).  
21. Lee, J., Zhen, B., Chua, S.-L., Shapira, O. & Soljacic, M. Fabricating centimeter-scale high quality factor two-dimensional periodic photonic crystal slabs. Opt. Express 22, 3724-3731 (2014).  
22. Zhou, H. et al. Observation of bulk Fermi arc and polarization half charge from paired exceptional points. Science 359, eaap9859 (2018).  
23. Zhang, Y. et al. Observation of polarization vortices in momentum space. Phys. Rev. Lett. 120, 186103 (2018).  
24. Liang, Y., Peng, C., Sakai, K., Iwahashi, S. & Noda, S. Three-dimensional coupled-wave analysis for square-lattice photonic crystal surface emitting lasers with transverse-electric polarization: finite-size effects. Opt. Express 20, 15945-15961 (2012).  
25. Ni, L., Jin, J., Peng, C. & Li, Z. Analytical and statistical investigation on structural fluctuations induced radiation in photonic crystal slabs. Opt. Express 25, 5580-5593 (2017).  
26. Regan, E. C. et al. Direct imaging of isofrequency contours in photonic structures. Sci. Adv. 2, e1601591 (2016).  
27. Lu, L., Joannopoulos, J. D. & Soljacic, M. Topological photonics. Nat. Photon. 8, 821-829 (2014).  
28. Ozawa, T. et al. Topological photonics. Rev. Mod. Phys. 91, 015006 (2019).  
29. Wang, Z., Chong, Y., Joannopoulos, J. D. & Soljacic, M. Observation of unidirectional backscattering-immune topological electromagnetic states. Nature 461, 772-775 (2009).  
30. Luchansky, M. S. & Bailey, R. C. High-Q optical sensors for chemical and biological analysis. Anal. Chem. 84, 793-821 (2012).  
Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2019

# Methods

# Sample fabrication

The sample was fabricated on a silicon-on-insulator wafer with electronbeam lithography (EBL), followed by inductively coupled plasma etching. For EBL, the silicon-on-insulator wafer was spin-coated with a 330-nm-thick layer of ZEP520A photo-resist before being exposed to EBL (JBX-6300FS) at a beam current of  $400\mathrm{pA}$  and a field size of  $500\mu \mathrm{m}$ . The sample was then etched with ICP (Oxford Plasmapro Estrelas 100) using a mixture of  $\mathrm{SF}_6$  and  $\mathrm{C_4F_8}$ . After etching, the resist was removed with N-methyl-2-pyrrolidone and the buried oxide layer was removed using  $49\%$  HF.

# Measurement system

The incident light source was a tunable  $\mathrm{C + L}$ -band telecommunication laser (Santec TSL-550), which was sent through a chopper for lock-in detection. A pinhole with diameter of  $500\mu \mathrm{m}$  was placed on the Fourier plane to select the desired wavevectors. Light scattered through the pinhole was collected by a photodiode (PDA1ODT-EC), which was connected to a lock-in amplifier (SRSSR830). A flip mirror was used to switch between the camera that was used to image isofrequency contours and the photodiode. Besides characterizing far-field radiation patterns, the setup could also take near-field images of the sample if another lens was inserted into the optical path.

# Data availability

The data that support the plots in this paper and other findings of this study are available from the corresponding author upon request.

Acknowledgements We thank C. W. Hsu for discussions. We also thank L. Zhang from Tsinghua University and W. Liu from the Institute of Semiconductors for assistance in the preparation of the device. C.P. was supported by the National Natural Science Foundation of China under grant number 61575002. B.Z. was supported by the US Air Force Office of Scientific Research under award number FA9550-18-1-0133, by the US National Science Foundation through grant DMR-1838412 and by the Army Research Office under grant number W91NF-19-1-0087. The research was sponsored in part by the Army Research Office under Cooperative Agreement number W91NF-18-2-0048.

Author contributions J.J., X.Y., L.N. and C.P. conceived the idea. J.J., X.Y., C.P., B.Z. and M.S. performed the theoretical study. J.J., X.Y., L.N. and C.P. performed the analytical calculations and numerical simulations. J.J. and X.Y. conducted the experiments and analysed the data. J.J., C.P. and B.Z. wrote the manuscript, with input from all authors. C.P. supervised the research. All authors discussed the results.

Competing interests The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41586-019-1664-7.

Correspondence and requests for materials should be addressed to C.P.

Reprints and permissions information is available at http://www.nature.com/reprints.