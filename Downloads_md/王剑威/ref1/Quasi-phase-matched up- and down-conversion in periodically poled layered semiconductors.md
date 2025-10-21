# Quasi-phase-matched up- and down-conversion in periodically poled layered semiconductors

Received: 2 May 2024

Accepted: 22 November 2024

Published online: 13 January 2025

![](images/366a3946988d6f25933dc764ef440546c34bb9cef2ca5bd9c327ff1b742e4508.jpg)

Check for updates

Chiara Trovatello  $^{1,2}$ , Carino Ferrante  $^{3}$ , Birui Yang  $^{4}$ , Josip Bajo  $^{5,6}$ , Benjamin Braun  $^{5,6}$ , Zhi Hao Peng  $^{1}$ , Xinyi Xu  $^{1}$ , Philipp K. Jenke  $^{5,6}$ , Andrew Ye  $^{7}$ , Milan Delor  $^{8}$ , D. N. Basov  $^{4}$ , Jiwoong Park  $^{7,9,10}$ , Philip Walther  $^{5,11}$ , Cory R. Dean  $^{4}$ , Lee A. Rozema  $^{5}$ , Andrea Marini  $^{3,12}$ , Giulio Cerullo  $^{2,13}$  & P. James Schuck  $^{1}$

Nonlinear optics lies at the heart of classical and quantum light generation. The invention of periodic poling revolutionized nonlinear optics and its commercial applications by enabling robust quasi-phase-matching in crystals such as lithium niobate. However, reaching useful frequency conversion efficiencies requires macroscopic dimensions, limiting further technology development and integration. Here we realize a periodically poled van der Waals semiconductor  $(3R - MoS_{2})$ . Owing to its large nonlinearity, we achieve a macroscopic frequency conversion efficiency of  $0.03\%$  at the relevant telecom wavelength over a microscopic thickness of  $3.4\mu \mathrm{m}$  (that is, 3 poling periods),  $10 - 100\times$  thinner than current systems with similar performances. Due to intrinsic cavity effects, the thickness-dependent quasi-phase-matched second harmonic signal surpasses the usual quadratic enhancement by  $50\%$ . Further, we report the broadband generation of photon pairs at telecom wavelength via quasi-phase-matched spontaneous parametric down-conversion, showing a maximum coincidence-to-accidental ratio of  $638\pm 75$ . This work opens the new and unexplored field of phase-matched nonlinear optics with microscopic van der Waals crystals, unlocking applications that require simple, ultra-compact technologies such as on-chip entangled photon-pair sources for integrated quantum circuitry and sensing.

The inherent nonlinear response of matter to external electromagnetic stimuli allows photons of different frequencies incident on a material to interact with each other, enabling a myriad of photonic applications such as frequency conversion and the generation of non-classical states of light. Particularly interesting are second-order nonlinear processes, which occur in non-centrosymmetric media with  $\chi^{(2)}\neq 0$  and are used to produce new light frequencies, for example, in second harmonic generation (SHG), sum and difference frequency

generation, and entangled photon pairs in spontaneous parametric down-conversion (SPDC) $^{1,2}$ .

Efficient nonlinear frequency conversion is achieved by fulfilling the so-called phase matching (PM) condition, which implies a zero wave-vector mismatch—that is, momentum conservation—for the interacting waves  $(\Delta k = 0)$ . In the following, we consider the case for SHG, but identical considerations apply for SPDC. For SHG,  $\Delta k = k_{2\omega} - 2k_{\omega} = \frac{2\omega}{c}(n_{2\omega} - n_{\omega})$  and PM requires matching

A full list of affiliations appears at the end of the paper  $\times$  e-mail: chiara.trovatello@polimi.it; lee.rozema@univie.ac.at; giulio.cerullo@polimi.it; p.j.schuck@columbia.edu

![](images/ed1bd47d72e98fba39a4f254c73ab2b035c62716cd7ac0fa1ab6003bb702f5b9.jpg)

![](images/f001d2c8029f7dc6621338340ebcc3f74b1cbc3fc1296464b0cb64deaf504198.jpg)  
Fig. 1|PPTMDs.a,b, Micrograph of the  $3\mathrm{R - MoS}_2$  flake before (a) and after (b) patterning (electron beam lithography, etching). c, Stacking procedure. Slab 1 is first transferred on a  $500 - \mu m$  -thick  $\mathrm{SiO}_2$  transparent substrate. Slab 2 is

![](images/5d5db334a4c8dbe70cf6552e93f4d109d08198de6fcf105ee80557780abc5a53.jpg)

![](images/333abef71484936e4cb2f3e3f4a73322f7ab4f7444d9ae7c2b55863a5daaffb6.jpg)

![](images/9f8ed5c61943c07438e5145e7909013a6b79a99148f9f2ed84028dc885fc6ef4.jpg)

![](images/22280f85fb1676fb4fe69d1fee2f50df6f56cdec170aaf7a38fd410e83e54372.jpg)  
twisted by  $180^{\circ}$  and released on top of slab 1. Slab 3 is transferred on top of slab 2. Finally, slab 4 is twisted by  $180^{\circ}$  and released on top of the 3 stacked portions. d, Micrographs of each stacking step. Scale bars,  $10\mu \mathrm{m}$ .

![](images/86ea80b143a71b6605d22d86c2e71f8fac34c3977798e774363a579d87a8d454.jpg)

![](images/4df98b2a19a7f83ddf97e9801ac34bbe711befb335d470088acdf43244a066e4.jpg)

![](images/5d17002febd2424ab8da4318e20996c7189315fbdb64dab429d20346e2f3ef95.jpg)

![](images/f59778fa993ec13fc48698e02f1c89a5dec60b89ef908c24b03015f4a8eb4fd8.jpg)

the refractive indexes of the fundamental wavelength (FW),  $n_{\omega}$ , and of the second harmonic (SH),  $n_{2\omega}$ . In the absence of PM, the conversion efficiency reaches its maximum for a propagation distance corresponding to the coherence length  $L_{\mathrm{c}} = \pi /\Delta \mathrm{k}$  and then oscillates with period  $2L_{\mathrm{c}}$  (ref. 1). Birefringent phase-matching (BPM) exploits the optical anisotropy of non-centrosymmetric nonlinear crystals by adjusting the propagation direction inside the crystal so that the fields at  $\omega$  and  $2\omega$  with different polarizations experience the same refractive index. For SHG with BPM, the SH intensity  $I_{2\omega}$  grows quadratically with the thickness  $L$  of the nonlinear medium. While BPM is simple and effective, it can only be applied to a limited number of crystals, such as the prototypical  $\beta$ -barium borate (BBO), which show moderate  $\chi^{(2)}$  values of a few pm  $\mathrm{V}^{-1}$  (ref. 1).

