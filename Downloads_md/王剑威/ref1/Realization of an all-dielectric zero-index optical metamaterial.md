# Realization of an all-dielectric zero-index optical metamaterial

Parikshit Moitra<sup>1†</sup>, Yuanmu Yang<sup>1†</sup>, Zachary Anderson<sup>2</sup>, Ivan I. Kravchenko<sup>3</sup>, Dayrl P. Briggs<sup>3</sup> and Jason Valentine<sup>4*</sup>

Metamaterials offer unprecedented flexibility for manipulating the optical properties of matter, including the ability to access negative index $^{1-4}$ , ultrahigh index $^{5}$  and chiral optical properties $^{6-8}$ . Recently, metamaterials with near-zero refractive index have attracted much attention $^{9-13}$ . Light inside such materials experiences no spatial phase change and extremely large phase velocity, properties that can be applied for realizing directional emission $^{14-16}$ , tunnelling waveguides $^{17}$ , large-area single-mode devices $^{18}$  and electromagnetic cloaks $^{19}$ . However, at optical frequencies, the previously demonstrated zero- or negative-refractive-index metamaterials have required the use of metallic inclusions, leading to large ohmic loss, a serious impediment to device applications $^{20,21}$ . Here, we experimentally demonstrate an impedance-matched zero-index metamaterial at optical frequencies based on purely dielectric constituents. Formed from stacked silicon-rod unit cells, the metamaterial has a nearly isotropic low-index response for transverse-magnetic polarized light, leading to angular selectivity of transmission and directive emission from quantum dots placed within the material.

Over the past several years, most work aimed at achieving zero index has been focused on epsilon-near-zero metamaterials (ENZs), which can be realized using diluted metals or metal waveguides operating below cutoff. These studies have included experimental demonstrations in the microwave $^{9,14}$ , mid-infrared $^{13}$  and visible regimes $^{12}$ . ENZ metamaterials have a permittivity  $\varepsilon$  near zero and a permeability  $\mu$  of unity, resulting in a near-zero refractive index ( $n = \sqrt{\mu\varepsilon}$ ). However, because the permeability remains finite, the relative optical impedance ( $Z = \sqrt{\mu/\varepsilon}$ ) is inevitably mismatched from free space, resulting in large reflections from the interface. Impedance-matched zero-index metamaterials (ZIMs), in which both the permittivity and permeability are set to zero, eliminate these strong reflections and have recently been demonstrated at optical frequencies using metal-based fishnet structures $^{11}$ . However, fishnet metamaterials do not have isotropic optical properties, and the use of metals inevitably introduces ohmic loss that will limit the thickness of the material.

Resonant all-dielectric metamaterials offer one potential solution to these issues[22-24]. Formed from high-refractive-index resonators, dielectric metamaterial unit cells support an electric and magnetic dipole response due to Mie resonances. Proper control of the lattice arrangement, resonator geometry, and composition allows control over the effective permittivity and permeability of the metamaterial. Because of the absence of ohmic loss, dielectric metamaterials can be much less absorptive than their metallic counterparts, and their simple unit-cell geometries offer the

possibility to achieve three-dimensional isotropic metamaterials $^{25}$ , a task that has proven challenging when utilizing more complicated metal-based unit cells $^{21}$ . However, while magnetic modes in high-index particles have recently been characterized experimentally at optical frequencies $^{26,27}$ , implementations of dielectric metamaterials have so far been limited to the microwave $^{25,28,29}$  and mid-infrared regimes $^{30}$ .

Here, we report the first experimental demonstration of an all-dielectric ZIM operating at infrared frequencies. The design of the metamaterial is based on a recent proposal reported in ref. 10 in which it was shown that a metamaterial made of purely dielectric high-index rods can exhibit a Dirac cone at the  $\Gamma$  point in the band structure, a feature that is similar to the electronic band structure in graphene $^{31}$ . At the Dirac point, the metamaterial exhibits zero effective permittivity and permeability, resulting in an impedance-matched ZIM. Experiments at microwave frequencies have demonstrated some of the unique properties arising from an effective index of zero $^{10}$ , such as cloaking and lensing. However, a demonstration at optical frequencies has yet to be provided. Here, we implement a ZIM at optical frequencies using vertically stacked silicon rods, allowing access from free space. We demonstrate that the optical ZIM serves as an angular optical filter while also enhancing the directivity of spontaneous emission from quantum dot light sources embedded inside the structure. The experimental results, together with numerical calculations, serve as direct evidence of impedance-matched near-zero index within the metamaterial.

