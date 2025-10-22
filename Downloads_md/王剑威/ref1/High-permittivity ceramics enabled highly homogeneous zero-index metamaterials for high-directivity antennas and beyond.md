# RESEARCH ARTICLE

# Open Access

# High-permittivity ceramics enabled highly homogeneous zero-index metamaterials for high-directivity antennas and beyond

![](images/92c6f212e71ae7043f96c86c5161a2d417ce55cab970c0fb22634c325815ae62.jpg)

Yueyang Liu $^{1\dagger}$ , Tian Dong $^{1\dagger}$ , Xu Qin $^{2}$ , Weijia Luo $^{3}$ , Ning Leng $^{4}$ , Yujing He $^{1}$ , Yong Yuan $^{1}$ , Ming Bai $^{4*}$ , Jingbo Sun $^{3*}$ , Ji Zhou $^{3*}$ , Yue Li $^{2*}$  and Yang Li $^{1*}$

# Abstract

Zero-index metamaterials (ZIMs) can support uniform electromagnetic field distributions at any frequency, but their applications are hampered by the ZIM's homogenization level—only 3 unit cells per free-space wavelength, which is fundamentally limited by the low-permittivity inclusions  $(\varepsilon_{\mathrm{r}} \approx 12)$  and background matrix  $(\varepsilon_{\mathrm{r}} \approx 1)$ . Here, by filling high-permittivity  $\mathrm{SrTiO}_3$  ceramic  $(\varepsilon_{\mathrm{r}} \approx 294)$  pillars in  $\mathrm{BaTiO}_3$ $(\varepsilon_{\mathrm{r}} \approx 25)$  background matrix, we demonstrate a highly homogeneous microwave ZIM with an over threefold increase in the homogenization level. Leveraging such a ZIM, we achieve not only an antenna, approaching the fundamental limit in the directivity with outstanding scalability, but also a concave lens with a focal length of as short as  $1\lambda_0$ . Our highly homogeneous ZIM has profound implications in ceramics, ZIM-based waveguides and cavities, free-space wavefront manipulation, and microwave quantum optics, and opens up enormous possibilities in wireless communications, remote sensing, global positioning satellites, etc.

Keywords Zero-refractive index, Metamaterials, Antenna

Yueyang Liu and Tian Dong contributed equally to this work.

*Correspondence:

Ming Bai

mbai@buaa.edu.cn

Jingbo Sun

jingbosun@mail.tsinghua.edu.cn

Ji Zhou

zhouji@tsinghua.edu.cn

Yue Li

lyee@tsinghua.edu.cn

Yang Li

yli9003@mail.tsinghua.edu.cn

$^{1}$  State Key Laboratory of Precision Measurement Technology and Instruments, Department of Precision Instrument, Tsinghua University, Beijing 100084, China  
$^{2}$  Department of Electronic Engineering, Tsinghua University, Beijing 100084, China  
<sup>3</sup> State Key Laboratory of New Ceramics and Fine Processing, School of Materials Science and Engineering, Tsinghua University, Beijing 100084, China  
<sup>4</sup>The School of Electronic and Information Engineering, Beihang University, Beijing 100191, China

# 1 Introduction

Electromagnetic (EM) metamaterials are artificial composites that can achieve EM properties that are unavailable or hard to find in nature via structural engineering [1-3]. To date, EM metamaterials have demonstrated several extreme EM properties, such as a zero refractive index. Zero-index metamaterials (ZIMs) can provide uniform EM fields at almost any frequency. As a result, ZIMs can be applied in high transmission waveguides with arbitrary shapes [4-8], coherent perfect absorbers [9], free-space cloaks [10], electromagnetic void space [11], waveguide crosstalk prohibition [12], measurements of sub-diffraction-limit displacements [13], direction-independent phase matching for nonlinear optics [14], large-area single-mode photonic crystal surface-emitting lasers (PCSELs) [15, 16], and extended super-radiance for many emitters over a large area [17].

According to the definition of the refractive index  $n = \sqrt{\varepsilon\mu}$ , we can obtain a ZIM via  $\varepsilon$  near zero (ENZ) medium,  $\mu$  near zero (MNZ) medium, or  $\varepsilon$  and  $\mu$  near

zero (EMNZ) medium. Based on the definition of the intrinsic impedance  $Z = \sqrt{\mu / \varepsilon}$ , ENZ and MNZ media show infinite and zero impedance, respectively, resulting in an impedance mismatch to regular media with a finite impedance. In contrast, EMNZ medium depicts a finite impedance, leading to a good impedance match to regular media. EMNZ medium is typically achieved via photonic crystals [18] or doped ENZ medium [19]. Doped ENZ medium usually shows high ohmic losses because it generally achieves ENZ based on metal or metal dioxide near plasma frequencies. In contrast, photonic crystal-based ZIMs are usually obtained via purely dielectric structures, thus eliminating ohmic losses.