There are many crystals with high nonlinearity but low anisotropy, for example, gallium arsenide (GaAs), for which BPM is not achievable. An alternative to BPM is quasi-phase-matching (QPM), which introduces periodic phase shifts of  $\pi$  between the fields at the FW and the SH at every coherence length  $L_{c}$ , restoring the proper phase relationship and the quadratic growth of the SH intensity with propagation length $^{3,4}$ .

Such a phase shift can be obtained by periodic inversion of the crystallographic orientation during material growth via molecular beam epitaxy $^{5-7}$  or by cleaving the nonlinear medium slabs along the different crystal planes and diffusion-bonding them into monolithic stacks $^{7-9}$ . In ferroelectric crystals such as lithium niobate  $(\mathrm{LN})^{10,11}$ , lithium tantalate $^{12}$  or potassium titanyl phosphate $^{13}$ , QPM can be achieved by periodic poling, that is, by periodically inverting the sign of the nonlinear coefficient  $\chi^{(2)}$  upon high-voltage switching of ferroelectric domains following lithographic patterning of the electrodes $^{14}$ . The spatial modulation of  $\chi^{(2)}$ , which follows the electrode spacing, is the so-called poling period, and it determines the frequencies for which a certain nonlinear process can be phase matched. For LN, the typical values of the poling periods are between  $5\mu \mathrm{m}$  and  $50~{\mu\mathrm{m}}$ , and the modulation can be extended over crystal thicknesses from millimetres to centimetres $^{14}$ .

The invention of QPM was a breakthrough in nonlinear optics because it enabled the use of nonlinear crystals with large  $\chi^{(2)}$  of the order of  $30 - 50\mathrm{pmV}^{-1}$ , for which BPM cannot be achieved[15]. Periodically poled LN (PPLN) crystals provide the highest conversion efficiency for waveguided SHG  $(I_{2\omega} / I_{\omega}\approx 70\%)$ [16,17], optical parametric amplifiers and oscillators[18-21] and entangled photon sources[22,23]. Along with their high conversion efficiencies, standard nonlinear crystals such as PPLN can be directly fabricated on silicon-based optical circuits, although their millimetre-to-centimetre thickness limits the number of devices that can be integrated on a single chip. This has spurred recent advances in the development of nonlinear metasurfaces[24-28],

thin films $^{29}$  and nanowaveguides $^{30}$ , which are now leading a paradigm shift towards more miniaturized, and more tunable, nonlinear optical device platforms.

The rise of quantum and two-dimensional material science $^{31-36}$  has inspired research on less traditional classes of optical crystals, including semiconducting transition metal dichalcogenides (TMDs), for example,  $\mathrm{MoS}_2$ ,  $\mathrm{MoSe}_2$ ,  $\mathrm{WS}_2$  and  $\mathrm{WSe}_2$ . These are layered materials comprised of crystalline sheets with strong in-plane covalent bonds but weak out-of-plane van der Waals interactions. Starting from the first reports of  $\mathrm{SHG}^{37-39}$ , their exceptional optical nonlinearities  $(\chi^{(2)} = 100 - 1,000\mathrm{pmV^{-1}})$ , up to  $100\times$  higher than standard bulk crystals owing in part to favourable quantum metrics, have recently been exploited to demonstrate nonlinear effects at the ultimate thinness limit in single-layer TMDs $^{40-43}$ . However, in such cases, the overall conversion efficiency is still limited by the sub-nm propagation length $^{44}$ . In contrast to the most common 2H crystallographic phase, which is centrosymmetric in the bulk  $(\chi^{(2)} = 0)$ , the 3R polytype is non-centrosymmetric  $(\chi^{(2)}\neq 0)$  and can be used to boost the conversion efficiency of second-order nonlinear optical processes by increasing the number of layers  $N$  in the TMD sample. Using thin 3R- $\mathrm{MoS}_2$  flakes (1-6 layers), it has been shown that the SH intensity grows quadratically with the number of layers, that is, with the thickness of the nonlinear medium  $(I_{\mathrm{SHG}}\propto N^2)^{45}$ .

However, when the number of layers is increased to  $\sim 200 - 300$ , the wave-vector mismatch  $\Delta k$  results in an inevitable deviation from the  $N^2$  enhancement $^{46,47}$ , and the SH oscillates with the sample thickness, with a semi-period equal to the coherence length  $L_{\mathrm{c}}$  (ref. 1). Recently, the coherence length  $L_{\mathrm{c}}$  in 3R-MoS $_2$  has been measured at telecom wavelengths $^{47}$ . At  $L_{\mathrm{c}}$  ( $\sim 500 \mathrm{~nm}$ ), the SHG efficiency is  $1.5 \times 10^{4}$  higher than for a monolayer ( $I_{2\omega} / I_{\omega} \approx 10^{-6}$ ), resulting in the highest conversion efficiency per unit length reported so far for a transparent material $^{47}$ . Further increasing this value to achieve macroscopic nonlinear conversion efficiencies, while still preserving the micrometre thickness of TMD crystals, remains an open challenge.

Here we bridge this gap using a non-centrosymmetric van der Waals crystal,  $3\mathrm{R - MoS}_2$  to achieve QPM in periodically poled transition metal dichalcogenides (PPTMDs) at the relevant telecommunications wavelengths. We flip the sign of the optical nonlinearity  $\chi^{(2)}$  by stacking consecutive slabs with opposite dipole orientation, obtaining programmable microstacks with thickness-tunable phase-matching bandwidths. The large nonlinearity of TMDs combined with QPM unlocks single-pass conversion efficiencies for SHG of  $0.03\%$  at telecom wavelengths over only 3 poling periods, that is, a microscopic thickness of  $3.4~{\mu\mathrm{m}}$ . We observe cavity effects prompted by internal reflections of both FW and SH, which increase the conversion

![](images/803b920282e580decbc993c4bc61a557c2928af933fb8fd1386156f820afb32a.jpg)  
a

![](images/28c03e2fe1ac2af5f634a5164a8087e5248b378eae3d1edfb884842f2d66894c.jpg)  
Fig. 2 | Quasi-phase-matched SHG from PPTMDs. a, Transmission microscope. The PPTMD is excited by the FW from the back side of the  $\mathrm{SiO}_2$  substrate with a  $40\times$  objective. The SH is collected by a  $50\times$  objective. b, Pump wavelength-dependent normalized (norm.) SH maps of the PPTMD, along with the SH spectra and the SHG enhancement factor with respect to the bare slab. The  
error bar represents the standard deviation of the SH intensity over 20 pixels (1 pixel = 1  $\mu$ m × 1  $\mu$ m) of each corresponding slab area. Data are presented as mean values of the SH intensity over 20 pixels of each corresponding slab area. Scale bars, 10  $\mu$ m.

efficiency by an additional  $50\%$  over standard QPM. Finally, we report efficient broadband generation of photon pairs at telecom wavelengths via quasi-phase-matched SPDC, showcasing a maximum coincidence-to-accidental ratio (CAR) of  $638 \pm 75$ , which outperforms by almost two orders of magnitude any microscopic SPDC source based on van der Waals crystals reported so far[31,48].