The fabricated ZIM consists of  $200 - \mu \mathrm{m}$  long silicon rods that support electric and magnetic resonances, and are separated by a low-index material—silicon dioxide  $(\mathrm{SiO}_2)$  (Fig. 1a). One of the consequences of low or zero index is that light will not be guided using a conventional slab waveguide, so the material must be fabricated for free-space access when metal or other reflective cladding layers cannot be utilized. To realize a free-space-accessible material, fabrication began with a multilayer stack of 11 alternating layers of  $\alpha$  Si  $(\varepsilon = 13.7$ , thickness  $= 260~\mathrm{nm})$  and  $\mathrm{SiO}_2$ $(\varepsilon = 2.25$ , thickness  $= 340~\mathrm{nm}$ ) followed by patterning and reactive ion etching (RIE) (see Supplementary Section S2 for details). In the final step, poly(methyl methacrylate) (PMMA)  $(\varepsilon = 2.23)$  was spin-coated onto the sample to fill the air gaps. Figure 1b presents a cross-section of the fabricated structure before final PMMA spin-coating, and the inset depicts a sample after spin-coating. A total of five functional layers  $(\mathrm{Si} / \mathrm{SiO}_2$  pairs) results in a metamaterial with a thickness of  $3\mu \mathrm{m}$ , about twice the free-space wavelength at the zero-index point.

The band structure corresponding to the bulk ZIM (infinitely thick), consisting of a stack of square-cross-section silicon rods

![](images/8ac7d7c3e77bb5e912f71aa91c7d8972121b534b2d54400cd5aded51116dcb22.jpg)  
#

![](images/aa42ef60c08946b6c78e1f6d567159fa2f8a2ec1e22c53fa88f5a36def39b391.jpg)  
Figure 1 | Diagram and images of fabricated ZIM structure. a, Diagram of the ZIM structure with a unit-cell period of  $a = 600 \mathrm{~nm}$  and  $w = t = 260 \mathrm{~nm}$ . b, False-colour focused ion beam image of the ZIM before spin-coating PMMA. Inset: cross-section of the structure after PMMA filling. The fabricated sample has 11 alternating  $\mathrm{Si} / \mathrm{SiO}_2$  layers with silicon rod widths of  $270 \mathrm{~nm}$ ,  $280 \mathrm{~nm}$ ,  $310 \mathrm{~nm}$ ,  $320 \mathrm{~nm}$  and  $380 \mathrm{~nm}$ , from top to bottom.  
b

embedded in  $\mathrm{SiO}_2$  with  $w = t = 260\mathrm{nm}$  and  $a = 600\mathrm{nm}$  (Fig. 1a), is shown in Fig. 2a. The band structure is computed for transverse-magnetic (TM) polarization with the electric field oriented along the rod axis, and the Dirac cone-like dispersion can be observed at the centre of the Brillouin zone where two transverse bands with linear dispersion intersect a flat quasi-longitudinal band, resulting in triple degeneracy. We utilized field averaging of the Bloch modes[32] to retrieve the effective bulk optical properties of the metamaterial (Fig. 2b), and simultaneous zero permittivity and permeability were obtained at the triple degeneracy frequency of  $211\mathrm{THz}$  ( $\lambda_0 = 1,422\mathrm{nm}$ ). This response is directly attributable to a linear combination of electric monopole and magnetic dipole Mie resonances within the silicon rods (Fig. 2b, inset), allowing the effective constitutive parameters to be extracted accurately using effective medium theory[33]. This was confirmed by the excellent agreement between the extracted propagation vector, acquired using field averaging, and the computed band structure around the triple degeneracy point. A relatively broadband impedance-matched low-index region is present around the zero-index point, and over the frequency range  $215 - 225\mathrm{THz}$  there is only one propagating band, TM4. The isofrequency contours (IFCs) over this frequency range are shown in Fig. 2c, and are shown to maintain a nearly circular shape. These features, combined with the fact that only the fundamental mode is excited within this region, allow us to define a relatively isotropic effective index of refraction for the structure for TM-polarized light over this bandwidth (see Supplementary Section S1 for further details regarding

homogenization of the material). This all-angle response is critical for preserving the unique physics associated with low- or zero-index materials, such as directionally selective transmission and emission from within the material. It should be noted that in a perfectly homogeneous zero-index metamaterial, the flat longitudinal band is not accessible with TM-polarized light. However, due to finite spatial dispersion, this band becomes quasi-longitudinal in our case and is accessible at off-normal angles of incidence. As can be seen from Fig. 2a, the band bends down and is accessible for off-normal incidence at frequencies at and below the Dirac point (extended states of the crystal are provided in Supplementary Fig. S1b). In this frequency region, a refractive index cannot be assigned for off-normal incidence, and directionally selective transmission is not preserved.

