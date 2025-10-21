# Direct Observation of Phase-Free Propagation in a Silicon Waveguide

Orad Reshef,\*, Philip Camayd-Muñoz, Daryl I. Vulis, Yang Li, Marko Lončar, and Eric Mazur

John A. Paulson School of Engineering and Applied Sciences, Harvard University, 9 Oxford Street, Cambridge, Massachusetts 02138, United States

Supporting Information

ABSTRACT: We demonstrate silicon waveguides that support phase-free propagation in the telecom regime. These waveguides have smaller footprints and exhibit improved energy transfer capabilities as compared to previous optical waveguides that support phase-advance-free modes. We measure the effective refractive index using on-chip interferometry and observe a zero-crossing around a wavelength of  $\lambda = 1625\mathrm{nm}$ . At this wavelength, we observe the coherent oscillations of waves that span the entire length of the waveguide. These waveguides are based on a 220-nm-thick silicon-on-insulator platform and, thus, are inherently compatible with established silicon photonic technologies.

![](images/4dda895ceb07fdf5c4bf0dba250e40b18bec9085ece275bebe5d07743e95bcf0.jpg)

KEYWORDS: silicon photonics, nanophotonics, metamaterials, zero refractive index, interferometry

Optical waveguides provide a mechanism to tailor the characteristics of electromagnetic waves. Since the refractive index of propagating modes depends on the geometry of the waveguide, the design of nanostructured waveguides offers enormous flexibility for integrated optics. This ability to precisely define the refractive index and dispersion profile of an optical waveguide is critical to photonic applications, where dispersion engineering has been used to achieve slow light propagation $^{1-3}$  and plays a crucial role in determining phase-matching conditions for nonlinear optics. $^{4-9}$

Nanostructuring can even push the index to extreme limits. Exotic physical phenomena emerge when the effective refractive index  $n_{\mathrm{eff}}$  of a waveguide approaches zero. A material with a refractive index of zero exhibits an infinite wavelength and phase-free propagation. $^{10-12}$  These properties open up low-index media for applications in supercoupling, $^{12-14}$  in quantum optics, $^{15}$  and in beam-steering $^{16}$  and allow for dramatic nonlinear optical effects. $^{17-19}$  Phase-free propagation can be realized in photonic crystals $^{3,20}$  or plasmonic waveguides operating near the cutoff frequency. $^{21,22}$  However, such zero-index waves are accompanied by slow light effects associated with low power flow and poor coupling. $^{23}$  This connection is a consequence of the dispersion at cutoff, where the group velocity goes to zero, resulting in no energy transport.

Here, we present a zero-index platform in a corrugated silicon waveguide. These waveguides demonstrate phase-free propagation in the telecom regime ( $\lambda = 1625 \mathrm{~nm}$ ) and exhibit excellent coupling to traditional dielectric waveguides (<0.15 dB/interface). To characterize the propagating modes, we perform on-chip interferometry and extract the effective index by directly imaging stationary waves using a standard free-space objective lens. Most strikingly, at the zero-index

wavelength, we observe the coherent oscillations of waves that span the entire length of the waveguide. Measurements of transmission through these waveguides indicate efficient power transfer via the zero-index mode.

Our work is inspired by recent implementations of integrated Dirac-cone metamaterials.[24-30] Such metamaterials can be realized as two-dimensional slab structures monolithically structured from a standard silicon-on-insulator substrate and have been used to tune the effective refractive index down to arbitrarily small values, even crossing zero, while maintaining a finite group index.[28,29]

The waveguide consists of a single row of the zero-index metamaterial with a lattice constant of  $a = 760 \, \mathrm{nm}$  and a cylindrical hole with a radius of  $r = 212 \, \mathrm{nm}$ . The unit cell from ref 29 is reconfigured to place the hole at its sides, resulting in a corrugated waveguide (Figure 1a). Eigenmode analysis of the waveguide (Figure 1b) yields a single propagating mode with an effective refractive index that transitions smoothly through zero with a finite group index due to the presence of both electric and magnetic dipole resonances (see Supporting Information, waveguide design). This configuration couples efficiently to standard silicon ridge waveguides, allowing efficient power transfer into zero-index modes. Because the modes in this structure operate above the light line, they exhibit moderate radiative losses. However, we may reduce the propagation loss of these waveguides by cladding them with photonic band gap materials (PBG) consisting of a periodic array of holes in a silicon slab (see Supporting Information, addition of PBG cladding).