The  $3\mathrm{R - MoS}_2$  crystals are mechanically exfoliated from a commercial bulk  $3\mathrm{R - MoS}_2$  crystal (HQ graphene) grown by chemical vapour transport on a  $\mathrm{SiO}_2 / \mathrm{Si}$  substrate. Characterization of the bulk crystal by energy-dispersive X-ray analysis and X-ray diffraction is provided in ref. 47. The thickness of the exfoliated flakes is measured using atomic force microscopy (Supplementary Note 4). To fabricate the PPTMD, we select a large flake with a lateral size of  $\sim 100~{\mu\mathrm{m}}$  and a thickness of  $\sim 300\mathrm{nm}$ , shown in Fig. 1a. We pattern the flake into smaller portions (Fig. 1b and Supplementary Note 1 for details) using a modified CMOS process, that is, electron beam lithography followed by reactive ion etching, the standard in large-scale device production. TMDs are readily dry etched with  $\mathrm{SF}_6$ -based reactive ion etching, which does not require hard mask and achieves high-quality side walls (see atomic force microscopy profiles of the patterned slabs in Supplementary Note 4). By cutting the different slabs out of a single flake, we ensure that all areas have identical thickness and the same macroscopic dipole orientation. Our design and fabrication methodology thus bypasses the need for angle-resolved SHG for crystal orientation characterization.

We choose a flake with thickness of  $L_{\mathrm{f}} \approx 300 \mathrm{~nm}$ , close to the coherence length  $L_{\mathrm{c}}$  measured for a FW at  $1,450 \mathrm{~nm}$  (Supplementary Note 7). The largest portion of the flake (area 1) is transferred onto a

500-μm-thick transparent fused silica  $(\mathrm{SiO}_2)$  substrate, and the other portions (areas 2, 3 and 4) are individually stacked on top of each other by keeping an interlayer twist angle of  $180^{\circ}$  (ref. 49) (symmetrically equivalent to  $60^{\circ}$  and  $300^{\circ}$  twist angles) to flip the sign of  $\chi^{(2)}$  at each coherence length (Fig. 1c), resulting in an overall thickness of  $\sim 1.2~\mu \mathrm{m}$  (Supplementary Note 4). The microscope images of the periodically poled crystal at each stacking step are shown in Fig. 1d.

