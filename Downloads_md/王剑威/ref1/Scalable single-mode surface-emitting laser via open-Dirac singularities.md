# Scalable single-mode surface-emitting laser via open-Dirac singularities

https://doi.org/10.1038/s41586-022-05021-4

Received: 31 January 2022

Accepted: 23 June 2022

Published online: 29 June 2022

Check for updates

Rushin Contractor $^{1,4}$ , Wanwoo Noh $^{1,4}$ , Walid Redjem $^{1,4}$ , Wayesh Qarony $^{2}$ , Emma Martin $^{1}$ , Scott Dhuey $^{3}$ , Adam Schwartzberg $^{3}$  & Boubacar Kante $^{1,2,3}$

Single-aperture cavities are a key component of lasers that are instrumental for the amplification and emission of a single light mode. However, the appearance of high-order transverse modes as the size of the cavities increases has frustrated efforts to scale-up cavities while preserving single-mode operation since the invention of the laser six decades ago $^{1-8}$ . A suitable physical mechanism that allows single-mode lasing irrespective of the cavity size—a 'scale invariant' cavity or laser—has not been identified yet. Here we propose and demonstrate experimentally that open-Dirac electromagnetic cavities with linear dispersion—which in our devices are realized by a truncated photonic crystal arranged in a hexagonal pattern—exhibit unconventional scaling of losses in reciprocal space, leading to single-mode lasing that is maintained as the cavity is scaled up in size. The physical origin of this phenomenon lies in the convergence of the complex part of the free spectral range in open-Dirac cavities towards a constant governed by the loss rates of distinct Bloch bands, whereas for common cavities it converges to zero as the size grows, leading to inevitable multimode emission. An unconventional flat-envelope fundamental mode locks all unit cells in the cavity in phase, leading to single-mode lasing. We name such sources Berkeley surface-emitting lasers (BerkSELs) and demonstrate that their far-field corresponds to a topological singularity of charge two, in agreement with our theory. Open-Dirac cavities unlock avenues for light-matter interaction and cavity quantum electrodynamics.

Dirac points are topological singularities that have attracted enormous interest since the discovery of massless Dirac fermions governing electronic transport in graphene<sup>9</sup>. Their occurrence usually indicates an imminent topological transition, and they are at the heart of the physics of topological insulators<sup>10</sup>. In general, wave systems that have a band structure, such as photonic crystals (PhCs)<sup>11,12</sup>, also exhibit Dirac cones (DCs) and it has been demonstrated that DCs are universal features that can be systematically implemented by controlling the symmetry of the structure<sup>13,14</sup>. In photonics, DCs have mostly been utilized to demonstrate effective zero-index materials and their properties or to control the dispersion of polaritons<sup>15-20</sup>. Recently, a DC implemented using a three-dimensional structure was theoretically proposed to enable large-area single-mode lasing<sup>21,22</sup>. However, the proposed mechanism relied on changes in the real part of the frequency spacing of the cavity modes that increases by an amount much smaller than the typical gain bandwidth of semiconductors and is thus insufficient to enable single-mode operation in lasers. Moreover, all observed modes exhibited oscillatory wavefunctions.

Surface-emitting lasers have had a fundamental role in science and technology since the invention of lasers<sup>1</sup>, the demonstration of distributed feedback lasers<sup>2</sup> and the invention of vertical cavity surface-emitting lasers<sup>3</sup>. However, scaling the cavity aperture has been

a challenge. Here we report a room-temperature scalable open-Dirac lasing cavity that exploits the linear dispersion of photons near the band edge of a PhC, and that can be scaled to large sizes. Our proposed structure is presented in Fig. 1a. It is a PhC with a hexagonal lattice. The unit cell of the PhC is shown in the inset of Fig. 1b. The linear dispersion of Fig. 1c is obtained for a laterally infinite structure ( $x-y$  direction) by overlapping doubly degenerate modes of the  $\mathrm{E}_2$  irreducible representation with a singly degenerate mode of the  $\mathrm{B}_1$  irreducible representation from the  $C_{6\nu}$  point group at the  $\Gamma$  point of the Brillouin zone $^{13,14}$  (Supplementary Information). The degeneracy of the modes is obtained for a critical radius of holes  $r_{\mathrm{Dirac}}$ . An open-Dirac cavity, shown in Fig. 1, is formed by truncating the infinite PhC as a hexagon around a central air-hole with edges normal to the M directions of the lattice. The entire cavity is suspended in air, and it is connected to the main membrane by six bridges at the corners of the hexagon for mechanical stability (Fig. 1a,b). The structure is fabricated using electron-beam lithography and the PhC is defined by inductively coupled plasma etching, followed by a wet-etching step to create the suspended membrane (Supplementary Information).

Three modes are involved in the formation of the DC. The coupling between the B and E modes is direction dependent and one of the E modes forms a flat band as seen in Fig. 1c. Therefore, the interaction