Although these bulk parameters are used as a design guide, the fabricated metamaterial has both a finite thickness and nonuniform rod sizes, and will thus deviate somewhat from the bulk parameters. To better understand the optical response of the fabricated metamaterial, full-wave finite-difference time-domain (FDTD) simulations were performed, and S-parameter retrieval[34,35] was used to compute the effective optical properties (Fig. 3a,b). Because of the non-uniform rod size, the impedance-matched point in the fabricated structure is shifted to  $1,400\mathrm{nm}$ , corresponding to  $n_{\mathrm{eff}} = \mu_{\mathrm{eff}} = \varepsilon_{\mathrm{eff}} = 0.12$ . It can also be observed that a metallic region is opened from  $1,432\mathrm{nm}$  to  $1,457\mathrm{nm}$  in which the permittivity is negative but the permeability remains positive. The metamaterial exhibits a negative-index region beginning at  $1,457\mathrm{nm}$ , although this region cannot be assigned with optical properties for arbitrary angles of incidence due to the presence of the quasi-longitudinal band that is accessible at large incident angles.

To gauge the agreement with the simulated material properties, the transmittance of the fabricated ZIM was acquired by illuminating the sample with normal-incident white light with the electric field oriented along the silicon rod axis (Fig. 3c). The simulated and measured transmittance show excellent agreement in spectral shape, although the experimentally obtained curve has a lower amplitude, probably due to non-uniformity in the rod width at the edges of the sample as well as surface roughness. The measured spectrum shows a peak transmission of  $80\%$  at  $1,409~\mathrm{nm}$ , the spectral position corresponding to the impedance-matched low-index point. A dip in transmission also occurs at  $1,460~\mathrm{nm}$ , corresponding to the metallic region of the sample.

One of the most fascinating properties of isotropic low-index materials is that light incident from free space is only transmitted

![](images/a1a9cabd29b86c83c6401aabad4a9274fff3f74cc84712f286c198acc7864c0c.jpg)

![](images/84ccc858f5c7b0438d5f1191228caa8d81edd1a16a885eb2fb34c2d833c25a45.jpg)

![](images/a9df2d1da4d9735046f498f8ba0979327dce5029c948bb4c5b4c1b687a49d823.jpg)  
Figure 2 | Optical properties of bulk ZIM. a, Band diagram of uniform bulk ZIM (infinitely thick) for TM polarization. Dirac cone dispersion is observed at the  $\Gamma$  point with triple degeneracy at 211 THz. The shaded area denotes regions outside the free-space light line. b, Retrieved effective permittivity and permeability of the bulk ZIM acquired using field-averaging. Inset: electric and magnetic fields within a single unit cell at zero-index frequency, indicating a strong electric monopole and magnetic dipole response. c, IFC of the TM4 band. The contours are nearly circular (that is, isotropic) for a broad frequency range and increase in size away from the zero-index frequency, indicating a progressively larger refractive index.

![](images/521b1772bd7babe7eb161bb36a3a71ed22fe2f55fb485fc15bae1a86c2e7d125.jpg)  
Figure 3 | Optical properties and transmittance of fabricated ZIM. a, Effective permittivity and permeability of the fabricated ZIM obtained using S-parameter retrieval. Regions corresponding to positive index, metallic properties and negative index are denoted by blue, grey and yellow shading, respectively. b, Effective refractive index of the fabricated structured obtained using S-parameter retrieval. c, Experimental (red) and theoretical (dotted blue) transmittance curves of the ZIM (total pattern area,  $200 \times 200 \mu \mathrm{m}^2$ ).