Received: July 13, 2017

![](images/5eda052f13f1f8d1738282c1b669fe062876b7fbc66aae0f0de5ee7b36774617.jpg)  
Figure 1. (a) Schematic of a silicon-based zero-index waveguide. (b) Simulated effective refractive index and group index for the zero-index waveguide. In contrast to other phase-free propagation structures, the group index remains finite throughout the wavelength operation range. (c) Scanning electron microscope image of a fabricated zero-index waveguide surrounded by a photonic band gap material.

![](images/9fecc0aa1a314ccbc214512eeea55b57b5508b1014b505539441d3bb2fc105ed.jpg)

![](images/623a7e599a1541643880fd77fbfbd84e3f2993fcc663400d5b19fe2015048417.jpg)

The device is fabricated using standard planar fabrication methods for silicon photonic circuits (Figure 1c). We characterize the waveguide by measuring the propagation constant  $\beta$  of the guided mode, which can be expressed as a function of the effective refractive index  $\beta = (2\pi n_{\mathrm{eff}} / \lambda)$ . While there exist several methods to determine the index of bulk or planar metamaterials,[10,26,28,32] these approaches are not applicable to one-dimensional propagation. Characterization of such a structure typically relies on complex interferometric structures instead.[25,33,34] However, an elegant alternative is available when the index is sufficiently low ( $|n| < 1$ ): we may directly observe the effective wavelength by imaging a standing wave within the waveguide.[20,22]

We form a standing wave within the waveguide by exciting it on both ends simultaneously (Figure 2). The intensity formed

![](images/e47785b72be6312e52cc0207c7410ec3512ad18916a7d276abe92e35d236f6f9.jpg)  
Figure 2. (a) A standing wave is formed when light enters coherently from both sides, which can be imaged directly in a low-index waveguide. The distance between the nodes in the standing wave is proportional to the effective wavelength. (b, c) Simulated and measured interference patterns obtained when illuminating a zero-index waveguide from both ends simultaneously with light at  $\lambda = 1495$  nm.

![](images/3c02bc2323be80ed599aee3418a5341baabf3422b0f82db392aeb1d6e50f0283.jpg)

by a pair of counter-propagating waves within a waveguide centered at  $z = 0$  is found to be

$$
I \propto \underbrace {\cos (2 \beta z + \Delta \varphi)} _ {\text {i n t e r f e r e n c e}} + \underbrace {\cosh (2 \alpha z)} _ {\text {b a c k g r o u n d}} \tag {1}
$$

where  $z$  is the propagation distance,  $\Delta \varphi$  is the relative phase between the two waves, and  $\alpha$  is the propagation loss. The first term represents the interference of the waves, while the second term corresponds to the incoherent background intensity. The resulting standing wave features regularly spaced nodes separated by a distance corresponding to  $\Delta z = (\lambda_0 / 2n_{\mathrm{eff}})$ .

Since  $n_{\mathrm{eff}}$  is typically larger than 1, the distance between successive nodes or antinodes is usually a fraction of the free-space wavelength and, therefore, below the Abbe diffraction limit  $(\approx \lambda /2)$ . In a low-index material, however, the effective wavelength is larger than the free-space wavelength, expanding subwavelength features to macroscopic scales and producing optical frequency standing waves that are resolvable using a standard free-space objective lens.

By imaging a zero-index waveguide clad with PBG from above, we experimentally observe standing waves that closely resemble the predictions from 3D full-wave simulations (Figure 2b,c). Identical standing waves are also observed in zero-index waveguides without PBG. We extract an effective wavelength from this standing wave, and thus the magnitude of the effective index, by measuring the distance between consecutive nodes in these standing waves (see Supporting Information, image analysis).