Photonic crystal-based ZIMs develop EMNZ behavior via Dirac-like cone (DC) dispersion at the center of the Brillouin zone. Ideally, such a DC should appear at a free-space wavelength  $\lambda_0$ , which is much longer than the lattice constant, to achieve a highly homogeneous DC-based ZIM (DCZIM) that has a performance similar to that of a bulk material. However, due to the limited permittivities of the inclusion and background matrix of DCZIMs, the DC usually appears at  $\lambda_0$ , which is approximately 3 times the lattice constant. Such a limitation leads to a large footprint of DCZIMs because they need at least  $5 \times 5$  unit cells to show an effective zero-index behavior [20]. Furthermore, this large footprint hampers the performance of many DCZIM-based devices, such as the compactness of ZIM-based waveguides, the mode area of zero-index waveguides for nonlinear optics, the minimum single-mode area of PCSELs, and the minimum thickness of a

hybrid cloak consisting of a DCZIM covered with a carefully designed metasurface [10].

In this work, we synthesized a ceramic— $\mathrm{SrTiO_3}$ —with a microwave relative permittivity  $\varepsilon_{\mathrm{r}}$  of over 290 considering the loss-permittivity balance and our synthesis technique. By fabricating a square array of  $\mathrm{SrTiO_3}$  pillars in a  $\mathrm{BaTiO_3}$  background matrix, we can develop a DCZIM (Fig. 1a). This metamaterial's lattice constant is one tenth of the free-space wavelength, which satisfies the effective medium condition [21] that leads to high homogeneity. By fully leveraging this metamaterial's highly uniform in-phase radiation in the near field, we can develop a high-directivity antenna even when its aperture size (size of radiation surface) is smaller than the operating wavelength. This antenna has various applications in wireless communications, remote sensing, and global positioning satellites. Other than antenna, we can also develop a DCZIM-based concave lens with an ultrashort focal length. Beyond antennas and lenses, our highly homogeneous ZIM can be used for various fundamental research and potential applications, including ultracompact zero-index waveguides and cavities [22], ultrathin free-space zero-index cloaks [10], and high-performance superconducting quantum computing [23].

# 2 Results and discussion

# 2.1 Zero-index metamaterial

For a homogeneous metamaterial with exotic effective constitutive parameters, the lattice constant  $a$  and the geometric size of its inclusion  $\delta$  must satisfy  $\frac{\max(a,\delta)}{\lambda_0} > 0.01$ , where  $\lambda_0$  is the free-space wavelength [21].

![](images/81d6eae32b5e7871bf6d770e487589b7492d11008e26d4965ca7d1a9124845df.jpg)  
Fig. 1 Schematic and electric field distribution of zero-index materials. a Schematic diagram of the ZIM with a high out-of-plane radiation directivity under TM excitation. The pitch, radius and height of the metamaterial are  $a$ ,  $r$  and  $h$ , respectively. Electric field phase distributions over the cross sections of b a conventional  $5a \times 5a$  2D ZIM with an inclusion relative permittivity equal to 13.8; c a bulk zero-index material based on the Lorentz model; d the same ZIM as in b whose size is approximately one operating wavelength; and e a 2D ZIM whose inclusion and background matrix permittivities are 294 and 25, respectively

![](images/a26a7f2794475284b2c70c9477a5ccad1c15b4742f68bc43d26e4caa8f510f6b.jpg)

![](images/1b41247061fc88f86a52dcab9d2b73e9e8ebca057ca18292af93017d57252178.jpg)  
Phase of  $E_{\mathrm{c}}$  (rad)

![](images/bf9a1fed408315ed618f8db9cc82f29d7a561ec770d2cd11824daf0dee0780fe.jpg)

![](images/bb370ec9939484987354d8fa682aedff182f40a14e129ed3a29927bfe29612e2.jpg)

Such a criterion requires that  $a$  and  $\delta$  have to be sufficiently large so that the metamaterial can exhibit extreme constitutive parameters in the anomalous dispersion regime. This condition can usually be satisfied by engineering the unit-cell structure of a metamaterial. Furthermore, the homogenization criterion  $\frac{\max(a,\delta)}{\lambda_0} < 0.2$  limits the upper bound of  $a$  and  $\delta$ , leading to a metamaterial behaving as a homogeneous bulk medium with effective constitutive parameters. However, this homogenization criterion is generally challenging to satisfy because it requires a high-permittivity inclusion and background matrix to achieve anomalous dispersion in the long wavelength regime. Such high-permittivity materials are usually unavailable [24] in nature.

As a purely dielectric EMNZ metamaterial, DCZIMs usually do not satisfy the homogenization criterion because typical DCZIMs are made by  $\mathrm{Al_2O_3}$  ( $\varepsilon_{\mathrm{r}} = 10$ ) pillars in an air matrix in the microwave regime [18] and silicon pillars ( $\varepsilon_{\mathrm{r}} = 12$ ) in a polymer matrix in the near-infrared regime [25]. These inclusions and matrices' low permittivities result in an  $a / \lambda_0$  from 0.3 to 0.5, thus significantly restricting the homogenization level. Such a large  $a / \lambda_0$  limits the minimum surface area of DCZIM to  $2.5\lambda_0\times 2.5\lambda_0$  because DCZIM needs a surface area larger than  $5a\times 5a$  (Fig. 1b) to behave as a bulk zero-index medium (Fig. 1c). This limitation restricts the performance of DCZIM-based devices, including the compactness of supercouplers [18, 26], aperture size of DCZIM-based antennas [27], thickness of free-space cloaks [10], mode area of zero-index waveguides for nonlinear optics [14], and radiation area of photonic crystal surface emitting lasers [15, 16]. If we increase the  $\varepsilon_{\mathrm{r}}$  of the inclusion from 12.25 to 294 and the background matrix from 1 to 25, we can achieve a highly homogeneous DCZIM even over a surface area of  $\lambda_0\times \lambda_0$  (Fig. 1d,