![](images/8b11d712841c1044e471653be3ee0f5324c30435cf8877d0236dac9dd20126a2.jpg)

![](images/652e46904e7f94a843ad76e49b1a09d7f851fda469726d775aebffd6ecce9153.jpg)

![](images/aed3a60b6bf20d89f31104e3c1ca54cdba33ce1a7e507fd04eb4608ca27a6d52.jpg)  
a

![](images/f054ae86642bc789bed7f7d5ae7227a938e11d4533091e1c04deb22aaea280b0.jpg)

![](images/c1a2466795840f92353c28196d52833c0143df2cc03113343a7be662bcf33799.jpg)  
c

![](images/62b64edd648b0653ba8ce65720716235a923379531a3454b1ef03f8efcb23440.jpg)  
d  
Figure 4 | Angular selectivity of transmission. a, IFCs of air and a low-index metamaterial, illustrating angularly selective transmission due to conservation of the wave vector parallel to the surface. b, Simulated angle- and wavelength-dependent transmittance of the fabricated structure. c-f, Fourier-plane images of a beam passing through the fabricated ZIM structure within the low-index band. Angularly selective transmission can be observed in the y-direction due to the low effective index. Along the x-direction, angular selectivity is not preserved due to the one-dimensional nature of silicon rods. g, Fourier-plane image of the illumination beam demonstrating uniform intensity over the measured angular range.

![](images/f85313079e3cb56548ce26adf0d2fc3e92fdb8d61d4a0f4462c8e69582a20a2e.jpg)  
e

![](images/b327bd02d83d61dd94581267066cdf8f30ec30d2491f349e30105d43f6b4cd15.jpg)  
f

![](images/0861ad5393ec1d1690733cda15a2cf8dffb7116ce3262a2b830a25cd9849267e.jpg)  
g

over a narrow range of incidence angles. This effect is a direct consequence of phase-matching at the interface, which requires that the wave vector along the interface be conserved. As illustrated with the IFCs depicted in Fig. 4a, in a low-index metamaterial, the wave vector is restricted to extremely small values, causing light incident at high angles  $(k_{y,0} > |k_{\mathrm{ZIM}}|)$  to be reflected while near-normal incident light is transmitted  $(k_{y,0} < |k_{\mathrm{ZIM}}|)$ . This effect is evident when examining the simulated transmittance versus wavelength and angle of incidence (Fig. 4b) for the fabricated ZIM. The material exhibits near-zero transmission at an off-normal incident angle within the positive index band centred at  $1,400~\mathrm{nm}$ , with improving angular confinement in transmission as we approach the zero-index

point. The presence of the quasi-longitudinal band within the negative-index region  $(\lambda_0\approx 1,475\mathrm{nm})$  is also apparent, allowing transmission at large incident angles.

To verify experimentally that the fabricated ZIM preserves these features, light transmitted through the sample was imaged in the Fourier plane. Illumination was provided by a femtosecond synchronously pumped optical parametric oscillator (Coherent, MIRA OPO) that was focused with a large-numerical-aperture objective  $(\mathrm{NA} = 0.85)$ , providing incident angles up to  $58.2^{\circ}$ . The acquired Fourier images (Fig. 4c-g) show confinement of light along the  $y$ -axis of the material, which is in the direction of in-plane periodicity. Within the low-index region between

![](images/91c14dea2e11ed16b7b36c36a1244987ca510127165154c93f73a7b7d8832eee.jpg)

![](images/55f01a87615fbfffe0e92a840530011bda3f7dbc01ab336660625ef2493000a0.jpg)

![](images/e08aa97c8fd6e7caf576912c31a39492addc0b5a6239e141500368788b0267d6.jpg)

![](images/9a18ed06ed9ccd62c92f3aafca8fd9da26fbaedb5b2bd5a4001f52787a9e040a.jpg)