We repeat this measurement for input wavelengths ranging from 1480 to  $1680\mathrm{nm}$  to reconstruct the waveguide dispersion profile (Figure 3; for more, see Supporting Information, broadband interference spectrum). At short operating wavelengths, the standing waves have closely spaced nodes, corresponding to a short effective wavelength (i.e., high refractive index). As the wavelength increases, the node separation grows until a single antinode spans the entire waveguide around  $\lambda = 1625\mathrm{nm}$ . This trend is reversed for longer excitation wavelengths: the node separation decreases as wavelength increases. Since the standing wave evolves continuously as the wavelength is varied, we interpret these results as the dispersion of the effective index. Because this measurement is based on the effective wavelength, we are unable to distinguish between positive- and negative-index modes. However, we know from the simulation presented in Figure 1b that the waveguide mode has a positive refractive index for short wavelengths and negative index for long wavelengths. The dispersion profile extracted from the observed standing wave patterns agrees closely with the simulated index (Figure 4a). Both exhibit linear dispersion through zero index, crossing zero at approximately  $\lambda = 1625\mathrm{nm}$ . Thus, on-chip interferometry provides unambiguous confirmation of phase-free propagation.

Any direct observation of zero-index modes will be inherently limited by the extent of the guiding structure: when the effective wavelength becomes longer than twice the length of the waveguide, the standing wave patterns become indistinguishable from phase-free propagation. This size constraint is effectively a measurement floor, representing the

![](images/938b06219de88b03241d566fa081ce674f30814215e692316e5c3d03428e6581.jpg)  
Figure 3. Distance between the nodes increases as the operating wavelength approaches the zero-index wavelength ( $\lambda = 1627 \, \mathrm{nm}$ ).

![](images/3a37847cd0dc4a7c9401584833eecdfc2b5509d07c6db66ba655ef8d540f54af.jpg)  
Figure 4. (a) The absolute value of the effective refractive index of a zero-index waveguide attains a value near zero at  $\lambda = 1627\mathrm{nm}$ , in good agreement with simulated extracted indices. The error bars correspond to  $95\%$  confidence intervals yielded by the fit. The black dashed line indicates the minimum effective index that can be measured using a  $15 - \mu \mathrm{m}$ -long waveguide. (b) Propagation loss of zero-index waveguides. At the zero-index wavelength (indicated by the vertical black line), the addition of a PBG cladding reduces the propagation loss by  $30\%$ . The region shaded in gray corresponds to the wavelengths for which the index is measured to be below the limit indicated in (a).

![](images/c5d50a31abf2218ae1651311630a7ea0f0402a293fa1bfccf40e0f1cb00e3c4d.jpg)

minimum resolvable refractive index, which is indicated by the gray-shaded regions in Figure 4. The measured index is  $|n_{\mathrm{eff}}| \leq 0.03$  for  $18 \mathrm{~nm}$  surrounding  $\lambda = 1627 \mathrm{~nm}$ . The absence of a band gap allows waves to propagate with finite group velocity and power flow even at the  $\Gamma$ -point.

We can quantify the power flowing in the zero-index mode by measuring the transmission through waveguides of various lengths. This allows us to estimate the propagation loss (Figure 4b) using a cutback analysis.36 We perform the measurement for both clad and unclad waveguides and obtain propagation losses of 0.89 and  $1.26\mathrm{dB} / \mu \mathrm{m}$ , respectively, at the wavelength where  $n_{\mathrm{eff}} = 0$  (see Supporting Information, propagation losses). As there are no absorptive materials, the remaining propagation loss in clad waveguides corresponds to out-of-plane radiative coupling with continuum modes above the light line. Notably, the transmission is unchanged, and the propagation loss remains finite at the refractive index zero-crossing, providing further evidence for the lack of a band gap and corresponding slow light effects, respectively.

We have experimentally demonstrated waveguides that support phase-advance-free propagation modes based on the standard silicon-on-insulator platform. Through simultaneous electric and magnetic resonances, these modes maintain a finite group velocity even as the refractive index approaches zero, resulting in efficient power coupling to conventional dielectric waveguides. Although the current implementation is limited by propagation loss, the loss can be eliminated by creating a bound state in continuum,[37,38] which would facilitate applications in nonlinear optics. Due to its small footprint, this design is suitable for dense integration with silicon photonic circuits.