e, Additional file 1: Sec. S1), leading to great potential in improving the performance of DCZIM-based devices.

To achieve highly homogeneous DCZIMs, we synthesized and characterized high-permittivity  $\mathrm{SrTiO_3}$  ceramics [28]. To achieve high permittivity, we fabricated the components of  $\mathrm{SrTiO_3}$  ceramics by the solid-state method with binder (see "Methods"). Then, we used the syntonic cavity method to characterize the microwave permittivity of the  $\mathrm{SrTiO_3}$  sample [29], showing a nearly dispersiveless  $\varepsilon_{\mathrm{r}}$  from 292 to 294 and a loss tangent from  $9\times 10^{-4}$  to  $1.45\times 10^{-3}$  at frequencies of  $5 - 8\mathrm{GHz}$ . To determine the crystal structure of the  $\mathrm{SrTiO_3}$  ceramic compounds, we performed X-ray diffraction (XRD) measurements. As shown in Fig. 2a, the XRD pattern is consistent with cubic perovskite  $\mathrm{SrTiO_3}$  (JCPDS: 35-0734), revealing that the main crystal phase of all the ceramics is  $\mathrm{SrTiO_3}$ . Furthermore, the scanning electron microscopy (SEM) results show that the polished  $\mathrm{SrTiO_3}$  sample with a mean grain size of  $3 - 8\mu \mathrm{m}$  features good densification (Fig. 2b).

By using high-permittivity  $\mathrm{SrTiO_3}$  as an inclusion and  $\mathrm{BaTiO_3}$ $(\varepsilon_{\mathrm{r}} = 25)$  as the background matrix, we designed a highly homogeneous DCZIM in the microwave regime. By engineering the geometric parameters of a DCZIM consisting of  $\mathrm{SrTiO_3}$  pillars embedded in a  $\mathrm{BaTiO_3}$  matrix (Fig. 1a, Additional file 1: Sec. S2 and S3), we can obtain a DC dispersion for the fundamental transverse magnetic (TM) mode at the center of the Brillouin zone at  $6.1\mathrm{GHz}$  (Fig. 3a). This dispersion corresponds to the fact that the effective refractive index crosses zero linearly at  $6.1\mathrm{GHz}$  with a near-zero refractive index  $(|\mathrm{Re}(n_{\mathrm{eff}})| < 0.1)$  bandwidth of  $\sim 0.1\mathrm{GHz}$  corresponding to a relative impedance of approximately 3 (relative to free space) (Fig. 3b). Such a DCZIM shows a homogenization level as high as

![](images/0fa508be194ac3f9d968420d98a4a8afb876999714410621cb8b6897e289fe6d.jpg)  
Fig. 2 Material properties of  $\mathrm{SrTiO_3}$  ceramics. a XRD result and b SEM image of  $\mathrm{SrTiO_3}$  ceramics

![](images/1d755fa6bed9d72b0c5677b759e30c17819432a393ba1c54a2d1c7607aa5b48f.jpg)

![](images/0ebe87c2db174d98bb0c2bb158a83947945c7fc914d6bd2bf65389c443b0d0b7.jpg)

![](images/ad669d5e1fa824476497db70f4a54a3f7aabf6a5e64993a95ff1c5a083e4db10.jpg)

![](images/b5bbfae10a664a07a82f4fc70f26b45e94636e915b68f0ba44edf19fa31f817c.jpg)  
Fig. 3 Simulated optical properties of ZIM. a Photonic band structure of the ZIM for TM modes. b The effective refractive index and relative impedance of ZIM. c Electric field distribution over the cross section of the ZIM. d The radiation rate of the ZIM, featuring a maximum radiation rate of approximately 6.1 GHz

![](images/9a0fd322bc62ac350008a9795794acece960d74c816b562104d5be6a4403aa44.jpg)

$a / \lambda_0\approx 0.1$  due to the high permittivities of the inclusion and background matrix (Additional file 1: Sec. S4). As a result of this high homogenization level, this DCZIM features a highly uniform electric field distribution over its cross section (Fig. 3c). To achieve a DCZIM-based antenna with a high gain, we fine-tune the height of the  $\mathrm{SrTiO}_3$  pillars to engineer the quality factor of the dipole mode, which forms the DC and behaves as an out-of-plane radiation channel that achieves a high out-of-plane radiation rate near the zero-index frequency of  $\sim 6.1$  GHz (Fig. 3d, Additional file 1: Sec. S5).

We experimentally fabricated and measured our design of a highly homogeneous DCZIM. We fabricated the metamaterial by placing  $\mathrm{SrTiO_3}$  pillars in a  $\mathrm{BaTiO_3}$  matrix that was polished by mechanical milling (Fig. 4a). We retrieved the effective constitutive parameters of the metamaterial sample from the experimentally measured transmission and reflection coefficients [30]. As shown in Fig. 4b, the measured  $\varepsilon_{\mathrm{r}}^{\mathrm{eff}}$  and  $\mu_{\mathrm{r}}^{\mathrm{eff}}$  show good agreement