![](images/b843da38cdce67608f1db7c8c7c6e3d2cfd2c3e043bb80828c1e9be7deed342b.jpg)  
Figure 5 | Directional quantum dot emission from within the ZIM. a, Schematic of laser-pumped quantum dot emission from within the ZIM structure. b, Calculated emission profile for a line source placed in the cell of the material (centred) and the average profile from line sources placed throughout the material (averaged). c, Two-dimensional Fourier-plane image of quantum dot emission on the substrate. Intensity is scaled by a factor of two. d, Cross-section of the emission taken at  $k_{x} = 0$ . e, Two-dimensional Fourier-plane image of quantum dot emission within the ZIM, showing enhanced rate and directivity of spontaneous emission. f, Cross-section of the emission taken at  $k_{x} = 0$ . CCD, charge-coupled device.

![](images/01032a21b5eeeee5b39053c332f7421dbf26656482d64ef86c3791bf60661d51.jpg)

$1,400\mathrm{nm}$  and  $1,475\mathrm{nm}$ , tighter confinement of  $k_{y}$  is observed with progressive lowering of the refractive index, in agreement with the simulated data. Confinement is absent in the  $x$ -direction due to the fact that the electric field is no longer directly along the rod axis for these incident angles. The directional filtering of transmission demonstrates that a nearly isotropic low index for TM-polarized light is indeed preserved within the fabricated metamaterial.

An additional consequence of the near-zero spatial phase change is that incoherent isotropic emitters placed within the ZIM will tend to emit coherently in the direction normal to the air-ZIM interface $^{14-16}$ . To demonstrate this effect, we first simulated the emission from a line source placed both in the centre of the material as well as sources distributed throughout the volume of the material, emitting at a free-space wavelength of  $\lambda_0 = 1,425~\mathrm{nm}$  (Fig. 5b). Both emission profiles are confined to an overall angular spread of  $10^{\circ}$  and are not sensitive to the position of the emitter. The two small side lobes at  $-60^{\circ}$  and  $60^{\circ}$  are due to scattering from the corners of the metamaterial, an effect associated with having a material with finite area. For experimental demonstrations, we placed PbS semiconductor quantum dots within the ZIM to act as the emitter. The quantum dots had a luminescence peak centred at  $1,420~\mathrm{nm}$  and a full-width at half-maximum of  $172~\mathrm{nm}$ . The quantum dots were sandwiched between two PMMA layers within the ZIM, and were excited with a tightly focused  $1,064~\mathrm{nm}$  laser beam (see Supplementary Section S3 for emission spectrum and fabrication procedure). The Fourier-plane images (Fig. 5c-f) from both an unstructured PMMA/quantum dot film and quantum dots placed within the

metamaterial show good angular confinement in the  $y$ -direction and an over twofold increase in intensity emitted normal to the interface from the ZIM compared to the unstructured sample. The increase in emission normal to the interface is a result of the uniform phase distribution within the ZIM leading to constructive interference from emitters throughout the material<sup>12</sup>, further supporting the realization of a near-zero refractive index. The constructive interference of multiple emitters is in competition with the reduced optical density of states associated with the low-index response. For instance, if the number of emitters is reduced to one, the emitted power in air will be greater than the ZIM in all directions. However, as expected for constructive interference within the material, the far-field intensity of waves propagating normal to the interface is proportional to the number of emitters squared (Supplementary Section S1g). We also note that although the luminescence peak of the quantum dots matches the low-index band of the fabricated ZIM structure quite closely, parts of the emission fall beyond the low-index band, resulting in slightly lower angular confinement compared with the transmission data.

Here, we have experimentally demonstrated the first all-dielectric zero-index metamaterial at optical frequencies, which exhibits a nearly isotropic low-index response for a particular polarization, resulting in angular selectivity of transmission and spontaneous emission. The realization of impedance-matched ZIMs at optical frequencies opens new avenues towards the development of angularly selective optical filters, directional light sources and large-area single-mode photonic devices. Furthermore, the advent of all-dielectric optical metamaterials provides a new route to developing novel optical metamaterials with both low absorption loss and isotropic optical properties.

# Methods

Simulations. Numerical simulations were carried out with the measured permittivity value of single-layer  $\alpha$ -Si deposited on quartz. The band structure was calculated using MIT photonic bands, and the fields at the boundary of the unit cell were extracted to compute the effective optical properties via field averaging, preserving the continuity of the tangential and normal averaged field components. FDTD simulations (CST Microwave Studio) were used to calculate the complex transmission and reflection coefficients, which were then used in S-parameter retrieval. The transmittance with respect to wavelength and angle of incidence was computed with finite-element method simulations (Comsol Multiphysics).