We determine the magnitude of the effective refractive index using an innovative on-chip interferometry method in which we directly image counter-propagating waves. This method is suitable for low-index devices of arbitrary shapes and can be implemented in situ without requiring additional interferometric circuitry. This experiment constitutes an additional independent proof that Dirac-cone metamaterials possess an effective refractive index of zero.

This one-dimensional implementation of zero-index metamaterials promises to expand the silicon photonics toolkit by extending the attainable values for the effective refractive index of a waveguide beyond what is conventionally permitted. Rather than a narrow range between the index of the core and the cladding, the refractive index of the waveguide can extend to values below the index of the cladding, including zero and even negative values. The design methodology outlined above can be used to extend these properties to any other desired material platform and to different operating wavelengths. Such metawaveguides provide unprecedented control over dispersion at the nanoscale.

# ASSOCIATED CONTENT

# Supporting Information

The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acsphotonics.7b00760.

Additional text with extra information on the experimental methods, the device design methodology, integration with the PBG cladding, additional discussion on propagation losses, the image analysis method,

additional measurements and a description of the appended visualizations (Figures S1-S6) (PDF)  
Visualization 1: Real-time unprocessed video taken with an infrared camera of standing waves in a  $15 - \mu \mathrm{m}$  long zero-index waveguide at a wavelength of  $1670\mathrm{nm}$  (AVI)  
Visualization 2: Same device at an operating wavelength of  $1650~\mathrm{nm}$  (AVI)  
Visualization 3: Same device at an operating wavelength of  $1630~\mathrm{nm}$  (AVI)

# AUTHOR INFORMATION

Corresponding Author

$^*\mathrm{E}$  mail: orad@reshef.ca.

ORCID

Orad Reshef: 0000-0001-9818-8491

Philip Camayd-Munoz: 0000-0002-1203-3083

Daryl I. Vulis: 0000-0002-9225-2621

Yang Li: 0000-0002-2146-6155

Eric Mazur: 0000-0003-3194-9836

Present Address

$^{\ddagger}$ Department of Physics, University of Ottawa, 25 Templeton Street, Ottawa, Ontario K1N 6N5, Canada.

Author Contributions

O.R. and P.C.M. conceived the basic idea for this work. O.R., P.C.M., D.V., and Y.L. performed the simulations, O.R. performed the fabrication and carried out the experiments, and P.C.M. analyzed the results. E.M. and M.L. supervised the research and the development of the manuscript. O.R. and P.C.M. wrote the first draft of the manuscript; all authors subsequently took part in the revision process and approved the final copy of the manuscript.

Author Contributions

†O. Reshef and P. Camayd-Muñoz contributed equally to this work.

Notes

The authors declare no competing financial interest.

# ACKNOWLEDGMENTS

The authors thank M. J. Burek for help with measurements. The research described in this article was supported by the National Science Foundation (NSF) under contract DMR-1360889. O.R. acknowledges the support of the Banting Postdoctoral Fellowship of the Natural Sciences and Engineering Research Council of Canada (NSERC). This work was performed in part at the Center for Nanoscale Systems (CNS), a member of the National Nanotechnology Coordinated Infrastructure Network (NNCI), which is supported by the National Science Foundation under NSF award no. 1541959. CNS is part of Harvard University.

# REFERENCES

(1) Notomi, M.; Yamada, K.; Shinya, A.; Takahashi, J.; Takahashi, C.; Yokohama, I. Extremely large group velocity dispersion of line-defect waveguides in photonic crystal slabs. Phys. Rev. Lett. 2001, 87, 253902.  
(2) Joannopoulos, J. D.; Johnson, S. G.; Winn, J. N.; Meade, R. D. Photonic Crystals, 2nd ed.; Princeton University Press: Princeton, NJ, 2008.  
(3) Schulz, S. A.; O'Faolain, L.; Beggs, D. M.; White, T. P.; Melloni, A.; Krauss, T. F. Dispersion engineered slow light in photonic crystals: a comparison. J. Opt. 2010, 12, 104004.  
(4) Agrawal, G. P. Nonlinear Fiber Optics, 4th ed.; Academic Press: Boston, MA, 2007.