with those calculated from the simulated transmission and reflection coefficients. Both measured and simulated  $\varepsilon_{\mathrm{r}}^{\mathrm{eff}}$  and  $\mu_{\mathrm{r}}^{\mathrm{eff}}$  cross zero simultaneously and linearly at approximately 6.1 GHz, corresponding to an impedance-matched zero index. To further validate the zero-index behavior of the metamaterial, we simulated and experimentally measured the near field over the top surface of the metamaterial (Additional file 1: Sec. S6). As shown in Fig. 4c, d, both the simulated and measured near fields show that the wave propagates through the metamaterial with nearly zero phase advance. To the best of our knowledge, this is the first demonstration of a DCZIM satisfying the rigid homogenization criterion [21].

# 2.2 From conventional antennas to ZIM-based antenna

Directivity—the ratio of antenna's radiation intensity along a certain direction to that of an isotropic radiator—is the most important parameter for characterizing an antenna's radiation property [31].

![](images/47edae1ef8a28d9a21356067e3581f1b033f2cdbbbb903aa252edbf0072e7b62.jpg)

![](images/22ac0724d370eb761ce9bc3f0b1aba364760282885f00e09b752f466e8fefce1.jpg)

![](images/ea5d4c115e57bb9f1e353aed915779a81e6134653b12699ac7bea869091962d2.jpg)  
Fig. 4 Experimental and simulated results of ZIM. a Photograph of the ZIM sample with two taper waveguides as input and output. b Simulated and measured effective relative permittivity and permeability. c, d Simulated and measured near-field distributions over the top surface of the ZIM

![](images/255a6debfd85fb4112943eb759958861694af0b39b25150019848f0d568870e2.jpg)

![](images/0428927129271ee5eddb2635a9f1cdac2276499f6f46dd1bfad6b8cc7e19d801.jpg)  
Fig. 5 Electric field phase distributions and far-field radiation patterns of a patch antenna, a zero-index medium-based antenna, and a DCZIM-based antenna. a The nonuniform spatial phase distribution over the patch antenna results in a low directivity. b, c The uniform spatial phase distributions over the zero-index medium and DCZIM lead to high directivities

![](images/8b4fd83dc5405e60bb63eb80fd0b742f2cec5ade71a974b4a2ab5a26547239b0.jpg)

![](images/695be02963ad61046dec538c2e569e3bb97617f43ed5f50004f455fb596d3fae.jpg)

High-directivity antennas are desirable for many applications such as remote sensing. However, directivity of conventional antennas is usually limited by the nonuniform spatial phase distribution over the radiation aperture (Fig. 5a). Here, we propose to achieve a highdirectivity antenna by harnessing the uniform spatial

phase distribution over a zero-index medium (Fig. 5b). Such an antenna can achieve a high directivity regardless of its aperture size, approaching the fundamental limit in antenna directivity [32]. To achieve this antenna, we need a highly homogeneous metamaterial (Figs. 1a, e, 5c) which can show zero-index behavior over a wide range of

![](images/2d521b50c0afad7481035ce47f02f77e541b0fc91ade2a9d2f95ac08be1f49ba.jpg)  
b

![](images/dddc04770103e4d7b27f81dce1a6c0dc20bad4f6e90e80266ea9015c9e860d9a.jpg)

![](images/db88a611f10d7194d973162f583ed551ee309df899e0670b5a73d6478e5d9440.jpg)  
Directivity (dB)

![](images/5dcc93cfa8a212bfd51176e6f916f334b102840e0454a8c69f8dc9ac0b284a7e.jpg)  
d  
C

![](images/67b409775fd6aeea48d86819d114181edf6e8cbcb189e4a17223423c9166aa24.jpg)

![](images/5c5849e81a9c072d96bd8c2a626de2857eb6bede2f168439215fc344bcc94950.jpg)

![](images/c4876feedda5ce6495f4e1a16464b7be5bdf9be80b7ed7019ad49536cddc7fbc.jpg)  
f  
Fig. 6 Experimental and simulated results of the DCZIM-based antenna. a Photograph of the DCZIM-based antenna. b Simulated far-field directivity pattern of the DCZIM-based antenna in a. c, d Simulated and measured directivity patterns in the  $E$  -plane and  $H$  -plane. e Measured  $S_{11}$  of the DCZIM-based antenna. f Comparison of simulated and measured directivities of DCZIM-based antennas and those of dielectric antennas with the calculated directivity limits

sizes from deep subwavelength scale to a scale of many wavelengths.

# 2.3 Zero-index metamaterial-based high-directivity antenna

To fully leverage the high homogeneity of our DCZIM, we designed a high-directivity DCZIM-based antenna with an aperture size varying from the subwavelength

![](images/79c5e6fa5d90f04ce9f170b73522c92900f1f47e42464b0646c46a1119f02d9b.jpg)  
Fig. 7 Photograph, simulated and experimental results of a DCZIM-based concave lens. a Photograph of the DCZIM-based concave lens sample. b measured field, c simulated field intensity in the near-field region over the top surface of the concave lens sample. Black circles indicate the positions of  $\mathrm{SrTiO_3}$  pillars