Sample fabrication. Five functional layers of  $\alpha$ -Si (260 nm) and  $\mathrm{SiO}_2$  (340 nm) with an additional 170 nm  $\mathrm{SiO}_2$  layer (total of 11 layers) were deposited on 4-inch quartz wafers using low-pressure chemical vapour deposition. An etch mask composed of chromium was defined using electron-beam lithography, and RIE (Oxford Plasma Lab) was used to structure the multilayer film. During RIE the chemistry was adjusted with etch depth so that the alternating silicon and  $\mathrm{SiO}_2$  layers could be patterned in a single process step. To ensure that PMMA completely filled the structure, a vacuum was used to remove air bubbles, followed by soft baking. Complete filling of the PMMA was confirmed using focused ion beam cross-sectioning at multiple points in the sample.

# Received 21 January 2013; accepted 8 July 2013; published online 25 August 2013

# References

1. Shelby, R. A., Smith, D. R. & Schultz, S. Experimental verification of a negative index of refraction. Science 292, 77-79 (2001).  
2. Zhang, S. et al. Experimental demonstration of near-infrared negative-index metamaterials. Phys. Rev. Lett. 95, 137404 (2005).  
3. Shalaev, V. M. et al. Negative index of refraction in optical metamaterials. Opt. Lett. 30, 3356-3358 (2005).  
4. Valentine, J. et al. Three-dimensional optical metamaterial with a negative refractive index. Nature 455, 376-379 (2008).  
5. Choi, M. et al. A terahertz metamaterial with unnaturally high refractive index. Nature 470, 369-373 (2011).  
6. Decker, M., Klein, M. W., Wegener, M. & Linden, S. Circular dichroism of planar chiral magnetic metamaterials. Opt. Lett. 32, 856-858 (2007).  
7. Plum, E., Fedotov, V. A., Schwanecke, A. S., Zheludev, N. I. & Chen, Y. Giant optical gyroentropy due to electromagnetic coupling. Appl. Phys. Lett. 90, 223113 (2007).

8. Zhang, S. et al. Negative refractive index in chiral metamaterials. Phys. Rev. Lett. 102, 023901 (2009).  
9. Liu, R. et al. Experimental demonstration of electromagnetic tunneling through an epsilon-near-zero metamaterial at microwave frequencies. Phys. Rev. Lett. 100, 023903 (2008).  
10. Huang, X., Lai, Y., Hang, Z. H., Zheng, H. & Chan, C. T. Dirac cones induced by accidental degeneracy in photonic crystals and zero-refractive-index materials. Nature Mater. 10, 582-586 (2011).  
11. Yun, S. et al. Low-loss impedance-matched optical metamaterials with zero-phase delay. ACS Nano 6, 4475-4482 (2012).  
12. Vesseur, E., Coenen, T., Caglayan, H., Engheta, N. & Polman, A. Experimental verification of  $n = 0$  structures for visible light. Phys. Rev. Lett. 110, 013902 (2013).  
13. Adams, D. et al. Funneling light through a subwavelength aperture with epsilon-near-zero materials. Phys. Rev. Lett. 107, 133901 (2011).  
14. Enoch, S., Tayeb, G., Sabouroux, P., Guérin, N. & Vincent, P. A metamaterial for directive emission. Phys. Rev. Lett. 89, 213902 (2002).  
15. Ziolkowski, R. Propagation in and scattering from a matched metamaterial having a zero index of refraction. Phys. Rev. E 70, 046608 (2004).  
16. Alù, A. Silveirinha, M., Salandrino, A. & Engheta, N. Epsilon-near-zero metamaterials and electromagnetic sources: tailoring the radiation phase pattern. Phys. Rev. B 75, 155410 (2007).  
17. Silveirinha, M. & Engheta, N. Tunneling of electromagnetic energy through subwavelength channels and bends using  $\varepsilon$ -near-zero materials. Phys. Rev. Lett. 97, 157403 (2006).  
18. Bravo-Abad, J., Joannopoulos, J. D. & Soljacic, M. Enabling single-mode behavior over large areas with photonic Dirac cones. Proc. Natl Acad. Sci. USA 109, 9761-9765 (2012).  
19. Hao, J., Yan, W. & Qiu, M. Super-reflection and cloaking based on zero index metamaterial. Appl. Phys. Lett. 96, 101109 (2010).  
20. Boltasseva, A. & Atwater, H. A. Low-loss plasmonic metamaterials. Science 331, 290-291 (2011).  
21. Soukoulis, C. M. & Wegener, M. Past achievements and future challenges in the development of three-dimensional photonic metamaterials. Nature Photon. 5, 523-530 (2011).  
22. Lewin, L. The electrical constants of a material loaded with spherical particles. Proc. Inst. Elec. Eng. Part 3 94, 65-68 (1947).  
23. O'Brien, S. & Pendry, J. B. Photonic band-gap effects and magnetic activity in dielectric composites. J. Phys. Condens. Matter 14, 4035-4044 (2002).  
24. Zhao, Q., Zhou, J., Zhang, F. & Lippens, D. Mie resonance-based dielectric metamaterials. Mater. Today 12, 60-69 (2009).  
25. Zhao, Q. et al. Experimental demonstration of isotropic negative permeability in a three-dimensional dielectric composite. Phys. Rev. Lett. 101, 027402 (2008).  
26. Kuznetsov, A. I., Miroshnichenko, A. E., Fu, Y. H., Zhang, J. & Luk'yanchuk, B. Magnetic light. Sci. Rep. 2, 492 (2012).