(5) Leuthold, J.; Koos, C.; Freude, W. Nonlinear silicon photonics. Nat. Photonics 2010, 4, 535-544.  
(6) Okawachi, Y.; Saha, K.; Levy, J. S.; Wen, Y. H.; Lipson, M.; Gaeta, A. L. Octave-spanning frequency comb generation in a silicon nitride chip. Opt. Lett. 2011, 36, 3398-3400.  
(7) Lan, S.; Kang, L.; Schoen, D. T.; Rodrigues, S. P.; Cui, Y.; Brongersma, M. L.; Cai, W. Backward phase-matching for nonlinear optical generation in negative-index materials. Nat. Mater. 2015, 14, 807-811.  
(8) Gattass, R. R.; Svacha, G. T.; Tong, L.; Mazur, E. Supercontinuum generation in submicrometer diameter silica fibers. Opt. Express 2006, 14, 9408-9414.  
(9) Foster, M. A.; Moll, K. D.; Gaeta, A. L. Optimal waveguide dimensions for nonlinear interactions. Opt. Express 2004, 12, 2880-2887.  
(10) Valentine, J.; Zhang, S.; Zentgraf, T.; Ulin-Avila, E.; Genov, D. A.; Bartal, G.; Zhang, X. Three-dimensional optical metamaterial with a negative refractive index. Nature 2008, 455, 376-379.  
(11) Liberal, I.; Engheta, N. Near-zero refractive index photonics. Nat. Photonics 2017, 11, 149-158.  
(12) Silveirinha, M.; Engheta, N. Tunneling of electromagnetic energy through subwavelength channels and bends using  $\epsilon$ -near-zero materials. Phys. Rev. Lett. 2006, 97, 157403.  
(13) Silveirinha, M. G.; Engheta, N. Theory of supercoupling, squeezing wave energy, and field confinement in narrow channels and tight bends using  $\epsilon$ -near-zero metamaterials. Phys. Rev. B: Condens. Matter Mater. Phys. 2007, 76, 245109.  
(14) Hajian, H.; Ozbay, E.; Caglayan, H. Enhanced transmission and beaming via a zero-index photonic crystal. Appl. Phys. Lett. 2016, 109, 031105.  
(15) Fleury, R.; Alù, A. Enhanced superradiance in epsilon-near-zero plasmonic channels. Phys. Rev. B: Condens. Matter Mater. Phys. 2013, 87, 201101.  
(16) Memarian, M.; Eleftheriades, G. V. Dirac leaky-wave antennas for continuous beam scanning from photonic crystals. Nat. Commun. 2015, 6, 5855.  
(17) Suchowski, H.; O'Brien, K.; Wong, Z. J.; Salandrino, A.; Yin, X.; Zhang, X. Phase mismatch-free nonlinear propagation in optical zero-index materials. Science 2013, 342, 1223-1226.  
(18) Alam, M. Z.; De Leon, I.; Boyd, R. W. Large optical nonlinearity of indium tin oxide in its epsilon-near-zero region. Science 2016, 352, 795-797.  
(19) Reshef, O.; Giese, E.; Alam, M. Z.; De Leon, I.; Upham, J.; Boyd, R. W. Beyond the perturbative description of the nonlinear optical response of low-index materials. Opt. Lett. 2017, 42, 3225.  
(20) Lončar, M.; Nedeljković, D.; Pearsall, T. P.; Vucković, J.; Scherer, A.; Kuchinsky, S.; Allan, D. C. Experimental and theoretical confirmation of Bloch-mode light propagation in planar photonic crystal waveguides. Appl. Phys. Lett. 2002, 80, 1689-1691.  
(21) Edwards, B.; Alù, A.; Young, M. E.; Silveirinha, M.; Engheta, N. Experimental verification of epsilon-near-zero metamaterial coupling and energy squeezing using a microwave waveguide. Phys. Rev. Lett. 2008, 100, 033903.  
(22) Vesseur, E. J. R.; Coenen, T.; Caglayan, H.; Engheta, N.; Polman, A. Experimental verification of  $n = 0$  structures for visible light. Phys. Rev. Lett. 2013, 110, 013902.  
(23) Javani, M. H.; Stockman, M. I. Real and Imaginary Properties of Epsilon-Near-Zero Materials. Phys. Rev. Lett. 2016, 117, 1-6.  
(24) Huang, X.; Lai, Y.; Hang, Z. H.; Zheng, H.; Chan, C. T. Dirac cones induced by accidental degeneracy in photonic crystals and zero-refractive-index materials. Nat. Mater. 2011, 10, 582-586.  
(25) Moitra, P.; Yang, Y.; Anderson, Z.; Kravchenko, I. I.; Briggs, D. P.; Valentine, J. Realization of an all-dielectric zero-index optical metamaterial. Nat. Photonics 2013, 7, 791-795.  
(26) Li, Y.; Kita, S.; Muñoz, P.; Reshef, O.; Vulis, D. I.; Yin, M.; Loncar, M.; Mazur, E. On-chip zero-index metamaterials. Nat. Photonics 2015, 9, 738-742.  
(27) Jahani, S.; Jacob, Z. All-dielectric metamaterials. Nat. Nanotechnol. 2016, 11, 23-36.