![](images/4a8a6050640ac14d9c56663ca679f6691365632de3d92b4e25eac5ea80209e7b.jpg)

![](images/829d160afd11304e7361a0c250542c324e5dd0eefa65121a8b9bc7444635f28e.jpg)

scale to a very large scale. As shown in Fig. 6a, this antenna consists of a DCZIM embedded in a metallic rectangular waveguide with the upper surface open, serving as the radiation aperture. To improve the homogeneity along the  $y$ -axis, we designed perfect magnetic boundary conditions for the TM modes along the  $y$ -axis, which are equivalent to periodic boundary conditions (Additional file 1: Sec. S7). This antenna is excited in the direction parallel to the plane of the  $\mathrm{SrTiO_3}$  pillars array. Along this direction, good impedance matching can be achieved because of the finite impedance of DCZIM along this direction (Fig. 3b). To match the tangential momentum of the EM wave at the interface between the upper surface of the DCZIM and the air, the EM wave radiates out of the DCZIM along the axis direction of the  $\mathrm{SrTiO_3}$  pillars. Such radiation shows a high directivity because of the uniform distribution of the EM field over the upper surface of the DCZIM (Fig. 4c, d). Furthermore, this high directivity remains as long as the aperture size is larger than  $5a\times 5a$  ( $0.5\lambda_0\times 0.5\lambda_0$ ), enabling a high directivity antenna with an aperture size from the subwavelength scale to a very large scale (Additional file 1: Sec. S8 and S9). Hence, our antenna can approach the fundamental limit with regards to the antenna directivity when the aperture size varies from  $0.5\lambda_0\times 0.5\lambda_0$  to a very large scale [31].

We experimentally fabricated and tested a DCZIM-based antenna. We designed a tapered waveguide to achieve fundamental TM mode excitations for the DCZIM-filled waveguide (Fig. 6a). Such a tapered waveguide, on the other hand, is connected to a rectangular waveguide input by a microwave source. To test this DCZIM-based antenna's directivity, we fabricated an antenna with an aperture size of  $12a \times 12a$  ( $1.2\lambda_0 \times 1.2\lambda_0$ ), featuring a high directivity in the far field (Fig. 6b) by harnessing the in-phase radiation over its aperture (Fig. 4c, d). As shown in Fig. 6c, d, the measured directivity patterns show good agreement with those computed by

full-wave simulations in both the  $E$ -plane ( $y-z$  plane in Fig. 6a) and  $H$ -plane ( $x-z$  plane in Fig. 6a). Both the experimental and simulation results feature a maximum directivity of approximately  $11.2\mathrm{dB}$ . We confirmed that this high directivity is induced by the DCZIM rather than the waveguide itself or the high-permittivity ceramic-filled waveguide by comparing the directivities of the DCZIM-based antenna, waveguide, and high-permittivity ceramic-filled waveguide (Additional file 1: Sec. S10). To test the overall impedance-matching performance of the DCZIM-based antenna, we measured its reflection coefficient (Fig. 6e), showing a valley of  $-35\mathrm{dB}$  near the operating frequency of  $6.1\mathrm{GHz}$ . Finally, as a rational comparison between our antenna's directivity and the fundamental limit of the directivity [31], we simulated the directivities of 8 DCZIM-based antennas with aperture sizes varying from  $0.8\lambda_0\times 0.8\lambda_0$  to  $1.5\lambda_0\times 1.5\lambda_0$ .

To demonstrate the performance of DCZIM-based antenna, we compare its directivity with those of dielectric antennas whose working principle is similar to that of DCZIM-based antenna [35-40]. As shown in Fig. 6f, measured directivities of all the antennas support the fact that directivity increases as aperture size increases. When the aperture size is smaller than  $2.4\lambda_0^2$ , only a multilayered cubic antenna [37] and a DCZIM-based antenna with an aperture size of  $0.6\lambda_0^2$  show directivities higher than the directivity limitation. However, the multilayered cubic antenna's aperture size is not scalable. In contrast, our DCZIM-based antenna can always approach the fundamental limit of the directivity when the aperture size varies from  $0.4\lambda_0^2$  to  $2.4\lambda_0^2$  (Additional file 1: Sec. S11).

To demonstrate the wave manipulation capability of our ZIM, we made a DCZIM-based concave lens (Fig. 7a). As shown in Fig. 7b, c, both simulation and measurement results show that the spatial phase is uniformly distributed over the ZIM, leading to the spherical output wavefront determined by the concave output boundary of the ZIM. Such a spherical wavefront forms a clear focal

point, demonstrating the focusing ability of this DCZIM-based lens whose focal length is as short as  $1\lambda_0^2$ . Such a small concave lens is enabled by the high homogeneity of our ZIM. In addition to antenna, our DCZIM can also achieve applications in cloaking by embedding air holes inside the ZIM (Additional file 1: Sec. S12).

# 3 Conclusion