27. Shi, L., Tuzer, T. U., Fenollosa, R. & Meseguer, F. A new dielectric metamaterial building block with a strong magnetic response in the sub-1.5-micrometer region: silicon colloid nanocavities. Adv. Mater. 24, 5934-5938 (2012).  
28. Peng, L. et al. Experimental observation of left-handed behavior in an array of standard dielectric resonators. Phys. Rev. Lett. 98, 157403 (2007).  
29. Popa, B-I. & Cummer, S. Compact dielectric particles as a building block for low-loss magnetic metamaterials. Phys. Rev. Lett. 100, 207401 (2008).  
30. Ginn, J. et al. Realizing optical magnetism from dielectric metamaterials. Phys. Rev. Lett. 108, 097402 (2012).  
31. Novoselov, K. S. et al. Two-dimensional gas of massless Dirac fermions in graphene. Nature 438, 197-200 (2005).  
32. Tsukerman, I. Effective parameters of metamaterials: a rigorous homogenization theory via Whitney interpolation. J. Opt. Soc. Am. B 28, 577-586 (2011).  
33. Wu, Y., Li, J., Zhang, Z.-Q. & Chan, C. Effective medium theory for magnetodielectric composites: beyond the long-wavelength limit. Phys. Rev. B 74, 085111 (2006).  
34. Chen, X., Grzegorczyk, T. & Wu, B. Robust method to retrieve the constitutive effective parameters of metamaterials. Phys. Rev. E 70, 016608 (2004).  
35. Smith, D. R., Vier, D. C., Koschny, T. & Soukoulis, C. M. Electromagnetic parameter retrieval from inhomogeneous metamaterials. Phys. Rev. E 71, 036617 (2005).

# Acknowledgements

This work was funded by the Office of Naval Research (programmes N00014-11-1-0521 and N00014-12-1-0571) and the United States-Israel Binational Science Foundation (programme 2010460). A portion of this research was conducted at the Center for Nanophase Materials Sciences, which is sponsored at Oak Ridge National Laboratory by the Scientific User Facilities Division, Office of Basic Energy Sciences, US Department of Energy. The authors thank N. Lavrik for discussions regarding RIE processing.

# Author contributions

P.M. fabricated the metamaterials and both P.M. and Y.Y. conducted the numerical simulations and experimental characterization. Z.A. assisted in measuring transmission as a function of incident angle. I.I.K. assisted in developing the electron-beam lithography and RIE processes and D.P.B. performed the low-pressure chemical vapour deposition. The idea was developed by J.V., who assisted in all aspects of the work and supervised the project. All authors discussed the results and contributed to writing the manuscript.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to J.V.

# Competing financial interests

The authors declare no competing financial interests.