![](images/427570418ec9330aac61cf61ae2ffbd64b7ad63a14edbae284fd36272eb2d643.jpg)  
Fig. 1 | Scalable open-Dirac electromagnetic cavity and the Berkeley surface-emitting laser. a, Top-view scanning electron micrograph of a hexagonal lattice PhC that is truncated to form an open-Dirac electromagnetic cavity. The free-standing structure is suspended by six bridges connecting the main membrane to the substrate along the  $\Gamma$ -K direction. The cavities are fabricated using electron-beam lithography, inductively coupled plasma etching and wet etching (Supplementary Information). b, Tilted view of the cavity showing two bridges, the array of holes and the PhC-air boundary. The thickness of the membrane is  $200\mathrm{nm}$ , the period of the crystal is  $1,265\mathrm{nm}$  and the radius of the holes is used to tune cavities around the Dirac singularity. The inset shows the quality of the nanofabrication with near-perfect circular air-hole interfaces. c, Dispersion of the structure showing a conical degeneracy

![](images/d1858f191837256cffa599b5cf066d41c04dbe3d43a8f9271d00e4aeebaea0f4.jpg)

![](images/c68c34861ff7954213f98567f9b553cf2c6235f2a66ec40438345740a773d376.jpg)

between the B and E modes detuned in frequency by  $\varepsilon$  can be expressed in a simplified form by the Hamiltonian

$$
H = \left( \begin{array}{c c} 0 & \beta k \\ \beta k & \epsilon \end{array} \right), \tag {1}
$$

where  $k$  is the Bloch momentum and  $\beta$  is a coupling constant. As  $\varepsilon \rightarrow 0$ , the eigenfrequencies of  $H$  form bands with a linear dependence on  $k$ . Moreover, the eigenvectors of  $H$  are mixed and the orthogonal modes B and E are transformed into an admixture of  $\mathrm{B} \pm \mathrm{E}$  as we move away from  $k = 0$ . When a system with the interaction Hamiltonian  $H$  is truncated to a finite cavity, the linear bands break up into discrete modes. This idea is demonstrated in Fig. 2a where the dispersion of the PhC at  $r_{\mathrm{Dirac}}$  is overlain on the discrete cavity modes. The colour of these modes indicates the purity of the eigenvector. We observe that when we are close to the Dirac singularity, only the fundamental mode at the  $\Gamma$  point is purely B. Higher-order modes originating from both the B and E bands consist of an admixture of fields from both these bands. The separation between modes  $\delta_k \approx \pi / D$  is governed by the length of the cavity  $D$ . The finite size of the cavity also introduces an uncertainty in the momentum space  $\sigma_k$ . We further note that no pure E mode at the  $\Gamma$  point exists owing to the six-fold rotational symmetry of the cavity. The E modes have only two-fold rotational symmetry and hence a fundamental mode that is spread across the entire cavity cannot originate from the E band. The presence of the corners also eliminates feedback along the K direction of the Brillouin zone and high-quality-factor  $(Q)$  modes are supported only along the M direction. The five lowest-order modes are computed for a cavity with  $D = 51a$  (where  $a$  is the size of the unit cell) and presented in Fig. 2a labelled as  $|0\rangle$  to  $|4\rangle$  with mode  $|0\rangle$  being the fundamental mode.

The linear dispersion around the open-Dirac singularity means that the fundamental mode effectively sees zero refractive index. This means that, unlike the fundamental mode of conventional PhC cavities that have a Gaussian envelope, the fundamental mode in our open-Dirac cavity with hexagonal boundaries has a flat envelope for all cavity sizes. This is confirmed in Fig. 2b for open-Dirac cavities of sizes  $D = 19a$ ,  $D = 35a$  and  $D = 51a$ . Such a mode locks all the resonators at the surface of the laser (aperture) in phase regardless of the size of

at  $193.5\mathrm{THz}$  for hole radii of  $r_{\mathrm{Dirac}} = 273\mathrm{nm}$ . The blue sheet corresponds to the frequency of the B mode and the red sheets correspond to the E modes. The truncation of the crystal, which opens the DC, is notably chosen to be more favourable for the B mode compared with the E modes. The iso-frequency contours, projected on the  $(k_x,k_y)$  plane, are sketched together with a representation of laser emission originating from the Dirac point.  $\hbar$  is the reduced Planck constant and  $\omega$  is the angular frequency. The inset shows the Brillouin zone. d, Schematic of a Berkeley surface-emitting laser (BerkSEL) illustrating the pump beam (blue) and the lasing beam (red) from an unconventional open-Dirac cavity mode that synchronizes all unit cells (or resonators) in phase. Therefore, all unit cells in the aperture participate in the lasing mode.

the cavity. The flatness of the envelope means that emission from the edge scales as the perimeter whereas emission from the surface scales as the area. The scaling of the higher-order modes can be understood by extending equation (1) for finite systems. Considering the first three modes, the eigenfrequencies for a finite cavity can be obtained by diagonalizing