We synthesized high-permittivity ceramic  $\mathrm{SrTiO_3}$  with a microwave relative permittivity over 290. Based on this ceramic, we designed, fabricated, and characterized a highly homogeneous ZIM in the microwave regime. Such a ZIM consists of a square array of  $\mathrm{SrTiO_3}$  pillars in a  $\mathrm{BaTiO_3}$  background matrix, showing an impedance-matched zero index at  $6.1\mathrm{GHz}$ . By taking advantage of the high permittivity of the inclusion and background matrix, this ZIM features a homogenization level of  $a / \lambda_0\approx 0.1$ , which is over 3 times higher than that of the state-of-the-art ZIM. This ZIM could boost the performance of several ZIM-based devices, such as the compactness of ZIM-based waveguides with arbitrary shapes, the thickness of free-space cloaks, and the complexity of the object that can be shielded by cloak. We proposed and demonstrated a high-directivity antenna by incorporating our ZIM into a metallic waveguide. This antenna can achieve a directivity as high as  $11.2\mathrm{dB}$  with an aperture size as small as  $1.2\lambda_0\times 1.2\lambda_0$ . Moreover, our antenna can achieve a high directivity when its aperture size varies from  $0.5\lambda_0\times 0.5\lambda_0$  to a very large scale, enabling it to approach the fundamental limit of the antenna directivity in a large range of aperture sizes. In comparison with dielectric antennas, our DCZIM-based antennas depict comparable directivities and a better scalability. This DCZIM-based antenna has broad applications in wireless communications, remote sensing, and global positioning satellites. Other than antenna, we also realized a DCZIM-based concave lens showing a focal length as short as  $1\lambda_0$ . Beyond antennas and lenses, our highly homogeneous DCZIM has profound implications in ceramics, ZIM-based waveguides and cavities, free-space wavefront manipulation, and microwave quantum optics. Moreover, DCZIM can also achieve negative and positive effective indices, which can be applied in several fields including wavefront engineering [33], imaging, and sensing [34].

# 4 Methods

# 4.1 Synthesis

The  $\mathrm{SrTiO_3}$  ceramic was synthesized by solid state method. This ceramics samples were prepared by a conventional mixed-oxide route starting from high-purity  $\mathrm{SrCO_3}$  and  $\mathrm{TiO_2}$  powder. The powders were mixed in a cyclohexanol suspension for  $1\mathrm{h}$ , ball milled for  $3\mathrm{h}$  and

subsequently calcined at  $1050^{\circ}\mathrm{C}$  for  $18\mathrm{h}$ . The synthesized powders were then uniaxially pressed into cylinders, which were sintered at  $1375^{\circ}\mathrm{C}$  for  $6\mathrm{h}$  and then at  $1100^{\circ}\mathrm{C}$  for  $4\mathrm{h}$ .

# 4.2 Simulations

The complex permittivities of  $\mathrm{SrTiO_3}$  used in our numerical simulations are measured by using syntonic cavity method. We computed the photonic band structure by using 3D finite-elements method (FEM) simulation software COMSOL. We computed complex reflection and transmission coefficients and far-field radiation patterns using 3D FEM simulation software Ansys HFSS. We computed the complex reflection and transmission coefficients, field distributions over the cross section of the metamaterial by using finite difference time domain (FDTD) simulation software Ansys Lumerical. To get the complex reflection and transmission coefficients, we extracted the reflected and transmitted electric fields at two points prior to the source and after the metamaterial, respectively.

# Supplementary Information

The online version contains supplementary material available at https://doi.org/10.1186/s43593-023-00059-x.

Additional file 1: Section.1: Comparison of antennas based on low- and high-homogenization level DCZIMs Figure S1. The near field distributions of  $E_{z}$  and radiation patterns of the alumina DCZIM-based antenna and  $\mathrm{SrTiO_3}$  DCZIM-based antenna. Section.2: Metamaterial design. Figure S2. Real part of the effective refractive index  $\mathrm{Re}(n_{\mathrm{eff}})$  of a 2D DCZIM as a function of pitch and radius at the design frequency of 6.1 GHz. Section.3: Robustness of geometric parameters against fabrication imperfections. Figure S3. Transmission coefficient  $S_{21}$  of DCZIM-based antenna as a function of the operating frequency and radius  $r$ . Section.4: Homogenization. Figure S4. Comparison of band structures of the DCZIM. Figure S5. Comparison of the phase of the electric field of a DCZIM and that of homogenized zero-index bulk medium. Figure S6. Imaginary parts of the effective relative permittivity and permeability. Section.5: Radiation characteristic and beam steering performance. Figure S7. The radiation properties of the electric monopole mode and the transverse magnetic dipole mode. Figure S8. E-plane directivity patterns as a function of radiation angle for various excitation frequencies. Section.6: Measurement of near field. Figure S9. The schematic diagram of the photo-induced plasma scanning method. Section.7: Perfect magnetic conductor (PMC) boundary condition. Figure S10. Perfect magnetic conductor (PMC) boundary condition for DCZIM. Section.8: Impedance matching between DCZIM-based antenna and free space. Figure S11. Simulation of impedance of ZIM along the out-of-plane direction. Section.9: Gain. Figure S12. Simulation of propagation losses of rectangular waveguide and taper waveguide Figure S13. Simulation of propagation loss of DCZIM. Figure S14. Simulated E-plane directivity patterns of DCZIM-based antennas with various aperture sizes. Figure S15. Simulated E-plane gain patterns of DCZIM-based antennas with various aperture sizes. Section.10: Control simulations. Figure S16. Control simulations of open-ended rectangular waveguides filled with different materials. Section.11: Scalability and directivity. Figure S17. Simulated and measured radiation patterns of DCZIM-based antennas with aperture sizes of  $0.8\lambda_0\times 0.8\lambda_0$  and  $1.4\lambda_0\times 1.4\lambda_0$ . Section.12: Applications of DCZIM in cloaking. Figure S18. Photograph, simulated and experimental results of ZIM-based cloak.