(28) Kita, S.; Li, Y.; Camayd-Muñoz, P.; Reshef, O.; Vulis, D. I.; Day, R. W.; Mazur, E.; Loncar, M. On-chip all-dielectric fabrication-tolerant zero-index metamaterials. Opt. Express 2017, 25, 8326-8334.  
(29) Vulis, D. I.; Li, Y.; Reshef, O.; Camayd-Muñoz, P.; Yin, M.; Kita, S.; Lončar, M.; Mazur, E. Monolithic CMOS-compatible zero-index metamaterials. Opt. Express 2017, 25, 12381-12399.  
(30) He, X.-T.; Huang, Z.-Z.; Chang, M.-L.; Xu, S.-Z.; Zhao, F.-L.; Deng, S.-Z.; She, J.-C.; Dong, J.-W. Realization of Zero-Refractive-Index Lens with Ultralow Spherical Aberration. ACS Photonics 2016, 3, 2262-2267.  
(31) Sakoda, K. Universality of mode symmetries in creating photonic Dirac cones. J. Opt. Soc. Am. B 2012, 29, 2770-2778.  
(32) Lezec, H. J.; Dionne, J. A.; Atwater, H. A. Negative refraction at visible frequencies. Science 2007, 316, 430-432.  
(33) Kocaman, S.; Aras, M. S.; Hsieh, P.; McMillan, J. F.; Biris, C. G.; Panoiu, N. C.; Yu, M. B.; Kwong, D. L.; Stein, A.; Wong, C. W. Zero phase delay in negative-refractive-index photonic crystal superlattices. Nat. Photonics 2011, 5, 499-505.  
(34) O'Brien, K.; Lanzillotti-Kimura, N. D.; Suchowski, H.; Kante, B.; Park, Y.; Yin, X.; Zhang, X. Reflective interferometry for optical metamaterial phase measurements. Opt. Lett. 2012, 37, 4089-4091.  
(35) Abbe, E. Beiträge zur Theorie des Mikroskopics und der mikroskopischen Wahrnehmung. Archiv für mikroskopische Anatomie 1873, 9, 413-418.  
(36) O'Faolain, L.; Schulz, S. A.; Beggs, D. M.; White, T. P.; Spasenovic, M.; Kuipers, L.; Morichetti, F.; Melloni, A.; Mazoyer, S.; Hugonin, J. P.; Lalanne, P.; Krauss, T. F. Loss engineered slow light waveguides. Opt. Express 2010, 18, 27627-27638.  
(37) Hsu, C. W.; Zhen, B.; Lee, J.; Chua, S.-L.; Johnson, S. G.; Joannopoulos, J. D.; Soljacic, M. Observation of trapped light within the radiation continuum. Nature 2013, 499, 188-91.  
(38) Muñoz, P.; Kita, S.; Mello, O.; Reshef, O.; Vulis, D. I.; Li, Y.; Loncar, M.; Mazur, E. Lossless Integrated Dirac-Cone Metamaterials; CLEO: Applications and Technology: San Jose, CA, 2016; p JW2A.24.