$$
\left( \begin{array}{c c c} - \sigma_ {k} + j \gamma_ {\mathrm {B}} & 0 & 0 \\ 0 & - \sigma_ {k} + j \gamma_ {\mathrm {B}} & \beta \delta_ {k} \\ 0 & \beta \delta_ {k} & \epsilon + \sigma_ {k} + j \gamma_ {\mathrm {E}} \end{array} \right) \binom {| 0 \rangle_ {\mathrm {B}}} {| 1 \rangle_ {\mathrm {B}}} = \boldsymbol {\Omega} (D) \binom {| 0 \rangle | | 1 \rangle | | 2 \rangle |, \tag {2}
$$

where the subscripts B and E on the left-hand side indicate the pure nature of the modes and  $\gamma_{\mathrm{B}}$  and  $\gamma_{\mathrm{E}}$  are the loss rates for the B and E modes induced by the boundaries of the cavity, respectively.  $j$  is the imaginary number.  $\Omega (D)$  is a diagonal matrix with elements representing the complex eigenfrequencies of the finite cavity (Supplementary Information). As the dispersion of the B and E bands has an opposite sign, the uncertainty in momentum caused by the finite size will shift the frequencies of the two bands in opposite directions. Thus,  $\sigma_{k}$  has an opposite sign for the modes originating from the B band than for the modes originating from the E band.

To demonstrate the validity of this model, we computed the modes of open-Dirac cavities of different sizes and for hole radii  $(r)$  smaller than, equal to and greater than the critical radius  $r_{\mathrm{Dirac}}$ . It is noted that we present only the first three modes of the cavities as modes of higher order have a lower  $Q$ . The computation was performed using a three-dimensional finite-element solver for the transverse-electric polarization, which corresponds to the polarization providing the highest gain for the multiple quantum wells used in our work. Figure 3a-c (markers) presents the computed frequency shifts of the first three cavity modes. The frequency shifts are computed by comparing cavity modes to the frequency of the B mode at the  $\Gamma$  point for an infinite membrane with holes of the same radius. Figure 3d-f (markers) shows the scaling of  $Q$  of the same three modes with increasing cavity sizes. The solid lines are obtained by fitting the simulation data with equation (2). When the radius of the holes is not close to  $r_{\mathrm{Dirac}}$ , cavity mode |1> asymptotes to the frequency of the fundamental mode at a

![](images/c076de195d2892fc8a1569007eb73192c72fe67cdbce8239a5dd01ab7c3c0c51.jpg)  
Fig. 2 | Quantization of the band structure in open-Dirac cavities forming higher-order modes and evidence for an unconventional fundamental mode with a flat envelope. a, Cavity modes on the dispersion of the unit cell (dashed lines), presented in colour to indicate the mixing of the B and E bands. The fundamental mode at the  $\Gamma$  point is the only purely B mode (cyan). Higher-order modes (copper) are photonic admixtures of the B and E bands and thus demonstrate a different scaling than the fundamental mode. The blur around cavity modes indicates the uncertainty in the momentum  $\sigma_{k}$  owing to the finite size of the cavity, and the spacing between the modes is the momentum imparted by the cavity  $\delta_{k}$ . The cavity provides greater feedback

![](images/ac3e24e63844e34a5b3aa6f232c4cfd7ce302e1b799a108bd99da598cb6c2c08.jpg)

![](images/edc0c9efbbf1977fe76263b66a51271519d7ac0436077d99689d562a1827879b.jpg)  
along the M direction and linear dispersion causes modes to be equispaced in frequency. The electric-field intensity of the five lowest-order modes for a cavity of size  $D = 51a$  (where  $a$  is the size of the unit cell) is shown on the right. b, Phase of the out-of-plane component of the magnetic field (sampled at the same point in each unit cell along the diagonal of the cavity) and magnitude of the electric field (averaged over each unit cell along the diagonal of the cavity) for cavities of sizes  $D = 19a$ ,  $D = 35a$  and  $D = 51a$ . The fundamental mode  $|0\rangle$  has an unconventional flat envelope for all cavity sizes. A zoom-in view of the field distribution in unit cells is presented in Supplementary Information.

rate of  $D^{-2}$ . This is shown in Fig. 3g along with the scaling for  $r_{\mathrm{Dirac}}$ , in which case the separation increases and scales at a rate of  $D^{-1}$ . It is noted that cavity mode  $|1\rangle$  flips from being at a lower frequency than the fundamental mode for  $r < r_{\mathrm{Dirac}}$  to a greater frequency than the fundamental mode for  $r > r_{\mathrm{Dirac}}$ . We also observe that even for the cavity with linear dispersion, the frequency separation rapidly drops to about a terahertz when the diameter of the aperture reaches  $D = 31a$  (Supplementary Information). The gain spectrum of semiconductors and notably the quantum wells on which the devices were fabricated, spans almost 100 THz, which is much larger than real mode spacing. The selectivity of the lasing mode can thus not be enabled by the scaling of the frequency shift afforded by linear dispersion alone as initially claimed[21-23].

We now investigate  $Q$  of our proposed open-Dirac cavities, with a hexagonal truncation. As previously discussed, the truncation of the cavity serves as selector of the fundamental mode  $|0\rangle$ , shown by circles on solid lines in Fig. 3. Cavity mode  $|1\rangle$  and cavity mode  $|2\rangle$  are denoted by square and triangle markers, respectively in Fig. 3a-f. Figure 3d-f (markers) shows that, as expected,  $Q$  of all the modes increases with the size. We also observe that  $Q$  of the fundamental mode  $(Q_0)$  decreases as the radius of the air-holes increases. This can be attributed to a decrease in the average refractive index of the membrane, which reduces the confinement of light. Analogous to the scaling of frequency, we observe that  $Q$  of cavity mode  $|1\rangle$  asymptotes to  $Q_0$  when  $r$  is detuned from  $r_{\mathrm{Dirac}}$  (Fig. 3d  $(r < r_{\mathrm{Dirac}})$  and Fig. 3f  $(r > r_{\mathrm{Dirac}})$ ). Surprisingly, when cavities are tuned to the Dirac point  $(r = r_{\mathrm{Dirac}})$  higher-order modes do not asymptote to the fundamental mode anymore, as seen in Fig. 3e. They lose energy at a rate always higher than the fundamental mode. Unlike the normalized real free spectral range that still decays quickly with the size (Fig. 3g), the normalized imaginary free spectral range maintains a non-decaying value despite

increasing cavity sizes (Fig. 3h). The loss rates of the modes scale with the size of the cavity as  $\gamma_{i} = c_{i}D^{-1} + d_{i}D^{-2}$  (Supplementary Information), where  $i = \mathrm{B}$  or E, and  $c_{i}$  and  $d_{i}$  are loss rates introduced owing to effects of the boundaries. As the  $C_6$  symmetry of the cavity is more favourable for the B band, we find that  $d_{\mathrm{E}} > d_{\mathrm{B}}$  and  $c_{\mathrm{E}} > c_{\mathrm{B}}$ . Moreover, as cavity modes  $|1\rangle$  and  $|2\rangle$  are formed from an admixture of both the B and the E modes, when  $\varepsilon \rightarrow 0$  their loss rate is dominated by  $\gamma_{\mathrm{E}}$ . Hence, for  $D\to \infty$ , the normalized complex free spectral range tends towards a non-vanishing value of  $1 - \frac{c_{\mathrm{B}}}{c_{\mathrm{E}}}\approx 0.8$ . Theoretical results, plotted in Fig. 3a-h as continuous lines, are in perfect agreement with numerical simulations (markers). The imaginary free spectral range in open-Dirac cavities is thus scale invariant. According to the Bloch theorem, cavity modes are the product of the envelopes and unit-cell wavefunctions. The flat-envelope fundamental mode (Fig. 2) and the non-vanishing complex free spectral range (Fig. 3) prevent cavity-scale and unit-cell-scale spatial hole burnings, respectively. Mixed higher-order modes means that the cross-saturation is comparable to the self-saturation[24]. Single-mode operation is thus guaranteed for scaled-up surface-emitting lasers operated around open-Dirac singularities (Supplementary Information).

To experimentally demonstrate our theory, we characterized Berkeley surface-emitting lasers (BerkSELs) of diameter  $D = 19a$  (Fig. 4a),  $D = 27a$  (Fig. 4e),  $D = 35a$  (Fig. 4i),  $D = 43a$  (Fig. 4m) and  $D = 51a$  (Fig. 4q). The cavities were optically pumped at room temperature with a pulsed laser (wavelength  $\lambda = 1,064$  nm, pulse time  $T = 12$  ns at a repetition rate  $f = 215$  kHz) and the emission from each aperture was collected through a confocal microscope optimized for near-infrared spectroscopy (Supplementary Information). The signal was directed towards a monochromator coupled to a indium-gallium-arsenide photodiode for spectral measurements. Figure 4 presents the evolution of the

![](images/14723246d14370a6cae5e849810a50caf203879d8192c881724cd8963c465fb4.jpg)

![](images/3040c0aceb9c38548c4ec541110d8f506d5398d906deb6428d08a3f231f87294.jpg)

![](images/1bc8a5de0a1120eed3e62eb9fe89070f284f4a5dd6f702c6ffd4655e5261dfe1.jpg)

![](images/ac304acd2c0ca34f00619ec4b79c89b8612471138703b91978ce3dadf656fbf4.jpg)

![](images/00f01bc31ec11f3e1248cb38fbc08d6ad86b8a31970a87c40a6619956708c974.jpg)

![](images/c7262423bb3d4381131406eb744d499dc962a9a3e111b2a9634dcc248727065f.jpg)

![](images/903f896bfdddbb8981a0554b28eb5ac7b3ed435f3e3c658485c98987474fe13c.jpg)  
Fig. 3 | Complex frequency scaling of open-Dirac electromagnetic cavities. a-c, Frequency shifts of the first three cavity modes for  $r < r_{\mathrm{Dirac}}(\mathbf{a})$ ,  $r = r_{\mathrm{Dirac}}(\mathbf{b})$  and  $r > r_{\mathrm{Dirac}}(\mathbf{c})$ , computed by comparing cavity modes to the frequency of the B mode at the  $\Gamma$  point for an infinite membrane with holes of the same radius. d-f, Quality factor of the first three cavity modes for  $r < r_{\mathrm{Dirac}}(\mathbf{d})$ ,  $r = r_{\mathrm{Dirac}}(\mathbf{e})$  and  $r > r_{\mathrm{Dirac}}(\mathbf{f})$ . g, Scaling of the frequency for various radii. When  $r$  is detuned from  $r_{\mathrm{Dirac}}$ , the dispersion is quadratic, and the frequency shift scales as  $D^{-2}$ . When  $r$  is

![](images/21f794b4fbbac299e38f3a40622fd6dd830adf45640d3f961109473c8e5f089a.jpg)  
tuned to  $r_{\mathrm{Dirac}}$ , the frequency shift scales as  $D^{-1}$ . h, Scaling of  $Q$  when the radius is detuned from  $r_{\mathrm{Dirac}}$  and when it is tuned to the singularity. For quadratic dispersion, cavities have an imaginary free spectral range that vanishes with the size of cavities. Interestingly, the normalized imaginary free spectral range does not vanish with the size for our open-Dirac cavities that can thus be scaled up in size. For all plots, the markers are numerical simulations and the continuous lines are theory based on our model.

normalized output power as a function of the wavelength and the size of the cavity for unit-cell hole radii smaller than the singular radius  $r_{\mathrm{Dirac}}$  (Fig. 4b,f,j,n,r), equal to  $r_{\mathrm{Dirac}}$  (Fig. 4c,g,k,o,s) and greater than  $r_{\mathrm{Dirac}}$  (Fig. 4d,h,l,p,t). For  $D = 19a$ , cavities are single mode for  $r < r_{\mathrm{Dirac}}$  (Fig. 4b),  $r = r_{\mathrm{Dirac}}$  (Fig. 4c) and  $r > r_{\mathrm{Dirac}}$  (Fig. 4d). For  $D = 27a$ , cavities remain single mode for  $r < r_{\mathrm{Dirac}}$  (Fig. 4f),  $r = r_{\mathrm{Dirac}}$  (Fig. 4g) and  $r > r_{\mathrm{Dirac}}$  (Fig. 4h). This is because these cavities are relatively small. However, when the size of cavities is increased to  $D = 35a$  or larger, we observe that they become multimode for  $r < r_{\mathrm{Dirac}}$  (Fig. 4j,n,r), remain single mode for  $r = r_{\mathrm{Dirac}}$  (Fig. 4k,o,s) and become multimode for  $r > r_{\mathrm{Dirac}}$  (Fig. 4l,p,t). The Dirac singularity erases higher-order modes in open-Dirac cavities and Berk-SELs remain single mode when their size is increased. It is worth noting that the uniform field profile across the aperture for the fundamental mode (Fig. 2) and the non-vanishing free spectral range (Fig. 3) depletes

gain across the aperture, making it more difficult for higher-order modes to lase. Single-mode lasing is thus maintained in BerkSELs even for near-damage-threshold pump power. BerkSELs are thus robust to size and pump power density scaling because of the non-vanishing complex free spectral range and the participation of all unit cells (or resonators) in the aperture to the lasing mode. These experiments validate our theory and make BerkSELs scale-invariant surface-emitting lasers. The apparent high threshold power density of our BerkSELs originates from surface recombination as we are directly structuring the quantum wells, and it is comparable to previously reported lasers using a similar strategy[25]. This can be alleviated by designing alternative structures or by additional chemical treatments of the devices. BerkSELs are, in principle, infinitely scalable if the proposed open-Dirac potential can be implemented exactly. In practice, considerations such

![](images/1b89c7925328ae3d1d8b068593de4506391c5e51944a0e4482632225dc4b7c9e.jpg)

![](images/953bab7e1d154c3207cce9cb6f36f49275ee85980b0bf334b0b23281c31b95f8.jpg)

![](images/4cae9b7fad6d1b126383d8709f3131690f63108e649c73c41e15f2e22e1ac68e.jpg)

![](images/856489558ceb85ed3d5af4941490851ea51f7b07b4ab0dea1b9ec737a4d24321.jpg)

![](images/d6c5020161d01ccbc6ccdd0b724b4f6348704aeb374565e12ddabfc250d28ea9.jpg)

![](images/8a6548deb1d7f8da325ea847d8930bd1693cbbdbf50a695293a55e90bc7c10fe.jpg)

![](images/8fb8f5c5401cf51b6476a55cc3354ceb4d48bc151b7024c45e00cb299426f073.jpg)

![](images/7816a38b294e8b415907fd69cd4cf3d8debd7f1322aa6f0dbd512f7f6da45dc9.jpg)

![](images/4a6d313b2e0474861f50d3ad5b30a9299710df20345c85bf7d2363f885ff2696.jpg)

![](images/ad682a247301d74f17a3d11816a247a17ad71970e5952af922bf5a82bfe9eaf3.jpg)

![](images/56712dd8a4e03230aa4427711c7d35f2c8886b0b77564cd35e4524f83fbc4b7d.jpg)

![](images/148ca1801722b368738353638cbf6f4c467d9be00f46c5b527bc59da152466b3.jpg)

![](images/fe39ebbe6bd8a51c113f1382f66a6ddd58957537603569015139a071704a50c9.jpg)

![](images/64b6bf7d4d4aa3666ea3f526875a50b0b19291ea47d2d2e7c533d64b235fd7f7.jpg)

![](images/31ba5aa9b2e4c1d98244151da479901603e704c4aa245be9793a80fab0a32b9d.jpg)

![](images/57402b93e8f21f1a16c8bc5cb4f24d0fc09fa28315b6aa1231838e1f611df3fc.jpg)

![](images/f2b4ed575bda784c754befb8661fb48d6994485a37a571c0ca5b35cd7f1af181.jpg)  
Fig. 4 | Lasing characteristics of BerkSELs erasing higher-order modes around the open-Dirac singularity. a, e, i, m, q. Top-view SEM of fabricated open-Dirac cavities of size  $D = 19a$  (a),  $D = 27a$  (e),  $D = 35a$  (i),  $D = 43a$  (m) and  $D = 51a$  (q), where  $D$  is the diameter of the aperture and  $a$  is the size of the unit cell of the PhC. Scale bars,  $25\mu m$ . b-d,f-h,j-l,n-p,r-t, Evolution of the normalized output power as a function of the wavelength and the size of the cavity for unit-cell hole radii smaller than the singular radius  $r_{\mathrm{Dirac}}$  (b,f,j,n,r), equal to  $r_{\mathrm{Dirac}}$  (c,g,k,o,s) and greater than  $r_{\mathrm{Dirac}}$  (d,h,l,p,t). The pump power density is  $1.1\mu W\mu m^{-2}$  in all cases. For  $D = 19a$ , cavities are single mode

![](images/e7edbb06f58bc151c340177113d0b04ec31c10c474216cf151c05a23abb45033.jpg)  
for  $r < r_{\mathrm{Dirac}}(\mathbf{b}), r = r_{\mathrm{Dirac}}(\mathbf{c})$  and  $r > r_{\mathrm{Dirac}}(\mathbf{d})$ . For  $D = 27a$ , cavities are single mode for  $r < r_{\mathrm{Dirac}}(\mathbf{f}), r = r_{\mathrm{Dirac}}(\mathbf{g})$  and  $r > r_{\mathrm{Dirac}}(\mathbf{h})$ . When the size is increased to  $D = 35a$ ,  $D = 43a$  and  $D = 51a$ , we observe that cavities become multimode mode for  $r < r_{\mathrm{Dirac}}(\mathbf{j}, \mathbf{n}, \mathbf{r})$ , remain single mode for  $r = r_{\mathrm{Dirac}}(\mathbf{k}, \mathbf{o}, \mathbf{s})$  and become multimode again for  $r > r_{\mathrm{Dirac}}(\mathbf{l}, \mathbf{p}, \mathbf{t})$ . The Dirac singularity erases higher-order modes in open-Dirac cavities and BerkSELs remain single mode when the size is increased. These experiments validate our theory and make BerkSELs scale-invariant surface-emitting lasers.

![](images/200443fda8393c03ce21f3bea39ab15282ed05831793eb01a2d5b448e5ac3c9a.jpg)

![](images/342c6682f1fef282c6abe4be08e0dcd10c3ff8b271a4134034bfdab3fdad0ab5.jpg)

as proximity effects in lithography, electrical injection or heat release will need to be addressed for high-power devices. Assuming typical fabrication imperfections with a variation of hole radii on the order of  $5\mathrm{nm}$ , the fundamental mode is found to be robust to disorder (Supplementary Information).

To further characterize the single-mode lasing of BerkSELs, we present in Fig. 5 the light-light curve (Fig. 5a), the second-order autocorrelation at zero-delay  $g^{2}(\tau = 0)$  (Fig. 5b) and its pulse width

(Fig. 5c). The three different regimes corresponding to spontaneous emission (blue region), amplified spontaneous emission (ASE) (yellow region) and stimulated emission (red region) are observed as the pump power is increased. The second-order autocorrelation function shows a transition from spontaneous emission to ASE as its width drops sharply and the bunching  $g^{2}(0)$  increases. The transition from ASE to stimulated emission is evident from  $g^{2}(0)$  decreasing to unity (Fig. 5b) and the width gradually increasing after the lasing threshold (Fig. 5c),

![](images/56007b7e3c8b6a630d0318bd0962873a84020d3bcbbae9f9b29bd4c1883bc40c.jpg)

![](images/5efcb2870145652002f4537996940d9482dd6d8ac9a482649f77a48236bcd526.jpg)

![](images/74847ce65cd421aa2e34788ccc9e9c81331142d8abc21275b52efe7ca94da423.jpg)  
Fig. 5 | Far-field scaling of BerkSELs and photon statistics. a, Emitted output power of a BerkSEL of aperture diameter  $D = 35a$  (where  $a$  is the size of the unit cell) as a function of the average pump power density (light-light curve). b,c, Second-order intensity autocorrelation measurements at zero-delay  $g^2(0)$  (b) and its pulse width (c). The pulse width of the second-order autocorrelation function shows a distinct transition from spontaneous emission to ASE as the width drops sharply and then from ASE to stimulated emission as the width gradually increases. These transitions unambiguously demonstrate single-mode lasing from BerkSELs. Experimental far fields (Fourier space images) of BerkSELs under optical pumping are presented for cavity sizes of

![](images/ba57ded1f16b605eecc62a8d68b9f2c350ed5acf41b74f62b87059cfcab3ba8d.jpg)

![](images/cdfbab9f720b780c0d6449e49ce5389de001dbaf124eee7765fb2fe2b576ac3c.jpg)  
$D = 11a(\mathbf{d}), D = 19a(\mathbf{e}), D = 27a(\mathbf{f}), D = 35a(\mathbf{g})$  and  $D = 51a(\mathbf{h})$ . Scale bars,  $10^{\circ}$ . (i) Measured and theoretical beam divergence angle as a function of the cavity size. The continuous line is the theoretical prediction and markers are experimental data. A good agreement is observed between theory and experiments. The inset shows the same data plotted on a log-log scale, demonstrating the  $1 / D$  scaling of the beam divergence where  $D$  is the diameter of the aperture (Supplementary Information). This scaling corresponds to the theoretical limit obtained for modes with a flat envelope fully covering an aperture (Fig. 2). Error bars indicate the standard deviation of the beam divergence.

![](images/3170ad251d0d23b7f878bb7a14964deee7c87a1b77fe0faa715a5ad714b98df7.jpg)

![](images/35aa77f5ad28aed60c5c011abddf06afefc2722f095ec6f88fdbfa9c733e6a1b.jpg)

unambiguously proving single-mode lasing action from BerkSELs $^{26,27}$ . To confirm that lasing originates from the theoretically predicted B mode (Figs. 2 and 3), experimental far fields (Fourier space images) of BerkSELs under optical pumping are presented for cavity sizes of  $D = 11a$  (Fig. 5d),  $D = 19a$  (Fig. 5e),  $D = 27a$  (Fig. 5f),  $D = 35a$  (Fig. 5g) and  $D = 51a$  (Fig. 4h). The six-fold symmetry of the beams match with the far-field obtained from simulations of finite cavities (Supplementary Information). The far fields originate from the B mode with a topological charge of two (Supplementary Information). Scaling up the cavity size manifests in a smaller beam divergence as expected. We plotted the measured beam divergence as a function of the size of the cavity. The measured beam divergence matches with our theory, and it scales as  $1 / D$  where  $D$  is the diameter of the cavity, in full agreement with theory for modes with a flat envelope fully covering an aperture. (The Regents of the University of California have filed a patent on systems, methods and applications using the principles described in this paper to control lasers and open-wave systems.) It is worth noting that BerkSELs are scalable to a large size, whereas the bound states in the continuum lasers become multimode when their size is increased, and are more suited for small-scale lasers as previously demonstrated $^{25}$ . To the best of our knowledge, there is no known laser or cavity, be it topological, polaritonic or of any other type, with the scale invariance hereby proposed and demonstrated.

We have thus demonstrated scale-invariant surface-emitting lasers that remain single mode when the size of the cavity is increased. They are based on open-Dirac singularities and are robust against size scaling. The unconventional scaling stems from a complex free spectral range that does not vanish with the size of cavities and the existence

of a flat-envelope fundamental mode that has never been predicted nor observed in a potential well. Around the open-Dirac singularity, higher-order modes are effectively suppressed by their admixture with more lossy bands of the structure. The fundamental mode with a flat envelope makes all resonators in the aperture participate in the mode. The fundamental mode thus effectively locks all unit cells (or resonators) in the aperture in phase, a long-standing challenge. Lasers based on such cavities are surface-emitting lasers that we named Berkeley surface-emitting lasers (BerkSELs). We have confirmed single-mode lasing from BerkSELs by measuring their second-order intensity correlation. We have further confirmed the lasing mode by measuring far-field emissions that agree with our theory. These results demonstrate the fundamental importance of openness and mode admixtures in reciprocal space for enabling scaling in optics, and they will have implications in linear and nonlinear classical and quantum wave-based systems, including atoms, electronics, acoustics, phononics or photonics based on real or synthetic dimensions. The simplicity of BerkSELs makes them universal lasing apertures, readily relevant to applications including virtual reality systems, lidars, interconnects, data centres, manufacturing, defence, or lasers for imaging and medicine.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-022-05021-4.

# Article

1. Schawlow, A. L. & Townes, C. H. Infrared and optical masers. Phys. Rev. 112, 1940-1949 (1958).  
2. Kogelnik, H. & Shank, C. V. Stimulated emission in a periodic structure. Appl. Phys. Lett. 18, 152-154 (1971).  
3. Soda, H., Iga, K., Kitahara, C. & Suematsu, Y. GalnAsP/InP surface emitting injection lasers. Jpn J. Appl. Phys. 18, 2329-2330 (1979).  
4. Meier, M. et al. Laser action from two-dimensional distributed feedback in photonic crystals. Appl. Phys. Lett. 74, 7-9 (1999).  
5. Imada, M. et al. Coherent two-dimensional lasing action in surface-emitting laser with triangular-lattice photonic crystal structure. Appl. Phys. Lett. 75, 316-318 (1999).  
6. Choquette, K. D., Hou, H. Q., Geib, K. M. & Hammons, B. E. Uniform and high power selectively oxidized 8x8 VCSEL array. In IEEE/LEOS Summer Topical Meetings 11-12 (IEEE, 1997).  
7. Francis, D., Chen, H.-L., Yuen, W., Li, G. & Chang-Hasnain, C. Monolithic 2D-VCSEL array with 2 W CW and 5 W pulsed output power. Electron. Lett. 34, 2132-2133 (1998).  
8. Yoshida, M. et al. Double-lattice photonic-crystal resonators enabling high-brightness semiconductor lasers with symmetric narrow-divergence beams. Nat. Mater. 18, 121-128 (2019).  
9. Novoselov, K. S. et al. Electric field effect in atomically thin carbon films. Science 306, 666-669 (2004).  
10. Haldane, F. D. M. Model for a quantum Hall effect without Landau levels: condensed-matter realization of the "parity anomaly". Phys. Rev. Lett. 61, 2015-2018 (1988).  
11. Yablonovitch, E. Inhibited spontaneous emission in solid-state physics and electronics. Phys. Rev. Lett. 58, 2059-2062 (1987).  
12. John, S. Strong localization of photons in certain disordered dielectric superlattices. Phys. Rev. Lett. 58, 2486-2489 (1987).  
13. Sakoda, K. Universality of mode symmetries in creating photonic Dirac cones. J. Opt. Soc. Am. B 29, 2770 (2012).  
14. Sakoda, K. Proof of the universality of mode symmetries in creating photonic Dirac cones. Opt. Express 20, 25181 (2012).

15. Enoch, S., Tayeb, G., Sabouroux, P., Guérin, N. & Vincent, P. A metamaterial for directive emission. Phys. Rev. Lett. 89, 213902 (2002).  
16. Huang, X., Lai, Y., Hang, Z. H., Zheng, H., & Chan, C. T. Dirac cones induced by accidental degeneracy in photonic crystals and zero-refractive-index materials. Nat. Mater. 10, 582-586 (2011).  
17. Moitra, P. et al. Realization of an all-dielectric zero-index optical metamaterial. Nat. Photon. 7, 791-795 (2013).  
18. Li, Y. et al. On-chip zero-index metamaterials. Nat. Photon. 9, 738-742 (2015).  
19. Liberal, I. & Engheta, N. Near-zero refractive index photonics. Nat. Photon. 11, 149-158 (2017).  
20. Jacqmin, T. et al. Direct observation of Dirac cones and a flatband in a honeycomb lattice for polaritons. Phys. Rev. Lett. 112, 116402 (2014).  
21. Bravo-Abad, J., Joannopoulos, J. D. & Soljacic, M. Enabling single-mode behavior over large areas with photonic Dirac cones. Proc. Natl Acad. Sci. USA 109, 9761-9765 (2012).  
22. Chua, S.-L., Lu, L., Bravo-Abad, J., Joannopoulos, J. D. & Soljacic, M. Larger-area single-mode photonic crystal surface-emitting lasers enabled by an accidental Dirac point. Opt. Lett. 39, 2072-2075 (2014).  
23. Gao, X. et al. Dirac-vortex topological cavities. Nat. Nanotechnol. 15, 1012-1018 (2020).  
24. Siegman, A. E. Lasers 466-472 (Univ. Science Book, 1986).  
25. Kodigala, A. et al. Lasing action from photonic bound states in continuum. Nature 541, 196-199 (2017).  
26. Loudon, R. The Quantum Theory of Light 3rd edn (Oxford Univ. Press, 2000).  
27. Pan, S. H., Gu, Q., El Amili, A., Vallini, F. & Fairman, Y. Dynamic hysteresis in a coherent high-  $\beta$  nanolaser. Optica 3, 1260-1265 (2016).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2022

# Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

# Code availability

The computer codes that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

Acknowledgements This research was mostly supported by the Office of Naval Research (ONR) Young Investigator Award (N00014-19-1-2737), the ONR JTO MRI Award (N00014-20-1-2752), the ONR grant N00014-20-1-2723 and the National Science Foundation (NSF) Career Award (ECCS-1929659). It was partially supported by the Laboratory Directed Research and Development Program of Lawrence Berkeley National Laboratory (LBNL) under US Department of Energy contract no. DE-AC02-05CH11231, the NSF QLCI programme through grant number OMA-2016245, the Moore Inventor Fellows programme and the Bakar Fellowship at UC

Berkeley. The work was partially performed at the UC Berkeley Marvel Nanofabrication Laboratory, the Molecular Foundry at LBNL and the San Diego Nanotechnology Infrastructure, a member of the National Nanotechnology Coordinated Infrastructure, which is supported by the National Science Foundation (ECCS-1542148). We thank M. Montero for technical assistance regarding fabrication.

Author contributions B.K. conceived the project, proposed the idea, and guided the theoretical and experimental investigations. R.C. performed the theoretical calculations. W.N. fabricated the devices. W.R. performed the measurements. W.Q., E.M., S.D. and A.S. contributed to the fabrication of the larger-size devices requested by the reviewers. All authors contributed to discussions and R.C., W.R. and B.K. wrote the manuscript.

Competing interests The Regents of the University of California have filed a patent application (US provisional application 63/304,581) on technology related to the processes described in this article.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41586-022-05021-4.

Correspondence and requests for materials should be addressed to Boubacar Kanté. Peer review information Nature thanks Alejandro Martinez and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at http://www.nature.com/reprints.