# Acknowledgements

The  $\mathrm{BaTiO_3}$  was synthesized by Shenzhen Oling Microwave Co., Ltd. The authors would like to acknowledge Shahin Firuzi and Qihua Xiong for discussion and Ziheng Zhou for the guidance of measuring the radiation patterns of antennas.

# Author contributions

Several people contributed to the work described in this paper. YangL and YueL conceived the basic idea for this work. YLiu and YY conducted the FDTD simulations. YLiu and TD conducted the FEM simulations. WL synthesized the  $\mathrm{SrTiO_3}$ . YLiu fabricated the metamaterial and antenna. YLiu measured the transmission and reflection coefficients of the metamaterial. NL and YLiu measured the near fields of the metamaterial. XQ, and YLiu measured the radiation patterns of the antenna. MB supervised the measurement of the near fields of the metamaterial. JS and JZ supervised the synthesis of  $\mathrm{SrTiO_3}$ . YueL supervised the measurement of the radiation patterns of antenna. YangL supervised the research and the development of the manuscript. YLiu, TD, and YangL wrote the first draft of the manuscript; all authors subsequently took part in the revision process and approved the final copy of the manuscript.

# Funding

This work was supported by the National Key Research and Development Program of China (2021YFB2801600), National Natural Science Foundation of China (62075114), Beijing Natural Science Foundation (4212050, Z220008), and Zhuhai Industry University Research Collaboration Project (ZH-22017001210108PWC).

# Availability of data and materials

The datasets used and/or analysed during the current study are available from the corresponding author on reasonable request.

# Declarations

# Competing interests

The authors declare that they have no competing interests.

Received: 19 July 2023 Revised: 12 November 2023 Accepted: 18 November 2023

Published online: 05 February 2024

# References

1. N. Engheta, R.W. Ziolkowski, Metamaterials: Physics and Engineering Explorations (Wiley, Hoboken, 2006)  
2. W. Cai, V. Shalaev, Optical Metamaterials: Fundamentals and Applications (Springer, Cham, 2010)  
3. G.V. Eleftheriades, K.G. Balmain, Negative-Refraction Metamaterials: Fundamental Principles and Applications (Wiley, Hoboken, 2005)  
4. J. Luo, W. Lu, Z. Hang, H. Chen, B. Hou, Y. Lai et al., Arbitrary control of electromagnetic flux in inhomogeneous anisotropic media with near-zero index. Phys. Rev. Lett. 112(7), 073903 (2014)  
5. M. Silveirinha, N. Engheta, Tunneling of electromagnetic energy through subwavelength channels and bends using epsilon-near-zero materials. Phys. Rev. Lett. 97(15), 157403 (2006)  
6. J. Luo, Y. Lai, Anisotropic zero-index waveguide with arbitrary shapes. Sci. Rep. 4(1), 5875 (2014)  
7. J. Luo, P. Xu, H. Chen, B. Hou, L. Gao, Y. Lai, Realizing almost perfect bending waveguides with anisotropic epsilon-near-zero metamaterials. Appl. Phys. Lett. 100(22), 221903 (2012)  
8. W. Ji, J. Luo, Y. Lai, Extremely anisotropic epsilon-near-zero media in waveguide metamaterials. Opt. Express 27(14), 19463-19473 (2019)  
9. J. Luo, B. Liu, Z.H. Hang, Y. Lai, Coherent perfect absorption via photonic doping of zero-index media. Laser Photonics Rev. 12(8), 1800001 (2018)