To characterize the nonlinear response of the PPTMD, we use a custom-built transmission microscope (Fig. 2a), illuminated by an optical parametric oscillator (OPO, Coherent Chameleon), emitting 200 fs pulses at  $80\mathrm{MHz}$  , tunable in the near-infrared  $(1,000 - 1,600\mathrm{nm})$  wavelength range. We use a long working-distance  $40\times$  reflective objective with numerical aperture (NA) 0.5 to focus the FW on the sample from the backside of the substrate. The SH is collected by a  $50\times$  objective with a 0.95 NA and directed onto a silicon charge-coupled device camera (Supplementary Note 2). The FW is tuned from  $1,430~\mathrm{nm}$  to  $1,580~\mathrm{nm}$  and the power is kept fixed at  $0.5\mathrm{mW}$  (peak power  $1.17\mathrm{GWcm}^{-2}$  Figure 2b shows the pump wavelength-dependent normalized SHG intensity maps, along with the corresponding SHG spectrum. For each pump wavelength, we extract the SH enhancement factor, defined as the SH emission intensity from the regions with 2, 3 and 4 slabs normalized to the SH emission intensity of 1 slab, shown in Fig. 2b. The peak of the SH enhancement is obtained at  $\mathrm{FW} = 1,460\mathrm{nm}$  ,at approximately the target operation wavelength for this stack. Compared with a standard first-order QPM  $(\chi^{(2)}$  flipped in sign at each coherence length) that predicts a quadratic enhancement of 4, 9 and 16 for 2, 3 and 4 slabs, respectively, the peak enhancement that we obtain is not monotonically

![](images/6366ce7a9c1dd1f18ca80746474fa27c25acb3d3cb65720d9c327aa9f89fbb4c.jpg)

![](images/670e29f7b4c4c7ab94eb788a8c1b6add480fb655a1150e91648c7fe18062e9c0.jpg)

![](images/72202dc366417f8c2dd3eb74f398a54236dfac374bae168b91026ea158b915cc.jpg)

![](images/a56a682c879c2816bf9a2ca778515d699894cef55648d1f90255a3dae4ffb644.jpg)  
Fig. 3 | Theoretical simulations of QPM in PPTMDs. a, Schematic of the simulated PPTMD structure. Multiple reflections of FW and SH fields are shown in orange and purple, respectively. The inversion of the electric field at each coherence length is induced by  $\chi^2$  flipped in sign via twist-controlled stacking of consecutive slabs. b, Experimental (Exp.) SH enhancement for different wavelengths and number of slabs, as shown in Fig. 2. c, Corresponding SH enhancement extracted from the model. d, Quantitative comparison of the wavelength-dependent enhancement between experiment and model for different numbers of slabs, that is, cross sections of b and c, respectively. The

![](images/725d669be4adfd6075bdf57fa1e50a3eb0227f036bcc448108c3882178f68702.jpg)  
error bar represents the standard deviation of the SH intensity over 20 pixels (1 pixel = 1  $\mu$ m × 1  $\mu$ m) of each corresponding slab area, as extracted in Fig. 2. Data are presented as mean values of the SH intensity over 20 pixels of each corresponding slab area. e,f, Calculated SH intensity as a function of slab thickness and number of slabs at FW = 1,450 nm and 5 GW cm $^{-2}$  intensity, in two cases: with interference effects of the FW (e) and without interference (f). The maximum intensity achievable as a function of the total number of slabs in the PPTMD is shown on the right, showing that interference boosts SHG, owing to intrinsic cavity-induced enhancements.

increasing with the slab number at each pump wavelength, and it is almost  $50\%$  higher in the portion of the stack with 4 slabs. This effect can be explained by considering the modulation of the optical properties caused by interference inside the PPTMD<sup>50</sup>. Owing to the large refractive index of 3R- $\mathrm{MoS}_2$ , ranging between 4 and 5.5 (ref. 47), multiple reflections of FW and SH radiation at the interfaces between the TMD and the air and glass substrate, acting as optical microcavities, provide nonlinear cavity enhancement effects.

To better understand the unconventional QPM regime that we observe in PPTMDs, we analytically model our signal by solving the coupled nonlinear equations considering the interference of FW and SH fields in the slabs, and the SH electric field sign inversion for the different poling conditions (Supplementary Note 6). Specifically, we assume that the SH process does not affect the intensity of the FW (undepleted-pump approximation), and we apply the boundary conditions at the entrance and the exit of the TMD slabs to analytically retrieve the interference effects. Calculating the forward and backward propagating FW electric fields and considering the poling, we are able to evaluate the SH in the system. We calculate the second-order nonlinear polarization in the slabs at  $2\omega$  induced by FW propagation and insert this term into Maxwell's equations to extract the SH electric and magnetic fields. Applying again the boundary condition for the SH,

we obtain the forward emitted SH intensity. The analytical calculation is performed, assuming a normal propagation in the different slabs. A sketch of the modelled structure is shown in Fig. 3a, in which the interference effects of FW and SH are depicted.

Figure 3b,c shows the measurements and the theoretical simulations of the SH enhancement factor (that is, SH emission from slabs 2, 3 and 4 normalized to the SH from slab 1) as a function of the SH wavelength and the number of slabs, respectively. For the theoretical simulations, we use  $|\chi^{(2)}| = 100\mathrm{pmV}^{-1}$  and a slab thickness equal to  $293\mathrm{nm}$  (Supplementary Note 6). Figure 3d shows the comparison between experiments and theory for poled structures with 2, 3 and 4 slabs, demonstrating a very good agreement with the data. The theoretical model also accurately reproduces the nonlinear response of PPTMDs with different poling periods (Supplementary Note 8). Data and simulations emphasize the importance of an appropriate choice of the number of slabs for each FW wavelength and a given slab thickness, to maximize the enhancement of SH. In particular, for our  $300\mathrm{nm}$  slab thickness, a configuration with 3 slabs provides a higher enhancement compared with the poled structure with 4 slabs for SH wavelengths above  $750\mathrm{nm}$ .

Figure 3e shows the intensity profile of SH for different slab thicknesses and number of slabs. The results show a maximum efficiency for

![](images/624bd66761ed1d4c1581b9ed7f18f0347d6f06971b3100b88a4443158343eb20.jpg)  
a

![](images/8041aefdc3c7047d9c54e35cd7cbb59026573f8d5f3377d372573959aec28f59.jpg)  
b  
Fig. 4 | PPTMD second harmonic conversion efficiency, a, Picture of the SHG spot at  $530\mathrm{nm}$ , and close-up of the tunable SH from  $400\mathrm{nm}$  to  $625\mathrm{nm}$ . b,c, Broadband SH conversion efficiency  $(I_{2\omega} / I_{\omega})$  with tunable pump wavelength  $(1,200 - 1,590\mathrm{nm})$  measured on the PPTMD with a slab thickness of  $300\mathrm{nm}$  (b)

![](images/54b6cabdb22be7b5f192f0fbe8e418f8ce8f63a1826a88474dabac85072a24a1.jpg)  
C  
(QPM resonance  $1,460\mathrm{nm}$ ) and PPTMD with a slab thickness of  $570\mathrm{nm}$  (c) (QPM resonance  $1,530\mathrm{nm}$ ). The pump power  $40\mathrm{mW}$  (b) (peak power  $98\mathrm{GWcm}^{-2}$ ) and  $52\mathrm{mW}$  (c) (peak power  $127\mathrm{GWcm}^{-2}$ ). Insets: exemplary normalized SHG intensity maps of the PPTMDs. Scale bars,  $10\mu \mathrm{m}$ .

a  $L_{\mathrm{f}} \sim 350 \mathrm{~nm}$ , with a strong dependence on the interference effects of the FW. The optimum poling period is strongly dependent on the FW. For instance, at  $1,550 \mathrm{~nm}$ , the maximum efficiency is achieved for  $L_{\mathrm{f}} \sim 550 \mathrm{~nm}$  (Supplementary Note 6). We also report the same simulation removing the interference of the FW in the slab (Fig. 3f), which we achieve by setting the real part of refractive index of air after the slabs equal to that of the TMD. In this case, the interference pattern is removed, obtaining a more homogeneous profile. However, the maximum efficiency is notably reduced (more than  $10 \times$  lower). This comparison highlights the key role played by the intrinsic cavity enhancement effects in PPTMDs.

To quantitatively measure the conversion efficiency of our PPTMD samples, we measure the pump wavelength-dependent SH power. We use the frequency-tunable OPO as the laser source. The photographs of the broadly tunable SH spots emitted from the  $1.2\text{-}\mu \mathrm{m}$  -thick PPTMD are shown in Fig. 4a. Owing to the macroscopic efficiencies of our PPTMDs (the SH reaches  $\sim 10~\mu \mathrm{W}$  powers at the phase-matching bandwidth; Supplementary Note 9), the SH power has been measured using a standard, spectrally calibrated, silicon power meter (Thorlabs S120VC). To show

that we can realize highly efficient and programmable microstacks with tunable phase matching, we measure the SH power emitted by two different PPTMD samples: the 4-stack PPTMD (2 poling periods) with a slab thickness of  $300\mathrm{nm}$  and a second 6-stack PPTMD (3 poling periods) with a slab thickness of  $570\mathrm{nm}$  (micrograph of the 6-stack PPTMD and SH spatial mapping are shown in Supplementary Fig. 8, Supplementary Note 9). Each sample is excited with tunable pump wavelength and a constant pump power. Figure 4b,c shows the conversion efficiency, that is, SH power/FW power, of the PPTMD with slab thicknesses of  $300\mathrm{nm}$  and  $570\mathrm{nm}$ , respectively. The QPM resonance is peaked at  $1,460\mathrm{nm}$  (Fig. 4b) and  $1,530\mathrm{nm}$  (Fig. 4c), respectively, demonstrating QPM resonance tunability with the slab thickness, as well as validating the theoretical model that predicts, with very good agreement, the optimum slab thickness as a function of the FW wavelength (Supplementary Fig. 4, Supplementary Note 6).

The peak of the conversion efficiency approaches  $\sim 10^{-4}$  (that is,  $0.01\%$  at  $\mathrm{FW} = 1,460\mathrm{nm}$  for the 4-stack PPTMD (Fig. 4b) and  $0.01 - 0.1\%$  at  $\mathrm{FW} = 1,530\mathrm{nm}$  for the 6-stack PPTMD (Fig. 4c). We stress the fact that

![](images/c34fd460ec57dd9d2d02fa8abff424989551efb85aefc278cc501fbcbb389819.jpg)

![](images/ad4f703e2c3522c495bc942c8bdba1592c38c669cee216347944af65ecb2d9d3.jpg)

![](images/ca36b7aaef71bc23d18476fad2d7a61729b4923b5172e6aa2ee6ee08bba7884b.jpg)

![](images/f7960a05cd3263508ed980ce5a381ff5d75c839be4d3486115dfea2a944d1c28.jpg)

![](images/4b25363c4639c074aabc501fa78fbf48783c2eb612bf201685f24d7b4196272f.jpg)

![](images/9e8d66c3e874e511888d3c55c4403045f5aca7b4a84fa415afb61826a9a3c4ba.jpg)  
Fig. 5 | Quasi-phase-matched SPDC from PPTMDs. a, Experimental set-up. A continuous wave laser at  $780\mathrm{nm}$  is used to pump the PPTMD in a transmission geometry. The generated SPDC photons are directed to an HBT interferometer for photon-pair correlation measurements. On the right side, we plot the signature of photon-pair detection, that is, an exemplary coincidence peak at the zero delay in the arrival time histogram between the counts of two detectors. b,c, Pump power-dependent SPDC coincidence rates (dots) for the 4-stack PPTMD (b) and 6-stack PPTMD (c), with corresponding linear fits (black lines). Data points are presented as the coincidence rate averaged over the measurement time. The error bar is calculated as the Poissonian error of total coincidence events over the whole measurement. d,e, Pump power dependence of the CAR peak (dots) at the zero time delay for the 4-stack PPTMD (d) and 6-stack PPTMD (e), with corresponding hyperbolic fits (black lines). Data points are

![](images/2c8138175d4a95703059a658ded2fb9ac8c43144ccb696056ac801e4f8d0d6d6.jpg)  
presented as the coincidence rate averaged over the measurement time divided by accidental coincidence events. The error bar is calculated as the Poissonian error of total coincidence events over the whole measurement divided by accidental coincidence events. f,g, Nonlinear enhancement of measured photon coincidence rates versus number of slabs for the 4-stack PPTMD (f) and 6-stack PPTMD (g). The pump power is set to  $4\mathrm{mW}$  (f) and  $12.5\mathrm{mW}$  (g). Insets in f and g show the trends in enhancement versus number of slabs of the measured SHG signal for 4-stack and 6-stack PPTMDs, respectively. Data points are presented as the coincidence rate averaged over the measurement time, normalized to the first data point. The error bar is calculated as the Poissonian error of total coincidence events over the whole measurement, normalized to the first data point (slab 1).

![](images/ed9ea6527142da045a5d0011c9a4e213c462c00bce19bffc5f2f173917994c5b.jpg)

such macroscopic conversion efficiencies are recorded over a sample thickness of only  $1.2\mu \mathrm{m}$  and  $3.4\mu \mathrm{m}$ , respectively. PPTMDs eclipse the previous thickness-conversion efficiency trade-off curves and now show macroscopic efficiencies over microscopic thicknesses. In addition, to retrieve the QPM bandwidth as a function of the number of slabs in the PPTMD, we measure the conversion efficiency of the PPTMD phase-matched at  $1,530\mathrm{nm}$  from the portion of the sample with 4 and 5 slabs, and we compare it with the emission from the 6 slabs. The extracted full-width at half-maximum of the QPM bandwidths are

$22.4 \pm 1.4, 16.6 \pm 1.8$  and  $15.5 \pm 1.0$  for the PPTMD with 4, 5 and 6 slabs, respectively (see Supplementary Fig. 8 in Supplementary Note 9). At the QPM resonance in the relevant telecom bandwidth, the extracted nonlinearity of  $3\mathrm{R - MoS}_2$  is  $\chi^{(2)} \sim 100 \mathrm{pmV}^{-1}$  (Supplementary Note 10). With higher  $\chi^{(2)}$  compared with BBO and PPLN $^{1,50}$ , PPTMDs achieve the same efficiency, but up to  $100 \times$  shorter propagation lengths.

Finally, we use PPTMDs to demonstrate SPDC. For these measurements, we use two PPTMD samples quasi-phase-matched in the telecom C band. In particular, we use a 4-stack PPTMD with a slab thickness of

450 nm, giving the best nonlinear enhancement at 1,560 nm (Supplementary Note 10), as well as the previously shown 6-stack PPTMD with a slab thickness of 570 nm and best enhancement at 1,530 nm. To perform temporal correlation measurements in the relevant telecom wavelength range, we use a different experimental set-up that is optimized for SPDC measurements. It features a different laser source and different detectors in a transmission geometry, as depicted in Fig. 5a.

In particular, we use a continuous wave  $780\mathrm{nm}$  laser (TOPTICA) as a pump for the SPDC process. An aspheric lens  $(\mathrm{NA} = 0.68)$  and an objective  $(\mathrm{NA} = 0.85)$ , optimized for telecom wavelengths, are used to focus the pump onto the sample and collect the down-converted light, respectively. After the PPTMD, the pump beam is filtered out with three hard-coated long-pass filters with a cut-off wavelength of  $1,150\mathrm{nm}$ . In addition, we use a hard-coated band-pass filter at  $1,560\mathrm{nm} \pm 6\mathrm{nm}$ , to only collect the degenerate portion of the SPDC emission. Owing to chromatic aberration in our collection optics, this enhances our CAR. The SPDC signal is then coupled into a single mode fibre (SMF28, Corning). Photon pairs are probabilistically split into two different fibre paths using a fibre-based Hanbury Brown-Twiss (HBT) interferometer (Fig. 5a), then guided to superconducting nanowire single-photon detectors (PhotonSpot), where detection events are registered by a timetagger (Universal Quantum Devices). Analysing temporal correlations of detection events yields a timing histogram, which, when detecting photon pairs generated by SPDC, is expected to show strong correlations at zero time delay between the detectors. A histogram taken in this experimental configuration is shown on the right of Fig. 5a.

Figure 5b,c shows the coincidence rates (dots) of the 4- and 6-stack PPTMDs, respectively, as a function of the pump power. Owing to the non-negligible background, accidental coincidence events are subtracted. All error bars are calculated as the standard deviation of the measured coincidence rates. The rates follow the expected linear dependence.

Figure 5d,e shows the pump power-dependent CAR along with a hyperbolic fit. At the relevant telecom wavelength, we reach a maximum CAR value of  $638 \pm 75$ , more than one order of magnitude higher than the previously reported values in microscopic van der Waals materials at visible wavelengths, and two orders of magnitude larger at telecom wavelengths[31,48]. Replacing the band-pass filters with broadband long-pass filters (with cut-offs at  $1,300\mathrm{nm}$  or  $1,500\mathrm{nm}$ ), coincidences still show a sharp correlation peak, indicating that the SPDC process is efficient over a broad spectral range. The corresponding data is presented in Supplementary Note 11.

In Fig. 5f,g, the relative enhancement of the coincidence rates is plotted as a function of the number of slabs in the PPTMD samples. The coherence length of degenerate SPDC is the same as that for the analogous SHG process at the same wavelengths, that is, the conversion of telecom to visible wavelengths and vice versa, which has been shown to be  $\sim 500\mathrm{nm}$  (ref. 47). We observe that the coincidence rate increases with the slab number (which is proportional the thickness of the medium). Since the medium thickness exceeds the coherence length, this increase can be unambiguously attributed to QPM. The slight deviations from a monotonic increase in efficiency can be attributed to cavity effects from the etalon-like behaviour of the PPTMDs acting on the pump and the down-converted light, as also observed for SHG. The insets show the SHG enhancement converting from  $1,560\mathrm{nm}$  to  $780\mathrm{nm}$ . In the 4-stack PPTMD, with QPM resonance exactly peaked at  $1,560\mathrm{nm}$ , SPDC and SHG enhancements are in excellent agreement (Fig. 5f). The slight difference between SHG and SPDC enhancements in the 6-stack PPTMD (Fig. 5g) may be attributed to the strong dispersion of the refractive index modulating the effective interaction length of the pump light with the material. The slab-dependent coincidence rates with broadband filtering, shown in Supplementary Note 11, also show a net increase of the coincidence rate, again indicating that the SPDC process is efficient over a broad spectral range, enabled by QPM.

Finally, we compare our maximum coincidence rate with the brightest bulk sources. We take, as an example, the sources that have been used to generate 10-photon entanglement<sup>51</sup>. Normalizing their reported brightness by the square of the crystal length (since the pair-generation rate scales with the interaction length squared) yields a brightness per interaction length of  $3\mathrm{MHz}\mathrm{W}^{-1}\mathrm{mm}^{-2}$ . In our case, we observe a coincidence rate of  $\sim 4.4\mathrm{Hz}$  with a pump power of  $0.5\mathrm{mW}$ , and a total crystal thickness of  $3.42\mu \mathrm{m}$ , using broadband filtering (Supplementary Note 11). This gives us a source brightness per length of  $\sim 750\mathrm{MHz}\mathrm{W}^{-1}\mathrm{mm}^{-2}$ ,  $250\times$  larger than the best bulk SPDC sources.

Moreover, the performance of our source could be notably improved by increasing the coupling efficiency using, for example, a variety of nanofabrication technologies such as metasurfaces $^{52}$ . Although our source may be comparable to or exceed bulk sources in some figures of merit, we believe that the true strength of our platform is its compatibility with integrated on-chip components $^{53}$ . In this context, producing photon pairs directly on chip will be an enabling technology for next-generation photonic quantum devices, bypassing the loss associated with coupling each photon onto the chip $^{54}$ . This loss scales exponentially with the number of photons produced. Thus, integrating PPTMDs into this environment could address a major bottleneck in photonic quantum computing.

In conclusion, we introduce periodically poled van der Waals layered materials as a novel, micrometre-sized, programmable nonlinear platform for applications in classical and quantum light generation. To realize periodically poled microstacks, we develop a modified CMOS process—standard in large-scale device production—which makes use of electron beam lithography and reactive ion etching to directly pattern individual  $3\mathrm{R - MoS}_2$  flakes into smaller rectangular slabs with identical thickness equal to the coherence length. By periodically stacking the slabs with an interlayer twist angle of  $180^{\circ}$ , we flip the sign of  $\chi^{(2)}$  and achieve QPM, restoring the proper phase relationship between fundamental and second harmonic, and between fundamental and spontaneously down-converted fields. Although the sample has been prepared by manual exfoliation and stacking, the periodic poling process is potentially scalable, as it can be automatized using a robotic stacking machine[55] (Supplementary Note 5).

Our programmable microstacks show tunable phase matching as a function of the different poling semi-period, that is, the slab thickness. Owing to the large nonlinearity of 3R-TMDs at the relevant telecom wavelength, we demonstrate record second harmonic conversion efficiencies between  $0.01\%$  and  $0.1\%$  over a thickness of only  $3.4\mu \mathrm{m}$  (3 poling periods). Moreover, in the phase-matched interaction, we observe nonlinear enhancement, which surpasses by more than  $50\%$  the usual quadratic enhancement typically observed in standard quasi-phase-matched crystals. This is attributed to cavity effects, which enhance the field overlap inside the periodically poled structure. Theoretical simulations accurately reproduce the conditions for such an unconventional QPM and predict the optimal slab thickness as a function of the FW/SH wavelength (Supplementary Note 6). In addition, we demonstrate the generation of down-converted photon pairs via SPDC at the relevant telecom wavelength, that is,  $1,550~\mathrm{nm}$ . The reported CAR from PPTMDs reaches a maximum value of  $638\pm 75$ , the highest value observed so far in microscopic van der Waals materials[31,48].

We envision that the highest impact of our work will be in establishing a platform that enables on-chip technologies for new applications at the micrometre scale, for example, generating entangled photons through SPDC on-chip—a goal not feasible with the existing bulk crystal systems. This microscale approach removes the losses typically involved in the coupling of SPDC photons to a chip, and the efficiencies of TMDs demonstrated here render this a promising and competitive system for on-chip quantum light generation. In addition, being ultrathin (that is, well below  $1\mathrm{mm}$ ), PPTMDs do not introduce substantial light walk-off and do not require sophisticated alignment

procedures, making them robust and versatile platforms that are also stable in ambient conditions for months/years. Recently, other ultrathin van der Waals compounds have also shown remarkable SH efficiencies in the visible range (FW = 800 nm, SH = 400 nm) over micrometre thicknesses $^{56}$ , although issues with long-term stability may be present $^{31}$ , further highlighting the strengths of TMDs.

We believe that our programmable microstacks set the groundwork for realizing tunable phase-matched microscopic crystals with ultra-compact footprints. PPTMDs now provide macroscopic nonlinear conversion efficiencies over microscopic thicknesses, establishing new routes for designing novel nonlinear optical devices and quantum nanophotonic circuit elements $^{57,58}$ , such as entangled photon sources based on SPDC directly embedded on chip.

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41566-024-01602-z.

# References

1. Boyd, R. W. Nonlinear Optics (Academic, 2020).  
2. Shih, Y. An Introduction to Quantum Optics: Photon and Biphoton Physics (Taylor & Francis, 2016).  
3. Fejer, M. M., Jundt, D. H., Byer, R. L. & Magelh, G. A. Quasi-phase-matched second harmonic generation: tuning and tolerances. IEEE J. Quantum Electron. 28, 2631-2654 (1992).  
4. Myers, L. E. et al. Quasi-phase-matched optical parametric oscillators in bulk periodically poled  $\mathrm{LiNbO}_3$ . J. Opt. Soc. Am. B 12, 2102-2116 (1995).  
5. Koh, S. et al. Sublattice reversal in GaAs/Si/GaAs (100) heterostructures by molecular beam epitaxy. Jpn. J. Appl. Phys. 37, L1493 (1998).  
6. Eyres, L. A. et al. All-epitaxial fabrication of thick, orientation-patterned GaAs films for nonlinear optical frequency conversion. Appl. Phys. Lett. 79, 904-906 (2001).  
7. Grisard, A. et al. Fabrication and applications of orientation-patterned gallium arsenide for mid-infrared generation. Phys. Status Solidi C 9, 1651-1654 (2012).  
8. Gordon, L. et al. Diffusion-bonded stacked GaAs for quasiphase-matched second-harmonic generation of a carbon dioxide laser. *Electron. Lett.* **29**, 1942–1944 (1993).  
9. Tanimoto, R., Takahashi, Y. & Shoji, I. Quasi-phase-matching stack of 25 GaAs plates with high transmittance for high-power mid-infrared wavelength conversion fabricated by use of room-temperature bonding. Phys. Status Solidi C 38, (2021).  
10. Feng, D. et al. Enhancement of second-harmonic generation in  $\mathrm{LiNbO}_3$  crystals with periodic laminar ferroelectric domains. Appl. Phys. Lett. 37, (1980).  
11. Feisst, A. & Koidl, P. Current induced periodic ferroelectric domain structures in  $\mathrm{LiNbO}_3$  applied for efficient nonlinear optical frequency mixing. Appl. Phys. Lett. 47, (1985).  
12. Matsumoto, S., Lim, E. J., Hertz, H. M. & Fejer, M. M. Quasiphase-matched second harmonic generation of blue light in electrically periodically-poled lithium tantalate waveguides. Electron. Lett. 27, 2040-2042 (1991).  
13. Van Der Poel, C. J., Bierlein, J. D., Brown, J. B. & Colak, S. Efficient type I blue second-harmonic generation in periodically segmented  $\mathrm{KTiOPO_4}$  waveguides. Appl. Phys. Lett. 57, 20 (1990).  
14. Hum, D. S. & Fejer, M. M. Quasi-phasematching. C. R. Phys. 8, 180-198 (2007).  
15. Boes, A. et al. Lithium niobate photonics: unlocking the electromagnetic spectrum. Science 379, eabj4396 (2023).

16. Wang, C. et al. Ultrahigh-efficiency wavelength conversion in nanophotonic periodically poled lithium niobate waveguides. Optica 5, 1438-1441 (2018).  
17. Suntsov, S., Rüter, C. E., Bruske, D. & Kip, D. Watt-level 775 nm SHG with  $70\%$  conversion efficiency and  $97\%$  pump depletion in annealed/reverse proton exchanged diced PPLN ridge waveguides. Opt. Express 29, 11386-11393 (2021).  
18. Myers, L. E. & Bosenberg, W. R. Periodically poled lithium niobate and quasi-phase-matched optical parametric oscillators. IEEE J. Quantum Electron. 33, 10 (1997).  
19. Yang, S. T. & Velsko, S. P. Frequency-agile kilohertz repetition-rate optical parametric oscillator based on periodically poled lithium niobate. Opt. Lett. 24, 133-135 (1999).  
20. Lu, J. et al. Ultralow-threshold thin-film lithium niobate optical parametric oscillator. Optica 8, 539-544 (2021).  
21. Ledezma, L. et al. Octave-spanning tunable infrared parametric oscillators in nanophotonics. Sci. Adv. 9, eadf9711 (2023).  
22. Solntsev, A. S. et al.  $\mathrm{LiNbO}_3$  waveguides for integrated SPDC spectroscopy. APL Photon. 3, 10 (2018).  
23. Zhang, C. et al. Spontaneous parametric down-conversion sources for multiphoton experiments. Adv. Quantum Technol. 4, 2000132 (2021).  
24. Krasnok, A., Tymchenko, M. & Alù, A. Nonlinear metasurfaces: a paradigm shift in nonlinear optics. Mater. Today 21, 8-21 (2018).  
25. Wang, K., Chekhova, M. & Kivshar, Y. Metasurfaces for quantum technologies. Phys. Today 75, 3745-3763 (2022).  
26. Fedotova, A. et al. Lithium niobate meta-optics. ACS Photon. 9, 3745-3763 (2022).  
27. Santiago-Cruz, T. et al. Resonant metasurfaces for generating complex quantum states. Science 377, 991-995 (2022).  
28. Neshev, D. N. & Miroshnichenko, A. E. Enabling smart vision with metasurfaces. Nat. Photon. 17, 26-35 (2023).  
29. Zhu, S. et al. Integrated photonics on thin-film lithium niobate. Adv. Opt. Photon. 13, 242-352 (2021).  
30. Jankowski, M. et al. Supercontinuum generation by saturated second-order nonlinear interactions. APL Photon. 8, 116104 (2023).  
31. Guo, Q. et al. Ultrathin quantum light source with van der Waals  $\mathrm{NbOCl}_2$  crystal. Nature 613, 53-59 (2023).  
32. Wu, L. et al. Giant anisotropic nonlinear optical response in transition metal monopnictide Weyl semimetals. Nat. Phys. 13, 350-355 (2017).  
33. Mueller, T. & Malic, E. Exciton physics and device application of two-dimensional transition metal dichalcogenide semiconductors. npj 2D Mater. Appl. 2, 29 (2018).  
34. Du, L. et al. Moiré photonics and optoelectronics. Science 379, eadg0014 (2023).  
35. Ma, Q. et al. Photocurrent as a multiphysics diagnostic of quantum materials. Nat. Rev. Phys. 5, 170-184 (2023).  
36. Sheffer, Y., Queiroz, R. & Stern, A. Symmetries as the guiding principle for flattening bands of Dirac fermions. Phys. Rev. X 13, 021012 (2023).  
37. Malard, L. M. et al. Observation of intense second harmonic generation from  $\mathrm{MoS}_2$  atomic crystals. Phys. Rev. B. 87, 201401 (2013).  
38. Li, Y. et al. Probing symmetry properties of few-layer  $\mathrm{MoS}_2$  and h-BN by optical second-harmonic generation. Nano Lett. 13, 3329-3333 (2013).  
39. Wang, G. et al. Giant enhancement of the optical second-harmonic emission of  $\mathrm{WSe}_2$  monolayers by laser excitation at exciton resonances. Phys. Rev. Lett. 114, 097403 (2015).  
40. Autere, A. et al. Nonlinear optics with 2D layered materials. Adv. Mater. 30, 1705963 (2018).

41. Wen, X. et al. Nonlinear optics of two-dimensional transition metal dichalcogenides. Wiley Online Library 1, 317-337 (2019).  
42. Liu, W. et al. Recent advances of 2D materials in nonlinear photonics and fiber lasers. Adv. Optical Mater. 8, 1901631 (2020).  
43. Dogadov, O. et al. Parametric nonlinear optics with layered materials and related heterostructures. *Laser Photon. Rev.* **16**, 2100726 (2022).  
44. Trovatello, C. et al. Optical parametric amplification by monolayer transition metal dichalcogenides. Nat. Photon. 15, 6-10 (2021).  
45. Zhao, M. et al. Atomically phase-matched second-harmonic generation in a 2D crystal. Light Sci. Appl. 5, e16131 (2016).  
46. Shi, J. et al. 3R MoS $_2$  with broken inversion symmetry: a promising ultrathin nonlinear optical device. Adv. Mater. 29, 1701486 (2017).  
47. Xu, X. et al. Towards compact phase-matched and waveguided nonlinear optics in atomically layered semiconductors. Nat. Photon. 16, 698-706 (2022).  
48. Weissflog, M. A. et al. A tunable transition metal dichalcogenide entangled photon-pair source. Nat. Commun. 15, 7600 (2024).  
49. Hong, H. et al. Twist-phase-matching in two-dimensional materials. Phys. Rev. Lett. 131, 233801 (2023).  
50. Shoji, I., Kondo, T., Kitamoto, A., Shirane, M. & Ito, R. Absolute scale of second-order nonlinear-optical coefficients. J. Opt. Soc. Am. B 14, 2268-2294 (1997).  
51. Wang, X.-L. et al. Experimental ten-photon entanglement. Phys. Rev. Lett. 117, 210502 (2016).  
52. Kuznetsov, A. I. et al. Roadmap for optical metasurfaces. ACS Photon. 11, 816-865 (2024).

53. Datta, I. et al. Low-loss composite photonic platform based on 2D semiconductor monolayers. Nat. Photon. 14, 256-262 (2020).  
54. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019).  
55. Mannix, A. J. et al. Robotic four-dimensional pixel assembly of van der Waals solids. Nat. Nanotechnol. 17, 361-366 (2022).  
56. Abdelwahab, I. et al. Giant second-harmonic generation in ferroelectric  $\mathrm{NbO}_2$ . Nat. Photon. 16, 644-650 (2022).  
57. Elshaari, A. W. et al. Hybrid integrated quantum photonic circuits. Nat. Photon. 14, 285-298 (2020).  
58. Li, H. et al. Probing dynamical symmetry breaking using quantum-entangled photons. Quantum Sci. Technol. 3, 015003 (2017).  
59. Trovatello, C. et al. Quasi-phase-matched up- and down-conversion in periodically poled layered semiconductors. Zenodo https://doi.org/10.5281/zenodo.13987619 (2024).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2025

$^{1}$ Department of Mechanical Engineering, Columbia University, New York, NY, USA.  $^{2}$ Dipartimento di Fisica, Politecnico di Milano, Milano, Italy.  $^{3}$ CNR-SPIN, c/o Dipartimento di Scienze Fisiche e Chimiche, L'Aquila, Italy.  $^{4}$ Department of Physics, Columbia University, New York, NY, USA.  $^{5}$ Faculty of Physics, Vienna Center for Quantum Science and Technology (VCQ), University of Vienna, Vienna, Austria.  $^{6}$ Faculty of Physics and Vienna Doctoral School in Physics, University of Vienna, Vienna, Austria.  $^{7}$ Pritzker School of Molecular Engineering, University of Chicago, Chicago, IL, USA.  $^{8}$ Department of Chemistry, Columbia University, New York, NY, USA.  $^{9}$ James Franck Institute, University of Chicago, Chicago, IL, USA.  $^{10}$ Department of Chemistry, University of Chicago, Chicago, IL, USA.  $^{11}$ Christian Doppler Laboratory for Photonic Quantum Computer, University of Vienna, Vienna, Austria.  $^{12}$ Department of Physical and Chemical Sciences, University of L'Aquila, L'Aquila, Italy.  $^{13}$ Istituto di Fotonica e Nanotechnologie, Consiglio Nazionale delle Ricerche, Milano, Italy.  $^{\text{e}}$ e-mail: chiara.trovatello@polimi.it; lee.rozema@univie.ac.at; giulio.cerullo@polimi.it; p.j.schuck@columbia.edu

# Data availability

All data generated or analysed during this study that support the plots within this paper and other findings of this study are available via Zenodo at https://doi.org/10.5281/zenodo.13987619 (ref. 59). Source data are provided with this paper.

# Acknowledgements

We thank B. Ursprung for the useful discussions. This work was supported by Programmable Quantum Materials, an Energy Frontier Research Center funded by the US Department of Energy, Office of Science, Basic Energy Sciences, under award DE-SC0019443. C.T. acknowledges the European Union's Horizon Europe research and innovation programme under the Marie Skłodowska-Curie PIONEER HORIZON-MSCA-2021-PF-GF grant agreement no. 101066108. C.T. also acknowledges the Optica Foundation and Coherent Inc. for supporting this research through the Bernard J. Couillaud Prize 2022. G.C. acknowledges support by the Progetti di ricerca di Rilevante Interesse Nazionale (PRIN) of the Italian Ministry of Research 2022HL9PRP Overcoming the Classical limits of ultRafast spEctroSCopy with ENtangleD phOtons (CRESCENDO). C.T. and G.C. acknowledge funding from the European Union-NextGenerationEU under the National Quantum Science and Technology Institute (NQSTI) grant no. PE00000023-q-ANTHEM-CUP H43C22000870001. A.M. acknowledges funding from the European Union-NextGenerationEU under the Italian Ministry of University and Research (MUR) National Innovation Ecosystem grant no. ECS00000041-VITALITY-CUP E13C22001060006, and Progetti di ricerca di Rilevante Interesse Nazionale (PRIN) of the Italian Ministry of Research PHOTO (Photonic Terahertz devices based on topological materials) no. 316 2020RPEPNH. A.Y. acknowledges support from the Department of Defense (DoD) through the National Defense Science and Engineering Graduate (NDSEG) Fellowship Program. J.P. acknowledges funding from the Air Force Office of Scientific Research (FA9550-21-1-0323) and the Office of Naval Research (NO00142212841). P.W. acknowledges support from the Air Force Office of Scientific Research under award number FA8655-20-1-7030

(PhoQuGraph) and FA8655-23-1-7063 (TIQI). This research was funded in whole or in part by the Austrian Science Fund (FWF) (10.55776/ F71). The financial support by the Austrian Federal Ministry of Labour and Economy, the National Foundation for Research, Technology and Development and the Christian Doppler Research Association is gratefully acknowledged. L.A.R. acknowledges support from the Erwin Schrödinger Center for Quantum Science and Technology (ESQ Discovery).

# Author contributions

C.T., G.C., and P.J.S. conceived the experiment. C.T. also conceived of the design and realization of the samples and performed the measurements. C.F. and A.M. developed the theory model. J.B., B.B., C.T. and P.K.J. performed the spontaneous parametric down-conversion measurements. B.Y., C.T., Z.H.P., X.X. and A.Y. prepared the samples. X.X., C.T. and Z.H.P. built the experimental set-up and performed the morphological characterization of the samples. M.D., D.N.B., J.P., L.A.R., P.W., C.R.D., G.C. and P.J.S. supervised the study. C.T. wrote the paper with input from all authors.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41566-024-01602-z.

Correspondence and requests for materials should be addressed to Chiara Trovatello, Lee A. Rozema, Giulio Cerullo or P. James Schuck.

Peer review information Nature Photonics thanks Maria Chekhova, Christiano de Matos, Qing Zhang and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at

www.nature.com/reprints.