10. H. Chu, Q. Li, B. Liu, J. Luo, S. Sun, Z.H. Hang et al., A hybrid invisibility cloak based on integration of transparent metasurfaces and zero-index materials. Light Sci. Appl. 7(1), 50 (2018)  
11. C. Xu, H. Chu, J. Luo, Z.H. Hang, Y.Wu, Y. Lai, Three-dimensional electromagnetic void space. Phys. Rev. Lett. 127(12), 123902 (2021)  
12. W. Ji, J. Luo, H. Chu, X. Zhou, X. Meng, R. Peng et al., Crosstalk inhibition at the deep-subwavelength scale by epsilon-near-zero claddings. Nanophotonics 12(11), 2007-2017 (2023)  
13. G. Dong, Z. Li, J. Zhou, P. Qiao, X. Yang, X. Meng, Precise displacement measurement in single-beam interferometry employing photonic metamaterial with effective zero-index. Opt. Express 25(25), 31509-31515 (2017)  
14. J.R. Gagnon, O. Reshef, D.H.G. Espinosa, M.Z. Alam, D.I. Vulis, E.N. Knall et al., Relaxed phase-matching constraints in zero-index waveguides. Phys. Rev. Lett. 128(20), 203902 (2022)  
15. S.-L. Chua, L. Lu, J. Bravo-Abad, J.D. Joannopoulos, M. Soljačić, Larger-area single-mode photonic crystal surface-emitting lasers enabled by an accidental Dirac point. Opt. Lett. 39(7), 2072-2075 (2014)  
16. R. Contractor, W. Noh, W. Redjem, W. Qarony, E. Martin, S. Dhuey et al., Scalable single-mode surface-emitting laser via open-Dirac singularities. Nature 608(7924), 692-698 (2022)  
17. O. Mello, Y. Li, S.A. Camayd-Muñoz, C. DeVault, M. Lobet, H. Tang et al., Extended many-body superradiance in diamond epsilon near-zero metamaterials. Appl. Phys. Lett. 120(6), 061105 (2022)  
18. X. Huang, Y. Lai, Z.H. Hang, H. Zheng, C.T. Chan, Dirac cones induced by accidental degeneracy in photonic crystals and zero-refractive-index materials. Nat. Mater. 10(8), 582-586 (2011)  
19. I. Liberal, A.M. Mahmoud, Y. Li, B. Edwards, N. Engheta, Photonic doping of epsilon-near-zero media. Science 355(6329), 1058-1062 (2017)  
20. Y. Li, C.T. Chan, E. Mazur, Dirac-like cone-based electromagnetic zero-index metamaterials. Light Sci. Appl. 10(1), 203 (2021)  
21. C.R. Simovski, S.A. Tretyakov, Local constitutive parameters of metamaterials from an effective-medium perspective. Phys. Rev. B 75(19), 195111 (2007)  
22. I. Liberal, N. Engheta, Near-zero refractive index photonics. Nat. Photonics 11(3), 149-158 (2017)  
23. A. Blais, A.L. Grimsmo, S.M. Girvin, A. Wallraff, Circuit quantum electrodynamics. Rev. Mod. Phys. 93(2), 025005 (2021)  
24. N. Kinsey, C. DeVault, A. Boltasseva, V.M. Shalaev, Near-zero-index materials for photonics. Nat. Rev. Mater. 4(12), 742-760 (2019)  
25. P. Moitra, Y.M. Yang, Z. Anderson, I.I. Kravchenko, D.P. Briggs, J. Valentine, Realization of an all-dielectric zero-index optical metamaterial. Nat. Photonics 7(10), 791-795 (2013)  
26. P. Camayd-Muñoz, Integrated zero-index metamaterials, Doctoral dissertation, 2016  
27. M. Memarian, G.V. Eleftheriades, Dirac leaky-wave antennas for continuous beam scanning from photonic crystals. Nat. Commun. 6(1), 5855 (2015)  
28. W. Luo, X. Wang, S. Wang, X. Wang, Z. Liu, L. Li et al., Miniaturization of dielectric ceramic-based metamaterial perfect absorber. Appl. Phys. Lett. 120(1), 013502 (2022)  
29. L. Li, X. Wang, W. Luo, S. Wang, T. Yang, J. Zhou, Internal-strain-controlled tungsten bronze structural ceramics for 5G millimeter-wave metamaterials. J. Mater. Chem. C 9(40), 14359-14370 (2021)  
30. D.R. Smith, S. Schultz, P. Markos, C.M. Soukoulis, Determination of effective permittivity and permeability of metamaterials from reflection and transmission coefficients. Phys. Rev. B 65(19), 5 (2002)  
31. C.A. Balanis, Antenna Theory: Analysis and Design (Wiley, Hoboken, 2016)  
32. M. Gustafsson, M. Capek, Maximum gain, effective area, and directivity. IEEE Trans. Antennas Propag. 67(8), 5282-5293 (2019)  
33. I. Staude, J. Schilling, Metamaterial-inspired silicon nanophotonics. Nat. Photonics 11(5), 274-284 (2017)  
34. J.B. Khurgin, Expanding the photonic palette: exploring high index materials. ACS Photonics 9(3), 743-751 (2022)  
35. Y.W. Wang, G.M. Wang, B.F. Zong, Directivity improvement of vivaldi antenna using double-slot structure. IEEE Antennas Wirel. Propag. Lett. 12, 1380-1383 (2013)

36. P. Liu, S. Yang, X. Wang, M. Yang, J. Song, L. Dong, Directivity-reconfigurable wideband two-arm spiral antenna. IEEE Antennas Wirel. Propag. Lett. 16, 66-69 (2017)  
37. Y. Samura, K. Horio, V.B. Antipov, S.E. Shipilov, A.I. Eremeev, O.V. Minin et al., Characterization of mesoscopic dielectric cuboid antenna at millimeter-wave band. IEEE Antennas Wirel. Propag. Lett. 18(9), 1828-1832 (2019)  
38. C. Biancotto, P. Record, Triangular lattice dielectric EBG antenna. IEEE Antennas Wirel. Propag. Lett. 9, 95-98 (2010)  
39. J.P.Turpin, Q.Wu, D.H.Werner, B.Martin, M.Bray, E.Lier, Near-zero-index metamaterial lens combined with AMC metasurface for high-directivity low-profile antennas. IEEE Trans. Antennas Propag. 62(4), 1928-1936 (2014)  
40. P. Juyal, L. Shafai, Sidelobe reduction of TM12 mode of circular patch via nonresonant narrow slot. IEEE Trans. Antennas Propag. 64(8), 3361-3369 (2016)